## Daily News

기존 Python 수집 스크립트로 국내 뉴스와 글로벌 뉴스를 CSV로 저장하고, Next.js 화면에서 날짜별로 조회할 수 있는 프로젝트입니다.

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

- `src/`: 네이버/글로벌 뉴스 수집 및 CSV 저장
- `news/`: 국내 뉴스 CSV 아카이브
- `global_news/`: 글로벌 뉴스 CSV 아카이브
- `app/`, `lib/`: Next.js 기반 조회 UI
