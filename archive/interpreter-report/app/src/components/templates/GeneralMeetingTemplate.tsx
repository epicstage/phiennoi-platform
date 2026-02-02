'use client';

import React from 'react';

interface GeneralMeetingTemplateProps {
  data: {
    date: string;
    venue: string;
    eventName: string;
    interpreter: string;
    koreanParty: {
      company: string;
      participants: string;
    };
    vietnameseParty: {
      company: string;
      participants: string;
    };
    agenda: string;
    discussion: string;
    decisions: string;
    actionItems: string;
    nextMeeting: string;
    notes: string;
  };
  mode?: 'preview' | 'print';
}

export default function GeneralMeetingTemplate({ data, mode = 'preview' }: GeneralMeetingTemplateProps) {
  return (
    <div
      className={`bg-white text-black ${mode === 'print' ? 'w-[210mm] min-h-[297mm]' : 'w-full'} p-6 font-sans`}
      style={{ fontSize: '11px' }}
    >
      {/* Header */}
      <div className="text-center mb-6 border-b-2 border-gray-800 pb-4">
        <h1 className="text-xl font-bold">회의록 / Meeting Minutes</h1>
        <h2 className="text-lg text-gray-600 mt-1">Biên bản cuộc họp</h2>
      </div>

      {/* Basic Info Table */}
      <table className="w-full border-collapse border border-gray-400 mb-6">
        <tbody>
          <tr className="bg-gray-100">
            <td className="border border-gray-400 p-2 w-28 text-center font-bold">일자 / Date</td>
            <td className="border border-gray-400 p-2 w-40">{data.date}</td>
            <td className="border border-gray-400 p-2 w-28 text-center font-bold">장소 / Venue</td>
            <td className="border border-gray-400 p-2">{data.venue}</td>
          </tr>
          <tr>
            <td className="border border-gray-400 p-2 text-center font-bold bg-gray-100">행사명</td>
            <td className="border border-gray-400 p-2" colSpan={3}>{data.eventName}</td>
          </tr>
          <tr>
            <td className="border border-gray-400 p-2 text-center font-bold bg-gray-100">통역사</td>
            <td className="border border-gray-400 p-2" colSpan={3}>{data.interpreter}</td>
          </tr>
        </tbody>
      </table>

      {/* Participants */}
      <table className="w-full border-collapse border border-gray-400 mb-6">
        <thead>
          <tr className="bg-gray-200">
            <th className="border border-gray-400 p-2 text-center">구분</th>
            <th className="border border-gray-400 p-2 text-center">회사명 / Company</th>
            <th className="border border-gray-400 p-2 text-center">참석자 / Participants</th>
          </tr>
        </thead>
        <tbody>
          <tr>
            <td className="border border-gray-400 p-2 text-center bg-blue-50 font-bold w-24">
              한국측<br/>Korean
            </td>
            <td className="border border-gray-400 p-2 w-40">{data.koreanParty.company}</td>
            <td className="border border-gray-400 p-2">{data.koreanParty.participants}</td>
          </tr>
          <tr>
            <td className="border border-gray-400 p-2 text-center bg-red-50 font-bold">
              베트남측<br/>Vietnamese
            </td>
            <td className="border border-gray-400 p-2">{data.vietnameseParty.company}</td>
            <td className="border border-gray-400 p-2">{data.vietnameseParty.participants}</td>
          </tr>
        </tbody>
      </table>

      {/* Meeting Content */}
      <table className="w-full border-collapse border border-gray-400 mb-6">
        <tbody>
          <tr>
            <td className="border border-gray-400 p-3 bg-gray-100 w-32 text-center font-bold align-top">
              안건<br/>Agenda
            </td>
            <td className="border border-gray-400 p-3 min-h-[60px] whitespace-pre-wrap">
              {data.agenda}
            </td>
          </tr>
          <tr>
            <td className="border border-gray-400 p-3 bg-gray-100 text-center font-bold align-top">
              논의 내용<br/>Discussion
            </td>
            <td className="border border-gray-400 p-3 min-h-[100px] whitespace-pre-wrap">
              {data.discussion}
            </td>
          </tr>
          <tr>
            <td className="border border-gray-400 p-3 bg-gray-100 text-center font-bold align-top">
              결정 사항<br/>Decisions
            </td>
            <td className="border border-gray-400 p-3 min-h-[60px] whitespace-pre-wrap">
              {data.decisions}
            </td>
          </tr>
          <tr>
            <td className="border border-gray-400 p-3 bg-gray-100 text-center font-bold align-top">
              액션 아이템<br/>Action Items
            </td>
            <td className="border border-gray-400 p-3 min-h-[60px] whitespace-pre-wrap">
              {data.actionItems}
            </td>
          </tr>
          <tr>
            <td className="border border-gray-400 p-3 bg-gray-100 text-center font-bold align-top">
              차기 일정<br/>Next Meeting
            </td>
            <td className="border border-gray-400 p-3">
              {data.nextMeeting}
            </td>
          </tr>
          <tr>
            <td className="border border-gray-400 p-3 bg-gray-100 text-center font-bold align-top">
              비고<br/>Notes
            </td>
            <td className="border border-gray-400 p-3 min-h-[40px] whitespace-pre-wrap">
              {data.notes}
            </td>
          </tr>
        </tbody>
      </table>

      {/* Signature Section */}
      <div className="mt-8 grid grid-cols-2 gap-8">
        <div className="text-center">
          <p className="font-bold mb-2">한국측 서명 / Korean Signature</p>
          <div className="border border-gray-400 h-20 rounded"></div>
          <p className="text-gray-500 mt-1 text-[10px]">성명 / Name: _______________</p>
        </div>
        <div className="text-center">
          <p className="font-bold mb-2">베트남측 서명 / Vietnamese Signature</p>
          <div className="border border-gray-400 h-20 rounded"></div>
          <p className="text-gray-500 mt-1 text-[10px]">성명 / Name: _______________</p>
        </div>
      </div>

      {/* Footer */}
      <div className="mt-8 pt-4 border-t border-gray-300">
        <div className="flex justify-between text-[9px] text-gray-500">
          <span>작성일: {new Date().toLocaleDateString('ko-KR')}</span>
          <span>한-베 비즈니스 회의록</span>
        </div>
      </div>
    </div>
  );
}
