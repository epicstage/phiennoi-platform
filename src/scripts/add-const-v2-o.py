#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Construction Terms Addition Script v2-o
Theme: 공정관리/시공계획 (Schedule & Planning)
Target: 10 terms, Tier S quality
"""

import json
import os

# 절대 경로 설정
SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
PROJECT_ROOT = os.path.dirname(SCRIPT_DIR)
CONSTRUCTION_JSON = os.path.join(PROJECT_ROOT, "data/terms/construction.json")

# 10개 용어 데이터 (Tier S 기준)
NEW_TERMS = [
    {
        "slug": "bieu-do-tien-do",
        "korean": "공정표",
        "vietnamese": "biểu đồ tiến độ",
        "hanja": "工程表",
        "hanjaReading": "공(장인 공) + 정(과정 정) + 표(나타낼 표)",
        "pronunciation": "비에우 도 띠엔 도",
        "meaningKo": "건설 프로젝트의 전체 일정을 시각적으로 나타낸 문서로, 각 공종의 시작과 종료 시점, 소요 기간, 선후행 관계를 표시합니다. 바차트(Bar Chart), 네트워크 공정표(CPM/PERT) 등의 형식이 있으며, 공기 관리의 핵심 도구입니다. 통역 시 '일정', '스케줄'로 혼용되나, 공정표는 공사 특화 일정표임을 구분해야 하며, 지연 사유와 대책 논의에서 자주 언급됩니다. 주간 공정회의에서 실적과 계획을 대조하며 검토합니다.",
        "meaningVi": "Tài liệu thể hiện trực quan toàn bộ tiến độ dự án xây dựng, hiển thị thời điểm bắt đầu-kết thúc, thời gian cần thiết và mối quan hệ tiên hậu của từng công việc. Có dạng Bar Chart, sơ đồ mạng CPM/PERT, là công cụ cốt lõi quản lý tiến độ.",
        "context": "공정 관리, 시공 계획, 프로젝트 관리",
        "contextVi": "Quản lý tiến độ, kế hoạch thi công, quản lý dự án",
        "culturalNote": "한국 건설현장은 공정표 준수율을 매우 중요시하며, 주간/월간 단위로 엄격히 관리합니다. 베트남은 상대적으로 유연하게 조정하는 경향이 있어, 일정 지연에 대한 책임 소재와 보고 방식에서 문화적 차이가 발생합니다. 한국은 지연 즉시 원인 분석과 만회 대책을 요구하지만, 베트남은 전체 흐름에서 조율하는 방식을 선호합니다.",
        "commonMistakes": [
            {
                "mistake": "\"일정표\"로만 번역하여 공사 특화 의미 누락",
                "correction": "\"biểu đồ tiến độ thi công\" 또는 \"biểu đồ tiến độ\"",
                "explanation": "일반 일정표(lịch trình)와 구분하여 공사 공정의 전문성을 명시해야 함"
            },
            {
                "mistake": "\"kế hoạch\"(계획)과 혼동",
                "correction": "계획(kế hoạch)은 사전 기획, 공정표(biểu đồ tiến độ)는 시각화된 일정 관리 도구",
                "explanation": "계획은 방향성, 공정표는 구체적 타임라인 관리 수단"
            },
            {
                "mistake": "공정 지연 보고 시 \"muộn\"(늦다)만 사용",
                "correction": "\"chậm tiến độ\"(공정 지연) 또는 \"trễ hạn\"(기한 지체) 구분",
                "explanation": "지연의 성격과 심각도에 따라 표현을 달리해야 책임 소재가 명확해짐"
            }
        ],
        "examples": [
            {
                "ko": "공정표 상으로는 이번 주에 콘크리트 타설을 완료해야 합니다.",
                "vi": "Theo biểu đồ tiến độ thì tuần này phải hoàn thành đổ bê tông.",
                "situation": "formal"
            },
            {
                "ko": "공정표 다시 짜야겠네요. 철근 반입이 늦어졌어요.",
                "vi": "Phải lập lại biểu đồ tiến độ rồi. Thép về muộn mất rồi.",
                "situation": "onsite"
            },
            {
                "ko": "주간 공정회의에서 공정표 대비 실적을 검토하겠습니다.",
                "vi": "Tại cuộc họp tiến độ tuần, chúng ta sẽ rà soát thực tế so với biểu đồ tiến độ.",
                "situation": "formal"
            }
        ],
        "relatedTerms": [
            "바차트",
            "네트워크공정표",
            "크리티컬패스",
            "마일스톤",
            "공정회의"
        ]
    },
    {
        "slug": "bar-chart",
        "korean": "바차트",
        "vietnamese": "biểu đồ thanh",
        "hanja": None,
        "hanjaReading": None,
        "pronunciation": "비에우 도 탄",
        "meaningKo": "가로축을 시간, 세로축을 작업 항목으로 배치하여 각 공종의 기간을 막대(Bar) 형태로 표시한 공정표입니다. 간트차트(Gantt Chart)라고도 불리며, 직관적이고 이해하기 쉬워 건설 현장에서 가장 널리 사용됩니다. 통역 시 '막대 차트', '진도 차트'로 혼용되나, 건설 분야에서는 '바차트'로 통일하여 사용합니다. 작업 간 선후행 관계는 명확히 표현되지 않으나, 전체 공기와 각 공종의 중첩 여부를 한눈에 파악할 수 있습니다.",
        "meaningVi": "Biểu đồ tiến độ thể hiện thời gian trên trục ngang, hạng mục công việc trên trục dọc, thời lượng từng công việc bằng hình thanh (bar). Còn gọi là Gantt Chart, trực quan dễ hiểu nên được dùng phổ biến nhất tại công trường.",
        "context": "공정 관리, 시공 계획, 일정 관리",
        "contextVi": "Quản lý tiến độ, kế hoạch thi công, quản lý lịch trình",
        "culturalNote": "한국 건설현장에서는 MS Project나 Primavera로 작성한 바차트를 주간 회의 시 프로젝터로 띄워 논의하며, 진척률을 즉석에서 업데이트합니다. 베트남 현장은 Excel 기반 수작업 바차트가 많아 실시간 수정이 어렵고, 회의 후 별도로 정리하는 경우가 많습니다. 이로 인해 공정 지연 대응 속도에서 차이가 발생할 수 있습니다.",
        "commonMistakes": [
            {
                "mistake": "\"막대 차트\"로 직역하여 전문성 결여",
                "correction": "건설 분야에서는 \"bar chart\" 또는 \"biểu đồ thanh\" 그대로 사용",
                "explanation": "건설 업계 공용어로 정착된 용어는 번역하지 않는 것이 관례"
            },
            {
                "mistake": "네트워크 공정표(CPM)와 혼동",
                "correction": "바차트는 막대형, CPM은 화살표 네트워크 형태로 시각적 차이 명확",
                "explanation": "바차트는 선후행 관계 미흡, CPM은 상세 의존성 표현"
            },
            {
                "mistake": "\"진척률\" 표현 시 \"tỉ lệ\"(비율)만 사용",
                "correction": "\"tiến độ hoàn thành\"(완료 진척도) 또는 \"tỷ lệ thực hiện\"",
                "explanation": "공정 맥락에서는 '완료도' 개념을 명확히 전달해야 함"
            }
        ],
        "examples": [
            {
                "ko": "바차트를 보면 이번 달 말까지 마감공사를 끝내야 합니다.",
                "vi": "Theo biểu đồ thanh thì đến cuối tháng này phải hoàn thành công tác hoàn thiện.",
                "situation": "formal"
            },
            {
                "ko": "바차트 업데이트 좀 해주세요. 실적 반영해야죠.",
                "vi": "Cập nhật biểu đồ thanh đi. Phải phản ánh thực tế chứ.",
                "situation": "onsite"
            },
            {
                "ko": "바차트에 표시된 중첩 구간에서 인력 배치를 조율하겠습니다.",
                "vi": "Tôi sẽ điều phối phân bổ nhân lực tại đoạn trùng lặp trên biểu đồ thanh.",
                "situation": "formal"
            }
        ],
        "relatedTerms": [
            "공정표",
            "간트차트",
            "진척률",
            "마일스톤",
            "공정회의"
        ]
    },
    {
        "slug": "so-do-mang",
        "korean": "네트워크공정표",
        "vietnamese": "sơ đồ mạng",
        "hanja": None,
        "hanjaReading": None,
        "pronunciation": "서 도 망",
        "meaningKo": "각 작업을 노드(Node)와 화살표(Arrow)로 연결하여 선후행 관계와 소요 기간을 표현한 공정표입니다. CPM(Critical Path Method) 또는 PERT(Program Evaluation and Review Technique) 방식으로 작성되며, 크리티컬 패스(주공정선)를 파악하여 공기 단축 전략을 수립할 수 있습니다. 통역 시 '주공정선', '여유시간(Float)', '선행작업' 등 네트워크 특화 용어를 정확히 전달해야 하며, 대형 프로젝트에서 필수적으로 사용됩니다.",
        "meaningVi": "Biểu đồ tiến độ thể hiện mối quan hệ tiên hậu và thời gian cần thiết bằng cách kết nối các công việc qua nút (node) và mũi tên (arrow). Lập theo phương pháp CPM hoặc PERT, giúp xác định đường găng (critical path) để đưa ra chiến lược rút ngắn tiến độ.",
        "context": "공정 관리, 대형 프로젝트, CPM 분석",
        "contextVi": "Quản lý tiến độ, dự án lớn, phân tích CPM",
        "culturalNote": "한국의 대형 건설사는 네트워크 공정표를 의무화하여 정밀 공정 관리를 수행하며, PM 전문가가 Primavera 등 소프트웨어로 관리합니다. 베트남은 중소형 프로젝트에서는 바차트만 사용하는 경우가 많아, 네트워크 공정표 개념이 생소할 수 있습니다. 통역 시 개념 설명과 함께 '왜 필요한지' 맥락을 전달해야 이해도가 높아집니다.",
        "commonMistakes": [
            {
                "mistake": "\"mạng lưới\"(네트워크 일반)로 번역하여 혼동",
                "correction": "\"sơ đồ mạng tiến độ\" 또는 \"sơ đồ mạng CPM\"으로 명시",
                "explanation": "IT 네트워크와 구분하여 공정 관리 맥락 명확화"
            },
            {
                "mistake": "크리티컬 패스를 \"đường quan trọng\"(중요한 길)으로 직역",
                "correction": "\"đường găng\" 또는 \"critical path\" 그대로 사용",
                "explanation": "건설 업계 전문 용어로 정착된 표현 사용"
            },
            {
                "mistake": "여유시간(Float)을 \"thời gian rảnh\"(한가한 시간)로 오역",
                "correction": "\"thời gian dự phòng\" 또는 \"float time\"",
                "explanation": "작업 지연 허용 범위를 의미하는 기술 용어"
            }
        ],
        "examples": [
            {
                "ko": "네트워크공정표 분석 결과, 주공정선 상의 철골공사가 지연되고 있습니다.",
                "vi": "Theo phân tích sơ đồ mạng, công tác khung thép trên đường găng đang bị chậm.",
                "situation": "formal"
            },
            {
                "ko": "이 작업은 여유시간이 5일이니까 조금 늦어져도 괜찮아요.",
                "vi": "Công việc này có thời gian dự phòng 5 ngày nên chậm chút không sao.",
                "situation": "onsite"
            },
            {
                "ko": "네트워크공정표를 기반으로 Fast Track 공법을 검토하겠습니다.",
                "vi": "Chúng tôi sẽ xem xét phương pháp Fast Track dựa trên sơ đồ mạng tiến độ.",
                "situation": "formal"
            }
        ],
        "relatedTerms": [
            "크리티컬패스",
            "CPM",
            "여유시간",
            "선행작업",
            "공기단축"
        ]
    },
    {
        "slug": "duong-gang",
        "korean": "크리티컬패스",
        "vietnamese": "đường găng",
        "hanja": None,
        "hanjaReading": None,
        "pronunciation": "드엉 강",
        "meaningKo": "네트워크 공정표에서 프로젝트 전체 공기를 결정하는 가장 긴 경로로, 여유시간이 전혀 없는 작업들의 연속입니다. '주공정선'이라고도 하며, 이 경로상의 작업이 지연되면 프로젝트 전체가 지연되므로 최우선 관리 대상입니다. 통역 시 '공기에 영향을 주는 핵심 작업'이라는 개념을 명확히 전달해야 하며, 공기 단축 전략은 주로 크리티컬 패스 단축에 집중됩니다. Fast Track, 공정 단축 회의에서 반드시 등장하는 핵심 용어입니다.",
        "meaningVi": "Chuỗi công việc dài nhất trong sơ đồ mạng quyết định tổng thời gian dự án, không có thời gian dự phòng. Còn gọi là đường chính yếu, nếu các công việc trên đường này bị chậm thì toàn bộ dự án bị chậm, nên phải ưu tiên quản lý.",
        "context": "공정 관리, 공기 단축, 프로젝트 관리",
        "contextVi": "Quản lý tiến độ, rút ngắn công kỳ, quản lý dự án",
        "culturalNote": "한국 PM들은 크리티컬 패스 관리를 프로젝트 성패의 핵심으로 보며, 주간 회의에서 반드시 점검합니다. 베트남 현장에서는 이 개념이 덜 일반화되어, '가장 중요한 작업'으로만 이해하고 정량적 분석을 생략하는 경우가 있습니다. 통역 시 '왜 이 작업이 크리티컬한지' 논리를 함께 전달하면 의사소통이 원활합니다.",
        "commonMistakes": [
            {
                "mistake": "\"đường quan trọng nhất\"(가장 중요한 길)로 직역",
                "correction": "\"đường găng\" 또는 \"critical path\" 그대로 사용",
                "explanation": "건설/PM 분야 표준 용어로 정착된 표현"
            },
            {
                "mistake": "모든 지연 작업을 크리티컬 패스로 오해",
                "correction": "여유시간 없는 경로상의 작업만 해당",
                "explanation": "지연되어도 전체 공기에 영향 없는 작업은 제외"
            },
            {
                "mistake": "공기 단축을 \"giảm thời gian\"(시간 줄이기)로만 표현",
                "correction": "\"rút ngắn công kỳ\" 또는 \"단축 크리티컬 패스\"",
                "explanation": "공정 관리 맥락에서 전문 용어 사용 필요"
            }
        ],
        "examples": [
            {
                "ko": "크리티컬 패스 상의 기초공사를 2주 앞당기면 전체 공기를 단축할 수 있습니다.",
                "vi": "Nếu đẩy nhanh công tác móng trên đường găng 2 tuần thì có thể rút ngắn tổng công kỳ.",
                "situation": "formal"
            },
            {
                "ko": "이 작업은 크리티컬 패스 아니니까 좀 늦어도 괜찮아요.",
                "vi": "Việc này không phải đường găng nên chậm chút không sao.",
                "situation": "onsite"
            },
            {
                "ko": "크리티컬 패스 분석 결과를 바탕으로 인력을 재배치하겠습니다.",
                "vi": "Tôi sẽ tái phân bổ nhân lực dựa trên kết quả phân tích đường găng.",
                "situation": "formal"
            }
        ],
        "relatedTerms": [
            "네트워크공정표",
            "여유시간",
            "공기단축",
            "주공정선",
            "CPM"
        ]
    },
    {
        "slug": "cot-moc",
        "korean": "마일스톤",
        "vietnamese": "cột mốc",
        "hanja": None,
        "hanjaReading": None,
        "pronunciation": "꼿 목",
        "meaningKo": "프로젝트 진행 과정에서 중요한 이정표가 되는 시점으로, 주요 공정의 완료 시점이나 검수일, 인허가 취득일 등을 의미합니다. '이정표', '중간 목표'라고도 하며, 발주처와의 계약에서 지급 조건으로 설정되는 경우가 많습니다. 통역 시 단순 '목표일'이 아니라 '계약상 의무 이행 시점'이라는 법적 의미를 포함해야 하며, 마일스톤 달성 여부는 성과 평가와 대금 지급에 직결됩니다.",
        "meaningVi": "Thời điểm quan trọng đánh dấu tiến độ dự án như ngày hoàn thành công đoạn chính, nghiệm thu hoặc nhận phép. Còn gọi là mốc tiến độ, mục tiêu trung gian, thường được đặt làm điều kiện thanh toán trong hợp đồng với chủ đầu tư.",
        "context": "공정 관리, 계약 관리, 프로젝트 관리",
        "contextVi": "Quản lý tiến độ, quản lý hợp đồng, quản lý dự án",
        "culturalNote": "한국 건설 계약은 마일스톤 기반 기성 지급이 일반적이며, 마일스톤 미달성 시 지체상금이 부과될 수 있습니다. 베트남은 월간 기성 지급이 더 흔하여, 마일스톤 개념이 덜 엄격하게 적용됩니다. 통역 시 계약 조건과 연계하여 중요성을 강조해야 하며, '단순 목표'와 '계약 의무' 차이를 명확히 해야 분쟁을 예방할 수 있습니다.",
        "commonMistakes": [
            {
                "mistake": "\"mục tiêu\"(목표)로만 번역하여 계약적 의미 누락",
                "correction": "\"cột mốc hợp đồng\" 또는 \"cột mốc quan trọng\"",
                "explanation": "법적 구속력 있는 이정표임을 명시"
            },
            {
                "mistake": "마일스톤과 일반 작업 완료일을 동일시",
                "correction": "마일스톤은 주요 공정 완료 시점, 일반 작업은 세부 태스크",
                "explanation": "중요도와 계약상 의미가 다름"
            },
            {
                "mistake": "지연 시 \"không đạt mục tiêu\"(목표 미달)로만 표현",
                "correction": "\"trễ cột mốc\" 또는 \"không hoàn thành đúng cột mốc\"",
                "explanation": "계약 위반 소지를 명확히 전달"
            }
        ],
        "examples": [
            {
                "ko": "다음 마일스톤은 구조체 완료 검수이며, 기한은 이번 달 말입니다.",
                "vi": "Cột mốc tiếp theo là nghiệm thu hoàn thành kết cấu, thời hạn cuối tháng này.",
                "situation": "formal"
            },
            {
                "ko": "마일스톤 맞추려면 인력 좀 더 투입해야겠어요.",
                "vi": "Để đúng cột mốc thì phải đầu tư thêm nhân lực mới được.",
                "situation": "onsite"
            },
            {
                "ko": "계약서 상 마일스톤 3개 중 2개는 달성했으니 80% 기성을 청구할 수 있습니다.",
                "vi": "Trong hợp đồng có 3 cột mốc, đã đạt 2 cột mốc nên có thể yêu cầu thanh toán 80% khối lượng.",
                "situation": "formal"
            }
        ],
        "relatedTerms": [
            "공정표",
            "기성",
            "검수",
            "계약",
            "지체상금"
        ]
    },
    {
        "slug": "quan-he-tien-hau",
        "korean": "선후행관계",
        "vietnamese": "quan hệ tiên hậu",
        "hanja": "先後行關係",
        "hanjaReading": "선(먼저 선) + 후(뒤 후) + 행(다닐 행) + 관(관계할 관) + 계(잇닿을 계)",
        "pronunciation": "꽌 헤 띠엔 허우",
        "meaningKo": "공정 계획에서 한 작업이 다른 작업에 앞서거나 뒤따라 수행되어야 하는 순서 관계를 의미합니다. 예를 들어 거푸집 조립(선행작업) 후 철근 배근(후행작업)이 가능하며, 이러한 의존성을 무시하면 재작업이나 품질 문제가 발생합니다. 통역 시 '먼저 해야 할 일', '나중에 할 일'이라는 단순 개념이 아니라, 기술적·안전적 필연성을 포함한 의미임을 전달해야 합니다. 네트워크 공정표 작성의 기초가 됩니다.",
        "meaningVi": "Mối quan hệ thứ tự trong kế hoạch tiến độ, một công việc phải thực hiện trước hoặc sau công việc khác. Ví dụ: lắp ván khuôn (tiên hành) xong mới được đặt cốt thép (hậu hành), bỏ qua quan hệ này sẽ dẫn đến làm lại hoặc vấn đề chất lượng.",
        "context": "공정 관리, 시공 계획, 네트워크 공정",
        "contextVi": "Quản lý tiến độ, kế hoạch thi công, sơ đồ mạng",
        "culturalNote": "한국 현장에서는 선후행 관계를 Primavera 등 소프트웨어로 체계화하며, 변경 시 전체 공정에 미치는 영향을 자동 계산합니다. 베트남 중소형 현장은 경험 기반 판단이 많아, 선후행 관계가 암묵적으로 관리되는 경우가 있습니다. 통역 시 '왜 이 순서인지' 기술적 근거를 함께 설명하면 신뢰도가 높아집니다.",
        "commonMistakes": [
            {
                "mistake": "\"trước sau\"(전후)로만 번역하여 기술적 의미 누락",
                "correction": "\"quan hệ tiên hậu\" 또는 \"thứ tự phụ thuộc\"",
                "explanation": "단순 시간 순서가 아닌 논리적 의존성 강조"
            },
            {
                "mistake": "선행작업을 \"công việc đầu tiên\"(첫 작업)으로 오역",
                "correction": "\"công việc tiên hành\" 또는 \"predecessor\"",
                "explanation": "프로젝트 최초 작업과 혼동 방지"
            },
            {
                "mistake": "의존성을 무시하고 병렬 작업으로 오해",
                "correction": "\"không thể làm đồng thời\" 명시",
                "explanation": "순차 필연성을 명확히 전달해야 재작업 방지"
            }
        ],
        "examples": [
            {
                "ko": "선후행 관계를 고려하면 이 두 작업은 동시에 진행할 수 없습니다.",
                "vi": "Xét quan hệ tiên hậu thì hai công việc này không thể làm cùng lúc.",
                "situation": "formal"
            },
            {
                "ko": "거푸집 먼저 치고 철근 넣어야죠. 순서 바꾸면 안 돼요.",
                "vi": "Phải lắp ván khuôn trước rồi mới đặt thép. Đổi thứ tự không được.",
                "situation": "onsite"
            },
            {
                "ko": "선후행 관계 분석을 통해 병렬 가능한 작업을 찾아 공기를 단축하겠습니다.",
                "vi": "Qua phân tích quan hệ tiên hậu, chúng tôi sẽ tìm các công việc có thể song song để rút ngắn công kỳ.",
                "situation": "formal"
            }
        ],
        "relatedTerms": [
            "네트워크공정표",
            "선행작업",
            "후행작업",
            "공정표",
            "CPM"
        ]
    },
    {
        "slug": "rut-ngan-cong-ky",
        "korean": "공기단축",
        "vietnamese": "rút ngắn công kỳ",
        "hanja": "工期短縮",
        "hanjaReading": "공(장인 공) + 기(기약할 기) + 단(짧을 단) + 축(줄일 축)",
        "pronunciation": "쭛 응언 꽁 끼",
        "meaningKo": "계획된 공사 기간을 원래보다 짧게 조정하는 것으로, 발주처 요구, 페널티 회피, 조기 준공 인센티브 등의 이유로 수행됩니다. Fast Track, 인력·장비 증설, 야간 작업, 공법 변경 등의 방법이 있으며, 추가 비용과 안전 리스크를 수반합니다. 통역 시 '왜 단축하는지', '어떻게 단축하는지', '비용은 누가 부담하는지'를 명확히 전달해야 하며, 무리한 단축은 품질 저하와 안전사고로 이어질 수 있어 신중한 논의가 필요합니다.",
        "meaningVi": "Điều chỉnh giảm thời gian thi công so với kế hoạch ban đầu, do yêu cầu chủ đầu tư, tránh phạt chậm tiến độ hoặc ưu đãi hoàn thành sớm. Có thể dùng Fast Track, tăng nhân lực-thiết bị, làm đêm, thay đổi công pháp nhưng kèm theo chi phí và rủi ro an toàn.",
        "context": "공정 관리, 계약 관리, 프로젝트 관리",
        "contextVi": "Quản lý tiến độ, quản lý hợp đồng, quản lý dự án",
        "culturalNote": "한국 발주처는 공기 단축 요구가 잦으며, 시공사는 추가 비용 협상을 통해 대응합니다. 베트남은 공기 연장이 상대적으로 쉽게 승인되어, 무리한 단축보다는 현실적 일정 조정을 선호합니다. 통역 시 한국 측의 '빨리빨리' 문화와 베트남 측의 '안전 우선' 문화 차이를 중재하는 역할이 중요하며, 양측이 납득할 수 있는 근거를 제시해야 합니다.",
        "commonMistakes": [
            {
                "mistake": "\"giảm thời gian\"(시간 줄이기)로만 표현",
                "correction": "\"rút ngắn công kỳ\" 또는 \"단축 tiến độ\"",
                "explanation": "건설 전문 용어로 공사 기간 특정 표현 사용"
            },
            {
                "mistake": "비용 증가 없이 단축 가능하다고 오해",
                "correction": "추가 인력, 장비, 야간 작업 등 비용 수반 명시",
                "explanation": "공기 단축 = 비용 증가는 건설의 상식"
            },
            {
                "mistake": "Fast Track을 \"nhanh\"(빠르다)로만 직역",
                "correction": "\"Fast Track\" 그대로 사용 또는 \"병렬 공정\"으로 설명",
                "explanation": "설계와 시공을 병렬화하는 특정 기법"
            }
        ],
        "examples": [
            {
                "ko": "발주처가 2개월 공기 단축을 요구하고 있어 Fast Track 방안을 검토 중입니다.",
                "vi": "Chủ đầu tư yêu cầu rút ngắn công kỳ 2 tháng nên đang xem xét phương án Fast Track.",
                "situation": "formal"
            },
            {
                "ko": "공기 단축하려면 야근하고 장비 더 넣어야 해요. 돈 많이 들 텐데요.",
                "vi": "Muốn rút ngắn công kỳ thì phải tăng ca và thêm thiết bị. Tốn tiền lắm đấy.",
                "situation": "onsite"
            },
            {
                "ko": "크리티컬 패스 상의 작업을 단축하면 전체 공기를 1개월 줄일 수 있습니다.",
                "vi": "Nếu rút ngắn công việc trên đường găng thì có thể giảm tổng công kỳ 1 tháng.",
                "situation": "formal"
            }
        ],
        "relatedTerms": [
            "크리티컬패스",
            "Fast Track",
            "공정표",
            "인력증설",
            "지체상금"
        ]
    },
    {
        "slug": "nhat-bao-thi-cong",
        "korean": "시공일보",
        "vietnamese": "nhật báo thi công",
        "hanja": "施工日報",
        "hanjaReading": "시(베풀 시) + 공(장인 공) + 일(날 일) + 보(알릴 보)",
        "pronunciation": "녓 바오 티 꽁",
        "meaningKo": "매일 현장에서 수행한 작업 내용, 투입 인력, 장비, 자재, 기상 상황, 안전 점검 사항 등을 기록한 일일 보고서입니다. '작업일보'라고도 하며, 클레임 발생 시 법적 증빙 자료로 활용되므로 정확하고 상세한 기록이 필수입니다. 통역 시 단순 '일지'가 아니라 '법적 기록물'이라는 성격을 전달해야 하며, 누락이나 허위 기재는 책임 문제로 이어질 수 있습니다. 감리단과 발주처도 열람 가능합니다.",
        "meaningVi": "Báo cáo hàng ngày ghi chép nội dung thi công, nhân lực, thiết bị, vật tư đầu vào, tình hình thời tiết, kiểm tra an toàn. Còn gọi là nhật ký công tác, là tài liệu chứng minh pháp lý khi có khiếu nại nên phải ghi chính xác chi tiết.",
        "context": "현장 관리, 문서 관리, 안전 관리",
        "contextVi": "Quản lý hiện trường, quản lý tài liệu, quản lý an toàn",
        "culturalNote": "한국 현장은 시공일보를 디지털화(모바일 앱)하여 실시간 공유하며, 감리와 발주처가 즉시 확인 가능합니다. 베트남은 종이 기반 수기 작성이 많아 집계와 공유가 느립니다. 통역 시 '기록의 법적 중요성'을 강조하고, 사진 첨부, 기상 상황, 안전 조치 내용까지 상세히 기록해야 분쟁 시 유리하다는 점을 전달하면 기록 품질이 향상됩니다.",
        "commonMistakes": [
            {
                "mistake": "\"nhật ký\"(일기)로 번역하여 법적 성격 누락",
                "correction": "\"nhật báo thi công\" 또는 \"báo cáo thi công hàng ngày\"",
                "explanation": "법적 증빙 문서임을 명시"
            },
            {
                "mistake": "기상 상황을 \"thời tiết tốt/xấu\"(좋다/나쁘다)로만 기록",
                "correction": "구체적 온도, 강수량, 풍속 등 수치 기록",
                "explanation": "클레임 시 공정 지연 정당성 입증 자료"
            },
            {
                "mistake": "안전 점검을 \"không có vấn đề\"(문제없음)로 일괄 기재",
                "correction": "점검 항목별 구체적 결과 기록",
                "explanation": "사고 발생 시 점검 누락 책임 소재 명확화"
            }
        ],
        "examples": [
            {
                "ko": "시공일보에 오늘 콘크리트 타설량과 투입 인원을 정확히 기록해 주세요.",
                "vi": "Hãy ghi chính xác khối lượng bê tông đổ và số nhân lực vào nhật báo thi công hôm nay.",
                "situation": "formal"
            },
            {
                "ko": "일보 작성 좀 꼼꼼히 해요. 나중에 클레임 나면 이거 증거니까요.",
                "vi": "Viết nhật báo kỹ càng vào. Sau này có khiếu nại thì đây là bằng chứng.",
                "situation": "onsite"
            },
            {
                "ko": "지난주 시공일보를 검토한 결과, 우천으로 3일간 작업이 중단되었음을 확인했습니다.",
                "vi": "Sau khi rà soát nhật báo thi công tuần trước, xác nhận đã dừng việc 3 ngày do mưa.",
                "situation": "formal"
            }
        ],
        "relatedTerms": [
            "작업일보",
            "안전점검",
            "클레임",
            "감리",
            "현장관리"
        ]
    },
    {
        "slug": "hop-tien-do-tuan",
        "korean": "주간공정회의",
        "vietnamese": "họp tiến độ tuần",
        "hanja": "週間工程會議",
        "hanjaReading": "주(두루 주) + 간(사이 간) + 공(장인 공) + 정(과정 정) + 회(모일 회) + 의(의논할 의)",
        "pronunciation": "홉 띠엔 도 뚜언",
        "meaningKo": "매주 정기적으로 개최되는 공정 점검 회의로, 전주 실적 대비 계획, 금주 작업 계획, 애로사항, 안전 이슈 등을 논의합니다. 시공사, 감리단, 발주처, 협력업체가 참석하며, 회의록이 공식 기록으로 남습니다. 통역 시 '단순 진행 상황 공유'가 아니라 '공식 약속과 책임 분담의 장'이라는 성격을 전달해야 하며, 회의에서 합의된 사항은 반드시 이행되어야 합니다. 공정 지연 시 원인과 만회 대책이 집중 논의됩니다.",
        "meaningVi": "Cuộc họp định kỳ hàng tuần kiểm tra tiến độ, thảo luận thực tế so với kế hoạch tuần trước, kế hoạch tuần này, khó khăn và vấn đề an toàn. Có sự tham gia của nhà thầu, giám sát, chủ đầu tư, nhà thầu phụ, biên bản họp là tài liệu chính thức.",
        "context": "공정 관리, 현장 관리, 회의 관리",
        "contextVi": "Quản lý tiến độ, quản lý hiện trường, quản lý cuộc họp",
        "culturalNote": "한국 현장의 주간 공정회의는 매우 형식적이고 체계적이며, 바차트를 프로젝터로 띄워 실적을 실시간 업데이트합니다. 발언은 직급 순서대로 하고, 회의록은 당일 배포됩니다. 베트남 현장은 자유로운 토론 분위기이며, 회의록 정리가 며칠 지연되는 경우도 있습니다. 통역 시 한국 측의 '형식 중시' 문화를 이해시키고, 회의 중 합의 사항을 명확히 정리해 주면 사후 혼란을 방지할 수 있습니다.",
        "commonMistakes": [
            {
                "mistake": "\"cuộc họp hàng tuần\"(주간 회의)로만 번역",
                "correction": "\"họp tiến độ tuần\" 또는 \"họp kiểm tra công trình tuần\"",
                "explanation": "공정 점검 목적을 명시"
            },
            {
                "mistake": "회의록을\"biên bản\"(조서) 일반으로 표현",
                "correction": "\"biên bản họp tiến độ\" 또는 \"minutes of meeting\"",
                "explanation": "공식 기록물로서의 법적 성격 강조"
            },
            {
                "mistake": "만회 대책을 \"cách khắc phục\"(해결 방법)로만 표현",
                "correction": "\"phương án gỡ tiến độ\" 또는 \"catch-up plan\"",
                "explanation": "지연된 공정을 만회하는 구체적 계획 의미"
            }
        ],
        "examples": [
            {
                "ko": "주간공정회의에서 지난주 공정률이 계획 대비 5% 부족하다고 지적받았습니다.",
                "vi": "Tại họp tiến độ tuần, bị chỉ ra tỷ lệ hoàn thành tuần trước thiếu 5% so với kế hoạch.",
                "situation": "formal"
            },
            {
                "ko": "주간회의 준비 잘해요. 발주처 오시니까 자료 빈틈없이 챙겨야죠.",
                "vi": "Chuẩn bị họp tuần kỹ nhé. Chủ đầu tư đến nên tài liệu phải chu đáo.",
                "situation": "onsite"
            },
            {
                "ko": "주간공정회의 결과, 철근 반입 지연으로 인해 다음 주 타설이 불가하다고 합의했습니다.",
                "vi": "Kết quả họp tiến độ tuần, thống nhất không thể đổ bê tông tuần sau do thép về muộn.",
                "situation": "formal"
            }
        ],
        "relatedTerms": [
            "공정표",
            "바차트",
            "진척률",
            "회의록",
            "만회대책"
        ]
    },
    {
        "slug": "nhat-ky-cong-tac",
        "korean": "작업일보",
        "vietnamese": "nhật ký công tác",
        "hanja": "作業日報",
        "hanjaReading": "작(지을 작) + 업(업 업) + 일(날 일) + 보(알릴 보)",
        "pronunciation": "녓 끼 꽁 딱",
        "meaningKo": "현장 기술자가 매일 수행한 세부 작업 내용을 기록하는 일지로, 시공일보보다 개인 중심의 상세 기록입니다. 작업 시간, 완료 항목, 미완료 사유, 특이사항, 품질·안전 이슈 등을 담으며, 개인 성과 평가와 교육 자료로 활용됩니다. 통역 시 '시공일보'(현장 전체)와 '작업일보'(개인 담당) 차이를 구분해야 하며, 작업일보는 주로 기술자 개인의 책임 범위를 명확히 하기 위한 자료로 사용됩니다.",
        "meaningVi": "Nhật ký ghi chép chi tiết nội dung công việc hàng ngày của kỹ thuật viên hiện trường, tập trung vào cá nhân hơn nhật báo thi công. Ghi thời gian làm việc, hạng mục hoàn thành, lý do chưa xong, vấn đề đặc biệt, chất lượng-an toàn, dùng cho đánh giá cá nhân và tài liệu đào tạo.",
        "context": "현장 관리, 개인 업무 관리, 품질 관리",
        "contextVi": "Quản lý hiện trường, quản lý công việc cá nhân, quản lý chất lượng",
        "culturalNote": "한국 건설사는 신입 기술자에게 작업일보 작성을 의무화하여 현장 경험을 체계적으로 축적하도록 합니다. 베트남은 구두 보고가 많아 문서 기록이 상대적으로 소홀합니다. 통역 시 '기록 문화'의 중요성을 강조하고, 작업일보가 개인 성장과 분쟁 시 자기 보호 수단이 된다는 점을 설명하면 기록 습관 정착에 도움이 됩니다.",
        "commonMistakes": [
            {
                "mistake": "시공일보와 작업일보를 구분하지 않음",
                "correction": "시공일보(현장 전체), 작업일보(개인 담당) 명확히 구분",
                "explanation": "용도와 작성 주체가 다름"
            },
            {
                "mistake": "\"nhật ký cá nhân\"(개인 일기)로 오해",
                "correction": "\"nhật ký công tác\" 또는 \"daily work log\"",
                "explanation": "공식 업무 기록임을 명시"
            },
            {
                "mistake": "미완료 사유를 \"chưa làm\"(안 했음)으로만 기재",
                "correction": "구체적 이유(자재 미입고, 선행작업 미완 등) 기록",
                "explanation": "책임 소재와 개선 방향 파악 위해 필수"
            }
        ],
        "examples": [
            {
                "ko": "작업일보에 오늘 완료한 배근 구간과 내일 계획을 작성해 주세요.",
                "vi": "Hãy ghi đoạn đặt cốt thép hoàn thành hôm nay và kế hoạch ngày mai vào nhật ký công tác.",
                "situation": "formal"
            },
            {
                "ko": "일보 쓰는 거 귀찮아도 꼭 해야 해요. 나중에 내 실적 증명 자료예요.",
                "vi": "Dù phiền nhưng phải viết nhật ký. Sau này là tài liệu chứng minh thành tích của mình.",
                "situation": "onsite"
            },
            {
                "ko": "작업일보를 검토한 결과, 철근 검수 지연으로 3일간 작업이 중단되었습니다.",
                "vi": "Sau khi rà soát nhật ký công tác, xác nhận dừng việc 3 ngày do chậm nghiệm thu thép.",
                "situation": "formal"
            }
        ],
        "relatedTerms": [
            "시공일보",
            "현장기술자",
            "업무기록",
            "성과평가",
            "안전점검"
        ]
    }
]

def main():
    """메인 실행 함수"""
    print("=" * 60)
    print("Construction Terms Addition Script v2-o")
    print("Theme: 공정관리/시공계획 (Schedule & Planning)")
    print("=" * 60)

    # 1. 기존 파일 읽기
    print(f"\n[1/3] Reading: {CONSTRUCTION_JSON}")
    try:
        with open(CONSTRUCTION_JSON, 'r', encoding='utf-8') as f:
            existing_data = json.load(f)
        print(f"✓ Loaded {len(existing_data)} existing terms")
    except FileNotFoundError:
        print("✗ File not found!")
        return
    except json.JSONDecodeError as e:
        print(f"✗ JSON parse error: {e}")
        return

    # 2. 중복 체크
    print("\n[2/3] Checking duplicates...")
    existing_slugs = {term['slug'] for term in existing_data}
    new_slugs = {term['slug'] for term in NEW_TERMS}
    duplicates = existing_slugs & new_slugs

    if duplicates:
        print(f"✗ Duplicate slugs found: {duplicates}")
        print("Please fix duplicates before running!")
        return

    print(f"✓ No duplicates. Adding {len(NEW_TERMS)} new terms")

    # 3. 데이터 병합 및 저장
    print("\n[3/3] Merging and saving...")
    merged_data = existing_data + NEW_TERMS

    try:
        with open(CONSTRUCTION_JSON, 'w', encoding='utf-8') as f:
            json.dump(merged_data, f, ensure_ascii=False, indent=2)
        print(f"✓ Successfully saved {len(merged_data)} terms")
    except Exception as e:
        print(f"✗ Save error: {e}")
        return

    # 4. 추가된 용어 목록 출력
    print("\n" + "=" * 60)
    print("Added Terms:")
    print("=" * 60)
    for i, term in enumerate(NEW_TERMS, 1):
        print(f"{i:2d}. {term['korean']:15s} ({term['slug']})")
        print(f"    {term['vietnamese']}")

    print("\n" + "=" * 60)
    print(f"✓ Total: {len(merged_data)} terms in construction.json")
    print("=" * 60)

if __name__ == "__main__":
    main()
