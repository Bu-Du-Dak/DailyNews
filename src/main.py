import os
from fetch_news import fetch_news
from fetch_global_news import fetch_global_news
from save_to_csv import save_to_csv
from git_push import git_push

PROJECT_DIR = os.path.dirname(os.path.abspath(__file__))
BASE_DIR = os.path.join(PROJECT_DIR, "../")

if __name__ == "__main__":
    # 1. 뉴스 데이터 가져오기
    news_data = fetch_news()
    global_news_data = fetch_global_news()
    # 2. 가져온 데이터를 CSV로 저장
    all_success = True
    if news_data:
        save_to_csv(news_data, base_dir=BASE_DIR, folder_name="news")
    else:
        print("뉴스 데이터를 가져오지 못했습니다.")
        all_success = False
        
    if global_news_data:
        save_to_csv(global_news_data, base_dir=BASE_DIR, folder_name="global_news")
    else:
        print("글로벌 뉴스를 가져오지 못했습니다.")
        all_success = False
        
    if all_success:
        print("모든 뉴스 데이터를 성공적으로 저장했습니다. Git에 푸시합니다.")
        git_push()
    else:
        print("일부 뉴스 데이터를 저장하지 못했습니다. Git 푸시는 생략합니다.")