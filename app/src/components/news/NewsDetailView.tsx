import Link from "next/link";
import styled from "styled-components";
import { type NewsArticle, type NewsSection } from "@/app/src/lib/news";
import NewsShell from "./NewsShell";
import { newsTheme } from "./NewsTokens";

const Header = styled.header`
  display: grid;
  gap: 16px;
  margin-bottom: 24px;
  padding: 28px;
  border-radius: 32px;
  backdrop-filter: blur(18px);
  background: rgba(13, 23, 39, 0.84);
  border: 1px solid ${newsTheme.colors.border};
  box-shadow: ${newsTheme.shadow};

  @media (max-width: 640px) {
    padding: 20px;
    border-radius: 24px;
  }
`;

const Breadcrumb = styled.nav`
  display: flex;
  flex-wrap: wrap;
  gap: 10px;
  color: ${newsTheme.colors.muted};
  font-size: 0.92rem;
`;

const BackLink = styled(Link)`
  width: fit-content;
  display: inline-flex;
  align-items: center;
  justify-content: center;
  min-height: 44px;
  padding: 0 16px;
  border-radius: 999px;
  background: rgba(255, 255, 255, 0.05);
  color: ${newsTheme.colors.text};
  text-decoration: none;
  font-weight: 600;
`;

const Title = styled.h1`
  margin: 0;
  font-size: clamp(2rem, 4vw, 3.6rem);
  line-height: 1.06;
  letter-spacing: -0.04em;
`;

const Meta = styled.div`
  display: flex;
  flex-wrap: wrap;
  gap: 12px;
  color: ${newsTheme.colors.accent};
  font-weight: 600;
`;

const Body = styled.article`
  padding: 32px;
  border-radius: 32px;
  backdrop-filter: blur(18px);
  background: rgba(19, 32, 52, 0.96);
  border: 1px solid ${newsTheme.colors.border};
  box-shadow: ${newsTheme.shadow};

  @media (max-width: 640px) {
    padding: 20px;
    border-radius: 24px;
  }
`;

const Description = styled.div`
  color: ${newsTheme.colors.muted};
  line-height: 1.8;
  white-space: pre-line;
  font-size: 1.04rem;
`;

const ActionRow = styled.div`
  display: flex;
  flex-wrap: wrap;
  gap: 12px;
  margin-top: 28px;
`;

const SourceButton = styled.a`
  display: inline-flex;
  align-items: center;
  justify-content: center;
  min-height: 46px;
  padding: 0 18px;
  border-radius: 999px;
  background: ${newsTheme.colors.white};
  color: ${newsTheme.colors.accentText};
  text-decoration: none;
  font-weight: 700;
`;

const SecondaryLink = styled(Link)`
  display: inline-flex;
  align-items: center;
  justify-content: center;
  min-height: 46px;
  padding: 0 18px;
  border-radius: 999px;
  background: rgba(255, 255, 255, 0.05);
  color: ${newsTheme.colors.text};
  text-decoration: none;
  font-weight: 600;
`;

export default function NewsDetailView({
  section,
  date,
  index,
  article
}: {
  section: NewsSection;
  date: string;
  index: number;
  article: NewsArticle;
}) {
  const listHref = `/?section=${section}&date=${date}`;

  return (
    <NewsShell>
      <Header>
        <Breadcrumb>
          <span>{section === "local" ? "국내 뉴스" : "글로벌 뉴스"}</span>
          <span>{date}</span>
          <span>{String(index + 1).padStart(2, "0")}번째 기사</span>
        </Breadcrumb>
        <BackLink href={listHref}>목록으로 돌아가기</BackLink>
        <Title>{article.title}</Title>
        <Meta>
          <span>{article.publishedKor}</span>
        </Meta>
      </Header>

      <Body>
        <Description>{article.description || "상세 설명이 없습니다."}</Description>
        <ActionRow>
          <SourceButton href={article.link} target="_blank" rel="noreferrer">
            원문 기사 열기
          </SourceButton>
          <SecondaryLink href={listHref}>같은 날짜 목록 보기</SecondaryLink>
        </ActionRow>
      </Body>
    </NewsShell>
  );
}
