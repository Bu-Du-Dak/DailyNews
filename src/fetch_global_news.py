import os
import requests
from dotenv import load_dotenv

load_dotenv()

NY_API_URL = os.getenv('NY_API_URL')
NY_API_KEY = os.getenv('NY_API_KEY')

params = {
    "api-key": NY_API_KEY
}
def fetch_global_news ():
    try:
        response = requests.get(NY_API_URL,params=params)
        response.raise_for_status()
        return response.json()
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