#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
건설 용어 추가 스크립트 - 가설공사 (Temporary Work) v2
10개 용어 / Tier S 품질 기준 준수
"""

import json
import os

# 용어 데이터 (배열)
terms_data = [
    {
        "slug": "hang-rao-tam-thoi",
        "korean": "가설울타리",
        "vietnamese": "Hàng rào tạm thời",
        "hanja": "假設-",
        "hanjaReading": "假(거짓 가) + 設(베풀 설)",
        "pronunciation": "까설울따리",
        "meaningKo": "공사 현장의 경계를 표시하고 외부인의 출입을 통제하기 위해 임시로 설치하는 울타리. 통역 시 '공사장 담장'이라고 풀어 설명하면 이해가 쉬우며, 베트남에서는 철판이나 컨테이너를 활용한 단단한 울타리를 선호하는 반면 한국은 철망 또는 경량 패널을 많이 사용하므로 재질과 구조를 명확히 구분해야 합니다. 높이 규정(보통 1.8m 이상)과 안전표지 부착 의무를 함께 전달하는 것이 중요합니다.",
        "meaningVi": "Hàng rào được lắp đặt tạm thời để phân định ranh giới công trường và kiểm soát người ra vào. Thường có chiều cao tối thiểu 1.8m và phải gắn biển báo an toàn. Vật liệu phổ biến gồm tôn, lưới thép hoặc panel nhẹ.",
        "context": "현장 안전관리, 경계 설정, 출입 통제",
        "culturalNote": "한국은 도심 공사 시 소음·분진 차단을 위해 철판 가설울타리를 선호하고 외관 디자인에도 신경 쓰지만, 베트남은 기능 위주로 단순한 철망이나 컨테이너 울타리를 많이 사용합니다. '담장'과 '울타리'를 구분하지 않고 통칭하는 경우가 많으므로 통역 시 '임시(tạm thời)'를 강조해야 영구 구조물과 혼동을 피할 수 있습니다.",
        "commonMistakes": [
            {
                "mistake": "Hàng rào vĩnh viễn",
                "correction": "Hàng rào tạm thời",
                "explanation": "'영구 울타리'가 아닌 '임시 울타리'이므로 tạm thời 반드시 포함"
            },
            {
                "mistake": "Tường rào",
                "correction": "Hàng rào tạm thời",
                "explanation": "Tường rào는 영구 담장을 의미하므로 부적절"
            },
            {
                "mistake": "가설펜스",
                "correction": "가설울타리",
                "explanation": "외래어보다 순우리말 '울타리' 사용 권장"
            }
        ],
        "examples": [
            {
                "ko": "가설울타리 설치 완료 후 안전점검을 실시하겠습니다.",
                "vi": "Sau khi lắp đặt hàng rào tạm thời xong, chúng tôi sẽ tiến hành kiểm tra an toàn.",
                "situation": "formal"
            },
            {
                "ko": "울타리 높이가 기준에 맞는지 확인해 주세요.",
                "vi": "Vui lòng kiểm tra xem chiều cao hàng rào có đạt tiêu chuẩn không.",
                "situation": "onsite"
            },
            {
                "ko": "이 구간 울타리는 철판으로 교체해야 합니다.",
                "vi": "Hàng rào đoạn này cần thay bằng tôn.",
                "situation": "informal"
            }
        ],
        "relatedTerms": ["안전표지", "출입통제", "공사현장"],
        "difficultyLevel": "beginner",
        "frequencyScore": 95,
        "tags": ["가설공사", "안전", "현장관리"]
    },
    {
        "slug": "van-phong-cong-truong",
        "korean": "현장사무소",
        "vietnamese": "Văn phòng công trường",
        "hanja": "現場事務所",
        "hanjaReading": "現(나타날 현) + 場(마당 장) + 事(일 사) + 務(힘쓸 무) + 所(바 소)",
        "pronunciation": "현장사무소",
        "meaningKo": "건설 현장에서 공사 관리와 행정 업무를 수행하기 위해 임시로 설치하는 사무 공간. 통역 시 '현장 사무실' 또는 '공사장 오피스'라고 부연하면 이해가 빠르며, 컨테이너형·조립식·프리패브 등 구조 형식과 냉난방 설비 유무를 함께 전달해야 합니다. 베트남에서는 간이 천막 사무소도 흔하지만 한국은 법적으로 일정 규모 이상 현장은 견고한 사무소 설치가 의무이므로 기준을 명확히 안내해야 합니다.",
        "meaningVi": "Không gian văn phòng lắp đặt tạm thời tại công trường để quản lý thi công và xử lý công việc hành chính. Thường làm bằng container, nhà lắp ghép hoặc prefab, có trang bị điều hòa hoặc quạt tùy quy mô.",
        "context": "현장 관리, 행정 업무, 회의",
        "culturalNote": "한국 현장사무소는 법적으로 일정 면적과 환기·채광 기준을 충족해야 하며, 안전보건관리 책임자 상주 의무가 있어 규모가 큰 편입니다. 베트남은 소규모 현장에서 천막이나 간이 컨테이너로 대체하는 경우가 많고, 에어컨 없이 선풍기만 사용하는 경우도 흔합니다. '사무소'를 '오피스'로 혼용하지 말고 văn phòng으로 통일해야 합니다.",
        "commonMistakes": [
            {
                "mistake": "Nhà ở công nhân",
                "correction": "Văn phòng công trường",
                "explanation": "근로자 숙소(nhà ở)와 사무소(văn phòng)는 다른 시설"
            },
            {
                "mistake": "Office hiện trường",
                "correction": "Văn phòng công trường",
                "explanation": "외래어 혼용보다 순수 베트남어 사용"
            },
            {
                "mistake": "현장캠프",
                "correction": "현장사무소",
                "explanation": "'캠프'는 숙소 포함 복합시설, 사무소는 업무 공간"
            }
        ],
        "examples": [
            {
                "ko": "내일 오전 9시 현장사무소에서 공정회의가 있습니다.",
                "vi": "Ngày mai 9h sáng có họp tiến độ tại văn phòng công trường.",
                "situation": "formal"
            },
            {
                "ko": "사무소 에어컨 고장났으니 수리 요청하세요.",
                "vi": "Điều hòa ở văn phòng hỏng rồi, yêu cầu sửa chữa đi.",
                "situation": "onsite"
            },
            {
                "ko": "컨테이너 사무소 2개 더 설치할 계획입니다.",
                "vi": "Dự định lắp thêm 2 văn phòng container.",
                "situation": "informal"
            }
        ],
        "relatedTerms": ["컨테이너", "조립식건물", "현장관리"],
        "difficultyLevel": "beginner",
        "frequencyScore": 90,
        "tags": ["가설공사", "현장관리", "시설"]
    },
    {
        "slug": "dien-tam-thoi",
        "korean": "가설전기",
        "vietnamese": "Điện tạm thời",
        "hanja": "假設電氣",
        "hanjaReading": "假(거짓 가) + 設(베풀 설) + 電(번개 전) + 氣(기운 기)",
        "pronunciation": "까설전끼",
        "meaningKo": "공사 현장에서 공사 기간 중 임시로 사용하기 위해 설치하는 전기 설비. 통역 시 '임시 전기 배선'이라고 부연하면 명확하며, 전압(220V/380V), 배전반 위치, 누전차단기 설치 여부, 접지 상태 등을 구체적으로 전달해야 합니다. 베트남은 전압 불안정과 무단 인입 사고가 많으므로 한국의 엄격한 안전 기준을 강조해야 하며, '정식 전기'와 혼동하지 않도록 주의가 필요합니다.",
        "meaningVi": "Hệ thống điện lắp đặt tạm thời tại công trường phục vụ thi công. Bao gồm tủ điện, dây dẫn, ổ cắm và thiết bị bảo vệ như CB, ELCB. Phải tuân thủ tiêu chuẩn an toàn và có заземление đầy đủ.",
        "context": "현장 안전, 전기 공사, 장비 운영",
        "culturalNote": "한국은 가설전기 설치 시 전기안전공사 검사를 받아야 하고 누전차단기·접지 의무가 엄격하지만, 베트남은 검사 없이 무단으로 전기를 끌어다 쓰는 경우가 많아 감전 사고가 빈번합니다. '가설'을 강조하지 않으면 '정식 전기 인입'으로 오해할 수 있으므로 tạm thời를 반드시 명시해야 하며, 전압 차이(한국 220V/380V, 베트남 220V/380V 동일하나 주파수 50Hz 동일)도 확인이 필요합니다.",
        "commonMistakes": [
            {
                "mistake": "Điện chính thức",
                "correction": "Điện tạm thời",
                "explanation": "정식 전기가 아닌 임시 전기이므로 tạm thời 필수"
            },
            {
                "mistake": "가설전원",
                "correction": "가설전기",
                "explanation": "'전원'보다 '전기'가 포괄적이고 정확"
            },
            {
                "mistake": "Hệ thống điện công trường",
                "correction": "Điện tạm thời",
                "explanation": "간결하게 '임시 전기'로 표현하는 것이 현장에서 통용"
            }
        ],
        "examples": [
            {
                "ko": "가설전기 배전반에 누전차단기가 설치되어 있는지 확인하십시오.",
                "vi": "Vui lòng kiểm tra xem tủ điện tạm thời có lắp ELCB chưa.",
                "situation": "formal"
            },
            {
                "ko": "전기줄 늘어져 있으니 정리 좀 해.",
                "vi": "Dây điện rủ xuống rồi, dọn dẹp đi.",
                "situation": "onsite"
            },
            {
                "ko": "380V 전기 끌어오는 데 며칠 걸릴까요?",
                "vi": "Kéo điện 380V mất mấy ngày ạ?",
                "situation": "informal"
            }
        ],
        "relatedTerms": ["배전반", "누전차단기", "접지"],
        "difficultyLevel": "intermediate",
        "frequencyScore": 88,
        "tags": ["가설공사", "전기", "안전"]
    },
    {
        "slug": "nuoc-tam-thoi",
        "korean": "가설수도",
        "vietnamese": "Nước tạm thời",
        "hanja": "假設水道",
        "hanjaReading": "假(거짓 가) + 設(베풀 설) + 水(물 수) + 道(길 도)",
        "pronunciation": "까설수도",
        "meaningKo": "건설 현장에서 공사 기간 중 임시로 사용하기 위해 설치하는 수도 설비. 통역 시 '임시 상수도' 또는 '공사용 물 배관'이라고 부연하면 이해가 쉬우며, 수압, 관경, 급수 지점, 동파 방지 조치 등을 함께 전달해야 합니다. 베트nam에서는 지하수나 빗물을 무단으로 사용하는 경우가 많지만, 한국은 상수도 정식 인입 또는 임시 급수전 설치가 의무이므로 법적 요건을 명확히 안내해야 합니다.",
        "meaningVi": "Hệ thống cấp nước lắp đặt tạm thời tại công trường phục vụ thi công và sinh hoạt. Gồm đường ống, van, vòi nước và đồng hồ đo. Phải đảm bảo áp lực và chất lượng nước đạt tiêu chuẩn, có biện pháp chống đóng băng mùa đông.",
        "context": "현장 위생, 급수 설비, 콘크리트 양생",
        "culturalNote": "한국은 가설수도 설치 시 상수도 사업소에 신청하여 임시 급수전을 설치하고 수도요금을 정기 납부하지만, 베트남은 지하수 펌핑이나 인근 수도에서 무단 인입하는 경우가 많아 분쟁이 잦습니다. 겨울철 동파 방지(보온재 감기)는 한국에서 필수이나 베트남에서는 불필요하므로 지역별 차이를 설명해야 하며, '수도'와 '용수'를 구분(수도는 상수, 용수는 공업용수 포함)해야 합니다.",
        "commonMistakes": [
            {
                "mistake": "Nước ngầm",
                "correction": "Nước tạm thời",
                "explanation": "지하수가 아닌 상수도 기반 임시 급수"
            },
            {
                "mistake": "가설급수",
                "correction": "가설수도",
                "explanation": "'급수'보다 '수도'가 포괄적"
            },
            {
                "mistake": "Hệ thống cấp nước chính thức",
                "correction": "Nước tạm thời",
                "explanation": "정식 설비가 아닌 임시 설비"
            }
        ],
        "examples": [
            {
                "ko": "가설수도 배관 동파 방지를 위해 보온재를 감아주세요.",
                "vi": "Vui lòng quấn ống nước tạm thời bằng vật liệu cách nhiệt để chống đóng băng.",
                "situation": "formal"
            },
            {
                "ko": "수도 수압이 약해서 콘크리트 타설에 문제 있어.",
                "vi": "Áp lực nước yếu, ảnh hưởng đến đổ bê tông.",
                "situation": "onsite"
            },
            {
                "ko": "수도 미터기 검침 결과 알려주세요.",
                "vi": "Cho biết kết quả đọc đồng hồ nước.",
                "situation": "informal"
            }
        ],
        "relatedTerms": ["급수전", "수압", "동파방지"],
        "difficultyLevel": "intermediate",
        "frequencyScore": 82,
        "tags": ["가설공사", "설비", "현장관리"]
    },
    {
        "slug": "duong-tam-thoi",
        "korean": "가설도로",
        "vietnamese": "Đường tạm thời",
        "hanja": "假設道路",
        "hanjaReading": "假(거짓 가) + 設(베풀 설) + 道(길 도) + 路(길 로)",
        "pronunciation": "까설도로",
        "meaningKo": "공사 현장 내에서 차량과 장비의 이동을 위해 임시로 조성하는 도로. 통역 시 '공사용 임시 길' 또는 '작업용 통로'라고 부연하면 이해가 쉬우며, 노폭, 포장 상태(쇄석·아스콘·철판), 배수 시설, 하중 제한 등을 명확히 전달해야 합니다. 베트남은 비포장 흙길을 그대로 쓰는 경우가 많지만, 한국은 대형 장비 통행을 위해 쇄석 다짐이나 철판 깔기가 일반적이므로 시공 방법을 구체적으로 설명해야 합니다.",
        "meaningVi": "Đường làm tạm thời trong công trường để xe cộ và thiết bị di chuyển. Thường trải đá dăm đầm chặt hoặc lát tấm thép, có rãnh thoát nước. Phải đảm bảo độ rộng tối thiểu 3.5m cho xe tải nặng.",
        "context": "현장 동선, 장비 이동, 안전 관리",
        "culturalNote": "한국 대형 현장에서는 가설도로를 철판이나 아스팔트 임시 포장으로 시공하여 우기에도 통행이 원활하지만, 베트남은 흙을 다져 쓰다가 우기에 진흙탕이 되는 경우가 많습니다. '도로'와 '통로'를 구분(도로는 차량용, 통로는 보행용)하고, 하중 제한(tonage limit)을 명확히 표시해야 안전사고를 예방할 수 있습니다. 철판 깔기(lát tấm thép)는 한국 특유의 공법이므로 설명이 필요합니다.",
        "commonMistakes": [
            {
                "mistake": "Đường chính thức",
                "correction": "Đường tạm thời",
                "explanation": "정식 도로가 아닌 임시 도로"
            },
            {
                "mistake": "가설통로",
                "correction": "가설도로",
                "explanation": "'통로'는 보행용, '도로'는 차량용"
            },
            {
                "mistake": "Đường đất",
                "correction": "Đường tạm thời trải đá dăm / lát thép",
                "explanation": "단순 흙길이 아닌 포장 방식 명시 필요"
            }
        ],
        "examples": [
            {
                "ko": "가설도로에 철판을 깔아 덤프트럭이 다닐 수 있게 하겠습니다.",
                "vi": "Chúng tôi sẽ lát tấm thép trên đường tạm thời để xe ben có thể đi lại.",
                "situation": "formal"
            },
            {
                "ko": "비 오니까 도로 진흙 범벅이네, 쇄석 좀 더 깔아.",
                "vi": "Mưa nên đường lầy quá, trải thêm đá dăm đi.",
                "situation": "onsite"
            },
            {
                "ko": "이 도로는 25톤 이상 차량 통행 금지예요.",
                "vi": "Đường này cấm xe trên 25 tấn.",
                "situation": "informal"
            }
        ],
        "relatedTerms": ["쇄석", "철판", "배수로"],
        "difficultyLevel": "beginner",
        "frequencyScore": 85,
        "tags": ["가설공사", "현장관리", "안전"]
    },
    {
        "slug": "gian-giao",
        "korean": "비계",
        "vietnamese": "Giàn giáo",
        "hanja": "飛階",
        "hanjaReading": "飛(날 비) + 階(섬돌 계)",
        "pronunciation": "비계",
        "meaningKo": "건물 외벽이나 구조물 시공 시 작업자가 안전하게 작업할 수 있도록 임시로 설치하는 발판 구조물. 통역 시 '작업 발판' 또는 '공사용 비계대'라고 부연하면 이해가 쉬우며, 강관비계·시스템비계·달비계 등 종류와 조립 방식, 안전난간·발판 간격, 수직·수평 하중 등을 명확히 전달해야 합니다. 베트nam에서는 대나무 비계도 사용하지만 한국은 금속제만 허용되므로 재질 차이를 설명해야 하며, 추락 방지가 핵심임을 강조해야 합니다.",
        "meaningVi": "Kết cấu tạm thời lắp dựng bên ngoài tường hoặc công trình để công nhân làm việc an toàn trên cao. Gồm giàn giáo ống thép, giàn giáo hệ thống (system scaffold), giàn treo. Phải có lan can, sàn làm việc và liên kết chắc chắn.",
        "context": "고소 작업, 외벽 시공, 안전 관리",
        "culturalNote": "베트남은 저층 건물에서 대나무 비계(giàn giáo tre)를 여전히 사용하지만 한국은 법적으로 금속제 강관비계만 허용되며, 조립·해체 시 '비계기능사' 자격증 소지자가 감독해야 합니다. '비계'라는 용어 자체가 생소할 수 있으므로 'giàn giáo(발판 구조)'로 설명하고, 추락 방지를 위한 안전난간(lan can)과 안전그물(lưới an toàn) 설치를 반드시 함께 안내해야 합니다.",
        "commonMistakes": [
            {
                "mistake": "Thang",
                "correction": "Giàn giáo",
                "explanation": "사다리(thang)와 비계(giàn giáo)는 다른 장비"
            },
            {
                "mistake": "발판",
                "correction": "비계",
                "explanation": "'발판'은 비계의 일부(sàn làm việc), 전체 구조물은 '비계'"
            },
            {
                "mistake": "Giàn giáo tre",
                "correction": "Giàn giáo thép",
                "explanation": "한국은 대나무가 아닌 금속제만 사용"
            }
        ],
        "examples": [
            {
                "ko": "비계 조립 완료 후 안전점검을 실시하고 작업 허가를 받으십시오.",
                "vi": "Sau khi lắp giàn giáo xong, thực hiện kiểm tra an toàn và xin giấy phép làm việc.",
                "situation": "formal"
            },
            {
                "ko": "비계 발판 간격이 너무 넓어, 좁혀서 다시 설치해.",
                "vi": "Khoảng cách sàn giàn giáo quá rộng, lắp lại gần hơn.",
                "situation": "onsite"
            },
            {
                "ko": "이번 주말까지 비계 해체 끝낼 수 있어요?",
                "vi": "Cuối tuần này tháo giàn giáo xong được không?",
                "situation": "informal"
            }
        ],
        "relatedTerms": ["강관비계", "시스템비계", "안전난간"],
        "difficultyLevel": "intermediate",
        "frequencyScore": 92,
        "tags": ["가설공사", "안전", "고소작업"]
    },
    {
        "slug": "gian-giao-he-thong",
        "korean": "시스템비계",
        "vietnamese": "Giàn giáo hệ thống",
        "hanja": None,
        "hanjaReading": None,
        "pronunciation": "시스템비계",
        "meaningKo": "표준화된 부재를 조립하여 빠르고 안전하게 설치할 수 있는 비계 시스템. 통역 시 '조립식 비계' 또는 '모듈형 비계'라고 부연하면 이해가 쉬우며, 강관비계보다 조립 속도가 빠르고 안전하다는 장점을 강조해야 합니다. 수직재·수평재·가새재·발판이 규격화되어 있어 오조립 위험이 적고, 하중 계산이 명확하므로 대형 현장에서 선호됩니다. 베트남에서는 아직 강관비계가 주류이므로 시스템비계의 장점과 임대 비용, 조립 교육 필요성을 함께 전달해야 합니다.",
        "meaningVi": "Hệ thống giàn giáo lắp ghép với các bộ phận tiêu chuẩn hóa, lắp đặt nhanh và an toàn hơn giàn giáo ống thép truyền thống. Gồm trụ đứng, xà ngang, thanh chống chéo và sàn làm việc theo module, dễ tính toán tải trọng và ít sai sót lắp đặt.",
        "context": "고소 작업, 대형 현장, 안전 관리",
        "culturalNote": "한국 대형 현장에서는 시스템비계가 표준화되어 있고 임대 업체가 많지만, 베트남은 초기 투자 비용 문제로 여전히 강관비계를 많이 사용합니다. '시스템'이라는 외래어를 그대로 쓰되 'hệ thống(체계)'으로 풀어 설명하고, 조립 속도와 안전성이 높아 장기적으로 경제적이라는 점을 강조해야 합니다. 부재 규격(예: 수직재 간격 1.8m, 발판 폭 0.4m)도 함께 안내하면 좋습니다.",
        "commonMistakes": [
            {
                "mistake": "Giàn giáo ống thép",
                "correction": "Giàn giáo hệ thống",
                "explanation": "강관비계와 시스템비계는 다른 시스템"
            },
            {
                "mistake": "조립식비계",
                "correction": "시스템비계",
                "explanation": "업계 표준 용어는 '시스템비계'"
            },
            {
                "mistake": "Giàn giáo lắp ráp",
                "correction": "Giàn giáo hệ thống",
                "explanation": "모든 비계가 조립식이므로 '시스템'으로 구분"
            }
        ],
        "examples": [
            {
                "ko": "시스템비계를 사용하면 조립 기간을 30% 단축할 수 있습니다.",
                "vi": "Sử dụng giàn giáo hệ thống có thể rút ngắn thời gian lắp đặt 30%.",
                "situation": "formal"
            },
            {
                "ko": "시스템비계 부재 하나 분실됐는데 어디서 구하지?",
                "vi": "Mất một bộ phận giàn giáo hệ thống, mua ở đâu nhỉ?",
                "situation": "onsite"
            },
            {
                "ko": "임대료가 비싸도 시스템비계가 안전해서 선택했어요.",
                "vi": "Tuy tiền thuê đắt nhưng chọn giàn giáo hệ thống vì an toàn hơn.",
                "situation": "informal"
            }
        ],
        "relatedTerms": ["비계", "강관비계", "조립"],
        "difficultyLevel": "intermediate",
        "frequencyScore": 78,
        "tags": ["가설공사", "안전", "고소작업"]
    },
    {
        "slug": "san-an-toan",
        "korean": "안전발판",
        "vietnamese": "Sàn an toàn",
        "hanja": "安全-",
        "hanjaReading": "安(편안 안) + 全(온전 전)",
        "pronunciation": "안전발판",
        "meaningKo": "비계나 작업대에서 작업자가 안전하게 서서 일할 수 있도록 설치하는 발을 디딜 수 있는 판. 통역 시 '작업용 발디딤판' 또는 '비계 바닥판'이라고 부연하면 이해가 쉬우며, 재질(목재·금속·합성수지), 폭(최소 40cm), 간격(최대 3cm), 고정 방식 등을 명확히 전달해야 합니다. 발판이 견고하지 않거나 간격이 넓으면 추락 사고로 이어지므로 안전 기준 준수가 필수이며, 미끄럼 방지 처리 여부도 중요합니다.",
        "meaningVi": "Tấm sàn lắp trên giàn giáo hoặc bục làm việc để công nhân đứng làm việc an toàn. Thường làm bằng gỗ, kim loại hoặc nhựa tổng hợp, rộng tối thiểu 40cm, khe hở không quá 3cm, phải cố định chắc chắn và chống trơn trượt.",
        "context": "고소 작업, 비계 시공, 안전 관리",
        "culturalNote": "한국은 안전발판 폭과 간격, 적재 하중(보통 250kg/㎡)이 법으로 규정되어 있고, 목재 발판은 두께 3.5cm 이상 사용해야 하지만, 베트남은 기준이 느슨하여 얇은 판자나 대나무를 쓰다가 파손되는 사고가 잦습니다. '발판'을 단순히 'sàn(바닥)'이라고만 하면 건물 바닥과 혼동되므로 'sàn làm việc(작업 바닥)' 또는 'sàn an toàn(안전 바닥)'으로 명확히 구분해야 합니다.",
        "commonMistakes": [
            {
                "mistake": "Ván",
                "correction": "Sàn an toàn",
                "explanation": "단순 판자가 아닌 안전 기준을 충족하는 발판"
            },
            {
                "mistake": "작업판",
                "correction": "안전발판",
                "explanation": "안전 강조를 위해 '안전발판' 사용"
            },
            {
                "mistake": "Sàn giàn giáo",
                "correction": "Sàn an toàn",
                "explanation": "'안전(an toàn)'을 명시하여 안전 기준 강조"
            }
        ],
        "examples": [
            {
                "ko": "안전발판 간격이 3cm를 초과하지 않도록 설치하십시오.",
                "vi": "Vui lòng lắp sàn an toàn sao cho khe hở không vượt quá 3cm.",
                "situation": "formal"
            },
            {
                "ko": "발판 하나 부러졌으니 교체해 주세요.",
                "vi": "Tấm sàn bị gãy rồi, thay cái mới đi.",
                "situation": "onsite"
            },
            {
                "ko": "이 발판 미끄러워서 위험해, 미끄럼방지 처리해야 돼.",
                "vi": "Sàn này trơn nguy hiểm, phải xử lý chống trượt.",
                "situation": "informal"
            }
        ],
        "relatedTerms": ["비계", "안전난간", "추락방지"],
        "difficultyLevel": "beginner",
        "frequencyScore": 87,
        "tags": ["가설공사", "안전", "고소작업"]
    },
    {
        "slug": "lan-can-an-toan",
        "korean": "안전난간",
        "vietnamese": "Lan can an toàn",
        "hanja": "安全欄干",
        "hanjaReading": "安(편안 안) + 全(온전 전) + 欄(난간 란) + 干(방패 간)",
        "pronunciation": "안전난간",
        "meaningKo": "비계나 개구부에서 작업자의 추락을 방지하기 위해 설치하는 난간. 통역 시 '추락 방지 난간' 또는 '안전 울타리'라고 부연하면 이해가 쉬우며, 상부난간(90~120cm 높이), 중간난간, 발끝막이판(10cm 이상) 구조와 강도 기준을 명확히 전달해야 합니다. 난간 없이 작업하면 추락 사고로 이어지므로 설치가 의무이며, 임시 제거 시에도 안전조치(안전대 착용 등)가 필수임을 강조해야 합니다.",
        "meaningVi": "Lan can lắp đặt trên giàn giáo hoặc cạnh khe hở để ngăn công nhân rơi xuống. Gồm thanh lan can trên (cao 90~120cm), thanh lan can giữa và tấm chắn chân (cao tối thiểu 10cm). Phải chịu lực tối thiểu 100kg theo phương ngang.",
        "context": "고소 작업, 개구부 안전, 추락 방지",
        "culturalNote": "한국은 안전난간 설치가 법적 의무이고 높이·강도 기준이 엄격하지만(상부 난간 90cm 이상, 중간 난간 필수), 베트남은 규정은 있으나 현장에서 잘 지키지 않아 추락 사고가 많습니다. '난간'을 'lan can'으로 그대로 쓰되, '안전(an toàn)'을 강조하여 단순 장식용 난간과 구분해야 하며, 발끝막이판(toe board)의 중요성도 함께 설명해야 합니다(공구·자재 낙하 방지).",
        "commonMistakes": [
            {
                "mistake": "Lan can",
                "correction": "Lan can an toàn",
                "explanation": "장식 난간과 구분하기 위해 'an toàn' 필수"
            },
            {
                "mistake": "추락방지대",
                "correction": "안전난간",
                "explanation": "'방지대'는 개인보호구, '난간'은 구조물"
            },
            {
                "mistake": "Tay vịn",
                "correction": "Lan can an toàn",
                "explanation": "손잡이(tay vịn)가 아닌 구조적 난간"
            }
        ],
        "examples": [
            {
                "ko": "안전난간 상부는 90cm 이상, 중간난간과 발끝막이판을 반드시 설치하십시오.",
                "vi": "Lan can trên phải cao tối thiểu 90cm, bắt buộc có thanh giữa và tấm chắn chân.",
                "situation": "formal"
            },
            {
                "ko": "난간 빠진 데 있으니 즉시 보수해.",
                "vi": "Có chỗ thiếu lan can, sửa ngay.",
                "situation": "onsite"
            },
            {
                "ko": "자재 반입하려고 난간 임시로 풀었는데 작업 끝나면 바로 다시 달아야 돼.",
                "vi": "Tháo lan can tạm để nhập vật tư, xong việc phải lắp lại ngay.",
                "situation": "informal"
            }
        ],
        "relatedTerms": ["비계", "안전발판", "추락방지"],
        "difficultyLevel": "beginner",
        "frequencyScore": 90,
        "tags": ["가설공사", "안전", "고소작업"]
    },
    {
        "slug": "ke-chong-roi",
        "korean": "낙하물방지선반",
        "vietnamese": "Kệ chống rơi",
        "hanja": "落下物防止-",
        "hanjaReading": "落(떨어질 락) + 下(아래 하) + 物(물건 물) + 防(막을 방) + 止(그칠 지)",
        "pronunciation": "나카물방지선반",
        "meaningKo": "고소 작업 시 공구나 자재가 떨어지는 것을 방지하기 위해 비계 외부에 설치하는 선반 구조물. 통역 시 '낙하 방지 선반' 또는 '공구 낙하 방지대'라고 부연하면 이해가 쉬우며, 설치 높이(1층마다 또는 10m마다), 폭(60cm 이상), 경사각(20도 이상) 등을 명확히 전달해야 합니다. 낙하물로 인한 하부 작업자나 보행자 사고를 예방하는 중요한 안전시설이므로 설치 의무를 강조해야 하며, 안전방망과 함께 사용됩니다.",
        "meaningVi": "Kệ lắp đặt bên ngoài giàn giáo để ngăn dụng cụ hoặc vật liệu rơi xuống, bảo vệ người làm việc bên dưới và người đi bộ. Thường lắp mỗi tầng hoặc cứ 10m chiều cao, rộng tối thiểu 60cm, nghiêng 20 độ trở lên để chặn vật rơi.",
        "context": "고소 작업, 안전 관리, 낙하물 방지",
        "culturalNote": "한국은 일정 높이 이상 작업 시 낙하물방지선반 설치가 법적 의무이고, 설치하지 않으면 과태료가 부과되지만, 베트남은 규정이 있어도 현장에서 잘 지키지 않아 낙하물 사고가 빈번합니다. '선반'을 'kệ'로 번역하되, '낙하 방지(chống rơi)'를 강조해야 하며, 안전방망(lưới an toàn)과의 차이(선반은 고체, 방망은 그물)를 설명해야 합니다. 공구 분실 방지 효과도 있습니다.",
        "commonMistakes": [
            {
                "mistake": "Lưới an toàn",
                "correction": "Kệ chống rơi",
                "explanation": "안전방망(그물)과 낙하물방지선반(판)은 다름"
            },
            {
                "mistake": "낙하방지망",
                "correction": "낙하물방지선반",
                "explanation": "'망'은 그물, '선반'은 판 구조물"
            },
            {
                "mistake": "Kệ đỡ",
                "correction": "Kệ chống rơi",
                "explanation": "단순 받침대가 아닌 '낙하 방지' 강조"
            }
        ],
        "examples": [
            {
                "ko": "낙하물방지선반을 10m 간격으로 설치하여 하부 작업자 안전을 확보하십시오.",
                "vi": "Vui lòng lắp kệ chống rơi cứ mỗi 10m để đảm bảo an toàn cho công nhân bên dưới.",
                "situation": "formal"
            },
            {
                "ko": "선반에 자재 쌓지 말고 바로 치워, 과하중 위험해.",
                "vi": "Đừng chất vật liệu trên kệ, dọn ngay đi, quá tải nguy hiểm.",
                "situation": "onsite"
            },
            {
                "ko": "낙하물방지선반 덕분에 떨어진 공구가 안 내려갔네.",
                "vi": "Nhờ kệ chống rơi mà dụng cụ rơi không xuống được.",
                "situation": "informal"
            }
        ],
        "relatedTerms": ["비계", "안전방망", "낙하물"],
        "difficultyLevel": "intermediate",
        "frequencyScore": 75,
        "tags": ["가설공사", "안전", "고소작업"]
    }
]

def main():
    # 파일 경로
    file_path = "/Users/mac/Documents/claude_code/projects/vn.epicstage.co.kr/src/data/terms/construction.json"

    # 기존 파일 읽기
    if os.path.exists(file_path):
        with open(file_path, 'r', encoding='utf-8') as f:
            existing_data = json.load(f)
    else:
        existing_data = []

    # 기존 slug 목록
    existing_slugs = {term['slug'] for term in existing_data}

    # 중복 확인 및 추가
    added_count = 0
    for term in terms_data:
        if term['slug'] in existing_slugs:
            print(f"⚠️  중복: {term['slug']} (건너뜀)")
        else:
            existing_data.append(term)
            existing_slugs.add(term['slug'])
            added_count += 1
            print(f"✅ 추가: {term['slug']} - {term['korean']}")

    # 파일 저장
    with open(file_path, 'w', encoding='utf-8') as f:
        json.dump(existing_data, f, ensure_ascii=False, indent=2)

    print(f"\n🎉 완료: {added_count}개 용어 추가됨")
    print(f"📊 총 용어 수: {len(existing_data)}개")

if __name__ == "__main__":
    main()
