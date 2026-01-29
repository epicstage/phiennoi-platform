"use client";

import { useState, useRef } from "react";
import { domains } from "@/data/pseo-dimensions";

type FormStatus = "idle" | "submitting" | "success" | "error";

export default function UploadForm() {
  const [selectedDomains, setSelectedDomains] = useState<string[]>([]);
  const [file, setFile] = useState<File | null>(null);
  const [status, setStatus] = useState<FormStatus>("idle");
  const [errorMessage, setErrorMessage] = useState("");
  const fileInputRef = useRef<HTMLInputElement>(null);

  const toggleDomain = (slug: string) => {
    setSelectedDomains((prev) =>
      prev.includes(slug) ? prev.filter((d) => d !== slug) : [...prev, slug]
    );
  };

  const handleFileChange = (e: React.ChangeEvent<HTMLInputElement>) => {
    const selected = e.target.files?.[0];
    if (!selected) return;

    // 10MB 제한
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
  };

  const handleSubmit = async (e: React.FormEvent<HTMLFormElement>) => {
    e.preventDefault();
    setStatus("submitting");
    setErrorMessage("");

    const form = e.currentTarget;
    const formData = new FormData(form);

    // 선택된 도메인 추가
    selectedDomains.forEach((d) => formData.append("domains", d));

    // 파일 추가
    if (file) {
      formData.set("resume", file);
    }

    try {
      const res = await fetch("/api/upload", {
        method: "POST",
        body: formData,
      });

      const data = await res.json();

      if (!res.ok) {
        throw new Error(data.error || "등록에 실패했습니다.");
      }

      setStatus("success");
    } catch (err) {
      setStatus("error");
      setErrorMessage(
        err instanceof Error ? err.message : "알 수 없는 오류가 발생했습니다."
      );
    }
  };

  if (status === "success") {
    return (
      <div className="max-w-3xl mx-auto px-6 py-12">
        <div className="bg-background-card border border-green-success/30 rounded-lg p-12 text-center">
          <svg
            className="w-16 h-16 mx-auto mb-6 text-green-success"
            fill="currentColor"
            viewBox="0 0 20 20"
          >
            <path
              fillRule="evenodd"
              d="M16.707 5.293a1 1 0 010 1.414l-8 8a1 1 0 01-1.414 0l-4-4a1 1 0 011.414-1.414L8 12.586l7.293-7.293a1 1 0 011.414 0z"
              clipRule="evenodd"
            />
          </svg>
          <h2 className="text-2xl font-bold text-foreground mb-3">
            등록이 완료되었습니다!
          </h2>
          <p className="text-foreground-secondary mb-6">
            이력서가 성공적으로 등록되었습니다. 전문 분야에 맞는 통역 의뢰가
            있으면 연락드리겠습니다.
          </p>
          <a
            href="/"
            className="inline-block px-6 py-3 bg-red-primary text-white font-semibold rounded-lg hover:bg-red-hover transition"
          >
            홈으로 돌아가기
          </a>
        </div>
      </div>
    );
  }

  return (
    <form onSubmit={handleSubmit} className="max-w-3xl mx-auto px-6 py-12">
      {/* Benefits */}
      <section className="bg-background-card border border-border-default rounded-lg p-8 mb-8">
        <h2 className="text-xl font-bold text-foreground mb-6">등록 혜택</h2>
        <div className="grid md:grid-cols-2 gap-4">
          {[
            {
              title: "전문 분야 매칭",
              desc: "경력에 맞는 통역 의뢰를 우선 안내",
            },
            { title: "프로필 노출", desc: "의뢰인에게 프로필 직접 노출" },
            { title: "무료 등록", desc: "이력서 등록 및 매칭 무료" },
            { title: "경력 관리", desc: "통역 경력 체계적 관리" },
          ].map((item) => (
            <div key={item.title} className="flex items-start gap-3">
              <svg
                className="w-5 h-5 text-green-success mt-0.5 shrink-0"
                fill="currentColor"
                viewBox="0 0 20 20"
              >
                <path
                  fillRule="evenodd"
                  d="M16.707 5.293a1 1 0 010 1.414l-8 8a1 1 0 01-1.414 0l-4-4a1 1 0 011.414-1.414L8 12.586l7.293-7.293a1 1 0 011.414 0z"
                  clipRule="evenodd"
                />
              </svg>
              <div>
                <h3 className="font-semibold text-foreground">{item.title}</h3>
                <p className="text-sm text-foreground-muted">{item.desc}</p>
              </div>
            </div>
          ))}
        </div>
      </section>

      {/* Domain Selection */}
      <section className="bg-background-card border border-border-default rounded-lg p-8 mb-8">
        <h2 className="text-xl font-bold text-foreground mb-4">
          전문 분야 선택
        </h2>
        <p className="text-foreground-secondary mb-6">
          경험이 있는 분야를 선택해주세요 (복수 선택 가능)
        </p>
        <div className="grid md:grid-cols-2 gap-3">
          {domains.map((domain) => (
            <button
              type="button"
              key={domain.slug}
              onClick={() => toggleDomain(domain.slug)}
              className={`flex items-center gap-3 p-4 border rounded-lg cursor-pointer transition text-left ${
                selectedDomains.includes(domain.slug)
                  ? "border-red-primary bg-red-primary/10"
                  : "border-border-default hover:border-red-primary/50 bg-background-surface"
              }`}
            >
              <div
                className={`w-5 h-5 rounded border-2 flex items-center justify-center shrink-0 ${
                  selectedDomains.includes(domain.slug)
                    ? "border-red-primary bg-red-primary"
                    : "border-foreground-muted"
                }`}
              >
                {selectedDomains.includes(domain.slug) && (
                  <svg
                    className="w-3 h-3 text-white"
                    fill="currentColor"
                    viewBox="0 0 20 20"
                  >
                    <path
                      fillRule="evenodd"
                      d="M16.707 5.293a1 1 0 010 1.414l-8 8a1 1 0 01-1.414 0l-4-4a1 1 0 011.414-1.414L8 12.586l7.293-7.293a1 1 0 011.414 0z"
                      clipRule="evenodd"
                    />
                  </svg>
                )}
              </div>
              <div>
                <span className="font-medium text-foreground">
                  {domain.name}
                </span>
                <span className="text-red-primary ml-2 text-sm">
                  {domain.nameVi}
                </span>
                <div className="text-xs text-foreground-muted mt-1">
                  {domain.keywords.slice(0, 3).join(", ")}
                </div>
              </div>
            </button>
          ))}
        </div>
      </section>

      {/* File Upload */}
      <section className="bg-background-card border border-border-default rounded-lg p-8 mb-8">
        <h2 className="text-xl font-bold text-foreground mb-4">
          이력서 업로드
        </h2>
        <p className="text-foreground-secondary mb-6">
          PDF 또는 Word 파일로 이력서를 업로드해주세요.
        </p>

        <input
          ref={fileInputRef}
          type="file"
          accept=".pdf,.doc,.docx"
          onChange={handleFileChange}
          className="hidden"
        />

        <div
          onClick={() => fileInputRef.current?.click()}
          className={`border-2 border-dashed rounded-lg p-12 text-center transition cursor-pointer ${
            file
              ? "border-green-success/50 bg-green-success/5"
              : "border-border-default hover:border-red-primary/50 bg-background-surface"
          }`}
        >
          {file ? (
            <>
              <svg
                className="w-12 h-12 mx-auto mb-4 text-green-success"
                fill="currentColor"
                viewBox="0 0 20 20"
              >
                <path
                  fillRule="evenodd"
                  d="M16.707 5.293a1 1 0 010 1.414l-8 8a1 1 0 01-1.414 0l-4-4a1 1 0 011.414-1.414L8 12.586l7.293-7.293a1 1 0 011.414 0z"
                  clipRule="evenodd"
                />
              </svg>
              <p className="text-foreground font-medium mb-1">{file.name}</p>
              <p className="text-sm text-foreground-muted">
                {(file.size / 1024 / 1024).toFixed(1)}MB · 클릭하여 변경
              </p>
            </>
          ) : (
            <>
              <svg
                className="w-12 h-12 mx-auto mb-4 text-foreground-muted"
                fill="none"
                stroke="currentColor"
                viewBox="0 0 24 24"
              >
                <path
                  strokeLinecap="round"
                  strokeLinejoin="round"
                  strokeWidth={1.5}
                  d="M7 16a4 4 0 01-.88-7.903A5 5 0 1115.9 6L16 6a5 5 0 011 9.9M15 13l-3-3m0 0l-3 3m3-3v12"
                />
              </svg>
              <p className="text-foreground font-medium mb-2">
                파일을 클릭하여 업로드
              </p>
              <p className="text-sm text-foreground-muted">
                PDF, DOC, DOCX (최대 10MB)
              </p>
            </>
          )}
        </div>

        <div className="mt-6 p-4 bg-background-surface border border-border-default rounded-lg">
          <h3 className="font-semibold text-foreground mb-2">
            이력서 포함 권장 항목
          </h3>
          <ul className="text-sm text-foreground-secondary space-y-1">
            <li>• 통역 경력 (행사명, 기간, 분야)</li>
            <li>• 학력 (베트남 대학 졸업 시 표기)</li>
            <li>• 언어 능력 (TOPIK, VSEPR 등)</li>
            <li>• 전문 분야 (농업, 뷰티, 제조 등)</li>
          </ul>
        </div>
      </section>

      {/* Basic Info */}
      <section className="bg-background-card border border-border-default rounded-lg p-8 mb-8">
        <h2 className="text-xl font-bold text-foreground mb-6">기본 정보</h2>
        <div className="space-y-4">
          <div>
            <label className="block text-sm font-medium text-foreground-secondary mb-1">
              이름 *
            </label>
            <input
              name="name"
              type="text"
              required
              className="w-full px-4 py-3 bg-background-surface border border-border-default rounded-lg text-foreground placeholder:text-foreground-muted focus:ring-2 focus:ring-red-primary focus:border-red-primary outline-none"
              placeholder="홍길동"
            />
          </div>
          <div>
            <label className="block text-sm font-medium text-foreground-secondary mb-1">
              이메일 *
            </label>
            <input
              name="email"
              type="email"
              required
              className="w-full px-4 py-3 bg-background-surface border border-border-default rounded-lg text-foreground placeholder:text-foreground-muted focus:ring-2 focus:ring-red-primary focus:border-red-primary outline-none"
              placeholder="example@email.com"
            />
          </div>
          <div>
            <label className="block text-sm font-medium text-foreground-secondary mb-1">
              연락처 *
            </label>
            <input
              name="phone"
              type="tel"
              required
              className="w-full px-4 py-3 bg-background-surface border border-border-default rounded-lg text-foreground placeholder:text-foreground-muted focus:ring-2 focus:ring-red-primary focus:border-red-primary outline-none"
              placeholder="010-1234-5678"
            />
          </div>
          <div>
            <label className="block text-sm font-medium text-foreground-secondary mb-1">
              활동 지역
            </label>
            <select
              name="location"
              className="w-full px-4 py-3 bg-background-surface border border-border-default rounded-lg text-foreground focus:ring-2 focus:ring-red-primary focus:border-red-primary outline-none"
            >
              <option value="">선택해주세요</option>
              <option value="호치민">호치민</option>
              <option value="하노이">하노이</option>
              <option value="다낭">다낭</option>
              <option value="서울/수도권">서울/수도권</option>
              <option value="부산">부산</option>
              <option value="원격 가능">원격 가능</option>
            </select>
          </div>
        </div>
      </section>

      {/* Error Message */}
      {errorMessage && (
        <div className="mb-4 p-4 bg-red-dark/20 border border-red-primary/30 rounded-lg text-red-primary text-sm">
          {errorMessage}
        </div>
      )}

      {/* Submit */}
      <button
        type="submit"
        disabled={status === "submitting"}
        className="w-full py-4 bg-red-primary text-white text-lg font-bold rounded-lg hover:bg-red-hover transition disabled:opacity-50 disabled:cursor-not-allowed"
      >
        {status === "submitting" ? "등록 중..." : "이력서 등록하기"}
      </button>

      <p className="text-center text-sm text-foreground-muted mt-4">
        등록 시{" "}
        <a href="/privacy" className="text-red-primary hover:underline">
          개인정보처리방침
        </a>
        에 동의합니다.
      </p>
    </form>
  );
}
