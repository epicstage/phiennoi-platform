import { ImageResponse } from "next/og";
import { domains } from "@/data/pseo-dimensions";
import type { Term } from "@/types/term";

export const runtime = "nodejs";
export const alt = "Epic Note 용어사전";
export const size = { width: 1200, height: 630 };
export const contentType = "image/png";

export default async function Image({
  params,
}: {
  params: Promise<{ domain: string }>;
}) {
  const { domain: domainSlug } = await params;
  const domain = domains.find((d) => d.slug === domainSlug);

  let termCount = 0;
  try {
    // eslint-disable-next-line @typescript-eslint/no-require-imports
    const terms = require(`@/data/terms/${domainSlug}.json`) as Term[];
    termCount = terms.length;
  } catch {
    // no data
  }

  const domainName = domain?.name ?? "통역";
  const domainNameVi = domain?.nameVi ?? "";
  const keywords = domain?.keywords?.slice(0, 4) ?? [];

  return new ImageResponse(
    (
      <div
        style={{
          display: "flex",
          flexDirection: "column",
          width: "100%",
          height: "100%",
          backgroundColor: "#1a1a2e",
          color: "#ffffff",
          padding: "60px",
          fontFamily: "sans-serif",
        }}
      >
        {/* Top bar */}
        <div
          style={{
            display: "flex",
            justifyContent: "space-between",
            alignItems: "center",
            marginBottom: "40px",
          }}
        >
          <div
            style={{
              display: "flex",
              fontSize: "28px",
              fontWeight: "bold",
              color: "#e63946",
            }}
          >
            Epic Note
          </div>
          <div
            style={{
              display: "flex",
              fontSize: "20px",
              color: "rgba(255,255,255,0.5)",
            }}
          >
            용어사전
          </div>
        </div>

        {/* Main content */}
        <div
          style={{
            display: "flex",
            flexDirection: "column",
            flex: 1,
            justifyContent: "center",
          }}
        >
          <div
            style={{
              display: "flex",
              fontSize: "64px",
              fontWeight: "bold",
              marginBottom: "12px",
            }}
          >
            {domainName} 통역 용어사전
          </div>
          <div
            style={{
              display: "flex",
              fontSize: "36px",
              color: "#e63946",
              marginBottom: "24px",
            }}
          >
            {domainNameVi}
          </div>
          <div
            style={{
              display: "flex",
              gap: "12px",
              flexWrap: "wrap",
            }}
          >
            {keywords.map((kw) => (
              <div
                key={kw}
                style={{
                  display: "flex",
                  padding: "8px 16px",
                  backgroundColor: "rgba(255,255,255,0.1)",
                  borderRadius: "16px",
                  fontSize: "20px",
                  color: "rgba(255,255,255,0.7)",
                }}
              >
                #{kw}
              </div>
            ))}
          </div>
        </div>

        {/* Bottom bar */}
        <div
          style={{
            display: "flex",
            justifyContent: "space-between",
            alignItems: "center",
            borderTop: "1px solid rgba(255,255,255,0.1)",
            paddingTop: "24px",
            fontSize: "20px",
            color: "rgba(255,255,255,0.5)",
          }}
        >
          <span>{termCount}개 전문 용어 수록</span>
          <span>vn.epicstage.co.kr</span>
        </div>
      </div>
    ),
    { ...size }
  );
}
