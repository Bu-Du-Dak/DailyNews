import os
import subprocess
from dotenv import load_dotenv

load_dotenv()
GIT_TOKEN = os.getenv('GIT_TOKEN')

def git_push():
    try:
        REPO_URL = f"https://{GIT_TOKEN}@github.com/Bu-Du-Dak/DailyNews.git"
        subprocess.run(["git", "add", "."], check=True)
        subprocess.run(["git", "commit", "-m", "Auto-update news data"], check=True)
        subprocess.run(["git", "push", REPO_URL, "main"], check=True)
        print("GitHub에 데이터를 성공적으로 푸시했습니다!")
    except subprocess.CalledProcessError as e:
        print(f"Git 명령어 실행 중 오류가 발생했습니다: {e}")