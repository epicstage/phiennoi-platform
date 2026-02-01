import Link from "next/link";
import { domains, interpretTypes } from "@/data/pseo-dimensions";
import Header from "@/components/Header";

export default function Home() {
  return (
    <div className="min-h-screen bg-background">
      <Header />

      {/* Hero Section */}
      <section className="py-24 md:py-32 px-6">
        <div className="max-w-4xl mx-auto text-center">
          <div className="inline-flex items-center gap-2 px-4 py-1.5 border border-red-primary rounded-full mb-8">
            <span className="w-2 h-2 bg-red-primary rounded-full" />
            <span className="text-sm font-medium text-red-primary">
              한국-베트남 전문 통역 플랫폼
            </span>
          </div>

          <h1 className="text-4xl md:text-6xl font-bold leading-tight mb-6">
            <span className="text-foreground">전문 통역이 필요한 순간,</span>
            <br />
            <span className="text-red-primary">Epic Note가 연결합니다</span>
          </h1>

          <p className="text-lg md:text-xl text-foreground-secondary mb-10 max-w-2xl mx-auto">
            {domains.length}개 전문 분야 · {interpretTypes.length}가지 통역 유형 · 2,000+ 전문 용어
          </p>

          <div className="flex flex-col sm:flex-row gap-4 justify-center">
            <Link
              href="/upload"
              className="inline-flex items-center justify-center gap-2 px-8 py-4 text-lg font-semibold bg-red-primary text-white rounded hover:bg-red-hover transition"
            >
              <svg className="w-5 h-5" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                <path strokeLinecap="round" strokeLinejoin="round" strokeWidth={2} d="M7 16a4 4 0 01-.88-7.903A5 5 0 1115.9 6L16 6a5 5 0 011 9.9M15 13l-3-3m0 0l-3 3m3-3v12" />
              </svg>
              이력서 등록하기
            </Link>
            <Link
              href="/terms"
              className="inline-flex items-center justify-center gap-2 px-8 py-4 text-lg font-medium text-foreground-secondary border border-border-default rounded hover:border-foreground-muted hover:text-foreground transition"
            >
              <svg className="w-5 h-5" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                <path strokeLinecap="round" strokeLinejoin="round" strokeWidth={2} d="M12 6.253v13m0-13C10.832 5.477 9.246 5 7.5 5S4.168 5.477 3 6.253v13C4.168 18.477 5.754 18 7.5 18s3.332.477 4.5 1.253m0-13C13.168 5.477 14.754 5 16.5 5c1.747 0 3.332.477 4.5 1.253v13C19.832 18.477 18.247 18 16.5 18c-1.746 0-3.332.477-4.5 1.253" />
              </svg>
              용어사전 둘러보기
            </Link>
          </div>

          {/* Stats */}
          <div className="grid grid-cols-2 md:grid-cols-4 gap-4 max-w-3xl mx-auto mt-16">
            <div className="bg-background-card border border-border-default rounded-lg p-5 text-center">
              <p className="text-3xl font-bold text-foreground">{domains.length}</p>
              <p className="text-foreground-muted text-sm mt-1">전문 분야</p>
            </div>
            <div className="bg-background-card border border-border-default rounded-lg p-5 text-center">
              <p className="text-3xl font-bold text-foreground">{interpretTypes.length}</p>
              <p className="text-foreground-muted text-sm mt-1">통역 유형</p>
            </div>
            <div className="bg-background-card border border-border-default rounded-lg p-5 text-center">
              <p className="text-3xl font-bold text-red-primary">2,000+</p>
              <p className="text-foreground-muted text-sm mt-1">전문 용어</p>
            </div>
            <div className="bg-background-card border border-border-default rounded-lg p-5 text-center">
              <p className="text-3xl font-bold text-foreground">한자</p>
              <p className="text-foreground-muted text-sm mt-1">분해 학습</p>
            </div>
          </div>
        </div>
      </section>

      {/* Domains Section */}
      <section className="py-20 px-6 bg-background-secondary">
        <div className="max-w-7xl mx-auto">
          <div className="text-center mb-12">
            <span className="text-xs font-semibold tracking-[0.2em] text-red-primary uppercase">
              Specialized Domains
            </span>
            <h2 className="text-3xl md:text-4xl font-bold text-foreground mt-3">
              {domains.length}개 전문 분야
            </h2>
            <p className="text-foreground-secondary mt-3">
              각 분야별 전문 용어와 통역 가이드를 제공합니다
            </p>
          </div>

          <div className="grid md:grid-cols-2 lg:grid-cols-5 gap-4">
            {domains.map((domain) => (
              <Link
                key={domain.slug}
                href={`/terms/${domain.slug}`}
                className="group bg-background-card border border-border-default rounded-lg p-5 hover:border-red-primary transition-all"
              >
                <h3 className="font-semibold text-foreground group-hover:text-red-primary transition">
                  {domain.name}
                </h3>
                <p className="text-red-primary text-sm mt-1">{domain.nameVi}</p>
                <div className="flex flex-wrap gap-1 mt-3">
                  {domain.keywords.slice(0, 2).map((k) => (
                    <span
                      key={k}
                      className="px-2 py-0.5 bg-background-surface text-foreground-muted text-xs rounded"
                    >
                      {k}
                    </span>
                  ))}
                </div>
              </Link>
            ))}
          </div>
        </div>
      </section>

      {/* Interpret Types */}
      <section className="py-20 px-6">
        <div className="max-w-7xl mx-auto">
          <div className="text-center mb-12">
            <span className="text-xs font-semibold tracking-[0.2em] text-red-primary uppercase">
              Interpretation Types
            </span>
            <h2 className="text-3xl md:text-4xl font-bold text-foreground mt-3">
              통역 유형
            </h2>
            <p className="text-foreground-secondary mt-3">
              유형별 맞춤 가이드로 통역을 준비하세요
            </p>
          </div>

          <div className="grid md:grid-cols-2 lg:grid-cols-4 gap-4">
            {interpretTypes.map((type) => (
              <div
                key={type.slug}
                className="bg-background-card border border-border-default rounded-lg p-5 hover:border-red-primary/50 transition"
              >
                <h3 className="font-semibold text-foreground">{type.name}</h3>
                <p className="text-red-primary text-sm mt-1">{type.nameVi}</p>
                <p className="text-foreground-muted text-sm mt-3">
                  {type.description}
                </p>
              </div>
            ))}
          </div>
        </div>
      </section>

      {/* CTA Section */}
      <section className="py-24 px-6 bg-background-secondary">
        <div className="max-w-3xl mx-auto text-center">
          <h2 className="text-3xl md:text-4xl font-bold text-foreground mb-6">
            지금 이력서를 등록하세요
          </h2>
          <p className="text-lg text-foreground-secondary mb-8">
            한-베 전문 통역 시장에서 기회를 잡으세요.
            <br />
            PDF, DOC, DOCX 파일을 업로드하면 됩니다.
          </p>

          <div className="flex flex-wrap justify-center gap-8 mb-10">
            <div className="flex items-center gap-2">
              <svg className="w-5 h-5 text-green-success" fill="currentColor" viewBox="0 0 20 20">
                <path fillRule="evenodd" d="M16.707 5.293a1 1 0 010 1.414l-8 8a1 1 0 01-1.414 0l-4-4a1 1 0 011.414-1.414L8 12.586l7.293-7.293a1 1 0 011.414 0z" clipRule="evenodd" />
              </svg>
              <span className="text-foreground-secondary">무료 등록</span>
            </div>
            <div className="flex items-center gap-2">
              <svg className="w-5 h-5 text-green-success" fill="currentColor" viewBox="0 0 20 20">
                <path fillRule="evenodd" d="M16.707 5.293a1 1 0 010 1.414l-8 8a1 1 0 01-1.414 0l-4-4a1 1 0 011.414-1.414L8 12.586l7.293-7.293a1 1 0 011.414 0z" clipRule="evenodd" />
              </svg>
              <span className="text-foreground-secondary">20개 전문 분야</span>
            </div>
            <div className="flex items-center gap-2">
              <svg className="w-5 h-5 text-green-success" fill="currentColor" viewBox="0 0 20 20">
                <path fillRule="evenodd" d="M16.707 5.293a1 1 0 010 1.414l-8 8a1 1 0 01-1.414 0l-4-4a1 1 0 011.414-1.414L8 12.586l7.293-7.293a1 1 0 011.414 0z" clipRule="evenodd" />
              </svg>
              <span className="text-foreground-secondary">빠른 매칭</span>
            </div>
          </div>

          <Link
            href="/upload"
            className="inline-flex items-center gap-3 px-10 py-5 text-lg font-bold bg-red-primary text-white rounded hover:bg-red-hover transition"
          >
            <svg className="w-6 h-6" fill="none" stroke="currentColor" viewBox="0 0 24 24">
              <path strokeLinecap="round" strokeLinejoin="round" strokeWidth={2} d="M7 16a4 4 0 01-.88-7.903A5 5 0 1115.9 6L16 6a5 5 0 011 9.9M15 13l-3-3m0 0l-3 3m3-3v12" />
            </svg>
            이력서 등록하기
          </Link>
        </div>
      </section>

      {/* Footer */}
      <footer className="border-t border-border-default bg-[#050505]">
        <div className="max-w-7xl mx-auto px-6 py-12">
          <div className="flex flex-col md:flex-row justify-between gap-8 mb-8">
            <div>
              <div className="flex items-center gap-2.5 mb-3">
                <div className="w-7 h-7 bg-red-primary rounded" />
                <span className="font-bold text-foreground">Epic Note</span>
              </div>
              <p className="text-sm text-foreground-muted">
                한국-베트남 전문 통역 플랫폼
              </p>
            </div>
            <div className="flex gap-16">
              <div>
                <h4 className="text-xs font-semibold text-foreground-secondary tracking-wider mb-3">
                  서비스
                </h4>
                <div className="flex flex-col gap-2.5">
                  <Link href="/terms" className="text-sm text-foreground-muted hover:text-foreground transition">
                    용어사전
                  </Link>
                  <Link href="/guides" className="text-sm text-foreground-muted hover:text-foreground transition">
                    통역 가이드
                  </Link>
                  <Link href="/upload" className="text-sm text-foreground-muted hover:text-foreground transition">
                    이력서 등록
                  </Link>
                </div>
              </div>
              <div>
                <h4 className="text-xs font-semibold text-foreground-secondary tracking-wider mb-3">
                  전문 분야
                </h4>
                <div className="flex flex-col gap-2.5">
                  <span className="text-sm text-foreground-muted">농업 · 자동차 · 뷰티 · 건설</span>
                  <span className="text-sm text-foreground-muted">교육 · 전자 · 환경 · 전시</span>
                  <span className="text-sm text-foreground-muted">금융 · 식품 · 인사 · IT 외 8개</span>
                </div>
              </div>
            </div>
          </div>
          <div className="border-t border-border-default pt-6 flex flex-col md:flex-row justify-between">
            <p className="text-xs text-foreground-muted">
              © 2026 Epic Note. All rights reserved.
            </p>
            <p className="text-xs text-foreground-muted">
              한국어 | Tiếng Việt
            </p>
          </div>
        </div>
      </footer>
    </div>
  );
}
