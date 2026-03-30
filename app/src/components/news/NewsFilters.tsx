import Link from "next/link";
import styled from "styled-components";
import { type NewsSection } from "@/app/src/lib/news";
import { newsTheme } from "./NewsTokens";

const Toolbar = styled.section`
  position: sticky;
  top: 0;
  z-index: 10;
  margin: 20px 0 24px;
  padding: 16px;
  border-radius: 24px;
  backdrop-filter: blur(18px);
  background: rgba(9, 18, 32, 0.88);
  border: 1px solid ${newsTheme.colors.border};
  box-shadow: ${newsTheme.shadow};

  @media (max-width: 640px) {
    padding: 12px;
    border-radius: 20px;
  }
`;

const SectionTabs = styled.div`
  display: inline-flex;
  gap: 8px;
  padding: 6px;
  border-radius: 999px;
  background: rgba(255, 255, 255, 0.05);
`;

const SectionTab = styled(Link)<{ $active: boolean }>`
  padding: 10px 16px;
  border-radius: 999px;
  color: ${({ $active }) =>
    $active ? newsTheme.colors.accentText : newsTheme.colors.muted};
  background: ${({ $active }) =>
    $active ? newsTheme.colors.accent : "transparent"};
  font-weight: 600;
  text-decoration: none;
  transition:
    transform 160ms ease,
    background 160ms ease,
    color 160ms ease;

  &:hover {
    transform: translateY(-1px);
  }
`;

const DateStrip = styled.div`
  display: flex;
  gap: 10px;
  overflow-x: auto;
  padding-top: 16px;
  scrollbar-width: none;

  &::-webkit-scrollbar {
    display: none;
  }
`;

const DatePill = styled(Link)<{ $active: boolean }>`
  flex: 0 0 auto;
  padding: 10px 14px;
  border-radius: 999px;
  border: 1px solid
    ${({ $active }) =>
      $active ? "transparent" : newsTheme.colors.border};
  background: ${({ $active }) =>
    $active ? newsTheme.colors.white : "rgba(255, 255, 255, 0.05)"};
  color: ${({ $active }) =>
    $active ? newsTheme.colors.accentText : newsTheme.colors.muted};
  text-decoration: none;
  transition:
    transform 160ms ease,
    background 160ms ease,
    color 160ms ease;

  &:hover {
    transform: translateY(-1px);
  }
`;

const EmptyDate = styled.span`
  flex: 0 0 auto;
  padding: 10px 14px;
  border-radius: 999px;
  border: 1px solid ${newsTheme.colors.border};
  background: rgba(255, 255, 255, 0.05);
  color: ${newsTheme.colors.muted};
`;

function buildHref(section: NewsSection, date: string) {
  return `/?section=${section}&date=${date}`;
}

export default function NewsFilters({
  section,
  dates,
  activeDate,
  latestLocalDate,
  latestGlobalDate
}: {
  section: NewsSection;
  dates: string[];
  activeDate?: string;
  latestLocalDate: string;
  latestGlobalDate: string;
}) {
  return (
    <Toolbar>
      <SectionTabs>
        <SectionTab
          href={buildHref("local", latestLocalDate)}
          $active={section === "local"}
        >
          국내
        </SectionTab>
        <SectionTab
          href={buildHref("global", latestGlobalDate)}
          $active={section === "global"}
        >
          글로벌
        </SectionTab>
      </SectionTabs>

      <DateStrip aria-label="날짜 선택">
        {dates.length === 0 ? (
          <EmptyDate>표시할 날짜가 없습니다.</EmptyDate>
        ) : (
          dates.slice(0, 14).map((date) => (
            <DatePill
              key={date}
              href={buildHref(section, date)}
              $active={date === activeDate}
            >
              {date}
            </DatePill>
          ))
        )}
      </DateStrip>
    </Toolbar>
  );
}
