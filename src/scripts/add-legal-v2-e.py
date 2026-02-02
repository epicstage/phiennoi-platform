#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
소비자보호/제품책임 법률 용어 추가 스크립트
Theme: Consumer Protection/Product Liability
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

# 새 용어 정의
new_terms = [
    {
        "slug": "quyen-loi-nguoi-tieu-dung",
        "korean": "소비자권익",
        "vietnamese": "quyền lợi người tiêu dùng",
        "hanja": "消費者權益",
        "hanjaReading": "消(消費할 소) + 費(費用 비) + 者(者 자) + 權(權利 권) + 益(利益 익)",
        "pronunciation": "꿘 러이 응으어이 띠에우 중",
        "meaningKo": "소비자가 상품이나 서비스를 구매·사용하는 과정에서 법적으로 보호받는 권리와 이익을 말합니다. 한국은 소비자기본법에서 안전권, 알 권리, 선택권, 의견반영권, 보상권, 교육권, 단체조직권, 안전한 환경에서 소비할 권리 등 8대 권리를 명시하고 있습니다. 베트남은 소비자권익보호법(Luật Bảo vệ quyền lợi người tiêu dùng)에서 정보제공권, 선택권, 안전권, 사생활권, 보상권 등을 규정합니다. 통역 시 양국의 소비자 보호 범위와 구제절차가 다르므로, 한국의 한국소비자원 같은 기관의 역할을 베트남의 Cục Cạnh tranh và Bảo vệ người tiêu dùng(경쟁·소비자보호국)와 비교 설명해야 합니다. 또한 한국의 집단소송제와 베트남의 소비자단체 소송제도의 차이를 명확히 구분해야 합니다.",
        "meaningVi": "Là các quyền và lợi ích được pháp luật bảo vệ trong quá trình người tiêu dùng mua sắm và sử dụng hàng hóa, dịch vụ. Luật Bảo vệ quyền lợi người tiêu dùng của Việt Nam quy định các quyền cơ bản như quyền được cung cấp thông tin, quyền lựa chọn, quyền an toàn, quyền riêng tư và quyền được bồi thường. Hàn Quốc có hệ thống 8 quyền cơ bản trong Luật cơ bản về người tiêu dùng, bao gồm cả quyền tổ chức đoàn thể và quyền tiêu dùng trong môi trường an toàn.",
        "context": "소비자보호법, 제품책임, 소비자분쟁조정, 소비자단체 소송",
        "culturalNote": "한국은 소비자 보호 의식이 높아 한국소비자원의 중재와 소비자단체의 활동이 활발하며, 집단소송제도도 도입되어 있습니다. 베트남은 소비자 보호 제도가 발전 중이며, 소비자 교육과 권리 인식이 상대적으로 낮은 편입니다. 한국에서는 소비자 불만을 1372 소비자상담센터에 신고하지만, 베트남에서는 시장관리국(Thanh tra Thị trường) 또는 경쟁·소비자보호국에 신고합니다. 한국의 소비자분쟁조정위원회와 베트남의 중재제도의 차이를 통역 시 명확히 설명해야 합니다.",
        "commonMistakes": [
            {
                "mistake": "quyền người tiêu dùng만 번역",
                "correction": "quyền lợi người tiêu dùng로 번역",
                "explanation": "'권익'은 권리(quyền)와 이익(lợi)을 모두 포함하는 개념이므로 'quyền lợi'로 번역해야 완전한 의미 전달"
            },
            {
                "mistake": "한국 소비자원을 Trung tâm người tiêu dùng로 번역",
                "correction": "Korea Consumer Agency 또는 고유명사로 유지",
                "explanation": "공식 기관명은 영문 또는 고유명사로 표기하고, 기능 설명 추가 필요"
            },
            {
                "mistake": "집단소송을 đơn kiện tập thể로 직역",
                "correction": "vụ kiện đại diện nhóm 또는 class action으로 설명",
                "explanation": "베트남 법체계에 집단소송 제도가 없으므로 개념 설명 필요"
            }
        ],
        "examples": [
            {
                "ko": "소비자권익이 침해된 경우 한국소비자원에 분쟁조정을 신청할 수 있습니다.",
                "vi": "Khi quyền lợi người tiêu dùng bị xâm phạm, có thể nộp đơn hòa giải tranh chấp tại Cơ quan Người tiêu dùng Hàn Quốc.",
                "situation": "formal"
            },
            {
                "ko": "이 제품은 소비자권익 보호를 위해 환불 가능 기간이 30일입니다.",
                "vi": "Sản phẩm này có thời hạn hoàn tiền 30 ngày để bảo vệ quyền lợi người tiêu dùng.",
                "situation": "onsite"
            },
            {
                "ko": "소비자권익 침해 사례를 신고하려면 1372로 전화하세요.",
                "vi": "Để báo cáo trường hợp xâm phạm quyền lợi người tiêu dùng, hãy gọi 1372.",
                "situation": "informal"
            }
        ],
        "relatedTerms": ["khieu-nai-nguoi-tieu-dung", "bao-hanh-san-pham", "hoan-tien"]
    },
    {
        "slug": "bao-hanh-san-pham",
        "korean": "제품보증",
        "vietnamese": "bảo hành sản phẩm",
        "hanja": "製品保證",
        "hanjaReading": "製(製作할 제) + 品(物品 품) + 保(保證 보) + 證(證明 증)",
        "pronunciation": "바오 한 산 팜",
        "meaningKo": "제조업체나 판매업체가 제품의 품질과 성능을 일정 기간 보증하고, 하자 발생 시 무상수리, 교환, 환불 등의 책임을 지는 제도입니다. 한국은 소비자기본법과 제품안전기본법에서 보증기간과 책임범위를 규정하며, 전자제품은 통상 1년, 가전제품은 2~3년의 보증기간이 일반적입니다. 베트남도 소비자권익보호법에서 보증의무를 규정하지만, 보증기간과 범위가 제품별로 다릅니다. 통역 시 한국의 '무상 AS'와 베트남의 'bảo hành miễn phí'가 동일 개념임을 명확히 하고, 보증서(phiếu bảo hành) 제출 요건, 사용자 과실 제외 조항 등을 정확히 전달해야 합니다. 또한 제조물책임(PL)과 보증책임의 차이를 구분해야 합니다.",
        "meaningVi": "Là chế độ nhà sản xuất hoặc nhà bán hàng cam kết chất lượng và hiệu suất của sản phẩm trong một thời gian nhất định, và chịu trách nhiệm sửa chữa miễn phí, đổi hàng hoặc hoàn tiền khi có lỗi. Luật Bảo vệ quyền lợi người tiêu dùng quy định nghĩa vụ bảo hành, nhưng thời hạn và phạm vi bảo hành khác nhau tùy sản phẩm. Bảo hành không bao gồm lỗi do người dùng gây ra.",
        "context": "제품 구매 계약, A/S 센터, 보증서 발급, 하자보수",
        "culturalNote": "한국은 AS 센터가 전국적으로 잘 구축되어 있고, 대형 제조사들은 신속한 A/S를 경쟁력으로 내세웁니다. 베트남은 도시 지역에는 A/S 센터가 있으나 농촌 지역은 접근성이 낮습니다. 한국에서는 보증서를 분실해도 구매 영수증으로 A/S를 받을 수 있지만, 베트남에서는 보증서(phiếu bảo hành)가 필수인 경우가 많습니다. 또한 한국의 '연장 보증'(bảo hành mở rộng) 개념이 베트남에서는 덜 일반적입니다.",
        "commonMistakes": [
            {
                "mistake": "bảo hiểm sản phẩm으로 번역",
                "correction": "bảo hành sản phẩm으로 번역",
                "explanation": "'bảo hiểm'은 보험이고, 'bảo hành'이 보증/워런티의 올바른 표현"
            },
            {
                "mistake": "무상 A/S를 dịch vụ miễn phí로만 번역",
                "correction": "bảo hành miễn phí 또는 sửa chữa miễn phí로 번역",
                "explanation": "A/S는 보증 범위 내 수리를 의미하므로 'bảo hành' 용어 사용 필요"
            },
            {
                "mistake": "보증기간을 thời gian đảm bảo로 번역",
                "correction": "thời hạn bảo hành로 번역",
                "explanation": "'thời hạn bảo hành'이 보증기간의 정확한 법률 용어"
            }
        ],
        "examples": [
            {
                "ko": "이 제품은 구매일로부터 2년간 무상 보증이 적용됩니다.",
                "vi": "Sản phẩm này được bảo hành miễn phí 2 năm kể từ ngày mua.",
                "situation": "formal"
            },
            {
                "ko": "보증서와 영수증을 가져오시면 A/S 센터에서 수리해 드립니다.",
                "vi": "Nếu mang phiếu bảo hành và hóa đơn, trung tâm bảo hành sẽ sửa chữa cho bạn.",
                "situation": "onsite"
            },
            {
                "ko": "사용자 과실로 인한 파손은 보증 범위에 포함되지 않습니다.",
                "vi": "Hư hỏng do lỗi người dùng không thuộc phạm vi bảo hành.",
                "situation": "formal"
            }
        ],
        "relatedTerms": ["trach-nhiem-san-pham", "thu-hoi-san-pham", "quyen-loi-nguoi-tieu-dung"]
    },
    {
        "slug": "hoan-tien",
        "korean": "환불",
        "vietnamese": "hoàn tiền",
        "hanja": "還拂",
        "hanjaReading": "還(還原할 환) + 拂(拂除 불)",
        "pronunciation": "호안 띠엔",
        "meaningKo": "구매자가 상품이나 서비스에 하자가 있거나 계약 해제 시 지불한 대금을 돌려받는 것을 말합니다. 한국은 전자상거래법에서 7일 이내 청약철회권을 보장하고, 제품 하자 시 환불을 소비자의 권리로 명시합니다. 방문판매법, 할부거래법 등도 환불 조항을 두고 있습니다. 베트남도 소비자권익보호법에서 환불권을 규정하지만, 온라인 쇼핑의 환불 정책이 판매자마다 다를 수 있습니다. 통역 시 한국의 '쿨링오프'(cooling-off) 제도와 베트남의 환불 정책 차이, 환불 가능 기간, 배송비 부담 주체, 중고품·맞춤제작품 환불 제외 등을 명확히 전달해야 합니다. 또한 환불과 교환(đổi hàng)의 차이를 구분하고, 부분 환불(hoàn tiền một phần) 개념도 설명해야 합니다.",
        "meaningVi": "Là việc người mua nhận lại số tiền đã thanh toán khi hàng hóa hoặc dịch vụ có lỗi hoặc khi hủy hợp đồng. Luật Bảo vệ quyền lợi người tiêu dùng quy định quyền hoàn tiền, nhưng chính sách hoàn tiền của mua sắm trực tuyến có thể khác nhau tùy người bán. Hoàn tiền khác với đổi hàng, và có thể là hoàn tiền toàn bộ hoặc một phần.",
        "context": "전자상거래, 청약철회, 계약 해제, 소비자 분쟁",
        "culturalNote": "한국은 온라인 쇼핑에서 7일 이내 '무조건 환불' 문화가 정착되어 있고, 대형 쇼핑몰들은 30일 환불 정책을 제공하기도 합니다. 베트남은 환불 정책이 판매자마다 다르고, 환불보다는 교환을 선호하는 경향이 있습니다. 한국에서는 단순 변심 환불도 가능하지만, 베트남에서는 제품 하자가 있어야 환불이 가능한 경우가 많습니다. 또한 한국의 '즉시 환불'과 베트남의 '검수 후 환불' 절차 차이를 통역 시 명확히 해야 합니다.",
        "commonMistakes": [
            {
                "mistake": "trả tiền lại로 번역",
                "correction": "hoàn tiền로 번역",
                "explanation": "'hoàn tiền'이 법률·상업 용어로 정확한 표현이며, 'trả tiền lại'는 구어체"
            },
            {
                "mistake": "청약철회를 hủy đơn hàng로만 번역",
                "correction": "quyền rút lại đơn đặt hàng 또는 hủy giao dịch로 번역",
                "explanation": "청약철회는 법적 권리이므로 'quyền'(권리)을 명시해야 함"
            },
            {
                "mistake": "쿨링오프를 직역",
                "correction": "quyền hủy giao dịch trong thời gian suy nghĩ로 설명",
                "explanation": "베트남에 쿨링오프 제도가 없으므로 개념 설명 필요"
            }
        ],
        "examples": [
            {
                "ko": "구매 후 7일 이내에는 이유 없이 환불을 요청할 수 있습니다.",
                "vi": "Trong vòng 7 ngày sau khi mua, bạn có thể yêu cầu hoàn tiền mà không cần lý do.",
                "situation": "formal"
            },
            {
                "ko": "제품에 하자가 있어서 환불 신청했는데, 언제 처리되나요?",
                "vi": "Tôi đã yêu cầu hoàn tiền vì sản phẩm có lỗi, khi nào sẽ được xử lý?",
                "situation": "informal"
            },
            {
                "ko": "환불 시 배송비는 판매자가 부담합니다.",
                "vi": "Khi hoàn tiền, phí vận chuyển do người bán chịu.",
                "situation": "formal"
            }
        ],
        "relatedTerms": ["quyen-loi-nguoi-tieu-dung", "bao-hanh-san-pham", "khieu-nai-nguoi-tieu-dung"]
    },
    {
        "slug": "khieu-nai-nguoi-tieu-dung",
        "korean": "소비자불만",
        "vietnamese": "khiếu nại người tiêu dùng",
        "hanja": "消費者不滿",
        "hanjaReading": "消(消費할 소) + 費(費用 비) + 者(者 자) + 不(不 불) + 滿(滿 만)",
        "pronunciation": "키에우 나이 응으어이 띠에우 중",
        "meaningKo": "소비자가 상품이나 서비스의 품질, 가격, 계약 조건 등에 불만을 제기하고 시정을 요구하는 행위를 말합니다. 한국은 소비자기본법에 따라 1372 소비자상담센터, 한국소비자원의 소비자분쟁조정위원회 등을 통해 불만을 접수하고 조정합니다. 베트남은 소비자권익보호법에서 불만 제기 절차를 규정하며, 시장관리국(Thanh tra Thị trường) 또는 경쟁·소비자보호국에 신고할 수 있습니다. 통역 시 한국의 소비자분쟁조정과 베트남의 중재(hòa giải) 절차의 차이, 분쟁 해결 기간, 조정 결정의 법적 효력 등을 명확히 전달해야 합니다. 또한 불만(khiếu nại)과 고소(tố cáo)의 차이를 구분해야 합니다.",
        "meaningVi": "Là hành vi người tiêu dùng đưa ra bất mãn về chất lượng, giá cả, điều kiện hợp đồng của hàng hóa hoặc dịch vụ và yêu cầu khắc phục. Luật Bảo vệ quyền lợi người tiêu dùng quy định thủ tục khiếu nại, có thể báo cáo với Thanh tra Thị trường hoặc Cục Cạnh tranh và Bảo vệ người tiêu dùng. Khiếu nại khác với tố cáo, và có thể được giải quyết qua hòa giải hoặc trọng tài.",
        "context": "소비자 분쟁, 소비자상담, 분쟁조정, 소비자보호",
        "culturalNote": "한국은 소비자 불만 제기가 활발하고, 1372 전화 한 통으로 신속하게 상담받을 수 있습니다. 소비자원의 분쟁조정은 무료이며, 조정 결정은 법적 구속력이 있습니다. 베트남은 소비자가 직접 판매자에게 불만을 제기하는 것이 우선이며, 해결되지 않으면 관련 기관에 신고합니다. 베트남의 소비자 불만 해결 절차가 한국보다 시간이 오래 걸릴 수 있으며, 조정보다는 법원 소송으로 가는 경우도 있습니다. 통역 시 양국의 분쟁 해결 문화 차이를 설명해야 합니다.",
        "commonMistakes": [
            {
                "mistake": "phàn nàn người tiêu dùng로 번역",
                "correction": "khiếu nại người tiêu dùng로 번역",
                "explanation": "'khiếu nại'는 공식적 불만 제기, 'phàn nàn'은 비공식적 불평"
            },
            {
                "mistake": "소비자상담센터를 Tư vấn người tiêu dùng로 번역",
                "correction": "Trung tâm tư vấn người tiêu dùng 1372로 번역",
                "explanation": "공식 기관명은 전체로 표기하고 핫라인 번호 포함"
            },
            {
                "mistake": "분쟁조정을 giải quyết tranh chấp로 번역",
                "correction": "hòa giải tranh chấp로 번역",
                "explanation": "'hòa giải'는 중재/조정의 정확한 법률 용어"
            }
        ],
        "examples": [
            {
                "ko": "제품 불량으로 소비자불만을 제기하려면 1372로 전화하세요.",
                "vi": "Để khiếu nại người tiêu dùng về sản phẩm lỗi, hãy gọi 1372.",
                "situation": "formal"
            },
            {
                "ko": "소비자불만이 접수되면 14일 이내에 조정 결과를 통보합니다.",
                "vi": "Khi nhận được khiếu nại người tiêu dùng, kết quả hòa giải sẽ được thông báo trong 14 ngày.",
                "situation": "formal"
            },
            {
                "ko": "판매자와 협의가 안 되면 소비자원에 불만을 제기할 수 있습니다.",
                "vi": "Nếu không thỏa thuận được với người bán, bạn có thể khiếu nại với Cơ quan Người tiêu dùng.",
                "situation": "informal"
            }
        ],
        "relatedTerms": ["quyen-loi-nguoi-tieu-dung", "hoan-tien", "trach-nhiem-san-pham"]
    },
    {
        "slug": "trach-nhiem-san-pham",
        "korean": "제조물책임",
        "vietnamese": "trách nhiệm sản phẩm",
        "hanja": "製造物責任",
        "hanjaReading": "製(製作할 제) + 造(造作 조) + 物(物 물) + 責(責任 책) + 任(任 임)",
        "pronunciation": "짝 니엠 산 팜",
        "meaningKo": "제조업체가 제조·설계·표시상의 결함으로 인해 소비자에게 발생한 생명·신체·재산상의 손해에 대해 지는 법적 책임을 말합니다. 한국은 제조물책임법(PL법)에서 무과실책임 원칙을 채택하여, 제조업체의 고의·과실을 입증하지 않아도 결함만 입증하면 배상받을 수 있습니다. 베트남은 2008년부터 PL 제도를 도입했으며, 민법과 소비자권익보호법에서 제조물책임을 규정합니다. 통역 시 한국과 베트남의 입증책임 차이, 결함의 3가지 유형(제조·설계·표시상 결함), 면책 사유, 손해배상 범위 등을 명확히 전달해야 합니다. 또한 PL 보험(bảo hiểm trách nhiệm sản phẩm) 가입 의무와 리콜 제도의 연관성도 설명해야 합니다.",
        "meaningVi": "Là trách nhiệm pháp lý của nhà sản xuất đối với thiệt hại về tính mạng, sức khỏe, tài sản của người tiêu dùng do lỗi sản xuất, thiết kế hoặc ghi nhãn sản phẩm. Luật dân sự và Luật Bảo vệ quyền lợi người tiêu dùng của Việt Nam quy định trách nhiệm sản phẩm, áp dụng nguyên tắc trách nhiệm không lỗi, nghĩa là không cần chứng minh cố ý hoặc lỗi của nhà sản xuất, chỉ cần chứng minh lỗi sản phẩm.",
        "context": "제조물책임법, 결함 제품, 손해배상, PL 보험",
        "culturalNote": "한국은 2002년 제조물책임법 시행 이후 PL 사고에 대한 인식이 높아졌고, 대형 제조사들은 PL 보험에 가입합니다. 베트남은 PL 제도가 상대적으로 덜 알려져 있으며, 소비자가 제조업체를 상대로 소송하는 것이 한국보다 어렵습니다. 한국에서는 한국소비자원이 PL 사고 조사·중재를 지원하지만, 베트남에서는 소비자가 직접 입증 자료를 준비해야 합니다. 통역 시 양국의 PL 제도 성숙도 차이를 고려해야 합니다.",
        "commonMistakes": [
            {
                "mistake": "trách nhiệm sản xuất로 번역",
                "correction": "trách nhiệm sản phẩm로 번역",
                "explanation": "'제조물책임'은 제조 과정이 아닌 제품 자체의 결함 책임이므로 'sản phẩm' 사용"
            },
            {
                "mistake": "무과실책임을 không lỗi로만 번역",
                "correction": "trách nhiệm không lỗi 또는 nghĩa vụ bồi thường không phụ thuộc lỗi로 번역",
                "explanation": "법률 개념이므로 'trách nhiệm'(책임) 용어 필요"
            },
            {
                "mistake": "PL 보험을 bảo hiểm sản xuất로 번역",
                "correction": "bảo hiểm trách nhiệm sản phẩm로 번역",
                "explanation": "Product Liability Insurance의 정확한 번역"
            }
        ],
        "examples": [
            {
                "ko": "이 제품의 설계 결함으로 인해 화재가 발생했다면 제조물책임을 물을 수 있습니다.",
                "vi": "Nếu hỏa hoạn xảy ra do lỗi thiết kế sản phẩm này, có thể truy cứu trách nhiệm sản phẩm.",
                "situation": "formal"
            },
            {
                "ko": "제조물책임법에 따라 소비자는 제조업체의 과실을 입증할 필요가 없습니다.",
                "vi": "Theo Luật trách nhiệm sản phẩm, người tiêu dùng không cần chứng minh lỗi của nhà sản xuất.",
                "situation": "formal"
            },
            {
                "ko": "대형 제조사들은 제조물책임 사고에 대비해 PL 보험에 가입합니다.",
                "vi": "Các nhà sản xuất lớn tham gia bảo hiểm trách nhiệm sản phẩm để phòng ngừa tai nạn PL.",
                "situation": "onsite"
            }
        ],
        "relatedTerms": ["bao-hanh-san-pham", "thu-hoi-san-pham", "quyen-loi-nguoi-tieu-dung"]
    },
    {
        "slug": "thu-hoi-san-pham",
        "korean": "리콜",
        "vietnamese": "thu hồi sản phẩm",
        "hanja": None,
        "hanjaReading": None,
        "pronunciation": "투 호이 산 팜",
        "meaningKo": "제품의 결함이나 안전 문제로 인해 제조업체나 유통업체가 이미 판매된 제품을 회수·수리·교환·환불하는 조치를 말합니다. 한국은 제품안전기본법과 제조물책임법에서 리콜 의무를 규정하며, 자발적 리콜(voluntary recall)과 강제 리콜(mandatory recall)로 구분합니다. 한국소비자원과 공정거래위원회가 리콜을 관리·감독하며, 리콜 정보는 소비자24(www.consumer.go.kr)에 공개됩니다. 베트남도 제품품질법과 소비자권익보호법에서 리콜 제도를 규정하며, 과학기술부가 관리합니다. 통역 시 리콜 절차, 소비자 통지 방법, 리콜 비용 부담 주체, 리콜 불응 시 처벌 등을 명확히 전달해야 합니다. 또한 리콜과 단순 교환·환불의 차이를 구분해야 합니다.",
        "meaningVi": "Là biện pháp nhà sản xuất hoặc nhà phân phối thu hồi, sửa chữa, đổi hoặc hoàn tiền sản phẩm đã bán do lỗi hoặc vấn đề an toàn. Luật Chất lượng sản phẩm và Luật Bảo vệ quyền lợi người tiêu dùng quy định nghĩa vụ thu hồi, phân biệt thu hồi tự nguyện và thu hồi bắt buộc. Bộ Khoa học và Công nghệ quản lý việc thu hồi sản phẩm.",
        "context": "제품 안전, 결함 제품, 제조물책임, 소비자 보호",
        "culturalNote": "한국은 리콜 제도가 잘 정착되어 있으며, 자동차·가전제품·식품 등에서 빈번하게 리콜이 발생합니다. 소비자는 리콜 공지를 받으면 무상으로 수리·교환을 받을 수 있습니다. 베트남은 리콜 제도가 있지만, 제조사의 자발적 리콜이 덜 활발하고, 소비자 인식도 낮은 편입니다. 한국의 리콜 정보 공개 시스템과 베트남의 정보 접근성 차이를 통역 시 설명해야 합니다. 또한 한국의 '사전 예방적 리콜' 문화와 베트남의 '사후 조치' 문화 차이를 고려해야 합니다.",
        "commonMistakes": [
            {
                "mistake": "triệu hồi sản phẩm로 번역",
                "correction": "thu hồi sản phẩm로 번역",
                "explanation": "'thu hồi'가 제품 회수의 정확한 표현이며, 'triệu hồi'는 사람 소환"
            },
            {
                "mistake": "리콜을 đổi trả로 번역",
                "correction": "thu hồi hoặc recall로 번역",
                "explanation": "리콜은 안전 문제로 인한 대규모 회수이며, 단순 교환·환불과 다름"
            },
            {
                "mistake": "자발적 리콜을 tự động thu hồi로 번역",
                "correction": "thu hồi tự nguyện로 번역",
                "explanation": "'tự nguyện'이 자발적의 정확한 표현이며, 'tự động'은 자동"
            }
        ],
        "examples": [
            {
                "ko": "이 자동차 모델은 브레이크 결함으로 인해 리콜 조치가 내려졌습니다.",
                "vi": "Mẫu xe này đã bị thu hồi sản phẩm do lỗi phanh.",
                "situation": "formal"
            },
            {
                "ko": "제조사는 리콜 대상 제품 소유자에게 개별 통지해야 합니다.",
                "vi": "Nhà sản xuất phải thông báo riêng cho chủ sở hữu sản phẩm bị thu hồi.",
                "situation": "formal"
            },
            {
                "ko": "리콜 비용은 전액 제조사가 부담하며, 소비자는 무상으로 수리받을 수 있습니다.",
                "vi": "Chi phí thu hồi do nhà sản xuất chịu toàn bộ, người tiêu dùng được sửa chữa miễn phí.",
                "situation": "onsite"
            }
        ],
        "relatedTerms": ["trach-nhiem-san-pham", "bao-hanh-san-pham", "quyen-loi-nguoi-tieu-dung"]
    },
    {
        "slug": "quang-cao-sai-su-that",
        "korean": "허위광고",
        "vietnamese": "quảng cáo sai sự thật",
        "hanja": "虛僞廣告",
        "hanjaReading": "虛(虛 허) + 僞(僞 위) + 廣(廣 광) + 告(告 고)",
        "pronunciation": "꽝 까오 사이 쓰 텃",
        "meaningKo": "상품이나 서비스의 내용, 거래 조건 등에 관하여 소비자를 속이거나 소비자로 하여금 잘못 알게 하는 광고를 말합니다. 한국은 표시·광고의 공정화에 관한 법률(표시광고법)에서 허위·과장 광고를 규제하며, 공정거래위원회가 단속·처벌합니다. 위반 시 시정명령, 과징금, 형사처벌이 가능합니다. 베트남도 광고법(Luật Quảng cáo)에서 허위광고를 금지하며, 경쟁관리국이 관리합니다. 통역 시 허위광고와 과장광고(quảng cáo phóng đại), 비교광고(quảng cáo so sánh)의 차이를 명확히 하고, 증거 자료 요구, 소비자 피해 구제 절차 등을 정확히 전달해야 합니다. 또한 온라인 광고(인플루언서, 바이럴 마케팅)의 허위광고 규제 강화 추세도 설명해야 합니다.",
        "meaningVi": "Là quảng cáo lừa dối hoặc gây hiểu nhầm cho người tiêu dùng về nội dung, điều kiện giao dịch của hàng hóa hoặc dịch vụ. Luật Quảng cáo của Việt Nam cấm quảng cáo sai sự thật, do Cục Quản lý cạnh tranh quản lý. Khi vi phạm, có thể bị lệnh chỉnh sửa, phạt tiền và xử lý hình sự. Quảng cáo sai sự thật khác với quảng cáo phóng đại và quảng cáo so sánh.",
        "context": "광고 규제, 소비자 보호, 공정거래, 표시광고법",
        "culturalNote": "한국은 허위광고에 대한 규제와 처벌이 엄격하며, 공정위가 적극적으로 단속합니다. 특히 건강기능식품, 의료기기, 부동산 광고에서 허위·과장 광고가 빈번하게 적발됩니다. 베트남도 허위광고를 규제하지만, 집행이 상대적으로 덜 엄격합니다. 한국에서는 소비자가 허위광고로 피해를 입으면 손해배상을 청구할 수 있지만, 베트남에서는 입증이 어렵습니다. 통역 시 양국의 광고 규제 수준과 소비자 보호 문화 차이를 설명해야 합니다.",
        "commonMistakes": [
            {
                "mistake": "quảng cáo giả로 번역",
                "correction": "quảng cáo sai sự thật로 번역",
                "explanation": "'giả'는 가짜 제품을 의미하며, 허위광고는 'sai sự thật'(사실과 다름)"
            },
            {
                "mistake": "과장광고를 quảng cáo sai로 번역",
                "correction": "quảng cáo phóng đại로 번역",
                "explanation": "허위광고(sai sự thật)와 과장광고(phóng đại)는 구분되는 개념"
            },
            {
                "mistake": "공정거래위원회를 Ủy ban giao dịch công bằng로 번역",
                "correction": "Ủy ban Cạnh tranh và Người tiêu dùng 또는 Korea Fair Trade Commission로 번역",
                "explanation": "공식 기관명은 영문 또는 정확한 베트남어 명칭 사용"
            }
        ],
        "examples": [
            {
                "ko": "이 제품의 효과를 과대 포장한 허위광고로 적발되어 과징금이 부과되었습니다.",
                "vi": "Quảng cáo sai sự thật phóng đại hiệu quả sản phẩm này đã bị phát hiện và bị phạt tiền.",
                "situation": "formal"
            },
            {
                "ko": "허위광고로 인해 피해를 입은 소비자는 손해배상을 청구할 수 있습니다.",
                "vi": "Người tiêu dùng bị thiệt hại do quảng cáo sai sự thật có thể yêu cầu bồi thường.",
                "situation": "formal"
            },
            {
                "ko": "인플루언서가 협찬받고 허위 리뷰를 올리면 표시광고법 위반입니다.",
                "vi": "Nếu influencer nhận tài trợ và đăng đánh giá sai sự thật, đó là vi phạm Luật Quảng cáo.",
                "situation": "informal"
            }
        ],
        "relatedTerms": ["quyen-loi-nguoi-tieu-dung", "hop-dong-mau", "tieu-chuan-chat-luong"]
    },
    {
        "slug": "hop-dong-mau",
        "korean": "약관",
        "vietnamese": "hợp đồng mẫu",
        "hanja": "約款",
        "hanjaReading": "約(約束 약) + 款(款式 관)",
        "pronunciation": "헙 동 머우",
        "meaningKo": "사업자가 다수의 고객과 계약을 체결하기 위해 미리 작성한 정형화된 계약 조건을 말합니다. 한국은 약관의 규제에 관한 법률(약관법)에서 약관의 작성, 명시·설명의무, 불공정약관의 무효 등을 규정합니다. 특히 고객에게 부당하게 불리한 조항, 면책조항, 손해배상 제한 조항 등은 무효로 봅니다. 베트남도 민법에서 표준계약서(hợp đồng mẫu) 사용을 인정하지만, 한국만큼 엄격한 규제는 없습니다. 통역 시 약관 동의 절차, 명시·설명의무, 불공정약관 판단 기준, 약관 변경 시 통지 의무 등을 명확히 전달해야 합니다. 또한 온라인 서비스의 '이용약관'(điều khoản sử dụng)과 일반 계약 약관의 차이도 설명해야 합니다.",
        "meaningVi": "Là điều kiện hợp đồng định sẵn mà doanh nghiệp soạn trước để ký kết với nhiều khách hàng. Luật dân sự Việt Nam công nhận việc sử dụng hợp đồng mẫu, nhưng quy định không nghiêm ngặt như Hàn Quốc. Các điều khoản bất lợi, điều khoản miễn trừ trách nhiệm, điều khoản hạn chế bồi thường có thể bị coi là vô hiệu nếu bất công.",
        "context": "계약법, 소비자 보호, 이용약관, 약관 규제",
        "culturalNote": "한국은 약관 규제가 엄격하여, 사업자는 중요한 약관 조항을 명시하고 설명해야 하며, 고객이 이해하지 못하면 계약이 무효가 될 수 있습니다. 온라인 서비스에서 '약관 동의' 체크박스가 필수이며, 약관 변경 시 사전 통지가 의무입니다. 베트남은 약관에 대한 인식이 상대적으로 낮으며, 소비자가 약관을 꼼꼼히 읽지 않는 경향이 있습니다. 통역 시 약관의 법적 효력과 소비자 권리를 강조해야 합니다.",
        "commonMistakes": [
            {
                "mistake": "điều khoản로만 번역",
                "correction": "hợp đồng mẫu 또는 điều khoản chuẩn로 번역",
                "explanation": "'약관'은 단순 조항(điều khoản)이 아닌 정형화된 계약(hợp đồng mẫu)"
            },
            {
                "mistake": "이용약관을 hợp đồng sử dụng로 번역",
                "correction": "điều khoản sử dụng로 번역",
                "explanation": "온라인 서비스 약관은 'điều khoản sử dụng'가 관용적 표현"
            },
            {
                "mistake": "불공정약관을 hợp đồng không công bằng로 번역",
                "correction": "điều khoản bất lợi 또는 điều khoản không công bằng로 번역",
                "explanation": "약관 자체가 아닌 약관 내 조항이 불공정한 것"
            }
        ],
        "examples": [
            {
                "ko": "이 약관은 소비자에게 부당하게 불리하여 무효입니다.",
                "vi": "Hợp đồng mẫu này bất lợi một cách không công bằng cho người tiêu dùng nên vô hiệu.",
                "situation": "formal"
            },
            {
                "ko": "회사는 약관을 변경할 경우 7일 전에 고객에게 통지해야 합니다.",
                "vi": "Công ty phải thông báo cho khách hàng trước 7 ngày khi thay đổi hợp đồng mẫu.",
                "situation": "formal"
            },
            {
                "ko": "이용약관에 동의하지 않으면 서비스를 이용할 수 없습니다.",
                "vi": "Nếu không đồng ý với điều khoản sử dụng, bạn không thể sử dụng dịch vụ.",
                "situation": "informal"
            }
        ],
        "relatedTerms": ["dieu-khoan-bat-loi", "quyen-loi-nguoi-tieu-dung", "hop-dong-mau"]
    },
    {
        "slug": "dieu-khoan-bat-loi",
        "korean": "불공정약관",
        "vietnamese": "điều khoản bất lợi",
        "hanja": "不公正約款",
        "hanjaReading": "不(不 불) + 公(公平 공) + 正(正義 정) + 約(約束 약) + 款(款式 관)",
        "pronunciation": "디에우 코안 밧 러이",
        "meaningKo": "약관 중에서 소비자에게 부당하게 불리하거나 공정성을 잃은 조항을 말합니다. 한국은 약관의 규제에 관한 법률에서 불공정약관의 유형을 구체적으로 열거하며, 이러한 조항은 무효로 봅니다. 대표적인 예로는 사업자의 손해배상책임을 면제·제한하는 조항, 소비자의 권리를 부당하게 제한하는 조항, 계약 해지권을 제한하는 조항 등이 있습니다. 공정거래위원회는 불공정약관을 심사하고 시정명령을 내릴 수 있습니다. 베트남도 민법에서 불공정 조항을 규제하지만, 한국처럼 세부적이지는 않습니다. 통역 시 불공정약관의 유형, 무효 효과, 입증책임, 약관 심사 절차 등을 명확히 전달해야 합니다. 또한 소비자가 불공정약관에 서명했더라도 무효라는 점을 강조해야 합니다.",
        "meaningVi": "Là điều khoản trong hợp đồng mẫu bất lợi một cách không công bằng cho người tiêu dùng hoặc mất tính công bằng. Luật Hàn Quốc liệt kê cụ thể các loại điều khoản bất lợi và coi chúng là vô hiệu. Ví dụ điển hình là điều khoản miễn trừ hoặc hạn chế trách nhiệm bồi thường của doanh nghiệp, điều khoản hạn chế quyền của người tiêu dùng một cách không hợp lý, điều khoản hạn chế quyền hủy hợp đồng. Ngay cả khi người tiêu dùng đã ký vào điều khoản bất lợi, điều khoản đó vẫn vô hiệu.",
        "context": "약관 규제, 소비자 보호, 계약법, 공정거래",
        "culturalNote": "한국은 불공정약관에 대한 규제가 매우 엄격하며, 공정위가 주요 업종의 약관을 정기적으로 심사합니다. 특히 보험, 통신, 금융, 온라인 플랫폼의 약관이 집중 관리됩니다. 베트남은 불공정 조항 규제가 있지만, 집행이 상대적으로 덜 엄격하며, 소비자가 불공정 조항을 인지하지 못하는 경우가 많습니다. 한국에서는 소비자가 불공정약관을 이유로 계약 무효를 주장할 수 있지만, 베트남에서는 입증이 어렵습니다. 통역 시 양국의 약관 규제 수준 차이를 설명해야 합니다.",
        "commonMistakes": [
            {
                "mistake": "điều khoản không công bằng로 번역",
                "correction": "điều khoản bất lợi로 번역",
                "explanation": "'bất lợi'가 소비자에게 불리함을 더 명확히 표현하는 법률 용어"
            },
            {
                "mistake": "면책조항을 điều khoản miễn phí로 번역",
                "correction": "điều khoản miễn trừ trách nhiệm로 번역",
                "explanation": "'miễn phí'는 무료이고, 'miễn trừ trách nhiệm'이 면책의 정확한 표현"
            },
            {
                "mistake": "약관 무효를 hủy hợp đồng로 번역",
                "correction": "vô hiệu điều khoản로 번역",
                "explanation": "약관 일부가 무효인 것이지 계약 전체가 취소되는 것이 아님"
            }
        ],
        "examples": [
            {
                "ko": "이 조항은 소비자의 손해배상청구권을 부당하게 제한하여 불공정약관으로 무효입니다.",
                "vi": "Điều khoản này hạn chế không hợp lý quyền yêu cầu bồi thường của người tiêu dùng nên là điều khoản bất lợi và vô hiệu.",
                "situation": "formal"
            },
            {
                "ko": "공정위는 통신사의 불공정약관을 시정하라고 명령했습니다.",
                "vi": "Ủy ban Cạnh tranh đã ra lệnh sửa đổi điều khoản bất lợi của công ty viễn thông.",
                "situation": "formal"
            },
            {
                "ko": "불공정약관에 동의했더라도 법적으로 무효이므로 보호받을 수 있습니다.",
                "vi": "Ngay cả khi đã đồng ý với điều khoản bất lợi, vẫn được bảo vệ vì nó vô hiệu về mặt pháp lý.",
                "situation": "onsite"
            }
        ],
        "relatedTerms": ["hop-dong-mau", "quyen-loi-nguoi-tieu-dung", "quang-cao-sai-su-that"]
    },
    {
        "slug": "tieu-chuan-chat-luong",
        "korean": "품질기준",
        "vietnamese": "tiêu chuẩn chất lượng",
        "hanja": "品質基準",
        "hanjaReading": "品(品質 품) + 質(質 질) + 基(基礎 기) + 準(準則 준)",
        "pronunciation": "띠에우 쭌 찟 르엉",
        "meaningKo": "제품이나 서비스가 갖추어야 할 품질 수준을 정한 기준을 말합니다. 한국은 산업표준화법에 따라 한국산업표준(KS, Korean Industrial Standards)을 제정하고, 식품의약품안전처, 국가기술표준원 등이 품질기준을 관리합니다. 국제표준화기구(ISO) 기준도 널리 채택됩니다. 베트남은 제품품질법(Luật Chất lượng sản phẩm)과 표준·계량법에서 품질기준을 규정하며, 과학기술부가 TCVN(Tiêu chuẩn Việt Nam, 베트남 국가표준)을 관리합니다. 통역 시 한국의 KS 인증과 베트남의 CR 인증(Chứng nhận hợp chuẩn) 제도의 차이, 강제인증과 자율인증의 구분, 수입 제품의 품질기준 적합성 검사 절차 등을 명확히 전달해야 합니다. 또한 품질기준 미달 시 제재 내용도 설명해야 합니다.",
        "meaningVi": "Là tiêu chuẩn quy định mức chất lượng mà sản phẩm hoặc dịch vụ phải đạt được. Luật Chất lượng sản phẩm và Luật Tiêu chuẩn và Đo lường quy định tiêu chuẩn chất lượng, do Bộ Khoa học và Công nghệ quản lý TCVN (Tiêu chuẩn Việt Nam). Hàn Quốc có hệ thống KS (Korean Industrial Standards), và tiêu chuẩn ISO cũng được áp dụng rộng rãi. Có sự khác biệt giữa chứng nhận bắt buộc và chứng nhận tự nguyện.",
        "context": "제품 인증, 품질 관리, 표준화, 수출입 검사",
        "culturalNote": "한국은 KS 인증 제도가 잘 정착되어 있으며, 소비자들이 KS 마크를 신뢰합니다. ISO 9001(품질경영), ISO 14001(환경경영) 등 국제 인증도 널리 사용됩니다. 베트남도 TCVN 표준을 운영하지만, 한국만큼 인증 제도가 활성화되지는 않았습니다. 수출입 제품은 양국 모두 품질기준 적합성 검사를 받아야 하며, 식품·의약품·전자제품 등은 강제인증 대상입니다. 통역 시 양국의 인증 제도와 상호 인정 협정(MRA) 여부를 확인해야 합니다.",
        "commonMistakes": [
            {
                "mistake": "tiêu chuẩn chất로만 번역",
                "correction": "tiêu chuẩn chất lượng로 번역",
                "explanation": "'chất lượng'(품질)이 완전한 단어이며, 'chất'만으로는 의미 불완전"
            },
            {
                "mistake": "KS 인증을 chứng nhận KS로 번역",
                "correction": "chứng nhận KS (Tiêu chuẩn Công nghiệp Hàn Quốc)로 번역",
                "explanation": "약어 뒤에 풀네임을 괄호로 설명 추가 필요"
            },
            {
                "mistake": "품질기준 미달을 không đạt tiêu chuẩn로 번역",
                "correction": "không đạt tiêu chuẩn chất lượng로 번역",
                "explanation": "정확한 법률 용어 사용 필요"
            }
        ],
        "examples": [
            {
                "ko": "이 제품은 KS 품질기준을 충족하여 인증을 받았습니다.",
                "vi": "Sản phẩm này đã được chứng nhận vì đáp ứng tiêu chuẩn chất lượng KS.",
                "situation": "formal"
            },
            {
                "ko": "수입 식품은 한국 식품안전기준에 맞는지 검사를 받아야 합니다.",
                "vi": "Thực phẩm nhập khẩu phải được kiểm tra xem có đáp ứng tiêu chuẩn an toàn thực phẩm Hàn Quốc không.",
                "situation": "formal"
            },
            {
                "ko": "품질기준 미달 제품은 판매가 금지되고 회수 조치됩니다.",
                "vi": "Sản phẩm không đạt tiêu chuẩn chất lượng bị cấm bán và thu hồi.",
                "situation": "onsite"
            }
        ],
        "relatedTerms": ["trach-nhiem-san-pham", "thu-hoi-san-pham", "bao-hanh-san-pham"]
    }
]

# 중복 제거
new_terms_filtered = [t for t in new_terms if t['slug'] not in existing_slugs]

# 데이터 추가
data.extend(new_terms_filtered)

# 파일 저장
with open(file_path, 'w', encoding='utf-8') as f:
    json.dump(data, f, ensure_ascii=False, indent=2)

print(f"✅ {len(new_terms_filtered)}개 용어 추가 완료")
print(f"📊 전체 용어 수: {len(data)}개")
