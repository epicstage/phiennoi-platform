import { Metadata } from "next";
import Link from "next/link";
import { domains, interpretTypes } from "@/data/pseo-dimensions";

export const metadata: Metadata = {
  title: "한-베 통역 가이드 | 분야별 통역 준비 가이드",
  description:
    "한국어-베트남어 통역 가이드 모음. 농업, 뷰티, 제조, 법률, IT 등 분야별, 통역 유형별 준비사항과 핵심 표현을 확인하세요.",
  keywords: [
    "베트남어 통역 가이드",
    "한베 통역",
    "통역 준비",
    ...domains.flatMap((d) => [d.name, d.nameVi]),
    ...interpretTypes.map((t) => t.name),
  ],
};

export default function GuidesIndexPage() {
  return (
    <div className="max-w-6xl mx-auto px-4 py-8">
      {/* Breadcrumb */}
      <nav className="text-sm text-gray-500 mb-6">
        <Link href="/" className="hover:text-blue-600">
          홈
        </Link>
        <span className="mx-2">/</span>
        <span className="text-gray-900">가이드</span>
      </nav>

      {/* 헤더 */}
      <header className="mb-8">
        <h1 className="text-3xl font-bold text-gray-900 mb-4">한-베 통역 가이드</h1>
        <p className="text-gray-600 text-lg">
          한국어-베트남어 통역을 준비하는 분들을 위한 분야별, 유형별 가이드입니다.
        </p>
      </header>

      {/* 통계 */}
      <div className="grid md:grid-cols-3 gap-4 mb-8">
        <div className="bg-blue-50 border border-blue-200 rounded-lg p-4 text-center">
          <p className="text-3xl font-bold text-blue-600">
            {domains.length * interpretTypes.length}
          </p>
          <p className="text-blue-800">가이드 페이지</p>
        </div>
        <div className="bg-green-50 border border-green-200 rounded-lg p-4 text-center">
          <p className="text-3xl font-bold text-green-600">{domains.length}</p>
          <p className="text-green-800">전문 분야</p>
        </div>
        <div className="bg-purple-50 border border-purple-200 rounded-lg p-4 text-center">
          <p className="text-3xl font-bold text-purple-600">{interpretTypes.length}</p>
          <p className="text-purple-800">통역 유형</p>
        </div>
      </div>

      {/* 분야별 선택 */}
      <section className="mb-12">
        <h2 className="text-xl font-bold text-gray-900 mb-6">분야별 가이드</h2>
        <div className="grid md:grid-cols-2 lg:grid-cols-3 gap-6">
          {domains.map((domain) => (
            <Link
              key={domain.slug}
              href={`/guides/${domain.slug}`}
              className="block border rounded-xl p-6 hover:border-blue-300 hover:shadow-lg transition"
            >
              <h3 className="text-xl font-bold text-gray-900 mb-2">{domain.name}</h3>
              <p className="text-blue-600 mb-3">{domain.nameVi}</p>
              <p className="text-sm text-gray-500 mb-4">{domain.description}</p>
              <div className="flex flex-wrap gap-1">
                {domain.keywords.slice(0, 3).map((keyword) => (
                  <span
                    key={keyword}
                    className="px-2 py-0.5 bg-gray-100 text-gray-600 text-xs rounded"
                  >
                    {keyword}
                  </span>
                ))}
              </div>
            </Link>
          ))}
        </div>
      </section>

      {/* 통역 유형별 선택 */}
      <section className="mb-12">
        <h2 className="text-xl font-bold text-gray-900 mb-6">통역 유형별 가이드</h2>
        <div className="grid md:grid-cols-2 lg:grid-cols-4 gap-4">
          {interpretTypes.map((type) => (
            <div key={type.slug} className="border rounded-lg p-4">
              <h3 className="font-bold text-gray-900 mb-1">{type.name}</h3>
              <p className="text-blue-600 text-sm mb-2">{type.nameVi}</p>
              <p className="text-xs text-gray-500">{type.description}</p>
            </div>
          ))}
        </div>
      </section>

      {/* 인기 조합 */}
      <section className="mb-12">
        <h2 className="text-xl font-bold text-gray-900 mb-6">인기 가이드</h2>
        <div className="flex flex-wrap gap-3">
          {[
            { domain: "agriculture", type: "b2b", label: "농업 B2B 매칭" },
            { domain: "beauty", type: "exhibition", label: "뷰티 박람회" },
            { domain: "manufacturing", type: "onsite", label: "제조 현장통역" },
            { domain: "legal", type: "consecutive", label: "법률 순차통역" },
            { domain: "exhibition", type: "exhibition", label: "박람회 통역" },
            { domain: "it", type: "phone", label: "IT 화상통역" },
          ].map((item) => (
            <Link
              key={`${item.domain}-${item.type}`}
              href={`/guides/${item.domain}/${item.type}`}
              className="px-4 py-2 bg-blue-100 hover:bg-blue-200 text-blue-800 rounded-lg transition"
            >
              {item.label}
            </Link>
          ))}
        </div>
      </section>

      {/* CTA */}
      <section className="bg-gradient-to-r from-blue-600 to-blue-700 text-white rounded-xl p-8 mb-8">
        <h2 className="text-2xl font-bold mb-3">전문 통역사로 등록하세요</h2>
        <p className="text-blue-100 mb-6">
          한-베 통역 경험이 있다면 이력서를 등록하고 프로젝트 의뢰를 받아보세요.
          전문 분야가 있으면 더욱 환영합니다!
        </p>
        <Link
          href="/upload"
          className="inline-block bg-white text-blue-600 px-6 py-3 rounded-lg font-semibold hover:bg-blue-50 transition"
        >
          📋 이력서 등록하기
        </Link>
      </section>

      {/* 용어사전 연결 */}
      <section className="bg-gray-50 rounded-lg p-6">
        <h3 className="font-semibold text-gray-900 mb-3">📖 용어사전도 함께 확인하세요</h3>
        <p className="text-gray-600 mb-4">
          분야별 전문 용어를 한자 분해와 함께 학습할 수 있습니다.
        </p>
        <Link href="/terms" className="text-blue-600 hover:underline font-medium">
          → 용어사전 바로가기
        </Link>
      </section>
    </div>
  );
}
