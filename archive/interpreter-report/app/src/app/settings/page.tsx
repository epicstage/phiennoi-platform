'use client';

import { useState, useEffect } from 'react';
import Link from 'next/link';
import { signOut, useSession } from 'next-auth/react';
import { useRouter } from 'next/navigation';
import {
  ArrowLeft,
  User,
  Bell,
  Shield,
  HelpCircle,
  LogOut,
  ChevronRight,
  Loader2,
  Mail,
  Phone,
  Building,
  BookOpen,
  Award,
  MapPin,
  FileText,
  Lock,
  Gift,
  Copy,
  Check,
  Users,
} from 'lucide-react';

interface UserData {
  name: string;
  email: string;
  phone: string;
  university: string;
  major: string;
  koreanCertificate: string;
  experience: string;
  region: string;
  profileCompleted: boolean;
  referralCode: string;
  referredBy: string | null;
}

export default function SettingsPage() {
  const { data: session, status } = useSession();
  const router = useRouter();
  const [user, setUser] = useState<UserData | null>(null);
  const [isLoading, setIsLoading] = useState(true);
  const [showLogoutConfirm, setShowLogoutConfirm] = useState(false);
  const [copied, setCopied] = useState(false);
  const [referralInput, setReferralInput] = useState('');
  const [referralLoading, setReferralLoading] = useState(false);
  const [referralMessage, setReferralMessage] = useState<{ type: 'success' | 'error'; text: string } | null>(null);

  useEffect(() => {
    if (status === 'unauthenticated') {
      router.push('/login');
    }
  }, [status, router]);

  useEffect(() => {
    const fetchUser = async () => {
      if (!session?.user?.email) return;

      try {
        const res = await fetch('/api/user');
        if (res.ok) {
          const data = await res.json() as UserData;
          setUser(data);
        }
      } catch (err) {
        console.error('Failed to fetch user:', err);
      } finally {
        setIsLoading(false);
      }
    };

    if (status === 'authenticated') {
      fetchUser();
    }
  }, [session, status]);

  const handleLogout = async () => {
    await signOut({ callbackUrl: '/' });
  };

  const copyReferralCode = async () => {
    if (!user?.referralCode) return;
    await navigator.clipboard.writeText(user.referralCode);
    setCopied(true);
    setTimeout(() => setCopied(false), 2000);
  };

  const handleApplyReferral = async () => {
    if (!referralInput.trim()) return;

    setReferralLoading(true);
    setReferralMessage(null);

    try {
      const res = await fetch('/api/referral', {
        method: 'POST',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify({ code: referralInput.trim().toUpperCase() }),
      });

      const data = await res.json() as { message?: string; error?: string };

      if (res.ok) {
        setReferralMessage({ type: 'success', text: data.message || '성공' });
        setReferralInput('');
        // Refresh user data
        const userRes = await fetch('/api/user');
        if (userRes.ok) {
          const userData = await userRes.json() as UserData;
          setUser(userData);
        }
      } else {
        setReferralMessage({ type: 'error', text: data.error || '오류가 발생했습니다.' });
      }
    } catch {
      setReferralMessage({ type: 'error', text: '네트워크 오류가 발생했습니다.' });
    } finally {
      setReferralLoading(false);
    }
  };

  if (status === 'loading' || isLoading) {
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
        <div className="max-w-2xl mx-auto flex items-center gap-4">
          <Link href="/dashboard" className="text-gray-400 hover:text-gray-200">
            <ArrowLeft className="w-6 h-6" />
          </Link>
          <h1 className="text-lg font-semibold text-gray-100">설정</h1>
        </div>
      </header>

      <main className="max-w-2xl mx-auto px-6 py-6 space-y-6">
        {/* Profile Section */}
        <section className="bg-[#1a1a1a] border border-[#2a2a2a] rounded-xl overflow-hidden">
          <div className="px-6 py-4 border-b border-[#2a2a2a]">
            <h2 className="font-medium text-gray-100 flex items-center gap-2">
              <User className="w-5 h-5" />
              프로필 정보
            </h2>
          </div>

          {user ? (
            <div className="divide-y divide-[#2a2a2a]">
              <div className="px-6 py-4 flex items-center gap-4">
                <Mail className="w-5 h-5 text-gray-500" />
                <div className="flex-1">
                  <p className="text-sm text-gray-500">이메일</p>
                  <p className="text-gray-200">{user.email}</p>
                </div>
              </div>

              <div className="px-6 py-4 flex items-center gap-4">
                <Phone className="w-5 h-5 text-gray-500" />
                <div className="flex-1">
                  <p className="text-sm text-gray-500">연락처</p>
                  <p className="text-gray-200">{user.phone || '미입력'}</p>
                </div>
              </div>

              <div className="px-6 py-4 flex items-center gap-4">
                <Building className="w-5 h-5 text-gray-500" />
                <div className="flex-1">
                  <p className="text-sm text-gray-500">대학교</p>
                  <p className="text-gray-200">{user.university || '미입력'}</p>
                </div>
              </div>

              <div className="px-6 py-4 flex items-center gap-4">
                <BookOpen className="w-5 h-5 text-gray-500" />
                <div className="flex-1">
                  <p className="text-sm text-gray-500">전공</p>
                  <p className="text-gray-200">{user.major || '미입력'}</p>
                </div>
              </div>

              <div className="px-6 py-4 flex items-center gap-4">
                <Award className="w-5 h-5 text-gray-500" />
                <div className="flex-1">
                  <p className="text-sm text-gray-500">한국어 자격증</p>
                  <p className="text-gray-200">{user.koreanCertificate || '미입력'}</p>
                </div>
              </div>

              <div className="px-6 py-4 flex items-center gap-4">
                <MapPin className="w-5 h-5 text-gray-500" />
                <div className="flex-1">
                  <p className="text-sm text-gray-500">활동 지역</p>
                  <p className="text-gray-200">{user.region || '미입력'}</p>
                </div>
              </div>

              {!user.profileCompleted && (
                <Link
                  href="/profile"
                  className="px-6 py-4 flex items-center justify-between text-indigo-400 hover:bg-indigo-900/20 transition"
                >
                  <span className="font-medium">프로필 완성하고 +20 크레딧 받기</span>
                  <ChevronRight className="w-5 h-5" />
                </Link>
              )}
            </div>
          ) : (
            <div className="px-6 py-8 text-center text-gray-500">
              프로필 정보를 불러올 수 없습니다.
            </div>
          )}
        </section>

        {/* Referral Section */}
        <section className="bg-[#1a1a1a] border border-[#2a2a2a] rounded-xl overflow-hidden">
          <div className="px-6 py-4 border-b border-[#2a2a2a]">
            <h2 className="font-medium text-gray-100 flex items-center gap-2">
              <Users className="w-5 h-5" />
              친구 추천
            </h2>
          </div>

          <div className="divide-y divide-[#2a2a2a]">
            {/* My Referral Code */}
            <div className="px-6 py-4">
              <div className="flex items-center justify-between mb-2">
                <p className="text-sm text-gray-500">내 추천 코드</p>
                <button
                  onClick={copyReferralCode}
                  className="flex items-center gap-1 text-xs text-indigo-400 hover:text-indigo-300"
                >
                  {copied ? (
                    <>
                      <Check className="w-3 h-3" />
                      복사됨
                    </>
                  ) : (
                    <>
                      <Copy className="w-3 h-3" />
                      복사
                    </>
                  )}
                </button>
              </div>
              <div className="flex items-center gap-2">
                <code className="flex-1 bg-[#242424] px-4 py-3 rounded-lg text-lg font-mono text-indigo-400 tracking-wider">
                  {user?.referralCode || '---'}
                </code>
              </div>
              <p className="text-xs text-gray-600 mt-2">
                친구가 이 코드로 가입하면 나와 친구 모두 10 크레딧!
              </p>
            </div>

            {/* Apply Referral Code */}
            {!user?.referredBy && (
              <div className="px-6 py-4">
                <p className="text-sm text-gray-500 mb-2">추천 코드 입력</p>
                <div className="flex gap-2">
                  <input
                    type="text"
                    value={referralInput}
                    onChange={(e) => setReferralInput(e.target.value.toUpperCase())}
                    placeholder="추천인 코드 입력"
                    className="flex-1 bg-[#242424] border border-[#3a3a3a] rounded-lg px-4 py-3 text-gray-100 placeholder-gray-600 font-mono tracking-wider focus:border-indigo-500 focus:outline-none"
                    maxLength={10}
                  />
                  <button
                    onClick={handleApplyReferral}
                    disabled={!referralInput.trim() || referralLoading}
                    className="px-4 py-3 bg-indigo-600 text-white rounded-lg font-medium hover:bg-indigo-500 disabled:opacity-50 disabled:cursor-not-allowed transition flex items-center gap-2"
                  >
                    {referralLoading ? (
                      <Loader2 className="w-4 h-4 animate-spin" />
                    ) : (
                      <Gift className="w-4 h-4" />
                    )}
                    적용
                  </button>
                </div>
                {referralMessage && (
                  <p className={`text-sm mt-2 ${referralMessage.type === 'success' ? 'text-green-400' : 'text-red-400'}`}>
                    {referralMessage.text}
                  </p>
                )}
              </div>
            )}

            {user?.referredBy && (
              <div className="px-6 py-4">
                <div className="flex items-center gap-2 text-green-400">
                  <Check className="w-4 h-4" />
                  <span className="text-sm">추천 코드가 이미 적용되었습니다</span>
                </div>
              </div>
            )}
          </div>
        </section>

        {/* App Settings */}
        <section className="bg-[#1a1a1a] border border-[#2a2a2a] rounded-xl overflow-hidden">
          <div className="px-6 py-4 border-b border-[#2a2a2a]">
            <h2 className="font-medium text-gray-100 flex items-center gap-2">
              <Bell className="w-5 h-5" />
              앱 설정
            </h2>
          </div>

          <div className="divide-y divide-[#2a2a2a]">
            <div className="px-6 py-4 flex items-center justify-between">
              <div>
                <p className="text-gray-200">알림</p>
                <p className="text-sm text-gray-500">푸시 알림 설정</p>
              </div>
              <span className="text-sm text-gray-600">준비 중</span>
            </div>

            <div className="px-6 py-4 flex items-center justify-between">
              <div>
                <p className="text-gray-200">언어</p>
                <p className="text-sm text-gray-500">앱 언어 설정</p>
              </div>
              <span className="text-sm text-gray-400">한국어</span>
            </div>
          </div>
        </section>

        {/* Legal & Support */}
        <section className="bg-[#1a1a1a] border border-[#2a2a2a] rounded-xl overflow-hidden">
          <div className="px-6 py-4 border-b border-[#2a2a2a]">
            <h2 className="font-medium text-gray-100 flex items-center gap-2">
              <Shield className="w-5 h-5" />
              법적 고지 및 지원
            </h2>
          </div>

          <div className="divide-y divide-[#2a2a2a]">
            <Link
              href="/terms"
              className="px-6 py-4 flex items-center justify-between hover:bg-[#242424] transition"
            >
              <div className="flex items-center gap-3">
                <FileText className="w-5 h-5 text-gray-500" />
                <span className="text-gray-200">이용약관</span>
              </div>
              <ChevronRight className="w-5 h-5 text-gray-600" />
            </Link>

            <Link
              href="/privacy"
              className="px-6 py-4 flex items-center justify-between hover:bg-[#242424] transition"
            >
              <div className="flex items-center gap-3">
                <Lock className="w-5 h-5 text-gray-500" />
                <span className="text-gray-200">개인정보처리방침</span>
              </div>
              <ChevronRight className="w-5 h-5 text-gray-600" />
            </Link>

            <Link
              href="mailto:support@phiennoi.com"
              className="px-6 py-4 flex items-center justify-between hover:bg-[#242424] transition"
            >
              <div className="flex items-center gap-3">
                <HelpCircle className="w-5 h-5 text-gray-500" />
                <span className="text-gray-200">고객 지원</span>
              </div>
              <ChevronRight className="w-5 h-5 text-gray-600" />
            </Link>
          </div>
        </section>

        {/* App Version */}
        <div className="text-center text-sm py-4">
          <p className="text-gray-600">Phiennoi v1.0.0</p>
          <p className="text-gray-700 text-xs mt-1">© 2025 Epicstage Corp.</p>
        </div>

        {/* Logout Button */}
        <button
          onClick={() => setShowLogoutConfirm(true)}
          className="w-full bg-[#1a1a1a] border border-[#2a2a2a] rounded-xl px-6 py-4 flex items-center justify-center gap-2 text-red-400 hover:bg-red-900/20 transition"
        >
          <LogOut className="w-5 h-5" />
          <span className="font-medium">로그아웃</span>
        </button>
      </main>

      {/* Logout Confirmation Modal */}
      {showLogoutConfirm && (
        <div className="fixed inset-0 bg-black/70 flex items-center justify-center z-50 px-6">
          <div className="bg-[#1a1a1a] border border-[#2a2a2a] rounded-2xl p-6 max-w-sm w-full">
            <h3 className="text-lg font-semibold text-gray-100 mb-2">
              로그아웃
            </h3>
            <p className="text-gray-400 mb-6">
              정말 로그아웃 하시겠습니까?
            </p>
            <div className="flex gap-3">
              <button
                onClick={() => setShowLogoutConfirm(false)}
                className="flex-1 py-3 border border-[#3a3a3a] rounded-xl text-gray-300 font-medium hover:bg-[#242424] transition"
              >
                취소
              </button>
              <button
                onClick={handleLogout}
                className="flex-1 py-3 bg-red-600 text-white rounded-xl font-medium hover:bg-red-500 transition"
              >
                로그아웃
              </button>
            </div>
          </div>
        </div>
      )}
    </div>
  );
}
