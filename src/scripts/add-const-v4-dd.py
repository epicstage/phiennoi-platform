#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
냉난방/공조(HVAC) 건설 용어 추가 스크립트
Tier S 품질 기준 준수
"""

import json
import os

# 추가할 용어 데이터 (10개)
data = [
    {
        "slug": "may-dieu-hoa-khong-khi",
        "korean": "에어컨",
        "vietnamese": "Máy điều hòa không khí",
        "hanja": "空調機",
        "hanjaReading": "空(빌 공) + 調(고를 조) + 機(틀 기)",
        "pronunciation": "마이 디에우 호아 콩 키",
        "meaningKo": "실내 온도와 습도를 조절하는 냉난방 설비. 통역 시 단순히 '에어컨'이라고만 하지 말고, 냉난방 기능 여부(냉방 전용/냉난방 겸용), 용량(kW 또는 평수), 설치 방식(벽걸이형/천장형/스탠드형)을 명확히 구분해야 합니다. 베트남에서는 냉방 전용이 대부분이므로 난방 기능 유무를 반드시 확인하세요.",
        "meaningVi": "Thiết bị điều chỉnh nhiệt độ và độ ẩm trong phòng. Cần phân biệt loại chỉ làm lạnh và loại làm lạnh/sưởi ấm kết hợp, công suất (kW), và phương thức lắp đặt (treo tường/âm trần/đứng sàn).",
        "context": "HVAC, 냉난방",
        "culturalNote": "한국은 냉난방 겸용 에어컨이 일반적이지만, 베트남은 열대 기후로 냉방 전용이 대부분입니다. 'Máy lạnh'는 냉방 전용, 'Máy điều hòa'는 냉난방 겸용을 의미할 수 있으므로 통역 시 기능을 명확히 해야 합니다. 또한 베트남에서는 전력 요금이 높아 인버터 에어컨(máy điều hòa inverter) 선호도가 높습니다.",
        "commonMistakes": [
            {
                "mistake": "모든 에어컨을 'máy lạnh'로 통일",
                "correction": "냉방 전용은 'máy lạnh', 냉난방 겸용은 'máy điều hòa'",
                "explanation": "기능 차이를 구분하지 않으면 냉난방 겸용 에어컨을 단순 냉방기로 오해할 수 있음"
            },
            {
                "mistake": "'실외기'를 'máy ngoài trời'로 직역",
                "correction": "'dàn nóng' (응축기) 또는 'cục nóng'",
                "explanation": "베트남 현장에서는 실외기를 'dàn nóng'이라고 부르며, 실내기는 'dàn lạnh'입니다"
            },
            {
                "mistake": "용량을 '평수'로만 설명",
                "correction": "kW 또는 BTU 단위로 명시",
                "explanation": "베트남에서는 평수 개념이 생소하므로 국제 표준 단위 사용 필수"
            }
        ],
        "examples": [
            {
                "ko": "이 사무실에는 18평형 시스템 에어컨을 설치합니다.",
                "vi": "Văn phòng này sẽ lắp đặt máy điều hòa multi 5kW (tương đương diện tích 60m²).",
                "situation": "formal"
            },
            {
                "ko": "실외기 위치는 소음 규정을 확인하세요.",
                "vi": "Vị trí đặt dàn nóng cần kiểm tra quy định về tiếng ồn.",
                "situation": "onsite"
            },
            {
                "ko": "냉매 충전 후 시운전하겠습니다.",
                "vi": "Sau khi nạp gas lạnh, chúng tôi sẽ chạy thử.",
                "situation": "onsite"
            }
        ],
        "relatedTerms": ["냉매", "실외기", "덕트", "칠러", "환기"]
    },
    {
        "slug": "dan-nong",
        "korean": "실외기",
        "vietnamese": "Dàn nóng",
        "hanja": "室外機",
        "hanjaReading": "室(집 실) + 外(밖 외) + 機(틀 기)",
        "pronunciation": "잔 농",
        "meaningKo": "에어컨의 열교환 장치로 실외에 설치되는 기기. 통역 시 주의할 점은 베트남에서는 '뜨거운 열을 배출하는 장치'라는 뜻으로 'dàn nóng'이라 부르며, 설치 위치(옥상/외벽/지상), 소음 규정, 배수 처리, 냉매 배관 거리 제한 등을 함께 설명해야 합니다. 멀티형의 경우 실내기 개수와의 매칭도 확인하세요.",
        "meaningVi": "Thiết bị trao đổi nhiệt của máy điều hòa, được lắp ở ngoài trời. Cần lưu ý vị trí lắp đặt, quy định tiếng ồn, thoát nước ngưng, và khoảng cách đường ống gas giữa dàn nóng và dàn lạnh.",
        "context": "HVAC, 에어컨",
        "culturalNote": "베트남에서는 고층 아파트가 많아 실외기 설치 공간이 제한적입니다. 발코니나 외벽에 설치 시 소음 및 미관 규정이 엄격하며, 이웃 민원이 자주 발생합니다. 한국처럼 옥상에 일괄 설치하는 경우는 드물고, 각 세대마다 개별 설치가 일반적입니다.",
        "commonMistakes": [
            {
                "mistake": "'실외기'를 'máy ngoài'로 축약",
                "correction": "'dàn nóng' 또는 'cục nóng' 사용",
                "explanation": "현장에서 통용되는 정확한 용어 사용 필요"
            },
            {
                "mistake": "냉매 배관 거리를 미터로만 설명",
                "correction": "최대 허용 거리와 성능 저하 가능성 함께 설명",
                "explanation": "거리가 멀어지면 냉방 효율이 떨어지므로 기술적 제약 명시 필요"
            },
            {
                "mistake": "'응축기'와 '실외기'를 혼용",
                "correction": "'dàn nóng'으로 통일 (응축기는 내부 부품)",
                "explanation": "실외기 전체를 의미할 때는 dàn nóng, 내부 응축기는 dàn ngưng"
            }
        ],
        "examples": [
            {
                "ko": "실외기는 통풍이 잘 되는 곳에 설치하세요.",
                "vi": "Dàn nóng cần lắp đặt ở nơi thông gió tốt.",
                "situation": "onsite"
            },
            {
                "ko": "이 시스템은 실외기 1대에 실내기 5대를 연결할 수 있습니다.",
                "vi": "Hệ thống này có thể kết nối 5 dàn lạnh với 1 dàn nóng.",
                "situation": "formal"
            },
            {
                "ko": "실외기 진동 때문에 방진 패드를 추가했습니다.",
                "vi": "Chúng tôi đã thêm tấm chống rung vì dàn nóng rung quá mạnh.",
                "situation": "onsite"
            }
        ],
        "relatedTerms": ["실내기", "냉매배관", "에어컨", "멀티에어컨", "인버터"]
    },
    {
        "slug": "chiller",
        "korean": "칠러",
        "vietnamese": "Chiller",
        "hanja": None,
        "hanjaReading": None,
        "pronunciation": "칠러",
        "meaningKo": "대형 건물의 중앙 냉방 시스템에서 냉수를 생산하는 장치. 통역 시 주의할 점은 칠러 방식(공랭식/수랭식), 냉매 종류, 용량(RT 또는 kW), 에너지 효율(COP), 냉각탑 연계 여부를 명확히 구분해야 합니다. 베트nam에서는 대형 오피스, 호텔, 쇼핑몰에서 주로 사용하며, 전력 소비가 크므로 운영비 관련 설명이 중요합니다.",
        "meaningVi": "Thiết bị sản xuất nước lạnh cho hệ thống điều hòa trung tâm của các tòa nhà lớn. Cần phân biệt loại làm mát bằng gió (air-cooled) và làm mát bằng nước (water-cooled), công suất (RT hoặc kW), và hiệu suất năng lượng (COP).",
        "context": "HVAC, 중앙냉방",
        "culturalNote": "베트남의 대형 빌딩은 대부분 수랭식 칠러를 사용하며, 냉각탑과 함께 운영됩니다. 공랭식은 초기 비용이 저렴하지만 효율이 낮아 선호도가 떨어집니다. 전력 요금이 높아 VRV/VRF 시스템으로 전환하는 건물도 증가하고 있습니다. 또한 레지오넬라균 방지를 위한 냉각수 관리가 중요합니다.",
        "commonMistakes": [
            {
                "mistake": "칠러를 'máy làm lạnh nước' 직역",
                "correction": "'Chiller' 그대로 사용 (국제 표준 용어)",
                "explanation": "베트남 HVAC 업계에서는 영어 그대로 사용하며, 직역하면 오히려 혼란"
            },
            {
                "mistake": "RT(냉동톤)를 kW로 환산하지 않고 설명",
                "correction": "1RT ≈ 3.52kW 환산 기준 제시",
                "explanation": "베트남에서는 kW 단위가 더 일반적이므로 환산 필요"
            },
            {
                "mistake": "공랭식과 수랭식을 'có gió'와 'có nước'로 단순화",
                "correction": "'Air-cooled chiller'와 'Water-cooled chiller'",
                "explanation": "기술 용어는 영어 그대로 사용하는 것이 표준"
            }
        ],
        "examples": [
            {
                "ko": "이 건물은 500RT 수랭식 칠러 2대를 사용합니다.",
                "vi": "Tòa nhà này sử dụng 2 chiller water-cooled 500RT (khoảng 1760kW).",
                "situation": "formal"
            },
            {
                "ko": "칠러 효율이 떨어져서 냉각수 온도를 확인하세요.",
                "vi": "Chiller hoạt động kém hiệu quả, hãy kiểm tra nhiệt độ nước làm mát.",
                "situation": "onsite"
            },
            {
                "ko": "냉각탑 청소 후 칠러 COP가 15% 향상되었습니다.",
                "vi": "Sau khi vệ sinh cooling tower, COP của chiller tăng 15%.",
                "situation": "formal"
            }
        ],
        "relatedTerms": ["냉각탑", "펌프", "AHU", "FCU", "냉수"]
    },
    {
        "slug": "boiler",
        "korean": "보일러",
        "vietnamese": "Boiler",
        "hanja": None,
        "hanjaReading": None,
        "pronunciation": "보일러",
        "meaningKo": "물을 가열하여 난방 또는 온수를 공급하는 설비. 통역 시 연료 종류(도시가스/LNG/경유/전기), 용량(kcal/h 또는 kW), 용도(난방 전용/온수 겸용/산업용 증기), 배기 방식(강제배기/자연배기)을 명확히 구분해야 합니다. 베트남은 난방이 거의 불필요하므로 보일러는 주로 온수 공급용이며, 호텔이나 병원, 공장에서 사용합니다.",
        "meaningVi": "Thiết bị đun nóng nước để cung cấp sưởi ấm hoặc nước nóng. Cần phân biệt loại nhiên liệu (gas, dầu, điện), công suất, mục đích sử dụng (sưởi ấm, nước nóng, hơi công nghiệp).",
        "context": "HVAC, 난방",
        "culturalNote": "베트남은 열대 기후라 난방용 보일러는 거의 사용하지 않습니다. 다만 호텔, 병원, 스파에서 온수 공급용으로 사용하며, 북부 산간 지역 일부에서만 겨울철 난방이 필요합니다. 한국식 바닥난방(sàn nóng)은 매우 생소하며, 설치 시 시공 방법과 에너지 비용을 충분히 설명해야 합니다.",
        "commonMistakes": [
            {
                "mistake": "보일러를 'lò đun nước' 직역",
                "correction": "'Boiler' 그대로 사용 (국제 표준)",
                "explanation": "HVAC 업계에서는 영어 그대로 사용하며, 직역하면 단순 온수기로 오해 가능"
            },
            {
                "mistake": "난방용과 온수용을 구분하지 않음",
                "correction": "'boiler sưởi ấm'과 'boiler nước nóng' 명확히 구분",
                "explanation": "용도가 다르면 용량과 설치 방식이 완전히 다름"
            },
            {
                "mistake": "배기 가스를 '연기'로만 표현",
                "correction": "'khí thải' (배기가스) 사용",
                "explanation": "안전 규정과 관련된 기술 용어이므로 정확한 표현 필요"
            }
        ],
        "examples": [
            {
                "ko": "이 호텔은 500L 용량 전기 보일러를 사용합니다.",
                "vi": "Khách sạn này sử dụng boiler điện dung tích 500L.",
                "situation": "formal"
            },
            {
                "ko": "보일러 압력이 낮아서 순환펌프를 점검하세요.",
                "vi": "Áp lực boiler thấp, hãy kiểm tra bơm tuần hoàn.",
                "situation": "onsite"
            },
            {
                "ko": "바닥난방은 보일러에서 온수를 공급받습니다.",
                "vi": "Hệ thống sàn nóng nhận nước nóng từ boiler.",
                "situation": "formal"
            }
        ],
        "relatedTerms": ["바닥난방", "순환펌프", "온수", "배관", "방열기"]
    },
    {
        "slug": "fcu",
        "korean": "팬코일유닛",
        "vietnamese": "FCU (Fan Coil Unit)",
        "hanja": None,
        "hanjaReading": None,
        "pronunciation": "팬코일유닛",
        "meaningKo": "칠러나 보일러에서 공급되는 냉온수를 이용해 실내 공기를 냉난방하는 장치. 통역 시 주의할 점은 설치 방식(천장형/벽걸이형/노출형), 풍량(CMH), 냉난방 용량(kW), 제어 방식(On-Off/PID), 결로 방지 대책을 명확히 해야 합니다. AHU와 달리 외기 공급 기능이 없으며, 주로 객실이나 사무실 개별 공조용으로 사용됩니다.",
        "meaningVi": "Thiết bị điều hòa không khí trong phòng bằng cách sử dụng nước lạnh/nóng từ chiller hoặc boiler. Cần phân biệt phương thức lắp đặt (âm trần, treo tường, lộ ống), lưu lượng gió (CMH), công suất làm lạnh/sưởi (kW).",
        "context": "HVAC, 중앙냉난방",
        "culturalNote": "베트남의 호텔, 오피스에서는 FCU가 매우 일반적입니다. 한국처럼 천장 내부에 은폐하는 경우도 있지만, 비용 절감을 위해 노출형으로 설치하는 경우도 많습니다. 습도가 높아 결로가 자주 발생하므로, 응축수 배수 처리와 단열이 중요합니다. 소음 문제로 인해 객실에서는 저소음 모델을 선호합니다.",
        "commonMistakes": [
            {
                "mistake": "FCU를 '에어컨'으로 통역",
                "correction": "'FCU' 또는 'Fan Coil Unit' 그대로 사용",
                "explanation": "FCU는 중앙 냉난방 시스템의 일부이며, 일반 에어컨과 구조가 다름"
            },
            {
                "mistake": "AHU와 FCU를 혼동",
                "correction": "FCU는 개별 공조, AHU는 중앙 공조",
                "explanation": "AHU는 외기 처리 + 대용량, FCU는 실내 순환만"
            },
            {
                "mistake": "'팬'을 'quạt'(선풍기)으로 오역",
                "correction": "'Fan' 그대로 사용",
                "explanation": "HVAC 용어에서 Fan은 송풍기를 의미하며, 선풍기(quạt)와 다름"
            }
        ],
        "examples": [
            {
                "ko": "각 객실에 2.5kW 천장형 FCU를 설치합니다.",
                "vi": "Mỗi phòng sẽ lắp FCU âm trần 2.5kW.",
                "situation": "formal"
            },
            {
                "ko": "FCU에서 물이 새는데, 응축수 배관을 확인하세요.",
                "vi": "FCU bị chảy nước, hãy kiểm tra ống thoát nước ngưng.",
                "situation": "onsite"
            },
            {
                "ko": "풍량을 3단으로 조절할 수 있는 FCU입니다.",
                "vi": "FCU này có thể điều chỉnh lưu lượng gió 3 cấp độ.",
                "situation": "formal"
            }
        ],
        "relatedTerms": ["AHU", "칠러", "냉수", "온수", "덕트"]
    },
    {
        "slug": "ahu",
        "korean": "공조기",
        "vietnamese": "AHU (Air Handling Unit)",
        "hanja": "空調機",
        "hanjaReading": "空(빌 공) + 調(고를 조) + 機(틀 기)",
        "pronunciation": "공조기",
        "meaningKo": "외기를 냉난방, 여과, 제습하여 실내로 공급하는 대형 공조 설비. 통역 시 주의할 점은 풍량(CMH), 냉난방 코일, 필터 등급(HEPA/중성능), 열회수 여부, 가습기 유무, 소음(dB)을 명확히 설명해야 합니다. FCU와 달리 외기 처리가 가능하며, 대형 건물의 중앙 공조 시스템에서 핵심 장비입니다.",
        "meaningVi": "Thiết bị xử lý không khí ngoài trời (lọc, làm lạnh/nóng, khử ẩm) rồi cung cấp vào trong phòng. Cần nêu rõ lưu lượng gió (CMH), coil lạnh/nóng, cấp lọc (HEPA, trung bình), thu hồi nhiệt, độ ồn (dB).",
        "context": "HVAC, 중앙공조",
        "culturalNote": "베트남의 고급 오피스, 병원, 쇼핑몰에서는 AHU가 필수입니다. 외기 도입 시 미세먼지와 습도 제어가 중요하며, 특히 하노이는 겨울철 미세먼지가 심해 HEPA 필터 수요가 높습니다. 열회수 장치(ERV)는 에너지 절감 효과가 크지만 초기 비용이 높아 선택적으로 적용됩니다.",
        "commonMistakes": [
            {
                "mistake": "AHU를 '환기장치'로만 번역",
                "correction": "'AHU' 또는 'Air Handling Unit' 사용",
                "explanation": "AHU는 냉난방 + 환기 + 여과를 모두 수행하므로 환기만으로는 부족"
            },
            {
                "mistake": "CMH를 m³/h로 설명하지 않음",
                "correction": "CMH = m³/h (시간당 입방미터)",
                "explanation": "단위를 명확히 해야 풍량 개념 전달 가능"
            },
            {
                "mistake": "필터를 '거름망'으로 직역",
                "correction": "'Filter' 또는 'Bộ lọc' 사용",
                "explanation": "HVAC 업계 표준 용어 사용 필요"
            }
        ],
        "examples": [
            {
                "ko": "이 AHU는 10,000CMH 풍량에 HEPA 필터가 장착되어 있습니다.",
                "vi": "AHU này có lưu lượng gió 10,000CMH và trang bị bộ lọc HEPA.",
                "situation": "formal"
            },
            {
                "ko": "외기 온도가 높아서 AHU 냉방 부하가 증가했습니다.",
                "vi": "Nhiệt độ không khí ngoài cao nên tải làm lạnh của AHU tăng.",
                "situation": "formal"
            },
            {
                "ko": "AHU 필터를 3개월마다 교체하세요.",
                "vi": "Hãy thay bộ lọc AHU mỗi 3 tháng.",
                "situation": "onsite"
            }
        ],
        "relatedTerms": ["FCU", "덕트", "칠러", "외기", "필터"]
    },
    {
        "slug": "vav",
        "korean": "가변풍량장치",
        "vietnamese": "VAV (Variable Air Volume)",
        "hanja": "可變風量裝置",
        "hanjaReading": "可(옳을 가) + 變(변할 변) + 風(바람 풍) + 量(헤아릴 량) + 裝(꾸밀 장) + 置(둘 치)",
        "pronunciation": "가변풍량장치",
        "meaningKo": "실내 부하에 따라 공급 풍량을 자동 조절하는 장치. 통역 시 주의할 점은 제어 방식(압력 독립형/비독립형), 댐퍼 타입(평행/대향), 재열 코일 유무, 최소 풍량 설정, 소음(NC 값)을 명확히 해야 합니다. CAV(정풍량)와 달리 에너지 절감 효과가 크지만 초기 비용과 유지보수 난이도가 높습니다.",
        "meaningVi": "Thiết bị tự động điều chỉnh lưu lượng gió cung cấp theo tải phòng. Cần nêu rõ phương thức điều khiển, loại damper, có coil gia nhiệt không, lưu lượng tối thiểu, độ ồn (NC).",
        "context": "HVAC, 에너지절감",
        "culturalNote": "베트남에서는 VAV 시스템이 아직 보편화되지 않았으며, 초기 비용 부담으로 인해 고급 빌딩에서만 사용됩니다. 대부분 CAV(정풍량) 시스템을 선호하지만, 최근 에너지 절감 규제가 강화되면서 VAV 수요가 증가하고 있습니다. 설치 시 댐퍼 제어 정확성과 덕트 압력 균형이 중요합니다.",
        "commonMistakes": [
            {
                "mistake": "VAV를 '바브'로 발음",
                "correction": "'브이에이브이' 또는 'Variable Air Volume'",
                "explanation": "영어 약자를 그대로 읽어야 하며, 한국식 발음은 혼란 초래"
            },
            {
                "mistake": "CAV와 VAV를 '정풍량'과 '변풍량'으로만 설명",
                "correction": "제어 방식과 에너지 효율 차이까지 설명",
                "explanation": "단순 명칭만으로는 기술적 차이 전달 불가"
            },
            {
                "mistake": "댐퍼를 '차단기'로 오역",
                "correction": "'Damper' 또는 'Van gió' 사용",
                "explanation": "댐퍼는 풍량 조절, 차단기는 전기 차단이므로 완전히 다름"
            }
        ],
        "examples": [
            {
                "ko": "각 존마다 VAV 박스를 설치하여 독립 제어합니다.",
                "vi": "Mỗi zone sẽ lắp VAV box để điều khiển độc lập.",
                "situation": "formal"
            },
            {
                "ko": "VAV 댐퍼가 열리지 않아서 풍량이 부족합니다.",
                "vi": "Damper của VAV không mở nên lưu lượng gió thiếu.",
                "situation": "onsite"
            },
            {
                "ko": "VAV 시스템으로 전환하면 에너지를 30% 절감할 수 있습니다.",
                "vi": "Nếu chuyển sang hệ thống VAV có thể tiết kiệm 30% năng lượng.",
                "situation": "formal"
            }
        ],
        "relatedTerms": ["CAV", "댐퍼", "덕트", "AHU", "존제어"]
    },
    {
        "slug": "duong-ong-gas-lanh",
        "korean": "냉매배관",
        "vietnamese": "Đường ống gas lạnh",
        "hanja": "冷媒配管",
        "hanjaReading": "冷(찰 냉) + 媒(매개할 매) + 配(나눌 배) + 管(대롱 관)",
        "pronunciation": "뚜엉 옹 갓 라잉",
        "meaningKo": "에어컨의 실내기와 실외기를 연결하여 냉매를 순환시키는 배관. 통역 시 주의할 점은 배관 재질(동관), 굵기(인치 또는 mm), 단열재 두께, 냉매 종류(R32/R410A), 최대 연결 길이, 기밀 시험 압력을 명확히 해야 합니다. 배관 길이가 길어지면 냉방 효율이 떨어지므로 제한 거리를 반드시 확인하세요.",
        "meaningVi": "Đường ống kết nối dàn lạnh và dàn nóng để tuần hoàn gas lạnh. Cần nêu rõ chất liệu (đồng), đường kính (inch hoặc mm), độ dày cách nhiệt, loại gas (R32/R410A), chiều dài tối đa, áp suất thử kín khí.",
        "context": "HVAC, 에어컨",
        "culturalNote": "베트남에서는 냉매 배관을 'ống đồng' (동관)이라고도 부르며, 시공 품질이 냉방 성능에 직접 영향을 미칩니다. 습도가 높아 단열이 부실하면 결로가 심하게 발생하므로, 단열재 두께와 밀착도가 매우 중요합니다. 불법 냉매 충전 업체가 많아 정품 냉매 사용 여부 확인이 필수입니다.",
        "commonMistakes": [
            {
                "mistake": "냉매를 '가스'로만 표현",
                "correction": "'Gas lạnh' 또는 냉매 종류 명시 (R32, R410A)",
                "explanation": "냉매 종류에 따라 압력과 효율이 다르므로 정확한 명칭 필요"
            },
            {
                "mistake": "배관 굵기를 '크기'로만 설명",
                "correction": "인치 또는 mm 단위로 명시",
                "explanation": "냉매 배관은 정확한 치수가 중요하며, 모호한 표현은 시공 오류 유발"
            },
            {
                "mistake": "단열재를 '보온재'로 통일",
                "correction": "냉매 배관은 '보냉재' (cách nhiệt)",
                "explanation": "보온(giữ ấm)과 보냉(giữ lạnh)은 용도가 정반대"
            }
        ],
        "examples": [
            {
                "ko": "실내외기 거리가 25m이므로 3/8인치와 5/8인치 동관을 사용합니다.",
                "vi": "Khoảng cách giữa dàn lạnh và dàn nóng là 25m nên dùng ống đồng 3/8 inch và 5/8 inch.",
                "situation": "onsite"
            },
            {
                "ko": "냉매 배관 용접 후 질소로 기밀 시험하세요.",
                "vi": "Sau khi hàn ống gas, hãy thử kín bằng khí nitơ.",
                "situation": "onsite"
            },
            {
                "ko": "단열재가 벗겨져서 배관에 물방울이 맺혔습니다.",
                "vi": "Cách nhiệt bị bong ra nên ống bị đọng nước.",
                "situation": "onsite"
            }
        ],
        "relatedTerms": ["냉매", "동관", "단열재", "실외기", "진공작업"]
    },
    {
        "slug": "bo-toa-nhiet",
        "korean": "방열기",
        "vietnamese": "Bộ tỏa nhiệt",
        "hanja": "放熱器",
        "hanjaReading": "放(놓을 방) + 熱(더울 열) + 器(그릇 기)",
        "pronunciation": "보 토아 니엣",
        "meaningKo": "보일러에서 공급되는 온수를 이용해 실내를 난방하는 장치. 통역 시 주의할 점은 재질(주철/알루미늄/강철), 방열량(kcal/h), 설치 위치(벽면/바닥), 밸브 종류(온도조절/차단), 배관 방식(단관/복관)을 명확히 해야 합니다. 베트남에서는 거의 사용하지 않으므로 한국 난방 문화를 충분히 설명해야 합니다.",
        "meaningVi": "Thiết bị sưởi ấm phòng bằng nước nóng từ boiler. Cần nêu rõ chất liệu (gang, nhôm, thép), công suất tỏa nhiệt (kcal/h), vị trí lắp (tường, sàn), loại van, phương thức đấu ống.",
        "context": "HVAC, 난방",
        "culturalNote": "베트남은 난방이 불필요하므로 방열기는 거의 사용하지 않습니다. 북부 산간 지역 고급 리조트나 한국인 거주 주택에서만 간혹 볼 수 있습니다. 베트남인들은 난방 개념이 생소하므로, 통역 시 '겨울철 실내를 따뜻하게 하는 장치'라는 기본 설명부터 시작해야 합니다.",
        "commonMistakes": [
            {
                "mistake": "방열기를 'tản nhiệt'로 번역",
                "correction": "'Bộ tỏa nhiệt' 또는 'Radiator'",
                "explanation": "Tản nhiệt는 컴퓨터 쿨러 등 '냉각' 의미, 난방용은 'Tỏa nhiệt'"
            },
            {
                "mistake": "온수를 'nước ấm'(따뜻한 물)으로 표현",
                "correction": "'Nước nóng' (뜨거운 물) 사용",
                "explanation": "난방용 온수는 60~80도로 매우 뜨거우므로 '따뜻한' 정도가 아님"
            },
            {
                "mistake": "방열기를 '히터'로 통칭",
                "correction": "전기 히터와 구분 ('máy sưởi điện'은 전기 히터)",
                "explanation": "방열기는 온수 순환 방식, 전기 히터는 전기 직접 발열"
            }
        ],
        "examples": [
            {
                "ko": "각 방마다 알루미늄 방열기를 설치합니다.",
                "vi": "Mỗi phòng sẽ lắp bộ tỏa nhiệt nhôm (radiator nhôm).",
                "situation": "formal"
            },
            {
                "ko": "방열기 온도 조절 밸브가 고장났습니다.",
                "vi": "Van điều chỉnh nhiệt độ của radiator bị hỏng.",
                "situation": "onsite"
            },
            {
                "ko": "방열기에서 공기 빼기 작업을 하세요.",
                "vi": "Hãy xả khí trong radiator.",
                "situation": "onsite"
            }
        ],
        "relatedTerms": ["보일러", "바닥난방", "온수", "순환펌프", "온도조절밸브"]
    },
    {
        "slug": "san-nong",
        "korean": "바닥난방",
        "vietnamese": "Sàn nóng",
        "hanja": "床暖房",
        "hanjaReading": "床(평상 상) + 暖(따뜻할 난) + 房(방 방)",
        "pronunciation": "산 농",
        "meaningKo": "바닥에 온수 배관을 설치하여 복사열로 난방하는 방식. 통역 시 주의할 점은 배관 재질(PE-X/PB), 배관 간격, 마감재 열전도율, 온수 공급 온도, 단열재 두께, 제어 방식(실별/통합)을 명확히 해야 합니다. 한국 고유의 난방 방식이므로 베트남인에게는 충분한 설명이 필요하며, 에너지 비용과 시공 난이도가 높다는 점을 강조하세요.",
        "meaningVi": "Hệ thống sưởi ấm bằng cách lắp đặt ống nước nóng dưới sàn để tỏa nhiệt bức xạ. Cần nêu rõ chất liệu ống (PE-X, PB), khoảng cách ống, độ dẫn nhiệt vật liệu hoàn thiện, nhiệt độ nước cung cấp, độ dày cách nhiệt, phương thức điều khiển.",
        "context": "HVAC, 난방",
        "culturalNote": "바닥난방은 한국의 대표적인 난방 방식이지만, 베트남에서는 거의 알려지지 않았습니다. 베트남인들은 '바닥이 따뜻하다'는 개념 자체가 생소하며, 초기 시공비와 전기/가스 요금 부담이 크다는 점을 우려합니다. 북부 일부 고급 주택에서만 한국인 거주자를 위해 설치하는 경우가 있으며, 시공 시 습기 방지와 배관 누수 방지가 중요합니다.",
        "commonMistakes": [
            {
                "mistake": "바닥난방을 'sưởi ấm dưới sàn'로 직역",
                "correction": "'Sàn nóng' (뜨거운 바닥) 사용",
                "explanation": "현지에서 통용되는 간결한 표현 사용 필요"
            },
            {
                "mistake": "'온돌'을 'Ondol'로 음차",
                "correction": "'Sàn nóng truyền thống Hàn Quốc' (한국 전통 바닥난방)",
                "explanation": "Ondol은 베트남인에게 생소하므로 설명적 표현 필요"
            },
            {
                "mistake": "배관을 '파이프'로만 표현",
                "correction": "'Ống nước nóng' 또는 'Ống PE-X' 명시",
                "explanation": "배관 종류가 시공 방법과 내구성에 영향"
            }
        ],
        "examples": [
            {
                "ko": "이 아파트는 전체 바닥난방으로 설계되었습니다.",
                "vi": "Căn hộ này được thiết kế với hệ thống sàn nóng toàn bộ.",
                "situation": "formal"
            },
            {
                "ko": "바닥난방 배관 간격은 15cm입니다.",
                "vi": "Khoảng cách ống sàn nóng là 15cm.",
                "situation": "onsite"
            },
            {
                "ko": "바닥난방은 복사열로 난방하므로 건조하지 않습니다.",
                "vi": "Sàn nóng sưởi ấm bằng nhiệt bức xạ nên không làm khô không khí.",
                "situation": "formal"
            }
        ],
        "relatedTerms": ["보일러", "온수배관", "단열재", "온도조절기", "방열기"]
    }
]

# 파일 경로
file_path = os.path.join(
    os.path.dirname(os.path.abspath(__file__)),
    "..",
    "data",
    "terms",
    "construction.json"
)

# 기존 데이터 로드
with open(file_path, "r", encoding="utf-8") as f:
    existing_data = json.load(f)

# 새 데이터 추가
existing_data.extend(data)

# 저장
with open(file_path, "w", encoding="utf-8") as f:
    json.dump(existing_data, f, ensure_ascii=False, indent=2)

print(f"✅ {len(data)}개 용어 추가 완료")
print(f"📂 파일: {file_path}")
print(f"📊 총 용어 수: {len(existing_data)}개")
