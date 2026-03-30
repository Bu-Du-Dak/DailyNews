import html
import os
import re
from datetime import datetime, timedelta, timezone
from email.utils import parsedate_to_datetime

import requests
from dotenv import load_dotenv

load_dotenv()

CLIENT_ID = os.getenv("CLIENT_ID")
CLIENT_SECRET = os.getenv("CLIENT_SECRET")
API_URL = os.getenv("API_URL")

HEADERS = {
    "X-Naver-Client-Id": CLIENT_ID,
    "X-Naver-Client-Secret": CLIENT_SECRET,
}

MAX_RESULTS = 20
REQUEST_TIMEOUT = 10
KST = timezone(timedelta(hours=9))

CATEGORY_KEYWORDS = {
    "politics": ["대통령", "국회", "정부", "정책"],
    "economy": ["증시", "환율", "금리", "경제"],
    "society": ["사건", "법원", "교육", "의료"],
    "tech": ["AI", "반도체", "플랫폼", "테크"],
}


def strip_html(text):
    clean_text = re.sub(r"<[^>]*>", "", text or "")
    clean_text = html.unescape(clean_text)
    return re.sub(r"\s+", " ", clean_text).strip()


def normalize_title(title):
    return re.sub(r"[^0-9A-Za-z가-힣]+", "", strip_html(title)).lower()


def parse_pub_date(pub_date):
    try:
        return parsedate_to_datetime(pub_date).astimezone(KST)
    except (TypeError, ValueError):
        return datetime.now(KST) - timedelta(days=7)


def build_params(keyword):
    return {
        "query": keyword,
        "display": MAX_RESULTS,
        "sort": "date",
    }


def request_keyword_news(keyword):
    response = requests.get(
        API_URL,
        headers=HEADERS,
        params=build_params(keyword),
        timeout=REQUEST_TIMEOUT,
    )
    response.raise_for_status()
    return response.json().get("items", [])


def score_article(article):
    mentions = article.get("_keyword_hits", 1)
    category_hits = article.get("_category_hits", 1)
    published_at = parse_pub_date(article.get("pubDate"))
    age_hours = max(0.0, (datetime.now(KST) - published_at).total_seconds() / 3600)
    recency_score = max(0.0, 36 - age_hours) / 36

    # 여러 키워드/카테고리에서 반복 등장하고, 더 최신일수록 높은 점수
    return round((mentions * 1.8) + (category_hits * 1.2) + (recency_score * 3), 4)


def merge_article(target, item, keyword, category):
    target["_keyword_set"].add(keyword)
    target["_category_set"].add(category)
    target["_keyword_hits"] = len(target["_keyword_set"])
    target["_category_hits"] = len(target["_category_set"])

    candidate_date = parse_pub_date(item.get("pubDate"))
    current_date = parse_pub_date(target.get("pubDate"))

    if candidate_date > current_date:
        target["title"] = item.get("title", target.get("title", ""))
        target["description"] = item.get("description", target.get("description", ""))
        target["pubDate"] = item.get("pubDate", target.get("pubDate", ""))
        target["originallink"] = item.get("originallink", target.get("originallink", ""))
        target["link"] = item.get("link", target.get("link", ""))


def finalize_articles(articles):
    for article in articles:
        article["_score"] = score_article(article)
        article.pop("_keyword_set", None)
        article.pop("_category_set", None)

    return sorted(
        articles,
        key=lambda article: (
            article.get("_score", 0),
            parse_pub_date(article.get("pubDate")),
        ),
        reverse=True,
    )[:MAX_RESULTS]


def fetch_news():
    aggregated = {}
    successful_requests = 0

    for category, keywords in CATEGORY_KEYWORDS.items():
        for keyword in keywords:
            try:
                items = request_keyword_news(keyword)
                successful_requests += 1
                print(f"[naver] {category}/{keyword}: {len(items)}건 수집")
            except requests.exceptions.RequestException as error:
                print(f"[naver] {category}/{keyword} 수집 실패: {error}")
                continue

            for item in items:
                dedupe_key = item.get("link") or normalize_title(item.get("title"))
                if not dedupe_key:
                    continue

                if dedupe_key not in aggregated:
                    aggregated[dedupe_key] = {
                        **item,
                        "_keyword_set": {keyword},
                        "_category_set": {category},
                        "_keyword_hits": 1,
                        "_category_hits": 1,
                    }
                else:
                    merge_article(aggregated[dedupe_key], item, keyword, category)

    if successful_requests == 0:
        return None

    ranked_items = finalize_articles(list(aggregated.values()))
    print(f"[naver] 중복 제거 후 {len(ranked_items)}건 선정")

    return {
        "lastBuildDate": datetime.now(KST).strftime("%a, %d %b %Y %H:%M:%S +0900"),
        "total": len(ranked_items),
        "start": 1,
        "display": len(ranked_items),
        "items": ranked_items,
    }


if __name__ == "__main__":
    news_data = fetch_news()
    if news_data:
        print("뉴스 데이터를 성공적으로 가져왔습니다!")
        print(news_data)
    else:
        print("뉴스 데이터를 가져오지 못했습니다.")
