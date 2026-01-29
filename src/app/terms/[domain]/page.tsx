import { Metadata } from "next";
import Link from "next/link";
import { notFound } from "next/navigation";
import { domains } from "@/data/pseo-dimensions";
import type { Term } from "@/types/term";
import Header from "@/components/Header";
import Footer from "@/components/Footer";

// 정적 페이지 생성 - 도메인 목록
export function generateStaticParams() {
  return domains.map((domain) => ({
    domain: domain.slug,
  }));
}

// 동적 메타데이터
export async function generateMetadata({
  params,
}: {
  params: Promise<{ domain: string }>;
}): Promise<Metadata> {
  const { domain: domainSlug } = await params;
  const domain = domains.find((d) => d.slug === domainSlug);

  if (!domain) {
    return { title: "페이지를 찾을 수 없습니다" };
  }

  const title = `${domain.name} 통역 용어사전 | 한-베 ${domain.name} 전문 용어`;
  const description = `${domain.name} 분야 한국어-베트남어 통역 필수 용어 모음. ${domain.keywords.join(", ")} 등 ${domain.name} 통역에 필요한 전문 용어를 한자 분해와 함께 학습하세요.`;

  return {
    title,
    description,
    keywords: [
      `${domain.name} 통역`,
      `${domain.name} 베트남어`,
      `${domain.nameVi}`,
      ...domain.keywords.map((k) => `${k} 베트남어`),
    ],
    openGraph: {
      title,
      description,
      type: "website",
    },
  };
}

export default async function DomainTermsPage({
  params,
}: {
  params: Promise<{ domain: string }>;
}) {
  const { domain: domainSlug } = await params;
  const domain = domains.find((d) => d.slug === domainSlug);

  if (!domain) {
    notFound();
  }

  let terms: Term[] = [];
  try {
    // eslint-disable-next-line @typescript-eslint/no-require-imports
    terms = require(`@/data/terms/${domainSlug}.json`) as Term[];
  } catch {
    // 데이터가 없으면 빈 배열
    terms = [];
  }

  // 다른 도메인들
  const otherDomains = domains.filter((d) => d.slug !== domainSlug);

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
          <Link href="/terms" className="hover:text-red-primary">
            용어사전
          </Link>
          <span className="mx-2">/</span>
          <span className="text-foreground">{domain.name}</span>
        </nav>

        {/* 헤더 */}
        <header className="mb-8">
          <div className="flex items-center gap-3 mb-4">
            <h1 className="text-3xl font-bold text-foreground">
              {domain.name} 통역 용어사전
            </h1>
            <span className="px-3 py-1 bg-background-surface text-red-primary text-sm rounded-full">
              {domain.nameVi}
            </span>
          </div>
          <p className="text-foreground-secondary text-lg">{domain.description}</p>
          <div className="flex flex-wrap gap-2 mt-4">
            {domain.keywords.map((keyword) => (
              <span
                key={keyword}
                className="px-3 py-1 bg-background-surface text-foreground-secondary text-sm rounded-full"
              >
                #{keyword}
              </span>
            ))}
          </div>
        </header>

        {/* 용어 수 */}
        <div className="bg-background-surface border border-border-default rounded-lg p-4 mb-8">
          <p className="text-foreground-secondary">
            <span className="font-bold text-2xl text-red-primary">{terms.length}</span>개의{" "}
            {domain.name} 전문 용어가 등록되어 있습니다.
          </p>
        </div>

        {/* 용어 목록 */}
        {terms.length > 0 ? (
          <section className="mb-12">
            <h2 className="text-xl font-bold text-foreground mb-4">
              전체 용어 목록
            </h2>
            <div className="grid md:grid-cols-2 lg:grid-cols-3 gap-4">
              {terms.map((term) => (
                <Link
                  key={term.slug}
                  href={`/terms/${domainSlug}/${term.slug}`}
                  className="block p-4 border border-border-default rounded-lg hover:border-red-primary transition bg-background-card"
                >
                  <div className="flex justify-between items-start mb-2">
                    <h3 className="font-bold text-foreground text-lg">
                      {term.korean}
                    </h3>
                    {term.hanja && (
                      <span className="text-sm text-foreground-muted">
                        {term.hanja}
                      </span>
                    )}
                  </div>
                  <p className="text-red-primary font-medium mb-2">
                    {term.vietnamese}
                  </p>
                  <p className="text-sm text-foreground-muted line-clamp-2">
                    {term.meaningKo}
                  </p>
                </Link>
              ))}
            </div>
          </section>
        ) : (
          <section className="mb-12 text-center py-12 bg-background-secondary rounded-lg">
            <p className="text-foreground-muted">
              아직 등록된 용어가 없습니다. 곧 업데이트 예정입니다.
            </p>
          </section>
        )}

        {/* CTA */}
        <section className="bg-gradient-to-r from-red-primary to-red-dark text-white rounded-lg p-8 mb-12">
          <h2 className="text-2xl font-bold mb-3">
            {domain.name} 전문 통역사이신가요?
          </h2>
          <p className="text-foreground-secondary mb-6">
            {domain.name} 분야 통역 경험이 있다면 이력서를 등록해주세요.
            관련 프로젝트 의뢰를 매칭해드립니다.
          </p>
          <Link
            href="/upload"
            className="inline-block bg-white text-red-primary px-6 py-3 rounded-lg font-semibold hover:bg-foreground-secondary transition"
          >
            이력서 등록하기
          </Link>
        </section>

        {/* 다른 분야 */}
        <section className="border-t border-border-default pt-8">
          <h2 className="text-lg font-semibold text-foreground mb-4">
            다른 분야 용어사전
          </h2>
          <div className="flex flex-wrap gap-3">
            {otherDomains.map((d) => (
              <Link
                key={d.slug}
                href={`/terms/${d.slug}`}
                className="px-4 py-2 bg-background-surface hover:bg-background-card rounded-lg text-foreground-secondary transition"
              >
                {d.name} ({d.nameVi})
              </Link>
            ))}
          </div>
        </section>
      </div>

      <Footer />
    </div>
  );
}
