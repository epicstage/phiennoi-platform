#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
한-베 통역 용어 플랫폼 - 법률 도메인 용어 추가 스크립트
테마: 의료과오/의료사고법 (Medical Malpractice Law)

용어: 의료과실, 의료소송, 설명의무, 환자동의, 진료거부, 응급의료, 장기이식, 의료광고, 의약분업, 임상시험

Tier S 품질 기준:
- meaningKo: 200자 이상, "통역" 키워드 포함
- meaningVi: 100자 이상
- culturalNote: 100자 이상
- commonMistakes: 3개 이상 (객체 형식)
- examples: 3개 이상 (situation 포함)
- relatedTerms: 3개 이상
- 베트남어 성조 필수
"""

import json
import os

# 용어 데이터 (Tier S 기준)
NEW_TERMS = [
    {
        "slug": "loi-y-khoa",
        "korean": "의료과실",
        "vietnamese": "Lỗi y khoa",
        "hanja": "醫療過失",
        "hanjaReading": "醫(고칠 의) + 療(고칠 료) + 過(지날 과) + 失(잃을 실)",
        "pronunciation": "이료과실",
        "meaningKo": "의료인이 환자를 진료하는 과정에서 주의의무를 위반하여 환자에게 손해를 발생시킨 과실을 의미합니다. 통역 시에는 '의료사고'와 구분해야 하며, 의료과실은 법적 책임을 묻는 개념이고 의료사고는 단순히 사고가 발생한 사실을 말합니다. 베트남에서는 '태만'의 의미가 강한 'sơ suất'보다는 전문적 실수를 뜻하는 'lỗi'를 사용하며, 통역 시 과실의 정도(경과실/중과실)를 명확히 구분해야 합니다.",
        "meaningVi": "Là hành vi vi phạm nghĩa vụ chú ý của nhân viên y tế trong quá trình khám chữa bệnh, gây thiệt hại cho bệnh nhân. Khác với 'tai nạn y tế' (medical accident) đơn thuần, lỗi y khoa là khái niệm pháp lý có thể dẫn đến trách nhiệm bồi thường.",
        "context": "의료소송, 손해배상 청구, 의료분쟁 조정",
        "culturalNote": "한국에서는 의료과실 입증책임이 환자 측에 있어 소송이 어렵지만, 최근 입증책임 완화 추세입니다. 베트남에서는 의료과실 개념이 명확하지 않아 '의료사고'로 통칭되는 경우가 많으며, 법적 분쟁보다는 행정적 해결을 선호합니다. 통역 시 양국의 의료과실 판단 기준과 입증책임 차이를 설명해야 합니다.",
        "commonMistakes": [
            {
                "mistake": "'sơ suất y tế'로 번역",
                "correction": "'lỗi y khoa'",
                "explanation": "sơ suất는 단순 실수를 의미하며, 법적 책임을 묻는 전문 용어로는 lỗi가 적절합니다."
            },
            {
                "mistake": "의료사고와 동일하게 번역",
                "correction": "의료과실(lỗi y khoa)은 법적 책임, 의료사고(tai nạn y tế)는 사실 관계",
                "explanation": "의료사고는 결과이고 의료과실은 원인으로, 법적 책임 여부에 따라 구분됩니다."
            },
            {
                "mistake": "과실의 정도를 구분하지 않음",
                "correction": "경과실(lỗi nhẹ), 중과실(lỗi nghiêm trọng) 명시",
                "explanation": "과실의 정도에 따라 법적 책임과 배상액이 달라지므로 반드시 구분해야 합니다."
            }
        ],
        "examples": [
            {
                "ko": "법원은 의사의 의료과실을 인정하여 손해배상을 명령했습니다.",
                "vi": "Tòa án đã công nhận lỗi y khoa của bác sĩ và ra lệnh bồi thường thiệt hại.",
                "situation": "formal"
            },
            {
                "ko": "수술 중 의료과실로 환자가 사망한 사건입니다.",
                "vi": "Đây là vụ việc bệnh nhân tử vong do lỗi y khoa trong quá trình phẫu thuật.",
                "situation": "onsite"
            },
            {
                "ko": "의료과실 여부는 의료감정을 통해 판단합니다.",
                "vi": "Việc có lỗi y khoa hay không được xác định thông qua giám định y khoa.",
                "situation": "formal"
            }
        ],
        "relatedTerms": ["의료사고", "설명의무", "주의의무", "손해배상"]
    },
    {
        "slug": "kien-tung-y-te",
        "korean": "의료소송",
        "vietnamese": "Kiện tụng y tế",
        "hanja": "醫療訴訟",
        "hanjaReading": "醫(고칠 의) + 療(고칠 료) + 訴(하소연할 소) + 訟(송사할 송)",
        "pronunciation": "이료소송",
        "meaningKo": "의료행위와 관련하여 발생한 분쟁을 법원에서 해결하는 절차를 의미합니다. 통역 시에는 민사소송(손해배상), 형사소송(업무상과실치사상), 행정소송(면허취소)을 구분해야 하며, 베트남에서는 의료소송이 드물어 개념 설명이 필요합니다. 한국의 의료분쟁조정제도와 베트남의 행정 해결 방식 차이를 이해하고 통역해야 하며, 소송 전 조정 절차의 중요성을 강조해야 합니다.",
        "meaningVi": "Là thủ tục giải quyết tranh chấp liên quan đến hành vi y tế tại tòa án. Bao gồm kiện dân sự (bồi thường thiệt hại), kiện hình sự (gây thương tích do vô ý trong công việc), và kiện hành chính (thu hồi giấy phép hành nghề).",
        "context": "의료분쟁, 손해배상 청구, 의료과실 입증",
        "culturalNote": "한국에서는 의료소송이 증가하고 있으며 의료분쟁조정중재원을 통한 조정이 활성화되어 있습니다. 베트남에서는 의료소송이 매우 드물며, 대부분 보건당국의 행정적 해결이나 합의로 마무리됩니다. 통역 시 한국의 법적 절차와 증거 제출 방식, 의료감정 제도를 상세히 설명해야 합니다.",
        "commonMistakes": [
            {
                "mistake": "'vụ kiện y tế'로만 번역",
                "correction": "'kiện tụng y tế' 또는 'tranh chấp y tế'",
                "explanation": "vụ kiện은 '소송 사건'을 의미하며, kiện tụng은 소송 절차 전체를 포괄하는 법률 용어입니다."
            },
            {
                "mistake": "민사/형사/행정 소송 구분 없이 번역",
                "correction": "kiện dân sự/hình sự/hành chính 명시",
                "explanation": "소송 유형에 따라 절차와 결과가 다르므로 반드시 구분해야 합니다."
            },
            {
                "mistake": "조정 절차를 생략하고 번역",
                "correction": "조정(hòa giải) 절차 설명 추가",
                "explanation": "한국은 의료분쟁조정제도가 발달했으므로 소송 전 조정 절차를 반드시 언급해야 합니다."
            }
        ],
        "examples": [
            {
                "ko": "의료소송에서 환자 측이 승소하기는 매우 어렵습니다.",
                "vi": "Rất khó để phía bệnh nhân thắng kiện trong kiện tụng y tế.",
                "situation": "formal"
            },
            {
                "ko": "의료소송 전에 의료분쟁조정을 신청할 수 있습니다.",
                "vi": "Trước khi kiện tụng y tế, có thể nộp đơn hòa giải tranh chấp y tế.",
                "situation": "onsite"
            },
            {
                "ko": "이 사건은 의료소송으로 발전할 가능성이 높습니다.",
                "vi": "Vụ việc này có khả năng cao sẽ phát triển thành kiện tụng y tế.",
                "situation": "informal"
            }
        ],
        "relatedTerms": ["의료분쟁", "손해배상", "의료과실", "의료감정"]
    },
    {
        "slug": "nghia-vu-giai-thich",
        "korean": "설명의무",
        "vietnamese": "Nghĩa vụ giải thích",
        "hanja": "說明義務",
        "hanjaReading": "說(말씀 설) + 明(밝을 명) + 義(옳을 의) + 務(힘쓸 무)",
        "pronunciation": "설명의무",
        "meaningKo": "의료인이 환자에게 질병의 진단, 치료 방법, 예후, 부작용 등을 설명해야 할 법적 의무를 의미합니다. 통역 시에는 단순 정보 제공이 아닌 '법적 의무'임을 강조해야 하며, 설명의무 위반 시 의료과실로 인정될 수 있음을 주의해야 합니다. 베트남에서는 설명의무 개념이 약하므로 환자의 알 권리와 자기결정권과 연계하여 설명하고, 통역 시 설명 내용과 환자 이해도를 확인하는 절차가 중요합니다.",
        "meaningVi": "Là nghĩa vụ pháp lý của nhân viên y tế phải giải thích cho bệnh nhân về chẩn đoán, phương pháp điều trị, tiên lượng, tác dụng phụ. Vi phạm nghĩa vụ này có thể được coi là lỗi y khoa và dẫn đến trách nhiệm pháp lý.",
        "context": "환자동의, 자기결정권, 의료과실",
        "culturalNote": "한국에서는 판례를 통해 설명의무가 확립되었으며, 설명 내용의 범위와 정도가 구체적으로 정해져 있습니다. 베트남에서는 설명의무가 법률로 명시되어 있지만 실무에서는 잘 지켜지지 않는 경우가 많습니다. 통역 시 설명의무의 법적 성격과 위반 시 책임을 명확히 전달하고, 환자가 이해했는지 확인하는 과정이 필수임을 강조해야 합니다.",
        "commonMistakes": [
            {
                "mistake": "'thông tin' 또는 'giải thích'로만 번역",
                "correction": "'nghĩa vụ giải thích' (법적 의무 강조)",
                "explanation": "단순 정보 제공이 아닌 법적 의무임을 명확히 해야 합니다."
            },
            {
                "mistake": "설명 내용의 범위를 명시하지 않음",
                "correction": "진단, 치료, 예후, 부작용 등 구체적 항목 나열",
                "explanation": "설명의무의 범위는 법적으로 정해져 있으므로 구체적으로 설명해야 합니다."
            },
            {
                "mistake": "환자 이해 확인 절차를 생략",
                "correction": "xác nhận bệnh nhân hiểu (환자 이해 확인) 추가",
                "explanation": "설명만 하는 것이 아니라 환자가 이해했는지 확인해야 의무가 이행됩니다."
            }
        ],
        "examples": [
            {
                "ko": "수술 전 의사는 환자에게 설명의무를 이행해야 합니다.",
                "vi": "Trước phẫu thuật, bác sĩ phải thực hiện nghĩa vụ giải thích cho bệnh nhân.",
                "situation": "formal"
            },
            {
                "ko": "설명의무를 위반하면 의료과실로 인정될 수 있습니다.",
                "vi": "Nếu vi phạm nghĩa vụ giải thích, có thể bị coi là lỗi y khoa.",
                "situation": "onsite"
            },
            {
                "ko": "환자가 이해할 수 있는 언어로 설명의무를 이행해야 합니다.",
                "vi": "Phải thực hiện nghĩa vụ giải thích bằng ngôn ngữ mà bệnh nhân có thể hiểu.",
                "situation": "formal"
            }
        ],
        "relatedTerms": ["환자동의", "자기결정권", "의료과실", "알권리"]
    },
    {
        "slug": "dong-y-benh-nhan",
        "korean": "환자동의",
        "vietnamese": "Đồng ý bệnh nhân",
        "hanja": "患者同意",
        "hanjaReading": "患(근심할 환) + 者(사람 자) + 同(한가지 동) + 意(뜻 의)",
        "pronunciation": "환자동의",
        "meaningKo": "의료행위를 실시하기 전에 환자로부터 자발적으로 받는 동의를 의미합니다. 통역 시에는 단순 동의가 아닌 '충분한 설명을 듣고 이해한 후의 동의(informed consent)'임을 강조해야 하며, 동의서 서명만으로는 부족하고 실질적 설명과 이해가 있어야 함을 주의해야 합니다. 베트남에서는 가족 동의가 중요한 반면 한국은 본인 동의가 원칙이므로, 통역 시 양국의 동의 주체 차이를 명확히 하고 응급상황 등 예외 사유도 함께 설명해야 합니다.",
        "meaningVi": "Là sự đồng ý tự nguyện từ bệnh nhân trước khi thực hiện hành vi y tế. Không chỉ là ký vào giấy đồng ý, mà phải là 'đồng ý sau khi được giải thích đầy đủ và hiểu rõ' (informed consent). Nguyên tắc là bệnh nhân tự quyết định, trừ trường hợp cấp cứu.",
        "context": "설명의무, 자기결정권, 의료행위",
        "culturalNote": "한국에서는 성인 환자 본인의 동의가 원칙이며, 의식 불명 등 특별한 경우에만 가족 동의로 대체합니다. 베트남에서는 가족, 특히 가장의 동의가 중요시되며 본인 동의만으로는 부족한 경우가 많습니다. 통역 시 동의 주체의 차이를 설명하고, 응급상황에서의 예외 규정과 대리 동의의 요건을 명확히 전달해야 합니다.",
        "commonMistakes": [
            {
                "mistake": "'chấp thuận' 또는 'đồng ý'로만 번역",
                "correction": "'đồng ý sau khi được giải thích đầy đủ' (informed consent)",
                "explanation": "단순 동의가 아닌 충분한 설명을 들은 후의 동의임을 명시해야 합니다."
            },
            {
                "mistake": "동의 주체를 명시하지 않음",
                "correction": "본인 동의(đồng ý của bản thân) 원칙 명시",
                "explanation": "한국은 본인 동의가 원칙이므로 가족 동의와 구분해야 합니다."
            },
            {
                "mistake": "응급상황 예외를 설명하지 않음",
                "correction": "cấp cứu (응급) 시 예외 규정 추가",
                "explanation": "응급상황에서는 동의 없이도 의료행위가 가능하므로 예외를 설명해야 합니다."
            }
        ],
        "examples": [
            {
                "ko": "수술을 위해서는 반드시 환자동의를 받아야 합니다.",
                "vi": "Để thực hiện phẫu thuật, nhất thiết phải có đồng ý bệnh nhân.",
                "situation": "formal"
            },
            {
                "ko": "환자동의 없이 진행한 의료행위는 위법입니다.",
                "vi": "Hành vi y tế thực hiện mà không có đồng ý bệnh nhân là vi phạm pháp luật.",
                "situation": "onsite"
            },
            {
                "ko": "응급상황에서는 환자동의 없이도 치료할 수 있습니다.",
                "vi": "Trong tình huống cấp cứu, có thể điều trị mà không cần đồng ý bệnh nhân.",
                "situation": "formal"
            }
        ],
        "relatedTerms": ["설명의무", "자기결정권", "동의서", "응급의료"]
    },
    {
        "slug": "tu-choi-kham-chua",
        "korean": "진료거부",
        "vietnamese": "Từ chối khám chữa",
        "hanja": "診療拒否",
        "hanjaReading": "診(살필 진) + 療(고칠 료) + 拒(막을 거) + 否(아닐 부)",
        "pronunciation": "진료거부",
        "meaningKo": "의료인이 정당한 사유 없이 환자의 진료 요청을 거부하는 행위를 의미합니다. 통역 시에는 무조건 진료해야 하는 것이 아니라 '정당한 사유'가 있으면 거부할 수 있음을 설명해야 하며, 응급환자는 원칙적으로 거부할 수 없음을 강조해야 합니다. 베트남에서는 진료거부 개념이 명확하지 않으므로, 통역 시 진료거부가 허용되는 경우(전문 분야 외, 진료 시간 외 등)와 금지되는 경우(응급, 차별적 거부)를 구체적으로 설명해야 합니다.",
        "meaningVi": "Là hành vi nhân viên y tế từ chối yêu cầu khám chữa bệnh của bệnh nhân mà không có lý do chính đáng. Nguyên tắc là không được từ chối, nhưng có thể từ chối trong một số trường hợp như ngoài chuyên môn, ngoài giờ khám. Tuyệt đối không được từ chối bệnh nhân cấp cứu.",
        "context": "응급의료, 의료윤리, 의료법",
        "culturalNote": "한국에서는 의료법상 정당한 사유 없는 진료거부가 금지되며, 특히 응급환자 진료거부는 처벌 대상입니다. 베트남에서는 진료거부에 대한 법적 규제가 약하며, 병원의 재량이 큽니다. 통역 시 한국의 응급의료법상 응급환자 진료 의무와 거부 시 형사처벌(업무상과실치사상) 가능성을 명확히 전달하고, 정당한 거부 사유를 구체적으로 설명해야 합니다.",
        "commonMistakes": [
            {
                "mistake": "'không khám' 또는 'từ chối'로만 번역",
                "correction": "'từ chối khám chữa không chính đáng' (정당성 강조)",
                "explanation": "정당한 사유가 있으면 거부할 수 있으므로 '부당한 거부'임을 명시해야 합니다."
            },
            {
                "mistake": "응급환자 예외를 명시하지 않음",
                "correction": "bệnh nhân cấp cứu (응급환자) 거부 금지 명시",
                "explanation": "응급환자는 어떤 경우에도 거부할 수 없으므로 반드시 구분해야 합니다."
            },
            {
                "mistake": "정당한 거부 사유를 설명하지 않음",
                "correction": "ngoài chuyên môn, ngoài giờ 등 정당 사유 예시",
                "explanation": "무조건 진료해야 하는 것이 아니므로 정당한 거부 사유를 설명해야 합니다."
            }
        ],
        "examples": [
            {
                "ko": "응급환자에 대한 진료거부는 법으로 금지되어 있습니다.",
                "vi": "Từ chối khám chữa bệnh nhân cấp cứu bị cấm theo luật.",
                "situation": "formal"
            },
            {
                "ko": "전문 분야가 아니라는 이유로 진료거부할 수 있습니다.",
                "vi": "Có thể từ chối khám chữa với lý do không phải chuyên môn của mình.",
                "situation": "onsite"
            },
            {
                "ko": "정당한 사유 없는 진료거부는 처벌 대상입니다.",
                "vi": "Từ chối khám chữa không có lý do chính đáng là đối tượng bị xử phạt.",
                "situation": "formal"
            }
        ],
        "relatedTerms": ["응급의료", "진료의무", "의료윤리", "환자권리"]
    },
    {
        "slug": "cap-cuu-y-te",
        "korean": "응급의료",
        "vietnamese": "Cấp cứu y tế",
        "hanja": "應急醫療",
        "hanjaReading": "應(응할 응) + 急(급할 급) + 醫(고칠 의) + 療(고칠 료)",
        "pronunciation": "응급의료",
        "meaningKo": "생명이나 신체에 급박한 위험이 있는 환자에게 신속히 제공되는 의료를 의미합니다. 통역 시에는 단순 '빠른 치료'가 아닌 법적으로 정의된 '응급상황'에 대한 의료임을 강조해야 하며, 응급의료 제공 의무와 거부 시 처벌을 명확히 전달해야 합니다. 베트님에서는 응급의료 개념이 포괄적이므로, 통역 시 한국의 응급의료법상 응급환자 정의와 응급의료기관의 의무, 응급의료 거부 시 형사책임을 구체적으로 설명해야 합니다.",
        "meaningVi": "Là y tế được cung cấp nhanh chóng cho bệnh nhân có nguy cơ khẩn cấp đối với tính mạng hoặc cơ thể. Theo Luật Y tế cấp cứu Hàn Quốc, cơ sở y tế không được từ chối bệnh nhân cấp cứu, và nếu từ chối có thể bị truy cứu trách nhiệm hình sự.",
        "context": "응급환자, 진료거부, 의료법",
        "culturalNote": "한국에서는 응급의료법으로 응급환자와 응급의료기관이 명확히 정의되어 있으며, 응급환자 진료 거부 시 형사처벌됩니다. 베트남에서는 응급의료 개념이 넓으며, 법적 규제보다는 의료기관의 재량이 큽니다. 통역 시 한국의 응급의료체계(119 구급차, 응급실 운영, 응급의료정보센터)와 응급환자 우선 진료 원칙, 동의 없이도 치료 가능한 법적 근거를 설명해야 합니다.",
        "commonMistakes": [
            {
                "mistake": "'khẩn cấp' 또는 'cấp tốc'으로 번역",
                "correction": "'cấp cứu y tế' (법적 용어)",
                "explanation": "khẩn cấp은 일반적 긴급을 의미하며, cấp cứu가 의료 분야의 법적 용어입니다."
            },
            {
                "mistake": "응급환자 정의를 명시하지 않음",
                "correction": "bệnh nhân có nguy cơ đối với tính mạng (생명 위험) 명시",
                "explanation": "응급의료는 법적으로 정의된 응급환자에게만 적용되므로 정의를 명확히 해야 합니다."
            },
            {
                "mistake": "진료 거부 금지를 강조하지 않음",
                "correction": "không được từ chối (거부 금지) 강조",
                "explanation": "응급의료의 핵심은 거부 금지이므로 반드시 강조해야 합니다."
            }
        ],
        "examples": [
            {
                "ko": "응급의료기관은 응급환자를 거부할 수 없습니다.",
                "vi": "Cơ sở y tế cấp cứu không được từ chối bệnh nhân cấp cứu.",
                "situation": "formal"
            },
            {
                "ko": "응급의료 상황에서는 환자 동의 없이도 치료할 수 있습니다.",
                "vi": "Trong tình huống cấp cứu y tế, có thể điều trị mà không cần đồng ý bệnh nhân.",
                "situation": "onsite"
            },
            {
                "ko": "응급의료 거부로 환자가 사망하면 형사처벌됩니다.",
                "vi": "Nếu bệnh nhân tử vong do từ chối cấp cứu y tế, sẽ bị truy cứu trách nhiệm hình sự.",
                "situation": "formal"
            }
        ],
        "relatedTerms": ["응급환자", "진료거부", "환자동의", "의료과실"]
    },
    {
        "slug": "cay-ghep-noi-tang",
        "korean": "장기이식",
        "vietnamese": "Cấy ghép nội tạng",
        "hanja": "臟器移植",
        "hanjaReading": "臟(오장 장) + 器(그릇 기) + 移(옮길 이) + 植(심을 식)",
        "pronunciation": "장기이식",
        "meaningKo": "사람의 장기를 적출하여 다른 사람의 신체에 이식하는 의료행위를 의미합니다. 통역 시에는 단순 의료 시술이 아닌 엄격한 법적 규제 대상임을 강조해야 하며, 뇌사자 장기이식과 생체 장기이식을 구분하고 기증 동의 절차의 중요성을 설명해야 합니다. 베트남에서는 장기이식이 드물고 법적 규제가 약하므로, 통역 시 한국의 장기이식법상 기증자/수혜자 요건, 장기매매 금지, 이식 윤리위원회 승인 절차를 상세히 설명해야 합니다.",
        "meaningVi": "Là hành vi y tế lấy nội tạng của người này để cấy ghép vào cơ thể người khác. Bao gồm cấy ghép từ người chết não và người sống. Theo pháp luật Hàn Quốc, bị cấm nghiêm ngặt mua bán nội tạng, và phải được Ủy ban Đạo đức cấy ghép phê duyệt.",
        "context": "장기기증, 뇌사, 의료윤리",
        "culturalNote": "한국에서는 장기이식법으로 뇌사 판정, 기증 동의, 이식 절차가 엄격히 규제되며, 장기매매는 중범죄입니다. 베트남에서는 장기이식이 매우 드물며, 가족 간 생체 이식이 대부분이고 뇌사 개념도 명확하지 않습니다. 통역 시 뇌사 판정 절차, 기증 동의 방식(본인 동의 vs 가족 동의), 이식 대기자 순위 결정 방식, 장기매매 금지와 처벌을 구체적으로 설명해야 합니다.",
        "commonMistakes": [
            {
                "mistake": "'ghép nội tạng'로만 번역",
                "correction": "'cấy ghép nội tạng' (법적 용어)",
                "explanation": "cấy ghép이 의료 및 법률 분야에서 사용되는 정확한 용어입니다."
            },
            {
                "mistake": "뇌사 이식과 생체 이식을 구분하지 않음",
                "correction": "từ người chết não/người sống 명시",
                "explanation": "법적 요건과 절차가 다르므로 반드시 구분해야 합니다."
            },
            {
                "mistake": "장기매매 금지를 강조하지 않음",
                "correction": "nghiêm cấm mua bán nội tạng (엄격 금지) 강조",
                "explanation": "장기매매는 중범죄이므로 금지 사항을 명확히 전달해야 합니다."
            }
        ],
        "examples": [
            {
                "ko": "장기이식을 위해서는 반드시 기증자의 동의가 필요합니다.",
                "vi": "Để thực hiện cấy ghép nội tạng, nhất thiết phải có sự đồng ý của người hiến tặng.",
                "situation": "formal"
            },
            {
                "ko": "뇌사자의 장기이식은 이식윤리위원회의 승인을 받아야 합니다.",
                "vi": "Cấy ghép nội tạng từ người chết não phải được Ủy ban Đạo đức cấy ghép phê duyệt.",
                "situation": "onsite"
            },
            {
                "ko": "장기매매는 법으로 엄격히 금지되어 있습니다.",
                "vi": "Mua bán nội tạng bị cấm nghiêm ngặt theo luật.",
                "situation": "formal"
            }
        ],
        "relatedTerms": ["장기기증", "뇌사", "장기매매", "의료윤리"]
    },
    {
        "slug": "quang-cao-y-te",
        "korean": "의료광고",
        "vietnamese": "Quảng cáo y tế",
        "hanja": "醫療廣告",
        "hanjaReading": "醫(고칠 의) + 療(고칠 료) + 廣(넓을 광) + 告(알릴 고)",
        "pronunciation": "의료광고",
        "meaningKo": "의료기관이나 의료인이 자신의 의료 서비스를 알리는 광고 활동을 의미합니다. 통역 시에는 일반 광고와 달리 엄격한 법적 규제 대상임을 강조해야 하며, 허위·과장 광고 금지와 심의 절차의 중요성을 설명해야 합니다. 베트남에서도 의료광고 규제가 있지만 한국만큼 엄격하지 않으므로, 통역 시 한국의 의료법상 광고 금지 사항(비교광고, 환자 유치 목적 광고), 광고 가능 항목, 심의 절차, 위반 시 처벌을 구체적으로 설명해야 합니다.",
        "meaningVi": "Là hoạt động quảng cáo mà cơ sở y tế hoặc nhân viên y tế thông báo về dịch vụ y tế của mình. Theo Luật Y tế Hàn Quốc, bị cấm nghiêm ngặt quảng cáo gian dối, phóng đại, và phải qua thẩm định trước khi quảng cáo. Quảng cáo nhằm mục đích thu hút bệnh nhân cũng bị cấm.",
        "context": "의료법, 허위광고, 과장광고",
        "culturalNote": "한국에서는 의료법으로 의료광고가 엄격히 규제되며, 비교광고, 환자 후기 등이 금지되고 모든 광고는 심의를 받아야 합니다. 베트남에서는 의료광고 규제가 있지만 실제로는 느슨하게 적용되는 경우가 많습니다. 통역 시 한국의 광고 심의 기관(한국의료광고심의위원회), 광고 가능 항목(진료과목, 시설, 장비 등), 금지 항목(치료 효과 보장, 환자 체험담 등), 위반 시 행정처분과 형사처벌을 상세히 설명해야 합니다.",
        "commonMistakes": [
            {
                "mistake": "'quảng cáo bệnh viện' 또는 'quảng cáo'로만 번역",
                "correction": "'quảng cáo y tế' (법적 용어)",
                "explanation": "일반 광고와 구분되는 법적 규제 대상임을 명확히 해야 합니다."
            },
            {
                "mistake": "허위·과장 광고 금지를 강조하지 않음",
                "correction": "cấm quảng cáo gian dối, phóng đại (금지 사항) 강조",
                "explanation": "의료광고의 핵심 규제 내용이므로 반드시 강조해야 합니다."
            },
            {
                "mistake": "심의 절차를 설명하지 않음",
                "correction": "phải qua thẩm định (심의 필수) 명시",
                "explanation": "모든 의료광고는 사전 심의를 받아야 하므로 절차를 설명해야 합니다."
            }
        ],
        "examples": [
            {
                "ko": "의료광고는 반드시 사전 심의를 받아야 합니다.",
                "vi": "Quảng cáo y tế nhất thiết phải được thẩm định trước.",
                "situation": "formal"
            },
            {
                "ko": "치료 효과를 보장하는 의료광고는 금지되어 있습니다.",
                "vi": "Quảng cáo y tế đảm bảo hiệu quả điều trị bị cấm.",
                "situation": "onsite"
            },
            {
                "ko": "허위 의료광고로 환자를 유치하면 처벌받습니다.",
                "vi": "Nếu thu hút bệnh nhân bằng quảng cáo y tế gian dối, sẽ bị xử phạt.",
                "situation": "formal"
            }
        ],
        "relatedTerms": ["허위광고", "과장광고", "의료법", "광고심의"]
    },
    {
        "slug": "phan-nghiep-y-duoc",
        "korean": "의약분업",
        "vietnamese": "Phân nghiệp y dược",
        "hanja": "醫藥分業",
        "hanjaReading": "醫(고칠 의) + 藥(약 약) + 分(나눌 분) + 業(업 업)",
        "pronunciation": "의약분업",
        "meaningKo": "의사는 처방하고 약사는 조제하도록 의료와 약무를 분리하는 제도를 의미합니다. 통역 시에는 단순 역할 분담이 아닌 법적으로 강제된 제도임을 강조해야 하며, 의약분업 위반(의사의 직접 약 판매, 약사의 처방전 없는 조제) 시 처벌을 명확히 전달해야 합니다. 베트남에서는 의약분업이 명확하지 않아 의사가 직접 약을 파는 경우가 많으므로, 통역 시 한국 제도의 목적(약물 오남용 방지, 전문성 강화)과 예외 사항(의료취약지, 한방)을 설명해야 합니다.",
        "meaningVi": "Là chế độ phân chia y tế và dược vụ, trong đó bác sĩ kê đơn và dược sĩ pha chế. Là chế độ bắt buộc theo luật Hàn Quốc, nhằm ngăn chặn lạm dụng thuốc và tăng cường chuyên môn. Vi phạm (bác sĩ bán thuốc trực tiếp, dược sĩ pha chế không có đơn) sẽ bị xử phạt.",
        "context": "의료법, 약사법, 처방전",
        "culturalNote": "한국에서는 2000년 의약분업이 시행되어 의사는 처방만, 약사는 조제만 하도록 법으로 강제되며, 위반 시 면허 정지 등 처벌을 받습니다. 베트남에서는 의약분업 개념이 약하며, 의사가 진료실에서 직접 약을 판매하는 경우가 일반적입니다. 통역 시 의약분업의 목적(전문성 강화, 약물 오남용 방지, 환자 안전), 예외 사항(의료취약지, 한약), 처방전 발급 의무, 위반 시 행정처분과 형사책임을 상세히 설명해야 합니다.",
        "commonMistakes": [
            {
                "mistake": "'tách y tế và dược'로 번역",
                "correction": "'phân nghiệp y dược' (법적 제도 용어)",
                "explanation": "단순 분리가 아닌 법적으로 강제된 업무 분담 제도임을 명확히 해야 합니다."
            },
            {
                "mistake": "제도의 목적을 설명하지 않음",
                "correction": "ngăn chặn lạm dụng thuốc (약물 오남용 방지) 등 목적 설명",
                "explanation": "제도의 취지를 이해해야 규정을 준수할 수 있으므로 목적을 설명해야 합니다."
            },
            {
                "mistake": "위반 시 처벌을 명시하지 않음",
                "correction": "đình chỉ giấy phép (면허 정지) 등 처벌 명시",
                "explanation": "법적 강제 사항이므로 위반 시 처벌을 명확히 전달해야 합니다."
            }
        ],
        "examples": [
            {
                "ko": "의약분업으로 의사는 처방만, 약사는 조제만 합니다.",
                "vi": "Do phân nghiệp y dược, bác sĩ chỉ kê đơn, dược sĩ chỉ pha chế.",
                "situation": "formal"
            },
            {
                "ko": "의약분업 위반 시 면허가 정지될 수 있습니다.",
                "vi": "Nếu vi phạm phân nghiệp y dược, giấy phép có thể bị đình chỉ.",
                "situation": "onsite"
            },
            {
                "ko": "의료취약지에서는 의약분업 예외가 인정됩니다.",
                "vi": "Tại khu vực thiếu y tế, được công nhận ngoại lệ phân nghiệp y dược.",
                "situation": "formal"
            }
        ],
        "relatedTerms": ["처방전", "조제", "약사법", "의료법"]
    },
    {
        "slug": "thu-nghiem-lam-sang",
        "korean": "임상시험",
        "vietnamese": "Thử nghiệm lâm sàng",
        "hanja": "臨床試驗",
        "hanjaReading": "臨(임할 임) + 床(평상 상) + 試(시험할 시) + 驗(시험할 험)",
        "pronunciation": "임상시험",
        "meaningKo": "의약품이나 의료기기의 안전성과 유효성을 확인하기 위해 사람을 대상으로 실시하는 시험을 의미합니다. 통역 시에는 단순 실험이 아닌 엄격한 윤리적·법적 규제 대상임을 강조해야 하며, 피험자 동의(informed consent), 임상시험심사위원회(IRB) 승인, 단계별 시험(1~4상)을 명확히 설명해야 합니다. 베트남에서는 임상시험이 드물고 규제가 약하므로, 통역 시 한국의 임상시험 절차, 피험자 보호 제도, 부작용 보고 의무, 중도 탈락 권리를 상세히 설명해야 합니다.",
        "meaningVi": "Là thử nghiệm thực hiện trên người nhằm xác nhận tính an toàn và hiệu quả của thuốc hoặc thiết bị y tế. Theo pháp luật Hàn Quốc, phải có sự đồng ý của người tham gia (informed consent), được Ủy ban Đánh giá Thử nghiệm Lâm sàng (IRB) phê duyệt, và chia thành các giai đoạn 1-4.",
        "context": "의약품, 의료기기, 피험자, IRB",
        "culturalNote": "한국에서는 약사법과 생명윤리법으로 임상시험이 엄격히 규제되며, IRB 승인, 피험자 동의, 부작용 보고가 필수입니다. 베트남에서는 임상시험 경험이 적고 규제가 약하며, 피험자 보호 제도도 미흡합니다. 통역 시 임상시험의 단계(1상: 안전성, 2상: 유효성, 3상: 대규모 검증, 4상: 시판 후 조사), 피험자 권리(자발적 참여, 중도 탈락, 부작용 보상), IRB의 역할, 동의서 내용을 구체적으로 설명해야 합니다.",
        "commonMistakes": [
            {
                "mistake": "'thí nghiệm' 또는 'thử nghiệm'로만 번역",
                "correction": "'thử nghiệm lâm sàng' (법적 용어)",
                "explanation": "일반 실험과 구분되는 의학 분야의 법적 용어임을 명확히 해야 합니다."
            },
            {
                "mistake": "피험자 동의를 강조하지 않음",
                "correction": "sự đồng ý của người tham gia (피험자 동의) 강조",
                "explanation": "임상시험의 핵심은 자발적 동의이므로 반드시 강조해야 합니다."
            },
            {
                "mistake": "IRB 승인을 설명하지 않음",
                "correction": "phê duyệt của Ủy ban IRB (IRB 승인) 명시",
                "explanation": "모든 임상시험은 IRB 승인을 받아야 하므로 절차를 설명해야 합니다."
            }
        ],
        "examples": [
            {
                "ko": "임상시험에 참여하려면 반드시 동의서에 서명해야 합니다.",
                "vi": "Để tham gia thử nghiệm lâm sàng, nhất thiết phải ký vào giấy đồng ý.",
                "situation": "formal"
            },
            {
                "ko": "이 약은 임상시험 3상을 진행 중입니다.",
                "vi": "Thuốc này đang tiến hành thử nghiệm lâm sàng giai đoạn 3.",
                "situation": "onsite"
            },
            {
                "ko": "임상시험 중 부작용이 발생하면 즉시 보고해야 합니다.",
                "vi": "Nếu xảy ra tác dụng phụ trong thử nghiệm lâm sàng, phải báo cáo ngay lập tức.",
                "situation": "formal"
            }
        ],
        "relatedTerms": ["피험자", "IRB", "부작용", "임상시험승인"]
    }
]

def add_terms_to_json(file_path, new_terms):
    """JSON 파일에 새 용어 추가"""
    # 기존 파일 읽기
    try:
        with open(file_path, 'r', encoding='utf-8') as f:
            data = json.load(f)
    except FileNotFoundError:
        print(f"❌ 파일을 찾을 수 없습니다: {file_path}")
        return False

    # 기존 slug 목록
    existing_slugs = {term['slug'] for term in data}

    # 중복 확인 및 추가
    added_count = 0
    for term in new_terms:
        if term['slug'] in existing_slugs:
            print(f"⚠️  중복: {term['slug']} (건너뜀)")
        else:
            data.append(term)
            existing_slugs.add(term['slug'])
            added_count += 1
            print(f"✅ 추가: {term['korean']} ({term['slug']})")

    # 파일 저장 (들여쓰기 2칸, 유니코드 그대로, 마지막 줄바꿈 추가)
    with open(file_path, 'w', encoding='utf-8') as f:
        json.dump(data, f, ensure_ascii=False, indent=2)
        f.write('\n')  # 마지막 줄바꿈

    print(f"\n✅ 총 {added_count}개 용어 추가 완료!")
    print(f"📁 파일: {file_path}")
    print(f"📊 전체 용어 수: {len(data)}개")

    return True

if __name__ == "__main__":
    # 법률 도메인 파일 경로
    LEGAL_JSON = os.path.join(
        os.path.dirname(os.path.dirname(__file__)),
        'data',
        'terms',
        'legal.json'
    )

    print("=" * 60)
    print("한-베 통역 용어 플랫폼 - 법률 도메인 용어 추가")
    print("테마: 의료과오/의료사고법 (Medical Malpractice Law)")
    print("=" * 60)
    print()

    # 용어 추가 실행
    add_terms_to_json(LEGAL_JSON, NEW_TERMS)

    print()
    print("=" * 60)
    print("🎉 작업 완료!")
    print("=" * 60)
