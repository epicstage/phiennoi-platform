// 용어 데이터 타입 정의

export interface TermExample {
  ko: string;
  vi: string;
}

export interface Term {
  slug: string;
  korean: string;
  vietnamese: string;
  hanja: string | null;
  hanjaReading: string | null;
  meaningKo: string;
  meaningVi: string;
  context: string;
  examples: TermExample[];
  relatedTerms: string[];
}

export interface TermWithDomain extends Term {
  domain: string;
  domainName: string;
  domainNameVi: string;
}
