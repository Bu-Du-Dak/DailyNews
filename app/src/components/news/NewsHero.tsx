import styled from "styled-components";
import { type NewsSection } from "@/app/src/lib/news";
import { newsTheme } from "./NewsTokens";

const Hero = styled.section`
  display: grid;
  grid-template-columns: minmax(0, 2fr) minmax(280px, 1fr);
  gap: 20px;
  align-items: stretch;

  @media (max-width: 960px) {
    grid-template-columns: 1fr;
  }
`;

const HeroCopy = styled.div`
  padding: 32px;
  border-radius: 32px;
  backdrop-filter: blur(18px);
  background: rgba(13, 23, 39, 0.84);
  border: 1px solid ${newsTheme.colors.border};
  box-shadow: ${newsTheme.shadow};
`;

const Eyebrow = styled.p`
  display: inline-block;
  margin: 0;
  letter-spacing: 0.16em;
  text-transform: uppercase;
  font-size: 0.72rem;
  font-weight: 700;
  color: ${newsTheme.colors.accent};
`;

const Title = styled.h1`
  margin: 12px 0 16px;
  max-width: 12ch;
  font-size: clamp(2.4rem, 5vw, 4.6rem);
  line-height: 0.98;
  letter-spacing: -0.04em;

  @media (max-width: 960px) {
    max-width: none;
  }

  @media (max-width: 640px) {
    font-size: 2.7rem;
  }
`;

const Description = styled.p`
  margin: 0;
  max-width: 58ch;
  color: ${newsTheme.colors.muted};
  line-height: 1.7;
  font-size: 1.02rem;
`;

const HeroPanel = styled.div`
  padding: 28px;
  border-radius: 28px;
  display: grid;
  gap: 18px;
  align-content: center;
  backdrop-filter: blur(18px);
  background: rgba(13, 23, 39, 0.84);
  border: 1px solid ${newsTheme.colors.border};
  box-shadow: ${newsTheme.shadow};

  @media (max-width: 640px) {
    padding: 20px;
    border-radius: 24px;
  }
`;

const Label = styled.span`
  display: inline-block;
  font-size: 0.72rem;
  font-weight: 700;
  letter-spacing: 0.16em;
  text-transform: uppercase;
  color: ${newsTheme.colors.accent};
`;

const Value = styled.strong`
  display: block;
  margin-top: 6px;
  font-size: 1.25rem;
`;

export default function NewsHero({
  section,
  latestLabel,
  articleCount,
}: {
  section: NewsSection;
  latestLabel: string;
  articleCount: number;
}) {
  return (
    <Hero>
      <HeroCopy>
        <Eyebrow>Daily Briefing</Eyebrow>
        <Title>Daily News.</Title>
        <Description>
          날짜별로 정리된 국내외 주요 뉴스를 빠르게 확인해보세요.
        </Description>
      </HeroCopy>

      <HeroPanel>
        <div>
          <Label>현재 섹션</Label>
          <Value>{section === "local" ? "국내 뉴스" : "글로벌 뉴스"}</Value>
        </div>
        <div>
          <Label>기본 날짜</Label>
          <Value>{latestLabel}</Value>
        </div>
        <div>
          <Label>기사 수</Label>
          <Value>{articleCount}건</Value>
        </div>
      </HeroPanel>
    </Hero>
  );
}
