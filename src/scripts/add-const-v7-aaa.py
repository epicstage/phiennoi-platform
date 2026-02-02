#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
건설 용어 추가 스크립트 - 지반조사/시험장비 테마
테마: 보링, SPT, CPT, 시추기, 시료채취, 지질주상도, 탄성파탐사, 전기비저항, 지하수위측정, 현장투수시험
"""

import json
import os

# 추가할 용어 데이터 (10개)
data = [
    {
        "slug": "khoan-dia-chat",
        "korean": "보링",
        "vietnamese": "Khoan địa chất",
        "hanja": "Boring",
        "hanjaReading": None,
        "pronunciation": "보링",
        "meaningKo": "지반조사를 위해 지중에 구멍을 뚫어 토질 및 암반의 상태를 파악하는 작업입니다. 통역 시 '시추'와 혼동되기 쉬우나, 보링은 주로 지질조사 목적의 작은 직경 천공을 의미하며, 시추는 석유·가스 등 자원 채취를 위한 대규모 굴착을 가리킵니다. 베트남 현장에서는 'khoan khảo sát'(조사용 천공)와 'khoan khai thác'(채취용 천공)을 명확히 구분해야 하며, 건설 현장에서는 전자를 사용합니다. 보링 깊이, 간격, 위치는 구조물 중요도에 따라 달라지므로 설계도면과 지질조사 계획서를 반드시 함께 검토해야 합니다.",
        "meaningVi": "Khoan địa chất là công tác khoan lỗ trong lòng đất để khảo sát tình trạng địa tầng, đất đá phục vụ thiết kế công trình. Khoan địa chất thường có đường kính nhỏ (76-150mm) và sâu từ 10-50m tùy loại công trình. Kỹ thuật khoan bao gồm khoan quay, khoan xoay, khoan ép để lấy mẫu nguyên trạng phục vụ thí nghiệm trong phòng.",
        "context": "지질조사, 기초설계, 토질시험",
        "culturalNote": "한국은 보링 작업 시 안전관리가 매우 엄격하여 작업 전 주변 지하매설물(상하수도, 전기, 통신) 조사를 필수로 하며, 베트남은 상대적으로 매설물 관리가 미흡해 사고 위험이 높습니다. 한국 현장에서는 보링 위치 변경 시 감리와 설계자 승인이 필요하지만, 베트남에서는 현장 판단으로 임의 변경하는 경우가 많아 통역사는 이러한 절차 차이를 명확히 전달해야 합니다. 또한 한국은 보링 후 공내재(grouting)를 통해 지반 교란을 복구하지만, 베트남은 이를 생략하는 경우가 많습니다.",
        "commonMistakes": [
            {
                "mistake": "보링을 'khoan dầu khí'(석유 시추)로 번역",
                "correction": "'khoan địa chất' 또는 'khoan khảo sát' 사용",
                "explanation": "건설 현장의 보링은 지질조사 목적이므로 석유·가스 시추와 구분해야 함"
            },
            {
                "mistake": "'보링머신'을 'máy khoan'으로만 번역",
                "correction": "'máy khoan địa chất' 또는 'máy khoan khảo sát địa tầng'",
                "explanation": "일반 천공기와 지질조사용 보링머신은 장비 사양과 목적이 다름"
            },
            {
                "mistake": "보링 깊이를 'm'로만 표기",
                "correction": "깊이와 함께 지하수위, 암반 출현 깊이 정보 병기",
                "explanation": "베트남 기술자는 보링 결과의 맥락 정보를 중요하게 여김"
            }
        ],
        "examples": [
            {
                "ko": "이 부지는 지하수위가 높아 보링 작업 시 케이싱 설치가 필수입니다.",
                "vi": "Khu vực này có mực nước ngầm cao nên phải lắp casing khi khoan địa chất.",
                "situation": "onsite"
            },
            {
                "ko": "보링 간격은 구조물 규모에 따라 15~30m로 조정하겠습니다.",
                "vi": "Khoảng cách giữa các lỗ khoan sẽ điều chỉnh từ 15-30m tùy theo quy mô công trình.",
                "situation": "formal"
            },
            {
                "ko": "보링 시료는 냉장 보관 후 48시간 내 실험실로 운반해 주세요.",
                "vi": "Mẫu khoan phải bảo quản lạnh và vận chuyển đến phòng thí nghiệm trong 48 giờ.",
                "situation": "onsite"
            }
        ],
        "relatedTerms": ["시추", "지질조사", "코어 샘플링", "SPT", "지하수위"]
    },
    {
        "slug": "thi-nghiem-xuyên-chuan-spt",
        "korean": "표준관입시험",
        "vietnamese": "Thí nghiệm xuyên chuẩn SPT",
        "hanja": "標準貫入試驗",
        "hanjaReading": "標(표 표) + 準(준할 준) + 貫(꿰뚫을 관) + 入(들 입) + 試(시험할 시) + 驗(시험할 험)",
        "pronunciation": "표준관입시험",
        "meaningKo": "Standard Penetration Test의 약자로, 63.5kg 해머를 76cm 높이에서 자유낙하시켜 샘플러를 30cm 관입하는 데 필요한 타격 횟수(N값)를 측정하는 지반조사 시험입니다. 통역 시 'N값'은 베트남어로 'chỉ số N' 또는 'giá trị SPT'로 표현하며, 이 값이 클수록 지반이 단단함을 의미합니다. 한국에서는 N값 50 이상을 지지층으로 간주하는 경우가 많으나, 베트남 기준은 다를 수 있어 설계기준을 명확히 확인해야 합니다. SPT 결과는 기초 형식 선정, 지내력 산정, 액상화 평가에 직접 활용되므로 통역 시 수치의 정확성이 매우 중요합니다.",
        "meaningVi": "Thí nghiệm xuyên chuẩn SPT là phương pháp thí nghiệm hiện trường đo chỉ số SPT-N bằng cách đếm số nhát búa (63.5kg rơi từ độ cao 76cm) cần thiết để xuyên ống lấy mẫu sâu 30cm vào đất. Chỉ số N càng lớn thì đất càng chặt, được dùng để đánh giá sức chịu tải và khả năng hóa lỏng của nền đất.",
        "context": "지질조사, 기초설계, 지내력 평가",
        "culturalNote": "한국은 SPT를 거의 모든 건설 현장에서 필수로 시행하며, 1.5m 간격으로 빠짐없이 측정하는 것이 일반적이지만, 베트남은 예산 제약으로 3~5m 간격으로 실시하는 경우가 많아 데이터 신뢰도 차이가 발생합니다. 한국 기술자는 N값을 절대적 기준으로 삼는 경향이 있으나, 베트남 지반공학자는 CPT, 실내시험 등 다른 시험 결과와 종합적으로 판단하는 경우가 많습니다. 또한 한국은 SPT 장비 검교정을 정기적으로 하지만, 베트남은 이를 소홀히 하는 경우가 있어 결과값 편차가 클 수 있습니다.",
        "commonMistakes": [
            {
                "mistake": "'N값 30'을 'giá trị N ba mươi'로 직역",
                "correction": "'chỉ số SPT-N bằng 30' 또는 'N=30'",
                "explanation": "베트남에서는 'chỉ số SPT-N'이 정식 표현이며, 단순 숫자 나열은 혼동 유발"
            },
            {
                "mistake": "SPT를 'thí nghiệm đâm xuyên'으로 번역",
                "correction": "'thí nghiệm xuyên chuẩn SPT' 전체 명칭 사용",
                "explanation": "'đâm xuyên'은 관입의 일반 용어이며, SPT는 표준화된 시험이므로 고유명 유지"
            },
            {
                "mistake": "'관입 깊이'를 'độ sâu xuyên'으로만 표기",
                "correction": "'độ sâu xuyên 30cm cho mỗi lần đo'",
                "explanation": "SPT는 30cm 단위 측정이 핵심이므로 이를 명시해야 함"
            }
        ],
        "examples": [
            {
                "ko": "이 지점의 SPT N값이 50 이상이므로 직접기초 적용이 가능합니다.",
                "vi": "Điểm này có chỉ số SPT-N trên 50 nên có thể áp dụng móng trực tiếp.",
                "situation": "formal"
            },
            {
                "ko": "GL-3m에서 N값이 급격히 증가하는데, 암반 출현으로 보입니다.",
                "vi": "Tại độ sâu GL-3m, chỉ số N tăng đột ngột, có thể do xuất hiện lớp đá gốc.",
                "situation": "onsite"
            },
            {
                "ko": "SPT 시험은 1.5m 간격으로 지지층까지 실시해 주세요.",
                "vi": "Thí nghiệm SPT thực hiện cách 1.5m cho đến khi gặp tầng chịu lực.",
                "situation": "formal"
            }
        ],
        "relatedTerms": ["N값", "지지층", "CPT", "지내력", "액상화"]
    },
    {
        "slug": "thi-nghiem-xuyên-hinh-non-cpt",
        "korean": "콘관입시험",
        "vietnamese": "Thí nghiệm xuyên hình nón CPT",
        "hanja": None,
        "hanjaReading": None,
        "pronunciation": "콘관입시험",
        "meaningKo": "Cone Penetration Test의 약자로, 원추형 콘을 일정 속도(2cm/초)로 지중에 압입하여 선단저항(qc)과 주면마찰력(fs)을 연속 측정하는 지반조사 시험입니다. 통역 시 'cone'은 '콘' 또는 '원추'로 표현하며, qc는 'sức kháng mũi nón', fs는 'ma sát thành bên'으로 번역합니다. SPT보다 연속적인 데이터를 얻을 수 있어 얇은 연약층 감지에 유리하며, 한국에서는 고속도로나 항만 등 대형 토목 현장에서 많이 사용합니다. 베트남에서는 장비 보급이 적어 SPT를 더 선호하는 경향이 있으나, 최근 정밀 조사가 필요한 프로젝트에서 CPT 활용이 증가하고 있습니다.",
        "meaningVi": "Thí nghiệm xuyên hình nón CPT là phương pháp ép mũi nón tiêu chuẩn vào đất với tốc độ 2cm/giây và đo liên tục sức kháng mũi nón (qc) và ma sát thành bên (fs). CPT cho kết quả liên tục theo chiều sâu, giúp phát hiện lớp yếu mỏng và đánh giá chi tiết đặc tính nền đất mà SPT không thể cung cấp.",
        "context": "지질조사, 연약지반, 항만공사",
        "culturalNote": "한국은 CPT 장비와 해석 기술이 발달하여 간극수압(u) 측정이 가능한 CPTu를 많이 사용하며, 실시간 데이터 분석 시스템을 갖추고 있습니다. 반면 베트남은 CPT 장비가 고가여서 보급률이 낮고, 대부분 기계식 CPT를 사용하며 데이터 해석 경험이 부족한 경우가 많습니다. 한국 기술자는 CPT 결과를 토질 분류, 지내력 산정에 직접 활용하지만, 베트남 기술자는 참고 자료로만 활용하는 경향이 있어 통역 시 데이터 활용 방식의 차이를 명확히 전달해야 합니다.",
        "commonMistakes": [
            {
                "mistake": "'콘'을 'hình côn'(기하학적 원뿔)으로 번역",
                "correction": "'mũi nón' 또는 'đầu nón' 사용",
                "explanation": "지반공학에서는 시험 장비의 '콘'을 'mũi nón'으로 특정함"
            },
            {
                "mistake": "'qc값'을 'giá trị qc'로만 표기",
                "correction": "'sức kháng mũi nón qc' 또는 'chỉ số qc'",
                "explanation": "물리적 의미(선단저항)를 포함하는 표현이 이해도를 높임"
            },
            {
                "mistake": "CPT와 SPT를 '같은 목적의 시험'으로 설명",
                "correction": "CPT는 연속 데이터, SPT는 이산 데이터 제공으로 목적 다름",
                "explanation": "두 시험의 장단점과 적용 분야가 다르므로 명확히 구분 필요"
            }
        ],
        "examples": [
            {
                "ko": "이 구간은 CPT로 연속 측정하여 연약층 분포를 정밀 파악하겠습니다.",
                "vi": "Đoạn này sẽ dùng CPT đo liên tục để xác định chính xác phân bố lớp đất yếu.",
                "situation": "formal"
            },
            {
                "ko": "qc값이 급격히 떨어지는 GL-5m 구간에 연약층이 협재된 것으로 판단됩니다.",
                "vi": "Tại độ sâu GL-5m có sức kháng mũi nón qc giảm đột ngột, có lớp yếu xen kẹp.",
                "situation": "onsite"
            },
            {
                "ko": "CPT 시험은 20m 깊이까지 연속으로 진행하며, 데이터는 실시간 기록됩니다.",
                "vi": "Thí nghiệm CPT thực hiện liên tục đến 20m, dữ liệu ghi nhận theo thời gian thực.",
                "situation": "formal"
            }
        ],
        "relatedTerms": ["SPT", "선단저항", "주면마찰력", "연약층", "지반조사"]
    },
    {
        "slug": "may-khoan-dia-chat",
        "korean": "시추기",
        "vietnamese": "Máy khoan địa chất",
        "hanja": "試錐機",
        "hanjaReading": "試(시험할 시) + 錐(송곳 추) + 機(기계 기)",
        "pronunciation": "시추기",
        "meaningKo": "지반조사를 위해 지중에 구멍을 뚫는 기계 장비로, 로터리식, 충격식, 오거식 등 다양한 방식이 있습니다. 통역 시 'máy khoan'만 사용하면 일반 천공기와 혼동될 수 있으므로 반드시 'máy khoan địa chất' 또는 'máy khoan khảo sát'로 명확히 구분해야 합니다. 한국 현장에서는 시추기 용량을 '굴착 깊이'와 '코어 직경'으로 표기하는데, 베트남에서는 '엔진 마력'으로 표기하는 경우가 많아 사양 확인 시 주의가 필요합니다. 시추기 선정은 지질 조건(토사/풍화암/경암)에 따라 달라지므로 지질 정보를 통역 시 정확히 전달해야 합니다.",
        "meaningVi": "Máy khoan địa chất là thiết bị dùng để tạo lỗ khoan trong đất đá nhằm lấy mẫu và khảo sát địa tầng. Các loại máy khoan phổ biến: khoan quay (rotary), khoan xoay (percussion), khoan vít (auger). Máy khoan được chọn dựa trên điều kiện địa chất (đất, đá phong hóa, đá gốc) và độ sâu yêu cầu.",
        "context": "지질조사, 보링 작업, 코어 채취",
        "culturalNote": "한국은 시추기 안전 기준이 엄격하여 작업 전 안전교육, 장비 점검 체크리스트 작성이 의무이며, 전도 방지를 위한 아웃리거 설치가 필수입니다. 베트남 현장에서는 이러한 안전 절차가 생략되는 경우가 많아 사고 위험이 높으며, 특히 경사지에서의 시추기 전도 사고가 빈번합니다. 한국 업체는 유압식 최신 장비를 사용하지만, 베트남 로컬 업체는 구식 수동 장비를 사용하는 경우가 많아 작업 속도와 품질에 차이가 발생합니다. 통역사는 장비 사양 논의 시 한국과 베트남의 장비 수준 차이를 고려해야 합니다.",
        "commonMistakes": [
            {
                "mistake": "'시추기'를 'máy khoan dầu'(석유 시추기)로 번역",
                "correction": "'máy khoan địa chất' 또는 'máy khoan khảo sát'",
                "explanation": "건설 현장의 시추기는 지질조사용이므로 석유 채굴용과 구분해야 함"
            },
            {
                "mistake": "'로터리식'을 'kiểu quay'로만 번역",
                "correction": "'máy khoan quay thủy lực' (유압 로터리식)",
                "explanation": "구동 방식(유압/기계)까지 명시해야 정확한 사양 전달"
            },
            {
                "mistake": "시추기 용량을 '톤'으로 표기",
                "correction": "'굴착 가능 깊이(m)'와 '코어 직경(mm)'으로 표기",
                "explanation": "시추기 성능은 무게가 아닌 굴착 능력으로 평가함"
            }
        ],
        "examples": [
            {
                "ko": "이 현장은 암반이 얕게 나와서 로터리식 시추기가 필요합니다.",
                "vi": "Công trường này có đá gốc nông nên cần máy khoan quay thủy lực.",
                "situation": "onsite"
            },
            {
                "ko": "시추기 세팅 전에 지하매설물 탐사를 먼저 진행해 주세요.",
                "vi": "Trước khi dựng máy khoan, hãy khảo sát đường ống ngầm trước.",
                "situation": "onsite"
            },
            {
                "ko": "이 시추기는 50m 깊이까지 NX 코어 채취가 가능합니다.",
                "vi": "Máy khoan này có thể lấy mẫu lõi NX đến độ sâu 50m.",
                "situation": "formal"
            }
        ],
        "relatedTerms": ["보링", "코어 샘플링", "로터리 드릴", "지질조사", "천공"]
    },
    {
        "slug": "lay-mau-dat",
        "korean": "시료채취",
        "vietnamese": "Lấy mẫu đất",
        "hanja": "試料採取",
        "hanjaReading": "試(시험할 시) + 料(헤아릴 료) + 採(캘 채) + 取(가질 취)",
        "pronunciation": "시료채취",
        "meaningKo": "지반조사 과정에서 토질 및 암반 시료를 채취하여 실내시험을 수행하는 작업입니다. 통역 시 '교란 시료'는 'mẫu xáo trộn', '불교란 시료'는 'mẫu nguyên trạng'으로 구분하며, 불교란 시료는 원지반의 구조를 유지한 상태로 채취해야 하므로 특수 샘플러(thin-wall tube, piston sampler)를 사용합니다. 한국 기준에서는 구조물 중요도에 따라 불교란 시료 채취 간격이 규정되어 있으며, 일반적으로 5~10m마다 1개씩 채취합니다. 시료는 채취 즉시 밀봉·냉장 보관해야 하며, 48시간 이내 실험실로 운반하는 것이 원칙입니다.",
        "meaningVi": "Lấy mẫu đất là công tác thu thập mẫu đất đá từ hiện trường để thí nghiệm trong phòng. Có hai loại mẫu: mẫu xáo trộn (cấu trúc bị phá hủy) và mẫu nguyên trạng (giữ nguyên cấu trúc tự nhiên). Mẫu nguyên trạng được lấy bằng ống lấy mẫu thành mỏng hoặc piston, cần bảo quản kín và vận chuyển trong 48 giờ đến phòng thí nghiệm.",
        "context": "지질조사, 토질시험, 실내실험",
        "culturalNote": "한국은 시료채취 절차가 매우 체계적이며, 시료마다 고유 번호를 부여하고 채취 위치·깊이·시간·담당자를 야장에 상세히 기록합니다. 시료 운반 시 충격 방지를 위한 전용 케이스를 사용하며, 냉장 트럭으로 운송합니다. 베트남은 이러한 절차가 간소화되어 시료 라벨링이 부실하거나 상온 운반하는 경우가 많아 시료 품질 저하 우려가 있습니다. 한국 실험실은 시료 입고 즉시 육안 관찰 후 사진 촬영하여 기록하지만, 베트남은 이를 생략하는 경우가 많습니다. 통역사는 시료 품질 관리의 중요성을 강조해야 합니다.",
        "commonMistakes": [
            {
                "mistake": "'불교란 시료'를 'mẫu không bị xáo trộn'으로 직역",
                "correction": "'mẫu nguyên trạng' 사용",
                "explanation": "베트남 지반공학 표준 용어는 'mẫu nguyên trạng'"
            },
            {
                "mistake": "'샘플러'를 'máy lấy mẫu'로 번역",
                "correction": "'ống lấy mẫu' 또는 'bộ lấy mẫu' 사용",
                "explanation": "샘플러는 독립 기계가 아닌 시추기에 부착되는 도구임"
            },
            {
                "mistake": "시료 크기를 '길이×직경'만 표기",
                "correction": "시료 종류(교란/불교란)와 보관 방법도 함께 명시",
                "explanation": "시료 취급 방법이 실험 결과의 신뢰도에 직접 영향"
            }
        ],
        "examples": [
            {
                "ko": "GL-8m에서 불교란 시료를 thin-wall tube로 채취해 주세요.",
                "vi": "Tại GL-8m, lấy mẫu nguyên trạng bằng ống thành mỏng thin-wall.",
                "situation": "onsite"
            },
            {
                "ko": "점성토 시료는 밀봉 후 냉장 보관하여 수분 손실을 방지해야 합니다.",
                "vi": "Mẫu đất sét phải bọc kín và bảo quản lạnh để tránh mất độ ẩm.",
                "situation": "formal"
            },
            {
                "ko": "이 시료는 압밀시험용이므로 교란되지 않게 각별히 주의해 주세요.",
                "vi": "Mẫu này dùng cho thí nghiệm nén lún nên phải cẩn thận không làm xáo trộn.",
                "situation": "onsite"
            }
        ],
        "relatedTerms": ["불교란 시료", "교란 시료", "샘플러", "실내시험", "보링"]
    },
    {
        "slug": "bieu-do-dia-tang",
        "korean": "지질주상도",
        "vietnamese": "Biểu đồ địa tầng",
        "hanja": "地質柱狀圖",
        "hanjaReading": "地(땅 지) + 質(바탕 질) + 柱(기둥 주) + 狀(모양 상) + 圖(그림 도)",
        "pronunciation": "지질주상도",
        "meaningKo": "보링 결과를 바탕으로 지층의 깊이별 토질·암질 구성을 기둥 형태로 도식화한 자료입니다. 통역 시 '주상도'는 'biểu đồ cột' 또는 'biểu đồ trụ'로 표현할 수 있으나, 지질 분야에서는 관습적으로 'biểu đồ địa tầng'을 사용합니다. 주상도에는 토층 구분, SPT N값, 지하수위, 암반 출현 깊이, 시료 채취 위치 등이 표기되며, 이는 기초 설계의 핵심 자료가 됩니다. 한국 설계사는 주상도를 CAD로 정교하게 작성하지만, 베트남은 손그림이나 간단한 스케치인 경우가 많아 정보의 정확도와 가독성에 차이가 있습니다.",
        "meaningVi": "Biểu đồ địa tầng là tài liệu thể hiện cấu trúc các lớp đất đá theo chiều sâu dựa trên kết quả khoan khảo sát, có dạng cột dọc. Biểu đồ bao gồm phân tầng đất, chỉ số SPT-N, mực nước ngầm, độ sâu xuất hiện đá gốc, vị trí lấy mẫu. Đây là tài liệu cơ bản để thiết kế móng công trình.",
        "context": "지질조사, 기초설계, 설계보고서",
        "culturalNote": "한국은 지질주상도를 법정 문서로 간주하여 작성자의 서명·날인이 필수이며, 표기 방식이 KS 기준으로 표준화되어 있습니다. 토층 색상은 Munsell 토색첩으로 정확히 구분하고, 지하수위는 측정 시간과 함께 기록합니다. 베트남은 주상도 작성 기준이 느슨하여 작성자마다 표기 방식이 다르고, 토층 구분이 주관적인 경우가 많습니다. 한국 기술자는 주상도의 세밀한 정보를 중시하지만, 베트남 기술자는 큰 틀의 지층 구성만 파악하는 경향이 있어 통역 시 정보의 정밀도에 대한 기대치 차이를 조정해야 합니다.",
        "commonMistakes": [
            {
                "mistake": "'주상도'를 'sơ đồ cột'(단순 기둥 그림)로 번역",
                "correction": "'biểu đồ địa tầng' 또는 'biểu đồ khoan' 사용",
                "explanation": "지질 전문 용어로서의 고유 표현을 유지해야 함"
            },
            {
                "mistake": "토층 두께를 'm'만 표기하고 GL 기준 불명확",
                "correction": "'từ GL-2m đến GL-5m' 형식으로 명확한 범위 표기",
                "explanation": "베트남 기술자는 지표면(GL) 기준 깊이를 명확히 선호"
            },
            {
                "mistake": "N값을 주상도 외부 별도 표로 제공",
                "correction": "주상도 내 각 토층 옆에 N값 직접 표기",
                "explanation": "베트남 관행은 주상도와 N값을 하나의 도면에 통합"
            }
        ],
        "examples": [
            {
                "ko": "지질주상도를 보면 GL-3m부터 풍화암이 나타나는데, 기초 형식을 다시 검토해야 할 것 같습니다.",
                "vi": "Theo biểu đồ địa tầng, từ GL-3m xuất hiện đá phong hóa, cần xem xét lại loại móng.",
                "situation": "formal"
            },
            {
                "ko": "각 보링공의 주상도를 나란히 배치하여 지층 변화를 단면으로 표현해 주세요.",
                "vi": "Hãy sắp xếp biểu đồ địa tầng các lỗ khoan cạnh nhau để thể hiện biến đổi địa tầng theo mặt cắt.",
                "situation": "formal"
            },
            {
                "ko": "이 주상도에서 지하수위가 GL-2.5m인데, 우기 시 더 상승할 수 있습니다.",
                "vi": "Biểu đồ này có mực nước ngầm ở GL-2.5m, nhưng mùa mưa có thể dâng cao hơn.",
                "situation": "onsite"
            }
        ],
        "relatedTerms": ["보링", "토층", "SPT", "지하수위", "지질조사"]
    },
    {
        "slug": "tham-do-song-dia-chan",
        "korean": "탄성파탐사",
        "vietnamese": "Thăm dò sóng địa chấn",
        "hanja": "彈性波探査",
        "hanjaReading": "彈(탄력 탄) + 性(성품 성) + 波(물결 파) + 探(찾을 탐) + 査(살필 사)",
        "pronunciation": "탄성파탐사",
        "meaningKo": "지중에 인공적인 충격을 가하여 발생한 탄성파가 지층 경계면에서 반사·굴절되어 돌아오는 시간을 측정함으로써 지하 구조를 탐사하는 물리탐사 기법입니다. 통역 시 'seismic survey'를 'thăm dò địa chấn'으로 표현하며, P파(종파)는 'sóng dọc', S파(횡파)는 'sóng ngang'으로 구분합니다. 탄성파탐사는 넓은 면적의 지층 구조를 빠르게 파악할 수 있어 터널, 댐, 도로 등 선형 구조물 건설 시 사전조사에 많이 활용됩니다. 한국에서는 굴절법과 반사법을 병행하는 경우가 많으나, 베트남은 장비와 분석 기술 부족으로 단순 굴절법만 사용하는 경우가 많습니다.",
        "meaningVi": "Thăm dò sóng địa chấn là phương pháp khảo sát vật lý bằng cách tạo chấn động nhân tạo (búa, nổ mìn) và đo thời gian sóng đàn hồi truyền qua các lớp đất đá để xác định cấu trúc địa chất dưới mặt đất. Phương pháp này giúp phát hiện ranh giới địa tầng, đá gốc, đới sụt lún mà không cần khoan nhiều lỗ.",
        "context": "지질조사, 터널공사, 대규모 토목",
        "culturalNote": "한국은 탄성파탐사를 정밀 지질조사의 표준 기법으로 인식하여 전문 장비와 소프트웨어(SeisImager, Rayfract 등)를 갖춘 전문 업체가 많으며, 데이터 해석에 지구물리학 전문가가 참여합니다. 베트남은 탄성파탐사 장비가 고가이고 전문 인력이 부족하여 대형 프로젝트(수력발전, 고속도로)에만 제한적으로 사용되며, 대부분 외국 업체에 의뢰합니다. 한국 기술자는 탄성파 속도 분포도를 세밀하게 분석하지만, 베트남 기술자는 개략적인 암반 심도 파악에만 활용하는 경향이 있습니다. 통역 시 탐사 결과의 활용 목적을 명확히 해야 합니다.",
        "commonMistakes": [
            {
                "mistake": "'탄성파'를 'sóng đàn hồi'로만 번역하고 P파/S파 구분 없음",
                "correction": "'sóng dọc P' (P파), 'sóng ngang S' (S파) 명확히 구분",
                "explanation": "두 파의 전파 속도와 특성이 다르므로 구분 필수"
            },
            {
                "mistake": "'굴절법'을 'phương pháp gấp khúc'으로 직역",
                "correction": "'phương pháp khúc xạ' 사용",
                "explanation": "물리학 용어는 정식 학술 표현 사용"
            },
            {
                "mistake": "탐사 깊이를 '심도'로만 표기",
                "correction": "'độ sâu thăm dò tối đa' (최대 탐사 깊이) 명시",
                "explanation": "탄성파탐사는 탐사 가능 깊이에 한계가 있음을 분명히 해야 함"
            }
        ],
        "examples": [
            {
                "ko": "터널 노선을 따라 탄성파탐사를 실시하여 암반 심도를 파악하겠습니다.",
                "vi": "Sẽ thực hiện thăm dò sóng địa chấn dọc tuyến hầm để xác định độ sâu đá gốc.",
                "situation": "formal"
            },
            {
                "ko": "P파 속도가 2,500m/s 이상인 구간은 경암으로 판단됩니다.",
                "vi": "Đoạn có vận tốc sóng dọc P trên 2,500m/s được đánh giá là đá cứng.",
                "situation": "formal"
            },
            {
                "ko": "탄성파 탐사 결과를 보링 결과와 대조하여 지질 단면도를 작성해 주세요.",
                "vi": "Hãy đối chiếu kết quả thăm dò địa chấn với kết quả khoan để lập mặt cắt địa chất.",
                "situation": "formal"
            }
        ],
        "relatedTerms": ["P파", "S파", "굴절법", "반사법", "지구물리탐사"]
    },
    {
        "slug": "tham-do-dien-tro-suat",
        "korean": "전기비저항탐사",
        "vietnamese": "Thăm dò điện trở suất",
        "hanja": "電氣比抵抗探査",
        "hanjaReading": "電(번개 전) + 氣(기운 기) + 比(견줄 비) + 抵(막을 저) + 抗(막을 항) + 探(찾을 탐) + 査(살필 사)",
        "pronunciation": "전기비저항탐사",
        "meaningKo": "지반에 전류를 흘려 나타나는 전기비저항(electrical resistivity) 분포를 측정하여 지하 지질 구조, 지하수, 오염물질 등을 탐사하는 물리탐사 기법입니다. 통역 시 'resistivity'는 'điện trở suất'로 번역하며, 단위는 'Ω·m'(ohm-meter)를 사용합니다. 점토는 비저항이 낮고(10~100 Ω·m), 암반은 높아(수천 Ω·m) 토층 구분에 유용하며, 특히 지하수 부존 지역, 동공(cavern) 탐지, 매립지 오염 범위 파악에 효과적입니다. 한국에서는 2D 전기비저항탐사가 일반적이며, 최근 3D 탐사도 증가하고 있습니다.",
        "meaningVi": "Thăm dò điện trở suất là phương pháp khảo sát địa vật lý bằng cách phát dòng điện vào đất và đo phân bố điện trở suất để xác định cấu trúc địa chất, nước ngầm, hang động, chất ô nhiễm. Đất sét có điện trở suất thấp (10-100 Ω·m), đá gốc cao (hàng nghìn Ω·m), giúp phân biệt các lớp đất đá.",
        "context": "지질조사, 지하수탐사, 환경조사",
        "culturalNote": "한국은 전기비저항탐사를 터널 공사 전 지하수 및 파쇄대 탐지, 댐 누수 조사, 오염토 범위 확인 등에 적극 활용하며, 자동 측정 장비(SYSCAL, SuperSting 등)와 해석 소프트웨어(RES2DINV, EarthImager)가 보편화되어 있습니다. 베트남은 장비 보급이 제한적이며, 주로 지하수 탐사에만 사용하고, 데이터 해석은 경험에 의존하는 경우가 많습니다. 한국 기술자는 비저항 단면도를 지질 단면도와 중첩 해석하지만, 베트남 기술자는 별개 자료로 취급하는 경향이 있어 통역 시 데이터 통합 해석의 중요성을 강조해야 합니다.",
        "commonMistakes": [
            {
                "mistake": "'비저항'을 'kháng điện'(전기 저항)으로 번역",
                "correction": "'điện trở suất' 사용",
                "explanation": "비저항(resistivity)은 저항(resistance)과 다른 물성치"
            },
            {
                "mistake": "측정 단위를 'Ohm'으로만 표기",
                "correction": "'Ω·m' (ohm-mét) 또는 'ohm-meter' 사용",
                "explanation": "비저항은 면적당 저항이므로 단위에 길이 차원 포함"
            },
            {
                "mistake": "'전극 간격'을 'khoảng cách điện cực'로만 표기하고 수치 없음",
                "correction": "구체적 간격(예: 5m, 10m)과 배열 방식(Wenner, Schlumberger) 명시",
                "explanation": "전극 배열 방식에 따라 탐사 깊이와 해상도가 달라짐"
            }
        ],
        "examples": [
            {
                "ko": "이 구간은 전기비저항이 급격히 낮아지는데, 지하수 부존 구역으로 추정됩니다.",
                "vi": "Đoạn này có điện trở suất giảm đột ngột, có thể là vùng chứa nước ngầm.",
                "situation": "onsite"
            },
            {
                "ko": "터널 노선을 따라 50m 간격으로 2D 전기비저항탐사를 진행하겠습니다.",
                "vi": "Sẽ thực hiện thăm dò điện trở suất 2D cách 50m dọc tuyến hầm.",
                "situation": "formal"
            },
            {
                "ko": "비저항 1000 Ω·m 이상인 구역은 건전한 암반으로 판단됩니다.",
                "vi": "Vùng có điện trở suất trên 1000 Ω·m được đánh giá là đá gốc lành.",
                "situation": "formal"
            }
        ],
        "relatedTerms": ["전기비저항", "물리탐사", "지하수", "파쇄대", "2D 탐사"]
    },
    {
        "slug": "do-muc-nuoc-ngam",
        "korean": "지하수위측정",
        "vietnamese": "Đo mực nước ngầm",
        "hanja": "地下水位測定",
        "hanjaReading": "地(땅 지) + 下(아래 하) + 水(물 수) + 位(자리 위) + 測(잴 측) + 定(정할 정)",
        "pronunciation": "지하수위측정",
        "meaningKo": "보링공이나 관측정을 통해 지하수면의 깊이를 측정하는 작업으로, 기초 설계, 굴착 계획, 배수 시스템 설계의 필수 자료입니다. 통역 시 '지하수위'는 'mực nước ngầm', '관측정'은 'giếng quan trắc'으로 표현합니다. 지하수위는 계절, 강우, 인근 공사 등에 따라 변동하므로 최소 3개월 이상 장기 관측하는 것이 원칙이며, 우기와 건기의 최고·최저 수위를 모두 파악해야 합니다. 한국에서는 자동 수위계(data logger)를 설치하여 실시간 모니터링하지만, 베트남은 수동 측정이 일반적입니다.",
        "meaningVi": "Đo mực nước ngầm là công tác xác định độ sâu của mặt nước ngầm qua lỗ khoan hoặc giếng quan trắc, phục vụ thiết kế móng, kế hoạch đào đất, hệ thống thoát nước. Mực nước ngầm thay đổi theo mùa, mưa, thi công lân cận nên cần quan trắc dài hạn ít nhất 3 tháng để xác định mực cao nhất và thấp nhất.",
        "context": "지질조사, 기초설계, 굴착공사",
        "culturalNote": "한국은 지하수위 측정을 매우 중시하여 보링공마다 24시간 안정화 후 수위를 측정하고, 중요 현장에서는 자동 수위계를 설치하여 시간별 변동을 기록합니다. 굴착 공사 시 인근 건물의 침하를 방지하기 위해 지하수위 변동을 실시간 모니터링하는 것이 의무화되어 있습니다. 베트남은 지하수위 측정이 형식적인 경우가 많아 1회 측정으로 끝내거나, 우기/건기 차이를 고려하지 않는 경우가 많습니다. 한국 기술자는 지하수위를 설계 변수로 직접 활용하지만, 베트남 기술자는 참고 수준으로만 인식하는 경향이 있습니다.",
        "commonMistakes": [
            {
                "mistake": "'지하수위'를 'nước ngầm'(지하수)로만 번역",
                "correction": "'mực nước ngầm' (수위) 사용",
                "explanation": "지하수(nước ngầm)와 지하수위(mực nước ngầm)는 다른 개념"
            },
            {
                "mistake": "수위를 GL 기준이 아닌 '보링공 상단'에서 측정",
                "correction": "반드시 GL(지표면) 기준으로 환산하여 표기",
                "explanation": "보링공 상단 높이는 지점마다 다르므로 GL 기준으로 통일해야 비교 가능"
            },
            {
                "mistake": "1회 측정값만 보고",
                "correction": "측정 일시, 강우 여부, 계절 정보 함께 기록",
                "explanation": "지하수위는 시간에 따라 변동하므로 측정 조건이 중요"
            }
        ],
        "examples": [
            {
                "ko": "보링 완료 24시간 후 지하수위를 측정한 결과 GL-2.8m입니다.",
                "vi": "Sau 24 giờ hoàn thành khoan, mực nước ngầm đo được là GL-2.8m.",
                "situation": "formal"
            },
            {
                "ko": "이 현장은 우기 시 지하수위가 GL-1m까지 상승하므로 차수 대책이 필요합니다.",
                "vi": "Công trường này mùa mưa mực nước ngầm dâng lên GL-1m nên cần biện pháp chống thấm.",
                "situation": "onsite"
            },
            {
                "ko": "굴착 중 지하수위 변동을 실시간 모니터링하여 인근 건물 침하를 예방해야 합니다.",
                "vi": "Trong quá trình đào, phải giám sát biến động mực nước ngầm theo thời gian thực để ngăn lún nhà lân cận.",
                "situation": "formal"
            }
        ],
        "relatedTerms": ["지하수", "관측정", "수위계", "지질조사", "배수공법"]
    },
    {
        "slug": "thi-nghiem-tham-nuoc-hien-truong",
        "korean": "현장투수시험",
        "vietnamese": "Thí nghiệm thấm nước hiện trường",
        "hanja": "現場透水試驗",
        "hanjaReading": "現(나타날 현) + 場(마당 장) + 透(통할 투) + 水(물 수) + 試(시험할 시) + 驗(시험할 험)",
        "pronunciation": "현장투수시험",
        "meaningKo": "지반의 투수 특성을 현장에서 직접 측정하는 시험으로, 보링공이나 시험 구덩이에 물을 주입하여 침투 속도를 측정함으로써 투수계수(k)를 산정합니다. 통역 시 '투수계수'는 'hệ số thấm', '투수시험'은 'thí nghiệm thấm'으로 표현하며, 단위는 'cm/s' 또는 'm/day'를 사용합니다. 현장투수시험은 실내 투수시험보다 신뢰도가 높으며, 댐, 제방, 차수벽 등 물과 관련된 구조물 설계 시 필수입니다. 시험 방법은 정수위(constant head)와 변수위(falling head)가 있으며, 지반 종류에 따라 선택합니다.",
        "meaningVi": "Thí nghiệm thấm nước hiện trường là thí nghiệm đo đặc tính thấm của đất trực tiếp tại công trường bằng cách bơm nước vào lỗ khoan hoặc hố thí nghiệm và đo tốc độ thấm để tính hệ số thấm (k). Hệ số thấm đơn vị cm/s hoặc m/ngày, là thông số quan trọng cho thiết kế đập, đê, tường chống thấm.",
        "context": "지질조사, 배수설계, 차수공사",
        "culturalNote": "한국은 현장투수시험을 매우 정밀하게 수행하며, 시험 전 보링공 내부를 충분히 세척하고, 정압을 일정하게 유지하기 위한 수위 조절 장치를 사용합니다. 시험 시간은 최소 30분~1시간 이상 지속하여 안정화된 유량을 측정합니다. 베트남은 장비와 인력 부족으로 간이 투수시험(단순히 물 붓고 빠지는 시간 측정)을 하는 경우가 많아 결과의 정확도가 낮습니다. 한국 설계자는 투수계수를 차수벽 두께, 배수 시설 용량 산정에 직접 적용하지만, 베트남 시공사는 경험치로 대체하는 경우가 많아 통역 시 시험 목적과 활용 방법을 명확히 해야 합니다.",
        "commonMistakes": [
            {
                "mistake": "'투수계수'를 'hệ số dẫn nước'(통수계수)로 번역",
                "correction": "'hệ số thấm' 사용",
                "explanation": "투수계수(permeability)는 지반의 물 통과 능력, 통수계수는 수로의 흐름 능력"
            },
            {
                "mistake": "투수계수 단위를 'm/s'만 표기",
                "correction": "'cm/s' 또는 'm/day' 병기 (베트남 관행)",
                "explanation": "베트남 기술자는 'm/day' 단위에 더 익숙함"
            },
            {
                "mistake": "'정수위법'을 'phương pháp nước tĩnh'으로 직역",
                "correction": "'phương pháp cột áp không đổi' 사용",
                "explanation": "수위가 일정(constant head)하다는 의미가 정확히 전달되어야 함"
            }
        ],
        "examples": [
            {
                "ko": "이 구간의 투수계수가 1×10⁻⁴ cm/s로 측정되어 투수성이 높습니다.",
                "vi": "Đoạn này có hệ số thấm đo được 1×10⁻⁴ cm/s, tính thấm cao.",
                "situation": "formal"
            },
            {
                "ko": "현장투수시험을 GL-5m, GL-10m 두 심도에서 실시하여 지층별 투수성을 파악하겠습니다.",
                "vi": "Sẽ thực hiện thí nghiệm thấm hiện trường ở hai độ sâu GL-5m và GL-10m để xác định tính thấm từng địa tầng.",
                "situation": "formal"
            },
            {
                "ko": "변수위법으로 투수시험을 진행하되, 수위 변화를 10분마다 기록해 주세요.",
                "vi": "Thí nghiệm thấm bằng phương pháp cột áp giảm dần, ghi nhận biến đổi mực nước mỗi 10 phút.",
                "situation": "onsite"
            }
        ],
        "relatedTerms": ["투수계수", "정수위법", "변수위법", "지하수", "차수공법"]
    }
]

def main():
    # 파일 경로 설정
    file_path = os.path.join(
        os.path.dirname(os.path.abspath(__file__)),
        '..',
        'data',
        'terms',
        'construction.json'
    )

    # 기존 데이터 읽기
    with open(file_path, 'r', encoding='utf-8') as f:
        existing_data = json.load(f)

    print(f"기존 용어 수: {len(existing_data)}")

    # 새 용어 추가
    existing_data.extend(data)

    print(f"추가 후 용어 수: {len(existing_data)}")

    # 파일에 저장
    with open(file_path, 'w', encoding='utf-8') as f:
        json.dump(existing_data, f, ensure_ascii=False, indent=2)

    print(f"✅ {len(data)}개 용어가 추가되었습니다.")
    print("\n추가된 용어:")
    for term in data:
        print(f"  - {term['korean']} ({term['vietnamese']})")

if __name__ == "__main__":
    main()
