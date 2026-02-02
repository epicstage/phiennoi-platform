#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
법률직업/법조윤리 용어 추가 스크립트
Legal Profession/Ethics Terms Addition Script

Theme: 법률직업/법조윤리 (Legal Profession/Ethics)
Target: 10 terms - Tier S quality (90+ score)
"""

import json
import os

# 파일 경로 설정 (CRITICAL: relative path from script location)
file_path = os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', 'data', 'terms', 'legal.json')

# 기존 데이터 로드
with open(file_path, 'r', encoding='utf-8') as f:
    data = json.load(f)  # data is a LIST, not dict!

# 기존 slug 수집 (중복 방지)
existing_slugs = {t['slug'] for t in data}

# 새 용어 정의
new_terms = [
    {
        "slug": "luat-su-bao-chua",
        "korean": "변호인",
        "vietnamese": "Luật sư bào chữa",
        "hanja": "辯護人",
        "hanjaReading": "辯(말씀할 변) + 護(지킬 호) + 人(사람 인)",
        "pronunciation": "루엇 스 바오 쭈아",
        "meaningKo": "형사소송에서 피의자 또는 피고인의 권익을 보호하고 변론하는 법률 전문가를 의미합니다. 통역 시 주의할 점은 베트남에서는 변호인 선임권이 한국보다 제한적이며, 특히 국가안보 관련 사건에서는 정부 지정 변호인만 가능한 경우가 있습니다. 또한 베트남의 변호인은 수사 단계에서의 접근권이 한국보다 제한적이므로, 변호인의 역할 범위에 대한 양국 간 차이를 명확히 설명해야 합니다. '변호사'와 구분하여 형사 사건의 방어권 행사자임을 강조해야 합니다.",
        "meaningVi": "Chuyên gia pháp lý bảo vệ quyền và lợi ích của nghi phạm hoặc bị cáo trong tố tụng hình sự, đại diện thực hiện quyền biện hộ. Tại Việt Nam, quyền chọn luật sư bào chữa có thể bị hạn chế trong một số vụ án liên quan đến an ninh quốc gia, chỉ được chỉ định luật sư do nhà nước chỉ định. Quyền tiếp cận của luật sư bào chữa trong giai đoạn điều tra cũng hạn chế hơn so với Hàn Quốc.",
        "context": "형사소송/법률대리",
        "culturalNote": "한국에서는 변호인의 조력을 받을 권리가 헌법상 기본권으로 강력하게 보장되며, 수사 초기 단계부터 변호인 접견이 원칙적으로 보장됩니다. 반면 베트남에서는 국가안보 관련 사건이나 중대 범죄의 경우 변호인 선임과 접견에 제한이 있을 수 있으며, 변호인의 역할이 한국보다 제한적인 경우가 많습니다. 또한 베트남에서는 변호인의 독립성이 한국만큼 강하지 않아, 국가 기관과의 관계에서 제약을 받을 수 있습니다.",
        "commonMistakes": [
            {
                "mistake": "변호사와 변호인을 동일하게 번역",
                "correction": "변호사는 'Luật sư', 변호인은 'Luật sư bào chữa'로 구분",
                "explanation": "변호사는 법률 전문가 자격을, 변호인은 형사 사건의 방어 역할을 의미하므로 명확히 구분해야 합니다."
            },
            {
                "mistake": "베트남에서도 한국과 동일한 변호인 권리를 설명",
                "correction": "양국의 변호인 권리 범위 차이를 명확히 설명",
                "explanation": "베트남의 변호인 접근권과 활동 범위가 한국과 다르므로, 이를 정확히 안내해야 오해를 방지할 수 있습니다."
            },
            {
                "mistake": "'Luật sư biện hộ'로 번역",
                "correction": "'Luật sư bào chữa'가 공식 용어",
                "explanation": "베트남 법률에서 공식적으로 사용하는 용어는 'bào chữa'입니다."
            }
        ],
        "examples": [
            {
                "ko": "피고인은 변호인의 조력을 받을 권리가 있습니다.",
                "vi": "Bị cáo có quyền được luật sư bào chữa hỗ trợ.",
                "situation": "formal"
            },
            {
                "ko": "변호인은 피의자와 자유롭게 접견할 수 있어야 합니다.",
                "vi": "Luật sư bào chữa phải được tự do gặp gỡ nghi phạm.",
                "situation": "formal"
            },
            {
                "ko": "국선 변호인이 선임되었습니다.",
                "vi": "Luật sư bào chữa do nhà nước chỉ định đã được chỉ định.",
                "situation": "onsite"
            }
        ],
        "relatedTerms": ["변호사", "피고인", "형사소송"]
    },
    {
        "slug": "cong-chung-vien",
        "korean": "공증인",
        "vietnamese": "Công chứng viên",
        "hanja": "公證人",
        "hanjaReading": "公(공평할 공) + 證(증거 증) + 人(사람 인)",
        "pronunciation": "꽁 쯩 비엔",
        "meaningKo": "법률행위나 사실관계에 대해 공적으로 증명하는 권한을 가진 법률 전문가를 의미합니다. 통역 시 주의할 점은 한국에서는 공증인이 주로 변호사나 법무사가 맡지만, 베트남에서는 국가 공무원으로서 공증 사무소에 소속되어 있습니다. 양국의 공증 제도와 공증 대상 범위가 다르므로, 특히 부동산 거래나 계약서 공증 시 양국의 법적 효력 차이를 명확히 설명해야 합니다. 베트남에서는 공증이 한국보다 더 광범위하게 요구되는 경향이 있습니다.",
        "meaningVi": "Chuyên gia pháp lý có thẩm quyền chứng thực công việc hành vi pháp lý hoặc quan hệ thực tế một cách chính thức. Tại Việt Nam, công chứng viên là công chức nhà nước thuộc tổ chức công chứng nhà nước, khác với Hàn Quốc nơi luật sư hoặc pháp vụ có thể đảm nhận vai trò này. Phạm vi công chứng tại Việt Nam rộng hơn và bắt buộc hơn so với Hàn Quốc.",
        "context": "공증/법률인증",
        "culturalNote": "한국에서는 공증인이 주로 사법 체계 내에서 민간 전문가로 활동하며, 공증의 강제성이 상대적으로 낮습니다. 반면 베트남에서는 공증인이 국가 공무원이며, 많은 법률 행위(특히 부동산 거래, 결혼, 상속 등)에서 공증이 법적으로 강제되어 있습니다. 베트남의 공증 제도는 중앙 집중식이며, 공증 사무소가 정부 기관으로 운영됩니다. 양국 간 공증 서류의 상호 인정 문제도 통역 시 중요한 사항입니다.",
        "commonMistakes": [
            {
                "mistake": "한국과 베트남의 공증인 지위를 동일하게 설명",
                "correction": "베트남은 국가 공무원, 한국은 민간 전문가임을 구분",
                "explanation": "공증인의 법적 지위와 소속이 양국에서 근본적으로 다르므로 명확히 구분해야 합니다."
            },
            {
                "mistake": "공증 범위를 동일하게 간주",
                "correction": "베트남이 공증 의무 범위가 더 넓음을 설명",
                "explanation": "베트남에서는 한국에서 공증이 선택 사항인 경우도 의무적으로 공증을 요구하는 경우가 많습니다."
            },
            {
                "mistake": "'Người công chứng'으로 번역",
                "correction": "'Công chứng viên'이 공식 용어",
                "explanation": "베트남 법률에서 공식적으로 사용하는 직함은 'Công chứng viên'입니다."
            }
        ],
        "examples": [
            {
                "ko": "이 계약서는 공증인의 인증이 필요합니다.",
                "vi": "Hợp đồng này cần được công chứng viên chứng thực.",
                "situation": "formal"
            },
            {
                "ko": "공증 사무소에서 서명을 확인받으세요.",
                "vi": "Hãy xác nhận chữ ký tại văn phòng công chứng.",
                "situation": "onsite"
            },
            {
                "ko": "부동산 매매 계약은 반드시 공증을 받아야 합니다.",
                "vi": "Hợp đồng mua bán bất động sản bắt buộc phải được công chứng.",
                "situation": "formal"
            }
        ],
        "relatedTerms": ["공증", "인증", "계약서"]
    },
    {
        "slug": "chap-hanh-vien",
        "korean": "집행관",
        "vietnamese": "Chấp hành viên",
        "hanja": "執行官",
        "hanjaReading": "執(잡을 집) + 行(다닐 행) + 官(벼슬 관)",
        "pronunciation": "쩝 한 비엔",
        "meaningKo": "법원의 판결이나 결정을 강제로 집행하는 권한을 가진 법원 소속 공무원을 의미합니다. 통역 시 주의할 점은 한국의 집행관은 법원에 소속되어 민사집행법에 따라 활동하지만, 베트남의 집행관은 법무부 산하 별도 조직에 소속되어 있으며 집행 절차와 권한이 다릅니다. 특히 베트남에서는 판결 집행률이 한국보다 낮고, 집행 과정에서 많은 실무적 어려움이 있으므로, 집행 가능성에 대해 현실적인 기대치를 설명해야 합니다.",
        "meaningVi": "Công chức thuộc cơ quan thi hành án dân sự, có thẩm quyền cưỡng chế thi hành các bản án, quyết định của tòa án. Tại Việt Nam, chấp hành viên thuộc Cục Thi hành án dân sự trực thuộc Bộ Tư pháp, khác với Hàn Quốc nơi họ là nhân viên tòa án. Tỷ lệ thi hành án thành công tại Việt Nam thấp hơn Hàn Quốc và quá trình thi hành thường gặp nhiều khó khăn thực tế.",
        "context": "강제집행/판결집행",
        "culturalNote": "한국에서는 집행관 제도가 체계적으로 운영되며, 강제집행이 비교적 효율적으로 이루어집니다. 반면 베트남에서는 집행 기관이 법원과 분리되어 있고, 판결을 받아도 실제 집행이 어려운 경우가 많습니다. 특히 채무자의 재산 파악이 어렵고, 집행 회피 수단이 다양하며, 집행관의 권한이 제한적인 경우가 있습니다. 베트남에서는 판결 승소보다 실제 집행 성공이 더 어려운 과제로 인식되고 있습니다.",
        "commonMistakes": [
            {
                "mistake": "한국과 동일한 집행 효율성을 기대하게 설명",
                "correction": "베트남의 낮은 집행률과 어려움을 명확히 안내",
                "explanation": "베트남에서는 판결을 받아도 집행이 어려운 경우가 많아, 현실적인 기대치를 설정해야 합니다."
            },
            {
                "mistake": "집행관의 소속을 법원으로 설명",
                "correction": "베트남은 법무부 산하 별도 조직임을 명시",
                "explanation": "양국의 집행 기관 구조가 다르므로 정확한 소속 관계를 설명해야 합니다."
            },
            {
                "mistake": "'Người thi hành'으로 번역",
                "correction": "'Chấp hành viên'이 공식 용어",
                "explanation": "베트남 법률에서 공식적으로 사용하는 직함은 'Chấp hành viên'입니다."
            }
        ],
        "examples": [
            {
                "ko": "집행관이 압류 집행을 실시했습니다.",
                "vi": "Chấp hành viên đã thực hiện thi hành kê biên.",
                "situation": "formal"
            },
            {
                "ko": "판결문을 집행관에게 제출하세요.",
                "vi": "Hãy nộp bản án cho chấp hành viên.",
                "situation": "onsite"
            },
            {
                "ko": "집행관은 채무자의 재산을 조사할 권한이 있습니다.",
                "vi": "Chấp hành viên có quyền điều tra tài sản của con nợ.",
                "situation": "formal"
            }
        ],
        "relatedTerms": ["강제집행", "압류", "판결"]
    },
    {
        "slug": "tham-tra-vien",
        "korean": "조사관",
        "vietnamese": "Thẩm tra viên",
        "hanja": "調査官",
        "hanjaReading": "調(고를 조) + 査(살필 사) + 官(벼슬 관)",
        "pronunciation": "탐 짜 비엔",
        "meaningKo": "법원이나 수사기관에서 사건의 사실관계를 조사하고 분석하는 전문 공무원을 의미합니다. 통역 시 주의할 점은 한국의 조사관은 법원 소속으로 중립적 입장에서 사건을 조사하지만, 베트남의 조사관은 주로 수사 기관 소속으로 검찰이나 공안과 협력하여 활동합니다. 특히 베트남에서는 조사 과정에서 피의자의 권리 보장이 한국보다 약할 수 있으며, 조사관의 역할과 권한에 대해 양국 간 차이를 명확히 이해시켜야 합니다. 가정법원의 가사조사관과 구분하여 설명해야 합니다.",
        "meaningVi": "Công chức chuyên môn thuộc tòa án hoặc cơ quan điều tra, có nhiệm vụ điều tra và phân tích quan hệ sự thật của vụ án. Tại Việt Nam, thẩm tra viên chủ yếu thuộc cơ quan điều tra, phối hợp với viện kiểm sát và công an, khác với Hàn Quốc nơi họ thuộc tòa án và giữ lập trường trung lập. Quyền của nghi phạm trong quá trình điều tra tại Việt Nam có thể yếu hơn so với Hàn Quốc.",
        "context": "사법조사/사실조사",
        "culturalNote": "한국에서는 법원 조사관이 독립적이고 중립적인 위치에서 사건을 조사하며, 특히 가정법원에서 가사조사관의 역할이 중요합니다. 반면 베트남에서는 조사관이 주로 수사 단계에서 활동하며, 검찰과 공안의 지휘를 받는 경우가 많습니다. 베트남의 조사 절차는 한국보다 당사자의 권리 보호가 약하고, 조사 과정의 투명성이 낮을 수 있습니다. 또한 베트남에서는 조사관의 조사 결과가 재판에 큰 영향을 미치므로, 조사 단계에서의 대응이 매우 중요합니다.",
        "commonMistakes": [
            {
                "mistake": "조사관을 수사관과 동일하게 번역",
                "correction": "조사관은 'Thẩm tra viên', 수사관은 'Điều tra viên'으로 구분",
                "explanation": "조사관은 사실관계 조사에 초점을 두고, 수사관은 범죄 수사에 초점을 두므로 구분해야 합니다."
            },
            {
                "mistake": "한국과 동일한 중립성을 기대하게 설명",
                "correction": "베트남 조사관의 소속과 역할의 차이를 명확히 안내",
                "explanation": "베트남의 조사관은 수사 기관에 더 가까워, 중립성이 한국의 법원 조사관과 다릅니다."
            },
            {
                "mistake": "가사조사관을 단순히 '조사관'으로만 번역",
                "correction": "'Thẩm tra viên gia đình'으로 구체적으로 번역",
                "explanation": "가사 사건의 특수성을 반영하여 구체적으로 표현해야 합니다."
            }
        ],
        "examples": [
            {
                "ko": "법원 조사관이 가정환경을 조사할 것입니다.",
                "vi": "Thẩm tra viên tòa án sẽ điều tra môi trường gia đình.",
                "situation": "formal"
            },
            {
                "ko": "조사관의 보고서가 판결에 중요한 참고자료가 됩니다.",
                "vi": "Báo cáo của thẩm tra viên là tài liệu tham khảo quan trọng cho bản án.",
                "situation": "formal"
            },
            {
                "ko": "조사관과의 면담에 성실히 응해야 합니다.",
                "vi": "Cần trả lời thành thật trong cuộc phỏng vấn với thẩm tra viên.",
                "situation": "onsite"
            }
        ],
        "relatedTerms": ["수사관", "조사", "증거조사"]
    },
    {
        "slug": "vien-kiem-sat",
        "korean": "검찰",
        "vietnamese": "Viện kiểm sát",
        "hanja": "檢察",
        "hanjaReading": "檢(검사할 검) + 察(살필 찰)",
        "pronunciation": "비엔 끼엠 삿",
        "meaningKo": "범죄 수사와 기소, 공소 유지 및 재판 집행 감독을 담당하는 국가 기관을 의미합니다. 통역 시 주의할 점은 한국의 검찰은 법무부 소속이지만 독립적으로 운영되는 반면, 베트남의 검찰은 국회 직속 기관으로 법원과 동급이며 매우 강력한 권한을 가지고 있습니다. 베트남 검찰은 수사권과 기소권뿐 아니라 법령 준수 감독권까지 가지고 있어, 한국보다 훨씬 광범위한 권한을 행사합니다. 베트남에서 검찰의 의견은 재판에 매우 큰 영향을 미치므로, 검찰 단계에서의 대응이 중요함을 강조해야 합니다.",
        "meaningVi": "Cơ quan nhà nước thực hành quyền công tố, kiểm sát hoạt động tư pháp, kiểm sát việc tuân theo pháp luật. Tại Việt Nam, Viện kiểm sát nhân dân là cơ quan trực thuộc Quốc hội, có vị trí ngang hàng với tòa án và có thẩm quyền rất rộng, bao gồm cả giám sát việc tuân thủ pháp luật. Ý kiến của viện kiểm sát có ảnh hưởng rất lớn đến phán quyết của tòa án.",
        "context": "형사사법/공소제기",
        "culturalNote": "한국에서는 검찰이 수사와 기소를 주도하지만 법원의 독립성이 보장되고 재판 과정에서 검찰의 영향력이 제한적입니다. 반면 베트남에서는 검찰이 국회 직속 기관으로 매우 강력한 권한을 가지며, 재판 과정에서도 검찰의 의견이 큰 비중을 차지합니다. 베트남 검찰은 법령 준수 감독 기능까지 가지고 있어, 사실상 사법 시스템 전반에 영향력을 행사합니다. 이러한 검찰의 강력한 지위는 베트남 법체계의 특징이므로, 통역 시 이를 명확히 전달해야 합니다.",
        "commonMistakes": [
            {
                "mistake": "검찰을 단순히 'Công tố'로만 번역",
                "correction": "'Viện kiểm sát'이 공식 기관명",
                "explanation": "베트남에서 검찰 기관의 정식 명칭은 'Viện kiểm sát nhân dân'입니다."
            },
            {
                "mistake": "한국과 동일한 검찰의 지위로 설명",
                "correction": "베트남 검찰의 국회 직속 지위와 광범위한 권한을 강조",
                "explanation": "베트남 검찰의 헌법적 지위와 권한이 한국과 근본적으로 다르므로 명확히 구분해야 합니다."
            },
            {
                "mistake": "검찰의 역할을 기소만으로 제한",
                "correction": "법령 준수 감독 기능까지 포함하여 설명",
                "explanation": "베트남 검찰은 기소권 외에도 법령 준수 전반을 감독하는 광범위한 권한을 가집니다."
            }
        ],
        "examples": [
            {
                "ko": "검찰이 피의자를 기소했습니다.",
                "vi": "Viện kiểm sát đã truy tố nghi phạm.",
                "situation": "formal"
            },
            {
                "ko": "검찰의 수사 지휘를 받아야 합니다.",
                "vi": "Phải tuân theo chỉ đạo điều tra của viện kiểm sát.",
                "situation": "onsite"
            },
            {
                "ko": "검찰이 항소를 제기했습니다.",
                "vi": "Viện kiểm sát đã kháng cáo.",
                "situation": "formal"
            }
        ],
        "relatedTerms": ["검사", "기소", "공소"]
    },
    {
        "slug": "luat-su-tu-van",
        "korean": "법률자문",
        "vietnamese": "Luật sư tư vấn",
        "hanja": "法律諮問",
        "hanjaReading": "法(법 법) + 律(법 률) + 諮(물을 자) + 問(물을 문)",
        "pronunciation": "루엇 스 뜨 반",
        "meaningKo": "개인이나 기업에게 법률적 조언과 상담을 제공하는 변호사를 의미합니다. 통역 시 주의할 점은 한국에서는 법률자문이 계약 관계로 명확히 정의되고 비밀유지 의무가 엄격하지만, 베트남에서는 법률자문의 범위와 책임이 덜 명확한 경우가 있습니다. 특히 외국 기업의 경우 베트남 법률자문의 한계를 이해하고, 필요시 국제 법무법인의 자문을 병행하는 것이 좋습니다. 법률자문과 법률대리의 차이, 자문료 산정 방식 등에서 양국 간 차이가 있으므로 명확히 설명해야 합니다.",
        "meaningVi": "Luật sư cung cấp tư vấn và hỗ trợ pháp lý cho cá nhân hoặc doanh nghiệp. Tại Việt Nam, phạm vi và trách nhiệm của luật sư tư vấn có thể ít rõ ràng hơn so với Hàn Quốc, và nghĩa vụ bảo mật cũng không nghiêm ngặt bằng. Đối với doanh nghiệp nước ngoài, nên hiểu rõ giới hạn của tư vấn pháp lý tại Việt Nam và có thể kết hợp tư vấn từ công ty luật quốc tế khi cần thiết.",
        "context": "법률서비스/상담",
        "culturalNote": "한국에서는 법률자문이 계약서를 통해 명확히 정의되고, 자문 변호사의 비밀유지 의무와 책임 범위가 법적으로 보호됩니다. 반면 베트남에서는 법률자문 계약의 법적 구속력이 약하고, 자문의 질과 책임 범위가 변호사마다 차이가 큽니다. 또한 베트남에서는 법률자문료가 한국보다 저렴하지만, 서비스의 질과 전문성도 다양합니다. 외국 기업의 경우 베트남 로컬 법률과 국제 법률을 모두 이해하는 자문을 받는 것이 중요합니다.",
        "commonMistakes": [
            {
                "mistake": "법률자문과 법률대리를 혼동",
                "correction": "자문은 조언 제공, 대리는 법적 행위 대행임을 구분",
                "explanation": "법률자문은 조언을 제공하는 것이고, 법률대리는 법정에서 대리하는 것으로 범위가 다릅니다."
            },
            {
                "mistake": "한국과 동일한 자문 책임을 기대",
                "correction": "베트남의 법률자문 책임 범위가 덜 명확함을 안내",
                "explanation": "베트남에서는 법률자문의 법적 책임 범위가 한국만큼 명확하지 않을 수 있습니다."
            },
            {
                "mistake": "'Cố vấn pháp lý'로 번역",
                "correction": "'Luật sư tư vấn'이 더 정확한 표현",
                "explanation": "'Cố vấn pháp lý'는 일반 법률 고문을, 'Luật sư tư vấn'은 변호사 자격을 가진 자문을 의미합니다."
            }
        ],
        "examples": [
            {
                "ko": "계약서 검토를 위해 법률자문을 받으세요.",
                "vi": "Hãy nhận tư vấn pháp lý để xem xét hợp đồng.",
                "situation": "informal"
            },
            {
                "ko": "회사의 상시 법률자문 변호사입니다.",
                "vi": "Đây là luật sư tư vấn thường xuyên của công ty.",
                "situation": "formal"
            },
            {
                "ko": "이 문제는 전문 법률자문이 필요합니다.",
                "vi": "Vấn đề này cần tư vấn pháp lý chuyên môn.",
                "situation": "onsite"
            }
        ],
        "relatedTerms": ["변호사", "법률대리", "자문계약"]
    },
    {
        "slug": "van-phong-luat-su",
        "korean": "법률사무소",
        "vietnamese": "Văn phòng luật sư",
        "hanja": "法律事務所",
        "hanjaReading": "法(법 법) + 律(법 률) + 事(일 사) + 務(일 무) + 所(바 소)",
        "pronunciation": "번 퐁 루엇 스",
        "meaningKo": "변호사가 법률 업무를 수행하기 위해 개설한 사무소를 의미합니다. 통역 시 주의할 점은 한국의 법률사무소는 개인 또는 법인 형태로 다양하게 운영되며 규모와 전문 분야가 명확하지만, 베트남의 법률사무소는 대부분 소규모이며 전문화 수준이 낮은 편입니다. 베트남에서는 대형 국제 법무법인이 제한적으로 진출해 있고, 로컬 법률사무소의 서비스 품질 편차가 큽니다. 외국 기업이 베트남 법률사무소를 선택할 때는 실제 경험과 전문성을 신중히 검토해야 함을 안내해야 합니다.",
        "meaningVi": "Văn phòng được luật sư thành lập để thực hiện các hoạt động pháp lý. Tại Việt Nam, hầu hết các văn phòng luật sư có quy mô nhỏ và mức độ chuyên môn hóa thấp hơn so với Hàn Quốc. Các công ty luật quốc tế lớn có mặt hạn chế, và chất lượng dịch vụ của các văn phòng luật địa phương có sự chênh lệch lớn. Doanh nghiệp nước ngoài cần xem xét kỹ kinh nghiệm và chuyên môn thực tế khi chọn văn phòng luật tại Việt Nam.",
        "context": "법률서비스/법무법인",
        "culturalNote": "한국에서는 법률사무소가 개인 사무소부터 수천 명 규모의 대형 법무법인까지 다양하며, 전문 분야별로 특화되어 있습니다. 반면 베트남에서는 대부분 소규모 법률사무소가 일반 법률 업무를 처리하고, 대형 법무법인은 주로 외국계 기업 대상 업무에 집중합니다. 베트남의 법률사무소는 한국만큼 전문화되지 않았고, 국제적 기준의 서비스를 제공하는 곳이 제한적입니다. 또한 베트남에서는 법률사무소 간 네트워크와 협업이 한국보다 약합니다.",
        "commonMistakes": [
            {
                "mistake": "법률사무소를 단순히 'Văn phòng'으로만 번역",
                "correction": "'Văn phòng luật sư'로 완전하게 표현",
                "explanation": "법률사무소임을 명확히 하기 위해 'luật sư'를 포함해야 합니다."
            },
            {
                "mistake": "한국의 대형 법무법인과 동일한 수준 기대",
                "correction": "베트남 법률사무소의 규모와 전문성 차이를 설명",
                "explanation": "베트남의 법률사무소는 대부분 소규모이며, 한국의 대형 법무법인과는 다른 서비스를 제공합니다."
            },
            {
                "mistake": "'Công ty luật'와 'Văn phòng luật sư'를 혼용",
                "correction": "법인은 'Công ty luật', 개인/소규모는 'Văn phòng luật sư'",
                "explanation": "조직 형태에 따라 용어를 구분하여 사용해야 합니다."
            }
        ],
        "examples": [
            {
                "ko": "이 법률사무소는 기업 법무에 특화되어 있습니다.",
                "vi": "Văn phòng luật sư này chuyên về pháp lý doanh nghiệp.",
                "situation": "formal"
            },
            {
                "ko": "법률사무소에 상담 예약을 하세요.",
                "vi": "Hãy đặt lịch tư vấn tại văn phòng luật sư.",
                "situation": "informal"
            },
            {
                "ko": "대형 법률사무소의 자문을 받는 것이 좋겠습니다.",
                "vi": "Nên nhận tư vấn từ văn phòng luật sư lớn.",
                "situation": "onsite"
            }
        ],
        "relatedTerms": ["변호사", "법무법인", "법률자문"]
    },
    {
        "slug": "phi-luat-su",
        "korean": "변호사비용",
        "vietnamese": "Phí luật sư",
        "hanja": "辯護士費用",
        "hanjaReading": "辯(말씀할 변) + 護(지킬 호) + 士(선비 사) + 費(쓸 비) + 用(쓸 용)",
        "pronunciation": "피 루엇 스",
        "meaningKo": "변호사에게 법률 서비스를 받는 대가로 지불하는 비용을 의미합니다. 통역 시 주의할 점은 한국과 베트남의 변호사비용 산정 방식과 수준이 크게 다릅니다. 한국은 대한변호사협회의 보수기준이 있고 시간당 요율제가 일반적이지만, 베트남은 협상에 의한 성공보수제가 많고 비용이 상대적으로 저렴합니다. 그러나 베트남에서는 공식 비용 외에 비공식 비용이 발생할 수 있으며, 특히 복잡한 사건이나 외국인 관련 사건에서는 비용이 크게 증가할 수 있습니다. 비용 산정 방식과 지급 조건을 사전에 명확히 계약서에 명시해야 합니다.",
        "meaningVi": "Chi phí trả cho luật sư để nhận dịch vụ pháp lý. Tại Việt Nam, cách tính và mức phí luật sư khác biệt lớn so với Hàn Quốc. Trong khi Hàn Quốc có tiêu chuẩn phí của Hiệp hội Luật sư và thường tính theo giờ, Việt Nam chủ yếu tính phí theo thỏa thuận và phí thành công, với mức phí tương đối thấp hơn. Tuy nhiên, tại Việt Nam có thể phát sinh chi phí không chính thức ngoài phí chính thức, và chi phí có thể tăng đáng kể trong các vụ án phức tạp hoặc liên quan đến người nước ngoài.",
        "context": "법률비용/수임료",
        "culturalNote": "한국에서는 변호사비용이 투명하게 산정되고 계약서에 명시되며, 대한변호사협회의 보수기준이 참고 기준으로 작용합니다. 시간당 요율제, 사건 단위 정액제, 성공보수제 등이 명확히 구분됩니다. 반면 베트남에서는 변호사비용 산정이 덜 투명하고, 협상에 따라 크게 달라집니다. 베트남에서는 성공보수제가 흔하며, 공식적인 변호사비용 외에 추가 비용이 발생할 가능성을 염두에 두어야 합니다. 외국인의 경우 현지 상황에 익숙하지 않아 과도한 비용을 청구받을 수 있으므로 주의가 필요합니다.",
        "commonMistakes": [
            {
                "mistake": "한국의 변호사비용 수준을 베트남에 적용",
                "correction": "베트남이 일반적으로 저렴하지만 사건에 따라 다름을 설명",
                "explanation": "베트남의 변호사비용은 한국보다 저렴하지만, 복잡한 사건이나 외국인 관련 사건은 높을 수 있습니다."
            },
            {
                "mistake": "공식 비용만으로 예산 책정",
                "correction": "비공식 비용 발생 가능성을 안내",
                "explanation": "베트남에서는 공식 변호사비용 외에 추가 비용이 발생할 수 있으므로 여유를 두어야 합니다."
            },
            {
                "mistake": "'Chi phí luật sư'로만 번역",
                "correction": "'Phí luật sư'가 더 간결하고 일반적",
                "explanation": "'Phí'가 비용을 의미하므로 'Chi phí'는 중복적입니다."
            }
        ],
        "examples": [
            {
                "ko": "변호사비용은 사건의 복잡도에 따라 달라집니다.",
                "vi": "Phí luật sư thay đổi tùy theo mức độ phức tạp của vụ án.",
                "situation": "formal"
            },
            {
                "ko": "착수금과 성공보수를 별도로 지급합니다.",
                "vi": "Thanh toán riêng phí ban đầu và phí thành công.",
                "situation": "onsite"
            },
            {
                "ko": "변호사비용 견적서를 받아보세요.",
                "vi": "Hãy nhận báo giá phí luật sư.",
                "situation": "informal"
            }
        ],
        "relatedTerms": ["착수금", "성공보수", "수임료"]
    },
    {
        "slug": "bao-mat-thong-tin",
        "korean": "비밀유지",
        "vietnamese": "Bảo mật thông tin",
        "hanja": "秘密維持",
        "hanjaReading": "秘(숨길 비) + 密(빽빽할 밀) + 維(맬 유) + 持(가질 지)",
        "pronunciation": "바오 맛 통 띤",
        "meaningKo": "변호사나 법률 전문가가 직무상 알게 된 의뢰인의 정보를 외부에 공개하지 않을 의무를 의미합니다. 통역 시 주의할 점은 한국에서는 변호사의 비밀유지 의무가 법적으로 강력하게 보호되고, 위반 시 엄격한 제재를 받지만, 베트남에서는 비밀유지 의무의 법적 구속력이 상대적으로 약합니다. 특히 국가안보와 관련된 사항이나 정부 기관의 요구가 있을 경우 베트남에서는 비밀유지가 제한될 수 있습니다. 외국 기업이 베트남 변호사와 작업할 때는 명시적인 비밀유지 계약을 체결하고, 민감한 정보의 취급에 특별히 주의해야 합니다.",
        "meaningVi": "Nghĩa vụ của luật sư hoặc chuyên gia pháp lý không tiết lộ thông tin khách hàng mà họ biết được trong quá trình làm việc. Tại Việt Nam, nghĩa vụ bảo mật của luật sư có hiệu lực pháp lý tương đối yếu hơn so với Hàn Quốc, và có thể bị hạn chế trong các vấn đề liên quan đến an ninh quốc gia hoặc theo yêu cầu của cơ quan chính phủ. Doanh nghiệp nước ngoài nên ký hợp đồng bảo mật rõ ràng với luật sư Việt Nam và đặc biệt cẩn thận với thông tin nhạy cảm.",
        "context": "법률윤리/직업윤리",
        "culturalNote": "한국에서는 변호사의 비밀유지 의무가 변호사법과 형법으로 이중 보호되며, 위반 시 형사처벌까지 가능합니다. 변호사-의뢰인 특권(attorney-client privilege)이 강력하게 인정됩니다. 반면 베트남에서는 비밀유지 의무가 주로 직업윤리 차원에서 규율되고, 법적 제재가 약합니다. 특히 정부 기관의 조사나 국가안보 관련 사항에서는 변호사도 정보 제공을 요구받을 수 있습니다. 베트남에서 민감한 사업 정보나 개인정보를 다룰 때는 추가적인 보호 조치가 필요합니다.",
        "commonMistakes": [
            {
                "mistake": "한국과 동일한 비밀유지 보호를 기대",
                "correction": "베트남의 약한 법적 보호와 제한 가능성을 안내",
                "explanation": "베트남에서는 비밀유지 의무의 법적 구속력이 약하고 예외 사항이 많습니다."
            },
            {
                "mistake": "'Giữ bí mật'로 번역",
                "correction": "'Bảo mật thông tin'이 공식적 표현",
                "explanation": "'Bảo mật thông tin'이 법률 및 계약서에서 사용하는 공식 용어입니다."
            },
            {
                "mistake": "계약서 없이 비밀유지를 당연시",
                "correction": "명시적 비밀유지 계약 체결 필요성 강조",
                "explanation": "베트남에서는 비밀유지 의무가 자동으로 보장되지 않으므로 계약으로 명시해야 합니다."
            }
        ],
        "examples": [
            {
                "ko": "변호사는 의뢰인의 정보에 대해 엄격한 비밀유지 의무가 있습니다.",
                "vi": "Luật sư có nghĩa vụ bảo mật thông tin nghiêm ngặt đối với khách hàng.",
                "situation": "formal"
            },
            {
                "ko": "비밀유지 계약서에 서명해 주세요.",
                "vi": "Xin ký vào hợp đồng bảo mật thông tin.",
                "situation": "onsite"
            },
            {
                "ko": "비밀유지 위반 시 법적 책임을 집니다.",
                "vi": "Vi phạm bảo mật thông tin sẽ chịu trách nhiệm pháp lý.",
                "situation": "formal"
            }
        ],
        "relatedTerms": ["직업윤리", "변호사", "계약"]
    },
    {
        "slug": "dao-duc-nghe-nghiep",
        "korean": "직업윤리",
        "vietnamese": "Đạo đức nghề nghiệp",
        "hanja": "職業倫理",
        "hanjaReading": "職(직분 직) + 業(업 업) + 倫(인륜 륜) + 理(다스릴 리)",
        "pronunciation": "다오 득 응에 응이엡",
        "meaningKo": "법조인이 직무를 수행하면서 지켜야 하는 윤리적 기준과 행동 규범을 의미합니다. 통역 시 주의할 점은 한국의 법조윤리는 대한변호사협회의 윤리규정으로 체계화되어 있고 징계 제도가 엄격하지만, 베트남의 법조윤리는 상대적으로 덜 체계적이며 실효성 있는 징계가 드뭅니다. 한국에서는 이해충돌, 비밀유지, 성실의무 등이 명확히 규정되고 엄격히 적용되지만, 베트남에서는 윤리 기준의 해석과 적용이 유연하고, 위반에 대한 제재가 약합니다. 외국 기업이 베트남 법조인과 일할 때는 한국 수준의 윤리 기준을 기대하기 어려울 수 있음을 인지해야 합니다.",
        "meaningVi": "Tiêu chuẩn đạo đức và quy tắc ứng xử mà người làm pháp luật phải tuân thủ trong khi thực hiện nhiệm vụ. Đạo đức nghề nghiệp pháp lý tại Việt Nam ít có hệ thống và kỷ luật hiệu quả hơn so với Hàn Quốc, nơi Hiệp hội Luật sư Hàn Quốc có quy định đạo đức hệ thống và chế độ kỷ luật nghiêm ngặt. Việc giải thích và áp dụng tiêu chuẩn đạo đức tại Việt Nam linh hoạt hơn, và chế tài đối với vi phạm yếu hơn.",
        "context": "법조윤리/전문가윤리",
        "culturalNote": "한국에서는 법조윤리가 법학 교육부터 강조되고, 변호사시험에도 포함되며, 실무에서 엄격히 적용됩니다. 대한변호사협회는 윤리 위반에 대해 경고, 정직, 제명 등의 징계를 내릴 수 있습니다. 반면 베트남에서는 법조윤리가 추상적인 수준에 머무르는 경우가 많고, 실제 징계 사례가 드뭅니다. 이해충돌 방지, 투명한 비용 산정, 의뢰인 이익 우선 등의 원칙이 베트남에서는 덜 엄격하게 적용됩니다. 특히 정부 기관이나 유력 인사와의 관계에서 독립성을 유지하는 것이 베트남 법조계에서는 어려울 수 있습니다.",
        "commonMistakes": [
            {
                "mistake": "한국의 엄격한 윤리 기준을 베트남에 동일하게 적용",
                "correction": "베트남의 유연한 윤리 기준과 약한 징계를 설명",
                "explanation": "베트남의 법조윤리는 한국만큼 엄격하게 적용되지 않으며, 문화적 차이를 이해해야 합니다."
            },
            {
                "mistake": "'Đạo đức luật sư'로 번역",
                "correction": "'Đạo đức nghề nghiệp'이 법조인 전체를 포괄",
                "explanation": "'Nghề nghiệp'이 변호사뿐 아니라 판사, 검사 등 모든 법조인을 포함합니다."
            },
            {
                "mistake": "윤리 위반의 법적 결과를 과대평가",
                "correction": "베트남에서 윤리 위반 징계가 드물다는 현실 안내",
                "explanation": "베트남에서는 윤리 위반에 대한 실질적 제재가 약하므로 현실적 기대치를 설정해야 합니다."
            }
        ],
        "examples": [
            {
                "ko": "변호사는 직업윤리를 철저히 준수해야 합니다.",
                "vi": "Luật sư phải tuân thủ đạo đức nghề nghiệp một cách triệt để.",
                "situation": "formal"
            },
            {
                "ko": "이해충돌은 직업윤리에 위반됩니다.",
                "vi": "Xung đột lợi ích vi phạm đạo đức nghề nghiệp.",
                "situation": "formal"
            },
            {
                "ko": "직업윤리 교육을 받아야 합니다.",
                "vi": "Phải được đào tạo về đạo đức nghề nghiệp.",
                "situation": "onsite"
            }
        ],
        "relatedTerms": ["비밀유지", "변호사", "이해충돌"]
    }
]

# 중복 제거 필터링
unique_new_terms = [term for term in new_terms if term['slug'] not in existing_slugs]

# 데이터 추가
data.extend(unique_new_terms)

# 파일 저장
with open(file_path, 'w', encoding='utf-8') as f:
    json.dump(data, f, ensure_ascii=False, indent=2)

print(f"✅ Successfully added {len(unique_new_terms)} terms to legal.json")
print(f"📊 Total terms: {len(data)}")
print(f"🔍 Duplicates filtered: {len(new_terms) - len(unique_new_terms)}")
print("\n📝 Added terms:")
for term in unique_new_terms:
    print(f"  - {term['slug']}: {term['korean']} ({term['vietnamese']})")
