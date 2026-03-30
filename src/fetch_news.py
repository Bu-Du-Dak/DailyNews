from gnews_client import fetch_top_headlines

LOCAL_REQUESTS = [
    ("general", {"category": "general", "country": "kr", "lang": "ko"}),
    ("nation", {"category": "nation", "country": "kr", "lang": "ko"}),
    ("business", {"category": "business", "country": "kr", "lang": "ko"}),
    ("technology", {"category": "technology", "country": "kr", "lang": "ko"}),
]


def fetch_news():
    return fetch_top_headlines(LOCAL_REQUESTS, "local")


if __name__ == "__main__":
    news_data = fetch_news()
    if news_data:
        print("국내 뉴스를 성공적으로 가져왔습니다!")
        print(news_data)
    else:
        print("국내 뉴스를 가져오지 못했습니다.")
