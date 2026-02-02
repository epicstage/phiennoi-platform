#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
의료 분야 전문용어 추가 스크립트 (20개)
- 한방/정신건강/성형/의료시스템 분야
- Tier S 품질 기준 충족 (90점 이상)
"""

import json
import os
from typing import List, Dict, Any

# PATH CODE (MUST USE)
file_path = os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', 'data', 'terms', 'medical.json')
with open(file_path, 'r', encoding='utf-8') as f:
    data = json.load(f)  # data is a LIST, not dict
existing_slugs = {t['slug'] for t in data}

# 신규 용어 20개 (Tier S 품질)
new_terms: List[Dict[str, Any]] = [
    {
        "slug": "cham-cuu",
        "korean": "침술",
        "vietnamese": "Châm cứu",
        "hanja": "鍼術",
        "hanjaReading": "鍼(바늘 침) + 術(재주 술)",
        "pronunciation": "짬꾸",
        "meaningKo": "한의학에서 가느다란 침을 경혈(經穴)에 찔러 넣어 자극함으로써 질병을 치료하는 방법. 통역 시 주의할 점은 베트남에서도 동양의학이 발달했지만 한국 침술과 치료 부위나 기법이 다를 수 있다는 점이다. '경혈'은 huyệt đạo, '자침'은 châm kim으로 구분해서 통역해야 한다. 시술자의 자격(한의사/침구사)도 명확히 전달해야 오해가 없다.",
        "meaningVi": "Phương pháp điều trị bệnh trong y học cổ truyền bằng cách dùng kim nhỏ đâm vào các huyệt đạo để kích thích cơ thể. Châm cứu có nguồn gốc từ Trung Quốc và được phát triển độc lập tại Việt Nam với một số kỹ thuật và huyệt vị khác nhau so với Hàn Quốc.",
        "context": "한방병원, 한의원 진료 설명",
        "culturalNote": "한국에서는 침술이 건강보험 적용 대상이지만 베트남에서는 전통 의료로 분류되어 보험 적용이 제한적이다. 한국 한의사는 6년 교육 과정을 이수하지만 베트남 y sĩ đông y는 교육 체계가 다르므로 자격 비교 시 주의가 필요하다.",
        "commonMistakes": [
            {
                "mistake": "침술을 그냥 'châm'으로만 표현",
                "correction": "châm cứu (침구 전체) 또는 châm kim (침 시술만)",
                "explanation": "'châm'만 쓰면 주사와 혼동될 수 있음"
            },
            {
                "mistake": "경혈을 'điểm châm'으로 번역",
                "correction": "huyệt đạo 또는 huyệt vị",
                "explanation": "전문 용어로서 정확성 유지 필요"
            },
            {
                "mistake": "한의사를 'bác sĩ châm cứu'로 표현",
                "correction": "bác sĩ y học cổ truyền 또는 thầy thuốc đông y",
                "explanation": "한의사는 침술만 하는 것이 아니므로 범위가 좁음"
            }
        ],
        "examples": [
            {
                "ko": "허리 통증에는 침술 치료가 효과적입니다.",
                "vi": "Châm cứu rất hiệu quả trong điều trị đau lưng.",
                "situation": "formal"
            },
            {
                "ko": "오늘 침 맞으러 가야 해요.",
                "vi": "Hôm nay tôi phải đi châm cứu.",
                "situation": "informal"
            },
            {
                "ko": "침술 시술 전에 환자의 체질을 먼저 확인합니다.",
                "vi": "Trước khi châm cứu, cần kiểm tra thể chất của bệnh nhân.",
                "situation": "onsite"
            }
        ],
        "relatedTerms": ["뜸치료", "한약", "추나요법", "경혈", "한의원"]
    },
    {
        "slug": "cuu-ngai",
        "korean": "뜸치료",
        "vietnamese": "Cứu ngải",
        "hanja": None,
        "hanjaReading": None,
        "pronunciation": "꾸우 응아이",
        "meaningKo": "쑥 등의 약재를 태워 그 열기로 경혈이나 환부를 자극하여 질병을 치료하는 한의학 요법. 통역 시 주의할 점은 '뜸'과 'moxibustion'을 구분하고, 직접구(da trực tiếp)와 간접구(da gián tiếp)의 차이를 명확히 설명해야 한다는 것이다. 화상 위험성과 금기 사항도 반드시 전달해야 환자 안전을 지킬 수 있다.",
        "meaningVi": "Phương pháp điều trị bằng cách đốt ngải cứu (hoặc các loại thảo dược khác) để kích thích huyệt đạo bằng nhiệt. Có hai loại chính: cứu trực tiếp (đặt ngải trực tiếp lên da) và cứu gián tiếp (có lớp đệm như gừng, tỏi). Phương pháp này giúp cải thiện tuần hoàn máu và giảm đau.",
        "context": "한방 치료 설명, 물리치료 대안",
        "culturalNote": "한국에서는 뜸치료가 노인층에게 익숙하고 가정에서도 자주 시행되지만, 베트남에서는 전문 시술자를 통해서만 받는 경우가 많다. 베트남 전통 뜸은 쑥 대신 다른 약초를 쓰기도 하며 시술 방식에 차이가 있다.",
        "commonMistakes": [
            {
                "mistake": "뜸을 'đốt cứu'로만 표현",
                "correction": "cứu ngải (정확한 전문 용어)",
                "explanation": "'đốt'는 일반적인 '태우다'는 의미로 비전문적"
            },
            {
                "mistake": "직접구/간접구 구분 없이 통역",
                "correction": "cứu trực tiếp / cứu gián tiếp 명시",
                "explanation": "환자 안전과 시술 방법 이해를 위해 필수"
            },
            {
                "mistake": "화상 위험을 'cháy da'로 표현",
                "correction": "nguy cơ bỏng da",
                "explanation": "'cháy'는 너무 과격한 표현, 'bỏng'이 의료 용어"
            }
        ],
        "examples": [
            {
                "ko": "무릎 관절염에는 뜸치료를 권장합니다.",
                "vi": "Với viêm khớp gối, tôi khuyên nên thử cứu ngải.",
                "situation": "formal"
            },
            {
                "ko": "뜸 뜨면 몸이 따뜻해져요.",
                "vi": "Khi được cứu, cơ thể sẽ ấm lên.",
                "situation": "informal"
            },
            {
                "ko": "간접구 방식으로 시술하겠습니다.",
                "vi": "Tôi sẽ thực hiện bằng phương pháp cứu gián tiếp.",
                "situation": "onsite"
            }
        ],
        "relatedTerms": ["침술", "한약", "경혈", "물리치료", "한방병원"]
    },
    {
        "slug": "thuoc-dong-y",
        "korean": "한약",
        "vietnamese": "Thuốc đông y",
        "hanja": "韓藥",
        "hanjaReading": "韓(나라 한) + 藥(약 약)",
        "pronunciation": "투억 동이",
        "meaningKo": "한의학 이론에 따라 처방되는 약재로, 주로 식물, 동물, 광물 등 자연물을 원료로 한다. 통역 시 주의할 점은 '탕약(thang dược)', '환약(hoEnvironn)', '산제(tán dược)'를 구분하고, 베트남 전통약(thuốc nam)과 혼동하지 않도록 명확히 전달해야 한다는 것이다. 복용법과 금기 사항도 정확히 통역해야 안전하다.",
        "meaningVi": "Thuốc được bào chế theo y học cổ truyền Hàn Quốc, chủ yếu từ nguyên liệu tự nhiên như thảo dược, động vật, khoáng chất. Khác với thuốc nam Việt Nam, thuốc đông y Hàn Quốc có hệ thống lý luận và bào chế riêng dựa trên âm dương, ngũ hành.",
        "context": "한의원 처방 설명, 약국 상담",
        "culturalNote": "한국에서는 한약이 건강보험 적용을 받지만 베트남에서는 전통약이 주로 자가 처방으로 이용된다. 한약재 중 일부는 베트남에서 구하기 어렵거나 금지된 것도 있으므로 처방 시 대체재를 고려해야 한다. 베트남 환자는 한약의 쓴맛에 익숙하지 않을 수 있다.",
        "commonMistakes": [
            {
                "mistake": "한약을 'thuốc Hàn Quốc'로 번역",
                "correction": "thuốc đông y (동양의학 약)",
                "explanation": "'thuốc Hàn Quốc'는 한국산 약품 전체를 의미해 범위가 넓음"
            },
            {
                "mistake": "탕약을 'nước thuốc'로만 표현",
                "correction": "thang dược 또는 thuốc sắc",
                "explanation": "전문 용어로 명확히 해야 혼동 방지"
            },
            {
                "mistake": "복용법을 '하루 3번'으로만 표현",
                "correction": "식전/식후, 온도, 보관법 포함",
                "explanation": "한약은 복용 시간과 온도가 효과에 영향"
            }
        ],
        "examples": [
            {
                "ko": "감기에는 이 한약을 하루 두 번 드세요.",
                "vi": "Với cảm cúm, hãy uống thuốc đông y này hai lần mỗi ngày.",
                "situation": "formal"
            },
            {
                "ko": "한약 지어왔어요.",
                "vi": "Tôi đã mua thuốc đông y về rồi.",
                "situation": "informal"
            },
            {
                "ko": "이 처방은 7일분 탕약입니다.",
                "vi": "Đơn này là thang dược cho 7 ngày.",
                "situation": "onsite"
            }
        ],
        "relatedTerms": ["침술", "한의원", "처방전", "탕약", "약재"]
    },
    {
        "slug": "nan-chinh-cot-song",
        "korean": "추나요법",
        "vietnamese": "Nắn chỉnh cột sống",
        "hanja": "推拿療法",
        "hanjaReading": "推(밀 추) + 拿(잡을 나) + 療(치료할 료) + 法(법 법)",
        "pronunciation": "넌 찐 껏송",
        "meaningKo": "한의학에서 손이나 신체 일부로 환자의 체표를 밀고, 누르고, 당기는 등의 물리적 자극을 가해 경락과 기혈을 조절하고 근골격계 질환을 치료하는 수기요법. 통역 시 주의할 점은 카이로프랙틱(chiropractic)과 구분하고, 시술 부위와 강도를 명확히 전달해야 한다는 것이다. 급성 디스크나 골절 환자에게는 금기일 수 있으므로 진단 결과를 함께 설명해야 안전하다.",
        "meaningVi": "Liệu pháp điều trị bằng tay trong y học cổ truyền, sử dụng các thao tác đẩy, ấn, kéo trên cơ thể để điều hòa kinh lạc, khí huyết và điều trị bệnh cơ xương khớp. Khác với chiropractic phương Tây, nắn chỉnh cột sống theo đông y kết hợp lý thuyết kinh lạc và huyệt đạo.",
        "context": "한방 물리치료, 척추 질환 치료",
        "culturalNote": "한국에서는 추나요법이 2019년부터 건강보험 적용을 받지만 베트nam에서는 전통 안마(massage truyền thống)와 혼동될 수 있다. 베트남 환자는 강한 압력의 시술에 익숙하지 않을 수 있으므로 강도 조절이 필요하다.",
        "commonMistakes": [
            {
                "mistake": "추나요법을 'massage'로 번역",
                "correction": "nắn chỉnh cột sống 또는 thủ pháp y học cổ truyền",
                "explanation": "일반 마사지와 구분되는 의료 행위"
            },
            {
                "mistake": "카이로프랙틱과 동일시",
                "correction": "두 가지의 차이점 명시 (경락 vs 신경계)",
                "explanation": "치료 원리와 접근법이 다름"
            },
            {
                "mistake": "금기 사항 설명 없이 권유",
                "correction": "골절, 골다공증, 급성 디스크 환자 제외 명시",
                "explanation": "환자 안전을 위해 필수"
            }
        ],
        "examples": [
            {
                "ko": "허리 디스크에는 추나요법이 도움이 됩니다.",
                "vi": "Với thoát vị đĩa đệm, liệu pháp nắn chỉnh cột sống rất có ích.",
                "situation": "formal"
            },
            {
                "ko": "추나 받으면 시원해요.",
                "vi": "Sau khi nắn chỉnh, cảm giác rất dễ chịu.",
                "situation": "informal"
            },
            {
                "ko": "골반 교정 추나를 시술하겠습니다.",
                "vi": "Tôi sẽ thực hiện thủ pháp nắn chỉnh điều chỉnh xương chậu.",
                "situation": "onsite"
            }
        ],
        "relatedTerms": ["물리치료", "척추", "디스크", "한방병원", "재활치료"]
    },
    {
        "slug": "tram-cam",
        "korean": "우울증",
        "vietnamese": "Trầm cảm",
        "hanja": "憂鬱症",
        "hanjaReading": "憂(근심 우) + 鬱(막힐 울) + 症(병 증)",
        "pronunciation": "쩜 깜",
        "meaningKo": "지속적인 슬픔, 무기력, 흥미 상실 등을 특징으로 하는 정신질환. 통역 시 주의할 점은 베트남에서 정신질환에 대한 사회적 편견이 강하므로 '우울감(buồn chán)'과 '우울증(trầm cảm)'을 명확히 구분하고, 치료 가능한 질병임을 강조해야 한다는 것이다. 자살 위험성 평가 시 직접적인 표현을 피하고 완곡하게 전달하는 것이 중요하다.",
        "meaningVi": "Bệnh lý tâm thần đặc trưng bởi buồn bã kéo dài, mất hứng thú, mệt mỏi và vô vọng. Trầm cảm không chỉ là tâm trạng buồn tạm thời mà là bệnh cần điều trị chuyên khoa. Có thể điều trị bằng thuốc, tâm lý trị liệu hoặc kết hợp.",
        "context": "정신건강의학과 진료, 상담",
        "culturalNote": "한국은 정신건강 서비스가 체계화되어 있고 사회적 인식도 개선되었지만, 베트남에서는 여전히 정신질환을 가족의 수치로 여기는 경향이 강하다. 베트남 환자는 신체 증상(두통, 소화불량)을 호소하며 정신과 진료를 꺼릴 수 있으므로 신뢰 관계 구축이 중요하다.",
        "commonMistakes": [
            {
                "mistake": "우울증을 'buồn'으로만 표현",
                "correction": "trầm cảm (의학적 진단명)",
                "explanation": "'buồn'은 일시적 감정, trầm cảm은 질환"
            },
            {
                "mistake": "자살 충동을 직접적으로 번역",
                "correction": "ý định tự gây hại bản thân (자해 의도)",
                "explanation": "문화적 민감성 고려 필요"
            },
            {
                "mistake": "약물 치료만 강조",
                "correction": "thuốc + tâm lý trị liệu (약물+심리치료) 병행 설명",
                "explanation": "종합적 치료 접근 필요"
            }
        ],
        "examples": [
            {
                "ko": "우울증은 치료 가능한 질병입니다.",
                "vi": "Trầm cảm là bệnh có thể điều trị được.",
                "situation": "formal"
            },
            {
                "ko": "요즘 우울해서 병원 갔어요.",
                "vi": "Dạo này tôi bị trầm cảm nên đã đi khám.",
                "situation": "informal"
            },
            {
                "ko": "항우울제 복용을 시작하겠습니다.",
                "vi": "Chúng ta sẽ bắt đầu dùng thuốc chống trầm cảm.",
                "situation": "onsite"
            }
        ],
        "relatedTerms": ["불안장애", "정신건강의학과", "상담치료", "항우울제", "인지행동치료"]
    },
    {
        "slug": "roi-loan-lo-au",
        "korean": "불안장애",
        "vietnamese": "Rối loạn lo âu",
        "hanja": "不安障碍",
        "hanjaReading": "不(아니 불) + 安(편안 안) + 障(막을 장) + 碍(막힐 애)",
        "pronunciation": "조이 로안 로 어우",
        "meaningKo": "과도하고 지속적인 걱정, 두려움, 긴장을 특징으로 하는 정신질환. 통역 시 주의할 점은 일반적인 걱정(lo lắng)과 병적 불안(lo âu bệnh lý)을 구분하고, 신체 증상(가슴 두근거림, 호흡곤란)도 함께 설명해야 환자가 이해하기 쉽다는 것이다. 공황장애, 사회불안장애 등 세부 유형도 정확히 구분해야 한다.",
        "meaningVi": "Nhóm rối loạn tâm thần đặc trưng bởi lo lắng, sợ hãi quá mức và kéo dài, ảnh hưởng đến sinh hoạt hàng ngày. Triệu chứng bao gồm căng thẳng, đánh trống ngực, khó thở, mất ngủ. Có nhiều loại như rối loạn lo âu lan tỏa, rối loạn lo âu xã hội, rối loạn hoảng sợ.",
        "context": "정신건강의학과 진단, 상담",
        "culturalNote": "한국에서는 불안장애 진단과 치료가 일반화되었지만, 베트남에서는 '마음이 약해서'로 치부되는 경우가 많다. 베트남 환자는 신체 증상을 강조하므로 내과를 먼저 방문하는 경향이 있어, 정신과 의뢰 시 세심한 설명이 필요하다.",
        "commonMistakes": [
            {
                "mistake": "불안을 'sợ hãi'로만 번역",
                "correction": "lo âu (의학 용어)",
                "explanation": "'sợ hãi'는 일시적 두려움, lo âu는 병적 상태"
            },
            {
                "mistake": "공황장애와 불안장애를 혼용",
                "correction": "rối loạn hoảng sợ vs rối loạn lo âu 구분",
                "explanation": "증상과 치료법이 다름"
            },
            {
                "mistake": "약물 의존성 우려를 무시",
                "correction": "환자의 우려를 인정하고 설명",
                "explanation": "베트남 환자는 약물 의존성을 매우 걱정함"
            }
        ],
        "examples": [
            {
                "ko": "불안장애는 심리치료로 많이 호전됩니다.",
                "vi": "Rối loạn lo âu có thể cải thiện nhiều nhờ tâm lý trị liệu.",
                "situation": "formal"
            },
            {
                "ko": "불안해서 잠을 못 자요.",
                "vi": "Tôi lo âu nên không ngủ được.",
                "situation": "informal"
            },
            {
                "ko": "범불안장애로 진단됩니다.",
                "vi": "Chẩn đoán là rối loạn lo âu lan tỏa (GAD).",
                "situation": "onsite"
            }
        ],
        "relatedTerms": ["공황장애", "우울증", "인지행동치료", "정신건강의학과", "항불안제"]
    },
    {
        "slug": "roi-loan-hoang-so",
        "korean": "공황장애",
        "vietnamese": "Rối loạn hoảng sợ",
        "hanja": "恐慌障碍",
        "hanjaReading": "恐(두려워할 공) + 慌(당황할 황) + 障(막을 장) + 碍(막힐 애)",
        "pronunciation": "조이 로안 호앙 쏘",
        "meaningKo": "갑작스럽고 강렬한 공포 발작이 반복적으로 나타나는 불안장애의 한 유형. 통역 시 주의할 점은 '공황발작(cơn hoảng sợ)'과 '공황장애(rối loạn hoảng sợ)'를 구분하고, 심장마비와 혼동할 수 있는 증상(가슴 통증, 호흡곤란)을 정확히 설명해야 환자가 안심할 수 있다는 것이다. 예기 불안도 함께 설명해야 완전한 이해가 가능하다.",
        "meaningVi": "Một dạng rối loạn lo âu đặc trưng bởi các cơn hoảng sợ đột ngột và dữ dội, kèm theo các triệu chứng như đau ngực, khó thở, chóng mặt, sợ chết. Bệnh nhân thường sợ cơn hoảng sợ tái phát (lo âu dự đoán) và tránh các tình huống có thể gây ra cơn.",
        "context": "응급실, 정신건강의학과",
        "culturalNote": "한국에서는 공황장애가 잘 알려져 있고 연예인들의 고백으로 인식이 개선되었지만, 베트남에서는 심장병으로 오인되는 경우가 많다. 베트남 환자는 공황발작을 '귀신 들림'으로 해석하기도 하므로 의학적 설명이 중요하다.",
        "commonMistakes": [
            {
                "mistake": "공황발작을 'sợ'로만 번역",
                "correction": "cơn hoảng sợ (패닉 어택)",
                "explanation": "갑작스런 발작 증상 강조 필요"
            },
            {
                "mistake": "심장병과 구분 안 함",
                "correction": "심장 검사 정상, 심리적 원인 설명",
                "explanation": "환자의 가장 큰 우려 해소 필요"
            },
            {
                "mistake": "예기 불안을 설명 안 함",
                "correction": "lo âu dự đoán (anticipatory anxiety) 포함",
                "explanation": "공황장애의 핵심 특징"
            }
        ],
        "examples": [
            {
                "ko": "공황장애는 약물과 인지행동치료로 치료합니다.",
                "vi": "Rối loạn hoảng sợ được điều trị bằng thuốc và liệu pháp nhận thức hành vi.",
                "situation": "formal"
            },
            {
                "ko": "지하철에서 공황발작이 왔어요.",
                "vi": "Tôi bị cơn hoảng sợ trên tàu điện ngầm.",
                "situation": "informal"
            },
            {
                "ko": "호흡법 훈련을 시작하겠습니다.",
                "vi": "Chúng ta sẽ bắt đầu luyện tập kỹ thuật hô hấp.",
                "situation": "onsite"
            }
        ],
        "relatedTerms": ["불안장애", "공황발작", "인지행동치료", "호흡법", "예기불안"]
    },
    {
        "slug": "roi-loan-stress-sau-sang-chan",
        "korean": "외상후스트레스장애",
        "vietnamese": "Rối loạn stress sau sang chấn",
        "hanja": "外傷後stress障碍",
        "hanjaReading": "外(밖 외) + 傷(상처 상) + 後(뒤 후)",
        "pronunciation": "조이 로안 스트렛 서우 상 쩐",
        "meaningKo": "충격적인 사건을 경험한 후 나타나는 정신적 외상 반응. 통역 시 주의할 점은 베트남전 참전 경험이 있는 환자나 가족이 많으므로 문화적 민감성을 유지해야 하고, 침습적 기억(flashback), 회피 증상, 과각성 상태를 정확히 구분해서 설명해야 한다는 것이다. 트라우마를 '마음이 약해서'로 치부하지 않도록 질병임을 강조해야 한다.",
        "meaningVi": "Rối loạn tâm thần xảy ra sau khi trải qua sự kiện chấn thương nghiêm trọng như chiến tranh, tai nạn, bạo lực. Triệu chứng gồm hồi tưởng (flashback), ác mộng, tránh né các yếu tố gợi nhớ, dễ giật mình, mất ngủ. Đây là bệnh lý cần điều trị chuyên khoa, không phải yếu đuối tinh thần.",
        "context": "정신건강의학과, 트라우마 센터",
        "culturalNote": "베트남은 전쟁 경험이 있는 국가로 PTSD 환자가 많지만 치료 자원이 부족하다. 한국은 재난 심리 지원 시스템이 발달했으나 베트남은 가족 내에서 해결하려는 경향이 강하다. 통역 시 전쟁 트라우마에 대한 이해가 필요하다.",
        "commonMistakes": [
            {
                "mistake": "PTSD를 '트라우마'로만 번역",
                "correction": "rối loạn stress sau sang chấn (PTSD)",
                "explanation": "트라우마는 원인, PTSD는 질환명"
            },
            {
                "mistake": "flashback을 '기억'으로 번역",
                "correction": "hồi tưởng xâm nhập (침습적 기억)",
                "explanation": "생생하게 재경험하는 특수한 증상"
            },
            {
                "mistake": "치료 기간을 단기로 설명",
                "correction": "장기 치료 필요성 명시",
                "explanation": "PTSD는 만성화될 수 있음"
            }
        ],
        "examples": [
            {
                "ko": "교통사고 후 PTSD 증상이 나타났습니다.",
                "vi": "Sau tai nạn giao thông, anh ấy có triệu chứng PTSD.",
                "situation": "formal"
            },
            {
                "ko": "악몽 때문에 잠을 못 자요.",
                "vi": "Tôi không ngủ được vì ác mộng.",
                "situation": "informal"
            },
            {
                "ko": "EMDR 치료를 시작하겠습니다.",
                "vi": "Chúng ta sẽ bắt đầu liệu pháp EMDR.",
                "situation": "onsite"
            }
        ],
        "relatedTerms": ["트라우마", "플래시백", "인지행동치료", "EMDR", "정신건강의학과"]
    },
    {
        "slug": "tam-than-phan-liet",
        "korean": "조현병",
        "vietnamese": "Tâm thần phân liệt",
        "hanja": "調絃病",
        "hanjaReading": "調(고를 조) + 絃(줄 현) + 病(병 병)",
        "pronunciation": "땀 턴 펀 리엣",
        "meaningKo": "현실 판단력 장애, 망상, 환청, 사고 장애 등을 특징으로 하는 만성 정신질환. 통역 시 주의할 점은 '정신분열병'이라는 구 명칭을 쓰지 않고 '조현병'으로 통일하며, 베트남에서 이 질환에 대한 낙인이 심하므로 치료 가능성과 회복 사례를 강조해야 한다는 것이다. 양성 증상과 음성 증상을 구분해서 설명하고 약물 치료의 중요성을 반드시 전달해야 한다.",
        "meaningVi": "Bệnh tâm thần nặng mạn tính đặc trưng bởi ảo giác (nghe thấy tiếng, nhìn thấy thứ không có), hoang tưởng, rối loạn tư duy. Có hai nhóm triệu chứng: dương tính (ảo giác, hoang tưởng) và âm tính (thiếu động lực, cảm xúc phẳng lặng). Cần điều trị thuốc lâu dài và theo dõi chuyên khoa.",
        "context": "정신건강의학과 입원, 외래",
        "culturalNote": "한국은 2011년 '정신분열병'을 '조현병'으로 개칭하여 낙인을 줄였지만, 베트남에서는 여전히 환자를 격리하거나 숨기는 경우가 많다. 베트남 가족은 전통 치료사를 먼저 찾는 경향이 있으므로 약물 치료의 필수성을 강조해야 한다.",
        "commonMistakes": [
            {
                "mistake": "'정신분열병'으로 번역",
                "correction": "조현병 (한국 공식 명칭)",
                "explanation": "낙인 감소를 위한 용어 변경"
            },
            {
                "mistake": "환청을 '귀신 소리'로 설명",
                "correction": "ảo thanh (의학적 증상)",
                "explanation": "미신과 구분 필요"
            },
            {
                "mistake": "완치 가능하다고 설명",
                "correction": "증상 조절 가능, 재발 방지 중요",
                "explanation": "현실적인 치료 목표 제시"
            }
        ],
        "examples": [
            {
                "ko": "조현병은 꾸준한 약물 치료가 중요합니다.",
                "vi": "Với tâm thần phân liệt, điều trị thuốc đều đặn rất quan trọng.",
                "situation": "formal"
            },
            {
                "ko": "환청이 들려요.",
                "vi": "Tôi nghe thấy tiếng nói (ảo thanh).",
                "situation": "informal"
            },
            {
                "ko": "항정신병 약물을 처방하겠습니다.",
                "vi": "Tôi sẽ kê đơn thuốc chống loạn thần.",
                "situation": "onsite"
            }
        ],
        "relatedTerms": ["망상", "환청", "항정신병약물", "정신건강의학과", "재활치료"]
    },
    {
        "slug": "lieu-phap-nhan-thuc-hanh-vi",
        "korean": "인지행동치료",
        "vietnamese": "Liệu pháp nhận thức hành vi",
        "hanja": "認知行動治療",
        "hanjaReading": "認(알 인) + 知(알 지) + 行(다닐 행) + 動(움직일 동) + 治(다스릴 치) + 療(치료할 료)",
        "pronunciation": "리에우 팝 년 턱 한 비",
        "meaningKo": "부적응적 사고와 행동 패턴을 찾아내어 변화시키는 심리치료 기법. 통역 시 주의할 점은 CBT가 단순한 상담이 아니라 구조화된 치료 기법임을 강조하고, 숙제(homework)의 중요성을 설명해야 한다는 것이다. 베트남 환자는 '대화만으로 치료가 되나?'는 의구심을 가질 수 있으므로 과학적 근거를 제시해야 한다.",
        "meaningVi": "Phương pháp trị liệu tâm lý tập trung vào nhận diện và thay đổi các suy nghĩ tiêu cực, bóp méo (nhận thức) và hành vi không phù hợp. CBT có cấu trúc rõ ràng với mục tiêu cụ thể, thường kéo dài 12-20 buổi, và yêu cầu bệnh nhân làm bài tập về nhà giữa các phiên.",
        "context": "심리상담, 정신건강의학과 치료",
        "culturalNote": "한국은 CBT가 보편화되어 앱으로도 제공되지만, 베트남은 심리치료 자체가 생소한 경우가 많다. 베트남 환자는 '말로 무엇을 해결하나'는 회의적 태도를 보일 수 있으므로 구체적 사례와 효과를 제시해야 한다.",
        "commonMistakes": [
            {
                "mistake": "CBT를 '상담'으로만 번역",
                "correction": "liệu pháp (치료 기법)",
                "explanation": "일반 상담보다 구조화되고 증거 기반"
            },
            {
                "mistake": "숙제를 선택 사항으로 설명",
                "correction": "bài tập về nhà (필수 과제)",
                "explanation": "CBT 효과의 핵심 요소"
            },
            {
                "mistake": "단기 치료로만 설명",
                "correction": "12-20 buổi, 경우에 따라 연장 가능",
                "explanation": "현실적 기대치 설정"
            }
        ],
        "examples": [
            {
                "ko": "불안장애에는 인지행동치료가 효과적입니다.",
                "vi": "Liệu pháp nhận thức hành vi rất hiệu quả với rối loạn lo âu.",
                "situation": "formal"
            },
            {
                "ko": "CBT 숙제 다 했어요.",
                "vi": "Tôi đã làm xong bài tập CBT.",
                "situation": "informal"
            },
            {
                "ko": "이번 주는 사고 기록지를 작성하세요.",
                "vi": "Tuần này bạn hãy ghi lại nhật ký suy nghĩ.",
                "situation": "onsite"
            }
        ],
        "relatedTerms": ["심리치료", "우울증", "불안장애", "사고기록지", "노출치료"]
    },
    {
        "slug": "tiem-botox",
        "korean": "보톡스시술",
        "vietnamese": "Tiêm Botox",
        "hanja": None,
        "hanjaReading": None,
        "pronunciation": "띠엠 보똑",
        "meaningKo": "보툴리눔 톡신을 주사하여 근육을 이완시켜 주름을 개선하는 시술. 통역 시 주의할 점은 미용 목적 외에도 사각턱, 다한증, 편두통 치료에도 쓰인다는 것을 설명해야 하고, 시술 후 주의사항(4시간 눕지 않기, 마사지 금지)을 정확히 전달해야 한다는 것이다. 베트남 환자는 가격에 민감하므로 정품 여부를 확인시켜야 한다.",
        "meaningVi": "Thủ thuật tiêm chất botulinum toxin để làm giãn cơ, cải thiện nếp nhăn. Ngoài mục đích thẩm mỹ, Botox còn được dùng điều trị hàm vuông, đổ mồ hôi nhiều, đau nửa đầu. Hiệu quả kéo dài 4-6 tháng và cần tiêm lại định kỳ.",
        "context": "성형외과, 피부과",
        "culturalNote": "한국은 보톡스 시술이 매우 보편화되어 점심시간에 시술받는 경우도 많지만, 베트남에서는 아직 부유층 중심이다. 베트남 환자는 저가 비정품에 노출될 위험이 크므로 정품 확인이 중요하다. 한국은 남성도 많이 받지만 베트남은 여성 위주다.",
        "commonMistakes": [
            {
                "mistake": "보톡스를 'thuốc chống nhăn'으로 표현",
                "correction": "tiêm Botox (고유명사)",
                "explanation": "보톡스는 브랜드명이자 시술명"
            },
            {
                "mistake": "영구 효과로 설명",
                "correction": "4-6개월 지속, 재시술 필요",
                "explanation": "현실적 기대치 설정"
            },
            {
                "mistake": "시술 후 주의사항 누락",
                "correction": "4시간 눕지 않기, 마사지 금지 명시",
                "explanation": "부작용 방지 위해 필수"
            }
        ],
        "examples": [
            {
                "ko": "이마 주름에 보톡스 20유닛 시술하겠습니다.",
                "vi": "Tôi sẽ tiêm 20 đơn vị Botox vào nếp nhăn trán.",
                "situation": "formal"
            },
            {
                "ko": "보톡스 맞고 왔어요.",
                "vi": "Tôi vừa đi tiêm Botox về.",
                "situation": "informal"
            },
            {
                "ko": "시술 후 4시간 동안 눕지 마세요.",
                "vi": "Sau khi tiêm, không nằm trong 4 giờ.",
                "situation": "onsite"
            }
        ],
        "relatedTerms": ["필러", "주름개선", "사각턱", "성형외과", "피부과"]
    },
    {
        "slug": "tiem-filler-hyaluronic-acid",
        "korean": "히알루론산필러",
        "vietnamese": "Tiêm filler hyaluronic acid",
        "hanja": None,
        "hanjaReading": None,
        "pronunciation": "띠엠 필러 히알루로닉 애씨",
        "meaningKo": "히알루론산 성분의 필러를 주입하여 볼륨을 채우거나 윤곽을 개선하는 시술. 통역 시 주의할 점은 보톡스와 달리 즉각적인 볼륨 효과가 있다는 것을 설명하고, 부작용(멍, 부기, 드물게 혈관 색전)에 대한 충분한 설명이 필요하다는 것이다. 베트남 환자는 필러 종류와 정품 여부를 확인하려 하므로 제품 정보를 투명하게 제공해야 한다.",
        "meaningVi": "Thủ thuật tiêm chất làm đầy (filler) chứa hyaluronic acid để tăng thể tích, cải thiện đường nét khuôn mặt. Khác với Botox (làm giãn cơ), filler làm đầy các vùng lõm, tạo khối. Hiệu quả kéo dài 6-18 tháng tùy loại filler và vị trí tiêm.",
        "context": "성형외과, 피부과",
        "culturalNote": "한국은 필러 시술이 대중화되어 다양한 부위에 시술하지만, 베트남에서는 코와 턱에 집중되는 경향이 있다. 베트남 환자는 입체적인 얼굴을 선호해 과도한 시술을 원할 수 있으므로 자연스러움을 강조해야 한다. 비정품 필러 사고가 많으므로 정품 확인이 중요하다.",
        "commonMistakes": [
            {
                "mistake": "필러를 'botox'와 혼용",
                "correction": "filler (볼륨) vs Botox (근육 이완)",
                "explanation": "작용 원리와 효과가 완전히 다름"
            },
            {
                "mistake": "영구 시술로 설명",
                "correction": "6-18개월 지속, 흡수됨",
                "explanation": "히알루론산은 체내 흡수됨"
            },
            {
                "mistake": "혈관 색전 위험 미고지",
                "correction": "드물지만 심각한 부작용 가능성 설명",
                "explanation": "사전 동의 필수 사항"
            }
        ],
        "examples": [
            {
                "ko": "팔자주름에 필러 1cc 시술하겠습니다.",
                "vi": "Tôi sẽ tiêm 1cc filler vào nếp nhăn rãnh mũi má.",
                "situation": "formal"
            },
            {
                "ko": "코 필러 맞고 싶어요.",
                "vi": "Tôi muốn tiêm filler mũi.",
                "situation": "informal"
            },
            {
                "ko": "멍이 들 수 있으니 일주일 후 행사는 피하세요.",
                "vi": "Có thể bị bầm, nên tránh sự kiện trong vòng một tuần.",
                "situation": "onsite"
            }
        ],
        "relatedTerms": ["보톡스", "주름개선", "볼륨", "성형외과", "피부과"]
    },
    {
        "slug": "laser-toning",
        "korean": "레이저토닝",
        "vietnamese": "Laser toning",
        "hanja": None,
        "hanjaReading": None,
        "pronunciation": "레이저 토닝",
        "meaningKo": "저출력 레이저를 이용해 색소 침착을 개선하고 피부 톤을 균일하게 하는 시술. 통역 시 주의할 점은 즉각적 효과가 아니라 여러 번 반복 시술이 필요하다는 것을 설명하고, 시술 후 자외선 차단의 중요성을 강조해야 한다는 것이다. 베트남 환자는 미백 효과를 기대하므로 현실적 기대치를 설정해야 한다.",
        "meaningVi": "Liệu trình dùng laser công suất thấp để cải thiện sắc tố da, đều màu da. Cần thực hiện nhiều lần (thường 5-10 lần, 2 tuần/lần) để thấy hiệu quả rõ. Sau khi làm phải chống nắng nghiêm ngặt để tránh tăng sắc tố ngược.",
        "context": "피부과, 의료미용",
        "culturalNote": "한국은 레이저 시술이 매우 발달하고 다양한 종류가 있지만, 베트남은 아직 제한적이다. 베트남 환자는 '하얀 피부'를 선호해 과도한 미백을 원할 수 있으므로 자연스러운 톤 개선을 권장해야 한다. 베트남은 자외선이 강하므로 사후 관리가 더욱 중요하다.",
        "commonMistakes": [
            {
                "mistake": "1회 시술로 효과 설명",
                "correction": "5-10회 반복 필요",
                "explanation": "누적 효과로 개선됨"
            },
            {
                "mistake": "미백 시술로 설명",
                "correction": "톤 균일화, 색소 개선 (미백 아님)",
                "explanation": "과도한 기대 방지"
            },
            {
                "mistake": "자외선 차단 중요성 누락",
                "correction": "SPF50 매일 사용 필수",
                "explanation": "재색소 침착 방지"
            }
        ],
        "examples": [
            {
                "ko": "기미 치료에 레이저토닝 10회 권장합니다.",
                "vi": "Để trị nám, tôi khuyên nên làm 10 lần laser toning.",
                "situation": "formal"
            },
            {
                "ko": "레이저토닝 받고 왔어요.",
                "vi": "Tôi vừa đi làm laser toning.",
                "situation": "informal"
            },
            {
                "ko": "시술 후 일주일간 사우나는 피하세요.",
                "vi": "Sau khi làm, tránh xông hơi trong một tuần.",
                "situation": "onsite"
            }
        ],
        "relatedTerms": ["기미", "색소침착", "미백", "피부과", "자외선차단"]
    },
    {
        "slug": "phau-thuat-cat-mi",
        "korean": "쌍꺼풀수술",
        "vietnamese": "Phẫu thuật cắt mí",
        "hanja": None,
        "hanjaReading": None,
        "pronunciation": "퍼우 투엇 껏 미",
        "meaningKo": "눈꺼풀에 주름선을 만들어 쌍꺼풀을 형성하는 미용 성형수술. 통역 시 주의할 점은 매몰법과 절개법의 차이를 명확히 설명하고, 회복 기간과 부작용(붓기, 멍, 흉터) 가능성을 솔직하게 전달해야 한다는 것이다. 베트남 환자는 자연스러운 쌍꺼풀보다 뚜렷한 라인을 선호할 수 있으므로 얼굴 조화를 강조해야 한다.",
        "meaningVi": "Phẫu thuật tạo nếp gấp mí mắt để có mắt hai mí. Có hai phương pháp: cắt mí không phẫu thuật (bấm mí) và cắt mí có phẫu thuật (cắt da thừa). Thời gian hồi phục khoảng 1-2 tuần, sẹo nhạt dần sau 3-6 tháng.",
        "context": "성형외과",
        "culturalNote": "한국은 쌍꺼풀수술이 가장 흔한 성형수술 중 하나이고 10대 후반에도 받지만, 베트남에서는 아직 부유층 중심이다. 베트남 환자는 서구적 외모를 선호하는 경향이 있어 과도하게 높은 라인을 원할 수 있으므로 자연스러움을 권장해야 한다.",
        "commonMistakes": [
            {
                "mistake": "매몰법과 절개법 구분 없이 설명",
                "correction": "bấm mí (매몰) vs cắt mí (절개) 차이 명시",
                "explanation": "비용, 회복기간, 지속성이 다름"
            },
            {
                "mistake": "영구적 효과로 설명 (매몰법)",
                "correction": "매몰법은 풀릴 수 있음 설명",
                "explanation": "재수술 가능성 인지 필요"
            },
            {
                "mistake": "수술 즉시 최종 모습으로 설명",
                "correction": "붓기 빠지는 데 2주-3개월 소요",
                "explanation": "현실적 기대치 설정"
            }
        ],
        "examples": [
            {
                "ko": "절개법 쌍꺼풀수술을 권장합니다.",
                "vi": "Tôi khuyên nên phẫu thuật cắt mí có rạch da.",
                "situation": "formal"
            },
            {
                "ko": "쌍수하고 싶어요.",
                "vi": "Tôi muốn cắt mí mắt.",
                "situation": "informal"
            },
            {
                "ko": "일주일 후 실밥 제거하러 오세요.",
                "vi": "Một tuần sau hãy đến cắt chỉ.",
                "situation": "onsite"
            }
        ],
        "relatedTerms": ["성형외과", "눈성형", "매몰법", "절개법", "회복기간"]
    },
    {
        "slug": "phau-thuat-nang-mui",
        "korean": "코성형",
        "vietnamese": "Phẫu thuật nâng mũi",
        "hanja": None,
        "hanjaReading": None,
        "pronunciation": "퍼우 투엇 능 무이",
        "meaningKo": "코의 모양을 변화시키는 미용 성형수술로 융비술, 비첨 성형, 콧볼 축소 등을 포함한다. 통역 시 주의할 점은 보형물(실리콘, 고어텍스)과 자가 연골의 차이를 설명하고, 합병증(구축, 염증, 보형물 이동) 위험성을 반드시 전달해야 한다는 것이다. 베트남 환자는 높고 뾰족한 코를 선호하므로 얼굴 조화를 강조해야 한다.",
        "meaningVi": "Phẫu thuật thay đổi hình dáng mũi, bao gồm nâng cao sống mũi, tạo hình đầu mũi, thu nhỏ cánh mũi. Vật liệu có thể dùng silicon, Gore-Tex hoặc sụn tự thân. Phẫu thuật lớn với thời gian hồi phục 2-4 tuần, có nguy cơ biến chứng như co cứng, nhiễm trùng, lệch sống mũi.",
        "context": "성형외과",
        "culturalNote": "한국은 코성형이 매우 발달해 자연스러운 결과를 추구하지만, 베트남 환자는 서구적 외모를 선호해 과도하게 높은 코를 원할 수 있다. 베트남은 더운 기후라 회복 중 관리가 더 어렵고, 재수술율도 고려해야 한다. 베트남 환자는 가격에 민감하므로 저가 시술의 위험성을 경고해야 한다.",
        "commonMistakes": [
            {
                "mistake": "코성형을 '코 높이기'로만 설명",
                "correction": "융비, 비첨, 콧볼 등 세부 시술 구분",
                "explanation": "환자가 원하는 부위 정확히 파악 필요"
            },
            {
                "mistake": "보형물 종류 설명 없이 진행",
                "correction": "실리콘, 고어텍스, 자가연골 차이 설명",
                "explanation": "재료별 장단점과 비용 차이"
            },
            {
                "mistake": "재수술 가능성 미고지",
                "correction": "10-20% 재수술율 있음 설명",
                "explanation": "현실적 기대치 설정"
            }
        ],
        "examples": [
            {
                "ko": "자가 연골로 코끝 성형을 하겠습니다.",
                "vi": "Tôi sẽ dùng sụn tự thân để tạo hình đầu mũi.",
                "situation": "formal"
            },
            {
                "ko": "코수술하고 싶어요.",
                "vi": "Tôi muốn phẫu thuật mũi.",
                "situation": "informal"
            },
            {
                "ko": "3개월간 안경 착용은 피하세요.",
                "vi": "Tránh đeo kính trong 3 tháng.",
                "situation": "onsite"
            }
        ],
        "relatedTerms": ["성형외과", "보형물", "자가연골", "융비술", "비첨성형"]
    },
    {
        "slug": "hut-mo",
        "korean": "지방흡입",
        "vietnamese": "Hút mỡ",
        "hanja": "脂肪吸入",
        "hanjaReading": "脂(기름 지) + 肪(기름 방) + 吸(들이마실 흡) + 入(들 입)",
        "pronunciation": "훗 머",
        "meaningKo": "수술적 방법으로 피하 지방을 제거하는 시술. 통역 시 주의할 점은 체중 감량 목적이 아니라 체형 교정 목적임을 명확히 하고, 전신마취 위험성과 회복 기간(압박복 착용 2-3개월)을 충분히 설명해야 한다는 것이다. 베트남 환자는 비만 치료로 오해할 수 있으므로 적응증을 정확히 전달해야 한다.",
        "meaningVi": "Phẫu thuật hút mỡ dưới da để cải thiện đường nét cơ thể. Không phải phương pháp giảm cân mà là tạo hình vùng mỡ cục bộ (bụng, đùi, cánh tay). Cần gây mê toàn thân, mặc áo nịt 2-3 tháng sau phẫu thuật, có nguy cơ chảy máu, nhiễm trùng, da không đều.",
        "context": "성형외과, 비만클리닉",
        "culturalNote": "한국은 지방흡입이 흔한 시술이지만 베트남에서는 아직 고가이고 접근성이 낮다. 베트남 환자는 '한 번에 살 빼는 방법'으로 오해할 수 있으므로 식이요법과 운동이 우선임을 강조해야 한다. 베트남은 더운 기후라 압박복 착용이 불편할 수 있다.",
        "commonMistakes": [
            {
                "mistake": "체중 감량 시술로 설명",
                "correction": "체형 교정 시술 (체중 변화 미미)",
                "explanation": "살이 아니라 모양을 바꾸는 것"
            },
            {
                "mistake": "회복 기간 축소 설명",
                "correction": "압박복 2-3개월, 부기 6개월",
                "explanation": "현실적 회복 기간 안내"
            },
            {
                "mistake": "부작용 위험 미고지",
                "correction": "전신마취 위험, 피부 울퉁불퉁 가능성",
                "explanation": "사전 동의 필수"
            }
        ],
        "examples": [
            {
                "ko": "복부 지방흡입 2리터 시술 예정입니다.",
                "vi": "Dự kiến hút 2 lít mỡ vùng bụng.",
                "situation": "formal"
            },
            {
                "ko": "팔뚝 지흡하고 싶어요.",
                "vi": "Tôi muốn hút mỡ cánh tay.",
                "situation": "informal"
            },
            {
                "ko": "압박복은 24시간 착용하세요.",
                "vi": "Hãy mặc áo nịt 24 giờ mỗi ngày.",
                "situation": "onsite"
            }
        ],
        "relatedTerms": ["성형외과", "체형교정", "압박복", "전신마취", "부작용"]
    },
    {
        "slug": "phien-dich-y-te",
        "korean": "의료통역",
        "vietnamese": "Phiên dịch y tế",
        "hanja": "醫療通譯",
        "hanjaReading": "醫(의원 의) + 療(치료할 료) + 通(통할 통) + 譯(번역할 역)",
        "pronunciation": "피엔 직 이 떼",
        "meaningKo": "의료 현장에서 환자와 의료진 간 언어 장벽을 해소하는 전문 통역. 통역 시 주의할 점은 단순 언어 전환이 아니라 문화적 중재자 역할도 해야 하고, 의료 용어의 정확성과 환자 프라이버시 보호가 필수라는 것이다. 의료 오역은 생명과 직결되므로 불확실하면 반드시 확인해야 하며, 윤리적 중립성을 지켜야 한다.",
        "meaningVi": "Phiên dịch chuyên môn tại cơ sở y tế, kết nối bệnh nhân và bác sĩ khi có rào cản ngôn ngữ. Yêu cầu: thuật ngữ y khoa chính xác, bảo mật thông tin bệnh nhân, trung lập (không thêm ý kiến cá nhân), hiểu văn hóa y tế của cả hai nước. Sai sót trong phiên dịch y tế có thể gây hậu quả nghiêm trọng.",
        "context": "병원, 클리닉, 원격 의료",
        "culturalNote": "한국은 의료통역사 제도가 있지만 베트남어 통역사가 부족하다. 베트남 환자는 가족이나 지인에게 통역을 맡기는 경우가 많아 정확성이 떨어지고 프라이버시 침해 우려가 있다. 의료통역사는 문화적 차이(한국의 직접적 의사소통 vs 베트남의 간접적 표현)도 중재해야 한다.",
        "commonMistakes": [
            {
                "mistake": "의역이나 요약으로 통역",
                "correction": "있는 그대로 정확히 통역",
                "explanation": "의료 정보는 누락이나 변형 불가"
            },
            {
                "mistake": "환자 대신 대답",
                "correction": "통역사는 전달자, 대리인 아님",
                "explanation": "윤리적 중립성 유지"
            },
            {
                "mistake": "전문 용어를 일상어로 바꿈",
                "correction": "정확한 의학 용어 사용 + 필요 시 부연",
                "explanation": "오진 방지 위해 필수"
            }
        ],
        "examples": [
            {
                "ko": "의료통역사가 동행하여 진료를 돕겠습니다.",
                "vi": "Phiên dịch viên y tế sẽ đi cùng để hỗ trợ khám bệnh.",
                "situation": "formal"
            },
            {
                "ko": "통역 필요하면 부르세요.",
                "vi": "Nếu cần phiên dịch, hãy gọi tôi.",
                "situation": "informal"
            },
            {
                "ko": "정확히 통역하기 위해 녹음해도 될까요?",
                "vi": "Để phiên dịch chính xác, tôi có thể ghi âm được không?",
                "situation": "onsite"
            }
        ],
        "relatedTerms": ["의료용어", "환자안전", "문화중재", "통역윤리", "프라이버시"]
    },
    {
        "slug": "bao-hiem-y-te-quoc-dan",
        "korean": "국민건강보험",
        "vietnamese": "Bảo hiểm y tế quốc dân",
        "hanja": "國民健康保險",
        "hanjaReading": "國(나라 국) + 民(백성 민) + 健(건강할 건) + 康(편안할 강) + 保(지킬 보) + 險(험할 험)",
        "pronunciation": "바오 히엠 이 떼 꾸억 잔",
        "meaningKo": "국가가 운영하는 사회보험 제도로 국민의 의료비를 보장한다. 통역 시 주의할 점은 한국은 전국민 의무가입이지만 베트남은 아직 보편적 적용이 안 되고 있다는 차이를 설명해야 하고, 보험 적용 항목과 본인부담금을 명확히 전달해야 한다는 것이다. 베트남 환자는 건강보험 사용법을 모를 수 있으므로 절차를 상세히 안내해야 한다.",
        "meaningVi": "Chế độ bảo hiểm xã hội do nhà nước điều hành, chi trả chi phí y tế cho người dân. Ở Hàn Quốc, mọi công dân đều phải tham gia (bắt buộc), bao phủ phần lớn chi phí khám chữa bệnh. Còn tại Việt Nam, bảo hiểm y tế chưa phổ cập hoàn toàn và tỷ lệ đồng chi trả cao hơn.",
        "context": "병원 접수, 보험 청구",
        "culturalNote": "한국은 1989년 전국민 건강보험을 달성했고 보장률이 높지만, 베트남은 아직 자비 진료가 많다. 베트남 환자는 한국에서 치료 시 건강보험 적용이 안 돼 고액 의료비에 놀랄 수 있으므로 사전 안내가 필요하다. 한국은 의료비가 저렴한 편이지만 베트남 환자에게는 여전히 부담일 수 있다.",
        "commonMistakes": [
            {
                "mistake": "베트남 건강보험과 동일시",
                "correction": "한국은 전국민 의무가입, 베트남은 선택적",
                "explanation": "제도 차이 명확히 설명"
            },
            {
                "mistake": "100% 보장으로 설명",
                "correction": "본인부담금 있음 (보통 20-30%)",
                "explanation": "실제 비용 예상 가능하게"
            },
            {
                "mistake": "외국인도 동일 적용으로 설명",
                "correction": "체류 자격에 따라 가입 조건 다름",
                "explanation": "베트남 환자 대부분 외국인"
            }
        ],
        "examples": [
            {
                "ko": "건강보험증을 지참하시면 본인부담금만 내시면 됩니다.",
                "vi": "Nếu mang thẻ bảo hiểm y tế, bạn chỉ trả phần đồng chi trả.",
                "situation": "formal"
            },
            {
                "ko": "보험 돼요?",
                "vi": "Có được bảo hiểm không?",
                "situation": "informal"
            },
            {
                "ko": "이 시술은 비급여 항목입니다.",
                "vi": "Thủ thuật này không được bảo hiểm chi trả.",
                "situation": "onsite"
            }
        ],
        "relatedTerms": ["의료비", "본인부담금", "비급여", "건강보험증", "의료보장"]
    },
    {
        "slug": "dong-y-truoc",
        "korean": "사전동의",
        "vietnamese": "Đồng ý trước",
        "hanja": "事前同意",
        "hanjaReading": "事(일 사) + 前(앞 전) + 同(한가지 동) + 意(뜻 의)",
        "pronunciation": "동 이 쯔억",
        "meaningKo": "의료 행위 전에 환자에게 목적, 방법, 위험성, 대안 등을 충분히 설명하고 자발적 동의를 받는 과정. 통역 시 주의할 점은 단순 서명이 아니라 이해를 바탕으로 한 동의여야 하므로, 환자가 완전히 이해했는지 확인해야 하고, 거부할 권리도 있음을 알려야 한다는 것이다. 문화적 차이로 인해 베트남 환자는 의사 결정을 가족에게 맡기려 할 수 있다.",
        "meaningVi": "Quy trình giải thích đầy đủ về mục đích, phương pháp, rủi ro, phương án thay thế của một thủ thuật y tế và xin sự đồng ý tự nguyện của bệnh nhân trước khi thực hiện. Không chỉ là ký tên mà phải dựa trên sự hiểu biết. Bệnh nhân có quyền từ chối.",
        "context": "수술 전, 시술 전, 임상시험",
        "culturalNote": "한국은 사전동의가 법적 의무이고 개인주의 문화라 환자 본인이 결정하지만, 베트남은 집단주의 문화로 가족(특히 가장)이 결정하는 경우가 많다. 베트남 환자는 의사에게 전적으로 의존하려는 경향이 있어 '선생님이 알아서 해주세요'라고 할 수 있으므로 능동적 참여를 독려해야 한다.",
        "commonMistakes": [
            {
                "mistake": "형식적 서명만 받음",
                "correction": "이해 여부 확인 질문 필수",
                "explanation": "법적 효력을 위해서도 필요"
            },
            {
                "mistake": "전문 용어로만 설명",
                "correction": "쉬운 말로 풀어서 설명 + 그림/모형 활용",
                "explanation": "진정한 이해 기반 동의 위해"
            },
            {
                "mistake": "거부 시 압박",
                "correction": "환자의 자율권 존중",
                "explanation": "윤리적 의무"
            }
        ],
        "examples": [
            {
                "ko": "수술 전 사전동의서에 서명해주셔야 합니다.",
                "vi": "Trước khi phẫu thuật, bạn cần ký vào giấy đồng ý.",
                "situation": "formal"
            },
            {
                "ko": "동의서 읽어보셨어요?",
                "vi": "Bạn đã đọc giấy đồng ý chưa?",
                "situation": "informal"
            },
            {
                "ko": "이해가 안 되는 부분이 있으면 질문하세요.",
                "vi": "Nếu có phần nào không hiểu, hãy hỏi.",
                "situation": "onsite"
            }
        ],
        "relatedTerms": ["환자권리", "의료윤리", "자율권", "설명의무", "동의서"]
    },
    {
        "slug": "benh-an-dien-tu",
        "korean": "전자의무기록",
        "vietnamese": "Bệnh án điện tử",
        "hanja": "電子醫務記錄",
        "hanjaReading": "電(번개 전) + 子(아들 자) + 醫(의원 의) + 務(힘쓸 무) + 記(기록할 기) + 錄(기록할 록)",
        "pronunciation": "벵 언 디엔 뜨",
        "meaningKo": "환자의 진료 정보를 전자적으로 기록·저장·관리하는 시스템. 통역 시 주의할 점은 종이 차트와 달리 여러 의료기관에서 공유 가능하다는 장점을 설명하고, 개인정보 보호 시스템도 함께 안내해야 한다는 것이다. 베트남 환자는 디지털 의료에 익숙하지 않을 수 있으므로 접근 방법과 권한을 명확히 설명해야 한다.",
        "meaningVi": "Hệ thống ghi chép, lưu trữ và quản lý thông tin khám chữa bệnh của bệnh nhân dưới dạng điện tử. Khác với hồ sơ giấy, bệnh án điện tử có thể chia sẻ giữa các cơ sở y tế, giúp theo dõi liên tục. Hệ thống bảo mật nghiêm ngặt để bảo vệ quyền riêng tư.",
        "context": "병원 시스템, 의료 정보",
        "culturalNote": "한국은 EMR이 보편화되어 환자도 모바일로 조회 가능하지만, 베트남은 아직 종이 기록이 많다. 베트남 환자는 자신의 의료 기록을 직접 볼 수 있다는 점에 놀랄 수 있다. 한국은 의료기관 간 정보 공유가 발달했지만 베트남은 개별 병원에 기록이 분산되어 있다.",
        "commonMistakes": [
            {
                "mistake": "종이 차트와 동일시",
                "correction": "실시간 공유, 검색, 분석 가능",
                "explanation": "디지털의 장점 설명"
            },
            {
                "mistake": "보안 우려 무시",
                "correction": "접근 권한, 암호화 시스템 설명",
                "explanation": "개인정보 보호 강조"
            },
            {
                "mistake": "환자 조회권 미고지",
                "correction": "본인 기록 열람 가능 안내",
                "explanation": "환자 권리 알림"
            }
        ],
        "examples": [
            {
                "ko": "전자의무기록으로 이전 진료 내역을 확인할 수 있습니다.",
                "vi": "Nhờ bệnh án điện tử, chúng tôi có thể xem lịch sử khám bệnh trước đó.",
                "situation": "formal"
            },
            {
                "ko": "앱에서 검사 결과 볼 수 있어요.",
                "vi": "Bạn có thể xem kết quả xét nghiệm trên ứng dụng.",
                "situation": "informal"
            },
            {
                "ko": "기록은 5년간 보관됩니다.",
                "vi": "Hồ sơ sẽ được lưu trữ trong 5 năm.",
                "situation": "onsite"
            }
        ],
        "relatedTerms": ["의무기록", "개인정보보호", "EMR", "의료정보", "환자권리"]
    }
]

print(f"✅ 생성된 신규 용어: {len(new_terms)}개")
print(f"📋 기존 용어: {len(data)}개")

# 중복 필터링
added = 0
for term in new_terms:
    if term['slug'] not in existing_slugs:
        data.append(term)
        existing_slugs.add(term['slug'])
        added += 1
    else:
        print(f"⚠️ 중복 제외: {term['slug']}")

# 저장
with open(file_path, 'w', encoding='utf-8') as f:
    json.dump(data, f, ensure_ascii=False, indent=2)

print(f"\n✅ 추가 완료: {added}개")
print(f"📊 최종 총 용어 수: {len(data)}개")
print(f"💾 저장 위치: {file_path}")
