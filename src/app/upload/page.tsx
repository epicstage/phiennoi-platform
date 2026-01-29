import { Metadata } from "next";
import Header from "@/components/Header";
import Footer from "@/components/Footer";
import UploadForm from "@/components/UploadForm";

export const metadata: Metadata = {
  title: "통역사 이력서 등록 | 한-베 전문 통역 플랫폼",
  description:
    "한-베 전문 통역사로 등록하세요. 이력서를 업로드하면 전문 분야에 맞는 통역 의뢰를 매칭해드립니다.",
  keywords: ["통역사 등록", "베트남어 통역", "이력서 업로드", "통역 의뢰"],
};

export default function UploadPage() {
  return (
    <div className="min-h-screen bg-background">
      <Header />

      {/* Hero */}
      <div className="py-16 px-6 text-center bg-background-secondary border-b border-border-default">
        <div className="max-w-3xl mx-auto">
          <h1 className="text-3xl md:text-4xl font-bold text-foreground mb-4">
            통역사 이력서 등록
          </h1>
          <p className="text-lg text-foreground-secondary">
            이력서를 등록하고 전문 분야 통역 의뢰를 받아보세요
          </p>
        </div>
      </div>

      {/* Form (Client Component) */}
      <UploadForm />

      <Footer />
    </div>
  );
}
