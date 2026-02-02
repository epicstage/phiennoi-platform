#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
건설 용어 추가 스크립트: 비계/작업대 테마 (10개)
- 강관비계, 틀비계, 달비계, 브래킷비계, 리프트, 곤돌라, 작업발판, 안전대, 수직구명줄, 수평구명줄
- Tier S 기준 준수 (90점 이상)
"""

import json
import os

# 추가할 용어 데이터 (10개)
data = [
    {
        "slug": "giao-giac-ong-thep",
        "korean": "강관비계",
        "vietnamese": "Giáo giác ống thép",
        "hanja": "鋼管飛階",
        "hanjaReading": "鋼(강철 강) + 管(대롱 관) + 飛(날 비) + 階(층계 계)",
        "pronunciation": "강관비계",
        "meaningKo": "강철 파이프를 조립하여 만든 임시 구조물로, 건축 현장에서 높은 곳 작업을 위해 사용됩니다. 통역 시 '비계'는 단순 '틀'이 아닌 '임시 작업 구조물'임을 명확히 전달해야 합니다. 베트남 현장에서는 대나무 비계(giáo giác tre)와 혼동하지 않도록 'ống thép(강관)'을 강조하세요. 조립식이므로 해체·이동이 가능하며, 안전 규정상 지면에서 2m 이상 작업 시 필수입니다. 강관 직경(48.6mm), 수직재·수평재·가새의 간격, 발판 폭(40cm 이상) 등 규격을 정확히 전달해야 하며, '조립 완료 후 안전 점검 필수'라는 안전 수칙도 함께 통역하세요.",
        "meaningVi": "Kết cấu tạm thời lắp ráp từ ống thép, dùng để làm việc ở độ cao trong công trường xây dựng. Khác với giáo giác tre (giàn giáo tre), giáo giác ống thép có khả năng chịu tải cao hơn và tuân thủ quy chuẩn an toàn quốc tế. Bắt buộc sử dụng khi làm việc trên 2m so với mặt đất.",
        "context": "안전관리, 고소작업",
        "culturalNote": "한국 건설 현장에서는 강관비계가 표준이지만, 베트남 일부 중소 현장에서는 대나무 비계(giáo giác tre)를 여전히 사용합니다. 통역 시 '강관비계는 법적 의무'임을 강조하고, 대나무 비계 사용 시 안전사고 책임 소재를 명확히 전달하세요. 베트남 근로자들이 대나무 비계에 익숙해 강관비계 조립법을 모를 수 있으므로, '사전 교육 필수'라는 점도 통역하세요.",
        "commonMistakes": [
            {
                "mistake": "giàn giáo (일반 비계)",
                "correction": "giáo giác ống thép (강관비계)",
                "explanation": "giàn giáo는 모든 비계를 포괄하는 용어이며, 강관비계는 재질을 명시한 giáo giác ống thép로 구분해야 합니다."
            },
            {
                "mistake": "khung sắt (철제 틀)",
                "correction": "giáo giác ống thép (강관비계)",
                "explanation": "khung sắt는 단순 '철 틀'을 의미하며, 건축 전문 용어로는 giáo giác(비계)를 사용해야 합니다."
            },
            {
                "mistake": "'비계 설치' → lắp đặt giàn giáo (비계 설치)",
                "correction": "'강관비계 조립' → lắp ráp giáo giác ống thép (강관비계 조립)",
                "explanation": "강관비계는 '설치'보다 '조립(lắp ráp)'이 정확하며, 해체 가능한 임시 구조물임을 나타냅니다."
            }
        ],
        "examples": [
            {
                "ko": "3층 외벽 작업을 위해 강관비계를 조립해 주세요.",
                "vi": "Vui lòng lắp ráp giáo giác ống thép để thi công tường ngoài tầng 3.",
                "situation": "onsite"
            },
            {
                "ko": "강관비계 조립 후 안전 점검을 실시하겠습니다.",
                "vi": "Sau khi lắp ráp giáo giác ống thép, chúng tôi sẽ tiến hành kiểm tra an toàn.",
                "situation": "formal"
            },
            {
                "ko": "이 현장은 강관비계 사용이 의무라서 대나무는 쓸 수 없어요.",
                "vi": "Công trường này bắt buộc dùng giáo giác ống thép nên không được dùng tre.",
                "situation": "informal"
            }
        ],
        "relatedTerms": [
            "틀비계",
            "달비계",
            "작업발판",
            "수직재",
            "가새"
        ]
    },
    {
        "slug": "giao-giac-khung",
        "korean": "틀비계",
        "vietnamese": "Giáo giác khung",
        "hanja": None,
        "hanjaReading": None,
        "pronunciation": "틀비계",
        "meaningKo": "프레임 형태로 미리 제작된 비계로, 강관비계보다 조립이 빠르고 구조가 견고합니다. 통역 시 '틀비계'는 '조립식 프레임 비계(frame scaffold)'임을 설명하고, 강관비계와의 차이(조립 속도, 안정성, 비용)를 명확히 전달하세요. 베트남 현장에서는 '틀비계'를 giàn giáo lắp ghép(조립식 비계)로 부르기도 하지만, 정확한 용어는 giáo giác khung입니다. H형·사다리형 등 종류별 명칭, 높이 제한(31m 이하), 수평 연결재 설치 의무 등을 통역할 때는 도면을 함께 보여주며 설명하세요. '틀비계는 외벽 작업에 최적'이라는 장점도 강조합니다.",
        "meaningVi": "Giàn giáo dạng khung được chế tạo sẵn, lắp ráp nhanh hơn giáo giác ống thép và có kết cấu chắc chắn hơn. Thích hợp cho công trình có độ cao dưới 31m, đặc biệt là thi công tường ngoài. Các loại phổ biến: khung chữ H, khung thang.",
        "context": "고층건물, 외벽작업",
        "culturalNote": "한국에서는 중·대형 현장에서 틀비계를 선호하지만, 베트남에서는 비용 문제로 강관비계를 더 많이 사용합니다. 통역 시 '틀비계는 초기 비용이 높지만 공기 단축'이라는 경제성을 설명하고, 발주자가 장기 프로젝트라면 투자 가치가 있다고 조언하세요. 베트남 근로자들이 틀비계 조립 경험이 적을 수 있으므로 '사전 교육 1일 필수'라는 안전 지침도 전달하세요.",
        "commonMistakes": [
            {
                "mistake": "giàn giáo lắp ghép (조립식 비계)",
                "correction": "giáo giác khung (틀비계)",
                "explanation": "lắp ghép은 '조립식'이라는 일반 표현이며, 틀비계는 khung(프레임)을 명시해야 정확합니다."
            },
            {
                "mistake": "khung giàn giáo (비계 틀)",
                "correction": "giáo giác khung (틀비계)",
                "explanation": "어순이 중요하며, giáo giác(비계)가 먼저 오고 khung(틀)이 뒤에 와야 합니다."
            },
            {
                "mistake": "'틀비계 설치' → lắp đặt giáo giác khung",
                "correction": "'틀비계 조립' → lắp ráp giáo giác khung",
                "explanation": "틀비계는 조립(lắp ráp)이 정확하며, 설치(lắp đặt)는 고정 구조물에 사용됩니다."
            }
        ],
        "examples": [
            {
                "ko": "이 건물은 높이가 25m라서 틀비계를 사용하겠습니다.",
                "vi": "Tòa nhà này cao 25m nên chúng tôi sẽ dùng giáo giác khung.",
                "situation": "onsite"
            },
            {
                "ko": "틀비계는 조립이 빠르지만 비용이 강관비계보다 높습니다.",
                "vi": "Giáo giác khung lắp ráp nhanh nhưng chi phí cao hơn giáo giác ống thép.",
                "situation": "formal"
            },
            {
                "ko": "틀비계 쓰면 일주일은 단축되는데, 예산이 빠듯해서 고민이에요.",
                "vi": "Dùng giáo giác khung thì rút ngắn được 1 tuần, nhưng ngân sách hơi chặt nên đang cân nhắc.",
                "situation": "informal"
            }
        ],
        "relatedTerms": [
            "강관비계",
            "H형 틀비계",
            "사다리형 틀비계",
            "수평연결재",
            "조립식비계"
        ]
    },
    {
        "slug": "giao-giac-treo",
        "korean": "달비계",
        "vietnamese": "Giáo giác treo",
        "hanja": None,
        "hanjaReading": None,
        "pronunciation": "달비계",
        "meaningKo": "건물 지붕이나 상부에서 와이어로프로 매달아 사용하는 비계로, 외벽 도장·청소·유리 교체 등에 사용됩니다. 통역 시 '달비계'는 '현수식 비계(suspended scaffold)'이며, 지면 비계와 달리 '공중에 매달린 상태'임을 강조하세요. 베트남에서는 giàn giáo treo(매달린 비계)로도 부르지만, 정확한 용어는 giáo giác treo입니다. 와이어로프 안전율(10배 이상), 추락방지대 설치, 승강장치 점검 등 안전 규정을 통역할 때는 '생명줄(dây cứu sinh)과 별도 설치'를 반드시 언급하세요. 강풍 시(풍속 10m/s 이상) 작업 중지 기준도 전달해야 합니다.",
        "meaningVi": "Giàn giáo được treo từ mái hoặc phần trên của công trình bằng cáp thép, dùng cho sơn tường ngoài, lau kính, bảo trì. Khác với giàn giáo mặt đất, giáo giác treo luôn ở trạng thái lơ lửng. Bắt buộc có dây cứu sinh riêng và hệ thống thăng giáng an toàn.",
        "context": "외벽작업, 고층건물보수",
        "culturalNote": "한국에서는 고층 건물 유지보수에 달비계가 필수지만, 베트남에서는 곤돌라(gondola)를 더 선호합니다. 통역 시 '달비계는 곤돌라보다 설치가 빠르고 비용이 저렴'하다는 장점을 설명하되, '안전교육 2일 필수'라는 조건도 전달하세요. 베트남 근로자들이 달비계 작업 경험이 적을 수 있으므로, '첫 사용 시 안전관리자 동행 의무'를 강조하세요.",
        "commonMistakes": [
            {
                "mistake": "giàn giáo treo (매달린 비계)",
                "correction": "giáo giác treo (달비계)",
                "explanation": "giàn giáo는 일반 비계이며, 전문 용어는 giáo giác을 사용해야 합니다."
            },
            {
                "mistake": "giàn giáo lơ lửng (공중 비계)",
                "correction": "giáo giác treo (달비계)",
                "explanation": "lơ lửng(공중)은 상태 설명이며, treo(매달린)가 달비계의 구조를 정확히 표현합니다."
            },
            {
                "mistake": "'달비계 설치' → lắp đặt giáo giác treo",
                "correction": "'달비계 설치' → lắp dựng giáo giác treo",
                "explanation": "달비계는 '세우는(dựng)' 것이 아닌 '매다는(treo)' 것이므로, lắp treo 또는 lắp dựng 모두 가능합니다."
            }
        ],
        "examples": [
            {
                "ko": "20층 외벽 도장을 위해 달비계를 설치하겠습니다.",
                "vi": "Chúng tôi sẽ lắp giáo giác treo để sơn tường ngoài tầng 20.",
                "situation": "onsite"
            },
            {
                "ko": "달비계 작업 시 안전대와 생명줄을 반드시 착용하세요.",
                "vi": "Khi làm việc trên giáo giác treo, bắt buộc phải đeo dây an toàn và dây cứu sinh.",
                "situation": "formal"
            },
            {
                "ko": "달비계는 바람 세면 위험하니까 오늘은 작업 중지해요.",
                "vi": "Giáo giác treo nguy hiểm khi gió mạnh, nên hôm nay tạm dừng thi công.",
                "situation": "informal"
            }
        ],
        "relatedTerms": [
            "와이어로프",
            "곤돌라",
            "추락방지대",
            "생명줄",
            "승강장치"
        ]
    },
    {
        "slug": "giao-giac-bracket",
        "korean": "브래킷비계",
        "vietnamese": "Giáo giác bracket",
        "hanja": None,
        "hanjaReading": None,
        "pronunciation": "브래킷비계",
        "meaningKo": "건물 벽면에 브래킷(돌출 받침대)을 설치하고 그 위에 작업발판을 얹는 비계로, 좁은 공간이나 지면 설치가 어려운 곳에 사용됩니다. 통역 시 'bracket'은 외래어 그대로 사용하며, '벽면 고정식 비계'임을 설명하세요. 베트남에서는 giàn giáo gắn tường(벽 부착 비계)로도 부르지만, 건설 전문가들은 bracket을 그대로 씁니다. 브래킷 간격(1.8m 이하), 앵커볼트 깊이(10cm 이상), 발판 폭(40cm 이상) 등 시공 기준을 통역할 때는 도면을 가리키며 설명하세요. '브래킷비계는 외벽에 구멍을 뚫으므로 방수 처리 필수'라는 주의사항도 전달해야 합니다.",
        "meaningVi": "Giàn giáo gắn bracket (giá đỡ nhô ra) vào tường và đặt sàn làm việc lên trên, dùng khi không gian hẹp hoặc không thể lắp giàn giáo mặt đất. Khoảng cách giữa các bracket tối đa 1.8m, bu-lông neo sâu tối thiểu 10cm. Sau khi tháo phải xử lý chống thấm vị trí khoan.",
        "context": "협소공간, 벽체작업",
        "culturalNote": "한국에서는 브래킷비계를 리모델링 현장에서 자주 쓰지만, 베트남에서는 인건비가 저렴해 달비계를 선호합니다. 통역 시 '브래킷비계는 장기 작업에 유리'하다는 점을 설명하고, '설치 후 안전점검 필수'를 강조하세요. 베트남 근로자들이 앵커볼트 시공 경험이 부족할 수 있으므로, '시공 교육 반나절 필수'라는 조건도 전달하세요.",
        "commonMistakes": [
            {
                "mistake": "giàn giáo gắn tường (벽 부착 비계)",
                "correction": "giáo giác bracket (브래킷비계)",
                "explanation": "일반적으로 gắn tường로 불리지만, 전문 용어는 bracket을 사용해야 합니다."
            },
            {
                "mistake": "giàn giáo khung treo (매단 틀비계)",
                "correction": "giáo giác bracket (브래킷비계)",
                "explanation": "브래킷비계는 '매다는(treo)' 것이 아니라 '벽에 고정(gắn)'하는 것입니다."
            },
            {
                "mistake": "'브래킷 설치' → lắp đặt bracket",
                "correction": "'브래킷 설치' → gắn bracket vào tường",
                "explanation": "브래킷은 벽에 '고정(gắn)'하는 것이므로 gắn vào tường이 정확합니다."
            }
        ],
        "examples": [
            {
                "ko": "이 좁은 골목에서는 브래킷비계만 설치 가능합니다.",
                "vi": "Trong con hẻm hẹp này chỉ có thể lắp giáo giác bracket.",
                "situation": "onsite"
            },
            {
                "ko": "브래킷비계 시공 후 방수 처리를 반드시 해야 합니다.",
                "vi": "Sau khi thi công giáo giác bracket, bắt buộc phải xử lý chống thấm.",
                "situation": "formal"
            },
            {
                "ko": "브래킷비계 쓰면 외벽에 구멍 뚫어야 해서 나중에 보수해야 돼요.",
                "vi": "Dùng giáo giác bracket thì phải khoan tường, sau này phải sửa lại.",
                "situation": "informal"
            }
        ],
        "relatedTerms": [
            "앵커볼트",
            "작업발판",
            "벽체 고정",
            "방수 처리",
            "리모델링"
        ]
    },
    {
        "slug": "thang-may-xay-dung",
        "korean": "리프트",
        "vietnamese": "Thang máy xây dựng",
        "hanja": None,
        "hanjaReading": None,
        "pronunciation": "리프트",
        "meaningKo": "건설 현장에서 인원과 자재를 수직으로 운반하는 승강기로, 일반 엘리베이터와 달리 개방형 구조입니다. 통역 시 'lift'는 '건설용 리프트(construction hoist)'이며, 일반 엘리베이터(thang máy)와 구별하여 thang máy xây dựng으로 표현하세요. 적재 하중(1톤/2톤), 운행 속도(60m/분), 안전 장치(낙하 방지 장치, 과부하 경보) 등을 통역할 때는 수치를 명확히 전달하세요. '리프트 탑승 시 안전모·안전화 필수'라는 규정과, '정원 초과 금지(8명 이하)'를 강조하세요. 베트남에서는 '리프트'를 cần cẩu(크레인)과 혼동하기 쉬우므로 주의하세요.",
        "meaningVi": "Thiết bị nâng hạ dọc dùng trong xây dựng để chở người và vật liệu, cấu trúc mở khác với thang máy thường. Tải trọng 1-2 tấn, tốc độ 60m/phút, có hệ thống chống rơi và cảnh báo quá tải. Bắt buộc đội mũ, đi giày bảo hộ khi lên xuống. Không vượt quá 8 người.",
        "context": "고층건설, 자재운반",
        "culturalNote": "한국 고층 현장에서는 리프트가 필수지만, 베트남 중소 현장에서는 비용 문제로 크레인과 계단만 쓰는 경우가 많습니다. 통역 시 '리프트는 공기 단축 + 안전성 향상'이라는 투자 가치를 설명하고, '월 임대료 300만 원 수준'이라는 비용 정보도 전달하세요. 베트남 근로자들이 리프트 탑승 경험이 적을 수 있으므로, '탑승 전 안전교육 1시간 필수'를 강조하세요.",
        "commonMistakes": [
            {
                "mistake": "thang máy (엘리베이터)",
                "correction": "thang máy xây dựng (건설용 리프트)",
                "explanation": "thang máy는 일반 엘리베이터이며, 건설 현장용은 xây dựng을 붙여야 합니다."
            },
            {
                "mistake": "cần cẩu (크레인)",
                "correction": "thang máy xây dựng (리프트)",
                "explanation": "크레인은 자재만 옮기지만, 리프트는 사람도 탈 수 있는 승강기입니다."
            },
            {
                "mistake": "'리프트 타다' → đi thang máy xây dựng",
                "correction": "'리프트 탑승하다' → lên thang máy xây dựng",
                "explanation": "엘리베이터는 '타는(đi)' 표현이 가능하지만, 리프트는 '오르는(lên)' 표현이 더 정확합니다."
            }
        ],
        "examples": [
            {
                "ko": "15층까지 자재를 나르려면 리프트가 필수입니다.",
                "vi": "Để vận chuyển vật liệu lên tầng 15 thì bắt buộc phải có thang máy xây dựng.",
                "situation": "onsite"
            },
            {
                "ko": "리프트 정원은 8명이므로 초과 탑승을 금지합니다.",
                "vi": "Sức chứa thang máy xây dựng là 8 người, nghiêm cấm vượt quá.",
                "situation": "formal"
            },
            {
                "ko": "리프트 없으면 계단으로 15층까지 올라가야 해서 힘들어요.",
                "vi": "Không có thang máy xây dựng thì phải leo cầu thang lên tầng 15, mệt lắm.",
                "situation": "informal"
            }
        ],
        "relatedTerms": [
            "곤돌라",
            "크레인",
            "낙하방지장치",
            "적재하중",
            "승강기"
        ]
    },
    {
        "slug": "gondola",
        "korean": "곤돌라",
        "vietnamese": "Gondola",
        "hanja": None,
        "hanjaReading": None,
        "pronunciation": "곤돌라",
        "meaningKo": "건물 지붕에 설치된 레일을 따라 이동하며 외벽 작업을 하는 승강 작업대로, 유리 청소·외벽 도장·고층 보수에 사용됩니다. 통역 시 'gondola'는 외래어 그대로 사용하며, '레일 이동식 달비계'임을 설명하세요. 베트남에서도 gondola로 통용되지만, 일부 현장에서는 giàn treo di động(이동식 매달린 비계)으로 부르기도 합니다. 곤돌라 정원(2~4명), 최대 적재 하중(250kg), 이동 속도(10m/분) 등을 통역할 때는 수치를 명확히 전달하세요. '곤돌라는 강풍 시(풍속 10m/s 이상) 작업 중지'라는 안전 수칙과, '탑승 전 안전대 착용 확인'을 강조하세요.",
        "meaningVi": "Sàn làm việc treo di chuyển theo ray trên mái nhà, dùng lau kính, sơn tường ngoài, bảo trì công trình cao tầng. Sức chứa 2-4 người, tải trọng tối đa 250kg, tốc độ di chuyển 10m/phút. Dừng làm việc khi gió trên 10m/s. Bắt buộc đeo dây an toàn trước khi lên.",
        "context": "고층건물, 외벽유지보수",
        "culturalNote": "한국에서는 50층 이상 초고층 건물에 곤돌라를 설치하지만, 베트남에서는 비용 문제로 달비계나 크레인을 선호합니다. 통역 시 '곤돌라는 장기 보수 작업에 경제적'이라는 점을 설명하고, '초기 설치비 2억 원, 월 유지비 50만 원'이라는 비용 정보도 전달하세요. 베트남 근로자들이 곤돌라 조작 경험이 적을 수 있으므로, '조작 교육 1일 + 자격증 필수'를 강조하세요.",
        "commonMistakes": [
            {
                "mistake": "giàn treo (달비계)",
                "correction": "gondola (곤돌라)",
                "explanation": "달비계는 고정형이지만, 곤돌라는 레일을 따라 이동 가능합니다."
            },
            {
                "mistake": "thang máy bên ngoài (외부 엘리베이터)",
                "correction": "gondola (곤돌라)",
                "explanation": "엘리베이터는 수직 이동만 가능하지만, 곤돌라는 수평·수직 이동이 모두 가능합니다."
            },
            {
                "mistake": "'곤돌라 타다' → đi gondola",
                "correction": "'곤돌라 탑승하다' → lên gondola",
                "explanation": "곤돌라는 '타는(đi)' 것이 아니라 '오르는(lên)' 작업 공간입니다."
            }
        ],
        "examples": [
            {
                "ko": "50층 유리 청소를 위해 곤돌라를 운행하겠습니다.",
                "vi": "Chúng tôi sẽ vận hành gondola để lau kính tầng 50.",
                "situation": "onsite"
            },
            {
                "ko": "곤돌라 작업 시 안전대를 반드시 착용하고 이동하세요.",
                "vi": "Khi làm việc trên gondola, bắt buộc phải đeo dây an toàn khi di chuyển.",
                "situation": "formal"
            },
            {
                "ko": "곤돌라는 바람 세면 흔들려서 무섭지만, 안전장치가 있어서 괜찮아요.",
                "vi": "Gondola lung lay khi gió mạnh nên sợ, nhưng có thiết bị an toàn nên không sao.",
                "situation": "informal"
            }
        ],
        "relatedTerms": [
            "달비계",
            "레일",
            "외벽청소",
            "고층보수",
            "승강작업대"
        ]
    },
    {
        "slug": "san-lam-viec",
        "korean": "작업발판",
        "vietnamese": "Sàn làm việc",
        "hanja": "作業발판",
        "hanjaReading": "作(지을 작) + 業(업 업) + 발판(순우리말)",
        "pronunciation": "작업발판",
        "meaningKo": "비계 위에서 근로자가 서서 작업하는 평평한 판으로, 안전한 작업 공간을 제공합니다. 통역 시 '발판'은 단순 '판(bảng)'이 아닌 '작업 공간(sàn làm việc)'임을 강조하세요. 베트남에서는 sàn giàn giáo(비계 바닥)로도 부르지만, 정확한 용어는 sàn làm việc입니다. 발판 폭(40cm 이상), 두께(3.8cm 이상), 재질(강재·합판·알루미늄) 등을 통역할 때는 규격을 명확히 전달하세요. '발판 틈새는 3cm 이하, 고정 필수'라는 안전 기준과, '파손된 발판 즉시 교체'를 강조하세요. 발판이 미끄러우면 추락 위험이 크므로 '빗물·기름 제거 필수'도 전달해야 합니다.",
        "meaningVi": "Tấm phẳng trên giàn giáo để công nhân đứng làm việc, tạo không gian an toàn. Độ rộng tối thiểu 40cm, dày 3.8cm, chất liệu thép/ván ép/nhôm. Khe hở giữa các tấm không quá 3cm, phải cố định chắc chắn. Tấm bị hỏng phải thay ngay. Không để nước mưa, dầu mỡ làm trơn.",
        "context": "비계작업, 고소작업",
        "culturalNote": "한국에서는 철재 발판(thép)을 표준으로 쓰지만, 베트남 중소 현장에서는 합판(ván ép)이나 대나무(tre)를 쓰는 경우가 많습니다. 통역 시 '합판·대나무 발판은 내구성이 약해 안전사고 위험'이라는 점을 강조하고, '철재 발판 의무 사용'을 전달하세요. 베트남 근로자들이 발판 고정 방법을 모를 수 있으므로, '결속선(철사) 사용법 교육'도 필요합니다.",
        "commonMistakes": [
            {
                "mistake": "bảng gỗ (나무 판)",
                "correction": "sàn làm việc (작업발판)",
                "explanation": "bảng는 단순 '판'을 의미하며, 작업발판은 sàn(바닥) + làm việc(작업)으로 표현해야 합니다."
            },
            {
                "mistake": "sàn giàn giáo (비계 바닥)",
                "correction": "sàn làm việc (작업발판)",
                "explanation": "일반적으로 sàn giàn giáo로 불리지만, 전문 용어는 sàn làm việc이 정확합니다."
            },
            {
                "mistake": "'발판 깔다' → đặt sàn làm việc",
                "correction": "'발판 설치하다' → lắp sàn làm việc",
                "explanation": "발판은 '깔다(đặt)'가 아니라 '설치(lắp)'해야 고정된 상태를 나타냅니다."
            }
        ],
        "examples": [
            {
                "ko": "작업발판을 40cm 폭으로 설치하고 고정해 주세요.",
                "vi": "Vui lòng lắp sàn làm việc rộng 40cm và cố định chắc chắn.",
                "situation": "onsite"
            },
            {
                "ko": "작업발판이 젖으면 미끄러워서 위험하니 물기를 제거하세요.",
                "vi": "Sàn làm việc ướt rất trơn và nguy hiểm, hãy lau khô.",
                "situation": "formal"
            },
            {
                "ko": "이 발판 금이 갔네요. 새 걸로 바꿔야겠어요.",
                "vi": "Tấm sàn này bị nứt rồi, phải thay cái mới.",
                "situation": "informal"
            }
        ],
        "relatedTerms": [
            "비계",
            "안전난간",
            "고정철물",
            "미끄럼방지",
            "추락방지"
        ]
    },
    {
        "slug": "day-an-toan",
        "korean": "안전대",
        "vietnamese": "Dây an toàn",
        "hanja": "安全帶",
        "hanjaReading": "安(편안할 안) + 全(온전할 전) + 帶(띠 대)",
        "pronunciation": "안전대",
        "meaningKo": "고소 작업 시 추락을 방지하기 위해 몸에 착용하는 띠 형태의 안전장비로, 하네스(harness) 형태가 표준입니다. 통역 시 '안전대'는 'safety belt'가 아닌 'safety harness(안전 하네스)'임을 강조하세요. 베트남에서는 dây an toàn(안전끈)으로 통용되지만, 허리만 묶는 구형 벨트(đai lưng)와 구별해야 합니다. 안전대 종류(1종: 추락방지대, 2종: 안전그네), 착용법(어깨·가슴·허벅지 고정), 체결 고리(D-ring) 위치 등을 통역할 때는 실물을 보여주며 설명하세요. '안전대는 2m 이상 고소작업 시 필수'이며, '생명줄과 함께 사용'해야 한다는 점을 강조하세요. '안전대 착용 확인은 작업 시작 전 의무'라는 규정도 전달해야 합니다.",
        "meaningVi": "Dây đai mang trên người để chống rơi khi làm việc trên cao, dạng harness (dây đai toàn thân) là tiêu chuẩn. Khác với đai lưng (chỉ buộc eo), dây an toàn phải cố định ở vai, ngực, đùi. Bắt buộc dùng khi làm việc trên 2m, kết hợp với dây cứu sinh. Kiểm tra trước khi bắt đầu thi công.",
        "context": "고소작업, 안전관리",
        "culturalNote": "한국에서는 2000년대 이후 전신형 안전대(harness)가 의무화되었지만, 베트남 일부 현장에서는 여전히 허리만 묶는 구형 벨트를 사용합니다. 통역 시 '구형 벨트는 추락 시 내장 파열 위험'이라는 안전 경고를 전달하고, '전신형 안전대 의무 착용'을 강조하세요. 베트남 근로자들이 안전대 착용을 불편해할 수 있으므로, '착용법 교육 + 첫 1주일 감독'이 필요합니다.",
        "commonMistakes": [
            {
                "mistake": "đai lưng (허리 벨트)",
                "correction": "dây an toàn (안전대)",
                "explanation": "đai lưng는 구형 허리 벨트이며, 현대 안전대는 전신형 dây an toàn입니다."
            },
            {
                "mistake": "dây đeo (끈)",
                "correction": "dây an toàn (안전대)",
                "explanation": "dây đeo는 일반 '끈'을 의미하며, 안전장비는 dây an toàn으로 표현해야 합니다."
            },
            {
                "mistake": "'안전대 매다' → buộc dây an toàn",
                "correction": "'안전대 착용하다' → mặc dây an toàn",
                "explanation": "안전대는 '묶는(buộc)' 것이 아니라 '입는(mặc)' 형태로 착용합니다."
            }
        ],
        "examples": [
            {
                "ko": "작업 시작 전에 안전대 착용 여부를 반드시 확인하세요.",
                "vi": "Trước khi bắt đầu thi công, bắt buộc phải kiểm tra việc mặc dây an toàn.",
                "situation": "onsite"
            },
            {
                "ko": "안전대는 전신형을 사용하며, 허리만 묶는 구형은 금지입니다.",
                "vi": "Sử dụng dây an toàn toàn thân, nghiêm cấm dùng loại chỉ buộc eo.",
                "situation": "formal"
            },
            {
                "ko": "안전대 안 매면 벌금 10만 원이니까 꼭 착용하세요.",
                "vi": "Không đeo dây an toàn bị phạt 10 vạn won, nên phải mặc nhé.",
                "situation": "informal"
            }
        ],
        "relatedTerms": [
            "생명줄",
            "추락방지대",
            "D링",
            "하네스",
            "안전고리"
        ]
    },
    {
        "slug": "day-cuu-sinh-doc",
        "korean": "수직구명줄",
        "vietnamese": "Dây cứu sinh dọc",
        "hanja": "垂直救命줄",
        "hanjaReading": "垂(드리울 수) + 直(곧을 직) + 救(구할 구) + 命(목숨 명) + 줄(순우리말)",
        "pronunciation": "수직구명줄",
        "meaningKo": "고소 작업 시 추락 방지를 위해 수직으로 설치하는 생명줄로, 안전대와 함께 사용하여 추락 시 하강을 자동으로 멈춥니다. 통역 시 '구명줄'은 'lifeline'이며, 수직(dọc)과 수평(ngang)을 구별하여 전달하세요. 베트남에서는 dây cứu sinh(생명줄)로 통용되지만, 방향을 명시할 때는 dọc(수직)를 붙입니다. 구명줄 종류(로프식·레일식), 설치 높이(5m마다 지지점), 자동 잠김 장치(fall arrester) 등을 통역할 때는 도면과 실물을 함께 보여주세요. '구명줄은 안전대와 별도 설치'이며, '1인 1줄 원칙'을 강조하세요. '사용 전 장력 테스트 필수'라는 안전 점검 사항도 전달해야 합니다.",
        "meaningVi": "Dây cứu sinh lắp theo phương dọc để chống rơi khi làm việc trên cao, dùng kèm dây an toàn và tự động dừng khi có người rơi. Phân biệt dọc (vertical) và ngang (horizontal). Cứ 5m phải có điểm giữ, có thiết bị tự động khóa (fall arrester). Nguyên tắc 1 người 1 dây. Kiểm tra lực căng trước khi dùng.",
        "context": "고소작업, 추락방지",
        "culturalNote": "한국에서는 5m 이상 고소작업 시 수직구명줄 설치가 의무지만, 베트남 중소 현장에서는 비용 문제로 생략하는 경우가 많습니다. 통역 시 '구명줄 없이 작업하다 추락 시 형사 처벌'이라는 법적 책임을 강조하고, '임대비 일 5만 원'이라는 비용 정보도 전달하세요. 베트남 근로자들이 구명줄 사용법을 모를 수 있으므로, '착용 교육 1시간 필수'를 명시하세요.",
        "commonMistakes": [
            {
                "mistake": "dây thừng (밧줄)",
                "correction": "dây cứu sinh dọc (수직구명줄)",
                "explanation": "thừng은 일반 밧줄이며, 안전장비는 cứu sinh(생명) + dọc(수직)으로 표현해야 합니다."
            },
            {
                "mistake": "dây an toàn (안전대)",
                "correction": "dây cứu sinh dọc (수직구명줄)",
                "explanation": "안전대(dây an toàn)는 몸에 착용하는 것이고, 구명줄(dây cứu sinh)은 수직으로 설치하는 것입니다."
            },
            {
                "mistake": "'구명줄 설치' → lắp đặt dây cứu sinh",
                "correction": "'구명줄 설치' → giăng dây cứu sinh dọc",
                "explanation": "구명줄은 '설치(lắp đặt)'보다 '펼치다(giăng)'가 더 정확한 동사입니다."
            }
        ],
        "examples": [
            {
                "ko": "10m 높이 작업이므로 수직구명줄을 반드시 설치하세요.",
                "vi": "Làm việc ở độ cao 10m nên bắt buộc phải giăng dây cứu sinh dọc.",
                "situation": "onsite"
            },
            {
                "ko": "수직구명줄은 5m마다 지지점을 확보하고, 자동 잠김 장치를 확인하세요.",
                "vi": "Dây cứu sinh dọc phải có điểm giữ mỗi 5m và kiểm tra thiết bị tự động khóa.",
                "situation": "formal"
            },
            {
                "ko": "구명줄 없이 작업하다 걸리면 벌금 맞으니까 꼭 설치해요.",
                "vi": "Làm việc không có dây cứu sinh bị phạt nặng, nên phải giăng nhé.",
                "situation": "informal"
            }
        ],
        "relatedTerms": [
            "수평구명줄",
            "안전대",
            "추락방지대",
            "자동잠김장치",
            "생명줄"
        ]
    },
    {
        "slug": "day-cuu-sinh-ngang",
        "korean": "수평구명줄",
        "vietnamese": "Dây cứu sinh ngang",
        "hanja": "水平救命줄",
        "hanjaReading": "水(물 수) + 平(평평할 평) + 救(구할 구) + 命(목숨 명) + 줄(순우리말)",
        "pronunciation": "수평구명줄",
        "meaningKo": "고소 작업 시 작업자가 수평으로 이동하며 작업할 수 있도록 수평으로 설치하는 생명줄로, 안전대와 연결하여 추락을 방지합니다. 통역 시 '수평구명줄'은 '수평 이동용 생명줄(horizontal lifeline)'이며, 수직구명줄과의 차이(이동 방향)를 명확히 설명하세요. 베트남에서는 dây cứu sinh ngang(수평 생명줄)으로 표현하며, 옥상·지붕·외벽 작업 시 필수입니다. 구명줄 장력(1,000kgf 이상), 설치 간격(10m마다 지지점), 슬라이더(이동 고리) 사용법 등을 통역할 때는 실물과 도면을 함께 보여주세요. '수평구명줄은 여러 명이 동시 사용 가능하지만, 장력 테스트 후 사용'을 강조하고, '바람에 흔들리지 않도록 중간 고정'도 전달하세요.",
        "meaningVi": "Dây cứu sinh lắp theo phương ngang để công nhân di chuyển ngang khi làm việc trên cao, kết nối với dây an toàn để chống rơi. Khác với dây cứu sinh dọc (di chuyển dọc), dây ngang cho phép nhiều người cùng làm việc. Lực căng tối thiểu 1,000kgf, mỗi 10m có điểm giữ, dùng slider (khoen trượt). Kiểm tra lực căng trước khi dùng, cố định giữa để không bị gió lay.",
        "context": "옥상작업, 지붕작업",
        "culturalNote": "한국에서는 옥상·지붕 작업 시 수평구명줄 설치가 의무지만, 베트남 일부 현장에서는 단순 안전대만 착용하고 고정점 없이 작업하는 경우가 많습니다. 통역 시 '고정점 없는 안전대는 추락 시 무용지물'이라는 안전 경고를 전달하고, '수평구명줄 설치 의무'를 강조하세요. 베트남 근로자들이 슬라이더 사용법을 모를 수 있으므로, '이동 고리 사용 교육 30분 필수'를 명시하세요.",
        "commonMistakes": [
            {
                "mistake": "dây thừng ngang (수평 밧줄)",
                "correction": "dây cứu sinh ngang (수평구명줄)",
                "explanation": "thừng은 일반 밧줄이며, 안전장비는 cứu sinh(생명) + ngang(수평)으로 표현해야 합니다."
            },
            {
                "mistake": "dây cứu sinh (구명줄)",
                "correction": "dây cứu sinh ngang (수평구명줄)",
                "explanation": "방향을 명시하지 않으면 수직/수평 구분이 안 되므로 ngang(수평)을 반드시 붙여야 합니다."
            },
            {
                "mistake": "'수평구명줄 설치' → lắp đặt dây cứu sinh ngang",
                "correction": "'수평구명줄 설치' → giăng dây cứu sinh ngang",
                "explanation": "구명줄은 '설치(lắp đặt)'보다 '펼치다(giăng)'가 더 정확한 동사입니다."
            }
        ],
        "examples": [
            {
                "ko": "옥상 방수 작업을 위해 수평구명줄을 10m 간격으로 설치하세요.",
                "vi": "Để thi công chống thấm mái, hãy giăng dây cứu sinh ngang cách nhau 10m.",
                "situation": "onsite"
            },
            {
                "ko": "수평구명줄은 장력 테스트 후 사용하며, 슬라이더로 이동하세요.",
                "vi": "Kiểm tra lực căng dây cứu sinh ngang trước khi dùng, di chuyển bằng slider.",
                "situation": "formal"
            },
            {
                "ko": "수평구명줄 있으면 지붕 위에서 자유롭게 움직일 수 있어서 편해요.",
                "vi": "Có dây cứu sinh ngang thì di chuyển tự do trên mái, tiện lắm.",
                "situation": "informal"
            }
        ],
        "relatedTerms": [
            "수직구명줄",
            "안전대",
            "슬라이더",
            "옥상작업",
            "지붕작업"
        ]
    }
]

# 저장 경로
target_file = os.path.join(
    os.path.dirname(os.path.dirname(__file__)),
    "data", "terms", "construction.json"
)

# 기존 데이터 로드
with open(target_file, "r", encoding="utf-8") as f:
    existing_data = json.load(f)

# 기존 slug 목록
existing_slugs = {term["slug"] for term in existing_data}

# 중복 제거 후 추가
new_terms = [term for term in data if term["slug"] not in existing_slugs]
existing_data.extend(new_terms)

# 저장 (들여쓰기 2칸, 한글 유지)
with open(target_file, "w", encoding="utf-8") as f:
    json.dump(existing_data, f, ensure_ascii=False, indent=2)

print(f"✅ {len(new_terms)}개 용어 추가 완료 (중복 {len(data) - len(new_terms)}개 제외)")
print(f"📂 저장 위치: {target_file}")
print(f"📊 전체 용어 수: {len(existing_data)}개")
