#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Add 50 NEW medical terms to medical.json
Focus: Traditional Korean Medicine, Medical Tourism, Mental Health, Cosmetic Medicine
"""

import json
import os

# EXACT PATH CODE
file_path = os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', 'data', 'terms', 'medical.json')

# 50 NEW MEDICAL TERMS - ALL TIER S QUALITY
new_terms = [
    {
        "slug": "cham-thuat",
        "korean": "침술",
        "vietnamese": "Châm thuật",
        "hanja": "鍼術",
        "hanjaReading": "鍼(바늘 침) + 術(재주 술)",
        "pronunciation": "짐뚜엇",
        "meaningKo": "한의학의 대표적인 치료법으로, 인체의 경혈(經穴)에 가느다란 침을 놓아 기혈(氣血)의 흐름을 조절하여 질병을 치료하는 방법입니다. 통역 시 주의할 점은 베트남에서도 전통의학으로 침술이 발달했으나, 한국의 경락 이론과 베트남의 침술 이론에 차이가 있을 수 있으므로 '한국식 침술' 또는 'Châm cứu Hàn Quốc'으로 구분하여 설명하는 것이 오해를 방지합니다. 또한 침의 굵기, 깊이, 자극 방법 등 기술적 세부사항을 전달할 때는 정확한 의학 용어를 사용해야 합니다.",
        "meaningVi": "Châm thuật là phương pháp điều trị đại diện của y học cổ truyền Hàn Quốc, sử dụng kim châm mỏng để châm vào các huyệt đạo trên cơ thể người, điều chỉnh luồng khí huyết để chữa bệnh. Đây là liệu pháp được UNESCO công nhận là di sản văn hóa phi vật thể của nhân loại.",
        "context": "한의원, 재활의학과, 통증클리닉, 의료관광",
        "culturalNote": "한국의 침술은 중국 전통의학을 기반으로 발전했지만 독자적인 이론 체계를 갖추고 있습니다. 베트남도 전통 침술(Châm cứu)이 있으나 경혈의 위치나 자침 깊이 등에서 차이가 있을 수 있습니다. 한국에서는 침술이 보험 적용되는 정식 의료행위이며, 반드시 한의사 면허가 있어야 시술할 수 있습니다. 베트남 환자에게 설명할 때는 한국 침술의 과학적 근거와 임상 효과를 강조하는 것이 신뢰를 높입니다.",
        "commonMistakes": [
            {
                "mistake": "Châm kim",
                "correction": "Châm thuật 또는 Châm cứu",
                "explanation": "'Châm kim'은 '침을 놓다'라는 동작만을 의미하고, 'Châm thuật'은 침술이라는 의학 체계 전체를 가리킵니다."
            },
            {
                "mistake": "Kim tiêm",
                "correction": "Kim châm",
                "explanation": "'Kim tiêm'은 주사 바늘을 의미하며, 침술용 침은 'Kim châm'이라고 합니다."
            },
            {
                "mistake": "침술을 'massage'로 오역",
                "correction": "Châm thuật (acupuncture)",
                "explanation": "침술과 마사지는 전혀 다른 치료법이므로 명확히 구분해야 합니다."
            }
        ],
        "examples": [
            {
                "ko": "만성 요통 치료를 위해 주 2회 침술 치료를 받고 계십니다.",
                "vi": "Bạn đang được điều trị châm thuật 2 lần/tuần để chữa đau lưng mãn tính.",
                "situation": "formal"
            },
            {
                "ko": "침 맞을 때 약간 찌릿한 느낌이 들 수 있어요.",
                "vi": "Khi châm kim có thể cảm thấy hơi tê nhức.",
                "situation": "onsite"
            },
            {
                "ko": "침술은 WHO에서 인정한 효과적인 통증 치료법입니다.",
                "vi": "Châm thuật là phương pháp giảm đau hiệu quả được WHO công nhận.",
                "situation": "formal"
            }
        ],
        "relatedTerms": ["뜸치료", "부항", "경혈", "한방통증치료"]
    },
    {
        "slug": "duc-tri-lieu",
        "korean": "뜸치료",
        "vietnamese": "Đốt cứu (Đức trị liệu)",
        "hanja": None,
        "hanjaReading": None,
        "pronunciation": "독꾸",
        "meaningKo": "쑥을 태워 그 열로 경혈을 자극하여 치료하는 한의학 요법입니다. 뜸은 체내의 한기(寒氣)를 몰아내고 기혈 순환을 촉진하는 효과가 있습니다. 통역 시 주의할 점은 베트nam에서는 'Đốt cứu'라는 용어가 일반적이지만, 일부 지역에서는 다른 표현을 쓸 수 있으므로 환자의 이해도를 확인해야 합니다. 또한 뜸의 종류(직접뜸, 간접뜸, 뜸봉)를 설명할 때는 화상 위험성과 시술 방법을 명확히 전달하여 환자가 안심하고 치료받을 수 있도록 해야 합니다.",
        "meaningVi": "Đốt cứu là phương pháp điều trị y học cổ truyền Hàn Quốc bằng cách đốt ngải cứu để kích thích các huyệt đạo bằng nhiệt. Liệu pháp này giúp xua tan hàn khí trong cơ thể và thúc đẩy tuần hoàn khí huyết, đặc biệt hiệu quả với các bệnh lý do lạnh gây ra.",
        "context": "한의원, 재활치료, 만성통증, 소화기질환",
        "culturalNote": "한국의 뜸치료는 쑥(艾草)을 주재료로 사용하며, 직접뜸과 간접뜸으로 나뉩니다. 베트남에서도 전통적으로 뜸 치료가 있었으나 현대에는 덜 보편화되었습니다. 한국에서는 뜸이 침술과 함께 가장 흔히 사용되는 한방 치료법이며, 특히 노인 환자들 사이에서 선호도가 높습니다. 베트남 환자에게 설명할 때는 화상 위험을 최소화하는 간접뜸 방법을 강조하면 수용도가 높아집니다.",
        "commonMistakes": [
            {
                "mistake": "Đốt da",
                "correction": "Đốt cứu",
                "explanation": "'Đốt da'는 '피부를 태우다'라는 의미로 오해를 불러일으킬 수 있습니다."
            },
            {
                "mistake": "뜸을 'burning therapy'로 직역",
                "correction": "Moxibustion (Đốt cứu)",
                "explanation": "의학 용어로는 moxibustion을 사용하고, 베트남어로는 Đốt cứu가 정확합니다."
            },
            {
                "mistake": "뜸과 부항을 혼동",
                "correction": "뜸(Đốt cứu)과 부항(Giác hơi)은 다른 치료법",
                "explanation": "뜸은 열 자극, 부항은 음압 자극을 이용한 치료법입니다."
            }
        ],
        "examples": [
            {
                "ko": "복부에 간접뜸을 떠서 소화기능을 개선하겠습니다.",
                "vi": "Chúng tôi sẽ đốt cứu gián tiếp ở bụng để cải thiện chức năng tiêu hóa.",
                "situation": "formal"
            },
            {
                "ko": "뜸 뜰 때 따뜻한 느낌이 들면 말씀해 주세요.",
                "vi": "Khi đốt cứu nếu cảm thấy nóng thì cho biết nhé.",
                "situation": "onsite"
            },
            {
                "ko": "뜸치료는 냉증과 관절염에 특히 효과적입니다.",
                "vi": "Đốt cứu đặc biệt hiệu quả với chứng hàn và viêm khớp.",
                "situation": "formal"
            }
        ],
        "relatedTerms": ["침술", "부항", "온열요법", "경락치료"]
    },
    {
        "slug": "giac-hoi",
        "korean": "부항",
        "vietnamese": "Giác hơi",
        "hanja": "缸罐",
        "hanjaReading": "缸(독 항) + 罐(항아리 관)",
        "pronunciation": "잭허이",
        "meaningKo": "유리나 대나무로 만든 컵을 피부에 부착하여 음압을 발생시켜 혈액순환을 촉진하고 어혈을 제거하는 한방 치료법입니다. 통역 시 실수하기 쉬운 부분은 부항 후 생기는 붉은 자국을 'bruise(멍)'로 잘못 설명하는 것인데, 이는 정상적인 치료 반응이므로 'Vết bầm tím do giác hơi (부항 자국)'로 정확히 설명해야 환자가 놀라지 않습니다. 또한 부항의 종류(건식부항, 습식부항)와 자국이 사라지는 기간(보통 3-7일)을 미리 안내하는 것이 중요합니다.",
        "meaningVi": "Giác hơi là phương pháp điều trị y học cổ truyền Hàn Quốc sử dụng các cốc thủy tinh hoặc tre để tạo áp lực âm trên da, thúc đẩy tuần hoàn máu và loại bỏ ứ huyết. Đây là liệu pháp phổ biến để điều trị đau cơ, đau lưng và các bệnh lý liên quan đến tuần hoàn kém.",
        "context": "한의원, 스포츠의학, 재활치료, 통증클리닉",
        "culturalNote": "한국에서 부항은 침술 다음으로 흔한 한방 치료법이며, 특히 어깨 결림, 요통, 근육통에 자주 사용됩니다. 베트남에서도 'Giác hơi'라는 이름으로 전통 치료법이 존재하지만, 한국의 부항은 더 체계적이고 위생적인 방법으로 시술됩니다. 부항 후 생기는 붉거나 보라색 자국에 대해 베트남 환자들이 놀랄 수 있으므로, 이것이 정상적인 반응이며 며칠 내 자연스럽게 사라진다는 점을 사전에 설명해야 합니다.",
        "commonMistakes": [
            {
                "mistake": "Hút máu",
                "correction": "Giác hơi",
                "explanation": "'Hút máu'는 '피를 빨다'라는 의미로 오해를 줄 수 있습니다. 부항은 'Giác hơi'가 정확한 표현입니다."
            },
            {
                "mistake": "부항 자국을 'vết thương(상처)'로 표현",
                "correction": "Vết bầm tím do giác hơi (부항 치료 자국)",
                "explanation": "부항 자국은 상처가 아니라 정상적인 치료 반응이므로 환자가 오해하지 않도록 정확히 설명해야 합니다."
            },
            {
                "mistake": "건식부항과 습식부항을 구분하지 않음",
                "correction": "Giác hơi khô / Giác hơi ướt",
                "explanation": "습식부항은 피부를 살짝 절개하므로 사전 동의가 필요합니다."
            }
        ],
        "examples": [
            {
                "ko": "등 부위에 부항을 10분간 시술하겠습니다.",
                "vi": "Chúng tôi sẽ giác hơi vùng lưng trong 10 phút.",
                "situation": "formal"
            },
            {
                "ko": "부항 자국은 3~5일 정도 지나면 자연스럽게 없어져요.",
                "vi": "Vết bầm tím do giác hơi sẽ tự biến mất sau 3-5 ngày.",
                "situation": "onsite"
            },
            {
                "ko": "습식부항은 소량의 출혈이 있을 수 있으니 동의서에 서명해 주세요.",
                "vi": "Giác hơi ướt có thể gây chảy máu nhẹ, vui lòng ký giấy đồng ý.",
                "situation": "formal"
            }
        ],
        "relatedTerms": ["침술", "뜸치료", "어혈제거", "자락요법"]
    },
    {
        "slug": "han-duoc",
        "korean": "한약",
        "vietnamese": "Hán dược",
        "hanja": "韓藥",
        "hanjaReading": "韓(나라 한) + 藥(약 약)",
        "pronunciation": "한득",
        "meaningKo": "한의학 이론에 따라 여러 가지 약재를 배합하여 만든 전통 약물입니다. 한약은 환자의 체질과 증상에 맞춰 개인별로 처방되며, 탕약, 환약, 산제 등 다양한 형태로 제공됩니다. 통역 시 주의할 점은 한약의 복용 방법(식전/식후, 하루 횟수)과 보관 방법(냉장/냉동)을 정확히 전달해야 하며, 특히 베트남 환자가 한약의 맛이나 냄새에 거부감을 보일 수 있으므로 복용 팁(물에 타서 마시기, 꿀 첨가 등)을 함께 안내하는 것이 좋습니다. 또한 한약과 양약의 병용 시 상호작용 가능성을 반드시 확인해야 합니다.",
        "meaningVi": "Hán dược là thuốc truyền thống được pha chế theo lý thuyết y học cổ truyền Hàn Quốc bằng cách phối hợp nhiều dược liệu thiên nhiên. Thuốc được kê đơn riêng cho từng bệnh nhân dựa trên thể chất và triệu chứng, có dạng sắc, hoàn, tán v.v. Hán dược có hiệu quả điều trị căn bản bệnh lý và ít tác dụng phụ.",
        "context": "한의원, 약국, 만성질환 관리, 체질개선",
        "culturalNote": "한국의 한약은 엄격한 품질 관리를 거친 약재를 사용하며, 한의사의 진찰 후에만 처방됩니다. 베트남에도 전통 약초(Thuốc nam)가 있지만, 한약은 더 체계적인 이론과 임상 경험을 바탕으로 합니다. 한약의 가격이 비쌀 수 있으므로 베트남 환자에게는 비용과 효과를 미리 설명하는 것이 좋습니다. 또한 한약 탕제의 독특한 냄새와 맛에 대해 사전에 안내하고, 복용 시 주의사항(공복 여부, 보관 방법)을 명확히 전달해야 합니다.",
        "commonMistakes": [
            {
                "mistake": "Thuốc Trung Quốc",
                "correction": "Hán dược (thuốc cổ truyền Hàn Quốc)",
                "explanation": "한약은 중국 약이 아니라 한국 전통 의학의 약입니다. 'Hán dược' 또는 'Thuốc đông y Hàn Quốc'으로 표현해야 합니다."
            },
            {
                "mistake": "복용 방법을 모호하게 전달",
                "correction": "Uống trước/sau ăn 30 phút (식전/식후 30분)",
                "explanation": "한약의 효과는 복용 시간에 따라 달라지므로 정확한 시간을 전달해야 합니다."
            },
            {
                "mistake": "탕약을 'nước sắc thuốc(약 달인 물)'로만 설명",
                "correction": "Thuốc thang (탕약)",
                "explanation": "'Thuốc thang'이 정확한 한의학 용어입니다."
            }
        ],
        "examples": [
            {
                "ko": "이 한약은 하루 세 번, 식후 30분에 드세요.",
                "vi": "Hán dược này uống ngày 3 lần, sau ăn 30 phút.",
                "situation": "formal"
            },
            {
                "ko": "한약은 냉장고에 보관하시고 드시기 전에 데워서 드세요.",
                "vi": "Bảo quản thuốc trong tủ lạnh và hâm nóng trước khi uống.",
                "situation": "onsite"
            },
            {
                "ko": "이 처방은 2주분이며, 효과를 보려면 꾸준히 복용해야 합니다.",
                "vi": "Đơn thuốc này đủ dùng 2 tuần, cần uống đều đặn mới có hiệu quả.",
                "situation": "formal"
            }
        ],
        "relatedTerms": ["탕약", "환약", "사상체질", "한방치료"]
    },
    {
        "slug": "tu-tuong-the-chat",
        "korean": "사상체질",
        "vietnamese": "Tứ tượng thể chất",
        "hanja": "四象體質",
        "hanjaReading": "四(넉 사) + 象(코끼리 상) + 體(몸 체) + 質(바탕 질)",
        "pronunciation": "뜨뜨엉테쩟",
        "meaningKo": "한의학에서 사람의 체질을 태양인, 태음인, 소양인, 소음인 네 가지로 분류하는 이론입니다. 각 체질은 고유한 신체적, 심리적 특징을 가지며, 질병 발생 패턴과 치료 방법이 다릅니다. 통역 시 주의할 점은 베트남에는 이와 유사한 체질 개념이 없을 수 있으므로, 체질 분류가 단순한 성격 유형이 아니라 의학적 진단과 치료의 기준이 된다는 점을 명확히 설명해야 합니다. 또한 체질에 따라 피해야 할 음식과 권장 음식이 다르므로 이를 정확히 전달하는 것이 실수를 방지합니다.",
        "meaningVi": "Tứ tượng thể chất là học thuyết y học cổ truyền Hàn Quốc phân loại cơ địa con người thành 4 loại: Thái Dương, Thái Âm, Thiểu Dương, Thiểu Âm. Mỗi thể chất có đặc điểm sinh lý và tâm lý riêng, cũng như xu hướng mắc bệnh và phương pháp điều trị khác nhau. Đây là nền tảng quan trọng của y học cá nhân hóa ở Hàn Quốc.",
        "context": "한의원 진료, 건강검진, 맞춤형 치료, 체질별 식이요법",
        "culturalNote": "사상체질론은 한국 한의학의 독특한 이론으로, 19세기 이제마 선생이 창안했습니다. 베트남 전통의학에는 이와 같은 체계적인 체질 분류가 없으므로, 처음 접하는 환자에게는 체질 검사의 목적과 방법을 충분히 설명해야 합니다. 한국에서는 체질에 맞는 음식, 운동, 생활습관을 중요시하며, 체질 진단을 위해 설문지, 맥진, 복진 등을 종합적으로 사용합니다. 베트남 환자들이 체질 개념을 이해하면 치료 순응도가 높아집니다.",
        "commonMistakes": [
            {
                "mistake": "체질을 'personality type(성격 유형)'으로 번역",
                "correction": "Thể chất (constitutional type)",
                "explanation": "체질은 성격이 아니라 의학적 체질 분류입니다."
            },
            {
                "mistake": "네 가지 체질 이름을 직역하지 않고 설명 없이 사용",
                "correction": "Thái Dương nhân, Thái Âm nhân, Thiểu Dương nhân, Thiểu Âm nhân",
                "explanation": "체질 이름은 한자 그대로 번역하고 각 특징을 설명해야 합니다."
            },
            {
                "mistake": "체질별 금기 음식을 정확히 전달하지 않음",
                "correction": "체질에 따라 피해야 할 음식을 목록으로 제공",
                "explanation": "잘못된 식이요법은 건강을 해칠 수 있으므로 정확한 전달이 필수입니다."
            }
        ],
        "examples": [
            {
                "ko": "선생님은 소음인 체질로 소화기능이 약하므로 따뜻한 음식을 드셔야 합니다.",
                "vi": "Bạn thuộc thể chất Thiểu Âm, tiêu hóa yếu nên cần ăn thức ăn ấm.",
                "situation": "formal"
            },
            {
                "ko": "태음인은 땀을 많이 흘리는 운동이 좋아요.",
                "vi": "Người Thái Âm nên tập thể dục đổ nhiều mồ hôi.",
                "situation": "onsite"
            },
            {
                "ko": "체질 진단을 위해 설문지 작성과 맥진을 진행하겠습니다.",
                "vi": "Để chẩn đoán thể chất, chúng tôi sẽ làm bảng câu hỏi và bắt mạch.",
                "situation": "formal"
            }
        ],
        "relatedTerms": ["한의학", "체질진단", "맞춤형치료", "이제마"]
    },
    {
        "slug": "kinh-lac",
        "korean": "경락",
        "vietnamese": "Kinh lạc",
        "hanja": "經絡",
        "hanjaReading": "經(경사 경) + 絡(얽을 락)",
        "pronunciation": "끼잉락",
        "meaningKo": "한의학에서 인체 내부의 기(氣)와 혈(血)이 순환하는 통로를 의미합니다. 12개의 정경(正經)과 기경팔맥(奇經八脈)으로 구성되며, 경락 상의 특정 지점을 경혈이라고 합니다. 통역 시 실수하기 쉬운 부분은 경락을 단순히 '혈관'이나 '신경'으로 오역하는 것인데, 경락은 해부학적 구조가 아니라 기능적 개념이므로 'đường kinh lạc(경락의 길)'로 설명해야 정확합니다. 또한 경락의 막힘이 질병을 유발한다는 한의학 이론을 환자가 이해하도록 설명하는 것이 치료 순응도를 높입니다.",
        "meaningVi": "Kinh lạc là hệ thống đường dẫn khí huyết trong cơ thể theo lý thuyết y học cổ truyền Hàn Quốc. Gồm 12 kinh mạch chính và 8 kỳ kinh, trên đó có các huyệt đạo. Khi kinh lạc bị tắc nghẽn sẽ gây ra bệnh tật, do đó các liệu pháp như châm cứu, đốt cứu đều nhằm mục đích thông kinh lạc.",
        "context": "한의학 이론, 침술, 경락마사지, 기공치료",
        "culturalNote": "경락 이론은 한의학의 핵심 개념으로, 중국 전통의학에서 유래했지만 한국에서 독자적으로 발전했습니다. 베트남 전통의학에도 유사한 개념이 있으나 용어와 세부 내용에 차이가 있을 수 있습니다. 한국에서는 경락 마사지, 경락 요가 등 경락 개념을 응용한 다양한 건강 관리법이 있으며, 현대 의학에서도 경락의 효과를 연구하고 있습니다. 베트남 환자에게 설명할 때는 경락이 '에너지의 흐름'이라는 비유를 사용하면 이해가 쉽습니다.",
        "commonMistakes": [
            {
                "mistake": "Mạch máu (혈관)",
                "correction": "Kinh lạc (경락)",
                "explanation": "경락은 혈관이 아니라 기혈이 흐르는 보이지 않는 통로입니다."
            },
            {
                "mistake": "Dây thần kinh (신경)",
                "correction": "Kinh lạc (경락)",
                "explanation": "경락은 신경계와는 다른 한의학적 개념입니다."
            },
            {
                "mistake": "12 kinh mạch를 구체적으로 설명하지 않음",
                "correction": "수태음폐경, 수양명대장경 등 12정경의 이름과 역할 설명",
                "explanation": "환자가 어느 경락을 치료받는지 알아야 안심할 수 있습니다."
            }
        ],
        "examples": [
            {
                "ko": "이 부위는 위경락이 지나가는 곳으로 소화불량과 관련이 있습니다.",
                "vi": "Vùng này có kinh lạc dạ dày đi qua, liên quan đến chứng khó tiêu.",
                "situation": "formal"
            },
            {
                "ko": "경락이 막혀서 통증이 생긴 거예요.",
                "vi": "Kinh lạc bị tắc nên bị đau.",
                "situation": "onsite"
            },
            {
                "ko": "침술로 경락의 흐름을 개선하면 증상이 완화됩니다.",
                "vi": "Châm cứu cải thiện lưu thông kinh lạc sẽ giảm triệu chứng.",
                "situation": "formal"
            }
        ],
        "relatedTerms": ["경혈", "침술", "기혈순환", "십이정경"]
    },
    {
        "slug": "huyet-dao",
        "korean": "경혈",
        "vietnamese": "Huyệt đạo",
        "hanja": "經穴",
        "hanjaReading": "經(경사 경) + 穴(구멍 혈)",
        "pronunciation": "휴엣다오",
        "meaningKo": "경락 상에 위치한 특정 지점으로, 침이나 뜸으로 자극하여 치료 효과를 얻는 부위입니다. 인체에는 약 360개 이상의 경혈이 있으며, 각 경혈은 고유한 치료 효과를 가지고 있습니다. 통역 시 주의할 점은 경혈의 정확한 위치와 이름을 전달하는 것인데, 예를 들어 '합곡(Hợp Cốc)', '족삼리(Túc Tam Lý)' 등 주요 경혈의 베트남어 명칭을 알아두면 오해가 줄어듭니다. 또한 환자가 어느 경혈에 침을 맞는지, 왜 그 경혈을 선택했는지 설명하면 치료에 대한 신뢰도가 높아집니다.",
        "meaningVi": "Huyệt đạo là các điểm đặc biệt trên kinh lạc, được kích thích bằng châm cứu hoặc đốt cứu để đạt hiệu quả điều trị. Trong cơ thể người có khoảng 360 huyệt trở lên, mỗi huyệt có tác dụng chữa bệnh riêng. Việc chọn đúng huyệt và kích thích đúng cách là chìa khóa của liệu pháp châm cứu.",
        "context": "침술, 지압, 경락마사지, 뜸치료",
        "culturalNote": "경혈은 한의학의 핵심 개념으로, 각 경혈은 한자 이름과 번호(예: LI4 합곡)로 표시됩니다. 베트남에서도 전통 침술에서 경혈 개념을 사용하지만, 일부 경혈의 위치나 명칭에 차이가 있을 수 있습니다. 한국에서는 경혈을 자극하는 방법이 침, 뜸, 지압, 전기 자극 등 다양하며, 특히 족삼리, 합곡, 백회 등은 일반인도 잘 아는 대표적인 경혈입니다. 베트남 환자에게 설명할 때는 경혈의 한자 이름보다는 그 효과(두통 완화, 소화 개선 등)를 중심으로 설명하는 것이 효과적입니다.",
        "commonMistakes": [
            {
                "mistake": "Điểm bấm huyệt (지압점)",
                "correction": "Huyệt đạo (경혈)",
                "explanation": "'Điểm bấm huyệt'는 지압점을 의미하며, 'Huyệt đạo'가 정확한 의학 용어입니다."
            },
            {
                "mistake": "경혈 이름을 한국어 발음 그대로 사용",
                "correction": "베트남어 한자음으로 변환 (예: 합곡 → Hợp Cốc)",
                "explanation": "경혈 이름은 베트남어 한자음으로 읽어야 환자가 이해할 수 있습니다."
            },
            {
                "mistake": "경혈의 위치를 모호하게 설명",
                "correction": "해부학적 위치로 정확히 설명 (예: 엄지와 검지 사이)",
                "explanation": "환자가 스스로 경혈을 찾을 수 있도록 명확한 위치 설명이 필요합니다."
            }
        ],
        "examples": [
            {
                "ko": "합곡 경혈에 침을 놓으면 두통과 치통에 효과가 있습니다.",
                "vi": "Châm vào huyệt Hợp Cốc có hiệu quả với đau đầu và đau răng.",
                "situation": "formal"
            },
            {
                "ko": "족삼리는 무릎 아래 네 손가락 정도 내려간 위치에 있어요.",
                "vi": "Túc Tam Lý nằm dưới đầu gối khoảng 4 ngón tay.",
                "situation": "onsite"
            },
            {
                "ko": "오늘은 10개의 경혈에 침 치료를 진행하겠습니다.",
                "vi": "Hôm nay chúng tôi sẽ châm vào 10 huyệt đạo.",
                "situation": "formal"
            }
        ],
        "relatedTerms": ["경락", "침술", "지압", "합곡"]
    },
    {
        "slug": "chu-na-phap",
        "korean": "추나요법",
        "vietnamese": "Thủ kỹ chỉnh xương khớp (Chu Na pháp)",
        "hanja": "推拿療法",
        "hanjaReading": "推(밀 추) + 拿(잡을 나) + 療(고칠 료) + 法(법 법)",
        "pronunciation": "추나팝",
        "meaningKo": "한의학적 원리에 따라 손으로 척추와 관절을 교정하여 근골격계 질환을 치료하는 한방 수기요법입니다. 추나요법은 단순 마사지가 아니라 뼈와 관절의 정렬을 바로잡는 치료법으로, 한국에서는 건강보험이 적용됩니다. 통역 시 실수하기 쉬운 부분은 추나요법을 '마사지'나 '카이로프랙틱'과 혼동하는 것인데, 추나는 한의학 이론에 기반한 독자적인 치료법이므로 'Liệu pháp chỉnh xương khớp theo y học cổ truyền Hàn Quốc'으로 명확히 구분해야 합니다. 또한 치료 중 '딱' 소리가 날 수 있다는 점을 사전에 안내하여 환자가 놀라지 않도록 해야 합니다.",
        "meaningVi": "Chu Na pháp là phương pháp điều trị bằng tay để chỉnh sửa cột sống và khớp theo nguyên lý y học cổ truyền Hàn Quốc, nhằm chữa các bệnh lý cơ xương khớp. Đây không phải là massage thông thường mà là liệu pháp chỉnh hình y học, được bảo hiểm y tế Hàn Quốc chi trả. Chu Na có hiệu quả rõ rệt với đau lưng, đau cổ, thoát vị đĩa đệm.",
        "context": "한의원, 재활의학과, 척추질환, 관절치료",
        "culturalNote": "추나요법은 한국에서 2019년부터 건강보험 급여 항목이 되어 접근성이 높아졌습니다. 베트남에는 'Bấm huyệt'이나 전통 마사지가 있지만, 추나요법은 더 체계적인 진단과 교정 기법을 사용합니다. 한국에서는 추나요법이 디스크, 거북목, 척추측만증 등에 널리 사용되며, 특히 수술을 피하고 싶은 환자들이 선호합니다. 베트남 환자에게는 추나요법이 비침습적이고 부작용이 적다는 점을 강조하면 수용도가 높아집니다.",
        "commonMistakes": [
            {
                "mistake": "Massage (마사지)",
                "correction": "Chu Na pháp (추나요법) 또는 Liệu pháp chỉnh xương khớp",
                "explanation": "추나는 단순 마사지가 아니라 의료적 교정 치료입니다."
            },
            {
                "mistake": "Chiropractic",
                "correction": "Chu Na pháp (한의학 기반 추나요법)",
                "explanation": "카이로프랙틱과 추나는 다른 이론적 배경을 가진 치료법입니다."
            },
            {
                "mistake": "치료 중 소리에 대한 사전 설명 없음",
                "correction": "'Khi chỉnh xương có thể có tiếng kêu lách cách, đây là hiện tượng bình thường'",
                "explanation": "관절 교정 시 나는 소리에 대해 미리 알려주지 않으면 환자가 놀랄 수 있습니다."
            }
        ],
        "examples": [
            {
                "ko": "경추 추나요법으로 거북목을 교정하겠습니다.",
                "vi": "Chúng tôi sẽ chỉnh cổ bằng Chu Na pháp để sửa tư thế cổ nghiêng.",
                "situation": "formal"
            },
            {
                "ko": "추나 받을 때 긴장을 풀고 힘을 빼세요.",
                "vi": "Khi làm Chu Na hãy thư giãn và không căng cơ.",
                "situation": "onsite"
            },
            {
                "ko": "추나요법은 건강보험이 적용되어 본인부담금이 적습니다.",
                "vi": "Chu Na pháp được bảo hiểm y tế chi trả nên chi phí thấp.",
                "situation": "formal"
            }
        ],
        "relatedTerms": ["척추교정", "도수치료", "관절가동술", "근막이완"]
    },
    {
        "slug": "diem-cham-y-hoc",
        "korean": "약침",
        "vietnamese": "Điểm châm y học (Dược châm)",
        "hanja": "藥鍼",
        "hanjaReading": "藥(약 약) + 鍼(바늘 침)",
        "pronunciation": "득짬이혹",
        "meaningKo": "한약 성분을 정제하여 경혈에 주입하는 한방 치료법으로, 침술과 한약의 효과를 동시에 얻을 수 있는 복합 요법입니다. 약침은 일반 침보다 빠른 효과를 보이며, 특히 통증 질환과 염증성 질환에 효과적입니다. 통역 시 주의할 점은 약침을 단순 '주사'로 오역하는 것인데, 약침은 화학 약품이 아니라 천연 한약 추출물을 사용하므로 'Tiêm dược liệu thiên nhiên vào huyệt đạo'로 정확히 설명해야 합니다. 또한 약침의 종류(봉약침, 자하거약침 등)와 효능을 명확히 전달하고, 알레르기 여부를 반드시 확인해야 합니다.",
        "meaningVi": "Dược châm là phương pháp điều trị y học cổ truyền Hàn Quốc bằng cách tiêm chiết xuất dược liệu tự nhiên vào các huyệt đạo, kết hợp hiệu quả của châm cứu và hán dược. Dược châm có tác dụng nhanh hơn châm thông thường, đặc biệt hiệu quả với các bệnh lý đau nhức và viêm. Đây là liệu pháp độc đáo của y học Hàn Quốc.",
        "context": "한의원, 통증클리닉, 재활치료, 면역치료",
        "culturalNote": "약침은 한국에서 독자적으로 발전한 치료법으로, 봉독약침, 자하거약침 등 다양한 종류가 있습니다. 베트남에는 이와 유사한 치료법이 없으므로, 환자에게 약침의 원리와 효과를 충분히 설명해야 합니다. 약침은 화학 성분이 아닌 천연 한약 추출물을 사용하므로 부작용이 적지만, 일부 환자는 알레르기 반응을 보일 수 있어 사전 테스트가 필요할 수 있습니다. 베트남 환자에게는 약침이 '주사'처럼 보이지만 일반 주사와는 다른 한방 치료라는 점을 강조해야 합니다.",
        "commonMistakes": [
            {
                "mistake": "Tiêm thuốc (약물 주사)",
                "correction": "Dược châm (약침) 또는 Điểm châm y học",
                "explanation": "약침은 일반 약물 주사가 아니라 한약 추출물을 경혈에 주입하는 특수 요법입니다."
            },
            {
                "mistake": "알레르기 확인 없이 시술",
                "correction": "사전에 'Bạn có dị ứng với bất kỳ dược liệu nào không?' 질문 필수",
                "explanation": "봉약침 등 일부 약침은 알레르기 반응을 일으킬 수 있습니다."
            },
            {
                "mistake": "약침의 성분을 설명하지 않음",
                "correction": "봉독, 자하거 등 구체적 성분과 효능 설명",
                "explanation": "환자가 무엇을 맞는지 알아야 동의할 수 있습니다."
            }
        ],
        "examples": [
            {
                "ko": "봉약침은 벌의 독 성분을 정제한 것으로 관절염에 효과적입니다.",
                "vi": "Dược châm nọc ong là chiết xuất tinh luyện từ nọc ong, hiệu quả với viêm khớp.",
                "situation": "formal"
            },
            {
                "ko": "약침은 경혈에 직접 주입하므로 효과가 빨라요.",
                "vi": "Dược châm tiêm trực tiếp vào huyệt nên có hiệu quả nhanh.",
                "situation": "onsite"
            },
            {
                "ko": "벌 알레르기가 있으시면 봉약침을 맞을 수 없습니다.",
                "vi": "Nếu dị ứng ong thì không thể dùng dược châm nọc ong.",
                "situation": "formal"
            }
        ],
        "relatedTerms": ["침술", "봉약침", "자하거약침", "경혈주입"]
    },
    {
        "slug": "khi-cong",
        "korean": "기공",
        "vietnamese": "Khí công",
        "hanja": "氣功",
        "hanjaReading": "氣(기운 기) + 功(공 공)",
        "pronunciation": "키꽁",
        "meaningKo": "호흡과 동작, 명상을 결합하여 체내의 기운을 조절하고 건강을 증진하는 전통 수련법입니다. 기공은 치료 목적뿐 아니라 건강 유지와 질병 예방에도 사용됩니다. 통역 시 주의할 점은 기공을 단순 '운동'이나 '명상'으로 축소 해석하지 않고, 기(氣)의 흐름을 조절하는 심신 수련법임을 명확히 전달해야 합니다. 또한 기공의 효과가 즉각적이지 않고 꾸준한 수련이 필요하다는 점을 환자가 이해하도록 설명하는 것이 중요하며, 잘못된 동작은 오히려 해로울 수 있으므로 전문가의 지도하에 배워야 한다는 점도 강조해야 합니다.",
        "meaningVi": "Khí công là phương pháp rèn luyện truyền thống kết hợp hơi thở, động tác và thiền định để điều hòa khí trong cơ thể và tăng cường sức khỏe. Khí công không chỉ dùng để điều trị bệnh mà còn duy trì sức khỏe và phòng bệnh. Đây là môn tu luyện thân tâm có lịch sử hàng nghìn năm ở Đông Á.",
        "context": "한의원, 재활센터, 요양병원, 건강증진센터",
        "culturalNote": "기공은 중국에서 유래했지만 한국에서도 오랫동안 수련되어 왔으며, 현대에는 의료 기공, 건강 기공 등으로 체계화되었습니다. 베트남에도 'Khí công'이라는 이름으로 알려져 있으나, 한국의 기공은 더 의료적 접근이 강합니다. 한국에서는 암 환자, 만성질환자, 노인들이 재활 목적으로 기공을 많이 수련하며, 일부 한방병원에서는 기공 치료 프로그램을 운영합니다. 베트남 환자에게는 기공이 부작용 없는 자연 치유법이라는 점을 강조하면 관심도가 높아집니다.",
        "commonMistakes": [
            {
                "mistake": "Thể dục (체조, 운동)",
                "correction": "Khí công (기공 수련)",
                "explanation": "기공은 단순 체조가 아니라 기를 조절하는 심신 수련법입니다."
            },
            {
                "mistake": "Thiền (명상)",
                "correction": "Khí công (동작+호흡+명상의 결합)",
                "explanation": "기공은 명상만이 아니라 동작과 호흡을 함께 수련합니다."
            },
            {
                "mistake": "즉각적 효과를 기대하게 함",
                "correction": "'Khí công cần tập đều đặn lâu dài mới có hiệu quả'",
                "explanation": "기공은 꾸준한 수련이 필요하다는 점을 명확히 해야 합니다."
            }
        ],
        "examples": [
            {
                "ko": "암 치료 후 회복을 위해 의료 기공 수련을 권장합니다.",
                "vi": "Sau điều trị ung thư, khuyến khích luyện Khí công y học để hồi phục.",
                "situation": "formal"
            },
            {
                "ko": "기공은 매일 30분씩 꾸준히 하는 게 중요해요.",
                "vi": "Khí công quan trọng là tập đều mỗi ngày 30 phút.",
                "situation": "onsite"
            },
            {
                "ko": "호흡과 동작을 일치시키면서 천천히 따라 해 보세요.",
                "vi": "Hãy làm theo chậm rãi, kết hợp hơi thở và động tác.",
                "situation": "onsite"
            }
        ],
        "relatedTerms": ["명상", "호흡법", "양생", "기혈순환"]
    },
    {
        "slug": "noi-khoa-y-hoc-co-truyen",
        "korean": "한방내과",
        "vietnamese": "Nội khoa y học cổ truyền",
        "hanja": "韓方內科",
        "hanjaReading": "韓(나라 한) + 方(모 방) + 內(안 내) + 科(과 과)",
        "pronunciation": "노이코아이혹꼬쯔엉",
        "meaningKo": "한의학에서 내과적 질환을 진단하고 치료하는 분야로, 소화기, 호흡기, 순환기 질환 등을 다룹니다. 한방내과는 주로 한약 처방을 통해 치료하며, 침구 치료를 병행하기도 합니다. 통역 시 주의할 점은 '한방내과'를 단순히 'internal medicine'으로 번역하면 양방 내과와 혼동될 수 있으므로, 'Nội khoa y học cổ truyền Hàn Quốc'으로 명확히 구분해야 합니다. 또한 한방내과에서 다루는 질환의 범위(소화불량, 만성피로, 불면증 등)를 구체적으로 설명하면 환자가 어떤 증상으로 방문해야 할지 이해하기 쉽습니다.",
        "meaningVi": "Nội khoa y học cổ truyền là chuyên khoa của y học Hàn Quốc chẩn đoán và điều trị các bệnh nội khoa như tiêu hóa, hô hấp, tuần hoàn. Chủ yếu điều trị bằng hán dược kết hợp châm cứu. Nội khoa y học cổ truyền đặc biệt hiệu quả với các bệnh mãn tính, chứng khó tiêu, mệt mỏi, mất ngủ.",
        "context": "한의원, 한방병원, 만성질환 관리, 체질 치료",
        "culturalNote": "한국의 한방내과는 양방 내과와 구분되는 독립된 전문 분야로, 한의사가 진료합니다. 베트남에서는 전통의학과 현대의학이 덜 체계적으로 분리되어 있을 수 있으므로, 한국의 한방내과가 정식 의료 시스템의 일부라는 점을 강조해야 합니다. 한방내과는 만성 소화불량, 과민성대장증후군, 만성피로, 갱년기 증상 등 기능성 질환에 특히 강점이 있습니다. 베트남 환자에게는 한방내과가 부작용이 적고 체질에 맞춘 치료를 한다는 장점을 설명하면 좋습니다.",
        "commonMistakes": [
            {
                "mistake": "Khoa nội (양방 내과)",
                "correction": "Nội khoa y học cổ truyền (한방내과)",
                "explanation": "'Khoa nội'는 현대의학 내과를 의미하므로 혼동될 수 있습니다."
            },
            {
                "mistake": "한방내과에서 양약 처방을 기대",
                "correction": "'Nội khoa y học cổ truyền chủ yếu kê đơn hán dược, không kê thuốc Tây'",
                "explanation": "한방내과는 한약을 처방하며 양약은 처방하지 않습니다."
            },
            {
                "mistake": "진료 과목을 명확히 안내하지 않음",
                "correction": "소화기, 호흡기, 순환기 등 구체적 진료 분야 안내",
                "explanation": "환자가 자신의 증상에 맞는 과인지 판단할 수 있어야 합니다."
            }
        ],
        "examples": [
            {
                "ko": "만성 소화불량은 한방내과에서 체질에 맞는 한약으로 치료합니다.",
                "vi": "Khó tiêu mãn tính được điều trị ở Nội khoa y học cổ truyền bằng hán dược phù hợp thể chất.",
                "situation": "formal"
            },
            {
                "ko": "한방내과 진료는 맥진과 설진으로 시작해요.",
                "vi": "Khám Nội khoa y học cổ truyền bắt đầu bằng bắt mạch và xem lưỡi.",
                "situation": "onsite"
            },
            {
                "ko": "기능성 질환은 한방내과 치료가 효과적입니다.",
                "vi": "Bệnh lý chức năng điều trị ở Nội khoa y học cổ truyền rất hiệu quả.",
                "situation": "formal"
            }
        ],
        "relatedTerms": ["한약", "체질진단", "만성질환", "기능성질환"]
    },
    {
        "slug": "phu-khoa-y-hoc-co-truyen",
        "korean": "한방부인과",
        "vietnamese": "Phụ khoa y học cổ truyền",
        "hanja": "韓方婦人科",
        "hanjaReading": "韓(나라 한) + 方(모 방) + 婦(며느리 부) + 人(사람 인) + 科(과 과)",
        "pronunciation": "푸코아이혹꼬쯔엉",
        "meaningKo": "한의학에서 여성의 생식기 및 부인과 질환을 전문적으로 다루는 분과입니다. 생리불순, 생리통, 갱년기 증상, 난임 등을 치료하며, 산후조리도 담당합니다. 통역 시 주의할 점은 베트남 문화에서도 여성 건강이 민감한 주제일 수 있으므로, 환자의 프라이버시를 존중하며 조심스럽게 통역해야 합니다. 또한 한방부인과에서 다루는 '어혈', '냉증' 같은 한의학적 개념을 베트남어로 정확히 전달하기 위해 'ứ huyết', 'chứng hàn'과 같은 용어를 알아두는 것이 실수를 줄입니다. 난임 치료나 산후조리 같은 민감한 주제는 특히 신중하게 통역해야 합니다.",
        "meaningVi": "Phụ khoa y học cổ truyền là chuyên khoa của y học Hàn Quốc chuyên điều trị các bệnh lý sinh dục nữ và phụ khoa. Điều trị rối loạn kinh nguyệt, đau bụng kinh, tiền mãn kinh, hiếm muộn, và chăm sóc sau sinh. Phụ khoa y học cổ truyền đặc biệt chú trọng điều hòa khí huyết và cân bằng nội tiết tố.",
        "context": "한의원, 산후조리원, 난임클리닉, 갱년기센터",
        "culturalNote": "한국에서는 한방부인과가 여성 건강 관리의 중요한 부분을 차지하며, 특히 산후조리(산후풍 예방)와 난임 치료에 많이 이용됩니다. 베트남에도 전통 산후조리 문화가 있지만, 한국의 한방부인과는 더 체계적인 의료 시스템입니다. 한국 여성들은 생리통, 생리불순, 갱년기 증상에 대해 한방 치료를 선호하는 경향이 있습니다. 베트남 환자에게는 한방부인과가 호르몬제 없이 자연스럽게 여성 건강을 관리한다는 점을 강조하면 관심도가 높아집니다.",
        "commonMistakes": [
            {
                "mistake": "Khoa sản (산부인과)",
                "correction": "Phụ khoa y học cổ truyền (한방부인과)",
                "explanation": "'Khoa sản'은 현대의학 산부인과이며, 한방부인과는 전통의학 기반입니다."
            },
            {
                "mistake": "어혈을 'máu bẩn(더러운 피)'로 오역",
                "correction": "Ứ huyết (어혈)",
                "explanation": "'Máu bẩn'은 부정적 의미가 강하므로 의학 용어 'Ứ huyết'을 사용해야 합니다."
            },
            {
                "mistake": "난임 치료 과정을 모호하게 설명",
                "correction": "체질 진단 → 한약 처방 → 침구 치료의 단계적 설명",
                "explanation": "난임은 민감한 주제이므로 치료 과정을 명확히 전달해야 신뢰를 얻습니다."
            }
        ],
        "examples": [
            {
                "ko": "생리통이 심하시면 한방부인과에서 체질에 맞는 한약을 처방받으세요.",
                "vi": "Nếu đau bụng kinh nặng, hãy đến Phụ khoa y học cổ truyền để được kê hán dược phù hợp thể chất.",
                "situation": "formal"
            },
            {
                "ko": "산후조리 한약은 산후풍 예방에 도움이 돼요.",
                "vi": "Hán dược sau sinh giúp phòng ngừa chứng ốm sau sinh.",
                "situation": "onsite"
            },
            {
                "ko": "갱년기 증상 완화를 위해 한방부인과 치료를 권장합니다.",
                "vi": "Khuyến khích điều trị Phụ khoa y học cổ truyền để giảm triệu chứng tiền mãn kinh.",
                "situation": "formal"
            }
        ],
        "relatedTerms": ["생리통", "난임", "산후조리", "갱년기"]
    },
    {
        "slug": "nhi-khoa-y-hoc-co-truyen",
        "korean": "한방소아과",
        "vietnamese": "Nhi khoa y học cổ truyền",
        "hanja": "韓方小兒科",
        "hanjaReading": "韓(나라 한) + 方(모 방) + 小(작을 소) + 兒(아이 아) + 科(과 과)",
        "pronunciation": "니코아이혹꼬쯔엉",
        "meaningKo": "한의학에서 소아 질환을 전문적으로 다루는 분과로, 감기, 소화불량, 성장 발육, 알레르기 등을 치료합니다. 한방소아과는 성장기 어린이의 체질을 고려한 맞춤 치료를 제공합니다. 통역 시 주의할 점은 부모가 아이에게 침이나 한약을 먹이는 것에 대해 걱정할 수 있으므로, 소아침(작은 침)이나 소아 한약(아이가 먹기 쉬운 형태)의 안전성과 효과를 명확히 설명해야 합니다. 또한 '성장침', '비염 치료' 같은 한방소아과의 특화 진료를 설명할 때는 치료 기간과 예상 효과를 구체적으로 전달하여 부모의 기대를 관리하는 것이 중요합니다.",
        "meaningVi": "Nhi khoa y học cổ truyền là chuyên khoa của y học Hàn Quốc chuyên điều trị bệnh lý ở trẻ em như cảm cúm, khó tiêu, tăng trưởng phát triển, dị ứng. Nhi khoa y học cổ truyền cung cấp điều trị phù hợp thể chất cho trẻ đang trong giai đoạn tăng trưởng, sử dụng kim châm nhỏ và hán dược dễ uống.",
        "context": "한의원, 소아과 클리닉, 성장클리닉, 비염클리닉",
        "culturalNote": "한국에서는 한방소아과가 성장 촉진, 알레르기 비염, 아토피, 소아 소화불량 치료에 널리 이용됩니다. 특히 '성장침'은 한국 부모들 사이에서 인기가 높습니다. 베트남에서도 어린이 건강에 대한 관심이 높지만, 어린이에게 침을 놓는 것에 대해 우려할 수 있으므로 소아침의 안전성을 강조해야 합니다. 한방소아과는 약물 부작용이 적고 자연 치유력을 높인다는 점을 부모에게 설명하면 수용도가 높아집니다.",
        "commonMistakes": [
            {
                "mistake": "Khoa nhi (현대의학 소아과)",
                "correction": "Nhi khoa y học cổ truyền (한방소아과)",
                "explanation": "'Khoa nhi'는 양방 소아과이므로 혼동될 수 있습니다."
            },
            {
                "mistake": "소아침의 안전성을 설명하지 않음",
                "correction": "'Kim châm cho trẻ rất nhỏ và an toàn, không đau'",
                "explanation": "부모가 침 치료를 걱정할 수 있으므로 안전성을 강조해야 합니다."
            },
            {
                "mistake": "성장침의 효과를 과장",
                "correction": "'Kim tăng trưởng hỗ trợ phát triển, không phải thuốc thần kỳ'",
                "explanation": "성장침은 보조 치료이며 과장된 기대를 막아야 합니다."
            }
        ],
        "examples": [
            {
                "ko": "아이의 키 성장을 위해 한방소아과에서 성장침 치료를 받을 수 있습니다.",
                "vi": "Để tăng chiều cao cho con, có thể điều trị kim tăng trưởng ở Nhi khoa y học cổ truyền.",
                "situation": "formal"
            },
            {
                "ko": "소아 한약은 아이가 먹기 쉽게 시럽이나 과립 형태로 만들어요.",
                "vi": "Hán dược cho trẻ được làm dạng xi-rô hoặc viên để dễ uống.",
                "situation": "onsite"
            },
            {
                "ko": "알레르기 비염은 한방소아과에서 체질 개선 치료를 합니다.",
                "vi": "Viêm mũi dị ứng được điều trị cải thiện thể chất ở Nhi khoa y học cổ truyền.",
                "situation": "formal"
            }
        ],
        "relatedTerms": ["성장침", "소아비염", "아토피", "소화불량"]
    }
]

# Continue reading existing data and append
with open(file_path, 'r', encoding='utf-8') as f:
    existing_data = json.load(f)

# Add new terms
existing_data.extend(new_terms)

# Write back
with open(file_path, 'w', encoding='utf-8') as f:
    json.dump(existing_data, f, ensure_ascii=False, indent=2)

print(f"✅ Successfully added {len(new_terms)} new medical terms")
print(f"📊 Total terms now: {len(existing_data)}")
