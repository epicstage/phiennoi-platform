'use client';

import Link from 'next/link';
import { ArrowLeft } from 'lucide-react';

export default function TermsPage() {
  return (
    <div className="min-h-screen bg-[#0f0f0f]">
      {/* Header */}
      <header className="bg-[#1a1a1a] border-b border-[#2a2a2a] px-6 py-4">
        <div className="max-w-2xl mx-auto flex items-center gap-4">
          <Link href="/settings" className="text-gray-400 hover:text-gray-200">
            <ArrowLeft className="w-6 h-6" />
          </Link>
          <h1 className="text-lg font-semibold text-gray-100">이용약관</h1>
        </div>
      </header>

      <main className="max-w-2xl mx-auto px-6 py-6">
        <div className="bg-[#1a1a1a] border border-[#2a2a2a] rounded-xl p-6 prose prose-invert max-w-none">
          <p className="text-sm text-gray-500 mb-6">시행일: 2024년 1월 1일</p>

          <section className="mb-8">
            <h2 className="text-lg font-semibold text-gray-100 mb-4">제1조 (목적)</h2>
            <p className="text-gray-400 leading-relaxed">
              이 약관은 Epicstage Corp.(이하 &quot;회사&quot;)가 운영하는 Phiennoi 통역사 보고서 자동화 서비스(이하 &quot;서비스&quot;)의 이용조건 및 절차, 회사와 이용자의 권리, 의무 및 책임사항을 규정함을 목적으로 합니다.
            </p>
          </section>

          <section className="mb-8">
            <h2 className="text-lg font-semibold text-gray-100 mb-4">제2조 (정의)</h2>
            <ol className="list-decimal list-inside text-gray-400 space-y-2">
              <li>&quot;서비스&quot;란 회사가 제공하는 통역 보고서 작성 및 관리 서비스를 말합니다.</li>
              <li>&quot;이용자&quot;란 이 약관에 따라 회사와 이용계약을 체결하고 서비스를 이용하는 자를 말합니다.</li>
              <li>&quot;크레딧&quot;이란 서비스 이용에 필요한 가상의 포인트를 말합니다.</li>
            </ol>
          </section>

          <section className="mb-8">
            <h2 className="text-lg font-semibold text-gray-100 mb-4">제3조 (약관의 효력 및 변경)</h2>
            <ol className="list-decimal list-inside text-gray-400 space-y-2">
              <li>이 약관은 서비스 화면에 게시하거나 기타의 방법으로 이용자에게 공지함으로써 효력이 발생합니다.</li>
              <li>회사는 필요하다고 인정되는 경우 이 약관을 변경할 수 있으며, 변경된 약관은 제1항과 같은 방법으로 공지함으로써 효력이 발생합니다.</li>
            </ol>
          </section>

          <section className="mb-8">
            <h2 className="text-lg font-semibold text-gray-100 mb-4">제4조 (이용계약의 성립)</h2>
            <ol className="list-decimal list-inside text-gray-400 space-y-2">
              <li>이용계약은 이용자가 약관의 내용에 동의하고, 회사가 정한 가입 양식에 따라 회원정보를 기입한 후 회원가입을 완료함으로써 성립됩니다.</li>
              <li>회사는 다음 각 호에 해당하는 이용신청에 대하여는 승낙을 하지 않을 수 있습니다.
                <ul className="list-disc list-inside ml-4 mt-2 space-y-1">
                  <li>실명이 아니거나 타인의 명의를 사용한 경우</li>
                  <li>허위의 정보를 기재하거나, 필수 정보를 기재하지 않은 경우</li>
                  <li>기타 이용신청 요건이 미비된 경우</li>
                </ul>
              </li>
            </ol>
          </section>

          <section className="mb-8">
            <h2 className="text-lg font-semibold text-gray-100 mb-4">제5조 (서비스의 제공)</h2>
            <ol className="list-decimal list-inside text-gray-400 space-y-2">
              <li>회사는 다음의 서비스를 제공합니다.
                <ul className="list-disc list-inside ml-4 mt-2 space-y-1">
                  <li>통역 보고서 자동 생성 서비스</li>
                  <li>보고서 관리 및 저장 서비스</li>
                  <li>기타 회사가 정하는 서비스</li>
                </ul>
              </li>
              <li>서비스는 연중무휴, 1일 24시간 제공함을 원칙으로 합니다.</li>
            </ol>
          </section>

          <section className="mb-8">
            <h2 className="text-lg font-semibold text-gray-100 mb-4">제6조 (크레딧)</h2>
            <ol className="list-decimal list-inside text-gray-400 space-y-2">
              <li>크레딧은 서비스 이용에 필요한 가상의 포인트입니다.</li>
              <li>회원가입 시 기본 크레딧이 지급되며, 프로필 완성 시 추가 크레딧이 지급됩니다.</li>
              <li>크레딧은 현금으로 환불되지 않습니다.</li>
            </ol>
          </section>

          <section className="mb-8">
            <h2 className="text-lg font-semibold text-gray-100 mb-4">제7조 (이용자의 의무)</h2>
            <ol className="list-decimal list-inside text-gray-400 space-y-2">
              <li>이용자는 서비스 이용 시 다음 각 호의 행위를 하여서는 안 됩니다.
                <ul className="list-disc list-inside ml-4 mt-2 space-y-1">
                  <li>타인의 정보를 도용하는 행위</li>
                  <li>서비스의 운영을 방해하는 행위</li>
                  <li>타인의 명예를 손상시키는 행위</li>
                  <li>기타 불법적이거나 부당한 행위</li>
                </ul>
              </li>
            </ol>
          </section>

          <section className="mb-8">
            <h2 className="text-lg font-semibold text-gray-100 mb-4">제8조 (면책조항)</h2>
            <ol className="list-decimal list-inside text-gray-400 space-y-2">
              <li>회사는 천재지변 또는 이에 준하는 불가항력으로 인하여 서비스를 제공할 수 없는 경우에는 책임이 면제됩니다.</li>
              <li>회사는 이용자의 귀책사유로 인한 서비스 이용의 장애에 대하여 책임을 지지 않습니다.</li>
            </ol>
          </section>

          <section>
            <h2 className="text-lg font-semibold text-gray-100 mb-4">제9조 (분쟁해결)</h2>
            <p className="text-gray-400 leading-relaxed">
              서비스 이용과 관련하여 분쟁이 발생한 경우, 양 당사자는 분쟁의 해결을 위해 성실히 협의합니다.
            </p>
          </section>

          <div className="mt-12 pt-6 border-t border-[#2a2a2a]">
            <p className="text-sm text-gray-500">
              본 약관은 2024년 1월 1일부터 시행됩니다.
            </p>
            <p className="text-xs text-gray-600 mt-2">
              © 2025 Epicstage Corp. All rights reserved.
            </p>
          </div>
        </div>
      </main>
    </div>
  );
}
