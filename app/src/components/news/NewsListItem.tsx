import styled from "styled-components";
import { type NewsArticle } from "@/app/src/lib/news";
import { newsTheme } from "./NewsTokens";

const Card = styled.article`
  padding: 22px;
  border-radius: 24px;
  background: rgba(19, 32, 52, 0.96);
  border: 1px solid ${newsTheme.colors.border};
  transition:
    transform 160ms ease,
    border-color 160ms ease,
    background 160ms ease;

  &:hover {
    transform: translateY(-1px);
    border-color: ${newsTheme.colors.borderStrong};
    background: rgba(24, 38, 60, 0.98);
  }
`;

const Meta = styled.div`
  display: flex;
  justify-content: space-between;
  gap: 12px;
  margin-bottom: 10px;
  color: ${newsTheme.colors.accent};
  font-size: 0.86rem;
  font-weight: 600;
`;

const Title = styled.h3`
  margin: 0 0 10px;
  font-size: 1.26rem;
  line-height: 1.3;
  letter-spacing: -0.02em;
`;

const Description = styled.p`
  margin: 0 0 18px;
  color: ${newsTheme.colors.muted};
  line-height: 1.7;
  white-space: pre-line;
  display: -webkit-box;
  -webkit-line-clamp: 3;
  -webkit-box-orient: vertical;
  overflow: hidden;
`;

const Actions = styled.div`
  display: flex;
  align-items: center;
  justify-content: flex-end;
  gap: 12px;

  @media (max-width: 640px) {
    flex-direction: column;
    align-items: stretch;
  }
`;

const Caption = styled.span`
  color: ${newsTheme.colors.muted};
  font-size: 0.92rem;
`;

const DetailButton = styled.a`
  display: inline-flex;
  align-items: center;
  justify-content: center;
  min-height: 44px;
  padding: 0 16px;
  border-radius: 999px;
  background: ${newsTheme.colors.white};
  color: ${newsTheme.colors.accentText};
  font-weight: 700;
  text-decoration: none;
`;

export default function NewsListItem({
  article,
  index,
}: {
  article: NewsArticle;
  index: number;
}) {
  return (
    <Card>
      <Meta>
        <span>{String(index + 1).padStart(2, "0")}</span>
        <span>{article.publishedKor}</span>
      </Meta>
      <Title>{article.title}</Title>
      <Description>{article.description}</Description>
      <Actions>
        <DetailButton href={article.link} target="_blank" rel="noreferrer">
          원문 보기
        </DetailButton>
      </Actions>
    </Card>
  );
}
