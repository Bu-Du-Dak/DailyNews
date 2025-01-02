import os
import requests
from dotenv import load_dotenv
from datetime import datetime
import pytz

load_dotenv()

NY_API_URL = os.getenv('NY_API_URL')
NY_API_KEY = os.getenv('NY_API_KEY')

NY_Time = pytz.timezone('America/New_York')
today = datetime.now(NY_Time).strftime("%Y%m%d")

params = {
    "api-key": NY_API_KEY,
    "begin_date": 20240101,
    "end_date": 20240101,
    "page": 0,
    "sort": "newest",
    "fq": "section_name:(\"World\")",
    "facet": "true",
    "facet_fields": "section_name"
}
def fetch_global_news ():
    try:
        response = requests.get(NY_API_URL,params=params)
        response.raise_for_status()
        data = response.json()
        print(f"API 응답 데이터: {data}")
        return data
    except requests.exceptions.RequestException as e :
        print(f"Fail: {e}")
        return None  
    
if __name__ == "__main__":
    news_data = fetch_global_news()
    if news_data:
        print("뉴스 데이터를 성공적으로 가져왔습니다!")
        # print(news_data)
    else:
        print("뉴스 데이터를 가져오지 못했습니다.")
