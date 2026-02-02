#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import json
import os

# Path handling (REQUIRED)
file_path = os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', 'data', 'terms', 'medical.json')

# Load existing data
with open(file_path, 'r', encoding='utf-8') as f:
    data = json.load(f)  # data is a LIST, not dict

existing_slugs = {t['slug'] for t in data}

# New terms (20)
new_terms = [
    {
        "slug": "sinh-thuong",
        "korean": "자연분만",
        "vietnamese": "Sinh thường",
        "hanja": "自然分娩",
        "hanjaReading": "自(스스로 자) + 然(그러할 연) + 分(나눌 분) + 娩(해산할 만)",
        "pronunciation": "자연분만",
        "meaningKo": "질을 통해 자연스럽게 아기를 출산하는 방법. 통역 시 '자연분만'과 '정상분만'을 구분해야 하며, 베트남에서는 'sinh thường'로 불림. 제왕절개(sinh mổ)와 명확히 구분하여 번역해야 하며, 환자에게 분만 방법을 설명할 때 오해가 없도록 주의 필요. 의료진과 산모 간 의사소통에서 가장 빈번히 사용되는 용어로, 정확한 통역이 중요함.",
        "meaningVi": "Phương pháp sinh con qua đường âm đạo một cách tự nhiên, không qua phẫu thuật. Đây là cách sinh con phổ biến nhất và được khuyến khích nếu sức khỏe mẹ và bé cho phép. Sinh thường giúp mẹ hồi phục nhanh hơn so với sinh mổ.",
        "context": "산부인과 진료, 출산 계획 상담",
        "culturalNote": "한국에서는 자연분만을 권장하지만 제왕절개율이 높은 편. 베트남도 최근 제왕절개가 증가하는 추세이나 여전히 자연분만을 선호. 양국 모두 산모의 선택권을 중요시하지만, 의료진의 권고가 큰 영향을 미침. 통역 시 산모의 불안감을 고려한 표현 사용 필요.",
        "commonMistakes": [
            {
                "mistake": "sinh tự nhiên (자연 출산)",
                "correction": "sinh thường (자연분만)",
                "explanation": "'sinh tự nhiên'은 일상 표현이며, 의료 용어로는 'sinh thường'이 정확함"
            },
            {
                "mistake": "정상분만을 sinh bình thường으로 번역",
                "correction": "정상분만도 sinh thường",
                "explanation": "한국어 '정상분만'과 '자연분만'은 같은 의미로 모두 'sinh thường'"
            },
            {
                "mistake": "đẻ thường (구어체)",
                "correction": "sinh thường (의료 용어)",
                "explanation": "환자와 대화 시 'đẻ thường'도 사용 가능하나, 의료진 간에는 'sinh thường' 사용"
            }
        ],
        "examples": [
            {
                "ko": "산모의 건강 상태가 좋아 자연분만이 가능합니다.",
                "vi": "Sức khỏe sản phụ tốt nên có thể sinh thường.",
                "situation": "formal"
            },
            {
                "ko": "자연분만과 제왕절개 중 어떤 방법을 원하시나요?",
                "vi": "Chị muốn sinh thường hay sinh mổ ạ?",
                "situation": "onsite"
            },
            {
                "ko": "첫째는 자연분만으로 낳았어요.",
                "vi": "Con đầu em đẻ thường ạ.",
                "situation": "informal"
            }
        ],
        "relatedTerms": ["제왕절개", "무통분만", "유도분만", "조산"]
    },
    {
        "slug": "sinh-mo",
        "korean": "제왕절개",
        "vietnamese": "Sinh mổ",
        "hanja": "帝王切開",
        "hanjaReading": "帝(임금 제) + 王(임금 왕) + 切(끊을 절) + 開(열 개)",
        "pronunciation": "제왕절개",
        "meaningKo": "복부와 자궁을 절개하여 아기를 출산하는 수술적 분만 방법. 통역 시 '계획 제왕절개'와 '응급 제왕절개'를 구분해야 하며, 베트남어로는 'sinh mổ' 또는 'mổ đẻ'로 표현. 수술 전 환자 동의와 설명이 중요하므로 정확한 통역 필요. 의료 실수나 오해를 방지하기 위해 수술 사유와 과정을 명확히 전달해야 함.",
        "meaningVi": "Phương pháp sinh con bằng cách phẫu thuật rạch bụng và tử cung của người mẹ để lấy thai nhi ra. Được chỉ định khi sinh thường gặp nguy hiểm hoặc theo yêu cầu của sản phụ. Thời gian hồi phục lâu hơn sinh thường.",
        "context": "산부인과 수술, 출산 방법 상담",
        "culturalNote": "한국의 제왕절개율은 OECD 국가 중 높은 편(약 50%)이며, 베트남도 도시 지역에서 증가 추세. 양국 모두 '편한 출산'을 위한 선택적 제왕절개가 논란. 한국은 '황제절개'라는 속칭도 있으나 베트남에는 그런 표현 없음. 통역 시 의학적 필요성과 산모의 선택권을 균형있게 전달 필요.",
        "commonMistakes": [
            {
                "mistake": "phẫu thuật sinh (수술 출산)",
                "correction": "sinh mổ 또는 mổ đẻ",
                "explanation": "'phẫu thuật sinh'은 정확하나 구체적이지 않음. 'sinh mổ'가 제왕절개 전문 용어"
            },
            {
                "mistake": "계획 제왕절개를 sinh mổ kế hoạch로 번역",
                "correction": "mổ đẻ theo lịch hẹn 또는 mổ đẻ có kế hoạch",
                "explanation": "베트남 의료 현장에서는 'mổ đẻ theo lịch hẹn'이 더 자연스러움"
            },
            {
                "mistake": "응급 제왕절개를 sinh mổ khẩn cấp",
                "correction": "mổ đẻ cấp cứu",
                "explanation": "'cấp cứu'가 응급 상황에 더 적합한 표현"
            }
        ],
        "examples": [
            {
                "ko": "태아의 위치상 제왕절개가 필요합니다.",
                "vi": "Vị trí thai nhi cần phải sinh mổ.",
                "situation": "formal"
            },
            {
                "ko": "언제 제왕절개 수술을 받으실 건가요?",
                "vi": "Khi nào chị sẽ mổ đẻ ạ?",
                "situation": "onsite"
            },
            {
                "ko": "둘째는 제왕절개로 낳았어요.",
                "vi": "Con thứ hai em mổ đẻ.",
                "situation": "informal"
            }
        ],
        "relatedTerms": ["자연분만", "응급제왕절개", "반복제왕절개", "수술"]
    },
    {
        "slug": "sinh-khong-dau",
        "korean": "무통분만",
        "vietnamese": "Sinh không đau",
        "hanja": "無痛分娩",
        "hanjaReading": "無(없을 무) + 痛(아플 통) + 分(나눌 분) + 娩(해산할 만)",
        "pronunciation": "무통분만",
        "meaningKo": "마취제를 사용하여 분만 시 통증을 줄이는 방법. 주로 경막외마취(epidural)를 사용함. 통역 시 '무통'이 '완전히 통증이 없다'는 오해를 주지 않도록 주의해야 하며, 실제로는 '통증 감소'를 의미함을 명확히 전달. 베트nam에서는 아직 보편화되지 않아 환자가 생소해할 수 있으므로 자세한 설명 필요.",
        "meaningVi": "Phương pháp giảm đau khi sinh con bằng cách sử dụng thuốc gây tê vùng cột sống (gây tê ngoài màng cứng). Giúp sản phụ giảm đau đớn trong quá trình chuyển dạ và sinh con, nhưng vẫn có thể cảm nhận được co thắt tử cung.",
        "context": "산부인과 분만, 마취과 협진",
        "culturalNote": "한국에서는 무통분만이 보편화되어 있으나 추가 비용 발생. 베트남에서는 대도시 큰 병원에서만 가능하며 비용이 높아 일반적이지 않음. 한국 산모들은 당연시하는 경우가 많으나 베트남 산모는 잘 모르는 경우 많음. 통역 시 비용과 효과, 부작용을 균형있게 설명 필요.",
        "commonMistakes": [
            {
                "mistake": "gây mê sinh (마취 분만)",
                "correction": "sinh không đau 또는 gây tê ngoài màng cứng khi sinh",
                "explanation": "'gây mê'는 전신마취를 의미하므로 부정확. 무통분만은 부분마취임"
            },
            {
                "mistake": "무통분만을 '완전히 아프지 않다'로 설명",
                "correction": "'통증이 많이 줄어든다'로 설명",
                "explanation": "무통분만도 약간의 통증과 압박감은 느낄 수 있음을 환자에게 명확히 전달 필요"
            },
            {
                "mistake": "epidural을 에피듀랄로 음역",
                "correction": "gây tê ngoài màng cứng (경막외마취)",
                "explanation": "베트남어로 정확한 의학 용어 사용 필요"
            }
        ],
        "examples": [
            {
                "ko": "무통분만을 원하시면 마취과 상담이 필요합니다.",
                "vi": "Nếu muốn sinh không đau, chị cần tư vấn với bác sĩ gây mê.",
                "situation": "formal"
            },
            {
                "ko": "무통분만 하시면 비용이 추가됩니다.",
                "vi": "Nếu sinh không đau sẽ tốn thêm chi phí ạ.",
                "situation": "onsite"
            },
            {
                "ko": "저는 무통분만으로 했는데 정말 좋았어요.",
                "vi": "Em sinh không đau, rất tốt luôn.",
                "situation": "informal"
            }
        ],
        "relatedTerms": ["경막외마취", "자연분만", "진통", "마취"]
    },
    {
        "slug": "chuyen-da-som",
        "korean": "조기진통",
        "vietnamese": "Chuyển dạ sớm",
        "hanja": "早期陣痛",
        "hanjaReading": "早(이를 조) + 期(기약할 기) + 陣(진칠 진) + 痛(아플 통)",
        "pronunciation": "조기진통",
        "meaningKo": "임신 37주 이전에 규칙적인 자궁수축이 나타나는 상태. 조산의 위험이 있어 즉시 의료 조치가 필요함. 통역 시 '진통'과 '수축'의 차이, 그리고 긴급성을 명확히 전달해야 함. 베트남어로 'chuyển dạ sớm'이며, 환자가 병원에 빨리 와야 한다는 긴박감을 전달하는 것이 중요. 실수로 정상 진통과 혼동하지 않도록 주의.",
        "meaningVi": "Tình trạng co thắt tử cung đều đặn xảy ra trước tuần thai thứ 37. Đây là dấu hiệu nguy hiểm có thể dẫn đến sinh non, cần đến bệnh viện ngay lập tức để được xử trí kịp thời và bảo vệ sức khỏe thai nhi.",
        "context": "응급 산부인과, 고위험 임신 관리",
        "culturalNote": "한국과 베트남 모두 조기진통을 심각하게 받아들이나, 베트남의 의료 접근성이 낮은 지역에서는 대응이 늦을 수 있음. 한국은 119 시스템이 잘 갖춰져 있으나 베트남은 지역 격차가 큼. 통역 시 즉시 병원 방문의 중요성을 강조하고, 이동 수단과 시간을 고려한 조언 필요.",
        "commonMistakes": [
            {
                "mistake": "đau bụng sớm (배 아픔 일찍)",
                "correction": "chuyển dạ sớm (조기진통)",
                "explanation": "'đau bụng'은 일반적인 복통으로 오해될 수 있음. 의학적으로 정확한 용어 사용 필요"
            },
            {
                "mistake": "진통을 đau đẻ로만 번역",
                "correction": "chuyển dạ (진통의 정확한 의학 용어)",
                "explanation": "'đau đẻ'는 구어체이며, 'chuyển dạ'가 의료 현장의 표준 용어"
            },
            {
                "mistake": "조기진통을 '가진통'과 혼동",
                "correction": "가진통은 co thắt giả, 조기진통은 chuyển dạ sớm",
                "explanation": "가진통(Braxton Hicks)과 조기진통은 완전히 다른 개념으로 구분 필요"
            }
        ],
        "examples": [
            {
                "ko": "규칙적인 수축이 있다면 조기진통일 수 있으니 즉시 오세요.",
                "vi": "Nếu có co thắt đều đặn có thể là chuyển dạ sớm, cần đến ngay.",
                "situation": "formal"
            },
            {
                "ko": "지금 몇 주인데 배가 계속 아프세요?",
                "vi": "Bây giờ được bao nhiêu tuần mà bụng cứ đau ạ?",
                "situation": "onsite"
            },
            {
                "ko": "32주에 조기진통 와서 입원했었어요.",
                "vi": "Tuần thứ 32 bị chuyển dạ sớm nên phải nhập viện.",
                "situation": "informal"
            }
        ],
        "relatedTerms": ["조산", "자궁수축억제제", "입원", "고위험임신"]
    },
    {
        "slug": "nhau-tien-dao",
        "korean": "전치태반",
        "vietnamese": "Nhau tiền đạo",
        "hanja": "前置胎盤",
        "hanjaReading": "前(앞 전) + 置(둘 치) + 胎(아이 밸 태) + 盤(소반 반)",
        "pronunciation": "전치태반",
        "meaningKo": "태반이 자궁경부를 부분적 또는 완전히 덮고 있는 상태. 출혈 위험이 높아 제왕절개가 필수이며 고위험 임신으로 분류됨. 통역 시 '전치태반'의 위험성과 제왕절개의 필요성을 명확히 전달해야 하며, 환자의 불안을 고려한 표현 사용 필요. 베트남어로 'nhau tiền đạo'이며, 절대 안정의 중요성을 강조해야 함.",
        "meaningVi": "Tình trạng bánh nhau (rau thai) che khuất một phần hoặc toàn bộ cổ tử cung. Đây là biến chứng nguy hiểm có thể gây chảy máu nhiều, bắt buộc phải sinh mổ và cần theo dõi sát sao trong suốt thai kỳ. Sản phụ cần hạn chế vận động mạnh.",
        "context": "산부인과 초음파 검사, 고위험 임신 상담",
        "culturalNote": "한국과 베트남 모두 전치태반을 심각한 합병증으로 인식. 한국은 정기 초음파로 조기 발견률이 높으나, 베트남 시골 지역은 검진 접근성이 낮아 뒤늦게 발견되는 경우 많음. 통역 시 정기 검진의 중요성과 출혈 시 응급 대응 방법을 명확히 전달해야 함. 환자의 공포심을 완화하면서도 위험성은 정확히 전달하는 균형 필요.",
        "commonMistakes": [
            {
                "mistake": "rau bong non (태반조기박리)",
                "correction": "nhau tiền đạo (전치태반)",
                "explanation": "태반조기박리와 전치태반은 완전히 다른 질환. 혼동 시 치명적 오해 발생 가능"
            },
            {
                "mistake": "태반 위치 이상을 vị trí nhau không bình thường로 모호하게 번역",
                "correction": "nhau tiền đạo (정확한 진단명)",
                "explanation": "명확한 진단명 사용으로 오해 방지 필요"
            },
            {
                "mistake": "전치태반 환자에게 '조금 위험하다' 정도로 축소 설명",
                "correction": "심각한 합병증임을 명확히 전달",
                "explanation": "환자가 위험성을 과소평가하지 않도록 정확한 통역 필요"
            }
        ],
        "examples": [
            {
                "ko": "전치태반으로 진단되어 절대 안정이 필요합니다.",
                "vi": "Chẩn đoán nhau tiền đạo, cần nghỉ ngơi tuyệt đối.",
                "situation": "formal"
            },
            {
                "ko": "출혈이 있으면 바로 응급실로 오셔야 해요.",
                "vi": "Nếu chảy máu phải đến cấp cứu ngay ạ.",
                "situation": "onsite"
            },
            {
                "ko": "전치태반이라 무조건 제왕절개래요.",
                "vi": "Nhau tiền đạo nên bắt buộc phải mổ đẻ.",
                "situation": "informal"
            }
        ],
        "relatedTerms": ["제왕절개", "태반조기박리", "산전출혈", "고위험임신"]
    },
    {
        "slug": "tien-san-giat",
        "korean": "임신중독증",
        "vietnamese": "Tiền sản giật",
        "hanja": "妊娠中毒症",
        "hanjaReading": "妊(아이 밸 임) + 娠(아이 밸 신) + 中(가운데 중) + 毒(독 독) + 症(병 증)",
        "pronunciation": "임신중독증",
        "meaningKo": "임신 20주 이후 고혈압과 단백뇨가 나타나는 질환으로, 심할 경우 경련(자간증)으로 진행될 수 있음. 모체와 태아 모두에게 치명적일 수 있어 즉각적인 치료 필요. 통역 시 '중독'이라는 표현이 오해를 줄 수 있으므로 정확한 의학적 설명 필요. 베트남어로 'tiền sản giật'이며, 혈압 관리와 정기 검진의 중요성을 강조해야 함.",
        "meaningVi": "Bệnh lý tăng huyết áp và protein niệu xuất hiện sau tuần thai thứ 20. Nếu không được điều trị kịp thời có thể gây co giật (sản giật), nguy hiểm đến tính mạng của cả mẹ và bé. Cần theo dõi huyết áp thường xuyên và khám thai định kỳ.",
        "context": "산부인과 진료, 고위험 임신 관리, 응급",
        "culturalNote": "한국에서는 '임신중독증'이라는 용어가 일반적이나 의학적으로는 '전자간증'이 정확함. 베트남은 'tiền sản giật'이 표준 용어. 양국 모두 이 질환을 심각하게 받아들이나, 베트남 시골에서는 검진 부족으로 발견이 늦은 경우 많음. 통역 시 '중독'이 태아에게 해로운 물질 섭취로 오해될 수 있으므로 혈압과 관련된 질환임을 명확히 설명.",
        "commonMistakes": [
            {
                "mistake": "중독을 ngộ độc (식중독 등)으로 번역",
                "correction": "tiền sản giật (전자간증의 정확한 용어)",
                "explanation": "'임신중독증'은 독성 물질 섭취가 아닌 혈압 질환임을 명확히 해야 함"
            },
            {
                "mistake": "전자간증과 자간증을 구분하지 않음",
                "correction": "tiền sản giật (전자간증), sản giật (자간증) 명확히 구분",
                "explanation": "경련 유무에 따라 다른 질환으로 심각도가 다름"
            },
            {
                "mistake": "단순 고혈압을 임신중독증으로 오역",
                "correction": "tăng huyết áp thai kỳ (임신성 고혈압) vs tiền sản giật (전자간증) 구분",
                "explanation": "단백뇨 유무로 구분되며 치료 방향이 다름"
            }
        ],
        "examples": [
            {
                "ko": "혈압이 높고 단백뇨가 나와 임신중독증이 의심됩니다.",
                "vi": "Huyết áp cao và có protein trong nước tiểu, nghi ngờ tiền sản giật.",
                "situation": "formal"
            },
            {
                "ko": "손발이 많이 부으시죠? 혈압 재봐야겠어요.",
                "vi": "Tay chân sưng nhiều phải không ạ? Cần đo huyết áp.",
                "situation": "onsite"
            },
            {
                "ko": "임신중독증 와서 일찍 낳았어요.",
                "vi": "Bị tiền sản giật nên phải sinh sớm.",
                "situation": "informal"
            }
        ],
        "relatedTerms": ["고혈압", "단백뇨", "부종", "자간증"]
    },
    {
        "slug": "thai-ngoai-tu-cung",
        "korean": "자궁외임신",
        "vietnamese": "Thai ngoài tử cung",
        "hanja": "子宮外妊娠",
        "hanjaReading": "子(아들 자) + 宮(집 궁) + 外(밖 외) + 妊(아이 밸 임) + 娠(아이 밸 신)",
        "pronunciation": "자궁외임신",
        "meaningKo": "수정란이 자궁이 아닌 다른 곳(주로 나팔관)에 착상하는 비정상 임신. 응급 수술이 필요한 위험한 상태로, 파열 시 대량 출혈로 생명이 위험할 수 있음. 통역 시 '외임신'과 '자궁외임신'을 구분 없이 사용하며, 즉각적인 치료의 필요성을 강조해야 함. 환자의 충격을 고려하되 긴급성을 정확히 전달하는 것이 중요.",
        "meaningVi": "Thai làm tổ ngoài tử cung, thường là trong vòi trứng. Đây là tình trạng nguy hiểm cần phẫu thuật khẩn cấp vì có thể vỡ gây chảy máu nội nhiều đe dọa tính mạng. Không thể tiếp tục thai kỳ và cần can thiệp y tế ngay.",
        "context": "응급 산부인과, 초음파 검사, 수술",
        "culturalNote": "한국과 베트남 모두 자궁외임신을 응급 상황으로 인식하나, 베트남 일부 지역에서는 복통을 가볍게 여겨 대응이 늦을 수 있음. 양국 모두 임신 가능성이 있는 가임기 여성의 복통은 자궁외임신을 의심해야 함. 통역 시 환자가 '유산'과 혼동하지 않도록 명확히 설명하고, 향후 임신 가능성에 대한 불안도 함께 다뤄야 함.",
        "commonMistakes": [
            {
                "mistake": "thai lạc chỗ (위치 이상)",
                "correction": "thai ngoài tử cung (자궁외임신)",
                "explanation": "'lạc chỗ'는 모호한 표현으로 정확한 의학 용어 사용 필요"
            },
            {
                "mistake": "자궁외임신을 '유산'으로 설명",
                "correction": "유산(sảy thai)과 자궁외임신(thai ngoài tử cung)은 다른 개념",
                "explanation": "자궁외임신은 비정상 착상으로 유산과는 원인과 치료가 다름"
            },
            {
                "mistake": "응급성을 축소하여 '나중에 병원 가세요'로 통역",
                "correction": "'즉시 응급실로 가야 합니다'로 긴급성 전달",
                "explanation": "파열 시 생명 위협이므로 즉각적인 조치 필요성 강조"
            }
        ],
        "examples": [
            {
                "ko": "초음파 결과 자궁외임신으로 확인되어 응급 수술이 필요합니다.",
                "vi": "Kết quả siêu âm xác định thai ngoài tử cung, cần phẫu thuật cấp cứu.",
                "situation": "formal"
            },
            {
                "ko": "한쪽 배가 심하게 아프고 출혈이 있나요?",
                "vi": "Một bên bụng đau dữ dội và có chảy máu không ạ?",
                "situation": "onsite"
            },
            {
                "ko": "자궁외임신으로 수술받았어요.",
                "vi": "Bị thai ngoài tử cung nên phải mổ.",
                "situation": "informal"
            }
        ],
        "relatedTerms": ["나팔관", "복강경수술", "응급수술", "유산"]
    },
    {
        "slug": "tram-cam-sau-sinh",
        "korean": "산후우울증",
        "vietnamese": "Trầm cảm sau sinh",
        "hanja": "産後憂鬱症",
        "hanjaReading": "産(낳을 산) + 後(뒤 후) + 憂(근심 우) + 鬱(답답할 울) + 症(병 증)",
        "pronunciation": "산후우울증",
        "meaningKo": "출산 후 발생하는 우울증으로, 단순 산후우울감(baby blues)보다 심각하고 장기적인 상태. 치료가 필요하며, 방치 시 모자 관계와 가족에게 심각한 영향을 미칠 수 있음. 통역 시 '산후조리 부족'이나 '나약함'으로 오해되지 않도록 의학적 질환임을 강조해야 함. 베트남에서는 정신질환에 대한 편견이 있어 환자가 증상을 숨길 수 있으므로 세심한 통역 필요.",
        "meaningVi": "Bệnh trầm cảm xảy ra sau khi sinh con, nghiêm trọng hơn tình trạng buồn bã nhẹ sau sinh (baby blues). Cần được điều trị bằng tâm lý trị liệu hoặc thuốc. Nếu không được chăm sóc, có thể ảnh hưởng nghiêm trọng đến mối quan hệ mẹ - bé và gia đình.",
        "context": "산부인과 산후 검진, 정신건강의학과 협진",
        "culturalNote": "한국에서는 산후우울증에 대한 인식이 높아지고 있으나 여전히 '산후조리 실패'로 치부하는 경향. 베트남은 정신질환에 대한 편견이 강해 치료를 꺼리는 경우 많음. 양국 모두 '나약함'이나 '의지 부족'으로 오해받기 쉬움. 통역 시 이것이 의학적 질환이며 치료 가능함을 강조하고, 가족의 이해와 지원이 중요함을 전달해야 함.",
        "commonMistakes": [
            {
                "mistake": "buồn sau sinh (산후 슬픔)",
                "correction": "trầm cảm sau sinh (산후우울증)",
                "explanation": "일시적 감정과 의학적 우울증을 구분해야 함"
            },
            {
                "mistake": "산후우울감(baby blues)과 산후우울증을 구분하지 않음",
                "correction": "baby blues는 2주 이내 자연 호전, 산후우울증은 치료 필요",
                "explanation": "기간과 심각도, 치료 필요성이 다른 별개 개념"
            },
            {
                "mistake": "환자에게 '마음을 강하게 먹으라'는 식으로 통역",
                "correction": "의학적 치료가 필요한 질환임을 명확히 전달",
                "explanation": "정신질환을 의지 문제로 치부하는 것은 위험한 오해"
            }
        ],
        "examples": [
            {
                "ko": "산후우울증으로 진단되어 약물 치료를 시작하겠습니다.",
                "vi": "Chẩn đoán trầm cảm sau sinh, sẽ bắt đầu điều trị bằng thuốc.",
                "situation": "formal"
            },
            {
                "ko": "아기가 귀여워 보이지 않고 돌보기 싫으신가요?",
                "vi": "Chị không thấy bé đáng yêu và không muốn chăm sóc bé phải không ạ?",
                "situation": "onsite"
            },
            {
                "ko": "산후우울증 때문에 약 먹고 있어요.",
                "vi": "Đang uống thuốc vì bị trầm cảm sau sinh.",
                "situation": "informal"
            }
        ],
        "relatedTerms": ["산후조리", "산후우울감", "정신건강", "상담치료"]
    },
    {
        "slug": "u-xo-tu-cung",
        "korean": "자궁근종",
        "vietnamese": "U xơ tử cung",
        "hanja": "子宮筋腫",
        "hanjaReading": "子(아들 자) + 宮(집 궁) + 筋(힘줄 근) + 腫(부을 종)",
        "pronunciation": "자궁근종",
        "meaningKo": "자궁 근육층에 생기는 양성 종양. 대부분 양성이나 크기와 위치에 따라 증상과 치료 방법이 다름. 통역 시 '종양'이라는 단어가 환자에게 공포를 줄 수 있으므로 '양성'임을 강조하되, 증상에 따라 치료가 필요함을 명확히 전달. 베트남어로 'u xơ tử cung'이며, 암과의 차이를 분명히 설명해야 함.",
        "meaningVi": "Khối u lành tính phát triển trong lớp cơ tử cung. Phần lớn là lành tính nhưng tùy theo kích thước và vị trí có thể gây ra các triệu chứng như đau bụng, kinh nguyệt nhiều. Có thể cần theo dõi hoặc điều trị tùy từng trường hợp.",
        "context": "산부인과 검진, 초음파 검사, 수술 상담",
        "culturalNote": "한국 여성의 20-30%가 자궁근종을 가지고 있으며 흔한 질환으로 인식. 베트남도 유사하나 정기 검진 부족으로 큰 근종이 된 후 발견되는 경우 많음. 양국 모두 '종양'이라는 말에 암을 연상하므로 통역 시 양성임을 먼저 강조. 치료 방법(경과 관찰, 약물, 수술)에 대한 선택권을 명확히 전달 필요.",
        "commonMistakes": [
            {
                "mistake": "u tử cung (자궁 종양)",
                "correction": "u xơ tử cung (자궁근종)",
                "explanation": "'u tử cung'은 모든 자궁 종양을 포함하므로 악성과 혼동 가능. 정확한 진단명 사용"
            },
            {
                "mistake": "종양을 '암'으로 오해하도록 통역",
                "correction": "'양성 종양'임을 명확히 강조",
                "explanation": "환자의 불필요한 공포를 방지하기 위해 양성임을 먼저 전달"
            },
            {
                "mistake": "모든 근종에 수술이 필요하다고 설명",
                "correction": "크기와 증상에 따라 경과 관찰도 가능함을 설명",
                "explanation": "과잉 치료 우려를 방지하고 환자의 선택권 보장"
            }
        ],
        "examples": [
            {
                "ko": "초음파에서 3cm 크기의 자궁근종이 발견되었습니다.",
                "vi": "Siêu âm phát hiện u xơ tử cung kích thước 3cm.",
                "situation": "formal"
            },
            {
                "ko": "생리량이 많고 생리통이 심한가요?",
                "vi": "Kinh nguyệt nhiều và đau bụng kinh nhiều không ạ?",
                "situation": "onsite"
            },
            {
                "ko": "자궁근종 있는데 아직 작아서 지켜보고 있어요.",
                "vi": "Có u xơ tử cung nhưng còn nhỏ nên đang theo dõi.",
                "situation": "informal"
            }
        ],
        "relatedTerms": ["양성종양", "자궁적출술", "생리과다", "초음파"]
    },
    {
        "slug": "u-nang-buong-trung",
        "korean": "난소낭종",
        "vietnamese": "U nang buồng trứng",
        "hanja": "卵巢囊腫",
        "hanjaReading": "卵(알 란) + 巢(집 소) + 囊(주머니 낭) + 腫(부을 종)",
        "pronunciation": "난소낭종",
        "meaningKo": "난소에 생기는 물혹. 대부분 양성이며 자연 소실되는 경우가 많으나, 크기가 크거나 증상이 있으면 치료 필요. 통역 시 '낭종'과 '종양'의 차이를 명확히 하고, 대부분 양성이며 경과 관찰이 가능함을 설명해야 함. 베트남어로 'u nang buồng trứng'이며, 정기 추적 검사의 중요성을 강조.",
        "meaningVi": "Túi chứa dịch phát sinh ở buồng trứng. Phần lớn là lành tính và có thể tự tiêu đi sau vài chu kỳ kinh. Tuy nhiên cần theo dõi định kỳ và nếu to hoặc có triệu chứng thì cần điều trị. Hiếm khi có nguy cơ xoắn cuống hoặc vỡ.",
        "context": "산부인과 검진, 초음파 검사, 복통 진단",
        "culturalNote": "한국에서는 정기 검진으로 조기 발견이 많으나, 베트남은 증상이 심해진 후 발견되는 경우 많음. 양국 모두 가임기 여성에게 흔하며, '낭종'이라는 용어에 불안해하는 경향. 통역 시 대부분 저절로 없어질 수 있다는 점을 강조하되, 정기 검사의 필요성도 함께 전달. 드물게 발생하는 응급 상황(난소 염전)에 대한 설명도 필요.",
        "commonMistakes": [
            {
                "mistake": "u buồng trứng (난소 종양)",
                "correction": "u nang buồng trứng (난소낭종)",
                "explanation": "'u nang'(낭종)과 'u'(종양)은 다른 개념으로 구분 필요"
            },
            {
                "mistake": "모든 낭종을 즉시 수술해야 한다고 설명",
                "correction": "크기와 종류에 따라 경과 관찰 가능함을 설명",
                "explanation": "기능성 낭종은 자연 소실되므로 과잉 치료 방지"
            },
            {
                "mistake": "난소 염전(xoắn cuống buồng trứng)과 혼동",
                "correction": "낭종과 염전은 다른 개념으로 구분",
                "explanation": "염전은 낭종의 합병증으로 응급 상황임"
            }
        ],
        "examples": [
            {
                "ko": "5cm 난소낭종이 있어 3개월 후 재검사가 필요합니다.",
                "vi": "Có u nang buồng trứng 5cm, cần tái khám sau 3 tháng.",
                "situation": "formal"
            },
            {
                "ko": "한쪽 아랫배가 갑자기 심하게 아프신가요?",
                "vi": "Một bên bụng dưới đột ngột đau dữ dội phải không ạ?",
                "situation": "onsite"
            },
            {
                "ko": "난소낭종 있었는데 저절로 없어졌어요.",
                "vi": "Có u nang buồng trứng nhưng tự hết rồi.",
                "situation": "informal"
            }
        ],
        "relatedTerms": ["난소", "초음파", "복강경수술", "난소염전"]
    },
    {
        "slug": "lac-noi-mac-tu-cung",
        "korean": "자궁내막증",
        "vietnamese": "Lạc nội mạc tử cung",
        "hanja": "子宮內膜症",
        "hanjaReading": "子(아들 자) + 宮(집 궁) + 內(안 내) + 膜(막 막) + 症(병 증)",
        "pronunciation": "자궁내막증",
        "meaningKo": "자궁내막 조직이 자궁 밖의 다른 장기에 자라는 질환. 생리통, 만성 골반통, 불임의 원인이 될 수 있음. 통역 시 '자궁내막증'과 '자궁선근증'을 구분하고, 만성 질환으로 장기 관리가 필요함을 설명해야 함. 베트남어로 'lạc nội mạc tử cung'이며, 통증 관리와 임신 계획에 미치는 영향을 명확히 전달 필요.",
        "meaningVi": "Bệnh lý mà mô nội mạc tử cung mọc ở ngoài tử cung, thường ở buồng trứng, vòi trứng, ổ bụng. Gây đau bụng kinh nghiêm trọng, đau mạn tính vùng chậu và có thể dẫn đến vô sinh. Cần điều trị dài hạn và theo dõi thường xuyên.",
        "context": "산부인과 진료, 불임 클리닉, 통증 관리",
        "culturalNote": "한국에서는 인식이 높아지고 있으나 진단까지 시간이 오래 걸리는 경우 많음. 베트남은 생리통을 '정상'으로 여겨 진단이 더 늦어지는 경향. 양국 모두 여성들이 통증을 참고 넘기는 문화가 있어, 통역 시 '심한 생리통은 정상이 아니다'는 인식 개선 필요. 불임과의 연관성 때문에 환자의 심리적 부담이 크므로 세심한 배려 필요.",
        "commonMistakes": [
            {
                "mistake": "viêm nội mạc tử cung (자궁내막염)",
                "correction": "lạc nội mạc tử cung (자궁내막증)",
                "explanation": "염증(viêm)과 조직 이소(lạc)는 완전히 다른 질환"
            },
            {
                "mistake": "자궁선근증(u tuyến tử cung)과 혼동",
                "correction": "자궁내막증(lạc nội mạc)과 자궁선근증(u tuyến)은 별개 질환",
                "explanation": "병변 위치와 치료가 다르므로 정확한 구분 필요"
            },
            {
                "mistake": "생리통을 '참으라'고 통역",
                "correction": "심한 생리통은 치료가 필요한 증상임을 전달",
                "explanation": "질환 진단과 치료 지연을 방지하기 위해 증상의 심각성 인식 필요"
            }
        ],
        "examples": [
            {
                "ko": "자궁내막증으로 진단되어 호르몬 치료를 시작하겠습니다.",
                "vi": "Chẩn đoán lạc nội mạc tử cung, sẽ bắt đầu điều trị hormone.",
                "situation": "formal"
            },
            {
                "ko": "생리 때마다 너무 아파서 일상생활이 어려우신가요?",
                "vi": "Mỗi lần có kinh đau quá không thể sinh hoạt bình thường phải không ạ?",
                "situation": "onsite"
            },
            {
                "ko": "자궁내막증 때문에 임신이 어렵대요.",
                "vi": "Vì lạc nội mạc tử cung nên khó có thai.",
                "situation": "informal"
            }
        ],
        "relatedTerms": ["생리통", "불임", "복강경수술", "호르몬치료"]
    },
    {
        "slug": "vo-sinh",
        "korean": "불임",
        "vietnamese": "Vô sinh",
        "hanja": "不姙",
        "hanjaReading": "不(아니 불) + 姙(아이 밸 임)",
        "pronunciation": "불임",
        "meaningKo": "정상적인 성생활에도 불구하고 1년 이상 임신이 되지 않는 상태. 남성과 여성 모두에게 원인이 있을 수 있으며, 정확한 진단과 치료 필요. 통역 시 '불임'과 '난임'의 차이를 이해하고, 환자의 심리적 부담을 고려한 표현 사용 필요. 베트남어로 'vô sinh'이며, 부부 모두 검사가 필요함을 명확히 전달.",
        "meaningVi": "Tình trạng không thể có thai sau 1 năm quan hệ tình dục đều đặn không sử dụng biện pháp tránh thai. Nguyên nhân có thể từ phía nam hoặc nữ, cần kiểm tra và điều trị cho cả hai vợ chồng. Có nhiều phương pháp hỗ trợ sinh sản hiện đại.",
        "context": "불임 클리닉, 산부인과 상담, 비뇨기과",
        "culturalNote": "한국에서는 '불임'보다 '난임'이라는 용어를 선호하는 추세이나 베트남은 'vô sinh'이 표준. 양국 모두 불임에 대한 사회적 압박이 크며, 특히 여성에게 책임을 돌리는 경향. 통역 시 남성 요인도 50%임을 명확히 하고, 부부가 함께 검사받아야 함을 강조. 환자의 정서적 스트레스를 고려한 공감적 통역 필요.",
        "commonMistakes": [
            {
                "mistake": "hiếm muộn (난임)",
                "correction": "vô sinh (불임)",
                "explanation": "한국은 '난임'을 선호하나 베트남은 'vô sinh'이 의학 용어"
            },
            {
                "mistake": "불임을 여성만의 문제로 통역",
                "correction": "남성과 여성 모두 원인이 될 수 있음을 명확히 전달",
                "explanation": "남성 요인이 약 40-50%이므로 부부 모두 검사 필요"
            },
            {
                "mistake": "vô sinh (완전 불가능)과 khó có con (어려움)을 구분하지 않음",
                "correction": "의학적으로는 vô sinh 사용하되 환자에게는 완화된 표현도 병행",
                "explanation": "환자의 심리적 부담을 고려한 표현 선택 필요"
            }
        ],
        "examples": [
            {
                "ko": "불임 검사를 위해 부부가 함께 오셔야 합니다.",
                "vi": "Để kiểm tra vô sinh, vợ chồng cần đến cùng nhau.",
                "situation": "formal"
            },
            {
                "ko": "결혼한 지 얼마나 되셨고, 피임 안 하신 지는 얼마나 되셨나요?",
                "vi": "Kết hôn được bao lâu và không tránh thai được bao lâu rồi ạ?",
                "situation": "onsite"
            },
            {
                "ko": "불임 때문에 시험관 준비 중이에요.",
                "vi": "Vì vô sinh nên đang chuẩn bị thụ tinh ống nghiệm.",
                "situation": "informal"
            }
        ],
        "relatedTerms": ["시험관시술", "배란유도", "정자검사", "난임"]
    },
    {
        "slug": "thu-tinh-ong-nghiem",
        "korean": "시험관시술",
        "vietnamese": "Thụ tinh ống nghiệm",
        "hanja": "試驗管施術",
        "hanjaReading": "試(시험할 시) + 驗(시험할 험) + 管(대롱 관) + 施(베풀 시) + 術(재주 술)",
        "pronunciation": "시험관시술",
        "meaningKo": "체외에서 난자와 정자를 수정시킨 후 배아를 자궁에 이식하는 보조생식술. IVF(In Vitro Fertilization)라고도 함. 통역 시 시술 과정, 성공률, 비용, 부작용 등을 명확히 전달해야 하며, 환자의 기대와 불안을 함께 다뤄야 함. 베트남어로 'thụ tinh ống nghiệm' 또는 'IVF'로 표현.",
        "meaningVi": "Phương pháp hỗ trợ sinh sản bằng cách thụ tinh trứng và tinh trùng bên ngoài cơ thể, sau đó cấy phôi vào tử cung. Còn gọi là IVF. Quy trình phức tạp, tốn kém nhưng mang lại cơ hội có con cho các cặp vợ chồng vô sinh. Tỷ lệ thành công phụ thuộc nhiều yếu tố.",
        "context": "불임 클리닉, 보조생식술 상담",
        "culturalNote": "한국은 정부 지원으로 시험관 시술 접근성이 높으나 베트남은 비용 부담이 큼. 양국 모두 사회적 압박과 경제적 부담으로 스트레스가 큼. 한국은 여러 차례 시도가 흔하나 베트남은 1-2회가 일반적. 통역 시 성공률이 100%가 아님을 명확히 하고, 실패 시 환자의 심리적 충격을 고려한 표현 사용 필요.",
        "commonMistakes": [
            {
                "mistake": "thụ tinh nhân tạo (인공수정)",
                "correction": "thụ tinh ống nghiệm (시험관) vs thụ tinh nhân tạo (인공수정)",
                "explanation": "인공수정(IUI)과 시험관(IVF)은 다른 시술로 구분 필요"
            },
            {
                "mistake": "100% 성공한다고 설명",
                "correction": "성공률은 연령과 조건에 따라 다름을 명확히 전달",
                "explanation": "과도한 기대를 방지하고 현실적 정보 제공 필요"
            },
            {
                "mistake": "IVF를 베트남어로 음역하지 않음",
                "correction": "IVF 또는 thụ tinh ống nghiệm 병기",
                "explanation": "의료진은 IVF 사용하나 환자는 베트남어 용어가 더 이해하기 쉬움"
            }
        ],
        "examples": [
            {
                "ko": "시험관 시술 성공률은 연령에 따라 30-40% 정도입니다.",
                "vi": "Tỷ lệ thành công thụ tinh ống nghiệm tùy tuổi khoảng 30-40%.",
                "situation": "formal"
            },
            {
                "ko": "난자 채취는 좀 불편하지만 금방 끝나요.",
                "vi": "Lấy trứng hơi khó chịu nhưng nhanh thôi ạ.",
                "situation": "onsite"
            },
            {
                "ko": "세 번째 시험관에서 성공했어요.",
                "vi": "Lần thứ ba thụ tinh ống nghiệm mới thành công.",
                "situation": "informal"
            }
        ],
        "relatedTerms": ["불임", "배아이식", "난자채취", "인공수정"]
    },
    {
        "slug": "nuoi-con-bang-sua-me",
        "korean": "모유수유",
        "vietnamese": "Nuôi con bằng sữa mẹ",
        "hanja": "母乳授乳",
        "hanjaReading": "母(어미 모) + 乳(젖 유) + 授(줄 수) + 乳(젖 유)",
        "pronunciation": "모유수유",
        "meaningKo": "엄마의 젖으로 아기를 먹이는 것. WHO는 생후 6개월까지 완전 모유수유를 권장함. 통역 시 모유수유의 장점과 어려움을 균형있게 전달하고, 산모가 죄책감을 느끼지 않도록 주의해야 함. 베트남어로 'nuôi con bằng sữa mẹ' 또는 간단히 'cho con bú'로 표현.",
        "meaningVi": "Cho trẻ bú sữa mẹ. WHO khuyến nghị cho con bú sữa mẹ hoàn toàn trong 6 tháng đầu. Sữa mẹ cung cấp đầy đủ dinh dưỡng và kháng thể cho bé. Tuy nhiên mỗi bà mẹ có hoàn cảnh khác nhau, không nên áp đặt.",
        "context": "산부인과 산후 교육, 소아과 상담",
        "culturalNote": "한국과 베트남 모두 모유수유를 강조하나 직장 복귀 등 현실적 어려움 많음. 한국은 '완모(완전 모유수유)'에 대한 압박이 크고, 베트남은 전통적으로 모유수유 비율이 높으나 도시에서는 감소 추세. 통역 시 모유수유의 장점을 전달하되 분유 사용을 비난하지 않는 균형잡힌 태도 필요. 유두 통증, 유선염 등 문제 발생 시 적극적 도움 요청 권장.",
        "commonMistakes": [
            {
                "mistake": "cho bú (단순히 수유)",
                "correction": "nuôi con bằng sữa mẹ (모유수유) vs cho bú sữa bột (분유수유)",
                "explanation": "'cho bú'만으로는 모유인지 분유인지 불명확"
            },
            {
                "mistake": "모유수유를 강요하는 듯한 통역",
                "correction": "권장하되 산모의 상황을 고려한 선택임을 전달",
                "explanation": "모유수유 실패 시 죄책감을 주지 않도록 주의"
            },
            {
                "mistake": "유두 통증을 '참으라'고 통역",
                "correction": "통증은 비정상이므로 자세 교정이나 도움 필요함을 전달",
                "explanation": "잘못된 수유 자세로 인한 문제를 방치하지 않도록"
            }
        ],
        "examples": [
            {
                "ko": "생후 6개월까지는 모유만으로 충분합니다.",
                "vi": "Đến 6 tháng tuổi chỉ cần sữa mẹ là đủ.",
                "situation": "formal"
            },
            {
                "ko": "젖이 잘 안 나오면 자주 물리세요.",
                "vi": "Nếu sữa ít thì cho bú thường xuyên ạ.",
                "situation": "onsite"
            },
            {
                "ko": "완모로 1년 먹였어요.",
                "vi": "Nuôi hoàn toàn bằng sữa mẹ đến 1 tuổi.",
                "situation": "informal"
            }
        ],
        "relatedTerms": ["유선염", "젖몸살", "이유식", "분유"]
    },
    {
        "slug": "vang-da-so-sinh",
        "korean": "신생아황달",
        "vietnamese": "Vàng da sơ sinh",
        "hanja": "新生兒黃疸",
        "hanjaReading": "新(새 신) + 生(날 생) + 兒(아이 아) + 黃(누를 황) + 疸(황달 달)",
        "pronunciation": "신생아황달",
        "meaningKo": "생후 며칠 내 신생아의 피부와 눈이 노랗게 변하는 증상. 대부분 생리적 황달로 자연 호전되나, 병적 황달은 치료 필요. 통역 시 '정상 범위의 황달'과 '치료가 필요한 황달'을 구분하여 설명하고, 부모의 불안을 완화하면서도 광선치료의 필요성을 명확히 전달. 베트남어로 'vàng da sơ sinh'.",
        "meaningVi": "Tình trạng da và mắt trẻ sơ sinh chuyển vàng trong những ngày đầu sau sinh do bilirubin tăng cao. Phần lớn là vàng da sinh lý tự khỏi, nhưng vàng da bệnh lý cần điều trị bằng đèn chiếu. Cần theo dõi chỉ số bilirubin để quyết định điều trị.",
        "context": "소아과, 신생아실, 산후 조리",
        "culturalNote": "한국과 베트남 모두 신생아 황달이 흔하며, 대부분 정상으로 인식. 그러나 심한 황달 방치 시 핵황달로 뇌손상 가능하므로 주의 필요. 한국은 퇴원 전 황달 검사가 일반적이나 베트남은 시설에 따라 다름. 통역 시 '햇빛 쐬기'만으로는 부족하며 필요 시 광선치료가 필요함을 명확히 전달. 수유와의 관계(모유황달)도 설명 필요.",
        "commonMistakes": [
            {
                "mistake": "vàng da (일반 황달)",
                "correction": "vàng da sơ sinh (신생아황달)",
                "explanation": "성인 황달과 신생아 황달은 원인과 치료가 다름"
            },
            {
                "mistake": "모든 황달을 '정상'으로 안심시킴",
                "correction": "수치와 시기에 따라 치료 필요 여부 구분",
                "explanation": "병적 황달 놓치면 뇌손상 위험 있으므로 정확한 평가 필요"
            },
            {
                "mistake": "광선치료를 đèn sưởi (난방등)로 오역",
                "correction": "đèn chiếu điều trị vàng da (황달 치료용 광선)",
                "explanation": "일반 램프와 의료용 광선치료 구분 필요"
            }
        ],
        "examples": [
            {
                "ko": "빌리루빈 수치가 높아 광선치료가 필요합니다.",
                "vi": "Chỉ số bilirubin cao cần điều trị bằng đèn chiếu.",
                "situation": "formal"
            },
            {
                "ko": "아기 피부가 노래 보이는데 언제부터 그랬나요?",
                "vi": "Da bé vàng từ khi nào vậy ạ?",
                "situation": "onsite"
            },
            {
                "ko": "신생아 황달로 하루 더 입원했어요.",
                "vi": "Vì vàng da sơ sinh nên phải nằm viện thêm một ngày.",
                "situation": "informal"
            }
        ],
        "relatedTerms": ["빌리루빈", "광선치료", "모유황달", "핵황달"]
    },
    {
        "slug": "tre-sinh-non",
        "korean": "미숙아",
        "vietnamese": "Trẻ sinh non",
        "hanja": "未熟兒",
        "hanjaReading": "未(아닐 미) + 熟(익을 숙) + 兒(아이 아)",
        "pronunciation": "미숙아",
        "meaningKo": "임신 37주 이전에 태어난 아기. 장기가 미성숙하여 특별한 관리가 필요하며, 호흡곤란, 체온조절 문제 등 합병증 위험이 높음. 통역 시 '미숙아'라는 용어가 부정적으로 들릴 수 있으므로 '조산아'로도 표현하며, 장기 추적 관찰의 중요성을 강조. 베트남어로 'trẻ sinh non' 또는 'trẻ đẻ non'.",
        "meaningVi": "Trẻ sinh ra trước tuần thai thứ 37. Các cơ quan chưa phát triển hoàn chỉnh nên cần chăm sóc đặc biệt, có nguy cơ khó thở, khó giữ nhiệt độ cơ thể. Cần theo dõi sát sao và có thể phải nằm lồng kính (incubator). Cần khám định kỳ dài hạn.",
        "context": "신생아 중환자실, 소아과 추적 관찰",
        "culturalNote": "한국과 베트남 모두 미숙아 생존율이 향상되었으나 베트남 시골은 신생아 중환자실 부족. 한국은 미숙아 지원 제도가 있으나 베트남은 가족 부담이 큼. 양국 모두 미숙아 부모의 죄책감과 경제적 부담이 큼. 통역 시 현재의 의학 발전으로 좋은 예후 가능함을 전달하되, 현실적인 어려움도 함께 설명. 발달 지연 가능성과 조기 개입의 중요성 강조.",
        "commonMistakes": [
            {
                "mistake": "trẻ yếu (약한 아기)",
                "correction": "trẻ sinh non (미숙아)",
                "explanation": "'yếu'는 일반적 표현으로 의학 용어로는 부적절"
            },
            {
                "mistake": "인큐베이터를 lồng (새장)으로 번역",
                "correction": "lồng kính hoặc máy ấp (인큐베이터)",
                "explanation": "'lồng'만으로는 부정적 의미로 들릴 수 있음"
            },
            {
                "mistake": "미숙아를 '문제아'처럼 통역",
                "correction": "조금 일찍 태어난 아기로 특별 관리 필요한 것으로 설명",
                "explanation": "부모의 죄책감을 줄이고 긍정적 전망 제시"
            }
        ],
        "examples": [
            {
                "ko": "34주에 태어나 인큐베이터에서 관리가 필요합니다.",
                "vi": "Sinh ở tuần 34 nên cần chăm sóc trong lồng kính.",
                "situation": "formal"
            },
            {
                "ko": "호흡이 약해서 산소 치료 중입니다.",
                "vi": "Hô hấp yếu nên đang điều trị oxy.",
                "situation": "onsite"
            },
            {
                "ko": "32주에 태어나서 한 달 입원했어요.",
                "vi": "Sinh ở tuần 32 nên nằm viện một tháng.",
                "situation": "informal"
            }
        ],
        "relatedTerms": ["조산", "인큐베이터", "신생아중환자실", "호흡곤란"]
    },
    {
        "slug": "tiem-chung",
        "korean": "예방접종",
        "vietnamese": "Tiêm chủng",
        "hanja": "豫防接種",
        "hanjaReading": "豫(미리 예) + 防(막을 방) + 接(이을 접) + 種(씨 종)",
        "pronunciation": "예방접종",
        "meaningKo": "질병을 예방하기 위해 백신을 접종하는 것. 영유아 필수 예방접종과 선택 예방접종이 있으며, 접종 일정 준수가 중요함. 통역 시 한국과 베트남의 접종 일정 차이를 설명하고, 부작용과 대처 방법을 명확히 전달. 베트남어로 'tiêm chủng' 또는 'tiêm phòng'이며, 백신 종류별 정확한 명칭 숙지 필요.",
        "meaningVi": "Tiêm vaccine để phòng bệnh. Có tiêm chủng bắt buộc và tự nguyện cho trẻ em. Cần tuân thủ lịch tiêm để đảm bảo hiệu quả. Sau tiêm có thể có phản ứng phụ nhẹ như sốt, đau chỗ tiêm. Cần theo dõi trẻ sau tiêm và báo bác sĩ nếu có phản ứng bất thường.",
        "context": "소아과, 보건소, 건강검진",
        "culturalNote": "한국은 국가 예방접종이 무료이며 일정이 체계적. 베트남도 기본 백신은 무료나 선택 백신은 비용 부담. 양국 모두 백신 거부 운동은 적으나, 부작용에 대한 우려 있음. 통역 시 한국에서 접종한 기록을 베트남에서 인정받을 수 있는지, 누락된 백신은 없는지 확인 필요. 부작용 발생 시 대처법과 응급 상황 판단 기준 명확히 전달.",
        "commonMistakes": [
            {
                "mistake": "tiêm (단순 주사)",
                "correction": "tiêm chủng 또는 tiêm phòng (예방접종)",
                "explanation": "'tiêm'만으로는 일반 주사와 구분 안 됨"
            },
            {
                "mistake": "백신 이름을 한국어 발음으로 음역",
                "correction": "국제 표준 명칭 또는 베트남어 명칭 사용 (예: BCG, MMR 등)",
                "explanation": "백신은 국제 약어가 통용되거나 베트남 고유 명칭 있음"
            },
            {
                "mistake": "부작용을 '없다'고 단정",
                "correction": "경미한 부작용(발열, 통증)은 정상 반응임을 설명",
                "explanation": "예상 가능한 반응과 응급 상황 구분하여 설명 필요"
            }
        ],
        "examples": [
            {
                "ko": "생후 2개월에 DTaP, 소아마비 등 기본 접종을 받습니다.",
                "vi": "Lúc 2 tháng tuổi sẽ tiêm chủng cơ bản như DTaP, bại liệt.",
                "situation": "formal"
            },
            {
                "ko": "접종 후 열이 나면 해열제 드리고 하루 지켜보세요.",
                "vi": "Sau tiêm nếu sốt thì cho uống thuốc hạ sốt và theo dõi một ngày.",
                "situation": "onsite"
            },
            {
                "ko": "오늘 예방접종 맞았어요.",
                "vi": "Hôm nay đi tiêm chủng rồi.",
                "situation": "informal"
            }
        ],
        "relatedTerms": ["백신", "부작용", "접종일정", "건강검진"]
    },
    {
        "slug": "co-giat-do-sot",
        "korean": "소아열성경련",
        "vietnamese": "Co giật do sốt",
        "hanja": "小兒熱性痙攣",
        "hanjaReading": "小(작을 소) + 兒(아이 아) + 熱(더울 열) + 性(성품 성) + 痙(경련 경) + 攣(오그라들 련)",
        "pronunciation": "소아열성경련",
        "meaningKo": "고열 시 소아에게 나타나는 경련. 대부분 양성이며 후유증 없이 회복되나, 처음 보는 부모는 매우 놀람. 통역 시 당황하지 말고 안전 조치(옆으로 눕히기, 질식 방지)를 명확히 전달하고, 응급실 방문 필요성을 설명. 베트남어로 'co giật do sốt'이며, 간질과는 다름을 강조.",
        "meaningVi": "Co giật xảy ra khi trẻ bị sốt cao. Phần lớn là lành tính và không để lại di chứng, nhưng rất đáng sợ với cha mẹ. Cần đặt trẻ nằm nghiêng, không cho gì vào miệng, gọi cấp cứu nếu lần đầu hoặc co giật kéo dài. Khác với động kinh.",
        "context": "응급실, 소아과, 열 관리 교육",
        "culturalNote": "한국과 베트남 모두 열성경련을 간질(동kinh)과 혼동하여 공포를 느낌. 실제로는 5세 미만 어린이의 2-5%가 경험하는 흔한 증상. 통역 시 부모의 극심한 불안을 이해하고 침착하게 대처법을 전달. '입에 수저 넣기' 같은 잘못된 민간요법을 하지 않도록 주의. 재발 가능성과 예방법(해열제 적극 사용) 설명 필요.",
        "commonMistakes": [
            {
                "mistake": "động kinh (간질)",
                "correction": "co giật do sốt (열성경련) - động kinh과는 다름",
                "explanation": "간질과 열성경련은 원인과 예후가 완전히 다르므로 명확히 구분"
            },
            {
                "mistake": "경련 시 입에 물건을 넣으라고 통역",
                "correction": "아무것도 입에 넣지 말고 옆으로 눕히라고 전달",
                "explanation": "잘못된 민간요법으로 질식이나 치아 손상 위험"
            },
            {
                "mistake": "열성경련을 '심각한 뇌 질환'으로 과장",
                "correction": "대부분 양성이며 성장하면 사라짐을 설명",
                "explanation": "과도한 공포를 주지 않되 적절한 대처는 필요함을 전달"
            }
        ],
        "examples": [
            {
                "ko": "열이 급격히 오르면서 경련이 있었다면 열성경련일 가능성이 높습니다.",
                "vi": "Nếu sốt cao đột ngột kèm co giật thì có thể là co giật do sốt.",
                "situation": "formal"
            },
            {
                "ko": "경련 시 옆으로 눕히고 입에 아무것도 넣지 마세요.",
                "vi": "Khi co giật, đặt bé nằm nghiêng và không cho gì vào miệng.",
                "situation": "onsite"
            },
            {
                "ko": "열성경련 한 번 있었는데 지금은 괜찮아요.",
                "vi": "Có một lần co giật do sốt nhưng bây giờ bình thường.",
                "situation": "informal"
            }
        ],
        "relatedTerms": ["고열", "경련", "해열제", "응급처치"]
    },
    {
        "slug": "benh-tay-chan-mieng",
        "korean": "수족구병",
        "vietnamese": "Bệnh tay chân miệng",
        "hanja": "手足口病",
        "hanjaReading": "手(손 수) + 足(발 족) + 口(입 구) + 病(병 병)",
        "pronunciation": "수족구병",
        "meaningKo": "손, 발, 입에 물집이 생기는 바이러스 감염병. 주로 영유아에게 발생하며 전염성이 강함. 대부분 경증이나 드물게 합병증 발생 가능. 통역 시 격리의 필요성, 전염 경로, 증상 완화 방법을 명확히 전달. 베트남어로 'bệnh tay chân miệng'이며, 어린이집/유치원 등원 중지 필요성 설명.",
        "meaningVi": "Bệnh nhiễm virus gây ra phỏng nước ở tay, chân, miệng. Chủ yếu ở trẻ nhỏ và rất dễ lây lan. Phần lớn nhẹ tự khỏi nhưng hiếm khi có biến chứng nguy hiểm. Cần cách ly trẻ, giữ vệ sinh, uống nhiều nước. Không nên đến trường/nhà trẻ cho đến khi hết bệnh.",
        "context": "소아과, 어린이집/유치원 보건",
        "culturalNote": "한국과 베트남 모두 어린이집에서 집단 발생 흔함. 한국은 등원 중지 규정이 엄격하나 베트남은 느슨한 편. 양국 모두 부모들이 '흔한 병'으로 가볍게 여기는 경향 있으나, 드물게 뇌수막염 등 합병증 발생 가능. 통역 시 전염성이 매우 강하므로 형제자매 간 격리도 필요함을 강조. 손씻기와 위생 관리의 중요성 전달.",
        "commonMistakes": [
            {
                "mistake": "bệnh nổi mụn nước (단순 물집 병)",
                "correction": "bệnh tay chân miệng (수족구병 정식 명칭)",
                "explanation": "정확한 질병명 사용으로 오해 방지"
            },
            {
                "mistake": "수두(thủy đậu)와 혼동",
                "correction": "수두와 수족구는 다른 병으로 발진 위치와 양상이 다름",
                "explanation": "수두는 전신, 수족구는 손발입에 국한"
            },
            {
                "mistake": "항생제가 필요하다고 설명",
                "correction": "바이러스 질환이므로 항생제 불필요, 대증치료만",
                "explanation": "불필요한 항생제 사용 방지"
            }
        ],
        "examples": [
            {
                "ko": "손과 발, 입 안에 물집이 있고 열이 나면 수족구병입니다.",
                "vi": "Nếu có phỏng nước ở tay, chân, trong miệng và sốt thì là bệnh tay chân miệng.",
                "situation": "formal"
            },
            {
                "ko": "입이 아파서 잘 못 먹으니까 시원한 음식 주세요.",
                "vi": "Miệng đau nên ăn khó, cho ăn đồ mát nhé.",
                "situation": "onsite"
            },
            {
                "ko": "수족구 걸려서 일주일 쉬었어요.",
                "vi": "Bị bệnh tay chân miệng nên nghỉ một tuần.",
                "situation": "informal"
            }
        ],
        "relatedTerms": ["전염병", "격리", "손씻기", "어린이집"]
    },
    {
        "slug": "kham-suc-khoe-tre-em",
        "korean": "영유아건강검진",
        "vietnamese": "Khám sức khỏe trẻ em",
        "hanja": "嬰幼兒健康檢診",
        "hanjaReading": "嬰(젖먹이 영) + 幼(어릴 유) + 兒(아이 아) + 健(건강할 건) + 康(편안할 강) + 檢(검사할 검) + 診(진찰할 진)",
        "pronunciation": "영유아건강검진",
        "meaningKo": "영유아의 성장 발달 상태를 정기적으로 확인하는 건강검진. 한국은 국가에서 무료로 제공하며, 월령별로 시기가 정해져 있음. 통역 시 검진 항목(신체 계측, 발달 평가, 상담)과 중요성을 설명하고, 놓치지 않도록 일정 관리 강조. 베트남어로 'khám sức khỏe trẻ em' 또는 'khám định kỳ'.",
        "meaningVi": "Khám sức khỏe định kỳ để theo dõi sự phát triển của trẻ nhỏ. Ở Hàn Quốc được cung cấp miễn phí bởi nhà nước theo lứa tuổi. Bao gồm đo chiều cao, cân nặng, đánh giá phát triển vận động, ngôn ngữ, tư vấn nuôi dưỡng. Rất quan trọng để phát hiện sớm vấn đề phát triển.",
        "context": "소아과, 보건소, 건강검진센터",
        "culturalNote": "한국은 국가 영유아 검진이 체계적으로 운영되나 베트남은 정기 검진 문화가 약함. 한국 거주 베트남인은 무료 검진 혜택을 모르는 경우 많음. 통역 시 무료이며 꼭 받아야 한다는 점 강조. 발달 지연 발견 시 조기 개입의 중요성과 지원 제도 안내. 검진표 지참과 예약 방법 등 실용 정보 제공.",
        "commonMistakes": [
            {
                "mistake": "khám bệnh (진료)",
                "correction": "khám sức khỏe 또는 khám định kỳ (건강검진)",
                "explanation": "'khám bệnh'는 아플 때 가는 것, 'khám sức khỏe'는 예방 검진"
            },
            {
                "mistake": "유료라고 오해",
                "correction": "한국 국가검진은 무료임을 명확히 전달",
                "explanation": "경제적 부담으로 검진을 포기하지 않도록"
            },
            {
                "mistake": "검진 시기를 '대충'으로 안내",
                "correction": "월령별 정해진 시기 있음을 명확히 전달",
                "explanation": "시기 놓치면 검진 기회 상실"
            }
        ],
        "examples": [
            {
                "ko": "생후 4개월, 9개월, 2세 등 정해진 시기에 검진을 받으셔야 합니다.",
                "vi": "Phải khám định kỳ vào các thời điểm quy định như 4 tháng, 9 tháng, 2 tuổi.",
                "situation": "formal"
            },
            {
                "ko": "키와 몸무게 재고 발달 상태 확인할게요.",
                "vi": "Sẽ đo chiều cao, cân nặng và kiểm tra phát triển nhé.",
                "situation": "onsite"
            },
            {
                "ko": "오늘 18개월 검진 받았어요.",
                "vi": "Hôm nay đi khám 18 tháng tuổi.",
                "situation": "informal"
            }
        ],
        "relatedTerms": ["성장곡선", "발달검사", "예방접종", "육아상담"]
    }
]

# Filter out duplicates
new_terms_filtered = [t for t in new_terms if t['slug'] not in existing_slugs]

print(f"⚠️  Filtered {len(new_terms) - len(new_terms_filtered)} duplicate(s)")
print(f"✅ Adding {len(new_terms_filtered)} new term(s)")

# Extend and save
data.extend(new_terms_filtered)

with open(file_path, 'w', encoding='utf-8') as f:
    json.dump(data, f, ensure_ascii=False, indent=2)

print(f"✅ Total terms in medical.json: {len(data)}")
print(f"📋 New terms added: {', '.join([t['korean'] for t in new_terms_filtered])}")
