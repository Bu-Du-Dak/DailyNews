from fetch_news import fetch_news
from save_to_csv import save_to_csv
from git_push import git_push

if __name__ == "__main__":
    # 1. 뉴스 데이터 가져오기
    news_data = fetch_news()
    
    # 2. 가져온 데이터를 CSV로 저장
    if news_data:
        save_to_csv(news_data)
        git_push()
    else:
        print("뉴스 데이터를 가져오지 못했습니다.")