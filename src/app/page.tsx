import Link from "next/link";
import { domains, interpretTypes } from "@/data/pseo-dimensions";

export default function Home() {
  return (
    <div className="min-h-screen bg-white">
      {/* 히어로 섹션 */}
      <section className="bg-gradient-to-br from-blue-600 via-blue-700 to-blue-800 text-white">
        <div className="max-w-6xl mx-auto px-4 py-20">
          <div className="text-center mb-12">
            <h1 className="text-4xl md:text-5xl font-bold mb-6">
              한-베 전문 통역 플랫폼
            </h1>
            <p className="text-xl md:text-2xl text-blue-100 mb-8 max-w-2xl mx-auto">
              {domains.length}개 전문 분야, {domains.length * 100}+ 통역 용어
              <br />
              한자 분해와 함께 배우는 베트남어 통역
            </p>
            <div className="flex flex-col sm:flex-row gap-4 justify-center">
              <Link
                href="/upload"
                className="inline-flex items-center justify-center px-8 py-4 text-lg font-semibold bg-white text-blue-600 rounded-xl hover:bg-blue-50 transition shadow-lg"
              >
                📋 통역사 이력서 등록
              </Link>
              <Link
                href="/terms"
                className="inline-flex items-center justify-center px-8 py-4 text-lg font-semibold bg-blue-500 text-white rounded-xl hover:bg-blue-400 transition border-2 border-blue-400"
              >
                📖 용어사전 보기
              </Link>
            </div>
          </div>

          {/* 통계 */}
          <div className="grid grid-cols-2 md:grid-cols-4 gap-4 max-w-3xl mx-auto">
            <div className="bg-white/10 backdrop-blur rounded-lg p-4 text-center">
              <p className="text-3xl font-bold">{domains.length}</p>
              <p className="text-blue-200 text-sm">전문 분야</p>
            </div>
            <div className="bg-white/10 backdrop-blur rounded-lg p-4 text-center">
              <p className="text-3xl font-bold">{interpretTypes.length}</p>
              <p className="text-blue-200 text-sm">통역 유형</p>
            </div>
            <div className="bg-white/10 backdrop-blur rounded-lg p-4 text-center">
              <p className="text-3xl font-bold">90+</p>
              <p className="text-blue-200 text-sm">등록 용어</p>
            </div>
            <div className="bg-white/10 backdrop-blur rounded-lg p-4 text-center">
              <p className="text-3xl font-bold">한자</p>
              <p className="text-blue-200 text-sm">분해 학습</p>
            </div>
          </div>
        </div>
      </section>

      {/* 주요 서비스 */}
      <section className="py-16 px-4">
        <div className="max-w-6xl mx-auto">
          <h2 className="text-2xl md:text-3xl font-bold text-center text-gray-900 mb-12">
            통역사를 위한 전문 콘텐츠
          </h2>

          <div className="grid md:grid-cols-3 gap-8">
            {/* 용어사전 */}
            <div className="bg-gray-50 rounded-2xl p-8">
              <div className="w-14 h-14 bg-blue-100 rounded-xl flex items-center justify-center text-2xl mb-4">
                📖
              </div>
              <h3 className="text-xl font-bold text-gray-900 mb-3">
                분야별 용어사전
              </h3>
              <p className="text-gray-600 mb-4">
                농업, 뷰티, 제조, 법률 등 {domains.length}개 분야의 전문 용어를
                한자 분해와 함께 학습하세요.
              </p>
              <Link
                href="/terms"
                className="text-blue-600 font-medium hover:underline"
              >
                용어사전 보기 →
              </Link>
            </div>

            {/* 통역 가이드 */}
            <div className="bg-gray-50 rounded-2xl p-8">
              <div className="w-14 h-14 bg-green-100 rounded-xl flex items-center justify-center text-2xl mb-4">
                📋
              </div>
              <h3 className="text-xl font-bold text-gray-900 mb-3">
                통역 가이드
              </h3>
              <p className="text-gray-600 mb-4">
                박람회, B2B 매칭, 현장통역 등 {interpretTypes.length}가지 통역 유형별
                준비사항과 핵심 표현을 확인하세요.
              </p>
              <Link
                href="/guides"
                className="text-blue-600 font-medium hover:underline"
              >
                가이드 보기 →
              </Link>
            </div>

            {/* 이력서 등록 */}
            <div className="bg-blue-600 rounded-2xl p-8 text-white">
              <div className="w-14 h-14 bg-white/20 rounded-xl flex items-center justify-center text-2xl mb-4">
                ✨
              </div>
              <h3 className="text-xl font-bold mb-3">통역사 등록</h3>
              <p className="text-blue-100 mb-4">
                이력서를 등록하고 전문 분야 통역 의뢰를 받아보세요.
                경력에 맞는 프로젝트를 매칭해드립니다.
              </p>
              <Link
                href="/upload"
                className="inline-block bg-white text-blue-600 px-4 py-2 rounded-lg font-medium hover:bg-blue-50 transition"
              >
                이력서 등록 →
              </Link>
            </div>
          </div>
        </div>
      </section>

      {/* 분야별 미리보기 */}
      <section className="py-16 px-4 bg-gray-50">
        <div className="max-w-6xl mx-auto">
          <h2 className="text-2xl md:text-3xl font-bold text-center text-gray-900 mb-4">
            전문 분야
          </h2>
          <p className="text-center text-gray-600 mb-12">
            각 분야별 전문 용어와 통역 가이드를 확인하세요
          </p>

          <div className="grid md:grid-cols-2 lg:grid-cols-5 gap-4">
            {domains.map((domain) => (
              <Link
                key={domain.slug}
                href={`/terms/${domain.slug}`}
                className="bg-white rounded-xl p-4 hover:shadow-lg transition text-center"
              >
                <h3 className="font-bold text-gray-900 mb-1">{domain.name}</h3>
                <p className="text-blue-600 text-sm mb-2">{domain.nameVi}</p>
                <div className="flex flex-wrap justify-center gap-1">
                  {domain.keywords.slice(0, 2).map((k) => (
                    <span
                      key={k}
                      className="px-2 py-0.5 bg-gray-100 text-gray-500 text-xs rounded"
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

      {/* 통역 유형 */}
      <section className="py-16 px-4">
        <div className="max-w-6xl mx-auto">
          <h2 className="text-2xl md:text-3xl font-bold text-center text-gray-900 mb-4">
            통역 유형
          </h2>
          <p className="text-center text-gray-600 mb-12">
            유형별 맞춤 가이드로 통역을 준비하세요
          </p>

          <div className="grid md:grid-cols-2 lg:grid-cols-4 gap-4">
            {interpretTypes.map((type) => (
              <div
                key={type.slug}
                className="border rounded-xl p-4 hover:border-blue-300 transition"
              >
                <h3 className="font-bold text-gray-900 mb-1">{type.name}</h3>
                <p className="text-blue-600 text-sm mb-2">{type.nameVi}</p>
                <p className="text-gray-500 text-sm">{type.description}</p>
              </div>
            ))}
          </div>
        </div>
      </section>

      {/* CTA 섹션 */}
      <section className="py-20 px-4 bg-gradient-to-br from-blue-600 to-blue-800 text-white">
        <div className="max-w-3xl mx-auto text-center">
          <h2 className="text-3xl md:text-4xl font-bold mb-6">
            한-베 전문 통역사로 등록하세요
          </h2>
          <p className="text-xl text-blue-100 mb-8">
            이력서를 등록하면 전문 분야에 맞는 통역 의뢰를 매칭해드립니다.
            <br />
            농업, 뷰티, 제조, 법률 등 경험이 있는 분야를 선택해주세요.
          </p>
          <Link
            href="/upload"
            className="inline-flex items-center justify-center px-8 py-4 text-lg font-semibold bg-white text-blue-600 rounded-xl hover:bg-blue-50 transition shadow-lg"
          >
            📋 이력서 등록하기
          </Link>
        </div>
      </section>

      {/* 푸터 */}
      <footer className="py-8 px-4 bg-gray-900 text-gray-400">
        <div className="max-w-6xl mx-auto text-center">
          <p className="mb-4">한-베 전문 통역 플랫폼</p>
          <div className="flex justify-center gap-6 text-sm">
            <Link href="/terms" className="hover:text-white">
              용어사전
            </Link>
            <Link href="/guides" className="hover:text-white">
              가이드
            </Link>
            <Link href="/upload" className="hover:text-white">
              이력서 등록
            </Link>
          </div>
        </div>
      </footer>
    </div>
  );
}
