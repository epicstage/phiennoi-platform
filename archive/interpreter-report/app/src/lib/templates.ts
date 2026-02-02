// 통역 보고서 템플릿 정의
// © 2025 Epicstage Corp.

export interface TemplateField {
  id: string;
  label: string;
  labelVi?: string;
  type: 'text' | 'textarea' | 'date' | 'time' | 'select' | 'rating' | 'number' | 'checkbox';
  placeholder?: string;
  options?: string[];
  required?: boolean;
  section?: string;
}

export interface ReportTemplate {
  id: string;
  name: string;
  nameVi?: string;
  description: string;
  descriptionVi?: string;
  styleDescription: string;  // 스타일 설명 (행사명 대신)
  styleDescriptionVi?: string;
  thumbnail: string;
  category: 'tech' | 'beauty' | 'trade' | 'general';
  colorTheme: string;  // 테마 색상
  fields: TemplateField[];
  componentName: 'KBeautyExpoTemplate' | 'OffshoreTechTemplate' | 'GeneralMeetingTemplate';
  pdfLayout?: {
    orientation: 'portrait' | 'landscape';
    margins: { top: number; right: number; bottom: number; left: number };
  };
}

// 템플릿 미리보기용 색상 테마
export const TEMPLATE_COLORS = {
  tech: { primary: '#3B82F6', secondary: '#1E40AF', gradient: 'from-blue-500 to-blue-700' },
  beauty: { primary: '#EC4899', secondary: '#9333EA', gradient: 'from-pink-500 to-purple-600' },
  trade: { primary: '#10B981', secondary: '#0D9488', gradient: 'from-emerald-500 to-teal-600' },
  general: { primary: '#6B7280', secondary: '#374151', gradient: 'from-gray-500 to-gray-700' },
};

export const REPORT_TEMPLATES: ReportTemplate[] = [
  {
    id: 'kbeauty-expo',
    name: '수출상담일지',
    nameVi: 'Nhật ký Tư vấn Xuất khẩu',
    description: '바이어 상담 보고서',
    descriptionVi: 'Báo cáo tư vấn người mua',
    styleDescription: '핑크/퍼플 테마 • 상담 체크리스트 • 별점 평가',
    styleDescriptionVi: 'Chủ đề hồng/tím • Danh sách kiểm tra • Đánh giá sao',
    thumbnail: '/api/template-preview/kbeauty-expo',
    category: 'beauty',
    colorTheme: 'pink-purple',
    componentName: 'KBeautyExpoTemplate',
    fields: [
      // 기본 정보
      { id: 'consultDate', label: '상담 일시', labelVi: 'Ngày tư vấn', type: 'date', required: true, section: 'basic' },
      { id: 'koreanCompany', label: '한국기업명', labelVi: 'Tên công ty Hàn Quốc', type: 'text', required: true, section: 'basic' },
      { id: 'boothNo', label: '부스 번호', labelVi: 'Số gian hàng', type: 'text', section: 'basic' },
      { id: 'staffName', label: '작성자(담당자)', labelVi: 'Người phụ trách', type: 'text', section: 'basic' },
      { id: 'interpreterName', label: '통역사', labelVi: 'Phiên dịch', type: 'text', section: 'basic' },

      // 바이어 정보
      { id: 'consultTime', label: '상담 시간', labelVi: 'Thời gian', type: 'time', section: 'buyer' },
      { id: 'consultItem', label: '상담 품목', labelVi: 'Mặt hàng tư vấn', type: 'text', section: 'buyer' },
      { id: 'buyerCompany', label: '바이어 회사명', labelVi: 'Tên công ty người mua', type: 'text', section: 'buyer' },
      { id: 'buyerContact', label: '담당자명', labelVi: 'Người liên hệ', type: 'text', section: 'buyer' },
      { id: 'buyerPosition', label: '직책', labelVi: 'Chức vụ', type: 'text', section: 'buyer' },
      { id: 'buyerPhone', label: '연락처', labelVi: 'Số điện thoại', type: 'text', section: 'buyer' },

      // 상담 유형 (체크박스)
      { id: 'consultType_price', label: '가격(바이어)>상담', labelVi: 'Tư vấn giá', type: 'checkbox', section: 'consult' },
      { id: 'consultType_sample', label: '샘플요청', labelVi: 'Yêu cầu mẫu', type: 'checkbox', section: 'consult' },
      { id: 'consultType_agent', label: '에이전트 관련', labelVi: 'Đại lý', type: 'checkbox', section: 'consult' },
      { id: 'consultType_quality', label: '품질 관련', labelVi: 'Chất lượng', type: 'checkbox', section: 'consult' },
      { id: 'consultType_market', label: '시장조사', labelVi: 'Nghiên cứu thị trường', type: 'checkbox', section: 'consult' },
      { id: 'consultType_license', label: '인허가 관련', labelVi: 'Giấy phép', type: 'checkbox', section: 'consult' },
      { id: 'consultType_other', label: '기타', labelVi: 'Khác', type: 'checkbox', section: 'consult' },

      // 상담 결과 (체크박스)
      { id: 'result_contract', label: '계약(현->바이어)', labelVi: 'Hợp đồng', type: 'checkbox', section: 'result' },
      { id: 'result_sample', label: '샘플제공', labelVi: 'Cung cấp mẫu', type: 'checkbox', section: 'result' },
      { id: 'result_catalog', label: '카탈로그 제공', labelVi: 'Cung cấp catalog', type: 'checkbox', section: 'result' },
      { id: 'result_revisit', label: '재방문(바이어->현지)', labelVi: 'Thăm lại', type: 'checkbox', section: 'result' },
      { id: 'result_none', label: '무결과', labelVi: 'Không kết quả', type: 'checkbox', section: 'result' },

      // 상담 평가
      { id: 'ratingInterest', label: '관심도 평가', labelVi: 'Đánh giá quan tâm', type: 'rating', section: 'rating' },
      { id: 'ratingPurchase', label: '구매가능성 평가', labelVi: 'Đánh giá khả năng mua', type: 'rating', section: 'rating' },

      // 수출 정보
      { id: 'exportAmount', label: '수출(예상) 금액', labelVi: 'Dự kiến xuất khẩu', type: 'number', placeholder: 'USD', section: 'export' },
      { id: 'currency', label: '통화', labelVi: 'Tiền tệ', type: 'select', options: ['USD', 'VND'], section: 'export' },

      // 상담 내용
      { id: 'consultContent', label: '상담내용(비고/MOU/추가요청 등)', labelVi: 'Nội dung tư vấn', type: 'textarea', section: 'content' },
      { id: 'dealPossibility', label: '거래 성사 가능성', labelVi: 'Khả năng giao dịch', type: 'select',
        options: ['상', '중', '하'], section: 'content' },
    ],
    pdfLayout: {
      orientation: 'portrait',
      margins: { top: 15, right: 10, bottom: 15, left: 10 }
    }
  },
  {
    id: 'offshore-tech',
    name: '기술 협력 상담',
    nameVi: 'Tư vấn Hợp tác Công nghệ',
    description: 'B2B 기술 상담 보고서',
    descriptionVi: 'Báo cáo tư vấn công nghệ B2B',
    styleDescription: '블루 테마 • 양측 기업 정보 • 협력 평가',
    styleDescriptionVi: 'Chủ đề xanh • Thông tin đôi bên • Đánh giá hợp tác',
    thumbnail: '/api/template-preview/offshore-tech',
    category: 'tech',
    colorTheme: 'blue',
    componentName: 'OffshoreTechTemplate',
    fields: [
      // 기본 정보
      { id: 'consultDate', label: '상담 일자', labelVi: 'Ngày tư vấn', type: 'date', required: true, section: 'basic' },
      { id: 'venue', label: '장소', labelVi: 'Địa điểm', type: 'text', section: 'basic' },
      { id: 'interpreterName', label: '통역사', labelVi: 'Phiên dịch', type: 'text', section: 'basic' },

      // 한국 기업 정보
      { id: 'koreanCompany', label: '한국 기업명', labelVi: 'Công ty Hàn Quốc', type: 'text', required: true, section: 'korean' },
      { id: 'koreanContact', label: '담당자명', labelVi: 'Người liên hệ', type: 'text', section: 'korean' },
      { id: 'koreanPosition', label: '직책', labelVi: 'Chức vụ', type: 'text', section: 'korean' },
      { id: 'koreanPhone', label: '연락처', labelVi: 'Số điện thoại', type: 'text', section: 'korean' },
      { id: 'koreanEmail', label: '이메일', labelVi: 'Email', type: 'text', section: 'korean' },
      { id: 'koreanIndustry', label: '업종', labelVi: 'Ngành nghề', type: 'text', section: 'korean' },

      // 베트남 기업 정보
      { id: 'vnCompany', label: '베트남 기업명', labelVi: 'Công ty Việt Nam', type: 'text', section: 'vietnam' },
      { id: 'vnContact', label: '담당자명', labelVi: 'Người liên hệ', type: 'text', section: 'vietnam' },
      { id: 'vnPosition', label: '직책', labelVi: 'Chức vụ', type: 'text', section: 'vietnam' },
      { id: 'vnPhone', label: '연락처', labelVi: 'Số điện thoại', type: 'text', section: 'vietnam' },
      { id: 'vnEmail', label: '이메일', labelVi: 'Email', type: 'text', section: 'vietnam' },
      { id: 'vnIndustry', label: '업종', labelVi: 'Ngành nghề', type: 'text', section: 'vietnam' },

      // 상담 목적 (체크박스)
      { id: 'purpose_partnership', label: '파트너십 구축', labelVi: 'Xây dựng đối tác', type: 'checkbox', section: 'purpose' },
      { id: 'purpose_investment', label: '투자 유치/진행', labelVi: 'Đầu tư', type: 'checkbox', section: 'purpose' },
      { id: 'purpose_tech', label: '기술 이전', labelVi: 'Chuyển giao công nghệ', type: 'checkbox', section: 'purpose' },
      { id: 'purpose_outsourcing', label: '아웃소싱', labelVi: 'Thuê ngoài', type: 'checkbox', section: 'purpose' },
      { id: 'purpose_market', label: '시장 조사', labelVi: 'Nghiên cứu thị trường', type: 'checkbox', section: 'purpose' },
      { id: 'purpose_other', label: '기타', labelVi: 'Khác', type: 'checkbox', section: 'purpose' },

      // 상담 내용
      { id: 'consultTime', label: '상담 시간', labelVi: 'Thời gian', type: 'time', section: 'content' },
      { id: 'discussionPoints', label: '주요 논의 사항', labelVi: 'Điểm thảo luận', type: 'textarea', section: 'content' },
      { id: 'actionItems', label: '후속 조치', labelVi: 'Hành động tiếp theo', type: 'textarea', section: 'content' },

      // 평가
      { id: 'ratingPotential', label: '협력 잠재력', labelVi: 'Tiềm năng hợp tác', type: 'rating', section: 'rating' },
      { id: 'ratingUrgency', label: '긴급도', labelVi: 'Mức độ khẩn cấp', type: 'rating', section: 'rating' },
      { id: 'dealPossibility', label: '협력 성사 가능성', labelVi: 'Khả năng hợp tác', type: 'select',
        options: ['상', '중', '하'], section: 'rating' },

      // 비고
      { id: 'notes', label: '비고', labelVi: 'Ghi chú', type: 'textarea', section: 'notes' },
    ],
    pdfLayout: {
      orientation: 'portrait',
      margins: { top: 15, right: 10, bottom: 15, left: 10 }
    }
  },
  {
    id: 'general-meeting',
    name: '일반 회의록',
    nameVi: 'Biên bản Cuộc họp Chung',
    description: '범용 비즈니스 미팅 보고서',
    descriptionVi: 'Báo cáo họp kinh doanh đa năng',
    styleDescription: '그레이 테마 • 심플 레이아웃 • 자유 형식',
    styleDescriptionVi: 'Chủ đề xám • Bố cục đơn giản • Dạng tự do',
    thumbnail: '/api/template-preview/general-meeting',
    category: 'general',
    colorTheme: 'gray',
    componentName: 'GeneralMeetingTemplate',
    fields: [
      { id: 'meetingTitle', label: '미팅 제목', labelVi: 'Tiêu đề cuộc họp', type: 'text', required: true, section: 'basic' },
      { id: 'meetingDate', label: '미팅 일시', labelVi: 'Ngày họp', type: 'date', required: true, section: 'basic' },
      { id: 'meetingTime', label: '미팅 시간', labelVi: 'Thời gian', type: 'time', section: 'basic' },
      { id: 'location', label: '장소', labelVi: 'Địa điểm', type: 'text', section: 'basic' },

      { id: 'koreanParty', label: '한국측 참석자', labelVi: 'Bên Hàn Quốc', type: 'textarea', section: 'participants' },
      { id: 'vietnamParty', label: '베트남측 참석자', labelVi: 'Bên Việt Nam', type: 'textarea', section: 'participants' },

      { id: 'agenda', label: '회의 안건', labelVi: 'Chương trình nghị sự', type: 'textarea', section: 'content' },
      { id: 'discussion', label: '논의 내용', labelVi: 'Nội dung thảo luận', type: 'textarea', section: 'content' },
      { id: 'decisions', label: '결정 사항', labelVi: 'Quyết định', type: 'textarea', section: 'content' },
      { id: 'nextSteps', label: '후속 조치', labelVi: 'Bước tiếp theo', type: 'textarea', section: 'content' },
    ],
    pdfLayout: {
      orientation: 'portrait',
      margins: { top: 20, right: 15, bottom: 20, left: 15 }
    }
  }
];

export function getTemplateById(id: string): ReportTemplate | undefined {
  return REPORT_TEMPLATES.find(t => t.id === id);
}

export function getTemplatesByCategory(category: string): ReportTemplate[] {
  if (category === 'all') return REPORT_TEMPLATES;
  return REPORT_TEMPLATES.filter(t => t.category === category);
}

// 섹션 라벨 정의
export const SECTION_LABELS: Record<string, { ko: string; vi: string }> = {
  basic: { ko: '기본 정보', vi: 'Thông tin cơ bản' },
  buyer: { ko: '바이어 정보', vi: 'Thông tin người mua' },
  korean: { ko: '한국 기업', vi: 'Công ty Hàn Quốc' },
  vietnam: { ko: '베트남 기업', vi: 'Công ty Việt Nam' },
  consult: { ko: '상담 유형', vi: 'Loại tư vấn' },
  result: { ko: '상담 결과', vi: 'Kết quả tư vấn' },
  rating: { ko: '평가', vi: 'Đánh giá' },
  export: { ko: '수출/계약', vi: 'Xuất khẩu/Hợp đồng' },
  content: { ko: '상담 내용', vi: 'Nội dung' },
  participants: { ko: '참석자', vi: 'Người tham dự' },
  purpose: { ko: '상담 목적', vi: 'Mục đích tư vấn' },
  notes: { ko: '비고', vi: 'Ghi chú' },
  default: { ko: '기타', vi: 'Khác' },
};
