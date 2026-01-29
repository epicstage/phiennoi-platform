import { Metadata } from "next";
import Link from "next/link";
import { notFound } from "next/navigation";
import { domains } from "@/data/pseo-dimensions";
import type { Term } from "@/types/term";

// 빌드 타임에 정적 페이지 생성
export async function generateStaticParams() {
  const params: { domain: string; term: string }[] = [];

  for (const domain of domains) {
    try {
      // eslint-disable-next-line @typescript-eslint/no-require-imports
      const terms = require(`@/data/terms/${domain.slug}.json`) as Term[];
      for (const term of terms) {
        params.push({
          domain: domain.slug,
          term: term.slug,
        });
      }
    } catch {
      continue;
    }
  }

  return params;
}

// 동적 메타데이터 생성
export async function generateMetadata({
  params,
}: {
  params: Promise<{ domain: string; term: string }>;
}): Promise<Metadata> {
  const { domain: domainSlug, term: termSlug } = await params;

  const domain = domains.find((d) => d.slug === domainSlug);
  if (!domain) {
    return { title: "페이지를 찾을 수 없습니다" };
  }

  let term: Term | undefined;
  try {
    // eslint-disable-next-line @typescript-eslint/no-require-imports
    const terms = require(`@/data/terms/${domainSlug}.json`) as Term[];
    term = terms.find((t) => t.slug === termSlug);
  } catch {
    return { title: "페이지를 찾을 수 없습니다" };
  }

  if (!term) {
    return { title: "페이지를 찾을 수 없습니다" };
  }

  const title = `${term.korean} 베트남어 | ${term.vietnamese} | ${domain.name} 통역 용어`;
  const description = `${term.korean}(${term.vietnamese})의 뜻과 통역 표현. ${term.meaningKo} ${domain.name} 분야 한-베 통역 필수 용어.`;

  return {
    title,
    description,
    keywords: [
      `${term.korean} 베트남어`,
      `${term.vietnamese} 뜻`,
      `${domain.name} 통역`,
      term.hanja || "",
      ...term.relatedTerms,
    ].filter(Boolean),
    openGraph: {
      title,
      description,
      type: "article",
      locale: "ko_KR",
      alternateLocale: "vi_VN",
    },
  };
}

export default async function TermPage({
  params,
}: {
  params: Promise<{ domain: string; term: string }>;
}) {
  const { domain: domainSlug, term: termSlug } = await params;

  const domain = domains.find((d) => d.slug === domainSlug);
  if (!domain) {
    notFound();
  }

  let terms: Term[] = [];
  let term: Term | undefined;

  try {
    // eslint-disable-next-line @typescript-eslint/no-require-imports
    terms = require(`@/data/terms/${domainSlug}.json`) as Term[];
    term = terms.find((t) => t.slug === termSlug);
  } catch {
    notFound();
  }

  if (!term) {
    notFound();
  }

  const relatedTerms = terms.filter((t) =>
    term.relatedTerms.includes(t.korean)
  );
  const otherTerms = terms.filter((t) => t.slug !== term.slug).slice(0, 6);

  return (
    <div className="min-h-screen bg-background">
      {/* Header */}
      <header className="sticky top-0 z-50 border-b border-border-default bg-background/95 backdrop-blur">
        <div className="max-w-7xl mx-auto px-6 h-16 flex items-center justify-between">
          <Link href="/" className="flex items-center gap-3">
            <div className="w-8 h-8 bg-red-primary rounded" />
            <span className="text-lg font-bold tracking-wide text-foreground">한베통역</span>
          </Link>
          <nav className="hidden md:flex items-center gap-8">
            <Link href="/terms" className="text-sm text-foreground-secondary hover:text-foreground transition">용어사전</Link>
            <Link href="/guides" className="text-sm text-foreground-secondary hover:text-foreground transition">통역 가이드</Link>
            <Link href="/upload" className="px-5 py-2 bg-red-primary text-white text-sm font-semibold rounded hover:bg-red-hover transition">이력서 등록</Link>
          </nav>
        </div>
      </header>

      <article className="max-w-4xl mx-auto px-6 py-10">
        {/* Breadcrumb */}
        <nav className="text-sm text-foreground-muted mb-8">
          <Link href="/" className="hover:text-foreground transition">홈</Link>
          <span className="mx-2 text-border-default">/</span>
          <Link href="/terms" className="hover:text-foreground transition">용어사전</Link>
          <span className="mx-2 text-border-default">/</span>
          <Link href={`/terms/${domain.slug}`} className="hover:text-foreground transition">{domain.name}</Link>
          <span className="mx-2 text-border-default">/</span>
          <span className="text-foreground">{term.korean}</span>
        </nav>

        {/* Header */}
        <header className="mb-10">
          <div className="flex items-center gap-2 mb-4">
            <span className="px-3 py-1 bg-red-primary/10 text-red-primary text-sm rounded-full border border-red-primary/20">
              {domain.name}
            </span>
            <span className="px-3 py-1 bg-background-surface text-foreground-secondary text-sm rounded-full border border-border-default">
              {domain.nameVi}
            </span>
          </div>

          <h1 className="text-4xl font-bold text-foreground mb-3">
            {term.korean}
          </h1>
          <p className="text-2xl text-red-primary font-medium mb-4">
            {term.vietnamese}
          </p>

          {term.hanja && (
            <div className="text-foreground-secondary">
              <span className="font-medium">한자:</span>{" "}
              <span className="text-xl text-foreground">{term.hanja}</span>
            </div>
          )}
        </header>

        {/* 한자 분해 */}
        {term.hanja && term.hanjaReading && (
          <section className="bg-background-card border border-border-default rounded-lg p-6 mb-8">
            <h2 className="text-lg font-semibold text-foreground mb-4">
              한자 분해
            </h2>
            <div className="flex flex-wrap gap-3">
              {term.hanjaReading.split(" + ").map((part, i) => (
                <div
                  key={i}
                  className="bg-background-surface rounded-lg px-4 py-2 border border-border-default"
                >
                  <span className="text-foreground-secondary">{part}</span>
                </div>
              ))}
            </div>
          </section>
        )}

        {/* 뜻 */}
        <section className="mb-8">
          <h2 className="text-xl font-bold text-foreground mb-4 pb-2 border-b border-border-default">
            뜻
          </h2>
          <div className="grid md:grid-cols-2 gap-4">
            <div className="bg-background-card border border-border-default rounded-lg p-5">
              <h3 className="text-xs font-semibold text-foreground-muted mb-2 tracking-wider uppercase">
                한국어 의미
              </h3>
              <p className="text-foreground-secondary leading-relaxed">{term.meaningKo}</p>
            </div>
            <div className="bg-background-card border border-red-primary/20 rounded-lg p-5">
              <h3 className="text-xs font-semibold text-red-primary mb-2 tracking-wider uppercase">
                Nghĩa tiếng Việt
              </h3>
              <p className="text-foreground-secondary leading-relaxed">{term.meaningVi}</p>
            </div>
          </div>
        </section>

        {/* 사용 맥락 */}
        <section className="mb-8">
          <h2 className="text-xl font-bold text-foreground mb-4 pb-2 border-b border-border-default">
            사용 맥락
          </h2>
          <p className="text-foreground-secondary bg-background-card border border-border-default rounded-lg p-5">
            {term.context}
          </p>
        </section>

        {/* 예문 */}
        <section className="mb-8">
          <h2 className="text-xl font-bold text-foreground mb-4 pb-2 border-b border-border-default">
            통역 예문
          </h2>
          <div className="space-y-4">
            {term.examples.map((example, i) => (
              <div key={i} className="border border-border-default rounded-lg overflow-hidden">
                <div className="bg-background-card p-4 border-b border-border-default">
                  <span className="text-xs font-semibold text-foreground-muted mb-1 block tracking-wider">
                    한국어
                  </span>
                  <p className="text-foreground">{example.ko}</p>
                </div>
                <div className="bg-background-surface p-4">
                  <span className="text-xs font-semibold text-red-primary mb-1 block tracking-wider">
                    Tiếng Việt
                  </span>
                  <p className="text-foreground">{example.vi}</p>
                </div>
              </div>
            ))}
          </div>
        </section>

        {/* 관련 용어 */}
        {relatedTerms.length > 0 && (
          <section className="mb-8">
            <h2 className="text-xl font-bold text-foreground mb-4 pb-2 border-b border-border-default">
              관련 용어
            </h2>
            <div className="flex flex-wrap gap-2">
              {relatedTerms.map((related) => (
                <Link
                  key={related.slug}
                  href={`/terms/${domainSlug}/${related.slug}`}
                  className="px-4 py-2 bg-background-card border border-border-default hover:border-red-primary rounded-lg text-foreground-secondary hover:text-foreground transition"
                >
                  {related.korean} ({related.vietnamese})
                </Link>
              ))}
              {term.relatedTerms
                .filter((rt) => !relatedTerms.find((r) => r.korean === rt))
                .map((rt) => (
                  <span
                    key={rt}
                    className="px-4 py-2 bg-background-surface text-foreground-muted rounded-lg"
                  >
                    {rt}
                  </span>
                ))}
            </div>
          </section>
        )}

        {/* CTA */}
        <section className="bg-background-card border border-red-primary/30 rounded-lg p-8 mb-8">
          <h2 className="text-2xl font-bold text-foreground mb-3">
            {domain.name} 전문 통역사이신가요?
          </h2>
          <p className="text-foreground-secondary mb-6">
            이력서를 등록하고 {domain.name} 분야 통역 의뢰를 받아보세요.
            {term.korean} 관련 프로젝트 경험이 있다면 더욱 환영합니다!
          </p>
          <Link
            href="/upload"
            className="inline-flex items-center gap-2 bg-red-primary text-white px-6 py-3 rounded font-semibold hover:bg-red-hover transition"
          >
            이력서 등록하기
          </Link>
        </section>

        {/* 같은 도메인 다른 용어 */}
        {otherTerms.length > 0 && (
          <section className="border-t border-border-default pt-8">
            <h2 className="text-lg font-semibold text-foreground mb-4">
              {domain.name} 분야 다른 용어
            </h2>
            <div className="grid md:grid-cols-2 lg:grid-cols-3 gap-3">
              {otherTerms.map((other) => (
                <Link
                  key={other.slug}
                  href={`/terms/${domainSlug}/${other.slug}`}
                  className="p-3 border border-border-default rounded-lg hover:border-red-primary/50 bg-background-card transition"
                >
                  <p className="font-medium text-foreground">{other.korean}</p>
                  <p className="text-sm text-red-primary">{other.vietnamese}</p>
                </Link>
              ))}
            </div>
            <div className="mt-4">
              <Link
                href={`/terms/${domainSlug}`}
                className="text-red-primary hover:underline"
              >
                {domain.name} 용어 전체보기 →
              </Link>
            </div>
          </section>
        )}
      </article>
    </div>
  );
}
