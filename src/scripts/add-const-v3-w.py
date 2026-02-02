#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Construction Terms - Painting & Anti-corrosion (도장/방식/방청)
10 terms: 프라이머, 중도, 상도, 에폭시도료, 우레탄도료, 내화도료, 방청도료, 블라스팅, 케렌, 도막두께
Tier S quality standard
"""

import json
import os

# 추가할 용어 데이터 (Tier S 기준)
data = [
    {
        "slug": "primer-son-lot",
        "korean": "프라이머",
        "vietnamese": "Sơn lót",
        "hanja": None,
        "hanjaReading": None,
        "pronunciation": "프라이머",
        "meaningKo": "도장 시스템의 첫 번째 층으로, 소지(素地)와 상도의 부착력을 향상시키고 방청 효과를 제공하는 하도 도료입니다. 통역 시 주의할 점은 베트남에서 'sơn lót'는 일반적인 밑칠을 의미하지만, 건설 현장에서는 방청 프라이머(sơn chống gỉ), 에폭시 프라이머(sơn lót epoxy) 등 종류를 정확히 구분해야 합니다. 도장 사양서(specification)에서 프라이머의 건조시간(thời gian khô), 도막두께(độ dày màng sơn)를 명확히 확인하고 통역하세요.",
        "meaningVi": "Lớp sơn đầu tiên trong hệ thống sơn, có tác dụng tăng độ bám dính giữa bề mặt và lớp sơn phủ, đồng thời cung cấp khả năng chống gỉ sét. Trong xây dựng, phải phân biệt rõ loại sơn lót như sơn chống gỉ, sơn lót epoxy theo đúng yêu cầu kỹ thuật.",
        "context": "도장공사 시방서, 철골 방청, 콘크리트 표면처리",
        "culturalNote": "한국 건설 현장에서는 프라이머를 도장 시스템의 필수 단계로 엄격히 적용하며, KS 규격(KS M 5331)에 따라 종류와 두께를 관리합니다. 베트남에서는 비용 절감을 위해 프라이머를 생략하거나 얇게 도포하는 경우가 있어 품질 문제가 발생할 수 있습니다. 통역 시 프라이머의 중요성과 한국 기준(최소 30~50㎛)을 명확히 전달하고, 'sơn lót bắt buộc'(필수 밑칠)임을 강조해야 합니다. 또한 양국에서 사용하는 프라이머 브랜드(일본 Nippon, 한국 KCC vs 베트남 Jotun, Hempel)가 다르므로 제품 사양을 정확히 확인하세요.",
        "commonMistakes": [
            {
                "mistake": "프라이머를 '밑칠'로만 통역",
                "correction": "sơn lót (일반) 또는 sơn chống gỉ (방청용) 구분",
                "explanation": "건설 현장에서는 프라이머의 기능(방청, 부착력 향상)에 따라 정확한 베트남어 용어를 사용해야 시공 오류를 방지할 수 있습니다."
            },
            {
                "mistake": "모든 프라이머를 'sơn lót epoxy'로 통역",
                "correction": "종류에 따라 sơn lót kẽm phốt-phat (아연계), sơn lót alkyd (알키드계) 등 구분",
                "explanation": "프라이머는 화학적 성분에 따라 종류가 다양하며, 각 용도와 성능이 다르므로 정확한 명칭이 필요합니다."
            },
            {
                "mistake": "프라이머 도막두께를 '얇게'로 모호하게 통역",
                "correction": "구체적 수치 사용 (예: 30 micromet, 50 micromet)",
                "explanation": "도막두께는 품질 관리의 핵심 지표이므로 반드시 수치로 명확히 전달해야 합니다."
            },
            {
                "mistake": "프라이머 건조시간을 생략하고 통역",
                "correction": "thời gian khô bề mặt (표면건조), thời gian khô hoàn toàn (완전건조) 구분",
                "explanation": "후속 도장 공정의 적기 시공을 위해 건조시간의 정확한 전달이 필수적입니다."
            }
        ],
        "examples": [
            {
                "ko": "철골 부재에 방청 프라이머를 도막두께 50㎛로 도포하세요.",
                "vi": "Sơn lót chống gỉ lên cấu kiện thép với độ dày màng sơn 50 micromet.",
                "situation": "onsite"
            },
            {
                "ko": "프라이머의 표면 건조시간은 2시간, 재도장 간격은 24시간 이내입니다.",
                "vi": "Thời gian khô bề mặt của sơn lót là 2 giờ, thời gian tối đa trước khi sơn lớp tiếp theo là 24 giờ.",
                "situation": "formal"
            },
            {
                "ko": "에폭시 프라이머 바르기 전에 표면 케렌 작업 완료했어?",
                "vi": "Đã hoàn thành công tác làm sạch bề mặt trước khi sơn lót epoxy chưa?",
                "situation": "informal"
            }
        ],
        "relatedTerms": ["중도", "상도", "케렌", "도막두께"]
    },
    {
        "slug": "trung-do-son-phu-giua",
        "korean": "중도",
        "vietnamese": "Sơn phủ giữa",
        "hanja": "中塗",
        "hanjaReading": "中(가운데 중) + 塗(칠할 도)",
        "pronunciation": "중도",
        "meaningKo": "프라이머와 상도 사이에 도포하는 중간층 도료로, 도막 두께 확보와 평활한 표면 형성, 상도의 광택 향상을 목적으로 합니다. 통역 시 주의할 점은 베트남 현장에서 중도를 생략하거나 프라이머를 중도로 대체하려는 경우가 많아, '3도 도장 시스템'(hệ thống sơn 3 lớp)의 필수 공정임을 명확히 강조해야 합니다. 또한 중도의 색상은 보통 상도보다 약간 진하게(màu đậm hơn) 해서 도포 여부를 육안으로 확인할 수 있게 하는 것이 한국 시공 관행입니다.",
        "meaningVi": "Lớp sơn trung gian giữa sơn lót và sơn phủ, có tác dụng tăng độ dày màng sơn, tạo bề mặt phẳng mịn và cải thiện độ bóng của lớp sơn hoàn thiện. Là công đoạn bắt buộc trong hệ thống sơn 3 lớp của tiêu chuẩn Hàn Quốc.",
        "context": "도장공사 3도 시스템, 품질관리, 마감 품질 향상",
        "culturalNote": "한국 건설 현장에서는 철골 구조물과 중요 마감면에 대해 '프라이머-중도-상도' 3도 도장을 표준으로 하며, 중도 생략은 감리자 승인 없이 불가합니다. 베트남에서는 비용과 공기 단축을 위해 중도를 생략하고 2도 도장(프라이머+상도)으로 완료하려는 경우가 많습니다. 통역 시 중도가 단순한 '추가 작업'이 아니라 내구성과 미관에 필수적임을 설명하고, 계약서의 도장 시방(specification sơn)을 근거로 제시하세요. 또한 한국은 중도를 상도보다 진한 색으로 칠해 시공 상태를 확인하는 반면, 베트남은 같은 색으로 칠하는 경우가 많아 소통에 혼란이 있을 수 있습니다.",
        "commonMistakes": [
            {
                "mistake": "중도를 'sơn lót thứ hai'(두 번째 밑칠)로 통역",
                "correction": "sơn phủ giữa 또는 sơn trung gian",
                "explanation": "중도는 프라이머가 아니라 독립적인 중간층이므로 정확한 명칭을 사용해야 합니다."
            },
            {
                "mistake": "중도 생략 요청을 그대로 수용하여 통역",
                "correction": "계약 및 시방서 확인 필요성을 함께 통역",
                "explanation": "중도 생략은 품질 저하로 이어지므로 한국 감리자에게 반드시 확인이 필요함을 전달해야 합니다."
            },
            {
                "mistake": "중도와 상도를 'sơn phủ'로 혼용",
                "correction": "sơn phủ giữa (중도), sơn hoàn thiện (상도) 명확히 구분",
                "explanation": "두 층의 기능과 요구 성능이 다르므로 정확한 구분이 필요합니다."
            },
            {
                "mistake": "중도 색상 차이를 설명하지 않고 통역",
                "correction": "màu sơn phủ giữa đậm hơn một chút (중도 색상이 약간 더 진함) 명시",
                "explanation": "시공 품질 확인 방법에 대한 양국 관행 차이를 설명해야 오해를 방지할 수 있습니다."
            }
        ],
        "examples": [
            {
                "ko": "중도는 프라이머 건조 후 24시간 이내에 도포하고, 도막두께는 40㎛를 확보하십시오.",
                "vi": "Sơn phủ giữa phải được thi công trong vòng 24 giờ sau khi sơn lót khô, và đảm bảo độ dày màng sơn đạt 40 micromet.",
                "situation": "formal"
            },
            {
                "ko": "중도는 상도보다 한 톤 진하게 칠해서 나중에 구분할 수 있게 해주세요.",
                "vi": "Sơn phủ giữa nên có màu đậm hơn một chút so với sơn hoàn thiện để có thể phân biệt được sau này.",
                "situation": "onsite"
            },
            {
                "ko": "중도 생략하면 안 돼요, 시방서에 3도 도장으로 명시돼 있어요.",
                "vi": "Không được bỏ qua lớp sơn phủ giữa, trong thuyết minh kỹ thuật đã ghi rõ phải sơn 3 lớp.",
                "situation": "informal"
            }
        ],
        "relatedTerms": ["프라이머", "상도", "도막두께", "도장시방서"]
    },
    {
        "slug": "sang-do-son-hoan-thien",
        "korean": "상도",
        "vietnamese": "Sơn hoàn thiện",
        "hanja": "上塗",
        "hanjaReading": "上(위 상) + 塗(칠할 도)",
        "pronunciation": "상도",
        "meaningKo": "도장 시스템의 최종층으로, 미관을 형성하고 외부 환경(자외선, 빗물, 오염물질)으로부터 보호하는 마감 도료입니다. 통역 시 주의할 점은 베트남에서 'sơn hoàn thiện'는 '완성 도료'라는 의미로 단독 사용될 수 있어, 반드시 '하도(sơn lót)와 중도(sơn phủ giữa) 위에 칠하는 최종층'임을 명확히 해야 합니다. 상도의 광택도(độ bóng: 유광 bóng, 반광 bán bóng, 무광 mờ)와 색상(màu sắc)은 발주자 승인사항이므로 시공 전 반드시 샘플 확인(kiểm tra mẫu)이 필요합니다.",
        "meaningVi": "Lớp sơn cuối cùng trong hệ thống sơn, có tác dụng tạo thẩm mỹ và bảo vệ bề mặt khỏi tác động của môi trường bên ngoài như tia UV, mưa, và các chất ô nhiễm. Độ bóng và màu sắc của sơn hoàn thiện cần được chủ đầu tư phê duyệt.",
        "context": "건축 마감, 외벽 도장, 철골 구조물 최종 마감",
        "culturalNote": "한국 건설 현장에서 상도는 단순한 마감이 아니라 '건물의 얼굴'로 여겨져 색상과 광택도를 발주자와 여러 차례 협의하며, 대형 프로젝트에서는 Mock-up(모형 시공)을 통해 사전 검증합니다. 베트남에서는 상도를 빠르게 마무리하려는 경향이 있어 하도 건조 시간을 충분히 확보하지 않고 시공하여 품질 문제(벗겨짐, 색 불균일)가 발생할 수 있습니다. 통역 시 상도 시공의 조건(온도 10~30℃, 습도 85% 이하, 바람 없음)과 건조시간(24~48시간)을 명확히 전달하고, 한국 품질 기준의 엄격함을 설명해야 합니다. 또한 한국은 내후성(độ bền thời tiết)을 중시하여 우레탄, 불소 수지 상도를 선호하는 반면, 베트남은 아크릴 상도를 많이 사용하여 내구성 차이가 있을 수 있습니다.",
        "commonMistakes": [
            {
                "mistake": "상도를 'sơn cuối'로 직역",
                "correction": "sơn hoàn thiện 또는 sơn phủ ngoài",
                "explanation": "'sơn cuối'는 구어체이며, 공식 문서와 현장에서는 'sơn hoàn thiện'가 표준 용어입니다."
            },
            {
                "mistake": "광택도를 설명 없이 '유광', '무광'으로만 통역",
                "correction": "bóng (유광), bán bóng (반광), mờ (무광) + 구체적 gloss 수치 (예: 80% bóng)",
                "explanation": "광택도는 시각적 평가가 주관적일 수 있으므로 수치 기준을 함께 제시해야 합니다."
            },
            {
                "mistake": "상도 시공 조건을 생략하고 통역",
                "correction": "nhiệt độ 10~30℃, độ ẩm dưới 85%, không có gió mạnh (온도, 습도, 바람 조건) 명시",
                "explanation": "시공 조건 미준수 시 품질 결함이 발생하므로 반드시 조건을 전달해야 합니다."
            },
            {
                "mistake": "상도 색상을 구두로만 전달",
                "correction": "색상 코드(mã màu, color code)와 샘플 확인 요구",
                "explanation": "색상은 말로 표현하기 어렵고 오해 소지가 크므로 반드시 샘플과 코드를 기준으로 해야 합니다."
            }
        ],
        "examples": [
            {
                "ko": "상도는 중도 완전 건조 후 48시간 이내에 도포하며, 색상은 KCC Color System NCS S 5020-B70G를 사용하십시오.",
                "vi": "Sơn hoàn thiện phải được thi công trong vòng 48 giờ sau khi sơn phủ giữa khô hoàn toàn, sử dụng màu theo hệ thống KCC Color System NCS S 5020-B70G.",
                "situation": "formal"
            },
            {
                "ko": "상도 광택은 무광으로 하고, 두께는 50마이크로미터 이상 확보해 주세요.",
                "vi": "Sơn hoàn thiện dạng mờ, độ dày màng sơn phải đạt tối thiểu 50 micromet.",
                "situation": "onsite"
            },
            {
                "ko": "상도 칠하기 전에 먼지 완전히 제거하고, 날씨 좋을 때 하세요.",
                "vi": "Trước khi sơn hoàn thiện, phải loại bỏ hoàn toàn bụi bẩn và thi công khi thời tiết tốt.",
                "situation": "informal"
            }
        ],
        "relatedTerms": ["프라이머", "중도", "광택도", "내후성"]
    },
    {
        "slug": "epoxy-do-ryo-son-epoxy",
        "korean": "에폭시도료",
        "vietnamese": "Sơn epoxy",
        "hanja": None,
        "hanjaReading": None,
        "pronunciation": "에폭시도료",
        "meaningKo": "에폭시 수지(epoxy resin)를 주성분으로 하는 2액형 도료로, 우수한 부착력, 내약품성, 내마모성을 가져 공장 바닥, 수조, 화학시설 등에 사용됩니다. 통역 시 주의할 점은 에폭시도료가 반드시 '경화제(chất đóng rắn, hardener)'와 혼합해야 하며, 혼합 비율(tỉ lệ trộn: 보통 주제 2 : 경화제 1)과 가사시간(pot life: thời gian sử dụng sau khi trộn, 보통 30분~2시간)을 정확히 전달해야 시공 오류를 방지할 수 있습니다. 또한 에폭시는 자외선에 약해 황변(пhỉ vàng)되므로 외부 노출 부위에는 우레탄 상도를 덧칠해야 합니다.",
        "meaningVi": "Loại sơn hai thành phần có thành phần chính là nhựa epoxy, có độ bám dính tốt, chống hóa chất và chống mài mòn xuất sắc, được sử dụng cho sàn nhà xưởng, bể chứa, và các công trình hóa chất. Phải trộn với chất đóng rắn theo đúng tỉ lệ và sử dụng trong thời gian quy định.",
        "context": "공장 바닥 도장, 방수 도장, 내약품 시설, 주차장 바닥",
        "culturalNote": "한국 건설 현장에서 에폭시도료는 공장과 주차장 바닥의 표준 마감재로, KS M 5316 규격을 준수하며 두께(보통 2~3mm)와 압축강도를 엄격히 관리합니다. 베트남에서도 에폭시 바닥재가 널리 사용되지만, 저가 제품 사용으로 인한 품질 문제(갈라짐, 벗겨짐)가 빈번합니다. 통역 시 한국산 또는 일본산 고품질 에폭시(Jotun, Hempel, KCC)와 베트남 로컬 제품의 차이를 설명하고, 시방서에 명시된 제품을 사용하도록 강조해야 합니다. 또한 에폭시 시공은 온도(25℃ 전후)와 습도(60% 전후)에 민감하므로 베트남의 고온다습한 환경에서는 경화 시간 조정이 필요함을 설명하세요.",
        "commonMistakes": [
            {
                "mistake": "에폭시를 '방수 페인트'로만 통역",
                "correction": "sơn epoxy chống thấm, chống hóa chất (방수 및 내약품성 에폭시)",
                "explanation": "에폭시는 방수뿐 아니라 내약품, 내마모 기능이 주요 특성이므로 용도에 맞게 정확히 표현해야 합니다."
            },
            {
                "mistake": "혼합 비율과 가사시간 설명 생략",
                "correction": "tỉ lệ trộn (혼합비율), thời gian sử dụng sau khi trộn (가사시간) 명확히 통역",
                "explanation": "2액형 도료는 정확한 혼합과 시간 내 사용이 필수이므로 이를 생략하면 시공 실패로 이어집니다."
            },
            {
                "mistake": "에폭시의 황변 현상을 설명하지 않음",
                "correction": "sơn epoxy bị vàng khi phơi nắng (자외선 노출 시 황변) + 해결책(우레탄 상도) 제시",
                "explanation": "외부 사용 시 황변 문제를 미리 알리지 않으면 추후 클레임이 발생할 수 있습니다."
            },
            {
                "mistake": "에폭시 바닥 두께를 도막두께(㎛)로 표현",
                "correction": "바닥재는 mm 단위 사용 (예: 2mm, 3mm)",
                "explanation": "도료는 ㎛(마이크로미터), 바닥재는 mm(밀리미터) 단위를 사용하여 혼동을 방지해야 합니다."
            }
        ],
        "examples": [
            {
                "ko": "공장 바닥에 에폭시도료를 2mm 두께로 시공하고, 주제와 경화제를 2:1 비율로 혼합하십시오.",
                "vi": "Thi công sơn epoxy cho sàn nhà xưởng với độ dày 2mm, trộn chất gốc và chất đóng rắn theo tỉ lệ 2:1.",
                "situation": "formal"
            },
            {
                "ko": "에폭시 혼합 후 1시간 안에 다 써야 해요, 그 뒤엔 굳어서 못 써요.",
                "vi": "Sau khi trộn sơn epoxy, phải sử dụng hết trong vòng 1 giờ, sau đó sẽ đông cứng và không dùng được nữa.",
                "situation": "informal"
            },
            {
                "ko": "외부 계단에는 에폭시 위에 우레탄 상도를 칠해서 햇빛에 안 누래지게 하세요.",
                "vi": "Đối với cầu thang ngoài trời, sơn lớp phủ polyurethane lên trên sơn epoxy để tránh bị vàng do ánh nắng.",
                "situation": "onsite"
            }
        ],
        "relatedTerms": ["우레탄도료", "2액형도료", "방수도료", "바닥마감"]
    },
    {
        "slug": "uretan-do-ryo-son-polyurethane",
        "korean": "우레탄도료",
        "vietnamese": "Sơn polyurethane",
        "hanja": None,
        "hanjaReading": None,
        "pronunciation": "우레탄도료",
        "meaningKo": "폴리우레탄 수지를 주성분으로 하는 도료로, 우수한 내후성, 광택 유지성, 내마모성을 가져 외부 철골 구조물, 차량, 기계 등의 최종 마감에 사용됩니다. 통역 시 주의할 점은 우레탄도료도 2액형(주제+경화제)이 일반적이지만, 1액형 습기 경화형(moisture-cure)도 있어 제품 타입을 명확히 구분해야 합니다. 우레탄은 에폭시와 달리 자외선에 강해 외부용으로 적합하지만, 가격이 비싸므로 시방서에서 우레탄 지정 여부를 반드시 확인하고 통역하세요. 또한 우레탄 도료는 이소시아네이트(isocyanate) 성분으로 인해 호흡기 자극이 있으므로 안전 장비(mặt nạ phòng độc, 방독면) 착용을 강조해야 합니다.",
        "meaningVi": "Loại sơn có thành phần chính là nhựa polyurethane, có khả năng chống chịu thời tiết, giữ độ bóng và chống mài mòn tốt, được sử dụng cho lớp hoàn thiện của kết cấu thép ngoài trời, xe cộ, máy móc. Có thể là loại hai thành phần hoặc một thành phần đóng rắng bằng độ ẩm.",
        "context": "외부 철골 마감, 교량 도장, 차량 도장, 목재 마감",
        "culturalNote": "한국 건설 현장에서 우레탄도료는 교량, 철탑, 고층 건물 외벽 철골 등 내구성이 중요한 부위의 최종 마감재로 선호되며, KS M 5314 규격을 준수합니다. 베트남에서는 우레탄의 높은 가격 때문에 아크릴이나 알키드로 대체하려는 경우가 많아, 통역 시 계약서와 시방서에 명시된 도료 종류를 근거로 제시해야 합니다. 또한 우레탄 도료의 시공 조건(온도 10~30℃, 습도 85% 이하)이 에폭시보다 까다로우며, 베트남의 우기(mùa mưa)에는 습도 관리가 어려워 품질 저하가 발생할 수 있음을 설명하세요. 우레탄 도료는 한국과 베트남 모두에서 Jotun, Hempel, International Paint 같은 글로벌 브랜드를 사용하므로 제품 데이터시트(technical data sheet, TDS)를 기준으로 소통하세요.",
        "commonMistakes": [
            {
                "mistake": "우레탄을 'sơn dầu'(유성도료)로 통역",
                "correction": "sơn polyurethane (PU)",
                "explanation": "우레탄은 특정 화학 구조의 수지이므로 일반적인 '유성도료'와는 다릅니다."
            },
            {
                "mistake": "우레탄과 에폭시를 혼용하여 통역",
                "correction": "epoxy (내약품, 실내용), polyurethane (내후성, 외부용) 구분",
                "explanation": "두 도료는 용도와 특성이 다르므로 명확한 구분이 필요합니다."
            },
            {
                "mistake": "우레탄 시공 시 안전 장비 요구사항 생략",
                "correction": "mặt nạ phòng độc, găng tay, quần áo bảo hộ (방독면, 장갑, 보호복) 필수 명시",
                "explanation": "이소시아네이트는 건강에 유해하므로 안전 수칙을 반드시 전달해야 합니다."
            },
            {
                "mistake": "우레탄 가격이 비싸다는 이유로 임의로 대체재 제안",
                "correction": "시방서 준수 필요성 강조, 대체 시 감리자 승인 필요 통역",
                "explanation": "도료 변경은 내구성과 보증에 영향을 미치므로 반드시 공식 절차를 거쳐야 합니다."
            }
        ],
        "examples": [
            {
                "ko": "교량 외부 철골에 우레탄도료 2액형을 상도로 사용하며, 건조 후 광택도는 80% 이상이어야 합니다.",
                "vi": "Sử dụng sơn polyurethane hai thành phần làm lớp hoàn thiện cho kết cấu thép ngoài trời của cầu, độ bóng sau khi khô phải đạt trên 80%.",
                "situation": "formal"
            },
            {
                "ko": "우레탄 칠할 때 꼭 방독면 쓰세요, 냄새 맡으면 머리 아파요.",
                "vi": "Khi sơn polyurethane nhất định phải đeo mặt nạ phòng độc, hít phải sẽ bị đau đầu.",
                "situation": "informal"
            },
            {
                "ko": "우레탄이 비싸긴 한데, 10년 보증하려면 이거 써야 해요.",
                "vi": "Sơn polyurethane tuy đắt nhưng để bảo hành 10 năm thì phải dùng loại này.",
                "situation": "onsite"
            }
        ],
        "relatedTerms": ["에폭시도료", "내후성", "2액형도료", "교량도장"]
    },
    {
        "slug": "nae-hwa-do-ryo-son-chong-chay",
        "korean": "내화도료",
        "vietnamese": "Sơn chống cháy",
        "hanja": "耐火塗料",
        "hanjaReading": "耐(견딜 내) + 火(불 화) + 塗(칠할 도) + 料(재료 료)",
        "pronunciation": "내화도료",
        "meaningKo": "고온에 노출될 때 발포(팽창)하여 단열층을 형성하고 철골의 온도 상승을 지연시켜 화재 시 건축물의 붕괴를 방지하는 도료입니다. 통역 시 주의할 점은 내화도료의 성능은 '내화시간'(thời gian chống cháy: 1시간, 2시간, 3시간 등)으로 표시되며, 이는 법적 요구사항(Building Code)이므로 임의로 생략하거나 변경할 수 없음을 강조해야 합니다. 또한 내화도료의 두께는 요구 내화시간에 따라 다르므로(예: 1시간 내화 시 2mm, 3시간 내화 시 5mm) 시방서의 두께를 정확히 확인하고 통역하세요.",
        "meaningVi": "Loại sơn khi tiếp xúc với nhiệt độ cao sẽ nở lên tạo thành lớp cách nhiệt, làm chậm sự gia tăng nhiệt độ của kết cấu thép, ngăn ngừa sự sụp đổ của công trình khi có hỏa hoạn. Hiệu suất được biểu thị bằng thời gian chống cháy (1 giờ, 2 giờ, 3 giờ) theo quy định pháp luật.",
        "context": "철골 구조물 내화 피복, 고층 건물, 소방 법규 준수",
        "culturalNote": "한국에서는 「건축법」과 「소방법」에 따라 일정 규모 이상의 건축물(4층 이상 또는 연면적 2,000㎡ 이상)은 철골에 의무적으로 내화 피복을 해야 하며, 내화도료는 뿜칠 내화재(SFRM)의 대안으로 많이 사용됩니다. 베트남에서도 고층 건물에 내화 규정이 있지만 단속이 느슨하여 생략되는 경우가 있습니다. 통역 시 한국 법규의 엄격함과 소방 검사(kiểm tra PCCC)에서 반드시 확인된다는 점을 강조하세요. 내화도료는 시공 후 두께 측정(đo độ dày)과 성능 시험 성적서(giấy chứng nhận thử nghiệm) 제출이 필수이므로, 이를 사전에 협력업체에 전달해야 합니다. 또한 내화도료는 가격이 일반 도료보다 3~5배 비싸므로 예산 논의 시 별도 비용임을 명확히 하세요.",
        "commonMistakes": [
            {
                "mistake": "내화도료를 '방화 페인트'로만 통역",
                "correction": "sơn chống cháy (내화) hoặc sơn chống lan lửa (방화) 구분",
                "explanation": "내화(耐火)는 불을 견딤, 방화(防火)는 불이 번지는 것을 막음으로 개념이 다릅니다."
            },
            {
                "mistake": "내화시간을 'thời gian khô'(건조시간)로 오역",
                "correction": "thời gian chống cháy (내화시간) hoặc mức chịu lửa (내화등급)",
                "explanation": "내화시간은 화재 시 견딜 수 있는 시간이지 건조 시간이 아닙니다."
            },
            {
                "mistake": "내화도료 두께를 일반 도막두께와 혼동",
                "correction": "내화도료는 mm 단위(2~5mm), 일반 도료는 ㎛ 단위 구분",
                "explanation": "내화도료는 훨씬 두껍게 시공되므로 단위 혼동 시 시공 오류가 발생합니다."
            },
            {
                "mistake": "내화도료 성능 시험 성적서 요구를 생략",
                "correction": "giấy chứng nhận thử nghiệm chống cháy (내화 시험 성적서) 필수 제출 명시",
                "explanation": "법규 준수와 준공 검사를 위해 반드시 필요한 서류입니다."
            }
        ],
        "examples": [
            {
                "ko": "이 건물은 3시간 내화 등급이므로, 철골 기둥에 내화도료를 5mm 두께로 도포하십시오.",
                "vi": "Tòa nhà này có mức chịu lửa 3 giờ, do đó phải sơn chống cháy lên cột thép với độ dày 5mm.",
                "situation": "formal"
            },
            {
                "ko": "내화도료 칠한 부분은 소방 검사 때 두께 측정하니까 정확하게 시공하세요.",
                "vi": "Phần sơn chống cháy sẽ được đo độ dày khi kiểm tra phòng cháy chữa cháy, nên phải thi công chính xác.",
                "situation": "onsite"
            },
            {
                "ko": "내화도료 비용은 일반 페인트보다 훨씬 비싸요, 예산 따로 잡아야 돼요.",
                "vi": "Chi phí sơn chống cháy đắt hơn nhiều so với sơn thường, phải dự trù ngân sách riêng.",
                "situation": "informal"
            }
        ],
        "relatedTerms": ["내화피복", "뿜칠내화재", "소방검사", "철골구조"]
    },
    {
        "slug": "bang-cheong-do-ryo-son-chong-gi",
        "korean": "방청도료",
        "vietnamese": "Sơn chống gỉ",
        "hanja": "防銹塗料",
        "hanjaReading": "防(막을 방) + 銹(녹 청) + 塗(칠할 도) + 料(재료 료)",
        "pronunciation": "방청도료",
        "meaningKo": "철강 재료의 부식(녹)을 방지하기 위한 도료로, 주로 프라이머(primer)로 사용되며, 아연 분말(zinc dust), 에폭시, 알키드 등 다양한 종류가 있습니다. 통역 시 주의할 점은 방청도료의 종류에 따라 방청 메커니즘(억제형, 희생양극형, 차단형)이 다르므로, 시방서에 명시된 제품을 정확히 확인해야 합니다. 특히 '징크 리치 프라이머'(Zinc-rich primer, sơn giàu kẽm)는 아연 함량 80% 이상의 고성능 방청도료로, 해양 구조물이나 교량에 필수적이므로 일반 방청도료와 구분하여 통역하세요.",
        "meaningVi": "Loại sơn ngăn ngừa sự ăn mòn (gỉ sét) của vật liệu thép, chủ yếu được sử dụng làm sơn lót, có nhiều loại như bột kẽm (zinc dust), epoxy, alkyd. Cơ chế chống gỉ khác nhau tùy loại sơn (ức chế, anốt hy sinh, cách ly).",
        "context": "철골 구조물, 교량, 선박, 해양 구조물, 공장 설비",
        "culturalNote": "한국에서는 철골 구조물에 대한 방청 관리가 엄격하며, 환경(일반 대기, 산업 지역, 해안)에 따라 방청도료의 등급을 KS M 5000 시리즈 규격에 따라 선정합니다. 베트남에서는 저가 방청도료 사용으로 인한 조기 부식이 빈번하여, 한국 시공사가 베트남에서 시공 시 방청도료 품질 관리에 특히 주의해야 합니다. 통역 시 '징크 리치 프라이머'(sơn lót giàu kẽm)와 일반 '방청 프라이머'(sơn lót chống gỉ)의 차이를 명확히 하고, 해안 지역(khu vực ven biển)에서는 반드시 고성능 제품을 사용해야 함을 강조하세요. 또한 방청도료는 표면 처리(케렌) 상태에 따라 성능이 크게 달라지므로, 블라스팅(làm sạch bằng phun cát) 등급을 함께 확인해야 합니다.",
        "commonMistakes": [
            {
                "mistake": "모든 방청도료를 'sơn chống gỉ'로만 통역",
                "correction": "sơn chống gỉ kẽm phốt-phat (아연계), sơn chống gỉ giàu kẽm (징크리치), sơn lót epoxy chống gỉ (에폭시계) 구분",
                "explanation": "방청도료의 종류에 따라 성능과 가격이 크게 다르므로 정확한 명칭이 필요합니다."
            },
            {
                "mistake": "방청도료와 프라이머를 별개로 통역",
                "correction": "방청도료는 보통 프라이머로 사용됨을 설명",
                "explanation": "방청도료는 대부분 하도(프라이머)로 적용되므로 혼동을 방지해야 합니다."
            },
            {
                "mistake": "표면 처리 등급 없이 방청도료만 지정",
                "correction": "표면 처리 등급(Sa 2.5, St 3 등)과 함께 통역",
                "explanation": "방청 성능은 표면 처리 상태에 크게 의존하므로 함께 명시해야 합니다."
            },
            {
                "mistake": "일반 환경과 해양 환경을 구분하지 않고 통역",
                "correction": "môi trường thông thường (일반), môi trường biển (해양) 구분 + 적합한 방청도료 종류 명시",
                "explanation": "환경에 따라 요구되는 방청 성능이 다르므로 구분이 필수입니다."
            }
        ],
        "examples": [
            {
                "ko": "해안 지역 철골에는 징크 리치 프라이머를 Sa 2.5 블라스팅 후 도막두께 75㎛로 도포하십시오.",
                "vi": "Đối với kết cấu thép khu vực ven biển, sau khi làm sạch bằng phun cát cấp Sa 2.5, sơn lót giàu kẽm với độ dày màng sơn 75 micromet.",
                "situation": "formal"
            },
            {
                "ko": "이 철골은 일반 환경이니까 에폭시 방청 프라이머면 충분해요.",
                "vi": "Kết cấu thép này ở môi trường thông thường nên dùng sơn lót epoxy chống gỉ là đủ.",
                "situation": "onsite"
            },
            {
                "ko": "방청 페인트 안 칠하면 1년도 안 돼서 녹슬어요, 꼭 제대로 칠하세요.",
                "vi": "Nếu không sơn chống gỉ thì chưa đầy 1 năm sẽ bị gỉ, nhất định phải sơn đúng cách.",
                "situation": "informal"
            }
        ],
        "relatedTerms": ["프라이머", "케렌", "블라스팅", "징크리치프라이머"]
    },
    {
        "slug": "blasting-phun-cat",
        "korean": "블라스팅",
        "vietnamese": "Phun cát",
        "hanja": None,
        "hanjaReading": None,
        "pronunciation": "블라스팅",
        "meaningKo": "압축 공기로 연마재(모래, 강구 등)를 고속 분사하여 철재 표면의 녹, 스케일, 오염물을 제거하고 거친 표면(조면)을 만드는 표면 처리 방법입니다. 통역 시 주의할 점은 블라스팅의 청정도 등급(cleanliness grade)을 ISO 8501-1 또는 SSPC 기준(Sa 1, Sa 2, Sa 2.5, Sa 3)에 따라 정확히 표현해야 하며, 베트남에서는 'phun cát'(모래 분사)가 일반적 용어이지만 실제로는 강구(steel shot), 가넷(garnet) 등 다양한 연마재를 사용하므로 재료도 명시해야 합니다. 블라스팅 후 표면 조도(粗度, surface roughness: Rz, Ra)도 방청도료의 부착력에 중요하므로 시방서에 명시된 경우 정확히 통역하세요.",
        "meaningVi": "Phương pháp xử lý bề mặt bằng cách phun các vật liệu mài (cát, bi thép, v.v.) với tốc độ cao bằng khí nén để loại bỏ gỉ sét, cáu bẩn, và tạo bề mặt nhám trên thép. Độ sạch được phân loại theo tiêu chuẩn ISO 8501-1 hoặc SSPC (Sa 1, Sa 2, Sa 2.5, Sa 3).",
        "context": "철골 표면 처리, 도장 전처리, 교량 정비, 탱크 보수",
        "culturalNote": "한국 건설 현장에서는 중요 철골 구조물(교량, 철탑, 플랜트)의 도장 전 블라스팅을 표준으로 하며, Sa 2.5 등급(거의 완전한 청정, nearly white metal) 이상을 요구하는 경우가 많습니다. 베트남에서는 블라스팅 설비와 기술이 부족하여 와이어 브러시(chổi sắt), 샌더(máy chà nhám) 등 간이 방법으로 대체하려는 경우가 많아, 통역 시 블라스팅의 필수성과 대체 불가함을 강조해야 합니다. 또한 블라스팅 작업은 분진(bụi), 소음(tiếng ồn), 진동(rung động)이 심하므로 안전 장비(mặt nạ, tai nghe, quần áo bảo hộ)와 주변 보양(che chắn)이 필수임을 전달하세요. 블라스팅 비용은 한국에서 ㎡당 5,000~10,000원으로 고가이므로, 예산 협의 시 별도 항목임을 명확히 하세요.",
        "commonMistakes": [
            {
                "mistake": "블라스팅을 'làm sạch'(청소)로만 통역",
                "correction": "phun cát 또는 phun bi thép (구체적 방법 명시)",
                "explanation": "블라스팅은 단순 청소가 아니라 특수 장비를 사용한 전문 공정이므로 정확한 용어가 필요합니다."
            },
            {
                "mistake": "청정도 등급을 설명 없이 'Sa 2.5'로만 통역",
                "correction": "Sa 2.5 (gần như kim loại trắng, 거의 백색 금속) + 육안 기준 설명",
                "explanation": "ISO 코드만으로는 이해하기 어려우므로 실제 상태를 설명해야 합니다."
            },
            {
                "mistake": "블라스팅을 와이어 브러시나 샌더로 대체 가능하다고 통역",
                "correction": "블라스팅과 다른 방법의 성능 차이 설명 + 시방서 준수 강조",
                "explanation": "블라스팅 대체 시 방청 성능이 크게 저하되므로 임의 변경을 막아야 합니다."
            },
            {
                "mistake": "블라스팅 후 표면 조도 요구사항 생략",
                "correction": "độ nhám bề mặt Rz 50~100 micromet (표면 조도 범위) 명시",
                "explanation": "조도가 너무 높거나 낮으면 도료 부착력에 문제가 생기므로 범위를 전달해야 합니다."
            }
        ],
        "examples": [
            {
                "ko": "교량 철골은 블라스팅 Sa 2.5 등급으로 처리 후 8시간 이내에 방청 프라이머를 도포하십시오.",
                "vi": "Kết cấu thép cầu phải được xử lý bằng phun cát cấp Sa 2.5, sau đó sơn lót chống gỉ trong vòng 8 giờ.",
                "situation": "formal"
            },
            {
                "ko": "블라스팅 할 때 주변에 비닐 쳐서 분진 안 날리게 하고, 작업자는 방진 마스크 꼭 쓰세요.",
                "vi": "Khi phun cát phải che chắn bằng bạt nhựa để bụi không bay ra, và người thi công nhất định phải đeo mặt nạ chống bụi.",
                "situation": "onsite"
            },
            {
                "ko": "블라스팅 비용이 좀 비싸긴 한데, 안 하면 페인트 금방 벗겨져요.",
                "vi": "Chi phí phun cát tuy hơi đắt nhưng nếu không làm thì sơn sẽ bong ra rất nhanh.",
                "situation": "informal"
            }
        ],
        "relatedTerms": ["케렌", "방청도료", "표면처리", "도장전처리"]
    },
    {
        "slug": "keren-lam-sach-be-mat",
        "korean": "케렌",
        "vietnamese": "Làm sạch bề mặt",
        "hanja": None,
        "hanjaReading": None,
        "pronunciation": "케렌",
        "meaningKo": "도장 전 철재 표면의 녹, 오염물, 기존 도막을 제거하는 표면 처리 작업의 총칭으로, 일본어 'ケレン(Keren)'에서 유래한 한국 건설 현장 용어입니다. 케렌은 방법에 따라 1종~4종으로 분류되며, 1종(블라스팅), 2종(동력공구+약액), 3종(동력공구), 4종(수공구)로 구분됩니다. 통역 시 주의할 점은 베트남어에 '케렌'에 해당하는 단일 용어가 없어 'làm sạch bề mặt'(표면 청소) 또는 'xử lý bề mặt'(표면 처리)로 표현하되, 구체적 방법(phun cát, chổi sắt, máy mài 등)을 함께 명시해야 정확히 전달됩니다.",
        "meaningVi": "Tổng thể các công tác xử lý bề mặt để loại bỏ gỉ sét, chất bẩn, và lớp sơn cũ trên bề mặt thép trước khi sơn. Phân loại theo phương pháp: loại 1 (phun cát), loại 2 (công cụ động lực + hóa chất), loại 3 (công cụ động lực), loại 4 (công cụ thủ công).",
        "context": "철골 도장 전처리, 재도장 공사, 유지보수",
        "culturalNote": "한국 건설 현장에서 '케렌'은 도장 품질을 결정하는 가장 중요한 공정으로 인식되며, '도장은 70%가 케렌이다'라는 말이 있을 정도입니다. 베트남에서는 케렌의 중요성에 대한 인식이 부족하여 간단히 와이어 브러시로 훑는 수준에서 마무리하는 경우가 많아, 통역 시 케렌 등급과 품질 기준을 명확히 전달해야 합니다. 특히 재도장(sơn lại) 공사에서는 기존 도막의 상태에 따라 케렌 방법을 달리해야 하므로, 시방서에 명시된 케렌 종류를 정확히 확인하고 통역하세요. 한국에서는 1종 케렌(블라스팅)을 선호하지만 비용이 높아, 베트남 협력업체와의 견적 협의 시 케렌 종류에 따른 비용 차이를 사전에 조율해야 합니다.",
        "commonMistakes": [
            {
                "mistake": "케렌을 'vệ sinh'(위생 청소)로 통역",
                "correction": "làm sạch bề mặt 또는 xử lý bề mặt (구체적 방법 추가)",
                "explanation": "'vệ sinh'는 일상적 청소를 의미하므로 전문적인 표면 처리 작업에는 부적합합니다."
            },
            {
                "mistake": "케렌 1종~4종을 번역 없이 '1종 케렌'으로만 통역",
                "correction": "loại 1 (phun cát), loại 2 (công cụ động lực + hóa chất) 등 방법 명시",
                "explanation": "케렌 종류는 한국 고유 분류이므로 구체적 방법을 설명해야 이해할 수 있습니다."
            },
            {
                "mistake": "케렌을 생략하고 바로 도장 가능하다고 통역",
                "correction": "케렌 없이는 도료 부착 불가, 반드시 필요한 공정임을 강조",
                "explanation": "표면 처리는 도장 품질의 기본이므로 생략 불가능함을 명확히 해야 합니다."
            },
            {
                "mistake": "재도장 시 케렌 방법을 구체적으로 확인하지 않고 통역",
                "correction": "기존 도막 상태 확인 후 적합한 케렌 방법 제시",
                "explanation": "재도장은 기존 도막 상태에 따라 케렌 방법이 달라지므로 현장 확인이 필수입니다."
            }
        ],
        "examples": [
            {
                "ko": "이 철골은 1종 케렌(블라스팅 Sa 2.5)으로 표면 처리 후 도장하십시오.",
                "vi": "Kết cấu thép này phải xử lý bề mặt bằng phương pháp loại 1 (phun cát cấp Sa 2.5) trước khi sơn.",
                "situation": "formal"
            },
            {
                "ko": "기존 페인트 상태가 좋으니까 3종 케렌(전동 공구)으로 녹만 제거하고 덧칠하세요.",
                "vi": "Lớp sơn cũ còn tốt nên chỉ cần loại bỏ gỉ bằng công cụ động lực (loại 3) rồi sơn lại.",
                "situation": "onsite"
            },
            {
                "ko": "케렌 제대로 안 하면 페인트 금방 벗겨져요, 시간 걸려도 꼼꼼히 하세요.",
                "vi": "Nếu làm sạch bề mặt không kỹ thì sơn sẽ bong ra nhanh, tốn thời gian nhưng phải làm kỹ càng.",
                "situation": "informal"
            }
        ],
        "relatedTerms": ["블라스팅", "표면처리", "방청도료", "재도장"]
    },
    {
        "slug": "do-mak-du-ke-do-day-mang-son",
        "korean": "도막두께",
        "vietnamese": "Độ dày màng sơn",
        "hanja": "塗膜厚",
        "hanjaReading": "塗(칠할 도) + 膜(막 막) + 厚(두꺼울 후)",
        "pronunciation": "도막두께",
        "meaningKo": "도장 후 형성된 도료 피막(도막)의 두께를 말하며, 단위는 마이크로미터(㎛, micrometer) 또는 밀(mil, 1mil=25.4㎛)을 사용합니다. 통역 시 주의할 점은 도막두께는 도장 품질과 내구성을 결정하는 핵심 지표로, 시방서에 명시된 최소 두께(건조 피막 두께, DFT: Dry Film Thickness)를 반드시 충족해야 하며, 현장에서 전자식 막두께 측정기(máy đo độ dày màng sơn, coating thickness gauge)로 측정하여 검증합니다. 습윤 피막 두께(WFT: Wet Film Thickness)와 건조 피막 두께(DFT)는 다르므로(도료의 고형분율에 따라 DFT는 WFT의 40~70%), 어느 것을 기준으로 하는지 명확히 해야 합니다.",
        "meaningVi": "Độ dày của lớp màng sơn sau khi sơn, đơn vị là micromet (㎛) hoặc mil (1mil=25.4㎛). Là chỉ tiêu then chốt quyết định chất lượng và độ bền của lớp sơn, phải đạt độ dày tối thiểu theo thuyết minh kỹ thuật và được kiểm tra bằng máy đo độ dày màng sơn.",
        "context": "도장 품질관리, 공사 검수, 감리 점검",
        "culturalNote": "한국 건설 현장에서 도막두께 측정은 도장 공정의 필수 품질 관리 항목으로, KS M ISO 2808 규격에 따라 일정 면적당 측정 개수(보통 ㎡당 5개소)가 정해져 있으며, 평균값과 최소값이 모두 기준을 충족해야 합니다. 베트남에서는 도막두께 측정을 생략하거나 육안으로만 확인하는 경우가 많아, 통역 시 측정의 필수성과 측정 방법을 구체적으로 설명해야 합니다. 특히 방청도료와 내화도료는 두께가 성능에 직결되므로 측정이 더욱 중요합니다. 도막두께 측정기는 전자식(điện tử, electromagnetic/eddy current)이 정확하지만 고가이므로, 베트남 협력업체가 보유하지 않은 경우 대여 또는 구매 방안을 사전에 협의하세요. 도막두께 부족 시 재시공해야 하므로 시공 중 중간 점검을 권장합니다.",
        "commonMistakes": [
            {
                "mistake": "도막두께를 'độ dày sơn'으로만 통역",
                "correction": "độ dày màng sơn 또는 độ dày lớp sơn khô (건조막 두께 강조)",
                "explanation": "'độ dày sơn'은 모호하며, '막'(màng) 개념을 명확히 해야 합니다."
            },
            {
                "mistake": "습윤막 두께(WFT)와 건조막 두께(DFT)를 구분하지 않고 통역",
                "correction": "độ dày màng ướt (WFT), độ dày màng khô (DFT) 구분 + 시방서 기준 명시",
                "explanation": "두 값은 다르므로 어느 것을 기준으로 하는지 명확히 해야 시공 오류를 방지할 수 있습니다."
            },
            {
                "mistake": "도막두께 단위 ㎛와 mm를 혼동",
                "correction": "일반 도료는 ㎛ (마이크로미터), 바닥재/내화도료는 mm (밀리미터) 사용",
                "explanation": "단위 혼동 시 1000배 차이가 나므로 심각한 시공 오류가 발생합니다."
            },
            {
                "mistake": "도막두께 측정 위치와 개수를 명시하지 않음",
                "correction": "측정 위치(골조, 평면 등), 개수(㎡당 5개소 등) 구체적 통역",
                "explanation": "측정 방법이 불명확하면 측정 결과의 신뢰성이 떨어지고 분쟁의 원인이 됩니다."
            }
        ],
        "examples": [
            {
                "ko": "이 철골의 도막두께는 프라이머 50㎛, 중도 40㎛, 상도 50㎛로 총 140㎛ 이상이어야 합니다.",
                "vi": "Độ dày màng sơn của kết cấu thép này phải đạt sơn lót 50 micromet, sơn phủ giữa 40 micromet, sơn hoàn thiện 50 micromet, tổng cộng tối thiểu 140 micromet.",
                "situation": "formal"
            },
            {
                "ko": "도막두께 측정기로 확인했더니 여기는 30㎛밖에 안 나와요, 다시 칠해야 해요.",
                "vi": "Đo bằng máy đo độ dày màng sơn thì chỗ này chỉ đạt 30 micromet thôi, phải sơn lại.",
                "situation": "onsite"
            },
            {
                "ko": "도막두께 얇으면 몇 년 못 가서 녹슬어요, 기준대로 두껍게 칠하세요.",
                "vi": "Nếu màng sơn mỏng thì không được vài năm sẽ bị gỉ, phải sơn dày theo tiêu chuẩn.",
                "situation": "informal"
            }
        ],
        "relatedTerms": ["프라이머", "중도", "상도", "품질관리"]
    }
]

# 기존 파일 로드
file_path = os.path.join(
    os.path.dirname(__file__),
    "..",
    "data",
    "terms",
    "construction.json"
)

with open(file_path, "r", encoding="utf-8") as f:
    existing_data = json.load(f)

# 중복 체크 (slug 기준)
existing_slugs = {term["slug"] for term in existing_data}
new_terms = [term for term in data if term["slug"] not in existing_slugs]

if not new_terms:
    print("⚠️  모든 용어가 이미 존재합니다. 추가할 용어가 없습니다.")
else:
    # 기존 데이터에 추가
    existing_data.extend(new_terms)

    # 파일 저장
    with open(file_path, "w", encoding="utf-8") as f:
        json.dump(existing_data, f, ensure_ascii=False, indent=2)

    print(f"✅ {len(new_terms)}개 용어 추가 완료!")
    print(f"📊 전체 용어 수: {len(existing_data)}개")
    for term in new_terms:
        print(f"   - {term['korean']} ({term['vietnamese']})")
