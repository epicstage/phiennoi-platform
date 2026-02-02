#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
민법/계약법 용어 추가 스크립트 (Civil Law/Contract Law - Batch A)
Tier S 품질 기준 준수
"""

import json
import os

# 파일 경로 설정
file_path = os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', 'data', 'terms', 'legal.json')

# 추가할 용어 데이터 (민법/계약법)
new_terms = [
    {
        "slug": "hop-dong-dan-su",
        "korean": "민사계약",
        "vietnamese": "hợp đồng dân sự",
        "hanja": "民事契約",
        "hanjaReading": "民(백성 민) + 事(일 사) + 契(맺을 계) + 約(약속할 약)",
        "pronunciation": "민사계약 / 호프동잔스",
        "meaningKo": "민법상 개인 간의 법률관계를 규율하는 계약으로, 상법상 상행위와 구분됩니다. 통역 시 주의할 점은 베트남에서는 'hợp đồng dân sự'와 'hợp đồng kinh tế'(경제계약)를 명확히 구분하며, 민사계약은 개인 간 거래, 경제계약은 기업 간 거래를 의미한다는 점입니다. 한국에서는 이러한 구분이 덜 엄격하므로, 계약 당사자의 성격을 먼저 확인한 후 정확한 용어를 선택해야 합니다.",
        "meaningVi": "Hợp đồng dân sự là thỏa thuận giữa các cá nhân về việc xác lập, thay đổi hoặc chấm dứt quyền, nghĩa vụ dân sự theo quy định của Bộ luật Dân sự Việt Nam. Khác với hợp đồng kinh tế (dùng cho các chủ thể kinh doanh), hợp đồng dân sự áp dụng cho các quan hệ cá nhân như mua bán, cho thuê, vay mượn giữa các cá nhân.",
        "context": "계약서 작성, 법률 상담, 분쟁 조정 시",
        "culturalNote": "베트남은 2015년 민법전에서 민사계약과 경제계약을 명확히 구분하여 규정하고 있으며, 각각 다른 법적 요건과 효력을 갖습니다. 한국은 민법과 상법으로 구분하되, 계약의 성격보다는 당사자의 지위에 따라 적용 법률이 달라집니다. 통역 시 계약 주체가 개인인지 법인인지를 먼저 확인하여 적절한 용어를 사용해야 하며, 베트남 측에서 'hợp đồng kinh tế'라고 할 경우 한국에서는 '상사계약' 또는 '기업 간 계약'으로 표현하는 것이 적절합니다.",
        "commonMistakes": [
            {
                "mistake": "모든 계약을 'hợp đồng dân sự'로 통역",
                "correction": "기업 간 계약은 'hợp đồng kinh tế' 또는 'hợp đồng thương mại' 사용",
                "explanation": "베트남법상 계약 주체에 따라 용어가 달라지므로, 당사자 확인 후 정확한 용어 선택 필요"
            },
            {
                "mistake": "'민사계약'을 단순히 'hợp đồng' (계약)으로만 통역",
                "correction": "법적 맥락에서는 반드시 'hợp đồng dân sự' 완전한 표현 사용",
                "explanation": "베트남 법률 문서에서 'dân sự' 생략 시 계약의 법적 성격이 불명확해질 수 있음"
            },
            {
                "mistake": "'민사계약'과 '사법계약'을 동일하게 통역",
                "correction": "'민사계약'은 'hợp đồng dân sự', '사법계약'은 'hợp đồng tư pháp'으로 구분",
                "explanation": "한국에서는 혼용되나 베트남에서는 다른 법적 개념으로 인식될 수 있음"
            }
        ],
        "examples": [
            {
                "ko": "이 민사계약은 양 당사자 간의 합의로 체결되었습니다.",
                "vi": "Hợp đồng dân sự này được ký kết trên cơ sở thỏa thuận giữa hai bên.",
                "situation": "formal"
            },
            {
                "ko": "민사계약 위반 시 손해배상 책임이 발생합니다.",
                "vi": "Khi vi phạm hợp đồng dân sự, sẽ phát sinh trách nhiệm bồi thường thiệt hại.",
                "situation": "formal"
            },
            {
                "ko": "개인 간 부동산 거래는 민사계약으로 처리됩니다.",
                "vi": "Giao dịch bất động sản giữa các cá nhân được xử lý theo hợp đồng dân sự.",
                "situation": "onsite"
            }
        ],
        "relatedTerms": ["계약", "민법", "계약당사자", "계약체결", "상사계약"]
    },
    {
        "slug": "quyen-so-huu",
        "korean": "소유권",
        "vietnamese": "quyền sở hữu",
        "hanja": "所有權",
        "hanjaReading": "所(바 소) + 有(있을 유) + 權(권세 권)",
        "pronunciation": "소유권 / 꾸옌서흐우",
        "meaningKo": "물건을 전면적으로 지배할 수 있는 권리로, 사용·수익·처분의 권능을 포함합니다. 통역 시 주의할 점은 베트남에서는 토지 소유권이 국가에 속하고 개인은 '사용권(quyền sử dụng đất)'만 가지므로, 부동산 관련 소유권 통역 시 반드시 '건물 소유권(quyền sở hữu nhà)'과 '토지 사용권'을 구분해야 합니다. 한국의 '토지 소유권'을 베트남어로 통역할 때 맥락을 고려하여 적절한 표현을 선택해야 합니다.",
        "meaningVi": "Quyền sở hữu là quyền được chiếm hữu, sử dụng, định đoạt tài sản theo quy định của pháp luật. Tại Việt Nam, quyền sở hữu áp dụng cho động sản và nhà ở, nhưng đất đai thuộc sở hữu toàn dân do Nhà nước đại diện, cá nhân chỉ có quyền sử dụng đất.",
        "context": "부동산 거래, 재산권 분쟁, 상속 문제 논의 시",
        "culturalNote": "베트남과 한국의 가장 큰 차이는 토지 소유권 개념입니다. 베트남에서는 모든 토지가 국가 소유이며, 개인이나 기업은 토지 사용권(quyền sử dụng đất)만 가질 수 있습니다. 반면 한국에서는 개인의 토지 소유권이 인정됩니다. 따라서 부동산 통역 시 '소유권'이라는 단어가 나오면 반드시 토지인지 건물인지 확인해야 하며, 베트남 측과 소통할 때는 'quyền sở hữu nhà và quyền sử dụng đất'(건물 소유권 및 토지 사용권)처럼 명확히 구분하여 표현해야 오해를 방지할 수 있습니다.",
        "commonMistakes": [
            {
                "mistake": "토지와 건물의 소유권을 구분하지 않고 'quyền sở hữu'로만 통역",
                "correction": "토지는 'quyền sử dụng đất', 건물은 'quyền sở hữu nhà'로 구분",
                "explanation": "베트남에서 토지는 사용권만 존재하므로, 소유권으로 통역하면 법적 오해 발생"
            },
            {
                "mistake": "'소유권 이전'을 'chuyển quyền sở hữu'로만 통역",
                "correction": "부동산의 경우 'chuyển nhượng quyền sử dụng đất' (토지), 'chuyển quyền sở hữu nhà' (건물)",
                "explanation": "베트남 부동산 거래는 토지와 건물을 별도로 처리하므로 정확한 표현 필요"
            },
            {
                "mistake": "'공동소유권'을 단순히 'quyền sở hữu chung'으로 통역",
                "correction": "맥락에 따라 'sở hữu chung' (공유) 또는 'đồng sở hữu' (합유) 구분",
                "explanation": "한국 민법의 공유와 합유 개념이 베트남에도 존재하므로 정확한 구분 필요"
            }
        ],
        "examples": [
            {
                "ko": "이 아파트의 소유권은 매수인에게 이전됩니다.",
                "vi": "Quyền sở hữu căn hộ này được chuyển cho bên mua.",
                "situation": "formal"
            },
            {
                "ko": "토지 소유권은 등기를 통해 공시됩니다.",
                "vi": "Quyền sử dụng đất được công khai thông qua đăng ký.",
                "situation": "formal"
            },
            {
                "ko": "부동산 소유권 분쟁이 발생했습니다.",
                "vi": "Đã phát sinh tranh chấp về quyền sở hữu nhà và quyền sử dụng đất.",
                "situation": "onsite"
            }
        ],
        "relatedTerms": ["점유권", "용익권", "담보권", "물권", "등기"]
    },
    {
        "slug": "nghia-vu",
        "korean": "의무",
        "vietnamese": "nghĩa vụ",
        "hanja": "義務",
        "hanjaReading": "義(옳을 의) + 務(힘쓸 무)",
        "pronunciation": "의무 / 응이아부",
        "meaningKo": "법률관계에서 특정 행위를 하거나 하지 않아야 하는 법적 구속으로, 권리와 대응하는 개념입니다. 통역 시 주의할 점은 '의무'와 '책임(trách nhiệm)'을 구분해야 한다는 것입니다. 베트남어에서 'nghĩa vụ'는 계약상 또는 법률상 해야 할 작위·부작위를 의미하며, 'trách nhiệm'은 의무 위반 시 감수해야 할 불이익을 의미합니다. 한국어에서는 두 개념이 혼용되는 경우가 많으므로, 맥락을 파악하여 정확히 구분해야 합니다.",
        "meaningVi": "Nghĩa vụ là những gì mà chủ thể phải làm hoặc không được làm theo quy định của pháp luật hoặc thỏa thuận trong hợp đồng. Nghĩa vụ luôn đi kèm với quyền lợi và là một trong những yếu tố cơ bản của quan hệ pháp luật dân sự.",
        "context": "계약서 작성, 권리·의무 설명, 법적 책임 논의 시",
        "culturalNote": "베트남 법률 체계에서는 'nghĩa vụ'(의무)와 'trách nhiệm'(책임)을 명확히 구분합니다. nghĩa vụ는 계약 또는 법률에 따라 이행해야 할 사항이고, trách nhiệm은 의무 불이행 시 부담하는 법적 결과입니다. 한국에서는 '책임'이라는 용어가 두 의미를 모두 포함하여 사용되는 경우가 많아, 통역 시 혼란이 발생할 수 있습니다. 예를 들어 '손해배상책임'은 'trách nhiệm bồi thường', '계약이행의무'는 'nghĩa vụ thực hiện hợp đồng'으로 구분해야 정확합니다.",
        "commonMistakes": [
            {
                "mistake": "'책임'과 '의무'를 모두 'nghĩa vụ'로 통역",
                "correction": "의무는 'nghĩa vụ', 책임(불이익)은 'trách nhiệm'으로 구분",
                "explanation": "베트남법에서 두 용어는 명확히 다른 법적 개념이므로 구분 필수"
            },
            {
                "mistake": "'법적 의무'를 'nghĩa vụ pháp lý'로 통역",
                "correction": "'nghĩa vụ theo quy định của pháp luật' 또는 'nghĩa vụ pháp định'",
                "explanation": "'pháp lý'는 '법률적' 의미로, 법정 의무를 표현할 때는 'pháp định' 사용"
            },
            {
                "mistake": "'의무를 다하다'를 'làm nghĩa vụ'로 직역",
                "correction": "'thực hiện nghĩa vụ' 또는 'hoàn thành nghĩa vụ'",
                "explanation": "'làm'보다는 'thực hiện'(이행하다)이 법률 용어로 적절"
            }
        ],
        "examples": [
            {
                "ko": "매도인은 물건을 인도할 의무가 있습니다.",
                "vi": "Bên bán có nghĩa vụ giao hàng.",
                "situation": "formal"
            },
            {
                "ko": "계약상 의무를 이행하지 않으면 책임을 져야 합니다.",
                "vi": "Nếu không thực hiện nghĩa vụ hợp đồng, phải chịu trách nhiệm.",
                "situation": "formal"
            },
            {
                "ko": "양 당사자의 권리와 의무를 명확히 해야 합니다.",
                "vi": "Cần làm rõ quyền lợi và nghĩa vụ của hai bên.",
                "situation": "onsite"
            }
        ],
        "relatedTerms": ["권리", "책임", "채무", "이행", "의무불이행"]
    },
    {
        "slug": "boi-thuong-thiet-hai",
        "korean": "손해배상",
        "vietnamese": "bồi thường thiệt hại",
        "hanja": "損害賠償",
        "hanjaReading": "損(덜 손) + 害(해칠 해) + 賠(갚을 배) + 償(갚을 상)",
        "pronunciation": "손해배상 / 보이투엉티엣하이",
        "meaningKo": "타인에게 가한 손해를 금전 또는 기타 방법으로 보상하는 것을 의미하며, 계약 위반이나 불법행위로 인해 발생합니다. 통역 시 주의할 점은 '손해배상'과 '위약금(tiền phạt vi phạm)'을 구분해야 한다는 것입니다. 손해배상은 실제 발생한 손해를 보전하는 것이고, 위약금은 계약에서 미리 정한 금액으로 손해 발생과 무관하게 지급됩니다. 베트남에서는 두 개념을 엄격히 구분하므로, 계약서에서 어떤 조항을 다루는지 명확히 파악해야 합니다.",
        "meaningVi": "Bồi thường thiệt hại là việc bên gây thiệt hại phải bồi hoàn cho bên bị thiệt hại bằng tiền hoặc các hình thức khác theo quy định của pháp luật. Thiệt hại có thể là tài sản, tinh thần hoặc cả hai, và được xác định dựa trên thiệt hại thực tế xảy ra.",
        "context": "계약 분쟁, 불법행위, 법적 책임 논의 시",
        "culturalNote": "베트남과 한국 모두 손해배상 제도를 가지고 있으나, 배상 범위와 산정 방식에 차이가 있습니다. 베트남은 실손해배상 원칙을 엄격히 적용하여, 실제 발생한 손해만 배상하며 징벌적 손해배상 개념이 거의 없습니다. 한국은 최근 일부 법률(하도급법, 개인정보보호법 등)에서 징벌적 손해배상을 도입했습니다. 또한 베트남에서는 정신적 손해(thiệt hại về tinh thần)를 별도로 청구할 수 있으며, 법원이 구체적 금액을 판단합니다. 통역 시 배상의 종류와 범위를 명확히 구분하여 전달해야 합니다.",
        "commonMistakes": [
            {
                "mistake": "'손해배상'과 '위약금'을 구분하지 않고 모두 'bồi thường'으로 통역",
                "correction": "손해배상은 'bồi thường thiệt hại', 위약금은 'tiền phạt vi phạm'",
                "explanation": "베트남법에서 두 개념은 법적 성격과 산정 방식이 완전히 다름"
            },
            {
                "mistake": "'정신적 손해배상'을 'bồi thường tinh thần'으로만 통역",
                "correction": "'bồi thường thiệt hại về tinh thần' (완전한 표현 사용)",
                "explanation": "법률 문서에서는 정확한 법률 용어 사용 필요"
            },
            {
                "mistake": "'배상하다'를 'đền bù'로 통역",
                "correction": "법률 맥락에서는 'bồi thường' 사용",
                "explanation": "'đền bù'는 보상의 일반적 의미로, 법적 손해배상은 'bồi thường'"
            }
        ],
        "examples": [
            {
                "ko": "계약 위반으로 인한 손해배상을 청구합니다.",
                "vi": "Yêu cầu bồi thường thiệt hại do vi phạm hợp đồng.",
                "situation": "formal"
            },
            {
                "ko": "실제 손해액을 입증해야 손해배상을 받을 수 있습니다.",
                "vi": "Phải chứng minh thiệt hại thực tế mới có thể nhận bồi thường.",
                "situation": "formal"
            },
            {
                "ko": "물질적·정신적 손해배상을 모두 청구할 수 있습니다.",
                "vi": "Có thể yêu cầu bồi thường cả thiệt hại vật chất và tinh thần.",
                "situation": "onsite"
            }
        ],
        "relatedTerms": ["위약금", "불법행위", "채무불이행", "과실", "인과관계"]
    },
    {
        "slug": "vi-pham-hop-dong",
        "korean": "계약위반",
        "vietnamese": "vi phạm hợp đồng",
        "hanja": "契約違反",
        "hanjaReading": "契(맺을 계) + 約(약속할 약) + 違(어길 위) + 反(돌이킬 반)",
        "pronunciation": "계약위반 / 비팜홉동",
        "meaningKo": "계약 당사자가 계약상 의무를 이행하지 않거나 불완전하게 이행하는 것을 의미합니다. 통역 시 주의할 점은 계약위반의 유형을 정확히 구분해야 한다는 것입니다. 베트남에서는 이행지체(chậm thực hiện), 불완전이행(thực hiện không đúng), 이행불능(không thể thực hiện)을 명확히 구분하며, 각각 다른 법적 효과가 발생합니다. 한국에서도 이러한 구분이 있으나 실무에서는 '계약위반'으로 통칭하는 경우가 많으므로, 구체적 상황을 파악하여 정확한 용어를 사용해야 합니다.",
        "meaningVi": "Vi phạm hợp đồng là hành vi không thực hiện hoặc thực hiện không đúng nghĩa vụ theo thỏa thuận trong hợp đồng. Vi phạm hợp đồng có thể dẫn đến các biện pháp khắc phục như yêu cầu tiếp tục thực hiện, giảm giá trị hợp đồng, bồi thường thiệt hại hoặc đơn phương chấm dứt hợp đồng.",
        "context": "계약 분쟁, 법적 책임 논의, 구제 조치 협의 시",
        "culturalNote": "베트남과 한국의 계약위반 처리 방식에는 문화적 차이가 있습니다. 베트남에서는 계약위반 시 먼저 협상을 통한 해결을 시도하는 것이 일반적이며, 법원 소송은 최후의 수단으로 여겨집니다. 중재(trọng tài) 제도가 활발히 활용됩니다. 한국도 협상을 선호하지만, 법적 권리 주장이 더 명확한 편입니다. 또한 베트남 민법은 불가항력(bất khả kháng) 사유를 계약위반 면책 사유로 폭넓게 인정하는 편이며, COVID-19 팬데믹 등 사회적 이슈 시 정부가 불가항력 인정 지침을 발표하기도 합니다. 통역 시 이러한 맥락을 고려해야 합니다.",
        "commonMistakes": [
            {
                "mistake": "모든 계약위반을 'vi phạm hợp đồng'으로만 통역",
                "correction": "이행지체는 'chậm thực hiện', 불완전이행은 'thực hiện không đúng'",
                "explanation": "위반 유형에 따라 구제 방법이 달라지므로 정확한 표현 필요"
            },
            {
                "mistake": "'계약해지'를 'hủy bỏ hợp đồng'으로만 통역",
                "correction": "일방적 해지는 'đơn phương chấm dứt', 합의해지는 'chấm dứt theo thỏa thuận'",
                "explanation": "해지의 근거와 방식에 따라 다른 용어 사용"
            },
            {
                "mistake": "'중대한 계약위반'을 직역하여 'vi phạm hợp đồng nghiêm trọng'",
                "correction": "'vi phạm hợp đồng căn bản' (근본적 위반)",
                "explanation": "베트남법은 'căn bản'(근본적) 개념을 사용하여 중대성 표현"
            }
        ],
        "examples": [
            {
                "ko": "매도인의 계약위반으로 인해 손해배상을 청구합니다.",
                "vi": "Yêu cầu bồi thường do bên bán vi phạm hợp đồng.",
                "situation": "formal"
            },
            {
                "ko": "납기 지연은 중대한 계약위반에 해당합니다.",
                "vi": "Chậm giao hàng được xem là vi phạm hợp đồng căn bản.",
                "situation": "formal"
            },
            {
                "ko": "불가항력으로 인한 계약위반은 면책됩니다.",
                "vi": "Vi phạm hợp đồng do sự kiện bất khả kháng được miễn trách nhiệm.",
                "situation": "onsite"
            }
        ],
        "relatedTerms": ["이행불능", "이행지체", "채무불이행", "해제", "해지"]
    },
    {
        "slug": "huy-bo-hop-dong",
        "korean": "계약해제",
        "vietnamese": "hủy bỏ hợp đồng",
        "hanja": "契約解除",
        "hanjaReading": "契(맺을 계) + 約(약속할 약) + 解(풀 해) + 除(덜 제)",
        "pronunciation": "계약해제 / 후이보홉동",
        "meaningKo": "계약이 처음부터 없었던 것과 같은 상태로 만드는 것으로, 소급효가 있습니다. 통역 시 주의할 점은 '해제(hủy bỏ)'와 '해지(chấm dứt)'를 명확히 구분해야 한다는 것입니다. 해제는 계약을 소급적으로 무효화하여 원상회복을 원칙으로 하지만, 해지는 장래에 향한 효력만 소멸시킵니다. 베트남에서는 'hủy bỏ'가 해제 개념에 가깝고, 'chấm dứt'가 해지에 해당하므로, 한국법상 효과를 정확히 파악하여 적절한 용어를 선택해야 합니다.",
        "meaningVi": "Hủy bỏ hợp đồng là việc làm cho hợp đồng không có hiệu lực từ đầu, đồng nghĩa với việc các bên phải hoàn trả cho nhau những gì đã nhận. Hủy bỏ thường áp dụng khi có sự vi phạm nghiêm trọng hoặc khi hợp đồng bị vô hiệu do thiếu điều kiện hợp lệ.",
        "context": "계약 분쟁, 원상회복 협의, 법적 구제 논의 시",
        "culturalNote": "베트남과 한국의 계약 종료 개념에는 미묘한 차이가 있습니다. 한국 민법은 '해제'(소급효)와 '해지'(장래효)를 명확히 구분하며, 계약의 종류와 위반 내용에 따라 적용이 달라집니다. 베트남 민법은 'hủy bỏ hợp đồng'(계약 무효화/취소), 'đơn phương chấm dứt'(일방적 종료), 'chấm dứt theo thỏa thuận'(합의 종료)로 구분합니다. 'hủy bỏ'는 주로 사기, 강박, 중대한 하자 등의 경우에 적용되며 소급효가 있습니다. 통역 시 한국의 '해제' 사유가 베트남에서 어떤 범주에 해당하는지 판단하여 정확한 용어를 사용해야 하며, 필요시 '원상회복(hoàn trả hiện trạng ban đầu)'을 추가 설명하는 것이 좋습니다.",
        "commonMistakes": [
            {
                "mistake": "'해제'와 '해지'를 모두 'hủy bỏ hợp đồng'으로 통역",
                "correction": "해제는 'hủy bỏ' (소급효), 해지는 'chấm dứt' (장래효)",
                "explanation": "법적 효과가 다르므로 정확한 구분 필수"
            },
            {
                "mistake": "'계약해제권'을 'quyền hủy bỏ hợp đồng'으로만 통역",
                "correction": "'quyền đơn phương chấm dứt hợp đồng' 또는 'quyền hủy bỏ'",
                "explanation": "베트남에서는 일방적 종료권 개념으로 이해되는 경우가 많음"
            },
            {
                "mistake": "'원상회복'을 'phục hồi nguyên trạng'으로 통역",
                "correction": "'hoàn trả hiện trạng ban đầu' 또는 'hoàn trả lẫn nhau'",
                "explanation": "계약법에서는 상호 반환의 의미로 'hoàn trả' 사용"
            }
        ],
        "examples": [
            {
                "ko": "중대한 하자로 인해 계약을 해제합니다.",
                "vi": "Hủy bỏ hợp đồng do có khuyết tật nghiêm trọng.",
                "situation": "formal"
            },
            {
                "ko": "계약 해제 시 양 당사자는 원상회복 의무가 있습니다.",
                "vi": "Khi hủy bỏ hợp đồng, hai bên có nghĩa vụ hoàn trả lẫn nhau.",
                "situation": "formal"
            },
            {
                "ko": "사기로 체결된 계약은 해제할 수 있습니다.",
                "vi": "Hợp đồng ký kết do lừa dối có thể bị hủy bỏ.",
                "situation": "onsite"
            }
        ],
        "relatedTerms": ["해지", "원상회복", "계약무효", "취소", "철회"]
    },
    {
        "slug": "thoi-hieu",
        "korean": "소멸시효",
        "vietnamese": "thời hiệu",
        "hanja": "消滅時效",
        "hanjaReading": "消(사라질 소) + 滅(꺼질 멸) + 時(때 시) + 效(효과 효)",
        "pronunciation": "소멸시효 / 토이히에우",
        "meaningKo": "일정 기간 동안 권리를 행사하지 않으면 그 권리가 소멸하는 제도입니다. 통역 시 주의할 점은 베트남에서는 'thời hiệu'가 소멸시효와 제척기간 개념을 모두 포함하므로, 한국법상 구분이 필요한 경우 추가 설명이 필요합니다. 또한 시효 기간이 양국 간 차이가 있으므로(한국 일반채권 10년, 베트남 3년), 구체적 사안에서 적용 기간을 명확히 해야 합니다. 시효 중단과 정지 사유도 양국 법이 다르므로 주의가 필요합니다.",
        "meaningVi": "Thời hiệu là khoảng thời gian mà pháp luật quy định để bảo vệ quyền, lợi ích hợp pháp của cá nhân, tổ chức. Sau khi hết thời hiệu, đương sự không còn quyền khởi kiện để bảo vệ quyền lợi của mình. Thời hiệu áp dụng cho nhiều loại quyền như quyền yêu cầu bồi thường, quyền khởi kiện hủy hợp đồng, quyền yêu cầu thi hành án.",
        "context": "소송 제기, 권리 행사, 법적 기한 논의 시",
        "culturalNote": "베트남과 한국의 시효 제도는 기본 개념은 유사하나 세부 사항에서 차이가 있습니다. 한국은 일반 채권의 소멸시효가 10년이지만, 베트남은 민사 관계의 일반 시효가 3년으로 훨씬 짧습니다. 또한 베트남은 'thời hiệu khởi kiện'(소제기 시효)라는 개념을 사용하며, 시효가 완성되면 법원이 청구를 각하합니다. 한국은 소멸시효 완성 후에도 소송은 가능하나 상대방이 시효 항변을 하면 패소합니다. 시효 중단 사유도 다른데, 베트남은 소 제기, 조정 신청 등으로 중단되며, 중단 후 새로운 시효가 진행됩니다. 통역 시 이러한 차이를 고려하여 정확히 전달해야 합니다.",
        "commonMistakes": [
            {
                "mistake": "'소멸시효'와 '제척기간'을 모두 'thời hiệu'로 통역",
                "correction": "소멸시효는 'thời hiệu', 제척기간은 'thời hạn' 또는 'thời hạn loại trừ'",
                "explanation": "한국법의 구분 개념을 베트남법에 정확히 대응시키기 위해 추가 설명 필요"
            },
            {
                "mistake": "'시효 중단'을 'gián đoạn thời hiệu'로 통역",
                "correction": "'tạm đình chỉ thời hiệu' (정지) 또는 'tái tính thời hiệu' (중단)",
                "explanation": "베트남은 중단과 정지 개념이 다르게 표현되므로 맥락 파악 필요"
            },
            {
                "mistake": "시효 기간을 한국 기준(10년)으로 통역",
                "correction": "베트남 기준(3년)임을 명확히 하거나 '한국법상 10년'으로 한정",
                "explanation": "양국 시효 기간이 다르므로 혼동 방지 필요"
            }
        ],
        "examples": [
            {
                "ko": "손해배상 청구권은 3년의 소멸시효가 적용됩니다.",
                "vi": "Quyền yêu cầu bồi thường thiệt hại có thời hiệu 3 năm.",
                "situation": "formal"
            },
            {
                "ko": "소 제기로 소멸시효가 중단됩니다.",
                "vi": "Việc khởi kiện làm tạm đình chỉ thời hiệu.",
                "situation": "formal"
            },
            {
                "ko": "시효가 완성되어 권리를 행사할 수 없습니다.",
                "vi": "Đã hết thời hiệu nên không thể thực hiện quyền.",
                "situation": "onsite"
            }
        ],
        "relatedTerms": ["제척기간", "시효중단", "시효정지", "권리행사", "채권"]
    },
    {
        "slug": "the-chap",
        "korean": "저당",
        "vietnamese": "thế chấp",
        "hanja": "抵當",
        "hanjaReading": "抵(막을 저) + 當(마땅할 당)",
        "pronunciation": "저당 / 테찹",
        "meaningKo": "채무 이행을 담보하기 위해 채무자 또는 제3자가 부동산 등에 설정하는 담보물권입니다. 통역 시 주의할 점은 한국의 '저당권(근저당권 포함)'과 베트남의 'thế chấp'(저당/질권), 'cầm cố'(전당) 개념을 정확히 구분해야 한다는 것입니다. 베트남에서 부동산은 주로 'thế chấp'로 담보하며, 동산은 'cầm cố'를 사용하는 경우가 많습니다. 또한 베트남은 토지 사용권과 건물 소유권을 함께 저당해야 하므로, 저당권 설정 대상을 명확히 해야 합니다.",
        "meaningVi": "Thế chấp là việc bên thế chấp dùng tài sản để đảm bảo thực hiện nghĩa vụ đối với bên nhận thế chấp. Tài sản thế chấp có thể là bất động sản (đất, nhà), động sản hoặc quyền sử dụng đất. Khi nghĩa vụ không được thực hiện, bên nhận thế chấp có quyền xử lý tài sản thế chấp để thu hồi nợ.",
        "context": "대출, 부동산 거래, 담보 설정 논의 시",
        "culturalNote": "베트남과 한국의 저당 제도는 유사하나 세부적으로 차이가 있습니다. 한국은 저당권 설정 시 점유를 이전하지 않고 등기만으로 효력이 발생하며, 근저당권 제도를 통해 계속적 거래의 담보가 가능합니다. 베트nam은 'thế chấp bất động sản'(부동산 저당) 시 점유 이전 없이 등기하며, 저당권 등록(đăng ký thế chấp)이 대항 요건입니다. 중요한 차이는 베트남에서 토지 사용권과 건물 소유권이 별도 재산이므로, 대출 시 둘 다 저당해야 완전한 담보가 된다는 점입니다. 또한 베트남은 동산 저당(thế chấp động sản)도 가능하나 실무에서는 'cầm cố'(점유 이전)를 선호하는 경우가 많습니다.",
        "commonMistakes": [
            {
                "mistake": "'저당'과 '질권'을 구분하지 않고 'thế chấp'로 통역",
                "correction": "저당(점유 유지)은 'thế chấp', 질권(점유 이전)은 'cầm cố'",
                "explanation": "베트남에서는 점유 이전 여부에 따라 다른 용어 사용"
            },
            {
                "mistake": "'근저당권'을 단순히 'quyền thế chấp'로 통역",
                "correction": "'quyền thế chấp tối đa' 또는 'quyền thế chấp cho nhiều nghĩa vụ'",
                "explanation": "베트남에 정확히 대응하는 개념이 없으므로 설명적 표현 필요"
            },
            {
                "mistake": "'저당권 설정'을 'thiết lập quyền thế chấp'으로 통역",
                "correction": "'đăng ký thế chấp' (저당 등록)",
                "explanation": "베트남에서는 등록(đăng ký)이라는 표현을 공식적으로 사용"
            }
        ],
        "examples": [
            {
                "ko": "부동산을 저당으로 제공하여 대출을 받았습니다.",
                "vi": "Đã vay tiền bằng cách thế chấp bất động sản.",
                "situation": "formal"
            },
            {
                "ko": "토지 사용권과 건물 소유권을 함께 저당해야 합니다.",
                "vi": "Phải thế chấp cả quyền sử dụng đất và quyền sở hữu nhà.",
                "situation": "formal"
            },
            {
                "ko": "저당권 실행을 통해 채권을 회수하겠습니다.",
                "vi": "Sẽ thu hồi nợ thông qua việc xử lý tài sản thế chấp.",
                "situation": "onsite"
            }
        ],
        "relatedTerms": ["담보", "질권", "근저당권", "저당권실행", "경매"]
    },
    {
        "slug": "bao-lanh",
        "korean": "보증",
        "vietnamese": "bảo lãnh",
        "hanja": "保證",
        "hanjaReading": "保(지킬 보) + 證(증거 증)",
        "pronunciation": "보증 / 바오란",
        "meaningKo": "주채무자가 채무를 이행하지 않을 경우 보증인이 그 채무를 이행할 것을 약정하는 것입니다. 통역 시 주의할 점은 '보증(bảo lãnh)'과 '연대보증(liên đới bảo lãnh)'을 구분해야 한다는 것입니다. 단순보증은 보충성이 있어 주채무자에게 먼저 청구해야 하지만, 연대보증은 채권자가 주채무자와 보증인 중 누구에게든 청구할 수 있습니다. 베트남에서는 연대보증이 일반적이며, 단순보증은 명시적으로 합의해야 인정됩니다.",
        "meaningVi": "Bảo lãnh là cam kết của người bảo lãnh với chủ nợ rằng nếu con nợ không thực hiện nghĩa vụ thì người bảo lãnh sẽ thực hiện thay. Bảo lãnh có thể là bảo lãnh đơn thuần hoặc bảo lãnh liên đới, trong đó bảo lãnh liên đới thường được sử dụng vì chủ nợ có thể yêu cầu người bảo lãnh thực hiện mà không cần phải yêu cầu con nợ trước.",
        "context": "대출, 계약 보증, 신용장 발행 시",
        "culturalNote": "베트남과 한국의 보증 제도는 기본 개념은 유사하나 실무 관행에 차이가 있습니다. 한국에서는 개인 보증, 특히 연대보증이 과거 남용되어 사회 문제가 되었고, 현재는 한정 보증을 원칙으로 하는 법개정이 이루어졌습니다. 베트남에서는 여전히 개인 보증(bảo lãnh cá nhân)이 활발히 이용되며, 특히 가족이나 친지 간 보증이 흔합니다. 기업 거래에서는 은행 보증(bảo lãnh ngân hàng)이 선호됩니다. 또한 베트남에서는 보증 계약이 서면으로 체결되어야 효력이 있으며(한국도 원칙적으로 동일), 보증 기간과 한도를 명확히 해야 합니다. 통역 시 보증의 종류와 범위를 정확히 전달하는 것이 중요합니다.",
        "commonMistakes": [
            {
                "mistake": "'보증'과 '연대보증'을 구분하지 않고 'bảo lãnh'로만 통역",
                "correction": "단순보증은 'bảo lãnh', 연대보증은 'bảo lãnh liên đới'",
                "explanation": "법적 책임 범위가 다르므로 명확한 구분 필수"
            },
            {
                "mistake": "'보증인'을 'người bảo đảm'으로 통역",
                "correction": "'người bảo lãnh' (보증인) 사용",
                "explanation": "'bảo đảm'은 담보의 의미, 보증 계약의 당사자는 'người bảo lãnh'"
            },
            {
                "mistake": "'한정보증'을 직역하여 'bảo lãnh giới hạn'",
                "correction": "'bảo lãnh có điều kiện' 또는 'bảo lãnh theo giới hạn quy định'",
                "explanation": "베트남에서는 조건부 보증 또는 한도 명시 보증으로 표현"
            }
        ],
        "examples": [
            {
                "ko": "은행이 지급을 보증하는 서류를 발급했습니다.",
                "vi": "Ngân hàng đã phát hành thư bảo lãnh thanh toán.",
                "situation": "formal"
            },
            {
                "ko": "연대보증인은 주채무자와 동일한 책임을 집니다.",
                "vi": "Người bảo lãnh liên đới chịu trách nhiệm như con nợ chính.",
                "situation": "formal"
            },
            {
                "ko": "보증 한도는 1억 원으로 합니다.",
                "vi": "Hạn mức bảo lãnh là 100 triệu won.",
                "situation": "onsite"
            }
        ],
        "relatedTerms": ["연대보증", "보증인", "구상권", "채무", "신용장"]
    },
    {
        "slug": "uy-quyen",
        "korean": "위임",
        "vietnamese": "ủy quyền",
        "hanja": "委任",
        "hanjaReading": "委(맡길 위) + 任(맡길 임)",
        "pronunciation": "위임 / 위꾸옌",
        "meaningKo": "당사자 일방이 상대방에 대하여 사무의 처리를 위탁하고 상대방이 이를 승낙함으로써 성립하는 계약입니다. 통역 시 주의할 점은 '위임(ủy quyền)'과 '대리(đại diện)'의 개념을 구분해야 한다는 것입니다. 위임은 내부 관계(위임인과 수임인 간)이고, 대리는 외부 관계(본인-대리인-상대방)입니다. 베트남에서는 'ủy quyền'이 두 개념을 포괄하는 경우가 많으므로, 법률 문서에서는 '위임장(giấy ủy quyền)' 또는 '대리권 수여'인지 명확히 해야 합니다.",
        "meaningVi": "Ủy quyền là việc một bên (bên ủy quyền) giao cho bên kia (bên nhận ủy quyền) thực hiện một hoặc nhiều công việc nhất định thay mặt mình. Ủy quyền phải được thể hiện bằng văn bản (giấy ủy quyền) và có thể thu hồi bất cứ lúc nào trừ khi có thỏa thuận khác.",
        "context": "법률 대리, 권한 위임, 위임장 작성 시",
        "culturalNote": "베트남과 한국의 위임 제도는 비슷하나 실무 관행에 차이가 있습니다. 베트남에서는 위임장(giấy ủy quyền)이 매우 광범위하게 사용되며, 공증(công chứng) 또는 인증(chứng thực)을 받는 것이 일반적입니다. 특히 부동산 거래, 기업 대표, 법적 절차 등에서 위임장이 필수입니다. 한국도 위임장을 사용하지만, 인감증명서와 함께 제출하는 형태가 많습니다. 베트남은 위임 사항을 구체적으로 명시해야 하며(특정 위임 원칙), 포괄 위임은 제한적으로만 인정됩니다. 또한 베트남에서는 위임장에 유효기간을 명시하는 것이 일반적이며, 기간 만료 후에는 자동으로 효력을 상실합니다. 통역 시 위임의 범위와 기간을 명확히 확인해야 합니다.",
        "commonMistakes": [
            {
                "mistake": "'위임'과 '대리'를 모두 'ủy quyền'으로 통역",
                "correction": "위임(계약)은 'ủy quyền', 대리(권한 행사)는 'đại diện'",
                "explanation": "내부 관계와 외부 관계를 구분하여 정확한 용어 사용"
            },
            {
                "mistake": "'위임장'을 'thư ủy quyền'으로 통역",
                "correction": "'giấy ủy quyền' (공식 문서)",
                "explanation": "'thư'는 편지, 공식 법률 문서는 'giấy' 사용"
            },
            {
                "mistake": "'포괄위임'을 'ủy quyền toàn bộ'로 직역",
                "correction": "'ủy quyền chung' 또는 'ủy quyền đầy đủ'",
                "explanation": "베트남 법률 용어에 맞는 표현 사용"
            }
        ],
        "examples": [
            {
                "ko": "부동산 매매 계약을 위임받아 체결했습니다.",
                "vi": "Đã ký hợp đồng mua bán bất động sản theo ủy quyền.",
                "situation": "formal"
            },
            {
                "ko": "위임장에는 위임 사항과 기간을 명시해야 합니다.",
                "vi": "Giấy ủy quyền phải ghi rõ nội dung và thời hạn ủy quyền.",
                "situation": "formal"
            },
            {
                "ko": "공증받은 위임장을 제출하세요.",
                "vi": "Hãy nộp giấy ủy quyền đã được công chứng.",
                "situation": "onsite"
            }
        ],
        "relatedTerms": ["대리", "위임장", "수임인", "대리권", "복대리"]
    }
]

def main():
    # JSON 파일 읽기
    print(f"📖 Reading file: {file_path}")
    with open(file_path, 'r', encoding='utf-8') as f:
        data = json.load(f)  # data는 리스트입니다!

    print(f"✅ Current terms count: {len(data)}")

    # 기존 slug 목록 생성
    existing_slugs = {term['slug'] for term in data}
    print(f"📋 Existing slugs: {len(existing_slugs)}")

    # 중복 제거 필터링
    filtered_terms = [term for term in new_terms if term['slug'] not in existing_slugs]
    duplicates = [term['slug'] for term in new_terms if term['slug'] in existing_slugs]

    if duplicates:
        print(f"⚠️  Found {len(duplicates)} duplicates (skipped): {duplicates}")

    if not filtered_terms:
        print("❌ No new terms to add (all duplicates)")
        return

    # 새 용어 추가
    data.extend(filtered_terms)
    print(f"➕ Adding {len(filtered_terms)} new terms")

    # JSON 파일 저장 (UTF-8, 들여쓰기 2칸, ensure_ascii=False)
    with open(file_path, 'w', encoding='utf-8') as f:
        json.dump(data, f, ensure_ascii=False, indent=2)

    print(f"✅ Successfully added {len(filtered_terms)} terms!")
    print(f"📊 Total terms now: {len(data)}")
    print("\n📝 Added terms:")
    for term in filtered_terms:
        print(f"   - {term['slug']}: {term['korean']} ({term['vietnamese']})")

if __name__ == "__main__":
    main()
