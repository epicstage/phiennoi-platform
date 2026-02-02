#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
경쟁법/독점규제 (Competition Law/Antitrust) 용어 추가 스크립트
Tier S 품질 기준 준수
"""

import json
import os

# CRITICAL: 절대 경로 구성
file_path = os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', 'data', 'terms', 'legal.json')

# 기존 데이터 로드
with open(file_path, 'r', encoding='utf-8') as f:
    data = json.load(f)  # data is a LIST, not dict!

# 기존 slug 수집 (중복 방지)
existing_slugs = {t['slug'] for t in data}

# 새 용어 10개 (경쟁법/독점규제)
new_terms = [
    {
        "slug": "canh-tranh-khong-lanh-manh",
        "korean": "부정경쟁",
        "vietnamese": "cạnh tranh không lành mạnh",
        "hanja": "不正競爭",
        "hanjaReading": "不(아닐 부) 正(바를 정) 競(겨룰 경) 爭(다툴 쟁)",
        "pronunciation": "cẳnh chảnh không lành mạnh",
        "meaningKo": "공정한 경쟁 질서를 해치는 행위로, 타인의 상표·상호 등을 무단으로 사용하거나 영업비밀을 침해하는 등의 행위를 말합니다. 베트남에서는 'cạnh tranh không lành mạnh'으로 표현하며, 한국의 부정경쟁방지법과 유사한 법체계가 있습니다. 통역 시 주의할 점은 베트남에서 이 용어가 독점금지법(Luật Cạnh tranh)의 일부로 규율된다는 점과, 한국처럼 별도의 부정경쟁방지법이 없다는 점을 설명해야 합니다. 'không lành mạnh'는 직역하면 '건강하지 않은'이라는 의미로, 공정하지 않다는 뉘앙스를 담고 있습니다.",
        "meaningVi": "Hành vi làm tổn hại đến trật tự cạnh tranh công bằng, bao gồm sử dụng trái phép nhãn hiệu, thương hiệu của người khác hoặc xâm phạm bí mật kinh doanh. Thuật ngữ này được quy định trong Luật Cạnh tranh của Việt Nam, tương tự như Luật Chống cạnh tranh không lành mạnh của Hàn Quốc, nhưng không có luật riêng biệt như Hàn Quốc.",
        "context": "법률 문서, 공정거래위원회 결정문, 소송 자료, 기업 컴플라이언스 교육에서 사용됩니다.",
        "culturalNote": "한국은 '부정경쟁방지 및 영업비밀보호에 관한 법률'이라는 별도 법률이 있지만, 베트남은 2018년 개정된 '경쟁법(Luật Cạnh tranh 2018)'에 독점규제와 부정경쟁 조항이 통합되어 있습니다. 한국에서는 공정거래위원회와 특허청이 분담 관할하지만, 베트nam은 경쟁관리국(Cục Quản lý cạnh tranh)이 단일 관할합니다. 베트남 기업들은 상표권 침해보다 영업비밀 유출에 더 민감한 경향이 있으며, 이는 제조업 중심 산업구조와 관련이 있습니다.",
        "commonMistakes": [
            {
                "mistake": "cạnh tranh bất chính",
                "correction": "cạnh tranh không lành mạnh",
                "explanation": "'bất chính'은 한자어 '불정(不正)'의 직역이지만, 베트남 법령에서는 'không lành mạnh'을 공식 용어로 사용합니다."
            },
            {
                "mistake": "hành vi cạnh tranh không công bằng",
                "correction": "cạnh tranh không lành mạnh",
                "explanation": "'không công bằng'은 의미는 비슷하지만 법률 용어가 아닙니다. 법령 번역 시 정확한 법정 용어를 사용해야 합니다."
            },
            {
                "mistake": "부정경쟁을 '독점'으로 번역",
                "correction": "부정경쟁(cạnh tranh không lành mạnh)과 독점(độc quyền)은 별개 개념",
                "explanation": "부정경쟁은 불공정한 경쟁 '행위'를 의미하고, 독점은 시장 '지배 상태'를 의미합니다. 통역 시 두 개념을 명확히 구분해야 합니다."
            }
        ],
        "examples": [
            {
                "ko": "피고는 원고의 상표를 무단으로 사용하여 부정경쟁행위를 저질렀습니다.",
                "vi": "Bị đơn đã sử dụng trái phép nhãn hiệu của nguyên đơn, thực hiện hành vi cạnh tranh không lành mạnh.",
                "situation": "formal"
            },
            {
                "ko": "이 회사는 경쟁사의 영업비밀을 빼내 부정경쟁방지법 위반으로 고발당했어요.",
                "vi": "Công ty này đã đánh cắp bí mật kinh doanh của đối thủ cạnh tranh, bị tố cáo vi phạm Luật Cạnh tranh.",
                "situation": "informal"
            },
            {
                "ko": "부정경쟁행위 금지청구 소송을 제기하겠습니다.",
                "vi": "Chúng tôi sẽ đệ đơn kiện yêu cầu cấm hành vi cạnh tranh không lành mạnh.",
                "situation": "formal"
            }
        ],
        "relatedTerms": ["doc-quyen", "vi-pham-canh-tranh", "thuong-hieu"]
    },
    {
        "slug": "doc-quyen",
        "korean": "독점",
        "vietnamese": "độc quyền",
        "hanja": "獨占",
        "hanjaReading": "獨(홀로 독) 占(점할 점)",
        "pronunciation": "độc 꾸옌",
        "meaningKo": "특정 사업자가 상품이나 서비스의 생산·판매를 독점적으로 지배하는 상태를 말합니다. 경쟁법에서는 독점적 지위를 남용하는 행위를 규제합니다. 베트남에서는 'độc quyền'이라고 하며, 한국의 시장지배적지위 개념과 유사합니다. 통역 시 주의할 점은 베트남에서 '독점'이 반드시 불법은 아니며, '독점적 지위의 남용(lạm dụng vị thế độc quyền)'이 규제 대상이라는 점을 명확히 해야 합니다. 한국의 '시장지배적 사업자' 개념을 베트남어로 설명할 때 'doanh nghiệp có vị thế độc quyền' 또는 'doanh nghiệp thống lĩnh thị trường'으로 풀어서 설명하면 이해가 쉽습니다.",
        "meaningVi": "Tình trạng một doanh nghiệp chiếm giữ toàn bộ hoặc phần lớn thị trường sản xuất, phân phối một loại hàng hóa hoặc dịch vụ. Luật Cạnh tranh quy định về hành vi lạm dụng vị thế độc quyền, tương tự như khái niệm 'vị thế thống lĩnh thị trường' của Hàn Quốc. Độc quyền không tự thân vi phạm pháp luật, nhưng việc lạm dụng vị thế độc quyền là hành vi bị cấm.",
        "context": "경쟁법 위반 사건, 기업결합 심사, 공정거래위원회 조사 자료에서 사용됩니다.",
        "culturalNote": "한국에서는 시장점유율 50% 이상 또는 3개 사업자 합계 75% 이상이면 시장지배적 사업자로 추정되지만, 베트남은 단일 사업자 30% 이상, 3개 사업자 합계 50% 이상이면 '지배적 지위'로 간주합니다. 베트남의 기준이 더 낮아 규제가 엄격한 편입니다. 또한 베트남에서는 국영기업이 주요 산업(전력, 통신, 석유 등)에서 법적 독점권을 보유한 경우가 많아, 민간 기업 독점과 국가 독점을 구분해서 설명해야 합니다. 한국 기업이 베트남 진출 시 이런 차이를 이해하지 못해 M&A 심사에서 어려움을 겪는 사례가 많습니다.",
        "commonMistakes": [
            {
                "mistake": "độc quyền을 '불법'으로 설명",
                "correction": "독점 자체는 합법이며, '독점적 지위 남용'이 불법",
                "explanation": "베트남 경쟁법 제11조는 독점적 지위를 인정하되, 제26조는 그 지위의 남용을 금지합니다. 통역 시 이를 명확히 구분해야 합니다."
            },
            {
                "mistake": "quyền độc quyền (독점권)",
                "correction": "vị thế độc quyền (독점적 지위)",
                "explanation": "'quyền'은 '권리'를 의미하므로 법적으로 부여된 독점권(특허권 등)과 혼동될 수 있습니다. 시장 지배력을 표현할 때는 'vị thế'를 사용합니다."
            },
            {
                "mistake": "독점을 'chiếm lĩnh thị trường'으로만 번역",
                "correction": "법률 맥락에서는 'độc quyền' 또는 'vị thế độc quyền' 사용",
                "explanation": "'chiếm lĩnh'은 '점령하다'라는 일반적 표현이며, 법률 용어로는 정확하지 않습니다."
            }
        ],
        "examples": [
            {
                "ko": "이 기업은 시장점유율 70%로 독점적 지위를 보유하고 있습니다.",
                "vi": "Doanh nghiệp này nắm giữ vị thế độc quyền với thị phần 70%.",
                "situation": "formal"
            },
            {
                "ko": "독점 기업이 가격을 임의로 올려서 소비자들이 피해를 보고 있어요.",
                "vi": "Doanh nghiệp độc quyền tăng giá tùy tiện khiến người tiêu dùng bị thiệt hại.",
                "situation": "informal"
            },
            {
                "ko": "공정거래위원회는 해당 기업의 독점적 지위 남용 행위를 조사 중입니다.",
                "vi": "Cục Quản lý cạnh tranh đang điều tra hành vi lạm dụng vị thế độc quyền của doanh nghiệp này.",
                "situation": "formal"
            }
        ],
        "relatedTerms": ["lam-dung-vi-the-thong-linh", "canh-tranh-khong-lanh-manh", "tap-trung-kinh-te"]
    },
    {
        "slug": "lam-dung-vi-the-thong-linh",
        "korean": "시장지배적지위남용",
        "vietnamese": "lạm dụng vị thế thống lĩnh",
        "hanja": "市場支配的地位濫用",
        "hanjaReading": "市(저자 시) 場(마당 장) 支(지탱할 지) 配(나눌 배) 的(과녁 적) 地(땅 지) 位(자리 위) 濫(넘칠 람) 用(쓸 용)",
        "pronunciation": "lạm zụng vị 떼 thống lĩnh",
        "meaningKo": "시장에서 지배적 지위를 가진 사업자가 그 지위를 남용하여 경쟁을 제한하거나 소비자에게 피해를 주는 행위를 말합니다. 대표적으로 부당한 가격인상, 거래거절, 끼워팔기 등이 있습니다. 베트남에서는 'lạm dụng vị thế thống lĩnh'이라고 하며, 한국 공정거래법 제3조의2(시장지배적 지위 남용 금지)와 유사한 규정이 베트남 경쟁법 제26조에 있습니다. 통역 시 주의할 점은 '시장지배적 지위'와 '남용 행위'를 분리해서 설명해야 한다는 점입니다. 베트남에서는 'vị thế thống lĩnh' 자체는 문제가 아니지만, 그것을 'lạm dụng(남용)'하는 것이 위법이라는 점을 명확히 해야 합니다.",
        "meaningVi": "Hành vi doanh nghiệp có vị thế thống lĩnh trên thị trường lợi dụng vị thế đó để hạn chế cạnh tranh hoặc gây thiệt hại cho người tiêu dùng. Các hành vi điển hình bao gồm: tăng giá bất hợp lý, từ chối giao dịch, bán kèm hàng hóa. Quy định tại Điều 26 Luật Cạnh tranh Việt Nam, tương tự Điều 3-2 Luật Công bằng giao dịch Hàn Quốc.",
        "context": "공정거래위원회 시정명령, 과징금 부과 결정문, 경쟁법 위반 소송에서 사용됩니다.",
        "culturalNote": "한국에서는 '시장지배적 지위'를 시장점유율과 진입장벽 등으로 판단하지만, 베트남은 시장점유율 기준이 더 구체적입니다(단일 사업자 30%, 3개 사업자 합계 50%). 또한 한국에서는 과징금이 매출액의 3% 이하이지만, 베트남은 위반 매출의 10% 또는 전년도 총매출의 1% 중 높은 금액을 부과할 수 있어 제재가 더 강력합니다. 베트남에서는 외국인 투자기업이 지배적 지위를 얻으면 더 엄격한 심사를 받는 경향이 있으며, 특히 중국 기업에 대한 경계가 강합니다. 통역 시 양국의 이런 차이를 설명하면 클라이언트의 리스크 관리에 도움이 됩니다.",
        "commonMistakes": [
            {
                "mistake": "lạm dụng độc quyền",
                "correction": "lạm dụng vị thế thống lĩnh",
                "explanation": "'độc quyền(독점)'보다 'vị thế thống lĩnh(지배적 지위)'이 법률 용어로 정확합니다. 베트남 경쟁법 제26조 제목도 'Lạm dụng vị thế thống lĩnh'입니다."
            },
            {
                "mistake": "남용을 'sử dụng sai'로 번역",
                "correction": "lạm dụng",
                "explanation": "'sử dụng sai'는 '잘못 사용하다'라는 일반적 표현이고, 'lạm dụng'은 '남용하다'라는 법률 용어입니다."
            },
            {
                "mistake": "시장지배적 지위를 'vị trí thống trị thị trường'으로 번역",
                "correction": "vị thế thống lĩnh thị trường",
                "explanation": "'vị trí'는 '위치'를 의미하고, 'vị thế'는 '지위, 입장'을 의미합니다. 법률 맥락에서는 'vị thế'가 적절합니다."
            }
        ],
        "examples": [
            {
                "ko": "공정거래위원회는 A사가 시장지배적 지위를 남용하여 경쟁사를 배제했다고 판단했습니다.",
                "vi": "Ủy ban Công bằng giao dịch kết luận rằng công ty A đã lạm dụng vị thế thống lĩnh để loại trừ đối thủ cạnh tranh.",
                "situation": "formal"
            },
            {
                "ko": "이 회사는 독점적 지위를 이용해서 가격을 마음대로 올리고 있어요.",
                "vi": "Công ty này đang lạm dụng vị thế thống lĩnh để tăng giá tùy ý.",
                "situation": "informal"
            },
            {
                "ko": "시장지배적 지위 남용으로 과징금 50억 원이 부과되었습니다.",
                "vi": "Công ty bị phạt tiền 50 tỷ won do lạm dụng vị thế thống lĩnh thị trường.",
                "situation": "formal"
            }
        ],
        "relatedTerms": ["doc-quyen", "xu-phat-vi-pham-canh-tranh", "thoa-thuan-han-che-canh-tranh"]
    },
    {
        "slug": "thoa-thuan-han-che-canh-tranh",
        "korean": "담합",
        "vietnamese": "thỏa thuận hạn chế cạnh tranh",
        "hanja": "談合",
        "hanjaReading": "談(말씀 담) 合(합할 합)",
        "pronunciation": "thỏa thuận hạn 쩨 cạnh tranh",
        "meaningKo": "경쟁관계에 있는 사업자들이 서로 합의하여 가격, 생산량, 시장분할 등을 결정함으로써 경쟁을 제한하는 행위를 말합니다. 대표적으로 가격담합, 입찰담합, 시장분할 담합이 있습니다. 베트남에서는 'thỏa thuận hạn chế cạnh tranh' 또는 줄여서 'thỏa thuận phản cạnh tranh'이라고 하며, 한국 공정거래법상 '부당한 공동행위'와 동일한 개념입니다. 통역 시 주의할 점은 한국에서는 '담합'이라는 한 단어로 표현되지만, 베트남어로는 '경쟁을 제한하는 합의'라고 풀어서 설명해야 자연스럽다는 점입니다. 특히 건설업 입찰담합 사례를 통역할 때 'thỏa thuận trong đấu thầu(입찰에서의 합의)'라고 명확히 해야 합니다.",
        "meaningVi": "Hành vi các doanh nghiệp cạnh tranh với nhau thỏa thuận về giá cả, sản lượng, phân chia thị trường để hạn chế cạnh tranh. Các dạng điển hình bao gồm: thỏa thuận về giá, thỏa thuận trong đấu thầu, phân chia thị trường. Quy định tại Điều 11 Luật Cạnh tranh Việt Nam, tương đương với 'hành vi thông đồng bất hợp lý' theo Luật Công bằng giao dịch Hàn Quốc.",
        "context": "공정거래위원회 조사, 입찰 관련 소송, 건설업·제약업 담합 사건에서 사용됩니다.",
        "culturalNote": "한국에서는 건설업 입찰담합이 가장 흔한 유형이지만, 베트남에서는 제약업과 의료기기 업계의 가격담합이 더 빈번하게 적발됩니다. 이는 베트남 의료보험 제도에서 정부가 의약품 가격을 통제하려 하자, 제약사들이 담합으로 대응하는 구조 때문입니다. 또한 베트남에서는 '암묵적 담합'도 처벌 대상이며, 명시적 합의 없이도 행위의 일치만으로도 위법으로 간주될 수 있습니다. 한국 기업이 베트남에서 업계 협회 모임에 참석할 때, 가격이나 생산량에 대한 논의를 피해야 하는 이유입니다. 통역사는 이런 리스크를 클라이언트에게 사전에 알려주는 것이 좋습니다.",
        "commonMistakes": [
            {
                "mistake": "담합을 'đồng minh'로 번역",
                "correction": "thỏa thuận hạn chế cạnh tranh",
                "explanation": "'đồng minh'은 '동맹'이라는 의미로 긍정적 뉘앙스가 있지만, 담합은 불법 행위이므로 'thỏa thuận hạn chế cạnh tranh(경쟁 제한 합의)'으로 표현해야 합니다."
            },
            {
                "mistake": "담합을 'cấu kết'로 번역",
                "correction": "thỏa thuận hạn chế cạnh tranh",
                "explanation": "'cấu kết'은 '결탁하다'라는 부정적 표현이지만 법률 용어가 아닙니다. 공식 문서에서는 'thỏa thuận hạn chế cạnh tranh'을 사용합니다."
            },
            {
                "mistake": "입찰담합을 'gian lận đấu thầu'로 번역",
                "correction": "thỏa thuận hạn chế cạnh tranh trong đấu thầu",
                "explanation": "'gian lận(부정행위)'은 범위가 넓고, 담합은 구체적으로 '경쟁 제한 합의'를 의미합니다."
            }
        ],
        "examples": [
            {
                "ko": "5개 건설사가 입찰담합으로 공정거래위원회로부터 과징금을 부과받았습니다.",
                "vi": "5 công ty xây dựng bị Ủy ban Công bằng giao dịch phạt tiền do thỏa thuận hạn chế cạnh tranh trong đấu thầu.",
                "situation": "formal"
            },
            {
                "ko": "제약회사들이 담합해서 약값을 함께 올렸대요.",
                "vi": "Các công ty dược phẩm thỏa thuận với nhau để cùng tăng giá thuốc.",
                "situation": "informal"
            },
            {
                "ko": "담합 행위가 적발되면 매출액의 10%까지 과징금이 부과될 수 있습니다.",
                "vi": "Nếu phát hiện hành vi thỏa thuận hạn chế cạnh tranh, có thể bị phạt tiền lên đến 10% doanh thu.",
                "situation": "formal"
            }
        ],
        "relatedTerms": ["lam-dung-vi-the-thong-linh", "xu-phat-vi-pham-canh-tranh", "tap-trung-kinh-te"]
    },
    {
        "slug": "tap-trung-kinh-te",
        "korean": "기업결합",
        "vietnamese": "tập trung kinh tế",
        "hanja": "企業結合",
        "hanjaReading": "企(꾀할 기) 業(업 업) 結(맺을 결) 合(합할 합)",
        "pronunciation": "tập chung kinh 떼",
        "meaningKo": "둘 이상의 기업이 합병, 인수, 지분 취득 등의 방법으로 결합하여 하나의 경제적 단위가 되는 것을 말합니다. 시장 집중도를 높이고 경쟁을 제한할 수 있어 공정거래위원회의 사전 신고·심사 대상입니다. 베트남에서는 'tập trung kinh tế'라고 하며, 직역하면 '경제 집중'입니다. 통역 시 주의할 점은 베트남에서는 M&A(sáp nhập và mua lại)보다 'tập trung kinh tế'라는 법률 용어를 사용한다는 점과, 한국의 '기업결합 신고' 제도와 유사하지만 신고 기준 금액이 다르다는 점을 설명해야 합니다. 베트남의 신고 기준은 총자산 3조 동(약 15억 달러) 또는 매출액 3조 동 이상일 때입니다.",
        "meaningVi": "Việc hai hoặc nhiều doanh nghiệp kết hợp với nhau thông qua sáp nhập, mua lại, mua cổ phần để trở thành một đơn vị kinh tế thống nhất. Tập trung kinh tế có thể làm tăng mức độ tập trung thị trường và hạn chế cạnh tranh, do đó phải thông báo và được Cục Quản lý cạnh tranh thẩm định trước. Quy định tại Điều 17-25 Luật Cạnh tranh Việt Nam.",
        "context": "M&A 거래, 공정거래위원회 심사 자료, 투자 계약서, 실사(due diligence) 보고서에서 사용됩니다.",
        "culturalNote": "한국에서는 대규모기업집단(재벌) 간 기업결합을 엄격히 규제하지만, 베트남에서는 외국인 투자 기업의 M&A를 더 민감하게 봅니다. 특히 중국 자본의 베트남 기업 인수는 정치적 이슈가 되기도 합니다. 베트남의 기업결합 심사 기간은 최대 90일이지만, 실제로는 6개월 이상 걸리는 경우도 많아 한국 기업들이 예상치 못한 지연을 경험합니다. 또한 베트남에서는 '경제 집중'이 무조건 나쁜 것은 아니며, 국가 경쟁력 강화를 위해 필요한 경우 승인된다는 점을 설명해야 합니다. 한국 기업이 베트남 기업을 인수할 때, 단순히 법적 요건만 충족하는 것이 아니라 '국가 경제에 기여'한다는 점을 강조하는 전략이 효과적입니다.",
        "commonMistakes": [
            {
                "mistake": "기업결합을 'sáp nhập doanh nghiệp'로만 번역",
                "correction": "tập trung kinh tế (법률 용어) 또는 sáp nhập và mua lại (일반 용어)",
                "explanation": "'sáp nhập'은 '합병'만을 의미하지만, 기업결합은 합병, 인수, 지분 취득 등을 모두 포함하는 상위 개념입니다."
            },
            {
                "mistake": "M&A를 그대로 'M&A'로 사용",
                "correction": "법률 문서에서는 'tập trung kinh tế', 일반 맥락에서는 'M&A' 또는 'sáp nhập và mua lại'",
                "explanation": "베트남 경쟁법에서는 'tập trung kinh tế'가 공식 법률 용어이므로, 법적 논의에서는 이 표현을 사용해야 합니다."
            },
            {
                "mistake": "기업결합 신고를 'đăng ký tập trung kinh tế'로 번역",
                "correction": "thông báo tập trung kinh tế",
                "explanation": "'đăng ký'는 '등록'이고, 'thông báo'는 '신고, 통지'입니다. 베트남 경쟁법 제24조는 'thông báo'를 사용합니다."
            }
        ],
        "examples": [
            {
                "ko": "이번 기업결합은 공정거래위원회의 승인을 받아야 합니다.",
                "vi": "Tập trung kinh tế này phải được Cục Quản lý cạnh tranh phê duyệt.",
                "situation": "formal"
            },
            {
                "ko": "두 회사가 합병하면 시장점유율이 너무 높아져서 심사에서 막힐 수 있어요.",
                "vi": "Nếu hai công ty sáp nhập, thị phần sẽ quá cao và có thể bị từ chối trong thẩm định tập trung kinh tế.",
                "situation": "informal"
            },
            {
                "ko": "기업결합 신고 기준을 초과하여 경쟁당국에 사전 신고했습니다.",
                "vi": "Vượt quá ngưỡng thông báo tập trung kinh tế nên chúng tôi đã thông báo trước cho cơ quan quản lý cạnh tranh.",
                "situation": "formal"
            }
        ],
        "relatedTerms": ["doc-quyen", "lam-dung-vi-the-thong-linh", "thi-truong-lien-quan"]
    },
    {
        "slug": "xu-phat-vi-pham-canh-tranh",
        "korean": "경쟁법위반처벌",
        "vietnamese": "xử phạt vi phạm cạnh tranh",
        "hanja": "競爭法違反處罰",
        "hanjaReading": "競(겨룰 경) 爭(다툴 쟁) 法(법 법) 違(어그러질 위) 反(돌이킬 반) 處(처리할 처) 罰(벌할 벌)",
        "pronunciation": "xử phạt vi 팜 cạnh tranh",
        "meaningKo": "경쟁법을 위반한 사업자에게 부과되는 제재 조치로, 과징금, 과태료, 시정명령, 형사처벌 등이 있습니다. 베트남에서는 'xử phạt vi phạm cạnh tranh'이라고 하며, 한국과 유사하게 행정적 제재와 형사처벌이 병행됩니다. 통역 시 주의할 점은 베트남의 제재 수준이 한국보다 높다는 점을 명확히 해야 합니다. 베트남에서는 위반 매출액의 최대 10% 또는 전년도 총매출의 1% 중 높은 금액을 과징금으로 부과할 수 있어, 한국의 매출액 3% 기준보다 훨씬 엄격합니다. 또한 베트남에서는 기업뿐만 아니라 개인(임원, 직원)도 형사처벌 대상이 될 수 있다는 점을 강조해야 합니다.",
        "meaningVi": "Các biện pháp xử phạt đối với doanh nghiệp vi phạm Luật Cạnh tranh, bao gồm: phạt tiền, lệnh khắc phục, và truy cứu trách nhiệm hình sự. Theo Luật Cạnh tranh Việt Nam, mức phạt tiền có thể lên đến 10% doanh thu liên quan đến vi phạm hoặc 1% tổng doanh thu năm trước, tùy mức nào cao hơn. Ngoài ra, cá nhân (lãnh đạo, nhân viên) cũng có thể bị truy cứu trách nhiệm hình sự.",
        "context": "공정거래위원회 결정문, 과징금 부과 처분, 형사 고발 사건, 컴플라이언스 교육 자료에서 사용됩니다.",
        "culturalNote": "한국에서는 과징금이 주된 제재 수단이고 형사처벌은 드물지만, 베트남에서는 형사처벌이 더 적극적으로 활용됩니다. 특히 담합이나 독점적 지위 남용이 소비자에게 심각한 피해를 준 경우, 기업 대표나 담당 임원이 징역형을 받을 수 있습니다. 베트남 형법 제205조는 경쟁법 위반에 대해 최대 7년의 징역형을 규정하고 있어, 한국 기업 주재원들이 매우 조심해야 합니다. 또한 베트남에서는 '경고(cảnh cáo)'도 공식 제재 수단이며, 2회 경고를 받으면 다음 위반 시 가중 처벌됩니다. 통역 시 이런 제재 단계를 명확히 설명해야 클라이언트가 리스크를 정확히 인식할 수 있습니다.",
        "commonMistakes": [
            {
                "mistake": "과징금을 'tiền phạt hành chính'로만 번역",
                "correction": "tiền phạt vi phạm cạnh tranh (경쟁법 위반 과징금) 또는 tiền xử phạt hành chính (행정 벌금)",
                "explanation": "'tiền phạt hành chính'은 일반적인 행정 벌금이고, 경쟁법 위반 과징금은 'tiền phạt vi phạm cạnh tranh'으로 구체화하는 것이 좋습니다."
            },
            {
                "mistake": "시정명령을 'lệnh sửa chữa'로 번역",
                "correction": "lệnh khắc phục",
                "explanation": "'sửa chữa'는 '수리하다'라는 의미이고, 'khắc phục'은 '시정하다, 교정하다'라는 법률 용어입니다."
            },
            {
                "mistake": "형사처벌을 'trừng phạt hình sự'로 번역",
                "correction": "truy cứu trách nhiệm hình sự",
                "explanation": "'trừng phạt'은 '응징하다'라는 강한 표현이고, 'truy cứu trách nhiệm hình sự'는 '형사 책임을 추궁하다'라는 법률 용어입니다."
            }
        ],
        "examples": [
            {
                "ko": "담합 행위로 과징금 100억 원이 부과되고 시정명령을 받았습니다.",
                "vi": "Do hành vi thỏa thuận hạn chế cạnh tranh, công ty bị phạt tiền 100 tỷ won và nhận lệnh khắc phục.",
                "situation": "formal"
            },
            {
                "ko": "경쟁법 위반으로 대표이사가 벌금형을 받았어요.",
                "vi": "Giám đốc bị phạt tiền do vi phạm Luật Cạnh tranh.",
                "situation": "informal"
            },
            {
                "ko": "1차 위반에는 경고 처분, 2차 위반부터는 과징금이 부과됩니다.",
                "vi": "Vi phạm lần đầu sẽ bị cảnh cáo, từ lần thứ hai trở đi sẽ bị phạt tiền.",
                "situation": "formal"
            }
        ],
        "relatedTerms": ["lam-dung-vi-the-thong-linh", "thoa-thuan-han-che-canh-tranh", "tap-trung-kinh-te"]
    },
    {
        "slug": "thi-truong-lien-quan",
        "korean": "관련시장",
        "vietnamese": "thị trường liên quan",
        "hanja": "關聯市場",
        "hanjaReading": "關(관계할 관) 聯(연결할 련) 市(저자 시) 場(마당 장)",
        "pronunciation": "thị trường lien 꾸안",
        "meaningKo": "특정 상품이나 서비스가 거래되는 시장의 범위로, 경쟁법 분석의 출발점입니다. '상품시장'과 '지역시장'으로 구분하며, 시장지배적 지위나 기업결합 심사 시 관련시장을 먼저 획정해야 합니다. 베트남에서는 'thị trường liên quan'이라고 하며, 한국 공정거래법상 '관련시장' 개념과 동일합니다. 통역 시 주의할 점은 '관련시장'이 단순히 '시장'이 아니라 '경쟁 평가를 위해 획정된 특정 범위의 시장'이라는 점을 명확히 해야 합니다. 예를 들어 '스마트폰 시장'이 관련시장인지, '모바일 기기 시장' 전체가 관련시장인지에 따라 시장점유율이 크게 달라집니다.",
        "meaningVi": "Phạm vi thị trường mà một hàng hóa hoặc dịch vụ cụ thể được giao dịch, là điểm khởi đầu của phân tích cạnh tranh. Thị trường liên quan được chia thành 'thị trường sản phẩm' và 'thị trường địa lý'. Việc xác định thị trường liên quan là bước đầu tiên trong thẩm định vị thế thống lĩnh hoặc tập trung kinh tế. Theo Điều 3 Luật Cạnh tranh Việt Nam, thị trường liên quan là thị trường có ranh giới được xác định bởi hàng hóa, dịch vụ có thể thay thế cho nhau và địa bàn địa lý.",
        "context": "공정거래위원회 심사보고서, 경제분석 보고서, 기업결합 신고서, 전문가 의견서에서 사용됩니다.",
        "culturalNote": "한국에서는 관련시장 획정 시 '수요 대체성'을 중심으로 판단하지만, 베트남에서는 '공급 대체성'도 함께 고려하는 경향이 있습니다. 예를 들어 한국에서는 '소주 시장'과 '맥주 시장'을 별도 관련시장으로 보지만, 베트남에서는 '주류 시장' 전체를 하나의 관련시장으로 볼 가능성이 높습니다. 또한 베트남은 지역 시장 획정에서 '운송비용'을 중요하게 고려하는데, 이는 베트남의 남북 간 물류 인프라가 한국보다 덜 발달했기 때문입니다. 통역 시 이런 차이를 설명하면 한국 기업이 베트남 경쟁당국의 시장 획정 방식을 이해하는 데 도움이 됩니다.",
        "commonMistakes": [
            {
                "mistake": "관련시장을 'thị trường có liên quan'로 번역",
                "correction": "thị trường liên quan",
                "explanation": "'có liên quan'은 '관련이 있는'이라는 형용사구이고, 'thị trường liên quan'은 하나의 법률 용어입니다."
            },
            {
                "mistake": "상품시장을 'thị trường hàng hóa'로 번역",
                "correction": "thị trường sản phẩm liên quan",
                "explanation": "'hàng hóa'는 '재화'를 의미하고, 경쟁법에서는 'sản phẩm(상품)'이 서비스를 포함하는 더 넓은 개념으로 사용됩니다."
            },
            {
                "mistake": "지역시장을 'thị trường khu vực'로만 번역",
                "correction": "thị trường địa lý liên quan",
                "explanation": "'khu vực'은 '지역'이지만, 법률 용어로는 'thị trường địa lý(지리적 시장)'이 정확합니다."
            }
        ],
        "examples": [
            {
                "ko": "관련시장은 '국내 스마트폰 시장'으로 획정되었습니다.",
                "vi": "Thị trường liên quan được xác định là 'thị trường điện thoại thông minh trong nước'.",
                "situation": "formal"
            },
            {
                "ko": "시장 범위를 어떻게 정하느냐에 따라 점유율이 완전히 달라져요.",
                "vi": "Tùy thuộc vào cách xác định phạm vi thị trường, thị phần có thể hoàn toàn khác nhau.",
                "situation": "informal"
            },
            {
                "ko": "관련시장 획정 시 수요 대체성과 공급 대체성을 모두 고려해야 합니다.",
                "vi": "Khi xác định thị trường liên quan, cần xem xét cả tính thay thế về cầu và tính thay thế về cung.",
                "situation": "formal"
            }
        ],
        "relatedTerms": ["doc-quyen", "tap-trung-kinh-te", "lam-dung-vi-the-thong-linh"]
    },
    {
        "slug": "hang-gia",
        "korean": "위조품",
        "vietnamese": "hàng giả",
        "hanja": "僞造品",
        "hanjaReading": "僞(거짓 위) 造(지을 조) 品(물건 품)",
        "pronunciation": "항 자",
        "meaningKo": "타인의 상표권이나 디자인권을 침해하여 만든 모조품을 말합니다. 진품으로 위장하여 소비자를 기만하며, 저작권법, 상표법, 부정경쟁방지법 위반에 해당합니다. 베트남에서는 'hàng giả' 또는 'hàng nhái(모조품)'이라고 하며, 한국보다 위조품 문제가 더 심각합니다. 통역 시 주의할 점은 베트남에서 'hàng giả'는 단순한 모조품이 아니라 형사처벌 대상인 범죄 행위라는 점을 강조해야 합니다. 베트남 형법 제226조는 위조품 생산·유통에 대해 최대 15년의 징역형을 규정하고 있어, 한국 기업이 베트남에서 위조품 피해를 입었을 때 형사 고발이 가능하다는 점을 안내해야 합니다.",
        "meaningVi": "Hàng hóa xâm phạm quyền nhãn hiệu hoặc quyền thiết kế công nghiệp của người khác. Hàng giả được ngụy trang là hàng chính hãng để lừa dối người tiêu dùng, vi phạm Luật Sở hữu trí tuệ và Luật Cạnh tranh. Theo Điều 226 Bộ luật Hình sự Việt Nam, hành vi sản xuất, buôn bán hàng giả có thể bị phạt tù lên đến 15 năm, nghiêm trọng hơn so với Hàn Quốc.",
        "context": "지재권 소송, 세관 단속, 온라인 플랫폼 침해 신고, 브랜드 보호 활동에서 사용됩니다.",
        "culturalNote": "베트남은 세계에서 위조품 생산·유통이 가장 심각한 국가 중 하나로, 특히 의류, 가방, 화장품 등 한류 제품의 위조품이 많습니다. 한국에서는 위조품 단속이 주로 세관과 경찰의 역할이지만, 베트남에서는 '시장관리국(Cục Quản lý thị trường)'이라는 별도 기관이 위조품 단속을 전담합니다. 베트남 시장에서는 '정품 보증'이 중요한 마케팅 포인트이며, 한국 기업들은 QR코드나 홀로그램 등으로 정품 인증 시스템을 구축하는 경우가 많습니다. 통역 시 베트남 소비자들이 위조품과 '병행수입품(hàng xách tay)'을 혼동하는 경우가 많아, 이 둘의 차이를 명확히 설명하는 것이 좋습니다.",
        "commonMistakes": [
            {
                "mistake": "위조품을 'hàng nhái'로만 번역",
                "correction": "법률 맥락에서는 'hàng giả', 일반 맥락에서는 'hàng nhái'",
                "explanation": "'hàng nhái'은 '모조품'이라는 일반적 표현이고, 'hàng giả'는 '위조품'이라는 법률 용어로 더 강한 불법성을 내포합니다."
            },
            {
                "mistake": "위조품을 'hàng fake' (영어 차용)",
                "correction": "hàng giả",
                "explanation": "'fake'는 베트남에서 구어체로 사용되지만, 법률 문서에서는 베트남어 'hàng giả'를 사용해야 합니다."
            },
            {
                "mistake": "병행수입품을 위조품으로 번역",
                "correction": "병행수입품은 'hàng xách tay' 또는 'hàng nhập khẩu song song', 위조품과 다름",
                "explanation": "병행수입품은 정품이지만 공식 유통망 외로 수입된 것이고, 위조품은 지재권을 침해한 불법 제품입니다."
            }
        ],
        "examples": [
            {
                "ko": "세관에서 위조품 1만 개를 적발하여 폐기 조치했습니다.",
                "vi": "Hải quan phát hiện và tiêu hủy 10.000 sản phẩm hàng giả.",
                "situation": "formal"
            },
            {
                "ko": "이 가방은 위조품인 것 같아요. 상표가 조금 다르네요.",
                "vi": "Túi này có vẻ là hàng giả. Nhãn hiệu hơi khác.",
                "situation": "informal"
            },
            {
                "ko": "위조품 제조·유통으로 기소되어 징역 3년을 선고받았습니다.",
                "vi": "Bị truy tố về tội sản xuất, buôn bán hàng giả và bị kết án 3 năm tù.",
                "situation": "formal"
            }
        ],
        "relatedTerms": ["canh-tranh-khong-lanh-manh", "thuong-hieu", "so-huu-tri-tue"]
    },
    {
        "slug": "ban-pha-gia",
        "korean": "덤핑",
        "vietnamese": "bán phá giá",
        "hanja": "Dumping",
        "hanjaReading": None,
        "pronunciation": "bán 파 자",
        "meaningKo": "수출국에서의 정상 가격보다 낮은 가격으로 수출하여 수입국 산업에 피해를 주는 행위를 말합니다. 국제 무역에서 불공정 거래로 간주되며, WTO 반덤핑협정에 따라 수입국은 반덤핑 관세를 부과할 수 있습니다. 베트남에서는 'bán phá giá'라고 하며, 직역하면 '가격을 파괴하며 판매'라는 의미입니다. 통역 시 주의할 점은 베트남이 덤핑 '피해국'인 동시에 덤핑 '가해국'으로도 자주 지목된다는 점입니다. 한국 기업이 베트남에서 생산한 제품을 제3국에 수출할 때, 그 제3국이 반덤핑 조사를 시작하면 베트남 생산기지 자체가 타격을 받을 수 있어 주의가 필요합니다.",
        "meaningVi": "Hành vi xuất khẩu hàng hóa với giá thấp hơn giá bình thường tại thị trường xuất khẩu, gây thiệt hại cho ngành sản xuất của nước nhập khẩu. Đây là hành vi giao dịch không công bằng trong thương mại quốc tế, và theo Hiệp định chống bán phá giá của WTO, nước nhập khẩu có thể áp dụng thuế chống bán phá giá. Việt Nam vừa là nước bị thiệt hại, vừa là nước bị cáo buộc bán phá giá trong nhiều vụ việc.",
        "context": "무역 분쟁, 반덤핑 조사, WTO 제소, 관세 당국 결정문, 수출입 법률 자문에서 사용됩니다.",
        "culturalNote": "베트남은 2007년 WTO 가입 후 반덤핑 조사를 적극 활용하고 있으며, 특히 중국산 철강, 화학제품에 대한 반덤핑 관세를 자주 부과합니다. 반면 베트남산 제품(철강, 수산물, 타이어 등)도 미국, EU, 한국으로부터 반덤핑 조사를 받는 경우가 많습니다. 한국 기업이 베트남에 공장을 세워 '메이드 인 베트남' 제품을 생산할 때, 원산지 규정을 충족하지 못하면 '우회 덤핑'으로 간주되어 추가 관세를 물 수 있습니다. 통역 시 '정상 가격(giá bình thường)', '수출 가격(giá xuất khẩu)', '덤핑 마진(biên độ phá giá)' 등 기술적 용어를 정확히 전달해야 합니다. 베트남 기업들은 반덤핑 제소를 법적 무기로 활용하는 경향이 있어, 한국 기업은 사전에 가격 정책을 신중히 수립해야 합니다.",
        "commonMistakes": [
            {
                "mistake": "덤핑을 'dumping'으로 그대로 사용",
                "correction": "bán phá giá",
                "explanation": "베트남어로는 'bán phá giá'라는 정확한 법률 용어가 있으므로, 영어를 그대로 쓰지 말고 베트남어를 사용해야 합니다."
            },
            {
                "mistake": "반덤핑 관세를 'thuế chống dumping'으로 번역",
                "correction": "thuế chống bán phá giá",
                "explanation": "베트남 무역법에서 공식 용어는 'thuế chống bán phá giá'입니다."
            },
            {
                "mistake": "덤핑 마진을 'lợi nhuận phá giá'로 번역",
                "correction": "biên độ phá giá",
                "explanation": "'lợi nhuận'은 '이윤'이고, 덤핑 마진은 '가격 차이'를 의미하므로 'biên độ(격차, 마진)'가 정확합니다."
            }
        ],
        "examples": [
            {
                "ko": "중국산 철강 제품에 대해 반덤핑 관세 25%가 부과되었습니다.",
                "vi": "Sản phẩm thép Trung Quốc bị áp thuế chống bán phá giá 25%.",
                "situation": "formal"
            },
            {
                "ko": "이 회사가 원가 이하로 팔아서 덤핑 의심을 받고 있어요.",
                "vi": "Công ty này đang bị nghi ngờ bán phá giá vì bán dưới giá thành.",
                "situation": "informal"
            },
            {
                "ko": "반덤핑 조사 결과, 덤핑 마진이 35%로 확정되어 잠정 관세가 부과됩니다.",
                "vi": "Kết quả điều tra chống bán phá giá xác định biên độ phá giá là 35%, thuế tạm thời sẽ được áp dụng.",
                "situation": "formal"
            }
        ],
        "relatedTerms": ["tro-cap-nha-nuoc", "canh-tranh-khong-lanh-manh", "thuong-mai-quoc-te"]
    },
    {
        "slug": "tro-cap-nha-nuoc",
        "korean": "정부보조금",
        "vietnamese": "trợ cấp nhà nước",
        "hanja": "政府補助金",
        "hanjaReading": "政(정사 정) 府(마을 부) 補(기울 보) 助(도울 조) 金(쇠 금)",
        "pronunciation": "쩌 깝 냐 느억",
        "meaningKo": "정부가 특정 산업이나 기업에 재정적 지원을 제공하는 것으로, 수출 보조금, 생산 보조금, R&D 지원금 등이 있습니다. WTO 보조금협정은 불공정 무역을 초래하는 보조금을 규제하며, 상계관세 부과의 근거가 됩니다. 베트남에서는 'trợ cấp nhà nước'라고 하며, 한국의 '정부 지원금' 개념과 동일합니다. 통역 시 주의할 점은 베트남 정부가 국영기업과 전략 산업(반도체, 전기차 등)에 막대한 보조금을 지급하고 있어, 한국 기업이 베트남 기업과 경쟁할 때 불리한 위치에 놓일 수 있다는 점을 설명해야 합니다. 또한 한국 정부의 FTA 활용 지원금이나 수출 바우처도 WTO 규정상 '보조금'으로 간주될 수 있어, 베트남 당국의 상계관세 조사 대상이 될 위험이 있습니다.",
        "meaningVi": "Hỗ trợ tài chính mà chính phủ cung cấp cho ngành hoặc doanh nghiệp cụ thể, bao gồm trợ cấp xuất khẩu, trợ cấp sản xuất, hỗ trợ R&D. Hiệp định Trợ cấp của WTO quy định về các loại trợ cấp gây mất công bằng trong thương mại, và là cơ sở để áp dụng thuế chống trợ cấp. Chính phủ Việt Nam cung cấp nhiều trợ cấp cho doanh nghiệp nhà nước và các ngành chiến lược (bán dẫn, xe điện), có thể tạo ra lợi thế cạnh tranh không công bằng với doanh nghiệp Hàn Quốc.",
        "context": "무역 분쟁, WTO 제소, 상계관세 조사, 정부 지원 정책 분석, 국제 통상 협상에서 사용됩니다.",
        "culturalNote": "베트남은 사회주의 시장경제 체제로, 정부가 경제에 깊이 개입하며 국영기업에 막대한 보조금을 지급합니다. 예를 들어 베트남 국영 석유기업 PetroVietnam이나 통신기업 VNPT는 정부로부터 토지, 세제 혜택, 저리 대출 등을 받아 민간 기업보다 유리한 조건에서 경쟁합니다. 한국 기업이 베트남에 투자할 때, '투자 인센티브'로 받는 세제 혜택이나 토지 지원도 WTO 규정상 '보조금'에 해당할 수 있어, 제3국으로 수출 시 상계관세 대상이 될 수 있습니다. 통역 시 '금지 보조금(trợ cấp bị cấm)', '허용 보조금(trợ cấp được phép)', '조치 가능 보조금(trợ cấp có thể bị xử lý)' 등 WTO 분류를 정확히 설명하는 것이 중요합니다.",
        "commonMistakes": [
            {
                "mistake": "보조금을 'tiền hỗ trợ'로만 번역",
                "correction": "법률 맥락에서는 'trợ cấp nhà nước', 일반 맥락에서는 'tiền hỗ trợ'",
                "explanation": "'tiền hỗ trợ'는 '지원금'이라는 일반적 표현이고, 'trợ cấp nhà nước'는 WTO 규정상 법률 용어입니다."
            },
            {
                "mistake": "상계관세를 'thuế đối kháng'로 번역",
                "correction": "thuế chống trợ cấp",
                "explanation": "'đối kháng'은 '대항하다'라는 의미이고, 'thuế chống trợ cấp'은 '보조금에 대응하는 관세'라는 정확한 법률 용어입니다."
            },
            {
                "mistake": "R&D 지원금을 일반 보조금과 동일하게 번역",
                "correction": "R&D 지원금은 'trợ cấp nghiên cứu và phát triển'로 구체화",
                "explanation": "WTO 보조금협정은 R&D 지원을 '허용 보조금'으로 분류하므로, 일반 보조금과 구분해서 설명해야 합니다."
            }
        ],
        "examples": [
            {
                "ko": "이 기업은 정부로부터 100억 원의 R&D 보조금을 받았습니다.",
                "vi": "Doanh nghiệp này nhận được trợ cấp nghiên cứu và phát triển 100 tỷ won từ chính phủ.",
                "situation": "formal"
            },
            {
                "ko": "수출 보조금을 받은 제품이라서 상계관세가 부과될 수 있어요.",
                "vi": "Sản phẩm này nhận trợ cấp xuất khẩu nên có thể bị áp thuế chống trợ cấp.",
                "situation": "informal"
            },
            {
                "ko": "WTO는 무역 왜곡 효과가 있는 정부 보조금을 금지하고 있습니다.",
                "vi": "WTO cấm các loại trợ cấp nhà nước có tác dụng bóp méo thương mại.",
                "situation": "formal"
            }
        ],
        "relatedTerms": ["ban-pha-gia", "canh-tranh-khong-lanh-manh", "thuong-mai-quoc-te"]
    }
]

# 중복 제거 (기존 slug와 비교)
filtered_terms = [term for term in new_terms if term['slug'] not in existing_slugs]

print(f"총 {len(new_terms)}개 용어 중 {len(filtered_terms)}개가 새로운 용어입니다.")

# 기존 데이터에 추가
data.extend(filtered_terms)

# 파일 저장 (들여쓰기 2칸, 유니코드 이스케이프 없음, 마지막 줄바꿈)
with open(file_path, 'w', encoding='utf-8') as f:
    json.dump(data, f, ensure_ascii=False, indent=2)
    f.write('\n')  # 마지막 줄바꿈 추가

print(f"✅ {len(filtered_terms)}개 용어가 legal.json에 추가되었습니다.")
print(f"총 용어 수: {len(data)}개")
