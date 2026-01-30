import { ImageResponse } from "next/og";

export const runtime = "nodejs";
export const alt = "Epic Note - 한국-베트남 전문 통역 플랫폼";
export const size = { width: 1200, height: 630 };
export const contentType = "image/png";

export default async function Image() {
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
            alignItems: "center",
            marginBottom: "60px",
          }}
        >
          <div
            style={{
              display: "flex",
              fontSize: "32px",
              fontWeight: "bold",
              color: "#e63946",
            }}
          >
            Epic Note
          </div>
        </div>

        {/* Main */}
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
              marginBottom: "20px",
              lineHeight: 1.3,
            }}
          >
            한국-베트남 전문 통역
          </div>
          <div
            style={{
              display: "flex",
              fontSize: "36px",
              color: "rgba(255,255,255,0.7)",
              marginBottom: "32px",
            }}
          >
            Nền tảng phiên dịch chuyên nghiệp Hàn-Việt
          </div>
          <div
            style={{
              display: "flex",
              gap: "16px",
            }}
          >
            <div
              style={{
                display: "flex",
                padding: "12px 24px",
                backgroundColor: "#e63946",
                borderRadius: "12px",
                fontSize: "24px",
                fontWeight: "600",
              }}
            >
              용어사전 297+
            </div>
            <div
              style={{
                display: "flex",
                padding: "12px 24px",
                backgroundColor: "rgba(230, 57, 70, 0.2)",
                borderRadius: "12px",
                fontSize: "24px",
                color: "#e63946",
              }}
            >
              가이드 80+
            </div>
            <div
              style={{
                display: "flex",
                padding: "12px 24px",
                backgroundColor: "rgba(255,255,255,0.1)",
                borderRadius: "12px",
                fontSize: "24px",
                color: "rgba(255,255,255,0.7)",
              }}
            >
              12개 분야
            </div>
          </div>
        </div>

        {/* Bottom */}
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
          <span>농업 · 법률 · 의료 · 제조 · 건설 · IT 외</span>
          <span>vn.epicstage.co.kr</span>
        </div>
      </div>
    ),
    { ...size }
  );
}
