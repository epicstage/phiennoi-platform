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
      // 해당 도메인의 데이터가 없으면 스킵
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

  // 관련 용어 찾기
  const relatedTerms = terms.filter((t) =>
    term.relatedTerms.includes(t.slug)
  );

  // 같은 도메인의 다른 용어 (최대 6개)
  const otherTerms = terms
    .filter((t) => t.slug !== term.slug)
    .slice(0, 6);

  return (
    <article className="max-w-4xl mx-auto px-4 py-8">
      {/* Breadcrumb */}
      <nav className="text-sm text-gray-500 mb-6">
        <Link href="/" className="hover:text-blue-600">
          홈
        </Link>
        <span className="mx-2">/</span>
        <Link href="/terms" className="hover:text-blue-600">
          용어사전
        </Link>
        <span className="mx-2">/</span>
        <Link
          href={`/terms/${domain.slug}`}
          className="hover:text-blue-600"
        >
          {domain.name}
        </Link>
        <span className="mx-2">/</span>
        <span className="text-gray-900">{term.korean}</span>
      </nav>

      {/* 헤더 */}
      <header className="mb-8">
        <div className="flex items-center gap-2 mb-2">
          <span className="px-3 py-1 bg-blue-100 text-blue-800 text-sm rounded-full">
            {domain.name}
          </span>
          <span className="px-3 py-1 bg-green-100 text-green-800 text-sm rounded-full">
            {domain.nameVi}
          </span>
        </div>

        <h1 className="text-4xl font-bold text-gray-900 mb-2">
          {term.korean}
        </h1>

        <p className="text-2xl text-blue-600 font-medium mb-4">
          {term.vietnamese}
        </p>

        {term.hanja && (
          <div className="text-gray-600">
            <span className="font-medium">한자:</span>{" "}
            <span className="text-xl">{term.hanja}</span>
          </div>
        )}
      </header>

      {/* 한자 분해 (있는 경우) */}
      {term.hanja && term.hanjaReading && (
        <section className="bg-amber-50 border border-amber-200 rounded-lg p-6 mb-8">
          <h2 className="text-lg font-semibold text-amber-900 mb-3">
            📖 한자 분해
          </h2>
          <div className="flex flex-wrap gap-4">
            {term.hanjaReading.split(" + ").map((part, i) => (
              <div
                key={i}
                className="bg-white rounded-lg px-4 py-2 border border-amber-200"
              >
                <span className="text-amber-800">{part}</span>
              </div>
            ))}
          </div>
        </section>
      )}

      {/* 뜻 */}
      <section className="mb-8">
        <h2 className="text-xl font-bold text-gray-900 mb-4 pb-2 border-b">
          📝 뜻
        </h2>
        <div className="grid md:grid-cols-2 gap-6">
          <div className="bg-gray-50 rounded-lg p-4">
            <h3 className="text-sm font-medium text-gray-500 mb-2">
              한국어 의미
            </h3>
            <p className="text-gray-800">{term.meaningKo}</p>
          </div>
          <div className="bg-blue-50 rounded-lg p-4">
            <h3 className="text-sm font-medium text-blue-600 mb-2">
              Nghĩa tiếng Việt
            </h3>
            <p className="text-gray-800">{term.meaningVi}</p>
          </div>
        </div>
      </section>

      {/* 사용 맥락 */}
      <section className="mb-8">
        <h2 className="text-xl font-bold text-gray-900 mb-4 pb-2 border-b">
          🎯 사용 맥락
        </h2>
        <p className="text-gray-700 bg-gray-50 rounded-lg p-4">
          {term.context}
        </p>
      </section>

      {/* 예문 */}
      <section className="mb-8">
        <h2 className="text-xl font-bold text-gray-900 mb-4 pb-2 border-b">
          💬 통역 예문
        </h2>
        <div className="space-y-4">
          {term.examples.map((example, i) => (
            <div
              key={i}
              className="border rounded-lg overflow-hidden"
            >
              <div className="bg-gray-50 p-4 border-b">
                <span className="text-xs font-medium text-gray-500 mb-1 block">
                  한국어
                </span>
                <p className="text-gray-900">{example.ko}</p>
              </div>
              <div className="bg-blue-50 p-4">
                <span className="text-xs font-medium text-blue-600 mb-1 block">
                  Tiếng Việt
                </span>
                <p className="text-gray-900">{example.vi}</p>
              </div>
            </div>
          ))}
        </div>
      </section>

      {/* 관련 용어 */}
      {relatedTerms.length > 0 && (
        <section className="mb-8">
          <h2 className="text-xl font-bold text-gray-900 mb-4 pb-2 border-b">
            🔗 관련 용어
          </h2>
          <div className="flex flex-wrap gap-2">
            {relatedTerms.map((related) => (
              <Link
                key={related.slug}
                href={`/terms/${domainSlug}/${related.slug}`}
                className="px-4 py-2 bg-gray-100 hover:bg-gray-200 rounded-lg text-gray-700 transition"
              >
                {related.korean} ({related.vietnamese})
              </Link>
            ))}
            {/* 링크 없는 관련 용어도 표시 */}
            {term.relatedTerms
              .filter((rt) => !relatedTerms.find((r) => r.slug === rt))
              .map((rt) => (
                <span
                  key={rt}
                  className="px-4 py-2 bg-gray-50 text-gray-500 rounded-lg"
                >
                  {rt}
                </span>
              ))}
          </div>
        </section>
      )}

      {/* CTA: 통역사 등록 */}
      <section className="bg-gradient-to-r from-blue-600 to-blue-700 text-white rounded-xl p-8 mb-8">
        <h2 className="text-2xl font-bold mb-3">
          {domain.name} 전문 통역사이신가요?
        </h2>
        <p className="text-blue-100 mb-6">
          이력서를 등록하고 {domain.name} 분야 통역 의뢰를 받아보세요.
          {term.korean} 관련 프로젝트 경험이 있다면 더욱 환영합니다!
        </p>
        <Link
          href="/upload"
          className="inline-block bg-white text-blue-600 px-6 py-3 rounded-lg font-semibold hover:bg-blue-50 transition"
        >
          📋 이력서 등록하기
        </Link>
      </section>

      {/* 같은 도메인의 다른 용어 */}
      {otherTerms.length > 0 && (
        <section className="border-t pt-8">
          <h2 className="text-lg font-semibold text-gray-900 mb-4">
            {domain.name} 분야 다른 용어
          </h2>
          <div className="grid md:grid-cols-2 lg:grid-cols-3 gap-3">
            {otherTerms.map((other) => (
              <Link
                key={other.slug}
                href={`/terms/${domainSlug}/${other.slug}`}
                className="p-3 border rounded-lg hover:border-blue-300 hover:bg-blue-50 transition"
              >
                <p className="font-medium text-gray-900">{other.korean}</p>
                <p className="text-sm text-blue-600">{other.vietnamese}</p>
              </Link>
            ))}
          </div>
          <div className="mt-4">
            <Link
              href={`/terms/${domainSlug}`}
              className="text-blue-600 hover:underline"
            >
              {domain.name} 용어 전체보기 →
            </Link>
          </div>
        </section>
      )}
    </article>
  );
}
