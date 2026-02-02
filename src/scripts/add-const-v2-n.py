#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Construction Heavy Equipment Terms Script
테마: 중장비/기계 (포클레인, 불도저, 로더, 크레인, 펌프카, 항타기, 로울러, 살수차, 지게차, 고소작업차)
Tier S 품질 기준 준수 (90점 이상)
"""

import json
import os

# 현재 스크립트 위치 기준 상대 경로
SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
JSON_FILE = os.path.join(SCRIPT_DIR, "../data/terms/construction.json")

# ⚠️ data는 배열! None 사용 금지!
data = [
    {
        "slug": "may-dao",
        "korean": "포클레인",
        "vietnamese": "máy đào",
        "hanja": None,
        "hanjaReading": None,
        "pronunciation": "마이 다오",
        "meaningKo": "굴착작업에 사용되는 대표적인 중장비로, 유압식 버킷을 이용해 흙과 암석을 파내는 장비입니다. '포클레인'은 일본 제조사 상표명이지만 한국에서는 일반명사처럼 쓰입니다. 통역 시 주의할 점은 베트남에서는 'máy xúc'(굴삭기), 'máy đào'(굴착기)로 구분하며, 작업 범위에 따라 용어가 달라집니다. 현장에서는 버킷 크기, 작업 깊이, 암석 강도 등을 정확히 전달해야 안전사고를 예방할 수 있습니다.",
        "meaningVi": "Thiết bị hạng nặng đại diện dùng cho công tác đào đất, sử dụng gầu thủy lực để đào đất và đá. 'Excavator' là tên thương hiệu Nhật nhưng ở Hàn được dùng như danh từ thông thường. Cần phân biệt với 'máy xúc' (máy xúc lật) khi thông dịch.",
        "context": "토목 공사, 기초 공사, 굴착 작업",
        "contextVi": "Công trình dân dụng, công trình nền móng, công tác đào",
        "commonMistakes": [
            {
                "mistake": "'máy xúc'으로만 번역",
                "correction": "'máy đào' 또는 구체적으로 'máy đào bánh xích'",
                "explanation": "máy xúc은 로더를 의미할 수 있어 혼동 가능"
            },
            {
                "mistake": "버킷 용량 단위를 번역 없이 그대로 사용",
                "correction": "m³ (mét khối) 단위 명시",
                "explanation": "작업 규모 파악에 필수적인 정보"
            },
            {
                "mistake": "'포클레인'을 그대로 음차",
                "correction": "정확한 베트남어 기계 용어 사용",
                "explanation": "현장 의사소통의 정확성 확보"
            }
        ],
        "culturalNote": "한국에서는 '포크레인', '포클레인'이 일반명사화되어 있지만, 베트남에서는 제조사와 무관하게 'máy đào', 'máy xúc đào'를 사용합니다. 한국 현장은 일본식 장비 명칭이 많이 남아있어 통역 시 주의가 필요합니다. 또한 한국은 장비 운전자의 자격증 체계가 베트남보다 엄격하며, 작업 전 안전 브리핑이 필수입니다.",
        "examples": [
            {
                "ko": "0.7 규격 포클레인으로 기초 굴착을 시작하겠습니다.",
                "vi": "Bắt đầu đào móng bằng máy đào 0.7 m³.",
                "situation": "formal"
            },
            {
                "ko": "포크레인 기사님, 이쪽 배관 조심해서 파주세요.",
                "vi": "Anh máy đào ơi, cẩn thận đường ống bên này nhé.",
                "situation": "onsite"
            },
            {
                "ko": "비 오면 포클레인 작업 중단하고 대기해야 해요.",
                "vi": "Mưa thì phải dừng máy đào và chờ.",
                "situation": "informal"
            }
        ],
        "relatedTerms": [
            "굴착",
            "버킷",
            "중장비"
        ]
    },
    {
        "slug": "may-uon",
        "korean": "불도저",
        "vietnamese": "máy ủi",
        "hanja": None,
        "hanjaReading": None,
        "pronunciation": "마이 우이",
        "meaningKo": "전면에 넓은 블레이드를 장착하여 흙과 암석을 밀어내거나 고르는 작업에 사용되는 궤도형 중장비입니다. 'bulldozer'는 영어 외래어로 한국 현장에서 그대로 사용됩니다. 통역 시 주의할 점은 '정지작업'(땅 고르기)과 '토공작업'(흙 이동)을 명확히 구분해야 하며, 블레이드 각도, 작업 경사도 등 기술 사양을 정확히 전달해야 합니다. 베트남에서는 'máy ủi đất'로 더 구체적으로 표현하기도 합니다.",
        "meaningVi": "Thiết bị hạng nặng có dạng bánh xích, gắn lưỡi rộng phía trước để đẩy hoặc san phẳng đất và đá. Tiếng Anh 'bulldozer' được dùng trực tiếp tại Hàn Quốc. Cần phân biệt rõ công tác san nền và di chuyển đất khi thông dịch.",
        "context": "토목 공사, 정지작업, 토공작업",
        "contextVi": "Công trình dân dụng, công tác san nền, đào đất",
        "commonMistakes": [
            {
                "mistake": "'máy đào'로 혼동",
                "correction": "'máy ủi' 또는 'máy ủi đất'",
                "explanation": "포클레인(굴착)과 불도저(밀기/고르기)는 작업이 다름"
            },
            {
                "mistake": "블레이드 각도 지시를 단순히 '각도'로만 번역",
                "correction": "'góc lưỡi máy ủi' 명시",
                "explanation": "작업 효율과 안전에 직결되는 정보"
            },
            {
                "mistake": "'정지작업'을 '멈추는 작업'으로 오역",
                "correction": "'công tác san nền' (땅 고르기)",
                "explanation": "토목 전문 용어의 정확한 이해 필요"
            }
        ],
        "culturalNote": "한국 건설현장에서 불도저는 부지 조성 초기 단계에서 주로 사용되며, 작업 전 측량 기준점 확인이 필수입니다. 베트남 현장은 상대적으로 소규모 장비를 선호하는 경향이 있어, 장비 규격과 작업 범위에 대한 사전 협의가 중요합니다. 또한 한국은 소음 및 진동 규제가 엄격하여 작업 시간대 제한이 있을 수 있습니다.",
        "examples": [
            {
                "ko": "불도저로 1차 정지작업을 완료한 후 그레이더를 투입합니다.",
                "vi": "Sau khi hoàn thành công tác san nền sơ bộ bằng máy ủi, sẽ đưa máy san vào.",
                "situation": "formal"
            },
            {
                "ko": "불도저 블레이드 각도 15도로 조정해 주세요.",
                "vi": "Điều chỉnh góc lưỡi máy ủi 15 độ.",
                "situation": "onsite"
            },
            {
                "ko": "이 구간은 불도저로 3회 왕복하면 평탄도 기준 맞을 거예요.",
                "vi": "Đoạn này máy ủi qua lại 3 lần là đạt tiêu chuẩn độ bằng phẳng.",
                "situation": "informal"
            }
        ],
        "relatedTerms": [
            "정지작업",
            "블레이드",
            "토공작업"
        ]
    },
    {
        "slug": "may-xuc-lat",
        "korean": "로더",
        "vietnamese": "máy xúc lật",
        "hanja": None,
        "hanjaReading": None,
        "pronunciation": "마이 숙 랏",
        "meaningKo": "전면에 대형 버킷을 장착하여 흙, 자갈, 골재 등을 퍼서 덤프트럭에 적재하거나 이동시키는 바퀴형 중장비입니다. 'loader'는 영어 외래어로 한국 현장에서는 '로다', '로우더'로도 불립니다. 통역 시 주의할 점은 휠로더(바퀴형)와 트랙로더(궤도형)를 구분하고, 버킷 용량과 적재 사이클을 정확히 전달해야 합니다. 골재 적재 시 과적 방지와 적재 균형이 안전의 핵심입니다.",
        "meaningVi": "Thiết bị hạng nặng có bánh lốp, gắn gầu lớn phía trước để xúc đất, sỏi, cốt liệu rồi chất lên xe tải hoặc di chuyển. Tiếng Anh 'loader' được phát âm là 'ro-deo' hoặc 'ro-u-deo' tại Hàn. Cần phân biệt wheel loader và track loader khi thông dịch.",
        "context": "골재 적재, 토사 운반, 야드 작업",
        "contextVi": "Chất cốt liệu, vận chuyển đất, công việc bãi",
        "commonMistakes": [
            {
                "mistake": "'máy đào'로 번역",
                "correction": "'máy xúc lật' 또는 'máy xúc bánh lốp'",
                "explanation": "로더는 적재용, 포클레인은 굴착용으로 용도가 다름"
            },
            {
                "mistake": "버킷 용량을 '삽 크기'로 의역",
                "correction": "'dung tích gầu' (버킷 용량) 정확히 명시",
                "explanation": "작업 효율 계산에 필수적"
            },
            {
                "mistake": "'로더' 음차 그대로 사용",
                "correction": "베트남어 정식 명칭 사용",
                "explanation": "현장 작업자와의 원활한 소통 위해"
            }
        ],
        "culturalNote": "한국 현장에서 로더는 골재장, 야드에서 많이 사용되며, 작업 효율을 'cycle time'(사이클 타임)으로 측정합니다. 베트남에서는 소형 로더나 스키드로더(bobcat)를 선호하는 경우가 많아, 장비 크기와 작업 공간에 대한 사전 확인이 필요합니다. 한국은 과적 단속이 엄격하여 적재량 관리가 중요합니다.",
        "examples": [
            {
                "ko": "3㎥ 로더로 골재 적재 작업을 진행하겠습니다.",
                "vi": "Tiến hành chất cốt liệu bằng máy xúc lật 3 m³.",
                "situation": "formal"
            },
            {
                "ko": "로더 기사님, 덤프트럭 적재할 때 과적 주의해 주세요.",
                "vi": "Anh máy xúc, cẩn thận chất quá tải khi đổ lên xe ben nhé.",
                "situation": "onsite"
            },
            {
                "ko": "이 로더는 사이클 타임이 빨라서 작업 효율 좋아요.",
                "vi": "Máy xúc này chu kỳ nhanh nên hiệu suất tốt.",
                "situation": "informal"
            }
        ],
        "relatedTerms": [
            "골재",
            "적재",
            "덤프트럭"
        ]
    },
    {
        "slug": "cau-truc",
        "korean": "크레인",
        "vietnamese": "cẩu trục",
        "hanja": None,
        "hanjaReading": None,
        "pronunciation": "꺼우 쭉",
        "meaningKo": "고층 건물이나 중량물 인양 작업에 사용되는 중장비로, 타워크레인, 이동식 크레인, 트럭크레인 등 종류가 다양합니다. 'crane'은 영어 외래어로 한국에서는 '크레인'으로 발음합니다. 통역 시 중요한 점은 인양 하중(ton), 작업 반경(radius), 붐 길이(boom length), 신호수 지시 등을 정확히 전달해야 하며, 안전사고 예방을 위해 풍속 제한과 작업 중지 기준을 명확히 해야 합니다.",
        "meaningVi": "Thiết bị hạng nặng dùng để nâng hạ vật nặng ở công trình cao tầng, có nhiều loại như cẩu tháp, cẩu di động, cẩu gắn xe tải. Tiếng Anh 'crane' được phát âm là 'keu-re-in' tại Hàn. Khi thông dịch cần truyền đạt chính xác tải trọng nâng, bán kính làm việc, chiều dài cần cẩu.",
        "context": "건축 공사, 중량물 인양, 고층 건물",
        "contextVi": "Xây dựng, nâng vật nặng, công trình cao tầng",
        "commonMistakes": [
            {
                "mistake": "'máy nâng'으로 단순 번역",
                "correction": "'cẩu trục' 또는 구체적으로 'cẩu tháp', 'cẩu bánh lốp'",
                "explanation": "크레인 종류에 따라 작업 범위와 안전 기준이 다름"
            },
            {
                "mistake": "인양 하중을 kg 단위만 사용",
                "correction": "'tấn' (ton) 단위로 통일",
                "explanation": "건설 현장에서는 ton 단위가 표준"
            },
            {
                "mistake": "'신호수'를 단순히 '신호하는 사람'으로 번역",
                "correction": "'người chỉ huy cẩu' (크레인 지휘자)",
                "explanation": "안전 관리의 핵심 역할 명시"
            }
        ],
        "culturalNote": "한국 건설현장에서 크레인 작업은 가장 위험도가 높은 작업 중 하나로, 작업 전 TBM(Tool Box Meeting) 필수이며 풍속 10m/s 이상 시 작업 중단이 원칙입니다. 베트남 현장은 타워크레인보다 이동식 크레인을 선호하는 경우가 많으며, 한국만큼 엄격한 자격증 제도가 없어 작업자 숙련도 확인이 중요합니다. 신호수의 역할과 책임 범위도 양국이 다를 수 있습니다.",
        "examples": [
            {
                "ko": "25톤 크레인으로 철골 부재를 인양하겠습니다.",
                "vi": "Nâng cấu kiện thép bằng cẩu trục 25 tấn.",
                "situation": "formal"
            },
            {
                "ko": "신호수 지시 없이 크레인 작업 절대 금지입니다.",
                "vi": "Tuyệt đối cấm vận hành cẩu trục mà không có chỉ huy.",
                "situation": "onsite"
            },
            {
                "ko": "오늘 바람 세니까 크레인 작업은 내일로 미뤄요.",
                "vi": "Hôm nay gió mạnh nên việc cẩu trục dời sang ngày mai.",
                "situation": "informal"
            }
        ],
        "relatedTerms": [
            "인양",
            "타워크레인",
            "신호수"
        ]
    },
    {
        "slug": "xe-bom-be-tong",
        "korean": "펌프카",
        "vietnamese": "xe bơm bê tông",
        "hanja": None,
        "hanjaReading": None,
        "pronunciation": "쎄 범 베 똥",
        "meaningKo": "레미콘 타설 작업 시 콘크리트를 압송하여 목적지까지 운반하는 특수 차량으로, 붐대(boom)를 이용해 고층 또는 원거리 타설이 가능합니다. '펌프카'는 'pump car'를 한국식으로 발음한 외래어이며, 정식 명칭은 '콘크리트 펌프차'입니다. 통역 시 중요한 점은 펌프 용량(㎥/h), 붐대 길이, 압송 거리, 배관 연결 방식 등을 정확히 전달해야 하며, 타설 속도와 콘크리트 슬럼프 값을 실시간으로 공유해야 합니다.",
        "meaningVi": "Xe đặc biệt dùng để bơm và vận chuyển bê tông đến vị trí đổ, có cần bơm (boom) giúp đổ tầng cao hoặc khoảng cách xa. 'Pump car' phát âm Hàn là 'peom-peu-ka', tên chính thức là 'xe bơm bê tông'. Cần truyền đạt chính xác dung tích bơm, chiều dài cần, khoảng cách bơm khi thông dịch.",
        "context": "콘크리트 타설, 레미콘 작업, 고층 타설",
        "contextVi": "Đổ bê tông, công việc bê tông trộn sẵn, đổ tầng cao",
        "commonMistakes": [
            {
                "mistake": "'xe bơm'으로만 번역",
                "correction": "'xe bơm bê tông' 전체 명칭 사용",
                "explanation": "다른 펌프차와 혼동 방지"
            },
            {
                "mistake": "붐대를 '막대기'로 의역",
                "correction": "'cần bơm' (펌프 붐) 정확한 용어 사용",
                "explanation": "장비의 핵심 부품 명칭"
            },
            {
                "mistake": "'압송'을 단순히 '밀어넣기'로 번역",
                "correction": "'bơm ép' (압력으로 펌핑)",
                "explanation": "콘크리트 타설의 기술적 특성 반영"
            }
        ],
        "culturalNote": "한국 건설현장에서 펌프카 작업은 레미콘 도착 시간과 정확히 맞춰야 하며, 타설 중단 시간이 길어지면 콘크리트가 경화되어 배관 막힘 사고가 발생할 수 있습니다. 베트남 현장은 소규모 프로젝트에서 인력 타설을 병행하는 경우가 많아, 펌프카 사용 여부와 작업 방식에 대한 사전 협의가 필요합니다. 한국은 펌프카 배관 세척과 유지보수 규정이 엄격합니다.",
        "examples": [
            {
                "ko": "28미터 붐대 펌프카로 5층 슬라브 타설을 시작합니다.",
                "vi": "Bắt đầu đổ sàn tầng 5 bằng xe bơm có cần 28 mét.",
                "situation": "formal"
            },
            {
                "ko": "펌프카 압송 속도 좀 늦춰주세요, 진동기 작업 속도가 안 맞아요.",
                "vi": "Giảm tốc độ bơm xuống, tốc độ đầm không theo kịp.",
                "situation": "onsite"
            },
            {
                "ko": "레미콘 10대 연속 타설이니까 펌프카 대기하고 있어야 해요.",
                "vi": "Đổ liên tục 10 xe bê tông nên xe bơm phải chờ sẵn.",
                "situation": "informal"
            }
        ],
        "relatedTerms": [
            "레미콘",
            "타설",
            "슬럼프"
        ]
    },
    {
        "slug": "may-dong-coc",
        "korean": "항타기",
        "vietnamese": "máy đóng cọc",
        "hanja": "杭打機",
        "hanjaReading": "항(항목 항) + 타(칠 타) + 기(기계 기)",
        "pronunciation": "마이 동 꼭",
        "meaningKo": "기초 공사에서 지반에 말뚝(pile)을 박아넣는 중장비로, 드롭 해머, 디젤 해머, 유압 해머 등 종류가 다양합니다. 한자어 '항타기'는 '말뚝을 때려 박는 기계'라는 뜻으로, 건설 현장에서는 'pile driver'라는 영어 용어도 함께 사용됩니다. 통역 시 중요한 점은 말뚝 종류(PC말뚝, PHC말뚝, 강관말뚝), 타격 에너지, 관입 깊이, 지지력 등을 정확히 전달해야 하며, 소음과 진동 관리도 필수 전달 사항입니다.",
        "meaningVi": "Thiết bị hạng nặng dùng để đóng cọc vào nền đất trong công trình móng, có nhiều loại như búa thả, búa diesel, búa thủy lực. Hán tự 'hàng đả cơ' có nghĩa là 'máy đóng cọc', cũng dùng thuật ngữ tiếng Anh 'pile driver'. Cần truyền đạt chính xác loại cọc, năng lượng đập, độ sâu đóng, sức chịu tải khi thông dịch.",
        "context": "기초 공사, 말뚝 공사, 지반 조사",
        "contextVi": "Công trình móng, công trình cọc, khảo sát nền đất",
        "commonMistakes": [
            {
                "mistake": "'máy đập'으로 단순 번역",
                "correction": "'máy đóng cọc' 전문 용어 사용",
                "explanation": "기초 공사의 핵심 장비 명칭 정확히"
            },
            {
                "mistake": "말뚝을 '나무 막대기'로 의역",
                "correction": "'cọc' (말뚝) 또는 'cọc bê tông' (콘크리트 말뚝)",
                "explanation": "공사 자재의 정확한 명칭"
            },
            {
                "mistake": "'관입'을 단순히 '들어간다'로 번역",
                "correction": "'độ sâu xuyên nhập' (관입 깊이)",
                "explanation": "지지력 계산의 핵심 개념"
            }
        ],
        "culturalNote": "한국 건설현장에서 항타기는 기초 공사의 핵심 장비이며, 작업 전 지반 조사 데이터와 말뚝 시공 계획서가 필수입니다. 도심지 공사에서는 소음과 진동 민원이 빈번하여 저소음 공법(프리보링, 회전압입 등)을 병행하는 경우가 많습니다. 베트남 현장은 연약 지반이 많아 말뚝 길이와 지지력 산정에 주의가 필요하며, 한국만큼 정밀한 지반 조사가 이루어지지 않을 수 있습니다.",
        "examples": [
            {
                "ko": "PHC 말뚝 500mm를 항타기로 15미터 관입합니다.",
                "vi": "Đóng cọc PHC 500mm xuống 15 mét bằng máy đóng cọc.",
                "situation": "formal"
            },
            {
                "ko": "항타기 작업 소음이 크니까 인근 주민께 사전 안내 필수예요.",
                "vi": "Tiếng ồn máy đóng cọc lớn nên phải thông báo trước cho dân xung quanh.",
                "situation": "onsite"
            },
            {
                "ko": "이 지반은 연약해서 항타기보다 회전압입이 나을 것 같아요.",
                "vi": "Nền đất này yếu nên dùng ép xoay hơn máy đóng cọc.",
                "situation": "informal"
            }
        ],
        "relatedTerms": [
            "말뚝",
            "기초공사",
            "지반조사"
        ]
    },
    {
        "slug": "may-lu",
        "korean": "로울러",
        "vietnamese": "máy lù",
        "hanja": None,
        "hanjaReading": None,
        "pronunciation": "마이 루",
        "meaningKo": "도로 포장이나 성토 공사에서 지반이나 아스팔트를 다지는 중장비로, 진동 로울러, 탠덤 로울러, 타이어 로울러 등 종류가 다양합니다. 'roller'는 영어 외래어로 한국에서는 '로울러', '롤러', '로라'로 불립니다. 통역 시 중요한 점은 다짐 횟수, 진동 주파수, 중량, 작업 속도 등을 정확히 전달해야 하며, 다짐도 시험 결과와 연계하여 품질 관리 기준을 명확히 해야 합니다.",
        "meaningVi": "Thiết bị hạng nặng dùng để đầm nén nền đất hoặc nhựa đường trong công trình đường bộ hoặc đắp đất, có nhiều loại như máy lù rung, máy lù tandem, máy lù bánh lốp. Tiếng Anh 'roller' phát âm là 'ro-ul-leo' tại Hàn. Cần truyền đạt chính xác số lần đầm, tần số rung, trọng lượng khi thông dịch.",
        "context": "도로 공사, 성토 작업, 다짐 작업",
        "contextVi": "Công trình đường, công tác đắp đất, đầm nén",
        "commonMistakes": [
            {
                "mistake": "'máy nén'으로만 번역",
                "correction": "'máy lù' 또는 구체적으로 'máy lù rung'",
                "explanation": "압축기(compressor)와 혼동 방지"
            },
            {
                "mistake": "'다짐'을 '누르기'로 의역",
                "correction": "'đầm nén' (다짐) 전문 용어 사용",
                "explanation": "토목 공사의 핵심 품질 관리 용어"
            },
            {
                "mistake": "진동 주파수를 '떨림'으로 번역",
                "correction": "'tần số rung' (진동 주파수) 기술 용어 사용",
                "explanation": "다짐 품질에 직접적 영향"
            }
        ],
        "culturalNote": "한국 도로 공사에서 로울러는 다짐도 95% 이상을 목표로 하며, 현장다짐시험(FDT)으로 품질을 검증합니다. 작업 시 다짐 횟수와 중복폭이 규정되어 있어 정밀한 관리가 필요합니다. 베트남 현장은 다짐도 기준이 상대적으로 낮거나 검증이 느슨할 수 있어, 한국 시공사가 참여하는 경우 품질 기준에 대한 명확한 사전 협의가 필요합니다. 로울러 작업 속도와 순서도 중요한 관리 포인트입니다.",
        "examples": [
            {
                "ko": "10톤 진동 로울러로 노상 다짐 작업을 실시합니다.",
                "vi": "Thực hiện đầm nén nền đường bằng máy lù rung 10 tấn.",
                "situation": "formal"
            },
            {
                "ko": "로울러 5회 왕복 후 다짐도 시험 진행합니다.",
                "vi": "Sau 5 lượt qua lại máy lù sẽ tiến hành kiểm tra độ chặt.",
                "situation": "onsite"
            },
            {
                "ko": "이 구간은 땅이 물러서 로울러 몇 번 더 해야 할 것 같아요.",
                "vi": "Đoạn này đất mềm nên máy lù phải đầm thêm mấy lần nữa.",
                "situation": "informal"
            }
        ],
        "relatedTerms": [
            "다짐",
            "노상",
            "아스팔트"
        ]
    },
    {
        "slug": "xe-tuoi-nuoc",
        "korean": "살수차",
        "vietnamese": "xe tưới nước",
        "hanja": "撒水車",
        "hanjaReading": "살(뿌릴 살) + 수(물 수) + 차(수레 차)",
        "pronunciation": "쎄 뜨어이 느억",
        "meaningKo": "공사 현장에서 비산먼지 억제를 위해 도로나 작업장에 물을 뿌리는 특수 차량입니다. 한자어 '살수차'는 '물을 뿌리는 차'라는 뜻으로, 환경 규제가 강화되면서 건설 현장의 필수 장비가 되었습니다. 통역 시 중요한 점은 살수 주기, 물 탱크 용량, 살수 범위, 미세먼지 농도 기준 등을 정확히 전달해야 하며, 계절과 날씨에 따른 운영 계획도 공유해야 합니다.",
        "meaningVi": "Xe đặc biệt dùng để phun nước lên đường hoặc khu vực thi công nhằm ngăn bụi bay tại công trường. Hán tự 'tát thủy xa' có nghĩa là 'xe phun nước', đã trở thành thiết bị bắt buộc do quy định môi trường nghiêm ngặt. Cần truyền đạt chu kỳ phun, dung tích bồn nước, phạm vi phun khi thông dịch.",
        "context": "환경 관리, 비산먼지 억제, 현장 관리",
        "contextVi": "Quản lý môi trường, ngăn chặn bụi bay, quản lý hiện trường",
        "commonMistakes": [
            {
                "mistake": "'xe nước'로 단순 번역",
                "correction": "'xe tưới nước' 또는 'xe phun nước'",
                "explanation": "급수차(물 공급)와 구분"
            },
            {
                "mistake": "'비산먼지'를 '날아가는 먼지'로 의역",
                "correction": "'bụi bay' (비산먼지) 환경 용어 사용",
                "explanation": "환경 규제의 핵심 관리 대상"
            },
            {
                "mistake": "살수 주기를 단순히 '횟수'로만 번역",
                "correction": "'chu kỳ tưới nước' (살수 주기) 명시",
                "explanation": "환경 관리 계획의 중요 항목"
            }
        ],
        "culturalNote": "한국 건설현장에서는 미세먼지 계절관리제(12~3월) 기간에 살수차 운영이 의무화되어 있으며, 일일 살수 기록을 작성해야 합니다. 도심 공사 현장은 살수 주기가 더 짧고 관리가 엄격합니다. 베트남 현장은 건기와 우기의 차이가 커서 계절별 살수 계획이 달라야 하며, 한국만큼 미세먼지 규제가 엄격하지 않아 현장 관리 수준에 차이가 있을 수 있습니다.",
        "examples": [
            {
                "ko": "오늘 미세먼지 농도가 높아 살수차를 2시간마다 운행합니다.",
                "vi": "Hôm nay nồng độ bụi mịn cao nên xe tưới nước chạy 2 giờ một lần.",
                "situation": "formal"
            },
            {
                "ko": "진출입로에 흙이 많이 묻었으니 살수차 한 번 더 돌려주세요.",
                "vi": "Đường ra vào dính nhiều đất, cho xe tưới chạy thêm một lượt.",
                "situation": "onsite"
            },
            {
                "ko": "비 오면 살수차 운행 안 해도 되지만, 기록은 남겨야 해요.",
                "vi": "Mưa thì không cần xe tưới nhưng phải ghi chép lại.",
                "situation": "informal"
            }
        ],
        "relatedTerms": [
            "비산먼지",
            "환경관리",
            "미세먼지"
        ]
    },
    {
        "slug": "xe-nang",
        "korean": "지게차",
        "vietnamese": "xe nâng",
        "hanja": None,
        "hanjaReading": None,
        "pronunciation": "쎄 낭",
        "meaningKo": "자재 야드나 창고에서 팔레트에 실린 자재를 들어 올려 이동시키는 소형 중장비입니다. '지게차'는 순우리말 '지게'(등에 지는 운반 도구)와 '차'가 합쳐진 단어로, 영어로는 'forklift'입니다. 통역 시 중요한 점은 적재 하중, 포크 길이, 리프트 높이, 좁은 통로 작업 가능 여부 등을 정확히 전달해야 하며, 팔레트 규격과 자재 특성에 맞는 작업 방식을 공유해야 합니다.",
        "meaningVi": "Thiết bị nhỏ dùng để nâng và di chuyển vật liệu trên pallet tại khu vực bãi hoặc kho. 'Địa giá xa' là từ thuần Hàn kết hợp giữa 'địa giá' (dụng cụ vận chuyển vác trên lưng) và 'xa', tiếng Anh là 'forklift'. Cần truyền đạt tải trọng, chiều dài chĩa, chiều cao nâng khi thông dịch.",
        "context": "자재 야드, 창고 관리, 하역 작업",
        "contextVi": "Bãi vật liệu, quản lý kho, bốc dỡ",
        "commonMistakes": [
            {
                "mistake": "'xe tải nhỏ'로 의역",
                "correction": "'xe nâng' 정식 명칭 사용",
                "explanation": "운반 차량과 명확히 구분"
            },
            {
                "mistake": "'포크'를 '삽'으로 번역",
                "correction": "'chĩa xe nâng' (포크) 전문 용어 사용",
                "explanation": "지게차의 핵심 작업 도구 명칭"
            },
            {
                "mistake": "리프트 높이를 단순히 '높이'로만 번역",
                "correction": "'chiều cao nâng' (리프트 높이) 명시",
                "explanation": "작업 범위 결정의 핵심 스펙"
            }
        ],
        "culturalNote": "한국 건설현장에서 지게차는 자재 야드와 창고에서 필수 장비이며, 좁은 공간에서도 작동 가능한 소형 지게차가 선호됩니다. 지게차 운전은 별도 자격증이 필요하며, 안전사고 예방을 위해 작업 구역 설정과 보행자 통제가 중요합니다. 베트남 현장은 팔레트 규격이 표준화되지 않은 경우가 많아, 자재 적재 방식과 지게차 포크 길이에 대한 사전 확인이 필요합니다.",
        "examples": [
            {
                "ko": "3톤 지게차로 철근 팔레트를 야드에서 현장으로 이동합니다.",
                "vi": "Di chuyển pallet thép từ bãi vào hiện trường bằng xe nâng 3 tấn.",
                "situation": "formal"
            },
            {
                "ko": "지게차로 자재 옮길 때 포크 높이 조심하세요, 전선 걸려요.",
                "vi": "Khi xe nâng chuyển vật liệu cẩn thận chiều cao chĩa, dễ vướng dây điện.",
                "situation": "onsite"
            },
            {
                "ko": "이 통로는 좁아서 지게차 못 들어가요, 수작업 해야 해요.",
                "vi": "Lối đi này hẹp xe nâng không vào được, phải làm bằng tay.",
                "situation": "informal"
            }
        ],
        "relatedTerms": [
            "팔레트",
            "하역",
            "자재야드"
        ]
    },
    {
        "slug": "xe-nang-nguoi",
        "korean": "고소작업차",
        "vietnamese": "xe nâng người",
        "hanja": "高所作業車",
        "hanjaReading": "고(높을 고) + 소(곳 소) + 작(지을 작) + 업(업 업) + 차(수레 차)",
        "pronunciation": "쎄 낭 응으어이",
        "meaningKo": "고층 건물 외벽 작업이나 천장 설비 공사를 위해 작업자를 높은 곳으로 올려주는 특수 차량입니다. 한자어 '고소작업차'는 '높은 곳에서 작업하는 차'라는 뜻으로, 영어로는 'aerial work platform' 또는 'cherry picker'입니다. 통역 시 중요한 점은 최대 작업 높이, 바스켓 적재 하중, 전도 위험 방지 조치, 전선 접촉 주의 등 안전 관련 사항을 정확히 전달해야 합니다.",
        "meaningVi": "Xe đặc biệt dùng để nâng người lao động lên cao nhằm làm việc ở tường ngoài tòa cao tầng hoặc lắp đặt trần. Hán tự 'cao sở tác nghiệp xa' có nghĩa 'xe làm việc ở nơi cao', tiếng Anh là 'aerial work platform' hoặc 'cherry picker'. Cần truyền đạt chiều cao làm việc tối đa, tải trọng sọt, biện pháp phòng ngừa lật xe khi thông dịch.",
        "context": "외벽 공사, 설비 공사, 고소 작업",
        "contextVi": "Công trình tường ngoài, lắp đặt thiết bị, làm việc trên cao",
        "commonMistakes": [
            {
                "mistake": "'cẩu người'로 번역",
                "correction": "'xe nâng người' 또는 'xe thang nâng người'",
                "explanation": "크레인 인양과 혼동 방지"
            },
            {
                "mistake": "'바스켓'을 단순히 '바구니'로 의역",
                "correction": "'sọt làm việc' (작업 바스켓) 전문 용어",
                "explanation": "고소작업차의 핵심 작업 공간"
            },
            {
                "mistake": "'전도'를 '떨어짐'으로 오역",
                "correction": "'lật xe' (전도, 차량이 넘어짐)",
                "explanation": "고소작업차의 주요 위험 요인"
            }
        ],
        "culturalNote": "한국 건설현장에서 고소작업차는 발판 설치가 어려운 곳에서 많이 사용되며, 작업 전 지반 상태 확인과 안전 난간 설치가 필수입니다. 전선 접촉 사고 예방을 위해 이격 거리를 엄격히 준수해야 하며, 풍속 10m/s 이상 시 작업 중단이 원칙입니다. 베트남 현장은 죽비계(대나무 비계)를 아직 많이 사용하여 고소작업차 도입이 상대적으로 적으며, 운전자 자격증 제도도 한국만큼 체계적이지 않을 수 있습니다.",
        "examples": [
            {
                "ko": "18미터 고소작업차로 외벽 마감 작업을 진행합니다.",
                "vi": "Tiến hành hoàn thiện tường ngoài bằng xe nâng người 18 mét.",
                "situation": "formal"
            },
            {
                "ko": "고소작업차 바스켓에 2명 이상 탑승 금지입니다.",
                "vi": "Cấm hơn 2 người lên sọt xe nâng.",
                "situation": "onsite"
            },
            {
                "ko": "오늘 바람 세니까 고소작업차는 내일 쓰는 게 안전해요.",
                "vi": "Hôm nay gió mạnh nên dùng xe nâng người ngày mai mới an toàn.",
                "situation": "informal"
            }
        ],
        "relatedTerms": [
            "외벽작업",
            "고소작업",
            "안전난간"
        ]
    }
]

def main():
    """메인 실행 함수"""
    print("=" * 70)
    print("Construction Heavy Equipment Terms Script")
    print("테마: 중장비/기계 (포클레인, 불도저, 로더, 크레인, 펌프카, 항타기, 로울러, 살수차, 지게차, 고소작업차)")
    print("=" * 70)
    print(f"\n📂 Target file: {JSON_FILE}")
    print(f"📊 Terms to add: {len(data)}")

    # 기존 파일 읽기
    try:
        with open(JSON_FILE, 'r', encoding='utf-8') as f:
            existing_data = json.load(f)
        print(f"✅ Existing terms: {len(existing_data)}")
    except FileNotFoundError:
        print("❌ Error: construction.json not found")
        return
    except json.JSONDecodeError as e:
        print(f"❌ Error: Invalid JSON format - {e}")
        return

    # 중복 체크
    existing_slugs = {term['slug'] for term in existing_data}
    new_slugs = {term['slug'] for term in data}
    duplicates = existing_slugs & new_slugs

    if duplicates:
        print(f"\n⚠️  Warning: Duplicate slugs found: {duplicates}")
        print("Script will NOT execute to prevent duplicates.")
        return

    # 데이터 병합
    merged_data = existing_data + data
    print(f"📈 Total after merge: {len(merged_data)}")

    # 파일 저장
    try:
        with open(JSON_FILE, 'w', encoding='utf-8') as f:
            json.dump(merged_data, f, ensure_ascii=False, indent=2)
        print(f"\n✅ Successfully saved {len(data)} terms to {JSON_FILE}")
        print("\n📋 Added terms:")
        for term in data:
            print(f"  - {term['slug']}: {term['korean']} ({term['vietnamese']})")
    except Exception as e:
        print(f"\n❌ Error saving file: {e}")
        return

    print("\n" + "=" * 70)
    print("✅ Script completed successfully!")
    print("⚠️  Next steps:")
    print("  1. Run: npm run validate:terms -- --domain=construction")
    print("  2. Verify all terms meet Tier S quality (90+ points)")
    print("  3. Commit if validation passes")
    print("=" * 70)

if __name__ == "__main__":
    main()
