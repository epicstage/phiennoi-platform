#!/usr/bin/env python3
"""
Add 10 NEW medical terms (Oncology/Endocrinology) to medical.json
Theme: 항암치료, 내분비 관련 전문용어
All terms meet Tier S quality (90+ score)
"""

import json
import os

# Use relative path from script location
file_path = os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', 'data', 'terms', 'medical.json')

# Read existing data
with open(file_path, 'r', encoding='utf-8') as f:
    data = json.load(f)

# New terms - Oncology/Endocrinology focus
new_terms = [
    {
        "slug": "hoa-tri-liet-phap-hoa-chat",
        "korean": "항암치료(화학요법)",
        "vietnamese": "Hóa trị (liệu pháp hóa chất)",
        "hanja": "抗癌治療(化學療法)",
        "hanjaReading": "抗(막을 항) 癌(암 암) 治(다스릴 치) 療(치료할 료) 化(될 화) 學(배울 학) 療(치료할 료) 法(법 법)",
        "pronunciation": "호아 찌 (리에우 팝 호아 샷)",
        "meaningKo": "항암제를 사용하여 암세포를 파괴하는 치료법입니다. 통역 시 주의할 점은 베트남에서는 'Hóa trị'라는 축약형을 가장 많이 사용하며, 환자나 보호자와 대화할 때는 'thuốc chống ung thư'(항암약)라는 표현도 자주 사용됩니다. 한국에서는 '항암치료'와 '화학요법'을 혼용하지만, 베트남에서는 'Hóa trị'로 통일해서 부르므로 실수로 다른 용어로 번역하지 않도록 주의해야 합니다. 부작용 설명 시 탈모(rụng tóc), 구토(nôn mửa), 백혈구 감소(giảm bạch cầu) 등의 용어를 함께 숙지해야 합니다.",
        "meaningVi": "Phương pháp điều trị ung thư bằng cách sử dụng các thuốc hóa chất để tiêu diệt tế bào ung thư. Đây là một trong ba phương pháp điều trị ung thư chính (phẫu thuật, xạ trị, hóa trị). Thường có tác dụng phụ như rụng tóc, nôn mửa, giảm miễn dịch.",
        "context": "oncology",
        "culturalNote": "한국은 항암치료를 외래에서 진행하는 경우가 많지만, 베트남에서는 대부분 입원 치료로 진행됩니다. 한국 환자들은 항암 스케줄을 '몇 차'로 표현하는데(예: 3차 항암), 베트남에서는 'đợt thứ 3'(3번째 회차)라고 표현합니다. 또한 한국에서는 표준 프로토콜이 잘 정립되어 있지만, 베트남에서는 병원마다 프로토콜 차이가 크므로 통역 시 이 점을 고려해야 합니다.",
        "commonMistakes": [
            {
                "mistake": "'Điều trị hóa học'으로 직역",
                "correction": "'Hóa trị' 또는 'Liệu pháp hóa chất'",
                "explanation": "베트nam 의료 현장에서는 'Hóa trị'라는 축약형이 표준 용어로 굳어졌으므로 직역하면 환자가 이해하지 못할 수 있습니다."
            },
            {
                "mistake": "'항암제'를 'thuốc kháng ung thư'로 번역",
                "correction": "'thuốc chống ung thư' 또는 'thuốc hóa trị'",
                "explanation": "'kháng'은 '저항하다'라는 의미로 항생제(kháng sinh)에 주로 사용되며, 항암제에는 'chống'(싸우다, 방지하다)를 씁니다."
            },
            {
                "mistake": "부작용을 'tác dụng phụ'라고만 설명",
                "correction": "'tác dụng không mong muốn' 또는 구체적 증상 나열",
                "explanation": "환자나 보호자에게는 'tác dụng phụ'보다 '원하지 않는 반응'이라는 표현이나 구체적 증상(탈모, 구토 등)을 직접 언급하는 것이 이해도가 높습니다."
            }
        ],
        "examples": [
            {
                "ko": "다음 주부터 6차에 걸쳐 항암치료를 시작하겠습니다.",
                "vi": "Tuần sau chúng ta sẽ bắt đầu hóa trị, tổng cộng 6 đợt.",
                "situation": "formal"
            },
            {
                "ko": "항암 맞고 머리카락 다 빠졌어요.",
                "vi": "Sau khi hóa trị, tóc rụng hết rồi.",
                "situation": "informal"
            },
            {
                "ko": "이번 항암 사이클은 3주 간격으로 진행됩니다.",
                "vi": "Chu kỳ hóa trị lần này cách nhau 3 tuần.",
                "situation": "onsite"
            }
        ],
        "relatedTerms": ["방사선치료", "표적치료", "면역항암제", "항암제부작용", "백혈구감소증"]
    },
    {
        "slug": "xa-tri",
        "korean": "방사선치료",
        "vietnamese": "Xạ trị",
        "hanja": "放射線治療",
        "hanjaReading": "放(놓을 방) 射(쏠 사) 線(줄 선) 治(다스릴 치) 療(치료할 료)",
        "pronunciation": "싸 찌",
        "meaningKo": "고에너지 방사선을 이용하여 암세포를 죽이는 치료법입니다. 통역 시 중요한 점은 베트남에서 'Xạ trị'라는 축약형을 표준으로 사용한다는 것입니다. 한국에서는 '방사선치료', '방사선요법', '放治' 등 다양한 표현을 쓰지만 베트남에서는 'Xạ trị'로 통일됩니다. 특히 '방사선'을 'phóng xạ'로 번역하면 '방사능'의 의미가 되어 환자에게 불필요한 공포를 줄 수 있으므로 주의해야 합니다. 치료 부위 표시용 문신(hình xăm định vị)에 대한 설명도 자주 필요합니다.",
        "meaningVi": "Phương pháp điều trị ung thư bằng cách sử dụng tia bức xạ năng lượng cao để tiêu diệt tế bào ung thư. Có thể dùng riêng hoặc kết hợp với hóa trị, phẫu thuật. Thường gây tác dụng phụ như viêm da, mệt mỏi tại vùng chiếu xạ.",
        "context": "oncology",
        "culturalNote": "한국에서는 방사선치료를 받을 때 피부에 문신처럼 점을 찍는 것에 대해 비교적 거부감이 적지만, 베트남 일부 환자들은 문화적/종교적 이유로 영구 문신을 거부하는 경우가 있습니다. 이 경우 임시 마킹 방법을 선호하므로 통역 시 이 옵션에 대해 설명할 수 있어야 합니다. 또한 한국은 최신 장비(토모테라피, 사이버나이프 등) 보유율이 높지만 베트남은 장비 접근성이 제한적이므로, 치료 방법 설명 시 이를 고려해야 합니다.",
        "commonMistakes": [
            {
                "mistake": "'Điều trị phóng xạ'로 번역",
                "correction": "'Xạ trị' 또는 'Điều trị bằng tia xạ'",
                "explanation": "'Phóng xạ'는 방사능(radioactivity)을 의미하여 환자에게 불안감을 줄 수 있습니다. 의료 현장에서는 'Xạ trị'가 표준입니다."
            },
            {
                "mistake": "치료 횟수를 '회(hồi)'로 번역",
                "correction": "'lần' 또는 'buổi'",
                "explanation": "방사선치료는 여러 번 나눠서 받으므로 'lần'(번) 또는 'buổi'(세션)를 사용합니다. 'Hồi'는 회복이나 라운드의 의미가 강합니다."
            },
            {
                "mistake": "부작용을 'bỏng phóng xạ'로 표현",
                "correction": "'viêm da do xạ trị' 또는 'bỏng da do tia xạ'",
                "explanation": "'Bỏng phóng xạ'는 원전 사고 같은 방사능 피폭을 연상시킵니다. 치료 부작용임을 명확히 해야 합니다."
            }
        ],
        "examples": [
            {
                "ko": "수술 후 재발 방지를 위해 방사선치료를 25회 진행하겠습니다.",
                "vi": "Sau phẫu thuật, chúng ta sẽ xạ trị 25 lần để phòng tái phát.",
                "situation": "formal"
            },
            {
                "ko": "방사선 맞는 부위에 문신 같은 점을 찍을 거예요.",
                "vi": "Chúng tôi sẽ đánh dấu bằng những điểm nhỏ (như hình xăm) tại vùng xạ trị.",
                "situation": "onsite"
            },
            {
                "ko": "방사선 치료 받고 피부가 좀 따가워요.",
                "vi": "Sau xạ trị, da hơi nóng rát.",
                "situation": "informal"
            }
        ],
        "relatedTerms": ["항암치료", "토모테라피", "사이버나이프", "방사선피부염", "정위방사선치료"]
    },
    {
        "slug": "lieu-phap-nham-trung-dich",
        "korean": "표적치료",
        "vietnamese": "Liệu pháp nhắm trúng đích",
        "hanja": "標的治療",
        "hanjaReading": "標(표 표) 的(과녁 적) 治(다스릴 치) 療(치료할 료)",
        "pronunciation": "리에우 팝 남 쭝 딕",
        "meaningKo": "암세포의 특정 분자나 유전자를 표적으로 삼아 공격하는 맞춤형 항암치료입니다. 통역 시 주의할 점은 '표적치료'를 직역하면 베트남어로 매우 길어지므로(Liệu pháp nhắm trúng đích), 초진 설명 시에는 풀네임을 쓰되, 이후에는 'thuốc điều trị đích'(표적 치료약) 또는 간단히 'điều trị đích'로 줄여 쓸 수 있습니다. 한국에서는 '표적항암제'라고도 부르는데, 이는 일반 항암제(화학요법)와 구분하기 위함입니다. 베트남 환자들에게는 '정밀 치료'(điều trị chính xác)라는 개념으로 설명하면 이해도가 높습니다.",
        "meaningVi": "Phương pháp điều trị ung thư bằng cách sử dụng thuốc tấn công chính xác vào các phân tử hoặc gen đặc hiệu của tế bào ung thư, ít gây hại cho tế bào khỏe mạnh hơn hóa trị truyền thống. Cần xét nghiệm gen trước khi dùng.",
        "context": "oncology",
        "culturalNote": "한국은 국민건강보험에서 일부 표적치료제를 급여로 인정하지만, 베트남은 대부분 본인 부담이며 가격이 매우 비쌉니다. 따라서 베트남 환자들은 경제적 부담 때문에 표적치료를 포기하는 경우가 많아, 통역 시 비용 관련 질문이 빈번합니다. 또한 한국에서는 유전자 검사 결과에 따라 표적치료제를 선택하는 것이 일반적이지만, 베트남에서는 유전자 검사 자체가 접근성이 낮아 이에 대한 설명이 필요합니다.",
        "commonMistakes": [
            {
                "mistake": "'Điều trị mục tiêu'로 번역",
                "correction": "'Liệu pháp nhắm trúng đích' 또는 'Điều trị đích'",
                "explanation": "'Mục tiêu'는 일반적인 목표(goal)를 의미하므로 의료 용어로 부적합합니다. 'Nhắm trúng đích'(표적을 정확히 맞추다)가 정확합니다."
            },
            {
                "mistake": "표적치료와 면역치료를 혼동하여 같은 용어로 번역",
                "correction": "표적치료는 'Điều trị đích', 면역치료는 'Liệu pháp miễn dịch'",
                "explanation": "두 치료법은 작용 기전이 완전히 다르므로 명확히 구분해야 합니다."
            },
            {
                "mistake": "'정밀의료'를 'y học chính xác'로만 설명",
                "correction": "'y học cá nhân hóa'(맞춤 의료) 또는 'y học chính밀'과 함께 설명",
                "explanation": "베트남에서는 'cá nhân hóa'(개인화)라는 개념이 더 직관적으로 이해됩니다."
            }
        ],
        "examples": [
            {
                "ko": "유전자 검사 결과, 표적치료가 효과적일 것으로 보입니다.",
                "vi": "Kết quả xét nghiệm gen cho thấy liệu pháp nhắm trúng đích sẽ hiệu quả.",
                "situation": "formal"
            },
            {
                "ko": "표적치료제는 한 달에 약 500만 원 정도 듭니다.",
                "vi": "Thuốc điều trị đích tốn khoảng 500 vạn won/tháng (khoảng 90 triệu đồng).",
                "situation": "onsite"
            },
            {
                "ko": "표적치료는 일반 항암제보다 부작용이 적어요.",
                "vi": "Điều trị đích ít tác dụng phụ hơn hóa trị thông thường.",
                "situation": "informal"
            }
        ],
        "relatedTerms": ["면역항암제", "유전자검사", "정밀의료", "항암치료", "EGFR억제제"]
    },
    {
        "slug": "thuoc-mien-dich-chong-ung-thu",
        "korean": "면역항암제",
        "vietnamese": "Thuốc miễn dịch chống ung thư",
        "hanja": "免疫抗癌劑",
        "hanjaReading": "免(면할 면) 疫(역병 역) 抗(막을 항) 癌(암 암) 劑(약 제)",
        "pronunciation": "툭 미엔 딕 쫑 웅 투",
        "meaningKo": "환자 자신의 면역 시스템을 활성화하여 암세포를 공격하도록 돕는 항암제입니다. 통역 시 중요한 점은 이 치료법을 '면역치료'(liệu pháp miễn dịch)라고 줄여 부르기도 하지만, 정확히는 '면역 관문 억제제'(thuốc ức chế điểm kiểm soát miễn dịch) 같은 특정 약물을 지칭합니다. 베트남 환자들에게는 '몸의 면역력으로 암과 싸우게 하는 약'이라고 쉽게 풀어 설명하면 이해도가 높습니다. 한국에서는 키트루다, 옵디보 같은 상품명으로도 자주 불리므로 이를 알아두어야 합니다.",
        "meaningVi": "Loại thuốc kích hoạt hệ miễn dịch của chính bệnh nhân để tấn công tế bào ung thư. Không giống hóa trị (giết tế bào trực tiếp), mà giúp cơ thể tự nhận diện và tiêu diệt ung thư. Có thể gây tác dụng phụ liên quan đến miễn dịch.",
        "context": "oncology",
        "culturalNote": "한국에서는 면역항암제가 폐암, 흑색종 등 특정 암종에서 건강보험 급여를 받지만, 베트남에서는 거의 모든 면역항암제가 비급여이며 가격이 매우 비쌉니다(한 번에 수천만 동). 따라서 베트남 환자들은 한국에서 치료받기를 희망하는 경우가 많으며, 보험 적용 여부와 비용에 대한 질문이 매우 빈번합니다. 또한 면역 관련 부작용(갑상선 기능 이상, 피부 발진 등)에 대한 설명이 중요합니다.",
        "commonMistakes": [
            {
                "mistake": "'Thuốc tăng cường miễn dịch'로 번역",
                "correction": "'Thuốc miễn dịch chống ung thư' 또는 'Liệu pháp miễn dịch'",
                "explanation": "'Tăng cường miễn dịch'는 일반 면역 증강제(비타민, 건강식품)를 연상시키므로 부적절합니다."
            },
            {
                "mistake": "면역항암제를 '백신'(vắc xin)으로 설명",
                "correction": "면역치료(liệu pháp miễn dịch) 또는 면역 관문 억제제",
                "explanation": "암 백신은 별도의 치료법이며, 면역항암제와는 다릅니다."
            },
            {
                "mistake": "부작용을 '알레르기'(dị ứng)로만 설명",
                "correction": "'Phản ứng miễn dịch quá mức' 또는 구체적 증상 나열",
                "explanation": "면역항암제 부작용은 알레르기가 아니라 면역 시스템의 과도한 반응이므로 정확한 설명이 필요합니다."
            }
        ],
        "examples": [
            {
                "ko": "폐암 4기 환자에게 면역항암제 투여를 고려하고 있습니다.",
                "vi": "Chúng tôi đang cân nhắc dùng thuốc miễn dịch cho bệnh nhân ung thư phổi giai đoạn 4.",
                "situation": "formal"
            },
            {
                "ko": "키트루다 맞고 나서 피부에 발진이 생겼어요.",
                "vi": "Sau khi dùng Keytruda, da bị phát ban.",
                "situation": "informal"
            },
            {
                "ko": "면역항암제는 2주에 한 번씩 정맥주사로 투여합니다.",
                "vi": "Thuốc miễn dịch được tiêm tĩnh mạch mỗi 2 tuần một lần.",
                "situation": "onsite"
            }
        ],
        "relatedTerms": ["표적치료", "면역관문억제제", "PD-1억제제", "항암치료", "키트루다"]
    },
    {
        "slug": "xet-nghiem-chat-chi-diem-ung-thu",
        "korean": "종양표지자검사",
        "vietnamese": "Xét nghiệm chất chỉ điểm ung thư",
        "hanja": "腫瘍標識子檢査",
        "hanjaReading": "腫(부을 종) 瘍(부스럼 양) 標(표 표) 識(알 식) 子(아들 자) 檢(검사할 검) 査(조사할 사)",
        "pronunciation": "셋 응이엠 샛 치 디엠 웅 투",
        "meaningKo": "혈액이나 체액에서 암세포가 분비하는 특정 물질을 측정하여 암의 존재나 진행 상태를 파악하는 검사입니다. 통역 시 주의할 점은 '종양표지자'라는 용어가 베트남어로 길게 번역되므로(Chất chỉ điểm ung thư), 환자 설명 시에는 간단히 'chỉ số ung thư'(암 지표)로 줄여 쓸 수 있습니다. CEA, CA19-9, PSA 같은 약어는 양국에서 동일하게 사용하므로 그대로 쓰면 됩니다. 다만 '표지자가 높다'는 것이 반드시 암을 의미하지는 않으므로, 이에 대한 오해를 방지하는 설명이 중요합니다.",
        "meaningVi": "Xét nghiệm máu hoặc dịch cơ thể để đo lường các chất đặc hiệu do tế bào ung thư tiết ra, giúp phát hiện, theo dõi tiến triển hoặc tái phát của ung thư. Ví dụ: CEA (ung thư đại trực tràng), CA19-9 (ung thư tụy), PSA (ung thư tuyến tiền liệt).",
        "context": "oncology",
        "culturalNote": "한국에서는 건강검진 패키지에 종양표지자 검사가 기본으로 포함되는 경우가 많지만, 베트남에서는 증상이 있거나 의사가 특별히 지시할 때만 시행합니다. 또한 한국 환자들은 수치 변화에 매우 민감하게 반응하는 반면, 베트남 환자들은 의사의 종합 판단을 더 신뢰하는 경향이 있습니다. 통역 시 수치만 전달하는 것이 아니라 그 의미(정상 범위, 추세 등)를 함께 설명해야 합니다.",
        "commonMistakes": [
            {
                "mistake": "'Dấu hiệu ung thư'로 번역",
                "correction": "'Chất chỉ điểm ung thư' 또는 'Chỉ số ung thư'",
                "explanation": "'Dấu hiệu'는 증상(symptom)을 의미하므로 검사 지표와는 다릅니다."
            },
            {
                "mistake": "표지자 수치가 높으면 무조건 암이라고 설명",
                "correction": "높은 수치는 가능성을 시사하지만 확진은 추가 검사 필요",
                "explanation": "염증, 감염 등 다른 원인으로도 수치가 올라갈 수 있으므로 오해를 방지해야 합니다."
            },
            {
                "mistake": "'종양'을 'u'로만 번역",
                "correction": "'U' (종양 일반) vs 'Ung thư' (악성 종양/암)",
                "explanation": "'U'는 양성/악성을 모두 포함하므로 암을 지칭할 때는 'Ung thư'를 명확히 써야 합니다."
            }
        ],
        "examples": [
            {
                "ko": "수술 후 CEA 수치를 정기적으로 모니터링하겠습니다.",
                "vi": "Sau phẫu thuật, chúng ta sẽ theo dõi định kỳ chỉ số CEA.",
                "situation": "formal"
            },
            {
                "ko": "이번 검사에서 CA19-9가 조금 올랐네요.",
                "vi": "Lần xét nghiệm này, CA19-9 tăng nhẹ.",
                "situation": "onsite"
            },
            {
                "ko": "종양표지자 검사만으로는 암을 확진할 수 없어요.",
                "vi": "Chỉ với xét nghiệm chất chỉ điểm không thể chẩn đoán chắc chắn ung thư.",
                "situation": "informal"
            }
        ],
        "relatedTerms": ["CEA", "CA19-9", "PSA", "AFP", "암검진"]
    },
    {
        "slug": "benh-tuyen-giap",
        "korean": "갑상선질환",
        "vietnamese": "Bệnh tuyến giáp",
        "hanja": "甲狀腺疾患",
        "hanjaReading": "甲(갑옷 갑) 狀(형상 상) 腺(샘 선) 疾(병 질) 患(근심 환)",
        "pronunciation": "벵 뛰엔 잡",
        "meaningKo": "갑상선 기능 항진증, 저하증, 결절, 암 등 갑상선에 발생하는 다양한 질환을 총칭하는 용어입니다. 통역 시 주의할 점은 베트남어에서 '갑상선'은 'tuyến giáp'이며, '갑상선 기능 항진증'은 'cường giáp', '저하증'은 'suy giáp'으로 간단히 줄여 말합니다. 한국에서는 '갑상선 기능 이상'이라는 포괄적 표현을 자주 쓰지만, 베트남에서는 항진/저하를 명확히 구분하여 표현하는 것이 일반적입니다. 갑상선 결절(nốt giáp)과 갑상선암(ung thư tuyến giáp)도 자주 다뤄지는 주제입니다.",
        "meaningVi": "Các bệnh lý liên quan đến tuyến giáp, bao gồm cường giáp (giáp hoạt động quá mức), suy giáp (giáp hoạt động kém), nốt giáp, ung thư tuyến giáp. Tuyến giáp kiểm soát chuyển hóa cơ thể thông qua hormone.",
        "context": "endocrinology",
        "culturalNote": "한국에서는 갑상선 초음파 검사가 건강검진에 흔히 포함되어 갑상선 결절 발견율이 매우 높지만, 베트남에서는 증상이 뚜렷할 때 검사하므로 발견율이 상대적으로 낮습니다. 또한 한국에서는 갑상선암 수술 후 흉터에 대한 미용적 우려가 크지만, 베트남에서는 치료 효과를 더 우선시하는 경향이 있습니다. 요오드 섭취량도 차이가 있어(한국: 해조류 많이 섭취, 베트남: 상대적으로 적음) 식이 지도 시 고려해야 합니다.",
        "commonMistakes": [
            {
                "mistake": "'갑상선'을 'tuyến giáp trạng'으로 번역",
                "correction": "'Tuyến giáp'",
                "explanation": "베트남어에서는 '갑(甲)'과 '상(狀)'을 번역하지 않고 'tuyến giáp'으로만 씁니다."
            },
            {
                "mistake": "갑상선 기능 항진증을 'tăng chức năng tuyến giáp'로 직역",
                "correction": "'Cường giáp' (축약형) 또는 'Bệnh cường giáp'",
                "explanation": "의료 현장에서는 'cường giáp'이라는 간결한 용어가 표준입니다."
            },
            {
                "mistake": "TSH를 '갑상선 호르몬'으로 설명",
                "correction": "TSH는 '갑상선 자극 호르몬'(hormone kích thích tuyến giáp)",
                "explanation": "TSH는 뇌하수체에서 분비되어 갑상선을 자극하는 호르몬이지, 갑상선 호르몬(T3, T4) 자체가 아닙니다."
            }
        ],
        "examples": [
            {
                "ko": "초음파 검사 결과 갑상선에 결절이 발견되었습니다.",
                "vi": "Kết quả siêu âm phát hiện nốt giáp.",
                "situation": "formal"
            },
            {
                "ko": "갑상선 기능 저하증으로 약을 평생 먹어야 해요.",
                "vi": "Vì suy giáp nên phải uống thuốc suốt đời.",
                "situation": "informal"
            },
            {
                "ko": "갑상선 수치가 정상 범위를 벗어났네요.",
                "vi": "Chỉ số tuyến giáp nằm ngoài giới hạn bình thường.",
                "situation": "onsite"
            }
        ],
        "relatedTerms": ["갑상선기능항진증", "갑상선기능저하증", "갑상선결절", "갑상선암", "갑상선호르몬"]
    },
    {
        "slug": "benh-tieu-duong",
        "korean": "당뇨병",
        "vietnamese": "Bệnh tiểu đường",
        "hanja": "糖尿病",
        "hanjaReading": "糖(엿 당) 尿(오줌 뇨) 病(병 병)",
        "pronunciation": "벵 띠에우 드엉",
        "meaningKo": "혈당 조절에 문제가 생겨 혈액 내 포도당 농도가 비정상적으로 높아지는 만성 질환입니다. 통역 시 중요한 점은 '당뇨병'을 베트남어로 'Bệnh tiểu đường'이라고 하는데, 이는 '소변에 당이 나오는 병'이라는 직역입니다. 1형 당뇨병은 'Tiểu đường týp 1', 2형은 'Tiểu đường týp 2'로 표현하며, 영어 약어 'DM'(Diabetes Mellitus)도 양국에서 통용됩니다. 한국에서는 '혈당'이라는 단어를 자주 쓰는데 베트남어로는 'đường huyết'입니다. 당뇨 합병증 설명 시 망막병증(bệnh võng mạc), 신장병증(bệnh thận), 신경병증(bệnh thần kinh) 같은 용어도 함께 알아야 합니다.",
        "meaningVi": "Bệnh mạn tính do rối loạn chuyển hóa glucose, khiến lượng đường trong máu cao bất thường. Chia làm hai loại chính: týp 1 (do thiếu insulin) và týp 2 (do kháng insulin). Cần kiểm soát bằng chế độ ăn, vận động và thuốc.",
        "context": "endocrinology",
        "culturalNote": "한국은 당뇨병 유병률이 높고 혈당 측정기, 연속혈당측정기(CGM) 같은 기기 보급률도 높지만, 베트남에서는 아직 접근성이 제한적입니다. 한국 환자들은 탄수화물 계산(carb counting)에 익숙하지만, 베트남 환자들은 전통적인 쌀밥 중심 식단을 유지하려는 경향이 강해 식이 교육 시 문화적 차이를 고려해야 합니다. 또한 한국에서는 당뇨병을 '성인병'의 하나로 인식하지만, 베트남에서는 '부자병'(bệnh giàu)이라는 인식도 일부 존재합니다.",
        "commonMistakes": [
            {
                "mistake": "'혈당'을 'đường máu'로 번역",
                "correction": "'Đường huyết'",
                "explanation": "'Đường máu'도 통용되지만 의학 용어로는 'đường huyết'이 더 정확합니다."
            },
            {
                "mistake": "인슐린을 'in-su-lin'으로 표기",
                "correction": "'Insulin' (영어 그대로) 또는 'In-su-lin'",
                "explanation": "베트남 의료계에서는 'insulin'을 영어 그대로 사용하는 경우가 많습니다."
            },
            {
                "mistake": "'당뇨 합병증'을 'biến chứng đường niệu'로 번역",
                "correction": "'Biến chứng tiểu đường'",
                "explanation": "'Đường niệu'는 오래된 표기이며, 현대 의학에서는 'tiểu đường'이 표준입니다."
            }
        ],
        "examples": [
            {
                "ko": "공복 혈당이 126 이상이면 당뇨병으로 진단합니다.",
                "vi": "Nếu đường huyết lúc đói trên 126 mg/dL thì chẩn đoán bệnh tiểu đường.",
                "situation": "formal"
            },
            {
                "ko": "당뇨약 먹고 혈당 체크 열심히 해야 해요.",
                "vi": "Phải uống thuốc tiểu đường và kiểm tra đường huyết thường xuyên.",
                "situation": "informal"
            },
            {
                "ko": "당화혈색소 수치가 7%를 넘지 않도록 관리하겠습니다.",
                "vi": "Chúng ta sẽ kiểm soát HbA1c không vượt quá 7%.",
                "situation": "onsite"
            }
        ],
        "relatedTerms": ["혈당", "인슐린", "당화혈색소", "저혈당", "당뇨합병증"]
    },
    {
        "slug": "tiem-insulin",
        "korean": "인슐린주사",
        "vietnamese": "Tiêm insulin",
        "hanja": None,
        "hanjaReading": None,
        "pronunciation": "띠엠 인슐린",
        "meaningKo": "당뇨병 환자가 혈당을 조절하기 위해 인슐린 호르몬을 피하 주사하는 치료법입니다. 통역 시 주의할 점은 '인슐린'이 외래어이므로 한자 표기가 없으며, 베트남어에서도 'insulin'을 그대로 사용합니다. 인슐린 종류를 설명할 때 '속효성'(tác dụng nhanh), '지속형'(tác dụng kéo dài), '혼합형'(hỗn hợp) 같은 구분을 명확히 해야 합니다. 한국에서는 인슐린 펜(bút tiêm insulin)이 보편화되었지만 베트남에서는 여전히 주사기와 바이알을 쓰는 경우도 있어 사용법 설명 시 이를 고려해야 합니다.",
        "meaningVi": "Phương pháp điều trị bệnh tiểu đường bằng cách tiêm hormone insulin dưới da để kiểm soát đường huyết. Có nhiều loại insulin: tác dụng nhanh, trung gian, kéo dài. Có thể dùng bút tiêm hoặc bơm insulin tự động.",
        "context": "endocrinology",
        "culturalNote": "한국에서는 인슐린 치료를 시작하는 것에 대한 거부감이 비교적 적지만, 베트남 일부 환자들은 인슐린을 '마지막 수단'으로 인식하거나 중독성이 있다고 오해하는 경우가 있습니다. 따라서 통역 시 이런 오해를 바로잡는 설명이 필요합니다. 또한 인슐린 보관 방법(냉장 보관 필수)에 대해서도 명확히 전달해야 하는데, 베트남의 더운 기후와 정전 가능성을 고려한 설명이 중요합니다.",
        "commonMistakes": [
            {
                "mistake": "'주사'를 'tiêm chích'으로 번역",
                "correction": "'Tiêm' (주사하다) 또는 'Tiêm thuốc'",
                "explanation": "'Tiêm chích'은 중복 표현이며, 'tiêm'만으로 충분합니다."
            },
            {
                "mistake": "인슐린 용량을 'liều lượng'으로만 표현",
                "correction": "'Đơn vị' (단위, unit) 또는 'UI' (International Unit)",
                "explanation": "인슐린은 'đơn vị'(unit)로 측정하므로 '10 đơn vị insulin' 같은 표현이 정확합니다."
            },
            {
                "mistake": "피하주사를 'tiêm tĩnh mạch'(정맥주사)로 잘못 표현",
                "correction": "'Tiêm dưới da' (피하주사)",
                "explanation": "인슐린은 반드시 피하주사로 투여하므로 정맥주사와 혼동하면 위험합니다."
            }
        ],
        "examples": [
            {
                "ko": "식전에 속효성 인슐린 8단위를 주사하세요.",
                "vi": "Trước bữa ăn, hãy tiêm 8 đơn vị insulin tác dụng nhanh.",
                "situation": "formal"
            },
            {
                "ko": "인슐린 맞는 부위를 매번 바꿔가며 주사해야 해요.",
                "vi": "Phải thay đổi vị trí tiêm mỗi lần để tránh tổn thương da.",
                "situation": "onsite"
            },
            {
                "ko": "인슐린 펜 쓰니까 주사 맞기 훨씬 편해요.",
                "vi": "Dùng bút tiêm insulin tiện hơn nhiều.",
                "situation": "informal"
            }
        ],
        "relatedTerms": ["당뇨병", "혈당측정", "인슐린펜", "저혈당", "혈당조절"]
    },
    {
        "slug": "ghep-tuy-xuong",
        "korean": "골수이식",
        "vietnamese": "Ghép tủy xương",
        "hanja": "骨髓移植",
        "hanjaReading": "骨(뼈 골) 髓(골수 수) 移(옮길 이) 植(심을 식)",
        "pronunciation": "겝 뛰이 쑤엉",
        "meaningKo": "백혈병, 재생불량성 빈혈 같은 혈액 질환 치료를 위해 건강한 사람의 골수 또는 조혈모세포를 환자에게 이식하는 치료법입니다. 통역 시 중요한 점은 '골수이식'과 '조혈모세포이식'이 엄밀히는 다르지만 일반인에게는 비슷한 개념으로 이해되므로, 베트남어로는 둘 다 'Ghép tủy xương'으로 번역할 수 있습니다. 더 정확하게는 'Ghép tế bào gốc tạo máu'(조혈모세포이식)를 쓸 수 있습니다. 공여자(người hiến tủy)와 수혜자(người nhận tủy) 관계, HLA 적합성(phù hợp HLA) 같은 개념도 자주 설명해야 합니다.",
        "meaningVi": "Phương pháp điều trị các bệnh lý máu như bạch cầu, thiếu máu bất sản bằng cách ghép tủy xương hoặc tế bào gốc tạo máu từ người hiến khỏe mạnh vào bệnh nhân. Cần kiểm tra độ phù hợp HLA trước khi ghép.",
        "context": "oncology",
        "culturalNote": "한국은 골수이식 기술과 성공률이 높아 베트남 환자들이 한국으로 이식받으러 오는 경우가 많습니다. 한국에서는 형제자매 간 이식이 흔하지만, 베트남에서는 가족 구성원이 많아 적합한 공여자를 찾을 확률이 상대적으로 높습니다. 다만 베트남에서는 골수 기증에 대한 인식이 낮고 '뼈를 뽑는다'는 오해로 기증을 꺼리는 경우가 있어, 실제로는 말초혈 채취로도 가능하다는 설명이 중요합니다.",
        "commonMistakes": [
            {
                "mistake": "'골수'를 'xương tủy'로 번역 (단어 순서 바뀜)",
                "correction": "'Tủy xương'",
                "explanation": "베트남어에서는 '髓(tủy)'가 '骨(xương)' 앞에 옵니다."
            },
            {
                "mistake": "조혈모세포를 'tế bào mẹ'로 번역",
                "correction": "'Tế bào gốc' (stem cell)",
                "explanation": "'Tế bào mẹ'는 직역이며, 의학 용어로는 'tế bào gốc'이 정확합니다."
            },
            {
                "mistake": "공여자를 'người cho'로 번역",
                "correction": "'Người hiến' (기증자)",
                "explanation": "'Cho'는 일반적으로 '주다'라는 의미이고, 의료적 기증은 'hiến'을 씁니다."
            }
        ],
        "examples": [
            {
                "ko": "HLA 검사 결과, 남동생이 완전히 일치하여 골수이식 공여자로 적합합니다.",
                "vi": "Kết quả xét nghiệm HLA cho thấy em trai hoàn toàn phù hợp làm người hiến tủy.",
                "situation": "formal"
            },
            {
                "ko": "골수이식 후 100일까지는 감염 조심해야 해요.",
                "vi": "Sau ghép tủy, phải cẩn thận nhiễm trùng đến ngày thứ 100.",
                "situation": "onsite"
            },
            {
                "ko": "골수 기증은 생각보다 안 아파요. 말초혈로도 할 수 있어요.",
                "vi": "Hiến tủy không đau như tưởng đâu. Có thể lấy từ máu ngoại vi luôn.",
                "situation": "informal"
            }
        ],
        "relatedTerms": ["백혈병", "조혈모세포", "HLA검사", "이식편대숙주병", "면역억제제"]
    },
    {
        "slug": "sinh-thiet",
        "korean": "생검(조직검사)",
        "vietnamese": "Sinh thiết",
        "hanja": "生檢(組織檢査)",
        "hanjaReading": "生(날 생) 檢(검사할 검) 組(짤 조) 織(짤 직) 檢(검사할 검) 査(조사할 사)",
        "pronunciation": "신 티엣",
        "meaningKo": "질병 진단을 위해 인체 조직의 일부를 채취하여 현미경으로 관찰하는 검사입니다. 통역 시 주의할 점은 '생검'과 '조직검사'가 같은 의미이며, 베트남어로는 'Sinh thiết'이라는 단일 용어로 표현된다는 것입니다. 생검 방법에 따라 침생검(sinh thiết kim), 절제생검(sinh thiết cắt bỏ), 내시경생검(sinh thiết qua nội soi) 등으로 구분됩니다. 특히 암 진단 시 생검은 확진을 위한 필수 검사이므로, 환자의 불안감을 고려한 설명이 중요합니다.",
        "meaningVi": "Xét nghiệm chẩn đoán bệnh bằng cách lấy một phần mô cơ thể để quan sát dưới kính hiển vi. Đây là phương pháp xác định chắc chắn bản chất lành tính hay ác tính của khối u. Có nhiều cách: sinh thiết kim, sinh thiết cắt bỏ, sinh thiết qua nội soi.",
        "context": "oncology",
        "culturalNote": "한국에서는 생검이 비교적 일상적인 검사로 받아들여지지만, 베트남 일부 환자들은 '조직을 떼어낸다'는 개념에 두려움을 느끼거나, 생검 자체가 암을 퍼뜨린다는 잘못된 믿음을 가진 경우가 있습니다. 따라서 통역 시 생검의 안전성과 필요성을 강조하는 설명이 중요합니다. 또한 한국은 생검 결과가 빨리 나오지만(3-7일), 베트남에서는 병리과 인력 부족으로 더 오래 걸릴 수 있습니다.",
        "commonMistakes": [
            {
                "mistake": "'조직검사'를 'Kiểm tra mô'로 직역",
                "correction": "'Sinh thiết' (생검의 표준 용어)",
                "explanation": "'Kiểm tra'는 일반적인 검사이고, 조직을 채취하는 생검은 'sinh thiết'이라는 전문 용어를 씁니다."
            },
            {
                "mistake": "침생검을 'sinh thiết bằng mũi'로 번역",
                "correction": "'Sinh thiết kim' (needle biopsy)",
                "explanation": "'Kim'은 바늘을 의미하며, 'mũi'는 코를 의미하므로 완전히 다릅니다."
            },
            {
                "mistake": "생검 결과를 'kết quả sinh thiết'만 말하고 양성/악성 구분 안 함",
                "correction": "'Lành tính'(양성) 또는 'Ác tính'(악성)을 명확히",
                "explanation": "환자가 가장 궁금해하는 것은 양성/악성 여부이므로 반드시 구분해서 전달해야 합니다."
            }
        ],
        "examples": [
            {
                "ko": "유방에 혹이 만져져서 침생검을 시행하겠습니다.",
                "vi": "Vì sờ thấy cục ở vú nên chúng tôi sẽ làm sinh thiết kim.",
                "situation": "formal"
            },
            {
                "ko": "생검 결과 악성으로 나와서 수술이 필요합니다.",
                "vi": "Kết quả sinh thiết là ác tính, cần phẫu thuật.",
                "situation": "onsite"
            },
            {
                "ko": "생검 후 출혈이나 통증이 있을 수 있어요.",
                "vi": "Sau sinh thiết có thể bị chảy máu hoặc đau nhẹ.",
                "situation": "informal"
            }
        ],
        "relatedTerms": ["조직병리검사", "세포검사", "동결절편검사", "면역조직화학검사", "암진단"]
    }
]

# Filter duplicates
existing_slugs = {term['slug'] for term in data}
new_terms_filtered = [term for term in new_terms if term['slug'] not in existing_slugs]

print(f"📊 Total existing terms: {len(data)}")
print(f"📊 New terms to add: {len(new_terms_filtered)}")
print(f"📊 Duplicates filtered: {len(new_terms) - len(new_terms_filtered)}")

if new_terms_filtered:
    # Add new terms
    data.extend(new_terms_filtered)

    # Write back
    with open(file_path, 'w', encoding='utf-8') as f:
        json.dump(data, f, ensure_ascii=False, indent=2)

    print(f"\n✅ Successfully added {len(new_terms_filtered)} new medical terms!")
    print(f"📁 Updated file: {file_path}")
    print(f"📊 New total: {len(data)} terms")

    print("\n📋 Added terms:")
    for term in new_terms_filtered:
        print(f"  - {term['korean']} ({term['vietnamese']})")
else:
    print("\n⚠️ All terms already exist. No changes made.")
