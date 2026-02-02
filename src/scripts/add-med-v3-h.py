#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
의료 도메인 신규 용어 추가 스크립트 v3-h
20개 의료 관련 신규 용어 (서류, 절차, 안전, 의료관광 등)
"""

import json
import os

# 파일 경로 설정
file_path = os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', 'data', 'terms', 'medical.json')

# 기존 데이터 로드
with open(file_path, 'r', encoding='utf-8') as f:
    data = json.load(f)  # data is a LIST

# 기존 slug 추출
existing_slugs = {t['slug'] for t in data}

# 신규 용어 20개 (Tier S 품질)
new_terms = [
    {
        "slug": "giay-dong-y-phau-thuat",
        "korean": "수술동의서",
        "vietnamese": "giấy đồng ý phẫu thuật",
        "hanja": "手術同意書",
        "hanjaReading": "수(손 수) + 술(재주 술) + 동(한가지 동) + 의(뜻 의) + 서(글 서)",
        "pronunciation": "su-sul-dong-ui-seo",
        "meaningKo": "환자가 수술을 받기 전에 수술의 목적, 방법, 위험성, 합병증 등을 충분히 설명 듣고 자발적으로 동의한다는 문서입니다. 통역 시 주의할 점은 환자가 내용을 완전히 이해했는지 재확인하는 것이 중요하며, 법적 효력이 있는 문서이므로 모든 항목을 정확히 번역해야 합니다. 서명 전 환자에게 질문할 기회를 충분히 주어야 하며, 가족 동의가 필요한 경우도 있음을 설명해야 합니다.",
        "meaningVi": "Văn bản xác nhận bệnh nhân đã được giải thích đầy đủ về mục đích, phương pháp, nguy cơ, biến chứng của phẫu thuật và tự nguyện đồng ý thực hiện. Đây là tài liệu có giá trị pháp lý quan trọng trong quy trình y tế tại Hàn Quốc.",
        "context": "수술 전 필수 절차, 의료 법적 문서",
        "culturalNote": "한국에서는 수술동의서가 법적으로 필수이며, 환자 본인이 서명할 수 없는 경우 법정대리인이나 가족이 대신 서명합니다. 베트남과 달리 매우 상세한 위험 설명이 포함되며, 거부권도 명시됩니다. 외국인 환자의 경우 모국어 통역사를 통한 설명이 권장됩니다.",
        "commonMistakes": [
            {
                "mistake": "'동의서'를 'giấy cam kết'(서약서)로 번역",
                "correction": "'giấy đồng ý'(동의서)가 정확",
                "explanation": "서약서는 일방적 약속이지만, 동의서는 충분한 설명 후 자발적 동의를 의미합니다"
            },
            {
                "mistake": "수술 위험 설명을 완화해서 통역",
                "correction": "의료진이 설명한 모든 위험을 정확히 전달",
                "explanation": "법적 보호를 위해 환자가 모든 위험을 이해했음을 증명해야 합니다"
            },
            {
                "mistake": "가족 동의 조항을 생략",
                "correction": "한국은 가족 동의가 필요한 경우가 많음을 설명",
                "explanation": "특히 응급수술이나 고위험 수술의 경우 가족 동의가 법적으로 요구됩니다"
            }
        ],
        "examples": [
            {
                "ko": "수술동의서에 서명하시기 전에 궁금한 점이 있으시면 말씀해 주세요.",
                "vi": "Trước khi ký vào giấy đồng ý phẫu thuật, nếu có thắc mắc gì xin vui lòng hỏi.",
                "situation": "formal"
            },
            {
                "ko": "보호자분도 수술동의서에 함께 서명해 주셔야 합니다.",
                "vi": "Người nhà bệnh nhân cũng cần ký vào giấy đồng ý phẫu thuật.",
                "situation": "onsite"
            },
            {
                "ko": "수술 합병증에 대해 충분히 이해하셨나요?",
                "vi": "Anh/chị đã hiểu đầy đủ về các biến chứng của phẫu thuật chưa?",
                "situation": "formal"
            }
        ],
        "relatedTerms": ["수술", "동의", "보호자", "합병증", "의료분쟁"]
    },
    {
        "slug": "giay-chan-doan",
        "korean": "진단서",
        "vietnamese": "giấy chẩn đoán",
        "hanja": "診斷書",
        "hanjaReading": "진(살필 진) + 단(끊을 단) + 서(글 서)",
        "pronunciation": "jin-dan-seo",
        "meaningKo": "의사가 환자의 질병이나 상태를 진찰하고 판단한 내용을 공식적으로 작성한 문서입니다. 보험 청구, 휴가 신청, 법적 절차 등에 필요하며, 통역 시 주의할 점은 병명의 정확한 베트남어 의학 용어를 사용해야 하며, 진단일자와 치료 기간을 명확히 구분해야 합니다. 한국에서는 진단서 발급에 수수료가 발생함을 미리 안내하는 것이 좋습니다.",
        "meaningVi": "Văn bản y tế do bác sĩ lập ra sau khi khám và chẩn đoán bệnh của bệnh nhân. Đây là giấy tờ chính thức có giá trị pháp lý, được dùng cho mục đích bảo hiểm, xin nghỉ phép, hoặc các thủ tục pháp lý khác tại Hàn Quốc.",
        "context": "의료 문서, 보험 청구, 법적 증빙",
        "culturalNote": "한국에서는 진단서가 법적 효력이 있는 공식 문서로, 의사 면허번호와 도장이 필수입니다. 베트남과 달리 진단서 발급에 통상 1만~3만원의 수수료가 발생하며, 영문 진단서는 추가 비용이 듭니다. 산재보험이나 자동차보험 청구 시 필수 서류입니다.",
        "commonMistakes": [
            {
                "mistake": "'진단서'를 'kết quả khám bệnh'(진료 결과)로 혼동",
                "correction": "'giấy chẩn đoán'이 공식 명칭",
                "explanation": "진료 결과는 비공식적이지만 진단서는 법적 효력이 있는 공식 문서입니다"
            },
            {
                "mistake": "진단서와 소견서를 구분하지 않고 번역",
                "correction": "진단서는 'giấy chẩn đoán', 소견서는 'giấy nhận định y khoa'",
                "explanation": "소견서는 의사의 의견이지만 진단서는 확정된 진단 내용입니다"
            },
            {
                "mistake": "발급 수수료 안내를 생략",
                "correction": "진단서 발급 비용이 있음을 미리 설명",
                "explanation": "베트남에서는 무료인 경우가 많아 환자가 놀랄 수 있습니다"
            }
        ],
        "examples": [
            {
                "ko": "진단서가 필요하시면 접수처에서 신청하시면 됩니다.",
                "vi": "Nếu cần giấy chẩn đoán, anh/chị vui lòng đăng ký ở quầy tiếp nhận.",
                "situation": "formal"
            },
            {
                "ko": "보험 청구용 진단서는 3일 후에 찾으실 수 있습니다.",
                "vi": "Giấy chẩn đoán để yêu cầu bồi thường bảo hiểm có thể nhận sau 3 ngày.",
                "situation": "onsite"
            },
            {
                "ko": "영문 진단서는 추가 비용이 발생합니다.",
                "vi": "Giấy chẩn đoán bằng tiếng Anh sẽ phát sinh thêm chi phí.",
                "situation": "formal"
            }
        ],
        "relatedTerms": ["진단", "소견서", "의료비영수증", "건강보험", "산재보험"]
    },
    {
        "slug": "don-thuoc-chi-tiet",
        "korean": "처방전",
        "vietnamese": "đơn thuốc chi tiết",
        "hanja": "處方箋",
        "hanjaReading": "처(처리할 처) + 방(모 방) + 전(종이 전)",
        "pronunciation": "cheo-bang-jeon",
        "meaningKo": "의사가 환자에게 필요한 약물의 종류, 용량, 복용 방법을 기록한 공식 문서로, 약국에서 약을 조제받을 때 필수입니다. 통역 시 주의사항은 약물 알레르기 정보를 정확히 전달하고, 복용 시간(식전/식후)과 용량을 명확히 설명해야 하며, 한국에서는 전문의약품은 처방전 없이 구매할 수 없음을 안내해야 합니다. 처방 기간과 재처방 가능 여부도 확인이 필요합니다.",
        "meaningVi": "Văn bản y tế do bác sĩ lập ra, ghi rõ loại thuốc, liều lượng, cách dùng cho bệnh nhân. Đây là giấy tờ bắt buộc để mua thuốc kê đơn tại nhà thuốc ở Hàn Quốc. Thông tin về dị ứng thuốc và thời gian dùng thuốc phải được ghi chép chính xác.",
        "context": "약물 처방, 약국 이용",
        "culturalNote": "한국에서는 의약분업으로 병원과 약국이 분리되어 있어, 처방전을 받아 약국에 가야 합니다. 베트남과 달리 항생제나 전문의약품은 반드시 처방전이 필요하며, 처방전 유효기간은 통상 3일입니다. 처방전 재발급 시 진료비가 다시 발생할 수 있습니다.",
        "commonMistakes": [
            {
                "mistake": "'처방전'을 단순히 'đơn thuốc'로만 번역",
                "correction": "'đơn thuốc chi tiết' 또는 'toa thuốc'로 정확히 표현",
                "explanation": "공식 처방전임을 강조하여 법적 문서임을 명확히 해야 합니다"
            },
            {
                "mistake": "식전/식후 복용을 시간으로만 통역",
                "correction": "'trước/sau bữa ăn'로 명확히 구분",
                "explanation": "약효와 부작용에 영향을 주므로 정확한 복용 시점을 전달해야 합니다"
            },
            {
                "mistake": "처방 기간과 약 복용 기간을 혼동",
                "correction": "처방전 유효기간과 약 복용 기간을 각각 설명",
                "explanation": "처방전은 3일 유효, 약 복용은 처방된 일수만큼 다를 수 있습니다"
            }
        ],
        "examples": [
            {
                "ko": "이 처방전은 3일 이내에 약국에 가져가셔야 합니다.",
                "vi": "Đơn thuốc này anh/chị phải mang đến nhà thuốc trong vòng 3 ngày.",
                "situation": "formal"
            },
            {
                "ko": "약은 하루 세 번, 식후 30분에 드세요.",
                "vi": "Thuốc uống 3 lần mỗi ngày, sau bữa ăn 30 phút.",
                "situation": "onsite"
            },
            {
                "ko": "약물 알레르ギ가 있으시면 미리 말씀해 주세요.",
                "vi": "Nếu có dị ứng thuốc, xin vui lòng thông báo trước.",
                "situation": "formal"
            }
        ],
        "relatedTerms": ["약국", "복용법", "전문의약품", "알레르기", "재처방"]
    },
    {
        "slug": "tom-tat-ra-vien",
        "korean": "퇴원요약",
        "vietnamese": "tóm tắt ra viện",
        "hanja": "退院要約",
        "hanjaReading": "퇴(물러날 퇴) + 원(집 원) + 요(요긴할 요) + 약(맺을 약)",
        "pronunciation": "toe-won-yo-yak",
        "meaningKo": "환자가 입원 기간 동안 받은 진단, 치료, 경과, 퇴원 후 주의사항 등을 요약한 의료 문서입니다. 통역 시 주의할 점은 퇴원 후 복약 지도와 생활 관리 사항을 정확히 전달해야 하며, 후속 진료 일정과 응급 상황 대처 방법을 명확히 설명해야 합니다. 건강보험 청구나 타 병원 전원 시 필수 서류이므로 분실하지 않도록 안내해야 합니다.",
        "meaningVi": "Bản tóm tắt y tế ghi lại toàn bộ quá trình chẩn đoán, điều trị, diễn biến bệnh trong thời gian nằm viện và hướng dẫn chăm sóc sau khi ra viện. Đây là tài liệu quan trọng cho việc yêu cầu bảo hiểm và chuyển viện tại Hàn Quốc.",
        "context": "퇴원 절차, 의료 기록",
        "culturalNote": "한국에서는 퇴원요약서가 건강보험 청구와 연계되어 있어 매우 중요한 문서입니다. 베트남과 달리 퇴원 당일이 아닌 3~7일 후 발급되는 경우가 많으며, 발급 수수료가 발생합니다. 외국인 근로자의 경우 본국 귀국 시 이 서류가 필요할 수 있어 보관이 중요합니다.",
        "commonMistakes": [
            {
                "mistake": "'퇴원요약'을 'giấy xuất viện'(퇴원증)로 혼동",
                "correction": "'tóm tắt ra viện'이 정확한 표현",
                "explanation": "퇴원증은 단순 퇴원 확인이지만 퇴원요약은 전체 치료 내용이 담긴 문서입니다"
            },
            {
                "mistake": "퇴원 후 주의사항을 구두로만 전달",
                "correction": "문서에 기록된 내용을 모두 읽어주고 확인",
                "explanation": "법적 책임 문제로 문서화된 지침을 정확히 전달해야 합니다"
            },
            {
                "mistake": "후속 진료 일정을 대략적으로 통역",
                "correction": "정확한 날짜와 시간, 담당 의사를 명시",
                "explanation": "후속 진료를 놓치면 치료 효과가 떨어지거나 합병증이 발생할 수 있습니다"
            }
        ],
        "examples": [
            {
                "ko": "퇴원요약서는 일주일 후에 발급됩니다.",
                "vi": "Tóm tắt ra viện sẽ được cấp sau một tuần.",
                "situation": "formal"
            },
            {
                "ko": "이 서류는 다른 병원에 갈 때 꼭 가져가세요.",
                "vi": "Khi đến bệnh viện khác, nhớ mang theo tài liệu này.",
                "situation": "onsite"
            },
            {
                "ko": "퇴원 후 2주 뒤에 외래로 다시 오셔야 합니다.",
                "vi": "Sau khi ra viện 2 tuần, anh/chị phải đến khám ngoại trú lại.",
                "situation": "formal"
            }
        ],
        "relatedTerms": ["퇴원", "입원", "외래진료", "후속치료", "의료기록"]
    },
    {
        "slug": "hoa-don-vien-phi",
        "korean": "의료비영수증",
        "vietnamese": "hóa đơn viện phí",
        "hanja": "醫療費領收證",
        "hanjaReading": "의(의원 의) + 료(치료할 료) + 비(쓸 비) + 영(받을 영) + 수(받을 수) + 증(증거 증)",
        "pronunciation": "ui-ryo-bi-yeong-su-jeung",
        "meaningKo": "병원에서 제공한 의료 서비스에 대한 비용을 상세히 기재한 공식 영수증으로, 건강보험 청구와 세금 공제에 필수적인 서류입니다. 통역 시 주의할 점은 급여 항목과 비급여 항목을 명확히 구분하여 설명해야 하며, 본인 부담금과 보험 적용 금액을 정확히 안내해야 합니다. 외국인 근로자의 경우 본국 보험 청구 시 영문 영수증이 필요할 수 있음을 알려주어야 합니다.",
        "meaningVi": "Hóa đơn chi tiết ghi rõ tất cả chi phí y tế mà bệnh nhân đã sử dụng tại bệnh viện, bao gồm phần bảo hiểm thanh toán và phần bệnh nhân tự trả. Đây là chứng từ bắt buộc để yêu cầu bảo hiểm và khấu trừ thuế tại Hàn Quốc.",
        "context": "의료비 정산, 보험 청구",
        "culturalNote": "한국의 건강보험 시스템에서는 진료비 영수증이 매우 상세하게 항목별로 구분되어 있습니다. 베트남과 달리 병원에서 직접 보험 청구를 처리하므로 환자는 본인 부담금만 지불합니다. 외국인 근로자도 입사 후 건강보험 의무 가입 대상이며, 영수증 보관으로 연말정산 시 세금 혜택을 받을 수 있습니다.",
        "commonMistakes": [
            {
                "mistake": "'의료비영수증'을 단순히 'hóa đơn'로만 번역",
                "correction": "'hóa đơn viện phí' 또는 'biên lai chi phí y tế'로 명확히",
                "explanation": "일반 영수증이 아닌 의료비 전용 영수증임을 강조해야 합니다"
            },
            {
                "mistake": "급여와 비급여 구분 없이 총액만 통역",
                "correction": "보험 적용 항목과 비적용 항목을 각각 설명",
                "explanation": "환자가 비용 구조를 이해하고 향후 의료 이용 계획을 세울 수 있습니다"
            },
            {
                "mistake": "영수증 재발급이 무료라고 안내",
                "correction": "재발급 시 수수료가 발생할 수 있음을 설명",
                "explanation": "병원마다 정책이 다르므로 확인이 필요합니다"
            }
        ],
        "examples": [
            {
                "ko": "의료비영수증은 계산하실 때 함께 드립니다.",
                "vi": "Hóa đơn viện phí sẽ được cấp khi thanh toán.",
                "situation": "formal"
            },
            {
                "ko": "건강보험이 적용되어 본인 부담금은 30%입니다.",
                "vi": "Sau khi áp dụng bảo hiểm y tế, phần tự trả là 30%.",
                "situation": "onsite"
            },
            {
                "ko": "영수증을 잘 보관하시면 연말정산에 도움이 됩니다.",
                "vi": "Nếu giữ hóa đơn cẩn thận, sẽ có lợi khi quyết toán thuế cuối năm.",
                "situation": "informal"
            }
        ],
        "relatedTerms": ["건강보험", "본인부담금", "비급여", "연말정산", "진료비"]
    },
    {
        "slug": "hang-muc-khong-bao-hiem",
        "korean": "비급여항목",
        "vietnamese": "hạng mục không bảo hiểm",
        "hanja": "非給與項目",
        "hanjaReading": "비(아닐 비) + 급(줄 급) + 여(줄 여) + 항(항목 항) + 목(눈 목)",
        "pronunciation": "bi-geup-yeo-hang-mok",
        "meaningKo": "건강보험이 적용되지 않아 환자가 전액을 부담해야 하는 진료 항목입니다. 통역 시 주의할 점은 비급여 항목은 병원마다 가격이 다를 수 있음을 설명하고, 사전에 비용을 확인할 권리가 있음을 안내해야 합니다. 미용 목적, 선택 진료, 상급 병실료 등이 대표적이며, 외국인 근로자가 예상치 못한 고액 진료비를 부담하지 않도록 사전 설명이 중요합니다.",
        "meaningVi": "Các hạng mục khám chữa bệnh không được bảo hiểm y tế Hàn Quốc chi trả, bệnh nhân phải tự thanh toán 100% chi phí. Giá cả có thể khác nhau tùy theo từng bệnh viện, bệnh nhân có quyền hỏi và xác nhận chi phí trước khi thực hiện.",
        "context": "의료비 부담, 보험 적용",
        "culturalNote": "한국 건강보험 시스템에서 비급여 항목은 투명하게 공개되어야 하며, 환자는 사전 동의 없이 비급여 진료를 받지 않을 권리가 있습니다. 베트남과 달리 비급여 항목이 세분화되어 있고, 병원은 비급여 진료 전 환자에게 비용을 고지할 의무가 있습니다. MRI, 초음파 일부, 특실료 등이 해당됩니다.",
        "commonMistakes": [
            {
                "mistake": "'비급여'를 'không được trả'(지불 안 됨)로 번역",
                "correction": "'không được bảo hiểm chi trả'(보험이 안 내줌)로 정확히",
                "explanation": "환자가 안 내는 것이 아니라 보험이 안 내주는 것임을 명확히 해야 합니다"
            },
            {
                "mistake": "모든 비급여가 필수라고 설명",
                "correction": "선택 가능한 비급여와 필수 비급여를 구분",
                "explanation": "환자가 경제 상황에 따라 선택할 수 있는 권리가 있습니다"
            },
            {
                "mistake": "비급여 가격이 고정되어 있다고 안내",
                "correction": "병원마다 가격이 다를 수 있음을 설명",
                "explanation": "비급여는 시장 가격이므로 병원 간 차이가 클 수 있습니다"
            }
        ],
        "examples": [
            {
                "ko": "이 검사는 비급여 항목이라 보험이 적용되지 않습니다.",
                "vi": "Xét nghiệm này là hạng mục không bảo hiểm nên bảo hiểm y tế không chi trả.",
                "situation": "formal"
            },
            {
                "ko": "상급 병실을 원하시면 비급여로 추가 비용이 발생합니다.",
                "vi": "Nếu muốn phòng bệnh cao cấp, sẽ phát sinh thêm chi phí không bảo hiểm.",
                "situation": "onsite"
            },
            {
                "ko": "비급여 진료를 원하지 않으시면 거부하실 수 있습니다.",
                "vi": "Nếu không muốn điều trị không bảo hiểm, anh/chị có quyền từ chối.",
                "situation": "formal"
            }
        ],
        "relatedTerms": ["건강보험", "본인부담금", "급여항목", "선택진료", "의료비"]
    },
    {
        "slug": "dac-le-tinh-phi",
        "korean": "산정특례",
        "vietnamese": "đặc lệ tính phí",
        "hanja": "算定特例",
        "hanjaReading": "산(셀 산) + 정(정할 정) + 특(특별할 특) + 례(례 례)",
        "pronunciation": "san-jeong-teuk-rye",
        "meaningKo": "암, 희귀질환, 중증난치질환 등 고액의 의료비가 지속적으로 발생하는 질환에 대해 건강보험 본인부담률을 대폭 낮춰주는 제도입니다. 통역 시 주의할 점은 신청 절차와 필요 서류를 정확히 안내하고, 적용 기간과 갱신 방법을 명확히 설명해야 합니다. 외국인 근로자도 건강보험 가입자라면 동일하게 혜택을 받을 수 있으며, 본인부담금이 5~10%로 감소함을 강조해야 합니다.",
        "meaningVi": "Chế độ đặc biệt giảm mạnh tỷ lệ chi phí tự trả của bệnh nhân đối với các bệnh cần điều trị lâu dài và tốn kém như ung thư, bệnh hiếm gặp, bệnh nan y trầm trọng. Bệnh nhân chỉ phải tự trả 5-10% thay vì 30-50% như thông thường.",
        "context": "중증질환 관리, 의료비 경감",
        "culturalNote": "한국의 산정특례 제도는 중증질환자의 경제적 부담을 크게 줄여주는 사회안전망입니다. 베트남과 달리 매우 체계적으로 운영되며, 암 환자의 경우 5년간 본인부담률 5%가 적용됩니다. 외국인 근로자도 동등하게 혜택을 받지만, 본국에서 진단받은 경우 한국 병원의 재진단이 필요할 수 있습니다.",
        "commonMistakes": [
            {
                "mistake": "'산정특례'를 'giảm giá đặc biệt'(특별 할인)로 번역",
                "correction": "'đặc lệ tính phí'(특례 산정) 또는 'chế độ hỗ trợ bệnh nặng'",
                "explanation": "단순 할인이 아닌 법적 제도임을 명확히 해야 합니다"
            },
            {
                "mistake": "자동으로 적용된다고 안내",
                "correction": "환자가 직접 신청해야 함을 강조",
                "explanation": "신청하지 않으면 혜택을 받을 수 없으므로 적극적 안내가 필요합니다"
            },
            {
                "mistake": "모든 질환에 적용된다고 설명",
                "correction": "지정된 질환 목록에만 적용됨을 명시",
                "explanation": "암, 희귀질환, 중증난치질환 등 법정 질환만 해당됩니다"
            }
        ],
        "examples": [
            {
                "ko": "암 진단을 받으셨으니 산정특례를 신청하시면 의료비가 많이 줄어듭니다.",
                "vi": "Vì được chẩn đoán ung thư, nếu đăng ký đặc lệ tính phí, chi phí y tế sẽ giảm rất nhiều.",
                "situation": "formal"
            },
            {
                "ko": "산정특례가 적용되면 본인부담금이 5%만 내시면 됩니다.",
                "vi": "Khi áp dụng đặc lệ tính phí, anh/chị chỉ phải tự trả 5%.",
                "situation": "onsite"
            },
            {
                "ko": "산정특례 등록증을 항상 지참하세요.",
                "vi": "Luôn mang theo giấy chứng nhận đăng ký đặc lệ tính phí.",
                "situation": "informal"
            }
        ],
        "relatedTerms": ["암", "희귀질환", "건강보험", "본인부담금", "중증질환"]
    },
    {
        "slug": "hoa-giai-tranh-chap-y-te",
        "korean": "의료분쟁조정",
        "vietnamese": "hòa giải tranh chấp y tế",
        "hanja": "醫療紛爭調停",
        "hanjaReading": "의(의원 의) + 료(치료할 료) + 분(어지러울 분) + 쟁(다툴 쟁) + 조(고를 조) + 정(바를 정)",
        "pronunciation": "ui-ryo-bun-jaeng-jo-jeong",
        "meaningKo": "의료사고나 의료 서비스에 대한 불만으로 환자와 의료기관 간 발생한 분쟁을 법원이 아닌 중재 기구를 통해 해결하는 제도입니다. 통역 시 주의할 점은 환자의 법적 권리를 정확히 설명하고, 조정 절차와 소요 기간을 명확히 안내해야 하며, 무료 법률 상담 서비스가 있음을 알려주어야 합니다. 외국인 근로자도 동등한 권리가 있으며, 통역 지원을 요청할 수 있음을 강조해야 합니다.",
        "meaningVi": "Chế độ giải quyết tranh chấp giữa bệnh nhân và cơ sở y tế do sự cố y tế hoặc bất mãn về dịch vụ y tế thông qua cơ quan hòa giải, không qua tòa án. Bệnh nhân nước ngoài cũng có quyền được hỗ trợ pháp lý và thông dịch miễn phí.",
        "context": "의료사고, 법적 권리",
        "culturalNote": "한국에는 '한국의료분쟁조정중재원'이라는 공적 기관이 있어 의료분쟁을 신속하고 공정하게 해결합니다. 베트남과 달리 법원 소송보다 조정을 먼저 권장하며, 조정 성공 시 소송보다 빠르고 비용이 적게 듭니다. 외국인 근로자를 위한 다국어 상담 서비스도 제공됩니다.",
        "commonMistakes": [
            {
                "mistake": "'의료분쟁'을 'tai nạn y tế'(의료사고)로만 번역",
                "correction": "'tranh chấp y tế'(의료 분쟁)가 더 넓은 개념",
                "explanation": "사고뿐 아니라 서비스 불만, 과잉 진료 등도 포함됩니다"
            },
            {
                "mistake": "반드시 소송해야 한다고 안내",
                "correction": "조정을 먼저 시도할 수 있음을 설명",
                "explanation": "조정이 더 빠르고 경제적이며, 관계 회복에도 유리합니다"
            },
            {
                "mistake": "외국인은 조정 신청이 어렵다고 설명",
                "correction": "외국인도 동등한 권리가 있으며 통역 지원이 제공됨",
                "explanation": "법적 차별이 없으며, 실제로 외국인 지원 시스템이 갖춰져 있습니다"
            }
        ],
        "examples": [
            {
                "ko": "의료사고가 발생하면 의료분쟁조정을 신청할 수 있습니다.",
                "vi": "Nếu xảy ra sự cố y tế, có thể đăng ký hòa giải tranh chấp y tế.",
                "situation": "formal"
            },
            {
                "ko": "조정 신청은 무료이며, 통역 서비스도 제공됩니다.",
                "vi": "Đăng ký hòa giải miễn phí và cũng cung cấp dịch vụ thông dịch.",
                "situation": "onsite"
            },
            {
                "ko": "소송보다 조정이 더 빠르고 비용이 적게 듭니다.",
                "vi": "Hòa giải nhanh hơn và ít tốn kém hơn so với kiện tụng.",
                "situation": "informal"
            }
        ],
        "relatedTerms": ["의료사고", "환자권리", "법적조치", "손해배상", "중재원"]
    },
    {
        "slug": "an-toan-benh-nhan",
        "korean": "환자안전",
        "vietnamese": "an toàn bệnh nhân",
        "hanja": "患者安全",
        "hanjaReading": "환(근심할 환) + 자(사람 자) + 안(편안할 안) + 전(온전할 전)",
        "pronunciation": "hwan-ja-an-jeon",
        "meaningKo": "의료 과정에서 환자에게 발생할 수 있는 위해를 예방하고, 안전한 의료 환경을 조성하기 위한 모든 활동과 시스템을 의미합니다. 통역 시 주의할 점은 환자 확인 절차(이름, 생년월일)의 중요성을 강조하고, 낙상 예방, 약물 오류 방지 등 구체적인 안전 수칙을 명확히 전달해야 합니다. 환자가 불안전한 상황을 발견하면 즉시 알릴 권리와 의무가 있음을 설명해야 합니다.",
        "meaningVi": "Tất cả các hoạt động và hệ thống nhằm ngăn ngừa tổn hại có thể xảy ra với bệnh nhân trong quá trình điều trị y tế và tạo ra môi trường y tế an toàn. Bệnh nhân có quyền và nghĩa vụ thông báo ngay khi phát hiện tình huống không an toàn.",
        "context": "병원 안전 관리, 환자 권리",
        "culturalNote": "한국 의료기관은 '환자안전법'에 따라 환자안전사고 보고 시스템을 운영하며, 환자 확인을 위해 매번 이름과 생년월일을 물어봅니다. 베트남보다 환자 확인 절차가 엄격하며, 낙상 고위험 환자에게는 노란 팔찌를 착용시킵니다. 외국인 환자의 경우 언어 장벽이 안전 위험 요소가 될 수 있어 통역이 중요합니다.",
        "commonMistakes": [
            {
                "mistake": "환자 확인 질문을 불필요한 절차로 설명",
                "correction": "환자 안전을 위한 필수 절차임을 강조",
                "explanation": "같은 이름의 환자 혼동을 방지하는 국제적 안전 기준입니다"
            },
            {
                "mistake": "'안전'을 'bảo vệ'(보호)로만 번역",
                "correction": "'an toàn'(안전)이 더 정확",
                "explanation": "보호는 수동적이지만 안전은 체계적 시스템을 의미합니다"
            },
            {
                "mistake": "환자가 수동적으로 따르기만 하면 된다고 안내",
                "correction": "환자도 안전에 적극 참여해야 함을 설명",
                "explanation": "환자가 자신의 치료 내용을 확인하고 질문하는 것이 안전의 핵심입니다"
            }
        ],
        "examples": [
            {
                "ko": "환자안전을 위해 매번 성함과 생년월일을 확인합니다.",
                "vi": "Để đảm bảo an toàn bệnh nhân, chúng tôi xác nhận tên và ngày sinh mỗi lần.",
                "situation": "formal"
            },
            {
                "ko": "화장실 갈 때는 호출벨을 눌러 도움을 요청하세요.",
                "vi": "Khi đi vệ sinh, hãy bấm chuông gọi để nhờ giúp đỡ.",
                "situation": "onsite"
            },
            {
                "ko": "약을 받으시면 이름을 꼭 확인하세요.",
                "vi": "Khi nhận thuốc, nhớ kiểm tra tên của mình.",
                "situation": "informal"
            }
        ],
        "relatedTerms": ["낙상예방", "환자확인", "투약오류", "의료사고", "안전수칙"]
    },
    {
        "slug": "kiem-soat-nhiem-khuan",
        "korean": "감염관리",
        "vietnamese": "kiểm soát nhiễm khuẩn",
        "hanja": "感染管理",
        "hanjaReading": "감(느낄 감) + 염(물들 염) + 관(다스릴 관) + 리(다스릴 리)",
        "pronunciation": "gam-yeom-gwan-ri",
        "meaningKo": "병원에서 환자, 의료진, 방문객 간 감염성 질환의 전파를 예방하고 관리하는 체계적인 활동입니다. 통역 시 주의할 점은 손 씻기, 마스크 착용, 격리 규정 등 구체적인 감염 예방 수칙을 명확히 설명해야 하며, 외국인 환자가 문화적 차이로 규칙을 어기지 않도록 배경을 설명하는 것이 중요합니다. 특히 다제내성균 감염 시 격리 조치의 필요성과 방법을 정확히 전달해야 합니다.",
        "meaningVi": "Hệ thống hoạt động có tổ chức nhằm ngăn ngừa và quản lý sự lây lan bệnh truyền nhiễm giữa bệnh nhân, nhân viên y tế và người thăm bệnh tại bệnh viện. Bao gồm các quy định về rửa tay, đeo khẩu trang, cách ly và vệ sinh môi trường.",
        "context": "병원 감염 예방, 공중보건",
        "culturalNote": "한국 병원은 감염관리에 매우 엄격하며, 전담 감염관리간호사가 배치되어 있습니다. 베트남보다 손 위생 강조가 강하고, 면회객 수 제한과 면회 시간 규정이 엄격합니다. COVID-19 이후 마스크 착용과 체온 측정이 일상화되었으며, 외국인도 예외 없이 규정을 준수해야 합니다.",
        "commonMistakes": [
            {
                "mistake": "'감염관리'를 'phòng ngừa nhiễm khuẩn'(감염 예방)로만 번역",
                "correction": "'kiểm soát nhiễm khuẩn'(감염 통제)가 더 포괄적",
                "explanation": "예방뿐 아니라 발생 후 관리, 확산 차단까지 포함됩니다"
            },
            {
                "mistake": "손 씻기를 선택 사항처럼 설명",
                "correction": "필수 규정이며 모든 접촉 전후 실시해야 함",
                "explanation": "손 위생은 가장 중요한 감염 예방 수단입니다"
            },
            {
                "mistake": "격리 조치를 처벌로 오해하게 통역",
                "correction": "환자 보호와 타인 안전을 위한 의학적 조치임을 강조",
                "explanation": "격리는 환자를 위한 것이지 처벌이 아닙니다"
            }
        ],
        "examples": [
            {
                "ko": "병실에 들어가시기 전에 반드시 손을 씻어주세요.",
                "vi": "Trước khi vào phòng bệnh, nhất định phải rửa tay.",
                "situation": "formal"
            },
            {
                "ko": "환자분은 다제내성균 감염으로 격리 치료가 필요합니다.",
                "vi": "Bệnh nhân bị nhiễm vi khuẩn kháng đa thuốc nên cần điều trị cách ly.",
                "situation": "onsite"
            },
            {
                "ko": "면회 시간 외에는 보호자도 출입이 제한됩니다.",
                "vi": "Ngoài giờ thăm bệnh, người nhà cũng bị hạn chế ra vào.",
                "situation": "formal"
            }
        ],
        "relatedTerms": ["손위생", "격리", "소독", "멸균", "원내감염"]
    },
    {
        "slug": "visa-du-lich-y-te",
        "korean": "의료관광비자",
        "vietnamese": "visa du lịch y tế",
        "hanja": "醫療觀光visa",
        "hanjaReading": "의(의원 의) + 료(치료할 료) + 관(볼 관) + 광(빛 광)",
        "pronunciation": "ui-ryo-gwan-gwang-bi-ja",
        "meaningKo": "외국인이 한국에서 의료 서비스를 받기 위해 발급받는 특별 비자로, 일반 관광비자보다 체류 기간이 길고 의료기관 이용에 특화되어 있습니다. 통역 시 주의할 점은 비자 신청 절차와 필요 서류(병원 예약 확인서, 치료 계획서 등)를 정확히 안내하고, 체류 기간 연장 조건과 방법을 명확히 설명해야 합니다. 의료관광 코디네이터를 통한 지원 서비스가 있음을 알려주면 도움이 됩니다.",
        "meaningVi": "Visa đặc biệt dành cho người nước ngoài đến Hàn Quốc để sử dụng dịch vụ y tế, có thời gian lưu trú dài hơn visa du lịch thông thường và chuyên biệt hóa cho việc sử dụng cơ sở y tế. Cần có giấy xác nhận đặt lịch khám và kế hoạch điều trị từ bệnh viện.",
        "context": "의료 관광, 비자 신청",
        "culturalNote": "한국은 의료관광 산업이 발달해 있어 전담 비자(C-3-3)가 있으며, 최대 90일 체류 가능하고 연장도 가능합니다. 베트남 환자들이 미용 성형, 건강검진, 암 치료 등을 위해 많이 방문합니다. 공항에 의료관광 전용 창구가 있고, 다국어 지원 서비스가 잘 갖춰져 있습니다.",
        "commonMistakes": [
            {
                "mistake": "'의료관광비자'를 일반 관광비자로 혼동",
                "correction": "C-3-3 특별 비자로 의료 목적이 명시되어야 함",
                "explanation": "일반 관광비자로는 장기 치료 시 체류 연장에 문제가 생길 수 있습니다"
            },
            {
                "mistake": "비자만 있으면 모든 병원 이용 가능하다고 안내",
                "correction": "비자 발급 시 명시된 병원에서만 치료 가능",
                "explanation": "비자 신청 시 지정한 의료기관 정보가 비자에 기록됩니다"
            },
            {
                "mistake": "건강보험 적용된다고 설명",
                "correction": "의료관광은 전액 본인 부담이며 보험 적용 안 됨",
                "explanation": "건강보험은 국내 거주자에게만 적용되므로 명확히 구분해야 합니다"
            }
        ],
        "examples": [
            {
                "ko": "의료관광비자를 신청하려면 병원 예약 확인서가 필요합니다.",
                "vi": "Để xin visa du lịch y tế, cần có giấy xác nhận đặt lịch khám từ bệnh viện.",
                "situation": "formal"
            },
            {
                "ko": "치료가 길어지면 비자 연장을 신청할 수 있습니다.",
                "vi": "Nếu điều trị kéo dài, có thể đăng ký gia hạn visa.",
                "situation": "onsite"
            },
            {
                "ko": "의료관광 코디네이터가 통역과 이동을 도와드립니다.",
                "vi": "Điều phối viên du lịch y tế sẽ hỗ trợ thông dịch và di chuyển.",
                "situation": "informal"
            }
        ],
        "relatedTerms": ["의료관광", "비자연장", "국제진료센터", "코디네이터", "건강검진"]
    },
    {
        "slug": "goi-kham-suc-khoe",
        "korean": "건강검진패키지",
        "vietnamese": "gói khám sức khỏe",
        "hanja": "健康檢診package",
        "hanjaReading": "건(건강할 건) + 강(강할 강) + 검(검사할 검) + 진(살필 진)",
        "pronunciation": "geon-gang-geom-jin-pae-ki-ji",
        "meaningKo": "여러 건강검진 항목을 묶어서 종합적으로 건강 상태를 확인하는 상품화된 검진 프로그램입니다. 통역 시 주의할 점은 패키지에 포함된 검사 항목과 제외된 항목을 명확히 구분하여 설명하고, 추가 검사 발생 시 비용이 발생함을 미리 안내해야 합니다. 검진 전 금식 시간, 복용 중단 약물 등 준비 사항을 정확히 전달하는 것이 중요하며, 결과 상담 일정도 확인해야 합니다.",
        "meaningVi": "Chương trình khám sức khỏe tổng hợp được sản phẩm hóa, bao gồm nhiều hạng mục kiểm tra để đánh giá toàn diện tình trạng sức khỏe. Cần phân biệt rõ các hạng mục được bao gồm và loại trừ trong gói, cũng như thông báo trước về chi phí phát sinh nếu có xét nghiệm bổ sung.",
        "context": "건강검진, 예방 의학",
        "culturalNote": "한국은 건강검진 문화가 발달해 있어 연령대별, 성별, 관심 질환별로 다양한 패키지가 있습니다. 베트남 사람들이 선호하는 암 정밀 검진, 심혈관 검진 등 특화 패키지가 많으며, 하루 만에 모든 검사를 끝낼 수 있도록 시스템화되어 있습니다. 가격은 10만원대부터 수백만원까지 다양합니다.",
        "commonMistakes": [
            {
                "mistake": "'패키지'를 'gói'로만 번역하고 내용 설명 생략",
                "correction": "포함된 검사 항목을 구체적으로 나열",
                "explanation": "환자가 어떤 검사를 받는지 정확히 알아야 준비하고 결정할 수 있습니다"
            },
            {
                "mistake": "모든 검사가 포함되어 있다고 오해하게 통역",
                "correction": "기본 패키지와 추가 옵션을 명확히 구분",
                "explanation": "추가 검사 비용 발생으로 인한 불만을 예방해야 합니다"
            },
            {
                "mistake": "검진 전 준비 사항을 대략적으로만 안내",
                "correction": "금식 시간, 중단 약물, 복장 등을 구체적으로 설명",
                "explanation": "준비가 부족하면 검사를 못 받거나 다시 와야 할 수 있습니다"
            }
        ],
        "examples": [
            {
                "ko": "기본 패키지는 30만원이고, 암 정밀 검진은 추가 옵션입니다.",
                "vi": "Gói cơ bản là 300,000 won, khám ung thư chi tiết là lựa chọn bổ sung.",
                "situation": "formal"
            },
            {
                "ko": "검진 전날 저녁 9시부터 금식해야 합니다.",
                "vi": "Phải nhịn ăn từ 9 giờ tối hôm trước ngày khám.",
                "situation": "onsite"
            },
            {
                "ko": "결과는 일주일 후 상담을 통해 설명드립니다.",
                "vi": "Kết quả sẽ được giải thích qua tư vấn sau một tuần.",
                "situation": "formal"
            }
        ],
        "relatedTerms": ["건강검진", "암검진", "종합검진", "내시경", "초음파"]
    },
    {
        "slug": "kham-benh-tu-xa",
        "korean": "원격진료",
        "vietnamese": "khám bệnh từ xa",
        "hanja": "遠隔診療",
        "hanjaReading": "원(멀 원) + 격(사이 격) + 진(살필 진) + 료(치료할 료)",
        "pronunciation": "won-gyeok-jin-ryo",
        "meaningKo": "의사와 환자가 물리적으로 같은 공간에 있지 않고, 정보통신기술을 이용하여 원격으로 진료하는 의료 서비스입니다. 통역 시 주의할 점은 한국에서는 코로나19 이후 한시적으로 허용되었으나 법적 제한이 여전히 있음을 설명하고, 처방전 발급과 약 수령 방법을 정확히 안내해야 합니다. 응급 상황이나 만성질환 관리에 제한적으로 사용되며, 대면 진료가 원칙임을 명확히 해야 합니다.",
        "meaningVi": "Dịch vụ y tế cho phép bác sĩ và bệnh nhân không ở cùng không gian vật lý, mà khám chữa bệnh từ xa thông qua công nghệ thông tin. Ở Hàn Quốc, sau COVID-19 được cho phép tạm thời nhưng vẫn có nhiều hạn chế pháp lý, nguyên tắc vẫn là khám trực tiếp.",
        "context": "원격 의료, 디지털 헬스케어",
        "culturalNote": "한국은 의료법상 원격진료가 엄격히 제한되어 왔으나, COVID-19 팬데믹 기간 한시적으로 허용되었습니다. 베트남보다 법적 규제가 강하며, 주로 재진 환자나 만성질환자에게만 제공됩니다. 화상 진료 후 처방전을 이메일이나 앱으로 받고, 약은 배송 또는 약국 방문으로 수령합니다.",
        "commonMistakes": [
            {
                "mistake": "'원격진료'를 'khám bệnh online'로 단순화",
                "correction": "'khám bệnh từ xa'가 의료 용어로 적합",
                "explanation": "온라인은 비공식적이지만 원격진료는 법적 규정이 있는 공식 의료행위입니다"
            },
            {
                "mistake": "모든 질환을 원격으로 볼 수 있다고 안내",
                "correction": "재진이나 경미한 질환에만 가능하며 응급은 불가",
                "explanation": "법적으로 초진은 대면이 원칙이며, 중증 질환은 원격진료 대상이 아닙니다"
            },
            {
                "mistake": "비용이 더 저렴하다고 설명",
                "correction": "진료비는 대면과 동일하며 통신비 추가 가능",
                "explanation": "원격이라고 해서 진료비가 할인되지 않습니다"
            }
        ],
        "examples": [
            {
                "ko": "코로나19 증상이 있으시면 원격진료를 이용하세요.",
                "vi": "Nếu có triệu chứng COVID-19, hãy sử dụng khám bệnh từ xa.",
                "situation": "formal"
            },
            {
                "ko": "처방전은 앱으로 전송되고 약은 배달됩니다.",
                "vi": "Đơn thuốc sẽ được gửi qua ứng dụng và thuốc sẽ được giao.",
                "situation": "onsite"
            },
            {
                "ko": "처음 진료는 꼭 병원에 오셔야 합니다.",
                "vi": "Lần khám đầu tiên nhất định phải đến bệnh viện.",
                "situation": "formal"
            }
        ],
        "relatedTerms": ["화상진료", "전화진료", "디지털헬스", "처방전", "재진"]
    },
    {
        "slug": "y-kien-bac-si-thu-hai",
        "korean": "세컨드오피니언",
        "vietnamese": "ý kiến bác sĩ thứ hai",
        "hanja": None,
        "hanjaReading": None,
        "pronunciation": "se-keun-deu-o-pi-ni-eon",
        "meaningKo": "현재 진료 중인 의사의 진단이나 치료 계획에 대해 다른 의사의 의견을 구하는 의료 서비스입니다. 통역 시 주의할 점은 환자의 권리임을 강조하고, 첫 번째 의사에 대한 불신이 아닌 신중한 결정을 위한 과정임을 설명해야 하며, 의료 기록 사본 요청 방법과 비용을 정확히 안내해야 합니다. 특히 수술이나 항암치료 같은 중요한 결정 전에 권장되며, 건강보험 적용 여부도 확인이 필요합니다.",
        "meaningVi": "Dịch vụ y tế cho phép bệnh nhân xin ý kiến của bác sĩ khác về chẩn đoán hoặc kế hoạch điều trị hiện tại. Đây là quyền của bệnh nhân, không phải là sự thiếu tin tưởng vào bác sĩ đầu tiên, mà là quá trình để đưa ra quyết định thận trọng.",
        "context": "환자 권리, 의료 결정",
        "culturalNote": "한국에서는 세컨드오피니언이 환자의 권리로 인정되며, 대형 병원에는 전담 센터가 있습니다. 베트남보다 의사와 환자 관계가 수평적이어서 다른 의견을 구하는 것에 대한 부담이 적습니다. 암이나 희귀질환의 경우 세컨드오피니언을 적극 권장하며, 의료진도 협조적입니다.",
        "commonMistakes": [
            {
                "mistake": "'세컨드오피니언'을 'tái khám'(재진)으로 번역",
                "correction": "'ý kiến bác sĩ thứ hai' 또는 'tham khảo ý kiến bác sĩ khác'",
                "explanation": "재진은 같은 의사를 다시 보는 것이고, 세컨드오피니언은 다른 의사의 의견을 구하는 것입니다"
            },
            {
                "mistake": "첫 번째 의사에게 비밀로 해야 한다고 안내",
                "correction": "공개적으로 요청할 수 있으며 의료 기록 제공이 필수",
                "explanation": "숨길 필요 없고 오히려 협조를 구하는 것이 정상적인 절차입니다"
            },
            {
                "mistake": "무조건 무료라고 설명",
                "correction": "병원과 보험 적용 여부에 따라 비용 발생 가능",
                "explanation": "일부는 건강보험이 적용되지만 병원마다 정책이 다릅니다"
            }
        ],
        "examples": [
            {
                "ko": "수술 전에 다른 병원에서 세컨드오피니언을 받고 싶습니다.",
                "vi": "Trước khi phẫu thuật, tôi muốn xin ý kiến bác sĩ thứ hai ở bệnh viện khác.",
                "situation": "formal"
            },
            {
                "ko": "의무기록 사본이 필요하시면 원무과에 신청하세요.",
                "vi": "Nếu cần bản sao hồ sơ bệnh án, hãy đăng ký ở phòng hành chính.",
                "situation": "onsite"
            },
            {
                "ko": "세컨드오피니언은 환자의 권리입니다.",
                "vi": "Ý kiến bác sĩ thứ hai là quyền của bệnh nhân.",
                "situation": "informal"
            }
        ],
        "relatedTerms": ["환자권리", "의무기록", "진단", "치료계획", "상담"]
    },
    {
        "slug": "quyet-dinh-y-te-keo-dai-su-song",
        "korean": "연명의료결정",
        "vietnamese": "quyết định y tế kéo dài sự sống",
        "hanja": "延命醫療決定",
        "hanjaReading": "연(늘일 연) + 명(목숨 명) + 의(의원 의) + 료(치료할 료) + 결(맺을 결) + 정(정할 정)",
        "pronunciation": "yeon-myeong-ui-ryo-gyeol-jeong",
        "meaningKo": "회생 가능성이 없는 임종 과정에 있는 환자에 대해 심폐소생술, 인공호흡기 등 생명 연장 치료를 시행할지 여부를 미리 결정하는 제도입니다. 통역 시 주의할 점은 매우 민감한 주제이므로 문화적, 종교적 배경을 고려하여 신중하게 설명해야 하며, 환자의 자기결정권과 가족의 의견을 모두 존중해야 합니다. 사전연명의료의향서 작성 시기와 방법, 법적 효력을 정확히 전달하는 것이 중요합니다.",
        "meaningVi": "Chế độ cho phép bệnh nhân quyết định trước về việc có thực hiện các biện pháp kéo dài sự sống như hồi sức tim phổi, máy thở nhân tạo hay không đối với bệnh nhân giai đoạn cuối không còn khả năng hồi phục. Đây là chủ đề nhạy cảm cần xem xét bối cảnh văn hóa và tôn giáo.",
        "context": "임종 관리, 환자 권리",
        "culturalNote": "한국은 2018년부터 '연명의료결정법'이 시행되어 환자의 자기결정권을 존중합니다. 베트남 문화권에서는 이러한 결정이 가족 중심으로 이뤄지는 경우가 많아 차이를 설명하는 것이 중요합니다. 사전연명의료의향서는 건강할 때 미리 작성하는 것이며, 언제든 변경 가능합니다. 종교적 신념도 존중됩니다.",
        "commonMistakes": [
            {
                "mistake": "'연명의료'를 'điều trị cấp cứu'(응급치료)로 혼동",
                "correction": "'y tế kéo dài sự sống'으로 명확히 구분",
                "explanation": "응급치료는 회복 가능성이 있지만, 연명의료는 임종 단계의 치료입니다"
            },
            {
                "mistake": "안락사와 동일하게 설명",
                "correction": "연명의료 중단은 자연사를 허용하는 것이지 안락사 아님",
                "explanation": "안락사는 불법이지만 연명의료 중단은 합법적인 환자 권리입니다"
            },
            {
                "mistake": "가족이 일방적으로 결정할 수 있다고 안내",
                "correction": "환자 본인 의사가 최우선이며, 가족은 보조적 역할",
                "explanation": "법적으로 환자의 자기결정권이 가장 중요합니다"
            }
        ],
        "examples": [
            {
                "ko": "사전연명의료의향서를 작성하시면 본인의 뜻을 미리 밝힐 수 있습니다.",
                "vi": "Nếu lập bản văn ý định y tế trước, có thể bày tỏ ý muốn của mình trước.",
                "situation": "formal"
            },
            {
                "ko": "연명의료 결정은 언제든 변경하실 수 있습니다.",
                "vi": "Quyết định y tế kéo dài sự sống có thể thay đổi bất cứ lúc nào.",
                "situation": "onsite"
            },
            {
                "ko": "가족분들과 충분히 상의하셔서 결정하시기 바랍니다.",
                "vi": "Xin hãy thảo luận đầy đủ với gia đình rồi quyết định.",
                "situation": "formal"
            }
        ],
        "relatedTerms": ["사전연명의료의향서", "호스피스", "완화의료", "임종", "자기결정권"]
    },
    {
        "slug": "hien-tang",
        "korean": "장기기증",
        "vietnamese": "hiến tạng",
        "hanja": "臟器寄贈",
        "hanjaReading": "장(오장 장) + 기(그릇 기) + 기(부칠 기) + 증(줄 증)",
        "pronunciation": "jang-gi-gi-jeung",
        "meaningKo": "사망 후 또는 생존 시에 자신의 장기를 이식이 필요한 환자에게 기증하는 숭고한 행위입니다. 통역 시 주의할 점은 뇌사와 심장사의 차이를 정확히 설명하고, 장기기증 등록과 실제 기증의 차이를 명확히 해야 하며, 가족의 동의가 필요함을 안내해야 합니다. 문화적, 종교적으로 민감한 주제이므로 강요하지 않고 존중하는 태도로 정보를 전달하는 것이 중요합니다.",
        "meaningVi": "Hành động cao quý hiến tặng các cơ quan của mình cho bệnh nhân cần ghép tạng sau khi chết hoặc khi còn sống. Cần giải thích rõ sự khác biệt giữa chết não và ngừng tim, cũng như sự khác nhau giữa đăng ký hiến tạng và việc thực sự hiến tạng.",
        "context": "장기 이식, 기증 문화",
        "culturalNote": "한국은 장기기증 문화가 점차 확산되고 있으나 여전히 공급이 부족합니다. 베트남 문화권에서는 유교적 영향으로 신체 훼손에 대한 거부감이 있을 수 있으나, 최근 세대는 개방적입니다. 장기기증 등록은 간단하지만, 실제 기증 시 가족 동의가 필수이며, 외국인도 등록 가능합니다.",
        "commonMistakes": [
            {
                "mistake": "'장기기증'을 'cho tạng'로만 번역",
                "correction": "'hiến tạng'이 공식적이고 존중받는 표현",
                "explanation": "'cho'는 일상적이지만 'hiến'은 숭고한 기증의 의미를 담고 있습니다"
            },
            {
                "mistake": "등록하면 즉시 기증된다고 오해하게 통역",
                "correction": "등록은 의사 표시일 뿐, 실제 기증은 사망 후 가족 동의 필요",
                "explanation": "등록과 실제 기증 사이의 과정을 명확히 해야 불안을 줄입니다"
            },
            {
                "mistake": "뇌사와 심장사를 구분 없이 설명",
                "correction": "뇌사는 심장 뛰지만 뇌 기능 상실, 심장사는 심장 정지",
                "explanation": "장기기증 가능 조건이 다르므로 정확한 구분이 필요합니다"
            }
        ],
        "examples": [
            {
                "ko": "장기기증 등록은 온라인이나 보건소에서 할 수 있습니다.",
                "vi": "Đăng ký hiến tạng có thể thực hiện trực tuyến hoặc tại trạm y tế.",
                "situation": "formal"
            },
            {
                "ko": "등록하셔도 나중에 언제든 취소할 수 있습니다.",
                "vi": "Dù đã đăng ký, sau này cũng có thể hủy bất cứ lúc nào.",
                "situation": "onsite"
            },
            {
                "ko": "뇌사 상태에서도 가족이 동의해야 기증이 가능합니다.",
                "vi": "Ngay cả khi chết não, cũng cần sự đồng ý của gia đình mới có thể hiến tạng.",
                "situation": "formal"
            }
        ],
        "relatedTerms": ["뇌사", "장기이식", "생체기증", "각막기증", "골수기증"]
    },
    {
        "slug": "thu-nghiem-lam-sang",
        "korean": "임상시험",
        "vietnamese": "thử nghiệm lâm sàng",
        "hanja": "臨床試驗",
        "hanjaReading": "임(임할 임) + 상(자리 상) + 시(시험할 시) + 험(시험할 험)",
        "pronunciation": "im-sang-si-heom",
        "meaningKo": "신약이나 의료기기의 안전성과 효과를 확인하기 위해 실제 환자를 대상으로 실시하는 연구입니다. 통역 시 주의할 점은 참여의 자발성과 중단 권리를 강조하고, 위약 대조군의 개념을 정확히 설명해야 하며, 발생 가능한 부작용과 보상 제도를 명확히 안내해야 합니다. 참여 전 충분한 설명을 듣고 동의서에 서명하는 과정이 필수임을 전달하는 것이 중요합니다.",
        "meaningVi": "Nghiên cứu thực hiện trên bệnh nhân thực tế để xác nhận tính an toàn và hiệu quả của thuốc mới hoặc thiết bị y tế mới. Sự tham gia là tự nguyện và có quyền dừng lại bất cứ lúc nào, cần giải thích rõ khái niệm nhóm đối chứng dùng giả dược và chế độ bồi thường.",
        "context": "의학 연구, 신약 개발",
        "culturalNote": "한국은 임상시험이 엄격한 윤리 규정과 법적 절차에 따라 진행됩니다. 베트남보다 환자 권리 보호가 강화되어 있으며, IRB(기관생명윤리위원회) 승인이 필수입니다. 참여자에게는 검사비 지원, 교통비, 보상금 등이 제공되며, 부작용 발생 시 치료와 배상이 보장됩니다. 외국인도 참여 가능하지만 언어 소통이 중요합니다.",
        "commonMistakes": [
            {
                "mistake": "'임상시험'을 'thí nghiệm'(실험)로 번역",
                "correction": "'thử nghiệm lâm sàng'이 의학 용어로 적절",
                "explanation": "실험은 동물 등을 대상으로 하지만, 임상시험은 인간 대상 연구입니다"
            },
            {
                "mistake": "참여하면 반드시 끝까지 해야 한다고 설명",
                "correction": "언제든 자유롭게 중단할 수 있음을 강조",
                "explanation": "강제성이 없으며 중단해도 불이익이 없음을 명확히 해야 합니다"
            },
            {
                "mistake": "위약을 '가짜 약'으로 부정적으로 표현",
                "correction": "'giả dược' 또는 'thuốc giả dược'으로 중립적으로",
                "explanation": "위약 대조군은 과학적으로 필수적인 절차임을 설명해야 합니다"
            }
        ],
        "examples": [
            {
                "ko": "이 임상시험에 참여하시면 새로운 치료법을 시도할 수 있습니다.",
                "vi": "Nếu tham gia thử nghiệm lâm sàng này, có thể thử phương pháp điều trị mới.",
                "situation": "formal"
            },
            {
                "ko": "참여 중에도 언제든 그만두실 수 있으며 불이익은 없습니다.",
                "vi": "Ngay cả khi đang tham gia, bất cứ lúc nào cũng có thể ngừng và không bị bất lợi.",
                "situation": "onsite"
            },
            {
                "ko": "부작용이 발생하면 즉시 연구팀에 연락하세요.",
                "vi": "Nếu có tác dụng phụ, hãy liên hệ ngay với nhóm nghiên cứu.",
                "situation": "formal"
            }
        ],
        "relatedTerms": ["신약", "위약", "IRB", "동의서", "부작용"]
    },
    {
        "slug": "phan-ung-co-hai-cua-thuoc",
        "korean": "약물이상반응",
        "vietnamese": "phản ứng có hại của thuốc",
        "hanja": "藥物異常反應",
        "hanjaReading": "약(약 약) + 물(물건 물) + 이(다를 이) + 상(항상 상) + 반(돌이킬 반) + 응(응할 응)",
        "pronunciation": "yak-mul-i-sang-ban-eung",
        "meaningKo": "약물 사용 후 나타나는 의도하지 않은 유해하거나 원하지 않는 반응으로, 알레르ギ부터 심각한 부작용까지 포함합니다. 통역 시 주의할 점은 가벼운 증상도 즉시 보고해야 함을 강조하고, 과거 약물 알레르기 이력을 정확히 전달하며, 응급 상황 시 대처 방법을 명확히 안내해야 합니다. 특히 항생제, 진통제, 조영제 등에서 흔히 발생하므로 사전 확인이 중요함을 설명해야 합니다.",
        "meaningVi": "Phản ứng có hại hoặc không mong muốn xảy ra sau khi sử dụng thuốc, từ dị ứng nhẹ đến tác dụng phụ nghiêm trọng. Cần nhấn mạnh việc báo cáo ngay cả triệu chứng nhẹ, truyền đạt chính xác tiền sử dị ứng thuốc và hướng dẫn rõ cách xử lý tình huống khẩn cấp.",
        "context": "약물 안전, 부작용 관리",
        "culturalNote": "한국 의료기관은 약물이상반응 보고 시스템이 체계화되어 있으며, 환자 안전을 위해 매우 중시합니다. 베트남보다 부작용에 대한 인식과 보고 문화가 강하며, 의료진은 모든 약물 투여 전 알레르기를 반드시 확인합니다. 중증 반응 시 신속한 응급 처치 시스템이 갖춰져 있습니다.",
        "commonMistakes": [
            {
                "mistake": "'약물이상반응'을 단순히 'dị ứng thuốc'(약 알레르기)로만 번역",
                "correction": "'phản ứng có hại của thuốc' 또는 'tác dụng phụ của thuốc'",
                "explanation": "알레르기는 일부이고, 이상반응은 더 넓은 개념입니다"
            },
            {
                "mistake": "가벼운 증상은 보고하지 않아도 된다고 안내",
                "correction": "모든 이상 증상을 즉시 보고해야 함을 강조",
                "explanation": "가벼운 증상도 심각한 반응의 전조일 수 있습니다"
            },
            {
                "mistake": "과거 알레르기 이력을 대략적으로만 통역",
                "correction": "약물명, 증상, 시기를 정확히 전달",
                "explanation": "정확한 정보가 있어야 유사 약물 사용을 피할 수 있습니다"
            }
        ],
        "examples": [
            {
                "ko": "약을 드신 후 발진이나 가려움이 생기면 즉시 알려주세요.",
                "vi": "Sau khi uống thuốc, nếu có phát ban hoặc ngứa, hãy báo ngay.",
                "situation": "formal"
            },
            {
                "ko": "과거에 약물 알레르기가 있었나요?",
                "vi": "Trước đây có bị dị ứng thuốc không?",
                "situation": "onsite"
            },
            {
                "ko": "심한 두드러기나 호흡곤란이 오면 응급실로 오세요.",
                "vi": "Nếu có mày đay nghiêm trọng hoặc khó thở, hãy đến phòng cấp cứu.",
                "situation": "formal"
            }
        ],
        "relatedTerms": ["알레르기", "부작용", "약물안전", "조영제", "항생제"]
    },
    {
        "slug": "su-co-y-te",
        "korean": "의료사고",
        "vietnamese": "sự cố y tế",
        "hanja": "醫療事故",
        "hanjaReading": "의(의원 의) + 료(치료할 료) + 사(일 사) + 고(옛 고)",
        "pronunciation": "ui-ryo-sa-go",
        "meaningKo": "의료 행위 과정에서 환자에게 의도하지 않은 손상이나 피해가 발생한 사건으로, 의료 과실과 불가항력적 합병증을 모두 포함합니다. 통역 시 주의할 점은 환자의 법적 권리와 보고 절차를 정확히 안내하고, 병원의 사고 보고 의무와 환자 보호 시스템을 설명해야 하며, 무료 법률 상담 서비스를 연결해 주어야 합니다. 감정적으로 대응하지 않고 객관적으로 사실을 전달하는 것이 중요합니다.",
        "meaningVi": "Sự kiện xảy ra tổn thương hoặc thiệt hại không mong muốn cho bệnh nhân trong quá trình điều trị y tế, bao gồm cả lỗi y khoa và biến chứng bất khả kháng. Cần hướng dẫn chính xác quyền lợi pháp lý và quy trình báo cáo của bệnh nhân, giải thích nghĩa vụ báo cáo sự cố và hệ thống bảo vệ bệnh nhân của bệnh viện.",
        "context": "환자 안전, 법적 권리",
        "culturalNote": "한국은 의료사고 발생 시 병원의 보고 의무가 법제화되어 있으며, 환자 안전 문화가 강조됩니다. 베트남보다 의료 분쟁 해결 시스템이 체계적이고, 환자 권리 보호가 강화되어 있습니다. 의료사고 발생 시 은폐보다는 투명한 공개와 재발 방지가 원칙이며, 외국인도 동등한 법적 보호를 받습니다.",
        "commonMistakes": [
            {
                "mistake": "'의료사고'를 'lỗi của bác sĩ'(의사 실수)로만 번역",
                "correction": "'sự cố y tế'가 중립적이고 포괄적",
                "explanation": "과실뿐 아니라 불가항력적 상황도 포함되므로 중립적 표현이 필요합니다"
            },
            {
                "mistake": "환자가 참고 넘어가야 한다고 암시",
                "correction": "법적 권리가 있으며 조정 신청 가능함을 명확히",
                "explanation": "환자는 정당한 보상을 요구할 권리가 있습니다"
            },
            {
                "mistake": "의료사고와 의료 과실을 동일하게 설명",
                "correction": "사고는 넓은 개념, 과실은 법적 책임이 있는 경우",
                "explanation": "모든 사고가 과실은 아니며, 법적 판단이 필요합니다"
            }
        ],
        "examples": [
            {
                "ko": "의료사고가 발생하면 병원에서 조사하고 환자분께 설명드립니다.",
                "vi": "Nếu xảy ra sự cố y tế, bệnh viện sẽ điều tra và giải thích cho bệnh nhân.",
                "situation": "formal"
            },
            {
                "ko": "환자안전사고 보고 시스템에 신고하실 수 있습니다.",
                "vi": "Có thể báo cáo vào hệ thống báo cáo sự cố an toàn bệnh nhân.",
                "situation": "onsite"
            },
            {
                "ko": "의료분쟁조정을 통해 공정한 해결을 받으실 수 있습니다.",
                "vi": "Có thể nhận được giải quyết công bằng thông qua hòa giải tranh chấp y tế.",
                "situation": "formal"
            }
        ],
        "relatedTerms": ["의료과실", "환자안전", "의료분쟁", "손해배상", "조정신청"]
    },
    {
        "slug": "van-chuyen-cap-cuu",
        "korean": "응급이송",
        "vietnamese": "vận chuyển cấp cứu",
        "hanja": "應急移送",
        "hanjaReading": "응(응할 응) + 급(급할 급) + 이(옮길 이) + 송(보낼 송)",
        "pronunciation": "eung-geup-i-song",
        "meaningKo": "응급환자를 신속하고 안전하게 의료기관으로 이동시키는 의료 서비스로, 구급차를 통한 병원 전 응급처치를 포함합니다. 통역 시 주의할 점은 119 신고 방법과 정확한 위치 전달의 중요성을 강조하고, 응급 증상 판단 기준을 명확히 설명해야 하며, 이송 비용과 보험 적용 여부를 안내해야 합니다. 외국인도 119를 무료로 이용할 수 있으며, 다국어 서비스가 제공됨을 알려주어야 합니다.",
        "meaningVi": "Dịch vụ y tế vận chuyển bệnh nhân cấp cứu nhanh chóng và an toàn đến cơ sở y tế, bao gồm sơ cứu trước khi đến bệnh viện trên xe cấp cứu. Người nước ngoài cũng có thể sử dụng 119 miễn phí và được cung cấp dịch vụ đa ngôn ngữ.",
        "context": "응급 의료, 구급차 이용",
        "culturalNote": "한국의 119 응급의료 시스템은 매우 발달해 있으며 전국 어디서나 신속하게 출동합니다. 베트남보다 구급차 이용이 체계적이고 무료이며, 구급대원의 응급처치 능력이 높습니다. 외국인을 위한 다국어 통역 서비스(1339)가 연계되어 있고, 응급실 과밀화로 경증 환자는 대기 시간이 길 수 있습니다.",
        "commonMistakes": [
            {
                "mistake": "'응급이송'을 단순히 'xe cấp cứu'(구급차)로만 번역",
                "correction": "'vận chuyển cấp cứu' 또는 'dịch vụ cấp cứu'",
                "explanation": "이송은 차량뿐 아니라 응급처치 서비스 전체를 포함합니다"
            },
            {
                "mistake": "모든 상황에 119를 부르라고 안내",
                "correction": "진짜 응급 상황과 일반 진료 상황을 구분",
                "explanation": "구급차 남용을 방지하고 진짜 응급 환자를 위해 적절한 이용이 필요합니다"
            },
            {
                "mistake": "119가 유료라고 잘못 안내",
                "correction": "119 구급차는 무료이며 건강보험 적용",
                "explanation": "일부 민간 구급차는 유료이지만 119는 공공 서비스로 무료입니다"
            }
        ],
        "examples": [
            {
                "ko": "심한 흉통이 있으시면 119에 전화하세요.",
                "vi": "Nếu có đau ngực dữ dội, hãy gọi 119.",
                "situation": "formal"
            },
            {
                "ko": "119 신고 시 정확한 주소를 말씀해 주세요.",
                "vi": "Khi báo 119, hãy nói địa chỉ chính xác.",
                "situation": "onsite"
            },
            {
                "ko": "외국인 환자를 위한 통역 서비스도 제공됩니다.",
                "vi": "Cũng cung cấp dịch vụ thông dịch cho bệnh nhân nước ngoài.",
                "situation": "informal"
            }
        ],
        "relatedTerms": ["119", "구급차", "응급실", "응급처치", "골든타임"]
    }
]

# 기존 슬러그와 중복 제거
filtered_terms = [term for term in new_terms if term['slug'] not in existing_slugs]

# 기존 데이터에 추가
data.extend(filtered_terms)

# 파일 저장
with open(file_path, 'w', encoding='utf-8') as f:
    json.dump(data, f, ensure_ascii=False, indent=2)

print(f"✅ 추가된 용어: {len(filtered_terms)}개")
print(f"✅ 전체 용어 수: {len(data)}개")
print(f"✅ 파일 저장 완료: {file_path}")
