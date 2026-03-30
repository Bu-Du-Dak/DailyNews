import styled from "styled-components";
import {
  type NewsFeed as NewsFeedType,
  type NewsSection,
} from "@/app/src/lib/news";
import { newsTheme } from "./NewsTokens";
import NewsListItem from "./NewsListItem";

const FeedPanel = styled.section`
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

const FeedHeader = styled.div`
  display: flex;
  justify-content: space-between;
  gap: 16px;
  align-items: center;
  margin-bottom: 20px;

  @media (max-width: 640px) {
    align-items: flex-start;
  }
`;

const Kicker = styled.p`
  margin: 0;
  font-size: 0.72rem;
  font-weight: 700;
  letter-spacing: 0.16em;
  text-transform: uppercase;
  color: ${newsTheme.colors.accent};
`;

const Heading = styled.h2`
  margin: 10px 0 0;
  font-size: 1.9rem;
  line-height: 1.12;
  letter-spacing: -0.03em;
`;

const CountBadge = styled.span`
  min-width: 52px;
  height: 52px;
  display: inline-grid;
  place-items: center;
  border-radius: 50%;
  background: ${newsTheme.colors.white};
  color: ${newsTheme.colors.accentText};
  font-weight: 700;
`;

const List = styled.div`
  display: grid;
  gap: 14px;
`;

const EmptyState = styled.div`
  padding: 36px 20px;
  border-radius: 24px;
  text-align: center;
  color: ${newsTheme.colors.muted};
  background: rgba(19, 32, 52, 0.96);
`;

export default function NewsFeed({
  feed,
  section,
}: {
  feed: NewsFeedType;
  section: NewsSection;
}) {
  return (
    <FeedPanel>
      <FeedHeader>
        <div>
          <Kicker>Top Stories</Kicker>
          <Heading>
            {section === "local" ? "국내 주요 기사" : "글로벌 주요 기사"}
          </Heading>
        </div>
        <CountBadge>{feed.articles.length}</CountBadge>
      </FeedHeader>

      {feed.articles.length === 0 ? (
        <EmptyState>선택한 날짜의 CSV를 찾지 못했습니다.</EmptyState>
      ) : (
        <List>
          {feed.articles.map((article, index) => (
            <NewsListItem
              key={`${article.link}-${index}`}
              article={article}
              index={index}
            />
          ))}
        </List>
      )}
    </FeedPanel>
  );
}
