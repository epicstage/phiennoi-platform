#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Construction 용어 추가 스크립트 v7-hhh
테마: 수처리/정화시설
"""

import json
import os

# 추가할 용어 데이터 (10개)
data = [
    {
        "slug": "be-xu-ly-nuoc-thai",
        "korean": "오수정화조",
        "vietnamese": "Bể xử lý nước thải",
        "hanja": "汚水淨化槽",
        "hanjaReading": "더러울 오(汚) + 물 수(水) + 맑을 정(淨) + 되 화(化) + 물통 조(槽)",
        "pronunciation": "오수정화조",
        "meaningKo": "건축물에서 발생하는 오수를 생물학적·화학적 방법으로 정화하여 방류 기준에 맞게 처리하는 시설입니다. 통역 시 '정화조'와 '하수처리시설'을 구분해야 하며, 정화조는 개별 건물 단위, 하수처리장은 지역 단위임을 명확히 해야 합니다. 베트남에서는 '베 셉틱(bể septic)'이라는 용어도 혼용되지만, 현대식 오수정화조는 'bể xử lý nước thải sinh hoạt'로 구분하여 설명하는 것이 정확합니다. 처리 용량(인원수 기준), 방류수 수질 기준(BOD, SS 등)을 함께 언급하면 실수를 줄일 수 있습니다.",
        "meaningVi": "Thiết bị xử lý nước thải sinh hoạt từ các công trình bằng phương pháp sinh học và hóa học để đạt tiêu chuẩn xả thải. Khác với hệ thống xử lý nước thải tập trung (nhà máy xử lý nước thải), bể xử lý nước thải thường được lắp đặt cho từng công trình riêng lẻ.",
        "context": "건설 현장에서 환경 설비 시공 시, 건축 인허가 과정에서 오수처리 계획 검토 시, 정화조 용량 계산 및 유지관리 교육 시 사용됩니다.",
        "culturalNote": "한국은 개별 건물에 오수정화조 설치가 법적으로 의무화되어 있으며, 정기적인 청소와 점검이 엄격히 관리됩니다. 베트남은 도시 지역에서는 하수관로 연결이 일반적이지만, 농촌이나 공단 지역에서는 개별 정화 시설이 많아 한국의 정화조 기술 수출이 활발합니다. 통역 시 'bể phốt(구식 정화조)'와 현대식 'bể xử lý sinh học'을 구분하여 설명하면 오해를 방지할 수 있습니다. 또한 한국은 질소·인 제거 고도처리가 일반화되었지만, 베트남은 기본 BOD/SS 처리 위주라는 차이를 인지해야 합니다.",
        "commonMistakes": [
            {
                "mistake": "정화조를 'bể nước'로 번역",
                "correction": "bể xử lý nước thải 또는 bể septic",
                "explanation": "'bể nước'는 단순 물탱크를 의미하여, 오수 처리 기능이 없는 저수조로 오해될 수 있습니다."
            },
            {
                "mistake": "하수처리장과 정화조를 같은 용어로 번역",
                "correction": "정화조는 'bể xử lý nước thải', 하수처리장은 'nhà máy xử lý nước thải'로 구분",
                "explanation": "규모와 처리 방식이 다르므로 명확히 구분해야 합니다."
            },
            {
                "mistake": "'합병정화조'를 단순히 'bể xử lý chung'으로 번역",
                "correction": "bể xử lý nước thải hợp nhất (hệ thống xử lý kết hợp nước đen và nước xám)",
                "explanation": "오수와 잡배수를 함께 처리하는 시스템임을 명확히 해야 합니다."
            }
        ],
        "examples": [
            {
                "ko": "이 건물은 50인용 오수정화조를 설치해야 합니다.",
                "vi": "Công trình này cần lắp đặt bể xử lý nước thải cho 50 người.",
                "situation": "formal"
            },
            {
                "ko": "정화조 방류수 수질검사 결과 BOD 기준을 초과했습니다.",
                "vi": "Kết quả kiểm tra chất lượng nước xả từ bể xử lý cho thấy vượt tiêu chuẩn BOD.",
                "situation": "formal"
            },
            {
                "ko": "정화조 청소는 최소 연 1회 이상 해야 합니다.",
                "vi": "Phải vệ sinh bể xử lý nước thải ít nhất 1 lần mỗi năm.",
                "situation": "onsite"
            }
        ],
        "relatedTerms": ["하수처리장", "침전조", "포기조", "방류수", "BOD"]
    },
    {
        "slug": "be-tach-mo",
        "korean": "그리스트랩",
        "vietnamese": "Bể tách mỡ",
        "hanja": None,
        "hanjaReading": None,
        "pronunciation": "그리스트랩",
        "meaningKo": "주방이나 식당에서 배출되는 폐수 중 유지(기름) 성분을 물리적으로 분리·제거하는 장치입니다. 통역 시 'grease trap'의 외래어인 '그리스트랩'과 순화어인 '유지분리기'를 모두 알아야 하며, 현장에서는 '그리스트랩'이 더 일반적으로 사용됩니다. 베트남어로는 'bể tách mỡ' 또는 'hố ga tách mỡ'로 표현하며, 주방 규모에 따라 설치 용량을 계산하는 방법을 설명할 수 있어야 합니다. 특히 대형 식당이나 급식소에서는 자동 유지분리기(automatic grease trap)를 설치하는 경우가 많아 이를 구분할 필요가 있습니다.",
        "meaningVi": "Thiết bị tách và loại bỏ dầu mỡ từ nước thải bếp ăn, nhà hàng bằng phương pháp vật lý trước khi xả vào hệ thống thoát nước. Giúp ngăn ngừa tắc nghẽn đường ống và bảo vệ hệ thống xử lý nước thải.",
        "context": "음식점, 급식소, 호텔 주방 등 유지류 배출이 많은 시설의 설계 및 시공 시, 배관 설비 점검 및 유지보수 시 사용됩니다.",
        "culturalNote": "한국은 식품위생법에 따라 일정 규모 이상의 식당은 그리스트랩 설치가 의무화되어 있으며, 정기적인 청소와 점검이 법적으로 요구됩니다. 베트남도 대도시 중심으로 규제가 강화되고 있지만, 소규모 식당에서는 설치율이 낮은 편입니다. 통역 시 한국의 엄격한 위생 기준과 관리 체계를 설명하면서, 베트남 현지의 설치 비용과 유지보수 현실을 함께 고려해야 합니다. 또한 한국은 자동 유지분리 시스템이 보편화되었지만, 베트남은 수동식 청소가 일반적이라는 차이가 있습니다.",
        "commonMistakes": [
            {
                "mistake": "'그리스트랩'을 'bể dầu'로만 번역",
                "correction": "bể tách mỡ (또는 hố ga tách mỡ, thiết bị tách dầu mỡ)",
                "explanation": "'bể dầu'는 유류 저장 탱크로 오해될 수 있습니다."
            },
            {
                "mistake": "'유지분리기'와 '그리스트랩'을 다른 장비로 설명",
                "correction": "같은 장비의 순화어와 외래어 표현임을 명확히",
                "explanation": "현장에서는 '그리스트랩'이 더 일반적이지만, 공식 문서에서는 '유지분리기'를 사용하는 경우가 많습니다."
            },
            {
                "mistake": "청소 주기를 'vệ sinh hàng tháng'으로만 표현",
                "correction": "vệ sinh định kỳ (theo quy định 1-3 tháng/lần tùy mức độ sử dụng)",
                "explanation": "청소 주기는 사용량에 따라 달라지므로 유연하게 설명해야 합니다."
            }
        ],
        "examples": [
            {
                "ko": "주방 배수관 앞에 그리스트랩을 설치해 주세요.",
                "vi": "Hãy lắp đặt bể tách mỡ trước đường ống thoát nước bếp.",
                "situation": "onsite"
            },
            {
                "ko": "그리스트랩에 기름이 가득 차서 청소가 필요합니다.",
                "vi": "Bể tách mỡ đã đầy dầu mỡ, cần vệ sinh ngay.",
                "situation": "onsite"
            },
            {
                "ko": "이 식당은 200리터 용량의 자동 그리스트랩이 설치되어 있습니다.",
                "vi": "Nhà hàng này được lắp đặt bể tách mỡ tự động dung tích 200 lít.",
                "situation": "formal"
            }
        ],
        "relatedTerms": ["오수정화조", "배수관", "유지", "주방배수", "자동청소"]
    },
    {
        "slug": "be-chua-nuoc-mua",
        "korean": "우수저류조",
        "vietnamese": "Bể chứa nước mưa",
        "hanja": "雨水貯留槽",
        "hanjaReading": "비 우(雨) + 물 수(水) + 모을 저(貯) + 머무를 류(留) + 물통 조(槽)",
        "pronunciation": "우수저류조",
        "meaningKo": "빗물을 일시적으로 저장하여 홍수 예방, 물 재이용, 지하수 함양 등의 목적으로 활용하는 시설입니다. 통역 시 '우수저류조'와 '우수저장조'는 같은 의미이지만, '빗물받이(집수정)'와는 다른 개념임을 주의해야 합니다. 베트남어로는 'bể chứa nước mưa' 또는 'bể tích trữ nước mưa'로 표현하며, 최근 친환경 건축과 물 부족 문제로 관심이 높아지고 있습니다. 저류 용량 계산 시 강우량, 집수면적, 방류 시간 등을 고려해야 하며, 이를 베트남어로 설명할 수 있어야 합니다.",
        "meaningVi": "Công trình chứa tạm thời nước mưa nhằm phòng chống lũ lụt, tái sử dụng nước và bổ cập nước ngầm. Là một phần của hệ thống thoát nước bền vững và kiến trúc xanh.",
        "context": "친환경 건축 설계 시, 도시 홍수 방지 대책 논의 시, 빗물 재이용 시스템 설명 시 사용됩니다.",
        "culturalNote": "한국은 2000년대 이후 도시 홍수 문제로 우수저류조 설치가 의무화되었으며, LID(Low Impact Development) 기법의 일환으로 확산되고 있습니다. 베트남은 최근 하노이, 호찌민 등 대도시에서 침수 문제가 심각해지면서 우수저류 시설에 대한 관심이 높아지고 있으나, 아직 법적 의무화는 제한적입니다. 통역 시 한국의 저류조 설계 기준(강우 재현빈도 30년 등)과 베트남의 현지 강우 패턴(열대 몬순 기후) 차이를 고려하여 설명해야 합니다. 또한 한국은 저류된 물을 조경용수, 화장실 용수로 재이용하는 시스템이 보편화되었으나, 베트남은 아직 초기 단계라는 점을 인지해야 합니다.",
        "commonMistakes": [
            {
                "mistake": "'우수저류조'를 'bể nước mưa'로만 번역",
                "correction": "bể chứa nước mưa (또는 bể tích trữ nước mưa, bể điều hòa nước mưa)",
                "explanation": "저류(貯留)의 의미인 '일시 저장'의 개념을 명확히 해야 합니다."
            },
            {
                "mistake": "'빗물받이'와 '우수저류조'를 같은 것으로 설명",
                "correction": "빗물받이는 'hố ga thu nước mưa'로, 집수 기능만 있는 소형 시설입니다.",
                "explanation": "규모와 기능이 다르므로 구분이 필요합니다."
            },
            {
                "mistake": "저류 용량을 'm3' 없이 숫자만 말함",
                "correction": "항상 단위(m³, mét khối)를 명시",
                "explanation": "베트남에서도 m³를 사용하지만, 'mét khối' 또는 'khối'로 발음하므로 단위를 명확히 해야 합니다."
            }
        ],
        "examples": [
            {
                "ko": "이 건물 지하에 500톤 용량의 우수저류조를 설치합니다.",
                "vi": "Tầng hầm tòa nhà này sẽ lắp đặt bể chứa nước mưa dung tích 500 tấn (500m³).",
                "situation": "formal"
            },
            {
                "ko": "우수저류조의 물은 조경용수로 재활용됩니다.",
                "vi": "Nước từ bể chứa nước mưa được tái sử dụng cho tưới cây cảnh quan.",
                "situation": "formal"
            },
            {
                "ko": "저류조가 꽉 차면 자동으로 하수관으로 방류됩니다.",
                "vi": "Khi bể chứa đầy, nước sẽ tự động xả vào hệ thống thoát nước.",
                "situation": "onsite"
            }
        ],
        "relatedTerms": ["빗물받이", "우수관", "방류", "집수면적", "LID"]
    },
    {
        "slug": "be-lang-cat",
        "korean": "침사지",
        "vietnamese": "Bể lắng cát",
        "hanja": "沈砂池",
        "hanjaReading": "잠길 침(沈) + 모래 사(砂) + 못 지(池)",
        "pronunciation": "침사지",
        "meaningKo": "수처리 시설에서 물속의 토사, 모래, 자갈 등 무거운 부유물질을 침전시켜 제거하는 최초 단계의 처리조입니다. 통역 시 '침사지'와 '침전지'를 구분해야 하며, 침사지는 주로 모래·자갈 등 무기물을 제거하고, 침전지는 유기물을 포함한 부유물을 침전시키는 차이가 있습니다. 베트남어로는 'bể lắng cát' 또는 'bể lắng cặn thô'로 표현하며, 하수처리장이나 정수장의 전처리 공정에서 필수적인 시설임을 설명할 수 있어야 합니다. 유속, 체류시간, 침강 속도 등 수리학적 개념도 함께 이해해야 정확한 통역이 가능합니다.",
        "meaningVi": "Bể xử lý sơ bộ trong hệ thống xử lý nước, dùng để lắng đọng và loại bỏ các tạp chất nặng như cát, sỏi, đất đá. Là công đoạn đầu tiên bảo vệ các thiết bị xử lý tiếp theo khỏi hư hỏng.",
        "context": "하수처리장, 정수장 설계 및 시공 시, 수처리 공정 설명 시, 유지보수 및 준설 작업 시 사용됩니다.",
        "culturalNote": "한국의 하수처리장은 침사지-침전지-생물학적처리-고도처리로 이어지는 다단계 처리 시스템이 표준화되어 있으며, 침사지의 모래 제거는 자동화된 기계식 준설 장비로 이루어집니다. 베트남도 대형 처리장은 유사한 시스템을 갖추고 있으나, 중소 규모에서는 수동 준설이 일반적입니다. 통역 시 '기계식 침사지(bể lắng cát cơ khí)'와 '중력식 침사지(bể lắng cát trọng lực)'를 구분하여 설명하면 이해도가 높아집니다. 또한 한국은 침사물을 건설 자재로 재활용하는 경우가 많지만, 베트남은 폐기물로 처리하는 것이 일반적이라는 차이가 있습니다.",
        "commonMistakes": [
            {
                "mistake": "'침사지'를 'bể lắng'으로만 번역",
                "correction": "bể lắng cát (침사지) vs bể lắng đợng (침전지) 구분 필수",
                "explanation": "'bể lắng'은 일반적인 침전지를 의미하여, 침사지의 전처리 기능이 누락됩니다."
            },
            {
                "mistake": "'준설'을 'đào'로 번역",
                "correction": "nạo vét (준설), không phải đào (굴착)",
                "explanation": "'đào'는 땅을 파는 것이고, 'nạo vét'은 물속 퇴적물을 제거하는 것입니다."
            },
            {
                "mistake": "침사지와 스크린(screen)을 같은 시설로 설명",
                "correction": "스크린은 'lưới chắn rác', 침사지는 'bể lắng cát'으로 별도 공정",
                "explanation": "스크린은 큰 부유물을 걸러내고, 침사지는 무거운 입자를 가라앉혀 제거합니다."
            }
        ],
        "examples": [
            {
                "ko": "침사지에 모래가 많이 쌓여서 준설이 필요합니다.",
                "vi": "Bể lắng cát đã tích đọng nhiều cát, cần nạo vét ngay.",
                "situation": "onsite"
            },
            {
                "ko": "이 하수처리장의 침사지는 시간당 1,000톤을 처리합니다.",
                "vi": "Bể lắng cát của nhà máy xử lý nước thải này xử lý 1.000 tấn mỗi giờ.",
                "situation": "formal"
            },
            {
                "ko": "침사지를 거친 물은 다음 침전지로 보내집니다.",
                "vi": "Nước qua bể lắng cát sẽ được chuyển đến bể lắng đợng tiếp theo.",
                "situation": "formal"
            }
        ],
        "relatedTerms": ["침전지", "스크린", "준설", "전처리", "하수처리"]
    },
    {
        "slug": "thiet-bi-khu-trung",
        "korean": "소독설비",
        "vietnamese": "Thiết bị khử trùng",
        "hanja": "消毒設備",
        "hanjaReading": "사라질 소(消) + 독 독(毒) + 베풀 설(設) + 갖출 비(備)",
        "pronunciation": "소독설비",
        "meaningKo": "정수장이나 수처리 시설에서 병원균을 제거하기 위해 염소, 자외선, 오존 등을 이용하여 소독하는 장비입니다. 통역 시 '소독'과 '살균', '멸균'을 구분해야 하며, 소독(disinfection)은 병원성 미생물을 사멸시키는 것, 살균(sterilization)은 모든 미생물을 제거하는 것으로 차이가 있습니다. 베트남어로는 'thiết bị khử trùng' 또는 'hệ thống sát trùng nước'로 표현하며, 염소 소독(khử trùng bằng clo), 자외선 소독(khử trùng bằng tia UV), 오존 소독(khử trùng bằng ozone) 등 방법별 용어를 알아야 합니다. 특히 잔류염소 농도, 접촉 시간 등 수질 기준을 설명할 수 있어야 정확한 통역이 가능합니다.",
        "meaningVi": "Thiết bị sử dụng clo, tia UV, ozone hoặc các phương pháp khác để tiêu diệt vi khuẩn gây bệnh trong nước tại nhà máy nước sạch hoặc hệ thống xử lý nước. Đảm bảo nước đạt tiêu chuẩn an toàn vi sinh trước khi cấp cho người dùng.",
        "context": "정수장, 하수처리장, 중수도 시설 등에서 수질 안전 확보를 위한 최종 공정 설명 시, 소독 방법 선정 및 설계 시 사용됩니다.",
        "culturalNote": "한국은 1990년대까지 염소 소독이 주류였으나, 2000년대 이후 자외선(UV) 소독과 오존 소독이 확대되고 있으며, 최근에는 고도산화(AOP) 기술도 도입되고 있습니다. 베트남은 여전히 염소 소독이 가장 일반적이며, 염소 냄새(mùi clo)에 대한 거부감이 있어 염소 주입량 조절이 중요합니다. 통역 시 한국의 다양한 소독 기술을 소개하면서, 베트남 현지의 비용과 유지관리 능력을 고려한 적정 기술을 제안하는 것이 효과적입니다. 또한 '잔류염소(clo dư)'는 한국에서는 수질 기준 항목이지만, 베트남에서는 모니터링이 느슨한 경우가 많아 이를 강조할 필요가 있습니다.",
        "commonMistakes": [
            {
                "mistake": "'소독설비'를 'thiết bị vệ sinh'으로 번역",
                "correction": "thiết bị khử trùng (또는 hệ thống sát trùng nước)",
                "explanation": "'thiết bị vệ sinh'은 청소 장비를 의미하여, 병원균 제거 기능이 누락됩니다."
            },
            {
                "mistake": "염소 소독을 'sát trùng clo'로만 표현",
                "correction": "khử trùng bằng clo (또는 xử lý clo, clo hóa)",
                "explanation": "'sát trùng'은 의료용 멸균을 연상시키므로, 'khử trùng'이 수처리에 더 적합합니다."
            },
            {
                "mistake": "자외선 소독을 'ánh sáng UV'로만 설명",
                "correction": "khử trùng bằng tia UV (또는 hệ thống đèn UV sát trùng)",
                "explanation": "'ánh sáng UV'는 단순히 자외선 빛을 의미하여, 소독 기능이 명확하지 않습니다."
            }
        ],
        "examples": [
            {
                "ko": "이 정수장은 자외선 소독설비를 사용합니다.",
                "vi": "Nhà máy nước này sử dụng thiết bị khử trùng bằng tia UV.",
                "situation": "formal"
            },
            {
                "ko": "염소 주입량을 조절해서 잔류염소 농도를 맞춰야 합니다.",
                "vi": "Cần điều chỉnh lượng clo bơm vào để đạt nồng độ clo dư phù hợp.",
                "situation": "onsite"
            },
            {
                "ko": "오존 소독은 염소 소독보다 비용이 높지만 냄새가 없습니다.",
                "vi": "Khử trùng bằng ozone tốn kém hơn clo nhưng không có mùi.",
                "situation": "formal"
            }
        ],
        "relatedTerms": ["염소", "자외선", "오존", "잔류염소", "수질기준"]
    },
    {
        "slug": "be-san-khi",
        "korean": "포기조",
        "vietnamese": "Bể sục khí",
        "hanja": "曝氣槽",
        "hanjaReading": "햇볕 쬘 폭(曝) + 기운 기(氣) + 물통 조(槽)",
        "pronunciation": "포기조",
        "meaningKo": "하수처리 과정에서 공기를 강제로 주입하여 호기성 미생물이 유기물을 분해하도록 하는 생물학적 처리조입니다. 통역 시 '폭기조'라는 용어도 사용되지만 '포기조'가 표준어이며, 베트남어로는 'bể sục khí' 또는 'bể hiếu khí'로 표현합니다. 활성슬러지법(activated sludge process)의 핵심 시설로, DO(용존산소) 농도, MLSS(혼합액부유물질) 농도, SRT(슬러지체류시간) 등 운영 지표를 정확히 설명할 수 있어야 합니다. 포기 방식에는 표면 포기(surface aeration), 산기식 포기(diffused aeration) 등이 있으며, 이를 구분하여 통역해야 합니다.",
        "meaningVi": "Bể xử lý sinh học trong hệ thống xử lý nước thải, sử dụng vi sinh vật hiếu khí để phân hủy chất hữu cơ. Không khí được bơm vào bể để cung cấp oxy cho vi sinh vật hoạt động. Là công đoạn chính trong phương pháp bùn hoạt tính.",
        "context": "하수처리장 설계 및 운영 시, 생물학적 처리 공정 설명 시, 수질 관리 및 미생물 활성 모니터링 시 사용됩니다.",
        "culturalNote": "한국의 하수처리장은 대부분 활성슬러지법을 기반으로 하며, 포기조는 가장 중요한 처리 단계입니다. 최근에는 에너지 절감을 위한 간헐 포기(intermittent aeration), 막분리(MBR) 결합형 등 고도화된 기술이 적용되고 있습니다. 베트남도 도시 하수처리장에서는 활성슬러지법이 일반적이지만, 산기 장치(diffuser)의 막힘, 블로워(blower) 고장 등 유지관리 문제가 자주 발생합니다. 통역 시 DO 농도를 2-3 mg/L로 유지해야 한다는 등 구체적인 운영 기준을 함께 설명하면 이해도가 높아지며, 'bể sục khí'와 'máy thổi khí(블로워)'를 구분하여 사용해야 혼란이 없습니다.",
        "commonMistakes": [
            {
                "mistake": "'포기조'를 'bể khí'로만 번역",
                "correction": "bể sục khí (또는 bể hiếu khí, bể oxy hóa sinh học)",
                "explanation": "'bể khí'는 공기 탱크로 오해될 수 있어, 생물학적 처리 기능을 명시해야 합니다."
            },
            {
                "mistake": "'포기'를 'bơm khí'로만 표현",
                "correction": "sục khí (포기), không chỉ là bơm khí (공기 주입)",
                "explanation": "'bơm khí'는 단순 공기 주입이고, 'sục khí'는 미세 기포로 포기하는 것입니다."
            },
            {
                "mistake": "DO를 'oxy'로만 말하고 단위 생략",
                "correction": "DO (oxy hòa tan) với đơn vị mg/L",
                "explanation": "DO(용존산소)는 수질 관리의 핵심 지표이므로 단위를 명확히 해야 합니다."
            }
        ],
        "examples": [
            {
                "ko": "포기조의 DO 농도가 1.5 mg/L로 낮아서 블로워 출력을 높였습니다.",
                "vi": "Nồng độ DO trong bể sục khí giảm xuống 1,5 mg/L nên đã tăng công suất máy thổi khí.",
                "situation": "onsite"
            },
            {
                "ko": "이 포기조는 24시간 연속 운전되며, MLSS는 3,000 mg/L로 유지됩니다.",
                "vi": "Bể sục khí này vận hành liên tục 24 giờ, duy trì MLSS ở mức 3.000 mg/L.",
                "situation": "formal"
            },
            {
                "ko": "산기식 포기 방식이 표면 포기보다 산소 효율이 높습니다.",
                "vi": "Phương pháp sục khí khuếch tán (산기식) hiệu quả oxy hóa cao hơn sục khí bề mặt.",
                "situation": "formal"
            }
        ],
        "relatedTerms": ["활성슬러지", "블로워", "DO", "MLSS", "생물학적처리"]
    },
    {
        "slug": "be-lang-dong",
        "korean": "침전조",
        "vietnamese": "Bể lắng đợng",
        "hanja": "沈澱槽",
        "hanjaReading": "잠길 침(沈) + 앙금 전(澱) + 물통 조(槽)",
        "pronunciation": "침전조",
        "meaningKo": "수처리 과정에서 물속의 부유물질(SS)을 중력에 의해 가라앉혀 제거하는 시설입니다. 통역 시 '최초침전지'(primary settling tank)와 '최종침전지'(final settling tank)를 구분해야 하며, 최초침전지는 생물학적 처리 전에 큰 고형물을 제거하고, 최종침전지는 활성슬러지를 침전시켜 분리하는 역할을 합니다. 베트남어로는 'bể lắng đợng' 또는 'bể lắng cặn'으로 표현하며, 침전지의 형태(원형/사각형), 슬러지 수집 방식(스크레이퍼/흡인) 등을 구분하여 설명할 수 있어야 합니다. 표면부하율(m³/m²·day), 월류율(m³/m·day) 등 설계 지표도 통역에 필요합니다.",
        "meaningVi": "Công trình xử lý nước sử dụng trọng lực để lắng đọng và loại bỏ các chất rắn lơ lửng (SS) trong nước. Có bể lắng đợng sơ cấp (trước xử lý sinh học) và bể lắng đợng thứ cấp (sau xử lý sinh học để tách bùn).",
        "context": "하수처리장, 정수장 설계 시, 침전 효율 개선 논의 시, 슬러지 관리 및 반송 작업 시 사용됩니다.",
        "culturalNote": "한국의 하수처리장은 최초침전지와 최종침전지가 명확히 구분되어 있으며, 원형 침전지에서는 중앙 구동식 스크레이퍼(scraper)로 슬러지를 수집합니다. 베트남도 유사한 구조이지만, 소규모 시설에서는 사각형 침전지가 많고, 슬러지 인발(引拔) 작업이 수동인 경우가 많습니다. 통역 시 'bể lắng đợng'과 'bể lắng cát'을 혼동하지 않도록 주의해야 하며, 최종침전지에서 반송슬러지(return sludge)를 포기조로 되돌리는 과정을 'bùn tuần hoàn' 또는 'bùn hoạt tính tuần hoàn'으로 설명하면 이해가 쉽습니다. 또한 한국은 침전지 상등수(supernatant)의 SS 기준이 엄격하지만, 베트남은 기준이 느슨한 경우가 많아 이를 강조할 필요가 있습니다.",
        "commonMistakes": [
            {
                "mistake": "'침전조'를 'bể lắng'으로만 번역",
                "correction": "bể lắng đợng (침전조) vs bể lắng cát (침사지) 구분",
                "explanation": "'bể lắng'은 일반 용어이므로, 침전지와 침사지를 구분하기 위해 정확한 용어를 사용해야 합니다."
            },
            {
                "mistake": "'최초침전지'와 '최종침전지'를 같은 용어로 번역",
                "correction": "bể lắng đợng sơ cấp (최초) vs bể lắng đợng thứ cấp (최종)",
                "explanation": "처리 공정상 위치와 기능이 다르므로 반드시 구분해야 합니다."
            },
            {
                "mistake": "'슬러지'를 'bùn'으로만 표현하고 종류 구분 안 함",
                "correction": "bùn sơ cấp (1차 슬러지), bùn hoạt tính (활성슬러지), bùn tuần hoàn (반송슬러지)",
                "explanation": "슬러지 종류에 따라 처리 방법이 다르므로 명확히 구분해야 합니다."
            }
        ],
        "examples": [
            {
                "ko": "최종침전지에서 슬러지가 잘 가라앉지 않아서 반송 비율을 조정했습니다.",
                "vi": "Bùn không lắng tốt ở bể lắng đợng thứ cấp nên đã điều chỉnh tỷ lệ bùn tuần hoàn.",
                "situation": "onsite"
            },
            {
                "ko": "이 침전지는 원형 구조로 지름 30미터입니다.",
                "vi": "Bể lắng đợng này có cấu trúc tròn, đường kính 30 mét.",
                "situation": "formal"
            },
            {
                "ko": "침전지 월류수의 SS 농도는 20 mg/L 이하로 유지됩니다.",
                "vi": "Nồng độ SS trong nước tràn của bể lắng đợng được duy trì dưới 20 mg/L.",
                "situation": "formal"
            }
        ],
        "relatedTerms": ["침사지", "슬러지", "스크레이퍼", "반송슬러지", "표면부하율"]
    },
    {
        "slug": "rua-nguoc",
        "korean": "역세척",
        "vietnamese": "Rửa ngược",
        "hanja": "逆洗滌",
        "hanjaReading": "거스를 역(逆) + 씻을 세(洗) + 빨 척(滌)",
        "pronunciation": "역세척",
        "meaningKo": "정수장이나 수처리 시설의 여과지(filter)에 쌓인 오염물질을 역방향으로 물을 흘려보내 제거하는 세척 방법입니다. 통역 시 '역세'라는 줄임말도 많이 사용되며, 베트남어로는 'rửa ngược' 또는 'rửa trôi ngược'로 표현합니다. 모래 여과, 활성탄 여과, 막 여과(membrane) 등 다양한 여과 방식에서 사용되며, 역세척 주기, 역세척 강도(backwash intensity), 역세척수량 등을 계산하고 설명할 수 있어야 합니다. 특히 막 여과(MF, UF)에서는 'chemical cleaning(약품세척)'과 구분하여 'physical backwash(물리적 역세척)'로 설명해야 합니다.",
        "meaningVi": "Phương pháp làm sạch bể lọc bằng cách cho nước chảy ngược chiều để loại bỏ cặn bẩn tích tụ trong vật liệu lọc (cát, than hoạt tính, màng lọc). Giúp khôi phục hiệu suất lọc và kéo dài tuổi thọ hệ thống.",
        "context": "정수장, 수영장, 공업용수 처리 시설 등에서 여과 설비 유지관리 시, 역세척 자동화 시스템 설명 시 사용됩니다.",
        "culturalNote": "한국의 정수장은 모래 여과지 역세척이 자동화되어 있으며, 압력 손실(pressure drop)을 감지하여 자동으로 역세척이 시작됩니다. 베트남도 대형 정수장은 유사하지만, 소규모 시설에서는 수동 역세척이나 역세척 주기가 불규칙한 경우가 많습니다. 통역 시 '역세척수(nước rửa ngược)'는 처리수의 일부를 사용하므로, 역세척 빈도가 높으면 생산 효율이 떨어진다는 점을 설명하면 경제성 이해에 도움이 됩니다. 또한 막 여과(màng lọc)의 경우, 물리적 역세척(rửa ngược vật lý)만으로 부족하면 화학 약품 세척(CIP: rửa hóa chất tại chỗ)이 필요하다는 점도 강조해야 합니다.",
        "commonMistakes": [
            {
                "mistake": "'역세척'을 'rửa ngược lại'로 번역",
                "correction": "rửa ngược (또는 xả ngược)",
                "explanation": "'rửa ngược lại'는 어색한 표현이며, 'rửa ngược'이 표준 용어입니다."
            },
            {
                "mistake": "'역세'를 'backwash'로 영어 그대로 사용",
                "correction": "베트남어 'rửa ngược'을 사용하되, 필요시 (backwash) 병기",
                "explanation": "현장에서 영어를 사용하는 경우도 있지만, 정확한 베트남어 표현을 우선해야 합니다."
            },
            {
                "mistake": "역세척과 배수(drain)를 혼동",
                "correction": "rửa ngược (역세척) vs xả nước, tháo nước (배수)",
                "explanation": "역세척은 역방향 흐름으로 세척하는 것이고, 배수는 단순히 물을 빼는 것입니다."
            }
        ],
        "examples": [
            {
                "ko": "여과지 압력이 2 bar를 넘어서 역세척을 시작합니다.",
                "vi": "Áp lực bể lọc vượt 2 bar, bắt đầu rửa ngược.",
                "situation": "onsite"
            },
            {
                "ko": "역세척 주기는 24시간마다 1회이며, 1회당 10분 소요됩니다.",
                "vi": "Chu kỳ rửa ngược là mỗi 24 giờ một lần, mỗi lần mất 10 phút.",
                "situation": "formal"
            },
            {
                "ko": "막 여과 시스템은 물리적 역세척 외에도 화학 세척이 필요합니다.",
                "vi": "Hệ thống màng lọc cần rửa ngược vật lý và cả rửa hóa chất (CIP).",
                "situation": "formal"
            }
        ],
        "relatedTerms": ["여과지", "압력손실", "모래여과", "활성탄", "막여과"]
    },
    {
        "slug": "loc-than-hoat-tinh",
        "korean": "활성탄여과",
        "vietnamese": "Lọc than hoạt tính",
        "hanja": "活性炭濾過",
        "hanjaReading": "살 활(活) + 성품 성(性) + 숯 탄(炭) + 거를 려(濾) + 지날 과(過)",
        "pronunciation": "활성탄여과",
        "meaningKo": "다공성 활성탄(activated carbon)을 이용하여 물속의 유기물, 냄새, 맛, 색도, 미량 오염물질 등을 흡착·제거하는 고도 정수 처리 방법입니다. 통역 시 '입상활성탄(GAC: Granular Activated Carbon)'과 '분말활성탄(PAC: Powdered Activated Carbon)'을 구분해야 하며, 입상활성탄은 여과지 형태로 사용되고, 분말활성탄은 혼합·침전 방식으로 사용됩니다. 베트남어로는 'lọc than hoạt tính' 또는 'xử lý bằng than hoạt tính'으로 표현하며, 활성탄의 재생(regeneration) 또는 교체 주기, 흡착 용량(adsorption capacity) 등 운영 지표를 설명할 수 있어야 합니다.",
        "meaningVi": "Phương pháp xử lý nước tiên tiến sử dụng than hoạt tính (activated carbon) có cấu trúc lỗ xốp để hấp phụ và loại bỏ chất hữu cơ, mùi, vị, màu và các chất ô nhiễm vi lượng trong nước. Có 2 dạng: than hoạt tính dạng hạt (GAC) và than hoạt tính dạng bột (PAC).",
        "context": "정수장 고도처리 공정, 산업 폐수 처리, 수돗물 냄새 제거, 미량 유해물질 제거 등에 사용되며, 수질 개선 프로젝트에서 자주 언급됩니다.",
        "culturalNote": "한국은 1990년대 이후 수돗물 고도정수처리의 일환으로 활성탄 여과가 보편화되었으며, 대부분의 대형 정수장에 설치되어 있습니다. 특히 냄새 물질(geosmin, 2-MIB) 제거에 효과적이어서 여름철 조류(algae) 문제 해결에 중요합니다. 베트남은 최근 도시 정수장에서 활성탄 도입이 증가하고 있으나, 활성탄 재생 시설이 부족하여 일회용으로 사용 후 폐기하는 경우가 많아 비용 부담이 큽니다. 통역 시 한국의 활성탄 재생 기술(재생로: lò tái sinh than)을 소개하면서, 베트남에서의 경제성을 함께 논의하는 것이 효과적입니다. 또한 '야자각 활성탄(than hoạt tính từ vỏ dừa)'과 '석탄계 활성탄(than hoạt tính từ than đá)'의 특성 차이도 설명할 수 있어야 합니다.",
        "commonMistakes": [
            {
                "mistake": "'활성탄'을 'than đen' 또는 'than củi'로 번역",
                "correction": "than hoạt tính (activated carbon)",
                "explanation": "'than đen'은 일반 숯, 'than củi'는 장작 숯으로, 활성탄의 특수한 다공성 구조를 표현하지 못합니다."
            },
            {
                "mistake": "'입상활성탄'과 '분말활성탄'을 구분 없이 'than hoạt tính'으로만 번역",
                "correction": "GAC (than hoạt tính dạng hạt) vs PAC (than hoạt tính dạng bột)",
                "explanation": "사용 방식과 효과가 다르므로 반드시 구분해야 합니다."
            },
            {
                "mistake": "'활성탄 재생'을 'tái sử dụng than'으로 표현",
                "correction": "tái sinh than hoạt tính (재생) hoặc tái tạo than hoạt tính",
                "explanation": "'tái sử dụng'는 단순 재사용이고, 'tái sinh'은 고온 처리로 흡착 능력을 회복시키는 것입니다."
            }
        ],
        "examples": [
            {
                "ko": "이 정수장은 입상활성탄 여과지 4개를 운영하고 있습니다.",
                "vi": "Nhà máy nước này vận hành 4 bể lọc than hoạt tính dạng hạt (GAC).",
                "situation": "formal"
            },
            {
                "ko": "여름철 조류 냄새 제거를 위해 분말활성탄을 주입합니다.",
                "vi": "Bơm than hoạt tính dạng bột (PAC) để khử mùi tảo vào mùa hè.",
                "situation": "onsite"
            },
            {
                "ko": "활성탄 교체 주기는 사용량에 따라 1~2년입니다.",
                "vi": "Chu kỳ thay than hoạt tính là 1-2 năm tùy mức độ sử dụng.",
                "situation": "formal"
            }
        ],
        "relatedTerms": ["정수장", "고도처리", "흡착", "재생", "GAC"]
    },
    {
        "slug": "he-thong-xu-ly-nuoc-tai-su-dung",
        "korean": "중수처리시설",
        "vietnamese": "Hệ thống xử lý nước tái sử dụng",
        "hanja": "中水處理施設",
        "hanjaReading": "가운데 중(中) + 물 수(水) + 처리할 처(處) + 다스릴 리(理) + 베풀 시(施) + 설치할 설(設)",
        "pronunciation": "중수처리시설",
        "meaningKo": "사용한 물(생활하수, 빗물 등)을 재처리하여 화장실 용수, 조경용수, 청소용수 등 비음용 목적으로 재이용하는 시설입니다. 통역 시 '중수(中水)'는 상수(上水: 식수)와 하수(下水: 오수)의 중간 단계 물이라는 의미이며, 베트남어로는 'nước tái sử dụng' 또는 'nước tái chế'로 표현합니다. 중수도(中水道) 시스템은 물 절약과 환경 보호를 위해 최근 건축물에서 의무화되는 추세이며, 처리 수준(BOD, SS, 대장균 등)과 용도별 수질 기준을 명확히 설명할 수 있어야 합니다. 특히 '중수'와 '재이용수'는 같은 의미로 사용되지만, '중수도'는 시스템 전체를 의미한다는 차이를 인지해야 합니다.",
        "meaningVi": "Hệ thống xử lý và tái sử dụng nước đã qua sử dụng (nước thải sinh hoạt, nước mưa) cho các mục đích không uống như tưới cây, rửa toilet, lau dọn. Góp phần tiết kiệm nước sạch và bảo vệ môi trường. Còn gọi là hệ thống nước tái chế hoặc nước xám (greywater).",
        "context": "친환경 건축물 설계 시, 물 재이용 시스템 도입 논의 시, 빌딩 유지관리 및 에너지 절약 프로젝트에서 사용됩니다.",
        "culturalNote": "한국은 2000년대 이후 대형 건축물(연면적 3만㎡ 이상)에 중수도 설치가 의무화되었으며, 화장실 세정수의 50% 이상을 중수로 사용하도록 권장됩니다. 최근에는 MBR(막분리활성슬러지) 기술을 적용한 고도 중수처리가 일반화되고 있습니다. 베트남은 중수도 개념이 아직 초기 단계로, 고급 빌딩이나 산업단지 일부에서만 시범 운영되고 있으며, 법적 기준도 명확하지 않은 경우가 많습니다. 통역 시 한국의 중수도 의무화 정책과 수질 기준(화장실용 BOD 10mg/L 이하 등)을 소개하면서, 베트님에서의 적용 가능성과 경제성을 함께 논의하는 것이 중요합니다. 또한 '중수'는 식수가 아니므로 배관 색상(보라색 또는 회색)을 구분하고, 오음용(誤飮用) 방지 표지를 반드시 설치해야 한다는 점을 강조해야 합니다.",
        "commonMistakes": [
            {
                "mistake": "'중수'를 'nước sạch thứ cấp' 또는 'nước sạch cấp 2'로 번역",
                "correction": "nước tái sử dụng (또는 nước tái chế, nước trung thủy)",
                "explanation": "'nước sạch cấp 2'는 2급 식수로 오해될 수 있어, 비음용 재이용수임을 명확히 해야 합니다."
            },
            {
                "mistake": "'중수처리'와 '하수처리'를 같은 것으로 설명",
                "correction": "중수처리는 재이용 목적, 하수처리는 환경 방류 목적으로 구분",
                "explanation": "처리 수준과 용도가 다르므로 혼동하지 않아야 합니다."
            },
            {
                "mistake": "중수를 'nước xám(그레이워터)'으로만 표현",
                "correction": "nước xám은 원수(세면, 세탁수)이고, nước tái sử dụng은 처리된 중수",
                "explanation": "그레이워터는 처리 전 원수이므로, 처리 후 중수와 구분해야 합니다."
            }
        ],
        "examples": [
            {
                "ko": "이 빌딩의 중수처리시설은 하루 50톤을 처리합니다.",
                "vi": "Hệ thống xử lý nước tái sử dụng của tòa nhà này xử lý 50 tấn mỗi ngày.",
                "situation": "formal"
            },
            {
                "ko": "중수는 화장실과 조경용수로 사용되며, 식수로는 사용할 수 없습니다.",
                "vi": "Nước tái sử dụng dùng cho toilet và tưới cây, không được dùng làm nước uống.",
                "situation": "formal"
            },
            {
                "ko": "중수도 배관은 보라색으로 표시하여 상수도와 구분합니다.",
                "vi": "Đường ống nước tái sử dụng được đánh dấu màu tím để phân biệt với đường ống nước sạch.",
                "situation": "onsite"
            }
        ],
        "relatedTerms": ["상수도", "하수도", "그레이워터", "MBR", "물재이용"]
    }
]

# 파일 경로
file_path = os.path.join(os.path.dirname(__file__), "..", "data", "terms", "construction.json")

# 기존 데이터 로드
with open(file_path, "r", encoding="utf-8") as f:
    existing_data = json.load(f)

# 새 용어 추가
existing_data.extend(data)

# 저장
with open(file_path, "w", encoding="utf-8") as f:
    json.dump(existing_data, f, ensure_ascii=False, indent=2)

print(f"✅ {len(data)}개 용어 추가 완료: {file_path}")
print("추가된 용어:", [term["korean"] for term in data])
