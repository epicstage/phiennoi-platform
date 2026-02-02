'use client';

import Link from 'next/link';
import { ArrowLeft } from 'lucide-react';

export default function PrivacyPage() {
  return (
    <div className="min-h-screen bg-[#0f0f0f]">
      {/* Header */}
      <header className="bg-[#1a1a1a] border-b border-[#2a2a2a] px-6 py-4">
        <div className="max-w-2xl mx-auto flex items-center gap-4">
          <Link href="/settings" className="text-gray-400 hover:text-gray-200">
            <ArrowLeft className="w-6 h-6" />
          </Link>
          <h1 className="text-lg font-semibold text-gray-100">개인정보처리방침</h1>
        </div>
      </header>

      <main className="max-w-2xl mx-auto px-6 py-6">
        <div className="bg-[#1a1a1a] border border-[#2a2a2a] rounded-xl p-6 prose prose-invert max-w-none">
          <p className="text-sm text-gray-500 mb-6">시행일: 2024년 1월 1일</p>

          <section className="mb-8">
            <h2 className="text-lg font-semibold text-gray-100 mb-4">1. 개인정보의 처리 목적</h2>
            <p className="text-gray-400 leading-relaxed mb-4">
              Epicstage Corp.(이하 &quot;회사&quot;)가 운영하는 Phiennoi 서비스는 다음의 목적을 위하여 개인정보를 처리합니다. 처리하고 있는 개인정보는 다음의 목적 이외의 용도로는 이용되지 않으며, 이용 목적이 변경되는 경우에는 별도의 동의를 받는 등 필요한 조치를 이행할 예정입니다.
            </p>
            <ul className="list-disc list-inside text-gray-400 space-y-2">
              <li>회원 가입 및 관리: 회원 가입의사 확인, 회원제 서비스 제공에 따른 본인 식별·인증</li>
              <li>서비스 제공: 통역 보고서 생성 및 관리 서비스 제공</li>
              <li>서비스 개선: 서비스 이용 기록 분석을 통한 서비스 품질 개선</li>
            </ul>
          </section>

          <section className="mb-8">
            <h2 className="text-lg font-semibold text-gray-100 mb-4">2. 수집하는 개인정보의 항목</h2>
            <p className="text-gray-400 leading-relaxed mb-4">
              회사는 다음의 개인정보 항목을 수집하고 있습니다.
            </p>
            <ul className="list-disc list-inside text-gray-400 space-y-2">
              <li><strong className="text-gray-300">필수항목:</strong> 이메일 주소, 이름</li>
              <li><strong className="text-gray-300">선택항목:</strong> 연락처, 대학교, 전공, 한국어 자격증, 통역 경력, 활동 지역</li>
              <li><strong className="text-gray-300">자동 수집항목:</strong> 서비스 이용 기록, 접속 로그</li>
            </ul>
          </section>

          <section className="mb-8">
            <h2 className="text-lg font-semibold text-gray-100 mb-4">3. 개인정보의 처리 및 보유 기간</h2>
            <p className="text-gray-400 leading-relaxed mb-4">
              회사는 법령에 따른 개인정보 보유·이용 기간 또는 정보주체로부터 개인정보를 수집 시에 동의받은 개인정보 보유·이용 기간 내에서 개인정보를 처리·보유합니다.
            </p>
            <ul className="list-disc list-inside text-gray-400 space-y-2">
              <li>회원 정보: 회원 탈퇴 시까지</li>
              <li>보고서 데이터: 회원 탈퇴 후 30일 이내 삭제</li>
              <li>서비스 이용 기록: 1년간 보관 후 삭제</li>
            </ul>
          </section>

          <section className="mb-8">
            <h2 className="text-lg font-semibold text-gray-100 mb-4">4. 개인정보의 제3자 제공</h2>
            <p className="text-gray-400 leading-relaxed">
              회사는 원칙적으로 이용자의 개인정보를 제3자에게 제공하지 않습니다. 다만, 다음의 경우에는 예외로 합니다.
            </p>
            <ul className="list-disc list-inside text-gray-400 space-y-2 mt-4">
              <li>이용자가 사전에 동의한 경우</li>
              <li>법령의 규정에 의거하거나, 수사 목적으로 법령에 정해진 절차와 방법에 따라 수사기관의 요구가 있는 경우</li>
            </ul>
          </section>

          <section className="mb-8">
            <h2 className="text-lg font-semibold text-gray-100 mb-4">5. 개인정보 처리의 위탁</h2>
            <p className="text-gray-400 leading-relaxed mb-4">
              회사는 서비스 향상을 위해 다음과 같이 개인정보 처리 업무를 위탁하고 있습니다.
            </p>
            <div className="bg-[#242424] rounded-lg p-4">
              <table className="w-full text-sm">
                <thead>
                  <tr className="border-b border-[#3a3a3a]">
                    <th className="text-left py-2 text-gray-300">수탁업체</th>
                    <th className="text-left py-2 text-gray-300">위탁업무</th>
                  </tr>
                </thead>
                <tbody>
                  <tr className="border-b border-[#3a3a3a]">
                    <td className="py-2 text-gray-400">Google</td>
                    <td className="py-2 text-gray-400">소셜 로그인 인증</td>
                  </tr>
                  <tr>
                    <td className="py-2 text-gray-400">Supabase</td>
                    <td className="py-2 text-gray-400">데이터베이스 호스팅</td>
                  </tr>
                </tbody>
              </table>
            </div>
          </section>

          <section className="mb-8">
            <h2 className="text-lg font-semibold text-gray-100 mb-4">6. 정보주체의 권리·의무 및 그 행사방법</h2>
            <p className="text-gray-400 leading-relaxed mb-4">
              이용자는 개인정보주체로서 다음과 같은 권리를 행사할 수 있습니다.
            </p>
            <ul className="list-disc list-inside text-gray-400 space-y-2">
              <li>개인정보 열람 요구</li>
              <li>오류 등이 있을 경우 정정 요구</li>
              <li>삭제 요구</li>
              <li>처리정지 요구</li>
            </ul>
            <p className="text-gray-400 leading-relaxed mt-4">
              권리 행사는 회사에 대해 서면, 전자우편 등을 통하여 하실 수 있으며 회사는 이에 대해 지체 없이 조치하겠습니다.
            </p>
          </section>

          <section className="mb-8">
            <h2 className="text-lg font-semibold text-gray-100 mb-4">7. 개인정보의 파기</h2>
            <p className="text-gray-400 leading-relaxed mb-4">
              회사는 개인정보 보유기간의 경과, 처리목적 달성 등 개인정보가 불필요하게 되었을 때에는 지체 없이 해당 개인정보를 파기합니다.
            </p>
            <ul className="list-disc list-inside text-gray-400 space-y-2">
              <li><strong className="text-gray-300">전자적 파일:</strong> 복구 및 재생이 불가능한 방법으로 영구 삭제</li>
              <li><strong className="text-gray-300">종이 문서:</strong> 분쇄기로 분쇄하거나 소각</li>
            </ul>
          </section>

          <section className="mb-8">
            <h2 className="text-lg font-semibold text-gray-100 mb-4">8. 개인정보의 안전성 확보 조치</h2>
            <p className="text-gray-400 leading-relaxed mb-4">
              회사는 개인정보의 안전성 확보를 위해 다음과 같은 조치를 취하고 있습니다.
            </p>
            <ul className="list-disc list-inside text-gray-400 space-y-2">
              <li>개인정보의 암호화</li>
              <li>해킹 등에 대비한 기술적 대책</li>
              <li>접근권한 관리</li>
            </ul>
          </section>

          <section className="mb-8">
            <h2 className="text-lg font-semibold text-gray-100 mb-4">9. 개인정보 보호책임자</h2>
            <p className="text-gray-400 leading-relaxed mb-4">
              회사는 개인정보 처리에 관한 업무를 총괄해서 책임지고, 개인정보 처리와 관련한 정보주체의 불만처리 및 피해구제 등을 위하여 아래와 같이 개인정보 보호책임자를 지정하고 있습니다.
            </p>
            <div className="bg-[#242424] rounded-lg p-4">
              <p className="text-gray-300"><strong>개인정보 보호책임자</strong></p>
              <p className="text-gray-400 text-sm mt-2">이메일: privacy@phiennoi.com</p>
            </div>
          </section>

          <section>
            <h2 className="text-lg font-semibold text-gray-100 mb-4">10. 개인정보처리방침 변경</h2>
            <p className="text-gray-400 leading-relaxed">
              이 개인정보처리방침은 시행일로부터 적용되며, 법령 및 방침에 따른 변경내용의 추가, 삭제 및 정정이 있는 경우에는 변경사항의 시행 7일 전부터 공지사항을 통하여 고지할 것입니다.
            </p>
          </section>

          <div className="mt-12 pt-6 border-t border-[#2a2a2a]">
            <p className="text-sm text-gray-500">
              본 개인정보처리방침은 2024년 1월 1일부터 시행됩니다.
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
