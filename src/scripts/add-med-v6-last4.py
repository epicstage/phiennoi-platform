#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Final 4 medical terms to reach 1000"""
import json, os

file_path = os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', 'data', 'terms', 'medical.json')

with open(file_path, 'r', encoding='utf-8') as f:
    data = json.load(f)

existing_slugs = {t['slug'] for t in data}

new_terms = [
    {
        "slug": "phau-thuat-tham-my",
        "korean": "성형수술",
        "vietnamese": "Phẫu thuật thẩm mỹ",
        "hanja": "成形手術",
        "hanjaReading": "成(이룰 성) + 形(모양 형) + 手(손 수) + 術(재주 술)",
        "pronunciation": "퍼우 투엣 탐 미",
        "meaningKo": "외모 개선이나 기능 회복을 목적으로 신체 부위를 수술하는 의료 행위입니다. 통역 시 '미용 목적 성형'과 '재건 목적 성형'을 구분해야 하며, 한국은 성형수술이 매우 발달하여 의료관광의 핵심 분야입니다. 베트남에서도 한국 성형에 대한 관심이 높지만, 수술 위험성과 부작용, 사후관리의 중요성을 정확히 전달해야 합니다. 특히 비보험 항목이므로 비용 상담을 철저히 해야 분쟁을 예방할 수 있습니다.",
        "meaningVi": "Hành vi y tế phẫu thuật các bộ phận cơ thể nhằm mục đích cải thiện ngoại hình hoặc phục hồi chức năng. Ở Hàn Quốc, phẫu thuật thẩm mỹ rất phát triển và là lĩnh vực chính của du lịch y tế. Cần phân biệt rõ phẫu thuật vì mục đích thẩm mỹ và phẫu thuật tái tạo. Đây là hạng mục không được bảo hiểm nên cần tư vấn chi phí kỹ lưỡng.",
        "context": "성형외과, 의료관광, 미용의료",
        "culturalNote": "한국은 세계 성형수술 수도로 불리며 강남 일대에 성형외과가 밀집해 있습니다. 베트남인들도 한국 성형을 선호하지만 언어 장벽, 부작용 시 대응, 귀국 후 사후관리가 문제입니다. 통역 시 수술 전 충분한 상담, 의사 자격 확인, 수술 동의서 내용을 꼼꼼히 전달해야 하며, '저렴한 성형 패키지'에 현혹되지 않도록 주의를 줘야 합니다.",
        "commonMistakes": [
            {"mistake": "Giải phẫu thẩm mỹ", "correction": "Phẫu thuật thẩm mỹ", "explanation": "'giải phẫu'는 해부학을 의미하므로 수술은 'phẫu thuật'입니다"},
            {"mistake": "미용과 재건을 구분하지 않음", "correction": "Thẩm mỹ (미용) vs Tái tạo (재건) 구분", "explanation": "보험 적용 여부와 의학적 필요성이 다릅니다"},
            {"mistake": "부작용 가능성을 축소", "correction": "감염, 비대칭, 감각이상 등 부작용 정확히 안내", "explanation": "환자가 충분한 정보를 바탕으로 결정해야 합니다"}
        ],
        "examples": [
            {"ko": "성형수술 전 충분한 상담을 받으세요", "vi": "Hãy tư vấn kỹ trước khi phẫu thuật thẩm mỹ", "situation": "formal"},
            {"ko": "수술 후 붓기가 빠지려면 2주 정도 걸려요", "vi": "Sau phẫu thuật, sưng sẽ giảm trong khoảng 2 tuần", "situation": "onsite"},
            {"ko": "이 수술은 비보험이라 전액 본인 부담입니다", "vi": "Phẫu thuật này không được bảo hiểm nên phải tự trả toàn bộ", "situation": "formal"}
        ],
        "relatedTerms": ["의료관광", "미용시술", "보형물"]
    },
    {
        "slug": "xet-nghiem-di-ung",
        "korean": "알레르기검사",
        "vietnamese": "Xét nghiệm dị ứng",
        "hanja": None,
        "hanjaReading": None,
        "pronunciation": "셋 응이엠 지 응",
        "meaningKo": "특정 물질에 대한 면역 반응 여부를 확인하는 검사로, 피부반응검사(skin prick test)와 혈액검사(IgE 측정)가 있습니다. 통역 시 알레르기와 과민반응을 구분하고, 검사 결과에 따라 원인 물질 회피, 약물 치료, 면역요법 등의 치료 방향이 달라짐을 설명해야 합니다. 한국에서는 약물 알레르기 확인이 수술 전 필수이며, 베트남 환자가 자신의 알레르기 이력을 정확히 전달하지 못하면 위험할 수 있으므로 통역 시 세심한 확인이 필요합니다.",
        "meaningVi": "Xét nghiệm xác nhận phản ứng miễn dịch đối với các chất cụ thể, bao gồm test da (skin prick test) và xét nghiệm máu (đo IgE). Kết quả giúp xác định hướng điều trị: tránh chất gây dị ứng, dùng thuốc hoặc liệu pháp miễn dịch. Tại Hàn Quốc, xác nhận dị ứng thuốc là bắt buộc trước phẫu thuật.",
        "context": "알레르기내과, 수술 전 검사, 소아과",
        "culturalNote": "한국은 알레르기 전문의가 많고 검사 시스템이 잘 갖춰져 있지만, 베트남은 알레르기 전문 진료 인프라가 부족합니다. 한국 병원에서는 입원 시 '약물 알레르기 밴드'를 착용하게 하지만 베트남은 그런 시스템이 없어, 한국에서 치료받는 베트남 환자에게 알레르기 이력 확인의 중요성을 반드시 교육해야 합니다.",
        "commonMistakes": [
            {"mistake": "Dị ứng과 과민반응을 혼동", "correction": "Dị ứng (면역 반응) vs Mẫn cảm (과민반응) 구분", "explanation": "의학적으로 다른 기전이므로 구분이 필요합니다"},
            {"mistake": "알레르기를 Bị ngứa로만 설명", "correction": "Dị ứng (전신 반응 포함)", "explanation": "가려움만이 아니라 아나필락시스 등 심각한 반응도 포함됩니다"},
            {"mistake": "약물 알레르기 이력을 확인하지 않음", "correction": "반드시 과거 약물 알레르기 이력 확인", "explanation": "생명에 관련될 수 있는 중요 정보입니다"}
        ],
        "examples": [
            {"ko": "수술 전 약물 알레르기 검사를 해야 합니다", "vi": "Trước phẫu thuật phải xét nghiệm dị ứng thuốc", "situation": "formal"},
            {"ko": "어떤 약이나 음식에 알레르기가 있으세요?", "vi": "Anh/chị có bị dị ứng thuốc hay thức ăn gì không?", "situation": "onsite"},
            {"ko": "알레르기 검사 결과 집먼지진드기에 양성 반응입니다", "vi": "Kết quả xét nghiệm dị ứng dương tính với mạt bụi nhà", "situation": "formal"}
        ],
        "relatedTerms": ["아나필락시스", "면역요법", "항히스타민제"]
    },
    {
        "slug": "phuc-hoi-sau-phau-thuat",
        "korean": "수술후회복",
        "vietnamese": "Phục hồi sau phẫu thuật",
        "hanja": "手術後回復",
        "hanjaReading": "手(손 수) + 術(재주 술) + 後(뒤 후) + 回(돌아올 회) + 復(다시 복)",
        "pronunciation": "푹 호이 사우 퍼우 투엣",
        "meaningKo": "수술 후 환자가 정상적인 신체 기능과 일상생활로 돌아가기 위한 회복 과정입니다. 통역 시 수술 후 주의사항(상처 관리, 약물 복용, 활동 제한, 식이 조절)을 정확히 전달하는 것이 매우 중요합니다. 한국은 수술 후 회복 프로그램이 체계적이지만 베트남 환자가 지시를 오해하면 합병증이 발생할 수 있으므로, 퇴원 시 주의사항을 문서로 번역하여 제공하는 것이 좋습니다.",
        "meaningVi": "Quá trình phục hồi để bệnh nhân trở lại chức năng cơ thể bình thường và sinh hoạt hàng ngày sau phẫu thuật. Bao gồm chăm sóc vết thương, uống thuốc đúng cách, hạn chế vận động và điều chỉnh chế độ ăn. Tại Hàn Quốc, chương trình phục hồi sau phẫu thuật được tổ chức có hệ thống.",
        "context": "외과, 재활의학, 퇴원 교육",
        "culturalNote": "한국 병원은 '조기 회복 프로그램(ERAS)'을 도입하여 수술 후 빠른 회복을 돕지만, 베트남은 이런 프로그램이 부족합니다. 한국에서는 수술 후 간호사가 체계적으로 회복 지도를 하지만, 베트남 환자는 보호자에게 의존하는 경향이 강합니다. 통역 시 회복 단계별 주의사항과 응급 상황 시 대처 방법을 명확히 안내해야 합니다.",
        "commonMistakes": [
            {"mistake": "Nghỉ ngơi sau mổ", "correction": "Phục hồi sau phẫu thuật (체계적 과정)", "explanation": "단순 휴식이 아닌 체계적 회복 과정입니다"},
            {"mistake": "수술 후 무조건 안정만 취함", "correction": "조기 보행 등 적극적 회복이 필요", "explanation": "과도한 안정은 오히려 회복을 지연시킵니다"},
            {"mistake": "퇴원 후 관리를 소홀히 함", "correction": "퇴원 후에도 지침 준수 필요", "explanation": "퇴원 후 합병증 예방이 중요합니다"}
        ],
        "examples": [
            {"ko": "수술 후 6시간 지나면 물을 드실 수 있습니다", "vi": "Sau phẫu thuật 6 tiếng có thể uống nước", "situation": "onsite"},
            {"ko": "회복을 위해 다음 날부터 걸으세요", "vi": "Để phục hồi, hãy bắt đầu đi từ ngày hôm sau", "situation": "formal"},
            {"ko": "수술 부위에 열감이나 고름이 나오면 즉시 오세요", "vi": "Nếu vết mổ nóng hoặc có mủ, hãy đến ngay", "situation": "onsite"}
        ],
        "relatedTerms": ["합병증", "퇴원교육", "조기보행"]
    },
    {
        "slug": "giay-chung-nhan-suc-khoe",
        "korean": "건강진단서",
        "vietnamese": "Giấy chứng nhận sức khỏe",
        "hanja": "健康診斷書",
        "hanjaReading": "健(건강할 건) + 康(편안할 강) + 診(진찰할 진) + 斷(끊을 단) + 書(글 서)",
        "pronunciation": "저이 쯩 년 숙 쾨",
        "meaningKo": "건강 상태를 증명하는 공식 문서로, 취업, 비자 발급, 입학 등에 필요합니다. 통역 시 한국의 건강진단서와 베트남의 건강진단서 양식이 다르므로, 어떤 목적의 진단서가 필요한지 정확히 확인해야 합니다. 특히 외국인 근로자의 경우 고용허가제 건강검진과 일반 건강검진을 구분해야 하며, 진단서에 포함될 검사 항목(혈액검사, 흉부X선, 약물검사 등)을 사전에 안내하여 재방문을 방지해야 합니다.",
        "meaningVi": "Văn bản chính thức chứng nhận tình trạng sức khỏe, cần thiết cho việc xin việc, cấp visa, nhập học. Ở Hàn Quốc và Việt Nam có mẫu giấy khác nhau nên cần xác nhận mục đích sử dụng. Đối với lao động nước ngoài, cần phân biệt khám sức khỏe theo chế độ cấp phép lao động và khám sức khỏe thông thường.",
        "context": "직업건강, 출입국관리, 의료행정",
        "culturalNote": "한국에서 외국인 근로자는 입국 시와 매년 건강검진을 받아야 하며, 특정 감염병(HIV, 매독 등) 양성 시 체류에 영향을 받을 수 있습니다. 베트남 근로자들은 이 사실을 모르는 경우가 많아, 통역 시 검진 의무와 결과에 따른 영향을 명확히 안내해야 합니다. 건강진단서는 병원 직인이 필수이며, 영문 또는 한국어 작성이 원칙입니다.",
        "commonMistakes": [
            {"mistake": "Giấy khám sức khỏe", "correction": "Giấy chứng nhận sức khỏe (공식 문서)", "explanation": "단순 건강검진이 아닌 공식 증명서입니다"},
            {"mistake": "목적을 확인하지 않고 발급 요청", "correction": "취업용, 비자용, 운전면허용 구분 필요", "explanation": "목적에 따라 포함 항목이 다릅니다"},
            {"mistake": "영문 발급을 요청하지 않음", "correction": "외국 제출용은 영문 병기 필요", "explanation": "베트남 제출 시 영문 또는 베트남어 번역 공증 필요"}
        ],
        "examples": [
            {"ko": "취업용 건강진단서를 발급받으려면 어떤 검사를 해야 하나요?", "vi": "Để được cấp giấy chứng nhận sức khỏe xin việc thì cần làm những xét nghiệm gì?", "situation": "formal"},
            {"ko": "건강진단서는 영문으로 발급해 드릴게요", "vi": "Giấy chứng nhận sức khỏe sẽ được cấp bằng tiếng Anh", "situation": "onsite"},
            {"ko": "이 진단서는 발급일로부터 3개월간 유효합니다", "vi": "Giấy chứng nhận này có hiệu lực 3 tháng kể từ ngày cấp", "situation": "formal"}
        ],
        "relatedTerms": ["건강검진", "진단서", "의무기록"]
    }
]

filtered = [t for t in new_terms if t['slug'] not in existing_slugs]
data.extend(filtered)

with open(file_path, 'w', encoding='utf-8') as f:
    json.dump(data, f, ensure_ascii=False, indent=2)

print(f"Added {len(filtered)} terms. Total: {len(data)}")
