#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
의료 용어 추가 스크립트 v2-861
내분비내과, 혈액종양내과, 신경과 전문 용어 50개 추가
Tier S 품질 기준 준수 (90점 이상)
"""

import json
import os

# 파일 경로 설정
file_path = os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', 'data', 'terms', 'medical.json')

# 50개 신규 의료 용어 데이터
new_terms = [
    {
        "slug": "cuong-giap",
        "korean": "갑상선기능항진증",
        "vietnamese": "Cường giáp",
        "hanja": "甲狀腺機能亢進症",
        "hanjaReading": "甲(갑 갑) + 狀(모양 상) + 腺(샘 선) + 機(틀 기) + 能(능할 능) + 亢(높을 항) + 進(나아갈 진) + 症(병 증)",
        "pronunciation": "깝쌍썬끼능항찐쯩",
        "meaningKo": "갑상선에서 갑상선호르몬이 과다하게 분비되어 신체 대사가 항진되는 질환입니다. 통역 시 주의할 점은 베트남어로 'Cường giáp'이라고 하며, 환자에게 증상을 설명할 때 '심계항진, 체중감소, 손떨림' 등의 증상을 정확히 전달해야 합니다. 한국에서는 '그레이브스병'과 혼용하여 사용하므로 구분이 필요하며, 통역 시 의사가 어떤 맥락에서 사용하는지 파악해야 합니다.",
        "meaningVi": "Bệnh lý tuyến giáp tiết quá nhiều hormone giáp, làm tăng quá trình trao đổi chất trong cơ thể. Triệu chứng bao gồm nhịp tim nhanh, sụt cân, run tay, mắt lồi.",
        "context": "내분비내과 진료실에서 갑상선 질환 진단 및 치료 계획 수립 시",
        "culturalNote": "한국에서는 갑상선 질환 검진이 일반 건강검진에 포함되어 조기 발견율이 높지만, 베트남에서는 증상이 심해진 후 병원을 찾는 경우가 많습니다. 한국 환자들은 '갑기항'으로 줄여 부르기도 하며, 베트남 환자들은 전통 약재로 먼저 치료를 시도하는 경우가 있어 통역 시 이를 고려해야 합니다.",
        "commonMistakes": [
            {
                "mistake": "갑상선암으로 오역",
                "correction": "갑상선기능항진증 (Cường giáp)",
                "explanation": "기능항진증은 호르몬 과다분비 질환이고, 암은 악성종양으로 전혀 다른 질환입니다"
            },
            {
                "mistake": "'Viêm tuyến giáp'으로 번역",
                "correction": "'Cường giáp' 사용",
                "explanation": "Viêm은 염증을 의미하므로 갑상선염이며, 기능항진증과 다릅니다"
            },
            {
                "mistake": "그레이브스병과 구분 없이 통역",
                "correction": "의사에게 확인 후 정확한 병명 전달",
                "explanation": "그레이브스병은 갑상선기능항진증의 원인 중 하나이므로 맥락 파악 필요"
            }
        ],
        "examples": [
            {
                "ko": "갑상선기능항진증으로 인한 빈맥과 체중감소가 관찰됩니다",
                "vi": "Quan sát thấy nhịp tim nhanh và sụt cân do cường giáp",
                "situation": "formal"
            },
            {
                "ko": "항갑상선제 복용 후 증상이 호전되고 있습니다",
                "vi": "Triệu chứng đang cải thiện sau khi uống thuốc kháng giáp",
                "situation": "onsite"
            },
            {
                "ko": "갑기항 때문에 손이 떨리고 잠을 못 자요",
                "vi": "Tay run và mất ngủ vì bệnh cường giáp",
                "situation": "informal"
            }
        ],
        "relatedTerms": ["갑상선기능저하증", "그레이브스병", "갑상선염", "항갑상선제"]
    },
    {
        "slug": "suy-giap",
        "korean": "갑상선기능저하증",
        "vietnamese": "Suy giáp",
        "hanja": "甲狀腺機能低下症",
        "hanjaReading": "甲(갑 갑) + 狀(모양 상) + 腺(샘 선) + 機(틀 기) + 能(능할 능) + 低(낮을 저) + 下(아래 하) + 症(병 증)",
        "pronunciation": "수이잡",
        "meaningKo": "갑상선호르몬이 부족하여 신체 대사가 저하되는 질환입니다. 통역 시 주의할 점은 '피로감, 체중증가, 추위 민감성, 변비' 등의 비특이적 증상이 많아 환자가 증상을 정확히 표현하지 못하는 경우가 많으므로, 통역사가 증상을 명확히 전달해야 합니다. 한국에서는 '하시모토 갑상선염'이 주요 원인이며, 평생 약물 복용이 필요하다는 점을 환자에게 오해 없이 전달해야 합니다.",
        "meaningVi": "Bệnh lý tuyến giáp tiết ít hormone giáp, làm giảm quá trình trao đổi chất. Triệu chứng gồm mệt mỏi, tăng cân, sợ lạnh, táo bón, chậm chạp.",
        "context": "내분비내과 외래 진료 및 갑상선호르몬 대체요법 상담 시",
        "culturalNote": "한국에서는 갑상선기능저하증 진단 후 즉시 호르몬 대체요법을 시작하지만, 베트남 환자들은 약물 의존에 대한 두려움으로 치료를 거부하는 경우가 있습니다. 한국 의료진은 TSH 수치로 정밀 관리하는 반면, 베트남에서는 증상 위주로 치료하는 경향이 있어 통역 시 수치의 중요성을 강조해야 합니다.",
        "commonMistakes": [
            {
                "mistake": "'Ung thư tuyến giáp'으로 오역",
                "correction": "'Suy giáp' 사용",
                "explanation": "기능저하증은 호르몬 부족 질환이고 암과는 전혀 다릅니다"
            },
            {
                "mistake": "임시 약물로 설명",
                "correction": "평생 복용 필요성 강조",
                "explanation": "대부분의 갑상선기능저하증은 영구적이어서 평생 약물 복용이 필요합니다"
            },
            {
                "mistake": "TSH를 '티에스에이치'로 음역",
                "correction": "'Hormone kích thích tuyến giáp' 또는 'TSH' 병기",
                "explanation": "환자 이해도를 높이기 위해 풀네임을 함께 설명해야 합니다"
            }
        ],
        "examples": [
            {
                "ko": "TSH 수치가 높아 갑상선기능저하증으로 진단됩니다",
                "vi": "Chỉ số TSH cao, chẩn đoán suy giáp",
                "situation": "formal"
            },
            {
                "ko": "레보티록신 50마이크로그램을 아침 공복에 복용하세요",
                "vi": "Uống Levothyroxine 50 microgam vào buổi sáng lúc đói",
                "situation": "onsite"
            },
            {
                "ko": "갑저 때문에 너무 피곤하고 살이 쪄요",
                "vi": "Mệt mỏi và tăng cân nhiều vì bệnh suy giáp",
                "situation": "informal"
            }
        ],
        "relatedTerms": ["갑상선기능항진증", "하시모토갑상선염", "레보티록신", "TSH"]
    },
    {
        "slug": "ung-thu-tuyen-giap",
        "korean": "갑상선암",
        "vietnamese": "Ung thư tuyến giáp",
        "hanja": "甲狀腺癌",
        "hanjaReading": "甲(갑 갑) + 狀(모양 상) + 腺(샘 선) + 癌(암 암)",
        "pronunciation": "웅투투옌잡",
        "meaningKo": "갑상선에 발생하는 악성 종양으로, 한국에서 발생률이 매우 높은 암입니다. 통역 시 주의할 점은 '유두암, 여포암, 수질암, 역형성암' 등 조직학적 유형을 정확히 구분해야 하며, 예후가 매우 좋은 암이므로 환자가 과도하게 불안해하지 않도록 의사의 설명을 정확히 전달해야 합니다. 한국은 갑상선암 검진이 활발해 조기 발견율이 높으며, '과잉진단' 논란도 있어 통역 시 이를 이해하고 있어야 합니다.",
        "meaningVi": "Khối u ác tính phát sinh từ tuyến giáp. Tỷ lệ mắc cao ở Hàn Quốc. Thường có tiên lượng tốt nếu phát hiện sớm và điều trị đúng cách.",
        "context": "내분비내과 및 외과 협진, 갑상선암 수술 전후 상담 시",
        "culturalNote": "한국에서는 국가 암검진 프로그램으로 갑상선초음파 검사가 보편화되어 조기 발견율이 세계 최고 수준이지만, 베트남에서는 증상이 나타난 후 진단되는 경우가 많습니다. 한국 환자들은 '암'이라는 단어에 민감하지만 갑상선암은 예후가 좋다는 인식이 있는 반면, 베트남 환자들은 암 진단 자체에 큰 충격을 받으므로 통역 시 의사의 안심시키는 뉘앙스를 잘 전달해야 합니다.",
        "commonMistakes": [
            {
                "mistake": "모든 갑상선암을 'Ung thư tuyến giáp ác tính'으로 번역",
                "correction": "조직학적 유형 정확히 구분 (ung thư nhú, ung thư nang, etc.)",
                "explanation": "유형에 따라 치료법과 예후가 다르므로 정확한 번역 필수"
            },
            {
                "mistake": "갑상선결절과 혼동",
                "correction": "결절(u nang)은 양성일 수 있고 암(ung thư)은 악성",
                "explanation": "결절의 대부분은 양성이므로 환자 불안을 조장하지 않도록 주의"
            },
            {
                "mistake": "예후 정보 생략",
                "correction": "갑상선암은 예후가 좋은 암임을 함께 전달",
                "explanation": "환자 안심을 위해 의사의 긍정적 설명을 정확히 전달해야 함"
            }
        ],
        "examples": [
            {
                "ko": "갑상선 유두암으로 진단되어 갑상선전절제술을 시행할 예정입니다",
                "vi": "Chẩn đoán ung thư nhú tuyến giáp, dự định phẫu thuật cắt toàn bộ tuyến giáp",
                "situation": "formal"
            },
            {
                "ko": "수술 후 방사성요오드 치료가 필요합니다",
                "vi": "Sau phẫu thuật cần điều trị bằng iod phóng xạ",
                "situation": "onsite"
            },
            {
                "ko": "갑상선암은 착한 암이라서 걱정 안 해도 된다고 하더라고요",
                "vi": "Nghe nói ung thư tuyến giáp là loại ung thư lành tính nên không cần lo lắng",
                "situation": "informal"
            }
        ],
        "relatedTerms": ["갑상선결절", "갑상선전절제술", "방사성요오드치료", "갑상선유두암"]
    },
    {
        "slug": "u-nang-tuyen-giap",
        "korean": "갑상선결절",
        "vietnamese": "U nang tuyến giáp",
        "hanja": "甲狀腺結節",
        "hanjaReading": "甲(갑 갑) + 狀(모양 상) + 腺(샘 선) + 結(맺을 결) + 節(마디 절)",
        "pronunciation": "우낭투옌잡",
        "meaningKo": "갑상선에 생긴 혹으로, 대부분 양성이지만 일부는 암일 수 있습니다. 통역 시 주의할 점은 환자들이 '혹=암'으로 오해하는 경우가 많으므로, 양성과 악성을 명확히 구분하여 전달해야 합니다. 한국에서는 초음파 검사로 결절을 발견하는 경우가 많으며, K-TIRADS 분류 체계를 사용하므로 통역사는 이 시스템을 이해하고 환자에게 위험도를 정확히 전달해야 합니다.",
        "meaningVi": "Khối u hoặc nang phát sinh trong tuyến giáp. Phần lớn là lành tính nhưng cần theo dõi và sinh thiết nếu có dấu hiệu nghi ngờ ác tính.",
        "context": "내분비내과 외래, 초음파 검사 결과 설명 및 세침흡인검사 상담 시",
        "culturalNote": "한국에서는 건강검진 시 갑상선초음파가 포함되어 우연히 결절을 발견하는 경우가 많지만, 베트남에서는 목에 만져지는 혹으로 내원하는 경우가 많습니다. 한국 의료진은 크기와 초음파 특성으로 추적관찰 여부를 결정하지만, 베트남 환자들은 '혹'이라는 말에 즉시 수술을 원하는 경우가 있어 통역 시 불필요한 시술을 방지하도록 의사의 설명을 명확히 전달해야 합니다.",
        "commonMistakes": [
            {
                "mistake": "결절을 모두 암으로 설명",
                "correction": "대부분 양성이며 추적관찰 가능함을 강조",
                "explanation": "환자의 불필요한 불안을 방지하기 위해 양성 가능성을 함께 전달"
            },
            {
                "mistake": "'U'와 'Nang'을 구분 없이 사용",
                "correction": "고형 결절은 'U', 낭성 결절은 'Nang'",
                "explanation": "초음파 소견에 따라 정확한 용어 사용 필요"
            },
            {
                "mistake": "세침흡인검사를 '수술'로 오역",
                "correction": "'Sinh thiết kim nhỏ' (바늘 생검)",
                "explanation": "환자가 수술로 오해하여 불필요한 공포심 유발 방지"
            }
        ],
        "examples": [
            {
                "ko": "1cm 크기의 갑상선 결절이 발견되어 세침흡인검사를 권장합니다",
                "vi": "Phát hiện u nang tuyến giáp kích thước 1cm, khuyến cáo sinh thiết kim nhỏ",
                "situation": "formal"
            },
            {
                "ko": "이 결절은 K-TIRADS 3등급으로 6개월 후 추적관찰하면 됩니다",
                "vi": "U nang này thuộc K-TIRADS độ 3, theo dõi lại sau 6 tháng",
                "situation": "onsite"
            },
            {
                "ko": "목에 혹이 만져져서 왔는데 암은 아니죠?",
                "vi": "Tôi sờ thấy u ở cổ, không phải ung thư chứ?",
                "situation": "informal"
            }
        ],
        "relatedTerms": ["갑상선암", "세침흡인검사", "갑상선초음파", "K-TIRADS"]
    },
    {
        "slug": "cuong-can-giap",
        "korean": "부갑상선기능항진증",
        "vietnamese": "Cường cận giáp",
        "hanja": "副甲狀腺機能亢進症",
        "hanjaReading": "副(버금 부) + 甲(갑 갑) + 狀(모양 상) + 腺(샘 선) + 機(틀 기) + 能(능할 능) + 亢(높을 항) + 進(나아갈 진) + 症(병 증)",
        "pronunciation": "꾸엉깐잡",
        "meaningKo": "부갑상선에서 부갑상선호르몬이 과다 분비되어 혈중 칼슘이 증가하는 질환입니다. 통역 시 주의할 점은 '갑상선'과 '부갑상선'을 명확히 구분해야 하며, 고칼슘혈증으로 인한 '신결석, 골다공증, 피로감' 등의 증상을 정확히 전달해야 합니다. 한국에서는 혈액검사에서 우연히 발견되는 경우가 많으며, 수술적 치료가 근본적 해결책이라는 점을 환자에게 오해 없이 설명해야 합니다.",
        "meaningVi": "Bệnh lý tuyến cận giáp tiết quá nhiều hormone cận giáp (PTH), gây tăng canxi máu. Triệu chứng gồm sỏi thận, loãng xương, mệt mỏi, rối loạn tiêu hóa.",
        "context": "내분비내과 외래, 고칼슘혈증 원인 감별 및 수술 전 상담 시",
        "culturalNote": "한국에서는 건강검진에서 혈청 칼슘 수치 이상으로 발견되는 경우가 많지만, 베트남에서는 신결석이나 골절 후 진단되는 경우가 많습니다. 한국 의료진은 부갑상선 종양이 발견되면 수술을 권장하지만, 베트남 환자들은 증상이 없으면 수술을 거부하는 경향이 있어 통역 시 장기적 합병증(골다공증, 신기능 저하)을 명확히 전달해야 합니다.",
        "commonMistakes": [
            {
                "mistake": "갑상선기능항진증과 혼동",
                "correction": "부갑상선(Tuyến cận giáp)은 갑상선(Tuyến giáp)과 다른 기관",
                "explanation": "위치와 기능이 완전히 다른 내분비샘이므로 명확히 구분 필요"
            },
            {
                "mistake": "PTH를 '피티에이치'로만 음역",
                "correction": "'Hormone cận giáp' 또는 'PTH' 병기",
                "explanation": "환자 이해도 향상을 위해 풀네임 함께 설명"
            },
            {
                "mistake": "칼슘 보충제 중단만으로 치료 가능하다고 오해",
                "correction": "근본 원인(종양) 제거 필요성 강조",
                "explanation": "대부분 부갑상선 종양이 원인이므로 수술이 필요함"
            }
        ],
        "examples": [
            {
                "ko": "혈청 칼슘 12mg/dL, PTH 상승으로 부갑상선기능항진증 진단됩니다",
                "vi": "Canxi huyết thanh 12mg/dL, PTH tăng, chẩn đoán cường cận giáp",
                "situation": "formal"
            },
            {
                "ko": "부갑상선 종양 제거 수술이 필요합니다",
                "vi": "Cần phẫu thuật cắt bỏ u tuyến cận giáp",
                "situation": "onsite"
            },
            {
                "ko": "신결석이 자꾸 생겨서 검사했더니 부갑상선 문제래요",
                "vi": "Bị sỏi thận nhiều lần, khám mới biết là do tuyến cận giáp",
                "situation": "informal"
            }
        ],
        "relatedTerms": ["고칼슘혈증", "부갑상선종양", "골다공증", "신결석"]
    },
    {
        "slug": "hoi-chung-cushing",
        "korean": "쿠싱증후군",
        "vietnamese": "Hội chứng Cushing",
        "hanja": None,
        "hanjaReading": None,
        "pronunciation": "호이쯩꾸싱",
        "meaningKo": "부신피질에서 코르티솔이 과다 분비되거나 스테로이드 약물의 장기 사용으로 발생하는 질환입니다. 통역 시 주의할 점은 '달덩이얼굴, 중심성 비만, 피부선조' 등 특징적인 외형 변화를 환자에게 민감하게 전달해야 하며, 스테로이드 약물 복용력을 정확히 확인해야 합니다. 한국에서는 외인성(약물성)이 많고, 내인성인 경우 부신종양이나 뇌하수체종양이 원인이므로 통역 시 구분이 필요합니다.",
        "meaningVi": "Bệnh lý do tuyến thượng thận tiết quá nhiều cortisol hoặc do dùng corticosteroid kéo dài. Triệu chứng đặc trưng: mặt trăng tròn, béo phì trung tâm, rạn da tím, tăng huyết áp.",
        "context": "내분비내과 외래, 비만 및 고혈압 원인 감별, 부신종양 평가 시",
        "culturalNote": "한국에서는 천식, 류마티스 질환 등으로 스테로이드를 장기 복용하는 환자가 많아 외인성 쿠싱증후군이 흔하지만, 베트남에서는 전통 치료를 선호하여 스테로이드 노출이 적을 수 있습니다. 한국 환자들은 외형 변화에 매우 민감하여 조기 진단되지만, 베트남 환자들은 증상이 심해진 후 내원하는 경우가 많아 통역 시 조기 발견의 중요성을 강조해야 합니다.",
        "commonMistakes": [
            {
                "mistake": "'Béo phì'로만 번역",
                "correction": "'Hội chứng Cushing' 정확히 사용",
                "explanation": "단순 비만이 아니라 호르몬 이상 질환임을 명확히 해야 함"
            },
            {
                "mistake": "약물성과 내인성을 구분 않고 통역",
                "correction": "원인에 따라 '외인성(do thuốc)' 또는 '내인성(do u)' 명시",
                "explanation": "치료 방향이 완전히 다르므로 원인 구분 필수"
            },
            {
                "mistake": "코르티솔을 '코티솔'로 음역",
                "correction": "'Cortisol' 또는 'Hormone vỏ thượng thận' 병기",
                "explanation": "환자 이해를 위해 호르몬 기능 함께 설명"
            }
        ],
        "examples": [
            {
                "ko": "쿠싱증후군으로 인한 중심성 비만과 고혈압이 관찰됩니다",
                "vi": "Quan sát thấy béo phì trung tâm và tăng huyết áp do hội chứng Cushing",
                "situation": "formal"
            },
            {
                "ko": "스테로이드 복용을 서서히 줄여야 합니다",
                "vi": "Cần giảm liều corticosteroid từ từ",
                "situation": "onsite"
            },
            {
                "ko": "얼굴이 자꾸 붓고 살이 쪄서 검사받았어요",
                "vi": "Mặt sưng và tăng cân nhiều nên đi khám",
                "situation": "informal"
            }
        ],
        "relatedTerms": ["부신종양", "코르티솔", "스테로이드", "부신피질자극호르몬"]
    },
    {
        "slug": "benh-addison",
        "korean": "에디슨병",
        "vietnamese": "Bệnh Addison",
        "hanja": None,
        "hanjaReading": None,
        "pronunciation": "벵아디손",
        "meaningKo": "부신피질에서 코르티솔과 알도스테론이 부족하게 분비되는 만성 질환입니다. 통역 시 주의할 점은 '피로감, 저혈압, 피부색소침착' 등의 증상이 비특이적이어서 진단이 늦어질 수 있으므로, 환자의 증상을 자세히 청취하고 전달해야 합니다. 한국에서는 자가면역성이 가장 흔한 원인이며, 스트레스 상황에서 부신위기가 올 수 있어 평생 호르몬 대체요법이 필요하다는 점을 환자에게 명확히 전달해야 합니다.",
        "meaningVi": "Bệnh lý mạn tính do tuyến thượng thận không tiết đủ cortisol và aldosterone. Triệu chứng: mệt mỏi, hạ huyết áp, da sẫm màu, buồn nôn, giảm cân.",
        "context": "내분비내과 외래, 만성 피로 및 저혈압 원인 감별, 부신위기 응급 상황",
        "culturalNote": "한국에서는 자가면역 질환에 대한 인식이 높아 조기 진단이 가능하지만, 베트남에서는 '결핵성 부신염'이 상대적으로 많을 수 있습니다. 한국 환자들은 평생 약물 복용에 대한 이해도가 높지만, 베트남 환자들은 증상이 호전되면 약을 중단하는 경우가 있어 통역 시 약물 중단의 위험성(부신위기)을 강조해야 합니다. 또한 스트레스 상황(수술, 감염)에서 용량 조절이 필요함을 명확히 전달해야 합니다.",
        "commonMistakes": [
            {
                "mistake": "'Mệt mỏi mạn tính'으로만 설명",
                "correction": "'Bệnh Addison' 정확한 병명 사용",
                "explanation": "단순 피로가 아니라 호르몬 결핍 질환임을 명확히 해야 함"
            },
            {
                "mistake": "일시적 약물 복용으로 오해",
                "correction": "평생 호르몬 대체요법 필요성 강조",
                "explanation": "약물 중단 시 생명을 위협하는 부신위기 발생 가능"
            },
            {
                "mistake": "부신위기를 '응급상황'으로만 번역",
                "correction": "'Cơn suy thượng thận cấp' 구체적 용어 사용",
                "explanation": "환자와 보호자가 위험성을 정확히 인지하도록 해야 함"
            }
        ],
        "examples": [
            {
                "ko": "에디슨병으로 하이드로코티손과 플루드로코티손 복용이 필요합니다",
                "vi": "Bệnh Addison cần uống hydrocortisone và fludrocortisone",
                "situation": "formal"
            },
            {
                "ko": "수술 받을 때는 스테로이드 용량을 늘려야 합니다",
                "vi": "Khi phẫu thuật cần tăng liều corticosteroid",
                "situation": "onsite"
            },
            {
                "ko": "계속 피곤하고 어지러운데 에디슨병이 맞나요?",
                "vi": "Luôn mệt mỏi và chóng mặt, có phải bệnh Addison không?",
                "situation": "informal"
            }
        ],
        "relatedTerms": ["부신피질부전", "부신위기", "하이드로코티손", "자가면역질환"]
    },
    {
        "slug": "u-to-crom",
        "korean": "갈색세포종",
        "vietnamese": "U tế bào ưa crom",
        "hanja": "褐色細胞腫",
        "hanjaReading": "褐(갈색 갈) + 色(빛 색) + 細(가늘 세) + 胞(세포 포) + 腫(부을 종)",
        "pronunciation": "우떼바오우아끄롬",
        "meaningKo": "부신수질에서 발생하는 종양으로 카테콜아민을 과다 분비하여 발작성 고혈압을 일으키는 질환입니다. 통역 시 주의할 점은 '두통, 심계항진, 발한' 등의 3대 증상을 정확히 전달해야 하며, 발작성 증상의 특징을 환자가 이해하도록 설명해야 합니다. 한국에서는 이차성 고혈압의 원인 감별 과정에서 발견되며, 수술 전 알파차단제로 혈압을 조절하는 것이 필수적이라는 점을 환자에게 오해 없이 전달해야 합니다.",
        "meaningVi": "Khối u phát sinh từ tủy thượng thận, tiết quá nhiều catecholamine gây tăng huyết áp kịch phát. Tam chứng đặc trưng: đau đầu, đánh trống ngực, vã mồ hôi.",
        "context": "내분비내과 및 외과 협진, 이차성 고혈압 감별, 수술 전 준비 상담",
        "culturalNote": "한국에서는 고혈압 환자 중 젊은 연령이거나 약물 치료에 잘 반응하지 않는 경우 갈색세포종 검사를 시행하지만, 베트남에서는 검사 접근성이 낮아 진단이 늦어질 수 있습니다. 한국 의료진은 수술 전 알파차단제로 2-4주간 혈압 조절을 필수로 하지만, 베트남 환자들은 수술을 서두르는 경향이 있어 통역 시 수술 전 준비의 중요성(수술 중 고혈압 위기 방지)을 명확히 전달해야 합니다.",
        "commonMistakes": [
            {
                "mistake": "'U thượng thận'으로만 번역",
                "correction": "'U tế bào ưa crom' 정확한 용어 사용",
                "explanation": "부신종양에는 여러 종류가 있으므로 정확한 병명 필요"
            },
            {
                "mistake": "카테콜아민을 '까떼꼴라민'으로만 음역",
                "correction": "'Catecholamine (adrenaline, noradrenaline)' 설명",
                "explanation": "환자 이해를 위해 구체적 호르몬명 함께 제시"
            },
            {
                "mistake": "즉시 수술 가능하다고 오역",
                "correction": "수술 전 알파차단제로 혈압 조절 필수임을 강조",
                "explanation": "준비 없이 수술 시 고혈압 위기로 생명 위험"
            }
        ],
        "examples": [
            {
                "ko": "24시간 소변 메타네프린 검사에서 갈색세포종이 의심됩니다",
                "vi": "Xét nghiệm metanephrine nước tiểu 24 giờ nghi ngờ u tế bào ưa crom",
                "situation": "formal"
            },
            {
                "ko": "수술 전 2주간 알파차단제 복용이 필요합니다",
                "vi": "Cần uống thuốc chẹn alpha 2 tuần trước phẫu thuật",
                "situation": "onsite"
            },
            {
                "ko": "갑자기 혈압이 확 올라가고 식은땀 나는 증상이 자주 있어요",
                "vi": "Thường xuyên bị tăng huyết áp đột ngột và vã mồ hôi lạnh",
                "situation": "informal"
            }
        ],
        "relatedTerms": ["부신종양", "카테콜아민", "이차성고혈압", "알파차단제"]
    },
    {
        "slug": "loang-xuong",
        "korean": "골다공증",
        "vietnamese": "Loãng xương",
        "hanja": "骨多孔症",
        "hanjaReading": "骨(뼈 골) + 多(많을 다) + 孔(구멍 공) + 症(병 증)",
        "pronunciation": "로앙쑤엉",
        "meaningKo": "뼈의 밀도가 감소하고 미세구조가 약해져 골절 위험이 증가하는 질환입니다. 통역 시 주의할 점은 '골밀도 T-점수'의 의미를 환자가 이해하도록 설명해야 하며, 골다공증은 증상이 없다가 골절로 발현되므로 예방적 치료의 중요성을 강조해야 합니다. 한국에서는 폐경 후 여성에서 검진이 활발하며, 비스포스포네이트 등 약물 치료와 함께 칼슘, 비타민D 보충이 필수적이라는 점을 환자에게 오해 없이 전달해야 합니다.",
        "meaningVi": "Bệnh lý giảm mật độ xương và suy yếu vi cấu trúc xương, tăng nguy cơ gãy xương. Thường không có triệu chứng cho đến khi xảy ra gãy xương.",
        "context": "내분비내과 외래, 폐경 후 여성 검진, 골절 위험 평가 및 약물 치료 상담",
        "culturalNote": "한국에서는 국가 건강검진에 골밀도 검사가 포함되어 폐경 후 여성의 조기 발견율이 높지만, 베트남에서는 골절이 발생한 후 진단되는 경우가 많습니다. 한국 환자들은 약물 부작용(턱뼈괴사)에 대한 우려로 치료를 거부하는 경우가 있고, 베트남 환자들은 칼슘 보충만으로 충분하다고 생각하는 경향이 있어 통역 시 약물 치료의 필요성과 부작용의 실제 발생률을 균형 있게 전달해야 합니다.",
        "commonMistakes": [
            {
                "mistake": "T-점수를 숫자로만 전달",
                "correction": "'-2.5 이하는 골다공증'이라는 기준 함께 설명",
                "explanation": "환자가 자신의 상태를 이해할 수 있도록 해석 필요"
            },
            {
                "mistake": "'Thiếu canxi'로만 번역",
                "correction": "'Loãng xương' 정확한 병명 사용",
                "explanation": "단순 칼슘 부족이 아니라 뼈 질환임을 명확히 해야 함"
            },
            {
                "mistake": "칼슘 보충만으로 치료 가능하다고 오해",
                "correction": "비스포스포네이트 등 약물 치료 필요성 강조",
                "explanation": "진행된 골다공증은 칼슘만으로 충분하지 않음"
            }
        ],
        "examples": [
            {
                "ko": "골밀도 T-점수 -3.0으로 골다공증 진단되어 비스포스포네이트 처방합니다",
                "vi": "Chỉ số T-score -3.0, chẩn đoán loãng xương, kê đơn bisphosphonate",
                "situation": "formal"
            },
            {
                "ko": "칼슘 하루 1000mg, 비타민D 보충하시고 주 3회 운동하세요",
                "vi": "Bổ sung canxi 1000mg/ngày, vitamin D và tập thể dục 3 lần/tuần",
                "situation": "onsite"
            },
            {
                "ko": "골다공증 약 먹으면 턱뼈가 썩는다던데 사실인가요?",
                "vi": "Nghe nói uống thuốc loãng xương sẽ làm xương hàm bị hoại tử, có đúng không?",
                "situation": "informal"
            }
        ],
        "relatedTerms": ["골밀도검사", "비스포스포네이트", "골절", "폐경후골다공증"]
    },
    {
        "slug": "benh-gut",
        "korean": "통풍",
        "vietnamese": "Bệnh gút",
        "hanja": "痛風",
        "hanjaReading": "痛(아플 통) + 風(바람 풍)",
        "pronunciation": "벵궛",
        "meaningKo": "요산이 관절에 침착되어 급성 염증성 관절염을 일으키는 질환입니다. 통역 시 주의할 점은 '엄지발가락 첫 관절'에 호발하는 특징과 극심한 통증을 정확히 전달해야 하며, 급성기 치료와 만성기 요산 강하 치료를 구분하여 설명해야 합니다. 한국에서는 식습관(고기, 술)과 관련이 깊어 생활습관 교정이 중요하며, 통증이 없을 때도 요산 강하제를 지속 복용해야 한다는 점을 환자에게 오해 없이 전달해야 합니다.",
        "meaningVi": "Bệnh lý do axit uric lắng đọng trong khớp gây viêm khớp cấp tính. Đặc trưng: đau khớp ngón chân cái dữ dội, sưng đỏ, thường xảy ra đêm khuya.",
        "context": "내분비내과 및 류마티스내과 외래, 급성 통풍 발작, 만성 요산 관리",
        "culturalNote": "한국에서는 회식 문화와 음주가 흔해 통풍 환자가 증가하고 있으며, 환자들은 '술 때문'이라는 인식이 강합니다. 베트남에서는 해산물과 맥주 소비가 많은 지역에서 통풍이 흔하며, 전통적으로 '바람이 들어온 병'이라는 인식이 있어 서양 의학적 설명을 명확히 전달해야 합니다. 한국 환자들은 급성기에만 약을 먹고 중단하는 경우가 많아 통역 시 장기 치료의 필요성을 강조해야 합니다.",
        "commonMistakes": [
            {
                "mistake": "'Viêm khớp'으로만 번역",
                "correction": "'Bệnh gút' 정확한 병명 사용",
                "explanation": "다른 관절염과 구별되는 요산 침착 질환임을 명확히"
            },
            {
                "mistake": "급성기 약과 만성기 약을 구분 않고 설명",
                "correction": "콜히친/NSAID(급성)와 알로퓨리놀(만성) 구분",
                "explanation": "치료 목적과 시기가 다르므로 명확한 설명 필요"
            },
            {
                "mistake": "통증 없으면 약 중단해도 된다고 오해",
                "correction": "요산 강하제는 평생 복용 필요성 강조",
                "explanation": "약 중단 시 요산 재축적으로 재발 위험"
            }
        ],
        "examples": [
            {
                "ko": "요산 수치 9.5mg/dL로 통풍 진단되어 알로퓨리놀 처방합니다",
                "vi": "Chỉ số axit uric 9.5mg/dL, chẩn đoán bệnh gút, kê đơn allopurinol",
                "situation": "formal"
            },
            {
                "ko": "맥주, 내장, 해산물 섭취를 줄이고 물을 많이 드세요",
                "vi": "Giảm bia, nội tạng, hải sản và uống nhiều nước",
                "situation": "onsite"
            },
            {
                "ko": "새벽에 엄지발가락이 너무 아파서 잠을 못 잤어요",
                "vi": "Sáng sớm đau ngón chân cái quá không ngủ được",
                "situation": "informal"
            }
        ],
        "relatedTerms": ["고요산혈증", "알로퓨리놀", "콜히친", "요산강하제"]
    },
    {
        "slug": "tang-axit-uric-mau",
        "korean": "고요산혈증",
        "vietnamese": "Tăng axit uric máu",
        "hanja": "高尿酸血症",
        "hanjaReading": "高(높을 고) + 尿(오줌 뇨) + 酸(신맛 산) + 血(피 혈) + 症(병 증)",
        "pronunciation": "땅앗싯우릭머우",
        "meaningKo": "혈중 요산 수치가 정상보다 높은 상태로, 통풍의 원인이 됩니다. 통역 시 주의할 점은 고요산혈증이 있어도 모두 통풍이 되는 것은 아니며, 무증상 고요산혈증의 경우 생활습관 교정을 우선한다는 점을 환자에게 명확히 전달해야 합니다. 한국에서는 건강검진에서 우연히 발견되는 경우가 많으며, 요산 수치가 높으면 신장 결석과 만성 신질환 위험도 증가한다는 점을 오해 없이 설명해야 합니다.",
        "meaningVi": "Tình trạng nồng độ axit uric trong máu cao hơn bình thường (nam >7mg/dL, nữ >6mg/dL). Có thể không có triệu chứng hoặc gây bệnh gút, sỏi thận.",
        "context": "내분비내과 외래, 건강검진 결과 상담, 통풍 예방 교육",
        "culturalNote": "한국에서는 건강검진 문화가 발달해 무증상 고요산혈증을 조기 발견하지만, 베트남에서는 통풍 발작 후 검사하여 발견되는 경우가 많습니다. 한국 환자들은 '수치가 높다'는 것에 불안해하며 즉시 약물 치료를 원하지만, 무증상이면 생활습관 교정을 우선하는 것이 원칙입니다. 베트남 환자들은 전통 약초 치료를 선호하는 경향이 있어 통역 시 식이 조절의 과학적 근거를 명확히 전달해야 합니다.",
        "commonMistakes": [
            {
                "mistake": "고요산혈증 = 통풍으로 오역",
                "correction": "고요산혈증은 통풍의 위험인자일 뿐 통풍과 다름",
                "explanation": "무증상 고요산혈증 환자 불안 방지"
            },
            {
                "mistake": "즉시 약물 치료 필요하다고 오해",
                "correction": "무증상이면 생활습관 교정 우선",
                "explanation": "불필요한 약물 투여 방지"
            },
            {
                "mistake": "요산을 '유산'으로 오역",
                "correction": "'Axit uric' 정확한 용어 사용",
                "explanation": "요산(uric acid)과 젖산(lactic acid)은 다른 물질"
            }
        ],
        "examples": [
            {
                "ko": "요산 수치 8.2mg/dL로 고요산혈증이지만 증상이 없어 생활습관 교정을 권장합니다",
                "vi": "Axit uric 8.2mg/dL, tăng axit uric máu nhưng không triệu chứng nên khuyến cáo thay đổi lối sống",
                "situation": "formal"
            },
            {
                "ko": "퓨린이 많은 음식을 줄이고 하루 물 2리터 드세요",
                "vi": "Giảm thực phẩm giàu purine và uống 2 lít nước mỗi ngày",
                "situation": "onsite"
            },
            {
                "ko": "검진에서 요산이 높다는데 통풍약 먹어야 하나요?",
                "vi": "Khám định kỳ axit uric cao, có cần uống thuốc gút không?",
                "situation": "informal"
            }
        ],
        "relatedTerms": ["통풍", "요산강하제", "퓨린", "신결석"]
    },
    {
        "slug": "hoi-chung-chuyen-hoa",
        "korean": "대사증후군",
        "vietnamese": "Hội chứng chuyển hóa",
        "hanja": "代謝症候群",
        "hanjaReading": "代(대신할 대) + 謝(사례할 사) + 症(병 증) + 候(기후 후) + 群(무리 군)",
        "pronunciation": "호이쯩쭈옌호아",
        "meaningKo": "복부비만, 고혈압, 고혈당, 이상지질혈증이 동시에 나타나는 상태로 심혈관질환과 당뇨병 위험을 증가시킵니다. 통역 시 주의할 점은 5가지 기준 중 3가지 이상일 때 진단하며, 각 항목의 기준치를 정확히 전달해야 합니다. 한국에서는 '대증'으로 줄여 부르기도 하며, 생활습관 개선(식이, 운동)이 가장 중요한 치료이지만 환자들은 약물 치료를 선호하는 경향이 있어 통역 시 생활습관 교정의 중요성을 강조해야 합니다.",
        "meaningVi": "Tình trạng xuất hiện đồng thời béo bụng, tăng huyết áp, đường huyết cao, rối loạn lipid máu, tăng nguy cơ bệnh tim mạch và đái tháo đường. Chẩn đoán khi có từ 3/5 tiêu chí.",
        "context": "내분비내과 외래, 건강검진 결과 상담, 심혈관 위험도 평가",
        "culturalNote": "한국에서는 건강검진 문화가 발달해 대사증후군을 조기 발견하지만, 환자들은 '병'이라기보다 '건강 주의 상태'로 인식하여 치료에 소극적입니다. 베트남에서는 최근 도시화로 대사증후군이 증가하고 있으며, 전통적인 마른 체형 선호로 복부비만을 문제로 인식하지 못하는 경우가 있어 통역 시 허리둘레 기준의 중요성을 강조해야 합니다. 한국 기준(남 90cm, 여 85cm)과 아시아 기준을 명확히 전달해야 합니다.",
        "commonMistakes": [
            {
                "mistake": "'Béo phì'로만 번역",
                "correction": "'Hội chứng chuyển hóa' 정확한 용어 사용",
                "explanation": "단순 비만이 아니라 여러 대사 이상이 동반된 증후군"
            },
            {
                "mistake": "5가지 기준을 모두 만족해야 한다고 오해",
                "correction": "3가지 이상이면 진단",
                "explanation": "진단 기준 정확한 전달로 환자 이해도 향상"
            },
            {
                "mistake": "약물 치료가 우선이라고 설명",
                "correction": "생활습관 개선이 1차 치료",
                "explanation": "불필요한 약물 투여 방지 및 근본적 치료 유도"
            }
        ],
        "examples": [
            {
                "ko": "허리둘레 95cm, 혈압 140/90, 공복혈당 110으로 대사증후군 진단됩니다",
                "vi": "Vòng eo 95cm, huyết áp 140/90, đường huyết đói 110, chẩn đoán hội chứng chuyển hóa",
                "situation": "formal"
            },
            {
                "ko": "하루 30분 빠르게 걷기와 탄수화물 줄이기를 시작하세요",
                "vi": "Bắt đầu đi bộ nhanh 30 phút/ngày và giảm carbohydrate",
                "situation": "onsite"
            },
            {
                "ko": "검진 결과 대증이라는데 이게 뭔가요?",
                "vi": "Kết quả khám nói hội chứng chuyển hóa, đó là gì?",
                "situation": "informal"
            }
        ],
        "relatedTerms": ["복부비만", "당뇨병", "고혈압", "이상지질혈증"]
    },
    {
        "slug": "khang-insulin",
        "korean": "인슐린저항성",
        "vietnamese": "Kháng insulin",
        "hanja": None,
        "hanjaReading": None,
        "pronunciation": "카잉인술린",
        "meaningKo": "세포가 인슐린에 정상적으로 반응하지 않아 혈당 조절에 더 많은 인슐린이 필요한 상태입니다. 통역 시 주의할 점은 제2형 당뇨병의 주요 원인이며, 비만과 밀접한 관련이 있다는 점을 환자에게 명확히 전달해야 합니다. 한국에서는 HOMA-IR 수치로 평가하며, 체중 감량과 운동이 가장 효과적인 개선 방법이라는 점을 환자가 오해 없이 이해하도록 통역해야 합니다. 메트포르민 등 약물 치료도 가능하다는 점도 전달해야 합니다.",
        "meaningVi": "Tình trạng tế bào không đáp ứng bình thường với insulin, cần nhiều insulin hơn để kiểm soát đường huyết. Nguyên nhân chính gây đái tháo đường type 2, liên quan mật thiết với béo phì.",
        "context": "내분비내과 외래, 당뇨병 전단계 평가, 비만 치료 상담",
        "culturalNote": "한국에서는 건강검진에서 공복혈당과 함께 인슐린 수치를 측정하여 인슐린저항성을 평가하지만, 베트남에서는 검사 접근성이 낮을 수 있습니다. 한국 환자들은 '저항성'이라는 용어를 어려워하므로 '인슐린이 제대로 작동하지 않는 상태'로 풀어서 설명하는 것이 좋습니다. 베트남 환자들은 체중 감량을 당장 실천하기 어려워하므로 통역 시 단계적 목표(3개월에 5% 감량)를 명확히 제시해야 합니다.",
        "commonMistakes": [
            {
                "mistake": "인슐린 부족으로 오역",
                "correction": "인슐린은 있지만 작동이 안 되는 상태",
                "explanation": "인슐린 결핍과 저항성은 다른 개념"
            },
            {
                "mistake": "'Thiếu insulin'으로 번역",
                "correction": "'Kháng insulin' 사용",
                "explanation": "부족(thiếu)이 아니라 저항(kháng)이 핵심"
            },
            {
                "mistake": "약물 치료만 강조",
                "correction": "체중 감량과 운동이 1차 치료임을 명확히",
                "explanation": "생활습관 개선이 가장 효과적인 치료"
            }
        ],
        "examples": [
            {
                "ko": "HOMA-IR 3.5로 인슐린저항성이 확인되어 메트포르민 처방합니다",
                "vi": "HOMA-IR 3.5 xác nhận kháng insulin, kê đơn metformin",
                "situation": "formal"
            },
            {
                "ko": "3개월간 체중 5% 감량을 목표로 하세요",
                "vi": "Mục tiêu giảm 5% cân nặng trong 3 tháng",
                "situation": "onsite"
            },
            {
                "ko": "인슐린 저항성이 있으면 당뇨병 되나요?",
                "vi": "Kháng insulin có bị đái tháo đường không?",
                "situation": "informal"
            }
        ],
        "relatedTerms": ["제2형당뇨병", "대사증후군", "메트포르민", "HOMA-IR"]
    },
    {
        "slug": "dai-thao-duong-type-1",
        "korean": "제1형당뇨병",
        "vietnamese": "Đái tháo đường type 1",
        "hanja": "第一型糖尿病",
        "hanjaReading": "第(차례 제) + 一(한 일) + 型(모형 형) + 糖(엿 당) + 尿(오줌 뇨) + 病(병 병)",
        "pronunciation": "다이타오두엉타입원",
        "meaningKo": "자가면역 반응으로 췌장의 베타세포가 파괴되어 인슐린을 전혀 분비하지 못하는 당뇨병입니다. 통역 시 주의할 점은 소아청소년기에 발병하지만 성인에서도 발병 가능하며, 평생 인슐린 주사가 필수적이라는 점을 환자와 보호자에게 명확히 전달해야 합니다. 한국에서는 제2형에 비해 드물지만 최근 증가 추세이며, '당뇨'라는 용어가 제2형과 혼동을 일으킬 수 있어 통역 시 두 유형의 차이를 정확히 설명해야 합니다.",
        "meaningVi": "Bệnh đái tháo đường do phản ứng tự miễn phá hủy tế bào beta tuyến tụy, không tiết insulin. Thường khởi phát ở trẻ em thanh thiếu niên, cần tiêm insulin suốt đời.",
        "context": "소아내분비내과 및 내분비내과 외래, 신규 진단 상담, 인슐린 펌프 교육",
        "culturalNote": "한국에서는 소아 제1형 당뇨병 환자에게 지속혈당측정기(CGM)와 인슐린 펌프 보급이 증가하고 있지만, 베트남에서는 접근성이 제한적일 수 있습니다. 한국 보호자들은 '완치'를 기대하는 경우가 많아 평생 치료가 필요하다는 점을 수용하는 데 시간이 걸리며, 베트남에서는 전통 의학으로 치료하려는 시도가 있을 수 있어 통역 시 인슐린 치료의 절대적 필요성을 강조해야 합니다.",
        "commonMistakes": [
            {
                "mistake": "제2형 당뇨병과 구분 없이 통역",
                "correction": "자가면역 질환으로 인슐린 절대 부족임을 강조",
                "explanation": "치료법이 완전히 다르므로 명확한 구분 필수"
            },
            {
                "mistake": "식이조절만으로 관리 가능하다고 오해",
                "correction": "반드시 인슐린 주사 필요",
                "explanation": "인슐린 없이는 생명 유지 불가능"
            },
            {
                "mistake": "'Đái tháo đường trẻ em'으로만 번역",
                "correction": "'Đái tháo đường type 1' 정확한 용어 사용",
                "explanation": "성인에서도 발병 가능하므로 연령으로 구분 부적절"
            }
        ],
        "examples": [
            {
                "ko": "항-GAD 항체 양성으로 제1형 당뇨병 진단되어 인슐린 치료를 시작합니다",
                "vi": "Kháng thể anti-GAD dương tính, chẩn đoán đái tháo đường type 1, bắt đầu điều trị insulin",
                "situation": "formal"
            },
            {
                "ko": "속효성 인슐린을 식사 직전에, 지속형 인슐린을 자기 전에 주사하세요",
                "vi": "Tiêm insulin tác dụng nhanh trước bữa ăn, insulin kéo dài trước khi ngủ",
                "situation": "onsite"
            },
            {
                "ko": "우리 아이 1형 당뇨인데 나중에 완치되나요?",
                "vi": "Con tôi bị đái tháo đường type 1, sau này có khỏi được không?",
                "situation": "informal"
            }
        ],
        "relatedTerms": ["제2형당뇨병", "인슐린", "자가면역질환", "지속혈당측정기"]
    },
    {
        "slug": "dai-thao-duong-type-2",
        "korean": "제2형당뇨병",
        "vietnamese": "Đái tháo đường type 2",
        "hanja": "第二型糖尿病",
        "hanjaReading": "第(차례 제) + 二(두 이) + 型(모형 형) + 糖(엿 당) + 尿(오줌 뇨) + 病(병 병)",
        "pronunciation": "다이타오두엉타입투",
        "meaningKo": "인슐린 저항성과 상대적 인슐린 부족으로 발생하는 당뇨병으로, 전체 당뇨병의 90% 이상을 차지합니다. 통역 시 주의할 점은 비만, 운동 부족, 가족력과 관련이 깊으며, 초기에는 생활습관 개선과 경구약으로 조절 가능하지만 진행하면 인슐린이 필요할 수 있다는 점을 환자에게 명확히 전달해야 합니다. 한국에서는 '당뇨'라고 하면 보통 제2형을 의미하며, 합병증 예방을 위한 혈당 목표치(HbA1c 6.5% 미만)를 정확히 전달해야 합니다.",
        "meaningVi": "Bệnh đái tháo đường do kháng insulin và thiếu insulin tương đối, chiếm >90% bệnh nhân đái tháo đường. Liên quan béo phì, ít vận động, di truyền. Có thể kiểm soát bằng thay đổi lối sống và thuốc uống ban đầu.",
        "context": "내분비내과 외래, 신규 진단 상담, 당뇨병 합병증 검진",
        "culturalNote": "한국에서는 국가 건강검진으로 공복혈당과 HbA1c를 측정하여 조기 진단이 가능하지만, 베트남에서는 증상(다음, 다식, 다뇨)이 나타난 후 진단되는 경우가 많습니다. 한국 환자들은 '당뇨는 불치병'이라는 인식으로 진단 초기 우울증을 겪는 경우가 많고, 베트남 환자들은 약물 의존을 꺼려 전통 약재로 치료하려는 경향이 있어 통역 시 현대 의학적 치료의 효과와 합병증 예방의 중요성을 강조해야 합니다.",
        "commonMistakes": [
            {
                "mistake": "제1형과 구분 없이 '당뇨병'으로만 번역",
                "correction": "'Đái tháo đường type 2' 명시",
                "explanation": "치료 접근이 다르므로 유형 구분 필수"
            },
            {
                "mistake": "인슐린 치료는 절대 필요 없다고 설명",
                "correction": "진행하면 인슐린 필요 가능성 언급",
                "explanation": "환자가 미래 치료 변화에 대비하도록"
            },
            {
                "mistake": "HbA1c를 '에이치비에이원씨'로만 음역",
                "correction": "'Đường huyết trung bình 3 tháng' 또는 'HbA1c' 병기",
                "explanation": "환자 이해도 향상을 위해 의미 함께 설명"
            }
        ],
        "examples": [
            {
                "ko": "공복혈당 145mg/dL, HbA1c 7.2%로 제2형 당뇨병 진단되어 메트포르민 처방합니다",
                "vi": "Đường huyết đói 145mg/dL, HbA1c 7.2%, chẩn đoán đái tháo đường type 2, kê đơn metformin",
                "situation": "formal"
            },
            {
                "ko": "하루 세 끼 규칙적으로 먹고 탄수화물 양을 줄이세요",
                "vi": "Ăn đều đặn 3 bữa/ngày và giảm lượng carbohydrate",
                "situation": "onsite"
            },
            {
                "ko": "당뇨약 먹으면 평생 먹어야 하나요?",
                "vi": "Uống thuốc đái tháo đường có phải uống suốt đời không?",
                "situation": "informal"
            }
        ],
        "relatedTerms": ["인슐린저항성", "메트포르민", "HbA1c", "당뇨병합병증"]
    },
    {
        "slug": "benh-than-kinh-dai-thao-duong",
        "korean": "당뇨병성신경병증",
        "vietnamese": "Bệnh thần kinh đái tháo đường",
        "hanja": "糖尿病性神經病症",
        "hanjaReading": "糖(엿 당) + 尿(오줌 뇨) + 病(병 병) + 性(성품 성) + 神(귀신 신) + 經(경서 경) + 病(병 병) + 症(병 증)",
        "pronunciation": "벵탄낑다이타오두엉",
        "meaningKo": "당뇨병으로 인한 고혈당이 지속되어 신경이 손상되는 합병증입니다. 통역 시 주의할 점은 '발저림, 통증, 감각 저하' 등의 증상을 정확히 전달해야 하며, 족부 궤양으로 진행할 수 있어 발 관리의 중요성을 강조해야 합니다. 한국에서는 정기적인 신경전도검사와 발 검진을 시행하며, 통증 조절을 위한 약물(프레가발린 등)과 함께 엄격한 혈당 조절이 필수적이라는 점을 환자에게 오해 없이 전달해야 합니다.",
        "meaningVi": "Biến chứng đái tháo đường do đường huyết cao kéo dài làm tổn thương thần kinh. Triệu chứng: tê bì, đau, giảm cảm giác chân, có thể dẫn đến loét bàn chân.",
        "context": "내분비내과 외래, 당뇨병 합병증 검진, 신경과 협진",
        "culturalNote": "한국에서는 당뇨병 진단 시부터 합병증 검진 교육을 받지만, 베트남에서는 증상이 나타난 후 합병증을 인지하는 경우가 많습니다. 한국 환자들은 발저림을 단순 노화로 생각하여 방치하다가 족부궤양으로 악화되는 경우가 있고, 베트남 환자들은 전통 마사지나 침술로 증상을 완화하려는 경향이 있어 통역 시 서양 의학적 통증 관리의 효과를 명확히 전달해야 합니다. 매일 발을 확인하는 습관의 중요성을 강조해야 합니다.",
        "commonMistakes": [
            {
                "mistake": "'Tê chân'으로만 번역",
                "correction": "'Bệnh thần kinh đái tháo đường' 정확한 병명 사용",
                "explanation": "단순 저림이 아니라 당뇨 합병증임을 명확히"
            },
            {
                "mistake": "통증약만 처방하면 된다고 오해",
                "correction": "혈당 조절이 가장 중요한 치료임을 강조",
                "explanation": "근본 원인 해결 없이 증상만 완화하면 진행"
            },
            {
                "mistake": "발 관리 교육 생략",
                "correction": "매일 발 확인, 적절한 신발, 상처 즉시 치료",
                "explanation": "족부궤양 예방을 위한 환자 교육 필수"
            }
        ],
        "examples": [
            {
                "ko": "양측 발에 당뇨병성 신경병증으로 프레가발린 처방하고 엄격한 혈당 조절을 권장합니다",
                "vi": "Bệnh thần kinh đái tháo đường cả hai bàn chân, kê đơn pregabalin và khuyến cáo kiểm soát đường huyết chặt chẽ",
                "situation": "formal"
            },
            {
                "ko": "매일 발을 확인하고 상처가 생기면 즉시 내원하세요",
                "vi": "Kiểm tra chân mỗi ngày, nếu có vết thương hãy đến ngay",
                "situation": "onsite"
            },
            {
                "ko": "발이 저리고 아픈데 당뇨 때문인가요?",
                "vi": "Chân tê và đau, có phải do đái tháo đường không?",
                "situation": "informal"
            }
        ],
        "relatedTerms": ["당뇨병합병증", "족부궤양", "프레가발린", "신경전도검사"]
    },
    {
        "slug": "nhiễm-acid-keto-dai-thao-duong",
        "korean": "당뇨병성케톤산증",
        "vietnamese": "Nhiễm axit keto đái tháo đường",
        "hanja": "糖尿病性케톤酸症",
        "hanjaReading": "糖(엿 당) + 尿(오줌 뇨) + 病(병 병) + 性(성품 성) + 酸(신맛 산) + 症(병 증)",
        "pronunciation": "니엠앗싯께토다이타오두엉",
        "meaningKo": "인슐린 절대 부족으로 체내 케톤체가 축적되어 산혈증을 일으키는 당뇨병의 급성 합병증입니다. 통역 시 주의할 점은 생명을 위협하는 응급 상황이며, '구역, 구토, 복통, 과호흡, 의식 저하' 등의 증상을 신속히 파악하여 전달해야 합니다. 한국에서는 제1형 당뇨병 환자에서 주로 발생하지만 제2형에서도 스트레스 상황(감염, 수술)에서 발생 가능하며, 즉시 응급실 내원과 수액 및 인슐린 치료가 필수적이라는 점을 환자와 보호자에게 명확히 전달해야 합니다.",
        "meaningVi": "Biến chứng cấp tính đái tháo đường do thiếu insulin tuyệt đối, tích tụ thể ketone gây toan máu. Nguy hiểm đến tính mạng. Triệu chứng: buồn nôn, nôn, đau bụng, thở nhanh sâu, rối loạn ý thức.",
        "context": "응급실, 내분비내과 입원, 제1형 당뇨병 교육",
        "culturalNote": "한국에서는 제1형 당뇨병 환자와 보호자가 진단 시 케톤산증 예방 교육을 받지만, 베트남에서는 교육 기회가 제한적일 수 있습니다. 한국 환자들은 '병원 가기 전 집에서 해결하려는' 경향이 있어 증상 악화를 초래하고, 베트남 환자들은 전통 치료를 먼저 시도하여 내원이 지연될 수 있어 통역 시 즉시 응급실 내원의 절대적 필요성을 강조해야 합니다. 소변 케톤 자가 측정의 중요성도 함께 전달해야 합니다.",
        "commonMistakes": [
            {
                "mistake": "'Ngộ độc'으로 번역",
                "correction": "'Nhiễm axit keto đái tháo đường' 정확한 용어",
                "explanation": "중독이 아니라 대사 이상으로 인한 산증"
            },
            {
                "mistake": "집에서 경구 수분 보충만 하면 된다고 오해",
                "correction": "즉시 응급실 내원하여 정맥 수액 치료 필요",
                "explanation": "생명을 위협하는 응급 상황임을 명확히"
            },
            {
                "mistake": "제1형에서만 발생한다고 설명",
                "correction": "제2형도 스트레스 상황에서 발생 가능",
                "explanation": "모든 당뇨병 환자가 경계해야 함"
            }
        ],
        "examples": [
            {
                "ko": "혈당 450mg/dL, pH 7.15로 당뇨병성 케톤산증 진단되어 응급 수액 및 인슐린 치료 중입니다",
                "vi": "Đường huyết 450mg/dL, pH 7.15, chẩn đoán nhiễm axit keto đái tháo đường, đang điều trị dịch truyền và insulin khẩn cấp",
                "situation": "formal"
            },
            {
                "ko": "구토가 계속되거나 소변 케톤이 양성이면 즉시 응급실로 오세요",
                "vi": "Nếu nôn liên tục hoặc ketone nước tiểu dương tính, hãy đến cấp cứu ngay",
                "situation": "onsite"
            },
            {
                "ko": "아이가 배 아프고 숨쉬기 힘들어 하는데 케톤산증인가요?",
                "vi": "Con đau bụng và khó thở, có phải nhiễm axit keto không?",
                "situation": "informal"
            }
        ],
        "relatedTerms": ["제1형당뇨병", "케톤체", "산혈증", "응급치료"]
    },
    {
        "slug": "ha-duong-huyet",
        "korean": "저혈당증",
        "vietnamese": "Hạ đường huyết",
        "hanja": "低血糖症",
        "hanjaReading": "低(낮을 저) + 血(피 혈) + 糖(엿 당) + 症(병 증)",
        "pronunciation": "하두엉후옛",
        "meaningKo": "혈당이 정상 범위 이하로 낮아지는 상태로, 당뇨병 치료 중 가장 흔한 급성 합병증입니다. 통역 시 주의할 점은 '식은땀, 떨림, 어지러움, 두근거림' 등의 증상을 환자가 인지하도록 교육하고, 저혈당 발생 시 즉시 당분 섭취(사탕, 주스)의 중요성을 강조해야 합니다. 한국에서는 혈당 70mg/dL 미만을 저혈당으로 정의하며, 무자각 저혈당의 위험성과 운전 중 저혈당 예방을 위한 주의사항을 환자에게 명확히 전달해야 합니다.",
        "meaningVi": "Tình trạng đường huyết thấp dưới mức bình thường (<70mg/dL), biến chứng cấp tính thường gặp nhất khi điều trị đái tháo đường. Triệu chứng: vã mồ hôi lạnh, run, chóng mặt, hồi hộp.",
        "context": "내분비내과 외래, 당뇨병 교육, 인슐린 용량 조절",
        "culturalNote": "한국에서는 당뇨병 환자에게 저혈당 교육을 철저히 하고 사탕을 항상 휴대하도록 권장하지만, 베트남 환자들은 저혈당 증상을 잘 모르거나 대수롭지 않게 생각하는 경향이 있습니다. 한국 환자들은 저혈당이 두려워 혈당을 높게 유지하는 경우가 있고, 베트남 환자들은 가족이나 주변 사람에게 자신이 당뇨병 환자임을 알리기 꺼려하여 응급 상황에서 적절한 도움을 받지 못할 수 있어 통역 시 주변에 알리는 것의 중요성을 강조해야 합니다.",
        "commonMistakes": [
            {
                "mistake": "'Mệt mỏi'로만 번역",
                "correction": "'Hạ đường huyết' 정확한 용어 사용",
                "explanation": "단순 피로가 아니라 응급 상황일 수 있음"
            },
            {
                "mistake": "저혈당 시 식사를 하라고 안내",
                "correction": "즉시 당분(사탕, 주스) 섭취 후 15분 재측정",
                "explanation": "빠른 혈당 상승을 위해 단순당 필요"
            },
            {
                "mistake": "무의식 환자에게 음식을 입에 넣으라고 안내",
                "correction": "의식 없으면 글루카곤 주사 또는 119 신고",
                "explanation": "흡인 위험으로 음식 금기, 응급 처치 필요"
            }
        ],
        "examples": [
            {
                "ko": "혈당 55mg/dL 저혈당으로 주스 150mL 섭취 후 15분 뒤 재측정하세요",
                "vi": "Hạ đường huyết 55mg/dL, uống 150mL nước ép sau 15 phút đo lại",
                "situation": "formal"
            },
            {
                "ko": "항상 사탕이나 주스를 휴대하고 운전 전 혈당을 확인하세요",
                "vi": "Luôn mang theo kẹo hoặc nước ép, kiểm tra đường huyết trước khi lái xe",
                "situation": "onsite"
            },
            {
                "ko": "식은땀 나고 손이 떨리는데 저혈당인가요?",
                "vi": "Vã mồ hôi lạnh và run tay, có phải hạ đường huyết không?",
                "situation": "informal"
            }
        ],
        "relatedTerms": ["당뇨병", "글루카곤", "무자각저혈당", "혈당측정"]
    },
    {
        "slug": "thieu-mau",
        "korean": "빈혈",
        "vietnamese": "Thiếu máu",
        "hanja": "貧血",
        "hanjaReading": "貧(가난할 빈) + 血(피 혈)",
        "pronunciation": "티에우머우",
        "meaningKo": "혈액 내 적혈구 수나 헤모글로빈 농도가 정상보다 낮은 상태입니다. 통역 시 주의할 점은 빈혈의 원인이 다양(철결핍, 비타민 결핍, 만성 질환, 출혈 등)하므로 원인 감별이 중요하며, '피로, 어지러움, 창백' 등의 증상과 함께 혈액검사 결과(Hb, MCV, ferritin)를 정확히 전달해야 합니다. 한국에서는 건강검진에서 발견되는 경우가 많으며, 여성의 철결핍성 빈혈이 가장 흔하다는 점을 환자에게 명확히 전달해야 합니다.",
        "meaningVi": "Tình trạng số lượng hồng cầu hoặc nồng độ hemoglobin trong máu thấp hơn bình thường. Triệu chứng: mệt mỏi, chóng mặt, nhợt nhạt, đánh trống ngực.",
        "context": "혈액내과 외래, 건강검진 결과 상담, 빈혈 원인 감별",
        "culturalNote": "한국에서는 여성의 월경과다나 편식으로 인한 철결핍성 빈혈이 흔하며, 철분제 복용을 권장하지만 부작용(변비, 속쓰림)으로 복용을 중단하는 경우가 많습니다. 베트남에서는 기생충 감염이나 영양 결핍으로 인한 빈혈이 상대적으로 많을 수 있으며, 전통적으로 '보약'으로 치료하려는 경향이 있어 통역 시 원인에 따른 적절한 치료의 중요성을 강조해야 합니다. 헤모글로빈 수치의 의미를 환자가 이해하도록 설명해야 합니다.",
        "commonMistakes": [
            {
                "mistake": "모든 빈혈을 '철분 부족'으로 설명",
                "correction": "원인에 따라 치료가 다름 (철결핍, B12 결핍, 만성 질환 등)",
                "explanation": "정확한 원인 감별 후 치료 필요"
            },
            {
                "mistake": "Hb를 '헤모글로빈'으로만 음역",
                "correction": "'Hemoglobin (sắc tố máu)' 의미 함께 설명",
                "explanation": "환자 이해도 향상"
            },
            {
                "mistake": "철분제만 먹으면 즉시 좋아진다고 오해",
                "correction": "최소 3개월 복용 필요, 정기 추적 검사 강조",
                "explanation": "단기간 치료로는 충분하지 않음"
            }
        ],
        "examples": [
            {
                "ko": "헤모글로빈 9.5g/dL, MCV 70으로 철결핍성 빈혈 진단되어 철분제 처방합니다",
                "vi": "Hemoglobin 9.5g/dL, MCV 70, chẩn đoán thiếu máu do thiếu sắt, kê đơn bổ sung sắt",
                "situation": "formal"
            },
            {
                "ko": "철분제는 식후에 복용하고 3개월 후 재검사하세요",
                "vi": "Uống thuốc bổ sung sắt sau bữa ăn, tái khám sau 3 tháng",
                "situation": "onsite"
            },
            {
                "ko": "계속 피곤하고 어지러운데 빈혈인가요?",
                "vi": "Luôn mệt mỏi và chóng mặt, có phải thiếu máu không?",
                "situation": "informal"
            }
        ],
        "relatedTerms": ["철결핍성빈혈", "헤모글로빈", "철분제", "혈액검사"]
    },
    {
        "slug": "thieu-mau-thieu-sat",
        "korean": "철결핍성빈혈",
        "vietnamese": "Thiếu máu thiếu sắt",
        "hanja": "鐵欠乏性貧血",
        "hanjaReading": "鐵(쇠 철) + 欠(하품 흠) + 乏(없을 핍) + 性(성품 성) + 貧(가난할 빈) + 血(피 혈)",
        "pronunciation": "티에우머우티에우삿",
        "meaningKo": "체내 철분이 부족하여 적혈구 생성이 저하되는 가장 흔한 빈혈입니다. 통역 시 주의할 점은 '월경과다, 편식, 위장관 출혈' 등 원인을 파악하는 것이 중요하며, 철분제 복용 시 '변비, 검은 변' 등의 부작용을 미리 설명하여 환자가 놀라지 않도록 해야 합니다. 한국에서는 가임기 여성에서 가장 흔하며, 철분제와 함께 비타민C를 복용하면 흡수가 증가하고 차나 커피는 흡수를 방해한다는 점을 환자에게 명확히 전달해야 합니다.",
        "meaningVi": "Thiếu máu phổ biến nhất do thiếu sắt trong cơ thể làm giảm sản xuất hồng cầu. Nguyên nhân: kinh nguyệt nhiều, ăn uống thiếu dinh dưỡng, chảy máu tiêu hóa.",
        "context": "혈액내과 및 산부인과 외래, 여성 건강검진, 철분 보충 상담",
        "culturalNote": "한국에서는 젊은 여성의 다이어트와 월경과다로 철결핍성 빈혈이 흔하며, 철분제 복용을 권장하지만 부작용으로 순응도가 낮습니다. 베트남에서는 임신부와 출산 후 여성에서 빈혈이 흔하며, 전통적으로 '보혈' 음식(대추, 붉은 살코기)으로 치료하려는 경향이 있어 통역 시 음식만으로는 부족하고 철분제가 필요하다는 점을 강조해야 합니다. 또한 위장관 출혈이 원인일 경우 내시경 검사가 필요함을 전달해야 합니다.",
        "commonMistakes": [
            {
                "mistake": "철분제만 먹으면 바로 좋아진다고 설명",
                "correction": "최소 3-6개월 복용, 저장철 보충까지 필요",
                "explanation": "증상 호전 후에도 지속 복용 필요"
            },
            {
                "mistake": "검은 변을 '출혈'로 오해하여 환자 불안 유발",
                "correction": "철분제 복용 시 정상적인 부작용임을 미리 설명",
                "explanation": "환자가 놀라서 약을 중단하지 않도록"
            },
            {
                "mistake": "음식으로만 치료 가능하다고 오해",
                "correction": "음식 + 철분제 병행 필요",
                "explanation": "음식만으로는 충분한 철분 보충 어려움"
            }
        ],
        "examples": [
            {
                "ko": "페리틴 5ng/mL로 철결핍성 빈혈 진단되어 철분제 하루 100mg 처방합니다",
                "vi": "Ferritin 5ng/mL, chẩn đoán thiếu máu thiếu sắt, kê đơn sắt 100mg/ngày",
                "situation": "formal"
            },
            {
                "ko": "비타민C와 함께 복용하고 차나 커피는 피하세요",
                "vi": "Uống cùng vitamin C, tránh trà và cà phê",
                "situation": "onsite"
            },
            {
                "ko": "생리양이 많아서 빈혈이 생긴 건가요?",
                "vi": "Kinh nguyệt nhiều nên bị thiếu máu à?",
                "situation": "informal"
            }
        ],
        "relatedTerms": ["빈혈", "페리틴", "철분제", "월경과다"]
    },
    {
        "slug": "thieu-mau-suy-tao-huyet",
        "korean": "재생불량성빈혈",
        "vietnamese": "Thiếu máu suy tạo huyết",
        "hanja": "再生不良性貧血",
        "hanjaReading": "再(다시 재) + 生(날 생) + 不(아닐 불) + 良(좋을 양) + 性(성품 성) + 貧(가난할 빈) + 血(피 혈)",
        "pronunciation": "티에우머우수이타오후옛",
        "meaningKo": "골수의 조혈기능이 저하되어 모든 혈구(적혈구, 백혈구, 혈소판)가 감소하는 중증 질환입니다. 통역 시 주의할 점은 생명을 위협할 수 있는 심각한 질환이며, '빈혈, 감염, 출혈' 증상이 동시에 나타날 수 있다는 점을 환자와 가족에게 명확히 전달해야 합니다. 한국에서는 면역억제제 치료나 골수이식이 필요할 수 있으며, 원인(약물, 바이러스, 자가면역)에 따라 치료가 다르다는 점을 환자에게 오해 없이 설명해야 합니다.",
        "meaningVi": "Bệnh lý nặng do suy giảm chức năng tạo máu của tủy xương, làm giảm tất cả các loại tế bào máu (hồng cầu, bạch cầu, tiểu cầu). Có thể đe dọa tính mạng.",
        "context": "혈액내과 입원, 골수검사 설명, 면역억제제 치료 또는 골수이식 상담",
        "culturalNote": "한국에서는 재생불량성빈혈 진단 시 즉시 삼차 병원으로 전원하여 전문 치료를 받지만, 베트남에서는 진단과 치료 접근성이 제한적일 수 있습니다. 한국 환자와 가족은 '골수이식'이라는 단어에 큰 부담을 느끼며 비용과 공여자 문제로 고민하고, 베트남 환자들은 전통 치료로 '골수를 보강'하려는 시도를 할 수 있어 통역 시 현대 의학적 치료의 절대적 필요성을 강조해야 합니다. 감염 예방을 위한 격리와 위생 관리의 중요성도 전달해야 합니다.",
        "commonMistakes": [
            {
                "mistake": "단순 빈혈로 설명",
                "correction": "모든 혈구 감소, 생명 위협 가능한 중증 질환",
                "explanation": "질환의 심각성을 정확히 전달"
            },
            {
                "mistake": "철분제로 치료 가능하다고 오해",
                "correction": "면역억제제 또는 골수이식 필요",
                "explanation": "골수 기능 회복이 필요한 질환"
            },
            {
                "mistake": "'Ung thư máu'으로 오역",
                "correction": "재생불량성빈혈은 암이 아님",
                "explanation": "백혈병과 구별되는 질환임을 명확히"
            }
        ],
        "examples": [
            {
                "ko": "범혈구감소증으로 골수검사 결과 재생불량성 빈혈 진단되어 면역억제제 치료를 시작합니다",
                "vi": "Giảm toàn bộ tế bào máu, sinh thiết tủy xương chẩn đoán thiếu máu suy tạo huyết, bắt đầu điều trị thuốc ức chế miễn dịch",
                "situation": "formal"
            },
            {
                "ko": "감염 예방을 위해 손씻기를 철저히 하고 사람 많은 곳을 피하세요",
                "vi": "Để phòng nhiễm trùng, rửa tay kỹ và tránh nơi đông người",
                "situation": "onsite"
            },
            {
                "ko": "골수이식 해야 하나요? 비용이 얼마나 드나요?",
                "vi": "Có cần ghép tủy xương không? Chi phí bao nhiêu?",
                "situation": "informal"
            }
        ],
        "relatedTerms": ["범혈구감소증", "골수검사", "골수이식", "면역억제제"]
    },
    {
        "slug": "thieu-mau-tan-huyet",
        "korean": "용혈성빈혈",
        "vietnamese": "Thiếu máu tan huyết",
        "hanja": "溶血性貧血",
        "hanjaReading": "溶(녹을 용) + 血(피 혈) + 性(성품 성) + 貧(가난할 빈) + 血(피 혈)",
        "pronunciation": "티에우머우탄후옛",
        "meaningKo": "적혈구가 정상보다 빨리 파괴되어 발생하는 빈혈입니다. 통역 시 주의할 점은 선천성(유전)과 후천성(자가면역, 약물)을 구분하여 설명해야 하며, '황달, 진한 소변, 비장 비대' 등의 특징적 증상을 정확히 전달해야 합니다. 한국에서는 원인 감별을 위한 정밀 검사(쿰스 검사, 헤모글로빈 전기영동)가 필요하며, 중증인 경우 수혈이나 비장절제술이 필요할 수 있다는 점을 환자에게 명확히 전달해야 합니다.",
        "meaningVi": "Thiếu máu do hồng cầu bị phá hủy nhanh hơn bình thường. Phân loại: bẩm sinh (di truyền) và mắc phải (tự miễn, thuốc). Triệu chứng đặc trưng: vàng da, nước tiểu sẫm màu, lách to.",
        "context": "혈액내과 외래, 황달 원인 감별, 수혈 및 비장절제술 상담",
        "culturalNote": "한국에서는 자가면역성 용혈성빈혈이 상대적으로 흔하며, 스테로이드 치료를 우선하지만 베트남에서는 유전성 용혈성빈혈(G6PD 결핍증 등)이 지역에 따라 흔할 수 있습니다. 한국 환자들은 '황달'을 간 질환으로 오해하는 경우가 많아 혈액 질환임을 명확히 설명해야 하고, 베트남 환자들은 전통 약재 중 일부가 용혈을 유발할 수 있어 통역 시 복용 약물과 식품을 자세히 확인해야 합니다. G6PD 결핍 환자는 특정 약물과 잠두콩을 피해야 함을 강조해야 합니다.",
        "commonMistakes": [
            {
                "mistake": "황달을 간염으로 오역",
                "correction": "용혈로 인한 황달임을 명확히",
                "explanation": "환자가 간 질환으로 오해하지 않도록"
            },
            {
                "mistake": "모든 용혈성빈혈을 유전병으로 설명",
                "correction": "선천성과 후천성 구분",
                "explanation": "원인에 따라 치료와 예후가 다름"
            },
            {
                "mistake": "G6PD 결핍 시 약물 금기 교육 생략",
                "correction": "피해야 할 약물과 식품 목록 제공",
                "explanation": "급성 용혈 발작 예방을 위해 필수"
            }
        ],
        "examples": [
            {
                "ko": "쿰스 검사 양성으로 자가면역성 용혈성 빈혈 진단되어 스테로이드 치료를 시작합니다",
                "vi": "Xét nghiệm Coombs dương tính, chẩn đoán thiếu máu tan huyết tự miễn, bắt đầu điều trị corticosteroid",
                "situation": "formal"
            },
            {
                "ko": "G6PD 결핍이므로 아스피린과 잠두콩을 피하세요",
                "vi": "Thiếu G6PD nên tránh aspirin và đậu tằm",
                "situation": "onsite"
            },
            {
                "ko": "눈이 노랗고 소변 색이 진한데 간이 나쁜 건가요?",
                "vi": "Mắt vàng và nước tiểu sẫm màu, có phải gan không tốt?",
                "situation": "informal"
            }
        ],
        "relatedTerms": ["황달", "쿰스검사", "G6PD결핍", "비장절제술"]
    },
    {
        "slug": "giam-tieu-cau",
        "korean": "혈소판감소증",
        "vietnamese": "Giảm tiểu cầu",
        "hanja": "血小板減少症",
        "hanjaReading": "血(피 혈) + 小(작을 소) + 板(널판 판) + 減(덜 감) + 少(적을 소) + 症(병 증)",
        "pronunciation": "잠티에우꺼우",
        "meaningKo": "혈소판 수가 정상보다 낮아 출혈 경향이 증가하는 상태입니다. 통역 시 주의할 점은 원인이 다양(ITP, 약물, 감염, 골수 질환)하므로 감별이 중요하며, '멍, 점상출혈, 잇몸 출혈, 코피' 등의 출혈 증상을 정확히 파악하여 전달해야 합니다. 한국에서는 혈소판 수가 10,000/μL 미만이면 자발적 출혈 위험이 높아 입원이 필요하며, 스테로이드나 면역글로불린 치료가 필요할 수 있다는 점을 환자에게 명확히 전달해야 합니다.",
        "meaningVi": "Tình trạng số lượng tiểu cầu thấp hơn bình thường, tăng nguy cơ chảy máu. Triệu chứng: bầm tím, xuất huyết điểm, chảy máu lợi, chảy máu cam.",
        "context": "혈액내과 외래 및 입원, 출혈 경향 평가, 스테로이드 치료 상담",
        "culturalNote": "한국에서는 건강검진에서 우연히 발견되는 무증상 혈소판감소증이 많으며, 환자들은 '혈소판이 낮다'는 말에 불안해하지만 증상이 없으면 추적관찰하는 경우도 많습니다. 베트남에서는 뎅기열 등 감염으로 인한 혈소판감소증이 흔할 수 있어 통역 시 원인 감별의 중요성을 강조해야 합니다. 한국 환자들은 멍이 잘 드는 것을 대수롭지 않게 생각하다가 진단이 늦어지는 경우가 있고, 베트남 환자들은 전통 약재로 '피를 보강'하려는 시도를 할 수 있어 의학적 치료의 필요성을 강조해야 합니다.",
        "commonMistakes": [
            {
                "mistake": "모든 혈소판감소증을 ITP로 설명",
                "correction": "원인 감별 필요 (ITP, 약물, 감염, 골수 질환 등)",
                "explanation": "원인에 따라 치료가 완전히 다름"
            },
            {
                "mistake": "혈소판 수치만 전달하고 출혈 위험 설명 생략",
                "correction": "수치와 함께 출혈 위험도 설명",
                "explanation": "환자가 주의사항을 이해하도록"
            },
            {
                "mistake": "아스피린 금기 교육 누락",
                "correction": "항혈소판제, NSAID 피해야 함을 강조",
                "explanation": "출혈 위험 증가 방지"
            }
        ],
        "examples": [
            {
                "ko": "혈소판 25,000/μL로 면역성 혈소판감소증 의심되어 스테로이드 치료를 시작합니다",
                "vi": "Tiểu cầu 25,000/μL nghi giảm tiểu cầu miễn dịch, bắt đầu điều trị corticosteroid",
                "situation": "formal"
            },
            {
                "ko": "아스피린이나 소염진통제는 피하고 부딪히지 않도록 조심하세요",
                "vi": "Tránh aspirin và thuốc giảm đau chống viêm, cẩn thận không va đập",
                "situation": "onsite"
            },
            {
                "ko": "멍이 자주 들고 코피가 나는데 혈소판이 낮은 건가요?",
                "vi": "Hay bị bầm tím và chảy máu cam, có phải tiểu cầu thấp không?",
                "situation": "informal"
            }
        ],
        "relatedTerms": ["ITP", "출혈경향", "스테로이드", "면역글로불린"]
    },
    {
        "slug": "bach-cau-mau",
        "korean": "백혈병",
        "vietnamese": "Bạch cầu máu",
        "hanja": "白血病",
        "hanjaReading": "白(흰 백) + 血(피 혈) + 病(병 병)",
        "pronunciation": "박꺼우머우",
        "meaningKo": "골수에서 비정상적인 백혈구가 과다 증식하는 혈액암입니다. 통역 시 주의할 점은 급성과 만성, 골수성과 림프구성으로 분류되며 각각 치료와 예후가 다르므로 정확한 유형을 전달해야 합니다. 한국에서는 '빈혈, 출혈, 감염' 증상으로 발견되거나 건강검진에서 백혈구 이상으로 발견되며, 항암화학요법이나 조혈모세포이식이 필요할 수 있다는 점을 환자와 가족에게 명확히 전달해야 합니다. '암'이라는 진단에 대한 환자의 심리적 충격을 고려하여 의사의 설명을 정확하고 공감적으로 통역해야 합니다.",
        "meaningVi": "Ung thư máu do tế bào bạch cầu bất thường tăng sinh quá mức trong tủy xương. Phân loại: cấp/mạn, dòng tủy/dòng lympho. Điều trị: hóa trị, ghép tế bào gốc tạo máu.",
        "context": "혈액내과 입원, 항암치료 설명, 조혈모세포이식 상담",
        "culturalNote": "한국에서는 백혈병 진단 시 즉시 삼차 병원으로 전원하여 전문 치료를 받으며, 급성 백혈병은 응급 상황으로 인식됩니다. 베트남에서는 진단과 치료 접근성이 제한적일 수 있으며, 경제적 부담으로 치료를 포기하는 경우도 있습니다. 한국 환자와 가족은 '완치율'을 가장 먼저 묻는 경향이 있고, 베트남 환자들은 전통 치료와 병행하려는 시도를 할 수 있어 통역 시 현대 의학적 치료의 절대적 필요성과 완치 가능성을 균형 있게 전달해야 합니다. 소아 급성 림프구성 백혈병의 경우 완치율이 높다는 점을 강조해야 합니다.",
        "commonMistakes": [
            {
                "mistake": "모든 백혈병을 동일하게 설명",
                "correction": "급성/만성, 골수성/림프구성 구분 필수",
                "explanation": "유형에 따라 치료와 예후가 완전히 다름"
            },
            {
                "mistake": "'Ung thư'로만 번역하여 불안 조성",
                "correction": "유형과 완치율 함께 전달",
                "explanation": "특히 소아 ALL은 완치율 높음을 강조"
            },
            {
                "mistake": "골수이식을 '마지막 수단'으로만 설명",
                "correction": "유형에 따라 1차 치료일 수 있음",
                "explanation": "치료 계획에 대한 정확한 이해 필요"
            }
        ],
        "examples": [
            {
                "ko": "급성 골수성 백혈병으로 진단되어 즉시 항암화학요법을 시작하고 관해 후 이식을 고려합니다",
                "vi": "Chẩn đoán bạch cầu cấp dòng tủy, bắt đầu hóa trị ngay và xem xét ghép sau khi thuyên giảm",
                "situation": "formal"
            },
            {
                "ko": "감염 예방을 위해 무균실에서 치료받게 됩니다",
                "vi": "Điều trị trong phòng vô trùng để phòng nhiễm trùng",
                "situation": "onsite"
            },
            {
                "ko": "백혈병이면 완치가 안 되나요?",
                "vi": "Bạch cầu máu có khỏi được không?",
                "situation": "informal"
            }
        ],
        "relatedTerms": ["급성백혈병", "만성백혈병", "항암화학요법", "조혈모세포이식"]
    },
    {
        "slug": "u-hat",
        "korean": "림프종",
        "vietnamese": "U hạch",
        "hanja": "淋巴腫",
        "hanjaReading": "淋(물흐를 림) + 巴(바랄 파) + 腫(부을 종)",
        "pronunciation": "우핫",
        "meaningKo": "림프계에 발생하는 악성 종양으로 호지킨 림프종과 비호지킨 림프종으로 분류됩니다. 통역 시 주의할 점은 '목, 겨드랑이, 사타구니의 무통성 림프절 비대'가 주요 증상이며, 발열, 체중감소, 식은땀 등 B 증상의 유무가 예후에 영향을 준다는 점을 환자에게 명확히 전달해야 합니다. 한국에서는 PET-CT로 병기를 결정하고 항암화학요법이나 방사선치료를 시행하며, 조직검사가 진단에 필수적이라는 점을 환자가 오해 없이 이해하도록 통역해야 합니다.",
        "meaningVi": "Khối u ác tính phát sinh từ hệ thống bạch huyết, phân loại Hodgkin và non-Hodgkin. Triệu chứng chính: hạch to không đau ở cổ, nách, bẹn. Triệu chứng B: sốt, sụt cân, vã mồ hôi đêm.",
        "context": "혈액내과 외래 및 입원, 조직검사 설명, 항암화학요법 및 방사선치료 상담",
        "culturalNote": "한국에서는 목의 혹으로 내원하여 조직검사 후 림프종을 진단받는 경우가 많으며, 환자들은 '암'이라는 진단에 충격을 받지만 림프종은 비교적 치료 반응이 좋은 암임을 알고 위안을 얻습니다. 베트남에서는 결핵성 림프절염이 흔하여 감별이 중요하며, 전통 의학으로 '혹'을 없애려는 시도로 진단이 늦어질 수 있어 통역 시 조기 조직검사의 중요성을 강조해야 합니다. 호지킨 림프종의 경우 젊은 연령에서 발생하지만 완치율이 높다는 점을 전달해야 합니다.",
        "commonMistakes": [
            {
                "mistake": "림프절염과 림프종을 구분 않고 통역",
                "correction": "염증(viêm)과 종양(u)은 완전히 다름",
                "explanation": "환자가 질환의 심각성을 정확히 인지하도록"
            },
            {
                "mistake": "조직검사를 '선택사항'으로 설명",
                "correction": "진단에 필수적인 검사임을 강조",
                "explanation": "정확한 진단과 치료 계획 수립을 위해 필요"
            },
            {
                "mistake": "B 증상의 중요성 설명 누락",
                "correction": "발열, 체중감소, 식은땀 유무 확인 필수",
                "explanation": "병기와 예후 결정에 중요"
            }
        ],
        "examples": [
            {
                "ko": "목 림프절 조직검사 결과 호지킨 림프종 2기로 진단되어 ABVD 항암화학요법을 시행합니다",
                "vi": "Sinh thiết hạch cổ chẩn đoán u hạch Hodgkin giai đoạn 2, thực hiện hóa trị ABVD",
                "situation": "formal"
            },
            {
                "ko": "치료 중 발열이나 감염 증상이 있으면 즉시 연락하세요",
                "vi": "Nếu sốt hoặc có dấu hiệu nhiễm trùng trong quá trình điều trị, hãy liên hệ ngay",
                "situation": "onsite"
            },
            {
                "ko": "목에 혹이 있는데 림프종인가요 결핵인가요?",
                "vi": "Có hạch ở cổ, là u hạch hay lao?",
                "situation": "informal"
            }
        ],
        "relatedTerms": ["호지킨림프종", "비호지킨림프종", "조직검사", "항암화학요법"]
    },
    {
        "slug": "da-u-tuy",
        "korean": "다발성골수종",
        "vietnamese": "Đa u tủy",
        "hanja": "多發性骨髓腫",
        "hanjaReading": "多(많을 다) + 發(필 발) + 性(성품 성) + 骨(뼈 골) + 髓(골수 수) + 腫(부을 종)",
        "pronunciation": "다우투이",
        "meaningKo": "형질세포의 악성 증식으로 발생하는 혈액암으로, 뼈 통증, 골절, 빈혈, 신기능 저하 등을 유발합니다. 통역 시 주의할 점은 '허리 통증, 병적 골절, 고칼슘혈증' 등의 증상을 정확히 전달해야 하며, 완치는 어렵지만 치료로 증상 조절과 생존 연장이 가능하다는 점을 환자에게 명확히 전달해야 합니다. 한국에서는 고령 환자에서 주로 발생하며, 항암화학요법과 자가조혈모세포이식으로 치료하고, 뼈 건강을 위한 비스포스포네이트 투여가 중요하다는 점을 환자가 오해 없이 이해하도록 통역해야 합니다.",
        "meaningVi": "Ung thư máu do tăng sinh ác tính tế bào plasma, gây đau xương, gãy xương, thiếu máu, suy thận. Thường gặp ở người cao tuổi. Khó chữa khỏi hoàn toàn nhưng có thể kiểm soát triệu chứng và kéo dài sống.",
        "context": "혈액내과 외래 및 입원, 골통증 원인 감별, 항암치료 및 골보호제 상담",
        "culturalNote": "한국에서는 고령 환자의 허리 통증으로 정형외과를 먼저 방문했다가 골다공증 검사에서 이상 소견으로 혈액내과로 의뢰되는 경우가 많습니다. 베트남에서는 노화로 인한 통증으로 간주하여 진단이 늦어질 수 있으며, 경제적 부담으로 치료를 지속하지 못하는 경우도 있습니다. 한국 환자와 가족은 '완치 가능성'을 묻지만 대부분 만성 질환으로 관리해야 한다는 점을 수용하는 데 시간이 걸리며, 통역 시 생존율 향상과 삶의 질 유지에 초점을 맞춰 설명해야 합니다.",
        "commonMistakes": [
            {
                "mistake": "골다공증과 혼동",
                "correction": "골다공증은 뼈 약화, 골수종은 혈액암",
                "explanation": "완전히 다른 질환이며 치료도 다름"
            },
            {
                "mistake": "완치 가능하다고 오해 조성",
                "correction": "만성 질환으로 관리, 완치는 어려움",
                "explanation": "현실적 기대치 설정 필요"
            },
            {
                "mistake": "통증 조절만 강조하고 항암치료 필요성 누락",
                "correction": "항암치료가 주 치료, 통증은 증상 관리",
                "explanation": "근본 치료의 중요성 전달"
            }
        ],
        "examples": [
            {
                "ko": "M 단백 양성, 골수 형질세포 40%로 다발성 골수종 진단되어 VRD 요법을 시작합니다",
                "vi": "M protein dương tính, tế bào plasma tủy xương 40%, chẩn đoán đa u tủy, bắt đầu liệu pháp VRD",
                "situation": "formal"
            },
            {
                "ko": "뼈 건강을 위해 비스포스포네이트를 매달 주사받으셔야 합니다",
                "vi": "Cần tiêm bisphosphonate hàng tháng để bảo vệ xương",
                "situation": "onsite"
            },
            {
                "ko": "허리가 너무 아픈데 골수종이 맞나요? 완치되나요?",
                "vi": "Đau lưng quá, có phải đa u tủy không? Có khỏi được không?",
                "situation": "informal"
            }
        ],
        "relatedTerms": ["형질세포", "병적골절", "M단백", "자가조혈모세포이식"]
    },
    {
        "slug": "ghep-tuy-xuong",
        "korean": "골수이식",
        "vietnamese": "Ghép tủy xương",
        "hanja": "骨髓移植",
        "hanjaReading": "骨(뼈 골) + 髓(골수 수) + 移(옮길 이) + 植(심을 식)",
        "pronunciation": "겝투이쑤엉",
        "meaningKo": "혈액암이나 재생불량성빈혈 등을 치료하기 위해 공여자의 건강한 조혈모세포를 환자에게 이식하는 치료법입니다. 통역 시 주의할 점은 '동종이식'과 '자가이식'을 구분하여 설명해야 하며, 고강도 항암치료 후 이식하므로 감염 위험이 높고 이식편대숙주병 등 합병증이 발생할 수 있다는 점을 환자와 가족에게 명확히 전달해야 합니다. 한국에서는 HLA 일치 공여자 찾기가 중요하며, 형제자매가 우선이지만 비혈연 공여자 은행도 활용 가능하다는 점을 환자가 오해 없이 이해하도록 통역해야 합니다.",
        "meaningVi": "Phương pháp điều trị ung thư máu hoặc suy tủy xương bằng cách ghép tế bào gốc tạo máu khỏe mạnh từ người hiến vào bệnh nhân. Phân loại: ghép đồng loại (người khác) và tự ghép (chính mình).",
        "context": "혈액내과 입원, 이식 전 설명회, 공여자 상담, 이식 후 관리 교육",
        "culturalNote": "한국에서는 골수이식이 '마지막 희망'이자 '완치 가능성'으로 인식되지만 비용과 공여자 문제, 합병증 우려로 결정이 어렵습니다. 베트남에서는 경제적 부담과 의료 접근성 문제로 이식을 받지 못하는 경우가 많습니다. 한국 가족들은 공여자가 되는 것에 대한 부담(통증, 회복 기간)을 걱정하고, 베트남에서는 전통적으로 '피를 나눈다'는 개념에 거부감이 있을 수 있어 통역 시 과학적 설명과 함께 공여자의 안전성을 강조해야 합니다. 이식 성공률과 합병증 가능성을 균형 있게 전달해야 합니다.",
        "commonMistakes": [
            {
                "mistake": "골수이식과 조혈모세포이식을 다른 것으로 설명",
                "correction": "같은 의미이며 최근 조혈모세포이식 용어 선호",
                "explanation": "환자 혼란 방지"
            },
            {
                "mistake": "공여자가 위험하다고 과장",
                "correction": "공여자 위험은 최소화되어 있음",
                "explanation": "공여자 확보를 위해 정확한 정보 전달"
            },
            {
                "mistake": "이식 후 즉시 퇴원 가능하다고 오해",
                "correction": "최소 4-6주 입원, 이후에도 추적 관찰 필수",
                "explanation": "현실적 기대치 설정"
            }
        ],
        "examples": [
            {
                "ko": "HLA 10/10 일치 형제 공여자로부터 동종 골수이식을 시행할 예정입니다",
                "vi": "Dự định ghép tủy xương đồng loại từ anh/chị em ruột HLA 10/10 phù hợp",
                "situation": "formal"
            },
            {
                "ko": "이식 후 100일까지는 감염 예방을 위해 마스크 착용이 필수입니다",
                "vi": "Đến 100 ngày sau ghép bắt buộc đeo khẩu trang để phòng nhiễm trùng",
                "situation": "onsite"
            },
            {
                "ko": "골수이식 받으면 완치되나요? 동생이 기증하면 위험하지 않나요?",
                "vi": "Ghép tủy xương có khỏi hoàn toàn không? Em tôi hiến có nguy hiểm không?",
                "situation": "informal"
            }
        ],
        "relatedTerms": ["조혈모세포이식", "HLA", "이식편대숙주병", "공여자"]
    },
    {
        "slug": "ghep-te-bao-goc-tao-mau",
        "korean": "조혈모세포이식",
        "vietnamese": "Ghép tế bào gốc tạo máu",
        "hanja": "造血母細胞移植",
        "hanjaReading": "造(지을 조) + 血(피 혈) + 母(어미 모) + 細(가늘 세) + 胞(세포 포) + 移(옮길 이) + 植(심을 식)",
        "pronunciation": "겝떼바오곡타오머우",
        "meaningKo": "골수, 말초혈, 제대혈에서 채취한 조혈모세포를 이식하는 치료법으로 골수이식의 현대적 명칭입니다. 통역 시 주의할 점은 채취 방법(골수 천자, 말초혈 채집, 제대혈)에 따라 장단점이 다르며, 환자와 공여자 모두에게 적합한 방법을 선택한다는 점을 명확히 전달해야 합니다. 한국에서는 말초혈 조혈모세포 이식이 가장 흔하며, 공여자는 G-CSF 주사 후 성분채집술로 채취하고, 골수 천자보다 덜 침습적이라는 점을 환자와 공여자에게 오해 없이 설명해야 합니다.",
        "meaningVi": "Phương pháp ghép tế bào gốc tạo máu lấy từ tủy xương, máu ngoại vi, hoặc máu dây rốn. Tên gọi hiện đại của ghép tủy xương. Phương pháp lấy máu ngoại vi ít xâm lấn hơn chọc tủy xương.",
        "context": "혈액내과 입원, 공여자 채취 설명, 이식 전후 관리 교육",
        "culturalNote": "한국에서는 '골수이식'이라는 용어가 익숙하지만 의료진은 '조혈모세포이식'을 선호하며, 환자와 가족에게 두 용어가 같은 의미임을 설명해야 합니다. 베트남에서는 제대혈 은행이 발달하지 않아 제대혈 이식 접근성이 낮을 수 있습니다. 한국 공여자들은 '골수를 뽑으면 장애가 생긴다'는 잘못된 인식이 있어 말초혈 채취 방법이 안전하다는 점을 강조해야 하고, 베트남에서는 전통적으로 '정기'를 빼앗긴다는 생각이 있을 수 있어 과학적 설명이 필요합니다.",
        "commonMistakes": [
            {
                "mistake": "골수이식과 완전히 다른 것으로 설명",
                "correction": "같은 개념, 조혈모세포이식이 포괄적 용어",
                "explanation": "환자 혼란 방지"
            },
            {
                "mistake": "말초혈 채취를 '수술'로 설명",
                "correction": "성분채집술로 헌혈과 유사",
                "explanation": "공여자 부담 감소"
            },
            {
                "mistake": "제대혈 이식을 소아에게만 가능하다고 설명",
                "correction": "성인도 가능하지만 체중에 따라 제한",
                "explanation": "정확한 정보 제공"
            }
        ],
        "examples": [
            {
                "ko": "공여자는 G-CSF 주사 후 말초혈 조혈모세포 채집술을 받게 됩니다",
                "vi": "Người hiến sẽ tiêm G-CSF sau đó thu thập tế bào gốc tạo máu từ máu ngoại vi",
                "situation": "formal"
            },
            {
                "ko": "채집 과정은 4-5시간 소요되며 헌혈과 비슷합니다",
                "vi": "Quá trình thu thập mất 4-5 tiếng, tương tự như hiến máu",
                "situation": "onsite"
            },
            {
                "ko": "조혈모세포 기증하면 나중에 건강에 문제 생기나요?",
                "vi": "Hiến tế bào gốc tạo máu có ảnh hưởng sức khỏe sau này không?",
                "situation": "informal"
            }
        ],
        "relatedTerms": ["골수이식", "말초혈채집", "제대혈", "G-CSF"]
    },
    {
        "slug": "hoa-tri-ung-thu",
        "korean": "항암화학요법",
        "vietnamese": "Hóa trị ung thư",
        "hanja": "抗癌化學療法",
        "hanjaReading": "抗(막을 항) + 癌(암 암) + 化(될 화) + 學(배울 학) + 療(고칠 료) + 法(법 법)",
        "pronunciation": "호아찌웅투",
        "meaningKo": "항암제를 사용하여 암세포를 죽이거나 성장을 억제하는 치료법입니다. 통역 시 주의할 점은 '구역, 구토, 탈모, 골수억제' 등의 부작용을 미리 설명하여 환자가 준비할 수 있도록 해야 하며, 부작용은 일시적이고 치료 종료 후 회복된다는 점을 명확히 전달해야 합니다. 한국에서는 외래에서 항암치료를 받는 경우가 많으며, 치료 전 혈액검사로 골수 기능을 확인하고 백혈구가 낮으면 치료를 연기한다는 점을 환자가 오해 없이 이해하도록 통역해야 합니다.",
        "meaningVi": "Phương pháp điều trị sử dụng thuốc hóa chất để tiêu diệt hoặc ức chế tăng trưởng tế bào ung thư. Tác dụng phụ: buồn nôn, nôn, rụng tóc, ức chế tủy xương. Tác dụng phụ tạm thời, hồi phục sau điều trị.",
        "context": "혈액종양내과 외래 및 주사실, 항암치료 전 설명, 부작용 관리 교육",
        "culturalNote": "한국에서는 항암치료에 대한 두려움이 크지만 대부분의 환자가 치료를 받아들이며, 탈모를 가장 걱정하는 경향이 있습니다. 베트남에서는 항암치료의 부작용을 과도하게 무서워하여 치료를 거부하거나, 전통 의학으로 대체하려는 시도가 있을 수 있어 통역 시 현대 항암치료의 효과와 부작용 관리 방법을 균형 있게 전달해야 합니다. 한국 환자들은 '항암제 맞으면 더 빨리 죽는다'는 속설을 믿는 경우가 있고, 베트남 환자들은 '독한 약'이라는 인식이 있어 치료의 필요성과 생존율 향상 데이터를 명확히 제시해야 합니다.",
        "commonMistakes": [
            {
                "mistake": "모든 항암제가 탈모를 유발한다고 설명",
                "correction": "약제에 따라 탈모 정도 다름",
                "explanation": "불필요한 불안 방지"
            },
            {
                "mistake": "부작용만 강조하여 공포 조성",
                "correction": "부작용과 함께 관리 방법, 효과 균형 있게 전달",
                "explanation": "치료 순응도 향상"
            },
            {
                "mistake": "백혈구 감소를 '면역력 없음'으로 과장",
                "correction": "일시적 감소, 회복 가능",
                "explanation": "환자 불안 감소"
            }
        ],
        "examples": [
            {
                "ko": "R-CHOP 요법 6주기 시행 예정이며 각 주기마다 21일 간격입니다",
                "vi": "Dự định thực hiện 6 chu kỳ liệu pháp R-CHOP, mỗi chu kỳ cách 21 ngày",
                "situation": "formal"
            },
            {
                "ko": "항암 후 3-7일째 백혈구가 가장 낮으니 감염 조심하세요",
                "vi": "Ngày 3-7 sau hóa trị bạch cầu thấp nhất, cẩn thận nhiễm trùng",
                "situation": "onsite"
            },
            {
                "ko": "항암치료 받으면 머리카락 다 빠지나요?",
                "vi": "Hóa trị có rụng hết tóc không?",
                "situation": "informal"
            }
        ],
        "relatedTerms": ["항암제", "부작용", "골수억제", "탈모"]
    },
    {
        "slug": "thuoc-dich-huong",
        "korean": "표적항암제",
        "vietnamese": "Thuốc đích hướng",
        "hanja": "標的抗癌劑",
        "hanjaReading": "標(표 표) + 的(과녁 적) + 抗(막을 항) + 癌(암 암) + 劑(약제 제)",
        "pronunciation": "툭딕후엉",
        "meaningKo": "암세포의 특정 분자나 경로를 선택적으로 공격하는 항암제로, 기존 화학요법보다 부작용이 적습니다. 통역 시 주의할 점은 특정 유전자 변이나 단백질이 있는 환자에게만 효과적이므로 유전자 검사가 필수적이며, 고가의 약제라는 점을 환자에게 명확히 전달해야 합니다. 한국에서는 폐암의 EGFR 변이, 유방암의 HER2 양성 등에 따라 표적치료를 시행하며, 건강보험 급여 기준을 충족해야 보험 적용이 가능하다는 점을 환자가 오해 없이 이해하도록 통역해야 합니다.",
        "meaningVi": "Thuốc ung thư tấn công chọn lọc phân tử hoặc đường dẫn cụ thể của tế bào ung thư, ít tác dụng phụ hơn hóa trị thông thường. Chỉ hiệu quả khi có đột biến gen hoặc protein cụ thể, cần xét nghiệm gen.",
        "context": "종양내과 외래, 유전자 검사 결과 설명, 표적치료 상담",
        "culturalNote": "한국에서는 표적항암제가 '신약'이고 '부작용이 적다'는 인식으로 선호하지만, 비용 부담과 급여 제한으로 접근성이 제한적입니다. 베트남에서는 경제적 부담으로 표적치료를 받지 못하는 경우가 많습니다. 한국 환자들은 '표적치료면 완치 가능하다'는 오해를 하는 경우가 있고, 베트남 환자들은 전통 약재가 '천연 표적치료'라고 생각하는 경향이 있어 통역 시 표적치료의 정확한 개념과 한계를 명확히 전달해야 합니다. 내성 발생 가능성과 정기적 검사 필요성도 설명해야 합니다.",
        "commonMistakes": [
            {
                "mistake": "모든 암 환자에게 사용 가능하다고 오해",
                "correction": "특정 변이 있을 때만 효과적",
                "explanation": "유전자 검사 필요성 강조"
            },
            {
                "mistake": "부작용이 전혀 없다고 설명",
                "correction": "화학요법과 다른 종류의 부작용 있음 (피부 발진, 설사 등)",
                "explanation": "정확한 정보 제공"
            },
            {
                "mistake": "급여 여부 확인 없이 처방 가능하다고 안내",
                "correction": "보험 기준 충족 여부 확인 필요",
                "explanation": "환자 경제적 부담 고려"
            }
        ],
        "examples": [
            {
                "ko": "EGFR 변이 양성으로 표적항암제 게피티닙 처방합니다",
                "vi": "Đột biến EGFR dương tính, kê đơn thuốc đích hướng gefitinib",
                "situation": "formal"
            },
            {
                "ko": "피부 발진이 생길 수 있으니 자외선 차단제를 꼭 바르세요",
                "vi": "Có thể nổi mẩn da, nhớ bôi kem chống nắng",
                "situation": "onsite"
            },
            {
                "ko": "표적치료 받으면 완치되나요? 비용은 얼마나 되나요?",
                "vi": "Điều trị đích hướng có khỏi hoàn toàn không? Chi phí bao nhiêu?",
                "situation": "informal"
            }
        ],
        "relatedTerms": ["유전자검사", "EGFR", "HER2", "면역항암제"]
    },
    {
        "slug": "mien-dich-lieu-phap",
        "korean": "면역항암제",
        "vietnamese": "Miễn dịch liệu pháp",
        "hanja": "免疫抗癌劑",
        "hanjaReading": "免(면할 면) + 疫(질병 역) + 抗(막을 항) + 癌(암 암) + 劑(약제 제)",
        "pronunciation": "미엔직리에우팝",
        "meaningKo": "환자의 면역체계를 활성화하여 암세포를 공격하도록 하는 치료법입니다. 통역 시 주의할 점은 면역관련 부작용(폐렴, 대장염, 갑상선염 등)이 발생할 수 있으며, 기존 화학요법과는 다른 양상의 부작용이므로 증상 발생 시 즉시 알려야 한다는 점을 환자에게 명확히 전달해야 합니다. 한국에서는 폐암, 흑색종, 신장암 등에서 사용되며, PD-L1 발현율에 따라 효과가 다르고 고가의 치료이지만 일부는 급여가 적용된다는 점을 환자가 오해 없이 이해하도록 통역해야 합니다.",
        "meaningVi": "Phương pháp điều trị kích hoạt hệ miễn dịch của bệnh nhân để tấn công tế bào ung thư. Tác dụng phụ liên quan miễn dịch: viêm phổi, viêm đại tràng, viêm tuyến giáp. Cần báo ngay khi có triệu chứng.",
        "context": "종양내과 외래, 면역치료 설명, 면역관련 부작용 교육",
        "culturalNote": "한국에서는 면역항암제가 '최신 치료'로 인식되며 많은 환자가 희망을 갖지만, 효과가 나타나는 환자가 제한적이고 비용이 매우 비싸 접근성이 낮습니다. 베트남에서는 경제적 부담으로 거의 접근 불가능할 수 있습니다. 한국 환자들은 '면역력을 높이는 치료'로 오해하여 홍삼, 영지버섯 등을 함께 복용하려 하고, 베트남 환자들은 전통 약재가 '면역 치료'라고 생각하는 경향이 있어 통역 시 면역항암제의 정확한 작용 기전과 전통 약재와의 차이를 명확히 설명해야 합니다.",
        "commonMistakes": [
            {
                "mistake": "면역력 강화 건강식품과 혼동",
                "correction": "면역체계를 암에 대항하도록 재프로그래밍하는 치료",
                "explanation": "정확한 기전 이해"
            },
            {
                "mistake": "부작용이 없다고 설명",
                "correction": "면역관련 부작용 발생 가능, 조기 발견 중요",
                "explanation": "환자 안전 확보"
            },
            {
                "mistake": "모든 암에 효과적이라고 오해",
                "correction": "특정 암종, PD-L1 발현에 따라 효과 다름",
                "explanation": "현실적 기대치 설정"
            }
        ],
        "examples": [
            {
                "ko": "PD-L1 발현율 80%로 면역항암제 펨브롤리주맙 단독요법을 시행합니다",
                "vi": "Tỷ lệ biểu hiện PD-L1 80%, thực hiện liệu pháp đơn độc miễn dịch pembrolizumab",
                "situation": "formal"
            },
            {
                "ko": "설사, 기침, 숨가쁨 등이 생기면 즉시 연락하세요",
                "vi": "Nếu tiêu chảy, ho, khó thở hãy liên hệ ngay",
                "situation": "onsite"
            },
            {
                "ko": "면역항암제 맞으면 부작용 없이 완치되나요?",
                "vi": "Miễn dịch liệu pháp có khỏi hoàn toàn mà không tác dụng phụ không?",
                "situation": "informal"
            }
        ],
        "relatedTerms": ["PD-1억제제", "PD-L1", "면역관련부작용", "표적항암제"]
    },
    {
        "slug": "xa-tri",
        "korean": "방사선치료",
        "vietnamese": "Xạ trị",
        "hanja": "放射線治療",
        "hanjaReading": "放(놓을 방) + 射(쏠 사) + 線(줄 선) + 治(다스릴 치) + 療(고칠 료)",
        "pronunciation": "싸찌",
        "meaningKo": "고에너지 방사선을 이용하여 암세포를 파괴하는 치료법입니다. 통역 시 주의할 점은 치료 부위에 따라 부작용이 다르며(뇌: 탈모, 두통 / 가슴: 식도염, 폐렴 / 골반: 설사, 방광염), 치료 중과 치료 후에도 피부 관리가 중요하다는 점을 환자에게 명확히 전달해야 합니다. 한국에서는 외래에서 매일 또는 주 5회 치료를 받으며, 치료 횟수와 기간이 정해져 있어 중간에 중단하면 효과가 떨어진다는 점을 환자가 오해 없이 이해하도록 통역해야 합니다.",
        "meaningVi": "Phương pháp điều trị sử dụng tia bức xạ năng lượng cao để tiêu diệt tế bào ung thư. Tác dụng phụ khác nhau tùy vị trí: não (rụng tóc, đau đầu), ngực (viêm thực quản, viêm phổi), chậu (tiêu chảy, viêm bàng quang).",
        "context": "방사선종양학과 외래, 치료 계획 설명, 부작용 관리 교육",
        "culturalNote": "한국에서는 방사선치료에 대한 막연한 두려움('방사능에 피폭된다')이 있지만 대부분의 환자가 치료를 받아들입니다. 베트남에서는 방사선에 대한 공포가 더 크고, 치료 받는 환자가 다른 사람에게 '방사능을 옮긴다'는 오해가 있을 수 있어 통역 시 과학적 설명이 필요합니다. 한국 환자들은 피부 화상을 가장 걱정하며, 베트남 환자들은 매일 병원에 와야 하는 것을 부담스러워하는 경향이 있어 치료 스케줄의 중요성을 강조해야 합니다. 치료 부위 피부에 로션, 비누 사용 제한 등 관리 방법을 명확히 전달해야 합니다.",
        "commonMistakes": [
            {
                "mistake": "치료 받으면 방사능이 남아있다고 오해",
                "correction": "외부 방사선치료는 체내 방사능 잔류 없음",
                "explanation": "환자와 가족 불안 해소"
            },
            {
                "mistake": "한두 번 빠져도 괜찮다고 안내",
                "correction": "정해진 횟수 모두 치료해야 효과적",
                "explanation": "치료 순응도 향상"
            },
            {
                "mistake": "피부 관리 방법 교육 생략",
                "correction": "자극적인 비누, 로션 피하기, 긁지 않기 등 구체적 안내",
                "explanation": "부작용 최소화"
            }
        ],
        "examples": [
            {
                "ko": "유방암 수술 후 남은 유방에 총 25회 방사선치료를 시행합니다",
                "vi": "Sau phẫu thuật ung thư vú, xạ trị vùng vú còn lại tổng 25 lần",
                "situation": "formal"
            },
            {
                "ko": "치료 부위는 순한 비누만 사용하고 긁지 마세요",
                "vi": "Vùng xạ trị chỉ dùng xà phòng nhẹ và không gãi",
                "situation": "onsite"
            },
            {
                "ko": "방사선 맞으면 다른 사람한테 방사능 옮기나요?",
                "vi": "Xạ trị có lây phóng xạ cho người khác không?",
                "situation": "informal"
            }
        ],
        "relatedTerms": ["외부방사선치료", "근접방사선치료", "피부반응", "방사선종양학"]
    },
    {
        "slug": "xa-tri-proton",
        "korean": "양성자치료",
        "vietnamese": "Xạ trị proton",
        "hanja": "陽性子治療",
        "hanjaReading": "陽(볕 양) + 性(성품 성) + 子(아들 자) + 治(다스릴 치) + 療(고칠 료)",
        "pronunciation": "싸찌프로통",
        "meaningKo": "양성자빔을 이용한 정밀 방사선치료로, 종양에만 선택적으로 방사선을 전달하여 주변 정상 조직 손상을 최소화합니다. 통역 시 주의할 점은 소아암, 뇌종양, 전립선암 등에 특히 유용하지만 매우 고가이고 치료 가능한 병원이 제한적이라는 점을 환자에게 명확히 전달해야 합니다. 한국에서는 일부 대학병원에만 시설이 있으며, 건강보험 급여가 제한적이어서 환자 부담이 크다는 점을 환자가 오해 없이 이해하도록 통역해야 합니다. 기존 방사선치료와의 차이점과 장점을 명확히 설명해야 합니다.",
        "meaningVi": "Xạ trị chính xác sử dụng chùm proton, truyền phóng xạ chọn lọc vào khối u, giảm thiểu tổn thương mô bình thường xung quanh. Đặc biệt hữu ích cho ung thư trẻ em, u não, ung thư tuyến tiền liệt. Chi phí rất cao, bệnh viện có máy hạn chế.",
        "context": "방사선종양학과 특수 상담, 소아암 치료 계획, 고비용 치료 안내",
        "culturalNote": "한국에서는 양성자치료가 '최첨단 치료'로 인식되며 많은 환자가 희망하지만, 비용(회당 수백만 원)과 접근성 문제로 실제 치료받는 환자는 제한적입니다. 베트남에서는 양성자치료 시설이 거의 없어 해외 원정 치료를 고려하는 경우가 있습니다. 한국 환자들은 '양성자치료면 부작용 없이 완치 가능하다'는 오해를 하는 경우가 있고, 베트남 환자들은 경제적 부담으로 아예 고려하지 못하는 경우가 많아 통역 시 치료의 장점과 한계, 비용을 명확히 전달하여 환자가 현실적인 선택을 할 수 있도록 해야 합니다.",
        "commonMistakes": [
            {
                "mistake": "일반 방사선치료와 같다고 설명",
                "correction": "정밀도 높고 주변 조직 손상 적음",
                "explanation": "치료 선택에 도움이 되는 정보 제공"
            },
            {
                "mistake": "부작용이 전혀 없다고 오해",
                "correction": "일반 방사선보다 적지만 부작용 여전히 있음",
                "explanation": "현실적 기대치 설정"
            },
            {
                "mistake": "보험 적용된다고 안내",
                "correction": "급여 기준 매우 제한적, 대부분 비급여",
                "explanation": "경제적 부담 사전 안내"
            }
        ],
        "examples": [
            {
                "ko": "소아 뇌종양으로 성장 중인 뇌 보호를 위해 양성자치료를 권장합니다",
                "vi": "U não trẻ em, khuyến cáo xạ trị proton để bảo vệ não đang phát triển",
                "situation": "formal"
            },
            {
                "ko": "치료 비용은 약 3000만 원이며 대부분 비급여입니다",
                "vi": "Chi phí điều trị khoảng 30 triệu won, phần lớn không được bảo hiểm",
                "situation": "onsite"
            },
            {
                "ko": "양성자치료 받으면 완치되나요? 부작용은 없나요?",
                "vi": "Xạ trị proton có khỏi hoàn toàn không? Có tác dụng phụ không?",
                "situation": "informal"
            }
        ],
        "relatedTerms": ["방사선치료", "정밀방사선치료", "소아암", "비급여"]
    },
    {
        "slug": "dot-quy",
        "korean": "뇌졸중",
        "vietnamese": "Đột quỵ",
        "hanja": "腦卒中",
        "hanjaReading": "腦(뇌 뇌) + 卒(마칠 졸) + 中(가운데 중)",
        "pronunciation": "돗꾸이",
        "meaningKo": "뇌혈관이 막히거나 터져서 뇌 조직이 손상되는 응급 질환입니다. 통역 시 주의할 점은 '갑자기 한쪽 팔다리 마비, 언어 장애, 심한 두통' 등의 증상 발생 시 골든타임(3-4.5시간) 내 병원 도착이 생명과 예후를 좌우하므로 즉시 119 신고의 중요성을 강조해야 합니다. 한국에서는 뇌경색과 뇌출혈을 구분하며 치료가 완전히 다르고, FAST(Face, Arm, Speech, Time) 캠페인으로 조기 인지를 교육한다는 점을 환자와 가족에게 명확히 전달해야 합니다.",
        "meaningVi": "Bệnh cấp cứu do mạch máu não bị tắc hoặc vỡ làm tổn thương mô não. Triệu chứng: đột ngột liệt một bên chi, rối loạn ngôn ngữ, đau đầu dữ dội. Thời gian vàng 3-4.5 giờ, cần cấp cứu ngay.",
        "context": "응급실, 신경과 외래, 재활의학과, 뇌졸중 예방 교육",
        "culturalNote": "한국에서는 뇌졸중을 '중풍'으로도 부르며, 고령 환자가 많지만 최근 젊은 층에서도 증가하고 있습니다. 베트남에서는 전통 의학으로 먼저 치료하려다 골든타임을 놓치는 경우가 있어 통역 시 즉시 병원 방문의 절대적 필요성을 강조해야 합니다. 한국 환자와 가족은 '침을 맞으면 낫는다'는 민간 요법을 믿는 경우가 있고, 베트남에서도 전통 침술을 선호하는 경향이 있어 현대 의학적 응급 치료(혈전용해제, 혈전제거술)의 중요성을 명확히 전달해야 합니다. 재활 치료의 중요성과 재발 예방(혈압, 당뇨, 콜레스테롤 관리)도 함께 교육해야 합니다.",
        "commonMistakes": [
            {
                "mistake": "뇌경색과 뇌출혈을 구분 않고 '뇌졸중'으로만 번역",
                "correction": "뇌경색(nhồi máu não)과 뇌출혈(xuất huyết não) 명확히 구분",
                "explanation": "치료가 정반대이므로 구분 필수"
            },
            {
                "mistake": "증상이 저절로 좋아지면 병원 안 가도 된다고 오해",
                "correction": "증상 호전되어도 반드시 응급실 방문",
                "explanation": "일과성 뇌허혈발작도 응급 상황"
            },
            {
                "mistake": "골든타임 중요성 설명 누락",
                "correction": "3-4.5시간 내 치료 시작 강조",
                "explanation": "예후 결정적 영향"
            }
        ],
        "examples": [
            {
                "ko": "뇌경색으로 발병 2시간 만에 내원하여 혈전용해제 투여 후 증상 호전되었습니다",
                "vi": "Nhồi máu não, đến viện sau 2 giờ khởi phát, triệu chứng cải thiện sau tiêm thuốc tiêu sợi huyết",
                "situation": "formal"
            },
            {
                "ko": "FAST 기억하세요. 얼굴 처짐, 팔 힘 빠짐, 말이 어눌하면 바로 119",
                "vi": "Nhớ FAST: Mặt chệch, Tay yếu, Nói khó, Thời gian quan trọng - gọi cấp cứu ngay",
                "situation": "onsite"
            },
            {
                "ko": "갑자기 한쪽 팔다리에 힘이 없는데 중풍인가요?",
                "vi": "Đột ngột một bên tay chân yếu, có phải đột quỵ không?",
                "situation": "informal"
            }
        ],
        "relatedTerms": ["뇌경색", "뇌출혈", "혈전용해제", "골든타임"]
    },
    {
        "slug": "nhoi-mau-nao",
        "korean": "뇌경색",
        "vietnamese": "Nhồi máu não",
        "hanja": "腦梗塞",
        "hanjaReading": "腦(뇌 뇌) + 梗(막힐 경) + 塞(막을 색)",
        "pronunciation": "뇌이머우나오",
        "meaningKo": "뇌혈관이 막혀서 뇌 조직으로 혈액 공급이 차단되어 발생하는 허혈성 뇌졸중입니다. 통역 시 주의할 점은 발병 4.5시간 이내 혈전용해제 투여가 가능하며, 큰 혈관 폐색은 기계적 혈전제거술을 시행할 수 있다는 점을 환자와 가족에게 명확히 전달해야 합니다. 한국에서는 고혈압, 당뇨병, 고지혈증, 심방세동 등이 주요 위험 인자이며, 재발 방지를 위해 항혈소판제나 항응고제를 평생 복용해야 한다는 점을 환자가 오해 없이 이해하도록 통역해야 합니다.",
        "meaningVi": "Đột quỵ thiếu máu não do mạch máu não bị tắc, ngừng cung cấp máu đến mô não. Trong 4.5 giờ có thể tiêm thuốc tiêu sợi huyết, tắc mạch lớn có thể lấy huyết khối cơ học.",
        "context": "응급실, 신경과 입원, 재활치료, 재발 예방 교육",
        "culturalNote": "한국에서는 뇌경색 환자에게 즉시 CT나 MRI를 시행하여 진단하고 치료 방침을 결정하지만, 베트남에서는 검사 접근성이 제한적일 수 있습니다. 한국 환자들은 '피를 맑게 하는' 건강식품을 선호하지만 항혈소판제나 항응고제와 상호작용 위험이 있어 주의가 필요하고, 베트남 환자들은 전통 약재로 '혈액순환을 개선'하려는 시도를 할 수 있어 통역 시 약물 상호작용의 위험성을 강조해야 합니다. 재활 치료의 중요성과 조기 시작의 필요성도 명확히 전달해야 합니다.",
        "commonMistakes": [
            {
                "mistake": "뇌출혈과 혼동",
                "correction": "뇌경색은 혈관 막힘, 뇌출혈은 혈관 터짐",
                "explanation": "치료가 정반대 (경색: 항혈소판제, 출혈: 금기)"
            },
            {
                "mistake": "증상 호전되면 약 중단해도 된다고 오해",
                "correction": "평생 항혈소판제/항응고제 복용 필수",
                "explanation": "재발 방지를 위해"
            },
            {
                "mistake": "재활 치료 시작 시기 설명 누락",
                "correction": "급성기 치료 직후부터 재활 시작",
                "explanation": "조기 재활이 예후 결정적"
            }
        ],
        "examples": [
            {
                "ko": "우측 중대뇌동맥 폐색으로 기계적 혈전제거술 시행 후 좌측 편마비가 남았습니다",
                "vi": "Tắc động mạch não giữa bên phải, sau lấy huyết khối cơ học vẫn còn liệt nửa người bên trái",
                "situation": "formal"
            },
            {
                "ko": "아스피린을 평생 복용하고 혈압, 혈당, 콜레스테롤을 잘 관리하세요",
                "vi": "Uống aspirin suốt đời và quản lý tốt huyết áp, đường huyết, cholesterol",
                "situation": "onsite"
            },
            {
                "ko": "뇌경색 왔는데 다리가 안 움직여요. 다시 걸을 수 있나요?",
                "vi": "Bị nhồi máu não mà chân không cử động được. Có đi lại được không?",
                "situation": "informal"
            }
        ],
        "relatedTerms": ["뇌졸중", "혈전용해제", "항혈소판제", "재활치료"]
    },
    {
        "slug": "xuat-huyet-nao",
        "korean": "뇌출혈",
        "vietnamese": "Xuất huyết não",
        "hanja": "腦出血",
        "hanjaReading": "腦(뇌 뇌) + 出(날 출) + 血(피 혈)",
        "pronunciation": "쑤엇후옛나오",
        "meaningKo": "뇌혈관이 터져서 뇌 조직 내로 출혈이 발생하는 출혈성 뇌졸중입니다. 통역 시 주의할 점은 고혈압이 가장 흔한 원인이며, 심한 두통과 의식 저하가 특징적이고, 출혈량과 위치에 따라 수술(혈종 제거술)이 필요할 수 있다는 점을 환자와 가족에게 명확히 전달해야 합니다. 한국에서는 응급 CT로 진단하고 혈압을 조절하며, 뇌경색과 달리 항혈소판제나 항응고제는 금기이고 지혈제를 사용한다는 점을 환자가 오해 없이 이해하도록 통역해야 합니다.",
        "meaningVi": "Đột quỵ xuất huyết não do mạch máu não vỡ, máu tràn vào mô não. Nguyên nhân thường gặp nhất: tăng huyết áp. Triệu chứng đặc trưng: đau đầu dữ dội, rối loạn ý thức. Có thể cần phẫu thuật lấy khối máu tụ.",
        "context": "응급실, 신경외과 및 신경과 입원, 중환자실, 수술 상담",
        "culturalNote": "한국에서는 뇌출혈을 뇌경색보다 더 위험한 것으로 인식하며, 실제로 사망률과 장애율이 높습니다. 베트남에서도 뇌출혈에 대한 두려움이 크며, 전통 의학으로는 치료가 불가능하다는 인식이 있습니다. 한국 환자들은 '수술하면 더 나빠진다'는 두려움으로 수술을 거부하는 경우가 있고, 베트남 환자들은 경제적 부담으로 적극적 치료를 포기하는 경우가 있어 통역 시 수술의 필요성과 비수술 치료의 한계를 균형 있게 전달해야 합니다. 혈압 조절의 절대적 중요성을 강조해야 합니다.",
        "commonMistakes": [
            {
                "mistake": "뇌경색과 같은 치료를 한다고 설명",
                "correction": "항혈소판제/항응고제 금기, 지혈 치료",
                "explanation": "치료가 정반대"
            },
            {
                "mistake": "수술이 항상 필요하다고 오해",
                "correction": "출혈량, 위치에 따라 보존적 치료 가능",
                "explanation": "불필요한 불안 방지"
            },
            {
                "mistake": "혈압 조절 중요성 설명 누락",
                "correction": "고혈압이 주 원인, 철저한 혈압 관리 필수",
                "explanation": "재발 방지"
            }
        ],
        "examples": [
            {
                "ko": "기저핵 출혈 30mL로 보존적 치료 중이며 혈압을 140/90 이하로 유지합니다",
                "vi": "Xuất huyết hạch nền 30mL, đang điều trị nội khoa và duy trì huyết áp dưới 140/90",
                "situation": "formal"
            },
            {
                "ko": "혈압약을 규칙적으로 복용하고 술, 담배를 끊으세요",
                "vi": "Uống thuốc huyết áp đều đặn và bỏ rượu, thuốc lá",
                "situation": "onsite"
            },
            {
                "ko": "뇌출혈이면 수술해야 하나요? 수술 안 하면 어떻게 되나요?",
                "vi": "Xuất huyết não có cần phẫu thuật không? Không mổ thì sao?",
                "situation": "informal"
            }
        ],
        "relatedTerms": ["뇌졸중", "고혈압", "혈종제거술", "뇌압상승"]
    },
    {
        "slug": "thieu-mau-nao-thoang-qua",
        "korean": "일과성뇌허혈발작",
        "vietnamese": "Thiếu máu não thoáng qua",
        "hanja": "一過性腦虛血發作",
        "hanjaReading": "一(한 일) + 過(지날 과) + 性(성품 성) + 腦(뇌 뇌) + 虛(빌 허) + 血(피 혈) + 發(필 발) + 作(지을 작)",
        "pronunciation": "티에우머우나오탕꽈",
        "meaningKo": "뇌혈관이 일시적으로 막혔다가 다시 열려 신경 증상이 24시간 이내 완전히 회복되는 상태로, 뇌졸중의 경고 신호입니다. 통역 시 주의할 점은 증상이 저절로 좋아졌다고 병원에 안 가면 안 되며, TIA 후 며칠 내 뇌경색으로 진행할 위험이 매우 높으므로 즉시 응급실 방문이 필수적이라는 점을 환자와 가족에게 명확히 전달해야 합니다. 한국에서는 TIA도 응급 상황으로 인식하고 입원하여 정밀 검사(혈관 영상, 심장 검사)를 시행하며, 재발 방지 약물을 시작한다는 점을 환자가 오해 없이 이해하도록 통역해야 합니다.",
        "meaningVi": "Mạch máu não tắc tạm thời rồi mở lại, triệu chứng thần kinh hồi phục hoàn toàn trong 24 giờ. Là dấu hiệu cảnh báo đột quỵ. Nguy cơ rất cao tiến triển thành nhồi máu não trong vài ngày, cần cấp cứu ngay.",
        "context": "응급실, 신경과 외래, 뇌졸중 예방 클리닉",
        "culturalNote": "한국에서는 TIA를 '미니 뇌졸중'으로 이해하지만 증상이 회복되어 대수롭지 않게 생각하는 환자가 많아 교육이 중요합니다. 베트남에서는 증상이 사라지면 병원에 가지 않는 경향이 더 강해 통역 시 응급 상황임을 강조해야 합니다. 한국 환자들은 '한쪽 눈이 잠깐 안 보였다'거나 '손에 힘이 빠졌다가 괜찮아졌다'는 증상을 대수롭지 않게 여기고, 베트남 환자들은 전통 침술로 해결하려는 경향이 있어 즉시 병원 방문의 중요성을 명확히 전달해야 합니다. ABCD2 점수로 위험도를 평가한다는 점도 설명할 수 있습니다.",
        "commonMistakes": [
            {
                "mistake": "증상이 사라졌으니 괜찮다고 안심",
                "correction": "TIA는 뇌졸중의 경고 신호, 즉시 응급실",
                "explanation": "며칠 내 뇌경색 위험 매우 높음"
            },
            {
                "mistake": "'Mini đột quỵ'로만 설명하여 심각성 간과",
                "correction": "일시적이지만 응급 상황임을 강조",
                "explanation": "환자가 대수롭지 않게 생각하지 않도록"
            },
            {
                "mistake": "정밀 검사 필요성 설명 누락",
                "correction": "원인 찾기 위한 혈관 영상, 심장 검사 필수",
                "explanation": "재발 방지 치료 계획 수립"
            }
        ],
        "examples": [
            {
                "ko": "일과성 뇌허혈발작으로 MRA에서 경동맥 70% 협착 발견되어 스텐트 시술 권장합니다",
                "vi": "Thiếu máu não thoáng qua, MRA phát hiện hẹp động mạch cảnh 70%, khuyến cáo đặt stent",
                "situation": "formal"
            },
            {
                "ko": "증상이 사라졌어도 반드시 약을 복용하고 추적 검사를 받으세요",
                "vi": "Dù triệu chứng hết vẫn phải uống thuốc và tái khám định kỳ",
                "situation": "onsite"
            },
            {
                "ko": "한쪽 눈이 안 보였다가 나았는데 괜찮은 건가요?",
                "vi": "Một bên mắt không nhìn thấy rồi hết, có sao không?",
                "situation": "informal"
            }
        ],
        "relatedTerms": ["뇌경색", "경동맥협착", "항혈소판제", "뇌졸중예방"]
    },
    {
        "slug": "benh-parkinson",
        "korean": "파킨슨병",
        "vietnamese": "Bệnh Parkinson",
        "hanja": None,
        "hanjaReading": None,
        "pronunciation": "벵파킨손",
        "meaningKo": "뇌의 도파민 신경세포가 소실되어 운동 기능이 저하되는 퇴행성 뇌 질환입니다. 통역 시 주의할 점은 '안정 떨림, 근육 경직, 느린 움직임, 자세 불안정' 4대 증상을 정확히 전달해야 하며, 완치는 불가능하지만 약물 치료로 증상 조절이 가능하다는 점을 환자와 가족에게 명확히 전달해야 합니다. 한국에서는 레보도파가 주 치료 약물이며, 초기에는 효과적이지만 장기 복용 시 약효 감소와 이상운동증이 나타날 수 있다는 점을 환자가 오해 없이 이해하도록 통역해야 합니다.",
        "meaningVi": "Bệnh thoái hóa não do mất tế bào thần kinh dopamine, giảm chức năng vận động. 4 triệu chứng chính: run khi nghỉ, cứng cơ, chậm chạp, mất thăng bằng tư thế. Không chữa khỏi nhưng kiểm soát triệu chứng bằng thuốc.",
        "context": "신경과 외래, 운동장애 클리닉, 장기 관리 교육",
        "culturalNote": "한국에서는 고령화로 파킨슨병 환자가 증가하고 있으며, '손 떨림 = 파킨슨병'으로 오해하는 경우가 많아 본태성 떨림과 구별이 필요합니다. 베트남에서는 노화의 자연스러운 과정으로 여겨 진단이 늦어질 수 있습니다. 한국 환자들은 약물 의존을 걱정하지만 파킨슨병은 약물 치료가 필수이며, 베트남 환자들은 전통 약재나 침술로 치료하려는 시도를 할 수 있어 통역 시 레보도파 치료의 필요성을 강조해야 합니다. 운동과 재활의 중요성, 낙상 예방도 함께 교육해야 합니다.",
        "commonMistakes": [
            {
                "mistake": "모든 떨림을 파킨슨병으로 설명",
                "correction": "본태성 떨림(동작 시)과 파킨슨병(안정 시) 구분",
                "explanation": "진단 오류 방지"
            },
            {
                "mistake": "완치 가능하다고 오해 조성",
                "correction": "퇴행성 질환으로 완치 불가, 증상 관리 가능",
                "explanation": "현실적 기대치 설정"
            },
            {
                "mistake": "약효 감소 문제 설명 누락",
                "correction": "장기 복용 시 약효 변동, 이상운동증 가능성",
                "explanation": "환자가 미래 변화에 대비하도록"
            }
        ],
        "examples": [
            {
                "ko": "파킨슨병 진단되어 레보도파 치료를 시작하고 규칙적인 운동을 권장합니다",
                "vi": "Chẩn đoán bệnh Parkinson, bắt đầu điều trị levodopa và khuyến cáo tập thể dục đều đặn",
                "situation": "formal"
            },
            {
                "ko": "약 효과가 떨어지는 시간에는 낙상 조심하고 활동을 줄이세요",
                "vi": "Khi thuốc hết tác dụng cẩn thận ngã và giảm hoạt động",
                "situation": "onsite"
            },
            {
                "ko": "손이 떨리는데 파킨슨병인가요? 나을 수 있나요?",
                "vi": "Tay run có phải bệnh Parkinson không? Có khỏi được không?",
                "situation": "informal"
            }
        ],
        "relatedTerms": ["레보도파", "도파민", "이상운동증", "운동장애"]
    },
    {
        "slug": "benh-alzheimer",
        "korean": "알츠하이머병",
        "vietnamese": "Bệnh Alzheimer",
        "hanja": None,
        "hanjaReading": None,
        "pronunciation": "벵안쯔하이머",
        "meaningKo": "뇌에 베타 아밀로이드와 타우 단백질이 축적되어 기억력과 인지 기능이 점진적으로 저하되는 치매의 가장 흔한 원인입니다. 통역 시 주의할 점은 초기에는 최근 기억력 저하가 주 증상이며, 진행하면서 언어, 판단력, 일상생활 능력이 떨어진다는 점을 환자와 보호자에게 명확히 전달해야 합니다. 한국에서는 치매 조기 검진을 권장하며, 완치는 불가능하지만 약물 치료(도네페질 등)로 진행을 늦출 수 있고, 보호자 교육과 지원이 매우 중요하다는 점을 가족이 오해 없이 이해하도록 통역해야 합니다.",
        "meaningVi": "Nguyên nhân thường gặp nhất của sa sút trí tuệ do tích tụ protein beta amyloid và tau trong não, làm giảm dần trí nhớ và chức năng nhận thức. Giai đoạn đầu: giảm trí nhớ gần, sau đó ảnh hưởng ngôn ngữ, phán đoán, sinh hoạt hàng ngày.",
        "context": "신경과 외래, 치매 클리닉, 보호자 상담 및 교육",
        "culturalNote": "한국에서는 고령화로 치매 환자가 급증하고 있으며, '건망증'과 '치매'를 구별하지 못하는 경우가 많아 교육이 중요합니다. 베트남에서는 노화의 자연스러운 과정으로 여겨 진단과 치료가 늦어질 수 있습니다. 한국 가족들은 치매 진단을 받아들이기 어려워하며 '부모님이 치매라니 믿을 수 없다'는 반응을 보이고, 베트남에서는 가족이 집에서 돌보는 것이 당연시되어 시설 입소를 고려하지 않는 경향이 있어 통역 시 보호자의 소진 방지와 지원 체계를 안내해야 합니다. 조기 진단과 약물 치료, 인지 훈련의 중요성을 강조해야 합니다.",
        "commonMistakes": [
            {
                "mistake": "건망증과 치매를 같다고 설명",
                "correction": "건망증은 정상 노화, 치매는 병적 상태",
                "explanation": "조기 진단의 중요성 인식"
            },
            {
                "mistake": "약물 치료가 완치시킨다고 오해",
                "correction": "진행 늦추는 것이 목표, 완치 불가",
                "explanation": "현실적 기대치 설정"
            },
            {
                "mistake": "보호자 교육 및 지원 정보 제공 누락",
                "correction": "보호자 부담 크므로 지원 체계 안내",
                "explanation": "보호자 소진 방지"
            }
        ],
        "examples": [
            {
                "ko": "알츠하이머병 초기로 도네페질 처방하고 인지 훈련 프로그램 참여를 권장합니다",
                "vi": "Alzheimer giai đoạn sớm, kê đơn donepezil và khuyến cáo tham gia chương trình huấn luyện nhận thức",
                "situation": "formal"
            },
            {
                "ko": "가스불 끄는 것 잊을 수 있으니 안전 장치를 설치하세요",
                "vi": "Có thể quên tắt bếp ga, hãy lắp thiết bị an toàn",
                "situation": "onsite"
            },
            {
                "ko": "자꾸 같은 말 반복하고 깜빡깜빡하는데 치매인가요?",
                "vi": "Cứ lặp lại câu nói và hay quên, có phải sa sút trí tuệ không?",
                "situation": "informal"
            }
        ],
        "relatedTerms": ["치매", "도네페질", "인지기능검사", "보호자교육"]
    },
    {
        "slug": "dong-kinh",
        "korean": "간질",
        "vietnamese": "Động kinh",
        "hanja": "癎疾",
        "hanjaReading": "癎(간질 간) + 疾(병 질)",
        "pronunciation": "동낑",
        "meaningKo": "뇌의 비정상적인 전기 활동으로 반복적인 발작이 나타나는 신경계 질환으로, 현대 의학에서는 '뇌전증'이라는 용어를 선호합니다. 통역 시 주의할 점은 '간질'이라는 용어가 사회적 낙인이 있어 '뇌전증'으로 번역하는 것이 권장되며, 발작 유형(전신 발작, 부분 발작)에 따라 증상과 치료가 다르다는 점을 환자와 가족에게 명확히 전달해야 합니다. 한국에서는 항경련제로 발작을 조절하며, 약물 순응도가 매우 중요하고, 임의로 약을 중단하면 발작이 재발하거나 뇌전증지속상태로 악화될 수 있다는 점을 환자가 오해 없이 이해하도록 통역해야 합니다.",
        "meaningVi": "Bệnh lý thần kinh do hoạt động điện bất thường trong não gây co giật tái phát. Thuật ngữ hiện đại: 'bệnh não' thay vì 'động kinh' để giảm kỳ thị. Phân loại: co giật toàn thân, co giật cục bộ. Điều trị bằng thuốc chống co giật, cần tuân thủ nghiêm ngặt.",
        "context": "신경과 외래, 응급실(발작 시), 약물 순응도 교육",
        "culturalNote": "한국에서는 '간질'이라는 용어가 사회적 낙인과 차별을 초래하여 2017년부터 공식적으로 '뇌전증'으로 명칭을 변경했지만, 여전히 많은 환자와 가족이 진단을 숨기려는 경향이 있습니다. 베트남에서도 'động kinh'에 대한 부정적 인식이 강하며, 전통적으로 귀신이 들렸다고 생각하는 경우가 있어 통역 시 과학적 설명과 함께 사회적 인식 개선의 필요성을 전달해야 합니다. 한국 환자들은 운전면허 제한, 직업 제한 등을 걱정하며, 베트남 환자들은 결혼과 출산에 대한 우려가 크므로 통역 시 적절한 치료로 정상 생활이 가능함을 강조해야 합니다.",
        "commonMistakes": [
            {
                "mistake": "'간질'을 그대로 'Động kinh'으로 번역",
                "correction": "'Bệnh não' 또는 'Bệnh động kinh não' 사용 권장",
                "explanation": "낙인 감소를 위한 용어 개선"
            },
            {
                "mistake": "약을 먹다가 발작 없으면 중단해도 된다고 오해",
                "correction": "의사 판단 없이 약 중단 절대 금지",
                "explanation": "발작 재발 및 뇌전증지속상태 위험"
            },
            {
                "mistake": "발작 시 입에 물건 넣으라고 안내",
                "correction": "발작 시 머리 보호, 옆으로 눕히기, 입에 아무것도 넣지 않기",
                "explanation": "질식 위험 및 치아 손상 방지"
            }
        ],
        "examples": [
            {
                "ko": "전신 강직간대 발작으로 뇌전증 진단되어 항경련제 레베티라세탐을 시작합니다",
                "vi": "Co giật cứng co toàn thân, chẩn đoán bệnh não, bắt đầu thuốc chống co giật levetiracetam",
                "situation": "formal"
            },
            {
                "ko": "매일 같은 시간에 약을 복용하고 의사와 상의 없이 절대 중단하지 마세요",
                "vi": "Uống thuốc cùng giờ mỗi ngày và tuyệt đối không tự ý ngừng thuốc",
                "situation": "onsite"
            },
            {
                "ko": "뇌전증 있으면 운전면허 못 따나요? 결혼하면 애기한테 유전되나요?",
                "vi": "Bệnh não có lấy bằng lái xe không? Kết hôn có di truyền cho con không?",
                "situation": "informal"
            }
        ],
        "relatedTerms": ["뇌전증", "항경련제", "발작", "뇌파검사"]
    },
    {
        "slug": "da-phat-xuong-hoa",
        "korean": "다발성경화증",
        "vietnamese": "Đa phát xơ hóa",
        "hanja": "多發性硬化症",
        "hanjaReading": "多(많을 다) + 發(필 발) + 性(성품 성) + 硬(굳을 경) + 化(될 화) + 症(병 증)",
        "pronunciation": "다팟써호아",
        "meaningKo": "중추신경계의 수초(myelin)가 면역 반응으로 손상되어 다양한 신경 증상이 재발과 완화를 반복하는 자가면역 질환입니다. 통역 시 주의할 점은 '시력 저하, 사지 마비, 감각 이상, 보행 장애' 등 증상이 매우 다양하며, 재발 방지를 위한 면역조절제 치료가 중요하다는 점을 환자에게 명확히 전달해야 합니다. 한국에서는 서양인보다 유병률이 낮지만 최근 증가 추세이며, MRI에서 특징적인 다발성 병변을 확인하여 진단하고, 급성기에는 스테로이드 치료를 시행한다는 점을 환자가 오해 없이 이해하도록 통역해야 합니다.",
        "meaningVi": "Bệnh tự miễn do tổn thương vỏ myelin hệ thần kinh trung ương, gây triệu chứng thần kinh đa dạng tái phát và thuyên giảm luân phiên. Triệu chứng: giảm thị lực, liệt chi, rối loạn cảm giác, rối loạn đi lại. Điều trị điều hòa miễn dịch để ngăn tái phát.",
        "context": "신경과 외래, 면역조절제 치료, 재발 관리",
        "culturalNote": "한국에서는 다발성경화증이 희귀 질환으로 분류되어 진단이 늦어지는 경우가 많으며, 환자들은 질환에 대한 정보가 부족하여 불안해합니다. 베트남에서는 더욱 드물고 진단 시설도 제한적일 수 있습니다. 한국 환자들은 '완치 가능성'을 묻지만 평생 관리가 필요한 만성 질환임을 수용하는 데 시간이 걸리며, 베트남 환자들은 전통 의학으로 치료하려는 시도를 할 수 있어 통역 시 면역조절제 치료의 필요성과 재발 방지의 중요성을 강조해야 합니다. 젊은 여성에서 많이 발생하므로 임신 계획과 관련된 상담도 중요합니다.",
        "commonMistakes": [
            {
                "mistake": "'Xơ cứng'으로만 번역하여 혼란",
                "correction": "'Đa phát xơ hóa' 또는 'Multiple sclerosis (MS)' 병기",
                "explanation": "정확한 질환명 전달"
            },
            {
                "mistake": "완치 가능하다고 오해 조성",
                "correction": "만성 질환으로 재발 방지가 목표",
                "explanation": "현실적 기대치 설정"
            },
            {
                "mistake": "증상 호전되면 약 중단해도 된다고 안내",
                "correction": "증상 없어도 재발 방지 위해 지속 치료 필요",
                "explanation": "재발 예방"
            }
        ],
        "examples": [
            {
                "ko": "MRI에서 뇌와 척수에 다발성 병변 확인되어 다발성경화증 진단, 인터페론 치료를 시작합니다",
                "vi": "MRI xác nhận tổn thương đa ổ não và tủy sống, chẩn đoán đa phát xơ hóa, bắt đầu điều trị interferon",
                "situation": "formal"
            },
            {
                "ko": "재발 증상(시력 저하, 팔다리 저림) 나타나면 즉시 연락하세요",
                "vi": "Nếu có triệu chứng tái phát (giảm thị lực, tê chân tay) hãy liên hệ ngay",
                "situation": "onsite"
            },
            {
                "ko": "다발성경화증 있으면 임신하면 안 되나요?",
                "vi": "Đa phát xơ hóa có mang thai được không?",
                "situation": "informal"
            }
        ],
        "relatedTerms": ["자가면역질환", "수초", "면역조절제", "MRI"]
    },
    {
        "slug": "xuong-hoa-cung-co-tac",
        "korean": "근위축성측삭경화증",
        "vietnamese": "Xơ hóa cứng cơ tắc",
        "hanja": "筋萎縮性側索硬化症",
        "hanjaReading": "筋(힘줄 근) + 萎(시들 위) + 縮(줄 축) + 性(성품 성) + 側(곁 측) + 索(노끈 삭) + 硬(굳을 경) + 化(될 화) + 症(병 증)",
        "pronunciation": "써호아꾸엉꺼딱",
        "meaningKo": "운동신경세포가 퇴행하여 근육이 점차 약화되고 위축되는 희귀 난치성 신경계 질환으로, ALS 또는 루게릭병으로도 불립니다. 통역 시 주의할 점은 팔다리 근력 약화로 시작하여 점차 호흡근과 연하근을 침범하여 결국 인공호흡기와 위루술이 필요하게 되는 진행성 질환이라는 점을 환자와 가족에게 신중하고 명확하게 전달해야 합니다. 한국에서는 진단 후 평균 생존 기간이 3-5년이지만 개인차가 크며, 릴루졸이라는 약물로 진행을 약간 늦출 수 있고, 호스피스와 완화 의료에 대한 상담이 중요하다는 점을 환자가 오해 없이 이해하도록 통역해야 합니다.",
        "meaningVi": "Bệnh lý thần kinh thoái hóa hiếm gặp do tế bào thần kinh vận động thoái hóa làm cơ yếu và teo dần. Gọi là ALS hoặc bệnh Lou Gehrig. Bệnh tiến triển, cuối cùng cần thở máy và đặt ống dạ dày. Thời gian sống trung bình 3-5 năm.",
        "context": "신경과 외래, 호흡재활, 영양 상담, 호스피스 연계",
        "culturalNote": "한국에서는 ALS를 '루게릭병'으로 더 많이 알고 있으며, 진단을 받은 환자와 가족은 극심한 충격과 절망에 빠집니다. 베트남에서는 질환에 대한 인식이 낮고 진단 시설도 제한적일 수 있습니다. 한국 환자들은 '기적적인 완치'를 바라며 검증되지 않은 치료를 찾는 경우가 많고, 베트남 환자들도 전통 의학이나 민간 요법에 의지하려는 경향이 있어 통역 시 현재 의학적으로 완치가 불가능함을 공감적으로 전달하면서도 증상 관리와 삶의 질 유지가 가능함을 강조해야 합니다. 연명 치료에 대한 환자의 의사 결정을 존중하는 것도 중요합니다.",
        "commonMistakes": [
            {
                "mistake": "완치 가능성이 있다고 희망 주기",
                "correction": "현재 완치 불가, 진행 늦추는 것이 목표",
                "explanation": "정직하고 공감적인 의사소통"
            },
            {
                "mistake": "예후 정보 전달 회피",
                "correction": "환자와 가족이 미래 계획 세울 수 있도록 정보 제공",
                "explanation": "연명 치료, 호스피스 등 의사 결정 지원"
            },
            {
                "mistake": "'Lou Gehrig'을 '루 게릭'으로만 음역",
                "correction": "'Bệnh Lou Gehrig (ALS)' 병기",
                "explanation": "환자 이해도 향상"
            }
        ],
        "examples": [
            {
                "ko": "근위축성측삭경화증으로 진단되어 릴루졸 치료를 시작하고 호흡 및 영양 관리를 병행합니다",
                "vi": "Chẩn đoán xơ hóa cứng cơ tắc (ALS), bắt đầu điều trị riluzole và quản lý hô hấp, dinh dưỡng",
                "situation": "formal"
            },
            {
                "ko": "호흡 근력 약화 시 비침습적 인공호흡기 사용을 고려합니다",
                "vi": "Khi cơ hô hấp yếu xem xét dùng máy thở không xâm lấn",
                "situation": "onsite"
            },
            {
                "ko": "ALS라면 살 수 있는 시간이 얼마나 되나요?",
                "vi": "Nếu bị ALS còn sống được bao lâu?",
                "situation": "informal"
            }
        ],
        "relatedTerms": ["ALS", "루게릭병", "릴루졸", "호흡재활"]
    },
    {
        "slug": "u-yeu-co-nang",
        "korean": "중증근무력증",
        "vietnamese": "U yếu cơ nặng",
        "hanja": "重症筋無力症",
        "hanjaReading": "重(무거울 중) + 症(병 증) + 筋(힘줄 근) + 無(없을 무) + 力(힘 력) + 症(병 증)",
        "pronunciation": "우이에우꺼낭",
        "meaningKo": "신경근 접합부의 자가면역 질환으로 아세틸콜린 수용체에 대한 항체로 인해 근육이 쉽게 피로해지는 질환입니다. 통역 시 주의할 점은 '눈꺼풀 처짐, 복시, 씹기·삼키기·말하기 어려움, 팔다리 근력 약화' 등의 증상이 활동 후 악화되고 휴식 후 호전되는 특징을 환자에게 명확히 전달해야 합니다. 한국에서는 항콜린에스터레이즈제와 면역억제제로 치료하며, 흉선종이 동반된 경우 흉선절제술이 필요하고, 근무력 위기 시 인공호흡기 치료가 필요할 수 있다는 점을 환자가 오해 없이 이해하도록 통역해야 합니다.",
        "meaningVi": "Bệnh tự miễn tại khớp thần kinh cơ do kháng thể chống thụ thể acetylcholine làm cơ dễ mệt. Triệu chứng: mi mắt sụp, nhìn đôi, khó nhai/nuốt/nói, yếu cơ tứ chi. Triệu chứng nặng hơn sau hoạt động, giảm sau nghỉ ngơi.",
        "context": "신경과 외래, 흉부외과 협진, 면역치료",
        "culturalNote": "한국에서는 중증근무력증이 희귀 질환으로 초기 진단이 늦어지는 경우가 많으며, 환자들은 '근력이 약하다'는 증상을 대수롭지 않게 생각하다가 중증으로 진행하는 경우가 있습니다. 베트남에서는 질환에 대한 인식이 더 낮고 진단 시설도 제한적일 수 있습니다. 한국 환자들은 '힘이 없다'는 증상을 단순 피로로 오해하고, 베트남 환자들은 전통 보약으로 해결하려는 경향이 있어 통역 시 자가면역 질환임을 명확히 설명하고 면역치료의 필요성을 강조해야 합니다. 스테로이드 부작용에 대한 우려도 함께 다뤄야 합니다.",
        "commonMistakes": [
            {
                "mistake": "단순 근력 약화로 설명",
                "correction": "자가면역 질환으로 특징적 변동성 있음",
                "explanation": "정확한 진단과 치료를 위해"
            },
            {
                "mistake": "운동하면 좋아진다고 안내",
                "correction": "활동 후 악화, 휴식 후 호전이 특징",
                "explanation": "잘못된 조언으로 증상 악화 방지"
            },
            {
                "mistake": "흉선종 검사 필요성 누락",
                "correction": "CT로 흉선종 확인 필수",
                "explanation": "흉선절제술 필요 여부 판단"
            }
        ],
        "examples": [
            {
                "ko": "중증근무력증으로 항콜린에스터레이즈제와 스테로이드 치료를 시작하고 흉부 CT로 흉선종 검사합니다",
                "vi": "Chẩn đoán u yếu cơ nặng, bắt đầu điều trị thuốc chống cholinesterase và corticosteroid, CT ngực kiểm tra u tuyến ức",
                "situation": "formal"
            },
            {
                "ko": "오후에 증상이 심해지면 휴식을 취하고 약을 시간 맞춰 복용하세요",
                "vi": "Nếu triệu chứng nặng vào chiều hãy nghỉ ngơi và uống thuốc đúng giờ",
                "situation": "onsite"
            },
            {
                "ko": "눈꺼풀이 처지고 오후만 되면 힘이 빠지는데 무슨 병인가요?",
                "vi": "Mi mắt sụp và chiều nào cũng yếu, bị bệnh gì vậy?",
                "situation": "informal"
            }
        ],
        "relatedTerms": ["자가면역질환", "항콜린에스터레이즈제", "흉선종", "근무력위기"]
    },
    {
        "slug": "guillain-barre",
        "korean": "길랭바레증후군",
        "vietnamese": "Hội chứng Guillain-Barré",
        "hanja": None,
        "hanjaReading": None,
        "pronunciation": "호이쯩기앙바레",
        "meaningKo": "감염 후 면역 반응으로 말초신경의 수초가 손상되어 급성 이완성 마비가 나타나는 질환입니다. 통역 시 주의할 점은 다리부터 시작하여 위로 올라가는 상행성 마비가 특징이며, 호흡근을 침범하면 인공호흡기 치료가 필요한 응급 상황이라는 점을 환자와 가족에게 명확히 전달해야 합니다. 한국에서는 감기나 장염 후 1-2주 뒤 발생하며, 면역글로불린 정맥 주사나 혈장교환술로 치료하고, 대부분 회복되지만 수개월이 걸릴 수 있다는 점을 환자가 오해 없이 이해하도록 통역해야 합니다.",
        "meaningVi": "Bệnh lý do phản ứng miễn dịch sau nhiễm trùng làm tổn thương vỏ myelin thần kinh ngoại biên, gây liệt mềm cấp tính. Đặc trưng: liệt tăng dần từ chân lên trên. Nếu ảnh hưởng cơ hô hấp cần thở máy cấp cứu.",
        "context": "응급실, 신경과 입원, 중환자실, 재활치료",
        "culturalNote": "한국에서는 길랭바레증후군이 희귀하지만 응급 질환으로 인식되며, 환자와 가족은 갑작스러운 마비에 큰 충격을 받습니다. 베트남에서는 질환에 대한 인식이 낮고 초기 대응이 늦어질 수 있습니다. 한국 환자들은 '감기 때문에 마비가 왔다'는 것을 이해하기 어려워하고, 베트남 환자들은 전통 침술이나 마사지로 치료하려는 시도를 할 수 있어 통역 시 면역 질환임을 명확히 설명하고 면역글로불린 치료의 시급성을 강조해야 합니다. 대부분 회복되지만 시간이 걸린다는 점과 재활의 중요성도 전달해야 합니다.",
        "commonMistakes": [
            {
                "mistake": "뇌졸중과 혼동",
                "correction": "말초신경 질환으로 뇌졸중과 다름",
                "explanation": "정확한 진단과 치료를 위해"
            },
            {
                "mistake": "회복 안 된다고 절망 조성",
                "correction": "대부분 회복되지만 수개월 소요",
                "explanation": "희망적 예후 전달"
            },
            {
                "mistake": "호흡 감시 중요성 누락",
                "correction": "호흡근 마비 가능성, 집중 모니터링 필요",
                "explanation": "생명 위협 상황 예방"
            }
        ],
        "examples": [
            {
                "ko": "길랭바레증후군으로 면역글로불린 정맥 주사 치료를 시작하고 호흡 기능을 집중 감시합니다",
                "vi": "Hội chứng Guillain-Barré, bắt đầu điều trị truyền miễn dịch cầu tĩnh mạch và theo dõi sát chức năng hô hấp",
                "situation": "formal"
            },
            {
                "ko": "지금은 걷기 어렵지만 몇 개월 재활 치료하면 대부분 회복됩니다",
                "vi": "Bây giờ khó đi lại nhưng sau vài tháng phục hồi chức năng phần lớn hồi phục",
                "situation": "onsite"
            },
            {
                "ko": "감기 앓고 나서 다리에 힘이 없는데 회복되나요?",
                "vi": "Sau cúm chân yếu, có hồi phục không?",
                "situation": "informal"
            }
        ],
        "relatedTerms": ["상행성마비", "면역글로불린", "혈장교환술", "호흡마비"]
    },
    {
        "slug": "dau-than-kinh-tam-xoa",
        "korean": "삼차신경통",
        "vietnamese": "Đau thần kinh tam xoa",
        "hanja": "三叉神經痛",
        "hanjaReading": "三(석 삼) + 叉(갈래 차) + 神(귀신 신) + 經(경서 경) + 痛(아플 통)",
        "pronunciation": "다우탄낑땀쏘아",
        "meaningKo": "얼굴의 감각을 담당하는 삼차신경에 발생하는 극심한 통증으로, '전기가 오는 듯한' 발작성 통증이 특징입니다. 통역 시 주의할 점은 세수, 양치질, 바람 등 사소한 자극에도 통증이 유발되며, 항경련제(카바마제핀)가 1차 치료이고 약물 치료에 반응하지 않으면 수술을 고려한다는 점을 환자에게 명확히 전달해야 합니다. 한국에서는 치과 질환으로 오인하여 발치를 하는 경우가 있고, MRI로 혈관 압박 여부를 확인하며, 미세혈관감압술로 근본 원인을 제거할 수 있다는 점을 환자가 오해 없이 이해하도록 통역해야 합니다.",
        "meaningVi": "Đau dữ dội thần kinh tam xoa (thần kinh cảm giác mặt), đau như bị điện giật từng cơn. Tác nhân kích thích nhỏ như rửa mặt, đánh răng, gió cũng gây đau. Điều trị đầu tiên: thuốc chống co giật (carbamazepine). Nếu không đáp ứng thuốc xem xét phẫu thuật.",
        "context": "신경과 외래, 통증 클리닉, 신경외과 수술 상담",
        "culturalNote": "한국에서는 삼차신경통을 '안면 신경통'으로 잘못 부르는 경우가 많으며, 치통으로 오해하여 치과를 먼저 방문하는 환자가 많습니다. 베트남에서도 치과 질환으로 오인하는 경우가 많고, 전통 침술이나 마사지로 치료하려는 시도를 할 수 있어 통역 시 신경과 질환임을 명확히 설명하고 항경련제 치료의 효과를 강조해야 합니다. 한국 환자들은 극심한 통증으로 일상생활이 불가능하여 절망하는 경우가 많고, 베트남 환자들도 통증으로 인한 삶의 질 저하가 심하므로 통역 시 적절한 치료로 통증 조절이 가능함을 강조해야 합니다.",
        "commonMistakes": [
            {
                "mistake": "치통으로 오역",
                "correction": "삼차신경 통증으로 치과 질환 아님",
                "explanation": "불필요한 치과 치료 방지"
            },
            {
                "mistake": "진통제로 치료 가능하다고 안내",
                "correction": "항경련제가 1차 치료",
                "explanation": "정확한 치료 정보 제공"
            },
            {
                "mistake": "수술이 위험하다고 과장",
                "correction": "미세혈관감압술은 효과적이고 안전",
                "explanation": "약물 무효 시 수술 고려 가능하도록"
            }
        ],
        "examples": [
            {
                "ko": "삼차신경통으로 카바마제핀 치료를 시작하고 MRI로 혈관 압박 여부를 확인합니다",
                "vi": "Đau thần kinh tam xoa, bắt đầu điều trị carbamazepine và MRI kiểm tra chèn ép mạch máu",
                "situation": "formal"
            },
            {
                "ko": "양치질이나 세수 시 통증 유발될 수 있으니 부드럽게 하세요",
                "vi": "Đánh răng hoặc rửa mặt có thể gây đau, hãy nhẹ nhàng",
                "situation": "onsite"
            },
            {
                "ko": "얼굴 한쪽이 전기 오듯이 아픈데 치아 문제인가요?",
                "vi": "Một bên mặt đau như bị điện giật, có phải răng không?",
                "situation": "informal"
            }
        ],
        "relatedTerms": ["안면통", "카바마제핀", "미세혈관감압술", "신경통"]
    },
    {
        "slug": "liet-day-than-kinh-mat",
        "korean": "안면신경마비",
        "vietnamese": "Liệt dây thần kinh mặt",
        "hanja": "顔面神經痲痺",
        "hanjaReading": "顔(낯 안) + 面(낯 면) + 神(귀신 신) + 經(경서 경) + 痲(저릴 마) + 痺(저릴 비)",
        "pronunciation": "리엣자이탄낑맛",
        "meaningKo": "얼굴 근육을 움직이는 안면신경이 마비되어 얼굴 한쪽이 움직이지 않는 질환으로, 벨마비가 가장 흔합니다. 통역 시 주의할 점은 '눈을 감을 수 없음, 이마 주름이 없어짐, 입이 한쪽으로 돌아감' 등의 증상을 정확히 전달해야 하며, 초기 스테로이드 치료가 예후에 중요하고 눈 보호를 위한 인공눈물과 안대 사용이 필수적이라는 점을 환자에게 명확히 전달해야 합니다. 한국에서는 대부분 회복되지만 수개월이 걸릴 수 있으며, 뇌졸중과 감별이 중요하다는 점을 환자가 오해 없이 이해하도록 통역해야 합니다.",
        "meaningVi": "Liệt thần kinh mặt khiến một bên mặt không cử động được, thường gặp nhất là liệt Bell. Triệu chứng: không nhắm mắt được, mất nếp nhăn trán, miệng lệch. Điều trị corticosteroid sớm quan trọng cho tiên lượng. Bảo vệ mắt bằng nước mắt nhân tạo và băng mắt.",
        "context": "신경과 외래, 응급실, 재활치료",
        "culturalNote": "한국에서는 안면신경마비를 '구안와사'로 부르며, 한의학에서 침 치료를 받는 경우가 많습니다. 베트남에서도 전통 침술을 선호하는 경향이 있습니다. 한국 환자들은 '중풍'으로 오해하여 뇌졸중과 혼동하고, 베트남 환자들도 '바람 맞아서' 생긴다고 믿는 경우가 있어 통역 시 말초 신경 질환임을 명확히 설명하고 스테로이드 치료의 효과를 강조해야 합니다. 눈을 감지 못해 각막 손상이 발생할 수 있으므로 눈 보호의 중요성을 반드시 전달해야 합니다. 대부분 회복되지만 시간이 걸린다는 점도 설명해야 합니다.",
        "commonMistakes": [
            {
                "mistake": "뇌졸중으로 오역",
                "correction": "말초신경 마비로 뇌졸중과 다름 (이마 주름 소실이 특징)",
                "explanation": "불필요한 공포 방지"
            },
            {
                "mistake": "눈 보호 교육 누락",
                "correction": "인공눈물, 안대 사용 필수",
                "explanation": "각막 손상 예방"
            },
            {
                "mistake": "침 치료만 권장",
                "correction": "스테로이드 치료가 1차, 침은 보조 가능",
                "explanation": "효과적 치료 우선"
            }
        ],
        "examples": [
            {
                "ko": "벨마비로 진단되어 7일간 스테로이드 치료하고 인공눈물과 안대로 눈을 보호합니다",
                "vi": "Chẩn đoán liệt Bell, điều trị corticosteroid 7 ngày và bảo vệ mắt bằng nước mắt nhân tạo và băng",
                "situation": "formal"
            },
            {
                "ko": "눈을 깜빡이지 못하니 자주 인공눈물을 넣고 자실 때는 안대를 하세요",
                "vi": "Không chớp mắt được nên nhỏ nước mắt nhân tạo thường xuyên và đeo băng khi ngủ",
                "situation": "onsite"
            },
            {
                "ko": "얼굴 한쪽이 안 움직이는데 중풍인가요?",
                "vi": "Một bên mặt không cử động, có phải đột quỵ không?",
                "situation": "informal"
            }
        ],
        "relatedTerms": ["벨마비", "구안와사", "스테로이드", "각막손상예방"]
    },
    {
        "slug": "dong-kinh-lien-tuc",
        "korean": "뇌전증지속상태",
        "vietnamese": "Động kinh liên tục",
        "hanja": "腦癲癇持續狀態",
        "hanjaReading": "腦(뇌 뇌) + 癲(미칠 전) + 癇(간질 간) + 持(가질 지) + 續(이을 속) + 狀(모양 상) + 態(모양 태)",
        "pronunciation": "동낑리엔뚝",
        "meaningKo": "발작이 5분 이상 지속되거나 발작 사이에 의식 회복 없이 반복되는 생명을 위협하는 응급 상황입니다. 통역 시 주의할 점은 즉시 응급실 방문이 필수이며, 정맥 항경련제로 발작을 중단시켜야 뇌손상을 막을 수 있다는 점을 환자 보호자에게 명확히 전달해야 합니다. 한국에서는 119를 부르고 환자를 옆으로 눕혀 기도를 확보하며, 입에 아무것도 넣지 말고, 시간을 측정하여 의료진에게 전달하는 것이 중요하다는 점을 보호자가 오해 없이 이해하도록 통역해야 합니다.",
        "meaningVi": "Tình trạng cấp cứu đe dọa tính mạng khi co giật kéo dài >5 phút hoặc lặp lại liên tục không hồi tỉnh. Cần cấp cứu ngay, thuốc chống co giật tĩnh mạch để ngừng co giật và ngăn tổn thương não.",
        "context": "응급실, 중환자실",
        "culturalNote": "한국에서는 뇌전증지속상태를 '간질 중첩증'으로도 부르며, 보호자들은 발작 시 혀를 깨물까봐 입에 물건을 넣으려는 경향이 있습니다. 베트남에서도 전통적으로 발작 시 입에 수건이나 나무 막대를 넣는 관습이 있을 수 있어 통역 시 이것이 매우 위험하며 절대 해서는 안 된다는 점을 강조해야 합니다. 한국 보호자들은 발작이 멈추면 병원에 안 가도 된다고 생각하는 경우가 있고, 베트남 보호자들도 마찬가지이므로 5분 이상 지속되면 무조건 응급실 방문이 필요함을 명확히 전달해야 합니다.",
        "commonMistakes": [
            {
                "mistake": "발작 시 입에 물건 넣으라고 안내",
                "correction": "절대 금지, 질식 및 치아 손상 위험",
                "explanation": "잘못된 응급 처치 방지"
            },
            {
                "mistake": "발작 멈추면 병원 안 가도 된다고 안내",
                "correction": "5분 이상 또는 반복 발작 시 반드시 응급실",
                "explanation": "뇌손상 방지"
            },
            {
                "mistake": "발작 시간 측정 중요성 누락",
                "correction": "시간 측정하여 의료진에게 전달",
                "explanation": "치료 결정에 중요한 정보"
            }
        ],
        "examples": [
            {
                "ko": "뇌전증지속상태로 응급실에서 로라제팜 정맥 주사 후 발작이 중단되었습니다",
                "vi": "Động kinh liên tục, sau tiêm tĩnh mạch lorazepam tại cấp cứu co giật ngừng",
                "situation": "formal"
            },
            {
                "ko": "발작이 5분 이상이거나 계속 반복되면 119를 부르고 환자를 옆으로 눕히세요",
                "vi": "Nếu co giật >5 phút hoặc lặp lại liên tục gọi cấp cứu và đặt bệnh nhân nằm nghiêng",
                "situation": "onsite"
            },
            {
                "ko": "발작이 멈추지 않는데 어떻게 해야 하나요?",
                "vi": "Co giật không ngừng phải làm sao?",
                "situation": "informal"
            }
        ],
        "relatedTerms": ["뇌전증", "간질중첩증", "항경련제", "응급처치"]
    },
    {
        "slug": "thuy-dau",
        "korean": "수두증",
        "vietnamese": "Thủy đầu",
        "hanja": "水頭症",
        "hanjaReading": "水(물 수) + 頭(머리 두) + 症(병 증)",
        "pronunciation": "투이더우",
        "meaningKo": "뇌척수액이 뇌실에 과다하게 축적되어 뇌압이 상승하는 질환입니다. 통역 시 주의할 점은 선천성과 후천성(외상, 종양, 감염)으로 나뉘며, '두통, 구역, 보행 장애, 인지 저하' 등의 증상을 정확히 전달해야 하고, 치료는 뇌실복강단락술(션트)로 뇌척수액을 배출시킨다는 점을 환자와 가족에게 명확히 전달해야 합니다. 한국에서는 소아 수두증은 머리둘레 증가로 발견되고, 성인은 정상압 수두증이 치매와 감별이 필요하며, 션트 수술 후 합병증(감염, 폐쇄) 가능성도 설명해야 합니다.",
        "meaningVi": "Bệnh lý dịch não tủy tích tụ quá mức trong não thất làm tăng áp lực nội sọ. Phân loại: bẩm sinh và mắc phải (chấn thương, u, nhiễm trùng). Triệu chứng: đau đầu, buồn nôn, rối loạn đi lại, suy giảm nhận thức. Điều trị: phẫu thuật shunt não thất-ổ bụng.",
        "context": "신경외과 외래, 소아신경과, 수술 상담",
        "culturalNote": "한국에서는 소아 수두증은 출생 전 초음파나 출생 후 머리둘레 측정으로 조기 발견되며, 션트 수술로 대부분 정상 생활이 가능합니다. 베트남에서는 출생 전 검진이 제한적이어서 증상이 심해진 후 발견되는 경우가 있습니다. 한국 부모들은 션트가 평생 유지되어야 한다는 점에 부담을 느끼고, 베트남 부모들은 수술에 대한 두려움이 크므로 통역 시 수술의 필요성과 안전성, 수술 후 정상 발달 가능성을 강조해야 합니다. 성인 정상압 수두증은 '걷기 이상, 요실금, 치매' 3대 증상이 특징이며 션트로 호전 가능함을 설명해야 합니다.",
        "commonMistakes": [
            {
                "mistake": "치매로만 진단하여 치료 기회 놓침",
                "correction": "성인은 정상압 수두증 감별 필수 (션트로 치료 가능)",
                "explanation": "치료 가능한 치매 원인"
            },
            {
                "mistake": "션트가 일시적이라고 오해",
                "correction": "대부분 평생 유지 필요, 정기 점검 중요",
                "explanation": "현실적 기대치 설정"
            },
            {
                "mistake": "션트 합병증 가능성 설명 누락",
                "correction": "감염, 폐쇄 가능성 있어 증상 시 즉시 내원",
                "explanation": "조기 발견 및 치료"
            }
        ],
        "examples": [
            {
                "ko": "수두증으로 뇌실복강단락술을 시행하여 뇌척수액을 복강으로 배출합니다",
                "vi": "Thủy đầu, phẫu thuật shunt não thất-ổ bụng để dẫn lưu dịch não tủy vào ổ bụng",
                "situation": "formal"
            },
            {
                "ko": "션트 부위가 붓거나 두통, 발열이 있으면 즉시 연락하세요",
                "vi": "Nếu vùng shunt sưng hoặc đau đầu, sốt hãy liên hệ ngay",
                "situation": "onsite"
            },
            {
                "ko": "아기 머리가 너무 큰데 수두증인가요? 수술하면 정상으로 자라나요?",
                "vi": "Đầu bé quá to, có phải thủy đầu không? Mổ có lớn bình thường không?",
                "situation": "informal"
            }
        ],
        "relatedTerms": ["뇌척수액", "뇌실복강단락술", "션트", "뇌압상승"]
    },
    {
        "slug": "phinh-dong-mach-nao",
        "korean": "뇌동맥류",
        "vietnamese": "Phình động mạch não",
        "hanja": "腦動脈瘤",
        "hanjaReading": "腦(뇌 뇌) + 動(움직일 동) + 脈(맥 맥) + 瘤(혹 류)",
        "pronunciation": "핀동맥나오",
        "meaningKo": "뇌혈관 벽이 약해져 풍선처럼 부풀어 오른 상태로, 파열 시 지주막하출혈을 일으킵니다. 통역 시 주의할 점은 대부분 무증상이며 검진에서 우연히 발견되거나 파열 시 '벼락 두통'으로 나타나며, 파열되지 않은 동맥류는 크기와 위치에 따라 수술 또는 경과 관찰을 결정한다는 점을 환자에게 명확히 전달해야 합니다. 한국에서는 코일색전술이나 클리핑 수술로 치료하며, 파열된 동맥류는 응급 수술이 필요하고 예후가 좋지 않을 수 있다는 점을 환자와 가족이 오해 없이 이해하도록 통역해야 합니다.",
        "meaningVi": "Tình trạng thành mạch máu não yếu phình to như bóng bay, khi vỡ gây xuất huyết dưới nhện. Phần lớn không triệu chứng, phát hiện ngẫu nhiên khi khám hoặc khi vỡ có đau đầu sét đánh. Phình chưa vỡ: phẫu thuật hoặc theo dõi tùy kích thước và vị trí.",
        "context": "신경외과 외래, 응급실(파열 시), 수술 상담",
        "culturalNote": "한국에서는 건강검진에서 뇌 MRA를 시행하여 우연히 동맥류를 발견하는 경우가 증가하고 있으며, 환자들은 '머릿속에 폭탄이 있다'는 공포를 느낍니다. 베트남에서는 검진 문화가 덜 발달하여 파열 후 발견되는 경우가 많을 수 있습니다. 한국 환자들은 작은 동맥류도 즉시 수술해야 한다고 생각하지만 크기가 작고 위치가 좋으면 경과 관찰할 수 있으며, 베트남 환자들은 수술에 대한 두려움으로 치료를 미루는 경향이 있어 통역 시 파열 위험과 수술의 안전성을 균형 있게 전달해야 합니다. 파열 시 즉시 응급실 방문의 중요성을 강조해야 합니다.",
        "commonMistakes": [
            {
                "mistake": "모든 동맥류를 즉시 수술해야 한다고 설명",
                "correction": "크기, 위치, 환자 상태에 따라 경과 관찰 가능",
                "explanation": "불필요한 불안 및 수술 방지"
            },
            {
                "mistake": "파열 증상 교육 누락",
                "correction": "벼락 두통 발생 시 즉시 119",
                "explanation": "응급 상황 대처"
            },
            {
                "mistake": "가족력 확인 중요성 누락",
                "correction": "가족 중 동맥류나 지주막하출혈 있으면 검진 권장",
                "explanation": "조기 발견"
            }
        ],
        "examples": [
            {
                "ko": "5mm 뇌동맥류가 발견되어 1년마다 MRA로 추적 관찰합니다",
                "vi": "Phát hiện phình động mạch não 5mm, theo dõi bằng MRA hàng năm",
                "situation": "formal"
            },
            {
                "ko": "갑자기 평생 처음 겪는 극심한 두통이 있으면 즉시 응급실로 가세요",
                "vi": "Nếu đột ngột đau đầu dữ dội chưa từng có, hãy đến cấp cứu ngay",
                "situation": "onsite"
            },
            {
                "ko": "뇌동맥류 있는데 터지면 어떻게 되나요? 수술 안 하면 안 되나요?",
                "vi": "Có phình động mạch não, vỡ thì sao? Không mổ được không?",
                "situation": "informal"
            }
        ],
        "relatedTerms": ["지주막하출혈", "코일색전술", "클리핑", "벼락두통"]
    },
    {
        "slug": "viem-mang-nao",
        "korean": "뇌수막염",
        "vietnamese": "Viêm màng não",
        "hanja": "腦髓膜炎",
        "hanjaReading": "腦(뇌 뇌) + 髓(골수 수) + 膜(막 막) + 炎(불꽃 염)",
        "pronunciation": "비엠망나오",
        "meaningKo": "뇌와 척수를 둘러싼 수막에 염증이 생기는 질환으로, 세균성과 바이러스성으로 나뉩니다. 통역 시 주의할 점은 '고열, 두통, 목 경직'이 3대 증상이며, 세균성은 생명을 위협하는 응급 상황으로 즉시 항생제 치료가 필요하고, 요추천자로 뇌척수액 검사를 시행한다는 점을 환자와 가족에게 명확히 전달해야 합니다. 한국에서는 소아는 예방접종(Hib, 폐렴구균, 수막구균)으로 예방 가능하며, 성인은 면역저하자에서 주로 발생하고, 뇌손상이나 사망 위험이 있어 조기 진단과 치료가 매우 중요하다는 점을 환자가 오해 없이 이해하도록 통역해야 합니다.",
        "meaningVi": "Viêm màng bao quanh não và tủy sống, phân loại vi khuẩn và virus. Tam chứng: sốt cao, đau đầu, cứng gáy. Viêm do vi khuẩn là cấp cứu đe dọa tính mạng, cần kháng sinh ngay. Chọc dò tủy sống xét nghiệm dịch não tủy.",
        "context": "응급실, 감염내과 입원, 소아과 입원",
        "culturalNote": "한국에서는 뇌수막염 예방접종이 필수 접종에 포함되어 발생률이 감소했지만, 성인에서는 여전히 발생합니다. 베트남에서는 예방접종 보급률이 낮을 수 있어 소아 뇌수막염이 상대적으로 흔할 수 있습니다. 한국 환자와 가족은 요추천자(척수 주사)를 매우 두려워하며 '척수를 뽑으면 장애가 온다'는 오해가 있고, 베트남에서도 비슷한 두려움이 있어 통역 시 요추천자가 진단에 필수적이고 안전한 검사임을 명확히 설명해야 합니다. 세균성 뇌수막염은 시간이 생명이므로 조기 항생제 투여의 중요성을 강조해야 합니다.",
        "commonMistakes": [
            {
                "mistake": "세균성과 바이러스성을 구분 않고 설명",
                "correction": "세균성은 응급, 바이러스성은 대부분 자연 회복",
                "explanation": "치료 긴급성 이해"
            },
            {
                "mistake": "요추천자를 위험하다고 과장",
                "correction": "진단에 필수적이고 안전한 검사",
                "explanation": "검사 거부로 진단 지연 방지"
            },
            {
                "mistake": "예방접종 정보 제공 누락",
                "correction": "Hib, 폐렴구균, 수막구균 백신으로 예방 가능",
                "explanation": "가족 및 밀접 접촉자 예방"
            }
        ],
        "examples": [
            {
                "ko": "세균성 뇌수막염 의심되어 요추천자 시행하고 즉시 항생제 치료를 시작합니다",
                "vi": "Nghi viêm màng não do vi khuẩn, chọc dò tủy sống và bắt đầu kháng sinh ngay",
                "situation": "formal"
            },
            {
                "ko": "고열과 함께 목이 뻣뻣하고 두통이 심하면 즉시 응급실로 가세요",
                "vi": "Nếu sốt cao kèm cứng gáy và đau đầu dữ dội hãy đến cấp cứu ngay",
                "situation": "onsite"
            },
            {
                "ko": "척수 주사 맞으면 나중에 걷지 못하게 되나요?",
                "vi": "Chọc dò tủy sống có bị liệt không đi được không?",
                "situation": "informal"
            }
        ],
        "relatedTerms": ["세균성뇌수막염", "요추천자", "뇌척수액검사", "예방접종"]
    }
]

def main():
    """메인 실행 함수"""
    try:
        # 기존 파일 읽기
        with open(file_path, 'r', encoding='utf-8') as f:
            data = json.load(f)

        print(f"기존 용어 수: {len(data)}")

        # 중복 확인 (slug 기준)
        existing_slugs = {term['slug'] for term in data}
        new_unique_terms = [term for term in new_terms if term['slug'] not in existing_slugs]

        print(f"신규 용어 수: {len(new_unique_terms)}")

        # 신규 용어 추가
        data.extend(new_unique_terms)

        # 파일 저장 (한글 유지, 들여쓰기 2칸)
        with open(file_path, 'w', encoding='utf-8') as f:
            json.dump(data, f, ensure_ascii=False, indent=2)

        print(f"✅ 완료! 총 용어 수: {len(data)}")
        print(f"✅ 추가된 용어: {len(new_unique_terms)}개")

        # 추가된 용어 목록 출력
        if new_unique_terms:
            print("\n추가된 용어:")
            for i, term in enumerate(new_unique_terms, 1):
                print(f"{i}. {term['korean']} ({term['vietnamese']})")

    except FileNotFoundError:
        print(f"❌ 오류: {file_path} 파일을 찾을 수 없습니다.")
    except json.JSONDecodeError:
        print(f"❌ 오류: JSON 파싱 실패. 파일 형식을 확인하세요.")
    except Exception as e:
        print(f"❌ 예상치 못한 오류: {e}")

if __name__ == "__main__":
    main()
