#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
건식/습식 시공법 용어 추가 스크립트
테마: 건식공법, 습식공법, 조적, 블록쌓기, 창호설치, 유리시공, 실리콘시공, 백업재설치, 브래킷, 앵커시공
"""

import json
import os

# 추가할 용어 데이터 (Tier S 기준)
data = [
    {
        "slug": "cong-phap-kho",
        "korean": "건식 공법",
        "vietnamese": "Công pháp khô",
        "hanja": "乾式工法",
        "hanjaReading": "乾(마를 건) + 式(법 식) + 工(장인 공) + 法(법 법)",
        "pronunciation": "꽁 팝 커",
        "meaningKo": "물이나 습기를 사용하지 않고 미리 제작된 부재를 조립·설치하는 건설 공법. 습식 공법 대비 공기 단축, 양생 시간 불필요, 계절·날씨 영향 적음이 장점이며, 석고보드, 드라이비트, 커튼월 등에 적용됩니다. 통역 시 베트남에서는 'thi công không ướt'로도 표현되나, 전문 회의에서는 'công pháp khô'가 표준입니다. 한국은 내장 공사의 대부분이 건식화되어 있으나, 베트남은 아직 습식 공법 선호도가 높아 기술 전환이 진행 중입니다.",
        "meaningVi": "Phương pháp thi công sử dụng cấu kiện được chế tạo sẵn và lắp ráp, không dùng nước hay độ ẩm. Tiết kiệm thời gian, không cần dưỡng hộ, ít bị ảnh hưởng thời tiết và mùa vụ.",
        "context": "내장 공사, 외벽 마감, 천장, 칸막이, 커튼월",
        "culturalNote": "한국은 아파트 내장재가 거의 100% 건식 공법으로 전환되었고, 정부도 '습식→건식' 전환을 장려하고 있으나, 베트남은 벽돌·몰탈 중심의 습식 공법이 여전히 주류입니다. 통역 시 한국의 '공기 단축(rút ngắn thời gian)' 및 '품질 균일성(chất lượng đồng đều)' 장점을 강조하면 베트남 측 이해를 도울 수 있습니다. 베트남에서는 'khô'라는 단어가 '건조'를 의미하므로, 'không dùng nước'라는 설명을 추가하면 혼동을 방지할 수 있습니다.",
        "commonMistakes": [
            {
                "mistake": "마른 공법",
                "correction": "건식 공법",
                "explanation": "직역이 아닌 전문 용어로 표현 필요"
            },
            {
                "mistake": "xây khô",
                "correction": "công pháp khô / thi công khô",
                "explanation": "'건조하게 쌓기'는 부정확, 건식 공법임을 명시 필요"
            },
            {
                "mistake": "조립식",
                "correction": "건식 공법 (또는 조립과 구분 설명)",
                "explanation": "조립은 방법, 건식은 공법 개념이므로 구분 필요"
            }
        ],
        "examples": [
            {
                "ko": "이번 현장은 공기 단축을 위해 건식 공법으로 진행합니다.",
                "vi": "Công trường này áp dụng công pháp khô để rút ngắn thời gian.",
                "situation": "formal"
            },
            {
                "ko": "건식 벽체는 양생 기간이 필요 없어서 바로 다음 공정으로 넘어갈 수 있어요.",
                "vi": "Vách khô không cần dưỡng hộ nên có thể chuyển ngay sang công đoạn tiếp theo.",
                "situation": "onsite"
            },
            {
                "ko": "장마철에는 건식 공법이 유리해요.",
                "vi": "Mùa mưa thì công pháp khô có lợi hơn.",
                "situation": "informal"
            }
        ],
        "relatedTerms": ["습식 공법", "석고보드", "경량벽체", "드라이비트", "커튼월"]
    },
    {
        "slug": "cong-phap-uot",
        "korean": "습식 공법",
        "vietnamese": "Công pháp ướt",
        "hanja": "濕式工法",
        "hanjaReading": "濕(젖을 습) + 式(법 식) + 工(장인 공) + 法(법 법)",
        "pronunciation": "꽁 팝 웃",
        "meaningKo": "물, 시멘트, 몰탈 등 습기를 사용하는 전통적인 건설 공법. 벽돌 쌓기, 미장, 타일 붙이기, 콘크리트 타설 등이 대표적이며, 견고함과 방수성이 장점이나 양생 기간이 필요하고 공기가 길어지는 단점이 있습니다. 통역 시 베트남에서는 'thi công truyền thống(전통 공법)'이라는 표현도 병용되며, 'phương pháp ướt'보다 'công pháp ướt'가 더 전문적입니다. 한국은 습식→건식 전환 추세이나, 베트남은 아직 습식이 주류여서 문화적 차이를 이해해야 합니다.",
        "meaningVi": "Phương pháp thi công truyền thống sử dụng nước, xi măng, vữa. Bao gồm xây gạch, trát, ốp gạch, đổ bê tông. Có ưu điểm vững chắc và chống thấm nhưng cần thời gian dưỡng hộ và kéo dài thời gian thi công.",
        "context": "벽돌 쌓기, 미장, 타일, 콘크리트, 방수",
        "culturalNote": "한국은 1990년대 이후 내장재의 건식화가 진행되어 습식 공법은 욕실·주방 등 일부 공간에만 사용되나, 베트남은 여전히 벽돌·몰탈 중심의 습식 공법이 건설 현장의 주류입니다. 통역 시 양국의 공법 선호도 차이를 설명하고, 한국의 '공기 단축 압박(áp lực rút ngắn thời gian)'을 언급하면 건식 전환 배경을 이해시킬 수 있습니다. 베트남에서는 습식 공법이 '견고하다(vững chắc)'는 인식이 강하므로, 건식 공법의 강도를 강조할 때는 데이터를 제시하세요.",
        "commonMistakes": [
            {
                "mistake": "물 공법",
                "correction": "습식 공법",
                "explanation": "직역이 아닌 전문 용어로 표현 필요"
            },
            {
                "mistake": "xây ướt",
                "correction": "công pháp ướt / thi công ướt",
                "explanation": "'젖게 쌓기'는 부정확, 습식 공법임을 명시 필요"
            },
            {
                "mistake": "전통 방식",
                "correction": "습식 공법 (또는 전통과 구분 설명)",
                "explanation": "전통은 문화적 맥락, 습식은 기술적 개념이므로 구분 필요"
            }
        ],
        "examples": [
            {
                "ko": "욕실은 방수가 중요해서 습식 공법으로 시공합니다.",
                "vi": "Phòng tắm cần chống thấm nên thi công bằng công pháp ướt.",
                "situation": "formal"
            },
            {
                "ko": "습식 미장은 양생 기간 7일 필요해요.",
                "vi": "Trát ướt cần dưỡng hộ 7 ngày.",
                "situation": "onsite"
            },
            {
                "ko": "습식은 날씨 영향을 많이 받아서 건기에 해야 해요.",
                "vi": "Công pháp ướt bị ảnh hưởng thời tiết nhiều nên phải làm vào mùa khô.",
                "situation": "informal"
            }
        ],
        "relatedTerms": ["건식 공법", "벽돌 쌓기", "미장", "타일", "양생"]
    },
    {
        "slug": "xay-gach",
        "korean": "조적",
        "vietnamese": "Xây gạch",
        "hanja": "組積",
        "hanjaReading": "組(짤 조) + 積(쌓을 적)",
        "pronunciation": "싸이 각",
        "meaningKo": "벽돌, 블록, 돌 등을 쌓아 벽체나 구조물을 만드는 공법. 내력벽과 비내력벽으로 구분되며, 시공 시 줄눈 정렬, 수직도, 수평도를 엄격히 관리해야 합니다. 통역 시 베트남에서는 'xây tường(벽 쌓기)'라는 표현도 흔하나, 전문 용어로는 'xây gạch' 또는 'công tác nề'를 사용하세요. 한국은 조적조가 감소 추세이나, 베트남은 여전히 주류 공법으로 숙련 기능공(thợ nề) 수요가 높습니다.",
        "meaningVi": "Phương pháp xây tường hoặc kết cấu bằng cách chồng gạch, block, đá. Phân loại thành tường chịu lực và không chịu lực, cần quản lý nghiêm ngặt đường nối, độ thẳng đứng và độ bằng phẳng.",
        "context": "벽체 시공, 담장, 내력벽, 비내력벽, 줄눈",
        "culturalNote": "한국은 조적조 건축물이 감소하고 철근콘크리트 및 철골조로 전환되었으나, 베트남은 여전히 벽돌 건축이 주류이며 '베트남 빨간 벽돌(gạch đỏ Việt Nam)'이 전통적으로 선호됩니다. 통역 시 한국의 '내진 성능(khả năng chống động đất)' 기준을 설명하면 조적조의 한계를 이해시킬 수 있습니다. 베트남에서는 'thợ nề(조적공)'가 매우 중요한 직종이므로, 기능공 존중의 표현을 사용하세요.",
        "commonMistakes": [
            {
                "mistake": "벽돌 쌓기",
                "correction": "조적 / 조적 공사",
                "explanation": "구어체가 아닌 전문 용어로 표현 필요"
            },
            {
                "mistake": "xây tường",
                "correction": "xây gạch / công tác nề",
                "explanation": "벽 쌓기는 일반 표현, 조적 공사 전문 용어 사용 필요"
            },
            {
                "mistake": "쌓기",
                "correction": "조적 / 조적 시공",
                "explanation": "단순 쌓기가 아닌 공법임을 명시 필요"
            }
        ],
        "examples": [
            {
                "ko": "조적 공사 시 줄눈 두께는 10mm로 유지해야 합니다.",
                "vi": "Khi xây gạch phải giữ độ dày mạch vữa 10mm.",
                "situation": "formal"
            },
            {
                "ko": "조적은 수직도가 생명이에요. 추를 항상 확인하세요.",
                "vi": "Xây gạch quan trọng nhất là độ thẳng đứng. Luôn kiểm tra dây dọi.",
                "situation": "onsite"
            },
            {
                "ko": "내일 외벽 조적 시작합니다.",
                "vi": "Mai bắt đầu xây gạch tường ngoài.",
                "situation": "informal"
            }
        ],
        "relatedTerms": ["벽돌", "블록", "줄눈", "내력벽", "미장"]
    },
    {
        "slug": "xay-block",
        "korean": "블록 쌓기",
        "vietnamese": "Xây block",
        "hanja": None,
        "hanjaReading": None,
        "pronunciation": "싸이 블록",
        "meaningKo": "콘크리트 블록이나 경량 블록을 사용하여 벽체를 시공하는 공법. 일반 벽돌 대비 시공 속도가 빠르고 단열·차음 성능이 우수하며, 비내력벽에 주로 사용됩니다. 통역 시 베트남에서는 'gạch block(블록 벽돌)'이라는 표현도 쓰이나, 'block' 자체가 외래어로 통용되므로 'xây block'으로 간결히 표현 가능합니다. 한국은 경량 기포 콘크리트 블록(ALC)이 널리 쓰이며, 베트남은 일반 콘크리트 블록이 주류입니다.",
        "meaningVi": "Phương pháp thi công tường bằng block bê tông hoặc block nhẹ. Tốc độ thi công nhanh hơn gạch thường, cách nhiệt cách âm tốt, chủ yếu dùng cho tường không chịu lực.",
        "context": "비내력벽, 칸막이벽, 단열, 차음",
        "culturalNote": "한국은 1990년대부터 경량 블록(ALC)이 아파트 내부 칸막이에 표준화되었고, 단열 성능이 강조되고 있으나, 베트남은 일반 콘크리트 블록이 주로 사용되며 단열 개념이 상대적으로 약합니다. 통역 시 한국의 '에너지 절약(tiết kiệm năng lượng)' 효과를 설명하면 경량 블록의 장점을 이해시킬 수 있습니다. 베트남에서는 'block'이 외래어지만 워낙 널리 쓰여 'gạch block'으로 표현해도 무방합니다.",
        "commonMistakes": [
            {
                "mistake": "블럭 쌓기",
                "correction": "블록 쌓기 (블록이 표준어)",
                "explanation": "'블럭'은 비표준어, '블록'으로 써야"
            },
            {
                "mistake": "gạch lớn",
                "correction": "block / gạch block",
                "explanation": "'큰 벽돌'은 부정확, 블록 자체가 다른 재료임을 명시 필요"
            },
            {
                "mistake": "콘크리트 벽돌",
                "correction": "블록 / 콘크리트 블록",
                "explanation": "벽돌과 블록은 다른 개념이므로 구분 필요"
            }
        ],
        "examples": [
            {
                "ko": "칸막이벽은 경량 블록으로 시공합니다.",
                "vi": "Tường ngăn thi công bằng block nhẹ.",
                "situation": "formal"
            },
            {
                "ko": "블록 쌓기는 벽돌보다 빨라서 공기 단축에 유리해요.",
                "vi": "Xây block nhanh hơn gạch nên có lợi cho rút ngắn thời gian.",
                "situation": "onsite"
            },
            {
                "ko": "내일 블록 100개 반입됩니다.",
                "vi": "Mai nhập 100 viên block.",
                "situation": "informal"
            }
        ],
        "relatedTerms": ["조적", "경량 블록", "ALC", "칸막이벽", "비내력벽"]
    },
    {
        "slug": "lap-dat-cua-so",
        "korean": "창호 설치",
        "vietnamese": "Lắp đặt cửa sổ",
        "hanja": "窓戶設置",
        "hanjaReading": "窓(창 창) + 戶(지게 호) + 設(베풀 설) + 置(둘 치)",
        "pronunciation": "럽 닷 꾸어 쏘",
        "meaningKo": "창문과 문(창호)을 벽체 개구부에 설치하는 공정. 수평·수직 정렬, 실링, 단열, 방수 처리가 중요하며, 시공 불량 시 누수와 결로가 발생합니다. 통역 시 베트남에서는 'cửa sổ(창문)'와 'cửa đi(출입문)'를 구분하여 표현하며, 한국의 '창호'는 두 가지를 통칭하는 개념이므로 'cửa (sổ và đi)'로 설명하세요. 한국은 PVC·알루미늄 시스템 창호가 주류이나, 베트남은 알루미늄이 대부분입니다.",
        "meaningVi": "Công đoạn lắp đặt cửa sổ và cửa đi vào ô tường. Cần chú ý căn chỉnh thẳng đứng ngang, trám kín, cách nhiệt và chống thấm. Thi công kém dẫn đến thấm nước và ngưng tụ ẩm.",
        "context": "창문, 출입문, 실링, 단열, 방수, 정렬",
        "culturalNote": "한국은 단열 성능(U-value)과 기밀 성능(Q-value) 기준이 엄격하여 고성능 시스템 창호가 의무화되어 있으나, 베트남은 아직 단열 개념이 약하고 가격 중심으로 선택됩니다. 통역 시 한국의 '에너지 절약(tiết kiệm năng lượng)' 및 '결로 방지(chống ngưng tụ)' 효과를 설명하면 고성능 창호의 필요성을 이해시킬 수 있습니다. 베트남에서는 'cửa nhôm kính(알루미늄 유리창)'이라는 표현이 매우 흔합니다.",
        "commonMistakes": [
            {
                "mistake": "창문 달기",
                "correction": "창호 설치 / 창호 시공",
                "explanation": "구어체가 아닌 전문 용어로 표현 필요"
            },
            {
                "mistake": "lắp cửa",
                "correction": "lắp đặt cửa sổ / thi công cửa",
                "explanation": "'문 달기'는 단순 표현, 설치 공정임을 명시 필요"
            },
            {
                "mistake": "창문 끼우기",
                "correction": "창호 설치",
                "explanation": "'끼우기'는 비전문적 표현, 설치로 표현 필요"
            }
        ],
        "examples": [
            {
                "ko": "창호 설치 시 수평계로 반드시 수평을 맞춰야 합니다.",
                "vi": "Khi lắp đặt cửa sổ phải dùng thước thủy kiểm tra độ ngang.",
                "situation": "formal"
            },
            {
                "ko": "창호 둘레에 실리콘 실링 빠짐없이 해주세요.",
                "vi": "Hãy trám silicone đầy đủ quanh cửa sổ.",
                "situation": "onsite"
            },
            {
                "ko": "내일 창호 설치 업체 옵니다.",
                "vi": "Mai đơn vị lắp cửa sổ đến.",
                "situation": "informal"
            }
        ],
        "relatedTerms": ["창호", "실링", "단열", "방수", "알루미늄 새시"]
    },
    {
        "slug": "thi-cong-kinh",
        "korean": "유리 시공",
        "vietnamese": "Thi công kính",
        "hanja": "琉璃施工",
        "hanjaReading": "琉(유리 유) + 璃(유리 리) + 施(베풀 시) + 工(장인 공)",
        "pronunciation": "티 꽁 낑",
        "meaningKo": "건물 외벽이나 내부에 유리를 설치하는 공정. 커튼월, 창호, 간판, 파티션 등에 적용되며, 유리 종류(강화, 접합, 복층), 두께, 안전 처리가 중요합니다. 통역 시 베트남에서는 'kính cường lực(강화유리)', 'kính hộp(복층유리)' 등 구체적인 유리 종류를 함께 명시하면 이해도가 높아집니다. 한국은 고층 빌딩의 커튼월 유리 시공 기술이 선진화되어 있으나, 베트남은 아직 숙련 기능공이 부족한 편입니다.",
        "meaningVi": "Công đoạn lắp đặt kính cho tường ngoài hoặc bên trong tòa nhà. Áp dụng cho curtain wall, cửa sổ, biển hiệu, vách ngăn. Cần chú ý loại kính (cường lực, an toàn, hộp), độ dày và xử lý an toàn.",
        "context": "커튼월, 창호, 강화유리, 복층유리, 안전",
        "culturalNote": "한국은 건축법상 일정 높이 이상 건물에 강화유리 또는 접합유리 사용이 의무화되어 있고, 안전 기준이 엄격하나, 베트남은 안전 규제가 상대적으로 느슨합니다. 통역 시 한국의 '낙하 사고 방지(phòng tránh tai nạn rơi kính)' 및 '자외선 차단(chống tia UV)' 기능을 설명하면 고성능 유리의 필요성을 이해시킬 수 있습니다. 베트남에서는 'kính'이라는 단어가 '안경'도 의미하므로, 맥락을 명확히 하세요.",
        "commonMistakes": [
            {
                "mistake": "유리 붙이기",
                "correction": "유리 시공 / 유리 설치",
                "explanation": "구어체가 아닌 전문 용어로 표현 필요"
            },
            {
                "mistake": "dán kính",
                "correction": "thi công kính / lắp đặt kính",
                "explanation": "'붙이기'는 단순 표현, 시공임을 명시 필요"
            },
            {
                "mistake": "유리창 끼우기",
                "correction": "유리 시공",
                "explanation": "'끼우기'는 비전문적 표현, 시공으로 표현 필요"
            }
        ],
        "examples": [
            {
                "ko": "커튼월 유리 시공 시 풍압을 고려한 설계가 필수입니다.",
                "vi": "Khi thi công kính curtain wall cần thiết kế tính đến áp lực gió.",
                "situation": "formal"
            },
            {
                "ko": "유리 시공 시 안전 장갑과 보호구 착용 필수예요.",
                "vi": "Khi thi công kính bắt buộc đeo găng tay và đồ bảo hộ.",
                "situation": "onsite"
            },
            {
                "ko": "다음 주에 로비 유리 시공합니다.",
                "vi": "Tuần sau thi công kính sảnh.",
                "situation": "informal"
            }
        ],
        "relatedTerms": ["커튼월", "강화유리", "복층유리", "실링", "창호"]
    },
    {
        "slug": "tram-silicone",
        "korean": "실리콘 시공",
        "vietnamese": "Trám silicone",
        "hanja": None,
        "hanjaReading": None,
        "pronunciation": "짬 실리꼰",
        "meaningKo": "건축물의 이음매, 틈새에 실리콘 실란트를 주입하여 방수·기밀·단열 성능을 확보하는 공정. 창호 둘레, 타일 줄눈, 커튼월 이음부 등에 적용되며, 시공 품질에 따라 누수와 곰팡이 발생 여부가 결정됩니다. 통역 시 베트남에서는 'trám kín(틈새 메우기)'이라는 표현도 쓰이나, 전문 용어로는 'trám silicone' 또는 'thi công silicone'을 사용하세요. 한국은 실리콘 색상·종류가 다양하나, 베트남은 투명(trong suốt)과 백색(trắng)이 주류입니다.",
        "meaningVi": "Công đoạn bơm silicone vào mối nối, khe hở của công trình để đảm bảo chống thấm, kín khí và cách nhiệt. Áp dụng cho quanh cửa sổ, mạch gạch, mối nối curtain wall. Chất lượng thi công quyết định thấm nước và nấm mốc.",
        "context": "방수, 기밀, 창호, 타일, 커튼월",
        "culturalNote": "한국은 실리콘 시공 품질 기준이 엄격하여 전문 시공업체가 존재하고, 색상·용도별 실리콘이 세분화되어 있으나, 베트남은 숙련공이 부족하고 범용 제품이 주로 사용됩니다. 통역 시 한국의 '곰팡이 방지(chống nấm mốc)' 및 '내구성(độ bền)' 효과를 설명하면 고품질 실리콘의 필요성을 이해시킬 수 있습니다. 베트남에서는 'keo silicon(실리콘 본드)'이라는 표현도 널리 쓰입니다.",
        "commonMistakes": [
            {
                "mistake": "실리콘 바르기",
                "correction": "실리콘 시공 / 실링 시공",
                "explanation": "구어체가 아닌 전문 용어로 표현 필요"
            },
            {
                "mistake": "bôi silicone",
                "correction": "trám silicone / thi công silicone",
                "explanation": "'바르기'는 단순 표현, 시공 공정임을 명시 필요"
            },
            {
                "mistake": "코킹",
                "correction": "실리콘 시공 (또는 코킹 설명)",
                "explanation": "코킹은 외래어, 실리콘 시공으로 표준화 필요"
            }
        ],
        "examples": [
            {
                "ko": "창호 설치 후 실리콘 시공으로 방수 처리를 완료합니다.",
                "vi": "Sau khi lắp cửa sổ hoàn tất chống thấm bằng trám silicone.",
                "situation": "formal"
            },
            {
                "ko": "실리콘은 건조 시간 24시간이니까 내일 검사하세요.",
                "vi": "Silicone khô mất 24 giờ nên mai hãy kiểm tra.",
                "situation": "onsite"
            },
            {
                "ko": "욕실 타일 줄눈에 실리콘 다시 쳐야 해요.",
                "vi": "Phải trám lại silicone mạch gạch phòng tắm.",
                "situation": "informal"
            }
        ],
        "relatedTerms": ["실링", "방수", "창호", "타일", "커튼월"]
    },
    {
        "slug": "lap-vat-lieu-lot",
        "korean": "백업재 설치",
        "vietnamese": "Lắp vật liệu lót",
        "hanja": None,
        "hanjaReading": None,
        "pronunciation": "럽 벗 리에우 롯",
        "meaningKo": "실리콘 시공 전 이음부에 삽입하는 폼 재료로, 실리콘 접착면을 조절하고 3면 접착을 방지하여 내구성을 높입니다. 커튼월, 창호, 타일 줄눈 등에 필수적이며, 시공 누락 시 실리콘 탈락 및 누수 발생 위험이 큽니다. 통역 시 베트남에서는 'backer rod'라는 영어 용어도 통용되나, 'vật liệu lót đáy' 또는 'foam đệm'으로 설명하면 이해가 쉽습니다. 한국은 백업재 설치가 표준화되어 있으나, 베트남은 인식이 낮아 생략되는 경우가 많습니다.",
        "meaningVi": "Vật liệu foam đặt vào mối nối trước khi trám silicone, giúp điều chỉnh mặt dính silicone và tránh dính 3 mặt, nâng cao độ bền. Bắt buộc cho curtain wall, cửa sổ, mạch gạch. Bỏ qua gây rủi ro silicone bong và thấm nước.",
        "context": "실리콘 시공, 커튼월, 창호, 이음부, 방수",
        "culturalNote": "한국은 건축 시방서에 백업재 설치가 명시되어 있고, 시공 감리 시 필수 확인 사항이나, 베트남은 백업재 개념 자체가 생소하여 현장에서 생략되는 경우가 많습니다. 통역 시 한국의 '실리콘 수명 연장(kéo dài tuổi thọ silicone)' 효과를 강조하면 백업재의 필요성을 이해시킬 수 있습니다. 베트남에서는 'backer rod'라는 영어가 더 통용될 수 있으므로, 'foam lót(폼 패드)'라는 표현과 병기하세요.",
        "commonMistakes": [
            {
                "mistake": "백업 폼",
                "correction": "백업재 / 백업 로드",
                "explanation": "폼은 재질, 백업재가 정식 명칭"
            },
            {
                "mistake": "miếng đệm",
                "correction": "vật liệu lót / foam lót đáy",
                "explanation": "단순 패드가 아닌 시공 재료임을 명시 필요"
            },
            {
                "mistake": "실리콘 받침대",
                "correction": "백업재",
                "explanation": "받침대는 기능 설명, 전문 용어 사용 필요"
            }
        ],
        "examples": [
            {
                "ko": "실리콘 시공 전 백업재를 먼저 설치해야 합니다.",
                "vi": "Trước khi trám silicone phải lắp vật liệu lót trước.",
                "situation": "formal"
            },
            {
                "ko": "백업재는 이음부 깊이의 2/3 지점에 넣으세요.",
                "vi": "Đặt vật liệu lót ở vị trí 2/3 độ sâu mối nối.",
                "situation": "onsite"
            },
            {
                "ko": "백업재 없이 실리콘 치면 금방 떨어져요.",
                "vi": "Trám silicone không có lót sẽ nhanh bong.",
                "situation": "informal"
            }
        ],
        "relatedTerms": ["실리콘 시공", "커튼월", "창호", "실링", "방수"]
    },
    {
        "slug": "goc-treo",
        "korean": "브래킷",
        "vietnamese": "Gọc treo",
        "hanja": None,
        "hanjaReading": None,
        "pronunciation": "곡 째오",
        "meaningKo": "기계, 배관, 전선관, 조명 등을 벽체나 천장에 고정하기 위한 금속 지지대. 하중 계산과 앵커 시공이 중요하며, 시공 불량 시 탈락 사고 위험이 있습니다. 통역 시 베트남에서는 'bracket(브래킷)'이라는 영어가 널리 통용되나, 공식 용어로는 'gọc treo(걸이 지지대)' 또는 'giá đỡ(지지대)'를 사용하세요. 한국은 앵커 볼트 규격이 엄격하나, 베트남은 현장 재량이 크므로 안전 기준을 명확히 전달해야 합니다.",
        "meaningVi": "Giá đỡ kim loại dùng để cố định máy móc, ống, ống dây điện, đèn lên tường hoặc trần. Quan trọng là tính tải trọng và thi công neo. Thi công kém có nguy cơ rơi.",
        "context": "설비, 배관, 전기, 조명, 앵커",
        "culturalNote": "한국은 브래킷 설치 시 앵커 볼트 규격과 간격이 건축 시방서에 명시되어 있고, 시공 감리가 엄격하나, 베트남은 현장 경험에 의존하는 경우가 많아 안전 사고 위험이 높습니다. 통역 시 한국의 '하중 계산(tính toán tải trọng)' 및 '안전 계수(hệ số an toàn)' 개념을 설명하면 체계적 시공의 필요성을 이해시킬 수 있습니다. 베트남에서는 'bracket'이라는 영어가 매우 흔하므로, 병기하면 소통이 원활합니다.",
        "commonMistakes": [
            {
                "mistake": "받침대",
                "correction": "브래킷 / 지지 브래킷",
                "explanation": "일반 받침대가 아닌 전문 부품임을 명시 필요"
            },
            {
                "mistake": "giá đỡ thường",
                "correction": "gọc treo / bracket",
                "explanation": "일반 지지대가 아닌 고정용 금속 브래킷임을 명시 필요"
            },
            {
                "mistake": "걸이",
                "correction": "브래킷",
                "explanation": "단순 걸이가 아닌 구조적 지지대임을 명시 필요"
            }
        ],
        "examples": [
            {
                "ko": "배관 브래킷은 2m 간격으로 설치해야 합니다.",
                "vi": "Gọc treo ống phải lắp cách nhau 2m.",
                "situation": "formal"
            },
            {
                "ko": "브래킷 앵커는 콘크리트 깊이 80mm 이상 박으세요.",
                "vi": "Neo gọc treo phải đóng sâu trên 80mm vào bê tông.",
                "situation": "onsite"
            },
            {
                "ko": "천장 브래킷 추가로 10개 필요해요.",
                "vi": "Cần thêm 10 cái gọc treo trần.",
                "situation": "informal"
            }
        ],
        "relatedTerms": ["앵커", "배관", "지지대", "하중", "볼트"]
    },
    {
        "slug": "thi-cong-neo",
        "korean": "앵커 시공",
        "vietnamese": "Thi công neo",
        "hanja": None,
        "hanjaReading": None,
        "pronunciation": "티 꽁 네오",
        "meaningKo": "콘크리트나 벽돌에 구멍을 뚫고 앵커 볼트를 삽입하여 구조물이나 설비를 고정하는 공정. 하중 계산, 천공 깊이, 앵커 종류 선택이 중요하며, 시공 불량 시 탈락 사고가 발생합니다. 통역 시 베트남에서는 'anchor(앵커)'라는 영어가 널리 통용되나, 공식 용어로는 'neo cố định(고정 앵커)' 또는 'bu lông neo(앵커 볼트)'를 사용하세요. 한국은 앵커 종류가 용도별로 세분화되어 있으나, 베트남은 범용 제품이 주로 사용됩니다.",
        "meaningVi": "Công đoạn khoan lỗ vào bê tông hoặc gạch và lắp bu lông neo để cố định kết cấu hoặc thiết bị. Quan trọng là tính tải trọng, độ sâu khoan, chọn loại neo. Thi công kém gây tai nạn rơi.",
        "context": "고정, 브래킷, 설비, 하중, 볼트",
        "culturalNote": "한국은 앵커 시공 시 하중 계산과 안전 계수가 법적으로 규정되어 있고, 엔지니어 승인이 필요하나, 베트남은 현장 판단에 의존하는 경우가 많습니다. 통역 시 한국의 '인발 강도 시험(thử nghiệm độ bền kéo)' 개념을 설명하면 체계적 시공의 필요성을 이해시킬 수 있습니다. 베트남에서는 'anchor'라는 영어가 매우 흔하므로, 'neo' 또는 'bu lông neo'와 병기하면 소통이 원활합니다.",
        "commonMistakes": [
            {
                "mistake": "앵커 박기",
                "correction": "앵커 시공 / 앵커 설치",
                "explanation": "구어체가 아닌 전문 용어로 표현 필요"
            },
            {
                "mistake": "đóng neo",
                "correction": "thi công neo / lắp đặt bu lông neo",
                "explanation": "'박기'는 단순 표현, 시공 공정임을 명시 필요"
            },
            {
                "mistake": "볼트 박기",
                "correction": "앵커 시공 (앵커와 볼트 구분 설명)",
                "explanation": "앵커는 볼트와 다른 개념이므로 구분 필요"
            }
        ],
        "examples": [
            {
                "ko": "앵커 시공 전 하중 계산서를 제출해야 합니다.",
                "vi": "Trước khi thi công neo phải nộp bản tính tải trọng.",
                "situation": "formal"
            },
            {
                "ko": "앵커는 콘크리트 강도 확인 후 시공하세요.",
                "vi": "Thi công neo sau khi kiểm tra cường độ bê tông.",
                "situation": "onsite"
            },
            {
                "ko": "내일 천장 앵커 시공합니다.",
                "vi": "Mai thi công neo trần.",
                "situation": "informal"
            }
        ],
        "relatedTerms": ["브래킷", "볼트", "하중", "천공", "인발 강도"]
    }
]

# 파일 경로 (절대 경로)
file_path = os.path.join(
    os.path.expanduser("~"),
    "Documents",
    "claude_code",
    "projects",
    "vn.epicstage.co.kr",
    "src",
    "data",
    "terms",
    "construction.json"
)

def main():
    """메인 실행 함수"""
    # 기존 파일 읽기
    with open(file_path, "r", encoding="utf-8") as f:
        existing_data = json.load(f)

    print(f"기존 용어 수: {len(existing_data)}")

    # 새 용어 추가
    existing_data.extend(data)

    print(f"추가 후 용어 수: {len(existing_data)}")

    # 파일 저장 (들여쓰기 2칸, 유니코드 이스케이프 없이)
    with open(file_path, "w", encoding="utf-8") as f:
        json.dump(existing_data, f, ensure_ascii=False, indent=2)

    print(f"✅ {len(data)}개 용어 추가 완료: {file_path}")
    print("\n추가된 용어:")
    for term in data:
        print(f"  - {term['korean']} ({term['vietnamese']})")

if __name__ == "__main__":
    main()
