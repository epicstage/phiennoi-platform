#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
정신건강/중독/상담 분야 의료 전문용어 10개 추가 스크립트
Medical Terms Addition: Mental Health/Addiction/Counseling (v6-ff)
"""

import json
import os

# 파일 경로 설정 (상대 경로 사용)
file_path = os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', 'data', 'terms', 'medical.json')

# 추가할 용어 데이터 (10개)
new_terms = [
    {
        "slug": "nghien-ruou",
        "korean": "알코올중독",
        "vietnamese": "Nghiện rượu",
        "hanja": "alcohol中毒",
        "hanjaReading": "alcohol + 中(가운데 중) 毒(독 독)",
        "pronunciation": "응이엔 쭈",
        "meaningKo": "알코올에 대한 신체적, 정신적 의존 상태를 의미하며, 베트남어로는 'Nghiện rượu' 또는 'Nghiện rượu bia'라고 표현합니다. 통역 시 주의할 점은 베트남에서는 사회적 음주 문화가 발달해 있어 '알코올중독'과 '과음'을 명확히 구분해야 하며, 의학적 진단으로서의 중독(nghiện)과 일시적인 과음(say rượu)을 혼동하지 않도록 해야 합니다. 또한 치료 계획 설명 시 'cai nghiện rượu'(금주 치료)와 'điều trị nghiện rượu'(알코올중독 치료) 용어를 정확히 구분하여 사용해야 합니다.",
        "meaningVi": "Tình trạng phụ thuộc về thể chất và tinh thần vào rượu, được coi là một bệnh lý nghiện nghiêm trọng. Trong y học, nghiện rượu được phân loại theo ICD-10 và DSM-5, đòi hỏi can thiệp y tế chuyên sâu bao gồm cai nghiện, tư vấn tâm lý và theo dõi dài hạn.",
        "context": "정신건강의학과, 중독치료센터, 재활치료, 상담",
        "culturalNote": "한국에서는 알코올중독을 질병으로 인식하는 경향이 강하며 전문 치료기관이 많은 반면, 베트남에서는 아직 '의지 부족'으로 여기는 경향이 있어 치료보다는 가족의 관리에 의존하는 경우가 많습니다. 통역 시 한국의 체계적인 치료 프로그램(12단계 프로그램, 입원치료 등)을 설명할 때 베트남 환자나 가족이 이해할 수 있도록 질병 개념을 강조해야 합니다. 또한 한국에서는 직장 내 알코올 문제가 산업재해로 인정받을 수 있지만 베트남에서는 개인 문제로 치부되는 차이가 있습니다.",
        "commonMistakes": [
            {
                "mistake": "Nghiện rượu를 say rượu(술 취함)와 혼용",
                "correction": "Nghiện rượu는 중독 질환, say rượu는 일시적 취기 상태",
                "explanation": "중독은 만성적 의존 상태이며 질병 코드가 부여되는 반면, 취기는 일시적 현상이므로 의학 기록에서 명확히 구분 필요"
            },
            {
                "mistake": "Cai rượu를 điều trị nghiện rượu와 동일하게 사용",
                "correction": "Cai rượu는 금주/단주, điều trị nghiện rượu는 통합적 중독 치료",
                "explanation": "금주는 치료의 일부이며, 중독 치료는 심리상담, 약물치료, 재활까지 포함하는 포괄적 개념"
            },
            {
                "mistake": "Uống nhiều rượu(술을 많이 마심)를 중독으로 번역",
                "correction": "과음과 중독은 다름 - 중독은 조절 능력 상실 상태",
                "explanation": "단순 과음은 nghiện이 아니라 uống quá nhiều로 표현하며, 의학적 진단 기준(DSM-5)을 충족해야 nghiện rượu 진단 가능"
            }
        ],
        "examples": [
            {
                "ko": "환자는 10년간 알코올중독 병력이 있으며 금단증상이 심각합니다.",
                "vi": "Bệnh nhân có tiền sử nghiện rượu 10 năm và triệu chứng cắt cơn rất nghiêm trọng.",
                "situation": "formal"
            },
            {
                "ko": "알코올중독 치료를 위해 3개월 입원 프로그램을 권장합니다.",
                "vi": "Chúng tôi khuyến nghị chương trình điều trị nội trú 3 tháng để cai nghiện rượu.",
                "situation": "formal"
            },
            {
                "ko": "술 끊으려고 여러 번 시도했지만 금단증상 때문에 실패했어요.",
                "vi": "Tôi đã thử bỏ rượu nhiều lần nhưng thất bại do triệu chứng cắt cơn.",
                "situation": "informal"
            }
        ],
        "relatedTerms": ["금단증상", "해독치료", "재활치료", "약물중독"]
    },
    {
        "slug": "nghien-ma-tuy",
        "korean": "약물중독",
        "vietnamese": "Nghiện ma túy",
        "hanja": "藥物中毒",
        "hanjaReading": "藥(약 약) 物(물건 물) 中(가운데 중) 毒(독 독)",
        "pronunciation": "응이엔 마 뚜이",
        "meaningKo": "마약류 또는 향정신성의약품에 대한 신체적, 정신적 의존 상태를 의미하며, 베트남어로 'Nghiện ma túy' 또는 'Nghiện chất gây nghiện'으로 표현합니다. 통역 시 매우 중요한 점은 한국에서 '약물중독'은 불법 마약뿐 아니라 처방약 남용도 포함하지만, 베트남에서 ma túy는 주로 불법 마약을 지칭하므로 처방약 중독은 'nghiện thuốc kê đơn'으로 별도 구분해야 합니다. 또한 법적 처벌과 의료적 치료의 경계가 양국에서 다르므로 치료 계획 설명 시 신중한 용어 선택이 필요합니다.",
        "meaningVi": "Tình trạng phụ thuộc vào ma túy hoặc các chất dạng ma túy, bao gồm cả thuốc kê đơn bị lạm dụng. Đây là bệnh lý nghiện nghiêm trọng cần điều trị y tế chuyên khoa kết hợp với can thiệp tâm lý xã hội và có thể liên quan đến vấn đề pháp lý.",
        "context": "정신건강의학과, 중독치료센터, 법의학, 응급의학",
        "culturalNote": "한국에서는 약물중독자를 환자로 보고 치료를 우선시하는 의료화 경향이 강한 반면, 베트남에서는 법적 처벌이 우선되며 치료시설보다는 강제 재활센터(trại cai nghiện)에 수용되는 경우가 많습니다. 통역 시 한국의 외래 치료, 대체요법(메타돈 치료 등) 프로그램을 설명할 때 베트남 환자나 가족이 이를 '처벌 회피'로 오해하지 않도록 의학적 근거를 명확히 설명해야 합니다. 또한 베트남에서는 마약 사용자에 대한 사회적 낙인이 매우 강해 치료 접근성이 낮다는 문화적 차이를 고려해야 합니다.",
        "commonMistakes": [
            {
                "mistake": "Ma túy를 모든 약물에 사용",
                "correction": "Ma túy는 불법 마약, 처방약 남용은 lạm dụng thuốc kê đơn",
                "explanation": "Ma túy는 법적으로 금지된 마약류를 지칭하며, 처방약 의존은 별도 용어로 구분해야 법적 오해 방지 가능"
            },
            {
                "mistake": "Điều trị nghiện를 trại cai nghiện(강제 재활소)로만 이해",
                "correction": "의료적 치료는 điều trị y tế, 강제 수용은 cơ sở cai nghiện bắt buộc",
                "explanation": "베트남 환자가 한국의 자발적 외래 치료를 이해할 수 있도록 강제 수용과 다름을 명확히 구분 필요"
            },
            {
                "mistake": "중독을 nghiện와 say로 혼용",
                "correction": "Nghiện은 의존성 중독, say는 일시적 취기(알코올) 또는 환각 상태",
                "explanation": "Say는 일시적 상태를, nghiện은 만성적 의존을 의미하므로 진단명으로는 nghiện 사용 필수"
            }
        ],
        "examples": [
            {
                "ko": "환자는 헤로인 약물중독으로 해독치료가 시급합니다.",
                "vi": "Bệnh nhân nghiện heroin cần điều trị giải độc khẩn cấp.",
                "situation": "formal"
            },
            {
                "ko": "처방받은 진통제에 중독되어 용량을 계속 늘리고 있어요.",
                "vi": "Tôi bị nghiện thuốc giảm đau được kê đơn và liên tục tăng liều.",
                "situation": "informal"
            },
            {
                "ko": "약물중독 치료를 위해 메타돈 대체요법을 시작하겠습니다.",
                "vi": "Chúng tôi sẽ bắt đầu liệu pháp thay thế methadone để điều trị nghiện ma túy.",
                "situation": "formal"
            }
        ],
        "relatedTerms": ["알코올중독", "금단증상", "해독치료", "재활치료"]
    },
    {
        "slug": "nghien-game",
        "korean": "게임중독",
        "vietnamese": "Nghiện game",
        "hanja": "game中毒",
        "hanjaReading": "game + 中(가운데 중) 毒(독 독)",
        "pronunciation": "응이엔 게임",
        "meaningKo": "게임 이용에 대한 조절 능력을 상실하여 일상생활에 심각한 지장을 초래하는 상태로, 베트남어로는 'Nghiện game' 또는 'Rối loạn chơi game'으로 표현합니다. 통역 시 중요한 점은 WHO가 2019년 '게임 이용 장애(Gaming Disorder)'를 질병으로 분류했지만 양국에서 이에 대한 인식 차이가 크다는 것입니다. 한국에서는 게임중독을 공중보건 문제로 보고 치료 프로그램이 활성화되어 있으나, 베트남에서는 아직 '교육 문제' 또는 '훈육 문제'로 여기는 경향이 강합니다. 진단 기준 설명 시 DSM-5의 '인터넷 게임 장애' 진단 기준을 명확히 전달해야 합니다.",
        "meaningVi": "Tình trạng mất kiểm soát việc chơi game dẫn đến ảnh hưởng nghiêm trọng đến cuộc sống hàng ngày. WHO đã công nhận 'Rối loạn chơi game' là bệnh lý vào năm 2019, đòi hỏi can thiệp y tế và tâm lý chuyên môn.",
        "context": "정신건강의학과, 청소년 상담, 중독치료, 학교 보건",
        "culturalNote": "한국은 세계 최초로 게임중독을 사회 문제로 인식하고 '게임 셧다운제' 등 제도적 대응을 시작한 국가로, 게임중독 전문 치료기관과 청소년 상담 프로그램이 발달해 있습니다. 반면 베트남에서는 게임중독을 부모의 통제 부족이나 자녀 교육 실패로 보는 시각이 강하며, 의료적 개입보다는 가정 내 훈육으로 해결하려는 경향이 있습니다. 통역 시 한국의 인지행동치료, 가족치료 프로그램을 설명할 때 '질병'으로서의 게임중독 개념을 충분히 설명하지 않으면 베트남 학부모가 '아이 편들기'로 오해할 수 있어 주의가 필요합니다.",
        "commonMistakes": [
            {
                "mistake": "Chơi game nhiều(게임을 많이 함)를 nghiện game으로 번역",
                "correction": "과도한 게임 이용과 중독은 다름 - 중독은 조절 불능 상태",
                "explanation": "단순히 게임을 오래 하는 것과 일상생활 기능 손상을 동반한 중독을 구분해야 정확한 진단과 치료 계획 수립 가능"
            },
            {
                "mistake": "Nghiện game을 lười học(공부 안 함)과 동일시",
                "correction": "게임중독은 의학적 질환, 학습 태만은 행동 문제",
                "explanation": "베트남 학부모가 중독을 '게으름'으로 오해하지 않도록 뇌 보상 체계 이상 등 의학적 근거 설명 필요"
            },
            {
                "mistake": "치료를 cấm chơi game(게임 금지)로만 번역",
                "correction": "치료는 điều trị nghiện game(종합 치료), 금지는 일부 방법일 뿐",
                "explanation": "한국의 단계적 치료 프로그램(인지행동치료, 대안활동 등)을 설명할 때 단순 금지와 구분 필요"
            }
        ],
        "examples": [
            {
                "ko": "게임중독으로 학업을 중단하고 하루 16시간 이상 게임만 합니다.",
                "vi": "Do nghiện game, em đã bỏ học và chơi game hơn 16 giờ mỗi ngày.",
                "situation": "formal"
            },
            {
                "ko": "게임을 안 하면 불안하고 짜증이 나서 참을 수가 없어요.",
                "vi": "Nếu không chơi game, tôi cảm thấy lo lắng và cáu gắt không chịu nổi.",
                "situation": "informal"
            },
            {
                "ko": "게임중독 치료를 위해 인지행동치료와 가족상담을 병행합니다.",
                "vi": "Chúng tôi kết hợp liệu pháp nhận thức hành vi và tư vấn gia đình để điều trị nghiện game.",
                "situation": "formal"
            }
        ],
        "relatedTerms": ["인터넷중독", "스마트폰중독", "인지행동치료", "청소년상담"]
    },
    {
        "slug": "roi-loan-stress-sau-chan-thuong",
        "korean": "외상후스트레스장애",
        "vietnamese": "Rối loạn stress sau chấn thương",
        "hanja": "外傷後stress障碍",
        "hanjaReading": "外(바깥 외) 傷(다칠 상) 後(뒤 후) + stress + 障(막을 장) 碍(거릴 애)",
        "pronunciation": "조이 로안 스트레스 사우 쩐 투엉",
        "meaningKo": "심각한 외상 사건을 경험한 후 발생하는 정신과적 장애로, 베트Nam어로는 'Rối loạn stress sau chấn thương' 또는 약어 'PTSD'로 표현합니다. 통역 시 주의할 점은 한국에서 PTSD는 전쟁, 재난, 성폭력 등 다양한 트라우마를 포괄하지만, 베트남에서는 주로 전쟁 경험자(베트남 전쟁 참전 군인)와 연관 지어 이해되는 경향이 있어, 일반적 트라우마(교통사고, 폭력, 자연재해 등)에도 적용됨을 명확히 설명해야 합니다. 또한 '악몽', '회피', '과각성' 등 핵심 증상을 설명할 때 문화적 맥락을 고려한 번역이 필요합니다.",
        "meaningVi": "Rối loạn tâm thần xảy ra sau khi trải qua hoặc chứng kiến sự kiện chấn thương nghiêm trọng như chiến tranh, tai nạn, bạo lực, thiên tai. Triệu chứng bao gồm ác mộng, hồi tưởng (flashback), tránh né, và tình trạng quá cảnh giác kéo dài trên 1 tháng.",
        "context": "정신건강의학과, 심리상담, 재난의학, 법의학",
        "culturalNote": "한국에서는 세월호 참사, 이태원 참사 등 대형 재난 이후 PTSD 치료와 트라우마 센터 설립이 활성화되었으며, 일반인도 PTSD 개념을 잘 이해하고 있습니다. 반면 베트남에서는 PTSD가 주로 베트남 전쟁 참전 군인 또는 고엽제 피해자와 연관되어 있어, 일반 시민이 교통사고나 폭력 후 PTSD를 호소하면 '과장'으로 여겨질 수 있습니다. 통역 시 PTSD가 누구에게나 발생할 수 있는 보편적 질환임을 강조하고, 한국의 체계적 트라우마 치료 프로그램(EMDR, 노출치료 등)을 설명할 때 과학적 근거를 제시하는 것이 중요합니다.",
        "commonMistakes": [
            {
                "mistake": "Chấn thương를 상처(vết thương)로만 이해",
                "correction": "Chấn thương tâm lý는 정신적 외상, 물리적 상처는 vết thương",
                "explanation": "PTSD의 chấn thương은 심리적 트라우마를 의미하며, 신체적 부상 유무와 무관하게 발생 가능함을 명확히 구분"
            },
            {
                "mistake": "PTSD를 sợ hãi(두려움)로만 번역",
                "correction": "단순 공포가 아닌 복합적 증상군 - flashback, tránh né, quá cảnh giác 포함",
                "explanation": "PTSD는 재경험, 회피, 부정적 인지/정서, 과각성의 4대 증상군으로 구성된 복합 장애임을 설명 필요"
            },
            {
                "mistake": "Stress sau chấn thương을 급성 스트레스와 혼동",
                "correction": "PTSD는 1개월 이상 지속, 급성은 rối loạn stress cấp tính(3일~1개월)",
                "explanation": "진단 기간 기준이 다르므로 치료 계획과 예후 설명 시 명확한 구분 필요"
            }
        ],
        "examples": [
            {
                "ko": "교통사고 후 3개월이 지났는데도 악몽과 불안이 계속됩니다. PTSD인가요?",
                "vi": "Đã 3 tháng sau tai nạn giao thông nhưng tôi vẫn gặp ác mộng và lo âu liên tục. Đây có phải PTSD không?",
                "situation": "informal"
            },
            {
                "ko": "외상후스트레스장애 진단을 위해 구조화된 면담을 시행하겠습니다.",
                "vi": "Chúng tôi sẽ thực hiện phỏng vấn có cấu trúc để chẩn đoán rối loạn stress sau chấn thương.",
                "situation": "formal"
            },
            {
                "ko": "EMDR 치료가 PTSD 증상 완화에 효과적입니다.",
                "vi": "Liệu pháp EMDR có hiệu quả trong việc giảm triệu chứng PTSD.",
                "situation": "formal"
            }
        ],
        "relatedTerms": ["트라우마", "급성스트레스장애", "적응장애", "불안장애"]
    },
    {
        "slug": "tam-than-phan-liet",
        "korean": "조현병",
        "vietnamese": "Tâm thần phân liệt",
        "hanja": "調絃病",
        "hanjaReading": "調(고를 조) 絃(줄 현) 病(병 병)",
        "pronunciation": "땀 틴 판 리엣",
        "meaningKo": "현실 검증 능력의 손상과 함께 망상, 환각, 와해된 언어 및 행동 등을 특징으로 하는 중증 정신질환으로, 베트남어로는 'Tâm thần phân liệt' 또는 'Bệnh tâm thần phân liệt'로 표현합니다. 통역 시 매우 중요한 점은 한국에서는 2011년 '정신분열병'에서 '조현병'으로 명칭을 변경하여 낙인을 줄이려 했으나, 베트남어 'tâm thần phân liệt'는 여전히 '정신 분열'이라는 직역적 의미를 담고 있어 강한 부정적 인식을 유발한다는 것입니다. 따라서 진단명 고지 시 환자와 가족의 정서적 반응을 고려하고, 치료 가능성과 회복 사례를 함께 설명하는 것이 필수적입니다.",
        "meaningVi": "Bệnh tâm thần nặng đặc trưng bởi rối loạn nhận thức, ảo giác, hoang tưởng, ngôn ngữ và hành vi rối loạn. Đây là bệnh mạn tính cần điều trị dài hạn bằng thuốc và liệu pháp tâm lý xã hội, nhưng có thể kiểm soát tốt nếu tuân thủ điều trị.",
        "context": "정신건강의학과, 재활치료, 사회복지, 법의학",
        "culturalNote": "한국에서는 조현병에 대한 인식이 점차 개선되고 있으며, 지역사회 정신건강복지센터를 통한 재활 프로그램과 취업 지원이 활성화되어 있습니다. 반면 베트남에서는 tâm thần phân liệt 환자에 대한 낙인이 매우 강하며, 가족들이 환자를 집에 감금하거나 무속인에게 치료를 의뢰하는 경우가 여전히 많습니다. 통역 시 한국의 항정신병 약물 치료, 재활 프로그램, 지역사회 통합 모델을 설명할 때 베트남 가족이 '치료 불가능한 병'으로 절망하지 않도록 회복 가능성을 강조하고, 약물 부작용 관리와 재발 방지의 중요성을 충분히 전달해야 합니다.",
        "commonMistakes": [
            {
                "mistake": "Tâm thần를 모든 정신질환에 사용",
                "correction": "Tâm thần phân liệt는 조현병, 우울증은 trầm cảm, 불안장애는 rối loạn lo âu",
                "explanation": "Tâm thần은 베트남어에서 '정신병'을 의미하며 중증 정신질환에 한정되므로, 경증 질환과 혼동 방지 필요"
            },
            {
                "mistake": "Phân liệt를 '인격 분열'로 이해",
                "correction": "조현병은 사고와 감정의 부조화이지 다중인격이 아님",
                "explanation": "Phân liệt(분열)이라는 용어가 해리성정체감장애(rối loạn nhân cách phân liệt)와 혼동될 수 있어 증상 설명 시 명확한 구분 필요"
            },
            {
                "mistake": "Điên(미침)을 tâm thần phân liệt와 동일시",
                "correction": "Điên은 비하적 표현, 의학 용어는 tâm thần phân liệt",
                "explanation": "Điên은 속어이며 환자와 가족에게 모욕적이므로 의료 통역에서 절대 사용 금지"
            }
        ],
        "examples": [
            {
                "ko": "조현병 진단을 받았지만 약물 치료로 증상이 잘 조절되고 있습니다.",
                "vi": "Tôi được chẩn đoán tâm thần phân liệt nhưng triệu chứng được kiểm soát tốt nhờ điều trị bằng thuốc.",
                "situation": "informal"
            },
            {
                "ko": "환자는 환청과 피해망상을 호소하며 조현병 급성기로 판단됩니다.",
                "vi": "Bệnh nhân than phiền về ảo thanh và hoang tưởng bị hại, được đánh giá là giai đoạn cấp của tâm thần phân liệt.",
                "situation": "formal"
            },
            {
                "ko": "항정신병 약물을 규칙적으로 복용하면 재발을 예방할 수 있습니다.",
                "vi": "Uống thuốc chống loạn thần đều đặn có thể phòng ngừa tái phát.",
                "situation": "formal"
            }
        ],
        "relatedTerms": ["망상", "환각", "항정신병약물", "정신재활"]
    },
    {
        "slug": "roi-loan-luong-cuc",
        "korean": "양극성장애",
        "vietnamese": "Rối loạn lưỡng cực",
        "hanja": "兩極性障碍",
        "hanjaReading": "兩(두 량) 極(다할 극) 性(성품 성) 障(막을 장) 碍(거릴 애)",
        "pronunciation": "조이 로안 르엉 꾹",
        "meaningKo": "조증 삽화와 우울증 삽화가 반복적으로 나타나는 기분장애로, 베트Nam어로는 'Rối loạn lưỡng cực' 또는 'Rối loạn hai cực'으로 표현합니다. 통역 시 주의할 점은 한국에서는 '양극성장애'라는 중립적 명칭을 사용하지만, 베트남에서는 과거 명칭인 'bệnh hưng cảm'(조울병)이 여전히 많이 사용되어 혼란을 줄 수 있다는 것입니다. 또한 '조증'과 '경조증'의 차이, 제1형과 제2형 양극성장애의 구분을 정확히 통역해야 치료 계획과 예후 설명이 가능합니다. 특히 조증 삽화 시 나타나는 과도한 에너지, 수면 욕구 감소, 충동적 행동 등을 설명할 때 문화적 맥락을 고려한 구체적 예시가 필요합니다.",
        "meaningVi": "Rối loạn tâm trạng đặc trưng bởi sự luân phiên giữa giai đoạn hưng cảm (hưng phấn quá mức) và trầm cảm. Chia thành type I (có cơn hưng cảm nặng) và type II (chỉ có nhẹ cảm - hypomanie). Cần điều trị bằng thuốc ổn định tâm trạng suốt đời.",
        "context": "정신건강의학과, 심리상담, 약물치료, 응급의학",
        "culturalNote": "한국에서는 양극성장애를 기분장애의 일종으로 이해하며, 기분 안정제(리튬, 항경련제 등)를 통한 장기 치료의 중요성이 널리 알려져 있습니다. 반면 베트남에서는 조증 삽화를 '기분이 좋은 상태'로 오해하거나, 우울 삽화만 치료하면 된다고 생각하는 경우가 많습니다. 통역 시 양극성장애가 '양쪽 극단을 오가는' 질환임을 강조하고, 조증이 단순히 기분 좋은 상태가 아니라 판단력 손상, 충동적 소비, 위험한 행동으로 이어질 수 있음을 명확히 설명해야 합니다. 또한 한국의 리튬 혈중농도 모니터링 시스템을 설명할 때 베트남에서는 이러한 체계가 부족할 수 있음을 고려해야 합니다.",
        "commonMistakes": [
            {
                "mistake": "Hưng cảm(조증)을 vui vẻ(기쁨)로 번역",
                "correction": "조증은 병적 흥분 상태, 단순 기쁨이 아님",
                "explanation": "Hưng cảm은 비정상적으로 고양된 기분으로 판단력 손상과 위험 행동을 동반하므로, vui(행복함)와 구분 필요"
            },
            {
                "mistake": "Rối loạn lưỡng cực을 우울증(trầm cảm)과 동일시",
                "correction": "양극성장애는 조증과 우울증 모두 포함, 단순 우울증과 다름",
                "explanation": "양극성장애는 조증 삽화가 핵심 진단 기준이며, 치료 약물도 우울증과 다르므로(기분안정제 필수) 명확한 구분 필요"
            },
            {
                "mistake": "Nhẹ cảm(경조증)을 심각하지 않은 것으로 번역",
                "correction": "Hypomanie(nhẹ cảm)도 치료 필요한 병적 상태",
                "explanation": "경조증이 '가벼운' 것으로 오해되어 치료를 소홀히 하면 제2형 양극성장애 진단을 놓칠 수 있음"
            }
        ],
        "examples": [
            {
                "ko": "양극성장애 환자는 조증기에 수면 없이 며칠을 지낼 수 있습니다.",
                "vi": "Bệnh nhân rối loạn lưỡng cực có thể không ngủ trong nhiều ngày ở giai đoạn hưng cảm.",
                "situation": "formal"
            },
            {
                "ko": "기분이 너무 좋아서 카드로 2천만 원어치 물건을 샀는데 문제인가요?",
                "vi": "Tôi cảm thấy quá hứng khởi nên đã mua đồ bằng thẻ tín dụng trị giá 500 triệu đồng, có vấn đề gì không?",
                "situation": "informal"
            },
            {
                "ko": "양극성장애 치료에는 리튬 같은 기분 안정제가 필수입니다.",
                "vi": "Điều trị rối loạn lưỡng cực cần thuốc ổn định tâm trạng như lithium.",
                "situation": "formal"
            }
        ],
        "relatedTerms": ["조증", "우울증", "기분안정제", "경조증"]
    },
    {
        "slug": "tu-van-tam-ly",
        "korean": "심리상담",
        "vietnamese": "Tư vấn tâm lý",
        "hanja": "心理相談",
        "hanjaReading": "心(마음 심) 理(다스릴 리) 相(서로 상) 談(말씀 담)",
        "pronunciation": "뜨 번 땀 리",
        "meaningKo": "정신적 어려움이나 심리적 문제를 전문가와의 대화를 통해 해결하는 과정으로, 베트남어로는 'Tư vấn tâm lý' 또는 'Tư vấn tâm lý học'으로 표현합니다. 통역 시 주의할 점은 한국에서 '심리상담'은 임상심리사, 상담심리사 등 전문 자격을 가진 인력이 제공하는 전문 서비스로 인식되지만, 베트남에서는 tư vấn(상담)이 일반적인 '조언'과 혼동될 수 있어 전문성을 강조하는 표현이 필요합니다. 또한 한국의 상담 유형(개인상담, 가족상담, 집단상담 등)과 접근법(인지행동치료, 정신역동치료 등)을 설명할 때 베트남어로 정확히 구분하여 통역해야 합니다.",
        "meaningVi": "Quá trình làm việc với chuyên gia tâm lý để giải quyết các vấn đề tinh thần, cảm xúc hoặc hành vi. Khác với tư vấn thông thường, tư vấn tâm lý được thực hiện bởi nhà tâm lý lâm sàng hoặc chuyên gia tư vấn có chứng chỉ chuyên môn.",
        "context": "정신건강의학과, 상담센터, 학교, 기업 복지",
        "culturalNote": "한국에서는 심리상담이 대중화되어 있으며, 직장인 EAP(Employee Assistance Program), 학교 Wee센터, 청소년상담복지센터 등 다양한 경로로 접근 가능합니다. 심리상담을 받는 것에 대한 사회적 낙인도 많이 감소했습니다. 반면 베트남에서는 심리상담이 아직 생소하며, '정신병자'만 가는 곳이라는 인식이 강해 상담 접근성이 매우 낮습니다. 통역 시 한국의 예방적 상담, 성장 상담 개념을 설명할 때 '문제가 있는 사람'만 받는 것이 아니라 '누구나 받을 수 있는' 서비스임을 강조해야 합니다. 또한 상담 비밀보장 원칙을 명확히 설명하여 베트남 내담자가 안심하고 상담받을 수 있도록 해야 합니다.",
        "commonMistakes": [
            {
                "mistake": "Tư vấn를 일반적인 '조언'으로 이해",
                "correction": "Tư vấn tâm lý는 전문가의 심리치료적 개입, 일반 조언은 khuyên bảo",
                "explanation": "심리상담의 전문성을 강조하지 않으면 베트남 내담자가 '친구와 대화하는 것'과 동일시할 수 있음"
            },
            {
                "mistake": "상담을 khám tâm thần(정신과 진찰)과 혼동",
                "correction": "상담은 tư vấn, 정신과 진료는 khám bệnh tâm thần - 약물 치료 유무 차이",
                "explanation": "심리상담은 비약물적 개입이며 정신과 진료와 다름을 명확히 해야 내담자가 불필요한 두려움을 갖지 않음"
            },
            {
                "mistake": "모든 심리 전문가를 bác sĩ tâm lý(심리 의사)로 호칭",
                "correction": "의사는 bác sĩ, 심리사는 nhà tâm lý học, 상담사는 chuyên viên tư vấn",
                "explanation": "한국의 정신과 의사, 임상심리사, 상담심리사 자격 차이를 베트남어로 정확히 구분해야 역할과 권한 오해 방지"
            }
        ],
        "examples": [
            {
                "ko": "우울감이 심해서 심리상담을 받아보려고 합니다.",
                "vi": "Tôi cảm thấy trầm cảm nặng nên muốn thử tư vấn tâm lý.",
                "situation": "informal"
            },
            {
                "ko": "환자에게 주 1회 개인 심리상담과 월 2회 집단상담을 권장합니다.",
                "vi": "Chúng tôi khuyến nghị bệnh nhân tham gia tư vấn cá nhân 1 lần/tuần và tư vấn nhóm 2 lần/tháng.",
                "situation": "formal"
            },
            {
                "ko": "심리상담 내용은 법적으로 비밀이 보장됩니다.",
                "vi": "Nội dung tư vấn tâm lý được bảo mật theo quy định pháp luật.",
                "situation": "formal"
            }
        ],
        "relatedTerms": ["임상심리사", "인지행동치료", "가족상담", "집단상담"]
    },
    {
        "slug": "lieu-phap-nhan-thuc-hanh-vi",
        "korean": "인지행동치료",
        "vietnamese": "Liệu pháp nhận thức hành vi",
        "hanja": "認知行動治療",
        "hanjaReading": "認(알 인) 知(알 지) 行(다닐 행) 動(움직일 동) 治(다스릴 치) 療(고칠 료)",
        "pronunciation": "리에우 팝 년 툭 한 비",
        "meaningKo": "왜곡된 인지(생각)를 교정하고 부적응적 행동을 변화시켜 정서적 문제를 해결하는 심리치료 기법으로, 베트남어로는 'Liệu pháp nhận thức hành vi' 또는 약어 'CBT'로 표현합니다. 통역 시 중요한 점은 한국에서 인지행동치료는 우울증, 불안장애, 강박장애 등의 표준 치료로 자리잡았으며, 구조화된 프로그램(12~16회기)으로 진행되지만, 베트남에서는 아직 도입 초기 단계로 일반인에게 생소하다는 것입니다. 따라서 '생각-감정-행동'의 연결고리, 자동적 사고 포착, 인지 왜곡 수정 등 CBT의 핵심 개념을 구체적 예시와 함께 설명해야 합니다.",
        "meaningVi": "Phương pháp trị liệu tâm lý tập trung vào việc nhận diện và thay đổi các suy nghĩ méo mó (nhận thức sai lệch) cùng hành vi không phù hợp để cải thiện tình trạng cảm xúc. CBT là liệu pháp có bằng chứng khoa học cho nhiều rối loạn tâm lý như trầm cảm, lo âu, rối loạn ám ảnh cưỡng bức.",
        "context": "심리상담, 정신건강의학과, 행동치료, 임상심리",
        "culturalNote": "한국에서는 인지행동치료가 보험 적용을 받는 표준 치료법이며, 온라인 CBT 프로그램, 자가 치료 워크북 등 다양한 형태로 제공됩니다. 많은 내담자가 'CBT'라는 약어를 알고 있으며, 숙제(과제) 수행의 중요성도 이해하고 있습니다. 반면 베트남에서는 심리치료 자체가 생소하며, 특히 '생각을 바꾸면 감정이 바뀐다'는 CBT의 핵심 원리가 문화적으로 낯설게 느껴질 수 있습니다. 통역 시 한국의 구조화된 CBT 프로그램(매주 과제, 사고 기록지 작성 등)을 설명할 때, 베트남 내담자가 '공부'나 '시험'으로 오해하지 않도록 치료적 의미를 강조하고, 구체적인 일상 예시를 들어 이해를 돕는 것이 중요합니다.",
        "commonMistakes": [
            {
                "mistake": "Nhận thức를 단순 '지식'으로 이해",
                "correction": "Nhận thức(인지)는 사고 과정과 신념 체계, 지식은 kiến thức",
                "explanation": "CBT의 nhận thức는 '어떻게 생각하는가'의 과정이므로, 정보나 지식과 구분하여 설명 필요"
            },
            {
                "mistake": "Liệu pháp를 điều trị bằng thuốc(약물치료)로 오해",
                "correction": "Liệu pháp는 치료법 일반, 약물치료는 điều trị bằng thuốc",
                "explanation": "CBT는 비약물 심리치료이므로 베트남 환자가 '약 처방'을 기대하지 않도록 명확히 구분"
            },
            {
                "mistake": "CBT를 단순 '긍정적 사고'로 번역",
                "correction": "CBT는 왜곡 인지 교정, 무조건 긍정이 아님 - suy nghĩ tích cực과 다름",
                "explanation": "CBT는 현실적이고 균형 잡힌 사고를 목표로 하며, 무조건 긍정적으로 생각하라는 것이 아님을 설명 필요"
            }
        ],
        "examples": [
            {
                "ko": "불안장애 치료를 위해 12회기 인지행동치료를 시작하겠습니다.",
                "vi": "Chúng tôi sẽ bắt đầu liệu pháp nhận thức hành vi 12 buổi để điều trị rối loạn lo âu.",
                "situation": "formal"
            },
            {
                "ko": "매주 상담 후 받은 과제를 꼭 해오셔야 효과가 있습니다.",
                "vi": "Bạn phải hoàn thành bài tập được giao sau mỗi buổi tư vấn thì mới có hiệu quả.",
                "situation": "informal"
            },
            {
                "ko": "자동적 사고를 기록하고 그것이 왜곡된 인지인지 평가합니다.",
                "vi": "Ghi lại các suy nghĩ tự động và đánh giá xem đó có phải là nhận thức méo mó hay không.",
                "situation": "formal"
            }
        ],
        "relatedTerms": ["심리상담", "인지왜곡", "자동적사고", "행동수정"]
    },
    {
        "slug": "giam-dinh-tam-than",
        "korean": "정신감정",
        "vietnamese": "Giám định tâm thần",
        "hanja": "精神鑑定",
        "hanjaReading": "精(정수 정) 神(귀신 신) 鑑(거울 감) 定(정할 정)",
        "pronunciation": "잠 딘 땀 틴",
        "meaningKo": "법적 절차에서 피의자, 피고인 또는 당사자의 정신 상태를 의학적으로 평가하는 전문가 감정으로, 베트남어로는 'Giám định tâm thần' 또는 'Giám định pháp y tâm thần'(법의정신감정)으로 표현합니다. 통역 시 매우 중요한 점은 한국에서 정신감정은 형사책임능력, 치료감호 필요성, 민사 행위능력 등을 판단하는 법적 효력이 있는 의학적 문서이며, 정신과 전문의나 정신감정 전문의가 수행한다는 것입니다. 베트남에서도 유사한 제도가 있지만, 감정 절차와 기준이 다를 수 있어 한국의 정신감정 결과를 설명할 때 법적 맥락을 명확히 전달해야 합니다.",
        "meaningVi": "Đánh giá chuyên môn về tình trạng tâm thần của bị can, bị cáo hoặc đương sự trong các thủ tục pháp lý, nhằm xác định năng lực chịu trách nhiệm hình sự, năng lực hành vi dân sự, hoặc nhu cầu điều trị bắt buộc. Được thực hiện bởi bác sĩ tâm thần có chứng chỉ giám định pháp y.",
        "context": "법의학, 형사소송, 민사소송, 치료감호",
        "culturalNote": "한국에서는 정신감정이 형사재판에서 중요한 증거로 작용하며, 심신상실·심신미약 판단, 치료감호 결정 등에 핵심적 역할을 합니다. 정신감정 절차는 법원 또는 검찰의 촉탁으로 이루어지며, 국립법무병원, 대학병원 등 전문기관에서 수행됩니다. 반면 베트남에서도 형사소송법상 giám định tâm thần 제도가 있으나, 전문 인력과 시설이 부족하여 활용도가 낮고, 감정 결과에 대한 법원의 신뢰도도 한국보다 낮은 편입니다. 통역 시 한국의 정신감정 결과를 베트남 법률 관계자에게 설명할 때, 감정 방법(임상 면담, 심리검사, 뇌영상 등)과 진단 기준(DSM-5, ICD-11)을 구체적으로 제시하여 신뢰성을 높여야 합니다.",
        "commonMistakes": [
            {
                "mistake": "Giám định를 일반 진단(chẩn đoán)과 혼용",
                "correction": "Giám định은 법적 감정, 일반 진단은 chẩn đoán y khoa",
                "explanation": "정신감정은 법적 목적의 전문가 의견이며 일반 진료와 절차, 효력이 다르므로 명확한 구분 필요"
            },
            {
                "mistake": "Tâm thần를 '정신병'으로만 한정",
                "correction": "정신감정은 정신질환뿐 아니라 정신지체, 치매 등도 포함",
                "explanation": "Giám định tâm thần은 모든 정신 상태 평가를 포함하므로 질환 유무와 무관하게 실시될 수 있음"
            },
            {
                "mistake": "심신미약을 '정신병이 조금 있음'으로 번역",
                "correction": "심신미약은 suy giảm năng lực nhận thức và điều khiển hành vi(인지·통제 능력 감소)",
                "explanation": "한국 형법상 심신미약은 법적 개념이므로 의학적 질병 유무가 아닌 책임능력 정도로 설명 필요"
            }
        ],
        "examples": [
            {
                "ko": "피고인에 대한 정신감정 결과 심신미약 상태로 판단됩니다.",
                "vi": "Kết quả giám định tâm thần cho thấy bị cáo ở tình trạng suy giảm năng lực nhận thức và điều khiển hành vi.",
                "situation": "formal"
            },
            {
                "ko": "법원에서 정신감정을 요청했는데 어떤 절차로 진행되나요?",
                "vi": "Tòa án đã yêu cầu giám định tâm thần, quy trình sẽ diễn ra như thế nào?",
                "situation": "informal"
            },
            {
                "ko": "정신감정서에 따르면 범행 당시 조현병 급성기로 현실 판단 능력이 없었습니다.",
                "vi": "Theo bản giám định tâm thần, tại thời điểm phạm tội, bị cáo đang ở giai đoạn cấp của tâm thần phân liệt và không có năng lực nhận thức thực tế.",
                "situation": "formal"
            }
        ],
        "relatedTerms": ["심신상실", "심신미약", "치료감호", "책임능력"]
    },
    {
        "slug": "phong-chong-tu-tu",
        "korean": "자살예방",
        "vietnamese": "Phòng chống tự tử",
        "hanja": "自殺豫防",
        "hanjaReading": "自(스스로 자) 殺(죽일 살) 豫(미리 예) 防(막을 방)",
        "pronunciation": "퐁 쫑 뜨 뜨",
        "meaningKo": "자살 위험이 있는 개인을 조기에 발견하고 개입하여 자살 시도 및 자살 사망을 막기 위한 포괄적 활동으로, 베트남어로는 'Phòng chống tự tử' 또는 'Phòng ngừa tự tử'로 표현합니다. 통역 시 주의할 점은 한국에서 자살예방은 국가 정책(자살예방법, 자살예방센터 등)으로 체계화되어 있으며, 자살 위험 평가 도구(PHQ-9, 자살사고 척도 등), 게이트키퍼 교육, 생명지킴이 양성 등 다층적 접근이 이루어지지만, 베트남에서는 아직 제도적 기반이 약하고 자살을 '금기'로 여겨 공개적 논의가 어렵다는 것입니다. 따라서 자살 위험 신호, 개입 방법, 위기상담 전화(한국 1393, 베트남 1800-599-999) 등을 설명할 때 문화적 민감성을 가지고 접근해야 합니다.",
        "meaningVi": "Các hoạt động toàn diện nhằm phát hiện sớm và can thiệp đối với những người có nguy cơ tự tử, ngăn chặn hành vi tự sát và tử vong do tự tử. Bao gồm đánh giá nguy cơ, tư vấn khủng hoảng, theo dõi sau xuất viện, và nâng cao nhận thức cộng đồng.",
        "context": "정신건강의학과, 응급의학, 위기상담, 공중보건",
        "culturalNote": "한국은 OECD 국가 중 자살률이 높아 자살예방이 국가적 과제로 인식되며, 정신건강복지센터, 자살예방센터, 생명의전화 등 다양한 지원 체계가 구축되어 있습니다. 학교, 직장, 군대 등에서 게이트키퍼 교육이 활발하며, 자살 시도자에 대한 사후관리(자살시도자 사례관리)도 체계적입니다. 반면 베트남에서는 자살이 종교적·문화적으로 금기시되어 공개적 논의가 어렵고, 자살 시도자가 가족에게 숨기거나 병원 방문을 꺼리는 경우가 많습니다. 통역 시 한국의 자살예방 프로그램을 설명할 때 '자살은 예방 가능한 공중보건 문제'라는 인식을 강조하고, 베트남 환자나 가족이 수치심 없이 도움을 요청할 수 있도록 비밀보장과 비판단적 태도를 명확히 전달해야 합니다.",
        "commonMistakes": [
            {
                "mistake": "Tự tử를 tự sát와 혼용하여 사용",
                "correction": "의학·공중보건 용어로는 tự tử, 법률·형사 용어로는 tự sát",
                "explanation": "Tự tử는 중립적 의학 용어, tự sát는 법적 용어로 맥락에 따라 구분 사용 필요"
            },
            {
                "mistake": "자살예방을 단순히 '말리기'(ngăn cản)로 번역",
                "correction": "예방은 phòng chống(체계적 예방), 단순 제지는 ngăn cản",
                "explanation": "자살예방은 위험 요인 감소, 보호 요인 강화 등 포괄적 접근이므로 일시적 제지와 구분 필요"
            },
            {
                "mistake": "자살 사고를 ý định tự tử(자살 의도)로만 번역",
                "correction": "자살 사고는 suy nghĩ tự tử(생각), 의도는 ý định, 계획은 kế hoạch",
                "explanation": "한국의 자살 위험 평가는 사고-의도-계획-수단을 단계적으로 평가하므로 각 개념을 정확히 구분 필요"
            }
        ],
        "examples": [
            {
                "ko": "자살 생각이 자주 드시나요? 구체적인 계획을 세운 적이 있나요?",
                "vi": "Anh/chị có thường xuyên có suy nghĩ tự tử không? Đã từng lên kế hoạch cụ thể chưa?",
                "situation": "formal"
            },
            {
                "ko": "죽고 싶다는 생각이 계속 들어서 무서워요.",
                "vi": "Tôi cứ nghĩ đến việc chết và cảm thấy sợ hãi.",
                "situation": "informal"
            },
            {
                "ko": "자살 고위험군 환자는 퇴원 후 1주일 이내 추적 관리가 필수입니다.",
                "vi": "Bệnh nhân nhóm nguy cơ tự tử cao bắt buộc phải được theo dõi trong vòng 1 tuần sau xuất viện.",
                "situation": "formal"
            }
        ],
        "relatedTerms": ["우울증", "자살사고", "위기개입", "응급입원"]
    }
]

def main():
    print("=" * 60)
    print("정신건강/중독/상담 분야 의료 전문용어 추가 스크립트")
    print("Mental Health/Addiction/Counseling Terms Addition (v6-ff)")
    print("=" * 60)

    # 1. 파일 존재 확인
    if not os.path.exists(file_path):
        print(f"❌ 오류: 파일을 찾을 수 없습니다: {file_path}")
        return

    # 2. 기존 데이터 로드
    print(f"\n📂 파일 로드 중: {file_path}")
    with open(file_path, 'r', encoding='utf-8') as f:
        data = json.load(f)

    print(f"✅ 기존 용어 수: {len(data)}개")

    # 3. 중복 확인 (slug 기준)
    existing_slugs = {term['slug'] for term in data}
    duplicates = []
    new_terms_filtered = []

    for term in new_terms:
        if term['slug'] in existing_slugs:
            duplicates.append(term['slug'])
        else:
            new_terms_filtered.append(term)

    if duplicates:
        print(f"\n⚠️  중복 발견 ({len(duplicates)}개): {', '.join(duplicates)}")
        print("   중복 용어는 건너뜁니다.")

    if not new_terms_filtered:
        print("\n❌ 추가할 새 용어가 없습니다 (모두 중복)")
        return

    # 4. 새 용어 추가
    print(f"\n➕ 새 용어 추가 중: {len(new_terms_filtered)}개")
    for term in new_terms_filtered:
        print(f"   - {term['korean']} ({term['vietnamese']})")
        data.append(term)

    # 5. 파일 저장 (들여쓰기 2칸, 유니코드 그대로, 후행 줄바꿈 추가)
    print(f"\n💾 파일 저장 중...")
    with open(file_path, 'w', encoding='utf-8') as f:
        json.dump(data, f, ensure_ascii=False, indent=2)
        f.write('\n')  # 파일 끝에 줄바꿈 추가

    print(f"✅ 저장 완료!")
    print(f"\n📊 최종 용어 수: {len(data)}개 (기존 {len(data) - len(new_terms_filtered)}개 + 신규 {len(new_terms_filtered)}개)")
    print("\n" + "=" * 60)
    print("✨ 작업 완료!")
    print("=" * 60)

if __name__ == "__main__":
    main()
