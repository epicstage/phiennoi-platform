"use client";

import { useState, useRef } from "react";

type FormStatus = "idle" | "submitting" | "success" | "error";

export default function UploadForm() {
  const [file, setFile] = useState<File | null>(null);
  const [status, setStatus] = useState<FormStatus>("idle");
  const [errorMessage, setErrorMessage] = useState("");
  const fileInputRef = useRef<HTMLInputElement>(null);

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

  const handleSubmit = async () => {
    if (!file) {
      setErrorMessage("파일을 선택해주세요.");
      return;
    }

    setStatus("submitting");
    setErrorMessage("");

    const formData = new FormData();
    formData.set("resume", file);

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
      <div className="max-w-xl mx-auto px-6 py-16">
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
            등록 완료!
          </h2>
          <p className="text-foreground-secondary mb-6">
            이력서가 성공적으로 등록되었습니다.
          </p>
          <a
            href="/"
            className="inline-block px-6 py-3 bg-red-primary text-white font-semibold rounded-lg hover:bg-red-hover transition"
          >
            홈으로
          </a>
        </div>
      </div>
    );
  }

  return (
    <div className="max-w-xl mx-auto px-6 py-16">
      <div className="bg-background-card border border-border-default rounded-lg p-8">
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
                이력서 파일 선택
              </p>
              <p className="text-sm text-foreground-muted">
                PDF, DOC, DOCX (최대 10MB)
              </p>
            </>
          )}
        </div>

        {/* Error Message */}
        {errorMessage && (
          <div className="mt-4 p-4 bg-red-dark/20 border border-red-primary/30 rounded-lg text-red-primary text-sm">
            {errorMessage}
          </div>
        )}

        {/* Submit */}
        <button
          type="button"
          onClick={handleSubmit}
          disabled={!file || status === "submitting"}
          className="w-full mt-6 py-4 bg-red-primary text-white text-lg font-bold rounded-lg hover:bg-red-hover transition disabled:opacity-50 disabled:cursor-not-allowed"
        >
          {status === "submitting" ? "업로드 중..." : "이력서 등록"}
        </button>
      </div>
    </div>
  );
}
