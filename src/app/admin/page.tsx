"use client";

import { useState, useEffect } from "react";
import Link from "next/link";

interface Interpreter {
  id: string;
  name: string;
  email: string;
  phone: string;
  location: string;
  domains: string[];
  resume_url: string | null;
  status: string;
  created_at: string;
}

const DOMAIN_LABELS: Record<string, string> = {
  agriculture: "농업",
  beauty: "뷰티",
  manufacturing: "제조업",
  legal: "법률",
  medical: "의료",
  it: "IT",
  finance: "금융",
  construction: "건설",
  logistics: "물류",
  food: "식품",
  realEstate: "부동산",
  exhibition: "전시",
};

const STATUS_LABELS: Record<string, { label: string; color: string }> = {
  pending: { label: "대기중", color: "bg-yellow-100 text-yellow-800" },
  approved: { label: "승인", color: "bg-green-100 text-green-800" },
  rejected: { label: "거절", color: "bg-red-100 text-red-800" },
};

export default function AdminPage() {
  const [interpreters, setInterpreters] = useState<Interpreter[]>([]);
  const [loading, setLoading] = useState(true);
  const [error, setError] = useState<string | null>(null);
  const [password, setPassword] = useState("");
  const [authenticated, setAuthenticated] = useState(false);

  // 간단한 비밀번호 인증 (실제 환경에서는 더 강력한 인증 필요)
  const ADMIN_PASSWORD = "hanbe2024";

  const handleLogin = (e: React.FormEvent) => {
    e.preventDefault();
    if (password === ADMIN_PASSWORD) {
      setAuthenticated(true);
      fetchInterpreters();
    } else {
      setError("비밀번호가 올바르지 않습니다.");
    }
  };

  const fetchInterpreters = async () => {
    try {
      setLoading(true);
      const res = await fetch("/api/admin/interpreters");
      if (!res.ok) throw new Error("데이터를 불러올 수 없습니다.");
      const data = await res.json();
      setInterpreters(data);
    } catch (err) {
      setError(err instanceof Error ? err.message : "오류가 발생했습니다.");
    } finally {
      setLoading(false);
    }
  };

  const updateStatus = async (id: string, status: string) => {
    try {
      const res = await fetch("/api/admin/interpreters", {
        method: "PATCH",
        headers: { "Content-Type": "application/json" },
        body: JSON.stringify({ id, status }),
      });
      if (!res.ok) throw new Error("상태 업데이트 실패");
      fetchInterpreters();
    } catch (err) {
      alert("상태 업데이트에 실패했습니다.");
    }
  };

  if (!authenticated) {
    return (
      <div className="min-h-screen bg-gray-50 flex items-center justify-center">
        <div className="bg-white p-8 rounded-lg shadow-md w-full max-w-md">
          <h1 className="text-2xl font-bold text-center mb-6">관리자 로그인</h1>
          <form onSubmit={handleLogin}>
            <input
              type="password"
              value={password}
              onChange={(e) => setPassword(e.target.value)}
              placeholder="비밀번호 입력"
              className="w-full px-4 py-3 border rounded-lg mb-4 focus:outline-none focus:ring-2 focus:ring-red-500"
            />
            {error && <p className="text-red-500 text-sm mb-4">{error}</p>}
            <button
              type="submit"
              className="w-full bg-red-600 text-white py-3 rounded-lg hover:bg-red-700 transition"
            >
              로그인
            </button>
          </form>
          <Link
            href="/"
            className="block text-center mt-4 text-gray-500 hover:text-gray-700"
          >
            ← 메인으로 돌아가기
          </Link>
        </div>
      </div>
    );
  }

  return (
    <div className="min-h-screen bg-gray-50">
      <header className="bg-white shadow">
        <div className="max-w-7xl mx-auto px-4 py-6 flex justify-between items-center">
          <h1 className="text-2xl font-bold text-gray-900">통역사 관리</h1>
          <Link href="/" className="text-gray-500 hover:text-gray-700">
            ← 메인으로
          </Link>
        </div>
      </header>

      <main className="max-w-7xl mx-auto px-4 py-8">
        {loading ? (
          <div className="text-center py-12">
            <div className="animate-spin rounded-full h-12 w-12 border-b-2 border-red-600 mx-auto"></div>
            <p className="mt-4 text-gray-500">데이터 로딩 중...</p>
          </div>
        ) : error ? (
          <div className="bg-red-50 text-red-600 p-4 rounded-lg">{error}</div>
        ) : interpreters.length === 0 ? (
          <div className="bg-white rounded-lg shadow p-12 text-center">
            <p className="text-gray-500">등록된 통역사가 없습니다.</p>
          </div>
        ) : (
          <div className="bg-white rounded-lg shadow overflow-hidden">
            <div className="px-6 py-4 border-b">
              <p className="text-gray-600">
                총 <span className="font-bold">{interpreters.length}</span>명의
                통역사가 등록되어 있습니다.
              </p>
            </div>
            <div className="overflow-x-auto">
              <table className="w-full">
                <thead className="bg-gray-50">
                  <tr>
                    <th className="px-6 py-3 text-left text-xs font-medium text-gray-500 uppercase tracking-wider">
                      이름
                    </th>
                    <th className="px-6 py-3 text-left text-xs font-medium text-gray-500 uppercase tracking-wider">
                      연락처
                    </th>
                    <th className="px-6 py-3 text-left text-xs font-medium text-gray-500 uppercase tracking-wider">
                      지역
                    </th>
                    <th className="px-6 py-3 text-left text-xs font-medium text-gray-500 uppercase tracking-wider">
                      전문분야
                    </th>
                    <th className="px-6 py-3 text-left text-xs font-medium text-gray-500 uppercase tracking-wider">
                      이력서
                    </th>
                    <th className="px-6 py-3 text-left text-xs font-medium text-gray-500 uppercase tracking-wider">
                      상태
                    </th>
                    <th className="px-6 py-3 text-left text-xs font-medium text-gray-500 uppercase tracking-wider">
                      등록일
                    </th>
                  </tr>
                </thead>
                <tbody className="divide-y divide-gray-200">
                  {interpreters.map((interpreter) => (
                    <tr key={interpreter.id} className="hover:bg-gray-50">
                      <td className="px-6 py-4 whitespace-nowrap">
                        <div className="font-medium text-gray-900">
                          {interpreter.name}
                        </div>
                        <div className="text-sm text-gray-500">
                          {interpreter.email}
                        </div>
                      </td>
                      <td className="px-6 py-4 whitespace-nowrap text-sm text-gray-500">
                        {interpreter.phone}
                      </td>
                      <td className="px-6 py-4 whitespace-nowrap text-sm text-gray-500">
                        {interpreter.location || "-"}
                      </td>
                      <td className="px-6 py-4">
                        <div className="flex flex-wrap gap-1">
                          {interpreter.domains?.map((domain) => (
                            <span
                              key={domain}
                              className="inline-block px-2 py-1 text-xs bg-gray-100 text-gray-700 rounded"
                            >
                              {DOMAIN_LABELS[domain] || domain}
                            </span>
                          ))}
                        </div>
                      </td>
                      <td className="px-6 py-4 whitespace-nowrap">
                        {interpreter.resume_url ? (
                          <a
                            href={interpreter.resume_url}
                            target="_blank"
                            rel="noopener noreferrer"
                            className="text-red-600 hover:text-red-800 text-sm"
                          >
                            다운로드
                          </a>
                        ) : (
                          <span className="text-gray-400 text-sm">없음</span>
                        )}
                      </td>
                      <td className="px-6 py-4 whitespace-nowrap">
                        <select
                          value={interpreter.status}
                          onChange={(e) =>
                            updateStatus(interpreter.id, e.target.value)
                          }
                          className={`px-2 py-1 text-xs rounded-full border-0 cursor-pointer ${
                            STATUS_LABELS[interpreter.status]?.color ||
                            "bg-gray-100"
                          }`}
                        >
                          <option value="pending">대기중</option>
                          <option value="approved">승인</option>
                          <option value="rejected">거절</option>
                        </select>
                      </td>
                      <td className="px-6 py-4 whitespace-nowrap text-sm text-gray-500">
                        {new Date(interpreter.created_at).toLocaleDateString(
                          "ko-KR"
                        )}
                      </td>
                    </tr>
                  ))}
                </tbody>
              </table>
            </div>
          </div>
        )}
      </main>
    </div>
  );
}
