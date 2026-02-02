#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
의료 용어 추가 스크립트 v5-t (내과/소화기/호흡기)
10개의 Tier S 품질 용어 추가
"""

import json
import os

# 파일 경로 설정
file_path = os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', 'data', 'terms', 'medical.json')

# 추가할 용어 데이터
new_terms = [
    {
        "slug": "noi-soi-da-day",
        "korean": "위내시경",
        "vietnamese": "Nội soi dạ dày",
        "hanja": "胃內視鏡",
        "hanjaReading": "胃(위 위) + 內(안 내) + 視(볼 시) + 鏡(거울 경)",
        "pronunciation": "노이 쏘이 자 다이",
        "meaningKo": "위 내부를 관찰하기 위해 내시경을 식도를 통해 삽입하여 검사하는 의료 절차입니다. 통역 시 주의할 점은 베트남에서는 사전 금식 시간이 한국보다 짧을 수 있으며, 수면내시경(nội soi có gây mê)과 일반내시경(nội soi không gây mê)을 명확히 구분해야 합니다. 환자에게 검사 전 준비사항을 설명할 때 '공복 8시간'을 정확히 전달하지 않으면 검사가 연기될 수 있으므로 주의가 필요합니다. 또한 조직검사(sinh thiết) 여부도 사전에 확인하여 통역해야 합니다.",
        "meaningVi": "Thủ thuật y tế sử dụng ống nội soi đưa qua thực quản để quan sát bên trong dạ dày. Bệnh nhân cần nhịn ăn trước khi làm thủ thuật. Ở Việt Nam thường yêu cầu nhịn ăn 6-8 tiếng, trong khi Hàn Quốc yêu cầu chặt chẽ hơn. Có hai loại: nội soi có gây mê (giúp bệnh nhân thoải mái hơn) và nội soi không gây mê.",
        "context": "소화기내과 진료, 건강검진, 위암 조기 발견",
        "culturalNote": "한국에서는 40세 이상 국민건강검진에 위내시경이 포함되어 2년마다 무료로 받을 수 있지만, 베트남에서는 건강보험 적용이 제한적이고 본인부담금이 높습니다. 한국 환자들은 수면내시경을 선호하는 반면, 베트남에서는 비용 문제로 일반내시경을 더 많이 선택합니다. 통역 시 검사 후 회복실 대기 시간, 보호자 동반 필요성 등을 명확히 안내해야 합니다.",
        "commonMistakes": [
            {
                "mistake": "Nội soi bụng (복강경)",
                "correction": "Nội soi dạ dày",
                "explanation": "복강경(laparoscopy)과 위내시경(gastroscopy)은 완전히 다른 시술입니다. 복강경은 복부에 구멍을 뚫어 카메라를 삽입하는 수술이고, 위내시경은 입을 통해 관을 삽입하는 검사입니다."
            },
            {
                "mistake": "Khám dạ dày (위 검사)",
                "correction": "Nội soi dạ dày (위내시경)",
                "explanation": "단순히 '위 검사'라고 하면 초음파, X-ray 등 다른 검사와 혼동될 수 있습니다. 정확히 '내시경'임을 명시해야 합니다."
            },
            {
                "mistake": "환자가 마취 없이는 못 받는다고 주장할 때 '진정제'를 '마취'로 통역",
                "correction": "Thuốc an thần nhẹ (진정제) ≠ Gây mê (전신마취)",
                "explanation": "수면내시경의 진정제는 전신마취가 아닙니다. 베트남 환자들이 '마취'를 두려워하는 경우가 많으므로 정확히 '진정제'임을 설명해야 합니다."
            },
            {
                "mistake": "Nội soi không đau (내시경은 안 아프다)",
                "correction": "Nội soi có thể gây khó chịu nhưng có thể chịu đựng được (불편할 수 있으나 참을 만하다)",
                "explanation": "통역사가 환자를 안심시키려다 과장하면 나중에 신뢰를 잃을 수 있습니다. 정직하게 불편함을 예고하되 관리 가능하다고 설명해야 합니다."
            }
        ],
        "examples": [
            {
                "ko": "내일 오전 9시에 위내시경 예약되어 있으니 오늘 밤 12시 이후로는 금식하세요.",
                "vi": "Ngày mai 9 giờ sáng anh có lịch nội soi dạ dày, vì vậy từ 12 giờ đêm nay anh phải nhịn ăn nhé.",
                "situation": "formal"
            },
            {
                "ko": "위내시경 결과 조직검사가 필요한 부위가 발견되어 생검을 시행했습니다.",
                "vi": "Kết quả nội soi dạ dày phát hiện vùng cần xét nghiệm mô, nên chúng tôi đã thực hiện sinh thiết.",
                "situation": "formal"
            },
            {
                "ko": "수면내시경 받으실 거면 검사 후에 운전 못 하시니까 보호자 모시고 오세요.",
                "vi": "Nếu anh làm nội soi có gây mê thì sau thủ thuật không được lái xe, nên phải có người nhà đi cùng nhé.",
                "situation": "onsite"
            }
        ],
        "relatedTerms": [
            "대장내시경",
            "조직검사",
            "헬리코박터균",
            "위염",
            "위암"
        ]
    },
    {
        "slug": "noi-soi-dai-trang",
        "korean": "대장내시경",
        "vietnamese": "Nội soi đại tràng",
        "hanja": "大腸內視鏡",
        "hanjaReading": "大(큰 대) + 腸(창자 장) + 內(안 내) + 視(볼 시) + 鏡(거울 경)",
        "pronunciation": "노이 쏘이 다이 짱",
        "meaningKo": "항문을 통해 내시경을 삽입하여 대장 내부를 관찰하는 검사입니다. 통역 시 가장 중요한 것은 검사 전 장 정결(làm sạch ruột) 과정을 정확히 설명하는 것입니다. 한국에서는 쿨프렙, 피코프렙 등의 하제를 사용하며, 복용 시간과 방법을 잘못 이해하면 검사가 불가능해집니다. '설사가 맑은 물처럼 나올 때까지'를 베트남어로 정확히 전달해야 하며, 용종 절제술(cắt polyp) 가능성도 사전에 설명해야 합니다. 베트남 환자들은 관장에 익숙하지만 한국식 경구 하제 복용법은 낯설 수 있습니다.",
        "meaningVi": "Thủ thuật đưa ống nội soi qua hậu môn để quan sát bên trong đại tràng và trực tràng. Trước khi làm, bệnh nhân phải uống thuốc nhuận tràng để làm sạch ruột hoàn toàn. Nước đi ngoài phải trong như nước lọc thì mới làm được. Trong quá trình nội soi, bác sĩ có thể cắt polyp nếu phát hiện. Ở Hàn Quốc, từ 50 tuổi được khám miễn phí theo bảo hiểm y tế quốc gia.",
        "context": "대장암 조기 발견, 혈변 원인 진단, 50세 이상 건강검진",
        "culturalNote": "한국에서는 50세 이상 국민건강검진에 대장내시경이 포함되며, 가족력이 있으면 더 일찍 권장됩니다. 베트남에서는 대장암 검진 문화가 덜 발달해 있어 '증상 없는데 왜 하느냐'는 반응을 보이는 환자가 많습니다. 통역 시 예방 검진의 중요성을 강조해야 합니다. 또한 한국에서는 검사 중 발견된 용종을 바로 제거하는 것이 일반적이지만, 베트남 환자들은 '사전 동의 없이 시술했다'고 오해할 수 있으므로 미리 설명이 필요합니다.",
        "commonMistakes": [
            {
                "mistake": "Chụp X-quang đại tràng (대장 X-ray)",
                "correction": "Nội soi đại tràng (대장내시경)",
                "explanation": "과거에는 바륨 관장 후 X-ray 촬영을 했으나, 현재는 내시경이 표준입니다. 환자가 'chụp'이라고 하면 영상 촬영으로 오해할 수 있습니다."
            },
            {
                "mistake": "Làm sạch bụng (뱃속을 깨끗이)",
                "correction": "Làm sạch ruột (장을 깨끗이)",
                "explanation": "'Bụng'은 복부 전체를 의미하여 모호합니다. 'Ruột'이라고 정확히 대장임을 명시해야 합니다."
            },
            {
                "mistake": "약을 먹으면 설사가 난다고만 말함",
                "correction": "Uống thuốc sẽ đi tiêu nhiều lần, nước phải trong như nước lọc (약을 먹으면 여러 번 설사하며, 물처럼 맑게 나와야 함)",
                "explanation": "단순히 설사가 난다고만 하면 환자가 준비 정도를 판단할 수 없습니다. '맑은 물'까지 나와야 한다는 기준을 명확히 해야 합니다."
            },
            {
                "mistake": "검사 중 polyp을 '혹'으로만 번역",
                "correction": "Polyp (khối u nhỏ ở niêm mạc ruột, có thể chuyển thành ung thư)",
                "explanation": "'혹'만으로는 환자가 심각성을 모를 수 있습니다. 암으로 발전 가능성을 설명해야 합니다."
            }
        ],
        "examples": [
            {
                "ko": "대장내시경 전날 저녁 6시부터 하제를 복용하시고, 당일 아침에도 추가 복용하셔야 합니다.",
                "vi": "Tối hôm trước ngày nội soi, từ 6 giờ tối anh bắt đầu uống thuốc nhuận tràng, và sáng hôm sau cũng phải uống thêm nữa.",
                "situation": "formal"
            },
            {
                "ko": "검사 중에 5mm 크기의 용종 2개를 발견해서 바로 제거했습니다.",
                "vi": "Trong quá trình nội soi phát hiện 2 polyp kích thước 5mm nên chúng tôi đã cắt bỏ ngay.",
                "situation": "formal"
            },
            {
                "ko": "용종 제거했으니까 일주일 동안은 무거운 것 들지 마시고 술, 담배 금지예요.",
                "vi": "Vì đã cắt polyp rồi nên trong một tuần đừng mang vác nặng, và cấm rượu bia, thuốc lá nhé.",
                "situation": "onsite"
            }
        ],
        "relatedTerms": [
            "용종",
            "대장암",
            "혈변",
            "장정결",
            "직장수지검사"
        ]
    },
    {
        "slug": "loet-da-day",
        "korean": "위궤양",
        "vietnamese": "Loét dạ dày",
        "hanja": "胃潰瘍",
        "hanjaReading": "胃(위 위) + 潰(헐 궤) + 瘍(부스럼 양)",
        "pronunciation": "로엣 자 다이",
        "meaningKo": "위 점막에 궤양이 생긴 상태로, 헬리코박터균 감염, 진통제 과다 복용, 스트레스 등이 원인입니다. 통역 시 주의할 점은 베트남어로 위궤양(loét dạ dày)과 십이지장궤양(loét tá tràng)을 명확히 구분해야 하며, 치료제인 PPI(thuốc ức chế bơm proton)를 '위산억제제'로 쉽게 풀어 설명해야 합니다. 한국에서는 헬리코박터 제균 치료가 표준이지만 베트nam 환자들은 항생제 복용을 꺼리는 경우가 많아 '왜 항생제를 먹어야 하는지' 설명이 필요합니다. 또한 '속쓰림'을 ợ nóng으로 잘못 통역하지 않도록 주의해야 합니다.",
        "meaningVi": "Tình trạng niêm mạc dạ dày bị tổn thương tạo thành vết loét. Nguyên nhân thường do vi khuẩn Helicobacter pylori, lạm dụng thuốc giảm đau, hoặc stress. Triệu chứng điển hình là đau bụng vùng thượng vị, đặc biệt khi đói hoặc ban đêm. Điều trị chủ yếu bằng thuốc ức chế bơm proton (PPI) và nếu có vi khuẩn HP thì phải dùng kháng sinh diệt khuẩn.",
        "context": "소화기내과 진료, 상복부 통증 호소, 헬리코박터 치료",
        "culturalNote": "한국에서는 위궤양을 '스트레스성 질환'으로 인식하는 경향이 강하지만, 실제로는 헬리코박터균이 주요 원인입니다. 베트남 환자들은 전통적으로 '위가 차다(dạ dày lạnh)'는 개념으로 이해하여 따뜻한 음식을 선호하며, 한약 처방을 병행하려는 경향이 있습니다. 통역 시 양방 치료의 중요성을 강조하되 문화적 배경을 존중해야 합니다. 또한 한국에서는 금연, 금주를 강력히 권고하지만 베트남 남성 환자들의 흡연율이 높아 순응도가 낮을 수 있습니다.",
        "commonMistakes": [
            {
                "mistake": "Đau dạ dày (위통)",
                "correction": "Loét dạ dày (위궤양)",
                "explanation": "단순 위통과 궤양은 다릅니다. 궤양은 점막 손상이 동반된 질환으로 진단명입니다."
            },
            {
                "mistake": "Thuốc kháng sinh (항생제) → 베트남 환자가 '감기약 아니냐'고 반문",
                "correction": "Thuốc diệt vi khuẩn HP gây loét dạ dày (위궤양 유발 헬리코박터균 제균제)",
                "explanation": "항생제의 목적을 구체적으로 설명하지 않으면 환자가 복용을 거부할 수 있습니다."
            },
            {
                "mistake": "Ợ nóng (속쓰림이 아닌 '신물')",
                "correction": "Nóng rát dạ dày (속쓰림)",
                "explanation": "'Ợ nóng'은 위산이 역류하는 증상(heartburn)이고, 위궤양의 통증은 'nóng rát' 또는 'đau rát'으로 표현해야 합니다."
            },
            {
                "mistake": "식이요법을 '부드러운 음식만 먹으라'로 단순화",
                "correction": "Tránh đồ cay, rượu bia, cà phê, thuốc giảm đau (자극적 음식, 술, 커피, 진통제 금지)",
                "explanation": "무엇을 피해야 하는지 구체적으로 나열해야 합니다. '부드러운 음식'만으로는 모호합니다."
            }
        ],
        "examples": [
            {
                "ko": "위내시경 결과 위궤양으로 진단되었으며, 헬리코박터균 검사도 양성입니다.",
                "vi": "Kết quả nội soi cho thấy anh bị loét dạ dày, và xét nghiệm vi khuẩn Helicobacter pylori cũng dương tính.",
                "situation": "formal"
            },
            {
                "ko": "제균 치료는 2주간 3가지 약을 복용하는데, 반드시 전부 다 드셔야 합니다.",
                "vi": "Liệu trình diệt khuẩn kéo dài 2 tuần với 3 loại thuốc, anh phải uống hết tất cả thuốc, không được bỏ sót.",
                "situation": "formal"
            },
            {
                "ko": "위궤양 환자는 아스피린 같은 진통제 먹으면 출혈 위험이 있어요.",
                "vi": "Người bị loét dạ dày mà uống thuốc giảm đau như aspirin thì có nguy cơ chảy máu đấy.",
                "situation": "onsite"
            }
        ],
        "relatedTerms": [
            "헬리코박터균",
            "십이지장궤양",
            "위염",
            "위출혈",
            "PPI"
        ]
    },
    {
        "slug": "viem-ruot",
        "korean": "장염",
        "vietnamese": "Viêm ruột",
        "hanja": "腸炎",
        "hanjaReading": "腸(창자 장) + 炎(불꽃 염)",
        "pronunciation": "비엠 주옷",
        "meaningKo": "세균, 바이러스, 기생충 등에 의해 장에 염증이 생긴 상태로, 설사와 복통이 주증상입니다. 통역 시 급성 장염(viêm ruột cấp)과 만성 염증성 장질환(bệnh viêm ruột mãn tính - IBD)을 반드시 구분해야 합니다. 식중독에 의한 급성 장염은 '며칠간 금식하고 수액 치료'로 회복되지만, 크론병이나 궤양성 대장염은 장기 치료가 필요합니다. 베트남 환자들은 설사 시 '지사제'를 바로 복용하려 하지만, 감염성 장염에서는 오히려 독소 배출을 방해할 수 있어 주의가 필요합니다. '탈수 여부 확인'이 치료의 핵심이므로 소변량, 입마름 등을 정확히 전달해야 합니다.",
        "meaningVi": "Tình trạng viêm nhiễm ở ruột do vi khuẩn, virus hoặc ký sinh trùng gây ra, có triệu chứng chính là tiêu chảy và đau bụng. Viêm ruột cấp tính (do ngộ độc thực phẩm) thường tự khỏi sau vài ngày với điều trị bổ sung nước. Tuy nhiên, cần phân biệt với bệnh viêm ruột mãn tính như Crohn hoặc viêm loét đại tràng, đây là bệnh tự miễn cần điều trị dài hạn. Quan trọng nhất là phòng ngừa mất nước bằng cách uống nhiều nước hoặc truyền dịch.",
        "context": "응급실 내원, 식중독 의심, 여행자 설사",
        "culturalNote": "한국에서는 급성 장염 환자에게 '미음→죽→밥' 순서로 식이를 진행하지만, 베트남에서는 'cháo lỏng'(묽은 죽)을 처음부터 권장하는 경우가 많습니다. 통역 시 한국 의사의 지시를 정확히 따르도록 설명해야 합니다. 또한 베트남 환자들은 '배가 차가워서 탈이 났다'고 생각하여 따뜻한 물을 많이 마시는데, 경구수액(ORS)의 중요성을 강조해야 합니다. 한국에서는 로타바이러스 백신이 보편화되어 있으나 베트남 환자들은 낯설 수 있습니다.",
        "commonMistakes": [
            {
                "mistake": "Tiêu chảy (설사) ≠ Viêm ruột (장염)",
                "correction": "Tiêu chảy는 증상, Viêm ruột는 질환명",
                "explanation": "설사는 증상이고 장염은 질환입니다. 환자가 '설사가 났다'고 하면 원인을 파악해야 합니다."
            },
            {
                "mistake": "Uống thuốc cầm tiêu chảy ngay (지사제 바로 복용)",
                "correction": "Viêm ruột do nhiễm khuẩn không nên uống thuốc cầm tiêu chảy (감염성 장염에는 지사제 금기)",
                "explanation": "감염성 장염에서 지사제는 독소 배출을 막아 증상을 악화시킬 수 있습니다. 의사 처방 없이 복용 금지임을 강조해야 합니다."
            },
            {
                "mistake": "Nhịn ăn hoàn toàn (완전 금식)",
                "correction": "Nhịn ăn đồ cứng, nhưng phải uống nhiều nước (고형식 금지, 수분 섭취 필수)",
                "explanation": "'금식'을 물까지 끊는 것으로 오해하면 탈수가 악화됩니다. 수분 섭취는 필수임을 명확히 해야 합니다."
            },
            {
                "mistake": "염증성 장질환을 단순 장염으로 통역",
                "correction": "Bệnh viêm ruột mãn tính (IBD) ≠ Viêm ruột cấp",
                "explanation": "크론병, 궤양성 대장염은 자가면역 질환으로 식중독과는 완전히 다릅니다. 혼동하면 환자가 질병의 심각성을 모를 수 있습니다."
            }
        ],
        "examples": [
            {
                "ko": "급성 장염으로 보이며, 탈수가 심하니 수액 치료부터 시작하겠습니다.",
                "vi": "Có vẻ là viêm ruột cấp tính, do mất nước nhiều nên chúng tôi sẽ truyền dịch trước.",
                "situation": "formal"
            },
            {
                "ko": "대변 검사에서 세균이 검출되면 항생제 치료가 필요할 수 있습니다.",
                "vi": "Nếu xét nghiệm phân phát hiện vi khuẩn thì có thể cần dùng kháng sinh.",
                "situation": "formal"
            },
            {
                "ko": "이틀 정도는 죽이나 미음만 드시고, 증상 좋아지면 서서히 밥 드세요.",
                "vi": "Khoảng 2 ngày anh chỉ ăn cháo loãng thôi, đợi bớt triệu chứng rồi từ từ ăn cơm.",
                "situation": "onsite"
            }
        ],
        "relatedTerms": [
            "식중독",
            "노로바이러스",
            "경구수액",
            "탈수",
            "염증성장질환"
        ]
    },
    {
        "slug": "xo-gan",
        "korean": "간경변",
        "vietnamese": "Xơ gan",
        "hanja": "肝硬變",
        "hanjaReading": "肝(간 간) + 硬(굳을 경) + 變(변할 변)",
        "pronunciation": "써 간",
        "meaningKo": "만성 간질환으로 인해 간 조직이 섬유화되어 굳어지는 비가역적 질환입니다. 통역 시 가장 중요한 것은 간경변의 원인(B형 간염, C형 간염, 알코올)을 정확히 파악하고 전달하는 것입니다. 베트남은 B형 간염 유병률이 높아 'xơ gan do viêm gan B'인 경우가 많으며, 한국 환자는 알코올성 간경변(xơ gan do rượu)이 상대적으로 많습니다. 합병증인 복수(cổ chướng), 정맥류 출혈(xuất huyết giãn tĩnh mạch), 간성뇌증(hôn mê gan)을 구분하여 통역해야 하며, '간이식'을 ghép gan으로 정확히 전달하되 베트남 환자들의 경제적 부담을 고려해야 합니다.",
        "meaningVi": "Bệnh gan mạn tính khiến mô gan bị xơ hóa và cứng lại, không thể hồi phục. Nguyên nhân chủ yếu ở Việt Nam là viêm gan B, trong khi ở Hàn Quốc thường do uống rượu nhiều. Biến chứng nguy hiểm bao gồm: cổ chướng (tích nước trong bụng), xuất huyết giãn tĩnh mạch thực quản, và hôn mê gan. Giai đoạn cuối có thể cần ghép gan. Bệnh nhân cần kiêng rượu tuyệt đối, ăn ít muối, và theo dõi định kỳ.",
        "context": "만성 간질환 관리, 간이식 평가, 복수 치료",
        "culturalNote": "한국에서는 간경변 환자에게 '금주'를 가장 강조하지만, 베트남 문화에서 술은 사회관계의 중요한 요소라 순응도가 낮을 수 있습니다. 통역 시 '단 한 잔도 안 된다(một giọt cũng không được)'를 명확히 전달해야 합니다. 또한 베트남에서는 간에 좋다는 민간요법(rau má, nghệ 등)을 병행하려는 환자가 많은데, 일부는 간에 부담을 줄 수 있어 의료진과 상의하도록 해야 합니다. 한국에서는 간이식이 활성화되어 있으나 베트남 환자들은 비용 문제로 접근성이 낮습니다.",
        "commonMistakes": [
            {
                "mistake": "Viêm gan (간염) = Xơ gan (간경변)",
                "correction": "Viêm gan은 염증, Xơ gan은 섬유화",
                "explanation": "간염은 간경변의 원인 질환입니다. 간경변은 간염이 오래되어 간이 굳어진 상태로 더 심각합니다."
            },
            {
                "mistake": "간이 나쁘다(Gan yếu)로만 설명",
                "correction": "Gan bị xơ cứng, không thể phục hồi (간이 섬유화되어 회복 불가)",
                "explanation": "'간이 약하다'는 표현은 가역적인 것으로 오해될 수 있습니다. 비가역적 손상임을 명확히 해야 합니다."
            },
            {
                "mistake": "Bụng to (배가 나옴) → 비만으로 오해",
                "correction": "Cổ chướng - tích nước trong bụng do xơ gan (복수 - 간경변으로 인한 복강 내 수분 축적)",
                "explanation": "복수는 복부 비만과 구분해야 합니다. 간경변의 심각한 합병증임을 설명해야 합니다."
            },
            {
                "mistake": "간수치가 높다고만 통역",
                "correction": "Men gan tăng cao, chức năng gan suy giảm nghiêm trọng (간효소 상승, 간기능 심각하게 저하)",
                "explanation": "간경변에서는 간효소 수치보다 '기능 저하'가 중요합니다. 알부민, PT 등 합성 기능을 함께 설명해야 합니다."
            }
        ],
        "examples": [
            {
                "ko": "B형 간염에 의한 간경변으로 진단되었으며, Child-Pugh 등급은 B입니다.",
                "vi": "Anh được chẩn đoán xơ gan do viêm gan B, mức độ Child-Pugh là B.",
                "situation": "formal"
            },
            {
                "ko": "복수가 차서 배가 불러오셨죠? 이뇨제 처방하고 염분 섭취를 줄여야 합니다.",
                "vi": "Bụng anh to lên vì tích nước phải không? Chúng tôi sẽ kê thuốc lợi tiểu và anh phải hạn chế muối.",
                "situation": "formal"
            },
            {
                "ko": "간경변은 술 한 방울도 절대 안 돼요. 맥주, 소주 다 끊으셔야 해요.",
                "vi": "Xơ gan thì tuyệt đối không được uống rượu, kể cả một giọt. Bia, soju đều phải bỏ hết.",
                "situation": "onsite"
            }
        ],
        "relatedTerms": [
            "B형간염",
            "간암",
            "복수",
            "간성뇌증",
            "간이식"
        ]
    },
    {
        "slug": "viem-phoi",
        "korean": "폐렴",
        "vietnamese": "Viêm phổi",
        "hanja": "肺炎",
        "hanjaReading": "肺(허파 폐) + 炎(불꽃 염)",
        "pronunciation": "비엠 포이",
        "meaningKo": "세균, 바이러스, 곰팡이 등에 의해 폐 조직에 염증이 생긴 감염성 질환입니다. 통역 시 지역사회획득폐렴(viêm phổi mắc tại cộng đồng)과 병원내폐렴(viêm phổi bệnh viện)을 구분해야 하며, 흉부 X-ray 소견을 '폐에 그림자가 보인다(có bóng mờ trên phổi)'로 설명해야 합니다. 베트남 환자들은 기침에 가래가 나오면 '감기가 심해진 것'으로 생각하지만, 고열, 호흡곤란이 동반되면 폐렴 가능성이 높음을 설명해야 합니다. 항생제 치료 기간을 임의로 단축하지 않도록 '최소 7일~10일 복용'을 강조하며, 노인 환자는 입원 치료가 필요할 수 있음을 미리 안내해야 합니다.",
        "meaningVi": "Bệnh nhiễm trùng ở mô phổi do vi khuẩn, virus hoặc nấm gây ra. Triệu chứng bao gồm sốt cao, ho có đờm, khó thở, đau ngực khi thở sâu. Chụp X-quang ngực sẽ thấy bóng mờ ở phổi. Điều trị chủ yếu bằng kháng sinh, thời gian tối thiểu 7-10 ngày và không được tự ý ngừng thuốc. Người già, trẻ em, hoặc có bệnh nền cần nhập viện. Có thể phòng ngừa bằng vắc-xin phế cầu.",
        "context": "호흡기내과 진료, 고열과 기침 호소, 입원 치료",
        "culturalNote": "한국에서는 노인과 만성질환자에게 폐렴구균 백신(vắc-xin phế cầu)을 적극 권장하며 국가예방접종에 포함되어 있으나, 베트남에서는 인식이 낮습니다. 통역 시 예방접종의 중요성을 설명해야 합니다. 또한 한국에서는 폐렴 입원 시 산소포화도 모니터링이 표준이지만, 베트남 환자들은 '손가락에 클립'의 의미를 모를 수 있어 설명이 필요합니다. 베트남 환자들은 가래 색깔(màu đờm)을 중요하게 생각하므로 누런 가래, 피섞인 가래 등을 구체적으로 질문받을 수 있습니다.",
        "commonMistakes": [
            {
                "mistake": "Cảm cúm nặng (독감이 심한 것)",
                "correction": "Viêm phổi (폐렴) - nghiêm trọng hơn cảm cúm",
                "explanation": "폐렴을 단순 독감 악화로 설명하면 환자가 심각성을 모를 수 있습니다. 폐렴은 별개의 질환임을 강조해야 합니다."
            },
            {
                "mistake": "Ho có đờm (기침 가래) = Viêm phổi",
                "correction": "Viêm phổi có ho, đờm, NHƯNG còn kèm sốt cao, khó thở",
                "explanation": "기침 가래만으로는 폐렴을 진단할 수 없습니다. 고열, 호흡곤란 등 동반 증상을 함께 설명해야 합니다."
            },
            {
                "mistake": "Uống kháng sinh 3 ngày là đủ (항생제 3일이면 충분)",
                "correction": "Phải uống kháng sinh ít nhất 7-10 ngày, không được tự ý ngừng (항생제 최소 7-10일, 임의 중단 금지)",
                "explanation": "증상이 호전되어도 항생제를 조기 중단하면 재발하거나 내성이 생길 수 있습니다. 전체 기간 복용을 강조해야 합니다."
            },
            {
                "mistake": "X-quang thấy bóng trắng (X-ray에 흰 그림자)",
                "correction": "X-quang thấy bóng mờ / thâm nhiễm (침윤 음영)",
                "explanation": "폐렴은 X-ray에서 '불투명한 음영'으로 나타납니다. '흰 그림자'는 모호하며, 'thâm nhiễm' 또는 'bóng mờ'가 정확합니다."
            }
        ],
        "examples": [
            {
                "ko": "흉부 X-ray 결과 우측 하엽에 폐렴 소견이 보이며, 입원 치료가 필요합니다.",
                "vi": "Kết quả chụp X-quang ngực cho thấy có viêm phổi ở thùy dưới bên phải, anh cần nhập viện điều trị.",
                "situation": "formal"
            },
            {
                "ko": "가래 검사에서 폐렴구균이 검출되어 페니실린 계열 항생제를 투여하겠습니다.",
                "vi": "Xét nghiệm đờm phát hiện vi khuẩn phế cầu, nên chúng tôi sẽ dùng kháng sinh nhóm penicillin.",
                "situation": "formal"
            },
            {
                "ko": "폐렴은 항생제 다 먹어야 해요. 열 떨어졌다고 끊으면 다시 재발해요.",
                "vi": "Viêm phổi phải uống hết kháng sinh. Đừng ngừng thuốc khi hết sốt, không thì tái phát đấy.",
                "situation": "onsite"
            }
        ],
        "relatedTerms": [
            "폐렴구균",
            "흉부X-ray",
            "산소포화도",
            "가래검사",
            "흡인성폐렴"
        ]
    },
    {
        "slug": "hen-suyen",
        "korean": "천식",
        "vietnamese": "Hen suyễn",
        "hanja": "喘息",
        "hanjaReading": "喘(숨찰 천) + 息(쉴 식)",
        "pronunciation": "헨 수옌",
        "meaningKo": "기도에 만성 염증이 생겨 기관지가 좁아지고 과민해져 호흡곤란, 천명음, 기침이 반복되는 질환입니다. 통역 시 가장 중요한 것은 '조절제(thuốc kiểm soát)'와 '증상완화제(thuốc giảm triệu chứng)'를 구분하는 것입니다. 베트남 환자들은 증상이 없을 때 흡입제 사용을 중단하는 경향이 있어, '매일 사용해야 한다'를 강조해야 합니다. 흡입기 사용법(cách dùng bình xịt)을 시연하며 통역하고, '입안을 헹구라'는 지시를 정확히 전달해야 합니다. 악화인자(yếu tố kích phát) 관리가 중요하므로 집먼지진드기, 반려동물, 담배연기 등을 피하도록 설명해야 합니다.",
        "meaningVi": "Bệnh viêm mạn tính đường hô hấp làm phế quản co thắt và nhạy cảm, gây khó thở, thở khò khè, ho. Có hai loại thuốc: thuốc kiểm soát (dùng hàng ngày dù không có triệu chứng) và thuốc giảm triệu chứng (dùng khi khó thở). Bệnh nhân cần tránh các yếu tố kích phát như bụi, lông thú, khói thuốc. Sử dụng bình xịt đúng cách rất quan trọng: lắc đều, thở hết khí, xịt và hít sâu, sau đó nhịn thở 10 giây, cuối cùng súc miệng.",
        "context": "호흡기내과 진료, 천명음 호소, 흡입제 처방",
        "culturalNote": "한국에서는 천식을 만성질환으로 인식하여 장기 관리를 강조하지만, 베트남 환자들은 '발작 시에만 치료하면 된다'고 생각하는 경향이 있습니다. 통역 시 '매일 조절제를 사용해야 발작을 예방한다'는 개념을 설명해야 합니다. 또한 한국에서는 흡입제가 표준 치료이지만, 베트남에서는 먹는 약을 선호하는 환자가 많아 흡입제의 장점(부작용 적음, 빠른 효과)을 설명해야 합니다. 베트남 환자들은 '천식은 어릴 때 생기는 병'으로 알고 있는 경우가 많아 성인 천식도 흔함을 설명해야 합니다.",
        "commonMistakes": [
            {
                "mistake": "Khó thở (호흡곤란) = Hen suyễn (천식)",
                "correction": "Khó thở는 증상, Hen suyễn은 질환명",
                "explanation": "호흡곤란은 천식의 증상 중 하나일 뿐입니다. 심장질환, 폐질환 등 다른 원인도 있을 수 있습니다."
            },
            {
                "mistake": "Thuốc xịt (흡입제) → 환자가 '스프레이'로 오해",
                "correction": "Bình xịt hen suyễn / Thuốc khí dung (천식 흡입기)",
                "explanation": "일반 스프레이와 구분하여 '천식 흡입기'임을 명확히 해야 합니다. 사용법도 다릅니다."
            },
            {
                "mistake": "증상 없으면 약 끊어도 된다고 통역",
                "correction": "Thuốc kiểm soát phải dùng hàng ngày, kể cả khi không có triệu chứng (조절제는 증상 없어도 매일 사용)",
                "explanation": "증상이 없는 것은 약이 효과가 있기 때문입니다. 중단하면 염증이 재발합니다."
            },
            {
                "mistake": "Thở mạnh vào bình xịt (흡입기에 세게 숨을 들이쉬라)",
                "correction": "Thở chậm, sâu và đều (천천히, 깊게, 고르게 흡입)",
                "explanation": "너무 빠르게 흡입하면 약이 목 뒤에만 남고 폐까지 도달하지 않습니다. 천천히 깊게 흡입해야 합니다."
            }
        ],
        "examples": [
            {
                "ko": "천식 진단을 받으셨고, 흡입 스테로이드를 매일 아침저녁으로 사용하셔야 합니다.",
                "vi": "Anh được chẩn đoán hen suyễn, phải dùng thuốc xịt steroid hít vào mỗi sáng và tối hàng ngày.",
                "situation": "formal"
            },
            {
                "ko": "폐기능 검사 결과 FEV1이 정상의 60%로 중등도 천식입니다.",
                "vi": "Kết quả đo chức năng hô hấp cho thấy FEV1 chỉ đạt 60% bình thường, là hen suyễn mức độ trung bình.",
                "situation": "formal"
            },
            {
                "ko": "발작 올 때는 이 파란색 흡입기 쓰시고, 갈색 거는 매일 쓰는 거예요.",
                "vi": "Khi lên cơn thì dùng bình xịt màu xanh này, còn bình màu nâu là dùng hàng ngày nhé.",
                "situation": "onsite"
            }
        ],
        "relatedTerms": [
            "흡입스테로이드",
            "속효성기관지확장제",
            "폐기능검사",
            "알레르기",
            "천명음"
        ]
    },
    {
        "slug": "benh-phoi-tac-nghen-man-tinh",
        "korean": "만성폐쇄성폐질환",
        "vietnamese": "Bệnh phổi tắc nghẽn mãn tính",
        "hanja": "慢性閉塞性肺疾患",
        "hanjaReading": "慢(느릴 만) + 性(성품 성) + 閉(닫을 폐) + 塞(막을 색) + 性(성품 성) + 肺(허파 폐) + 疾(병 질) + 患(근심 환)",
        "pronunciation": "벵 포이 닥 녠 만 띤",
        "meaningKo": "주로 흡연에 의해 기도와 폐포가 손상되어 공기 흐름이 제한되는 진행성 폐질환으로, COPD로 약칭합니다. 통역 시 '만성기관지염(viêm phế quản mãn tính)'과 '폐기종(khí phế thũng)'이 COPD의 주요 형태임을 설명해야 하며, 가장 중요한 것은 '금연(bỏ thuốc lá)'이 유일한 진행 억제 방법임을 강조하는 것입니다. 베트남 남성 환자의 흡연율이 높아 금연 저항이 심할 수 있으므로, '매일 1갑씩 40년 피우면 100% COPD'처럼 구체적 수치로 설명해야 합니다. 산소치료(điều trị oxy)가 필요한 단계를 사전에 안내하고, 호흡재활(phục hồi chức năng hô hấp)의 중요성도 전달해야 합니다.",
        "meaningVi": "Bệnh phổi tiến triển do hút thuốc lá lâu năm làm hỏng đường thở và phế nang, gây khó thở mạn tính. Viết tắt là COPD. Bao gồm viêm phế quản mãn tính (ho, đờm nhiều) và khí phế thũng (phổi phồng, khó thở). Cách duy nhất để ngăn bệnh tiến triển là BỎ THUỐC LÁ hoàn toàn. Giai đoạn nặng cần dùng oxy tại nhà. Thuốc chỉ giảm triệu chứng, không chữa khỏi. Hút thuốc 1 bao mỗi ngày trong 40 năm sẽ gần như chắc chắn bị COPD.",
        "context": "호흡기내과 진료, 만성 기침과 호흡곤란, 흡연력",
        "culturalNote": "한국과 베트남 모두 남성 흡연율이 높지만, 베트남에서는 '담배를 끊으면 살이 찐다', '스트레스가 풀린다' 등의 이유로 금연 저항이 더 강합니다. 통역 시 '담배를 계속 피우면 산소통을 메고 다녀야 한다'처럼 구체적 미래를 제시해야 효과적입니다. 한국에서는 COPD 환자에게 독감, 폐렴구균 백신을 적극 권장하지만 베트남 환자들은 '백신은 어린이나 맞는 것'으로 생각하는 경향이 있어 설명이 필요합니다. 또한 한국에서는 호흡재활 프로그램이 잘 되어 있으나 베트남 환자들은 생소할 수 있습니다.",
        "commonMistakes": [
            {
                "mistake": "Bệnh phổi mãn tính (만성 폐질환) → 너무 포괄적",
                "correction": "Bệnh phổi TẮC NGHẼN mãn tính (COPD)",
                "explanation": "'폐쇄성'이라는 핵심 개념이 빠지면 다른 만성 폐질환과 구분이 안 됩니다."
            },
            {
                "mistake": "담배를 줄이면 된다(Giảm thuốc lá là được)",
                "correction": "Phải BỎ HOÀN TOÀN, giảm không có tác dụng (완전 금연 필수, 감량은 무의미)",
                "explanation": "하루 5개비로 줄여도 COPD는 계속 진행됩니다. '완전 금연'만이 유일한 답임을 강조해야 합니다."
            },
            {
                "mistake": "Hen suyễn (천식) = COPD",
                "correction": "Hen suyễn là bệnh dị ứng, COPD do hút thuốc",
                "explanation": "천식은 알레르기 질환이고 가역적이지만, COPD는 비가역적이며 주로 흡연이 원인입니다. 치료도 다릅니다."
            },
            {
                "mistake": "Chỉ cần uống thuốc là khỏi (약만 먹으면 낫는다)",
                "correction": "Thuốc CHỈ GIẢM triệu chứng, KHÔNG chữa khỏi (약은 증상 완화뿐, 완치 불가)",
                "explanation": "COPD는 비가역적 질환입니다. 약은 증상을 관리할 뿐 폐 손상을 회복시키지 못함을 명확히 해야 합니다."
            }
        ],
        "examples": [
            {
                "ko": "폐기능 검사 결과 FEV1/FVC 비율이 0.65로 COPD로 진단됩니다.",
                "vi": "Kết quả đo chức năng hô hấp cho thấy tỷ lệ FEV1/FVC là 0.65, chẩn đoán COPD.",
                "situation": "formal"
            },
            {
                "ko": "40년간 하루 한 갑씩 피우셨다면 80갑년으로 중증 COPD 위험군입니다.",
                "vi": "Anh hút 1 bao mỗi ngày trong 40 năm tức là 80 pack-years, thuộc nhóm nguy cơ cao COPD nặng.",
                "situation": "formal"
            },
            {
                "ko": "COPD는 담배 안 끊으면 점점 나빠져서 나중엔 산소통 메고 다녀야 해요.",
                "vi": "COPD không bỏ thuốc thì ngày càng nặng, cuối cùng phải mang bình oxy đi khắp nơi đấy.",
                "situation": "onsite"
            }
        ],
        "relatedTerms": [
            "폐기종",
            "만성기관지염",
            "폐기능검사",
            "금연",
            "산소치료"
        ]
    },
    {
        "slug": "lao-phoi",
        "korean": "결핵",
        "vietnamese": "Lao phổi",
        "hanja": "結核",
        "hanjaReading": "結(맺을 결) + 核(씨 핵)",
        "pronunciation": "라오 포이",
        "meaningKo": "결핵균(Mycobacterium tuberculosis)에 의한 감염성 질환으로, 주로 폐를 침범하지만 다른 장기도 감염될 수 있습니다. 통역 시 가장 중요한 것은 '전염성'과 '치료 기간'입니다. 베트남은 결핵 유병률이 한국보다 높아 환자들이 질병에 대한 선입견을 가지고 있을 수 있습니다. 통역 시 '최소 6개월 치료'를 강조하고, 약을 임의로 중단하면 내성결핵(lao kháng thuốc)이 생긴다는 점을 명확히 해야 합니다. 가족 검진(khám sàng lọc gia đình)의 필요성을 설명하고, 치료 중 격리 기간(보통 2주)을 정확히 안내해야 합니다. 한국에서는 무료 치료와 생활비 지원이 있으나 베트남 환자들은 모를 수 있습니다.",
        "meaningVi": "Bệnh nhiễm trùng do vi khuẩn lao (Mycobacterium tuberculosis), chủ yếu tấn công phổi nhưng có thể lây sang các cơ quan khác. Triệu chứng: ho kéo dài hơn 2 tuần, ho ra máu, sốt nhẹ buổi chiều, đổ mồ hôi đêm, sút cân. Bệnh LÂY TRUYỀN qua đường hô hấp. Điều trị TỐI THIỂU 6 tháng, không được tự ý ngừng thuốc nếu không sẽ sinh ra lao kháng thuốc rất khó chữa. Ở Hàn Quốc, thuốc và chi phí sinh hoạt được hỗ trợ miễn phí.",
        "context": "만성 기침, 객혈, 체중 감소, 접촉자 검진",
        "culturalNote": "베트남에서는 결핵이 여전히 흔한 질환이라 환자들이 '흔한 병'으로 가볍게 여기는 경향이 있지만, 한국에서는 법정 감염병으로 엄격히 관리됩니다. 통역 시 '전염병으로 신고 의무가 있다'는 점을 설명해야 합니다. 베트남 환자들은 증상이 호전되면 약을 중단하는 경향이 강하므로, '6개월 완치까지 복용'을 반복해서 강조해야 합니다. 한국에서는 결핵 환자에게 생활비와 영양비를 지원하며, 가족 검진도 무료임을 안내하면 순응도가 높아집니다. 베트남에서는 결핵 환자가 사회적 낙인을 받는 경우가 있어 비밀 보장에 대한 안심을 주어야 합니다.",
        "commonMistakes": [
            {
                "mistake": "Ho lâu ngày (오래된 기침) = Lao phổi",
                "correction": "Ho lâu ngày CHỈ LÀ triệu chứng, cần xét nghiệm mới chẩn đoán lao",
                "explanation": "2주 이상 기침은 결핵 의심 증상이지만, 확진은 객담검사, X-ray 등으로 해야 합니다."
            },
            {
                "mistake": "Uống thuốc 2 tháng hết ho là được rồi (2개월 먹고 기침 멈추면 됐다)",
                "correction": "Phải uống thuốc ÍT NHẤT 6 tháng, dù hết triệu chứng (증상 없어도 최소 6개월 복용)",
                "explanation": "초기 2개월은 집중치료기이고, 이후 4개월은 유지치료입니다. 조기 중단하면 재발하고 내성이 생깁니다."
            },
            {
                "mistake": "Lây qua đồ dùng chung (공용 물건으로 전염)",
                "correction": "Lao phổi lây qua ĐƯỜNG HÔ HẤP, không lây qua đồ dùng (공기 전염, 물건 접촉으론 전염 안 됨)",
                "explanation": "결핵은 비말(기침, 재채기)로 전염되지 식기, 수건 등으로는 전염되지 않습니다. 과도한 공포를 줄여야 합니다."
            },
            {
                "mistake": "내성결핵을 '약이 안 듣는 감기'로 설명",
                "correction": "Lao kháng thuốc - bệnh rất nguy hiểm, khó chữa, tốn kém (내성결핵 - 매우 위험, 치료 어렵고 비용 많이 듦)",
                "explanation": "다제내성결핵은 치료 기간이 2년 이상이고 성공률도 낮습니다. 심각성을 정확히 전달해야 합니다."
            }
        ],
        "examples": [
            {
                "ko": "객담 검사에서 항산균 양성, PCR 검사에서 결핵균이 확인되었습니다.",
                "vi": "Xét nghiệm đờm dương tính với vi khuẩn kháng acid, và xét nghiệm PCR xác nhận vi khuẩn lao.",
                "situation": "formal"
            },
            {
                "ko": "결핵 치료는 4가지 약을 6개월간 복용하며, 처음 2주는 전염성이 있어 격리가 필요합니다.",
                "vi": "Điều trị lao là uống 4 loại thuốc trong 6 tháng, 2 tuần đầu có lây nhiễm nên cần cách ly.",
                "situation": "formal"
            },
            {
                "ko": "약 먹기 시작하면 2주 후엔 전염 안 돼요. 하지만 6개월은 꼭 다 드셔야 해요.",
                "vi": "Sau khi uống thuốc 2 tuần thì không lây nữa. Nhưng phải uống đủ 6 tháng mới được nhé.",
                "situation": "onsite"
            }
        ],
        "relatedTerms": [
            "항산균도말검사",
            "흉부X-ray",
            "잠복결핵",
            "다제내성결핵",
            "BCG백신"
        ]
    },
    {
        "slug": "nguong-tho-khi-ngu",
        "korean": "수면무호흡증",
        "vietnamese": "Ngưng thở khi ngủ",
        "hanja": "睡眠無呼吸症",
        "hanjaReading": "睡(잠잘 수) + 眠(잠잘 면) + 無(없을 무) + 呼(부를 호) + 吸(마실 흡) + 症(병 증)",
        "pronunciation": "응엉 토 키 응우",
        "meaningKo": "수면 중 상기도가 반복적으로 막혀 호흡이 멈추는 질환으로, 코골이, 주간 졸음, 집중력 저하가 주요 증상입니다. 통역 시 '폐쇄성(tắc nghẽn đường thở trên)'과 '중추성(não không gửi tín hiệu thở)'을 구분해야 하며, 대부분은 폐쇄성입니다. 수면다원검사(xét nghiệm đa ký giấc ngủ)를 통해 AHI(apnea-hypopnea index)를 측정하며, 시간당 무호흡 횟수로 중증도를 판단합니다. CPAP(máy thở áp lực dương liên tục)이 표준 치료임을 설명하고, 베트남 환자들은 '기계를 쓰고 자는 것'에 거부감을 보일 수 있어 합병증(고혈압, 심근경색, 뇌졸중)을 강조해야 합니다. 체중 감량과 금주가 중요함도 전달해야 합니다.",
        "meaningVi": "Bệnh đường thở trên bị tắc nghẽn nhiều lần khi ngủ, khiến ngừng thở tạm thời. Triệu chứng: ngáy to, ngưng thở khi ngủ (người nhà phát hiện), buồn ngủ ban ngày, đau đầu buổi sáng, giảm trí nhớ. Chẩn đoán bằng xét nghiệm đa ký giấc ngủ (ngủ qua đêm ở bệnh viện với thiết bị ghi nhận). Điều trị chủ yếu bằng máy CPAP (máy thở áp lực dương) đeo khi ngủ. Nếu không điều trị, nguy cơ cao huyết áp, nhồi máu cơ tim, đột quỵ. Giảm cân và kiêng rượu rất quan trọng.",
        "context": "코골이 호소, 주간 졸음, 고혈압 동반",
        "culturalNote": "한국에서는 수면무호흡증을 심혈관 질환의 위험인자로 적극 치료하지만, 베트남에서는 '코골이는 잘 자는 것'으로 오해하는 경향이 있습니다. 통역 시 '코골이는 건강한 수면이 아니다'라는 인식 전환이 필요합니다. CPAP 기계가 베트남에서는 비용 부담이 크고 낯설어 환자들이 거부하는 경우가 많으므로, '매일 밤 사용해야 효과가 있다'는 점과 함께 '뇌졸중 예방'이라는 장기적 이득을 강조해야 합니다. 한국에서는 수면다원검사가 보험 적용되지만 베트남 환자들은 비용을 문의할 수 있습니다.",
        "commonMistakes": [
            {
                "mistake": "Ngáy to (코골이) = Ngưng thở khi ngủ",
                "correction": "Ngáy to CHỈ LÀ triệu chứng, ngưng thở khi ngủ là BỆNH",
                "explanation": "모든 코골이 환자가 수면무호흡증은 아닙니다. 무호흡이 동반되는지 검사해야 합니다."
            },
            {
                "mistake": "Ngủ nhiều nhưng vẫn mệt (많이 자도 피곤) → 게으름으로 오해",
                "correction": "Buồn ngủ ban ngày mặc dù ngủ đủ giờ là DẤU HIỆU bệnh ngưng thở khi ngủ",
                "explanation": "주간 졸음은 의지의 문제가 아니라 야간 수면의 질이 나쁘기 때문입니다. 질환임을 명확히 해야 합니다."
            },
            {
                "mistake": "Máy CPAP chỉ cần dùng khi mệt (CPAP는 피곤할 때만 사용)",
                "correction": "Phải dùng MỖI ĐÊM, không phải lúc cần (매일 밤 사용 필수)",
                "explanation": "CPAP는 증상이 있을 때만 쓰는 것이 아니라 수면 중 기도를 지속적으로 열어주기 위해 매일 사용해야 합니다."
            },
            {
                "mistake": "술 마시면 잠 잘 온다 (술이 수면에 도움)",
                "correction": "Rượu LÀM NẶNG THÊM bệnh ngưng thở khi ngủ (알코올은 수면무호흡을 악화)",
                "explanation": "알코올은 상기도 근육을 이완시켜 무호흡을 더 심하게 만듭니다. 금주를 권장해야 합니다."
            }
        ],
        "examples": [
            {
                "ko": "수면다원검사 결과 시간당 무호흡 횟수가 35회로 중증 수면무호흡증입니다.",
                "vi": "Kết quả xét nghiệm đa ký giấc ngủ cho thấy ngưng thở 35 lần mỗi giờ, là ngưng thở khi ngủ mức độ nặng.",
                "situation": "formal"
            },
            {
                "ko": "CPAP 치료를 시작하면 코골이가 없어지고 낮에 졸음도 줄어듭니다.",
                "vi": "Sau khi bắt đầu điều trị CPAP, sẽ hết ngáy và giảm buồn ngủ ban ngày.",
                "situation": "formal"
            },
            {
                "ko": "체중 10kg만 빠져도 무호흡이 많이 좋아질 수 있어요. 술도 끊으셔야 해요.",
                "vi": "Chỉ cần giảm 10kg cũng cải thiện nhiều rồi. Và phải bỏ rượu nữa nhé.",
                "situation": "onsite"
            }
        ],
        "relatedTerms": [
            "코골이",
            "수면다원검사",
            "CPAP",
            "주간졸음",
            "폐쇄성수면무호흡"
        ]
    }
]

def main():
    print("🏥 의료 용어 추가 스크립트 v5-t 시작")
    print(f"📂 파일 경로: {file_path}")

    # 기존 파일 읽기
    try:
        with open(file_path, 'r', encoding='utf-8') as f:
            data = json.load(f)
        print(f"✅ 기존 파일 로드 완료 (현재 {len(data)}개 용어)")
    except FileNotFoundError:
        print("❌ 파일을 찾을 수 없습니다.")
        return
    except json.JSONDecodeError as e:
        print(f"❌ JSON 파싱 오류: {e}")
        return

    # 기존 slug 목록
    existing_slugs = {term['slug'] for term in data}
    print(f"📋 기존 slug 개수: {len(existing_slugs)}")

    # 중복 필터링
    new_terms_to_add = [term for term in new_terms if term['slug'] not in existing_slugs]
    duplicate_count = len(new_terms) - len(new_terms_to_add)

    if duplicate_count > 0:
        print(f"⚠️  중복 제거: {duplicate_count}개")
        duplicate_slugs = [term['slug'] for term in new_terms if term['slug'] in existing_slugs]
        print(f"   중복 slug: {', '.join(duplicate_slugs)}")

    if not new_terms_to_add:
        print("ℹ️  추가할 새 용어가 없습니다 (모두 중복)")
        return

    # 용어 추가
    data.extend(new_terms_to_add)
    print(f"✅ {len(new_terms_to_add)}개 용어 추가 완료")

    # 파일 저장
    try:
        with open(file_path, 'w', encoding='utf-8') as f:
            json.dump(data, f, ensure_ascii=False, indent=2)
        print(f"💾 파일 저장 완료 (총 {len(data)}개 용어)")
        print("\n📊 추가된 용어:")
        for term in new_terms_to_add:
            print(f"   • {term['korean']} ({term['vietnamese']}) - {term['slug']}")
    except Exception as e:
        print(f"❌ 파일 저장 오류: {e}")
        return

    print("\n🎉 스크립트 실행 완료!")

if __name__ == "__main__":
    main()
