#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
민사소송/재판절차 전문용어 추가 스크립트 (Civil Litigation/Court Procedure)
Tier S 품질 기준 준수
"""

import json
import os

# 파일 경로 설정
file_path = os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', 'data', 'terms', 'legal.json')

# 기존 데이터 로드
with open(file_path, 'r', encoding='utf-8') as f:
    data = json.load(f)  # data is a LIST

# 기존 slug 추출 (중복 방지)
existing_slugs = {t['slug'] for t in data}

# 새 용어 정의
new_terms = [
    {
        "slug": "nguyen-don",
        "korean": "원고",
        "vietnamese": "nguyên đơn",
        "hanja": "原告",
        "hanjaReading": "原(근원 원) + 告(고할 고)",
        "pronunciation": "응우옌 던",
        "meaningKo": "민사소송에서 소를 제기하는 당사자. 통역 시 '원고 측'은 'phía nguyên đơn', '원고 대리인'은 'đại diện nguyên đơn'으로 정확히 구분해야 합니다. 베트남 법정에서는 원고가 먼저 진술하는 순서가 엄격히 지켜지므로, 소송 절차 통역 시 이 점을 유의해야 합니다. 또한 베트남에서는 원고가 소송비용을 먼저 예납하는 제도(tạm ứng án phí)가 있어, 한국의 인지대 제도와 차이가 있습니다.",
        "meaningVi": "Người khởi kiện trong vụ án dân sự. Nguyên đơn là bên đề nghị tòa án giải quyết tranh chấp và bảo vệ quyền, lợi ích hợp pháp của mình. Nguyên đơn có quyền yêu cầu bồi thường thiệt hại, trả lại tài sản hoặc các biện pháp khắc phục khác.",
        "context": "민사소송, 법정 절차, 소장 작성",
        "culturalNote": "한국에서는 원고가 소를 제기하면서 인지대를 납부하지만, 베트남에서는 소송비용(án phí)을 예납하는 제도가 있어 절차상 차이가 있습니다. 또한 베트남 법정은 한국보다 원고의 입증 책임을 더 엄격히 요구하는 경향이 있으며, 원고가 충분한 증거를 제출하지 못하면 소가 각하될 수 있습니다. 한국의 '원고 적격'은 베트남에서 'tư cách nguyên đơn'으로 번역되며, 법적 개념이 유사합니다.",
        "commonMistakes": [
            {
                "mistake": "nguyên cáo (응우옌 까오)",
                "correction": "nguyên đơn (응우옌 던)",
                "explanation": "원고는 'nguyên đơn'이 정확한 법률 용어입니다. 'nguyên cáo'는 형사사건의 '고소인'을 뜻하므로 민사소송에서는 사용하지 않습니다."
            },
            {
                "mistake": "người kiện (응으어이 끼엔)",
                "correction": "nguyên đơn (응우옌 던)",
                "explanation": "'người kiện'은 일상어이며, 법정에서는 반드시 'nguyên đơn'이라는 정식 법률 용어를 사용해야 합니다."
            },
            {
                "mistake": "bên khởi kiện (벤 커이 끼엔)",
                "correction": "nguyên đơn (응우옌 던)",
                "explanation": "'bên khởi kiện'은 '소를 제기하는 측'이라는 의미로 맞지만, 법정 기록에서는 'nguyên đơn'이 공식 용어입니다."
            },
            {
                "mistake": "원고인 (nguyên đơn nhân)",
                "correction": "nguyên đơn (응우옌 던)",
                "explanation": "베트nam어에서는 '~인'을 붙이지 않고 'nguyên đơn'만 사용합니다. 'nhân'을 붙이면 부자연스럽습니다."
            }
        ],
        "examples": [
            {
                "ko": "원고는 피고에게 1억 원의 손해배상을 청구합니다.",
                "vi": "Nguyên đơn yêu cầu bị đơn bồi thường thiệt hại 100 triệu won.",
                "situation": "formal"
            },
            {
                "ko": "원고 측 증인이 법정에 출석했습니다.",
                "vi": "Nhân chứng phía nguyên đơn đã có mặt tại phiên tòa.",
                "situation": "onsite"
            },
            {
                "ko": "원고는 계약 위반을 이유로 소를 제기했습니다.",
                "vi": "Nguyên đơn đã khởi kiện với lý do vi phạm hợp đồng.",
                "situation": "formal"
            }
        ],
        "relatedTerms": ["bi-don", "phien-toa", "ban-an", "dai-dien-phap-luat"]
    },
    {
        "slug": "bi-don",
        "korean": "피고",
        "vietnamese": "bị đơn",
        "hanja": "被告",
        "hanjaReading": "被(입을 피) + 告(고할 고)",
        "pronunciation": "비 던",
        "meaningKo": "민사소송에서 소를 제기당한 당사자. 통역 시 '피고 측'은 'phía bị đơn', '피고 대리인'은 'đại diện bị đơn'으로 구분해야 합니다. 베트남 법정에서는 피고가 답변서(đơn答변)를 제출해야 하며, 한국과 달리 피고의 불출석 시에도 재판이 진행될 수 있습니다. 피고의 방어권 보장은 '권리 보호'(quyền bào chữa)로 번역되며, 법정에서 매우 중요한 개념입니다.",
        "meaningVi": "Người bị kiện trong vụ án dân sự. Bị đơn là bên phải trả lời yêu cầu của nguyên đơn và bảo vệ quyền lợi của mình trước tòa án. Bị đơn có quyền phản bác, đưa ra chứng cứ và yêu cầu tòa án bác yêu cầu của nguyên đơn.",
        "context": "민사소송, 답변서 제출, 법정 방어",
        "culturalNote": "한국에서는 피고가 답변서를 제출하지 않으면 원고 주장을 인정한 것으로 간주될 수 있지만, 베트남에서는 피고의 불출석이나 미답변이 자동적인 패소를 의미하지 않습니다. 베트남 법원은 직권으로 증거를 조사할 수 있어, 피고가 방어하지 않아도 법원이 사실관계를 확인합니다. 또한 베트남에서는 피고가 반소(phản tố)를 제기할 수 있는 기한이 한국보다 짧으므로 통역 시 주의가 필요합니다.",
        "commonMistakes": [
            {
                "mistake": "bị cáo (비 까오)",
                "correction": "bị đơn (비 던)",
                "explanation": "'bị cáo'는 형사사건의 '피고인'을 뜻합니다. 민사소송에서는 반드시 'bị đơn'을 사용해야 합니다."
            },
            {
                "mistake": "người bị kiện (응으어이 비 끼엔)",
                "correction": "bị đơn (비 던)",
                "explanation": "'người bị kiện'은 일상어이며, 법정에서는 'bị đơn'이라는 공식 법률 용어를 사용해야 합니다."
            },
            {
                "mistake": "đối tượng kiện (도이 뜨엉 끼엔)",
                "correction": "bị đơn (비 던)",
                "explanation": "'đối tượng kiện'은 '소송 대상'이라는 뜻으로, 피고 당사자를 지칭할 때는 부적절합니다."
            },
            {
                "mistake": "피고인 (bị cáo)",
                "correction": "bị đơn (비 던)",
                "explanation": "한국어 '피고'를 형사 용어 'bị cáo'로 잘못 번역하는 경우가 많습니다. 민사는 'bị đơn'입니다."
            }
        ],
        "examples": [
            {
                "ko": "피고는 원고의 청구를 전면 부인했습니다.",
                "vi": "Bị đơn đã hoàn toàn phủ nhận yêu cầu của nguyên đơn.",
                "situation": "formal"
            },
            {
                "ko": "피고 측 변호사가 반박 의견을 제출했습니다.",
                "vi": "Luật sư phía bị đơn đã trình bày ý kiến phản bác.",
                "situation": "onsite"
            },
            {
                "ko": "피고는 다음 공판기일까지 증거를 제출해야 합니다.",
                "vi": "Bị đơn phải nộp chứng cứ trước phiên tòa tiếp theo.",
                "situation": "formal"
            }
        ],
        "relatedTerms": ["nguyen-don", "phien-toa", "khang-cao", "dai-dien-phap-luat"]
    },
    {
        "slug": "toa-an",
        "korean": "법원",
        "vietnamese": "tòa án",
        "hanja": "法院",
        "hanjaReading": "法(법 법) + 院(집 원)",
        "pronunciation": "토아 안",
        "meaningKo": "법에 따라 민사·형사·행정 사건을 심판하는 국가 기관. 통역 시 베트남의 법원 체계는 한국과 다르므로 주의해야 합니다. 베트남은 '인민법원'(Tòa án Nhân dân) 체계로, 지방인민법원(cấp huyện), 성인민법원(cấp tỉnh), 고등인민법원(cấp cao), 대법원(Tòa án Nhân dân Tối cao) 4급으로 나뉩니다. 한국의 '지방법원'은 성인민법원에, '고등법원'은 고등인민법원에 대응되지만 정확히 일치하지는 않습니다. '법원 관할'은 'thẩm quyền của tòa án'으로 번역됩니다.",
        "meaningVi": "Cơ quan nhà nước có thẩm quyền xét xử các vụ án dân sự, hình sự, hành chính và các tranh chấp khác theo quy định của pháp luật. Hệ thống tòa án Việt Nam gồm Tòa án Nhân dân các cấp: cấp huyện, cấp tỉnh, cấp cao và Tòa án Nhân dân Tối cao.",
        "context": "사법 제도, 재판 관할, 소송 절차",
        "culturalNote": "한국은 '법원'이라는 중립적 명칭을 사용하지만, 베트남은 '인민법원'(Tòa án Nhân dân)으로 사회주의 체제의 특성을 반영합니다. 베트남 법원은 국회에 대해 책임을 지는 구조로, 한국의 사법부 독립 원칙과 차이가 있습니다. 또한 베트남에서는 '인민참심원'(hội thẩm nhân dân) 제도가 있어, 일반 시민이 판사와 함께 재판에 참여하는 점이 특징입니다. 통역 시 양국 법원의 권한과 역할 차이를 명확히 이해해야 합니다.",
        "commonMistakes": [
            {
                "mistake": "toà (토아)",
                "correction": "tòa án (토아 안)",
                "explanation": "'toà'만 사용하면 '법정'이나 '건물'을 뜻할 수 있습니다. 법원 기관을 지칭할 때는 'tòa án'을 완전히 발음해야 합니다."
            },
            {
                "mistake": "pháp viện (팝 비엔)",
                "correction": "tòa án (토아 안)",
                "explanation": "'pháp viện'은 중국식 한자어 번역으로, 베트남에서는 사용하지 않습니다. 'tòa án'이 정확한 용어입니다."
            },
            {
                "mistake": "tòa án Hàn Quốc (토아 안 한 꾸옥)",
                "correction": "tòa án của Hàn Quốc (토아 안 꾸아 한 꾸옥)",
                "explanation": "한국 법원을 지칭할 때는 소유격 'của'를 넣어야 자연스럽습니다."
            },
            {
                "mistake": "법원에 가다 (đến tòa án)",
                "correction": "ra tòa (라 토아)",
                "explanation": "'법원에 가다'는 'đến tòa án'보다 'ra tòa'(재판받다, 출정하다)가 더 자연스러운 표현입니다."
            }
        ],
        "examples": [
            {
                "ko": "이 사건은 서울중앙지방법원에 계류 중입니다.",
                "vi": "Vụ án này đang được giải quyết tại Tòa án Nhân dân tỉnh Seoul trung tâm.",
                "situation": "formal"
            },
            {
                "ko": "법원은 다음 주에 판결을 선고할 예정입니다.",
                "vi": "Tòa án dự kiến tuyên án vào tuần tới.",
                "situation": "onsite"
            },
            {
                "ko": "법원의 허가를 받아야 재산을 처분할 수 있습니다.",
                "vi": "Phải được sự cho phép của tòa án mới có thể xử lý tài sản.",
                "situation": "formal"
            }
        ],
        "relatedTerms": ["tham-phan", "phien-toa", "ban-an", "khang-cao"]
    },
    {
        "slug": "tham-phan",
        "korean": "판사",
        "vietnamese": "thẩm phán",
        "hanja": "審判",
        "hanjaReading": "審(살필 심) + 判(판단할 판)",
        "pronunciation": "탐 판",
        "meaningKo": "법원에서 재판을 주재하고 판결을 내리는 법관. 통역 시 베트남에서는 '판사'와 '인민참심원'을 명확히 구분해야 합니다. 베트남의 판사는 'thẩm phán', 인민참심원은 'hội thẩm nhân dân'입니다. 한국의 '재판장'은 'chủ tọa phiên tòa' 또는 'thẩm phán chủ tọa'로 번역되며, 합의부에서 가장 중요한 역할을 합니다. 베트남에서는 판사가 직권으로 증거조사를 할 수 있어, 한국보다 적극적인 역할을 수행합니다. '판사님'을 부를 때는 'thưa thẩm phán' 또는 'kính thưa hội đồng xét xử'(재판부에 아뢰옵니다)를 사용합니다.",
        "meaningVi": "Người có thẩm quyền chủ tọa phiên tòa, xem xét, đánh giá chứng cứ và tuyên án theo quy định của pháp luật. Thẩm phán là thành viên chuyên nghiệp của Hội đồng xét xử, có nhiệm vụ bảo đảm việc xét xử đúng pháp luật và công bằng.",
        "context": "법정 절차, 재판 진행, 판결 선고",
        "culturalNote": "한국에서는 판사가 독립적으로 판결하며 외부 간섭을 받지 않지만, 베트남에서는 판사가 국회와 인민의 감독을 받는 구조입니다. 베트남 법정에서는 판사가 검사 및 변호사와 함께 앉아 있는 배치가 일반적이며, 한국처럼 판사가 높은 곳에 혼자 앉는 것과 다릅니다. 또한 베트남에서는 '인민참심원'이 판사와 동등한 권한으로 재판에 참여하므로, 통역 시 '재판부'는 'hội đồng xét xử'(판사+참심원)로 번역해야 정확합니다.",
        "commonMistakes": [
            {
                "mistake": "quan tòa (꾸안 토아)",
                "correction": "thẩm phán (탐 판)",
                "explanation": "'quan tòa'는 오래된 표현으로, 현대 베트남에서는 'thẩm phán'을 사용합니다."
            },
            {
                "mistake": "pháp quan (팝 꾸안)",
                "correction": "thẩm phán (탐 판)",
                "explanation": "'pháp quan'은 중국식 한자어로, 베트남 법률 용어는 'thẩm phán'입니다."
            },
            {
                "mistake": "thẩm phán viên (탐 판 비엔)",
                "correction": "thẩm phán (탐 판)",
                "explanation": "'viên'을 붙이지 않고 'thẩm phán'만 사용합니다. '~viên'은 불필요한 접미사입니다."
            },
            {
                "mistake": "재판장 (thẩm phán trưởng)",
                "correction": "chủ tọa phiên tòa (쭈 토아 피엔 토아)",
                "explanation": "재판장은 'thẩm phán trưởng'보다 'chủ tọa phiên tòa'가 공식 법률 용어입니다."
            }
        ],
        "examples": [
            {
                "ko": "판사님, 추가 증거를 제출하고자 합니다.",
                "vi": "Kính thưa thẩm phán, chúng tôi xin trình bày thêm chứng cứ.",
                "situation": "onsite"
            },
            {
                "ko": "재판부는 3명의 판사로 구성됩니다.",
                "vi": "Hội đồng xét xử gồm 3 thẩm phán.",
                "situation": "formal"
            },
            {
                "ko": "판사는 양측의 주장을 신중히 검토했습니다.",
                "vi": "Thẩm phán đã xem xét cẩn thận lập luận của hai bên.",
                "situation": "formal"
            }
        ],
        "relatedTerms": ["toa-an", "phien-toa", "ban-an", "hoi-dong-xet-xu"]
    },
    {
        "slug": "phien-toa",
        "korean": "공판",
        "vietnamese": "phiên tòa",
        "hanja": "公判",
        "hanjaReading": "公(공변될 공) + 判(판단할 판)",
        "pronunciation": "피엔 토아",
        "meaningKo": "법원에서 사건을 심리하고 판결하는 재판 절차. 통역 시 '공판기일'은 'ngày xét xử' 또는 'ngày mở phiên tòa', '공판 준비'는 'chuẩn bị xét xử'로 번역합니다. 베트남에서는 공판이 공개 원칙(công khai)을 따르지만, 국가기밀이나 미풍양속 사건은 비공개로 진행됩니다. 한국의 '첫 공판'은 'phiên tòa đầu tiên', '속행 공판'은 'phiên tòa tiếp theo'로 번역되며, 베트남 법정은 한국보다 공판 연기가 적고 집중심리 원칙이 강합니다. '공판 조서'는 'biên bản phiên tòa'로 번역됩니다.",
        "meaningVi": "Quá trình xét xử công khai tại tòa án, trong đó Hội đồng xét xử tiến hành thẩm vấn, xem xét chứng cứ, nghe ý kiến của các bên và tuyên án. Phiên tòa phải được tiến hành công khai, trừ trường hợp pháp luật quy định khác vì lý do bảo vệ bí mật nhà nước hoặc thuần phong mỹ tục.",
        "context": "재판 절차, 증인 심문, 변론",
        "culturalNote": "한국에서는 공판이 여러 차례 연기되거나 나뉘어 진행되는 경우가 많지만, 베트남에서는 '집중심리 원칙'(nguyên tắc tập trung xét xử)에 따라 한 번의 공판에서 사건을 종결하려고 노력합니다. 베트남 법정에서는 판사가 직접 증인을 심문하고, 변호사는 판사의 허가를 받아 질문하는 구조로 한국과 다릅니다. 또한 베트남에서는 '인민참심원'이 공판에 참여하며, 일반 시민의 의견이 판결에 반영될 수 있습니다. 공판 진행 순서도 양국이 달라 통역 시 주의가 필요합니다.",
        "commonMistakes": [
            {
                "mistake": "tòa án (토아 안)",
                "correction": "phiên tòa (피엔 토아)",
                "explanation": "'tòa án'은 법원 기관을, 'phiên tòa'는 재판 절차를 뜻합니다. '공판'은 'phiên tòa'입니다."
            },
            {
                "mistake": "phiên xử (피엔 쓰)",
                "correction": "phiên tòa (피엔 토아)",
                "explanation": "'phiên xử'는 비공식적 표현이며, 공식 법률 용어는 'phiên tòa'입니다."
            },
            {
                "mistake": "buổi xét xử (부오이 셋 쓰)",
                "correction": "phiên tòa (피엔 토아)",
                "explanation": "'buổi xét xử'는 일상어이며, 법정 기록에는 'phiên tòa'를 사용해야 합니다."
            },
            {
                "mistake": "공판 개정 (mở phiên tòa)",
                "correction": "khai mạc phiên tòa (카이 막 피엔 토아)",
                "explanation": "공판 개정(개시)은 'mở'보다 'khai mạc'가 더 공식적인 표현입니다."
            }
        ],
        "examples": [
            {
                "ko": "다음 공판은 2월 15일로 지정되었습니다.",
                "vi": "Phiên tòa tiếp theo được ấn định vào ngày 15 tháng 2.",
                "situation": "formal"
            },
            {
                "ko": "공판에서 증인 3명이 출석하여 증언했습니다.",
                "vi": "Tại phiên tòa, 3 nhân chứng đã có mặt và khai báo.",
                "situation": "onsite"
            },
            {
                "ko": "공판은 오전 9시에 시작됩니다.",
                "vi": "Phiên tòa bắt đầu lúc 9 giờ sáng.",
                "situation": "formal"
            }
        ],
        "relatedTerms": ["tham-phan", "toa-an", "ban-an", "nhan-chung"]
    },
    {
        "slug": "ban-an",
        "korean": "판결",
        "vietnamese": "bản án",
        "hanja": "判決",
        "hanjaReading": "判(판단할 판) + 決(결정할 결)",
        "pronunciation": "반 안",
        "meaningKo": "법원이 소송 사건에 대해 내리는 최종적인 법적 결정. 통역 시 '판결문'은 'bản án', '판결 선고'는 'tuyên án', '판결 이유'는 'lý do của bản án'으로 번역합니다. 베트남에서는 판결이 확정되면 '법적 효력 발생'(có hiệu lực pháp luật)이라고 표현하며, 한국의 '확정판결'은 'bản án đã có hiệu lực'로 번역됩니다. 베트남 판결문은 한국보다 짧고 간결하며, 판결 이유가 상대적으로 간단한 편입니다. '승소 판결'은 'bản án thắng kiện', '패소 판결'은 'bản án thua kiện'으로 번역됩니다.",
        "meaningVi": "Quyết định cuối cùng của tòa án về vụ án sau khi xem xét toàn bộ chứng cứ và lập luận của các bên. Bản án bao gồm phần mở đầu, nội dung vụ án, lý do và quyết định của tòa án. Bản án có hiệu lực pháp luật sau khi hết thời hạn kháng cáo hoặc kháng nghị.",
        "context": "재판 결과, 법적 효력, 집행",
        "culturalNote": "한국에서는 판결문이 매우 상세하게 작성되며, 판결 이유가 수십 페이지에 달하는 경우도 많지만, 베트남 판결문은 비교적 간결합니다. 베트남에서는 판결이 선고되면 즉시 '원본'(bản chính)과 '사본'(bản sao)이 발급되며, 당사자는 사본을 받습니다. 한국의 '선고 유예'는 베트남에서 'hoãn thi hành án'(판결 집행 유예)로 번역되지만, 법적 개념이 다소 다릅니다. 베트남에서는 판결 확정 후 집행이 매우 신속하게 이루어지는 편입니다.",
        "commonMistakes": [
            {
                "mistake": "phán quyết (판 꾸엣)",
                "correction": "bản án (반 안)",
                "explanation": "'phán quyết'은 '결정'이나 '판단'을 뜻하며, '판결문'은 'bản án'입니다."
            },
            {
                "mistake": "quyết định (꾸엣 딘)",
                "correction": "bản án (반 안)",
                "explanation": "'quyết định'은 '결정'(재판 외 행정결정 등)이며, 재판의 판결은 'bản án'입니다."
            },
            {
                "mistake": "tuyên án (뜨엔 안)",
                "correction": "bản án (반 안)",
                "explanation": "'tuyên án'은 판결을 '선고하는 행위'이고, 판결문 자체는 'bản án'입니다."
            },
            {
                "mistake": "판결서 (văn bản án)",
                "correction": "bản án (반 안)",
                "explanation": "베트남어에서는 'văn bản'을 붙이지 않고 'bản án'만으로 판결문을 의미합니다."
            }
        ],
        "examples": [
            {
                "ko": "법원은 원고 승소 판결을 내렸습니다.",
                "vi": "Tòa án đã tuyên bản án thắng kiện cho nguyên đơn.",
                "situation": "formal"
            },
            {
                "ko": "판결문은 일주일 내에 교부됩니다.",
                "vi": "Bản án sẽ được giao trong vòng một tuần.",
                "situation": "onsite"
            },
            {
                "ko": "이 판결은 항소심에서 파기되었습니다.",
                "vi": "Bản án này đã bị hủy tại phiên tòa phúc thẩm.",
                "situation": "formal"
            }
        ],
        "relatedTerms": ["tham-phan", "phien-toa", "khang-cao", "thi-hanh-an"]
    },
    {
        "slug": "khang-cao",
        "korean": "항소",
        "vietnamese": "kháng cáo",
        "hanja": "抗訴",
        "hanjaReading": "抗(막을 항) + 訴(호소할 소)",
        "pronunciation": "캉 까오",
        "meaningKo": "1심 판결에 불복하여 상급 법원에 다시 재판해 달라고 청구하는 절차. 통역 시 '항소장'은 'đơn kháng cáo', '항소 기간'은 'thời hạn kháng cáo', '항소심'은 'phiên tòa phúc thẩm'으로 번역합니다. 베트남에서는 항소 기간이 판결 선고일로부터 15일이며, 한국(2주)과 비슷하지만 계산 방식이 다를 수 있습니다. 베트남의 항소심은 '복심'(phúc thẩm) 개념으로, 사실관계와 법률 적용을 모두 다시 심리합니다. '항소 취하'는 'rút đơn kháng cáo', '항소 기각'은 'bác kháng cáo'로 번역됩니다.",
        "meaningVi": "Việc người có quyền và lợi ích liên quan yêu cầu tòa án cấp trên xem xét lại bản án, quyết định sơ thẩm chưa có hiệu lực pháp luật. Kháng cáo phải được nộp trong thời hạn 15 ngày kể từ ngày tuyên án sơ thẩm. Tòa án phúc thẩm sẽ xem xét lại toàn bộ vụ án về cả sự kiện và pháp luật.",
        "context": "불복 절차, 상급심, 재판 청구",
        "culturalNote": "한국에서는 항소 이유를 명확히 기재해야 하지만, 베트남에서는 항소장에 간단히 '판결에 불복한다'고만 써도 접수됩니다. 베트남 항소심은 한국보다 '직권 조사'가 강하여, 당사자가 주장하지 않은 부분도 법원이 조사할 수 있습니다. 또한 베트남에서는 항소 제기 시 '항소 비용'(lệ phí kháng cáo)을 납부해야 하며, 한국의 인지대와 유사합니다. 베트남 항소심은 한국보다 신속하게 진행되는 편으로, 대부분 3~6개월 내에 판결이 나옵니다.",
        "commonMistakes": [
            {
                "mistake": "kháng nghị (캉 응이)",
                "correction": "kháng cáo (캉 까오)",
                "explanation": "'kháng nghị'는 검찰이 제기하는 '상고'를 뜻합니다. 당사자가 제기하는 항소는 'kháng cáo'입니다."
            },
            {
                "mistake": "phản đối (판 도이)",
                "correction": "kháng cáo (캉 까오)",
                "explanation": "'phản đối'는 일상어로 '반대하다'는 뜻이며, 법적 항소는 'kháng cáo'입니다."
            },
            {
                "mistake": "kêu oan (꺼우 완)",
                "correction": "kháng cáo (캉 까오)",
                "explanation": "'kêu oan'은 '억울함을 호소하다'는 의미로, 법정 항소 절차는 'kháng cáo'입니다."
            },
            {
                "mistake": "항소심 (tòa án kháng cáo)",
                "correction": "phúc thẩm (푹 탐)",
                "explanation": "항소심 재판은 'phúc thẩm'(복심)이라고 하며, 'tòa án kháng cáo'는 부자연스럽습니다."
            }
        ],
        "examples": [
            {
                "ko": "피고는 판결에 불복하여 항소했습니다.",
                "vi": "Bị đơn đã kháng cáo do không đồng ý với bản án.",
                "situation": "formal"
            },
            {
                "ko": "항소 기간은 내일까지입니다.",
                "vi": "Thời hạn kháng cáo là đến hết ngày mai.",
                "situation": "onsite"
            },
            {
                "ko": "항소심에서 원심 판결이 유지되었습니다.",
                "vi": "Tại phiên tòa phúc thẩm, bản án sơ thẩm đã được giữ nguyên.",
                "situation": "formal"
            }
        ],
        "relatedTerms": ["ban-an", "khang-nghi", "phuc-tham", "so-tham"]
    },
    {
        "slug": "khang-nghi",
        "korean": "상고",
        "vietnamese": "kháng nghị",
        "hanja": "上告",
        "hanjaReading": "上(위 상) + 告(고할 고)",
        "pronunciation": "캉 응이",
        "meaningKo": "항소심 판결에 불복하여 최고 법원(대법원)에 재심사를 청구하는 최종 불복 절차. 통역 시 주의할 점은, 베트남에서 'kháng nghị'는 주로 검찰총장이 제기하는 특별 불복 절차를 의미하며, 한국의 '상고'와 정확히 일치하지 않습니다. 베트남에서 당사자가 제기하는 상고는 'kháng cáo lên Tòa án Nhân dân Tối cao'(대법원에 항소)로 표현하기도 합니다. 베트남 대법원은 '법률 위반'만 심사하며, 사실관계는 다시 조사하지 않습니다. '상고 이유서'는 'đơn kháng nghị có nêu lý do', '상고 기각'은 'bác kháng nghị'로 번역됩니다.",
        "meaningVi": "Việc Viện trưởng Viện kiểm sát nhân dân tối cao hoặc người có thẩm quyền yêu cầu Tòa án Nhân dân Tối cao xem xét lại bản án, quyết định đã có hiệu lực pháp luật nhưng có vi phạm pháp luật nghiêm trọng. Kháng nghị giám đốc thẩm là biện pháp đặc biệt để bảo đảm tính chính xác của bản án.",
        "context": "최종 불복, 법률 심사, 대법원",
        "culturalNote": "한국에서는 당사자 누구나 상고할 수 있지만, 베트남에서 'kháng nghị'는 주로 검찰총장의 권한입니다. 당사자의 상고는 '재심 청구'(tái thẩm) 또는 '감독심 청구'(giám đốc thẩm) 형태로 이루어지며, 절차가 한국과 다릅니다. 베트남 대법원은 한국보다 상고 사건을 매우 제한적으로 받아들이며, 대부분의 사건은 항소심에서 종결됩니다. 베트남의 상고 제도는 사회주의 법체계의 특성을 반영하여, 검찰의 역할이 매우 중요합니다. 통역 시 '상고'를 단순히 'kháng nghị'로만 번역하면 오해를 초래할 수 있으므로, 문맥에 따라 정확히 설명해야 합니다.",
        "commonMistakes": [
            {
                "mistake": "kháng cáo lần 2 (캉 까오 런 2)",
                "correction": "kháng nghị (캉 응이) 또는 giám đốc thẩm (잠 독 탐)",
                "explanation": "상고를 '2차 항소'로 표현하면 안 됩니다. 베트남에서는 'kháng nghị' 또는 'giám đốc thẩm'이 정확합니다."
            },
            {
                "mistake": "thượng tố (뜨엉 또)",
                "correction": "kháng nghị (캉 응이)",
                "explanation": "'thượng tố'는 중국식 한자어로, 베트남에서는 사용하지 않습니다."
            },
            {
                "mistake": "kháng cáo lên Tòa án Tối cao (캉 까오 렌 토아 안 또이 까오)",
                "correction": "kháng nghị (캉 응이) 또는 giám đốc thẩm (잠 독 탐)",
                "explanation": "대법원에 대한 불복은 일반 'kháng cáo'와 다르며, 공식적으로 'kháng nghị' 또는 'giám đốc thẩm'입니다."
            },
            {
                "mistake": "상소 (kháng cáo)",
                "correction": "상고는 kháng nghị, 항소는 kháng cáo",
                "explanation": "한국어 '상소'를 베트남어로 번역할 때 항소와 상고를 명확히 구분해야 합니다."
            }
        ],
        "examples": [
            {
                "ko": "검찰은 판결에 대해 상고했습니다.",
                "vi": "Viện kiểm sát đã kháng nghị đối với bản án.",
                "situation": "formal"
            },
            {
                "ko": "대법원은 상고를 기각했습니다.",
                "vi": "Tòa án Nhân dân Tối cao đã bác kháng nghị.",
                "situation": "formal"
            },
            {
                "ko": "상고 이유는 법률 적용의 오류입니다.",
                "vi": "Lý do kháng nghị là có sai sót trong việc áp dụng pháp luật.",
                "situation": "onsite"
            }
        ],
        "relatedTerms": ["khang-cao", "ban-an", "phuc-tham", "giam-doc-tham"]
    },
    {
        "slug": "hoa-giai",
        "korean": "조정",
        "vietnamese": "hòa giải",
        "hanja": "調停",
        "hanjaReading": "調(고를 조) + 停(머물 정)",
        "pronunciation": "호아 자이",
        "meaningKo": "분쟁 당사자가 법원이나 조정위원회의 중재로 합의하여 분쟁을 해결하는 절차. 통역 시 '조정 절차'는 'thủ tục hòa giải', '조정 성립'은 'hòa giải thành', '조정 불성립'은 'hòa giải không thành'으로 번역합니다. 베트남에서는 법원 조정(hòa giải tại tòa án) 외에도 마을 조정(hòa giải ở cơ sở)이 매우 활성화되어 있으며, 소송 전에 조정을 거치도록 권장됩니다. 베트남의 조정은 한국보다 강제성이 약하며, 당사자의 자발적 합의를 중시합니다. '조정 조서'는 'biên bản hòa giải', '조정 조항'은 'điều khoản hòa giải'로 번역됩니다.",
        "meaningVi": "Hoạt động do tòa án, cơ quan hòa giải hoặc hòa giải viên thực hiện nhằm giúp các bên tự nguyện thỏa thuận với nhau để giải quyết tranh chấp. Hòa giải thành sẽ lập thành biên bản có giá trị pháp lý. Hòa giải là phương thức ưu tiên để giải quyết tranh chấp dân sự trước khi khởi kiện.",
        "context": "분쟁 해결, 합의, 소송 전 절차",
        "culturalNote": "베트남 사회에서는 '화해'와 '조정'을 매우 중시하며, 소송보다 조정을 통한 해결을 선호합니다. 베트남에는 '마을 조정위원회'(Tổ hòa giải ở cơ sở)가 광범위하게 설치되어 있어, 작은 분쟁은 마을에서 먼저 조정을 시도합니다. 한국의 법원 조정과 달리, 베트남 조정은 '조정관'(hòa giải viên)이 주도하며, 판사가 직접 조정하는 경우는 적습니다. 베트남에서 조정이 성립하면 '집행력'(có hiệu lực thi hành)이 있어 판결과 동일한 효력을 가집니다. 통역 시 조정의 중요성과 문화적 배경을 이해해야 합니다.",
        "commonMistakes": [
            {
                "mistake": "hòa hợp (호아 헙)",
                "correction": "hòa giải (호아 자이)",
                "explanation": "'hòa hợp'은 '화합하다'는 의미이며, 법적 조정은 'hòa giải'입니다."
            },
            {
                "mistake": "thương lượng (뜨엉 르엉)",
                "correction": "hòa giải (호아 자이)",
                "explanation": "'thương lượng'은 '협상하다'는 뜻이며, 법정 조정은 'hòa giải'입니다."
            },
            {
                "mistake": "điều đình (디에우 딘)",
                "correction": "hòa giải (호아 자이)",
                "explanation": "'điều đình'은 '중재'를 뜻하며, 조정은 'hòa giải'입니다. 'điều đình'은 국제법이나 외교에서 사용됩니다."
            },
            {
                "mistake": "조정위원회 (ủy ban hòa giải)",
                "correction": "Tổ hòa giải (또 호아 자이)",
                "explanation": "베트남 마을 조정위원회는 'Tổ hòa giải ở cơ sở'이며, 'ủy ban'보다 'Tổ'가 정확합니다."
            }
        ],
        "examples": [
            {
                "ko": "법원은 양측에 조정을 권고했습니다.",
                "vi": "Tòa án đã đề nghị hai bên tiến hành hòa giải.",
                "situation": "formal"
            },
            {
                "ko": "조정이 성립되어 소송이 취하되었습니다.",
                "vi": "Hòa giải đã thành nên vụ kiện đã được rút.",
                "situation": "onsite"
            },
            {
                "ko": "조정 조서는 판결과 동일한 효력이 있습니다.",
                "vi": "Biên bản hòa giải có hiệu lực pháp lý như bản án.",
                "situation": "formal"
            }
        ],
        "relatedTerms": ["nguyen-don", "bi-don", "phien-toa", "ban-an"]
    },
    {
        "slug": "thi-hanh-an",
        "korean": "강제집행",
        "vietnamese": "thi hành án",
        "hanja": "强制執行",
        "hanjaReading": "强(강할 강) + 制(제도 제) + 執(잡을 집) + 行(다닐 행)",
        "pronunciation": "티 한 안",
        "meaningKo": "확정된 판결이나 조정 내용을 강제로 실현하는 법적 절차. 통역 시 '강제집행 신청'은 'đơn yêu cầu thi hành án', '집행 불능'은 'không thể thi hành án', '집행 정지'는 'tạm đình chỉ thi hành án'으로 번역합니다. 베트남에서는 집행 기관이 '민사판결집행국'(Cục Thi hành án dân sự)으로, 법원과 별도 조직입니다. 한국은 법원이 직접 집행하지만, 베트남은 법무부 산하 집행국이 담당하여 시스템이 다릅니다. 베트남에서는 판결 확정 후 당사자가 '집행 신청'을 해야 집행이 시작되며, 자동으로 진행되지 않습니다. '집행관'은 'chấp hành viên'으로 번역됩니다.",
        "meaningVi": "Hoạt động của cơ quan thi hành án dân sự nhằm buộc người phải thi hành án thực hiện đúng và đầy đủ nghĩa vụ ghi trong bản án, quyết định đã có hiệu lực pháp luật. Thi hành án bao gồm các biện pháp như kê biên tài sản, phong tỏa tài khoản, cưỡng chế giao tài sản.",
        "context": "판결 집행, 재산 압류, 강제 이행",
        "culturalNote": "한국에서는 법원 집행관이 집행을 담당하지만, 베트남에서는 법무부 산하 '민사판결집행국'이 전담합니다. 베트남의 집행 절차는 한국보다 느리고 복잡하며, 채무자가 재산을 숨기는 경우 집행이 어려울 수 있습니다. 베트남에서는 '집행 불능'(không thể thi hành án) 비율이 높아, 승소 판결을 받아도 실제 집행까지는 시간이 오래 걸립니다. 베트남에는 '집행 화해'(hòa giải trong thi hành án) 제도가 있어, 집행 단계에서도 당사자 간 합의를 유도합니다. 통역 시 집행 절차의 현실적 어려움을 설명해야 할 때가 많습니다.",
        "commonMistakes": [
            {
                "mistake": "cưỡng chế (꾸엉 쩨)",
                "correction": "thi hành án (티 한 안)",
                "explanation": "'cưỡng chế'는 '강제'라는 일반적 의미이며, 법적 '강제집행'은 'thi hành án'입니다."
            },
            {
                "mistake": "thực thi án (턱 티 안)",
                "correction": "thi hành án (티 한 안)",
                "explanation": "'thực thi án'은 비공식적 표현이며, 공식 법률 용어는 'thi hành án'입니다."
            },
            {
                "mistake": "thi hành bản án (티 한 반 안)",
                "correction": "thi hành án (티 한 안)",
                "explanation": "'bản'을 넣지 않고 'thi hành án'만 사용하는 것이 표준 용어입니다."
            },
            {
                "mistake": "집행 법원 (tòa án thi hành)",
                "correction": "Cục Thi hành án dân sự (꾹 티 한 안 진 쓰)",
                "explanation": "베트남에서는 법원이 아니라 '민사판결집행국'이 집행을 담당합니다."
            }
        ],
        "examples": [
            {
                "ko": "판결 확정 후 강제집행을 신청했습니다.",
                "vi": "Sau khi bản án có hiệu lực, đã nộp đơn yêu cầu thi hành án.",
                "situation": "formal"
            },
            {
                "ko": "집행관이 채무자의 재산을 압류했습니다.",
                "vi": "Chấp hành viên đã kê biên tài sản của người phải thi hành án.",
                "situation": "onsite"
            },
            {
                "ko": "강제집행이 완료되어 채권이 회수되었습니다.",
                "vi": "Thi hành án đã hoàn tất và khoản nợ đã được thu hồi.",
                "situation": "formal"
            }
        ],
        "relatedTerms": ["ban-an", "nguyen-don", "bi-don", "tai-san"]
    }
]

# 중복 필터링
new_terms_filtered = [t for t in new_terms if t['slug'] not in existing_slugs]

if not new_terms_filtered:
    print("❌ 모든 용어가 이미 존재합니다. 추가할 항목이 없습니다.")
else:
    # 기존 데이터에 추가
    data.extend(new_terms_filtered)

    # 파일 저장
    with open(file_path, 'w', encoding='utf-8') as f:
        json.dump(data, f, ensure_ascii=False, indent=2)

    print(f"✅ {len(new_terms_filtered)}개 용어 추가 완료!")
    print(f"📁 파일: {file_path}")
    print(f"📊 총 용어 수: {len(data)}개")

    # 추가된 용어 목록 출력
    print("\n추가된 용어:")
    for term in new_terms_filtered:
        print(f"  - {term['slug']}: {term['korean']} ({term['vietnamese']})")
