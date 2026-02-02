#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
법률 도메인 용어 추가 스크립트 v8-j
테마: 법원조직/사법제도
- 대법원, 고등법원, 지방법원, 헌법재판소, 법관, 검사, 변호사, 법률구조, 사법연수원, 법조윤리
"""

import json
import os

# 프로젝트 루트 기준 상대 경로
SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
PROJECT_ROOT = os.path.dirname(os.path.dirname(SCRIPT_DIR))
JSON_PATH = os.path.join(PROJECT_ROOT, "src", "data", "terms", "legal.json")

# 추가할 10개 용어 (Tier S 기준)
NEW_TERMS = [
    {
        "slug": "toa-an-toi-cao",
        "korean": "대법원",
        "vietnamese": "Tòa án Tối cao",
        "hanja": "大法院",
        "hanjaReading": "大(큰 대) + 法(법 법) + 院(집 원)",
        "pronunciation": "떠어 언 떠이 까오",
        "meaningKo": "최고법원. 한국의 최종 상급법원으로 법률심을 담당하며 하급법원의 판결에 대한 상고심을 재판한다. 통역 시 주의할 점은 베트남의 'Tòa án nhân dân tối cao'(인민최고법원)와 구조가 다르다는 점이다. 한국은 3심제(지방법원-고등법원-대법원)인 반면 베트남은 2심제(성급법원-최고법원)이며, 한국 대법원은 원칙적으로 법률심만 담당하여 사실관계는 재심리하지 않는다. 또한 한국에서는 대법원장이 사법부 수장으로서 독립적 지위를 갖지만, 베트namにおいては 국회에 대해 책임을 진다. 통역 시 양국 사법제도의 근본적 차이를 설명할 필요가 있다.",
        "meaningVi": "Tòa án cao nhất của Hàn Quốc, thực hiện chức năng xét xử về mặt pháp luật và xét xử phúc thẩm đối với các bản án của tòa cấp dưới. Khác với Việt Nam áp dụng chế độ hai cấp xét xử, Hàn Quốc áp dụng chế độ ba cấp (tòa sơ thẩm - tòa phúc thẩm - tòa tối cao). Tòa án Tối cao Hàn Quốc chủ yếu xét xử về mặt pháp luật, không xem xét lại các sự kiện.",
        "context": "법원 조직, 사법제도, 상고심 재판",
        "culturalNote": "한국의 대법원은 사법부 독립의 상징으로 행정부와 입법부로부터 완전히 독립된 지위를 갖는다. 대법원장은 국회 동의를 거쳐 대통령이 임명하며 임기는 6년이다. 베트남의 인민최고법원은 국회에 대해 책임을 지며 국회가 법관을 선출/해임한다는 점에서 큰 차이가 있다. 또한 한국은 판례법 전통이 강해 대법원 판례가 사실상 구속력을 갖지만, 베트남은 성문법 중심이다.",
        "commonMistakes": [
            {
                "mistake": "Tòa án Tối cao를 '최고인민법원'으로 번역",
                "correction": "'대법원'으로 번역",
                "explanation": "베트남식 명칭을 그대로 직역하면 오해 발생. 한국은 '인민'이라는 용어를 사용하지 않음"
            },
            {
                "mistake": "대법원이 모든 사건을 재심리한다고 설명",
                "correction": "원칙적으로 법률심만 담당하며 사실관계는 재심리하지 않음을 명확히",
                "explanation": "한국 대법원은 법률 적용의 적정성만 판단하는 법률심 법원"
            },
            {
                "mistake": "Tòa phúc thẩm(항소법원)과 Tòa tối cao(대법원)를 혼동",
                "correction": "한국은 3심제이므로 고등법원(phúc thẩm)과 대법원(tối cao)을 명확히 구분",
                "explanation": "베트남은 2심제이므로 한국의 3단계 법원 체계 설명 필요"
            }
        ],
        "examples": [
            {
                "ko": "이 사건은 대법원에 상고되어 최종 판결을 기다리고 있습니다.",
                "vi": "Vụ án này đã được kháng cáo lên Tòa án Tối cao và đang chờ phán quyết cuối cùng.",
                "situation": "formal"
            },
            {
                "ko": "대법원 판례에 따르면 이러한 경우 손해배상 책임이 인정됩니다.",
                "vi": "Theo tiền lệ của Tòa án Tối cao, trong trường hợp này trách nhiệm bồi thường thiệt hại được công nhận.",
                "situation": "formal"
            },
            {
                "ko": "대법원장은 사법부의 수장으로서 법관 인사권을 행사합니다.",
                "vi": "Chánh án Tòa án Tối cao với tư cách là người đứng đầu nền tư pháp, thực hiện quyền nhân sự đối với các thẩm phán.",
                "situation": "formal"
            }
        ],
        "relatedTerms": ["고등법원", "지방법원", "상고", "법률심", "판례"]
    },
    {
        "slug": "toa-phuc-tham",
        "korean": "고등법원",
        "vietnamese": "Tòa phúc thẩm",
        "hanja": "高等法院",
        "hanjaReading": "高(높을 고) + 等(무리 등) + 法(법 법) + 院(집 원)",
        "pronunciation": "떠어 푹 tham",
        "meaningKo": "항소심 법원. 지방법원의 제1심 판결에 불복하여 항소한 사건을 재판하는 상급법원이다. 전국에 서울, 부산, 대구, 광주, 대전, 인천 6개 고등법원이 있다. 통역 시 주의할 점은 베트남에는 고등법원 개념이 없다는 것이다. 베트남은 2심제로 성급 인민법원(Tòa án nhân dân cấp tỉnh)의 1심 판결에 불복하면 바로 최고인민법원으로 항소한다. 따라서 한국의 3심제(지방법원 1심 → 고등법원 2심 항소심 → 대법원 3심 상고심) 구조를 명확히 설명해야 한다. 또한 고등법원은 사실심과 법률심을 모두 담당하여 새로운 증거 제출이 가능하다는 점도 중요하다.",
        "meaningVi": "Tòa án cấp phúc thẩm xét xử các vụ án kháng cáo không đồng ý với bản án sơ thẩm của tòa sơ thẩm. Có 6 tòa phúc thẩm trên toàn quốc. Khác với Việt Nam áp dụng chế độ hai cấp xét xử, Hàn Quốc có tòa phúc thẩm là cấp xét xử trung gian giữa tòa sơ thẩm và tòa tối cao.",
        "context": "항소심 재판, 법원 조직, 3심제",
        "culturalNote": "한국의 고등법원은 사실심이므로 새로운 증거를 제출하고 증인을 신문할 수 있다. 이는 베트남의 항소심이 주로 서류 심사 중심인 것과 대조적이다. 또한 한국은 지역별로 고등법원이 배치되어 있어 항소심 접근성이 높은 편이다. 고등법원 판결에 불복하면 대법원에 상고할 수 있으나, 대법원은 법률심이므로 사실관계 다툼은 고등법원이 사실상 최종심이 된다.",
        "commonMistakes": [
            {
                "mistake": "Tòa phúc thẩm을 '최고법원'으로 오역",
                "correction": "'고등법원'으로 정확히 번역",
                "explanation": "베트남에서는 phúc thẩm이 최종심이지만 한국은 중간 심급"
            },
            {
                "mistake": "고등법원을 Tòa án cấp cao(고급법원)로 번역",
                "correction": "Tòa phúc thẩm 또는 Tòa kháng cáo로 번역",
                "explanation": "기능을 나타내는 용어가 더 정확"
            },
            {
                "mistake": "고등법원에서 새 증거 제출이 불가능하다고 설명",
                "correction": "사실심이므로 새로운 증거 제출 가능함을 명확히",
                "explanation": "대법원(법률심)과 혼동하여 발생하는 오류"
            }
        ],
        "examples": [
            {
                "ko": "1심 판결에 불복하여 서울고등법원에 항소했습니다.",
                "vi": "Không đồng ý với bản án sơ thẩm nên đã kháng cáo lên Tòa phúc thẩm Seoul.",
                "situation": "formal"
            },
            {
                "ko": "고등법원에서 새로운 증거를 제출하여 무죄 판결을 받았습니다.",
                "vi": "Đã nộp bằng chứng mới tại Tòa phúc thẩm và nhận được phán quyết trắng án.",
                "situation": "formal"
            },
            {
                "ko": "항소심은 고등법원에서 약 6개월 후 선고될 예정입니다.",
                "vi": "Phiên phúc thẩm dự kiến sẽ tuyên án sau khoảng 6 tháng tại Tòa phúc thẩm.",
                "situation": "formal"
            }
        ],
        "relatedTerms": ["항소", "지방법원", "대법원", "사실심", "3심제"]
    },
    {
        "slug": "toa-so-tham",
        "korean": "지방법원",
        "vietnamese": "Tòa sơ thẩm",
        "hanja": "地方法院",
        "hanjaReading": "地(땅 지) + 方(모 방) + 法(법 법) + 院(집 원)",
        "pronunciation": "떠어 sơ tham",
        "meaningKo": "제1심 법원. 민사, 형사, 행정, 가사 등 대부분의 사건을 최초로 재판하는 법원이다. 전국에 18개 지방법원 본원과 40여 개 지원이 있다. 통역 시 주의할 점은 '지방'이라는 용어가 '지역'을 의미하지 '지방자치단체 소속'을 뜻하지 않는다는 것이다. 한국의 지방법원은 국가 사법기관으로 독립되어 있다. 베트남의 경우 '기층인민법원(Tòa án nhân dân cấp huyện)'과 '성급인민법원(Tòa án nhân dân cấp tỉnh)'으로 나뉘는데, 한국의 지방법원은 대략 성급법원에 해당하지만 1심만 담당한다는 점이 다르다. 또한 지방법원 내에도 단독판사와 합의부가 있어 사건의 경중에 따라 구성이 달라진다.",
        "meaningVi": "Tòa án sơ thẩm xét xử lần đầu hầu hết các vụ án dân sự, hình sự, hành chính, gia đình. Có 18 tòa sơ thẩm chính và hơn 40 chi nhánh trên toàn quốc. 'Địa phương' (지방) ở đây không có nghĩa là thuộc chính quyền địa phương mà là tòa án quốc gia đặt tại các địa phương.",
        "context": "제1심 재판, 민형사 소송, 법원 조직",
        "culturalNote": "한국의 지방법원은 사법권 독립 원칙에 따라 국가기관이지 지방자치단체 소속이 아니다. 베트남 통역사들이 흔히 '지방'을 'địa phương'으로 번역하면서 지방정부 소속으로 오해하는 경우가 많다. 또한 한국은 사건 규모에 따라 단독판사 또는 3인 합의부가 재판하는데, 베트남은 항상 합의제(hội thẩm)로 재판한다는 차이가 있다. 지방법원 판결에 불복하면 고등법원에 항소할 수 있다.",
        "commonMistakes": [
            {
                "mistake": "지방법원을 '지방정부 소속 법원'으로 설명",
                "correction": "국가 사법기관으로 독립된 법원임을 명확히",
                "explanation": "'지방'은 지역을 의미할 뿐 지방자치단체와 무관"
            },
            {
                "mistake": "Tòa án cấp huyện(기층법원)으로 번역",
                "correction": "Tòa án cấp tỉnh 또는 Tòa sơ thẩm으로 번역",
                "explanation": "한국 지방법원은 베트남 기층법원보다 상위 개념"
            },
            {
                "mistake": "모든 재판이 합의부로 진행된다고 설명",
                "correction": "사건 경중에 따라 단독판사 또는 합의부 구성",
                "explanation": "베트남과 달리 한국은 사건별로 재판부 구성이 다름"
            }
        ],
        "examples": [
            {
                "ko": "이 사건은 서울중앙지방법원에 민사소송으로 제기되었습니다.",
                "vi": "Vụ án này đã được đưa ra Tòa án Seoul trung ương dưới dạng vụ kiện dân sự.",
                "situation": "formal"
            },
            {
                "ko": "지방법원에서 1심 판결이 선고된 후 항소 여부를 결정하겠습니다.",
                "vi": "Sau khi tòa sơ thẩm tuyên án, chúng tôi sẽ quyết định có kháng cáo hay không.",
                "situation": "formal"
            },
            {
                "ko": "이 사건은 합의부가 아닌 단독판사가 재판합니다.",
                "vi": "Vụ án này do thẩm phán đơn nhất xét xử, không phải hội đồng xét xử.",
                "situation": "formal"
            }
        ],
        "relatedTerms": ["제1심", "합의부", "단독판사", "고등법원", "관할"]
    },
    {
        "slug": "toa-hien-phap",
        "korean": "헌법재판소",
        "vietnamese": "Tòa Hiến pháp",
        "hanja": "憲法裁判所",
        "hanjaReading": "憲(법 헌) + 法(법 법) + 裁(재결할 재) + 判(판단할 판) + 所(바 소)",
        "pronunciation": "떠어 히엔 fáp",
        "meaningKo": "헌법에 관한 최종 해석기관. 법률의 위헌 여부 심판, 탄핵 심판, 정당 해산 심판, 권한쟁의 심판, 헌법소원 심판을 담당하는 독립된 헌법기관이다. 9명의 재판관으로 구성되며 대통령, 국회, 대법원장이 각 3명씩 지명한다. 통역 시 주의할 점은 헌법재판소가 일반 법원 체계와 별개의 독립기관이라는 점이다. 베트남에는 헌법재판소가 없고 국회 상임위원회가 위헌 여부를 판단한다. 따라서 사법심사권(judicial review) 개념과 헌법재판소의 정치적 중립성, 위헌법률심사의 효력 등을 상세히 설명해야 한다. 한국에서는 헌법재판소 결정으로 법률이 무효화될 수 있다는 점이 중요하다.",
        "meaningVi": "Cơ quan giải thích cuối cùng về Hiến pháp. Thực hiện xét xử vi hiến luật, xét xử luận tội, xét xử giải thể đảng, xét xử tranh chấp thẩm quyền, xét xử khiếu nại hiến pháp. Là cơ quan hiến pháp độc lập gồm 9 thẩm phán. Khác với Việt Nam, nơi Ủy ban Thường vụ Quốc hội xem xét tính vi hiến, Hàn Quốc có cơ quan độc lập chuyên trách xét xử các vấn đề hiến pháp.",
        "context": "위헌법률심사, 헌법소원, 탄핵심판, 헌법기관",
        "culturalNote": "한국의 헌법재판소는 1988년 설립되어 민주주의 발전에 중요한 역할을 했다. 일반 국민도 헌법소원을 통해 기본권 침해를 다툴 수 있다는 점이 특징이다. 베트남은 국회가 헌법 해석과 위헌 판단을 하므로 입법부와 사법부가 분리되지 않는다. 헌법재판소는 대통령 탄핵, 정당 해산 등 정치적으로 민감한 사안도 다루며, 과거 대통령 탄핵 인용(2004년 노무현, 2017년 박근혜) 사례가 있다.",
        "commonMistakes": [
            {
                "mistake": "헌법재판소를 일반 법원의 일부로 설명",
                "correction": "법원과 별개의 독립된 헌법기관임을 명확히",
                "explanation": "대법원과는 다른 조직이며 상하 관계가 아님"
            },
            {
                "mistake": "Tòa án Hiến pháp을 베트남 국회 기능과 동일시",
                "correction": "사법기관으로서의 독립성과 구속력 있는 판결권 강조",
                "explanation": "베트남 국회 결정과 달리 헌재 결정은 사법적 판단"
            },
            {
                "mistake": "일반 국민은 헌법재판소를 이용할 수 없다고 설명",
                "correction": "헌법소원을 통해 국민이 직접 기본권 침해 구제 가능",
                "explanation": "헌법소원 제도는 한국 헌법재판의 중요한 특징"
            }
        ],
        "examples": [
            {
                "ko": "이 법률은 헌법재판소에서 위헌 결정을 받아 효력을 상실했습니다.",
                "vi": "Luật này đã bị Tòa Hiến pháp tuyên bố vi hiến nên mất hiệu lực.",
                "situation": "formal"
            },
            {
                "ko": "국민은 헌법소원을 통해 기본권 침해에 대해 헌법재판소에 구제를 청구할 수 있습니다.",
                "vi": "Công dân có thể yêu cầu Tòa Hiến pháp cứu tế về việc xâm phạm quyền cơ bản thông qua khiếu nại hiến pháp.",
                "situation": "formal"
            },
            {
                "ko": "대통령 탄핵소추안은 헌법재판소의 최종 심판을 받게 됩니다.",
                "vi": "Đề nghị luận tội tổng thống sẽ nhận được phán quyết cuối cùng của Tòa Hiến pháp.",
                "situation": "formal"
            }
        ],
        "relatedTerms": ["위헌법률심사", "헌법소원", "탄핵", "기본권", "사법심사"]
    },
    {
        "slug": "tham-phan",
        "korean": "법관",
        "vietnamese": "Thẩm phán",
        "hanja": "法官",
        "hanjaReading": "法(법 법) + 官(벼슬 관)",
        "pronunciation": "tham fán",
        "meaningKo": "재판을 담당하는 법률 전문가. 판사라고도 불리며 사법권 독립의 원칙에 따라 헌법과 법률에 의해서만 재판하고 어떠한 외부 압력이나 간섭을 받지 않는다. 통역 시 주의할 점은 한국의 법관 임명 및 신분 보장 제도가 베트남과 매우 다르다는 것이다. 한국은 대법원장이 법관을 임명하고 임기 없이 정년까지 신분이 보장되지만, 베트남은 국회가 선출하고 5년 임기제이다. 또한 한국은 법관이 되려면 사법시험(현재는 로스쿨) 합격 후 사법연수원을 거쳐야 하는 엄격한 자격 요건이 있다. 법관의 독립성과 중립성은 사법 신뢰의 핵심이므로 통역 시 이 개념을 명확히 전달해야 한다.",
        "meaningVi": "Chuyên gia pháp lý phụ trách xét xử. Còn gọi là thẩm phán (판사). Theo nguyên tắc độc lập tư pháp, chỉ xét xử theo Hiến pháp và pháp luật, không chịu bất kỳ áp lực hay can thiệp từ bên ngoài. Khác với Việt Nam nơi Quốc hội bầu thẩm phán với nhiệm kỳ 5 năm, ở Hàn Quốc Chánh án Tòa án Tối cao bổ nhiệm và thẩm phán có quyền giữ chức đến tuổi nghỉ hưu.",
        "context": "재판 진행, 사법권 독립, 법조인",
        "culturalNote": "한국의 법관은 엄격한 중립 의무가 있어 정치 활동, 영리 활동이 금지되며 품위 유지 의무도 있다. 법관 탄핵은 국회가 소추하고 헌법재판소가 심판한다. 베트남의 경우 법관이 국회에 대해 책임을 지며 정치적으로 더 밀접하다. 한국은 법관에 대한 사회적 존경과 신뢰가 높으며, 법복(검은 법복)을 입고 법정에서 높은 단상에 앉아 재판을 진행하는 것이 전통이다.",
        "commonMistakes": [
            {
                "mistake": "법관과 판사를 다른 직위로 설명",
                "correction": "법관과 판사는 같은 의미이며 공식 명칭은 법관",
                "explanation": "일상에서는 '판사'를 더 많이 쓰지만 법률 용어는 '법관'"
            },
            {
                "mistake": "베트남식 임기제를 한국에도 적용",
                "correction": "한국 법관은 임기가 없고 정년(65세)까지 신분 보장",
                "explanation": "양국의 법관 임명 제도가 근본적으로 다름"
            },
            {
                "mistake": "법관을 '법원 공무원' 정도로 격하",
                "correction": "사법권을 행사하는 헌법기관 구성원으로 높은 지위",
                "explanation": "일반 공무원과 달리 독립성과 신분보장이 강함"
            }
        ],
        "examples": [
            {
                "ko": "법관은 헌법과 법률에 의하여 그 양심에 따라 독립하여 심판합니다.",
                "vi": "Thẩm phán xét xử độc lập theo Hiến pháp và pháp luật, tuân theo lương tâm của mình.",
                "situation": "formal"
            },
            {
                "ko": "이번 재판의 법관은 민사소송 전문가입니다.",
                "vi": "Thẩm phán của phiên tòa này là chuyên gia về tố tụng dân sự.",
                "situation": "formal"
            },
            {
                "ko": "법관 3명으로 구성된 합의부가 이 사건을 재판합니다.",
                "vi": "Hội đồng xét xử gồm 3 thẩm phán sẽ xét xử vụ án này.",
                "situation": "formal"
            }
        ],
        "relatedTerms": ["판사", "사법권", "재판", "사법연수원", "법조인"]
    },
    {
        "slug": "kiem-sat-vien",
        "korean": "검사",
        "vietnamese": "Kiểm sát viên",
        "hanja": "檢事",
        "hanjaReading": "檢(검사할 검) + 事(일 사)",
        "pronunciation": "끼엠 sát 비엔",
        "meaningKo": "검찰청에 소속되어 범죄 수사 지휘, 공소 제기 및 유지, 형집행 감독 등을 담당하는 법률 전문가. 한국의 검사는 수사권과 기소권을 모두 가지며 사법경찰을 지휘할 수 있는 강력한 권한을 갖는다. 통역 시 주의할 점은 베트남의 '검찰원(Viện Kiểm sát)'과 한국의 '검찰청'의 조직 구조와 권한이 다르다는 것이다. 베트남 검찰은 재판 감독권까지 가지지만 한국 검사는 형사소송의 당사자로서 공소를 제기하고 유지하는 역할만 한다. 또한 최근 검경 수사권 조정으로 경찰의 독자 수사권이 확대되었으나 여전히 기소독점권은 검사에게 있다. 검사는 공익의 대표자로서 무죄 입증 증거도 제출해야 하는 의무가 있다.",
        "meaningVi": "Chuyên gia pháp lý thuộc Viện Kiểm sát, phụ trách chỉ đạo điều tra tội phạm, truy tố và duy trì công tố, giám sát thi hành án hình sự. Kiểm sát viên Hàn Quốc có cả quyền điều tra và truy tố, có thể chỉ đạo cảnh sát tư pháp. Khác với Việt Nam nơi Viện Kiểm sát có quyền giám sát xét xử, ở Hàn Quốc kiểm sát viên chỉ là đương sự trong tố tụng hình sự.",
        "context": "형사소송, 공소 제기, 범죄 수사",
        "culturalNote": "한국의 검사는 매우 강력한 권한을 가져 '권력기관'으로 인식된다. 검찰총장은 법무부 장관의 지휘를 받지만 개별 사건 수사에서는 독립성이 보장된다. 검사 임용은 사법연수원을 거친 법조인이나 변호사 경력자 중에서 이루어진다. 베트남과 달리 한국은 검사와 판사가 같은 사법시험 출신으로 서로 전환이 가능하며(법관과 검사 상호 전직), 이로 인한 유착 논란도 있다. 최근 검찰 개혁으로 수사권과 기소권 분리 논의가 활발하다.",
        "commonMistakes": [
            {
                "mistake": "검사를 재판 감독 기관으로 설명",
                "correction": "형사소송의 한 당사자로서 공소 제기·유지 역할만 수행",
                "explanation": "베트남 검찰과 달리 재판 감독권은 없음"
            },
            {
                "mistake": "경찰과 검찰의 수사권을 혼동",
                "correction": "현재는 경찰이 독자 수사권을 가지지만 기소는 검사만 가능",
                "explanation": "최근 검경 수사권 조정으로 권한 구조 변화"
            },
            {
                "mistake": "Công tố viên(공소인)으로 번역",
                "correction": "Kiểm sát viên이 정확한 대응어",
                "explanation": "검사는 기소 외에도 수사지휘, 형집행 감독 등 다양한 역할"
            }
        ],
        "examples": [
            {
                "ko": "검사는 이 사건에 대해 징역 5년을 구형했습니다.",
                "vi": "Kiểm sát viên đã yêu cầu mức án 5 năm tù cho vụ án này.",
                "situation": "formal"
            },
            {
                "ko": "검사의 불기소 처분에 불복하여 항고했습니다.",
                "vi": "Đã kháng cáo không đồng ý với quyết định không truy tố của kiểm sát viên.",
                "situation": "formal"
            },
            {
                "ko": "검사는 공익의 대표자로서 무죄 증거도 제출할 의무가 있습니다.",
                "vi": "Kiểm sát viên với tư cách đại diện lợi ích công có nghĩa vụ nộp cả bằng chứng vô tội.",
                "situation": "formal"
            }
        ],
        "relatedTerms": ["검찰청", "공소", "기소", "불기소", "구형"]
    },
    {
        "slug": "luat-su",
        "korean": "변호사",
        "vietnamese": "Luật sư",
        "hanja": "辯護士",
        "hanjaReading": "辯(말씀 변) + 護(보호할 호) + 士(선비 사)",
        "pronunciation": "루엇 sư",
        "meaningKo": "의뢰인의 법률 사무를 대리하고 법정에서 변론하는 법률 전문가. 한국에서는 변호사 자격을 취득하려면 사법시험 합격(2017년 폐지) 또는 로스쿨 졸업 후 변호사시험 합격이 필요하다. 통역 시 주의할 점은 한국의 변호사 제도가 단일 자격제라는 것이다. 즉, 변호사 자격만 있으면 민사, 형사, 행정, 특허 등 모든 분야의 사건을 수임할 수 있다(실제로는 전문 분야별로 특화). 베트남은 변호사 자격이 상대적으로 쉽게 취득되지만 한국은 매우 어렵고 경쟁이 치열하다. 변호사는 의뢰인의 비밀을 지킬 의무(변호사-의뢰인 특권)가 있으며, 이를 위반하면 형사처벌을 받는다. 또한 변호사는 법무법인, 개인 사무실 등 다양한 형태로 개업할 수 있다.",
        "meaningVi": "Chuyên gia pháp lý đại diện công việc pháp lý cho khách hàng và biện hộ tại tòa án. Ở Hàn Quốc, để có được tư cách luật sư cần thi đậu kỳ thi tư pháp (đã bãi bỏ năm 2017) hoặc tốt nghiệp trường luật và đậu kỳ thi luật sư. Là chế độ tư cách duy nhất, một khi có tư cách luật sư có thể nhận tất cả các loại vụ việc.",
        "context": "법률 자문, 소송 대리, 변론",
        "culturalNote": "한국의 변호사는 사회적으로 높은 지위와 소득을 가진 전문직이다. 과거 사법시험 합격률이 2~3%로 매우 낮아 '고시 낭인' 문제가 있었고, 이를 해결하기 위해 로스쿨 제도를 도입했다. 변호사는 법정 변론 외에도 기업 자문, 계약서 검토, M&A 자문 등 다양한 업무를 한다. 최근 변호사 수가 증가하면서 경쟁이 치열해지고 있다. 베트남과 달리 한국은 변호사 강제주의를 채택하여 일정 금액 이상 소송은 반드시 변호사를 선임해야 한다.",
        "commonMistakes": [
            {
                "mistake": "변호사가 형사 사건만 담당한다고 설명",
                "correction": "민사, 형사, 행정, 가사 등 모든 법률 분야 담당 가능",
                "explanation": "단일 자격제이므로 전 분야 수임 자격 있음"
            },
            {
                "mistake": "Luật sư bào chữa(형사변호사)로만 번역",
                "correction": "Luật sư가 포괄적 용어, 필요시 분야 특정",
                "explanation": "변호사는 형사 변론뿐 아니라 모든 법률 사무 담당"
            },
            {
                "mistake": "변호사 자격 취득이 쉽다고 설명",
                "correction": "한국은 매우 어렵고 경쟁이 치열한 자격임을 강조",
                "explanation": "베트남과 달리 한국은 변호사 자격 취득이 매우 어려움"
            }
        ],
        "examples": [
            {
                "ko": "변호사를 선임하여 소송을 준비하고 있습니다.",
                "vi": "Đang chuẩn bị kiện tụng với việc chỉ định luật sư.",
                "situation": "formal"
            },
            {
                "ko": "이 계약서는 변호사의 검토를 받은 후 서명하겠습니다.",
                "vi": "Sẽ ký hợp đồng này sau khi được luật sư xem xét.",
                "situation": "formal"
            },
            {
                "ko": "변호사-의뢰인 간 비밀은 법적으로 보호됩니다.",
                "vi": "Bí mật giữa luật sư và khách hàng được bảo vệ về mặt pháp lý.",
                "situation": "formal"
            }
        ],
        "relatedTerms": ["법무법인", "변론", "소송대리", "법률자문", "변호사시험"]
    },
    {
        "slug": "tro-giup-phap-ly",
        "korean": "법률구조",
        "vietnamese": "Trợ giúp pháp lý",
        "hanja": "法律救助",
        "hanjaReading": "法(법 법) + 律(법 률) + 救(구원할 구) + 助(도울 조)",
        "pronunciation": "쩌 zúp fáp lí",
        "meaningKo": "경제적으로 어렵거나 법을 잘 모르는 국민에게 무료 또는 저렴한 비용으로 법률 서비스를 제공하는 제도. 한국에는 대한법률구조공단이라는 국가기관이 있어 일정 소득 이하 국민에게 소송 대리, 법률 상담, 형사변호 등을 지원한다. 통역 시 주의할 점은 법률구조가 자선이 아닌 '국민의 권리'라는 점이다. 헌법은 국가에게 법률구조 제도를 실시할 의무를 부과하고 있다. 베트남도 법률구조 제도가 있지만 한국이 더 체계적이고 지원 범위가 넓다. 법률구조는 민사, 형사, 가사 사건 모두 가능하며, 특히 성폭력, 가정폭력, 산재 사건 등에는 소득 요건을 완화하여 지원한다. 변호사 비용이 부담되는 서민들에게 법률 접근권을 보장하는 중요한 제도이다.",
        "meaningVi": "Chế độ cung cấp dịch vụ pháp lý miễn phí hoặc chi phí thấp cho công dân gặp khó khăn về kinh tế hoặc không hiểu rõ pháp luật. Hàn Quốc có Công đoàn Trợ giúp Pháp lý Hàn Quốc, cơ quan nhà nước hỗ trợ đại diện tố tụng, tư vấn pháp luật, biện hộ hình sự cho công dân có thu nhập dưới mức nhất định.",
        "context": "법률 접근권, 사회복지, 소송 지원",
        "culturalNote": "한국의 법률구조 제도는 1972년 대한법률구조공단 설립으로 시작되었다. 법률구조는 단순히 가난한 사람을 돕는 것이 아니라 '법 앞의 평등'을 실질적으로 보장하는 헌법적 권리이다. 외국인 근로자, 결혼이민자 등에게도 법률구조가 제공되며, 최근에는 온라인 상담도 활발하다. 베트남 근로자들이 한국에서 임금 체불, 산재 등의 문제를 겪을 때 법률구조공단의 도움을 받을 수 있다는 점을 통역 시 적극 안내해야 한다.",
        "commonMistakes": [
            {
                "mistake": "법률구조를 자선 사업으로 설명",
                "correction": "국가가 헌법상 의무로 실시하는 제도임을 명확히",
                "explanation": "법률구조는 권리이지 시혜가 아님"
            },
            {
                "mistake": "법률구조가 형사 사건만 지원한다고 설명",
                "correction": "민사, 형사, 가사, 행정 사건 모두 지원 가능",
                "explanation": "법률구조 범위는 매우 포괄적"
            },
            {
                "mistake": "외국인은 법률구조를 받을 수 없다고 설명",
                "correction": "외국인 근로자, 결혼이민자 등도 지원 대상",
                "explanation": "한국에 합법적으로 체류하는 외국인도 법률구조 가능"
            }
        ],
        "examples": [
            {
                "ko": "소득이 낮으면 법률구조공단을 통해 무료 변호사를 선임할 수 있습니다.",
                "vi": "Nếu thu nhập thấp, có thể chỉ định luật sư miễn phí thông qua Công đoàn Trợ giúp Pháp lý.",
                "situation": "formal"
            },
            {
                "ko": "외국인 근로자도 임금 체불 사건에서 법률구조를 받을 수 있습니다.",
                "vi": "Lao động nước ngoài cũng có thể nhận trợ giúp pháp lý trong vụ án nợ lương.",
                "situation": "onsite"
            },
            {
                "ko": "법률구조공단 홈페이지에서 온라인 법률 상담을 신청하세요.",
                "vi": "Hãy đăng ký tư vấn pháp luật trực tuyến trên trang web Công đoàn Trợ giúp Pháp lý.",
                "situation": "informal"
            }
        ],
        "relatedTerms": ["대한법률구조공단", "무료변론", "법률상담", "접근권", "공익변호"]
    },
    {
        "slug": "vien-dao-tao-tu-phap",
        "korean": "사법연수원",
        "vietnamese": "Viện Đào tạo Tư pháp",
        "hanja": "司法硏修院",
        "hanjaReading": "司(맡을 사) + 法(법 법) + 硏(연구할 연) + 修(닦을 수) + 院(집 원)",
        "pronunciation": "비엔 다오 따오 tư fáp",
        "meaningKo": "법조인 양성 교육기관. 과거 사법시험 합격자들이 2년간 법조윤리, 실무 교육을 받던 곳으로, 졸업 후 판사, 검사, 변호사로 임용되었다. 2017년 사법시험 폐지 후 로스쿨 체제로 전환되면서 역할이 축소되었으나, 여전히 신임 판사·검사에게 보충 교육을 제공한다. 통역 시 주의할 점은 사법연수원이 단순 교육기관이 아니라 법조인 '선발'과 '검증'의 마지막 관문이었다는 것이다. 사법연수원 성적이 판사·검사 임용과 대형 로펌 취업에 결정적 영향을 미쳤다. 베트남에는 이런 통합 법조인 교육기관이 없고 판사·검사·변호사가 별도 경로로 양성된다. 한국의 법조 일원화(판사·검사·변호사가 같은 자격 기반) 개념을 설명하는 것이 중요하다.",
        "meaningVi": "Cơ sở giáo dục đào tạo pháp nhân. Trước đây, những người đậu kỳ thi tư pháp học 2 năm về đạo đức pháp nhân và thực vụ, sau khi tốt nghiệp được bổ nhiệm làm thẩm phán, kiểm sát viên, luật sư. Sau khi bãi bỏ kỳ thi tư pháp năm 2017 và chuyển sang chế độ trường luật, vai trò bị thu hẹp.",
        "context": "법조인 교육, 사법시험, 법조 자격",
        "culturalNote": "한국의 사법연수원은 법조인들의 강한 동질감과 네트워크를 형성하는 데 기여했다. 같은 '기수'(연수원 입소 연도) 출신들은 평생 유대를 유지하며, 이것이 한국 법조계의 특징이다. 사법연수원에서는 모의재판, 법률문서 작성, 법정 변론 등 실무 중심 교육을 받았다. 로스쿨 도입 후 이런 집중 교육이 로스쿨로 분산되었지만, 여전히 신임 법관·검사는 사법연수원에서 추가 연수를 받는다. 베트남 통역사들에게는 한국의 '법조 일원화' 개념(모든 법조인이 같은 출발점)을 설명하는 것이 중요하다.",
        "commonMistakes": [
            {
                "mistake": "사법연수원을 로스쿨과 혼동",
                "correction": "로스쿨은 법학전문대학원, 사법연수원은 실무 연수기관",
                "explanation": "로스쿨 도입 후 사법연수원 역할이 변화했으나 별개 기관"
            },
            {
                "mistake": "Trường luật(로스쿨)으로 번역",
                "correction": "Viện Đào tạo Tư pháp 또는 Viện Nghiên tu Tư pháp",
                "explanation": "법학대학원과는 다른 실무 연수 기관"
            },
            {
                "mistake": "현재도 모든 법조인이 사법연수원을 거친다고 설명",
                "correction": "2017년 이후는 로스쿨 출신, 판사·검사만 추가 연수",
                "explanation": "법조인 양성 체계가 변화했음을 반영"
            }
        ],
        "examples": [
            {
                "ko": "그는 사법연수원 43기로 판사로 임용되었습니다.",
                "vi": "Anh ấy là khóa 43 Viện Đào tạo Tư pháp và được bổ nhiệm làm thẩm phán.",
                "situation": "formal"
            },
            {
                "ko": "사법연수원에서는 모의재판을 통해 실무 능력을 키웁니다.",
                "vi": "Tại Viện Đào tạo Tư pháp, nâng cao năng lực thực vụ thông qua phiên tòa giả định.",
                "situation": "formal"
            },
            {
                "ko": "사법시험 폐지 후 사법연수원의 역할이 축소되었습니다.",
                "vi": "Sau khi bãi bỏ kỳ thi tư pháp, vai trò của Viện Đào tạo Tư pháp bị thu hẹp.",
                "situation": "formal"
            }
        ],
        "relatedTerms": ["사법시험", "로스쿨", "법조인", "기수", "법조 일원화"]
    },
    {
        "slug": "dao-duc-phap-nhan",
        "korean": "법조윤리",
        "vietnamese": "Đạo đức pháp nhân",
        "hanja": "法曹倫理",
        "hanjaReading": "法(법 법) + 曹(무리 조) + 倫(인륜 륜) + 理(다스릴 리)",
        "pronunciation": "다오 득 fáp nhân",
        "meaningKo": "법조인(판사, 검사, 변호사)이 지켜야 할 직업윤리. 공정성, 독립성, 성실의무, 비밀유지의무, 품위유지의무 등을 포함한다. 통역 시 주의할 점은 한국에서 법조윤리 위반이 매우 엄격하게 처벌된다는 것이다. 판사·검사는 탄핵이나 징계로 파면될 수 있고, 변호사는 변호사법에 따라 업무정지·등록취소 처분을 받을 수 있다. 특히 이해충돌(conflict of interest) 규정이 엄격하여, 과거 담당했던 사건과 관련된 일을 할 수 없다. 예를 들어 판사·검사로 재직 중 다룬 사건을 변호사로 전직한 후 수임하는 것은 금지된다. 또한 법조인은 의뢰인 비밀을 누설하면 형사처벌을 받으며, 품위손상 행위(음주운전, 성범죄 등)도 엄격히 징계된다. 베트남보다 훨씬 엄격한 윤리 기준이 적용된다.",
        "meaningVi": "Đạo đức nghề nghiệp mà pháp nhân (thẩm phán, kiểm sát viên, luật sư) phải tuân thủ. Bao gồm tính công bằng, độc lập, nghĩa vụ tận tâm, nghĩa vụ bảo mật, nghĩa vụ giữ uy tín. Ở Hàn Quốc, vi phạm đạo đức pháp nhân bị xử phạt rất nghiêm khắc, thẩm phán/kiểm sát viên có thể bị luận tội hoặc kỷ luật cách chức, luật sư bị đình chỉ hoặc hủy đăng ký.",
        "context": "법조인 의무, 직업윤리, 징계",
        "culturalNote": "한국 법조계는 매우 높은 윤리 기준을 요구받는다. 최근 법조비리(판사·검사·변호사 간 유착, 금품수수 등)에 대한 사회적 비판이 강해지면서 윤리 규정이 더욱 강화되고 있다. '전관예우' 문제(퇴직 판사·검사가 변호사로 개업하여 과거 인맥 활용)도 법조윤리 차원에서 비판받는다. 법조인은 공적 인물로서 사생활에서도 높은 도덕성을 요구받으며, SNS 발언조차 품위유지 의무 위반으로 징계받을 수 있다. 베트남보다 법조인에 대한 사회적 기대와 감시가 훨씬 강하다.",
        "commonMistakes": [
            {
                "mistake": "법조윤리를 '일반 직업윤리'와 동일시",
                "correction": "공권력 행사자로서 훨씬 엄격한 기준 적용",
                "explanation": "법조인은 국민의 권리와 자유를 다루므로 특별한 책임"
            },
            {
                "mistake": "윤리 위반이 도덕적 비난으로만 끝난다고 설명",
                "correction": "징계, 파면, 형사처벌까지 이어질 수 있음",
                "explanation": "법조윤리는 법적 강제력이 있는 의무"
            },
            {
                "mistake": "Đạo đức nghề nghiệp chung(일반 직업윤리)으로 번역",
                "correction": "Đạo đức pháp nhân(법조윤리)로 특정",
                "explanation": "법조인의 특수한 윤리 의무를 나타내는 전문 용어"
            }
        ],
        "examples": [
            {
                "ko": "법조윤리를 위반하여 변호사 자격이 정지되었습니다.",
                "vi": "Đã bị đình chỉ tư cách luật sư do vi phạm đạo đức pháp nhân.",
                "situation": "formal"
            },
            {
                "ko": "과거 판사로 담당했던 사건을 변호사로 수임하는 것은 법조윤리 위반입니다.",
                "vi": "Nhận vụ án mà trước đây đã phụ trách với tư cách thẩm phán khi làm luật sư là vi phạm đạo đức pháp nhân.",
                "situation": "formal"
            },
            {
                "ko": "변호사는 의뢰인의 비밀을 지킬 법조윤리상 의무가 있습니다.",
                "vi": "Luật sư có nghĩa vụ theo đạo đức pháp nhân phải giữ bí mật của khách hàng.",
                "situation": "formal"
            }
        ],
        "relatedTerms": ["품위유지의무", "비밀유지의무", "이해충돌", "징계", "전관예우"]
    }
]


def load_json():
    """JSON 파일 로드"""
    try:
        with open(JSON_PATH, "r", encoding="utf-8") as f:
            return json.load(f)
    except FileNotFoundError:
        print(f"❌ 파일을 찾을 수 없습니다: {JSON_PATH}")
        return None
    except json.JSONDecodeError as e:
        print(f"❌ JSON 파싱 오류: {e}")
        return None


def save_json(data):
    """JSON 파일 저장 (들여쓰기 2칸, 유니코드 그대로, 마지막 줄바꿈)"""
    try:
        with open(JSON_PATH, "w", encoding="utf-8") as f:
            json.dump(data, f, ensure_ascii=False, indent=2)
            f.write("\n")  # 마지막 줄바꿈 추가
        return True
    except Exception as e:
        print(f"❌ 파일 저장 오류: {e}")
        return False


def add_terms():
    """용어 추가 메인 로직"""
    print("=" * 80)
    print("법률 도메인 용어 추가 스크립트 v8-j")
    print("테마: 법원조직/사법제도")
    print("=" * 80)
    print()

    # 1. 기존 데이터 로드
    data = load_json()
    if data is None:
        return

    existing_slugs = {term["slug"] for term in data}
    print(f"✅ 기존 용어 수: {len(data)}개")
    print()

    # 2. 중복 체크
    new_slugs = [term["slug"] for term in NEW_TERMS]
    duplicates = [slug for slug in new_slugs if slug in existing_slugs]

    if duplicates:
        print(f"⚠️  중복된 slug 발견: {', '.join(duplicates)}")
        print("중복 제거 후 진행합니다.")
        print()

    # 3. 신규 용어만 필터링
    terms_to_add = [term for term in NEW_TERMS if term["slug"] not in existing_slugs]

    if not terms_to_add:
        print("⚠️  추가할 신규 용어가 없습니다.")
        return

    # 4. 추가할 용어 미리보기
    print(f"📝 추가할 용어: {len(terms_to_add)}개")
    print("-" * 80)
    for i, term in enumerate(terms_to_add, 1):
        print(f"{i}. {term['korean']} ({term['vietnamese']}) - {term['slug']}")
    print("-" * 80)
    print()

    # 5. 용어 추가
    data.extend(terms_to_add)
    print(f"✅ {len(terms_to_add)}개 용어를 데이터에 추가했습니다.")
    print(f"📊 총 용어 수: {len(data)}개")
    print()

    # 6. 파일 저장
    if save_json(data):
        print(f"✅ 파일 저장 완료: {JSON_PATH}")
        print()
        print("=" * 80)
        print("🎉 작업 완료!")
        print("=" * 80)
        print()
        print("📌 다음 단계:")
        print("   npm run validate:terms -- --domain=legal")
    else:
        print("❌ 파일 저장 실패")


if __name__ == "__main__":
    add_terms()
