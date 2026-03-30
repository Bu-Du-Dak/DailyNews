import os
from datetime import datetime, timedelta, timezone

import requests
from dotenv import load_dotenv

load_dotenv()

GNEWS_API_KEY = (
    os.getenv("GNEWS_API_KEY")
    or os.getenv("GLOBAL_API_KEY")
)

GNEWS_API_URL = (
    os.getenv("GNEWS_API_URL")
    or os.getenv("GLOBAL_API_URL")
    or "https://gnews.io/api/v4/top-headlines"
)

REQUEST_TIMEOUT = 10
KST = timezone(timedelta(hours=9))
MAX_RESULTS_PER_REQUEST = 10
FINAL_RESULTS = 20


def parse_gnews_date(published_at):
    try:
        return datetime.fromisoformat((published_at or "").replace("Z", "+00:00"))
    except ValueError:
        return datetime.now(timezone.utc) - timedelta(days=7)


def score_article(article):
    category_hits = article.get("_category_hits", 1)
    source_hits = article.get("_source_hits", 1)
    published_at = parse_gnews_date(article.get("publishedAt"))
    age_hours = max(
        0.0,
        (datetime.now(timezone.utc) - published_at).total_seconds() / 3600,
    )
    recency_score = max(0.0, 36 - age_hours) / 36

    return round((category_hits * 1.5) + (source_hits * 0.8) + (recency_score * 3), 4)


def build_article(item, bucket):
    source_name = (item.get("source") or {}).get("name", "").strip()
    return {
        "title": item.get("title", ""),
        "description": item.get("description", ""),
        "content": item.get("content", ""),
        "publishedAt": item.get("publishedAt", ""),
        "url": item.get("url", ""),
        "image": item.get("image", ""),
        "source": item.get("source", {}),
        "_category_set": {bucket},
        "_source_set": {source_name} if source_name else set(),
        "_category_hits": 1,
        "_source_hits": 1 if source_name else 0,
    }


def merge_article(existing, item, bucket):
    source_name = (item.get("source") or {}).get("name", "").strip()
    existing["_category_set"].add(bucket)
    if source_name:
        existing["_source_set"].add(source_name)

    existing["_category_hits"] = len(existing["_category_set"])
    existing["_source_hits"] = len(existing["_source_set"])

    current_date = parse_gnews_date(existing.get("publishedAt"))
    candidate_date = parse_gnews_date(item.get("publishedAt"))

    if candidate_date >= current_date:
        existing["title"] = item.get("title", existing.get("title", ""))
        existing["description"] = item.get("description", existing.get("description", ""))
        existing["content"] = item.get("content", existing.get("content", ""))
        existing["publishedAt"] = item.get("publishedAt", existing.get("publishedAt", ""))
        existing["url"] = item.get("url", existing.get("url", ""))
        existing["image"] = item.get("image", existing.get("image", ""))
        existing["source"] = item.get("source", existing.get("source", {}))


def finalize_articles(articles):
    for article in articles:
        article["_score"] = score_article(article)
        article.pop("_category_set", None)
        article.pop("_source_set", None)

    return sorted(
        articles,
        key=lambda article: (
            article.get("_score", 0),
            parse_gnews_date(article.get("publishedAt")),
        ),
        reverse=True,
    )[:FINAL_RESULTS]


def fetch_top_headlines(requests_config, label):
    if not GNEWS_API_KEY:
        print(f"[gnews] {label} 수집 실패: GNEWS_API_KEY 또는 GLOBAL_API_KEY가 없습니다.")
        return None

    aggregated = {}
    successful_requests = 0

    for bucket, params in requests_config:
        request_params = {
            **params,
            "max": MAX_RESULTS_PER_REQUEST,
            "apikey": GNEWS_API_KEY,
        }

        try:
            response = requests.get(
                GNEWS_API_URL,
                params=request_params,
                timeout=REQUEST_TIMEOUT,
            )
            response.raise_for_status()
            articles = response.json().get("articles", [])
            successful_requests += 1
            print(f"[gnews] {label}/{bucket}: {len(articles)}건 수집")
        except requests.exceptions.RequestException as error:
            print(f"[gnews] {label}/{bucket} 수집 실패: {error}")
            continue

        for item in articles:
            dedupe_key = item.get("url")
            if not dedupe_key:
                continue

            if dedupe_key not in aggregated:
                aggregated[dedupe_key] = build_article(item, bucket)
            else:
                merge_article(aggregated[dedupe_key], item, bucket)

    if successful_requests == 0:
        return None

    ranked_articles = finalize_articles(list(aggregated.values()))
    print(f"[gnews] {label} 중복 제거 후 {len(ranked_articles)}건 선정")

    return {
        "totalArticles": len(ranked_articles),
        "articles": ranked_articles,
        "fetchedAt": datetime.now(KST).isoformat(),
    }
