#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
건설(Construction) 용어 추가 스크립트 v8
테마: 신재생에너지설비 (Renewable Energy Systems)
- 태양광인버터, 풍력발전, 지열히트펌프, ESS, 전기차충전기 등
Tier S 기준 준수
"""

import json
import os

# 파일 경로 설정
file_path = os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', 'data', 'terms', 'construction.json')

# 추가할 용어 데이터 (10개)
data = [
    {
        "slug": "bo-bien-tan-nang-luong-mat-troi",
        "korean": "태양광인버터",
        "vietnamese": "Bộ biến tần năng lượng mặt trời",
        "hanja": "太陽光inverter",
        "hanjaReading": "太(클 태) + 陽(볕 양) + 光(빛 광)",
        "pronunciation": "태양광인버터",
        "meaningKo": "태양광 패널에서 생산된 직류(DC) 전기를 교류(AC) 전기로 변환하는 장치입니다. 통역 시 'inverter'를 '인버터'로 그대로 쓰는 경우가 많지만, 베트남어로는 'bộ biến tần'이라고 명확히 표현해야 합니다. 용량(kW), 효율(%), MPPT 방식 등 기술 사양을 정확히 전달하는 것이 중요하며, 한국에서는 '인버터'로 통칭하지만 베트남에서는 기능을 설명하는 'bộ biến tần'이 더 일반적입니다. 설치 위치(옥내/옥외), 냉각 방식(자연냉각/강제냉각) 등도 함께 통역해야 합니다.",
        "meaningVi": "Thiết bị chuyển đổi điện một chiều (DC) từ tấm pin mặt trời thành điện xoay chiều (AC). Là thành phần quan trọng trong hệ thống điện mặt trời, quyết định hiệu suất chuyển đổi năng lượng.",
        "context": "신재생에너지설비, 태양광발전",
        "culturalNote": "한국은 태양광 인버터를 주로 옥내 설치를 선호하고 용량별로 엄격히 구분하는 반면, 베트남은 열대기후 특성상 냉각 성능과 방수 등급을 더 중시합니다. 한국에서는 'SMP(계통한계가격)' 기준으로 수익성을 계산하지만, 베트남은 'FIT(발전차액지원)' 제도를 사용했었고 현재는 직접 PPA 계약으로 전환되고 있어 통역 시 제도 차이를 명확히 설명해야 합니다.",
        "commonMistakes": [
            {
                "mistake": "inverter를 '인버터'로 음역만 하는 경우",
                "correction": "bộ biến tần (변환기) 또는 bộ nghịch lưu",
                "explanation": "베트남어로는 기능을 설명하는 용어를 사용해야 이해가 빠름"
            },
            {
                "mistake": "MPPT를 설명 없이 그대로 사용",
                "correction": "MPPT (điểm công suất cực đại) - 최대전력점 추적",
                "explanation": "약어는 반드시 풀어서 설명해야 함"
            },
            {
                "mistake": "kW와 kWh를 혼동하여 통역",
                "correction": "kW(용량), kWh(발전량)를 명확히 구분",
                "explanation": "용량과 발전량은 완전히 다른 개념"
            }
        ],
        "examples": [
            {
                "ko": "이 태양광 인버터는 99kW 용량에 최대효율 98.5%입니다.",
                "vi": "Bộ biến tần năng lượng mặt trời này có công suất 99kW với hiệu suất tối đa 98,5%.",
                "situation": "formal"
            },
            {
                "ko": "인버터가 과열되면 자동으로 출력을 제한합니다.",
                "vi": "Khi bộ biến tần quá nhiệt, nó sẽ tự động giới hạn công suất đầu ra.",
                "situation": "onsite"
            },
            {
                "ko": "MPPT 방식으로 발전효율을 극대화합니다.",
                "vi": "Tối ưu hóa hiệu suất phát điện bằng phương pháp MPPT (theo dõi điểm công suất cực đại).",
                "situation": "formal"
            }
        ],
        "relatedTerms": [
            "태양광패널",
            "직류전원",
            "교류전원",
            "계통연계"
        ]
    },
    {
        "slug": "he-thong-phat-dien-gio",
        "korean": "풍력발전",
        "vietnamese": "Hệ thống phát điện gió",
        "hanja": "風力發電",
        "hanjaReading": "風(바람 풍) + 力(힘 력) + 發(필 발) + 電(번개 전)",
        "pronunciation": "풍력발전",
        "meaningKo": "바람의 운동에너지를 전기에너지로 변환하는 발전 방식입니다. 통역 시 육상풍력(onshore)과 해상풍력(offshore)을 명확히 구분해야 하며, 터빈 용량(MW), 허브 높이(hub height), 로터 직경(rotor diameter) 등 기술 사양을 정확히 전달해야 합니다. 한국에서는 주로 '풍력발전기'라고 하지만 베트남어로는 'hệ thống phát điện gió'(시스템) 또는 'tuabin gió'(터빈)로 구분하여 사용하므로 주의가 필요합니다. 설비용량, 설비이용률(capacity factor), 연간발전량 등도 함께 통역해야 합니다.",
        "meaningVi": "Phương thức phát điện chuyển đổi động năng của gió thành điện năng. Bao gồm tuabin gió, tháp, hệ thống truyền động và máy phát điện. Phân loại thành phát điện gió trên bờ và ngoài khơi.",
        "context": "신재생에너지설비, 발전설비",
        "culturalNote": "한국은 산악지형과 해상풍력을 주로 개발하며 주민 수용성 문제가 크지만, 베트남은 중남부 해안과 메콩델타 지역의 풍부한 바람자원을 활용하여 대규모 풍력단지를 조성하고 있습니다. 한국은 '발전사업허가' 절차가 복잡하지만, 베트남은 '투자등록증명서(IRC)'와 'PPA 계약'이 핵심이므로 통역 시 제도 차이를 명확히 해야 합니다. 또한 한국은 20년 고정가격 계약(FIT)에서 경쟁입찰(REC)로 전환되었고, 베트nam도 유사한 변화를 겪고 있어 최신 정책을 숙지해야 합니다.",
        "commonMistakes": [
            {
                "mistake": "wind turbine을 '풍력터빈'으로만 통역",
                "correction": "tuabin gió (터빈) 또는 hệ thống phát điện gió (시스템)",
                "explanation": "맥락에 따라 개별 터빈인지 전체 시스템인지 구분 필요"
            },
            {
                "mistake": "offshore를 '해안풍력'으로 잘못 통역",
                "correction": "offshore = phát điện gió ngoài khơi (해상풍력)",
                "explanation": "해안(ven biển)과 해상(ngoài khơi)은 다른 개념"
            },
            {
                "mistake": "MW와 MWh를 혼동",
                "correction": "MW(용량), MWh(발전량) 명확히 구분",
                "explanation": "설비용량과 발전량은 전혀 다른 지표"
            }
        ],
        "examples": [
            {
                "ko": "3MW급 풍력발전기 20기를 설치하여 총 60MW 규모의 풍력단지를 조성합니다.",
                "vi": "Lắp đặt 20 tuabin gió công suất 3MW để xây dựng trang trại điện gió quy mô tổng cộng 60MW.",
                "situation": "formal"
            },
            {
                "ko": "허브 높이는 100m이고 로터 직경은 120m입니다.",
                "vi": "Chiều cao trục (hub height) là 100m và đường kính cánh quạt (rotor) là 120m.",
                "situation": "formal"
            },
            {
                "ko": "설비이용률이 30%면 연간 약 15,000MWh를 생산합니다.",
                "vi": "Với hệ số công suất 30%, sản xuất khoảng 15.000 MWh điện năng mỗi năm.",
                "situation": "onsite"
            }
        ],
        "relatedTerms": [
            "해상풍력",
            "터빈",
            "발전기",
            "블레이드"
        ]
    },
    {
        "slug": "bom-nhiet-dia-nhiet",
        "korean": "지열히트펌프",
        "vietnamese": "Bơm nhiệt địa nhiệt",
        "hanja": "地熱heat pump",
        "hanjaReading": "地(땅 지) + 熱(더울 열)",
        "pronunciation": "지열히트펌프",
        "meaningKo": "땅속의 일정한 온도를 이용하여 냉난방을 하는 열펌프 시스템입니다. 통역 시 'heat pump'를 '히트펌프'로 음역하지 말고 'bơm nhiệt'(열펌프)로 정확히 표현해야 합니다. 수직밀폐형(vertical closed-loop), 수평밀폐형(horizontal closed-loop), 개방형(open-loop) 등 방식을 구분하고, 천공깊이(boring depth), COP(성능계수), 냉매 종류 등을 정확히 통역해야 합니다. 한국에서는 '지열 냉난방'이라고 하지만 베트남어로는 '냉방'과 '난방'을 각각 'làm lạnh'와 'sưởi ấm'으로 구분하여 설명하는 것이 좋습니다.",
        "meaningVi": "Hệ thống bơm nhiệt sử dụng nhiệt độ ổn định của lòng đất để làm lạnh và sưởi ấm. Hiệu quả cao hơn hệ thống điều hòa thông thường, tiết kiệm năng lượng 30-50%.",
        "context": "신재생에너지설비, 냉난방설비",
        "culturalNote": "한국은 4계절이 뚜렷하여 냉난방이 모두 중요하지만, 베트남은 열대기후라 주로 냉방 수요가 높아 지열 시스템의 경제성이 다릅니다. 한국에서는 천공깊이 150~200m가 일반적이지만, 베트남 남부는 지하수위가 높아 수평형 또는 얕은 수직형이 선호됩니다. 통역 시 'COP(성능계수)'는 베트남어로 'hệ số hiệu suất'로 표현하며, 값이 클수록 효율이 좋다는 것을 명확히 설명해야 합니다. 또한 한국은 '신재생에너지 의무비율(RPS)' 인정을 받지만, 베트남은 아직 지열 관련 인센티브가 부족하여 초기투자 회수기간이 길다는 점도 함께 안내해야 합니다.",
        "commonMistakes": [
            {
                "mistake": "heat pump를 '히트펌프'로 음역",
                "correction": "bơm nhiệt (열펌프)",
                "explanation": "베트남어로는 기능을 설명하는 용어 사용"
            },
            {
                "mistake": "지열을 'địa nhiệt' 대신 'nhiệt độ đất'로 통역",
                "correction": "địa nhiệt (지열) - 전문용어 사용",
                "explanation": "공식 용어를 사용해야 전문성 유지"
            },
            {
                "mistake": "COP를 설명 없이 숫자만 전달",
                "correction": "COP (hệ số hiệu suất) 3.5 = 전기 1kW로 냉난방 3.5kW 생산",
                "explanation": "기술 지표는 의미를 함께 설명해야 함"
            }
        ],
        "examples": [
            {
                "ko": "수직밀폐형으로 150m 천공 5공을 설치합니다.",
                "vi": "Lắp đặt hệ thống kín dạng thẳng đứng với 5 giếng khoan sâu 150m.",
                "situation": "formal"
            },
            {
                "ko": "이 지열 시스템은 COP 4.2로 기존 에어컨보다 40% 절감됩니다.",
                "vi": "Hệ thống địa nhiệt này có COP 4,2, tiết kiệm 40% so với điều hòa thông thường.",
                "situation": "onsite"
            },
            {
                "ko": "지하 15도 온도를 활용해서 여름엔 냉방, 겨울엔 난방합니다.",
                "vi": "Sử dụng nhiệt độ 15°C dưới lòng đất để làm lạnh vào mùa hè và sưởi ấm vào mùa đông.",
                "situation": "informal"
            }
        ],
        "relatedTerms": [
            "열펌프",
            "천공",
            "냉매",
            "성능계수"
        ]
    },
    {
        "slug": "he-thong-luu-tru-nang-luong",
        "korean": "에너지저장장치",
        "vietnamese": "Hệ thống lưu trữ năng lượng (ESS)",
        "hanja": "energy貯藏裝置",
        "hanjaReading": "貯(저축할 저) + 藏(감출 장) + 裝(꾸밀 장) + 置(둘 치)",
        "pronunciation": "에너지저장장치",
        "meaningKo": "전기를 배터리에 저장했다가 필요할 때 사용하는 시스템으로, ESS로 약칭합니다. 통역 시 'ESS'를 그대로 쓰되 반드시 'hệ thống lưu trữ năng lượng'이라고 풀어서 설명해야 합니다. 용량(kWh 또는 MWh), 출력(kW 또는 MW), 배터리 종류(리튬이온, LFP 등), BMS(배터리관리시스템), PCS(전력변환장치) 등 구성요소를 정확히 통역해야 합니다. 한국에서는 '피크저감', '주파수조정' 등 용도별로 구분하지만, 베트남에서는 주로 태양광/풍력 연계용으로 사용되므로 맥락 파악이 중요합니다. 화재안전 기준(UL9540A, KS 등)도 함께 설명해야 합니다.",
        "meaningVi": "Hệ thống lưu trữ điện năng trong pin (battery) để sử dụng khi cần thiết. Thường kết hợp với năng lượng tái tạo (mặt trời, gió) để ổn định nguồn điện và giảm đỉnh tải.",
        "context": "신재생에너지설비, 전력설비",
        "culturalNote": "한국은 ESS를 전력시장의 주파수조정용(FR), 피크저감용으로 활발히 사용하며 '전력거래소'를 통한 수익모델이 확립되어 있지만, 베트남은 아직 전력시장이 초기 단계라 주로 자가소비(self-consumption)용으로 설치됩니다. 한국은 2017~2019년 ESS 화재사고 이후 안전기준이 매우 엄격해졌으나, 베트남은 아직 관련 규정이 미흡하여 한국 기준을 참고하여 통역해야 합니다. 'kWh(용량)'와 'kW(출력)'의 차이를 명확히 설명하지 않으면 오해가 발생하므로 주의가 필요합니다.",
        "commonMistakes": [
            {
                "mistake": "ESS를 설명 없이 약어만 사용",
                "correction": "ESS (hệ thống lưu trữ năng lượng) - Energy Storage System",
                "explanation": "약어는 반드시 풀어서 설명 필요"
            },
            {
                "mistake": "BMS를 '배터리 매니지먼트'로 음역",
                "correction": "BMS (hệ thống quản lý pin) - Battery Management System",
                "explanation": "기능을 설명하는 베트남어 사용"
            },
            {
                "mistake": "용량(kWh)과 출력(kW)을 혼동",
                "correction": "kWh = 저장용량, kW = 충방전 출력",
                "explanation": "완전히 다른 개념이므로 반드시 구분"
            }
        ],
        "examples": [
            {
                "ko": "1MWh 용량, 500kW 출력의 리튬이온 배터리 ESS를 설치합니다.",
                "vi": "Lắp đặt ESS pin lithium-ion dung lượng 1MWh, công suất 500kW.",
                "situation": "formal"
            },
            {
                "ko": "PCS가 배터리 DC를 계통 AC로 변환합니다.",
                "vi": "PCS (bộ chuyển đổi công suất) chuyển đổi DC từ pin thành AC của lưới điện.",
                "situation": "onsite"
            },
            {
                "ko": "화재감지 및 자동소화장치를 필수로 설치해야 합니다.",
                "vi": "Phải lắp đặt bắt buộc thiết bị phát hiện và dập lửa tự động.",
                "situation": "formal"
            }
        ],
        "relatedTerms": [
            "배터리",
            "리튬이온",
            "전력변환장치",
            "충방전"
        ]
    },
    {
        "slug": "tram-sac-xe-dien",
        "korean": "전기차충전기",
        "vietnamese": "Trạm sạc xe điện",
        "hanja": "電氣車充電機",
        "hanjaReading": "電(번개 전) + 氣(기운 기) + 車(수레 차) + 充(채울 충) + 電(번개 전) + 機(틀 기)",
        "pronunciation": "전기차충전기",
        "meaningKo": "전기자동차에 전기를 공급하는 충전설비로, EV 충전기 또는 전기차 충전소라고도 합니다. 통역 시 완속충전기(AC, 7kW 이하)와 급속충전기(DC, 50kW 이상), 초급속충전기(ultra-fast, 350kW)를 명확히 구분해야 합니다. 커넥터 타입(Type1, Type2, CCS, CHAdeMO 등), 충전속도(kW), 동시충전 대수, 결제시스템(RFID, 앱, 신용카드) 등도 정확히 통역해야 합니다. 한국은 '환경부 보조금', '전기요금 할인', '의무설치(주차장 등)' 제도가 있지만 베트남은 아직 초기 단계이므로 제도 차이를 명확히 해야 합니다.",
        "meaningVi": "Thiết bị cung cấp điện năng cho xe ô tô điện. Phân loại: sạc chậm (AC, dưới 7kW), sạc nhanh (DC, từ 50kW), sạc siêu nhanh (trên 350kW). Thường lắp tại bãi đỗ xe, trung tâm thương mại, trạm xăng.",
        "context": "신재생에너지설비, 전기설비",
        "culturalNote": "한국은 전기차 보급이 빠르게 증가하며 아파트, 공공기관, 고속도로 휴게소 등에 의무적으로 충전기를 설치해야 하지만, 베트남은 아직 전기차 보급 초기 단계라 주로 고급 아파트나 쇼핑몰에만 설치됩니다. 한국은 '환경부 통합플랫폼'으로 충전기 위치를 실시간 확인할 수 있지만, 베트남은 각 사업자별로 앱이 따로 있어 불편합니다. 통역 시 충전속도를 '시간당 주행거리(km/h 충전)'로 설명하면 이해가 빠릅니다(예: 50kW 급속충전으로 30분 충전 시 약 200km 주행 가능). 전기요금 체계도 한국은 '저압전력' 또는 '전기차 전용요금'이지만 베트남은 일반 산업용 요금을 적용하므로 차이가 큽니다.",
        "commonMistakes": [
            {
                "mistake": "EV charger를 '충전기'로만 통역",
                "correction": "trạm sạc xe điện (충전소) 또는 bộ sạc (충전기)",
                "explanation": "설비 전체인지 기기 하나인지 맥락에 따라 구분"
            },
            {
                "mistake": "AC/DC를 설명 없이 사용",
                "correction": "AC (교류, sạc chậm) / DC (직류, sạc nhanh)",
                "explanation": "전기 전문용어는 반드시 풀어서 설명"
            },
            {
                "mistake": "kW를 '킬로와트'로만 음역",
                "correction": "kW + 충전시간 또는 주행거리로 구체화",
                "explanation": "추상적 숫자보다 실생활 단위로 설명"
            }
        ],
        "examples": [
            {
                "ko": "50kW 급속충전기 2기를 설치하여 동시에 2대 충전 가능합니다.",
                "vi": "Lắp đặt 2 trạm sạc nhanh 50kW, có thể sạc đồng thời 2 xe.",
                "situation": "formal"
            },
            {
                "ko": "CCS 타입2 커넥터를 사용하며 30분에 80% 충전됩니다.",
                "vi": "Sử dụng đầu cắm CCS Type 2, sạc được 80% trong 30 phút.",
                "situation": "onsite"
            },
            {
                "ko": "통신형 충전기라서 앱으로 원격 제어하고 사용내역 확인 가능합니다.",
                "vi": "Là trạm sạc thông minh, có thể điều khiển từ xa qua app và kiểm tra lịch sử sử dụng.",
                "situation": "informal"
            }
        ],
        "relatedTerms": [
            "전기차",
            "급속충전",
            "완속충전",
            "커넥터"
        ]
    },
    {
        "slug": "bo-thu-nhiet-mat-troi",
        "korean": "태양열집열기",
        "vietnamese": "Bộ thu nhiệt mặt trời",
        "hanja": "太陽熱集熱器",
        "hanjaReading": "太(클 태) + 陽(볕 양) + 熱(더울 열) + 集(모을 집) + 熱(더울 열) + 器(그릇 기)",
        "pronunciation": "태양열집열기",
        "meaningKo": "태양의 복사열을 흡수하여 물 또는 공기를 가열하는 장치입니다. '태양광(전기 생산)'과 '태양열(온수 생산)'을 명확히 구분해야 하며, 통역 시 '태양광은 điện mặt trời', '태양열은 nhiệt mặt trời'로 반드시 구분하여 표현해야 합니다. 평판형(flat plate), 진공관형(evacuated tube), 집광형(concentrator) 등 종류와 집열 효율(%), 설치 각도, 순환방식(자연순환/강제순환) 등을 정확히 통역해야 합니다. 주로 온수 생산, 난방, 산업공정열 등에 사용되며, 한국에서는 '태양열 온수기'라고 많이 부르지만 베트남어로는 'máy nước nóng năng lượng mặt trời'가 더 일반적입니다.",
        "meaningVi": "Thiết bị hấp thụ nhiệt bức xạ mặt trời để đun nóng nước hoặc không khí. Khác với pin mặt trời (sản xuất điện), bộ thu nhiệt sản xuất nước nóng cho sinh hoạt, sưởi ấm hoặc công nghiệp.",
        "context": "신재생에너지설비, 급탕설비",
        "culturalNote": "한국은 4계절이 있어 난방용 태양열 시스템을 많이 설치하지만, 베트남은 열대기후라 주로 온수(목욕, 세탁) 용도로만 사용합니다. 한국에서는 집열기 면적을 '㎡'로 표시하고 정부 보조금을 지원하지만, 베트남에서는 주로 리터(L) 단위로 온수탱크 용량을 기준으로 선택합니다. 통역 시 '태양광 패널(pin mặt trời)'과 '태양열 집열기(bộ thu nhiệt)'를 혼동하지 않도록 주의해야 하며, 한국은 겨울철 동파 방지를 위한 부동액 사용이 필수이지만 베트남은 불필요하다는 점도 설명해야 합니다. 효율은 '집열효율(thermal efficiency)'로 표현하며, 일반적으로 평판형 60~70%, 진공관형 70~80% 수준입니다.",
        "commonMistakes": [
            {
                "mistake": "태양광과 태양열을 혼동하여 통역",
                "correction": "태양광 = pin mặt trời (전기), 태양열 = bộ thu nhiệt (온수)",
                "explanation": "완전히 다른 기술이므로 반드시 구분"
            },
            {
                "mistake": "집열기를 'máy thu thập'로 직역",
                "correction": "bộ thu nhiệt (열 수집기)",
                "explanation": "전문용어 사용 필요"
            },
            {
                "mistake": "효율을 '%'만 말하고 의미 설명 안 함",
                "correction": "hiệu suất thu nhiệt 70% = 태양에너지의 70%를 열로 변환",
                "explanation": "수치의 의미를 함께 설명"
            }
        ],
        "examples": [
            {
                "ko": "진공관형 집열기 10㎡로 하루 300리터 온수를 생산합니다.",
                "vi": "Bộ thu nhiệt ống chân không 10㎡ sản xuất 300 lít nước nóng mỗi ngày.",
                "situation": "formal"
            },
            {
                "ko": "집열기를 남향으로 30도 각도로 설치하세요.",
                "vi": "Lắp đặt bộ thu nhiệt hướng nam với góc nghiêng 30 độ.",
                "situation": "onsite"
            },
            {
                "ko": "이 시스템은 강제순환 방식으로 펌프가 물을 순환시킵니다.",
                "vi": "Hệ thống này dùng phương pháp tuần hoàn cưỡng bức, bơm làm nước lưu thông.",
                "situation": "informal"
            }
        ],
        "relatedTerms": [
            "태양광패널",
            "온수탱크",
            "집열효율",
            "진공관"
        ]
    },
    {
        "slug": "he-thong-pin-nhien-lieu",
        "korean": "연료전지",
        "vietnamese": "Hệ thống pin nhiên liệu",
        "hanja": "燃料電池",
        "hanjaReading": "燃(불사를 연) + 料(헤아릴 료) + 電(번개 전) + 池(못 지)",
        "pronunciation": "연료전지",
        "meaningKo": "수소와 산소의 화학반응으로 전기를 생산하는 발전장치입니다. 통역 시 'fuel cell'을 '연료전지'로만 하지 말고 'pin nhiên liệu'(연료 배터리) 또는 'hệ thống phát điện pin nhiên liệu'로 정확히 표현해야 합니다. PEMFC(고분자전해질), SOFC(고체산화물), PAFC(인산형) 등 종류와 발전효율(%), 열병합 여부(CHP), 수소공급 방식 등을 명확히 통역해야 합니다. 한국에서는 '수소연료전지'라고 하며 가정용, 건물용, 발전용으로 구분하지만, 베트남에서는 아직 생소한 기술이므로 원리부터 설명해야 합니다. 부산물로 물과 열만 나오므로 친환경적이라는 점도 강조해야 합니다.",
        "meaningVi": "Thiết bị phát điện thông qua phản ứng hóa học giữa hydro và oxy, chỉ tạo ra điện, nước và nhiệt. Hiệu suất cao (40-60%), không gây ô nhiễm, có thể kết hợp phát điện và nhiệt (CHP).",
        "context": "신재생에너지설비, 수소에너지",
        "culturalNote": "한국은 세계적으로 연료전지 기술이 앞서 있으며 정부 주도로 '수소경제' 정책을 추진하지만, 베트남은 아직 수소인프라가 거의 없어 연료전지 보급이 미미합니다. 한국에서는 아파트 단지나 건물에 '가정용 연료전지(1kW급)'를 설치하여 전기와 온수를 동시에 생산하는 열병합 시스템이 보급되고 있으나, 베트남은 천연가스 개질 방식의 수소 생산이 주류라서 '그린수소(재생에너지 기반)'와 구분하여 통역해야 합니다. 통역 시 '발전효율'과 '종합효율(전기+열)'을 구분하고, CHP(Combined Heat and Power, 열병합)는 'phát điện kết hợp nhiệt'로 표현합니다. 한국은 1kW당 정부보조금이 있지만 베트남은 아직 인센티브가 없으므로 경제성 비교 시 주의가 필요합니다.",
        "commonMistakes": [
            {
                "mistake": "fuel cell을 '연료셀'로 음역",
                "correction": "pin nhiên liệu (연료전지)",
                "explanation": "베트남어로는 'pin(배터리)' 사용"
            },
            {
                "mistake": "수소를 'hydro'로 그대로 사용",
                "correction": "hydro (수소, khí hydro)",
                "explanation": "화학 원소는 베트남어 명칭 병기"
            },
            {
                "mistake": "CHP를 설명 없이 약어만 사용",
                "correction": "CHP (phát điện kết hợp nhiệt) - 전기+온수 동시 생산",
                "explanation": "약어는 풀어서 설명 필요"
            }
        ],
        "examples": [
            {
                "ko": "1kW 가정용 연료전지는 하루 24kWh 전기와 온수를 생산합니다.",
                "vi": "Pin nhiên liệu gia đình 1kW sản xuất 24kWh điện và nước nóng mỗi ngày.",
                "situation": "formal"
            },
            {
                "ko": "PEMFC 방식으로 발전효율 40%, 종합효율은 85%입니다.",
                "vi": "Sử dụng phương pháp PEMFC, hiệu suất phát điện 40%, hiệu suất tổng hợp 85%.",
                "situation": "formal"
            },
            {
                "ko": "도시가스를 개질해서 수소를 만들어 발전합니다.",
                "vi": "Cải chất khí đốt thành hydro để phát điện.",
                "situation": "onsite"
            }
        ],
        "relatedTerms": [
            "수소",
            "열병합",
            "발전효율",
            "전해질"
        ]
    },
    {
        "slug": "den-led",
        "korean": "LED조명",
        "vietnamese": "Đèn LED",
        "hanja": "LED照明",
        "hanjaReading": "照(비출 조) + 明(밝을 명)",
        "pronunciation": "엘이디조명",
        "meaningKo": "발광다이오드(Light Emitting Diode)를 이용한 조명기구로, 기존 백열등이나 형광등 대비 전력소비가 적고 수명이 깁니다. 통역 시 LED를 'đèn LED'로 표현하되, 광효율(lm/W), 색온도(K), 연색지수(CRI), 조도(lux) 등 조명 기술용어를 정확히 전달해야 합니다. 한국에서는 '에너지 효율 1등급', '고효율 인증' 제품이 의무화되지만, 베트남은 아직 기준이 느슨하여 저가 제품이 많으므로 품질 차이를 명확히 설명해야 합니다. 건물에너지 절감을 위한 '스마트 조명', '센서 연동 조명' 등도 함께 통역하는 경우가 많습니다.",
        "meaningVi": "Đèn chiếu sáng sử dụng diode phát quang (LED), tiết kiệm điện 70-80% so với đèn sợi đốt, tuổi thọ lên đến 50.000 giờ. Là giải pháp chiếu sáng tiết kiệm năng lượng chủ đạo hiện nay.",
        "context": "신재생에너지설비, 조명설비",
        "culturalNote": "한국은 정부 주도로 LED 조명 보급사업을 진행하여 공공건물, 가로등 등이 대부분 LED로 교체되었지만, 베트남은 아직 형광등이 많고 저가 LED 제품의 품질 문제가 있습니다. 한국에서는 '광효율(lm/W)'과 'KS 인증'을 중시하지만, 베트남에서는 가격이 우선이라 통역 시 '초기비용은 비싸지만 전기요금 절감으로 2~3년 안에 회수 가능'이라는 경제성을 강조해야 합니다. '색온도(nhiệt độ màu)'는 사무실 5,000~6,500K(주백색), 주거공간 3,000~4,000K(전구색)로 구분하며, '연색지수(chỉ số hoàn màu, CRI)'는 80 이상이 좋다는 것도 설명해야 합니다. 한국은 '스마트 조명(조도센서, 재실센서)'이 일반화되었지만 베트남은 아직 수동 스위치가 대부분입니다.",
        "commonMistakes": [
            {
                "mistake": "LED를 '엘이디'로만 음역",
                "correction": "LED (diode phát quang) - đèn LED",
                "explanation": "약어 의미를 한 번은 설명 필요"
            },
            {
                "mistake": "lm/W를 설명 없이 숫자만 전달",
                "correction": "120 lm/W = 1와트당 120루멘 빛 생산 (효율 지표)",
                "explanation": "기술 단위는 의미를 함께 설명"
            },
            {
                "mistake": "색온도를 '색깔 온도'로 직역",
                "correction": "nhiệt độ màu (색온도) - 빛의 색감 (K 단위)",
                "explanation": "전문용어 정확히 사용"
            }
        ],
        "examples": [
            {
                "ko": "120lm/W 고효율 LED로 교체하면 조명전력이 70% 절감됩니다.",
                "vi": "Thay bằng đèn LED hiệu suất cao 120lm/W sẽ tiết kiệm 70% điện năng chiếu sáng.",
                "situation": "formal"
            },
            {
                "ko": "색온도 5,700K 주백색으로 사무실에 적합합니다.",
                "vi": "Nhiệt độ màu 5.700K ánh sáng trắng ngày, phù hợp cho văn phòng.",
                "situation": "onsite"
            },
            {
                "ko": "재실센서 연동해서 사람 없으면 자동으로 꺼집니다.",
                "vi": "Kết nối cảm biến hiện diện, tự động tắt khi không có người.",
                "situation": "informal"
            }
        ],
        "relatedTerms": [
            "광효율",
            "색온도",
            "연색지수",
            "조도센서"
        ]
    },
    {
        "slug": "den-hieu-suat-cao",
        "korean": "고효율조명",
        "vietnamese": "Đèn hiệu suất cao",
        "hanja": "高效率照明",
        "hanjaReading": "高(높을 고) + 效(공 효) + 率(비율 률) + 照(비출 조) + 明(밝을 명)",
        "pronunciation": "고효율조명",
        "meaningKo": "에너지 효율이 높은 조명기구의 총칭으로, LED, T5 형광등, 메탈할라이드 등을 포함합니다. 통역 시 단순히 '효율 좋은 조명'이 아니라 '고효율 인증(한국에너지공단)' 또는 '에너지효율 1~5등급' 기준을 충족하는 제품임을 명확히 해야 합니다. 광효율(lm/W) 외에도 소비전력(W), 조도(lux), 연색성(CRI), 수명(시간) 등을 종합적으로 평가하며, 건축물 에너지효율등급 인증이나 녹색건축 인증 시 필수 항목입니다. 베트남어로는 'đèn hiệu suất cao' 또는 'chiếu sáng tiết kiệm năng lượng'로 표현하며, 단순 교체만으로 건물 전체 전력의 20~30%를 절감할 수 있다는 경제성을 강조해야 합니다.",
        "meaningVi": "Thiết bị chiếu sáng có hiệu suất năng lượng cao, bao gồm LED, đèn huỳnh quang T5, đèn Metal Halide. Đạt tiêu chuẩn tiết kiệm năng lượng, giảm 50-80% điện năng so với đèn thông thường.",
        "context": "신재생에너지설비, 에너지절감",
        "culturalNote": "한국은 '고효율에너지기자재 인증제도'로 조명, 냉난방, 보일러 등을 관리하며 공공기관은 의무적으로 고효율 제품을 사용해야 하지만, 베트남은 아직 인증제도가 미흡하여 자율적으로 선택합니다. 한국에서는 '에너지효율등급 라벨'로 1~5등급을 표시하지만, 베트남은 '별표(sao)' 시스템(1~5별)을 사용하므로 통역 시 혼동하지 않도록 주의해야 합니다. '고효율 조명'은 초기 비용은 비싸지만 유지비가 저렴하여 LCC(Life Cycle Cost, 생애주기비용) 관점에서 경제적이라는 점을 강조하고, 교체 시 기존 조명 폐기물 처리(형광등의 수은 문제 등)도 함께 설명해야 합니다. 한국은 '조명밀도(W/㎡)' 기준이 있지만 베트남은 아직 없으므로 한국 기준을 참고하여 제안하는 것이 좋습니다.",
        "commonMistakes": [
            {
                "mistake": "고효율을 'hiệu quả cao'로 번역",
                "correction": "hiệu suất cao (고효율) - 에너지 효율 기준",
                "explanation": "'hiệu quả'는 일반 효과, 'hiệu suất'는 에너지 효율"
            },
            {
                "mistake": "조명밀도를 설명 없이 W/㎡만 말함",
                "correction": "mật độ chiếu sáng (W/㎡) = 단위면적당 조명전력",
                "explanation": "기술 지표는 의미를 함께 설명"
            },
            {
                "mistake": "LCC를 약어만 사용",
                "correction": "LCC (chi phí vòng đời) = 초기비용 + 운영비 + 폐기비용",
                "explanation": "경제성 개념은 구체적으로 설명 필요"
            }
        ],
        "examples": [
            {
                "ko": "고효율 LED로 전체 교체하면 조명전력 70% 절감, 3년 내 투자회수 가능합니다.",
                "vi": "Thay toàn bộ bằng LED hiệu suất cao sẽ tiết kiệm 70% điện chiếu sáng, thu hồi vốn trong 3 năm.",
                "situation": "formal"
            },
            {
                "ko": "에너지효율 1등급 제품으로 조명밀도 10W/㎡ 이하를 만족합니다.",
                "vi": "Sản phẩm hạng tiết kiệm năng lượng số 1, đạt mật độ chiếu sáng dưới 10W/㎡.",
                "situation": "formal"
            },
            {
                "ko": "형광등을 T5로 바꾸는 것만으로도 30% 절감됩니다.",
                "vi": "Chỉ cần thay đèn huỳnh quang sang T5 cũng tiết kiệm được 30%.",
                "situation": "onsite"
            }
        ],
        "relatedTerms": [
            "LED조명",
            "에너지효율등급",
            "조명밀도",
            "광효율"
        ]
    },
    {
        "slug": "he-thong-quan-ly-nang-luong-toa-nha",
        "korean": "건물에너지관리시스템",
        "vietnamese": "Hệ thống quản lý năng lượng tòa nhà (BEMS)",
        "hanja": "建物energy管理system",
        "hanjaReading": "建(세울 건) + 物(만물 물) + 管(대롱 관) + 理(다스릴 리)",
        "pronunciation": "건물에너지관리시스템",
        "meaningKo": "건물의 냉난방, 조명, 환기 등 에너지 사용을 통합 모니터링하고 자동 제어하는 시스템으로, BEMS(Building Energy Management System)로 약칭합니다. 통역 시 BEMS를 반드시 'hệ thống quản lý năng lượng tòa nhà'로 풀어서 설명하고, BAS(Building Automation System, 빌딩자동화)와의 차이(BAS는 제어 중심, BEMS는 에너지 관리+최적화)를 명확히 해야 합니다. 실시간 모니터링, 데이터 분석, 예측 제어, 에너지 절감 리포트 등 기능을 구체적으로 설명하며, 센서(온도, 습도, 조도, CO2), 계측기(전력, 가스, 수도), 제어기(HVAC, 조명) 등 구성요소를 정확히 통역해야 합니다. 한국에서는 '제로에너지빌딩(ZEB)' 인증 시 필수이며, 베트남에서도 고급 건물에 도입이 증가하고 있습니다.",
        "meaningVi": "Hệ thống giám sát và điều khiển tự động năng lượng tòa nhà (làm lạnh, sưởi ấm, chiếu sáng, thông gió). Tích hợp cảm biến, đồng hồ đo và bộ điều khiển để tối ưu hóa tiêu thụ năng lượng, giảm 20-40% chi phí vận hành.",
        "context": "신재생에너지설비, 빌딩자동화",
        "culturalNote": "한국은 '녹색건축 인증', '제로에너지빌딩(ZEB)' 의무화로 BEMS 설치가 증가하고 있으며, 정부는 '에너지진단 의무대상 건물'에 BEMS 설치 시 보조금을 지원하지만, 베트남은 아직 의무 규정이 없어 주로 외국계 기업이나 고급 오피스빌딩에만 도입됩니다. 한국에서는 'EMS(에너지관리시스템)'과 'BEMS'를 혼용하지만, 엄밀히는 BEMS가 건물 특화 시스템입니다. 통역 시 'AI 기반 예측 제어', '머신러닝 최적화' 등 최신 기술도 함께 설명하며, '투자회수기간(payback period)'을 명확히 제시해야 합니다(보통 3~5년). 베트남어로 'BAS(hệ thống tự động hóa tòa nhà)'와 'BEMS(hệ thống quản lý năng lượng)'의 차이를 설명할 때는 'BAS는 편의성, BEMS는 절감'으로 구분하면 이해가 빠릅니다.",
        "commonMistakes": [
            {
                "mistake": "BEMS를 약어만 사용하고 설명 안 함",
                "correction": "BEMS (hệ thống quản lý năng lượng tòa nhà) - Building Energy Management System",
                "explanation": "약어는 반드시 풀어서 설명"
            },
            {
                "mistake": "BAS와 BEMS를 같은 것으로 통역",
                "correction": "BAS = 자동화(편의), BEMS = 에너지관리(절감)",
                "explanation": "목적과 기능이 다름"
            },
            {
                "mistake": "절감률을 %만 말하고 금액 환산 안 함",
                "correction": "30% 절감 = 월 XX백만동 절약 (구체적 금액)",
                "explanation": "경제성은 돈으로 표현해야 설득력 있음"
            }
        ],
        "examples": [
            {
                "ko": "BEMS 구축으로 에너지 사용량 30% 절감, 연간 5억원 절약됩니다.",
                "vi": "Xây dựng BEMS giảm 30% tiêu thụ năng lượng, tiết kiệm 5 tỷ won mỗi năm.",
                "situation": "formal"
            },
            {
                "ko": "실시간 모니터링으로 이상 징후를 즉시 감지하고 알림을 보냅니다.",
                "vi": "Giám sát thời gian thực phát hiện ngay bất thường và gửi cảnh báo.",
                "situation": "onsite"
            },
            {
                "ko": "AI가 날씨 예측하여 냉난방을 미리 조절해서 피크를 줄입니다.",
                "vi": "AI dự báo thời tiết để điều chỉnh trước hệ thống làm lạnh/sưởi, giảm đỉnh tải.",
                "situation": "formal"
            }
        ],
        "relatedTerms": [
            "빌딩자동화",
            "에너지절감",
            "스마트빌딩",
            "제로에너지빌딩"
        ]
    }
]

def add_terms():
    """기존 construction.json에 신규 용어 추가"""
    try:
        # 기존 파일 읽기
        with open(file_path, 'r', encoding='utf-8') as f:
            existing_data = json.load(f)

        print(f"✅ 기존 파일 로드 완료: {len(existing_data)}개 용어")

        # 중복 체크 (slug 기준)
        existing_slugs = {term['slug'] for term in existing_data}
        new_terms = [term for term in data if term['slug'] not in existing_slugs]
        duplicates = [term['slug'] for term in data if term['slug'] in existing_slugs]

        if duplicates:
            print(f"⚠️  중복 slug 발견 (추가 안 함): {', '.join(duplicates)}")

        if not new_terms:
            print("ℹ️  추가할 신규 용어 없음 (모두 중복)")
            return

        # 신규 용어 추가
        existing_data.extend(new_terms)

        # 파일 저장 (pretty-print)
        with open(file_path, 'w', encoding='utf-8') as f:
            json.dump(existing_data, f, ensure_ascii=False, indent=2)

        print(f"✅ 저장 완료: {len(new_terms)}개 용어 추가")
        print(f"📊 전체: {len(existing_data)}개 용어")
        print(f"📝 추가된 용어:")
        for term in new_terms:
            print(f"   - {term['korean']} ({term['slug']})")

    except FileNotFoundError:
        print(f"❌ 파일 없음: {file_path}")
        print("ℹ️  신규 파일로 저장합니다.")
        with open(file_path, 'w', encoding='utf-8') as f:
            json.dump(data, f, ensure_ascii=False, indent=2)
        print(f"✅ 신규 파일 생성: {len(data)}개 용어")

    except json.JSONDecodeError as e:
        print(f"❌ JSON 파싱 오류: {e}")

    except Exception as e:
        print(f"❌ 오류 발생: {e}")

if __name__ == "__main__":
    print("=" * 60)
    print("건설(Construction) 용어 추가 스크립트 v8")
    print("테마: 신재생에너지설비")
    print("=" * 60)
    add_terms()
    print("=" * 60)
