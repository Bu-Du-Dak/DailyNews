import styled from "styled-components";
import { newsTheme } from "./NewsTokens";

const Shell = styled.main`
  min-height: 100vh;
  color: ${newsTheme.colors.text};
  background:
    radial-gradient(circle at top left, rgba(110, 155, 255, 0.18), transparent 26%),
    radial-gradient(circle at top right, rgba(255, 255, 255, 0.06), transparent 18%),
    linear-gradient(180deg, #0b1424 0%, ${newsTheme.colors.bg} 45%, ${newsTheme.colors.bgDeep} 100%);
`;

const Inner = styled.div`
  max-width: 1240px;
  margin: 0 auto;
  padding: 32px 20px 56px;

  @media (max-width: 640px) {
    padding: 16px 14px 32px;
  }
`;

export default function NewsShell({ children }: { children: React.ReactNode }) {
  return (
    <Shell>
      <Inner>{children}</Inner>
    </Shell>
  );
}
