#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
가족법/상속법 전문용어 추가 스크립트
Theme: Family Law/Inheritance
Tier S Quality (90+ points)
"""

import json
import os

# 파일 경로 설정
file_path = os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', 'data', 'terms', 'legal.json')

# 추가할 용어 데이터 (Tier S 기준)
new_terms = [
    {
        "slug": "hon-nhan",
        "korean": "혼인",
        "vietnamese": "hôn nhân",
        "hanja": "婚姻",
        "hanjaReading": "婚(장가들 혼) + 姻(사돈 인)",
        "pronunciation": "혼인",
        "meaningKo": "법적으로 부부관계를 맺는 행위. 한국에서는 혼인신고를 통해 법률혼이 성립되며, 사실혼은 법적 보호가 제한적이다. 베트남도 법률혼 중심 체계이나, 등록하지 않은 사실혼에도 일정한 법적 권리를 인정한다. 통역 시 '결혼식'과 '법률혼 성립'을 명확히 구분해야 하며, 특히 베트남에서는 결혼식 후에도 등록을 미루는 경우가 있어 법적 지위 확인이 중요하다. 양국 모두 혼인 요건(연령, 근친혼 금지 등)을 두고 있으나 세부 규정이 다르므로 국제결혼 통역 시 각국 법률을 정확히 전달해야 한다.",
        "meaningVi": "Hành vi thiết lập quan hệ vợ chồng theo pháp luật. Ở Hàn Quốc, hôn nhân pháp lý được thành lập thông qua đăng ký kết hôn, trong khi hôn nhân sự thực có giới hạn về bảo vệ pháp lý. Việt Nam cũng tập trung vào hôn nhân pháp lý nhưng công nhận một số quyền cho hôn nhân sự thực chưa đăng ký. Cả hai nước đều có các yêu cầu về hôn nhân (tuổi, cấm kết hôn cận huyết...) nhưng chi tiết khác nhau.",
        "context": "가족법 기본 개념, 혼인신고, 국제결혼 상담",
        "culturalNote": "한국은 혼인신고 전 결혼식도 사실혼으로 인정받기 어려우나, 베트남은 공개적 부부생활 사실이 있으면 등록 없이도 일정한 권리를 보장한다. 또한 한국은 협의이혼이 상대적으로 쉬운 반면, 베트남은 이혼 절차가 더 복잡하고 조정 기간이 필수적이다. 국제결혼 통역 시 양국의 혼인 요건 차이(베트남은 18세 이상, 한국은 18세 이상이나 미성년자 혼인 시 부모 동의 필요)를 명확히 설명해야 한다.",
        "commonMistakes": [
            {
                "mistake": "결혼식을 올렸으니 법적으로 부부",
                "correction": "혼인신고를 해야 법률혼 성립",
                "explanation": "결혼식은 사회적 의식일 뿐, 법적 효력은 혼인신고로 발생"
            },
            {
                "mistake": "사실혼과 법률혼의 법적 효과가 동일하다",
                "correction": "사실혼은 상속권, 배우자 공제 등 일부 권리 제한",
                "explanation": "법률혼만이 완전한 법적 보호를 받음"
            },
            {
                "mistake": "베트남 결혼식 후 등록 안 해도 한국에서 인정",
                "correction": "양국 모두 법적 혼인신고 필요",
                "explanation": "국제결혼은 양국 법률에 따라 각각 등록해야 법적 효력 발생"
            }
        ],
        "examples": [
            {
                "ko": "혼인신고를 하지 않으면 법적 부부로 인정받을 수 없습니다.",
                "vi": "Nếu không đăng ký kết hôn, không thể được công nhận là vợ chồng hợp pháp.",
                "situation": "formal"
            },
            {
                "ko": "사실혼 관계에서는 상속권이 인정되지 않습니다.",
                "vi": "Trong quan hệ hôn nhân sự thực, quyền thừa kế không được công nhận.",
                "situation": "formal"
            },
            {
                "ko": "국제결혼 시 양국에서 모두 혼인신고를 해야 합니다.",
                "vi": "Khi kết hôn quốc tế, phải đăng ký kết hôn ở cả hai nước.",
                "situation": "onsite"
            }
        ],
        "relatedTerms": ["ly-hon", "hon-nhan-quoc-te", "dang-ky-hon-nhan", "hon-nhan-su-thuc"]
    },
    {
        "slug": "ly-hon",
        "korean": "이혼",
        "vietnamese": "ly hôn",
        "hanja": "離婚",
        "hanjaReading": "離(떠날 리) + 婚(장가들 혼)",
        "pronunciation": "이혼",
        "meaningKo": "법적 부부관계를 해소하는 행위. 한국은 협의이혼(양측 합의)과 재판이혼(법원 판결)으로 나뉘며, 협의이혼도 법원의 이혼의사 확인 절차를 거쳐야 한다. 베트남은 이혼 절차가 더 엄격하여 법원 조정 기간이 필수적이며, 합의가 안 되면 재판이혼으로 진행된다. 통역 시 '협의이혼'과 '재판이혼'의 차이를 명확히 전달해야 하며, 특히 재산분할, 양육권, 위자료 등의 부수적 문제를 함께 다루므로 관련 용어들을 정확히 이해해야 한다. 베트남은 이혼 후 자녀 양육비 지급 의무가 엄격하게 집행되는 반면, 한국은 집행 실효성이 상대적으로 낮은 편이다.",
        "meaningVi": "Hành vi chấm dứt quan hệ vợ chồng hợp pháp. Hàn Quốc chia thành ly hôn thỏa thuận (cả hai đồng ý) và ly hôn qua tòa án (phán quyết của tòa), ngay cả ly hôn thỏa thuận cũng phải qua thủ tục xác nhận ý định ly hôn tại tòa. Việt Nam có thủ tục ly hôn nghiêm ngặt hơn với thời gian hòa giải bắt buộc tại tòa, nếu không thỏa thuận được sẽ chuyển sang ly hôn qua tòa. Sau ly hôn, nghĩa vụ trả phí nuôi con ở Việt Nam được thi hành nghiêm ngặt hơn so với Hàn Quốc.",
        "context": "가족법 절차, 이혼소송, 재산분할 상담",
        "culturalNote": "한국은 협의이혼이 상대적으로 간소하고 빠르나(법원 확인 절차 후 즉시 가능), 베트남은 이혼 신청 후 의무적 조정 기간(보통 3개월)을 거쳐야 하며 합의가 안 되면 재판으로 간다. 또한 한국은 이혼 후 친권과 양육권을 분리할 수 있으나, 베트남은 양육권이 곧 친권을 포함하는 경우가 많다. 한국은 위자료 개념이 명확한 반면, 베트남은 위자료보다 '정신적 손해배상'으로 처리되며 금액도 상대적으로 낮다. 국제결혼 이혼 통역 시 양국 법률 차이를 숙지해야 한다.",
        "commonMistakes": [
            {
                "mistake": "합의만 하면 바로 이혼 가능",
                "correction": "한국도 법원 확인 절차 필수, 베트남은 조정 기간 필요",
                "explanation": "양국 모두 법원 절차를 거쳐야 법적 이혼 성립"
            },
            {
                "mistake": "이혼하면 상대 재산 절반 무조건 받는다",
                "correction": "재산분할은 기여도, 혼인 기간 등 고려하여 결정",
                "explanation": "재산분할 비율은 사건마다 다르며 법원이 판단"
            },
            {
                "mistake": "베트남 이혼 절차가 한국과 같다",
                "correction": "베트남은 조정 기간 필수, 절차가 더 복잡",
                "explanation": "양국 이혼 절차 차이를 정확히 전달해야 오해 방지"
            }
        ],
        "examples": [
            {
                "ko": "협의이혼을 하려면 법원에서 이혼의사 확인을 받아야 합니다.",
                "vi": "Để ly hôn thỏa thuận, phải nhận xác nhận ý định ly hôn tại tòa án.",
                "situation": "formal"
            },
            {
                "ko": "재산분할 비율은 혼인 기간과 기여도를 고려하여 정합니다.",
                "vi": "Tỷ lệ chia tài sản được xác định dựa trên thời gian hôn nhân và mức độ đóng góp.",
                "situation": "formal"
            },
            {
                "ko": "베트남에서는 이혼 전에 조정 기간을 반드시 거쳐야 합니다.",
                "vi": "Ở Việt Nam, bắt buộc phải qua thời gian hòa giải trước khi ly hôn.",
                "situation": "onsite"
            }
        ],
        "relatedTerms": ["tai-san-chung", "quyen-nuoi-con", "cap-duong", "hon-nhan"]
    },
    {
        "slug": "quyen-nuoi-con",
        "korean": "양육권",
        "vietnamese": "quyền nuôi con",
        "hanja": "養育權",
        "hanjaReading": "養(기를 양) + 育(기를 육) + 權(권세 권)",
        "pronunciation": "양육권",
        "meaningKo": "미성년 자녀를 직접 양육하고 보호·교육할 권리이자 의무. 한국은 친권(법률적 대리권)과 양육권(실제 양육)을 분리할 수 있으나, 베트남은 양육권이 친권을 포함하는 경우가 많다. 이혼 시 부모 합의로 정하거나 법원이 자녀의 복리를 최우선으로 판단하여 결정한다. 통역 시 '양육권'과 '친권'의 차이를 명확히 구분해야 하며, 특히 베트님에서는 양육권자가 법적 대리권도 함께 갖는 경우가 많음을 설명해야 한다. 양육권이 없는 부모도 면접교섭권(자녀와 만날 권리)을 가지며, 양육비 지급 의무는 양육권 유무와 무관하다. 베트남은 양육비 미지급 시 법적 제재가 엄격한 반면, 한국은 집행이 상대적으로 어려운 편이다.",
        "meaningVi": "Quyền và nghĩa vụ trực tiếp nuôi dưỡng, bảo vệ và giáo dục con chưa thành niên. Hàn Quốc có thể tách quyền giám hộ (đại diện pháp lý) và quyền nuôi con (chăm sóc thực tế), nhưng ở Việt Nam quyền nuôi con thường bao gồm cả quyền giám hộ. Khi ly hôn, quyền nuôi con được xác định theo thỏa thuận của cha mẹ hoặc quyết định của tòa án dựa trên lợi ích tốt nhất của con. Cha mẹ không có quyền nuôi con vẫn có quyền thăm nom con và nghĩa vụ trả phí nuôi con.",
        "context": "이혼소송, 가족법 상담, 친권 분쟁",
        "culturalNote": "한국은 전통적으로 부계 중심 사회였으나 현재는 모(母)의 양육권 인정 비율이 높아졌고, 법원도 자녀의 복리를 최우선으로 판단한다. 베트남도 과거 부계 중심이었으나 현재는 성평등적으로 판단하며, 자녀가 어릴수록 어머니에게 양육권을 주는 경향이 있다. 한국은 양육권과 친권을 분리하여 한쪽이 양육하고 다른 쪽이 법적 대리권을 갖는 경우도 있지만, 베트남은 양육권자가 친권도 함께 갖는 것이 일반적이다. 국제결혼 이혼 시 양국 법률 차이와 자녀 국적에 따라 복잡한 문제가 발생할 수 있어 정확한 통역이 필수적이다.",
        "commonMistakes": [
            {
                "mistake": "양육권과 친권이 같은 것",
                "correction": "한국은 양육권(실제 양육)과 친권(법적 대리) 분리 가능",
                "explanation": "베트남은 보통 함께 가지만 한국은 분리 가능하여 혼동 주의"
            },
            {
                "mistake": "양육권이 없으면 자녀와 만날 수 없다",
                "correction": "면접교섭권으로 자녀와 만날 권리 보장",
                "explanation": "양육권이 없어도 면접교섭권은 별도로 인정됨"
            },
            {
                "mistake": "양육비는 양육권자만 부담",
                "correction": "양육권 없는 부모도 양육비 지급 의무",
                "explanation": "양육비는 부모 공동 책임이며 양육권과 무관"
            }
        ],
        "examples": [
            {
                "ko": "양육권은 자녀의 복리를 최우선으로 고려하여 결정됩니다.",
                "vi": "Quyền nuôi con được quyết định ưu tiên hàng đầu cho lợi ích của con.",
                "situation": "formal"
            },
            {
                "ko": "양육권이 없는 부모도 면접교섭권으로 자녀를 만날 수 있습니다.",
                "vi": "Cha mẹ không có quyền nuôi con vẫn có thể gặp con thông qua quyền thăm nom.",
                "situation": "formal"
            },
            {
                "ko": "한국에서는 양육권과 친권을 분리하여 정할 수 있습니다.",
                "vi": "Ở Hàn Quốc, có thể tách quyền nuôi con và quyền giám hộ.",
                "situation": "onsite"
            }
        ],
        "relatedTerms": ["cap-duong", "ly-hon", "quyen-tham-nom", "quyen-giam-ho"]
    },
    {
        "slug": "cap-duong",
        "korean": "양육비",
        "vietnamese": "cấp dưỡng",
        "hanja": "養育費",
        "hanjaReading": "養(기를 양) + 育(기를 육) + 費(쓸 비)",
        "pronunciation": "양육비",
        "meaningKo": "미성년 자녀의 양육과 교육에 필요한 비용. 이혼 후 양육권이 없는 부모가 양육권자에게 지급하는 금전으로, 부모의 소득, 재산, 자녀 수, 자녀 나이 등을 고려하여 산정한다. 한국은 양육비 산정 기준표를 참고하며, 당사자 합의 또는 법원 결정으로 정한다. 베트남도 부모 소득과 자녀 필요에 따라 결정되며, 미지급 시 강제집행이 엄격하다. 통역 시 양육비는 양육권과 무관하게 부모 공동 책임임을 명확히 전달해야 하며, '부양료'와 혼동하지 않도록 주의해야 한다. 부양료는 배우자 간 생활비 지급이고, 양육비는 자녀를 위한 비용이다. 한국은 양육비 이행관리원을 통해 미지급 양육비 추심을 지원하지만, 실효성이 제한적인 반면, 베트남은 법적 제재가 더 강력하다.",
        "meaningVi": "Chi phí cần thiết cho việc nuôi dưỡng và giáo dục con chưa thành niên. Sau ly hôn, cha mẹ không có quyền nuôi con phải trả cho người có quyền nuôi con, được tính toán dựa trên thu nhập, tài sản của cha mẹ, số con, độ tuổi con... Hàn Quốc có bảng tiêu chuẩn tính phí nuôi con để tham khảo, được xác định theo thỏa thuận hoặc quyết định của tòa. Việt Nam cũng quyết định dựa trên thu nhập cha mẹ và nhu cầu con, khi không trả sẽ bị cưỡng chế nghiêm khắc. Phí nuôi con là trách nhiệm chung của cha mẹ, không liên quan đến quyền nuôi con.",
        "context": "이혼소송, 양육권 분쟁, 가사조정",
        "culturalNote": "한국은 양육비 산정 기준표가 있어 소득별 양육비 범위를 참고할 수 있으나, 실제 지급률이 낮고 집행이 어려운 편이다. 양육비 이행관리원이 추심을 지원하지만, 비양육 부모가 소득을 숨기거나 해외 체류 시 집행이 곤란하다. 베트남은 양육비 미지급 시 재산 압류, 출국 금지 등 법적 제재가 강력하며, 법원이 양육비를 명확히 정하고 이행을 감독한다. 국제결혼 이혼 시 양육비 집행이 복잡하므로, 양국 법률을 모두 고려한 합의가 필요하다. 또한 양육비는 자녀가 성년이 될 때까지 지급되며, 물가 상승이나 자녀 필요 증가 시 증액 청구도 가능하다.",
        "commonMistakes": [
            {
                "mistake": "양육비는 양육권자만 부담",
                "correction": "양육권 없는 부모도 양육비 지급 의무",
                "explanation": "양육비는 부모 공동 책임이며 양육권과 무관"
            },
            {
                "mistake": "양육비와 부양료가 같다",
                "correction": "양육비는 자녀 비용, 부양료는 배우자 생활비",
                "explanation": "법적 성격과 지급 대상이 완전히 다름"
            },
            {
                "mistake": "양육비를 안 주면 면접교섭권 박탈",
                "correction": "양육비 미지급과 면접교섭권은 별개 문제",
                "explanation": "자녀와 부모의 만남 권리는 금전 문제와 분리"
            }
        ],
        "examples": [
            {
                "ko": "양육비는 부모의 소득과 자녀 수를 고려하여 산정합니다.",
                "vi": "Phí nuôi con được tính toán dựa trên thu nhập của cha mẹ và số con.",
                "situation": "formal"
            },
            {
                "ko": "양육비를 지급하지 않으면 강제집행 절차가 진행될 수 있습니다.",
                "vi": "Nếu không trả phí nuôi con, có thể tiến hành thủ tục cưỡng chế.",
                "situation": "formal"
            },
            {
                "ko": "자녀가 성년이 될 때까지 양육비를 지급해야 합니다.",
                "vi": "Phải trả phí nuôi con cho đến khi con thành niên.",
                "situation": "onsite"
            }
        ],
        "relatedTerms": ["quyen-nuoi-con", "ly-hon", "bao-duong", "thi-hanh-cuong-che"]
    },
    {
        "slug": "tai-san-chung",
        "korean": "공동재산",
        "vietnamese": "tài sản chung",
        "hanja": "共同財產",
        "hanjaReading": "共(한가지 공) + 同(한가지 동) + 財(재물 재) + 產(낳을 산)",
        "pronunciation": "공동재산",
        "meaningKo": "혼인 중 부부가 공동으로 형성한 재산. 한국은 혼인 중 취득한 재산은 부부 공동 노력으로 형성된 것으로 추정하며, 이혼 시 재산분할 대상이 된다. 혼인 전 재산이나 상속·증여받은 재산은 특유재산(개인 재산)으로 분할 대상이 아니다. 베트남도 혼인 중 재산은 공동재산으로 추정하지만, 부부가 재산 약정을 할 수 있어 합의로 특유재산을 정할 수 있다. 통역 시 '공동재산'과 '특유재산'의 구분을 명확히 전달해야 하며, 특히 부동산, 주식, 사업체 등 고가 재산의 경우 취득 시점과 재원을 증명해야 분할 대상 여부가 결정됨을 설명해야 한다. 한국은 명의와 무관하게 실질적 기여도를 중시하며, 가사노동도 재산 형성 기여로 인정한다.",
        "meaningVi": "Tài sản được hình thành chung bởi vợ chồng trong thời kỳ hôn nhân. Hàn Quốc coi tài sản có được trong hôn nhân là do nỗ lực chung của vợ chồng, khi ly hôn sẽ là đối tượng chia tài sản. Tài sản trước hôn nhân hoặc thừa kế, tặng cho là tài sản riêng, không phải chia. Việt Nam cũng coi tài sản trong hôn nhân là tài sản chung, nhưng vợ chồng có thể thỏa thuận về tài sản và xác định tài sản riêng. Hàn Quốc coi trọng mức độ đóng góp thực tế bất kể tên sở hữu, và lao động nội trợ cũng được công nhận là đóng góp vào việc hình thành tài sản.",
        "context": "이혼소송, 재산분할, 가사조정",
        "culturalNote": "한국은 가사노동을 재산 형성 기여로 명확히 인정하여, 전업주부도 재산분할 시 상당한 몫을 받을 수 있다. 재산분할 비율은 보통 30~50%이지만, 혼인 기간, 기여도, 자녀 양육 부담 등을 고려하여 법원이 판단한다. 베트남은 공동재산 원칙이 강하여 명의와 무관하게 50:50 분할이 원칙이나, 기여도 차이가 명백하면 비율 조정이 가능하다. 한국은 재산분할 청구권이 이혼 후 2년 내로 제한되지만, 베트남은 시효가 더 길다. 국제결혼 이혼 시 양국에 재산이 분산되어 있으면 관할과 집행이 복잡하므로, 합의를 통한 명확한 재산분할이 중요하다.",
        "commonMistakes": [
            {
                "mistake": "명의가 남편이면 남편 재산",
                "correction": "혼인 중 취득 재산은 명의 무관하게 공동재산",
                "explanation": "실질적 기여도로 판단하며 명의는 중요하지 않음"
            },
            {
                "mistake": "전업주부는 재산분할 못 받는다",
                "correction": "가사노동도 재산 형성 기여로 인정",
                "explanation": "소득이 없어도 가사·육아 기여로 분할 권리 있음"
            },
            {
                "mistake": "공동재산은 무조건 50:50 분할",
                "correction": "기여도, 혼인 기간 등 고려하여 비율 결정",
                "explanation": "법원이 사건별로 형평성 있게 판단"
            }
        ],
        "examples": [
            {
                "ko": "혼인 중 취득한 부동산은 명의와 관계없이 공동재산입니다.",
                "vi": "Bất động sản có được trong hôn nhân là tài sản chung bất kể tên sở hữu.",
                "situation": "formal"
            },
            {
                "ko": "가사노동도 재산 형성에 기여한 것으로 인정됩니다.",
                "vi": "Lao động nội trợ cũng được công nhận là đóng góp vào hình thành tài sản.",
                "situation": "formal"
            },
            {
                "ko": "재산분할 청구는 이혼 후 2년 이내에 해야 합니다.",
                "vi": "Yêu cầu chia tài sản phải thực hiện trong vòng 2 năm sau ly hôn.",
                "situation": "onsite"
            }
        ],
        "relatedTerms": ["chia-tai-san", "ly-hon", "tai-san-rieng", "quyen-yeu-cau-chia-tai-san"]
    },
    {
        "slug": "thoi-ky-hon-nhan",
        "korean": "혼인기간",
        "vietnamese": "thời kỳ hôn nhân",
        "hanja": "婚姻期間",
        "hanjaReading": "婚(장가들 혼) + 姻(사돈 인) + 期(기약할 기) + 間(사이 간)",
        "pronunciation": "혼인기간",
        "meaningKo": "법적 혼인관계가 지속된 기간. 한국은 혼인신고일부터 이혼일까지를 기준으로 하며, 별거 기간도 포함된다. 혼인기간은 재산분할, 위자료, 연금분할 등 이혼 시 권리 산정의 중요한 기준이 된다. 일반적으로 혼인기간이 길수록 재산분할 비율이 높아지며, 국민연금 분할도 혼인기간에 비례한다. 베트남도 혼인기간을 재산분할과 양육권 판단의 중요 요소로 본다. 통역 시 '별거 기간'도 법적 혼인기간에 포함됨을 명확히 전달해야 하며, 사실혼 기간은 법적 혼인기간으로 인정되지 않음을 주의해야 한다. 다만 사실혼이 장기간 지속되고 재산 형성 기여가 명백하면 법원이 형평상 일부 권리를 인정할 수 있다.",
        "meaningVi": "Khoảng thời gian duy trì quan hệ hôn nhân hợp pháp. Hàn Quốc tính từ ngày đăng ký kết hôn đến ngày ly hôn, bao gồm cả thời gian ly thân. Thời kỳ hôn nhân là tiêu chuẩn quan trọng để xác định quyền lợi khi ly hôn như chia tài sản, bồi thường tinh thần, chia lương hưu... Nói chung, thời gian hôn nhân càng dài thì tỷ lệ chia tài sản càng cao, và việc chia lương hưu quốc gia cũng tỷ lệ với thời gian hôn nhân. Việt Nam cũng coi thời kỳ hôn nhân là yếu tố quan trọng trong việc phán xét chia tài sản và quyền nuôi con.",
        "context": "이혼소송, 재산분할, 연금분할 상담",
        "culturalNote": "한국은 혼인기간이 20년 이상이면 재산분할 비율이 높아지고, 배우자 상속권도 강화된다. 또한 국민연금 분할 청구권은 혼인기간 중 납부한 연금에 대해서만 인정되므로, 혼인기간 증명이 중요하다. 베트남은 혼인기간이 길수록 공동재산으로 인정되는 범위가 넓어지며, 자녀가 어릴수록 양육권 판단 시 혼인기간 중 주 양육자가 누구였는지를 중시한다. 한국은 별거 기간이 길어도 법적으로 이혼하지 않으면 혼인기간으로 인정되지만, 재산분할 시 별거 이후 형성된 재산은 제외될 수 있다. 국제결혼 이혼 시 양국 혼인신고 날짜가 다를 수 있어 혼인기간 산정에 주의가 필요하다.",
        "commonMistakes": [
            {
                "mistake": "별거하면 혼인기간에서 제외",
                "correction": "별거 기간도 법적 혼인기간에 포함",
                "explanation": "이혼 전까지는 모두 혼인기간으로 인정"
            },
            {
                "mistake": "사실혼 기간도 혼인기간에 포함",
                "correction": "법적 혼인신고 기간만 인정",
                "explanation": "사실혼은 법적 혼인기간으로 인정 안 됨"
            },
            {
                "mistake": "혼인기간이 길면 무조건 50:50 분할",
                "correction": "혼인기간은 분할 비율의 한 요소일 뿐",
                "explanation": "기여도, 재산 형성 과정 등 종합 고려"
            }
        ],
        "examples": [
            {
                "ko": "혼인기간은 혼인신고일부터 이혼일까지입니다.",
                "vi": "Thời kỳ hôn nhân tính từ ngày đăng ký kết hôn đến ngày ly hôn.",
                "situation": "formal"
            },
            {
                "ko": "별거 기간도 법적 혼인기간에 포함됩니다.",
                "vi": "Thời gian ly thân cũng được tính vào thời kỳ hôn nhân hợp pháp.",
                "situation": "formal"
            },
            {
                "ko": "혼인기간이 20년 이상이면 재산분할 비율이 높아집니다.",
                "vi": "Nếu thời kỳ hôn nhân trên 20 năm thì tỷ lệ chia tài sản sẽ cao hơn.",
                "situation": "onsite"
            }
        ],
        "relatedTerms": ["tai-san-chung", "chia-tai-san", "ly-hon", "ly-than"]
    },
    {
        "slug": "thua-ke",
        "korean": "상속",
        "vietnamese": "thừa kế",
        "hanja": "相續",
        "hanjaReading": "相(서로 상) + 續(이을 속)",
        "pronunciation": "상속",
        "meaningKo": "사망자(피상속인)의 재산과 권리·의무가 법률 또는 유언에 따라 상속인에게 이전되는 것. 한국은 법정상속(민법 규정)과 유언상속으로 나뉘며, 유언이 없으면 민법에 따라 배우자와 직계비속(자녀)이 공동 상속한다. 배우자는 직계비속과 함께 상속 시 1.5배를 받는다. 베트남도 법정상속과 유언상속을 인정하며, 유언이 우선하되 법정 상속인의 유류분(최소 몫)을 침해할 수 없다. 통역 시 '상속'과 '증여'(생전 재산 이전)를 구분해야 하며, 특히 한국은 상속세가 높아 상속 계획이 중요함을 설명해야 한다. 또한 채무도 상속되므로, 상속 포기나 한정승인 제도를 알려야 한다. 국제결혼 가정의 상속은 국적법과 속지법이 충돌할 수 있어 복잡하다.",
        "meaningVi": "Tài sản, quyền và nghĩa vụ của người chết (người để lại di sản) được chuyển cho người thừa kế theo pháp luật hoặc di chúc. Hàn Quốc chia thành thừa kế theo pháp luật (quy định dân luật) và thừa kế theo di chúc, nếu không có di chúc thì vợ/chồng và con cái sẽ cùng thừa kế theo dân luật. Vợ/chồng nhận gấp 1,5 lần khi thừa kế cùng con cái. Việt Nam cũng công nhận thừa kế pháp luật và di chúc, di chúc được ưu tiên nhưng không thể xâm phạm phần bắt buộc (phần tối thiểu) của người thừa kế theo pháp luật. Nợ cũng được thừa kế, nên có chế độ từ chối thừa kế hoặc chấp nhận thừa kế có giới hạn.",
        "context": "상속법, 유언 작성, 상속세 상담",
        "culturalNote": "한국은 상속세율이 높아(최대 50%) 생전 증여나 보험을 활용한 상속 계획이 중요하며, 배우자 공제, 자녀 공제 등 세액 공제 제도가 복잡하다. 베트남은 상속세가 없어 세금 부담이 적지만, 상속 절차가 복잡하고 서류 요구가 많다. 한국은 상속 개시 후 3개월 내 상속 포기나 한정승인을 해야 하지만, 베트남은 기한이 더 길다. 한국은 배우자가 직계비속보다 1.5배 상속받지만, 베트남은 평등하게 상속한다. 국제결혼 가정은 사망자 국적에 따라 준거법이 달라져 복잡하므로, 생전에 유언장을 명확히 작성하는 것이 중요하다.",
        "commonMistakes": [
            {
                "mistake": "상속은 재산만 물려받는다",
                "correction": "채무도 함께 상속됨",
                "explanation": "빚이 많으면 상속 포기나 한정승인 고려 필요"
            },
            {
                "mistake": "유언장만 있으면 모든 재산 자유롭게 분배",
                "correction": "법정 상속인의 유류분 보장 필요",
                "explanation": "유언도 최소 상속 몫(유류분)을 침해할 수 없음"
            },
            {
                "mistake": "상속세는 상속인 각자 부담",
                "correction": "상속인 전체가 연대하여 납부 의무",
                "explanation": "한 명이 안 내면 다른 상속인이 대신 낼 수 있음"
            }
        ],
        "examples": [
            {
                "ko": "법정상속인은 배우자와 직계비속입니다.",
                "vi": "Người thừa kế theo pháp luật là vợ/chồng và con cái.",
                "situation": "formal"
            },
            {
                "ko": "채무가 많으면 상속 포기를 고려해야 합니다.",
                "vi": "Nếu nợ nhiều, cần cân nhắc từ chối thừa kế.",
                "situation": "formal"
            },
            {
                "ko": "유언장이 있어도 유류분은 보장됩니다.",
                "vi": "Ngay cả khi có di chúc, phần bắt buộc vẫn được đảm bảo.",
                "situation": "onsite"
            }
        ],
        "relatedTerms": ["di-chuc", "nguoi-thua-ke", "chia-tai-san-thua-ke", "quyen-luu-phan"]
    },
    {
        "slug": "di-chuc",
        "korean": "유언",
        "vietnamese": "di chúc",
        "hanja": "遺言",
        "hanjaReading": "遺(남길 유) + 言(말씀 언)",
        "pronunciation": "유언",
        "meaningKo": "사망 후 재산 처분과 신변에 관한 최종 의사 표시. 한국은 민법에서 유언의 엄격한 방식(자필증서, 녹음, 공정증서, 비밀증서, 구수증서)을 규정하며, 방식을 지키지 않으면 무효가 된다. 공정증서 유언(공증인 작성)이 가장 안전하고 분쟁 가능성이 낮다. 베트남도 유언 방식을 법으로 정하며, 서면 유언이 원칙이고 공증을 권장한다. 유언은 언제든 철회·변경 가능하며, 최종 유언이 우선한다. 통역 시 유언은 반드시 법정 방식을 준수해야 효력이 있음을 강조해야 하며, 특히 자필증서 유언은 전문을 자필로 작성하고 날짜와 서명이 필수임을 설명해야 한다. 유언으로도 법정 상속인의 유류분(최소 몫)을 침해할 수 없다.",
        "meaningVi": "Tuyên bố ý chí cuối cùng về xử lý tài sản và các vấn đề cá nhân sau khi chết. Hàn Quốc quy định nghiêm ngặt về hình thức di chúc trong dân luật (di chúc tự viết, ghi âm, công chứng, bí mật, miệng...), nếu không tuân thủ hình thức sẽ vô hiệu. Di chúc công chứng (do công chứng viên lập) an toàn nhất và ít tranh chấp. Việt Nam cũng quy định hình thức di chúc theo pháp luật, nguyên tắc là di chúc bằng văn bản và khuyến khích công chứng. Di chúc có thể hủy bỏ hoặc thay đổi bất cứ lúc nào, di chúc cuối cùng được ưu tiên. Ngay cả với di chúc cũng không thể xâm phạm phần bắt buộc của người thừa kế theo pháp luật.",
        "context": "상속 계획, 유언 작성, 공증",
        "culturalNote": "한국은 유언 문화가 아직 보편화되지 않았고, 자필증서 유언이 많지만 방식 하자로 무효가 되는 경우가 많다. 공정증서 유언이 안전하지만 비용과 절차 부담으로 기피하는 경우가 있다. 베트남도 유언 문화가 발달하지 않았으나, 상속 분쟁 증가로 유언 작성이 늘고 있다. 한국은 유류분(법정 상속분의 1/2)이 보장되어 유언으로도 완전히 배제할 수 없으며, 유류분 침해 시 반환 청구 소송이 가능하다. 베트남도 유류분 제도가 있으며, 법정 상속인의 최소 몫을 보호한다. 국제결혼 가정은 양국 법률을 고려한 유언 작성이 필요하며, 가능하면 양국에서 각각 공증받는 것이 안전하다.",
        "commonMistakes": [
            {
                "mistake": "유언은 말로만 해도 된다",
                "correction": "법정 방식(자필, 녹음, 공정증서 등)을 지켜야 유효",
                "explanation": "방식 위반 시 유언 무효로 법정상속 진행"
            },
            {
                "mistake": "유언으로 모든 재산을 한 명에게 몰아줄 수 있다",
                "correction": "법정 상속인의 유류분은 보장됨",
                "explanation": "유류분 침해 시 반환 청구 가능"
            },
            {
                "mistake": "유언은 한 번 쓰면 못 바꾼다",
                "correction": "언제든 철회·변경 가능, 최종 유언이 우선",
                "explanation": "새 유언이 이전 유언을 대체"
            }
        ],
        "examples": [
            {
                "ko": "유언은 법정 방식을 지켜야 효력이 있습니다.",
                "vi": "Di chúc phải tuân thủ hình thức pháp định mới có hiệu lực.",
                "situation": "formal"
            },
            {
                "ko": "공정증서 유언이 가장 안전하고 분쟁 가능성이 낮습니다.",
                "vi": "Di chúc công chứng an toàn nhất và ít khả năng tranh chấp.",
                "situation": "formal"
            },
            {
                "ko": "유언으로도 법정 상속인의 유류분은 침해할 수 없습니다.",
                "vi": "Ngay cả với di chúc cũng không thể xâm phạm phần bắt buộc của người thừa kế.",
                "situation": "onsite"
            }
        ],
        "relatedTerms": ["thua-ke", "nguoi-thua-ke", "quyen-luu-phan", "cong-chung"]
    },
    {
        "slug": "nguoi-thua-ke",
        "korean": "상속인",
        "vietnamese": "người thừa kế",
        "hanja": "相續人",
        "hanjaReading": "相(서로 상) + 續(이을 속) + 人(사람 인)",
        "pronunciation": "상속인",
        "meaningKo": "피상속인(사망자)의 재산과 권리·의무를 물려받는 사람. 한국 민법은 상속 순위를 정하여, 1순위는 직계비속(자녀, 손자녀), 2순위는 직계존속(부모, 조부모), 3순위는 형제자매, 4순위는 4촌 이내 방계혈족이다. 배우자는 직계비속·직계존속과 공동 상속인이 되며, 이들이 없으면 단독 상속한다. 유언이 있으면 유언에 따르지만, 법정 상속인의 유류분은 보장된다. 베트남도 법정 상속 순위가 있으며, 배우자와 자녀가 1순위이다. 통역 시 '법정 상속인'과 '유언 수증자'를 구분해야 하며, 상속 포기나 결격(살해, 유기 등) 사유로 상속권을 잃을 수 있음을 설명해야 한다. 또한 상속인은 상속 개시 사실을 안 날부터 3개월 내 상속 승인·포기·한정승인 중 선택해야 한다.",
        "meaningVi": "Người nhận tài sản, quyền và nghĩa vụ của người để lại di sản (người chết). Dân luật Hàn Quốc quy định thứ tự thừa kế: thứ nhất là con cái (con, cháu), thứ hai là cha mẹ (cha mẹ, ông bà), thứ ba là anh chị em, thứ tư là họ hàng bên 4 đời. Vợ/chồng là người đồng thừa kế với con cái hoặc cha mẹ, nếu không có sẽ thừa kế đơn độc. Nếu có di chúc thì theo di chúc nhưng phần bắt buộc của người thừa kế pháp luật được đảm bảo. Việt Nam cũng có thứ tự thừa kế pháp luật, vợ/chồng và con cái là thứ nhất. Người thừa kế phải chọn chấp nhận, từ chối hoặc chấp nhận có giới hạn trong 3 tháng kể từ khi biết việc mở thừa kế.",
        "context": "상속법, 유언 상담, 상속 분쟁",
        "culturalNote": "한국은 과거 호주제 폐지 이후 남녀 상속권이 평등해졌으나, 여전히 장남이 제사를 주관하며 제사용 재산(묘지 등)을 우선 상속하는 관습이 일부 남아 있다. 베트남은 전통적으로 장남 중심 상속 문화였으나 현행법은 남녀 평등 상속을 규정한다. 한국은 배우자가 직계비속과 함께 상속 시 1.5배를 받지만, 베트남은 평등하게 배분한다. 한국은 상속 포기가 비교적 간단하지만(법원 신고), 베트남은 절차가 더 복잡하다. 국제결혼 가정은 자녀의 국적과 사망자 국적에 따라 상속법이 달라지므로, 생전에 유언으로 명확히 하거나 양국 법률 전문가 상담이 필요하다.",
        "commonMistakes": [
            {
                "mistake": "장남만 상속받는다",
                "correction": "자녀는 남녀 구분 없이 평등하게 상속",
                "explanation": "현행법은 성별 차별 없이 균등 상속 원칙"
            },
            {
                "mistake": "배우자는 항상 절반 상속",
                "correction": "공동 상속인 유무에 따라 달라짐",
                "explanation": "자녀와 함께 상속 시 1.5배, 단독 시 전부"
            },
            {
                "mistake": "상속 포기는 언제든 가능",
                "correction": "상속 개시 사실을 안 날부터 3개월 내",
                "explanation": "기한 내 법원에 신고해야 효력 발생"
            }
        ],
        "examples": [
            {
                "ko": "법정 상속인은 직계비속, 직계존속, 형제자매 순입니다.",
                "vi": "Người thừa kế pháp luật theo thứ tự: con cái, cha mẹ, anh chị em.",
                "situation": "formal"
            },
            {
                "ko": "배우자는 직계비속과 공동 상속할 때 1.5배를 받습니다.",
                "vi": "Vợ/chồng nhận gấp 1,5 lần khi đồng thừa kế với con cái.",
                "situation": "formal"
            },
            {
                "ko": "채무가 많으면 3개월 내 상속 포기를 해야 합니다.",
                "vi": "Nếu nợ nhiều, phải từ chối thừa kế trong 3 tháng.",
                "situation": "onsite"
            }
        ],
        "relatedTerms": ["thua-ke", "di-chuc", "quyen-luu-phan", "tu-choi-thua-ke"]
    },
    {
        "slug": "chia-tai-san-thua-ke",
        "korean": "유산분할",
        "vietnamese": "chia tài sản thừa kế",
        "hanja": "遺產分割",
        "hanjaReading": "遺(남길 유) + 產(낳을 산) + 分(나눌 분) + 割(나눌 할)",
        "pronunciation": "유산분할",
        "meaningKo": "상속인들이 상속재산을 구체적으로 나누는 절차. 상속이 개시되면 상속재산은 공동상속인의 공유가 되며, 유산분할을 통해 각자의 몫을 확정한다. 유언으로 분할 방법을 정할 수 있고, 없으면 상속인 간 협의로 정한다. 협의가 안 되면 법원에 유산분할 심판을 청구한다. 한국은 법정 상속분을 기준으로 하되, 특별수익(생전 증여)과 기여분(피상속인 부양)을 고려하여 구체적 상속분을 정한다. 베트남도 협의 우선이며, 협의 불성립 시 법원이 판단한다. 통역 시 '상속'(권리 취득)과 '유산분할'(구체적 배분)을 구분해야 하며, 특히 부동산이 포함되면 등기 이전 절차가 복잡함을 설명해야 한다. 유산분할 전까지는 공동상속인 전원 동의 없이 재산 처분이 불가하다.",
        "meaningVi": "Thủ tục chia cụ thể tài sản thừa kế giữa các người thừa kế. Khi mở thừa kế, tài sản trở thành sở hữu chung của các người đồng thừa kế, thông qua chia di sản để xác định phần của từng người. Có thể xác định phương thức chia bằng di chúc, nếu không có thì theo thỏa thuận giữa người thừa kế. Nếu không thỏa thuận được thì yêu cầu tòa án phán quyết chia di sản. Hàn Quốc lấy phần thừa kế pháp định làm chuẩn, nhưng xem xét lợi ích đặc biệt (tặng cho khi còn sống) và phần đóng góp (phụng dưỡng người để lại di sản) để xác định phần thừa kế cụ thể. Việt Nam cũng ưu tiên thỏa thuận, nếu không thành thì tòa án phán quyết. Trước khi chia di sản, không thể xử lý tài sản mà không có sự đồng ý của tất cả người đồng thừa kế.",
        "context": "상속 절차, 재산 분쟁, 상속 협의",
        "culturalNote": "한국은 유산분할 시 생전 증여(특별수익)를 상속분에서 공제하고, 피상속인을 특별히 부양한 상속인에게는 기여분을 인정하여 더 많이 배분한다. 부동산이 여러 개면 현물 분할이 원칙이나, 불가능하면 경매 후 금전 배분(대금분할)을 한다. 베트남은 현물 분할이 어려우면 일부 상속인이 재산을 취득하고 다른 상속인에게 금전 보상하는 방식도 가능하다. 한국은 유산분할 청구권에 소멸시효가 없어 언제든 청구 가능하지만, 베트남은 제한이 있다. 국제결혼 가정은 양국에 재산이 분산되어 있으면 각국 법률에 따라 별도로 유산분할을 진행해야 하므로 복잡하다.",
        "commonMistakes": [
            {
                "mistake": "법정 상속분대로 무조건 나눈다",
                "correction": "특별수익, 기여분 등 고려하여 조정",
                "explanation": "생전 증여나 부양 기여도가 반영됨"
            },
            {
                "mistake": "유산분할 전에도 자기 몫은 처분 가능",
                "correction": "분할 전까지는 공유 상태로 전원 동의 필요",
                "explanation": "공동상속인 합의 없이 처분 불가"
            },
            {
                "mistake": "부동산은 무조건 매각 후 금전 배분",
                "correction": "현물 분할이 원칙, 불가능 시 대금분할",
                "explanation": "가능하면 현물로 나누고 안 되면 경매"
            }
        ],
        "examples": [
            {
                "ko": "유산분할은 상속인 간 협의로 정하되, 협의가 안 되면 법원에 청구합니다.",
                "vi": "Chia di sản theo thỏa thuận giữa người thừa kế, nếu không được thì yêu cầu tòa án.",
                "situation": "formal"
            },
            {
                "ko": "생전에 증여받은 재산은 특별수익으로 상속분에서 공제됩니다.",
                "vi": "Tài sản được tặng cho khi còn sống sẽ bị trừ vào phần thừa kế như lợi ích đặc biệt.",
                "situation": "formal"
            },
            {
                "ko": "유산분할 전에는 공동상속인 전원 동의 없이 재산을 처분할 수 없습니다.",
                "vi": "Trước khi chia di sản, không thể xử lý tài sản mà không có sự đồng ý của tất cả người thừa kế.",
                "situation": "onsite"
            }
        ],
        "relatedTerms": ["thua-ke", "nguoi-thua-ke", "di-chuc", "dong-y-chia-tai-san"]
    }
]

def main():
    print("=" * 60)
    print("가족법/상속법 전문용어 추가 스크립트")
    print("=" * 60)

    # 파일 읽기
    print(f"\n1. 파일 읽기: {file_path}")
    try:
        with open(file_path, 'r', encoding='utf-8') as f:
            data = json.load(f)
        print(f"   ✓ 기존 용어 수: {len(data)}개")
    except FileNotFoundError:
        print(f"   ✗ 파일을 찾을 수 없습니다: {file_path}")
        return
    except json.JSONDecodeError as e:
        print(f"   ✗ JSON 파싱 오류: {e}")
        return

    # 중복 확인
    print("\n2. 중복 확인")
    existing_slugs = {term['slug'] for term in data}
    print(f"   기존 slug 수: {len(existing_slugs)}개")

    new_slugs = {term['slug'] for term in new_terms}
    duplicates = existing_slugs & new_slugs

    if duplicates:
        print(f"   ⚠ 중복된 slug 발견: {duplicates}")
        print("   중복 제거 후 진행...")
        new_terms_filtered = [t for t in new_terms if t['slug'] not in existing_slugs]
    else:
        print("   ✓ 중복 없음")
        new_terms_filtered = new_terms

    if not new_terms_filtered:
        print("\n   모든 용어가 이미 존재합니다. 추가할 항목이 없습니다.")
        return

    # 용어 추가
    print(f"\n3. 용어 추가 ({len(new_terms_filtered)}개)")
    for term in new_terms_filtered:
        print(f"   + {term['slug']} ({term['korean']} - {term['vietnamese']})")

    data.extend(new_terms_filtered)

    # 파일 저장
    print(f"\n4. 파일 저장: {file_path}")
    try:
        with open(file_path, 'w', encoding='utf-8') as f:
            json.dump(data, f, ensure_ascii=False, indent=2)
        print(f"   ✓ 저장 완료")
        print(f"   ✓ 최종 용어 수: {len(data)}개")
    except Exception as e:
        print(f"   ✗ 저장 실패: {e}")
        return

    print("\n" + "=" * 60)
    print("✅ 작업 완료")
    print("=" * 60)
    print("\n다음 단계:")
    print("1. npm run validate:terms -- --domain=legal")
    print("2. 검증 통과 확인")
    print("3. git add src/data/terms/legal.json")
    print("4. git commit")

if __name__ == "__main__":
    main()
