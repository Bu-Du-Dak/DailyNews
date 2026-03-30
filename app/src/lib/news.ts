import fs from "fs";
import path from "path";

export const NEWS_SECTIONS = ["local", "global"] as const;

export type NewsSection = (typeof NEWS_SECTIONS)[number];

export type NewsArticle = {
  title: string;
  publishedKor: string;
  description: string;
  link: string;
};

export type NewsFeed = {
  date: string | null;
  articles: NewsArticle[];
};

const SECTION_FOLDER: Record<NewsSection, string> = {
  local: "news",
  global: "global_news"
};

function getSectionDir(section: NewsSection) {
  return path.join(process.cwd(), SECTION_FOLDER[section]);
}

function listCsvFiles(section: NewsSection): string[] {
  const sectionDir = getSectionDir(section);

  if (!fs.existsSync(sectionDir)) {
    return [];
  }

  const monthDirs = fs
    .readdirSync(sectionDir, { withFileTypes: true })
    .filter((entry) => entry.isDirectory())
    .map((entry) => entry.name)
    .sort()
    .reverse();

  return monthDirs.flatMap((monthDir) => {
    const monthPath = path.join(sectionDir, monthDir);
    return fs
      .readdirSync(monthPath, { withFileTypes: true })
      .filter((entry) => entry.isFile() && entry.name.endsWith("_news.csv"))
      .map((entry) => path.join(monthPath, entry.name));
  });
}

function extractDateFromPath(filePath: string) {
  return path.basename(filePath).replace("_news.csv", "");
}

function parseCsvLine(content: string): string[][] {
  const rows: string[][] = [];
  let row: string[] = [];
  let field = "";
  let inQuotes = false;

  for (let index = 0; index < content.length; index += 1) {
    const char = content[index];
    const next = content[index + 1];

    if (char === '"') {
      if (inQuotes && next === '"') {
        field += '"';
        index += 1;
      } else {
        inQuotes = !inQuotes;
      }
      continue;
    }

    if (char === "," && !inQuotes) {
      row.push(field);
      field = "";
      continue;
    }

    if ((char === "\n" || char === "\r") && !inQuotes) {
      if (char === "\r" && next === "\n") {
        index += 1;
      }

      row.push(field);
      field = "";

      if (row.some((value) => value.length > 0)) {
        rows.push(row);
      }

      row = [];
      continue;
    }

    field += char;
  }

  if (field.length > 0 || row.length > 0) {
    row.push(field);
    rows.push(row);
  }

  return rows;
}

function mapRowsToArticles(rows: string[][]): NewsArticle[] {
  return rows.slice(1).map((columns) => ({
    title: columns[0] ?? "",
    publishedKor: columns[1] ?? "",
    description: columns[2] ?? "",
    link: columns[3] ?? "#"
  }));
}

export function getAvailableDates(section: NewsSection): string[] {
  return listCsvFiles(section)
    .map(extractDateFromPath)
    .sort()
    .reverse();
}

export function getNewsFeed(section: NewsSection, date?: string | null): NewsFeed {
  const files = listCsvFiles(section);
  const targetDate = date ?? extractDateFromPath(files[0] ?? "");
  const targetFile = files.find(
    (filePath) => extractDateFromPath(filePath) === targetDate
  );

  if (!targetDate || !targetFile || !fs.existsSync(targetFile)) {
    return {
      date: targetDate ?? null,
      articles: []
    };
  }

  const raw = fs.readFileSync(targetFile, "utf8").replace(/^\uFEFF/, "");
  const rows = parseCsvLine(raw);

  return {
    date: targetDate,
    articles: mapRowsToArticles(rows)
  };
}

export function getNewsArticle(
  section: NewsSection,
  date: string,
  articleIndex: number
) {
  const feed = getNewsFeed(section, date);
  return feed.articles[articleIndex] ?? null;
}
