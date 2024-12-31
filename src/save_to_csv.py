import os
import csv
import re
import html
from datetime import datetime, timezone, timedelta


PROJECT_DIR = os.path.dirname(os.path.abspath(__file__))
NEWS_DIR = os.path.join(PROJECT_DIR, "../news")

# news 폴더 생성
if not os.path.exists(NEWS_DIR):
    os.makedirs(NEWS_DIR)
    print(f"{NEWS_DIR} 폴더를 생성했습니다.")

# 날짜 한국 시 변환
def convert_to_kst(published):
    parsed_date = datetime.strptime(published,"%a, %d %b %Y %H:%M:%S %z")
    kst_date = parsed_date.astimezone(timezone(timedelta(hours=9)))
    return kst_date.strftime("%Y-%m-%d %H:%M:%S (KST)")

# HTML 태그 제거
def clean_tag(item):
    clean_text = re.sub(r'<[^>]*>', '', item)
    clean_text = html.unescape(clean_text)
    clean_text = re.sub(r'\s+', ' ', clean_text).strip()
    return clean_text

# 파일 저장
def save_to_csv(news_data):
    today = datetime.now()
    yyyy_mm = today.strftime("%Y-%m")
    yyyy_mm_dir = os.path.join(NEWS_DIR, yyyy_mm) 
    filename = os.path.join(yyyy_mm_dir, f"{today.strftime('%Y-%m-%d')}_news.csv")
    
    if not os.path.exists(yyyy_mm_dir):
        os.makedirs(yyyy_mm_dir)
        print(f"{yyyy_mm_dir} 폴더를 생성했습니다.")

    items = news_data.get("items",[])
    with open(filename, mode="w", newline="", encoding="utf-8-sig") as file:
        writer = csv.writer(file)
        writer.writerow(["Title","Published(Kor)","Description","Link"])
        for item in items:
            writer.writerow([
                clean_tag(item["title"]),
                convert_to_kst(item["pubDate"]),
                clean_tag(item["description"]).replace('. ','./n'),
                item["link"],
            ])
    print(f"{filename}에 뉴스 데이터를 저장했습니다.")
