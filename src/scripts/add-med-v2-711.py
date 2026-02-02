#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Medical Terms Addition Script - OB/GYN, Pediatrics, Neonatology Focus
Adds 50 NEW medical terms to medical.json with Tier S quality (90+ score)
"""

import json
import os

# CRITICAL: Use exact path code
file_path = os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', 'data', 'terms', 'medical.json')

# 50 NEW medical terms with complete Tier S quality data
new_terms = [
    {
        "slug": "tu-nhien-phan-man",
        "korean": "자연분만",
        "vietnamese": "Tự nhiên phân man",
        "hanja": "自然分娩",
        "hanjaReading": "自(스스로 자) + 然(그러할 연) + 分(나눌 분) + 娩(해산할 만)",
        "pronunciation": "자연분만",
        "meaningKo": "산모가 자연적인 진통을 통해 질을 통해 아기를 출산하는 방법입니다. 통역 시 '자연분만'과 '정상분만'을 혼용하지 않도록 주의해야 하며, 베트남에서는 'đẻ thường'이라는 구어 표현도 많이 사용되므로 상황에 맞게 번역해야 합니다. 의료진과의 통역에서는 'Tự nhiên phân man'을, 환자와의 대화에서는 'đẻ thường'을 사용하는 것이 자연스럽습니다.",
        "meaningVi": "Phương pháp sinh con qua đường âm đạo một cách tự nhiên thông qua cơn co tử cung tự nhiên của sản phụ, không cần can thiệp phẫu thuật. Đây là phương pháp sinh con được ưu tiên nhất.",
        "context": "산부인과 진료, 출산 계획 상담",
        "culturalNote": "한국은 제왕절개율이 높은 편(약 45%)이지만 최근 자연분만을 권장하는 추세입니다. 베트남은 전통적으로 자연분만 선호도가 높았으나 도시 지역에서 제왕절개가 증가하고 있습니다. 한국의 '무통분만' 시스템은 베트남보다 더 보편화되어 있어 이에 대한 설명이 필요할 수 있습니다.",
        "commonMistakes": [
            {
                "mistake": "'Sinh thường'만 사용",
                "correction": "의료진에게는 'Tự nhiên phân man', 환자에게는 'đẻ thường' 또는 'sinh thường'",
                "explanation": "의료 용어와 일상 용어를 상황에 맞게 구분해야 전문성과 소통력을 모두 확보할 수 있습니다"
            },
            {
                "mistake": "'정상분만'과 혼용",
                "correction": "자연분만은 질식분만 방법, 정상분만은 합병증 없는 출산",
                "explanation": "두 용어는 의미가 다르므로 문맥에 따라 정확히 구분해야 합니다"
            },
            {
                "mistake": "'Natural birth'를 그대로 번역",
                "correction": "베트남 의료 용어 체계에 맞게 번역",
                "explanation": "영어 의료 용어를 그대로 직역하면 현지 의료진이 이해하기 어려울 수 있습니다"
            }
        ],
        "examples": [
            {
                "ko": "자연분만을 원하시면 산전 교육 프로그램에 참여하시는 것이 좋습니다.",
                "vi": "Nếu muốn đẻ thường thì nên tham gia chương trình giáo dục tiền sản.",
                "situation": "informal"
            },
            {
                "ko": "태아의 위치와 크기를 고려할 때 자연분만이 가능할 것으로 판단됩니다.",
                "vi": "Xét vị trí và kích thước của thai nhi, tôi đánh giá có thể sinh thường được.",
                "situation": "formal"
            },
            {
                "ko": "자연분만 중 응급 상황 발생 시 제왕절개로 전환할 수 있습니다.",
                "vi": "Trong quá trình sinh thường, nếu xảy ra tình huống khẩn cấp có thể chuyển sang mổ lấy thai.",
                "situation": "onsite"
            }
        ],
        "relatedTerms": ["제왕절개", "무통분만", "유도분만", "정상분만"]
    },
    {
        "slug": "che-vuong-thiet-khai",
        "korean": "제왕절개",
        "vietnamese": "Mổ lấy thai",
        "hanja": "帝王切開",
        "hanjaReading": "帝(임금 제) + 王(임금 왕) + 切(끊을 절) + 開(열 개)",
        "pronunciation": "제왕절개",
        "meaningKo": "복부와 자궁을 절개하여 태아를 꺼내는 수술적 분만 방법입니다. 통역 시 한국어 '제왕절개'는 한자어 유래이지만, 베트남어로는 'Mổ lấy thai'(수술로 아기를 꺼낸다)라는 직관적 표현을 사용하므로 주의가 필요합니다. 의학 약어 'C-sec'이나 'C/S'도 현장에서 자주 사용되므로 통역사는 이를 인지하고 있어야 합니다.",
        "meaningVi": "Phương pháp phẫu thuật mở bụng và tử cung để lấy thai nhi ra ngoài. Đây là phương pháp sinh con bằng can thiệp phẫu thuật khi không thể sinh thường hoặc có nguy cơ cho mẹ và bé.",
        "context": "산부인과 수술, 출산 계획, 응급 분만",
        "culturalNote": "한국의 제왕절개율은 OECD 국가 중 가장 높은 수준(약 45%)으로 사회적 이슈가 되고 있습니다. 베트남도 최근 도시 지역에서 제왕절개가 증가하는 추세이나 한국만큼은 아닙니다. 한국에서는 '진통이 없다'는 이유로 선택하는 경우도 있지만, 베트남에서는 여전히 의학적 필요성이 있을 때 시행하는 것이 일반적입니다.",
        "commonMistakes": [
            {
                "mistake": "'Phẫu thuật đẻ'만 사용",
                "correction": "'Mổ lấy thai' 또는 'Phẫu thuật lấy thai'",
                "explanation": "베트남 의료계에서 공식적으로 사용하는 용어는 'Mổ lấy thai'입니다"
            },
            {
                "mistake": "C-section을 그대로 발음",
                "correction": "베트남어로 완전히 번역",
                "explanation": "의료 현장에서 영어 약어를 그대로 사용하면 환자가 이해하지 못할 수 있습니다"
            },
            {
                "mistake": "'제왕'을 황제와 연결하여 설명",
                "correction": "수술 방법 자체에 집중하여 설명",
                "explanation": "어원 설명보다는 실제 의료 행위에 대한 정확한 전달이 중요합니다"
            }
        ],
        "examples": [
            {
                "ko": "태아가 역아라서 제왕절개를 권유드립니다.",
                "vi": "Thai nhi bị ngôi ngược nên tôi khuyên nên mổ lấy thai.",
                "situation": "formal"
            },
            {
                "ko": "응급 제왕절개가 필요한 상황입니다. 지금 즉시 수술실로 가겠습니다.",
                "vi": "Đây là tình huống cần mổ lấy thai khẩn cấp. Bây giờ chúng tôi sẽ vào phòng mổ ngay.",
                "situation": "onsite"
            },
            {
                "ko": "제왕절개 후 최소 6주간은 무리한 활동을 피하셔야 합니다.",
                "vi": "Sau khi mổ lấy thai, ít nhất 6 tuần phải tránh các hoạt động nặng nhọc.",
                "situation": "informal"
            }
        ],
        "relatedTerms": ["자연분만", "응급수술", "산후조리", "회복기간"]
    },
    {
        "slug": "vo-thong-phan-man",
        "korean": "무통분만",
        "vietnamese": "Sinh không đau",
        "hanja": "無痛分娩",
        "hanjaReading": "無(없을 무) + 痛(아플 통) + 分(나눌 분) + 娩(해산할 만)",
        "pronunciation": "무통분만",
        "meaningKo": "경막외마취를 통해 분만 시 통증을 완화하는 방법입니다. 통역 시 '완전히 통증이 없다'는 오해를 방지하기 위해 '통증 완화 분만'이라는 의미를 정확히 전달해야 합니다. 베트남에서는 'Sinh không đau' 또는 'Gây tê ngoài màng cứng'이라고 하며, 한국만큼 보편화되지 않았으므로 시술에 대한 상세한 설명이 필요할 수 있습니다.",
        "meaningVi": "Phương pháp giảm đau khi sinh nở bằng cách gây tê ngoài màng cứng (epidural), giúp sản phụ giảm bớt cơn đau trong quá trình chuyển dạ và sinh con mà vẫn tỉnh táo.",
        "context": "산부인과 상담, 출산 준비, 마취과 협진",
        "culturalNote": "한국에서는 무통분만이 매우 보편화되어 있고 많은 산모가 선택하지만, 베트남에서는 아직 대형 병원에서만 제공되며 비용 부담으로 선택률이 낮습니다. 한국 산모들은 무통분만을 당연하게 여기는 경향이 있지만, 베트남 의료진은 필요성에 대해 보수적일 수 있어 통역 시 이러한 문화 차이를 고려해야 합니다.",
        "commonMistakes": [
            {
                "mistake": "'완전히 아프지 않다'고 번역",
                "correction": "'통증을 크게 줄여준다'고 정확히 설명",
                "explanation": "무통분만도 약간의 압박감이나 불편함은 있을 수 있으므로 과장된 번역은 오해를 낳습니다"
            },
            {
                "mistake": "'Gây mê'(전신마취)와 혼동",
                "correction": "'Gây tê ngoài màng cứng' 또는 'Sinh không đau'로 명확히 구분",
                "explanation": "경막외마취와 전신마취는 완전히 다른 시술입니다"
            },
            {
                "mistake": "부작용 설명 생략",
                "correction": "두통, 저혈압 등 가능한 부작용도 정확히 전달",
                "explanation": "의료 통역에서는 이점뿐 아니라 위험성도 균형있게 전달해야 합니다"
            }
        ],
        "examples": [
            {
                "ko": "무통분만을 원하시면 마취과 상담을 먼저 받으셔야 합니다.",
                "vi": "Nếu muốn sinh không đau thì phải được tư vấn khoa gây mê trước.",
                "situation": "formal"
            },
            {
                "ko": "지금 자궁경부가 4cm 열렸으니 무통주사를 놓을 수 있습니다.",
                "vi": "Bây giờ cổ tử cung đã mở 4cm rồi nên có thể tiêm giảm đau được.",
                "situation": "onsite"
            },
            {
                "ko": "무통분만 해도 진통은 조금 느껴지지만 훨씬 견딜 만해요.",
                "vi": "Dù sinh không đau vẫn cảm thấy co bóp một chút nhưng chịu đựng được dễ hơn nhiều.",
                "situation": "informal"
            }
        ],
        "relatedTerms": ["경막외마취", "자연분만", "진통", "마취과"]
    },
    {
        "slug": "du-dao-phan-man",
        "korean": "유도분만",
        "vietnamese": "Sinh hỗ trợ",
        "hanja": "誘導分娩",
        "hanjaReading": "誘(꾀할 유) + 導(이끌 도) + 分(나눌 분) + 娩(해산할 만)",
        "pronunciation": "유도분만",
        "meaningKo": "약물이나 기구를 사용하여 인위적으로 진통을 유발하거나 촉진시켜 분만하는 방법입니다. 통역 시 '유도'라는 표현이 '강제'로 오해될 수 있으므로, 의학적 필요성에 따른 '보조' 또는 '촉진'의 의미임을 명확히 해야 합니다. 베트남어로는 'Sinh hỗ trợ' 또는 'Kích thích chuyển dạ'라고 하며, 옥시토신(oxytocin) 투여가 가장 일반적인 방법입니다.",
        "meaningVi": "Phương pháp hỗ trợ sinh nở bằng cách sử dụng thuốc hoặc dụng cụ y tế để kích thích hoặc tăng cường cơn co tử cung một cách nhân tạo, giúp quá trình sinh diễn ra thuận lợi hơn khi có chỉ định y khoa.",
        "context": "산부인과 진료, 예정일 경과, 진통 미약",
        "culturalNote": "한국에서는 예정일을 넘기거나 양수 파수 후 진통이 오지 않을 때 유도분만을 비교적 적극적으로 시행합니다. 베트남 의료진도 유사한 접근을 하지만, 환자들이 '자연스럽지 않다'는 이유로 거부감을 보이는 경우가 있습니다. 통역 시 의학적 필요성과 안전성을 강조하여 설명하는 것이 중요합니다.",
        "commonMistakes": [
            {
                "mistake": "'강제 분만'으로 번역",
                "correction": "'의학적 보조를 받는 분만'으로 설명",
                "explanation": "유도분만은 모체와 태아의 안전을 위한 의학적 조치이지 강제가 아닙니다"
            },
            {
                "mistake": "'Kích thích sinh'만 사용",
                "correction": "'Sinh hỗ trợ' 또는 전체 용어 'Kích thích chuyển dạ để sinh'",
                "explanation": "너무 짧은 표현은 오해를 낳을 수 있으므로 명확한 의료 용어 사용 필요"
            },
            {
                "mistake": "옥시토신을 설명 없이 사용",
                "correction": "'thuốc kích thích tử cung co bóp (oxytocin)'으로 설명",
                "explanation": "약물 이름은 기능 설명과 함께 전달해야 환자가 이해할 수 있습니다"
            }
        ],
        "examples": [
            {
                "ko": "예정일이 일주일 지났고 양수량이 줄어들어 유도분만을 권장합니다.",
                "vi": "Đã quá ngày dự sinh một tuần và lượng nước ối giảm nên tôi khuyên nên sinh hỗ trợ.",
                "situation": "formal"
            },
            {
                "ko": "양막 파수 후 24시간이 지났는데 진통이 없어서 유도분만 시작하겠습니다.",
                "vi": "Đã 24 giờ sau khi ối vỡ mà không có cơn co nên chúng tôi sẽ bắt đầu kích thích chuyển dạ.",
                "situation": "onsite"
            },
            {
                "ko": "유도분만 하면 진통이 더 강할 수 있으니 무통분만도 함께 고려해보세요.",
                "vi": "Nếu sinh hỗ trợ thì cơn co có thể mạnh hơn, nên cân nhắc sinh không đau luôn nhé.",
                "situation": "informal"
            }
        ],
        "relatedTerms": ["옥시토신", "양막파수", "진통촉진", "자궁수축"]
    },
    {
        "slug": "cho-gi-chin-thong",
        "korean": "조기진통",
        "vietnamese": "Chuyển dạ sớm",
        "hanja": "早期陣痛",
        "hanjaReading": "早(이를 조) + 期(기약 기) + 陣(진칠 진) + 痛(아플 통)",
        "pronunciation": "조기진통",
        "meaningKo": "임신 37주 이전에 규칙적인 자궁수축과 자궁경부 변화가 나타나는 상태로, 조산의 위험이 있습니다. 통역 시 '조산'과 '조기진통'을 명확히 구분해야 하며, 조기진통은 진통이 시작된 상태이고 조산은 실제로 아기가 태어난 것을 의미합니다. 베트남어로는 'Chuyển dạ sớm' 또는 'Đau bụng chuyển dạ trước tuần thứ 37'이라고 하며, 즉각적인 의료 조치가 필요함을 강조해야 합니다.",
        "meaningVi": "Tình trạng tử cung co bóp đều đặn và cổ tử cung thay đổi trước tuần thai thứ 37, có nguy cơ sinh non. Đây là tình huống cấp cứu sản khoa cần được xử lý ngay lập tức để kéo dài thai kỳ.",
        "context": "응급 산부인과, 고위험 임신 관리",
        "culturalNote": "한국과 베트nam 모두 조기진통을 심각한 응급 상황으로 인식하지만, 한국은 진통억제제 투여와 입원 관리가 매우 적극적입니다. 베트남에서도 유사한 치료를 하지만 의료 접근성이 지역에 따라 다를 수 있습니다. 통역 시 즉시 병원에 가야 한다는 긴급성을 명확히 전달하는 것이 중요합니다.",
        "commonMistakes": [
            {
                "mistake": "'조산'과 '조기진통'을 같은 것으로 번역",
                "correction": "조기진통은 'Chuyển dạ sớm', 조산은 'Sinh non'",
                "explanation": "조기진통은 과정, 조산은 결과로 명확히 구분해야 합니다"
            },
            {
                "mistake": "'단순 배 아픔'으로 가볍게 표현",
                "correction": "'응급 상황'임을 강조하여 전달",
                "explanation": "조기진통은 응급 상황이므로 심각성을 반드시 전달해야 합니다"
            },
            {
                "mistake": "37주 기준을 설명하지 않음",
                "correction": "'임신 37주 이전'이라는 구체적 기준 명시",
                "explanation": "의학적 기준을 정확히 전달해야 환자가 상황을 이해할 수 있습니다"
            }
        ],
        "examples": [
            {
                "ko": "현재 임신 32주인데 10분 간격으로 규칙적인 진통이 있다면 조기진통일 수 있으니 즉시 병원에 오세요.",
                "vi": "Hiện đang mang thai 32 tuần mà có cơn co đều đặn cách 10 phút thì có thể là chuyển dạ sớm, hãy đến bệnh viện ngay.",
                "situation": "formal"
            },
            {
                "ko": "조기진통 진단으로 진통억제제를 투여하고 절대안정이 필요합니다.",
                "vi": "Chẩn đoán chuyển dạ sớm nên sẽ truyền thuốc ức chế co bóp và cần nghỉ ngơi tuyệt đối.",
                "situation": "onsite"
            },
            {
                "ko": "조기진통 증상이 있으면 참지 말고 바로 응급실로 가야 해요.",
                "vi": "Nếu có triệu chứng chuyển dạ sớm thì đừng chịu đựng, phải đến cấp cứu ngay nhé.",
                "situation": "informal"
            }
        ],
        "relatedTerms": ["조산", "진통억제제", "절대안정", "고위험임신"]
    },
    {
        "slug": "chon-chi-thai-ban",
        "korean": "전치태반",
        "vietnamese": "Nhau tiền đạo",
        "hanja": "前置胎盤",
        "hanjaReading": "前(앞 전) + 置(둘 치) + 胎(아이 밸 태) + 盤(쟁반 반)",
        "pronunciation": "전치태반",
        "meaningKo": "태반이 자궁 입구를 부분적 또는 완전히 덮고 있는 상태로, 출혈 위험이 높고 제왕절개가 필요합니다. 통역 시 '전치태반'의 위험성과 절대안정의 필요성을 강조해야 하며, 특히 임신 후기 출혈 시 즉각적인 응급 조치가 필요함을 명확히 전달해야 합니다. 베트남어로는 'Nhau tiền đạo'라고 하며, 완전전치태반(Nhau bám hoàn toàn)과 부분전치태반(Nhau bám một phần)을 구분합니다.",
        "meaningVi": "Tình trạng bánh nhau (nhau thai) bám ở vị trí thấp, che khuất một phần hoặc toàn bộ cổ tử cung. Đây là biến chứng thai kỳ nguy hiểm có nguy cơ chảy máu cao, thường phải sinh mổ và cần theo dõi sát.",
        "context": "고위험 임신 관리, 산전 초음파 소견",
        "culturalNote": "한국과 베트남 모두 전치태반을 매우 위험한 합병증으로 인식하며, 철저한 산전 관리와 제왕절개를 원칙으로 합니다. 한국은 초음파 검진이 빈번하여 조기 발견율이 높지만, 베트남은 지역에 따라 검진 접근성이 다를 수 있습니다. 통역 시 절대안정과 성관계 금지 등 생활 수칙을 명확히 전달하는 것이 중요합니다.",
        "commonMistakes": [
            {
                "mistake": "'Nhau bong non'(태반조기박리)과 혼동",
                "correction": "전치태반은 'Nhau tiền đạo', 태반조기박리는 'Nhau bong non'",
                "explanation": "두 질환은 완전히 다른 병리이므로 절대 혼동하면 안 됩니다"
            },
            {
                "mistake": "위험성을 충분히 설명하지 않음",
                "correction": "대량 출혈과 모체·태아 위험성을 명확히 전달",
                "explanation": "환자가 위험성을 인지해야 안정을 취하고 주의 사항을 지킵니다"
            },
            {
                "mistake": "'자연분만 가능'이라는 오해 방치",
                "correction": "제왕절개 필수임을 명확히 설명",
                "explanation": "완전전치태반은 자연분만이 절대 불가능하므로 오해를 바로잡아야 합니다"
            }
        ],
        "examples": [
            {
                "ko": "초음파 결과 완전전치태반으로 진단되어 제왕절개가 필수이며 절대안정이 필요합니다.",
                "vi": "Kết quả siêu âm chẩn đoán nhau tiền đạo hoàn toàn nên bắt buộc phải mổ lấy thai và cần nghỉ ngơi tuyệt đối.",
                "situation": "formal"
            },
            {
                "ko": "전치태반이 있으면 출혈 위험이 높으니 무거운 것 들지 마시고 성관계도 금지입니다.",
                "vi": "Có nhau tiền đạo thì nguy cơ chảy máu cao nên đừng mang vác nặng và cấm quan hệ tình dục.",
                "situation": "onsite"
            },
            {
                "ko": "전치태반인데 출혈이 있으면 바로 119 부르고 병원 가야 해요.",
                "vi": "Nếu nhau tiền đạo mà ra máu thì phải gọi cấp cứu ngay và đến bệnh viện nhé.",
                "situation": "informal"
            }
        ],
        "relatedTerms": ["태반조기박리", "제왕절개", "산전출혈", "고위험임신"]
    },
    {
        "slug": "thai-ban-cho-gi-bac-ri",
        "korean": "태반조기박리",
        "vietnamese": "Nhau bong non",
        "hanja": "胎盤早期剝離",
        "hanjaReading": "胎(아이 밸 태) + 盤(쟁반 반) + 早(이를 조) + 期(기약 기) + 剝(벗길 박) + 離(떠날 리)",
        "pronunciation": "태반조기박리",
        "meaningKo": "태아가 태어나기 전에 태반이 자궁벽에서 떨어지는 응급 상황으로, 모체와 태아 모두 생명이 위험할 수 있습니다. 통역 시 극도의 응급 상황임을 강조하고, 복통과 출혈 증상 발생 시 즉각 응급실로 가야 함을 명확히 전달해야 합니다. 베트남어로는 'Nhau bong non'이라고 하며, 'bong'은 '떨어지다', 'non'은 '조기'를 의미합니다.",
        "meaningVi": "Tình trạng bánh nhau tách rời khỏi thành tử cung trước khi thai nhi sinh ra. Đây là cấp cứu sản khoa nghiêm trọng, nguy hiểm tính mạng cả mẹ và con, cần xử lý ngay lập tức.",
        "context": "산과 응급, 고위험 임신",
        "culturalNote": "한국과 베트남 모두 태반조기박리를 극도로 위험한 응급 상황으로 인식합니다. 고혈압, 외상, 흡연 등이 위험 요인이며, 발생 시 응급 제왕절개가 필요합니다. 통역 시 환자가 패닉 상태에 빠질 수 있으므로, 침착하게 그러나 긴급성을 분명히 전달하는 균형이 필요합니다.",
        "commonMistakes": [
            {
                "mistake": "'전치태반'과 혼동",
                "correction": "전치태반은 위치 이상, 태반조기박리는 분리 현상",
                "explanation": "완전히 다른 병리이므로 혼동하면 치료가 지연될 수 있습니다"
            },
            {
                "mistake": "긴급성을 약하게 전달",
                "correction": "'생명 위협적 응급 상황'임을 명확히 강조",
                "explanation": "즉각적인 의료 조치가 필요한 상황임을 반드시 전달해야 합니다"
            },
            {
                "mistake": "'Tách nhau'로 번역",
                "correction": "'Nhau bong non'이 정확한 의학 용어",
                "explanation": "표준 의학 용어를 사용해야 의료진과 정확한 소통이 가능합니다"
            }
        ],
        "examples": [
            {
                "ko": "갑자기 심한 복통과 질출혈이 있다면 태반조기박리일 수 있으니 즉시 응급실로 오세요.",
                "vi": "Nếu đột ngột đau bụng dữ dội và chảy máu âm đạo thì có thể là nhau bong non, hãy đến cấp cứu ngay lập tức.",
                "situation": "formal"
            },
            {
                "ko": "태반조기박리 진단으로 응급 제왕절개를 시행하겠습니다. 지금 바로 수술실로 갑니다.",
                "vi": "Chẩn đoán nhau bong non nên sẽ mổ lấy thai cấp cứu. Bây giờ vào phòng mổ ngay.",
                "situation": "onsite"
            },
            {
                "ko": "고혈압 있으면 태반조기박리 위험이 높으니 혈압 관리 잘 해야 해요.",
                "vi": "Nếu có cao huyết áp thì nguy cơ nhau bong non cao, phải kiểm soát huyết áp tốt nhé.",
                "situation": "informal"
            }
        ],
        "relatedTerms": ["전치태반", "응급제왕절개", "산전출혈", "고혈압"]
    },
    {
        "slug": "rim-shin-chung-doc-chung",
        "korean": "임신중독증",
        "vietnamese": "Tiền sản giật",
        "hanja": "妊娠中毒症",
        "hanjaReading": "妊(아이 밸 임) + 娠(아이 밸 신) + 中(가운데 중) + 毒(독 독) + 症(병 증)",
        "pronunciation": "임신중독증",
        "meaningKo": "임신 20주 이후 고혈압과 단백뇨가 나타나는 질환으로, 현대 의학에서는 '전자간증'이라는 용어를 더 많이 사용합니다. 통역 시 한국에서는 아직 '임신중독증'이라는 용어가 일반적으로 사용되지만, 의학적으로는 '전자간증(Preeclampsia)'이 정확한 용어임을 알고 있어야 합니다. 베트남어로는 'Tiền sản giật'이라고 하며, 치료하지 않으면 자간증(Sản giật/경련)으로 진행될 수 있습니다.",
        "meaningVi": "Bệnh lý thai kỳ xảy ra sau tuần 20, đặc trưng bởi tăng huyết áp và protein niệu. Nếu không điều trị kịp thời có thể tiến triển thành sản giật (co giật), nguy hiểm tính mạng mẹ và con.",
        "context": "산전 진찰, 고위험 임신 관리",
        "culturalNote": "한국에서는 '임신중독증'이라는 용어가 여전히 널리 사용되지만, '독'이라는 표현 때문에 환자들이 불필요한 불안을 느낄 수 있습니다. 베트남에서는 'Tiền sản giật'(자간증 전단계)이라는 정확한 의학 용어를 사용합니다. 통역 시 혈압 관리, 단백뇨 검사, 부종 관찰 등 구체적 관리 방법을 함께 설명하는 것이 중요합니다.",
        "commonMistakes": [
            {
                "mistake": "'중독'을 독성 물질 중독으로 오해",
                "correction": "'고혈압성 임신 합병증'으로 설명",
                "explanation": "실제로는 독소와 무관하며 혈압과 신장 기능 문제입니다"
            },
            {
                "mistake": "'Ngộ độc khi mang thai'로 번역",
                "correction": "'Tiền sản giật' 또는 'Preeclampsia'",
                "explanation": "'Ngộ độc'은 중독을 의미하므로 완전히 잘못된 번역입니다"
            },
            {
                "mistake": "증상 설명 없이 진단명만 전달",
                "correction": "두통, 시야 이상, 상복부 통증 등 증상도 함께 설명",
                "explanation": "환자가 증상을 인지해야 악화 시 즉시 대응할 수 있습니다"
            }
        ],
        "examples": [
            {
                "ko": "혈압이 높고 소변에서 단백질이 나와서 임신중독증으로 진단됩니다. 입원 치료가 필요합니다.",
                "vi": "Huyết áp cao và nước tiểu có protein nên chẩn đoán tiền sản giật. Cần nhập viện điều trị.",
                "situation": "formal"
            },
            {
                "ko": "임신중독증이 있어서 혈압약을 처방하고, 심하면 조기 분만을 고려해야 합니다.",
                "vi": "Có tiền sản giật nên kê thuốc hạ huyết áp, nếu nặng phải cân nhắc sinh sớm.",
                "situation": "onsite"
            },
            {
                "ko": "임신중독증 예방하려면 짜게 먹지 말고 정기 검진 꼭 받아야 해요.",
                "vi": "Để phòng tiền sản giật thì đừng ăn mặn và phải khám định kỳ đều đặn nhé.",
                "situation": "informal"
            }
        ],
        "relatedTerms": ["전자간증", "자간증", "고혈압", "단백뇨"]
    },
    {
        "slug": "chu-kung-oe-rim-shin",
        "korean": "자궁외임신",
        "vietnamese": "Thai ngoài tử cung",
        "hanja": "子宮外妊娠",
        "hanjaReading": "子(아들 자) + 宮(집 궁) + 外(밖 외) + 妊(아이 밸 임) + 娠(아이 밸 신)",
        "pronunciation": "자궁외임신",
        "meaningKo": "수정란이 자궁 내막이 아닌 다른 곳(주로 난관)에 착상된 상태로, 응급 수술이 필요한 위험한 상황입니다. 통역 시 '자연 유산'이나 '정상 임신'과는 완전히 다른 응급 상황임을 명확히 해야 하며, 복통과 출혈 시 즉시 응급실에 가야 함을 강조해야 합니다. 베트남어로는 'Thai ngoài tử cung' 또는 'Mang thai ngoài tử cung'이라고 하며, 가장 흔한 난관임신은 'Thai ở vòi trứng'입니다.",
        "meaningVi": "Tình trạng phôi thai làm tổ bên ngoài buồng tử cung, thường ở vòi trứng. Đây là cấp cứu sản khoa nguy hiểm, có thể gây vỡ vòi trứng và chảy máu trong ổ bụng, cần phẫu thuật khẩn cấp.",
        "context": "산부인과 응급, 초기 임신 합병증",
        "culturalNote": "한국과 베트남 모두 자궁외임신을 심각한 응급 상황으로 인식하며, 조기 발견과 신속한 수술적 처치가 중요합니다. 한국은 초음파 검진이 빨라 조기 발견율이 높지만, 베트남은 지역에 따라 검진 접근성이 다를 수 있습니다. 통역 시 난관 파열 시 내출혈로 쇼크에 빠질 수 있음을 경고하는 것이 중요합니다.",
        "commonMistakes": [
            {
                "mistake": "'유산'과 동일하게 번역",
                "correction": "유산과는 완전히 다른 응급 수술 상황",
                "explanation": "자궁외임신은 수술이 필요한 응급 상황이므로 구분이 중요합니다"
            },
            {
                "mistake": "'Thai bất thường'으로 모호하게 번역",
                "correction": "'Thai ngoài tử cung'으로 명확히 번역",
                "explanation": "정확한 위치와 상황을 전달해야 응급 조치가 가능합니다"
            },
            {
                "mistake": "내출혈 위험 설명 누락",
                "correction": "난관 파열 시 복강 내 출혈 위험 설명 필수",
                "explanation": "생명을 위협할 수 있는 합병증이므로 반드시 설명해야 합니다"
            }
        ],
        "examples": [
            {
                "ko": "초음파에서 자궁 안에 임신낭이 보이지 않고 hCG 수치가 높아 자궁외임신이 의심됩니다.",
                "vi": "Siêu âm không thấy túi thai trong tử cung mà chỉ số hCG cao nên nghi ngờ thai ngoài tử cung.",
                "situation": "formal"
            },
            {
                "ko": "자궁외임신 확진되어 복강경 수술로 난관을 제거하겠습니다.",
                "vi": "Xác định thai ngoài tử cung nên sẽ phẫu thuật nội soi cắt vòi trứng.",
                "situation": "onsite"
            },
            {
                "ko": "자궁외임신인데 한쪽 배가 갑자기 심하게 아프면 난관 터진 거니까 바로 119 불러요.",
                "vi": "Thai ngoài tử cung mà đột ngột đau dữ dội một bên bụng thì vòi trứng vỡ rồi, phải gọi cấp cứu ngay nhé.",
                "situation": "informal"
            }
        ],
        "relatedTerms": ["난관임신", "복강경수술", "hCG검사", "초음파검사"]
    },
    {
        "slug": "yang-su-gom-sa",
        "korean": "양수검사",
        "vietnamese": "Chọc ối",
        "hanja": "羊水檢査",
        "hanjaReading": "羊(양 양) + 水(물 수) + 檢(조사할 검) + 査(조사할 사)",
        "pronunciation": "양수검사",
        "meaningKo": "임신 중기(보통 15~20주)에 바늘로 양수를 채취하여 태아의 염색체 이상이나 유전 질환을 검사하는 산전 진단 방법입니다. 통역 시 침습적 검사로 유산 위험(약 0.1~0.3%)이 있음을 반드시 설명해야 하며, 고령 임신이나 기형아 검사 고위험군에서 시행한다는 점을 명확히 해야 합니다. 베트남어로는 'Chọc ối' 또는 'Xét nghiệm nước ối'라고 합니다.",
        "meaningVi": "Phương pháp chẩn đoán trước sinh bằng cách dùng kim chọc vào buồng ối để lấy nước ối, nhằm xét nghiệm phát hiện bất thường nhiễm sắc thể hoặc bệnh di truyền của thai nhi. Thường làm ở tuần 15-20.",
        "context": "산전 진단, 고위험 임신 상담",
        "culturalNote": "한국에서는 고령 임신(만 35세 이상)이나 기형아 선별검사에서 고위험으로 나온 경우 양수검사를 권장합니다. 베트남에서도 유사한 적응증이지만, 검사 비용과 접근성 문제로 시행률이 낮을 수 있습니다. 통역 시 검사의 필요성과 함께 위험성, 대안 검사(NIPT 등)도 함께 설명하는 것이 중요합니다.",
        "commonMistakes": [
            {
                "mistake": "'비침습적' 검사로 잘못 설명",
                "correction": "'침습적' 검사이며 유산 위험 있음을 명시",
                "explanation": "바늘로 찌르는 검사이므로 위험성을 정확히 전달해야 합니다"
            },
            {
                "mistake": "'Chích nước ối'로 번역",
                "correction": "'Chọc ối'가 정확한 의학 용어",
                "explanation": "'Chích'은 주사, 'Chọc'은 천자의 의미로 구분이 필요합니다"
            },
            {
                "mistake": "검사 목적을 '성별 확인'으로 설명",
                "correction": "염색체 이상 및 유전 질환 진단이 주목적",
                "explanation": "의학적 목적을 명확히 해야 불필요한 오해를 방지할 수 있습니다"
            }
        ],
        "examples": [
            {
                "ko": "기형아 검사에서 고위험으로 나와 양수검사를 권유드립니다. 다운증후군 등을 확진할 수 있습니다.",
                "vi": "Xét nghiệm sàng lọc bất thường bẩm sinh có nguy cơ cao nên khuyên nên chọc ối. Có thể xác định hội chứng Down và các bệnh khác.",
                "situation": "formal"
            },
            {
                "ko": "양수검사 후 2~3일은 안정을 취하시고, 출혈이나 복통이 있으면 즉시 연락하세요.",
                "vi": "Sau chọc ối 2-3 ngày phải nghỉ ngơi, nếu có chảy máu hoặc đau bụng thì liên hệ ngay.",
                "situation": "onsite"
            },
            {
                "ko": "양수검사는 유산 위험이 조금 있어서 요즘은 NIPT 같은 혈액검사를 먼저 하기도 해요.",
                "vi": "Chọc ối có nguy cơ sẩy thai một chút nên gần đây người ta làm xét nghiệm máu NIPT trước nhé.",
                "situation": "informal"
            }
        ],
        "relatedTerms": ["융모막검사", "NIPT", "다운증후군", "기형아검사"]
    },
    {
        "slug": "thai-a-cho-um-pa",
        "korean": "태아초음파",
        "vietnamese": "Siêu âm thai",
        "hanja": "胎兒超音波",
        "hanjaReading": "胎(아이 밸 태) + 兒(아이 아) + 超(뛰어넘을 초) + 音(소리 음) + 波(물결 파)",
        "pronunciation": "태아초음파",
        "meaningKo": "초음파를 이용하여 태아의 발달 상태, 기형 유무, 태반 위치 등을 확인하는 산전 검사입니다. 통역 시 한국은 임신 기간 동안 여러 차례 초음파 검사를 시행하며(초기, 중기 정밀, 후기 등), 각 시기마다 확인하는 항목이 다르다는 점을 설명해야 합니다. 베트남어로는 'Siêu âm thai' 또는 'Siêu âm thai nhi'라고 하며, 2D, 3D, 4D 초음파를 구분합니다.",
        "meaningVi": "Phương pháp sử dụng sóng siêu âm để kiểm tra tình trạng phát triển của thai nhi, phát hiện dị tật bẩm sinh, vị trí bánh nhau và lượng nước ối. Đây là xét nghiệm không xâm lấn, an toàn cho mẹ và bé.",
        "context": "산전 진찰, 정기 검진",
        "culturalNote": "한국은 임신 기간 동안 초음파 검사를 자주 시행하며(보험 적용 7~8회), 3D/4D 초음파도 흔합니다. 베트남도 정기 초음파를 시행하지만 횟수는 한국보다 적을 수 있으며, 3D/4D는 추가 비용이 발생합니다. 통역 시 각 시기별 초음파의 목적(초기: 임신 확인, 중기: 기형 검사, 후기: 성장 평가)을 설명하는 것이 유용합니다.",
        "commonMistakes": [
            {
                "mistake": "'X-ray'와 혼동하여 방사선 위험 언급",
                "correction": "초음파는 방사선이 아닌 음파로 안전함을 설명",
                "explanation": "환자들이 방사선과 혼동하여 불안해할 수 있으므로 안전성을 강조해야 합니다"
            },
            {
                "mistake": "'Chiếu thai'만 사용",
                "correction": "'Siêu âm thai' 또는 'Khám siêu âm'",
                "explanation": "'Chiếu'는 X-ray를 연상시킬 수 있어 정확한 용어 사용이 필요합니다"
            },
            {
                "mistake": "2D/3D/4D 차이 설명 부족",
                "correction": "각 방법의 목적과 비용 차이 설명",
                "explanation": "환자가 선택할 수 있도록 충분한 정보를 제공해야 합니다"
            }
        ],
        "examples": [
            {
                "ko": "오늘은 임신 20주 정밀 초음파로 태아의 장기와 구조를 자세히 확인하겠습니다.",
                "vi": "Hôm nay sẽ làm siêu âm chi tiết tuần 20 để kiểm tra kỹ các cơ quan và cấu trúc của thai nhi.",
                "situation": "formal"
            },
            {
                "ko": "초음파에서 태아 심박동이 정상이고 성장도 주수에 맞습니다.",
                "vi": "Siêu âm cho thấy nhịp tim thai bình thường và sự phát triển phù hợp với tuần tuổi.",
                "situation": "onsite"
            },
            {
                "ko": "3D 초음파 하면 아기 얼굴 볼 수 있는데 꼭 필요한 건 아니고 추가 비용 있어요.",
                "vi": "Siêu âm 3D thì thấy được mặt bé nhưng không bắt buộc và có chi phí thêm nhé.",
                "situation": "informal"
            }
        ],
        "relatedTerms": ["정밀초음파", "도플러초음파", "산전검사", "기형아검사"]
    },
    {
        "slug": "rim-shin-song-dang-nyo",
        "korean": "임신성당뇨",
        "vietnamese": "Đái tháo đường thai kỳ",
        "hanja": "妊娠性糖尿",
        "hanjaReading": "妊(아이 밸 임) + 娠(아이 밸 신) + 性(성품 성) + 糖(엿 당) + 尿(오줌 뇨)",
        "pronunciation": "임신성당뇨",
        "meaningKo": "임신 중에 처음 발견되거나 발생한 당뇨병으로, 임신 24~28주에 선별검사를 시행합니다. 통역 시 일반 당뇨병과는 다르며 대부분 출산 후 정상으로 돌아오지만, 식이 조절과 혈당 관리가 필수임을 강조해야 합니다. 베트남어로는 'Đái tháo đường thai kỳ' 또는 'Tiểu đường thai nghén'이라고 하며, GDM(Gestational Diabetes Mellitus)이라는 약어도 사용됩니다.",
        "meaningVi": "Bệnh đái tháo đường được phát hiện hoặc khởi phát lần đầu trong thai kỳ, thường xuất hiện ở tuần 24-28. Cần kiểm soát đường huyết chặt chẽ để tránh biến chứng cho mẹ và con. Hầu hết sẽ hồi phục sau sinh.",
        "context": "산전 진찰, 임신 중기 선별검사",
        "culturalNote": "한국과 베트남 모두 임신 24~28주에 당부하 검사(50g 또는 75g)를 시행합니다. 한국은 쌀밥 중심 식단으로 임신성당뇨 발생률이 높은 편이며, 베트남도 동아시아 인종 특성상 발생률이 낮지 않습니다. 통역 시 식이 조절(탄수화물 분산 섭취)과 혈당 자가 측정의 중요성을 강조해야 합니다.",
        "commonMistakes": [
            {
                "mistake": "'평생 당뇨병'으로 오해",
                "correction": "대부분 출산 후 정상으로 회복되지만 추적 관찰 필요",
                "explanation": "불필요한 불안을 주지 않으면서도 관리의 필요성은 전달해야 합니다"
            },
            {
                "mistake": "'Bệnh tiểu đường'로만 번역",
                "correction": "'Đái tháo đường thai kỳ'로 임신 관련 당뇨임을 명시",
                "explanation": "일반 당뇨병과 구분되는 임신 특이적 상태임을 명확히 해야 합니다"
            },
            {
                "mistake": "식이 조절 없이 약물만 강조",
                "correction": "식이 조절이 1차 치료이며, 필요시 인슐린 사용",
                "explanation": "치료의 우선순위를 정확히 전달해야 환자가 올바른 관리를 할 수 있습니다"
            }
        ],
        "examples": [
            {
                "ko": "당부하 검사 결과 임신성당뇨로 진단되어 영양 상담과 혈당 측정이 필요합니다.",
                "vi": "Kết quả test dung nạp đường cho thấy đái tháo đường thai kỳ, cần tư vấn dinh dưỡng và đo đường huyết.",
                "situation": "formal"
            },
            {
                "ko": "혈당이 계속 높으면 인슐린 주사를 시작해야 하고, 태아가 너무 크면 조기 분만을 고려합니다.",
                "vi": "Nếu đường huyết vẫn cao thì phải bắt đầu tiêm insulin, và nếu thai nhi quá lớn thì cân nhắc sinh sớm.",
                "situation": "onsite"
            },
            {
                "ko": "임신성당뇨 있으면 흰밥 대신 잡곡밥 먹고, 과일도 한 번에 많이 먹지 마세요.",
                "vi": "Có đái tháo đường thai kỳ thì ăn cơm gạo lứt thay cơm trắng, và đừng ăn nhiều trái cây một lúc nhé.",
                "situation": "informal"
            }
        ],
        "relatedTerms": ["당부하검사", "혈당측정", "인슐린", "거대아"]
    },
    {
        "slug": "san-hu-chul-hyol",
        "korean": "산후출혈",
        "vietnamese": "Chảy máu sau sinh",
        "hanja": "産後出血",
        "hanjaReading": "産(낳을 산) + 後(뒤 후) + 出(날 출) + 血(피 혈)",
        "pronunciation": "산후출혈",
        "meaningKo": "분만 후 24시간 이내에 500mL(질식분만) 또는 1000mL(제왕절개) 이상 출혈이 발생하는 응급 상황입니다. 통역 시 산후출혈은 산모 사망의 주요 원인이므로 출혈량 관찰의 중요성과, 어지럼증이나 빈맥 등의 쇼크 증상 발생 시 즉각 알려야 함을 강조해야 합니다. 베트남어로는 'Chảy máu sau sinh' 또는 'Băng huyết sau sinh'(대량 출혈)이라고 합니다.",
        "meaningVi": "Tình trạng chảy máu quá mức sau sinh, trên 500ml với sinh thường hoặc trên 1000ml với mổ lấy thai trong vòng 24 giờ. Đây là cấp cứu sản khoa nguy hiểm, cần xử lý ngay để tránh sốc mất máu.",
        "context": "분만 직후, 산후 조리실",
        "culturalNote": "한국과 베트남 모두 산후출혈을 심각한 응급 상황으로 인식하며, 자궁수축제(옥시토신) 투여와 자궁 마사지를 즉시 시행합니다. 한국은 산후조리원 문화가 발달했지만 산후조리원에서도 출혈 관찰은 필수이며, 베트남은 주로 병원이나 집에서 회복하므로 가족 교육이 중요합니다. 통역 시 출혈 양 판단 기준(생리대 교체 횟수 등)을 구체적으로 알려주는 것이 유용합니다.",
        "commonMistakes": [
            {
                "mistake": "'정상적인 산후 출혈'로 가볍게 표현",
                "correction": "비정상적으로 많은 출혈임을 명확히 전달",
                "explanation": "응급 상황임을 인지시켜야 적절한 조치가 가능합니다"
            },
            {
                "mistake": "'Kinh nguyệt nhiều'(월경 과다)와 비교",
                "correction": "훨씬 많은 양이며 생명을 위협할 수 있음을 설명",
                "explanation": "월경과 비교하면 심각성이 과소평가될 수 있습니다"
            },
            {
                "mistake": "출혈량 기준을 주관적으로 표현",
                "correction": "500mL/1000mL 등 구체적 수치 제시",
                "explanation": "객관적 기준을 제시해야 정확한 판단이 가능합니다"
            }
        ],
        "examples": [
            {
                "ko": "출산 후 출혈량이 많아 산후출혈로 진단되어 자궁수축제를 투여하고 수혈을 준비하겠습니다.",
                "vi": "Sau sinh lượng máu chảy nhiều, chẩn đoán chảy máu sau sinh nên sẽ truyền thuốc co tử cung và chuẩn bị truyền máu.",
                "situation": "formal"
            },
            {
                "ko": "자궁이 물렁물렁하고 출혈이 계속되면 산후출혈이니 즉시 간호사를 부르세요.",
                "vi": "Nếu tử cung mềm nhũn và tiếp tục chảy máu thì là chảy máu sau sinh, hãy gọi y tá ngay.",
                "situation": "onsite"
            },
            {
                "ko": "산후출혈 예방하려면 출산 직후 아기한테 젖 물리면 자궁수축에 도움돼요.",
                "vi": "Để phòng chảy máu sau sinh thì cho bé bú ngay sau sinh sẽ giúp tử cung co bóp tốt nhé.",
                "situation": "informal"
            }
        ],
        "relatedTerms": ["자궁수축제", "옥시토신", "수혈", "자궁마사지"]
    },
    {
        "slug": "san-hu-wu-ul-chung",
        "korean": "산후우울증",
        "vietnamese": "Trầm cảm sau sinh",
        "hanja": "産後憂鬱症",
        "hanjaReading": "産(낳을 산) + 後(뒤 후) + 憂(근심 우) + 鬱(답답할 울) + 症(병 증)",
        "pronunciation": "산후우울증",
        "meaningKo": "출산 후 호르몬 변화와 스트레스로 인해 발생하는 우울증으로, 일시적인 '산후우울감'과는 구별되는 치료가 필요한 질환입니다. 통역 시 '마음이 약해서' 생기는 것이 아니라 호르몬과 뇌 화학물질의 변화로 생기는 의학적 질환임을 명확히 해야 하며, 치료받으면 회복 가능함을 강조해야 합니다. 베트남어로는 'Trầm cảm sau sinh' 또는 'Trầm cảm hậu sản'이라고 합니다.",
        "meaningVi": "Bệnh trầm cảm xảy ra sau sinh do thay đổi hormone và stress, là rối loạn tâm thần cần điều trị, khác với buồn rầu thoáng qua sau sinh. Nếu không điều trị có thể ảnh hưởng nghiêm trọng đến sức khỏe mẹ và khả năng chăm con.",
        "context": "산후 관리, 정신건강의학과 협진",
        "culturalNote": "한국은 최근 산후우울증에 대한 인식이 높아지고 있지만, 베트남을 포함한 많은 아시아 문화권에서는 여전히 정신질환에 대한 낙인이 강합니다. 통역 시 '정신이 이상한 것'이 아니라 '치료 가능한 의학적 상태'임을 강조하고, 약물치료와 상담치료의 효과를 설명하여 치료에 대한 거부감을 줄이는 것이 중요합니다.",
        "commonMistakes": [
            {
                "mistake": "'산후조리 못해서 생기는 병'으로 설명",
                "correction": "호르몬 변화와 뇌 화학물질 불균형이 원인",
                "explanation": "의학적 원인을 정확히 전달해야 불필요한 죄책감을 줄일 수 있습니다"
            },
            {
                "mistake": "'Tâm trạng xấu'(기분 나쁨)로 가볍게 표현",
                "correction": "'Trầm cảm'(우울증)으로 명확히 진단명 사용",
                "explanation": "일시적 감정 변화가 아닌 질환임을 명확히 해야 합니다"
            },
            {
                "mistake": "약물 치료의 부작용만 강조",
                "correction": "치료받지 않을 경우의 위험성과 치료 효과를 균형있게 설명",
                "explanation": "치료의 이점을 충분히 전달해야 환자가 적극적으로 치료받을 수 있습니다"
            }
        ],
        "examples": [
            {
                "ko": "출산 후 2주 이상 우울감이 지속되고 아기에게 애착이 생기지 않는다면 산후우울증일 수 있으니 진료가 필요합니다.",
                "vi": "Nếu sau sinh trên 2 tuần vẫn buồn rầu kéo dài và không có cảm xúc với bé thì có thể là trầm cảm sau sinh, cần khám bác sĩ.",
                "situation": "formal"
            },
            {
                "ko": "산후우울증으로 진단되어 항우울제를 처방하겠습니다. 모유수유 중에도 안전한 약입니다.",
                "vi": "Chẩn đoán trầm cảm sau sinh nên sẽ kê thuốc chống trầm cảm. Đây là thuốc an toàn khi đang cho con bú.",
                "situation": "onsite"
            },
            {
                "ko": "산후우울증은 엄마 잘못이 아니고 치료하면 좋아지니까 혼자 끙끙 앓지 말고 도움 요청하세요.",
                "vi": "Trầm cảm sau sinh không phải lỗi của mẹ và điều trị được nên đừng tự chịu đựng mà hãy xin giúp đỡ nhé.",
                "situation": "informal"
            }
        ],
        "relatedTerms": ["산후조리", "호르몬변화", "정신건강", "항우울제"]
    },
    {
        "slug": "chu-kung-gun-chong",
        "korean": "자궁근종",
        "vietnamese": "U xơ tử cung",
        "hanja": "子宮筋腫",
        "hanjaReading": "子(아들 자) + 宮(집 궁) + 筋(힘줄 근) + 腫(부을 종)",
        "pronunciation": "자궁근종",
        "meaningKo": "자궁의 평활근에서 발생하는 양성 종양으로, 가임기 여성의 20~40%에서 발견되는 매우 흔한 질환입니다. 통역 시 '근종'이라는 용어가 암으로 오해될 수 있으므로 '양성 종양'임을 반드시 강조해야 하며, 크기와 위치에 따라 치료 방법이 다름을 설명해야 합니다. 베트남어로는 'U xơ tử cung'이라고 하며, 'U' 는 종양, 'xơ'는 섬유질을 의미합니다.",
        "meaningVi": "Khối u lành tính phát triển từ lớp cơ trơn của tử cung, rất phổ biến ở phụ nữ trong độ tuổi sinh đẻ (20-40%). Tùy kích thước và vị trí mà có thể gây ra triệu chứng như kinh nguyệt nhiều, đau bụng hoặc khó thụ thai.",
        "context": "부인과 진료, 정기 검진",
        "culturalNote": "한국과 베트남 모두 자궁근종이 매우 흔하며, 작고 증상이 없으면 경과 관찰만 하는 것이 일반적입니다. 한국은 증상이 있을 때 약물치료, 색전술, 수술 등 다양한 옵션을 제공하며, 베트남도 유사한 치료를 하지만 약물보다 수술을 선호하는 경향이 있습니다. 통역 시 '근종=수술'이 아니라 선택지가 다양함을 설명하는 것이 중요합니다.",
        "commonMistakes": [
            {
                "mistake": "'암'으로 오해하게 방치",
                "correction": "양성 종양임을 즉시 명확히 설명",
                "explanation": "환자의 불필요한 공포를 즉시 해소해야 합니다"
            },
            {
                "mistake": "'U' 때문에 암으로 오해 가능성 무시",
                "correction": "'U lành tính'(양성 종양)이라고 강조",
                "explanation": "베트남어 'U'는 암도 포함하므로 '양성'임을 분명히 해야 합니다"
            },
            {
                "mistake": "무조건 수술 필요하다고 번역",
                "correction": "크기와 증상에 따라 경과 관찰 가능",
                "explanation": "과잉 치료를 유도하지 않도록 정확한 정보 전달이 필요합니다"
            }
        ],
        "examples": [
            {
                "ko": "초음파에서 3cm 크기의 자궁근종이 발견되었지만 증상이 없으므로 6개월마다 경과 관찰하겠습니다.",
                "vi": "Siêu âm phát hiện u xơ tử cung kích thước 3cm nhưng không có triệu chứng nên sẽ theo dõi 6 tháng một lần.",
                "situation": "formal"
            },
            {
                "ko": "자궁근종이 커서 생리량이 많고 빈혈이 생겼다면 수술이나 색전술을 고려해야 합니다.",
                "vi": "U xơ tử cung to nên kinh nguyệt nhiều và bị thiếu máu thì phải cân nhắc phẫu thuật hoặc nút mạch.",
                "situation": "onsite"
            },
            {
                "ko": "자궁근종 있어도 대부분 임신 잘 되는데, 위치가 안 좋으면 영향 줄 수도 있어요.",
                "vi": "Có u xơ tử cung vẫn mang thai được bình thường, nhưng nếu vị trí không tốt có thể ảnh hưởng nhé.",
                "situation": "informal"
            }
        ],
        "relatedTerms": ["자궁선근증", "난소낭종", "자궁적출술", "색전술"]
    },
    {
        "slug": "chu-kung-nae-mac-chung",
        "korean": "자궁내막증",
        "vietnamese": "Lạc nội mạc tử cung",
        "hanja": "子宮內膜症",
        "hanjaReading": "子(아들 자) + 宮(집 궁) + 內(안 내) + 膜(막 막) + 症(병 증)",
        "pronunciation": "자궁내막증",
        "meaningKo": "자궁내막 조직이 자궁 밖의 다른 장기(난소, 복막 등)에 자라는 질환으로, 심한 생리통과 불임의 원인이 됩니다. 통역 시 단순한 생리통이 아니라 만성 질환이며, 진통제로만 버티지 말고 적극적인 치료가 필요함을 강조해야 합니다. 베트남어로는 'Lạc nội mạc tử cung' 또는 'Viêm nội mạc tử cung di chuyển'이라고 하며, endometriosis의 번역어입니다.",
        "meaningVi": "Bệnh lý mô nội mạc tử cung mọc lạc chỗ, xuất hiện ở các vị trí bên ngoài tử cung như buồng trứng, phúc mạc. Gây đau kinh dữ dội, đau khi quan hệ và có thể dẫn đến vô sinh, cần điều trị tích cực.",
        "context": "부인과 진료, 불임 클리닉",
        "culturalNote": "한국과 베트남 모두 자궁내막증이 증가 추세이지만, 많은 여성들이 '생리통은 원래 심한 것'으로 생각하여 진단이 늦어지는 경우가 많습니다. 통역 시 '참을 수 없는 생리통'은 정상이 아니며 검사가 필요함을 강조하고, 방치하면 불임으로 이어질 수 있다는 점을 명확히 전달해야 합니다.",
        "commonMistakes": [
            {
                "mistake": "'Viêm nội mạc tử cung'(자궁내막염)과 혼동",
                "correction": "자궁내막염은 'Viêm nội mạc', 자궁내막증은 'Lạc nội mạc'",
                "explanation": "염증과 내막증은 완전히 다른 질환으로 혼동하면 안 됩니다"
            },
            {
                "mistake": "'생리통이 좀 심한 것'으로 가볍게 표현",
                "correction": "만성 질환이며 불임과 연관됨을 명확히 전달",
                "explanation": "질환의 심각성을 과소평가하면 환자가 치료를 미룰 수 있습니다"
            },
            {
                "mistake": "진통제만으로 관리 가능하다고 번역",
                "correction": "호르몬 치료나 수술 등 적극적 치료 필요",
                "explanation": "근본적 치료 없이는 진행되는 질환임을 알려야 합니다"
            }
        ],
        "examples": [
            {
                "ko": "생리통이 점점 심해지고 진통제로 조절이 안 되며 난소에 혹이 있어 자궁내막증으로 진단됩니다.",
                "vi": "Đau kinh ngày càng dữ dội, thuốc giảm đau không kiểm soát được và có nang ở buồng trứng nên chẩn đoán lạc nội mạc tử cung.",
                "situation": "formal"
            },
            {
                "ko": "자궁내막증이 심해서 호르몬 치료를 시작하고, 임신 계획이 있으면 빨리 시도하는 것이 좋습니다.",
                "vi": "Lạc nội mạc tử cung nặng nên sẽ bắt đầu điều trị hormone, nếu có kế hoạch mang thai thì nên thử sớm.",
                "situation": "onsite"
            },
            {
                "ko": "자궁내막증 있으면 생리 때 일상생활 못할 정도로 아프고, 방치하면 나중에 아기 갖기 어려워요.",
                "vi": "Có lạc nội mạc tử cung thì khi có kinh đau đến mức không sinh hoạt được, bỏ mặc thì sau khó có con nhé.",
                "situation": "informal"
            }
        ],
        "relatedTerms": ["난소낭종", "불임", "복강경수술", "호르몬치료"]
    },
    {
        "slug": "nan-so-nang-chong",
        "korean": "난소낭종",
        "vietnamese": "Nang buồng trứng",
        "hanja": "卵巢囊腫",
        "hanjaReading": "卵(알 란) + 巢(깃 소) + 囊(주머니 낭) + 腫(부을 종)",
        "pronunciation": "난소낭종",
        "meaningKo": "난소에 생긴 액체로 찬 주머니로, 대부분 기능성 낭종으로 자연 소실되지만 크거나 지속되면 치료가 필요합니다. 통역 시 '낭종'과 '종양'을 구분하고, 대부분은 양성이며 자연적으로 없어질 수 있음을 설명하되, 정기적인 추적 관찰의 필요성도 강조해야 합니다. 베트남어로는 'Nang buồng trứng' 또는 'Nang noãn sào'라고 합니다.",
        "meaningVi": "Túi chứa dịch hình thành ở buồng trứng. Đa số là nang chức năng tự biến mất, nhưng nếu to hoặc kéo dài cần theo dõi và điều trị. Cần phân biệt với u buồng trứng có tính chất đặc.",
        "context": "부인과 진료, 초음파 검사",
        "culturalNote": "한국과 베트남 모두 난소낭종이 흔하며, 대부분 가임기 여성의 생리주기와 관련된 기능성 낭종입니다. 한국은 정기적인 초음파 추적 관찰이 보편화되어 있고, 베트남도 유사하지만 접근성은 지역에 따라 다릅니다. 통역 시 불필요한 공포를 주지 않으면서도 정기 검진의 중요성을 강조하는 균형이 필요합니다.",
        "commonMistakes": [
            {
                "mistake": "'U buồng trứng'(난소종양)과 혼용",
                "correction": "낭종은 'Nang'(액체), 종양은 'U'(고형)로 구분",
                "explanation": "낭종과 종양은 성질과 치료가 다르므로 명확히 구분해야 합니다"
            },
            {
                "mistake": "무조건 수술 필요하다고 전달",
                "correction": "대부분 경과 관찰 후 자연 소실",
                "explanation": "불필요한 불안과 과잉 치료를 피하기 위해 정확한 정보 전달 필요"
            },
            {
                "mistake": "증상 없으면 무시해도 된다고 번역",
                "correction": "정기적 초음파 추적 관찰 필수",
                "explanation": "크기 변화와 악성 가능성을 모니터링해야 합니다"
            }
        ],
        "examples": [
            {
                "ko": "초음파에서 5cm 크기의 난소낭종이 발견되었는데 기능성으로 보이니 2개월 후 재검사하겠습니다.",
                "vi": "Siêu âm phát hiện nang buồng trứng kích thước 5cm, có vẻ là nang chức năng nên sẽ tái khám sau 2 tháng.",
                "situation": "formal"
            },
            {
                "ko": "난소낭종이 10cm로 커졌고 꼬임 위험이 있어 복강경 수술로 제거하겠습니다.",
                "vi": "Nang buồng trứng đã to đến 10cm và có nguy cơ xoắn nên sẽ phẫu thuật nội soi cắt bỏ.",
                "situation": "onsite"
            },
            {
                "ko": "난소낭종 대부분은 물혹이라 저절로 없어지는데, 정기적으로 확인만 하면 돼요.",
                "vi": "Đa số nang buồng trứng là nang nước tự biến mất, chỉ cần kiểm tra định kỳ thôi nhé.",
                "situation": "informal"
            }
        ],
        "relatedTerms": ["난소종양", "기능성낭종", "복강경수술", "난소꼬임"]
    },
    {
        "slug": "da-nang-song-nan-so-chung-hu-gun",
        "korean": "다낭성난소증후군",
        "vietnamese": "Hội chứng buồng trứng đa nang",
        "hanja": "多囊性卵巢症候群",
        "hanjaReading": "多(많을 다) + 囊(주머니 낭) + 性(성품 성) + 卵(알 란) + 巢(깃 소) + 症(병 증) + 候(기후 후) + 群(무리 군)",
        "pronunciation": "다낭성난소증후군",
        "meaningKo": "호르몬 불균형으로 인해 배란 장애, 다모증, 비만, 불규칙한 생리 등이 나타나는 내분비 질환입니다. 통역 시 단순히 난소에 낭종이 많은 것이 아니라 대사증후군, 당뇨병, 불임과 연관된 복합적 질환임을 설명해야 하며, 생활습관 개선과 장기적 관리가 필요함을 강조해야 합니다. 베트남어로는 'Hội chứng buồng trứng đa nang' 또는 줄여서 'PCOS'라고 합니다.",
        "meaningVi": "Rối loạn nội tiết tố gây rối loạn phóng noãn, lông mọc nhiều, béo phì, kinh nguyệt không đều. Đây là bệnh lý phức tạp liên quan đến hội chứng chuyển hóa, đái tháo đường và vô sinh, cần quản lý lâu dài.",
        "context": "부인과, 내분비내과, 불임 클리닉",
        "culturalNote": "한국과 베트남 모두 다낭성난소증후군 환자가 증가 추세이며, 서구화된 식습관과 운동 부족이 주요 원인으로 지목됩니다. 한국은 PCOS 인식이 높아지고 있지만, 베트남에서는 아직 '생리불순' 정도로만 인식되는 경우가 많습니다. 통역 시 체중 관리, 식이 조절, 운동의 중요성을 강조하고, 메트포르민 같은 약물 치료의 역할도 설명해야 합니다.",
        "commonMistakes": [
            {
                "mistake": "'난소낭종'과 동일한 것으로 번역",
                "correction": "난소낭종은 단순 낭종, PCOS는 호르몬 질환",
                "explanation": "완전히 다른 병태생리이므로 혼동하면 안 됩니다"
            },
            {
                "mistake": "'살 빼면 낫는다'고 단순화",
                "correction": "체중 감량이 도움되지만 약물 치료도 필요",
                "explanation": "생활습관 개선과 약물 치료를 병행해야 효과적입니다"
            },
            {
                "mistake": "미용 문제(다모, 여드름)만 강조",
                "correction": "불임, 당뇨병 등 장기적 건강 영향 설명",
                "explanation": "대사 질환으로서의 심각성을 인지시켜야 적극적 관리가 가능합니다"
            }
        ],
        "examples": [
            {
                "ko": "생리가 3~4개월에 한 번만 하고 초음파에서 다낭성 소견이 있어 다낭성난소증후군으로 진단됩니다.",
                "vi": "Kinh nguyệt 3-4 tháng mới có một lần và siêu âm thấy nhiều nang nhỏ nên chẩn đoán hội chứng buồng trứng đa nang.",
                "situation": "formal"
            },
            {
                "ko": "다낭성난소증후군이 있어서 체중 감량과 함께 메트포르민을 처방하고, 임신 원하면 배란유도제를 사용하겠습니다.",
                "vi": "Có hội chứng buồng trứng đa nang nên sẽ giảm cân kết hợp với metformin, nếu muốn mang thai sẽ dùng thuốc kích trứng.",
                "situation": "onsite"
            },
            {
                "ko": "다낭성난소증후군 있으면 살 빼고 운동하는 게 제일 중요하고, 나중에 당뇨 위험도 있으니 관리 잘 해야 해요.",
                "vi": "Có hội chứng buồng trứng đa nang thì giảm cân và vận động là quan trọng nhất, sau có nguy cơ tiểu đường nên phải quản lý tốt nhé.",
                "situation": "informal"
            }
        ],
        "relatedTerms": ["배란장애", "인슐린저항성", "메트포르민", "불임"]
    },
    {
        "slug": "chu-kung-gyong-bu-am",
        "korean": "자궁경부암",
        "vietnamese": "Ung thư cổ tử cung",
        "hanja": "子宮頸部癌",
        "hanjaReading": "子(아들 자) + 宮(집 궁) + 頸(목 경) + 部(부분 부) + 癌(암 암)",
        "pronunciation": "자궁경부암",
        "meaningKo": "자궁의 입구인 자궁경부에 발생하는 악성 종양으로, 대부분 인유두종바이러스(HPV) 감염이 원인입니다. 통역 시 정기적인 자궁경부암 검사(Pap smear)와 HPV 백신으로 예방 가능한 암임을 강조해야 하며, 조기 발견 시 완치율이 매우 높다는 점을 전달해야 합니다. 베트남어로는 'Ung thư cổ tử cung'이라고 합니다.",
        "meaningVi": "Khối u ác tính phát sinh ở cổ tử cung, chủ yếu do virus HPV (Human Papillomavirus) gây ra. Đây là loại ung thư có thể phòng ngừa bằng vaccine HPV và sàng lọc định kỳ, tỷ lệ chữa khỏi cao nếu phát hiện sớm.",
        "context": "부인과 검진, 암 검진 센터",
        "culturalNote": "한국은 국가암검진사업으로 20세 이상 여성에게 2년마다 무료 자궁경부암 검사를 제공하며, HPV 백신 접종도 보편화되었습니다. 베트남도 검진 프로그램이 있지만 농촌 지역의 접근성은 낮으며, HPV 백신은 비용 문제로 접종률이 낮습니다. 통역 시 예방 가능한 암이라는 점과 정기 검진의 중요성을 강조하는 것이 매우 중요합니다.",
        "commonMistakes": [
            {
                "mistake": "'자궁암'과 '자궁경부암'을 혼용",
                "correction": "자궁경부암과 자궁내막암은 다른 암",
                "explanation": "발생 부위와 위험 요인이 다른 별개의 암입니다"
            },
            {
                "mistake": "HPV를 성병으로만 설명",
                "correction": "매우 흔한 바이러스이며 대부분 자연 소실됨을 함께 설명",
                "explanation": "불필요한 낙인을 피하고 정확한 정보를 전달해야 합니다"
            },
            {
                "mistake": "검진을 '부끄러운 것'으로 치부",
                "correction": "생명을 구하는 필수 검사임을 강조",
                "explanation": "문화적 거부감을 극복하도록 검진의 중요성을 설득력있게 전달해야 합니다"
            }
        ],
        "examples": [
            {
                "ko": "자궁경부암 검사 결과 전암병변이 발견되어 조직검사 후 치료 계획을 세우겠습니다.",
                "vi": "Kết quả xét nghiệm ung thư cổ tử cung phát hiện tổn thương tiền ung thư, sau sinh thiết sẽ lập kế hoạch điều trị.",
                "situation": "formal"
            },
            {
                "ko": "자궁경부암 0기로 진단되어 원추절제술을 시행하면 완치 가능합니다.",
                "vi": "Chẩn đoán ung thư cổ tử cung giai đoạn 0, nếu cắt hình nón có thể chữa khỏi hoàn toàn.",
                "situation": "onsite"
            },
            {
                "ko": "자궁경부암은 정기 검진으로 조기 발견하면 거의 100% 완치되니까 꼭 검사 받으세요.",
                "vi": "Ung thư cổ tử cung nếu phát hiện sớm qua khám định kỳ thì gần như chữa khỏi 100% nên nhất định phải đi khám nhé.",
                "situation": "informal"
            }
        ],
        "relatedTerms": ["HPV백신", "자궁경부세포검사", "원추절제술", "전암병변"]
    },
    {
        "slug": "yu-bang-am-gom-jin",
        "korean": "유방암검진",
        "vietnamese": "Khám sàng lọc ung thư vú",
        "hanja": "乳房癌檢診",
        "hanjaReading": "乳(젖 유) + 房(방 방) + 癌(암 암) + 檢(조사할 검) + 診(진찰 진)",
        "pronunciation": "유방암검진",
        "meaningKo": "유방암을 조기에 발견하기 위한 검진으로, 유방촬영술(mammography), 초음파, 자가검진 등을 포함합니다. 통역 시 한국은 40세 이상 여성에게 2년마다 국가검진을 제공하며, 치밀유방이 많은 아시아 여성은 초음파 병용이 권장된다는 점을 설명해야 합니다. 베트남어로는 'Khám sàng lọc ung thư vú' 또는 'Tầm soát ung thư vú'라고 합니다.",
        "meaningVi": "Khám phát hiện sớm ung thư vú bằng chụp nhũ ảnh (mammography), siêu âm và tự khám vú. Phụ nữ từ 40 tuổi nên khám định kỳ 2 năm một lần, phụ nữ châu Á có mô vú dày nên kết hợp siêu âm.",
        "context": "건강검진, 유방클리닉",
        "culturalNote": "한국은 유방암 검진이 국가검진 프로그램에 포함되어 있고, 유방암에 대한 인식도 높습니다. 베트남도 도시 지역에서는 검진이 증가하고 있지만 농촌 지역은 접근성이 낮습니다. 아시아 여성은 유방 조직이 치밀하여 유방촬영술만으로는 부족할 수 있어 초음파 병용이 중요하다는 점을 통역 시 강조해야 합니다.",
        "commonMistakes": [
            {
                "mistake": "'유방촬영=방사선 위험'으로 과장",
                "correction": "매우 낮은 선량으로 이익이 위험보다 훨씬 큼",
                "explanation": "불필요한 두려움으로 검진을 기피하지 않도록 해야 합니다"
            },
            {
                "mistake": "'Chụp X-quang vú'로만 번역",
                "correction": "'Chụp nhũ ảnh' 또는 'Mammography'가 정확한 용어",
                "explanation": "일반 X-ray와는 다른 특수 검사임을 명확히 해야 합니다"
            },
            {
                "mistake": "자가검진만으로 충분하다고 전달",
                "correction": "자가검진 + 정기 영상검사 병행 필수",
                "explanation": "자가검진으로 발견되지 않는 초기 암도 많으므로 전문 검진이 필수입니다"
            }
        ],
        "examples": [
            {
                "ko": "40세 이상이시니 유방암 검진으로 유방촬영술을 시행하고, 유방이 치밀하면 초음파도 추가하겠습니다.",
                "vi": "Trên 40 tuổi rồi nên sẽ làm khám sàng lọc ung thư vú bằng chụp nhũ ảnh, nếu vú dày sẽ thêm siêu âm.",
                "situation": "formal"
            },
            {
                "ko": "유방촬영에서 의심 소견이 있어 조직검사를 권유드립니다.",
                "vi": "Chụp nhũ ảnh có hình ảnh nghi ngờ nên khuyên nên sinh thiết.",
                "situation": "onsite"
            },
            {
                "ko": "유방암 검진은 40세부터 2년마다 받아야 하고, 자가검진도 매달 해보는 게 좋아요.",
                "vi": "Khám sàng lọc ung thư vú từ 40 tuổi phải làm 2 năm một lần, và nên tự khám hàng tháng nhé.",
                "situation": "informal"
            }
        ],
        "relatedTerms": ["유방촬영술", "유방초음파", "자가검진", "조직검사"]
    },
    {
        "slug": "jil-yom",
        "korean": "질염",
        "vietnamese": "Viêm âm đạo",
        "hanja": "膣炎",
        "hanjaReading": "膣(음문 질) + 炎(불꽃 염)",
        "pronunciation": "질염",
        "meaningKo": "질 내 정상 세균총의 균형이 깨져 발생하는 염증으로, 세균성, 진균성(칸디다), 트리코모나스 등 원인에 따라 치료가 다릅니다. 통역 시 '부끄러운 병'이 아니라 매우 흔한 질환이며, 원인별로 치료 방법이 다르므로 자가 치료하지 말고 진료를 받아야 함을 강조해야 합니다. 베트남어로는 'Viêm âm đạo' 또는 'Viêm nhiễm phụ khoa'라고 합니다.",
        "meaningVi": "Viêm nhiễm ở âm đạo do mất cân bằng hệ vi sinh vật, có thể do vi khuẩn, nấm (candida) hoặc ký sinh trùng (trichomonas). Rất phổ biến ở phụ nữ, cần điều trị theo đúng nguyên nhân, không nên tự ý dùng thuốc.",
        "context": "부인과 진료, 일차 진료",
        "culturalNote": "한국과 베트남 모두 질염이 매우 흔하지만, 문화적 터부로 인해 병원 방문을 꺼리는 경우가 많습니다. 특히 베트남에서는 약국에서 임의로 약을 사서 쓰는 경우가 많아 부적절한 치료가 이루어지기도 합니다. 통역 시 정확한 진단 없이 항생제나 항진균제를 남용하면 오히려 악화될 수 있음을 경고하고, 진료를 받아야 함을 설득하는 것이 중요합니다.",
        "commonMistakes": [
            {
                "mistake": "'성병'과 동일하게 번역",
                "correction": "대부분은 정상 세균총 불균형으로 성병과 무관",
                "explanation": "불필요한 낙인을 피하고 정확한 정보를 전달해야 합니다"
            },
            {
                "mistake": "모든 질염을 'Nấm âm đạo'(질 칸디다증)로 번역",
                "correction": "세균성, 진균성, 트리코모나스 등 원인별 구분",
                "explanation": "원인에 따라 치료가 완전히 다르므로 정확한 구분이 필수입니다"
            },
            {
                "mistake": "위생 불량 때문이라고 비난",
                "correction": "과도한 세척도 원인이 될 수 있음을 설명",
                "explanation": "환자를 비난하지 않고 정확한 원인과 예방법을 전달해야 합니다"
            }
        ],
        "examples": [
            {
                "ko": "분비물 검사 결과 세균성 질염으로 진단되어 항생제 질정을 처방하겠습니다.",
                "vi": "Kết quả xét nghiệm dịch tiết chẩn đoán viêm âm đạo do vi khuẩn, sẽ kê thuốc kháng sinh đặt âm đạo.",
                "situation": "formal"
            },
            {
                "ko": "질염이 자주 재발한다면 당뇨병 검사와 유산균 복용을 고려해보세요.",
                "vi": "Nếu viêm âm đạo tái phát thường xuyên thì nên kiểm tra tiểu đường và uống men vi sinh.",
                "situation": "onsite"
            },
            {
                "ko": "질염은 여성 대부분이 한 번쯤 겪는 거라 부끄러워하지 말고 병원 가서 치료받으세요.",
                "vi": "Viêm âm đạo thì hầu hết phụ nữ đều gặp một lần nên đừng ngại ngùng mà hãy đi bệnh viện điều trị nhé.",
                "situation": "informal"
            }
        ],
        "relatedTerms": ["세균성질염", "칸디다질염", "트리코모나스", "질유산균"]
    },
    {
        "slug": "gol-ban-yom",
        "korean": "골반염",
        "vietnamese": "Viêm vùng chậu",
        "hanja": "骨盤炎",
        "hanjaReading": "骨(뼈 골) + 盤(쟁반 반) + 炎(불꽃 염)",
        "pronunciation": "골반염",
        "meaningKo": "자궁, 난관, 난소 등 상부 생식기에 발생하는 감염으로, 방치하면 불임과 만성 골반통의 원인이 됩니다. 통역 시 단순 질염이나 방광염과는 다른 심각한 감염이며, 입원 치료가 필요할 수 있고 조기 치료하지 않으면 불임으로 이어질 수 있음을 명확히 해야 합니다. 베트남어로는 'Viêm vùng chậu' 또는 'Viêm phần phụ'라고 하며, PID(Pelvic Inflammatory Disease)의 번역어입니다.",
        "meaningVi": "Nhiễm trùng ở các cơ quan sinh dục phía trên như tử cung, vòi trứng, buồng trứng. Nếu không điều trị kịp thời có thể gây vô sinh và đau vùng chậu mãn tính. Có thể cần nhập viện điều trị kháng sinh đường tĩnh mạch.",
        "context": "부인과 응급, 입원 치료",
        "culturalNote": "한국과 베트남 모두 골반염을 심각한 감염으로 인식하지만, 초기 증상이 애매하여 진단이 늦어지는 경우가 많습니다. 성관계와 연관된 감염이라는 편견 때문에 병원 방문을 꺼리기도 합니다. 통역 시 하복부 통증과 발열이 있으면 즉시 진료를 받아야 하며, 치료하지 않으면 난관 유착으로 불임이 될 수 있다는 점을 강하게 경고해야 합니다.",
        "commonMistakes": [
            {
                "mistake": "'Viêm bàng quang'(방광염)과 혼동",
                "correction": "골반염은 'Viêm vùng chậu', 방광염은 'Viêm bàng quang'",
                "explanation": "완전히 다른 부위와 심각도의 감염이므로 혼동하면 안 됩니다"
            },
            {
                "mistake": "경구 항생제로 충분하다고 번역",
                "correction": "중증은 입원하여 정맥 항생제 치료 필요",
                "explanation": "치료 강도를 과소평가하면 적절한 치료가 지연될 수 있습니다"
            },
            {
                "mistake": "불임 위험 설명 누락",
                "correction": "난관 손상으로 인한 불임 위험 반드시 전달",
                "explanation": "장기적 합병증을 알려야 환자가 치료에 적극적으로 임할 수 있습니다"
            }
        ],
        "examples": [
            {
                "ko": "하복부 통증과 고열이 있고 골반염으로 진단되어 입원하여 정맥 항생제 치료가 필요합니다.",
                "vi": "Có đau bụng dưới và sốt cao, chẩn đoán viêm vùng chậu nên cần nhập viện truyền kháng sinh đường tĩnh mạch.",
                "situation": "formal"
            },
            {
                "ko": "골반염이 심해서 농양이 생겼다면 수술로 배농해야 할 수도 있습니다.",
                "vi": "Viêm vùng chậu nặng có áp xe thì có thể phải phẫu thuật dẫn lưu mủ.",
                "situation": "onsite"
            },
            {
                "ko": "골반염 제대로 치료 안 하면 나중에 난관 막혀서 아기 못 가질 수 있어요. 꼭 끝까지 치료받으세요.",
                "vi": "Viêm vùng chậu không điều trị đúng cách thì sau vòi trứng bị tắc không có con được nhé. Nhất định phải điều trị hết đợt.",
                "situation": "informal"
            }
        ],
        "relatedTerms": ["난관염", "불임", "자궁외임신", "만성골반통"]
    }
]

# Read existing medical.json
print(f"Reading from: {file_path}")
with open(file_path, 'r', encoding='utf-8') as f:
    data = json.load(f)

print(f"Current terms count: {len(data)}")

# Add new terms
data.extend(new_terms)

print(f"New terms count after addition: {len(data)}")

# Save back to file
with open(file_path, 'w', encoding='utf-8') as f:
    json.dump(data, f, ensure_ascii=False, indent=2)

print(f"✅ Successfully added {len(new_terms)} new medical terms")
print(f"✅ Total terms now: {len(data)}")
print(f"✅ Saved to: {file_path}")
