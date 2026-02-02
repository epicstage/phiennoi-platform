#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
노동법/고용법 용어 추가 스크립트 (Labor Law/Employment Law)
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

# 신규 용어 정의
new_terms = [
    {
        "slug": "nguoi-lao-dong",
        "korean": "근로자",
        "vietnamese": "người lao động",
        "hanja": "勤勞者",
        "hanjaReading": "勤(부지런할 근) + 勞(일할 로) + 者(사람 자)",
        "pronunciation": "응으어이 라오 동",
        "meaningKo": "노동계약에 따라 사용자에게 근로를 제공하고 임금을 받는 사람. 통역 시 '근로자'와 '노동자'를 혼용하지 않도록 주의해야 하며, 베트남에서는 người lao động이 법적 용어로 통일되어 있음을 설명해야 한다. 한국의 근로기준법상 근로자는 직업의 종류와 관계없이 임금을 목적으로 사업이나 사업장에 근로를 제공하는 자를 의미하며, 베트남 노동법(Bộ luật Lao động)의 정의와 범위가 다를 수 있으므로 양국 법률 차이를 명확히 구분하여 통역해야 한다. 특히 프리랜서나 플랫폼 노동자의 근로자성 판단 기준이 한국과 베트남이 다르므로 문맥에 따라 정확한 법적 지위를 설명하는 것이 중요하다.",
        "meaningVi": "Người ký kết hợp đồng lao động với người sử dụng lao động, làm việc theo sự quản lý và điều hành của người sử dụng lao động, và được trả lương. Theo Bộ luật Lao động Việt Nam, người lao động bao gồm cả lao động có hợp đồng chính thức và lao động thời vụ. Phạm vi và quyền lợi của người lao động có thể khác nhau giữa luật Hàn Quốc và Việt Nam, đặc biệt trong trường hợp lao động tự do hoặc lao động nền tảng số.",
        "context": "고용 관계, 노동 계약, 근로 조건 협상에서 사용",
        "culturalNote": "한국에서는 '근로자'라는 용어가 법률적으로 정의되어 있으며, 정규직/비정규직/임시직 등으로 세분화된다. 베트Nam에서는 người lao động이 포괄적 개념으로 사용되며, hợp đồng lao động(노동계약) 유무에 따라 법적 보호 수준이 달라진다. 한국은 근로기준법이 적용되는 범위가 넓지만, 베트남은 노동계약서가 없으면 법적 보호를 받기 어려운 경우가 많아 이 차이를 통역 시 명확히 설명해야 한다. 또한 한국의 특수고용직(특수형태근로종사자)과 베트남의 계약직 개념이 다르므로 주의가 필요하다.",
        "commonMistakes": [
            {
                "mistake": "công nhân으로만 번역",
                "correction": "người lao động 사용",
                "explanation": "công nhân은 주로 제조업 현장 노동자를 지칭하며, 법률 용어로는 người lao động이 정확함"
            },
            {
                "mistake": "근로자를 nhân viên으로 번역",
                "correction": "người lao động으로 통역",
                "explanation": "nhân viên은 회사 직원을 의미하며 법적 개념인 근로자와는 범위가 다름"
            },
            {
                "mistake": "한국 근로기준법 개념을 그대로 적용",
                "correction": "베트남 노동법(Bộ luật Lao động) 맥락에서 설명",
                "explanation": "양국 법률 체계가 다르므로 근로자 정의와 보호 범위를 각각 구분하여 통역해야 함"
            }
        ],
        "examples": [
            {
                "ko": "이 회사는 현재 500명의 근로자를 고용하고 있습니다.",
                "vi": "Công ty này hiện đang tuyển dụng 500 người lao động.",
                "situation": "formal"
            },
            {
                "ko": "근로자는 부당해고에 대해 이의를 제기할 권리가 있습니다.",
                "vi": "Người lao động có quyền khiếu nại về việc sa thải trái luật.",
                "situation": "formal"
            },
            {
                "ko": "현장에서 근로자 안전이 최우선입니다.",
                "vi": "Tại hiện trường, an toàn của người lao động là ưu tiên hàng đầu.",
                "situation": "onsite"
            }
        ],
        "relatedTerms": ["nguoi-su-dung-lao-dong", "hop-dong-lao-dong-co-thoi-han", "cong-doan"]
    },
    {
        "slug": "nguoi-su-dung-lao-dong",
        "korean": "사용자",
        "vietnamese": "người sử dụng lao động",
        "hanja": "使用者",
        "hanjaReading": "使(부릴 사) + 用(쓸 용) + 者(사람 자)",
        "pronunciation": "응으어이 쓰 중 라오 동",
        "meaningKo": "근로자를 고용하여 근로계약에 따라 임금을 지급하고 지휘·감독하는 사업주 또는 사업 경영 담당자. 통역 시 '고용주'와 '사용자'를 문맥에 따라 구분해야 하며, 베트남에서는 người sử dụng lao động 또는 chủ lao động으로 표현한다. 한국 근로기준법에서는 사업주 또는 사업 경영 담당자를 포괄하는 개념이며, 베트남 노동법에서도 유사하게 고용 관계의 주체로 정의된다. 다만 한국에서는 사용자의 책임 범위가 넓고, 부당노동행위 금지 의무 등이 명확하게 규정되어 있으므로 양국 법률상 사용자 의무와 책임의 차이를 정확히 전달해야 한다.",
        "meaningVi": "Người ký kết hợp đồng lao động với người lao động, trả lương và quản lý, điều hành hoạt động lao động. Người sử dụng lao động có thể là chủ doanh nghiệp, người đại diện hợp pháp của doanh nghiệp, hoặc người được ủy quyền quản lý lao động. Trách nhiệm của người sử dụng lao động bao gồm đảm bảo điều kiện làm việc an toàn, trả lương đúng hạn, và tuân thủ các quy định của pháp luật lao động.",
        "context": "고용 계약, 노사 관계, 노동 분쟁 해결에서 사용",
        "culturalNote": "한국에서는 '사용자'가 법률 용어로 명확히 정의되며, 근로기준법상 사용자는 부당노동행위 금지, 안전배려의무 등 다양한 법적 책임을 진다. 베트남에서는 người sử dụng lao động이 일반적이며, chủ lao động(노동주)와 혼용되기도 한다. 한국은 노사관계가 법으로 엄격히 규율되지만, 베트남은 상대적으로 사용자의 재량권이 크고 노동조합 활동이 제한적인 경우가 많다. 따라서 통역 시 양국의 노사 문화 차이와 법적 책임 범위를 명확히 설명하는 것이 중요하다.",
        "commonMistakes": [
            {
                "mistake": "chủ nhân으로 번역",
                "correction": "người sử dụng lao động 사용",
                "explanation": "chủ nhân은 주인이라는 뜻으로 법률 용어가 아니며, 공식 문서에서는 người sử dụng lao động을 사용해야 함"
            },
            {
                "mistake": "사용자를 giám đốc(사장)로만 번역",
                "correction": "người sử dụng lao động으로 포괄적으로 통역",
                "explanation": "사용자는 사업주뿐 아니라 사업 경영 담당자를 포함하는 법적 개념이므로 특정 직급으로 한정하면 안 됨"
            },
            {
                "mistake": "사용자 책임을 베트남 기준으로만 설명",
                "correction": "한국 근로기준법상 사용자 의무를 명확히 전달",
                "explanation": "한국은 안전배려의무, 부당노동행위 금지 등 사용자 책임이 베트남보다 광범위하므로 차이를 설명해야 함"
            }
        ],
        "examples": [
            {
                "ko": "사용자는 근로자에게 최저임금 이상을 지급할 의무가 있습니다.",
                "vi": "Người sử dụng lao động có nghĩa vụ trả lương tối thiểu trở lên cho người lao động.",
                "situation": "formal"
            },
            {
                "ko": "사용자가 일방적으로 근로조건을 변경할 수 없습니다.",
                "vi": "Người sử dụng lao động không thể đơn phương thay đổi điều kiện lao động.",
                "situation": "formal"
            },
            {
                "ko": "사용자 측에서 안전교육을 실시해야 합니다.",
                "vi": "Phía người sử dụng lao động phải thực hiện đào tạo an toàn.",
                "situation": "onsite"
            }
        ],
        "relatedTerms": ["nguoi-lao-dong", "hop-dong-lao-dong-co-thoi-han", "sa-thai"]
    },
    {
        "slug": "hop-dong-lao-dong-co-thoi-han",
        "korean": "기간제근로계약",
        "vietnamese": "hợp đồng lao động có thời hạn",
        "hanja": "期間制勤勞契約",
        "hanjaReading": "期(기약할 기) + 間(사이 간) + 制(제도 제) + 勤(부지런할 근) + 勞(일할 로) + 契(맺을 계) + 約(약속할 약)",
        "pronunciation": "헙 동 라오 동 꼬 터이 한",
        "meaningKo": "근로계약 기간이 정해진 계약으로, 계약 종료일이 명시되어 있는 근로 형태. 통역 시 한국의 기간제 근로자 보호법과 베트남의 유기계약 규정을 구분해야 하며, 계약 갱신 및 무기계약 전환 조건이 양국에서 다르다는 점을 명확히 전달해야 한다. 한국에서는 2년을 초과하여 기간제 계약을 사용하면 기간의 정함이 없는 근로계약으로 간주되지만, 베트남은 최대 36개월까지 유기계약이 가능하고 갱신 횟수 제한이 다르므로 주의가 필요하다. 또한 한국은 부당한 기간제 사용을 제한하는 법률이 있지만, 베트남은 사용자의 재량이 상대적으로 크므로 이러한 차이를 통역 시 설명해야 한다.",
        "meaningVi": "Hợp đồng lao động có xác định thời hạn làm việc cụ thể, thường từ đủ 12 tháng đến 36 tháng. Theo Bộ luật Lao động Việt Nam, hợp đồng lao động có thời hạn có thể được gia hạn nhưng tổng thời gian không quá 36 tháng, sau đó phải chuyển thành hợp đồng không xác định thời hạn nếu tiếp tục làm việc. Hợp đồng này thường được sử dụng cho công việc theo dự án hoặc công việc có tính chất tạm thời.",
        "context": "고용 계약 체결, 계약직 채용, 계약 갱신 협상에서 사용",
        "culturalNote": "한국에서는 기간제 근로자에 대한 차별을 금지하고 2년 초과 시 정규직 전환을 의무화하는 등 보호 규정이 강하다. 베트남에서는 hợp đồng lao động có thời hạn이 일반적이며, 최대 36개월까지 가능하고 그 이후 무기계약(hợp đồng không xác định thời hạn)으로 전환된다. 그러나 베트남에서는 계약 만료 시 갱신하지 않는 것이 상대적으로 쉬우므로, 한국의 근로자 보호 수준과 차이가 있다. 통역 시 양국의 계약 갱신 및 전환 조건, 해지 절차의 차이를 명확히 설명해야 하며, 특히 한국 기업이 베트남에서 기간제 계약을 사용할 때 현지 법률을 준수하도록 안내해야 한다.",
        "commonMistakes": [
            {
                "mistake": "한국의 2년 기준을 베트남에도 적용",
                "correction": "베트남은 36개월 기준임을 명시",
                "explanation": "한국은 2년 초과 시 무기계약 간주, 베트남은 36개월까지 유기계약 가능"
            },
            {
                "mistake": "hợp đồng tạm thời로 번역",
                "correction": "hợp đồng lao động có thời hạn 사용",
                "explanation": "tạm thời는 임시적이라는 뜻으로 법률 용어가 아니며, có thời hạn이 정확한 표현"
            },
            {
                "mistake": "계약 갱신 거부를 해고로 설명",
                "correction": "계약 만료와 해고는 별개임을 구분",
                "explanation": "기간제 계약은 만료 시 자동 종료되며, 이는 해고(sa thải)와 법적 성격이 다름"
            }
        ],
        "examples": [
            {
                "ko": "이 직원은 1년 기간제근로계약으로 채용되었습니다.",
                "vi": "Nhân viên này được tuyển dụng theo hợp đồng lao động có thời hạn 1 năm.",
                "situation": "formal"
            },
            {
                "ko": "기간제 계약이 2년을 초과하면 무기계약으로 전환됩니다.",
                "vi": "Nếu hợp đồng có thời hạn vượt quá 2 năm (theo luật Hàn Quốc), sẽ chuyển thành hợp đồng không xác định thời hạn.",
                "situation": "formal"
            },
            {
                "ko": "기간제 계약 갱신 여부를 다음 달까지 통보해 드리겠습니다.",
                "vi": "Chúng tôi sẽ thông báo về việc gia hạn hợp đồng có thời hạn trước tháng sau.",
                "situation": "formal"
            }
        ],
        "relatedTerms": ["nguoi-lao-dong", "nguoi-su-dung-lao-dong", "cham-dut-hop-dong"]
    },
    {
        "slug": "cham-dut-hop-dong",
        "korean": "계약해지",
        "vietnamese": "chấm dứt hợp đồng",
        "hanja": "契約解止",
        "hanjaReading": "契(맺을 계) + 約(약속할 약) + 解(풀 해) + 止(그칠 지)",
        "pronunciation": "쩜 쭛 헙 동",
        "meaningKo": "근로계약 당사자 간의 합의 또는 일방의 의사표시로 계약 관계를 종료시키는 법률 행위. 통역 시 합의 해지와 일방적 해지를 구분해야 하며, 한국의 해고 제한 법리와 베트남의 계약 해지 절차가 다르다는 점을 명확히 전달해야 한다. 한국에서는 정당한 사유 없는 해고가 무효이며, 해고 예고 기간 및 해고 수당 지급 의무가 엄격하게 규정되어 있다. 베트남에서도 chấm dứt hợp đồng lao động은 일방적 해지와 합의 해지로 나뉘며, 각각의 법적 요건과 절차가 다르므로 통역 시 정확한 법률 용어를 사용해야 한다. 특히 부당해고 소송이나 노동 분쟁에서 계약해지의 정당성 여부가 핵심 쟁점이 되므로, 양국 법률상 해지 사유와 절차를 정확히 구분하여 설명하는 것이 중요하다.",
        "meaningVi": "Việc chấm dứt quan hệ lao động giữa người lao động và người sử dụng lao động theo thỏa thuận hoặc đơn phương. Chấm dứt hợp đồng có thể do hết hạn hợp đồng, thỏa thuận hai bên, hoặc một bên đơn phương chấm dứt với các điều kiện theo quy định pháp luật. Người lao động có quyền đơn phương chấm dứt hợp đồng với thời gian báo trước, và người sử dụng lao động cũng có quyền chấm dứt hợp đồng với lý do chính đáng và tuân thủ thủ tục pháp luật.",
        "context": "근로계약 종료, 퇴사 처리, 노동 분쟁에서 사용",
        "culturalNote": "한국에서는 근로자 보호를 위해 해고 제한이 엄격하며, 부당해고 시 근로자는 노동위원회에 구제 신청을 할 수 있다. 베트남에서도 chấm dứt hợp đồng은 법률에 따라 엄격히 규율되지만, 합의 해지가 상대적으로 흔하고, 일방적 해지 시에도 절차만 준수하면 가능한 경우가 많다. 한국은 해고 예고 기간(30일) 및 해고 수당 지급이 필수이지만, 베트남은 계약 종류와 해지 사유에 따라 보상금 지급 여부가 달라진다. 통역 시 양국의 해지 절차, 예고 기간, 보상금 규정의 차이를 명확히 설명하고, 특히 부당해고 여부를 판단하는 기준이 다르므로 주의해야 한다.",
        "commonMistakes": [
            {
                "mistake": "모든 계약 종료를 sa thải(해고)로 번역",
                "correction": "합의 해지는 chấm dứt hợp đồng, 일방적 해고는 sa thải로 구분",
                "explanation": "해고는 사용자의 일방적 의사에 의한 것이고, 계약해지는 합의 또는 계약 만료를 포함하는 넓은 개념"
            },
            {
                "mistake": "한국의 해고 예고 기간을 베트남에도 동일하게 적용",
                "correction": "베트남의 báo trước(예고) 기간은 계약 유형별로 다름",
                "explanation": "한국은 30일 예고 원칙이지만, 베트남은 무기계약 45일, 유기계약 30일 등으로 다름"
            },
            {
                "mistake": "계약해지를 nghỉ việc(퇴사)로만 설명",
                "correction": "chấm dứt hợp đồng lao động으로 법률 용어 사용",
                "explanation": "nghỉ việc은 일상 용어이고, 법률 문서에서는 chấm dứt hợp đồng을 사용해야 함"
            }
        ],
        "examples": [
            {
                "ko": "양측 합의 하에 계약을 해지하기로 했습니다.",
                "vi": "Hai bên đã thỏa thuận chấm dứt hợp đồng lao động.",
                "situation": "formal"
            },
            {
                "ko": "회사는 30일 전에 계약해지를 통보해야 합니다.",
                "vi": "Công ty phải thông báo chấm dứt hợp đồng trước 30 ngày.",
                "situation": "formal"
            },
            {
                "ko": "정당한 사유 없이 계약을 해지할 수 없습니다.",
                "vi": "Không thể chấm dứt hợp đồng mà không có lý do chính đáng.",
                "situation": "formal"
            }
        ],
        "relatedTerms": ["sa-thai", "hop-dong-lao-dong-co-thoi-han", "nguoi-lao-dong"]
    },
    {
        "slug": "sa-thai",
        "korean": "해고",
        "vietnamese": "sa thải",
        "hanja": "解雇",
        "hanjaReading": "解(풀 해) + 雇(부릴 고)",
        "pronunciation": "싸 타이",
        "meaningKo": "사용자가 일방적으로 근로계약을 종료시키는 행위. 통역 시 정당한 해고와 부당해고를 명확히 구분해야 하며, 한국의 해고 제한 법리가 매우 엄격하다는 점을 베트남 측에 설명해야 한다. 한국 근로기준법에서는 정당한 이유 없는 해고를 금지하며, 경영상 이유에 의한 해고도 긴박한 경영상 필요, 해고 회피 노력, 합리적 해고 대상자 선정, 노동조합 협의 등 엄격한 요건을 충족해야 한다. 베트남에서도 sa thải는 법률상 정당한 사유가 필요하지만, 한국보다 절차적 요건이 덜 엄격한 경우가 있으므로 양국 법률의 차이를 정확히 전달해야 한다. 특히 부당해고 구제 절차와 복직 명령, 손해배상 규정이 다르므로 주의가 필요하다.",
        "meaningVi": "Hành vi chấm dứt hợp đồng lao động một cách đơn phương của người sử dụng lao động. Sa thải phải có lý do chính đáng theo quy định pháp luật, chẳng hạn như vi phạm kỷ luật lao động nghiêm trọng, không hoàn thành công việc sau khi đã được cảnh báo, hoặc do tình hình kinh doanh khó khăn buộc phải cắt giảm nhân sự. Người lao động bị sa thải trái luật có quyền yêu cầu phục hồi công việc hoặc được bồi thường thiệt hại theo quy định pháp luật.",
        "context": "인사 관리, 노동 분쟁, 부당해고 소송에서 사용",
        "culturalNote": "한국에서는 해고가 매우 민감한 사안이며, 부당해고 시 근로자는 노동위원회에 구제 신청을 하고 복직 명령을 받을 수 있다. 법원도 해고의 정당성을 엄격하게 심사하며, 정당한 이유 없는 해고는 무효로 판단된다. 베트남에서도 sa thải trái luật(부당해고)은 금지되지만, 실무상 절차만 준수하면 해고가 비교적 용이한 편이며, 복직보다는 금전 보상으로 해결되는 경우가 많다. 한국 기업이 베트남 직원을 해고할 때는 베트남 노동법상 절차를 철저히 준수해야 하며, 반대로 베트남 기업이 한국에서 직원을 해고할 때는 한국의 엄격한 해고 제한 법리를 이해해야 한다. 통역 시 양국의 해고 요건, 절차, 구제 수단의 차이를 명확히 설명하는 것이 중요하다.",
        "commonMistakes": [
            {
                "mistake": "sa thải를 계약 만료와 혼동",
                "correction": "계약 만료는 hết hạn hợp đồng, 해고는 sa thải로 구분",
                "explanation": "계약 만료는 자동 종료이고, 해고는 사용자의 일방적 의사표시로 인한 계약 종료"
            },
            {
                "mistake": "정리해고를 일반 해고와 동일하게 번역",
                "correction": "정리해고는 sa thải do tình hình kinh doanh(경영상 이유 해고)로 명시",
                "explanation": "정리해고는 경영상 필요에 의한 것으로, 일반 징계 해고와 법적 요건이 다름"
            },
            {
                "mistake": "한국의 해고 제한을 베트남에도 동일하게 적용",
                "correction": "양국의 해고 요건과 절차 차이를 명시",
                "explanation": "한국은 해고 제한이 매우 엄격하지만, 베트남은 상대적으로 절차적 요건이 덜 엄격함"
            }
        ],
        "examples": [
            {
                "ko": "징계 사유로 직원을 해고했습니다.",
                "vi": "Công ty đã sa thải nhân viên vì lý do kỷ luật.",
                "situation": "formal"
            },
            {
                "ko": "부당해고로 노동위원회에 구제 신청을 했습니다.",
                "vi": "Tôi đã nộp đơn khiếu nại lên Ủy ban Lao động về việc sa thải trái luật.",
                "situation": "formal"
            },
            {
                "ko": "경영 악화로 인해 정리해고를 실시할 예정입니다.",
                "vi": "Do tình hình kinh doanh khó khăn, công ty dự định thực hiện sa thải giảm biên chế.",
                "situation": "formal"
            }
        ],
        "relatedTerms": ["cham-dut-hop-dong", "nguoi-su-dung-lao-dong", "nguoi-lao-dong"]
    },
    {
        "slug": "dinh-cong",
        "korean": "파업",
        "vietnamese": "đình công",
        "hanja": "罷業",
        "hanjaReading": "罷(그만둘 파) + 業(업 업)",
        "pronunciation": "딘 꽁",
        "meaningKo": "근로자들이 근로조건 개선이나 요구 관철을 위해 집단적으로 노무 제공을 거부하는 쟁의행위. 통역 시 한국의 파업권은 헌법상 보장된 기본권이지만, 베트남에서는 đình công이 법률로 엄격히 규제되며 정치적 파업이 금지된다는 점을 명확히 설명해야 한다. 한국에서는 노동조합 및 노동관계조정법에 따라 합법적 파업 절차를 거치면 형사 처벌이나 손해배상 책임이 면제되지만, 베트남은 파업 전 복잡한 절차(조정, 중재 등)를 거쳐야 하고, 절차를 위반한 파업은 불법으로 간주되어 징계 대상이 된다. 또한 한국은 필수공익사업에서도 제한적으로 파업이 가능하지만, 베트남은 특정 산업에서 파업이 원천적으로 금지되므로 이러한 차이를 통역 시 정확히 전달해야 한다.",
        "meaningVi": "Hành vi tập thể của người lao động tạm ngưng làm việc để yêu cầu giải quyết tranh chấp lao động. Theo Bộ luật Lao động Việt Nam, đình công phải tuân thủ các quy trình pháp luật bao gồm hòa giải, trọng tài, và thông báo trước. Đình công trái pháp luật có thể dẫn đến kỷ luật lao động hoặc chấm dứt hợp đồng. Việt Nam cũng cấm đình công trong một số ngành nghề quan trọng như điện, nước, y tế công cộng, và giao thông vận tải.",
        "context": "노사 분쟁, 노동조합 활동, 단체교섭에서 사용",
        "culturalNote": "한국에서는 파업이 헌법상 보장된 노동3권(단결권, 단체교섭권, 단체행동권) 중 하나로 인정되며, 합법적 파업 절차를 거치면 형사·민사 책임이 면제된다. 그러나 베트남에서는 đình công이 법률로 엄격히 통제되며, 정치적 목적의 파업이나 절차를 위반한 파업은 불법으로 간주된다. 베트남은 노동조합이 국가 주도로 운영되는 경우가 많고, 파업보다는 협상과 조정을 통한 해결을 선호한다. 한국은 파업이 노사 대립의 수단으로 자주 활용되지만, 베트남은 파업 발생 시 정부가 적극 개입하여 조기 해결을 유도하는 경우가 많다. 통역 시 양국의 파업 절차, 합법성 요건, 불법 파업의 법적 결과 차이를 명확히 설명해야 한다.",
        "commonMistakes": [
            {
                "mistake": "모든 파업을 bãi công으로 번역",
                "correction": "법률 용어로는 đình công 사용",
                "explanation": "bãi công은 구어체이고, 법률 문서에서는 đình công이 정식 용어"
            },
            {
                "mistake": "한국의 파업권을 베트남에도 동일하게 설명",
                "correction": "베트남은 파업 절차가 엄격하고 정치적 파업이 금지됨을 명시",
                "explanation": "한국은 파업이 헌법상 권리지만, 베트남은 법률로 엄격히 규제되며 절차 위반 시 불법"
            },
            {
                "mistake": "불법 파업을 단순 절차 위반으로 가볍게 설명",
                "correction": "불법 파업 시 징계 및 해고 가능함을 명확히 전달",
                "explanation": "베트남에서 절차 위반 파업은 중대한 법 위반으로 간주되어 엄중한 처벌 대상"
            }
        ],
        "examples": [
            {
                "ko": "노동조합이 임금 인상을 요구하며 파업을 예고했습니다.",
                "vi": "Công đoàn đã thông báo đình công để yêu cầu tăng lương.",
                "situation": "formal"
            },
            {
                "ko": "합법적 절차를 거치지 않은 파업은 불법입니다.",
                "vi": "Đình công không tuân thủ quy trình pháp luật là bất hợp pháp.",
                "situation": "formal"
            },
            {
                "ko": "회사와 노조가 협상하여 파업을 철회했습니다.",
                "vi": "Công ty và công đoàn đã đàm phán và rút lại quyết định đình công.",
                "situation": "formal"
            }
        ],
        "relatedTerms": ["cong-doan", "nguoi-lao-dong", "nguoi-su-dung-lao-dong"]
    },
    {
        "slug": "cong-doan",
        "korean": "노동조합",
        "vietnamese": "công đoàn",
        "hanja": "勞動組合",
        "hanjaReading": "勞(일할 로) + 動(움직일 동) + 組(짤 조) + 合(합할 합)",
        "pronunciation": "꽁 도안",
        "meaningKo": "근로자들이 근로조건의 유지·개선과 근로자의 경제적·사회적 지위 향상을 목적으로 자주적으로 조직한 단체. 통역 시 한국의 노동조합은 자율적이고 다원적인 반면, 베트남의 공đoàn은 국가 주도의 단일 체계라는 점을 명확히 설명해야 한다. 한국에서는 노동조합 및 노동관계조정법에 따라 근로자 2명 이상이면 노조를 설립할 수 있으며, 복수노조가 허용되고, 노조 활동이 법으로 보호된다. 베트남에서는 Tổng Liên đoàn Lao động Việt Nam(베트남 노동총연맹) 산하의 단일 노조 체계로 운영되며, 독립적인 노조 설립이 제한된다. 따라서 양국의 노조 구조, 설립 절차, 활동 범위의 차이를 통역 시 정확히 전달해야 하며, 특히 한국 기업이 베트남에 진출할 때 현지 노조 시스템을 이해하도록 안내해야 한다.",
        "meaningVi": "Tổ chức tự nguyện của người lao động nhằm bảo vệ quyền và lợi ích hợp pháp, chính đáng của người lao động. Tại Việt Nam, công đoàn hoạt động dưới sự lãnh đạo của Đảng Cộng sản và thuộc hệ thống Tổng Liên đoàn Lao động Việt Nam. Công đoàn có vai trò đại diện người lao động trong đàm phán tập thể, giám sát việc thực hiện pháp luật lao động, và hỗ trợ giải quyết tranh chấp lao động.",
        "context": "노사 관계, 단체교섭, 근로조건 협상에서 사용",
        "culturalNote": "한국에서는 노동조합이 자율적으로 설립·운영되며, 기업별·산업별·지역별 노조 등 다양한 형태가 존재한다. 노조 활동은 헌법과 법률로 보호되며, 사용자는 부당노동행위를 금지당한다. 베트남에서는 công đoàn이 국가 주도로 운영되며, Tổng Liên đoàn Lao động Việt Nam 산하에서만 합법적으로 활동할 수 있다. 독립적인 노조 설립은 사실상 불가능하며, 노조는 정부와 협력하여 노사 분쟁을 조정하는 역할을 한다. 한국은 노조 가입률이 낮아지고 있지만 노조의 영향력이 여전히 크며, 베트남은 노조 가입률이 높지만 실질적인 교섭력은 제한적이다. 통역 시 양국의 노조 체계, 설립 절차, 활동 범위, 교섭권의 차이를 명확히 설명하고, 특히 한국 기업이 베트남에서 노조와 협상할 때 현지 관행을 이해하도록 안내해야 한다.",
        "commonMistakes": [
            {
                "mistake": "한국 노조 시스템을 베트Nam에도 동일하게 적용",
                "correction": "베트남은 단일 노조 체계임을 명시",
                "explanation": "한국은 복수노조가 가능하지만, 베트남은 Tổng Liên đoàn Lao động 산하 단일 체계"
            },
            {
                "mistake": "công đoàn을 단순히 '노조'로만 번역",
                "correction": "베트남 공đoàn의 국가 주도 성격을 설명",
                "explanation": "베트남 공đoàn은 한국의 자율적 노조와 성격이 다르므로 맥락 설명 필요"
            },
            {
                "mistake": "노조 설립 절차를 양국 동일하게 설명",
                "correction": "한국은 자유 설립, 베트남은 정부 승인 필요",
                "explanation": "한국은 신고제이지만, 베트남은 Tổng Liên đoàn 가입이 필수"
            }
        ],
        "examples": [
            {
                "ko": "이 회사에는 기업별 노동조합이 있습니다.",
                "vi": "Công ty này có công đoàn cơ sở.",
                "situation": "formal"
            },
            {
                "ko": "노동조합과 임금 협상을 진행 중입니다.",
                "vi": "Đang đàm phán lương với công đoàn.",
                "situation": "formal"
            },
            {
                "ko": "노동조합은 근로자의 권익을 보호합니다.",
                "vi": "Công đoàn bảo vệ quyền lợi của người lao động.",
                "situation": "formal"
            }
        ],
        "relatedTerms": ["dinh-cong", "nguoi-lao-dong", "nguoi-su-dung-lao-dong"]
    },
    {
        "slug": "luong-toi-thieu",
        "korean": "최저임금",
        "vietnamese": "lương tối thiểu",
        "hanja": "最低賃金",
        "hanjaReading": "最(가장 최) + 低(낮을 저) + 賃(품삯 임) + 金(쇠 금)",
        "pronunciation": "르엉 토이 티에우",
        "meaningKo": "국가가 근로자의 생활 안정을 위해 법으로 정한 임금의 최저 한도. 통역 시 한국은 전국 단일 최저임금제를 운영하지만, 베트남은 지역과 업종에 따라 4개 등급으로 차등 적용된다는 점을 명확히 설명해야 한다. 한국에서는 최저임금법에 따라 매년 최저임금위원회가 최저임금을 결정하며, 시간급으로 고시된다. 베트남에서는 lương tối thiểu vùng(지역별 최저임금)이 정부령으로 정해지며, 베트남인과 외국인 근로자에게 각각 다른 기준이 적용될 수 있다. 또한 한국은 최저임금 미만 지급 시 형사 처벌 대상이지만, 베트남은 행정 벌금이 부과되므로 법적 제재의 차이를 통역 시 정확히 전달해야 한다. 특히 한국 기업이 베트남에 진출할 때 현지 최저임금 기준을 준수하고, 사회보험료 등 추가 비용을 고려하도록 안내해야 한다.",
        "meaningVi": "Mức lương thấp nhất mà người sử dụng lao động phải trả cho người lao động theo quy định của pháp luật. Tại Việt Nam, lương tối thiểu được chia thành 4 vùng (vùng 1 đến vùng 4) tùy theo mức độ phát triển kinh tế của từng khu vực. Lương tối thiểu áp dụng cho người lao động làm việc theo hợp đồng lao động và được điều chỉnh định kỳ theo quyết định của Chính phủ. Người sử dụng lao động vi phạm quy định về lương tối thiểu sẽ bị xử phạt hành chính.",
        "context": "임금 협상, 고용 계약, 근로조건 논의에서 사용",
        "culturalNote": "한국에서는 최저임금이 전국적으로 단일하게 적용되며, 매년 인상률이 정치·경제적 쟁점이 된다. 최저임금 미만 지급 시 3년 이하 징역 또는 2천만원 이하 벌금형에 처해진다. 베트남에서는 lương tối thiểu가 지역별로 차등 적용되며(하노이·호치민 등 1급 지역이 가장 높음), 외국인 투자 기업과 베트남 기업 간에도 기준이 다를 수 있다. 베트남은 최저임금 외에도 사회보험, 의료보험, 실업보험 등 의무 가입 비용을 고려해야 하므로, 실제 인건비는 최저임금보다 높다. 통역 시 양국의 최저임금 결정 방식, 적용 범위, 법적 제재의 차이를 명확히 설명하고, 특히 한국 기업이 베트남에서 급여 체계를 설계할 때 현지 법률을 준수하도록 안내해야 한다.",
        "commonMistakes": [
            {
                "mistake": "한국의 단일 최저임금을 베트남에도 적용",
                "correction": "베트남은 4개 지역별로 최저임금이 다름",
                "explanation": "베트남은 vùng 1~4로 나뉘며, 각각 최저임금이 다르게 책정됨"
            },
            {
                "mistake": "lương cơ bản(기본급)과 lương tối thiểu 혼동",
                "correction": "lương tối thiểu는 법정 최저임금, lương cơ bản은 계약상 기본급",
                "explanation": "기본급은 최저임금 이상이어야 하지만, 두 개념은 다름"
            },
            {
                "mistake": "최저임금만 고려하고 사회보험료 제외",
                "correction": "베트남은 사회보험 등 의무 가입 비용 포함하여 계산",
                "explanation": "실제 인건비는 최저임금 + 사회보험료(약 22%) 등을 합산해야 함"
            }
        ],
        "examples": [
            {
                "ko": "2025년 한국 최저임금은 시간당 10,030원입니다.",
                "vi": "Lương tối thiểu Hàn Quốc năm 2025 là 10.030 won mỗi giờ.",
                "situation": "formal"
            },
            {
                "ko": "베트남은 지역별로 최저임금이 다릅니다.",
                "vi": "Việt Nam có lương tối thiểu khác nhau theo từng vùng.",
                "situation": "formal"
            },
            {
                "ko": "최저임금 미만으로 지급하면 법적 처벌을 받습니다.",
                "vi": "Trả lương thấp hơn mức tối thiểu sẽ bị xử phạt theo pháp luật.",
                "situation": "formal"
            }
        ],
        "relatedTerms": ["nguoi-lao-dong", "nguoi-su-dung-lao-dong", "hop-dong-lao-dong-co-thoi-han"]
    },
    {
        "slug": "bao-hiem-xa-hoi",
        "korean": "사회보험",
        "vietnamese": "bảo hiểm xã hội",
        "hanja": "社會保險",
        "hanjaReading": "社(모일 사) + 會(모일 회) + 保(지킬 보) + 險(험할 험)",
        "pronunciation": "바오 히엠 싸 호이",
        "meaningKo": "국가가 국민의 질병·노령·실업·산재 등 사회적 위험으로부터 보호하기 위해 운영하는 강제 보험 제도. 통역 시 한국의 4대 사회보험(국민연금, 건강보험, 고용보험, 산재보험)과 베트남의 bảo hiểm xã hội 체계가 다르다는 점을 명확히 설명해야 한다. 한국에서는 사용자와 근로자가 보험료를 분담하며, 가입 의무가 법으로 엄격히 규정되어 있다. 베트남에서도 bảo hiểm xã hội, bảo hiểm y tế(의료보험), bảo hiểm thất nghiệp(실업보험)가 의무이며, 사용자는 근로자의 사회보험료를 급여에서 공제하고 자신의 부담분과 함께 납부해야 한다. 양국 모두 미가입 시 벌금이나 가산금이 부과되므로, 한국 기업이 베트남에서 직원을 고용할 때 현지 사회보험 가입 의무를 준수하도록 안내해야 한다.",
        "meaningVi": "Chế độ bảo hiểm bắt buộc do Nhà nước tổ chức nhằm bảo vệ người lao động trước các rủi ro như ốm đau, thai sản, tai nạn lao động, hưu trí, và tử tuất. Tại Việt Nam, bảo hiểm xã hội bao gồm bảo hiểm xã hội bắt buộc, bảo hiểm y tế, và bảo hiểm thất nghiệp. Người sử dụng lao động và người lao động đều có nghĩa vụ đóng góp theo tỷ lệ quy định. Việc không tham gia hoặc chậm đóng bảo hiểm xã hội sẽ bị xử phạt hành chính và phải nộp tiền lãi chậm đóng.",
        "context": "고용 계약, 급여 계산, 근로 복지에서 사용",
        "culturalNote": "한국에서는 국민연금, 건강보험, 고용보험, 산재보험을 4대 사회보험이라 부르며, 정규직은 물론 일정 조건을 충족한 비정규직도 의무 가입 대상이다. 사용자와 근로자가 보험료를 절반씩 부담하는 것이 일반적이며(산재보험은 사용자 전액 부담), 미가입 시 추징금과 가산금이 부과된다. 베트남에서는 bảo hiểm xã hội(사회보험), bảo hiểm y tế(의료보험), bảo hiểm thất nghiệp(실업보험)가 의무이며, 사용자가 약 21.5%, 근로자가 약 10.5%를 부담한다. 베트남은 외국인 근로자도 일정 조건 하에 사회보험 가입 의무가 있으므로, 한국 기업이 베트남 현지 직원을 고용할 때 이를 준수해야 한다. 통역 시 양국의 보험 종류, 부담률, 가입 의무, 미가입 시 제재의 차이를 명확히 설명해야 한다.",
        "commonMistakes": [
            {
                "mistake": "한국의 4대 보험을 베트남에도 동일하게 적용",
                "correction": "베트남은 bảo hiểm xã hội, y tế, thất nghiệp 3종으로 구분",
                "explanation": "한국은 국민연금·건강·고용·산재로 나뉘지만, 베트남은 체계가 다름"
            },
            {
                "mistake": "bảo hiểm xã hội를 단순히 '연금'으로만 번역",
                "correction": "bảo hiểm xã hội는 연금, 질병, 출산, 산재 등을 포함하는 포괄 개념",
                "explanation": "베트남 bảo hiểm xã hội는 한국의 국민연금과 산재보험을 합친 개념에 가까움"
            },
            {
                "mistake": "외국인 근로자는 사회보험 가입 불필요하다고 설명",
                "correction": "베트남에서 외국인도 일정 조건 하에 가입 의무",
                "explanation": "2018년부터 베트남은 외국인 근로자도 사회보험 가입 의무화"
            }
        ],
        "examples": [
            {
                "ko": "회사는 직원의 사회보험료를 매달 납부해야 합니다.",
                "vi": "Công ty phải đóng bảo hiểm xã hội cho nhân viên hàng tháng.",
                "situation": "formal"
            },
            {
                "ko": "사회보험 미가입 시 벌금이 부과됩니다.",
                "vi": "Nếu không tham gia bảo hiểm xã hội sẽ bị phạt.",
                "situation": "formal"
            },
            {
                "ko": "근로자는 급여에서 사회보험료가 공제됩니다.",
                "vi": "Người lao động bị khấu trừ phí bảo hiểm xã hội từ lương.",
                "situation": "formal"
            }
        ],
        "relatedTerms": ["nguoi-lao-dong", "nguoi-su-dung-lao-dong", "luong-toi-thieu"]
    },
    {
        "slug": "tai-nan-lao-dong",
        "korean": "산업재해",
        "vietnamese": "tai nạn lao động",
        "hanja": "産業災害",
        "hanjaReading": "産(낳을 산) + 業(업 업) + 災(재앙 재) + 害(해칠 해)",
        "pronunciation": "따이 난 라오 동",
        "meaningKo": "근로자가 업무 수행 중 또는 업무와 관련하여 발생한 부상·질병·사망 등의 재해. 통역 시 한국의 산업재해보상보험법과 베트남의 산재 보상 규정이 다르다는 점을 명확히 설명해야 한다. 한국에서는 업무상 재해 인정 기준이 명확하며, 산재보험을 통해 치료비, 휴업급여, 장해급여, 유족급여 등이 지급된다. 베트남에서도 tai nạn lao động 발생 시 bảo hiểm xã hội(사회보험)를 통해 보상이 이루어지지만, 인정 기준과 보상 수준이 한국과 다를 수 있다. 특히 한국은 업무상 질병(직업병)의 범위가 넓고 인정률이 높지만, 베트남은 상대적으로 제한적이므로 통역 시 이러한 차이를 정확히 전달해야 한다. 또한 한국 기업이 베트남에서 산재 사고 발생 시 현지 법률에 따른 신고 의무와 보상 절차를 준수하도록 안내해야 한다.",
        "meaningVi": "Sự cố xảy ra trong quá trình làm việc hoặc liên quan đến công việc gây ra thương tích, bệnh tật hoặc tử vong cho người lao động. Theo pháp luật Việt Nam, khi xảy ra tai nạn lao động, người sử dụng lao động phải báo cáo cho cơ quan chức năng, điều tra nguyên nhân, và thực hiện bồi thường theo quy định. Người lao động bị tai nạn lao động được hưởng các chế độ từ bảo hiểm xã hội bao gồm chi phí điều trị, trợ cấp thương tật, và trợ cấp hưu trí nếu bị mất khả năng lao động.",
        "context": "산업 안전, 산재 보상, 안전 교육에서 사용",
        "culturalNote": "한국에서는 산업재해가 발생하면 사용자는 즉시 산재 신고를 해야 하며, 산재보험을 통해 근로자가 보상을 받는다. 산재 은폐 시 사용자는 형사 처벌을 받을 수 있으며, 중대재해처벌법에 따라 경영책임자도 처벌 대상이 된다. 베트남에서도 tai nạn lao động 발생 시 사용자는 즉시 보고하고 조사해야 하며, 근로자는 bảo hiểm xã hội를 통해 보상을 받는다. 그러나 베트남은 산재 인정 기준이 한국보다 엄격하고, 보상 수준도 낮은 편이다. 또한 베트남은 산업 안전 감독이 상대적으로 느슨하여 산재 발생률이 높은 편이므로, 한국 기업이 베트남에 진출할 때 안전 교육과 예방 조치를 철저히 하도록 안내해야 한다. 통역 시 양국의 산재 인정 기준, 신고 절차, 보상 내용, 법적 책임의 차이를 명확히 설명해야 한다.",
        "commonMistakes": [
            {
                "mistake": "tai nạn(사고)과 tai nạn lao động(산재) 혼동",
                "correction": "일반 사고는 tai nạn, 업무상 재해는 tai nạn lao động",
                "explanation": "산재는 업무 관련성이 있어야 하며, 일반 사고와 법적 보상이 다름"
            },
            {
                "mistake": "한국의 산재 인정 기준을 베트남에도 적용",
                "correction": "베트남의 tai nạn lao động 인정 기준은 더 제한적",
                "explanation": "한국은 업무상 질병 범위가 넓지만, 베트남은 상대적으로 좁음"
            },
            {
                "mistake": "산재 발생 시 신고 의무를 간과",
                "correction": "양국 모두 즉시 신고 의무가 있으며, 미신고 시 처벌",
                "explanation": "한국은 산재 은폐 시 형사 처벌, 베트남도 행정 처분 대상"
            }
        ],
        "examples": [
            {
                "ko": "작업 중 산업재해가 발생하여 즉시 신고했습니다.",
                "vi": "Đã xảy ra tai nạn lao động trong quá trình làm việc và đã báo cáo ngay.",
                "situation": "formal"
            },
            {
                "ko": "산업재해 예방을 위해 안전 교육을 실시합니다.",
                "vi": "Thực hiện đào tạo an toàn để phòng ngừa tai nạn lao động.",
                "situation": "onsite"
            },
            {
                "ko": "산재로 인정되어 치료비를 보상받았습니다.",
                "vi": "Được công nhận là tai nạn lao động và nhận bồi thường chi phí điều trị.",
                "situation": "formal"
            }
        ],
        "relatedTerms": ["nguoi-lao-dong", "bao-hiem-xa-hoi", "nguoi-su-dung-lao-dong"]
    }
]

# 중복 필터링
new_terms_filtered = [term for term in new_terms if term['slug'] not in existing_slugs]

# 데이터 추가
data.extend(new_terms_filtered)

# 파일 저장
with open(file_path, 'w', encoding='utf-8') as f:
    json.dump(data, f, ensure_ascii=False, indent=2)

print(f"✅ {len(new_terms_filtered)}개 노동법/고용법 용어 추가 완료")
print(f"📊 총 용어 수: {len(data)}개")
print(f"🔍 추가된 용어: {', '.join([t['slug'] for t in new_terms_filtered])}")
