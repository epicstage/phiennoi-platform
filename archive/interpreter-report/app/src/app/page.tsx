'use client';

import { useState } from 'react';
import { Mic, FileAudio, Camera, FileText, ArrowRight, Check } from 'lucide-react';
import Link from 'next/link';

export default function Home() {
  const [isLoggedIn] = useState(false); // TODO: Replace with actual auth state

  return (
    <div className="min-h-screen bg-[#0f0f0f]">
      {/* Header */}
      <header className="px-6 py-4 flex justify-between items-center max-w-6xl mx-auto">
        <div>
          <h1 className="text-2xl font-bold text-indigo-400">Phiennoi</h1>
          <p className="text-[10px] text-gray-600">by Epicstage Corp.</p>
        </div>
        {isLoggedIn ? (
          <Link
            href="/dashboard"
            className="bg-indigo-600 text-white px-4 py-2 rounded-lg hover:bg-indigo-500 transition"
          >
            대시보드
          </Link>
        ) : (
          <Link
            href="/login"
            className="bg-indigo-600 text-white px-4 py-2 rounded-lg hover:bg-indigo-500 transition"
          >
            시작하기
          </Link>
        )}
      </header>

      {/* Hero Section */}
      <main className="px-6 py-16 max-w-6xl mx-auto">
        <div className="text-center mb-16">
          <h2 className="text-4xl md:text-5xl font-bold text-gray-100 mb-6">
            통역은 당신이,<br />
            <span className="text-indigo-400">보고서는 AI가</span>
          </h2>
          <p className="text-xl text-gray-400 mb-8 max-w-2xl mx-auto">
            녹음하고 양식만 알려주세요.<br />
            Phiennoi가 보고서를 자동으로 작성해드립니다.
          </p>
          <Link
            href="/login"
            className="inline-flex items-center gap-2 bg-indigo-600 text-white px-8 py-4 rounded-xl text-lg font-medium hover:bg-indigo-500 transition"
          >
            무료로 시작하기 <ArrowRight className="w-5 h-5" />
          </Link>
          <p className="text-sm text-gray-500 mt-3">
            가입하면 무료 5회 제공 | 프로필 완성시 +20회
          </p>
        </div>

        {/* How it works */}
        <div className="grid md:grid-cols-4 gap-6 mb-16">
          <StepCard
            icon={<Mic className="w-8 h-8" />}
            step={1}
            title="녹음하기"
            description="미팅을 녹음하거나 파일을 업로드하세요"
          />
          <StepCard
            icon={<Camera className="w-8 h-8" />}
            step={2}
            title="양식 입력"
            description="보고서 양식을 촬영하거나 항목을 입력하세요"
          />
          <StepCard
            icon={<FileText className="w-8 h-8" />}
            step={3}
            title="자동 생성"
            description="AI가 녹음 내용을 분석하여 보고서를 작성합니다"
          />
          <StepCard
            icon={<FileAudio className="w-8 h-8" />}
            step={4}
            title="서명 & 제출"
            description="서명하고 PDF로 다운로드하세요"
          />
        </div>

        {/* Features */}
        <div className="bg-[#1a1a1a] rounded-2xl p-8 border border-[#2a2a2a]">
          <h3 className="text-2xl font-bold text-center mb-8 text-gray-100">주요 기능</h3>
          <div className="grid md:grid-cols-2 gap-6">
            <FeatureItem text="한국어/베트남어 자동 인식 및 전사" />
            <FeatureItem text="다양한 보고서 양식 지원" />
            <FeatureItem text="전문용어 문맥 파악 및 설명" />
            <FeatureItem text="PDF 생성 및 서명 기능" />
            <FeatureItem text="오프라인 녹음 지원 (PWA)" />
            <FeatureItem text="친구 추천시 크레딧 지급" />
          </div>
        </div>
      </main>

      {/* Footer */}
      <footer className="px-6 py-8 text-center text-sm">
        <p className="text-gray-500 mb-1">한-베 통역사를 위한 보고서 자동화 서비스</p>
        <p className="text-gray-600">© 2025 Epicstage Corp. All rights reserved.</p>
      </footer>
    </div>
  );
}

function StepCard({ icon, step, title, description }: {
  icon: React.ReactNode;
  step: number;
  title: string;
  description: string;
}) {
  return (
    <div className="bg-[#1a1a1a] rounded-xl p-6 border border-[#2a2a2a] text-center">
      <div className="inline-flex items-center justify-center w-16 h-16 rounded-full bg-indigo-900/50 text-indigo-400 mb-4">
        {icon}
      </div>
      <div className="text-sm text-indigo-400 font-medium mb-1">Step {step}</div>
      <h4 className="text-lg font-semibold text-gray-100 mb-2">{title}</h4>
      <p className="text-gray-400 text-sm">{description}</p>
    </div>
  );
}

function FeatureItem({ text }: { text: string }) {
  return (
    <div className="flex items-center gap-3">
      <div className="flex-shrink-0 w-6 h-6 rounded-full bg-green-900/50 flex items-center justify-center">
        <Check className="w-4 h-4 text-green-400" />
      </div>
      <span className="text-gray-300">{text}</span>
    </div>
  );
}
