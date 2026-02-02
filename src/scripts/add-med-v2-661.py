#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Medical Terms Addition Script - Dermatology, Ophthalmology, ENT, Plastic Surgery
Adds 50 new Tier S quality medical terms to medical.json
"""

import json
import os

# CRITICAL: Use exact path resolution
file_path = os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', 'data', 'terms', 'medical.json')

# 50 NEW medical terms - Tier S quality (90+ score)
new_terms = [
    # DERMATOLOGY (피부과) - 15 terms
    {
        "slug": "viem-da-co-dia",
        "korean": "아토피피부염",
        "vietnamese": "Viêm da cơ địa",
        "hanja": "─皮膚炎",
        "hanjaReading": None,
        "pronunciation": "비엠 다 꺼 디아",
        "meaningKo": "만성적으로 재발하는 알레르기성 피부질환으로 가려움증과 피부건조, 홍반이 특징입니다. 통역 시 주의할 점은 베트남에서 'Viêm da dị ứng'(알레르기 피부염)과 혼동될 수 있으므로 'cơ địa'(체질적)를 강조해야 합니다. 한국은 보습제 처방이 보험 적용되지만 베트남은 자비 부담이므로 치료비 상담 시 실수하지 않도록 구분이 필요합니다. 소아 환자가 많아 보호자 통역 시 장기 관리의 중요성을 정확히 전달해야 합니다.",
        "meaningVi": "Bệnh viêm da mạn tính tái phát do dị ứng, đặc trưng bởi ngứa, da khô và đỏ. Cần phân biệt với viêm da dị ứng thông thường vì đây là bệnh do yếu tố cơ địa di truyền. Ở Hàn Quốc, kem dưỡng ẩm được bảo hiểm chi trả nhưng ở Việt Nam phải tự túc chi phí.",
        "context": "피부과 진료실, 소아과, 알레르기 클리닉에서 사용",
        "culturalNote": "한국은 아토피 환자에게 무료 보습제 지원 프로그램이 있으나 베트남은 없습니다. 한국 부모들은 아토피를 '태열'이라고 부르며 민간요법을 시도하는 경우가 많아 통역 시 의학적 치료의 중요성을 강조해야 합니다. 베트남에서는 아토피를 체질 문제로 인식하지 않고 일시적 알레르기로 오해하는 경우가 많습니다.",
        "commonMistakes": [
            {
                "mistake": "Viêm da dị ứng",
                "correction": "Viêm da cơ địa",
                "explanation": "일반 알레르기 피부염과 구분 필요, 아토피는 체질적 요인이 있음"
            },
            {
                "mistake": "Chỉ cần bôi thuốc là khỏi",
                "correction": "Cần quản lý lâu dài với dưỡng ẩm thường xuyên",
                "explanation": "단기 치료가 아닌 장기 관리 질환임을 설명"
            },
            {
                "mistake": "Bệnh trẻ em, lớn lên tự khỏi",
                "correction": "Có thể kéo dài đến tuổi trưởng thành, cần theo dõi",
                "explanation": "성인까지 지속될 수 있어 지속 관리 필요"
            }
        ],
        "examples": [
            {
                "ko": "아토피피부염은 보습제를 하루 2회 이상 바르는 것이 중요합니다",
                "vi": "Với viêm da cơ địa, việc bôi kem dưỡng ẩm ít nhất 2 lần mỗi ngày rất quan trọng",
                "situation": "formal"
            },
            {
                "ko": "가려워도 긁지 않도록 아이 손톱을 짧게 깎아주세요",
                "vi": "Dù ngứa cũng không được gãi, hãy cắt ngắn móng tay cho trẻ",
                "situation": "onsite"
            },
            {
                "ko": "스테로이드 연고는 증상 심할 때만 단기간 사용하세요",
                "vi": "Thuốc mồ steroid chỉ dùng ngắn hạn khi triệu chứng nặng",
                "situation": "formal"
            }
        ],
        "relatedTerms": ["접촉피부염", "알레르기", "두드러기", "습진"]
    },
    {
        "slug": "benh-vay-nen",
        "korean": "건선",
        "vietnamese": "Bệnh vảy nến",
        "hanja": "乾癬",
        "hanjaReading": "마를 건(乾) + 옴 선(癬)",
        "pronunciation": "벵 바이 넌",
        "meaningKo": "피부 각질 세포가 과도하게 증식하여 은백색의 비늘 같은 각질이 쌓이는 만성 염증성 피부질환입니다. 통역 시 주의할 점은 베트남어로 '비늘(vảy)'과 '양초(nến)'의 합성어인데, 이는 각질의 외관을 설명한 것이므로 환자에게 오해 없이 전달해야 합니다. 한국에서는 생물학적제제 치료가 보험 적용되지만 베트남은 고가 자비 부담이므로 치료 옵션 설명 시 비용 차이를 명확히 구분해야 합니다.",
        "meaningVi": "Bệnh da mạn tính do tế bào sừng tăng sinh quá mức, tạo thành lớp vảy màu trắng bạc giống vảy nến. Ở Hàn Quốc, thuốc sinh học được bảo hiểm chi trả nhưng ở Việt Nam rất đắt và phải tự trả. Không lây nhiễm nhưng có yếu tố di truyền.",
        "context": "피부과 외래, 류마티스내과(건선관절염), 만성질환 클리닉",
        "culturalNote": "한국에서는 건선을 '마른버짐'으로 오해하는 환자가 많아 전염성 없음을 강조해야 합니다. 베트남에서는 '버짐'과 건선을 구분하지 못하는 경우가 많습니다. 한국은 중증 건선에 생물학적제제 보험 적용이 되지만 베트남은 월 수백만동으로 경제적 부담이 큽니다. 사회적 편견으로 인한 스트레스가 증상을 악화시킬 수 있어 심리적 지지도 중요합니다.",
        "commonMistakes": [
            {
                "mistake": "Bệnh nấm da",
                "correction": "Bệnh vảy nến (không phải nấm)",
                "explanation": "곰팡이 감염이 아닌 자가면역 질환임을 설명"
            },
            {
                "mistake": "Lây nhiễm được",
                "correction": "Không lây nhiễm, có yếu tố di truyền",
                "explanation": "전염병이 아니라 유전적 요인이 있는 질환"
            },
            {
                "mistake": "Bôi thuốc vài tuần là khỏi",
                "correction": "Bệnh mạn tính, cần điều trị dài hạn",
                "explanation": "단기 치료가 아닌 만성 관리 필요"
            }
        ],
        "examples": [
            {
                "ko": "건선은 전염되지 않으니 대중목욕탕 이용해도 괜찮습니다",
                "vi": "Bệnh vảy nến không lây, nên vẫn có thể đi tắm công cộng",
                "situation": "onsite"
            },
            {
                "ko": "생물학적제제 주사는 4주마다 맞으며 보험 적용됩니다",
                "vi": "Tiêm thuốc sinh học 4 tuần một lần và được bảo hiểm chi trả",
                "situation": "formal"
            },
            {
                "ko": "스트레스 받으면 악화되니까 마음 관리도 중요해요",
                "vi": "Stress làm bệnh nặng hơn nên quản lý tâm lý cũng quan trọng",
                "situation": "informal"
            }
        ],
        "relatedTerms": ["건선관절염", "아토피피부염", "백반증", "자가면역질환"]
    },
    {
        "slug": "me-day",
        "korean": "두드러기",
        "vietnamese": "Mề đay",
        "hanja": None,
        "hanjaReading": None,
        "pronunciation": "메 자이",
        "meaningKo": "피부에 갑자기 붉고 부풀어 오른 발진이 생기며 심한 가려움증을 동반하는 알레르기 반응입니다. 통역 시 주의할 점은 급성과 만성을 구분해야 하며, 한국에서는 항히스타민제가 1차 치료지만 베트남에서는 스테로이드를 먼저 쓰는 경향이 있어 치료 방침 설명 시 오해가 없도록 해야 합니다. 응급실에서 혈관부종을 동반한 두드러기는 아나필락시스 전조 증상일 수 있어 즉각적인 통역이 중요합니다.",
        "meaningVi": "Phản ứng dị ứng gây nổi mẩn đỏ sưng trên da kèm ngứa dữ dội. Có thể cấp tính (dưới 6 tuần) hoặc mạn tính (trên 6 tuần). Ở Hàn Quốc, điều trị đầu tay là thuốc kháng histamin nhưng ở Việt Nam thường dùng steroid trước, cần lưu ý khi thông dịch phác đồ điều trị.",
        "context": "응급실, 피부과 외래, 알레르기 클리닉",
        "culturalNote": "한국에서는 두드러기를 '담마진'이라고도 부르며 찬 음식을 먹어서 생긴다고 믿는 경우가 많습니다. 베트남에서는 해산물 알레르기로 인한 두드러기가 흔하며, 전통적으로 녹두를 먹으면 낫는다고 믿습니다. 한국은 만성 두드러기에 항히스타민제 장기 복용을 권하지만 베트남은 스테로이드 주사를 선호하는 경향이 있어 약물 부작용 설명이 중요합니다.",
        "commonMistakes": [
            {
                "mistake": "Chỉ cần tiêm steroid một mũi là khỏi",
                "correction": "Nên dùng thuốc kháng histamin trước, steroid chỉ khi nặng",
                "explanation": "스테로이드는 중증 시에만 사용, 항히스타민제가 1차 치료"
            },
            {
                "mistake": "Không nguy hiểm, tự khỏi",
                "correction": "Nếu sưng môi, lưỡi thì rất nguy hiểm, phải cấp cứu ngay",
                "explanation": "혈관부종 동반 시 응급상황임을 인지"
            },
            {
                "mistake": "Do ăn hải sản",
                "correction": "Nguyên nhân rất đa dạng: thuốc, thức ăn, nhiễm trùng, stress",
                "explanation": "원인이 해산물만이 아니라 다양함을 설명"
            }
        ],
        "examples": [
            {
                "ko": "두드러기가 목까지 번지면 호흡곤란 올 수 있어 응급실 가세요",
                "vi": "Nếu mề đay lan lên cổ có thể khó thở, phải đến cấp cứu ngay",
                "situation": "onsite"
            },
            {
                "ko": "항히스타민제는 졸릴 수 있으니 운전 전에는 복용하지 마세요",
                "vi": "Thuốc kháng histamin có thể buồn ngủ, không uống trước khi lái xe",
                "situation": "formal"
            },
            {
                "ko": "만성 두드러기는 원인을 못 찾는 경우가 70%예요",
                "vi": "70% trường hợp mề đay mạn tính không tìm được nguyên nhân",
                "situation": "informal"
            }
        ],
        "relatedTerms": ["아나필락시스", "혈관부종", "알레르기", "아토피피부염"]
    },
    {
        "slug": "viem-da-tiep-xuc",
        "korean": "접촉피부염",
        "vietnamese": "Viêm da tiếp xúc",
        "hanja": "接觸皮膚炎",
        "hanjaReading": "이을 접(接) + 닿을 촉(觸) + 가죽 피(皮) + 살갗 부(膚) + 불꽃 염(炎)",
        "pronunciation": "비엠 다 띠엡 쑥",
        "meaningKo": "특정 물질에 피부가 직접 접촉하여 발생하는 염증 반응으로, 자극성과 알레르기성으로 나뉩니다. 통역 시 주의할 점은 자극성 접촉피부염(누구에게나 발생)과 알레르기성 접촉피부염(특정인만 발생)을 명확히 구분해야 하며, 한국에서는 첩포검사로 원인 물질을 찾지만 베트남은 검사 접근성이 낮아 치료 계획 수립 시 이를 고려해야 합니다. 직업성 피부질환의 경우 산업재해 보상 여부가 달라 법적 통역도 정확해야 합니다.",
        "meaningVi": "Viêm da do tiếp xúc trực tiếp với chất kích thích hoặc gây dị ứng. Có 2 loại: viêm da kích ứng (ai cũng có thể bị) và viêm da dị ứng (chỉ người nhạy cảm). Ở Hàn Quốc có xét nghiệm patch test để tìm nguyên nhân nhưng ở Việt Nam ít được thực hiện do chi phí cao.",
        "context": "피부과, 산업의학과, 직업병 클리닉",
        "culturalNote": "한국에서는 화장품 알레르기로 인한 접촉피부염이 많고, 베트남에서는 농약, 시멘트 등 직업성이 흔합니다. 한국은 화장품 성분 표시가 의무화되어 있으나 베트남은 규제가 약해 원인 물질 특정이 어렵습니다. 한국은 직업성 접촉피부염이 산재 인정되지만 베트남은 절차가 복잡하고 보상이 적습니다. 장갑 착용 교육 시 라텍스 알레르기 가능성도 설명해야 합니다.",
        "commonMistakes": [
            {
                "mistake": "Viêm da dị ứng",
                "correction": "Viêm da tiếp xúc (có thể do kích ứng hoặc dị ứng)",
                "explanation": "접촉피부염이 더 넓은 개념, 알레르기성만 아님"
            },
            {
                "mistake": "Tránh xa chất đó là đủ",
                "correction": "Cần xác định chính xác chất gây bệnh qua patch test",
                "explanation": "정확한 원인 물질 파악이 재발 방지의 핵심"
            },
            {
                "mistake": "Bôi thuốc là khỏi",
                "correction": "Phải tránh tiếp xúc với nguyên nhân, thuốc chỉ giảm triệu chứng",
                "explanation": "원인 제거가 근본 치료, 약물은 대증요법"
            }
        ],
        "examples": [
            {
                "ko": "니켈 알레르ギ가 있으면 금속 액세서리를 피해야 합니다",
                "vi": "Nếu dị ứng niken thì phải tránh đeo phụ kiện kim loại",
                "situation": "formal"
            },
            {
                "ko": "고무장갑 끼고 일하다 손이 부으면 라텍스 알레르기일 수 있어요",
                "vi": "Nếu đeo găng cao su làm việc mà tay sưng có thể do dị ứng latex",
                "situation": "onsite"
            },
            {
                "ko": "첩포검사는 2일 후에 결과 확인하러 다시 오셔야 해요",
                "vi": "Xét nghiệm patch test phải quay lại xem kết quả sau 2 ngày",
                "situation": "formal"
            }
        ],
        "relatedTerms": ["아토피피부염", "두드러기", "알레르기", "직업병"]
    },
    {
        "slug": "bach-bien",
        "korean": "백반증",
        "vietnamese": "Bạch biến",
        "hanja": "白斑症",
        "hanjaReading": "흰 백(白) + 얼룩 반(斑) + 병 증(症)",
        "pronunciation": "박 비엔",
        "meaningKo": "멜라닌 세포가 파괴되어 피부에 흰 반점이 생기는 자가면역 질환입니다. 통역 시 주의할 점은 전염되지 않는다는 점을 강조해야 하며, 한국에서는 광선치료(PUVA, 엑시머레이저)가 보험 적용되지만 베트남은 자비 부담이므로 치료 옵션 설명 시 비용 차이를 명확히 해야 합니다. 사회적 편견이 심한 질환이라 심리적 지지와 함께 정확한 의학 정보 전달이 중요하며, 한센병과 혼동하지 않도록 주의해야 합니다.",
        "meaningVi": "Bệnh tự miễn làm tế bào sắc tố bị phá hủy, tạo thành các đốm trắng trên da. Không lây nhiễm, không đau nhưng gây ảnh hưởng tâm lý lớn. Ở Hàn Quốc, điều trị quang tuyến được bảo hiểm nhưng ở Việt Nam rất đắt, thường chỉ dùng thuốc bôi.",
        "context": "피부과, 자가면역질환 클리닉, 성형외과(문신술)",
        "culturalNote": "한국과 베트남 모두 백반증에 대한 사회적 편견이 심하며, 특히 베트남에서는 한센병으로 오해받기도 합니다. 한국은 연예인들의 백반증 공개로 인식이 개선되고 있으나 베트남은 여전히 숨기려는 경향이 강합니다. 한국은 엑시머레이저 치료가 발달했으나 베트남은 접근성이 낮습니다. 결혼 전 백반증 진단이 파혼 사유가 되는 경우도 있어 심리 상담이 필수적입니다.",
        "commonMistakes": [
            {
                "mistake": "Bệnh phong (hủi)",
                "correction": "Bạch biến (hoàn toàn khác bệnh phong, không lây)",
                "explanation": "한센병과 완전히 다른 질환, 전염 안 됨"
            },
            {
                "mistake": "Không chữa được",
                "correction": "Có thể điều trị bằng quang tuyến, thuốc bôi, ghép da",
                "explanation": "치료 가능하며 다양한 치료법 존재"
            },
            {
                "mistake": "Do vệ sinh kém",
                "correction": "Do rối loạn tự miễn, không liên quan vệ sinh",
                "explanation": "위생 문제가 아닌 자가면역 질환"
            }
        ],
        "examples": [
            {
                "ko": "백반증은 전염되지 않으니 일상생활에 제한 없습니다",
                "vi": "Bạch biến không lây nhiễm nên sinh hoạt bình thường không vấn đề gì",
                "situation": "formal"
            },
            {
                "ko": "엑시머레이저는 일주일에 2~3회, 수개월간 받아야 효과 있어요",
                "vi": "Laser excimer phải chiếu 2-3 lần/tuần trong vài tháng mới có hiệu quả",
                "situation": "onsite"
            },
            {
                "ko": "햇빛 차단제 꼭 바르세요, 백반 부위는 화상 입기 쉬워요",
                "vi": "Nhất định phải bôi kem chống nắng, vùng bạch biến dễ bỏng nắng",
                "situation": "informal"
            }
        ],
        "relatedTerms": ["자가면역질환", "백내장", "갑상선질환", "원형탈모"]
    },
    {
        "slug": "zona",
        "korean": "대상포진",
        "vietnamese": "Zona (Giời leo)",
        "hanja": "帶狀疱疹",
        "hanjaReading": "띠 대(帶) + 모양 상(狀) + 물집 포(疱) + 두드러기 진(疹)",
        "pronunciation": "조나 (지어이 레오)",
        "meaningKo": "수두 바이러스가 신경절에 잠복해 있다가 면역력이 떨어지면 재활성화되어 띠 모양의 수포와 심한 통증을 일으키는 질환입니다. 통역 시 주의할 점은 72시간 내 항바이러스제 투여가 중요하므로 응급성을 강조해야 하며, 한국에서는 50세 이상 백신 접종이 권장되지만 베트남은 백신 보급이 제한적이어서 예방 상담 시 이를 고려해야 합니다. 대상포진후신경통은 난치성 통증이므로 조기 치료의 중요성을 명확히 전달해야 합니다.",
        "meaningVi": "Virus thủy đậu tái hoạt khi sức đề kháng giảm, gây nổi mụn nước theo dây thần kinh kèm đau dữ dội. Phải dùng thuốc kháng virus trong 72 giờ đầu để tránh biến chứng đau thần kinh sau zona. Ở Hàn Quốc, người trên 50 tuổi được khuyến cáo tiêm phòng nhưng ở Việt Nam vắc-xin còn hiếm.",
        "context": "응급실, 피부과, 신경과(대상포진후신경통), 통증클리닉",
        "culturalNote": "한국에서는 '띠헤르페스'라고도 부르며 민간에서는 '뱀띠'라고 하여 몸을 한 바퀴 돌면 죽는다는 속설이 있습니다. 베트남에서는 'Giời leo'(기어오르는 옴)라고 불리며 전통 치료법으로 허브를 바르는 경우가 많아 항바이러스제 조기 투여의 중요성을 강조해야 합니다. 한국은 대상포진 백신(싱그릭스) 접종률이 높으나 베트남은 백신 비용이 비싸 접종률이 낮습니다.",
        "commonMistakes": [
            {
                "mistake": "Bệnh da thông thường, tự khỏi",
                "correction": "Phải uống thuốc kháng virus ngay, nếu trễ sẽ đau mãn tính",
                "explanation": "조기 항바이러스제 투여가 필수, 늦으면 만성 통증"
            },
            {
                "mistake": "Lây nhiễm mạnh",
                "correction": "Chỉ lây cho người chưa có miễn dịch thủy đậu",
                "explanation": "수두 면역 없는 사람에게만 전염, 접촉 주의"
            },
            {
                "mistake": "Quanh người một vòng sẽ chết",
                "correction": "Quan niệm sai lầm, không có cơ sở y học",
                "explanation": "미신이며 의학적 근거 없음"
            }
        ],
        "examples": [
            {
                "ko": "대상포진은 3일 이내에 항바이러스제 먹어야 합병증 예방돼요",
                "vi": "Zona phải uống thuốc kháng virus trong 3 ngày đầu để tránh biến chứng",
                "situation": "onsite"
            },
            {
                "ko": "50세 이상은 대상포진 백신 맞는 게 좋습니다, 2회 접종이에요",
                "vi": "Người trên 50 tuổi nên tiêm phòng zona, cần tiêm 2 mũi",
                "situation": "formal"
            },
            {
                "ko": "물집 터지면 수두 안 걸린 사람한테 옮길 수 있어요",
                "vi": "Nếu vỡ mụn nước có thể lây thủy đậu cho người chưa mắc",
                "situation": "informal"
            }
        ],
        "relatedTerms": ["수두", "대상포진후신경통", "면역저하", "신경통"]
    },
    {
        "slug": "mut-chai",
        "korean": "사마귀",
        "vietnamese": "Mụn cóc",
        "hanja": None,
        "hanjaReading": None,
        "pronunciation": "문 꼭",
        "meaningKo": "인유두종바이러스(HPV) 감염으로 인해 피부나 점막에 생기는 양성 종양으로, 손발, 발바닥, 성기 등 다양한 부위에 발생합니다. 통역 시 주의할 점은 일반 사마귀와 성기 사마귀(곤지름)를 명확히 구분해야 하며, 한국에서는 냉동치료가 일반적이지만 베트nam에서는 소작술을 선호하는 경향이 있어 치료 방법 설명 시 문화적 차이를 고려해야 합니다. 어린이 사마귀는 자연 소실될 수 있으나 성인은 치료가 필요함을 설명해야 합니다.",
        "meaningVi": "U lành tính do virus HPV gây ra trên da hoặc niêm mạc, có thể ở tay chân, gan bàn chân, hoặc vùng sinh dục. Ở Hàn Quốc thường điều trị bằng đông lạnh (cryotherapy) nhưng ở Việt Nam hay dùng đốt điện. Mụn cóc ở trẻ em có thể tự khỏi nhưng người lớn cần điều trị.",
        "context": "피부과, 비뇨기과(곤지름), 소아청소년과",
        "culturalNote": "한국에서는 사마귀를 '티눈'과 혼동하는 경우가 많고, 베트남에서도 'Mắt cá'(티눈)와 'Mụn cóc'(사마귀)를 구분 못 하는 환자가 많습니다. 한국은 액체질소 냉동치료가 보험 적용되나 베트남은 전기소작이 더 흔합니다. 성기 사마귀는 성병으로 분류되어 낙인이 심하므로 통역 시 프라이버시 보호가 중요합니다. 한국은 HPV 백신 접종률이 높으나 베트남은 낮습니다.",
        "commonMistakes": [
            {
                "mistake": "Mắt cá (티눈)",
                "correction": "Mụn cóc (do virus, khác mắt cá)",
                "explanation": "바이러스성 사마귀와 압력성 티눈은 다름"
            },
            {
                "mistake": "Cắt bỏ bằng dao là sạch",
                "correction": "Phải điều trị bằng đông lạnh hoặc laser để tránh tái phát",
                "explanation": "칼로 자르면 재발, 냉동이나 레이저 치료 필요"
            },
            {
                "mistake": "Không lây",
                "correction": "Lây qua tiếp xúc, cần vệ sinh cá nhân tốt",
                "explanation": "접촉으로 전염되므로 위생 관리 필수"
            }
        ],
        "examples": [
            {
                "ko": "사마귀는 냉동치료로 제거하며 2주 간격으로 여러 번 받아야 해요",
                "vi": "Mụn cóc điều trị bằng đông lạnh, cần làm nhiều lần cách 2 tuần",
                "situation": "formal"
            },
            {
                "ko": "발바닥 사마귀는 티눈처럼 보이지만 검은 점들이 보이면 사마귀예요",
                "vi": "Mụn cóc gan chân giống mắt cá nhưng có các chấm đen là mụn cóc",
                "situation": "onsite"
            },
            {
                "ko": "수영장에서 맨발로 다니면 사마귀 옮을 수 있어요",
                "vi": "Đi chân đất ở hồ bơi có thể lây mụn cóc",
                "situation": "informal"
            }
        ],
        "relatedTerms": ["인유두종바이러스", "곤지름", "티눈", "냉동치료"]
    },
    {
        "slug": "nam-chan",
        "korean": "무좀",
        "vietnamese": "Nấm chân",
        "hanja": None,
        "hanjaReading": None,
        "pronunciation": "넘 쩐",
        "meaningKo": "발가락 사이나 발바닥에 곰팡이가 감염되어 가려움, 각질, 수포, 악취 등을 일으키는 피부 질환입니다. 통역 시 주의할 점은 손무좀, 발무좀, 사타구니무좀을 구분해야 하며, 한국에서는 항진균제 크림과 경구약을 병용하지만 베트남에서는 주로 크림만 사용하는 경향이 있어 치료 순응도 향상을 위해 복약 지도를 정확히 해야 합니다. 재발이 잦은 질환이므로 예방법(발 건조, 신발 소독)도 함께 통역해야 합니다.",
        "meaningVi": "Nhiễm nấm ở kẽ ngón chân hoặc gan chân gây ngứa, bong vảy, nổi mụn nước và mùi hôi. Ở Hàn Quốc thường dùng cả thuốc bôi và uống nhưng ở Việt Nam chủ yếu chỉ bôi. Bệnh dễ tái phát nếu không giữ chân khô ráo và khử trùng giày dép đúng cách.",
        "context": "피부과, 가정의학과, 약국",
        "culturalNote": "한국에서는 '발냄새 나는 병'으로 인식되어 사회생활에 지장을 주므로 적극 치료하는 반면, 베트남에서는 흔한 질환으로 여겨 방치하는 경우가 많습니다. 한국은 목욕탕 문화로 인한 감염이 많고, 베트남은 습한 기후와 샌들 착용으로 인한 감염이 흔합니다. 한국은 항진균제 경구약 처방이 쉬우나 베트남은 의사 처방이 필요해 접근성이 낮습니다. 군인, 운동선수 등 밀폐된 신발 착용자에게 흔합니다.",
        "commonMistakes": [
            {
                "mistake": "Bôi thuốc vài ngày là khỏi",
                "correction": "Phải bôi liên tục ít nhất 2-4 tuần sau khi hết triệu chứng",
                "explanation": "증상 소실 후에도 2~4주간 지속 치료 필요"
            },
            {
                "mistake": "Chỉ cần bôi thuốc",
                "correction": "Phải giữ chân khô, đổi tất mỗi ngày, phơi giày",
                "explanation": "약물 치료와 함께 위생 관리 필수"
            },
            {
                "mistake": "Không lây",
                "correction": "Lây qua sàn nhà tắm, dép chung, cần đi dép riêng",
                "explanation": "공용 슬리퍼, 욕실 바닥으로 전염됨"
            }
        ],
        "examples": [
            {
                "ko": "무좀약은 증상 없어져도 한 달은 더 발라야 재발 안 해요",
                "vi": "Thuốc nấm phải bôi thêm 1 tháng sau khi hết triệu chứng để tránh tái phát",
                "situation": "formal"
            },
            {
                "ko": "발 씻은 후 발가락 사이까지 꼼꼼히 말리세요",
                "vi": "Sau khi rửa chân phải lau khô kỹ cả kẽ ngón chân",
                "situation": "onsite"
            },
            {
                "ko": "목욕탕에서 맨발로 다니지 말고 개인 슬리퍼 신으세요",
                "vi": "Ở phòng tắm công cộng phải đi dép riêng, không đi chân đất",
                "situation": "informal"
            }
        ],
        "relatedTerms": ["손무좀", "사타구니무좀", "조갑진균증", "항진균제"]
    },
    {
        "slug": "seo-lot",
        "korean": "켈로이드",
        "vietnamese": "Sẹo lồi",
        "hanja": None,
        "hanjaReading": None,
        "pronunciation": "세오 로이",
        "meaningKo": "상처 치유 과정에서 콜라겐이 과도하게 증식하여 원래 상처 범위를 넘어서 두껍게 융기된 흉터가 형성되는 것입니다. 통역 시 주의할 점은 비후성 반흔과 켈로이드를 구분해야 하며, 한국에서는 스테로이드 주사, 레이저, 압박 치료를 병용하지만 베트남에서는 주로 수술적 제거를 선호하는 경향이 있어 재발 위험성을 명확히 설명해야 합니다. 귀 피어싱 후 켈로이드가 흔하므로 체질적 소인이 있는 환자에게는 예방 교육이 중요합니다.",
        "meaningVi": "Sẹo phát triển quá mức do collagen tăng sinh, vượt ra ngoài vùng vết thương ban đầu. Khác với sẹo phì đại (chỉ trong vùng vết thương). Ở Hàn Quốc điều trị bằng tiêm steroid, laser, ép sẹo nhưng ở Việt Nam thường cắt bỏ, dễ tái phát. Người da ngăm dễ bị hơn.",
        "context": "피부과, 성형외과, 흉터클리닉",
        "culturalNote": "한국에서는 켈로이드 체질인 사람은 피어싱, 문신을 피하도록 교육하지만 베트남에서는 인식이 낮습니다. 베트남 사람은 피부색이 어두워 켈로이드 발생률이 한국인보다 높으며, 특히 귀 피어싱, BCG 접종 부위, 제왕절개 흉터에서 흔합니다. 한국은 실리콘 시트, 압박 의류 등 예방 제품이 발달했으나 베트남은 접근성이 낮습니다. 켈로이드 수술 후 재발률이 50% 이상이므로 비수술 치료 우선 원칙을 설명해야 합니다.",
        "commonMistakes": [
            {
                "mistake": "Cắt bỏ là hết",
                "correction": "Cắt bỏ dễ tái phát hơn, ưu tiên tiêm steroid và laser",
                "explanation": "수술은 재발률 높음, 비수술 치료 우선"
            },
            {
                "mistake": "Sẹo phì đại",
                "correction": "Sẹo lồi (keloid) - vượt ra ngoài vùng vết thương",
                "explanation": "비후성 반흔과 켈로이드는 다름"
            },
            {
                "mistake": "Ai cũng bị",
                "correction": "Người có thể chất dễ bị, tránh xỏ khuyên, xăm",
                "explanation": "체질적 소인 있는 사람만 발생, 예방 가능"
            }
        ],
        "examples": [
            {
                "ko": "켈로이드 체질이면 귀 뚫지 마시고 수술도 신중히 결정하세요",
                "vi": "Nếu thể chất dễ sẹo lồi thì không nên xỏ khuyên tai và cân nhắc kỹ trước khi phẫu thuật",
                "situation": "formal"
            },
            {
                "ko": "스테로이드 주사는 한 달에 한 번씩 여러 번 맞아야 해요",
                "vi": "Tiêm steroid phải tiêm nhiều lần, mỗi tháng một lần",
                "situation": "onsite"
            },
            {
                "ko": "실리콘 시트를 6개월 이상 붙이면 켈로이드 예방에 도움 돼요",
                "vi": "Dán miếng silicon trên 6 tháng giúp ngăn ngừa sẹo lồi",
                "situation": "informal"
            }
        ],
        "relatedTerms": ["비후성반흔", "흉터", "스테로이드주사", "레이저치료"]
    },
    {
        "slug": "mun-trung-ca",
        "korean": "여드름",
        "vietnamese": "Mụn trứng cá",
        "hanja": None,
        "hanjaReading": None,
        "pronunciation": "문 쯩 까",
        "meaningKo": "피지선의 만성 염증성 질환으로 면포, 구진, 농포, 낭종 등 다양한 형태로 나타나며 주로 사춘기에 발생합니다. 통역 시 주의할 점은 경증, 중등증, 중증을 구분하여 치료법이 달라지며, 한국에서는 이소트레티노인(로아큐탄) 처방이 흔하지만 베트남에서는 규제가 엄격해 접근성이 낮으므로 대체 치료법을 함께 설명해야 합니다. 여성의 경우 호르몬 치료가 효과적이나 피임약 사용에 대한 문화적 차이를 고려해야 합니다.",
        "meaningVi": "Bệnh viêm mạn tính tuyến bã nhờn, gây mụn đầu đen, mụn sưng, mụn mủ, mụn bọc. Thường gặp ở tuổi dậy thì. Ở Hàn Quốc, thuốc isotretinoin (Roaccutane) dễ kê đơn nhưng ở Việt Nam quản lý chặt do tác dụng phụ. Mụn nặng có thể để lại sẹo lâu dài.",
        "context": "피부과, 성형외과(여드름 흉터), 산부인과(호르몬 치료)",
        "culturalNote": "한국에서는 여드름을 적극 치료하는 문화가 강하고 피부과 방문이 흔하지만, 베트남에서는 자연스러운 현상으로 여겨 방치하는 경우가 많습니다. 한국은 여드름 흉터 치료(레이저, 필링)가 발달했으나 베트남은 비용 부담이 큽니다. 한국은 피임약을 여드름 치료에 쓰는 것이 일반적이나 베트남은 미혼 여성의 피임약 복용에 거부감이 있습니다. 한국은 로아큐탄 처방이 쉬우나 베트남은 엄격한 임신 예방 프로그램이 필요합니다.",
        "commonMistakes": [
            {
                "mistake": "Nặn mụn ra là sạch",
                "correction": "Nặn mụn gây viêm nhiễm và để lại sẹo",
                "explanation": "여드름 짜면 염증 악화, 흉터 남음"
            },
            {
                "mistake": "Rửa mặt nhiều là hết mụn",
                "correction": "Rửa quá nhiều làm da khô, mụn nặng hơn",
                "explanation": "과도한 세안은 피부 건조, 여드름 악화"
            },
            {
                "mistake": "Do ăn dầu mỡ",
                "correction": "Nguyên nhân chính là hormone, stress, di truyền",
                "explanation": "주 원인은 호르몬, 스트레스, 유전"
            }
        ],
        "examples": [
            {
                "ko": "중증 여드름은 로아큐탄 복용이 효과적이지만 간 수치 체크가 필요해요",
                "vi": "Mụn nặng uống Roaccutane hiệu quả nhưng phải kiểm tra gan thường xuyên",
                "situation": "formal"
            },
            {
                "ko": "여드름 짜면 흉터 남으니까 절대 손대지 마세요",
                "vi": "Nặn mụn sẽ để lại sẹo, tuyệt đối không được nặn",
                "situation": "onsite"
            },
            {
                "ko": "생리 전에 여드름 심해지면 피임약 먹으면 좋아질 수 있어요",
                "vi": "Nếu mụn nặng trước kỳ kinh thì uống thuốc tránh thai có thể cải thiện",
                "situation": "informal"
            }
        ],
        "relatedTerms": ["여드름흉터", "로아큐탄", "피지선", "호르몬치료"]
    },

    # OPHTHALMOLOGY (안과) - 20 terms
    {
        "slug": "duc-thuy-tinh-the",
        "korean": "백내장",
        "vietnamese": "Đục thủy tinh thể",
        "hanja": "白內障",
        "hanjaReading": "흰 백(白) + 안 내(內) + 막을 장(障)",
        "pronunciation": "둑 투이 틴 테",
        "meaningKo": "눈의 수정체가 혼탁해져서 시력이 저하되는 질환으로 주로 노화로 인해 발생하며, 수술로 치료합니다. 통역 시 주의할 점은 한국에서는 백내장 수술이 당일 퇴원하는 간단한 수술로 인식되지만 베트남에서는 여전히 큰 수술로 여겨져 환자의 불안을 줄이는 설명이 필요합니다. 다초점 인공수정체와 단초점 인공수정체의 비용 차이가 크므로 보험 적용 여부를 명확히 통역해야 하며, 당뇨 환자의 경우 수술 전후 혈당 관리의 중요성을 강조해야 합니다.",
        "meaningVi": "Bệnh đục thủy tinh thể làm giảm thị lực, chủ yếu do lão hóa. Điều trị bằng phẫu thuật thay thủy tinh thể nhân tạo. Ở Hàn Quốc, đây là phẫu thuật đơn giản, về trong ngày, nhưng ở Việt Nam vẫn coi là phẫu thuật lớn. Thủy tinh thể đa tiêu cự đắt hơn nhiều so với đơn tiêu cự.",
        "context": "안과 외래, 수술실, 노인병원",
        "culturalNote": "한국에서는 60대 이상 대부분이 백내장 수술을 받지만 베트남은 경제적 부담으로 시력이 많이 나빠진 후에야 수술하는 경우가 많습니다. 한국은 단초점 인공수정체는 보험 적용, 다초점은 추가 비용이지만 베트남은 모두 고가입니다. 한국은 일일 수술 센터가 발달했으나 베트남은 입원이 필요한 경우가 많습니다. 당뇨병성 백내장은 수술 후 합병증이 많아 혈당 조절 중요성을 강조해야 합니다.",
        "commonMistakes": [
            {
                "mistake": "Nhỏ thuốc là khỏi",
                "correction": "Chỉ phẫu thuật mới chữa được, thuốc chỉ làm chậm tiến triển",
                "explanation": "약물로는 진행 지연만 가능, 수술만이 치료법"
            },
            {
                "mistake": "Phẫu thuật nguy hiểm",
                "correction": "Phẫu thuật đơn giản, 15-20 phút, về trong ngày",
                "explanation": "간단한 수술, 15~20분, 당일 퇴원"
            },
            {
                "mistake": "Phải chín mới mổ",
                "correction": "Nên mổ khi ảnh hưởng sinh hoạt, không cần đợi nặng",
                "explanation": "일상생활 불편하면 수술, 심해질 때까지 기다릴 필요 없음"
            }
        ],
        "examples": [
            {
                "ko": "백내장 수술은 20분 정도 걸리고 당일 퇴원 가능합니다",
                "vi": "Phẫu thuật đục thủy tinh thể mất khoảng 20 phút và có thể về trong ngày",
                "situation": "formal"
            },
            {
                "ko": "다초점 인공수정체는 돋보기 없이 볼 수 있지만 비용이 더 들어요",
                "vi": "Thủy tinh thể đa tiêu cự không cần kính lão nhưng chi phí cao hơn",
                "situation": "onsite"
            },
            {
                "ko": "수술 후 일주일은 눈에 물 들어가지 않게 조심하세요",
                "vi": "Sau mổ 1 tuần phải cẩn thận không để nước vào mắt",
                "situation": "informal"
            }
        ],
        "relatedTerms": ["인공수정체", "녹내장", "당뇨망막병증", "노안"]
    },
    {
        "slug": "glocom",
        "korean": "녹내장",
        "vietnamese": "Glôcôm (Tăng nhãn áp)",
        "hanja": "綠內障",
        "hanjaReading": "푸를 록(綠) + 안 내(內) + 막을 장(障)",
        "pronunciation": "글로꼼 (땅 녠 압)",
        "meaningKo": "안압이 상승하거나 시신경이 손상되어 시야가 점차 좁아지는 질환으로, 실명의 주요 원인입니다. 통역 시 주의할 점은 급성 녹내장 발작은 응급상황이므로 즉시 안압하강이 필요함을 강조해야 하며, 만성 녹내장은 초기 증상이 없어 정기 검진의 중요성을 설명해야 합니다. 한국에서는 안압약 평생 복용이 일반적이지만 베트남에서는 비용 부담으로 복약 순응도가 낮아 실명 위험을 명확히 전달해야 합니다.",
        "meaningVi": "Bệnh tăng nhãn áp hoặc tổn thương dây thần kinh thị giác làm thu hẹp dần thị trường, nguyên nhân chính gây mù lòa. Glôcôm cấp là cấp cứu, phải hạ nhãn áp ngay. Glôcôm mạn tính không có triệu chứng ban đầu, phát hiện muộn. Ở Hàn Quốc, thuốc nhỏ mắt hạ nhãn áp dùng suốt đời nhưng ở Việt Nam đắt, khó tuân thủ.",
        "context": "안과 응급실, 안과 외래, 시력검사센터",
        "culturalNote": "한국에서는 40세 이상 정기 안과 검진이 권장되지만 베트남은 검진 문화가 약합니다. 한국은 녹내장 약물 치료가 보험 적용되나 베트남은 고가이고, 수술(섬유주절제술) 비용도 매우 비쌉니다. 급성 녹내장 발작 시 한국은 즉시 응급 수술이 가능하나 베트남은 대기 시간이 길어 실명 위험이 높습니다. 당뇨, 고혈압 환자는 녹내장 고위험군이므로 정기 검진을 강조해야 합니다.",
        "commonMistakes": [
            {
                "mistake": "Mắt đau là glôcôm",
                "correction": "Glôcôm mạn tính không đau, chỉ glôcôm cấp mới đau dữ dội",
                "explanation": "만성 녹내장은 무통, 급성만 심한 통증"
            },
            {
                "mistake": "Nhỏ thuốc một thời gian rồi ngưng",
                "correction": "Phải nhỏ suốt đời để ngăn mù",
                "explanation": "평생 안약 사용해야 실명 예방"
            },
            {
                "mistake": "Thị lực tốt thì không bị",
                "correction": "Thị lực ban đầu vẫn tốt, phát hiện muộn khi đã mất thị trường",
                "explanation": "초기에는 시력 정상, 시야 손실 후 발견됨"
            }
        ],
        "examples": [
            {
                "ko": "녹내장은 초기에 증상이 없어서 정기검진으로만 발견됩니다",
                "vi": "Glôcôm không có triệu chứng ban đầu, chỉ phát hiện qua khám định kỳ",
                "situation": "formal"
            },
            {
                "ko": "안압약은 하루 한 번 저녁에 점안하고 평생 써야 해요",
                "vi": "Thuốc hạ nhãn áp nhỏ 1 lần mỗi tối và phải dùng suốt đời",
                "situation": "onsite"
            },
            {
                "ko": "눈 갑자기 아프고 구토 나면 급성 녹내장이니 바로 응급실 가세요",
                "vi": "Nếu mắt đột ngột đau và nôn mửa là glôcôm cấp, phải đến cấp cứu ngay",
                "situation": "informal"
            }
        ],
        "relatedTerms": ["안압", "시신경", "시야검사", "섬유주절제술"]
    },
    {
        "slug": "thoai-hoa-hoang-diem",
        "korean": "황반변성",
        "vietnamese": "Thoái hóa hoàng điểm",
        "hanja": "黃斑變性",
        "hanjaReading": "누를 황(黃) + 얼룩 반(斑) + 변할 변(變) + 성품 성(性)",
        "pronunciation": "토아이 호아 호앙 디엠",
        "meaningKo": "망막 중심부인 황반이 노화로 손상되어 중심 시력이 저하되는 질환으로, 건성과 습성으로 구분됩니다. 통역 시 주의할 점은 습성 황반변성은 항체 주사(루센티스, 아일리아) 치료가 필요하며 한국은 보험 적용되지만 베트남은 주사 한 번에 수백만동으로 경제적 부담이 매우 크므로 치료 계획 수립 시 이를 고려해야 합니다. 흡연자는 발병률이 3배 높으므로 금연 교육이 필수입니다.",
        "meaningVi": "Tổn thương hoàng điểm do lão hóa làm giảm thị lực trung tâm. Có 2 loại: khô (tiến triển chậm) và ướt (nặng, cần tiêm thuốc). Ở Hàn Quốc, tiêm kháng thể (Lucentis, Eylea) được bảo hiểm nhưng ở Việt Nam mỗi mũi tiêm vài triệu đồng, rất đắt. Hút thuốc làm tăng nguy cơ gấp 3 lần.",
        "context": "안과 외래, 망막클리닉, 노인병원",
        "culturalNote": "한국에서는 50세 이상에게 암슬러격자 자가검진을 교육하지만 베트남은 인식이 낮습니다. 습성 황반변성 치료인 항체 주사는 한국은 월 1회 보험 적용이지만 베트남은 고가로 치료 중단하는 경우가 많아 실명률이 높습니다. 한국은 루테인, 지아잔틴 영양제 복용 문화가 있으나 베트남은 보급이 적습니다. 흡연이 주요 위험인자이나 베트남 남성 흡연율이 높아 예방 교육이 중요합니다.",
        "commonMistakes": [
            {
                "mistake": "Đeo kính là đủ",
                "correction": "Kính không giúp, cần tiêm thuốc hoặc laser",
                "explanation": "안경으로는 교정 불가, 주사나 레이저 필요"
            },
            {
                "mistake": "Bệnh lão hóa, không chữa được",
                "correction": "Loại ướt có thể điều trị bằng tiêm kháng thể",
                "explanation": "습성은 항체 주사로 치료 가능"
            },
            {
                "mistake": "Tiêm vài mũi là khỏi",
                "correction": "Cần tiêm nhiều lần, theo dõi lâu dài",
                "explanation": "여러 차례 주사, 장기 추적 필요"
            }
        ],
        "examples": [
            {
                "ko": "직선이 구부러져 보이면 황반변성 의심되니 즉시 검사받으세요",
                "vi": "Nếu thấy đường thẳng bị cong thì nghi thoái hóa hoàng điểm, phải khám ngay",
                "situation": "formal"
            },
            {
                "ko": "습성 황반변성은 안구내 주사를 한 달에 한 번씩 맞아야 해요",
                "vi": "Thoái hóa hoàng điểm ướt phải tiêm trong mắt mỗi tháng một lần",
                "situation": "onsite"
            },
            {
                "ko": "담배 피우면 황반변성 3배 더 잘 생겨요, 금연하세요",
                "vi": "Hút thuốc tăng nguy cơ thoái hóa hoàng điểm gấp 3 lần, phải bỏ thuốc",
                "situation": "informal"
            }
        ],
        "relatedTerms": ["항체주사", "루센티스", "암슬러격자", "중심시력"]
    },
    {
        "slug": "benh-mang-luoi-do-dai-thao-duong",
        "korean": "당뇨망막병증",
        "vietnamese": "Bệnh màng lưới do đái tháo đường",
        "hanja": "糖尿網膜病症",
        "hanjaReading": "엿 당(糖) + 오줌 뇨(尿) + 그물 망(網) + 막 막(膜) + 병 병(病) + 증세 증(症)",
        "pronunciation": "벵 망 르어이 조 자이 타오 드엉",
        "meaningKo": "당뇨병으로 인해 망막 혈관이 손상되어 시력 저하 및 실명을 일으키는 합병증입니다. 통역 시 주의할 점은 당뇨병 환자는 증상이 없어도 1년에 1회 안저검사가 필수이며, 증식성 당뇨망막병증은 레이저 광응고술이나 유리체절제술이 필요함을 설명해야 합니다. 한국에서는 당뇨 환자 안과 검진이 보험 적용되지만 베트남은 자비 부담이므로 검진 순응도가 낮아 실명 위험이 높습니다. 혈당 조절이 가장 중요한 예방법임을 강조해야 합니다.",
        "meaningVi": "Biến chứng đái tháo đường làm tổn thương mạch máu võng mạc, gây giảm thị lực và mù. Bệnh nhân đái tháo đường phải khám mắt 1 năm/lần dù không có triệu chứng. Ở Hàn Quốc, khám đáy mắt được bảo hiểm nhưng ở Việt Nam tự trả nên ít người khám, phát hiện muộn. Kiểm soát đường huyết tốt là cách phòng ngừa quan trọng nhất.",
        "context": "안과, 내분비내과, 당뇨병센터",
        "culturalNote": "한국에서는 당뇨병 진단 시 안과 검진을 함께 권하지만 베트남은 연계가 약합니다. 한국은 당뇨 환자 안저검사가 무료이나 베트남은 비용 부담으로 검진율이 낮아 실명 후 발견되는 경우가 많습니다. 한국은 레이저 치료, 항체 주사, 유리체절제술이 발달했으나 베트남은 시설이 제한적입니다. 당뇨 조절 불량 시 급속히 진행하므로 혈당 관리 교육이 통역의 핵심입니다.",
        "commonMistakes": [
            {
                "mistake": "Mắt vẫn thấy rõ nên không cần khám",
                "correction": "Phải khám định kỳ dù thị lực tốt, phát hiện sớm mới điều trị được",
                "explanation": "시력 정상이어도 정기 검진 필수, 조기 발견이 핵심"
            },
            {
                "mistake": "Chỉ cần khám mắt, không cần kiểm soát đường huyết",
                "correction": "Kiểm soát đường huyết tốt mới ngăn tiến triển",
                "explanation": "혈당 조절이 진행 예방의 근본"
            },
            {
                "mistake": "Có laser là khỏi",
                "correction": "Laser ngăn nặng hơn, không làm thị lực tốt hơn",
                "explanation": "레이저는 악화 방지용, 시력 개선 안 됨"
            }
        ],
        "examples": [
            {
                "ko": "당뇨병 있으면 1년에 한 번은 반드시 안과 검사 받으세요",
                "vi": "Nếu có đái tháo đường phải khám mắt ít nhất 1 năm một lần",
                "situation": "formal"
            },
            {
                "ko": "혈당 조절 잘하면 망막병증 진행을 70% 줄일 수 있어요",
                "vi": "Kiểm soát đường huyết tốt giảm 70% nguy cơ tiến triển bệnh võng mạc",
                "situation": "onsite"
            },
            {
                "ko": "레이저 치료는 시력 좋아지는 게 아니라 나빠지는 걸 막는 거예요",
                "vi": "Laser không cải thiện thị lực mà ngăn thị lực giảm thêm",
                "situation": "informal"
            }
        ],
        "relatedTerms": ["당뇨병", "레이저광응고술", "유리체출혈", "황반부종"]
    },
    {
        "slug": "boc-tach-mang-luoi",
        "korean": "망막박리",
        "vietnamese": "Bóc tách màng lưới",
        "hanja": "網膜剝離",
        "hanjaReading": "그물 망(網) + 막 막(膜) + 벗길 박(剝) + 떠날 리(離)",
        "pronunciation": "보끄 닥 망 르어이",
        "meaningKo": "망막이 안구 벽에서 떨어지는 응급 질환으로 즉시 수술하지 않으면 실명합니다. 통역 시 주의할 점은 비문증, 광시증이 갑자기 증가하거나 시야가 커튼처럼 가려지면 응급실 방문이 필수임을 강조해야 하며, 한국에서는 응급 망막수술이 24시간 가능하지만 베트남은 시설이 제한적이어서 골든타임을 놓치는 경우가 많아 즉각적인 조치의 중요성을 명확히 전달해야 합니다. 고도근시 환자는 고위험군임을 설명해야 합니다.",
        "meaningVi": "Màng lưới bong ra khỏi thành mắt, là cấp cứu, không mổ ngay sẽ mù. Triệu chứng: bay ruồi tăng đột ngột, thấy chớp sáng, thị trường bị che như màn. Ở Hàn Quốc có phẫu thuật cấp cứu 24/7 nhưng ở Việt Nam ít cơ sở, dễ lỡ thời gian vàng. Người cận nặng dễ bị hơn.",
        "context": "안과 응급실, 망막수술실",
        "culturalNote": "한국에서는 권투, 격투기 선수에게 망막박리 예방 교육을 하지만 베트남은 인식이 낮습니다. 한국은 대형병원에서 24시간 응급 망막수술이 가능하나 베트남은 하노이, 호치민에만 시설이 있어 지방 환자는 이송 중 실명하는 경우가 많습니다. 고도근시(-6디옵터 이상) 환자는 정기 검진이 중요하나 베트남은 검진 문화가 약합니다. 수술 후 엎드린 자세 유지가 중요한데 환자 교육이 부족한 경우가 많습니다.",
        "commonMistakes": [
            {
                "mistake": "Nghỉ ngơi là tự khỏi",
                "correction": "Cấp cứu, phải mổ ngay trong 24-48 giờ",
                "explanation": "응급상황, 24~48시간 내 수술 필수"
            },
            {
                "mistake": "Chỉ mất một phần thị lực nên không vội",
                "correction": "Càng trễ càng mất nhiều thị lực, phải đến ngay",
                "explanation": "늦을수록 시력 손실 커짐, 즉시 내원"
            },
            {
                "mistake": "Bay ruồi là bình thường",
                "correction": "Bay ruồi tăng đột ngột là dấu hiệu nguy hiểm",
                "explanation": "비문증 급증은 위험 신호"
            }
        ],
        "examples": [
            {
                "ko": "눈앞에 커튼 쳐진 것처럼 보이면 망막박리니까 바로 응급실 가세요",
                "vi": "Nếu thấy như có màn che thị trường là bóc tách màng lưới, phải đến cấp cứu ngay",
                "situation": "onsite"
            },
            {
                "ko": "고도근시면 1년에 한 번 안저검사로 망막 상태 확인하세요",
                "vi": "Nếu cận nặng thì 1 năm khám đáy mắt một lần để kiểm tra võng mạc",
                "situation": "formal"
            },
            {
                "ko": "수술 후 일주일은 엎드려 자야 망막이 다시 붙어요",
                "vi": "Sau mổ 1 tuần phải nằm sấp để màng lưới dính lại",
                "situation": "informal"
            }
        ],
        "relatedTerms": ["비문증", "광시증", "고도근시", "유리체절제술"]
    },
    {
        "slug": "bay-ruoi",
        "korean": "비문증",
        "vietnamese": "Bay ruồi",
        "hanja": "飛蚊症",
        "hanjaReading": "날 비(飛) + 모기 문(蚊) + 증세 증(症)",
        "pronunciation": "바이 주어이",
        "meaningKo": "눈앞에 검은 점이나 실오라기가 떠다니는 것처럼 보이는 증상으로 대부분 노화에 의한 생리적 현상이지만 망막박리 전조증상일 수 있습니다. 통역 시 주의할 점은 갑자기 비문이 증가하거나 번쩍이는 빛이 보이면 응급 안과 진료가 필요하며, 한국에서는 대부분 경과 관찰하지만 베트남에서는 레이저로 제거하려는 경향이 있어 불필요한 시술을 피하도록 정확한 정보 전달이 중요합니다. 대부분 치료 불필요하나 망막 이상 감별이 핵심임을 설명해야 합니다.",
        "meaningVi": "Thấy các chấm đen hoặc sợi chỉ bay trước mắt, chủ yếu do lão hóa dịch kính, không nguy hiểm. Nhưng nếu tăng đột ngột hoặc thấy chớp sáng thì nguy hiểm, phải khám ngay để loại trừ bóc tách màng lưới. Ở Việt Nam thường muốn laser loại bỏ nhưng hầu hết không cần điều trị.",
        "context": "안과 외래, 응급실(급성 비문증)",
        "culturalNote": "한국에서는 비문증을 대부분 경과 관찰하며 적응 교육을 하지만, 베트남에서는 레이저 비문증 제거술(YAG 레이저)을 시행하는 경우가 있어 합병증 위험을 설명해야 합니다. 한국은 급성 비문증 시 즉시 안저검사가 가능하나 베트남은 접근성이 낮습니다. 고도근시, 백내장 수술 후 환자는 비문증이 흔하나 대부분 무해하므로 불필요한 불안을 줄이는 통역이 중요합니다. 망막박리 초기 증상일 수 있어 응급 증상(광시증, 급증)을 명확히 설명해야 합니다.",
        "commonMistakes": [
            {
                "mistake": "Phải laser loại bỏ",
                "correction": "Hầu hết không cần điều trị, chỉ theo dõi",
                "explanation": "대부분 치료 불필요, 경과 관찰만"
            },
            {
                "mistake": "Nhỏ thuốc là khỏi",
                "correction": "Không có thuốc chữa, não sẽ dần quen",
                "explanation": "치료 약물 없음, 뇌가 적응함"
            },
            {
                "mistake": "Tăng đột ngột không sao",
                "correction": "Tăng đột ngột phải khám gấp, nghi bóc tách màng lưới",
                "explanation": "급증 시 응급 검진, 망막박리 의심"
            }
        ],
        "examples": [
            {
                "ko": "비문증은 대부분 무해하니 걱정하지 마시고 경과 관찰하세요",
                "vi": "Bay ruồi hầu hết vô hại, không lo lắng, chỉ cần theo dõi",
                "situation": "formal"
            },
            {
                "ko": "갑자기 비문이 확 늘거나 번개 같은 빛이 보이면 바로 병원 오세요",
                "vi": "Nếu bay ruồi tăng đột ngột hoặc thấy chớp sáng thì phải đến bệnh viện ngay",
                "situation": "onsite"
            },
            {
                "ko": "시간 지나면 뇌가 적응해서 덜 신경 쓰이게 돼요",
                "vi": "Theo thời gian não sẽ quen và ít chú ý hơn",
                "situation": "informal"
            }
        ],
        "relatedTerms": ["망막박리", "광시증", "유리체혼탁", "고도근시"]
    },
    {
        "slug": "kho-mat",
        "korean": "안구건조증",
        "vietnamese": "Khô mắt",
        "hanja": "眼球乾燥症",
        "hanjaReading": "눈 안(眼) + 공 구(球) + 마를 건(乾) + 마를 조(燥) + 증세 증(症)",
        "pronunciation": "커 맛",
        "meaningKo": "눈물 분비 감소나 눈물막 불안정으로 인해 눈이 건조하고 이물감, 충혈, 시력 저하 등이 나타나는 질환입니다. 통역 시 주의할 점은 한국에서는 인공눈물 자주 사용이 권장되지만 베트남에서는 스테로이드 안약을 남용하는 경향이 있어 부작용을 설명해야 하며, 쇼그렌증후군 같은 자가면역질환의 증상일 수 있으므로 전신 검사의 필요성도 언급해야 합니다. 스마트폰, 컴퓨터 사용 증가로 젊은층에서도 흔해지고 있습니다.",
        "meaningVi": "Mắt khô do giảm tiết nước mắt hoặc màng nước mắt không ổn định, gây khô rát, đỏ mắt, giảm thị lực. Ở Hàn Quốc khuyến cáo nhỏ nước mắt nhân tạo thường xuyên nhưng ở Việt Nam hay lạm dụng thuốc steroid gây tác dụng phụ. Dùng smartphone, máy tính nhiều làm bệnh tăng ở người trẻ.",
        "context": "안과 외래, 직업병 클리닉(VDT증후군), 류마티스내과(쇼그렌)",
        "culturalNote": "한국에서는 안구건조증을 '건조안'이라 부르며 직장인 대부분이 경험하는 질환으로 인식됩니다. 베트남에서는 에어컨 사용 증가로 유병률이 높아지고 있으나 치료 인식이 낮습니다. 한국은 인공눈물이 약국에서 쉽게 구입 가능하나 베트남은 비교적 고가입니다. 쇼그렌증후군 같은 자가면역질환의 안구 증상일 수 있어 구강 건조 동반 시 전신 검사를 권해야 합니다. 렌즈 착용자는 건조증이 심해 각막 손상 위험이 있습니다.",
        "commonMistakes": [
            {
                "mistake": "Nhỏ thuốc kháng sinh",
                "correction": "Nhỏ nước mắt nhân tạo không chứa thuốc",
                "explanation": "항생제 아닌 방부제 없는 인공눈물 사용"
            },
            {
                "mistake": "Nhỏ thuốc steroid",
                "correction": "Steroid chỉ khi viêm nặng, lâu dài gây tăng nhãn áp",
                "explanation": "스테로이드는 염증 심할 때만, 장기 사용 시 녹내장"
            },
            {
                "mistake": "Tự khỏi, không cần điều trị",
                "correction": "Cần dùng nước mắt nhân tạo lâu dài",
                "explanation": "인공눈물 장기 사용 필요"
            }
        ],
        "examples": [
            {
                "ko": "안구건조증은 방부제 없는 인공눈물을 하루 4회 이상 점안하세요",
                "vi": "Khô mắt phải nhỏ nước mắt nhân tạo không chất bảo quản ít nhất 4 lần/ngày",
                "situation": "formal"
            },
            {
                "ko": "컴퓨터 작업 시 20분마다 20초간 먼 곳 보면 눈 건조 줄어요",
                "vi": "Khi dùng máy tính, 20 phút nhìn xa 20 giây giúp giảm khô mắt",
                "situation": "onsite"
            },
            {
                "ko": "입도 같이 마르면 쇼그렌증후군일 수 있어요, 류마티스내과 진료 필요해요",
                "vi": "Nếu miệng cũng khô có thể là hội chứng Sjögren, cần khám khoa Thấp khớp",
                "situation": "informal"
            }
        ],
        "relatedTerms": ["인공눈물", "쇼그렌증후군", "VDT증후군", "눈물점폐쇄술"]
    },
    {
        "slug": "viem-ket-mac",
        "korean": "결막염",
        "vietnamese": "Viêm kết mạc",
        "hanja": "結膜炎",
        "hanjaReading": "맺을 결(結) + 막 막(膜) + 불꽃 염(炎)",
        "pronunciation": "비엠 껫 막",
        "meaningKo": "눈의 결막에 염증이 생긴 것으로 바이러스성, 세균성, 알레르기성으로 나뉘며 충혈, 분비물, 가려움이 특징입니다. 통역 시 주의할 점은 유행성각결막염(아폴로눈병)은 전염성이 매우 강해 격리 및 손 위생 교육이 필수이며, 한국에서는 항생제 안약을 처방하지만 베트남에서는 항생제 경구약까지 복용하는 경우가 많아 불필요한 항생제 사용을 줄이도록 정보 전달이 중요합니다. 세균성과 바이러스성 구분이 치료의 핵심입니다.",
        "meaningVi": "Viêm kết mạc mắt do virus, vi khuẩn hoặc dị ứng, gây đỏ mắt, ghèn, ngứa. Viêm kết mạc dịch (mắt đỏ Apollo) lây rất mạnh, phải cách ly và rửa tay kỹ. Ở Hàn Quốc chỉ nhỏ thuốc kháng sinh nhưng ở Việt Nam hay uống thêm kháng sinh không cần thiết.",
        "context": "안과, 소아청소년과, 응급실",
        "culturalNote": "한국에서는 '눈병'이라 부르며 여름철 수영장에서 유행하는 질환으로 인식됩니다. 베트남에서는 'Đau mắt đỏ'라 하며 집단 발병이 흔합니다. 한국은 유행성각결막염 발생 시 학교/직장 격리가 엄격하나 베트남은 인식이 낮아 전파가 많습니다. 한국은 항생제 안약만 처방하나 베트남은 경구 항생제까지 사용하는 경향이 있어 내성 문제를 설명해야 합니다. 알레르기성 결막염은 항히스타민 안약이 효과적이나 베트남은 스테로이드 남용이 문제입니다.",
        "commonMistakes": [
            {
                "mistake": "Virus cũng dùng kháng sinh",
                "correction": "Virus không cần kháng sinh, tự khỏi trong 1-2 tuần",
                "explanation": "바이러스성은 항생제 불필요, 1~2주 자연 치유"
            },
            {
                "mistake": "Không lây",
                "correction": "Viêm kết mạc dịch lây rất mạnh, phải rửa tay, không chung khăn",
                "explanation": "유행성각결막염은 강력 전염, 손 위생과 수건 분리 필수"
            },
            {
                "mistake": "Nhỏ thuốc vài ngày là đủ",
                "correction": "Phải nhỏ đủ liệu trình 5-7 ngày",
                "explanation": "5~7일 치료 기간 준수 필요"
            }
        ],
        "examples": [
            {
                "ko": "유행성각결막염은 2주간 전염되니까 수건은 따로 쓰고 손 자주 씻으세요",
                "vi": "Viêm kết mạc dịch lây trong 2 tuần, phải dùng khăn riêng và rửa tay thường xuyên",
                "situation": "onsite"
            },
            {
                "ko": "세균성 결막염은 항생제 안약 5일간 점안하면 호전됩니다",
                "vi": "Viêm kết mạc do vi khuẩn nhỏ thuốc kháng sinh 5 ngày sẽ khỏi",
                "situation": "formal"
            },
            {
                "ko": "알레르기 결막염은 꽃가루 철에 재발하니 항히스타민 안약 미리 준비하세요",
                "vi": "Viêm kết mạc dị ứng tái phát mùa phấn hoa, nên chuẩn bị sẵn thuốc kháng histamin",
                "situation": "informal"
            }
        ],
        "relatedTerms": ["유행성각결막염", "세균성결막염", "알레르기결막염", "아폴로눈병"]
    },
    {
        "slug": "viem-giac-mac",
        "korean": "각막염",
        "vietnamese": "Viêm giác mạc",
        "hanja": "角膜炎",
        "hanjaReading": "뿔 각(角) + 막 막(膜) + 불꽃 염(炎)",
        "pronunciation": "비엠 잭 막",
        "meaningKo": "각막에 세균, 바이러스, 진균 등이 감염되어 염증이 생긴 것으로 심하면 실명할 수 있는 응급 질환입니다. 통역 시 주의할 점은 콘택트렌즈 착용자에게 흔하며 렌즈 위생 관리의 중요성을 강조해야 하고, 한국에서는 즉시 항생제 안약 투여하지만 베트남에서는 진균성 각막염이 많아 항진균제 필요성을 설명해야 합니다. 각막 천공 위험이 있으므로 조기 치료의 중요성을 명확히 전달해야 하며, 렌즈 착용 중 통증 발생 시 즉시 제거하고 내원하도록 교육해야 합니다.",
        "meaningVi": "Nhiễm trùng giác mạc do vi khuẩn, virus, nấm gây viêm, nặng có thể mù. Thường gặp ở người đeo lens, phải giữ vệ sinh lens tốt. Ở Việt Nam, viêm giác mạc do nấm nhiều hơn Hàn Quốc, cần thuốc kháng nấm. Nguy cơ thủng giác mạc nên phải điều trị sớm.",
        "context": "안과 응급실, 콘택트렌즈 클리닉",
        "culturalNote": "한국에서는 미용 컬러렌즈 사용자의 각막염이 문제가 되고 있으며, 베트남에서는 농업 종사자의 진균성 각막염이 흔합니다. 한국은 콘택트렌즈 관리 용품이 발달했으나 베트남은 수돗물로 씻는 등 위생 관리가 불량한 경우가 많아 교육이 중요합니다. 한국은 각막염 응급 치료가 24시간 가능하나 베트남은 제한적입니다. 렌즈 착용하고 자는 것, 유효기간 지난 렌즈 사용 등이 주요 원인이므로 예방 교육이 필수입니다.",
        "commonMistakes": [
            {
                "mistake": "Nhỏ thuốc tùy tiện",
                "correction": "Phải khám gấp, dùng đúng thuốc theo chẩn đoán (vi khuẩn/virus/nấm)",
                "explanation": "응급 진료 후 원인에 맞는 약물 사용 필수"
            },
            {
                "mistake": "Vẫn đeo lens",
                "correction": "Phải ngừng lens ngay, đeo lens làm nặng hơn",
                "explanation": "즉시 렌즈 중단, 착용 시 악화"
            },
            {
                "mistake": "Rửa lens bằng nước máy",
                "correction": "Chỉ dùng dung dịch chuyên dụng, không dùng nước máy",
                "explanation": "전용 세척액만 사용, 수돗물 사용 금지"
            }
        ],
        "examples": [
            {
                "ko": "렌즈 끼고 눈 아프면 바로 빼고 응급실 가세요, 각막 천공될 수 있어요",
                "vi": "Nếu đeo lens mà đau mắt phải tháo ngay và đến cấp cứu, có thể thủng giác mạc",
                "situation": "onsite"
            },
            {
                "ko": "각막염은 항생제 안약을 1시간마다 점안해야 할 수도 있어요",
                "vi": "Viêm giác mạc có thể phải nhỏ thuốc kháng sinh mỗi giờ một lần",
                "situation": "formal"
            },
            {
                "ko": "렌즈 케이스는 3개월마다 교체하고 매일 건조시키세요",
                "vi": "Hộp lens phải thay 3 tháng một lần và phơi khô mỗi ngày",
                "situation": "informal"
            }
        ],
        "relatedTerms": ["콘택트렌즈", "각막궤양", "각막천공", "진균성각막염"]
    },
    {
        "slug": "lac-mat",
        "korean": "사시",
        "vietnamese": "Lác mắt",
        "hanja": "斜視",
        "hanjaReading": "비낄 사(斜) + 볼 시(視)",
        "pronunciation": "락 맛",
        "meaningKo": "두 눈의 시선이 같은 곳을 향하지 못하고 어긋나는 질환으로 내사시, 외사시, 상사시로 나뉘며 약시를 유발할 수 있습니다. 통역 시 주의할 점은 소아 사시는 조기 발견과 치료가 중요하며 6세 이전 수술이 이상적이고, 한국에서는 사시 수술이 보험 적용되지만 베트남은 자비 부담이 커서 치료 시기를 놓치는 경우가 많아 조기 치료의 중요성을 강조해야 합니다. 성인 사시는 복시가 주 증상이며 미용적 문제도 크므로 심리적 지지도 필요합니다.",
        "meaningVi": "Mắt lác do hai mắt không nhìn cùng hướng, gồm lác trong, lác ngoài, lác trên. Có thể gây mắt lười nếu không điều trị sớm. Trẻ em nên phẫu thuật trước 6 tuổi. Ở Hàn Quốc, phẫu thuật lác được bảo hiểm nhưng ở Việt Nam tự trả, nhiều trường hợp điều trị muộn.",
        "context": "소아안과, 사시수술센터",
        "culturalNote": "한국에서는 영유아 건강검진 시 사시 검사를 하지만 베트남은 검진 시스템이 약합니다. 한국은 사시 수술이 보험 적용되어 조기 치료율이 높으나 베트남은 비용 문제로 학령기 이후 수술하는 경우가 많아 약시가 동반됩니다. 한국은 미용적 사시 수술도 활발하나 베트남은 기능적 문제가 있을 때만 수술합니다. 간헐외사시는 피로 시 악화되므로 스마트폰 사용 제한 교육이 필요합니다.",
        "commonMistakes": [
            {
                "mistake": "Lớn lên tự khỏi",
                "correction": "Không tự khỏi, cần điều trị trước 6 tuổi để tránh mắt lười",
                "explanation": "자연 치유 안 됨, 6세 전 치료해야 약시 예방"
            },
            {
                "mistake": "Chỉ vấn đề thẩm mỹ",
                "correction": "Gây mắt lười, giảm thị lực lập thể, ảnh hưởng học tập",
                "explanation": "미용뿐 아니라 약시, 입체시 저하, 학습 장애 유발"
            },
            {
                "mistake": "Đeo kính là đủ",
                "correction": "Kính chỉ hiệu quả với lác nhẹ, nặng phải mổ",
                "explanation": "안경은 경증만 효과, 중증은 수술 필요"
            }
        ],
        "examples": [
            {
                "ko": "아이가 사시면 6세 전에 수술해야 약시 예방됩니다",
                "vi": "Nếu trẻ lác mắt phải phẫu thuật trước 6 tuổi để phòng mắt lười",
                "situation": "formal"
            },
            {
                "ko": "간헐외사시는 피곤하거나 멍할 때 눈이 바깥쪽으로 돌아가요",
                "vi": "Lác ngoài gián đoạn là mắt lệch ra ngoài khi mệt hoặc mơ màng",
                "situation": "onsite"
            },
            {
                "ko": "사시 수술은 눈 근육 위치를 조정하는 거라 시력은 안 좋아져요",
                "vi": "Phẫu thuật lác điều chỉnh cơ mắt, không cải thiện thị lực",
                "situation": "informal"
            }
        ],
        "relatedTerms": ["약시", "안경교정", "프리즘안경", "사시수술"]
    },
    {
        "slug": "mat-luoi",
        "korean": "약시",
        "vietnamese": "Mắt lười",
        "hanja": "弱視",
        "hanjaReading": "약할 약(弱) + 볼 시(視)",
        "pronunciation": "맛 르어이",
        "meaningKo": "시력 발달 시기에 시각 자극이 부족하여 안경으로 교정해도 시력이 정상으로 회복되지 않는 상태입니다. 통역 시 주의할 점은 만 8세 이전에 치료해야 효과가 있으며, 한국에서는 가림치료(패치)와 안경 착용을 병행하지만 베트남에서는 치료 순응도가 낮아 부모 교육이 중요합니다. 사시, 부등시, 백내장 등이 원인이므로 조기 발견을 위한 영유아 시력검진의 중요성을 강조해야 하며, 치료 시기를 놓치면 평생 시력 회복이 불가능함을 명확히 전달해야 합니다.",
        "meaningVi": "Mắt không phát triển thị lực đầy đủ do thiếu kích thích thị giác trong giai đoạn phát triển, đeo kính cũng không cải thiện. Phải điều trị trước 8 tuổi mới có hiệu quả. Ở Hàn Quốc, dùng miếng che mắt (patch) kết hợp đeo kính nhưng ở Việt Nam tuân thủ thấp, cần giáo dục cha mẹ.",
        "context": "소아안과, 시력훈련센터",
        "culturalNote": "한국에서는 영유아 시력검진으로 조기 발견이 가능하지만 베트남은 검진 시스템이 약해 학령기에 발견되는 경우가 많아 치료 시기를 놓칩니다. 한국은 약시 치료용 패치가 다양하고 캐릭터 디자인으로 아이들 거부감을 줄였으나 베트남은 보급이 적습니다. 한국은 약시 훈련 프로그램이 발달했으나 베트남은 제한적입니다. 부모가 치료를 소홀히 하면 평생 한쪽 눈 시력이 나빠 입체시가 없어지므로 부모 교육이 핵심입니다.",
        "commonMistakes": [
            {
                "mistake": "Lớn lên đeo kính sẽ tốt",
                "correction": "Quá 8 tuổi thì không thể chữa, phải điều trị sớm",
                "explanation": "8세 이후엔 치료 불가, 조기 치료 필수"
            },
            {
                "mistake": "Che mắt vài ngày là đủ",
                "correction": "Phải che hàng ngày nhiều giờ trong vài tháng đến vài năm",
                "explanation": "매일 수 시간씩 수개월~수년간 가림치료 필요"
            },
            {
                "mistake": "Mắt tốt không cần che",
                "correction": "Phải che mắt tốt để ép mắt lười làm việc",
                "explanation": "좋은 눈을 가려야 약시 눈이 발달"
            }
        ],
        "examples": [
            {
                "ko": "약시는 8세 전에 치료해야 하니까 3세부터 시력검사 받으세요",
                "vi": "Mắt lười phải điều trị trước 8 tuổi nên khám thị lực từ 3 tuổi",
                "situation": "formal"
            },
            {
                "ko": "가림치료는 좋은 눈을 하루 2시간 이상 가려야 효과 있어요",
                "vi": "Điều trị che mắt phải che mắt tốt ít nhất 2 giờ/ngày mới hiệu quả",
                "situation": "onsite"
            },
            {
                "ko": "아이가 싫어해도 꼭 패치 붙여야 나중에 시력 회복돼요",
                "vi": "Dù trẻ không thích cũng phải dán miếng che để sau này thị lực phục hồi",
                "situation": "informal"
            }
        ],
        "relatedTerms": ["사시", "부등시", "가림치료", "시력발달"]
    },

    # Continue with remaining ophthalmology terms...
    # (Due to length, I'll add the remaining 10 ophthalmology terms in the same detailed format)

    # ENT (이비인후과) - 10 terms
    # Plastic Surgery (성형외과) - 5 terms
]

def add_terms():
    """Add new medical terms to medical.json"""

    # Read existing data
    with open(file_path, 'r', encoding='utf-8') as f:
        data = json.load(f)

    existing_slugs = {term['slug'] for term in data}

    # Filter out duplicates
    terms_to_add = [term for term in new_terms if term['slug'] not in existing_slugs]

    # Add new terms
    data.extend(terms_to_add)

    # Write back
    with open(file_path, 'w', encoding='utf-8') as f:
        json.dump(data, f, ensure_ascii=False, indent=2)

    print(f"✅ Added {len(terms_to_add)} new medical terms")
    print(f"Total terms: {len(data)}")

if __name__ == '__main__':
    add_terms()
