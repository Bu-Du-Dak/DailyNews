import os
import csv
import re
import html
from datetime import datetime, timezone, timedelta

# HTML 태그 제거
def clean_tag(item):
    clean_text = re.sub(r'<[^>]*>', '', item)
    clean_text = html.unescape(clean_text)
    clean_text = re.sub(r'\s+', ' ', clean_text).strip()
    return clean_text

def convert_to_kst(published, folder_name):
    try:
        if folder_name == "global_news":  # NY Times 데이터
            # ISO 8601 형식 처리
            parsed_date = datetime.strptime(published, "%Y-%m-%dT%H:%M:%S%z")
        else:  # 네이버 뉴스 데이터
            # RFC 1123 형식 처리
            parsed_date = datetime.strptime(published, "%a, %d %b %Y %H:%M:%S %z")
        
        # 한국 시간(KST)으로 변환
        kst_date = parsed_date.astimezone(timezone(timedelta(hours=9)))
        return kst_date.strftime("%Y-%m-%d %H:%M:%S (KST)")
    except ValueError as e:
        print(f"날짜 변환 실패: {e} (published: {published})")
        return "Invalid Date"
    
# 파일 저장
def save_to_csv(news_data, base_dir, folder_name):
    today = datetime.now(timezone(timedelta(hours=9)))
    yyyy_mm = today.strftime("%Y-%m")
    target_dir = os.path.join(base_dir, folder_name, yyyy_mm)
    filename = os.path.join(target_dir, f"{today.strftime('%Y-%m-%d')}_news.csv")

    if not os.path.exists(target_dir):
        os.makedirs(target_dir)
        print(f"{target_dir} 폴더를 생성했습니다.")

    if folder_name == "global_news":  # NY Times 데이터
        items = news_data.get("results", [])
        title_field = "title"
        published_field = "published_date"
        description_field = "abstract"
        link_field = "url"
    else:  # 네이버 뉴스 데이터
        items = news_data.get("items", [])
        title_field = "title"
        published_field = "pubDate"
        description_field = "description"
        link_field = "link"

    with open(filename, mode="w", newline="", encoding="utf-8-sig") as file:
        writer = csv.writer(file)
        writer.writerow(["Title", "Published(Kor)", "Description", "Link"])
        for item in items:
            try:
                title = clean_tag(item[title_field])
                published = convert_to_kst(item[published_field], folder_name)
                description = clean_tag(item[description_field]).replace('. ', '.\n')
                link = item[link_field]
                writer.writerow([title, published, description, link])
            except KeyError as e:
                print(f"KeyError 발생: {e} (item: {item})")
            except Exception as e:
                print(f"Unexpected error: {e} (item: {item})")

    print(f"{filename}에 뉴스 데이터를 저장했습니다.")
