import type { Metadata, Viewport } from "next";
import StyledComponentsRegistry from "@/app/src/lib/styled-components-registry";
import "./globals.css";

export const metadata: Metadata = {
  title: "Daily News Briefing",
  description: "CSV로 저장한 매일 뉴스를 웹과 모바일에서 보기 쉽게 정리한 브리핑 앱"
};

export const viewport: Viewport = {
  width: "device-width",
  initialScale: 1,
  themeColor: "#08111f"
};

export default function RootLayout({
  children
}: Readonly<{
  children: React.ReactNode;
}>) {
  return (
    <html lang="ko">
      <body>
        <StyledComponentsRegistry>{children}</StyledComponentsRegistry>
      </body>
    </html>
  );
}
