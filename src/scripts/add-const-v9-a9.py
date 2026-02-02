#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Construction 용어 추가 스크립트 - 실내공기질/환기 테마
테마: 포름알데히드, VOC, 새집증후군, 전열교환기, 환기설비, 공기질측정, 베이크아웃, 친환경자재, E0등급, 녹색건자재인증
"""

import json
import os

# 추가할 용어 데이터 (Tier S 기준)
data = [
    {
        "slug": "formaldehyde",
        "korean": "포름알데히드",
        "vietnamese": "Formaldehyd",
        "hanja": "甲醛",
        "hanjaReading": "갑(첫째 갑) + 醛(알데히드 전)",
        "pronunciation": "포름알데히드",
        "meaningKo": "새 건물이나 리모델링 공사 후 실내에서 방출되는 유해 화학물질로, 합판, MDF, 접착제, 페인트, 벽지 등 건축자재에서 주로 나오며 '새집증후군'의 주요 원인입니다. 통역 시 주의할 점은 한국에서는 '포름알데히드'를 외래어 그대로 사용하지만, 공식적으로는 '폼알데하이드' 또는 한자 '甲醛(갑전)'이라고도 하며, 베트남어로는 'formaldehyd' 또는 'fomanđehit'로 표기합니다. 포름알데히드는 무색의 자극적 냄새가 나는 기체로, WHO 기준 1급 발암물질로 분류되어 있으며, 장기간 노출 시 두통, 눈·코·목 자극, 호흡기 질환, 피부염을 유발합니다. 한국 실내공기질 관리법에서는 신축 공동주택(아파트)의 포름알데히드 기준을 0.08ppm 이하로 규정하고 있으며, 입주 전 반드시 공기질 측정을 의무화하고 있습니다. 통역 시 포름알데히드 수치가 기준을 초과할 경우 환기, 베이크아웃, 공기정화 등의 조치가 필요하다는 점과, 근로자 보호를 위해 작업 시 마스크 착용 및 환기가 필수임을 명확히 전달해야 합니다.",
        "meaningVi": "Formaldehyd là chất hóa học độc hại phát tán từ vật liệu xây dựng như ván ép, MDF, keo dán, sơn và giấy dán tường trong các công trình mới hoặc sau cải tạo, là nguyên nhân chính gây 'hội chứng nhà mới' (sick building syndrome). Formaldehyd là chất khí không màu có mùi kích thích, được WHO phân loại là chất gây ung thư nhóm 1. Tiếp xúc lâu dài gây đau đầu, kích ứng mắt/mũi/họng, bệnh hô hấp và viêm da. Theo pháp luật Hàn Quốc, nồng độ formaldehyd trong chung cư mới phải dưới 0,08ppm và bắt buộc đo chất lượng không khí trước khi vào ở.",
        "context": "신축 건물 준공 검사, 리모델링 후 공기질 측정, 새집증후군 예방, 근로자 건강 보호",
        "culturalNote": "한국에서는 2006년부터 '실내공기질 관리법'으로 신축 아파트의 포름알데히드 농도를 엄격히 규제하며, 입주 전 공기질 측정 결과를 입주민에게 공개해야 합니다. 기준 초과 시 건설사가 환기 설비 개선, 베이크아웃(고온 환기), 공기정화 등의 조치를 취해야 하며, 입주 시기를 연기할 수도 있습니다. 베트남에서는 실내공기질 규제가 한국만큼 엄격하지 않아, 베트남 근로자들이 포름알데히드의 위험성을 낮게 평가하거나 환기 없이 작업하는 경우가 있습니다. 통역 시 포름알데히드는 냄새로만 판단할 수 없으며(냄새 역치 이하 농도도 유해), 측정 장비로 정확히 확인해야 한다는 점과, 신축 현장에서는 작업 중 창문을 열어 환기하고 마스크를 착용해야 한다는 안전 수칙을 강조해야 합니다.",
        "commonMistakes": [
            {
                "mistake": "'formaldehyd' 발음을 '포말데히드'로 잘못 전달",
                "correction": "정확한 발음 '포름알데히드'로 교정",
                "explanation": "한국에서는 '포름알데히드'가 표준 발음입니다."
            },
            {
                "mistake": "냄새가 나지 않으면 안전하다고 설명",
                "correction": "냄새 역치 이하 농도도 유해하므로 측정 필수",
                "explanation": "포름알데히드는 무취 상태에서도 유해할 수 있습니다."
            },
            {
                "mistake": "WHO 발암물질 등급 미전달",
                "correction": "1급 발암물질임을 명시하여 위험성 강조",
                "explanation": "발암물질임을 알려야 근로자가 보호 조치의 중요성을 이해합니다."
            }
        ],
        "examples": [
            {
                "ko": "이 현장의 포름알데히드 농도가 0.12ppm으로 기준치를 초과했습니다. 베이크아웃 작업 후 재측정하겠습니다.",
                "vi": "Nồng độ formaldehyd tại công trường này là 0,12ppm, vượt quá tiêu chuẩn. Chúng tôi sẽ đo lại sau khi làm bake-out.",
                "situation": "formal"
            },
            {
                "ko": "합판 작업할 때는 포름알데히드가 많이 나오니까 반드시 마스크 쓰고 창문 열어서 일하세요.",
                "vi": "Khi làm việc với ván ép, formaldehyd thoát ra nhiều nên nhất định phải đeo khẩu trang và mở cửa sổ làm việc.",
                "situation": "onsite"
            },
            {
                "ko": "여기 냄새 좀 나는데? 포름알데히드 아냐? 측정기 가져와봐.",
                "vi": "Chỗ này có mùi nhỉ? Formaldehyd hả? Lấy máy đo đến xem.",
                "situation": "informal"
            }
        ],
        "relatedTerms": [
            "VOC",
            "새집증후군",
            "베이크아웃",
            "공기질측정",
            "친환경자재"
        ]
    },
    {
        "slug": "voc-chat-huu-co-bay-hoi",
        "korean": "VOC",
        "vietnamese": "VOC (Chất hữu cơ bay hơi)",
        "hanja": "揮發性有機化合物",
        "hanjaReading": "휘(휘두를 휘) + 發(발할 발) + 性(성품 성) + 有(있을 유) + 機(틀 기) + 化(될 화) + 合(합할 합) + 物(물건 물)",
        "pronunciation": "브이오씨 / 휘발성유기화합물",
        "meaningKo": "상온에서 쉽게 증발하는 유기화합물의 총칭으로, 페인트, 접착제, 실란트, 방수제, 용제 등 건축자재와 마감재에서 방출되는 유해 물질입니다. 통역 시 주의할 점은 한국에서는 영문 약어 'VOC(브이오씨)'를 주로 사용하지만, 공식 용어는 '휘발성 유기화합물'이며, 베트남어로는 'chất hữu cơ bay hơi' 또는 약어 그대로 'VOC'를 사용합니다. VOC에는 벤젠, 톨루엔, 자일렌, 에틸벤젠, 스티렌 등 수백 종의 화합물이 포함되며, 각각 독성과 냄새가 다릅니다. 한국 실내공기질 관리법에서는 신축 공동주택의 총 VOC(TVOC) 기준을 500㎍/㎥ 이하로 규정하고 있으며, 일부 유해 VOC(벤젠, 톨루엔 등)는 개별 기준도 있습니다. 통역 시 VOC는 단기적으로 두통, 현기증, 눈·코·목 자극을 유발하고, 장기 노출 시 간 손상, 신경계 이상, 암을 유발할 수 있다는 점과, 페인트나 접착제 작업 시 반드시 환기하고 보호구를 착용해야 한다는 안전 수칙을 강조해야 합니다.",
        "meaningVi": "VOC (Volatile Organic Compounds - Chất hữu cơ bay hơi) là tổng hợp các hợp chất hữu cơ dễ bay hơi ở nhiệt độ thường, phát tán từ sơn, keo dán, chất trám kín, chất chống thấm và dung môi trong vật liệu xây dựng. VOC bao gồm hàng trăm hợp chất như benzen, toluen, xylen, etylbenzen, styren, mỗi loại có độc tính và mùi khác nhau. Theo luật Hàn Quốc, tổng VOC (TVOC) trong chung cư mới phải dưới 500㎍/㎥. Tiếp xúc ngắn hạn gây đau đầu, chóng mặt, kích ứng mắt/mũi/họng; tiếp xúc lâu dài gây tổn thương gan, rối loạn thần kinh và ung thư.",
        "context": "도장 작업, 접착 작업, 방수 작업, 실내 마감 공사, 공기질 측정",
        "culturalNote": "한국 건설 현장에서는 VOC 저감을 위해 '친환경 자재' 사용을 권장하며, 특히 학교, 병원, 어린이집 등 민감 시설에서는 저VOC 또는 무VOC 제품 사용을 의무화하고 있습니다. 페인트나 접착제 제품에는 VOC 함량이 표기되어 있으며, 'E0 등급', '친환경 마크', 'HB(Healthy Building) 마크' 등으로 인증받은 제품이 선호됩니다. 베트남에서는 VOC 규제가 덜 엄격하여 가격이 저렴한 고VOC 제품을 사용하는 경우가 많은데, 한국에서는 이것이 법적 기준 위반이며 근로자 건강에도 해롭다는 점을 명확히 해야 합니다. 통역 시 VOC 함량이 높은 작업(페인트, 방수, 접착) 시에는 반드시 방독 마스크를 착용하고, 밀폐 공간에서는 송풍기로 강제 환기해야 하며, 작업 후에도 최소 2~3일간 환기를 지속해야 한다는 안전 수칙을 강조해야 합니다.",
        "commonMistakes": [
            {
                "mistake": "'VOC'를 구체적 물질 하나로 오해",
                "correction": "수백 종 화합물의 총칭임을 설명",
                "explanation": "VOC는 단일 물질이 아니라 휘발성 유기화합물 전체를 의미합니다."
            },
            {
                "mistake": "냄새로만 VOC 유무 판단",
                "correction": "무취 VOC도 존재하므로 측정 필수",
                "explanation": "일부 VOC는 냄새가 없어도 유해합니다."
            },
            {
                "mistake": "환기만으로 충분하다고 설명",
                "correction": "고농도 작업 시 방독 마스크 필수 착용",
                "explanation": "환기만으로는 불충분하며 개인 보호구가 필요합니다."
            }
        ],
        "examples": [
            {
                "ko": "이 페인트는 TVOC 함량이 50g/L 이하로 친환경 인증을 받았으니, 학교 공사에 사용 가능합니다.",
                "vi": "Sơn này có hàm lượng TVOC dưới 50g/L, đã được chứng nhận thân thiện môi trường nên có thể dùng cho công trình trường học.",
                "situation": "formal"
            },
            {
                "ko": "방수 작업할 때 VOC가 많이 나오니까 방독 마스크 쓰고, 송풍기 틀어놓고 일하세요.",
                "vi": "Khi làm chống thấm, VOC thoát ra nhiều nên phải đeo mặt nạ chống độc và bật quạt thông gió làm việc.",
                "situation": "onsite"
            },
            {
                "ko": "이 접착제 냄새 장난 아니네. VOC 얼마나 되는 거야? 환기 좀 시켜.",
                "vi": "Keo này mùi kinh khủng. VOC bao nhiêu vậy? Thông gió đi.",
                "situation": "informal"
            }
        ],
        "relatedTerms": [
            "포름알데히드",
            "TVOC",
            "친환경자재",
            "E0등급",
            "베이크아웃"
        ]
    },
    {
        "slug": "hoi-chung-nha-moi",
        "korean": "새집증후군",
        "vietnamese": "Hội chứng nhà mới",
        "hanja": None,
        "hanjaReading": None,
        "pronunciation": "새집증후군",
        "meaningKo": "신축 건물이나 리모델링 공사 직후 실내공기 오염으로 인해 거주자나 근로자가 겪는 건강 이상 증상으로, 영어로는 'Sick Building Syndrome'이라고 합니다. 통역 시 주의할 점은 한국에서는 '새집증후군'이라는 용어가 일반적이지만, 공식적으로는 '실내공기질 관련 건강 장애'라고 하며, 베트남어로는 'hội chứng nhà mới' 또는 'hội chứng tòa nhà ốm'으로 표현합니다. 새집증후군의 주요 증상으로는 두통, 어지러움, 눈·코·목 자극, 피부 발진, 호흡곤란, 피로감, 집중력 저하 등이 있으며, 원인 물질로는 포름알데히드, VOC, 라돈, 곰팡이, 석면 등이 있습니다. 한국에서는 2005년 이후 신축 아파트 입주 시 새집증후군이 사회적 이슈가 되어, 2006년 실내공기질 관리법이 제정되었고 입주 전 공기질 측정이 의무화되었습니다. 통역 시 새집증후군 예방을 위해 입주·사용 전 최소 2주간 집중 환기(베이크아웃)가 필요하며, 증상이 나타나면 즉시 환기하고 의료 조치를 받아야 한다는 점을 명확히 전달해야 합니다.",
        "meaningVi": "Hội chứng nhà mới (Sick Building Syndrome) là các triệu chứng bất thường về sức khỏe mà cư dân hoặc công nhân gặp phải do ô nhiễm không khí trong nhà sau xây dựng mới hoặc cải tạo. Triệu chứng chính bao gồm đau đầu, chóng mặt, kích ứng mắt/mũi/họng, phát ban da, khó thở, mệt mỏi và giảm khả năng tập trung. Nguyên nhân là các chất độc hại như formaldehyd, VOC, radon, nấm mốc, amiăng. Tại Hàn Quốc, từ năm 2006, luật quản lý chất lượng không khí trong nhà bắt buộc đo chất lượng không khí trước khi vào ở.",
        "context": "신축 건물 입주 전, 리모델링 후 사용 전, 실내공기질 측정, 근로자 건강 관리",
        "culturalNote": "한국에서는 새집증후군이 매우 심각한 문제로 인식되며, 특히 아파트 입주민들이 건설사에 공기질 개선을 요구하거나 손해배상 소송을 제기하는 경우도 많습니다. 이에 따라 건설사들은 친환경 자재 사용, 사전 베이크아웃, 공기청정기 무상 지원 등 적극적인 대책을 마련합니다. 베트남에서는 새집증후군 개념이 덜 알려져 있어, 베트남 근로자들이 신축 현장에서 환기 없이 작업하거나 즉시 입주하여 건강 문제를 겪는 경우가 있습니다. 통역 시 새집증후군은 예방이 핵심이며, 공사 중에는 저VOC·저포름알데히드 자재를 사용하고, 완공 후에는 최소 2주간(여름 기준, 겨울은 4주) 창문을 열어 환기하며, 가능하면 베이크아웃(실내 온도를 30도 이상으로 올려 유해물질 방출 가속 후 환기)을 실시해야 한다는 점을 강조해야 합니다.",
        "commonMistakes": [
            {
                "mistake": "'새집'만 문제라고 설명",
                "correction": "리모델링, 인테리어 공사 후에도 발생 가능",
                "explanation": "기존 건물도 공사 후 공기질 문제가 생길 수 있습니다."
            },
            {
                "mistake": "환기만 하면 즉시 해결된다고 설명",
                "correction": "최소 2~4주간 지속 환기 및 베이크아웃 필요",
                "explanation": "단기 환기로는 불충분하며 장기 대책이 필요합니다."
            },
            {
                "mistake": "증상이 가벼우니 참으라고 조언",
                "correction": "증상 발생 시 즉시 환기 및 의료 조치 필요",
                "explanation": "초기 증상을 무시하면 만성 질환으로 악화될 수 있습니다."
            }
        ],
        "examples": [
            {
                "ko": "이 아파트는 입주 전 2주간 베이크아웃을 실시하여 새집증후군을 예방하고, 공기질 측정 결과 모든 항목이 기준치 이하입니다.",
                "vi": "Chung cư này đã thực hiện bake-out trong 2 tuần trước khi vào ở để phòng hội chứng nhà mới, và kết quả đo chất lượng không khí cho thấy tất cả chỉ số đều dưới tiêu chuẩn.",
                "situation": "formal"
            },
            {
                "ko": "페인트 칠하고 나서 바로 들어가지 말고, 최소 2주는 창문 열어서 환기시키세요. 새집증후군 생깁니다.",
                "vi": "Sau khi sơn xong đừng vào ngay, ít nhất 2 tuần phải mở cửa sổ thông gió. Sẽ bị hội chứng nhà mới.",
                "situation": "onsite"
            },
            {
                "ko": "여기 들어오면 머리 아프고 눈 따가워. 새집증후군 아냐? 환기 좀 시켜.",
                "vi": "Vào đây là đau đầu và cay mắt. Hội chứng nhà mới hả? Thông gió đi.",
                "situation": "informal"
            }
        ],
        "relatedTerms": [
            "포름알데히드",
            "VOC",
            "베이크아웃",
            "공기질측정",
            "실내공기질"
        ]
    },
    {
        "slug": "may-thong-gio-hoi-nhiet",
        "korean": "전열교환기",
        "vietnamese": "Máy thông gió hồi nhiệt",
        "hanja": "全熱交換器",
        "hanjaReading": "전(온전할 전) + 열(더울 열) + 교(사귈 교) + 환(바꿀 환) + 기(그릇 기)",
        "pronunciation": "전열교환기",
        "meaningKo": "실내 환기 시 배출되는 공기의 열을 회수하여 유입되는 외부 공기에 전달함으로써 에너지 손실을 줄이는 환기 장치로, '열회수 환기장치', 'HRV(Heat Recovery Ventilator)' 또는 'ERV(Energy Recovery Ventilator)'라고도 불립니다. 통역 시 주의할 점은 한국에서는 '전열교환기'가 공식 용어이지만 현장에서는 'HRV'를 더 많이 사용하며, 베트남어로는 'máy thông gió hồi nhiệt' 또는 'thiết bị trao đổi nhiệt toàn phần'으로 표현합니다. 전열교환기는 열교환 소자(필터)를 통해 배출 공기와 유입 공기가 교차하면서 온도와 습도를 교환하며, 겨울에는 따뜻한 실내 공기의 열을 차가운 외부 공기에 전달하고, 여름에는 반대로 작동합니다. 한국 건축법에서는 2006년 이후 신축 공동주택(아파트) 전체 세대에 전열교환기 설치를 의무화하고 있으며, 환기 효율은 보통 70~80% 수준입니다. 통역 시 전열교환기는 단순 환풍기와 달리 에너지 절약형 환기 장치이며, 필터를 정기적으로 청소·교체해야 환기 효율이 유지된다는 점을 명확히 전달해야 합니다.",
        "meaningVi": "Máy thông gió hồi nhiệt (HRV/ERV - Heat/Energy Recovery Ventilator) là thiết bị thông gió thu hồi nhiệt từ không khí thải trong nhà để truyền sang không khí ngoài đưa vào, giảm tổn thất năng lượng. Thiết bị này có bộ trao đổi nhiệt (lõi lọc) cho phép không khí thải và không khí vào trao đổi nhiệt độ và độ ẩm: mùa đông truyền nhiệt từ không khí ấm trong nhà sang không khí lạnh ngoài, mùa hè ngược lại. Luật xây dựng Hàn Quốc bắt buộc lắp máy thông gió hồi nhiệt trong tất cả căn hộ chung cư mới từ năm 2006, với hiệu suất thông gió thường đạt 70~80%.",
        "context": "아파트 환기 설비, 공동주택 필수 설비, 에너지 절약 시스템, 실내공기질 관리",
        "culturalNote": "한국 아파트에서는 전열교환기가 '필수 가전'처럼 인식되며, 입주민들은 24시간 약풍으로 가동하거나 요리·청소 시 강풍으로 전환합니다. 최근에는 미세먼지 필터가 추가된 고성능 제품이나 IoT 연동 제품도 보급되고 있습니다. 전열교환기 필터는 3~6개월마다 청소하고, 2~3년마다 교체해야 하는데, 관리를 소홀히 하면 오히려 실내 공기가 오염될 수 있습니다. 베트남에서는 전열교환기가 거의 보급되지 않아, 베트남 근로자들이 장치의 원리와 중요성을 이해하기 어려워할 수 있습니다. 통역 시 전열교환기는 '에너지를 아끼면서 환기하는 기계'라고 쉽게 설명하고, 설치 위치(보통 화장실 천장 또는 발코니), 조작 방법(약·중·강풍 모드), 필터 청소 주기 등 실용적 정보를 함께 전달해야 합니다.",
        "commonMistakes": [
            {
                "mistake": "일반 환풍기와 혼동",
                "correction": "열회수 기능이 있는 에너지 절약형 환기 장치임을 명시",
                "explanation": "일반 환풍기는 단순 배기만 하지만, 전열교환기는 열교환을 합니다."
            },
            {
                "mistake": "필터 청소 불필요하다고 설명",
                "correction": "3~6개월마다 필터 청소 필수, 2~3년마다 교체",
                "explanation": "필터 관리를 소홀히 하면 환기 효율이 떨어지고 공기가 오염됩니다."
            },
            {
                "mistake": "HRV와 ERV를 완전히 다른 장치로 설명",
                "correction": "HRV는 열만, ERV는 열+습기 교환하는 차이",
                "explanation": "원리는 유사하며 ERV가 더 고급 기능을 포함합니다."
            }
        ],
        "examples": [
            {
                "ko": "이 아파트 전 세대에 전열교환기가 설치되어 있으며, 환기 효율 75% 이상의 제품을 사용하여 에너지 손실을 최소화합니다.",
                "vi": "Tất cả căn hộ trong chung cư này đều được lắp máy thông gió hồi nhiệt với hiệu suất thông gió trên 75%, giảm thiểu tổn thất năng lượng.",
                "situation": "formal"
            },
            {
                "ko": "전열교환기는 3개월마다 필터를 빼서 물로 씻고 말려서 다시 끼워야 합니다. 안 하면 공기가 더러워요.",
                "vi": "Máy thông gió hồi nhiệt phải tháo lõi lọc ra rửa nước và phơi khô rồi lắp lại mỗi 3 tháng. Không làm thì không khí sẽ bẩn.",
                "situation": "onsite"
            },
            {
                "ko": "전열교환기 필터 청소 언제 했어? 바람이 안 나오네.",
                "vi": "Lõi lọc máy thông gió hồi nhiệt lần cuối rửa khi nào? Gió không ra.",
                "situation": "informal"
            }
        ],
        "relatedTerms": [
            "환기설비",
            "HRV",
            "ERV",
            "열회수",
            "공기청정"
        ]
    },
    {
        "slug": "thiet-bi-thong-gio",
        "korean": "환기설비",
        "vietnamese": "Thiết bị thông gió",
        "hanja": "換氣設備",
        "hanjaReading": "환(바꿀 환) + 기(기운 기) + 설(베풀 설) + 비(갖출 비)",
        "pronunciation": "환기설비",
        "meaningKo": "건물 내부의 오염된 공기를 외부로 배출하고 신선한 외부 공기를 유입시키는 설비의 총칭으로, 자연환기(창문)와 기계환기(환풍기, 전열교환기, 송풍기 등)를 모두 포함합니다. 통역 시 주의할 점은 한국에서는 '환기설비'가 공식 용어이지만 현장에서는 '환기장치', '통풍설비', '공조설비' 등으로도 불리며, 베트남어로는 'thiết bị thông gió', 'hệ thống thông gió' 또는 'thiết bị thông khí'로 표현합니다. 환기설비는 종류에 따라 제1종(급기+배기 모두 기계), 제2종(급기만 기계), 제3종(배기만 기계), 제4종(자연환기)으로 분류되며, 한국 건축법에서는 용도와 면적에 따라 설치 기준이 다릅니다. 특히 지하주차장, 밀폐 작업장, 다중이용시설 등에서는 시간당 환기 횟수(ACH: Air Changes per Hour)를 법으로 규정하고 있습니다. 통역 시 환기설비는 단순히 공기를 순환시키는 것이 아니라 실내 공기질을 유지하고 유해 물질을 제거하는 필수 안전 설비이며, 작동 여부를 정기적으로 점검해야 한다는 점을 명확히 전달해야 합니다.",
        "meaningVi": "Thiết bị thông gió là tổng hợp các thiết bị đưa không khí ô nhiễm trong nhà ra ngoài và đưa không khí sạch từ ngoài vào, bao gồm cả thông gió tự nhiên (cửa sổ) và thông gió cơ học (quạt thông gió, máy thông gió hồi nhiệt, quạt thổi). Thiết bị thông gió được phân loại theo phương thức: Loại 1 (cấp + xả cơ học), Loại 2 (chỉ cấp cơ học), Loại 3 (chỉ xả cơ học), Loại 4 (tự nhiên). Luật xây dựng Hàn Quốc quy định tiêu chuẩn lắp đặt khác nhau theo mục đích và diện tích, đặc biệt quy định số lần thay không khí mỗi giờ (ACH) cho bãi đậu xe ngầm, khu làm việc kín và cơ sở phục vụ công chúng.",
        "context": "건축 설계, 공조 시스템, 지하공간 환기, 작업장 안전, 실내공기질 관리",
        "culturalNote": "한국에서는 환기설비 설치가 법적으로 매우 엄격하게 규제되며, 특히 2017년 이후 미세먼지 문제가 심각해지면서 환기설비에 공기청정 기능을 추가한 '스마트 환기 시스템'이 보급되고 있습니다. 지하주차장은 CO 농도가 25ppm 이상 시 환기설비가 자동 작동하도록 설계되며, 밀폐 작업장(페인트, 용접 등)은 국소배기장치 설치가 의무입니다. 베트남에서는 환기설비가 한국만큼 보편화되지 않아, 베트남 근로자들이 환기의 중요성을 낮게 평가하거나 비용 절감을 위해 환기설비를 끄는 경우가 있습니다. 통역 시 환기설비는 법적 필수 설비이므로 임의로 끄거나 차단하면 안 되며, 특히 유해 가스나 분진이 발생하는 작업 중에는 반드시 가동해야 한다는 안전 수칙을 강조해야 합니다.",
        "commonMistakes": [
            {
                "mistake": "환기설비를 단순 '선풍기'로 번역",
                "correction": "'thiết bị thông gió' 또는 'hệ thống thông gió'로 명시",
                "explanation": "환기설비는 체계적인 공기 순환 시스템입니다."
            },
            {
                "mistake": "환기설비 종류(제1~4종) 설명 누락",
                "correction": "급배기 방식에 따른 분류 설명",
                "explanation": "현장에서 사용하는 환기설비 유형을 이해해야 합니다."
            },
            {
                "mistake": "환기설비를 임의로 꺼도 된다고 설명",
                "correction": "법적 필수 설비이므로 허가 없이 끄면 안 됨",
                "explanation": "환기설비는 안전과 직결되므로 임의 조작을 금지해야 합니다."
            }
        ],
        "examples": [
            {
                "ko": "이 지하주차장은 제1종 환기설비로 시간당 10회 환기되며, CO 센서 연동으로 자동 작동합니다.",
                "vi": "Bãi đậu xe ngầm này sử dụng thiết bị thông gió Loại 1, thay không khí 10 lần mỗi giờ và tự động hoạt động khi cảm biến CO phát hiện khí.",
                "situation": "formal"
            },
            {
                "ko": "페인트 작업할 때는 환기설비 켜고, 송풍기도 추가로 설치해서 공기가 잘 빠지게 하세요.",
                "vi": "Khi làm việc sơn, phải bật thiết bị thông gió và lắp thêm quạt thổi để không khí thoát ra tốt.",
                "situation": "onsite"
            },
            {
                "ko": "환기설비 소리 시끄럽다고 끄지 마. 그거 안전 장비야.",
                "vi": "Đừng tắt thiết bị thông gió vì ồn. Đó là thiết bị an toàn.",
                "situation": "informal"
            }
        ],
        "relatedTerms": [
            "전열교환기",
            "송풍기",
            "배기팬",
            "공조설비",
            "환기횟수"
        ]
    },
    {
        "slug": "do-chat-luong-khong-khi",
        "korean": "공기질측정",
        "vietnamese": "Đo chất lượng không khí",
        "hanja": "空氣質測定",
        "hanjaReading": "공(빌 공) + 기(기운 기) + 질(바탕 질) + 측(헤아릴 측) + 정(정할 정)",
        "pronunciation": "공기질측정",
        "meaningKo": "건물 내부 공기의 유해 물질 농도를 측정하여 실내공기질이 법적 기준에 적합한지 확인하는 작업으로, '실내공기질 검사', 'IAQ(Indoor Air Quality) 측정'이라고도 불립니다. 통역 시 주의할 점은 한국에서는 '공기질 측정'이 일반적이지만 공식적으로는 '실내공기질 측정'이며, 베트남어로는 'đo chất lượng không khí', 'kiểm tra chất lượng không khí trong nhà' 또는 'phân tích không khí'로 표현합니다. 공기질 측정 항목에는 포름알데히드, TVOC(총휘발성유기화합물), 벤젠, 톨루엔, 라돈, 미세먼지(PM10, PM2.5), 이산화탄소(CO2), 일산화탄소(CO) 등이 포함되며, 건물 용도에 따라 측정 항목과 기준이 다릅니다. 한국 실내공기질 관리법에서는 신축 공동주택(100세대 이상), 다중이용시설(지하역사, 병원, 학교 등)에 대해 주기적 측정을 의무화하고 있으며, 측정은 공인된 실내공기질 측정 대행업체가 수행해야 합니다. 통역 시 공기질 측정은 입주·사용 전 필수 절차이며, 기준 초과 시 환기·베이크아웃 등 개선 조치 후 재측정을 받아야 한다는 점을 명확히 전달해야 합니다.",
        "meaningVi": "Đo chất lượng không khí (IAQ - Indoor Air Quality measurement) là công việc đo nồng độ các chất độc hại trong không khí trong nhà để xác nhận chất lượng không khí đáp ứng tiêu chuẩn pháp lý. Các chỉ số đo bao gồm formaldehyd, TVOC, benzen, toluen, radon, bụi mịn (PM10, PM2.5), CO2, CO, với các hạng mục và tiêu chuẩn khác nhau tùy theo mục đích sử dụng tòa nhà. Theo luật quản lý chất lượng không khí trong nhà Hàn Quốc, bắt buộc phải đo định kỳ đối với chung cư mới (từ 100 hộ), cơ sở phục vụ công chúng (ga tàu điện ngầm, bệnh viện, trường học), và phải do đơn vị đo lường được chứng nhận thực hiện.",
        "context": "신축 건물 준공 검사, 다중이용시설 정기 점검, 리모델링 후 검사, 실내공기질 관리",
        "culturalNote": "한국에서는 2006년 이후 신축 아파트 입주 전 공기질 측정이 의무화되면서, 측정 결과를 입주민에게 공개하고 기준 초과 시 입주를 연기하거나 개선 조치를 취합니다. 최근에는 '공기질 인증' 제도도 생겨 우수 등급을 받은 건물은 분양 시 홍보 포인트로 활용됩니다. 공기질 측정은 전문 장비(광학식 측정기, 가스 크로마토그래피 등)를 사용하며, 측정 위치·시간·온도 등 조건이 법으로 규정되어 있습니다. 베트남에서는 공기질 측정이 일반화되지 않아, 베트남 근로자들이 측정의 필요성을 이해하지 못하거나 비용 낭비로 여기는 경우가 있습니다. 통역 시 공기질 측정은 법적 의무이자 근로자·거주자 건강 보호를 위한 필수 절차이며, 측정 시 창문을 닫고 5시간 이상 밀폐 후 측정한다는 등 측정 조건도 함께 설명해야 합니다.",
        "commonMistakes": [
            {
                "mistake": "측정 항목을 포름알데히드만으로 한정",
                "correction": "TVOC, 벤젠, 톨루엔, 라돈, 미세먼지 등 다양한 항목 설명",
                "explanation": "공기질 측정은 여러 유해 물질을 종합적으로 측정합니다."
            },
            {
                "mistake": "측정 시 환기하면서 진행",
                "correction": "측정 전 5시간 이상 밀폐 후 측정 필수",
                "explanation": "정확한 측정을 위해서는 일정 시간 밀폐가 필요합니다."
            },
            {
                "mistake": "간이 측정기로 자체 측정해도 된다고 설명",
                "correction": "공인 측정 대행업체의 정식 측정 필수",
                "explanation": "법적 효력을 위해서는 공인 기관의 측정이 필요합니다."
            }
        ],
        "examples": [
            {
                "ko": "준공 전 공기질 측정 결과 포름알데히드 0.06ppm, TVOC 350㎍/㎥로 모두 기준치 이하이므로 입주 가능합니다.",
                "vi": "Kết quả đo chất lượng không khí trước khi nghiệm thu cho thấy formaldehyd 0,06ppm, TVOC 350㎍/㎥, đều dưới tiêu chuẩn nên có thể vào ở.",
                "situation": "formal"
            },
            {
                "ko": "공기질 측정 하려면 창문 다 닫고 5시간 후에 측정합니다. 그 전에는 환기 금지예요.",
                "vi": "Để đo chất lượng không khí, phải đóng tất cả cửa sổ và đo sau 5 giờ. Trước đó cấm thông gió.",
                "situation": "onsite"
            },
            {
                "ko": "공기질 측정 언제 와? 빨리 끝내고 입주하고 싶은데.",
                "vi": "Đo chất lượng không khí khi nào đến? Muốn làm nhanh để vào ở.",
                "situation": "informal"
            }
        ],
        "relatedTerms": [
            "포름알데히드",
            "TVOC",
            "실내공기질",
            "IAQ",
            "준공검사"
        ]
    },
    {
        "slug": "bake-out",
        "korean": "베이크아웃",
        "vietnamese": "Bake-out",
        "hanja": None,
        "hanjaReading": None,
        "pronunciation": "베이크아웃",
        "meaningKo": "신축 건물이나 리모델링 공사 후 실내 온도를 30~40도로 높여 건축자재에서 유해 물질(포름알데히드, VOC 등)의 방출을 가속화한 후 환기하여 제거하는 공기질 개선 방법으로, '강제 환기법', '고온 환기법'이라고도 불립니다. 통역 시 주의할 점은 한국에서는 영어 그대로 '베이크아웃(bake-out)'을 사용하며, 베트남어로는 음차하여 'bake-out' 또는 의역하여 'phương pháp thông gió nhiệt độ cao'로 표현합니다. 베이크아웃은 보통 여름철(고온기)에 2~4주간 실시하며, 난방 또는 전기 히터로 실내 온도를 올리고, 2~3일 가열 후 창문을 열어 환기하는 과정을 반복합니다. 연구에 따르면 베이크아웃으로 포름알데히드를 30~50%, VOC를 40~60% 감소시킬 수 있으며, 한국 건설사들은 입주 전 '사전 베이크아웃'을 실시하여 새집증후군을 예방합니다. 통역 시 베이크아웃은 단순 환기보다 효과적이지만 전기 요금이 많이 들고, 여름철에 실시해야 효과가 크다는 점을 명확히 전달해야 합니다.",
        "meaningVi": "Bake-out là phương pháp cải thiện chất lượng không khí bằng cách tăng nhiệt độ trong nhà lên 30~40 độ sau xây dựng mới hoặc cải tạo để đẩy nhanh quá trình thoát các chất độc hại (formaldehyd, VOC) từ vật liệu xây dựng, sau đó thông gió để loại bỏ. Thường thực hiện trong 2~4 tuần vào mùa hè, sử dụng hệ thống sưởi hoặc máy sưởi điện để tăng nhiệt độ, lặp lại quy trình: sưởi ấm 2~3 ngày rồi mở cửa sổ thông gió. Nghiên cứu cho thấy bake-out giảm formaldehyd 30~50%, VOC 40~60%, và các công ty xây dựng Hàn Quốc thường thực hiện bake-out trước khi bàn giao để phòng hội chứng nhà mới.",
        "context": "신축 아파트 입주 전, 리모델링 후, 새집증후군 예방, 실내공기질 개선",
        "culturalNote": "한국에서는 베이크아웃이 새집증후군 예방의 핵심 방법으로 인식되며, 건설사들은 입주 2~3개월 전부터 전 세대에 대해 베이크아웃을 실시하거나, 입주민들에게 베이크아웃 방법을 안내합니다. 최근에는 IoT 기반 '스마트 베이크아웃' 시스템도 등장하여 온도·습도·공기질을 자동 제어합니다. 베이크아웃 시 주의할 점은 고온으로 인해 벽지 접착제가 녹거나 마루가 팽창할 수 있으므로 온도를 40도 이하로 유지하고, 가구를 들여놓기 전에 실시해야 한다는 것입니다. 베트남에서는 베이크아웃 개념이 거의 알려져 있지 않아, 베트남 근로자들이 '왜 난방을 틀어놓느냐'며 의아해하거나 전기 낭비로 여기는 경우가 있습니다. 통역 시 베이크아웃은 건강을 위한 과학적 방법이며, 입주 후 건강 문제를 예방하는 투자라는 점을 강조해야 합니다.",
        "commonMistakes": [
            {
                "mistake": "'베이크아웃'을 '굽기' 또는 'nướng'으로 직역",
                "correction": "베이크아웃은 고유명사로 'bake-out' 또는 '고온 환기법'으로 설명",
                "explanation": "요리 용어가 아니라 공기질 개선 기술 용어입니다."
            },
            {
                "mistake": "베이크아웃 시 창문을 계속 열어놓으라고 설명",
                "correction": "가열 시에는 밀폐, 가열 후 환기하는 반복 과정",
                "explanation": "가열과 환기를 반복해야 효과적입니다."
            },
            {
                "mistake": "겨울철에도 효과가 같다고 설명",
                "correction": "여름철(고온기)에 실시해야 효과 극대화",
                "explanation": "외부 온도가 높아야 실내 가열이 용이합니다."
            }
        ],
        "examples": [
            {
                "ko": "입주 2개월 전부터 베이크아웃을 실시하여 포름알데히드를 40% 감소시켰으며, 재측정 결과 기준치 이하를 확인했습니다.",
                "vi": "Đã thực hiện bake-out từ 2 tháng trước khi vào ở, giảm formaldehyd 40%, và kết quả đo lại xác nhận dưới tiêu chuẩn.",
                "situation": "formal"
            },
            {
                "ko": "베이크아웃 하려면 난방 30도로 틀고 2~3일 둔 다음, 창문 활짝 열어서 하루 환기하세요. 이걸 2주간 반복하면 됩니다.",
                "vi": "Để làm bake-out, bật sưởi 30 độ và để 2~3 ngày, sau đó mở toang cửa sổ thông gió 1 ngày. Lặp lại trong 2 tuần.",
                "situation": "onsite"
            },
            {
                "ko": "여름에 난방 틀라고? 베이크아웃이라는 거야. 냄새 빼는 거래.",
                "vi": "Bật sưởi mùa hè à? Gọi là bake-out. Để khử mùi đấy.",
                "situation": "informal"
            }
        ],
        "relatedTerms": [
            "포름알데히드",
            "VOC",
            "새집증후군",
            "환기",
            "공기질개선"
        ]
    },
    {
        "slug": "vat-lieu-than-thien-moi-truong",
        "korean": "친환경자재",
        "vietnamese": "Vật liệu thân thiện môi trường",
        "hanja": "親環境資材",
        "hanjaReading": "친(친할 친) + 환(고리 환) + 경(지경 경) + 자(재물 자) + 재(재목 재)",
        "pronunciation": "친환경자재",
        "meaningKo": "환경과 인체에 유해한 물질이 적거나 없는 건축자재로, 저VOC·저포름알데히드 제품, 재활용 자재, 자연 소재 등을 포함하며 '친환경 건축자재', '그린 자재', '에코 자재'라고도 불립니다. 통역 시 주의할 점은 한국에서는 '친환경 자재'가 일반적이지만 공식적으로는 '환경표지 인증 자재' 또는 '저방출 자재'라고 하며, 베트남어로는 'vật liệu thân thiện môi trường', 'vật liệu xanh' 또는 'vật liệu sinh thái'로 표현합니다. 친환경 자재는 한국환경산업기술원의 '환경표지(에코라벨)', 한국공기청정협회의 'HB(Healthy Building) 마크', 한국건설기술연구원의 '녹색건자재 인증' 등 공인 인증을 받아야 하며, 인증 기준은 포름알데히드·TVOC 방출량, 중금속 함량, 재활용률 등입니다. 최근에는 E0 등급(포름알데히드 0.3mg/L 이하), E1 등급(0.5mg/L 이하)처럼 유해 물질 방출 등급으로 분류하기도 합니다. 통역 시 친환경 자재는 일반 자재보다 가격이 10~30% 비싸지만 건강과 환경 보호에 필수이며, 특히 학교·병원·어린이집 등 민감 시설에서는 사용이 의무화되어 있다는 점을 명확히 전달해야 합니다.",
        "meaningVi": "Vật liệu thân thiện môi trường là vật liệu xây dựng ít hoặc không chứa chất độc hại cho môi trường và con người, bao gồm sản phẩm VOC thấp/formaldehyd thấp, vật liệu tái chế và vật liệu tự nhiên. Tại Hàn Quốc, vật liệu này phải được chứng nhận bởi các tổ chức uy tín như 'Nhãn môi trường' (Eco-label), 'Dấu HB' (Healthy Building), 'Chứng nhận vật liệu xây dựng xanh', với tiêu chuẩn về lượng phát thải formaldehyd/TVOC, hàm lượng kim loại nặng, tỷ lệ tái chế. Hiện nay phân loại theo cấp độ phát thải như E0 (formaldehyd ≤0,3mg/L), E1 (≤0,5mg/L).",
        "context": "친환경 건축, 학교·병원 시공, 실내공기질 개선, 녹색건축 인증",
        "culturalNote": "한국에서는 2000년대 후반부터 친환경 자재 사용이 확대되었으며, 특히 2010년 이후 녹색건축 인증제와 연계되어 가점을 받을 수 있어 건설사들이 적극 도입하고 있습니다. 아파트 분양 광고에서도 '친환경 자재 100% 사용', 'E0 등급 마루', '무VOC 페인트' 등을 주요 홍보 포인트로 사용합니다. 하지만 시중에는 인증 없이 '친환경'을 표방하는 제품도 많아, 실제 구매 시 인증 마크를 확인해야 합니다. 베트남에서는 친환경 자재가 고가 제품으로 인식되어 일반 프로젝트에서는 거의 사용하지 않는데, 한국에서는 법적 의무이거나 인증 요건인 경우가 많아 비용이 들더라도 사용해야 한다는 점을 명확히 해야 합니다. 통역 시 친환경 자재는 '값비싼 사치품'이 아니라 '근로자와 사용자 건강을 위한 필수 투자'임을 강조하고, 인증 마크 확인 방법도 함께 전달해야 합니다.",
        "commonMistakes": [
            {
                "mistake": "'친환경'을 단순 '자연 소재'로만 이해",
                "correction": "저방출·재활용·에너지 효율 등 다양한 기준 포함",
                "explanation": "친환경 자재는 자연 소재뿐 아니라 과학적 기준을 충족한 자재입니다."
            },
            {
                "mistake": "인증 없이 '친환경'이라고 표시된 제품 사용",
                "correction": "환경표지, HB 마크, 녹색건자재 인증 등 공인 인증 확인",
                "explanation": "인증 없는 제품은 친환경으로 인정받지 못합니다."
            },
            {
                "mistake": "친환경 자재는 선택 사항이라고 설명",
                "correction": "학교·병원 등 민감 시설에서는 법적 의무",
                "explanation": "일부 시설에서는 친환경 자재 사용이 필수입니다."
            }
        ],
        "examples": [
            {
                "ko": "이 학교 공사에는 환경표지 인증을 받은 E0 등급 친환경 자재만 사용하며, 페인트는 무VOC 제품을 적용합니다.",
                "vi": "Công trình trường học này chỉ sử dụng vật liệu thân thiện môi trường cấp E0 đã được chứng nhận Nhãn môi trường, và sơn là sản phẩm không VOC.",
                "situation": "formal"
            },
            {
                "ko": "합판 살 때 뒷면에 환경표지 마크 있는지 확인하세요. 그게 친환경 자재예요.",
                "vi": "Khi mua ván ép, kiểm tra mặt sau có dấu Nhãn môi trường không. Đó là vật liệu thân thiện môi trường.",
                "situation": "onsite"
            },
            {
                "ko": "친환경 자재 비싸네. 일반 거 쓰면 안 돼?",
                "vi": "Vật liệu thân thiện môi trường đắt nhỉ. Dùng loại thường không được à?",
                "situation": "informal"
            }
        ],
        "relatedTerms": [
            "E0등급",
            "환경표지",
            "녹색건자재",
            "HB마크",
            "저VOC"
        ]
    },
    {
        "slug": "cap-e0",
        "korean": "E0등급",
        "vietnamese": "Cấp E0",
        "hanja": None,
        "hanjaReading": None,
        "pronunciation": "이제로등급",
        "meaningKo": "합판, MDF, 파티클보드 등 목질 건축자재의 포름알데히드 방출량이 0.3mg/L 이하인 최고 등급으로, 'E0급', 'E제로급'이라고도 불립니다. 통역 시 주의할 점은 한국에서는 'E0(이제로)'로 발음하며, E1(0.5mg/L 이하), E2(5mg/L 이하) 등급도 있지만 E0이 가장 우수하며, 베트남어로는 'cấp E0', 'hạng E0' 또는 'loại E0'으로 표현합니다. E 등급은 유럽 기준(EN 13986)에서 유래한 것으로, 한국에서는 산업통상자원부 고시로 규정하고 있으며, 2010년 이후 친환경 건축 확산으로 E0 등급 자재 수요가 급증했습니다. E0 등급 자재는 일반(E1, E2) 자재보다 20~40% 비싸지만, 새집증후군 예방과 실내공기질 개선에 효과적이어서 아파트·학교·병원 등에서 선호합니다. 통역 시 E0 등급은 '포름알데히드 무방출'이 아니라 '초저방출'이며(완전 제로는 아님), 자재 구매 시 제품 뒷면이나 포장에 표기된 등급을 확인해야 한다는 점을 명확히 전달해야 합니다.",
        "meaningVi": "Cấp E0 là cấp độ cao nhất cho vật liệu gỗ công nghiệp như ván ép, MDF, ván dăm, với lượng phát thải formaldehyd dưới 0,3mg/L. Ngoài E0 còn có E1 (≤0,5mg/L) và E2 (≤5mg/L), nhưng E0 là tốt nhất. Tiêu chuẩn E xuất phát từ châu Âu (EN 13986) và được quy định bởi Bộ Thương mại và Công nghiệp Hàn Quốc. Vật liệu cấp E0 đắt hơn loại thường (E1, E2) khoảng 20~40% nhưng hiệu quả trong phòng hội chứng nhà mới và cải thiện chất lượng không khí, nên được ưa chuộng trong chung cư, trường học, bệnh viện.",
        "context": "친환경 건축, 실내 마감재 선정, 학교·병원 시공, 새집증후군 예방",
        "culturalNote": "한국에서는 E0 등급이 '프리미엄 자재'의 상징처럼 인식되며, 아파트 분양 광고에서 'E0 등급 마루', 'E0 등급 가구' 등을 강조합니다. 실제로 2010년대 이후 신축 아파트의 80% 이상이 E0 등급 마루와 붙박이장을 기본 사양으로 채택하고 있습니다. 하지만 E0 등급이라도 접착제나 마감재에서 포름알데히드가 나올 수 있으므로, 전체 자재가 E0 등급이어야 실내공기질이 우수합니다. 베트남에서는 E 등급 체계가 일반화되지 않아, 베트남 근로자들이 E0과 E1의 차이를 이해하지 못하거나 '비슷한 것'으로 여기는 경우가 있습니다. 통역 시 E0과 E1은 수치상 작은 차이지만 실내공기질에는 큰 영향을 미치며, 한국에서는 E1도 법적 기준이지만 건강을 위해 E0을 선호한다는 점을 강조해야 합니다.",
        "commonMistakes": [
            {
                "mistake": "'E0'을 '영제로' 또는 '영영'으로 발음",
                "correction": "정확한 발음은 '이제로'",
                "explanation": "한국에서는 E0을 '이제로'로 발음합니다."
            },
            {
                "mistake": "E0 등급은 포름알데히드가 완전히 없다고 설명",
                "correction": "0.3mg/L 이하의 '초저방출'로 설명",
                "explanation": "완전 제로가 아니라 매우 낮은 수준입니다."
            },
            {
                "mistake": "E0과 E1의 차이를 무시",
                "correction": "E0(0.3mg/L)과 E1(0.5mg/L)의 차이와 중요성 설명",
                "explanation": "수치 차이가 작아 보이지만 건강에는 유의미한 차이입니다."
            }
        ],
        "examples": [
            {
                "ko": "이 아파트는 전 세대 E0 등급 강화마루와 붙박이장을 적용하여 포름알데히드 방출을 최소화했습니다.",
                "vi": "Chung cư này sử dụng sàn gỗ công nghiệp cấp E0 và tủ âm tường cấp E0 cho tất cả căn hộ, giảm thiểu phát thải formaldehyd.",
                "situation": "formal"
            },
            {
                "ko": "합판 주문할 때 E0 등급으로 달라고 하세요. 제품에 E0 마크 찍혀 있는지 확인하고요.",
                "vi": "Khi đặt ván ép, yêu cầu cấp E0. Kiểm tra xem có dấu E0 trên sản phẩm không.",
                "situation": "onsite"
            },
            {
                "ko": "E0이랑 E1이 뭐가 다른데? 그냥 싼 거 쓰면 안 돼?",
                "vi": "E0 với E1 khác gì? Dùng loại rẻ không được à?",
                "situation": "informal"
            }
        ],
        "relatedTerms": [
            "E1등급",
            "포름알데히드",
            "친환경자재",
            "강화마루",
            "합판"
        ]
    },
    {
        "slug": "chung-nhan-vat-lieu-xay-dung-xanh",
        "korean": "녹색건자재인증",
        "vietnamese": "Chứng nhận vật liệu xây dựng xanh",
        "hanja": "綠色建資材認證",
        "hanjaReading": "록(푸를 록) + 색(빛 색) + 건(세울 건) + 자(재물 자) + 재(재목 재) + 인(알 인) + 증(증거 증)",
        "pronunciation": "녹색건자재인증",
        "meaningKo": "한국건설기술연구원(KICT)이 환경 영향을 최소화하고 자원 순환성이 우수한 건축자재에 부여하는 친환경 인증으로, 'G-SEED 자재 인증', '그린 자재 인증'이라고도 불립니다. 통역 시 주의할 점은 한국에서는 '녹색건자재 인증'이 공식 용어이지만 현장에서는 '그린 자재 마크', '녹색 인증'이라고도 하며, 베트남어로는 'chứng nhận vật liệu xây dựng xanh', 'chứng nhận vật liệu sinh thái' 또는 'chứng nhận G-SEED vật liệu'로 표현합니다. 녹색건자재 인증은 자재의 전 생애주기(생산·운송·사용·폐기)를 평가하며, 평가 항목에는 유해 물질 저감(포름알데히드, VOC, 중금속 등), 재활용률, 탄소 배출량, 에너지 효율, 내구성 등이 포함됩니다. 인증 등급은 최우수, 우수, 일반 3단계로 나뉘며, 녹색건축 인증(G-SEED) 건물을 지을 때 녹색건자재를 사용하면 가점을 받습니다. 통역 시 녹색건자재 인증은 '환경표지(에코라벨)'와는 다른 제도이며(환경표지는 환경부, 녹색건자재는 국토부), 건설 프로젝트에서는 두 인증을 모두 활용한다는 점을 명확히 전달해야 합니다.",
        "meaningVi": "Chứng nhận vật liệu xây dựng xanh là chứng nhận thân thiện môi trường do Viện Nghiên cứu Công nghệ Xây dựng Hàn Quốc (KICT) cấp cho vật liệu xây dựng giảm thiểu tác động môi trường và có tính tuần hoàn tài nguyên cao. Chứng nhận này đánh giá toàn bộ vòng đời vật liệu (sản xuất, vận chuyển, sử dụng, thải bỏ), với các tiêu chí như giảm chất độc hại (formaldehyd, VOC, kim loại nặng), tỷ lệ tái chế, phát thải carbon, hiệu quả năng lượng, độ bền. Có 3 cấp: Xuất sắc, Tốt, Thông thường. Khi xây dựng công trình được chứng nhận xanh (G-SEED), sử dụng vật liệu chứng nhận xanh sẽ được cộng điểm.",
        "context": "녹색건축 프로젝트, 친환경 자재 선정, G-SEED 인증, 공공 건축물",
        "culturalNote": "한국에서는 2010년 이후 녹색건축 확산 정책에 따라 공공 건축물(학교, 관공서 등)은 의무적으로 일정 비율 이상 녹색건자재를 사용해야 하며, 민간 건축물도 녹색건축 인증을 받으려면 녹색건자재 사용이 필수입니다. 녹색건자재 인증 제품은 한국건설기술연구원 홈페이지에서 검색 가능하며, 제품 포장에 '녹색건자재 인증' 마크가 부착됩니다. 하지만 인증받지 않은 제품도 '친환경', '에코' 등의 용어를 사용하는 경우가 많아, 실제 구매 시 인증 번호를 확인해야 합니다. 베트남에서는 녹색건자재 인증 개념이 생소하여, 베트남 근로자들이 인증 마크를 확인하지 않고 '친환경'이라고 표기된 제품을 그대로 사용하는 경우가 있습니다. 통역 시 녹색건자재 인증은 정부가 검증한 공식 인증이므로 반드시 인증 마크를 확인해야 하며, 미인증 제품 사용 시 녹색건축 인증을 받을 수 없다는 점을 강조해야 합니다.",
        "commonMistakes": [
            {
                "mistake": "환경표지 인증과 녹색건자재 인증을 같은 것으로 설명",
                "correction": "환경표지는 환경부, 녹색건자재는 국토부 인증으로 구분",
                "explanation": "두 인증은 발급 기관과 평가 기준이 다릅니다."
            },
            {
                "mistake": "'친환경' 표기만 보고 녹색건자재로 판단",
                "correction": "공식 인증 마크와 인증 번호 확인 필수",
                "explanation": "인증 없이 친환경을 표방하는 제품이 많아 확인이 필요합니다."
            },
            {
                "mistake": "녹색건자재 사용이 선택 사항이라고 설명",
                "correction": "공공 건축물 및 녹색건축 인증 시 의무 사항",
                "explanation": "일부 프로젝트에서는 녹색건자재 사용이 법적 의무입니다."
            }
        ],
        "examples": [
            {
                "ko": "이 학교 신축 공사는 녹색건축 최우수 등급을 목표로 하므로, 모든 자재는 녹색건자재 인증을 받은 제품으로 사용해야 합니다.",
                "vi": "Công trình xây trường học này nhắm đến cấp Xuất sắc chứng nhận xanh, nên tất cả vật liệu phải là sản phẩm đã được chứng nhận vật liệu xây dựng xanh.",
                "situation": "formal"
            },
            {
                "ko": "자재 납품 시 녹색건자재 인증서 사본을 같이 제출하세요. 인증 번호도 확인할 거예요.",
                "vi": "Khi giao vật liệu, nộp kèm bản sao giấy chứng nhận vật liệu xây dựng xanh. Sẽ kiểm tra số chứng nhận.",
                "situation": "onsite"
            },
            {
                "ko": "이거 녹색건자재 맞아? 마크 안 보이는데.",
                "vi": "Cái này đúng là vật liệu xây dựng xanh không? Không thấy dấu chứng nhận.",
                "situation": "informal"
            }
        ],
        "relatedTerms": [
            "G-SEED",
            "친환경자재",
            "환경표지",
            "녹색건축",
            "에코라벨"
        ]
    }
]

# 파일 경로
project_root = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
construction_file = os.path.join(project_root, "src", "data", "terms", "construction.json")

def main():
    """메인 실행 함수 (실행 금지)"""
    print("⚠️ 이 스크립트는 실행하지 마세요.")
    print("데이터 검토 후 수동으로 construction.json에 추가하세요.")
    print(f"\n추가할 용어 수: {len(data)}개")
    print("\n용어 목록:")
    for i, term in enumerate(data, 1):
        print(f"{i}. {term['korean']} ({term['slug']})")

if __name__ == "__main__":
    # 실행 금지 - 데이터만 저장
    pass
