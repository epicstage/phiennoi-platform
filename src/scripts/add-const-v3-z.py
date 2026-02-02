#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
건설 용어 추가 스크립트 v3-z: 엘리베이터/주차설비 (Elevator & Parking)
Tier S 품질 기준 (90점 이상)
"""

import json
import os

# 추가할 용어 데이터 (10개)
new_terms = [
    {
        "slug": "thang-may-hanh-khach",
        "korean": "승객용 승강기",
        "vietnamese": "Thang máy hành khách",
        "hanja": "乘客用昇降機",
        "hanjaReading": "乘(탈 승) + 客(손 객) + 用(쓸 용) + 昇(오를 승) + 降(내릴 강) + 機(틀 기)",
        "pronunciation": "승깍뇽 승강기",
        "meaningKo": "사람을 수직으로 운송하기 위한 승강기로, 화물용과 구분됩니다. 통역 시 주의사항: 베트남에서는 'thang máy'만으로 승객용을 의미하는 경우가 많지만, 정식 도면이나 계약서에서는 반드시 'hành khách(승객용)'을 명시해야 합니다. 한국의 건축법상 6층 이상 건물에는 승객용 승강기 설치가 의무이며, 속도·정원·안전장치 기준이 화물용과 다릅니다. 베트남 통역사는 '엘리베이터'와 '리프트'를 혼용하지 않도록 주의하고, 승객용/화물용 구분을 정확히 전달해야 합니다.",
        "meaningVi": "Thang máy dùng để vận chuyển người theo phương thẳng đứng, phân biệt với thang máy chở hàng. Theo quy định xây dựng Hàn Quốc, tòa nhà từ 6 tầng trở lên bắt buộc phải lắp đặt thang máy hành khách với tiêu chuẩn tốc độ, sức chứa và thiết bị an toàn khác với loại chở hàng.",
        "context": "건축설계, 기계설비, 안전검사",
        "culturalNote": "한국은 승강기 안전관리법에 따라 정기검사·자체점검이 엄격하며, 15인승 이상 승강기는 반드시 관리주체를 두어야 합니다. 베트남은 상대적으로 소형 건물에 승강기 설치율이 낮고, 유지보수 체계가 덜 정비되어 있어 한국 기준을 설명할 때 '법적 의무'임을 강조해야 합니다. 또한 베트남에서는 '승강기 기사(thợ thang máy)'가 상주하는 경우가 드물어, 한국의 관리 시스템을 설명할 때 문화적 차이를 고려해야 합니다.",
        "commonMistakes": [
            {
                "mistake": "thang máy chở khách",
                "correction": "thang máy hành khách",
                "explanation": "'chở khách'은 화물 운송 뉘앙스가 강해 부적절. 'hành khách'이 표준 용어."
            },
            {
                "mistake": "lift hành khách",
                "correction": "thang máy hành khách",
                "explanation": "베트남어에서는 'lift'보다 'thang máy'가 표준. 영어 차용어 혼용 금지."
            },
            {
                "mistake": "승객용 엘리베이터를 '리프트'로 번역",
                "correction": "엘리베이터 = thang máy",
                "explanation": "한국에서 '엘리베이터'가 표준 용어이며, 베트남어 'thang máy'로 통일."
            }
        ],
        "examples": [
            {
                "ko": "이 건물은 20인승 승객용 승강기 2대를 설치해야 합니다.",
                "vi": "Tòa nhà này cần lắp đặt 2 thang máy hành khách sức chứa 20 người.",
                "situation": "formal"
            },
            {
                "ko": "승객용 승강기 정기검사는 연 1회 실시됩니다.",
                "vi": "Kiểm tra định kỳ thang máy hành khách được thực hiện 1 lần/năm.",
                "situation": "formal"
            },
            {
                "ko": "승객용 승강기에 화물을 실으면 안 됩니다.",
                "vi": "Không được chở hàng hóa trong thang máy hành khách.",
                "situation": "onsite"
            }
        ],
        "relatedTerms": ["화물용 승강기", "비상용 승강기", "전망용 승강기", "기계실"]
    },
    {
        "slug": "thang-cuon",
        "korean": "에스컬레이터",
        "vietnamese": "Thang cuốn",
        "hanja": None,
        "hanjaReading": None,
        "pronunciation": "에스컬레이터",
        "meaningKo": "계단 형태의 발판이 연속적으로 움직여 사람을 수직 또는 경사지게 운송하는 설비입니다. 통역 시 주의사항: 한국에서는 '에스컬레이터'라는 외래어를 그대로 사용하지만, 베트남어로는 'thang cuốn(말려 올라가는 계단)'이라는 고유 표현을 씁니다. 쇼핑몰·지하철역 등에서 흔히 볼 수 있으며, 상행/하행, 속도(분당 30m 기준), 경사각(30~35도), 폭(600mm/800mm/1000mm) 등의 사양을 정확히 전달해야 합니다. 또한 '무빙워크'와 혼동하지 않도록 주의해야 합니다.",
        "meaningVi": "Thiết bị vận chuyển người theo phương thẳng đứng hoặc nghiêng bằng các bậc thang di chuyển liên tục. Thường thấy ở trung tâm thương mại, ga tàu điện ngầm, với các thông số như hướng lên/xuống, tốc độ (30m/phút), góc nghiêng (30-35 độ), chiều rộng (600/800/1000mm).",
        "context": "상업건축, 대중교통시설, 기계설비",
        "culturalNote": "한국은 에스컬레이터 안전사고(특히 어린이·노인) 예방을 위해 비상정지버튼·빗살 안전장치·손잡이 속도 동기화 등을 법적으로 의무화하고 있습니다. 베트남은 대도시 쇼핑몰에서는 흔하지만, 2~3선 도시에서는 설치율이 낮아 유지보수 경험이 부족한 경우가 많습니다. 통역 시 한국의 엄격한 안전기준(KS 기준)을 설명하고, 베트남 현지 기술자가 익숙하지 않은 부분을 명확히 전달해야 합니다.",
        "commonMistakes": [
            {
                "mistake": "thang bộ tự động",
                "correction": "thang cuốn",
                "explanation": "'thang bộ tự động'은 직역이지만 베트남어 표준 용어는 'thang cuốn'."
            },
            {
                "mistake": "escalator",
                "correction": "thang cuốn",
                "explanation": "베트남어 공식 문서에서는 영어 차용어 대신 고유어 'thang cuốn' 사용."
            },
            {
                "mistake": "에스컬레이터를 '계단식 승강기'로 번역",
                "correction": "thang cuốn",
                "explanation": "승강기(thang máy)와 혼동 방지. 에스컬레이터는 별도 용어."
            }
        ],
        "examples": [
            {
                "ko": "1층에서 3층까지 상행 에스컬레이터 3대를 설치합니다.",
                "vi": "Lắp đặt 3 thang cuốn đi lên từ tầng 1 đến tầng 3.",
                "situation": "formal"
            },
            {
                "ko": "에스컬레이터 비상정지버튼 위치를 확인하세요.",
                "vi": "Kiểm tra vị trí nút dừng khẩn cấp thang cuốn.",
                "situation": "onsite"
            },
            {
                "ko": "에스컬레이터 폭은 1000mm, 속도는 분당 30m입니다.",
                "vi": "Thang cuốn rộng 1000mm, tốc độ 30m/phút.",
                "situation": "formal"
            }
        ],
        "relatedTerms": ["무빙워크", "승객용 승강기", "경사로", "비상정지버튼"]
    },
    {
        "slug": "bai-do-xe-tu-dong",
        "korean": "기계식 주차장",
        "vietnamese": "Bãi đỗ xe tự động",
        "hanja": "機械式駐車場",
        "hanjaReading": "機(틀 기) + 械(기계 계) + 式(법 식) + 駐(머무를 주) + 車(수레 차) + 場(마당 장)",
        "pronunciation": "기계식 주차장",
        "meaningKo": "기계장치(리프트·회전판 등)를 이용해 차량을 자동으로 주차시키는 주차설비로, 좁은 부지에 다층으로 차량을 적재할 수 있습니다. 통역 시 주의사항: '자주식 주차장'과 명확히 구분해야 하며, 베트남어로는 'bãi đỗ xe tự động(자동 주차장)' 또는 'bãi đỗ xe cơ khí(기계식 주차장)'로 표현합니다. 한국에서는 승강기식·승강횡행식·수직순환식·다층순환식 등 다양한 방식이 있으며, 각 방식의 차이를 정확히 설명해야 합니다. 또한 '타워형 주차장'과 혼동하지 않도록 주의하세요.",
        "meaningVi": "Hệ thống đỗ xe sử dụng thiết bị cơ khí (thang máy, bàn xoay) để tự động xếp xe nhiều tầng trên diện tích hẹp. Có các loại như thang máy đơn thuần, thang máy + di chuyển ngang, tuần hoàn dọc, tuần hoàn nhiều tầng. Phân biệt rõ với bãi đỗ xe tự lái (tự chủ).",
        "context": "건축설계, 주차시설, 기계설비",
        "culturalNote": "한국은 도심 부지 부족으로 기계식 주차장이 아파트·오피스텔에 널리 보급되었으며, 안전기준(낙하방지·비상정지 등)이 엄격합니다. 베트남은 아직 기계식 주차장 도입이 초기 단계로, 하노이·호치민 일부 고급 건물에만 설치되어 있습니다. 통역 시 한국 기술의 선진성을 강조하되, 베트남 현지 유지보수 인력 부족 문제를 고려해 교육·AS 계획을 함께 설명해야 합니다. 또한 베트남 운전자들이 기계식 주차 경험이 적어, 사용법 안내가 필수임을 전달하세요.",
        "commonMistakes": [
            {
                "mistake": "bãi đỗ xe cơ học",
                "correction": "bãi đỗ xe tự động / bãi đỗ xe cơ khí",
                "explanation": "'cơ học'은 '역학(mechanics)'을 의미. '기계식'은 'cơ khí' 또는 'tự động'."
            },
            {
                "mistake": "nhà để xe tự động",
                "correction": "bãi đỗ xe tự động",
                "explanation": "'nhà để xe'는 '차고'에 가까움. 주차장은 'bãi đỗ xe'."
            },
            {
                "mistake": "기계식 주차장을 '타워형 주차장'과 동일시",
                "correction": "기계식 주차장 ⊃ 타워형 주차장",
                "explanation": "타워형은 기계식의 한 유형. 포함 관계를 명확히 설명."
            }
        ],
        "examples": [
            {
                "ko": "이 건물은 지하에 승강횡행식 기계식 주차장 50면을 계획하고 있습니다.",
                "vi": "Tòa nhà này dự kiến lắp đặt bãi đỗ xe tự động kiểu thang máy + di chuyển ngang 50 chỗ ở tầng hầm.",
                "situation": "formal"
            },
            {
                "ko": "기계식 주차장은 자주식보다 공간 효율이 2배 이상 높습니다.",
                "vi": "Bãi đỗ xe tự động có hiệu suất diện tích cao gấp 2 lần so với bãi tự lái.",
                "situation": "formal"
            },
            {
                "ko": "기계식 주차장 낙하방지장치를 점검해 주세요.",
                "vi": "Kiểm tra thiết bị chống rơi của bãi đỗ xe tự động.",
                "situation": "onsite"
            }
        ],
        "relatedTerms": ["자주식 주차장", "타워형 주차장", "승강횡행식", "주차면"]
    },
    {
        "slug": "bai-do-xe-tu-lai",
        "korean": "자주식 주차장",
        "vietnamese": "Bãi đỗ xe tự lái",
        "hanja": "自走式駐車場",
        "hanjaReading": "自(스스로 자) + 走(달릴 주) + 式(법 식) + 駐(머무를 주) + 車(수레 차) + 場(마당 장)",
        "pronunciation": "자주식 주차장",
        "meaningKo": "운전자가 직접 차량을 몰고 들어가 주차하는 방식의 주차장으로, 램프(경사로) 또는 승강기를 이용해 층간 이동합니다. 통역 시 주의사항: '기계식 주차장'과 반대 개념으로, 베트남어로는 'bãi đỗ xe tự lái(스스로 운전해 주차)'로 표현합니다. 한국에서는 대형 쇼핑몰·오피스 건물에 주로 사용되며, 층고·램프 경사도·회전반경 등의 설계 기준을 준수해야 합니다. '평면 주차장'과는 달리 다층 구조를 의미하므로, 단순 '노외주차장'과 혼동하지 않도록 주의하세요.",
        "meaningVi": "Bãi đỗ xe mà tài xế tự lái xe vào và đỗ, di chuyển giữa các tầng bằng dốc (rampe) hoặc thang máy. Khái niệm đối lập với bãi đỗ xe tự động. Thường dùng ở trung tâm thương mại, tòa nhà văn phòng, cần tuân thủ tiêu chuẩn chiều cao tầng, độ dốc rampe, bán kính quay đầu.",
        "context": "건축설계, 주차시설, 교통계획",
        "culturalNote": "한국은 자주식 주차장 설계 시 장애인 주차구역·여성 우선 주차구역·전기차 충전구역을 의무 배치하며, 주차면 크기(폭 2.3m 이상)가 법으로 정해져 있습니다. 베트남은 자주식 주차장이 일반적이지만, 램프 경사도가 가파르거나 층고가 낮은 경우가 많아 한국 차량(특히 SUV) 진입에 어려움이 있을 수 있습니다. 통역 시 한국 기준(층고 2.3m 이상, 경사 1/6 이하)을 명확히 전달하고, 베트남 기준과의 차이를 설명해야 합니다.",
        "commonMistakes": [
            {
                "mistake": "bãi đỗ xe tự do",
                "correction": "bãi đỗ xe tự lái",
                "explanation": "'tự do(자유)'는 부적절. '자주(스스로 주행)'는 'tự lái'."
            },
            {
                "mistake": "bãi đỗ xe phẳng",
                "correction": "bãi đỗ xe tự lái (nhiều tầng)",
                "explanation": "'phẳng'은 '평면 주차장'을 의미. 다층 구조는 'nhiều tầng' 추가."
            },
            {
                "mistake": "자주식 주차장을 '일반 주차장'으로 번역",
                "correction": "bãi đỗ xe tự lái",
                "explanation": "'일반'은 모호. 기계식과 대비되는 '자주식' 개념을 명확히 표현."
            }
        ],
        "examples": [
            {
                "ko": "지하 3층부터 지상 5층까지 자주식 주차장 300면을 계획합니다.",
                "vi": "Dự kiến bãi đỗ xe tự lái 300 chỗ từ tầng hầm B3 đến tầng 5.",
                "situation": "formal"
            },
            {
                "ko": "자주식 주차장 램프 경사도는 1/6 이하로 설계하세요.",
                "vi": "Thiết kế dốc rampe bãi đỗ xe tự lái không quá 1/6.",
                "situation": "formal"
            },
            {
                "ko": "자주식 주차장 3층에 전기차 충전구역 10면을 배치합니다.",
                "vi": "Bố trí 10 chỗ đỗ xe điện có sạc ở tầng 3 bãi tự lái.",
                "situation": "onsite"
            }
        ],
        "relatedTerms": ["기계식 주차장", "램프", "평면 주차장", "전기차 충전시설"]
    },
    {
        "slug": "thap-do-xe",
        "korean": "주차타워",
        "vietnamese": "Tháp đỗ xe",
        "hanja": "駐車塔",
        "hanjaReading": "駐(머무를 주) + 車(수레 차) + 塔(탑 탑)",
        "pronunciation": "주차타",
        "meaningKo": "수직으로 높이 솟은 형태의 기계식 주차장으로, 좁은 부지에 최대 주차면을 확보하기 위한 타워형 구조입니다. 통역 시 주의사항: '기계식 주차장'의 한 유형이며, 베트남어로는 'tháp đỗ xe(주차 탑)'로 표현합니다. 한국에서는 도심 주차난 해소를 위해 공영 주차타워가 많이 설치되며, 높이 20~30m, 최대 50~100대 수용이 가능합니다. 자주식 주차장과 달리 운전자가 차를 맡기고 내리면 기계가 자동으로 적재하는 방식이므로, 이 차이를 명확히 설명해야 합니다.",
        "meaningVi": "Bãi đỗ xe cơ khí dạng tháp cao theo phương thẳng đứng, tối đa hóa số chỗ đỗ trên diện tích nhỏ. Tài xế giao xe và rời đi, hệ thống tự động xếp xe vào tháp cao 20-30m, chứa 50-100 xe. Là một dạng của bãi đỗ xe tự động.",
        "context": "도시계획, 주차시설, 기계설비",
        "culturalNote": "한국은 서울·부산 등 대도시에서 공영 주차타워가 많이 운영되며, 무인 결제 시스템과 연동되어 있습니다. 베트남은 아직 주차타워 개념이 생소하고, 하노이·호치민 일부 프리미엄 건물에만 시범 도입되었습니다. 통역 시 한국의 공영 주차타워 사례(24시간 무인 운영, 모바일 결제 등)를 소개하고, 베트남 도입 시 고려사항(전력 공급 안정성, 현지 유지보수 인력 교육, 사용자 교육)을 함께 설명해야 합니다. 또한 '타워형 주차장'이라는 용어와 혼용되므로 문맥에 따라 정확히 구분하세요.",
        "commonMistakes": [
            {
                "mistake": "tòa nhà đỗ xe",
                "correction": "tháp đỗ xe",
                "explanation": "'tòa nhà'는 일반 건물. '타워'는 'tháp'이 정확."
            },
            {
                "mistake": "bãi đỗ xe cao tầng",
                "correction": "tháp đỗ xe / bãi đỗ xe dạng tháp",
                "explanation": "'cao tầng'은 모호. '타워형' 구조는 'tháp' 또는 'dạng tháp'."
            },
            {
                "mistake": "주차타워를 '주차빌딩'으로 번역",
                "correction": "tháp đỗ xe",
                "explanation": "주차빌딩은 자주식 다층 주차장. 타워는 기계식 수직 구조."
            }
        ],
        "examples": [
            {
                "ko": "역 앞에 공영 주차타워를 건설하여 200대를 수용할 예정입니다.",
                "vi": "Dự kiến xây tháp đỗ xe công cộng trước ga, chứa 200 xe.",
                "situation": "formal"
            },
            {
                "ko": "주차타워는 무인 운영 시스템으로 24시간 이용 가능합니다.",
                "vi": "Tháp đỗ xe hoạt động tự động 24/7 không người trực.",
                "situation": "formal"
            },
            {
                "ko": "주차타워 입출고 시간은 평균 90초입니다.",
                "vi": "Thời gian nhập/xuất xe từ tháp đỗ xe trung bình 90 giây.",
                "situation": "onsite"
            }
        ],
        "relatedTerms": ["기계식 주차장", "공영주차장", "무인운영시스템", "입출고시간"]
    },
    {
        "slug": "doc-rampe",
        "korean": "램프",
        "vietnamese": "Dốc rampe",
        "hanja": None,
        "hanjaReading": None,
        "pronunciation": "램프",
        "meaningKo": "자주식 주차장에서 층간 이동을 위한 경사로로, 차량이 직접 주행하여 오르내립니다. 통역 시 주의사항: 한국에서는 외래어 '램프(ramp)'를 그대로 사용하지만, 베트남어로는 'dốc(경사로)' 또는 'dốc rampe'로 표현합니다. 설계 기준으로 경사도 1/6 이하, 최소 폭 3.5m(양방향 6m), 회전반경 6m 이상 등이 있으며, 미끄럼 방지 마감과 배수 처리가 중요합니다. '엘리베이터'와 달리 차량이 '직접 주행'한다는 점을 강조하고, '경사로'라는 일반 용어와 '램프'라는 주차장 전문 용어를 구분해야 합니다.",
        "meaningVi": "Đường dốc trong bãi đỗ xe tự lái để xe di chuyển giữa các tầng. Tiêu chuẩn thiết kế: độ dốc tối đa 1/6, chiều rộng tối thiểu 3,5m (2 chiều 6m), bán kính quay 6m trở lên, cần xử lý chống trượt và thoát nước.",
        "context": "주차장설계, 교통계획, 토목공사",
        "culturalNote": "한국은 장애인·노약자를 위해 램프 입구에 경사 완화 구간을 두고, 미끄럼 방지 마감(요철 포장 등)을 의무화합니다. 베트남은 일부 주차장에서 램프 경사가 가파르거나 폭이 좁아 대형 차량 진입이 어려운 경우가 있습니다. 통역 시 한국 기준(경사 1/6, 폭 3.5m 이상)을 설명하고, 베트남 현지 차량 크기(소형차 중심)와 한국 차량(SUV 증가)의 차이를 고려해 설계 여유를 확보할 것을 제안하세요. 또한 우기 배수 처리의 중요성을 강조해야 합니다.",
        "commonMistakes": [
            {
                "mistake": "đường dốc",
                "correction": "dốc rampe / dốc xe",
                "explanation": "'đường dốc'은 일반 경사로. 주차장 전용은 'dốc rampe' 또는 'dốc xe'."
            },
            {
                "mistake": "thang máy xe",
                "correction": "dốc rampe",
                "explanation": "램프는 경사로이지 승강기(thang máy)가 아님."
            },
            {
                "mistake": "램프를 '경사로'로만 번역",
                "correction": "dốc rampe (주차장 맥락)",
                "explanation": "일반 경사로와 구분 위해 'rampe' 또는 '주차장 dốc' 명시."
            }
        ],
        "examples": [
            {
                "ko": "지하 주차장으로 내려가는 램프 경사도는 1/6입니다.",
                "vi": "Độ dốc rampe xuống bãi đỗ xe tầng hầm là 1/6.",
                "situation": "formal"
            },
            {
                "ko": "램프 바닥에 미끄럼 방지 마감을 시공하세요.",
                "vi": "Thi công mặt chống trượt trên dốc rampe.",
                "situation": "onsite"
            },
            {
                "ko": "램프 회전반경이 좁아서 대형 차량 진입이 어렵습니다.",
                "vi": "Bán kính quay dốc rampe hẹp, khó cho xe lớn vào.",
                "situation": "onsite"
            }
        ],
        "relatedTerms": ["자주식 주차장", "경사도", "미끄럼방지", "회전반경"]
    },
    {
        "slug": "thang-may-hang-hoa",
        "korean": "화물용 승강기",
        "vietnamese": "Thang máy hàng hóa",
        "hanja": "貨物用昇降機",
        "hanjaReading": "貨(물건 화) + 物(물건 물) + 用(쓸 용) + 昇(오를 승) + 降(내릴 강) + 機(틀 기)",
        "pronunciation": "화물룡 승강기",
        "meaningKo": "화물을 수직으로 운송하기 위한 승강기로, 승객용보다 적재 하중이 크고 내부 마감이 견고합니다. 통역 시 주의사항: '승객용 승강기'와 명확히 구분해야 하며, 베트남어로는 'thang máy hàng hóa(화물 승강기)' 또는 'thang máy chở hàng'으로 표현합니다. 한국에서는 공장·물류센터·병원(침대 이송용) 등에 설치되며, 적재하중(500kg~5톤), 카 크기, 출입구 폭 등이 용도에 따라 다릅니다. '사람 탑승 금지' 표지가 필수이며, 안전장치(과부하 방지, 문 잠금 장치 등)가 승객용과 다릅니다. 통역 시 '화물용'과 '승객용'의 법적 구분을 정확히 전달하세요.",
        "meaningVi": "Thang máy dùng để vận chuyển hàng hóa theo phương thẳng đứng, tải trọng lớn hơn và nội thất chắc chắn hơn thang máy hành khách. Dùng ở nhà máy, kho logistics, bệnh viện (chuyển giường bệnh). Tải trọng 500kg~5 tấn, cấm người đi cùng, thiết bị an toàn khác loại hành khách.",
        "context": "공장설계, 물류시설, 기계설비",
        "culturalNote": "한국은 화물용 승강기에 대해 승객용과 별도의 안전기준(적재하중 표시, 과부하 경보, 비상정지 등)을 적용하며, 정기검사 주기도 다릅니다. 베트남은 소규모 공장에서 승객용 승강기를 화물 운송에 임의로 사용하는 경우가 있어, 한국 기준에서는 불법임을 명확히 설명해야 합니다. 통역 시 '화물용'과 '승객용'의 법적 구분, 적재하중 초과 시 위험성, 안전장치 차이를 강조하고, 베트남 현장에서 혼용하지 않도록 교육해야 합니다.",
        "commonMistakes": [
            {
                "mistake": "thang máy tải",
                "correction": "thang máy hàng hóa",
                "explanation": "'tải'는 '싣다'는 동사. 화물용은 'hàng hóa'가 정확."
            },
            {
                "mistake": "thang máy công nghiệp",
                "correction": "thang máy hàng hóa",
                "explanation": "'công nghiệp'은 '산업용' 일반. 화물용은 'hàng hóa' 명시."
            },
            {
                "mistake": "화물용 승강기를 '리프트'로 번역",
                "correction": "thang máy hàng hóa",
                "explanation": "베트남어에서는 'thang máy'로 통일. 'lift'는 비표준."
            }
        ],
        "examples": [
            {
                "ko": "공장 3층에 적재하중 3톤 화물용 승강기를 설치합니다.",
                "vi": "Lắp đặt thang máy hàng hóa tải trọng 3 tấn ở tầng 3 nhà máy.",
                "situation": "formal"
            },
            {
                "ko": "화물용 승강기에는 사람이 탑승해서는 안 됩니다.",
                "vi": "Không được để người đi cùng trong thang máy hàng hóa.",
                "situation": "onsite"
            },
            {
                "ko": "화물용 승강기 출입구 폭은 1.5m, 높이는 2.2m입니다.",
                "vi": "Cửa thang máy hàng hóa rộng 1,5m, cao 2,2m.",
                "situation": "formal"
            }
        ],
        "relatedTerms": ["승객용 승강기", "적재하중", "과부하방지장치", "물류센터"]
    },
    {
        "slug": "thang-may-khan-cap",
        "korean": "비상용 승강기",
        "vietnamese": "Thang máy khẩn cấp",
        "hanja": "非常用昇降機",
        "hanjaReading": "非(아닐 비) + 常(항상 상) + 用(쓸 용) + 昇(오를 승) + 降(내릴 강) + 機(틀 기)",
        "pronunciation": "비상용 승강기",
        "meaningKo": "화재 등 비상시 소방대원과 피난자가 사용할 수 있도록 특수 설계된 승강기로, 일반 승강기보다 내화·내수·비상전원 기준이 엄격합니다. 통역 시 주의사항: 베트남어로는 'thang máy khẩn cấp(긴급 승강기)' 또는 'thang máy cứu hỏa(소방 승강기)'로 표현합니다. 한국 건축법상 11층 이상 건물에는 비상용 승강기 설치가 의무이며, 기계실·승강로가 내화구조이고, 정전 시에도 자가발전으로 작동해야 합니다. '일반 승객용 승강기'와 외관상 구분이 어려우므로, '비상용' 표지 부착과 평상시 사용 제한을 명확히 설명해야 합니다.",
        "meaningVi": "Thang máy được thiết kế đặc biệt để lính cứu hỏa và người tránh nạn sử dụng khi khẩn cấp (cháy nổ), tiêu chuẩn chống cháy, chống nước, nguồn điện dự phòng nghiêm ngặt hơn thang máy thường. Tòa nhà từ 11 tầng trở lên ở Hàn Quốc bắt buộc có, hoạt động bằng máy phát điện khi mất điện.",
        "context": "건축설계, 소방설비, 안전관리",
        "culturalNote": "한국은 고층 건물 화재 대비를 위해 비상용 승강기 설치·운영을 법으로 엄격히 규제하며, 연 1회 이상 소방 합동 훈련을 실시합니다. 베트남은 고층 건물이 증가하고 있으나 비상용 승강기 설치율이 낮고, 유지관리가 미흡한 경우가 많습니다. 통역 시 한국의 엄격한 법적 기준(내화 2시간 이상, 침수 방지, 자가발전 30분 이상)을 설명하고, 베트남에서 '일반 승강기를 비상시 사용'하는 관행이 매우 위험함을 강조해야 합니다. 또한 '비상용'과 '소방용'을 동일 개념으로 이해하도록 안내하세요.",
        "commonMistakes": [
            {
                "mistake": "thang máy khẩn",
                "correction": "thang máy khẩn cấp",
                "explanation": "'khẩn'만으로는 불완전. 'khẩn cấp'이 완전한 표현."
            },
            {
                "mistake": "thang máy cứu nạn",
                "correction": "thang máy khẩn cấp / thang máy cứu hỏa",
                "explanation": "'cứu nạn'은 '구조'를 의미. '비상용'은 'khẩn cấp' 또는 'cứu hỏa'."
            },
            {
                "mistake": "비상용 승강기를 '피난용 승강기'로만 번역",
                "correction": "thang máy khẩn cấp (소방대원 + 피난자 겸용)",
                "explanation": "소방대원 진입 + 피난자 대피 겸용임을 명확히 설명."
            }
        ],
        "examples": [
            {
                "ko": "이 건물은 15층이므로 비상용 승강기 1대가 법적으로 필요합니다.",
                "vi": "Tòa nhà này 15 tầng nên theo luật phải có 1 thang máy khẩn cấp.",
                "situation": "formal"
            },
            {
                "ko": "비상용 승강기는 평상시 일반인 사용이 금지됩니다.",
                "vi": "Thang máy khẩn cấp cấm sử dụng thường ngày.",
                "situation": "onsite"
            },
            {
                "ko": "비상용 승강기 승강로는 내화 2시간 이상 구조로 시공하세요.",
                "vi": "Thi công hố thang máy khẩn cấp chịu lửa tối thiểu 2 giờ.",
                "situation": "formal"
            }
        ],
        "relatedTerms": ["소방설비", "내화구조", "자가발전설비", "피난계획"]
    },
    {
        "slug": "cho-do-xe-nguoi-khuyet-tat",
        "korean": "장애인 전용 주차구역",
        "vietnamese": "Chỗ đỗ xe người khuyết tật",
        "hanja": "障碍人專用駐車區域",
        "hanjaReading": "障(막을 장) + 碍(막을 애) + 人(사람 인) + 專(오로지 전) + 用(쓸 용) + 駐(머무를 주) + 車(수레 차) + 區(구역 구) + 域(지경 역)",
        "pronunciation": "장애인 전용 주차구역",
        "meaningKo": "장애인의 주차 편의를 위해 법적으로 지정된 주차면으로, 일반 주차면보다 넓고(폭 3.3m 이상) 출입구와 가까운 곳에 배치해야 합니다. 통역 시 주의사항: 베트남어로는 'chỗ đỗ xe người khuyết tật(장애인 주차 공간)' 또는 'bãi đỗ xe dành riêng cho người khuyết tật(장애인 전용 주차장)'로 표현합니다. 한국에서는 '장애인·노인·임산부 등의 편의증진 보장에 관한 법률'에 따라 주차장 규모별로 장애인 주차구역 설치 비율이 정해져 있으며(50면당 1면 이상), 무단 주차 시 과태료가 부과됩니다. 베트남 통역 시 한국의 엄격한 법적 의무와 사회적 인식을 설명해야 합니다.",
        "meaningVi": "Chỗ đỗ xe được chỉ định theo luật cho người khuyết tật, rộng hơn chỗ thường (tối thiểu 3,3m) và gần lối vào. Theo luật Hàn Quốc, bãi đỗ xe phải có tỷ lệ chỗ dành cho người khuyết tật (tối thiểu 1 chỗ/50 chỗ), đỗ xe trái phép bị phạt nặng.",
        "context": "주차장설계, 장애인편의시설, 건축법규",
        "culturalNote": "한국은 장애인 주차구역을 법적으로 엄격히 보호하며, 장애인 표지판과 노면 표시(휠체어 마크)를 의무화하고, 무단 주차 시 10만 원 과태료를 부과합니다. 베트남은 장애인 주차구역 개념이 도입되고 있으나, 표지판이 없거나 일반 차량이 무단 주차하는 경우가 많습니다. 통역 시 한국의 법적 의무(설치 비율, 폭 3.3m 이상, 경사 1/50 이하)와 사회적 인식(무단 주차 금지 문화)을 설명하고, 베트님 현지에서도 점차 확대되는 추세임을 안내하세요. 또한 '장애인'이라는 표현 대신 'người khuyết tật(결핍된 사람)'이 베트남어 존중 표현임을 유의하세요.",
        "commonMistakes": [
            {
                "mistake": "chỗ đỗ xe người tàn tật",
                "correction": "chỗ đỗ xe người khuyết tật",
                "explanation": "'tàn tật'은 비하 표현. 'khuyết tật'이 존중 용어."
            },
            {
                "mistake": "bãi đỗ xe ưu tiên",
                "correction": "chỗ đỗ xe người khuyết tật / chỗ đỗ xe dành riêng",
                "explanation": "'ưu tiên'은 '우선'. '전용'은 'dành riêng'이 정확."
            },
            {
                "mistake": "장애인 주차구역을 '장애인 주차장'으로 번역",
                "correction": "chỗ đỗ xe người khuyết tật (구역)",
                "explanation": "주차장 내 일부 '구역'이지, 별도 '주차장'이 아님."
            }
        ],
        "examples": [
            {
                "ko": "지하 1층 출입구 앞에 장애인 전용 주차구역 5면을 배치합니다.",
                "vi": "Bố trí 5 chỗ đỗ xe người khuyết tật trước lối vào tầng hầm B1.",
                "situation": "formal"
            },
            {
                "ko": "장애인 주차구역 폭은 3.3m 이상으로 설계하세요.",
                "vi": "Thiết kế chỗ đỗ xe người khuyết tật rộng tối thiểu 3,3m.",
                "situation": "formal"
            },
            {
                "ko": "장애인 주차구역에 휠체어 마크를 노면에 표시해 주세요.",
                "vi": "Vẽ biểu tượng xe lăn trên mặt chỗ đỗ xe người khuyết tật.",
                "situation": "onsite"
            }
        ],
        "relatedTerms": ["장애인편의시설", "주차면", "휠체어", "무단주차"]
    },
    {
        "slug": "tram-sac-xe-dien",
        "korean": "전기차 충전시설",
        "vietnamese": "Trạm sạc xe điện",
        "hanja": "電氣車充電施設",
        "hanjaReading": "電(번개 전) + 氣(기운 기) + 車(수레 차) + 充(채울 충) + 電(번개 전) + 施(베풀 시) + 設(베풀 설)",
        "pronunciation": "전기차 충전시설",
        "meaningKo": "전기 자동차(EV)의 배터리를 충전하기 위한 설비로, 완속(7kW)과 급속(50kW 이상) 충전기로 구분됩니다. 통역 시 주의사항: 베트남어로는 'trạm sạc xe điện(전기차 충전소)' 또는 'thiết bị sạc xe điện(충전 설비)'으로 표현합니다. 한국에서는 '환경친화적 자동차의 개발 및 보급 촉진에 관한 법률'에 따라 신축 건물(주차 규모별)에 전기차 충전시설 설치가 의무화되고 있으며, 완속 충전기는 주차면마다, 급속 충전기는 주차장별로 배치 기준이 다릅니다. 통역 시 '완속/급속' 구분, 전기 용량(kW), 커넥터 타입(Type2 등)을 정확히 전달하세요.",
        "meaningVi": "Thiết bị sạc pin cho xe ô tô điện (EV), phân loại thành sạc chậm (7kW) và sạc nhanh (từ 50kW). Theo luật Hàn Quốc, tòa nhà mới bắt buộc lắp đặt trạm sạc xe điện theo tỷ lệ bãi đỗ, sạc chậm theo từng chỗ, sạc nhanh theo khu vực bãi.",
        "context": "주차장설계, 전기설비, 환경정책",
        "culturalNote": "한국은 2030년까지 전기차 300만 대 보급 목표로 충전 인프라를 급속히 확대하고 있으며, 아파트·오피스텔 신축 시 주차면의 5~10%에 충전시설 설치를 의무화합니다. 베트남은 전기차 보급 초기 단계로, 하노이·호치민 일부 고급 건물에만 충전시설이 있으며, 전력 공급 안정성이 과제입니다. 통역 시 한국의 충전 인프라 확대 정책, 정부 보조금, 전기차 증가 추세를 설명하고, 베트남 도입 시 전력 용량 확보와 충전기 표준화(Type2 커넥터)의 중요성을 강조하세요. 또한 '충전소'와 '충전시설'의 차이(독립형 vs 건물 내 설비)를 명확히 구분해야 합니다.",
        "commonMistakes": [
            {
                "mistake": "trạm xăng xe điện",
                "correction": "trạm sạc xe điện",
                "explanation": "'xăng'은 '휘발유'. 전기차는 '충전(sạc)'이지 '주유'가 아님."
            },
            {
                "mistake": "thiết bị nạp điện xe",
                "correction": "trạm sạc xe điện / thiết bị sạc xe điện",
                "explanation": "'nạp điện'은 직역이지만 'sạc'이 표준 용어."
            },
            {
                "mistake": "전기차 충전시설을 '전기차 주유소'로 번역",
                "correction": "trạm sạc xe điện",
                "explanation": "주유소(trạm xăng)는 화석연료. 전기차는 충전소(trạm sạc)."
            }
        ],
        "examples": [
            {
                "ko": "지하 주차장에 완속 충전기 20면, 급속 충전기 2면을 설치합니다.",
                "vi": "Lắp đặt 20 chỗ sạc chậm và 2 chỗ sạc nhanh ở bãi đỗ xe tầng hầm.",
                "situation": "formal"
            },
            {
                "ko": "전기차 충전시설 전기 용량은 7kW입니다.",
                "vi": "Công suất điện trạm sạc xe điện là 7kW.",
                "situation": "formal"
            },
            {
                "ko": "전기차 충전 커넥터는 Type2 규격을 사용합니다.",
                "vi": "Đầu sạc xe điện dùng chuẩn Type2.",
                "situation": "onsite"
            }
        ],
        "relatedTerms": ["전기차", "완속충전", "급속충전", "친환경자동차"]
    }
]

def add_terms_to_construction():
    """건설 용어 JSON 파일에 새 용어 추가"""
    # 파일 경로
    json_path = os.path.join(
        os.path.dirname(os.path.dirname(__file__)),
        "data",
        "terms",
        "construction.json"
    )

    # 기존 데이터 읽기
    try:
        with open(json_path, "r", encoding="utf-8") as f:
            data = json.load(f)
        print(f"✅ 기존 파일 로드 완료: {len(data)} 용어")
    except FileNotFoundError:
        print(f"❌ 파일을 찾을 수 없습니다: {json_path}")
        return
    except json.JSONDecodeError:
        print(f"❌ JSON 파싱 오류: {json_path}")
        return

    # 중복 확인 (slug 기준)
    existing_slugs = {term["slug"] for term in data}
    new_slugs = {term["slug"] for term in new_terms}
    duplicates = existing_slugs & new_slugs

    if duplicates:
        print(f"⚠️  중복된 slug 발견: {duplicates}")
        print("중복 제거 후 진행합니다.")
        new_terms_filtered = [t for t in new_terms if t["slug"] not in existing_slugs]
    else:
        new_terms_filtered = new_terms

    # 새 용어 추가
    data.extend(new_terms_filtered)
    print(f"✅ {len(new_terms_filtered)}개 용어 추가 완료")

    # 파일 저장 (pretty print)
    with open(json_path, "w", encoding="utf-8") as f:
        json.dump(data, f, ensure_ascii=False, indent=2)

    print(f"✅ 저장 완료: {json_path}")
    print(f"📊 총 용어 수: {len(data)}")

if __name__ == "__main__":
    add_terms_to_construction()
