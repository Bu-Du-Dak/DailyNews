## Daily News

Python 수집 스크립트로 GNews 헤드라인을 국내/글로벌 CSV로 저장하고, Next.js 화면에서 날짜별로 조회할 수 있는 프로젝트입니다.

### Python 수집 실행

```bash
source venv/bin/activate
python3 src/main.py
deactivate
```

### Next 웹 실행

```bash
npm install
npm run dev
```

브라우저에서 `http://localhost:3000`으로 접속하면 됩니다.

### 현재 구조

- `src/`: GNews 기반 국내/글로벌 뉴스 수집 및 CSV 저장
- `news/`: 국내 뉴스 CSV 아카이브
- `global_news/`: 글로벌 뉴스 CSV 아카이브
- `app/`: Next.js 기반 조회 UI

### 환경 변수

- `GNEWS_API_KEY` 또는 `GLOBAL_API_KEY`: GNews API 키
- `GNEWS_API_URL` 또는 `GLOBAL_API_URL`: 기본값은 `https://gnews.io/api/v4/top-headlines`
