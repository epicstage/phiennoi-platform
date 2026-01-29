"use client";

import { useState, useMemo } from "react";
import Link from "next/link";

interface SearchableTerm {
  slug: string;
  korean: string;
  vietnamese: string;
  hanja: string | null;
  pronunciation?: string;
  difficulty?: "beginner" | "intermediate" | "advanced";
  domain: string;
  domainName: string;
}

interface TermSearchProps {
  terms: SearchableTerm[];
}

const difficultyLabel = {
  beginner: { text: "초급", color: "text-green-success" },
  intermediate: { text: "중급", color: "text-yellow-400" },
  advanced: { text: "고급", color: "text-red-primary" },
};

export default function TermSearch({ terms }: TermSearchProps) {
  const [query, setQuery] = useState("");
  const [selectedDomain, setSelectedDomain] = useState<string>("all");

  const domains = useMemo(() => {
    const uniqueDomains = new Map<string, string>();
    terms.forEach((t) => uniqueDomains.set(t.domain, t.domainName));
    return Array.from(uniqueDomains.entries());
  }, [terms]);

  const filtered = useMemo(() => {
    let result = terms;

    if (selectedDomain !== "all") {
      result = result.filter((t) => t.domain === selectedDomain);
    }

    if (query.trim()) {
      const q = query.trim().toLowerCase();
      result = result.filter(
        (t) =>
          t.korean.toLowerCase().includes(q) ||
          t.vietnamese.toLowerCase().includes(q) ||
          (t.hanja && t.hanja.includes(q)) ||
          (t.pronunciation && t.pronunciation.toLowerCase().includes(q))
      );
    }

    return result;
  }, [terms, query, selectedDomain]);

  return (
    <div>
      {/* 검색바 */}
      <div className="flex flex-col sm:flex-row gap-3 mb-6">
        <div className="relative flex-1">
          <input
            type="text"
            placeholder="용어 검색 (한국어, 베트남어, 한자)..."
            value={query}
            onChange={(e) => setQuery(e.target.value)}
            className="w-full px-4 py-3 pl-10 bg-background-card border border-border-default rounded-lg text-foreground placeholder:text-foreground-muted focus:outline-none focus:border-red-primary transition"
          />
          <svg
            className="absolute left-3 top-1/2 -translate-y-1/2 w-4 h-4 text-foreground-muted"
            fill="none"
            stroke="currentColor"
            viewBox="0 0 24 24"
          >
            <path
              strokeLinecap="round"
              strokeLinejoin="round"
              strokeWidth={2}
              d="M21 21l-6-6m2-5a7 7 0 11-14 0 7 7 0 0114 0z"
            />
          </svg>
        </div>
        <select
          value={selectedDomain}
          onChange={(e) => setSelectedDomain(e.target.value)}
          className="px-4 py-3 bg-background-card border border-border-default rounded-lg text-foreground focus:outline-none focus:border-red-primary transition"
        >
          <option value="all">전체 분야</option>
          {domains.map(([slug, name]) => (
            <option key={slug} value={slug}>
              {name}
            </option>
          ))}
        </select>
      </div>

      {/* 결과 카운트 */}
      <p className="text-sm text-foreground-muted mb-4">
        {filtered.length}개 용어
        {query && ` · "${query}" 검색 결과`}
      </p>

      {/* 결과 목록 */}
      {filtered.length > 0 ? (
        <div className="grid sm:grid-cols-2 lg:grid-cols-3 gap-3">
          {filtered.slice(0, 60).map((term) => (
            <Link
              key={`${term.domain}-${term.slug}`}
              href={`/terms/${term.domain}/${term.slug}`}
              className="p-4 border border-border-default rounded-lg hover:border-red-primary/50 bg-background-card transition"
            >
              <div className="flex items-start justify-between">
                <div>
                  <p className="font-medium text-foreground">{term.korean}</p>
                  <p className="text-sm text-red-primary">{term.vietnamese}</p>
                </div>
                {term.difficulty && (
                  <span
                    className={`text-xs ${difficultyLabel[term.difficulty].color}`}
                  >
                    {difficultyLabel[term.difficulty].text}
                  </span>
                )}
              </div>
              {term.pronunciation && (
                <p className="text-xs text-foreground-muted mt-1">
                  [{term.pronunciation}]
                </p>
              )}
              {term.hanja && (
                <p className="text-xs text-foreground-muted mt-1">
                  {term.hanja}
                </p>
              )}
              <p className="text-xs text-foreground-muted mt-2">
                {term.domainName}
              </p>
            </Link>
          ))}
        </div>
      ) : (
        <div className="text-center py-12 text-foreground-muted">
          <p className="text-lg mb-2">검색 결과가 없습니다</p>
          <p className="text-sm">다른 키워드로 검색해 보세요</p>
        </div>
      )}

      {filtered.length > 60 && (
        <p className="text-center text-foreground-muted text-sm mt-4">
          {filtered.length - 60}개 용어가 더 있습니다. 검색어를 좁혀보세요.
        </p>
      )}
    </div>
  );
}
