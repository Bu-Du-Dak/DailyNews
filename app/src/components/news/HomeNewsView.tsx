import {
  type NewsFeed,
  type NewsSection,
  getAvailableDates
} from "@/app/src/lib/news";
import NewsFeedPanel from "./NewsFeed";
import NewsFilters from "./NewsFilters";
import NewsHero from "./NewsHero";
import NewsShell from "./NewsShell";

export default function HomeNewsView({
  section,
  dates,
  activeDate,
  feed
}: {
  section: NewsSection;
  dates: string[];
  activeDate?: string;
  feed: NewsFeed;
}) {
  const latestLabel = dates[0] ?? "데이터 없음";

  return (
    <NewsShell>
      <NewsHero
        section={section}
        latestLabel={latestLabel}
        articleCount={feed.articles.length}
      />
      <NewsFilters
        section={section}
        dates={dates}
        activeDate={activeDate}
        latestLocalDate={getAvailableDates("local")[0] ?? ""}
        latestGlobalDate={getAvailableDates("global")[0] ?? ""}
      />
      <NewsFeedPanel feed={feed} section={section} />
    </NewsShell>
  );
}
