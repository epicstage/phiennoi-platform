#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Medical Terms Batch Addition Script - Nutrition/Diet/Lifestyle Medicine
Adds 10 new terms to medical.json with Tier S quality (90+ score)
"""

import json
import os

# Construct absolute file path
file_path = os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', 'data', 'terms', 'medical.json')

# New terms to add - Nutrition/Diet/Lifestyle Medicine theme
new_terms = [
    {
        "slug": "tu-van-dinh-duong",
        "korean": "영양상담",
        "vietnamese": "Tư vấn dinh dưỡng",
        "hanja": "營養相談",
        "hanjaReading": "營(경영할 영) + 養(기를 양) + 相(서로 상) + 談(말씀 담)",
        "pronunciation": "뜨번잉증",
        "meaningKo": "환자의 건강 상태와 질병 특성에 맞춘 식이요법과 영양 섭취에 대해 전문가와 상담하는 것을 의미합니다. 통역 시 주의할 점은 한국에서는 영양사(영양士)가 주로 담당하지만 베트남에서는 의사가 직접 영양 상담을 하는 경우가 많다는 점입니다. '상담'을 단순히 'Tư vấn'으로만 번역하지 말고, 병원 내 공식 서비스인지 일반 조언인지 구분해야 합니다. 입원 환자의 경우 '영양 평가(Đánh giá dinh dưỡng)'가 선행되므로 맥락을 파악해야 합니다. 한국 병원에서는 보험 적용 여부가 중요하므로 '급여/비급여' 개념도 함께 설명할 수 있어야 합니다.",
        "meaningVi": "Dịch vụ tư vấn chuyên môn về chế độ ăn uống và dinh dưỡng phù hợp với tình trạng sức khỏe và bệnh lý của bệnh nhân. Ở Hàn Quốc, dịch vụ này thường do chuyên viên dinh dưỡng (영양사) đảm nhận và có thể được bảo hiểm y tế chi trả trong một số trường hợp như bệnh tiểu đường, thận mạn, ung thư. Nội dung tư vấn bao gồm phân tích thói quen ăn uống, tính toán lượng calo cần thiết, và lập kế hoạch thực đơn phù hợp.",
        "context": "병원 영양과, 당뇨병 클리닉, 신장내과, 암 치료 병동에서 주로 사용됩니다. '영양상담 예약하세요', '영양상담이 필요합니다' 등의 표현으로 쓰입니다.",
        "culturalNote": "한국 병원에서는 영양사가 별도 직군으로 존재하며 영양상담실이 독립적으로 운영되는 경우가 많습니다. 반면 베트남에서는 의사가 영양 조언을 겸하는 경우가 많아 'chuyên viên dinh dưỡng'이라는 직군 자체가 생소할 수 있습니다. 한국에서는 당뇨, 신장질환 환자의 영양상담이 건강보험 적용이 되지만, 베트남에서는 대부분 본인 부담입니다. 또한 한국의 영양상담은 체계적인 식단표(thực đơn chi tiết)를 제공하지만, 베트남에서는 일반적인 조언 수준인 경우가 많습니다.",
        "commonMistakes": [
            {
                "mistake": "'Tư vấn ăn uống'으로 번역",
                "correction": "'Tư vấn dinh dưỡng' 사용",
                "explanation": "'Ăn uống'은 일반적인 식사를 의미하며, 의료 전문 서비스인 영양상담의 전문성을 표현하지 못합니다. 'Dinh dưỡng'이 영양학적 의미를 정확히 전달합니다."
            },
            {
                "mistake": "영양사를 'Bác sĩ dinh dưỡng'으로 번역",
                "correction": "'Chuyên viên dinh dưỡng' 또는 'Nhà dinh dưỡng' 사용",
                "explanation": "영양사는 의사(Bác sĩ)가 아닙니다. 한국에서는 별도의 국가자격증을 가진 전문직이므로 'Chuyên viên'으로 표현해야 정확합니다."
            },
            {
                "mistake": "상담 내용을 'Lời khuyên'(조언)으로만 표현",
                "correction": "'Kế hoạch dinh dưỡng cá nhân hóa'(개인 맞춤 영양 계획)로 구체화",
                "explanation": "한국의 영양상담은 단순 조언이 아니라 체계적인 식단 계획, 칼로리 계산, 추적 관리를 포함하는 전문 서비스입니다."
            },
            {
                "mistake": "보험 적용을 'Miễn phí'(무료)로 설명",
                "correction": "'Được bảo hiểm y tế chi trả'(보험 적용) 또는 'Tự chi trả'(본인부담) 구분",
                "explanation": "무료가 아니라 보험 적용 여부에 따라 본인부담금이 발생합니다. 정확한 비용 정보 전달이 중요합니다."
            }
        ],
        "examples": [
            {
                "ko": "당뇨 진단 받으셨으니 영양상담을 받아보시는 게 좋겠습니다.",
                "vi": "Anh/chị đã được chẩn đoán tiểu đường, nên tham khảo tư vấn dinh dưỡng.",
                "situation": "formal"
            },
            {
                "ko": "영양상담 예약은 1층 영양과에서 하시면 됩니다.",
                "vi": "Có thể đặt lịch tư vấn dinh dưỡng tại khoa Dinh dưỡng ở tầng 1.",
                "situation": "onsite"
            },
            {
                "ko": "이번 영양상담에서 저염식 식단표를 받으셨어요.",
                "vi": "Trong buổi tư vấn dinh dưỡng này, anh/chị đã nhận được thực đơn chế độ ăn ít muối.",
                "situation": "informal"
            }
        ],
        "relatedTerms": ["영양평가", "식이요법", "영양사", "당뇨식이", "치료식"]
    },
    {
        "slug": "dinh-duong-qua-ong-thong",
        "korean": "경관영양",
        "vietnamese": "Dinh dưỡng qua ống thông",
        "hanja": "經管營養",
        "hanjaReading": "經(경로 경) + 管(관 관) + 營(경영할 영) + 養(기를 양)",
        "pronunciation": "잉증과옹통",
        "meaningKo": "입으로 음식을 섭취할 수 없는 환자에게 코나 위장에 삽입한 관(튜브)을 통해 영양액을 공급하는 방법입니다. 통역 시 주의할 점은 'ống thông'이 일반적인 튜브가 아니라 의료용 영양공급관이라는 점을 명확히 해야 합니다. 한국에서는 비위관(L-tube), 비공장관(L-J tube), 위루관(gastrostomy) 등 삽입 위치에 따라 세부 명칭이 다르므로 정확한 종류를 확인해야 합니다. '경관'이라는 한자어가 생소할 수 있으니 '튜브를 통한 영양공급'으로 풀어 설명하는 것이 효과적입니다. 환자 가족에게 설명할 때는 경관영양의 필요성과 관리 방법을 함께 안내해야 합니다.",
        "meaningVi": "Phương pháp cung cấp dinh dưỡng qua ống thông được đặt vào dạ dày hoặc ruột non cho bệnh nhân không thể ăn uống bằng đường miệng. Các loại phổ biến bao gồm: ống thông qua mũi vào dạ dày (ống thông mũi-dạ dày), ống thông qua mũi vào ruột non (ống thông mũi-tá tràng), hoặc ống thông trực tiếp qua thành bụng (ống thông dạ dày qua da). Phương pháp này thường áp dụng cho bệnh nhân hôn mê, nuốt khó, hoặc phẫu thuật đường tiêu hóa. Dung dịch dinh dưỡng được thiết kế đặc biệt với đầy đủ calo, protein, vitamin và khoáng chất.",
        "context": "중환자실, 신경과, 재활의학과, 암 병동에서 주로 사용됩니다. '경관영양 시작합니다', 'L-tube 삽입하겠습니다' 등의 표현으로 쓰입니다.",
        "culturalNote": "한국 병원에서는 경관영양이 매우 체계적으로 관리되며, 영양사가 환자별 맞춤 영양액 처방을 계산하고, 간호사가 투여 속도와 위치를 정밀하게 모니터링합니다. 베트남에서는 경관영양 관리 시스템이 덜 정교한 경우가 많아, 가족이 직접 영양액 주입을 담당하는 경우도 있습니다. 한국에서는 경관영양 합병증(흡인성 폐렴, 설사 등) 예방을 위한 프로토콜이 엄격하지만, 베트남에서는 이러한 교육이 부족할 수 있습니다. 또한 한국에서는 장기 경관영양 환자를 위한 '위루술(gastrostomy)' 시술이 일반적이지만, 베트남에서는 상대적으로 드뭅니다.",
        "commonMistakes": [
            {
                "mistake": "'Ống dây'로 관(tube)을 번역",
                "correction": "'Ống thông' 또는 'Ống sonde' 사용",
                "explanation": "'Ống dây'는 일반 케이블이나 전선을 의미합니다. 의료용 영양공급관은 'Ống thông'이 정확한 의료 용어입니다."
            },
            {
                "mistake": "비위관을 'Ống thông mũi'로만 번역",
                "correction": "'Ống thông mũi-dạ dày' (nasogastric tube)로 완전히 표현",
                "explanation": "삽입 경로(mũi)뿐 아니라 최종 위치(dạ dày)까지 명시해야 정맥주사관 등과 혼동되지 않습니다."
            },
            {
                "mistake": "영양액을 'Nước dinh dưỡng'(영양수)로 번역",
                "correction": "'Dung dịch dinh dưỡng' 또는 'Sữa dinh dưỡng đặc biệt' 사용",
                "explanation": "'Nước'는 단순한 물을 연상시킵니다. 경관영양액은 의료용으로 설계된 특수 영양 제품이므로 'dung dịch'(용액)이 적절합니다."
            },
            {
                "mistake": "가족에게 '집에서 직접 주입하세요'라고 안내",
                "correction": "'반드시 교육받은 후 시행' 및 '정기적인 병원 방문 관리 필요' 강조",
                "explanation": "경관영양은 흡인, 감염 등 심각한 합병증 위험이 있으므로, 체계적인 교육과 추적 관리가 필수입니다."
            }
        ],
        "examples": [
            {
                "ko": "환자분이 의식이 없으셔서 경관영양을 시작하겠습니다.",
                "vi": "Bệnh nhân bất tỉnh nên chúng tôi sẽ bắt đầu cung cấp dinh dưỡng qua ống thông.",
                "situation": "formal"
            },
            {
                "ko": "L-tube로 하루 1500칼로리 영양액을 주입하고 있습니다.",
                "vi": "Đang truyền dung dịch dinh dưỡng 1500 calo mỗi ngày qua ống thông mũi-dạ dày.",
                "situation": "onsite"
            },
            {
                "ko": "경관영양 하시는 동안 머리를 30도 이상 올려주세요.",
                "vi": "Trong khi truyền dinh dưỡng qua ống thông, vui lòng nâng đầu giường lên trên 30 độ.",
                "situation": "informal"
            }
        ],
        "relatedTerms": ["비위관", "위루술", "영양액", "흡인성폐렴", "연하곤란"]
    },
    {
        "slug": "dinh-duong-qua-duong-tinh-mach",
        "korean": "정맥영양",
        "vietnamese": "Dinh dưỡng qua đường tĩnh mạch",
        "hanja": "靜脈營養",
        "hanjaReading": "靜(고요할 정) + 脈(맥 맥) + 營(경영할 영) + 養(기를 양)",
        "pronunciation": "잉증과증맥",
        "meaningKo": "소화기계를 통하지 않고 정맥을 통해 직접 영양분을 공급하는 방법으로, 소화 기능이 심각하게 손상되었거나 장을 쉬게 해야 하는 환자에게 사용됩니다. 통역 시 주의할 점은 말초정맥영양(PPN)과 중심정맥영양(TPN)을 구분해야 한다는 것입니다. TPN은 대량의 영양을 장기간 공급할 수 있지만 중심정맥관 삽입이 필요하고 감염 위험이 높습니다. '정맥영양'이라는 용어가 생소할 수 있으니 '링거를 통한 영양 공급'으로 쉽게 설명할 수 있지만, 일반 수액(링거)과는 성분과 목적이 다르다는 점을 반드시 강조해야 합니다. 환자 가족에게는 비용이 고액이며 합병증 위험이 있음을 사전에 안내해야 합니다.",
        "meaningVi": "Phương pháp cung cấp dinh dưỡng trực tiếp vào máu qua đường tĩnh mạch, bỏ qua hệ tiêu hóa. Có hai loại chính: dinh dưỡng tĩnh mạch ngoại vi (PPN - qua tĩnh mạch tay/chân) và dinh dưỡng tĩnh mạch trung tâm (TPN - qua tĩnh mạch lớn gần tim). TPN được sử dụng khi bệnh nhân không thể sử dụng đường tiêu hóa trong thời gian dài, như sau phẫu thuật lớn đường ruột, viêm tụy cấp nặng, hoặc suy ruột. Dung dịch TPN chứa glucose, amino acid, lipid, vitamin, và chất điện giải, được pha chế riêng theo nhu cầu từng bệnh nhân.",
        "context": "중환자실, 외과 병동, 소화기내과, 종양내과에서 주로 사용됩니다. 'TPN 시작합니다', '중심정맥관 삽입 후 정맥영양 공급하겠습니다' 등의 표현으로 쓰입니다.",
        "culturalNote": "한국 병원에서는 정맥영양이 고도로 전문화된 영역으로, 영양지원팀(NST: Nutrition Support Team)이 처방, 조제, 모니터링을 담당합니다. TPN 용액은 무균 조제실에서 약사가 환자별로 맞춤 제조하며, 매일 혈액검사로 전해질과 혈당을 추적합니다. 베트남에서는 TPN 사용이 상대적으로 제한적이며, 표준화된 기성품 영양액을 사용하는 경우가 많습니다. 한국에서는 TPN의 고비용(하루 10-20만원)이 부담이지만 보험 적용이 되는 반면, 베트남에서는 대부분 본인 부담입니다. 또한 한국에서는 PICC line(말초삽입 중심정맥관) 사용이 보편화되어 장기 TPN이 안전하게 관리되지만, 베트남에서는 이 기술이 덜 보급되어 있습니다.",
        "commonMistakes": [
            {
                "mistake": "정맥영양을 'Truyền dịch'(수액)로 번역",
                "correction": "'Dinh dưỡng tĩnh mạch' 또는 'Dinh dưỡng qua đường truyền' 사용",
                "explanation": "'Truyền dịch'은 일반 수액(saline, dextrose)을 의미합니다. 정맥영양은 완전한 영양 공급이 목적이므로 'dinh dưỡng'이 반드시 포함되어야 합니다."
            },
            {
                "mistake": "TPN을 'Tiêm dinh dưỡng'(영양 주사)로 표현",
                "correction": "'Dinh dưỡng tĩnh mạch trung tâm (TPN)' 또는 'Dinh dưỡng hoàn toàn qua đường tĩnh mạch' 사용",
                "explanation": "'Tiêm'은 근육주사나 피하주사를 연상시킵니다. TPN은 지속적인 정맥 주입(truyền tĩnh mạch)입니다."
            },
            {
                "mistake": "PPN과 TPN을 구분하지 않고 모두 '정맥영양'으로만 통역",
                "correction": "PPN은 'dinh dưỡng tĩnh mạch ngoại vi', TPN은 'dinh dưỡng tĩnh mạch trung tâm'으로 구분",
                "explanation": "두 방법은 투여 경로, 영양분 농도, 사용 기간, 합병증 위험이 완전히 다르므로 반드시 구별해야 합니다."
            },
            {
                "mistake": "비용 설명 시 'Rất đắt'(매우 비싸다)로만 표현",
                "correction": "구체적 금액 범위와 보험 적용 여부 안내",
                "explanation": "막연한 '비싸다'는 표현은 불안을 초래합니다. '하루 약 15만원, 건강보험 적용 시 본인부담 20%' 등 구체적 정보를 제공해야 합니다."
            }
        ],
        "examples": [
            {
                "ko": "장 수술 후 회복될 때까지 TPN으로 영양을 공급하겠습니다.",
                "vi": "Sau phẫu thuật ruột, chúng tôi sẽ cung cấp dinh dưỡng qua đường tĩnh mạch trung tâm (TPN) cho đến khi phục hồi.",
                "situation": "formal"
            },
            {
                "ko": "중심정맥관 통해서 하루 2000칼로리 정맥영양 들어가고 있어요.",
                "vi": "Đang truyền 2000 calo mỗi ngày qua ống thông tĩnh mạch trung tâm.",
                "situation": "onsite"
            },
            {
                "ko": "정맥영양 하는 동안 혈당이 높아질 수 있으니까 자주 체크할 거예요.",
                "vi": "Trong khi dùng dinh dưỡng tĩnh mạch, đường huyết có thể tăng nên chúng tôi sẽ kiểm tra thường xuyên.",
                "situation": "informal"
            }
        ],
        "relatedTerms": ["중심정맥관", "말초정맥영양", "영양지원팀", "전해질불균형", "PICC"]
    },
    {
        "slug": "che-do-an-tieu-duong",
        "korean": "당뇨식이",
        "vietnamese": "Chế độ ăn tiểu đường",
        "hanja": "糖尿食餌",
        "hanjaReading": "糖(엿 당) + 尿(오줌 뇨) + 食(밥 식) + 餌(미끼 이)",
        "pronunciation": "쩨도언띠에우득",
        "meaningKo": "당뇨병 환자의 혈당 조절을 위해 설계된 특수 식사 요법으로, 탄수화물 섭취량을 조절하고 식이섬유를 늘리며 규칙적인 식사 시간을 유지하는 것이 핵심입니다. 통역 시 주의할 점은 '당뇨식'이 단순히 설탕을 빼는 것이 아니라 총 탄수화물 양과 혈당지수(GI)를 관리하는 과학적 식단이라는 점을 강조해야 합니다. 한국에서는 '식품교환표'를 활용한 당뇨식이 교육이 체계적으로 이루어지지만, 베트남에서는 이러한 도구가 생소할 수 있습니다. '밥을 아예 먹지 마세요'가 아니라 '적정량의 밥을 규칙적으로 드세요'라는 메시지가 중요하며, 환자가 좋아하는 음식을 완전히 금지하기보다는 양과 빈도를 조절하는 현실적인 접근이 필요합니다.",
        "meaningVi": "Chế độ ăn uống được thiết kế đặc biệt cho bệnh nhân tiểu đường nhằm kiểm soát đường huyết, bao gồm việc điều chỉnh lượng carbohydrate, tăng chất xơ, giảm đường tinh luyện, và duy trì bữa ăn đều đặn. Nguyên tắc chính là ăn 3 bữa chính và 2-3 bữa phụ đều đặn, chọn thực phẩm có chỉ số đường huyết (GI) thấp như ngũ cốc nguyên hạt, rau xanh, và đạm nạc. Tránh đồ ngọt, nước ngọt có ga, và thực phẩm chiên rán. Lượng carbohydrate mỗi bữa nên được phân bổ đều để tránh tăng đường huyết đột ngột.",
        "context": "내분비내과, 당뇨병 클리닉, 영양과, 입원 병동에서 주로 사용됩니다. '당뇨식으로 주문하세요', '당뇨식이 교육 받으셨나요' 등의 표현으로 쓰입니다.",
        "culturalNote": "한국 병원에서는 당뇨식이 교육이 매우 체계적이며, 1:1 맞춤 교육, 식품교환표 제공, 외식 가이드까지 포함됩니다. 입원 시 제공되는 당뇨식은 칼로리와 탄수화물이 정밀하게 계산되어 나옵니다. 베트남에서는 당뇨식 개념이 '설탕만 피하면 된다'는 단순한 이해에 머무르는 경우가 많고, 쌀밥(cơm trắng) 중심 식습관 때문에 탄수화물 조절이 어렵습니다. 한국에서는 '당뇨병 식품교환표'로 음식을 6가지 군으로 나눠 교환 가능하도록 교육하지만, 베트남에는 이러한 도구가 표준화되어 있지 않습니다. 또한 한국 음식(김치, 나물 등)은 저칼로리 고섬유질이라 당뇨식에 유리하지만, 베트남 음식은 느억맘(nước mắm)의 높은 염분과 튀긴 요리가 많아 조절이 필요합니다.",
        "commonMistakes": [
            {
                "mistake": "'Không ăn đường'(설탕 안 먹기)로만 설명",
                "correction": "'Kiểm soát lượng carbohydrate tổng thể'(총 탄수화물 조절) 강조",
                "explanation": "당뇨식의 핵심은 설탕뿐 아니라 밥, 빵, 국수 등 모든 탄수화물의 총량과 배분을 관리하는 것입니다."
            },
            {
                "mistake": "'Ăn ít cơm'(밥 적게 먹기)로만 번역",
                "correction": "'Ăn lượng cơm vừa phải, đều đặn mỗi bữa'(적정량을 규칙적으로) 표현",
                "explanation": "탄수화물을 극단적으로 줄이면 저혈당 위험이 있고, 불규칙하게 먹으면 혈당 변동이 커집니다. '적당량을 규칙적으로'가 핵심입니다."
            },
            {
                "mistake": "과일을 'Trái cây tốt cho sức khỏe, ăn nhiều được'(건강에 좋으니 많이 먹어도 됨)로 안내",
                "correction": "'Trái cây có đường tự nhiên, nên ăn với khối lượng giới hạn'(과일도 당분 있으니 제한된 양) 설명",
                "explanation": "과일의 과당도 혈당을 올립니다. 하루 1-2회, 주먹 크기 분량으로 제한해야 합니다."
            },
            {
                "mistake": "식품교환표를 설명 없이 'Bảng thay thế thực phẩm'으로만 번역",
                "correction": "개념을 먼저 설명: '같은 양의 carbohydrate를 가진 음식끼리 바꿔 먹을 수 있는 목록'",
                "explanation": "식품교환표는 베트남에 없는 개념이므로, 용도와 사용법을 함께 설명해야 환자가 이해할 수 있습니다."
            }
        ],
        "examples": [
            {
                "ko": "당뇨 환자분이시니까 입원 식사는 당뇨식으로 나갈 겁니다.",
                "vi": "Vì anh/chị là bệnh nhân tiểu đường nên suất ăn trong bệnh viện sẽ là chế độ ăn tiểu đường.",
                "situation": "formal"
            },
            {
                "ko": "당뇨식이 교육 오늘 2시에 영양과에서 받으시면 됩니다.",
                "vi": "Anh/chị có thể tham gia buổi giáo dục chế độ ăn tiểu đường lúc 2 giờ chiều hôm nay tại khoa Dinh dưỡng.",
                "situation": "onsite"
            },
            {
                "ko": "과일도 당분이 있으니까 하루 사과 한 개 정도만 드세요.",
                "vi": "Trái cây cũng có đường nên chỉ nên ăn khoảng một quả táo mỗi ngày thôi.",
                "situation": "informal"
            }
        ],
        "relatedTerms": ["혈당지수", "식품교환표", "탄수화물계산", "당화혈색소", "저혈당"]
    },
    {
        "slug": "che-do-an-it-muoi",
        "korean": "저염식",
        "vietnamese": "Chế độ ăn ít muối",
        "hanja": "低鹽食",
        "hanjaReading": "低(낮을 저) + 鹽(소금 염) + 食(밥 식)",
        "pronunciation": "쩨도언잇무어이",
        "meaningKo": "고혈압, 심부전, 신장질환 환자의 나트륨 섭취를 제한하기 위한 식사요법으로, 하루 나트륨 섭취량을 2000mg(소금 5g) 이하로 제한하는 것이 목표입니다. 통역 시 주의할 점은 '저염'이 단순히 음식에 소금을 덜 넣는 것이 아니라 가공식품, 장류, 젓갈 등에 숨어있는 나트륨까지 관리해야 한다는 점입니다. 한국 음식은 김치, 된장, 간장 등 발효식품에 나트륨이 많아 저염식 실천이 어렵습니다. 환자에게 '싱겁게 드세요'보다는 '국물을 남기세요', '김치는 물에 헹궈 드세요'처럼 구체적인 실천 방법을 안내해야 합니다. 저염식 식단에서 맛을 내기 위해 향신료, 허브, 레몬즙 등을 활용할 수 있다는 대안도 제시해야 합니다.",
        "meaningVi": "Chế độ ăn hạn chế natri dành cho bệnh nhân tăng huyết áp, suy tim, hoặc bệnh thận, với mục tiêu giới hạn lượng natri dưới 2000mg mỗi ngày (tương đương khoảng 5g muối ăn). Nguyên tắc bao gồm: tránh thực phẩm chế biến sẵn (xúc xích, thịt hun khói, đồ hộp), hạn chế nước mắm và nước tương, không ăn đồ muối chua, giảm ăn ngoài. Nên nấu ăn tại nhà để kiểm soát lượng muối, sử dụng gia vị tự nhiên như tỏi, hành, gừng, chanh để tăng hương vị thay vì muối.",
        "context": "순환기내과, 신장내과, 심장내과, 영양과에서 주로 사용됩니다. '저염식 처방합니다', '저염식 드시고 계신가요' 등의 표현으로 쓰입니다.",
        "culturalNote": "한국 음식은 김치, 된장찌개, 국물 요리 등 나트륨 함량이 매우 높은 편입니다. 한국인의 평균 나트륨 섭취량은 WHO 권장량의 2배가 넘습니다. 한국 병원에서는 저염식 교육 시 '국물 반만 드세요', '김치는 하루 2쪽 이하'처럼 한국 식문화에 맞춤화된 지침을 제공합니다. 베트남 음식도 느억맘(nước mắm), 간장(xì dầu), 새우젓(mắm tôm) 등 염도가 높은 양념을 많이 사용하지만, 한국만큼 국물 문화가 강하지 않아 상대적으로 저염식 실천이 용이할 수 있습니다. 그러나 베트남에서는 '저염' 제품(muối ít natri)이 거의 없고, 외식 시 염도 조절 요청이 어려운 문화적 차이가 있습니다. 한국에서는 저염 간장, 저염 된장 등 대체 제품이 보편화되어 있습니다.",
        "commonMistakes": [
            {
                "mistake": "'Ăn nhạt'(싱겁게 먹기)로만 표현",
                "correction": "'Hạn chế natri dưới 2000mg/ngày' 등 구체적 수치 제공",
                "explanation": "'싱겁다'는 주관적 표현입니다. 정량적 목표(하루 나트륨 2000mg)를 제시해야 환자가 명확히 이해합니다."
            },
            {
                "mistake": "소금만 강조하고 가공식품의 숨은 나트륨 언급 안 함",
                "correction": "'Thực phẩm chế biến sẵn có nhiều natri ẩn' (가공식품에 숨은 나트륨 많음) 교육",
                "explanation": "햄, 소시지, 라면, 빵, 치즈 등에 나트륨이 대량 포함되어 있지만 짠맛이 느껴지지 않아 간과되기 쉽습니다."
            },
            {
                "mistake": "김치를 'Không ăn kimchi'(김치 먹지 마세요)로 금지",
                "correction": "'Rửa kimchi với nước trước khi ăn, chỉ ăn 2-3 miếng/ngày' (물에 헹궈서 하루 2-3쪽만)",
                "explanation": "한국인에게 김치 완전 금지는 비현실적입니다. 현실적인 절충안(물에 헹구기, 양 제한)을 제시해야 순응도가 높아집니다."
            },
            {
                "mistake": "국물을 'Không uống canh'(국 마시지 마세요)로 금지",
                "correction": "'Chỉ ăn phần rau và thịt, bỏ nước canh' (건더기만 먹고 국물은 남기세요) 안내",
                "explanation": "한국에서 국은 식사의 필수 요소입니다. 전면 금지보다는 '건더기는 먹고 국물만 남기기'가 현실적입니다."
            }
        ],
        "examples": [
            {
                "ko": "신장 기능이 안 좋으셔서 저염식 식단으로 바꾸겠습니다.",
                "vi": "Vì chức năng thận không tốt nên chúng tôi sẽ chuyển sang chế độ ăn ít muối.",
                "situation": "formal"
            },
            {
                "ko": "국은 건더기만 드시고 국물은 남겨주세요. 나트륨이 많아요.",
                "vi": "Vui lòng chỉ ăn phần thịt và rau trong canh, bỏ nước canh vì có nhiều natri.",
                "situation": "onsite"
            },
            {
                "ko": "라면이나 햄 같은 가공식품은 짜니까 드시지 마세요.",
                "vi": "Đừng ăn thực phẩm chế biến sẵn như mì gói hay giăm bông vì chúng rất mặn.",
                "situation": "informal"
            }
        ],
        "relatedTerms": ["나트륨", "고혈압", "부종", "심부전", "만성신부전"]
    },
    {
        "slug": "phong-kham-beo-phi",
        "korean": "비만클리닉",
        "vietnamese": "Phòng khám béo phì",
        "hanja": "肥滿클리닉",
        "hanjaReading": "肥(살찔 비) + 滿(찰 만) + [외래어]",
        "pronunciation": "퐁캄베오피",
        "meaningKo": "비만 환자의 체중 감량과 대사질환 관리를 전문으로 하는 의료 클리닉으로, 단순히 다이어트 상담이 아니라 의학적 평가, 식이요법, 운동처방, 약물치료, 필요시 수술까지 포괄하는 종합 치료를 제공합니다. 통역 시 주의할 점은 한국의 비만클리닉이 미용 목적의 다이어트센터와는 다른 정식 의료기관이라는 점을 명확히 해야 합니다. BMI 25 이상이거나 복부비만, 대사증후군이 있는 경우 건강보험 적용을 받을 수 있습니다. '살을 빼고 싶어서'라는 미용적 동기보다는 '당뇨 예방', '고혈압 관리' 등 의학적 필요성을 강조하는 것이 환자의 동기부여와 보험 적용에 유리합니다. 비만클리닉에서는 체성분 분석, 기초대사량 측정, 혈액검사 등 과학적 평가를 기반으로 개인 맞춤 치료 계획을 수립합니다.",
        "meaningVi": "Phòng khám chuyên khoa điều trị béo phì và quản lý bệnh chuyển hóa liên quan, cung cấp đánh giá y tế toàn diện, tư vấn dinh dưỡng, kê đơn vận động, điều trị thuốc, và phẫu thuật giảm cân khi cần thiết. Khác với trung tâm thẩm mỹ, phòng khám béo phì là cơ sở y tế chính thức do bác sĩ chuyên khoa điều hành. Điều trị bao gồm: phân tích thành phần cơ thể, xét nghiệm máu (đường huyết, lipid máu, hormone), lập kế hoạch ăn uống cá nhân hóa, tư vấn tâm lý hành vi, và theo dõi định kỳ. Ở Hàn Quốc, bệnh nhân có BMI ≥25 hoặc có biến chứng như tiểu đường, tăng huyết áp có thể được bảo hiểm y tế hỗ trợ.",
        "context": "가정의학과, 내분비내과, 건강검진센터에서 주로 운영됩니다. '비만클리닉 예약하세요', '체중 관리 프로그램 시작하겠습니다' 등의 표현으로 쓰입니다.",
        "culturalNote": "한국에서는 비만이 질병으로 인식되며, 비만클리닉이 종합병원 내에 정식 진료과로 존재합니다. 의사, 영양사, 운동처방사, 심리상담사가 팀을 이루어 다학제적 치료를 제공합니다. 한국은 BMI 25 이상을 비만으로 분류(아시아 기준)하며, 서구(BMI 30 이상)보다 기준이 낮습니다. 베트남에서도 비만이 증가 추세이지만 전문 비만클리닉은 드물고, 대부분 일반 내과나 영양상담으로 대체됩니다. 한국에서는 비만 치료에 GLP-1 작용제(삭센다, 위고비 등) 처방이 흔하지만, 베트남에서는 이러한 약물의 접근성이 제한적입니다. 또한 한국에서는 비만대사수술(위소매절제술, 위우회술)이 보편화되어 있고 보험 적용도 가능하지만, 베트남에서는 아직 제한적입니다. 문화적으로 한국은 '마른 몸'에 대한 사회적 압박이 강해 정상 체중인 사람도 비만클리닉을 찾는 경우가 있지만, 베트남은 상대적으로 체형에 대한 관용적 태도가 있습니다.",
        "commonMistakes": [
            {
                "mistake": "비만클리닉을 'Trung tâm giảm cân'(다이어트센터)로 번역",
                "correction": "'Phòng khám béo phì' 또는 'Phòng khám chuyên khoa béo phì' 사용",
                "explanation": "'Trung tâm giảm cân'은 미용/피트니스 시설을 연상시킵니다. 비만클리닉은 의사가 진료하는 의료기관이므로 'phòng khám'(클리닉)이 적절합니다."
            },
            {
                "mistake": "BMI 기준을 설명 없이 숫자만 제시",
                "correction": "한국(아시아) 기준과 국제 기준이 다르다는 점 명시",
                "explanation": "한국은 BMI 25 이상을 비만으로 분류하지만, 베트남 환자는 국제 기준(BMI 30)에 익숙할 수 있어 혼란 가능성이 있습니다."
            },
            {
                "mistake": "비만 치료약을 'Thuốc giảm cân'(다이어트약)로만 표현",
                "correction": "'Thuốc điều trị béo phì theo chỉ định bác sĩ'(의사 처방 비만 치료약) 강조",
                "explanation": "시중 다이어트약과 구분하여, 의학적 근거가 있는 전문의약품임을 명확히 해야 합니다."
            },
            {
                "mistake": "비만수술을 'Phẫu thuật thẩm mỹ'(미용수술)로 분류",
                "correction": "'Phẫu thuật điều trị béo phì'(비만 치료 수술) 또는 'Phẫu thuật chuyển hóa'(대사수술) 사용",
                "explanation": "비만수술은 외모가 아니라 당뇨, 고혈압 등 대사질환 치료가 목적이므로 미용수술과 구별해야 합니다."
            }
        ],
        "examples": [
            {
                "ko": "BMI가 30이 넘으시니까 비만클리닉에서 체계적으로 관리받으시는 게 좋겠습니다.",
                "vi": "Vì BMI của anh/chị trên 30, nên tốt nhất là được quản lý có hệ thống tại phòng khám béo phì.",
                "situation": "formal"
            },
            {
                "ko": "비만클리닉에서 체성분 검사하고 식단 상담 받으실 거예요.",
                "vi": "Tại phòng khám béo phì, anh/chị sẽ làm xét nghiệm thành phần cơ thể và nhận tư vấn chế độ ăn.",
                "situation": "onsite"
            },
            {
                "ko": "당뇨도 있으시니까 체중 감량이 꼭 필요합니다. 비만클리닉 한번 가보세요.",
                "vi": "Vì anh/chị cũng có tiểu đường nên việc giảm cân rất cần thiết. Hãy thử đến phòng khám béo phì một lần.",
                "situation": "informal"
            }
        ],
        "relatedTerms": ["체질량지수", "복부비만", "대사증후군", "식이요법", "운동처방"]
    },
    {
        "slug": "phong-kham-cai-thuoc",
        "korean": "금연클리닉",
        "vietnamese": "Phòng khám cai thuốc",
        "hanja": "禁煙클리닉",
        "hanjaReading": "禁(금할 금) + 煙(연기 연) + [외래어]",
        "pronunciation": "퐁캄까이투억",
        "meaningKo": "흡연자의 금연을 돕기 위한 전문 클리닉으로, 니코틴 중독을 의학적으로 치료하고 금연 성공률을 높이기 위해 상담, 행동치료, 약물치료(니코틴 패치, 금연 보조제 등)를 복합적으로 제공합니다. 통역 시 주의할 점은 한국의 금연클리닉이 보건소와 병원 양쪽에서 운영되며, 보건소는 무료, 병원은 유료지만 더 집중적인 치료를 제공한다는 차이를 설명해야 합니다. '의지만 있으면 끊을 수 있다'는 인식과 달리, 니코틴 중독은 질병이므로 의학적 도움이 필요하다는 점을 강조해야 합니다. 금연 성공률은 전문가 도움 없이 혼자 시도할 때 5% 미만이지만, 금연클리닉 이용 시 30% 이상으로 증가합니다. 금연 시도 중 금단증상(짜증, 불안, 집중력 저하)이 나타날 수 있으며, 이는 정상 반응이므로 약물로 완화할 수 있다고 안내해야 합니다.",
        "meaningVi": "Phòng khám chuyên khoa hỗ trợ người hút thuốc cai nghiện nicotine thông qua tư vấn hành vi, liệu pháp tâm lý, và điều trị bằng thuốc (miếng dán nicotine, thuốc cai thuốc lá). Ở Hàn Quốc, phòng khám cai thuốc được vận hành tại cả trung tâm y tế công cộng (miễn phí) và bệnh viện (có phí). Chương trình điều trị kéo dài từ 8-12 tuần, bao gồm gặp bác sĩ định kỳ, theo dõi nồng độ CO trong hơi thở, và điều chỉnh liều thuốc. Các phương pháp hỗ trợ bao gồm thay thế nicotine (miếng dán, kẹo cao su), thuốc kê đơn (varenicline, bupropion), và tư vấn hành vi nhận thức (CBT).",
        "context": "가정의학과, 호흡기내과, 보건소에서 주로 운영됩니다. '금연클리닉 등록하세요', '금연 보조제 처방하겠습니다' 등의 표현으로 쓰입니다.",
        "culturalNote": "한국 정부는 국가 금연정책의 일환으로 전국 보건소에 무료 금연클리닉을 운영하며, 등록자에게 니코틴 패치와 상담을 6개월간 무료 제공합니다. 한국 남성 흡연율은 약 30%로 베트남(약 45%)보다 낮지만, 금연 압력은 훨씬 강합니다(공공장소 전면 금연, 담뱃갑 경고 그림 등). 베트남에서는 금연클리닉이 드물고 금연 치료에 대한 인식도 낮습니다. 한국에서는 금연 실패 후 재도전이 당연하게 받아들여지며(평균 5-7회 시도 후 성공), 재등록을 적극 권장합니다. 베트남에서는 금연이 '개인의 의지' 문제로 여겨져 의학적 치료의 필요성이 간과되는 경우가 많습니다. 한국의 금연클리닉에서는 CO 측정기(일산화탄소 측정)로 객관적 금연 성공을 확인하지만, 베트남에서는 이러한 장비가 보편적이지 않습니다.",
        "commonMistakes": [
            {
                "mistake": "금연클리닉을 'Tư vấn bỏ thuốc'(금연 상담)로만 번역",
                "correction": "'Phòng khám cai thuốc' 또는 'Phòng khám cai nghiện nicotine' 사용",
                "explanation": "단순 상담이 아니라 약물치료와 정기 방문을 포함한 의료 프로그램이므로 'phòng khám'(클리닉)이 적절합니다."
            },
            {
                "mistake": "니코틴 패치를 'Băng dán'(일반 밴드)로 번역",
                "correction": "'Miếng dán nicotine' 또는 'Cao dán cai thuốc' 사용",
                "explanation": "니코틴 대체요법 약물임을 명확히 표현해야 합니다. 'Băng dán'은 상처 치료용 밴드를 의미합니다."
            },
            {
                "mistake": "'Chỉ cần quyết tâm là bỏ được'(의지만 있으면 끊을 수 있다)로 조언",
                "correction": "'Nghiện nicotine là bệnh, cần điều trị y khoa'(니코틴 중독은 질병, 의학 치료 필요) 교육",
                "explanation": "의지만으로는 성공률이 5% 미만입니다. 니코틴 중독을 질병으로 인식하고 전문 치료를 받도록 유도해야 합니다."
            },
            {
                "mistake": "금단증상을 '참으세요'로 안내",
                "correction": "'Các triệu chứng cai nghiện có thể giảm bằng thuốc'(금단증상은 약으로 완화 가능) 설명",
                "explanation": "짜증, 불안, 집중력 저하 등 금단증상은 니코틴 대체요법이나 약물로 관리할 수 있습니다. 무조건 참으라고 하면 실패율이 높아집니다."
            }
        ],
        "examples": [
            {
                "ko": "폐 건강을 위해서 금연클리닉 이용해보시는 걸 추천드립니다.",
                "vi": "Để bảo vệ sức khỏe phổi, tôi khuyên anh/chị nên sử dụng dịch vụ phòng khám cai thuốc.",
                "situation": "formal"
            },
            {
                "ko": "금연클리닉 등록하시면 니코틴 패치랑 상담 무료로 받으실 수 있어요.",
                "vi": "Nếu đăng ký phòng khám cai thuốc, anh/chị có thể nhận miễn phí miếng dán nicotine và tư vấn.",
                "situation": "onsite"
            },
            {
                "ko": "혼자 끊기 어려우시면 금연클리닉 가보세요. 약도 주고 도와줘요.",
                "vi": "Nếu khó cai một mình thì hãy đến phòng khám cai thuốc. Họ sẽ cho thuốc và hỗ trợ anh/chị.",
                "situation": "informal"
            }
        ],
        "relatedTerms": ["니코틴중독", "금연보조제", "금단증상", "바레니클린", "행동치료"]
    },
    {
        "slug": "phong-kham-giac-ngu",
        "korean": "수면클리닉",
        "vietnamese": "Phòng khám giấc ngủ",
        "hanja": "睡眠클리닉",
        "hanjaReading": "睡(잘 수) + 眠(잘 면) + [외래어]",
        "pronunciation": "퐁캄짝응우",
        "meaningKo": "불면증, 수면무호흡증, 하지불안증후군 등 다양한 수면장애를 진단하고 치료하는 전문 클리닉입니다. 통역 시 주의할 점은 단순히 '잠을 못 잔다'는 증상이 아니라 수면다원검사(PSG)라는 정밀 검사를 통해 수면 중 뇌파, 호흡, 심박수, 산소포화도를 측정하여 정확한 진단을 내린다는 점입니다. 특히 수면무호흡증은 단순한 코골이가 아니라 수면 중 호흡이 멈춰 심혈관질환 위험을 높이는 심각한 질환이므로, 가족이 '코골이가 심하다'고 말할 때 수면클리닉 방문을 권유해야 합니다. 한국에서는 수면다원검사가 1박 입원으로 진행되며 건강보험 적용이 가능합니다. 불면증 치료는 수면제 처방뿐 아니라 인지행동치료(CBT-I)를 병행하며, 장기 복용 시 의존성을 고려하여 약물 조절을 합니다.",
        "meaningVi": "Phòng khám chuyên khoa chẩn đoán và điều trị các rối loạn giấc ngủ như mất ngủ, ngưng thở khi ngủ (sleep apnea), hội chứng chân không yên (restless legs syndrome). Xét nghiệm chính là đa ký giấc ngủ (polysomnography - PSG), bệnh nhân ngủ qua đêm tại bệnh viện trong khi các cảm biến theo dõi sóng não, nhịp tim, nhịp thở, nồng độ oxy máu, và vận động cơ thể. Điều trị bao gồm: liệu pháp hành vi nhận thức cho mất ngủ (CBT-I), máy thở CPAP cho ngưng thở khi ngủ, thuốc an thần khi cần thiết, và tư vấn vệ sinh giấc ngủ (sleep hygiene).",
        "context": "신경과, 정신건강의학과, 이비인후과에서 주로 운영됩니다. '수면클리닉 예약하세요', '수면다원검사 받아보시겠습니까' 등의 표현으로 쓰입니다.",
        "culturalNote": "한국에서는 수면장애가 질병으로 인식되며, 수면클리닉이 대형병원에 정식 진료과로 존재합니다. 수면다원검사(PSG)는 건강보험 적용이 되어 본인부담금 10-20만원 정도입니다. 한국인의 약 20%가 만성 불면증을 겪으며, 직장인의 과로와 스트레스가 주요 원인입니다. 베트남에서는 수면클리닉이 드물고, 수면다원검사 시설이 대도시 일부 병원에만 있습니다. 베트남에서는 '잠 못 자는 것'을 개인 문제로 여겨 의료기관을 찾지 않는 경향이 있습니다. 한국에서는 수면무호흡증 치료에 CPAP(지속적 기도양압) 기계가 보편적으로 사용되고 건강보험 적용(대여 방식)이 가능하지만, 베트남에서는 이 장비가 고가이며 접근성이 낮습니다. 한국의 수면클리닉에서는 '수면위생 교육'(일정한 수면 시간, 카페인 제한, 침실 환경 조절 등)을 필수로 제공하지만, 베트남에서는 이러한 행동치료 개념이 덜 알려져 있습니다.",
        "commonMistakes": [
            {
                "mistake": "수면클리닉을 '불면증 치료만 하는 곳'으로 설명",
                "correction": "'불면증, 수면무호흡증, 기면증 등 모든 수면장애 진단 및 치료' 포괄적 설명",
                "explanation": "수면클리닉은 불면증뿐 아니라 다양한 수면장애를 다루는 종합 진료과입니다."
            },
            {
                "mistake": "수면다원검사를 '잠자는 걸 관찰하는 검사'로만 설명",
                "correction": "'뇌파, 심전도, 호흡, 산소포화도 등을 종합 측정하는 정밀 검사' 상세 설명",
                "explanation": "단순 관찰이 아니라 여러 생체신호를 동시 기록하는 과학적 검사임을 명확히 해야 합니다."
            },
            {
                "mistake": "코골이를 'Ngáy không nguy hiểm'(위험하지 않음)으로 설명",
                "correction": "'Ngáy to có thể là dấu hiệu ngưng thở khi ngủ, cần khám'(큰 코골이는 수면무호흡 신호, 진료 필요) 경고",
                "explanation": "코골이가 심하면 수면무호흡증 가능성이 높으며, 이는 심근경색, 뇌졸중 위험을 증가시킵니다."
            },
            {
                "mistake": "수면제를 'Có thể uống lâu dài'(장기 복용 가능)로 안내",
                "correction": "'Thuốc ngủ chỉ dùng ngắn hạn, có nguy cơ phụ thuộc'(수면제는 단기 사용, 의존성 위험) 경고",
                "explanation": "수면제는 의존성과 내성이 생길 수 있으므로, 최소 기간 최소 용량 사용 원칙을 강조해야 합니다."
            }
        ],
        "examples": [
            {
                "ko": "코골이가 심하고 자주 깨신다면 수면무호흡증 가능성이 있으니 수면클리닉 가보세요.",
                "vi": "Nếu ngáy to và thường xuyên tỉnh giấc, có thể là ngưng thở khi ngủ, nên đến phòng khám giấc ngủ kiểm tra.",
                "situation": "formal"
            },
            {
                "ko": "수면다원검사 하려면 하룻밤 입원하셔야 해요. 검사실에서 주무시면서 측정합니다.",
                "vi": "Để làm xét nghiệm đa ký giấc ngủ, anh/chị cần nhập viện qua đêm. Chúng tôi sẽ đo trong khi anh/chị ngủ ở phòng xét nghiệm.",
                "situation": "onsite"
            },
            {
                "ko": "불면증이 2주 이상 계속되면 수면클리닉에서 정확한 원인 찾아보는 게 좋아요.",
                "vi": "Nếu mất ngủ kéo dài hơn 2 tuần, tốt nhất là đến phòng khám giấc ngủ để tìm nguyên nhân chính xác.",
                "situation": "informal"
            }
        ],
        "relatedTerms": ["수면다원검사", "수면무호흡증", "불면증", "CPAP", "수면위생"]
    },
    {
        "slug": "thuc-pham-chuc-nang",
        "korean": "건강기능식품",
        "vietnamese": "Thực phẩm chức năng",
        "hanja": "健康機能食品",
        "hanjaReading": "健(튼튼할 건) + 康(편안할 강) + 機(틀 기) + 能(능할 능) + 食(밥 식) + 品(물건 품)",
        "pronunciation": "틱팜쭉낭",
        "meaningKo": "일상 식사에서 부족한 영양소를 보충하거나 건강 유지에 도움을 주는 기능성 성분을 함유한 식품으로, 한국 식품의약품안전처(식약처)의 인증을 받은 제품을 말합니다. 통역 시 주의할 점은 건강기능식품이 '약'이 아니라 '식품'이므로 질병 치료 효과는 없으며, 건강 유지 및 개선에 도움을 주는 보조적 역할이라는 점을 명확히 해야 합니다. 한국에서는 건강기능식품에 표시된 '기능성' 문구(예: 혈행 개선, 피로 회복, 뼈 건강)가 식약처 인증을 받은 것이므로 신뢰할 수 있지만, 과장광고에 주의해야 합니다. 홍삼, 오메가3, 비타민D, 유산균, 루테인 등이 대표적이며, 환자가 복용 중인 약과 상호작용 가능성이 있으므로 의사에게 반드시 알려야 합니다. '건강기능식품 드시고 계신가요?'라는 질문은 약물 상호작용 확인을 위한 중요한 질문입니다.",
        "meaningVi": "Thực phẩm bổ sung có chứa các thành phần chức năng giúp duy trì và cải thiện sức khỏe, bổ sung dinh dưỡng thiếu hụt trong chế độ ăn hàng ngày. Ở Hàn Quóc, thực phẩm chức năng phải được Cục Quản lý An toàn Thực phẩm và Dược phẩm (MFDS) chứng nhận về tính an toàn và hiệu quả. Các loại phổ biến bao gồm: hồng sâm (cải thiện miễn dịch), omega-3 (sức khỏe tim mạch), vitamin D (sức khỏe xương), men vi sinh (tiêu hóa), lutein (thị lực). Quan trọng: thực phẩm chức năng KHÔNG phải thuốc, không có tác dụng chữa bệnh, chỉ hỗ trợ duy trì sức khỏe. Cần thông báo cho bác sĩ nếu đang dùng vì có thể tương tác với thuốc điều trị.",
        "context": "약국, 병원, 건강검진센터, 영양상담실에서 자주 언급됩니다. '어떤 건강기능식품 드세요?', '홍삼 드셔도 됩니다' 등의 표현으로 쓰입니다.",
        "culturalNote": "한국은 건강기능식품 시장이 매우 발달하여 연간 5조원 규모이며, 국민 70% 이상이 하나 이상의 건강기능식품을 복용합니다. 특히 홍삼(Korean red ginseng)은 한국 대표 건강식품으로 인식되며, 선물용으로도 많이 사용됩니다. 한국에서는 건강기능식품에 대한 규제가 엄격하여 '건강기능식품' 마크(초록색 원형)가 있는 제품만 기능성을 표시할 수 있습니다. 베트남에서도 'Thực phẩm chức năng' 시장이 성장 중이지만 규제가 상대적으로 느슨하고, 효과가 검증되지 않은 제품도 많습니다. 한국 환자들은 병원 진료 시 건강기능식품 복용 사실을 자발적으로 말하지 않는 경우가 많은데, 특히 혈액응고에 영향을 주는 오메가3, 은행잎추출물 등은 수술 전 중단이 필요하므로 반드시 확인해야 합니다. 베트남에서는 건강기능식품을 '약'으로 인식하는 경향이 있어, '이것은 약이 아니라 건강 보조 식품'이라는 점을 명확히 교육해야 합니다.",
        "commonMistakes": [
            {
                "mistake": "건강기능식품을 'Thuốc bổ'(보약)로 번역",
                "correction": "'Thực phẩm chức năng' 또는 'Thực phẩm bổ sung dinh dưỡng' 사용",
                "explanation": "'Thuốc'는 약(medicine)을 의미합니다. 건강기능식품은 식품(thực phẩm) 범주이며 질병 치료 목적이 아닙니다."
            },
            {
                "mistake": "'약이 아니니까 의사에게 말할 필요 없다'고 안내",
                "correction": "'반드시 의사에게 알려야 함, 약물 상호작용 가능' 강조",
                "explanation": "오메가3(출혈 위험), 홍삼(혈압 변화), 칼슘(항생제 흡수 방해) 등 약물과 상호작용할 수 있습니다."
            },
            {
                "mistake": "건강기능식품의 효과를 'Chữa bệnh'(병 치료)로 설명",
                "correction": "'Hỗ trợ duy trì sức khỏe, không chữa bệnh'(건강 유지 도움, 질병 치료 아님) 명확화",
                "explanation": "건강기능식품은 질병 치료 효과가 없습니다. 과장된 기대를 방지하기 위해 보조적 역할임을 강조해야 합니다."
            },
            {
                "mistake": "식약처 인증 마크를 설명 없이 'Logo'로만 언급",
                "correction": "'Dấu chứng nhận của Cục Quản lý Dược phẩm, đảm bảo an toàn'(식약처 인증, 안전 보장) 설명",
                "explanation": "한국의 건강기능식품 인증 마크는 안전성과 기능성이 검증되었다는 의미이므로, 신뢰성 지표로 설명해야 합니다."
            }
        ],
        "examples": [
            {
                "ko": "현재 복용 중인 건강기능식품이 있으신가요? 약과 같이 드시면 문제될 수 있어요.",
                "vi": "Anh/chị có đang dùng thực phẩm chức năng nào không? Có thể có vấn đề nếu dùng cùng thuốc.",
                "situation": "formal"
            },
            {
                "ko": "수술 일주일 전부터는 오메가3 같은 건강기능식품 중단하세요.",
                "vi": "Từ một tuần trước phẫu thuật, vui lòng ngừng dùng thực phẩm chức năng như omega-3.",
                "situation": "onsite"
            },
            {
                "ko": "홍삼은 건강기능식품이지 약은 아니에요. 병을 치료하는 건 아닙니다.",
                "vi": "Hồng sâm là thực phẩm chức năng chứ không phải thuốc. Nó không chữa bệnh.",
                "situation": "informal"
            }
        ],
        "relatedTerms": ["영양제", "보조제", "홍삼", "오메가3", "프로바이오틱스"]
    },
    {
        "slug": "thuc-pham-bo-sung",
        "korean": "영양제",
        "vietnamese": "Thực phẩm bổ sung",
        "hanja": "營養劑",
        "hanjaReading": "營(경영할 영) + 養(기를 양) + 劑(약제 제)",
        "pronunciation": "틱팜보쑹",
        "meaningKo": "부족한 영양소를 보충하기 위해 섭취하는 비타민, 미네랄, 아미노산 등의 제품으로, 건강기능식품보다 넓은 개념이며 일상적으로 더 많이 쓰이는 용어입니다. 통역 시 주의할 점은 영양제와 건강기능식품이 엄밀히는 다르지만(영양제는 영양소 보충, 건강기능식품은 기능성 인정), 일상 대화에서는 혼용되므로 맥락을 파악해야 합니다. '종합비타민', '비타민D', '철분제', '칼슘제' 등이 대표적이며, 특히 임산부, 노인, 성장기 어린이에게 자주 처방됩니다. 한국에서는 약국에서 쉽게 구입할 수 있지만, 과다 복용 시 부작용(비타민A 과다, 철분 중독 등)이 있으므로 권장량을 지켜야 합니다. 또한 '영양제 먹으면 소변이 노래진다'는 것은 비타민B 때문이며 정상 반응입니다. 환자가 '영양제 처방해 주세요'라고 요청할 때, 실제 필요성을 판단하기 위해 식습관과 증상을 먼저 확인해야 합니다.",
        "meaningVi": "Các sản phẩm bổ sung vitamin, khoáng chất, amino acid để bù đắp dinh dưỡng thiếu hụt trong chế độ ăn hàng ngày. Khác với thực phẩm chức năng (có chứng nhận hiệu quả cụ thể), thực phẩm bổ sung chủ yếu cung cấp các chất dinh dưỡng cơ bản. Các loại phổ biến bao gồm: vitamin tổng hợp (multivitamin), vitamin D (xương và miễn dịch), sắt (thiếu máu), canxi (xương), axit folic (phụ nữ mang thai). Thực phẩm bổ sung không phải thuốc nhưng cần tuân thủ liều lượng khuyến nghị vì dùng quá liều có thể gây độc (ví dụ: vitamin A, sắt). Không nên tự ý dùng mà nên tham khảo bác sĩ hoặc dược sĩ.",
        "context": "약국, 병원, 산부인과, 소아과에서 자주 언급됩니다. '영양제 드세요', '철분제 처방하겠습니다' 등의 표현으로 쓰입니다.",
        "culturalNote": "한국에서는 영양제 복용이 매우 보편적이며, 특히 직장인들이 피로 회복을 위해 종합비타민을 일상적으로 복용합니다. 약국에서 처방전 없이 구입 가능하며, 편의점에서도 일부 제품을 판매합니다. 한국인은 비타민D 결핍률이 높아(햇볕 노출 부족) 의사들이 비타민D 보충을 적극 권장합니다. 임산부에게는 엽산과 철분제가 필수로 처방되며, 건강보험 적용도 됩니다. 베트남에서도 영양제 사용이 증가하고 있지만 한국만큼 보편적이지는 않으며, '영양은 음식으로 섭취해야 한다'는 인식이 강합니다. 한국에서는 '아침 영양제'를 챙겨 먹는 것이 건강관리의 기본으로 여겨지지만, 베트남에서는 의사 처방 없이 영양제를 복용하는 것에 대한 거부감이 있을 수 있습니다. 한국의 영양제는 대부분 캡슐/정제 형태인 반면, 베트남에서는 시럽이나 분말 형태가 더 흔합니다. 또한 한국에서는 '어린이 영양제'(키 성장, 집중력) 시장이 발달했지만, 베트남에서는 덜 보편적입니다.",
        "commonMistakes": [
            {
                "mistake": "영양제를 'Thuốc vitamin'(비타민 약)로 번역",
                "correction": "'Thực phẩm bổ sung vitamin' 또는 'Vitamin bổ sung' 사용",
                "explanation": "'Thuốc'는 의약품을 의미합니다. 영양제는 식품 범주에 가까우므로 'thực phẩm bổ sung'이 정확합니다."
            },
            {
                "mistake": "'많이 먹을수록 좋다'는 뉘앙스로 안내",
                "correction": "'Dùng đúng liều khuyến nghị, dùng quá liều có hại'(권장량 준수, 과다 복용 해로움) 경고",
                "explanation": "지용성 비타민(A, D, E, K)과 철분은 과다 복용 시 체내 축적되어 중독 증상을 일으킬 수 있습니다."
            },
            {
                "mistake": "영양제와 건강기능식품을 같은 것으로 설명",
                "correction": "영양제는 'bổ sung dinh dưỡng', 건강기능식품은 'thực phẩm chức năng có chứng nhận' 구분",
                "explanation": "법적으로 다른 범주이며, 건강기능식품은 식약처 인증을 받은 기능성 제품입니다."
            },
            {
                "mistake": "'영양제로 식사 대체 가능'으로 안내",
                "correction": "'Thực phẩm bổ sung chỉ hỗ trợ, không thể thay thế bữa ăn'(영양제는 보조, 식사 대체 불가) 강조",
                "explanation": "영양제는 균형 잡힌 식사를 대체할 수 없으며, 식사를 통한 영양 섭취가 우선입니다."
            }
        ],
        "examples": [
            {
                "ko": "임신 초기시니까 엽산이랑 철분제 드시는 게 좋습니다.",
                "vi": "Vì đang ở giai đoạn đầu thai kỳ, anh/chị nên dùng axit folic và sắt bổ sung.",
                "situation": "formal"
            },
            {
                "ko": "비타민D 수치가 낮으시니까 영양제 3개월 드시고 다시 검사할게요.",
                "vi": "Vì nồng độ vitamin D thấp, anh/chị nên dùng thực phẩm bổ sung vitamin D trong 3 tháng rồi xét nghiệm lại.",
                "situation": "onsite"
            },
            {
                "ko": "종합비타민은 아침 식후에 드시는 게 흡수가 잘 돼요.",
                "vi": "Vitamin tổng hợp nên uống sau bữa sáng để hấp thụ tốt hơn.",
                "situation": "informal"
            }
        ],
        "relatedTerms": ["비타민", "미네랄", "엽산", "철분제", "칼슘제"]
    }
]

def add_terms():
    """Add new medical terms to medical.json"""
    print(f"📂 Reading file: {file_path}")

    # Read existing data
    with open(file_path, 'r', encoding='utf-8') as f:
        data = json.load(f)

    print(f"✅ Loaded {len(data)} existing terms")

    # Get existing slugs for duplicate check
    existing_slugs = {term['slug'] for term in data}
    print(f"🔍 Checking for duplicates among {len(existing_slugs)} existing slugs...")

    # Filter out duplicates
    new_terms_to_add = []
    duplicates = []

    for term in new_terms:
        if term['slug'] in existing_slugs:
            duplicates.append(term['slug'])
        else:
            new_terms_to_add.append(term)

    if duplicates:
        print(f"⚠️  Found {len(duplicates)} duplicate(s): {', '.join(duplicates)}")

    if not new_terms_to_add:
        print("⛔ No new terms to add (all duplicates)")
        return

    # Add new terms
    print(f"➕ Adding {len(new_terms_to_add)} new terms...")
    data.extend(new_terms_to_add)

    # Write back to file
    with open(file_path, 'w', encoding='utf-8') as f:
        json.dump(data, f, ensure_ascii=False, indent=2)

    print(f"✅ Successfully added {len(new_terms_to_add)} terms")
    print(f"📊 Total terms now: {len(data)}")
    print("\n🎯 Added terms (slugs):")
    for term in new_terms_to_add:
        print(f"   - {term['slug']} ({term['korean']} / {term['vietnamese']})")

if __name__ == "__main__":
    add_terms()
