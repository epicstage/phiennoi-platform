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
  params: Promise<{ domain: string; term: string }>;
}) {
  const { domain: domainSlug, term: termSlug } = await params;
  const domain = domains.find((d) => d.slug === domainSlug);

  let term: Term | undefined;
  try {
    // eslint-disable-next-line @typescript-eslint/no-require-imports
    const terms = require(`@/data/terms/${domainSlug}.json`) as Term[];
    term = terms.find((t) => t.slug === termSlug);
  } catch {
    // no data
  }

  const korean = term?.korean ?? "용어";
  const vietnamese = term?.vietnamese ?? "";
  const hanja = term?.hanja ?? "";
  const domainName = domain?.name ?? "통역";
  const domainNameVi = domain?.nameVi ?? "";

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
              alignItems: "center",
              gap: "12px",
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
              padding: "8px 20px",
              backgroundColor: "rgba(230, 57, 70, 0.2)",
              borderRadius: "20px",
              fontSize: "20px",
              color: "#e63946",
            }}
          >
            {domainName} · {domainNameVi}
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
              fontSize: "72px",
              fontWeight: "bold",
              marginBottom: "16px",
              lineHeight: 1.2,
            }}
          >
            {korean}
          </div>
          {hanja && (
            <div
              style={{
                display: "flex",
                fontSize: "36px",
                color: "rgba(255,255,255,0.5)",
                marginBottom: "16px",
              }}
            >
              {hanja}
            </div>
          )}
          <div
            style={{
              display: "flex",
              fontSize: "40px",
              color: "#e63946",
              fontWeight: "600",
            }}
          >
            {vietnamese}
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
          <span>한국어-베트남어 전문 통역 용어사전</span>
          <span>vn.epicstage.co.kr</span>
        </div>
      </div>
    ),
    { ...size }
  );
}
