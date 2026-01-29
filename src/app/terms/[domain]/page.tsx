import { Metadata } from "next";
import Link from "next/link";
import { notFound } from "next/navigation";
import { domains } from "@/data/pseo-dimensions";
import type { Term } from "@/types/term";

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
    <div className="max-w-6xl mx-auto px-4 py-8">
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
        <span className="text-gray-900">{domain.name}</span>
      </nav>

      {/* 헤더 */}
      <header className="mb-8">
        <div className="flex items-center gap-3 mb-4">
          <h1 className="text-3xl font-bold text-gray-900">
            {domain.name} 통역 용어사전
          </h1>
          <span className="px-3 py-1 bg-blue-100 text-blue-800 text-sm rounded-full">
            {domain.nameVi}
          </span>
        </div>
        <p className="text-gray-600 text-lg">{domain.description}</p>
        <div className="flex flex-wrap gap-2 mt-4">
          {domain.keywords.map((keyword) => (
            <span
              key={keyword}
              className="px-3 py-1 bg-gray-100 text-gray-600 text-sm rounded-full"
            >
              #{keyword}
            </span>
          ))}
        </div>
      </header>

      {/* 용어 수 */}
      <div className="bg-blue-50 border border-blue-200 rounded-lg p-4 mb-8">
        <p className="text-blue-800">
          <span className="font-bold text-2xl">{terms.length}</span>개의{" "}
          {domain.name} 전문 용어가 등록되어 있습니다.
        </p>
      </div>

      {/* 용어 목록 */}
      {terms.length > 0 ? (
        <section className="mb-12">
          <h2 className="text-xl font-bold text-gray-900 mb-4">
            전체 용어 목록
          </h2>
          <div className="grid md:grid-cols-2 lg:grid-cols-3 gap-4">
            {terms.map((term) => (
              <Link
                key={term.slug}
                href={`/terms/${domainSlug}/${term.slug}`}
                className="block p-4 border rounded-lg hover:border-blue-300 hover:shadow-md transition"
              >
                <div className="flex justify-between items-start mb-2">
                  <h3 className="font-bold text-gray-900 text-lg">
                    {term.korean}
                  </h3>
                  {term.hanja && (
                    <span className="text-sm text-gray-400">
                      {term.hanja}
                    </span>
                  )}
                </div>
                <p className="text-blue-600 font-medium mb-2">
                  {term.vietnamese}
                </p>
                <p className="text-sm text-gray-500 line-clamp-2">
                  {term.meaningKo}
                </p>
              </Link>
            ))}
          </div>
        </section>
      ) : (
        <section className="mb-12 text-center py-12 bg-gray-50 rounded-lg">
          <p className="text-gray-500">
            아직 등록된 용어가 없습니다. 곧 업데이트 예정입니다.
          </p>
        </section>
      )}

      {/* CTA */}
      <section className="bg-gradient-to-r from-blue-600 to-blue-700 text-white rounded-xl p-8 mb-12">
        <h2 className="text-2xl font-bold mb-3">
          {domain.name} 전문 통역사이신가요?
        </h2>
        <p className="text-blue-100 mb-6">
          {domain.name} 분야 통역 경험이 있다면 이력서를 등록해주세요.
          관련 프로젝트 의뢰를 매칭해드립니다.
        </p>
        <Link
          href="/upload"
          className="inline-block bg-white text-blue-600 px-6 py-3 rounded-lg font-semibold hover:bg-blue-50 transition"
        >
          📋 이력서 등록하기
        </Link>
      </section>

      {/* 다른 분야 */}
      <section className="border-t pt-8">
        <h2 className="text-lg font-semibold text-gray-900 mb-4">
          다른 분야 용어사전
        </h2>
        <div className="flex flex-wrap gap-3">
          {otherDomains.map((d) => (
            <Link
              key={d.slug}
              href={`/terms/${d.slug}`}
              className="px-4 py-2 bg-gray-100 hover:bg-gray-200 rounded-lg text-gray-700 transition"
            >
              {d.name} ({d.nameVi})
            </Link>
          ))}
        </div>
      </section>
    </div>
  );
}
