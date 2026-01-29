import { Metadata } from "next";
import Link from "next/link";
import { domains } from "@/data/pseo-dimensions";
import type { Term } from "@/types/term";
import Header from "@/components/Header";
import Footer from "@/components/Footer";

export const metadata: Metadata = {
  title: "한-베 통역 용어사전 | 분야별 전문 용어 모음",
  description:
    "한국어-베트남어 통역 전문 용어사전. 농업, 뷰티, 제조, 법률, IT 등 분야별 통역 필수 용어를 한자 분해와 함께 학습하세요.",
  keywords: [
    "베트남어 통역",
    "한베 통역",
    "통역 용어",
    "전문 용어",
    ...domains.flatMap((d) => [d.name, d.nameVi]),
  ],
};

// 각 도메인별 용어 수 가져오기
function getTermCount(domainSlug: string): number {
  try {
    // eslint-disable-next-line @typescript-eslint/no-require-imports
    const terms = require(`@/data/terms/${domainSlug}.json`) as Term[];
    return terms.length;
  } catch {
    return 0;
  }
}

export default function TermsIndexPage() {
  // 도메인별 통계
  const domainStats = domains.map((domain) => ({
    ...domain,
    termCount: getTermCount(domain.slug),
  }));

  const totalTerms = domainStats.reduce((sum, d) => sum + d.termCount, 0);

  return (
    <div className="min-h-screen bg-background">
      <Header />

      <div className="max-w-6xl mx-auto px-4 py-8">
        {/* Breadcrumb */}
        <nav className="text-sm text-foreground-muted mb-6">
          <Link href="/" className="hover:text-red-primary">
            홈
          </Link>
          <span className="mx-2">/</span>
          <span className="text-foreground">용어사전</span>
        </nav>

        {/* 헤더 */}
        <header className="mb-8">
          <h1 className="text-3xl font-bold text-foreground mb-4">
            한-베 통역 용어사전
          </h1>
          <p className="text-foreground-secondary text-lg">
            한국어-베트남어 통역에 필요한 분야별 전문 용어를 한자 분해와 함께
            학습하세요.
          </p>
        </header>

        {/* 통계 */}
        <div className="grid md:grid-cols-3 gap-4 mb-8">
          <div className="bg-background-surface border border-border-default rounded-lg p-4 text-center">
            <p className="text-3xl font-bold text-red-primary">{totalTerms}</p>
            <p className="text-foreground-secondary">등록 용어</p>
          </div>
          <div className="bg-background-surface border border-border-default rounded-lg p-4 text-center">
            <p className="text-3xl font-bold text-green-success">{domains.length}</p>
            <p className="text-foreground-secondary">전문 분야</p>
          </div>
          <div className="bg-background-surface border border-border-default rounded-lg p-4 text-center">
            <p className="text-3xl font-bold text-red-primary">한자 분해</p>
            <p className="text-foreground-secondary">학습 지원</p>
          </div>
        </div>

        {/* 분야별 카드 */}
        <section className="mb-12">
          <h2 className="text-xl font-bold text-foreground mb-6">분야별 용어</h2>
          <div className="grid md:grid-cols-2 lg:grid-cols-3 gap-6">
            {domainStats.map((domain) => (
              <Link
                key={domain.slug}
                href={`/terms/${domain.slug}`}
                className="block border border-border-default rounded-lg p-6 hover:border-red-primary transition bg-background-card"
              >
                <div className="flex justify-between items-start mb-3">
                  <h3 className="text-xl font-bold text-foreground">
                    {domain.name}
                  </h3>
                  <span className="px-2 py-1 bg-background-surface text-red-primary text-sm rounded">
                    {domain.termCount}개
                  </span>
                </div>
                <p className="text-red-primary mb-3">{domain.nameVi}</p>
                <p className="text-sm text-foreground-muted mb-4">{domain.description}</p>
                <div className="flex flex-wrap gap-1">
                  {domain.keywords.slice(0, 4).map((keyword) => (
                    <span
                      key={keyword}
                      className="px-2 py-0.5 bg-background-surface text-foreground-secondary text-xs rounded"
                    >
                      {keyword}
                    </span>
                  ))}
                </div>
              </Link>
            ))}
          </div>
        </section>

        {/* CTA */}
        <section className="bg-gradient-to-r from-red-primary to-red-dark text-white rounded-lg p-8 mb-8">
          <h2 className="text-2xl font-bold mb-3">전문 통역사로 등록하세요</h2>
          <p className="text-foreground-secondary mb-6">
            한-베 통역 경험이 있다면 이력서를 등록하고 프로젝트 의뢰를 받아보세요.
            전문 분야가 있으면 더욱 환영합니다!
          </p>
          <Link
            href="/upload"
            className="inline-block bg-white text-red-primary px-6 py-3 rounded-lg font-semibold hover:bg-foreground-secondary transition"
          >
            이력서 등록하기
          </Link>
        </section>

        {/* 안내 */}
        <section className="bg-background-secondary rounded-lg p-6">
          <h3 className="font-semibold text-foreground mb-3">용어사전 활용법</h3>
          <ul className="space-y-2 text-foreground-secondary">
            <li>• 각 용어의 한자 분해로 어원을 이해하세요</li>
            <li>• 한국어-베트남어 대조 예문으로 실제 통역 표현을 익히세요</li>
            <li>• 관련 용어를 함께 학습하여 어휘력을 넓히세요</li>
            <li>• 통역 현장에서 자주 쓰이는 맥락을 확인하세요</li>
          </ul>
        </section>
      </div>

      <Footer />
    </div>
  );
}
