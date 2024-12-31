import os
import requests
from dotenv import load_dotenv

load_dotenv()

CLIENT_ID = os.getenv('CLIENT_ID')
CLIENT_SECRET = os.getenv('CLIENT_SECRET')
API_URL = os.getenv('API_URL')

headers = {
    "X-Naver-Client-Id": CLIENT_ID,
    "X-Naver-Client-Secret": CLIENT_SECRET,
}
params = {
    "query": '오늘',
    "display": 20,
    "sort": "date"
}

def fetch_news():
    try:
        response = requests.get(API_URL,headers=headers,params=params)
        response.raise_for_status()
        return response.json()
    except requests.exceptions.RequestException as e:
        print(f"Fail:{e}")
        return None
    
    
if __name__ == "__main__":
    news_data = fetch_news()
    if news_data:
        print("뉴스 데이터를 성공적으로 가져왔습니다!")
        print(news_data)
    else:
        print("뉴스 데이터를 가져오지 못했습니다.")