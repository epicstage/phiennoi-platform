import { Metadata } from "next";
import Link from "next/link";
import { notFound } from "next/navigation";
import { domains, interpretTypes } from "@/data/pseo-dimensions";

// 도메인별 가이드 목록 페이지 생성
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

  const title = `${domain.name} 통역 가이드 | 한-베 ${domain.name} 통역`;
  const description = `${domain.name} 분야 한국어-베트남어 통역 가이드 모음. ${domain.keywords.join(", ")} 등 ${domain.name} 통역 유형별 준비사항과 팁을 확인하세요.`;

  return {
    title,
    description,
    keywords: [
      `${domain.name} 통역`,
      `${domain.name} 베트남어`,
      `${domain.nameVi}`,
      ...domain.keywords.map((k) => `${k} 통역`),
    ],
    openGraph: {
      title,
      description,
      type: "website",
    },
  };
}

export default async function DomainGuidesPage({
  params,
}: {
  params: Promise<{ domain: string }>;
}) {
  const { domain: domainSlug } = await params;
  const domain = domains.find((d) => d.slug === domainSlug);

  if (!domain) {
    notFound();
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
        <Link href="/guides" className="hover:text-blue-600">
          가이드
        </Link>
        <span className="mx-2">/</span>
        <span className="text-gray-900">{domain.name}</span>
      </nav>

      {/* 헤더 */}
      <header className="mb-8">
        <div className="flex items-center gap-3 mb-4">
          <h1 className="text-3xl font-bold text-gray-900">
            {domain.name} 통역 가이드
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

      {/* 통역 유형별 가이드 카드 */}
      <section className="mb-12">
        <h2 className="text-xl font-bold text-gray-900 mb-6">통역 유형별 가이드</h2>
        <div className="grid md:grid-cols-2 gap-6">
          {interpretTypes.map((type) => (
            <Link
              key={type.slug}
              href={`/guides/${domainSlug}/${type.slug}`}
              className="block border rounded-xl p-6 hover:border-blue-300 hover:shadow-lg transition"
            >
              <h3 className="text-xl font-bold text-gray-900 mb-2">
                {domain.name} {type.name}
              </h3>
              <p className="text-blue-600 mb-3">{type.nameVi}</p>
              <p className="text-sm text-gray-500">{type.description}</p>
            </Link>
          ))}
        </div>
      </section>

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

      {/* 용어사전 링크 */}
      <section className="bg-amber-50 border border-amber-200 rounded-lg p-6 mb-8">
        <h3 className="font-semibold text-amber-900 mb-2">
          📖 {domain.name} 용어사전도 확인하세요
        </h3>
        <p className="text-amber-800 mb-4">
          {domain.name} 분야 전문 용어를 한자 분해와 함께 학습할 수 있습니다.
        </p>
        <Link
          href={`/terms/${domainSlug}`}
          className="text-amber-700 font-medium hover:underline"
        >
          → {domain.name} 용어사전 보기
        </Link>
      </section>

      {/* 다른 분야 */}
      <section className="border-t pt-8">
        <h2 className="text-lg font-semibold text-gray-900 mb-4">다른 분야 가이드</h2>
        <div className="flex flex-wrap gap-3">
          {otherDomains.map((d) => (
            <Link
              key={d.slug}
              href={`/guides/${d.slug}`}
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
