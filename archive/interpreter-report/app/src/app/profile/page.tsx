'use client';

import { useState, useEffect, useRef, useCallback } from 'react';
import Link from 'next/link';
import { useSession } from 'next-auth/react';
import { useRouter } from 'next/navigation';
import { ArrowLeft, Gift, Check, Loader2, Upload, X, Search, FileText, Phone, Plus, Trash2, ChevronDown, ChevronUp, Briefcase, Calendar, MapPin, Building2 } from 'lucide-react';
import { searchUniversities, VietnamUniversity } from '@/lib/vietnam-universities';

// 경력 항목 타입
interface CareerItem {
  id: string;
  period: string;        // 예: "2021.01~2021.10"
  description: string;   // 예: "대표 비서 / 통번역"
  organization: string;  // 예: "EQ LOGIS CO., LTD."
  location?: string;     // 예: "HCMC, D7"
}

interface ProfileForm {
  phone: string;
  zaloVerified: boolean;
  university: string;
  universityId: string;
  major: string;
  koreanCertificate: string;
  // 기존 단순 텍스트 -> 구조화된 경력으로 변경
  experience: string;              // 기존 호환용 (요약)
  fullTimeCareer: CareerItem[];    // 정규직 경력
  projectCareer: CareerItem[];     // 프로젝트/워크샵/세미나
  exhibitionCareer: CareerItem[];  // 전시회/현장 통역
  b2bCareer: CareerItem[];         // B2B 매칭
  otherCareer: CareerItem[];       // 기타 (법원, 구치소 등)
  region: string;
  resumeUrl: string;
}

const regions = ['호치민', '하노이', '다낭', '껀터', '냐짱', '빈즈엉', '기타'];
const certificates = ['TOPIK 3급', 'TOPIK 4급', 'TOPIK 5급', 'TOPIK 6급', '기타', '없음'];

export default function ProfilePage() {
  const { data: session, status } = useSession();
  const router = useRouter();
  const [form, setForm] = useState<ProfileForm>({
    phone: '',
    zaloVerified: false,
    university: '',
    universityId: '',
    major: '',
    koreanCertificate: '',
    experience: '',
    fullTimeCareer: [],
    projectCareer: [],
    exhibitionCareer: [],
    b2bCareer: [],
    otherCareer: [],
    region: '',
    resumeUrl: '',
  });

  // 경력 섹션 접기/펼치기
  const [expandedSections, setExpandedSections] = useState<Record<string, boolean>>({
    fullTime: true,
    project: true,
    exhibition: false,
    b2b: false,
    other: false,
  });

  // 경력 항목 추가
  const addCareerItem = (type: 'fullTimeCareer' | 'projectCareer' | 'exhibitionCareer' | 'b2bCareer' | 'otherCareer') => {
    const newItem: CareerItem = {
      id: crypto.randomUUID(),
      period: '',
      description: '',
      organization: '',
      location: '',
    };
    setForm(prev => ({
      ...prev,
      [type]: [...prev[type], newItem],
    }));
  };

  // 경력 항목 삭제
  const removeCareerItem = (type: 'fullTimeCareer' | 'projectCareer' | 'exhibitionCareer' | 'b2bCareer' | 'otherCareer', id: string) => {
    setForm(prev => ({
      ...prev,
      [type]: prev[type].filter(item => item.id !== id),
    }));
  };

  // 경력 항목 수정
  const updateCareerItem = (
    type: 'fullTimeCareer' | 'projectCareer' | 'exhibitionCareer' | 'b2bCareer' | 'otherCareer',
    id: string,
    field: keyof CareerItem,
    value: string
  ) => {
    setForm(prev => ({
      ...prev,
      [type]: prev[type].map(item =>
        item.id === id ? { ...item, [field]: value } : item
      ),
    }));
  };

  // 경력 통계 계산
  const careerStats = {
    totalItems: form.fullTimeCareer.length + form.projectCareer.length +
                form.exhibitionCareer.length + form.b2bCareer.length + form.otherCareer.length,
    fullTimeCount: form.fullTimeCareer.length,
    projectCount: form.projectCareer.length,
    exhibitionCount: form.exhibitionCareer.length,
    b2bCount: form.b2bCareer.length,
  };
  const [isSubmitting, setIsSubmitting] = useState(false);
  const [isLoading, setIsLoading] = useState(true);
  const [completed, setCompleted] = useState(false);
  const [error, setError] = useState<string | null>(null);

  // University autocomplete state
  const [universityQuery, setUniversityQuery] = useState('');
  const [universityResults, setUniversityResults] = useState<VietnamUniversity[]>([]);
  const [showUniversityDropdown, setShowUniversityDropdown] = useState(false);
  const universityInputRef = useRef<HTMLInputElement>(null);
  const universityDropdownRef = useRef<HTMLDivElement>(null);

  // Resume upload state
  const [resumeFile, setResumeFile] = useState<File | null>(null);
  const [isParsingResume, setIsParsingResume] = useState(false);
  const fileInputRef = useRef<HTMLInputElement>(null);

  // Redirect if not logged in
  useEffect(() => {
    if (status === 'unauthenticated') {
      router.push('/login');
    }
  }, [status, router]);

  // Fetch existing profile data
  useEffect(() => {
    const fetchProfile = async () => {
      if (!session?.user?.email) return;

      try {
        const res = await fetch('/api/user');
        if (res.ok) {
          const data = await res.json() as {
            user?: {
              profile_completed?: boolean;
              phone?: string;
              zalo_verified?: boolean;
              university?: string;
              university_id?: string;
              major?: string;
              korean_certificate?: string;
              experience?: string;
              region?: string;
              resume_url?: string;
            };
          };
          if (data.user?.profile_completed) {
            router.push('/dashboard');
            return;
          }
          const user = data.user;
          if (user) {
            setForm(prev => ({
              ...prev,
              phone: user.phone || '',
              zaloVerified: user.zalo_verified || false,
              university: user.university || '',
              universityId: user.university_id || '',
              major: user.major || '',
              koreanCertificate: user.korean_certificate || '',
              experience: user.experience || '',
              region: user.region || '',
              resumeUrl: user.resume_url || '',
            }));
            if (user.university) {
              setUniversityQuery(user.university);
            }
          }
        }
      } catch (err) {
        console.error('Failed to fetch profile:', err);
      } finally {
        setIsLoading(false);
      }
    };

    if (status === 'authenticated') {
      fetchProfile();
    }
  }, [session, status, router]);

  // University search
  const handleUniversitySearch = useCallback((query: string) => {
    setUniversityQuery(query);
    if (query.length >= 1) {
      const results = searchUniversities(query);
      setUniversityResults(results);
      setShowUniversityDropdown(true);
    } else {
      setUniversityResults([]);
      setShowUniversityDropdown(false);
    }
    // Clear selection if user is typing
    if (form.university !== query) {
      setForm(prev => ({ ...prev, university: '', universityId: '' }));
    }
  }, [form.university]);

  const selectUniversity = (uni: VietnamUniversity) => {
    const displayName = uni.nameKo || uni.nameEn;
    setUniversityQuery(displayName);
    setForm(prev => ({
      ...prev,
      university: displayName,
      universityId: uni.id,
    }));
    setShowUniversityDropdown(false);
  };

  // Click outside to close dropdown
  useEffect(() => {
    const handleClickOutside = (e: MouseEvent) => {
      if (
        universityDropdownRef.current &&
        !universityDropdownRef.current.contains(e.target as Node) &&
        universityInputRef.current &&
        !universityInputRef.current.contains(e.target as Node)
      ) {
        setShowUniversityDropdown(false);
      }
    };
    document.addEventListener('mousedown', handleClickOutside);
    return () => document.removeEventListener('mousedown', handleClickOutside);
  }, []);

  // Resume upload and parsing
  const handleResumeUpload = async (file: File) => {
    setResumeFile(file);
    setIsParsingResume(true);
    setError(null);

    try {
      const formData = new FormData();
      formData.append('resume', file);

      const res = await fetch('/api/parse-resume', {
        method: 'POST',
        body: formData,
      });

      if (res.ok) {
        interface ParsedCareerItem {
          company?: string;
          period?: string;
          description?: string;
        }
        interface ParsedData {
          parsed?: {
            phone?: string;
            major?: string;
            koreanCertificate?: string;
            university?: string;
            fullTimeCareer?: ParsedCareerItem[];
            projectCareer?: ParsedCareerItem[];
            exhibitionCareer?: ParsedCareerItem[];
            b2bCareer?: ParsedCareerItem[];
            otherCareer?: ParsedCareerItem[];
          };
          resumeUrl?: string;
        }

        // 파싱된 경력 데이터를 폼 형식으로 변환
        const convertCareer = (items?: ParsedCareerItem[]): CareerItem[] => {
          if (!items || items.length === 0) return [];
          return items.map(item => ({
            id: crypto.randomUUID(),
            period: item.period || '',
            description: item.description || '',
            organization: item.company || '',
            location: '',
          }));
        };

        const data = await res.json() as ParsedData;
        const parsed = data.parsed;
        // Auto-fill form with parsed data
        if (parsed) {
          const fullTimeCareer = convertCareer(parsed.fullTimeCareer);
          const projectCareer = convertCareer(parsed.projectCareer);
          const exhibitionCareer = convertCareer(parsed.exhibitionCareer);
          const b2bCareer = convertCareer(parsed.b2bCareer);
          const otherCareer = convertCareer(parsed.otherCareer);

          setForm(prev => ({
            ...prev,
            phone: parsed.phone || prev.phone,
            major: parsed.major || prev.major,
            koreanCertificate: parsed.koreanCertificate || prev.koreanCertificate,
            // 구조화된 경력 데이터 반영
            fullTimeCareer: fullTimeCareer.length > 0 ? fullTimeCareer : prev.fullTimeCareer,
            projectCareer: projectCareer.length > 0 ? projectCareer : prev.projectCareer,
            exhibitionCareer: exhibitionCareer.length > 0 ? exhibitionCareer : prev.exhibitionCareer,
            b2bCareer: b2bCareer.length > 0 ? b2bCareer : prev.b2bCareer,
            otherCareer: otherCareer.length > 0 ? otherCareer : prev.otherCareer,
          }));

          // 경력이 파싱되면 해당 섹션 펼치기
          const hasFullTime = fullTimeCareer.length > 0;
          const hasProject = projectCareer.length > 0;
          if (hasFullTime || hasProject) {
            setExpandedSections(prev => ({
              ...prev,
              fullTime: hasFullTime,
              project: hasProject,
              exhibition: exhibitionCareer.length > 0,
              b2b: b2bCareer.length > 0,
              other: otherCareer.length > 0,
            }));
          }

          // Handle university
          if (parsed.university) {
            const results = searchUniversities(parsed.university);
            if (results.length > 0) {
              selectUniversity(results[0]);
            } else {
              setUniversityQuery(parsed.university);
              setForm(prev => ({
                ...prev,
                university: parsed.university || '',
                universityId: '',
              }));
            }
          }
        }
        if (data.resumeUrl) {
          setForm(prev => ({ ...prev, resumeUrl: data.resumeUrl || '' }));
        }
      } else {
        const errorData = await res.json() as { error?: string };
        setError(errorData.error || '이력서 분석에 실패했습니다.');
      }
    } catch (err) {
      console.error('Resume parsing error:', err);
      setError('이력서 업로드 중 오류가 발생했습니다.');
    } finally {
      setIsParsingResume(false);
    }
  };

  // Format phone number with Vietnam country code
  const formatPhoneNumber = (value: string) => {
    // Remove all non-digits except +
    let cleaned = value.replace(/[^\d+]/g, '');

    // If starts with 0, assume Vietnam local number
    if (cleaned.startsWith('0')) {
      cleaned = '+84' + cleaned.substring(1);
    }
    // If doesn't start with +, add +84
    else if (!cleaned.startsWith('+')) {
      cleaned = '+84' + cleaned;
    }

    return cleaned;
  };

  const handlePhoneChange = (value: string) => {
    const formatted = formatPhoneNumber(value);
    setForm(prev => ({ ...prev, phone: formatted }));
  };

  // Check if form is complete
  // 기본 필드 + 경력 최소 1건 이상
  const requiredFields = ['phone', 'university', 'major', 'koreanCertificate', 'region'];
  const hasBasicFields = requiredFields.every(field =>
    (form[field as keyof ProfileForm] as string).trim() !== ''
  );
  const hasCareer = careerStats.totalItems > 0;
  const isFormComplete = hasBasicFields && hasCareer;

  // 경력 요약 텍스트 자동 생성 (저장 시 experience 필드에 반영)
  const generateExperienceSummary = () => {
    const parts: string[] = [];
    if (form.fullTimeCareer.length > 0) {
      parts.push(`정규직 ${form.fullTimeCareer.length}건`);
    }
    if (form.projectCareer.length > 0) {
      parts.push(`프로젝트/세미나 ${form.projectCareer.length}건`);
    }
    if (form.exhibitionCareer.length > 0) {
      parts.push(`전시회 ${form.exhibitionCareer.length}건`);
    }
    if (form.b2bCareer.length > 0) {
      parts.push(`B2B ${form.b2bCareer.length}건`);
    }
    if (form.otherCareer.length > 0) {
      parts.push(`기타 ${form.otherCareer.length}건`);
    }
    return parts.join(', ') || '경력 없음';
  };

  const handleSubmit = async (e: React.FormEvent) => {
    e.preventDefault();
    if (!isFormComplete) return;

    setIsSubmitting(true);
    setError(null);

    try {
      // 경력 데이터를 JSON으로 저장
      const careerData = {
        fullTime: form.fullTimeCareer,
        project: form.projectCareer,
        exhibition: form.exhibitionCareer,
        b2b: form.b2bCareer,
        other: form.otherCareer,
      };

      const res = await fetch('/api/profile', {
        method: 'POST',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify({
          ...form,
          universityId: form.universityId,
          experience: generateExperienceSummary(),
          careerData: JSON.stringify(careerData),
        }),
      });

      const data = await res.json() as { error?: string };

      if (!res.ok) {
        throw new Error(data.error || '프로필 저장에 실패했습니다.');
      }

      setCompleted(true);
    } catch (err) {
      setError(err instanceof Error ? err.message : '오류가 발생했습니다.');
    } finally {
      setIsSubmitting(false);
    }
  };

  if (status === 'loading' || isLoading) {
    return (
      <div className="min-h-screen bg-[#0f0f0f] flex items-center justify-center">
        <Loader2 className="w-8 h-8 animate-spin text-indigo-400" />
      </div>
    );
  }

  if (completed) {
    return (
      <div className="min-h-screen bg-[#0f0f0f] flex items-center justify-center px-6">
        <div className="bg-[#1a1a1a] border border-[#2a2a2a] rounded-2xl p-8 max-w-md w-full text-center">
          <div className="w-20 h-20 bg-green-900/50 rounded-full flex items-center justify-center mx-auto mb-6">
            <Check className="w-10 h-10 text-green-400" />
          </div>
          <h1 className="text-2xl font-bold text-gray-100 mb-2">
            프로필 완성!
          </h1>
          <p className="text-gray-400 mb-4">
            <span className="text-indigo-400 font-semibold">+20 크레딧</span>이 지급되었습니다.
          </p>
          <p className="text-sm text-gray-500 mb-6">
            이제 총 25회 사용 가능합니다.
          </p>
          <Link
            href="/dashboard"
            className="inline-block w-full bg-indigo-600 text-white py-3 rounded-xl font-medium hover:bg-indigo-500 transition"
          >
            대시보드로 이동
          </Link>
          <p className="text-xs text-gray-600 mt-4">
            Powered by Epicstage Corp.
          </p>
        </div>
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
          <div>
            <h1 className="text-lg font-semibold text-gray-100">프로필 완성</h1>
            <p className="text-xs text-gray-500">Epicstage Corp.</p>
          </div>
        </div>
      </header>

      <main className="max-w-2xl mx-auto px-6 py-6">
        {/* Reward Banner */}
        <div className="bg-gradient-to-r from-yellow-600 to-yellow-700 rounded-xl p-4 mb-6 flex items-center gap-4">
          <div className="w-12 h-12 bg-white/20 rounded-full flex items-center justify-center">
            <Gift className="w-6 h-6 text-white" />
          </div>
          <div className="text-white">
            <p className="font-semibold">프로필 완성 보너스</p>
            <p className="text-sm text-yellow-200">모든 항목 입력 시 +20 크레딧 지급!</p>
          </div>
        </div>

        {/* Resume Upload Section */}
        <div className="bg-[#1a1a1a] border border-[#2a2a2a] rounded-xl p-6 mb-6">
          <div className="flex items-center gap-3 mb-4">
            <FileText className="w-5 h-5 text-indigo-400" />
            <div>
              <h3 className="font-medium text-gray-200">이력서로 자동 입력 (선택)</h3>
              <p className="text-xs text-gray-500">PDF 또는 Word 파일을 업로드하면 자동으로 정보를 추출합니다</p>
            </div>
          </div>

          <input
            ref={fileInputRef}
            type="file"
            accept=".pdf,.doc,.docx"
            onChange={(e) => {
              const file = e.target.files?.[0];
              if (file) handleResumeUpload(file);
            }}
            className="hidden"
          />

          {resumeFile ? (
            <div className="flex items-center gap-3 p-3 bg-[#242424] rounded-lg">
              <FileText className="w-5 h-5 text-green-400" />
              <span className="flex-1 text-sm text-gray-300 truncate">{resumeFile.name}</span>
              {isParsingResume ? (
                <Loader2 className="w-5 h-5 animate-spin text-indigo-400" />
              ) : (
                <button
                  type="button"
                  onClick={() => {
                    setResumeFile(null);
                    if (fileInputRef.current) fileInputRef.current.value = '';
                  }}
                  className="text-gray-500 hover:text-gray-300"
                >
                  <X className="w-5 h-5" />
                </button>
              )}
            </div>
          ) : (
            <button
              type="button"
              onClick={() => fileInputRef.current?.click()}
              disabled={isParsingResume}
              className="w-full py-4 border-2 border-dashed border-[#3a3a3a] rounded-xl text-gray-400 hover:border-indigo-500 hover:text-indigo-400 transition flex items-center justify-center gap-2"
            >
              <Upload className="w-5 h-5" />
              이력서 업로드하기
            </button>
          )}
        </div>

        <form onSubmit={handleSubmit} className="bg-[#1a1a1a] border border-[#2a2a2a] rounded-xl p-6 space-y-6">
          {/* Phone with Vietnam country code */}
          <div>
            <label className="block text-sm font-medium text-gray-300 mb-2">
              <Phone className="w-4 h-4 inline-block mr-1" />
              연락처 (Zalo/WhatsApp) *
            </label>
            <div className="relative">
              <div className="absolute left-4 top-1/2 -translate-y-1/2 flex items-center gap-1 text-gray-400">
                <span className="text-lg">🇻🇳</span>
              </div>
              <input
                type="tel"
                value={form.phone}
                onChange={e => handlePhoneChange(e.target.value)}
                placeholder="+84 912 345 678"
                className="w-full pl-12 pr-4 py-3 bg-[#242424] border border-[#3a3a3a] rounded-xl text-gray-200 placeholder-gray-500 focus:ring-2 focus:ring-indigo-500 focus:border-transparent"
              />
            </div>
            <p className="text-xs text-gray-500 mt-1">
              베트남 휴대폰 번호를 입력하세요 (예: 0912345678 또는 +84912345678)
            </p>
          </div>

          {/* University with autocomplete */}
          <div className="relative">
            <label className="block text-sm font-medium text-gray-300 mb-2">
              대학교 *
            </label>
            <div className="relative">
              <Search className="absolute left-4 top-1/2 -translate-y-1/2 w-4 h-4 text-gray-500" />
              <input
                ref={universityInputRef}
                type="text"
                value={universityQuery}
                onChange={e => handleUniversitySearch(e.target.value)}
                onFocus={() => {
                  if (universityQuery.length >= 1) {
                    setShowUniversityDropdown(true);
                  }
                }}
                placeholder="대학명 검색 (한글/영어/베트남어)"
                className="w-full pl-10 pr-4 py-3 bg-[#242424] border border-[#3a3a3a] rounded-xl text-gray-200 placeholder-gray-500 focus:ring-2 focus:ring-indigo-500 focus:border-transparent"
              />
              {form.university && (
                <Check className="absolute right-4 top-1/2 -translate-y-1/2 w-4 h-4 text-green-400" />
              )}
            </div>

            {/* Dropdown */}
            {showUniversityDropdown && universityResults.length > 0 && (
              <div
                ref={universityDropdownRef}
                className="absolute z-50 w-full mt-1 bg-[#242424] border border-[#3a3a3a] rounded-xl shadow-lg max-h-60 overflow-y-auto"
              >
                {universityResults.map((uni) => (
                  <button
                    key={uni.id}
                    type="button"
                    onClick={() => selectUniversity(uni)}
                    className="w-full px-4 py-3 text-left hover:bg-[#2a2a2a] border-b border-[#3a3a3a] last:border-b-0"
                  >
                    <div className="text-gray-200 font-medium">
                      {uni.nameKo || uni.nameEn}
                    </div>
                    <div className="text-xs text-gray-500 flex gap-2 mt-1">
                      <span>{uni.nameVi}</span>
                      {uni.abbreviation && <span>({uni.abbreviation})</span>}
                      <span>• {uni.city}</span>
                    </div>
                  </button>
                ))}
              </div>
            )}

            {showUniversityDropdown && universityQuery.length >= 1 && universityResults.length === 0 && (
              <div className="absolute z-50 w-full mt-1 bg-[#242424] border border-[#3a3a3a] rounded-xl p-4 text-gray-500 text-sm">
                검색 결과가 없습니다. 직접 입력해주세요.
              </div>
            )}
          </div>

          {/* Major */}
          <div>
            <label className="block text-sm font-medium text-gray-300 mb-2">
              전공 *
            </label>
            <input
              type="text"
              value={form.major}
              onChange={e => setForm(prev => ({ ...prev, major: e.target.value }))}
              placeholder="예: 한국학과, Khoa Hàn Quốc học"
              className="w-full px-4 py-3 bg-[#242424] border border-[#3a3a3a] rounded-xl text-gray-200 placeholder-gray-500 focus:ring-2 focus:ring-indigo-500 focus:border-transparent"
            />
          </div>

          {/* Korean Certificate */}
          <div>
            <label className="block text-sm font-medium text-gray-300 mb-2">
              한국어 자격증 *
            </label>
            <select
              value={form.koreanCertificate}
              onChange={e => setForm(prev => ({ ...prev, koreanCertificate: e.target.value }))}
              className="w-full px-4 py-3 bg-[#242424] border border-[#3a3a3a] rounded-xl text-gray-200 focus:ring-2 focus:ring-indigo-500 focus:border-transparent"
            >
              <option value="" className="bg-[#242424]">선택하세요</option>
              {certificates.map(cert => (
                <option key={cert} value={cert} className="bg-[#242424]">{cert}</option>
              ))}
            </select>
          </div>

          {/* Career Stats Banner */}
          {careerStats.totalItems > 0 && (
            <div className="bg-gradient-to-r from-indigo-900/30 to-purple-900/30 border border-indigo-800/50 rounded-xl p-4">
              <div className="flex items-center gap-2 mb-2">
                <Briefcase className="w-5 h-5 text-indigo-400" />
                <span className="font-medium text-gray-200">경력 현황</span>
              </div>
              <div className="grid grid-cols-4 gap-2 text-center">
                <div className="bg-[#1a1a1a] rounded-lg p-2">
                  <div className="text-xl font-bold text-indigo-400">{careerStats.fullTimeCount}</div>
                  <div className="text-xs text-gray-500">정규직</div>
                </div>
                <div className="bg-[#1a1a1a] rounded-lg p-2">
                  <div className="text-xl font-bold text-green-400">{careerStats.projectCount}</div>
                  <div className="text-xs text-gray-500">프로젝트</div>
                </div>
                <div className="bg-[#1a1a1a] rounded-lg p-2">
                  <div className="text-xl font-bold text-yellow-400">{careerStats.exhibitionCount}</div>
                  <div className="text-xs text-gray-500">전시회</div>
                </div>
                <div className="bg-[#1a1a1a] rounded-lg p-2">
                  <div className="text-xl font-bold text-blue-400">{careerStats.b2bCount}</div>
                  <div className="text-xs text-gray-500">B2B</div>
                </div>
              </div>
            </div>
          )}

          {/* 1. Full-time Career */}
          <CareerSection
            title="정규직 경력"
            subtitle="회사에서 근무한 경력"
            icon={<Building2 className="w-5 h-5" />}
            color="indigo"
            items={form.fullTimeCareer}
            type="fullTimeCareer"
            isExpanded={expandedSections.fullTime}
            onToggle={() => setExpandedSections(prev => ({ ...prev, fullTime: !prev.fullTime }))}
            onAdd={() => addCareerItem('fullTimeCareer')}
            onRemove={(id) => removeCareerItem('fullTimeCareer', id)}
            onUpdate={(id, field, value) => updateCareerItem('fullTimeCareer', id, field, value)}
            showLocation={false}
          />

          {/* 2. Project/Workshop/Seminar */}
          <CareerSection
            title="프로젝트 / 워크샵 / 세미나"
            subtitle="프리랜서 통역 프로젝트"
            icon={<Calendar className="w-5 h-5" />}
            color="green"
            items={form.projectCareer}
            type="projectCareer"
            isExpanded={expandedSections.project}
            onToggle={() => setExpandedSections(prev => ({ ...prev, project: !prev.project }))}
            onAdd={() => addCareerItem('projectCareer')}
            onRemove={(id) => removeCareerItem('projectCareer', id)}
            onUpdate={(id, field, value) => updateCareerItem('projectCareer', id, field, value)}
            showLocation={true}
          />

          {/* 3. Exhibition/Field */}
          <CareerSection
            title="전시회 / 현장 통역"
            subtitle="전시회, 박람회 등 현장 통역"
            icon={<MapPin className="w-5 h-5" />}
            color="yellow"
            items={form.exhibitionCareer}
            type="exhibitionCareer"
            isExpanded={expandedSections.exhibition}
            onToggle={() => setExpandedSections(prev => ({ ...prev, exhibition: !prev.exhibition }))}
            onAdd={() => addCareerItem('exhibitionCareer')}
            onRemove={(id) => removeCareerItem('exhibitionCareer', id)}
            onUpdate={(id, field, value) => updateCareerItem('exhibitionCareer', id, field, value)}
            showLocation={true}
          />

          {/* 4. B2B Matching */}
          <CareerSection
            title="B2B 매칭 / 바이어 상담"
            subtitle="수출상담회, 비즈니스 미팅"
            icon={<Briefcase className="w-5 h-5" />}
            color="blue"
            items={form.b2bCareer}
            type="b2bCareer"
            isExpanded={expandedSections.b2b}
            onToggle={() => setExpandedSections(prev => ({ ...prev, b2b: !prev.b2b }))}
            onAdd={() => addCareerItem('b2bCareer')}
            onRemove={(id) => removeCareerItem('b2bCareer', id)}
            onUpdate={(id, field, value) => updateCareerItem('b2bCareer', id, field, value)}
            showLocation={true}
          />

          {/* 5. Other */}
          <CareerSection
            title="기타 경력"
            subtitle="법원, 수사통역, 교육 등"
            icon={<FileText className="w-5 h-5" />}
            color="gray"
            items={form.otherCareer}
            type="otherCareer"
            isExpanded={expandedSections.other}
            onToggle={() => setExpandedSections(prev => ({ ...prev, other: !prev.other }))}
            onAdd={() => addCareerItem('otherCareer')}
            onRemove={(id) => removeCareerItem('otherCareer', id)}
            onUpdate={(id, field, value) => updateCareerItem('otherCareer', id, field, value)}
            showLocation={true}
          />

          {/* Legacy Experience Summary (hidden but kept for compatibility) */}
          <input
            type="hidden"
            value={form.experience}
            onChange={e => setForm(prev => ({ ...prev, experience: e.target.value }))}
          />

          {/* Region */}
          <div>
            <label className="block text-sm font-medium text-gray-300 mb-2">
              활동 지역 *
            </label>
            <div className="flex flex-wrap gap-2">
              {regions.map(region => (
                <button
                  key={region}
                  type="button"
                  onClick={() => setForm(prev => ({ ...prev, region }))}
                  className={`px-4 py-2 rounded-lg border-2 transition ${
                    form.region === region
                      ? 'border-indigo-500 bg-indigo-900/30 text-indigo-400'
                      : 'border-[#3a3a3a] text-gray-400 hover:border-[#4a4a4a]'
                  }`}
                >
                  {region}
                </button>
              ))}
            </div>
          </div>

          {/* Error Message */}
          {error && (
            <div className="bg-red-900/30 border border-red-800/50 rounded-xl p-4 text-red-400 text-sm">
              {error}
            </div>
          )}

          {/* Submit Button */}
          <button
            type="submit"
            disabled={!isFormComplete || isSubmitting}
            className={`w-full py-3 rounded-xl font-medium transition flex items-center justify-center gap-2 ${
              isFormComplete
                ? 'bg-indigo-600 text-white hover:bg-indigo-500'
                : 'bg-[#2a2a2a] text-gray-600 cursor-not-allowed'
            }`}
          >
            {isSubmitting ? (
              <>
                <span className="w-5 h-5 border-2 border-white border-t-transparent rounded-full animate-spin" />
                저장 중...
              </>
            ) : (
              <>
                완성하고 +20 크레딧 받기
              </>
            )}
          </button>
        </form>

        {/* Footer */}
        <p className="text-center text-xs text-gray-600 mt-6">
          © 2025 Epicstage Corp. All rights reserved.
        </p>
      </main>
    </div>
  );
}

// 경력 섹션 컴포넌트
interface CareerSectionProps {
  title: string;
  subtitle: string;
  icon: React.ReactNode;
  color: 'indigo' | 'green' | 'yellow' | 'blue' | 'gray';
  items: CareerItem[];
  type: 'fullTimeCareer' | 'projectCareer' | 'exhibitionCareer' | 'b2bCareer' | 'otherCareer';
  isExpanded: boolean;
  onToggle: () => void;
  onAdd: () => void;
  onRemove: (id: string) => void;
  onUpdate: (id: string, field: keyof CareerItem, value: string) => void;
  showLocation: boolean;
}

function CareerSection({
  title,
  subtitle,
  icon,
  color,
  items,
  isExpanded,
  onToggle,
  onAdd,
  onRemove,
  onUpdate,
  showLocation,
}: CareerSectionProps) {
  const colorClasses = {
    indigo: 'text-indigo-400 bg-indigo-900/30 border-indigo-800/50',
    green: 'text-green-400 bg-green-900/30 border-green-800/50',
    yellow: 'text-yellow-400 bg-yellow-900/30 border-yellow-800/50',
    blue: 'text-blue-400 bg-blue-900/30 border-blue-800/50',
    gray: 'text-gray-400 bg-gray-800/30 border-gray-700/50',
  };

  const iconColorClass = {
    indigo: 'text-indigo-400',
    green: 'text-green-400',
    yellow: 'text-yellow-400',
    blue: 'text-blue-400',
    gray: 'text-gray-400',
  };

  return (
    <div className={`border rounded-xl overflow-hidden ${colorClasses[color].split(' ').slice(1).join(' ')}`}>
      {/* Header */}
      <button
        type="button"
        onClick={onToggle}
        className="w-full px-4 py-3 flex items-center justify-between bg-[#1a1a1a] hover:bg-[#222]"
      >
        <div className="flex items-center gap-3">
          <div className={iconColorClass[color]}>{icon}</div>
          <div className="text-left">
            <div className="font-medium text-gray-200 flex items-center gap-2">
              {title}
              {items.length > 0 && (
                <span className={`text-xs px-2 py-0.5 rounded-full ${colorClasses[color]}`}>
                  {items.length}건
                </span>
              )}
            </div>
            <div className="text-xs text-gray-500">{subtitle}</div>
          </div>
        </div>
        {isExpanded ? (
          <ChevronUp className="w-5 h-5 text-gray-500" />
        ) : (
          <ChevronDown className="w-5 h-5 text-gray-500" />
        )}
      </button>

      {/* Content */}
      {isExpanded && (
        <div className="p-4 space-y-4 bg-[#141414]">
          {items.map((item, index) => (
            <div key={item.id} className="bg-[#1a1a1a] rounded-lg p-4 border border-[#2a2a2a]">
              <div className="flex items-center justify-between mb-3">
                <span className="text-xs text-gray-500">#{index + 1}</span>
                <button
                  type="button"
                  onClick={() => onRemove(item.id)}
                  className="text-red-400 hover:text-red-300 p-1"
                >
                  <Trash2 className="w-4 h-4" />
                </button>
              </div>

              <div className="grid gap-3">
                {/* Period */}
                <div>
                  <label className="block text-xs text-gray-500 mb-1">기간</label>
                  <input
                    type="text"
                    value={item.period}
                    onChange={e => onUpdate(item.id, 'period', e.target.value)}
                    placeholder="예: 2024.01~2024.06"
                    className="w-full px-3 py-2 bg-[#242424] border border-[#3a3a3a] rounded-lg text-sm text-gray-200 placeholder-gray-500 focus:ring-1 focus:ring-indigo-500 focus:border-transparent"
                  />
                </div>

                {/* Description */}
                <div>
                  <label className="block text-xs text-gray-500 mb-1">업무 내용</label>
                  <input
                    type="text"
                    value={item.description}
                    onChange={e => onUpdate(item.id, 'description', e.target.value)}
                    placeholder="예: K-Beauty Expo 통역, 대표비서/통번역"
                    className="w-full px-3 py-2 bg-[#242424] border border-[#3a3a3a] rounded-lg text-sm text-gray-200 placeholder-gray-500 focus:ring-1 focus:ring-indigo-500 focus:border-transparent"
                  />
                </div>

                {/* Organization */}
                <div>
                  <label className="block text-xs text-gray-500 mb-1">기관/회사</label>
                  <input
                    type="text"
                    value={item.organization}
                    onChange={e => onUpdate(item.id, 'organization', e.target.value)}
                    placeholder="예: SECC전시회, KOTRA, 삼성전자"
                    className="w-full px-3 py-2 bg-[#242424] border border-[#3a3a3a] rounded-lg text-sm text-gray-200 placeholder-gray-500 focus:ring-1 focus:ring-indigo-500 focus:border-transparent"
                  />
                </div>

                {/* Location (optional) */}
                {showLocation && (
                  <div>
                    <label className="block text-xs text-gray-500 mb-1">장소 (선택)</label>
                    <input
                      type="text"
                      value={item.location || ''}
                      onChange={e => onUpdate(item.id, 'location', e.target.value)}
                      placeholder="예: HCMC D7, Lotte Hotel"
                      className="w-full px-3 py-2 bg-[#242424] border border-[#3a3a3a] rounded-lg text-sm text-gray-200 placeholder-gray-500 focus:ring-1 focus:ring-indigo-500 focus:border-transparent"
                    />
                  </div>
                )}
              </div>
            </div>
          ))}

          {/* Add Button */}
          <button
            type="button"
            onClick={onAdd}
            className={`w-full py-3 border-2 border-dashed rounded-lg flex items-center justify-center gap-2 text-sm transition hover:bg-[#1a1a1a] ${
              color === 'indigo' ? 'border-indigo-800/50 text-indigo-400' :
              color === 'green' ? 'border-green-800/50 text-green-400' :
              color === 'yellow' ? 'border-yellow-800/50 text-yellow-400' :
              color === 'blue' ? 'border-blue-800/50 text-blue-400' :
              'border-gray-700/50 text-gray-400'
            }`}
          >
            <Plus className="w-4 h-4" />
            경력 추가
          </button>
        </div>
      )}
    </div>
  );
}
