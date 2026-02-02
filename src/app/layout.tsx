import type { Metadata } from "next";
import Script from "next/script";
import { Geist, Geist_Mono, Noto_Serif_KR, Playfair_Display } from "next/font/google";
import "./globals.css";

const geistSans = Geist({
  variable: "--font-geist-sans",
  subsets: ["latin"],
});

const geistMono = Geist_Mono({
  variable: "--font-geist-mono",
  subsets: ["latin"],
});

const notoSerifKR = Noto_Serif_KR({
  variable: "--font-noto-serif-kr",
  subsets: ["latin"],
  weight: ["400", "500", "600", "700"],
});

const playfairDisplay = Playfair_Display({
  variable: "--font-playfair",
  subsets: ["latin"],
  weight: ["400", "500", "600", "700"],
});

export const metadata: Metadata = {
  title: {
    default: "Epic Note | 한국-베트남 전문 통역 플랫폼",
    template: "%s | Epic Note",
  },
  description:
    "한국-베트남 전문 통역사 매칭 플랫폼. 농업, 뷰티, 제조, 법률, 의료, IT 등 21개 전문 분야 통역 용어사전과 가이드를 제공합니다.",
  keywords: [
    "Epic Note",
    "한국 베트남 통역",
    "베트남 통역사",
    "전문 통역",
    "통역 용어사전",
    "phiên dịch",
    "phiên dịch tiếng Hàn",
  ],
  icons: {
    icon: "/favicon.svg",
    shortcut: "/favicon.svg",
    apple: "/favicon.svg",
  },
  openGraph: {
    title: "Epic Note | 한국-베트남 전문 통역 플랫폼",
    description:
      "21개 전문 분야, 4,800+ 용어 데이터베이스. 한-베 전문 통역사를 찾고 있다면.",
    siteName: "Epic Note",
    locale: "ko_KR",
    type: "website",
    url: "https://vn.epicstage.co.kr",
  },
  robots: {
    index: true,
    follow: true,
  },
  metadataBase: new URL("https://vn.epicstage.co.kr"),
};

export default function RootLayout({
  children,
}: Readonly<{
  children: React.ReactNode;
}>) {
  return (
    <html lang="ko">
      <head>
        <Script
          src="https://www.googletagmanager.com/gtag/js?id=G-Z7WKGPGYYR"
          strategy="afterInteractive"
        />
        <Script id="google-analytics" strategy="afterInteractive">
          {`
            window.dataLayer = window.dataLayer || [];
            function gtag(){dataLayer.push(arguments);}
            gtag('js', new Date());
            gtag('config', 'G-Z7WKGPGYYR');
          `}
        </Script>
      </head>
      <body
        className={`${geistSans.variable} ${geistMono.variable} ${notoSerifKR.variable} ${playfairDisplay.variable} antialiased`}
      >
        {children}
      </body>
    </html>
  );
}
