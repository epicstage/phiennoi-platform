#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Medical Terms Batch Addition Script - Surgery/Anesthesia/ICU
Adds 10 new medical terms to medical.json with Tier S quality
"""

import json
import os

file_path = os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', 'data', 'terms', 'medical.json')

new_terms = [
    {
        "slug": "gay-me-toan-than",
        "korean": "전신마취",
        "vietnamese": "Gây mê toàn thân",
        "hanja": "全身麻醉",
        "hanjaReading": "全(온전할 전) 身(몸 신) 麻(마비할 마) 醉(취할 취)",
        "pronunciation": "전신마취",
        "meaningKo": "환자의 의식을 완전히 소실시켜 통증을 느끼지 못하게 하는 마취 방법입니다. 통역 시 주의할 점은 베트남에서는 'gây mê'와 'gây tê'를 명확히 구분하므로, 전신마취는 반드시 'gây mê toàn thân'으로 표현해야 합니다. 환자에게 설명할 때는 '의식이 없어지는 마취'라는 점을 강조하여 국소마취와 혼동하지 않도록 해야 합니다. 마취 전 금식 시간, 마취 후 회복 시간 등 구체적인 정보를 전달할 때는 숫자와 단위를 정확히 통역하는 것이 중요합니다.",
        "meaningVi": "Là phương pháp gây mê làm mất hoàn toàn ý thức của bệnh nhân để không cảm nhận được đau. Trong quá trình gây mê toàn thân, bệnh nhân sẽ không có ý thức, không cảm giác và không di chuyển được. Thường được sử dụng cho các ca phẫu thuật lớn hoặc phẫu thuật kéo dài.",
        "context": "수술 전 마취과 의사 상담, 마취 동의서 작성 시, 수술 전 설명",
        "culturalNote": "한국에서는 전신마취 전 최소 8시간 금식이 일반적이나, 베트남 일부 병원에서는 6시간 금식도 허용됩니다. 한국 환자들은 마취에 대한 두려움이 크지만, 베트남 환자들은 상대적으로 마취보다 수술 자체를 더 걱정하는 경향이 있습니다. 마취 후 회복실 운영 방식도 양국 간 차이가 있어, 보호자 면회 규정 등을 명확히 설명해야 합니다.",
        "commonMistakes": [
            {
                "mistake": "마취를 모두 'gây tê'로 통역",
                "correction": "전신마취는 'gây mê toàn thân', 국소마취는 'gây tê'",
                "explanation": "베트남어에서 gây mê는 의식 소실, gây tê는 감각 소실을 의미하므로 구분 필수"
            },
            {
                "mistake": "'마취가 깨다'를 'tỉnh dậy từ gây tê'로 표현",
                "correction": "'tỉnh lại sau gây mê' 또는 'hồi tỉnh'",
                "explanation": "전신마취 후 의식 회복은 'tỉnh lại' 또는 'hồi tỉnh' 사용"
            },
            {
                "mistake": "금식 시간을 'không ăn uống'으로만 설명",
                "correction": "'nhịn ăn nhịn uống ít nhất 8 tiếng'",
                "explanation": "구체적인 시간과 함께 '최소한'이라는 의미를 명확히 전달"
            }
        ],
        "examples": [
            {
                "ko": "내일 오전 수술을 위해 오늘 밤 12시부터 금식하셔야 합니다",
                "vi": "Để phẫu thuật vào sáng mai, anh/chị cần nhịn ăn uống từ 12 giờ đêm nay",
                "situation": "formal"
            },
            {
                "ko": "전신마취 후 회복실에서 약 1-2시간 관찰합니다",
                "vi": "Sau gây mê toàn thân, sẽ theo dõi tại phòng hồi sức khoảng 1-2 tiếng",
                "situation": "formal"
            },
            {
                "ko": "마취과 선생님이 수술 전에 환자분 상태를 확인하러 오실 겁니다",
                "vi": "Bác sĩ gây mê sẽ đến kiểm tra tình trạng của anh/chị trước phẫu thuật",
                "situation": "onsite"
            }
        ],
        "relatedTerms": ["국소마취", "척추마취", "마취과", "회복실"]
    },
    {
        "slug": "gay-te-tai-cho",
        "korean": "국소마취",
        "vietnamese": "Gây tê tại chỗ",
        "hanja": "局所麻醉",
        "hanjaReading": "局(국한될 국) 所(바 소) 麻(마비할 마) 醉(취할 취)",
        "pronunciation": "국소마취",
        "meaningKo": "신체의 특정 부위만 감각을 차단하여 통증을 느끼지 못하게 하는 마취 방법으로, 환자의 의식은 유지됩니다. 통역 시 핵심은 'gây tê'가 감각 소실만을 의미하며 의식은 유지된다는 점을 명확히 해야 합니다. 환자들이 '의식이 있는 상태에서 수술받는 것'에 대한 불안을 표현할 때, 통증은 전혀 느끼지 못하며 필요시 진정제를 투여할 수 있다는 점을 설명해야 합니다. 시술 부위, 마취 지속 시간 등의 정보를 정확히 전달하는 것이 중요합니다.",
        "meaningVi": "Là phương pháp gây tê chỉ làm mất cảm giác tại một vùng cụ thể trên cơ thể, bệnh nhân vẫn tỉnh táo và có ý thức. Thường dùng cho các thủ thuật nhỏ hoặc phẫu thuật tại chỗ như khâu vết thương, nhổ răng, mổ u nhỏ.",
        "context": "소수술, 치과 시술, 피부 시술, 외래 수술",
        "culturalNote": "한국에서는 간단한 시술에도 국소마취를 선호하는 반면, 베트남에서는 환자가 통증에 대한 두려움이 커서 전신마취를 요청하는 경우가 많습니다. 국소마취 시 '아프지 않다'는 보장을 원하는 환자들에게, 마취 주사 시 순간적인 통증은 있을 수 있으나 이후에는 통증이 없다는 점을 명확히 설명해야 합니다.",
        "commonMistakes": [
            {
                "mistake": "'국소마취'를 'gây mê cục bộ'로 표현",
                "correction": "'gây tê tại chỗ' 또는 'gây tê cục bộ'",
                "explanation": "gây mê는 의식 소실을 의미하므로 국소마취에는 부적절"
            },
            {
                "mistake": "마취 효과 지속 시간을 'có hiệu lực'으로만 표현",
                "correction": "'thuốc tê có tác dụng trong khoảng X giờ'",
                "explanation": "구체적인 지속 시간을 명시해야 환자가 이해 가능"
            },
            {
                "mistake": "'마취가 풀리다'를 'thuốc tê hết'으로만 표현",
                "correction": "'thuốc tê hết tác dụng' 또는 'hết tê'",
                "explanation": "마취 효과가 소멸되는 과정을 명확히 표현"
            }
        ],
        "examples": [
            {
                "ko": "국소마취 주사를 놓을 때 따끔한 느낌이 있을 수 있습니다",
                "vi": "Khi tiêm thuốc tê có thể có cảm giác hơi đau nhói",
                "situation": "formal"
            },
            {
                "ko": "마취 효과는 약 2-3시간 지속되며, 그 동안은 운전을 피하셔야 합니다",
                "vi": "Thuốc tê có tác dụng khoảng 2-3 tiếng, trong thời gian đó anh/chị không nên lái xe",
                "situation": "formal"
            },
            {
                "ko": "시술 중에 의식은 있지만 통증은 전혀 느끼지 못하실 겁니다",
                "vi": "Trong khi thủ thuật anh/chị vẫn tỉnh táo nhưng hoàn toàn không cảm thấy đau",
                "situation": "onsite"
            }
        ],
        "relatedTerms": ["전신마취", "척추마취", "진정마취", "표면마취"]
    },
    {
        "slug": "gay-te-tuy-song",
        "korean": "척추마취",
        "vietnamese": "Gây tê tủy sống",
        "hanja": "脊椎麻醉",
        "hanjaReading": "脊(등뼈 척) 椎(등골뼈 추) 麻(마비할 마) 醉(취할 취)",
        "pronunciation": "척추마취",
        "meaningKo": "척추 내 지주막하강에 마취제를 주입하여 하반신의 감각과 운동을 차단하는 마취 방법입니다. 통역 시 중요한 점은 환자가 '척추에 주사를 맞는다'는 것에 대한 두려움이 크므로, 시술 과정과 안전성을 차근차근 설명해야 합니다. 베트남어로는 'gây tê tủy sống' 또는 'gây tê vùng cột sống'으로 표현하며, 경막외마취(gây tê ngoài màng cứng)와 구분해야 합니다. 마취 후 자세 제한, 두통 가능성 등 부작용에 대한 설명도 정확히 전달해야 합니다.",
        "meaningVi": "Là phương pháp tiêm thuốc tê vào khoang dưới nhện của cột sống để gây tê toàn bộ phần dưới cơ thể. Bệnh nhân vẫn tỉnh táo nhưng không cảm nhận và di chuyển được phần dưới thắt lưng. Thường dùng cho phẫu thuật vùng bụng dưới, chân hoặc mổ đẻ.",
        "context": "제왕절개, 하지 수술, 비뇨기과 수술, 항문 수술",
        "culturalNote": "한국에서는 제왕절개 시 척추마취를 우선적으로 고려하지만, 베트남에서는 병원과 의사의 선호도에 따라 전신마취를 선택하는 경우도 많습니다. 척추마취 후 두통 예방을 위해 한국에서는 수술 후 6-8시간 누워있기를 권장하나, 베트남에서는 병원마다 지침이 다를 수 있습니다. 마취 주사 시 '등을 구부려 새우처럼 웅크리는 자세'에 대한 설명이 필요합니다.",
        "commonMistakes": [
            {
                "mistake": "척추마취와 경막외마취를 모두 'gây tê cột sống'으로 통역",
                "correction": "척추마취는 'gây tê tủy sống', 경막외마취는 'gây tê ngoài màng cứng'",
                "explanation": "두 마취 방법은 주입 위치와 효과가 다르므로 명확히 구분 필요"
            },
            {
                "mistake": "'하반신 마비'를 'liệt nửa dưới cơ thể'로 표현",
                "correction": "'tê nửa dưới cơ thể' 또는 'mất cảm giác phần dưới thắt lưng'",
                "explanation": "liệt는 영구적 마비를 연상시키므로 일시적 감각 차단은 tê 사용"
            },
            {
                "mistake": "마취 후 자세를 'nằm ngửa'로만 설명",
                "correction": "'nằm ngửa hoặc nằm nghiêng, không được ngồi dậy'",
                "explanation": "두통 예방을 위한 구체적인 자세 지침 전달"
            }
        ],
        "examples": [
            {
                "ko": "척추마취를 위해 등을 둥글게 구부리고 새우처럼 웅크려주세요",
                "vi": "Để gây tê tủy sống, anh/chị cần cong lưng tròn và co người lại như con tôm",
                "situation": "onsite"
            },
            {
                "ko": "마취 후 약 6시간 동안은 침대에 누워계셔야 두통을 예방할 수 있습니다",
                "vi": "Sau khi gây tê, anh/chị cần nằm trên giường khoảng 6 tiếng để phòng ngừa đau đầu",
                "situation": "formal"
            },
            {
                "ko": "다리에 힘이 돌아올 때까지 보통 3-4시간 정도 걸립니다",
                "vi": "Thường mất khoảng 3-4 tiếng để chân có thể cử động trở lại",
                "situation": "formal"
            }
        ],
        "relatedTerms": ["경막외마취", "전신마취", "제왕절개", "하지수술"]
    },
    {
        "slug": "giay-dong-y-phau-thuat",
        "korean": "수술동의서",
        "vietnamese": "Giấy đồng ý phẫu thuật",
        "hanja": "手術同意書",
        "hanjaReading": "手(손 수) 術(재주 술) 同(한가지 동) 意(뜻 의) 書(글 서)",
        "pronunciation": "수술동의서",
        "meaningKo": "환자나 보호자가 수술의 목적, 방법, 위험성, 합병증 등을 충분히 이해하고 수술 시행에 동의한다는 법적 문서입니다. 통역 시 주의할 점은 단순히 서명만 받는 절차가 아니라, 환자가 수술 내용을 완전히 이해했는지 확인하는 과정이라는 점을 강조해야 합니다. '동의서'를 'giấy đồng ý' 또는 'bản cam kết'로 표현하며, 합병증(biến chứng), 위험성(rủi ro) 등의 용어를 정확히 전달해야 합니다. 환자가 질문할 권리와 동의를 철회할 수 있는 권리도 함께 설명해야 합니다.",
        "meaningVi": "Là văn bản pháp lý xác nhận rằng bệnh nhân hoặc người thân đã hiểu rõ về mục đích, phương pháp, rủi ro và biến chứng của ca phẫu thuật và đồng ý tiến hành. Đây là tài liệu bắt buộc trước mọi ca phẫu thuật để bảo vệ quyền lợi của cả bệnh nhân và bác sĩ.",
        "context": "수술 전 설명, 입원 절차, 응급 수술 상황, 법적 요구사항",
        "culturalNote": "한국에서는 수술동의서 작성 시 의사가 직접 설명하고 환자/보호자의 서명을 받는 것이 엄격히 준수되지만, 베트남 일부 병원에서는 간호사가 설명하거나 형식적으로 진행되는 경우가 있습니다. 한국은 환자 본인의 자기결정권을 중시하나, 베트남에서는 가족 특히 가장의 의견이 더 중요시되는 경향이 있습니다. 미성년자나 의식불명 환자의 경우 법적 대리인 범위도 양국 간 차이가 있을 수 있습니다.",
        "commonMistakes": [
            {
                "mistake": "'동의서'를 'giấy cam kết'으로만 표현",
                "correction": "'giấy đồng ý phẫu thuật' 또는 'bản đồng ý phẫu thuật'",
                "explanation": "cam kết는 약속/서약의 의미가 강해 의료 동의서에는 đồng ý가 적절"
            },
            {
                "mistake": "'합병증'을 'tai biến'으로 표현",
                "correction": "'biến chứng' 사용",
                "explanation": "tai biến은 심각한 사고/재난을 의미, biến chứng이 의학적으로 정확"
            },
            {
                "mistake": "'서명하다'를 'viết tên'으로 표현",
                "correction": "'ký tên' 또는 'ký vào giấy đồng ý'",
                "explanation": "ký는 공식적인 서명, viết는 단순히 쓰는 행위"
            }
        ],
        "examples": [
            {
                "ko": "수술 전에 의사 선생님께서 수술 방법과 위험성에 대해 설명드릴 겁니다",
                "vi": "Trước phẫu thuật, bác sĩ sẽ giải thích về phương pháp phẫu thuật và các rủi ro",
                "situation": "formal"
            },
            {
                "ko": "동의서에 서명하시기 전에 궁금한 점이 있으시면 언제든 질문하세요",
                "vi": "Trước khi ký vào giấy đồng ý, nếu có thắc mắc gì anh/chị cứ hỏi thoải mái",
                "situation": "formal"
            },
            {
                "ko": "환자분이 의식이 없으셔서 보호자분께서 대신 동의서를 작성하셔야 합니다",
                "vi": "Vì bệnh nhân bất tỉnh nên người thân cần ký giấy đồng ý thay",
                "situation": "onsite"
            }
        ],
        "relatedTerms": ["수술", "합병증", "법적동의", "환자권리"]
    },
    {
        "slug": "bien-chung",
        "korean": "합병증",
        "vietnamese": "Biến chứng",
        "hanja": "合倂症",
        "hanjaReading": "合(합할 합) 倂(아울러 병) 症(증세 증)",
        "pronunciation": "합병증",
        "meaningKo": "질병이나 수술, 시술 후에 발생하는 예상치 못한 부작용이나 새로운 질환을 의미합니다. 통역 시 핵심은 '합병증'이 의료진의 실수가 아니라 의학적으로 발생 가능한 상황임을 환자에게 이해시키는 것입니다. 베트남어로는 'biến chứng'이 정확하며, 'tai biến'(사고), 'tác dụng phụ'(부작용)와는 구분해야 합니다. 합병증의 종류, 발생 확률, 대처 방법을 설명할 때는 객관적이고 정확한 수치와 표현을 사용하여 환자의 불안을 최소화하면서도 정보를 충분히 전달해야 합니다.",
        "meaningVi": "Là những tình trạng bệnh lý hoặc triệu chứng không mong muốn phát sinh trong hoặc sau quá trình điều trị, phẫu thuật hoặc do bệnh lý chính gây ra. Biến chứng có thể nhẹ hoặc nặng, tạm thời hoặc vĩnh viễn, và cần được theo dõi và xử lý kịp thời.",
        "context": "수술 설명, 치료 계획, 환자 모니터링, 의료 분쟁",
        "culturalNote": "한국 의료진은 합병증 발생 가능성을 사전에 상세히 설명하는 경향이 있으나, 베트남에서는 환자를 안심시키기 위해 긍정적인 면만 강조하는 경우가 있습니다. 한국 환자들은 합병증에 대한 자세한 설명을 듣고 싶어하지만, 베트남 환자들은 너무 상세한 설명이 오히려 불안을 증가시킬 수 있습니다. 합병증 발생 시 책임 소재에 대한 인식도 양국 간 차이가 있어, 의료진의 과실 여부를 명확히 구분하여 설명해야 합니다.",
        "commonMistakes": [
            {
                "mistake": "'합병증'을 'tai biến'으로 표현",
                "correction": "'biến chứng' 사용",
                "explanation": "tai biến은 심각한 의료사고를 의미하여 합병증보다 훨씬 부정적"
            },
            {
                "mistake": "'부작용'과 '합병증'을 모두 'biến chứng'으로 표현",
                "correction": "부작용은 'tác dụng phụ', 합병증은 'biến chứng'",
                "explanation": "부작용은 예상 가능한 반응, 합병증은 새로운 질병 발생"
            },
            {
                "mistake": "합병증 발생률을 '드물다'로만 표현",
                "correction": "구체적 확률 제시 'tỷ lệ khoảng X%'",
                "explanation": "모호한 표현은 환자의 불안을 증가시킬 수 있음"
            }
        ],
        "examples": [
            {
                "ko": "이 수술의 가장 흔한 합병증은 출혈과 감염으로, 발생률은 약 2-3% 정도입니다",
                "vi": "Biến chứng thường gặp nhất của ca phẫu thuật này là chảy máu và nhiễm trùng, tỷ lệ khoảng 2-3%",
                "situation": "formal"
            },
            {
                "ko": "합병증이 발생하면 즉시 추가 치료를 시작할 것이니 너무 걱정하지 마세요",
                "vi": "Nếu có biến chứng xảy ra, chúng tôi sẽ bắt đầu điều trị bổ sung ngay lập tức, anh/chị đừng lo lắng quá",
                "situation": "formal"
            },
            {
                "ko": "당뇨병 환자분들은 수술 후 상처 회복이 늦어지는 합병증이 생길 수 있습니다",
                "vi": "Bệnh nhân tiểu đường có thể gặp biến chứng vết thương lâu lành sau phẫu thuật",
                "situation": "onsite"
            }
        ],
        "relatedTerms": ["부작용", "후유증", "감염", "출혈"]
    },
    {
        "slug": "quan-ly-dau-sau-phau-thuat",
        "korean": "수술후통증관리",
        "vietnamese": "Quản lý đau sau phẫu thuật",
        "hanja": "手術後痛症管理",
        "hanjaReading": "手(손 수) 術(재주 술) 後(뒤 후) 痛(아플 통) 症(증세 증) 管(대롱 관) 理(다스릴 리)",
        "pronunciation": "수술후통증관리",
        "meaningKo": "수술 후 환자가 겪는 통증을 체계적으로 평가하고 적절한 진통제와 비약물적 방법을 통해 조절하는 의료 행위입니다. 통역 시 중요한 점은 환자가 통증을 참지 말고 적극적으로 표현해야 한다는 것을 강조하는 것입니다. 한국 의료진은 통증 점수(0-10점)로 객관화하려 하지만, 베트남 환자들은 주관적 표현('hơi đau', 'đau nhiều')을 선호할 수 있습니다. 진통제의 종류(giảm đau thông thường, giảm đau mạnh), 투여 경로(uống, tiêm, truyền), 부작용(buồn nôn, chóng mặt) 등을 명확히 설명해야 합니다.",
        "meaningVi": "Là quá trình đánh giá và kiểm soát cơn đau mà bệnh nhân trải qua sau phẫu thuật thông qua thuốc giảm đau và các phương pháp không dùng thuốc. Quản lý đau tốt giúp bệnh nhân phục hồi nhanh hơn, giảm nguy cơ biến chứng và cải thiện chất lượng cuộc sống sau phẫu thuật.",
        "context": "회복실, 병동 간호, 퇴원 교육, 통증 평가",
        "culturalNote": "한국에서는 수술 후 통증 관리가 체계적으로 이루어지며 환자가 통증을 호소하면 즉시 대응하지만, 베트남에서는 통증을 참는 것을 미덕으로 여기는 문화가 있어 환자가 통증을 충분히 표현하지 않을 수 있습니다. 한국은 PCA(자가조절진통펌프) 사용이 보편화되어 있으나, 베트남에서는 병원에 따라 사용 여부가 다릅니다. 마약성 진통제에 대한 우려도 양국 간 차이가 있어, 중독 위험성과 적절한 사용에 대한 설명이 필요합니다.",
        "commonMistakes": [
            {
                "mistake": "'통증 점수'를 'điểm đau'로만 표현",
                "correction": "'thang điểm đau từ 0 đến 10' 또는 'mức độ đau'",
                "explanation": "0-10 척도 시스템을 명확히 설명해야 환자가 이해 가능"
            },
            {
                "mistake": "'진통펌프'를 'máy bơm thuốc'으로만 표현",
                "correction": "'máy bơm thuốc giảm đau tự điều khiển' 또는 'PCA'",
                "explanation": "자가조절 기능을 명시하여 환자의 능동적 참여 강조"
            },
            {
                "mistake": "'참지 마세요'를 'đừng chịu đựng'으로만 표현",
                "correction": "'anh/chị cần nói với y tá khi đau, đừng cố chịu'",
                "explanation": "행동 지침을 구체적으로 제시하여 환자가 실행 가능하게"
            }
        ],
        "examples": [
            {
                "ko": "통증이 10점 만점에 몇 점 정도인지 말씀해주세요. 0점은 전혀 안 아프고 10점은 참을 수 없을 정도입니다",
                "vi": "Anh/chị cho biết mức độ đau trên thang điểm 10. Số 0 là không đau, số 10 là đau không chịu nổi",
                "situation": "formal"
            },
            {
                "ko": "이 버튼을 누르면 진통제가 자동으로 투여됩니다. 통증이 있을 때마다 누르세요",
                "vi": "Khi bấm nút này, thuốc giảm đau sẽ được bơm tự động. Anh/chị bấm mỗi khi cảm thấy đau",
                "situation": "onsite"
            },
            {
                "ko": "진통제를 먹으면 약간 어지러울 수 있지만 곧 괜찮아질 겁니다",
                "vi": "Sau khi uống thuốc giảm đau có thể hơi chóng mặt nhưng sẽ nhanh hết",
                "situation": "formal"
            }
        ],
        "relatedTerms": ["진통제", "통증평가", "자가조절진통펌프", "마약성진통제"]
    },
    {
        "slug": "phong-cham-soc-tich-cuc",
        "korean": "중환자실",
        "vietnamese": "Phòng chăm sóc tích cực",
        "hanja": "重患者室",
        "hanjaReading": "重(무거울 중) 患(근심 환) 者(놈 자) 室(집 실)",
        "pronunciation": "중환자실",
        "meaningKo": "생명이 위독하거나 집중적인 치료와 모니터링이 필요한 환자를 위한 특수 병동입니다. 통역 시 핵심은 중환자실 입실이 반드시 부정적인 신호가 아니라 최선의 치료를 위한 조치임을 설명하는 것입니다. 베트남어로는 'Phòng chăm sóc tích cực' 또는 'ICU(Intensive Care Unit)'로 표현하며, 일반 병동과의 차이점을 명확히 해야 합니다. 면회 제한(hạn chế thăm bệnh), 24시간 모니터링, 의료진 대 환자 비율 등 중환자실의 특성을 설명하여 가족들의 불안을 완화해야 합니다.",
        "meaningVi": "Là khu vực đặc biệt trong bệnh viện dành cho bệnh nhân có tình trạng nguy kịch hoặc cần theo dõi và điều trị tích cực liên tục. Phòng chăm sóc tích cực được trang bị đầy đủ thiết bị hiện đại và có đội ngũ y bác sĩ chuyên môn cao theo dõi 24/7.",
        "context": "수술 후 관리, 응급 상황, 중증 질환, 보호자 면회",
        "culturalNote": "한국 중환자실은 감염 관리를 위해 면회가 엄격히 제한되고 보호자가 상주할 수 없지만, 베트남에서는 병원에 따라 보호자 1명이 상주하는 것을 허용하기도 합니다. 한국은 환자 프라이버시 보호를 위해 커튼이나 칸막이로 구분하나, 베트남은 개방형 병상이 많습니다. 중환자실 비용도 양국 간 차이가 크며, 한국은 건강보험 적용이 되지만 베트남은 본인부담금이 높을 수 있습니다.",
        "commonMistakes": [
            {
                "mistake": "'중환자실'을 'phòng cấp cứu'로 표현",
                "correction": "'phòng chăm sóc tích cực' 또는 'ICU'",
                "explanation": "phòng cấp cứu는 응급실, 중환자실은 별도의 집중치료실"
            },
            {
                "mistake": "면회 시간을 '언제든지 가능'으로 잘못 전달",
                "correction": "정해진 면회 시간과 인원 제한 명시",
                "explanation": "중환자실은 감염 관리를 위해 면회가 제한됨"
            },
            {
                "mistake": "'위독하다'를 'sắp chết'로 표현",
                "correction": "'tình trạng nguy kịch' 또는 'bệnh nặng'",
                "explanation": "sắp chết는 너무 직접적이고 희망을 빼앗는 표현"
            }
        ],
        "examples": [
            {
                "ko": "수술 후 안전을 위해 하루 정도 중환자실에서 집중 관찰할 예정입니다",
                "vi": "Sau phẫu thuật, để đảm bảo an toàn, bệnh nhân sẽ được theo dõi tích cực tại ICU khoảng một ngày",
                "situation": "formal"
            },
            {
                "ko": "중환자실 면회는 하루 2회, 오전 11시와 오후 5시에 가족 한 분만 가능합니다",
                "vi": "Thăm bệnh tại ICU chỉ được 2 lần mỗi ngày, lúc 11 giờ sáng và 5 giờ chiều, chỉ một người thân",
                "situation": "formal"
            },
            {
                "ko": "중환자실에서는 24시간 전문 간호사가 환자를 지켜보고 있으니 안심하세요",
                "vi": "Tại ICU có y tá chuyên môn theo dõi bệnh nhân 24 giờ, gia đình yên tâm",
                "situation": "onsite"
            }
        ],
        "relatedTerms": ["집중치료", "인공호흡기", "생체징후모니터링", "응급실"]
    },
    {
        "slug": "may-tho",
        "korean": "인공호흡기",
        "vietnamese": "Máy thở",
        "hanja": "人工呼吸器",
        "hanjaReading": "人(사람 인) 工(장인 공) 呼(부를 호) 吸(마실 흡) 器(그릇 기)",
        "pronunciation": "인공호흡기",
        "meaningKo": "스스로 호흡하기 어려운 환자에게 공기나 산소를 폐로 전달하여 호흡을 돕는 의료 장비입니다. 통역 시 가장 중요한 점은 인공호흡기 사용이 환자의 회복을 돕는 일시적 조치일 수 있으며, 반드시 영구적이거나 최악의 상황을 의미하는 것이 아님을 설명하는 것입니다. 베트남어로는 'máy thở' 또는 'máy thở nhân tạo'로 표현하며, 삽관(đặt nội khí quản), 진정(an thần), 이탈 과정(tập cai máy thở) 등의 용어를 정확히 전달해야 합니다. 가족들의 불안이 큰 상황이므로 차분하고 명확한 통역이 필수입니다.",
        "meaningVi": "Là thiết bị y tế hỗ trợ hoặc thay thế chức năng thở cho bệnh nhân không thể tự thở được hoặc thở không đủ. Máy thở cung cấp không khí hoặc oxy vào phổi thông qua ống thở đặt vào khí quản hoặc qua mặt nạ. Thường được sử dụng trong ICU, phòng mổ hoặc cấp cứu.",
        "context": "중환자실, 수술 중, 응급 상황, 호흡기 질환",
        "culturalNote": "한국에서는 인공호흡기 적용 여부를 환자와 가족이 사전에 결정할 수 있는 연명치료중단제도가 있지만, 베트남에서는 이러한 제도가 명확하지 않을 수 있습니다. 한국 가족들은 인공호흡기 치료 기간과 이탈 가능성에 대해 구체적인 정보를 원하지만, 베트Nam 가족들은 의료진의 결정을 더 신뢰하는 경향이 있습니다. 인공호흡기 사용 중 환자와 소통이 불가능하다는 점에 대한 설명도 필요합니다.",
        "commonMistakes": [
            {
                "mistake": "'인공호흡기'를 'ống thở'로만 표현",
                "correction": "'máy thở' 또는 'máy thở nhân tạo'",
                "explanation": "ống thở는 삽관튜브, máy thở는 인공호흡기 장비 전체"
            },
            {
                "mistake": "삽관을 'đặt ống'으로만 표현",
                "correction": "'đặt nội khí quản' 또는 'đặt ống thở vào khí quản'",
                "explanation": "의학적으로 정확한 용어 사용 필요"
            },
            {
                "mistake": "'인공호흡기를 떼다'를 'tháo máy thở'로만 표현",
                "correction": "'cai máy thở' 또는 'rút ống thở sau khi tập thở'",
                "explanation": "이탈 과정이 단순히 제거가 아닌 단계적 훈련임을 표현"
            }
        ],
        "examples": [
            {
                "ko": "수술 중에는 전신마취를 하기 때문에 일시적으로 인공호흡기를 사용합니다",
                "vi": "Trong khi phẫu thuật, do gây mê toàn thân nên sẽ sử dụng máy thở tạm thời",
                "situation": "formal"
            },
            {
                "ko": "환자분이 스스로 호흡할 수 있을 때까지 인공호흡기가 호흡을 도와줄 겁니다",
                "vi": "Máy thở sẽ hỗ trợ hô hấp cho đến khi bệnh nhân có thể tự thở được",
                "situation": "formal"
            },
            {
                "ko": "인공호흡기를 떼기 위해 매일 환자분의 호흡 능력을 테스트하고 있습니다",
                "vi": "Chúng tôi đang kiểm tra khả năng thở của bệnh nhân mỗi ngày để có thể cai máy thở",
                "situation": "onsite"
            }
        ],
        "relatedTerms": ["삽관", "진정", "중환자실", "산소포화도"]
    },
    {
        "slug": "phong-ngua-loet-ti-de",
        "korean": "욕창예방",
        "vietnamese": "Phòng ngừa loét tì đè",
        "hanja": "褥瘡豫防",
        "hanjaReading": "褥(자리 욕) 瘡(헐 창) 豫(미리 예) 防(막을 방)",
        "pronunciation": "욕창예방",
        "meaningKo": "장시간 같은 자세로 누워있거나 앉아있을 때 압력을 받는 부위의 피부와 조직이 손상되는 것을 예방하는 간호 활동입니다. 통역 시 중요한 점은 욕창이 단순한 피부 문제가 아니라 심부 조직까지 손상될 수 있는 심각한 합병증임을 설명하는 것입니다. 베트Nam어로는 'phòng ngừa loét tì đè' 또는 'phòng loét do nằm lâu'로 표현하며, 체위 변경(thay đổi tư thế), 압력 분산 매트리스(nệm chống loét), 피부 청결 유지 등의 예방법을 구체적으로 설명해야 합니다.",
        "meaningVi": "Là các biện pháp chăm sóc nhằm ngăn ngừa tổn thương da và mô dưới da do bị ép lâu ở một vị trí. Loét tì đè thường xảy ra ở những vùng xương nhô như cùng cụt, gót chân, khuỷu tay khi bệnh nhân nằm một chỗ lâu. Phòng ngừa bao gồm thay đổi tư thế thường xuyên, giữ da sạch và khô, sử dụng nệm chống loét.",
        "context": "장기 입원, 중환자 간호, 노인 환자, 마비 환자",
        "culturalNote": "한국 병원에서는 욕창 예방을 위한 체계적인 프로토콜이 있으며 2시간마다 체위 변경을 기록하지만, 베트Nam에서는 병원과 간병인에 따라 관리 수준이 다를 수 있습니다. 한국은 욕창 발생 시 의료진의 책임으로 간주될 수 있으나, 베트Nam에서는 가족이나 간병인의 책임으로 여겨지는 경향이 있습니다. 욕창 예방용 특수 매트리스나 쿠션의 비용 부담도 양국 간 차이가 있습니다.",
        "commonMistakes": [
            {
                "mistake": "'욕창'을 'vết thương do nằm'으로만 표현",
                "correction": "'loét tì đè' 또는 'loét do ép lâu'",
                "explanation": "의학 용어로 정확히 표현해야 심각성 전달 가능"
            },
            {
                "mistake": "체위 변경을 'lật người'로 표현",
                "correction": "'thay đổi tư thế' 또는 'đổi tư thế nằm'",
                "explanation": "lật는 뒤집는다는 의미로 부적절, 전문적 표현 사용"
            },
            {
                "mistake": "'2시간마다'를 'hai tiếng một lần'으로만 표현",
                "correction": "'mỗi hai tiếng' 또는 'cứ hai tiếng một lần'",
                "explanation": "주기를 명확히 표현하여 오해 방지"
            }
        ],
        "examples": [
            {
                "ko": "욕창을 예방하기 위해 2시간마다 환자분의 자세를 바꿔드려야 합니다",
                "vi": "Để phòng ngừa loét tì đè, cần thay đổi tư thế cho bệnh nhân mỗi hai tiếng",
                "situation": "formal"
            },
            {
                "ko": "엉덩이와 발뒤꿈치 같이 뼈가 튀어나온 부위를 특히 조심해야 합니다",
                "vi": "Cần đặc biệt chú ý các vùng xương nhô như mông và gót chân",
                "situation": "onsite"
            },
            {
                "ko": "피부를 항상 깨끗하고 건조하게 유지하고, 주름진 시트는 즉시 펴주세요",
                "vi": "Luôn giữ da sạch và khô ráo, và ngay lập tức làm phẳng ga trải giường nếu bị nhăn",
                "situation": "formal"
            }
        ],
        "relatedTerms": ["체위변경", "압력궤양", "피부간호", "특수매트리스"]
    },
    {
        "slug": "truyen-mau",
        "korean": "수혈",
        "vietnamese": "Truyền máu",
        "hanja": "輸血",
        "hanjaReading": "輸(보낼 수) 血(피 혈)",
        "pronunciation": "수혈",
        "meaningKo": "혈액 손실이나 혈액 질환으로 인해 환자에게 혈액이나 혈액 성분을 주입하는 의료 행위입니다. 통역 시 핵심은 수혈의 필요성, 혈액형 확인 과정, 부작용 가능성을 명확히 설명하는 것입니다. 베트Nam어로는 'truyền máu'로 표현하며, 전혈 수혈(truyền máu toàn phần)과 성분 수혈(truyền chế phẩm máu)을 구분해야 합니다. 수혈 동의서, 교차시험(xét nghiệm phản ứng chéo), 수혈 반응(phản ứng truyền máu) 등의 용어를 정확히 전달하고, 종교적 이유로 수혈을 거부하는 경우의 대안도 논의해야 합니다.",
        "meaningVi": "Là quá trình truyền máu hoặc các thành phần máu từ người hiến tặng vào cơ thể bệnh nhân để bù đắp lượng máu mất hoặc điều trị các bệnh lý về máu. Trước khi truyền máu cần kiểm tra nhóm máu, xét nghiệm phản ứng chéo và theo dõi bệnh nhân trong suốt quá trình truyền để phát hiện phản ứng bất lợi.",
        "context": "수술 전후, 출혈 상황, 빈혈 치료, 혈액 질환",
        "culturalNote": "한국은 헌혈 문화가 발달하여 혈액 수급이 비교적 원활하지만, 베트Nam에서는 가족 간 헌혈이나 유상 헌혈이 아직 존재합니다. 한국은 수혈 전 교차시험을 철저히 하고 부작용 모니터링이 체계적이나, 베트Nam에서는 병원마다 프로토콜이 다를 수 있습니다. 수혈에 대한 종교적 거부(예: 여호와의 증인)에 대한 대응도 양국 간 차이가 있으며, 한국은 대체 치료법을 적극 모색하는 편입니다.",
        "commonMistakes": [
            {
                "mistake": "'수혈'을 'tiêm máu'로 표현",
                "correction": "'truyền máu' 사용",
                "explanation": "tiêm은 주사, truyền은 수액/수혈을 의미"
            },
            {
                "mistake": "'혈액형'을 'loại máu'로만 표현",
                "correction": "'nhóm máu' 사용",
                "explanation": "nhóm máu가 의학적으로 정확한 용어"
            },
            {
                "mistake": "수혈 부작용을 '알레르기'로만 설명",
                "correction": "'phản ứng truyền máu' 또는 'tác dụng phụ của truyền máu'",
                "explanation": "수혈 반응은 알레르기 외에도 다양한 형태가 있음"
            }
        ],
        "examples": [
            {
                "ko": "수술 중 출혈이 예상되어 수혈이 필요할 수 있습니다. 혈액형 검사를 먼저 하겠습니다",
                "vi": "Có thể cần truyền máu do dự kiến chảy máu trong phẫu thuật. Chúng tôi sẽ xét nghiệm nhóm máu trước",
                "situation": "formal"
            },
            {
                "ko": "수혈 중에 열이 나거나 가려움증이 생기면 즉시 말씀해주세요",
                "vi": "Nếu trong khi truyền máu có sốt hoặc ngứa, anh/chị báo ngay cho y tá",
                "situation": "formal"
            },
            {
                "ko": "헤모글로빈 수치가 너무 낮아서 적혈구 수혈이 필요합니다",
                "vi": "Do chỉ số hemoglobin quá thấp nên cần truyền hồng cầu",
                "situation": "onsite"
            }
        ],
        "relatedTerms": ["혈액형", "교차시험", "수혈반응", "헌혈"]
    }
]

def load_existing_terms():
    """Load existing terms from medical.json"""
    try:
        with open(file_path, 'r', encoding='utf-8') as f:
            data = json.load(f)
            return data
    except FileNotFoundError:
        print(f"Error: {file_path} not found")
        return []
    except json.JSONDecodeError as e:
        print(f"Error decoding JSON: {e}")
        return []

def filter_duplicates(existing_data, new_terms):
    """Filter out duplicate terms based on slug"""
    existing_slugs = {term['slug'] for term in existing_data}
    filtered_terms = [term for term in new_terms if term['slug'] not in existing_slugs]

    duplicates = len(new_terms) - len(filtered_terms)
    if duplicates > 0:
        print(f"Filtered out {duplicates} duplicate term(s)")

    return filtered_terms

def save_terms(data):
    """Save terms back to medical.json"""
    try:
        with open(file_path, 'w', encoding='utf-8') as f:
            json.dump(data, f, ensure_ascii=False, indent=2)
        return True
    except Exception as e:
        print(f"Error saving file: {e}")
        return False

def main():
    print("=" * 60)
    print("Medical Terms Batch Addition - Surgery/Anesthesia/ICU")
    print("=" * 60)

    existing_data = load_existing_terms()
    if not existing_data:
        print("Failed to load existing data. Aborting.")
        return

    print(f"Loaded {len(existing_data)} existing terms")

    filtered_new_terms = filter_duplicates(existing_data, new_terms)

    if not filtered_new_terms:
        print("No new terms to add (all duplicates)")
        return

    print(f"Adding {len(filtered_new_terms)} new term(s)...")

    existing_data.extend(filtered_new_terms)

    if save_terms(existing_data):
        print(f"\nSuccess! Added {len(filtered_new_terms)} new term(s)")
        print(f"Total terms now: {len(existing_data)}")
        print("\nAdded terms:")
        for term in filtered_new_terms:
            print(f"  - {term['korean']} ({term['vietnamese']})")
    else:
        print("\nFailed to save terms")

if __name__ == "__main__":
    main()
