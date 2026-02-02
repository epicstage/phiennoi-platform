'use client';

import React from 'react';

interface CompanyInfo {
  companyName: string;
  contactPerson: string;
  position: string;
  phone: string;
  email: string;
  address: string;
  industry: string;
  employees: string;
  revenue: string;
}

interface MeetingRecord {
  time: string;
  koreanCompany: CompanyInfo;
  vietnameseCompany: CompanyInfo;
  meetingPurpose: {
    partnership: boolean;
    investment: boolean;
    techTransfer: boolean;
    outsourcing: boolean;
    marketResearch: boolean;
    other: boolean;
  };
  discussionPoints: string;
  actionItems: string;
  followUp: string;
  rating: {
    potential: number; // 1-5
    urgency: number; // 1-5
  };
  notes: string;
}

interface OffshoreTechTemplateProps {
  data: {
    eventName: string;
    date: string;
    venue: string;
    interpreter: string;
    meetings: MeetingRecord[];
  };
  mode?: 'preview' | 'print';
}

export default function OffshoreTechTemplate({ data, mode = 'preview' }: OffshoreTechTemplateProps) {
  const renderRatingCircles = (value: number) => {
    return (
      <div className="flex gap-0.5">
        {[5, 4, 3, 2, 1].map((num) => (
          <div
            key={num}
            className={`w-4 h-4 rounded-full border border-gray-400 flex items-center justify-center text-[8px] ${
              value === num ? 'bg-blue-600 text-white' : 'bg-white'
            }`}
          >
            {num}
          </div>
        ))}
      </div>
    );
  };

  const renderCheckbox = (checked: boolean, label: string) => (
    <div className="flex items-center gap-1">
      <div className={`w-3 h-3 border border-gray-400 rounded-sm ${checked ? 'bg-blue-600' : 'bg-white'}`}>
        {checked && <span className="text-white text-[8px] flex items-center justify-center">✓</span>}
      </div>
      <span className="text-[9px]">{label}</span>
    </div>
  );

  return (
    <div
      className={`bg-white text-black ${mode === 'print' ? 'w-[210mm] min-h-[297mm]' : 'w-full'} p-4 font-sans`}
      style={{ fontSize: '10px' }}
    >
      {/* Header */}
      <div className="text-center mb-4 border-b-2 border-blue-600 pb-3">
        <h1 className="text-lg font-bold text-blue-800">2025 한-베 오프쇼어 테크 커넥트</h1>
        <h2 className="text-md font-semibold text-blue-600">Korea-Vietnam Offshore Tech Connect 2025</h2>
        <p className="text-sm text-gray-600 mt-2">비즈니스 상담 보고서 / Business Meeting Report</p>
      </div>

      {/* Event Info */}
      <table className="w-full border-collapse border border-gray-400 mb-4">
        <tbody>
          <tr className="bg-blue-50">
            <td className="border border-gray-400 p-2 w-24 text-center font-medium">행사명</td>
            <td className="border border-gray-400 p-2">{data.eventName || '2025 한-베 오프쇼어 테크 커넥트'}</td>
            <td className="border border-gray-400 p-2 w-20 text-center font-medium">일자</td>
            <td className="border border-gray-400 p-2 w-28">{data.date}</td>
          </tr>
          <tr>
            <td className="border border-gray-400 p-2 text-center font-medium bg-blue-50">장소</td>
            <td className="border border-gray-400 p-2">{data.venue}</td>
            <td className="border border-gray-400 p-2 text-center font-medium bg-blue-50">통역사</td>
            <td className="border border-gray-400 p-2">{data.interpreter}</td>
          </tr>
        </tbody>
      </table>

      {/* Meeting Records */}
      {data.meetings.map((meeting, index) => (
        <div key={index} className="mb-6 border border-gray-300 rounded-lg overflow-hidden">
          {/* Meeting Header */}
          <div className="bg-blue-600 text-white p-2 flex justify-between items-center">
            <span className="font-bold">상담 #{index + 1}</span>
            <span className="text-sm">{meeting.time}</span>
          </div>

          {/* Companies Info */}
          <div className="grid grid-cols-2 gap-0">
            {/* Korean Company */}
            <div className="border-r border-gray-300">
              <div className="bg-blue-100 p-2 font-bold text-center text-sm border-b border-gray-300">
                한국 기업 / Korean Company
              </div>
              <div className="p-3 space-y-1 text-[9px]">
                <p><span className="font-medium">회사명:</span> {meeting.koreanCompany.companyName}</p>
                <p><span className="font-medium">담당자:</span> {meeting.koreanCompany.contactPerson}</p>
                <p><span className="font-medium">직책:</span> {meeting.koreanCompany.position}</p>
                <p><span className="font-medium">연락처:</span> {meeting.koreanCompany.phone}</p>
                <p><span className="font-medium">이메일:</span> {meeting.koreanCompany.email}</p>
                <p><span className="font-medium">업종:</span> {meeting.koreanCompany.industry}</p>
              </div>
            </div>

            {/* Vietnamese Company */}
            <div>
              <div className="bg-red-100 p-2 font-bold text-center text-sm border-b border-gray-300">
                베트남 기업 / Vietnamese Company
              </div>
              <div className="p-3 space-y-1 text-[9px]">
                <p><span className="font-medium">회사명:</span> {meeting.vietnameseCompany.companyName}</p>
                <p><span className="font-medium">담당자:</span> {meeting.vietnameseCompany.contactPerson}</p>
                <p><span className="font-medium">직책:</span> {meeting.vietnameseCompany.position}</p>
                <p><span className="font-medium">연락처:</span> {meeting.vietnameseCompany.phone}</p>
                <p><span className="font-medium">이메일:</span> {meeting.vietnameseCompany.email}</p>
                <p><span className="font-medium">업종:</span> {meeting.vietnameseCompany.industry}</p>
              </div>
            </div>
          </div>

          {/* Meeting Details */}
          <table className="w-full border-collapse">
            <tbody>
              <tr>
                <td className="border border-gray-300 p-2 bg-gray-100 w-28 text-center font-medium text-[9px]">
                  상담 목적
                </td>
                <td className="border border-gray-300 p-2">
                  <div className="grid grid-cols-3 gap-2 text-[8px]">
                    {renderCheckbox(meeting.meetingPurpose.partnership, '파트너십 구축')}
                    {renderCheckbox(meeting.meetingPurpose.investment, '투자 유치/진행')}
                    {renderCheckbox(meeting.meetingPurpose.techTransfer, '기술 이전')}
                    {renderCheckbox(meeting.meetingPurpose.outsourcing, '아웃소싱')}
                    {renderCheckbox(meeting.meetingPurpose.marketResearch, '시장 조사')}
                    {renderCheckbox(meeting.meetingPurpose.other, '기타')}
                  </div>
                </td>
              </tr>
              <tr>
                <td className="border border-gray-300 p-2 bg-gray-100 text-center font-medium text-[9px]">
                  주요 논의 사항
                </td>
                <td className="border border-gray-300 p-2 text-[9px] min-h-[60px]">
                  {meeting.discussionPoints}
                </td>
              </tr>
              <tr>
                <td className="border border-gray-300 p-2 bg-gray-100 text-center font-medium text-[9px]">
                  후속 조치
                </td>
                <td className="border border-gray-300 p-2 text-[9px]">
                  {meeting.actionItems}
                </td>
              </tr>
              <tr>
                <td className="border border-gray-300 p-2 bg-gray-100 text-center font-medium text-[9px]">
                  협력 가능성
                </td>
                <td className="border border-gray-300 p-2">
                  <div className="flex items-center gap-4">
                    <span className="text-[9px]">잠재력:</span>
                    {renderRatingCircles(meeting.rating.potential)}
                    <span className="text-[9px] ml-4">긴급도:</span>
                    {renderRatingCircles(meeting.rating.urgency)}
                  </div>
                </td>
              </tr>
              <tr>
                <td className="border border-gray-300 p-2 bg-gray-100 text-center font-medium text-[9px]">
                  비고
                </td>
                <td className="border border-gray-300 p-2 text-[9px]">
                  {meeting.notes}
                </td>
              </tr>
            </tbody>
          </table>

          {/* Success Probability */}
          <div className="bg-gray-50 p-2 text-right text-[10px] border-t border-gray-300">
            협력 성사 가능성: <span className="font-bold text-blue-600">상</span> · 중 · 하
          </div>
        </div>
      ))}

      {/* Footer */}
      <div className="mt-6 pt-4 border-t border-gray-300">
        <div className="flex justify-between text-[9px] text-gray-500">
          <span>작성일: {new Date().toLocaleDateString('ko-KR')}</span>
          <span>Korea-Vietnam Offshore Tech Connect 2025</span>
        </div>
      </div>
    </div>
  );
}
