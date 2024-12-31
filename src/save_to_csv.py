import os
import csv
import re
import html
from datetime import datetime, timezone, timedelta

# 날짜 한국 시 변환
def convert_to_kst(published):
    if not published:
        print("날짜 데이터가 비어 있습니다.")
        return "Invalid Date"
    try:
        # ISO 8601 형식 (NY Times)
        if "T" in published:
            parsed_date = datetime.strptime(published, "%Y-%m-%dT%H:%M:%S%z")
        else:
            # RFC 1123 형식 (네이버)
            parsed_date = datetime.strptime(published, "%a, %d %b %Y %H:%M:%S %z")
        
        # KST로 변환
        kst_date = parsed_date.astimezone(timezone(timedelta(hours=9)))
        return kst_date.strftime("%Y-%m-%d %H:%M:%S (KST)")
    except ValueError as e:
        print(f"날짜 변환 실패: {published} -> {e}")
        return "Invalid Date"


# HTML 태그 제거
def clean_tag(item):
    clean_text = re.sub(r'<[^>]*>', '', item)
    clean_text = html.unescape(clean_text)
    clean_text = re.sub(r'\s+', ' ', clean_text).strip()
    return clean_text

# 파일 저장
def save_to_csv(news_data, base_dir, folder_name):
    today = datetime.now()
    yyyy_mm = today.strftime("%Y-%m")
    target_dir = os.path.join(base_dir,folder_name, yyyy_mm) 
    filename = os.path.join(target_dir, f"{today.strftime('%Y-%m-%d')}_news.csv")
    
    # 뉴스 저장 할 폴더 만들기
    if not os.path.exists(target_dir):
        os.makedirs(target_dir)
        print(f"{target_dir} 폴더를 생성했습니다.")

     # 데이터 소스에 따른 필드 분기
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
        writer.writerow(["Title","Published(Kor)","Description","Link"])
        for item in items:
            try:
                title = clean_tag(item[title_field])
                published = convert_to_kst(item[published_field])
                description = clean_tag(item[description_field]).replace('. ', '.\n')
                link = item[link_field]
                writer.writerow([title, published, description, link])
            except KeyError as e:
                print(f"KeyError 발생: {e} (item: {item})")
            except Exception as e:
                print(f"Unexpected error: {e} (item: {item})")
    print(f"{filename}에 뉴스 데이터를 저장했습니다.")
