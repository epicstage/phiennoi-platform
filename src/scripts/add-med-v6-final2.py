#!/usr/bin/env python3
import json, os

file_path = os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', 'data', 'terms', 'medical.json')

with open(file_path, 'r', encoding='utf-8') as f:
    data = json.load(f)

existing_slugs = {t['slug'] for t in data}

new_terms = [
    {
        "slug": "giay-ra-vien",
        "korean": "퇴원확인서",
        "vietnamese": "Giấy ra viện",
        "hanja": "退院確認書",
        "hanjaReading": "退(물러날 퇴) + 院(집 원) + 確(확실할 확) + 認(알 인) + 書(글 서)",
        "pronunciation": "저이 자 비엔",
        "meaningKo": "환자가 병원에서 퇴원할 때 발급하는 공식 문서로, 입원 기간, 진단명, 치료 내용, 퇴원 후 주의사항이 기재됩니다. 통역 시 퇴원확인서와 진단서를 혼동하지 않도록 주의해야 하며, 베트남 환자에게는 퇴원 후 외래 방문 일정, 약물 복용법, 응급 상황 시 연락처를 반드시 확인시켜야 합니다. 한국 병원은 퇴원 교육을 체계적으로 하지만 언어 장벽으로 베트남 환자가 내용을 이해하지 못하는 경우가 많으므로 통역사의 역할이 매우 중요합니다.",
        "meaningVi": "Văn bản chính thức được cấp khi bệnh nhân xuất viện, ghi rõ thời gian nằm viện, chẩn đoán, nội dung điều trị và lưu ý sau khi ra viện. Cần phân biệt với giấy chẩn đoán. Bệnh nhân Việt Nam cần được hướng dẫn rõ về lịch tái khám, cách uống thuốc và số liên lạc khi khẩn cấp.",
        "context": "퇴원 절차, 의료행정, 보험 청구",
        "culturalNote": "한국 병원은 퇴원 시 간호사가 퇴원 교육을 실시하고 퇴원요약서를 발급하지만, 외국인 환자의 경우 언어 문제로 충분히 이해하지 못하는 경우가 많습니다. 베트남에서는 퇴원 절차가 비교적 간단하고 서류가 적지만, 한국에서는 퇴원확인서, 진료비계산서, 처방전 등 여러 서류를 받아야 하므로 통역사가 서류 확인을 도와야 합니다.",
        "commonMistakes": [
            {"mistake": "Giấy chẩn đoán", "correction": "Giấy ra viện (퇴원확인서)", "explanation": "진단서와 퇴원확인서는 다른 문서입니다"},
            {"mistake": "퇴원 후 주의사항을 전달하지 않음", "correction": "약물, 식이, 활동 제한, 재방문 일정 모두 안내", "explanation": "퇴원 교육이 재입원 방지에 핵심적입니다"},
            {"mistake": "서류를 확인하지 않고 퇴원", "correction": "퇴원확인서, 처방전, 진료비영수증 모두 확인", "explanation": "보험 청구와 사후관리에 필요한 서류입니다"}
        ],
        "examples": [
            {"ko": "퇴원확인서를 발급해 드리겠습니다", "vi": "Chúng tôi sẽ cấp giấy ra viện cho bạn", "situation": "formal"},
            {"ko": "퇴원 후 2주 후에 외래 방문하세요", "vi": "Sau khi ra viện, hãy đến khám lại sau 2 tuần", "situation": "onsite"},
            {"ko": "이 서류는 보험 청구 시 필요하니 잘 보관하세요", "vi": "Giấy này cần khi yêu cầu bảo hiểm, hãy giữ cẩn thận", "situation": "informal"}
        ],
        "relatedTerms": ["퇴원", "진단서", "진료비영수증"]
    },
    {
        "slug": "tien-su-benh",
        "korean": "병력(기왕력)",
        "vietnamese": "Tiền sử bệnh",
        "hanja": "病歷",
        "hanjaReading": "病(병 병) + 歷(지날 력)",
        "pronunciation": "띠엔 쓰 벵",
        "meaningKo": "환자가 과거에 앓았던 질병, 수술 이력, 알레르기 반응, 가족력 등의 의료 기록을 의미합니다. 통역 시 병력 청취는 정확한 진단의 기초이므로, 환자의 과거 질병, 수술 경험, 복용 약물, 알레르기, 가족 질환 이력을 빠짐없이 전달해야 합니다. 베트남 환자는 자신의 병력을 정확히 기억하지 못하거나, 정신질환이나 성병 등을 숨기려는 경향이 있어 통역사가 편안한 분위기에서 솔직한 답변을 유도하는 것이 중요합니다.",
        "meaningVi": "Hồ sơ y tế về các bệnh đã mắc, lịch sử phẫu thuật, phản ứng dị ứng, tiền sử gia đình của bệnh nhân. Khai thác tiền sử bệnh là nền tảng cho chẩn đoán chính xác, cần truyền đạt đầy đủ bệnh trong quá khứ, kinh nghiệm phẫu thuật, thuốc đang dùng, dị ứng và tiền sử bệnh gia đình.",
        "context": "초진, 응급진료, 수술 전 상담",
        "culturalNote": "한국 병원은 초진 시 상세한 문진표를 작성하게 하지만 외국어 문진표가 없는 경우가 많아 통역사의 도움이 필수적입니다. 베트남 환자는 건강검진 문화가 덜 발달하여 자신의 정확한 병명이나 복용 약물을 모르는 경우가 많고, 문화적으로 정신질환이나 성병 이력을 숨기려 하므로 비밀 보장을 강조하여 솔직한 답변을 유도해야 합니다.",
        "commonMistakes": [
            {"mistake": "Lịch sử bệnh", "correction": "Tiền sử bệnh (의학 용어)", "explanation": "'역사'가 아닌 '전력'이라는 의학 전문 용어를 써야 합니다"},
            {"mistake": "가족력을 빠뜨림", "correction": "개인 병력과 가족 병력(tiền sử gia đình) 모두 확인", "explanation": "유전적 요인이 진단에 중요합니다"},
            {"mistake": "환자가 숨기는 정보를 묻지 않음", "correction": "비밀 보장 설명 후 정신건강, 음주, 흡연 등 확인", "explanation": "정확한 진단을 위해 모든 정보가 필요합니다"}
        ],
        "examples": [
            {"ko": "과거에 큰 병이나 수술을 받은 적이 있으세요?", "vi": "Trước đây anh/chị có bị bệnh nặng hay phẫu thuật không?", "situation": "formal"},
            {"ko": "현재 복용 중인 약이 있으면 알려주세요", "vi": "Nếu đang uống thuốc gì, xin cho biết", "situation": "onsite"},
            {"ko": "가족 중에 암이나 당뇨 환자가 있나요?", "vi": "Trong gia đình có ai bị ung thư hoặc tiểu đường không?", "situation": "formal"}
        ],
        "relatedTerms": ["문진", "초진", "가족력"]
    }
]

filtered = [t for t in new_terms if t['slug'] not in existing_slugs]
data.extend(filtered)

with open(file_path, 'w', encoding='utf-8') as f:
    json.dump(data, f, ensure_ascii=False, indent=2)

print(f"Added {len(filtered)} terms. Total: {len(data)}")
