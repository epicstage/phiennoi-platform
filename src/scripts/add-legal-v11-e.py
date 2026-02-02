#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""중재법/ADR 용어 추가 (v11-E)"""
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
            "slug": "trong-tai",
            "korean": "중재",
            "vietnamese": "Trọng tài",
            "hanja": "仲裁",
            "hanjaReading": "仲(가운데 중) 裁(재단할 재)",
            "pronunciation": "중재",
            "meaningKo": "분쟁 당사자가 제3자인 중재인을 선정하여 그의 판정으로 분쟁을 해결하는 제도입니다. 통역 시 중재는 소송과 달리 비공개이며, 당사자 합의로 진행되고, 중재판정은 확정판결과 동일한 효력을 가진다는 점을 명확히 해야 합니다. 베트남 중재법(Luật Trọng tài thương mại)에서도 상사중재를 인정하며, 한국과 동일하게 뉴욕협약(외국중재판정의 승인 및 집행에 관한 협약)에 가입하여 외국 중재판정을 집행할 수 있습니다. 통역 시 중재합의서 작성 방법, 중재인 선정 절차, 중재판정의 취소 사유(절차 위반, 공서양속 위반), 중재지와 준거법 선택의 중요성을 설명하고, 베트남에서는 VIAC(베트남 국제중재센터)가 주요 중재기관임을 안내해야 합니다.",
            "meaningVi": "Chế độ giải quyết tranh chấp bằng cách các bên chọn trọng tài viên (bên thứ ba) để phán quyết. Khác với tố tụng, trọng tài không công khai, tiến hành theo thỏa thuận của các bên, và phán quyết trọng tài có hiệu lực tương đương bản án xác định. Luật Trọng tài thương mại Việt Nam công nhận trọng tài thương mại. Việt Nam gia nhập Công ước New York nên có thể thi hành phán quyết trọng tài nước ngoài. Cần chú ý cách soạn thỏa thuận trọng tài, quy trình chọn trọng tài viên, lý do hủy phán quyết (vi phạm thủ tục, trái trật tự công), tầm quan trọng của việc chọn địa điểm trọng tài và luật áp dụng. VIAC (Trung tâm Trọng tài Quốc tế Việt Nam) là cơ quan trọng tài chính.",
            "context": "국제 계약, 투자 분쟁, 건설 분쟁 시",
            "culturalNote": "한국은 중재를 소송의 대안으로 적극 활용하지만, 베트남은 중재 문화가 미발달하여 기업들이 여전히 소송을 선호합니다. 베트남에서는 중재판정이 법원에서 집행 거부되는 경우가 있어 실효성이 의심되므로, 통역 시 중재지를 한국이나 싱가포르로 하는 것이 집행 가능성을 높일 수 있다고 조언해야 합니다. 베트남은 중재합의가 명확하지 않으면 법원이 중재 관할권을 부정하는 경우가 많아, 통역 시 중재조항을 계약서에 명확히 기재하고 분쟁 유형을 구체적으로 명시하도록 권장해야 합니다. 한국 기업이 베트남 기업과 중재합의를 할 때는 VIAC 규칙과 ICC 규칙의 차이를 이해하고, 중재비용 분담 방식을 사전에 합의하도록 통역사가 조력해야 합니다. 베트남에서는 중재인의 전문성이 부족한 경우가 있으므로, 통역 시 중재인 자격과 경력을 확인하도록 조언하는 것이 중요합니다.",
            "commonMistakes": [
                {
                    "mistake": "중재와 조정을 구분하지 않음",
                    "correction": "중재는 강제력 있는 판정, 조정은 합의 권고",
                    "explanation": "중재는 판정으로 종결, 조정은 당사자 합의로 종결"
                },
                {
                    "mistake": "중재판정에 불복하면 항소 가능하다고 설명",
                    "correction": "중재판정은 확정적, 항소 불가",
                    "explanation": "중재판정은 일심제로 상소 제도 없음"
                },
                {
                    "mistake": "중재합의 없이도 중재 가능하다고 설명",
                    "correction": "중재는 당사자 합의 필수, 합의 없으면 불가",
                    "explanation": "중재는 합의주의 원칙으로 중재합의 필수"
                }
            ],
            "examples": [
                {
                    "ko": "본 계약의 분쟁은 대한상사중재원의 중재규칙에 따라 해결합니다",
                    "vi": "Tranh chấp theo hợp đồng này sẽ được giải quyết theo quy tắc trọng tài của KCAB Hàn Quốc",
                    "situation": "formal"
                },
                {
                    "ko": "소송 대신 중재로 하면 빠르고 비공개로 해결돼요",
                    "vi": "Nếu dùng trọng tài thay vì tố tụng thì giải quyết nhanh và không công khai",
                    "situation": "informal"
                },
                {
                    "ko": "현장 계약서에 중재조항 넣으세요. 나중에 분쟁 시 소송보다 유리해요",
                    "vi": "Hãy bổ sung điều khoản trọng tài vào hợp đồng hiện trường. Khi có tranh chấp sau này sẽ có lợi hơn tố tụng",
                    "situation": "onsite"
                }
            ],
            "relatedTerms": ["조정", "중재판정", "중재합의", "대한상사중재원"]
        },
        {
            "slug": "thoa-thuan-trong-tai",
            "korean": "중재합의",
            "vietnamese": "Thỏa thuận trọng tài",
            "hanja": "仲裁合議",
            "hanjaReading": "仲(가운데 중) 裁(재단할 재) 合(합할 합) 議(의논할 의)",
            "pronunciation": "중재합의",
            "meaningKo": "당사자가 현재 또는 장래의 분쟁을 중재로 해결하기로 하는 합의입니다. 통역 시 중재합의는 계약서의 중재조항 또는 별도의 중재합의서로 작성되며, 서면으로 해야 유효하고, 중재합의가 있으면 법원은 소송을 각하한다는 점을 명확히 해야 합니다. 베트남 중재법에서도 'thỏa thuận trọng tài(중재합의)'는 서면 요식을 요구하며, 이메일이나 계약서 조항으로도 가능합니다. 통역 시 중재합의의 독립성(주계약 무효여도 중재합의는 유효), 중재 대상의 구체적 명시, 중재기관과 중재규칙의 선택, 중재지와 중재언어의 지정 등을 명확히 전달하고, 중재합의가 불명확하면 법원이 중재 관할을 부정할 수 있음을 경고해야 합니다.",
            "meaningVi": "Thỏa thuận giữa các bên để giải quyết tranh chấp hiện tại hoặc tương lai bằng trọng tài. Thỏa thuận trọng tài được lập thành điều khoản trong hợp đồng hoặc văn bản riêng, phải bằng văn bản mới có hiệu lực, và khi có thỏa thuận trọng tài thì tòa án phải bác đơn kiện. Luật Trọng tài Việt Nam cũng yêu cầu hình thức văn bản, có thể qua email hoặc điều khoản hợp đồng. Cần chú ý tính độc lập của thỏa thuận trọng tài (hợp đồng chính vô hiệu nhưng thỏa thuận trọng tài vẫn có hiệu lực), ghi rõ đối tượng trọng tài, chọn tổ chức trọng tài và quy tắc, chỉ định địa điểm và ngôn ngữ trọng tài. Nếu thỏa thuận không rõ ràng, tòa có thể từ chối thẩm quyền trọng tài.",
            "context": "계약 체결, 분쟁 예방, 국제 거래 시",
            "culturalNote": "한국은 계약서에 중재조항을 표준으로 삽입하지만, 베트남은 중재조항을 생략하는 경우가 많아 분쟁 시 소송으로 진행됩니다. 베트남에서는 중재합의가 모호하게 작성되어 법원이 중재 관할을 인정하지 않는 사례가 빈번하므로, 통역 시 중재조항을 명확하고 구체적으로 작성하도록 조언해야 합니다. 베트남은 중재합의에 '대한상사중재원'이나 'ICC 중재'로 명시하면 베트남 법원이 더 존중하는 경향이 있으므로, 통역 시 국제적 중재기관 선택을 권장해야 합니다. 한국 기업이 베트남 기업과 계약할 때는 중재합의서에 준거법(한국법 또는 베트남법)과 중재지(서울 또는 싱가포르)를 명시하고, 중재비용 부담 방식을 사전에 합의하도록 통역사가 조력해야 합니다. 베트남에서는 중재합의를 번역할 때 'tranh chấp phát sinh từ hoặc liên quan đến hợp đồng(계약에서 발생하거나 관련된 분쟁)'으로 넓게 표현하는 것이 분쟁 포괄 범위를 확대합니다.",
            "commonMistakes": [
                {
                    "mistake": "중재합의는 구두로 가능하다고 설명",
                    "correction": "중재합의는 반드시 서면으로 해야 유효",
                    "explanation": "중재합의는 서면 요식행위로 구두는 무효"
                },
                {
                    "mistake": "주계약 무효면 중재합의도 무효라고 설명",
                    "correction": "중재합의는 주계약과 독립, 주계약 무효여도 유효",
                    "explanation": "중재합의의 독립성 원칙"
                },
                {
                    "mistake": "중재합의 후에도 소송 제기 가능하다고 설명",
                    "correction": "중재합의 있으면 법원은 소송 각하",
                    "explanation": "중재합의는 소송 배제 효력 있음"
                }
            ],
            "examples": [
                {
                    "ko": "본 계약에서 발생하는 모든 분쟁은 서울 소재 대한상사중재원의 중재로 최종 해결한다",
                    "vi": "Mọi tranh chấp phát sinh từ hợp đồng này sẽ được giải quyết cuối cùng bằng trọng tài tại KCAB Seoul",
                    "situation": "formal"
                },
                {
                    "ko": "중재합의서에 사인하면 법원에 못 가고 중재로만 해결해야 해요",
                    "vi": "Nếu ký thỏa thuận trọng tài thì không thể kiện tòa mà chỉ giải quyết bằng trọng tài",
                    "situation": "informal"
                },
                {
                    "ko": "현장 계약서 중재조항에 VIAC 말고 ICC로 하자고 제안하세요",
                    "vi": "Trong điều khoản trọng tài của hợp đồng hiện trường, hãy đề xuất dùng ICC thay vì VIAC",
                    "situation": "onsite"
                }
            ],
            "relatedTerms": ["중재", "중재조항", "중재기관", "분쟁해결"]
        },
        {
            "slug": "phan-quyet-trong-tai",
            "korean": "중재판정",
            "vietnamese": "Phán quyết trọng tài",
            "hanja": "仲裁判定",
            "hanjaReading": "仲(가운데 중) 裁(재단할 재) 判(판단할 판) 定(정할 정)",
            "pronunciation": "중재판정",
            "meaningKo": "중재인이 분쟁에 대하여 내리는 최종 결정입니다. 통역 시 중재판정은 확정판결과 동일한 효력을 가지며, 상소할 수 없고, 법원의 집행판결을 받아 강제집행이 가능하다는 점을 명확히 해야 합니다. 베트남 중재법에서도 'phán quyết trọng tài(중재판정)'는 확정적이며, 베트남 법원에서 집행 승인을 받아 집행할 수 있습니다. 통역 시 중재판정의 취소 사유(중재합의 무효, 적법한 통지 없음, 중재 범위 초과, 중재절차 위반, 공서양속 위반)를 명확히 전달하고, 중재판정 취소는 중재지 법원에만 청구 가능하며, 취소 사유는 제한적임을 설명해야 합니다. 베트남에서는 중재판정 집행 승인 시 법원이 실체 심사를 하는 경우가 있어 집행이 지연될 수 있음을 경고해야 합니다.",
            "meaningVi": "Quyết định cuối cùng của trọng tài viên về tranh chấp. Phán quyết trọng tài có hiệu lực tương đương bản án xác định, không thể kháng cáo, và có thể thi hành cưỡng chế sau khi được tòa án cấp quyết định công nhận thi hành. Luật Trọng tài Việt Nam cũng quy định phán quyết trọng tài là chung thẩm, có thể xin tòa Việt Nam công nhận thi hành. Cần chú ý lý do hủy phán quyết (thỏa thuận trọng tài vô hiệu, không thông báo hợp pháp, vượt phạm vi trọng tài, vi phạm thủ tục, trái trật tự công). Hủy phán quyết chỉ được yêu cầu tại tòa nơi trọng tài, và lý do hủy có hạn. Tại Việt Nam, khi xin công nhận thi hành, tòa có thể xem xét nội dung nên việc thi hành có thể bị trì hoãn.",
            "context": "중재 절차 종료, 판정 집행 시",
            "culturalNote": "한국은 중재판정을 신속히 집행하지만, 베트남은 법원이 중재판정 집행을 거부하거나 지연시키는 경우가 많아 실효성이 떨어집니다. 베트남에서는 중재판정이 '공서양속'에 위반된다는 이유로 집행이 거부되는 사례가 있으며, 공서양속의 범위가 불명확하여 법원의 재량이 크므로 통역 시 이 위험을 설명해야 합니다. 베트남은 외국 중재판정(특히 한국 중재판정)을 집행할 때 베트남어 공증 번역본을 요구하고 절차가 복잡하므로, 통역 시 집행 준비에 충분한 시간을 두도록 조언해야 합니다. 한국 기업이 베트남에서 중재판정을 집행할 때는 베트남 법원에 집행 승인 신청을 해야 하며, 통역사가 신청서 작성과 번역을 지원해야 합니다. 베트남에서는 중재판정문을 분실하면 재발급이 어려우므로, 통역 시 원본을 안전하게 보관하고 공증본을 여러 부 확보하도록 조언하는 것이 중요합니다.",
            "commonMistakes": [
                {
                    "mistake": "중재판정에 불복하면 항소 가능하다고 설명",
                    "correction": "중재판정은 최종 결정으로 항소 불가",
                    "explanation": "중재는 일심제로 상소 제도 없음"
                },
                {
                    "mistake": "중재판정 취소는 어떤 법원에나 청구 가능하다고 설명",
                    "correction": "중재지 법원에만 취소 청구 가능",
                    "explanation": "중재판정 취소는 중재지국 법원의 전속 관할"
                },
                {
                    "mistake": "중재판정은 바로 집행 가능하다고 설명",
                    "correction": "법원의 집행판결 받아야 강제집행 가능",
                    "explanation": "중재판정은 집행력 없어 법원 승인 필요"
                }
            ],
            "examples": [
                {
                    "ko": "중재판정에서 피고는 원고에게 1억원을 지급하라고 판정합니다",
                    "vi": "Phán quyết trọng tài: Bị đơn phải trả cho nguyên đơn 100 triệu won",
                    "situation": "formal"
                },
                {
                    "ko": "중재판정 나오면 끝이에요. 항소 못 해요",
                    "vi": "Khi có phán quyết trọng tài là xong. Không thể kháng cáo",
                    "situation": "informal"
                },
                {
                    "ko": "현장에서 중재판정 받으면 베트남 법원에 집행승인 신청해야 해요",
                    "vi": "Khi nhận phán quyết trọng tài tại hiện trường, phải nộp đơn xin công nhận thi hành tại tòa Việt Nam",
                    "situation": "onsite"
                }
            ],
            "relatedTerms": ["중재", "집행판결", "중재판정취소", "강제집행"]
        },
        {
            "slug": "dieu-정",
            "korean": "조정",
            "vietnamese": "Điều đình",
            "hanja": "調停",
            "hanjaReading": "調(고를 조) 停(머무를 정)",
            "pronunciation": "조정",
            "meaningKo": "분쟁 당사자가 제3자인 조정인의 도움을 받아 합의로 분쟁을 해결하는 제도입니다. 통역 시 조정은 중재와 달리 강제력이 없고, 당사자 합의가 없으면 불성립되며, 조정이 성립하면 재판상 화해와 동일한 효력을 가진다는 점을 명확히 해야 합니다. 베트남 민사소송법에서도 'hòa giải(조정)' 제도를 두어 법원 조정과 법원 외 조정을 인정합니다. 통역 시 조정 신청 절차, 조정인 선정 방법, 조정 불성립 시 소송 이행, 조정 성립 시 조정조서 작성과 집행력 등을 명확히 전달하고, 베트남에서는 법원 조정이 활성화되어 있어 소송 전 조정을 권장한다는 점을 설명해야 합니다.",
            "meaningVi": "Chế độ giải quyết tranh chấp bằng cách các bên đạt được thỏa thuận với sự giúp đỡ của điều đình viên (bên thứ ba). Khác với trọng tài, điều đình không có cưỡng chế, nếu không thỏa thuận thì không thành. Khi điều đình thành, có hiệu lực như hòa giải tại tòa. Luật Tố tụng dân sự Việt Nam có chế độ hòa giải, công nhận hòa giải tại tòa và ngoài tòa. Cần chú ý thủ tục nộp đơn điều đình, cách chọn điều đình viên, khi không thành thì chuyển sang tố tụng, khi thành thì lập biên bản điều đình và có hiệu lực thi hành. Tại Việt Nam, hòa giải tại tòa phát triển nên khuyến khích hòa giải trước khi kiện.",
            "context": "민사 분쟁, 가족 분쟁, 노동 분쟁 시",
            "culturalNote": "한국은 조정을 소송 전 단계로 활용하지만, 베트남은 조정이 더욱 강조되어 법원이 직권으로 조정을 권고하는 경우가 많습니다. 베트남에서는 소송을 제기하기 전 마을 조정위원회나 지역 조정기관을 통한 조정을 시도해야 하는 경우가 있으며, 통역 시 이 절차를 설명하고 조정 불성립 확인서를 받아야 소송이 가능함을 안내해야 합니다. 베트남은 조정 문화가 발달하여 분쟁을 공개적으로 드러내는 것을 꺼리므로, 통역 시 한국 기업에게 먼저 조정을 시도하여 관계를 유지하면서 문제를 해결하도록 조언하는 것이 효과적입니다. 한국 기업이 베트남에서 조정을 신청할 때는 조정인의 중립성과 전문성을 확인하고, 조정안이 법적으로 집행 가능한지 사전에 검토하도록 통역사가 조력해야 합니다. 베트남에서는 조정조서가 공증되지 않으면 집행력이 없는 경우가 있으므로, 통역 시 조정 성립 후 반드시 공증을 받도록 권장해야 합니다.",
            "commonMistakes": [
                {
                    "mistake": "조정과 중재를 구분하지 않음",
                    "correction": "조정은 합의 권고, 중재는 강제 판정",
                    "explanation": "조정은 당사자 합의 필요, 중재는 중재인 판정"
                },
                {
                    "mistake": "조정 불성립 시 자동으로 소송 진행된다고 설명",
                    "correction": "조정 불성립 시 별도로 소송 제기해야 함",
                    "explanation": "조정 불성립은 소송 개시가 아님"
                },
                {
                    "mistake": "조정 합의는 집행력이 없다고 설명",
                    "correction": "법원 조정 성립 시 재판상 화해와 동일한 집행력",
                    "explanation": "법원 조정조서는 집행권원"
                }
            ],
            "examples": [
                {
                    "ko": "소송에 앞서 법원 조정을 신청하여 합의를 시도하겠습니다",
                    "vi": "Trước khi kiện, tôi sẽ nộp đơn điều đình tại tòa để thử thỏa thuận",
                    "situation": "formal"
                },
                {
                    "ko": "조정으로 합의하면 소송 안 해도 돼서 시간이랑 돈 아껴요",
                    "vi": "Nếu thỏa thuận bằng điều đình thì không phải kiện nên tiết kiệm thời gian và tiền",
                    "situation": "informal"
                },
                {
                    "ko": "현장 분쟁 발생 시 먼저 조정 시도하세요. 베트남은 조정 문화 강해요",
                    "vi": "Khi có tranh chấp tại hiện trường, hãy thử điều đình trước. Việt Nam có văn hóa hòa giải mạnh",
                    "situation": "onsite"
                }
            ],
            "relatedTerms": ["중재", "화해", "법원조정", "ADR"]
        },
        {
            "slug": "giai-quyet-tranh-chap-thay-the",
            "korean": "대체적 분쟁해결",
            "vietnamese": "Giải quyết tranh chấp thay thế",
            "hanja": "代替的紛爭解決",
            "hanjaReading": "代(대신할 대) 替(바꿀 체) 的(과녁 적) 紛(어지러울 분) 爭(다툴 쟁) 解(풀 해) 決(결단할 결)",
            "pronunciation": "대체적 분쟁해결",
            "meaningKo": "소송 이외의 방법으로 분쟁을 해결하는 제도를 통칭하며, ADR(Alternative Dispute Resolution)이라고도 합니다. 통역 시 ADR은 중재, 조정, 협상 등을 포함하며, 소송보다 빠르고 비용이 적게 들며 비공개로 진행된다는 장점이 있음을 명확히 해야 합니다. 베트남에서도 'giải quyết tranh chấp thay thế(ADR)'가 법적으로 인정되며, 최근 정부가 ADR을 장려하고 있습니다. 통역 시 ADR의 종류(중재, 조정, 협상, 전문가 결정), 각 방법의 장단점, 적절한 분쟁 유형, ADR 성립 시 법적 효력 등을 명확히 전달하고, 베트남에서는 외국 기업에게 ADR 사용을 권장하는 추세임을 설명해야 합니다.",
            "meaningVi": "Chế độ giải quyết tranh chấp bằng các phương pháp ngoài tố tụng, còn gọi là ADR (Alternative Dispute Resolution). ADR bao gồm trọng tài, điều đình, đàm phán, v.v., có ưu điểm nhanh hơn tố tụng, tốn ít chi phí hơn, và tiến hành không công khai. Tại Việt Nam, ADR được công nhận pháp lý và gần đây chính phủ khuyến khích sử dụng. Cần chú ý các loại ADR (trọng tài, điều đình, đàm phán, quyết định chuyên gia), ưu nhược điểm từng phương pháp, loại tranh chấp phù hợp, hiệu lực pháp lý khi ADR thành. Việt Nam có xu hướng khuyến khích doanh nghiệp nước ngoài dùng ADR.",
            "context": "계약 체결, 분쟁 예방, 국제 거래 시",
            "culturalNote": "한국은 ADR을 소송의 보완책으로 활용하지만, 베트남은 ADR이 아직 초기 단계로 인식과 활용도가 낮습니다. 베트남에서는 ADR 전문 기관이 부족하고 전문가 풀이 제한적이므로, 통역 시 한국이나 싱가포르의 ADR 기관을 활용하는 것이 효과적임을 조언해야 합니다. 베트남은 ADR 결과에 대한 신뢰도가 낮아 강제집행이 어려울 수 있으므로, 통역 시 ADR 합의서를 공증하고 법원 승인을 받도록 권장해야 합니다. 한국 기업이 베트남 기업과 ADR을 활용할 때는 ADR 방법을 계약서에 명시하고, ADR 불성립 시 후속 절차(소송 또는 중재)를 사전에 정하도록 통역사가 조력해야 합니다. 베트남에서는 ADR 비용이 명확하지 않아 분쟁이 발생할 수 있으므로, 통역 시 비용 분담을 계약서에 명확히 기재하도록 조언하는 것이 중요합니다.",
            "commonMistakes": [
                {
                    "mistake": "ADR은 법적 효력이 없다고 설명",
                    "correction": "ADR도 합의·판정 시 법적 효력 인정",
                    "explanation": "법원 승인받으면 집행 가능"
                },
                {
                    "mistake": "ADR은 중재만 의미한다고 설명",
                    "correction": "ADR은 중재, 조정, 협상 등 포괄 개념",
                    "explanation": "ADR은 소송 외 모든 분쟁해결 방법"
                },
                {
                    "mistake": "ADR은 항상 소송보다 빠르다고 설명",
                    "correction": "복잡한 사건은 ADR도 오래 걸릴 수 있음",
                    "explanation": "ADR 속도는 사건 복잡도에 따라 다름"
                }
            ],
            "examples": [
                {
                    "ko": "본 계약 분쟁은 소송 전 ADR로 해결을 시도합니다",
                    "vi": "Tranh chấp theo hợp đồng này sẽ thử giải quyết bằng ADR trước khi kiện",
                    "situation": "formal"
                },
                {
                    "ko": "ADR 쓰면 법정 안 가고 빠르게 해결할 수 있어요",
                    "vi": "Nếu dùng ADR thì không phải ra tòa và có thể giải quyết nhanh",
                    "situation": "informal"
                },
                {
                    "ko": "현장 계약서에 ADR 조항 넣으면 나중에 분쟁 시 유리해요",
                    "vi": "Nếu bổ sung điều khoản ADR vào hợp đồng hiện trường thì khi tranh chấp sau sẽ có lợi",
                    "situation": "onsite"
                }
            ],
            "relatedTerms": ["중재", "조정", "협상", "분쟁해결"]
        },
        {
            "slug": "trong-tai-vien",
            "korean": "중재인",
            "vietnamese": "Trọng tài viên",
            "hanja": "仲裁人",
            "hanjaReading": "仲(가운데 중) 裁(재단할 재) 人(사람 인)",
            "pronunciation": "중재인",
            "meaningKo": "중재판정을 하는 사람으로, 당사자가 선정하거나 중재기관이 지명합니다. 통역 시 중재인은 독립적이고 공정해야 하며, 법률·기술 전문가가 선임되고, 단독 또는 3인 합의부로 구성된다는 점을 명확히 해야 합니다. 베트남 중재법에서도 'trọng tài viên(중재인)'의 자격과 의무를 규정하며, 중재인은 공정성과 독립성을 유지해야 합니다. 통역 시 중재인 선정 방법(당사자 합의 선정, 중재기관 지명), 중재인 기피 사유(편파성, 이해관계), 중재인의 권한(증거조사, 증인신문), 중재인의 책임(고의·중과실 시 손해배상)을 명확히 전달하고, 베트남에서는 중재인의 전문성이 부족한 경우가 있으므로 경력을 확인하도록 조언해야 합니다.",
            "meaningVi": "Người ra phán quyết trọng tài, được các bên chọn hoặc tổ chức trọng tài chỉ định. Trọng tài viên phải độc lập và công bằng, thường là chuyên gia pháp lý hoặc kỹ thuật, cấu thành đơn lẻ hoặc hội đồng 3 người. Luật Trọng tài Việt Nam quy định tư cách và nghĩa vụ của trọng tài viên, phải duy trì công bằng và độc lập. Cần chú ý cách chọn trọng tài viên (các bên chọn thỏa thuận, tổ chức trọng tài chỉ định), lý do từ chối (thiên vị, lợi ích liên quan), quyền hạn của trọng tài viên (điều tra chứng cứ, thẩm vấn nhân chứng), trách nhiệm (bồi thường khi c고의 hoặc lỗi nặng). Tại Việt Nam, chuyên môn trọng tài viên có thể thiếu nên cần kiểm tra kinh nghiệm.",
            "context": "중재 절차, 중재인 선정 시",
            "culturalNote": "한국은 중재인 풀이 풍부하고 전문성이 높지만, 베트남은 중재인 수가 제한적이고 전문성이 부족한 경우가 많습니다. 베트남에서는 중재인이 법관 출신이거나 정부 관계자인 경우가 많아 독립성이 의심될 수 있으므로, 통역 시 한국 기업에게 외국인 중재인을 선임하거나 국제 중재기관의 중재인 명부를 활용하도록 조언해야 합니다. 베트남은 중재인의 편파성 문제로 기피 신청이 빈번하므로, 통역 시 중재인 선정 전 이해관계를 확인하고 공개 의무를 명확히 하도록 권장해야 합니다. 한국 기업이 베트남 중재에서 중재인을 선정할 때는 중재인의 베트남 법률 이해도와 언어 능력을 고려하고, 통역사를 동석시켜 언어 장벽을 해소하도록 조력해야 합니다. 베트남에서는 중재인 보수가 명확하지 않아 분쟁이 발생할 수 있으므로, 통역 시 중재인 보수를 계약서에 명시하도록 조언하는 것이 중요합니다.",
            "commonMistakes": [
                {
                    "mistake": "중재인은 법관과 동일하다고 설명",
                    "correction": "중재인은 사인, 법관은 공무원",
                    "explanation": "중재인은 당사자가 선정한 사적 판정자"
                },
                {
                    "mistake": "중재인은 반드시 변호사여야 한다고 설명",
                    "correction": "중재인은 법률·기술 전문가 가능",
                    "explanation": "중재인 자격은 분쟁 성격에 따라 다양"
                },
                {
                    "mistake": "중재인은 책임이 없다고 설명",
                    "correction": "중재인은 고의·중과실 시 손해배상 책임",
                    "explanation": "중재인도 공정성 위반 시 책임 부담"
                }
            ],
            "examples": [
                {
                    "ko": "양 당사자는 각 1인의 중재인을 선정하고, 제3의 중재인은 합의로 정합니다",
                    "vi": "Hai bên mỗi bên chọn 1 trọng tài viên, trọng tài viên thứ ba do thỏa thuận chung",
                    "situation": "formal"
                },
                {
                    "ko": "중재인은 양쪽 얘기 다 듣고 판정 내려요. 법관이랑 비슷해요",
                    "vi": "Trọng tài viên nghe cả hai bên rồi ra phán quyết. Giống thẩm phán",
                    "situation": "informal"
                },
                {
                    "ko": "현장 중재 시 중재인 경력 확인하고, 가능하면 한국인 중재인 넣으세요",
                    "vi": "Khi trọng tài tại hiện trường, hãy kiểm tra kinh nghiệm trọng tài viên, nếu được thì bổ sung trọng tài viên người Hàn",
                    "situation": "onsite"
                }
            ],
            "relatedTerms": ["중재", "중재판정", "중재기관", "기피신청"]
        },
        {
            "slug": "trung-tam-trong-tai",
            "korean": "중재기관",
            "vietnamese": "Trung tâm trọng tài",
            "hanja": "仲裁機關",
            "hanjaReading": "仲(가운데 중) 裁(재단할 재) 機(틀 기) 關(관문 관)",
            "pronunciation": "중재기관",
            "meaningKo": "중재를 관리하고 지원하는 기관으로, 중재 규칙을 제공하고 중재인 명부를 관리합니다. 통역 시 대표적 중재기관으로 대한상사중재원(KCAB), 국제상업회의소(ICC), 싱가포르국제중재센터(SIAC) 등이 있으며, 기관중재는 임시중재보다 신속하고 체계적이라는 점을 명확히 해야 합니다. 베트남의 주요 중재기관은 VIAC(베트남 국제중재센터)이며, 상사 분쟁에 특화되어 있습니다. 통역 시 중재기관 선택 기준(전문성, 신뢰성, 비용, 중재지), 기관중재와 임시중재의 차이, 중재규칙의 중요성, 중재기관의 역할(중재인 지명, 절차 관리, 비용 징수)을 명확히 전달하고, 한국 기업에게는 KCAB나 ICC를 권장하는 것이 효과적임을 설명해야 합니다.",
            "meaningVi": "Tổ chức quản lý và hỗ trợ trọng tài, cung cấp quy tắc trọng tài và quản lý danh sách trọng tài viên. Các tổ chức trọng tài tiêu biểu: KCAB Hàn Quốc, ICC, SIAC Singapore. Trọng tài thể chế nhanh và có hệ thống hơn trọng tài tùy nghi. Tổ chức trọng tài chính của Việt Nam là VIAC (Trung tâm Trọng tài Quốc tế Việt Nam), chuyên về tranh chấp thương mại. Cần chú ý tiêu chí chọn tổ chức (chuyên môn, uy tín, chi phí, địa điểm), sự khác biệt giữa trọng tài thể chế và tùy nghi, tầm quan trọng của quy tắc trọng tài, vai trò của tổ chức (chỉ định trọng tài viên, quản lý thủ tục, thu phí). Khuyến nghị doanh nghiệp Hàn Quốc dùng KCAB hoặc ICC hiệu quả hơn.",
            "context": "계약 체결, 중재합의 작성 시",
            "culturalNote": "한국은 KCAB을 신뢰하지만, 베트남 기업은 VIAC를 선호하므로 중재기관 선택에서 갈등이 발생할 수 있습니다. 베트남에서는 VIAC가 비용이 저렴하지만 중재인의 전문성이 부족하고 절차가 느린 경우가 있어, 통역 시 한국 기업에게 ICC나 SIAC 같은 국제 중재기관을 제안하도록 조언해야 합니다. 베트남은 중재기관의 중재규칙이 복잡하고 이해하기 어려우므로, 통역 시 중재규칙을 사전에 검토하고 불리한 조항이 있는지 확인하도록 권장해야 합니다. 한국 기업이 베트남 기업과 중재기관을 선택할 때는 중재비용, 중재 소요 기간, 중재판정의 집행 가능성을 비교하고, 통역사가 각 기관의 장단점을 설명하여 합리적 선택을 지원해야 합니다. 베트남에서는 중재기관이 없는 임시중재(ad hoc)는 절차가 불명확하여 분쟁이 발생할 수 있으므로, 통역 시 기관중재를 권장하는 것이 안전합니다.",
            "commonMistakes": [
                {
                    "mistake": "모든 중재는 중재기관을 통해야 한다고 설명",
                    "correction": "임시중재(ad hoc)도 가능, 당사자가 선택",
                    "explanation": "중재는 기관중재와 임시중재로 구분"
                },
                {
                    "mistake": "중재기관이 직접 판정을 내린다고 설명",
                    "correction": "중재인이 판정, 중재기관은 절차 지원",
                    "explanation": "중재기관은 관리 역할, 판정은 중재인"
                },
                {
                    "mistake": "중재기관은 모두 동일한 규칙을 쓴다고 설명",
                    "correction": "각 중재기관은 고유한 중재규칙 보유",
                    "explanation": "KCAB, ICC, SIAC 등 규칙이 다름"
                }
            ],
            "examples": [
                {
                    "ko": "본 계약 분쟁은 대한상사중재원의 중재규칙에 따라 해결합니다",
                    "vi": "Tranh chấp theo hợp đồng này sẽ được giải quyết theo quy tắc trọng tài của KCAB",
                    "situation": "formal"
                },
                {
                    "ko": "중재기관을 정하면 거기서 중재인도 추천해주고 절차도 도와줘요",
                    "vi": "Nếu chọn tổ chức trọng tài thì họ giới thiệu trọng tài viên và hỗ trợ thủ tục",
                    "situation": "informal"
                },
                {
                    "ko": "현장 계약서에 VIAC 말고 KCAB이나 SIAC로 중재기관 정하세요",
                    "vi": "Trong hợp đồng hiện trường, hãy chọn KCAB hoặc SIAC thay vì VIAC làm tổ chức trọng tài",
                    "situation": "onsite"
                }
            ],
            "relatedTerms": ["중재", "대한상사중재원", "ICC", "VIAC"]
        },
        {
            "slug": "cong-uoc-new-york",
            "korean": "뉴욕협약",
            "vietnamese": "Công ước New York",
            "hanja": None,
            "hanjaReading": None,
            "pronunciation": "뉴욕협약",
            "meaningKo": "외국 중재판정의 승인 및 집행에 관한 협약으로, 1958년 뉴욕에서 체결되어 '뉴욕협약'이라고 합니다. 통역 시 뉴욕협약에 가입한 국가 간에는 외국 중재판정을 상호 인정하고 집행할 수 있으며, 한국과 베트남 모두 가입국이므로 상호 중재판정 집행이 가능하다는 점을 명확히 해야 합니다. 베트남은 1995년 뉴욕협약에 가입했으며, 베트남 법원은 협약에 따라 외국 중재판정을 집행해야 합니다. 통역 시 뉴욕협약의 집행 거부 사유(중재합의 무효, 적법한 통지 없음, 중재 범위 초과, 공서양속 위반), 집행 신청 절차, 집행 기간을 명확히 전달하고, 베트남에서는 협약에도 불구하고 집행이 지연되거나 거부될 위험이 있음을 경고해야 합니다.",
            "meaningVi": "Công ước về công nhận và thi hành phán quyết trọng tài nước ngoài, ký kết tại New York năm 1958 nên gọi là Công ước New York. Các nước gia nhập có thể công nhận và thi hành lẫn nhau phán quyết trọng tài nước ngoài. Hàn Quốc và Việt Nam đều là thành viên nên có thể thi hành phán quyết trọng tài lẫn nhau. Việt Nam gia nhập năm 1995, tòa Việt Nam phải thi hành phán quyết trọng tài nước ngoài theo công ước. Cần chú ý lý do từ chối thi hành (thỏa thuận trọng tài vô hiệu, không thông báo hợp pháp, vượt phạm vi, trái trật tự công), thủ tục nộp đơn thi hành, thời hạn. Tại Việt Nam, dù có công ước nhưng vẫn có rủi ro thi hành bị trì hoãn hoặc từ chối.",
            "context": "국제 중재, 외국 판정 집행 시",
            "culturalNote": "한국은 뉴욕협약을 충실히 이행하지만, 베트남은 협약 가입국임에도 외국 중재판정 집행을 자주 거부하여 실효성이 떨어집니다. 베트남에서는 '공서양속 위반'을 이유로 집행을 거부하는 경우가 많으며, 공서양속의 범위가 불명확하여 법원의 재량이 크므로 통역 시 이 위험을 명확히 설명해야 합니다. 베트남은 외국 중재판정 집행 신청 시 베트남어 공증 번역본과 함께 중재판정문 원본을 요구하므로, 통역 시 서류 준비에 충분한 시간을 두도록 조언해야 합니다. 한국 기업이 베트남에서 한국 중재판정을 집행할 때는 베트남 변호사를 선임하여 집행 절차를 진행하고, 통역사가 법원 출석 시 통역을 지원해야 합니다. 베트남에서는 집행 승인이 거부되면 재신청이 어려우므로, 통역 시 첫 신청에서 완벽한 서류를 준비하고 법원 심문에 철저히 대응하도록 조언하는 것이 중요합니다.",
            "commonMistakes": [
                {
                    "mistake": "뉴욕협약은 중재합의에 관한 협약이라고 설명",
                    "correction": "뉴욕협약은 외국 중재판정의 집행에 관한 협약",
                    "explanation": "중재합의 아니라 판정 집행이 핵심"
                },
                {
                    "mistake": "협약 가입국이면 무조건 집행된다고 설명",
                    "correction": "협약에도 집행 거부 사유 있음, 공서양속 등",
                    "explanation": "협약은 원칙 집행이나 예외 사유 존재"
                },
                {
                    "mistake": "베트남은 뉴욕협약 미가입국이라고 설명",
                    "correction": "베트남은 1995년 가입, 한국은 1973년 가입",
                    "explanation": "양국 모두 협약 가입국"
                }
            ],
            "examples": [
                {
                    "ko": "한국 중재판정은 뉴욕협약에 따라 베트남에서 집행 가능합니다",
                    "vi": "Phán quyết trọng tài Hàn Quốc có thể thi hành tại Việt Nam theo Công ước New York",
                    "situation": "formal"
                },
                {
                    "ko": "뉴욕협약 덕분에 외국 중재판정도 집행할 수 있어요",
                    "vi": "Nhờ Công ước New York mà có thể thi hành phán quyết trọng tài nước ngoài",
                    "situation": "informal"
                },
                {
                    "ko": "현장에서 한국 중재판정 집행 시 뉴욕협약 근거로 신청하세요",
                    "vi": "Khi thi hành phán quyết trọng tài Hàn Quốc tại hiện trường, hãy nộp đơn dựa trên Công ước New York",
                    "situation": "onsite"
                }
            ],
            "relatedTerms": ["중재판정", "외국판정집행", "중재", "국제협약"]
        },
        {
            "slug": "thoa-thuan-dam-phan",
            "korean": "협상",
            "vietnamese": "Thỏa thuận đàm phán",
            "hanja": "協商",
            "hanjaReading": "協(화합할 협) 商(장사 상)",
            "pronunciation": "협상",
            "meaningKo": "분쟁 당사자가 직접 대화하여 합의로 문제를 해결하는 방법입니다. 통역 시 협상은 제3자 개입 없이 당사자 간 자율적으로 진행되며, 비용이 가장 적게 들고 신속하며 관계 유지에 유리하다는 점을 명확히 해야 합니다. 베트남 기업 문화에서는 협상이 매우 중요하며, 직접 대면하여 문제를 해결하는 것을 선호합니다. 통역 시 협상 전략(양보와 타협, BATNA 준비), 협상 합의서 작성 방법, 합의 불이행 시 대응 방안(조정·중재·소송 전환), 협상 과정의 기록 보존을 명확히 전달하고, 베트남에서는 협상 시 감정 조절과 체면 유지가 중요하므로 문화적 배려를 강조해야 합니다.",
            "meaningVi": "Phương pháp giải quyết vấn đề bằng cách các bên tranh chấp trực tiếp đối thoại và thỏa thuận. Đàm phán tiến hành tự nguyện giữa các bên không có bên thứ ba, tốn ít chi phí nhất, nhanh, và có lợi cho duy trì quan hệ. Trong văn hóa doanh nghiệp Việt Nam, đàm phán rất quan trọng và ưu tiên gặp trực tiếp để giải quyết. Cần chú ý chiến lược đàm phán (nhượng bộ và타협, chuẩn bị BATNA), cách lập văn bản thỏa thuận, phương án đối phó khi không thực hiện thỏa thuận (chuyển sang điều đình, trọng tài, tố tụng), lưu giữ hồ sơ quá trình đàm phán. Tại Việt Nam, khi đàm phán cần kiểm soát cảm xúc và giữ thể diện nên phải chú ý văn hóa.",
            "context": "분쟁 초기, 계약 협상, 관계 회복 시",
            "culturalNote": "한국은 협상을 논리적·효율적으로 진행하지만, 베트남은 협상 시 관계와 체면을 중시하여 시간이 오래 걸리는 경향이 있습니다. 베트남에서는 협상 중 직접적인 거절이나 비판을 피하고 우회적으로 표현하므로, 통역 시 한국 기업에게 베트남의 '하이 컨텍스트' 의사소통 방식을 설명하고 상대방의 진의를 파악하도록 조언해야 합니다. 베트남은 협상 합의서를 구두로만 하고 서면화하지 않는 경우가 많아 나중에 분쟁이 발생하므로, 통역 시 협상 결과를 반드시 서면으로 작성하고 양측이 서명하도록 권장해야 합니다. 한국 기업이 베트남 기업과 협상할 때는 초기에 과도한 양보를 하면 나중에 불리할 수 있으므로, 통역 시 협상 전략을 사전에 준비하고 BATNA(협상 결렬 시 최선의 대안)를 명확히 하도록 조력해야 합니다. 베트남에서는 협상 시 식사나 차를 함께 하며 친분을 쌓는 것이 중요하므로, 통역 시 협상 외 시간을 활용하여 관계를 강화하도록 조언하는 것이 효과적입니다.",
            "commonMistakes": [
                {
                    "mistake": "협상과 조정을 구분하지 않음",
                    "correction": "협상은 당사자 직접, 조정은 제3자 개입",
                    "explanation": "협상은 양자 대화, 조정은 조정인 도움"
                },
                {
                    "mistake": "협상 합의는 법적 효력이 없다고 설명",
                    "correction": "서면 합의서는 계약으로 법적 효력 있음",
                    "explanation": "협상 결과를 서면화하면 집행 가능"
                },
                {
                    "mistake": "협상은 항상 성공한다고 설명",
                    "correction": "협상 결렬 시 조정·중재·소송 전환 필요",
                    "explanation": "협상 실패 시 다른 분쟁해결 수단 필요"
                }
            ],
            "examples": [
                {
                    "ko": "소송 전 직접 협상으로 원만히 합의하여 분쟁을 종결하겠습니다",
                    "vi": "Trước khi kiện, sẽ đàm phán trực tiếp để thỏa thuận hòa bình và kết thúc tranh chấp",
                    "situation": "formal"
                },
                {
                    "ko": "협상으로 서로 양보하면 법원 안 가고 해결할 수 있어요",
                    "vi": "Nếu đàm phán và nhượng bộ nhau thì không phải ra tòa mà giải quyết được",
                    "situation": "informal"
                },
                {
                    "ko": "현장 분쟁 발생 시 먼저 협상 시도하세요. 베트남은 관계 중시해요",
                    "vi": "Khi có tranh chấp tại hiện trường, hãy thử đàm phán trước. Việt Nam coi trọng quan hệ",
                    "situation": "onsite"
                }
            ],
            "relatedTerms": ["조정", "ADR", "분쟁해결", "합의"]
        },
        {
            "slug": "quyet-dinh-chuyen-gia",
            "korean": "전문가결정",
            "vietnamese": "Quyết định chuyên gia",
            "hanja": "專門家決定",
            "hanjaReading": "專(오로지 전) 門(문 문) 家(집 가) 決(결단할 결) 定(정할 정)",
            "pronunciation": "전문가결정",
            "meaningKo": "기술적·전문적 분쟁을 해당 분야 전문가가 판단하여 해결하는 제도입니다. 통역 시 전문가결정은 건설, IT, 의료 등 기술 분쟁에 적합하며, 신속하고 비용이 적게 들지만 법적 구속력이 약하다는 점을 명확히 해야 합니다. 베트남에서는 'quyết định chuyên gia(전문가결정)'가 법적으로 명확히 규정되지 않았으나, 실무상 건설·엔지니어링 분쟁에서 활용됩니다. 통역 시 전문가 선정 방법, 전문가의 권한과 책임, 전문가 의견의 법적 효력(권고적 또는 구속적), 전문가결정 불복 시 소송·중재 전환 가능성을 명확히 전달하고, 계약서에 전문가결정 조항을 삽입하여 절차를 명확히 하도록 조언해야 합니다.",
            "meaningVi": "Chế độ giải quyết tranh chấp kỹ thuật hoặc chuyên môn bằng cách chuyên gia trong lĩnh vực đó phán đoán. Quyết định chuyên gia phù hợp với tranh chấp kỹ thuật như xây dựng, IT, y tế, nhanh và tốn ít chi phí nhưng ràng buộc pháp lý yếu. Tại Việt Nam, quyết định chuyên gia chưa được quy định rõ ràng nhưng thực tế dùng trong tranh chấp xây dựng, kỹ thuật. Cần chú ý cách chọn chuyên gia, quyền hạn và trách nhiệm, hiệu lực pháp lý của ý kiến chuyên gia (khuyến nghị hay ràng buộc), khả năng chuyển sang tố tụng/trọng tài khi không phục. Nên bổ sung điều khoản quyết định chuyên gia vào hợp đồng để làm rõ thủ tục.",
            "context": "건설 분쟁, 기술 분쟁, 품질 분쟁 시",
            "culturalNote": "한국은 전문가결정을 건설 분쟁에서 자주 활용하지만, 베트남은 전문가결정 제도가 미발달하여 법적 근거가 불명확합니다. 베트남에서는 전문가 의견이 법원에서 증거로만 사용되고 구속력이 없는 경우가 많아, 통역 시 전문가결정을 활용할 때는 계약서에 당사자가 전문가 의견에 구속된다는 조항을 명시하도록 조언해야 합니다. 베트남은 전문가의 전문성과 독립성이 의심되는 경우가 많으므로, 통역 시 한국이나 제3국의 전문가를 선임하여 신뢰성을 높이도록 권장해야 합니다. 한국 기업이 베트남 건설 프로젝트에서 전문가결정을 활용할 때는 전문가 선정 기준과 보수를 계약서에 명시하고, 통역사가 전문가와 당사자 간 의사소통을 지원해야 합니다. 베트남에서는 전문가결정이 번복되는 경우가 많아 안정성이 떨어지므로, 통역 시 전문가결정을 최종 해결이 아닌 협상의 참고자료로 활용하는 것이 현실적임을 설명해야 합니다.",
            "commonMistakes": [
                {
                    "mistake": "전문가결정은 법적 구속력이 있다고 설명",
                    "correction": "전문가결정은 권고적, 계약으로 구속력 부여 가능",
                    "explanation": "전문가결정은 기본적으로 의견에 불과"
                },
                {
                    "mistake": "전문가결정과 중재를 구분하지 않음",
                    "correction": "중재는 법적 구속력, 전문가결정은 기술 의견",
                    "explanation": "중재는 판정, 전문가결정은 자문"
                },
                {
                    "mistake": "전문가는 반드시 변호사여야 한다고 설명",
                    "correction": "전문가는 해당 분야 기술 전문가",
                    "explanation": "전문가는 엔지니어, 건축사 등 기술자"
                }
            ],
            "examples": [
                {
                    "ko": "하자 여부는 독립적인 건축 전문가의 결정에 따릅니다",
                    "vi": "Việc có hay không có lỗi sẽ theo quyết định của chuyên gia kiến trúc độc lập",
                    "situation": "formal"
                },
                {
                    "ko": "기술 문제는 전문가한테 맡기면 빠르게 판단받을 수 있어요",
                    "vi": "Vấn đề kỹ thuật nếu giao cho chuyên gia thì có thể được phán đoán nhanh",
                    "situation": "informal"
                },
                {
                    "ko": "현장 품질 분쟁 시 한국 기술사 불러서 전문가결정 받으세요",
                    "vi": "Khi có tranh chấp chất lượng tại hiện trường, hãy mời kỹ sư Hàn Quốc để nhận quyết định chuyên gia",
                    "situation": "onsite"
                }
            ],
            "relatedTerms": ["중재", "조정", "기술자문", "건설분쟁"]
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
    print(f"Added {len(filtered)} terms. Total: {len(data)}")

if __name__ == '__main__':
    main()
