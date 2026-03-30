import type { MetadataRoute } from "next";

export default function manifest(): MetadataRoute.Manifest {
  return {
    name: "Daily News Briefing",
    short_name: "DailyNews",
    description: "매일 저장한 CSV 뉴스를 모바일과 웹에서 빠르게 확인하는 앱",
    start_url: "/",
    display: "standalone",
    background_color: "#f7f1e3",
    theme_color: "#f7f1e3",
    lang: "ko"
  };
}
