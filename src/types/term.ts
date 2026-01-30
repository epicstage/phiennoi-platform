// 용어 데이터 타입 정의

export interface TermExample {
  ko: string;
  vi: string;
  /** 상황: formal(공식), informal(비공식), document(문서), meeting(회의), onsite(현장) */
  situation?: string;
}

export interface Term {
  slug: string;
  korean: string;
  vietnamese: string;
  hanja: string | null;
  hanjaReading: string | null;
  /** 한국어 의미 - 최소 150자 */
  meaningKo: string;
  /** 베트남어 의미 - 최소 150자 */
  meaningVi: string;
  /** 사용 맥락 - 구체적 상황 설명 200자+ */
  context: string;
  /** 베트남어 맥락 설명 */
  contextVi?: string;
  /** 통역 예문 - 최소 3개, 상황별 */
  examples: TermExample[];
  relatedTerms: string[];

  // === 신규 필드 (P1 보강) ===

  /** 베트남어 발음 가이드 (한글 표기) */
  pronunciation?: string;
  /** 난이도: beginner | intermediate | advanced */
  difficulty?: "beginner" | "intermediate" | "advanced";
  /** 사용 빈도 (1~5) */
  frequency?: number;
  /** 흔한 통역 실수 */
  commonMistakes?: (string | { mistake: string; correction: string; explanation: string })[];
  /** 문화적 차이 / 주의사항 */
  culturalNote?: string;
  /** 격식 수준: formal | informal | neutral | document */
  formalLevel?: "formal" | "informal" | "neutral" | "document";
  /** 약어/줄임말 */
  abbreviation?: string;
  /** 동의어 (한국어) */
  synonyms?: string[];
  /** 동의어 (베트남어) */
  synonymsVi?: string[];
}

export interface TermWithDomain extends Term {
  domain: string;
  domainName: string;
  domainNameVi: string;
}

// 가이드 콘텐츠 타입

export interface GuideScenario {
  title: string;
  titleVi: string;
  description: string;
  dialogues: { speaker: string; ko: string; vi: string }[];
}

export interface GuideChecklist {
  category: string;
  items: string[];
}

export interface GuideContent {
  domain: string;
  type: string;
  /** 가이드 고유 개요 (300자+) */
  overview: string;
  /** 이 통역 유형의 특징 */
  characteristics: string[];
  /** 준비사항 상세 */
  preparation: {
    title: string;
    description: string;
    tips: string[];
  }[];
  /** 핵심 표현 (상황별 5개+) */
  keyExpressions: {
    situation: string;
    ko: string;
    vi: string;
    note?: string;
  }[];
  /** 실제 시나리오 대화문 */
  scenarios: GuideScenario[];
  /** 체크리스트 */
  checklists: GuideChecklist[];
  /** 문화적 주의사항 */
  culturalNotes: string[];
  /** 흔한 실수 */
  commonMistakes: string[];
  /** 관련 용어 키 목록 */
  relatedTermSlugs: string[];
  /** 추천 학습 순서 */
  studyOrder?: string[];
}
