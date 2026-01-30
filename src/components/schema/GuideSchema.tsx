interface GuideSchemaProps {
  domainName: string;
  domainNameVi: string;
  domainSlug: string;
  typeName: string;
  typeNameVi: string;
  typeSlug: string;
  typeDescription: string;
  domainKeywords: readonly string[];
}

export default function GuideSchema({
  domainName,
  domainNameVi,
  domainSlug,
  typeName,
  typeNameVi,
  typeSlug,
  typeDescription,
  domainKeywords,
}: GuideSchemaProps) {
  const baseUrl = "https://vn.epicstage.co.kr";
  const pageUrl = `${baseUrl}/guides/${domainSlug}/${typeSlug}`;

  // Article Schema
  const articleSchema = {
    "@context": "https://schema.org",
    "@type": "Article",
    headline: `${domainName} ${typeName} 가이드 | 한-베 통역`,
    description: `${domainName} 분야 ${typeDescription}을 위한 완벽 가이드. ${domainKeywords.slice(0, 3).join(", ")} 관련 통역 준비사항, 핵심 표현, 주의점.`,
    url: pageUrl,
    inLanguage: "ko",
    about: [
      { "@type": "Thing", name: `${domainName} 통역` },
      { "@type": "Thing", name: typeName },
    ],
    publisher: {
      "@type": "Organization",
      name: "Epic Note",
      url: baseUrl,
    },
  };

  // HowTo Schema (가이드는 실질적으로 How-to)
  const howToSchema = {
    "@context": "https://schema.org",
    "@type": "HowTo",
    name: `${domainName} ${typeName} 준비 가이드`,
    description: `${domainName}(${domainNameVi}) 분야 ${typeName}(${typeNameVi})을 위한 단계별 준비 가이드`,
    step: [
      {
        "@type": "HowToStep",
        name: "용어 사전 준비",
        text: `${domainName} 분야 전문 용어 목록을 미리 준비하세요. ${domainKeywords.join(", ")} 관련 용어가 중요합니다.`,
        url: `${baseUrl}/terms/${domainSlug}`,
      },
      {
        "@type": "HowToStep",
        name: "자료 사전 검토",
        text: "행사/미팅 관련 자료를 미리 받아 검토하세요. 회사 소개서, 제품 카탈로그, 발표 자료 등을 확인합니다.",
      },
      {
        "@type": "HowToStep",
        name: "핵심 표현 학습",
        text: `${domainName} ${typeName}에서 자주 사용되는 한-베 핵심 표현을 미리 학습하세요.`,
      },
      {
        "@type": "HowToStep",
        name: "문화적 차이 숙지",
        text: "한국과 베트남의 비즈니스 문화 차이를 이해하고, 통역 시 적절히 보충 설명할 준비를 하세요.",
      },
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
        name: "가이드",
        item: `${baseUrl}/guides`,
      },
      {
        "@type": "ListItem",
        position: 3,
        name: domainName,
        item: `${baseUrl}/guides/${domainSlug}`,
      },
      {
        "@type": "ListItem",
        position: 4,
        name: typeName,
        item: pageUrl,
      },
    ],
  };

  return (
    <>
      <script
        type="application/ld+json"
        dangerouslySetInnerHTML={{
          __html: JSON.stringify(articleSchema),
        }}
      />
      <script
        type="application/ld+json"
        dangerouslySetInnerHTML={{
          __html: JSON.stringify(howToSchema),
        }}
      />
      <script
        type="application/ld+json"
        dangerouslySetInnerHTML={{
          __html: JSON.stringify(breadcrumbSchema),
        }}
      />
    </>
  );
}
