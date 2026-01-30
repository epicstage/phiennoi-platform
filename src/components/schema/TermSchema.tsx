import type { Term } from "@/types/term";

interface TermSchemaProps {
  term: Term;
  domainName: string;
  domainNameVi: string;
  domainSlug: string;
}

export default function TermSchema({
  term,
  domainName,
  domainNameVi,
  domainSlug,
}: TermSchemaProps) {
  const baseUrl = "https://vn.epicstage.co.kr";
  const pageUrl = `${baseUrl}/terms/${domainSlug}/${term.slug}`;

  // DefinedTerm Schema
  const definedTermSchema = {
    "@context": "https://schema.org",
    "@type": "DefinedTerm",
    name: term.korean,
    alternateName: term.vietnamese,
    description: term.meaningKo,
    inDefinedTermSet: {
      "@type": "DefinedTermSet",
      name: `${domainName} 한-베 통역 용어사전`,
      description: `${domainName}(${domainNameVi}) 분야 한국어-베트남어 통역 전문 용어 모음`,
    },
    url: pageUrl,
  };

  // FAQ Schema - 검색 결과에 FAQ 리치 스니펫 표시
  const faqSchema = {
    "@context": "https://schema.org",
    "@type": "FAQPage",
    mainEntity: [
      {
        "@type": "Question",
        name: `${term.korean}을(를) 베트남어로 뭐라고 하나요?`,
        acceptedAnswer: {
          "@type": "Answer",
          text: `${term.korean}은(는) 베트남어로 "${term.vietnamese}"${term.pronunciation ? ` (발음: ${term.pronunciation})` : ""}입니다. ${term.meaningKo}`,
        },
      },
      {
        "@type": "Question",
        name: `${term.korean} 통역 시 주의할 점은?`,
        acceptedAnswer: {
          "@type": "Answer",
          text: term.commonMistakes?.length
            ? term.commonMistakes.map((m: string | { mistake: string; correction: string; explanation: string }) =>
                typeof m === "string" ? m : `${m.mistake} → ${m.correction}`
              ).join(" / ")
            : `${term.context}. ${domainName} 분야 전문 용어이므로 정확한 발음과 맥락 파악이 중요합니다.`,
        },
      },
      ...(term.culturalNote
        ? [
            {
              "@type": "Question",
              name: `${term.korean} 관련 한-베 문화 차이가 있나요?`,
              acceptedAnswer: {
                "@type": "Answer",
                text: term.culturalNote,
              },
            },
          ]
        : []),
    ],
  };

  // BreadcrumbList Schema
  const breadcrumbSchema = {
    "@context": "https://schema.org",
    "@type": "BreadcrumbList",
    itemListElement: [
      {
        "@type": "ListItem",
        position: 1,
        name: "홈",
        item: baseUrl,
      },
      {
        "@type": "ListItem",
        position: 2,
        name: "용어사전",
        item: `${baseUrl}/terms`,
      },
      {
        "@type": "ListItem",
        position: 3,
        name: domainName,
        item: `${baseUrl}/terms/${domainSlug}`,
      },
      {
        "@type": "ListItem",
        position: 4,
        name: term.korean,
        item: pageUrl,
      },
    ],
  };

  // Article Schema (for rich search appearance)
  const articleSchema = {
    "@context": "https://schema.org",
    "@type": "Article",
    headline: `${term.korean} 베트남어 | ${term.vietnamese} | ${domainName} 통역 용어`,
    description: `${term.korean}(${term.vietnamese})의 뜻과 통역 표현. ${domainName} 분야 한-베 통역 필수 용어.`,
    url: pageUrl,
    inLanguage: "ko",
    about: {
      "@type": "Thing",
      name: `${domainName} 통역`,
    },
    publisher: {
      "@type": "Organization",
      name: "Epic Note",
      url: baseUrl,
    },
  };

  return (
    <>
      <script
        type="application/ld+json"
        dangerouslySetInnerHTML={{
          __html: JSON.stringify(definedTermSchema),
        }}
      />
      <script
        type="application/ld+json"
        dangerouslySetInnerHTML={{
          __html: JSON.stringify(faqSchema),
        }}
      />
      <script
        type="application/ld+json"
        dangerouslySetInnerHTML={{
          __html: JSON.stringify(breadcrumbSchema),
        }}
      />
      <script
        type="application/ld+json"
        dangerouslySetInnerHTML={{
          __html: JSON.stringify(articleSchema),
        }}
      />
    </>
  );
}
