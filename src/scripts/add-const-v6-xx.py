#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
건설(Construction) 용어 추가 스크립트 v6-xx
테마: 지하주차장/지하층 - 지하굴착, 역타공법, 탑다운, 집수정, 배수펌프장, 피트, 방수층, 확산구간, 차량동선, 환기탑
"""

import json
import os

# 추가할 용어 데이터 (10개)
data = [
    {
        "slug": "dao-ham-duoi-dat",
        "korean": "지하굴착",
        "vietnamese": "Đào hầm dưới đất",
        "hanja": "地下掘鑿",
        "hanjaReading": "땅 지(地) + 아래 하(下) + 굴 굴(掘) + 뚫을 착(鑿)",
        "pronunciation": "짜오 험 주어이 닷",
        "meaningKo": "지하 공간을 만들기 위해 땅을 파는 작업. 통역 시 '굴착 깊이', '흙막이 공법', '지하수위'를 함께 설명해야 하며, 베트남에서는 'đào đất' 대신 'đào hầm'이라는 표현을 써야 지하 구조물 공사임을 명확히 전달할 수 있습니다. 안전 관리 강조 필수.",
        "meaningVi": "Công tác đào đất để tạo không gian ngầm. Cần chú ý độ sâu đào, phương pháp chống đỡ thành hố, và mực nước ngầm. Khác với đào móng thông thường.",
        "context": "지하주차장, 지하층 시공",
        "culturalNote": "한국은 지하 3~4층 주차장이 일반적이지만 베트남은 도심에서도 지하 1~2층이 많습니다. 굴착 깊이에 따른 공법 차이(개착식/역타공법)를 명확히 구분해야 하며, 베트Nam에서는 지하수 처리가 더 중요한 이슈입니다.",
        "commonMistakes": [
            {
                "mistake": "đào đất → 지하굴착",
                "correction": "đào hầm dưới đất → 지하굴착",
                "explanation": "'đào đất'는 단순 토공이고, 'đào hầm'은 지하 구조물 공사"
            },
            {
                "mistake": "굴착 = excavation만 언급",
                "correction": "굴착 + 흙막이 + 지하수 대책 세트로 설명",
                "explanation": "지하굴착은 단순 파기가 아니라 안전 시스템 전체를 의미"
            },
            {
                "mistake": "깊이를 mét로만 표현",
                "correction": "몇 층 지하 + mét 병기",
                "explanation": "한국은 층수, 베트남은 미터 단위 선호"
            }
        ],
        "examples": [
            {
                "ko": "지하 3층까지 굴착 예정이며, 역타공법을 적용합니다.",
                "vi": "Dự kiến đào hầm đến tầng hầm 3, áp dụng phương pháp top-down.",
                "situation": "formal"
            },
            {
                "ko": "굴착 중 지하수가 나와서 배수펌프를 설치했어요.",
                "vi": "Khi đào gặp nước ngầm nên đã lắp máy bơm thoát nước.",
                "situation": "onsite"
            },
            {
                "ko": "흙막이 벽이 안정적이어야 안전하게 굴착할 수 있습니다.",
                "vi": "Tường chắn đất phải ổn định mới đào an toàn được.",
                "situation": "formal"
            }
        ],
        "relatedTerms": ["흙막이공사", "역타공법", "집수정", "지하수위"]
    },
    {
        "slug": "phuong-phap-top-down",
        "korean": "역타공법",
        "vietnamese": "Phương pháp top-down",
        "hanja": "逆打工法",
        "hanjaReading": "거스를 역(逆) + 칠 타(打) + 장인 공(工) + 법 법(法)",
        "pronunciation": "프엉 팝 톱 다운",
        "meaningKo": "지상층과 지하층을 동시에 시공하는 공법. 위에서 아래로(top-down) 작업하므로 공기 단축 효과가 큽니다. 통역 시 '슬래브를 먼저 타설해 버팀대로 활용'한다는 원리를 설명해야 하며, 베트남에서는 영어 'top-down'을 그대로 사용하지만 원리 설명이 필수입니다.",
        "meaningVi": "Phương pháp thi công đồng thời tầng trên mặt đất và tầng hầm. Đổ sàn bê tông trước để làm giá đỡ, sau đó đào xuống dưới. Rút ngắn thời gian thi công đáng kể.",
        "context": "대형 지하주차장, 고층 건물",
        "culturalNote": "한국에서는 공기 단축을 위해 역타공법이 보편화되었지만, 베트남에서는 아직 일반 개착식이 많습니다. 비용과 기술력 차이로 인해 고급 프로젝트에서만 적용되므로, 통역 시 공법의 장단점과 적용 조건을 명확히 전달해야 합니다.",
        "commonMistakes": [
            {
                "mistake": "top-down = 위에서 아래로 파는 것",
                "correction": "슬래브를 먼저 치고 그 아래를 파는 공법",
                "explanation": "단순 굴착 방향이 아니라 구조물 선시공 방식"
            },
            {
                "mistake": "'역타' 그대로 번역 시도",
                "correction": "phương pháp top-down 사용",
                "explanation": "베트남에서는 영어 용어가 표준"
            },
            {
                "mistake": "개착식과의 차이 설명 누락",
                "correction": "개착식(đào hở) vs 역타(top-down) 대비 설명",
                "explanation": "공법 선택 이유 이해를 위해 필수"
            }
        ],
        "examples": [
            {
                "ko": "이 현장은 역타공법으로 지상과 지하를 동시 시공합니다.",
                "vi": "Công trường này áp dụng phương pháp top-down, thi công đồng thời tầng trên và tầng hầm.",
                "situation": "formal"
            },
            {
                "ko": "1층 슬래브를 먼저 타설하고 그 밑을 파내려가요.",
                "vi": "Đổ sàn tầng 1 trước rồi đào xuống dưới.",
                "situation": "onsite"
            },
            {
                "ko": "역타공법은 공기는 짧지만 시공 난이도가 높습니다.",
                "vi": "Phương pháp top-down rút ngắn thời gian nhưng thi công phức tạp.",
                "situation": "formal"
            }
        ],
        "relatedTerms": ["개착식공법", "지하굴착", "슬래브", "버팀대"]
    },
    {
        "slug": "ho-thu-nuoc",
        "korean": "집수정",
        "vietnamese": "Hố thu nước",
        "hanja": "集水井",
        "hanjaReading": "모을 집(集) + 물 수(水) + 우물 정(井)",
        "pronunciation": "호 투 느억",
        "meaningKo": "지하 공사 중 지하수나 빗물을 모아 배수하기 위한 구덩이. 통역 시 '펌프장과의 차이'를 명확히 해야 하며, 집수정은 임시 시설이고 펌프장은 영구 시설입니다. 베트남에서는 'hố thu nước' 또는 'giếng thu nước'로 표현하며, 우기 대비를 강조해야 합니다.",
        "meaningVi": "Hố đào để thu gom nước ngầm hoặc nước mưa trong quá trình thi công, sau đó bơm ra ngoài. Khác với trạm bơm vĩnh cửu, đây là công trình tạm thời phục vụ thi công.",
        "context": "지하굴착, 배수 시스템",
        "culturalNote": "한국은 지하수위가 낮은 곳이 많지만, 베트남 특히 남부는 지하수위가 높고 우기 강수량이 많아 집수정 설계가 더 중요합니다. 호치민 같은 도시에서는 굴착 즉시 지하수가 차오르므로 집수정과 배수펌프 용량 산정이 필수적입니다.",
        "commonMistakes": [
            {
                "mistake": "집수정 = trạm bơm (펌프장)",
                "correction": "집수정 = hố thu nước (임시), 펌프장 = trạm bơm (영구)",
                "explanation": "용도와 영구성이 다름"
            },
            {
                "mistake": "위치 설명 없이 '집수정 만들자'",
                "correction": "'가장 낮은 곳에 집수정 설치' 명시",
                "explanation": "물이 자연스럽게 모이는 위치 선정 중요"
            },
            {
                "mistake": "크기/용량 누락",
                "correction": "지하수량 대비 용량 설명",
                "explanation": "베트남은 지하수가 많아 용량이 핵심"
            }
        ],
        "examples": [
            {
                "ko": "굴착 현장 최저점에 집수정을 설치하고 펌프로 배수합니다.",
                "vi": "Lắp hố thu nước ở điểm thấp nhất công trường đào, dùng máy bơm thoát ra ngoài.",
                "situation": "formal"
            },
            {
                "ko": "비 오면 물이 여기로 다 모여서 펌프 돌려야 해요.",
                "vi": "Mưa là nước chảy hết về đây, phải chạy máy bơm.",
                "situation": "onsite"
            },
            {
                "ko": "집수정 용량이 부족해서 펌프를 추가 설치했습니다.",
                "vi": "Hố thu nước không đủ dung tích nên lắp thêm máy bơm.",
                "situation": "formal"
            }
        ],
        "relatedTerms": ["배수펌프장", "지하수위", "배수공사", "우수배수"]
    },
    {
        "slug": "tram-bom-thoat-nuoc",
        "korean": "배수펌프장",
        "vietnamese": "Trạm bơm thoát nước",
        "hanja": "排水Pump場",
        "hanjaReading": "배설할 배(排) + 물 수(水) + (외래어) + 마당 장(場)",
        "pronunciation": "짬 붐 토앗 느억",
        "meaningKo": "지하 공간에 고인 물을 영구적으로 배출하기 위한 펌프 설비와 공간. 통역 시 '집수정(임시)'과 구분하고, '자동 운전', '예비 펌프', '비상발전기' 등 시스템 구성을 설명해야 합니다. 베트남에서는 'trạm bơm'이 표준 용어이며, 침수 방지 측면을 강조합니다.",
        "meaningVi": "Hệ thống bơm nước cố định để thoát nước tích tụ trong không gian ngầm. Bao gồm máy bơm chính, máy dự phòng, hệ thống tự động, và máy phát điện dự phòng. Khác với hố thu nước tạm thời.",
        "context": "지하주차장, 지하층 영구시설",
        "culturalNote": "한국은 지하 주차장 배수펌프장이 법적 필수 설비이며, 침수 사고 대비가 엄격합니다. 베트남도 최근 침수 사고 증가로 규정이 강화되고 있지만, 유지보수 문화 차이로 인해 한국식 자동화 시스템 설명 시 '정기 점검'의 중요성을 함께 전달해야 합니다.",
        "commonMistakes": [
            {
                "mistake": "펌프장 = máy bơm (펌프 기계)",
                "correction": "펌프장 = trạm bơm (펌프 + 시설 전체)",
                "explanation": "공간과 시스템을 포함하는 개념"
            },
            {
                "mistake": "임시 집수정과 혼동",
                "correction": "영구 시설임을 명시",
                "explanation": "시공 후에도 계속 사용되는 시설"
            },
            {
                "mistake": "자동/수동 구분 없이 설명",
                "correction": "hệ thống tự động (자동 시스템) 강조",
                "explanation": "베트남에서는 수동 펌프도 많아 구분 필요"
            }
        ],
        "examples": [
            {
                "ko": "지하 3층에 배수펌프장을 설치하며, 자동 운전 시스템을 적용합니다.",
                "vi": "Lắp trạm bơm thoát nước ở tầng hầm 3, áp dụng hệ thống vận hành tự động.",
                "situation": "formal"
            },
            {
                "ko": "예비 펌프도 있어서 하나 고장 나도 괜찮아요.",
                "vi": "Có máy bơm dự phòng nên một cái hỏng vẫn ổn.",
                "situation": "onsite"
            },
            {
                "ko": "펌프장 유지보수는 월 1회 정기 점검이 필요합니다.",
                "vi": "Trạm bơm cần bảo trì kiểm tra định kỳ mỗi tháng một lần.",
                "situation": "formal"
            }
        ],
        "relatedTerms": ["집수정", "배수펌프", "침수방지", "자동운전"]
    },
    {
        "slug": "ho-ky-thuat",
        "korean": "피트",
        "vietnamese": "Hố kỹ thuật",
        "hanja": None,
        "hanjaReading": None,
        "pronunciation": "호 끼 툿",
        "meaningKo": "차량 정비나 설비 점검을 위해 지하주차장 바닥에 만드는 작업 공간. 영어 'pit'에서 유래. 통역 시 '엘리베이터 피트'(승강기 바닥 공간)와 혼동하지 않도록 주의해야 하며, 베트남에서는 'hố kỹ thuật' 또는 'hầm bảo dưỡng'으로 표현합니다. 안전난간, 배수 필수.",
        "meaningVi": "Khoang làm việc đào sâu dưới sàn để bảo dưỡng xe hoặc kiểm tra thiết bị. Thường thấy trong gara hoặc tầng hầm để xe. Cần có lan can an toàn và hệ thống thoát nước.",
        "context": "지하주차장, 정비공간",
        "culturalNote": "한국 대형 빌딩 지하주차장에는 차량 정비용 피트가 법적으로 요구되는 경우가 있지만, 베트남에서는 아직 일반적이지 않습니다. 통역 시 '사고 예방을 위한 안전난간'과 '추락 방지 조명' 등 안전 요소를 강조해야 하며, 용도를 명확히 설명해야 합니다.",
        "commonMistakes": [
            {
                "mistake": "pit 그대로 → phít",
                "correction": "hố kỹ thuật 또는 hầm bảo dưỡng",
                "explanation": "베트남어 표준 용어 사용"
            },
            {
                "mistake": "엘리베이터 피트와 혼동",
                "correction": "용도 명시: 차량 정비용 / 승강기용",
                "explanation": "같은 'hố'지만 용도가 다름"
            },
            {
                "mistake": "안전시설 설명 누락",
                "correction": "난간, 조명, 배수 시설 포함 설명",
                "explanation": "피트는 추락 위험이 있어 안전이 핵심"
            }
        ],
        "examples": [
            {
                "ko": "지하 1층에 차량 정비용 피트를 2개소 설치합니다.",
                "vi": "Lắp 2 hố kỹ thuật bảo dưỡng xe ở tầng hầm 1.",
                "situation": "formal"
            },
            {
                "ko": "피트 주변에 안전난간 꼭 설치하세요.",
                "vi": "Nhớ lắp lan can an toàn quanh hố kỹ thuật nhé.",
                "situation": "onsite"
            },
            {
                "ko": "피트 바닥에 배수구를 만들어 물이 고이지 않게 합니다.",
                "vi": "Làm cống thoát nước ở đáy hố kỹ thuật để không bị đọng nước.",
                "situation": "formal"
            }
        ],
        "relatedTerms": ["지하주차장", "정비공간", "안전난간", "배수구"]
    },
    {
        "slug": "lop-chong-tham",
        "korean": "방수층",
        "vietnamese": "Lớp chống thấm",
        "hanja": "防水層",
        "hanjaReading": "막을 방(防) + 물 수(水) + 층 층(層)",
        "pronunciation": "럽 쫑 텀",
        "meaningKo": "물의 침투를 막기 위해 시공하는 층. 지하 구조물에서 필수적이며, 통역 시 '도막방수', '시트방수', '액체방수' 등 공법 차이를 설명해야 합니다. 베트남에서는 'chống thấm'이 표준이며, 우기와 지하수 대비 측면을 강조해야 합니다. 누수 시 보수 비용이 크므로 시공 품질이 핵심입니다.",
        "meaningVi": "Lớp thi công để ngăn nước xâm nhập. Rất quan trọng với công trình ngầm. Có nhiều phương pháp: phủ màng, tráng chống thấm lỏng, hoặc tấm chống thấm. Chất lượng thi công quyết định nguy cơ thấm rỉ.",
        "context": "지하층, 옥상, 화장실",
        "culturalNote": "한국은 4계절과 동결융해로 인해 방수층 품질 기준이 매우 엄격하지만, 베트남은 열대기후라 동결은 없고 대신 우기 집중호우와 높은 습도가 문제입니다. 통역 시 '균열 방지'와 '이음부 처리'의 중요성을 강조하고, 양국 기후 차이에 따른 공법 선택을 설명해야 합니다.",
        "commonMistakes": [
            {
                "mistake": "방수 = chống nước (일반 방수)",
                "correction": "방수층 = lớp chống thấm (구조물 방수)",
                "explanation": "'chống nước'는 우산 수준, 'chống thấm'은 건축 방수"
            },
            {
                "mistake": "공법 구분 없이 방수층만 언급",
                "correction": "도막/시트/액체 등 공법 명시",
                "explanation": "베트남에서 공법에 따라 자재와 비용이 크게 다름"
            },
            {
                "mistake": "1회 시공으로 설명",
                "correction": "여러 층 중첩 시공 설명",
                "explanation": "방수층은 보통 2~3중으로 시공"
            }
        ],
        "examples": [
            {
                "ko": "지하 외벽에 시트 방수층을 2중으로 시공합니다.",
                "vi": "Thi công lớp chống thấm tấm màng 2 lớp cho tường ngoài tầng hầm.",
                "situation": "formal"
            },
            {
                "ko": "방수층 이음부 잘 붙였는지 확인해주세요.",
                "vi": "Kiểm tra chỗ nối lớp chống thấm đã dán kỹ chưa nhé.",
                "situation": "onsite"
            },
            {
                "ko": "누수 발생 시 방수층 전체를 다시 해야 할 수도 있습니다.",
                "vi": "Nếu bị thấm có thể phải làm lại toàn bộ lớp chống thấm.",
                "situation": "formal"
            }
        ],
        "relatedTerms": ["누수", "도막방수", "시트방수", "방습층"]
    },
    {
        "slug": "khu-vuc-ram-phan-cach",
        "korean": "램프",
        "vietnamese": "Khu vực rampe",
        "hanja": None,
        "hanjaReading": None,
        "pronunciation": "쿠 븍 램프",
        "meaningKo": "지하주차장 진입을 위한 경사로. 영어 'ramp'에서 유래. 통역 시 '경사도(보통 12~17%)', '폭', '회전 반경' 등 구체적 수치를 함께 설명해야 하며, 베트남에서는 프랑스어 영향으로 'rampe'로 표기하기도 합니다. 미끄럼 방지와 배수가 중요한 요소입니다.",
        "meaningVi": "Đường dốc để xe đi vào/ra tầng hầm. Cần tính toán độ dốc (thường 12-17%), bán kính cong, và làm chống trơn. Thoát nước mưa là yếu tố quan trọng.",
        "context": "지하주차장 진출입",
        "culturalNote": "한국은 대형 차량 진입을 고려해 램프 폭과 회전 반경을 넉넉히 설계하지만, 베트남은 오토바이와 소형차가 많아 램프가 좁고 급경사인 경우가 많습니다. 통역 시 차량 유형에 따른 설계 기준 차이를 설명하고, 우기 빗물 유입 방지 대책을 강조해야 합니다.",
        "commonMistakes": [
            {
                "mistake": "ramp → ráp",
                "correction": "rampe (프랑스식) 또는 đường dốc (일반)",
                "explanation": "베트남에서는 'rampe' 또는 'đường dốc' 사용"
            },
            {
                "mistake": "경사도 표현 누락",
                "correction": "độ dốc X% 명시",
                "explanation": "안전과 직결되므로 수치 필수"
            },
            {
                "mistake": "미끄럼방지 처리 미언급",
                "correction": "bề mặt chống trơn 포함",
                "explanation": "베트남 우기에는 램프가 매우 미끄러움"
            }
        ],
        "examples": [
            {
                "ko": "지하주차장 램프는 경사도 15%로 설계합니다.",
                "vi": "Thiết kế rampe tầng hầm với độ dốc 15%.",
                "situation": "formal"
            },
            {
                "ko": "램프 바닥에 미끄럼 방지 처리 꼭 하세요.",
                "vi": "Nhớ làm bề mặt chống trơn cho rampe nhé.",
                "situation": "onsite"
            },
            {
                "ko": "램프 입구에 배수로를 설치해 빗물 유입을 막습니다.",
                "vi": "Lắp rãnh thoát nước ở đầu rampe để ngăn nước mưa chảy vào.",
                "situation": "formal"
            }
        ],
        "relatedTerms": ["지하주차장", "경사로", "미끄럼방지", "배수로"]
    },
    {
        "slug": "dong-tuyen-xe",
        "korean": "차량동선",
        "vietnamese": "Động tuyến xe",
        "hanja": "車輛動線",
        "hanjaReading": "수레 차(車) + 무리 량(輛) + 움직일 동(動) + 선 선(線)",
        "pronunciation": "동 뜌옌 쎄",
        "meaningKo": "차량이 주차장 내에서 이동하는 경로. 통역 시 '진입 동선', '주차 동선', '출차 동선'을 구분하고, '교차 최소화', '회전 반경', '시야 확보' 등 설계 원칙을 설명해야 합니다. 베트남에서는 'động tuyến' 또는 'lưu thông xe'로 표현하며, 오토바이 동선과의 분리도 고려해야 합니다.",
        "meaningVi": "Đường đi của xe trong bãi đậu. Cần phân biệt động tuyến vào, đỗ xe, và ra. Thiết kế tốt giúp giảm giao cắt, đảm bảo tầm nhìn, và tăng an toàn.",
        "context": "지하주차장 설계",
        "culturalNote": "한국은 승용차 중심 동선 설계이지만, 베트남은 오토바이와 자동차 동선을 분리하거나 혼용하는 경우가 많습니다. 통역 시 '사각지대 최소화'와 '보행자 동선과의 분리'를 강조하고, 호치민처럼 오토바이가 많은 도시에서는 별도 구역 필요성을 설명해야 합니다.",
        "commonMistakes": [
            {
                "mistake": "동선 = đường đi (일반 길)",
                "correction": "động tuyến (설계된 이동 경로)",
                "explanation": "'đường đi'는 단순 길, 'động tuyến'은 계획된 동선"
            },
            {
                "mistake": "진입/출구 동선 구분 없이 설명",
                "correction": "động tuyến vào/ra 명확히 구분",
                "explanation": "일방통행/양방통행 여부가 중요"
            },
            {
                "mistake": "오토바이 동선 고려 누락 (베트남)",
                "correction": "오토바이/차량 동선 분리 언급",
                "explanation": "베트남에서는 오토바이 동선이 핵심"
            }
        ],
        "examples": [
            {
                "ko": "차량 동선이 교차하지 않도록 일방통행으로 설계합니다.",
                "vi": "Thiết kế một chiều để động tuyến xe không giao cắt nhau.",
                "situation": "formal"
            },
            {
                "ko": "회전 구간에서 시야가 확보되도록 기둥 위치를 조정했어요.",
                "vi": "Điều chỉnh vị trí cột để đảm bảo tầm nhìn ở chỗ xe rẽ.",
                "situation": "onsite"
            },
            {
                "ko": "오토바이 주차 구역은 차량 동선과 분리하는 것이 좋습니다.",
                "vi": "Khu để xe máy nên tách riêng khỏi động tuyến ô tô.",
                "situation": "formal"
            }
        ],
        "relatedTerms": ["주차장설계", "램프", "회전반경", "보행자동선"]
    },
    {
        "slug": "thap-thong-gio",
        "korean": "환기탑",
        "vietnamese": "Tháp thông gió",
        "hanja": "換氣塔",
        "hanjaReading": "바꿀 환(換) + 기운 기(氣) + 탑 탑(塔)",
        "pronunciation": "탑 통 조",
        "meaningKo": "지하주차장의 공기를 순환시키기 위해 지상으로 연결된 구조물. 통역 시 '급배기 시스템', 'CO 농도 감지', '소음 방지' 등을 함께 설명해야 하며, 베트남에서는 'tháp thông gió' 또는 'ống thông gió'로 표현합니다. 지상 노출부의 미관 처리도 중요한 요소입니다.",
        "meaningVi": "Công trình nối từ tầng hầm lên mặt đất để tuần hoàn không khí. Hệ thống cấp/xả gió, cảm biến khí CO, và giảm ồn là yếu tố quan trọng. Phần lộ ra mặt đất cần xử lý thẩm mỹ.",
        "context": "지하주차장 환기 시스템",
        "culturalNote": "한국은 지하주차장 환기 기준이 엄격하고 환기탑 설치가 법적 필수인 경우가 많지만, 베트남은 기준이 상대적으로 느슨합니다. 통역 시 '일산화탄소 중독 예방'과 '쾌적한 공기질'의 중요성을 강조하고, 환기량 계산 방식을 설명해야 합니다. 지상부 디자인은 건축주의 큰 관심사입니다.",
        "commonMistakes": [
            {
                "mistake": "환기탑 = ống thông gió (환기관)",
                "correction": "환기탑 = tháp thông gió (탑 구조물)",
                "explanation": "'ống'은 관, 'tháp'은 탑 구조"
            },
            {
                "mistake": "급기/배기 구분 없이 설명",
                "correction": "cấp gió/xả gió 명확히 구분",
                "explanation": "공기 흐름 방향이 중요"
            },
            {
                "mistake": "소음 문제 미언급",
                "correction": "giảm ồn (소음 저감) 대책 포함",
                "explanation": "주거지 인접 시 민원 발생 가능"
            }
        ],
        "examples": [
            {
                "ko": "지하 2층 주차장에 환기탑 2개소를 설치합니다.",
                "vi": "Lắp 2 tháp thông gió cho tầng hầm 2.",
                "situation": "formal"
            },
            {
                "ko": "환기탑에서 소음 나지 않게 소음기 달아주세요.",
                "vi": "Lắp bộ giảm ồn cho tháp thông gió để không ồn nhé.",
                "situation": "onsite"
            },
            {
                "ko": "환기탑 지상부는 조경과 어울리도록 디자인합니다.",
                "vi": "Thiết kế phần tháp thông gió trên mặt đất hài hòa với cảnh quan.",
                "situation": "formal"
            }
        ],
        "relatedTerms": ["환기설비", "급배기", "CO감지기", "지하주차장"]
    },
    {
        "slug": "khu-vuc-phan-tan",
        "korean": "확산구간",
        "vietnamese": "Khu vực phân tán",
        "hanja": "擴散區間",
        "hanjaReading": "넓힐 확(擴) + 흩을 산(散) + 구역 구(區) + 사이 간(間)",
        "pronunciation": "쿠 븍 판 딴",
        "meaningKo": "지하주차장에서 차량이 각 주차 구획으로 분산되는 구역. 통역 시 '주 동선에서 가지 동선으로 나뉘는 지점'을 설명하고, '회전 공간', '시야 확보', '기둥 간격' 등 설계 요소를 언급해야 합니다. 베트남에서는 'khu vực phân tán' 또는 'khu vực phân phối'로 표현하며, 혼잡 방지가 핵심입니다.",
        "meaningVi": "Khu vực trong bãi đậu xe nơi các xe phân tán từ động tuyến chính vào các chỗ đỗ riêng lẻ. Cần đảm bảo không gian quay xe, tầm nhìn, và khoảng cách cột phù hợp để tránh tắc nghẽn.",
        "context": "지하주차장 동선 설계",
        "culturalNote": "한국은 대형 승용차를 고려해 확산구간을 넓게 설계하지만, 베트남은 오토바이와 소형차가 많아 상대적으로 좁은 편입니다. 통역 시 '동시 진입 차량 수'를 고려한 폭 설계와 '사고 예방을 위한 표지판/바닥 표시'의 중요성을 강조해야 합니다.",
        "commonMistakes": [
            {
                "mistake": "확산 = mở rộng (단순 확장)",
                "correction": "확산구간 = khu vực phân tán (분산 구역)",
                "explanation": "'mở rộng'은 확장, 'phân tán'은 분산 개념"
            },
            {
                "mistake": "주 동선과 구분 없이 설명",
                "correction": "주 동선 → 확산구간 → 주차칸 흐름 명시",
                "explanation": "단계별 동선 구조 이해 필요"
            },
            {
                "mistake": "회전 공간 고려 누락",
                "correction": "không gian quay xe (회전 공간) 포함",
                "explanation": "확산구간은 회전이 많아 공간 필수"
            }
        ],
        "examples": [
            {
                "ko": "확산구간은 차량 3대가 동시에 진입해도 여유 있게 설계합니다.",
                "vi": "Thiết kế khu vực phân tán rộng rãi để 3 xe cùng vào được.",
                "situation": "formal"
            },
            {
                "ko": "여기가 확산구간이니까 기둥 간격 넓게 잡으세요.",
                "vi": "Đây là khu phân tán nên khoảng cách cột làm rộng ra nhé.",
                "situation": "onsite"
            },
            {
                "ko": "확산구간에 방향 표시를 명확히 해야 혼잡을 줄일 수 있습니다.",
                "vi": "Khu vực phân tán cần đánh dấu hướng đi rõ ràng để giảm tắc nghẽn.",
                "situation": "formal"
            }
        ],
        "relatedTerms": ["차량동선", "주차구획", "회전반경", "기둥간격"]
    }
]

# 파일 경로 설정
base_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
file_path = os.path.join(base_dir, "data", "terms", "construction.json")

# 기존 데이터 로드
with open(file_path, "r", encoding="utf-8") as f:
    existing_data = json.load(f)

# 새 용어 추가
existing_data.extend(data)

# 파일 저장
with open(file_path, "w", encoding="utf-8") as f:
    json.dump(existing_data, f, ensure_ascii=False, indent=2)

print(f"✅ 지하주차장/지하층 테마 건설 용어 {len(data)}개 추가 완료!")
print(f"📂 파일: {file_path}")
print(f"📊 총 용어 수: {len(existing_data)}개")
