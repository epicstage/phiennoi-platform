'use client';

import { useState, useEffect, useCallback } from 'react';
import { useSession } from 'next-auth/react';
import { useRouter } from 'next/navigation';
import Link from 'next/link';
import {
  Users,
  FileText,
  CreditCard,
  ArrowLeft,
  RefreshCw,
  Search,
  ChevronLeft,
  ChevronRight,
  X,
  Trash2,
  Eye,
  Download,
  History,
} from 'lucide-react';

const ADMIN_EMAILS = ['seokheel.kang@gmail.com', 'admin@phiennoi.com'];

interface Stats {
  totalUsers: number;
  totalReports: number;
  totalCreditsUsed: number;
  todaySignups: number;
}

interface User {
  id: string;
  email: string;
  name: string | null;
  credits: number;
  profile_completed: boolean;
  created_at: string;
}

interface Report {
  id: string;
  title: string;
  user_email: string;
  status: string;
  credits_used: number;
  language_pair: string;
  created_at: string;
}

interface Transaction {
  id: string;
  user_email: string;
  amount: number;
  type: string;
  description: string;
  created_at: string;
}

interface UserDetail {
  user: User & {
    interpreter_name?: string;
    interpreter_phone?: string;
    preferred_language?: string;
  };
  reports: Report[];
  transactions: Transaction[];
}

type TabType = 'overview' | 'users' | 'reports' | 'transactions';

export default function AdminPage() {
  const { data: session, status } = useSession();
  const router = useRouter();
  const [stats, setStats] = useState<Stats | null>(null);
  const [users, setUsers] = useState<User[]>([]);
  const [reports, setReports] = useState<Report[]>([]);
  const [transactions, setTransactions] = useState<Transaction[]>([]);
  const [loading, setLoading] = useState(true);
  const [activeTab, setActiveTab] = useState<TabType>('overview');

  // Pagination
  const [usersPage, setUsersPage] = useState(1);
  const [reportsPage, setReportsPage] = useState(1);
  const [reportsTotal, setReportsTotal] = useState(0);
  const [transactionsPage, setTransactionsPage] = useState(1);
  const [transactionsTotal, setTransactionsTotal] = useState(0);

  // Search
  const [userSearch, setUserSearch] = useState('');
  const [reportSearch, setReportSearch] = useState('');

  // Modal
  const [selectedUser, setSelectedUser] = useState<UserDetail | null>(null);
  const [userModalOpen, setUserModalOpen] = useState(false);

  const isAdmin = session?.user?.email && ADMIN_EMAILS.includes(session.user.email);

  const fetchStats = useCallback(async () => {
    const res = await fetch('/api/admin/stats');
    if (res.ok) {
      const data: Stats = await res.json();
      setStats(data);
    }
  }, []);

  const fetchUsers = useCallback(async () => {
    const res = await fetch('/api/admin/users');
    if (res.ok) {
      const data = await res.json() as { users: User[] };
      setUsers(data.users || []);
    }
  }, []);

  const fetchReports = useCallback(async (page: number, search: string) => {
    const params = new URLSearchParams({ page: String(page), limit: '20' });
    if (search) params.append('search', search);

    const res = await fetch(`/api/admin/reports?${params}`);
    if (res.ok) {
      const data = await res.json() as { reports: Report[]; totalPages: number };
      setReports(data.reports || []);
      setReportsTotal(data.totalPages || 1);
    }
  }, []);

  const fetchTransactions = useCallback(async (page: number) => {
    const res = await fetch(`/api/admin/transactions?page=${page}&limit=50`);
    if (res.ok) {
      const data = await res.json() as { transactions: Transaction[]; totalPages: number };
      setTransactions(data.transactions || []);
      setTransactionsTotal(data.totalPages || 1);
    }
  }, []);

  const fetchAll = useCallback(async () => {
    setLoading(true);
    await Promise.all([
      fetchStats(),
      fetchUsers(),
      fetchReports(1, ''),
      fetchTransactions(1),
    ]);
    setLoading(false);
  }, [fetchStats, fetchUsers, fetchReports, fetchTransactions]);

  useEffect(() => {
    if (status === 'loading') return;
    if (!session || !isAdmin) {
      router.push('/dashboard');
      return;
    }
    fetchAll();
  }, [session, status, isAdmin, router, fetchAll]);

  useEffect(() => {
    if (activeTab === 'reports') {
      fetchReports(reportsPage, reportSearch);
    }
  }, [reportsPage, reportSearch, activeTab, fetchReports]);

  useEffect(() => {
    if (activeTab === 'transactions') {
      fetchTransactions(transactionsPage);
    }
  }, [transactionsPage, activeTab, fetchTransactions]);

  const adjustCredits = async (userId: string, amount: number) => {
    const reason = prompt(`크레딧 ${amount > 0 ? '추가' : '차감'} 사유를 입력하세요:`);
    if (!reason) return;

    try {
      const res = await fetch('/api/admin/credits', {
        method: 'POST',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify({ userId, amount, reason }),
      });

      if (res.ok) {
        fetchUsers();
        fetchStats();
        alert('크레딧이 조정되었습니다.');
      } else {
        alert('크레딧 조정에 실패했습니다.');
      }
    } catch {
      alert('오류가 발생했습니다.');
    }
  };

  const viewUserDetail = async (userId: string) => {
    try {
      const res = await fetch(`/api/admin/users/${userId}`);
      if (res.ok) {
        const data = await res.json() as UserDetail;
        setSelectedUser(data);
        setUserModalOpen(true);
      }
    } catch {
      alert('사용자 정보를 불러올 수 없습니다.');
    }
  };

  const deleteReport = async (reportId: string) => {
    if (!confirm('이 보고서를 삭제하시겠습니까?')) return;

    try {
      const res = await fetch('/api/admin/reports', {
        method: 'DELETE',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify({ reportId }),
      });

      if (res.ok) {
        fetchReports(reportsPage, reportSearch);
        fetchStats();
        alert('보고서가 삭제되었습니다.');
      } else {
        alert('삭제에 실패했습니다.');
      }
    } catch {
      alert('오류가 발생했습니다.');
    }
  };

  const deleteUser = async (userId: string) => {
    if (!confirm('이 사용자를 삭제하시겠습니까? 관련 데이터도 함께 삭제됩니다.')) return;

    try {
      const res = await fetch(`/api/admin/users/${userId}`, {
        method: 'DELETE',
      });

      if (res.ok) {
        setUserModalOpen(false);
        fetchUsers();
        fetchStats();
        alert('사용자가 삭제되었습니다.');
      } else {
        alert('삭제에 실패했습니다.');
      }
    } catch {
      alert('오류가 발생했습니다.');
    }
  };

  const exportUsers = () => {
    const csv = [
      ['이메일', '이름', '크레딧', '프로필완료', '가입일'].join(','),
      ...users.map((u) =>
        [
          u.email,
          u.name || '',
          u.credits,
          u.profile_completed ? 'Y' : 'N',
          new Date(u.created_at).toLocaleDateString('ko-KR'),
        ].join(',')
      ),
    ].join('\n');

    const blob = new Blob(['\uFEFF' + csv], { type: 'text/csv;charset=utf-8;' });
    const url = URL.createObjectURL(blob);
    const a = document.createElement('a');
    a.href = url;
    a.download = `users_${new Date().toISOString().split('T')[0]}.csv`;
    a.click();
  };

  const filteredUsers = users.filter(
    (u) =>
      u.email.toLowerCase().includes(userSearch.toLowerCase()) ||
      (u.name && u.name.toLowerCase().includes(userSearch.toLowerCase()))
  );

  if (status === 'loading' || loading) {
    return (
      <div className="min-h-screen bg-[#0f0f0f] flex items-center justify-center">
        <RefreshCw className="w-8 h-8 animate-spin text-indigo-400" />
      </div>
    );
  }

  if (!isAdmin) {
    return null;
  }

  return (
    <div className="min-h-screen bg-[#0f0f0f]">
      {/* Header */}
      <header className="bg-[#1a1a1a] border-b border-[#2a2a2a]">
        <div className="max-w-7xl mx-auto px-4 py-4 flex items-center justify-between">
          <div className="flex items-center gap-4">
            <Link href="/dashboard" className="text-gray-400 hover:text-gray-200">
              <ArrowLeft className="w-5 h-5" />
            </Link>
            <div>
              <h1 className="text-xl font-bold text-gray-100">Phiennoi Admin</h1>
              <p className="text-[10px] text-gray-600">Epicstage Corp. Management Console</p>
            </div>
          </div>
          <button
            onClick={fetchAll}
            className="flex items-center gap-2 text-gray-400 hover:text-gray-200"
          >
            <RefreshCw className="w-4 h-4" />
            새로고침
          </button>
        </div>
      </header>

      <main className="max-w-7xl mx-auto px-4 py-8">
        {/* Stats Cards */}
        {stats && (
          <div className="grid grid-cols-2 md:grid-cols-4 gap-4 mb-8">
            <div className="bg-[#1a1a1a] border border-[#2a2a2a] rounded-xl p-6">
              <div className="flex items-center gap-3 mb-2">
                <Users className="w-5 h-5 text-indigo-400" />
                <span className="text-gray-400 text-sm">총 회원</span>
              </div>
              <p className="text-2xl font-bold text-gray-100">{stats.totalUsers}</p>
              <p className="text-xs text-gray-500 mt-1">오늘 +{stats.todaySignups}</p>
            </div>

            <div className="bg-[#1a1a1a] border border-[#2a2a2a] rounded-xl p-6">
              <div className="flex items-center gap-3 mb-2">
                <FileText className="w-5 h-5 text-green-400" />
                <span className="text-gray-400 text-sm">총 보고서</span>
              </div>
              <p className="text-2xl font-bold text-gray-100">{stats.totalReports}</p>
            </div>

            <div className="bg-[#1a1a1a] border border-[#2a2a2a] rounded-xl p-6">
              <div className="flex items-center gap-3 mb-2">
                <CreditCard className="w-5 h-5 text-amber-400" />
                <span className="text-gray-400 text-sm">사용된 크레딧</span>
              </div>
              <p className="text-2xl font-bold text-gray-100">{stats.totalCreditsUsed}</p>
            </div>

            <div className="bg-[#1a1a1a] border border-[#2a2a2a] rounded-xl p-6">
              <div className="flex items-center gap-3 mb-2">
                <History className="w-5 h-5 text-purple-400" />
                <span className="text-gray-400 text-sm">오늘 가입</span>
              </div>
              <p className="text-2xl font-bold text-gray-100">{stats.todaySignups}</p>
            </div>
          </div>
        )}

        {/* Tabs */}
        <div className="flex gap-2 mb-6 overflow-x-auto">
          {[
            { id: 'overview', label: '개요' },
            { id: 'users', label: '회원 관리' },
            { id: 'reports', label: '보고서 관리' },
            { id: 'transactions', label: '거래 내역' },
          ].map((tab) => (
            <button
              key={tab.id}
              onClick={() => setActiveTab(tab.id as TabType)}
              className={`px-4 py-2 rounded-lg font-medium whitespace-nowrap ${
                activeTab === tab.id
                  ? 'bg-indigo-600 text-white'
                  : 'bg-[#1a1a1a] border border-[#2a2a2a] text-gray-400 hover:bg-[#242424]'
              }`}
            >
              {tab.label}
            </button>
          ))}
        </div>

        {/* Overview Tab */}
        {activeTab === 'overview' && (
          <div className="bg-[#1a1a1a] border border-[#2a2a2a] rounded-xl p-6">
            <h2 className="text-lg font-semibold text-gray-100 mb-4">최근 가입 회원</h2>
            <div className="space-y-3">
              {users.slice(0, 5).map((user) => (
                <div
                  key={user.id}
                  className="flex items-center justify-between py-2 border-b border-[#2a2a2a] last:border-0"
                >
                  <div>
                    <p className="font-medium text-gray-200">{user.email}</p>
                    <p className="text-sm text-gray-500">
                      {new Date(user.created_at).toLocaleDateString('ko-KR')}
                    </p>
                  </div>
                  <span className="text-sm text-gray-400">{user.credits} 크레딧</span>
                </div>
              ))}
            </div>
          </div>
        )}

        {/* Users Tab */}
        {activeTab === 'users' && (
          <div className="bg-[#1a1a1a] border border-[#2a2a2a] rounded-xl overflow-hidden">
            <div className="p-4 border-b border-[#2a2a2a] flex flex-col sm:flex-row gap-4 justify-between">
              <div className="relative flex-1 max-w-md">
                <Search className="absolute left-3 top-1/2 -translate-y-1/2 w-4 h-4 text-gray-500" />
                <input
                  type="text"
                  placeholder="이메일 또는 이름 검색..."
                  value={userSearch}
                  onChange={(e) => setUserSearch(e.target.value)}
                  className="w-full pl-10 pr-4 py-2 bg-[#242424] border border-[#3a3a3a] rounded-lg text-gray-200 placeholder-gray-500 focus:ring-2 focus:ring-indigo-500 focus:border-transparent"
                />
              </div>
              <button
                onClick={exportUsers}
                className="flex items-center gap-2 px-4 py-2 bg-green-600 text-white rounded-lg hover:bg-green-500"
              >
                <Download className="w-4 h-4" />
                CSV 내보내기
              </button>
            </div>

            <div className="overflow-x-auto">
              <table className="w-full">
                <thead className="bg-[#242424]">
                  <tr>
                    <th className="px-6 py-3 text-left text-xs font-medium text-gray-400 uppercase">
                      이메일
                    </th>
                    <th className="px-6 py-3 text-left text-xs font-medium text-gray-400 uppercase">
                      이름
                    </th>
                    <th className="px-6 py-3 text-left text-xs font-medium text-gray-400 uppercase">
                      크레딧
                    </th>
                    <th className="px-6 py-3 text-left text-xs font-medium text-gray-400 uppercase">
                      프로필
                    </th>
                    <th className="px-6 py-3 text-left text-xs font-medium text-gray-400 uppercase">
                      가입일
                    </th>
                    <th className="px-6 py-3 text-left text-xs font-medium text-gray-400 uppercase">
                      액션
                    </th>
                  </tr>
                </thead>
                <tbody className="divide-y divide-[#2a2a2a]">
                  {filteredUsers.map((user) => (
                    <tr key={user.id} className="hover:bg-[#242424]">
                      <td className="px-6 py-4 text-sm text-gray-200">{user.email}</td>
                      <td className="px-6 py-4 text-sm text-gray-400">{user.name || '-'}</td>
                      <td className="px-6 py-4 text-sm font-medium text-gray-200">
                        {user.credits}
                      </td>
                      <td className="px-6 py-4">
                        <span
                          className={`px-2 py-1 text-xs rounded-full ${
                            user.profile_completed
                              ? 'bg-green-900/50 text-green-400'
                              : 'bg-[#2a2a2a] text-gray-500'
                          }`}
                        >
                          {user.profile_completed ? '완료' : '미완료'}
                        </span>
                      </td>
                      <td className="px-6 py-4 text-sm text-gray-500">
                        {new Date(user.created_at).toLocaleDateString('ko-KR')}
                      </td>
                      <td className="px-6 py-4">
                        <div className="flex gap-2">
                          <button
                            onClick={() => viewUserDetail(user.id)}
                            className="p-1 text-gray-500 hover:text-indigo-400"
                            title="상세보기"
                          >
                            <Eye className="w-4 h-4" />
                          </button>
                          <button
                            onClick={() => adjustCredits(user.id, 10)}
                            className="px-2 py-1 text-xs bg-green-900/50 text-green-400 rounded hover:bg-green-900/70"
                          >
                            +10
                          </button>
                          <button
                            onClick={() => adjustCredits(user.id, -5)}
                            className="px-2 py-1 text-xs bg-red-900/50 text-red-400 rounded hover:bg-red-900/70"
                          >
                            -5
                          </button>
                        </div>
                      </td>
                    </tr>
                  ))}
                </tbody>
              </table>
            </div>

            {filteredUsers.length === 0 && (
              <div className="p-8 text-center text-gray-500">검색 결과가 없습니다.</div>
            )}
          </div>
        )}

        {/* Reports Tab */}
        {activeTab === 'reports' && (
          <div className="bg-[#1a1a1a] border border-[#2a2a2a] rounded-xl overflow-hidden">
            <div className="p-4 border-b border-[#2a2a2a]">
              <div className="relative max-w-md">
                <Search className="absolute left-3 top-1/2 -translate-y-1/2 w-4 h-4 text-gray-500" />
                <input
                  type="text"
                  placeholder="제목 또는 이메일 검색..."
                  value={reportSearch}
                  onChange={(e) => {
                    setReportSearch(e.target.value);
                    setReportsPage(1);
                  }}
                  className="w-full pl-10 pr-4 py-2 bg-[#242424] border border-[#3a3a3a] rounded-lg text-gray-200 placeholder-gray-500 focus:ring-2 focus:ring-indigo-500 focus:border-transparent"
                />
              </div>
            </div>

            <div className="overflow-x-auto">
              <table className="w-full">
                <thead className="bg-[#242424]">
                  <tr>
                    <th className="px-6 py-3 text-left text-xs font-medium text-gray-400 uppercase">
                      제목
                    </th>
                    <th className="px-6 py-3 text-left text-xs font-medium text-gray-400 uppercase">
                      사용자
                    </th>
                    <th className="px-6 py-3 text-left text-xs font-medium text-gray-400 uppercase">
                      상태
                    </th>
                    <th className="px-6 py-3 text-left text-xs font-medium text-gray-400 uppercase">
                      언어
                    </th>
                    <th className="px-6 py-3 text-left text-xs font-medium text-gray-400 uppercase">
                      크레딧
                    </th>
                    <th className="px-6 py-3 text-left text-xs font-medium text-gray-400 uppercase">
                      생성일
                    </th>
                    <th className="px-6 py-3 text-left text-xs font-medium text-gray-400 uppercase">
                      액션
                    </th>
                  </tr>
                </thead>
                <tbody className="divide-y divide-[#2a2a2a]">
                  {reports.map((report) => (
                    <tr key={report.id} className="hover:bg-[#242424]">
                      <td className="px-6 py-4 text-sm text-gray-200 max-w-xs truncate">
                        {report.title || '제목 없음'}
                      </td>
                      <td className="px-6 py-4 text-sm text-gray-400">{report.user_email}</td>
                      <td className="px-6 py-4">
                        <span
                          className={`px-2 py-1 text-xs rounded-full ${
                            report.status === 'completed'
                              ? 'bg-green-900/50 text-green-400'
                              : report.status === 'processing'
                              ? 'bg-yellow-900/50 text-yellow-400'
                              : 'bg-[#2a2a2a] text-gray-500'
                          }`}
                        >
                          {report.status}
                        </span>
                      </td>
                      <td className="px-6 py-4 text-sm text-gray-400">
                        {report.language_pair || '-'}
                      </td>
                      <td className="px-6 py-4 text-sm text-gray-400">{report.credits_used}</td>
                      <td className="px-6 py-4 text-sm text-gray-500">
                        {new Date(report.created_at).toLocaleDateString('ko-KR')}
                      </td>
                      <td className="px-6 py-4">
                        <button
                          onClick={() => deleteReport(report.id)}
                          className="p-1 text-gray-500 hover:text-red-400"
                          title="삭제"
                        >
                          <Trash2 className="w-4 h-4" />
                        </button>
                      </td>
                    </tr>
                  ))}
                </tbody>
              </table>
            </div>

            {reports.length === 0 && (
              <div className="p-8 text-center text-gray-500">보고서가 없습니다.</div>
            )}

            {/* Pagination */}
            {reportsTotal > 1 && (
              <div className="p-4 border-t border-[#2a2a2a] flex justify-center gap-2">
                <button
                  onClick={() => setReportsPage((p) => Math.max(1, p - 1))}
                  disabled={reportsPage === 1}
                  className="p-2 rounded-lg border border-[#3a3a3a] text-gray-400 disabled:opacity-50 hover:bg-[#242424]"
                >
                  <ChevronLeft className="w-4 h-4" />
                </button>
                <span className="px-4 py-2 text-gray-400">
                  {reportsPage} / {reportsTotal}
                </span>
                <button
                  onClick={() => setReportsPage((p) => Math.min(reportsTotal, p + 1))}
                  disabled={reportsPage === reportsTotal}
                  className="p-2 rounded-lg border border-[#3a3a3a] text-gray-400 disabled:opacity-50 hover:bg-[#242424]"
                >
                  <ChevronRight className="w-4 h-4" />
                </button>
              </div>
            )}
          </div>
        )}

        {/* Transactions Tab */}
        {activeTab === 'transactions' && (
          <div className="bg-[#1a1a1a] border border-[#2a2a2a] rounded-xl overflow-hidden">
            <div className="overflow-x-auto">
              <table className="w-full">
                <thead className="bg-[#242424]">
                  <tr>
                    <th className="px-6 py-3 text-left text-xs font-medium text-gray-400 uppercase">
                      사용자
                    </th>
                    <th className="px-6 py-3 text-left text-xs font-medium text-gray-400 uppercase">
                      금액
                    </th>
                    <th className="px-6 py-3 text-left text-xs font-medium text-gray-400 uppercase">
                      유형
                    </th>
                    <th className="px-6 py-3 text-left text-xs font-medium text-gray-400 uppercase">
                      설명
                    </th>
                    <th className="px-6 py-3 text-left text-xs font-medium text-gray-400 uppercase">
                      일시
                    </th>
                  </tr>
                </thead>
                <tbody className="divide-y divide-[#2a2a2a]">
                  {transactions.map((tx) => (
                    <tr key={tx.id} className="hover:bg-[#242424]">
                      <td className="px-6 py-4 text-sm text-gray-200">{tx.user_email}</td>
                      <td className="px-6 py-4">
                        <span
                          className={`font-medium ${
                            tx.amount > 0 ? 'text-green-400' : 'text-red-400'
                          }`}
                        >
                          {tx.amount > 0 ? '+' : ''}
                          {tx.amount}
                        </span>
                      </td>
                      <td className="px-6 py-4">
                        <span className="px-2 py-1 text-xs rounded-full bg-[#2a2a2a] text-gray-400">
                          {tx.type}
                        </span>
                      </td>
                      <td className="px-6 py-4 text-sm text-gray-400 max-w-xs truncate">
                        {tx.description}
                      </td>
                      <td className="px-6 py-4 text-sm text-gray-500">
                        {new Date(tx.created_at).toLocaleString('ko-KR')}
                      </td>
                    </tr>
                  ))}
                </tbody>
              </table>
            </div>

            {transactions.length === 0 && (
              <div className="p-8 text-center text-gray-500">거래 내역이 없습니다.</div>
            )}

            {/* Pagination */}
            {transactionsTotal > 1 && (
              <div className="p-4 border-t border-[#2a2a2a] flex justify-center gap-2">
                <button
                  onClick={() => setTransactionsPage((p) => Math.max(1, p - 1))}
                  disabled={transactionsPage === 1}
                  className="p-2 rounded-lg border border-[#3a3a3a] text-gray-400 disabled:opacity-50 hover:bg-[#242424]"
                >
                  <ChevronLeft className="w-4 h-4" />
                </button>
                <span className="px-4 py-2 text-gray-400">
                  {transactionsPage} / {transactionsTotal}
                </span>
                <button
                  onClick={() => setTransactionsPage((p) => Math.min(transactionsTotal, p + 1))}
                  disabled={transactionsPage === transactionsTotal}
                  className="p-2 rounded-lg border border-[#3a3a3a] text-gray-400 disabled:opacity-50 hover:bg-[#242424]"
                >
                  <ChevronRight className="w-4 h-4" />
                </button>
              </div>
            )}
          </div>
        )}
      </main>

      {/* User Detail Modal */}
      {userModalOpen && selectedUser && (
        <div className="fixed inset-0 bg-black/70 flex items-center justify-center z-50 p-4">
          <div className="bg-[#1a1a1a] border border-[#2a2a2a] rounded-xl max-w-2xl w-full max-h-[90vh] overflow-y-auto">
            <div className="p-6 border-b border-[#2a2a2a] flex justify-between items-center sticky top-0 bg-[#1a1a1a]">
              <h2 className="text-lg font-semibold text-gray-100">회원 상세 정보</h2>
              <button onClick={() => setUserModalOpen(false)} className="text-gray-500 hover:text-gray-300">
                <X className="w-5 h-5" />
              </button>
            </div>

            <div className="p-6 space-y-6">
              {/* User Info */}
              <div>
                <h3 className="font-medium text-gray-200 mb-3">기본 정보</h3>
                <div className="grid grid-cols-2 gap-4 text-sm">
                  <div>
                    <span className="text-gray-500">이메일</span>
                    <p className="font-medium text-gray-200">{selectedUser.user.email}</p>
                  </div>
                  <div>
                    <span className="text-gray-500">이름</span>
                    <p className="font-medium text-gray-200">{selectedUser.user.name || '-'}</p>
                  </div>
                  <div>
                    <span className="text-gray-500">크레딧</span>
                    <p className="font-medium text-gray-200">{selectedUser.user.credits}</p>
                  </div>
                  <div>
                    <span className="text-gray-500">프로필 완료</span>
                    <p className="font-medium text-gray-200">
                      {selectedUser.user.profile_completed ? '완료' : '미완료'}
                    </p>
                  </div>
                  <div>
                    <span className="text-gray-500">통역사 이름</span>
                    <p className="font-medium text-gray-200">{selectedUser.user.interpreter_name || '-'}</p>
                  </div>
                  <div>
                    <span className="text-gray-500">통역사 연락처</span>
                    <p className="font-medium text-gray-200">{selectedUser.user.interpreter_phone || '-'}</p>
                  </div>
                  <div>
                    <span className="text-gray-500">가입일</span>
                    <p className="font-medium text-gray-200">
                      {new Date(selectedUser.user.created_at).toLocaleDateString('ko-KR')}
                    </p>
                  </div>
                </div>
              </div>

              {/* Reports */}
              <div>
                <h3 className="font-medium text-gray-200 mb-3">
                  최근 보고서 ({selectedUser.reports.length})
                </h3>
                {selectedUser.reports.length > 0 ? (
                  <div className="space-y-2">
                    {selectedUser.reports.map((report) => (
                      <div
                        key={report.id}
                        className="flex justify-between items-center py-2 border-b border-[#2a2a2a] text-sm"
                      >
                        <span className="truncate max-w-xs text-gray-300">{report.title || '제목 없음'}</span>
                        <span className="text-gray-500">
                          {new Date(report.created_at).toLocaleDateString('ko-KR')}
                        </span>
                      </div>
                    ))}
                  </div>
                ) : (
                  <p className="text-gray-500 text-sm">보고서가 없습니다.</p>
                )}
              </div>

              {/* Transactions */}
              <div>
                <h3 className="font-medium text-gray-200 mb-3">
                  최근 거래 ({selectedUser.transactions.length})
                </h3>
                {selectedUser.transactions.length > 0 ? (
                  <div className="space-y-2">
                    {selectedUser.transactions.map((tx) => (
                      <div
                        key={tx.id}
                        className="flex justify-between items-center py-2 border-b border-[#2a2a2a] text-sm"
                      >
                        <div>
                          <span
                            className={`font-medium ${
                              tx.amount > 0 ? 'text-green-400' : 'text-red-400'
                            }`}
                          >
                            {tx.amount > 0 ? '+' : ''}
                            {tx.amount}
                          </span>
                          <span className="text-gray-500 ml-2">{tx.type}</span>
                        </div>
                        <span className="text-gray-500">
                          {new Date(tx.created_at).toLocaleDateString('ko-KR')}
                        </span>
                      </div>
                    ))}
                  </div>
                ) : (
                  <p className="text-gray-500 text-sm">거래 내역이 없습니다.</p>
                )}
              </div>

              {/* Actions */}
              <div className="flex gap-3 pt-4 border-t border-[#2a2a2a]">
                <button
                  onClick={() => adjustCredits(selectedUser.user.id, 10)}
                  className="flex-1 py-2 bg-green-600 text-white rounded-lg hover:bg-green-500"
                >
                  크레딧 +10
                </button>
                <button
                  onClick={() => deleteUser(selectedUser.user.id)}
                  className="px-4 py-2 bg-red-600 text-white rounded-lg hover:bg-red-500"
                >
                  <Trash2 className="w-4 h-4" />
                </button>
              </div>
            </div>
          </div>
        </div>
      )}
    </div>
  );
}
