#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
의료법/식품안전법 전문용어 추가 스크립트 (Medical Law/Food Safety Law Terms)
Tier S 품질 기준 준수
"""

import json
import os

# 파일 경로 설정
file_path = os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', 'data', 'terms', 'legal.json')

# 기존 데이터 로드
with open(file_path, 'r', encoding='utf-8') as f:
    data = json.load(f)  # data is a LIST

# 기존 slug 추출
existing_slugs = {t['slug'] for t in data}

# 새 용어 정의
new_terms = [
    {
        "slug": "giay-phep-hanh-nghe-y",
        "korean": "의사면허",
        "vietnamese": "Giấy phép hành nghề y",
        "hanja": "醫師免許",
        "hanjaReading": "醫(의원 의) + 師(스승 사) + 免(면할 면) + 許(허락할 허)",
        "pronunciation": "기엡 펩 한 응에 이",
        "meaningKo": "의료인이 의료 행위를 할 수 있는 법적 자격을 증명하는 면허증. 통역 시 주의할 점은 베트남에서는 'Giấy phép'(허가증)과 'Chứng chỉ'(자격증)를 구분하며, 의사면허는 보건부에서 발급하는 공식 허가이므로 반드시 'Giấy phép hành nghề'로 표현해야 함. 한국의 의사면허와 베트nam의 의사면허는 갱신 주기와 보수교육 요건이 다르므로, 면허 관련 통역 시 양국 제도 차이를 명확히 설명해야 오해를 방지할 수 있음.",
        "meaningVi": "Giấy chứng nhận pháp lý cho phép người hành nghề y tế được thực hiện các hoạt động khám, chữa bệnh. Tại Việt Nam, giấy phép hành nghề y do Bộ Y tế cấp và phải được gia hạn định kỳ theo quy định pháp luật.",
        "context": "의료법, 면허 관리, 의료인 자격",
        "culturalNote": "한국에서는 의사면허를 일생 유효한 자격으로 보는 경우가 많지만, 베트남에서는 정기적인 갱신과 보수교육이 필수적임. 또한 베트남에서는 '동의학 의사'(y sĩ y học cổ truyền)와 '현대의학 의사'(bác sĩ y học hiện đại)의 면허가 구분되어 발급되며, 진료 범위도 다름. 통역 시 이러한 차이를 명확히 전달하지 않으면 법적 분쟁이 발생할 수 있음.",
        "commonMistakes": [
            {
                "mistake": "Bằng bác sĩ (의사 학위)",
                "correction": "Giấy phép hành nghề y (의사면허)",
                "explanation": "학위(Bằng)와 면허(Giấy phép)는 다름. 학위는 교육 이수를 증명하고, 면허는 실제 진료 권한을 부여함"
            },
            {
                "mistake": "Chứng chỉ hành nghề (자격증)",
                "correction": "Giấy phép hành nghề y (의사면허)",
                "explanation": "의사면허는 정부 발급 공식 허가이므로 'Giấy phép'을 써야 하며, 'Chứng chỉ'는 민간 자격증에 사용됨"
            },
            {
                "mistake": "한국 의사면허 = 베트남에서도 유효",
                "correction": "각국 면허는 별도로 취득해야 함",
                "explanation": "의사면허는 국가별로 발급되며, 상호인정협정이 없는 한 다른 나라에서 진료할 수 없음"
            }
        ],
        "examples": [
            {
                "ko": "의사면허를 취득하기 위해서는 의과대학을 졸업하고 국가시험에 합격해야 합니다.",
                "vi": "Để có được giấy phép hành nghề y, cần phải tốt nghiệp trường y và đậu kỳ thi quốc gia.",
                "situation": "formal"
            },
            {
                "ko": "의사면허 없이 진료 행위를 하면 무면허 의료 행위로 처벌받습니다.",
                "vi": "Nếu hành nghề y mà không có giấy phép sẽ bị xử phạt vì hành nghề bất hợp pháp.",
                "situation": "formal"
            },
            {
                "ko": "베트남에서는 의사면허를 5년마다 갱신해야 한다고 들었어요.",
                "vi": "Tôi nghe nói ở Việt Nam phải gia hạn giấy phép hành nghề y mỗi 5 năm.",
                "situation": "informal"
            }
        ],
        "relatedTerms": ["luat-kham-benh-chua-benh", "trach-nhiem-y-te", "dong-y-dieu-tri"]
    },
    {
        "slug": "luat-kham-benh-chua-benh",
        "korean": "의료법",
        "vietnamese": "Luật Khám bệnh, chữa bệnh",
        "hanja": "醫療法",
        "hanjaReading": "醫(의원 의) + 療(치료할 료) + 法(법 법)",
        "pronunciation": "루엇 캄 벵 쯔어 벵",
        "meaningKo": "의료 행위와 의료기관 운영에 관한 법률. 통역 시 주의할 점은 베트남의 '의료법'은 '진료법'(Luật Khám bệnh, chữa bệnh)이라는 명칭으로, 한국의 '의료법'보다 범위가 좁고 구체적임. 베트남 의료법은 진료 행위 자체에 초점을 맞추며, 병원 시설 기준이나 의료 광고는 별도 법령으로 규제됨. 한국 의료법 관련 문서를 번역할 때는 해당 조항이 베트남의 어느 법령에 해당하는지 명확히 파악하고 통역해야 법적 오해를 방지할 수 있음.",
        "meaningVi": "Luật quy định về hoạt động khám bệnh, chữa bệnh và quản lý cơ sở y tế tại Việt Nam. Luật này quy định chi tiết về quyền và nghĩa vụ của người bệnh, trách nhiệm của người hành nghề y, và các tiêu chuẩn hành nghề y tế.",
        "context": "보건 법규, 의료 행정, 법적 책임",
        "culturalNote": "한국의 의료법은 단일 법률로 의료 전반을 규율하지만, 베트남은 '진료법', '약사법', '보험법' 등 여러 법률로 분산되어 있음. 따라서 한국 의료법의 특정 조항을 베트남어로 통역할 때는 해당 내용이 베트남의 어느 법령에 속하는지 먼저 확인해야 함. 또한 베트남에서는 전통의학(y học cổ truyền)에 대한 별도 법령이 있어, 한방 관련 통역 시 주의 필요.",
        "commonMistakes": [
            {
                "mistake": "Luật y tế (보건법)",
                "correction": "Luật Khám bệnh, chữa bệnh (의료법/진료법)",
                "explanation": "'Luật y tế'는 일반적인 보건법을 의미하며, 구체적인 진료 행위를 규율하는 법은 'Luật Khám bệnh, chữa bệnh'임"
            },
            {
                "mistake": "한국 의료법 조항을 그대로 직역",
                "correction": "베트남 법체계에 맞게 의역",
                "explanation": "양국 법체계가 다르므로, 한국 의료법의 내용이 베트남의 어느 법령에 해당하는지 파악 후 통역해야 함"
            },
            {
                "mistake": "Luật bệnh viện (병원법)",
                "correction": "Luật Khám bệnh, chữa bệnh (의료법)",
                "explanation": "베트남에는 '병원법'이라는 별도 법률이 없으며, 병원 운영도 진료법 내에서 규율됨"
            }
        ],
        "examples": [
            {
                "ko": "의료법에 따르면 의료기관은 진료기록을 10년간 보관해야 합니다.",
                "vi": "Theo Luật Khám bệnh, chữa bệnh, cơ sở y tế phải lưu trữ hồ sơ bệnh án trong 10 năm.",
                "situation": "formal"
            },
            {
                "ko": "의료법 위반으로 면허가 취소될 수 있습니다.",
                "vi": "Vi phạm Luật Khám bệnh, chữa bệnh có thể bị thu hồi giấy phép hành nghề.",
                "situation": "formal"
            },
            {
                "ko": "의료법 개정으로 원격진료가 부분적으로 허용되었어요.",
                "vi": "Do sửa đổi Luật Khám bệnh, chữa bệnh, khám chữa bệnh từ xa được cho phép một phần.",
                "situation": "informal"
            }
        ],
        "relatedTerms": ["giay-phep-hanh-nghe-y", "trach-nhiem-y-te", "quyen-benh-nhan"]
    },
    {
        "slug": "an-toan-thuc-pham",
        "korean": "식품안전",
        "vietnamese": "An toàn thực phẩm",
        "hanja": "食品安全",
        "hanjaReading": "食(밥 식) + 品(물건 품) + 安(편안 안) + 全(온전 전)",
        "pronunciation": "안 또안 턱 팜",
        "meaningKo": "식품이 인체에 해를 끼치지 않고 안전하게 섭취될 수 있도록 보장하는 것. 통역 시 주의할 점은 베트남에서는 '식품 위생'(Vệ sinh thực phẩm)과 '식품 안전'(An toàn thực phẩm)을 구분하여 사용하며, 전자는 청결 상태를, 후자는 유해 물질 부재를 의미함. 한국 식품안전 기준과 베트남 기준이 다르므로(특히 식품첨가물, 농약 잔류 허용치), 수출입 통역 시 양국 기준을 명확히 비교 설명해야 법적 문제를 예방할 수 있음.",
        "meaningVi": "Đảm bảo thực phẩm không gây hại cho sức khỏe con người khi tiêu dùng. Bao gồm kiểm soát chất độc hại, vi sinh vật gây bệnh, và các chất phụ gia thực phẩm. Tại Việt Nam, an toàn thực phẩm được quản lý chặt chẽ theo Luật An toàn thực phẩm.",
        "context": "식품 법규, 위생 관리, 수출입 검역",
        "culturalNote": "베트남은 길거리 음식 문화가 발달했지만 식품안전 인프라는 아직 발전 중이어서, 한국보다 식품 매개 질병 발생률이 높음. 따라서 식품안전 관련 통역 시 '예방적 조치'의 중요성을 강조해야 함. 또한 베트남에서는 전통 발효식품(mắm, nước mắm 등)의 안전 기준이 한국과 다르므로, 이러한 전통식품 수출입 통역 시 문화적 맥락 이해가 필수적임.",
        "commonMistakes": [
            {
                "mistake": "Vệ sinh thực phẩm (식품 위생)",
                "correction": "An toàn thực phẩm (식품 안전)",
                "explanation": "위생은 청결 상태, 안전은 유해 물질 부재를 의미. 법적 맥락에서는 'An toàn'이 더 포괄적"
            },
            {
                "mistake": "한국 식품안전 기준 = 베트남 기준",
                "correction": "각국 기준이 다름을 명시",
                "explanation": "식품첨가물 허용 목록, 농약 잔류 허용치 등이 국가마다 다르므로 반드시 구분 설명 필요"
            },
            {
                "mistake": "Chất lượng thực phẩm (식품 품질)",
                "correction": "An toàn thực phẩm (식품 안전)",
                "explanation": "품질은 맛, 영양 등 우수성을 의미하고, 안전은 위해 요소 부재를 의미함"
            }
        ],
        "examples": [
            {
                "ko": "식품안전법에 따라 모든 식품에는 유통기한을 표시해야 합니다.",
                "vi": "Theo Luật An toàn thực phẩm, tất cả thực phẩm phải ghi rõ hạn sử dụng.",
                "situation": "formal"
            },
            {
                "ko": "식품안전 검사를 통과하지 못하면 수입이 금지됩니다.",
                "vi": "Nếu không qua được kiểm tra an toàn thực phẩm sẽ bị cấm nhập khẩu.",
                "situation": "formal"
            },
            {
                "ko": "이 레스토랑은 식품안전 등급이 우수해요.",
                "vi": "Nhà hàng này có xếp hạng an toàn thực phẩm xuất sắc.",
                "situation": "informal"
            }
        ],
        "relatedTerms": ["luat-kham-benh-chua-benh", "thuoc-ke-don", "quang-cao-thuoc"]
    },
    {
        "slug": "trach-nhiem-y-te",
        "korean": "의료과실",
        "vietnamese": "Trách nhiệm y tế / Sai sót y khoa",
        "hanja": "醫療過失",
        "hanjaReading": "醫(의원 의) + 療(치료할 료) + 過(지날 과) + 失(잃을 실)",
        "pronunciation": "짝 니엠 이 떼 / 사이 쏟 이 코아",
        "meaningKo": "의료인이 의료 행위 중 주의 의무를 위반하여 환자에게 손해를 입힌 과실. 통역 시 주의할 점은 베트남에서는 '의료 과실'을 'Sai sót y khoa'(의학적 실수) 또는 'Trách nhiệm y tế'(의료 책임)로 표현하며, 한국보다 입증 책임이 환자에게 무거운 편임. 한국의 의료분쟁조정제도와 달리 베트남은 법원 소송이 주된 해결 방법이므로, 의료과실 관련 통역 시 양국 분쟁 해결 절차의 차이를 명확히 설명해야 환자 권리 보호에 도움이 됨.",
        "meaningVi": "Lỗi của người hành nghề y tế khi vi phạm nghĩa vụ chăm sóc, gây thiệt hại cho người bệnh. Bao gồm chẩn đoán sai, điều trị không đúng, hoặc thiếu sót trong quy trình y tế. Trách nhiệm y tế có thể dẫn đến xử lý hành chính, dân sự hoặc hình sự.",
        "context": "의료 분쟁, 법적 책임, 환자 권리",
        "culturalNote": "베트남에서는 의료과실 분쟁 시 환자가 과실을 입증해야 하는 부담이 크며, 한국처럼 감정인 제도가 체계화되지 않아 입증이 어려운 편임. 또한 베트남은 의사-환자 관계가 한국보다 더 위계적이어서, 환자가 의사의 과실을 지적하는 것 자체를 꺼리는 문화가 있음. 통역 시 이러한 문화 차이를 고려하여, 환자가 자신의 권리를 정확히 이해하도록 도와야 함.",
        "commonMistakes": [
            {
                "mistake": "Lỗi bác sĩ (의사 실수)",
                "correction": "Sai sót y khoa / Trách nhiệm y tế (의료과실)",
                "explanation": "'Lỗi bác sĩ'는 비공식적 표현이고, 법적 맥락에서는 'Sai sót y khoa' 또는 'Trách nhiệm y tế' 사용"
            },
            {
                "mistake": "의료과실 = 항상 형사 처벌",
                "correction": "민사/행정/형사 책임으로 구분됨",
                "explanation": "모든 의료과실이 형사 처벌로 이어지는 것은 아니며, 대부분 민사 배상이나 행정 처분으로 해결됨"
            },
            {
                "mistake": "Tai nạn y khoa (의료 사고)",
                "correction": "Sai sót y khoa (의료 과실)",
                "explanation": "'Tai nạn'은 우연한 사고, 'Sai sót'은 과실을 의미함. 법적 책임 여부가 다름"
            }
        ],
        "examples": [
            {
                "ko": "의료과실로 인한 손해배상 청구 소송이 증가하고 있습니다.",
                "vi": "Các vụ kiện đòi bồi thường do sai sót y khoa đang gia tăng.",
                "situation": "formal"
            },
            {
                "ko": "의사의 과실이 입증되면 손해배상 책임을 집니다.",
                "vi": "Nếu chứng minh được lỗi của bác sĩ, bác sĩ phải chịu trách nhiệm bồi thường.",
                "situation": "formal"
            },
            {
                "ko": "수술 중 실수로 합병증이 생겼는데, 이게 의료과실인가요?",
                "vi": "Có biến chứng do sai sót trong phẫu thuật, đây có phải là sai sót y khoa không?",
                "situation": "informal"
            }
        ],
        "relatedTerms": ["luat-kham-benh-chua-benh", "dong-y-dieu-tri", "quyen-benh-nhan"]
    },
    {
        "slug": "dong-y-dieu-tri",
        "korean": "치료동의",
        "vietnamese": "Đồng ý điều trị / Chấp thuận y tế",
        "hanja": "治療同意",
        "hanjaReading": "治(다스릴 치) + 療(치료할 료) + 同(한가지 동) + 意(뜻 의)",
        "pronunciation": "동 이 지에우 찌",
        "meaningKo": "환자가 의료 행위의 내용과 위험을 충분히 설명받고 자발적으로 치료에 동의하는 것. 통역 시 주의할 점은 베트남에서는 '서면 동의'(Đồng ý bằng văn bản)가 필수인 의료 행위 범위가 한국보다 좁으며, 구두 동의도 많이 인정됨. 하지만 수술이나 침습적 시술의 경우 반드시 서면 동의가 필요하므로, 통역 시 어떤 경우에 서면 동의가 필수인지 명확히 전달해야 법적 분쟁을 예방할 수 있음. 또한 베트남에서는 가족 동의가 환자 본인 동의만큼 중요시되는 경향이 있어, 이 차이를 설명해야 함.",
        "meaningVi": "Sự chấp thuận của người bệnh sau khi được giải thích đầy đủ về nội dung, lợi ích và rủi ro của điều trị. Đồng ý điều trị phải tự nguyện, có hiểu biết và được ghi nhận bằng văn bản đối với các can thiệp y tế lớn như phẫu thuật.",
        "context": "환자 권리, 의료 윤리, 법적 절차",
        "culturalNote": "베트남은 유교 문화의 영향으로 가족주의가 강해서, 환자 본인보다 가족(특히 가장)이 치료 결정권을 행사하는 경우가 많음. 반면 한국은 최근 환자 자기결정권이 강조되면서 본인 동의가 우선시됨. 통역 시 이러한 문화 차이로 인한 갈등을 예방하기 위해, 양국의 '동의' 개념 차이를 명확히 설명해야 함. 특히 말기 환자의 연명치료 중단 등 민감한 사안에서는 더욱 주의 필요.",
        "commonMistakes": [
            {
                "mistake": "Cho phép điều trị (치료 허가)",
                "correction": "Đồng ý điều trị (치료 동의)",
                "explanation": "'Cho phép'은 위에서 아래로 허가하는 뉘앙스, 'Đồng ý'는 대등한 입장에서 동의하는 의미"
            },
            {
                "mistake": "구두 동의만으로 충분",
                "correction": "수술 등 주요 시술은 서면 동의 필수",
                "explanation": "침습적 의료 행위는 반드시 서면 동의가 필요하며, 구두 동의는 법적 효력이 약함"
            },
            {
                "mistake": "Ký tên (서명)",
                "correction": "Đồng ý điều trị có hiểu biết (충분한 설명 후 동의)",
                "explanation": "단순 서명이 아니라 충분한 설명을 듣고 이해한 후의 동의여야 법적 효력이 있음"
            }
        ],
        "examples": [
            {
                "ko": "수술 전에 환자로부터 치료동의서를 받아야 합니다.",
                "vi": "Trước khi phẫu thuật phải có giấy đồng ý điều trị từ người bệnh.",
                "situation": "formal"
            },
            {
                "ko": "치료동의 없이 수술하면 의료법 위반입니다.",
                "vi": "Phẫu thuật mà không có đồng ý điều trị là vi phạm Luật Khám bệnh, chữa bệnh.",
                "situation": "formal"
            },
            {
                "ko": "이 시술은 위험이 있으니 동의서에 서명해 주세요.",
                "vi": "Ca can thiệp này có rủi ro, xin vui lòng ký vào giấy đồng ý.",
                "situation": "onsite"
            }
        ],
        "relatedTerms": ["quyen-benh-nhan", "trach-nhiem-y-te", "luat-kham-benh-chua-benh"]
    },
    {
        "slug": "bao-hiem-y-te",
        "korean": "건강보험",
        "vietnamese": "Bảo hiểm y tế",
        "hanja": "健康保險",
        "hanjaReading": "健(굳셀 건) + 康(편안 강) + 保(지킬 보) + 險(험할 험)",
        "pronunciation": "바오 히엠 이 떼",
        "meaningKo": "질병이나 부상으로 인한 의료비를 보장하는 사회보험 제도. 통역 시 주의할 점은 한국의 건강보험은 전국민 강제가입 단일보험자 제도인 반면, 베트남은 의무가입 대상이 제한적이고 민간보험 비중이 높다는 점임. 베트남 건강보험 적용 범위가 한국보다 좁아서(특히 고가 의료 장비, 신약 등), 본인 부담금 비율이 높음. 한국 환자가 베트남에서 치료받거나 그 반대의 경우, 보험 적용 여부와 사후 환급 절차를 명확히 통역해야 경제적 분쟁을 예방할 수 있음.",
        "meaningVi": "Chế độ bảo hiểm xã hội để chi trả chi phí khám chữa bệnh khi ốm đau, tai nạn. Tại Việt Nam, bảo hiểm y tế bắt buộc đối với người lao động và một số nhóm đối tượng, nhưng chưa bao phủ toàn dân như Hàn Quốc. Tỷ lệ đồng chi trả của người bệnh còn cao.",
        "context": "사회보험, 의료비 지급, 보험 청구",
        "culturalNote": "한국은 1989년부터 전국민 건강보험을 시행하여 보험 적용률이 매우 높지만, 베트남은 2014년에야 전국민 건강보험을 목표로 했고 아직 미가입자가 많음. 또한 베트남은 공립병원과 사립병원의 보험 적용 범위가 크게 달라서, 사립병원 이용 시 본인 부담이 훨씬 큼. 통역 시 이러한 차이를 모르면 환자가 예상치 못한 고액 의료비를 부담하게 될 수 있으므로 주의 필요.",
        "commonMistakes": [
            {
                "mistake": "한국 건강보험 = 베트남 건강보험",
                "correction": "양국 제도 차이 명확히 설명",
                "explanation": "적용 범위, 본인부담률, 급여 항목이 크게 다르므로 혼동하면 안 됨"
            },
            {
                "mistake": "Bảo hiểm sức khỏe (건강 보험 일반)",
                "correction": "Bảo hiểm y tế (사회건강보험)",
                "explanation": "'Bảo hiểm sức khỏe'는 민간 건강보험 포함, 'Bảo hiểm y tế'는 사회보험 의미"
            },
            {
                "mistake": "모든 병원에서 보험 적용 동일",
                "correction": "공립/사립, 등급별로 적용 범위 다름",
                "explanation": "베트남은 병원 등급과 공립/사립 여부에 따라 보험 적용률이 크게 차이남"
            }
        ],
        "examples": [
            {
                "ko": "건강보험증을 지참하시면 진료비의 80%가 보장됩니다.",
                "vi": "Nếu có thẻ bảo hiểm y tế, 80% chi phí khám chữa bệnh sẽ được chi trả.",
                "situation": "formal"
            },
            {
                "ko": "외국인도 한국 건강보험에 가입할 수 있나요?",
                "vi": "Người nước ngoài có thể tham gia bảo hiểm y tế Hàn Quốc không?",
                "situation": "formal"
            },
            {
                "ko": "이 약은 건강보험이 안 돼서 전액 본인 부담이에요.",
                "vi": "Thuốc này không thuộc bảo hiểm y tế nên phải tự trả toàn bộ.",
                "situation": "informal"
            }
        ],
        "relatedTerms": ["luat-kham-benh-chua-benh", "thuoc-ke-don", "quyen-benh-nhan"]
    },
    {
        "slug": "thuoc-ke-don",
        "korean": "처방약",
        "vietnamese": "Thuốc kê đơn / Thuốc theo toa",
        "hanja": "處方藥",
        "hanjaReading": "處(곳 처) + 方(모 방) + 藥(약 약)",
        "pronunciation": "툭 께 던 / 툭 테오 또아",
        "pronunciation": "툭 께 던",
        "meaningKo": "의사의 처방전이 있어야만 구입할 수 있는 의약품. 통역 시 주의할 점은 한국과 베트남의 처방약 분류 기준이 다르며, 한국에서 일반의약품인 것이 베트남에서는 처방약인 경우도 있고 그 반대도 있음. 특히 항생제의 경우 베트남은 처방전 없이 구입 가능한 경우가 많아 오남용 문제가 심각함. 한국 환자가 베트남에서 약 구입 시 또는 베트남 환자가 한국 약 구입 시, 처방전 필요 여부를 명확히 통역해야 불법 구입이나 건강 위해를 방지할 수 있음.",
        "meaningVi": "Thuốc chỉ được bán khi có đơn thuốc từ bác sĩ. Bao gồm kháng sinh, thuốc điều trị mạn tính, và các thuốc có nguy cơ tác dụng phụ cao. Tại Việt Nam, quy định về thuốc kê đơn chưa được thực thi chặt chẽ như Hàn Quốc, dẫn đến tình trạng lạm dụng kháng sinh.",
        "context": "약사법, 의약품 관리, 환자 안전",
        "culturalNote": "베트남은 약국에서 처방전 없이 항생제 등 처방약을 쉽게 구입할 수 있는 문화가 있어, 항생제 내성 문제가 심각함. 반면 한국은 처방약 관리가 엄격하여, 베트남 환자들이 한국에서 익숙한 약을 구하지 못해 당황하는 경우가 많음. 통역 시 이러한 문화 차이를 설명하고, 처방약의 오남용 위험성을 강조하여 환자 안전을 도모해야 함.",
        "commonMistakes": [
            {
                "mistake": "Thuốc bán theo đơn (판매용 약)",
                "correction": "Thuốc kê đơn / Thuốc theo toa (처방약)",
                "explanation": "'Thuốc kê đơn'이 공식 용어이며, 'Thuốc bán theo đơn'은 비표준 표현"
            },
            {
                "mistake": "한국 처방약 = 베트남 처방약",
                "correction": "각국 분류 기준 다름",
                "explanation": "같은 성분이라도 국가별로 처방약/일반약 분류가 다를 수 있음"
            },
            {
                "mistake": "Thuốc chữa bệnh (치료약)",
                "correction": "Thuốc kê đơn (처방약)",
                "explanation": "'Thuốc chữa bệnh'는 모든 치료약을 의미하며, 처방약만을 지칭하지 않음"
            }
        ],
        "examples": [
            {
                "ko": "이 약은 처방약이므로 의사 처방전 없이는 구입할 수 없습니다.",
                "vi": "Thuốc này là thuốc kê đơn nên không thể mua nếu không có đơn thuốc của bác sĩ.",
                "situation": "formal"
            },
            {
                "ko": "처방약을 임의로 복용하면 부작용이 발생할 수 있습니다.",
                "vi": "Dùng thuốc kê đơn tùy tiện có thể gây tác dụng phụ.",
                "situation": "formal"
            },
            {
                "ko": "베트남에서는 항생제를 처방전 없이도 살 수 있다던데 사실인가요?",
                "vi": "Nghe nói ở Việt Nam có thể mua kháng sinh mà không cần đơn thuốc, có đúng không?",
                "situation": "informal"
            }
        ],
        "relatedTerms": ["an-toan-thuc-pham", "quang-cao-thuoc", "bao-hiem-y-te"]
    },
    {
        "slug": "quang-cao-thuoc",
        "korean": "의약품광고",
        "vietnamese": "Quảng cáo thuốc",
        "hanja": "醫藥品廣告",
        "hanjaReading": "醫(의원 의) + 藥(약 약) + 品(물건 품) + 廣(넓을 광) + 告(알릴 고)",
        "pronunciation": "꽝 까오 툭",
        "meaningKo": "의약품의 효능, 안전성 등을 알리는 광고 행위로, 허위·과대 광고가 엄격히 규제됨. 통역 시 주의할 점은 한국과 베트남 모두 처방약 광고는 금지하지만, 일반의약품 광고 규제 수준이 다름. 한국은 심의를 거친 후에만 광고 가능하지만, 베트남은 규제가 느슨한 편이어서 과대광고가 많음. 한국 제약사가 베트남에서 광고할 때 또는 그 반대의 경우, 양국 광고 규제 차이를 명확히 통역해야 법적 제재를 피할 수 있음.",
        "meaningVi": "Hoạt động quảng bá thuốc về công dụng, tính an toàn. Quảng cáo thuốc kê đơn bị cấm, quảng cáo thuốc không kê đơn phải được cơ quan y tế phê duyệt. Việt Nam còn tồn tại nhiều quảng cáo thuốc sai sự thật, thổi phồng công dụng.",
        "context": "약사법, 소비자 보호, 광고 규제",
        "culturalNote": "베트남은 TV, 라디오, 인터넷에서 의약품 광고가 매우 활발하며, 유명인을 모델로 한 광고도 흔함. 반면 한국은 의약품 광고 규제가 엄격하여, 효능·효과를 과장하거나 의사 추천 문구를 사용할 수 없음. 통역 시 이러한 차이를 모르면 한국 제약사가 베트남식 광고를 한국에서 그대로 사용하려다 법적 문제가 생길 수 있으므로 주의 필요.",
        "commonMistakes": [
            {
                "mistake": "Quảng cáo y tế (의료 광고 일반)",
                "correction": "Quảng cáo thuốc (의약품 광고)",
                "explanation": "'Quảng cáo y tế'는 병원, 의료 서비스 광고 포함. 의약품 광고는 'Quảng cáo thuốc'"
            },
            {
                "mistake": "처방약도 광고 가능",
                "correction": "처방약 광고는 양국 모두 금지",
                "explanation": "한국, 베트남 모두 처방약의 소비자 대상 광고는 불법임"
            },
            {
                "mistake": "Tiếp thị thuốc (약품 마케팅)",
                "correction": "Quảng cáo thuốc (의약품 광고)",
                "explanation": "마케팅은 포괄적 개념, 광고는 구체적 홍보 행위를 의미"
            }
        ],
        "examples": [
            {
                "ko": "의약품광고는 식약처의 사전 심의를 받아야 합니다.",
                "vi": "Quảng cáo thuốc phải được Cục Quản lý Dược thẩm định trước.",
                "situation": "formal"
            },
            {
                "ko": "허위·과대 의약품광고는 처벌 대상입니다.",
                "vi": "Quảng cáo thuốc gian dối, phóng đại sẽ bị xử phạt.",
                "situation": "formal"
            },
            {
                "ko": "이 약 광고 진짜 효과가 있을까요? 너무 과장된 것 같은데.",
                "vi": "Quảng cáo thuốc này có thật sự hiệu quả không? Cảm giác như bị thổi phồng quá.",
                "situation": "informal"
            }
        ],
        "relatedTerms": ["thuoc-ke-don", "an-toan-thuc-pham", "luat-kham-benh-chua-benh"]
    },
    {
        "slug": "thu-nghiem-lam-sang",
        "korean": "임상시험",
        "vietnamese": "Thử nghiệm lâm sàng",
        "hanja": "臨床試驗",
        "hanjaReading": "臨(임할 임) + 床(평상 상) + 試(시험 시) + 驗(시험 험)",
        "pronunciation": "투 응이엠 람 상",
        "meaningKo": "신약이나 치료법의 안전성과 유효성을 평가하기 위해 사람을 대상으로 실시하는 시험. 통역 시 주의할 점은 베트남의 임상시험 규제가 한국보다 덜 엄격하여, 시험 대상자 보호 수준이 낮은 편임. 한국은 IRB(기관생명윤리위원회) 승인과 피험자 동의가 엄격하지만, 베트남은 절차가 간소하여 윤리 문제가 발생하기도 함. 한국 제약사가 베트남에서 임상시험 시, 양국 기준 차이를 명확히 통역하여 윤리적 문제나 법적 분쟁을 예방해야 함.",
        "meaningVi": "Nghiên cứu trên người để đánh giá tính an toàn và hiệu quả của thuốc mới hoặc phương pháp điều trị mới. Thử nghiệm lâm sàng phải được Bộ Y tế phê duyệt và có sự đồng ý tự nguyện của người tham gia sau khi được giải thích đầy đủ.",
        "context": "신약 개발, 의학 연구, 피험자 권리",
        "culturalNote": "베트남은 임상시험 비용이 저렴하고 피험자 모집이 용이하여, 국제 제약사들의 임상시험지로 선호되지만, 피험자 권리 보호 체계가 한국보다 미흡함. 한국은 피험자에게 발생한 손해에 대한 보상 체계가 명확하지만, 베트남은 이러한 보상 제도가 충분히 정비되지 않음. 통역 시 피험자 권리와 보상 문제를 명확히 설명하여, 피험자가 충분한 정보에 기반해 동의할 수 있도록 해야 함.",
        "commonMistakes": [
            {
                "mistake": "Thử nghiệm y học (의학 시험)",
                "correction": "Thử nghiệm lâm sàng (임상시험)",
                "explanation": "'Thử nghiệm lâm sàng'이 공식 용어이며, 사람 대상 시험을 명확히 나타냄"
            },
            {
                "mistake": "임상시험 = 인체 실험",
                "correction": "임상시험은 윤리적 승인 받은 연구",
                "explanation": "'인체 실험'은 부정적 뉘앙스, '임상시험'은 윤리적 절차를 거친 합법적 연구"
            },
            {
                "mistake": "Nghiên cứu thuốc (약물 연구)",
                "correction": "Thử nghiệm lâm sàng (임상시험)",
                "explanation": "약물 연구는 동물실험 포함, 임상시험은 사람 대상 연구만을 의미"
            }
        ],
        "examples": [
            {
                "ko": "이 신약은 현재 3상 임상시험 단계에 있습니다.",
                "vi": "Thuốc mới này hiện đang trong giai đoạn thử nghiệm lâm sàng pha 3.",
                "situation": "formal"
            },
            {
                "ko": "임상시험 참여는 자발적이며, 언제든지 중단할 수 있습니다.",
                "vi": "Tham gia thử nghiệm lâm sàng là tự nguyện và có thể dừng lại bất cứ lúc nào.",
                "situation": "formal"
            },
            {
                "ko": "임상시험에 참여하면 무료로 치료받을 수 있다던데, 위험은 없나요?",
                "vi": "Nghe nói tham gia thử nghiệm lâm sàng được điều trị miễn phí, có rủi ro gì không?",
                "situation": "informal"
            }
        ],
        "relatedTerms": ["dong-y-dieu-tri", "thuoc-ke-don", "trach-nhiem-y-te"]
    },
    {
        "slug": "quyen-benh-nhan",
        "korean": "환자권리",
        "vietnamese": "Quyền bệnh nhân",
        "hanja": "患者權利",
        "hanjaReading": "患(근심 환) + 者(사람 자) + 權(권세 권) + 利(이로울 리)",
        "pronunciation": "꾸옌 벵 년",
        "meaningKo": "환자가 의료 서비스를 받을 때 법적으로 보장받는 권리로, 알 권리, 선택권, 자기결정권, 비밀보장 등을 포함함. 통역 시 주의할 점은 베트남의 환자권리 개념이 한국보다 덜 발달했으며, 특히 '알 권리'와 '자기결정권' 보장이 미흡함. 베트남은 의사 중심의 온정주의적(paternalistic) 의료 문화가 강해서, 환자가 자신의 병명이나 예후를 제대로 통보받지 못하는 경우도 있음. 한국 의료기관에서 베트남 환자 진료 시, 환자권리를 명확히 통역하여 문화적 갈등을 예방해야 함.",
        "meaningVi": "Các quyền lợi được pháp luật bảo vệ khi người bệnh nhận dịch vụ y tế, bao gồm quyền được biết thông tin, quyền tự quyết định, quyền được bảo mật, và quyền từ chối điều trị. Tại Việt Nam, nhận thức về quyền bệnh nhân còn hạn chế so với Hàn Quốc.",
        "context": "의료 윤리, 환자 보호, 법적 권리",
        "culturalNote": "한국은 2016년 '환자 알 권리 및 자기결정권 존중'을 명시한 법률이 시행되어 환자권리가 강화되었지만, 베트남은 아직 이러한 체계적 법제화가 미흡함. 베트남 환자들은 의사에게 질문하거나 다른 의견을 제시하는 것을 꺼리는 경향이 있어, 한국 의료진이 환자에게 선택권을 주면 오히려 당황하는 경우도 있음. 통역 시 이러한 문화 차이를 고려하여, 환자가 자신의 권리를 이해하고 행사할 수 있도록 도와야 함.",
        "commonMistakes": [
            {
                "mistake": "Quyền lợi bệnh nhân (환자 혜택)",
                "correction": "Quyền bệnh nhân (환자 권리)",
                "explanation": "'Quyền lợi'는 '혜택', 'Quyền'은 '권리'. 법적 권리는 'Quyền' 사용"
            },
            {
                "mistake": "환자 권리 = 의사에게 요구할 수 있는 것",
                "correction": "법으로 보장된 기본 권리",
                "explanation": "환자 권리는 단순 요구가 아니라 법적으로 보장된 권리이며, 의료진은 이를 존중할 의무가 있음"
            },
            {
                "mistake": "Lợi ích bệnh nhân (환자 이익)",
                "correction": "Quyền bệnh nhân (환자 권리)",
                "explanation": "'Lợi ích'은 '이익', 법적 권리를 나타낼 때는 'Quyền' 사용"
            }
        ],
        "examples": [
            {
                "ko": "환자권리장전에 따라 귀하는 진료 정보를 열람할 권리가 있습니다.",
                "vi": "Theo Hiến chương quyền bệnh nhân, quý vị có quyền xem hồ sơ bệnh án của mình.",
                "situation": "formal"
            },
            {
                "ko": "환자에게는 치료를 거부할 권리도 있습니다.",
                "vi": "Bệnh nhân cũng có quyền từ chối điều trị.",
                "situation": "formal"
            },
            {
                "ko": "제 병에 대해서 자세히 설명해 주세요. 환자도 알 권리가 있잖아요.",
                "vi": "Xin giải thích rõ về bệnh của tôi. Bệnh nhân cũng có quyền được biết mà.",
                "situation": "informal"
            }
        ],
        "relatedTerms": ["dong-y-dieu-tri", "luat-kham-benh-chua-benh", "bao-hiem-y-te"]
    }
]

# 중복 필터링
new_terms_filtered = [term for term in new_terms if term['slug'] not in existing_slugs]

# 데이터 추가
data.extend(new_terms_filtered)

# 파일 저장
with open(file_path, 'w', encoding='utf-8') as f:
    json.dump(data, f, ensure_ascii=False, indent=2)

print(f"✅ 추가 완료: {len(new_terms_filtered)}개 용어")
print(f"📊 전체 용어 수: {len(data)}개")
print(f"🔍 중복 제외: {len(new_terms) - len(new_terms_filtered)}개")
