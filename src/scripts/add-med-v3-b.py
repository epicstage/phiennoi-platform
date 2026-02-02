#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
의료 용어 추가 스크립트 v3-b
20개 안과/이비인후과/피부과 용어 추가 (Tier S 기준)
"""

import json
import os

# 파일 경로 설정
file_path = os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', 'data', 'terms', 'medical.json')

# 기존 데이터 로드
with open(file_path, 'r', encoding='utf-8') as f:
    data = json.load(f)

existing_slugs = {t['slug'] for t in data}

# 새로운 용어 20개 (Tier S 기준)
new_terms = [
    {
        "slug": "duc-thuy-tinh-the",
        "korean": "백내장",
        "vietnamese": "đục thủy tinh thể",
        "hanja": "白內障",
        "hanjaReading": "白(흰 백) + 內(안 내) + 障(막을 장)",
        "pronunciation": "백내장",
        "meaningKo": "눈의 수정체가 혼탁해져 시력이 저하되는 질환. 통역 시 주의할 점은 베트남어로 'đục thủy tinh thể'(수정체 혼탁)와 'cườm mắt'(구어체 표현)를 구분해야 한다는 것입니다. 특히 수술 상담 시 '인공수정체 삽입'을 'cấy thủy tinh thể nhân tạo'로 정확히 번역해야 오해가 없습니다. 베트남에서는 백내장을 노화의 자연스러운 현상으로 여겨 수술을 미루는 경향이 있어, 조기 치료의 중요성을 강조할 때 문화적 차이를 고려해야 합니다.",
        "meaningVi": "Bệnh lý mắt do thủy tinh thể bị đục, làm giảm thị lực. Thường gặp ở người cao tuổi nhưng cũng có thể do chấn thương, tiểu đường hoặc di truyền. Điều trị chủ yếu bằng phẫu thuật thay thủy tinh thể.",
        "context": "안과 외래, 수술 상담, 노인 건강검진",
        "culturalNote": "한국에서는 백내장을 조기에 발견하면 적극적으로 수술을 권하는 반면, 베트남에서는 '시력이 많이 나빠질 때까지' 기다리는 경향이 있습니다. 따라서 통역 시 조기 수술의 이점(회복 빠름, 합병증 적음)을 충분히 설명해야 합니다. 또한 한국의 다초점 인공수정체 개념이 베트남 환자들에게 생소할 수 있어 추가 설명이 필요합니다.",
        "commonMistakes": [
            {
                "mistake": "cườm mắt을 모든 상황에서 사용",
                "correction": "공식 진단은 đục thủy tinh thể 사용",
                "explanation": "cườm mắt은 구어체이며 의료 기록에는 đục thủy tinh thể를 써야 함"
            },
            {
                "mistake": "'수술이 필요하다'를 cần mổ로 직역",
                "correction": "cần phẫu thuật thay thủy tinh thể로 구체화",
                "explanation": "mổ는 너무 일반적이며 환자가 수술 내용을 오해할 수 있음"
            },
            {
                "mistake": "인공수정체를 kính nhân tạo(인공 안경)로 오역",
                "correction": "thủy tinh thể nhân tạo가 정확",
                "explanation": "렌즈와 안경을 혼동하지 않도록 주의"
            }
        ],
        "examples": [
            {
                "ko": "백내장이 진행되어 수술이 필요합니다. 인공수정체를 삽입하는 수술로 회복 기간은 약 2주입니다.",
                "vi": "Đục thủy tinh thể đã tiến triển, cần phẫu thuật cấy thủy tinh thể nhân tạo. Thời gian hồi phục khoảng 2 tuần.",
                "situation": "formal"
            },
            {
                "ko": "현장에서 '앞이 뿌옇게 보인다'고 하시면 백내장 의심해봐야 합니다.",
                "vi": "Tại hiện trường, nếu nói 'nhìn mờ như có màn che' thì nghi ngờ đục thủy tinh thể.",
                "situation": "onsite"
            },
            {
                "ko": "어머니가 백내장 수술 받으셨는데 지금은 잘 보이세요.",
                "vi": "Mẹ tôi đã phẫu thuật đục thủy tinh thể, bây giờ nhìn rõ lắm.",
                "situation": "informal"
            }
        ],
        "relatedTerms": ["녹내장", "황반변성", "당뇨망막병증", "안구건조증"]
    },
    {
        "slug": "tang-nhan-ap",
        "korean": "녹내장",
        "vietnamese": "tăng nhãn áp",
        "hanja": "綠內障",
        "hanjaReading": "綠(푸를 록) + 內(안 내) + 障(막을 장)",
        "pronunciation": "녹내장",
        "meaningKo": "안압 상승으로 시신경이 손상되어 시야가 좁아지는 질환. 통역 시 실수하기 쉬운 점은 'tăng nhãn áp'(안압 상승)을 병명 자체로 오해하는 것인데, 정확히는 'bệnh tăng nhãn áp' 또는 'glôcôm'으로 표현해야 합니다. 한국에서는 조기 발견을 위해 정기 안과 검진을 강조하지만, 베트남에서는 증상이 뚜렷해진 후 내원하는 경우가 많아 통역 시 예방의 중요성을 강조해야 합니다. '실명 위험'을 언급할 때는 환자가 과도하게 불안해하지 않도록 주의가 필요합니다.",
        "meaningVi": "Bệnh lý mắt do tăng áp lực trong nhãn cầu, gây tổn thương dây thần kinh thị giác và thu hẹp thị trường. Nếu không điều trị kịp thời có thể dẫn đến mù vĩnh viễn. Thường không có triệu chứng rõ ràng ở giai đoạn đầu.",
        "context": "안과 진료, 정기 검진, 만성질환 관리",
        "culturalNote": "한국에서는 40세 이상이면 정기적으로 안압을 측정하지만, 베트남에서는 이러한 예방적 검진 문화가 덜 발달했습니다. 따라서 '증상이 없어도 검사 필요'라는 개념을 설명할 때 문화적 차이를 고려해야 합니다. 또한 한국은 녹내장 수술 기술이 발달했으나, 베트남 환자들은 수술에 대한 두려움이 커서 안약 치료를 선호하는 경향이 있습니다.",
        "commonMistakes": [
            {
                "mistake": "tăng nhãn áp만 말하고 병명 생략",
                "correction": "bệnh tăng nhãn áp 또는 glôcôm 명시",
                "explanation": "안압 상승은 증상이지 병명이 아님"
            },
            {
                "mistake": "'실명한다'를 mù로만 표현",
                "correction": "mù vĩnh viễn(영구 실명) 또는 mất thị lực hoàn toàn",
                "explanation": "일시적 시력 저하와 구분 필요"
            },
            {
                "mistake": "시야 협착을 hẹp mắt로 오역",
                "correction": "thu hẹp thị trường(시야 축소)가 정확",
                "explanation": "의학 용어로 정확히 전달해야 함"
            }
        ],
        "examples": [
            {
                "ko": "녹내장은 초기에 증상이 없어 정기 검진이 중요합니다. 안압과 시신경 검사가 필수입니다.",
                "vi": "Bệnh tăng nhãn áp giai đoạn đầu không có triệu chứng nên khám định kỳ rất quan trọng. Cần đo nhãn áp và kiểm tra dây thần kinh thị giác.",
                "situation": "formal"
            },
            {
                "ko": "현장에서 '옆이 안 보인다'고 하면 녹내장 가능성이 있습니다.",
                "vi": "Tại hiện trường, nếu nói 'không nhìn thấy hai bên' thì có khả năng bị tăng nhãn áp.",
                "situation": "onsite"
            },
            {
                "ko": "아버지가 녹내장이라 매일 안약 넣으세요.",
                "vi": "Bố tôi bị tăng nhãn áp nên phải nhỏ thuốc mắt hàng ngày.",
                "situation": "informal"
            }
        ],
        "relatedTerms": ["백내장", "안압측정", "시야검사", "시신경유두"]
    },
    {
        "slug": "thoai-hoa-hoang-diem",
        "korean": "황반변성",
        "vietnamese": "thoái hóa hoàng điểm",
        "hanja": "黃斑變性",
        "hanjaReading": "黃(누를 황) + 斑(얼룩 반) + 變(변할 변) + 性(성품 성)",
        "pronunciation": "황반변성",
        "meaningKo": "망막 중심부인 황반이 손상되어 중심 시력이 저하되는 질환. 통역 시 주의할 점은 'hoàng điểm'을 문자 그대로 '황반'이 아니라 '망막 중심부'로 부연 설명해야 베트남 환자가 이해하기 쉽다는 것입니다. 특히 '건성'과 '습성' 황반변성을 구분할 때, 베트nam어로 'khô'(건성)와 'ướt'(습성)로 표현하되 치료 방법이 완전히 다르다는 점을 강조해야 합니다. 한국에서는 루테인 영양제 복용을 권장하지만, 베트남에서는 이러한 예방적 보충제 개념이 생소할 수 있어 추가 설명이 필요합니다.",
        "meaningVi": "Bệnh lý thoái hóa vùng hoàng điểm ở trung tâm võng mạc, gây giảm thị lực trung tâm. Có hai loại: khô (chiếm 90%) và ướt (nguy hiểm hơn). Thường gặp ở người trên 50 tuổi, liên quan đến tuổi tác và di truyền.",
        "context": "안과 진료, 노인 건강관리, 시력 저하 상담",
        "culturalNote": "한국에서는 황반변성을 노화성 질환으로 인식하고 조기 검진을 강조하지만, 베트남에서는 이 질환에 대한 인지도가 낮아 '중심이 안 보인다'는 증상을 단순 노안으로 오해하는 경우가 많습니다. 따라서 통역 시 황반변성과 노안의 차이를 명확히 설명해야 합니다. 또한 습성 황반변성 치료를 위한 안구 내 주사(anti-VEGF)가 베트남에서는 고가 치료로 인식되어 경제적 부담을 우려하는 환자가 많습니다.",
        "commonMistakes": [
            {
                "mistake": "hoàng điểm만 말하고 võng mạc 생략",
                "correction": "hoàng điểm võng mạc(망막 황반)으로 완전히 표현",
                "explanation": "황반이 망막의 일부임을 명확히 해야 함"
            },
            {
                "mistake": "'중심이 안 보인다'를 không nhìn thấy giữa로 직역",
                "correction": "mất thị lực trung tâm(중심 시력 상실)이 정확",
                "explanation": "의학적으로 정확한 표현 사용 필요"
            },
            {
                "mistake": "습성을 ướt(젖은)로만 표현",
                "correction": "type ướt 또는 thể ướt로 병형 구분",
                "explanation": "병의 유형임을 명확히 해야 함"
            }
        ],
        "examples": [
            {
                "ko": "황반변성은 중심 시력이 떨어지는 질환으로, 습성인 경우 안구 주사 치료가 필요합니다.",
                "vi": "Thoái hóa hoàng điểm làm giảm thị lực trung tâm, nếu là type ướt cần điều trị bằng tiêm nội nhãn.",
                "situation": "formal"
            },
            {
                "ko": "현장에서 '한가운데가 검게 보인다'고 하면 황반변성 의심해야 합니다.",
                "vi": "Tại hiện trường, nếu nói 'nhìn giữa bị đen' thì nghi ngờ thoái hóa hoàng điểm.",
                "situation": "onsite"
            },
            {
                "ko": "할머니가 황반변성이라 루테인 드세요.",
                "vi": "Bà tôi bị thoái hóa hoàng điểm nên uống lutein.",
                "situation": "informal"
            }
        ],
        "relatedTerms": ["망막박리", "당뇨망막병증", "녹내장", "노안"]
    },
    {
        "slug": "kho-mat-nang",
        "korean": "안구건조증",
        "vietnamese": "khô mắt nặng",
        "hanja": "眼球乾燥症",
        "hanjaReading": "眼(눈 안) + 球(공 구) + 乾(마를 건) + 燥(마를 조) + 症(증세 증)",
        "pronunciation": "안구건조증",
        "meaningKo": "눈물 분비 감소나 눈물막 불안정으로 안구 표면이 건조해지는 질환. 통역 시 주의할 점은 베트남어로 단순히 'khô mắt'(눈 마름)이 아니라 'khô mắt nặng' 또는 'hội chứng khô mắt'으로 질환임을 명확히 해야 한다는 것입니다. 특히 '인공눈물'을 'nước mắt nhân tạo'로 번역할 때, 베트남 환자들이 '눈물'과 '안약'을 혼동하지 않도록 'thuốc nhỏ mắt giả nước mắt'로 부연 설명하는 것이 좋습니다. 한국에서는 장시간 컴퓨터 사용이나 콘택트렌즈 착용과 연관 짓지만, 베트남에서는 환경적 요인(먼지, 습도)을 더 중요하게 여기는 경향이 있습니다.",
        "meaningVi": "Hội chứng khô mắt do giảm tiết nước mắt hoặc nước mắt bốc hơi nhanh, gây khô bề mặt nhãn cầu. Triệu chứng: khô rát, cộm, dễ mỏi mắt. Thường gặp ở người dùng máy tính nhiều, đeo kính áp tròng lâu hoặc người cao tuổi.",
        "context": "안과 외래, 직장인 건강관리, 안경원 상담",
        "culturalNote": "한국에서는 안구건조증을 '현대병'으로 인식하고 인공눈물을 일상적으로 사용하지만, 베트남에서는 '눈이 좀 마른 것'으로 가볍게 여겨 치료를 미루는 경향이 있습니다. 따라서 통역 시 만성화 시 각막 손상 위험을 강조해야 합니다. 또한 한국에서는 온열 안대나 눈 마사지 기기를 권장하지만, 베트남에서는 이러한 제품이 생소하여 사용법을 자세히 설명해야 합니다.",
        "commonMistakes": [
            {
                "mistake": "khô mắt으로만 표현",
                "correction": "hội chứng khô mắt 또는 khô mắt nặng으로 질환 명시",
                "explanation": "단순 증상이 아닌 질환임을 분명히 해야 함"
            },
            {
                "mistake": "인공눈물을 nước mắt giả로 직역",
                "correction": "thuốc nhỏ mắt giả nước mắt 또는 nước mắt nhân tạo",
                "explanation": "의약품임을 명확히 해야 함"
            },
            {
                "mistake": "'눈이 뻑뻑하다'를 mắt cứng으로 오역",
                "correction": "mắt khô rát, mắt cộm(건조하고 따끔함)이 적절",
                "explanation": "증상을 정확히 전달해야 함"
            }
        ],
        "examples": [
            {
                "ko": "안구건조증이 심하면 각막에 상처가 날 수 있으니 인공눈물을 자주 사용하세요.",
                "vi": "Nếu khô mắt nặng có thể làm tổn thương giác mạc, nên nhỏ nước mắt nhân tạo thường xuyên.",
                "situation": "formal"
            },
            {
                "ko": "현장에서 '눈이 뻑뻑하고 따갑다'고 하면 안구건조증일 수 있습니다.",
                "vi": "Tại hiện trường, nếu nói 'mắt khô và cộm' thì có thể bị hội chứng khô mắt.",
                "situation": "onsite"
            },
            {
                "ko": "컴퓨터 오래 보면 안구건조증 생겨요. 인공눈물 넣으세요.",
                "vi": "Nhìn máy tính lâu dễ bị khô mắt. Nhỏ nước mắt nhân tạo nhé.",
                "situation": "informal"
            }
        ],
        "relatedTerms": ["각막염", "결막염", "눈물길폐쇄", "안검염"]
    },
    {
        "slug": "viem-ket-mac",
        "korean": "결막염",
        "vietnamese": "viêm kết mạc",
        "hanja": "結膜炎",
        "hanjaReading": "結(맺을 결) + 膜(막 막) + 炎(불꽃 염)",
        "pronunciation": "결막염",
        "meaningKo": "눈의 결막에 염증이 생기는 질환으로 전염성과 비전염성으로 구분됨. 통역 시 주의할 점은 베트남어로 'đau mắt đỏ'(빨간 눈 통증)라는 구어 표현이 널리 쓰이지만, 의료 현장에서는 'viêm kết mạc'을 사용해야 한다는 것입니다. 특히 전염성 결막염(유행성 각결막염)은 'viêm kết mạc truyền nhiễm' 또는 'đau mắt đỏ lây'로 명확히 구분해야 하며, 격리 및 위생 관리의 중요성을 강조해야 합니다. 한국에서는 항생제 안약을 즉시 처방하지만, 베트남에서는 민간요법(차잎으로 씻기 등)을 먼저 시도하는 경우가 많아 적절한 치료 시기를 놓칠 수 있습니다.",
        "meaningVi": "Viêm màng kết mạc phủ bề mặt nhãn cầu và mí mắt. Có thể do vi khuẩn, virus, dị ứng hoặc kích ứng. Triệu chứng: mắt đỏ, ngứa, chảy nước mắt, ghèn. Loại truyền nhiễm lây lan nhanh qua tiếp xúc.",
        "context": "안과 진료, 학교 보건, 직장 건강관리",
        "culturalNote": "한국에서는 결막염을 '유행성 눈병'으로 인식하고 등교·출근 중지 조치를 취하지만, 베트남에서는 '흔한 눈병'으로 여겨 일상생활을 계속하는 경우가 많습니다. 따라서 통역 시 전염 위험과 격리의 필요성을 문화적 맥락에서 설명해야 합니다. 또한 한국에서는 일회용 안약을 선호하지만, 베트남에서는 경제적 이유로 다회용 안약을 여러 사람이 공유하는 경우가 있어 위생 교육이 중요합니다.",
        "commonMistakes": [
            {
                "mistake": "đau mắt đỏ를 모든 상황에서 사용",
                "correction": "의료 기록에는 viêm kết mạc 사용",
                "explanation": "구어체와 의학 용어를 구분해야 함"
            },
            {
                "mistake": "'전염성'을 chỉ lây로만 표현",
                "correction": "truyền nhiễm(전염성) 또는 lây lan(전파)로 명확히",
                "explanation": "의학적으로 정확한 용어 사용 필요"
            },
            {
                "mistake": "'눈곱'을 ghèn mắt으로만 표현",
                "correction": "dịch tiết mắt(눈 분비물)가 의학적으로 정확",
                "explanation": "공식 진료에서는 정확한 용어 사용"
            }
        ],
        "examples": [
            {
                "ko": "바이러스성 결막염은 전염성이 강하므로 2주간 출근하지 마시고 안약을 규칙적으로 넣으세요.",
                "vi": "Viêm kết mạc do virus lây lan mạnh, nên nghỉ làm 2 tuần và nhỏ thuốc mắt đều đặn.",
                "situation": "formal"
            },
            {
                "ko": "현장에서 '눈이 빨갛고 눈곱이 많이 낀다'고 하면 결막염 가능성 높습니다.",
                "vi": "Tại hiện trường, nếu nói 'mắt đỏ và ghèn nhiều' thì khả năng cao bị viêm kết mạc.",
                "situation": "onsite"
            },
            {
                "ko": "애들이 결막염 걸렸는데 학교에서 옮은 것 같아요.",
                "vi": "Các con bị viêm kết mạc, hình như bị lây ở trường.",
                "situation": "informal"
            }
        ],
        "relatedTerms": ["각막염", "안검염", "알레르기결막염", "유행성각결막염"]
    },
    {
        "slug": "phau-thuat-lasik",
        "korean": "라식수술",
        "vietnamese": "phẫu thuật LASIK",
        "hanja": None,
        "hanjaReading": None,
        "pronunciation": "라식수술",
        "meaningKo": "각막을 레이저로 교정하여 근시·난시·원시를 치료하는 시력교정술. 통역 시 주의할 점은 LASIK, LASEK, 스마일라식 등 다양한 수술법을 베트남어로 구분해야 한다는 것입니다. 'phẫu thuật LASIK'은 일반적인 라식, 'phẫu thuật LASEK'은 라섹, 'phẫu thuật SMILE'은 스마일라식으로 각각 표기하되, 각 수술법의 차이(회복 기간, 적합한 각막 두께 등)를 명확히 설명해야 합니다. 한국에서는 라식수술이 대중화되어 있지만, 베트남에서는 여전히 고가 시술로 인식되며 안전성에 대한 우려도 크므로, 수술 성공률과 부작용 관리에 대한 충분한 설명이 필요합니다.",
        "meaningVi": "Phẫu thuật chỉnh hình giác mạc bằng laser để điều trị cận thị, loạn thị, viễn thị. Sử dụng tia laser để tạo hình lại bề mặt giác mạc, giúp ánh sáng hội tụ đúng trên võng mạc. Thời gian hồi phục nhanh, thường 1-2 ngày.",
        "context": "안과 수술 상담, 시력교정 클리닉",
        "culturalNote": "한국에서는 라식수술을 '보편적인 시력교정 방법'으로 인식하고 20대 초반에 받는 경우가 많지만, 베트남에서는 '고급 수술'로 여겨 신중하게 결정합니다. 따라서 통역 시 수술의 장기 안전성과 부작용(안구건조, 야간 빛 번짐 등)을 솔직하게 설명해야 환자의 신뢰를 얻을 수 있습니다. 또한 한국에서는 군 입대 전 라식수술이 일반적이지만, 베트남에서는 이러한 문화가 없어 수술 동기를 이해하는 데 추가 설명이 필요할 수 있습니다.",
        "commonMistakes": [
            {
                "mistake": "모든 시력교정술을 LASIK으로 통칭",
                "correction": "LASIK, LASEK, SMILE 등 정확한 수술명 사용",
                "explanation": "수술 방법에 따라 회복 기간과 부작용이 다름"
            },
            {
                "mistake": "'각막 절삭'을 cắt giác mạc으로 직역",
                "correction": "tạo hình giác mạc(각막 성형)이 더 적절",
                "explanation": "환자가 '자른다'는 표현에 공포를 느낄 수 있음"
            },
            {
                "mistake": "'시력 1.0'을 thị lực 1.0으로 직역",
                "correction": "10/10 또는 100% thị lực로 표현",
                "explanation": "베트남에서는 10점 만점 체계 사용"
            }
        ],
        "examples": [
            {
                "ko": "라식수술 후 일주일간은 눈을 비비지 말고 안약을 규칙적으로 넣으세요. 시력은 1.0 이상으로 회복될 것입니다.",
                "vi": "Sau phẫu thuật LASIK 1 tuần không được dụi mắt, nhỏ thuốc đều đặn. Thị lực sẽ phục hồi lên 10/10 trở lên.",
                "situation": "formal"
            },
            {
                "ko": "현장에서 '수술 후 언제부터 일할 수 있나요?'라고 물으면 보통 2-3일 후 가능하다고 답하세요.",
                "vi": "Tại hiện trường, nếu hỏi 'bao lâu sau phẫu thuật mới đi làm được?' thì trả lời thường 2-3 ngày sau là được.",
                "situation": "onsite"
            },
            {
                "ko": "친구가 라식 받고 안경 벗었는데 너무 편하대.",
                "vi": "Bạn tôi phẫu thuật LASIK rồi bỏ kính, tiện lắm.",
                "situation": "informal"
            }
        ],
        "relatedTerms": ["근시", "난시", "각막두께", "안구건조증"]
    },
    {
        "slug": "viem-tai-giua",
        "korean": "중이염",
        "vietnamese": "viêm tai giữa",
        "hanja": "中耳炎",
        "hanjaReading": "中(가운데 중) + 耳(귀 이) + 炎(불꽃 염)",
        "pronunciation": "중이염",
        "meaningKo": "고막 안쪽의 중이에 염증이 생기는 질환으로 주로 소아에게 발생함. 통역 시 주의할 점은 급성 중이염(viêm tai giữa cấp)과 만성 중이염(viêm tai giữa mãn)을 명확히 구분해야 한다는 것입니다. 특히 '삼출성 중이염'은 'viêm tai giữa tiết dịch'으로 번역하되, 고름이 아닌 액체가 차는 것임을 설명해야 오해가 없습니다. 한국에서는 중이염을 즉시 항생제로 치료하지만, 베트남에서는 귀에 물이 들어가서 생긴다는 민간 믿음이 있어 예방법(감기 치료, 수유 자세 등)을 교육할 때 문화적 차이를 고려해야 합니다.",
        "meaningVi": "Viêm vùng tai giữa phía sau màng nhĩ, thường do vi khuẩn hoặc virus từ họng lan lên qua vòi nhĩ. Hay gặp ở trẻ em do vòi nhĩ ngắn và nằm ngang. Triệu chứng: đau tai, sốt, giảm thính lực, có thể chảy mủ nếu thủng màng nhĩ.",
        "context": "소아과 진료, 이비인후과, 예방접종 상담",
        "culturalNote": "한국에서는 중이염을 '흔한 소아 질환'으로 인식하고 조기에 항생제를 투여하지만, 베트남에서는 '귀에 물 들어간 것'으로 오해하여 귀를 후비거나 민간요법을 시도하는 경우가 많습니다. 따라서 통역 시 중이염의 원인(감기, 상기도 감염)과 적절한 치료법을 설명하고, 고막 천공을 예방하기 위해 조기 치료가 중요함을 강조해야 합니다. 또한 한국에서는 폐렴구균 백신으로 중이염을 예방하지만, 베트남에서는 이 백신이 필수가 아니어서 접종률이 낮습니다.",
        "commonMistakes": [
            {
                "mistake": "'귀에서 고름 나온다'를 tai chảy mủ로만 표현",
                "correction": "thủng màng nhĩ, chảy mủ(고막 천공, 고름 유출)로 구체화",
                "explanation": "고막 손상 여부를 명확히 전달해야 함"
            },
            {
                "mistake": "삼출성 중이염을 viêm tai có mủ로 오역",
                "correction": "viêm tai giữa tiết dịch(액체 저류)가 정확",
                "explanation": "고름과 삼출액을 구분해야 함"
            },
            {
                "mistake": "'귀가 먹먹하다'를 tai tắc으로 직역",
                "correction": "nghe kém, tai nghẹt(청력 저하, 귀 막힘)이 적절",
                "explanation": "증상을 정확히 전달해야 함"
            }
        ],
        "examples": [
            {
                "ko": "아이가 급성 중이염으로 고열과 귀 통증이 있습니다. 항생제를 5일간 복용해야 하고, 고막이 터지지 않도록 주의해야 합니다.",
                "vi": "Bé bị viêm tai giữa cấp, sốt cao và đau tai. Cần uống kháng sinh 5 ngày, chú ý tránh thủng màng nhĩ.",
                "situation": "formal"
            },
            {
                "ko": "현장에서 아이가 '귀가 아프다'고 울면 중이염 가능성이 높으니 바로 병원 가야 합니다.",
                "vi": "Tại hiện trường, nếu bé khóc 'đau tai' thì khả năng cao bị viêm tai giữa, cần đi bệnh viện ngay.",
                "situation": "onsite"
            },
            {
                "ko": "우리 애 감기 걸리면 중이염으로 발전해서 항상 조심해요.",
                "vi": "Con tôi cảm là tiến triển thành viêm tai giữa nên luôn phải cẩn thận.",
                "situation": "informal"
            }
        ],
        "relatedTerms": ["급성중이염", "만성중이염", "삼출성중이염", "고막천공"]
    },
    {
        "slug": "viem-xoang",
        "korean": "부비동염",
        "vietnamese": "viêm xoang",
        "hanja": "副鼻洞炎",
        "hanjaReading": "副(버금 부) + 鼻(코 비) + 洞(골 동) + 炎(불꽃 염)",
        "pronunciation": "부비동염",
        "meaningKo": "코 주변 얼굴뼈 속 공간인 부비동에 염증이 생기는 질환으로 급성과 만성으로 구분됨. 통역 시 주의할 점은 베트남어로 'viêm xoang'이 일반적이지만, 구어로는 'viêm mũi xoang'(콧속 염증)이라고도 하므로 상황에 맞게 사용해야 한다는 것입니다. 특히 '축농증'이라는 옛 용어는 베트남어로 직역하면 혼란을 줄 수 있으므로 사용하지 않는 것이 좋습니다. 한국에서는 부비동염을 만성화되면 수술(내시경 부비동 수술)을 권하지만, 베트남에서는 수술에 대한 거부감이 커서 약물 치료를 오래 지속하는 경향이 있습니다. 따라서 수술의 필요성을 설명할 때는 보존적 치료의 한계와 삶의 질 개선을 강조해야 합니다.",
        "meaningVi": "Viêm các xoang quanh mũi (xoang trán, xoang hàm, xoang bướm, xoang sàng). Do vi khuẩn, virus hoặc nấm. Triệu chứng: nghẹt mũi, chảy mũi vàng xanh, đau đầu, đau mặt, giảm khứu giác. Cấp tính (dưới 4 tuần) hoặc mãn tính (trên 12 tuần).",
        "context": "이비인후과 진료, 두통 클리닉, 알레르기 상담",
        "culturalNote": "한국에서는 부비동염을 '만성 질환'으로 인식하고 꾸준한 치료를 강조하지만, 베트남에서는 '감기가 오래간 것'으로 가볍게 여겨 치료를 중단하는 경우가 많습니다. 따라서 통역 시 만성 부비동염의 합병증(후각 상실, 안구 감염 등)을 언급하여 치료의 중요성을 강조해야 합니다. 또한 한국에서는 비염과 부비동염을 별개로 보지만, 베트남에서는 둘을 혼동하는 경우가 많아 증상의 차이를 명확히 설명해야 합니다.",
        "commonMistakes": [
            {
                "mistake": "'축농증'을 trữ mủ로 직역",
                "correction": "viêm xoang(부비동염) 사용",
                "explanation": "축농증은 구식 용어이며 혼란을 줄 수 있음"
            },
            {
                "mistake": "'콧물이 뒤로 넘어간다'를 mũi chảy sau로 직역",
                "correction": "hậu nhỏ mũi(후비루) 또는 mũi chảy xuống họng",
                "explanation": "의학 용어로 정확히 표현해야 함"
            },
            {
                "mistake": "내시경 수술을 mổ nội soi로만 표현",
                "correction": "phẫu thuật nội soi xoang(내시경 부비동 수술)로 구체화",
                "explanation": "수술 부위를 명확히 해야 함"
            }
        ],
        "examples": [
            {
                "ko": "만성 부비동염으로 3개월 이상 약물 치료했지만 효과가 없어 내시경 수술을 권합니다.",
                "vi": "Viêm xoang mãn tính đã điều trị thuốc hơn 3 tháng không đỡ, nên phẫu thuật nội soi xoang.",
                "situation": "formal"
            },
            {
                "ko": "현장에서 '코가 막히고 머리가 무겁다'고 하면 부비동염 가능성 있습니다.",
                "vi": "Tại hiện trường, nếu nói 'nghẹt mũi và đầu nặng' thì có thể bị viêm xoang.",
                "situation": "onsite"
            },
            {
                "ko": "나 부비동염이라 계절 바뀔 때마다 심해져.",
                "vi": "Tôi bị viêm xoang nên mỗi khi chuyển mùa lại nặng.",
                "situation": "informal"
            }
        ],
        "relatedTerms": ["비염", "비중격만곡증", "비용종", "후비루"]
    },
    {
        "slug": "viem-amidan",
        "korean": "편도선염",
        "vietnamese": "viêm amidan",
        "hanja": "扁桃腺炎",
        "hanjaReading": "扁(납작할 편) + 桃(복숭아 도) + 腺(샘 선) + 炎(불꽃 염)",
        "pronunciation": "편도선염",
        "meaningKo": "목 뒤쪽 편도선에 염증이 생기는 질환으로 주로 세균이나 바이러스 감염으로 발생함. 통역 시 주의할 점은 베트남어로 'amidan'이 편도선을 뜻하므로 'viêm amidan'이 정확하며, 구어로는 'sưng họng'(목 부음)이라고도 하지만 의학적으로는 구분해야 한다는 것입니다. 특히 '편도선 절제술'은 'cắt amidan' 또는 'phẫu thuật cắt amidan'으로 표현하되, 한국에서는 재발성 편도선염의 경우 적극적으로 수술을 권하지만, 베트남에서는 편도선이 '면역 기관'이라고 믿어 수술을 꺼리는 경향이 있어 수술 적응증을 명확히 설명해야 합니다. 또한 베트남에서는 '목이 부었다'는 표현이 편도선염뿐 아니라 림프절 비대 등도 포함할 수 있어 정확한 진단명을 확인해야 합니다.",
        "meaningVi": "Viêm các tuyến amidan ở hai bên họng do vi khuẩn (thường là liên cầu) hoặc virus. Triệu chứng: đau họng, nuốt đau, sốt cao, amidan đỏ sưng có mủ trắng. Nếu tái phát nhiều lần cần cắt amidan.",
        "context": "이비인후과 진료, 소아과, 학교 보건",
        "culturalNote": "한국에서는 편도선염이 1년에 5회 이상 재발하면 수술을 권하지만, 베트남에서는 '편도선이 면역력을 담당한다'는 인식이 강해 수술에 소극적입니다. 따라서 통역 시 수술 적응증(수면 무호흡, 만성 감염)과 수술 후에도 면역 기능에는 문제가 없다는 점을 강조해야 환자의 우려를 덜 수 있습니다. 또한 한국에서는 항생제를 즉시 처방하지만, 베트남에서는 소금물 가글 등 민간요법을 먼저 시도하는 경향이 있어 적절한 치료 시기를 놓칠 수 있습니다.",
        "commonMistakes": [
            {
                "mistake": "sưng họng을 모든 편도선염에 사용",
                "correction": "viêm amidan이 의학적으로 정확",
                "explanation": "목 부음은 여러 원인이 있을 수 있음"
            },
            {
                "mistake": "'고름이 낀다'를 có mủ로만 표현",
                "correction": "amidan có mảng mủ trắng(편도에 흰 농양)로 구체화",
                "explanation": "진단 소견을 정확히 전달해야 함"
            },
            {
                "mistake": "편도선 제거를 lấy amidan으로 표현",
                "correction": "cắt amidan 또는 phẫu thuật cắt amidan",
                "explanation": "'제거'는 cắt(절제)로 표현해야 함"
            }
        ],
        "examples": [
            {
                "ko": "급성 편도선염으로 고열이 있고 편도에 흰 고름이 보입니다. 항생제 치료가 필요하며, 1년에 5회 이상 재발하면 수술을 고려해야 합니다.",
                "vi": "Viêm amidan cấp có sốt cao và thấy mảng mủ trắng trên amidan. Cần điều trị kháng sinh, nếu tái phát từ 5 lần/năm trở lên thì cân nhắc phẫu thuật cắt amidan.",
                "situation": "formal"
            },
            {
                "ko": "현장에서 '목이 너무 아파서 침도 못 삼킨다'고 하면 급성 편도선염일 수 있습니다.",
                "vi": "Tại hiện trường, nếu nói 'đau họng quá nuốt nước bọt cũng không được' thì có thể là viêm amidan cấp.",
                "situation": "onsite"
            },
            {
                "ko": "우리 애 편도선염 자주 걸려서 수술할까 고민 중이야.",
                "vi": "Con tôi hay bị viêm amidan nên đang cân nhắc phẫu thuật cắt amidan.",
                "situation": "informal"
            }
        ],
        "relatedTerms": ["인두염", "급성편도선염", "만성편도선염", "편도주위농양"]
    },
    {
        "slug": "benh-meniere",
        "korean": "메니에르병",
        "vietnamese": "bệnh Ménière",
        "hanja": None,
        "hanjaReading": None,
        "pronunciation": "메니에르병",
        "meaningKo": "내이의 림프액 과다로 발생하는 어지럼증, 이명, 청력 저하를 동반하는 질환. 통역 시 주의할 점은 베트남어로 'bệnh Ménière'로 표기하되 발음은 '메니에르'에 가깝게 해야 한다는 것입니다. 이 질환은 '발작성 어지럼증'이 특징이므로 'chóng mặt cơn'(발작성 현기증)이라는 표현을 함께 사용하면 이해를 돕습니다. 한국에서는 메니에르병을 만성 질환으로 인식하고 저염식과 이뇨제로 관리하지만, 베트남에서는 이 질환에 대한 인지도가 낮아 단순 어지럼증으로 오해하는 경우가 많습니다. 따라서 통역 시 증상의 특징(회전성 어지럼, 청력 변동)을 구체적으로 설명하여 다른 어지럼증과 구분해야 합니다.",
        "meaningVi": "Bệnh do tăng áp lực dịch nội tai, gây chóng mặt kiểu quay tròn (vertigo), ù tai, giảm thính lực, và cảm giác đầy tai. Thường xuất hiện từng cơn kéo dài 20 phút đến vài giờ. Điều trị bằng thuốc lợi tiểu, hạn chế muối, tránh stress.",
        "context": "이비인후과 진료, 어지럼증 클리닉",
        "culturalNote": "한국에서는 메니에르병을 '난치성 만성 질환'으로 인식하고 장기 관리의 중요성을 강조하지만, 베트남에서는 '일시적인 어지럼증'으로 가볍게 여겨 치료를 중단하는 경우가 많습니다. 따라서 통역 시 증상 관리(저염식, 스트레스 감소)와 합병증 예방(영구 청력 손실)의 필요성을 설명해야 합니다. 또한 한국에서는 이뇨제를 장기 복용하지만, 베트남 환자들은 약물 부작용을 우려하여 복용을 꺼리는 경향이 있어 약물의 필요성과 안전성을 강조해야 합니다.",
        "commonMistakes": [
            {
                "mistake": "'어지럽다'를 chóng mặt로만 표현",
                "correction": "chóng mặt kiểu quay tròn(회전성 어지럼)으로 구체화",
                "explanation": "메니에르병 특유의 증상을 명확히 해야 함"
            },
            {
                "mistake": "'귀가 먹먹하다'를 tai tắc으로 오역",
                "correction": "cảm giác đầy tai(귀 충만감)가 정확",
                "explanation": "막힘과 충만감을 구분해야 함"
            },
            {
                "mistake": "저염식을 ăn ít muối로만 표현",
                "correction": "chế độ ăn hạn chế muối nghiêm ngặt(엄격한 저염식)로 강조",
                "explanation": "치료의 중요성을 전달해야 함"
            }
        ],
        "examples": [
            {
                "ko": "메니에르병은 발작성 회전성 어지럼증과 청력 변동이 특징입니다. 저염식을 철저히 하고 이뇨제를 복용해야 합니다.",
                "vi": "Bệnh Ménière đặc trưng là chóng mặt kiểu quay tròn từng cơn và thính lực lên xuống. Cần hạn chế muối nghiêm ngặt và uống thuốc lợi tiểu.",
                "situation": "formal"
            },
            {
                "ko": "현장에서 '갑자기 세상이 빙글빙글 돌고 구토한다'고 하면 메니에르병 의심해야 합니다.",
                "vi": "Tại hiện trường, nếu nói 'đột ngột thế giới quay tròn và nôn' thì nghi ngờ bệnh Ménière.",
                "situation": "onsite"
            },
            {
                "ko": "나 메니에르병이라 짠 음식 못 먹어. 스트레스 받으면 발작 와.",
                "vi": "Tôi bị bệnh Ménière nên không ăn mặn được. Stress là lại lên cơn.",
                "situation": "informal"
            }
        ],
        "relatedTerms": ["이명", "돌발성난청", "전정신경염", "양성돌발체위성어지럼증"]
    },
    {
        "slug": "diec-dot-ngot",
        "korean": "돌발성난청",
        "vietnamese": "điếc đột ngột",
        "hanja": "突發性難聽",
        "hanjaReading": "突(갑자기 돌) + 發(필 발) + 性(성품 성) + 難(어려울 난) + 聽(들을 청)",
        "pronunciation": "돌발성난청",
        "meaningKo": "갑작스럽게 한쪽 귀의 청력이 급격히 떨어지는 응급 질환. 통역 시 주의할 점은 베트nam어로 'điếc đột ngột' 또는 'giảm thính lực đột ngột'으로 표현하되, 응급 상황임을 강조하기 위해 'cấp cứu thính học'(청각 응급)이라는 표현을 추가하는 것이 좋습니다. 특히 '72시간 골든타임'을 설명할 때 'thời gian vàng 72 giờ'로 번역하고, 이 시간 내 치료를 시작해야 청력 회복 가능성이 높다는 점을 강조해야 합니다. 한국에서는 돌발성난청을 응급으로 인식하고 즉시 스테로이드 치료를 시작하지만, 베트남에서는 '귀가 좀 안 들린다'고 가볍게 여겨 병원 방문을 미루는 경향이 있어 조기 치료의 중요성을 문화적 맥락에서 설명해야 합니다.",
        "meaningVi": "Mất thính lực đột ngột ở một bên tai trong vòng 72 giờ, không rõ nguyên nhân. Là cấp cứu tai mũi họng, cần điều trị steroid trong 72 giờ đầu để tăng cơ hội phục hồi thính lực. Có thể kèm ù tai, chóng mặt.",
        "context": "이비인후과 응급, 청력 클리닉",
        "culturalNote": "한국에서는 돌발성난청을 '72시간 골든타임'이 있는 응급 질환으로 인식하고 즉시 입원 치료를 하지만, 베트남에서는 '며칠 쉬면 나을 것'으로 가볍게 여겨 치료 시기를 놓치는 경우가 많습니다. 따라서 통역 시 조기 치료의 중요성과 치료하지 않을 경우 영구 청력 손실 가능성을 명확히 설명해야 합니다. 또한 한국에서는 고압산소치료를 병행하기도 하지만, 베트남에서는 이 치료법이 생소하여 추가 설명이 필요합니다.",
        "commonMistakes": [
            {
                "mistake": "'갑자기 귀가 안 들린다'를 tai đột ngột không nghe로 직역",
                "correction": "điếc đột ngột 또는 giảm thính lực đột ngột",
                "explanation": "의학 용어로 정확히 표현해야 함"
            },
            {
                "mistake": "골든타임을 golden time으로 영어 그대로 사용",
                "correction": "thời gian vàng 72 giờ(72시간 골든타임)로 번역",
                "explanation": "베트남 환자가 이해할 수 있도록 번역 필요"
            },
            {
                "mistake": "스테로이드를 steroid로만 표현",
                "correction": "thuốc corticosteroid(코르티코스테로이드 약물)로 구체화",
                "explanation": "약물 종류를 명확히 해야 함"
            }
        ],
        "examples": [
            {
                "ko": "돌발성난청은 72시간 내 치료를 시작해야 청력 회복 가능성이 높습니다. 즉시 스테로이드 치료를 시작하겠습니다.",
                "vi": "Điếc đột ngột cần bắt đầu điều trị trong 72 giờ mới có khả năng phục hồi thính lực cao. Sẽ bắt đầu điều trị corticosteroid ngay.",
                "situation": "formal"
            },
            {
                "ko": "현장에서 '아침에 일어났는데 한쪽 귀가 안 들린다'고 하면 돌발성난청 의심하고 즉시 병원 가야 합니다.",
                "vi": "Tại hiện trường, nếu nói 'sáng dậy một bên tai không nghe' thì nghi điếc đột ngột, phải đi bệnh viện ngay.",
                "situation": "onsite"
            },
            {
                "ko": "친구가 돌발성난청 걸렸는데 바로 병원 가서 다행히 회복됐대.",
                "vi": "Bạn tôi bị điếc đột ngột nhưng đi bệnh viện ngay nên may mắn hồi phục.",
                "situation": "informal"
            }
        ],
        "relatedTerms": ["메니에르병", "이명", "청력검사", "고압산소치료"]
    },
    {
        "slug": "u-tai",
        "korean": "이명",
        "vietnamese": "ù tai",
        "hanja": "耳鳴",
        "hanjaReading": "耳(귀 이) + 鳴(울 명)",
        "pronunciation": "이명",
        "meaningKo": "외부 소리 없이 귀에서 소리가 들리는 증상으로 다양한 원인으로 발생함. 통역 시 주의할 점은 베트nam어로 'ù tai'가 일반적이지만, 소리의 종류에 따라 'kêu tai'(귀에서 소리), 'rền tai'(귀 울림) 등 다양한 표현이 있으므로 환자의 증상을 정확히 파악해야 한다는 것입니다. 특히 이명의 양상을 설명할 때 '삐- 소리'는 'tiếng rít', '웅- 소리'는 'tiếng vo vo', '매미 소리'는 'tiếng ve' 등으로 구분하여 번역해야 진단에 도움이 됩니다. 한국에서는 이명을 '난치성 증상'으로 인식하고 소리치료나 인지행동치료를 권하지만, 베트남에서는 '신경 쓰지 않으면 된다'는 식으로 가볍게 여기는 경향이 있어 적절한 치료와 관리의 중요성을 설명해야 합니다.",
        "meaningVi": "Triệu chứng nghe thấy tiếng kêu trong tai khi không có nguồn âm thanh bên ngoài. Có thể là tiếng rít, vo vo, ve kêu. Nguyên nhân: tổn thương thính giác, stress, thuốc độc tai, bệnh Ménière. Điều trị: tìm nguyên nhân, liệu pháp âm thanh, quản lý stress.",
        "context": "이비인후과 진료, 스트레스 관리 상담",
        "culturalNote": "한국에서는 이명을 '삶의 질을 저하시키는 증상'으로 인식하고 적극적으로 치료하지만, 베트남에서는 '나이 들면 생기는 것'으로 여겨 방치하는 경우가 많습니다. 따라서 통역 시 이명이 우울증, 불면증 등을 유발할 수 있으며 적절한 관리가 필요하다는 점을 강조해야 합니다. 또한 한국에서는 이명 재훈련 치료(TRT)나 소리 발생기를 사용하지만, 베트남에서는 이러한 치료법이 생소하여 자세한 설명이 필요합니다.",
        "commonMistakes": [
            {
                "mistake": "모든 이명을 ù tai로만 표현",
                "correction": "소리 종류에 따라 tiếng rít/vo vo/ve kêu 구분",
                "explanation": "증상을 구체적으로 전달해야 진단에 도움"
            },
            {
                "mistake": "'귀에서 소리 난다'를 tai có tiếng로만 표현",
                "correction": "nghe tiếng kêu trong tai(귀에서 소리 들림)가 정확",
                "explanation": "자각 증상임을 명확히 해야 함"
            },
            {
                "mistake": "소리치료를 điều trị bằng âm thanh로만 표현",
                "correction": "liệu pháp âm thanh 또는 TRT(이명재훈련치료)로 구체화",
                "explanation": "치료법을 정확히 전달해야 함"
            }
        ],
        "examples": [
            {
                "ko": "이명은 완치가 어렵지만 소리치료와 인지행동치료로 증상을 줄일 수 있습니다. 스트레스 관리도 중요합니다.",
                "vi": "Ù tai khó chữa khỏi hoàn toàn nhưng có thể giảm triệu chứng bằng liệu pháp âm thanh và liệu pháp nhận thức hành vi. Quản lý stress cũng rất quan trọng.",
                "situation": "formal"
            },
            {
                "ko": "현장에서 '귀에서 삐- 소리가 계속 난다'고 하면 이명 증상입니다.",
                "vi": "Tại hiện trường, nếu nói 'trong tai cứ kêu tiếng rít mãi' thì đó là triệu chứng ù tai.",
                "situation": "onsite"
            },
            {
                "ko": "나 이명 때문에 밤에 잠 못 자. 귀에서 매미 소리 나.",
                "vi": "Tôi ù tai nên đêm không ngủ được. Trong tai nghe tiếng ve.",
                "situation": "informal"
            }
        ],
        "relatedTerms": ["돌발성난청", "메니에르병", "청각과민", "소음성난청"]
    },
    {
        "slug": "lech-vach-ngan-mui",
        "korean": "비중격만곡증",
        "vietnamese": "lệch vách ngăn mũi",
        "hanja": "鼻中隔彎曲症",
        "hanjaReading": "鼻(코 비) + 中(가운데 중) + 隔(사이 격) + 彎(굽을 만) + 曲(굽을 곡) + 症(증세 증)",
        "pronunciation": "비중격만곡증",
        "meaningKo": "코 안의 중앙 칸막이인 비중격이 휘어진 상태로 코막힘을 유발함. 통역 시 주의할 점은 베트nam어로 'lệch vách ngăn mũi'(코 칸막이 휨) 또는 'vách ngăn mũi cong'으로 표현하되, '만곡'이라는 한자어를 직역하지 말고 '휘어진/굽은' 의미로 풀어서 설명해야 한다는 것입니다. 특히 '비중격 교정술'을 설명할 때 'phẫu thuật chỉnh vách ngăn mũi'로 번역하고, 수술이 코 모양이 아닌 기능 개선을 위한 것임을 명확히 해야 미용 수술과의 혼동을 피할 수 있습니다. 한국에서는 비중격만곡증을 적극적으로 수술하지만, 베트남에서는 '코가 좀 막히는 것'으로 가볍게 여겨 수술을 꺼리는 경향이 있어 수술의 필요성(수면 무호흡 예방, 부비동염 재발 방지)을 구체적으로 설명해야 합니다.",
        "meaningVi": "Tình trạng vách ngăn ở giữa mũi bị lệch hoặc cong, gây nghẹt mũi một bên hoặc cả hai bên. Có thể bẩm sinh hoặc do chấn thương. Triệu chứng: nghẹt mũi mãn tính, chảy máu mũi, viêm xoang tái phát. Điều trị: phẫu thuật chỉnh vách ngăn mũi.",
        "context": "이비인후과 진료, 코골이 클리닉, 수면 무호흡 상담",
        "culturalNote": "한국에서는 비중격만곡증을 '삶의 질을 저하시키는 질환'으로 인식하고 수술을 권장하지만, 베트남에서는 '코막힘 정도는 참을 수 있다'는 인식이 강해 수술에 소극적입니다. 따라서 통역 시 비중격만곡증이 부비동염, 수면 무호흡, 코골이 등을 유발할 수 있으며, 수술로 이를 예방할 수 있다는 점을 강조해야 합니다. 또한 한국에서는 비중격 교정술과 코 성형술을 동시에 하는 경우가 많지만, 베트남에서는 미용 수술에 대한 거부감이 있어 기능 개선 수술임을 명확히 해야 합니다.",
        "commonMistakes": [
            {
                "mistake": "'비중격이 휘었다'를 vách ngăn mũi bị uốn으로 직역",
                "correction": "lệch vách ngăn mũi 또는 vách ngăn mũi cong",
                "explanation": "의학 용어로 정확히 표현해야 함"
            },
            {
                "mistake": "교정술을 sửa mũi(코 고치기)로 오역",
                "correction": "phẫu thuật chỉnh vách ngăn mũi(비중격 교정술)",
                "explanation": "미용 수술과 구분해야 함"
            },
            {
                "mistake": "'코가 막힌다'를 mũi tắc으로만 표현",
                "correction": "nghẹt mũi mãn tính(만성 코막힘)으로 증상 명확화",
                "explanation": "일시적 코막힘과 구분 필요"
            }
        ],
        "examples": [
            {
                "ko": "비중격만곡증으로 만성 코막힘과 부비동염이 반복됩니다. 비중격 교정술을 권장합니다.",
                "vi": "Lệch vách ngăn mũi gây nghẹt mũi mãn tính và viêm xoang tái phát. Nên phẫu thuật chỉnh vách ngăn mũi.",
                "situation": "formal"
            },
            {
                "ko": "현장에서 '한쪽 코가 항상 막혀 있다'고 하면 비중격만곡증 의심해야 합니다.",
                "vi": "Tại hiện trường, nếu nói 'một bên mũi luôn bị nghẹt' thì nghi ngờ lệch vách ngăn mũi.",
                "situation": "onsite"
            },
            {
                "ko": "나 비중격만곡증이라 코로 숨쉬기 힘들어. 수술 생각 중이야.",
                "vi": "Tôi bị lệch vách ngăn mũi nên thở bằng mũi khó. Đang nghĩ đến phẫu thuật.",
                "situation": "informal"
            }
        ],
        "relatedTerms": ["비염", "부비동염", "코골이", "수면무호흡증"]
    },
    {
        "slug": "viem-da-co-dia",
        "korean": "아토피피부염",
        "vietnamese": "viêm da cơ địa",
        "hanja": None,
        "hanjaReading": None,
        "pronunciation": "아토피피부염",
        "meaningKo": "만성 재발성 염증성 피부질환으로 가려움과 피부 건조가 특징임. 통역 시 주의할 점은 베트nam어로 'viêm da cơ địa' 또는 'eczema thể tạng'으로 표현하되, 'cơ địa'는 '체질'을 의미하므로 유전적·면역학적 요인과 연관됨을 설명해야 한다는 것입니다. 특히 '아토피 행진(atopic march)'을 설명할 때 'hành trình dị ứng'로 번역하고, 아토피피부염→식품 알레르기→천식→비염 순으로 진행될 수 있다는 점을 강조해야 합니다. 한국에서는 아토피를 '만성 질환'으로 인식하고 보습과 스테로이드 관리를 강조하지만, 베트남에서는 '피부가 좀 거친 것'으로 가볍게 여기거나 스테로이드에 대한 두려움이 커서 치료를 거부하는 경우가 많습니다. 따라서 적절한 스테로이드 사용의 안전성과 효과를 설명하고, 보습의 중요성을 문화적 맥락에서 강조해야 합니다.",
        "meaningVi": "Bệnh viêm da mãn tính tái phát, có yếu tố di truyền và miễn dịch. Triệu chứng: ngứa, da khô, đỏ, nứt nẻ, thường ở nếp gấp. Hay gặp ở trẻ em, có thể kèm hen, viêm mũi dị ứng. Điều trị: dưỡng ẩm, corticosteroid bôi, tránh tác nhân kích ứng.",
        "context": "피부과 진료, 소아과, 알레르기 클리닉",
        "culturalNote": "한국에서는 아토피피부염을 '적극적으로 관리해야 할 만성 질환'으로 인식하고 보습제를 하루 2회 이상 바르도록 권장하지만, 베트남에서는 '어릴 때 흔한 피부병'으로 여겨 자연 치유를 기대하며 방치하는 경우가 많습니다. 따라서 통역 시 조기 치료와 관리의 중요성, 그리고 방치 시 피부 감염이나 색소침착 등의 합병증이 생길 수 있음을 강조해야 합니다. 또한 한국에서는 스테로이드 연고를 단계적으로 사용하지만, 베트남에서는 '스테로이드=부작용'이라는 인식이 강해 사용을 거부하는 환자가 많으므로, 적절한 사용 시 안전하다는 점을 반복 설명해야 합니다.",
        "commonMistakes": [
            {
                "mistake": "'아토피'를 atopy로 영어 그대로 사용",
                "correction": "viêm da cơ địa 또는 eczema thể tạng",
                "explanation": "베트남어 의학 용어로 번역해야 함"
            },
            {
                "mistake": "'보습제'를 kem dưỡng da로만 표현",
                "correction": "kem dưỡng ẩm chuyên dụng(전용 보습제)로 구체화",
                "explanation": "일반 화장품과 구분해야 함"
            },
            {
                "mistake": "스테로이드 연고를 thuốc bôi da로만 표현",
                "correction": "thuốc bôi corticosteroid(스테로이드 연고)로 명확히",
                "explanation": "약물 종류를 정확히 전달해야 함"
            }
        ],
        "examples": [
            {
                "ko": "아토피피부염은 만성 질환으로 보습이 가장 중요합니다. 하루 2회 이상 보습제를 바르고, 염증이 심할 때는 스테로이드 연고를 단기간 사용하세요.",
                "vi": "Viêm da cơ địa là bệnh mãn tính, dưỡng ẩm là quan trọng nhất. Thoa kem dưỡng ẩm từ 2 lần/ngày trở lên, khi viêm nặng dùng thuốc bôi corticosteroid ngắn ngày.",
                "situation": "formal"
            },
            {
                "ko": "현장에서 '아이가 가려워서 긁어 피가 난다'고 하면 아토피피부염 악화 상태입니다.",
                "vi": "Tại hiện trường, nếu nói 'bé ngứa gãi đến chảy máu' thì viêm da cơ địa đang trầm trọng.",
                "situation": "onsite"
            },
            {
                "ko": "우리 애 아토피 심해서 밤에 잠도 못 자. 보습제 계속 발라야 해.",
                "vi": "Con tôi viêm da cơ địa nặng nên đêm không ngủ được. Phải thoa kem dưỡng ẩm liên tục.",
                "situation": "informal"
            }
        ],
        "relatedTerms": ["건선", "접촉피부염", "지루피부염", "식품알레르기"]
    },
    {
        "slug": "vay-nen",
        "korean": "건선",
        "vietnamese": "vảy nến",
        "hanja": "乾癬",
        "hanjaReading": "乾(마를 건) + 癬(버짐 선)",
        "pronunciation": "건선",
        "meaningKo": "피부 세포가 과도하게 증식하여 은백색 각질을 동반한 붉은 반점이 생기는 만성 염증성 피부질환. 통역 시 주의할 점은 베트nam어로 'vảy nến'(비늘 같은 각질)으로 표현하되, 'bệnh vẩy nến' 또는 'bệnh á sừng'이라고도 하므로 환자가 익숙한 용어를 확인해야 한다는 것입니다. 특히 건선은 전염되지 않는다는 점을 'không lây nhiễm'으로 강조해야 하는데, 베트남에서는 피부병을 전염병으로 오해하는 경향이 있어 사회적 낙인을 우려하는 환자가 많습니다. 따라서 통역 시 질환의 면역학적 원인과 비전염성을 명확히 설명해야 합니다. 한국에서는 생물학적 제제까지 사용하지만, 베트남에서는 고가 치료에 대한 접근성이 낮아 경제적 부담을 고려한 치료 계획 수립이 필요합니다.",
        "meaningVi": "Bệnh da mãn tính do tăng sinh tế bào da, gây mảng đỏ phủ vảy bạc trắng dày. Không lây nhiễm, liên quan đến miễn dịch và di truyền. Có thể kèm viêm khớp. Điều trị: thuốc bôi (corticosteroid, vitamin D), quang trị liệu, thuốc sinh học.",
        "context": "피부과 진료, 류마티스내과, 면역질환 클리닉",
        "culturalNote": "한국에서는 건선을 '만성 면역 질환'으로 인식하고 장기 치료를 강조하지만, 베트남에서는 '불치병'으로 오해하거나 '전염병'으로 잘못 알아 사회적 격리를 경험하는 환자가 많습니다. 따라서 통역 시 건선이 전염되지 않으며, 적절한 치료로 증상 조절이 가능하다는 점을 반복 강조해야 합니다. 또한 한국에서는 생물학적 제제(TNF-α 억제제 등)를 사용하지만, 베트남에서는 경제적 부담으로 인해 접근성이 낮으므로, 단계적 치료 계획(외용제→광선치료→전신치료)을 명확히 설명해야 합니다.",
        "commonMistakes": [
            {
                "mistake": "'건선'을 bệnh khô da(건조한 피부병)로 오역",
                "correction": "vảy nến 또는 bệnh á sừng",
                "explanation": "정확한 질환명 사용 필요"
            },
            {
                "mistake": "'각질'을 vảy da로만 표현",
                "correction": "vảy bạc trắng dày(두꺼운 은백색 각질)로 구체화",
                "explanation": "건선 특유의 증상 전달해야 함"
            },
            {
                "mistake": "생물학적 제제를 thuốc sinh học으로만 표현",
                "correction": "thuốc điều trị sinh học(생물학적 치료제)로 명확히",
                "explanation": "치료제 종류를 정확히 전달해야 함"
            }
        ],
        "examples": [
            {
                "ko": "건선은 전염되지 않는 만성 면역 질환입니다. 스테로이드 연고와 광선치료로 증상을 조절할 수 있으며, 심하면 생물학적 제제를 사용합니다.",
                "vi": "Vảy nến là bệnh miễn dịch mãn tính không lây nhiễm. Có thể kiểm soát triệu chứng bằng thuốc bôi corticosteroid và quang trị liệu, nếu nặng dùng thuốc điều trị sinh học.",
                "situation": "formal"
            },
            {
                "ko": "현장에서 '팔꿈치와 무릎에 은백색 딱지가 생긴다'고 하면 건선 의심해야 합니다.",
                "vi": "Tại hiện trường, nếu nói 'ở khuỷu tay và đầu gối có vảy bạc trắng' thì nghi ngờ vảy nến.",
                "situation": "onsite"
            },
            {
                "ko": "나 건선 있는데 겨울만 되면 심해져. 보습 열심히 해야 돼.",
                "vi": "Tôi bị vảy nến, mỗi mùa đông là nặng lên. Phải dưỡng ẩm chăm chỉ.",
                "situation": "informal"
            }
        ],
        "relatedTerms": ["아토피피부염", "지루피부염", "건선관절염", "광선치료"]
    },
    {
        "slug": "zona-than-kinh",
        "korean": "대상포진",
        "vietnamese": "zona thần kinh",
        "hanja": "帶狀疱疹",
        "hanjaReading": "帶(띠 대) + 狀(모양 상) + 疱(물집 포) + 疹(돋을 진)",
        "pronunciation": "대상포진",
        "meaningKo": "수두 바이러스가 재활성화되어 신경을 따라 띠 모양의 물집과 통증을 일으키는 질환. 통역 시 주의할 점은 베트nam어로 'zona thần kinh' 또는 'bệnh zona'로 표현하되, '포진 후 신경통(PHN)'을 'đau thần kinh sau zona'로 번역하고 조기 치료의 중요성을 강조해야 한다는 것입니다. 특히 '72시간 골든타임'을 설명할 때 항바이러스제를 빨리 복용할수록 신경통 예방에 효과적이라는 점을 강조해야 합니다. 한국에서는 50세 이상에게 대상포진 백신을 권장하지만, 베트남에서는 이 백신이 필수가 아니어서 접종률이 낮습니다. 따라서 통역 시 백신의 효과(발병률 50% 감소, 신경통 67% 감소)를 구체적으로 설명하여 예방의 중요성을 강조해야 합니다.",
        "meaningVi": "Bệnh do virus herpes zoster (virus thủy đậu tái hoạt) gây phồng rộp và đau dọc theo dây thần kinh. Thường ở người lớn tuổi, suy giảm miễn dịch. Biến chứng nguy hiểm: đau thần kinh sau zona (PHN). Cần uống thuốc kháng virus trong 72 giờ đầu.",
        "context": "피부과 진료, 통증 클리닉, 노인 건강관리",
        "culturalNote": "한국에서는 대상포진을 '조기 치료가 중요한 질환'으로 인식하고 즉시 항바이러스제를 처방하지만, 베트남에서는 '띠 모양 물집'을 단순 피부병으로 오해하여 치료를 미루는 경우가 많습니다. 따라서 통역 시 대상포진의 합병증(포진 후 신경통, 실명 위험)과 조기 치료의 중요성을 강조해야 합니다. 또한 한국에서는 대상포진 백신(싱그릭스)을 적극 권장하지만, 베트남에서는 백신 접종 문화가 덜 발달하여 예방접종의 필요성을 설명할 때 문화적 차이를 고려해야 합니다.",
        "commonMistakes": [
            {
                "mistake": "'대상포진'을 bệnh phồng rộp로만 표현",
                "correction": "zona thần kinh 또는 bệnh zona",
                "explanation": "정확한 질환명 사용 필요"
            },
            {
                "mistake": "포진 후 신경통을 đau sau bệnh로만 표현",
                "correction": "đau thần kinh sau zona(PHN)로 구체화",
                "explanation": "합병증을 명확히 전달해야 함"
            },
            {
                "mistake": "'띠 모양'을 hình dải로만 표현",
                "correction": "phân bố dọc theo dây thần kinh(신경 분포)로 설명",
                "explanation": "질환의 특징을 정확히 전달해야 함"
            }
        ],
        "examples": [
            {
                "ko": "대상포진은 72시간 내 항바이러스제를 복용해야 포진 후 신경통을 예방할 수 있습니다. 50세 이상은 백신 접종을 권장합니다.",
                "vi": "Zona thần kinh cần uống thuốc kháng virus trong 72 giờ mới ngăn được đau thần kinh sau zona. Người trên 50 tuổi nên tiêm vắc xin phòng bệnh.",
                "situation": "formal"
            },
            {
                "ko": "현장에서 '한쪽 몸에 띠 모양으로 물집이 생기고 아프다'고 하면 대상포진입니다.",
                "vi": "Tại hiện trường, nếu nói 'một bên thân mình có phồng rộp thành dải và đau' thì đó là zona thần kinh.",
                "situation": "onsite"
            },
            {
                "ko": "어머니가 대상포진 걸렸는데 통증이 너무 심하시대.",
                "vi": "Mẹ tôi bị zona thần kinh, đau quá.",
                "situation": "informal"
            }
        ],
        "relatedTerms": ["수두", "포진후신경통", "대상포진백신", "항바이러스제"]
    },
    {
        "slug": "rung-toc",
        "korean": "탈모",
        "vietnamese": "rụng tóc",
        "hanja": "脫毛",
        "hanjaReading": "脫(벗을 탈) + 毛(털 모)",
        "pronunciation": "탈모",
        "meaningKo": "머리카락이 비정상적으로 많이 빠지는 증상으로 다양한 원인이 있음. 통역 시 주의할 점은 베트nam어로 'rụng tóc'이 일반적이지만, 유형에 따라 '원형탈모(hói đầu vòng)', '남성형 탈모(hói đầu nam giới)', '휴지기 탈모(rụng tóc giai đoạn nghỉ)' 등으로 구분해야 한다는 것입니다. 특히 '모낭'은 'nang lông'으로 번역하며, 탈모 치료제인 미녹시딜(minoxidil)과 피나스테리드(finasteride)는 발음 그대로 사용하되 효과와 부작용을 설명해야 합니다. 한국에서는 탈모를 '적극적으로 치료할 질환'으로 인식하고 조기 치료를 강조하지만, 베트남에서는 '나이 들면 생기는 것'으로 여겨 치료를 미루는 경향이 있습니다. 따라서 조기 치료의 중요성과 치료 옵션(약물, 모발이식)을 명확히 설명해야 합니다.",
        "meaningVi": "Tình trạng rụng tóc bất thường, có nhiều nguyên nhân: di truyền (hói đầu nam giới), stress, thiếu dinh dưỡng, bệnh lý (giáp,빈혈), thuốc. Điều trị: minoxidil (bôi), finasteride (uống), cấy tóc. Cần tìm nguyên nhân để điều trị hiệu quả.",
        "context": "피부과 진료, 모발이식 클리닉, 내분비 클리닉",
        "culturalNote": "한국에서는 탈모를 '외모와 자존감에 영향을 주는 문제'로 인식하고 조기 치료를 강조하지만, 베트남에서는 '자연스러운 노화 과정'으로 여겨 치료에 소극적입니다. 따라서 통역 시 탈모 치료의 효과와 삶의 질 개선을 강조하되, 경제적 부담(모발이식 비용)을 고려한 단계적 치료 계획을 제시해야 합니다. 또한 한국에서는 피나스테리드를 남성형 탈모에 널리 사용하지만, 베트남에서는 부작용(성기능 저하)에 대한 우려가 커서 약물의 안전성을 충분히 설명해야 합니다.",
        "commonMistakes": [
            {
                "mistake": "모든 탈모를 rụng tóc으로만 표현",
                "correction": "유형에 따라 hói đầu vòng/nam giới/giai đoạn nghỉ 구분",
                "explanation": "탈모 유형에 따라 치료가 다름"
            },
            {
                "mistake": "'머리가 벗겨진다'를 đầu bị lột로 직역",
                "correction": "hói đầu(대머리) 또는 rụng tóc nhiều(많이 빠짐)",
                "explanation": "자연스러운 표현 사용 필요"
            },
            {
                "mistake": "모발이식을 trồng tóc(머리 심기)로만 표현",
                "correction": "cấy tóc 또는 ghép tóc(모발이식)",
                "explanation": "의학 용어로 정확히 표현해야 함"
            }
        ],
        "examples": [
            {
                "ko": "남성형 탈모는 조기에 치료할수록 효과가 좋습니다. 미녹시딜과 피나스테리드를 병용하면 탈모 진행을 늦출 수 있습니다.",
                "vi": "Hói đầu nam giới điều trị sớm càng hiệu quả. Dùng kết hợp minoxidil và finasteride có thể làm chậm quá trình rụng tóc.",
                "situation": "formal"
            },
            {
                "ko": "현장에서 '머리카락이 하루에 100개 이상 빠진다'고 하면 탈모 진행 중일 수 있습니다.",
                "vi": "Tại hiện trường, nếu nói 'rụng hơn 100 sợi/ngày' thì có thể đang bị rụng tóc bệnh lý.",
                "situation": "onsite"
            },
            {
                "ko": "나 요즘 스트레스 받아서 머리 많이 빠져. 탈모약 먹어야 하나.",
                "vi": "Dạo này tôi stress nên rụng tóc nhiều. Phải uống thuốc chống rụng tóc không nhỉ.",
                "situation": "informal"
            }
        ],
        "relatedTerms": ["원형탈모", "남성형탈모", "모발이식", "미녹시딜"]
    },
    {
        "slug": "mun-trung-ca",
        "korean": "여드름",
        "vietnamese": "mụn trứng cá",
        "hanja": None,
        "hanjaReading": None,
        "pronunciation": "여드름",
        "meaningKo": "모낭과 피지선에 염증이 생겨 발생하는 피부질환으로 주로 청소년기에 나타남. 통역 시 주의할 점은 베트nam어로 'mụn trứng cá'가 일반적이지만, 정도에 따라 '좁쌀여드름(mụn đầu trắng)', '화농성 여드름(mụn mủ)', '낭종성 여드름(mụn bọc)'으로 구분해야 한다는 것입니다. 특히 '피지'는 'bã nhờn'으로 번역하며, 여드름 치료제인 '레티노이드(retinoid)'는 'thuốc retinoid', '벤조일퍼옥사이드(benzoyl peroxide)'는 'benzoyl peroxide'로 발음 그대로 사용하되 효과를 설명해야 합니다. 한국에서는 여드름을 '적극적으로 치료할 질환'으로 인식하고 흉터 예방을 강조하지만, 베트남에서는 '사춘기에 생기는 것'으로 가볍게 여겨 치료를 미루거나 손으로 짜는 경우가 많아 흉터 위험을 강조해야 합니다.",
        "meaningVi": "Bệnh da do viêm nang lông và tuyến bã nhờn, gây mụn đầu trắng, mụn đầu đen, mụn mủ. Hay gặp ở tuổi vị thành niên do hormone. Điều trị: rửa mặt đúng cách, thuốc bôi (retinoid, benzoyl peroxide), kháng sinh, isotretinoin (nếu nặng).",
        "context": "피부과 진료, 미용 클리닉, 청소년 건강관리",
        "culturalNote": "한국에서는 여드름을 '조기 치료로 흉터를 예방해야 할 질환'으로 인식하고 피부과 진료를 권장하지만, 베트남에서는 '사춘기에 생기는 것'으로 여겨 민간요법(치약 바르기, 레몬즙)이나 미용실 시술로 해결하려는 경향이 있습니다. 따라서 통역 시 잘못된 관리가 흉터를 남길 수 있음을 강조하고, 전문적인 치료의 필요성을 설명해야 합니다. 또한 한국에서는 이소트레티노인(로아큐탄)을 중증 여드름에 사용하지만, 베트남에서는 부작용(건조, 기형아)에 대한 우려가 커서 약물의 효과와 주의사항을 충분히 설명해야 합니다.",
        "commonMistakes": [
            {
                "mistake": "모든 여드름을 mụn으로만 표현",
                "correction": "mụn trứng cá 또는 유형별로 mụn đầu trắng/mụn mủ 구분",
                "explanation": "여드름 종류에 따라 치료가 다름"
            },
            {
                "mistake": "'여드름을 짠다'를 nặn mụn으로만 표현",
                "correction": "nặn mụn không đúng cách(잘못 짜기) + 흉터 경고",
                "explanation": "위험성을 함께 전달해야 함"
            },
            {
                "mistake": "피지를 dầu da(피부 기름)로만 표현",
                "correction": "bã nhờn(피지)이 의학적으로 정확",
                "explanation": "정확한 용어 사용 필요"
            }
        ],
        "examples": [
            {
                "ko": "화농성 여드름은 손으로 짜면 흉터가 남으니 절대 짜지 마세요. 레티노이드 연고와 경구 항생제로 치료하겠습니다.",
                "vi": "Mụn mủ nặn tay sẽ để lại scar nên tuyệt đối không nặn. Sẽ điều trị bằng thuốc bôi retinoid và kháng sinh uống.",
                "situation": "formal"
            },
            {
                "ko": "현장에서 '얼굴에 빨간 여드름이 많이 났다'고 하면 염증성 여드름입니다.",
                "vi": "Tại hiện trường, nếu nói 'mặt nhiều mụn đỏ' thì đó là mụn trứng cá viêm.",
                "situation": "onsite"
            },
            {
                "ko": "나 요즘 여드름 너무 심해. 피부과 가야 하나.",
                "vi": "Dạo này mụn trứng cá nặng quá. Phải đi khám da liễu không nhỉ.",
                "situation": "informal"
            }
        ],
        "relatedTerms": ["모낭염", "지루피부염", "여드름흉터", "이소트레티노인"]
    },
    {
        "slug": "me-day-nang",
        "korean": "두드러기",
        "vietnamese": "mề đay nặng",
        "hanja": None,
        "hanjaReading": None,
        "pronunciation": "두드러기",
        "meaningKo": "피부에 가려운 팽진이 갑자기 나타났다 사라지는 알레르기 반응. 통역 시 주의할 점은 베트nam어로 'mề đay'가 일반적이지만, 급성 두드러기는 'mề đay cấp', 만성 두드러기는 'mề đay mãn'으로 구분해야 한다는 것입니다. 특히 '혈관부종(angioedema)'을 동반한 경우 'phù mạch'으로 번역하고, 기도 폐쇄 위험이 있으므로 응급 상황임을 강조해야 합니다. 한국에서는 두드러기를 항히스타민제로 즉시 치료하지만, 베트남에서는 '스스로 낫는 것'으로 여겨 치료를 미루는 경우가 많습니다. 따라서 만성 두드러기의 경우 원인 파악과 장기 관리의 필요성을 설명해야 하며, 혈관부종 시 응급 치료의 중요성을 강조해야 합니다.",
        "meaningVi": "Phản ứng da dị ứng gây nổi mề sẩn ngứa, xuất hiện đột ngột và biến mất trong vài giờ. Có thể do thức ăn, thuốc, côn trùng cắn, stress. Nếu kèm phù mạch (sưng môi, mí mắt, họng) là nguy hiểm cần cấp cứu. Điều trị: thuốc kháng histamine.",
        "context": "응급실, 피부과 진료, 알레르기 클리닉",
        "culturalNote": "한국에서는 두드러기를 '즉시 치료해야 할 알레르기 반응'으로 인식하고 항히스타민제를 처방하지만, 베트남에서는 '피부가 좀 부은 것'으로 가볍게 여겨 방치하는 경우가 많습니다. 따라서 통역 시 두드러기가 심하면 아나필락시스로 진행될 수 있으며, 특히 혈관부종이 동반되면 기도 폐쇄로 생명이 위험할 수 있음을 강조해야 합니다. 또한 한국에서는 만성 두드러기의 원인을 찾기 위해 알레르기 검사를 하지만, 베트남에서는 검사 비용 부담으로 인해 원인을 파악하지 않고 증상만 치료하는 경향이 있습니다.",
        "commonMistakes": [
            {
                "mistake": "mề đay로만 표현하고 중증도 구분 없음",
                "correction": "급성/만성, 혈관부종 동반 여부 명시",
                "explanation": "응급 상황 여부를 판단해야 함"
            },
            {
                "mistake": "'부었다'를 sưng으로만 표현",
                "correction": "phù mạch(혈관부종) 또는 mề sẩn(팽진)으로 구분",
                "explanation": "증상을 정확히 전달해야 함"
            },
            {
                "mistake": "아나필락시스를 sốc dị ứng로만 표현",
                "correction": "sốc phản vệ(아나필락시스 쇼크)로 구체화",
                "explanation": "응급 상황을 명확히 해야 함"
            }
        ],
        "examples": [
            {
                "ko": "급성 두드러기로 전신에 팽진이 있고 입술이 부었습니다. 혈관부종이 동반되어 응급 상황이니 즉시 항히스타민제와 스테로이드를 투여하겠습니다.",
                "vi": "Mề đay cấp toàn thân có mề sẩn và môi sưng. Kèm phù mạch là tình huống cấp cứu, sẽ tiêm kháng histamine và steroid ngay.",
                "situation": "formal"
            },
            {
                "ko": "현장에서 '온몸에 붉은 두드러기가 나고 가렵다'고 하면 알레르기 반응입니다.",
                "vi": "Tại hiện trường, nếu nói 'toàn thân nổi mề đỏ và ngứa' thì đó là phản ứng dị ứng.",
                "situation": "onsite"
            },
            {
                "ko": "나 해산물 먹으면 두드러기 나. 항히스타민제 항상 가지고 다녀.",
                "vi": "Tôi ăn hải sản là nổi mề đay. Luôn mang theo thuốc kháng histamine.",
                "situation": "informal"
            }
        ],
        "relatedTerms": ["혈관부종", "아나필락시스", "식품알레르기", "항히스타민제"]
    },
    {
        "slug": "bach-bien-nang",
        "korean": "백반증",
        "vietnamese": "bạch biến nặng",
        "hanja": "白斑症",
        "hanjaReading": "白(흰 백) + 斑(얼룩 반) + 症(증세 증)",
        "pronunciation": "백반증",
        "meaningKo": "멜라닌 세포가 파괴되어 피부에 흰 반점이 생기는 자가면역 질환. 통역 시 주의할 점은 베트nam어로 'bạch biến'으로 표현하되, 증상이 심한 경우 'bạch biến nặng'으로 강조해야 한다는 것입니다. 특히 백반증이 전염되지 않는다는 점을 'không lây nhiễm'으로 반복 강조해야 하는데, 베트남에서는 피부 색소 이상을 전염병으로 오해하는 경향이 있어 사회적 낙인이 심합니다. 따라서 통역 시 질환의 자가면역적 원인과 비전염성을 명확히 설명해야 합니다. 한국에서는 광선치료나 타크로리무스 연고 등 다양한 치료를 시도하지만, 베트남에서는 치료 옵션이 제한적이고 경제적 부담도 커서 현실적인 치료 계획을 제시해야 합니다.",
        "meaningVi": "Bệnh tự miễn làm mất tế bào sắc tố da (melanin), gây các mảng trắng trên da. Không lây nhiễm, không đau nhưng ảnh hưởng tâm lý. Điều trị: quang trị liệu, thuốc bôi corticosteroid hoặc tacrolimus, ghép da (nếu ổn định). Hiệu quả điều trị khác nhau tùy người.",
        "context": "피부과 진료, 면역질환 클리닉, 심리 상담",
        "culturalNote": "한국에서는 백반증을 '치료 가능한 자가면역 질환'으로 인식하고 조기 치료를 강조하지만, 베트남에서는 '불치병' 또는 '전염병'으로 오해하여 사회적 격리를 경험하는 환자가 많습니다. 따라서 통역 시 백반증이 전염되지 않으며, 적절한 치료로 색소 재생이 가능하다는 점을 반복 강조해야 합니다. 또한 한국에서는 심리적 지원(상담, 지지 그룹)을 제공하지만, 베트남에서는 이러한 지원 체계가 부족하여 환자의 심리적 어려움을 이해하고 공감하는 태도가 중요합니다.",
        "commonMistakes": [
            {
                "mistake": "'백반증'을 bệnh trắng da로 직역",
                "correction": "bạch biến이 정확한 질환명",
                "explanation": "의학 용어 사용 필요"
            },
            {
                "mistake": "'색소가 없다'를 không có màu로만 표현",
                "correction": "mất sắc tố melanin(멜라닌 색소 소실)로 구체화",
                "explanation": "병리 기전을 정확히 전달해야 함"
            },
            {
                "mistake": "광선치료를 điều trị ánh sáng로만 표현",
                "correction": "quang trị liệu UVB(UVB 광선치료)로 구체화",
                "explanation": "치료법을 명확히 해야 함"
            }
        ],
        "examples": [
            {
                "ko": "백반증은 전염되지 않는 자가면역 질환입니다. 광선치료와 타크로리무스 연고로 색소 재생을 시도할 수 있으며, 심리적 지원도 중요합니다.",
                "vi": "Bạch biến là bệnh tự miễn không lây nhiễm. Có thể thử tái tạo sắc tố bằng quang trị liệu và thuốc bôi tacrolimus, hỗ trợ tâm lý cũng rất quan trọng.",
                "situation": "formal"
            },
            {
                "ko": "현장에서 '손과 얼굴에 흰 반점이 생긴다'고 하면 백반증 의심해야 합니다.",
                "vi": "Tại hiện trường, nếu nói 'tay và mặt có mảng trắng' thì nghi ngờ bạch biến.",
                "situation": "onsite"
            },
            {
                "ko": "친구가 백반증인데 사람들이 피해서 속상해해.",
                "vi": "Bạn tôi bị bạch biến, mọi người tránh nên buồn lắm.",
                "situation": "informal"
            }
        ],
        "relatedTerms": ["백색증", "색소침착", "자가면역질환", "광선치료"]
    }
]

# 중복 제거 및 데이터 추가
new_terms_filtered = [t for t in new_terms if t['slug'] not in existing_slugs]
data.extend(new_terms_filtered)

# 파일 저장
with open(file_path, 'w', encoding='utf-8') as f:
    json.dump(data, f, ensure_ascii=False, indent=2)

print(f"✅ 추가 완료: {len(new_terms_filtered)}개")
print(f"📊 전체 용어 수: {len(data)}개")
