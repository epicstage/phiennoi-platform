const fs = require('fs');
const path = '/Users/mac/Documents/claude_code/projects/hanbe-interpreter/phiennoi-platform/src/data/terms/legal.json';
const existing = JSON.parse(fs.readFileSync(path, 'utf8'));
const existingSlugs = new Set(existing.map(e => e.slug));

const terms = [
{
  slug: "luat-hinh-su-viet-nam",
  korean: "소송비용",
  vietnamese: "án phí",
  hanja: "訴訟費用",
  hanjaReading: "소(호소할 소) + 송(다툴 송) + 비(쓸 비) + 용(쓸 용)",
  termType: "word",
  meaningKo: "법원에서 재판을 진행하기 위해 당사자가 납부해야 하는 비용으로, 소장 접수비, 감정비, 증인 출석비 등을 포함합니다. 패소한 당사자가 부담하는 것이 원칙이며, 한-베 소송에서 양국 법원의 소송비용 체계가 다르므로 사전 확인이 필요합니다.",
  meaningVi: "Chi phí các bên phải nộp để tòa án tiến hành xét xử, bao gồm phí nộp đơn, phí giám định, phí nhân chứng. Nguyên tắc bên thua kiện chịu án phí. Trong kiện tụng Hàn-Việt, hệ thống án phí hai nước khác nhau nên cần xác nhận trước.",
  pronunciation: "안 피",
  commonMistakes: ["소송비용(án phí)과 변호사비(chi phí luật sư) 혼동","án phí를 법원 비용으로만 한정하면 안 됨","소송비용 부담 주체를 사전에 확인해야 함"],
  culturalNote: "베트남의 소송비용은 한국보다 상대적으로 낮지만, 소송 기간이 길어질수록 총 비용이 증가하므로 예산 계획이 중요합니다.",
  context: "재판, 법률 비용",
  examples: [
    {ko: "소송비용은 패소자가 부담합니다.", vi: "Án phí do bên thua kiện chịu.", situation: "formal"},
    {ko: "소송비용 얼마나 들어?", vi: "Án phí bao nhiêu?", situation: "onsite"},
    {ko: "소송비용이 너무 비싸.", vi: "Án phí đắt quá.", situation: "informal"}
  ],
  relatedTerms: ["소송", "법원", "변호사"],
  difficulty: "intermediate",
  frequency: 3,
  formalLevel: "formal"
},
{
  slug: "hop-dong-lao-dong",
  korean: "근로계약",
  vietnamese: "hợp đồng lao động",
  hanja: "勤勞契約",
  hanjaReading: "근(부지런할 근) + 로(일할 로) + 계(맺을 계) + 약(약속 약)",
  termType: "word",
  meaningKo: "사용자와 근로자 간에 근로 조건(임금, 근로시간, 업무내용 등)을 약정하는 계약입니다. 베트남 노동법에 따라 서면 계약이 의무이며, 무기한 계약과 기간제 계약으로 구분됩니다. 한국 투자 기업이 베트남 직원을 채용할 때 필수적으로 체결해야 합니다.",
  meaningVi: "Hợp đồng thỏa thuận điều kiện lao động (lương, giờ làm, nội dung công việc) giữa người sử dụng lao động và người lao động. Theo luật lao động Việt Nam, hợp đồng bằng văn bản là bắt buộc. Phân thành hợp đồng không xác định thời hạn và hợp đồng có thời hạn.",
  pronunciation: "헙 동 라오 동",
  commonMistakes: ["근로계약(hợp đồng lao động)과 도급계약(hợp đồng khoán) 혼동","수습기간(thử việc) 규정이 한국과 다름","계약 해지 조건이 양국에서 상이함"],
  culturalNote: "베트남에서 근로계약 체결 시 수습기간은 최대 60일이며, 수습 급여는 정규 급여의 85% 이상이어야 합니다.",
  context: "인사 관리, 노동법",
  examples: [
    {ko: "근로계약을 체결합니다.", vi: "Ký kết hợp đồng lao động.", situation: "formal"},
    {ko: "근로계약 내용 확인해 봐.", vi: "Kiểm tra nội dung hợp đồng lao động.", situation: "onsite"},
    {ko: "근로계약 몇 년짜리야?", vi: "Hợp đồng lao động mấy năm?", situation: "informal"}
  ],
  relatedTerms: ["노동법", "계약서", "근로자 권리"],
  difficulty: "beginner",
  frequency: 5,
  formalLevel: "formal"
}
];

const filtered = terms.filter(t => !existingSlugs.has(t.slug));
console.log(`Batch 3: adding ${filtered.length}`);
const result = [...existing, ...filtered];
fs.writeFileSync(path, JSON.stringify(result, null, 2), 'utf8');
console.log(`Final total: ${result.length}`);
