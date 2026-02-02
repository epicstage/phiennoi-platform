#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""공증/인증 용어 추가 (v11-D)"""
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
            "slug": "cong-chung",
            "korean": "공증",
            "vietnamese": "Công chứng",
            "hanja": "公證",
            "hanjaReading": "公(공변할 공) + 證(증거 증)",
            "pronunciation": "공증",
            "meaningKo": "공증(公證)은 특정 법률행위나 사실이 진정하게 성립되었음을 공적 기관이 증명하는 제도입니다. 통역 시 베트남의 공증제도가 한국보다 훨씬 광범위하게 활용된다는 점을 주의해야 합니다. 한국에서는 주로 공증인이 담당하지만 베트남에서는 Văn phòng công chứng(공증사무소) 외에도 UBND(인민위원회)에서도 공증 업무를 수행할 수 있습니다. 특히 부동산 거래, 위임장, 계약서 등에서 공증이 필수적인 경우가 많아 통역사는 양국의 공증 요건 차이를 명확히 설명할 수 있어야 합니다.",
            "meaningVi": "Công chứng là việc cơ quan có thẩm quyền xác nhận tính xác thực của một hành vi pháp lý hoặc sự kiện. Ở Việt Nam, công chứng được thực hiện tại Văn phòng công chứng hoặc UBND cấp xã/phường. Công chứng là bắt buộc đối với nhiều giao dịch quan trọng như mua bán bất động sản, ủy quyền, di chúc.",
            "context": "법률 서류 작성 및 부동산 거래 시",
            "culturalNote": "베트남에서는 한국보다 공증이 훨씬 더 광범위하게 요구됩니다. 특히 외국인이 관련된 거래에서는 거의 모든 중요 서류가 공증을 거쳐야 하며, 공증 비용도 거래 금액에 따라 달라집니다. 한국에서는 공증인 사무실에서만 공증이 가능하지만, 베트남에서는 읍면동 사무소(UBND)에서도 일부 공증 업무를 처리할 수 있어 접근성이 더 높습니다.",
            "commonMistakes": [
                {
                    "mistake": "공증과 인증을 혼동하여 번역",
                    "correction": "공증은 Công chứng, 인증은 Chứng thực으로 구분",
                    "explanation": "공증은 법률행위의 진정성을 증명하는 것이고, 인증은 서명이나 사본의 진실성을 확인하는 것으로 법적 효력이 다릅니다"
                },
                {
                    "mistake": "베트남의 공증 범위를 한국과 동일하게 생각",
                    "correction": "베트남은 훨씬 광범위한 공증 요구사항이 있음을 설명",
                    "explanation": "베트남에서는 임대차 계약, 차용증 등 한국에서는 공증이 선택사항인 문서도 공증이 필수인 경우가 많습니다"
                },
                {
                    "mistake": "공증 기관을 단순히 'notary office'로만 설명",
                    "correction": "Văn phòng công chứng과 UBND의 차이를 명확히 구분",
                    "explanation": "베트남에서는 두 기관 모두 공증 업무를 수행하지만 처리 가능한 업무 범위와 수수료가 다릅니다"
                }
            ],
            "examples": [
                {
                    "ko": "부동산 매매 계약서는 반드시 공증을 받아야 합니다",
                    "vi": "Hợp đồng mua bán bất động sản phải được công chứng",
                    "situation": "formal"
                },
                {
                    "ko": "공증 수수료는 거래 금액의 0.5%입니다",
                    "vi": "Phí công chứng là 0,5% giá trị giao dịch",
                    "situation": "onsite"
                },
                {
                    "ko": "이 서류는 공증인의 인증을 받았습니다",
                    "vi": "Tài liệu này đã được công chứng viên xác nhận",
                    "situation": "formal"
                }
            ],
            "relatedTerms": ["인증", "사서증서", "확정일자", "진정성립"]
        },
        {
            "slug": "chung-thuc",
            "korean": "인증",
            "vietnamese": "Chứng thực",
            "hanja": "認證",
            "hanjaReading": "認(인정할 인) + 證(증거 증)",
            "pronunciation": "인증",
            "meaningKo": "인증(認證)은 서명, 날인, 서류 사본의 진정성을 공적 기관이 확인해주는 행위입니다. 공증과 달리 인증은 형식적 진정성만을 확인하며 내용의 적법성까지 보증하지는 않습니다. 통역 시 '인증'과 '공증'의 법적 효력 차이를 명확히 구분해야 하며, 특히 베트남어로는 인증이 Chứng thực, 공증이 Công chứng으로 다릅니다. 한국에서는 주민센터에서 간단한 인증 업무를 처리하지만, 베트남에서는 UBND나 Phòng Tư pháp(법무과)에서 담당합니다. 외국인 서류의 경우 영사 인증(Lãnh sự hóa)이 추가로 필요할 수 있습니다.",
            "meaningVi": "Chứng thực là việc cơ quan có thẩm quyền xác nhận chữ ký, con dấu hoặc bản sao của tài liệu là đúng với bản chính. Chứng thực không đảm bảo tính hợp pháp của nội dung tài liệu mà chỉ xác nhận tính chân thực về hình thức. Thường được thực hiện tại UBND hoặc Phòng Tư pháp.",
            "context": "서류 사본 확인 및 서명 진위 확인 시",
            "culturalNote": "한국에서는 주민센터에서 간단히 '확인' 도장을 받는 수준의 인증도 많지만, 베트남에서는 Chứng thực이 더 공식적이고 엄격한 절차를 거칩니다. 특히 해외로 보내는 서류의 경우 Lãnh sự hóa(영사 인증)까지 거쳐야 하는 경우가 많습니다. 베트남에서는 사본 인증 비용도 페이지당 부과되는 경우가 많아 두꺼운 서류의 경우 비용이 상당할 수 있습니다.",
            "commonMistakes": [
                {
                    "mistake": "인증과 공증을 같은 의미로 사용",
                    "correction": "인증(Chứng thực)은 형식 확인, 공증(Công chứng)은 내용까지 증명",
                    "explanation": "인증은 서명이나 사본이 진짜인지만 확인하지만, 공증은 그 법률행위 자체의 진정성을 보증합니다"
                },
                {
                    "mistake": "영사 인증을 일반 인증과 동일하게 번역",
                    "correction": "영사 인증은 Lãnh sự hóa로 별도 표현",
                    "explanation": "해외 사용 서류의 영사 인증은 추가 단계로 외교부나 대사관이 관여하는 특별한 절차입니다"
                },
                {
                    "mistake": "인증 수수료를 고정 금액으로 안내",
                    "correction": "페이지 수나 서류 종류에 따라 달라짐을 설명",
                    "explanation": "베트남에서는 인증 비용이 서류 분량과 종류에 따라 차등 적용됩니다"
                }
            ],
            "examples": [
                {
                    "ko": "졸업증명서 사본에 대한 인증이 필요합니다",
                    "vi": "Cần chứng thực bản sao bằng tốt nghiệp",
                    "situation": "formal"
                },
                {
                    "ko": "서명 인증은 동사무소에서 받을 수 있습니다",
                    "vi": "Chứng thực chữ ký có thể làm tại UBND phường",
                    "situation": "onsite"
                },
                {
                    "ko": "해외로 보낼 서류는 영사 인증이 필요합니다",
                    "vi": "Tài liệu gửi ra nước ngoài cần lãnh sự hóa",
                    "situation": "formal"
                }
            ],
            "relatedTerms": ["공증", "아포스티유", "영사확인", "사본대조"]
        },
        {
            "slug": "sa-so-jeung-seo",
            "korean": "사서증서",
            "vietnamese": "Chứng thư tư",
            "hanja": "私署證書",
            "hanjaReading": "私(사사로울 사) + 署(관청 서) + 證(증거 증) + 書(글 서)",
            "pronunciation": "사서증서",
            "meaningKo": "사서증서(私署證書)는 공무원이 아닌 사인(私人)이 작성한 문서를 의미합니다. 계약서, 각서, 차용증 등이 대표적이며, 공증을 받지 않은 경우 법정에서 그 진정성립이 문제될 수 있습니다. 통역 시 베트남어로는 Chứng thư tư 또는 Văn bản tư로 표현하며, 이를 공문서(Văn bản công)와 명확히 구분해야 합니다. 한국 민사소송법에서는 사서증서의 경우 작성자의 서명이나 날인이 진정한 것으로 인정되면 그 문서 전체가 진정하게 성립된 것으로 추정되는 반면, 베트nam에서는 사서증서의 증명력이 상대적으로 약하여 분쟁 시 공증을 받지 않은 사서증서는 증거로서의 가치가 제한될 수 있습니다.",
            "meaningVi": "Chứng thư tư là văn bản do cá nhân tư nhân lập ra, không phải do cơ quan nhà nước ban hành. Bao gồm hợp đồng, giấy vay nợ, biên nhận. Nếu không được công chứng, tính xác thực của chứng thư tư có thể bị nghi ngờ trong tố tụng. Ở Việt Nam, giá trị chứng minh của chứng thư tư thấp hơn văn bản công.",
            "context": "개인 간 계약서 및 법적 문서 작성 시",
            "culturalNote": "한국에서는 사서증서라도 서명/날인만 진정하면 법적 효력이 인정되지만, 베트남에서는 공증 없는 사서증서의 증거력이 매우 약합니다. 특히 부동산이나 고액 거래에서는 반드시 공증을 받아야 하며, 공증 없는 계약서는 법원에서 거의 인정받지 못하는 경우가 많습니다. 이러한 차이 때문에 베트남인들은 한국에서도 사적 계약서를 작성할 때 습관적으로 공증을 원하는 경우가 많습니다.",
            "commonMistakes": [
                {
                    "mistake": "사서증서를 단순히 'private document'로 번역",
                    "correction": "Chứng thư tư 또는 Văn bản tư로 정확히 표현",
                    "explanation": "베트남 법률 용어로는 Chứng thư tư가 표준 표현이며, 공문서와 명확히 구분됩니다"
                },
                {
                    "mistake": "한국과 베트남의 사서증서 증명력을 동일하게 설명",
                    "correction": "베트남에서는 공증 없는 사서증서의 효력이 매우 제한적임을 강조",
                    "explanation": "한국에서는 서명만 진정하면 증거력이 있지만 베트남에서는 공증이 거의 필수입니다"
                },
                {
                    "mistake": "사서증서를 공증서와 혼동",
                    "correction": "공증을 받지 않은 개인 작성 문서임을 명확히 구분",
                    "explanation": "사서증서는 개인이 작성한 원본 상태의 문서이고, 공증서는 공증 절차를 거친 문서입니다"
                }
            ],
            "examples": [
                {
                    "ko": "이 차용증은 공증받지 않은 사서증서입니다",
                    "vi": "Giấy vay nợ này là chứng thư tư chưa công chứng",
                    "situation": "formal"
                },
                {
                    "ko": "사서증서의 진정성립을 다투겠습니다",
                    "vi": "Tôi sẽ tranh chấp tính xác thực của chứng thư tư này",
                    "situation": "formal"
                },
                {
                    "ko": "계약서는 사서증서지만 법적 효력은 있습니다",
                    "vi": "Hợp đồng là chứng thư tư nhưng vẫn có hiệu lực pháp lý",
                    "situation": "onsite"
                }
            ],
            "relatedTerms": ["공문서", "공정증서", "진정성립", "추정"]
        },
        {
            "slug": "xac-dinh-nhat-tu",
            "korean": "확정일자",
            "vietnamese": "Xác định nhật tự",
            "hanja": "確定日字",
            "hanjaReading": "確(확실할 확) + 定(정할 정) + 日(날 일) + 字(글자 자)",
            "pronunciation": "확정일자",
            "meaningKo": "확정일자(確定日字)는 특정 문서가 그 날짜에 존재했음을 공적으로 증명하는 제도입니다. 주로 임대차 계약서에서 대항력을 갖추기 위해 필요하며, 한국에서는 주민센터나 등기소에서 확정일자를 받을 수 있습니다. 통역 시 베트남에는 이와 정확히 대응하는 제도가 없다는 점을 주의해야 합니다. 베트남에서는 계약서 자체를 공증하는 방식으로 날짜를 확정하며, 한국의 확정일자처럼 간단한 날짜 스탬프만 찍는 제도는 없습니다. 특히 주택임대차보호법상의 대항력과 우선변제권 설명 시, 베트남인에게는 이 개념이 생소할 수 있어 구체적인 사례로 설명해야 합니다.",
            "meaningVi": "Xác định nhật tự là việc cơ quan có thẩm quyền xác nhận một văn bản đã tồn tại vào ngày cụ thể. Chủ yếu dùng cho hợp đồng thuê nhà để có hiệu lực đối kháng. Ở Hàn Quốc, có thể xin xác định nhật tự tại văn phòng hành chính hoặc văn phòng đăng ký. Việt Nam không có chế độ tương tự, thay vào đó phải công chứng toàn bộ hợp đồng.",
            "context": "임대차 계약 및 채권 관계 성립 시",
            "culturalNote": "한국의 확정일자 제도는 베트남에 없는 독특한 시스템입니다. 한국에서는 단돈 600원으로 확정일자를 받아 수억 원의 보증금을 보호받을 수 있지만, 베트남에서는 임대차 계약서를 공증해야 하며 비용도 훨씬 높습니다. 베트남인에게 확정일자를 설명할 때는 '날짜 증명 스탬프'라는 개념 자체가 생소할 수 있으므로, 대항력과 우선변제권의 실제 효과를 사례 중심으로 설명하는 것이 효과적입니다.",
            "commonMistakes": [
                {
                    "mistake": "확정일자를 공증과 동일한 것으로 설명",
                    "correction": "확정일자는 날짜만 증명하고 내용은 증명하지 않음을 명확히",
                    "explanation": "공증은 계약 내용의 진정성까지 증명하지만 확정일자는 단순히 그 날짜에 문서가 존재했다는 것만 증명합니다"
                },
                {
                    "mistake": "베트남에도 확정일자 제도가 있다고 오해",
                    "correction": "베트남에는 확정일자 개념이 없고 공증으로 대체됨을 설명",
                    "explanation": "베트남에서는 임대차 계약 자체를 공증하여 날짜를 확정합니다"
                },
                {
                    "mistake": "확정일자의 법적 효과를 단순하게 설명",
                    "correction": "대항력, 우선변제권 등 구체적 효과를 사례로 설명",
                    "explanation": "베트남인에게는 생소한 개념이므로 '집주인이 파산해도 보증금을 먼저 돌려받을 수 있다'는 식의 구체적 설명이 필요합니다"
                }
            ],
            "examples": [
                {
                    "ko": "임대차 계약서에 확정일자를 받아야 대항력이 생깁니다",
                    "vi": "Phải xin xác định nhật tự cho hợp đồng thuê nhà để có hiệu lực đối kháng",
                    "situation": "formal"
                },
                {
                    "ko": "확정일자는 동사무소에서 무료로 받을 수 있습니다",
                    "vi": "Xác định nhật tự có thể xin miễn phí tại văn phòng hành chính",
                    "situation": "onsite"
                },
                {
                    "ko": "확정일자가 없으면 우선변제권이 없습니다",
                    "vi": "Nếu không có xác định nhật tự thì không có quyền thanh toán ưu tiên",
                    "situation": "formal"
                }
            ],
            "relatedTerms": ["대항력", "우선변제권", "임대차계약서", "전입신고"]
        },
        {
            "slug": "jin-jeong-seong-reop",
            "korean": "진정성립",
            "vietnamese": "Thành lập chân chính",
            "hanja": "眞正成立",
            "hanjaReading": "眞(참 진) + 正(바를 정) + 成(이룰 성) + 立(설 립)",
            "pronunciation": "진정성립",
            "meaningKo": "진정성립(眞正成立)은 문서가 작성 명의인의 의사에 기하여 진실로 작성된 것을 의미합니다. 민사소송에서 사서증서의 증거능력을 인정받기 위해서는 진정성립이 증명되어야 하며, 이를 위해 통상 작성자의 서명이나 날인의 진정성을 먼저 증명합니다. 통역 시 베트남어로는 Thành lập chân chính 또는 Được lập một cách chân thực으로 표현하며, 이는 단순히 문서가 '존재한다'는 것이 아니라 '작성자의 진정한 의사로 만들어졌다'는 의미임을 명확히 해야 합니다. 한국 민사소송법 제358조는 사서증서의 서명 또는 날인이 본인의 것으로 인정되면 진정성립이 추정된다고 규정하지만, 베트남에서는 이러한 추정 규정이 약하여 공증의 중요성이 더 큽니다.",
            "meaningVi": "Thành lập chân chính có nghĩa là văn bản được lập ra theo ý chí thực sự của người có tên trong đó. Trong tố tụng dân sự, để chứng thư tư được công nhận là chứng cứ, phải chứng minh được tính thành lập chân chính. Thường phải chứng minh chữ ký hoặc con dấu là thật. Ở Việt Nam, do không có quy định suy đoán mạnh như Hàn Quốc, công chứng càng quan trọng.",
            "context": "민사소송 및 증거 제출 시",
            "culturalNote": "한국 법원은 서명이나 날인이 진정하면 문서 전체의 진정성립을 추정해주지만, 베트남 법원은 이러한 추정이 약합니다. 따라서 베트남에서는 애초에 공증을 받아두는 것이 분쟁 예방에 훨씬 효과적입니다. 통역 시 '진정성립의 추정'이라는 법리를 베트남인에게 설명할 때는, 한국 법원이 서명만 진짜로 인정되면 나머지는 법원이 믿어준다는 식으로 쉽게 풀어 설명하는 것이 좋습니다.",
            "commonMistakes": [
                {
                    "mistake": "진정성립을 단순히 '문서가 진짜'라고 번역",
                    "correction": "작성자의 의사에 따라 진실로 작성되었다는 의미로 정확히 설명",
                    "explanation": "진정성립은 문서의 물리적 진위가 아니라 작성 의사의 진정성을 의미합니다"
                },
                {
                    "mistake": "진정성립의 추정을 베트남에도 동일하게 적용",
                    "correction": "한국의 추정 규정이 베트남보다 훨씬 강력함을 설명",
                    "explanation": "한국은 서명만 진정하면 문서 전체를 추정하지만 베트남은 그렇지 않습니다"
                },
                {
                    "mistake": "진정성립과 증거능력을 혼동",
                    "correction": "진정성립은 증거능력의 전제 조건임을 명확히",
                    "explanation": "문서가 진정성립되어야 비로소 증거로 채택될 수 있습니다"
                }
            ],
            "examples": [
                {
                    "ko": "이 계약서의 진정성립을 다투겠습니다",
                    "vi": "Tôi sẽ tranh chấp tính thành lập chân chính của hợp đồng này",
                    "situation": "formal"
                },
                {
                    "ko": "서명이 본인 것으로 인정되면 진정성립이 추정됩니다",
                    "vi": "Nếu chữ ký được xác nhận là của bản thân thì suy đoán thành lập chân chính",
                    "situation": "formal"
                },
                {
                    "ko": "공증을 받으면 진정성립에 대한 다툼이 없습니다",
                    "vi": "Nếu công chứng thì không có tranh chấp về thành lập chân chính",
                    "situation": "onsite"
                }
            ],
            "relatedTerms": ["사서증서", "추정", "증거능력", "형식적증거력"]
        },
        {
            "slug": "gong-jeong-jeung-seo",
            "korean": "공정증서",
            "vietnamese": "Văn bản công chứng",
            "hanja": "公正證書",
            "hanjaReading": "公(공변할 공) + 正(바를 정) + 證(증거 증) + 書(글 서)",
            "pronunciation": "공정증서",
            "meaningKo": "공정증서(公正證書)는 공증인이 일정한 방식에 따라 작성한 공문서로, 집행력 있는 공정증서의 경우 재판 없이 바로 강제집행이 가능합니다. 금전대차, 양육비, 위자료 등에서 주로 활용되며, 특히 집행증서로서의 효력이 있어 채권자에게 강력한 권리구제 수단이 됩니다. 통역 시 베트남어로는 Văn bản công chứng 또는 Chứng thư công chứng으로 표현하며, 베트남에도 유사한 제도가 있지만 한국처럼 즉시 집행력을 부여하는 경우는 제한적입니다. 한국에서는 채무자가 공정증서 작성 시 '바로 강제집행을 당해도 좋다'는 집행인낙조항에 동의하면 판결 없이 압류가 가능하지만, 베트남에서는 대부분 법원 판결을 거쳐야 합니다.",
            "meaningVi": "Văn bản công chứng là văn bản do công chứng viên lập theo một thể thức nhất định, có tính chất văn bản công. Nếu là văn bản công chứng có hiệu lực thi hành thì có thể cưỡng chế thi hành ngay mà không cần phán quyết của tòa. Chủ yếu dùng trong cho vay tiền, tiền nuôi con, tiền bồi thường. Ở Việt Nam, hiệu lực thi hành trực tiếp như Hàn Quốc bị hạn chế.",
            "context": "금전대차 및 강제집행 필요 시",
            "culturalNote": "한국의 공정증서는 채권자에게 매우 강력한 권리구제 수단입니다. 특히 집행인낙조항이 있는 공정증서는 소송 없이 바로 재산을 압류할 수 있어, 베트남인들이 한국에서 처음 접하면 놀라는 경우가 많습니다. 베트남에서는 공증을 받아도 대부분 법원 판결을 거쳐야 강제집행이 가능하기 때문입니다. 통역 시 '소송 없이 바로 재산 압류가 가능하다'는 점을 명확히 강조해야 합니다.",
            "commonMistakes": [
                {
                    "mistake": "공정증서를 일반 공증 문서와 동일시",
                    "correction": "공정증서는 집행력이 있는 특별한 공문서임을 강조",
                    "explanation": "일반 공증은 진정성만 증명하지만 공정증서는 판결과 같은 집행력을 가질 수 있습니다"
                },
                {
                    "mistake": "집행인낙조항을 단순 동의로 설명",
                    "correction": "'소송 없이 바로 재산 압류 가능'이라는 강력한 효과를 명시",
                    "explanation": "베트남인에게는 이 조항의 법적 무게가 생소하므로 구체적 결과를 설명해야 합니다"
                },
                {
                    "mistake": "베트남에도 동일한 집행력이 있다고 오해",
                    "correction": "베트남은 대부분 법원 판결을 거쳐야 함을 설명",
                    "explanation": "한국의 공정증서 집행력은 국제적으로도 강한 편입니다"
                }
            ],
            "examples": [
                {
                    "ko": "공정증서를 작성하면 판결 없이 강제집행이 가능합니다",
                    "vi": "Nếu lập văn bản công chứng thì có thể cưỡng chế thi hành mà không cần phán quyết",
                    "situation": "formal"
                },
                {
                    "ko": "이 공정증서에는 집행인낙조항이 포함되어 있습니다",
                    "vi": "Văn bản công chứng này có điều khoản chấp thuận thi hành",
                    "situation": "formal"
                },
                {
                    "ko": "공증사무실에서 공정증서를 작성할 수 있습니다",
                    "vi": "Có thể lập văn bản công chứng tại văn phòng công chứng",
                    "situation": "onsite"
                }
            ],
            "relatedTerms": ["집행권원", "집행인낙조항", "강제집행", "공증"]
        },
        {
            "slug": "jip-haeng-in-rak-jo-hang",
            "korean": "집행인낙조항",
            "vietnamese": "Điều khoản chấp thuận thi hành",
            "hanja": "執行認諾條項",
            "hanjaReading": "執(잡을 집) + 行(다닐 행) + 認(인정할 인) + 諾(허락할 낙) + 條(가지 조) + 項(항목 항)",
            "pronunciation": "집행인낙조항",
            "meaningKo": "집행인낙조항(執行認諾條項)은 채무자가 채무불이행 시 즉시 강제집행을 당해도 이의 없다는 의사를 표시하는 조항입니다. 공정증서에 이 조항이 포함되면 채권자는 소송 절차 없이 바로 강제집행을 신청할 수 있어 매우 강력한 권리구제 수단이 됩니다. 통역 시 베트남어로는 Điều khoản chấp thuận thi hành 또는 Điều khoản đồng ý cưỡng chế로 표현하며, 이 조항의 법적 무게를 충분히 설명해야 합니다. 한국에서는 금전대차, 양육비, 위자료 등의 공정증서에서 흔히 사용되지만, 베트남에는 이와 같은 명시적 조항이 일반적이지 않아 베트남인들이 가볍게 서명했다가 큰 불이익을 받는 경우가 있습니다.",
            "meaningVi": "Điều khoản chấp thuận thi hành là điều khoản mà con nợ cam kết chấp nhận ngay lập tức cưỡng chế thi hành nếu không thực hiện nghĩa vụ. Nếu văn bản công chứng có điều khoản này thì chủ nợ có thể xin cưỡng chế ngay mà không cần khởi kiện. Ở Việt Nam, điều khoản rõ ràng như vậy không phổ biến, nên người Việt thường ký mà không hiểu hết hậu quả nghiêm trọng.",
            "context": "금전대차 및 공정증서 작성 시",
            "culturalNote": "집행인낙조항은 한국 법률문화에서 채권자를 강력하게 보호하는 독특한 장치입니다. 베트남인들은 이 조항의 의미를 충분히 이해하지 못하고 서명하는 경우가 많으며, 나중에 '소송도 없이 바로 재산이 압류되었다'며 놀라는 사례가 빈번합니다. 통역 시에는 '당신이 돈을 안 갚으면 법원에 가지 않고도 바로 당신의 은행계좌나 월급이 압류될 수 있다'는 식으로 구체적이고 강하게 설명해야 합니다. 특히 베트남에서는 대부분 법원 판결을 거쳐야 하므로, 한국의 이 제도가 얼마나 강력한지 비교하여 설명하는 것이 효과적입니다.",
            "commonMistakes": [
                {
                    "mistake": "집행인낙조항을 단순한 동의 조항으로 가볍게 설명",
                    "correction": "'소송 없이 즉시 재산 압류'라는 강력한 법적 효과를 명확히 강조",
                    "explanation": "베트남인은 이 조항의 무게를 모르고 가볍게 서명할 위험이 큽니다"
                },
                {
                    "mistake": "집행인낙조항과 일반 변제 약속을 혼동",
                    "correction": "일반 약속은 소송이 필요하지만 집행인낙조항은 소송 불필요함을 구분",
                    "explanation": "집행권원으로서의 특별한 지위를 가진다는 점을 명확히 해야 합니다"
                },
                {
                    "mistake": "베트남에도 비슷한 제도가 있다고 오해",
                    "correction": "베트남에는 이런 강력한 조항이 일반적이지 않음을 설명",
                    "explanation": "한국의 집행인낙조항은 매우 강력하고 독특한 제도입니다"
                }
            ],
            "examples": [
                {
                    "ko": "이 공정증서에는 집행인낙조항이 있어서 소송 없이 압류가 가능합니다",
                    "vi": "Văn bản công chứng này có điều khoản chấp thuận thi hành nên có thể phong tỏa mà không cần kiện",
                    "situation": "formal"
                },
                {
                    "ko": "집행인낙조항에 동의하면 불이행 시 즉시 강제집행됩니다",
                    "vi": "Nếu đồng ý điều khoản chấp thuận thi hành thì khi vi phạm sẽ bị cưỡng chế ngay",
                    "situation": "formal"
                },
                {
                    "ko": "이 조항은 매우 중요하니 신중히 결정하세요",
                    "vi": "Điều khoản này rất quan trọng, hãy quyết định thận trọng",
                    "situation": "onsite"
                }
            ],
            "relatedTerms": ["공정증서", "집행권원", "강제집행", "채무명의"]
        },
        {
            "slug": "yeong-sa-in-jeung",
            "korean": "영사인증",
            "vietnamese": "Lãnh sự hóa",
            "hanja": "領事認證",
            "hanjaReading": "領(거느릴 령) + 事(일 사) + 認(인정할 인) + 證(증거 증)",
            "pronunciation": "영사인증",
            "meaningKo": "영사인증(領事認證)은 한 나라에서 발행된 문서를 다른 나라에서 사용하기 위해 해당 국가의 영사관이 그 문서의 진정성을 확인하는 절차입니다. 통상 문서 발행국의 외교부 인증을 먼저 받은 후 사용국 대사관이나 영사관의 인증을 받는 2단계 절차를 거칩니다. 통역 시 베트남어로는 Lãnh sự hóa로 표현하며, 이는 아포스티유(Apostille)와는 다른 절차임을 명확히 해야 합니다. 한국과 베트남은 아직 아포스티유 협약 적용 대상이 아니므로(2024년 기준 베트남은 일부 문서만 적용), 대부분의 문서는 영사인증을 거쳐야 합니다. 특히 학력, 경력, 가족관계 등 개인 신분 관련 문서의 해외 사용 시 필수입니다.",
            "meaningVi": "Lãnh sự hóa là thủ tục xác nhận tính xác thực của văn bản do một quốc gia cấp để sử dụng tại quốc gia khác. Thông thường phải trải qua 2 bước: xác nhận của Bộ Ngoại giao nước cấp văn bản, sau đó xác nhận của Đại sứ quán nước sử dụng. Khác với Apostille. Do Hàn Quốc và Việt Nam chưa áp dụng đầy đủ Apostille, hầu hết văn bản cần lãnh sự hóa. Bắt buộc với văn bản cá nhân như học vấn, kinh nghiệm, quan hệ gia đình.",
            "context": "해외 취업, 유학, 결혼 등 국제 문서 사용 시",
            "culturalNote": "영사인증은 시간과 비용이 많이 드는 절차로, 보통 2~4주가 소요되며 비용도 문서당 수만 원씩 듭니다. 베트남인들이 한국에서 일하거나 유학하기 위해 베트남 문서를 가져올 때, 또는 한국인이 베트남에서 일할 때 모두 이 절차를 거쳐야 합니다. 특히 코로나19 이후 많은 나라가 아포스티유로 전환했지만, 한국-베트남 간에는 여전히 영사인증이 필요한 경우가 많아 번거로움을 느끼는 사람들이 많습니다. 통역 시 '외교부 → 대사관'의 2단계 절차와 예상 소요 시간을 명확히 안내해야 합니다.",
            "commonMistakes": [
                {
                    "mistake": "영사인증과 아포스티유를 동일하게 취급",
                    "correction": "영사인증은 2단계(외교부+대사관), 아포스티유는 1단계 절차임을 구분",
                    "explanation": "아포스티유는 협약 가입국 간 간소화된 절차이지만 영사인증은 전통적인 복잡한 절차입니다"
                },
                {
                    "mistake": "한국-베트남 모든 문서가 아포스티유 가능하다고 안내",
                    "correction": "대부분의 문서는 여전히 영사인증이 필요함을 명확히",
                    "explanation": "베트남은 아포스티유 가입국이지만 한국과의 관계에서는 제한적으로만 적용됩니다"
                },
                {
                    "mistake": "영사인증을 단순 번역 공증으로 오해",
                    "correction": "번역 공증과 별개로 원본 문서의 국가 간 진정성 확인 절차임을 설명",
                    "explanation": "번역 공증은 번역문의 정확성을, 영사인증은 원본 문서의 진정성을 증명합니다"
                }
            ],
            "examples": [
                {
                    "ko": "졸업증명서를 베트남에서 쓰려면 영사인증을 받아야 합니다",
                    "vi": "Để dùng bằng tốt nghiệp ở Việt Nam phải làm lãnh sự hóa",
                    "situation": "formal"
                },
                {
                    "ko": "영사인증은 외교부와 대사관 두 곳을 거쳐야 합니다",
                    "vi": "Lãnh sự hóa phải qua Bộ Ngoại giao và Đại sứ quán",
                    "situation": "onsite"
                },
                {
                    "ko": "영사인증에는 보통 2~3주가 걸립니다",
                    "vi": "Lãnh sự hóa thường mất 2-3 tuần",
                    "situation": "formal"
                }
            ],
            "relatedTerms": ["아포스티유", "외교부인증", "대사관", "국제문서"]
        },
        {
            "slug": "a-po-seu-ti-yu",
            "korean": "아포스티유",
            "vietnamese": "Apostille",
            "hanja": None,
            "hanjaReading": None,
            "pronunciation": "아포스티유",
            "meaningKo": "아포스티유(Apostille)는 1961년 헤이그 협약에 따라 협약 가입국 간에 문서의 진정성을 간소하게 인증하는 제도입니다. 전통적인 영사인증과 달리 문서 발행국의 외교부가 발급한 아포스티유 확인서만 있으면 다른 가입국에서 바로 사용할 수 있어 절차가 훨씬 간편합니다. 통역 시 베트남어로는 원어 그대로 Apostille로 표현하며, 일부 사람들은 Xác nhận Apostille(아포스티유 확인)이라고 부르기도 합니다. 한국은 2007년부터, 베트남은 2023년부터 헤이그 협약에 가입했으나, 양국 간 실무적용은 아직 제한적이므로 통역 시 영사인증이 여전히 필요한 경우가 많음을 안내해야 합니다. 특히 베트남은 단계적으로 아포스티유를 적용 중이라 문서 종류에 따라 가능 여부가 다릅니다.",
            "meaningVi": "Apostille là chế độ xác nhận đơn giản tính xác thực của văn bản giữa các nước thành viên Công ước Hague năm 1961. Khác với lãnh sự hóa truyền thống, chỉ cần giấy xác nhận Apostille do Bộ Ngoại giao nước cấp văn bản là có thể dùng ngay tại nước thành viên khác. Hàn Quốc gia nhập từ 2007, Việt Nam từ 2023 nhưng áp dụng thực tế giữa hai nước còn hạn chế. Việt Nam đang áp dụng từng bước nên tùy loại văn bản.",
            "context": "국제 문서 인증 및 해외 사용 시",
            "culturalNote": "아포스티유는 영사인증에 비해 시간과 비용을 크게 절약할 수 있는 제도입니다. 한국에서는 외교부나 법원, 검찰청 등에서 즉시 발급받을 수 있고 비용도 저렴합니다(문서당 3,000~5,000원). 그러나 베트남이 2023년에야 가입했고 단계적 적용 중이라, 모든 문서에 아포스티유가 적용되는 것은 아닙니다. 통역 시 해당 문서가 아포스티유 대상인지, 아니면 여전히 영사인증이 필요한지를 먼저 확인해야 하며, 불확실하면 베트남 대사관에 문의하도록 안내하는 것이 안전합니다. 특히 베트남인들에게는 아포스티유가 비교적 생소한 개념이므로 '간소화된 국가 간 문서 확인서'라고 설명하는 것이 이해를 돕습니다.",
            "commonMistakes": [
                {
                    "mistake": "한국-베트남 간 모든 문서가 아포스티유로 가능하다고 안내",
                    "correction": "베트남이 단계적 적용 중이므로 문서별로 확인 필요함을 명시",
                    "explanation": "베트남은 최근 가입국이라 아직 모든 문서에 아포스티유가 적용되지 않습니다"
                },
                {
                    "mistake": "아포스티유를 번역 공증으로 오해",
                    "correction": "아포스티유는 원본 문서의 국가 간 인증이고 번역은 별도임을 구분",
                    "explanation": "아포스티유는 원본의 진정성을 증명하고, 번역이 필요하면 공증번역을 추가로 받아야 합니다"
                },
                {
                    "mistake": "아포스티유 발급을 외교부에서만 가능하다고 안내",
                    "correction": "문서 종류에 따라 법원, 검찰청 등 여러 기관에서 발급 가능함을 설명",
                    "explanation": "학교 서류는 교육부, 법원 서류는 법원 등 발급 기관이 다릅니다"
                }
            ],
            "examples": [
                {
                    "ko": "이 졸업증명서는 아포스티유 확인을 받으면 바로 사용할 수 있습니다",
                    "vi": "Bằng tốt nghiệp này nếu có xác nhận Apostille thì dùng ngay được",
                    "situation": "formal"
                },
                {
                    "ko": "아포스티유는 외교부에서 당일 발급받을 수 있습니다",
                    "vi": "Apostille có thể xin ngay trong ngày tại Bộ Ngoại giao",
                    "situation": "onsite"
                },
                {
                    "ko": "베트남은 최근에 협약에 가입해서 일부 문서만 가능합니다",
                    "vi": "Việt Nam mới gia nhập gần đây nên chỉ một số văn bản được áp dụng",
                    "situation": "formal"
                }
            ],
            "relatedTerms": ["영사인증", "헤이그협약", "외교부인증", "국제문서"]
        },
        {
            "slug": "sa-bon-dae-jo",
            "korean": "사본대조",
            "vietnamese": "Đối chiếu bản sao",
            "hanja": "寫本對照",
            "hanjaReading": "寫(베낄 사) + 本(근본 본) + 對(대할 대) + 照(비출 조)",
            "pronunciation": "사본대조",
            "meaningKo": "사본대조(寫本對照)는 사본이 원본과 동일함을 공적 기관이 확인해주는 행위입니다. 한국에서는 주민센터나 관공서에서 원본을 제시하면 사본에 '원본과 대조하였음'이라는 확인 도장을 찍어주며, 이는 인증(Chứng thực)의 한 형태입니다. 통역 시 베트남어로는 Đối chiếu bản sao 또는 Chứng thực bản sao로 표현하며, 베트남에서도 동일한 제도가 있으나 통상 '인증(Chứng thực)'이라는 용어로 통칭합니다. 한국에서는 간단한 무료 서비스인 경우가 많지만, 베트남에서는 페이지당 수수료를 받는 경우가 일반적입니다. 특히 공문서의 사본대조는 원본 제시가 필수이며, 사본만 가지고는 사본대조를 받을 수 없다는 점을 명확히 안내해야 합니다.",
            "meaningVi": "Đối chiếu bản sao là việc cơ quan có thẩm quyền xác nhận bản sao giống hệt bản gốc. Ở Hàn Quốc, nếu xuất trình bản gốc tại văn phòng hành chính thì đóng dấu xác nhận trên bản sao. Đây là một hình thức chứng thực. Ở Việt Nam cũng có chế độ tương tự nhưng thường gọi chung là 'chứng thực'. Ở Việt Nam thường tính phí theo trang, còn Hàn Quốc nhiều trường hợp miễn phí.",
            "context": "서류 제출 시 원본 보존이 필요한 경우",
            "culturalNote": "한국에서는 주민센터에서 간단히 무료로 사본대조를 받을 수 있어 매우 편리하지만, 베트남에서는 페이지당 수수료를 내야 하고 절차도 더 까다롭습니다. 특히 두꺼운 서류의 경우 전체 페이지를 대조받으면 비용이 상당하므로, 필요한 페이지만 선택적으로 대조받는 것이 일반적입니다. 통역 시 '원본 없이는 사본대조가 불가능하다'는 점을 명확히 해야 하며, 간혹 '사본의 사본'을 대조해달라는 요청이 있는데 이는 불가능함을 설명해야 합니다.",
            "commonMistakes": [
                {
                    "mistake": "사본대조를 공증과 동일시",
                    "correction": "사본대조는 원본과의 일치만 확인, 공증은 내용의 진정성까지 증명",
                    "explanation": "사본대조는 형식적 확인이고 공증은 실질적 증명입니다"
                },
                {
                    "mistake": "원본 없이 사본만으로 사본대조 가능하다고 안내",
                    "correction": "반드시 원본을 지참해야 사본대조가 가능함을 명시",
                    "explanation": "원본 대조 없이는 사본의 진정성을 확인할 수 없습니다"
                },
                {
                    "mistake": "한국과 베트남의 사본대조 비용을 동일하게 안내",
                    "correction": "한국은 무료인 경우가 많지만 베트남은 페이지당 유료임을 설명",
                    "explanation": "양국의 수수료 체계가 다릅니다"
                }
            ],
            "examples": [
                {
                    "ko": "졸업증명서 원본을 가져오시면 사본대조해드립니다",
                    "vi": "Nếu mang bản gốc bằng tốt nghiệp thì chúng tôi sẽ đối chiếu bản sao",
                    "situation": "onsite"
                },
                {
                    "ko": "사본대조는 주민센터에서 무료로 받을 수 있습니다",
                    "vi": "Đối chiếu bản sao có thể xin miễn phí tại văn phòng hành chính",
                    "situation": "formal"
                },
                {
                    "ko": "사본만 가지고는 사본대조를 받을 수 없습니다",
                    "vi": "Chỉ có bản sao thì không thể đối chiếu được",
                    "situation": "onsite"
                }
            ],
            "relatedTerms": ["인증", "원본", "사본", "확인"]
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
    print(f"✅ Added {len(filtered)} terms (공증/인증/사서증서). Total: {len(data)}")

if __name__ == '__main__':
    main()
