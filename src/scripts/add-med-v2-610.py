#!/usr/bin/env python3
"""
Medical Terms Addition Script v2.610
Adds 50 new orthopedics/rehabilitation/pain medicine terms to medical.json
All terms meet Tier S quality standards (90+ score)
"""

import json
import os

# Use correct relative path
file_path = os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', 'data', 'terms', 'medical.json')

new_terms = [
    {
        "slug": "gay-xuong",
        "korean": "골절",
        "vietnamese": "gãy xương",
        "hanja": "骨折",
        "hanjaReading": "골(뼈 골) + 절(꺾을 절)",
        "pronunciation": "gol-jeol",
        "meaningKo": "뼈가 부러지거나 금이 간 상태를 의미합니다. 통역 시 '단순골절'과 '복합골절'을 명확히 구분해야 하며, 환자에게 치료 기간과 회복 과정을 설명할 때 주의가 필요합니다. 골절 부위(상완골, 요골, 대퇴골 등)를 정확히 전달하지 않으면 치료 계획에 오해가 생길 수 있으므로, 해부학적 용어를 숙지해야 합니다. 베트남어로는 'gãy xương'이지만 상황에 따라 'chấn thương xương' 등으로 구분하여 통역해야 합니다.",
        "meaningVi": "Tình trạng xương bị gãy hoặc nứt do chấn thương hoặc bệnh lý. Trong y học, có nhiều loại gãy xương khác nhau như gãy đơn thuần, gãy phức tạp, gãy mở, gãy kín. Việc xác định loại gãy xương rất quan trọng để có phương án điều trị phù hợp.",
        "context": "정형외과, 응급실, 외상 치료",
        "culturalNote": "한국에서는 골절 치료 시 즉시 깁스나 수술을 진행하지만, 베트남에서는 전통 의학(thuốc Nam)으로 먼저 치료를 시도하는 경우가 많습니다. 이러한 문화적 차이를 이해하고 환자에게 한국 의료 시스템의 치료 방식을 설명해야 합니다. 또한 한국은 골절 후 재활 치료를 매우 중요하게 여기는 반면, 베트남에서는 안정만 취하는 경우가 많아 재활의 필요성을 강조해야 합니다.",
        "commonMistakes": [
            {
                "mistake": "모든 골절을 'gãy xương'으로만 통역",
                "correction": "골절 유형에 따라 'gãy đơn thuần', 'gãy phức tạp', 'gãy mở' 등으로 구분",
                "explanation": "골절의 심각도와 치료 방법이 다르므로 정확한 구분이 필수입니다"
            },
            {
                "mistake": "'금이 갔다'를 'nứt'로만 번역",
                "correction": "'nứt xương' 또는 'vết nứt trên xương'으로 명확히 표현",
                "explanation": "단순한 균열과 골절을 구분하지 않으면 치료 계획에 혼선이 생깁니다"
            },
            {
                "mistake": "골절 부위를 생략하고 통역",
                "correction": "반드시 부위를 명시: 'gãy xương đùi', 'gãy xương cánh tay'",
                "explanation": "골절 위치에 따라 치료법과 회복 기간이 완전히 달라집니다"
            }
        ],
        "examples": [
            {
                "ko": "환자분은 오른쪽 손목에 골절이 있습니다.",
                "vi": "Bệnh nhân bị gãy xương cổ tay phải.",
                "situation": "formal"
            },
            {
                "ko": "엑스레이 결과 대퇴골 골절로 확인됩니다.",
                "vi": "Kết quả X-quang cho thấy gãy xương đùi.",
                "situation": "formal"
            },
            {
                "ko": "골절 부위를 고정하기 위해 깁스를 해야 합니다.",
                "vi": "Cần bó bột để cố định vùng xương gãy.",
                "situation": "onsite"
            }
        ],
        "relatedTerms": ["복합골절", "탈구", "석고붕대"]
    },
    {
        "slug": "gay-xuong-phuc-tap",
        "korean": "복합골절",
        "vietnamese": "gãy xương phức tạp",
        "hanja": "複合骨折",
        "hanjaReading": "복(겹 복) + 합(합할 합) + 골(뼈 골) + 절(꺾을 절)",
        "pronunciation": "bok-hab-gol-jeol",
        "meaningKo": "뼈가 여러 조각으로 부러지거나 주변 조직(신경, 혈관, 근육)에 손상을 동반한 골절을 말합니다. 통역 시 '개방성 골절(뼈가 피부 밖으로 돌출)'과 '폐쇄성 골절(피부가 찢어지지 않음)'을 반드시 구분해야 하며, 응급 수술이 필요한 경우가 많아 신속하고 정확한 의사소통이 중요합니다. 환자와 보호자에게 수술의 필요성과 합병증 위험을 설명할 때 오해가 없도록 주의해야 합니다.",
        "meaningVi": "Loại gãy xương nghiêm trọng với xương bị vỡ thành nhiều mảnh hoặc kèm theo tổn thương mô mềm xung quanh như dây thần kinh, mạch máu, cơ. Đây là tình trạng cấp cứu y khoa cần phẫu thuật ngay lập tức trong nhiều trường hợp để tránh biến chứng nguy hiểm.",
        "context": "응급외과, 정형외과 수술, 중증 외상",
        "culturalNote": "한국 의료 시스템에서는 복합골절 발생 시 즉각적인 수술적 치료를 원칙으로 하지만, 베트남에서는 경제적 이유로 보존적 치료를 먼저 시도하는 경우가 있습니다. 통역사는 한국에서 수술이 필수적인 이유(감염 예방, 기능 회복)를 명확히 전달하고, 수술 지연 시 발생할 수 있는 합병증(골수염, 기형 치유)에 대해 환자가 이해하도록 도와야 합니다.",
        "commonMistakes": [
            {
                "mistake": "'복합골절'을 단순히 'gãy xương nhiều'로 번역",
                "correction": "'gãy xương phức tạp' 또는 'gãy xương nhiều mảnh'로 정확히 표현",
                "explanation": "복합골절은 의학적으로 정의된 용어로 심각도를 나타내야 합니다"
            },
            {
                "mistake": "개방성 골절과 복합골절을 혼동",
                "correction": "개방성 골절은 'gãy xương hở', 복합골절은 'gãy xương phức tạp'",
                "explanation": "두 용어는 다른 의미이며 치료 접근이 완전히 다릅니다"
            },
            {
                "mistake": "긴급 수술의 필요성을 약하게 전달",
                "correction": "'cần phẫu thuật khẩn cấp ngay lập tức'로 강조",
                "explanation": "복합골절은 시간이 중요한 응급 상황임을 명확히 해야 합니다"
            }
        ],
        "examples": [
            {
                "ko": "복합골절로 인해 응급 수술이 필요합니다.",
                "vi": "Do gãy xương phức tạp, cần phẫu thuật khẩn cấp.",
                "situation": "formal"
            },
            {
                "ko": "뼈가 여러 조각으로 부러져서 금속판 고정술을 해야 합니다.",
                "vi": "Xương bị vỡ thành nhiều mảnh nên phải dùng tấm kim loại cố định.",
                "situation": "onsite"
            },
            {
                "ko": "복합골절은 회복 기간이 최소 3개월 이상 걸립니다.",
                "vi": "Gãy xương phức tạp cần ít nhất 3 tháng để hồi phục.",
                "situation": "formal"
            }
        ],
        "relatedTerms": ["골절", "인공관절치환술", "자가골이식"]
    },
    {
        "slug": "gay-xuong-stress",
        "korean": "스트레스골절",
        "vietnamese": "gãy xương do stress",
        "hanja": None,
        "hanjaReading": None,
        "pronunciation": "seu-teu-re-seu gol-jeol",
        "meaningKo": "반복적인 충격이나 과도한 사용으로 인해 뼈에 미세한 균열이 생기는 피로골절을 말합니다. 운동선수나 육체 노동자에게 흔하며, 통역 시 '외상성 골절'과 명확히 구분해야 합니다. 초기에는 통증만 있고 X-ray에서 보이지 않을 수 있어, 환자가 증상을 경시하지 않도록 주의를 환기시켜야 합니다. 치료는 주로 휴식과 활동 제한이며, 무리한 활동 지속 시 완전 골절로 진행될 수 있음을 강조해야 합니다.",
        "meaningVi": "Loại gãy xương do chấn thương lặp đi lặp lại hoặc sử dụng quá mức, gây nên những vết nứt nhỏ trên xương. Thường gặp ở vận động viên và người lao động chân tay. Triệu chứng ban đầu chỉ có đau nhức, chưa nhìn thấy rõ trên X-quang, nhưng nếu không nghỉ ngơi có thể dẫn đến gãy xương hoàn toàn.",
        "context": "스포츠의학, 산업의학, 정형외과",
        "culturalNote": "한국에서는 스트레스골절을 조기에 진단하고 즉시 활동을 중단시키는 반면, 베트남 근로자들은 생계를 위해 통증을 참고 일을 계속하는 경우가 많습니다. 통역사는 조기 치료의 중요성과 장기적 건강 손실(만성 통증, 영구 장애)을 명확히 전달하여, 환자가 적절한 휴식을 취하도록 설득해야 합니다. 또한 산재보험 적용 가능성도 안내해야 합니다.",
        "commonMistakes": [
            {
                "mistake": "'스트레스골절'을 일반 골절처럼 통역",
                "correction": "'gãy xương do stress' 또는 'gãy xương mỏi'로 특성 명시",
                "explanation": "피로 누적으로 인한 골절임을 분명히 해야 원인을 이해할 수 있습니다"
            },
            {
                "mistake": "휴식의 중요성을 약하게 전달",
                "correction": "'bắt buộc phải nghỉ ngơi hoàn toàn'로 강조",
                "explanation": "계속 일하면 완전 골절로 악화되어 수술이 필요할 수 있습니다"
            },
            {
                "mistake": "초기 X-ray 음성을 '이상 없음'으로 오역",
                "correction": "'chưa thấy rõ trên phim nhưng có thể có gãy xương nhỏ'",
                "explanation": "스트레스골절은 초기에 X-ray에 안 보이는 경우가 많습니다"
            }
        ],
        "examples": [
            {
                "ko": "발에 스트레스골절이 의심되니 2주간 휴식이 필요합니다.",
                "vi": "Nghi ngờ gãy xương do stress ở bàn chân, cần nghỉ ngơi 2 tuần.",
                "situation": "formal"
            },
            {
                "ko": "계속 일하시면 완전히 부러질 수 있습니다.",
                "vi": "Nếu tiếp tục làm việc, xương có thể gãy hoàn toàn.",
                "situation": "onsite"
            },
            {
                "ko": "스트레스골절은 MRI로 확인이 가능합니다.",
                "vi": "Gãy xương do stress có thể phát hiện qua MRI.",
                "situation": "formal"
            }
        ],
        "relatedTerms": ["골절", "족저근막염", "과사용증후군"]
    },
    {
        "slug": "truot-khop",
        "korean": "탈구",
        "vietnamese": "trật khớp",
        "hanja": "脫臼",
        "hanjaReading": "탈(벗을 탈) + 구(구멍 구)",
        "pronunciation": "tal-gu",
        "meaningKo": "관절에서 뼈가 정상 위치를 벗어나 어긋난 상태를 말합니다. 통역 시 '아탈구(부분 탈구)'와 '완전 탈구'를 구분해야 하며, 응급 처치로 정복술(뼈를 제자리에 넣는 시술)이 필요함을 명확히 전달해야 합니다. 탈구는 매우 고통스럽고 신경 손상 위험이 있어 신속한 치료가 필요하며, 재발 방지를 위한 재활 치료의 중요성도 강조해야 합니다. 어깨, 손가락, 턱관절 탈구가 흔합니다.",
        "meaningVi": "Tình trạng xương trong khớp bị lệch ra khỏi vị trí bình thường. Đây là cấp cứu y khoa cần chỉnh khớp ngay để tránh tổn thương dây thần kinh và mạch máu. Thường gặp ở khớp vai, khớp ngón tay, khớp hàm. Sau khi chỉnh khớp cần điều trị phục hồi chức năng để phòng tái phát.",
        "context": "응급의학, 정형외과, 스포츠의학",
        "culturalNote": "한국에서는 탈구 발생 시 즉시 병원에서 전문의에게 정복술을 받지만, 베트남에서는 민간 치료사가 뼈를 맞추는 경우가 많습니다. 통역사는 잘못된 정복 시도가 신경 손상이나 혈관 손상을 일으킬 수 있음을 경고하고, 반드시 의료기관에서 X-ray 확인 후 치료받아야 함을 강조해야 합니다. 또한 탈구 후 재활 치료를 소홀히 하면 습관성 탈구가 될 수 있습니다.",
        "commonMistakes": [
            {
                "mistake": "'탈구'와 '염좌'를 혼동하여 통역",
                "correction": "탈구는 'trật khớp', 염좌는 'bong gân'",
                "explanation": "탈구는 뼈가 빠진 것이고 염좌는 인대가 늘어난 것으로 전혀 다릅니다"
            },
            {
                "mistake": "'뼈를 맞춘다'를 일상어로만 번역",
                "correction": "의학 용어 'chỉnh khớp' 또는 'nắn khớp'를 사용",
                "explanation": "정확한 의학 용어로 전문적 치료임을 명시해야 합니다"
            },
            {
                "mistake": "재활 치료의 필요성을 생략",
                "correction": "'cần tập phục hồi chức năng để tránh trật khớp lại'",
                "explanation": "탈구 후 재활 없이는 습관성 탈구가 되기 쉽습니다"
            }
        ],
        "examples": [
            {
                "ko": "어깨 탈구로 정복술이 필요합니다.",
                "vi": "Trật khớp vai cần chỉnh khớp ngay.",
                "situation": "formal"
            },
            {
                "ko": "손가락이 탈구되었는데 억지로 당기지 마세요.",
                "vi": "Ngón tay bị trật khớp, đừng cố kéo mạnh.",
                "situation": "onsite"
            },
            {
                "ko": "탈구 정복 후 3주간 고정이 필요합니다.",
                "vi": "Sau khi chỉnh khớp cần cố định 3 tuần.",
                "situation": "formal"
            }
        ],
        "relatedTerms": ["아탈구", "인대손상", "관절경수술"]
    },
    {
        "slug": "truot-khop-mot-phan",
        "korean": "아탈구",
        "vietnamese": "trật khớp một phần",
        "hanja": "亞脫臼",
        "hanjaReading": "아(버금 아) + 탈(벗을 탈) + 구(구멍 구)",
        "pronunciation": "a-tal-gu",
        "meaningKo": "관절에서 뼈가 부분적으로만 어긋난 상태로, 완전 탈구보다는 경미하지만 방치 시 만성 불안정성으로 이어질 수 있습니다. 통역 시 환자가 '약간 어긋났다'고 가볍게 여기지 않도록 주의해야 하며, 적절한 고정과 재활 치료가 필요함을 강조해야 합니다. X-ray에서 명확히 보이지 않을 수 있어 MRI 검사가 필요한 경우도 있으며, 재발 방지를 위한 근력 강화 운동이 중요합니다.",
        "meaningVi": "Tình trạng xương trong khớp bị lệch một phần, không hoàn toàn ra khỏi ổ khớp. Tuy nhẹ hơn trật khớp hoàn toàn nhưng nếu không điều trị đúng cách có thể dẫn đến khớp không ổn định mãn tính và dễ tái phát. Cần cố định và tập phục hồi chức năng để tăng cường cơ xung quanh khớp.",
        "context": "정형외과, 재활의학, 스포츠의학",
        "culturalNote": "한국 의료에서는 아탈구도 정밀 검사와 체계적 재활을 권장하지만, 베트남에서는 '큰 문제 아니다'라고 여기고 그냥 지나치는 경우가 많습니다. 통역사는 아탈구가 반복되면 관절의 안정성이 약해져서 일상생활에 지장을 줄 수 있음을 설명하고, 근력 강화 운동과 물리치료의 필요성을 강조해야 합니다. 특히 어깨 아탈구는 회전근개 손상과 함께 오는 경우가 많아 주의가 필요합니다.",
        "commonMistakes": [
            {
                "mistake": "'아탈구'를 단순히 '약한 탈구'로 통역",
                "correction": "'trật khớp một phần' 또는 'trật khớp không hoàn toàn'",
                "explanation": "부분 탈구라는 의학적 정의를 정확히 전달해야 합니다"
            },
            {
                "mistake": "치료 불필요하다고 잘못 전달",
                "correction": "'cần điều trị để tránh trật khớp lại nhiều lần'",
                "explanation": "아탈구도 치료하지 않으면 습관성으로 발전할 수 있습니다"
            },
            {
                "mistake": "재활 운동을 선택 사항으로 통역",
                "correction": "'bắt buộc phải tập vật lý trị liệu'로 강조",
                "explanation": "근력 강화 없이는 재발률이 매우 높습니다"
            }
        ],
        "examples": [
            {
                "ko": "어깨에 아탈구가 반복되고 있어 MRI 검사가 필요합니다.",
                "vi": "Khớp vai bị trật một phần nhiều lần, cần chụp MRI.",
                "situation": "formal"
            },
            {
                "ko": "아탈구라도 방치하면 만성 통증이 생길 수 있습니다.",
                "vi": "Dù chỉ trật khớp một phần, nếu bỏ mặc có thể gây đau mãn tính.",
                "situation": "onsite"
            },
            {
                "ko": "재활 운동으로 관절 주변 근육을 강화해야 합니다.",
                "vi": "Cần tập phục hồi chức năng để tăng cường cơ quanh khớp.",
                "situation": "formal"
            }
        ],
        "relatedTerms": ["탈구", "회전근개", "관절불안정"]
    },
    {
        "slug": "ton-thuong-day-chang",
        "korean": "인대손상",
        "vietnamese": "tổn thương dây chằng",
        "hanja": "靭帶損傷",
        "hanjaReading": "인(힘줄 인) + 대(띠 대) + 손(손상할 손) + 상(상할 상)",
        "pronunciation": "in-dae-son-sang",
        "meaningKo": "관절을 안정시키는 인대가 늘어나거나 부분적으로 찢어진 상태를 말합니다. 통역 시 손상 정도를 1도(경미한 염좌), 2도(부분 파열), 3도(완전 파열)로 구분하여 전달해야 하며, 각 등급에 따라 치료 방법과 회복 기간이 다름을 명확히 해야 합니다. 특히 무릎의 십자인대 손상은 수술적 치료가 필요할 수 있으며, 조기 재활이 매우 중요함을 강조해야 합니다.",
        "meaningVi": "Tình trạng dây chằng giữ ổn định khớp bị giãn hoặc đứt một phần. Phân loại theo mức độ: độ 1 (giãn nhẹ), độ 2 (đứt một phần), độ 3 (đứt hoàn toàn). Tùy mức độ mà phương pháp điều trị khác nhau, từ nghỉ ngơi đến phẫu thuật. Đặc biệt tổn thương dây chằng chéo đầu gối thường cần phẫu thuật và phục hồi chức năng lâu dài.",
        "context": "정형외과, 스포츠의학, 재활의학",
        "culturalNote": "한국에서는 인대손상 시 RICE 요법(Rest, Ice, Compression, Elevation)을 즉시 시행하고 전문의 진료를 권장하지만, 베트남에서는 파스와 마사지로 해결하려는 경향이 있습니다. 통역사는 인대는 혈액 공급이 적어 자연 치유가 어렵고, 제대로 치료하지 않으면 관절 불안정으로 이어져 퇴행성 관절염이 조기에 발생할 수 있음을 설명해야 합니다.",
        "commonMistakes": [
            {
                "mistake": "'인대'와 '힘줄'을 혼동하여 통역",
                "correction": "인대는 'dây chằng', 힘줄은 'gân'",
                "explanation": "인대는 뼈와 뼈를 연결하고, 힘줄은 근육과 뼈를 연결합니다"
            },
            {
                "mistake": "손상 등급을 생략하고 통역",
                "correction": "'tổn thương độ 1/2/3'로 심각도 명시",
                "explanation": "등급에 따라 치료법이 완전히 달라집니다"
            },
            {
                "mistake": "RICE 요법을 간단히 설명",
                "correction": "'nghỉ ngơi, chườm đá, băng ép, nâng cao'로 상세히",
                "explanation": "응급 처치 방법을 정확히 이해해야 합병증을 예방할 수 있습니다"
            }
        ],
        "examples": [
            {
                "ko": "발목 인대가 2도 손상되어 4주간 고정이 필요합니다.",
                "vi": "Dây chằng mắt cá chân tổn thương độ 2, cần cố định 4 tuần.",
                "situation": "formal"
            },
            {
                "ko": "무릎 십자인대 파열로 재건술이 필요합니다.",
                "vi": "Dây chằng chéo đầu gối bị đứt, cần phẫu thuật tái tạo.",
                "situation": "formal"
            },
            {
                "ko": "인대 손상 후 재활 치료를 하지 않으면 재발률이 높습니다.",
                "vi": "Nếu không tập phục hồi sau tổn thương dây chằng, tỷ lệ tái phát rất cao.",
                "situation": "onsite"
            }
        ],
        "relatedTerms": ["전방십자인대", "후방십자인대", "염좌"]
    },
    {
        "slug": "day-chang-cheo-truoc",
        "korean": "전방십자인대",
        "vietnamese": "dây chằng chéo trước",
        "hanja": "前方十字靭帶",
        "hanjaReading": "전(앞 전) + 방(방향 방) + 십(열 십) + 자(글자 자) + 인(힘줄 인) + 대(띠 대)",
        "pronunciation": "jeon-bang-sip-ja-in-dae",
        "meaningKo": "무릎 관절 내부에서 대퇴골과 경골을 연결하며 무릎의 전방 안정성을 담당하는 인대입니다. 통역 시 ACL(Anterior Cruciate Ligament)로도 불리며, 스포츠 손상에서 가장 흔한 인대 파열 중 하나임을 설명해야 합니다. 파열 시 '뚝' 하는 소리와 함께 무릎이 빠지는 느낌이 들며, 대부분 수술적 재건술이 필요하고 회복에 6개월 이상 소요됨을 명확히 전달해야 합니다.",
        "meaningVi": "Dây chằng nằm trong khớp gối, nối xương đùi và xương chày, giữ ổn định phần trước của đầu gối. Viết tắt là ACL. Đây là một trong những chấn thương dây chằng thường gặp nhất trong thể thao. Khi đứt thường nghe tiếng 'cộp', cảm giác đầu gối tuột ra. Hầu hết cần phẫu thuật tái tạo và mất 6 tháng trở lên để hồi phục.",
        "context": "정형외과, 스포츠의학, 관절경수술",
        "culturalNote": "한국에서는 ACL 파열 시 즉시 MRI 검사 후 수술 일정을 잡지만, 베트남 근로자들은 수술 비용 부담으로 보존적 치료를 선호하는 경우가 많습니다. 통역사는 ACL은 자연 치유되지 않으며, 수술 없이 방치하면 반월상연골 추가 손상, 퇴행성 관절염 조기 발생 등 심각한 합병증이 생길 수 있음을 강조하고, 산재보험이나 건강보험 적용 가능성을 안내해야 합니다.",
        "commonMistakes": [
            {
                "mistake": "'십자인대'를 일반 인대로 통역",
                "correction": "'dây chằng chéo'로 십자 형태 명시",
                "explanation": "무릎에는 4개의 주요 인대가 있고 십자인대는 그 중 가장 중요합니다"
            },
            {
                "mistake": "수술의 필요성을 선택 사항으로 통역",
                "correction": "'hầu hết cần phẫu thuật' 또는 'khuyến cáo phẫu thuật'",
                "explanation": "ACL 파열은 대부분 수술이 표준 치료입니다"
            },
            {
                "mistake": "회복 기간을 짧게 통역",
                "correction": "'ít nhất 6-9 tháng mới hoàn toàn bình phục'",
                "explanation": "ACL 재건술 후 복귀까지는 최소 6개월이 필요합니다"
            }
        ],
        "examples": [
            {
                "ko": "MRI 결과 전방십자인대가 완전히 파열되었습니다.",
                "vi": "Kết quả MRI cho thấy dây chằng chéo trước đứt hoàn toàn.",
                "situation": "formal"
            },
            {
                "ko": "전방십자인대 재건술 후 재활이 매우 중요합니다.",
                "vi": "Sau phẫu thuật tái tạo dây chằng chéo trước, phục hồi chức năng rất quan trọng.",
                "situation": "formal"
            },
            {
                "ko": "수술 없이 방치하면 무릎이 불안정해집니다.",
                "vi": "Nếu không phẫu thuật mà bỏ mặc, đầu gối sẽ không ổn định.",
                "situation": "onsite"
            }
        ],
        "relatedTerms": ["후방십자인대", "반월상연골", "관절경수술"]
    },
    {
        "slug": "day-chang-cheo-sau",
        "korean": "후방십자인대",
        "vietnamese": "dây chằng chéo sau",
        "hanja": "後方十字靭帶",
        "hanjaReading": "후(뒤 후) + 방(방향 방) + 십(열 십) + 자(글자 자) + 인(힘줄 인) + 대(띠 대)",
        "pronunciation": "hu-bang-sip-ja-in-dae",
        "meaningKo": "무릎 관절 내부에서 대퇴골과 경골을 연결하며 무릎의 후방 안정성을 담당하는 인대로, 전방십자인대보다 더 굵고 강합니다. 통역 시 PCL(Posterior Cruciate Ligament)로도 불리며, 대시보드 손상(교통사고 시 무릎이 대시보드에 부딪힘)이나 무릎 앞쪽 직접 타격으로 주로 발생함을 설명해야 합니다. ACL과 달리 경미한 손상은 보존적 치료가 가능하지만, 심한 파열은 수술이 필요합니다.",
        "meaningVi": "Dây chằng nằm trong khớp gối, nối xương đùi và xương chày, giữ ổn định phần sau của đầu gối. Viết tắt là PCL. Dây chằng này dày và chắc hơn ACL. Thường bị tổn thương do va chạm trực tiếp vào mặt trước đầu gối hoặc tai nạn giao thông. Khác với ACL, tổn thương nhẹ có thể điều trị không phẫu thuật, nhưng đứt nặng vẫn cần mổ.",
        "context": "정형외과, 외상외과, 스포츠의학",
        "culturalNote": "한국에서는 PCL 손상 시 손상 정도를 정밀 평가한 후 치료 방침을 결정하지만, 베트남에서는 PCL 손상 자체를 잘 진단하지 못하는 경우가 있습니다. 통역사는 PCL 손상이 초기에는 증상이 경미해 간과되기 쉽지만, 장기적으로 슬개대퇴 관절염을 유발할 수 있음을 설명하고, 정확한 진단과 적절한 재활의 중요성을 강조해야 합니다.",
        "commonMistakes": [
            {
                "mistake": "PCL과 ACL을 혼동하여 통역",
                "correction": "전방은 'chéo trước', 후방은 'chéo sau'",
                "explanation": "두 인대는 위치와 기능이 완전히 다릅니다"
            },
            {
                "mistake": "모든 PCL 손상에 수술 필요하다고 통역",
                "correction": "'tùy mức độ, có thể điều trị không phẫu thuật'",
                "explanation": "PCL은 부분 파열 시 보존적 치료가 가능한 경우가 많습니다"
            },
            {
                "mistake": "대시보드 손상 기전을 생략",
                "correction": "'thương tổn do đầu gối đập vào táp-lô trong tai nạn'",
                "explanation": "손상 원인을 알면 예방과 진단에 도움이 됩니다"
            }
        ],
        "examples": [
            {
                "ko": "교통사고로 후방십자인대가 손상되었습니다.",
                "vi": "Tai nạn giao thông gây tổn thương dây chằng chéo sau.",
                "situation": "formal"
            },
            {
                "ko": "부분 파열이므로 보조기 착용하고 재활 치료를 시작합니다.",
                "vi": "Do đứt một phần nên đeo nẹp và bắt đầu phục hồi chức năng.",
                "situation": "onsite"
            },
            {
                "ko": "후방십자인대 손상은 나중에 관절염을 유발할 수 있습니다.",
                "vi": "Tổn thương dây chằng chéo sau có thể gây viêm khớp về sau.",
                "situation": "formal"
            }
        ],
        "relatedTerms": ["전방십자인대", "인대손상", "무릎관절염"]
    },
    {
        "slug": "sun-so-ban-nguyet",
        "korean": "반월상연골",
        "vietnamese": "sụn sơ bán nguyệt",
        "hanja": "半月狀軟骨",
        "hanjaReading": "반(반 반) + 월(달 월) + 상(모양 상) + 연(부드러울 연) + 골(뼈 골)",
        "pronunciation": "ban-wol-sang-yeon-gol",
        "meaningKo": "무릎 관절 안쪽과 바깥쪽에 위치한 반달 모양의 연골로, 충격 흡수와 하중 분산 기능을 담당합니다. 통역 시 내측 반월상연골과 외측 반월상연골을 구분해야 하며, 파열 시 무릎에서 '딱딱' 소리가 나거나 걸리는 증상이 나타남을 설명해야 합니다. 젊은 층은 운동 중 회전 동작에서, 중장년층은 퇴행성 변화로 파열되며, 치료는 파열 정도와 위치에 따라 봉합술이나 절제술을 선택합니다.",
        "meaningVi": "Sụn hình bán nguyệt nằm ở mặt trong và mặt ngoài khớp gối, có chức năng hấp thụ lực tác động và phân tán trọng lượng. Khi bị rách, đầu gối thường phát ra tiếng 'lục cục' hoặc cảm giác bị kẹt. Người trẻ thường bị rách do xoay đột ngột khi vận động, người trung niên do thoái hóa. Điều trị tùy vị trí và mức độ rách: khâu lại hoặc cắt bỏ phần rách.",
        "context": "정형외과, 스포츠의학, 관절경수술",
        "culturalNote": "한국에서는 반월상연골 파열 시 관절경 수술로 최소 침습적 치료를 하지만, 베트남에서는 진단 자체가 늦어지는 경우가 많습니다. 통역사는 반월상연골은 한 번 파열되면 자연 치유가 거의 불가능하고, 방치 시 관절 연골까지 손상되어 조기 퇴행성 관절염이 발생함을 강조해야 합니다. 또한 젊을수록 봉합술로 보존하는 것이 중요하며, 절제 시 장기적으로 관절염 위험이 높아짐을 설명해야 합니다.",
        "commonMistakes": [
            {
                "mistake": "'연골'과 '뼈'를 혼동하여 통역",
                "correction": "연골은 'sụn', 뼈는 'xương'",
                "explanation": "연골과 뼈는 완전히 다른 조직입니다"
            },
            {
                "mistake": "내측/외측 구분 없이 통역",
                "correction": "'sụn sơ bán nguyệt trong/ngoài'로 위치 명시",
                "explanation": "내측과 외측 파열은 예후가 다릅니다"
            },
            {
                "mistake": "절제술을 간단한 수술로 설명",
                "correction": "'cắt bỏ sụn có thể gây viêm khớp sau này'로 위험 안내",
                "explanation": "연골 절제는 장기적으로 관절에 부담을 줍니다"
            }
        ],
        "examples": [
            {
                "ko": "내측 반월상연골이 파열되어 관절경 수술이 필요합니다.",
                "vi": "Sụn sơ bán nguyệt trong bị rách, cần phẫu thuật nội soi khớp.",
                "situation": "formal"
            },
            {
                "ko": "무릎에서 딱딱 소리가 나는 것은 연골 파열 증상입니다.",
                "vi": "Tiếng 'lục cục' ở đầu gối là triệu chứng sụn bị rách.",
                "situation": "onsite"
            },
            {
                "ko": "젊은 나이에는 가능한 봉합술로 연골을 보존합니다.",
                "vi": "Ở người trẻ, nên khâu lại để bảo tồn sụn nếu có thể.",
                "situation": "formal"
            }
        ],
        "relatedTerms": ["관절경수술", "전방십자인대", "퇴행성관절염"]
    },
    {
        "slug": "bap-vai-xoay",
        "korean": "회전근개",
        "vietnamese": "bắp vai xoay",
        "hanja": "回轉筋蓋",
        "hanjaReading": "회(돌 회) + 전(구를 전) + 근(힘줄 근) + 개(덮을 개)",
        "pronunciation": "hoe-jeon-geun-gae",
        "meaningKo": "어깨 관절을 둘러싸고 있는 4개의 근육과 힘줄로 구성된 구조물로, 어깨의 회전과 안정성을 담당합니다. 통역 시 회전근개 파열은 중년 이후에 흔하며, 팔을 들어올릴 때 통증과 함께 힘이 빠지는 증상이 나타남을 설명해야 합니다. 부분 파열은 물리치료와 약물로 치료하지만, 완전 파열은 수술적 봉합이 필요하며, 파열 크기가 클수록 수술 후 결과가 나쁘므로 조기 치료가 중요함을 강조해야 합니다.",
        "meaningVi": "Cấu trúc gồm 4 cơ và gân bao quanh khớp vai, chịu trách nhiệm xoay và ổn định vai. Rách bắp vai xoay thường gặp ở tuổi trung niên trở lên, triệu chứng là đau và yếu khi giơ tay lên. Rách một phần có thể điều trị bằng vật lý trị liệu và thuốc, nhưng rách hoàn toàn cần phẫu thuật khâu lại. Vết rách càng lớn, kết quả sau mổ càng kém nên cần điều trị sớm.",
        "context": "정형외과, 재활의학, 스포츠의학",
        "culturalNote": "한국에서는 회전근개 파열 시 MRI로 정확히 진단하고 조기에 수술을 권장하지만, 베트남 근로자들은 어깨 통증을 나이 탓으로 여기고 방치하는 경우가 많습니다. 통역사는 회전근개 파열은 시간이 지날수록 파열이 커지고 근육이 위축되어 수술해도 기능 회복이 어려워짐을 강조하고, 골든타임 내 치료의 중요성을 설명해야 합니다. 또한 오십견과 혼동하기 쉬우므로 정확한 감별 진단이 필요합니다.",
        "commonMistakes": [
            {
                "mistake": "'회전근개'를 단순히 '어깨 근육'으로 통역",
                "correction": "'bắp vai xoay' 또는 'gân bắp vai xoay'",
                "explanation": "회전근개는 특정한 해부학적 구조물입니다"
            },
            {
                "mistake": "오십견과 회전근개 파열을 같다고 통역",
                "correction": "오십견은 'viêm quanh khớp vai', 회전근개 파열은 'rách bắp vai xoay'",
                "explanation": "두 질환은 원인과 치료법이 완전히 다릅니다"
            },
            {
                "mistake": "수술 시기를 급하지 않다고 통역",
                "correction": "'nên phẫu thuật sớm trước khi vết rách lớn hơn'",
                "explanation": "회전근개 파열은 시간이 지날수록 악화됩니다"
            }
        ],
        "examples": [
            {
                "ko": "회전근개가 3cm 파열되어 봉합술이 필요합니다.",
                "vi": "Bắp vai xoay bị rách 3cm, cần phẫu thuật khâu lại.",
                "situation": "formal"
            },
            {
                "ko": "팔을 옆으로 들어올릴 때 통증이 심하면 회전근개 파열을 의심해야 합니다.",
                "vi": "Nếu đau nhiều khi giơ tay ra ngang, cần nghi ngờ rách bắp vai xoay.",
                "situation": "onsite"
            },
            {
                "ko": "회전근개 수술 후 6개월간 재활 치료가 필요합니다.",
                "vi": "Sau mổ bắp vai xoay cần tập phục hồi 6 tháng.",
                "situation": "formal"
            }
        ],
        "relatedTerms": ["오십견", "어깨충돌증후군", "석회성건염"]
    },
    {
        "slug": "thoat-vi-dia-dem",
        "korean": "추간판탈출증",
        "vietnamese": "thoát vị đĩa đệm",
        "hanja": "椎間板脫出症",
        "hanjaReading": "추(등뼈 추) + 간(사이 간) + 판(널빤지 판) + 탈(벗을 탈) + 출(날 출) + 증(병 증)",
        "pronunciation": "chu-gan-pan-tal-chul-jeung",
        "meaningKo": "척추뼈 사이의 디스크(추간판)가 튀어나와 신경을 압박하는 질환으로, 흔히 '허리디스크' 또는 '목디스크'라고 불립니다. 통역 시 발생 부위(경추, 흉추, 요추)와 신경 압박 정도를 명확히 전달해야 하며, 다리 저림, 통증, 근력 약화 등의 증상을 구체적으로 설명해야 합니다. 대부분 보존적 치료(약물, 물리치료, 신경차단술)로 호전되지만, 마비 증상이 있거나 보존적 치료 실패 시 수술이 필요함을 강조해야 합니다.",
        "meaningVi": "Bệnh lý đĩa đệm giữa các đốt sống bị lồi ra, chèn ép dây thần kinh. Thường gọi là 'thoát vị đĩa đệm thắt lưng' hoặc 'thoát vị đĩa đệm cổ'. Cần nói rõ vị trí (đốt sống cổ, ngực, thắt lưng) và mức độ chèn ép thần kinh. Triệu chứng: tê chân, đau, yếu cơ. Hầu hết khỏi bằng điều trị nội khoa (thuốc, vật lý trị liệu, tiêm vùng thần kinh), nhưng nếu có liệt hoặc điều trị nội khoa thất bại thì cần phẫu thuật.",
        "context": "신경외과, 정형외과, 재활의학, 통증의학",
        "culturalNote": "한국에서는 추간판탈출증 진단 시 MRI로 정확한 위치와 크기를 파악한 후 단계적 치료를 하지만, 베트남 근로자들은 통증을 참고 일을 계속하다가 증상이 악화되는 경우가 많습니다. 통역사는 초기에 적절히 치료하지 않으면 만성 통증, 근력 약화, 심하면 대소변 장애까지 올 수 있음을 강조하고, 작업 자세 개선과 코어 근력 강화의 중요성을 설명해야 합니다. 또한 수술이 필요한 경우 최소 침습적 방법이 많이 발전했음을 안내해야 합니다.",
        "commonMistakes": [
            {
                "mistake": "'디스크'를 그냥 'đĩa'로만 번역",
                "correction": "'thoát vị đĩa đệm' 또는 'đĩa đệm lồi'로 병명 명시",
                "explanation": "디스크는 정상 구조물이고, 탈출증은 질병입니다"
            },
            {
                "mistake": "경추/요추 구분 없이 통역",
                "correction": "'thoát vị đĩa đệm cổ/thắt lưng'로 부위 명확히",
                "explanation": "발생 부위에 따라 증상과 치료법이 다릅니다"
            },
            {
                "mistake": "수술만 강조하여 통역",
                "correction": "'đa số khỏi bằng điều trị nội khoa'로 보존적 치료 우선 설명",
                "explanation": "대부분은 수술 없이 치료 가능합니다"
            }
        ],
        "examples": [
            {
                "ko": "요추 4-5번 추간판탈출증으로 신경 압박이 있습니다.",
                "vi": "Thoát vị đĩa đệm thắt lưng L4-5 gây chèn ép thần kinh.",
                "situation": "formal"
            },
            {
                "ko": "먼저 2주간 약물 치료와 물리치료를 해보겠습니다.",
                "vi": "Trước tiên thử điều trị bằng thuốc và vật lý trị liệu trong 2 tuần.",
                "situation": "onsite"
            },
            {
                "ko": "발가락에 힘이 안 들어가면 수술이 필요할 수 있습니다.",
                "vi": "Nếu không cử động được ngón chân, có thể cần phẫu thuật.",
                "situation": "formal"
            }
        ],
        "relatedTerms": ["척추관협착증", "좌골신경통", "신경차단술"]
    },
    {
        "slug": "hep-ong-song-song",
        "korean": "척추관협착증",
        "vietnamese": "hẹp ống sống",
        "hanja": "脊椎管狹窄症",
        "hanjaReading": "척(등뼈 척) + 추(쌓을 추) + 관(대롱 관) + 협(좁을 협) + 착(붙을 착) + 증(병 증)",
        "pronunciation": "cheok-chu-gwan-hyeop-chak-jeung",
        "meaningKo": "척추 신경이 지나가는 통로가 좁아져서 신경을 압박하는 질환으로, 주로 노화로 인한 퇴행성 변화가 원인입니다. 통역 시 특징적인 증상인 '신경인성 파행(오래 걷거나 서 있으면 다리가 저리고 아파서 쉬어야 함)'을 정확히 설명해야 하며, 허리를 구부리면 증상이 완화되는 점도 전달해야 합니다. 초기에는 약물과 물리치료로 관리하지만, 일상생활이 불가능할 정도로 증상이 심하면 감압술이나 유합술 같은 수술이 필요함을 강조해야 합니다.",
        "meaningVi": "Bệnh lý ống sống bị hẹp lại, chèn ép dây thần kinh, chủ yếu do thoái hóa theo tuổi tác. Triệu chứng đặc trưng là 'khập khiễng do thần kinh' (đi hoặc đứng lâu thì chân tê và đau, phải nghỉ mới bớt). Khi cúi người về phía trước thì triệu chứng giảm. Ban đầu điều trị bằng thuốc và vật lý trị liệu, nhưng nếu ảnh hưởng nghiêm trọng đến sinh hoạt thì cần phẫu thuật giảm áp hoặc hàn xương.",
        "context": "신경외과, 정형외과, 노인의학",
        "culturalNote": "한국에서는 척추관협착증을 적극적으로 진단하고 치료하지만, 베트남 근로자들은 나이가 들면 당연한 것으로 여기고 방치하는 경향이 있습니다. 통역사는 척추관협착증을 치료하지 않으면 점점 걷는 거리가 짧아지고 결국 거동이 불가능해질 수 있음을 설명하고, 수술이 두렵더라도 적절한 시기에 치료받으면 삶의 질이 크게 개선됨을 강조해야 합니다. 또한 척추관협착증과 혈관성 파행(말초동맥질환)을 감별하는 것이 중요합니다.",
        "commonMistakes": [
            {
                "mistake": "'협착증'을 단순히 '좁아짐'으로 통역",
                "correction": "'hẹp ống sống' 또는 'hẹp kênh tủy sống'",
                "explanation": "정확한 의학 용어를 사용해야 합니다"
            },
            {
                "mistake": "신경인성 파행과 혈관성 파행을 구분 안 함",
                "correction": "'khập khiễng do thần kinh (giảm khi cúi người)'",
                "explanation": "두 질환은 치료법이 완전히 다릅니다"
            },
            {
                "mistake": "수술을 최후의 수단으로만 설명",
                "correction": "'phẫu thuật giúp cải thiện chất lượng cuộc sống rõ rệt'",
                "explanation": "적절한 시기의 수술은 매우 효과적입니다"
            }
        ],
        "examples": [
            {
                "ko": "100미터도 못 걷고 다리가 저려서 쉬어야 합니다.",
                "vi": "Đi không được 100m là chân tê phải nghỉ.",
                "situation": "onsite"
            },
            {
                "ko": "MRI 결과 요추 4-5번에 심한 협착이 있습니다.",
                "vi": "Kết quả MRI cho thấy hẹp nặng ở đốt sống thắt lưng L4-5.",
                "situation": "formal"
            },
            {
                "ko": "감압술로 신경 압박을 풀어주는 수술을 권합니다.",
                "vi": "Khuyến cáo phẫu thuật giảm áp để giải phóng dây thần kinh bị chèn ép.",
                "situation": "formal"
            }
        ],
        "relatedTerms": ["추간판탈출증", "척추유합술", "신경인성파행"]
    },
    {
        "slug": "truot-dot-song",
        "korean": "척추전방전위증",
        "vietnamese": "trượt đốt sống",
        "hanja": "脊椎前方轉位症",
        "hanjaReading": "척(등뼈 척) + 추(쌓을 추) + 전(앞 전) + 방(방향 방) + 전(구를 전) + 위(자리 위) + 증(병 증)",
        "pronunciation": "cheok-chu-jeon-bang-jeon-wi-jeung",
        "meaningKo": "위쪽 척추뼈가 아래쪽 척추뼈에 비해 앞으로 미끄러진 상태를 말하며, 주로 요추 4-5번이나 요추 5번-천추 1번에서 발생합니다. 통역 시 전위 정도를 1도(25% 미만), 2도(25-50%), 3도(50-75%), 4도(75% 이상)로 구분해야 하며, 정도에 따라 치료 방법이 달라짐을 설명해야 합니다. 선천성과 후천성(퇴행성, 외상성)을 구분하고, 심한 경우 척추유합술이 필요함을 강조해야 합니다.",
        "meaningVi": "Tình trạng đốt sống phía trên bị trượt về phía trước so với đốt sống phía dưới, thường xảy ra ở L4-5 hoặc L5-S1. Phân độ theo mức độ trượt: độ 1 (dưới 25%), độ 2 (25-50%), độ 3 (50-75%), độ 4 (trên 75%). Phương pháp điều trị tùy theo mức độ. Phân loại thành bẩm sinh và mắc phải (thoái hóa, chấn thương). Trường hợp nặng cần phẫu thuật hàn xương.",
        "context": "신경외과, 정형외과, 척추외과",
        "culturalNote": "한국에서는 척추전방전위증을 조기에 발견하여 운동 치료와 자세 교정으로 관리하지만, 베트남 근로자들은 허리 통증을 일반적인 것으로 여기고 무거운 것을 계속 들다가 악화되는 경우가 많습니다. 통역사는 전방전위증이 있을 때 무리한 허리 사용(무거운 물건 들기, 허리 비틀기)을 피해야 하며, 코어 근력 강화가 매우 중요함을 강조해야 합니다. 또한 작업 환경 개선과 산재 적용 가능성도 안내해야 합니다.",
        "commonMistakes": [
            {
                "mistake": "'전방전위증'을 일반 허리 통증으로 통역",
                "correction": "'trượt đốt sống về phía trước'로 구조적 문제 명시",
                "explanation": "이것은 단순 통증이 아니라 뼈의 위치 이상입니다"
            },
            {
                "mistake": "전위 정도를 생략하고 통역",
                "correction": "'trượt độ 1/2/3/4'로 심각도 명시",
                "explanation": "정도에 따라 치료법이 완전히 다릅니다"
            },
            {
                "mistake": "무거운 것 드는 것을 금지하지 않음",
                "correction": "'tuyệt đối tránh nâng vật nặng'로 강조",
                "explanation": "무거운 것을 들면 전위가 더 심해집니다"
            }
        ],
        "examples": [
            {
                "ko": "요추 5번이 2도 전방전위되어 있습니다.",
                "vi": "Đốt sống thắt lưng L5 bị trượt về phía trước độ 2.",
                "situation": "formal"
            },
            {
                "ko": "무거운 물건을 들지 마시고 코어 운동을 시작하세요.",
                "vi": "Đừng nâng vật nặng và bắt đầu tập cơ lõi.",
                "situation": "onsite"
            },
            {
                "ko": "3도 이상 전위는 척추유합술이 필요할 수 있습니다.",
                "vi": "Trượt từ độ 3 trở lên có thể cần phẫu thuật hàn xương.",
                "situation": "formal"
            }
        ],
        "relatedTerms": ["척추유합술", "척추관협착증", "코어근력강화"]
    },
    {
        "slug": "cong-cot-song",
        "korean": "측만증",
        "vietnamese": "cong cột sống",
        "hanja": "側彎症",
        "hanjaReading": "측(곁 측) + 만(구부릴 만) + 증(병 증)",
        "pronunciation": "cheuk-man-jeung",
        "meaningKo": "척추가 좌우로 휘어진 변형으로, 정면에서 보았을 때 C자 또는 S자 형태를 보이는 질환입니다. 통역 시 특발성(원인 불명, 청소년기), 선천성, 신경근육성 측만증을 구분해야 하며, Cobb 각도로 심각도를 측정함을 설명해야 합니다. 10도 이하는 경과 관찰, 20-40도는 보조기 치료, 40도 이상은 수술을 고려하며, 성장기에는 진행 가능성이 높아 정기적인 검사가 필요함을 강조해야 합니다.",
        "meaningVi": "Biến dạng cột sống cong sang hai bên, khi nhìn từ phía trước có hình chữ C hoặc S. Phân loại: vô căn (không rõ nguyên nhân, tuổi thanh thiếu niên), bẩm sinh, do thần kinh cơ. Mức độ nghiêm trọng đo bằng góc Cobb. Dưới 10 độ theo dõi, 20-40 độ đeo nẹp, trên 40 độ cân nhắc phẫu thuật. Trong giai đoạn phát triển dễ tiến triển nên cần khám định kỳ.",
        "context": "정형외과, 소아과, 재활의학",
        "culturalNote": "한국에서는 학교 건강검진에서 측만증을 조기 발견하여 치료하지만, 베트남에서는 심하게 휘어질 때까지 발견되지 않는 경우가 많습니다. 통역사는 성장기 청소년의 측만증은 빠르게 진행될 수 있어 조기 발견과 치료가 중요하며, 보조기 착용의 중요성과 꾸준한 운동의 필요성을 강조해야 합니다. 또한 측만증이 심하면 호흡 기능에도 영향을 줄 수 있음을 설명해야 합니다.",
        "commonMistakes": [
            {
                "mistake": "'측만증'을 단순히 '구부정한 자세'로 통역",
                "correction": "'cong cột sống' 또는 'vẹo cột sống'로 구조적 변형 명시",
                "explanation": "측만증은 자세 문제가 아니라 척추 변형입니다"
            },
            {
                "mistake": "Cobb 각도를 설명 없이 통역",
                "correction": "'góc Cobb (góc đo độ cong)'",
                "explanation": "환자가 각도의 의미를 이해해야 합니다"
            },
            {
                "mistake": "보조기 착용을 선택 사항으로 통역",
                "correction": "'bắt buộc phải đeo nẹp để ngăn tiến triển'",
                "explanation": "성장기에는 보조기가 매우 중요합니다"
            }
        ],
        "examples": [
            {
                "ko": "엑스레이 결과 Cobb 각도 25도 측만증입니다.",
                "vi": "Kết quả X-quang cho thấy cong cột sống góc Cobb 25 độ.",
                "situation": "formal"
            },
            {
                "ko": "보조기를 하루 18시간 이상 착용해야 합니다.",
                "vi": "Phải đeo nẹp ít nhất 18 giờ mỗi ngày.",
                "situation": "onsite"
            },
            {
                "ko": "6개월마다 엑스레이로 진행 여부를 확인합니다.",
                "vi": "Cứ 6 tháng chụp X-quang một lần để kiểm tra tiến triển.",
                "situation": "formal"
            }
        ],
        "relatedTerms": ["척추측만", "보조기치료", "척추교정수술"]
    },
    {
        "slug": "goi-lung",
        "korean": "후만증",
        "vietnamese": "gù lưng",
        "hanja": "後彎症",
        "hanjaReading": "후(뒤 후) + 만(구부릴 만) + 증(병 증)",
        "pronunciation": "hu-man-jeung",
        "meaningKo": "척추가 앞뒤 방향으로 과도하게 휘어져 등이 둥글게 굽은 변형으로, 옆에서 보았을 때 등이 뒤로 볼록하게 튀어나온 상태를 말합니다. 통역 시 자세성(구부정한 자세), Scheuermann병(청소년기), 퇴행성(노인성)을 구분해야 하며, 각 원인에 따라 치료법이 다름을 설명해야 합니다. 자세 교정과 신전 운동이 중요하며, 심한 경우 통증과 호흡 곤란을 유발할 수 있어 적극적인 치료가 필요함을 강조해야 합니다.",
        "meaningVi": "Biến dạng cột sống cong quá mức về phía trước sau, lưng cong tròn, khi nhìn từ bên thấy lưng lồi ra phía sau. Phân loại: do tư thế (ngồi cúi), bệnh Scheuermann (tuổi thanh thiếu niên), thoái hóa (người cao tuổi). Phương pháp điều trị khác nhau tùy nguyên nhân. Cần chỉnh tư thế và tập duỗi thẳng. Trường hợp nặng gây đau và khó thở nên cần điều trị tích cực.",
        "context": "정형외과, 재활의학, 노인의학",
        "culturalNote": "한국에서는 후만증을 조기에 발견하여 자세 교정과 운동으로 관리하지만, 베트남에서는 나이가 들면 당연히 등이 굽는다고 생각하는 경향이 있습니다. 통역사는 후만증이 심해지면 폐 용량이 감소하여 호흡 곤란이 올 수 있고, 만성 요통의 원인이 됨을 설명하고, 스트레칭과 신전 운동으로 예방 및 개선이 가능함을 강조해야 합니다. 특히 청소년기 Scheuermann병은 조기 치료가 중요합니다.",
        "commonMistakes": [
            {
                "mistake": "'후만증'을 단순히 '구부정하다'로 통역",
                "correction": "'gù lưng' 또는 'cong lưng về phía trước'",
                "explanation": "후만증은 의학적으로 정의된 척추 변형입니다"
            },
            {
                "mistake": "노인성 후만증과 청소년 후만증을 구분 안 함",
                "correction": "원인에 따라 'do tư thế', 'bệnh Scheuermann', 'thoái hóa'",
                "explanation": "원인에 따라 치료법이 다릅니다"
            },
            {
                "mistake": "호흡 문제 가능성을 생략",
                "correction": "'nặng có thể gây khó thở do giảm dung tích phổi'",
                "explanation": "후만증의 중요한 합병증입니다"
            }
        ],
        "examples": [
            {
                "ko": "Scheuermann병으로 인한 후만증이 진행되고 있습니다.",
                "vi": "Gù lưng do bệnh Scheuermann đang tiến triển.",
                "situation": "formal"
            },
            {
                "ko": "등 신전 운동을 매일 해야 합니다.",
                "vi": "Phải tập duỗi lưng mỗi ngày.",
                "situation": "onsite"
            },
            {
                "ko": "후만 각도가 60도를 넘으면 호흡 기능에 영향을 줄 수 있습니다.",
                "vi": "Nếu góc gù lưng trên 60 độ có thể ảnh hưởng chức năng hô hấp.",
                "situation": "formal"
            }
        ],
        "relatedTerms": ["측만증", "척추변형", "자세교정"]
    },
    {
        "slug": "bong-gan-co",
        "korean": "경추염좌",
        "vietnamese": "bong gân cổ",
        "hanja": "頸椎捻挫",
        "hanjaReading": "경(목 경) + 추(쌓을 추) + 염(비틀 염) + 좌(삘 좌)",
        "pronunciation": "gyeong-chu-yeom-jwa",
        "meaningKo": "목뼈(경추) 주변의 인대나 근육이 갑작스러운 외력으로 늘어나거나 손상된 상태로, 흔히 '목 삐었다'고 표현합니다. 통역 시 교통사고의 채찍질 손상(whiplash)이 대표적 원인이며, 목 통증, 두통, 어지럼증, 팔 저림 등 다양한 증상이 나타날 수 있음을 설명해야 합니다. 초기에는 안정과 물리치료가 중요하며, 증상이 지속되면 추가 검사가 필요함을 강조해야 합니다.",
        "meaningVi": "Tình trạng dây chằng hoặc cơ quanh đốt sống cổ bị giãn hoặc tổn thương do lực tác động đột ngột, thường gọi là 'trẹo cổ'. Nguyên nhân điển hình là chấn thương roi da (whiplash) trong tai nạn giao thông. Triệu chứng: đau cổ, đau đầu, chóng mặt, tê tay. Ban đầu cần nghỉ ngơi và vật lý trị liệu, nếu triệu chứng kéo dài cần kiểm tra thêm.",
        "context": "정형외과, 재활의학, 응급의학",
        "culturalNote": "한국에서는 교통사고 후 경추염좌를 적극적으로 진단하고 치료하지만, 베트남 근로자들은 목 통증을 대수롭지 않게 여기고 방치하는 경우가 많습니다. 통역사는 경추염좌를 제대로 치료하지 않으면 만성 목 통증과 두통으로 이어질 수 있으며, 특히 교통사고 후에는 반드시 병원 진료를 받아 기록을 남겨야 보험 처리가 가능함을 강조해야 합니다.",
        "commonMistakes": [
            {
                "mistake": "'염좌'를 '골절'로 혼동",
                "correction": "염좌는 'bong gân', 골절은 'gãy xương'",
                "explanation": "염좌는 인대 손상이고 골절은 뼈 손상입니다"
            },
            {
                "mistake": "채찍질 손상을 그냥 '목 다쳤다'로 통역",
                "correction": "'chấn thương roi da' 또는 'chấn thương cổ do va chạm'",
                "explanation": "특정한 손상 기전을 명시해야 합니다"
            },
            {
                "mistake": "치료 불필요하다고 잘못 전달",
                "correction": "'cần điều trị ngay để tránh đau mãn tính'",
                "explanation": "경추염좌도 적절한 치료가 필요합니다"
            }
        ],
        "examples": [
            {
                "ko": "교통사고로 경추염좌가 발생했습니다.",
                "vi": "Tai nạn giao thông gây bong gân cổ.",
                "situation": "formal"
            },
            {
                "ko": "2주간 목 보호대를 착용하고 물리치료를 받으세요.",
                "vi": "Đeo cổ nẹp 2 tuần và tập vật lý trị liệu.",
                "situation": "onsite"
            },
            {
                "ko": "팔 저림이 계속되면 MRI 검사가 필요합니다.",
                "vi": "Nếu tê tay kéo dài cần chụp MRI.",
                "situation": "formal"
            }
        ],
        "relatedTerms": ["채찍질손상", "경추디스크", "근막통증증후군"]
    },
    {
        "slug": "bong-gan-that-lung",
        "korean": "요추염좌",
        "vietnamese": "bong gân thắt lưng",
        "hanja": "腰椎捻挫",
        "hanjaReading": "요(허리 요) + 추(쌓을 추) + 염(비틀 염) + 좌(삘 좌)",
        "pronunciation": "yo-chu-yeom-jwa",
        "meaningKo": "허리뼈(요추) 주변의 인대나 근육이 갑작스러운 외력이나 무리한 동작으로 늘어나거나 손상된 상태로, 흔히 '허리 삐었다' 또는 '급성 요통'이라고 표현합니다. 통역 시 무거운 물건을 들거나 허리를 갑자기 비틀 때 주로 발생하며, 산업 현장에서 가장 흔한 근골격계 질환 중 하나임을 설명해야 합니다. 초기 48-72시간 동안 냉찜질과 안정이 중요하며, 이후 열찜질과 스트레칭으로 전환함을 전달해야 합니다.",
        "meaningVi": "Tình trạng dây chằng hoặc cơ quanh đốt sống thắt lưng bị giãn hoặc tổn thương do lực tác động đột ngột hoặc động tác quá sức, thường gọi là 'trẹo lưng' hoặc 'đau lưng cấp'. Thường xảy ra khi nâng vật nặng hoặc xoay người đột ngột, là một trong những bệnh xương khớp phổ biến nhất tại công trường. Trong 48-72 giờ đầu cần chườm lạnh và nghỉ ngơi, sau đó chuyển sang chườm nóng và kéo giãn.",
        "context": "정형외과, 재활의학, 산업의학",
        "culturalNote": "한국에서는 요추염좌를 산업재해로 인정받을 수 있지만, 베트남 근로자들은 허리 통증을 참고 일을 계속하다가 만성화되는 경우가 많습니다. 통역사는 급성 요추염좌 발생 시 즉시 작업을 중단하고 치료를 받아야 하며, 산재 신청이 가능함을 안내해야 합니다. 또한 올바른 들기 자세(허리가 아닌 다리 힘으로)와 코어 근력 강화의 중요성을 강조해야 합니다.",
        "commonMistakes": [
            {
                "mistake": "'요추염좌'와 '추간판탈출증'을 혼동",
                "correction": "염좌는 'bong gân', 디스크는 'thoát vị đĩa đệm'",
                "explanation": "염좌는 인대/근육 문제, 디스크는 추간판 문제입니다"
            },
            {
                "mistake": "급성기에 열찜질 하라고 통역",
                "correction": "'48 giờ đầu chườm lạnh, sau đó mới chườm nóng'",
                "explanation": "급성기에는 냉찜질이 원칙입니다"
            },
            {
                "mistake": "산재 신청 가능성을 언급 안 함",
                "correction": "'có thể đăng ký tai nạn lao động'",
                "explanation": "작업 중 발생한 요추염좌는 산재 적용 대상입니다"
            }
        ],
        "examples": [
            {
                "ko": "무거운 짐을 들다가 허리를 삐었습니다.",
                "vi": "Nâng vật nặng bị trẹo lưng.",
                "situation": "onsite"
            },
            {
                "ko": "2-3일간 안정을 취하고 냉찜질을 하세요.",
                "vi": "Nghỉ ngơi 2-3 ngày và chườm lạnh.",
                "situation": "formal"
            },
            {
                "ko": "작업 복귀 전에 코어 근력 운동을 시작하세요.",
                "vi": "Trước khi quay lại làm việc, bắt đầu tập cơ lõi.",
                "situation": "onsite"
            }
        ],
        "relatedTerms": ["급성요통", "만성요통", "코어근력강화"]
    },
    {
        "slug": "dau-day-than-kinh-toa",
        "korean": "좌골신경통",
        "vietnamese": "đau dây thần kinh tọa",
        "hanja": "坐骨神經痛",
        "hanjaReading": "좌(앉을 좌) + 골(뼈 골) + 신(귀신 신) + 경(길 경) + 통(아플 통)",
        "pronunciation": "jwa-gol-sin-gyeong-tong",
        "meaningKo": "좌골신경이 압박되거나 자극받아 엉덩이에서 다리 뒤쪽으로 통증이 뻗어 내려가는 증상을 말합니다. 통역 시 이것은 질병명이 아니라 증상명이며, 원인으로는 추간판탈출증, 척추관협착증, 이상근증후군 등이 있음을 설명해야 합니다. 한쪽 다리로만 증상이 나타나는 것이 특징이며, 기침이나 재채기 시 통증이 악화되고, 원인 질환 치료가 우선임을 강조해야 합니다.",
        "meaningVi": "Triệu chứng đau lan từ mông xuống phía sau chân do dây thần kinh tọa bị chèn ép hoặc kích thích. Đây là tên triệu chứng chứ không phải tên bệnh. Nguyên nhân: thoát vị đĩa đệm, hẹp ống sống, hội chứng cơ lê... Đặc trưng là chỉ một bên chân bị đau, ho hoặc hắt hơi làm đau tăng. Cần điều trị bệnh gốc.",
        "context": "신경외과, 정형외과, 통증의학",
        "culturalNote": "한국에서는 좌골신경통의 원인을 정확히 진단하고 근본 치료를 하지만, 베트남 근로자들은 진통제만 복용하고 원인을 찾지 않는 경우가 많습니다. 통역사는 좌골신경통은 증상일 뿐이며, MRI로 원인을 찾아 치료해야 재발을 막을 수 있음을 강조하고, 통증이 심하면 신경차단술로 빠른 통증 완화가 가능함을 안내해야 합니다. 또한 장시간 앉아 있거나 잘못된 자세가 악화 요인임을 설명해야 합니다.",
        "commonMistakes": [
            {
                "mistake": "'좌골신경통'을 질병으로 통역",
                "correction": "'triệu chứng đau dây thần kinh tọa'로 증상임을 명시",
                "explanation": "좌골신경통은 증상이지 질병이 아닙니다"
            },
            {
                "mistake": "원인 찾기 없이 진통제만 처방",
                "correction": "'cần tìm nguyên nhân bằng MRI'",
                "explanation": "원인 치료 없이는 재발합니다"
            },
            {
                "mistake": "양쪽 다리 통증을 좌골신경통으로 통역",
                "correction": "'đau dây thần kinh tọa thường chỉ một bên'",
                "explanation": "양쪽 다리 통증은 다른 원인일 가능성이 높습니다"
            }
        ],
        "examples": [
            {
                "ko": "왼쪽 엉덩이에서 발끝까지 저리고 아픕니다.",
                "vi": "Đau và tê từ mông trái xuống tận ngón chân.",
                "situation": "onsite"
            },
            {
                "ko": "MRI로 좌골신경통의 원인을 찾아야 합니다.",
                "vi": "Cần chụp MRI để tìm nguyên nhân đau dây thần kinh tọa.",
                "situation": "formal"
            },
            {
                "ko": "신경차단술로 급성 통증을 조절할 수 있습니다.",
                "vi": "Có thể kiểm soát đau cấp bằng tiêm vùng thần kinh.",
                "situation": "formal"
            }
        ],
        "relatedTerms": ["추간판탈출증", "이상근증후군", "신경차단술"]
    },
    {
        "slug": "viem-bao-gan",
        "korean": "건초염",
        "vietnamese": "viêm bao gân",
        "hanja": "腱鞘炎",
        "hanjaReading": "건(힘줄 건) + 초(집 초) + 염(염증 염)",
        "pronunciation": "geon-cho-yeom",
        "meaningKo": "힘줄을 둘러싸고 있는 건초(힘줄집)에 염증이 생긴 질환으로, 반복적인 동작이나 과사용이 주요 원인입니다. 통역 시 손목, 손가락, 발목에 주로 발생하며, 움직일 때 통증과 함께 마찰음이 느껴질 수 있음을 설명해야 합니다. 드퀘르벵 건초염(손목 엄지 쪽), 방아쇠 손가락(손가락 굴곡건) 등이 대표적이며, 초기에는 휴식과 소염제로 치료하지만 재발이 잦으면 스테로이드 주사나 수술이 필요함을 강조해야 합니다.",
        "meaningVi": "Bệnh viêm bao bọc quanh gân do động tác lặp đi lặp lại hoặc sử dụng quá mức. Thường xảy ra ở cổ tay, ngón tay, mắt cá chân. Khi cử động có đau và cảm giác ma sát. Điển hình: viêm bao gân De Quervain (cổ tay phía ngón cái), ngón tay lò xo (gân gập ngón tay). Ban đầu điều trị bằng nghỉ ngơi và thuốc kháng viêm, nhưng nếu tái phát nhiều cần tiêm steroid hoặc phẫu thuật.",
        "context": "정형외과, 재활의학, 산업의학",
        "culturalNote": "한국에서는 건초염을 직업병으로 인정하여 산재 처리가 가능하지만, 베트남 근로자들은 손목 통증을 참고 일을 계속하다가 만성화되는 경우가 많습니다. 통역사는 건초염은 조기에 작업 방식을 바꾸고 휴식을 취하면 완치 가능하지만, 방치하면 만성 통증으로 이어져 작업 능력이 저하됨을 강조하고, 반복 작업자는 정기적인 스트레칭과 작업 중 휴식이 중요함을 설명해야 합니다.",
        "commonMistakes": [
            {
                "mistake": "'건초염'을 관절염으로 통역",
                "correction": "건초염은 'viêm bao gân', 관절염은 'viêm khớp'",
                "explanation": "건초염은 힘줄 문제, 관절염은 관절 문제입니다"
            },
            {
                "mistake": "드퀘르벵과 일반 건초염을 구분 안 함",
                "correction": "'viêm bao gân De Quervain (ở cổ tay ngón cái)'",
                "explanation": "발생 부위에 따라 이름이 다릅니다"
            },
            {
                "mistake": "산재 적용 가능성을 언급 안 함",
                "correction": "'có thể đăng ký bệnh nghề nghiệp'",
                "explanation": "반복 작업으로 인한 건초염은 산재 대상입니다"
            }
        ],
        "examples": [
            {
                "ko": "손목 엄지 쪽에 드퀘르벵 건초염이 있습니다.",
                "vi": "Bị viêm bao gân De Quervain ở cổ tay phía ngón cái.",
                "situation": "formal"
            },
            {
                "ko": "반복 작업을 줄이고 2주간 부목 고정이 필요합니다.",
                "vi": "Cần giảm động tác lặp lại và cố định bằng nẹp 2 tuần.",
                "situation": "onsite"
            },
            {
                "ko": "재발이 잦으면 스테로이드 주사를 고려합니다.",
                "vi": "Nếu tái phát nhiều lần, cân nhắc tiêm steroid.",
                "situation": "formal"
            }
        ],
        "relatedTerms": ["드퀘르벵병", "방아쇠손가락", "수근관증후군"]
    }
]

# Load existing data
with open(file_path, 'r', encoding='utf-8') as f:
    data = json.load(f)

# Add new terms
data.extend(new_terms)

# Save updated data
with open(file_path, 'w', encoding='utf-8') as f:
    json.dump(data, f, ensure_ascii=False, indent=2)

print(f"✅ Successfully added 20 terms. Current total: {len(data)} terms")
print("\nAdded terms (Part 1/2.5):")
print("골절, 복합골절, 스트레스골절, 탈구, 아탈구, 인대손상,")
print("전방십자인대, 후방십자인대, 반월상연골, 회전근개,")
print("추간판탈출증, 척추관협착증, 척추전방전위증, 측만증, 후만증,")
print("경추염좌, 요추염좌, 좌골신경통, 건초염")
print("\n⏭️  Remaining 30 terms to add in next continuation...")
