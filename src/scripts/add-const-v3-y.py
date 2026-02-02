#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
건설 용어 추가 스크립트 v3-y
테마: 소방/피난 (Firefighting & Evacuation)
Tier S 기준 (90점 이상)
"""

import json
import os

# 추가할 용어 데이터 (10개)
new_terms = [
    {
        "slug": "cua-chong-chay",
        "korean": "방화문",
        "vietnamese": "Cửa chống cháy",
        "hanja": "防火門",
        "hanjaReading": "防(막을 방) 火(불 화) 門(문 문)",
        "pronunciation": "방화문",
        "meaningKo": "화재 시 불길과 연기의 확산을 차단하기 위해 내화성능을 갖춘 특수 제작된 문입니다. 통역 시 '자동 폐쇄 장치(automatic closing device)'와 '내화 등급(fire resistance rating)'을 함께 설명해야 하며, 베트남어로는 단순히 'cửa'가 아닌 'cửa chống cháy'로 명확히 구분해야 합니다. 일반문과 혼동하지 않도록 '소방 인증(chứng nhận PCCC - Phòng cháy chữa cháy)'을 받은 제품임을 강조하세요.",
        "meaningVi": "Cửa được chế tạo đặc biệt với khả năng chịu lửa, ngăn chặn sự lan rộng của ngọn lửa và khói trong trường hợp hỏa hoạn. Phải có chứng nhận PCCC và hệ thống đóng tự động.",
        "context": "소방 설비, 피난 계획, 건축 안전",
        "culturalNote": "한국은 건축법상 일정 규모 이상 건물에 방화문 설치가 의무이며, 등급(60분, 90분 내화)이 엄격히 구분됩니다. 베트남도 최근 소방 규정이 강화되고 있으나 한국만큼 세분화되지 않았으며, 현장에서 'cửa sắt'(철문)과 혼동하는 경우가 많습니다. 방화문은 단순 철문이 아니라 내화 충전재가 들어간 인증 제품임을 명확히 해야 합니다.",
        "commonMistakes": [
            {
                "mistake": "cửa sắt",
                "correction": "cửa chống cháy",
                "explanation": "철문(cửa sắt)은 일반 금속문이고, 방화문은 내화 성능이 있는 특수문입니다."
            },
            {
                "mistake": "cửa thoát hiểm",
                "correction": "cửa chống cháy / cửa thoát nạn",
                "explanation": "방화문은 불을 막는 문이고, 비상구(cửa thoát hiểm)는 대피용 출구입니다. 기능이 다릅니다."
            },
            {
                "mistake": "cửa không cháy",
                "correction": "cửa chống cháy (cửa chịu lửa)",
                "explanation": "'불에 타지 않는 문'이 아니라 '일정 시간 불을 견디는 문'이므로 'chống cháy' 또는 'chịu lửa'가 정확합니다."
            }
        ],
        "examples": [
            {
                "ko": "60분 내화 성능의 방화문을 복도 양쪽에 설치하세요.",
                "vi": "Lắp đặt cửa chống cháy chịu lửa 60 phút ở hai bên hành lang.",
                "situation": "formal"
            },
            {
                "ko": "방화문은 항상 닫혀 있어야 합니다. 고임목으로 열어두지 마세요.",
                "vi": "Cửa chống cháy phải luôn đóng. Không được chặn cửa bằng gỗ.",
                "situation": "onsite"
            },
            {
                "ko": "이 방화문은 자동 폐쇄 장치가 고장났으니 즉시 수리하세요.",
                "vi": "Cửa chống cháy này bị hỏng thiết bị đóng tự động, sửa ngay.",
                "situation": "onsite"
            }
        ],
        "relatedTerms": ["방화셔터", "제연설비", "비상구", "내화구조"]
    },
    {
        "slug": "rem-chong-chay",
        "korean": "방화셔터",
        "vietnamese": "Rèm chống cháy",
        "hanja": "防火shutter",
        "hanjaReading": "防(막을 방) 火(불 화)",
        "pronunciation": "방화셔터",
        "meaningKo": "화재 발생 시 자동으로 내려와 불길과 연기의 수평 확산을 차단하는 셔터형 방화 설비입니다. 통역 시 'shutter'는 베트남어로 'rèm'(커튼형) 또는 'cửa cuốn'(롤링도어형)으로 구분하며, 한국에서는 주로 대형 개구부(통로, 에스컬레이터 주변)에 설치됩니다. 감지기 연동(fire detector linkage)과 수동 해제 장치(manual release)를 함께 설명하세요.",
        "meaningVi": "Thiết bị chống cháy dạng rèm cuốn tự động hạ xuống khi phát hiện hỏa hoạn, ngăn chặn sự lan rộng của lửa và khói theo chiều ngang. Thường lắp ở lối đi lớn, thang cuốn.",
        "context": "소방 설비, 대형 건물, 피난 동선",
        "culturalNote": "한국은 대형 상업시설, 지하철역 등에 방화셔터 설치가 의무화되어 있으며, 평소에는 천장에 수납되어 있다가 화재 시 자동으로 내려옵니다. 베트남에서는 아직 보편화되지 않아 'rèm sắt'(철 커튼) 정도로 오해하는 경우가 많습니다. 자동 감지 시스템과 연동된다는 점을 강조하세요.",
        "commonMistakes": [
            {
                "mistake": "cửa cuốn sắt",
                "correction": "rèm chống cháy / cửa cuốn chống cháy",
                "explanation": "일반 철제 셔터(cửa cuốn sắt)는 보안용이고, 방화셔터는 내화 성능이 있는 소방 설비입니다."
            },
            {
                "mistake": "màn che lửa",
                "correction": "rèm chống cháy",
                "explanation": "'불을 가리는 커튼'이 아니라 법적 인증을 받은 소방 설비이므로 'rèm chống cháy'가 정확합니다."
            },
            {
                "mistake": "tự động mở",
                "correction": "tự động hạ xuống (đóng)",
                "explanation": "화재 시 '열리는(mở)' 것이 아니라 '내려와서 닫히는(hạ xuống đóng)' 것입니다."
            }
        ],
        "examples": [
            {
                "ko": "화재 감지 시 방화셔터가 자동으로 내려와 구역을 분리합니다.",
                "vi": "Khi phát hiện cháy, rèm chống cháy tự động hạ xuống ngăn khu vực.",
                "situation": "formal"
            },
            {
                "ko": "방화셔터 아래에 물건 쌓지 마세요. 비상 시 작동이 안 됩니다.",
                "vi": "Không để đồ dưới rèm chống cháy. Khẩn cấp sẽ không hoạt động.",
                "situation": "onsite"
            },
            {
                "ko": "이 셔터는 수동으로도 내릴 수 있습니다. 빨간 버튼을 누르세요.",
                "vi": "Rèm này cũng hạ được bằng tay. Nhấn nút đỏ.",
                "situation": "onsite"
            }
        ],
        "relatedTerms": ["방화문", "방화구획", "자동폐쇄장치", "감지기"]
    },
    {
        "slug": "thiet-bi-kiem-soat-khoi",
        "korean": "제연설비",
        "vietnamese": "Thiết bị kiểm soát khói",
        "hanja": "除煙設備",
        "hanjaReading": "除(덜 제) 煙(연기 연) 設(베풀 설) 備(갖출 비)",
        "pronunciation": "제연설비",
        "meaningKo": "화재 시 발생하는 연기를 강제로 배출하거나 특정 구역으로 유입을 차단하여 인명 피해를 줄이는 소방 설비입니다. 통역 시 '제연(除煙)'은 '연기 제거'를 의미하며, 베트남어로는 'kiểm soát khói'(연기 제어) 또는 'hệ thống thông gió khẩn cấp'(비상 환기 시스템)으로 설명합니다. 급기(supply air)와 배기(exhaust)의 원리를 함께 언급하세요.",
        "meaningVi": "Hệ thống cưỡng bức đẩy khói ra ngoài hoặc ngăn khói lan vào khu vực nhất định khi hỏa hoạn, giảm thiệt hại về người. Bao gồm hệ thống cấp gió và thải khói.",
        "context": "소방 설비, 고층 건물, 피난 안전",
        "culturalNote": "한국은 고층 건물, 지하 공간에 제연설비 설치가 법적 의무이며, 자연 배연(자연 환기)과 기계 배연(팬 사용)으로 구분됩니다. 베트남에서는 '환기 시스템(thông gió)'과 혼동하는 경우가 많은데, 제연설비는 평상시가 아닌 화재 시에만 작동하는 특수 설비임을 강조하세요. 계단실 가압(stairwell pressurization)도 제연의 일종입니다.",
        "commonMistakes": [
            {
                "mistake": "hệ thống thông gió",
                "correction": "thiết bị kiểm soát khói / hệ thống thông gió khẩn cấp",
                "explanation": "일반 환기는 평상시 공기 순환이고, 제연은 화재 시 연기 배출 전용입니다."
            },
            {
                "mistake": "quạt hút khói",
                "correction": "thiết bị kiểm soát khói (hệ thống cấp gió và thải khói)",
                "explanation": "단순 배기팬이 아니라 급배기를 통합한 소방 시스템입니다."
            },
            {
                "mistake": "lọc khói",
                "correction": "kiểm soát khói (thải khói)",
                "explanation": "연기를 '정화(lọc)'하는 게 아니라 '배출(thải)'하는 시스템입니다."
            }
        ],
        "examples": [
            {
                "ko": "제연설비가 작동하면 복도에 신선한 공기가 공급되고 연기는 밖으로 배출됩니다.",
                "vi": "Khi thiết bị kiểm soát khói hoạt động, hành lang được cấp không khí sạch và khói thải ra ngoài.",
                "situation": "formal"
            },
            {
                "ko": "계단실 제연 덕분에 연기가 안 들어와서 안전하게 대피할 수 있습니다.",
                "vi": "Nhờ kiểm soát khói ở cầu thang, không có khói vào, thoát nạn an toàn.",
                "situation": "onsite"
            },
            {
                "ko": "제연 팬 점검 시 수동 작동 테스트도 같이 해주세요.",
                "vi": "Khi kiểm tra quạt thải khói, làm thử vận hành thủ công luôn.",
                "situation": "onsite"
            }
        ],
        "relatedTerms": ["배연설비", "급기가압", "방화구획", "비상환기"]
    },
    {
        "slug": "den-khan-cap",
        "korean": "비상조명",
        "vietnamese": "Đèn khẩn cấp",
        "hanja": "非常照明",
        "hanjaReading": "非(아닐 비) 常(떳떳할 상) 照(비출 조) 明(밝을 명)",
        "pronunciation": "비상조명",
        "meaningKo": "정전 시에도 일정 시간 동안 자동으로 점등되어 피난 경로를 밝혀주는 조명 설비입니다. 통역 시 '비상(非常)'은 '긴급 상황'을 의미하며, 베트남어로는 'đèn khẩn cấp' 또는 'đèn dự phòng'(예비 조명)으로 표현합니다. 배터리 내장형(battery backup)과 최소 조도(lux) 기준을 함께 설명하세요.",
        "meaningVi": "Hệ thống chiếu sáng tự động bật khi mất điện, duy trì đủ ánh sáng trong thời gian nhất định để sơ tán. Có pin dự phòng tích hợp.",
        "context": "소방 설비, 피난 안전, 전기 설비",
        "culturalNote": "한국은 건축법상 일정 규모 이상 건물에 비상조명 설치가 의무이며, 최소 30분 이상 점등(일부는 60분)되어야 합니다. 베트남에서는 'đèn dự phòng'이 일반 예비 조명과 혼동될 수 있으므로, 법적 기준을 충족한 'đèn khẩn cấp PCCC'(소방 비상조명)임을 명확히 하세요. 유도등(exit sign)과는 구분되는 개념입니다.",
        "commonMistakes": [
            {
                "mistake": "đèn dự phòng bình thường",
                "correction": "đèn khẩn cấp PCCC",
                "explanation": "일반 예비 조명이 아니라 소방법 기준을 충족한 비상조명입니다."
            },
            {
                "mistake": "đèn báo lối thoát",
                "correction": "đèn khẩn cấp / đèn chiếu sáng khẩn cấp",
                "explanation": "유도등(exit sign)은 방향 표시이고, 비상조명은 공간 전체를 밝히는 조명입니다."
            },
            {
                "mistake": "đèn tự động bật",
                "correction": "đèn khẩn cấp tự động sáng khi mất điện",
                "explanation": "단순 자동등이 아니라 '정전 시 자동 점등'되는 특수 조명임을 명시하세요."
            }
        ],
        "examples": [
            {
                "ko": "정전이 되면 비상조명이 자동으로 켜져서 30분간 유지됩니다.",
                "vi": "Khi mất điện, đèn khẩn cấp tự động sáng và duy trì 30 phút.",
                "situation": "formal"
            },
            {
                "ko": "비상조명 배터리 상태 점검하고 교체 주기 확인하세요.",
                "vi": "Kiểm tra pin đèn khẩn cấp và xác nhận chu kỳ thay.",
                "situation": "onsite"
            },
            {
                "ko": "이 복도 비상조명이 안 들어오네요. 전기 담당자 불러주세요.",
                "vi": "Đèn khẩn cấp hành lang này không sáng. Gọi điện công.",
                "situation": "onsite"
            }
        ],
        "relatedTerms": ["유도등", "유도표지", "피난구유도등", "객석유도등"]
    },
    {
        "slug": "den-chi-dan-thoat-nạn",
        "korean": "유도등",
        "vietnamese": "Đèn chỉ dẫn thoát nạn",
        "hanja": "誘導燈",
        "hanjaReading": "誘(꾀할 유) 導(인도할 도) 燈(등불 등)",
        "pronunciation": "유도등",
        "meaningKo": "화재 등 비상 상황 시 피난 방향과 출구를 표시하는 조명 장치입니다. 통역 시 '유도(誘導)'는 '안내, 인도'를 의미하며, 베트남어로는 'đèn chỉ dẫn thoát nạn' 또는 'đèn exit'로 표현합니다. 피난구유도등(exit sign), 통로유도등(corridor light), 계단유도등(stairway light)으로 구분되며, 항상 점등 상태를 유지해야 합니다.",
        "meaningVi": "Thiết bị chiếu sáng chỉ hướng thoát nạn và lối ra trong tình huống khẩn cấp như hỏa hoạn. Bao gồm đèn exit, đèn hành lang, đèn cầu thang. Phải luôn sáng.",
        "context": "소방 설비, 피난 유도, 안전 표지",
        "culturalNote": "한국은 소방법상 건물 규모에 따라 유도등 설치가 의무이며, 녹색(초록색) 바탕에 흰색 픽토그램이 표준입니다. 베트남에서는 'đèn exit' 또는 'biển thoát hiểm'(비상구 표지)로 불리며, 색상과 디자인이 통일되지 않은 경우가 많습니다. 한국 기준에서는 항상 점등(상시점등형) 또는 비상시 점등(비상점등형)으로 나뉘므로 명확히 구분하세요.",
        "commonMistakes": [
            {
                "mistake": "biển báo thoát hiểm",
                "correction": "đèn chỉ dẫn thoát nạn (đèn exit)",
                "explanation": "단순 표지판(biển báo)이 아니라 자체 발광하는 조명 장치입니다."
            },
            {
                "mistake": "đèn cửa ra",
                "correction": "đèn chỉ dẫn lối thoát nạn",
                "explanation": "'출구 조명'이 아니라 '비상 탈출 경로 안내등'이므로 'thoát nạn'을 명시하세요."
            },
            {
                "mistake": "chỉ sáng khi cháy",
                "correction": "luôn sáng hoặc sáng khi khẩn cấp (tùy loại)",
                "explanation": "상시점등형은 항상 켜져 있고, 비상점등형만 화재 시 점등됩니다."
            }
        ],
        "examples": [
            {
                "ko": "유도등을 따라가면 가장 가까운 비상구로 나갈 수 있습니다.",
                "vi": "Đi theo đèn chỉ dẫn sẽ ra được lối thoát nạn gần nhất.",
                "situation": "formal"
            },
            {
                "ko": "계단 유도등이 고장났으니 오늘 중으로 교체하세요.",
                "vi": "Đèn chỉ dẫn cầu thang hỏng, thay trong hôm nay.",
                "situation": "onsite"
            },
            {
                "ko": "피난구 유도등은 녹색 바탕에 사람 달리는 표시가 있습니다.",
                "vi": "Đèn exit có nền xanh lá, biểu tượng người chạy.",
                "situation": "onsite"
            }
        ],
        "relatedTerms": ["비상조명", "피난구", "비상구", "피난유도선"]
    },
    {
        "slug": "cau-thang-thoat-nan",
        "korean": "비상계단",
        "vietnamese": "Cầu thang thoát nạn",
        "hanja": "非常階段",
        "hanjaReading": "非(아닐 비) 常(떳떗할 상) 階(섬돌 계) 段(층계 단)",
        "pronunciation": "비상계단",
        "meaningKo": "화재 등 비상 상황 시 안전하게 대피할 수 있도록 설계된 전용 계단입니다. 통역 시 '특별피난계단(special evacuation stairway)'과 '일반 비상계단'을 구분하며, 베트남어로는 'cầu thang thoát nạn' 또는 'cầu thang PCCC'로 표현합니다. 제연설비(smoke control), 방화문(fire door), 비상조명이 갖춰진 독립된 구조임을 강조하세요.",
        "meaningVi": "Cầu thang được thiết kế riêng để sơ tán an toàn trong tình huống khẩn cấp như hỏa hoạn. Có hệ thống kiểm soát khói, cửa chống cháy, đèn khẩn cấp. Cấu trúc độc lập.",
        "context": "소방 설비, 피난 계획, 건축 설계",
        "culturalNote": "한국은 건축법상 고층 건물(11층 이상)은 특별피난계단 설치가 의무이며, 계단실 내부는 양압(positive pressure)을 유지해 연기 유입을 차단합니다. 베트남에서는 비상계단이 창고나 잡동사니 보관 공간으로 사용되는 경우가 많은데, 한국에서는 엄격히 금지되며 정기 점검 대상입니다. 항상 통행 가능한 상태 유지가 필수임을 명시하세요.",
        "commonMistakes": [
            {
                "mistake": "cầu thang phụ",
                "correction": "cầu thang thoát nạn (cầu thang PCCC)",
                "explanation": "보조 계단(phụ)이 아니라 법적으로 지정된 비상 대피 전용 계단입니다."
            },
            {
                "mistake": "cầu thang ngoài",
                "correction": "cầu thang thoát nạn (có thể ở ngoài hoặc trong)",
                "explanation": "실외 계단(ngoài)뿐 아니라 실내 특별피난계단도 있으므로 위치가 아닌 용도로 구분하세요."
            },
            {
                "mistake": "để đồ ở cầu thang",
                "correction": "cấm để đồ ở cầu thang thoát nạn",
                "explanation": "비상계단에는 어떤 물건도 보관 금지입니다. 한국에서는 법적 처벌 대상입니다."
            }
        ],
        "examples": [
            {
                "ko": "화재 경보가 울리면 엘리베이터 말고 비상계단으로 대피하세요.",
                "vi": "Khi chuông báo cháy kêu, không dùng thang máy, đi cầu thang thoát nạn.",
                "situation": "formal"
            },
            {
                "ko": "비상계단에 짐 쌓아두지 마세요. 소방 점검 나오면 과태료 나옵니다.",
                "vi": "Không để đồ ở cầu thang thoát nạn. Thanh tra PCCC phạt tiền.",
                "situation": "onsite"
            },
            {
                "ko": "특별피난계단은 전실이 있어서 연기가 안 들어옵니다.",
                "vi": "Cầu thang thoát nạn đặc biệt có tiền thất, không vào khói.",
                "situation": "onsite"
            }
        ],
        "relatedTerms": ["특별피난계단", "피난층", "대피공간", "전실"]
    },
    {
        "slug": "khong-gian-ti-nan",
        "korean": "대피공간",
        "vietnamese": "Không gian tị nạn",
        "hanja": "待避空間",
        "hanjaReading": "待(기다릴 대) 避(피할 피) 空(빌 공) 間(사이 간)",
        "pronunciation": "대피공간",
        "meaningKo": "고층 건물에서 화재 시 일시적으로 대피하여 구조를 기다릴 수 있는 안전 공간입니다. 통역 시 '대피(待避)'는 '임시 피난'을 의미하며, 베트남어로는 'không gian tị nạn' 또는 'khu vực trú ẩn tạm thời'로 표현합니다. 발코니형, 계단실 부속실형 등이 있으며, 내화구조(fire-resistant structure)와 외기 개방(outdoor access)이 필수입니다.",
        "meaningVi": "Không gian an toàn trong nhà cao tầng để tạm trú khi hỏa hoạn, chờ cứu hộ. Có cấu trúc chịu lửa và tiếp xúc với không khí bên ngoài. Dạng ban công hoặc phòng phụ cầu thang.",
        "context": "소방 설비, 고층 건물, 피난 안전",
        "culturalNote": "한국은 11층 이상 아파트에 대피공간 설치가 의무화되어 있으며(2011년 이후), 발코니 한쪽에 방화문으로 구획된 공간입니다. 베트남은 아직 이러한 제도가 없어 생소한 개념이므로, '엘리베이터로 탈출 불가 시 임시 대기 공간'임을 명확히 설명하세요. 절대 창고나 세탁실로 사용해서는 안 됩니다.",
        "commonMistakes": [
            {
                "mistake": "phòng an toàn",
                "correction": "không gian tị nạn (khu vực trú ẩn tạm thời)",
                "explanation": "완전한 안전실(phòng)이 아니라 임시 대피 공간(không gian)입니다."
            },
            {
                "mistake": "ban công bình thường",
                "correction": "không gian tị nạn (khu vực ban công chống cháy)",
                "explanation": "일반 발코니가 아니라 방화 구획된 법적 대피 공간입니다."
            },
            {
                "mistake": "để đồ tạm",
                "correction": "cấm để đồ - phải để trống hoàn toàn",
                "explanation": "임시 보관도 금지입니다. 항상 비워두어야 합니다."
            }
        ],
        "examples": [
            {
                "ko": "대피공간은 비상시를 위한 곳이니 짐을 쌓아두지 마세요.",
                "vi": "Không gian tị nạn dành cho khẩn cấp, không để đồ.",
                "situation": "formal"
            },
            {
                "ko": "불이 나면 대피공간으로 가서 문 닫고 구조 기다리세요.",
                "vi": "Khi cháy, vào không gian tị nạn, đóng cửa và chờ cứu hộ.",
                "situation": "onsite"
            },
            {
                "ko": "이 아파트는 대피공간이 발코니 쪽에 있습니다. 방화문으로 구분되어 있어요.",
                "vi": "Căn hộ này có không gian tị nạn ở phía ban công. Ngăn bằng cửa chống cháy.",
                "situation": "onsite"
            }
        ],
        "relatedTerms": ["비상계단", "피난층", "특별피난계단", "방화구획"]
    },
    {
        "slug": "voi-chua-chay-trong-nha",
        "korean": "옥내소화전",
        "vietnamese": "Vòi chữa cháy trong nhà",
        "hanja": "屋內消火栓",
        "hanjaReading": "屋(집 옥) 內(안 내) 消(끌 소) 火(불 화) 栓(마개 전)",
        "pronunciation": "옥내소화전",
        "meaningKo": "건물 내부에 설치된 소화용 급수 설비로, 화재 초기에 호스를 연결하여 직접 진화할 수 있는 장치입니다. 통역 시 '옥내(屋內)'는 '건물 내부'를 의미하며, 베트남어로는 'vòi chữa cháy trong nhà' 또는 'hydrant nội bộ'로 표현합니다. 소화전함(fire hose cabinet) 안에 호스, 노즐, 밸브가 갖춰져 있으며, 정기 점검 대상입니다.",
        "meaningVi": "Thiết bị cấp nước chữa cháy lắp đặt bên trong tòa nhà, dùng ống mềm để dập lửa giai đoạn đầu. Trong tủ có ống, vòi phun, van. Phải kiểm tra định kỳ.",
        "context": "소방 설비, 화재 진압, 자체 소방",
        "culturalNote": "한국은 연면적 3,000㎡ 이상 건물에 옥내소화전 설치가 의무이며, 각 층 보행거리 25m 이내마다 설치됩니다. 베트남에서는 'vòi nước cứu hỏa'(소방 호스)로 통칭하나, 옥내소화전은 건물 내부 전용 설비로 고압 펌프와 연결되어 있음을 명확히 하세요. 일반 수도와는 별도 배관입니다.",
        "commonMistakes": [
            {
                "mistake": "vòi nước thường",
                "correction": "vòi chữa cháy trong nhà (hệ thống PCCC)",
                "explanation": "일반 수도꼭지가 아니라 소방 전용 고압 급수 설비입니다."
            },
            {
                "mistake": "bình cứu hỏa",
                "correction": "vòi chữa cháy trong nhà (không phải bình)",
                "explanation": "소화기(bình)가 아니라 호스 릴 방식의 소화전입니다."
            },
            {
                "mistake": "chỉ cứu hỏa dùng",
                "correction": "nhân viên được đào tạo có thể dùng",
                "explanation": "소방관 전용이 아니라 교육받은 직원도 초기 진화에 사용 가능합니다."
            }
        ],
        "examples": [
            {
                "ko": "옥내소화전은 빨간 박스 안에 있고, 유리창을 깨면 사용할 수 있습니다.",
                "vi": "Vòi chữa cháy trong nhà ở trong hộp đỏ, đập kính sẽ dùng được.",
                "situation": "formal"
            },
            {
                "ko": "소화전 점검 때 호스 압력 테스트하고 누수 확인하세요.",
                "vi": "Kiểm tra vòi, test áp lực ống và xác nhận rò rỉ.",
                "situation": "onsite"
            },
            {
                "ko": "이 층 소화전 밸브가 녹슬어서 안 열립니다. 교체 필요해요.",
                "vi": "Van vòi tầng này bị rỉ, không mở được. Cần thay.",
                "situation": "onsite"
            }
        ],
        "relatedTerms": ["옥외소화전", "스프링클러", "소화기", "방수총"]
    },
    {
        "slug": "voi-chua-chay-ngoai-troi",
        "korean": "옥외소화전",
        "vietnamese": "Vòi chữa cháy ngoài trời",
        "hanja": "屋外消火栓",
        "hanjaReading": "屋(집 옥) 外(밖 외) 消(끌 소) 火(불 화) 栓(마개 전)",
        "pronunciation": "옥외소화전",
        "meaningKo": "건물 외부 또는 대지 내에 설치된 소화용 급수 설비로, 소방차가 접근하기 어려운 곳에서 소방 호스를 연결하여 사용합니다. 통역 시 '옥외(屋外)'는 '건물 밖'을 의미하며, 베트남어로는 'vòi chữa cháy ngoài trời' 또는 'trụ cứu hỏa'로 표현합니다. 지상형과 지하식이 있으며, 공공 소화전과는 구분되는 건물 부속 설비입니다.",
        "meaningVi": "Thiết bị cấp nước chữa cháy lắp đặt bên ngoài tòa nhà hoặc trong khuôn viên, dùng khi xe cứu hỏa khó tiếp cận. Có dạng trên mặt đất và dưới đất. Thiết bị phụ thuộc của tòa nhà.",
        "context": "소방 설비, 화재 진압, 외부 소방",
        "culturalNote": "한국은 대형 건물 부지 내에 옥외소화전 설치가 의무이며, 소방펌프실과 직결되어 있습니다. 베트남에서는 공공 소화전(trụ nước PCCC công cộng)과 혼동하는 경우가 많은데, 옥외소화전은 해당 건물 소유주가 관리하는 사유 설비임을 명확히 하세요. 겨울철 동파 방지(freeze protection)도 중요 포인트입니다.",
        "commonMistakes": [
            {
                "mistake": "trụ nước công cộng",
                "correction": "vòi chữa cháy ngoài trời (của tòa nhà)",
                "explanation": "공공 소화전이 아니라 건물 소유주 관리 설비입니다."
            },
            {
                "mistake": "chỉ xe cứu hỏa dùng",
                "correction": "xe cứu hỏa hoặc nhân viên được đào tạo",
                "explanation": "소방차 전용이 아니라 교육받은 인원도 사용 가능합니다."
            },
            {
                "mistake": "vòi tưới cây",
                "correction": "vòi chữa cháy ngoài trời (PCCC chuyên dụng)",
                "explanation": "조경용 호스가 아니라 소방 전용 고압 설비입니다."
            }
        ],
        "examples": [
            {
                "ko": "옥외소화전은 주차장 입구 쪽에 빨간 기둥으로 표시되어 있습니다.",
                "vi": "Vòi chữa cháy ngoài trời ở lối vào bãi xe, cột đỏ.",
                "situation": "formal"
            },
            {
                "ko": "겨울에 옥외소화전 동파 방지 점검 꼭 해주세요.",
                "vi": "Mùa đông nhớ kiểm tra chống đông vòi ngoài trời.",
                "situation": "onsite"
            },
            {
                "ko": "이 소화전은 지하식이라 뚜껑 열고 호스 연결해야 합니다.",
                "vi": "Vòi này dạng dưới đất, mở nắp rồi nối ống.",
                "situation": "onsite"
            }
        ],
        "relatedTerms": ["옥내소화전", "소방펌프실", "급수배관", "방수구"]
    },
    {
        "slug": "thiet-bi-phun-nuoc-lien-ket",
        "korean": "연결살수설비",
        "vietnamese": "Thiết bị phun nước liên kết",
        "hanja": "連結撒水設備",
        "hanjaReading": "連(이을 연) 結(맺을 결) 撒(뿌릴 살) 水(물 수) 設(베풀 설) 備(갖출 비)",
        "pronunciation": "연결살수설비",
        "meaningKo": "소방차의 물 공급을 건물 내부 배관에 연결하여 자동으로 살수하는 소화 설비입니다. 통역 시 '연결(連結)'은 '소방차와 연결'을 의미하며, 베트남어로는 'thiết bị phun nước liên kết' 또는 'hệ thống sprinkler kết nối xe cứu hỏa'로 표현합니다. 지하층, 무창층 등 스프링클러 설치가 어려운 곳에 주로 설치되며, 송수구(fire department connection)를 통해 급수합니다.",
        "meaningVi": "Hệ thống chữa cháy tự động phun nước bằng cách kết nối cấp nước từ xe cứu hỏa vào đường ống bên trong tòa nhà. Thường lắp ở tầng hầm, khu vực không cửa sổ. Cấp nước qua đầu nối xe cứu hỏa.",
        "context": "소방 설비, 지하 공간, 화재 진압",
        "culturalNote": "한국은 지하층이 있는 건물이나 무창층에 연결살수설비 설치가 의무이며, 건물 외벽에 '송수구' 표시가 있습니다. 베트남에서는 생소한 개념이므로, '소방차 없이는 작동 안 하는 스프링클러'로 설명하면 이해가 빠릅니다. 일반 스프링클러는 자체 물탱크로 작동하지만, 연결살수는 외부 급수가 필수입니다.",
        "commonMistakes": [
            {
                "mistake": "sprinkler tự động",
                "correction": "thiết bị phun nước liên kết (cần xe cứu hỏa)",
                "explanation": "일반 스프링클러는 자동이지만, 연결살수는 소방차 급수가 필수입니다."
            },
            {
                "mistake": "tự động phun khi cháy",
                "correction": "phun khi xe cứu hỏa cấp nước",
                "explanation": "화재 감지만으로는 작동하지 않고, 송수구에 소방차가 물을 공급해야 합니다."
            },
            {
                "mistake": "hệ thống nước riêng",
                "correction": "hệ thống phụ thuộc nước từ xe cứu hỏa",
                "explanation": "자체 물탱크가 없고 외부 급수에 의존합니다."
            }
        ],
        "examples": [
            {
                "ko": "지하 2층은 연결살수설비가 있어서 소방차가 송수구에 연결하면 자동으로 살수됩니다.",
                "vi": "Tầng hầm 2 có thiết bị phun nước liên kết, xe cứu hỏa nối vào đầu cấp nước sẽ tự động phun.",
                "situation": "formal"
            },
            {
                "ko": "송수구 위치 확인하고 주차 금지 표시 해주세요. 소방차가 접근해야 합니다.",
                "vi": "Xác nhận vị trí đầu cấp nước và dán cấm đỗ xe. Xe cứu hỏa phải vào được.",
                "situation": "onsite"
            },
            {
                "ko": "연결살수 헤드는 스프링클러처럼 생겼지만 물탱크 없이 외부 급수로만 작동합니다.",
                "vi": "Đầu phun nước liên kết giống sprinkler nhưng không có bồn nước, chỉ chạy bằng cấp nước ngoài.",
                "situation": "onsite"
            }
        ],
        "relatedTerms": ["스프링클러", "송수구", "옥내소화전", "제연설비"]
    }
]

def main():
    # 파일 경로 설정
    base_dir = os.path.dirname(os.path.abspath(__file__))
    json_path = os.path.join(base_dir, "..", "data", "terms", "construction.json")

    # 기존 데이터 읽기
    with open(json_path, "r", encoding="utf-8") as f:
        data = json.load(f)

    # 새 용어 추가
    data.extend(new_terms)

    # 저장
    with open(json_path, "w", encoding="utf-8") as f:
        json.dump(data, f, ensure_ascii=False, indent=2)

    print(f"✅ {len(new_terms)}개 용어 추가 완료")
    print(f"📁 파일: {json_path}")
    print(f"📊 총 용어 수: {len(data)}개")

if __name__ == "__main__":
    main()
