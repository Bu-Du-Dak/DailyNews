import HomeNewsView from "@/app/src/components/news/HomeNewsView";
import {
  NEWS_SECTIONS,
  type NewsSection,
  getAvailableDates,
  getNewsFeed
} from "@/app/src/lib/news";

type SearchParams = {
  section?: string;
  date?: string;
};

export default function Home({
  searchParams,
}: {
  searchParams?: SearchParams;
}) {
  const section = NEWS_SECTIONS.includes(searchParams?.section as NewsSection)
    ? (searchParams?.section as NewsSection)
    : "local";

  const dates = getAvailableDates(section);
  const activeDate =
    searchParams?.date && dates.includes(searchParams.date)
      ? searchParams.date
      : dates[0];

  const feed = getNewsFeed(section, activeDate);
  return <HomeNewsView section={section} dates={dates} activeDate={activeDate} feed={feed} />;
}
