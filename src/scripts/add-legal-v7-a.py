#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""지식재산권 심화 용어 추가 스크립트 (v7-a)"""

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
            "slug": "bi-mat-kinh-doanh",
            "korean": "영업비밀",
            "vietnamese": "Bí mật kinh doanh",
            "hanja": "營業秘密",
            "hanjaReading": "營(경영할 영) 業(업 업) 秘(숨길 비) 密(빽빽할 밀)",
            "pronunciation": "비 밋 끼잉 조안",
            "meaningKo": "영업비밀은 공공연히 알려져 있지 않고 독립된 경제적 가치를 가지며 상당한 노력에 의하여 비밀로 유지된 생산방법, 판매방법, 그 밖에 영업활동에 유용한 기술상 또는 경영상의 정보를 말합니다. 통역 시 주의할 점은 영업비밀은 특허와 달리 등록이나 출원 절차 없이 보호되며, 비밀유지계약(NDA)과 밀접한 관련이 있다는 점을 강조해야 합니다. 또한 영업비밀 침해는 형사처벌 대상이 될 수 있어 기업 간 분쟁에서 매우 민감한 사안이므로 통역사는 기밀유지 의무를 철저히 준수해야 합니다.",
            "meaningVi": "Bí mật kinh doanh là thông tin kỹ thuật hoặc kinh doanh hữu ích cho hoạt động kinh doanh, không được công chúng biết đến, có giá trị kinh tế độc lập và được duy trì bí mật bằng nỗ lực đáng kể. Khác với bằng sáng chế, bí mật kinh doanh được bảo vệ mà không cần đăng ký.",
            "context": "부정경쟁방지법, 기술유출 분쟁, NDA 계약서",
            "culturalNote": "한국은 부정경쟁방지법으로 영업비밀을 보호하며 침해 시 형사처벌이 가능하지만, 베트남은 지적재산권법에서 규율하며 민사적 구제가 주를 이룹니다. 한국 기업들은 영업비밀 보호를 매우 중시하여 입사 시부터 퇴사 후까지 엄격한 비밀유지 서약을 요구하는 반면, 베트nam 기업들은 상대적으로 덜 체계적인 경우가 많아 한국 기업과의 기술협력 시 인식 차이가 발생할 수 있습니다.",
            "commonMistakes": [
                {
                    "mistake": "영업비밀을 'bí mật công ty'로 번역",
                    "correction": "'bí mật kinh doanh'로 정확히 표현",
                    "explanation": "'bí mật công ty'는 단순히 '회사 비밀'이라는 의미로 법적 용어가 아니며, 'bí mật kinh doanh'가 법률에서 정의된 정확한 용어입니다."
                },
                {
                    "mistake": "특허(bằng sáng chế)와 영업비밀을 혼동",
                    "correction": "등록 여부와 보호 방식의 차이를 명확히 구분",
                    "explanation": "특허는 공개를 전제로 등록하여 보호받지만, 영업비밀은 비공개 상태를 유지함으로써 보호받는다는 근본적 차이가 있습니다."
                },
                {
                    "mistake": "'비밀유지'를 'giữ bí mật'로만 번역",
                    "correction": "법적 맥락에서는 'bảo vệ bí mật kinh doanh' 사용",
                    "explanation": "'giữ bí mật'은 일상적 표현이고, 법률 문서에서는 'bảo vệ'(보호하다)를 사용하여 법적 의무임을 명확히 해야 합니다."
                }
            ],
            "examples": [
                {
                    "ko": "본 계약에 따라 을은 갑의 영업비밀을 제3자에게 누설하지 않을 의무를 부담합니다.",
                    "vi": "Theo hợp đồng này, Bên B có nghĩa vụ không tiết lộ bí mật kinh doanh của Bên A cho bên thứ ba.",
                    "situation": "formal"
                },
                {
                    "ko": "퇴직 후에도 재직 중 알게 된 영업비밀을 사용하거나 공개할 수 없습니다.",
                    "vi": "Ngay cả sau khi nghỉ việc, không được sử dụng hoặc tiết lộ bí mật kinh doanh đã biết trong thời gian làm việc.",
                    "situation": "formal"
                },
                {
                    "ko": "경쟁사로 이직한 직원이 우리 회사의 영업비밀을 유출한 정황이 포착되었습니다.",
                    "vi": "Phát hiện dấu hiệu nhân viên chuyển sang công ty đối thủ đã rò rỉ bí mật kinh doanh của công ty chúng ta.",
                    "situation": "onsite"
                }
            ],
            "relatedTerms": ["부정경쟁행위", "비밀유지계약", "기술유출", "경업금지"]
        },
        {
            "slug": "hanh-vi-canh-tranh-khong-lanh-manh",
            "korean": "부정경쟁행위",
            "vietnamese": "Hành vi cạnh tranh không lành mạnh",
            "hanja": "不正競爭行爲",
            "hanjaReading": "不(아닐 부) 正(바를 정) 競(다툴 경) 爭(다툴 쟁) 行(다닐 행) 爲(할 위)",
            "pronunciation": "하잉 비 까잉 짱 콩 라잉 마잉",
            "meaningKo": "부정경쟁행위는 부정한 수단으로 경쟁자의 고객을 빼앗거나 영업비밀을 침해하는 등 공정한 상거래 질서를 해치는 행위를 말합니다. 통역 시 주의할 점은 단순한 '불공정행위'가 아니라 상법과 부정경쟁방지법상 금지되는 구체적 행위 유형이라는 점을 분명히 해야 합니다. 혼동표지 사용, 원산지 허위표시, 영업비밀 침해, 타인의 상품 형태 모방 등 다양한 유형이 있으며, 통역사는 각 유형의 법적 요건과 효과를 정확히 구분하여 전달해야 합니다.",
            "meaningVi": "Hành vi cạnh tranh không lành mạnh là hành vi sử dụng phương tiện không chính đáng để chiếm đoạt khách hàng của đối thủ hoặc xâm phạm bí mật kinh doanh, gây tổn hại đến trật tự giao dịch công bằng. Bao gồm nhiều loại như sử dụng ký hiệu gây nhầm lẫn, ghi sai xuất xứ, xâm phạm bí mật kinh doanh, sao chép hình thức sản phẩm.",
            "context": "부정경쟁방지법, 상표권 분쟁, 영업비밀 침해 소송",
            "culturalNote": "한국의 부정경쟁방지법은 일본 법제의 영향을 받아 매우 상세하고 구체적인 행위 유형을 열거하는 반면, 베트남은 일반 조항 중심으로 규율하여 법원의 재량이 더 큽니다. 한국 기업들은 상표나 디자인이 유사하다는 이유만으로도 적극적으로 법적 대응을 하는 경향이 있지만, 베트남에서는 실질적 혼동 가능성이 높아야 인정되는 경우가 많아 양국 간 법적 기준의 차이를 통역 시 명확히 전달해야 합니다.",
            "commonMistakes": [
                {
                    "mistake": "'cạnh tranh không công bằng'으로 번역",
                    "correction": "'cạnh tranh không lành mạnh'가 법률 용어",
                    "explanation": "'không công bằng'(불공정)보다 'không lành mạnh'(불건전)가 베트남 법률에서 사용하는 정확한 표현입니다."
                },
                {
                    "mistake": "단순 불공정거래와 부정경쟁행위를 혼동",
                    "correction": "부정경쟁행위는 지적재산권 관련 특수 유형임을 강조",
                    "explanation": "공정거래법상 불공정거래는 시장지배적지위 남용 등이고, 부정경쟁행위는 상표·영업비밀 등 지재권 침해 유형입니다."
                },
                {
                    "mistake": "'부정'을 'gian lận'으로만 번역",
                    "correction": "법적 맥락에서는 'không lành mạnh' 또는 'không chính đáng' 사용",
                    "explanation": "'gian lận'은 사기(fraud)의 의미가 강하여 법률 용어로는 부적절합니다."
                }
            ],
            "examples": [
                {
                    "ko": "피고의 상표 사용은 원고의 저명상표와 혼동을 일으킬 수 있어 부정경쟁행위에 해당합니다.",
                    "vi": "Việc sử dụng nhãn hiệu của bị đơn có thể gây nhầm lẫn với nhãn hiệu nổi tiếng của nguyên đơn, cấu thành hành vi cạnh tranh không lành mạnh.",
                    "situation": "formal"
                },
                {
                    "ko": "부정경쟁방지법은 영업비밀 침해뿐 아니라 원산지 허위표시도 금지하고 있습니다.",
                    "vi": "Luật chống cạnh tranh không lành mạnh không chỉ cấm xâm phạm bí mật kinh doanh mà còn cấm ghi sai xuất xứ.",
                    "situation": "formal"
                },
                {
                    "ko": "타사 제품 디자인을 무단 모방한 것은 명백한 부정경쟁행위로 손해배상 청구가 가능합니다.",
                    "vi": "Việc sao chép trái phép thiết kế sản phẩm của công ty khác là hành vi cạnh tranh không lành mạnh rõ ràng, có thể yêu cầu bồi thường thiệt hại.",
                    "situation": "onsite"
                }
            ],
            "relatedTerms": ["영업비밀", "혼동표지", "원산지표시", "상품형태모방"]
        },
        {
            "slug": "phat-minh-trong-cong-viec",
            "korean": "직무발명",
            "vietnamese": "Phát minh trong công việc",
            "hanja": "職務發明",
            "hanjaReading": "職(직무 직) 務(일 무) 發(필 발) 明(밝을 명)",
            "pronunciation": "팟 밍 쫑 꽁 비엑",
            "meaningKo": "직무발명은 종업원이 사용자의 업무 범위에 속하고 그 발명을 하게 된 행위가 종업원의 현재 또는 과거 직무에 속하는 발명을 말합니다. 통역 시 주의할 점은 직무발명의 권리는 원칙적으로 발명자인 종업원에게 속하지만, 회사가 승계할 수 있으며 이 경우 종업원은 정당한 보상을 받을 권리가 있다는 점입니다. 특히 대기업과 중소기업 간, 한국과 베트남 간 직무발명 보상 관행의 차이가 크므로 통역 시 이를 명확히 설명해야 합니다.",
            "meaningVi": "Phát minh trong công việc là phát minh thuộc phạm vi công việc của người sử dụng lao động và hành vi dẫn đến phát minh đó thuộc nhiệm vụ hiện tại hoặc trước đây của người lao động. Quyền sở hữu ban đầu thuộc về người lao động nhưng công ty có thể kế thừa và phải trả thù lao hợp lý.",
            "context": "발명진흥법, 특허 출원, 연구개발 계약서",
            "culturalNote": "한국은 발명진흥법으로 직무발명 보상을 의무화하고 있으며, 대기업의 경우 수억 원 규모의 보상금 지급 사례도 있지만, 베트남은 이에 대한 법적 규정이 명확하지 않아 노사 분쟁의 소지가 큽니다. 한국 연구원들은 직무발명 보상에 대한 인식이 높고 적극적으로 권리를 주장하는 반면, 베트남에서는 회사의 재산으로 당연시하는 경향이 있어 한국 기업이 베트남 지사에서 연구개발 조직을 운영할 때 보상 체계를 명확히 정립해야 합니다.",
            "commonMistakes": [
                {
                    "mistake": "'phát minh của công ty'로 번역하여 소유권 혼동",
                    "correction": "'phát minh trong công việc' 또는 'phát minh chức vụ'로 정확히 표현",
                    "explanation": "직무발명은 회사 소유가 아니라 특정 법적 요건을 충족하는 발명의 유형이며, 권리 귀속은 별도로 결정됩니다."
                },
                {
                    "mistake": "보상금(thù lao)과 급여(lương)를 혼동",
                    "correction": "직무발명 보상은 급여와 별도의 'thù lao phát minh'임을 강조",
                    "explanation": "직무발명 보상은 발명의 경제적 가치에 비례하여 지급되는 별도의 보상으로, 통상 급여와는 다른 산정 기준을 적용합니다."
                },
                {
                    "mistake": "'승계'를 'thừa kế'(상속)로 번역",
                    "correction": "계약적 이전의 의미로 'chuyển giao' 또는 'tiếp nhận' 사용",
                    "explanation": "'thừa kế'는 사망에 따른 상속이므로, 직무발명의 계약적 권리 이전에는 'chuyển giao quyền'이 적절합니다."
                }
            ],
            "examples": [
                {
                    "ko": "귀하의 발명은 직무발명에 해당하므로 회사가 특허를 받을 권리를 승계하되, 정당한 보상금을 지급하겠습니다.",
                    "vi": "Phát minh của anh/chị là phát minh trong công việc nên công ty sẽ tiếp nhận quyền được cấp bằng sáng chế, nhưng sẽ trả thù lao hợp lý.",
                    "situation": "formal"
                },
                {
                    "ko": "연구소에 근무하는 직원의 발명은 대부분 직무발명으로 인정됩니다.",
                    "vi": "Hầu hết các phát minh của nhân viên làm việc tại viện nghiên cứu được công nhận là phát minh trong công việc.",
                    "situation": "onsite"
                },
                {
                    "ko": "직무발명 보상금 산정 시 특허의 경제적 가치와 회사의 기여도를 종합적으로 고려합니다.",
                    "vi": "Khi tính thù lao phát minh trong công việc, xem xét tổng hợp giá trị kinh tế của bằng sáng chế và mức độ đóng góp của công ty.",
                    "situation": "formal"
                }
            ],
            "relatedTerms": ["특허권", "발명자", "승계", "보상금"]
        },
        {
            "slug": "giai-phap-huu-ich",
            "korean": "실용신안",
            "vietnamese": "Giải pháp hữu ích",
            "hanja": "實用新案",
            "hanjaReading": "實(열매 실) 用(쓸 용) 新(새 신) 案(책상 안)",
            "pronunciation": "자이 팝 흐우 윽",
            "meaningKo": "실용신안은 물품의 형상, 구조 또는 조합에 관한 고안으로서 실용적 가치가 있는 발명을 보호하는 제도입니다. 통역 시 주의할 점은 특허가 '발명'을 보호하는 반면 실용신안은 '고안'을 보호하며, 기술 수준이 특허보다 낮아도 등록이 가능하다는 점입니다. 심사 절차가 특허보다 간소하고 등록이 빠르지만 보호 기간은 10년으로 특허의 20년보다 짧습니다. 베트남에서는 'Giải pháp hữu ích'로 불리며 한국과 유사한 제도를 운영하고 있음을 안내해야 합니다.",
            "meaningVi": "Giải pháp hữu ích là chế độ bảo hộ sáng chế về hình dạng, cấu trúc hoặc tổ hợp của vật phẩm có giá trị thực tiễn. Khác với bằng sáng chế bảo hộ 'phát minh', giải pháp hữu ích bảo hộ 'sáng kiến' với mức độ kỹ thuật thấp hơn. Thủ tục thẩm định đơn giản hơn và đăng ký nhanh hơn, nhưng thời hạn bảo hộ chỉ 10 năm so với 20 năm của bằng sáng chế.",
            "context": "특허법, 실용신안법, 기술 보호 전략",
            "culturalNote": "한국에서는 중소기업이나 개인 발명가들이 특허보다 저렴하고 빠른 실용신안을 선호하는 경향이 있으며, 생활용품이나 간단한 도구 개량에 많이 활용됩니다. 베트남도 유사한 제도를 운영하지만 인지도가 낮아 활용도가 떨어지는 편입니다. 한국 기업이 베트남에서 신속한 권리 확보가 필요한 경우 실용신안 출원을 고려할 수 있으나, 기술적 가치가 높은 발명은 특허로 출원하는 것이 유리함을 조언해야 합니다.",
            "commonMistakes": [
                {
                    "mistake": "실용신안을 'sáng chế thực dụng'으로 번역",
                    "correction": "'Giải pháp hữu ích'가 법정 용어",
                    "explanation": "베트남 지적재산권법에서 정의한 정확한 용어는 'Giải pháp hữu ích'이며, 'sáng chế'는 특허(bằng sáng chế)와 혼동됩니다."
                },
                {
                    "mistake": "특허와 실용신안의 차이를 설명하지 않음",
                    "correction": "발명 vs 고안, 심사 난이도, 보호 기간 차이를 명확히 구분",
                    "explanation": "두 제도는 보호 대상과 요건이 다르므로 통역 시 반드시 구분하여 설명해야 클라이언트가 적절한 선택을 할 수 있습니다."
                },
                {
                    "mistake": "'고안'을 단순히 'ý tưởng'로 번역",
                    "correction": "'sáng kiến kỹ thuật' 또는 'giải pháp kỹ thuật'로 표현",
                    "explanation": "'ý tưởng'는 추상적 아이디어이고, 실용신안의 '고안'은 구체적이고 실용적인 기술적 해결책을 의미합니다."
                }
            ],
            "examples": [
                {
                    "ko": "이 제품은 기존 제품의 구조를 개선한 것이므로 특허보다는 실용신안으로 출원하는 것이 적합합니다.",
                    "vi": "Sản phẩm này cải tiến cấu trúc của sản phẩm hiện có nên thích hợp đăng ký giải pháp hữu ích hơn là bằng sáng chế.",
                    "situation": "formal"
                },
                {
                    "ko": "실용신안은 심사 기간이 짧아 빠르게 권리를 확보할 수 있지만, 보호 기간이 10년에 불과합니다.",
                    "vi": "Giải pháp hữu ích có thời gian thẩm định ngắn nên có thể xác lập quyền nhanh chóng, nhưng thời hạn bảo hộ chỉ có 10 năm.",
                    "situation": "formal"
                },
                {
                    "ko": "간단한 생활용품 개량이라면 실용신안 등록만으로도 충분히 권리를 보호받을 수 있습니다.",
                    "vi": "Nếu chỉ là cải tiến đồ dùng sinh hoạt đơn giản thì chỉ cần đăng ký giải pháp hữu ích cũng đủ để bảo vệ quyền.",
                    "situation": "onsite"
                }
            ],
            "relatedTerms": ["특허", "고안", "기술혁신", "등록출원"]
        },
        {
            "slug": "bang-sang-che-thiet-ke",
            "korean": "디자인특허",
            "vietnamese": "Bằng sáng chế thiết kế",
            "hanja": None,
            "hanjaReading": None,
            "pronunciation": "방 상 쩨 티엣 께",
            "meaningKo": "디자인특허는 물품의 형상, 모양, 색채 또는 이들의 결합으로 시각을 통하여 미감을 일으키게 하는 디자인을 보호하는 권리입니다. 통역 시 주의할 점은 한국에서는 '디자인보호법'으로 특허와 별도 법률로 보호하지만 영문으로는 'Design Patent'라 하며, 베트남도 지적재산권법 내에서 '공업디자인(Kiểu dáng công nghiệp)' 또는 '디자인특허'로 보호한다는 점입니다. 신규성과 창작성이 요구되며, 실물 제품뿐 아니라 GUI(그래픽 유저 인터페이스) 디자인도 보호 대상에 포함됨을 설명해야 합니다.",
            "meaningVi": "Bằng sáng chế thiết kế là quyền bảo hộ thiết kế tạo nên cảm thụ thẩm mỹ thông qua thị giác nhờ hình dạng, kiểu dáng, màu sắc của sản phẩm hoặc sự kết hợp của chúng. Yêu cầu tính mới và tính sáng tạo, bảo hộ cả sản phẩm vật lý và thiết kế GUI (giao diện đồ họa người dùng).",
            "context": "디자인보호법, 제품 디자인 보호, 모방 분쟁",
            "culturalNote": "한국은 디자인 보호에 매우 적극적이어서 가전제품, 자동차, 화장품 용기 등 거의 모든 제품에 디자인 출원을 하며, 삼성·LG 등 대기업은 수만 건의 디자인 포트폴리오를 보유하고 있습니다. 베트남도 디자인 보호 제도가 있지만 활용도가 낮고, 특히 중소기업은 디자인 등록의 중요성을 잘 인식하지 못하는 경우가 많습니다. 한국 기업이 베트남에서 제품을 출시할 때는 현지 디자인 등록을 반드시 선행해야 모방품 대응이 가능함을 조언해야 합니다.",
            "commonMistakes": [
                {
                    "mistake": "'thiết kế công nghiệp'과 'bằng sáng chế thiết kế'를 혼용",
                    "correction": "베트남 법률상 'Kiểu dáng công nghiệp'이 정확하지만 'bằng sáng chế thiết kế'도 통용됨을 안내",
                    "explanation": "베트남 지적재산권법의 공식 용어는 'Kiểu dáng công nghiệp'이지만, 실무에서는 두 용어가 혼용되므로 문맥에 따라 선택합니다."
                },
                {
                    "mistake": "디자인과 상표를 혼동",
                    "correction": "디자인은 물품의 외관, 상표는 출처 표시 기능임을 구분",
                    "explanation": "디자인은 제품의 형상·모양을 보호하고, 상표는 브랜드를 보호하는 전혀 다른 권리입니다."
                },
                {
                    "mistake": "'미감'을 'vẻ đẹp'로만 번역",
                    "correction": "'cảm thụ thẩm mỹ' 또는 'giá trị thẩm mỹ'로 법률적 표현 사용",
                    "explanation": "'vẻ đẹp'는 일상 용어이고, 법률에서는 '심미적 감각'이라는 의미의 정확한 용어를 사용해야 합니다."
                }
            ],
            "examples": [
                {
                    "ko": "귀사의 신제품 디자인은 독창적이므로 출시 전에 디자인특허를 출원하시길 권장합니다.",
                    "vi": "Thiết kế sản phẩm mới của quý công ty rất độc đáo nên khuyến nghị nộp đơn đăng ký bằng sáng chế thiết kế trước khi tung ra thị trường.",
                    "situation": "formal"
                },
                {
                    "ko": "경쟁사가 우리 제품 디자인을 모방했으므로 디자인권 침해 소송을 제기하겠습니다.",
                    "vi": "Đối thủ cạnh tranh đã sao chép thiết kế sản phẩm của chúng ta nên sẽ khởi kiện xâm phạm quyền thiết kế.",
                    "situation": "onsite"
                },
                {
                    "ko": "스마트폰 화면의 아이콘 배치도 GUI 디자인으로 보호받을 수 있습니다.",
                    "vi": "Cách bố trí biểu tượng trên màn hình điện thoại thông minh cũng có thể được bảo hộ như thiết kế GUI.",
                    "situation": "formal"
                }
            ],
            "relatedTerms": ["공업디자인", "의장권", "신규성", "창작성"]
        },
        {
            "slug": "xam-pham-nhan-hieu",
            "korean": "상표침해",
            "vietnamese": "Xâm phạm nhãn hiệu",
            "hanja": "商標侵害",
            "hanjaReading": "商(장사 상) 標(표 표) 侵(침노할 침) 害(해할 해)",
            "pronunciation": "삼 팜 년 히에우",
            "meaningKo": "상표침해는 타인의 등록상표를 정당한 권원 없이 동일·유사한 상품에 사용하여 상표권자의 독점적 권리를 침해하는 행위를 말합니다. 통역 시 주의할 점은 단순히 비슷한 상표를 사용하는 것뿐 아니라 혼동을 일으킬 우려가 있는지가 핵심 판단 기준이라는 점입니다. 한국은 상표 침해에 대해 형사처벌과 손해배상을 모두 인정하며, 관세청을 통한 수입 금지 조치도 가능함을 설명해야 합니다. 베트남에서도 상표권 침해는 중대한 법적 책임을 수반하므로 사전 상표 검색이 필수임을 강조해야 합니다.",
            "meaningVi": "Xâm phạm nhãn hiệu là hành vi sử dụng nhãn hiệu đã đăng ký của người khác trên sản phẩm giống hoặc tương tự mà không có quyền hợp pháp, xâm phạm quyền độc quyền của chủ sở hữu nhãn hiệu. Tiêu chí quan trọng là khả năng gây nhầm lẫn, không chỉ là sử dụng nhãn hiệu tương tự. Có thể bị xử lý hình sự và bồi thường thiệt hại, cũng như cấm nhập khẩu qua cơ quan hải quan.",
            "context": "상표법, 브랜드 보호, 모조품 단속",
            "culturalNote": "한국은 상표권 보호가 매우 엄격하여 글로벌 브랜드들이 적극적으로 법적 대응을 하며, 동대문 시장 등에서 모조품 단속이 정기적으로 이루어집니다. 베트남은 상표 침해가 만연하여 위조품 시장이 크지만, 최근 법 집행이 강화되는 추세입니다. 한국 브랜드가 베트남에 진출할 때는 현지 상표 등록과 함께 적극적인 감시·단속 활동이 필요하며, 특히 온라인 플랫폼에서의 모조품 유통에 주의해야 함을 조언해야 합니다.",
            "commonMistakes": [
                {
                    "mistake": "'침해'를 'vi phạm'으로만 번역",
                    "correction": "지재권 침해는 'xâm phạm', 일반 위반은 'vi phạm'으로 구분",
                    "explanation": "'xâm phạm'은 권리 침해의 의미로 더 강하고 법적인 표현이며, 'vi phạm'은 규정 위반 등에 사용됩니다."
                },
                {
                    "mistake": "동일상표만 침해로 보고 유사상표는 제외",
                    "correction": "혼동을 일으킬 우려가 있는 유사상표도 침해 대상임을 명확히",
                    "explanation": "상표법은 '동일·유사' 상표를 모두 침해로 규정하며, 실무에서는 유사성 판단이 주요 쟁점이 됩니다."
                },
                {
                    "mistake": "'모조품'과 '상표침해'를 동일시",
                    "correction": "모조품(hàng giả)은 상표침해의 한 유형이지만 모든 침해가 모조품은 아님",
                    "explanation": "상표침해는 유사 상표 사용, 희석화 등 다양한 유형이 있으며, 물리적 모조품 제조는 그 중 일부입니다."
                }
            ],
            "examples": [
                {
                    "ko": "피고가 사용한 상표는 원고의 등록상표와 외관이 유사하여 일반 소비자에게 혼동을 일으킬 우려가 있으므로 상표침해에 해당합니다.",
                    "vi": "Nhãn hiệu mà bị đơn sử dụng có hình thức tương tự với nhãn hiệu đã đăng ký của nguyên đơn, có khả năng gây nhầm lẫn cho người tiêu dùng thông thường nên cấu thành xâm phạm nhãn hiệu.",
                    "situation": "formal"
                },
                {
                    "ko": "상표권 침해로 형사고소와 함께 손해배상 청구를 병행하겠습니다.",
                    "vi": "Vừa tố cáo hình sự về xâm phạm quyền nhãn hiệu vừa yêu cầu bồi thường thiệt hại song song.",
                    "situation": "formal"
                },
                {
                    "ko": "온라인 쇼핑몰에서 우리 브랜드를 무단 사용한 판매자를 발견했으니 즉시 삭제 요청하겠습니다.",
                    "vi": "Phát hiện người bán sử dụng trái phép thương hiệu của chúng ta trên sàn thương mại điện tử nên sẽ yêu cầu xóa ngay lập tức.",
                    "situation": "onsite"
                }
            ],
            "relatedTerms": ["등록상표", "혼동가능성", "모조품", "손해배상"]
        },
        {
            "slug": "quyen-lien-quan",
            "korean": "저작인접권",
            "vietnamese": "Quyền liên quan",
            "hanja": "著作隣接權",
            "hanjaReading": "著(지을 저) 作(지을 작) 隣(이웃 린) 接(이을 접) 權(권세 권)",
            "pronunciation": "꾸엔 리엔 꾸안",
            "meaningKo": "저작인접권은 저작물의 공연·실연·방송·음반제작 등 저작물을 매개하는 자(실연자, 음반제작자, 방송사업자)에게 인정되는 권리로서, 저작권과 유사하지만 별개의 독립된 권리입니다. 통역 시 주의할 점은 저작권이 창작자에게 부여되는 반면, 저작인접권은 창작물을 전달·보급하는 과정에서 기여한 자에게 주어진다는 차이를 명확히 해야 합니다. 예를 들어 가수는 노래(저작물)를 부른 실연자로서 저작인접권을 가지며, 이는 작곡가의 저작권과는 별개입니다.",
            "meaningVi": "Quyền liên quan là quyền được công nhận cho những người trung gian truyền tải tác phẩm (nghệ sĩ biểu diễn, nhà sản xuất bản ghi âm, tổ chức phát sóng) như biểu diễn, phát sóng, sản xuất bản ghi âm tác phẩm, là quyền độc lập tương tự nhưng khác biệt với quyền tác giả. Quyền tác giả thuộc về người sáng tạo, còn quyền liên quan thuộc về người đóng góp trong quá trình truyền tải và phổ biến tác phẩm sáng tạo.",
            "context": "저작권법, 음반 계약, 방송 권리, 공연 계약",
            "culturalNote": "한국은 저작인접권 개념이 정착되어 가수, 방송사 등이 독자적 권리를 적극적으로 행사하며, 음원 사이트나 유튜브에서 수익 배분 시 저작권자와 실연자가 각각 몫을 받습니다. 베트남도 법적으로는 저작인접권을 인정하지만 실무에서는 인식이 낮아 실연자나 음반제작자가 권리를 제대로 주장하지 못하는 경우가 많습니다. 한국 엔터테인먼트 기업이 베트남에서 활동할 때는 저작인접권 계약을 명확히 하여 향후 분쟁을 예방해야 합니다.",
            "commonMistakes": [
                {
                    "mistake": "저작인접권을 단순히 'quyền tác giả phụ'(부차적 저작권)로 번역",
                    "correction": "'quyền liên quan'이 법정 용어",
                    "explanation": "'quyền tác giả phụ'는 저작권의 하위 개념으로 오해될 수 있으나, 저작인접권은 독립된 별개의 권리입니다."
                },
                {
                    "mistake": "실연자(nghệ sĩ biểu diễn)와 저작자를 혼동",
                    "correction": "작곡가는 저작권자, 가수는 저작인접권자임을 구분",
                    "explanation": "같은 노래에 대해 작곡가는 저작권을, 가수는 실연에 대한 저작인접권을 가지는 별개의 권리 주체입니다."
                },
                {
                    "mistake": "'방송사업자'를 단순히 'đài truyền hình'으로만 번역",
                    "correction": "법적 주체로서 'tổ chức phát sóng' 사용",
                    "explanation": "'đài truyền hình'은 TV 방송국이고, 저작인접권의 주체로는 라디오 등을 포함하는 'tổ chức phát sóng'이 적절합니다."
                }
            ],
            "examples": [
                {
                    "ko": "이 노래의 작곡가는 저작권을, 가수는 저작인접권을 각각 보유하며, 음원 사용 시 양자의 허락이 모두 필요합니다.",
                    "vi": "Nhạc sĩ sáng tác bài hát này có quyền tác giả, ca sĩ có quyền liên quan, khi sử dụng bản nhạc cần có sự cho phép của cả hai bên.",
                    "situation": "formal"
                },
                {
                    "ko": "방송사는 프로그램에 대한 저작인접권을 가지므로, 타 매체에서 무단 재방송할 수 없습니다.",
                    "vi": "Đài phát thanh có quyền liên quan đối với chương trình nên các phương tiện khác không được phát sóng lại tùy tiện.",
                    "situation": "formal"
                },
                {
                    "ko": "실연자의 공연 영상을 유튜브에 올리려면 저작인접권자의 동의가 필요합니다.",
                    "vi": "Để đăng video biểu diễn của nghệ sĩ lên YouTube cần có sự đồng ý của người có quyền liên quan.",
                    "situation": "onsite"
                }
            ],
            "relatedTerms": ["저작권", "실연자", "음반제작자", "방송사업자"]
        },
        {
            "slug": "quyen-co-so-du-lieu",
            "korean": "데이터베이스권",
            "vietnamese": "Quyền cơ sở dữ liệu",
            "hanja": None,
            "hanjaReading": None,
            "pronunciation": "꾸엔 꺼 써 주 리에우",
            "meaningKo": "데이터베이스권은 데이터베이스의 제작 또는 그 소재의 갱신·검증·보충에 인적 또는 물적으로 상당한 투자를 한 자가 그 데이터베이스의 전부 또는 상당한 부분을 복제·배포·방송·전송할 권리를 독점하는 것을 말합니다. 통역 시 주의할 점은 이는 개별 데이터의 저작권과는 별개로, 데이터의 수집·정리·배열이라는 '투자'를 보호하는 권리라는 점입니다. 한국은 EU와 유사하게 데이터베이스 제작자의 권리를 인정하지만, 베트남은 명문 규정이 없어 저작권법상 편집저작물로 보호받는 정도여서 한-베 간 법적 보호 수준에 차이가 있음을 설명해야 합니다.",
            "meaningVi": "Quyền cơ sở dữ liệu là quyền độc quyền sao chép, phân phối, phát sóng, truyền đạt toàn bộ hoặc phần đáng kể của cơ sở dữ liệu mà người đã đầu tư đáng kể về nhân lực hoặc vật lực vào việc sản xuất hoặc cập nhật, xác minh, bổ sung tài liệu của cơ sở dữ liệu đó. Khác với quyền tác giả của dữ liệu riêng lẻ, đây là quyền bảo vệ 'sự đầu tư' vào việc thu thập, sắp xếp dữ liệu.",
            "context": "저작권법, 빅데이터, 정보 서비스 계약",
            "culturalNote": "한국은 포털사이트, 통신사 등 대규모 데이터베이스를 운영하는 기업들이 데이터베이스권을 적극 주장하며, 특히 웹 스크래핑이나 크롤링에 대해 법적 조치를 취하는 경우가 많습니다. 베트남은 데이터베이스 보호 개념이 약하여 무단 수집·활용이 빈번하며, 한국 기업이 베트남에 DB 기반 서비스를 제공할 때는 기술적 보호조치(API 제한, 접근 통제 등)를 병행해야 합니다. 최근 AI 학습 데이터로서 DB의 가치가 높아지면서 데이터베이스권의 중요성이 더욱 부각되고 있습니다.",
            "commonMistakes": [
                {
                    "mistake": "데이터베이스권을 단순히 'quyền sở hữu dữ liệu'로 번역",
                    "correction": "'quyền cơ sở dữ liệu' 또는 'quyền đối với cơ sở dữ liệu'",
                    "explanation": "'sở hữu dữ liệu'는 데이터 자체의 소유이고, 법적 개념은 데이터베이스 '제작'에 대한 권리입니다."
                },
                {
                    "mistake": "편집저작물과 데이터베이스권을 혼동",
                    "correction": "편집저작물은 창작성 요구, 데이터베이스권은 투자만으로 보호",
                    "explanation": "편집저작물은 선택·배열의 창작성이 있어야 하지만, 데이터베이스권은 상당한 투자만 있으면 창작성 없이도 보호됩니다."
                },
                {
                    "mistake": "'스크래핑'을 단순 기술 용어로만 설명",
                    "correction": "무단 스크래핑은 데이터베이스권 침해가 될 수 있음을 경고",
                    "explanation": "웹 스크래핑은 기술적으로는 가능하지만 법적으로는 데이터베이스 제작자의 권리를 침해할 수 있습니다."
                }
            ],
            "examples": [
                {
                    "ko": "당사의 부동산 매물 데이터베이스는 수년간의 투자로 구축한 것이므로, 무단 크롤링 시 데이터베이스권 침해로 법적 조치를 취하겠습니다.",
                    "vi": "Cơ sở dữ liệu bất động sản của công ty chúng tôi được xây dựng qua nhiều năm đầu tư, nếu thu thập trái phép sẽ bị xử lý pháp lý về xâm phạm quyền cơ sở dữ liệu.",
                    "situation": "formal"
                },
                {
                    "ko": "데이터베이스의 상당 부분을 복제하여 경쟁 서비스를 만드는 것은 데이터베이스권 침해입니다.",
                    "vi": "Sao chép phần đáng kể của cơ sở dữ liệu để tạo dịch vụ cạnh tranh là xâm phạm quyền cơ sở dữ liệu.",
                    "situation": "formal"
                },
                {
                    "ko": "API를 통한 정상적인 데이터 접근은 허용하지만, 대량 수집은 이용약관 위반이자 권리 침해입니다.",
                    "vi": "Cho phép truy cập dữ liệu thông thường qua API nhưng thu thập hàng loạt là vi phạm điều khoản sử dụng và xâm phạm quyền.",
                    "situation": "onsite"
                }
            ],
            "relatedTerms": ["편집저작물", "빅데이터", "웹크롤링", "정보수집"]
        },
        {
            "slug": "giong-cay-trong-moi",
            "korean": "식물신품종",
            "vietnamese": "Giống cây trồng mới",
            "hanja": "植物新品種",
            "hanjaReading": "植(심을 식) 物(만물 물) 新(새 신) 品(물건 품) 種(씨 종)",
            "pronunciation": "종 까이 쫑 머이",
            "meaningKo": "식물신품종은 식물학에 따른 최하위 분류 단위의 식물군으로서 유전적으로 조절되는 특성의 어느 하나 이상에 의해 다른 식물군과 구별되고, 변함없이 증식될 수 있는 것을 말하며, 품종보호 출원을 통해 육성자에게 독점적 권리를 부여합니다. 통역 시 주의할 점은 이는 특허나 상표와는 다른 독자적인 지적재산권 영역이며, 농업·원예 분야에서 신품종 개발에 대한 보상과 보호를 목적으로 한다는 점입니다. 베트남은 농업국가로서 식물신품종 보호가 중요하지만 아직 제도가 미흡하여 한국 종자회사가 진출 시 각별한 주의가 필요합니다.",
            "meaningVi": "Giống cây trồng mới là nhóm thực vật thuộc đơn vị phân loại thấp nhất theo thực vật học, được phân biệt với nhóm thực vật khác bằng một hoặc nhiều đặc tính di truyền có thể kiểm soát và có thể nhân giống một cách ổn định. Qua đơn đăng ký bảo hộ giống cây trồng, người tạo giống được cấp quyền độc quyền. Đây là lĩnh vực sở hữu trí tuệ độc lập khác với bằng sáng chế và nhãn hiệu, nhằm bảo vệ và đền bù cho việc phát triển giống mới trong nông nghiệp và làm vườn.",
            "context": "식물신품종보호법, 종자 계약, 농업 기술 이전",
            "culturalNote": "한국은 국립종자원을 통해 식물신품종 보호 제도를 체계적으로 운영하며, 딸기·장미 등 고부가가치 품종 개발에 적극적이고 해외 로열티 수입도 늘고 있습니다. 베트남은 농업 비중이 높지만 품종 보호 인식이 낮아 무단 증식이 만연하며, 한국 육종가들이 개발한 품종이 베트남에서 불법 재배되는 사례가 빈번합니다. 한국 종자 기업이 베트남에 진출할 때는 현지 품종보호 등록과 함께 계약 재배, 기술 이전 조건 등을 명확히 하여 권리를 보호해야 합니다.",
            "commonMistakes": [
                {
                    "mistake": "'품종'을 단순히 'loại' 또는 'chủng loại'로 번역",
                    "correction": "법률 용어로는 'giống' 또는 'giống cây trồng'",
                    "explanation": "'loại'는 일반적 종류이고, 식물신품종의 '품종'은 법적 개념인 'giống'으로 표현해야 합니다."
                },
                {
                    "mistake": "육성자(người tạo giống)와 재배자를 혼동",
                    "correction": "육성자는 품종을 개발한 자, 재배자는 단순 생산자로 권리 주체가 다름",
                    "explanation": "육성자만이 품종보호권을 가지며, 재배자는 허락을 받아 재배할 수 있을 뿐입니다."
                },
                {
                    "mistake": "'신규성'과 '구별성'을 혼용",
                    "correction": "신규성은 시판 여부, 구별성은 다른 품종과의 차이로 별개 요건",
                    "explanation": "품종보호는 신규성·구별성·균일성·안정성 4가지 요건을 모두 충족해야 하며 각각 다른 개념입니다."
                }
            ],
            "examples": [
                {
                    "ko": "당사가 개발한 신품종 딸기는 베트남에서도 품종보호 출원을 완료하여 무단 증식을 방지하고 있습니다.",
                    "vi": "Giống dâu tây mới do công ty chúng tôi phát triển đã hoàn tất đơn đăng ký bảo hộ giống cây trồng tại Việt Nam để ngăn chặn nhân giống trái phép.",
                    "situation": "formal"
                },
                {
                    "ko": "품종보호권자의 허락 없이 종자를 증식·판매하면 권리 침해로 법적 책임을 집니다.",
                    "vi": "Nếu nhân giống và bán hạt giống mà không có sự cho phép của người có quyền bảo hộ giống cây trồng sẽ phải chịu tr책nhiệm pháp lý về xâm phạm quyền.",
                    "situation": "formal"
                },
                {
                    "ko": "계약 재배 방식으로 종자를 공급하고 생산물을 전량 수매하여 품종이 유출되지 않도록 관리합니다.",
                    "vi": "Cung cấp hạt giống theo phương thức canh tác hợp đồng và thu mua toàn bộ sản phẩm để quản lý không để giống bị rò rỉ.",
                    "situation": "onsite"
                }
            ],
            "relatedTerms": ["육성자권", "품종보호", "종자산업", "로열티"]
        },
        {
            "slug": "quyen-bo-tri-mach-ban-dan",
            "korean": "반도체배치설계권",
            "vietnamese": "Quyền bố trí mạch bán dẫn",
            "hanja": "半導體配置設計權",
            "hanjaReading": "半(반 반) 導(인도할 도) 體(몸 체) 配(나눌 배) 置(둘 치) 設(베풀 설) 計(셀 계) 權(권세 권)",
            "pronunciation": "꾸엔 보 찌 맛 반 전",
            "meaningKo": "반도체배치설계권은 반도체집적회로의 회로 소자 및 그 소자를 연결하는 도선의 배치를 평면적 또는 입체적으로 표현한 것으로서, 창작성이 있는 배치설계를 보호하는 권리입니다. 통역 시 주의할 점은 이는 특허나 디자인과는 별개의 독자적 권리이며, 반도체 산업의 특성상 개발 비용은 높지만 모방은 쉽기 때문에 특별히 보호한다는 점을 설명해야 합니다. 한국은 세계적인 반도체 강국으로서 이 권리의 보호가 매우 중요하며, 베트남도 IT 산업 육성 과정에서 관련 제도를 도입하고 있음을 안내해야 합니다.",
            "meaningVi": "Quyền bố trí mạch bán dẫn là quyền bảo hộ bố trí mạch có tính sáng tạo, biểu hiện bằng mặt phẳng hoặc lập thể về cách sắp xếp các phần tử mạch của vi mạch tích hợp bán dẫn và dây dẫn kết nối các phần tử đó. Đây là quyền độc lập khác với bằng sáng chế và thiết kế, được bảo hộ đặc biệt vì đặc thù ngành bán dẫn là chi phí phát triển cao nhưng dễ bị sao chép.",
            "context": "반도체산업법, 반도체 설계 계약, 기술 보호",
            "culturalNote": "한국은 삼성·SK하이닉스 등 글로벌 반도체 기업을 보유하고 있어 배치설계권 보호가 국가 경쟁력과 직결되며, 산업스파이나 기술 유출에 매우 민감합니다. 베트남은 아직 반도체 산업이 초기 단계이지만 삼성 등 한국 기업의 생산기지가 있어 관련 법제를 정비 중입니다. 한국 반도체 기업이 베트남에서 생산 활동을 할 때는 핵심 설계 정보의 유출을 방지하기 위한 보안 체계가 필수이며, 현지 인력 교육 시에도 기밀유지 교육을 철저히 해야 합니다.",
            "commonMistakes": [
                {
                    "mistake": "'반도체'를 'chất bán dẫn'으로 번역",
                    "correction": "산업 용어로는 'bán dẫn' 또는 'chip bán dẫn'",
                    "explanation": "'chất bán dẫn'은 반도체 물질(재료)이고, 반도체 산업의 '반도체'는 'bán dẫn' 또는 'vi mạch bán dẫn'입니다."
                },
                {
                    "mistake": "배치설계(bố trí mạch)와 회로설계(thiết kế mạch)를 혼동",
                    "correction": "배치설계는 물리적 배열, 회로설계는 논리적 구조로 구분",
                    "explanation": "회로설계는 전기적 기능을 설계하는 것이고, 배치설계는 그것을 물리적으로 배치하는 것으로 다른 단계입니다."
                },
                {
                    "mistake": "'창작성'을 단순히 'tính sáng tạo'로만 번역",
                    "correction": "법적 요건임을 강조하여 'tính sáng tạo theo quy định pháp luật' 사용",
                    "explanation": "창작성은 법적 보호 요건이므로 단순한 독창성과 구별하여 법률상의 기준임을 명확히 해야 합니다."
                }
            ],
            "examples": [
                {
                    "ko": "당사의 반도체 배치설계는 등록을 완료하였으므로, 무단 복제 시 법적 조치를 취할 것입니다.",
                    "vi": "Bố trí mạch bán dẫn của công ty chúng tôi đã hoàn tất đăng ký nên nếu sao chép trái phép sẽ có biện pháp pháp lý.",
                    "situation": "formal"
                },
                {
                    "ko": "반도체 배치설계는 특허와 달리 등록 후 10년간 보호되며, 창작성 요건이 상대적으로 낮습니다.",
                    "vi": "Bố trí mạch bán dẫn khác với bằng sáng chế, được bảo hộ 10 năm sau đăng ký và yêu cầu tính sáng tạo tương đối thấp hơn.",
                    "situation": "formal"
                },
                {
                    "ko": "베트남 공장에서는 조립만 하고 핵심 배치설계 정보는 한국 본사에서만 관리합니다.",
                    "vi": "Tại nhà máy Việt Nam chỉ lắp ráp, thông tin bố trí mạch cốt lõi chỉ được quản lý tại trụ sở chính Hàn Quốc.",
                    "situation": "onsite"
                }
            ],
            "relatedTerms": ["집적회로", "반도체설계", "기술유출", "산업기밀"]
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
