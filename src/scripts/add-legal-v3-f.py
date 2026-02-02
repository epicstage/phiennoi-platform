#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Add Local Government/Organization Law Terms to legal.json
Theme: 지방자치/조직법 (Local Government/Organization Law)
Tier S Quality: All fields complete, 200+ char meaningKo, 100+ char meaningVi/culturalNote
"""

import json
import os

# CRITICAL: Correct file path resolution
file_path = os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', 'data', 'terms', 'legal.json')

# Load existing data (data is a LIST, not dict!)
with open(file_path, 'r', encoding='utf-8') as f:
    data = json.load(f)

# Get existing slugs to prevent duplicates
existing_slugs = {t['slug'] for t in data}

# New terms: Local Government/Organization Law (10 terms)
new_terms = [
    {
        "slug": "uy-ban-nhan-dan",
        "korean": "인민위원회",
        "vietnamese": "Ủy ban nhân dân",
        "hanja": "人民委員會",
        "hanjaReading": "人(사람 인) + 民(백성 민) + 委(맡길 위) + 員(인원 원) + 會(모일 회)",
        "pronunciation": "우이 반 년 잔",
        "meaningKo": "베트남의 지방행정 집행기관으로, 한국의 '지방자치단체장 + 집행부'에 해당합니다. 통역 시 주의할 점은 베트남은 인민의회(입법)와 인민위원회(집행)가 명확히 분리되어 있으나, 한국은 지방의회와 단체장이 독립적으로 선출되는 구조라는 점입니다. '인민'이라는 용어 때문에 오해할 수 있으나 실제로는 일반적인 지방정부 집행기관이며, 실무에서는 '지방정부', '시/도청', '구청' 등으로 맥락에 따라 번역해야 합니다.",
        "meaningVi": "Cơ quan hành chính nhà nước ở địa phương, do Hội đồng nhân dân bầu ra. Ủy ban nhân dân chịu trách nhiệm trước Hội đồng nhân dân cùng cấp và cơ quan hành chính nhà nước cấp trên. Tổ chức và hoạt động theo nguyên tắc tập trung dân chủ.",
        "context": "베트남 헌법 및 지방자치법에서 규정하는 지방행정 집행기관",
        "culturalNote": "베트남의 인민위원회는 한국의 지방자치단체장과 달리 주민이 직접 선출하지 않고 인민의회가 선출합니다. 또한 집단지도체제로 운영되며 위원장(주석) 외에도 부위원장과 위원들이 있습니다. 한국은 단체장 1인 중심의 책임제인 반면, 베트남은 위원회 집단책임제입니다. 통역 시 '인민'이라는 용어가 주는 이념적 뉘앙스를 배제하고 중립적으로 설명해야 합니다.",
        "commonMistakes": [
            {
                "mistake": "인민위원회를 '시민위원회'로 번역",
                "correction": "인민위원회 또는 지방정부",
                "explanation": "'인민'은 베트남 정치 용어의 고유 표현이며, 자의적으로 '시민'으로 바꾸면 법적 정확성이 떨어집니다."
            },
            {
                "mistake": "한국의 지방의회와 동일시",
                "correction": "한국의 지방자치단체장(집행부)에 해당",
                "explanation": "인민위원회는 집행기관이고, 입법기관은 인민의회입니다."
            },
            {
                "mistake": "'People's Committee'를 '국민위원회'로 역번역",
                "correction": "인민위원회",
                "explanation": "베트남 법률 용어의 공식 한국어 표기는 '인민위원회'입니다."
            }
        ],
        "examples": [
            {
                "ko": "하노이시 인민위원회는 도시 개발 계획을 승인했습니다.",
                "vi": "Ủy ban nhân dân Thành phố Hà Nội đã phê duyệt kế hoạch phát triển đô thị.",
                "situation": "formal"
            },
            {
                "ko": "인민위원회 위원장님께 보고서를 제출해야 합니다.",
                "vi": "Chúng tôi phải trình báo cáo lên Chủ tịch Ủy ban nhân dân.",
                "situation": "formal"
            },
            {
                "ko": "구 인민위원회에서 사업 허가를 받았어요.",
                "vi": "Chúng tôi đã nhận giấy phép kinh doanh từ Ủy ban nhân dân quận.",
                "situation": "informal"
            }
        ],
        "relatedTerms": ["hoi-dong-nhan-dan", "tinh", "chu-tich-ubnd", "co-quan-hanh-chinh"]
    },
    {
        "slug": "hoi-dong-nhan-dan",
        "korean": "인민의회",
        "vietnamese": "Hội đồng nhân dân",
        "hanja": "人民議會",
        "hanjaReading": "人(사람 인) + 民(백성 민) + 議(의논할 의) + 會(모일 회)",
        "pronunciation": "호이 동 년 잔",
        "meaningKo": "베트남의 지방 입법기관으로, 한국의 '지방의회'에 해당합니다. 통역 시 주의할 점은 베트남 인민의회는 주민이 직접 선출하지만 정당 공천이 아닌 조국전선의 추천을 받는다는 점입니다. 한국은 정당 중심의 지방의회 선거를 실시합니다. 실무에서는 '지방의회', '시의회', '도의회' 등으로 맥락에 따라 번역하며, 베트남의 인민의회가 인민위원회를 선출하고 감독한다는 권력구조를 정확히 이해해야 합니다.",
        "meaningVi": "Cơ quan quyền lực nhà nước ở địa phương, do nhân dân địa phương bầu ra. Hội đồng nhân dân quyết định các vấn đề quan trọng của địa phương, bầu Ủy ban nhân dân và giám sát hoạt động của Ủy ban nhân dân.",
        "context": "베트남 헌법에서 규정하는 지방 입법 및 감독 기관",
        "culturalNote": "베트남 인민의회는 한국 지방의회와 달리 '의원내각제적' 특성이 있습니다. 인민의회가 인민위원회(집행부)를 선출하고 해임할 수 있는 권한을 가지며, 이는 한국의 지방의회가 단체장을 견제만 할 수 있는 것과 다릅니다. 또한 베트남은 단일정당(공산당) 체제이므로 야당이 없고, 조국전선이 후보를 추천합니다. 통역 시 이러한 정치체제 차이를 설명할 준비가 필요합니다.",
        "commonMistakes": [
            {
                "mistake": "인민의회를 '국회'로 번역",
                "correction": "인민의회 또는 지방의회",
                "explanation": "국회는 중앙의 국회(Quốc hội)이고, 인민의회는 지방의 의회입니다."
            },
            {
                "mistake": "한국 지방의회와 동일한 권한이라고 설명",
                "correction": "인민의회는 집행부(인민위원회)를 선출하고 해임하는 권한 보유",
                "explanation": "한국 지방의회는 단체장 견제만 가능하고 선출/해임 불가능"
            },
            {
                "mistake": "'의원'을 '대표(đại biểu)'로만 번역",
                "correction": "인민의회 의원 또는 대표",
                "explanation": "공식 용어는 '대표(đại biểu)'이지만 통역 시 '의원'으로 설명하는 것이 한국인에게 이해하기 쉽습니다."
            }
        ],
        "examples": [
            {
                "ko": "호치민시 인민의회가 새로운 조례를 통과시켰습니다.",
                "vi": "Hội đồng nhân dân Thành phố Hồ Chí Minh đã thông qua nghị quyết mới.",
                "situation": "formal"
            },
            {
                "ko": "인민의회 대표들이 예산안을 심의하고 있습니다.",
                "vi": "Các đại biểu Hội đồng nhân dân đang thẩm tra dự toán ngân sách.",
                "situation": "formal"
            },
            {
                "ko": "다음 주에 인민의회 회의가 열려요.",
                "vi": "Tuần sau sẽ có kỳ họp Hội đồng nhân dân.",
                "situation": "informal"
            }
        ],
        "relatedTerms": ["uy-ban-nhan-dan", "dai-bieu-hdnd", "nghi-quyet", "ky-hop-hdnd"]
    },
    {
        "slug": "tinh",
        "korean": "성",
        "vietnamese": "Tỉnh",
        "hanja": "省",
        "hanjaReading": "省(살필 성)",
        "pronunciation": "띤",
        "meaningKo": "베트남의 1급 지방행정구역으로, 한국의 '도(道)'에 해당합니다. 통역 시 주의할 점은 베트남은 '성(Tỉnh)'과 '중앙직할시(Thành phố trực thuộc trung ương)'를 구분한다는 점입니다. 한국은 '특별시/광역시/도/특별자치도'로 구분되며 인구와 경제 규모에 따라 등급이 나뉩니다. 베트남에서 '성'은 주로 지방 지역을 의미하며, 하노이·호치민·다낭·하이퐁·껀터 5개 도시는 성급 직할시로 분류됩니다. 실무 번역 시 '○○성' 또는 '○○도'로 표기합니다.",
        "meaningVi": "Đơn vị hành chính cấp tỉnh của Việt Nam, không bao gồm các thành phố trực thuộc trung ương. Tỉnh có Hội đồng nhân dân tỉnh và Ủy ban nhân dân tỉnh. Hiện Việt Nam có 58 tỉnh.",
        "context": "베트남 행정구역 체계에서 1급 지방행정단위",
        "culturalNote": "베트남의 '성(Tỉnh)'은 한국의 '도(道)'와 유사하지만 인구 규모는 훨씬 작습니다. 한국의 경기도가 1,300만 명인 반면, 베트남 대부분 성은 100~200만 명 수준입니다. 또한 베트남은 '중앙직할시'와 '성'이 동일한 행정등급이지만, 한국은 특별시·광역시가 도보다 높은 지위를 가집니다. 통역 시 한국인이 '성'을 중국의 '省'과 혼동할 수 있으므로, '베트남의 도 단위'라고 설명하는 것이 효과적입니다.",
        "commonMistakes": [
            {
                "mistake": "모든 Tỉnh을 '성'으로만 번역",
                "correction": "맥락에 따라 '도' 또는 '성'으로 번역",
                "explanation": "한국인에게는 '○○도'가 더 익숙하므로 문서 유형에 따라 조정 필요"
            },
            {
                "mistake": "Thành phố(시)도 Tỉnh에 포함된다고 설명",
                "correction": "중앙직할시는 Tỉnh과 별개의 동급 행정구역",
                "explanation": "하노이, 호치민 등은 'Thành phố trực thuộc trung ương'으로 Tỉnh이 아닙니다."
            },
            {
                "mistake": "'Tỉnh lỵ'를 '성청 소재지'로 번역",
                "correction": "도청 소재지 또는 성도",
                "explanation": "한국에서 '성청'은 사용하지 않고 '도청'이라고 합니다."
            }
        ],
        "examples": [
            {
                "ko": "박닌성 인민위원회가 투자 인센티브를 발표했습니다.",
                "vi": "Ủy ban nhân dân tỉnh Bắc Ninh đã công bố chính sách ưu đãi đầu tư.",
                "situation": "formal"
            },
            {
                "ko": "우리 회사는 빈증성에 공장을 건설할 계획입니다.",
                "vi": "Công ty chúng tôi có kế hoạch xây dựng nhà máy tại tỉnh Vĩnh Phúc.",
                "situation": "formal"
            },
            {
                "ko": "어느 성에서 오셨어요?",
                "vi": "Anh từ tỉnh nào đến?",
                "situation": "informal"
            }
        ],
        "relatedTerms": ["thanh-pho-truc-thuoc", "huyen", "xa", "don-vi-hanh-chinh"]
    },
    {
        "slug": "huyen",
        "korean": "현",
        "vietnamese": "Huyện",
        "hanja": "縣",
        "hanjaReading": "縣(고을 현)",
        "pronunciation": "후옌",
        "meaningKo": "베트남의 2급 지방행정구역으로, 한국의 '군(郡)'에 해당합니다. 통역 시 주의할 점은 베트남의 현(Huyện)은 성(Tỉnh) 아래 단위이며 주로 농촌 지역을 포함하는 반면, 도시 지역은 시사(Thị xã)나 시(Thành phố)로 분류된다는 점입니다. 한국의 군도 농촌 지역이지만 베트남보다 인구밀도가 높고 산업화된 경우가 많습니다. 실무에서는 '○○군' 또는 '○○현'으로 번역하며, 베트남 현의 하부에는 사(Xã, 면), 티쩐(Thị trấn, 읍)이 있습니다.",
        "meaningVi": "Đơn vị hành chính cấp huyện thuộc tỉnh, thường bao gồm các vùng nông thôn và thị trấn. Huyện có Hội đồng nhân dân huyện và Ủy ban nhân dân huyện. Dưới huyện là các xã, thị trấn.",
        "context": "베트남 행정구역 체계에서 2급 지방행정단위 (성/중앙직할시 산하)",
        "culturalNote": "베트남의 '현(Huyện)'은 한국의 '군(郡)'과 유사하지만, 베트남은 도시화가 진행되면 현이 '시사(Thị xã)' 또는 '시(Thành phố)'로 승격되는 체계입니다. 한국은 군이 시로 승격되면 완전히 다른 행정단위가 되지만, 베트남은 같은 2급 행정구역 내에서 등급 변화가 일어납니다. 또한 하노이, 호치민 같은 중앙직할시 내에도 '군(Quận, 도시형)'과 '현(Huyện, 농촌형)'이 공존합니다. 통역 시 이러한 차이를 명확히 설명해야 합니다.",
        "commonMistakes": [
            {
                "mistake": "모든 Huyện을 '군'으로 번역",
                "correction": "맥락에 따라 '군' 또는 '현'으로 번역",
                "explanation": "공식 문서에서는 '현'이 정확하지만, 한국인 이해를 위해 '군'을 쓸 수 있습니다."
            },
            {
                "mistake": "Quận(군)과 Huyện(현)을 같은 것으로 설명",
                "correction": "Quận은 도시형 2급 행정구역, Huyện은 농촌형",
                "explanation": "호치민시 내의 '1군(Quận 1)'과 '꾸찌현(Huyện Củ Chi)'은 다른 유형입니다."
            },
            {
                "mistake": "'Huyện lỵ'를 '현청'으로 번역",
                "correction": "군청 또는 현청 소재지",
                "explanation": "한국에서는 '군청'이 일반적이지만 베트남 공식 표기는 '현'입니다."
            }
        ],
        "examples": [
            {
                "ko": "자람현 인민위원회가 농업 개발 계획을 수립했습니다.",
                "vi": "Ủy ban nhân dân huyện Gia Lâm đã xây dựng kế hoạch phát triển nông nghiệp.",
                "situation": "formal"
            },
            {
                "ko": "빈현에 새로운 산업단지가 조성될 예정입니다.",
                "vi": "Khu công nghiệp mới sẽ được xây dựng tại huyện Bình.",
                "situation": "formal"
            },
            {
                "ko": "현청에 서류 제출하러 가야 해요.",
                "vi": "Tôi phải đi nộp hồ sơ ở Ủy ban nhân dân huyện.",
                "situation": "informal"
            }
        ],
        "relatedTerms": ["tinh", "xa", "thi-tran", "quan-do-thi"]
    },
    {
        "slug": "xa",
        "korean": "사",
        "vietnamese": "Xã",
        "hanja": "社",
        "hanjaReading": "社(모일 사)",
        "pronunciation": "싸",
        "meaningKo": "베트남의 3급 지방행정구역으로, 한국의 '면(面)'에 해당하는 농촌 지역 최하위 행정단위입니다. 통역 시 주의할 점은 베트남의 사(Xã)는 여러 개의 촌락(Thôn, 村)으로 구성되며, 한국의 면보다 인구가 적고 면적이 작다는 점입니다. 베트남은 사(Xã, 농촌), 푸엉(Phường, 도시형 동), 티쩐(Thị trấn, 읍)이 동일한 3급 행정구역이지만 성격이 다릅니다. 실무에서는 '○○사' 또는 '○○면'으로 번역하며, 사 단위에도 인민위원회가 구성됩니다.",
        "meaningVi": "Đơn vị hành chính cấp xã thuộc huyện, là đơn vị hành chính cơ sở ở nông thôn. Xã có Hội đồng nhân dân xã và Ủy ban nhân dân xã. Dưới xã là các thôn, ấp.",
        "context": "베트남 행정구역 체계에서 농촌형 3급 지방행정단위 (현 산하)",
        "culturalNote": "베트남의 '사(Xã)'는 한국의 '면(面)'과 유사하지만, 베트남에서는 사 단위에서도 인민의회와 인민위원회가 구성되어 정치적 권한을 가집니다. 한국의 면은 군청의 하부 행정조직일 뿐 독립적인 의결기관이 없습니다. 또한 베트남 농촌은 사(Xã) - 촌(Thôn) 체계로 이루어지며, 남부에서는 촌 대신 압(Ấp)이라는 명칭을 사용합니다. 통역 시 한국의 '리(里)' 개념과 베트남의 '촌(Thôn)' 개념이 유사하다고 설명하면 이해하기 쉽습니다.",
        "commonMistakes": [
            {
                "mistake": "Xã를 '마을'로 번역",
                "correction": "사(면) 또는 면",
                "explanation": "Xã는 행정구역이고, '마을'은 Thôn(촌) 또는 Làng(랑)입니다."
            },
            {
                "mistake": "Phường(도시 동)도 Xã로 번역",
                "correction": "Phường은 '동(洞)', Xã는 '면(面)'",
                "explanation": "둘 다 3급 행정구역이지만 Phường은 도시, Xã는 농촌입니다."
            },
            {
                "mistake": "'Xã hội'를 '사회'가 아닌 '사'로 번역",
                "correction": "Xã hội는 '사회(社會)'",
                "explanation": "행정구역 Xã(社)와 사회 Xã hội(社會)는 다른 단어입니다."
            }
        ],
        "examples": [
            {
                "ko": "딴트리사 인민위원회가 관개 시설 개선 사업을 추진합니다.",
                "vi": "Ủy ban nhân dân xã Tân Triều triển khai dự án cải tạo hệ thống thủy lợi.",
                "situation": "formal"
            },
            {
                "ko": "이 사에는 15개 촌락이 있습니다.",
                "vi": "Xã này có 15 thôn.",
                "situation": "formal"
            },
            {
                "ko": "사무소에 가서 호적 등본 떼야 해요.",
                "vi": "Tôi phải ra Ủy ban nhân dân xã làm giấy xác nhận hộ khẩu.",
                "situation": "informal"
            }
        ],
        "relatedTerms": ["huyen", "phuong-do-thi", "thi-tran", "thon-lang"]
    },
    {
        "slug": "thanh-pho-truc-thuoc",
        "korean": "직할시",
        "vietnamese": "Thành phố trực thuộc trung ương",
        "hanja": "直轄市",
        "hanjaReading": "直(곧을 직) + 轄(다스릴 할) + 市(저자 시)",
        "pronunciation": "타잉 포 쯕 투억 쯩 윙",
        "meaningKo": "베트남의 중앙정부 직할 도시로, 성(Tỉnh)과 동일한 1급 행정구역입니다. 통역 시 주의할 점은 한국의 '특별시·광역시'와 달리 베트남 직할시는 성(Tỉnh)과 법적 지위가 동등하다는 점입니다. 현재 하노이, 호치민, 다낭, 하이퐁, 껀터 5개 도시가 있으며, 한국의 특별시(서울)나 광역시(부산, 인천 등)처럼 인구 밀집 대도시입니다. 실무에서는 '중앙직할시', '직할시' 또는 '특별시'로 번역하며, 이들 도시는 국무총리 직속으로 관리됩니다.",
        "meaningVi": "Đơn vị hành chính cấp tỉnh, trực thuộc trung ương, do Chính phủ quản lý trực tiếp. Hiện có 5 thành phố: Hà Nội, Hồ Chí Minh, Đà Nẵng, Hải Phòng, Cần Thơ. Có quy mô dân số và kinh tế lớn.",
        "context": "베트남 헌법 및 행정구역법에서 규정하는 1급 중앙직할 도시",
        "culturalNote": "베트남의 중앙직할시는 한국의 특별시·광역시와 유사하지만, 법적 지위는 성(Tỉnh)과 완전히 동등합니다. 한국은 특별시가 도보다 상위 개념이지만, 베트남은 동등합니다. 또한 베트남 직할시 내부에도 '군(Quận, 도시형)'과 '현(Huyện, 농촌형)'이 혼재합니다. 예를 들어 하노이는 12개 군과 17개 현으로 구성됩니다. 한국의 서울특별시는 전역이 '구(區)'로만 이루어진 것과 대조적입니다. 통역 시 이러한 행정구조 차이를 설명해야 합니다.",
        "commonMistakes": [
            {
                "mistake": "모든 Thành phố를 '직할시'로 번역",
                "correction": "중앙직할시는 5개만 해당, 나머지는 '시'",
                "explanation": "성(Tỉnh) 산하에도 Thành phố(시)가 있으며, 이들은 직할시가 아닙니다."
            },
            {
                "mistake": "한국 특별시와 동일하게 최고 등급으로 설명",
                "correction": "베트남 직할시는 성(Tỉnh)과 동등한 1급 행정구역",
                "explanation": "한국은 특별시>광역시>도 순이지만 베트남은 직할시=성입니다."
            },
            {
                "mistake": "'직할시 산하 시(Thành phố thuộc)'를 '구'로 번역",
                "correction": "시급 도시(2급 행정구역)",
                "explanation": "호치민시 산하 '투득시'는 Quận(군)이 아니라 Thành phố(시)입니다."
            }
        ],
        "examples": [
            {
                "ko": "하노이 중앙직할시는 베트남의 수도입니다.",
                "vi": "Thành phố Hà Nội trực thuộc trung ương là thủ đô của Việt Nam.",
                "situation": "formal"
            },
            {
                "ko": "호치민시는 베트남 최대의 경제 중심지입니다.",
                "vi": "Thành phố Hồ Chí Minh là trung tâm kinh tế lớn nhất Việt Nam.",
                "situation": "formal"
            },
            {
                "ko": "다낭시가 직할시로 승격된 건 2004년이에요.",
                "vi": "Đà Nẵng được nâng lên thành phố trực thuộc trung ương năm 2004.",
                "situation": "informal"
            }
        ],
        "relatedTerms": ["tinh", "thanh-pho-cap-tinh", "quan-do-thi", "huyen"]
    },
    {
        "slug": "phan-cap-quan-ly",
        "korean": "권한 위임",
        "vietnamese": "Phân cấp quản lý",
        "hanja": "分級管理",
        "hanjaReading": "分(나눌 분) + 級(등급 급) + 管(대롱 관) + 理(다스릴 리)",
        "pronunciation": "판 껍 꾸안 리",
        "meaningKo": "중앙정부에서 지방정부로 행정권한을 이양하는 제도로, 한국의 '지방분권'과 유사합니다. 통역 시 주의할 점은 베트남은 중앙집권적 전통이 강해 권한 위임이 제한적이며, 주요 의사결정은 여전히 중앙정부와 공산당이 통제한다는 점입니다. 한국은 지방자치법에 따라 단체장과 지방의회를 주민이 직접 선출하지만, 베트남은 인민의회는 선출하되 인민위원회는 의회가 선출합니다. 실무에서는 '권한 위임', '분권화', '지방분권'으로 번역하며, 베트남 정부가 추진하는 행정개혁의 핵심 과제입니다.",
        "meaningVi": "Quá trình chuyển giao quyền hạn và trách nhiệm từ cơ quan nhà nước cấp trên xuống cấp dưới, nhằm tăng quyền tự chủ và hiệu quả quản lý của chính quyền địa phương. Là một trong những nội dung quan trọng của cải cách hành chính.",
        "context": "베트남 행정개혁 및 지방자치 강화 정책의 핵심 개념",
        "culturalNote": "베트남의 '권한 위임(Phân cấp quản lý)'은 한국의 '지방분권'과 방향은 유사하지만 정도가 다릅니다. 베트남은 중앙집권적 단일정당 체제이므로 지방정부의 자율성이 한국보다 제한적입니다. 한국은 헌법에서 지방자치를 보장하고 조례 제정권, 과세권 등을 지방에 부여하지만, 베트남은 중앙정부가 허용하는 범위 내에서만 권한을 행사합니다. 또한 베트남은 공산당 지방위원회가 행정기관보다 강한 권한을 가지므로, 실질적 의사결정 구조를 이해해야 정확한 통역이 가능합니다.",
        "commonMistakes": [
            {
                "mistake": "Phân cấp을 '분산화(decentralization)'로만 번역",
                "correction": "권한 위임 또는 지방분권",
                "explanation": "베트남 문맥에서는 '위임'의 뉘앙스가 강하며 완전한 분권은 아닙니다."
            },
            {
                "mistake": "한국과 동일한 수준의 지방자치라고 설명",
                "correction": "베트남은 중앙의 통제 하에 제한적 권한 위임",
                "explanation": "베트남 지방정부는 자율적 조례 제정이나 독립 과세권이 제한적입니다."
            },
            {
                "mistake": "'Phân quyền'과 'Phân cấp'을 동일하게 번역",
                "correction": "Phân quyền은 권한분산, Phân cấp은 등급별 위임",
                "explanation": "Phân cấp은 계층적 권한 이양, Phân quyền은 수평적 권한 분산입니다."
            }
        ],
        "examples": [
            {
                "ko": "정부는 지방정부에 대한 권한 위임을 확대하고 있습니다.",
                "vi": "Chính phủ đang mở rộng phân cấp quản lý cho chính quyền địa phương.",
                "situation": "formal"
            },
            {
                "ko": "권한 위임 정책으로 지방의 투자 결정권이 강화되었습니다.",
                "vi": "Chính sách phân cấp quản lý đã tăng cường quyền quyết định đầu tư của địa phương.",
                "situation": "formal"
            },
            {
                "ko": "중앙에서 지방으로 권한을 더 내려줘야 해요.",
                "vi": "Cần phân cấp nhiều hơn từ trung ương xuống địa phương.",
                "situation": "informal"
            }
        ],
        "relatedTerms": ["tu-tri-dia-phuong", "phan-quyen", "tu-chu-tai-chinh", "cai-cach-hanh-chinh"]
    },
    {
        "slug": "ngan-sach-dia-phuong",
        "korean": "지방 예산",
        "vietnamese": "Ngân sách địa phương",
        "hanja": "地方豫算",
        "hanjaReading": "地(땅 지) + 方(모 방) + 豫(미리 예) + 算(셈 산)",
        "pronunciation": "응안 싹 디아 프엉",
        "meaningKo": "지방정부(성, 시, 현, 사)의 1년 수입과 지출 계획으로, 한국의 '지방자치단체 예산'과 동일한 개념입니다. 통역 시 주의할 점은 베트남 지방예산은 중앙예산과 분리되어 있지만 중앙정부의 이전재원 비중이 매우 높아 재정자립도가 낮다는 점입니다. 한국도 지방교부세와 보조금 비중이 높지만, 베트남은 특히 농촌 지역의 경우 중앙 의존도가 90% 이상인 경우도 있습니다. 실무에서는 '지방예산', '지방재정'으로 번역하며, 인민의회가 심의·의결하고 인민위원회가 집행합니다.",
        "meaningVi": "Toàn bộ các khoản thu, chi của ngân sách nhà nước ở địa phương trong một năm, do Hội đồng nhân dân quyết định và Ủy ban nhân dân thực hiện. Bao gồm thu từ địa phương và nguồn bổ sung từ ngân sách cấp trên.",
        "context": "베트남 예산법 및 지방재정 관리 제도에서 규정하는 지방정부의 재정 계획",
        "culturalNote": "베트남 지방예산은 한국과 달리 '이중 예산 체계'를 가집니다. 중앙예산(Ngân sách trung ương)과 지방예산(Ngân sách địa phương)이 법적으로 분리되어 있으며, 각 지방정부는 독립적인 예산을 편성합니다. 하지만 재원의 대부분은 중앙정부로부터의 이전재원(Nguồn bổ sung)입니다. 한국의 지방교부세·보조금과 유사하지만, 베트남은 지방의 과세권이 더욱 제한적입니다. 통역 시 '재정자립도'를 설명할 때 베트남이 한국보다 훨씬 낮다는 점을 명확히 해야 합니다.",
        "commonMistakes": [
            {
                "mistake": "Ngân sách을 '예산안'으로 번역",
                "correction": "예산 (확정된 것) 또는 예산안 (심의 중)",
                "explanation": "Dự toán은 예산안, Ngân sách은 확정 예산입니다."
            },
            {
                "mistake": "지방예산이 중앙정부와 무관하다고 설명",
                "correction": "지방예산의 대부분은 중앙정부 이전재원",
                "explanation": "베트남 지방정부는 재정자립도가 낮아 중앙 의존도가 높습니다."
            },
            {
                "mistake": "'Thu ngân sách'를 '세금 징수'로만 번역",
                "correction": "예산 수입 (세금 외에 수수료, 이전재원 등 포함)",
                "explanation": "Thu ngân sách은 세금뿐 아니라 모든 예산 수입을 의미합니다."
            }
        ],
        "examples": [
            {
                "ko": "하노이시 인민의회가 2025년 지방예산안을 승인했습니다.",
                "vi": "Hội đồng nhân dân Thành phố Hà Nội đã phê duyệt dự toán ngân sách địa phương năm 2025.",
                "situation": "formal"
            },
            {
                "ko": "이번 사업은 지방예산으로 추진됩니다.",
                "vi": "Dự án này được thực hiện bằng ngân sách địa phương.",
                "situation": "formal"
            },
            {
                "ko": "우리 성은 지방예산이 부족해서 중앙 지원을 받아요.",
                "vi": "Tỉnh chúng ta thiếu ngân sách địa phương nên nhận bổ sung từ trung ương.",
                "situation": "informal"
            }
        ],
        "relatedTerms": ["ngan-sach-trung-uong", "thu-ngan-sach", "chi-ngan-sach", "tu-chu-tai-chinh"]
    },
    {
        "slug": "tu-tri-dia-phuong",
        "korean": "지방 자치",
        "vietnamese": "Tự trị địa phương",
        "hanja": "自治地方",
        "hanjaReading": "自(스스로 자) + 治(다스릴 치) + 地(땅 지) + 方(모 방)",
        "pronunciation": "뚜 찌 디아 프엉",
        "meaningKo": "지방정부가 중앙정부의 간섭 없이 자율적으로 지역 문제를 결정하고 처리하는 제도로, 한국의 '지방자치'와 같은 개념입니다. 통역 시 주의할 점은 베트남에서 '지방자치'는 한국처럼 헌법적 보장이 명확하지 않으며, 실질적으로는 중앙정부와 공산당의 통제 하에 있다는 점입니다. 베트남 헌법은 '인민자주권(Quyền làm chủ của nhân dân)'을 강조하지만, 서구식 지방자치와는 차이가 있습니다. 실무에서는 '지방자치', '지역 자율성'으로 번역하며, 베트남 정치 맥락에서 조심스럽게 사용해야 하는 용어입니다.",
        "meaningVi": "Quyền tự quản lý các vấn đề địa phương của chính quyền và nhân dân địa phương, trong khuôn khổ pháp luật và sự lãnh đạo của Đảng. Là một trong những yếu tố quan trọng của dân chủ cơ sở.",
        "context": "베트남 행정 개혁 및 민주화 논의에서 사용되는 지방정부 자율성 개념",
        "culturalNote": "베트남의 '지방자치(Tự trị địa phương)'는 서구나 한국의 지방자치와 다릅니다. 베트남은 단일정당 체제이므로 지방정부가 아무리 자율성을 가져도 공산당 지방위원회의 영향력이 절대적입니다. 한국은 헌법 제117조에서 지방자치를 보장하고 조례 제정권, 과세권을 명시하지만, 베트남 헌법은 '인민자주권'을 강조할 뿐 서구식 자치권은 보장하지 않습니다. 통역 시 '자치'라는 용어가 주는 오해를 방지하기 위해 '제한적 자율성' 또는 '위임된 권한 범위 내 자치'로 설명하는 것이 정확합니다.",
        "commonMistakes": [
            {
                "mistake": "베트남 지방자치가 한국과 동일하다고 설명",
                "correction": "베트남은 중앙집권 체제 내 제한적 자율성",
                "explanation": "베트남 지방정부는 독립적 조례 제정권이나 과세권이 제한적입니다."
            },
            {
                "mistake": "'Tự trị'를 '독립'으로 번역",
                "correction": "자치 또는 자율성",
                "explanation": "'독립'은 정치적으로 민감한 용어이며 Tự trị는 자치권을 의미합니다."
            },
            {
                "mistake": "'Quyền tự chủ'와 'Tự trị'를 구분 없이 번역",
                "correction": "Quyền tự chủ는 자율권, Tự trị는 자치제도",
                "explanation": "Quyền tự chủ는 권한, Tự trị는 제도적 자치를 의미합니다."
            }
        ],
        "examples": [
            {
                "ko": "베트남은 지방자치 제도를 점진적으로 강화하고 있습니다.",
                "vi": "Việt Nam đang dần tăng cường tự trị địa phương.",
                "situation": "formal"
            },
            {
                "ko": "지방자치는 지역 발전의 핵심 요소입니다.",
                "vi": "Tự trị địa phương là yếu tố quan trọng cho sự phát triển của địa phương.",
                "situation": "formal"
            },
            {
                "ko": "지방에서 자율적으로 결정할 수 있는 권한이 늘어났어요.",
                "vi": "Quyền tự quyết của địa phương đã được mở rộng.",
                "situation": "informal"
            }
        ],
        "relatedTerms": ["phan-cap-quan-ly", "dan-chu-co-so", "quyen-lam-chu", "ngan-sach-dia-phuong"]
    },
    {
        "slug": "bo-may-nha-nuoc",
        "korean": "국가 기구",
        "vietnamese": "Bộ máy nhà nước",
        "hanja": "國家機構",
        "hanjaReading": "國(나라 국) + 家(집 가) + 機(틀 기) + 構(얽을 구)",
        "pronunciation": "보 마이 냐 느억",
        "meaningKo": "국가의 권력을 행사하는 모든 조직과 기관을 총칭하는 용어로, 한국의 '국가기관' 또는 '정부조직'과 유사합니다. 통역 시 주의할 점은 베트남에서 '국가기구'는 입법(국회), 행정(정부), 사법(법원), 검찰, 감사원 등을 모두 포함하며, 한국보다 더 넓은 개념이라는 점입니다. 또한 베트남은 공산당이 국가기구를 영도(lãnh đạo)하는 구조이므로, 당과 국가의 관계를 이해해야 정확한 통역이 가능합니다. 실무에서는 '국가기구', '정부조직', '행정체계'로 번역합니다.",
        "meaningVi": "Toàn bộ các cơ quan thực hiện quyền lực nhà nước, bao gồm Quốc hội, Chủ tịch nước, Chính phủ, Tòa án, Viện kiểm sát và chính quyền địa phương. Hoạt động dưới sự lãnh đạo của Đảng Cộng sản Việt Nam.",
        "context": "베트남 헌법 및 정치 체제에서 국가 권력 구조를 설명하는 총괄 개념",
        "culturalNote": "베트남의 '국가기구(Bộ máy nhà nước)'는 한국의 '삼권분립' 개념과 다릅니다. 베트남은 '국회 중심제(Quốc hội là cơ quan quyền lực nhà nước cao nhất)'를 표방하며, 정부·법원·검찰이 국회 산하에 있는 구조입니다. 한국은 입법·행정·사법이 서로 견제하는 삼권분립이지만, 베트남은 국회가 최고 기관이며 모든 국가기구를 통제합니다. 또한 공산당이 모든 국가기구를 '영도'하므로, 실질적 권력 구조는 '당 → 국회 → 정부'입니다. 통역 시 이러한 정치체제 차이를 명확히 해야 합니다.",
        "commonMistakes": [
            {
                "mistake": "Bộ máy nhà nước을 '정부'로만 번역",
                "correction": "국가기구 (입법·행정·사법 모두 포함)",
                "explanation": "'정부(Chính phủ)'는 행정부만 의미하고, Bộ máy nhà nước은 전체 국가조직입니다."
            },
            {
                "mistake": "베트남도 한국처럼 삼권분립이라고 설명",
                "correction": "베트남은 국회 중심제, 삼권분립과 다름",
                "explanation": "베트남 헌법은 국회를 최고 권력기관으로 규정합니다."
            },
            {
                "mistake": "'Cơ quan nhà nước'와 'Bộ máy nhà nước'를 구분 없이 번역",
                "correction": "Cơ quan은 개별 기관, Bộ máy는 전체 체계",
                "explanation": "Cơ quan은 '기관(부처 등)', Bộ máy는 '조직 체계' 전체입니다."
            }
        ],
        "examples": [
            {
                "ko": "국가기구 개혁은 베트남 행정 개혁의 핵심 과제입니다.",
                "vi": "Cải cách bộ máy nhà nước là nhiệm vụ trọng tâm của cải cách hành chính Việt Nam.",
                "situation": "formal"
            },
            {
                "ko": "국가기구의 효율성을 높이기 위한 조치가 필요합니다.",
                "vi": "Cần có biện pháp nâng cao hiệu quả hoạt động của bộ máy nhà nước.",
                "situation": "formal"
            },
            {
                "ko": "국가기구가 너무 비대해서 간소화해야 해요.",
                "vi": "Bộ máy nhà nước quá cồng kềnh, cần tinh giản.",
                "situation": "informal"
            }
        ],
        "relatedTerms": ["quoc-hoi", "chinh-phu", "to-an", "vien-kiem-sat", "chu-tich-nuoc"]
    }
]

# Filter out duplicates
new_terms_filtered = [t for t in new_terms if t['slug'] not in existing_slugs]

if not new_terms_filtered:
    print("⚠️  All terms already exist. No new terms to add.")
else:
    # Extend data (data is a list!)
    data.extend(new_terms_filtered)

    # Write back to file
    with open(file_path, 'w', encoding='utf-8') as f:
        json.dump(data, f, ensure_ascii=False, indent=2)

    print(f"✅ Added {len(new_terms_filtered)} new Local Government/Organization Law terms to legal.json")
    print(f"📊 Total terms now: {len(data)}")
    for term in new_terms_filtered:
        print(f"   - {term['slug']}: {term['korean']} / {term['vietnamese']}")
