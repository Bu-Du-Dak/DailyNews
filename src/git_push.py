import os
import subprocess
from datetime import datetime
from dotenv import load_dotenv

load_dotenv()
PAT = os.getenv('PAT')

def git_push():
    today = datetime.now().strftime("%Y-%m-%d")
    try:
        REPO_URL = f"https://{PAT}@github.com/Bu-Du-Dak/DailyNews.git"
        subprocess.run(["git", "config", "--global", "user.name", "Bu-Du-Dak"], check=True)
        subprocess.run(["git", "config", "--global", "user.email", "guri930219@gmail.com"], check=True)
        subprocess.run(["git", "add", "."], check=True)
        subprocess.run(["git", "commit", "-m", f"Auto-update {today} news data"], check=True)
        subprocess.run(["git", "push", REPO_URL, "main"], check=True)
        print("GitHub에 데이터를 성공적으로 푸시했습니다!")
    except subprocess.CalledProcessError as e:
        print(f"Git 명령어 실행 중 오류가 발생했습니다: {e}")