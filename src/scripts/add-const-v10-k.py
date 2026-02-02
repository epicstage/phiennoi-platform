#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
건축설비 심화 용어 추가 스크립트 (Advanced Building Services)
Tier S 품질 기준 준수 (90점 이상)
"""

import json
import os

# 파일 경로 설정
file_path = os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', 'data', 'terms', 'construction.json')

# 신규 용어 10개 (건축설비 심화)
new_terms = [
    {
        "slug": "he-thong-bms",
        "korean": "빌딩자동제어",
        "vietnamese": "Hệ thống BMS (Building Management System)",
        "hanja": "Building自動制禦",
        "hanjaReading": "Building(빌딩) + 自(스스로 자) + 動(움직일 동) + 制(제어할 제) + 禦(막을 어)",
        "pronunciation": "빌딩자동제어",
        "meaningKo": "건물의 공조, 조명, 전력, 방재, 보안 등을 통합 관리하는 자동제어시스템입니다. 통역 시 'BMS'는 베트남 현장에서도 영문 약어로 통용되므로 그대로 사용하되, 'hệ thống quản lý tòa nhà'로 풀어 설명해야 합니다. 특히 베트남에서는 스마트빌딩 개념이 확산되면서 BMS 도입이 늘고 있으나, 유지보수 체계가 한국만큼 체계적이지 않아 운영상 주의사항을 강조해야 합니다. 에너지 절감 효과를 설명할 때는 구체적인 수치(20~30% 절감)를 제시하면 이해가 빠릅니다.",
        "meaningVi": "Hệ thống quản lý và điều khiển tự động các thiết bị trong tòa nhà như điều hòa không khí, chiếu sáng, điện lực, phòng cháy chữa cháy và an ninh. BMS giúp tối ưu hóa năng lượng, giảm chi phí vận hành và nâng cao hiệu suất quản lý tòa nhà thông qua giám sát tập trung và điều khiển từ xa.",
        "context": "스마트빌딩, 시설관리",
        "culturalNote": "한국은 고층빌딩 대부분이 BMS를 표준 설치하며 원격 통합관리가 일반화되어 있으나, 베트남은 대형 빌딩에만 도입되고 유지보수 인력이 부족해 시스템 활용도가 낮은 경우가 많습니다. 통역 시 한국 측이 요구하는 BMS 수준과 베트남 현지 운영 역량의 차이를 사전에 조율해야 합니다.",
        "commonMistakes": [
            {
                "mistake": "BMS를 '빌딩관리시스템'으로만 번역",
                "correction": "Hệ thống BMS (Building Management System) - hệ thống quản lý tòa nhà",
                "explanation": "약어 BMS를 그대로 두고 풀어서 설명하는 것이 현장에서 소통하기 쉽습니다"
            },
            {
                "mistake": "'자동제어'를 'tự động hóa'로만 번역",
                "correction": "điều khiển tự động / quản lý tự động",
                "explanation": "제어(control)와 자동화(automation)는 의미가 다르므로 문맥에 맞게 구분해야 합니다"
            },
            {
                "mistake": "에너지 절감 효과를 '매우 크다'로 모호하게 표현",
                "correction": "tiết kiệm 20-30% năng lượng (에너지 20~30% 절감)",
                "explanation": "구체적인 수치를 제시해야 설득력이 높아집니다"
            }
        ],
        "examples": [
            {
                "ko": "이 건물은 BMS를 통해 전체 설비를 통합 관리합니다",
                "vi": "Tòa nhà này quản lý tổng thể các thiết bị thông qua hệ thống BMS",
                "situation": "formal"
            },
            {
                "ko": "BMS 운영 교육은 준공 전에 실시됩니다",
                "vi": "Đào tạo vận hành BMS sẽ được thực hiện trước khi hoàn công",
                "situation": "onsite"
            },
            {
                "ko": "중앙제어실에서 BMS로 전체 빌딩을 모니터링합니다",
                "vi": "Giám sát toàn bộ tòa nhà bằng BMS từ phòng điều khiển trung tâm",
                "situation": "formal"
            }
        ],
        "relatedTerms": ["스마트빌딩", "중앙감시제어", "에너지관리시스템"]
    },
    {
        "slug": "may-phat-dien",
        "korean": "발전기",
        "vietnamese": "Máy phát điện",
        "hanja": "發電機",
        "hanjaReading": "發(필 발) + 電(번개 전) + 機(틀 기)",
        "pronunciation": "발전기",
        "meaningKo": "정전 시 건물에 전력을 공급하기 위한 비상 전원 장치입니다. 통역 시 발전기 용량(kVA)과 연료 종류(경유/가스)를 명확히 구분해야 하며, 베트남에서는 정전이 잦아 발전기를 '비상용'이 아닌 '상시 보조용'으로 간주하는 경우가 많습니다. 특히 소음 기준(dB)과 배기가스 규제가 한국보다 느슨하므로, 한국 기준으로 설계된 발전기 사양을 설명할 때 현지 규정과의 차이를 짚어줘야 합니다. 유지보수 주기(500시간/1000시간)도 반드시 통역에 포함해야 합니다.",
        "meaningVi": "Thiết bị cung cấp điện dự phòng cho tòa nhà khi mất điện lưới. Máy phát điện thường dùng nhiên liệu diesel hoặc gas, công suất đo bằng kVA. Ở Việt Nam, do tình trạng cúp điện thường xuyên, máy phát điện được coi là thiết bị thiết yếu chứ không chỉ là dự phòng khẩn cấp.",
        "context": "전기설비, 비상전원",
        "culturalNote": "한국은 정전이 드물어 발전기가 주로 법적 요구사항으로 설치되지만, 베트남(특히 공단 지역)은 정전이 빈번해 발전기 가동률이 매우 높습니다. 따라서 베트남 프로젝트에서는 발전기 용량을 여유 있게 설계하고, 연료 저장 탱크 용량도 크게 잡아야 합니다.",
        "commonMistakes": [
            {
                "mistake": "'발전기'를 'máy điện'으로만 번역",
                "correction": "máy phát điện (발전기) / máy điện (전기기기 일반)",
                "explanation": "'máy điện'은 전기기기 전체를 가리키므로 발전기는 반드시 'máy phát điện'으로 표현해야 합니다"
            },
            {
                "mistake": "용량을 'kW'와 'kVA' 혼용",
                "correction": "공칭용량은 kVA, 실제출력은 kW로 구분",
                "explanation": "발전기 용량은 kVA로 표시하고, 실제 사용 가능한 전력은 역률을 고려한 kW로 설명해야 합니다"
            },
            {
                "mistake": "'비상발전기'를 'máy phát điện khẩn cấp'으로 번역",
                "correction": "máy phát điện dự phòng (예비발전기)",
                "explanation": "베트남에서는 'dự phòng'(예비)이 일반적이며, 'khẩn cấp'(긴급)은 과도하게 들립니다"
            }
        ],
        "examples": [
            {
                "ko": "500kVA 발전기를 지하 1층에 설치합니다",
                "vi": "Lắp đặt máy phát điện 500kVA tại tầng hầm 1",
                "situation": "onsite"
            },
            {
                "ko": "발전기는 정전 시 10초 내에 자동 기동됩니다",
                "vi": "Máy phát điện tự động khởi động trong vòng 10 giây khi mất điện",
                "situation": "formal"
            },
            {
                "ko": "발전기 연료 탱크 용량은 8시간 연속 가동 기준입니다",
                "vi": "Dung tích bình nhiên liệu đủ cho máy phát điện hoạt động liên tục 8 giờ",
                "situation": "onsite"
            }
        ],
        "relatedTerms": ["비상전원", "무정전전원장치", "연료탱크"]
    },
    {
        "slug": "tram-bien-ap",
        "korean": "변전소",
        "vietnamese": "Trạm biến áp",
        "hanja": "變電所",
        "hanjaReading": "變(변할 변) + 電(번개 전) + 所(바 소)",
        "pronunciation": "변전소",
        "meaningKo": "고압 전력을 건물에서 사용 가능한 전압으로 변환하는 시설입니다. 통역 시 한국의 '수전 전압'(22.9kV)과 베트남(22kV 또는 35kV)의 차이를 명확히 해야 하며, 변전소 설치 위치(옥내형/옥외형)와 안전거리 규정도 양국이 다릅니다. 특히 베트남에서는 변전소 인근 주민들이 전자파 우려로 반대하는 경우가 많아, 공사 전 주민 설명회가 필수입니다. 한국처럼 지중 배전이 일반화되지 않아 가공선로 연결이 많으므로 이 점도 통역 시 짚어줘야 합니다.",
        "meaningVi": "Công trình điện chuyển đổi điện áp cao từ lưới điện quốc gia xuống điện áp sử dụng trong tòa nhà hoặc khu công nghiệp. Ở Việt Nam, điện áp đầu vào thường là 22kV hoặc 35kV, sau đó hạ xuống 380V/220V để sử dụng. Trạm biến áp có thể lắp đặt trong nhà hoặc ngoài trời, tùy quy mô công trình.",
        "context": "전기설비, 수전설비",
        "culturalNote": "한국은 변전소가 대부분 건물 내부 지하에 설치되고 지중선로로 연결되지만, 베트남은 부지 내 독립 건물로 설치하고 가공선로로 연결하는 경우가 많습니다. 또한 베트남은 전력공사(EVN)의 승인 절차가 까다롭고 시간이 오래 걸리므로, 변전소 설계 단계부터 EVN과 긴밀히 협의해야 합니다.",
        "commonMistakes": [
            {
                "mistake": "'변전소'와 '배전반'을 혼동",
                "correction": "변전소(trạm biến áp)는 고압→저압 변환 시설, 배전반(tủ điện)은 저압 분배 설비",
                "explanation": "변전소는 전압 변환 기능이 있고, 배전반은 단순히 전력을 분배하는 패널입니다"
            },
            {
                "mistake": "'22.9kV'를 '23kV'로 반올림",
                "correction": "22,9kV (한국) / 22kV (베트남)",
                "explanation": "수전 전압은 국가 표준이 다르므로 정확한 값을 사용해야 합니다"
            },
            {
                "mistake": "'옥내 변전소'를 'trạm biến áp trong nhà'로만 번역",
                "correction": "trạm biến áp kiểu đóng (옥내형) / trạm biến áp kiểu mở (옥외형)",
                "explanation": "베트남에서는 'kiểu đóng/mở'로 구분하는 것이 기술적으로 정확합니다"
            }
        ],
        "examples": [
            {
                "ko": "22.9kV 수전용 변전소를 건물 지하에 설치합니다",
                "vi": "Lắp đặt trạm biến áp nhận điện 22,9kV tại tầng hầm tòa nhà",
                "situation": "formal"
            },
            {
                "ko": "변전소에서 380V로 강압하여 각 층에 공급합니다",
                "vi": "Hạ áp xuống 380V từ trạm biến áp và cấp điện cho các tầng",
                "situation": "onsite"
            },
            {
                "ko": "변전소 설치 승인은 전력공사와 협의가 필요합니다",
                "vi": "Cần thỏa thuận với Tổng công ty Điện lực (EVN) để phê duyệt lắp đặt trạm biến áp",
                "situation": "formal"
            }
        ],
        "relatedTerms": ["수전설비", "고압차단기", "변압기"]
    },
    {
        "slug": "tu-dien-chinh",
        "korean": "주배전반",
        "vietnamese": "Tủ điện chính",
        "hanja": "主配電盤",
        "hanjaReading": "主(주인 주) + 配(나눌 배) + 電(번개 전) + 盤(소반 반)",
        "pronunciation": "주배전반",
        "meaningKo": "변전소에서 받은 전력을 건물 각 부분으로 분배하는 주 전기 패널입니다. 통역 시 '주배전반(MCCB)', '동력반(동력용)', '전등반(조명용)'을 명확히 구분해야 하며, 베트남에서는 분전반 용어가 혼용되므로 도면 기준으로 정확히 소통해야 합니다. 특히 차단기 용량(A)과 극수(2P/3P/4P)를 반드시 통역에 포함하고, 베트남은 접지 방식이 한국(TN-C-S)과 다를 수 있어(TN-S, TT 등) 이를 사전 확인해야 합니다. 결선도(single line diagram)를 함께 보면서 설명하는 것이 가장 효과적입니다.",
        "meaningVi": "Tủ điện tổng phân phối điện năng từ trạm biến áp đến các khu vực trong tòa nhà. Tủ điện chính chứa các thiết bị bảo vệ như cầu dao, aptomat và thiết bị đo lường. Đây là trung tâm phân phối điện cho toàn bộ hệ thống điện của công trình, đảm bảo cung cấp điện an toàn và ổn định.",
        "context": "전기설비, 배전설비",
        "culturalNote": "한국은 주배전반이 체계적으로 구획되고 표준화되어 있으나, 베트남은 현장마다 구성이 제각각이고 명칭도 통일되지 않아 혼선이 잦습니다. 통역 시 도면의 'MDB(Main Distribution Board)' 기호를 같이 보여주며 설명하는 것이 오해를 줄이는 방법입니다.",
        "commonMistakes": [
            {
                "mistake": "'주배전반'을 'tủ điện'으로만 번역",
                "correction": "tủ điện chính (주배전반) / tủ điện phân phối chính (주배전반) / tủ điện phụ (분전반)",
                "explanation": "'tủ điện'은 전기패널 전체를 지칭하므로, 주배전반은 'chính'(메인)을 붙여 구분해야 합니다"
            },
            {
                "mistake": "'차단기'를 'cầu dao'로만 번역",
                "correction": "aptomat (자동차단기) / cầu dao (수동 나이프 스위치)",
                "explanation": "현대 건축에서는 대부분 자동차단기(aptomat/MCCB)를 사용하므로 정확히 구분해야 합니다"
            },
            {
                "mistake": "전압 표기를 '380V'로만 하고 단상/삼상 구분 없이 통역",
                "correction": "380V 3 pha (삼상) / 220V 1 pha (단상)",
                "explanation": "베트남에서는 상수(pha)를 명시하지 않으면 오해가 생깁니다"
            }
        ],
        "examples": [
            {
                "ko": "주배전반은 전기실에 설치하고, 각 층 분전반으로 배선합니다",
                "vi": "Lắp đặt tủ điện chính tại phòng điện, sau đó đi dây đến các tủ điện tầng",
                "situation": "onsite"
            },
            {
                "ko": "주배전반의 주차단기는 1600A 4극입니다",
                "vi": "Aptomat tổng của tủ điện chính là 1600A 4 cực",
                "situation": "formal"
            },
            {
                "ko": "주배전반에서 각 층까지 간선은 케이블 트레이로 시공합니다",
                "vi": "Thi công đường dây chính từ tủ điện chính đến các tầng bằng thang cáp",
                "situation": "onsite"
            }
        ],
        "relatedTerms": ["분전반", "차단기", "간선"]
    },
    {
        "slug": "he-thong-ups",
        "korean": "무정전전원장치",
        "vietnamese": "Hệ thống UPS (Uninterruptible Power Supply)",
        "hanja": "無停電電源裝置",
        "hanjaReading": "無(없을 무) + 停(멈출 정) + 電(번개 전) + 電(번개 전) + 源(근원 원) + 裝(꾸밀 장) + 置(놓을 치)",
        "pronunciation": "무정전전원장치",
        "meaningKo": "정전이나 전압 변동 시에도 중단 없이 전원을 공급하는 장치로, 주로 서버실, 통신실, 의료기기 등 전원 중단이 치명적인 설비에 사용됩니다. 통역 시 UPS 타입(On-line/Off-line/Line-interactive)과 용량(kVA), 백업 시간(분)을 반드시 명시해야 하며, 베트남은 전력 품질이 불안정해 UPS 용량을 한국보다 20~30% 여유 있게 설계해야 합니다. 특히 배터리 교체 주기(3~5년)와 유지보수 비용을 사전에 설명하지 않으면 나중에 클레임이 발생할 수 있습니다. 'UPS'는 베트남에서도 영문 약어로 통용됩니다.",
        "meaningVi": "Thiết bị cung cấp điện liên tục không gián đoạn khi mất điện hoặc điện áp không ổn định, bảo vệ các thiết bị quan trọng như máy chủ, thiết bị y tế, hệ thống thông tin. UPS có ba loại chính: On-line (luôn hoạt động qua biến tần), Off-line (chỉ kích hoạt khi mất điện), Line-interactive (điều chỉnh điện áp đầu vào). Thời gian dự phòng phụ thuộc vào dung lượng ắc quy, thường từ 10 phút đến 2 giờ.",
        "context": "전기설비, 비상전원",
        "culturalNote": "한국은 전력 품질이 안정적이어서 UPS를 주로 순간 정전 대비용으로 쓰지만, 베트남은 전압 변동과 정전이 잦아 UPS가 훨씬 자주 작동합니다. 따라서 베트남 프로젝트에서는 UPS 용량과 배터리 수명을 여유 있게 설계해야 하며, 정기 점검 계획도 철저히 세워야 합니다.",
        "commonMistakes": [
            {
                "mistake": "'무정전전원장치'를 'nguồn điện không ngừng'으로 직역",
                "correction": "hệ thống UPS / thiết bị lưu điện UPS",
                "explanation": "UPS는 베트남에서도 보편적인 약어이므로 그대로 사용하는 것이 자연스럽습니다"
            },
            {
                "mistake": "UPS 백업 시간을 '충분히 길다'로 모호하게 표현",
                "correction": "thời gian dự phòng 30 phút / 1 giờ / 2 giờ",
                "explanation": "백업 시간은 설계의 핵심 요소이므로 구체적인 시간(분/시간)을 명시해야 합니다"
            },
            {
                "mistake": "'배터리'를 'pin'으로 번역",
                "correction": "ắc quy (축전지) / pin (건전지)",
                "explanation": "UPS는 대용량 축전지(ắc quy)를 쓰므로, 소형 건전지(pin)와 구분해야 합니다"
            }
        ],
        "examples": [
            {
                "ko": "서버실에는 30분 백업용 50kVA UPS를 설치합니다",
                "vi": "Lắp đặt UPS 50kVA với thời gian dự phòng 30 phút cho phòng server",
                "situation": "formal"
            },
            {
                "ko": "UPS는 On-line 방식으로 상시 전력을 공급합니다",
                "vi": "UPS hoạt động theo kiểu On-line, cung cấp điện liên tục",
                "situation": "onsite"
            },
            {
                "ko": "UPS 배터리는 3년마다 교체가 필요합니다",
                "vi": "Ắc quy UPS cần thay thế mỗi 3 năm",
                "situation": "formal"
            }
        ],
        "relatedTerms": ["비상전원", "발전기", "축전지"]
    },
    {
        "slug": "cap-ngam",
        "korean": "지중케이블",
        "vietnamese": "Cáp ngầm",
        "hanja": "地中cable",
        "hanjaReading": "地(땅 지) + 中(가운데 중) + cable(케이블)",
        "pronunciation": "지중케이블",
        "meaningKo": "땅속에 매설하여 전력이나 통신 신호를 전송하는 케이블입니다. 통역 시 케이블 종류(CV, CNCV 등), 굵기(mm²), 코어 수(3C, 4C 등)를 명확히 구분해야 하며, 베트남은 지중 배선이 한국만큼 보편화되지 않아 시공 방법과 매설 깊이 기준을 상세히 설명해야 합니다. 특히 베트남은 우기에 침수 위험이 크므로 방수 처리와 배수로 설치를 강조해야 하며, 케이블 접속부(joint)의 방수 시공이 매우 중요합니다. 지중 배선 경로는 준공도면에 정확히 표기해야 나중에 보수 시 케이블 손상을 방지할 수 있습니다.",
        "meaningVi": "Cáp điện hoặc cáp thông tin được chôn ngầm dưới mặt đất để truyền tải điện năng hoặc tín hiệu. Cáp ngầm giúp cảnh quan đô thị gọn gàng, giảm rủi ro do thời tiết và tai nạn so với đường dây trên không. Tuy nhiên, chi phí lắp đặt và bảo trì cáp ngầm cao hơn, đặc biệt ở Việt Nam do nguy cơ ngập úng và chất lượng thi công chưa đồng đều.",
        "context": "전기설비, 통신설비",
        "culturalNote": "한국은 도심 지역 대부분이 지중 배선이지만, 베트남은 여전히 가공선로(đường dây trên không)가 많고 지중 배선은 대형 프로젝트에만 적용됩니다. 지중 배선 시공 경험이 부족한 현지 업체가 많아, 한국 측이 시공 기준과 품질 관리를 철저히 감독해야 합니다.",
        "commonMistakes": [
            {
                "mistake": "'지중케이블'을 'cáp điện dưới đất'로 직역",
                "correction": "cáp ngầm (지중케이블)",
                "explanation": "'cáp ngầm'이 베트남에서 통용되는 표준 용어입니다"
            },
            {
                "mistake": "케이블 굵기를 '두껍다/얇다'로만 표현",
                "correction": "cáp 3x95mm² (3심 95제곱밀리) / cáp 4x150mm²",
                "explanation": "케이블 규격은 심수(C)와 단면적(mm²)을 정확히 표기해야 합니다"
            },
            {
                "mistake": "'매설 깊이'를 구체적인 수치 없이 통역",
                "correction": "chôn sâu 80cm (매설 깊이 80cm) / chôn sâu tối thiểu 1m (최소 1m)",
                "explanation": "매설 깊이는 안전 기준이므로 반드시 수치로 명시해야 합니다"
            }
        ],
        "examples": [
            {
                "ko": "변전소에서 건물까지 지중케이블로 연결합니다",
                "vi": "Nối từ trạm biến áp đến tòa nhà bằng cáp ngầm",
                "situation": "onsite"
            },
            {
                "ko": "지중케이블은 80cm 깊이에 매설하고 보호관을 씌웁니다",
                "vi": "Chôn cáp ngầm ở độ sâu 80cm và bọc ống bảo vệ",
                "situation": "onsite"
            },
            {
                "ko": "지중케이블 경로는 준공도면에 정확히 표기해야 합니다",
                "vi": "Phải ghi chính xác tuyến đường cáp ngầm trên bản vẽ hoàn công",
                "situation": "formal"
            }
        ],
        "relatedTerms": ["가공선로", "전선관", "접속함"]
    },
    {
        "slug": "ong-gio",
        "korean": "덕트",
        "vietnamese": "Ống gió",
        "hanja": "duct",
        "hanjaReading": "duct(덕트)",
        "pronunciation": "덕트",
        "meaningKo": "공조 시스템에서 냉난방 공기를 각 공간으로 보내는 배관을 말합니다. 통역 시 덕트 재질(아연도금강판/GI, 스테인리스/STS, 알루미늄 등)과 형태(원형/사각), 단열 여부를 반드시 구분해야 하며, 베트남에서는 '덕트'를 'ống gió'(공기관)로 부르므로 혼동하지 않도록 주의해야 합니다. 특히 덕트 크기는 폭×높이(mm)로 표기하고, 풍량(CMH)과 풍속(m/s)도 함께 통역해야 합니다. 베트남은 습도가 높아 단열재 시공이 필수이며, 단열재 두께(25mm/50mm)도 명시해야 합니다. 덕트 청소 주기(6개월~1년)도 통역에 포함해야 나중에 유지보수 분쟁을 막을 수 있습니다.",
        "meaningVi": "Đường ống dẫn khí lạnh hoặc khí nóng từ máy điều hòa trung tâm đến các phòng trong hệ thống HVAC. Ống gió thường làm từ tôn mạ kẽm, inox hoặc nhôm, có dạng tròn hoặc chữ nhật. Ở Việt Nam, do độ ẩm cao, ống gió phải bọc cách nhiệt để tránh ngưng tụ hơi nước và tăng hiệu suất làm lạnh.",
        "context": "공조설비, HVAC",
        "culturalNote": "한국은 덕트 설계와 시공이 매우 정밀하고 표준화되어 있으나, 베트남은 덕트 크기 산정이 부정확하고 시공 품질이 들쭉날쭉한 경우가 많습니다. 특히 덕트 누기(air leakage) 검사를 생략하는 경우가 많아, 한국 감리는 반드시 누기 시험을 요구해야 합니다.",
        "commonMistakes": [
            {
                "mistake": "'덕트'를 'ống dẫn'으로만 번역",
                "correction": "ống gió (공조 덕트) / ống dẫn (일반 배관)",
                "explanation": "'ống gió'는 공조 전용 용어이고, 'ống dẫn'은 모든 배관을 포괄하므로 구분해야 합니다"
            },
            {
                "mistake": "덕트 크기를 '크다/작다'로만 표현",
                "correction": "ống gió 600x400mm (폭 600mm, 높이 400mm)",
                "explanation": "덕트 크기는 설계의 핵심이므로 정확한 치수(mm)로 통역해야 합니다"
            },
            {
                "mistake": "'단열재'를 'chất cách nhiệt'로만 번역하고 두께 생략",
                "correction": "bọc cách nhiệt dày 25mm (두께 25mm 단열재) / bọc cách nhiệt dày 50mm",
                "explanation": "단열재 두께는 냉방 효율과 결로 방지에 직결되므로 반드시 명시해야 합니다"
            }
        ],
        "examples": [
            {
                "ko": "주 덕트는 800×600mm 아연도금강판으로 제작합니다",
                "vi": "Ống gió chính kích thước 800x600mm làm bằng tôn mạ kẽm",
                "situation": "onsite"
            },
            {
                "ko": "모든 덕트에 50mm 단열재를 시공해야 합니다",
                "vi": "Tất cả ống gió phải bọc cách nhiệt dày 50mm",
                "situation": "formal"
            },
            {
                "ko": "덕트 내부는 6개월마다 청소가 필요합니다",
                "vi": "Cần vệ sinh bên trong ống gió mỗi 6 tháng",
                "situation": "formal"
            }
        ],
        "relatedTerms": ["공조설비", "디퓨저", "댐퍼"]
    },
    {
        "slug": "may-bom-nuoc",
        "korean": "급수펌프",
        "vietnamese": "Máy bơm nước",
        "hanja": "給水pump",
        "hanjaReading": "給(줄 급) + 水(물 수) + pump(펌프)",
        "pronunciation": "급수펌프",
        "meaningKo": "건물에 물을 공급하기 위한 펌프 장치로, 수도 본관에서 각 층 위생기구까지 물을 올려주는 역할을 합니다. 통역 시 펌프 타입(원심펌프/터빈펌프), 양정(m), 토출량(㎥/h)을 명확히 해야 하며, 베트남은 수압이 낮고 불안정해 한국보다 큰 용량의 펌프와 고가수조를 설치해야 합니다. 특히 '부스터 펌프'(증압펌프)와 '양수 펌프'(양수용)를 구분하고, 배관 재질(STS, 동관, PVC 등)도 함께 통역해야 합니다. 베트남은 정전이 잦아 급수펌프에 비상전원(발전기 또는 UPS) 연결이 필수이며, 이를 빠뜨리면 정전 시 급수가 중단되는 큰 문제가 생깁니다.",
        "meaningVi": "Máy bơm cấp nước cho tòa nhà, đưa nước từ đường ống cấp chính hoặc bể chứa lên các tầng và thiết bị vệ sinh. Máy bơm có các loại: ly tâm (phổ biến nhất), turbin, hoặc bơm tăng áp. Công suất máy bơm được tính theo lưu lượng (m³/h) và cột áp (m). Ở Việt Nam, do áp lực nước yếu và không đều, cần thiết kế máy bơm với công suất lớn hơn và có bể chứa nước cao.",
        "context": "급배수설비, 위생설비",
        "culturalNote": "한국은 수도 본관 수압이 안정적이어서 부스터 펌프만으로 충분한 경우가 많으나, 베트남은 수압이 약하고 단수가 잦아 고가수조(bể nước trên cao)를 반드시 설치해야 합니다. 또한 베트남은 물탱크 청소를 소홀히 하는 경우가 많아, 정기 청소 주기(3개월~6개월)를 계약서에 명시해야 합니다.",
        "commonMistakes": [
            {
                "mistake": "'급수펌프'를 'bơm nước'로만 번역",
                "correction": "máy bơm cấp nước (급수펌프) / máy bơm tăng áp (부스터펌프) / máy bơm chìm (수중펌프)",
                "explanation": "펌프 용도에 따라 명칭을 구분해야 오해가 없습니다"
            },
            {
                "mistake": "펌프 용량을 '충분하다'로 모호하게 표현",
                "correction": "máy bơm 20m³/h, cột áp 50m (토출량 20㎥/h, 양정 50m)",
                "explanation": "펌프 성능은 구체적인 수치(토출량, 양정)로 표기해야 합니다"
            },
            {
                "mistake": "'고가수조'를 'bể nước cao'로만 번역",
                "correction": "bể nước trên cao (옥상 고가수조) / bể nước ngầm (지하 물탱크)",
                "explanation": "물탱크 위치를 명확히 해야 펌프 시스템 설계가 정확해집니다"
            }
        ],
        "examples": [
            {
                "ko": "지하 물탱크에서 옥상 고가수조로 물을 올리는 급수펌프를 설치합니다",
                "vi": "Lắp đặt máy bơm cấp nước từ bể ngầm tầng hầm lên bể trên cao sân thượng",
                "situation": "onsite"
            },
            {
                "ko": "급수펌프는 20㎥/h 용량, 양정 50m로 2대를 병렬 운전합니다",
                "vi": "Máy bơm cấp nước công suất 20m³/h, cột áp 50m, vận hành song song 2 máy",
                "situation": "formal"
            },
            {
                "ko": "급수펌프에는 발전기 비상전원을 연결해야 합니다",
                "vi": "Máy bơm cấp nước phải kết nối nguồn điện dự phòng từ máy phát điện",
                "situation": "formal"
            }
        ],
        "relatedTerms": ["고가수조", "부스터펌프", "급수배관"]
    },
    {
        "slug": "binh-gian-no",
        "korean": "팽창탱크",
        "vietnamese": "Bình giãn nở",
        "hanja": "膨脹tank",
        "hanjaReading": "膨(부풀 팽) + 脹(부풀 창) + tank(탱크)",
        "pronunciation": "팽창탱크",
        "meaningKo": "냉난방 배관 내 물이 온도 변화로 팽창하거나 수축할 때 압력 변화를 흡수하는 장치입니다. 통역 시 팽창탱크 타입(밀폐형/개방형), 용량(L), 설정 압력(kPa)을 명확히 해야 하며, 베트님에서는 '팽창탱크'를 'bình giãn nở'(팽창 용기)로 부르므로 혼동하지 않도록 주의해야 합니다. 특히 냉온수 배관 시스템에서는 팽창탱크가 필수이며, 크기가 부족하면 배관이 파손되거나 안전밸브가 자주 작동하는 문제가 생깁니다. 베트남은 고온다습하여 배관 온도 변화가 크므로, 팽창탱크 용량을 한국보다 10~20% 크게 설계하는 것이 안전합니다.",
        "meaningVi": "Bình chứa hấp thụ sự thay đổi áp suất do nước trong hệ thống đường ống giãn nở hoặc co lại khi nhiệt độ thay đổi. Bình giãn nở có hai loại: kín (có màng ngăn khí và nước) và hở (tiếp xúc với không khí). Bình giãn nở kín phổ biến hơn trong các công trình hiện đại vì an toàn và ít bảo trì. Dung tích bình phải tính toán theo thể tích nước trong hệ thống và chênh lệch nhiệt độ vận hành.",
        "context": "냉난방설비, 배관설비",
        "culturalNote": "한국은 팽창탱크 설계 기준이 명확하고 시공이 철저하나, 베트남은 팽창탱크를 생략하거나 용량을 과소 설계하는 경우가 많아 냉난방 시스템 고장의 주요 원인이 됩니다. 한국 엔지니어는 반드시 팽창탱크 용량 계산서를 요구하고 검증해야 합니다.",
        "commonMistakes": [
            {
                "mistake": "'팽창탱크'를 'bình nở'로 축약",
                "correction": "bình giãn nở (팽창탱크)",
                "explanation": "'bình giãn nở'가 정확한 기술 용어이므로 축약하지 말아야 합니다"
            },
            {
                "mistake": "'밀폐형'과 '개방형'을 구분 없이 통역",
                "correction": "bình giãn nở kín (밀폐형) / bình giãn nở hở (개방형)",
                "explanation": "두 타입은 구조와 유지보수 방법이 완전히 다르므로 반드시 구분해야 합니다"
            },
            {
                "mistake": "팽창탱크 용량을 '적절하다'로만 표현",
                "correction": "bình giãn nở 100 lít (용량 100리터) / dung tích 200 lít",
                "explanation": "용량(리터)은 설계의 핵심 수치이므로 정확히 통역해야 합니다"
            }
        ],
        "examples": [
            {
                "ko": "냉온수 배관에는 200L 밀폐형 팽창탱크를 설치합니다",
                "vi": "Lắp đặt bình giãn nở kín dung tích 200 lít cho đường ống nước nóng lạnh",
                "situation": "onsite"
            },
            {
                "ko": "팽창탱크 압력은 2.5bar로 설정합니다",
                "vi": "Cài đặt áp suất bình giãn nở ở mức 2,5bar",
                "situation": "formal"
            },
            {
                "ko": "팽창탱크가 없으면 배관 파손 위험이 있습니다",
                "vi": "Nếu không có bình giãn nở, đường ống có nguy cơ bị vỡ",
                "situation": "formal"
            }
        ],
        "relatedTerms": ["냉온수배관", "압력계", "안전밸브"]
    },
    {
        "slug": "he-thong-pccc",
        "korean": "소방설비",
        "vietnamese": "Hệ thống PCCC (Phòng Cháy Chữa Cháy)",
        "hanja": "消防設備",
        "hanjaReading": "消(끌 소) + 防(막을 방) + 設(베풀 설) + 備(갖출 비)",
        "pronunciation": "소방설비",
        "meaningKo": "화재를 예방하고 진압하기 위한 모든 설비를 통칭하며, 소화기, 스프링클러, 소화전, 자동화재탐지설비, 제연설비 등을 포함합니다. 통역 시 베트남에서는 'PCCC'(Phòng Cháy Chữa Cháy)라는 약어를 공식적으로 사용하므로 이를 알아두어야 하며, 소방법 기준이 한국(소방법)과 베트남(QCVN 06)이 달라 설계 기준을 사전에 확인해야 합니다. 특히 스프링클러 헤드 간격, 소화전 방수량, 제연팬 풍량 등이 양국이 다르므로, 한국 설계를 베트남에 그대로 적용하면 현지 소방 인증을 받지 못할 수 있습니다. 통역 시 반드시 '한국 기준' 또는 '베트남 기준'을 명시해야 합니다.",
        "meaningVi": "Toàn bộ hệ thống thiết bị phòng chống và chữa cháy trong công trình, bao gồm: bình chữa cháy, hệ thống sprinkler (phun nước tự động), vòi chữa cháy, hệ thống báo cháy tự động, hệ thống thoát khói. Ở Việt Nam, các công trình phải tuân thủ tiêu chuẩn QCVN 06 của Bộ Công an về phòng cháy chữa cháy. Việc nghiệm thu PCCC do Cảnh sát Phòng cháy chữa cháy (PC07) thực hiện.",
        "context": "소방설비, 안전설비",
        "culturalNote": "한국은 소방 설계와 시공, 감리가 매우 엄격하고 체계적이나, 베트남은 법규는 있으나 현장 적용이 느슨한 경우가 많습니다. 특히 베트남은 소방 인증(PC07 승인)이 준공의 필수 조건이므로, 설계 단계부터 베트남 소방 기준을 철저히 반영하지 않으면 준공이 지연됩니다. 한국 업체가 흔히 간과하는 부분이므로 통역사가 적극적으로 주의를 환기해야 합니다.",
        "commonMistakes": [
            {
                "mistake": "'소방설비'를 'thiết bị chữa cháy'로만 번역",
                "correction": "hệ thống PCCC (소방설비 시스템 전체) / thiết bị chữa cháy (개별 소방기구)",
                "explanation": "PCCC는 베트남 공식 용어이자 약어이므로 반드시 사용해야 합니다"
            },
            {
                "mistake": "'스프링클러'를  'vòi phun nước'로 번역",
                "correction": "hệ thống sprinkler / đầu phun sprinkler",
                "explanation": "'sprinkler'는 베트남에서도 영어 그대로 쓰이는 전문 용어입니다"
            },
            {
                "mistake": "한국 소방법 기준으로만 설명하고 베트남 기준(QCVN 06) 언급 없이 통역",
                "correction": "theo tiêu chuẩn Hàn Quốc (한국 기준) / theo QCVN 06 của Việt Nam (베트남 기준)",
                "explanation": "양국 소방 기준이 다르므로 어느 기준인지 명시하지 않으면 큰 혼란이 생깁니다"
            }
        ],
        "examples": [
            {
                "ko": "전 층에 스프링클러와 자동화재탐지설비를 설치합니다",
                "vi": "Lắp đặt hệ thống sprinkler và hệ thống báo cháy tự động ở tất cả các tầng",
                "situation": "formal"
            },
            {
                "ko": "소방설비는 베트남 QCVN 06 기준에 맞춰 설계합니다",
                "vi": "Hệ thống PCCC được thiết kế theo tiêu chuẩn QCVN 06 của Việt Nam",
                "situation": "formal"
            },
            {
                "ko": "소방 준공 검사는 현지 소방서(PC07)가 담당합니다",
                "vi": "Nghiệm thu hoàn công PCCC do Cảnh sát PCCC (PC07) địa phương thực hiện",
                "situation": "onsite"
            }
        ],
        "relatedTerms": ["스프링클러", "소화전", "제연설비"]
    }
]

def main():
    # 파일 읽기
    with open(file_path, 'r', encoding='utf-8') as f:
        data = json.load(f)

    # 기존 slug 목록 생성
    existing_slugs = {term['slug'] for term in data}

    # 중복 제거 후 추가
    unique_new_terms = [term for term in new_terms if term['slug'] not in existing_slugs]

    if not unique_new_terms:
        print("⚠️  모든 용어가 이미 존재합니다. 추가할 항목이 없습니다.")
        return

    # 데이터 확장
    data.extend(unique_new_terms)

    # 파일 저장
    with open(file_path, 'w', encoding='utf-8') as f:
        json.dump(data, f, ensure_ascii=False, indent=2)

    print(f"✅ {len(unique_new_terms)}개의 건축설비 심화 용어를 추가했습니다.")
    print(f"📂 파일 위치: {file_path}")
    print(f"📊 총 용어 수: {len(data)}개")

    # 추가된 용어 목록 출력
    print("\n📋 추가된 용어:")
    for i, term in enumerate(unique_new_terms, 1):
        print(f"{i}. {term['slug']} - {term['korean']} ({term['vietnamese']})")

if __name__ == "__main__":
    main()
