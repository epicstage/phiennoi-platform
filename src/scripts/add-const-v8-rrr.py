#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
건설 용어 추가 스크립트 - 배수/우수처리 테마
U형측구, L형측구, 집수정, 트렌치, 투수블록, 저류조, 침투시설, 우수관거, 합류식, 분류식
"""

import json
import os

# 배수/우수처리 테마 용어 10개 (Tier S 기준)
data = [
    {
        "slug": "cong-u",
        "korean": "U형측구",
        "vietnamese": "cống U",
        "hanja": None,
        "hanjaReading": None,
        "pronunciation": "꽁 우",
        "meaningKo": "도로 양측에 설치하는 배수로의 일종으로, 단면이 U자 형태를 띠는 프리캐스트 콘크리트 측구입니다. 빗물을 집수하여 하수관거나 집수정으로 유도하는 역할을 하며, 표면 배수 시스템의 핵심 요소입니다. 통역 시 'U형측구'는 단순히 '배수로(rãnh thoát nước)'가 아닌 'cống U' 또는 'rãnh chữ U bê tông đúc sẵn'으로 명확히 표현해야 합니다. L형측구와 혼동되기 쉬우므로 단면 형태를 설명할 때 주의가 필요하며, 설치 깊이, 경사, 그레이팅(격자 뚜껑) 유무 등을 함께 전달해야 합니다. 한국 도로공사 표준시방서에서는 KCS 44 50 20(도로 배수시설)을 따르며, 측구 규격은 폭 300~600mm, 깊이 200~400mm가 일반적입니다.",
        "meaningVi": "Cống U (rãnh chữ U) là loại rãnh thoát nước lắp đặt hai bên đường, có tiết diện hình chữ U bằng bê tông đúc sẵn. Nhiệm vụ thu nước mưa và dẫn vào hệ thống cống thoát nước hoặc hố ga. Kích thước phổ biến: rộng 300~600mm, sâu 200~400mm.",
        "context": "도로공사, 배수설계, 토목시공",
        "culturalNote": "한국은 U형측구를 공장제작 프리캐스트로 납품받아 현장에서 연결 시공하는 방식이 표준이며, 이음부 방수 처리를 엄격히 관리합니다. 측구 상부에 그레이팅을 설치하여 보행자 안전과 차량 통행을 고려합니다. 베트남은 현장 타설(cast-in-place) 방식이 많고, 프리캐스트를 사용하더라도 이음부 처리가 미흡하여 누수가 발생하기 쉽습니다. 그레이팅 대신 콘크리트 덮개를 사용하는 경우도 많습니다. 한국 감리는 측구 기울기, 이음부 밀실성, 그레이팅 고정 상태를 세밀히 확인하지만, 베트남 현장은 육안 검수만 하는 경우가 많아 통역 시 검수 기준을 명확히 전달해야 합니다.",
        "commonMistakes": [
            {
                "mistake": "'U형측구'를 단순히 'rãnh thoát nước'(배수로)로 번역",
                "correction": "'cống U' 또는 'rãnh chữ U bê tông đúc sẵn' 사용",
                "explanation": "베트남 기술자는 'cống U'로 U자 단면 프리캐스트 측구를 정확히 인식함"
            },
            {
                "mistake": "'측구'와 'L형측구'를 구분 없이 번역",
                "correction": "U형은 'cống U', L형은 'cống L' 또는 'rãnh chữ L'로 명확히 구분",
                "explanation": "단면 형태와 설치 방법이 다르므로 혼동 시 시공 오류 발생"
            },
            {
                "mistake": "'그레이팅'을 'nắp đậy'(덮개)로 일반화",
                "correction": "'song chắn' 또는 'tấm song sắt/thép' 사용",
                "explanation": "그레이팅은 격자형 철제/강재 덮개로, 콘크리트 덮개와 구조가 다름"
            }
        ],
        "examples": [
            {
                "ko": "U형측구를 300mm 간격으로 설치하고, 이음부에 지수재를 충전하세요.",
                "vi": "Lắp cống U với khoảng cách 300mm, và điền vật liệu chống thấm vào mối nối.",
                "situation": "onsite"
            },
            {
                "ko": "U형측구 위에 그레이팅을 설치하여 보행자 안전을 확보합니다.",
                "vi": "Lắp song chắn trên cống U để đảm bảo an toàn cho người đi bộ.",
                "situation": "formal"
            },
            {
                "ko": "측구 기울기가 0.5%로 충분한지 확인해야 합니다.",
                "vi": "Cần kiểm tra xem độ dốc cống 0.5% có đủ không.",
                "situation": "formal"
            }
        ],
        "relatedTerms": [
            "L형측구",
            "집수정",
            "그레이팅",
            "배수로",
            "이음부"
        ]
    },
    {
        "slug": "cong-l",
        "korean": "L형측구",
        "vietnamese": "cống L",
        "hanja": None,
        "hanjaReading": None,
        "pronunciation": "꽁 엘",
        "meaningKo": "도로 가장자리에 설치하는 측구로, 단면이 L자 형태를 띠며 한쪽 면이 연석(kerb) 역할을 겸하는 구조입니다. U형측구와 달리 수직면과 수평면이 직각으로 만나며, 보도와 차도의 경계 역할도 수행합니다. 통역 시 'L형측구'는 'cống L' 또는 'rãnh chữ L kiêm lề đường'으로 표현하며, 연석 기능을 강조해야 합니다. L형측구는 프리캐스트 제품으로 공급되며, 설치 시 수평 정렬과 높이 조정이 중요합니다. 한국 표준품은 폭 250~350mm, 높이 120~150mm이며, 강도는 최소 21MPa(210kgf/cm²) 이상이어야 합니다. 도로공사 표준시방서 KCS 44 50 20에 따라 시공하며, 차도와의 높이 차는 보통 100~150mm입니다.",
        "meaningVi": "Cống L (rãnh chữ L) là loại rãnh thoát nước lắp ở rìa đường, có tiết diện hình chữ L với mặt đứng kiêm lề đường (kerb). Khác với cống U, cống L có mặt đứng và mặt nằm giao nhau vuông góc, vừa thoát nước vừa phân chia lòng đường và vỉa hè. Kích thước phổ biến: rộng 250~350mm, cao 120~150mm.",
        "context": "도로공사, 배수설계, 포장공사",
        "culturalNote": "한국은 L형측구를 보도와 차도 경계에 설치하며, 시각장애인용 점자블록, 볼라드(bollard) 등과 연계하여 종합적인 보행 안전 시스템을 구축합니다. 측구 상단은 차량 하중을 고려하여 설계하며, 결빙 방지를 위해 배수구 간격을 좁게 설정합니다. 베트남은 L형측구보다 U형측구를 선호하며, L형측구를 사용하더라도 연석과 측구를 별도로 시공하는 경우가 많습니다. 한국식 일체형 L형측구는 시공 속도가 빠르고 이음부가 적어 누수 위험이 낮지만, 베트남 현장은 이러한 장점을 잘 모르는 경우가 많아 통역 시 공법 설명이 중요합니다.",
        "commonMistakes": [
            {
                "mistake": "'L형측구'를 'rãnh chữ L'로만 번역하고 연석 기능을 누락",
                "correction": "'cống L kiêm lề đường' 또는 'rãnh chữ L kết hợp viền đá'로 표현",
                "explanation": "L형측구는 배수와 경계석 기능을 동시에 수행하는 구조물"
            },
            {
                "mistake": "'연석'을 'viền đá'(돌 경계)로만 번역",
                "correction": "'lề đường'(kerb, kerbstone) 사용 권장",
                "explanation": "베트남에서는 'lề đường'이 도로 연석을 지칭하는 표준 용어"
            },
            {
                "mistake": "L형측구와 U형측구의 차이를 설명하지 않고 번역",
                "correction": "단면 형태, 설치 위치, 기능 차이를 명확히 전달",
                "explanation": "두 측구의 용도와 시공법이 다르므로 혼동 시 설계 오류 발생"
            }
        ],
        "examples": [
            {
                "ko": "L형측구를 차도 경계에 설치하여 연석 역할을 겸하도록 합니다.",
                "vi": "Lắp cống L ở biên lòng đường để kiêm vai trò lề đường.",
                "situation": "formal"
            },
            {
                "ko": "L형측구 높이를 GL+150mm로 맞추고, 수평 정렬을 확인하세요.",
                "vi": "Điều chỉnh độ cao cống L đến GL+150mm và kiểm tra độ thẳng ngang.",
                "situation": "onsite"
            },
            {
                "ko": "L형측구는 U형보다 시공이 간편하고 보행자 안전에 유리합니다.",
                "vi": "Cống L thi công đơn giản hơn cống U và có lợi cho an toàn người đi bộ.",
                "situation": "formal"
            }
        ],
        "relatedTerms": [
            "U형측구",
            "연석",
            "보도",
            "차도",
            "배수로"
        ]
    },
    {
        "slug": "ho-thu-nuoc",
        "korean": "집수정",
        "vietnamese": "hố thu nước",
        "hanja": "集水井",
        "hanjaReading": "집(모을 집) + 수(물 수) + 정(우물 정)",
        "pronunciation": "호 투 늑",
        "meaningKo": "도로나 부지 내 빗물을 모아 하수관거로 유입시키는 지하 구조물로, 측구·배수로에서 흘러온 물을 집수하는 중간 시설입니다. 통역 시 '집수정'은 'hố thu nước' 또는 'hố ga thu nước'로 표현하며, '맨홀(manhole)'과 구분해야 합니다. 맨홀은 점검·유지보수용 출입구이고, 집수정은 배수 기능이 주목적입니다. 집수정은 크게 우수용(빗물)과 오수용(생활하수)으로 구분되며, 한국에서는 합류식과 분류식 하수도 시스템에 따라 설치 기준이 다릅니다. 표준 규격은 직경 600mm~1200mm이며, 바닥에 토사 침전을 위한 집수정 바닥(sump)을 설치하여 관거 막힘을 방지합니다. 상부는 맨홀 뚜껑(manhole cover)으로 덮으며, 차량 하중을 고려하여 강도를 선정합니다.",
        "meaningVi": "Hố thu nước (hố ga thu nước) là cấu trúc ngầm thu nước mưa từ đường, rãnh thoát nước và dẫn vào hệ thống cống thoát nước. Khác với manhole (hố ga kiểm tra), hố thu nước có mục đích chính là thoát nước, không phải kiểm tra. Đường kính phổ biến 600mm~1200mm, đáy có hố lắng (sump) để ngăn bùn cát.",
        "context": "도로공사, 배수설계, 하수도공사",
        "culturalNote": "한국은 집수정을 프리캐스트 제품으로 공급받아 설치하며, 바닥 슬래브, 몸체(shaft), 맨홀 뚜껑이 일체형 또는 조립식으로 구성됩니다. 집수정 내부에는 방충망(insect screen)과 침전조를 의무 설치하며, 악취 방지를 위해 트랩(trap) 구조를 적용하기도 합니다. 유지관리 편의를 위해 집수정 위치를 도면에 명확히 표시하고, GPS 좌표를 기록합니다. 베트남은 집수정을 현장 타설로 시공하는 경우가 많고, 바닥 침전조나 방충망 설치를 생략하는 경우가 흔합니다. 맨홀 뚜껑도 강도가 낮은 콘크리트 제품을 사용하여 파손이 잦습니다. 한국 감리는 집수정 내부 마감, 이음부 방수, 뚜껑 고정 상태를 세밀히 검수하지만, 베트남은 설치 여부만 확인하는 경우가 많아 통역 시 검수 항목을 구체적으로 전달해야 합니다.",
        "commonMistakes": [
            {
                "mistake": "'집수정'을 'hố ga'(맨홀)로만 번역",
                "correction": "'hố thu nước' 또는 'hố ga thu nước' 사용",
                "explanation": "맨홀은 점검용, 집수정은 배수용으로 목적이 다름"
            },
            {
                "mistake": "'침전조'를 'bể lắng'(침전지)로 번역",
                "correction": "'hố lắng' 또는 'phần đáy lắng cặn' 사용",
                "explanation": "집수정 내부의 작은 침전 공간은 'bể lắng'(대규모 침전지)와 구분"
            },
            {
                "mistake": "'맨홀 뚜껑'을 'nắp đậy'(일반 뚜껑)로 번역",
                "correction": "'nắp hố ga' 또는 'nắp gang cầu' 사용",
                "explanation": "맨홀 뚜껑은 차량 하중을 견디는 주철제 또는 강재 뚜껑"
            }
        ],
        "examples": [
            {
                "ko": "집수정을 50m 간격으로 설치하여 우수를 집수하세요.",
                "vi": "Lắp hố thu nước mỗi 50m để thu nước mưa.",
                "situation": "onsite"
            },
            {
                "ko": "집수정 바닥에 침전조를 설치하여 토사가 관거로 유입되는 것을 방지합니다.",
                "vi": "Lắp hố lắng cặn ở đáy hố thu nước để ngăn bùn cát chảy vào cống.",
                "situation": "formal"
            },
            {
                "ko": "집수정 뚜껑이 파손되었으니 교체가 필요합니다.",
                "vi": "Nắp hố ga bị hỏng nên cần thay mới.",
                "situation": "informal"
            }
        ],
        "relatedTerms": [
            "맨홀",
            "우수관거",
            "오수관거",
            "침전조",
            "배수로"
        ]
    },
    {
        "slug": "ranh-trench",
        "korean": "트렌치",
        "vietnamese": "rãnh trench",
        "hanja": None,
        "hanjaReading": None,
        "pronunciation": "자인 트렌치",
        "meaningKo": "선형 배수로(linear drainage)의 일종으로, 좁고 긴 형태의 배수 채널에 그레이팅을 덮어 빗물을 신속히 배수하는 시스템입니다. 'trench'는 영어 외래어로, 한국어로는 '트렌치 배수로', '슬롯 배수로', '선형 배수로'로 불립니다. 통역 시 'rãnh trench' 또는 'rãnh thoát nước dạng khe'로 표현하며, 일반 U형측구보다 집수 능력이 뛰어나고 미관이 우수한 고급 배수 시스템임을 강조해야 합니다. 트렌치는 공항, 쇼핑몰, 광장, 고속도로 휴게소 등 넓은 포장면에서 집중 호우 시 급속 배수가 필요한 곳에 설치됩니다. 폭은 100~200mm로 좁고, 길이는 1~2m 모듈로 연결하여 필요한 길이만큼 확장 가능합니다. 상부 그레이팅은 스테인리스, 주철, 플라스틱 등 다양하며, 차량 하중 등급(A15~E600)에 따라 선정합니다.",
        "meaningVi": "Rãnh trench (rãnh thoát nước dạng khe) là hệ thống thoát nước tuyến tính, có dạng kênh hẹp dài phủ song chắn để thoát nước mưa nhanh. Trench có khả năng thu nước tốt hơn cống U và thẩm mỹ cao, thường lắp ở sân bay, trung tâm thương mại, quảng trường. Rộng 100~200mm, dài theo module 1~2m có thể nối thêm.",
        "context": "배수설계, 포장공사, 조경공사",
        "culturalNote": "한국은 트렌치 배수로를 고급 건축물, 공공시설, 주차장 진출입구에 적극 도입하며, 디자인 그레이팅(무늬, 색상, 로고 각인)을 적용하여 건축 미관과 조화를 이룹니다. 트렌치는 폴리머 콘크리트(polymer concrete) 또는 스테인리스 재질로 제작되며, 내구성과 내부식성이 뛰어납니다. 베트남은 트렌치 배수로 개념이 낯설고, 대부분 U형측구나 일반 배수로를 사용합니다. 트렌치를 도입하더라도 그레이팅이 약하거나 고정이 불량하여 도난·파손 위험이 높습니다. 한국 설계자가 트렌치를 지정하면 베트남 시공사는 '비싸다', '유지관리 어렵다'는 이유로 대체안을 요구하는 경우가 많아, 통역 시 트렌치의 장점(급속 배수, 미관, 청소 편의)을 설득력 있게 전달해야 합니다.",
        "commonMistakes": [
            {
                "mistake": "'트렌치'를 'rãnh hở'(개방 배수로)로 번역",
                "correction": "'rãnh trench' 또는 'rãnh thoát nước tuyến tính' 사용",
                "explanation": "트렌치는 선형 배수로(linear drainage)의 고급 시스템으로, 일반 개방 배수로와 다름"
            },
            {
                "mistake": "'선형 배수로'를 'rãnh thẳng'(직선 배수로)로 직역",
                "correction": "'rãnh thoát nước dạng khe' 또는 'hệ thống thoát nước tuyến tính' 사용",
                "explanation": "선형 배수로는 좁고 긴 슬롯(khe) 형태를 강조하는 용어"
            },
            {
                "mistake": "차량 하중 등급을 설명 없이 'A15', 'E600'로만 표기",
                "correction": "'cấp tải trọng A15 (người đi bộ)', 'E600 (xe tải nặng)' 병기",
                "explanation": "베트남 기술자는 유럽 하중 등급(EN 1433)에 익숙하지 않음"
            }
        ],
        "examples": [
            {
                "ko": "주차장 진입로에 트렌치 배수로를 설치하여 빗물이 건물 내로 유입되지 않도록 합니다.",
                "vi": "Lắp rãnh trench ở lối vào bãi đỗ để ngăn nước mưa chảy vào tòa nhà.",
                "situation": "formal"
            },
            {
                "ko": "트렌치 그레이팅은 하중 등급 E600으로 지정하여 중차량 통행에 대비하세요.",
                "vi": "Chỉ định song chắn rãnh trench cấp tải trọng E600 để chịu được xe tải nặng.",
                "situation": "formal"
            },
            {
                "ko": "트렌치는 청소가 쉽고 낙엽이나 쓰레기를 빠르게 제거할 수 있어요.",
                "vi": "Rãnh trench dễ vệ sinh, nhanh chóng loại bỏ lá rụng và rác.",
                "situation": "informal"
            }
        ],
        "relatedTerms": [
            "선형배수로",
            "그레이팅",
            "U형측구",
            "슬롯배수로",
            "폴리머콘크리트"
        ]
    },
    {
        "slug": "gach-tham",
        "korean": "투수블록",
        "vietnamese": "gạch thấm",
        "hanja": "透水블록",
        "hanjaReading": "투(통할 투) + 수(물 수)",
        "pronunciation": "자익 탐",
        "meaningKo": "빗물을 지표면에서 지하로 침투시키는 기능을 가진 포장 블록으로, 블록 자체 또는 블록 사이 간격을 통해 물이 스며들도록 설계된 친환경 포장재입니다. 통역 시 '투수블록'은 'gạch thấm' 또는 'gạch thoát nước'으로 표현하며, 일반 콘크리트 블록과 명확히 구분해야 합니다. 투수블록은 크게 세 가지 유형이 있습니다: (1) 블록 자체가 다공성 재질로 물을 투과하는 '전면투수형', (2) 블록 사이 줄눈(joint)으로 물이 배수되는 '줄눈투수형', (3) 블록에 구멍(hole)을 뚫어 투수하는 '구멍형'입니다. 투수계수는 1×10⁻² cm/s 이상이어야 하며, 압축강도는 최소 20MPa(200kgf/cm²) 이상을 확보해야 합니다. 한국 환경부는 '저영향개발(LID, Low Impact Development)' 기법의 일환으로 투수블록 사용을 권장하며, 주차장, 보도, 광장, 공원에 적용이 확대되고 있습니다.",
        "meaningVi": "Gạch thấm (gạch thoát nước) là loại gạch lát có chức năng thấm nước mưa từ mặt đất xuống lòng đất, được thiết kế để nước thấm qua chính gạch hoặc khe hở giữa các viên gạch. Có 3 loại: toàn bộ thấm, thấm qua khe hở, thấm qua lỗ khoan. Hệ số thấm ≥1×10⁻² cm/s, cường độ nén ≥20MPa.",
        "context": "포장공사, 조경공사, LID 기법",
        "culturalNote": "한국은 투수블록을 '물순환 도시', '스펀지 도시(sponge city)' 조성의 핵심 기술로 간주하며, 정부 지원으로 보급이 확대되고 있습니다. 투수블록 하부에는 투수층(자갈, 쇄석), 필터층(모래), 저류층을 설치하여 물을 지하로 유도하고, 초과 유출수는 배수관으로 처리합니다. 블록 표면은 미끄럼 방지 가공을 하여 보행자 안전을 확보합니다. 베트남은 투수블록 개념이 생소하며, 일반 블록과 가격 차이로 인해 채택을 꺼립니다. 투수블록을 사용하더라도 하부 투수층을 생략하거나 다짐이 과도하여 투수 성능이 발휘되지 않는 경우가 많습니다. 한국 감리는 투수계수 현장 시험(투수시험)을 요구하지만, 베트남 현장은 시험 장비가 없어 육안 확인만 하는 경우가 대부분입니다. 통역 시 투수블록의 환경적·경제적 효과(우수 관거 부담 감소, 지하수 함양, 도시 열섬 완화)를 강조하여 설득해야 합니다.",
        "commonMistakes": [
            {
                "mistake": "'투수블록'을 'gạch lát'(포장 블록)으로만 번역",
                "correction": "'gạch thấm' 또는 'gạch thoát nước' 사용",
                "explanation": "일반 블록과 투수 기능을 명확히 구분해야 함"
            },
            {
                "mistake": "'투수계수'를 'hệ số dẫn nước'로 번역",
                "correction": "'hệ số thấm' 사용",
                "explanation": "투수계수(permeability)는 지반·재료의 물 통과 능력을 나타내는 용어"
            },
            {
                "mistake": "투수블록과 일반 블록의 차이를 설명하지 않고 번역",
                "correction": "투수 기능, 하부 투수층, LID 개념을 함께 설명",
                "explanation": "베트남 기술자는 투수블록의 구조와 목적을 잘 모르는 경우가 많음"
            }
        ],
        "examples": [
            {
                "ko": "주차장 포장을 투수블록으로 시공하여 빗물을 지하로 침투시키세요.",
                "vi": "Thi công lát bãi đỗ xe bằng gạch thấm để nước mưa thấm xuống đất.",
                "situation": "onsite"
            },
            {
                "ko": "투수블록 하부에 쇄석층 200mm, 모래층 50mm를 설치합니다.",
                "vi": "Dưới gạch thấm lắp lớp đá dăm 200mm, lớp cát 50mm.",
                "situation": "formal"
            },
            {
                "ko": "투수블록은 일반 블록보다 비싸지만, 우수 관거 비용을 줄일 수 있어요.",
                "vi": "Gạch thấm đắt hơn gạch thường nhưng tiết kiệm chi phí hệ thống cống thoát nước mưa.",
                "situation": "informal"
            }
        ],
        "relatedTerms": [
            "투수성포장",
            "LID",
            "저류조",
            "침투시설",
            "물순환"
        ]
    },
    {
        "slug": "be-chua",
        "korean": "저류조",
        "vietnamese": "bể chứa",
        "hanja": "貯留槽",
        "hanjaReading": "저(쌓을 저) + 류(머물 류) + 조(구유 조)",
        "pronunciation": "베 쭈어",
        "meaningKo": "빗물을 일시적으로 저장하여 홍수를 방지하고, 저장된 물을 서서히 방류하거나 재이용하는 지하 또는 지상 시설입니다. 통역 시 '저류조'는 'bể chứa nước mưa' 또는 'bể điều hòa nước mưa'로 표현하며, '저수조(water tank)'와 구분해야 합니다. 저수조는 음용수·소방수 등을 저장하는 시설이고, 저류조는 빗물을 임시 저장하는 우수 관리 시설입니다. 저류조는 크게 '저류형(detention)'과 '저류+침투형(infiltration)'으로 구분됩니다. 저류형은 빗물을 모아 천천히 방류하여 하류 하천의 홍수 부담을 줄이고, 저류+침투형은 바닥을 투수층으로 설계하여 빗물을 지하로 침투시켜 지하수를 함양합니다. 한국은 「빗물관리법」에 따라 일정 규모 이상 개발사업에 저류조 설치를 의무화하고 있으며, 용량은 개발면적×강우량×유출계수로 산정합니다. 저류조는 콘크리트 구조물, 플라스틱 모듈, 침투 트렌치 등 다양한 형태로 시공되며, 유지관리를 위해 침전조, 스크린, 점검구를 설치합니다.",
        "meaningVi": "Bể chứa nước mưa (bể điều hòa) là công trình tạm trữ nước mưa để phòng lũ, sau đó xả chậm hoặc tái sử dụng. Khác với bể chứa nước (water tank), bể chứa nước mưa là cơ sở quản lý nước mưa tạm thời. Có 2 loại: chỉ chứa, và chứa + thấm. Dung tích tính theo diện tích × lượng mưa × hệ số dòng chảy.",
        "context": "우수관리, 홍수방지, LID 기법",
        "culturalNote": "한국은 도시화로 인한 불투수면 증가와 집중호우 빈발로 저류조 설치가 확대되고 있으며, 아파트 단지, 공공시설, 산업단지에 대규모 저류조를 의무 설치합니다. 저류조 물을 조경용수, 청소용수, 화장실 용수로 재이용하는 사례도 늘고 있습니다. 저류조 용량은 설계 빈도(10년, 30년, 50년 빈도 강우)에 따라 산정하며, 펌프, 배수밸브, 수위계를 설치하여 자동 제어합니다. 베트남은 저류조 개념이 생소하고, 빗물을 즉시 배출하는 방식(직배수)을 선호합니다. 저류조를 설치하더라도 용량이 부족하거나 유지관리 부족으로 퇴적물이 쌓여 기능을 상실하는 경우가 많습니다. 한국 설계자가 저류조를 요구하면 베트남 시공사는 '땅을 낭비한다', '비용이 많이 든다'는 이유로 반발하는 경우가 있어, 통역 시 저류조의 홍수 방지 효과와 법적 의무를 명확히 전달해야 합니다.",
        "commonMistakes": [
            {
                "mistake": "'저류조'를 'bể chứa nước'(저수조)로 번역",
                "correction": "'bể chứa nước mưa' 또는 'bể điều hòa nước mưa' 사용",
                "explanation": "저수조(water tank)는 음용수 저장, 저류조는 빗물 임시 저장"
            },
            {
                "mistake": "'저류'와 '침투'를 구분하지 않고 번역",
                "correction": "'chứa'(저류), 'thấm'(침투)로 명확히 구분",
                "explanation": "저류는 물을 모으는 것, 침투는 물을 지하로 보내는 것"
            },
            {
                "mistake": "저류조 용량 산정 공식을 설명 없이 제시",
                "correction": "개발면적, 강우량, 유출계수 의미를 함께 설명",
                "explanation": "베트남 기술자는 유출계수(runoff coefficient) 개념에 익숙하지 않음"
            }
        ],
        "examples": [
            {
                "ko": "단지 지하에 1000㎥ 용량의 저류조를 설치하여 30년 빈도 강우에 대응합니다.",
                "vi": "Lắp bể chứa nước mưa 1000m³ dưới khu đất để ứng phó mưa tần suất 30 năm.",
                "situation": "formal"
            },
            {
                "ko": "저류조에 모인 빗물을 조경용수로 재이용하여 수도 요금을 절감하세요.",
                "vi": "Tái sử dụng nước mưa từ bể chứa làm nước tưới cây để tiết kiệm tiền nước.",
                "situation": "informal"
            },
            {
                "ko": "저류조 바닥을 투수층으로 설계하여 지하수 함양 효과를 높입니다.",
                "vi": "Thiết kế đáy bể chứa thành lớp thấm để tăng hiệu quả bổ cập nước ngầm.",
                "situation": "formal"
            }
        ],
        "relatedTerms": [
            "침투시설",
            "우수관거",
            "LID",
            "유출계수",
            "홍수방지"
        ]
    },
    {
        "slug": "cong-trinh-tham",
        "korean": "침투시설",
        "vietnamese": "công trình thấm",
        "hanja": "浸透施設",
        "hanjaReading": "침(젖을 침) + 투(통할 투) + 시(베풀 시) + 설(베풀 설)",
        "pronunciation": "꽁 찡 탐",
        "meaningKo": "빗물을 지표면에서 지하로 침투시켜 지하수를 함양하고 홍수를 방지하는 우수 관리 시설의 총칭입니다. 침투 트렌치(infiltration trench), 침투조(infiltration basin), 침투통(soakaway), 투수블록 등이 포함됩니다. 통역 시 '침투시설'은 'công trình thấm' 또는 'cơ sở thấm nước mưa'로 표현하며, '배수시설(thoát nước)'과 구분해야 합니다. 배수시설은 빗물을 외부로 배출하는 것이고, 침투시설은 빗물을 지하로 보내는 것입니다. 침투시설은 '저영향개발(LID)' 기법의 핵심 요소로, 도시화로 인한 불투수면 증가, 지하수 고갈, 하천 건천화 문제를 해결하기 위해 도입되었습니다. 한국은 「빗물관리법」에 따라 일정 규모 이상 개발사업에 침투시설 설치를 의무화하고 있으며, 침투 용량은 토양 투수계수, 지하수위, 강우 강도를 고려하여 산정합니다. 침투시설은 토양 조건(투수성 양호)에 따라 적용 가능 여부가 결정되므로, 사전에 현장투수시험을 실시하여 투수계수를 확인해야 합니다.",
        "meaningVi": "Công trình thấm (cơ sở thấm nước mưa) là tổng hợp các công trình đưa nước mưa từ mặt đất xuống lòng đất để bổ cập nước ngầm và phòng lũ. Bao gồm rãnh thấm, hố thấm, ống thấm, gạch thấm. Khác với công trình thoát nước (xả ra ngoài), công trình thấm đưa nước xuống đất. Dung tích tính theo hệ số thấm đất, mực nước ngầm, cường độ mưa.",
        "context": "우수관리, LID 기법, 지하수 함양",
        "culturalNote": "한국은 침투시설을 '물순환 회복', '스펀지 도시' 조성의 핵심 기술로 간주하며, 정부가 설치 비용을 보조하고 있습니다. 침투시설은 도시 열섬 완화, 지하수 함양, 하천 건천화 방지, 홍수 저감 등 다양한 효과를 제공하며, 장기적으로 우수 관거 건설 비용을 절감합니다. 침투시설 설치 시 토양 오염 방지를 위해 침전조, 필터층을 설치하고, 유지관리를 위해 점검구, 청소구를 설치합니다. 베트남은 침투시설 개념이 생소하고, 빗물을 즉시 배출하는 방식(직배수)을 선호합니다. 침투시설을 도입하더라도 토양 투수계수를 확인하지 않고 설치하거나, 필터층을 생략하여 막힘이 발생하는 경우가 많습니다. 한국 설계자가 침투시설을 요구하면 베트남 시공사는 '효과가 불확실하다', '유지관리가 어렵다'는 이유로 반발하는 경우가 있어, 통역 시 침투시설의 환경적·경제적 효과를 설득력 있게 전달해야 합니다.",
        "commonMistakes": [
            {
                "mistake": "'침투시설'을 'công trình thoát nước'(배수시설)로 번역",
                "correction": "'công trình thấm' 또는 'cơ sở thấm nước mưa' 사용",
                "explanation": "배수시설은 물을 외부로 배출, 침투시설은 지하로 침투"
            },
            {
                "mistake": "'침투 트렌치'를 'rãnh thoát nước'(배수 트렌치)로 번역",
                "correction": "'rãnh thấm' 또는 'rãnh thoát nước ngầm' 사용",
                "explanation": "침투 트렌치는 물을 지하로 침투시키는 구조물"
            },
            {
                "mistake": "침투시설과 저류조를 동일한 것으로 설명",
                "correction": "저류조는 '저장 후 방류', 침투시설은 '지하로 침투'로 구분",
                "explanation": "목적과 구조가 다르므로 혼동 시 설계 오류 발생"
            }
        ],
        "examples": [
            {
                "ko": "주차장 하부에 침투 트렌치를 설치하여 빗물을 지하로 침투시키세요.",
                "vi": "Lắp rãnh thấm dưới bãi đỗ xe để thấm nước mưa xuống đất.",
                "situation": "onsite"
            },
            {
                "ko": "침투시설은 토양 투수계수가 1×10⁻³ cm/s 이상인 지역에 적용 가능합니다.",
                "vi": "Công trình thấm có thể áp dụng ở khu vực có hệ số thấm đất ≥1×10⁻³ cm/s.",
                "situation": "formal"
            },
            {
                "ko": "침투시설을 설치하면 우수 관거 부담이 줄어들어 비용을 절감할 수 있어요.",
                "vi": "Lắp công trình thấm giảm gánh nặng cống thoát nước mưa, tiết kiệm chi phí.",
                "situation": "informal"
            }
        ],
        "relatedTerms": [
            "침투트렌치",
            "저류조",
            "투수블록",
            "LID",
            "지하수함양"
        ]
    },
    {
        "slug": "cong-thoat-nuoc-mua",
        "korean": "우수관거",
        "vietnamese": "cống thoát nước mưa",
        "hanja": "雨水管渠",
        "hanjaReading": "우(비 우) + 수(물 수) + 관(대롱 관) + 거(도랑 거)",
        "pronunciation": "꽁 토앗 늑 므어",
        "meaningKo": "빗물을 집수하여 하천이나 바다로 배출하는 지하 관로 시스템으로, 도시 배수 인프라의 핵심 요소입니다. 통역 시 '우수관거'는 'cống thoát nước mưa' 또는 'hệ thống cống nước mưa'로 표현하며, '오수관거(cống nước thải)'와 명확히 구분해야 합니다. 오수관거는 생활하수를 처리장으로 운반하는 관로이고, 우수관거는 빗물을 자연 수계로 배출하는 관로입니다. 한국은 '분류식 하수도(separate sewer system)'를 원칙으로 하여 우수와 오수를 별도 관거로 처리하지만, 일부 구도심은 '합류식 하수도(combined sewer system)'로 우수와 오수를 동일 관거로 처리합니다. 우수관거 설계 시 유역 면적, 강우 강도, 유출계수를 고려하여 관경과 경사를 결정하며, 관거 내 최소 유속은 0.6m/s, 최대 유속은 3.0m/s로 제한합니다. 관거 재질은 철근콘크리트관(RCP), PVC관, HDPE관 등이 사용되며, 접합부는 고무링 또는 시멘트 모르타르로 밀봉합니다.",
        "meaningVi": "Cống thoát nước mưa (hệ thống cống nước mưa) là hệ thống đường ống ngầm thu nước mưa và xả ra sông biển, là yếu tố cốt lõi của hạ tầng thoát nước đô thị. Khác với cống nước thải (xử lý nước sinh hoạt), cống nước mưa xả trực tiếp ra tự nhiên. Thiết kế dựa trên diện tích lưu vực, cường độ mưa, hệ số dòng chảy. Vận tốc tối thiểu 0.6m/s, tối đa 3.0m/s.",
        "context": "하수도공사, 도로공사, 배수설계",
        "culturalNote": "한국은 우수관거를 분류식으로 설치하는 것이 원칙이며, 신도시·개발지역은 100% 분류식입니다. 우수관거는 10년~30년 빈도 강우를 기준으로 설계하며, 대형 관거는 100년 빈도까지 고려합니다. 관거 내부는 CCTV로 정기 점검하고, 퇴적물을 준설 차량으로 제거하여 배수 능력을 유지합니다. 베트남은 우수관거와 오수관거를 구분하지 않는 합류식이 많으며, 신규 개발지에서도 비용 절감을 이유로 합류식을 선택하는 경우가 있습니다. 합류식은 건기에는 문제가 없지만, 우기에 관거 용량이 부족하여 미처리 하수가 하천으로 월류(overflow)하는 문제가 발생합니다. 한국 설계자가 분류식을 요구하면 베트남 시공사는 '관거가 2배로 늘어난다', '비용이 많이 든다'는 이유로 반발하는 경우가 있어, 통역 시 분류식의 환경적·위생적 장점을 명확히 전달해야 합니다.",
        "commonMistakes": [
            {
                "mistake": "'우수관거'를 'cống thoát nước'(일반 배수관)로만 번역",
                "correction": "'cống thoát nước mưa'로 명확히 표기",
                "explanation": "'cống thoát nước'는 우수·오수 모두 포함하는 일반 용어"
            },
            {
                "mistake": "'분류식'을 'hệ thống riêng'(별도 시스템)으로 직역",
                "correction": "'hệ thống tách riêng nước mưa và nước thải' 사용",
                "explanation": "분류식은 우수와 오수를 별도 관거로 분리하는 방식"
            },
            {
                "mistake": "'합류식'을 'hệ thống chung'(공동 시스템)으로 직역",
                "correction": "'hệ thống thoát nước hỗn hợp' 또는 'cống chung nước mưa và nước thải' 사용",
                "explanation": "합류식은 우수와 오수를 하나의 관거로 처리하는 방식"
            }
        ],
        "examples": [
            {
                "ko": "이 지역은 분류식 하수도이므로 우수관거와 오수관거를 별도로 설치하세요.",
                "vi": "Khu này là hệ thống tách riêng nên lắp cống nước mưa và cống nước thải riêng biệt.",
                "situation": "onsite"
            },
            {
                "ko": "우수관거 관경은 D600mm로 설계하고, 경사는 0.3%로 유지합니다.",
                "vi": "Đường kính cống nước mưa thiết kế D600mm, độ dốc duy trì 0.3%.",
                "situation": "formal"
            },
            {
                "ko": "합류식은 우기에 하수가 넘쳐서 오염 문제가 생길 수 있어요.",
                "vi": "Hệ thống hỗn hợp có thể tràn nước thải mùa mưa gây ô nhiễm.",
                "situation": "informal"
            }
        ],
        "relatedTerms": [
            "오수관거",
            "분류식",
            "합류식",
            "집수정",
            "맨홀"
        ]
    },
    {
        "slug": "he-thong-hon-hop",
        "korean": "합류식",
        "vietnamese": "hệ thống hỗn hợp",
        "hanja": "合流式",
        "hanjaReading": "합(합할 합) + 류(흐를 류) + 식(법 식)",
        "pronunciation": "헤 통 혼 홉",
        "meaningKo": "빗물(우수)과 생활하수(오수)를 하나의 관거로 함께 배수하는 하수도 시스템 방식입니다. 통역 시 '합류식'은 'hệ thống hỗn hợp' 또는 'hệ thống thoát nước chung'으로 표현하며, '분류식(hệ thống tách riêng)'과 대비하여 설명해야 합니다. 합류식은 관거가 하나이므로 초기 건설비가 저렴하고 시공이 간편하지만, 우기에 관거 용량이 부족하여 미처리 하수가 하천으로 월류(CSO, Combined Sewer Overflow)하는 문제가 발생합니다. 한국은 구도심(1980년대 이전 개발지)에 합류식이 많이 남아 있으며, 환경부는 합류식 개선 사업(CSO 저감 사업)을 추진하여 차집관거(interceptor sewer), 저류조, 스크린 시설을 설치하고 있습니다. 신규 개발지는 분류식을 의무 적용하며, 합류식은 점차 분류식으로 전환되고 있습니다. 합류식 하수도는 건기에는 모든 하수가 처리장으로 가지만, 우기에는 관거 용량의 3배 이상 유량이 유입되어 초과분이 하천으로 월류합니다.",
        "meaningVi": "Hệ thống hỗn hợp (hệ thống thoát nước chung) là phương thức thoát nước chung cho nước mưa và nước thải sinh hoạt trong một cống. Ưu điểm: chi phí xây dựng thấp, thi công đơn giản. Nhược điểm: mùa mưa dung tích cống không đủ, nước thải chưa xử lý tràn ra sông (CSO). Hàn Quốc đang chuyển đổi hệ thống hỗn hợp thành hệ thống tách riêng.",
        "context": "하수도공사, 배수설계, 환경공학",
        "culturalNote": "한국은 합류식 하수도의 환경 문제를 심각하게 인식하고 있으며, 정부 예산으로 합류식 개선 사업을 추진합니다. CSO 저감을 위해 차집관거를 설치하여 오수를 최대한 처리장으로 보내고, 초과 유량은 저류조에 임시 저장하거나 스크린으로 협잡물을 제거한 후 방류합니다. 합류식 관거는 내부 퇴적물(슬러지, 모래)이 많아 정기적인 준설(청소)이 필수입니다. 베트남은 대부분 합류식 하수도이며, 신규 개발지에서도 비용 절감을 이유로 합류식을 선택하는 경우가 많습니다. 합류식의 CSO 문제를 인식하지 못하거나, 인식하더라도 처리 시설 투자를 꺼립니다. 한국 설계자가 분류식을 요구하면 베트남 발주처는 '비용이 2배'라며 합류식을 고집하는 경우가 있어, 통역 시 합류식의 장기 환경 비용(하천 오염, 처리장 과부하)을 설명하여 분류식의 필요성을 설득해야 합니다.",
        "commonMistakes": [
            {
                "mistake": "'합류식'을 'hệ thống chung'(공동 시스템)으로만 번역",
                "correction": "'hệ thống hỗn hợp' 또는 'hệ thống thoát nước chung nước mưa và nước thải' 사용",
                "explanation": "'hệ thống chung'은 의미가 모호하므로 우수+오수 혼합을 명확히 해야 함"
            },
            {
                "mistake": "'CSO(Combined Sewer Overflow)'를 번역 없이 영문 약어만 사용",
                "correction": "'tràn cống hỗn hợp' 또는 'nước thải tràn từ hệ thống chung' 병기",
                "explanation": "베트남 기술자는 CSO 용어에 익숙하지 않음"
            },
            {
                "mistake": "합류식과 분류식의 차이를 설명 없이 번역",
                "correction": "관거 수, 비용, 환경 영향을 비교 설명",
                "explanation": "베트남 발주처는 합류식의 장기 문제를 잘 모르는 경우가 많음"
            }
        ],
        "examples": [
            {
                "ko": "이 구도심은 합류식 하수도이므로 우기에 CSO가 발생할 수 있습니다.",
                "vi": "Khu cũ này là hệ thống hỗn hợp nên mùa mưa có thể xảy ra tràn cống.",
                "situation": "formal"
            },
            {
                "ko": "합류식을 분류식으로 개선하여 하천 수질을 보호해야 합니다.",
                "vi": "Cần cải tạo hệ thống hỗn hợp thành hệ thống tách riêng để bảo vệ chất lượng nước sông.",
                "situation": "formal"
            },
            {
                "ko": "합류식은 초기 비용은 적지만, 나중에 환경 문제로 더 많은 돈이 들어요.",
                "vi": "Hệ thống hỗn hợp chi phí ban đầu thấp nhưng sau này tốn nhiều tiền hơn vì vấn đề môi trường.",
                "situation": "informal"
            }
        ],
        "relatedTerms": [
            "분류식",
            "CSO",
            "차집관거",
            "우수관거",
            "오수관거"
        ]
    },
    {
        "slug": "he-thong-tach-rieng",
        "korean": "분류식",
        "vietnamese": "hệ thống tách riêng",
        "hanja": "分流式",
        "hanjaReading": "분(나눌 분) + 류(흐를 류) + 식(법 식)",
        "pronunciation": "헤 통 타익 지엥",
        "meaningKo": "빗물(우수)과 생활하수(오수)를 각각 별도의 관거로 분리하여 배수하는 하수도 시스템 방식입니다. 통역 시 '분류식'은 'hệ thống tách riêng' 또는 'hệ thống thoát nước phân ly'로 표현하며, '합류식(hệ thống hỗn hợp)'과 대비하여 설명해야 합니다. 분류식은 우수는 우수관거로 하천에 직접 배출하고, 오수는 오수관거로 하수처리장에 보내어 처리 후 방류하므로, 하천 수질 보호와 처리장 효율성이 높습니다. 한국은 1980년대 이후 신규 개발지에 분류식을 의무 적용하고 있으며, 「하수도법」에서 분류식을 원칙으로 규정하고 있습니다. 분류식은 관거가 2개이므로 초기 건설비가 합류식보다 1.5~2배 높지만, 장기적으로 하수처리장 용량 절감, 하천 오염 방지, 유지관리비 절감 등의 효과가 있습니다. 분류식 하수도는 오수관거와 우수관거의 오접(misconne ction)을 방지하기 위해 준공 전 염색시험(dye test) 또는 CCTV 조사를 실시하여 정확한 연결 여부를 확인합니다.",
        "meaningVi": "Hệ thống tách riêng (hệ thống thoát nước phân ly) là phương thức thoát nước riêng biệt cho nước mưa (cống nước mưa) và nước thải (cống nước thải). Nước mưa xả trực tiếp ra sông, nước thải đưa vào nhà máy xử lý. Ưu điểm: bảo vệ chất lượng nước sông, hiệu quả xử lý cao. Nhược điểm: chi phí xây dựng cao hơn hệ thống hỗn hợp 1.5~2 lần.",
        "context": "하수도공사, 배수설계, 환경공학",
        "culturalNote": "한국은 분류식 하수도를 환경 보호의 핵심 인프라로 간주하며, 정부가 분류식 전환 사업에 막대한 예산을 투입하고 있습니다. 분류식은 우수와 오수를 분리하므로 처리장 용량을 줄일 수 있고, 우기에도 처리 효율이 안정적입니다. 분류식 관거는 오접을 방지하기 위해 색상(우수=청색, 오수=갈색)으로 구분하고, 맨홀 뚜껑에 표시('U'=우수, 'S'=오수)를 합니다. 베트남은 분류식의 장점을 알고 있지만, 초기 투자비 부담으로 합류식을 선호하는 경향이 있습니다. 분류식을 적용하더라도 시공 단계에서 오접(우수관거에 오수 연결, 또는 그 반대)이 발생하는 경우가 많아, 준공 후 악취, 하천 오염 문제가 나타납니다. 한국 감리는 염색시험(오수관거에 염료를 넣어 우수관거에 나오는지 확인)을 의무 실시하지만, 베트남 현장은 비용·시간 문제로 생략하는 경우가 많아 통역 시 시험의 중요성을 강조해야 합니다.",
        "commonMistakes": [
            {
                "mistake": "'분류식'을 'hệ thống riêng'(별도 시스템)으로만 번역",
                "correction": "'hệ thống tách riêng nước mưa và nước thải' 사용",
                "explanation": "'hệ thống riêng'은 의미가 모호하므로 우수·오수 분리를 명확히 해야 함"
            },
            {
                "mistake": "'오접(誤接)'을 'sai kết nối'(잘못 연결)로만 번역",
                "correction": "'kết nối sai ống cống' 또는 'nhầm lẫn cống nước mưa và nước thải' 사용",
                "explanation": "오접은 우수관거와 오수관거를 잘못 연결하는 특정 오류"
            },
            {
                "mistake": "분류식과 합류식의 장단점을 설명 없이 번역",
                "correction": "초기 비용, 환경 효과, 유지관리를 비교 설명",
                "explanation": "베트남 발주처는 분류식의 장기 이점을 이해하지 못하는 경우가 많음"
            }
        ],
        "examples": [
            {
                "ko": "신규 개발지는 분류식 하수도로 설계하여 우수와 오수를 분리하세요.",
                "vi": "Khu phát triển mới thiết kế hệ thống tách riêng để phân ly nước mưa và nước thải.",
                "situation": "formal"
            },
            {
                "ko": "분류식은 처리장 부담을 줄이고 하천 수질을 보호하는 효과가 있습니다.",
                "vi": "Hệ thống tách riêng giảm gánh nặng nhà máy xử lý và bảo vệ chất lượng nước sông.",
                "situation": "formal"
            },
            {
                "ko": "분류식은 비용이 더 들지만, 환경을 생각하면 꼭 필요해요.",
                "vi": "Hệ thống tách riêng tốn tiền hơn nhưng cần thiết cho môi trường.",
                "situation": "informal"
            }
        ],
        "relatedTerms": [
            "합류식",
            "우수관거",
            "오수관거",
            "오접",
            "염색시험"
        ]
    }
]

# 저장 경로
output_path = os.path.join(
    os.path.dirname(os.path.abspath(__file__)),
    "..",
    "data",
    "terms",
    "construction.json"
)

print(f"저장 경로: {output_path}")
print(f"추가할 용어 개수: {len(data)}개")
print("\n추가할 용어 목록:")
for i, term in enumerate(data, 1):
    print(f"{i}. {term['korean']} ({term['vietnamese']})")

# 실행 금지 - 스크립트만 생성
print("\n⚠️  이 스크립트는 실행하지 마세요. Write만 하고 종료합니다.")
