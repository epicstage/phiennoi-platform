import type { Metadata } from "next";
import { Geist, Geist_Mono } from "next/font/google";
import "./globals.css";

const geistSans = Geist({
  variable: "--font-geist-sans",
  subsets: ["latin"],
});

const geistMono = Geist_Mono({
  variable: "--font-geist-mono",
  subsets: ["latin"],
});

export const metadata: Metadata = {
  title: {
    default: "한베통역 | 한국-베트남 전문 통역 플랫폼",
    template: "%s | 한베통역",
  },
  description:
    "한국-베트남 전문 통역사 매칭 플랫폼. 농업, 뷰티, 제조, 법률, 의료, IT 등 10개 전문 분야 통역 용어사전과 가이드를 제공합니다.",
  keywords: [
    "한베통역",
    "한국 베트남 통역",
    "베트남 통역사",
    "전문 통역",
    "통역 용어사전",
    "phiên dịch",
    "phiên dịch tiếng Hàn",
  ],
  openGraph: {
    title: "한베통역 | 한국-베트남 전문 통역 플랫폼",
    description:
      "10개 전문 분야, 1,130개 용어 데이터베이스. 한-베 전문 통역사를 찾고 있다면.",
    siteName: "한베통역",
    locale: "ko_KR",
    type: "website",
  },
  robots: {
    index: true,
    follow: true,
  },
};

export default function RootLayout({
  children,
}: Readonly<{
  children: React.ReactNode;
}>) {
  return (
    <html lang="ko">
      <body
        className={`${geistSans.variable} ${geistMono.variable} antialiased`}
      >
        {children}
      </body>
    </html>
  );
}
