import os
import requests
from dotenv import load_dotenv
from datetime import datetime, timedelta
import pytz

load_dotenv()

GLOBAL_API_URL = os.getenv('GLOBAL_API_URL')
GLOBAL_API_KEY = os.getenv('GLOBAL_API_KEY')

NY_Time = pytz.timezone('America/New_York')
today = datetime.now(NY_Time).strftime("%Y-%m-%d")
yesterday = (datetime.now(NY_Time) - timedelta(days=1)).strftime("%Y-%m-%d")

headers = {
    "X-Api-Key": GLOBAL_API_KEY 
}
params = {
    "q":"today",
    "to": today,
    "from": yesterday,
    "sortBy": "popularity",
    "pageSize": 20,
    "page": 1
}
def fetch_global_news ():
    try:
        response = requests.get(GLOBAL_API_URL,params=params, headers=headers)
        response.raise_for_status()
        data = response.json()
        return data
    except requests.exceptions.RequestException as e :
        print(f"Fail: {e}")
        return None  
    
if __name__ == "__main__":
    news_data = fetch_global_news()
    if news_data:
        print("뉴스 데이터를 성공적으로 가져왔습니다!")
        print(news_data)
    else:
        print("뉴스 데이터를 가져오지 못했습니다.")
