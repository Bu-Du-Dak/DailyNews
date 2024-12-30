import os
import csv
from datetime import datetime

PROJECT_DIR = os.path.dirname(os.path.abspath(__file__))
NEWS_DIR = os.path.join(PROJECT_DIR, "../news")

# news 폴더 생성
if not os.path.exists(NEWS_DIR):
    os.makedirs(NEWS_DIR)
    print(f"{NEWS_DIR} 폴더를 생성했습니다.")

def save_to_csv(news_data):
    today = datetime.now().strftime("%Y-%m-%d")
    filename = os.path.join(NEWS_DIR,f"{today}_news.csv")
    
    items = news_data.get("items",[])
    with open(filename, mode="w", newline="", encoding="utf-8-sig") as file:
        writer = csv.writer(file)
        writer.writerow(["Title","Published","Description","Link"])
        for item in items:
            writer.writerow([
                item["title"],
                item["pubDate"],
                item["description"],
                item["link"],
            ])
    print(f"{filename}에 뉴스 데이터를 저장했습니다.")
