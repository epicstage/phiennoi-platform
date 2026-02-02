#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
항만/해양건설 테마 건설 용어 10개 추가 스크립트
Tier S 기준 준수 (90점 이상)
"""

import json
import os

# 추가할 용어 데이터 (10개)
data = [
    {
        "slug": "caisson",
        "korean": "케이슨",
        "vietnamese": "Caisson",
        "hanja": None,
        "hanjaReading": None,
        "pronunciation": "케이슨",
        "meaningKo": "항만 공사에서 사용하는 대형 콘크리트 상자 구조물로, 육상에서 제작 후 바다에 띄워 목적지로 예인해 가라앉혀 안벽이나 방파제의 본체로 사용합니다. 통역 시 '케이슨 거치', '케이슨 침설' 등 공정 용어와 함께 사용되며, 베트남어로는 프랑스어 유래 단어로 그대로 Caisson이라 하므로 발음 주의가 필요합니다. 크기와 중량 단위(톤, m³)를 정확히 전달하는 것이 중요합니다.",
        "meaningVi": "Cấu trúc hộp bê tông lớn được sử dụng trong xây dựng cảng, được chế tạo trên bờ sau đó thả nổi trên biển, kéo đến vị trí và chìm xuống để làm thân chính của bờ kè hoặc đê chắn sóng. Là công trình quan trọng trong xây dựng hải cảng.",
        "context": "항만/해양건설",
        "culturalNote": "한국은 프리캐스트 케이슨 공법이 발달했으나 베트남은 상대적으로 현장타설 방식을 많이 사용합니다. 케이슨 제작 야드의 규모와 장비(플로팅 크레인) 수준에서 차이가 있으며, 한국 기술진은 대형화·표준화된 케이슨 시공에 익숙한 반면 베트남 현지 인력은 소규모 단위 시공 경험이 많아 공법 설명 시 세심한 통역이 필요합니다.",
        "commonMistakes": [
            {
                "mistake": "Caisson을 '박스'로 번역",
                "correction": "케이슨(고유명사로 유지)",
                "explanation": "케이슨은 공법명이자 구조물명으로 번역 없이 그대로 사용해야 합니다."
            },
            {
                "mistake": "침설과 거치를 혼용",
                "correction": "침설은 물속에 가라앉히는 것, 거치는 정확한 위치에 설치하는 것",
                "explanation": "침설(chìm xuống)과 거치(đặt vào vị trí)는 공정이 다릅니다."
            },
            {
                "mistake": "중량을 부피로 혼동",
                "correction": "케이슨 중량(톤)과 용적(m³)을 구분",
                "explanation": "설계 시 중량과 부력 계산이 다르므로 단위를 정확히 전달해야 합니다."
            }
        ],
        "examples": [
            {
                "ko": "케이슨 12기를 순차적으로 침설하여 안벽 본체를 구축합니다.",
                "vi": "Chìm lần lượt 12 caisson để xây dựng thân chính của bờ kè.",
                "situation": "formal"
            },
            {
                "ko": "케이슨 내부에 모래를 채워 중량을 증가시켜야 합니다.",
                "vi": "Cần lấp đầy cát vào bên trong caisson để tăng trọng lượng.",
                "situation": "onsite"
            },
            {
                "ko": "케이슨 제작 야드에서 품질 검사를 실시합니다.",
                "vi": "Tiến hành kiểm tra chất lượng tại bãi chế tạo caisson.",
                "situation": "formal"
            }
        ],
        "relatedTerms": ["안벽", "방파제", "준설", "부잔교"]
    },
    {
        "slug": "bang-pha-je",
        "korean": "방파제",
        "vietnamese": "Đê chắn sóng",
        "hanja": "防波堤",
        "hanjaReading": "防(막을 방) + 波(물결 파) + 堤(둑 제)",
        "pronunciation": "방파제",
        "meaningKo": "항만 외곽에 설치하여 외해의 파랑을 막아 항내를 정온하게 유지하는 구조물입니다. 통역 시 '외곽방파제', '잠제식 방파제', '케이슨식 방파제' 등 형식 구분이 중요하며, 베트nam에서는 Đê chắn sóng 외에 Kè chắn sóng이라고도 하므로 맥락에 따라 구분해야 합니다. 설계파고, 파주기 등 기상해양 데이터와 함께 언급되므로 수치 단위(m, sec)를 정확히 전달해야 합니다.",
        "meaningVi": "Công trình được xây dựng ở ngoài cảng để ngăn chặn sóng từ biển khơi, giữ cho vùng nước trong cảng yên tĩnh. Là cấu trúc thiết yếu để bảo vệ tàu thuyền và cơ sở hạ tầng cảng biển.",
        "context": "항만/해양건설",
        "culturalNote": "한국은 태풍과 높은 파랑에 대비한 대형 방파제 설계 경험이 풍부하나, 베트남은 상대적으로 온화한 해상 조건으로 방파제 규모가 작고 공법도 단순한 편입니다. 한국 기술진이 제시하는 과설계(over-design) 기준이 베트남 발주처에게 과도하게 느껴질 수 있어 설계 기준 설명 시 통역사의 보충 설명이 필요합니다.",
        "commonMistakes": [
            {
                "mistake": "방파제를 '파도 벽'으로 직역",
                "correction": "Đê chắn sóng (공식 용어)",
                "explanation": "방파제는 항만 구조물의 고유 명칭으로 정확한 베트남어 용어를 사용해야 합니다."
            },
            {
                "mistake": "호안과 방파제 혼동",
                "correction": "호안(Kè bảo vệ bờ)은 해안 보호, 방파제는 항내 정온 유지",
                "explanation": "목적과 위치가 다른 구조물입니다."
            },
            {
                "mistake": "설계파고를 일반 파도 높이로 오역",
                "correction": "설계파고는 Cao độ sóng thiết kế(설계 기준값)",
                "explanation": "관측값과 설계값을 구분해야 합니다."
            }
        ],
        "examples": [
            {
                "ko": "외곽방파제는 설계파고 8m를 기준으로 설계되었습니다.",
                "vi": "Đê chắn sóng ngoài được thiết kế theo cao độ sóng thiết kế 8m.",
                "situation": "formal"
            },
            {
                "ko": "방파제 두부에 등대를 설치할 예정입니다.",
                "vi": "Dự kiến lắp đặt đèn hải đăng tại đầu đê chắn sóng.",
                "situation": "formal"
            },
            {
                "ko": "잠제식 방파제로 경관 영향을 최소화합니다.",
                "vi": "Giảm thiểu tác động cảnh quan bằng đê chắn sóng chìm.",
                "situation": "onsite"
            }
        ],
        "relatedTerms": ["케이슨", "호안", "안벽", "사석"]
    },
    {
        "slug": "an-byeok",
        "korean": "안벽",
        "vietnamese": "Bờ kè cảng",
        "hanja": "岸壁",
        "hanjaReading": "岸(언덕 안) + 壁(벽 벽)",
        "pronunciation": "안벽",
        "meaningKo": "선박이 접안하여 화물을 싣고 내리는 항만의 벽 구조물로, 육지와 바다의 경계를 이루며 하역 장비가 설치됩니다. 통역 시 '컨테이너 안벽', '잡화 안벽' 등 용도별 구분과 함께 '안벽 수심', '접안 능력' 등 제원을 정확히 전달해야 합니다. 베트남어로는 Cầu cảng(부두)와 구분하여 Bờ kè cảng이라 하며, 구조형식(중력식, 잔교식)에 따라 명칭이 달라질 수 있습니다.",
        "meaningVi": "Công trình tường ngăn ở cảng biển nơi tàu thuyền neo đậu để bốc dỡ hàng hóa, tạo ranh giới giữa đất liền và biển và có lắp đặt thiết bị bốc xếp. Là hạ tầng cốt lõi của cảng biển.",
        "context": "항만/해양건설",
        "culturalNote": "한국은 대형 컨테이너선 접안을 위한 고규격 안벽(수심 -16m 이상) 건설 경험이 많으나, 베트남은 상대적으로 소형 선박 중심으로 안벽 수심이 얕고 구조가 단순합니다. 한국 기술진은 대형 케이슨 안벽에 익숙한 반면 베트남은 잔교식 안벽이 많아 공법 설명 시 시각 자료를 활용한 통역이 효과적입니다.",
        "commonMistakes": [
            {
                "mistake": "안벽을 부두(Cầu cảng)로 통칭",
                "correction": "안벽(Bờ kè cảng)과 부두(Cầu cảng)는 구조가 다름",
                "explanation": "안벽은 중력식 벽체, 부두는 잔교식 구조입니다."
            },
            {
                "mistake": "수심을 깊이로만 표현",
                "correction": "안벽 전면 수심(Độ sâu trước bờ kè)으로 명확히",
                "explanation": "항만 설계에서 수심은 기준면 기준 정확한 수치입니다."
            },
            {
                "mistake": "접안을 정박으로 오역",
                "correction": "접안은 Cập cảng(안벽에 붙이는 것), 정박은 Neo đậu",
                "explanation": "접안은 하역 작업, 정박은 대기 상태입니다."
            }
        ],
        "examples": [
            {
                "ko": "이 안벽은 5만톤급 선박의 접안이 가능합니다.",
                "vi": "Bờ kè này có thể đón tàu trọng tải 50,000 tấn cập cảng.",
                "situation": "formal"
            },
            {
                "ko": "안벽 전면 수심은 -15m입니다.",
                "vi": "Độ sâu trước bờ kè là -15m.",
                "situation": "onsite"
            },
            {
                "ko": "안벽 배후에 야드를 조성하여 컨테이너를 적치합니다.",
                "vi": "Xây dựng bãi sau bờ kè để xếp dỡ container.",
                "situation": "formal"
            }
        ],
        "relatedTerms": ["케이슨", "방파제", "부잔교", "준설"]
    },
    {
        "slug": "bu-jan-gyo",
        "korean": "부잔교",
        "vietnamese": "Cầu tàu nổi",
        "hanja": "浮棧橋",
        "hanjaReading": "浮(뜰 부) + 棧(잔다리 잔) + 橋(다리 교)",
        "pronunciation": "부잔교",
        "meaningKo": "조수간만의 차에 따라 상하로 움직이며 선박 접안을 돕는 부유식 잔교로, 고정식 안벽과 선박을 연결하는 중간 시설입니다. 통역 시 '폰툰(Pontoon)' 등 외래어와 혼용되며, '부잔교 계류', '부력 조정' 등 해양 공법 용어와 함께 사용됩니다. 베트남어로는 Cầu tàu nổi 또는 Phao nổi라 하며, 조석 조건이 다른 지역에서는 부잔교 필요성에 대한 설명이 추가로 필요할 수 있습니다.",
        "meaningVi": "Cầu tàu nổi di chuyển lên xuống theo thủy triều để hỗ trợ tàu thuyền cập bến, là cơ sở trung gian kết nối bờ kè cố định và tàu. Thích hợp cho khu vực có biên độ thủy triều lớn.",
        "context": "항만/해양건설",
        "culturalNote": "한국 서해안은 조수간만의 차가 크므로(최대 10m 이상) 부잔교가 필수적이나, 베트남 대부분 해역은 조차가 작아(1~2m) 부잔교 사용 빈도가 낮습니다. 한국 기술진이 제시하는 부잔교 설계가 베트남 현지에서는 과도한 시설로 인식될 수 있어, 조석 데이터를 근거로 필요성을 명확히 설명하는 통역이 중요합니다.",
        "commonMistakes": [
            {
                "mistake": "부잔교를 단순히 '다리'로 번역",
                "correction": "Cầu tàu nổi(부유식 선착장)",
                "explanation": "부잔교는 조석 대응 특수 구조물입니다."
            },
            {
                "mistake": "폰툰과 부잔교를 동일시",
                "correction": "폰툰(Phao nổi)은 부력체, 부잔교는 전체 시스템",
                "explanation": "폰툰은 부잔교의 구성 요소입니다."
            },
            {
                "mistake": "조수간만의 차를 일반 수위 변화로 표현",
                "correction": "조석(Thủy triều), 간만의 차(Biên độ thủy triều)",
                "explanation": "해양 공학 용어로 정확히 전달해야 합니다."
            }
        ],
        "examples": [
            {
                "ko": "조수간만의 차가 크므로 부잔교 설치가 필요합니다.",
                "vi": "Do biên độ thủy triều lớn nên cần lắp đặt cầu tàu nổi.",
                "situation": "formal"
            },
            {
                "ko": "부잔교와 고정 잔교를 연결하는 경사로를 설치합니다.",
                "vi": "Lắp đặt dốc nối giữa cầu tàu nổi và cầu tàu cố định.",
                "situation": "onsite"
            },
            {
                "ko": "폰툰 내부에 부력 조절용 밸브를 배치합니다.",
                "vi": "Bố trí van điều chỉnh phao nổi bên trong phao nổi.",
                "situation": "onsite"
            }
        ],
        "relatedTerms": ["안벽", "잔교", "계류", "조석"]
    },
    {
        "slug": "jun-seol",
        "korean": "준설",
        "vietnamese": "Nạo vét",
        "hanja": "浚渫",
        "hanjaReading": "浚(깊을 준) + 渫(파낼 설)",
        "pronunciation": "준설",
        "meaningKo": "항만이나 수로의 바닥을 파내어 수심을 확보하거나 유지하는 작업으로, 대형 준설선을 투입하여 토사, 암반을 제거합니다. 통역 시 '유지준설', '신규준설', '암준설' 등 목적과 대상에 따른 구분이 중요하며, 베트남어로는 Nạo vét이라 합니다. 준설토 처리 방안(매립, 투기)과 환경 영향 평가가 함께 언급되므로 관련 용어(dredging spoil, 투기장)도 숙지해야 합니다.",
        "meaningVi": "Công việc đào bới đáy cảng hoặc luồng tàu để tạo hoặc duy trì độ sâu, sử dụng tàu nạo vét lớn để loại bỏ bùn đất và đá. Là công tác cần thiết để đảm bảo tàu lớn ra vào cảng an toàn.",
        "context": "항만/해양건설",
        "culturalNote": "한국은 대형 준설선(그랩, 펌프식)을 보유하고 대규모 준설 공사 경험이 풍부하나, 베트남은 중소형 장비 중심으로 준설 속도와 정밀도에서 차이가 있습니다. 한국 기술진이 제시하는 준설량(m³/일)과 정밀도 기준이 베트남 현지 장비로는 달성하기 어려울 수 있어, 공정 계획 논의 시 장비 스펙을 확인하는 통역이 필요합니다.",
        "commonMistakes": [
            {
                "mistake": "준설을 단순히 '파기'로 번역",
                "correction": "Nạo vét(해저/수중 굴착 전용 용어)",
                "explanation": "준설은 해양 토목의 전문 공정입니다."
            },
            {
                "mistake": "준설토를 일반 토사로 표현",
                "correction": "준설토는 Bùn đất nạo vét(해저 퇴적물)",
                "explanation": "성상과 처리 방법이 육상 토사와 다릅니다."
            },
            {
                "mistake": "암준설과 토사준설을 구분하지 않음",
                "correction": "암준설(Nạo vét đá), 토사준설(Nạo vét bùn đất)",
                "explanation": "장비와 공법이 완전히 다릅니다."
            }
        ],
        "examples": [
            {
                "ko": "항로 유지를 위해 연간 10만㎥의 준설이 필요합니다.",
                "vi": "Cần nạo vét 100,000 m³ hàng năm để duy trì luồng tàu.",
                "situation": "formal"
            },
            {
                "ko": "암반 구간은 암준설 전문 장비를 투입합니다.",
                "vi": "Khu vực đá sẽ sử dụng thiết bị nạo vét đá chuyên dụng.",
                "situation": "onsite"
            },
            {
                "ko": "준설토는 매립지로 운반하여 처리합니다.",
                "vi": "Bùn đất nạo vét sẽ được vận chuyển đến bãi lấp để xử lý.",
                "situation": "formal"
            }
        ],
        "relatedTerms": ["안벽", "매립", "사석", "항로"]
    },
    {
        "slug": "ho-an",
        "korean": "호안",
        "vietnamese": "Kè bảo vệ bờ",
        "hanja": "護岸",
        "hanjaReading": "護(지킬 호) + 岸(언덕 안)",
        "pronunciation": "호안",
        "meaningKo": "하천이나 해안의 제방을 보호하기 위해 설치하는 구조물로, 파랑이나 유수에 의한 침식을 방지합니다. 통역 시 '사석 호안', '콘크리트 호안', '식생 호안' 등 공법별 구분과 함께 '세굴 방지', '침식 대책' 등 목적을 명확히 해야 합니다. 베트남어로는 Kè bảo vệ bờ이며, 방파제(Đê chắn sóng)와는 목적과 위치가 다르므로 구분이 필요합니다.",
        "meaningVi": "Công trình được xây dựng để bảo vệ đê sông hoặc bờ biển, ngăn chặn xói mòn do sóng hoặc dòng chảy. Là biện pháp quan trọng để bảo vệ đất liền và cơ sở hạ tầng ven bờ.",
        "context": "항만/해양건설",
        "culturalNote": "한국은 콘크리트 테트라포드 등 대형 이형 블록을 사용한 호안이 일반적이나, 베트남은 사석 쌓기나 자연석 호안이 많아 공법 수준에서 차이가 있습니다. 한국 기술진이 제시하는 고규격 호안이 베트남 발주처에게는 과잉 투자로 인식될 수 있으므로, 경제성과 내구성을 균형있게 설명하는 통역이 중요합니다.",
        "commonMistakes": [
            {
                "mistake": "호안을 방파제로 혼동",
                "correction": "호안(Kè bảo vệ bờ)은 해안 보호, 방파제(Đê chắn sóng)는 항내 정온",
                "explanation": "목적과 구조가 다릅니다."
            },
            {
                "mistake": "세굴을 단순 침식으로 표현",
                "correction": "세굴은 Xói lở đáy(수중 토사 유실)",
                "explanation": "호안 설계에서 세굴은 중요한 파괴 메커니즘입니다."
            },
            {
                "mistake": "테트라포드를 일반 블록으로 번역",
                "correction": "테트라포드는 Khối bê tông hình tứ giác(4각뿔 블록)",
                "explanation": "이형 블록의 고유 명칭입니다."
            }
        ],
        "examples": [
            {
                "ko": "사석 호안으로 해안 침식을 방지합니다.",
                "vi": "Ngăn chặn xói mòn bờ biển bằng kè đá hộc.",
                "situation": "formal"
            },
            {
                "ko": "호안 전면에 세굴 방지공을 설치합니다.",
                "vi": "Lắp đặt công trình chống xói lở đáy trước kè.",
                "situation": "onsite"
            },
            {
                "ko": "테트라포드를 2열로 배치하여 소파 효과를 높입니다.",
                "vi": "Bố trí khối bê tông hình tứ giác 2 hàng để tăng hiệu quả giảm sóng.",
                "situation": "formal"
            }
        ],
        "relatedTerms": ["방파제", "사석", "케이슨", "침식"]
    },
    {
        "slug": "hae-sang-keu-re-in",
        "korean": "해상크레인",
        "vietnamese": "Cần trục biển",
        "hanja": "海上크레인",
        "hanjaReading": "海(바다 해) + 上(위 상) + 크레인(외래어)",
        "pronunciation": "해상크레인",
        "meaningKo": "바다 위에서 중량물을 인양하거나 거치하는 작업을 수행하는 대형 부유식 크레인으로, 항만 공사나 해상 구조물 설치에 필수적입니다. 통역 시 '기중기 용량(톤)', '작업 반경(m)' 등 제원과 함께 '플로팅 크레인(Floating Crane)', '바지선 크레인' 등 형식 구분이 중요합니다. 베트남어로는 Cần trục biển 또는 Cần trục nổi라 하며, 장비 부족으로 한국에서 임대하는 경우가 많아 비용 협상 시 통역사의 세심한 수치 전달이 필요합니다.",
        "meaningVi": "Cần trục nổi lớn hoạt động trên biển để nâng hạ hoặc lắp đặt vật nặng, thiết bị thiết yếu trong xây dựng cảng và công trình biển. Có vai trò quan trọng trong thi công các cấu kiện lớn như caisson, cọc khoan nhồi.",
        "context": "항만/해양건설",
        "culturalNote": "한국은 3,000톤급 이상 대형 해상크레인을 다수 보유하고 있으나 베트남은 500~1,000톤급 중소형 장비가 대부분으로 대형 구조물 시공 시 한국 장비를 임대하는 경우가 많습니다. 장비 임대료(일당 수천만원)와 기상 대기 기간에 대한 비용 산정 방식이 달라 계약 협상 시 통역사의 명확한 수치 전달과 조건 확인이 중요합니다.",
        "commonMistakes": [
            {
                "mistake": "해상크레인을 일반 크레인으로 번역",
                "correction": "Cần trục biển(해상 전용 장비)",
                "explanation": "육상 크레인(Cần trục bộ)과 구조가 다릅니다."
            },
            {
                "mistake": "플로팅 크레인과 해상크레인을 구분하지 않음",
                "correction": "플로팅 크레인은 Cần trục nổi(부유식), 해상크레인은 포괄 용어",
                "explanation": "형식에 따라 명칭이 세분화됩니다."
            },
            {
                "mistake": "기중기 용량을 중량으로 오해",
                "correction": "용량은 Sức nâng(인양 능력), 자체 중량은 Trọng lượng",
                "explanation": "기중기 스펙 표기가 다릅니다."
            }
        ],
        "examples": [
            {
                "ko": "1,500톤급 해상크레인으로 케이슨을 거치합니다.",
                "vi": "Lắp đặt caisson bằng cần trục biển 1,500 tấn.",
                "situation": "formal"
            },
            {
                "ko": "해상크레인 작업은 풍속 15m/s 이하에서만 가능합니다.",
                "vi": "Thi công bằng cần trục biển chỉ khả thi khi tốc độ gió dưới 15m/s.",
                "situation": "onsite"
            },
            {
                "ko": "플로팅 크레인 임대료는 일당 5,000만원입니다.",
                "vi": "Chi phí thuê cần trục nổi là 50 triệu won mỗi ngày.",
                "situation": "formal"
            }
        ],
        "relatedTerms": ["케이슨", "안벽", "해상공사", "부잔교"]
    },
    {
        "slug": "jam-ham",
        "korean": "잠함",
        "vietnamese": "Giếng chìm",
        "hanja": "潛函",
        "hanjaReading": "潛(잠길 잠) + 函(상자 함)",
        "pronunciation": "잠함",
        "meaningKo": "지하 구조물 시공 시 상부에 압축공기를 주입하여 지하수를 차단하고 굴착하는 공법으로 사용되는 대형 상자 구조물입니다. 주로 교각 기초, 지하철 역사 등 깊은 지반 굴착에 사용되며, 해양 공사에서는 해저 지반 시공에 활용됩니다. 통역 시 '압기공법(Pneumatic Caisson)', '잠함병' 등 안전 용어와 함께 언급되므로 주의가 필요합니다. 베트남어로는 Giếng chìm이며, 고압 작업 환경의 위험성을 명확히 전달해야 합니다.",
        "meaningVi": "Cấu trúc hộp lớn sử dụng trong thi công công trình ngầm, bơm khí nén vào phía trên để ngăn nước ngầm và đào đất. Chủ yếu dùng cho móng trụ cầu, nhà ga tàu điện ngầm và thi công nền đáy biển.",
        "context": "항만/해양건설",
        "culturalNote": "한국은 압기공법 경험이 풍부하고 안전 관리 체계가 확립되어 있으나, 베트남은 잠함 공사 사례가 적고 고압 작업 안전 교육이 부족합니다. 한국 기술진이 요구하는 압력 챔버, 의료진 대기 등 안전 조건이 베트남 현장에서는 과도하게 느껴질 수 있으나, '잠함병(Bệnh lặn)' 등 생명과 직결된 위험을 명확히 설명하는 통역이 필수적입니다.",
        "commonMistakes": [
            {
                "mistake": "잠함을 단순 '지하 상자'로 번역",
                "correction": "Giếng chìm(압기공법 전용 구조물)",
                "explanation": "잠함은 고압 환경 특수 공법입니다."
            },
            {
                "mistake": "압기를 단순 공기로 표현",
                "correction": "압축공기(Khí nén có áp suất)",
                "explanation": "압력 수치가 중요한 안전 요소입니다."
            },
            {
                "mistake": "잠함병을 일반 질병으로 오역",
                "correction": "잠함병은 Bệnh lặn(감압병, 생명 위험)",
                "explanation": "산업재해 중 치명적 질환입니다."
            }
        ],
        "examples": [
            {
                "ko": "해저 지반이 연약하여 잠함공법을 적용합니다.",
                "vi": "Áp dụng phương pháp giếng chìm do nền đáy biển yếu.",
                "situation": "formal"
            },
            {
                "ko": "잠함 내부 작업은 2기압 환경에서 진행됩니다.",
                "vi": "Thi công bên trong giếng chìm diễn ra ở áp suất 2 atm.",
                "situation": "onsite"
            },
            {
                "ko": "잠함병 예방을 위해 감압실을 설치합니다.",
                "vi": "Lắp đặt buồng giảm áp để phòng ngừa bệnh lặn.",
                "situation": "formal"
            }
        ],
        "relatedTerms": ["기초", "압기공법", "안전", "지하수"]
    },
    {
        "slug": "sa-seok",
        "korean": "사석",
        "vietnamese": "Đá hộc",
        "hanja": "砂石",
        "hanjaReading": "砂(모래 사) + 石(돌 석)",
        "pronunciation": "사석",
        "meaningKo": "항만이나 호안 공사에서 기초나 사면 보호용으로 사용하는 자연석 또는 쇄석으로, 보통 50kg~1톤급 암석을 의미합니다. 통역 시 '사석 투입', '사석 마운드(mound)' 등 공법 용어와 함께 사용되며, 베트남어로는 Đá hộc이라 합니다. 입도(크기 분포)와 중량 기준이 설계에 중요하므로 수치를 정확히 전달해야 하며, 채석장 위치와 운반 거리가 공사비에 큰 영향을 미치므로 물류 관련 통역도 필요합니다.",
        "meaningVi": "Đá tự nhiên hoặc đá dăm được sử dụng làm nền móng hoặc bảo vệ mái dốc trong xây dựng cảng và kè, thường là đá từ 50kg đến 1 tấn. Là vật liệu quan trọng trong công trình biển.",
        "context": "항만/해양건설",
        "culturalNote": "한국은 대형 채석장에서 규격화된 사석을 대량 공급받을 수 있으나, 베트남은 채석장이 분산되어 있고 품질 편차가 커서 입도 관리가 어렵습니다. 한국 설계 기준의 엄격한 입도 분포 요구가 베트남 현지에서는 달성하기 어려울 수 있어, 현실적인 기준 조정이나 대안 공법 논의 시 통역사의 기술적 이해가 필요합니다.",
        "commonMistakes": [
            {
                "mistake": "사석을 모래로 오역",
                "correction": "사석은 Đá hộc(큰 돌), 모래는 Cát",
                "explanation": "입도와 용도가 완전히 다릅니다."
            },
            {
                "mistake": "입도를 단순 크기로 표현",
                "correction": "입도는 Cấp phối hạt(크기 분포 범위)",
                "explanation": "설계 기준은 범위로 제시됩니다."
            },
            {
                "mistake": "마운드를 단순 더미로 번역",
                "correction": "마운드는 Nền đá(사석 기초층)",
                "explanation": "항만 공학의 전문 용어입니다."
            }
        ],
        "examples": [
            {
                "ko": "방파제 기초로 1톤급 사석 1만㎥를 투입합니다.",
                "vi": "Đổ 10,000 m³ đá hộc 1 tấn làm nền móng đê chắn sóng.",
                "situation": "formal"
            },
            {
                "ko": "사석 마운드 상부에 케이슨을 거치합니다.",
                "vi": "Lắp đặt caisson lên trên nền đá hộc.",
                "situation": "onsite"
            },
            {
                "ko": "사석 입도는 500~1,000mm 범위로 관리합니다.",
                "vi": "Quản lý cấp phối đá hộc trong khoảng 500~1,000mm.",
                "situation": "formal"
            }
        ],
        "relatedTerms": ["케이슨", "방파제", "호안", "기초"]
    },
    {
        "slug": "mae-rip",
        "korean": "매립",
        "vietnamese": "Lấp biển",
        "hanja": "埋立",
        "hanjaReading": "埋(묻을 매) + 立(설 립)",
        "pronunciation": "매립",
        "meaningKo": "바다나 습지를 흙이나 암석으로 채워 육지로 만드는 공사로, 항만 배후 부지 조성이나 산업단지 개발에 사용됩니다. 통역 시 '준설토 매립', '사토 매립', '매립 높이' 등 공법과 재료 구분이 중요하며, 베트남어로는 Lấp biển 또는 San lấp이라 합니다. 환경 영향 평가와 어업 보상 문제가 함께 논의되므로, 관련 용어(EIA, 어업권)도 숙지해야 합니다.",
        "meaningVi": "Công trình lấp đầy biển hoặc đất ngập nước bằng đất đá để tạo đất liền, sử dụng cho xây dựng bãi sau cảng hoặc khu công nghiệp. Là giải pháp mở rộng đất ven biển nhưng cần đánh giá tác động môi trường.",
        "context": "항만/해양건설",
        "culturalNote": "한국은 대규모 매립 사업(새만금, 인천 송도 등) 경험이 풍부하고 환경 관리 기술이 발달했으나, 베트남은 환경 규제가 상대적으로 느슨하고 어업 보상 체계가 불명확합니다. 한국 기술진이 제시하는 환경 저감 대책이 베트남 발주처에게는 과도한 비용으로 인식될 수 있으나, 국제 환경 기준 준수 필요성을 명확히 설명하는 통역이 중요합니다.",
        "commonMistakes": [
            {
                "mistake": "매립을 단순 '흙 채우기'로 번역",
                "correction": "Lấp biển(해상 매립), San lấp(육상 성토)",
                "explanation": "대상 지역에 따라 용어가 다릅니다."
            },
            {
                "mistake": "준설토와 사토를 구분하지 않음",
                "correction": "준설토(Bùn đất nạo vét), 사토(Đất san lấp)",
                "explanation": "매립 재료의 성상과 출처가 다릅니다."
            },
            {
                "mistake": "어업 보상을 단순 보상금으로 표현",
                "correction": "어업권 보상(Bồi thường quyền khai thác thủy sản)",
                "explanation": "법적 권리에 대한 보상입니다."
            }
        ],
        "examples": [
            {
                "ko": "준설토 50만㎥를 이용하여 배후 부지를 매립합니다.",
                "vi": "Lấp bãi sau cảng bằng 500,000 m³ bùn đất nạo vét.",
                "situation": "formal"
            },
            {
                "ko": "매립 높이는 해수면 상 +5m로 계획되었습니다.",
                "vi": "Độ cao lấp biển được thiết kế ở mức +5m so với mực nước biển.",
                "situation": "formal"
            },
            {
                "ko": "환경 영향 평가 결과에 따라 어업 보상을 진행합니다.",
                "vi": "Tiến hành bồi thường quyền khai thác thủy sản theo kết quả đánh giá tác động môi trường.",
                "situation": "onsite"
            }
        ],
        "relatedTerms": ["준설", "사석", "환경", "항만"]
    }
]

# 파일 경로
file_path = os.path.join(
    os.path.dirname(__file__),
    "..",
    "data",
    "terms",
    "construction.json"
)

# 기존 데이터 읽기
with open(file_path, "r", encoding="utf-8") as f:
    existing_data = json.load(f)

# 새 용어 추가
existing_data.extend(data)

# 저장 (들여쓰기 2칸, 한글 유니코드 이스케이프 비활성화)
with open(file_path, "w", encoding="utf-8") as f:
    json.dump(existing_data, f, ensure_ascii=False, indent=2)

print(f"✅ {len(data)}개 용어가 {file_path}에 추가되었습니다.")
print("⚠️  npm run validate:terms로 품질 검증을 진행하세요.")
