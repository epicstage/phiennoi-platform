import { Metadata } from "next";
import Link from "next/link";
import { domains } from "@/data/pseo-dimensions";

export const metadata: Metadata = {
  title: "통역사 이력서 등록 | 한-베 전문 통역 플랫폼",
  description:
    "한-베 전문 통역사로 등록하세요. 이력서를 업로드하면 전문 분야에 맞는 통역 의뢰를 매칭해드립니다.",
  keywords: ["통역사 등록", "베트남어 통역", "이력서 업로드", "통역 의뢰"],
};

export default function UploadPage() {
  return (
    <div className="min-h-screen bg-gray-50">
      {/* 헤더 */}
      <div className="bg-gradient-to-br from-blue-600 to-blue-800 text-white py-16 px-4">
        <div className="max-w-3xl mx-auto text-center">
          <h1 className="text-3xl md:text-4xl font-bold mb-4">
            통역사 이력서 등록
          </h1>
          <p className="text-xl text-blue-100">
            이력서를 등록하고 전문 분야 통역 의뢰를 받아보세요
          </p>
        </div>
      </div>

      {/* 메인 콘텐츠 */}
      <div className="max-w-3xl mx-auto px-4 py-12">
        {/* 혜택 */}
        <section className="bg-white rounded-2xl p-8 shadow-sm mb-8">
          <h2 className="text-xl font-bold text-gray-900 mb-6">
            등록 혜택
          </h2>
          <div className="grid md:grid-cols-2 gap-4">
            <div className="flex items-start gap-3">
              <span className="text-2xl">✅</span>
              <div>
                <h3 className="font-semibold text-gray-900">전문 분야 매칭</h3>
                <p className="text-sm text-gray-600">
                  경력에 맞는 통역 의뢰를 우선 안내
                </p>
              </div>
            </div>
            <div className="flex items-start gap-3">
              <span className="text-2xl">✅</span>
              <div>
                <h3 className="font-semibold text-gray-900">프로필 노출</h3>
                <p className="text-sm text-gray-600">
                  의뢰인에게 프로필 직접 노출
                </p>
              </div>
            </div>
            <div className="flex items-start gap-3">
              <span className="text-2xl">✅</span>
              <div>
                <h3 className="font-semibold text-gray-900">무료 등록</h3>
                <p className="text-sm text-gray-600">
                  이력서 등록 및 매칭 무료
                </p>
              </div>
            </div>
            <div className="flex items-start gap-3">
              <span className="text-2xl">✅</span>
              <div>
                <h3 className="font-semibold text-gray-900">경력 관리</h3>
                <p className="text-sm text-gray-600">
                  통역 경력 체계적 관리
                </p>
              </div>
            </div>
          </div>
        </section>

        {/* 전문 분야 선택 */}
        <section className="bg-white rounded-2xl p-8 shadow-sm mb-8">
          <h2 className="text-xl font-bold text-gray-900 mb-4">
            전문 분야 선택
          </h2>
          <p className="text-gray-600 mb-6">
            경험이 있는 분야를 선택해주세요 (복수 선택 가능)
          </p>
          <div className="grid md:grid-cols-2 gap-3">
            {domains.map((domain) => (
              <label
                key={domain.slug}
                className="flex items-center gap-3 p-4 border rounded-lg hover:border-blue-300 cursor-pointer transition"
              >
                <input
                  type="checkbox"
                  className="w-5 h-5 text-blue-600 rounded focus:ring-blue-500"
                />
                <div>
                  <span className="font-medium text-gray-900">{domain.name}</span>
                  <span className="text-blue-600 ml-2 text-sm">
                    {domain.nameVi}
                  </span>
                  <div className="text-xs text-gray-500 mt-1">
                    {domain.keywords.slice(0, 3).join(", ")}
                  </div>
                </div>
              </label>
            ))}
          </div>
        </section>

        {/* 이력서 업로드 */}
        <section className="bg-white rounded-2xl p-8 shadow-sm mb-8">
          <h2 className="text-xl font-bold text-gray-900 mb-4">
            이력서 업로드
          </h2>
          <p className="text-gray-600 mb-6">
            PDF 또는 Word 파일로 이력서를 업로드해주세요.
            AI가 자동으로 경력을 분석하여 분류합니다.
          </p>

          <div className="border-2 border-dashed border-gray-300 rounded-xl p-12 text-center hover:border-blue-400 transition cursor-pointer">
            <div className="text-5xl mb-4">📄</div>
            <p className="text-gray-700 font-medium mb-2">
              파일을 드래그하거나 클릭하여 업로드
            </p>
            <p className="text-sm text-gray-500">
              PDF, DOC, DOCX (최대 10MB)
            </p>
          </div>

          <div className="mt-6 p-4 bg-blue-50 rounded-lg">
            <h3 className="font-semibold text-blue-900 mb-2">
              📋 이력서 포함 권장 항목
            </h3>
            <ul className="text-sm text-blue-800 space-y-1">
              <li>• 통역 경력 (행사명, 기간, 분야)</li>
              <li>• 학력 (베트남 대학 졸업 시 표기)</li>
              <li>• 언어 능력 (TOPIK, VSEPR 등)</li>
              <li>• 전문 분야 (농업, 뷰티, 제조 등)</li>
            </ul>
          </div>
        </section>

        {/* 기본 정보 */}
        <section className="bg-white rounded-2xl p-8 shadow-sm mb-8">
          <h2 className="text-xl font-bold text-gray-900 mb-6">
            기본 정보
          </h2>

          <div className="space-y-4">
            <div>
              <label className="block text-sm font-medium text-gray-700 mb-1">
                이름 *
              </label>
              <input
                type="text"
                className="w-full px-4 py-3 border rounded-lg focus:ring-2 focus:ring-blue-500 focus:border-blue-500"
                placeholder="홍길동"
              />
            </div>

            <div>
              <label className="block text-sm font-medium text-gray-700 mb-1">
                이메일 *
              </label>
              <input
                type="email"
                className="w-full px-4 py-3 border rounded-lg focus:ring-2 focus:ring-blue-500 focus:border-blue-500"
                placeholder="example@email.com"
              />
            </div>

            <div>
              <label className="block text-sm font-medium text-gray-700 mb-1">
                연락처 *
              </label>
              <input
                type="tel"
                className="w-full px-4 py-3 border rounded-lg focus:ring-2 focus:ring-blue-500 focus:border-blue-500"
                placeholder="010-1234-5678"
              />
            </div>

            <div>
              <label className="block text-sm font-medium text-gray-700 mb-1">
                활동 지역
              </label>
              <select className="w-full px-4 py-3 border rounded-lg focus:ring-2 focus:ring-blue-500 focus:border-blue-500">
                <option>선택해주세요</option>
                <option>호치민</option>
                <option>하노이</option>
                <option>다낭</option>
                <option>서울/수도권</option>
                <option>부산</option>
                <option>원격 가능</option>
              </select>
            </div>
          </div>
        </section>

        {/* 제출 버튼 */}
        <button
          type="button"
          className="w-full py-4 bg-blue-600 text-white text-lg font-semibold rounded-xl hover:bg-blue-700 transition"
        >
          이력서 등록하기
        </button>

        <p className="text-center text-sm text-gray-500 mt-4">
          등록 시{" "}
          <Link href="/privacy" className="text-blue-600 hover:underline">
            개인정보처리방침
          </Link>
          에 동의합니다.
        </p>
      </div>

      {/* 푸터 링크 */}
      <div className="max-w-3xl mx-auto px-4 py-8 text-center">
        <p className="text-gray-600 mb-4">
          통역 준비가 필요하신가요?
        </p>
        <div className="flex justify-center gap-4">
          <Link
            href="/terms"
            className="text-blue-600 hover:underline font-medium"
          >
            용어사전 보기
          </Link>
          <Link
            href="/guides"
            className="text-blue-600 hover:underline font-medium"
          >
            가이드 보기
          </Link>
        </div>
      </div>
    </div>
  );
}
