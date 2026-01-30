import { Metadata } from "next";
import Link from "next/link";
import { notFound } from "next/navigation";
import { domains, interpretTypes } from "@/data/pseo-dimensions";
import type { Term } from "@/types/term";
import Header from "@/components/Header";
import Footer from "@/components/Footer";
import TermSchema from "@/components/schema/TermSchema";

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
  const description = `${term.korean}(${term.vietnamese})의 뜻과 통역 표현. ${term.meaningKo.slice(0, 100)} ${domain.name} 분야 한-베 통역 필수 용어.`;

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
    alternates: {
      canonical: `https://vn.epicstage.co.kr/terms/${domainSlug}/${termSlug}`,
    },
    openGraph: {
      title,
      description,
      type: "article",
      locale: "ko_KR",
      alternateLocale: "vi_VN",
      url: `https://vn.epicstage.co.kr/terms/${domainSlug}/${termSlug}`,
    },
    twitter: {
      card: "summary",
      title,
      description,
    },
  };
}

const difficultyLabel = {
  beginner: { text: "초급", color: "text-green-success" },
  intermediate: { text: "중급", color: "text-yellow-400" },
  advanced: { text: "고급", color: "text-red-primary" },
};

const situationLabel: Record<string, string> = {
  formal: "공식",
  informal: "비공식",
  document: "문서",
  meeting: "회의",
  onsite: "현장",
};

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
  const otherTerms = terms.filter((t) => t.slug !== term.slug).slice(0, 8);

  return (
    <div className="min-h-screen bg-background">
      <TermSchema
        term={term}
        domainName={domain.name}
        domainNameVi={domain.nameVi}
        domainSlug={domain.slug}
      />

      <Header />

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
          <div className="flex flex-wrap items-center gap-2 mb-4">
            <span className="px-3 py-1 bg-red-primary/10 text-red-primary text-sm rounded-full border border-red-primary/20">
              {domain.name}
            </span>
            <span className="px-3 py-1 bg-background-surface text-foreground-secondary text-sm rounded-full border border-border-default">
              {domain.nameVi}
            </span>
            {term.difficulty && (
              <span className={`px-3 py-1 bg-background-surface text-sm rounded-full border border-border-default ${difficultyLabel[term.difficulty].color}`}>
                {difficultyLabel[term.difficulty].text}
              </span>
            )}
            {term.frequency && (
              <span className="px-3 py-1 bg-background-surface text-foreground-muted text-sm rounded-full border border-border-default">
                빈도 {"★".repeat(term.frequency)}{"☆".repeat(5 - term.frequency)}
              </span>
            )}
            {term.formalLevel && (
              <span className="px-3 py-1 bg-background-surface text-foreground-muted text-sm rounded-full border border-border-default">
                {term.formalLevel === "formal" ? "격식" : term.formalLevel === "informal" ? "비격식" : term.formalLevel === "document" ? "문서" : "중립"}
              </span>
            )}
          </div>

          <h1 className="text-4xl font-bold text-foreground mb-3">
            {term.korean}
          </h1>
          <div className="flex flex-wrap items-baseline gap-4 mb-4">
            <p className="text-2xl text-red-primary font-medium">
              {term.vietnamese}
            </p>
            {term.pronunciation && (
              <p className="text-lg text-foreground-muted">
                [{term.pronunciation}]
              </p>
            )}
          </div>

          {term.hanja && (
            <div className="text-foreground-secondary">
              <span className="font-medium">한자:</span>{" "}
              <span className="text-xl text-foreground">{term.hanja}</span>
            </div>
          )}

          {/* 동의어 */}
          {((term.synonyms && term.synonyms.length > 0) || (term.synonymsVi && term.synonymsVi.length > 0)) && (
            <div className="mt-3 flex flex-wrap gap-2 text-sm">
              {term.synonyms && term.synonyms.length > 0 && (
                <span className="text-foreground-muted">
                  동의어: {term.synonyms.join(", ")}
                </span>
              )}
              {term.synonymsVi && term.synonymsVi.length > 0 && (
                <span className="text-foreground-muted">
                  | Từ đồng nghĩa: {term.synonymsVi.join(", ")}
                </span>
              )}
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
          <div className="space-y-3">
            <div className="bg-background-card border border-border-default rounded-lg p-5">
              <p className="text-foreground-secondary leading-relaxed">{term.context}</p>
            </div>
            {term.contextVi && (
              <div className="bg-background-card border border-red-primary/20 rounded-lg p-5">
                <h3 className="text-xs font-semibold text-red-primary mb-2 tracking-wider uppercase">
                  Bối cảnh sử dụng
                </h3>
                <p className="text-foreground-secondary leading-relaxed">{term.contextVi}</p>
              </div>
            )}
          </div>
        </section>

        {/* 통역 예문 */}
        <section className="mb-8">
          <h2 className="text-xl font-bold text-foreground mb-4 pb-2 border-b border-border-default">
            통역 예문
          </h2>
          <div className="space-y-4">
            {term.examples.map((example, i) => (
              <div key={i} className="border border-border-default rounded-lg overflow-hidden">
                {example.situation && (
                  <div className="bg-background-surface px-4 py-2 border-b border-border-default">
                    <span className="text-xs font-semibold text-foreground-muted tracking-wider uppercase">
                      {situationLabel[example.situation] || example.situation}
                    </span>
                  </div>
                )}
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

        {/* 흔한 실수 */}
        {term.commonMistakes && term.commonMistakes.length > 0 && (
          <section className="mb-8">
            <h2 className="text-xl font-bold text-foreground mb-4 pb-2 border-b border-border-default">
              ⚠ 흔한 통역 실수
            </h2>
            <div className="bg-background-card border border-red-primary/20 rounded-lg p-5">
              <ul className="space-y-3">
                {term.commonMistakes.map((mistake: string | { mistake: string; correction: string; explanation: string }, i: number) => (
                  <li key={i} className="flex items-start gap-3 text-foreground-secondary">
                    <span className="text-red-primary shrink-0 mt-0.5">✗</span>
                    {typeof mistake === "string" ? (
                      <span>{mistake}</span>
                    ) : (
                      <div>
                        <p className="font-medium text-red-primary">{mistake.mistake}</p>
                        <p className="text-green-500 mt-1">→ {mistake.correction}</p>
                        <p className="text-foreground-tertiary text-sm mt-1">{mistake.explanation}</p>
                      </div>
                    )}
                  </li>
                ))}
              </ul>
            </div>
          </section>
        )}

        {/* 문화적 차이 */}
        {term.culturalNote && (
          <section className="mb-8">
            <h2 className="text-xl font-bold text-foreground mb-4 pb-2 border-b border-border-default">
              문화 노트
            </h2>
            <div className="bg-background-card border-l-4 border-red-primary rounded-lg p-5">
              <p className="text-foreground-secondary leading-relaxed">{term.culturalNote}</p>
            </div>
          </section>
        )}

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

        {/* 관련 가이드 링크 (내부 링크 강화) */}
        <section className="mb-8">
          <h2 className="text-xl font-bold text-foreground mb-4 pb-2 border-b border-border-default">
            {domain.name} 통역 가이드
          </h2>
          <div className="grid md:grid-cols-2 gap-3">
            {interpretTypes.slice(0, 4).map((type) => (
              <Link
                key={type.slug}
                href={`/guides/${domainSlug}/${type.slug}`}
                className="p-4 border border-border-default rounded-lg hover:border-red-primary/50 bg-background-card transition"
              >
                <p className="font-medium text-foreground">{domain.name} {type.name}</p>
                <p className="text-sm text-red-primary">{type.nameVi}</p>
                <p className="text-xs text-foreground-muted mt-1">{type.description}</p>
              </Link>
            ))}
          </div>
          <div className="mt-3">
            <Link
              href={`/guides/${domainSlug}`}
              className="text-red-primary hover:underline text-sm"
            >
              {domain.name} 가이드 전체보기 →
            </Link>
          </div>
        </section>

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
            <div className="grid md:grid-cols-2 lg:grid-cols-4 gap-3">
              {otherTerms.map((other) => (
                <Link
                  key={other.slug}
                  href={`/terms/${domainSlug}/${other.slug}`}
                  className="p-3 border border-border-default rounded-lg hover:border-red-primary/50 bg-background-card transition"
                >
                  <p className="font-medium text-foreground">{other.korean}</p>
                  <p className="text-sm text-red-primary">{other.vietnamese}</p>
                  {other.pronunciation && (
                    <p className="text-xs text-foreground-muted mt-1">[{other.pronunciation}]</p>
                  )}
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

      <Footer />
    </div>
  );
}
