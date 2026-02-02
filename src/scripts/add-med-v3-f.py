#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
의료(medical) 도메인 용어 추가 스크립트 - v3-f
20개 신규 용어 추가: 내분비/대사질환, 혈액질환, 종양치료, 신경계질환
"""

import json
import os

# 파일 경로 설정
file_path = os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', 'data', 'terms', 'medical.json')

# 기존 데이터 로드
with open(file_path, 'r', encoding='utf-8') as f:
    data = json.load(f)

# 기존 slug 추출
existing_slugs = {t['slug'] for t in data}

# 신규 용어 20개 (Tier S 기준)
new_terms = [
    {
        "slug": "cuong-giap",
        "korean": "갑상선기능항진증",
        "vietnamese": "Cường giáp",
        "hanja": "甲狀腺機能亢進症",
        "hanjaReading": "甲(갑 갑) + 狀(모양 상) + 腺(샘 선) + 機(틀 기) + 能(능할 능) + 亢(높을 항) + 進(나아갈 진) + 症(병 증)",
        "pronunciation": "갑상선기능항진쯩",
        "meaningKo": "갑상선에서 호르몬이 과다하게 분비되어 신진대사가 비정상적으로 빨라지는 질환입니다. 통역 시 주의할 점은 베트남어로 'cường giáp'이 일반적이지만 의료 문서에서는 'cường năng giáp'이라고도 쓰이므로 맥락을 구분해야 합니다. 환자가 '자꾸 떨린다', '살이 빠진다'고 호소하는 증상을 통역할 때 이 질환 가능성을 염두에 두세요. 베트남에서는 요오드 결핍보다는 그레이브스병(bệnh Basedow)이 주요 원인으로 인식됩니다.",
        "meaningVi": "Bệnh tuyến giáp tiết ra quá nhiều hormone, làm cho quá trình trao đổi chất trong cơ thể diễn ra nhanh bất thường. Triệu chứng bao gồm run tay, giảm cân nhanh, mất ngủ, mắt lồi. Nguyên nhân phổ biến nhất là bệnh Basedow (Graves). Cần điều trị bằng thuốc kháng giáp hoặc phẫu thuật.",
        "context": "내분비내과 진료, 대사질환 상담, 호르몬 검사 결과 설명 시",
        "culturalNote": "한국에서는 '갑상선 기능 항진'이라고 풀어서 설명하는 경우가 많지만, 베트남에서는 'cường giáp' 단일 용어로 환자들도 잘 이해합니다. 한국은 해조류 섭취가 많아 요오드 과다가 원인일 수 있지만, 베트남은 자가면역질환(bệnh Basedow)이 더 흔합니다. 베트남 환자들은 '안구돌출(lồi mắt)'을 매우 우려하므로 이 증상에 대한 설명이 중요합니다.",
        "commonMistakes": [
            {
                "mistake": "갑상선 과다증",
                "correction": "갑상선기능항진증",
                "explanation": "'과다증'은 비의학적 표현이며, 정확한 진단명은 '기능항진증'입니다."
            },
            {
                "mistake": "Tăng giáp",
                "correction": "Cường giáp",
                "explanation": "'Tăng'은 '증가'를 의미하지만, 의학 용어로는 'cường(항진)'이 정확합니다."
            },
            {
                "mistake": "Bệnh Basedow와 갑상선기능항진증을 동일시",
                "correction": "그레이브스병은 갑상선기능항진증의 원인 중 하나",
                "explanation": "그레이브스병은 자가면역질환으로 갑상선기능항진증을 일으키는 가장 흔한 원인이지만, 항진증의 원인은 다양합니다."
            }
        ],
        "examples": [
            {
                "ko": "갑상선기능항진증으로 인해 체중이 급격히 감소하고 심박수가 증가했습니다.",
                "vi": "Do cường giáp, cân nặng giảm nhanh và nhịp tim tăng cao.",
                "situation": "formal"
            },
            {
                "ko": "손이 자꾸 떨리고 잠도 못 자는데 갑상선 검사 좀 해봐야겠어요.",
                "vi": "Tay cứ run run và mất ngủ, em cần kiểm tra tuyến giáp.",
                "situation": "onsite"
            },
            {
                "ko": "항갑상선제를 복용하면서 정기적으로 혈액검사를 받아야 합니다.",
                "vi": "Phải uống thuốc kháng giáp và xét nghiệm máu định kỳ.",
                "situation": "formal"
            }
        ],
        "relatedTerms": ["갑상선", "갑상선기능저하증", "그레이브스병", "호르몬"]
    },
    {
        "slug": "suy-giap",
        "korean": "갑상선기능저하증",
        "vietnamese": "Suy giáp",
        "hanja": "甲狀腺機能低下症",
        "hanjaReading": "甲(갑 갑) + 狀(모양 상) + 腺(샘 선) + 機(틀 기) + 能(능할 능) + 低(낮을 저) + 下(아래 하) + 症(병 증)",
        "pronunciation": "갑상선기능저하쯩",
        "meaningKo": "갑상선에서 호르몬이 부족하게 분비되어 신진대사가 느려지는 질환입니다. 통역 시 환자가 '맨날 피곤하다', '추위를 많이 탄다', '살이 찐다'고 호소하는 경우 이 질환을 의심할 수 있습니다. 베트남어로는 'suy giáp'이 표준이며, 'giảm năng giáp'은 거의 쓰이지 않으니 주의하세요. 산후 갑상선염(viêm giáp sau sinh)으로 인한 일시적 저하증과 영구적 저하증을 구분해서 통역해야 합니다.",
        "meaningVi": "Bệnh tuyến giáp không tiết đủ hormone, làm chậm quá trình trao đổi chất. Triệu chứng gồm mệt mỏi, sợ lạnh, tăng cân, da khô, táo bón. Phổ biến ở phụ nữ trung niên. Cần điều trị bằng hormone thay thế (levothyroxin) suốt đời.",
        "context": "내분비내과 진료, 만성피로 상담, 임신 전후 검사",
        "culturalNote": "한국에서는 산후조리원에서 산후 갑상선 검사를 권장하지만, 베트남에서는 아직 일반화되지 않았습니다. 베트남 환자들은 '맥 없음', '무기력'을 나이 탓으로 돌리는 경향이 있어 진단이 늦어질 수 있습니다. 한국은 levothyroxin 100mcg 단위로 처방하지만, 베트남은 50mcg부터 시작하는 경우가 많습니다.",
        "commonMistakes": [
            {
                "mistake": "갑상선 감소증",
                "correction": "갑상선기능저하증",
                "explanation": "갑상선 자체가 줄어드는 것이 아니라 '기능이 저하'되는 것입니다."
            },
            {
                "mistake": "Giảm giáp",
                "correction": "Suy giáp",
                "explanation": "의학 용어로는 'suy(쇠약)'가 정확하며, 'giảm'은 일반적인 감소를 의미합니다."
            },
            {
                "mistake": "평생 약을 먹어야 한다를 'uống thuốc mãi mãi'로 통역",
                "correction": "'điều trị thay thế hormone suốt đời'",
                "explanation": "'mãi mãi'는 너무 구어적이고 부정적 뉘앙스가 있습니다."
            }
        ],
        "examples": [
            {
                "ko": "갑상선기능저하증 진단을 받고 레보티록신을 복용 중입니다.",
                "vi": "Được chẩn đoán suy giáp và đang uống levothyroxin.",
                "situation": "formal"
            },
            {
                "ko": "요즘 너무 피곤하고 추위를 많이 타서 갑상선 검사를 받아봤어요.",
                "vi": "Dạo này mệt quá và sợ lạnh nên đi xét nghiệm giáp.",
                "situation": "onsite"
            },
            {
                "ko": "TSH 수치가 높게 나와서 갑상선기능저하증으로 진단되었습니다.",
                "vi": "Chỉ số TSH cao nên được chẩn đoán suy giáp.",
                "situation": "formal"
            }
        ],
        "relatedTerms": ["갑상선", "갑상선기능항진증", "레보티록신", "TSH"]
    },
    {
        "slug": "ung-thu-tuyen-giap",
        "korean": "갑상선암",
        "vietnamese": "Ung thư tuyến giáp",
        "hanja": "甲狀腺癌",
        "hanjaReading": "甲(갑 갑) + 狀(모양 상) + 腺(샘 선) + 癌(암 암)",
        "pronunciation": "갑상선암",
        "meaningKo": "갑상선에 발생하는 악성 종양으로, 대부분 유두암(ung thư nhũ đầu)입니다. 통역 시 주의할 점은 갑상선암은 예후가 좋은 암으로 알려져 있지만, 환자에게는 '암'이라는 단어 자체가 큰 충격이므로 설명 방식을 신중히 해야 합니다. 베트남에서는 '갑상선 결절(u giáp)'과 '갑상선암'을 구분하지 못하는 환자가 많으니, 양성과 악성의 차이를 명확히 통역하세요. 수술 후 '목소리 변화(thay đổi giọng nói)' 가능성에 대한 설명이 필수입니다.",
        "meaningVi": "Khối u ác tính phát sinh từ tuyến giáp, phổ biến nhất là ung thư nhũ đầu (papillary). Tiên lượng thường tốt nếu phát hiện sớm. Điều trị chủ yếu bằng phẫu thuật cắt tuyến giáp, sau đó có thể dùng iod phóng xạ. Cần theo dõi lâu dài.",
        "context": "종양내과, 내분비외과, 암 진단 상담, 수술 전후 설명",
        "culturalNote": "한국은 건강검진에서 갑상선 초음파가 보편화되어 조기 발견율이 높지만, 베트남은 증상이 있을 때 발견되는 경우가 많습니다. 한국에서는 '착한 암'이라는 표현을 쓰기도 하지만, 베트남에서는 모든 암을 심각하게 받아들이므로 이런 표현은 피해야 합니다. 갑상선 전절제 후 평생 호르몬 복용에 대한 설명이 중요합니다.",
        "commonMistakes": [
            {
                "mistake": "갑상선 종양",
                "correction": "갑상선암 (악성인 경우)",
                "explanation": "종양은 양성과 악성을 모두 포함하므로, 암은 명확히 '암(ung thư)'으로 통역해야 합니다."
            },
            {
                "mistake": "U giáp",
                "correction": "Ung thư tuyến giáp (악성), U giáp (양성 포함)",
                "explanation": "'U'만으로는 악성인지 불명확하므로 반드시 'ung thư'를 붙여야 합니다."
            },
            {
                "mistake": "착한 암을 'ung thư hiền lành'로 통역",
                "correction": "'ung thư có tiên lượng tốt'",
                "explanation": "'hiền lành'은 양성을 의미하므로 오해의 소지가 있습니다."
            }
        ],
        "examples": [
            {
                "ko": "갑상선암으로 진단되어 갑상선 전절제술을 시행했습니다.",
                "vi": "Được chẩn đoán ung thư tuyến giáp và đã phẫu thuật cắt toàn bộ tuyến giáp.",
                "situation": "formal"
            },
            {
                "ko": "초음파에서 결절이 발견되어 조직검사를 했는데 암으로 나왔어요.",
                "vi": "Siêu âm phát hiện u nhỏ, sinh thiết ra là ung thư.",
                "situation": "onsite"
            },
            {
                "ko": "수술 후 방사성요오드 치료가 필요할 수 있습니다.",
                "vi": "Sau phẫu thuật có thể cần điều trị iod phóng xạ.",
                "situation": "formal"
            }
        ],
        "relatedTerms": ["갑상선", "갑상선결절", "갑상선절제술", "방사성요오드치료"]
    },
    {
        "slug": "loang-xuong",
        "korean": "골다공증",
        "vietnamese": "Loãng xương",
        "hanja": "骨多孔症",
        "hanjaReading": "骨(뼈 골) + 多(많을 다) + 孔(구멍 공) + 症(병 증)",
        "pronunciation": "골다공쯩",
        "meaningKo": "뼈의 밀도가 감소하고 구조가 약해져 골절 위험이 높아지는 질환입니다. 통역 시 주의할 점은 '골다공증'과 '골감소증(giảm khối lượng xương)'을 명확히 구분해야 하며, 베트남어로는 'loãng xương'이 표준입니다. 폐경기 여성에게 흔하므로 호르몬 요법에 대한 설명이 자주 필요합니다. 베트남에서는 칼슘 보충제를 과신하는 경향이 있어, 비타민D와 운동의 중요성도 함께 강조해야 합니다.",
        "meaningVi": "Bệnh xương bị mất mật độ, cấu trúc xốp, dễ gãy. Phổ biến ở phụ nữ sau mãn kinh và người cao tuổi. Nguyên nhân do thiếu canxi, vitamin D, nội tiết tố, ít vận động. Cần bổ sung dinh dưỡng, thuốc tăng mật độ xương, tập thể dục đều đặn.",
        "context": "정형외과, 내분비내과, 폐경 클리닉, 골절 예방 상담",
        "culturalNote": "한국은 골밀도 검사(DXA)가 건강검진에 포함되지만, 베트남은 골절 후에야 검사하는 경우가 많습니다. 한국에서는 골다공증 약물(비스포스포네이트)을 적극 처방하지만, 베트남에서는 칼슘제만 먹는 환자가 많습니다. '압박골절(gãy xương do loãng xương)'의 심각성에 대한 설명이 중요합니다.",
        "commonMistakes": [
            {
                "mistake": "뼈가 약한 병",
                "correction": "골다공증",
                "explanation": "정확한 의학 용어를 사용해야 합니다."
            },
            {
                "mistake": "Xương yếu",
                "correction": "Loãng xương",
                "explanation": "'yếu'는 일반적 표현이고, 'loãng'이 의학 용어입니다."
            },
            {
                "mistake": "칼슘만 먹으면 된다고 오역",
                "correction": "칼슘 + 비타민D + 운동 + 필요시 약물",
                "explanation": "골다공증은 복합적 치료가 필요하며, 칼슘만으로는 불충분합니다."
            }
        ],
        "examples": [
            {
                "ko": "골밀도 검사 결과 골다공증으로 진단되어 약물치료를 시작했습니다.",
                "vi": "Kết quả đo mật độ xương cho thấy loãng xương, bắt đầu điều trị bằng thuốc.",
                "situation": "formal"
            },
            {
                "ko": "폐경 후 골다공증 위험이 높아지니까 칼슘이랑 비타민D 드세요.",
                "vi": "Sau mãn kinh dễ loãng xương, chị nên uống canxi và vitamin D.",
                "situation": "onsite"
            },
            {
                "ko": "경미한 넘어짐에도 척추 압박골절이 발생했습니다.",
                "vi": "Chỉ ngã nhẹ mà bị gãy đốt sống do loãng xương.",
                "situation": "formal"
            }
        ],
        "relatedTerms": ["골절", "골밀도검사", "칼슘", "비타민D"]
    },
    {
        "slug": "benh-gut",
        "korean": "통풍",
        "vietnamese": "Bệnh gút",
        "hanja": "痛風",
        "hanjaReading": "痛(아플 통) + 風(바람 풍)",
        "pronunciation": "통풍",
        "meaningKo": "혈액 내 요산 수치가 높아져 관절에 요산 결정이 쌓여 심한 통증과 염증을 일으키는 질환입니다. 통역 시 주의할 점은 '통풍'과 '류마티스 관절염'을 혼동하는 환자가 많으므로 명확히 구분해야 합니다. 베트남어로는 'bệnh gút' 또는 'gút'이 표준이며, 'gout'라고 영어 발음 그대로 쓰기도 합니다. 육류와 주류 섭취 제한에 대한 식이 교육이 반드시 필요하며, 급성 발작 시 응급처치 방법도 설명해야 합니다.",
        "meaningVi": "Bệnh do axit uric cao trong máu, lắng đọng tinh thể ở khớp gây đau nhức dữ dội, sưng đỏ, thường ở ngón chân cái. Nguyên nhân từ ăn nhiều thịt đỏ, hải sản, uống rượu bia. Điều trị bằng thuốc hạ axit uric, chống viêm, kiêng ăn nghiêm ngặt.",
        "context": "류마티스내과, 응급실, 만성질환 관리, 식이 상담",
        "culturalNote": "한국에서는 '바람만 스쳐도 아프다'는 표현을 쓰지만, 베트nam에서는 이런 관용적 표현이 없어 직역하면 이해하지 못합니다. 베트남에서는 맥주(bia) 소비가 많아 통풍 환자가 증가 추세입니다. 한국은 콜히친을 급성기 치료로 쓰지만, 베트nam에서는 구하기 어려운 경우가 있어 NSAIDs가 주로 사용됩니다.",
        "commonMistakes": [
            {
                "mistake": "류마티스와 혼동",
                "correction": "통풍은 요산 결정에 의한 질환, 류마티스는 자가면역질환",
                "explanation": "발병 기전이 완전히 다른 질환입니다."
            },
            {
                "mistake": "Bệnh thấp khớp",
                "correction": "Bệnh gút",
                "explanation": "'Thấp khớp'은 류마티스를 의미하며, 통풍과는 다릅니다."
            },
            {
                "mistake": "술만 끊으면 된다고 오역",
                "correction": "주류 + 육류 + 해산물 제한, 약물치료 필수",
                "explanation": "식이요법만으로는 불충분하며, 약물치료가 반드시 필요합니다."
            }
        ],
        "examples": [
            {
                "ko": "엄지발가락 관절이 갑자기 빨갛게 부어오르고 통증이 심해서 통풍으로 진단받았습니다.",
                "vi": "Ngón chân cái bỗng sưng đỏ và đau dữ dội, được chẩn đoán bệnh gút.",
                "situation": "formal"
            },
            {
                "ko": "요산 수치가 높아서 고기랑 술을 줄이고 약을 먹어야 해요.",
                "vi": "Axit uric cao nên phải giảm thịt, rượu bia và uống thuốc.",
                "situation": "onsite"
            },
            {
                "ko": "통풍 발작 시 콜히친을 즉시 복용하세요.",
                "vi": "Khi gút cấp, uống ngay colchicine.",
                "situation": "formal"
            }
        ],
        "relatedTerms": ["요산", "관절염", "콜히친", "퓨린"]
    },
    {
        "slug": "dai-thao-duong-type-1",
        "korean": "제1형당뇨병",
        "vietnamese": "Đái tháo đường type 1",
        "hanja": "第一型糖尿病",
        "hanjaReading": "第(차례 제) + 一(한 일) + 型(형 형) + 糖(엿 당) + 尿(오줌 뇨) + 病(병 병)",
        "pronunciation": "제일형당뇨병",
        "meaningKo": "췌장의 베타세포가 파괴되어 인슐린을 전혀 분비하지 못하는 자가면역질환입니다. 통역 시 주의할 점은 제1형과 제2형 당뇨병의 차이를 명확히 설명해야 하며, 제1형은 평생 인슐린 주사가 필수라는 점을 강조해야 합니다. 베트남어로는 'đái tháo đường type 1' 또는 'típ 1'로 씁니다. 어린 나이에 발병하므로 '소아당뇨(đái tháo đường ở trẻ em)'라고도 하지만, 성인에서도 발병할 수 있으니 오해하지 않도록 주의하세요.",
        "meaningVi": "Bệnh tự miễn dịch phá hủy tế bào beta tuyến tụy, không tiết insulin. Thường khởi phát ở trẻ em, thanh thiếu niên. Bắt buộc phải tiêm insulin suốt đời, kiểm soát đường huyết chặt chẽ. Biến chứng nguy hiểm là nhiễm toan ceton (toan ceton).",
        "context": "소아내분비과, 당뇨클리닉, 인슐린 교육, 응급실(당뇨병케톤산증)",
        "culturalNote": "한국에서는 소아청소년 당뇨병 환자에게 연속혈당측정기(CGM)가 보험 적용되지만, 베트남은 아직 보급이 안 되어 자가혈당측정만 가능합니다. 베트남 가족들은 '인슐린=중증'으로 오해하는 경우가 많아 제1형과 제2형의 차이를 교육해야 합니다. 학교에서 인슐린 주사에 대한 편견이 있을 수 있습니다.",
        "commonMistakes": [
            {
                "mistake": "소아당뇨",
                "correction": "제1형당뇨병 (성인도 발병 가능)",
                "explanation": "'소아당뇨'는 나이를 기준으로 한 비의학적 용어입니다."
            },
            {
                "mistake": "Đái tháo đường ở trẻ em",
                "correction": "Đái tháo đường type 1",
                "explanation": "나이가 아니라 병태생리에 따른 분류가 정확합니다."
            },
            {
                "mistake": "살 빼면 나아진다고 오역",
                "correction": "제1형은 체중과 무관, 평생 인슐린 필수",
                "explanation": "제2형과 혼동한 오류입니다."
            }
        ],
        "examples": [
            {
                "ko": "제1형당뇨병으로 진단받아 하루 4회 인슐린 주사를 맞고 있습니다.",
                "vi": "Được chẩn đoán đái tháo đường type 1, tiêm insulin 4 lần mỗi ngày.",
                "situation": "formal"
            },
            {
                "ko": "애가 갑자기 살이 빠지고 물을 많이 마셔서 병원 갔더니 당뇨래요.",
                "vi": "Con gầy đột ngột và uống nước nhiều, đi khám thì bị đái tháo đường.",
                "situation": "onsite"
            },
            {
                "ko": "저혈당 증상이 나타나면 즉시 사탕이나 주스를 섭취하세요.",
                "vi": "Khi hạ đường huyết, ăn ngay kẹo hoặc uống nước ngọt.",
                "situation": "formal"
            }
        ],
        "relatedTerms": ["당뇨병", "인슐린", "혈당", "당뇨병케톤산증"]
    },
    {
        "slug": "benh-than-kinh-do-dai-thao-duong",
        "korean": "당뇨병성신경병증",
        "vietnamese": "Bệnh thần kinh do đái tháo đường",
        "hanja": "糖尿病性神經病症",
        "hanjaReading": "糖(엿 당) + 尿(오줌 뇨) + 病(병 병) + 性(성품 성) + 神(귀신 신) + 經(지날 경) + 病(병 병) + 症(병 증)",
        "pronunciation": "당뇨병성신경병쯩",
        "meaningKo": "당뇨병으로 인해 신경이 손상되어 통증, 저림, 감각 이상 등이 나타나는 합병증입니다. 통역 시 주의할 점은 말초신경병증(tổn thương thần kinh ngoại vi)이 가장 흔하며, '발이 저리다', '양말 신은 것 같다'는 환자의 호소를 정확히 전달해야 합니다. 베트남어로는 'bệnh thần kinh do đái tháo đường' 또는 'biến chứng thần kinh đái tháo đường'으로 씁니다. 당뇨발(chân đái tháo đường) 예방을 위한 발 관리 교육이 필수입니다.",
        "meaningVi": "Biến chứng đái tháo đường làm tổn thương dây thần kinh, gây tê, đau, mất cảm giác ở chân tay. Nguy hiểm nhất là loét chân khó lành, dễ nhiễm trùng, có thể phải cắt cụt. Cần kiểm soát đường huyết tốt, chăm sóc chân đúng cách, dùng thuốc giảm đau thần kinh.",
        "context": "당뇨클리닉, 신경과, 재활의학과, 당뇨발 클리닉",
        "culturalNote": "한국에서는 당뇨발 전문 클리닉이 많지만, 베트nam에서는 일반 정형외과에서 치료하는 경우가 많습니다. 베트남 환자들은 발 감각이 없어도 방치하다가 궤양(loét)이 생긴 후에야 병원을 찾는 경우가 많습니다. '발톱 깎기', '맨발로 걷지 않기' 같은 기본적인 발 관리 교육이 중요합니다.",
        "commonMistakes": [
            {
                "mistake": "당뇨 합병증",
                "correction": "당뇨병성신경병증 (구체적 합병증명)",
                "explanation": "합병증은 여러 종류가 있으므로 정확한 진단명을 써야 합니다."
            },
            {
                "mistake": "Biến chứng đái tháo đường (막연히)",
                "correction": "Bệnh thần kinh do đái tháo đường",
                "explanation": "어떤 합병증인지 명확히 해야 합니다."
            },
            {
                "mistake": "발 저림을 단순 혈액순환 문제로 오역",
                "correction": "신경 손상으로 인한 감각 이상",
                "explanation": "신경병증과 혈관 문제는 다릅니다."
            }
        ],
        "examples": [
            {
                "ko": "당뇨병성신경병증으로 발 감각이 둔해져서 다쳐도 모를 수 있습니다.",
                "vi": "Do bệnh thần kinh đái tháo đường, chân mất cảm giác, bị thương cũng không biết.",
                "situation": "formal"
            },
            {
                "ko": "발이 저리고 타는 것 같은 통증이 밤에 심해져요.",
                "vi": "Chân tê và đau như bị cháy, ban đêm càng nặng.",
                "situation": "onsite"
            },
            {
                "ko": "매일 발을 씻고 상처가 있는지 확인하세요.",
                "vi": "Mỗi ngày rửa chân và kiểm tra xem có vết thương không.",
                "situation": "formal"
            }
        ],
        "relatedTerms": ["당뇨병", "말초신경병증", "당뇨발", "족부궤양"]
    },
    {
        "slug": "thieu-mau",
        "korean": "빈혈",
        "vietnamese": "Thiếu máu",
        "hanja": "貧血",
        "hanjaReading": "貧(가난할 빈) + 血(피 혈)",
        "pronunciation": "빈혈",
        "meaningKo": "혈액 내 적혈구 수나 헤모글로빈 농도가 정상보다 낮아진 상태입니다. 통역 시 주의할 점은 '빈혈'과 '저혈압'을 혼동하는 환자가 많으므로 명확히 구분해야 합니다. 베트남어로는 'thiếu máu'가 표준이며, '빈혈로 쓰러진다'는 표현을 'ngất do thiếu máu'로 통역할 수 있지만, 실제로는 저혈압이나 다른 원인인 경우가 많으니 정확히 확인해야 합니다. 철분결핍성 빈혈(thiếu máu do thiếu sắt)이 가장 흔하므로 철분제 복용법도 설명해야 합니다.",
        "meaningVi": "Tình trạng số lượng hồng cầu hoặc nồng độ hemoglobin trong máu thấp hơn bình thường. Triệu chứng gồm mệt mỏi, chóng mặt, da xanh, tim đập nhanh. Nguyên nhân phổ biến là thiếu sắt, thiếu vitamin B12, mất máu. Điều trị tùy nguyên nhân, thường bổ sung sắt.",
        "context": "일반내과, 산부인과, 소화기내과, 건강검진",
        "culturalNote": "한국에서는 철분제를 공복에 복용하라고 권장하지만, 베트남에서는 위장 부작용 때문에 식후 복용을 선호합니다. 베트남 여성들은 월경과다로 인한 빈혈이 많지만 참고 넘어가는 경우가 많습니다. '빈혈'과 '어지럼증(chóng mặt)'을 동일시하는 경향이 있어 구분이 필요합니다.",
        "commonMistakes": [
            {
                "mistake": "빈혈 = 저혈압",
                "correction": "빈혈은 적혈구/헤모글로빈 부족, 저혈압은 혈압이 낮은 것",
                "explanation": "완전히 다른 개념입니다."
            },
            {
                "mistake": "Huyết áp thấp",
                "correction": "Thiếu máu (빈혈), Huyết áp thấp (저혈압)",
                "explanation": "'Huyết áp'는 혈압, 'thiếu máu'는 빈혈입니다."
            },
            {
                "mistake": "빈혈약",
                "correction": "철분제, 빈혈 치료제",
                "explanation": "'약'보다는 구체적으로 '철분제(viên sắt)'라고 해야 합니다."
            }
        ],
        "examples": [
            {
                "ko": "헤모글로빈 수치가 10g/dL로 낮아서 철분결핍성 빈혈로 진단되었습니다.",
                "vi": "Hemoglobin chỉ 10g/dL, được chẩn đoán thiếu máu do thiếu sắt.",
                "situation": "formal"
            },
            {
                "ko": "요즘 너무 피곤하고 얼굴이 창백해서 검사했더니 빈혈이래요.",
                "vi": "Dạo này mệt quá và mặt xanh xao, xét nghiệm thì thiếu máu.",
                "situation": "onsite"
            },
            {
                "ko": "철분제는 비타민C와 함께 복용하면 흡수가 잘 됩니다.",
                "vi": "Uống viên sắt cùng vitamin C thì hấp thu tốt hơn.",
                "situation": "formal"
            }
        ],
        "relatedTerms": ["헤모글로빈", "철분", "적혈구", "조혈"]
    },
    {
        "slug": "benh-bach-cau",
        "korean": "백혈병",
        "vietnamese": "Bệnh bạch cầu",
        "hanja": "白血病",
        "hanjaReading": "白(흰 백) + 血(피 혈) + 病(병 병)",
        "pronunciation": "백혈병",
        "meaningKo": "골수에서 백혈구가 비정상적으로 증식하는 혈액암입니다. 통역 시 주의할 점은 급성과 만성, 골수성과 림프구성으로 구분되며 치료법이 다르므로 정확한 분류를 통역해야 합니다. 베트남어로는 'bệnh bạch cầu' 또는 'ung thư máu(혈액암)'로 씁니다. 항암치료와 골수이식에 대한 설명이 필수이며, 치료 기간이 길고 힘들다는 점을 솔직히 전달해야 합니다. 환자와 가족의 감정적 충격이 크므로 통역사의 태도가 중요합니다.",
        "meaningVi": "Ung thư máu do tủy xương sản xuất quá nhiều bạch cầu bất thường. Chia thành cấp tính và mãn tính, tủy và lympho. Triệu chứng: mệt, sốt, xuất huyết, nhiễm trùng. Điều trị bằng hóa trị, ghép tủy xương. Tiên lượng phụ thuộc loại và giai đoạn.",
        "context": "혈액종양내과, 소아혈액종양과, 이식센터",
        "culturalNote": "한국은 비혈연 골수기증자 풀이 크지만, 베트남은 아직 부족해 형제간 이식이 주류입니다. 베트남에서는 '백혈병=죽음'이라는 인식이 강하지만, 최근 치료 성적이 많이 개선되었음을 설명해야 합니다. 항암치료 부작용(탈모, 구토)에 대한 두려움이 크므로 미리 설명해야 합니다.",
        "commonMistakes": [
            {
                "mistake": "혈액암 = 백혈병",
                "correction": "백혈병은 혈액암의 한 종류",
                "explanation": "림프종, 골수종 등도 혈액암에 포함됩니다."
            },
            {
                "mistake": "Ung thư máu (막연히)",
                "correction": "Bệnh bạch cầu cấp tính/mãn tính",
                "explanation": "정확한 진단명을 써야 합니다."
            },
            {
                "mistake": "골수이식을 '수혈'로 오역",
                "correction": "Ghép tủy xương (골수이식), Truyền máu (수혈)",
                "explanation": "완전히 다른 치료법입니다."
            }
        ],
        "examples": [
            {
                "ko": "급성골수성백혈병으로 진단되어 항암치료를 시작했습니다.",
                "vi": "Được chẩn đoán bệnh bạch cầu tủy cấp, bắt đầu hóa trị.",
                "situation": "formal"
            },
            {
                "ko": "몸에 멍이 자주 들고 코피가 나서 검사했더니 백혈병이래요.",
                "vi": "Hay bị bầm tím và chảy máu cam, xét nghiệm ra bệnh bạch cầu.",
                "situation": "onsite"
            },
            {
                "ko": "관해 상태를 유지하기 위해 골수이식을 고려해야 합니다.",
                "vi": "Để duy trì thuyên giảm, cần cân nhắc ghép tủy xương.",
                "situation": "formal"
            }
        ],
        "relatedTerms": ["골수", "항암치료", "골수이식", "관해"]
    },
    {
        "slug": "u-lympho-ac-tinh",
        "korean": "림프종",
        "vietnamese": "U lympho ác tính",
        "hanja": "淋巴腫",
        "hanjaReading": "淋(임할 림) + 巴(바랄 파) + 腫(부을 종)",
        "pronunciation": "림프종",
        "meaningKo": "림프계에 발생하는 악성 종양으로, 호지킨 림프종과 비호지킨 림프종으로 나뉩니다. 통역 시 주의할 점은 목이나 겨드랑이에 만져지는 '림프절 비대(hạch to)'와 '림프종'을 구분해야 하며, 대부분의 림프절 비대는 염증성이므로 환자를 안심시킬 필요가 있습니다. 베트남어로는 'u lympho ác tính' 또는 'ung thư hạch'로 씁니다. 병기(giai đoạn)와 아형(phân týp)에 따라 치료가 달라지므로 정확히 통역해야 합니다.",
        "meaningVi": "Ung thư phát triển từ hệ lympho, chia thành Hodgkin và non-Hodgkin. Triệu chứng: hạch to không đau, sốt, đổ mồ hôi đêm, sút cân. Chẩn đoán bằng sinh thiết hạch. Điều trị chủ yếu bằng hóa trị, xạ trị. Tiên lượng tùy loại và giai đoạn.",
        "context": "혈액종양내과, 방사선종양학과, 조직검사",
        "culturalNote": "한국에서는 PET-CT로 병기를 정확히 판단하지만, 베트남은 비용 문제로 CT만 찍는 경우가 많습니다. 베트남 환자들은 '혹(u)'과 '암(ung thư)'을 구분하지 못하는 경우가 많아 설명이 필요합니다. 림프종은 완치 가능성이 높은 암이라는 점을 강조해야 합니다.",
        "commonMistakes": [
            {
                "mistake": "림프암",
                "correction": "림프종",
                "explanation": "정확한 의학 용어는 '림프종'입니다."
            },
            {
                "mistake": "Ung thư hạch (막연히)",
                "correction": "U lympho ác tính (Hodgkin/non-Hodgkin)",
                "explanation": "호지킨과 비호지킨을 구분해야 합니다."
            },
            {
                "mistake": "림프절 비대 = 림프종",
                "correction": "림프절 비대는 염증, 감염 등 다양한 원인",
                "explanation": "대부분 양성이며, 림프종은 조직검사로 확진합니다."
            }
        ],
        "examples": [
            {
                "ko": "비호지킨 림프종 3기로 진단되어 R-CHOP 항암치료를 시작했습니다.",
                "vi": "Được chẩn đoán u lympho non-Hodgkin giai đoạn 3, bắt đầu hóa trị R-CHOP.",
                "situation": "formal"
            },
            {
                "ko": "목에 혹이 만져져서 조직검사를 했더니 림프종이래요.",
                "vi": "Sờ thấy u ở cổ, sinh thiết ra u lympho ác tính.",
                "situation": "onsite"
            },
            {
                "ko": "치료 반응이 좋아서 완전관해 상태입니다.",
                "vi": "Đáp ứng điều trị tốt, hiện đang thuyên giảm hoàn toàn.",
                "situation": "formal"
            }
        ],
        "relatedTerms": ["림프절", "조직검사", "항암치료", "병기"]
    },
    {
        "slug": "hoa-tri",
        "korean": "항암화학요법",
        "vietnamese": "Hóa trị",
        "hanja": "抗癌化學療法",
        "hanjaReading": "抗(막을 항) + 癌(암 암) + 化(될 화) + 學(배울 학) + 療(고칠 료) + 法(법 법)",
        "pronunciation": "항암화학요법",
        "meaningKo": "항암제를 사용하여 암세포를 죽이거나 성장을 억제하는 치료법입니다. 통역 시 주의할 점은 '항암치료'라는 넓은 용어와 '항암화학요법(세포독성 항암제)'을 구분해야 하며, 최근에는 표적치료, 면역치료와 병행하는 경우가 많습니다. 베트남어로는 'hóa trị'가 가장 일반적이며, 'hóa trị liệu'라고도 씁니다. 부작용(탈모, 구토, 백혈구 감소)에 대한 설명과 대처법 교육이 필수입니다.",
        "meaningVi": "Phương pháp điều trị ung thư bằng thuốc hóa chất tiêu diệt tế bào ung thư. Tác dụng phụ: rụng tóc, buồn nôn, giảm bạch cầu, mệt mỏi. Có thể kết hợp với phẫu thuật, xạ trị. Cần theo dõi xét nghiệm máu thường xuyên, phòng nhiễm trùng.",
        "context": "종양내과, 외래 항암치료실, 입원 항암치료",
        "culturalNote": "한국은 외래 항암치료가 보편화되었지만, 베트남은 입원 치료 비중이 높습니다. 베트남 환자들은 탈모(rụng tóc)를 매우 두려워하므로 가발이나 두건 사용을 미리 안내해야 합니다. 한국은 부작용 완화제(지사제, 진토제)를 적극 처방하지만, 베트남은 환자가 참는 경향이 있습니다.",
        "commonMistakes": [
            {
                "mistake": "항암제",
                "correction": "항암화학요법 (치료 과정 전체)",
                "explanation": "항암제는 약물이고, 항암화학요법은 치료법입니다."
            },
            {
                "mistake": "Thuốc chống ung thư (막연히)",
                "correction": "Hóa trị (화학요법), Điều trị đích (표적치료)",
                "explanation": "치료 방식에 따라 구분해야 합니다."
            },
            {
                "mistake": "부작용은 참아야 한다고 오역",
                "correction": "부작용은 약물로 조절 가능하며 참지 말고 말씀해야 함",
                "explanation": "부작용 관리가 치료 성공의 핵심입니다."
            }
        ],
        "examples": [
            {
                "ko": "유방암 3기로 수술 후 6차례의 항암화학요법을 받았습니다.",
                "vi": "Ung thư vú giai đoạn 3, sau phẫu thuật đã hóa trị 6 đợt.",
                "situation": "formal"
            },
            {
                "ko": "항암치료 받고 나서 머리카락이 다 빠졌어요.",
                "vi": "Sau hóa trị, tóc rụng hết.",
                "situation": "onsite"
            },
            {
                "ko": "백혈구 수치가 낮아서 다음 항암치료를 연기해야 합니다.",
                "vi": "Bạch cầu thấp nên phải hoãn đợt hóa trị tiếp theo.",
                "situation": "formal"
            }
        ],
        "relatedTerms": ["항암제", "부작용", "백혈구", "항암치료"]
    },
    {
        "slug": "thuoc-dieu-tri-dich",
        "korean": "표적항암제",
        "vietnamese": "Thuốc điều trị đích",
        "hanja": "標的抗癌劑",
        "hanjaReading": "標(표할 표) + 的(과녁 적) + 抗(막을 항) + 癌(암 암) + 劑(약제 제)",
        "pronunciation": "표적항암제",
        "meaningKo": "암세포의 특정 분자나 경로를 표적으로 하여 암세포만 선택적으로 공격하는 항암제입니다. 통역 시 주의할 점은 기존 항암화학요법과 달리 정상세포 손상이 적어 부작용이 적다는 장점을 설명해야 하지만, 모든 환자에게 효과가 있는 것은 아니며 유전자 검사가 필요한 경우가 많습니다. 베트남어로는 'thuốc điều trị đích' 또는 'thuốc nhắm trúng đích'로 씁니다. 비용이 매우 높으므로 보험 적용 여부를 확인해야 합니다.",
        "meaningVi": "Thuốc chống ung thư tác động chính xác vào tế bào ung thư, ít gây hại cho tế bào bình thường. Tác dụng phụ nhẹ hơn hóa trị truyền thống. Cần xét nghiệm gen để xác định hiệu quả. Giá thành cao. Ví dụ: Herceptin cho ung thư vú HER2+, Gleevec cho bạch cầu mãn.",
        "context": "종양내과, 유전자 검사 상담, 신약 설명",
        "culturalNote": "한국은 표적항암제가 건강보험에 많이 등재되어 있지만, 베트남은 대부분 전액 본인부담이라 경제적 부담이 큽니다. 베트남 환자들은 '신약=효과 좋음'으로만 인식하는 경향이 있어, 유전자 검사 결과에 따라 효과가 다르다는 점을 설명해야 합니다. 한국은 HER2, EGFR 등 유전자 검사가 표준이지만, 베트남은 비용 문제로 검사를 안 하는 경우가 많습니다.",
        "commonMistakes": [
            {
                "mistake": "표적치료 = 면역치료",
                "correction": "표적치료는 암세포 표적, 면역치료는 면역체계 활성화",
                "explanation": "작용 기전이 완전히 다릅니다."
            },
            {
                "mistake": "Thuốc chống ung thư mới",
                "correction": "Thuốc điều trị đích",
                "explanation": "'신약'이 아니라 '표적치료'라는 분류입니다."
            },
            {
                "mistake": "모든 암에 효과적이라고 오역",
                "correction": "특정 유전자 변이가 있는 암에만 효과",
                "explanation": "유전자 검사가 필수입니다."
            }
        ],
        "examples": [
            {
                "ko": "HER2 양성 유방암으로 허셉틴 표적항암제 치료를 받고 있습니다.",
                "vi": "Ung thư vú HER2 dương tính, đang dùng thuốc điều trị đích Herceptin.",
                "situation": "formal"
            },
            {
                "ko": "유전자 검사 결과 EGFR 돌연변이가 있어서 표적치료가 가능해요.",
                "vi": "Xét nghiệm gen có đột biến EGFR nên có thể điều trị đích.",
                "situation": "onsite"
            },
            {
                "ko": "표적항암제는 기존 항암제보다 부작용이 적지만 비용이 높습니다.",
                "vi": "Thuốc điều trị đích ít tác dụng phụ hơn hóa trị nhưng giá cao.",
                "situation": "formal"
            }
        ],
        "relatedTerms": ["항암제", "유전자검사", "HER2", "EGFR"]
    },
    {
        "slug": "thuoc-mien-dich-chong-ung-thu",
        "korean": "면역항암제",
        "vietnamese": "Thuốc miễn dịch chống ung thư",
        "hanja": "免疫抗癌劑",
        "hanjaReading": "免(면할 면) + 疫(전염병 역) + 抗(막을 항) + 癌(암 암) + 劑(약제 제)",
        "pronunciation": "면역항암제",
        "meaningKo": "인체의 면역체계를 활성화하여 암세포를 공격하도록 돕는 항암제입니다. 통역 시 주의할 점은 '면역항암제'와 '면역력 강화제'를 혼동하지 않도록 해야 하며, PD-1, PD-L1 같은 용어가 자주 등장하므로 미리 숙지해야 합니다. 베트남어로는 'thuốc miễn dịch chống ung thư' 또는 'thuốc liệu pháp miễn dịch'로 씁니다. 자가면역 부작용(viêm phổi, viêm đại tràng 등)이 특이하므로 증상 설명이 중요합니다.",
        "meaningVi": "Thuốc kích hoạt hệ miễn dịch của cơ thể để tấn công tế bào ung thư. Ví dụ: Keytruda, Opdivo (thuốc ức chế PD-1). Hiệu quả tốt ở một số loại ung thư như ung thư phổi, ung thư da. Tác dụng phụ đặc biệt: viêm tự miễn như viêm phổi, viêm đại tràng. Giá rất cao.",
        "context": "종양내과, 면역치료 클리닉, PD-L1 검사 설명",
        "culturalNote": "한국은 면역항암제가 많은 암종에 보험 적용되지만, 베트남은 아직 극히 제한적입니다. 베트남 환자들은 '면역력을 높인다'는 표현 때문에 건강식품과 혼동하는 경우가 많아 구분이 필요합니다. 자가면역 부작용은 베트남 의료진도 익숙하지 않은 경우가 있어 증상 모니터링이 중요합니다.",
        "commonMistakes": [
            {
                "mistake": "면역력 강화제",
                "correction": "면역항암제 (면역체계를 활성화하여 암 치료)",
                "explanation": "건강식품이 아니라 전문 항암제입니다."
            },
            {
                "mistake": "Thuốc tăng cường miễn dịch",
                "correction": "Thuốc miễn dịch chống ung thư (liệu pháp miễn dịch)",
                "explanation": "'tăng cường'은 일반적 강화를 의미하므로 부정확합니다."
            },
            {
                "mistake": "부작용이 없다고 오역",
                "correction": "자가면역 부작용이 있을 수 있음",
                "explanation": "일반 항암제와 다른 특이한 부작용이 있습니다."
            }
        ],
        "examples": [
            {
                "ko": "PD-L1 발현율이 높아서 키트루다 면역항암제 치료를 시작했습니다.",
                "vi": "PD-L1 cao nên bắt đầu điều trị bằng thuốc miễn dịch Keytruda.",
                "situation": "formal"
            },
            {
                "ko": "면역항암제 맞고 나서 설사가 심한데 괜찮은 건가요?",
                "vi": "Sau khi dùng thuốc miễn dịch, tiêu chảy nhiều, có sao không?",
                "situation": "onsite"
            },
            {
                "ko": "면역관련 부작용으로 스테로이드 치료가 필요할 수 있습니다.",
                "vi": "Tác dụng phụ liên quan miễn dịch có thể cần điều trị steroid.",
                "situation": "formal"
            }
        ],
        "relatedTerms": ["면역치료", "PD-1", "PD-L1", "자가면역"]
    },
    {
        "slug": "xa-tri",
        "korean": "방사선치료",
        "vietnamese": "Xạ trị",
        "hanja": "放射線治療",
        "hanjaReading": "放(놓을 방) + 射(쏠 사) + 線(줄 선) + 治(다스릴 치) + 療(고칠 료)",
        "pronunciation": "방사선치료",
        "meaningKo": "고에너지 방사선을 이용하여 암세포를 파괴하는 치료법입니다. 통역 시 주의할 점은 '방사선'이라는 단어에 환자들이 두려움을 느끼므로 안전성을 설명해야 하며, 치료 부위에 따라 부작용이 다르다는 점을 명확히 해야 합니다. 베트남어로는 'xạ trị' 또는 'xạ trị liệu'가 표준입니다. 피부 반응(da sạm, đỏ)과 피로감이 흔한 부작용이므로 관리법을 알려줘야 합니다.",
        "meaningVi": "Điều trị ung thư bằng tia phóng xạ năng lượng cao tiêu diệt tế bào ung thư tại vùng cụ thể. Thường kết hợp với phẫu thuật, hóa trị. Tác dụng phụ: da đỏ sạm, mệt, rụng tóc vùng xạ. Cần bôi kem dưỡng da, nghỉ ngơi đủ, uống nhiều nước.",
        "context": "방사선종양학과, 암 치료 계획, 수술 전후 보조치료",
        "culturalNote": "한국은 IMRT, IGRT 같은 정밀 방사선치료가 보편화되었지만, 베트남은 기본적인 방사선치료만 가능한 병원이 많습니다. 베트남 환자들은 '방사선=위험'이라는 인식이 강해 치료를 거부하는 경우도 있습니다. 치료 중 피부 관리(로션, 자극 피하기)에 대한 교육이 필수입니다.",
        "commonMistakes": [
            {
                "mistake": "방사선 = 방사능",
                "correction": "방사선치료는 통제된 의료 방사선, 방사능 오염과는 다름",
                "explanation": "환자들이 흔히 혼동하는 개념입니다."
            },
            {
                "mistake": "Tia phóng xạ (막연히)",
                "correction": "Xạ trị (방사선치료)",
                "explanation": "치료법을 명확히 표현해야 합니다."
            },
            {
                "mistake": "방사선치료 후 격리 필요하다고 오역",
                "correction": "외부 방사선치료는 격리 불필요 (내부 방사성동위원소 치료는 예외)",
                "explanation": "외부 방사선치료와 내부 치료를 구분해야 합니다."
            }
        ],
        "examples": [
            {
                "ko": "유방암 수술 후 재발 방지를 위해 6주간 방사선치료를 받았습니다.",
                "vi": "Sau phẫu thuật ung thư vú, xạ trị 6 tuần để phòng tái phát.",
                "situation": "formal"
            },
            {
                "ko": "방사선 맞는 부위 피부가 까맣게 탔어요.",
                "vi": "Vùng da xạ trị sạm đen.",
                "situation": "onsite"
            },
            {
                "ko": "방사선치료 중에는 자극적인 비누나 로션 사용을 피하세요.",
                "vi": "Trong thời gian xạ trị, tránh xà phòng và kem dưỡng kích ứng.",
                "situation": "formal"
            }
        ],
        "relatedTerms": ["방사선", "피부반응", "암치료", "부작용"]
    },
    {
        "slug": "dot-quy-nao",
        "korean": "뇌졸중",
        "vietnamese": "Đột quỵ não",
        "hanja": "腦卒中",
        "hanjaReading": "腦(뇌 뇌) + 卒(갑자기 졸) + 中(맞을 중)",
        "pronunciation": "뇌졸중",
        "meaningKo": "뇌혈관이 막히거나(뇌경색) 터져서(뇌출혈) 뇌 손상이 발생하는 응급질환입니다. 통역 시 주의할 점은 '중풍'이라는 한자어를 사용하는 노인 환자가 많으므로 '중풍 = 뇌졸중'임을 알아야 하며, 골든타임(golden time)이 중요하므로 FAST(얼굴, 팔, 언어, 시간) 증상을 명확히 통역해야 합니다. 베트남어로는 'đột quỵ não' 또는 간단히 'đột quỵ'로 씁니다. 재활치료의 중요성과 장기간 소요됨을 설명해야 합니다.",
        "meaningVi": "Bệnh mạch máu não bị tắc (nhồi máu não) hoặc vỡ (xuất huyết não), gây tổn thương não đột ngột. Triệu chứng: méo miệng, liệt nửa người, nói khó, đau đầu dữ dội. Cấp cứu khẩn trong 4,5 giờ đầu. Điều trị tiêu sợi huyết hoặc phẫu thuật. Cần phục hồi chức năng lâu dài.",
        "context": "응급실, 신경과, 재활의학과, 중환자실",
        "culturalNote": "한국은 뇌졸중 전문센터가 잘 갖춰져 있고 119를 통한 빠른 이송 시스템이 있지만, 베트남은 교통 문제로 골든타임을 놓치는 경우가 많습니다. 베트남 가족들은 '중풍'을 나이 들면 당연한 것으로 여기는 경향이 있어 예방 교육이 중요합니다. 한국은 재활치료를 적극적으로 하지만, 베트남은 가정에서 간병하는 경우가 많습니다.",
        "commonMistakes": [
            {
                "mistake": "중풍",
                "correction": "뇌졸중 (의학 용어)",
                "explanation": "중풍은 한자어이고, 뇌졸중이 정확한 의학 용어입니다."
            },
            {
                "mistake": "Đột quỵ não = Tai biến mạch máu não (혼용)",
                "correction": "둘 다 같은 의미로 쓰임",
                "explanation": "베트남에서는 두 표현 모두 사용되며, 'tai biến'이 더 격식적입니다."
            },
            {
                "mistake": "뇌출혈 = 뇌졸중",
                "correction": "뇌출혈은 뇌졸중의 한 종류",
                "explanation": "뇌졸중은 뇌경색과 뇌출혈을 포괄합니다."
            }
        ],
        "examples": [
            {
                "ko": "갑자기 한쪽 팔다리에 힘이 빠지고 말이 어눌해져서 뇌졸중으로 진단되었습니다.",
                "vi": "Đột ngột tay chân một bên yếu và nói khó, được chẩn đoán đột quỵ não.",
                "situation": "formal"
            },
            {
                "ko": "중풍 왔을 때는 빨리 병원 가야 해요. 시간이 중요해요.",
                "vi": "Khi đột quỵ phải đến bệnh viện nhanh. Thời gian rất quan trọng.",
                "situation": "onsite"
            },
            {
                "ko": "혈전용해제를 투여하여 막힌 혈관을 뚫었습니다.",
                "vi": "Đã tiêm thuốc tiêu sợi huyết để thông mạch bị tắc.",
                "situation": "formal"
            }
        ],
        "relatedTerms": ["뇌경색", "뇌출혈", "재활치료", "골든타임"]
    },
    {
        "slug": "nhoi-mau-nao",
        "korean": "뇌경색",
        "vietnamese": "Nhồi máu não",
        "hanja": "腦梗塞",
        "hanjaReading": "腦(뇌 뇌) + 梗(막힐 경) + 塞(막힐 색)",
        "pronunciation": "뇌경색",
        "meaningKo": "뇌혈관이 막혀서 뇌 조직에 혈액 공급이 차단되는 질환으로, 뇌졸중의 약 80%를 차지합니다. 통역 시 주의할 점은 '뇌경색'과 '뇌출혈'을 명확히 구분해야 하며, 치료법이 정반대(혈전용해 vs 지혈)이므로 오역하면 위험합니다. 베트남어로는 'nhồi máu não' 또는 'tắc mạch não'로 씁니다. tPA 혈전용해제는 4.5시간 이내 투여가 원칙이므로 시간 개념을 명확히 통역해야 합니다.",
        "meaningVi": "Mạch máu não bị tắc, ngừng cung cấp máu cho não. Nguyên nhân: cục máu đông, mảng xơ vữa. Điều trị cấp cứu: tiêm tPA tiêu sợi huyết trong 4,5 giờ đầu hoặc lấy huyết khối. Phòng ngừa: kiểm soát huyết áp, đường huyết, mỡ máu, uống thuốc chống đông.",
        "context": "응급실, 신경과, 중환자실, 뇌졸중센터",
        "culturalNote": "한국은 tPA 사용이 보편화되어 있지만, 베트남은 약품 수급과 비용 문제로 제한적입니다. 베트남에서는 아스피린 같은 항혈전제를 '혈액순환 개선제'로 이해하는 환자가 많아 정확한 작용 기전을 설명해야 합니다. 한국은 MRI로 정확한 진단을 하지만, 베트남은 CT만 가능한 병원이 많습니다.",
        "commonMistakes": [
            {
                "mistake": "뇌경색 = 뇌출혈",
                "correction": "뇌경색은 혈관 막힘, 뇌출혈은 혈관 터짐",
                "explanation": "정반대 병태생리이므로 반드시 구분해야 합니다."
            },
            {
                "mistake": "Xuất huyết não",
                "correction": "Nhồi máu não (경색), Xuất huyết não (출혈)",
                "explanation": "'xuất huyết'는 출혈, 'nhồi máu'는 경색입니다."
            },
            {
                "mistake": "골든타임을 '몇 시간 정도'로 애매하게 통역",
                "correction": "4.5시간 이내 (chính xác trong 4,5 giờ)",
                "explanation": "정확한 시간이 생명과 직결됩니다."
            }
        ],
        "examples": [
            {
                "ko": "MRI 검사 결과 좌측 대뇌 중동맥 영역의 급성 뇌경색으로 확인되었습니다.",
                "vi": "Kết quả MRI xác nhận nhồi máu não cấp vùng động mạch não giữa bên trái.",
                "situation": "formal"
            },
            {
                "ko": "증상 발생 후 3시간 만에 도착해서 혈전용해제를 맞을 수 있었어요.",
                "vi": "Đến bệnh viện sau 3 giờ có triệu chứng nên được tiêm thuốc tiêu sợi huyết.",
                "situation": "onsite"
            },
            {
                "ko": "재발 방지를 위해 항혈소판제를 평생 복용해야 합니다.",
                "vi": "Để phòng tái phát, phải uống thuốc chống kết tập tiểu cầu suốt đời.",
                "situation": "formal"
            }
        ],
        "relatedTerms": ["뇌졸중", "혈전용해제", "tPA", "항혈소판제"]
    },
    {
        "slug": "benh-parkinson",
        "korean": "파킨슨병",
        "vietnamese": "Bệnh Parkinson",
        "hanja": None,
        "hanjaReading": None,
        "pronunciation": "파킨슨병",
        "meaningKo": "뇌의 도파민 생성 세포가 점차 소실되어 운동 기능에 장애가 생기는 퇴행성 신경질환입니다. 통역 시 주의할 점은 '떨림(run)', '경직(cứng)', '느린 움직임(chậm chạp)', '자세 불안정(mất thăng bằng)'이라는 4대 증상을 정확히 전달해야 하며, 치매(sa sút trí tuệ)와 혼동하지 않도록 해야 합니다. 베트남어로는 'bệnh Parkinson'으로 고유명사 그대로 씁니다. 약물치료로 증상 조절이 가능하지만 완치는 불가능하다는 점을 솔직히 설명해야 합니다.",
        "meaningVi": "Bệnh thoái hóa thần kinh do giảm dopamine, gây rối loạn vận động. Triệu chứng: run tay chân, cứng cơ, chậm chạp, mất thăng bằng. Thường gặp ở người trên 60 tuổi. Điều trị bằng thuốc bổ sung dopamine (levodopa), không chữa khỏi nhưng kiểm soát được triệu chứng.",
        "context": "신경과, 노인의학과, 운동장애클리닉",
        "culturalNote": "한국에서는 파킨슨병 환자에 대한 인식이 개선되고 있지만, 베트남에서는 '노쇠함'으로 치부하는 경향이 있습니다. 베트남은 levodopa가 주 치료제이지만 한국은 다양한 약물 조합을 사용합니다. 한국은 뇌심부자극술(DBS) 같은 수술적 치료도 활발하지만, 베트남은 거의 시행되지 않습니다. 베트남 환자들은 '떨림'을 가장 창피해하므로 심리적 지지가 필요합니다.",
        "commonMistakes": [
            {
                "mistake": "파킨슨병 = 치매",
                "correction": "파킨슨병은 운동장애, 치매는 인지장애 (동반 가능하지만 다름)",
                "explanation": "완전히 다른 질환이며, 파킨슨병 말기에 치매가 동반될 수 있습니다."
            },
            {
                "mistake": "Bệnh run (단순히)",
                "correction": "Bệnh Parkinson",
                "explanation": "떨림은 증상 중 하나일 뿐이며, 정확한 병명을 써야 합니다."
            },
            {
                "mistake": "levodopa를 '떨림 약'으로 통역",
                "correction": "도파민 보충제 (thuốc bổ sung dopamine)",
                "explanation": "작용 기전을 정확히 이해하고 통역해야 합니다."
            }
        ],
        "examples": [
            {
                "ko": "손 떨림과 걸음걸이가 느려져서 검사 받았더니 파킨슨병으로 진단되었습니다.",
                "vi": "Tay run và đi chậm, xét nghiệm thì bị bệnh Parkinson.",
                "situation": "formal"
            },
            {
                "ko": "레보도파 약을 먹으니까 떨림이 많이 좋아졌어요.",
                "vi": "Uống levodopa thì run bớt nhiều.",
                "situation": "onsite"
            },
            {
                "ko": "약효가 떨어지는 시간대에 증상이 심해질 수 있습니다.",
                "vi": "Khi hết tác dụng thuốc, triệu chứng có thể nặng lên.",
                "situation": "formal"
            }
        ],
        "relatedTerms": ["떨림", "도파민", "레보도파", "운동장애"]
    },
    {
        "slug": "benh-alzheimer",
        "korean": "알츠하이머병",
        "vietnamese": "Bệnh Alzheimer",
        "hanja": None,
        "hanjaReading": None,
        "pronunciation": "알츠하이머병",
        "meaningKo": "뇌의 신경세포가 점차 파괴되어 기억력과 인지기능이 서서히 저하되는 치매의 가장 흔한 원인 질환입니다. 통역 시 주의할 점은 '치매(sa sút trí tuệ)'와 '알츠하이머병'을 구분해야 하며, 초기 증상인 '최근 기억력 저하(quên gần nhớ xa)'를 정확히 전달해야 합니다. 베트남어로는 'bệnh Alzheimer'로 고유명사 그대로 쓰며, 'lãng trí'라는 구어적 표현도 씁니다. 가족의 부담이 크므로 요양시설이나 돌봄 서비스 정보도 제공해야 합니다.",
        "meaningVi": "Bệnh thoái hóa não, nguyên nhân phổ biến nhất gây sa sút trí tuệ (dementia). Triệu chứng: quên gần nhớ xa, lú lẫn thời gian-không gian, thay đổi tính cách, khó giao tiếp. Tiến triển chậm, chưa có thuốc chữa khỏi. Điều trị làm chậm tiến triển, chăm sóc dài hạn.",
        "context": "신경과, 정신건강의학과, 노인의학과, 요양병원",
        "culturalNote": "한국은 국가 치매 책임제로 진단과 관리 시스템이 구축되어 있지만, 베트남은 아직 가족이 전적으로 돌보는 경우가 대부분입니다. 베트남에서는 '미치다(điên)'라는 부정적 인식이 강해 환자 가족이 숨기는 경향이 있습니다. 한국은 치매 안심센터 같은 공공 서비스가 있지만, 베트남은 거의 없습니다.",
        "commonMistakes": [
            {
                "mistake": "치매 = 알츠하이머병",
                "correction": "알츠하이머병은 치매의 한 원인 (가장 흔함)",
                "explanation": "치매는 증후군이고, 알츠하이머병은 질환명입니다."
            },
            {
                "mistake": "Sa sút trí tuệ = Bệnh Alzheimer (혼용)",
                "correction": "Sa sút trí tuệ (치매 증후군), Bệnh Alzheimer (알츠하이머병)",
                "explanation": "치매는 증상, 알츠하이머는 원인 질환입니다."
            },
            {
                "mistake": "건망증을 알츠하이머 초기로 오역",
                "correction": "정상 노화에 의한 건망증과 병적 기억장애는 다름",
                "explanation": "열쇠를 어디 뒀는지 잊는 것(정상)과 열쇠가 무엇인지 모르는 것(병적)을 구분해야 합니다."
            }
        ],
        "examples": [
            {
                "ko": "최근 일을 자꾸 잊고 같은 말을 반복해서 알츠하이머병 초기로 진단되었습니다.",
                "vi": "Cứ quên chuyện gần đây và lặp lại câu nói, được chẩn đoán Alzheimer giai đoạn đầu.",
                "situation": "formal"
            },
            {
                "ko": "할머니가 집 주소를 못 찾아서 경찰에서 연락 왔어요.",
                "vi": "Bà không tìm được đường về nhà, công an gọi điện.",
                "situation": "onsite"
            },
            {
                "ko": "알츠하이머 치료제로 증상 진행을 늦출 수 있습니다.",
                "vi": "Thuốc điều trị Alzheimer có thể làm chậm tiến triển.",
                "situation": "formal"
            }
        ],
        "relatedTerms": ["치매", "인지장애", "기억력", "돌봄"]
    },
    {
        "slug": "dong-kinh",
        "korean": "간질",
        "vietnamese": "Động kinh",
        "hanja": "癎疾",
        "hanjaReading": "癎(간질 간) + 疾(병 질)",
        "pronunciation": "간질",
        "meaningKo": "뇌의 비정상적인 전기 활동으로 인해 반복적인 발작이 일어나는 신경질환입니다. 통역 시 주의할 점은 '간질'이라는 용어에 사회적 편견이 있어 최근 '뇌전증'이라는 용어를 사용하는 추세이지만, 베트남어로는 여전히 'động kinh'이 표준입니다. 발작 유형(toàn thể, bộ phận)과 응급처치법(놓아두기, 옆으로 눕히기)을 명확히 설명해야 합니다. 항경련제는 평생 복용이 필요한 경우가 많으므로 복약 순응도 교육이 중요합니다.",
        "meaningVi": "Bệnh thần kinh do hoạt động điện bất thường trong não, gây co giật lặp lại. Phân loại: động kinh toàn thể (toàn thân) và bộ phận (khu trú). Điều trị bằng thuốc chống động kinh, cần uống đều đặn. Xử trí cơn: nằm nghiêng, không nhét gì vào miệng, gọi cấp cứu nếu kéo dài >5 phút.",
        "context": "신경과, 응급실, 소아신경과",
        "culturalNote": "한국은 '뇌전증'이라는 용어로 개선하려 하지만, 베트남은 'động kinh'이 유일한 용어이며 사회적 편견이 여전히 강합니다. 베트남에서는 발작 시 입에 숟가락을 넣는 잘못된 민간요법이 있어 교정이 필요합니다. 한국은 항경련제 선택지가 다양하지만, 베트남은 오래된 약물(phenobarbital) 위주입니다.",
        "commonMistakes": [
            {
                "mistake": "간질 = 정신병",
                "correction": "간질은 뇌 전기 활동 이상, 정신질환 아님",
                "explanation": "사회적 편견에서 비롯된 오해입니다."
            },
            {
                "mistake": "Bệnh tâm thần",
                "correction": "Động kinh (뇌전증), Bệnh tâm thần (정신병)",
                "explanation": "완전히 다른 질환입니다."
            },
            {
                "mistake": "발작 시 입에 무언가 넣어야 한다고 통역",
                "correction": "입에 아무것도 넣지 말고 옆으로 눕힐 것",
                "explanation": "잘못된 응급처치는 질식이나 치아 손상을 일으킬 수 있습니다."
            }
        ],
        "examples": [
            {
                "ko": "전신 강직 간대 발작으로 항경련제를 복용하고 있습니다.",
                "vi": "Co giật toàn thân, đang uống thuốc chống động kinh.",
                "situation": "formal"
            },
            {
                "ko": "갑자기 쓰러져서 경련하더니 5분쯤 후에 깨어났어요.",
                "vi": "Đột ngột té và co giật, sau khoảng 5 phút thì tỉnh.",
                "situation": "onsite"
            },
            {
                "ko": "약을 임의로 끊으면 발작이 더 심해질 수 있습니다.",
                "vi": "Nếu tự ý ngừng thuốc, cơn động kinh có thể nặng hơn.",
                "situation": "formal"
            }
        ],
        "relatedTerms": ["발작", "뇌파검사", "항경련제", "뇌전증"]
    },
    {
        "slug": "xo-cung-rai-rac",
        "korean": "다발성경화증",
        "vietnamese": "Xơ cứng rải rác",
        "hanja": "多發性硬化症",
        "hanjaReading": "多(많을 다) + 發(필 발) + 性(성품 성) + 硬(굳을 경) + 化(될 화) + 症(병 증)",
        "pronunciation": "다발성경화쯩",
        "meaningKo": "중추신경계의 여러 부위에서 면역체계가 신경을 공격하여 염증과 손상이 반복되는 자가면역질환입니다. 통역 시 주의할 점은 '재발-완화형'이 가장 흔하며, 증상이 다양하고(시력저하, 감각이상, 보행장애 등) 예측 불가능하다는 점을 설명해야 합니다. 베트남어로는 'xơ cứng rải rác' 또는 'đa xơ cứng'으로 씁니다. MRI와 뇌척수액 검사가 진단에 필수이며, 면역조절제 치료가 필요합니다.",
        "meaningVi": "Bệnh tự miễn tấn công hệ thần kinh trung ương, gây tổn thương nhiều vùng trong não và tủy sống. Triệu chứng: giảm thị lực, tê liệt, khó đi, mệt. Thường tái phát và lui bệnh xen kẽ. Chẩn đoán bằng MRI, dịch não tủy. Điều trị điều hòa miễn dịch.",
        "context": "신경과, 면역질환 클리닉, MRI 판독",
        "culturalNote": "한국은 다발성경화증 환자가 비교적 적지만(동양인에 드물), 최근 증가 추세입니다. 베트남은 더욱 드물어 의료진도 경험이 적을 수 있습니다. 한국은 면역조절제(인터페론, 글라티라머)가 보험 적용되지만, 베트남은 구하기 어렵고 비쌉니다. '재발'과 '악화'의 차이를 명확히 통역해야 합니다.",
        "commonMistakes": [
            {
                "mistake": "근육경화증",
                "correction": "다발성경화증 (중추신경계 질환)",
                "explanation": "근육이 아니라 신경의 탈수초화 질환입니다."
            },
            {
                "mistake": "Xơ cứng cơ (근육)",
                "correction": "Xơ cứng rải rác (신경)",
                "explanation": "'cơ'는 근육, 신경계 질환과는 다릅니다."
            },
            {
                "mistake": "완치 가능하다고 오역",
                "correction": "완치 불가능, 증상 조절 및 재발 억제가 목표",
                "explanation": "만성 질환으로 장기 관리가 필요합니다."
            }
        ],
        "examples": [
            {
                "ko": "시력이 갑자기 떨어지고 팔다리가 저려서 MRI를 찍었더니 다발성경화증으로 진단되었습니다.",
                "vi": "Thị lực đột ngột giảm và tê tay chân, chụp MRI thì bị xơ cứng rải rác.",
                "situation": "formal"
            },
            {
                "ko": "증상이 좋아졌다 나빠졌다 반복돼요.",
                "vi": "Triệu chứng lúc tốt lúc xấu.",
                "situation": "onsite"
            },
            {
                "ko": "재발을 막기 위해 면역조절제를 꾸준히 맞아야 합니다.",
                "vi": "Để ngăn tái phát, phải tiêm thuốc điều hòa miễn dịch đều đặn.",
                "situation": "formal"
            }
        ],
        "relatedTerms": ["자가면역질환", "MRI", "재발", "면역조절제"]
    }
]

print(f"📚 의료 용어 추가 스크립트 v3-f")
print(f"대상: {len(new_terms)}개 용어 (내분비/대사, 혈액, 종양치료, 신경계)")
print(f"파일: {file_path}\n")

# 중복 제거 (기존 slug와 비교)
unique_new_terms = [t for t in new_terms if t['slug'] not in existing_slugs]

print(f"✅ 신규 용어: {len(unique_new_terms)}개")
print(f"⚠️  중복 제외: {len(new_terms) - len(unique_new_terms)}개\n")

# 기존 데이터에 추가
data.extend(unique_new_terms)

# 파일 저장
with open(file_path, 'w', encoding='utf-8') as f:
    json.dump(data, f, ensure_ascii=False, indent=2)

print(f"💾 저장 완료!")
print(f"📊 총 용어 수: {len(data)}개")
print(f"🎯 추가된 용어: {len(unique_new_terms)}개\n")

if len(unique_new_terms) > 0:
    print("📋 추가된 용어 목록:")
    for i, term in enumerate(unique_new_terms, 1):
        print(f"   {i}. {term['korean']} ({term['vietnamese']})")
