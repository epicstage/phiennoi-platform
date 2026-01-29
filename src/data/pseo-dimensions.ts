// pSEO 대량 페이지 생성을 위한 데이터 정의
// 참조: Progamtic/epicstage/data/pseo-dimensions.ts

export const domains = [
  {
    slug: "agriculture",
    name: "농업",
    nameVi: "Nông nghiệp",
    keywords: ["비료", "농기계", "종자", "농산물", "수출", "검역"],
    description: "농업 분야 한-베 통역 전문 용어 및 가이드",
  },
  {
    slug: "beauty",
    name: "뷰티",
    nameVi: "Làm đẹp",
    keywords: ["화장품", "OEM", "ODM", "K-Beauty", "스킨케어", "EXPO"],
    description: "화장품/뷰티 분야 통역 전문 용어",
  },
  {
    slug: "manufacturing",
    name: "제조",
    nameVi: "Sản xuất",
    keywords: ["공장", "품질관리", "설비", "생산라인", "QC"],
    description: "제조업 현장 통역 필수 용어",
  },
  {
    slug: "legal",
    name: "법률",
    nameVi: "Pháp luật",
    keywords: ["수사", "비자", "노동", "계약", "분쟁", "법원"],
    description: "법률/수사 통역 전문 용어",
  },
  {
    slug: "it",
    name: "IT",
    nameVi: "Công nghệ thông tin",
    keywords: ["개발", "아웃소싱", "서버", "소프트웨어", "앱"],
    description: "IT/소프트웨어 분야 통역 용어",
  },
  {
    slug: "construction",
    name: "건설",
    nameVi: "Xây dựng",
    keywords: ["현장", "설계", "감리", "시공", "안전"],
    description: "건설 현장 통역 필수 용어",
  },
  {
    slug: "exhibition",
    name: "박람회",
    nameVi: "Triển lãm",
    keywords: ["EXPO", "전시", "부스", "바이어", "상담회"],
    description: "박람회/전시회 통역 가이드",
  },
  {
    slug: "medical",
    name: "의료",
    nameVi: "Y tế",
    keywords: ["병원", "진료", "약품", "의료기기", "건강검진"],
    description: "의료/헬스케어 통역 용어",
  },
  {
    slug: "finance",
    name: "금융",
    nameVi: "Tài chính",
    keywords: ["은행", "투자", "회계", "세금", "송금"],
    description: "금융/회계 분야 통역 용어",
  },
  {
    slug: "logistics",
    name: "물류",
    nameVi: "Logistics",
    keywords: ["운송", "통관", "창고", "수출입", "관세"],
    description: "물류/통관 분야 통역 용어",
  },
] as const;

export const interpretTypes = [
  {
    slug: "exhibition",
    name: "박람회 통역",
    nameVi: "Phiên dịch triển lãm",
    description: "전시회, EXPO, 박람회 현장 통역",
  },
  {
    slug: "b2b",
    name: "B2B 매칭 통역",
    nameVi: "Phiên dịch B2B",
    description: "수출상담회, 바이어 미팅 통역",
  },
  {
    slug: "onsite",
    name: "현장 통역",
    nameVi: "Phiên dịch tại chỗ",
    description: "공장, 건설현장 등 현장 통역",
  },
  {
    slug: "escort",
    name: "수행 통역",
    nameVi: "Phiên dịch tháp tùng",
    description: "VIP 수행, 출장 동행 통역",
  },
  {
    slug: "simultaneous",
    name: "동시 통역",
    nameVi: "Phiên dịch đồng thời",
    description: "컨퍼런스, 세미나 동시통역",
  },
  {
    slug: "consecutive",
    name: "순차 통역",
    nameVi: "Phiên dịch liên tục",
    description: "회의, 협상 순차통역",
  },
  {
    slug: "phone",
    name: "전화/화상 통역",
    nameVi: "Phiên dịch điện thoại/video",
    description: "원격 통역 서비스",
  },
  {
    slug: "document",
    name: "문서 번역",
    nameVi: "Dịch tài liệu",
    description: "계약서, 기술문서 번역",
  },
] as const;

export const locations = [
  { slug: "hochiminh", name: "호치민", nameVi: "TP. Hồ Chí Minh" },
  { slug: "hanoi", name: "하노이", nameVi: "Hà Nội" },
  { slug: "danang", name: "다낭", nameVi: "Đà Nẵng" },
  { slug: "seoul", name: "서울", nameVi: "Seoul" },
  { slug: "busan", name: "부산", nameVi: "Busan" },
  { slug: "remote", name: "원격", nameVi: "Từ xa" },
] as const;

// 타입 정의
export type Domain = (typeof domains)[number];
export type InterpretType = (typeof interpretTypes)[number];
export type Location = (typeof locations)[number];

// 헬퍼 함수
export function getDomainBySlug(slug: string): Domain | undefined {
  return domains.find((d) => d.slug === slug);
}

export function getInterpretTypeBySlug(slug: string): InterpretType | undefined {
  return interpretTypes.find((t) => t.slug === slug);
}

export function getLocationBySlug(slug: string): Location | undefined {
  return locations.find((l) => l.slug === slug);
}

// 페이지 수 계산
export const pageCountEstimate = {
  termsPages: domains.length * 100, // 10 × 100 = 1,000
  guidesPages: domains.length * interpretTypes.length, // 10 × 8 = 80
  scenariosPages: 50, // 수동 생성
  total: function () {
    return this.termsPages + this.guidesPages + this.scenariosPages;
  },
};

// 예상 pSEO 페이지 수: 1,130
