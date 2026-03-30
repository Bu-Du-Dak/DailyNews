import { notFound } from "next/navigation";
import NewsDetailView from "@/app/src/components/news/NewsDetailView";
import {
  NEWS_SECTIONS,
  getNewsArticle,
  type NewsSection
} from "@/app/src/lib/news";

export default function NewsDetailPage({
  params
}: {
  params: {
    section: string;
    date: string;
    index: string;
  };
}) {
  if (!NEWS_SECTIONS.includes(params.section as NewsSection)) {
    notFound();
  }

  const section = params.section as NewsSection;
  const index = Number.parseInt(params.index, 10);

  if (Number.isNaN(index) || index < 0) {
    notFound();
  }

  const article = getNewsArticle(section, params.date, index);

  if (!article) {
    notFound();
  }

  return (
    <NewsDetailView
      section={section}
      date={params.date}
      index={index}
      article={article}
    />
  );
}
