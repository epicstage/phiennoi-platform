import { ImageResponse } from "next/og";
import { domains, interpretTypes } from "@/data/pseo-dimensions";

export const runtime = "nodejs";
export const alt = "Epic Note 통역 가이드";
export const size = { width: 1200, height: 630 };
export const contentType = "image/png";

export default async function Image({
  params,
}: {
  params: Promise<{ domain: string; type: string }>;
}) {
  const { domain: domainSlug, type: typeSlug } = await params;
  const domain = domains.find((d) => d.slug === domainSlug);
  const interpType = interpretTypes.find((t) => t.slug === typeSlug);

  const domainName = domain?.name ?? "통역";
  const domainNameVi = domain?.nameVi ?? "";
  const typeName = interpType?.name ?? "통역";
  const typeNameVi = interpType?.nameVi ?? "";

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
            통역 가이드
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
              gap: "16px",
              marginBottom: "24px",
            }}
          >
            <div
              style={{
                display: "flex",
                padding: "8px 20px",
                backgroundColor: "rgba(230, 57, 70, 0.2)",
                borderRadius: "20px",
                fontSize: "24px",
                color: "#e63946",
              }}
            >
              {domainName} · {domainNameVi}
            </div>
          </div>
          <div
            style={{
              display: "flex",
              fontSize: "56px",
              fontWeight: "bold",
              marginBottom: "16px",
              lineHeight: 1.3,
            }}
          >
            {domainName} {typeName} 가이드
          </div>
          <div
            style={{
              display: "flex",
              fontSize: "32px",
              color: "#e63946",
            }}
          >
            {typeNameVi}
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
          <span>한국-베트남 전문 통역 플랫폼</span>
          <span>vn.epicstage.co.kr</span>
        </div>
      </div>
    ),
    { ...size }
  );
}
