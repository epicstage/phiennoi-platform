#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import json
import os

# Get absolute path to medical.json
file_path = os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', 'data', 'terms', 'medical.json')

# Read existing data
with open(file_path, 'r', encoding='utf-8') as f:
    data = json.load(f)

# New terms to add
new_terms = [
    {
        "id": "medical-occupational-accident",
        "slug": "tai-nan-lao-dong",
        "korean": "산업재해",
        "vietnamese": "Tai nạn lao động",
        "hanja": "産業災害",
        "hanjaReading": "産(낳을 산) + 業(업 업) + 災(재앙 재) + 害(해칠 해)",
        "pronunciation": "따이 난 라오 동",
        "meaningKo": "업무와 관련하여 발생하는 부상, 질병, 사망을 의미합니다. 통역 시 '산재'라는 축약형과 정식 용어를 구분하고, 베트남에서는 노동 허가서가 있는 근로자만 산재 보상을 받을 수 있다는 점을 유의해야 합니다. 한국은 산재보험 가입이 의무이지만 베트남은 고용주가 직접 보상하는 경우가 많아 통역 시 보험 제도 차이를 명확히 설명해야 합니다. 산업재해 인정 기준도 양국이 다를 수 있으므로 주의가 필요합니다.",
        "meaningVi": "Chấn thương, bệnh tật hoặc tử vong xảy ra liên quan đến công việc. Ở Việt Nam, chỉ người lao động có giấy phép lao động mới được hưởng bồi thường tai nạn lao động. Cần phân biệt rõ giữa tai nạn lao động (tai nạn khi làm việc) và tai nạn cá nhân (tai nạn ngoài giờ làm việc).",
        "context": "산업안전, 노동법, 보험",
        "culturalNote": "한국은 산재보험이 의무 가입 제도로 전국민건강보험공단에서 운영하지만, 베트남은 고용주가 직접 책임지는 경우가 많습니다. 한국에서는 출퇴근 재해도 산재로 인정되지만 베트남은 작업장 내 사고만 인정하는 경향이 있어 통역 시 이를 명확히 설명해야 합니다. 또한 한국은 정신적 스트레스로 인한 질병도 산재로 인정받을 수 있으나 베트남은 주로 물리적 부상만 인정합니다.",
        "commonMistakes": [
            {
                "mistake": "Tai nạn công nghiệp",
                "correction": "Tai nạn lao động",
                "explanation": "'공업 사고'가 아니라 '노동 재해'가 정확한 표현입니다"
            },
            {
                "mistake": "Bệnh công nhân",
                "correction": "Bệnh nghề nghiệp",
                "explanation": "산업재해는 사고(tai nạn)를, 직업병은 질병(bệnh)을 의미합니다"
            },
            {
                "mistake": "산재를 Tai nạn으로만 번역",
                "correction": "Tai nạn lao động (산업재해) 전체 표현 사용",
                "explanation": "Tai nạn만으로는 일반 사고와 구분이 안 됩니다"
            }
        ],
        "examples": [
            {
                "ko": "작업 중 추락 사고로 산업재해 신청을 했습니다",
                "vi": "Tôi đã nộp đơn yêu cầu bồi thường tai nạn lao động do bị ngã trong khi làm việc",
                "situation": "formal"
            },
            {
                "ko": "이 부상은 산재로 인정받을 수 있나요?",
                "vi": "Chấn thương này có được công nhận là tai nạn lao động không?",
                "situation": "onsite"
            },
            {
                "ko": "산재 처리하려면 어떤 서류가 필요합니까?",
                "vi": "Cần những giấy tờ gì để xử lý tai nạn lao động?",
                "situation": "formal"
            }
        ],
        "relatedTerms": ["직업병", "산업안전", "근로복지공단"]
    },
    {
        "id": "medical-occupational-disease",
        "slug": "benh-nghe-nghiep",
        "korean": "직업병",
        "vietnamese": "Bệnh nghề nghiệp",
        "hanja": "職業病",
        "hanjaReading": "職(직분 직) + 業(업 업) + 病(병 병)",
        "pronunciation": "벵 응에 응이엡",
        "meaningKo": "특정 직업이나 작업 환경에서 장기간 노출로 인해 발생하는 질병을 의미합니다. 통역 시 급성 산업재해(tai nạn)와 만성 직업병(bệnh)을 명확히 구분해야 하며, 한국에서는 진폐증, 소음성 난청, 화학물질 중독 등이 대표적입니다. 베트남에서는 광산 근로자의 폐질환이나 농약 중독이 흔하며, 직업병 인정 기준이 한국보다 엄격하여 통역 시 이를 사전에 설명해야 합니다.",
        "meaningVi": "Bệnh tật phát sinh do tiếp xúc lâu dài với môi trường làm việc đặc thù. Ở Việt Nam, bệnh phổi do bụi mỏ và ngộ độc thuốc trừ sâu là phổ biến. Tiêu chuẩn công nhận bệnh nghề nghiệp ở Việt Nam nghiêm ngặt hơn Hàn Quốc, cần có bằng chứng y khoa rõ ràng về mối liên hệ giữa bệnh và công việc.",
        "context": "산업의학, 노동보건, 예방의학",
        "culturalNote": "한국은 근로복지공단을 통해 직업병 판정과 보상이 이루어지지만, 베트남은 노동부 산하 기관에서 별도로 판정합니다. 한국에서는 근골격계 질환(손목터널증후군 등)도 직업병으로 인정받지만 베트남은 주로 화학물질 노출이나 물리적 환경(소음, 분진) 관련 질환만 인정하는 경향이 있습니다. 또한 한국은 정기 건강검진으로 직업병을 조기 발견하지만 베트남은 증상 발현 후 진단받는 경우가 많습니다.",
        "commonMistakes": [
            {
                "mistake": "Bệnh công nhân",
                "correction": "Bệnh nghề nghiệp",
                "explanation": "'노동자의 병'이 아니라 '직업과 관련된 병'이 정확한 표현입니다"
            },
            {
                "mistake": "직업병을 Bệnh do công việc로 풀어서 번역",
                "correction": "Bệnh nghề nghiệp (공식 용어) 사용",
                "explanation": "법적 용어는 공식 표현을 사용해야 합니다"
            },
            {
                "mistake": "산업재해와 직업병을 같은 용어로 번역",
                "correction": "산업재해=Tai nạn lao động, 직업병=Bệnh nghề nghiệp",
                "explanation": "급성 사고와 만성 질환은 법적으로 다릅니다"
            }
        ],
        "examples": [
            {
                "ko": "15년간 도장 작업을 하면서 직업병이 생겼습니다",
                "vi": "Sau 15 năm làm công việc sơn phủ, tôi đã mắc bệnh nghề nghiệp",
                "situation": "formal"
            },
            {
                "ko": "소음성 난청은 대표적인 직업병입니다",
                "vi": "Điếc do tiếng ồn là một bệnh nghề nghiệp điển hình",
                "situation": "onsite"
            },
            {
                "ko": "직업병 예방을 위해 보호장구를 착용하세요",
                "vi": "Hãy đeo đồ bảo hộ để phòng ngừa bệnh nghề nghiệp",
                "situation": "informal"
            }
        ],
        "relatedTerms": ["산업재해", "진폐증", "작업환경측정"]
    },
    {
        "id": "medical-health-checkup",
        "slug": "kham-suc-khoe",
        "korean": "건강검진",
        "vietnamese": "Khám sức khỏe",
        "hanja": "健康檢診",
        "hanjaReading": "健(건강할 건) + 康(편안할 강) + 檢(검사할 검) + 診(진찰할 진)",
        "pronunciation": "캄 썩 코에",
        "meaningKo": "질병의 조기 발견과 예방을 위해 정기적으로 실시하는 종합적인 건강 상태 점검을 의미합니다. 통역 시 한국의 국가건강검진 제도(일반검진, 암검진, 생애전환기검진)를 베트남에는 없는 제도임을 설명하고, 베트남에서는 개인이 비용을 부담하여 병원에서 받는 경우가 대부분임을 안내해야 합니다. 한국은 직장인 연 1회 의무 검진이지만 베트남은 자율적입니다.",
        "meaningVi": "Kiểm tra toàn diện tình trạng sức khỏe để phát hiện sớm và phòng ngừa bệnh tật. Ở Việt Nam, khám sức khỏe chủ yếu là dịch vụ tự nguyện tại bệnh viện, trong khi Hàn Quốc có chương trình khám sức khỏe quốc gia miễn phí hoặc có trợ cấp. Người lao động Việt Nam ở Hàn Quốc cần tận dụng quyền lợi khám sức khỏe định kỳ hàng năm.",
        "context": "예방의학, 직장건강관리, 국민건강보험",
        "culturalNote": "한국은 만 20세 이상 전 국민이 2년마다 무료 또는 일부 본인부담으로 건강검진을 받을 수 있으며, 직장인은 매년 받습니다. 베트남은 국가 차원의 무료 건강검진 제도가 없어 개인이 전액 부담하므로, 한국에서 일하는 베트남 근로자들에게 검진 혜택을 적극 안내해야 합니다. 또한 한국은 검진 결과를 모바일 앱으로 확인할 수 있지만 베트남은 종이 서류로만 받는 경우가 많습니다.",
        "commonMistakes": [
            {
                "mistake": "Kiểm tra sức khỏe",
                "correction": "Khám sức khỏe",
                "explanation": "의학 용어는 '검사(kiểm tra)'가 아닌 '진찰(khám)'을 사용합니다"
            },
            {
                "mistake": "건강검진을 Kiểm tra y tế로 번역",
                "correction": "Khám sức khỏe định kỳ (정기 건강검진)",
                "explanation": "정기 검진임을 명확히 해야 합니다"
            },
            {
                "mistake": "종합검진과 일반검진을 구분 안 함",
                "correction": "일반검진=Khám sức khỏe tổng quát, 종합검진=Khám sức khỏe toàn diện",
                "explanation": "검진 범위에 따라 다른 표현을 사용합니다"
            }
        ],
        "examples": [
            {
                "ko": "내년 1월에 건강검진을 받아야 합니다",
                "vi": "Tôi phải khám sức khỏe vào tháng 1 năm sau",
                "situation": "formal"
            },
            {
                "ko": "회사에서 건강검진 비용을 지원해줍니다",
                "vi": "Công ty hỗ trợ chi phí khám sức khỏe",
                "situation": "onsite"
            },
            {
                "ko": "건강검진 결과 이상 소견이 없습니다",
                "vi": "Kết quả khám sức khỏe không có bất thường",
                "situation": "formal"
            }
        ],
        "relatedTerms": ["종합검진", "암검진", "채용검진"]
    },
    {
        "id": "medical-metabolic-syndrome",
        "slug": "hoi-chung-chuyen-hoa",
        "korean": "대사증후군",
        "vietnamese": "Hội chứng chuyển hóa",
        "hanja": "代謝症候群",
        "hanjaReading": "代(대신할 대) + 謝(사례할 사) + 症(증세 증) + 候(기후 후) + 群(무리 군)",
        "pronunciation": "호이 쭝 쭈옌 호아",
        "meaningKo": "복부비만, 고혈압, 고혈당, 이상지질혈증 등이 동시에 나타나 심혈관질환 위험이 높아진 상태를 의미합니다. 통역 시 단순히 '비만'이 아닌 여러 대사 이상이 결합된 증후군임을 강조하고, 한국은 건강검진에서 대사증후군 판정 기준(5개 항목 중 3개 이상)을 명확히 제시하지만 베트남은 아직 표준화된 기준이 덜 보급되어 있음을 설명해야 합니다. 식습관과 운동 부족이 주 원인입니다.",
        "meaningVi": "Tình trạng kết hợp nhiều rối loạn chuyển hóa như béo phì vùng bụng, huyết áp cao, đường huyết cao và rối loạn lipid máu, làm tăng nguy cơ bệnh tim mạch. Ở Việt Nam, thuật ngữ này còn mới và nhiều người chưa nhận thức đầy đủ về nguy hiểm của hội chứng này. Thay đổi lối sống (ăn uống, vận động) là cách phòng ngừa chính.",
        "context": "만성질환, 생활습관병, 예방의학",
        "culturalNote": "한국은 국가건강검진에서 대사증후군을 별도 항목으로 판정하고 생활습관 개선 상담을 제공하지만, 베트남은 개별 질환(고혈압, 당뇨 등)으로만 보는 경향이 있습니다. 한국인은 '대사증후군'이라는 용어를 잘 알지만 베트남인은 생소할 수 있어 통역 시 '여러 만성질환이 한꺼번에 온 상태'라고 부연 설명이 필요합니다. 또한 한국은 허리둘레 기준이 남성 90cm, 여성 85cm이지만 베트남은 기준이 다를 수 있습니다.",
        "commonMistakes": [
            {
                "mistake": "Hội chứng béo phì",
                "correction": "Hội chứng chuyển hóa",
                "explanation": "단순 비만이 아니라 대사 이상 증후군입니다"
            },
            {
                "mistake": "대사증후군을 Bệnh chuyển hóa로 번역",
                "correction": "Hội chứng chuyển hóa (증후군=hội chứng)",
                "explanation": "질병(bệnh)이 아니라 증후군(hội chứng)입니다"
            },
            {
                "mistake": "Metabolic syndrome을 그대로 사용",
                "correction": "Hội chứng chuyển hóa (베트남어 번역)",
                "explanation": "환자에게는 모국어 용어를 사용해야 합니다"
            }
        ],
        "examples": [
            {
                "ko": "검진 결과 대사증후군으로 판정되었습니다",
                "vi": "Kết quả khám cho thấy bạn bị hội chứng chuyển hóa",
                "situation": "formal"
            },
            {
                "ko": "대사증후군은 운동과 식이요법으로 개선할 수 있습니다",
                "vi": "Hội chứng chuyển hóa có thể cải thiện bằng vận động và chế độ ăn",
                "situation": "onsite"
            },
            {
                "ko": "허리둘레가 기준을 초과하면 대사증후군 위험이 높습니다",
                "vi": "Nếu vòng eo vượt mức tiêu chuẩn thì nguy cơ hội chứng chuyển hóa cao",
                "situation": "formal"
            }
        ],
        "relatedTerms": ["복부비만", "당뇨병전단계", "심혈관질환"]
    },
    {
        "id": "medical-gout",
        "slug": "benh-gut",
        "korean": "통풍",
        "vietnamese": "Bệnh gút",
        "hanja": "痛風",
        "hanjaReading": "痛(아플 통) + 風(바람 풍)",
        "pronunciation": "벵 굿",
        "meaningKo": "혈액 내 요산 수치가 높아져 관절에 결정이 쌓여 극심한 통증과 염증을 일으키는 대사 질환입니다. 통역 시 '바람만 스쳐도 아프다'는 한자 의미를 설명하면 이해가 쉽고, 한국에서는 고기와 술 과다 섭취가 주 원인이지만 베트남에서는 해산물(조개, 새우) 과다 섭취도 흔한 원인임을 설명해야 합니다. 급성 발작 시 즉시 치료해야 하며 만성화되면 관절 변형이 올 수 있습니다.",
        "meaningVi": "Bệnh rối loạn chuyển hóa do nồng độ axit uric trong máu cao, tạo tinh thể lắng đọng ở khớp gây đau dữ dội và viêm. Ở Việt Nam, ăn nhiều hải sản (tôm, nghêu, sò) và uống rượu bia là nguyên nhân phổ biến. Cơn đau cấp tính thường xảy ra vào đêm khuya, đặc biệt ở khớp ngón chân cái. Cần kiêng ăn thực phẩm giàu purin và uống nhiều nước.",
        "context": "류마티스내과, 대사질환, 식이요법",
        "culturalNote": "한국에서는 '통풍'을 부유층 질병(고기, 술 과다)으로 인식하는 경향이 있지만 베트남에서는 해산물 섭취가 많아 일반인에게도 흔합니다. 한국은 통풍 치료제(알로푸리놀, 페북소스타트)가 보험 적용되어 저렴하지만 베트남은 약값이 비싸 치료 중단율이 높습니다. 통역 시 한국에서의 치료 접근성과 식이요법 교육이 잘 되어 있음을 안내하면 좋습니다.",
        "commonMistakes": [
            {
                "mistake": "Bệnh phong thấp",
                "correction": "Bệnh gút",
                "explanation": "류마티스(phong thấp)와 통풍(gút)은 다른 질환입니다"
            },
            {
                "mistake": "통풍을 Đau khớp do gió로 직역",
                "correction": "Bệnh gút (의학 용어)",
                "explanation": "한자 의미 직역이 아닌 의학 용어를 사용해야 합니다"
            },
            {
                "mistake": "Bệnh axit uric cao",
                "correction": "Bệnh gút (고요산혈증은 원인이지 병명이 아님)",
                "explanation": "원인(요산 높음)과 질병명(통풍)을 구분해야 합니다"
            }
        ],
        "examples": [
            {
                "ko": "발가락이 퉁퉁 붓고 아픈 게 통풍 증상입니다",
                "vi": "Ngón chân sưng và đau dữ dội là triệu chứng của bệnh gút",
                "situation": "onsite"
            },
            {
                "ko": "통풍 예방을 위해 맥주와 육류를 줄이세요",
                "vi": "Để phòng bệnh gút, hãy giảm bia và thịt đỏ",
                "situation": "informal"
            },
            {
                "ko": "요산 수치를 낮추는 약을 처방해드리겠습니다",
                "vi": "Tôi sẽ kê đơn thuốc hạ axit uric cho bạn",
                "situation": "formal"
            }
        ],
        "relatedTerms": ["고요산혈증", "관절염", "퓨린"]
    },
    {
        "id": "medical-rheumatoid-arthritis",
        "slug": "viem-khop-dang-thap",
        "korean": "류마티스관절염",
        "vietnamese": "Viêm khớp dạng thấp",
        "hanja": "類-關節炎",
        "hanjaReading": "類(무리 류) + 關(관계할 관) + 節(마디 절) + 炎(불꽃 염)",
        "pronunciation": "비엠 콥 장 탑",
        "meaningKo": "자가면역 질환으로 면역계가 자신의 관절을 공격하여 만성 염증과 통증, 변형을 일으키는 질환입니다. 통역 시 단순 관절염(퇴행성)과 류마티스 관절염(자가면역)을 명확히 구분하고, 조조강직(아침에 손이 뻣뻣함)이 특징적 증상임을 설명해야 합니다. 한국은 생물학적 제제 치료가 보험 적용되지만 베트남은 비용 부담이 커서 치료 접근성이 낮으므로 한국에서의 치료 기회를 적극 안내해야 합니다.",
        "meaningVi": "Bệnh tự miễn dịch mà hệ miễn dịch tấn công các khớp của cơ thể, gây viêm mãn tính, đau và biến dạng khớp. Triệu chứng đặc trưng là cứng khớp vào buổi sáng, đặc biệt ở các khớp tay. Ở Việt Nam, thuốc sinh học điều trị bệnh này rất đắt và ít được bảo hiểm chi trả, trong khi Hàn Quốc có chính sách hỗ trợ tốt hơn.",
        "context": "류마티스내과, 자가면역질환, 재활의학",
        "culturalNote": "한국은 류마티스 관절염 진단 후 조기에 생물학적 제제(TNF 억제제 등) 치료를 시작하여 관절 손상을 막지만, 베트남은 약값이 비싸 진행된 후에야 치료받는 경우가 많습니다. 한국에서는 류마티스내과 전문의가 많고 정기적인 혈액검사(CRP, ESR, RF)로 질병 활성도를 모니터링하지만 베트남은 전문의가 부족합니다. 통역 시 한국에서의 조기 진단과 치료 중요성을 강조해야 합니다.",
        "commonMistakes": [
            {
                "mistake": "Viêm khớp",
                "correction": "Viêm khớp dạng thấp",
                "explanation": "일반 관절염과 류마티스 관절염은 다릅니다"
            },
            {
                "mistake": "류마티스를 Bệnh phong thấp로만 번역",
                "correction": "Viêm khớp dạng thấp (정확한 의학 용어)",
                "explanation": "'phong thấp'은 민간 용어로 부정확합니다"
            },
            {
                "mistake": "관절염과 류마티스관절염을 구분 안 함",
                "correction": "관절염=Viêm khớp, 류마티스관절염=Viêm khớp dạng thấp",
                "explanation": "퇴행성과 자가면역은 전혀 다른 질환입니다"
            }
        ],
        "examples": [
            {
                "ko": "아침에 손이 뻣뻣한 증상이 류마티스관절염의 신호입니다",
                "vi": "Triệu chứng tay cứng vào buổi sáng là dấu hiệu của viêm khớp dạng thấp",
                "situation": "formal"
            },
            {
                "ko": "류마티스 인자 검사가 양성으로 나왔습니다",
                "vi": "Xét nghiệm yếu tố dạng thấp cho kết quả dương tính",
                "situation": "onsite"
            },
            {
                "ko": "생물학적 제제로 치료하면 관절 손상을 막을 수 있습니다",
                "vi": "Điều trị bằng thuốc sinh học có thể ngăn chặn tổn thương khớp",
                "situation": "formal"
            }
        ],
        "relatedTerms": ["자가면역질환", "조조강직", "생물학적제제"]
    },
    {
        "id": "medical-lupus",
        "slug": "lupus-ban-do",
        "korean": "루푸스",
        "vietnamese": "Lupus ban đỏ",
        "hanja": None,
        "hanjaReading": None,
        "pronunciation": "루푸스 반 도",
        "meaningKo": "전신홍반루푸스(SLE)의 약칭으로, 자가면역 질환 중 하나로 피부, 관절, 신장, 심장 등 전신 장기를 침범할 수 있는 만성 질환입니다. 통역 시 '루푸스'라는 외래어와 함께 '전신홍반루푸스'라는 정식 명칭을 병기하고, 나비 모양 얼굴 발진이 특징적 증상임을 설명해야 합니다. 한국은 희귀질환 산정특례로 치료비를 지원하지만 베트남은 그런 제도가 없어 환자 부담이 큽니다.",
        "meaningVi": "Lupus ban đỏ hệ thống (SLE) là bệnh tự miễn dịch mãn tính có thể tấn công nhiều cơ quan như da, khớp, thận, tim. Triệu chứng đặc trưng là phát ban đỏ hình cánh bướm trên má. Ở Việt Nam, bệnh này chưa được hỗ trợ chi phí điều trị như ở Hàn Quốc, khiến nhiều bệnh nhân gặp khó khăn về tài chính. Cần tránh ánh nắng mặt trời và tuân thủ điều trị dài hạn.",
        "context": "류마티스내과, 자가면역질환, 희귀질환",
        "culturalNote": "한국은 루푸스를 희귀난치성질환으로 지정하여 산정특례(본인부담 10%)를 적용하고 전문 진료팀이 관리하지만, 베트남은 희귀질환 지원 제도가 미흡합니다. 한국에서는 루푸스 환자들이 정기적으로 혈액검사(ANA, anti-dsDNA)와 신장검사를 받으며 하이드록시클로로퀸 등 약물을 지속 복용하지만, 베트남은 약값 부담으로 치료 중단이 잦습니다. 통역 시 한국에서의 지원 제도를 안내하면 도움이 됩니다.",
        "commonMistakes": [
            {
                "mistake": "Bệnh sói",
                "correction": "Lupus ban đỏ (의학 용어)",
                "explanation": "'늑대병'이라는 직역보다 의학 용어를 사용해야 합니다"
            },
            {
                "mistake": "루푸스를 Bệnh da đỏ로만 번역",
                "correction": "Lupus ban đỏ hệ thống (전신 질환임을 명시)",
                "explanation": "피부만이 아닌 전신 질환임을 강조해야 합니다"
            },
            {
                "mistake": "Lupus만 사용 (외래어 그대로)",
                "correction": "Lupus ban đỏ (베트남어 병기)",
                "explanation": "환자 이해를 위해 베트남어를 함께 써야 합니다"
            }
        ],
        "examples": [
            {
                "ko": "얼굴에 나비 모양 발진이 있으면 루푸스를 의심해야 합니다",
                "vi": "Nếu có phát ban hình cánh bướm trên mặt thì cần nghi ngờ lupus ban đỏ",
                "situation": "formal"
            },
            {
                "ko": "루푸스 환자는 햇빛을 피해야 합니다",
                "vi": "Bệnh nhân lupus ban đỏ cần tránh ánh nắng mặt trời",
                "situation": "onsite"
            },
            {
                "ko": "루푸스는 조기 진단과 치료가 매우 중요합니다",
                "vi": "Lupus ban đỏ cần chẩn đoán và điều trị sớm rất quan trọng",
                "situation": "formal"
            }
        ],
        "relatedTerms": ["자가면역질환", "희귀질환", "면역억제제"]
    },
    {
        "id": "medical-transplant-rejection",
        "slug": "phan-ung-thai-ghep",
        "korean": "이식거부반응",
        "vietnamese": "Phản ứng thải ghép",
        "hanja": "移植拒否反應",
        "hanjaReading": "移(옮길 이) + 植(심을 식) + 拒(막을 거) + 否(아닐 부) + 反(돌이킬 반) + 應(응할 응)",
        "pronunciation": "판 응 타이 겝",
        "meaningKo": "장기이식 후 수혜자의 면역체계가 이식된 장기를 외부 물질로 인식하여 공격하는 현상을 의미합니다. 통역 시 급성 거부반응(이식 직후)과 만성 거부반응(장기간 후)을 구분하고, 면역억제제 복용이 평생 필요함을 강조해야 합니다. 한국은 장기이식 후 관리 시스템이 잘 갖춰져 있지만 베트남은 사후관리가 미흡하여 거부반응 발생 시 대처가 어려울 수 있음을 설명해야 합니다.",
        "meaningVi": "Hiện tượng hệ miễn dịch của người nhận nhận ra cơ quan ghép là vật lạ và tấn công nó. Có phản ứng thải ghép cấp tính (ngay sau ghép) và mãn tính (sau nhiều năm). Người bệnh cần uống thuốc ức chế miễn dịch suốt đời để ngăn ngừa phản ứng thải ghép. Ở Việt Nam, hệ thống theo dõi sau ghép cơ quan còn hạn chế so với Hàn Quốc.",
        "context": "이식외과, 면역학, 장기이식",
        "culturalNote": "한국은 장기이식 후 정기적인 혈액검사와 조직검사로 거부반응을 조기 발견하고, 면역억제제(타크로리무스, 사이클로스포린 등)를 국가에서 지원하지만 베트남은 약값이 비싸 복용 중단이 잦아 거부반응 위험이 높습니다. 한국에서 이식받은 베트남인이 귀국 후 약을 끊으면 거부반응으로 이식 장기를 잃을 수 있으므로, 통역 시 평생 복약의 중요성을 반드시 강조해야 합니다.",
        "commonMistakes": [
            {
                "mistake": "Phản ứng từ chối ghép",
                "correction": "Phản ứng thải ghép",
                "explanation": "'거부(từ chối)'가 아닌 '배척(thải)'이 의학 용어입니다"
            },
            {
                "mistake": "이식거부를 Không chấp nhận ghép로 번역",
                "correction": "Phản ứng thải ghép (의학 용어)",
                "explanation": "면역학적 반응을 나타내는 전문 용어를 써야 합니다"
            },
            {
                "mistake": "급성과 만성 거부반응 구분 안 함",
                "correction": "급성=Cấp tính, 만성=Mãn tính 명시",
                "explanation": "발생 시기와 치료법이 다르므로 구분이 중요합니다"
            }
        ],
        "examples": [
            {
                "ko": "이식 후 거부반응 징후가 보이면 즉시 병원에 오세요",
                "vi": "Nếu thấy dấu hiệu phản ứng thải ghép sau khi ghép, hãy đến bệnh viện ngay",
                "situation": "formal"
            },
            {
                "ko": "면역억제제를 빠뜨리지 말고 정확한 시간에 복용하세요",
                "vi": "Hãy uống thuốc ức chế miễn dịch đúng giờ, không được bỏ sót",
                "situation": "onsite"
            },
            {
                "ko": "크레아티닌 수치가 올라가면 거부반응을 의심합니다",
                "vi": "Nếu chỉ số creatinine tăng thì nghi ngờ phản ứng thải ghép",
                "situation": "formal"
            }
        ],
        "relatedTerms": ["장기이식", "면역억제제", "조직적합성"]
    },
    {
        "id": "medical-mammography",
        "slug": "chup-x-quang-vu",
        "korean": "유방촬영술",
        "vietnamese": "Chụp X-quang vú",
        "hanja": "乳房撮影術",
        "hanjaReading": "乳(젖 유) + 房(방 방) + 撮(찍을 촬) + 影(그림자 영) + 術(재주 술)",
        "pronunciation": "쭙 엑스꽝 부",
        "meaningKo": "유방암 조기 발견을 위해 유방을 X선으로 촬영하는 검사 방법입니다. 통역 시 한국은 만 40세 이상 여성에게 2년마다 무료 유방촬영술을 제공하지만 베트남은 그런 제도가 없어 개인이 비용을 부담해야 함을 설명해야 합니다. 검사 시 유방을 압박하여 약간의 통증이 있을 수 있지만 정확한 진단을 위해 필요하며, 생리 직후에 검사하면 통증이 덜합니다.",
        "meaningVi": "Phương pháp chụp X-quang vú để phát hiện sớm ung thư vú. Ở Hàn Quốc, phụ nữ từ 40 tuổi được chụp X-quang vú miễn phí 2 năm một lần, trong khi ở Việt Nam chưa có chương trình sầm lọc quốc gia. Khi chụp, vú sẽ bị ép lại nên có thể hơi đau nhưng cần thiết để chẩn đoán chính xác. Nên chụp ngay sau kỳ kinh nguyệt để giảm đau.",
        "context": "유방외과, 암검진, 여성건강",
        "culturalNote": "한국은 국가암검진 사업으로 만 40세 이상 여성에게 2년마다 무료 유방촬영술을 제공하고, 이상 소견 시 초음파 추가 검사도 지원하지만 베트남은 국가 차원의 유방암 검진 프로그램이 없습니다. 한국 여성들은 유방암 검진의 중요성을 잘 알지만 베트남 여성들은 인식이 낮아, 한국에서 일하는 베트남 여성 근로자들에게 무료 검진 혜택을 적극 안내해야 합니다.",
        "commonMistakes": [
            {
                "mistake": "Chụp ảnh vú",
                "correction": "Chụp X-quang vú",
                "explanation": "일반 사진이 아닌 X선 촬영임을 명시해야 합니다"
            },
            {
                "mistake": "유방촬영술을 Soi vú로 번역",
                "correction": "Chụp X-quang vú (정확한 의학 용어)",
                "explanation": "'soi'는 내시경 검사를 의미하므로 부적절합니다"
            },
            {
                "mistake": "Mammography를 외래어 그대로 사용",
                "correction": "Chụp X-quang vú (베트남어 번역)",
                "explanation": "환자 이해를 위해 베트남어를 사용해야 합니다"
            }
        ],
        "examples": [
            {
                "ko": "만 40세가 되면 유방촬영술을 받으세요",
                "vi": "Khi đủ 40 tuổi, hãy đi chụp X-quang vú",
                "situation": "formal"
            },
            {
                "ko": "유방촬영 결과 석회화 소견이 보입니다",
                "vi": "Kết quả chụp X-quang vú thấy có vôi hóa",
                "situation": "onsite"
            },
            {
                "ko": "검사 시 유방을 압박하므로 약간 불편할 수 있습니다",
                "vi": "Khi chụp vú sẽ bị ép nên có thể hơi khó chịu",
                "situation": "formal"
            }
        ],
        "relatedTerms": ["유방암", "유방초음파", "조직검사"]
    },
    {
        "id": "medical-cervical-cancer-screening",
        "slug": "xet-nghiem-ung-thu-co-tu-cung",
        "korean": "자궁경부암검사",
        "vietnamese": "Xét nghiệm ung thư cổ tử cung",
        "hanja": "子宮頸部癌檢査",
        "hanjaReading": "子(아들 자) + 宮(집 궁) + 頸(목 경) + 部(부분 부) + 癌(암 암) + 檢(검사할 검) + 査(조사할 사)",
        "pronunciation": "셋 응이엠 웅 투 꼬 뜨 꿍",
        "meaningKo": "자궁경부암을 조기에 발견하기 위한 검사로 자궁경부 세포를 채취하여 검사합니다. 통역 시 한국은 만 20세 이상 여성에게 2년마다 무료 검사를 제공하지만 베트남은 그런 제도가 없음을 설명하고, 자궁경부암은 인유두종바이러스(HPV) 감염이 주 원인이므로 HPV 백신 접종도 권장해야 합니다. 검사는 간단하고 통증이 거의 없으며 조기 발견 시 완치율이 매우 높습니다.",
        "meaningVi": "Xét nghiệm phát hiện sớm ung thư cổ tử cung bằng cách lấy tế bào cổ tử cung để kiểm tra. Ở Hàn Quốc, phụ nữ từ 20 tuổi được xét nghiệm miễn phí 2 năm một lần, trong khi Việt Nam chưa có chương trình quốc gia. Nguyên nhân chính là nhiễm HPV (Human Papillomavirus), nên khuyến cáo tiêm vắc xin HPV. Xét nghiệm đơn giản, gần như không đau và tỷ lệ chữa khỏi rất cao nếu phát hiện sớm.",
        "context": "산부인과, 암검진, 여성건강",
        "culturalNote": "한국은 국가암검진으로 만 20세 이상 여성에게 자궁경부암 검사를 무료 제공하고, HPV 백신도 만 12~17세 여학생에게 무료 접종하지만 베트남은 두 가지 모두 개인 부담입니다. 한국 여성들은 정기 검진을 당연하게 여기지만 베트남 여성들은 산부인과 검진을 꺼리는 문화가 있어, 통역 시 검사의 중요성과 간편함을 강조하고 한국에서의 무료 혜택을 안내해야 합니다.",
        "commonMistakes": [
            {
                "mistake": "Kiểm tra tử cung",
                "correction": "Xét nghiệm ung thư cổ tử cung",
                "explanation": "자궁 전체가 아닌 자궁경부 암 검사임을 명시해야 합니다"
            },
            {
                "mistake": "자궁경부암검사를 Pap smear로만 표현",
                "correction": "Xét nghiệm ung thư cổ tử cung (Pap smear)",
                "explanation": "베트남어 용어를 주로 쓰고 괄호로 영어 병기합니다"
            },
            {
                "mistake": "HPV 검사와 세포검사를 혼동",
                "correction": "세포검사(Pap), HPV 검사 구분",
                "explanation": "두 검사는 목적과 방법이 다릅니다"
            }
        ],
        "examples": [
            {
                "ko": "20세 이상 여성은 2년마다 자궁경부암 검사를 받으세요",
                "vi": "Phụ nữ từ 20 tuổi nên xét nghiệm ung thư cổ tử cung 2 năm một lần",
                "situation": "formal"
            },
            {
                "ko": "검사 결과 이상세포가 발견되어 정밀검사가 필요합니다",
                "vi": "Kết quả xét nghiệm phát hiện tế bào bất thường, cần kiểm tra kỹ hơn",
                "situation": "onsite"
            },
            {
                "ko": "HPV 백신을 맞으면 자궁경부암을 70% 예방할 수 있습니다",
                "vi": "Tiêm vắc xin HPV có thể phòng ngừa 70% ung thư cổ tử cung",
                "situation": "formal"
            }
        ],
        "relatedTerms": ["자궁경부암", "인유두종바이러스", "세포진검사"]
    },
    {
        "id": "medical-std-testing",
        "slug": "xet-nghiem-benh-lay-qua-duong-tinh-duc",
        "korean": "성병검사",
        "vietnamese": "Xét nghiệm bệnh lây qua đường tình dục",
        "hanja": "性病檢査",
        "hanjaReading": "性(성품 성) + 病(병 병) + 檢(검사할 검) + 査(조사할 사)",
        "pronunciation": "셋 응이엠 벵 라이 꽈 드엉 띤 쭉",
        "meaningKo": "성 접촉을 통해 전염되는 질환들을 진단하기 위한 검사로, 매독, 임질, 클라미디아, HIV 등을 포함합니다. 통역 시 베트남에서는 성병 검사가 사회적으로 터부시되어 검사를 꺼리는 경향이 있지만, 한국에서는 보건소에서 익명으로 무료 검사를 받을 수 있음을 안내해야 합니다. 조기 발견 시 대부분 치료가 가능하며, 파트너에게 전파를 막기 위해 솔직한 검사와 치료가 중요함을 강조해야 합니다.",
        "meaningVi": "Xét nghiệm chẩn đoán các bệnh lây truyền qua tiếp xúc tình dục như giang mai, lậu, chlamydia, HIV v.v. Ở Việt Nam, xét nghiệm bệnh này bị coi là điều kỵ kỵ trong xã hội nên nhiều người ngại đi khám, nhưng ở Hàn Quốc có thể xét nghiệm miễn phí và ẩn danh tại trạm y tế. Hầu hết bệnh đều chữa được nếu phát hiện sớm, cần xét nghiệm và điều trị trung thực để không lây cho bạn tình.",
        "context": "비뇨기과, 산부인과, 감염내과",
        "culturalNote": "한국은 전국 보건소에서 익명으로 무료 성병검사(HIV, 매독, 임질, 클라미디아 등)를 제공하고 결과를 비밀로 보장하지만, 베트남은 검사 접근성이 낮고 사회적 낙인이 강합니다. 한국에서 일하는 베트남 근로자들에게 익명 검사 제도를 안내하고, 검사 결과는 절대 회사나 타인에게 공유되지 않음을 강조하여 검사를 독려해야 합니다. 조기 치료로 건강을 지킬 수 있습니다.",
        "commonMistakes": [
            {
                "mistake": "Bệnh hoa liễu",
                "correction": "Bệnh lây qua đường tình dục",
                "explanation": "'화류병'은 구식 표현이므로 현대 의학 용어를 써야 합니다"
            },
            {
                "mistake": "성병을 Bệnh xấu로 번역",
                "correction": "Bệnh lây qua đường tình dục (정확한 표현)",
                "explanation": "'나쁜 병'이라는 편견 표현은 부적절합니다"
            },
            {
                "mistake": "STD를 외래어 그대로 사용",
                "correction": "Bệnh lây qua đường tình dục (베트남어)",
                "explanation": "환자 이해를 위해 모국어를 사용해야 합니다"
            }
        ],
        "examples": [
            {
                "ko": "보건소에서 익명으로 성병검사를 무료로 받을 수 있습니다",
                "vi": "Có thể xét nghiệm bệnh lây qua đường tình dục miễn phí và ẩn danh tại trạm y tế",
                "situation": "formal"
            },
            {
                "ko": "성병 증상이 있으면 즉시 검사를 받으세요",
                "vi": "Nếu có triệu chứng bệnh lây qua đường tình dục, hãy xét nghiệm ngay",
                "situation": "onsite"
            },
            {
                "ko": "파트너도 함께 검사받는 것이 중요합니다",
                "vi": "Quan trọng là bạn tình cũng phải xét nghiệm cùng",
                "situation": "informal"
            }
        ],
        "relatedTerms": ["HIV검사", "매독", "임질"]
    },
    {
        "id": "medical-rehabilitation-counseling",
        "slug": "tu-van-phuc-hoi-chuc-nang",
        "korean": "재활상담",
        "vietnamese": "Tư vấn phục hồi chức năng",
        "hanja": "再活相談",
        "hanjaReading": "再(다시 재) + 活(살 활) + 相(서로 상) + 談(말씀 담)",
        "pronunciation": "뜨 반 푹 호이 쭉 낭",
        "meaningKo": "질병이나 사고 후 신체적, 정신적, 사회적 기능을 회복하기 위한 계획을 세우고 지원하는 상담 서비스입니다. 통역 시 재활은 단순히 물리치료만이 아니라 직업 복귀, 심리 회복, 보조기구 사용 등을 포괄하는 개념임을 설명하고, 한국은 재활의학과 전문의와 재활상담사가 체계적으로 지원하지만 베트남은 재활 인프라가 부족함을 안내해야 합니다. 조기 재활 시작이 회복 결과에 결정적입니다.",
        "meaningVi": "Dịch vụ tư vấn lập kế hoạch và hỗ trợ phục hồi chức năng thể chất, tinh thần và xã hội sau bệnh tật hoặc tai nạn. Phục hồi chức năng không chỉ là vật lý trị liệu mà còn bao gồm quay lại làm việc, phục hồi tâm lý, sử dụng dụng cụ hỗ trợ. Ở Hàn Quốc có bác sĩ chuyên khoa phục hồi chức năng và chuyên viên tư vấn phục hồi hỗ trợ hệ thống, trong khi Việt Nam thiếu cơ sở hạ tầng phục hồi. Bắt đầu phục hồi sớm rất quyết định đến kết quả hồi phục.",
        "context": "재활의학, 사회복지, 직업재활",
        "culturalNote": "한국은 국민건강보험에서 재활치료를 적극 지원하고, 재활의학과 전문의, 물리치료사, 작업치료사, 언어치료사, 재활상담사가 팀을 이뤄 환자를 돕지만 베트남은 재활 전문 인력과 시설이 부족합니다. 한국에서 산재나 교통사고로 다친 베트남 근로자들이 재활상담을 받으면 귀국 후에도 지속할 수 있는 재활 계획을 세울 수 있으므로, 통역 시 상담 혜택을 적극 안내해야 합니다.",
        "commonMistakes": [
            {
                "mistake": "Tư vấn vật lý trị liệu",
                "correction": "Tư vấn phục hồi chức năng",
                "explanation": "물리치료만이 아닌 포괄적 재활 상담입니다"
            },
            {
                "mistake": "재활상담을 Tư vấn tập luyện으로 번역",
                "correction": "Tư vấn phục hồi chức năng (의학 용어)",
                "explanation": "'훈련 상담'이 아닌 기능 회복 상담입니다"
            },
            {
                "mistake": "물리치료와 재활상담을 혼동",
                "correction": "물리치료=Vật lý trị liệu, 재활상담=Tư vấn phục hồi",
                "explanation": "치료와 상담은 다른 서비스입니다"
            }
        ],
        "examples": [
            {
                "ko": "뇌졸중 후 재활상담을 받으면 회복 계획을 세울 수 있습니다",
                "vi": "Sau đột quỵ não, nếu nhận tư vấn phục hồi chức năng có thể lập kế hoạch hồi phục",
                "situation": "formal"
            },
            {
                "ko": "재활상담사가 직업 복귀를 도와드릴 것입니다",
                "vi": "Chuyên viên tư vấn phục hồi sẽ giúp bạn quay lại làm việc",
                "situation": "onsite"
            },
            {
                "ko": "재활 목표를 함께 정하고 단계별로 진행합니다",
                "vi": "Chúng ta sẽ cùng đặt mục tiêu phục hồi và tiến hành từng bước",
                "situation": "informal"
            }
        ],
        "relatedTerms": ["물리치료", "작업치료", "직업재활"]
    },
    {
        "id": "medical-medical-tourism",
        "slug": "du-lich-y-te",
        "korean": "의료관광",
        "vietnamese": "Du lịch y tế",
        "hanja": "醫療觀光",
        "hanjaReading": "醫(의원 의) + 療(치료할 료) + 觀(볼 관) + 光(빛 광)",
        "pronunciation": "유 릭 이 떼",
        "meaningKo": "치료 목적으로 해외를 방문하거나 관광과 함께 의료 서비스를 받는 것을 의미합니다. 통역 시 한국은 성형외과, 치과, 건강검진, 암 치료 등에서 의료관광이 활발하며, 베트남에서도 한국 의료의 질과 기술을 높이 평가하여 많은 환자가 방문함을 설명해야 합니다. 의료관광 시 언어 장벽, 사후관리, 비용 등을 사전에 충분히 상담하고 공인된 의료기관을 이용해야 함을 안내해야 합니다.",
        "meaningVi": "Đi nước ngoài với mục đích điều trị hoặc kết hợp du lịch với dịch vụ y tế. Hàn Quốc phát triển du lịch y tế mạnh trong các lĩnh vực phẫu thuật thẩm mỹ, nha khoa, khám sức khỏe tổng quát, điều trị ung thư. Người Việt Nam đánh giá cao chất lượng và công nghệ y tế Hàn Quốc nên nhiều bệnh nhân đến khám. Khi du lịch y tế cần tư vấn kỹ trước về rào cản ngôn ngữ, chăm sóc sau điều trị, chi phí và sử dụng cơ sở y tế được công nhận.",
        "context": "국제의료, 관광산업, 헬스케어",
        "culturalNote": "한국 정부는 의료관광을 적극 육성하여 외국인 환자 유치에 힘쓰고 있으며, 주요 병원들은 국제진료센터와 통역 서비스를 제공합니다. 베트남인들은 주로 성형수술, 건강검진, 암 치료를 위해 한국을 방문하며, 한국 의료진의 실력을 신뢰하지만 비용 부담이 크고 언어 소통이 어려운 점이 장벽입니다. 통역사는 의료 용어뿐 아니라 한국 의료 시스템, 보험, 사후관리까지 안내할 수 있어야 합니다.",
        "commonMistakes": [
            {
                "mistake": "Du lịch khám bệnh",
                "correction": "Du lịch y tế",
                "explanation": "'병 보러 여행'이 아닌 공식 용어를 사용합니다"
            },
            {
                "mistake": "의료관광을 Du lịch chữa bệnh로 번역",
                "correction": "Du lịch y tế (표준 용어)",
                "explanation": "국제적으로 통용되는 용어를 써야 합니다"
            },
            {
                "mistake": "Medical tourism을 외래어 그대로 사용",
                "correction": "Du lịch y tế (베트남어 번역)",
                "explanation": "환자와 보호자 이해를 위해 베트남어를 써야 합니다"
            }
        ],
        "examples": [
            {
                "ko": "한국은 의료관광으로 유명합니다",
                "vi": "Hàn Quốc nổi tiếng về du lịch y tế",
                "situation": "informal"
            },
            {
                "ko": "의료관광 비자를 신청하려면 병원 예약 확인서가 필요합니다",
                "vi": "Để xin visa du lịch y tế cần giấy xác nhận đặt lịch khám tại bệnh viện",
                "situation": "formal"
            },
            {
                "ko": "치료 후 경과 관찰을 위해 한 달 후 재방문하세요",
                "vi": "Sau điều trị, hãy quay lại sau một tháng để theo dõi diễn biến",
                "situation": "onsite"
            }
        ],
        "relatedTerms": ["국제진료센터", "의료통역", "건강검진"]
    },
    {
        "id": "medical-pain-clinic",
        "slug": "phong-kham-dau",
        "korean": "통증클리닉",
        "vietnamese": "Phòng khám đau",
        "hanja": "疼痛-",
        "hanjaReading": "疼(아플 동) + 痛(아플 통)",
        "pronunciation": "퐁 캄 다우",
        "meaningKo": "만성 통증을 전문적으로 진단하고 치료하는 의료 시설로, 신경차단술, 약물치료, 물리치료 등을 제공합니다. 통역 시 단순 진통제 처방이 아니라 통증의 원인을 찾아 근본적으로 치료하는 곳임을 설명하고, 한국은 마취통증의학과 전문의가 운영하는 통증클리닉이 많지만 베트nam에서는 아직 생소한 개념임을 안내해야 합니다. 만성 요통, 목 디스크, 대상포진 후 신경통 등이 주요 치료 대상입니다.",
        "meaningVi": "Cơ sở y tế chuyên chẩn đoán và điều trị đau mãn tính, cung cấp các dịch vụ như phong tỏa thần kinh, điều trị bằng thuốc, vật lý trị liệu. Không chỉ đơn thuần kê thuốc giảm đau mà tìm nguyên nhân gây đau để điều trị căn bản. Ở Hàn Quốc có nhiều phòng khám đau do bác sĩ chuyên khoa gây mê và điều trị đau vận hành, trong khi ở Việt Nam khái niệm này còn khá mới. Các bệnh chính được điều trị: đau lưng mãn tính, thoát vị đĩa đệm cổ, đau thần kinh sau zona.",
        "context": "마취통증의학, 재활의학, 통증관리",
        "culturalNote": "한국은 마취통증의학과가 발달하여 통증클리닉이 많고, 신경차단술(injection)이나 고주파치료 등 비수술적 통증 치료 기술이 앞서 있습니다. 베트남은 통증을 '참는' 문화가 강하고 전문적인 통증 치료 시설이 적어, 만성 통증으로 고생하는 환자들이 많습니다. 한국에서 일하는 베트남 근로자 중 요통이나 어깨 통증으로 고생하는 경우가 많으므로, 통증클리닉 이용을 적극 권유하고 치료 방법을 설명해야 합니다.",
        "commonMistakes": [
            {
                "mistake": "Phòng khám giảm đau",
                "correction": "Phòng khám đau",
                "explanation": "통증 감소가 아닌 통증 전문 클리닉입니다"
            },
            {
                "mistake": "통증클리닉을 Phòng khám đau đớn으로 번역",
                "correction": "Phòng khám đau (간결한 표현)",
                "explanation": "'đau đớn'은 감정적 표현이므로 의학 용어로 부적절합니다"
            },
            {
                "mistake": "Pain clinic을 외래어 그대로 사용",
                "correction": "Phòng khám đau (베트남어)",
                "explanation": "환자 이해를 위해 베트남어를 사용해야 합니다"
            }
        ],
        "examples": [
            {
                "ko": "만성 요통은 통증클리닉에서 치료받으세요",
                "vi": "Đau lưng mãn tính nên điều trị tại phòng khám đau",
                "situation": "formal"
            },
            {
                "ko": "신경차단술로 통증을 완화할 수 있습니다",
                "vi": "Có thể giảm đau bằng phương pháp phong tỏa thần kinh",
                "situation": "onsite"
            },
            {
                "ko": "통증클리닉에서 정확한 원인을 찾아드리겠습니다",
                "vi": "Phòng khám đau sẽ tìm nguyên nhân chính xác cho bạn",
                "situation": "formal"
            }
        ],
        "relatedTerms": ["신경차단술", "만성통증", "마취통증의학"]
    }
]

# Read existing data
print(f"Reading file: {file_path}")
with open(file_path, 'r', encoding='utf-8') as f:
    data = json.load(f)

print(f"Current term count: {len(data)}")

# Filter out duplicates
existing_slugs = {term['slug'] for term in data}
# Remove 'id' field from new terms and filter duplicates
for t in new_terms:
    t.pop('id', None)
terms_to_add = [term for term in new_terms if term['slug'] not in existing_slugs]

print(f"Terms to add (after filtering duplicates): {len(terms_to_add)}")

# Add new terms
data.extend(terms_to_add)

# Write back
with open(file_path, 'w', encoding='utf-8') as f:
    json.dump(data, f, ensure_ascii=False, indent=2)

print(f"✅ Added {len(terms_to_add)} new medical terms")
print(f"Final term count: {len(data)}")
