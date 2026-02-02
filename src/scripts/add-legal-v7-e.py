#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""소비자보호법 심화 용어 추가 스크립트 (v7-e)"""

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
            "slug": "tap-doan-to-tung",
            "korean": "집단소송",
            "vietnamese": "Tập đoàn tố tụng",
            "hanja": "集團訴訟",
            "hanjaReading": "集(모을 집) 團(둥글 단) 訴(하소연할 소) 訟(송사 송)",
            "pronunciation": "땁 도안 또 뚱",
            "meaningKo": "다수의 피해자가 공통의 소송 원인에 대하여 공동으로 제기하는 소송을 의미합니다. 통역 시 '대표소송(đại diện tố tụng)'과 구분해야 하며, 베트남에서는 아직 제도화가 미흡하여 개념 차이를 명확히 설명해야 합니다. 한국은 증권관련집단소송법, 소비자기본법상 단체소송 등이 존재하나, 베트남은 주로 개별 소송으로 진행되므로 통역 시 제도적 차이를 보충 설명하는 것이 중요합니다. 소비자 피해 사건에서 자주 등장하는 용어입니다.",
            "meaningVi": "Vụ kiện do nhiều người bị hại cùng khởi kiện chung về một nguyên nhân giống nhau. Khác với đại diện tố tụng (một người đại diện nhóm), tập đoàn tố tụng là nhiều người cùng tham gia. Tại Việt Nam chưa có chế độ rõ ràng như Hàn Quốc (Luật tập đoàn tố tụng chứng khoán, tố tụng đoàn thể theo Luật bảo vệ người tiêu dùng). Người phiên dịch cần giải thích sự khác biệt về chế độ pháp lý hai nước.",
            "context": "소비자 집단 피해 구제, 증권 소송",
            "culturalNote": "한국은 2005년 증권관련집단소송법 시행 이후 제도화되었으나, 베트남은 아직 명시적인 집단소송 제도가 없어 대부분 개별 소송으로 진행됩니다. 통역 시 한국 의뢰인이 집단소송 경험을 언급할 경우, 베트남에서는 동일한 절차가 불가능함을 안내해야 합니다. 법률 제도의 발전 단계 차이를 인식하고 통역해야 합니다.",
            "commonMistakes": [
                {
                    "mistake": "Kiện tập thể",
                    "correction": "Tập đoàn tố tụng",
                    "explanation": "'Kiện tập thể'는 구어체이며 법률 용어로는 부정확합니다. 'Tập đoàn tố tụng'이 정확한 법률 용어입니다."
                },
                {
                    "mistake": "Đại diện tố tụng으로 번역",
                    "correction": "Tập đoàn tố tụng",
                    "explanation": "대표소송(đại diện tố tụng)은 한 명이 대표하는 것이고, 집단소송은 다수가 함께 참여하는 것으로 개념이 다릅니다."
                },
                {
                    "mistake": "베트남에도 동일한 제도가 있다고 통역",
                    "correction": "제도 차이를 명시적으로 설명",
                    "explanation": "베트남은 집단소송 제도가 아직 미비하므로, 한국과 동일한 절차로 오해되지 않도록 주의해야 합니다."
                }
            ],
            "examples": [
                {
                    "ko": "불량 제품으로 피해를 입은 소비자들이 집단소송을 제기했습니다.",
                    "vi": "Những người tiêu dùng bị thiệt hại do sản phẩm lỗi đã khởi kiện tập đoàn tố tụng.",
                    "situation": "formal"
                },
                {
                    "ko": "집단소송 제도가 없어서 개별적으로 소송을 진행해야 합니다.",
                    "vi": "Vì không có chế độ tập đoàn tố tụng nên phải tiến hành kiện riêng lẻ.",
                    "situation": "formal"
                },
                {
                    "ko": "한국에서는 증권 관련 집단소송이 가능합니다.",
                    "vi": "Tại Hàn Quốc có thể tiến hành tập đoàn tố tụng liên quan đến chứng khoán.",
                    "situation": "formal"
                }
            ],
            "relatedTerms": ["대표소송", "단체소송", "소비자기본법", "증권관련집단소송법"]
        },
        {
            "slug": "thu-hoi-san-pham",
            "korean": "리콜",
            "vietnamese": "Thu hồi sản phẩm",
            "hanja": None,
            "hanjaReading": None,
            "pronunciation": "투 호이 산 팜",
            "meaningKo": "결함이 있는 제품을 제조업체나 판매업체가 회수하여 수리, 교환, 환불하는 제도입니다. 통역 시 '회수(thu hồi)'와 혼동되지 않도록 '리콜 제도(chế độ thu hồi sản phẩm)'로 명확히 표현해야 합니다. 한국은 자동차, 식품, 의약품 등에서 리콜 제도가 활발히 운영되며, 베트남도 최근 강화되고 있으나 집행 수준에 차이가 있습니다. 통역 시 자발적 리콜과 강제 리콜의 구분, 리콜 비용 부담 주체 등을 정확히 전달해야 합니다.",
            "meaningVi": "Chế độ thu hồi sản phẩm có lỗi do nhà sản xuất hoặc nhà bán hàng để sửa chữa, đổi mới hoặc hoàn tiền. Tại Hàn Quốc, chế độ thu hồi được vận hành tích cực trong ô tô, thực phẩm, dược phẩm. Việt Nam cũng đang tăng cường gần đây nhưng có sự khác biệt về mức độ thực thi. Cần phân biệt thu hồi tự nguyện và thu hồi bắt buộc khi phiên dịch.",
            "context": "제조물 책임, 소비자 안전",
            "culturalNote": "한국은 리콜 제도가 법적으로 강력하게 집행되며, 자동차 리콜의 경우 공개적으로 공지되고 소비자 보상이 체계적으로 이루어집니다. 베트남도 리콜 제도가 있으나 소비자 인식과 기업의 자발적 참여가 상대적으로 낮은 편입니다. 통역 시 한국 기업이 베트남에서 리콜을 진행할 때의 법적 의무와 절차를 정확히 안내해야 합니다.",
            "commonMistakes": [
                {
                    "mistake": "Thu hồi만 사용",
                    "correction": "Thu hồi sản phẩm 또는 Lệnh thu hồi",
                    "explanation": "'Thu hồi'만으로는 일반적인 회수로 오해될 수 있어, '리콜'의 의미를 명확히 하기 위해 'sản phẩm'을 추가하거나 'Lệnh thu hồi'(리콜 명령)로 표현해야 합니다."
                },
                {
                    "mistake": "Triệu hồi로 번역",
                    "correction": "Thu hồi sản phẩm",
                    "explanation": "'Triệu hồi'는 '소환'의 의미가 강하므로 제품 리콜에는 'Thu hồi'가 적절합니다."
                },
                {
                    "mistake": "리콜 비용을 소비자가 부담한다고 통역",
                    "correction": "제조사 부담이 원칙임을 명시",
                    "explanation": "리콜 비용은 제조사가 부담하는 것이 원칙이므로, 통역 시 이를 명확히 해야 합니다."
                }
            ],
            "examples": [
                {
                    "ko": "결함이 발견되어 해당 모델의 리콜을 결정했습니다.",
                    "vi": "Phát hiện lỗi nên quyết định thu hồi sản phẩm mẫu mã đó.",
                    "situation": "formal"
                },
                {
                    "ko": "리콜 대상 차량은 무상으로 수리됩니다.",
                    "vi": "Xe thuộc diện thu hồi sẽ được sửa chữa miễn phí.",
                    "situation": "formal"
                },
                {
                    "ko": "자발적 리콜을 통해 소비자 신뢰를 회복하고자 합니다.",
                    "vi": "Muốn phục hồi lòng tin người tiêu dùng thông qua thu hồi sản phẩm tự nguyện.",
                    "situation": "formal"
                }
            ],
            "relatedTerms": ["제조물책임", "결함", "소비자안전", "품질보증"]
        },
        {
            "slug": "trach-nhiem-san-pham",
            "korean": "제조물책임",
            "vietnamese": "Trách nhiệm sản phẩm",
            "hanja": "製造物責任",
            "hanjaReading": "製(지을 제) 造(만들 조) 物(물건 물) 責(꾸짖을 책) 任(맡길 임)",
            "pronunciation": "짝 니엠 산 팜",
            "meaningKo": "제조물의 결함으로 인해 소비자에게 발생한 손해에 대해 제조업체가 지는 법적 책임을 의미합니다. 통역 시 'PL법(Product Liability)'이라는 약어를 함께 설명하면 이해가 빠르며, 한국은 2002년 제조물책임법 시행 이후 무과실책임주의를 채택하고 있음을 안내해야 합니다. 베트남도 민법과 소비자보호법에 관련 조항이 있으나, 입증 책임과 손해배상 범위에서 차이가 있습니다. 통역 시 결함의 종류(설계, 제조, 표시상 결함)를 정확히 구분하고, 면책 사유를 명확히 전달해야 합니다.",
            "meaningVi": "Trách nhiệm pháp lý mà nhà sản xuất phải gánh chịu đối với thiệt hại xảy ra cho người tiêu dùng do lỗi sản phẩm. Hàn Quốc áp dụng nguyên tắc trách nhiệm vô lỗi từ năm 2002 (Luật trách nhiệm sản phẩm). Việt Nam cũng có quy định trong Bộ luật Dân sự và Luật bảo vệ người tiêu dùng nhưng có sự khác biệt về gánh nặng chứng minh và phạm vi bồi thường. Cần phân biệt các loại lỗi: lỗi thiết kế, lỗi sản xuất, lỗi hướng dẫn sử dụng.",
            "context": "제품 결함 소송, 손해배상",
            "culturalNote": "한국의 제조물책임법은 무과실책임주의를 채택하여 소비자가 제조업체의 과실을 입증할 필요가 없으나, 베트남은 과실책임주의가 기본이므로 소비자의 입증 부담이 더 큽니다. 통역 시 한국 기업이 베트남에서 제조물책임 소송을 대비할 때 이러한 법적 차이를 명확히 안내해야 합니다. 특히 다국적 기업의 경우 어느 국가 법률이 적용되는지가 중요한 쟁점이 됩니다.",
            "commonMistakes": [
                {
                    "mistake": "Trách nhiệm nhà sản xuất로만 번역",
                    "correction": "Trách nhiệm sản phẩm (PL)",
                    "explanation": "'제조물책임'은 제조업체뿐 아니라 유통업체도 포함될 수 있으므로 'Trách nhiệm sản phẩm'이 더 정확합니다."
                },
                {
                    "mistake": "무과실책임과 과실책임을 구분하지 않고 통역",
                    "correction": "Trách nhiệm vô lỗi vs Trách nhiệm có lỗi 명시",
                    "explanation": "한국과 베트남의 법체계 차이를 명확히 전달하지 않으면 법적 오해가 발생할 수 있습니다."
                },
                {
                    "mistake": "결함의 종류를 구분하지 않음",
                    "correction": "Lỗi thiết kế, lỗi sản xuất, lỗi hướng dẫn 구분",
                    "explanation": "결함의 종류에 따라 책임 범위와 입증 방법이 달라지므로 정확히 구분해야 합니다."
                }
            ],
            "examples": [
                {
                    "ko": "제조물책임법에 따라 결함 제품으로 인한 피해를 배상합니다.",
                    "vi": "Theo Luật trách nhiệm sản phẩm, bồi thường thiệt hại do sản phẩm lỗi gây ra.",
                    "situation": "formal"
                },
                {
                    "ko": "설계상 결함으로 인정되어 제조물책임이 성립되었습니다.",
                    "vi": "Được xác nhận là lỗi thiết kế nên thành lập trách nhiệm sản phẩm.",
                    "situation": "formal"
                },
                {
                    "ko": "제조물책임 보험에 가입하여 리스크를 관리하고 있습니다.",
                    "vi": "Đang quản lý rủi ro bằng cách tham gia bảo hiểm trách nhiệm sản phẩm.",
                    "situation": "formal"
                }
            ],
            "relatedTerms": ["리콜", "결함", "무과실책임", "손해배상", "품질보증"]
        },
        {
            "slug": "quy-dinh-dieu-khoan",
            "korean": "약관규제",
            "vietnamese": "Quy định điều khoản",
            "hanja": "約款規制",
            "hanjaReading": "約(맺을 약) 款(관 관) 規(법 규) 制(억제할 제)",
            "pronunciation": "귀 딘 디에우 코안",
            "meaningKo": "사업자가 일방적으로 작성한 계약 조건(약관)이 소비자에게 불리하거나 불공정하지 않도록 규제하는 법률 제도입니다. 통역 시 '약관의규제에관한법률'을 'Luật quy định điều khoản giao dịch'으로 풀어서 설명하고, 불공정 약관의 유형(면책조항, 손해배상 제한, 소송 제기 제한 등)을 구체적으로 안내해야 합니다. 한국은 약관심사제도가 발달했으나 베트남은 아직 제도적 정비가 미흡하여, 통역 시 한국 기업이 베트남에서 약관을 작성할 때 주의사항을 명확히 전달해야 합니다.",
            "meaningVi": "Chế độ pháp lý quy định để điều khoản hợp đồng do doanh nghiệp soạn thảo một chiều không bất lợi hoặc không công bằng đối với người tiêu dùng. Hàn Quốc có Luật quy định điều khoản giao dịch (약관의규제에관한법률) và chế độ kiểm tra điều khoản phát triển. Việt Nam còn hạn chế về mặt thể chế. Cần giải thích các loại điều khoản không công bằng: miễn trách nhiệm, hạn chế bồi thường, hạn chế quyền khởi kiện.",
            "context": "전자상거래, 금융 계약, 보험",
            "culturalNote": "한국은 공정거래위원회와 한국소비자원이 불공정 약관을 사전·사후 심사하는 제도가 확립되어 있으나, 베트남은 계약 자유의 원칙이 강하고 사후 분쟁 해결이 주로 이루어집니다. 통역 시 한국 기업이 베트남에서 약관을 사용할 때, 베트남 소비자보호법과 민법의 관련 조항을 준수해야 함을 안내해야 합니다. 특히 전자상거래와 금융 상품에서 약관 분쟁이 빈번합니다.",
            "commonMistakes": [
                {
                    "mistake": "Kiểm soát điều khoản로 번역",
                    "correction": "Quy định điều khoản",
                    "explanation": "'Kiểm soát'은 '통제'의 의미가 강하므로, 법률적 '규제'는 'Quy định'이 적절합니다."
                },
                {
                    "mistake": "약관과 계약을 구분하지 않고 통역",
                    "correction": "Điều khoản giao dịch vs Hợp đồng 구분",
                    "explanation": "약관은 일방적으로 작성된 조건(điều khoản)이고, 계약(hợp đồng)은 쌍방 합의이므로 구분이 필요합니다."
                },
                {
                    "mistake": "불공정 약관의 예시를 생략",
                    "correction": "면책조항, 손해배상 제한 등 구체적 예시 포함",
                    "explanation": "추상적으로 설명하면 이해가 어려우므로, 구체적인 불공정 약관 유형을 예시로 들어야 합니다."
                }
            ],
            "examples": [
                {
                    "ko": "이 약관은 소비자에게 부당하게 불리하여 약관규제법 위반입니다.",
                    "vi": "Điều khoản này bất lợi bất công cho người tiêu dùng nên vi phạm Luật quy định điều khoản.",
                    "situation": "formal"
                },
                {
                    "ko": "약관심사 결과 면책조항이 무효로 판단되었습니다.",
                    "vi": "Kết quả kiểm tra điều khoản, điều khoản miễn trách nhiệm bị xác định vô hiệu.",
                    "situation": "formal"
                },
                {
                    "ko": "약관을 명확하고 이해하기 쉽게 작성해야 합니다.",
                    "vi": "Phải soạn thảo điều khoản rõ ràng và dễ hiểu.",
                    "situation": "formal"
                }
            ],
            "relatedTerms": ["불공정약관", "계약서", "소비자보호법", "면책조항"]
        },
        {
            "slug": "thuong-mai-dien-tu",
            "korean": "전자상거래",
            "vietnamese": "Thương mại điện tử",
            "hanja": "電子商去來",
            "hanjaReading": "電(번개 전) 子(아들 자) 商(장사 상) 去(갈 거) 來(올 래)",
            "pronunciation": "투엉 마이 디엔 뜨",
            "meaningKo": "인터넷이나 전자 네트워크를 통해 상품이나 서비스를 거래하는 모든 활동을 의미합니다. 통역 시 'e-commerce' 또는 'online shopping'과 동일한 개념임을 안내하고, 한국의 전자상거래법, 베트남의 Luật thương mại điện tử를 언급하면 이해가 빠릅니다. 통역에서 주의할 점은 전자상거래 특유의 청약철회권, 배송 책임, 개인정보 처리 등의 법적 의무를 정확히 전달하는 것입니다. 한국과 베트남 모두 전자상거래가 급성장하고 있으나, 소비자 보호 제도의 집행 수준에 차이가 있습니다.",
            "meaningVi": "Mọi hoạt động giao dịch hàng hóa hoặc dịch vụ thông qua internet hoặc mạng điện tử. Giống với e-commerce hoặc online shopping. Hàn Quốc có Luật thương mại điện tử, Việt Nam cũng có Luật thương mại điện tử. Cần chú ý các nghĩa vụ pháp lý đặc thù: quyền hủy đơn hàng, trách nhiệm vận chuyển, xử lý thông tin cá nhân. Cả hai nước đều phát triển nhanh thương mại điện tử nhưng có sự khác biệt về mức độ thực thi chế độ bảo vệ người tiêu dùng.",
            "context": "온라인 쇼핑, 소비자 보호",
            "culturalNote": "한국은 쿠팡, 네이버 등 대형 플랫폼 중심으로 전자상거래가 발달했고, 소비자 보호 제도(청약철회, 배송 지연 보상 등)가 체계화되어 있습니다. 베트남은 Shopee, Lazada, Tiki 등이 주도하며, 최근 전자상거래법 개정으로 소비자 보호가 강화되고 있으나 아직 분쟁 해결 절차가 복잡합니다. 통역 시 한국 기업이 베트남에 진출할 때 플랫폼 수수료, 세금, 소비자 분쟁 대응 방법을 명확히 안내해야 합니다.",
            "commonMistakes": [
                {
                    "mistake": "Mua bán online으로만 번역",
                    "correction": "Thương mại điện tử",
                    "explanation": "'Mua bán online'은 구어체이며, 법률 및 공식 문서에서는 'Thương mại điện tử'를 사용해야 합니다."
                },
                {
                    "mistake": "청약철회권을 'hủy đơn hàng'로만 번역",
                    "correction": "Quyền rút đơn hàng / Quyền hủy bỏ giao dịch",
                    "explanation": "법적 권리이므로 'quyền'을 명시하고, 'rút đơn hàng' 또는 'hủy bỏ giao dịch'로 정확히 표현해야 합니다."
                },
                {
                    "mistake": "전자상거래와 소셜커머스를 혼동",
                    "correction": "전자상거래는 포괄 개념, 소셜커머스는 하위 유형",
                    "explanation": "소셜커머스(thương mại xã hội)는 전자상거래의 한 형태이므로 개념을 구분해야 합니다."
                }
            ],
            "examples": [
                {
                    "ko": "전자상거래법에 따라 7일 내 청약철회가 가능합니다.",
                    "vi": "Theo Luật thương mại điện tử, có thể rút đơn hàng trong vòng 7 ngày.",
                    "situation": "formal"
                },
                {
                    "ko": "전자상거래 플랫폼에서 판매자의 의무를 명확히 해야 합니다.",
                    "vi": "Phải làm rõ nghĩa vụ của người bán trên nền tảng thương mại điện tử.",
                    "situation": "formal"
                },
                {
                    "ko": "전자상거래 분쟁은 온라인 중재로 해결할 수 있습니다.",
                    "vi": "Tranh chấp thương mại điện tử có thể giải quyết bằng trọng tài trực tuyến.",
                    "situation": "formal"
                }
            ],
            "relatedTerms": ["청약철회", "온라인쇼핑", "소비자보호", "배송", "개인정보보호"]
        },
        {
            "slug": "ban-hang-vieng-tham",
            "korean": "방문판매",
            "vietnamese": "Bán hàng viếng thăm",
            "hanja": "訪問販賣",
            "hanjaReading": "訪(찾을 방) 問(물을 문) 販(팔 판) 賣(팔 매)",
            "pronunciation": "반 항 비엥 탐",
            "meaningKo": "판매자가 소비자의 집이나 직장을 직접 방문하여 상품을 판매하는 거래 방식을 의미합니다. 통역 시 '외판(ngoại bán)'과 구분하고, 한국의 방문판매법에서는 특정 냉각기간(청약철회 14일)과 방문 시간 제한 등을 규정하고 있음을 설명해야 합니다. 베트남에서도 유사한 판매 방식이 존재하나 법적 규제가 상대적으로 약하므로, 통역 시 한국의 엄격한 소비자 보호 규정을 명확히 전달해야 합니다. 특히 노인 대상 불공정 방문판매가 사회적 문제가 되고 있습니다.",
            "meaningVi": "Phương thức giao dịch mà người bán trực tiếp đến nhà hoặc nơi làm việc của người tiêu dùng để bán hàng. Khác với ngoại bán (bán ngoài đường). Luật bán hàng viếng thăm của Hàn Quốc quy định thời gian làm mát (14 ngày rút đơn hàng), hạn chế giờ viếng thăm. Việt Nam cũng có phương thức tương tự nhưng quy định pháp lý tương đối yếu. Đặc biệt bán hàng không công bằng cho người cao tuổi đang trở thành vấn đề xã hội.",
            "context": "소비자 보호, 노인 피해 방지",
            "culturalNote": "한국은 방문판매법으로 방문 시간(오전 9시~오후 9시), 재방문 금지, 청약철회 절차 등을 엄격히 규제하지만, 베트남은 이러한 세부 규정이 부족하여 소비자 피해가 빈번합니다. 통역 시 한국 기업이 베트남에서 방문판매를 할 경우, 현지 법규를 준수하되 한국 수준의 윤리 기준을 적용할 것을 권장해야 합니다. 특히 노인 대상 고가 상품 판매는 양국 모두 사회적으로 민감한 이슈입니다.",
            "commonMistakes": [
                {
                    "mistake": "Bán hàng tại nhà로만 번역",
                    "correction": "Bán hàng viếng thăm",
                    "explanation": "'Bán hàng tại nhà'는 가정 내 판매 일반을 의미하므로, 법적 개념인 '방문판매'는 'Bán hàng viếng thăm'으로 표현해야 합니다."
                },
                {
                    "mistake": "청약철회 기간을 명시하지 않음",
                    "correction": "14일 냉각기간(thời gian làm mát 14 ngày) 명시",
                    "explanation": "방문판매의 핵심 소비자 보호 장치이므로 반드시 기간을 명시해야 합니다."
                },
                {
                    "mistake": "방문판매와 전화권유판매를 혼동",
                    "correction": "방문판매(viếng thăm) vs 전화권유판매(qua điện thoại) 구분",
                    "explanation": "두 판매 방식은 규제 내용이 다르므로 명확히 구분해야 합니다."
                }
            ],
            "examples": [
                {
                    "ko": "방문판매로 구매한 상품은 14일 내 청약철회가 가능합니다.",
                    "vi": "Sản phẩm mua qua bán hàng viếng thăm có thể rút đơn hàng trong 14 ngày.",
                    "situation": "formal"
                },
                {
                    "ko": "방문판매원은 신분증을 제시해야 합니다.",
                    "vi": "Nhân viên bán hàng viếng thăm phải xuất trình giấy tờ tùy thân.",
                    "situation": "formal"
                },
                {
                    "ko": "노인 대상 불공정 방문판매가 증가하고 있습니다.",
                    "vi": "Bán hàng viếng thăm không công bằng nhắm vào người cao tuổi đang gia tăng.",
                    "situation": "formal"
                }
            ],
            "relatedTerms": ["청약철회", "전화권유판매", "다단계판매", "소비자보호법"]
        },
        {
            "slug": "giao-dich-tra-gop",
            "korean": "할부거래",
            "vietnamese": "Giao dịch trả góp",
            "hanja": "割賦去來",
            "hanjaReading": "割(나눌 할) 賦(나눌 부) 去(갈 거) 來(올 래)",
            "pronunciation": "자오 지크 짜 고프",
            "meaningKo": "상품 대금을 일시불로 지급하지 않고 여러 차례에 걸쳐 나누어 지급하는 거래 방식입니다. 통역 시 '할부(trả góp)'와 '신용카드 할부(trả góp thẻ tín dụng)'를 구분하고, 한국의 할부거래법에서는 선불식 할부와 후불식 할부로 나누어 규제하고 있음을 설명해야 합니다. 베트남에서도 할부 판매가 일반적이나, 이자율 고지와 중도 상환 수수료 등에서 법적 보호가 약하므로, 통역 시 계약 조건을 명확히 확인하도록 안내해야 합니다.",
            "meaningVi": "Phương thức giao dịch thanh toán tiền hàng không một lần mà chia ra nhiều lần. Cần phân biệt trả góp thông thường và trả góp thẻ tín dụng. Luật giao dịch trả góp của Hàn Quốc chia ra trả góp trả trước và trả góp trả sau để quy định. Việt Nam cũng phổ biến bán trả góp nhưng bảo vệ pháp lý yếu hơn về công bố lãi suất và phí trả trước hạn. Cần xác nhận rõ điều kiện hợp đồng khi phiên dịch.",
            "context": "가전제품, 자동차 구매",
            "culturalNote": "한국은 할부거래법으로 할부 계약서 작성 의무, 이자율 고지, 중도 상환 시 수수료 제한 등을 규정하지만, 베트남은 계약 자유도가 높아 소비자가 불리한 조건에 동의할 위험이 있습니다. 통역 시 한국 소비자가 베트남에서 할부로 상품을 구매할 때, 총 할부 금액, 이자율, 중도 상환 조건을 꼼꼼히 확인하도록 안내해야 합니다. 특히 가전제품, 오토바이, 자동차 구매에서 할부가 흔합니다.",
            "commonMistakes": [
                {
                    "mistake": "Trả chậm로 번역",
                    "correction": "Trả góp",
                    "explanation": "'Trả chậm'은 '연체'의 의미가 강하므로, 할부는 'Trả góp'으로 표현해야 합니다."
                },
                {
                    "mistake": "이자율을 lãi suất 없이 통역",
                    "correction": "반드시 lãi suất(이자율) 명시",
                    "explanation": "할부 거래에서 이자율은 필수 정보이므로 반드시 언급해야 합니다."
                },
                {
                    "mistake": "신용할부와 일반할부를 구분하지 않음",
                    "correction": "Trả góp thẻ tín dụng vs Trả góp thông thường 구분",
                    "explanation": "신용카드 할부와 일반 할부는 이자율과 계약 주체가 다르므로 구분이 필요합니다."
                }
            ],
            "examples": [
                {
                    "ko": "이 제품은 12개월 무이자 할부가 가능합니다.",
                    "vi": "Sản phẩm này có thể trả góp 12 tháng không lãi suất.",
                    "situation": "formal"
                },
                {
                    "ko": "할부 계약서에 총 할부 금액이 명시되어 있습니다.",
                    "vi": "Hợp đồng trả góp ghi rõ tổng số tiền trả góp.",
                    "situation": "formal"
                },
                {
                    "ko": "중도 상환 시 수수료가 발생할 수 있습니다.",
                    "vi": "Khi trả trước hạn có thể phát sinh phí.",
                    "situation": "formal"
                }
            ],
            "relatedTerms": ["신용카드", "이자율", "중도상환", "소비자금융"]
        },
        {
            "slug": "bieu-thi-quang-cao",
            "korean": "표시광고",
            "vietnamese": "Biểu thị quảng cáo",
            "hanja": "表示廣告",
            "hanjaReading": "表(겉 표) 示(보일 시) 廣(넓을 광) 告(고할 고)",
            "pronunciation": "비에우 티 꽝 까오",
            "meaningKo": "상품이나 서비스에 대한 정보를 표시하거나 광고하는 행위를 의미하며, 허위·과장 광고를 규제하는 법률 개념입니다. 통역 시 '표시광고의공정화에관한법률'을 언급하고, 허위 광고(quảng cáo gian dối), 과장 광고(quảng cáo phóng đại), 기만 광고(quảng cáo lừa dối)를 구분해야 합니다. 한국은 공정거래위원회가 엄격히 심사하지만, 베트남은 광고법 집행이 상대적으로 느슨하여 소비자 피해가 발생하기 쉽습니다. 통역 시 온라인 광고, 인플루언서 마케팅 등 새로운 형태의 광고도 규제 대상임을 안내해야 합니다.",
            "meaningVi": "Hành vi biểu thị hoặc quảng cáo thông tin về hàng hóa hoặc dịch vụ, là khái niệm pháp lý quy định quảng cáo gian dối và phóng đại. Hàn Quốc có Luật công bằng hóa biểu thị quảng cáo, Ủy ban cạnh tranh công bằng kiểm tra nghiêm ngặt. Việt Nam có Luật quảng cáo nhưng thực thi tương đối lỏng lẻo nên dễ xảy ra thiệt hại cho người tiêu dùng. Cần phân biệt quảng cáo gian dối, quảng cáo phóng đại, quảng cáo lừa dối. Quảng cáo trực tuyến, marketing qua người có ảnh hưởng cũng là đối tượng quy định.",
            "context": "마케팅, 소비자 보호",
            "culturalNote": "한국은 표시광고법으로 비교 광고, 최고·최상급 표현 사용, 할인율 허위 표시 등을 세밀하게 규제하며, 위반 시 과징금과 형사 처벌이 가능합니다. 베트남은 광고법이 있으나 집행력이 약하고 온라인 광고에 대한 감독이 미흡합니다. 통역 시 한국 기업이 베트남에서 마케팅할 때, 과장 표현을 자제하고 증빙 자료를 준비하도록 안내해야 합니다. 특히 건강기능식품, 화장품 광고에서 허위·과장 문제가 빈번합니다.",
            "commonMistakes": [
                {
                    "mistake": "Quảng cáo로만 번역",
                    "correction": "Biểu thị quảng cáo",
                    "explanation": "'표시광고'는 광고(quảng cáo)와 표시(biểu thị)를 모두 포함하는 개념이므로 함께 표현해야 합니다."
                },
                {
                    "mistake": "허위 광고와 과장 광고를 구분하지 않음",
                    "correction": "Quảng cáo gian dối vs Quảng cáo phóng đại 구분",
                    "explanation": "허위(gian dối)는 사실과 다른 것, 과장(phóng đại)은 사실을 부풀린 것으로 법적 책임이 다릅니다."
                },
                {
                    "mistake": "인플루언서 광고를 규제 대상 아닌 것으로 설명",
                    "correction": "인플루언서 마케팅도 규제 대상임을 명시",
                    "explanation": "최근 인플루언서 광고도 표시광고법 적용 대상이므로 이를 명확히 해야 합니다."
                }
            ],
            "examples": [
                {
                    "ko": "허위 표시광고로 과징금이 부과되었습니다.",
                    "vi": "Bị phạt tiền do biểu thị quảng cáo gian dối.",
                    "situation": "formal"
                },
                {
                    "ko": "비교 광고 시 객관적인 자료를 제시해야 합니다.",
                    "vi": "Khi quảng cáo so sánh phải trình bày tài liệu khách quan.",
                    "situation": "formal"
                },
                {
                    "ko": "할인율을 과장한 표시광고는 위법입니다.",
                    "vi": "Biểu thị quảng cáo phóng đại tỷ lệ giảm giá là vi phạm pháp luật.",
                    "situation": "formal"
                }
            ],
            "relatedTerms": ["허위광고", "과장광고", "공정거래법", "소비자보호"]
        },
        {
            "slug": "xam-pham-thong-tin-ca-nhan",
            "korean": "개인정보침해",
            "vietnamese": "Xâm phạm thông tin cá nhân",
            "hanja": "個人情報侵害",
            "hanjaReading": "個(낱 개) 人(사람 인) 情(뜻 정) 報(알릴 보) 侵(침범할 침) 害(해칠 해)",
            "pronunciation": "삼 팜 통 틴 까 년",
            "meaningKo": "개인의 동의 없이 개인정보를 수집, 이용, 제공하거나 유출하여 개인의 사생활과 권리를 침해하는 행위를 의미합니다. 통역 시 '개인정보보호법'을 언급하고, 개인정보의 범위(이름, 주민등록번호, 연락처, 위치정보 등)를 구체적으로 설명해야 합니다. 한국은 개인정보보호위원회가 강력히 규제하며, GDPR 수준의 보호를 제공하지만, 베트남은 개인정보보호법이 있으나 집행이 약하고 소비자 인식도 낮습니다. 통역 시 동의 절차, 유출 시 대응 방법, 손해배상 청구 등을 명확히 전달해야 합니다.",
            "meaningVi": "Hành vi thu thập, sử dụng, cung cấp hoặc làm lộ thông tin cá nhân không có sự đồng ý của cá nhân, xâm phạm quyền riêng tư và quyền lợi cá nhân. Hàn Quốc có Ủy ban bảo vệ thông tin cá nhân quy định mạnh mẽ, cung cấp bảo vệ tương đương GDPR. Việt Nam có Luật bảo vệ thông tin cá nhân nhưng thực thi yếu và nhận thức người tiêu dùng thấp. Cần giải thích rõ phạm vi thông tin cá nhân (tên, số CMND, liên lạc, thông tin vị trí), quy trình đồng ý, cách đối phóng khi lộ thông tin, yêu cầu bồi thường.",
            "context": "전자상거래, 금융, 의료",
            "culturalNote": "한국은 개인정보 유출 시 기업의 손해배상 책임이 크고, 집단소송도 가능하며, 과징금과 형사 처벌이 엄격합니다. 베트남은 개인정보 보호 의식이 낮고, 유출 시 대응이 느린 편입니다. 통역 시 한국 기업이 베트남에서 개인정보를 다룰 때, 현지법 준수와 함께 한국 수준의 보안 기준을 적용하도록 권장해야 합니다. 특히 전자상거래, 금융, 의료 분야에서 개인정보 보호가 중요합니다.",
            "commonMistakes": [
                {
                    "mistake": "Vi phạm thông tin cá nhân로 번역",
                    "correction": "Xâm phạm thông tin cá nhân",
                    "explanation": "'Vi phạm'은 일반적인 위반, 'Xâm phạm'은 침해의 의미가 강하므로 'Xâm phạm'이 적절합니다."
                },
                {
                    "mistake": "개인정보 범위를 명시하지 않음",
                    "correction": "이름, 주민번호, 연락처 등 구체적 예시 포함",
                    "explanation": "개인정보의 범위가 넓으므로 구체적인 예시를 들어 이해를 돕는 것이 중요합니다."
                },
                {
                    "mistake": "동의 절차를 생략하고 통역",
                    "correction": "명시적 동의(sự đồng ý rõ ràng) 필요성 강조",
                    "explanation": "개인정보 수집 시 명시적 동의가 필수이므로 이를 강조해야 합니다."
                }
            ],
            "examples": [
                {
                    "ko": "개인정보 유출로 인한 손해배상 청구가 증가하고 있습니다.",
                    "vi": "Yêu cầu bồi thường do làm lộ thông tin cá nhân đang gia tăng.",
                    "situation": "formal"
                },
                {
                    "ko": "개인정보 수집 시 명시적 동의를 받아야 합니다.",
                    "vi": "Khi thu thập thông tin cá nhân phải có sự đồng ý rõ ràng.",
                    "situation": "formal"
                },
                {
                    "ko": "개인정보 침해 사고에 대비한 보안 대책이 필요합니다.",
                    "vi": "Cần có biện pháp bảo mật đề phòng sự cố xâm phạm thông tin cá nhân.",
                    "situation": "formal"
                }
            ],
            "relatedTerms": ["개인정보보호법", "정보유출", "동의", "손해배상", "암호화"]
        },
        {
            "slug": "rut-don-hang",
            "korean": "청약철회",
            "vietnamese": "Rút đơn hàng",
            "hanja": "請約撤回",
            "hanjaReading": "請(청할 청) 約(맺을 약) 撤(물리칠 철) 回(돌아올 회)",
            "pronunciation": "줏 돈 항",
            "meaningKo": "소비자가 계약 체결 후 일정 기간 내에 별도의 이유 없이 계약을 해제할 수 있는 권리를 의미합니다. 통역 시 '쿨링오프(cooling-off)'와 같은 개념이며, 전자상거래(7일), 방문판매(14일), 할부거래(14일) 등 거래 유형에 따라 기간이 다름을 설명해야 합니다. 한국은 소비자 보호를 위해 청약철회권을 강력히 보장하지만, 베트남은 제도는 있으나 집행이 약하고 판매자의 거부나 지연이 빈번합니다. 통역 시 청약철회 가능 기간, 반품 비용 부담, 환불 절차를 명확히 전달해야 합니다.",
            "meaningVi": "Quyền của người tiêu dùng được hủy bỏ hợp đồng trong thời gian nhất định sau khi ký kết mà không cần lý do cụ thể. Giống với cooling-off. Thời gian khác nhau theo loại giao dịch: thương mại điện tử (7 ngày), bán hàng viếng thăm (14 ngày), trả góp (14 ngày). Hàn Quốc bảo đảm mạnh mẽ quyền rút đơn hàng để bảo vệ người tiêu dùng, Việt Nam có chế độ nhưng thực thi yếu, thường xảy ra từ chối hoặc trì hoãn từ người bán. Cần truyền đạt rõ thời gian có thể rút đơn, gánh chi phí trả hàng, quy trình hoàn tiền.",
            "context": "전자상거래, 방문판매, 할부거래",
            "culturalNote": "한국은 청약철회권이 법으로 보장되어 소비자가 단순 변심으로도 반품 가능하며, 판매자가 이를 거부하면 처벌받습니다. 베트남은 청약철회 제도가 있으나 판매자의 자발적 수용 정도가 낮고, 소비자가 반품 비용을 부담하는 경우가 많습니다. 통역 시 한국 소비자가 베트남에서 온라인 쇼핑 시 청약철회가 어렵거나 지연될 수 있음을 사전에 안내해야 합니다.",
            "commonMistakes": [
                {
                    "mistake": "Hủy đơn hàng로만 번역",
                    "correction": "Rút đơn hàng 또는 Quyền rút đơn hàng",
                    "explanation": "'Hủy đơn hàng'는 일반적인 취소, '청약철회'는 법적 권리이므로 'Rút đơn hàng' 또는 'Quyền rút đơn hàng'로 표현해야 합니다."
                },
                {
                    "mistake": "청약철회 기간을 명시하지 않음",
                    "correction": "거래 유형별 기간(7일, 14일 등) 명시",
                    "explanation": "거래 유형에 따라 기간이 다르므로 반드시 명시해야 합니다."
                },
                {
                    "mistake": "반품 비용 부담 주체를 생략",
                    "correction": "소비자 변심 시 소비자 부담, 하자 시 판매자 부담 구분",
                    "explanation": "반품 사유에 따라 비용 부담 주체가 다르므로 명확히 해야 합니다."
                }
            ],
            "examples": [
                {
                    "ko": "온라인 구매 시 7일 이내 청약철회가 가능합니다.",
                    "vi": "Khi mua hàng trực tuyến có thể rút đơn hàng trong 7 ngày.",
                    "situation": "formal"
                },
                {
                    "ko": "청약철회 시 반품 배송비는 소비자 부담입니다.",
                    "vi": "Khi rút đơn hàng, phí vận chuyển trả hàng do người tiêu dùng chịu.",
                    "situation": "formal"
                },
                {
                    "ko": "제품 하자로 인한 청약철회는 전액 환불됩니다.",
                    "vi": "Rút đơn hàng do lỗi sản phẩm sẽ được hoàn tiền toàn bộ.",
                    "situation": "formal"
                }
            ],
            "relatedTerms": ["전자상거래", "방문판매", "환불", "반품", "소비자권리"]
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
