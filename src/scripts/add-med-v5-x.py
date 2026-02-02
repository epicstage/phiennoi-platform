#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
수술/마취/중환자 관련 의료 용어 10개 추가 스크립트
Theme: Surgery/Anesthesia/ICU
"""

import json
import os

# 파일 경로 설정
file_path = os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', 'data', 'terms', 'medical.json')

# 새로 추가할 용어들 (Tier S 기준 충족)
new_terms = [
    {
        "slug": "gay-me-toan-than",
        "korean": "전신마취",
        "vietnamese": "Gây mê toàn thân",
        "hanja": "全身麻醉",
        "hanjaReading": "全(온전할 전) + 身(몸 신) + 麻(마비할 마) + 醉(취할 취)",
        "pronunciation": "가이 메 또안 턴",
        "meaningKo": "환자의 의식을 완전히 소실시켜 수술 중 통증을 느끼지 못하게 하는 마취 방법입니다. 통역 시 주의할 점은 베트남어 'gây mê'는 '잠들게 하다'라는 뜻으로 환자가 쉽게 이해할 수 있지만, 'toàn thân'(전신)을 강조해야 국소마취와 구분됩니다. 수술 전 설명 시 환자가 '완전히 자는 것'과 '부분만 마비되는 것'의 차이를 정확히 이해하도록 통역해야 하며, 마취 전 금식 시간, 각성 후 회복 과정 등을 명확히 전달해야 합니다. 베트남 환자들은 전신마취에 대한 두려움이 있을 수 있으므로 안전성을 강조하는 것이 중요합니다.",
        "meaningVi": "Phương pháp gây mê làm mất hoàn toàn ý thức của bệnh nhân để không cảm thấy đau trong quá trình phẫu thuật. Thuốc mê được tiêm tĩnh mạch hoặc hít qua đường thở, bệnh nhân sẽ ngủ sâu và không nhận biết được bất cứ điều gì xảy ra trong suốt ca mổ. Sau khi phẫu thuật kết thúc, bác sĩ gây mê sẽ ngừng thuốc và bệnh nhân dần tỉnh lại trong phòng hồi sức.",
        "context": "수술 전 마취과 상담, 수술 동의서 설명, 회복실 안내 시 사용",
        "culturalNote": "한국에서는 전신마취가 일반적이고 안전하다고 인식되지만, 베트남에서는 일부 환자들이 '깨어나지 못할까봐' 두려워하는 경우가 있습니다. 한국 병원에서는 마취통증의학과 전문의가 독립적으로 마취를 담당하지만, 베트남 일부 지역 병원에서는 외과의가 직접 마취를 관리하기도 합니다. 통역 시 한국의 체계적인 마취 시스템과 안전 관리 절차를 설명하여 환자의 불안을 해소해야 합니다. 또한 마취 전 금식 시간(보통 8시간)을 정확히 전달하는 것이 중요합니다.",
        "commonMistakes": [
            {
                "mistake": "'잠자는 주사'라고만 설명",
                "correction": "'gây mê toàn thân' (전신마취)로 정확히 표현",
                "explanation": "단순히 '자는 것'으로 설명하면 국소마취나 진정과 혼동될 수 있으며, 환자가 마취의 깊이를 오해할 수 있습니다"
            },
            {
                "mistake": "'gây tê' (마비시키다)로 통역",
                "correction": "'gây mê' (의식을 잃게 하다)로 표현",
                "explanation": "'gây tê'는 국소마취를 의미하므로 전신마취와 완전히 다른 개념입니다"
            },
            {
                "mistake": "마취 위험성을 과소평가하여 통역",
                "correction": "의사의 설명을 정확히 전달하되, 안전 관리 시스템도 함께 설명",
                "explanation": "환자의 동의를 얻기 위해서는 위험성과 안전성을 모두 균형있게 전달해야 합니다"
            }
        ],
        "examples": [
            {
                "ko": "이번 수술은 전신마취로 진행되므로 수술 8시간 전부터 금식하셔야 합니다.",
                "vi": "Ca phẫu thuật này sẽ được thực hiện bằng gây mê toàn thân nên bạn phải nhịn ăn từ 8 giờ trước khi mổ.",
                "situation": "formal"
            },
            {
                "ko": "전신마취 후 회복실에서 약 1-2시간 계시다가 병실로 올라가십니다.",
                "vi": "Sau khi gây mê toàn thân, bạn sẽ ở phòng hồi sức khoảng 1-2 tiếng rồi mới lên phòng bệnh.",
                "situation": "onsite"
            },
            {
                "ko": "전신마취 중에는 완전히 잠들어 계시기 때문에 아무것도 느끼지 못하십니다.",
                "vi": "Trong quá trình gây mê toàn thân, bạn sẽ ngủ hoàn toàn nên không cảm thấy bất cứ điều gì.",
                "situation": "informal"
            }
        ],
        "relatedTerms": ["국소마취", "척추마취", "마취통증의학과", "회복실"]
    },
    {
        "slug": "gay-te-tai-cho",
        "korean": "국소마취",
        "vietnamese": "Gây tê tại chỗ",
        "hanja": "局所麻醉",
        "hanjaReading": "局(구역 국) + 所(바 소) + 麻(마비할 마) + 醉(취할 취)",
        "pronunciation": "가이 떼 때이 쪼",
        "meaningKo": "수술 부위만 감각을 차단하여 통증을 느끼지 못하게 하는 마취 방법으로, 환자는 의식이 있는 상태를 유지합니다. 통역 시 중요한 점은 'tại chỗ'(그 자리에)라는 표현으로 '부분적'이라는 개념을 명확히 전달해야 한다는 것입니다. 환자가 '깨어있지만 아프지 않다'는 점을 이해하도록 설명해야 하며, 시술 중 압박감이나 당김은 느낄 수 있다는 점도 미리 알려야 합니다. 베트남 환자들은 의식이 있는 상태에서 수술받는 것을 선호하는 경우가 많으므로, 국소마취의 장점을 잘 설명하는 것이 중요합니다.",
        "meaningVi": "Phương pháp gây tê chỉ làm tê một vùng cụ thể trên cơ thể, bệnh nhân vẫn tỉnh táo và có thể giao tiếp trong suốt quá trình phẫu thuật. Thuốc tê được tiêm trực tiếp vào vùng cần phẫu thuật, chỉ làm mất cảm giác đau ở khu vực đó mà không ảnh hưởng đến các bộ phận khác. Thường được sử dụng cho các ca phẫu thuật nhỏ như khâu vết thương, nhổ răng, hoặc phẫu thuật da.",
        "context": "피부 시술, 치과 치료, 소수술, 봉합 시 사용",
        "culturalNote": "한국에서는 작은 수술이나 시술에 국소마취를 선호하며, 환자가 의식이 있어 빠른 회복이 가능하다는 점을 강조합니다. 베트남에서도 국소마취는 일반적이지만, 일부 환자들은 시술 과정을 보거나 듣는 것에 불안을 느낄 수 있습니다. 한국 병원에서는 환자의 불안을 줄이기 위해 스크린을 설치하거나 진정제를 병용하는 경우가 많은데, 이를 미리 설명하면 환자의 협조를 얻기 쉽습니다. 또한 국소마취는 전신마취에 비해 금식이 필요 없다는 장점을 강조할 수 있습니다.",
        "commonMistakes": [
            {
                "mistake": "'gây mê một phần' (부분 마취)로 통역",
                "correction": "'gây tê tại chỗ' (국소 마취)로 정확히 표현",
                "explanation": "'gây mê'는 의식 소실을 의미하지만 국소마취는 의식이 유지되므로 'gây tê'(감각 차단)로 표현해야 합니다"
            },
            {
                "mistake": "척추마취와 혼동하여 설명",
                "correction": "국소마취는 피부 표면 주사, 척추마취는 척추강 내 주사로 구분",
                "explanation": "두 마취 방법은 적용 범위와 방법이 완전히 다르므로 명확히 구분해야 합니다"
            },
            {
                "mistake": "'아무 느낌도 없다'고 설명",
                "correction": "'통증은 없지만 압박감은 느낄 수 있다'고 정확히 전달",
                "explanation": "환자가 시술 중 압박감을 느끼면 마취가 안 된 것으로 오해할 수 있으므로 미리 설명이 필요합니다"
            }
        ],
        "examples": [
            {
                "ko": "이 정도 상처는 국소마취로 충분하니 금식하지 않으셔도 됩니다.",
                "vi": "Vết thương này chỉ cần gây tê tại chỗ nên bạn không cần nhịn ăn.",
                "situation": "formal"
            },
            {
                "ko": "국소마취 주사 놓을 때 조금 따끔할 수 있어요.",
                "vi": "Khi tiêm thuốc tê tại chỗ có thể hơi đau một chút.",
                "situation": "onsite"
            },
            {
                "ko": "국소마취라서 시술 중에 의사 선생님 말씀 들으실 수 있어요.",
                "vi": "Vì là gây tê tại chỗ nên trong quá trình làm thủ thuật bạn vẫn nghe được bác sĩ nói.",
                "situation": "informal"
            }
        ],
        "relatedTerms": ["전신마취", "표면마취", "침윤마취", "진통제"]
    },
    {
        "slug": "gay-te-tuy-song",
        "korean": "척추마취",
        "vietnamese": "Gây tê tủy sống",
        "hanja": "脊椎麻醉",
        "hanjaReading": "脊(등뼈 척) + 椎(등골뼈 추) + 麻(마비할 마) + 醉(취할 취)",
        "pronunciation": "가이 떼 뚜이 송",
        "meaningKo": "척추 신경을 차단하여 하반신의 감각과 운동을 일시적으로 마비시키는 마취 방법입니다. 통역 시 중요한 점은 베트nam어 'tủy sống'(척수)라는 해부학적 용어를 사용하여 정확히 전달하되, 환자가 이해하기 쉽게 '허리에 주사를 놓아 아래쪽을 마비시킨다'고 부연 설명해야 합니다. 환자가 '다리를 못 움직인다'는 것에 놀라지 않도록 미리 설명하고, 마취 후 일정 시간이 지나면 회복된다는 점을 강조해야 합니다. 척추마취 후 두통이나 요통이 발생할 수 있음을 알리고, 시술 중 자세 협조의 중요성을 정확히 통역해야 합니다.",
        "meaningVi": "Phương pháp gây tê bằng cách tiêm thuốc vào khoang tủy sống để làm tê và liệt tạm thời phần dưới cơ thể từ thắt lưng trở xuống. Bệnh nhân vẫn tỉnh táo nhưng không cảm thấy đau và không thể cử động chân trong suốt quá trình phẫu thuật. Thường được sử dụng cho các ca mổ vùng bụng dưới, xương chậu, hoặc chân. Sau khi thuốc hết tác dụng, cảm giác và khả năng vận động sẽ dần hồi phục.",
        "context": "제왕절개, 하복부 수술, 정형외과 하지 수술 시 사용",
        "culturalNote": "한국에서는 제왕절개 시 척추마취가 표준이며, 산모가 아기 출생을 직접 볼 수 있다는 장점을 강조합니다. 베트남에서도 척추마취는 일반적이지만, 일부 환자들은 '허리에 주사를 맞는 것'에 대한 두려움이나 '나중에 허리 통증이 생길까봐' 걱정하는 경우가 많습니다. 통역 시 척추마취 후 요통은 대부분 일시적이며, 적절한 시술로 합병증을 최소화할 수 있다는 점을 설명해야 합니다. 또한 시술 중 '새우 자세'(웅크린 자세)를 정확히 취하는 것이 중요하므로 자세 지시를 명확히 통역해야 합니다.",
        "commonMistakes": [
            {
                "mistake": "'허리 마취'로 단순화",
                "correction": "'gây tê tủy sống' (척추마취)로 의학 용어 사용",
                "explanation": "정확한 의학 용어를 사용해야 환자가 시술의 성격을 제대로 이해하고, 의료진과의 소통도 원활해집니다"
            },
            {
                "mistake": "경막외마취와 혼동",
                "correction": "척추마취는 'gây tê tủy sống', 경막외마취는 'gây tê ngoài màng cứng'로 구분",
                "explanation": "두 마취는 주사 위치와 작용 범위가 다르므로 정확히 구분해야 합니다"
            },
            {
                "mistake": "'영구적으로 다리를 못 쓴다'고 오해할 여지를 줌",
                "correction": "'일시적으로 마비되며 몇 시간 후 회복된다'고 명확히 설명",
                "explanation": "환자가 마비에 대한 공포를 느끼지 않도록 일시적이라는 점을 강조해야 합니다"
            }
        ],
        "examples": [
            {
                "ko": "제왕절개는 척추마취로 진행하므로 아기 나오는 것을 보실 수 있습니다.",
                "vi": "Ca mổ sinh mổ sẽ được thực hiện bằng gây tê tủy sống nên bạn có thể nhìn thấy em bé khi ra đời.",
                "situation": "formal"
            },
            {
                "ko": "척추마취 주사 맞을 때 새우처럼 몸을 둥글게 말아주세요.",
                "vi": "Khi tiêm gây tê tủy sống, bạn hãy cuộn tròn người như con tôm.",
                "situation": "onsite"
            },
            {
                "ko": "척추마취 후 6시간 정도는 누워 계셔야 두통을 예방할 수 있어요.",
                "vi": "Sau khi gây tê tủy sống, bạn nên nằm yên khoảng 6 tiếng để phòng ngừa đau đầu.",
                "situation": "informal"
            }
        ],
        "relatedTerms": ["경막외마취", "전신마취", "제왕절개", "마취후두통"]
    },
    {
        "slug": "giay-dong-y-phau-thuat",
        "korean": "수술동의서",
        "vietnamese": "Giấy đồng ý phẫu thuật",
        "hanja": "手術同意書",
        "hanjaReading": "手(손 수) + 術(재주 술) + 同(한가지 동) + 意(뜻 의) + 書(글 서)",
        "pronunciation": "지에이 동 이 퍼우 투엇",
        "meaningKo": "환자가 수술의 목적, 방법, 위험성, 합병증 등을 충분히 이해하고 자발적으로 수술을 받겠다는 의사를 표시하는 법적 문서입니다. 통역 시 가장 중요한 것은 단순히 서명을 받기 위한 형식이 아니라, 환자가 내용을 진정으로 이해했는지 확인하는 과정이라는 점을 전달하는 것입니다. '동의서'라는 단어를 'giấy đồng ý'로 정확히 통역하되, 환자가 질문할 권리가 있고 이해 안 되는 부분은 반드시 물어봐야 한다는 점을 강조해야 합니다. 특히 합병증 부분에서 환자가 겁을 먹지 않으면서도 위험성을 정확히 인지하도록 균형있게 통역하는 것이 중요합니다.",
        "meaningVi": "Văn bản pháp lý trong đó bệnh nhân xác nhận đã hiểu rõ mục đích, phương pháp, nguy cơ và biến chứng của ca phẫu thuật, và tự nguyện đồng ý thực hiện phẫu thuật. Đây là tài liệu bắt buộc trước khi tiến hành bất kỳ ca mổ nào, đảm bảo quyền được biết thông tin đầy đủ của bệnh nhân. Bệnh nhân có quyền hỏi bất kỳ điều gì chưa rõ và có thể từ chối không ký nếu không đồng ý.",
        "context": "수술 전 상담, 입원 수속, 응급수술 설명 시 사용",
        "culturalNote": "한국 의료 시스템에서는 수술동의서가 법적 필수 문서이며, 환자의 자기결정권을 매우 중요하게 여깁니다. 베트남에서도 동의서 문화가 있지만, 일부 지역이나 작은 병원에서는 형식적으로 처리되는 경우가 있습니다. 한국 병원에서는 의사가 직접 설명하고 환자의 질문에 답변한 후 서명을 받는 절차를 거치므로, 통역사는 이 과정에서 환자가 충분히 이해하고 질문할 수 있도록 시간을 주어야 합니다. 특히 가족 동의의 경우, 누가 서명 권한이 있는지 한국 법률을 설명해야 할 수 있습니다.",
        "commonMistakes": [
            {
                "mistake": "'서명만 하면 된다'는 식으로 간소화",
                "correction": "'내용을 이해한 후 동의한다는 의미'임을 명확히 전달",
                "explanation": "동의서는 법적 문서이므로 환자가 내용을 이해했다는 것을 확인하는 과정이 필수입니다"
            },
            {
                "mistake": "합병증 부분을 축소하거나 생략",
                "correction": "합병증 내용도 정확히 통역하되, 발생 확률도 함께 설명",
                "explanation": "환자가 위험성을 알 권리가 있으며, 법적으로도 충분한 설명이 필요합니다"
            },
            {
                "mistake": "'giấy cam kết' (약속서)로 통역",
                "correction": "'giấy đồng ý' (동의서)로 정확히 표현",
                "explanation": "'cam kết'는 일방적 약속이지만 'đồng ý'는 양방향 합의를 의미하므로 의학적 맥락에 더 적합합니다"
            }
        ],
        "examples": [
            {
                "ko": "수술동의서에 서명하시기 전에 궁금한 점이 있으시면 언제든 질문해주세요.",
                "vi": "Trước khi ký vào giấy đồng ý phẫu thuật, nếu có bất kỳ điều gì thắc mắc, bạn cứ hỏi bất cứ lúc nào.",
                "situation": "formal"
            },
            {
                "ko": "이 동의서에는 수술 방법과 예상되는 합병증이 적혀 있습니다.",
                "vi": "Trong giấy đồng ý này có ghi phương pháp phẫu thuật và các biến chứng có thể xảy ra.",
                "situation": "onsite"
            },
            {
                "ko": "보호자 분도 함께 동의서를 읽어보시고 서명해주셔야 해요.",
                "vi": "Người nhà cũng cần đọc giấy đồng ý cùng và ký tên.",
                "situation": "informal"
            }
        ],
        "relatedTerms": ["informed consent", "합병증설명", "보호자동의", "응급수술"]
    },
    {
        "slug": "bien-chung",
        "korean": "합병증",
        "vietnamese": "Biến chứng",
        "hanja": "合倂症",
        "hanjaReading": "合(합할 합) + 倂(아울러 병) + 症(병 증)",
        "pronunciation": "비엔 쯩",
        "meaningKo": "질병이나 수술 후에 발생하는 예상치 못한 새로운 병적 상태나 증상을 의미합니다. 통역 시 주의할 점은 베트남어 'biến chứng'가 '변화된 증상'이라는 뜻으로 환자가 비교적 쉽게 이해할 수 있지만, 합병증이 '실수'나 '의료진의 잘못'이 아니라 '의학적으로 예측 가능한 위험'이라는 점을 명확히 전달해야 합니다. 합병증 설명 시 발생 확률도 함께 통역하여 환자가 과도한 불안을 갖지 않도록 해야 하며, 동시에 합병증 발생 시 대처 방법도 함께 설명하여 신뢰를 줄 수 있습니다. 특히 '부작용'(tác dụng phụ)과 구분하여 통역해야 합니다.",
        "meaningVi": "Tình trạng bệnh lý mới hoặc triệu chứng không mong muốn xảy ra trong hoặc sau quá trình điều trị, phẫu thuật hoặc do bệnh chính gây ra. Biến chứng không phải do sai sót y tế mà là nguy cơ có thể xảy ra trong y học, có thể được dự đoán và phòng ngừa nhưng không thể loại trừ hoàn toàn. Mức độ biến chứng có thể từ nhẹ đến nặng, cần được theo dõi và xử lý kịp thời.",
        "context": "수술 전 설명, 치료 계획 논의, 환자 상태 모니터링 시 사용",
        "culturalNote": "한국 의료 시스템에서는 합병증을 환자에게 미리 설명하고 동의를 받는 것이 법적 의무입니다. 베트남에서도 합병증 개념은 있지만, 일부 환자들은 합병증을 '의사의 실수'로 오해하는 경우가 있습니다. 통역 시 합병증은 의학적으로 예측 가능한 위험이며, 의료진이 최선을 다해도 발생할 수 있다는 점을 명확히 설명해야 합니다. 한국 병원은 합병증 예방 프로토콜이 체계적이며, 발생 시 신속한 대처 시스템이 있다는 점을 강조하면 환자의 신뢰를 얻을 수 있습니다.",
        "commonMistakes": [
            {
                "mistake": "'부작용'(tác dụng phụ)과 혼용",
                "correction": "합병증은 'biến chứng', 부작용은 'tác dụng phụ'로 구분",
                "explanation": "부작용은 약물의 예상된 반응이고, 합병증은 질병/수술 후 발생하는 새로운 병적 상태로 개념이 다릅니다"
            },
            {
                "mistake": "'의사 잘못'이라는 뉘앙스로 전달",
                "correction": "'의학적으로 예측 가능한 위험'임을 명확히 설명",
                "explanation": "합병증을 의료 과실로 오해하면 환자-의료진 간 신뢰가 무너질 수 있습니다"
            },
            {
                "mistake": "발생 확률 없이 합병증만 나열",
                "correction": "각 합병증의 발생 확률과 예방 방법도 함께 통역",
                "explanation": "확률 정보 없이 합병증만 나열하면 환자가 과도하게 불안해할 수 있습니다"
            }
        ],
        "examples": [
            {
                "ko": "이 수술의 주요 합병증으로는 출혈, 감염, 혈전증이 있으며 각각 발생률은 1% 미만입니다.",
                "vi": "Các biến chứng chính của ca phẫu thuật này bao gồm chảy máu, nhiễm trùng, và huyết khối, tỷ lệ xảy ra mỗi loại đều dưới 1%.",
                "situation": "formal"
            },
            {
                "ko": "당뇨가 있으신 분은 수술 후 합병증 위험이 높아서 혈당 관리가 중요합니다.",
                "vi": "Người có tiểu đường có nguy cơ biến chứng sau phẫu thuật cao hơn nên việc kiểm soát đường huyết rất quan trọng.",
                "situation": "onsite"
            },
            {
                "ko": "합병증이 생기면 바로 의료진에게 알려주셔야 빨리 치료할 수 있어요.",
                "vi": "Nếu có biến chứng xảy ra, bạn phải báo ngay cho nhân viên y tế để có thể điều trị kịp thời.",
                "situation": "informal"
            }
        ],
        "relatedTerms": ["부작용", "후유증", "감염", "수술위험도"]
    },
    {
        "slug": "quan-ly-dau-sau-phau-thuat",
        "korean": "수술후통증관리",
        "vietnamese": "Quản lý đau sau phẫu thuật",
        "hanja": "手術後痛症管理",
        "hanjaReading": "手(손 수) + 術(재주 술) + 後(뒤 후) + 痛(아플 통) + 症(병 증) + 管(대롱 관) + 理(다스릴 리)",
        "pronunciation": "꽌 리 다우 사우 퍼우 투엇",
        "meaningKo": "수술 후 발생하는 통증을 체계적으로 평가하고 적절한 방법으로 조절하여 환자의 회복을 돕는 의료 행위입니다. 통역 시 중요한 점은 'quản lý'(관리)라는 표현으로 단순히 진통제를 주는 것이 아니라 '체계적으로 관리한다'는 개념을 전달하는 것입니다. 환자에게 통증 척도(0-10점)를 설명하고, 참을 필요 없이 아프면 말해야 한다는 점을 강조해야 합니다. 베트남 환자들 중에는 '참는 것이 미덕'이라고 생각하거나 진통제 중독을 걱정하는 경우가 있으므로, 적절한 통증 관리가 회복에 도움이 된다는 점을 설명해야 합니다.",
        "meaningVi": "Hoạt động y tế đánh giá và kiểm soát cơn đau xảy ra sau phẫu thuật bằng các phương pháp phù hợp nhằm giúp bệnh nhân hồi phục tốt hơn. Bao gồm việc sử dụng thuốc giảm đau, các kỹ thuật vật lý trị liệu, và theo dõi mức độ đau thường xuyên. Quản lý đau hiệu quả giúp bệnh nhân di chuyển sớm hơn, giảm nguy cơ biến chứng và rút ngắn thời gian nằm viện.",
        "context": "수술 후 회복실, 병동 간호, 통증 평가 시 사용",
        "culturalNote": "한국 병원에서는 수술 후 통증 관리를 매우 중요하게 여기며, 정기적으로 통증 점수를 측정하고 기록합니다. PCA(자가통증조절장치)를 적극적으로 사용하며, 환자가 참지 말고 아프면 바로 말하도록 교육합니다. 베트남에서는 통증을 참는 것을 미덕으로 여기는 문화가 있어, 일부 환자들은 진통제 요청을 꺼릴 수 있습니다. 통역 시 적절한 통증 관리가 회복 속도를 높이고 합병증을 줄인다는 의학적 근거를 설명하여 환자가 적극적으로 통증을 표현하도록 유도해야 합니다.",
        "commonMistakes": [
            {
                "mistake": "'진통제 처방'으로만 단순화",
                "correction": "'통증 평가 + 다양한 방법의 관리'로 포괄적으로 설명",
                "explanation": "통증 관리는 약물뿐 아니라 자세, 냉찜질, 심호흡 등 다양한 방법을 포함합니다"
            },
            {
                "mistake": "통증 척도 설명 없이 '얼마나 아프냐'고만 물음",
                "correction": "0-10점 척도를 설명하고 객관적으로 평가",
                "explanation": "통증은 주관적이므로 표준화된 척도를 사용해야 정확한 평가와 기록이 가능합니다"
            },
            {
                "mistake": "'참으면 강하다'는 문화적 편견 강화",
                "correction": "'적절한 통증 관리가 빠른 회복에 도움이 된다'고 교육",
                "explanation": "과도한 통증은 스트레스 호르몬 증가, 면역력 저하 등 회복을 방해하므로 관리가 필수입니다"
            }
        ],
        "examples": [
            {
                "ko": "수술 후 통증은 0에서 10까지 숫자로 표현해주시면 적절한 진통제를 드리겠습니다.",
                "vi": "Mức độ đau sau phẫu thuật bạn hãy cho biết theo thang điểm từ 0 đến 10, chúng tôi sẽ cho thuốc giảm đau phù hợp.",
                "situation": "formal"
            },
            {
                "ko": "통증이 5점 이상이면 참지 마시고 바로 말씀해주세요.",
                "vi": "Nếu mức đau từ 5 điểm trở lên, đừng chịu đựng mà hãy nói ngay.",
                "situation": "onsite"
            },
            {
                "ko": "PCA 버튼 누르면 자동으로 진통제가 들어가니까 아플 때 누르세요.",
                "vi": "Khi bạn nhấn nút PCA, thuốc giảm đau sẽ tự động được bơm vào, nên khi đau thì hãy nhấn.",
                "situation": "informal"
            }
        ],
        "relatedTerms": ["PCA", "통증척도", "진통제", "마취통증의학과"]
    },
    {
        "slug": "phong-cham-soc-tich-cuc",
        "korean": "중환자실",
        "vietnamese": "Phòng chăm sóc tích cực",
        "hanja": "重患者室",
        "hanjaReading": "重(무거울 중) + 患(근심 환) + 者(사람 자) + 室(집 실)",
        "pronunciation": "퐁 짬 쏙 틱 껙",
        "meaningKo": "생명이 위독하거나 중증 질환으로 집중적인 모니터링과 치료가 필요한 환자를 24시간 관리하는 특수 병실입니다. 통역 시 'chăm sóc tích cực'(집중 치료)라는 표현이 단순히 '조금 더 신경 쓴다'는 의미가 아니라 '생명 유지를 위한 고도의 의료 장비와 전문 인력이 투입된다'는 점을 명확히 전달해야 합니다. 환자 가족에게 ICU 입실이 '위급 상황'을 의미할 수 있으므로, 예방적 입실인지 응급 상황인지를 구분하여 설명해야 하며, 면회 제한 규정과 그 이유(감염 예방)도 함께 통역해야 합니다.",
        "meaningVi": "Phòng bệnh đặc biệt dành cho bệnh nhân nguy kịch hoặc bệnh nặng, cần theo dõi sát và điều trị chuyên sâu 24/24 giờ. Được trang bị các thiết bị y tế hiện đại như máy thở, máy theo dõi nhịp tim, máy lọc máu, và có đội ngũ bác sĩ, điều dưỡng chuyên khoa hồi sức tích cực luôn túc trực. Thường viết tắt là ICU (Intensive Care Unit).",
        "context": "중증 환자 이송, 수술 후 관리, 응급 상황 설명 시 사용",
        "culturalNote": "한국 대형병원의 중환자실은 최첨단 장비와 1:1 또는 1:2 간호 인력 배치로 매우 체계적입니다. 면회가 엄격히 제한되며, 보호자가 24시간 상주할 수 없는 것이 일반적입니다. 베트남에서는 중환자실이 있는 병원이 제한적이며, 일부 병원에서는 보호자가 함께 상주하는 문화가 있어 한국의 엄격한 면회 규정에 당황할 수 있습니다. 통역 시 면회 제한이 환자의 안전과 감염 예방을 위한 것임을 설명하고, 정해진 면회 시간과 규칙을 명확히 전달해야 합니다.",
        "commonMistakes": [
            {
                "mistake": "'응급실'(Phòng cấp cứu)과 혼동",
                "correction": "중환자실은 'ICU - Phòng chăm sóc tích cực', 응급실은 'ER - Phòng cấp cứu'로 구분",
                "explanation": "응급실은 급성 환자 초기 처치 공간이고, 중환자실은 중증 환자 집중 치료 공간으로 역할이 다릅니다"
            },
            {
                "mistake": "'일반 병실보다 조금 더 신경 쓴다'고 축소",
                "correction": "'생명 유지 장비와 전문 인력이 24시간 집중 관리한다'고 정확히 설명",
                "explanation": "ICU의 의료 수준과 중요성을 정확히 전달해야 환자 가족이 상황을 이해할 수 있습니다"
            },
            {
                "mistake": "면회 제한 이유 설명 없이 규칙만 전달",
                "correction": "감염 예방과 환자 안정을 위한 것임을 먼저 설명 후 규칙 안내",
                "explanation": "이유를 모르면 가족이 '환자를 못 보게 한다'고 오해하거나 불만을 가질 수 있습니다"
            }
        ],
        "examples": [
            {
                "ko": "수술 후 안전을 위해 하루 정도 중환자실에서 집중 관리를 받으시게 됩니다.",
                "vi": "Sau phẫu thuật, để đảm bảo an toàn, bạn sẽ được chăm sóc tích cực tại phòng ICU khoảng một ngày.",
                "situation": "formal"
            },
            {
                "ko": "중환자실은 감염 예방을 위해 면회 시간이 하루 두 번, 각 10분으로 제한됩니다.",
                "vi": "Phòng chăm sóc tích cực hạn chế giờ thăm bệnh hai lần mỗi ngày, mỗi lần 10 phút để phòng ngừa nhiễm trùng.",
                "situation": "onsite"
            },
            {
                "ko": "중환자실에는 인공호흡기, 심장 모니터 등이 있어서 24시간 환자 상태를 지켜봐요.",
                "vi": "Phòng ICU có máy thở, màn hình theo dõi tim và nhiều thiết bị khác để theo dõi tình trạng bệnh nhân 24 giờ.",
                "situation": "informal"
            }
        ],
        "relatedTerms": ["인공호흡기", "모니터링", "집중치료", "응급실"]
    },
    {
        "slug": "may-tho",
        "korean": "인공호흡기",
        "vietnamese": "Máy thở",
        "hanja": "人工呼吸器",
        "hanjaReading": "人(사람 인) + 工(장인 공) + 呼(부를 호) + 吸(마실 흡) + 器(그릇 기)",
        "pronunciation": "마이 터",
        "meaningKo": "스스로 호흡할 수 없거나 호흡이 불충분한 환자의 폐에 공기를 강제로 넣어주어 생명을 유지시키는 의료 기기입니다. 통역 시 베트남어 'máy thở'는 문자 그대로 '숨쉬는 기계'라는 뜻으로 이해하기 쉬우나, 환자나 가족이 '기계가 숨을 쉬어준다'는 것이 '완전히 의식이 없다' 또는 '죽어간다'는 뜻으로 오해할 수 있으므로 주의해야 합니다. 인공호흡기 적용이 반드시 말기 상태를 의미하는 것은 아니며, 수술 중 마취 시에도 사용된다는 점을 설명해야 합니다. 또한 인공호흡기 제거(발관) 과정과 시기도 함께 설명하여 희망을 주는 것이 중요합니다.",
        "meaningVi": "Thiết bị y tế hỗ trợ hoặc thay thế hoàn toàn chức năng hô hấp cho bệnh nhân không thể tự thở hoặc thở không đủ, giúp duy trì sự sống bằng cách đưa không khí vào phổi. Máy thở được sử dụng trong phòng mổ khi gây mê, trong ICU cho bệnh nhân nguy kịch, hoặc cho người bị suy hô hấp. Có nhiều chế độ máy thở tùy theo tình trạng bệnh nhân.",
        "context": "중환자실 치료, 전신마취 수술, 호흡 부전 환자 관리 시 사용",
        "culturalNote": "한국 병원의 인공호흡기는 다양한 모드와 정밀한 설정이 가능하며, 조기에 이탈(weaning) 프로토콜을 적용하여 환자가 빨리 자가 호흡으로 돌아가도록 합니다. 베트남에서는 인공호흡기가 '거의 죽어가는 사람'에게만 사용된다는 인식이 있어, 가족들이 매우 충격을 받을 수 있습니다. 통역 시 인공호흡기가 '일시적인 호흡 보조 수단'이며, 많은 환자가 회복 후 제거한다는 점을 강조해야 합니다. 또한 기관삽관(intubation)과 인공호흡기를 구분하여 설명하고, 환자가 의식이 있어도 기계 호흡을 할 수 있다는 점도 알려야 합니다.",
        "commonMistakes": [
            {
                "mistake": "'máy thở = 환자가 죽어간다'는 뉘앙스로 전달",
                "correction": "'호흡을 돕는 의료 기기이며 회복 가능하다'고 희망적으로 설명",
                "explanation": "인공호흡기 사용이 반드시 예후 불량을 의미하지 않으며, 수술이나 일시적 치료에도 사용됩니다"
            },
            {
                "mistake": "인공호흡기와 산소마스크를 혼동",
                "correction": "산소마스크는 'mặt nạ dưỡng khí', 인공호흡기는 'máy thở'로 구분",
                "explanation": "산소마스크는 보조적 산소 공급이고, 인공호흡기는 기계적 환기로 완전히 다릅니다"
            },
            {
                "mistake": "발관(제거) 가능성 언급 없이 적용만 설명",
                "correction": "적용 이유와 함께 회복 시 제거 가능하다는 계획도 전달",
                "explanation": "가족에게 희망을 주고, 치료 목표를 이해시키기 위해 전체 과정을 설명해야 합니다"
            }
        ],
        "examples": [
            {
                "ko": "전신마취 수술 중에는 모든 환자가 인공호흡기를 사용하며, 수술 후 깨어나면 바로 제거합니다.",
                "vi": "Trong ca mổ gây mê toàn thân, tất cả bệnh nhân đều sử dụng máy thở, và khi tỉnh sau phẫu thuật sẽ tháo ngay.",
                "situation": "formal"
            },
            {
                "ko": "인공호흡기는 환자분의 폐가 쉴 수 있도록 일시적으로 숨을 도와주는 기계예요.",
                "vi": "Máy thở là thiết bị tạm thời giúp hỗ trợ hô hấp để phổi của bệnh nhân được nghỉ ngơi.",
                "situation": "onsite"
            },
            {
                "ko": "상태가 좋아지면 점차 인공호흡기 의존도를 줄이고 스스로 숨쉬도록 연습해요.",
                "vi": "Khi tình trạng được cải thiện, chúng tôi sẽ giảm dần sự phụ thuộc vào máy thở và luyện tập thở tự nhiên.",
                "situation": "informal"
            }
        ],
        "relatedTerms": ["기관삽관", "발관", "산소포화도", "호흡부전"]
    },
    {
        "slug": "phong-ngua-loet",
        "korean": "욕창예방",
        "vietnamese": "Phòng ngừa loét",
        "hanja": "褥瘡豫防",
        "hanjaReading": "褥(자리 욕) + 瘡(부스럼 창) + 豫(미리 예) + 防(막을 방)",
        "pronunciation": "퐁 응어 로엣",
        "meaningKo": "장시간 같은 자세로 누워있거나 앉아있을 때 압력을 받는 부위의 피부와 조직이 손상되지 않도록 미리 관리하는 간호 행위입니다. 통역 시 베트남어 'loét'는 '궤양'을 의미하며, 단순한 '까짐'이 아니라 깊은 조직 손상으로 이어질 수 있는 심각한 문제라는 점을 전달해야 합니다. 욕창 예방을 위한 체위 변경(2시간마다)의 중요성과 보호자의 협조가 필요하다는 점을 강조하고, 욕창이 한번 생기면 치료가 매우 어렵고 고통스러우므로 예방이 최선이라는 점을 설명해야 합니다. 특히 중환자실이나 장기 입원 환자에게 필수적인 관리임을 명확히 해야 합니다.",
        "meaningVi": "Hoạt động chăm sóc nhằm ngăn ngừa tổn thương da và mô dưới da ở những vùng chịu áp lực khi bệnh nhân nằm hoặc ngồi lâu ở một tư thế. Bao gồm việc thay đổi tư thế định kỳ (mỗi 2 giờ), sử dụng đệm chống loét, giữ da sạch và khô, cải thiện dinh dưỡng. Loét do tỳ đè nếu không phòng ngừa có thể gây nhiễm trùng nghiêm trọng và rất khó lành.",
        "context": "중환자 간호, 장기 입원 환자 관리, 마비 환자 케어 시 사용",
욕창예방은 한국 병원에서 간호의 핵심 질 지표 중 하나이며, 체위 변경 스케줄과 피부 상태 기록이 체계적으로 관리됩니다. 에어매트, 쿠션 등 예방 장비도 적극 활용합니다. 베트남에서는 욕창 예방 개념이 덜 강조되거나, 보호자가 직접 체위 변경을 해야 하는 경우가 많습니다. 한국 병원에서는 간호사가 주도적으로 예방 관리를 하지만, 보호자의 협조도 필요하므로 통역 시 체위 변경의 중요성과 방법을 명확히 교육해야 합니다. 또한 욕창 고위험 부위(엉덩이, 발꿈치, 팔꿈치 등)를 설명하고 관찰 방법을 알려주는 것이 좋습니다.",
        "commonMistakes": [
            {
                "mistake": "'loét da' (피부 궤양)로만 단순화",
                "correction": "'loét do tỳ đè' (압력 궤양) 또는 'loét bệnh viện'으로 구체화",
                "explanation": "욕창은 압력에 의한 특수한 유형의 궤양이므로 원인을 명확히 해야 예방 방법을 이해할 수 있습니다"
            },
            {
                "mistake": "'가끔 뒤집어드리면 된다'고 축소",
                "correction": "'2시간마다 정기적으로 체위를 변경해야 한다'고 정확한 주기 전달",
                "explanation": "불규칙한 체위 변경은 효과가 없으며, 2시간 주기가 의학적 권장 사항입니다"
            },
            {
                "mistake": "욕창 발생 후 치료만 설명",
                "correction": "예방의 중요성을 먼저 강조하고 '한번 생기면 치료가 매우 어렵다' 경고",
                "explanation": "욕창은 예방이 최선이며, 발생 후에는 치료가 길고 고통스러우므로 예방 동기 부여가 중요합니다"
            }
        ],
        "examples": [
            {
                "ko": "욕창 예방을 위해 2시간마다 환자분의 자세를 바꿔드리고 있으니 협조 부탁드립니다.",
                "vi": "Để phòng ngừa loét do tỳ đè, chúng tôi sẽ thay đổi tư thế cho bệnh nhân mỗi 2 giờ, mong quý vị hợp tác.",
                "situation": "formal"
            },
            {
                "ko": "엉덩이, 발꿈치, 팔꿈치 같은 뼈가 튀어나온 부분을 자주 확인해주세요.",
                "vi": "Các vùng xương nhô ra như mông, gót chân, khuỷu tay cần được kiểm tra thường xuyên.",
                "situation": "onsite"
            },
            {
                "ko": "욕창 생기면 치료하기 정말 힘들어서 미리 예방하는 게 최선이에요.",
                "vi": "Loét do tỳ đè nếu xảy ra rất khó điều trị nên phòng ngừa từ đầu là tốt nhất.",
                "situation": "informal"
            }
        ],
        "relatedTerms": ["체위변경", "에어매트", "압력궤양", "피부간호"]
    },
    {
        "slug": "truyen-mau",
        "korean": "수혈",
        "vietnamese": "Truyền máu",
        "hanja": "輸血",
        "hanjaReading": "輸(보낼 수) + 血(피 혈)",
        "pronunciation": "쭈엔 마우",
        "meaningKo": "출혈, 빈혈, 혈액 질환 등으로 인해 부족해진 혈액이나 혈액 성분을 환자에게 정맥으로 주입하는 치료법입니다. 통역 시 베트남어 'truyền máu'는 문자 그대로 '피를 수혈하다'라는 뜻으로 이해하기 쉬우나, 수혈 전 동의서, 혈액형 교차 검사, 수혈 부작용 관찰 등 복잡한 절차가 있다는 점을 명확히 전달해야 합니다. 특히 베트남 환자들 중에는 종교적 또는 문화적 이유로 수혈을 거부하는 경우가 있을 수 있으므로, 수혈의 필요성과 대안(자가수혈 등)을 충분히 설명해야 합니다. 또한 수혈 중 발열, 두드러기 등 부작용 발생 시 즉시 알려야 한다는 점을 강조해야 합니다.",
        "meaningVi": "Phương pháp điều trị bằng cách truyền máu hoặc các thành phần máu (hồng cầu, tiểu cầu, huyết tương) vào tĩnh mạch cho bệnh nhân bị thiếu máu do chảy máu,빈혈, hoặc bệnh lý về máu. Trước khi truyền máu phải xét nghiệm nhóm máu, làm test phản ứng chéo, và theo dõi sát bệnh nhân để phát hiện phản ứng phụ như sốt, ngứa, khó thở.",
        "context": "수술 전후, 응급 출혈, 빈혈 치료, 혈액 질환 시 사용",
        "culturalNote": "한국 병원의 수혈 시스템은 매우 안전하며, 혈액은행에서 철저한 검사를 거친 혈액만 사용합니다. HIV, 간염 등 감염 검사가 필수이며, 교차 시험으로 적합성을 확인합니다. 베트남에서는 혈액 수급이 원활하지 않아 가족이 직접 헌혈하는 경우가 많고, 일부는 혈액 안전성에 대한 우려가 있을 수 있습니다. 통역 시 한국의 체계적인 혈액 관리 시스템과 안전성을 강조하고, 수혈 동의서 작성의 중요성을 설명해야 합니다. 또한 종교적 이유(여호와의 증인 등)로 수혈을 거부하는 경우 대안을 의료진과 상의하도록 안내해야 합니다.",
        "commonMistakes": [
            {
                "mistake": "'그냥 피 넣어주는 것'으로 단순화",
                "correction": "'혈액형 확인, 교차 시험, 동의서, 부작용 관찰 등 체계적 절차'임을 설명",
                "explanation": "수혈은 복잡한 의료 행위이며, 환자가 절차를 이해해야 협조가 원활합니다"
            },
            {
                "mistake": "'máu của người khác' (다른 사람 피)라고만 표현",
                "correction": "'máu đã qua kiểm tra an toàn' (안전 검사를 거친 혈액)으로 안전성 강조",
                "explanation": "환자가 '누구의 피인지 모른다'는 불안을 느끼지 않도록 안전성을 먼저 설명해야 합니다"
            },
            {
                "mistake": "수혈 부작용 가능성을 언급하지 않음",
                "correction": "수혈 중 발열, 두드러기 등 발생 시 즉시 알려야 한다고 미리 교육",
                "explanation": "부작용 발생 시 조기 발견과 대처가 중요하므로 환자가 증상을 인지하고 보고하도록 해야 합니다"
            }
        ],
        "examples": [
            {
                "ko": "수술 중 출혈량이 많아 수혈이 필요하니 동의서에 서명 부탁드립니다.",
                "vi": "Do lượng máu mất nhiều trong phẫu thuật nên cần truyền máu, xin ký vào giấy đồng ý.",
                "situation": "formal"
            },
            {
                "ko": "수혈하는 동안 몸에 이상 증상 있으면 바로 간호사에게 말씀하세요.",
                "vi": "Trong quá trình truyền máu, nếu có bất kỳ triệu chứng bất thường nào thì hãy báo ngay cho y tá.",
                "situation": "onsite"
            },
            {
                "ko": "혈색소 수치가 너무 낮아서 수혈해야 빨리 회복할 수 있어요.",
                "vi": "Chỉ số huyết sắc tố quá thấp nên phải truyền máu mới có thể hồi phục nhanh.",
                "situation": "informal"
            }
        ],
        "relatedTerms": ["혈액형", "교차시험", "수혈부작용", "자가수혈"]
    }
]

def main():
    print("=" * 60)
    print("수술/마취/중환자 관련 의료 용어 10개 추가 스크립트")
    print("=" * 60)

    # 파일 존재 확인
    if not os.path.exists(file_path):
        print(f"❌ 파일을 찾을 수 없습니다: {file_path}")
        return

    # 기존 데이터 로드
    with open(file_path, 'r', encoding='utf-8') as f:
        data = json.load(f)

    print(f"\n📂 파일 로드 완료: {file_path}")
    print(f"📊 기존 용어 개수: {len(data)}")

    # 중복 확인 (slug 기준)
    existing_slugs = {term['slug'] for term in data}
    new_terms_filtered = [term for term in new_terms if term['slug'] not in existing_slugs]
    duplicates = [term['slug'] for term in new_terms if term['slug'] in existing_slugs]

    if duplicates:
        print(f"\n⚠️  중복된 용어 {len(duplicates)}개 발견 (추가하지 않음):")
        for slug in duplicates:
            print(f"   - {slug}")

    if not new_terms_filtered:
        print("\n❌ 추가할 새 용어가 없습니다 (모두 중복)")
        return

    print(f"\n✅ 추가할 새 용어: {len(new_terms_filtered)}개")
    for term in new_terms_filtered:
        print(f"   - {term['korean']} ({term['slug']})")

    # 데이터 추가
    data.extend(new_terms_filtered)

    # 파일 저장
    with open(file_path, 'w', encoding='utf-8') as f:
        json.dump(data, f, ensure_ascii=False, indent=2)

    print(f"\n💾 파일 저장 완료!")
    print(f"📊 최종 용어 개수: {len(data)}")
    print("\n" + "=" * 60)
    print("✨ 작업 완료!")
    print("=" * 60)

if __name__ == "__main__":
    main()
