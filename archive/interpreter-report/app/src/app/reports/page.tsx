'use client';

import { useEffect, useState } from 'react';
import Link from 'next/link';
import { useSession } from 'next-auth/react';
import { useRouter } from 'next/navigation';
import {
  ArrowLeft,
  FileText,
  Clock,
  ChevronRight,
  Plus,
  Loader2,
  Search
} from 'lucide-react';

interface Report {
  id: string;
  title: string;
  created_at: string;
  status: string;
  template_type: string;
  language: string;
}

export default function ReportsPage() {
  const { data: session, status } = useSession();
  const router = useRouter();
  const [reports, setReports] = useState<Report[]>([]);
  const [isLoading, setIsLoading] = useState(true);
  const [searchQuery, setSearchQuery] = useState('');
  const [page, setPage] = useState(1);
  const [totalPages, setTotalPages] = useState(1);

  useEffect(() => {
    if (status === 'unauthenticated') {
      router.push('/login');
    }
  }, [status, router]);

  useEffect(() => {
    const fetchReports = async () => {
      if (!session?.user?.email) return;

      setIsLoading(true);
      try {
        const res = await fetch(`/api/reports?page=${page}&limit=20`);
        if (res.ok) {
          const data = await res.json() as { reports?: Report[]; totalPages?: number };
          setReports(data.reports || []);
          setTotalPages(data.totalPages || 1);
        }
      } catch (err) {
        console.error('Failed to fetch reports:', err);
      } finally {
        setIsLoading(false);
      }
    };

    if (status === 'authenticated') {
      fetchReports();
    }
  }, [session, status, page]);

  const formatDate = (dateString: string) => {
    const date = new Date(dateString);
    return date.toLocaleDateString('ko-KR', {
      year: 'numeric',
      month: 'short',
      day: 'numeric',
      hour: '2-digit',
      minute: '2-digit',
    });
  };

  const getTemplateLabel = (type: string) => {
    switch (type) {
      case 'meeting': return '회의록';
      case 'business': return '비즈니스';
      case 'standard': return '표준';
      default: return type;
    }
  };

  const filteredReports = reports.filter(report =>
    (report.title || '').toLowerCase().includes(searchQuery.toLowerCase())
  );

  if (status === 'loading') {
    return (
      <div className="min-h-screen bg-[#0f0f0f] flex items-center justify-center">
        <Loader2 className="w-8 h-8 animate-spin text-indigo-400" />
      </div>
    );
  }

  return (
    <div className="min-h-screen bg-[#0f0f0f]">
      {/* Header */}
      <header className="bg-[#1a1a1a] border-b border-[#2a2a2a] px-6 py-4">
        <div className="max-w-4xl mx-auto flex items-center gap-4">
          <Link href="/dashboard" className="text-gray-400 hover:text-gray-200">
            <ArrowLeft className="w-6 h-6" />
          </Link>
          <h1 className="text-lg font-semibold text-gray-100">내 보고서</h1>
        </div>
      </header>

      <main className="max-w-4xl mx-auto px-6 py-6 space-y-6">
        {/* Search & Actions */}
        <div className="flex gap-4">
          <div className="flex-1 relative">
            <Search className="absolute left-3 top-1/2 -translate-y-1/2 w-5 h-5 text-gray-500" />
            <input
              type="text"
              value={searchQuery}
              onChange={(e) => setSearchQuery(e.target.value)}
              placeholder="보고서 검색..."
              className="w-full pl-10 pr-4 py-3 bg-[#1a1a1a] border border-[#2a2a2a] rounded-xl text-gray-200 placeholder-gray-500 focus:ring-2 focus:ring-indigo-500 focus:border-transparent"
            />
          </div>
          <Link
            href="/report/new"
            className="flex items-center gap-2 bg-indigo-600 text-white px-4 py-3 rounded-xl font-medium hover:bg-indigo-500 transition"
          >
            <Plus className="w-5 h-5" />
            새 보고서
          </Link>
        </div>

        {/* Reports List */}
        <div className="bg-[#1a1a1a] border border-[#2a2a2a] rounded-xl">
          {isLoading ? (
            <div className="p-12 text-center">
              <Loader2 className="w-8 h-8 animate-spin text-indigo-400 mx-auto" />
            </div>
          ) : filteredReports.length > 0 ? (
            <div className="divide-y divide-[#2a2a2a]">
              {filteredReports.map((report) => (
                <Link
                  key={report.id}
                  href={`/report/${report.id}`}
                  className="flex items-center gap-4 px-6 py-4 hover:bg-[#242424] transition"
                >
                  <div className="w-12 h-12 rounded-lg bg-[#2a2a2a] flex items-center justify-center">
                    <FileText className="w-6 h-6 text-gray-400" />
                  </div>
                  <div className="flex-1 min-w-0">
                    <p className="font-medium text-gray-100 truncate">
                      {report.title || '제목 없음'}
                    </p>
                    <div className="flex items-center gap-3 text-sm text-gray-500">
                      <span className="flex items-center gap-1">
                        <Clock className="w-3 h-3" />
                        {formatDate(report.created_at)}
                      </span>
                      <span className="text-xs bg-[#2a2a2a] px-2 py-0.5 rounded text-gray-400">
                        {getTemplateLabel(report.template_type)}
                      </span>
                    </div>
                  </div>
                  <span className={`text-xs px-2 py-1 rounded-full ${
                    report.status === 'completed'
                      ? 'bg-green-900/50 text-green-400'
                      : 'bg-yellow-900/50 text-yellow-400'
                  }`}>
                    {report.status === 'completed' ? '완료' : '임시저장'}
                  </span>
                  <ChevronRight className="w-5 h-5 text-gray-600" />
                </Link>
              ))}
            </div>
          ) : (
            <div className="px-6 py-12 text-center">
              <div className="w-16 h-16 rounded-full bg-[#2a2a2a] flex items-center justify-center mx-auto mb-4">
                <FileText className="w-8 h-8 text-gray-600" />
              </div>
              <p className="text-gray-500">
                {searchQuery ? '검색 결과가 없습니다' : '아직 작성한 보고서가 없습니다'}
              </p>
              {!searchQuery && (
                <Link
                  href="/report/new"
                  className="inline-flex items-center gap-2 text-indigo-400 hover:text-indigo-300 mt-2"
                >
                  <Plus className="w-4 h-4" />
                  첫 보고서 작성하기
                </Link>
              )}
            </div>
          )}
        </div>

        {/* Pagination */}
        {totalPages > 1 && (
          <div className="flex justify-center gap-2">
            <button
              onClick={() => setPage(p => Math.max(1, p - 1))}
              disabled={page === 1}
              className="px-4 py-2 border border-[#3a3a3a] rounded-lg text-gray-300 disabled:opacity-50 disabled:cursor-not-allowed hover:bg-[#242424]"
            >
              이전
            </button>
            <span className="px-4 py-2 text-gray-500">
              {page} / {totalPages}
            </span>
            <button
              onClick={() => setPage(p => Math.min(totalPages, p + 1))}
              disabled={page === totalPages}
              className="px-4 py-2 border border-[#3a3a3a] rounded-lg text-gray-300 disabled:opacity-50 disabled:cursor-not-allowed hover:bg-[#242424]"
            >
              다음
            </button>
          </div>
        )}

        {/* Footer */}
        <footer className="text-center py-4">
          <p className="text-xs text-gray-600">© 2025 Epicstage Corp.</p>
        </footer>
      </main>
    </div>
  );
}
