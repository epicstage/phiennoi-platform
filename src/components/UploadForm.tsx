"use client";

import { useState, useRef, useMemo } from "react";
import { domains } from "@/data/pseo-dimensions";
import { vietnamUniversities, searchUniversities } from "@/lib/vietnam-universities";
import { koreanUniversities, searchKoreanUniversities } from "@/lib/korean-universities";

type FormStatus = "idle" | "parsing" | "parsed" | "submitting" | "success" | "error";

interface ParsedResume {
  name: string;
  phoneVietnam: string;
  phoneKorea: string;
  email: string;
  universityVietnam: string;
  universityKorea: string;
  major: string;
  koreanLevel: string;
  location: string;
  domains: string[];
  companyExperience: Array<{
    period: string;
    company: string;
    position: string;
    description: string;
  }>;
  eventExperience: Array<{
    period: string;
    eventName: string;
    client: string;
    type: string;
    location: string;
  }>;
  summary: string;
}

const eventTypeLabels: Record<string, string> = {
  exhibition: "전시회",
  b2b: "B2B",
  seminar: "세미나",
  project: "프로젝트",
  legal: "법률",
  other: "기타",
};

export default function UploadForm() {
  const [file, setFile] = useState<File | null>(null);
  const [status, setStatus] = useState<FormStatus>("idle");
  const [errorMessage, setErrorMessage] = useState("");
  const [parsed, setParsed] = useState<ParsedResume | null>(null);
  const [formData, setFormData] = useState<ParsedResume>({
    name: "",
    phoneVietnam: "",
    phoneKorea: "",
    email: "",
    universityVietnam: "",
    universityKorea: "",
    major: "",
    koreanLevel: "",
    location: "",
    domains: [],
    companyExperience: [],
    eventExperience: [],
    summary: "",
  });
  const fileInputRef = useRef<HTMLInputElement>(null);

  // 대학 자동완성 상태
  const [vnUniQuery, setVnUniQuery] = useState("");
  const [krUniQuery, setKrUniQuery] = useState("");
  const [showVnSuggestions, setShowVnSuggestions] = useState(false);
  const [showKrSuggestions, setShowKrSuggestions] = useState(false);

  const vnSuggestions = useMemo(
    () => (vnUniQuery.length >= 2 ? searchUniversities(vnUniQuery) : []),
    [vnUniQuery]
  );
  const krSuggestions = useMemo(
    () => (krUniQuery.length >= 2 ? searchKoreanUniversities(krUniQuery) : []),
    [krUniQuery]
  );

  const handleFileChange = async (e: React.ChangeEvent<HTMLInputElement>) => {
    const selected = e.target.files?.[0];
    if (!selected) return;

    if (selected.size > 10 * 1024 * 1024) {
      setErrorMessage("파일 크기는 10MB 이하여야 합니다.");
      return;
    }

    const allowedTypes = [
      "application/pdf",
      "application/msword",
      "application/vnd.openxmlformats-officedocument.wordprocessingml.document",
    ];
    if (!allowedTypes.includes(selected.type)) {
      setErrorMessage("PDF, DOC, DOCX 파일만 업로드 가능합니다.");
      return;
    }

    setFile(selected);
    setErrorMessage("");
    setStatus("parsing");

    const fd = new FormData();
    fd.set("resume", selected);

    try {
      const res = await fetch("/api/parse-resume", {
        method: "POST",
        body: fd,
      });

      const data = await res.json();

      if (!res.ok) {
        throw new Error(data.error || "파싱에 실패했습니다.");
      }

      setParsed(data.parsed);
      setFormData(data.parsed);
      setVnUniQuery(data.parsed.universityVietnam || "");
      setKrUniQuery(data.parsed.universityKorea || "");
      setStatus("parsed");
    } catch (err) {
      setStatus("idle");
      setErrorMessage(
        err instanceof Error ? err.message : "파싱 중 오류가 발생했습니다."
      );
    }
  };

  const handleInputChange = (field: keyof ParsedResume, value: string | string[]) => {
    setFormData((prev) => ({ ...prev, [field]: value }));
  };

  const toggleDomain = (slug: string) => {
    setFormData((prev) => ({
      ...prev,
      domains: prev.domains.includes(slug)
        ? prev.domains.filter((d) => d !== slug)
        : [...prev.domains, slug],
    }));
  };

  const handleSubmit = async () => {
    if (!formData.name || !formData.email || (!formData.phoneVietnam && !formData.phoneKorea)) {
      setErrorMessage("이름, 이메일, 연락처(베트남 또는 한국) 중 하나는 필수입니다.");
      return;
    }

    setStatus("submitting");
    setErrorMessage("");

    const fd = new FormData();
    fd.set("name", formData.name);
    fd.set("email", formData.email);
    fd.set("phoneVietnam", formData.phoneVietnam);
    fd.set("phoneKorea", formData.phoneKorea);
    fd.set("location", formData.location);
    fd.set("universityVietnam", formData.universityVietnam);
    fd.set("universityKorea", formData.universityKorea);
    fd.set("major", formData.major);
    fd.set("koreanLevel", formData.koreanLevel);
    fd.set("summary", formData.summary);
    fd.set("companyExperience", JSON.stringify(formData.companyExperience));
    fd.set("eventExperience", JSON.stringify(formData.eventExperience));
    formData.domains.forEach((d) => fd.append("domains", d));
    if (file) fd.set("resume", file);

    try {
      const res = await fetch("/api/upload", {
        method: "POST",
        body: fd,
      });

      const data = await res.json();

      if (!res.ok) {
        throw new Error(data.error || "등록에 실패했습니다.");
      }

      setStatus("success");
    } catch (err) {
      setStatus("error");
      setErrorMessage(
        err instanceof Error ? err.message : "등록 중 오류가 발생했습니다."
      );
    }
  };

  if (status === "success") {
    return (
      <div className="max-w-2xl mx-auto px-6 py-16">
        <div className="bg-background-card border border-green-success/30 rounded-lg p-12 text-center">
          <svg className="w-16 h-16 mx-auto mb-6 text-green-success" fill="currentColor" viewBox="0 0 20 20">
            <path fillRule="evenodd" d="M16.707 5.293a1 1 0 010 1.414l-8 8a1 1 0 01-1.414 0l-4-4a1 1 0 011.414-1.414L8 12.586l7.293-7.293a1 1 0 011.414 0z" clipRule="evenodd" />
          </svg>
          <h2 className="text-2xl font-bold text-foreground mb-3">등록 완료!</h2>
          <p className="text-foreground-secondary mb-6">이력서가 성공적으로 등록되었습니다.</p>
          <a href="/" className="inline-block px-6 py-3 bg-red-primary text-white font-semibold rounded-lg hover:bg-red-hover transition">홈으로</a>
        </div>
      </div>
    );
  }

  return (
    <div className="max-w-2xl mx-auto px-6 py-12">
      {/* 파일 업로드 */}
      <div className="bg-background-card border border-border-default rounded-lg p-8 mb-6">
        <h2 className="text-xl font-bold text-foreground mb-4">1. 이력서 업로드</h2>

        <input
          ref={fileInputRef}
          type="file"
          accept=".pdf,.doc,.docx"
          onChange={handleFileChange}
          className="hidden"
        />

        <div
          onClick={() => fileInputRef.current?.click()}
          className={`border-2 border-dashed rounded-lg p-8 text-center transition cursor-pointer ${
            file
              ? "border-green-success/50 bg-green-success/5"
              : "border-border-default hover:border-red-primary/50 bg-background-surface"
          }`}
        >
          {status === "parsing" ? (
            <>
              <div className="w-10 h-10 mx-auto mb-4 border-4 border-red-primary border-t-transparent rounded-full animate-spin" />
              <p className="text-foreground font-medium">이력서 분석 중...</p>
            </>
          ) : file ? (
            <>
              <svg className="w-10 h-10 mx-auto mb-3 text-green-success" fill="currentColor" viewBox="0 0 20 20">
                <path fillRule="evenodd" d="M16.707 5.293a1 1 0 010 1.414l-8 8a1 1 0 01-1.414 0l-4-4a1 1 0 011.414-1.414L8 12.586l7.293-7.293a1 1 0 011.414 0z" clipRule="evenodd" />
              </svg>
              <p className="text-foreground font-medium mb-1">{file.name}</p>
              <p className="text-sm text-foreground-muted">{(file.size / 1024 / 1024).toFixed(1)}MB · 클릭하여 변경</p>
            </>
          ) : (
            <>
              <svg className="w-10 h-10 mx-auto mb-3 text-foreground-muted" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                <path strokeLinecap="round" strokeLinejoin="round" strokeWidth={1.5} d="M7 16a4 4 0 01-.88-7.903A5 5 0 1115.9 6L16 6a5 5 0 011 9.9M15 13l-3-3m0 0l-3 3m3-3v12" />
              </svg>
              <p className="text-foreground font-medium mb-1">이력서 파일 선택</p>
              <p className="text-sm text-foreground-muted">PDF, DOC, DOCX (최대 10MB)</p>
            </>
          )}
        </div>
      </div>

      {/* 파싱 결과 + 수정 폼 */}
      {status === "parsed" && parsed && (
        <>
          {/* 요약 */}
          {parsed.summary && (
            <div className="bg-background-card border border-border-default rounded-lg p-6 mb-6">
              <h3 className="text-lg font-bold text-foreground mb-2">📋 경력 요약</h3>
              <p className="text-foreground-secondary">{parsed.summary}</p>
            </div>
          )}

          {/* 기본 정보 */}
          <div className="bg-background-card border border-border-default rounded-lg p-8 mb-6">
            <h2 className="text-xl font-bold text-foreground mb-4">2. 기본 정보</h2>
            <p className="text-sm text-foreground-muted mb-6">파싱된 정보를 확인하고 수정하세요. *는 필수 항목입니다.</p>

            <div className="grid md:grid-cols-2 gap-4">
              <div>
                <label className="block text-sm font-medium text-foreground-secondary mb-1">이름 *</label>
                <input
                  type="text"
                  value={formData.name}
                  onChange={(e) => handleInputChange("name", e.target.value)}
                  className="w-full px-4 py-3 bg-background-surface border border-border-default rounded-lg text-foreground focus:ring-2 focus:ring-red-primary outline-none"
                  placeholder="LE NGOC HUONG NHU"
                />
              </div>
              <div>
                <label className="block text-sm font-medium text-foreground-secondary mb-1">이메일 *</label>
                <input
                  type="email"
                  value={formData.email}
                  onChange={(e) => handleInputChange("email", e.target.value)}
                  className="w-full px-4 py-3 bg-background-surface border border-border-default rounded-lg text-foreground focus:ring-2 focus:ring-red-primary outline-none"
                  placeholder="example@email.com"
                />
              </div>

              {/* 베트남 전화번호 */}
              <div>
                <label className="block text-sm font-medium text-foreground-secondary mb-1">🇻🇳 베트남 전화번호</label>
                <input
                  type="tel"
                  value={formData.phoneVietnam}
                  onChange={(e) => handleInputChange("phoneVietnam", e.target.value)}
                  className="w-full px-4 py-3 bg-background-surface border border-border-default rounded-lg text-foreground focus:ring-2 focus:ring-red-primary outline-none"
                  placeholder="090 xxx xxxx"
                />
              </div>

              {/* 한국 전화번호 */}
              <div>
                <label className="block text-sm font-medium text-foreground-secondary mb-1">🇰🇷 한국 전화번호</label>
                <input
                  type="tel"
                  value={formData.phoneKorea}
                  onChange={(e) => handleInputChange("phoneKorea", e.target.value)}
                  className="w-full px-4 py-3 bg-background-surface border border-border-default rounded-lg text-foreground focus:ring-2 focus:ring-red-primary outline-none"
                  placeholder="010-xxxx-xxxx"
                />
              </div>

              <div>
                <label className="block text-sm font-medium text-foreground-secondary mb-1">활동 지역</label>
                <select
                  value={formData.location}
                  onChange={(e) => handleInputChange("location", e.target.value)}
                  className="w-full px-4 py-3 bg-background-surface border border-border-default rounded-lg text-foreground focus:ring-2 focus:ring-red-primary outline-none"
                >
                  <option value="">선택하세요</option>
                  <option value="호치민">호치민 (HCMC)</option>
                  <option value="하노이">하노이 (Hanoi)</option>
                  <option value="다낭">다낭 (Da Nang)</option>
                  <option value="기타">기타</option>
                </select>
              </div>

              <div>
                <label className="block text-sm font-medium text-foreground-secondary mb-1">한국어 수준</label>
                <input
                  type="text"
                  value={formData.koreanLevel}
                  onChange={(e) => handleInputChange("koreanLevel", e.target.value)}
                  className="w-full px-4 py-3 bg-background-surface border border-border-default rounded-lg text-foreground focus:ring-2 focus:ring-red-primary outline-none"
                  placeholder="TOPIK 6급"
                />
              </div>
            </div>

            {/* 학력 섹션 */}
            <div className="mt-6 pt-6 border-t border-border-default">
              <h3 className="text-lg font-bold text-foreground mb-4">🎓 학력</h3>
              <div className="grid md:grid-cols-2 gap-4">
                {/* 베트남 대학 */}
                <div className="relative">
                  <label className="block text-sm font-medium text-foreground-secondary mb-1">🇻🇳 베트남 대학교</label>
                  <input
                    type="text"
                    value={vnUniQuery}
                    onChange={(e) => {
                      setVnUniQuery(e.target.value);
                      setShowVnSuggestions(true);
                      handleInputChange("universityVietnam", e.target.value);
                    }}
                    onFocus={() => setShowVnSuggestions(true)}
                    onBlur={() => setTimeout(() => setShowVnSuggestions(false), 200)}
                    className="w-full px-4 py-3 bg-background-surface border border-border-default rounded-lg text-foreground focus:ring-2 focus:ring-red-primary outline-none"
                    placeholder="대학교명 검색..."
                  />
                  {showVnSuggestions && vnSuggestions.length > 0 && (
                    <div className="absolute z-10 w-full mt-1 bg-background-card border border-border-default rounded-lg shadow-lg max-h-48 overflow-y-auto">
                      {vnSuggestions.map((uni) => (
                        <button
                          key={uni.id}
                          type="button"
                          className="w-full px-4 py-2 text-left hover:bg-background-surface text-sm"
                          onClick={() => {
                            setVnUniQuery(uni.nameVi);
                            handleInputChange("universityVietnam", uni.nameVi);
                            setShowVnSuggestions(false);
                          }}
                        >
                          <span className="text-foreground">{uni.nameVi}</span>
                          {uni.nameKo && <span className="text-foreground-muted ml-2">({uni.nameKo})</span>}
                        </button>
                      ))}
                    </div>
                  )}
                </div>

                {/* 한국 대학 */}
                <div className="relative">
                  <label className="block text-sm font-medium text-foreground-secondary mb-1">🇰🇷 한국 대학교</label>
                  <input
                    type="text"
                    value={krUniQuery}
                    onChange={(e) => {
                      setKrUniQuery(e.target.value);
                      setShowKrSuggestions(true);
                      handleInputChange("universityKorea", e.target.value);
                    }}
                    onFocus={() => setShowKrSuggestions(true)}
                    onBlur={() => setTimeout(() => setShowKrSuggestions(false), 200)}
                    className="w-full px-4 py-3 bg-background-surface border border-border-default rounded-lg text-foreground focus:ring-2 focus:ring-red-primary outline-none"
                    placeholder="대학교명 검색..."
                  />
                  {showKrSuggestions && krSuggestions.length > 0 && (
                    <div className="absolute z-10 w-full mt-1 bg-background-card border border-border-default rounded-lg shadow-lg max-h-48 overflow-y-auto">
                      {krSuggestions.map((uni) => (
                        <button
                          key={uni.id}
                          type="button"
                          className="w-full px-4 py-2 text-left hover:bg-background-surface text-sm"
                          onClick={() => {
                            setKrUniQuery(uni.nameKo);
                            handleInputChange("universityKorea", uni.nameKo);
                            setShowKrSuggestions(false);
                          }}
                        >
                          <span className="text-foreground">{uni.nameKo}</span>
                          <span className="text-foreground-muted ml-2">({uni.city})</span>
                        </button>
                      ))}
                    </div>
                  )}
                </div>

                <div className="md:col-span-2">
                  <label className="block text-sm font-medium text-foreground-secondary mb-1">전공</label>
                  <input
                    type="text"
                    value={formData.major}
                    onChange={(e) => handleInputChange("major", e.target.value)}
                    className="w-full px-4 py-3 bg-background-surface border border-border-default rounded-lg text-foreground focus:ring-2 focus:ring-red-primary outline-none"
                    placeholder="한국어학과 / 한국어 통번역"
                  />
                </div>
              </div>
            </div>
          </div>

          {/* 전문 분야 - AI가 미리 선택 */}
          <div className="bg-background-card border border-border-default rounded-lg p-8 mb-6">
            <h2 className="text-xl font-bold text-foreground mb-2">3. 전문 분야</h2>
            <p className="text-sm text-foreground-muted mb-4">
              {formData.domains.length > 0
                ? `AI가 이력서 기반으로 ${formData.domains.length}개 분야를 선택했습니다. 수정 가능합니다.`
                : "경험 있는 분야를 선택하세요 (복수 선택 가능)"
              }
            </p>

            <div className="grid grid-cols-2 md:grid-cols-4 gap-2">
              {domains.map((domain) => (
                <button
                  key={domain.slug}
                  type="button"
                  onClick={() => toggleDomain(domain.slug)}
                  className={`px-3 py-2 text-sm border rounded-lg transition text-left ${
                    formData.domains.includes(domain.slug)
                      ? "border-red-primary bg-red-primary/10 text-red-primary font-medium"
                      : "border-border-default text-foreground-secondary hover:border-red-primary/50"
                  }`}
                >
                  {domain.name}
                </button>
              ))}
            </div>
          </div>

          {/* 회사 경력 */}
          {formData.companyExperience.length > 0 && (
            <div className="bg-background-card border border-border-default rounded-lg p-8 mb-6">
              <h2 className="text-xl font-bold text-foreground mb-2">4. 회사 경력</h2>
              <p className="text-sm text-foreground-muted mb-4">정규직/계약직 근무 이력</p>
              <div className="space-y-3">
                {formData.companyExperience.map((exp, idx) => (
                  <div key={idx} className="p-4 bg-background-surface border border-border-default rounded-lg">
                    <div className="flex items-center gap-2 mb-1">
                      <span className="text-xs px-2 py-0.5 bg-blue-500/20 text-blue-400 rounded">🏢 회사</span>
                      <span className="text-sm text-foreground-muted">{exp.period}</span>
                    </div>
                    <p className="text-foreground font-medium">{exp.company}</p>
                    {exp.position && <p className="text-sm text-foreground-secondary">{exp.position}</p>}
                    {exp.description && <p className="text-sm text-foreground-muted mt-1">{exp.description}</p>}
                  </div>
                ))}
              </div>
            </div>
          )}

          {/* 행사/통역 경력 */}
          {formData.eventExperience.length > 0 && (
            <div className="bg-background-card border border-border-default rounded-lg p-8 mb-6">
              <h2 className="text-xl font-bold text-foreground mb-2">5. 통역 경력</h2>
              <p className="text-sm text-foreground-muted mb-4">전시회, B2B, 세미나 등 통역 이력</p>
              <div className="space-y-3">
                {formData.eventExperience.map((exp, idx) => (
                  <div key={idx} className="p-4 bg-background-surface border border-border-default rounded-lg">
                    <div className="flex items-center gap-2 mb-1">
                      <span className={`text-xs px-2 py-0.5 rounded ${
                        exp.type === 'exhibition' ? 'bg-purple-500/20 text-purple-400' :
                        exp.type === 'b2b' ? 'bg-green-500/20 text-green-400' :
                        exp.type === 'seminar' ? 'bg-yellow-500/20 text-yellow-400' :
                        exp.type === 'project' ? 'bg-orange-500/20 text-orange-400' :
                        exp.type === 'legal' ? 'bg-red-500/20 text-red-400' :
                        'bg-gray-500/20 text-gray-400'
                      }`}>
                        {eventTypeLabels[exp.type] || exp.type}
                      </span>
                      <span className="text-sm text-foreground-muted">{exp.period}</span>
                    </div>
                    <p className="text-foreground font-medium">{exp.eventName}</p>
                    {exp.client && <p className="text-sm text-foreground-secondary">클라이언트: {exp.client}</p>}
                    {exp.location && <p className="text-sm text-foreground-muted">{exp.location}</p>}
                  </div>
                ))}
              </div>
            </div>
          )}
        </>
      )}

      {/* 에러 메시지 */}
      {errorMessage && (
        <div className="mb-4 p-4 bg-red-dark/20 border border-red-primary/30 rounded-lg text-red-primary text-sm">
          {errorMessage}
        </div>
      )}

      {/* 제출 버튼 */}
      {(status === "parsed" || status === "submitting") && (
        <button
          type="button"
          onClick={handleSubmit}
          disabled={status === "submitting"}
          className="w-full py-4 bg-red-primary text-white text-lg font-bold rounded-lg hover:bg-red-hover transition disabled:opacity-50 disabled:cursor-not-allowed"
        >
          {status === "submitting" ? "등록 중..." : "이력서 등록하기"}
        </button>
      )}
    </div>
  );
}
