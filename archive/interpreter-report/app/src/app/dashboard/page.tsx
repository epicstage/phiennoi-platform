'use client';

import { useEffect, useState } from 'react';
import Link from 'next/link';
import { useSession } from 'next-auth/react';
import { useRouter } from 'next/navigation';
import {
  Mic,
  FileText,
  Clock,
  CreditCard,
  Settings,
  Plus,
  ChevronRight,
  Gift,
  Loader2,
  Play,
  X
} from 'lucide-react';

interface UserData {
  name: string;
  credits: number;
  profileCompleted: boolean;
  referralCode: string;
}

interface Report {
  id: string;
  title: string;
  created_at: string;
  status: string;
}

interface AdWatchInfo {
  remaining: number;
  dailyLimit: number;
  rewardPerWatch: number;
}

export default function DashboardPage() {
  const { data: session, status } = useSession();
  const router = useRouter();
  const [user, setUser] = useState<UserData | null>(null);
  const [reports, setReports] = useState<Report[]>([]);
  const [isLoading, setIsLoading] = useState(true);
  const [adInfo, setAdInfo] = useState<AdWatchInfo | null>(null);
  const [showAdModal, setShowAdModal] = useState(false);
  const [adCountdown, setAdCountdown] = useState(15);
  const [isWatchingAd, setIsWatchingAd] = useState(false);
  const [adMessage, setAdMessage] = useState<string | null>(null);

  useEffect(() => {
    if (status === 'unauthenticated') {
      router.push('/login');
    }
  }, [status, router]);

  useEffect(() => {
    const fetchData = async () => {
      if (!session?.user?.email) return;

      try {
        // Fetch user data and reports in parallel
        const [userRes, reportsRes] = await Promise.all([
          fetch('/api/user'),
          fetch('/api/reports?limit=5'),
        ]);

        if (userRes.ok) {
          const userData = await userRes.json() as {
            name?: string;
            credits?: number;
            profileCompleted?: boolean;
            referralCode?: string;
          };
          setUser({
            name: userData.name || session.user.name || '사용자',
            credits: userData.credits || 0,
            profileCompleted: userData.profileCompleted || false,
            referralCode: userData.referralCode || '',
          });
        }

        if (reportsRes.ok) {
          const reportsData = await reportsRes.json() as { reports?: Report[] };
          setReports(reportsData.reports || []);
        }

        // Fetch ad watch info
        const adRes = await fetch('/api/watch-ad');
        if (adRes.ok) {
          const adData = await adRes.json() as AdWatchInfo;
          setAdInfo(adData);
        }
      } catch (err) {
        console.error('Failed to fetch data:', err);
      } finally {
        setIsLoading(false);
      }
    };

    if (status === 'authenticated') {
      fetchData();
    }
  }, [session, status]);

  // Ad countdown timer
  useEffect(() => {
    if (!isWatchingAd || adCountdown <= 0) return;

    const timer = setTimeout(() => {
      setAdCountdown(prev => prev - 1);
    }, 1000);

    return () => clearTimeout(timer);
  }, [isWatchingAd, adCountdown]);

  // Complete ad watch when countdown reaches 0
  useEffect(() => {
    if (isWatchingAd && adCountdown === 0) {
      completeAdWatch();
    }
  }, [adCountdown, isWatchingAd]);

  const startAdWatch = () => {
    if (!adInfo || adInfo.remaining <= 0) return;
    setShowAdModal(true);
    setAdCountdown(15);
    setIsWatchingAd(true);
    setAdMessage(null);
  };

  const completeAdWatch = async () => {
    setIsWatchingAd(false);
    try {
      const res = await fetch('/api/watch-ad', {
        method: 'POST',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify({ adToken: 'completed' }),
      });
      const data = await res.json() as { success?: boolean; message?: string; credits?: number; error?: string };

      if (data.success) {
        setAdMessage(data.message || '크레딧이 지급되었습니다!');
        // Update user credits
        if (data.credits !== undefined) {
          setUser(prev => prev ? { ...prev, credits: data.credits! } : null);
        }
        // Update remaining ad watches
        setAdInfo(prev => prev ? { ...prev, remaining: prev.remaining - 1 } : null);
      } else {
        setAdMessage(data.error || '오류가 발생했습니다.');
      }
    } catch (err) {
      setAdMessage('서버 오류가 발생했습니다.');
    }
  };

  const closeAdModal = () => {
    setShowAdModal(false);
    setIsWatchingAd(false);
    setAdCountdown(15);
  };

  if (status === 'loading' || isLoading) {
    return (
      <div className="min-h-screen bg-[#0f0f0f] flex items-center justify-center">
        <Loader2 className="w-8 h-8 animate-spin text-indigo-400" />
      </div>
    );
  }

  const displayUser = user || {
    name: session?.user?.name || '사용자',
    credits: 0,
    profileCompleted: false,
    referralCode: '',
  };

  const formatDate = (dateString: string) => {
    const date = new Date(dateString);
    return date.toLocaleDateString('ko-KR', {
      month: 'short',
      day: 'numeric',
      hour: '2-digit',
      minute: '2-digit',
    });
  };

  return (
    <div className="min-h-screen bg-[#0f0f0f]">
      {/* Header */}
      <header className="bg-[#1a1a1a] border-b border-[#2a2a2a] px-6 py-4">
        <div className="max-w-4xl mx-auto flex justify-between items-center">
          <div>
            <h1 className="text-xl font-bold text-indigo-400">Phiennoi</h1>
            <p className="text-[10px] text-gray-600">by Epicstage Corp.</p>
          </div>
          <Link href="/settings" className="p-2 text-gray-400 hover:text-gray-200">
            <Settings className="w-6 h-6" />
          </Link>
        </div>
      </header>

      <main className="max-w-4xl mx-auto px-6 py-6 space-y-6">
        {/* Credit Card */}
        <div className="bg-gradient-to-r from-indigo-600 to-indigo-700 rounded-2xl p-6 text-white">
          <div className="flex justify-between items-start mb-4">
            <div>
              <p className="text-indigo-200 text-sm">안녕하세요</p>
              <p className="text-xl font-semibold">{displayUser.name}님</p>
            </div>
            <div className="flex items-center gap-2 bg-white/20 rounded-lg px-3 py-1">
              <CreditCard className="w-4 h-4" />
              <span className="font-medium">{displayUser.credits} 크레딧</span>
            </div>
          </div>

          {!displayUser.profileCompleted && (
            <Link
              href="/profile"
              className="flex items-center justify-between bg-white/10 rounded-xl p-4 hover:bg-white/20 transition"
            >
              <div className="flex items-center gap-3">
                <div className="w-10 h-10 rounded-full bg-yellow-400 flex items-center justify-center">
                  <Gift className="w-5 h-5 text-yellow-900" />
                </div>
                <div>
                  <p className="font-medium">프로필 완성하고 +20 크레딧 받기</p>
                  <p className="text-sm text-indigo-200">대학, 전공, 자격증 정보 입력</p>
                </div>
              </div>
              <ChevronRight className="w-5 h-5" />
            </Link>
          )}

          {/* Ad Watch Button */}
          {adInfo && adInfo.remaining > 0 && (
            <button
              onClick={startAdWatch}
              className="w-full flex items-center justify-between bg-green-600/20 rounded-xl p-4 hover:bg-green-600/30 transition mt-3"
            >
              <div className="flex items-center gap-3">
                <div className="w-10 h-10 rounded-full bg-green-500 flex items-center justify-center">
                  <Play className="w-5 h-5 text-white" />
                </div>
                <div className="text-left">
                  <p className="font-medium">광고 보고 +{adInfo.rewardPerWatch} 크레딧 받기</p>
                  <p className="text-sm text-green-200">오늘 {adInfo.remaining}회 남음</p>
                </div>
              </div>
              <ChevronRight className="w-5 h-5" />
            </button>
          )}
        </div>

        {/* Ad Watch Modal */}
        {showAdModal && (
          <div className="fixed inset-0 bg-black/80 flex items-center justify-center z-50 p-4">
            <div className="bg-[#1a1a1a] rounded-2xl w-full max-w-md p-6 relative">
              {!adMessage ? (
                <>
                  <div className="text-center mb-6">
                    <div className="w-20 h-20 rounded-full bg-green-600 flex items-center justify-center mx-auto mb-4">
                      <Play className="w-10 h-10 text-white" />
                    </div>
                    <h3 className="text-xl font-bold text-gray-100 mb-2">광고 시청 중</h3>
                    <p className="text-gray-400">
                      {isWatchingAd
                        ? `${adCountdown}초 후 크레딧이 지급됩니다`
                        : '잠시만 기다려주세요...'}
                    </p>
                  </div>

                  {/* Progress bar */}
                  <div className="bg-[#2a2a2a] rounded-full h-3 mb-6 overflow-hidden">
                    <div
                      className="bg-green-500 h-full transition-all duration-1000 ease-linear"
                      style={{ width: `${((15 - adCountdown) / 15) * 100}%` }}
                    />
                  </div>

                  {/* Fake ad content placeholder */}
                  <div className="bg-gradient-to-br from-indigo-900/50 to-purple-900/50 rounded-xl p-8 text-center border border-indigo-800/30">
                    <p className="text-indigo-300 text-sm mb-2">광고 영역</p>
                    <p className="text-gray-400 text-xs">실제 광고가 여기에 표시됩니다</p>
                  </div>
                </>
              ) : (
                <div className="text-center py-6">
                  <div className="w-16 h-16 rounded-full bg-green-600 flex items-center justify-center mx-auto mb-4">
                    <Gift className="w-8 h-8 text-white" />
                  </div>
                  <h3 className="text-xl font-bold text-gray-100 mb-2">완료!</h3>
                  <p className="text-gray-300 mb-6">{adMessage}</p>
                  <button
                    onClick={closeAdModal}
                    className="w-full bg-green-600 hover:bg-green-700 text-white font-medium py-3 rounded-xl transition"
                  >
                    확인
                  </button>
                </div>
              )}

              {/* Close button (only when not watching) */}
              {!isWatchingAd && !adMessage && (
                <button
                  onClick={closeAdModal}
                  className="absolute top-4 right-4 text-gray-400 hover:text-gray-200"
                >
                  <X className="w-6 h-6" />
                </button>
              )}
            </div>
          </div>
        )}

        {/* Quick Actions */}
        <div className="grid grid-cols-2 gap-4">
          <Link
            href="/report/new"
            className="bg-[#1a1a1a] border border-[#2a2a2a] rounded-xl p-6 hover:bg-[#242424] transition flex flex-col items-center gap-3 text-center"
          >
            <div className="w-14 h-14 rounded-full bg-indigo-900/50 flex items-center justify-center">
              <Plus className="w-7 h-7 text-indigo-400" />
            </div>
            <div>
              <p className="font-semibold text-gray-100">새 보고서</p>
              <p className="text-sm text-gray-500">녹음 또는 파일 업로드</p>
            </div>
          </Link>

          <Link
            href="/report/new?mode=record"
            className="bg-[#1a1a1a] border border-[#2a2a2a] rounded-xl p-6 hover:bg-[#242424] transition flex flex-col items-center gap-3 text-center"
          >
            <div className="w-14 h-14 rounded-full bg-red-900/50 flex items-center justify-center">
              <Mic className="w-7 h-7 text-red-400" />
            </div>
            <div>
              <p className="font-semibold text-gray-100">녹음 시작</p>
              <p className="text-sm text-gray-500">실시간 녹음</p>
            </div>
          </Link>
        </div>

        {/* Recent Reports */}
        <div className="bg-[#1a1a1a] border border-[#2a2a2a] rounded-xl">
          <div className="flex justify-between items-center px-6 py-4 border-b border-[#2a2a2a]">
            <h2 className="font-semibold text-gray-100">최근 보고서</h2>
            <Link href="/reports" className="text-sm text-indigo-400 hover:text-indigo-300">
              전체보기
            </Link>
          </div>

          {reports.length > 0 ? (
            <div className="divide-y divide-[#2a2a2a]">
              {reports.map((report) => (
                <Link
                  key={report.id}
                  href={`/report/${report.id}`}
                  className="flex items-center gap-4 px-6 py-4 hover:bg-[#242424] transition"
                >
                  <div className="w-10 h-10 rounded-lg bg-[#2a2a2a] flex items-center justify-center">
                    <FileText className="w-5 h-5 text-gray-400" />
                  </div>
                  <div className="flex-1">
                    <p className="font-medium text-gray-100">{report.title || '제목 없음'}</p>
                    <p className="text-sm text-gray-500 flex items-center gap-1">
                      <Clock className="w-3 h-3" />
                      {formatDate(report.created_at)}
                    </p>
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
              <p className="text-gray-500">아직 작성한 보고서가 없습니다</p>
              <Link
                href="/report/new"
                className="inline-flex items-center gap-2 text-indigo-400 hover:text-indigo-300 mt-2"
              >
                <Plus className="w-4 h-4" />
                첫 보고서 작성하기
              </Link>
            </div>
          )}
        </div>

        {/* Help Section */}
        <div className="bg-indigo-900/20 border border-indigo-800/30 rounded-xl p-6">
          <h3 className="font-semibold text-gray-100 mb-2">사용 방법</h3>
          <ol className="text-sm text-gray-400 space-y-2">
            <li className="flex items-start gap-2">
              <span className="flex-shrink-0 w-5 h-5 rounded-full bg-indigo-600 text-white text-xs flex items-center justify-center">1</span>
              <span>미팅을 녹음하거나 녹음 파일을 업로드하세요</span>
            </li>
            <li className="flex items-start gap-2">
              <span className="flex-shrink-0 w-5 h-5 rounded-full bg-indigo-600 text-white text-xs flex items-center justify-center">2</span>
              <span>보고서 양식을 선택하세요</span>
            </li>
            <li className="flex items-start gap-2">
              <span className="flex-shrink-0 w-5 h-5 rounded-full bg-indigo-600 text-white text-xs flex items-center justify-center">3</span>
              <span>AI가 자동으로 보고서를 생성해드립니다</span>
            </li>
            <li className="flex items-start gap-2">
              <span className="flex-shrink-0 w-5 h-5 rounded-full bg-indigo-600 text-white text-xs flex items-center justify-center">4</span>
              <span>서명 후 PDF로 다운로드하세요</span>
            </li>
          </ol>
        </div>

        {/* Footer */}
        <footer className="text-center py-4">
          <p className="text-xs text-gray-600">© 2025 Epicstage Corp. All rights reserved.</p>
        </footer>
      </main>
    </div>
  );
}
