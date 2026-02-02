'use client';

import React from 'react';

interface BuyerInfo {
  companyName: string;
  contactPerson: string;
  position: string;
  contactPoint: string;
  time: string;
  items: string;
  consultType: {
    priceConsult: boolean;
    sampleRequest: boolean;
    agentConsult: boolean;
    qualityConsult: boolean;
    otherConsult: boolean;
    marketResearch: boolean;
    regulationConsult: boolean;
  };
  result: {
    contractSigned: boolean;
    sampleProvided: boolean;
    catalogProvided: boolean;
    revisit: boolean;
    noResult: boolean;
  };
  rating: {
    interest: number; // 1-5
    purchase: number; // 1-5
  };
  exportAmount: string;
  currency: 'USD' | 'VND';
  notes: string;
}

interface KBeautyExpoTemplateProps {
  data: {
    date: string;
    koreanCompany: string;
    boothNo: string;
    staff: string;
    interpreter: string;
    buyers: BuyerInfo[];
  };
  mode?: 'preview' | 'print';
}

export default function KBeautyExpoTemplate({ data, mode = 'preview' }: KBeautyExpoTemplateProps) {
  const renderRatingCircles = (value: number) => {
    return (
      <div className="flex gap-0.5">
        {[5, 4, 3, 2, 1].map((num) => (
          <div
            key={num}
            className={`w-4 h-4 rounded-full border border-gray-400 flex items-center justify-center text-[8px] ${
              value === num ? 'bg-gray-800 text-white' : 'bg-white'
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
      <div className={`w-3 h-3 border border-gray-400 ${checked ? 'bg-gray-800' : 'bg-white'}`}>
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
      <div className="text-center mb-4">
        <h1 className="text-lg font-bold">K-Beauty Expo Vietnam 2025 수출상담일지</h1>
        <p className="text-sm text-gray-600">
          ※ 동 자료는 귀사의 상담 후속지원을 위한 소중한 자료로 활용되니, 다소 불편하시더라도 상세히 명기하여
        </p>
        <p className="text-sm text-gray-600">주실 것을 요청 드립니다.</p>
      </div>

      {/* Date */}
      <div className="text-right mb-2">
        <span className="border-b border-black px-2">{data.date?.split('-')[1] || '___'}</span> 월
        <span className="border-b border-black px-2 ml-2">{data.date?.split('-')[2] || '___'}</span> 일
      </div>

      {/* Company Info Table */}
      <table className="w-full border-collapse border border-gray-400 mb-4">
        <tbody>
          <tr className="bg-blue-100">
            <td colSpan={6} className="border border-gray-400 p-1 text-center font-bold text-sm">
              BUSINESS MEETING REPORT
            </td>
          </tr>
          <tr>
            <td className="border border-gray-400 p-1 bg-gray-100 w-24 text-center font-medium">
              KOREAN<br/>COMPANY
            </td>
            <td className="border border-gray-400 p-1 w-40">{data.koreanCompany}</td>
            <td className="border border-gray-400 p-1 bg-gray-100 w-20 text-center">Booth No.</td>
            <td className="border border-gray-400 p-1 w-16">{data.boothNo}</td>
            <td className="border border-gray-400 p-1 bg-gray-100 w-20 text-center">작성자(담당자)</td>
            <td className="border border-gray-400 p-1">{data.staff}</td>
          </tr>
          <tr>
            <td className="border border-gray-400 p-1 bg-gray-100 text-center">통역사</td>
            <td colSpan={5} className="border border-gray-400 p-1">{data.interpreter}</td>
          </tr>
        </tbody>
      </table>

      {/* Buyer Sections */}
      {data.buyers.map((buyer, index) => (
        <div key={index} className="mb-6">
          {/* Buyer Company Profile */}
          <table className="w-full border-collapse border border-gray-400 mb-2">
            <tbody>
              <tr className="bg-yellow-100">
                <td colSpan={8} className="border border-gray-400 p-1 font-bold">
                  BUYER COMPANY PROFILE
                </td>
                <td className="border border-gray-400 p-1 bg-yellow-100 text-center w-20">
                  {buyer.time}
                </td>
              </tr>
              <tr>
                <td colSpan={2} className="border border-gray-400 p-1 bg-gray-50 text-[9px]">
                  [ BUSINESS CARD OF BUYER ]<br/>
                  <span className="text-gray-500">명함 부착 또는, 간단한 회사명과 담당자 이름 기재</span>
                </td>
                <td className="border border-gray-400 p-1 bg-gray-100 w-16 text-center text-[9px]">상담아이템</td>
                <td className="border border-gray-400 p-1" colSpan={2}>{buyer.items}</td>
                <td className="border border-gray-400 p-1 bg-gray-100 text-center text-[9px]">상담유형</td>
                <td className="border border-gray-400 p-1 text-[8px]" colSpan={2}>
                  <div className="grid grid-cols-2 gap-1">
                    {renderCheckbox(buyer.consultType.priceConsult, '가격(바이어)>사')}
                    {renderCheckbox(buyer.consultType.sampleRequest, '샘플요청')}
                    {renderCheckbox(buyer.consultType.agentConsult, '에이전트 관련')}
                    {renderCheckbox(buyer.consultType.qualityConsult, '품질 관련')}
                    {renderCheckbox(buyer.consultType.otherConsult, '기타')}
                    {renderCheckbox(buyer.consultType.marketResearch, '시장조사')}
                    {renderCheckbox(buyer.consultType.regulationConsult, '인허가 관련')}
                  </div>
                </td>
              </tr>
              <tr>
                <td rowSpan={4} className="border border-gray-400 p-2 w-32 align-top">
                  <div className="text-[9px] space-y-1">
                    <p>• Company Name: <span className="font-medium">{buyer.companyName}</span></p>
                    <p>• Contact person Name: <span className="font-medium">{buyer.contactPerson}</span></p>
                    <p>• Position: <span className="font-medium">{buyer.position}</span></p>
                    <p>• Contact Point: <span className="font-medium">{buyer.contactPoint}</span></p>
                  </div>
                </td>
                <td className="border border-gray-400 p-1 bg-gray-100 text-center text-[9px]" rowSpan={4}>
                  상담내용<br/>(비고/MOU/<br/>추가요청 등)
                </td>
                <td className="border border-gray-400 p-1 bg-gray-100 text-center text-[9px]">상담결과</td>
                <td className="border border-gray-400 p-1 text-[8px]" colSpan={2}>
                  <div className="space-y-0.5">
                    {renderCheckbox(buyer.result.contractSigned, '계약(현->바이어)')}
                    {renderCheckbox(buyer.result.sampleProvided, '샘플제공')}
                    {renderCheckbox(buyer.result.catalogProvided, '카탈로그 제공')}
                  </div>
                </td>
                <td className="border border-gray-400 p-1 text-[8px]" colSpan={2}>
                  <div className="space-y-0.5">
                    {renderCheckbox(buyer.result.revisit, '재방문(바이어->현지)')}
                    {renderCheckbox(buyer.result.noResult, '무결과')}
                  </div>
                </td>
                <td className="border border-gray-400 p-1 bg-gray-100 text-center text-[9px] w-20">
                  수출(예상)<br/>금액
                </td>
              </tr>
              <tr>
                <td className="border border-gray-400 p-1 bg-gray-100 text-center text-[9px]">
                  관심도 평가
                </td>
                <td className="border border-gray-400 p-1 text-center" colSpan={4}>
                  {renderRatingCircles(buyer.rating.interest)}
                </td>
                <td className="border border-gray-400 p-1 text-center" rowSpan={2}>
                  <div className="text-[9px]">
                    {buyer.currency}(단위)
                    <div className="font-bold mt-1">{buyer.exportAmount}</div>
                  </div>
                </td>
              </tr>
              <tr>
                <td className="border border-gray-400 p-1 bg-gray-100 text-center text-[9px]">
                  구매가능성 평가
                </td>
                <td className="border border-gray-400 p-1 text-center" colSpan={4}>
                  {renderRatingCircles(buyer.rating.purchase)}
                </td>
              </tr>
              <tr>
                <td className="border border-gray-400 p-2 text-[9px]" colSpan={6}>
                  {buyer.notes}
                </td>
              </tr>
            </tbody>
          </table>

          {/* Transaction Possibility */}
          <div className="text-right text-[10px] mb-4">
            거래 성사 가능성 (<span className="font-bold">상</span> · 중 · 하)
          </div>
        </div>
      ))}

      {/* Footer */}
      <div className="text-[8px] text-gray-500 mt-4 text-center">
        CS | Được quét bằng CamScanner
      </div>
    </div>
  );
}
