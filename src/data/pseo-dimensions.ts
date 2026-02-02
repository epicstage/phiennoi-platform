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
  {
    slug: "food",
    name: "식품",
    nameVi: "Thực phẩm",
    keywords: ["식품안전", "HACCP", "수출", "가공", "유통기한"],
    description: "식품/외식 분야 통역 용어",
  },
  {
    slug: "realEstate",
    name: "부동산",
    nameVi: "Bất động sản",
    keywords: ["임대", "매매", "아파트", "토지", "개발"],
    description: "부동산/건축 분야 통역 용어",
  },
  {
    slug: "tourism",
    name: "관광",
    nameVi: "Du lịch",
    keywords: ["호텔", "투어", "가이드", "관광비자", "리조트"],
    description: "관광/호텔 분야 통역 용어",
  },
  {
    slug: "education",
    name: "교육",
    nameVi: "Giáo dục",
    keywords: ["유학", "연수", "대학", "장학금", "학위"],
    description: "교육/연수 분야 통역 용어",
  },
  {
    slug: "environment",
    name: "환경",
    nameVi: "Môi trường",
    keywords: ["폐수처리", "재활용", "환경영향평가", "탄소", "에너지"],
    description: "환경/에너지 분야 통역 용어",
  },
  {
    slug: "textile",
    name: "섬유",
    nameVi: "Dệt may",
    keywords: ["원단", "봉제", "패션", "원사", "염색"],
    description: "섬유/의류 분야 통역 용어",
  },
  {
    slug: "automotive",
    name: "자동차",
    nameVi: "Ô tô",
    keywords: ["부품", "조립", "엔진", "전기차", "딜러"],
    description: "자동차/부품 분야 통역 용어",
  },
  {
    slug: "electronics",
    name: "전자",
    nameVi: "Điện tử",
    keywords: ["반도체", "PCB", "디스플레이", "배터리", "조립"],
    description: "전자/반도체 분야 통역 용어",
  },
  {
    slug: "hr",
    name: "인사노무",
    nameVi: "Nhân sự",
    keywords: ["채용", "근로계약", "급여", "사회보험", "노동법"],
    description: "인사/노무 분야 통역 용어",
  },
  {
    slug: "trade",
    name: "무역",
    nameVi: "Thương mại",
    keywords: ["수출", "수입", "LC", "통관", "FOB", "CIF"],
    description: "무역/통관 분야 통역 용어",
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

// 페이지 수 계산 (실제 용어 수는 도메인마다 다름: medical 1000, construction 1000, legal 995, 나머지 100)
export const pageCountEstimate = {
  termsPages: 4794, // 실제 총 용어 수 (동적 계산은 lib/terms.ts의 getTotalTermCount 사용)
  guidesPages: domains.length * interpretTypes.length, // 20 × 8 = 160
  scenariosPages: 50, // 수동 생성
  total: function () {
    return this.termsPages + this.guidesPages + this.scenariosPages;
  },
};

// 예상 pSEO 페이지 수: ~5,004
