from gnews_client import fetch_top_headlines

GLOBAL_REQUESTS = [
    ("world", {"topic": "world", "lang": "en"}),
    ("business", {"topic": "business", "lang": "en"}),
    ("technology", {"topic": "technology", "lang": "en"}),
    ("science", {"topic": "science", "lang": "en"}),
]


def fetch_global_news():
    return fetch_top_headlines(GLOBAL_REQUESTS, "global")


if __name__ == "__main__":
    news_data = fetch_global_news()
    if news_data:
        print("글로벌 뉴스를 성공적으로 가져왔습니다!")
        print(news_data)
    else:
        print("글로벌 뉴스를 가져오지 못했습니다.")
