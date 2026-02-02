import os
import sys
import json

# 현장전기/수변전 테마 용어 10개 (Tier S 기준)
data = [
    {
        "slug": "thiet-bi-thu-dien",
        "korean": "수전설비",
        "vietnamese": "Thiết bị thu điện",
        "hanja": "受電設備",
        "hanjaReading": "受(받을 수) + 電(전기 전) + 設(베풀 설) + 備(갖출 비)",
        "pronunciation": "수전설비",
        "meaningKo": "한국전력 등 전력회사로부터 전기를 인수받는 설비 일체를 의미합니다. 통역 시 주의할 점은 베트남에서는 'Thiết bị thu điện' 또는 'Hệ thống tiếp nhận điện'으로 표현하며, 한국의 한전과 베트남의 EVN(Tập đoàn Điện lực Việt Nam) 간 수전 방식과 전압 레벨이 다를 수 있어 구체적인 전압(22.9kV, 154kV 등)을 함께 언급해야 합니다. 수전점(điểm thu điện), 인입구(điểm đấu nối) 등의 세부 용어도 정확히 구분해야 합니다.",
        "meaningVi": "Tập hợp thiết bị dùng để tiếp nhận điện năng từ công ty cung cấp điện (như EVN ở Việt Nam hoặc KEPCO ở Hàn Quốc). Bao gồm các thiết bị như máy cắt đầu nguồn, tủ đấu nối, thiết bị đo đếm và bảo vệ. Cần lưu ý sự khác biệt về cấp điện áp và phương thức tiếp nhận giữa hai quốc gia.",
        "context": "현장 전기공사 계약 협의, 수변전실 설계, 전력 용량 검토",
        "culturalNote": "한국은 한전이 독점적으로 전력을 공급하며 수전설비 기준이 엄격하게 표준화되어 있습니다. 베트남은 EVN이 주요 공급자이나 지역별로 전력 안정성 차이가 크며, 정전 대비 비상발전기 설치가 더 보편적입니다. 통역 시 양국의 전력 인프라 수준 차이를 고려하여 설명해야 합니다.",
        "commonMistakes": [
            {
                "mistake": "'전기 받는 곳'으로 직역",
                "correction": "Thiết bị thu điện (수전설비)",
                "explanation": "수전설비는 단순히 장소가 아닌 설비 시스템 전체를 의미하므로 'thiết bị' 또는 'hệ thống'으로 표현해야 합니다."
            },
            {
                "mistake": "'변전소'와 혼동",
                "correction": "수전설비는 건물 내 설비, 변전소는 전력망의 독립 시설",
                "explanation": "변전소(trạm biến áp)는 전력회사의 송배전 시설이고, 수전설비는 수용가 측 설비입니다."
            },
            {
                "mistake": "전압 레벨 생략",
                "correction": "22.9kV 수전설비 (Thiết bị thu điện 22.9kV)",
                "explanation": "수전 전압에 따라 설비 규격과 안전 기준이 크게 달라지므로 반드시 전압을 명시해야 합니다."
            }
        ],
        "examples": [
            {
                "ko": "이 현장은 22.9kV 수전설비를 통해 전력을 공급받습니다.",
                "vi": "Công trường này được cung cấp điện thông qua thiết bị thu điện 22.9kV.",
                "situation": "formal"
            },
            {
                "ko": "수전설비 설치 위치를 1층 전기실로 확정했습니다.",
                "vi": "Đã xác định vị trí lắp đặt thiết bị thu điện tại phòng điện tầng 1.",
                "situation": "onsite"
            },
            {
                "ko": "한전 측과 수전점 협의가 완료되었습니다.",
                "vi": "Đã hoàn tất thỏa thuận về điểm thu điện với phía KEPCO.",
                "situation": "formal"
            }
        ],
        "relatedTerms": ["변압기", "배전반", "전력케이블", "비상발전기"]
    },
    {
        "slug": "may-bien-ap",
        "korean": "변압기",
        "vietnamese": "Máy biến áp",
        "hanja": "變壓器",
        "hanjaReading": "變(변할 변) + 壓(누를 압) + 器(그릇 기)",
        "pronunciation": "변압기",
        "meaningKo": "전압의 크기를 변환하는 전기 기기로, 건설 현장에서는 수전 전압(22.9kV 등)을 사용 전압(380V, 220V)으로 낮추는 강압 변압기가 주로 사용됩니다. 통역 시 주의할 점은 용량 표기 단위(kVA)와 권선 방식(유입식/몰드식), 냉각 방식 등을 정확히 전달해야 하며, 베트남에서는 'máy biến áp' 또는 줄여서 'biến áp'로 표현합니다. 변압기실(phòng biến áp) 설치 기준이 양국 간 차이가 있으므로 주의가 필요합니다.",
        "meaningVi": "Thiết bị điện dùng để biến đổi mức điện áp, thường dùng để hạ áp từ cấp điện áp cao (22.9kV) xuống điện áp sử dụng (380V, 220V). Trong xây dựng, cần chú ý đến công suất (kVA), kiểu dây quấn (ngâm dầu/khô), và phương thức làm mát. Tiêu chuẩn lắp đặt phòng biến áp có sự khác biệt giữa Hàn Quốc và Việt Nam.",
        "context": "전기 용량 산정, 수변전실 설계, 전기설비 시방서 작성",
        "culturalNote": "한국은 변압기실 설치 기준이 매우 엄격하며(소방법, 전기설비기준 등), 도심지에서는 몰드 변압기가 선호됩니다. 베트남은 유입식 변압기가 더 보편적이나 화재 위험성으로 인해 최근 몰드식 변압기 사용이 증가하고 있습니다. 통역 시 안전 기준과 유지보수 차이를 설명해야 합니다.",
        "commonMistakes": [
            {
                "mistake": "용량 단위 kW와 kVA 혼동",
                "correction": "변압기 용량은 kVA로 표기 (예: 1000kVA)",
                "explanation": "kW는 유효전력, kVA는 피상전력으로 변압기는 kVA로 표기합니다."
            },
            {
                "mistake": "'전압 바꾸는 기계'로 직역",
                "correction": "Máy biến áp (변압기)",
                "explanation": "기술 용어는 표준 베트남어 용어로 사용해야 혼란을 방지합니다."
            },
            {
                "mistake": "유입식과 몰드식 구분 없이 통역",
                "correction": "유입식(ngâm dầu), 몰드식(khô/epoxy)",
                "explanation": "냉각 방식에 따라 설치 장소와 안전 기준이 크게 다릅니다."
            }
        ],
        "examples": [
            {
                "ko": "1000kVA 몰드 변압기 2대를 지하 1층 변압기실에 설치합니다.",
                "vi": "Lắp đặt 2 máy biến áp khô 1000kVA tại phòng biến áp tầng hầm 1.",
                "situation": "formal"
            },
            {
                "ko": "변압기 소음 기준치를 초과해서 방음 대책이 필요합니다.",
                "vi": "Tiếng ồn máy biến áp vượt quá tiêu chuẩn, cần có biện pháp cách âm.",
                "situation": "onsite"
            },
            {
                "ko": "이 변압기는 22.9kV를 380V로 변환합니다.",
                "vi": "Máy biến áp này chuyển đổi từ 22.9kV xuống 380V.",
                "situation": "formal"
            }
        ],
        "relatedTerms": ["수전설비", "배전반", "전력케이블", "전력감시시스템"]
    },
    {
        "slug": "tu-phan-phoi-dien",
        "korean": "배전반",
        "vietnamese": "Tủ phân phối điện",
        "hanja": "配電盤",
        "hanjaReading": "配(나눌 배) + 電(전기 전) + 盤(쟁반 반)",
        "pronunciation": "배전반",
        "meaningKo": "변압기에서 받은 전력을 각 부하(조명, 동력, 콘센트 등)로 분배하는 전기 설비입니다. 통역 시 주의할 점은 배전반(저압 분전반), 분전반(소형 분전), MCC반(동력제어반) 등을 명확히 구분해야 하며, 베트남에서는 'Tủ phân phối điện' 또는 'Tủ điện phân phối'로 표현합니다. 차단기 용량, MCCB/ACB 사양, 접지 방식 등 세부 스펙을 정확히 전달해야 하며, 한국의 KS 규격과 베트남의 TCVN 규격 차이를 고려해야 합니다.",
        "meaningVi": "Thiết bị điện dùng để phân phối điện năng từ máy biến áp đến các tải khác nhau (chiếu sáng, động lực, ổ cắm). Cần phân biệt rõ tủ phân phối chính, tủ phân phối phụ và tủ MCC (điều khiển động cơ). Phải chú ý đến dung lượng CB, loại MCCB/ACB, và phương thức tiếp địa. Có sự khác biệt giữa tiêu chuẩn KS của Hàn Quốc và TCVN của Việt Nam.",
        "context": "전기설비 시공 계획, 전력 계통도 작성, 안전점검",
        "culturalNote": "한국은 배전반 내부 배선과 라벨링이 매우 체계적이며, 정기적인 열화상 점검이 의무화되어 있습니다. 베트남은 상대적으로 유지보수 기준이 느슨하나, 습도와 고온으로 인한 부식 문제가 더 흔합니다. 통역 시 예방정비의 중요성을 강조해야 합니다.",
        "commonMistakes": [
            {
                "mistake": "분전반과 배전반을 구분하지 않음",
                "correction": "배전반(Tủ phân phối chính), 분전반(Tủ phân phối phụ)",
                "explanation": "배전반은 큰 용량의 주 분배 설비, 분전반은 말단 분기 설비입니다."
            },
            {
                "mistake": "'전기 박스'로 통역",
                "correction": "Tủ phân phối điện (배전반)",
                "explanation": "기술 용어를 일상어로 번역하면 전문성이 떨어지고 오해를 유발합니다."
            },
            {
                "mistake": "MCC반과 배전반 혼동",
                "correction": "배전반(phân phối), MCC반(điều khiển động cơ)",
                "explanation": "MCC반은 모터 제어에 특화된 설비로 배전반과 기능이 다릅니다."
            }
        ],
        "examples": [
            {
                "ko": "지하 전기실에 메인 배전반을 설치하고, 각 층에 분전반을 배치합니다.",
                "vi": "Lắp đặt tủ phân phối chính tại phòng điện tầng hầm, và bố trí tủ phân phối phụ ở mỗi tầng.",
                "situation": "formal"
            },
            {
                "ko": "배전반 내부 온도가 높아서 냉각팬 추가가 필요합니다.",
                "vi": "Nhiệt độ bên trong tủ phân phối cao, cần bổ sung quạt làm mát.",
                "situation": "onsite"
            },
            {
                "ko": "배전반 차단기 용량을 확인해 주세요.",
                "vi": "Vui lòng kiểm tra dung lượng CB trong tủ phân phối.",
                "situation": "onsite"
            }
        ],
        "relatedTerms": ["변압기", "MCC반", "전력케이블", "차단기"]
    },
    {
        "slug": "tu-mcc",
        "korean": "MCC반",
        "vietnamese": "Tủ MCC",
        "hanja": None,
        "hanjaReading": None,
        "pronunciation": "엠씨씨반",
        "meaningKo": "Motor Control Center의 약자로, 여러 대의 전동기를 집중 제어하고 보호하는 전기 설비입니다. 통역 시 주의할 점은 단순히 '모터 제어반'이 아니라 MCC반의 구성 요소(전자접촉기, 열동계전기, 인버터 등)와 제어 방식(직입 기동, 스타델타 기동, 인버터 기동 등)을 정확히 전달해야 합니다. 베트남에서는 'Tủ MCC' 또는 'Tủ điều khiển động cơ tập trung'으로 표현하며, 건설 현장에서는 펌프, 송풍기, 냉각탑 등의 동력 설비 제어에 필수적입니다.",
        "meaningVi": "Viết tắt của Motor Control Center, là thiết bị điện tập trung điều khiển và bảo vệ nhiều động cơ. Bao gồm các thành phần như contactor, rơle nhiệt, biến tần. Cần chú ý đến phương thức khởi động (khởi động trực tiếp, sao-tam giác, biến tần). Trong công trường xây dựng, MCC được dùng để điều khiển bơm, quạt, tháp giải nhiệt và các thiết bị động lực khác.",
        "context": "기계설비 연동, 전기 동력 설비 시공, 제어 시스템 통합",
        "culturalNote": "한국은 MCC반에 PLC 기반 자동 제어와 원격 감시 기능이 표준화되어 있으며, 에너지 절감을 위해 인버터 사용률이 높습니다. 베트남은 초기 투자 비용 때문에 직입 기동 방식이 여전히 많으나, 최근 에너지 효율 규제 강화로 인버터 도입이 증가하고 있습니다. 통역 시 제어 방식의 장단점을 비교 설명해야 합니다.",
        "commonMistakes": [
            {
                "mistake": "'모터 컨트롤 센터'를 그대로 읽음",
                "correction": "MCC반 (Tủ MCC)",
                "explanation": "현장에서는 약어를 그대로 사용하는 것이 일반적입니다."
            },
            {
                "mistake": "배전반과 구분 없이 사용",
                "correction": "배전반은 전력 분배, MCC반은 모터 제어",
                "explanation": "기능과 내부 구성이 완전히 다른 설비입니다."
            },
            {
                "mistake": "인버터와 MCC반 혼동",
                "correction": "인버터는 MCC반의 구성 요소 중 하나",
                "explanation": "인버터(biến tần)는 MCC반 내에 포함될 수 있는 제어 장치입니다."
            }
        ],
        "examples": [
            {
                "ko": "기계실 MCC반에서 급배수 펌프를 제어합니다.",
                "vi": "Điều khiển bơm cấp thoát nước từ tủ MCC tại phòng máy.",
                "situation": "formal"
            },
            {
                "ko": "MCC반 내 인버터 고장으로 냉각탑 운전이 중단되었습니다.",
                "vi": "Tháp giải nhiệt ngừng hoạt động do biến tần trong tủ MCC bị hỏng.",
                "situation": "onsite"
            },
            {
                "ko": "이 현장은 15kW급 모터 20대를 MCC반으로 통합 제어합니다.",
                "vi": "Công trường này điều khiển tập trung 20 động cơ 15kW bằng tủ MCC.",
                "situation": "formal"
            }
        ],
        "relatedTerms": ["배전반", "인버터", "전자접촉기", "전력감시시스템"]
    },
    {
        "slug": "ups",
        "korean": "UPS",
        "vietnamese": "UPS",
        "hanja": None,
        "hanjaReading": None,
        "pronunciation": "유피에스",
        "meaningKo": "Uninterruptible Power Supply의 약자로, 무정전 전원장치를 의미합니다. 정전 또는 전압 이상 시 축전지로 순간적으로 전력을 공급하여 컴퓨터, 서버, 통신 설비, 보안 시스템 등 중요 부하의 연속 운전을 보장합니다. 통역 시 주의할 점은 UPS 용량(kVA), 백업 시간(분), 타입(On-line/Off-line/Line-interactive) 등을 정확히 전달해야 하며, 베트남에서는 'UPS' 또는 'Bộ lưu điện'으로 표현합니다. 건설 현장에서는 소방 설비, CCTV, 출입통제 시스템 등의 백업 전원으로 필수적입니다.",
        "meaningVi": "Viết tắt của Uninterruptible Power Supply, thiết bị cung cấp điện liên tục không gián đoạn. Khi mất điện hoặc điện áp bất thường, UPS sử dụng ắc quy để cung cấp điện tức thì cho các tải quan trọng như máy tính, server, hệ thống thông tin, an ninh. Cần chú ý đến công suất (kVA), thời gian dự phòng (phút), và loại UPS (On-line/Off-line/Line-interactive). Trong xây dựng, UPS là thiết bị bắt buộc cho hệ thống PCCC, camera, kiểm soát ra vào.",
        "context": "약전 설비 설계, 정보통신실 구축, 비상전원 계획",
        "culturalNote": "한국은 UPS가 건축법과 소방법에 따라 특정 설비(소방, 승강기 비상등)에 의무적으로 설치되며, 정기적인 부하 테스트가 법적으로 요구됩니다. 베트남은 정전 빈도가 높아 UPS 사용이 더 보편적이지만, 유지보수가 부실한 경우가 많아 실제 정전 시 작동하지 않는 사례가 빈번합니다. 통역 시 정기 점검의 중요성을 강조해야 합니다.",
        "commonMistakes": [
            {
                "mistake": "'무정전 장치'로만 통역",
                "correction": "UPS 또는 Bộ lưu điện (무정전 전원장치)",
                "explanation": "약어를 함께 사용해야 기술 문서와 일치합니다."
            },
            {
                "mistake": "비상발전기와 혼동",
                "correction": "UPS는 즉시 전환(ms), 발전기는 수십 초 소요",
                "explanation": "UPS는 순간 전환, 발전기는 기동 시간이 필요합니다."
            },
            {
                "mistake": "용량 kW와 kVA 혼동",
                "correction": "UPS 용량은 kVA로 표기 (예: 10kVA UPS)",
                "explanation": "UPS는 피상전력(kVA)으로 용량을 표기합니다."
            }
        ],
        "examples": [
            {
                "ko": "서버실에 20kVA UPS를 설치하여 30분간 백업 전원을 공급합니다.",
                "vi": "Lắp đặt UPS 20kVA tại phòng server để cung cấp điện dự phòng trong 30 phút.",
                "situation": "formal"
            },
            {
                "ko": "UPS 배터리 교체 주기가 지났습니다.",
                "vi": "Đã đến chu kỳ thay thế ắc quy UPS.",
                "situation": "onsite"
            },
            {
                "ko": "소방 설비는 UPS와 비상발전기 이중 백업으로 설계했습니다.",
                "vi": "Hệ thống PCCC được thiết kế dự phòng kép bằng UPS và máy phát điện dự phòng.",
                "situation": "formal"
            }
        ],
        "relatedTerms": ["비상발전기", "축전지", "배전반", "전력감시시스템"]
    },
    {
        "slug": "may-phat-dien-du-phong",
        "korean": "비상발전기",
        "vietnamese": "Máy phát điện dự phòng",
        "hanja": "非常發電機",
        "hanjaReading": "非(아닐 비) + 常(떳떳할 상) + 發(쏠 발) + 電(전기 전) + 機(기계 기)",
        "pronunciation": "비상발전기",
        "meaningKo": "정전 시 자동으로 기동하여 전력을 공급하는 디젤 또는 가스 발전기입니다. 통역 시 주의할 점은 발전기 용량(kVA), 연료 종류(경유/LNG), 기동 방식(자동/수동), ATS(자동절체개폐기) 연동 여부를 정확히 전달해야 하며, 베트남에서는 'Máy phát điện dự phòng' 또는 'Máy phát dự phòng'으로 표현합니다. 한국은 소방법에 따라 일정 규모 이상 건축물에 의무 설치되며, 베트남은 정전 빈도가 높아 대부분의 상업 건물에 설치되지만 유지보수 수준 차이가 큽니다.",
        "meaningVi": "Máy phát điện (diesel hoặc gas) tự động khởi động cung cấp điện khi mất điện lưới. Cần chú ý đến công suất (kVA), loại nhiên liệu (dầu DO/LNG), phương thức khởi động (tự động/thủ công), và liên động với ATS (thiết bị chuyển đổi nguồn tự động). Ở Hàn Quốc, luật PCCC bắt buộc lắp đặt cho các tòa nhà từ quy mô nhất định. Ở Việt Nam, mất điện thường xuyên nên hầu hết các tòa nhà thương mại đều có máy phát, nhưng chất lượng bảo trì khác nhau rất lớn.",
        "context": "전기 설비 계획, 비상전원 용량 산정, 소방 설비 연동",
        "culturalNote": "한국은 비상발전기 설치 기준(소방법, 건축법)이 엄격하며, 월 1회 무부하 시험과 연 1회 부하 시험이 의무화되어 있습니다. 베트남은 정전이 잦아 비상발전기가 거의 상시 가동되는 경우도 있으며, 연료 품질과 유지보수 불량으로 인한 고장이 빈번합니다. 통역 시 정기 점검과 연료 관리 중요성을 강조해야 합니다.",
        "commonMistakes": [
            {
                "mistake": "'발전기'만 언급",
                "correction": "비상발전기 (Máy phát điện dự phòng)",
                "explanation": "비상용과 상용 발전기를 구분해야 합니다."
            },
            {
                "mistake": "UPS와 혼동",
                "correction": "UPS는 즉시, 발전기는 수십 초 후 전환",
                "explanation": "작동 원리와 백업 시간이 완전히 다릅니다."
            },
            {
                "mistake": "ATS 없이 발전기만 언급",
                "correction": "비상발전기 + ATS (자동절체개폐기) 시스템",
                "explanation": "발전기는 ATS와 함께 동작하는 시스템입니다."
            }
        ],
        "examples": [
            {
                "ko": "500kVA 비상발전기를 옥상 발전기실에 설치합니다.",
                "vi": "Lắp đặt máy phát điện dự phòng 500kVA tại phòng máy phát trên sân thượng.",
                "situation": "formal"
            },
            {
                "ko": "정전 후 15초 내에 비상발전기가 자동 기동됩니다.",
                "vi": "Máy phát điện dự phòng tự động khởi động trong vòng 15 giây sau khi mất điện.",
                "situation": "formal"
            },
            {
                "ko": "발전기 월간 시운전 일정을 공유해 주세요.",
                "vi": "Vui lòng chia sẻ lịch thử máy phát hàng tháng.",
                "situation": "onsite"
            }
        ],
        "relatedTerms": ["UPS", "ATS", "축전지", "전력감시시스템"]
    },
    {
        "slug": "ac-quy",
        "korean": "축전지",
        "vietnamese": "Ắc quy",
        "hanja": "蓄電池",
        "hanjaReading": "蓄(쌓을 축) + 電(전기 전) + 池(못 지)",
        "pronunciation": "축전지",
        "meaningKo": "전기를 화학 에너지로 저장했다가 필요 시 방전하여 사용하는 2차 전지입니다. 건설 현장에서는 UPS, 비상조명, 비상발전기 기동용 등으로 사용됩니다. 통역 시 주의할 점은 배터리 타입(납축전지/리튬이온), 용량(Ah), 전압(V), 수명(사이클) 등을 정확히 전달해야 하며, 베트남에서는 'Ắc quy' 또는 'Bình ắc quy'로 표현합니다. 한국은 소방법에 따라 비상조명용 축전지 교체 주기가 법적으로 규정되어 있으며, 베트남은 고온 환경으로 인해 배터리 수명이 짧아지는 경향이 있습니다.",
        "meaningVi": "Pin sạc (ắc quy) dùng để lưu trữ năng lượng điện dưới dạng hóa năng và phóng điện khi cần. Trong xây dựng, được sử dụng cho UPS, đèn chiếu sáng khẩn cấp, khởi động máy phát điện dự phòng. Cần chú ý đến loại ắc quy (chì-axit/lithium-ion), dung lượng (Ah), điện áp (V), tuổi thọ (chu kỳ). Ở Hàn Quốc, luật PCCC quy định chu kỳ thay thế ắc quy cho đèn khẩn cấp. Ở Việt Nam, môi trường nhiệt độ cao làm giảm tuổi thọ ắc quy.",
        "context": "비상전원 설계, UPS 사양 검토, 소방 설비 유지보수",
        "culturalNote": "한국은 축전지 폐기 시 환경 규제가 엄격하여 전문 업체를 통해 처리해야 하며, 리튬이온 배터리 사용이 증가하고 있습니다. 베트남은 납축전지가 여전히 주류이나, 폐기 처리 기준이 느슨하여 환경 문제가 우려됩니다. 통역 시 안전 보관과 폐기 절차를 설명해야 합니다.",
        "commonMistakes": [
            {
                "mistake": "'배터리'로만 통역",
                "correction": "축전지 (Ắc quy) 또는 배터리 (Pin)",
                "explanation": "공식 문서에서는 '축전지' 용어를 사용합니다."
            },
            {
                "mistake": "용량 단위 Wh와 Ah 혼동",
                "correction": "축전지는 Ah(암페어시), 에너지는 Wh(와트시)",
                "explanation": "Ah는 전하량, Wh는 에너지량입니다."
            },
            {
                "mistake": "자동차 배터리와 산업용 축전지 혼동",
                "correction": "자동차용(12V), UPS용(수십~수백V)",
                "explanation": "용도와 전압, 용량이 완전히 다릅니다."
            }
        ],
        "examples": [
            {
                "ko": "UPS용 축전지는 200Ah 납축전지 20개로 구성됩니다.",
                "vi": "Ắc quy cho UPS gồm 20 bình ắc quy chì-axit 200Ah.",
                "situation": "formal"
            },
            {
                "ko": "비상조명 축전지 교체 주기가 지나서 점검이 필요합니다.",
                "vi": "Đã quá chu kỳ thay ắc quy đèn khẩn cấp, cần kiểm tra.",
                "situation": "onsite"
            },
            {
                "ko": "발전기 시동용 축전지 전압이 낮습니다.",
                "vi": "Điện áp ắc quy khởi động máy phát thấp.",
                "situation": "onsite"
            }
        ],
        "relatedTerms": ["UPS", "비상발전기", "비상조명", "전력케이블"]
    },
    {
        "slug": "cap-dien-luc",
        "korean": "전력케이블",
        "vietnamese": "Cáp điện lực",
        "hanja": "電力cable",
        "hanjaReading": "電(전기 전) + 力(힘 력) + cable(영어)",
        "pronunciation": "전력케이블",
        "meaningKo": "전력을 전송하기 위한 절연 케이블로, 건설 현장에서는 수전설비부터 변압기, 배전반을 거쳐 각 부하까지 연결하는 핵심 설비입니다. 통역 시 주의할 점은 케이블 규격(mm²), 심수(3C, 4C 등), 절연 등급(FR, HFIX 등), 포설 방식(전선관/덕트/케이블트레이) 등을 정확히 전달해야 하며, 베트남에서는 'Cáp điện lực' 또는 'Cáp động lực'으로 표현합니다. 한국의 KS 규격과 베트난의 TCVN 규격 간 차이, 특히 난연 등급과 허용 전류 기준을 비교 설명해야 합니다.",
        "meaningVi": "Cáp cách điện dùng để truyền tải điện năng, từ thiết bị thu điện đến máy biến áp, tủ phân phối và các tải cuối. Cần chú ý đến tiết diện cáp (mm²), số lõi (3C, 4C...), cấp cách điện (FR, HFIX...), và phương thức lắp đặt (ống luồn dây/máng cáp/thang cáp). Có sự khác biệt giữa tiêu chuẩn KS của Hàn Quốc và TCVN của Việt Nam, đặc biệt là cấp chống cháy và dòng điện cho phép.",
        "context": "전기 배선 시공, 케이블 물량 산출, 전력 손실 계산",
        "culturalNote": "한국은 지중 배선 비율이 높고 난연 케이블 사용이 의무화되어 있으며, 케이블 트레이 시공 기준이 엄격합니다. 베트남은 가공 배선이 여전히 많고, 비용 절감을 위해 저급 케이블을 사용하는 경우가 있어 화재 위험이 높습니다. 통역 시 안전 기준 준수의 중요성을 강조해야 합니다.",
        "commonMistakes": [
            {
                "mistake": "'전선'과 '케이블' 혼용",
                "correction": "전선(dây điện)은 단선, 케이블(cáp)은 다심",
                "explanation": "전선은 단일 도체, 케이블은 여러 도체가 절연 피복으로 묶인 것입니다."
            },
            {
                "mistake": "규격 표기 없이 '케이블'만 언급",
                "correction": "185mm² 4C HFIX 케이블 (Cáp HFIX 4C 185mm²)",
                "explanation": "시공과 견적을 위해 규격을 반드시 명시해야 합니다."
            },
            {
                "mistake": "통신 케이블과 전력 케이블 혼동",
                "correction": "전력 케이블(cáp điện lực), 통신 케이블(cáp thông tin)",
                "explanation": "용도와 구조가 완전히 다릅니다."
            }
        ],
        "examples": [
            {
                "ko": "변압기에서 배전반까지 240mm² 4C HFIX 케이블로 연결합니다.",
                "vi": "Kết nối từ máy biến áp đến tủ phân phối bằng cáp HFIX 4C 240mm².",
                "situation": "formal"
            },
            {
                "ko": "케이블 트레이 지지 간격을 1.5m로 시공하세요.",
                "vi": "Thi công khoảng cách giá đỡ thang cáp là 1.5m.",
                "situation": "onsite"
            },
            {
                "ko": "이 구간은 난연 케이블 사용이 의무입니다.",
                "vi": "Đoạn này bắt buộc sử dụng cáp chống cháy.",
                "situation": "formal"
            }
        ],
        "relatedTerms": ["버스덕트", "케이블트레이", "배전반", "변압기"]
    },
    {
        "slug": "bus-duct",
        "korean": "버스덕트",
        "vietnamese": "Bus duct",
        "hanja": None,
        "hanjaReading": None,
        "pronunciation": "버스덕트",
        "meaningKo": "대용량 전력을 전송하기 위한 금속 덕트형 배전 장치로, 전력케이블을 대체하여 공간 절약과 시공 효율성을 높입니다. 통역 시 주의할 점은 정격 전류(A), 타입(플러그인식/페더식), 방진 등급(IP 등급) 등을 정확히 전달해야 하며, 베트남에서는 'Bus duct' 또는 'Thanh cái dẫn điện'으로 표현합니다. 한국은 대형 건물과 공장에서 케이블 대신 버스덕트 사용이 증가하고 있으며, 베트남은 초기 비용 때문에 아직 케이블이 주류이나 고층 건물에서는 버스덕트 도입이 늘고 있습니다.",
        "meaningVi": "Hệ thống dẫn điện dạng thanh cái đóng kín trong hộp kim loại, dùng để truyền tải điện công suất lớn, thay thế cáp điện lực giúp tiết kiệm không gian và hiệu quả thi công. Cần chú ý đến dòng điện định mức (A), loại (plug-in/feeder), cấp bảo vệ bụi nước (IP rating). Ở Hàn Quốc, bus duct ngày càng được sử dụng thay cáp trong các tòa nhà lớn và nhà máy. Ở Việt Nam, do chi phí ban đầu cao nên cáp vẫn phổ biến, nhưng các tòa nhà cao tầng bắt đầu áp dụng bus duct.",
        "context": "대형 건물 전기 간선 설계, 공장 전력 배선, 케이블 대안 검토",
        "culturalNote": "한국은 버스덕트 제조사와 시공 업체가 전문화되어 있으며, 품질 기준이 엄격합니다. 베트남은 수입 의존도가 높아 가격이 상대적으로 비싸며, 숙련된 시공 인력이 부족하여 설치 품질 편차가 큽니다. 통역 시 시공 교육과 품질 관리 중요성을 강조해야 합니다.",
        "commonMistakes": [
            {
                "mistake": "'버스 덕트'를 '버스 관'으로 직역",
                "correction": "버스덕트 (Bus duct)",
                "explanation": "고유 기술 용어이므로 그대로 사용합니다."
            },
            {
                "mistake": "케이블 트레이와 혼동",
                "correction": "버스덕트는 도체 내장, 케이블 트레이는 케이블 거치대",
                "explanation": "버스덕트는 전력 전송 장치, 트레이는 케이블 지지 구조물입니다."
            },
            {
                "mistake": "용량 kVA와 정격 전류 A 혼동",
                "correction": "버스덕트는 정격 전류(A)로 표기 (예: 3200A)",
                "explanation": "버스덕트 용량은 암페어(A)로 표시합니다."
            }
        ],
        "examples": [
            {
                "ko": "지하 전기실에서 각 층까지 3200A 버스덕트로 간선을 구성합니다.",
                "vi": "Cấu trúc đường dây chính từ phòng điện tầng hầm đến các tầng bằng bus duct 3200A.",
                "situation": "formal"
            },
            {
                "ko": "버스덕트 접속부 볼트 조임 토크를 확인하세요.",
                "vi": "Kiểm tra mô-men xiết bu-lông tại điểm nối bus duct.",
                "situation": "onsite"
            },
            {
                "ko": "케이블 대신 버스덕트를 사용하면 샤프트 공간을 30% 절약할 수 있습니다.",
                "vi": "Sử dụng bus duct thay cáp có thể tiết kiệm 30% không gian shaft.",
                "situation": "formal"
            }
        ],
        "relatedTerms": ["전력케이블", "배전반", "케이블트레이", "변압기"]
    },
    {
        "slug": "he-thong-giam-sat-dien",
        "korean": "전력감시시스템",
        "vietnamese": "Hệ thống giám sát điện",
        "hanja": "電力監視system",
        "hanjaReading": "電(전기 전) + 力(힘 력) + 監(볼 감) + 視(볼 시) + system(영어)",
        "pronunciation": "전력감시시스템",
        "meaningKo": "건물의 전력 사용량, 전압, 전류, 역률, 수요 전력 등을 실시간으로 모니터링하고 제어하는 시스템입니다. 통역 시 주의할 점은 EMS(에너지관리시스템), BEMS(건물에너지관리시스템), SCADA(원격감시제어) 등 상위 시스템과의 연동 여부, 계측 항목, 데이터 수집 주기 등을 정확히 전달해야 하며, 베트남에서는 'Hệ thống giám sát điện' 또는 'Hệ thống quản lý năng lượng điện'으로 표현합니다. 한국은 에너지법에 따라 일정 규모 이상 건물에 전력감시시스템 설치가 의무화되어 있으며, 베트남도 에너지 절감 정책으로 도입이 확대되고 있습니다.",
        "meaningVi": "Hệ thống giám sát và điều khiển thời gian thực các thông số như lượng điện tiêu thụ, điện áp, dòng điện, hệ số công suất, công suất yêu cầu của tòa nhà. Cần chú ý đến khả năng liên kết với hệ thống cấp cao hơn như EMS (quản lý năng lượng), BEMS (quản lý năng lượng tòa nhà), SCADA (điều khiển giám sát từ xa), các thông số đo lường, chu kỳ thu thập dữ liệu. Ở Hàn Quốc, luật năng lượng bắt buộc lắp đặt hệ thống giám sát điện cho các tòa nhà từ quy mô nhất định. Ở Việt Nam, chính sách tiết kiệm năng lượng cũng thúc đẩy việc áp dụng hệ thống này.",
        "context": "스마트 빌딩 구축, 에너지 절감 계획, BEMS 통합",
        "culturalNote": "한국은 전력감시시스템이 IoT 기반으로 고도화되어 AI 예측 기능까지 통합되고 있으며, 정부 보조금으로 설치가 장려됩니다. 베트남은 대형 건물 중심으로 도입되고 있으나, 데이터 분석과 활용 수준은 아직 초기 단계입니다. 통역 시 시스템 도입의 경제적 효과를 강조해야 합니다.",
        "commonMistakes": [
            {
                "mistake": "'전기 모니터링'으로만 통역",
                "correction": "전력감시시스템 (Hệ thống giám sát điện)",
                "explanation": "공식 용어를 사용해야 기술 문서와 일치합니다."
            },
            {
                "mistake": "BEMS와 동일한 개념으로 사용",
                "correction": "전력감시는 BEMS의 하위 시스템",
                "explanation": "BEMS는 전력, 냉난방, 조명 등 전체 에너지를 관리합니다."
            },
            {
                "mistake": "단순 전력량계와 혼동",
                "correction": "감시시스템은 실시간 분석과 제어 기능 포함",
                "explanation": "전력량계는 단순 계량, 감시시스템은 분석과 제어까지 수행합니다."
            }
        ],
        "examples": [
            {
                "ko": "전력감시시스템을 통해 층별 전력 사용량을 실시간으로 확인할 수 있습니다.",
                "vi": "Có thể kiểm tra lượng điện tiêu thụ từng tầng theo thời gian thực qua hệ thống giám sát điện.",
                "situation": "formal"
            },
            {
                "ko": "수요 전력이 계약 전력을 초과하면 시스템이 자동으로 경보를 발생시킵니다.",
                "vi": "Khi công suất yêu cầu vượt công suất hợp đồng, hệ thống tự động phát cảnh báo.",
                "situation": "formal"
            },
            {
                "ko": "전력감시시스템 데이터를 분석해서 에너지 절감 방안을 제안하세요.",
                "vi": "Vui lòng phân tích dữ liệu hệ thống giám sát điện để đề xuất phương án tiết kiệm năng lượng.",
                "situation": "onsite"
            }
        ],
        "relatedTerms": ["배전반", "MCC반", "UPS", "비상발전기"]
    }
]

# construction.json 파일 경로
project_root = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
file_path = os.path.join(project_root, "data", "terms", "construction.json")

# 기존 파일 읽기
with open(file_path, "r", encoding="utf-8") as f:
    existing_data = json.load(f)

# 새 데이터 추가
existing_data.extend(data)

# 파일 저장
with open(file_path, "w", encoding="utf-8") as f:
    json.dump(existing_data, f, ensure_ascii=False, indent=2)

print(f"✅ {len(data)}개 용어 추가 완료 → {file_path}")
