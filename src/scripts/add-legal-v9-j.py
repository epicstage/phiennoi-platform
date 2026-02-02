#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""국제형사법 용어 추가 (v9-j)"""
import json
import os

def load_existing_terms():
    file_path = os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', 'data', 'terms', 'legal.json')
    with open(file_path, 'r', encoding='utf-8') as f:
        data = json.load(f)
    return data, file_path

def create_legal_terms():
    terms = [
        {
            "slug": "toa-an-hinh-su-quoc-te",
            "korean": "국제형사재판소",
            "vietnamese": "Tòa án hình sự quốc tế",
            "hanja": "國際刑事裁判所",
            "hanjaReading": "國(나라 국) + 際(사이 제) + 刑(형벌 형) + 事(일 사) + 裁(재단할 재) + 判(판단할 판) + 所(바 소)",
            "pronunciation": "국제형사재판소",
            "meaningKo": "집단학살·전쟁범죄·인도에 반한 죄 등 중대 국제범죄를 재판하는 상설 국제법정입니다. 통역 시 ICC(International Criminal Court)로 약칭하며, 네덜란드 헤이그에 소재, 한국은 2003년 가입, 국내법이 처벌하지 못할 때 보충적으로 관할하며, 미국·중국·러시아는 미가입이라는 점을 명확히 전달해야 합니다.",
            "meaningVi": "Tòa án quốc tế thường trực xét xử tội phạm quốc tế nghiêm trọng như diệt chủng, tội phạm chiến tranh, tội phạm chống lại nhân loại. Viết tắt là ICC (International Criminal Court), tọa lạc tại Hague Hà Lan, Hàn Quốc gia nhập năm 2003, có thẩm quyền bổ sung khi luật quốc gia không trừng phạt được, Mỹ, Trung Quốc, Nga chưa gia nhập.",
            "context": "국제범죄 기소 및 ICC 관할권 논의 상황에서 사용",
            "culturalNote": "한국은 ICC 가입국이지만 아직 국내 이행법을 제정하지 못해 실제 협력에 한계가 있습니다. ICC는 아프리카 국가 지도자를 주로 기소하여 선진국 편향 논란이 있으며, 푸틴 러시아 대통령도 체포영장이 발부되었으나 집행이 어렵습니다. 베트남은 미가입국이어서 통역 시 ICC의 역할과 한계를 설명해야 합니다.",
            "commonMistakes": [
                {
                    "mistake": "tòa án quốc tế",
                    "correction": "tòa án hình sự quốc tế (형사 전담)",
                    "explanation": "'국제법원'은 국제사법재판소(ICJ)와 혼동되며 형사 전담 법원임을 명시해야 합니다"
                },
                {
                    "mistake": "ICC",
                    "correction": "tòa án hình sự quốc tế (ICC) - 약자 병기",
                    "explanation": "약자만 쓰지 말고 베트남어로 풀어 쓰고 약자를 병기해야 합니다"
                },
                {
                    "mistake": "tòa án chiến tranh",
                    "correction": "tòa án hình sự quốc tế (전쟁범죄는 일부)",
                    "explanation": "'전쟁법원'은 전쟁범죄만 연상되며 집단학살·인도에 반한 죄가 누락됩니다"
                }
            ],
            "examples": [
                {
                    "ko": "국제형사재판소는 푸틴 러시아 대통령에게 체포영장을 발부했습니다",
                    "vi": "Tòa án hình sự quốc tế đã phát lệnh bắt Tổng thống Nga Putin",
                    "situation": "formal"
                },
                {
                    "ko": "ICC는 어떤 범죄를 다루나요?",
                    "vi": "ICC xử lý tội phạm nào?",
                    "situation": "onsite"
                },
                {
                    "ko": "국제형사재판소는 국내법이 처벌하지 못할 때 보충적으로 관할합니다",
                    "vi": "Tòa án hình sự quốc tế có thẩm quyền bổ sung khi luật quốc gia không trừng phạt được",
                    "situation": "formal"
                }
            ],
            "relatedTerms": ["ICC", "로마규정", "집단학살", "보편적관할권"]
        },
        {
            "slug": "toi-pham-chien-tranh",
            "korean": "전쟁범죄",
            "vietnamese": "Tội phạm chiến tranh",
            "hanja": "戰爭犯罪",
            "hanjaReading": "戰(싸울 전) + 爭(다툴 쟁) + 犯(범할 범) + 罪(허물 죄)",
            "pronunciation": "전쟁범죄",
            "meaningKo": "무력충돌 중 제네바협약 등 국제인도법을 위반하여 민간인을 살해·고문하거나 전쟁포로를 학대하는 등의 범죄입니다. 통역 시 민간인 공격·포로 학대·약탈·강간·문화재 파괴 등이 포함되며, ICC와 국내 법원이 처벌하고, 시효가 없으며, 지휘관책임도 인정된다는 점을 명확히 전달해야 합니다.",
            "meaningVi": "Tội phạm trong xung đột vũ trang vi phạm luật nhân đạo quốc tế như Công ước Geneva, giết, tra tấn dân thường hoặc ngược đãi tù binh chiến tranh. Bao gồm tấn công dân thường, ngược đãi tù binh, cướp bóc, hiếp dâm, phá hoại di sản văn hóa, ICC và tòa án quốc gia trừng phạt, không có thời hiệu, cũng công nhận trách nhiệm chỉ huy viên.",
            "context": "전쟁범죄 조사 및 국제법정 기소 상황에서 사용",
            "culturalNote": "한국은 한국전쟁 시 민간인 학살 등 전쟁범죄가 있었으나 기소되지 않았으며, 베트남전 당시 한국군의 민간인 학살 의혹도 제기되었습니다. 우크라이나전쟁에서 러시아군 전쟁범죄가 국제적으로 조사 중입니다. 베트남전 전쟁범죄는 미국이 주로 비판받았습니다. 통역 시 양국의 역사적 맥락을 고려해야 합니다.",
            "commonMistakes": [
                {
                    "mistake": "tội ác chiến tranh",
                    "correction": "tội phạm chiến tranh (법적 용어)",
                    "explanation": "'전쟁 악행'은 도덕적 비난이며 법적 범죄의 개념이 약화됩니다"
                },
                {
                    "mistake": "vi phạm luật chiến tranh",
                    "correction": "tội phạm chiến tranh (범죄)",
                    "explanation": "'전쟁법 위반'은 일반 위반이며 형사 범죄로서의 성격이 누락됩니다"
                },
                {
                    "mistake": "giết người trong chiến tranh",
                    "correction": "tội phạm chiến tranh (포괄적)",
                    "explanation": "'전쟁 중 살인'은 일부이며 고문·약탈 등 다른 범죄가 제외됩니다"
                }
            ],
            "examples": [
                {
                    "ko": "러시아군은 부차에서 민간인을 학살하여 전쟁범죄로 기소되었습니다",
                    "vi": "Quân Nga bị truy tố tội phạm chiến tranh vì thảm sát dân thường tại Bucha",
                    "situation": "formal"
                },
                {
                    "ko": "전쟁 중 민간인을 죽이면 전쟁범죄인가요?",
                    "vi": "Giết dân thường trong chiến tranh có phải tội phạm chiến tranh không?",
                    "situation": "onsite"
                },
                {
                    "ko": "전쟁범죄는 시효가 없어 언제든 처벌할 수 있습니다",
                    "vi": "Tội phạm chiến tranh không có thời hiệu nên có thể trừng phạt bất cứ lúc nào",
                    "situation": "formal"
                }
            ],
            "relatedTerms": ["제네바협약", "국제인도법", "민간인학살", "지휘관책임"]
        },
        {
            "slug": "toi-chong-lai-nhan-loai",
            "korean": "인도에반한죄",
            "vietnamese": "Tội chống lại nhân loại",
            "hanja": "人道에反한罪",
            "hanjaReading": "人(사람 인) + 道(길 도) + 反(반대할 반) + 罪(허물 죄)",
            "pronunciation": "인도에반한죄",
            "meaningKo": "민간인에 대한 광범위하거나 조직적인 공격으로 살해·고문·강제실종 등을 저지르는 범죄입니다. 통역 시 전쟁 여부와 무관하게 평시에도 성립하며, 집단학살보다 범위가 넓고, 나치 홀로코스트·캄보디아 킬링필드가 대표 사례이며, ICC와 국내 법원이 처벌하고 시효가 없다는 점을 명확히 전달해야 합니다.",
            "meaningVi": "Tội phạm tấn công rộng hoặc có tổ chức vào dân thường, gây giết, tra tấn, mất tích cưỡng bức. Thành lập bất kể có chiến tranh hay không, ngay cả thời bình, phạm vi rộng hơn diệt chủng, Holocaust Nazi và Killing Fields Campuchia là ví dụ tiêu biểu, ICC và tòa án quốc gia trừng phạt, không có thời hiệu.",
            "context": "대규모 인권침해 조사 및 국제법정 기소 상황에서 사용",
            "culturalNote": "한국은 일제강점기 위안부·강제징용 등이 인도에 반한 죄로 주장되지만 국제법정 기소는 없었습니다. 북한 정치범수용소도 인도에 반한 죄로 지적되며, 유엔 조사위가 보고서를 발표했습니다. 중국 위구르 탄압도 논란입니다. 베트남은 킬링필드 피해국이어서 통역 시 역사적 맥락을 고려해야 합니다.",
            "commonMistakes": [
                {
                    "mistake": "tội ác nhân đạo",
                    "correction": "tội chống lại nhân loại (법적 용어)",
                    "explanation": "'인도적 범죄'는 비공식적이며 법률 용어로 부적절합니다"
                },
                {
                    "mistake": "vi phạm nhân quyền",
                    "correction": "tội chống lại nhân loại (형사 범죄)",
                    "explanation": "'인권 침해'는 일반 침해이며 형사 범죄로서의 성격이 누락됩니다"
                },
                {
                    "mistake": "tội diệt chủng",
                    "correction": "tội chống lại nhân loại (더 넓음) vs diệt chủng (특정 집단)",
                    "explanation": "'집단학살죄'는 특정 집단 말살이며 인도에 반한 죄가 더 넓습니다"
                }
            ],
            "examples": [
                {
                    "ko": "나치는 유대인 학살로 인도에 반한 죄로 뉘른베르크 재판에서 유죄 판결을 받았습니다",
                    "vi": "Đức Nazi bị kết tội chống lại nhân loại tại Tòa án Nuremberg vì thảm sát người Do Thái",
                    "situation": "formal"
                },
                {
                    "ko": "전쟁 없어도 인도에 반한 죄가 되나요?",
                    "vi": "Không có chiến tranh cũng có tội chống lại nhân loại à?",
                    "situation": "onsite"
                },
                {
                    "ko": "인도에 반한 죄는 평시에도 민간인에 대한 조직적 공격으로 성립합니다",
                    "vi": "Tội chống lại nhân loại thành lập ngay cả thời bình do tấn công có tổ chức vào dân thường",
                    "situation": "formal"
                }
            ],
            "relatedTerms": ["집단학살", "전쟁범죄", "홀로코스트", "조직적공격"]
        },
        {
            "slug": "diet-chung",
            "korean": "집단학살",
            "vietnamese": "Diệt chủng",
            "hanja": "集團虐殺",
            "hanjaReading": "集(모을 집) + 團(둥글 단) + 虐(학대할 학) + 殺(죽일 살)",
            "pronunciation": "집단학살",
            "meaningKo": "특정 인종·민족·종교·국민 집단을 전부 또는 일부 파괴할 의도로 행하는 행위를 말합니다. 통역 시 genocide(제노사이드)로 영어 표현도 일반적이며, 살해·신체·정신 해침·생활조건 악화·출산 방해·아동 이전 등 5가지 행위가 포함되고, 의도 입증이 핵심이며, ICC가 처벌하고 시효가 없다는 점을 명확히 전달해야 합니다.",
            "meaningVi": "Hành vi với ý định tiêu diệt toàn bộ hoặc một phần nhóm chủng tộc, dân tộc, tôn giáo, quốc dân cụ thể. Tiếng Anh là genocide cũng thông dụng, bao gồm 5 hành vi: giết, gây hại thân thể/tinh thần, làm xấu điều kiện sống, cản trở sinh đẻ, chuyển trẻ em, cốt lõi là chứng minh ý định, ICC trừng phạt, không có thời hiệu.",
            "context": "집단학살 조사 및 국제법정 기소 상황에서 사용",
            "culturalNote": "한국은 일제강점기와 한국전쟁 시 집단학살을 경험했으며, 북한 정치범수용소도 집단학살 논란이 있습니다. 르완다 집단학살(1994)과 보스니아 스레브레니차 학살(1995)이 대표 사례이며, 미얀마 로힝야 학살도 제노사이드로 지적됩니다. 베트남전 미라이 학살은 전쟁범죄이지 제노사이드는 아닙니다. 통역 시 정의를 명확히 해야 합니다.",
            "commonMistakes": [
                {
                    "mistake": "thảm sát",
                    "correction": "diệt chủng (특정 집단 말살 의도)",
                    "explanation": "'학살'은 대량 살인이며 특정 집단 말살 의도가 없으면 집단학살이 아닙니다"
                },
                {
                    "mistake": "tội ác diệt chủng",
                    "correction": "diệt chủng (genocide)",
                    "explanation": "'제노사이드 범죄'는 장황하며 '제노사이드'가 간결합니다"
                },
                {
                    "mistake": "giết hàng loạt",
                    "correction": "diệt chủng (특정 집단 + 의도)",
                    "explanation": "'대량 살인'은 무차별 살인이며 특정 집단 말살 의도가 누락됩니다"
                }
            ],
            "examples": [
                {
                    "ko": "르완다에서 후투족이 투치족 100만 명을 학살한 것은 집단학살로 인정되었습니다",
                    "vi": "Người Hutu thảm sát 1 triệu người Tutsi ở Rwanda được công nhận là diệt chủng",
                    "situation": "formal"
                },
                {
                    "ko": "집단학살과 전쟁범죄는 어떻게 다른가요?",
                    "vi": "Diệt chủng và tội phạm chiến tranh khác nhau thế nào?",
                    "situation": "onsite"
                },
                {
                    "ko": "집단학살은 특정 집단을 파괴할 의도가 있어야 성립합니다",
                    "vi": "Diệt chủng phải có ý định tiêu diệt nhóm cụ thể mới thành lập",
                    "situation": "formal"
                }
            ],
            "relatedTerms": ["제노사이드", "르완다학살", "인도에반한죄", "특정집단"]
        },
        {
            "slug": "trach-nhiem-chi-huy-vien",
            "korean": "지휘관책임",
            "vietnamese": "Trách nhiệm chỉ huy viên",
            "hanja": "指揮官責任",
            "hanjaReading": "指(가리킬 지) + 揮(휘두를 휘) + 官(벼슬 관) + 責(꾸짖을 책) + 任(맡길 임)",
            "pronunciation": "지휘관책임",
            "meaningKo": "부하가 저지른 전쟁범죄를 지휘관이 알았거나 알 수 있었는데도 방지·처벌하지 않은 경우 지휘관도 책임을 지는 원칙입니다. 통역 시 실제 범행을 직접 하지 않아도 책임을 지며, 군 지휘관뿐 아니라 민간 상관도 포함하고, 뉘른베르크 재판에서 확립되었으며, ICC 로마규정에 명시되었다는 점을 명확히 전달해야 합니다.",
            "meaningVi": "Nguyên tắc chỉ huy viên cũng chịu trách nhiệm nếu biết hoặc có thể biết tội phạm chiến tranh của cấp dưới nhưng không ngăn chặn/trừng phạt. Ngay cả không trực tiếp thực hiện hành vi cũng chịu trách nhiệm, không chỉ chỉ huy quân sự mà cả cấp trên dân sự, được thiết lập tại Tòa án Nuremberg, được ghi rõ trong Quy chế Rome của ICC.",
            "context": "전쟁범죄 재판 및 지휘관 기소 상황에서 사용",
            "culturalNote": "한국은 베트남전 당시 민간인 학살에 대한 지휘관책임 논란이 있으며, 북한 정치범수용소 운영자의 지휘관책임도 제기됩니다. 유고전범재판소는 스레브레니차 학살에서 지휘관책임으로 여러 장성을 유죄 판결했습니다. 베트남전 미라이 학살에서도 지휘관 책임이 문제되었습니다. 통역 시 직접 범행 없이도 책임을 진다는 점을 강조해야 합니다.",
            "commonMistakes": [
                {
                    "mistake": "lỗi của chỉ huy",
                    "correction": "trách nhiệm chỉ huy viên (법적 원칙)",
                    "explanation": "'지휘관 과실'은 일상 표현이며 법적 책임 원칙의 개념이 약화됩니다"
                },
                {
                    "mistake": "cấp trên chịu trách nhiệm",
                    "correction": "trách nhiệm chỉ huy viên (군 + 민간)",
                    "explanation": "'상관 책임'은 일반 책임이며 전쟁범죄의 특수 책임과 다릅니다"
                },
                {
                    "mistake": "người chỉ huy có tội",
                    "correction": "trách nhiệm chỉ huy viên (법리)",
                    "explanation": "'지휘자 유죄'는 결과이며 책임 원칙으로서의 법리가 누락됩니다"
                }
            ],
            "examples": [
                {
                    "ko": "세르비아 장군은 부하의 학살을 방치하여 지휘관책임으로 유죄 판결을 받았습니다",
                    "vi": "Tướng Serbia bị kết tội trách nhiệm chỉ huy viên vì để mặc cấp dưới thảm sát",
                    "situation": "formal"
                },
                {
                    "ko": "지휘관이 직접 죽이지 않았는데 왜 처벌받나요?",
                    "vi": "Chỉ huy viên không trực tiếp giết sao lại bị phạt?",
                    "situation": "onsite"
                },
                {
                    "ko": "지휘관책임은 부하의 범죄를 알고도 방지하지 않으면 성립합니다",
                    "vi": "Trách nhiệm chỉ huy viên thành lập nếu biết tội phạm của cấp dưới nhưng không ngăn chặn",
                    "situation": "formal"
                }
            ],
            "relatedTerms": ["전쟁범죄", "뉘른베르크재판", "상급자책임", "방치책임"]
        },
        {
            "slug": "dan-do",
            "korean": "인도",
            "vietnamese": "Dẫn độ",
            "hanja": "引渡",
            "hanjaReading": "引(끌 인) + 渡(건널 도)",
            "pronunciation": "인도",
            "meaningKo": "범죄인을 재판·형 집행을 위해 외국으로 인도하는 절차입니다. 통역 시 한국은 인도조약 체결국에만 인도하며, 정치범·사형 가능범은 인도하지 않고, 자국민 불인도 원칙이 있으며, 상호주의로 조약 없어도 가능하고, 법원 심사를 거쳐 법무부가 결정한다는 점을 명확히 전달해야 합니다.",
            "meaningVi": "Thủ tục giao tội phạm sang nước ngoài để xét xử/thi hành hình phạt. Hàn Quốc chỉ dẫn độ cho nước ký hiệp ước dẫn độ, không dẫn độ tội phạm chính trị và tội có thể bị tử hình, có nguyên tắc không dẫn độ công dân, có thể theo chủ nghĩa tương hỗ ngay cả không có hiệp ước, qua thẩm tra tòa án và Bộ Pháp lý quyết định.",
            "context": "범죄인 인도 요청 및 심사 절차에서 사용",
            "culturalNote": "한국은 미국·일본 등 30여 국과 인도조약을 체결했으며, 중국과는 2002년 체결했으나 정치적 이유로 실제 인도는 드뭅니다. 2008년 미국 쇠고기 수입 반대 시위자를 인도한 논란이 있었고, 북한 탈북자 강제 송환은 인도와 다릅니다. 베트남은 인도조약이 적어 통역 시 한국의 인도 요건을 설명해야 합니다.",
            "commonMistakes": [
                {
                    "mistake": "giao nộp tội phạm",
                    "correction": "dẫn độ (법적 절차)",
                    "explanation": "'범죄자 인계'는 일상 표현이며 법적 절차로서의 인도와 다릅니다"
                },
                {
                    "mistake": "trả về",
                    "correction": "dẫn độ (외국으로)",
                    "explanation": "'돌려보내다'는 모호하며 외국으로 인도하는 의미가 불명확합니다"
                },
                {
                    "mistake": "trục xuất",
                    "correction": "dẫn độ (재판 목적) vs trục xuất (추방)",
                    "explanation": "'강제퇴거'는 불법체류자 추방이며 범죄인 인도와 법적 성격이 다릅니다"
                }
            ],
            "examples": [
                {
                    "ko": "한국은 미국 요청으로 사기범을 인도했습니다",
                    "vi": "Hàn Quốc đã dẫn độ kẻ lừa đảo theo yêu cầu của Mỹ",
                    "situation": "formal"
                },
                {
                    "ko": "인도되면 사형받을 수 있나요?",
                    "vi": "Nếu bị dẫn độ có thể bị tử hình không?",
                    "situation": "onsite"
                },
                {
                    "ko": "사형이 가능한 범죄는 인도하지 않습니다",
                    "vi": "Tội có thể bị tử hình thì không dẫn độ",
                    "situation": "formal"
                }
            ],
            "relatedTerms": ["인도조약", "정치범불인도", "자국민불인도", "상호주의"]
        },
        {
            "slug": "hop-tac-hinh-su-quoc-te",
            "korean": "국제형사공조",
            "vietnamese": "Hợp tác hình sự quốc tế",
            "hanja": "國際刑事共助",
            "hanjaReading": "國(나라 국) + 際(사이 제) + 刑(형벌 형) + 事(일 사) + 共(함께 공) + 助(도울 조)",
            "pronunciation": "국제형사공조",
            "meaningKo": "국가 간 범죄 수사·재판을 위해 증거 수집·증인 조사·압수수색 등을 협력하는 제도입니다. 통역 시 한국은 국제형사사법공조법으로 규율하며, 조약 체결국과 협력하고, 상호주의로 조약 없어도 가능하며, 증거 송부·증인 신문·서류 송달 등이 포함되고, 국제범죄 수사에 필수적이라는 점을 명확히 전달해야 합니다.",
            "meaningVi": "Chế độ hợp tác giữa các nước để thu thập chứng cứ, điều tra nhân chứng, khám xét thu giữ phục vụ điều tra/xét xử tội phạm. Hàn Quốc quy định bởi Luật hợp tác tư pháp hình sự quốc tế, hợp tác với nước ký hiệp ước, có thể theo chủ nghĩa tương hỗ ngay cả không có hiệp ước, bao gồm gửi chứng cứ, thẩm vấn nhân chứng, tống đạt tài liệu, cần thiết cho điều tra tội phạm quốc tế.",
            "context": "국제범죄 수사 협력 요청 및 증거 수집 상황에서 사용",
            "culturalNote": "한국은 국제범죄가 증가하며 형사공조가 활발해졌고, 미국·중국·일본 등과 빈번히 협력합니다. 보이스피싱 범죄는 중국에서 조직되어 한국인을 대상으로 하므로 공조가 필수이며, 마약·테러 수사도 국제 공조가 중요합니다. 베트남과도 범죄인 인도·증거 수집 협력이 증가하고 있습니다. 통역 시 공조의 중요성을 설명해야 합니다.",
            "commonMistakes": [
                {
                    "mistake": "hợp tác tội phạm",
                    "correction": "hợp tác hình sự quốc tế (수사 협력)",
                    "explanation": "'범죄 협력'은 범죄자들의 공모처럼 들리며 수사 협력의 의미가 왜곡됩니다"
                },
                {
                    "mistake": "giúp đỡ điều tra",
                    "correction": "hợp tác hình sự quốc tế (법적 제도)",
                    "explanation": "'수사 도움'은 일상 표현이며 법적 제도로서의 공조 개념이 약화됩니다"
                },
                {
                    "mistake": "tương trợ quốc tế",
                    "correction": "hợp tác hình sự quốc tế (형사 특화)",
                    "explanation": "'국제 상호지원'은 포괄적이며 형사 분야의 특수성이 누락됩니다"
                }
            ],
            "examples": [
                {
                    "ko": "한국은 미국에 보이스피싱 범죄 증거 수집을 위해 국제형사공조를 요청했습니다",
                    "vi": "Hàn Quốc đã yêu cầu Mỹ hợp tác hình sự quốc tế để thu thập chứng cứ tội phạm voice phishing",
                    "situation": "formal"
                },
                {
                    "ko": "외국에서 증거를 받으려면 어떻게 하나요?",
                    "vi": "Muốn nhận chứng cứ từ nước ngoài thì làm sao?",
                    "situation": "onsite"
                },
                {
                    "ko": "국제형사공조는 국제범죄 수사에 필수적입니다",
                    "vi": "Hợp tác hình sự quốc tế là cần thiết cho điều tra tội phạm quốc tế",
                    "situation": "formal"
                }
            ],
            "relatedTerms": ["국제공조법", "증거수집", "증인조사", "상호주의"]
        },
        {
            "slug": "dan-do-toi-pham",
            "korean": "범죄인인도",
            "vietnamese": "Dẫn độ tội phạm",
            "hanja": "犯罪人引渡",
            "hanjaReading": "犯(범할 범) + 罪(허물 죄) + 人(사람 인) + 引(끌 인) + 渡(건널 도)",
            "pronunciation": "범죄인인도",
            "meaningKo": "범죄를 저지른 사람을 재판이나 형 집행을 위해 외국에 넘기는 제도로, 인도와 같은 의미입니다. 통역 시 한국은 인도법으로 규율하며, 인도조약 필요, 쌍방가벌성(양국 모두 범죄), 정치범·군사범 불인도, 자국민 불인도 원칙, 특정범죄 원칙(청구 범죄만 처벌)이 적용된다는 점을 명확히 전달해야 합니다.",
            "meaningVi": "Chế độ giao người phạm tội sang nước ngoài để xét xử hoặc thi hành hình phạt, cùng nghĩa với dẫn độ. Hàn Quốc quy định bởi Luật dẫn độ, cần hiệp ước dẫn độ, có thể phạt ở cả hai nước, không dẫn độ tội phạm chính trị/quân sự, nguyên tắc không dẫn độ công dân, áp dụng nguyên tắc tội đặc biệt (chỉ phạt tội yêu cầu).",
            "context": "범죄인 인도 청구 및 심사 절차에서 사용",
            "culturalNote": "한국은 범죄인인도법을 1988년 제정했으며, 미국·일본·중국 등과 인도조약을 체결했습니다. 정치범 불인도 원칙으로 북한 이탈 주민을 중국이 북송하는 것은 난민 강제송환이지 범죄인 인도가 아닙니다. 자국민 불인도 원칙으로 한국인은 한국에서 재판받으며, 외국에 인도하지 않습니다. 베트남도 유사한 원칙을 따릅니다.",
            "commonMistakes": [
                {
                    "mistake": "giao tội phạm cho nước ngoài",
                    "correction": "dẫn độ tội phạm (법적 용어)",
                    "explanation": "'범죄자를 외국에 인계'는 설명이며 법률 용어로 '범죄인인도'가 정확합니다"
                },
                {
                    "mistake": "đưa về nước",
                    "correction": "dẫn độ tội phạm (청구국으로)",
                    "explanation": "'본국 송환'은 자국민 송환이며 외국 인도와 반대입니다"
                },
                {
                    "mistake": "trục xuất tội phạm",
                    "correction": "dẫn độ tội phạm (재판 목적)",
                    "explanation": "'범죄자 추방'은 강제퇴거이며 재판 목적 인도와 다릅니다"
                }
            ],
            "examples": [
                {
                    "ko": "한국은 자국민은 범죄인인도를 하지 않고 국내에서 재판합니다",
                    "vi": "Hàn Quốc không dẫn độ tội phạm công dân mà xét xử trong nước",
                    "situation": "formal"
                },
                {
                    "ko": "양국 모두 범죄여야 인도되나요?",
                    "vi": "Phải là tội ở cả hai nước mới dẫn độ à?",
                    "situation": "onsite"
                },
                {
                    "ko": "범죄인인도는 쌍방가벌성 원칙이 적용됩니다",
                    "vi": "Dẫn độ tội phạm áp dụng nguyên tắc có thể phạt ở cả hai bên",
                    "situation": "formal"
                }
            ],
            "relatedTerms": ["인도조약", "쌍방가벌성", "정치범불인도", "자국민불인도"]
        },
        {
            "slug": "truy-na-quoc-te",
            "korean": "국제수배",
            "vietnamese": "Truy nã quốc tế",
            "hanja": "國際手配",
            "hanjaReading": "國(나라 국) + 際(사이 제) + 手(손 수) + 配(나눌 배)",
            "pronunciation": "국제수배",
            "meaningKo": "국제형사경찰기구(인터폴)를 통해 범죄인을 전 세계에 수배하는 제도입니다. 통역 시 적색수배(체포·인도 목적)가 가장 강력하며, 청색수배(소재 파악), 녹색수배(상습범 경고) 등 7가지가 있고, 인터폴 회원국은 협조 의무가 있으며, 정치적 수배는 금지되고, 북한 김정은도 수배 대상으로 제기된다는 점을 명확히 전달해야 합니다.",
            "meaningVi": "Chế độ truy nã tội phạm toàn cầu qua Tổ chức Cảnh sát hình sự quốc tế (Interpol). Truy nã đỏ (mục đích bắt/dẫn độ) mạnh nhất, có 7 loại như truy nã xanh (xác định vị trí), truy nã xanh lá (cảnh báo tội phạm thường xuyên), nước thành viên Interpol có nghĩa vụ hợp tác, cấm truy nã chính trị, Kim Jong-un Triều Tiên cũng được đề xuất làm đối tượng truy nã.",
            "context": "국제범죄 수사 및 도주범 체포 상황에서 사용",
            "culturalNote": "한국은 인터폴 회원국이며, 보이스피싱 조직·해외 도피 경제사범 등을 적색수배합니다. 조선족 조직범죄는 중국과 협력하여 수배하며, 미국 FBI 10대 수배범처럼 인터폴 수배도 전 세계에 공개됩니다. 북한 김정은은 인권 침해로 수배 요구가 있으나 정치적 이유로 기각되었습니다. 베트남도 인터폴 회원국입니다.",
            "commonMistakes": [
                {
                    "mistake": "lệnh truy nã toàn cầu",
                    "correction": "truy nã quốc tế (인터폴 통해)",
                    "explanation": "'전 세계 수배령'은 일반 표현이며 인터폴 통한 공식 수배 개념이 약화됩니다"
                },
                {
                    "mistake": "Interpol truy bắt",
                    "correction": "truy nã quốc tế (qua Interpol)",
                    "explanation": "'인터폴 체포'는 인터폴이 직접 체포하는 것처럼 오해되며 수배의 의미가 누락됩니다"
                },
                {
                    "mistake": "tìm kiếm quốc tế",
                    "correction": "truy nã quốc tế (범죄인 수배)",
                    "explanation": "'국제 수색'은 일반 수색이며 범죄인 수배의 법적 성격이 약화됩니다"
                }
            ],
            "examples": [
                {
                    "ko": "한국은 인터폴을 통해 해외 도피 사기범을 적색수배했습니다",
                    "vi": "Hàn Quốc đã truy nã đỏ quốc tế kẻ lừa đảo trốn ra nước ngoài qua Interpol",
                    "situation": "formal"
                },
                {
                    "ko": "적색수배되면 어느 나라에서나 체포되나요?",
                    "vi": "Nếu bị truy nã đỏ, ở nước nào cũng bắt à?",
                    "situation": "onsite"
                },
                {
                    "ko": "국제수배는 인터폴 회원국의 협조로 범죄인을 체포합니다",
                    "vi": "Truy nã quốc tế bắt tội phạm bằng hợp tác nước thành viên Interpol",
                    "situation": "formal"
                }
            ],
            "relatedTerms": ["인터폴", "적색수배", "청색수배", "국제협력"]
        },
        {
            "slug": "tham-quyen-toan-cau",
            "korean": "보편적관할권",
            "vietnamese": "Thẩm quyền toàn cầu",
            "hanja": "普遍的管轄權",
            "hanjaReading": "普(넓을 보) + 遍(두루 편) + 的(과녁 적) + 管(대롱 관) + 轄(다스릴 할) + 權(권리 권)",
            "pronunciation": "보편적관할권",
            "meaningKo": "집단학살·고문·해적행위 등 인류 전체에 대한 범죄는 범행지·범인 국적과 무관하게 어느 나라든 재판할 수 있는 관할권입니다. 통역 시 전쟁범죄·인도에 반한 죄·노예제 등이 대상이며, 범죄인이 자국에 있으면 재판·인도 의무가 있고, 벨기에·스페인이 적극 활용했으나 외교 마찰로 축소되었다는 점을 명확히 전달해야 합니다.",
            "meaningVi": "Thẩm quyền bất kỳ nước nào cũng có thể xét xử tội phạm chống lại toàn nhân loại như diệt chủng, tra tấn, hành vi hải tặc bất kể nơi phạm tội và quốc tịch tội phạm. Đối tượng là tội phạm chiến tranh, tội chống lại nhân loại, chế độ nô lệ, nếu tội phạm ở trong nước có nghĩa vụ xét xử/dẫn độ, Bỉ và Tây Ban Nha sử dụng tích cực nhưng bị thu hẹp do ma sát ngoại giao.",
            "context": "국제범죄 재판 관할권 논의 및 기소 상황에서 사용",
            "culturalNote": "한국은 보편적 관할권을 제한적으로 인정하며, 해적행위처벌법으로 소말리아 해적을 재판한 사례가 있습니다. 벨기에는 르완다 집단학살 범인을 재판했고, 스페인은 칠레 피노체트를 기소했으나 외교 마찰로 철회했습니다. 북한 전쟁범죄도 보편적 관할권으로 재판 가능하다는 주장이 있습니다. 베트남은 보편적 관할권 개념이 없어 통역 시 설명이 필요합니다.",
            "commonMistakes": [
                {
                    "mistake": "thẩm quyền quốc tế",
                    "correction": "thẩm quyền toàn cầu (보편적)",
                    "explanation": "'국제 관할권'은 모호하며 모든 국가가 행사할 수 있는 보편성이 누락됩니다"
                },
                {
                    "mistake": "quyền xét xử toàn thế giới",
                    "correction": "thẩm quyền toàn cầu (법적 용어)",
                    "explanation": "'전 세계 재판권'은 일상 표현이며 법률 용어로 부적절합니다"
                },
                {
                    "mistake": "tài phán phổ quát",
                    "correction": "thẩm quyền toàn cầu (관할권)",
                    "explanation": "'보편 재판'은 직역이며 '보편적 관할권'이 정확합니다"
                }
            ],
            "examples": [
                {
                    "ko": "한국은 보편적 관할권으로 소말리아 해적을 재판했습니다",
                    "vi": "Hàn Quốc đã xét xử cướp biển Somalia theo thẩm quyền toàn cầu",
                    "situation": "formal"
                },
                {
                    "ko": "외국인이 외국에서 범죄를 저질러도 재판할 수 있나요?",
                    "vi": "Người nước ngoài phạm tội ở nước ngoài cũng có thể xét xử à?",
                    "situation": "onsite"
                },
                {
                    "ko": "보편적 관할권은 인류 전체에 대한 범죄에 적용됩니다",
                    "vi": "Thẩm quyền toàn cầu áp dụng cho tội phạm chống lại toàn nhân loại",
                    "situation": "formal"
                }
            ],
            "relatedTerms": ["집단학살", "전쟁범죄", "해적행위", "국제관할"]
        }
    ]
    return terms

def main():
    data, file_path = load_existing_terms()
    existing_slugs = {t['slug'] for t in data}
    new_terms = create_legal_terms()
    filtered = [t for t in new_terms if t['slug'] not in existing_slugs]
    data.extend(filtered)
    with open(file_path, 'w', encoding='utf-8') as f:
        json.dump(data, f, ensure_ascii=False, indent=2)
    print(f"✅ Added {len(filtered)} terms (국제형사법). Total: {len(data)}")

if __name__ == '__main__':
    main()
