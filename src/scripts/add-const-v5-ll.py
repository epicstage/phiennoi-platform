#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
건설 용어 추가 스크립트 v5-ll
테마: 토목재료/지오텍스타일 (10개)
- 토목섬유, 지오그리드, 지오멤브레인, 가배수로, 토사유출방지
- 사방댐, 석축, 돌망태, 블록쌓기, 식생매트
품질: Tier S (90점 이상)
"""

import json
import os

# 추가할 용어 데이터 (10개)
new_terms = [
    {
        "slug": "tho-moc-xiem-du",
        "korean": "토목섬유",
        "vietnamese": "Vải địa kỹ thuật",
        "hanja": "土木纖維",
        "hanjaReading": "土(흙 토) + 木(나무 목) + 纖(가늘 섬) + 維(벌레 유)",
        "pronunciation": "토목서무",
        "meaningKo": "지반 보강, 배수, 분리, 여과 등의 목적으로 사용되는 합성섬유 재료입니다. 도로, 제방, 옹벽 등 다양한 토목 구조물에 사용되며, 통역 시 '지오텍스타일(geotextile)'과 혼용되므로 맥락을 명확히 해야 합니다. 베트남에서는 'Vải địa kỹ thuật' 또는 'Vải không dệt kỹ thuật'으로 표현하며, 품질 규격(TCVN 등)을 함께 언급하는 것이 중요합니다.",
        "meaningVi": "Vải địa kỹ thuật là vật liệu tổng hợp được sử dụng để gia cố nền đất, thoát nước, phân tách và lọc trong các công trình xây dựng như đường, đê, tường chắn. Cần phân biệt rõ loại vải dệt (woven) và không dệt (non-woven) khi thông dịch.",
        "context": "지반 보강 공사, 도로 포장, 제방 보호, 옹벽 배수 시공 등에서 사용",
        "culturalNote": "한국에서는 '토목섬유' 또는 '지오텍스타일'로 혼용하지만, 베트남에서는 'Vải địa kỹ thuật'가 공식 용어입니다. 한국은 KS 규격, 베트남은 TCVN 규격을 따르므로, 품질 인증 기준이 다릅니다. 현장에서는 '짚신(chiếu)', '매트(thảm)'로 불리기도 하므로 주의가 필요합니다.",
        "commonMistakes": [
            {
                "mistake": "토목섬유를 'Vải dệt'로만 번역",
                "correction": "'Vải địa kỹ thuật' 또는 'Geotextile'",
                "explanation": "'Vải dệt'은 일반 직물을 의미하며, 토목용 기술 섬유는 'Vải địa kỹ thuật'으로 표현해야 합니다."
            },
            {
                "mistake": "지오텍스타일과 지오그리드를 혼동",
                "correction": "토목섬유(Vải)와 지오그리드(Lưới)는 구조와 용도가 다름",
                "explanation": "토목섬유는 직조/부직포 형태이고, 지오그리드는 격자 구조입니다. 용도가 다르므로 구분이 필수입니다."
            },
            {
                "mistake": "품질 등급을 명시하지 않음",
                "correction": "강도(kN/m), 투수성(mm/s) 등 규격 포함",
                "explanation": "토목섬유는 용도에 따라 강도와 투수성이 다르므로, 규격을 명확히 해야 시공 오류를 방지할 수 있습니다."
            }
        ],
        "examples": [
            {
                "ko": "부직포 토목섬유를 노반과 노상 사이에 포설하여 분리층을 형성합니다.",
                "vi": "Trải vải địa kỹ thuật không dệt giữa nền đường và lớp móng để tạo lớp phân tách.",
                "situation": "onsite"
            },
            {
                "ko": "이 구간은 지오텍스타일 200g/㎡ 규격으로 시공하겠습니다.",
                "vi": "Khu vực này sẽ thi công bằng vải địa kỹ thuật quy cách 200g/m².",
                "situation": "formal"
            },
            {
                "ko": "토목섬유가 찢어졌으니 즉시 교체해야 합니다.",
                "vi": "Vải địa kỹ thuật bị rách, cần thay thế ngay.",
                "situation": "onsite"
            }
        ],
        "relatedTerms": ["지오그리드", "지오멤브레인", "부직포", "노상", "노반", "분리층"]
    },
    {
        "slug": "gio-grid",
        "korean": "지오그리드",
        "vietnamese": "Lưới địa kỹ thuật",
        "hanja": None,
        "hanjaReading": None,
        "pronunciation": "지오그리드",
        "meaningKo": "격자형 구조의 합성수지 재료로, 지반 보강 및 인장력 증대를 위해 사용됩니다. 도로 노상, 성토부, 옹벽 뒷채움 등에 적용되며, 통역 시 '토목섬유'와 혼동하지 않도록 주의해야 합니다. 베트남에서는 'Lưới địa kỹ thuật' 또는 'Geogrid'로 표현하며, 단축(uniaxial)과 쌍축(biaxial) 종류를 구분하는 것이 중요합니다.",
        "meaningVi": "Lưới địa kỹ thuật là vật liệu tổng hợp có cấu trúc lưới giúp gia cố nền đất và tăng sức chịu kéo. Được sử dụng trong đường, đắp đất, tường chắn. Cần phân biệt loại một trục (uniaxial) và hai trục (biaxial) khi thông dịch.",
        "context": "지반 보강, 성토 시공, 옹벽 배면, 경사면 안정화 등에서 사용",
        "culturalNote": "한국에서는 '지오그리드'로 외래어 표기하지만, 베트남에서는 'Lưới địa kỹ thuật' 또는 'Geogrid'를 혼용합니다. 한국 현장에서는 '그리드', '격자망'으로도 불리며, 베트남에서는 'Lưới nhựa(플라스틱 망)'로 오해받을 수 있으므로 'địa kỹ thuật(지반공학용)'을 강조해야 합니다.",
        "commonMistakes": [
            {
                "mistake": "지오그리드를 'Lưới sắt(철망)'로 번역",
                "correction": "'Lưới địa kỹ thuật' 또는 'Geogrid'",
                "explanation": "'Lưới sắt'은 철망을 의미하며, 지오그리드는 합성수지 재료이므로 혼동하면 안 됩니다."
            },
            {
                "mistake": "단축과 쌍축을 구분하지 않음",
                "correction": "Lưới một trục / Lưới hai trục",
                "explanation": "단축(uniaxial)은 한 방향, 쌍축(biaxial)은 양방향 보강이므로, 용도에 따라 명확히 구분해야 합니다."
            },
            {
                "mistake": "토목섬유와 혼동",
                "correction": "토목섬유(Vải)는 섬유, 지오그리드(Lưới)는 격자",
                "explanation": "구조와 용도가 다르므로, 명확히 구분하여 통역해야 시공 오류를 방지할 수 있습니다."
            }
        ],
        "examples": [
            {
                "ko": "쌍축 지오그리드를 150mm 간격으로 포설하겠습니다.",
                "vi": "Sẽ trải lưới địa kỹ thuật hai trục với khoảng cách 150mm.",
                "situation": "onsite"
            },
            {
                "ko": "이 구간은 지오그리드로 지반을 보강해야 합니다.",
                "vi": "Khu vực này cần gia cố nền đất bằng lưới địa kỹ thuật.",
                "situation": "formal"
            },
            {
                "ko": "지오그리드가 파손되었으니 즉시 교체하세요.",
                "vi": "Lưới địa kỹ thuật bị hỏng, cần thay thế ngay.",
                "situation": "onsite"
            }
        ],
        "relatedTerms": ["토목섬유", "지오멤브레인", "지반보강", "성토", "옹벽", "노상"]
    },
    {
        "slug": "gio-membrane",
        "korean": "지오멤브레인",
        "vietnamese": "Màng địa kỹ thuật",
        "hanja": None,
        "hanjaReading": None,
        "pronunciation": "지오멤브레인",
        "meaningKo": "불투수성 합성수지 막으로, 차수 및 방수를 목적으로 사용됩니다. 매립지 차수층, 저수지 차수막, 터널 방수 등에 적용되며, 통역 시 '방수막'과 구분이 필요합니다. 베트남에서는 'Màng địa kỹ thuật' 또는 'Geomembrane'으로 표현하며, 두께(mm)와 재질(HDPE, PVC 등)을 명확히 해야 합니다.",
        "meaningVi": "Màng địa kỹ thuật là màng tổng hợp không thấm nước dùng để chống thấm và ngăn nước trong các công trình như bãi chôn lấp, hồ chứa, hầm. Cần nêu rõ độ dày (mm) và chất liệu (HDPE, PVC) khi thông dịch.",
        "context": "매립지 차수, 저수지 방수, 터널 차수, 연못 차수 등에서 사용",
        "culturalNote": "한국에서는 '지오멤브레인' 또는 '차수막'으로 불리지만, 베트남에서는 'Màng địa kỹ thuật' 또는 'Màng chống thấm(방수막)'으로 표현합니다. 한국은 HDPE(고밀도 폴리에틸렌)를 주로 사용하고, 베트남에서는 PVC도 흔히 사용되므로, 재질을 명확히 해야 합니다.",
        "commonMistakes": [
            {
                "mistake": "지오멤브레인을 'Màng nhựa(비닐막)'로 번역",
                "correction": "'Màng địa kỹ thuật' 또는 'Geomembrane'",
                "explanation": "'Màng nhựa'는 일반 비닐막을 의미하며, 지오멤브레인은 고강도 차수용 재료이므로 구분이 필수입니다."
            },
            {
                "mistake": "재질과 두께를 명시하지 않음",
                "correction": "HDPE 1.5mm, PVC 2.0mm 등 구체적으로 표기",
                "explanation": "재질과 두께에 따라 차수 성능과 시공 방법이 다르므로, 반드시 명시해야 합니다."
            },
            {
                "mistake": "방수막과 혼동",
                "correction": "일반 방수막(Màng chống thấm)과 구분",
                "explanation": "지오멤브레인은 토목용 고강도 차수막이므로, 일반 건축용 방수막과는 용도가 다릅니다."
            }
        ],
        "examples": [
            {
                "ko": "HDPE 지오멤브레인 1.5mm를 매립지 바닥에 포설합니다.",
                "vi": "Trải màng địa kỹ thuật HDPE 1.5mm tại đáy bãi chôn lấp.",
                "situation": "onsite"
            },
            {
                "ko": "이 저수지는 지오멤브레인으로 차수 처리가 필요합니다.",
                "vi": "Hồ chứa này cần xử lý chống thấm bằng màng địa kỹ thuật.",
                "situation": "formal"
            },
            {
                "ko": "지오멤브레인 이음부를 융착기로 접합하겠습니다.",
                "vi": "Sẽ hàn nối mối ghép màng địa kỹ thuật bằng máy hàn nhiệt.",
                "situation": "onsite"
            }
        ],
        "relatedTerms": ["차수층", "방수막", "매립지", "저수지", "터널", "HDPE"]
    },
    {
        "slug": "ga-bae-su-ro",
        "korean": "가배수로",
        "vietnamese": "Rãnh thoát nước tạm",
        "hanja": "假排水路",
        "hanjaReading": "假(거짓 가) + 排(물리칠 배) + 水(물 수) + 路(길 로)",
        "pronunciation": "가배수로",
        "meaningKo": "공사 중 우수나 지하수를 임시로 배제하기 위해 설치하는 배수로입니다. 토공사, 터파기, 터널 공사 등에서 필수적이며, 통역 시 '영구 배수로'와 구분이 중요합니다. 베트남에서는 'Rãnh thoát nước tạm' 또는 'Mương thoát nước tạm thời'로 표현하며, 경사와 배수 용량을 명확히 해야 합니다.",
        "meaningVi": "Rãnh thoát nước tạm là hệ thống thoát nước lắp đặt tạm thời trong quá trình thi công để loại bỏ nước mưa và nước ngầm. Cần phân biệt với hệ thống thoát nước vĩnh viễn khi thông dịch.",
        "context": "토공사, 터파기, 터널 공사, 성토 공사 등에서 임시 배수를 위해 사용",
        "culturalNote": "한국에서는 '가배수로' 또는 '임시 배수로'로 불리며, 베트남에서는 'Rãnh tạm(임시 배수로)' 또는 'Mương tạm'으로 표현합니다. 한국은 PVC관이나 콘크리트 U형관을 주로 사용하고, 베트nam에서는 흙배수로나 대나무 배수로도 흔하므로, 시공 방법을 명확히 해야 합니다.",
        "commonMistakes": [
            {
                "mistake": "가배수로를 'Rãnh vĩnh viễn(영구 배수로)'로 번역",
                "correction": "'Rãnh thoát nước tạm' 또는 'Rãnh tạm thời'",
                "explanation": "가배수로는 임시 시설이므로, '영구(vĩnh viễn)'가 아닌 '임시(tạm)'로 표현해야 합니다."
            },
            {
                "mistake": "배수 용량을 명시하지 않음",
                "correction": "배수 용량(m³/h), 경사(%) 등 구체적으로 표기",
                "explanation": "배수 용량과 경사에 따라 배수로 규격이 결정되므로, 반드시 명시해야 합니다."
            },
            {
                "mistake": "측구(側溝)와 혼동",
                "correction": "측구(Rãnh bên đường)는 영구 시설",
                "explanation": "측구는 도로 영구 배수 시설이고, 가배수로는 공사 중 임시 시설이므로 구분이 필수입니다."
            }
        ],
        "examples": [
            {
                "ko": "터파기 전에 가배수로를 먼저 설치하겠습니다.",
                "vi": "Trước khi đào đất, sẽ lắp đặt rãnh thoát nước tạm trước.",
                "situation": "onsite"
            },
            {
                "ko": "이 구간 가배수로는 경사 2%로 시공합니다.",
                "vi": "Rãnh thoát nước tạm ở khu vực này thi công với độ dốc 2%.",
                "situation": "formal"
            },
            {
                "ko": "비 오니까 가배수로 막혔나 확인해 보세요.",
                "vi": "Trời mưa rồi, kiểm tra xem rãnh tạm có bị tắc không.",
                "situation": "onsite"
            }
        ],
        "relatedTerms": ["배수로", "측구", "터파기", "토공사", "집수정", "우수"]
    },
    {
        "slug": "tho-sa-yu-chul-bang-ji",
        "korean": "토사유출방지",
        "vietnamese": "Ngăn chặn rò rỉ đất cát",
        "hanja": "土砂流出防止",
        "hanjaReading": "土(흙 토) + 砂(모래 사) + 流(흐를 류) + 出(날 출) + 防(막을 방) + 止(그칠 지)",
        "pronunciation": "토사유출방지",
        "meaningKo": "공사 중 비나 지하수로 인해 토사가 외부로 유출되는 것을 방지하는 조치입니다. 침사지, 토사펜스, 가배수로 등이 포함되며, 통역 시 환경 규제와 연계하여 설명해야 합니다. 베트남에서는 'Ngăn chặn rò rỉ đất cát' 또는 'Kiểm soát xói mòn'으로 표현하며, 환경 보호 규정을 준수하는 것이 중요합니다.",
        "meaningVi": "Ngăn chặn rò rỉ đất cát là các biện pháp ngăn đất cát bị cuốn trôi ra ngoài trong quá trình thi công do mưa hoặc nước ngầm. Bao gồm bể lắng, hàng rào chặn bùn cát, rãnh thoát nước tạm. Cần tuân thủ quy định bảo vệ môi trường.",
        "context": "토공사, 절토, 성토, 하천 인근 공사 등에서 환경 보호를 위해 필수적으로 시행",
        "culturalNote": "한국에서는 '토사유출방지' 또는 '토사펜스', '침사지' 등으로 표현하며, 베트남에서는 'Ngăn chặn xói mòn(침식 방지)' 또는 'Kiểm soát bùn cát(토사 제어)'로 불립니다. 한국은 환경부 규정(토양환경보전법)을 따르고, 베트남은 자원환경부(MONRE) 규정을 따르므로, 법규 준수를 강조해야 합니다.",
        "commonMistakes": [
            {
                "mistake": "토사유출방지를 'Chống lũ(홍수 방지)'로 번역",
                "correction": "'Ngăn chặn rò rỉ đất cát' 또는 'Kiểm soát xói mòn'",
                "explanation": "홍수 방지(Chống lũ)와 토사 유출 방지는 목적이 다르므로, 명확히 구분해야 합니다."
            },
            {
                "mistake": "침사지와 집수정을 혼동",
                "correction": "침사지(Bể lắng cát)는 토사 침전, 집수정(Hố thu nước)은 물 모으기",
                "explanation": "침사지는 토사를 가라앉히고, 집수정은 물을 모으는 시설이므로 용도가 다릅니다."
            },
            {
                "mistake": "환경 규제를 언급하지 않음",
                "correction": "환경 보호 규정 준수 필수임을 명시",
                "explanation": "토사 유출은 환경 오염 문제로 이어지므로, 법규 준수를 강조해야 과태료를 피할 수 있습니다."
            }
        ],
        "examples": [
            {
                "ko": "토사유출방지를 위해 침사지와 토사펜스를 설치하겠습니다.",
                "vi": "Để ngăn chặn rò rỉ đất cát, sẽ lắp đặt bể lắng và hàng rào chặn bùn cát.",
                "situation": "formal"
            },
            {
                "ko": "비 오기 전에 토사펜스 점검하세요.",
                "vi": "Trước khi mưa, kiểm tra hàng rào chặn bùn cát.",
                "situation": "onsite"
            },
            {
                "ko": "이 구간은 하천 인근이라 토사유출방지 조치를 철저히 해야 합니다.",
                "vi": "Khu vực này gần sông nên phải thực hiện nghiêm túc biện pháp ngăn chặn rò rỉ đất cát.",
                "situation": "formal"
            }
        ],
        "relatedTerms": ["침사지", "토사펜스", "가배수로", "집수정", "환경보호", "침식"]
    },
    {
        "slug": "sa-bang-dam",
        "korean": "사방댐",
        "vietnamese": "Đập chắn cát đá",
        "hanja": "砂防댐",
        "hanjaReading": "砂(모래 사) + 防(막을 방) + 댐(외래어)",
        "pronunciation": "사방댐",
        "meaningKo": "산간 계곡에 설치하여 토석류나 토사의 유출을 방지하는 소형 댐입니다. 산사태 예방, 하상 안정화, 토사 유출 방지 등의 목적으로 사용되며, 통역 시 '일반 댐'과 구분이 필요합니다. 베트남에서는 'Đập chắn cát đá' 또는 'Đập phòng chống lũ bùn đá'로 표현하며, 산지 보호 사업과 연계하여 설명해야 합니다.",
        "meaningVi": "Đập chắn cát đá là đập nhỏ xây dựng tại khe suối miền núi để ngăn chặn dòng bùn đá và đất cát trôi ra. Có mục đích phòng chống sạt lở, ổn định lòng suối, ngăn chặn xói mòn. Cần phân biệt với đập thủy điện thông thường.",
        "context": "산간 계곡, 급경사 지역, 산사태 위험 지역 등에서 사용",
        "culturalNote": "한국에서는 '사방댐'으로 통칭하며, 베트남에서는 'Đập chắn cát đá(토사 차단 댐)' 또는 'Đập sabo(사보 댐)'로 불립니다. 한국은 산림청 사방 사업으로 관리하고, 베트남은 농업농촌개발부가 관할하므로, 담당 기관을 명확히 해야 합니다. '사방(砂防)'은 일본어 유래 용어이므로 베트남에서는 직역보다 기능을 설명하는 것이 효과적입니다.",
        "commonMistakes": [
            {
                "mistake": "사방댐을 'Đập thủy điện(수력발전댐)'로 번역",
                "correction": "'Đập chắn cát đá' 또는 'Đập phòng chống lũ bùn đá'",
                "explanation": "수력발전댐은 전기 생산용이고, 사방댐은 토사 유출 방지용이므로 목적이 다릅니다."
            },
            {
                "mistake": "규모를 명시하지 않음",
                "correction": "소형 댐(높이 10m 이하)임을 명시",
                "explanation": "사방댐은 소형 구조물이므로, 대형 댐과 혼동하지 않도록 규모를 명확히 해야 합니다."
            },
            {
                "mistake": "토석류(土石流)와 토사류(土砂流)를 구분하지 않음",
                "correction": "토석류(Lũ bùn đá), 토사류(Lũ bùn cát)",
                "explanation": "토석류는 돌과 흙, 토사류는 흙과 모래이므로, 댐 설계 시 구분이 필요합니다."
            }
        ],
        "examples": [
            {
                "ko": "이 계곡에는 높이 8m 사방댐을 설치하겠습니다.",
                "vi": "Tại khe suối này sẽ xây dựng đập chắn cát đá cao 8m.",
                "situation": "formal"
            },
            {
                "ko": "사방댐 덕분에 하류 마을이 토석류 피해를 면했습니다.",
                "vi": "Nhờ đập chắn cát đá, làng hạ du tránh được thiệt hại do lũ bùn đá.",
                "situation": "informal"
            },
            {
                "ko": "사방댐 퇴사(淤砂) 제거 작업을 진행하겠습니다.",
                "vi": "Sẽ tiến hành công tác nạo vét cát đá tích tụ tại đập.",
                "situation": "onsite"
            }
        ],
        "relatedTerms": ["토석류", "산사태", "계곡", "토사유출", "침식", "사면"]
    },
    {
        "slug": "seok-chuk",
        "korean": "석축",
        "vietnamese": "Tường đá xây",
        "hanja": "石築",
        "hanjaReading": "石(돌 석) + 築(쌓을 축)",
        "pronunciation": "석축",
        "meaningKo": "돌을 쌓아 만든 옹벽이나 제방 구조물입니다. 도로 절개지, 하천 호안, 경사면 보호 등에 사용되며, 통역 시 '콘크리트 옹벽'과 구분이 필요합니다. 베트남에서는 'Tường đá xây' 또는 'Tường chắn đá'로 표현하며, 쌓기 방식(찰쌓기/메쌓기)을 명확히 해야 합니다.",
        "meaningVi": "Tường đá xây là kết cấu tường hoặc đê được xây dựng bằng cách chồng đá. Sử dụng trong bảo vệ taluy đường, kè sông, gia cố sườn dốc. Cần phân biệt với tường bê tông và nêu rõ phương pháp xây (xây khô/xây vữa).",
        "context": "도로 절개지, 하천 제방, 산지 경사면 보호, 옹벽 등에서 사용",
        "culturalNote": "한국에서는 '석축' 또는 '돌쌓기'로 불리며, 베트남에서는 'Tường đá(돌벽)' 또는 'Kè đá(돌 호안)'로 표현합니다. 한국은 찰쌓기(모르타르 사용)가 주류이고, 베트남에서는 메쌓기(모르타르 없이 쌓기)도 흔하므로, 시공 방법을 명확히 해야 합니다. '석축'은 전통 토목 용어로, 현대에는 '돌쌓기 옹벽'으로도 표현됩니다.",
        "commonMistakes": [
            {
                "mistake": "석축을 'Tường bê tông(콘크리트 옹벽)'로 번역",
                "correction": "'Tường đá xây' 또는 'Tường chắn đá'",
                "explanation": "콘크리트 옹벽과 석축은 재료가 다르므로, 명확히 구분해야 합니다."
            },
            {
                "mistake": "찰쌓기와 메쌓기를 구분하지 않음",
                "correction": "찰쌓기(Xây vữa), 메쌓기(Xây khô)",
                "explanation": "찰쌓기는 모르타르를 사용하고, 메쌓기는 사용하지 않으므로 시공 방법이 다릅니다."
            },
            {
                "mistake": "호안(護岸)과 혼동",
                "correction": "석축(Tường đá)은 옹벽, 호안(Kè)은 하천 보호",
                "explanation": "석축은 일반적인 돌쌓기 옹벽이고, 호안은 하천 보호 시설이므로 용도에 따라 구분이 필요합니다."
            }
        ],
        "examples": [
            {
                "ko": "이 구간은 석축으로 옹벽을 축조하겠습니다.",
                "vi": "Khu vực này sẽ xây dựng tường chắn bằng tường đá xây.",
                "situation": "formal"
            },
            {
                "ko": "석축 기초를 콘크리트로 보강해야 합니다.",
                "vi": "Cần gia cố móng tường đá bằng bê tông.",
                "situation": "onsite"
            },
            {
                "ko": "찰쌓기로 석축을 시공하니 안정성이 높습니다.",
                "vi": "Thi công tường đá bằng phương pháp xây vữa nên độ ổn định cao.",
                "situation": "informal"
            }
        ],
        "relatedTerms": ["옹벽", "호안", "절개지", "찰쌓기", "메쌓기", "제방"]
    },
    {
        "slug": "dol-mang-tae",
        "korean": "돌망태",
        "vietnamese": "Rọ đá",
        "hanja": None,
        "hanjaReading": None,
        "pronunciation": "돌망태",
        "meaningKo": "철망이나 철선으로 만든 망에 돌을 채워 사용하는 토목 구조물입니다. 하천 호안, 사면 보호, 옹벽 등에 적용되며, 통역 시 '가비온(gabion)'과 같은 의미입니다. 베트남에서는 'Rọ đá' 또는 'Giỏ đá'로 표현하며, 철망 규격(mm)과 돌의 크기를 명확히 해야 합니다.",
        "meaningVi": "Rọ đá là kết cấu làm bằng lưới thép hoặc dây thép chứa đầy đá, dùng trong kè sông, bảo vệ taluy, tường chắn. Cần nêu rõ quy cách lưới (mm) và kích thước đá khi thông dịch.",
        "context": "하천 호안, 산지 사면 보호, 옹벽, 제방 등에서 사용",
        "culturalNote": "한국에서는 '돌망태' 또는 '가비온(gabion)'으로 불리며, 베트남에서는 'Rọ đá(돌 바구니)' 또는 'Giỏ đá'로 표현합니다. 한국은 아연도금 철망을 주로 사용하고, 베트남에서는 PVC 코팅 철망도 흔히 사용되므로, 부식 방지 처리를 명확히 해야 합니다. '돌망태'는 순우리말이므로 베트남어로 직역이 어렵고, 기능을 설명하는 것이 효과적입니다.",
        "commonMistakes": [
            {
                "mistake": "돌망태를 'Giỏ sắt(철 바구니)'로 번역",
                "correction": "'Rọ đá' 또는 'Gabion'",
                "explanation": "'Giỏ sắt'은 철 바구니 일반을 의미하며, 돌망태는 토목용 구조물이므로 'Rọ đá'로 표현해야 합니다."
            },
            {
                "mistake": "철망 규격을 명시하지 않음",
                "correction": "철망 규격(8mm, 10mm 등) 및 부식 방지 처리 명시",
                "explanation": "철망 규격과 부식 방지 처리에 따라 내구성이 달라지므로, 반드시 명시해야 합니다."
            },
            {
                "mistake": "석축과 혼동",
                "correction": "석축(Tường đá xây)은 쌓기, 돌망태(Rọ đá)는 망 사용",
                "explanation": "석축은 돌을 쌓고, 돌망태는 철망에 돌을 채우므로 시공 방법이 다릅니다."
            }
        ],
        "examples": [
            {
                "ko": "하천 호안에 돌망태를 설치하겠습니다.",
                "vi": "Sẽ lắp đặt rọ đá tại kè sông.",
                "situation": "onsite"
            },
            {
                "ko": "이 구간은 가비온으로 사면을 보호합니다.",
                "vi": "Khu vực này bảo vệ taluy bằng rọ đá.",
                "situation": "formal"
            },
            {
                "ko": "돌망태 철망이 부식되었으니 교체하세요.",
                "vi": "Lưới rọ đá bị gỉ, cần thay thế.",
                "situation": "onsite"
            }
        ],
        "relatedTerms": ["가비온", "호안", "석축", "사면보호", "철망", "하천"]
    },
    {
        "slug": "block-ssah-gi",
        "korean": "블록쌓기",
        "vietnamese": "Xây khối bê tông",
        "hanja": None,
        "hanjaReading": None,
        "pronunciation": "블록쌓기",
        "meaningKo": "콘크리트 블록을 쌓아 옹벽이나 제방을 축조하는 공법입니다. 도로 절개지, 하천 호안, 산지 사면 등에 사용되며, 통역 시 블록 종류(일반 블록, 식생 블록, 연결 블록 등)를 명확히 해야 합니다. 베트남에서는 'Xây khối bê tông' 또는 'Xếp block'으로 표현하며, 블록 규격과 결속 방법을 구체적으로 설명해야 합니다.",
        "meaningVi": "Xây khối bê tông là phương pháp xây dựng tường chắn hoặc đê bằng cách chồng các khối bê tông đúc sẵn. Sử dụng trong taluy đường, kè sông, sườn dốc. Cần nêu rõ loại khối (thường, trồng cỏ, liên kết) và quy cách khi thông dịch.",
        "context": "도로 절개지, 하천 호안, 산지 사면, 옹벽 등에서 사용",
        "culturalNote": "한국에서는 '블록쌓기' 또는 '블록 옹벽'으로 불리며, 베트남에서는 'Xây block(블록 쌓기)' 또는 'Tường block'으로 표현합니다. 한국은 식생 블록(잔디 블록)을 친환경 공법으로 선호하고, 베트남에서는 일반 콘크리트 블록이 주류이므로, 블록 종류를 명확히 해야 합니다. '블록'은 외래어이므로 베트남어로도 'Block'으로 통용됩니다.",
        "commonMistakes": [
            {
                "mistake": "블록쌓기를 'Xây gạch(벽돌쌓기)'로 번역",
                "correction": "'Xây khối bê tông' 또는 'Xây block'",
                "explanation": "벽돌(gạch)과 콘크리트 블록(block)은 재료와 규격이 다르므로, 구분이 필수입니다."
            },
            {
                "mistake": "블록 종류를 명시하지 않음",
                "correction": "일반 블록(Block thường), 식생 블록(Block trồng cỏ) 등 구분",
                "explanation": "블록 종류에 따라 용도와 시공 방법이 다르므로, 반드시 명시해야 합니다."
            },
            {
                "mistake": "석축과 혼동",
                "correction": "석축(Tường đá)은 자연석, 블록쌓기(Xây block)는 콘크리트 블록",
                "explanation": "재료가 다르므로, 명확히 구분하여 통역해야 시공 오류를 방지할 수 있습니다."
            }
        ],
        "examples": [
            {
                "ko": "이 구간은 식생 블록쌓기로 옹벽을 시공하겠습니다.",
                "vi": "Khu vực này sẽ thi công tường chắn bằng xây khối bê tông trồng cỏ.",
                "situation": "formal"
            },
            {
                "ko": "블록 간격을 10mm로 유지하며 쌓으세요.",
                "vi": "Giữ khoảng cách giữa các khối là 10mm khi xếp.",
                "situation": "onsite"
            },
            {
                "ko": "연결 블록으로 사면을 보호하니 안정성이 높습니다.",
                "vi": "Bảo vệ taluy bằng khối liên kết nên độ ổn định cao.",
                "situation": "informal"
            }
        ],
        "relatedTerms": ["옹벽", "식생블록", "연결블록", "석축", "사면보호", "절개지"]
    },
    {
        "slug": "sik-saeng-mat",
        "korean": "식생매트",
        "vietnamese": "Thảm thực vật",
        "hanja": "植生mat",
        "hanjaReading": "植(심을 식) + 生(날 생) + mat(외래어)",
        "pronunciation": "식생매트",
        "meaningKo": "사면이나 비탈면에 식물이 자랄 수 있도록 돕는 매트형 자재입니다. 침식 방지, 경관 개선, 녹화 촉진 등의 목적으로 사용되며, 통역 시 재질(코코넛 섬유, 짚, 합성섬유 등)을 명확히 해야 합니다. 베트남에서는 'Thảm thực vật' 또는 'Thảm xanh hóa'로 표현하며, 기후와 토질에 맞는 종자 선택이 중요합니다.",
        "meaningVi": "Thảm thực vật là vật liệu dạng thảm giúp cây trồng phát triển trên taluy hoặc sườn dốc. Có mục đích chống xói mòn, cải thiện cảnh quan, thúc đẩy phủ xanh. Cần nêu rõ chất liệu (xơ dừa, rơm, sợi tổng hợp) và hạt giống phù hợp với khí hậu, đất đai.",
        "context": "도로 사면, 제방, 산지 경사면, 절토 비탈면 등에서 녹화 및 침식 방지를 위해 사용",
        "culturalNote": "한국에서는 '식생매트' 또는 '녹화매트'로 불리며, 베트남에서는 'Thảm thực vật(식물 매트)' 또는 'Thảm phủ xanh(녹화 매트)'로 표현합니다. 한국은 코코넛 섬유나 짚 매트를 주로 사용하고, 베트남에서는 야자 섬유나 합성섬유도 흔히 사용되므로, 재질과 내구성을 명확히 해야 합니다. '매트(mat)'는 외래어이므로 베트남어로도 'Mat'으로 통용되기도 합니다.",
        "commonMistakes": [
            {
                "mistake": "식생매트를 'Thảm nhựa(비닐 매트)'로 번역",
                "correction": "'Thảm thực vật' 또는 'Thảm xanh hóa'",
                "explanation": "'Thảm nhựa'는 비닐 매트를 의미하며, 식생매트는 식물 생장용이므로 구분이 필수입니다."
            },
            {
                "mistake": "재질과 종자를 명시하지 않음",
                "correction": "코코넛 섬유(Xơ dừa), 짚(Rơm) + 잔디 종자(Hạt cỏ) 등 구체적으로 표기",
                "explanation": "재질과 종자에 따라 녹화 효과와 내구성이 다르므로, 반드시 명시해야 합니다."
            },
            {
                "mistake": "토목섬유와 혼동",
                "correction": "토목섬유(Vải địa kỹ thuật)는 보강용, 식생매트(Thảm thực vật)는 녹화용",
                "explanation": "토목섬유는 지반 보강이고, 식생매트는 식물 생장 촉진이므로 용도가 다릅니다."
            }
        ],
        "examples": [
            {
                "ko": "절토 비탈면에 코코넛 섬유 식생매트를 포설하겠습니다.",
                "vi": "Sẽ trải thảm thực vật xơ dừa trên taluy cắt đất.",
                "situation": "onsite"
            },
            {
                "ko": "이 구간은 식생매트로 녹화하여 경관을 개선합니다.",
                "vi": "Khu vực này phủ xanh bằng thảm thực vật để cải thiện cảnh quan.",
                "situation": "formal"
            },
            {
                "ko": "식생매트에 잔디가 잘 자라고 있습니다.",
                "vi": "Cỏ đang phát triển tốt trên thảm thực vật.",
                "situation": "informal"
            }
        ],
        "relatedTerms": ["녹화", "사면보호", "침식방지", "토목섬유", "비탈면", "잔디"]
    }
]

# 파일 경로
construction_file = os.path.join(
    os.path.dirname(__file__),
    "..",
    "data",
    "terms",
    "construction.json"
)

def main():
    """기존 construction.json에 10개 용어 추가"""
    # 기존 데이터 로드
    with open(construction_file, "r", encoding="utf-8") as f:
        data = json.load(f)

    # 새 용어 추가
    data.extend(new_terms)

    # 저장 (들여쓰기 2칸, 한글 유지)
    with open(construction_file, "w", encoding="utf-8") as f:
        json.dump(data, f, ensure_ascii=False, indent=2)

    print(f"✅ {len(new_terms)}개 용어 추가 완료")
    print(f"📂 파일: {construction_file}")
    print(f"📊 총 용어 수: {len(data)}개")

if __name__ == "__main__":
    main()
