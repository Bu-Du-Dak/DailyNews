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
    saved_any_data = False

    if news_data:
        try:
            save_to_csv(news_data, base_dir=BASE_DIR, folder_name="news")
            saved_any_data = True
        except Exception as e:
            print(f"국내 뉴스 저장 중 에러 발생: {e}")
    else:
        print("국내 뉴스를 가져오지 못했습니다.")

    if global_news_data:
        try:
            save_to_csv(global_news_data, base_dir=BASE_DIR, folder_name="global_news")
            saved_any_data = True
        except Exception as e:
            print(f"글로벌 뉴스 저장 중 에러 발생: {e}")
    else:
        print("글로벌 뉴스를 가져오지 못했습니다.")

    # 3. 하나라도 저장에 성공하면 Git 푸시
    if saved_any_data:
        print("저장된 뉴스 데이터가 있어 Git에 푸시합니다.")
        git_push()
    else:
        print("저장된 뉴스 데이터가 없어 Git 푸시는 생략합니다.")
