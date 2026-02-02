#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
한-베 통역 용어 플랫폼 - 법률 도메인 용어 추가 스크립트
테마: 공정거래법 심화 (시장지배적지위남용, 기업결합, 부당공동행위, 불공정거래, 하도급법, 가맹사업법, 대규모유통업, 표시광고, 동의의결, 과징금)
"""

import json
import os

# 스크립트 파일의 디렉토리 경로
SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
PROJECT_ROOT = os.path.abspath(os.path.join(SCRIPT_DIR, "../.."))
LEGAL_JSON_PATH = os.path.join(PROJECT_ROOT, "src/data/terms/legal.json")

# 추가할 용어 데이터 (Tier S 기준)
NEW_TERMS = [
    {
        "slug": "lam-dung-vi-the-thong-tri-thi-truong",
        "korean": "시장지배적지위남용",
        "vietnamese": "Lạm dụng vị thế thống trị thị trường",
        "hanja": "市場支配的地位濫用",
        "hanjaReading": "市(저자 시) + 場(마당 장) + 支(지탱할 지) + 配(나눌 배) + 的(과녁 적) + 地(땅 지) + 位(자리 위) + 濫(넘칠 람) + 用(쓸 용)",
        "pronunciation": "시장지배적지위남용",
        "meaningKo": "시장에서 지배적 지위를 가진 사업자가 그 지위를 이용하여 부당하게 경쟁을 제한하거나 소비자 이익을 침해하는 행위를 말합니다. 통역 시 베트남어로 'lạm dụng vị thế thống trị'만 사용하면 법적 의미가 약해지므로 반드시 'thị trường'을 붙여 시장 개념을 명확히 해야 합니다. 독과점 규제와 혼동하지 말고, 이미 지배적 지위를 가진 사업자의 '행위'를 규제하는 것임을 강조해야 합니다. 베트남 경쟁법(Luật Cạnh tranh)에서도 유사한 개념이 있으므로 양국 법제 비교가 필요합니다.",
        "meaningVi": "Hành vi của doanh nghiệp có vị thế thống trị thị trường lợi dụng vị thế đó để hạn chế cạnh tranh bất hợp lý hoặc xâm hại lợi ích người tiêu dùng. Theo pháp luật cạnh tranh Việt Nam, đây cũng là hành vi bị nghiêm cấm và có thể bị xử phạt nặng.",
        "context": "공정거래위원회 심의, 독과점 규제, 경쟁법 소송",
        "culturalNote": "한국은 공정거래법으로 시장지배적 지위 남용을 엄격히 규제하며, 대기업의 불공정 행위를 집중 감시합니다. 베트남도 경쟁법(Luật Cạnh tranh 2018)에서 유사한 규정을 두고 있으나, 한국처럼 공정위 같은 강력한 전담 기관이 아닌 경쟁관리국(Cục Quản lý cạnh tranh)에서 담당하며 집행력이 상대적으로 약한 편입니다. 통역 시 양국의 집행 수준 차이를 이해하고 설명해야 합니다.",
        "commonMistakes": [
            {
                "mistake": "독점(độc quyền)과 혼용",
                "correction": "시장지배적 지위는 반드시 독점이 아님",
                "explanation": "시장점유율 50% 이상이면 추정되지만, 독점과는 다른 개념입니다. '독점'은 시장 구조, '지배적 지위 남용'은 행위를 규제하는 것입니다."
            },
            {
                "mistake": "'thống trị thị trường'만 번역",
                "correction": "'lạm dụng'(남용) 개념 반드시 포함",
                "explanation": "지위 자체는 문제가 아니고, 그것을 '남용'하는 행위가 위법입니다. 베트남어에서 'lạm dụng'을 빠뜨리면 의미가 완전히 달라집니다."
            },
            {
                "mistake": "불공정거래행위와 동일시",
                "correction": "별개의 법 위반 유형",
                "explanation": "불공정거래는 모든 사업자가 대상이지만, 시장지배적 지위 남용은 특정 지위를 가진 사업자만 해당됩니다."
            }
        ],
        "examples": [
            {
                "ko": "공정거래위원회는 해당 기업이 시장지배적지위를 남용하여 경쟁사를 배제했다고 판단했습니다.",
                "vi": "Ủy ban Cạnh tranh Công bằng đã kết luận rằng doanh nghiệp này đã lạm dụng vị thế thống trị thị trường để loại trừ đối thủ cạnh tranh.",
                "situation": "formal"
            },
            {
                "ko": "시장점유율 60%를 가진 사업자가 납품단가를 일방적으로 인하한 것은 지위 남용에 해당합니다.",
                "vi": "Việc doanh nghiệp có 60% thị phần đơn phương hạ giá cung ứng là hành vi lạm dụng vị thế.",
                "situation": "onsite"
            },
            {
                "ko": "이 계약 조항은 시장지배적지위남용 소지가 있어 수정이 필요합니다.",
                "vi": "Điều khoản hợp đồng này có dấu hiệu lạm dụng vị thế thống trị thị trường nên cần sửa đổi.",
                "situation": "formal"
            }
        ],
        "relatedTerms": ["불공정거래행위", "독과점", "경쟁제한", "시장점유율"]
    },
    {
        "slug": "sap-nhap-doanh-nghiep",
        "korean": "기업결합",
        "vietnamese": "Sáp nhập doanh nghiệp",
        "hanja": "企業結合",
        "hanjaReading": "企(꾀할 기) + 業(업 업) + 結(맺을 결) + 合(합할 합)",
        "pronunciation": "기업결합",
        "meaningKo": "둘 이상의 기업이 합병, 영업양수, 주식취득 등을 통해 결합하는 행위로, 경쟁 제한 우려가 있으면 공정거래위원회의 사전 신고 및 심사 대상이 됩니다. 통역 시 베트남어 'sáp nhập'은 합병(merger)을 주로 의미하므로, 주식 취득이나 임원 겸임 등 넓은 개념을 전달할 때는 'kết hợp doanh nghiệp' 또는 'tập trung kinh tế'라는 표현을 병행해야 합니다. 한국은 M&A 거래 전 반드시 공정위 신고를 해야 하며, 미신고 시 과징금과 거래 무효 처분을 받을 수 있어 통역사가 절차를 정확히 이해해야 합니다.",
        "meaningVi": "Hành vi hai hoặc nhiều doanh nghiệp kết hợp thông qua sáp nhập, mua lại kinh doanh, mua cổ phần, v.v. Nếu có nguy cơ hạn chế cạnh tranh thì phải báo cáo trước và được Ủy ban Cạnh tranh Công bằng thẩm tra. Ở Việt Nam cũng có quy định tương tự trong Luật Cạnh tranh.",
        "context": "M&A 거래, 공정위 신고, 인수합병 자문",
        "culturalNote": "한국은 일정 규모 이상(자산 3천억 원 이상 등)의 기업결합을 공정위에 사전 신고해야 하며, 심사 기간이 30일~120일 소요됩니다. 베트남도 경쟁법상 '경제 집중'(tập trung kinh tế) 신고 의무가 있으나, 한국보다 기준 금액이 높고 심사 기간도 짧아(보통 60일) 실무적 차이가 큽니다. 통역 시 양국의 신고 기준과 절차 차이를 명확히 전달해야 클라이언트의 오해를 방지할 수 있습니다.",
        "commonMistakes": [
            {
                "mistake": "'hợp nhất'(합병)로만 번역",
                "correction": "기업결합은 합병보다 넓은 개념",
                "explanation": "주식 취득, 임원 겸임, 영업 양수 등도 모두 포함되므로 'kết hợp doanh nghiệp' 또는 'tập trung kinh tế'로 번역해야 정확합니다."
            },
            {
                "mistake": "신고 의무를 '허가'로 오역",
                "correction": "신고(báo cáo) vs 허가(cho phép) 구분",
                "explanation": "한국 공정거래법상 기업결합은 '신고' 대상이며, 공정위가 제한하지 않으면 진행 가능합니다. 허가제가 아닙니다."
            },
            {
                "mistake": "베트남 법과 동일하게 설명",
                "correction": "양국 신고 기준 금액 차이 명시",
                "explanation": "한국은 3천억 원, 베트남은 약 3조 VND(약 1,500억 원) 이상으로 기준이 다릅니다."
            }
        ],
        "examples": [
            {
                "ko": "이번 인수 건은 자산 총액이 5천억 원을 초과하여 기업결합 신고 대상입니다.",
                "vi": "Vụ mua lại này có tổng tài sản vượt 500 tỷ won nên thuộc đối tượng phải báo cáo kết hợp doanh nghiệp.",
                "situation": "formal"
            },
            {
                "ko": "공정위는 이 기업결합이 경쟁을 실질적으로 제한한다고 보아 시정명령을 내렸습니다.",
                "vi": "Ủy ban Cạnh tranh Công bằng đã ra lệnh sửa chữa vì cho rằng sáp nhập này hạn chế cạnh tranh đáng kể.",
                "situation": "formal"
            },
            {
                "ko": "기업결합 심사에서 조건부 승인을 받았으니, 해당 조건을 이행해야 합니다.",
                "vi": "Đã nhận phê duyệt có điều kiện trong thẩm tra kết hợp doanh nghiệp, nên phải thực hiện các điều kiện đó.",
                "situation": "onsite"
            }
        ],
        "relatedTerms": ["인수합병", "합병", "주식취득", "영업양수"]
    },
    {
        "slug": "hanh-vi-dong-loat-bat-hop-ly",
        "korean": "부당공동행위",
        "vietnamese": "Hành vi đồng loạt bất hợp lý",
        "hanja": "不當共同行爲",
        "hanjaReading": "不(아니 불) + 當(마땅 당) + 共(함께 공) + 同(한가지 동) + 行(다닐 행) + 爲(할 위)",
        "pronunciation": "부당공동행위",
        "meaningKo": "사업자들이 계약, 협정, 결의 등으로 가격, 거래조건, 생산량 등을 공동으로 결정하거나 조작하여 경쟁을 제한하는 행위를 말합니다. 일명 '카르텔'(cartel)이라고도 하며, 공정거래법상 가장 중대한 위반 행위 중 하나입니다. 통역 시 베트남어 'thỏa thuận hạn chế cạnh tranh'(경쟁 제한 합의)도 사용 가능하나, 법률 문서에서는 'hành vi đồng loạt bất hợp lý'가 공식 용어입니다. 한국은 담합에 대해 매우 강력한 처벌(매출액의 10% 이하 과징금, 형사 처벌)을 부과하므로, 통역 시 이 위험성을 강조해야 합니다.",
        "meaningVi": "Hành vi các doanh nghiệp thông qua hợp đồng, thỏa thuận, quyết định chung để quy định hoặc thao túng giá cả, điều kiện giao dịch, sản lượng, v.v., nhằm hạn chế cạnh tranh. Còn gọi là 'cartel', là vi phạm nghiêm trọng nhất trong luật cạnh tranh.",
        "context": "담합 조사, 입찰 담합, 가격 카르텔",
        "culturalNote": "한국은 입찰 담합, 가격 담합 등에 대해 공정위가 강력히 단속하며, 건설업계, 제약업계 등에서 적발 사례가 많습니다. 베트남도 경쟁법에서 '경쟁 제한 합의'(Thỏa thuận hạn chế cạnh tranh)를 금지하지만, 한국만큼 적발 사례가 많지 않고 과징금 수준도 낮은 편입니다. 통역 시 한국의 엄격한 법 집행 환경을 베트남 클라이언트에게 충분히 경고해야 합니다.",
        "commonMistakes": [
            {
                "mistake": "'cấu kết'(결탁)로 번역",
                "correction": "'hành vi đồng loạt' 또는 'thỏa thuận hạn chế cạnh tranh'",
                "explanation": "'cấu kết'은 범죄적 뉘앙스가 강하고 법률 용어로 부적합합니다."
            },
            {
                "mistake": "카르텔(cartel)만 사용",
                "correction": "공식 법률 용어와 병기",
                "explanation": "'cartel'은 통칭이므로 법률 문서에서는 베트남어 정식 용어를 함께 써야 합니다."
            },
            {
                "mistake": "과징금만 언급하고 형사 처벌 누락",
                "correction": "한국은 형사 처벌도 가능함을 명시",
                "explanation": "한국은 담합 주도자에게 3년 이하 징역 또는 2억 원 이하 벌금을 부과할 수 있어, 베트남보다 훨씬 엄격합니다."
            }
        ],
        "examples": [
            {
                "ko": "공정위는 5개 건설사가 입찰에서 부당공동행위를 했다고 판단하고 총 500억 원의 과징금을 부과했습니다.",
                "vi": "Ủy ban Cạnh tranh Công bằng đã kết luận 5 công ty xây dựng có hành vi đồng loạt bất hợp lý trong đấu thầu và phạt tổng cộng 50 tỷ won.",
                "situation": "formal"
            },
            {
                "ko": "가격 담합은 부당공동행위로 적발되면 형사 처벌까지 받을 수 있습니다.",
                "vi": "Thỏa thuận giá cả nếu bị phát hiện là hành vi đồng loạt bất hợp lý có thể bị xử lý hình sự.",
                "situation": "onsite"
            },
            {
                "ko": "이 협회의 회원사 간 가격 합의는 명백한 부당공동행위입니다.",
                "vi": "Thỏa thuận giá giữa các thành viên hiệp hội này rõ ràng là hành vi đồng loạt bất hợp lý.",
                "situation": "formal"
            }
        ],
        "relatedTerms": ["카르텔", "담합", "가격담합", "입찰담합"]
    },
    {
        "slug": "hanh-vi-giao-dich-bat-cong-bang",
        "korean": "불공정거래행위",
        "vietnamese": "Hành vi giao dịch bất công bằng",
        "hanja": "不公正去來行爲",
        "hanjaReading": "不(아니 불) + 公(공평할 공) + 正(바를 정) + 去(갈 거) + 來(올 래) + 行(다닐 행) + 爲(할 위)",
        "pronunciation": "불공정거래행위",
        "meaningKo": "사업자가 공정한 거래 질서를 해치는 행위로, 거래 거절, 차별 취급, 경쟁사 배제, 부당 염매, 끼워팔기, 거래상 지위 남용 등 총 9가지 유형이 법으로 정해져 있습니다. 통역 시 베트남어 'hành vi cạnh tranh không lành mạnh'(불건전 경쟁 행위)와 혼동하지 말아야 하며, 'bất công bằng'(불공정)을 명확히 표현해야 합니다. 한국 공정거래법의 핵심 규제 영역이며, 시장지배적 지위가 없는 일반 사업자도 위반 주체가 될 수 있습니다. 베트남 클라이언트에게 한국의 넓은 규제 범위를 충분히 설명해야 합니다.",
        "meaningVi": "Hành vi của doanh nghiệp làm tổn hại đến trật tự giao dịch công bằng, bao gồm 9 loại như từ chối giao dịch, phân biệt đối xử, loại trừ đối thủ, bán phá giá, bán kèm, lạm dụng địa vị giao dịch, v.v. Luật quy định cụ thể từng loại.",
        "context": "거래 계약 심사, 유통 계약, 대리점 계약",
        "culturalNote": "한국은 공정거래법으로 불공정거래행위 9가지 유형을 명확히 규정하고 있으며, 대기업과 중소기업 간 거래에서 특히 엄격히 적용됩니다. 베트남은 경쟁법에서 '불공정 경쟁'(cạnh tranh không lành mạnh)을 금지하지만, 한국처럼 세밀한 유형 분류는 없고 주로 상표 도용, 영업비밀 침해 등에 초점을 맞춥니다. 통역 시 양국의 규제 초점 차이를 명확히 전달해야 합니다.",
        "commonMistakes": [
            {
                "mistake": "'cạnh tranh không lành mạnh'로 번역",
                "correction": "'giao dịch bất công bằng'이 정확",
                "explanation": "베트남 경쟁법의 '불공정 경쟁'과 한국 공정거래법의 '불공정거래'는 다른 개념입니다."
            },
            {
                "mistake": "시장지배적 지위 남용과 동일시",
                "correction": "별개의 위반 유형",
                "explanation": "지배적 지위 남용은 특정 사업자만 해당되지만, 불공정거래행위는 모든 사업자가 대상입니다."
            },
            {
                "mistake": "9가지 유형 중 일부만 설명",
                "correction": "전체 유형 파악 필수",
                "explanation": "거래 거절, 차별 취급, 부당 염매, 끼워팔기, 거래 강제, 사업 활동 방해, 부당 이익 제공 요구, 거래상 지위 남용, 구속 조건부 거래 등 9가지를 모두 알아야 합니다."
            }
        ],
        "examples": [
            {
                "ko": "대형마트가 납품업체에 판촉비를 일방적으로 요구한 것은 불공정거래행위에 해당합니다.",
                "vi": "Việc siêu thị lớn đơn phương yêu cầu nhà cung ứng chi trả phí khuyến mại là hành vi giao dịch bất công bằng.",
                "situation": "onsite"
            },
            {
                "ko": "이 계약의 끼워팔기 조항은 불공정거래행위 소지가 있어 삭제해야 합니다.",
                "vi": "Điều khoản bán kèm trong hợp đồng này có dấu hiệu vi phạm hành vi giao dịch bất công bằng nên cần xóa bỏ.",
                "situation": "formal"
            },
            {
                "ko": "공정위는 해당 기업의 거래 거절 행위를 불공정거래행위로 판단하고 시정명령을 내렸습니다.",
                "vi": "Ủy ban Cạnh tranh Công bằng đã xác định hành vi từ chối giao dịch của doanh nghiệp này là hành vi giao dịch bất công bằng và ra lệnh sửa chữa.",
                "situation": "formal"
            }
        ],
        "relatedTerms": ["끼워팔기", "거래거절", "부당염매", "거래상지위남용"]
    },
    {
        "slug": "luat-hop-dong-thau",
        "korean": "하도급법",
        "vietnamese": "Luật hợp đồng thầu",
        "hanja": "下都給法",
        "hanjaReading": "下(아래 하) + 都(도읍 도) + 給(줄 급) + 法(법 법)",
        "pronunciation": "하도급법",
        "meaningKo": "하도급거래 공정화에 관한 법률의 약칭으로, 원사업자가 수급사업자(하도급업체)에게 제조, 건설, 용역 등을 위탁할 때 부당한 행위를 하지 못하도록 규제하는 법입니다. 통역 시 베트남어로 'luật thầu phụ'(하청법)보다는 'luật hợp đồng thầu'가 더 공식적이며, 'công bằng hóa giao dịch thầu phụ'(하도급 거래 공정화)라는 개념을 함께 설명해야 합니다. 한국은 서면 발급 의무, 부당 단가 인하 금지, 대금 지급 기한(60일 이내) 등을 엄격히 규정하며, 위반 시 공정위 제재와 형사 처벌이 가능합니다.",
        "meaningVi": "Luật về công bằng hóa giao dịch thầu phụ, quy định nhằm ngăn chặn hành vi bất hợp lý của nhà thầu chính đối với nhà thầu phụ trong các hợp đồng gia công, xây dựng, dịch vụ. Luật quy định nghiêm ngặt về phát hành văn bản, cấm hạ giá đơn phương, thời hạn thanh toán 60 ngày.",
        "context": "제조 위탁 계약, 건설 하도급, 용역 계약",
        "culturalNote": "한국은 대기업과 중소기업 간 불공정 거래를 방지하기 위해 하도급법을 매우 엄격하게 운영하며, 공정위가 정기적으로 조사합니다. 특히 서면 미발급, 단가 인하 강요, 대금 미지급 등은 중점 단속 대상입니다. 베트남도 하도급 관계가 많지만, 한국처럼 별도의 하도급 전문 법률은 없고 민법과 상법으로 규율하며, 분쟁 시 법원 소송으로 해결하는 경우가 많습니다. 통역 시 한국의 강력한 사전 규제 체계를 베트남 클라이언트에게 명확히 전달해야 합니다.",
        "commonMistakes": [
            {
                "mistake": "'luật thầu phụ'로만 번역",
                "correction": "'luật hợp đồng thầu' 또는 'luật công bằng hóa thầu phụ'",
                "explanation": "'thầu phụ'는 하청을 의미하지만, 법률명은 '공정화'라는 취지를 담아야 합니다."
            },
            {
                "mistake": "민법상 계약으로 설명",
                "correction": "별도의 특별법임을 명시",
                "explanation": "하도급법은 민법보다 우선 적용되는 특별법이며, 공정위가 직권으로 조사할 수 있습니다."
            },
            {
                "mistake": "대금 지급 기한 90일로 잘못 안내",
                "correction": "60일 이내 (제조업 등), 건설은 별도",
                "explanation": "제조·수리·용역은 60일 이내, 건설은 '건설산업기본법'에 따라 다르므로 구분해야 합니다."
            }
        ],
        "examples": [
            {
                "ko": "하도급법에 따라 원사업자는 수급사업자에게 반드시 서면으로 발주 내용을 통지해야 합니다.",
                "vi": "Theo luật hợp đồng thầu, nhà thầu chính phải thông báo nội dung đặt hàng bằng văn bản cho nhà thầu phụ.",
                "situation": "formal"
            },
            {
                "ko": "이 계약은 하도급법 위반 소지가 있으니 법률 검토가 필요합니다.",
                "vi": "Hợp đồng này có dấu hiệu vi phạm luật hợp đồng thầu nên cần xem xét pháp lý.",
                "situation": "onsite"
            },
            {
                "ko": "하도급 대금을 60일 이내에 지급하지 않으면 지연 이자를 물어야 합니다.",
                "vi": "Nếu không thanh toán tiền thầu phụ trong 60 ngày thì phải trả lãi chậm trả.",
                "situation": "formal"
            }
        ],
        "relatedTerms": ["원사업자", "수급사업자", "하도급대금", "서면발급의무"]
    },
    {
        "slug": "luat-kinh-doanh-nhuong-quyen",
        "korean": "가맹사업법",
        "vietnamese": "Luật kinh doanh nhượng quyền",
        "hanja": "加盟事業法",
        "hanjaReading": "加(더할 가) + 盟(맹세 맹) + 事(일 사) + 業(업 업) + 法(법 법)",
        "pronunciation": "가맹사업법",
        "meaningKo": "가맹사업거래의 공정화에 관한 법률의 약칭으로, 프랜차이즈 본부(가맹본부)와 가맹점주 간 거래를 규제하는 법입니다. 통역 시 베트남어 'nhượng quyền thương mại'(상업 프랜차이즈)과 'luật kinh doanh nhượng quyền'을 병행해야 하며, 정보공개서 제공 의무, 허위·과장 광고 금지, 불공정 계약 조항 규제 등을 포함합니다. 한국은 가맹본부가 가맹점주에게 사전에 '정보공개서'를 의무적으로 제공해야 하며, 미제공 시 형사 처벌(3년 이하 징역 또는 1억 원 이하 벌금)이 가능합니다. 베트남에도 프랜차이즈가 많지만 한국처럼 상세한 법 규정은 없으므로, 통역 시 이 차이를 명확히 해야 합니다.",
        "meaningVi": "Luật về công bằng hóa kinh doanh nhượng quyền (franchise), điều chỉnh giao dịch giữa trụ sở nhượng quyền và chủ cửa hàng nhượng quyền. Quy định nghĩa vụ cung cấp bản công khai thông tin, cấm quảng cáo gian dối, quy định điều khoản hợp đồng bất công.",
        "context": "프랜차이즈 계약, 가맹점 모집, 정보공개서 작성",
        "culturalNote": "한국은 편의점, 치킨집, 커피숍 등 프랜차이즈 산업이 매우 발달했으며, 가맹본부의 불공정 행위를 방지하기 위해 가맹사업법을 엄격히 적용합니다. 특히 정보공개서 미제공, 예상 매출 허위 과장, 가맹점주에게 부당한 비용 전가 등은 중점 단속 대상입니다. 베트남도 프랜차이즈가 증가하고 있으나, 별도의 프랜차이즈 전문 법률은 없고 상법과 경쟁법으로 규율하며, 정보공개서 제도도 없습니다. 통역 시 한국의 상세한 규제 체계를 베트남 클라이언트에게 충분히 설명해야 합니다.",
        "commonMistakes": [
            {
                "mistake": "'nhượng quyền thương mại'로만 번역",
                "correction": "'luật kinh doanh nhượng quyền' (법률명)",
                "explanation": "프랜차이즈는 'nhượng quyền', 법률은 'luật kinh doanh nhượng quyền'으로 정확히 구분해야 합니다."
            },
            {
                "mistake": "정보공개서를 'hồ sơ công ty'(회사 서류)로 오역",
                "correction": "'bản công khai thông tin'(정보공개서)",
                "explanation": "정보공개서는 가맹사업법상 법정 의무 문서로, 재무제표, 가맹점 현황, 소송 이력 등을 담은 특수한 문서입니다."
            },
            {
                "mistake": "허위·과장 광고를 일반 광고법으로 설명",
                "correction": "가맹사업법 위반이며 형사 처벌 가능",
                "explanation": "가맹 모집 광고에서 예상 매출을 부풀리면 가맹사업법 위반으로 형사 고발될 수 있습니다."
            }
        ],
        "examples": [
            {
                "ko": "가맹사업법에 따라 가맹본부는 가맹 희망자에게 최소 14일 전에 정보공개서를 제공해야 합니다.",
                "vi": "Theo luật kinh doanh nhượng quyền, trụ sở nhượng quyền phải cung cấp bản công khai thông tin cho người muốn nhượng quyền ít nhất 14 ngày trước.",
                "situation": "formal"
            },
            {
                "ko": "이 가맹 계약서는 가맹사업법상 불공정 조항이 있어 수정이 필요합니다.",
                "vi": "Hợp đồng nhượng quyền này có điều khoản bất công theo luật kinh doanh nhượng quyền nên cần sửa đổi.",
                "situation": "onsite"
            },
            {
                "ko": "가맹본부가 예상 매출을 과장했다면 가맹사업법 위반으로 형사 처벌받을 수 있습니다.",
                "vi": "Nếu trụ sở nhượng quyền phóng đại doanh thu dự kiến thì có thể bị xử lý hình sự vì vi phạm luật kinh doanh nhượng quyền.",
                "situation": "formal"
            }
        ],
        "relatedTerms": ["프랜차이즈", "정보공개서", "가맹본부", "가맹점주"]
    },
    {
        "slug": "luat-phat-trien-ban-le-quy-mo-lon",
        "korean": "대규모유통업법",
        "vietnamese": "Luật phát triển bán lẻ quy mô lớn",
        "hanja": "大規模流通業法",
        "hanjaReading": "大(큰 대) + 規(법 규) + 模(본뜰 모) + 流(흐를 류) + 通(통할 통) + 業(업 업) + 法(법 법)",
        "pronunciation": "대규모유통업법",
        "meaningKo": "대규모유통업에서의 거래 공정화에 관한 법률의 약칭으로, 대형마트, SSM, 백화점 등 대규모 유통업체와 납품업체(입점업체) 간 불공정 거래를 규제하는 법입니다. 통역 시 베트남어 'luật siêu thị lớn'(대형마트법)보다는 'luật bán lẻ quy mô lớn' 또는 'luật phân phối quy mô lớn'이 더 정확하며, '공정화'(công bằng hóa) 개념을 함께 설명해야 합니다. 한국은 판촉비 전가 금지, 개점 시간 제한, 의무 휴업일 지정 등 납품업체와 전통시장 보호를 위한 다양한 규제를 두고 있습니다. 베트남도 대형마트가 많지만 한국처럼 별도 법률은 없으므로 통역 시 주의가 필요합니다.",
        "meaningVi": "Luật về công bằng hóa giao dịch trong bán lẻ quy mô lớn, quy định nhằm ngăn chặn giao dịch bất công giữa siêu thị lớn, trung tâm thương mại, cửa hàng tiện lợi quy mô lớn (SSM) và nhà cung ứng. Luật quy định cấm chuyển gánh nặng chi phí khuyến mại, giới hạn giờ mở cửa, quy định ngày nghỉ bắt buộc.",
        "context": "납품 계약, 입점 계약, 유통업체 규제",
        "culturalNote": "한국은 대형마트의 급속한 성장으로 전통시장과 소상공인이 위협받자 2012년 대규모유통업법을 강화하여 매월 2회 의무 휴업, 자정~오전 10시 영업 제한 등을 도입했습니다. 또한 납품업체에게 판촉비, 진열비 등을 일방적으로 전가하는 행위를 엄격히 금지합니다. 베트남은 대형마트(Lotte, Big C, Vinmart 등)가 많지만 영업 시간 제한이나 의무 휴업 규정은 없으며, 납품업체 보호 법률도 미비합니다. 통역 시 한국의 독특한 규제 환경을 명확히 전달해야 합니다.",
        "commonMistakes": [
            {
                "mistake": "'luật siêu thị lớn'로만 번역",
                "correction": "'luật bán lẻ quy mô lớn' 또는 'luật phân phối quy mô lớn'",
                "explanation": "단순히 '대형마트'가 아니라 '대규모 유통업' 전체를 규율하는 법입니다."
            },
            {
                "mistake": "하도급법과 혼동",
                "correction": "별도의 법이며 적용 대상 다름",
                "explanation": "하도급법은 제조·건설 위탁, 대규모유통업법은 유통업체-납품업체 관계를 규율합니다."
            },
            {
                "mistake": "의무 휴업일을 '공휴일'로 오역",
                "correction": "'ngày nghỉ bắt buộc'(의무 휴업일)",
                "explanation": "공휴일이 아니라 법으로 정한 의무 휴업일(매월 2회, 주로 일요일)입니다."
            }
        ],
        "examples": [
            {
                "ko": "대규모유통업법에 따라 대형마트는 매월 2회 의무 휴업을 해야 합니다.",
                "vi": "Theo luật bán lẻ quy mô lớn, siêu thị lớn phải nghỉ bắt buộc 2 lần mỗi tháng.",
                "situation": "formal"
            },
            {
                "ko": "이 납품 계약서의 판촉비 전가 조항은 대규모유통업법 위반 소지가 있습니다.",
                "vi": "Điều khoản chuyển gánh chi phí khuyến mại trong hợp đồng cung ứng này có dấu hiệu vi phạm luật bán lẻ quy mô lớn.",
                "situation": "onsite"
            },
            {
                "ko": "대형마트가 납품업체에게 진열비를 일방적으로 요구하는 것은 불법입니다.",
                "vi": "Việc siêu thị lớn đơn phương yêu cầu nhà cung ứng chi trả phí trưng bày là bất hợp pháp.",
                "situation": "formal"
            }
        ],
        "relatedTerms": ["대형마트", "SSM", "납품업체", "의무휴업일"]
    },
    {
        "slug": "luat-bieu-thi-quang-cao",
        "korean": "표시광고법",
        "vietnamese": "Luật biểu thị quảng cáo",
        "hanja": "表示廣告法",
        "hanjaReading": "表(겉 표) + 示(보일 시) + 廣(넓을 광) + 告(고할 고) + 法(법 법)",
        "pronunciation": "표시광고법",
        "meaningKo": "표시·광고의 공정화에 관한 법률의 약칭으로, 사업자가 상품·용역에 대해 허위·과장 표시나 광고를 하지 못하도록 규제하는 법입니다. 통역 시 베트남어 'luật quảng cáo'(광고법)만 쓰면 개념이 좁아지므로 'luật biểu thị và quảng cáo' 또는 'luật công bằng hóa biểu thị quảng cáo'로 번역해야 하며, '표시'(biểu thị, 즉 제품 라벨·포장)와 '광고'(quảng cáo)를 구분해야 합니다. 한국은 허위·과장 광고뿐 아니라 비교 광고, 추천·보증 광고(인플루언서 협찬 등)까지 엄격히 규제하며, 위반 시 공정위 제재, 시정명령, 과징금이 부과됩니다.",
        "meaningVi": "Luật về công bằng hóa biểu thị và quảng cáo, quy định nhằm ngăn chặn biểu thị hoặc quảng cáo gian dối, phóng đại về hàng hóa, dịch vụ. Luật điều chỉnh cả nhãn mác sản phẩm (biểu thị) và quảng cáo thương mại, bao gồm quảng cáo so sánh, quảng cáo có sự bảo trợ.",
        "context": "제품 라벨 검토, 광고 캠페인 승인, 인플루언서 마케팅",
        "culturalNote": "한국은 최근 인플루언서 뒷광고(협찬 미고지)를 집중 단속하고 있으며, '협찬' 또는 '#ad' 표기 의무화를 강조합니다. 또한 식품, 건강기능식품, 화장품 등의 허위·과장 광고에 대해 매우 엄격하며, 질병 치료 효과를 암시하는 표현은 즉시 제재됩니다. 베트남도 광고법(Luật Quảng cáo 2012)이 있으나, 한국처럼 '표시'와 '광고'를 통합 규율하지는 않고, 인플루언서 규제도 아직 초기 단계입니다. 통역 시 한국의 포괄적 규제 범위를 명확히 전달해야 합니다.",
        "commonMistakes": [
            {
                "mistake": "'luật quảng cáo'로만 번역",
                "correction": "'luật biểu thị và quảng cáo' (표시와 광고 모두 포함)",
                "explanation": "제품 라벨, 포장의 '표시'(biểu thị)도 규제 대상이므로 반드시 병기해야 합니다."
            },
            {
                "mistake": "인플루언서 협찬 고지 의무 누락",
                "correction": "한국은 '#ad' 또는 '협찬' 표기 필수",
                "explanation": "뒷광고는 표시광고법 위반이며, 공정위가 적극 단속하고 있습니다."
            },
            {
                "mistake": "비교 광고를 무조건 금지로 설명",
                "correction": "허위·과장 없으면 비교 광고 가능",
                "explanation": "한국은 객관적 사실에 기반한 비교 광고는 허용하지만, 경쟁사를 비방하거나 사실을 왜곡하면 위법입니다."
            }
        ],
        "examples": [
            {
                "ko": "이 제품 라벨에 '100% 천연'이라고 표시했는데 합성 성분이 있다면 표시광고법 위반입니다.",
                "vi": "Nếu nhãn sản phẩm này ghi '100% tự nhiên' nhưng có thành phần tổng hợp thì vi phạm luật biểu thị quảng cáo.",
                "situation": "onsite"
            },
            {
                "ko": "인플루언서가 협찬받고 '#ad' 표기를 안 하면 표시광고법 위반으로 제재받을 수 있습니다.",
                "vi": "Nếu influencer nhận tài trợ mà không ghi '#ad' thì có thể bị xử phạt vì vi phạm luật biểu thị quảng cáo.",
                "situation": "formal"
            },
            {
                "ko": "이 광고는 질병 치료 효과를 암시하고 있어 표시광고법 위반 소지가 큽니다.",
                "vi": "Quảng cáo này ám chỉ hiệu quả chữa bệnh nên có khả năng cao vi phạm luật biểu thị quảng cáo.",
                "situation": "formal"
            }
        ],
        "relatedTerms": ["허위광고", "과장광고", "비교광고", "뒷광고"]
    },
    {
        "slug": "quyet-dinh-dong-y",
        "korean": "동의의결",
        "vietnamese": "Quyết định đồng ý",
        "hanja": "同意議決",
        "hanjaReading": "同(한가지 동) + 意(뜻 의) + 議(의논할 의) + 決(결정할 결)",
        "pronunciation": "동의의결",
        "meaningKo": "공정거래위원회가 법 위반 혐의가 있는 사업자와 합의하여 시정 방안을 의결로 확정하는 제도로, 사업자가 스스로 시정 계획을 제출하고 공정위가 이를 승인하면 정식 심의 절차를 생략할 수 있습니다. 통역 시 베트남어 'quyết định đồng ý'(동의 결정) 또는 'thỏa thuận khắc phục'(시정 합의)로 번역하며, 이는 미국의 'consent decree'와 유사한 제도임을 설명하면 이해가 빠릅니다. 동의의결을 받으면 과징금은 30% 감경되지만, 법 위반 사실 자체는 인정하는 것이므로 손해배상 소송에서 불리할 수 있어 신중한 판단이 필요합니다.",
        "meaningVi": "Chế độ Ủy ban Cạnh tranh Công bằng thỏa thuận với doanh nghiệp bị nghi vi phạm để quyết định phương án khắc phục bằng nghị quyết. Nếu doanh nghiệp tự đề xuất kế hoạch sửa chữa và Ủy ban phê duyệt thì có thể bỏ qua thủ tục thẩm tra chính thức. Tương tự 'consent decree' của Mỹ. Nếu được đồng ý thì phạt giảm 30% nhưng phải thừa nhận vi phạm.",
        "context": "공정위 조사 대응, 법 위반 시정 협상",
        "culturalNote": "한국 공정거래위원회는 2004년부터 동의의결 제도를 도입하여 신속한 법 집행과 사업자의 자발적 시정을 유도하고 있습니다. 사업자 입장에서는 과징금을 30% 감경받고 절차를 조기 종결할 수 있지만, 법 위반을 인정하는 것이므로 후속 손해배상 소송에서 불리한 증거로 사용될 수 있습니다. 베트남에는 유사한 제도가 없으며, 행정 처벌은 일반적으로 위반 확정 후 부과되고 합의로 감경하는 절차가 드뭅니다. 통역 시 이 제도의 장단점을 명확히 전달해야 클라이언트의 전략적 판단을 도울 수 있습니다.",
        "commonMistakes": [
            {
                "mistake": "'hòa giải'(조정, mediation)로 오역",
                "correction": "'quyết định đồng ý' 또는 'thỏa thuận khắc phục'",
                "explanation": "조정(hòa giải)은 분쟁 당사자 간 합의이지만, 동의의결은 공정위와 사업자 간 시정 합의입니다."
            },
            {
                "mistake": "법 위반을 인정하지 않는다고 설명",
                "correction": "동의의결은 위반 사실을 인정하는 것",
                "explanation": "동의의결을 하면 법 위반을 인정하는 것이므로, 손해배상 소송에서 불리할 수 있습니다."
            },
            {
                "mistake": "과징금 100% 면제로 잘못 안내",
                "correction": "30% 감경 (완전 면제 아님)",
                "explanation": "동의의결 시 과징금은 30% 감경되지만, 여전히 70%는 부과됩니다."
            }
        ],
        "examples": [
            {
                "ko": "공정위와 동의의결을 하면 과징금이 30% 감경되지만, 법 위반은 인정하게 됩니다.",
                "vi": "Nếu ký quyết định đồng ý với Ủy ban thì phạt giảm 30%, nhưng phải thừa nhận vi phạm pháp luật.",
                "situation": "formal"
            },
            {
                "ko": "동의의결 절차를 진행하면 정식 심의를 받지 않고 조기에 사건을 종결할 수 있습니다.",
                "vi": "Nếu tiến hành thủ tục quyết định đồng ý thì có thể kết thúc vụ việc sớm mà không cần thẩm tra chính thức.",
                "situation": "onsite"
            },
            {
                "ko": "동의의결은 손해배상 소송에서 불리한 증거가 될 수 있으니 신중히 검토해야 합니다.",
                "vi": "Quyết định đồng ý có thể trở thành chứng cứ bất lợi trong vụ kiện bồi thường thiệt hại nên cần xem xét cẩn thận.",
                "situation": "formal"
            }
        ],
        "relatedTerms": ["시정명령", "과징금", "합의", "손해배상"]
    },
    {
        "slug": "tien-phat-hanh-chinh",
        "korean": "과징금",
        "vietnamese": "Tiền phạt hành chính",
        "hanja": "課徵金",
        "hanjaReading": "課(과할 과) + 徵(징수할 징) + 金(쇠 금)",
        "pronunciation": "과징금",
        "meaningKo": "법 위반으로 얻은 경제적 이익을 환수하고 제재하기 위해 행정기관이 부과하는 금전적 제재로, 벌금(형사 처벌)과는 다른 행정 제재입니다. 통역 시 베트남어 'tiền phạt hành chính'(행정 벌금)으로 번역하지만, 한국의 과징금은 단순 벌금이 아니라 '부당 이득 환수 + 제재'의 성격을 함께 가지므로 'tiền thu hồi lợi ích bất hợp pháp'(부당 이익 환수금)이라는 설명을 병행해야 합니다. 한국 공정거래법상 과징금은 매출액의 최대 10%까지 부과될 수 있으며, 수천억 원에 달하는 경우도 있어 기업에 큰 부담이 됩니다. 베트남은 행정 벌금 상한이 상대적으로 낮아(대부분 수억 VND 수준), 한국의 높은 과징금 수준을 미리 경고해야 합니다.",
        "meaningVi": "Chế tài tài chính do cơ quan hành chính áp dụng để thu hồi lợi ích kinh tế thu được từ vi phạm pháp luật và trừng phạt. Khác với tiền phạt hình sự (phạt tù), là chế tài hành chính. Theo luật cạnh tranh Hàn Quốc, có thể lên đến 10% doanh thu, đôi khi lên tới hàng nghìn tỷ won.",
        "context": "공정위 제재, 법 위반 처벌, 기업 컴플라이언스",
        "culturalNote": "한국은 공정거래법, 하도급법, 가맹사업법, 대규모유통업법 등에서 과징금을 매출액 기준으로 부과하며, 대기업의 경우 수천억 원에 달하는 경우가 많습니다. 특히 담합, 시장지배적 지위 남용 등 중대 위반에는 매출액의 10%까지 부과 가능합니다. 베트남은 행정 벌금이 대부분 고정 금액(예: 5억 VND)이며, 한국처럼 매출액 비례 제도는 없어 금액 규모가 훨씬 작습니다. 통역 시 한국의 높은 과징금 수준을 강조하여 베트남 기업이 리스크를 충분히 인식하도록 해야 합니다.",
        "commonMistakes": [
            {
                "mistake": "'tiền phạt'(벌금)로만 번역",
                "correction": "'tiền phạt hành chính' 또는 'tiền thu hồi bất hợp pháp'",
                "explanation": "과징금은 부당 이득 환수 성격이 있으므로 단순 '벌금'보다 넓은 개념입니다."
            },
            {
                "mistake": "형사 벌금(phạt hình sự)과 혼동",
                "correction": "과징금은 행정 제재, 벌금은 형사 처벌",
                "explanation": "과징금은 공정위 등 행정기관이 부과하고, 벌금은 법원이 선고하는 형사 처벌입니다."
            },
            {
                "mistake": "베트남과 동일한 금액 수준으로 설명",
                "correction": "한국은 매출액 비례로 수천억 원 가능",
                "explanation": "베트남은 고정 금액(수억 VND)이지만, 한국은 매출액의 최대 10%로 금액이 매우 큽니다."
            }
        ],
        "examples": [
            {
                "ko": "공정위는 이 담합 사건에 대해 총 5천억 원의 과징금을 부과했습니다.",
                "vi": "Ủy ban Cạnh tranh Công bằng đã áp dụng tổng cộng 500 tỷ won tiền phạt hành chính cho vụ thỏa thuận này.",
                "situation": "formal"
            },
            {
                "ko": "과징금은 매출액의 최대 10%까지 부과될 수 있으므로 금액이 매우 클 수 있습니다.",
                "vi": "Tiền phạt hành chính có thể lên đến 10% doanh thu nên số tiền có thể rất lớn.",
                "situation": "onsite"
            },
            {
                "ko": "동의의결을 하면 과징금을 30% 감경받을 수 있습니다.",
                "vi": "Nếu ký quyết định đồng ý thì có thể được giảm 30% tiền phạt hành chính.",
                "situation": "formal"
            }
        ],
        "relatedTerms": ["시정명령", "벌금", "행정제재", "동의의결"]
    }
]

def main():
    """메인 실행 함수"""
    print("=" * 60)
    print("한-베 통역 용어 플랫폼 - 법률 도메인 용어 추가")
    print("테마: 공정거래법 심화")
    print("=" * 60)

    # legal.json 파일 읽기
    try:
        with open(LEGAL_JSON_PATH, 'r', encoding='utf-8') as f:
            data = json.load(f)
        print(f"✅ 기존 법률 용어 데이터 로드 완료: {len(data)} 개")
    except FileNotFoundError:
        print(f"❌ 오류: {LEGAL_JSON_PATH} 파일을 찾을 수 없습니다.")
        return
    except json.JSONDecodeError:
        print(f"❌ 오류: {LEGAL_JSON_PATH} 파일이 올바른 JSON 형식이 아닙니다.")
        return

    # 중복 확인
    existing_slugs = {term['slug'] for term in data}
    new_terms_to_add = []
    duplicates = []

    for term in NEW_TERMS:
        if term['slug'] in existing_slugs:
            duplicates.append(term['slug'])
        else:
            new_terms_to_add.append(term)

    if duplicates:
        print(f"⚠️  중복된 slug 발견 (추가하지 않음): {', '.join(duplicates)}")

    if not new_terms_to_add:
        print("ℹ️  추가할 새 용어가 없습니다.")
        return

    # 새 용어 추가
    data.extend(new_terms_to_add)
    print(f"✅ {len(new_terms_to_add)}개 용어 추가 준비 완료")

    # 파일 저장
    try:
        with open(LEGAL_JSON_PATH, 'w', encoding='utf-8') as f:
            json.dump(data, f, ensure_ascii=False, indent=2)
        print(f"✅ {LEGAL_JSON_PATH} 파일 저장 완료")
        print(f"📊 총 법률 용어 수: {len(data)} 개")
    except Exception as e:
        print(f"❌ 파일 저장 중 오류 발생: {e}")
        return

    # 추가된 용어 목록 출력
    print("\n" + "=" * 60)
    print("추가된 용어 목록:")
    print("=" * 60)
    for i, term in enumerate(new_terms_to_add, 1):
        print(f"{i}. {term['korean']} ({term['slug']})")
    print("=" * 60)
    print("✅ 작업 완료!")

if __name__ == "__main__":
    main()
