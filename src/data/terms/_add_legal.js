const fs = require('fs');
const path = '/Users/mac/Documents/claude_code/projects/hanbe-interpreter/phiennoi-platform/src/data/terms/legal.json';
const existing = JSON.parse(fs.readFileSync(path, 'utf8'));
const existingSlugs = new Set(existing.map(e => e.slug));

const newTerms = [
// === WORD (30) ===
{
  slug: "luat-su-2",
  korean: "변호사",
  vietnamese: "luật sư",
  hanja: "辯護士",
  hanjaReading: "변(말씀 변) + 호(지킬 호) + 사(선비 사)",
  termType: "word",
  meaningKo: "법률 전문 자격을 갖추고 의뢰인의 법적 권리를 대리하여 보호하는 전문직으로, 소송 대리, 법률 자문, 계약서 검토 등의 업무를 수행합니다. 베트남에서는 luật sư 자격을 취득하려면 법학 학위와 실무 수습이 필요합니다.",
  meaningVi: "Người có chuyên môn pháp luật, đại diện và bảo vệ quyền lợi hợp pháp của thân chủ trong các vấn đề pháp lý, bao gồm tố tụng, tư vấn pháp luật và soạn thảo hợp đồng. Tại Việt Nam, muốn trở thành luật sư phải có bằng cử nhân luật và thực tập nghề.",
  pronunciation: "루엇 쓰",
  commonMistakes: ["luật sư와 chuyên viên pháp lý(법무사)를 혼동하는 경우가 많음", "변호사를 '법률가'로 통역하면 정확도가 떨어짐", "luật sư의 성조를 잘못 발음하면 다른 단어로 들릴 수 있음"],
  culturalNote: "베트남 진출 한국 기업은 한국어 가능한 베트남 변호사를 선호하며, 호치민과 하노이에 한국어 가능 로펌이 다수 있습니다.",
  context: "법률 상담, 소송 대리, 계약 검토",
  examples: [
    {ko: "변호사를 선임해야 합니다.", vi: "Cần thuê luật sư.", situation: "formal"},
    {ko: "변호사한테 먼저 물어보고 결정하자.", vi: "Hỏi luật sư trước rồi hãy quyết định.", situation: "onsite"},
    {ko: "우리 변호사 누구야? 연락처 좀.", vi: "Luật sư của mình là ai? Cho số liên lạc đi.", situation: "informal"}
  ],
  relatedTerms: ["소송", "법원", "계약서"],
  difficulty: "beginner",
  frequency: 5,
  formalLevel: "formal"
},
{
  slug: "toa-an",
  korean: "법원",
  vietnamese: "tòa án",
  hanja: "法院",
  hanjaReading: "법(법 법) + 원(집 원)",
  termType: "word",
  meaningKo: "법률에 따라 분쟁을 해결하고 판결을 내리는 국가 사법 기관으로, 민사·형사·행정 사건을 관할합니다. 베트남은 최고인민법원을 정점으로 3심 제도를 운영하며, 한국과 유사한 사법 체계를 갖추고 있습니다.",
  meaningVi: "Cơ quan tư pháp của nhà nước có thẩm quyền giải quyết tranh chấp và đưa ra phán quyết theo pháp luật, bao gồm các vụ dân sự, hình sự và hành chính. Việt Nam áp dụng chế độ ba cấp xét xử với Tòa án nhân dân tối cao đứng đầu.",
  pronunciation: "또아 안",
  commonMistakes: ["tòa án을 tòa nhà(건물)와 혼동하지 않도록 주의", "법원과 검찰을 구분하지 못하는 경우가 있음", "지방법원(tòa án cấp huyện)과 고등법원(tòa án cấp cao)의 체계 차이를 인식해야 함"],
  culturalNote: "베트남 법원은 인민법원(Tòa án nhân dân)이라는 명칭을 사용하며, 한국의 법원 명칭 체계와 다르므로 통역 시 주의가 필요합니다.",
  context: "재판, 법적 분쟁 해결",
  examples: [
    {ko: "법원에 소장을 제출했습니다.", vi: "Đã nộp đơn kiện lên tòa án.", situation: "formal"},
    {ko: "법원에서 날짜 잡혔어?", vi: "Tòa án đã ấn định ngày chưa?", situation: "onsite"},
    {ko: "법원까지 가야 되는 거야?", vi: "Phải ra tòa à?", situation: "informal"}
  ],
  relatedTerms: ["판결", "소송", "항소"],
  difficulty: "beginner",
  frequency: 5,
  formalLevel: "formal"
},
{
  slug: "phan-quyet",
  korean: "판결",
  vietnamese: "phán quyết",
  hanja: "判決",
  hanjaReading: "판(판단할 판) + 결(결정할 결)",
  termType: "word",
  meaningKo: "법원이 소송 사건에 대해 법률을 적용하여 내리는 최종적인 법적 결정을 의미합니다. 판결이 확정되면 법적 구속력을 가지며, 불복할 경우 항소할 수 있습니다. 한국과 베트남 모두 3심까지 항소가 가능합니다.",
  meaningVi: "Quyết định cuối cùng của tòa án về một vụ kiện, có hiệu lực pháp lý bắt buộc. Khi phán quyết được tuyên, các bên phải tuân thủ. Nếu không đồng ý, có thể kháng cáo lên tòa cấp trên. Cả Hàn Quốc và Việt Nam đều áp dụng chế độ ba cấp xét xử.",
  pronunciation: "판 꾸잇",
  commonMistakes: ["판결(phán quyết)과 결정(quyết định)을 혼동하는 경우가 많음", "판결문(bản án)과 판결(phán quyết)의 차이를 구분해야 함", "bản án은 서면 문서이고 phán quyết은 법적 결정 행위임"],
  culturalNote: "베트남 법원의 판결 집행은 한국과 다르게 집행기관(cơ quan thi hành án)이 별도로 존재하며, 판결 이후에도 집행까지 시간이 걸릴 수 있습니다.",
  context: "재판 결과, 법적 판단",
  examples: [
    {ko: "법원이 원고 승소 판결을 내렸습니다.", vi: "Tòa án đã phán quyết nguyên đơn thắng kiện.", situation: "formal"},
    {ko: "판결 나왔어? 결과가 어떻게 됐어?", vi: "Phán quyết ra rồi à? Kết quả thế nào?", situation: "onsite"},
    {ko: "판결이 좀 억울한데 항소할까?", vi: "Phán quyết hơi oan, có nên kháng cáo không?", situation: "informal"}
  ],
  relatedTerms: ["항소", "소송", "법원"],
  difficulty: "intermediate",
  frequency: 4,
  formalLevel: "formal"
},
{
  slug: "khang-cao-2",
  korean: "항소",
  vietnamese: "kháng cáo",
  hanja: "抗訴",
  hanjaReading: "항(대항할 항) + 소(호소할 소)",
  termType: "word",
  meaningKo: "1심 판결에 불복하여 상급 법원에 재심리를 요청하는 법적 절차입니다. 항소 기간은 판결 선고일로부터 일정 기간 내에 제기해야 하며, 한국은 2주, 베트남은 15일 이내입니다. 항소심에서 원심이 유지되거나 변경될 수 있습니다.",
  meaningVi: "Thủ tục pháp lý yêu cầu tòa án cấp trên xét xử lại khi không đồng ý với phán quyết sơ thẩm. Thời hạn kháng cáo tại Hàn Quốc là 2 tuần, tại Việt Nam là 15 ngày kể từ ngày tuyên án. Tòa phúc thẩm có thể giữ nguyên hoặc thay đổi bản án sơ thẩm.",
  pronunciation: "캉 까오",
  commonMistakes: ["항소(kháng cáo)와 상고(kháng nghị/giám đốc thẩm)를 혼동", "kháng cáo를 '반대하다(phản đối)'로 단순 통역하면 안 됨", "항소 기간이 한국과 베트남에서 다르다는 점을 놓치는 경우가 있음"],
  culturalNote: "베트남에서 항소는 kháng cáo(당사자)와 kháng nghị(검찰)로 구분되며, 한국과 달리 검찰도 민사 사건에 개입할 수 있는 경우가 있습니다.",
  context: "불복 절차, 상급 법원 심리",
  examples: [
    {ko: "1심 판결에 불복하여 항소합니다.", vi: "Kháng cáo bản án sơ thẩm vì không đồng ý.", situation: "formal"},
    {ko: "항소할 거야? 비용이 많이 드는데.", vi: "Có kháng cáo không? Tốn nhiều chi phí lắm.", situation: "onsite"},
    {ko: "항소 기간 놓치면 안 돼, 빨리 결정해.", vi: "Không được bỏ lỡ thời hạn kháng cáo, quyết định nhanh đi.", situation: "informal"}
  ],
  relatedTerms: ["판결", "소송", "법원"],
  difficulty: "intermediate",
  frequency: 3,
  formalLevel: "formal"
},
{
  slug: "van-ban-hop-dong",
  korean: "계약서",
  vietnamese: "văn bản hợp đồng",
  hanja: "契約書",
  hanjaReading: "계(맺을 계) + 약(약속 약) + 서(글 서)",
  termType: "word",
  meaningKo: "당사자 간 합의된 권리와 의무를 문서로 작성한 법적 효력을 가진 공식 서류입니다. 계약의 대상, 가격, 기간, 위반 시 제재, 분쟁 해결 방법 등을 명시합니다. 한-베 비즈니스에서는 이중 언어 계약서가 일반적입니다.",
  meaningVi: "Văn bản chính thức ghi nhận quyền và nghĩa vụ đã thỏa thuận giữa các bên, có hiệu lực pháp lý. Nội dung bao gồm đối tượng hợp đồng, giá cả, thời hạn, chế tài vi phạm và phương thức giải quyết tranh chấp. Trong kinh doanh Hàn-Việt, hợp đồng song ngữ là phổ biến.",
  pronunciation: "반 반 헙 동",
  commonMistakes: ["계약(hợp đồng)과 계약서(văn bản hợp đồng)를 혼동", "hợp đồng만으로도 계약서를 의미할 수 있어 문맥 파악 필요", "계약서와 합의서(biên bản thỏa thuận)의 법적 효력 차이를 인식해야 함"],
  culturalNote: "한국과 베트남 모두 계약서에 법인 도장(con dấu)을 찍는 문화가 있으며, 도장이 없으면 효력이 인정되지 않는 경우가 많습니다.",
  context: "비즈니스 협약, 법률 문서 작성",
  examples: [
    {ko: "계약서 초안을 검토해 주십시오.", vi: "Xin vui lòng xem xét bản thảo hợp đồng.", situation: "formal"},
    {ko: "계약서 내용 좀 수정해야 할 것 같은데.", vi: "Hình như cần sửa nội dung hợp đồng.", situation: "onsite"},
    {ko: "계약서 아직 안 받았어?", vi: "Chưa nhận được hợp đồng à?", situation: "informal"}
  ],
  relatedTerms: ["공증", "위임장", "합의"],
  difficulty: "beginner",
  frequency: 5,
  formalLevel: "document"
},
{
  slug: "cong-chung-2",
  korean: "공증",
  vietnamese: "công chứng",
  hanja: "公證",
  hanjaReading: "공(공정할 공) + 증(증명할 증)",
  termType: "word",
  meaningKo: "공증인이 문서의 진정성, 서명의 진위, 법률행위의 적법성을 공적으로 증명하는 절차입니다. 공증된 문서는 법적 증거력이 강화되며, 한-베 비즈니스에서 계약서, 위임장, 번역문 등의 공증이 자주 필요합니다.",
  meaningVi: "Thủ tục mà công chứng viên xác nhận tính xác thực của văn bản, chữ ký và tính hợp pháp của hành vi pháp lý. Văn bản đã công chứng có giá trị chứng cứ mạnh hơn. Trong kinh doanh Hàn-Việt, công chứng hợp đồng, giấy ủy quyền và bản dịch rất phổ biến.",
  pronunciation: "꽁 쯩",
  commonMistakes: ["공증(công chứng)과 인증(chứng thực)을 혼동", "공증 사무소(văn phòng công chứng)와 법원을 같은 곳으로 오해", "베트남의 공증 절차가 한국과 다르다는 점을 인식해야 함"],
  culturalNote: "베트남에서는 공증 사무소(văn phòng công chứng)가 민영화되어 있으며, 한국의 공증인과 역할이 유사하지만 절차와 비용이 다릅니다.",
  context: "문서 인증, 법적 증명",
  examples: [
    {ko: "이 서류는 공증이 필요합니다.", vi: "Tài liệu này cần được công chứng.", situation: "formal"},
    {ko: "공증 받으러 같이 가자.", vi: "Đi công chứng cùng nhé.", situation: "onsite"},
    {ko: "공증 비용이 얼마나 해?", vi: "Chi phí công chứng bao nhiêu?", situation: "informal"}
  ],
  relatedTerms: ["계약서", "위임장", "인감"],
  difficulty: "intermediate",
  frequency: 4,
  formalLevel: "formal"
},
{
  slug: "con-dau",
  korean: "인감",
  vietnamese: "con dấu",
  hanja: "印鑑",
  hanjaReading: "인(도장 인) + 감(거울 감)",
  termType: "word",
  meaningKo: "법인이나 개인의 공식적인 도장으로, 법률 문서나 계약서에 날인하여 문서의 진정성과 효력을 증명합니다. 한국에서는 인감증명서 제도가 있으며, 베트남에서도 법인 도장(con dấu)은 필수적인 법적 요소입니다.",
  meaningVi: "Con dấu chính thức của pháp nhân hoặc cá nhân, được đóng trên văn bản pháp lý và hợp đồng để chứng minh tính xác thực và hiệu lực. Tại Hàn Quốc có chế độ giấy chứng nhận con dấu, tại Việt Nam con dấu pháp nhân cũng là yếu tố pháp lý bắt buộc.",
  pronunciation: "꼰 저우",
  commonMistakes: ["인감(con dấu)과 서명(chữ ký)의 법적 효력 차이를 혼동", "con dấu를 '스탬프(tem)'로 통역하면 법적 의미가 사라짐", "한국의 인감증명서 제도는 베트남에 없으므로 설명이 필요함"],
  culturalNote: "한국과 베트남 모두 도장 문화가 강하지만, 한국은 인감증명서가 필요한 반면 베트남은 도장 등록증(giấy đăng ký mẫu dấu)이 필요합니다.",
  context: "문서 날인, 법인 인증",
  examples: [
    {ko: "법인 인감을 날인해 주십시오.", vi: "Xin đóng dấu pháp nhân.", situation: "formal"},
    {ko: "인감 가져왔어? 여기 찍어야 해.", vi: "Mang con dấu theo chưa? Phải đóng ở đây.", situation: "onsite"},
    {ko: "인감 없으면 서명으로 되나?", vi: "Không có con dấu thì ký tên được không?", situation: "informal"}
  ],
  relatedTerms: ["공증", "계약서", "법인설립"],
  difficulty: "intermediate",
  frequency: 3,
  formalLevel: "formal"
},
{
  slug: "giay-uy-quyen-2",
  korean: "위임장",
  vietnamese: "giấy ủy quyền",
  hanja: "委任狀",
  hanjaReading: "위(맡길 위) + 임(맡길 임) + 장(문서 장)",
  termType: "word",
  meaningKo: "특정 업무나 권한을 다른 사람에게 위탁한다는 내용을 담은 공식 문서입니다. 위임인과 수임인의 정보, 위임 범위, 유효기간 등을 명시하며, 공증이 필요한 경우가 많습니다. 한-베 비즈니스에서는 대리인 지정 시 필수적입니다.",
  meaningVi: "Văn bản chính thức giao phó công việc hoặc quyền hạn cho người khác thay mặt thực hiện. Phải ghi rõ thông tin người ủy quyền, người được ủy quyền, phạm vi ủy quyền và thời hạn. Thường cần công chứng. Trong kinh doanh Hàn-Việt, đây là tài liệu bắt buộc khi chỉ định đại diện.",
  pronunciation: "저이 우이 꾸옌",
  commonMistakes: ["위임장(giấy ủy quyền)과 대리권(quyền đại diện)을 혼동", "위임장의 유효기간을 명시하지 않으면 분쟁 소지가 있음", "위임 범위가 포괄적인지 제한적인지 통역 시 구분해야 함"],
  culturalNote: "베트남에서 위임장은 반드시 공증(công chứng)을 받아야 효력이 인정되는 경우가 많으며, 한국과 달리 위임장 자체의 형식 요건이 엄격합니다.",
  context: "대리권 위탁, 권한 이양",
  examples: [
    {ko: "위임장을 작성하여 공증받아 주십시오.", vi: "Xin lập giấy ủy quyền và công chứng.", situation: "formal"},
    {ko: "위임장 없으면 대리 서명 못 해.", vi: "Không có giấy ủy quyền thì không ký thay được.", situation: "onsite"},
    {ko: "위임장 양식 어디서 받아?", vi: "Lấy mẫu giấy ủy quyền ở đâu?", situation: "informal"}
  ],
  relatedTerms: ["공증", "계약서", "인감"],
  difficulty: "intermediate",
  frequency: 4,
  formalLevel: "document"
},
{
  slug: "quyen-so-huu",
  korean: "소유권",
  vietnamese: "quyền sở hữu",
  hanja: "所有權",
  hanjaReading: "소(바 소) + 유(있을 유) + 권(권리 권)",
  termType: "word",
  meaningKo: "물건이나 재산에 대해 사용, 수익, 처분할 수 있는 법적 권리입니다. 소유권은 부동산, 동산, 지식재산 등 다양한 대상에 적용되며, 등기나 등록을 통해 공식적으로 인정됩니다. 한-베 투자에서 토지 소유권 문제는 특히 중요한 법률 이슈입니다.",
  meaningVi: "Quyền pháp lý cho phép sử dụng, hưởng lợi và định đoạt tài sản. Quyền sở hữu áp dụng cho bất động sản, động sản, tài sản trí tuệ và được công nhận thông qua đăng ký. Trong đầu tư Hàn-Việt, vấn đề quyền sở hữu đất đai là vấn đề pháp lý đặc biệt quan trọng.",
  pronunciation: "꾸옌 써 흐우",
  commonMistakes: ["소유권(quyền sở hữu)과 사용권(quyền sử dụng)을 혼동", "베트남에서 외국인 토지 소유가 불가하다는 점을 인식해야 함", "소유권 이전(chuyển nhượng quyền sở hữu)과 사용권 이전을 구분해야 함"],
  culturalNote: "베트남은 토지의 개인 소유를 인정하지 않고 사용권(quyền sử dụng đất)만 인정하므로, 한국의 소유권 개념과 근본적으로 다릅니다.",
  context: "재산권, 부동산, 투자",
  examples: [
    {ko: "소유권 이전 등기를 완료했습니다.", vi: "Đã hoàn tất đăng ký chuyển nhượng quyền sở hữu.", situation: "formal"},
    {ko: "소유권이 누구한테 있는 거야?", vi: "Quyền sở hữu thuộc về ai?", situation: "onsite"},
    {ko: "소유권 문제 때문에 계약이 안 돼.", vi: "Vì vấn đề quyền sở hữu nên không ký hợp đồng được.", situation: "informal"}
  ],
  relatedTerms: ["담보", "저당", "법인설립"],
  difficulty: "intermediate",
  frequency: 4,
  formalLevel: "formal"
},
{
  slug: "so-huu-tri-tue",
  korean: "지적재산",
  vietnamese: "sở hữu trí tuệ",
  hanja: "知的財産",
  hanjaReading: "지(알 지) + 적(과녁 적) + 재(재물 재) + 산(낳을 산)",
  termType: "word",
  meaningKo: "인간의 지적 창작 활동으로 발생하는 무형의 재산으로, 특허, 상표, 저작권, 영업비밀 등을 포괄합니다. 지적재산권은 창작자에게 독점적 사용 권리를 부여하며, 한-베 비즈니스에서 기술 이전이나 브랜드 라이선스 시 핵심적인 법률 쟁점입니다.",
  meaningVi: "Tài sản vô hình phát sinh từ hoạt động sáng tạo trí tuệ của con người, bao gồm sáng chế, nhãn hiệu, bản quyền và bí mật kinh doanh. Quyền sở hữu trí tuệ trao cho người sáng tạo quyền sử dụng độc quyền. Trong kinh doanh Hàn-Việt, đây là vấn đề pháp lý cốt lõi khi chuyển giao công nghệ.",
  pronunciation: "써 흐우 찌 뚜에",
  commonMistakes: ["지적재산(sở hữu trí tuệ)과 지식재산을 동의어로 혼용", "IP를 '인터넷 프로토콜'로 오해하는 경우가 있음", "지적재산권 침해(vi phạm quyền SHTT)와 위조(làm giả)를 구분해야 함"],
  culturalNote: "베트남에서의 지적재산권 보호는 한국보다 집행력이 약한 편이며, 한국 기업이 베트남 진출 시 상표 선등록 문제에 자주 직면합니다.",
  context: "기술 이전, 브랜드 보호, 라이선스",
  examples: [
    {ko: "지적재산권 보호 조항을 넣어야 합니다.", vi: "Cần đưa vào điều khoản bảo hộ quyền sở hữu trí tuệ.", situation: "formal"},
    {ko: "지적재산 침해 당했는데 어떻게 해?", vi: "Bị vi phạm quyền sở hữu trí tuệ thì làm sao?", situation: "onsite"},
    {ko: "지재권 등록 했어?", vi: "Đã đăng ký quyền SHTT chưa?", situation: "informal"}
  ],
  relatedTerms: ["특허", "상표", "저작권"],
  difficulty: "advanced",
  frequency: 3,
  formalLevel: "formal"
}
];

// Filter duplicates
const filtered = newTerms.filter(t => !existingSlugs.has(t.slug));
console.log(`Existing: ${existing.length}, Adding: ${filtered.length}`);
const result = [...existing, ...filtered];
fs.writeFileSync(path, JSON.stringify(result, null, 2), 'utf8');
console.log(`Total: ${result.length}`);
