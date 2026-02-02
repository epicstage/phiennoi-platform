#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
상법/기업법 (Commercial Law/Corporate Law) 용어 추가 스크립트
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

# 새로운 용어 정의
new_terms = [
    {
        "slug": "cong-ty-tnhh",
        "korean": "유한회사",
        "vietnamese": "công ty TNHH",
        "hanja": "有限會社",
        "hanjaReading": "有(있을 유) 限(한정할 한) 會(모일 회) 社(모일 사)",
        "pronunciation": "꽁 띠 떼엔한쩨뜨이엔",
        "meaningKo": "출자자의 책임이 출자액으로 제한되는 회사 형태. 베트남에서는 TNHH(Trách nhiệm hữu hạn)로 표기하며, 한국의 유한회사와 유사하나 베트남 기업법상 가장 흔한 외국인 투자 형태입니다. 통역 시 주의할 점은 베트남의 TNHH는 1인 유한회사(TNHH MTV)와 2인 이상 유한회사(TNHH 2TV)로 구분되므로, 한국의 단순 유한회사 개념과 혼동하지 않도록 정확히 구분해야 합니다. 계약서 통역 시 출자 비율, 의결권 구조를 명확히 확인하세요.",
        "meaningVi": "Loại hình công ty mà trách nhiệm của thành viên được giới hạn trong phạm vi số vốn góp vào công ty. Đây là loại hình phổ biến nhất cho doanh nghiệp có vốn đầu tư nước ngoài (FDI) tại Việt Nam theo Luật Doanh nghiệp. Có hai loại: TNHH MTV (một thành viên) và TNHH hai thành viên trở lên.",
        "context": "계약서, 법인 설립, 투자 협상",
        "culturalNote": "한국에서는 주식회사가 더 선호되지만, 베트남에서는 유한회사(TNHH)가 외국인 투자 기업의 약 70% 이상을 차지합니다. 베트남에서는 설립이 상대적으로 간단하고 자본금 요건이 유연하며, 이사회 구성이 필수가 아니라는 장점 때문입니다. 한국 투자자들이 베트남에 법인 설립 시 대부분 TNHH MTV(1인 유한회사)를 선택합니다.",
        "commonMistakes": [
            {
                "mistake": "TNHH를 '티엔에이치'로 발음",
                "correction": "떼엔한쩨뜨이엔으로 정확히 발음",
                "explanation": "베트nam어 약어는 각 글자를 정확히 발음해야 전문성이 드러남"
            },
            {
                "mistake": "한국의 유한회사와 완전히 동일한 개념으로 설명",
                "correction": "베트남 기업법상 TNHH의 특성(1인/2인 이상 구분)을 명확히 설명",
                "explanation": "법체계가 다르므로 단순 대응이 아닌 제도적 차이 인식 필요"
            },
            {
                "mistake": "공티를 '회사'로만 번역",
                "correction": "문맥에 따라 유한회사/주식회사/법인 등 정확한 형태 명시",
                "explanation": "베트남어 công ty는 포괄적 의미이므로 법적 형태를 명확히 구분"
            }
        ],
        "examples": [
            {
                "ko": "저희는 베트남에 유한회사 형태로 법인을 설립하려고 합니다.",
                "vi": "Chúng tôi dự định thành lập pháp nhân dưới hình thức công ty TNHH tại Việt Nam.",
                "situation": "formal"
            },
            {
                "ko": "1인 유한회사와 2인 이상 유한회사의 의결권 구조가 어떻게 다른가요?",
                "vi": "Cơ cấu quyền biểu quyết của công ty TNHH MTV và công ty TNHH hai thành viên trở lên khác nhau như thế nào?",
                "situation": "formal"
            },
            {
                "ko": "유한회사 정관에 출자 비율이 명시되어 있습니다.",
                "vi": "Tỷ lệ góp vốn được quy định rõ trong điều lệ công ty TNHH.",
                "situation": "onsite"
            }
        ],
        "relatedTerms": ["cong-ty-co-phan", "von-dieu-le", "dieu-le-cong-ty", "thanh-vien-gop-von"]
    },
    {
        "slug": "cong-ty-co-phan",
        "korean": "주식회사",
        "vietnamese": "công ty cổ phần",
        "hanja": "株式會社",
        "hanjaReading": "株(그루 주) 式(법 식) 會(모일 회) 社(모일 사)",
        "pronunciation": "꽁 띠 꼬 판",
        "meaningKo": "자본이 주식으로 나뉘고 주주의 책임이 출자액으로 제한되는 회사. 베트남에서는 '공띠꼬판'이라 하며, 최소 3명의 주주가 필요합니다(한국은 1인도 가능). 통역 시 주의할 점은 베트남 주식회사는 상장 여부와 무관하게 모두 '공띠꼬판'으로 불리므로, 한국식 '상장사/비상장사' 구분을 덧붙여 설명해야 혼동을 방지할 수 있습니다. IPO 관련 통역 시 베트남 증권법상 '공개회사(công ty đại chúng)' 개념도 함께 설명하세요.",
        "meaningVi": "Loại hình công ty có vốn điều lệ được chia thành nhiều cổ phần bằng nhau, cổ đông chịu trách nhiệm về các khoản nợ và nghĩa vụ tài sản khác của doanh nghiệp trong phạm vi số vốn đã góp vào doanh nghiệp. Theo Luật Doanh nghiệp Việt Nam, công ty cổ phần phải có ít nhất 03 cổ đông và không hạn chế số lượng tối đa.",
        "context": "상장, IPO, 기업 인수합병",
        "culturalNote": "한국에서는 1인 주식회사 설립이 가능하지만, 베트남은 반드시 3인 이상의 주주가 필요합니다. 이는 베트남이 집단주의 문화와 상호 견제 시스템을 중요시하기 때문입니다. 또한 베트남에서는 국영기업의 민영화(cổ phần hóa) 과정에서 주식회사 형태가 많이 사용되므로, '꼬판화'라는 용어가 민영화와 동의어처럼 쓰이기도 합니다.",
        "commonMistakes": [
            {
                "mistake": "상장사만 주식회사로 번역",
                "correction": "비상장 주식회사도 công ty cổ phần",
                "explanation": "베트남에서는 상장 여부와 무관하게 주식으로 나뉜 회사는 모두 공띠꼬판"
            },
            {
                "mistake": "한국처럼 1인 주식회사 가능하다고 설명",
                "correction": "베트남은 최소 3인 주주 필요",
                "explanation": "법적 요건이 다르므로 정확한 정보 전달 필수"
            },
            {
                "mistake": "cổ phần을 '고판'으로 발음",
                "correction": "'꼬판'으로 정확히 발음",
                "explanation": "ổ는 'ㅗ' 발음이며 성조에 주의"
            }
        ],
        "examples": [
            {
                "ko": "우리 회사는 내년에 주식회사로 전환할 예정입니다.",
                "vi": "Công ty chúng tôi dự định chuyển đổi sang công ty cổ phần vào năm sau.",
                "situation": "formal"
            },
            {
                "ko": "주식회사는 최소 몇 명의 주주가 필요한가요?",
                "vi": "Công ty cổ phần cần tối thiểu bao nhiêu cổ đông?",
                "situation": "formal"
            },
            {
                "ko": "주주총회에서 이사회 구성원을 선임합니다.",
                "vi": "Đại hội đồng cổ đông bầu thành viên hội đồng quản trị.",
                "situation": "onsite"
            }
        ],
        "relatedTerms": ["co-dong", "hoi-dong-quan-tri", "co-phieu", "dai-hoi-dong-co-dong"]
    },
    {
        "slug": "von-dieu-le",
        "korean": "자본금",
        "vietnamese": "vốn điều lệ",
        "hanja": "資本金",
        "hanjaReading": "資(재물 자) 本(근본 본) 金(쇠 금)",
        "pronunciation": "번 지에우 레",
        "meaningKo": "회사 설립 시 정관에 기재된 자본의 총액. 베트남에서는 '번지에우레'라 하며, 한국과 달리 최저자본금 제도가 없어 1동(약 5원)으로도 설립 가능합니다. 다만 사업 분야(금융, 보험, 건설 등)에 따라 최저 자본금 요건이 별도로 존재합니다. 통역 시 주의할 점은 '번지에우레'는 정관상 자본금이며, 실제 납입된 자본은 '번곱(vốn góp)'이라고 구분되므로, 투자 계약서 통역 시 납입 일정(tiến độ góp vốn)과 함께 정확히 전달해야 합니다.",
        "meaningVi": "Tổng giá trị tài sản do các thành viên, cổ đông cam kết góp và ghi vào điều lệ công ty. Theo Luật Doanh nghiệp 2020, không quy định mức vốn điều lệ tối thiểu đối với hầu hết các loại hình doanh nghiệp, trừ các ngành nghề đặc thù như ngân hàng, bảo hiểm, chứng khoán.",
        "context": "법인 설립, 투자 계약, 증자/감자",
        "culturalNote": "한국은 2009년부터 최저자본금 제도를 폐지했지만 실무상 여전히 일정 규모 이상을 요구하는 경향이 있습니다. 반면 베트남은 법적으로 최저 한도가 없어 외국인 투자자들이 소액으로도 시장 진입이 가능합니다. 다만 투자등록증명서(IRC) 발급 시 사업 계획과 자본금의 합리성을 심사받으므로, 과도하게 적은 자본금은 승인이 거부될 수 있습니다.",
        "commonMistakes": [
            {
                "mistake": "vốn điều lệ를 '실제 납입 자본'으로 번역",
                "correction": "정관상 자본금(약정 자본)으로 정확히 구분",
                "explanation": "vốn điều lệ는 약정액이고, 실제 납입액은 vốn góp thực tế"
            },
            {
                "mistake": "한국처럼 최저자본금이 있다고 설명",
                "correction": "일반 기업은 최저 한도 없음, 단 특정 업종은 예외",
                "explanation": "법적 요건이 다르므로 업종별 차이 인지 필요"
            },
            {
                "mistake": "điều lệ를 '디에우 레'로 발음",
                "correction": "'지에우 레'로 정확히 발음",
                "explanation": "d는 북부 베트남어에서 'ㅈ' 또는 'ㅉ' 소리"
            }
        ],
        "examples": [
            {
                "ko": "정관상 자본금은 100억 동이며, 3년 내 전액 납입 예정입니다.",
                "vi": "Vốn điều lệ là 100 tỷ đồng và dự kiến góp đủ trong vòng 3 năm.",
                "situation": "formal"
            },
            {
                "ko": "자본금 증자를 위해 주주총회 결의가 필요합니다.",
                "vi": "Cần có nghị quyết của đại hội đồng cổ đông để tăng vốn điều lệ.",
                "situation": "formal"
            },
            {
                "ko": "이 업종은 최저 자본금 요건이 있나요?",
                "vi": "Ngành nghề này có quy định vốn điều lệ tối thiểu không?",
                "situation": "onsite"
            }
        ],
        "relatedTerms": ["von-gop", "tang-von", "giam-von", "dieu-le-cong-ty"]
    },
    {
        "slug": "co-dong",
        "korean": "주주",
        "vietnamese": "cổ đông",
        "hanja": "株主",
        "hanjaReading": "株(그루 주) 主(주인 주)",
        "pronunciation": "꼬 동",
        "meaningKo": "주식회사의 주식을 소유한 사람 또는 법인. 베트남에서는 '꼬동'이라 하며, 주주총회(đại hội đồng cổ đông)에서 의결권을 행사합니다. 통역 시 주의할 점은 베트남 기업법상 '지배주주(cổ đông chi phối)'와 '소액주주(cổ đông thiểu số)' 개념이 명확히 구분되므로, M&A 통역 시 지분율에 따른 권리 차이를 정확히 전달해야 합니다. 특히 51% 이상 보유 시 '지배주주', 65% 이상 시 정관 변경 가능, 75% 이상 시 합병/분할 결정 가능 등 임계점을 숙지하세요.",
        "meaningVi": "Cá nhân hoặc tổ chức sở hữu ít nhất một cổ phần của công ty cổ phần và được ghi tên trong sổ đăng ký cổ đông của công ty. Cổ đông có quyền tham dự và biểu quyết tại đại hội đồng cổ đông, quyền nhận cổ tức và các quyền khác theo quy định của pháp luật và điều lệ công ty.",
        "context": "주주총회, 배당, 의결권",
        "culturalNote": "한국에서는 주주 권리 보호가 상대적으로 약하고 대주주 중심 경영이 일반적이지만, 베트남은 2020년 기업법 개정으로 소액주주 보호 규정이 크게 강화되었습니다. 예를 들어 10% 이상 지분 보유 주주는 임시 주주총회 소집을 요구할 수 있으며, 5% 이상 보유 주주는 회사 장부 열람권이 있습니다. 한국 투자자들이 베트남 기업 인수 시 이러한 소액주주 권리를 간과하면 분쟁 위험이 있습니다.",
        "commonMistakes": [
            {
                "mistake": "모든 주주를 동일한 권리를 가진 것으로 설명",
                "correction": "지분율에 따라 권리가 명확히 구분됨",
                "explanation": "베트남 기업법은 지분율별 권리를 상세히 규정"
            },
            {
                "mistake": "cổ đông을 '고동'으로 발음",
                "correction": "'꼬동'으로 정확히 발음",
                "explanation": "성조 없는 cổ는 'ㅗ' 발음이며 đ는 'd' 소리"
            },
            {
                "mistake": "주주총회를 '주주회의'로 번역",
                "correction": "đại hội đồng cổ đông (주주총회)",
                "explanation": "법적 용어는 정확한 대응어 사용 필수"
            }
        ],
        "examples": [
            {
                "ko": "10% 이상 지분을 보유한 주주는 임시 주주총회 소집을 요구할 수 있습니다.",
                "vi": "Cổ đông sở hữu từ 10% cổ phần trở lên có quyền yêu cầu triệu tập đại hội đồng cổ đông bất thường.",
                "situation": "formal"
            },
            {
                "ko": "지배주주의 지분율은 얼마인가요?",
                "vi": "Tỷ lệ sở hữu của cổ đông chi phối là bao nhiêu?",
                "situation": "formal"
            },
            {
                "ko": "주주 명부에 등재되어야 의결권을 행사할 수 있습니다.",
                "vi": "Phải được ghi tên trong sổ đăng ký cổ đông mới có quyền biểu quyết.",
                "situation": "onsite"
            }
        ],
        "relatedTerms": ["cong-ty-co-phan", "co-phieu", "dai-hoi-dong-co-dong", "co-tuc"]
    },
    {
        "slug": "hoi-dong-quan-tri",
        "korean": "이사회",
        "vietnamese": "hội đồng quản trị",
        "hanja": "理事會",
        "hanjaReading": "理(다스릴 리) 事(일 사) 會(모일 회)",
        "pronunciation": "호이 동 꾸안 찌",
        "meaningKo": "주식회사에서 업무 집행을 결정하는 필수 기관. 베트남에서는 '호이동꾸안찌'라 하며, 주식회사는 반드시 이사회를 두어야 합니다(유한회사는 선택). 통역 시 주의할 점은 베트nam 이사회는 최소 3인, 최대 11인으로 구성되며(한국은 3인 이상만 규정), 이사 임기가 5년을 초과할 수 없다는 점입니다. 또한 베트남에서는 이사회 의장(chủ tịch HĐQT)과 총경리(giám đốc/tổng giám đốc)의 겸직이 제한되므로, 지배구조 통역 시 반드시 구분해야 합니다.",
        "meaningVi": "Cơ quan quản lý công ty, có toàn quyền nhân danh công ty để quyết định, thực hiện các quyền và nghĩa vụ của công ty không thuộc thẩm quyền của đại hội đồng cổ đông. HĐQT của công ty cổ phần có từ 3 đến 11 thành viên, nhiệm kỳ không quá 5 năm và có thể được bầu lại với số nhiệm kỳ không hạn chế.",
        "context": "기업 지배구조, 의사결정, 경영 감독",
        "culturalNote": "한국에서는 이사회가 형식적으로 운영되는 경우가 많고 대표이사에게 권한이 집중되지만, 베트남은 이사회 중심 경영이 법으로 강제됩니다. 특히 외국인 투자 기업의 경우 투자 비율에 따라 이사 수를 배분하므로, 한국 투자자가 51% 지분을 가져도 이사회에서 과반을 차지하지 못하면 실질적 경영권 행사가 어렵습니다. 이사회 의사록(biên bản họp HĐQT)이 법적 효력이 크므로 통역 시 정확성이 매우 중요합니다.",
        "commonMistakes": [
            {
                "mistake": "이사회를 '관리위원회'로 번역",
                "correction": "hội đồng quản trị (이사회)",
                "explanation": "법적 용어는 정확한 대응어 사용 필수"
            },
            {
                "mistake": "이사회 의장과 CEO를 동일 인물로 가정",
                "correction": "베트남은 겸직 제한, 별도 인물임을 명확히",
                "explanation": "한국과 달리 분리가 원칙"
            },
            {
                "mistake": "hội đồng을 '호이동'으로만 발음",
                "correction": "'호이 동'으로 띄어 발음",
                "explanation": "두 단어로 구성되어 있음"
            }
        ],
        "examples": [
            {
                "ko": "이사회는 분기별로 최소 1회 개최되어야 합니다.",
                "vi": "Hội đồng quản trị phải họp ít nhất mỗi quý một lần.",
                "situation": "formal"
            },
            {
                "ko": "이사회 의장과 총경리는 동일인이 겸직할 수 없습니다.",
                "vi": "Chủ tịch HĐQT và giám đốc không thể do cùng một người đảm nhiệm.",
                "situation": "formal"
            },
            {
                "ko": "이사회 결의는 과반 출석, 3분의 2 이상 찬성으로 통과됩니다.",
                "vi": "Nghị quyết HĐQT được thông qua khi có ít nhất quá bán số thành viên dự họp tán thành.",
                "situation": "onsite"
            }
        ],
        "relatedTerms": ["chu-tich-hdqt", "giam-doc-dieu-hanh", "thanh-vien-hdqt", "dai-hoi-dong-co-dong"]
    },
    {
        "slug": "giam-doc-dieu-hanh",
        "korean": "대표이사",
        "vietnamese": "giám đốc điều hành",
        "hanja": "代表理事",
        "hanjaReading": "代(대신할 대) 表(나타낼 표) 理(다스릴 리) 事(일 사)",
        "pronunciation": "잠 독 지에우 한",
        "meaningKo": "회사의 일상 업무를 집행하고 대외적으로 회사를 대표하는 사람. 베트남에서는 '잠독지에우한' 또는 단순히 '잠독(giám đốc)' 또는 '총잠독(tổng giám đốc, 총경리)'이라 합니다. 통역 시 주의할 점은 베트남에서는 이사회 의장(chủ tịch HĐQT)과 대표이사(giám đốc)가 반드시 분리되어야 하므로(한국은 겸직 가능), 한국식 '대표이사 겸 이사회 의장' 개념을 그대로 번역하면 법적 오류가 됩니다. 계약서 서명 시 giám đốc 명의로 해야 법적 효력이 있습니다.",
        "meaningVi": "Người điều hành công việc kinh doanh hàng ngày của công ty, chịu trách nhiệm trước hội đồng quản trị và trước pháp luật về việc thực hiện các quyền và nghĩa vụ của mình. Giám đốc hoặc Tổng giám đốc phải là cá nhân, có thể là thành viên HĐQT hoặc được thuê từ bên ngoài, và không được đồng thời làm Chủ tịch HĐQT theo quy định pháp luật hiện hành.",
        "context": "법인 대표, 계약 서명, 일상 업무",
        "culturalNote": "한국에서는 대표이사가 최고 경영자(CEO)이자 이사회 의장을 겸하는 경우가 많아 권한이 집중되지만, 베트남은 권력 분산을 위해 이사회 의장(전략/감독)과 대표이사(집행)를 분리합니다. 이는 베트남이 과거 국영기업 체제에서 당 서기와 사장을 분리했던 관행이 민간 기업법에도 반영된 것입니다. 한국 기업이 베트남 자회사 설립 시 한국인 대표를 의장과 사장 겸직시키려다 법적 문제가 생기는 사례가 많습니다.",
        "commonMistakes": [
            {
                "mistake": "giám đốc를 '이사'로 번역",
                "correction": "대표이사 또는 총경리로 번역",
                "explanation": "giám đốc는 대표 집행 임원이지 단순 이사가 아님"
            },
            {
                "mistake": "chủ tịch HĐQT와 giám đốc를 동일인으로 가정",
                "correction": "법적으로 분리 필수",
                "explanation": "베트남 기업법상 겸직 금지"
            },
            {
                "mistake": "'지암독'으로 발음",
                "correction": "'잠독'으로 정확히 발음",
                "explanation": "gi는 북부에서 'ㅈ' 또는 'ㅉ' 소리"
            }
        ],
        "examples": [
            {
                "ko": "대표이사는 이사회 결의에 따라 회사를 경영합니다.",
                "vi": "Giám đốc điều hành công ty theo nghị quyết của HĐQT.",
                "situation": "formal"
            },
            {
                "ko": "계약서에 대표이사 서명이 필요합니다.",
                "vi": "Hợp đồng cần có chữ ký của giám đốc.",
                "situation": "formal"
            },
            {
                "ko": "대표이사와 이사회 의장은 다른 사람이어야 합니다.",
                "vi": "Giám đốc và chủ tịch HĐQT phải là hai người khác nhau.",
                "situation": "onsite"
            }
        ],
        "relatedTerms": ["hoi-dong-quan-tri", "chu-tich-hdqt", "tong-giam-doc", "nguoi-dai-dien-phap-luat"]
    },
    {
        "slug": "dieu-le-cong-ty",
        "korean": "정관",
        "vietnamese": "điều lệ công ty",
        "hanja": "定款",
        "hanjaReading": "定(정할 정) 款(조목 관)",
        "pronunciation": "지에우 레 꽁 띠",
        "meaningKo": "회사의 조직과 운영에 관한 기본 규칙을 정한 문서. 베트남에서는 '지에우레꽁띠'라 하며, 회사 설립 시 필수 서류입니다. 통역 시 주의할 점은 베트남 정관은 기업법에서 정한 필수 기재사항(22개 항목)을 반드시 포함해야 하며, 한국보다 훨씬 상세한 내용을 요구합니다. 특히 출자 비율, 의결권 구조, 이익 배분 방식, 이사회 구성, 분쟁 해결 절차 등을 명확히 기재해야 하므로, 정관 번역 시 베트남 기업법 조문을 참조하여 누락 없이 통역하세요.",
        "meaningVi": "Văn bản pháp lý quy định về tổ chức và hoạt động của công ty, bao gồm các nội dung bắt buộc theo quy định của Luật Doanh nghiệp như: tên công ty, địa chỉ trụ sở, mục tiêu và ngành nghề kinh doanh, vốn điều lệ, quyền và nghĩa vụ của thành viên/cổ đông, cơ cấu tổ chức quản lý, phương thức giải quyết tranh chấp nội bộ. Điều lệ có hiệu lực ràng buộc đối với công ty và toàn thể thành viên, cổ đông.",
        "context": "법인 설립, 정관 변경, M&A",
        "culturalNote": "한국에서는 정관이 형식적인 경우가 많고 실제 운영은 주주간 계약서(SHA)로 정하지만, 베트남은 정관이 최우선 법률 문서이며 주주간 합의가 정관과 충돌하면 무효입니다. 따라서 한국 투자자들이 베트남 합작 투자 시 정관에 모든 중요 사항을 명시하지 않고 별도 계약에만 의존하면, 나중에 분쟁 시 법적 보호를 받지 못합니다. 정관 변경은 주주총회 65% 이상 찬성이 필요하므로 초기 작성이 매우 중요합니다.",
        "commonMistakes": [
            {
                "mistake": "정관을 '회사 규정'으로 번역",
                "correction": "điều lệ công ty (정관)",
                "explanation": "법적 용어는 정확한 대응어 사용 필수"
            },
            {
                "mistake": "주주간 계약서와 정관을 동일시",
                "correction": "정관이 최우선, 주주간 계약은 정관 범위 내에서만 유효",
                "explanation": "베트남 법체계상 정관이 우선"
            },
            {
                "mistake": "điều lệ를 '디에우레'로 발음",
                "correction": "'지에우레'로 정확히 발음",
                "explanation": "d는 북부에서 'ㅈ' 또는 'ㅉ' 소리"
            }
        ],
        "examples": [
            {
                "ko": "정관 변경을 위해서는 주주총회 특별 결의가 필요합니다.",
                "vi": "Để sửa đổi điều lệ công ty cần có nghị quyết đặc biệt của đại hội đồng cổ đông.",
                "situation": "formal"
            },
            {
                "ko": "정관에 명시되지 않은 사항은 기업법을 따릅니다.",
                "vi": "Những vấn đề không được quy định trong điều lệ sẽ tuân theo Luật Doanh nghiệp.",
                "situation": "formal"
            },
            {
                "ko": "정관 초안을 법무팀에서 검토 중입니다.",
                "vi": "Bộ phận pháp lý đang xem xét dự thảo điều lệ công ty.",
                "situation": "onsite"
            }
        ],
        "relatedTerms": ["von-dieu-le", "dai-hoi-dong-co-dong", "sua-doi-dieu-le", "luat-doanh-nghiep"]
    },
    {
        "slug": "pha-san",
        "korean": "파산",
        "vietnamese": "phá sản",
        "hanja": "破産",
        "hanjaReading": "破(깨뜨릴 파) 産(낳을 산)",
        "pronunciation": "파 산",
        "meaningKo": "채무자가 채무를 변제할 능력이 없을 때 법원의 선고를 받아 재산을 청산하는 절차. 베트남에서는 '파산'이라 하며(한자 차용), 2014년 파산법(Luật Phá sản)에 따라 진행됩니다. 통역 시 주의할 점은 베트남은 파산 절차가 한국보다 훨씬 복잡하고 시간이 오래 걸리며(평균 5년), 채권자 보호가 약하다는 점입니다. 또한 베트남에서는 '기업 회생(tái cơ cấu doanh nghiệp)'과 '파산 청산(thanh lý phá sản)'이 명확히 구분되므로, 한국의 회생/파산 개념과 대응시킬 때 정확히 구분해야 합니다.",
        "meaningVi": "Trạng thái pháp lý của doanh nghiệp, hợp tác xã, cá nhân không có khả năng thanh toán các khoản nợ đã đến hạn theo quy định của Luật Phá sản. Thủ tục phá sản bao gồm các biện pháp: hòa giải phá sản, tái cơ cấu doanh nghiệp, hoặc thanh lý tài sản để thanh toán nợ. Tòa án nhân dân có thẩm quyền mở thủ tục phá sản theo đơn yêu cầu của chủ nợ hoặc doanh nghiệp.",
        "context": "채무 불이행, 기업 청산, 법원 절차",
        "culturalNote": "한국에서는 파산이 비교적 신속하게 진행되고 재기 문화도 형성되어 있지만, 베트남은 파산에 대한 사회적 낙인이 크고 법적 절차도 매우 복잡합니다. 베트남에서는 파산 선고를 받으면 기업 대표자가 출국 금지될 수 있고, 형사 책임까지 물을 수 있어 한국보다 훨씬 엄격합니다. 외국인 투자 기업의 경우 파산 절차 중 투자등록증명서(IRC) 회수 절차도 병행되므로 더욱 복잡합니다.",
        "commonMistakes": [
            {
                "mistake": "회생과 파산을 구분하지 않고 모두 phá sản으로 번역",
                "correction": "회생은 tái cơ cấu, 파산은 phá sản/thanh lý",
                "explanation": "법적 절차가 완전히 다름"
            },
            {
                "mistake": "파산 절차가 한국처럼 빠르다고 설명",
                "correction": "베트남은 평균 5년 소요, 매우 복잡",
                "explanation": "법체계와 절차가 다름"
            },
            {
                "mistake": "phá sản을 '파상'으로 발음",
                "correction": "'파산'으로 정확히 발음",
                "explanation": "베트남어 차용어지만 한자음과 동일"
            }
        ],
        "examples": [
            {
                "ko": "회사가 파산 신청을 법원에 제출했습니다.",
                "vi": "Công ty đã nộp đơn yêu cầu mở thủ tục phá sản lên tòa án.",
                "situation": "formal"
            },
            {
                "ko": "파산 절차에서 채권자들이 우선 변제를 받습니다.",
                "vi": "Trong thủ tục phá sản, các chủ nợ được thanh toán theo thứ tự ưu tiên.",
                "situation": "formal"
            },
            {
                "ko": "기업 회생 절차로 전환할 수 있나요?",
                "vi": "Có thể chuyển sang thủ tục tái cơ cấu doanh nghiệp không?",
                "situation": "onsite"
            }
        ],
        "relatedTerms": ["thanh-ly-tai-san", "tai-co-cau-doanh-nghiep", "chu-no", "no-phai-tra"]
    },
    {
        "slug": "sap-nhap",
        "korean": "합병",
        "vietnamese": "sáp nhập",
        "hanja": "合倂",
        "hanjaReading": "合(합할 합) 倂(아울러 병)",
        "pronunciation": "삽 냅",
        "meaningKo": "두 개 이상의 회사가 하나로 통합되는 행위. 베트남에서는 '삽냅'이라 하며, 흡수합병(sáp nhập hấp thụ)과 신설합병(sáp nhập mới)으로 구분됩니다. 통역 시 주의할 점은 베트남 합병은 주주총회 75% 이상 찬성이 필요하고(한국은 2/3), 노동자 대표 의견 청취가 법적으로 의무화되어 있으며, 채권자 보호 절차(공고 후 이의 제기 기간 45일)가 까다롭습니다. M&A 통역 시 세법상 혜택(면세, 이월 손실 승계 등) 조건을 정확히 전달하세요.",
        "meaningVi": "Hình thức tổ chức lại doanh nghiệp theo đó một hoặc một số doanh nghiệp (gọi là doanh nghiệp bị sáp nhập) chuyển toàn bộ tài sản, quyền, nghĩa vụ và lợi ích hợp pháp sang một doanh nghiệp khác (gọi là doanh nghiệp nhận sáp nhập) hoặc hình thành doanh nghiệp mới (sáp nhập mới). Doanh nghiệp bị sáp nhập chấm dứt tồn tại sau khi hoàn tất thủ tục sáp nhập theo quy định của Luật Doanh nghiệp.",
        "context": "M&A, 기업 구조조정, 시장 통합",
        "culturalNote": "한국에서는 합병이 주주와 경영진 중심으로 신속하게 진행되지만, 베트남은 노동자 대표 의견 청취가 법적 의무이며, 노동조합(công đoàn)의 영향력이 큽니다. 특히 국영기업 민영화 합병의 경우 정부 승인 절차가 추가되어 더욱 복잡합니다. 한국 기업이 베트남 기업 인수 후 합병 시 노동자 권리 침해 시비로 분쟁이 생기는 사례가 많으므로, 통역 시 노동법 관련 설명을 빠뜨리지 마세요.",
        "commonMistakes": [
            {
                "mistake": "합병과 인수를 구분하지 않고 모두 sáp nhập으로 번역",
                "correction": "합병은 sáp nhập, 인수는 mua lại/thâu tóm",
                "explanation": "법적 성격이 완전히 다름"
            },
            {
                "mistake": "노동자 의견 청취 절차를 생략하고 설명",
                "correction": "베트남은 노동자 대표 의견 청취 법적 의무",
                "explanation": "절차 누락 시 합병 무효 위험"
            },
            {
                "mistake": "sáp nhập을 '삽닙'으로 발음",
                "correction": "'삽냅'으로 정확히 발음",
                "explanation": "nhập의 p는 약하게 발음"
            }
        ],
        "examples": [
            {
                "ko": "두 회사의 합병은 주주총회 75% 이상 찬성으로 승인되었습니다.",
                "vi": "Sáp nhập hai công ty đã được phê duyệt với hơn 75% số phiếu tán thành tại đại hội đồng cổ đông.",
                "situation": "formal"
            },
            {
                "ko": "합병 공고 후 채권자가 이의를 제기할 수 있습니다.",
                "vi": "Sau khi thông báo sáp nhập, chủ nợ có quyền phản đối.",
                "situation": "formal"
            },
            {
                "ko": "흡수합병 후 존속 회사가 모든 권리와 의무를 승계합니다.",
                "vi": "Sau sáp nhập hấp thụ, doanh nghiệp nhận sáp nhập kế thừa toàn bộ quyền và nghĩa vụ.",
                "situation": "onsite"
            }
        ],
        "relatedTerms": ["mua-lai-doanh-nghiep", "chia-tach", "chuyen-doi-loai-hinh", "to-chuc-lai"]
    },
    {
        "slug": "co-phieu",
        "korean": "주식",
        "vietnamese": "cổ phiếu",
        "hanja": "株式",
        "hanjaReading": "株(그루 주) 式(법 식)",
        "pronunciation": "꼬 피에우",
        "meaningKo": "주식회사의 자본을 구성하는 단위로, 주주의 권리와 의무를 나타내는 증권. 베트남에서는 '꼬피에우'라 하며, 기명식만 인정됩니다(무기명 불가). 통역 시 주의할 점은 베트남은 주식 양도 시 반드시 회사와 다른 주주들에게 우선매수권(quyền ưu tiên mua)을 부여해야 하며(정관에 달리 규정하지 않는 한), 주식 양도는 회사 주식 명부(sổ đăng ký cổ đông)에 등재되어야 효력이 발생합니다. 상장 주식과 비상장 주식의 양도 절차가 완전히 다르므로 명확히 구분하세요.",
        "meaningVi": "Chứng chỉ do công ty cổ phần phát hành, bút toán ghi sổ hoặc dữ liệu điện tử xác nhận quyền sở hữu một hoặc một số cổ phần của công ty đó. Mỗi cổ phiếu đại diện cho một cổ phần, cổ đông sở hữu cổ phiếu có các quyền và nghĩa vụ tương ứng theo quy định của Luật Doanh nghiệp và điều lệ công ty. Cổ phiếu phải là cổ phiếu ghi danh và chỉ được chuyển nhượng cho người khác theo quy định pháp luật.",
        "context": "증권, 투자, 주식 거래",
        "culturalNote": "한국에서는 주식 거래가 활발하고 주식시장이 발달했지만, 베트남 증권시장은 아직 초기 단계이며 유동성이 낮습니다. 특히 비상장 주식의 경우 우선매수권 때문에 제3자에게 양도가 쉽지 않아, 한국 투자자들이 베트남 스타트업 투자 후 엑시트가 어려운 경우가 많습니다. 또한 베트남은 외국인 투자자의 주식 보유 한도(foreign ownership limit)가 업종별로 제한되어 있어(은행 30%, 항공 30% 등), M&A 통역 시 이를 반드시 확인해야 합니다.",
        "commonMistakes": [
            {
                "mistake": "cổ phiếu를 '고피에우'로 발음",
                "correction": "'꼬피에우'로 정확히 발음",
                "explanation": "cổ는 성조 없이 'ㅗ' 발음"
            },
            {
                "mistake": "주식 양도를 자유롭게 할 수 있다고 설명",
                "correction": "비상장 주식은 우선매수권 및 정관 제약",
                "explanation": "베트남은 주식 양도 제한이 엄격"
            },
            {
                "mistake": "무기명 주식 발행 가능하다고 설명",
                "correction": "베트남은 기명식만 인정",
                "explanation": "법적으로 무기명 주식 금지"
            }
        ],
        "examples": [
            {
                "ko": "주식 양도 시 다른 주주들에게 우선매수권이 있습니다.",
                "vi": "Khi chuyển nhượng cổ phiếu, các cổ đông khác có quyền ưu tiên mua.",
                "situation": "formal"
            },
            {
                "ko": "외국인 투자자의 주식 보유 한도는 얼마인가요?",
                "vi": "Tỷ lệ sở hữu nước ngoài đối với cổ phiếu là bao nhiêu?",
                "situation": "formal"
            },
            {
                "ko": "주식 명부에 등재되어야 주주 권리를 행사할 수 있습니다.",
                "vi": "Phải được ghi vào sổ đăng ký cổ đông mới có thể thực hiện quyền cổ đông.",
                "situation": "onsite"
            }
        ],
        "relatedTerms": ["co-dong", "cong-ty-co-phan", "so-dang-ky-co-dong", "chuyen-nhuong-co-phieu"]
    }
]

# 중복 제거
new_terms_filtered = [t for t in new_terms if t['slug'] not in existing_slugs]

print(f"기존 용어 수: {len(data)}")
print(f"추가할 용어 수: {len(new_terms_filtered)}")
print(f"중복 제외된 용어 수: {len(new_terms) - len(new_terms_filtered)}")

# 데이터 추가
data.extend(new_terms_filtered)

# 파일 저장
with open(file_path, 'w', encoding='utf-8') as f:
    json.dump(data, f, ensure_ascii=False, indent=2)

print(f"✅ 총 {len(data)}개 용어 저장 완료")
print("추가된 용어:")
for term in new_terms_filtered:
    print(f"  - {term['slug']} ({term['korean']} / {term['vietnamese']})")
