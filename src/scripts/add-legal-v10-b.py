#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""물권법 심화 용어 추가 (v10-B)"""
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
            "slug": "chiem-huu",
            "korean": "점유",
            "vietnamese": "Chiếm hữu",
            "hanja": "占有",
            "hanjaReading": "占(점칠 점) 有(있을 유)",
            "pronunciation": "점유",
            "meaningKo": "물건을 사실상 지배하는 상태를 말하며, 소유권과는 별개의 개념입니다. 통역 시 점유자는 물건에 대한 소유권이 없어도 점유만으로 일정한 법적 보호를 받는다는 점을 명확히 해야 합니다. 베트남 민법에서도 'chiếm hữu(점유)'와 'sở hữu(소유)'를 구분하며, 점유자는 점유물을 침해당했을 때 점유보호청구권을 행사할 수 있습니다. 통역 시 점유의 종류(자주점유, 타주점유), 점유 취득 시효, 점유자의 권리와 의무를 명확히 전달해야 합니다. 부동산 분쟁에서 실제 거주자(점유자)와 등기부상 소유자가 다른 경우 법적 문제가 복잡해지므로 주의가 필요합니다.",
            "meaningVi": "Tình trạng thực tế kiểm soát tài sản, khác với quyền sở hữu. Người chiếm hữu được pháp luật bảo vệ nhất định ngay cả khi không có quyền sở hữu. Luật Việt Nam phân biệt chiếm hữu (possession) và sở hữu (ownership). Người chiếm hữu có quyền yêu cầu bảo vệ chiếm hữu khi bị xâm phạm. Cần lưu ý các loại chiếm hữu (tự chủ, tha chủ) và quyền lợi của người chiếm hữu.",
            "context": "부동산 분쟁, 물건 인도, 점유 취득 시효 주장 시",
            "culturalNote": "한국은 점유 개념이 법률적으로 정교하게 발달했으나, 베트남은 실무상 점유와 소유를 혼동하는 경우가 많습니다. 베트남에서는 '사실상 사용하는 사람'을 중시하는 경향이 있어, 한국의 엄격한 점유권 구분이 이해되지 않을 수 있습니다. 통역 시 점유자가 소유자가 아닐 수 있으며, 점유만으로는 물건을 처분할 수 없다는 점을 명확히 설명해야 합니다. 베트남은 점유 취득시효 기간이 한국(10년, 20년)보다 길어 30년인 경우도 있으므로, 통역 시 양국 법의 차이를 설명해야 합니다. 특히 토지 점유 분쟁에서는 역사적 배경과 정치적 요인이 개입될 수 있어 통역사는 중립을 유지하며 법적 쟁점만 전달해야 합니다.",
            "commonMistakes": [
                {
                    "mistake": "점유와 소유를 동일하게 번역",
                    "correction": "점유는 chiếm hữu, 소유는 sở hữu로 엄격히 구분",
                    "explanation": "점유는 사실상 지배, 소유는 법률상 권리로 전혀 다른 개념"
                },
                {
                    "mistake": "점유자가 물건을 처분할 수 있다고 설명",
                    "correction": "점유는 사용권만 있고 처분권은 소유자에게만",
                    "explanation": "점유자는 보관·사용 의무가 있으나 매각·증여 등 처분 불가"
                },
                {
                    "mistake": "점유 취득시효가 한국과 베트남이 같다고 설명",
                    "correction": "한국 10-20년, 베트남 30년으로 차이 있음",
                    "explanation": "베트남은 점유 취득시효 기간이 더 길어 주의 필요"
                }
            ],
            "examples": [
                {
                    "ko": "소유권 등기가 없더라도 20년간 평온·공연하게 점유하면 취득시효가 완성됩니다",
                    "vi": "Ngay cả khi không có đăng ký quyền sở hữu, nếu chiếm hữu một cách bình yên, công khai trong 20 năm thì có thể hoàn thành thời hiệu chiếm hữu",
                    "situation": "formal"
                },
                {
                    "ko": "이 땅은 제가 실제로 쓰고 있으니 제 거예요 - 아니요, 점유와 소유는 달라요. 등기부 확인이 필요합니다",
                    "vi": "Mảnh đất này tôi đang dùng nên là của tôi - Không, chiếm hữu và sở hữu khác nhau. Cần kiểm tra sổ đỏ",
                    "situation": "informal"
                },
                {
                    "ko": "현장에서 점유자가 인도 거부하면 법원에 점유이전청구 소송 제기해야 합니다",
                    "vi": "Nếu người chiếm hữu từ chối giao tại hiện trường, phải nộp đơn kiện yêu cầu chuyển giao chiếm hữu tại tòa án",
                    "situation": "onsite"
                }
            ],
            "relatedTerms": ["소유권", "점유취득시효", "부동산등기", "물건인도"]
        },
        {
            "slug": "quyen-luu-chi",
            "korean": "유치권",
            "vietnamese": "Quyền lưu치",
            "hanja": "留置權",
            "hanjaReading": "留(머무를 류) 置(둘 치) 權(권세 권)",
            "pronunciation": "유치권",
            "meaningKo": "타인의 물건을 점유한 자가 그 물건에 관해 생긴 채권을 변제받을 때까지 그 물건을 유치할 수 있는 권리입니다. 통역 시 유치권자는 채무 변제를 받을 때까지 물건을 돌려주지 않을 수 있으며, 이는 담보권의 일종으로 법적 보호를 받는다는 점을 명확히 해야 합니다. 베트남 민법에서는 'quyền giữ lại tài sản(재산 보유권)'으로 표현하며, 건설 현장에서 공사대금을 받지 못한 시공사가 건물을 유치하는 경우가 대표적입니다. 통역 시 유치권 성립 요건(채권, 점유, 견련성)과 효력 범위를 명확히 전달해야 하며, 유치권은 등기 없이도 제3자에게 대항할 수 있다는 점이 중요합니다.",
            "meaningVi": "Quyền giữ lại tài sản của người khác cho đến khi được thanh toán khoản nợ liên quan đến tài sản đó. Người có quyền lưu giữ có thể từ chối trả lại tài sản cho đến khi nhận được thanh toán, đây là một loại quyền bảo đảm được pháp luật bảo vệ. Trong xây dựng, nhà thầu chưa nhận tiền công có thể lưu giữ công trình. Quyền này có hiệu lực ngay cả không đăng ký.",
            "context": "공사대금 미지급, 수리비 청구, 보관료 청구 시",
            "culturalNote": "한국은 유치권이 강력한 담보권으로 인정되어 경매에서도 우선 변제를 받을 수 있으나, 베트남은 유치권 개념이 덜 발달하여 법적 보호가 약한 편입니다. 베트남에서는 유치권 대신 물건을 반환하지 않고 버티는 행위가 '횡령'으로 처벌받을 수 있어 통역 시 주의가 필요합니다. 통역사는 한국 기업에게 베트남에서는 유치권보다 계약서에 선지급 조건이나 은행 보증을 명시하는 것이 안전하다고 조언해야 합니다. 베트남에서 공사대금을 못 받은 시공사가 건물을 점거하면 강제 퇴거 명령을 받을 수 있으므로, 법적 절차를 통한 해결을 권장해야 합니다. 한국의 유치권 개념을 베트남에 그대로 적용하면 법적 분쟁이 발생할 수 있습니다.",
            "commonMistakes": [
                {
                    "mistake": "모든 채권자가 유치권을 주장할 수 있다고 설명",
                    "correction": "채권과 물건 간 견련성 필요, 무관한 채권은 불가",
                    "explanation": "유치권은 물건에서 발생한 채권에만 인정됨"
                },
                {
                    "mistake": "유치권으로 물건을 처분할 수 있다고 설명",
                    "correction": "유치권은 보유권일 뿐, 처분권은 없음",
                    "explanation": "유치권자는 물건을 팔 수 없고 유치만 가능"
                },
                {
                    "mistake": "베트남에서도 유치권이 한국처럼 강하다고 설명",
                    "correction": "베트남은 유치권 보호가 약해 계약서에 담보 명시 필요",
                    "explanation": "베트남은 유치권 개념이 미발달, 실무적 보호 미흡"
                }
            ],
            "examples": [
                {
                    "ko": "공사대금 5억원을 받을 때까지 본 건물에 대한 유치권을 행사합니다",
                    "vi": "Chúng tôi thực hiện quyền giữ lại công trình này cho đến khi nhận được 5 tỷ won tiền công xây dựng",
                    "situation": "formal"
                },
                {
                    "ko": "돈 안 주면 차 안 돌려줘도 되는 게 유치권이에요",
                    "vi": "Nếu không trả tiền, có thể không trả xe, đó là quyền lưu giữ",
                    "situation": "informal"
                },
                {
                    "ko": "현장에서 유치권 행사하려면 점유를 계속 유지해야 하니 주의하세요",
                    "vi": "Để thực hiện quyền lưu giữ tại hiện trường, phải duy trì chiếm hữu liên tục nên cẩn thận",
                    "situation": "onsite"
                }
            ],
            "relatedTerms": ["담보권", "점유", "견련관계", "경매"]
        },
        {
            "slug": "quyen-the-chap",
            "korean": "질권",
            "vietnamese": "Quyền thế chấp",
            "hanja": "質權",
            "hanjaReading": "質(바탕 질) 權(권세 권)",
            "pronunciation": "질권",
            "meaningKo": "채권의 담보로 채무자 또는 제3자가 제공한 동산이나 권리를 채권자가 점유하고, 채무 불이행 시 그 목적물로부터 우선 변제받을 수 있는 담보물권입니다. 통역 시 질권은 점유를 이전해야 성립한다는 점에서 저당권(점유 이전 없음)과 구분되며, 주로 동산이나 유가증권에 설정된다는 점을 명확히 해야 합니다. 베트남 민법에서는 'quyền cầm cố(담보권)'로 표현하며, 전통적으로 금은방에서 금반지를 맡기고 돈을 빌리는 것이 대표적 사례입니다. 통역 시 질권의 성립 요건(점유 이전, 합의), 효력(우선변제권), 소멸 사유를 명확히 전달하고, 질권자는 질물을 선관주의 의무로 보관해야 한다는 점을 설명해야 합니다.",
            "meaningVi": "Quyền bảo đảm bằng cách giao quyền chiếm hữu tài sản động sản hoặc quyền cho chủ nợ, khi không trả nợ, chủ nợ có quyền ưu tiên thanh toán từ tài sản đó. Khác với thế chấp (không giao chiếm hữu), quyền cầm cố yêu cầu bàn giao tài sản. Ví dụ điển hình là cầm vàng ở tiệm vàng để vay tiền. Người giữ tài sản phải bảo quản cẩn thận.",
            "context": "동산 담보, 유가증권 담보, 대출 거래 시",
            "culturalNote": "한국은 질권보다 저당권을 선호하는 경향이 있으나, 베트남은 전통적으로 질권(cầm cố) 문화가 강합니다. 베트남에서는 금은방, 전당포 등에서 금, 오토바이, 전자제품 등을 맡기고 소액 대출을 받는 것이 일반적이며, 통역 시 이러한 문화적 차이를 이해하고 설명해야 합니다. 한국은 질권 설정 시 공증이나 확정일자가 필요하지만, 베트남은 실무상 간단한 영수증만으로 거래하는 경우가 많아 법적 분쟁 시 입증이 어려울 수 있습니다. 통역사는 계약서에 질물의 상세 내역, 보관 조건, 변제 방법을 명확히 기재하도록 조언하고, 분실이나 훼손 시 책임 소재를 정해두도록 권장해야 합니다. 베트남에서는 질권 설정 후 질물을 사용하는 관행도 있어 한국 기업이 주의해야 합니다.",
            "commonMistakes": [
                {
                    "mistake": "질권과 저당권을 구분하지 않고 번역",
                    "correction": "질권은 quyền cầm cố(점유 이전), 저당권은 quyền thế chấp(점유 유지)",
                    "explanation": "점유 이전 여부가 핵심 차이점"
                },
                {
                    "mistake": "질권 설정 후 질물을 계속 사용할 수 있다고 설명",
                    "correction": "질권은 점유 이전 필수, 채무자가 사용 불가",
                    "explanation": "점유 이전이 성립 요건이므로 질권자가 보관해야 함"
                },
                {
                    "mistake": "질권자가 임의로 질물을 처분할 수 있다고 설명",
                    "correction": "채무 불이행 시에도 법적 절차 거쳐 환가",
                    "explanation": "질권자의 임의 처분은 횡령죄, 반드시 법적 절차 필요"
                }
            ],
            "examples": [
                {
                    "ko": "주식 100주를 질권으로 제공하고 5천만원을 대출받았습니다",
                    "vi": "Tôi đã cầm 100 cổ phiếu để vay 50 triệu won",
                    "situation": "formal"
                },
                {
                    "ko": "금반지 맡기고 돈 빌리는 게 질권이에요",
                    "vi": "Cầm nhẫn vàng để vay tiền chính là quyền cầm cố",
                    "situation": "informal"
                },
                {
                    "ko": "현장에서 장비를 질권으로 제공하려면 실제로 인도해야 합니다",
                    "vi": "Để cầm thiết bị tại hiện trường, phải thực sự giao nộp",
                    "situation": "onsite"
                }
            ],
            "relatedTerms": ["저당권", "동산담보", "우선변제권", "전당포"]
        },
        {
            "slug": "quyen-the-chap-bat-dong-san",
            "korean": "저당권",
            "vietnamese": "Quyền thế chấp bất động sản",
            "hanja": "抵當權",
            "hanjaReading": "抵(막을 저) 當(마땅 당) 權(권세 권)",
            "pronunciation": "저당권",
            "meaningKo": "채무자 또는 제3자가 점유를 이전하지 않고 채무의 담보로 제공한 부동산에 대해, 채권자가 다른 채권자보다 우선하여 변제받을 수 있는 담보물권입니다. 통역 시 저당권은 부동산 등기를 통해 공시되고, 설정자가 계속 사용할 수 있다는 점에서 질권과 구분된다는 점을 명확히 해야 합니다. 베트남 민법에서도 'quyền thế chấp bất động sản'으로 동일하게 규정하며, 은행 대출 시 가장 일반적인 담보 수단입니다. 통역 시 저당권 설정 등기, 순위, 피담보채권 범위, 실행 방법을 명확히 전달하고, 후순위 저당권의 위험성을 설명해야 합니다. 베트남에서는 'sổ đỏ(레드북, 부동산 등기증)'에 저당권이 기재되므로 계약 시 반드시 확인해야 합니다.",
            "meaningVi": "Quyền bảo đảm bằng bất động sản mà không cần giao quyền chiếm hữu, chủ nợ có quyền ưu tiên thanh toán khi bán tài sản thế chấp nếu không trả nợ. Quyền thế chấp được đăng ký tại sổ đỏ (giấy chứng nhận quyền sử dụng đất), người đặt thế chấp vẫn có thể tiếp tục sử dụng tài sản. Đây là phương thức bảo đảm phổ biến nhất khi vay ngân hàng.",
            "context": "부동산 대출, 담보 설정, 경매 절차 시",
            "culturalNote": "한국과 베트남 모두 저당권 제도가 유사하지만, 베트남은 저당권 실행 절차가 복잡하고 시간이 오래 걸려 한국 기업이 예상보다 채권 회수가 어려울 수 있습니다. 베트남에서는 저당권 실행 시 법원 경매가 아닌 협의매각을 우선하는 경향이 있으며, 통역 시 양 당사자에게 매각 방법을 명확히 합의하도록 조언해야 합니다. 베트남은 토지 사용권과 건물 소유권이 분리되어 저당권 설정 시 두 가지를 모두 확인해야 하므로, 통역 시 이 차이를 설명하고 '토지+건물' 일괄 저당 설정을 권장해야 합니다. 베트남에서는 저당권 말소 절차가 지연되는 경우가 많아, 채무 변제 후 즉시 말소 등기를 진행하도록 통역사가 독촉해야 합니다.",
            "commonMistakes": [
                {
                    "mistake": "저당권 설정하면 부동산을 사용할 수 없다고 설명",
                    "correction": "저당권은 점유 이전 없이 계속 사용 가능",
                    "explanation": "저당권의 핵심은 비점유 담보, 설정자가 계속 사용"
                },
                {
                    "mistake": "저당권 순위가 중요하지 않다고 설명",
                    "correction": "후순위는 선순위 변제 후 배당, 위험 높음",
                    "explanation": "경매 시 선순위부터 변제하므로 후순위는 받지 못할 수 있음"
                },
                {
                    "mistake": "저당권 실행이 즉시 가능하다고 설명",
                    "correction": "베트남은 절차가 복잡하고 6개월~1년 소요",
                    "explanation": "베트남은 저당권 실행 절차가 한국보다 느림"
                }
            ],
            "examples": [
                {
                    "ko": "본 아파트에 1순위 저당권 3억원, 2순위 저당권 1억원이 설정되어 있습니다",
                    "vi": "Căn hộ này có quyền thế chấp hạng 1 là 300 triệu won, hạng 2 là 100 triệu won",
                    "situation": "formal"
                },
                {
                    "ko": "집을 담보로 은행에서 돈 빌리는 게 저당권이에요",
                    "vi": "Thế chấp nhà để vay tiền ngân hàng chính là quyền thế chấp",
                    "situation": "informal"
                },
                {
                    "ko": "현장 부동산에 저당권 있는지 sổ đỏ 확인하세요",
                    "vi": "Hãy kiểm tra sổ đỏ xem bất động sản tại hiện trường có quyền thế chấp không",
                    "situation": "onsite"
                }
            ],
            "relatedTerms": ["질권", "경매", "우선변제권", "근저당권"]
        },
        {
            "slug": "chuyen-nhuong-dam-bao",
            "korean": "양도담보",
            "vietnamese": "Chuyển nhượng담보",
            "hanja": "讓渡擔保",
            "hanjaReading": "讓(사양할 양) 渡(건널 도) 擔(멜 담) 保(지킬 보)",
            "pronunciation": "양도담보",
            "meaningKo": "채무의 담보로 목적물의 소유권을 채권자에게 이전하되, 채무 변제 시 다시 반환받기로 하는 담보 방법입니다. 통역 시 양도담보는 명의는 채권자에게 이전되지만 실질적 소유권은 채무자에게 남는다는 점을 명확히 해야 하며, 저당권과 달리 등기 없이도 가능하다는 점을 설명해야 합니다. 베트남 민법은 양도담보 개념이 명확하지 않아 'chuyển quyền sở hữu để bảo đảm(소유권 이전 담보)'로 설명해야 하며, 실무상 분쟁 소지가 많아 통역 시 주의가 필요합니다. 통역사는 양도담보의 위험성(채권자가 임의 처분 가능성)을 설명하고, 가능하면 저당권 등 등기된 담보를 사용하도록 권장해야 합니다. 베트남에서는 양도담보가 매매로 오인되어 법적 분쟁이 발생할 수 있습니다.",
            "meaningVi": "Phương thức bảo đảm bằng cách chuyển quyền sở hữu tài sản cho chủ nợ, nhưng khi trả nợ sẽ nhận lại. Tên nghĩa thuộc chủ nợ nhưng quyền sở hữu thực chất vẫn của người vay. Khác với thế chấp, có thể thực hiện mà không cần đăng ký. Luật Việt Nam không quy định rõ ràng, dễ gây tranh chấp vì có thể nhầm với mua bán thực sự.",
            "context": "동산 담보, 재고자산 담보, 기업 대출 시",
            "culturalNote": "한국은 양도담보가 판례법으로 인정되지만, 베트남은 법적 근거가 불명확하여 통역 시 매우 신중해야 합니다. 베트남에서는 양도담보를 '가장 매매(bán giả)'로 오해하거나, 채권자가 실제 소유권을 주장하여 분쟁이 발생하는 경우가 많습니다. 통역사는 양도담보 계약서에 '담보 목적임'을 명확히 기재하고, 채무 변제 시 소유권 반환 조건을 상세히 명시하도록 조언해야 합니다. 베트남 법원은 양도담보를 인정하지 않고 실제 매매로 판단하는 경향이 있어, 한국 기업이 담보로 제공한 재산을 회수하지 못하는 사례가 있으므로 통역 시 이 위험을 경고해야 합니다. 가능하면 베트남에서는 양도담보 대신 등기된 저당권이나 질권 사용을 권장하는 것이 안전합니다.",
            "commonMistakes": [
                {
                    "mistake": "양도담보와 매매를 구분하지 않음",
                    "correction": "양도담보는 담보 목적, 매매는 소유권 완전 이전",
                    "explanation": "양도담보는 조건부 소유권 이전으로 매매와 다름"
                },
                {
                    "mistake": "양도담보가 베트남에서도 안전하다고 설명",
                    "correction": "베트남은 법적 근거 미흡, 분쟁 위험 높음",
                    "explanation": "베트남 법원은 양도담보를 인정하지 않는 경향"
                },
                {
                    "mistake": "양도담보는 등기 불요라고만 설명",
                    "correction": "등기 없어 제3자 대항력 없어 위험",
                    "explanation": "등기 없으면 채권자가 제3자에게 재매각 시 보호 안 됨"
                }
            ],
            "examples": [
                {
                    "ko": "재고자산을 양도담보로 제공하되, 대출 상환 시 소유권을 반환받습니다",
                    "vi": "Chuyển quyền sở hữu hàng tồn kho làm bảo đảm, khi trả nợ sẽ nhận lại quyền sở hữu",
                    "situation": "formal"
                },
                {
                    "ko": "일단 명의를 넘기지만 돈 갚으면 다시 받는 게 양도담보예요",
                    "vi": "Tạm chuyển tên nghĩa nhưng khi trả tiền sẽ nhận lại, đó là chuyển nhượng담보",
                    "situation": "informal"
                },
                {
                    "ko": "현장 장비를 양도담보로 제공할 때는 계약서에 담보 목적을 명확히 쓰세요",
                    "vi": "Khi chuyển nhượng thiết bị hiện trường làm담보, hãy ghi rõ mục đích bảo đảm trong hợp đồng",
                    "situation": "onsite"
                }
            ],
            "relatedTerms": ["저당권", "소유권이전", "담보권", "가등기담보"]
        },
        {
            "slug": "quyen-dia-thuong-phap-dinh",
            "korean": "법정지상권",
            "vietnamese": "Quyền địa thượng pháp định",
            "hanja": "法定地上權",
            "hanjaReading": "法(법 법) 定(정할 정) 地(땅 지) 上(위 상) 權(권세 권)",
            "pronunciation": "법정지상권",
            "meaningKo": "토지와 건물의 소유자가 달라진 경우, 건물 소유자가 토지를 사용할 수 있는 법정 권리입니다. 통역 시 법정지상권은 당사자 합의 없이도 법률상 당연히 발생하며, 주로 저당권 실행으로 토지와 건물 소유자가 분리될 때 성립한다는 점을 명확히 해야 합니다. 베트남은 토지 국유제로 '토지 사용권'과 '건물 소유권'이 원래 분리되어 있어, 한국의 법정지상권 개념이 적용되지 않습니다. 통역 시 이 근본적 차이를 설명하고, 베트남에서는 토지 사용권 이전 시 건물도 함께 이전되는 것이 원칙임을 전달해야 합니다. 한국 기업이 베트남 부동산에 투자 시 토지와 건물의 법적 관계를 명확히 이해하도록 통역사가 조력해야 합니다.",
            "meaningVi": "Quyền sử dụng đất được pháp luật quy định khi chủ sở hữu đất và chủ sở hữu công trình trên đất khác nhau. Ở Hàn Quốc, khi đất và nhà thuộc về chủ khác nhau (thường do bán đấu giá thế chấp), chủ nhà tự động có quyền sử dụng đất. Tuy nhiên, Việt Nam là chế độ đất công hữu nên không có khái niệm này, quyền sử dụng đất và quyền sở hữu nhà thường đi kèm nhau.",
            "context": "경매, 부동산 거래, 건물 철거 분쟁 시",
            "culturalNote": "한국은 토지와 건물이 별개 부동산으로 각각 거래 가능하지만, 베트남은 토지 사용권과 건물 소유권이 원칙적으로 분리 불가능하여 법정지상권 개념이 없습니다. 통역 시 한국의 법정지상권 설명이 베트남인에게 혼란을 줄 수 있으므로, '토지와 건물이 다른 사람 소유일 때 건물주가 땅을 쓸 수 있는 권리'로 쉽게 풀어 설명해야 합니다. 베트남에서는 건물을 지으면 자동으로 토지 사용권도 취득하는 것이 일반적이며, 토지만 따로 거래하는 경우는 드뭅니다. 통역사는 한국 법정지상권 관련 분쟁을 베트남에 유추 적용하지 않도록 주의하고, 각국의 부동산 제도 차이를 명확히 설명해야 합니다.",
            "commonMistakes": [
                {
                    "mistake": "베트남에도 법정지상권이 있다고 설명",
                    "correction": "베트남은 토지 국유제로 법정지상권 개념 없음",
                    "explanation": "토지 사용권과 건물 소유권이 원칙적으로 함께 이동"
                },
                {
                    "mistake": "법정지상권은 등기해야 한다고 설명",
                    "correction": "법정지상권은 법률상 당연 발생, 등기 불요",
                    "explanation": "법정지상권은 요건 충족 시 자동 성립"
                },
                {
                    "mistake": "법정지상권자는 토지를 무상 사용한다고 설명",
                    "correction": "지료 지급 의무 있음, 협의 안 되면 법원 결정",
                    "explanation": "법정지상권도 유상 사용이 원칙"
                }
            ],
            "examples": [
                {
                    "ko": "경매로 토지만 낙찰받았으나 건물주가 법정지상권을 주장하고 있습니다",
                    "vi": "Tôi đã mua đất qua đấu giá nhưng chủ nhà đang yêu cầu quyền sử dụng đất theo pháp luật",
                    "situation": "formal"
                },
                {
                    "ko": "땅 주인이 바뀌어도 건물주는 계속 땅을 쓸 수 있어요. 법정지상권이거든요",
                    "vi": "Dù chủ đất thay đổi, chủ nhà vẫn có thể tiếp tục dùng đất. Đó là quyền địa thượng pháp định",
                    "situation": "informal"
                },
                {
                    "ko": "현장 건물에 법정지상권 성립하면 철거 못하니 주의하세요",
                    "vi": "Nếu công trình tại hiện trường có quyền địa thượng pháp định thì không thể phá dỡ, hãy cẩn thận",
                    "situation": "onsite"
                }
            ],
            "relatedTerms": ["지상권", "토지사용권", "경매", "저당권"]
        },
        {
            "slug": "quyen-dat-mo",
            "korean": "분묘기지권",
            "vietnamese": "Quyền đất mộ",
            "hanja": "墳墓基地權",
            "hanjaReading": "墳(무덤 분) 墓(무덤 묘) 基(터 기) 地(땅 지) 權(권세 권)",
            "pronunciation": "분묘기지권",
            "meaningKo": "타인 소유 토지에 조상의 분묘를 설치한 경우, 관습법상 인정되는 토지 사용권입니다. 통역 시 분묘기지권은 등기 없이도 성립하고 토지 소유자에게 대항할 수 있으며, 한국 고유의 관습법으로 베트남에는 존재하지 않는다는 점을 명확히 해야 합니다. 베트남은 묘지를 공공묘지(nghĩa trang công cộng)에만 조성하도록 하고 있어, 사유지에 분묘를 설치하는 한국의 관습이 이해되지 않을 수 있습니다. 통역 시 분묘기지권은 한국의 유교 문화와 조상 숭배 전통에서 비롯된 특수한 권리임을 설명하고, 베트남에서는 유사한 권리가 인정되지 않는다는 점을 전달해야 합니다. 한국인이 베트남 토지에 분묘 설치를 시도하면 법적 문제가 발생할 수 있으므로 통역사가 사전에 경고해야 합니다.",
            "meaningVi": "Quyền sử dụng đất để đặt mộ tổ tiên trên đất người khác theo tập quán ở Hàn Quốc. Đây là quyền đặc thù của Hàn Quốc xuất phát từ văn hóa Nho giáo và thờ cúng tổ tiên, không cần đăng ký vẫn có hiệu lực. Việt Nam không có quyền này vì luật quy định mộ phải đặt tại nghĩa trang công cộng, không được đặt trên đất tư nhân tùy tiện.",
            "context": "토지 매매, 분묘 이전 협상, 상속 분쟁 시",
            "culturalNote": "한국은 조상 숭배 문화가 강해 분묘기지권이 관습법으로 인정되지만, 베트남은 묘지를 공공시설로만 허용하여 분묘기지권 개념 자체가 없습니다. 베트남인에게 한국의 분묘기지권을 설명할 때는 '조상의 무덤이 있는 땅을 계속 사용할 수 있는 한국의 특별한 권리'로 문화적 맥락을 함께 전달해야 이해가 쉽습니다. 베트남에서는 사유지에 무단으로 묘를 조성하면 불법 건축물로 간주되어 철거 명령을 받을 수 있으므로, 한국 교민이 베트남에서 묘지를 조성하려 할 때 통역사가 법적 절차를 명확히 안내해야 합니다. 베트남은 화장 문화가 확산되고 있어 묘지에 대한 인식이 한국과 다르므로, 통역 시 문화적 차이를 존중하며 중립적으로 설명해야 합니다.",
            "commonMistakes": [
                {
                    "mistake": "베트남에도 분묘기지권이 있다고 설명",
                    "correction": "베트남은 공공묘지만 허용, 분묘기지권 없음",
                    "explanation": "베트남은 사유지 묘지 설치 금지"
                },
                {
                    "mistake": "분묘기지권은 영구적이라고 설명",
                    "correction": "토지 소유자가 상당 기간 경과 후 이장 청구 가능",
                    "explanation": "한국도 60년 경과 등 요건 충족 시 이장 가능"
                },
                {
                    "mistake": "분묘기지권은 유상이라고 설명",
                    "correction": "관습법상 무상 사용 원칙, 지료 지급 불요",
                    "explanation": "분묘기지권은 무상 사용이 원칙이나 협의로 지료 가능"
                }
            ],
            "examples": [
                {
                    "ko": "이 토지에는 조상 묘가 있어 분묘기지권이 인정되므로 함부로 개발할 수 없습니다",
                    "vi": "Đất này có mộ tổ tiên nên được công nhận quyền đất mộ, không thể tùy tiện phát triển",
                    "situation": "formal"
                },
                {
                    "ko": "할아버지 산소가 있는 땅은 분묘기지권으로 보호받아요",
                    "vi": "Đất có mộ ông nội được bảo vệ bởi quyền đất mộ",
                    "situation": "informal"
                },
                {
                    "ko": "현장 토지에 분묘 있으면 개발 전에 이장 협상 먼저 하세요",
                    "vi": "Nếu đất hiện trường có mộ, hãy thương lượng di chuyển trước khi phát triển",
                    "situation": "onsite"
                }
            ],
            "relatedTerms": ["관습법", "지상권", "묘지", "이장"]
        },
        {
            "slug": "cong-huu",
            "korean": "공유",
            "vietnamese": "Công hữu",
            "hanja": "共有",
            "hanjaReading": "共(한가지 공) 有(있을 유)",
            "pronunciation": "공유",
            "meaningKo": "하나의 물건을 여러 사람이 지분에 따라 공동으로 소유하는 것입니다. 통역 시 공유는 각 공유자가 지분 비율에 따라 권리를 가지며, 지분 처분은 자유롭지만 물건 전체의 처분은 공유자 전원의 동의가 필요하다는 점을 명확히 해야 합니다. 베트남 민법에서도 'sở hữu chung(공동 소유)'로 규정하며, 부부 공동재산, 상속재산 분할 전 등이 대표적 사례입니다. 통역 시 공유물 관리 방법(보존행위, 관리행위, 변경행위), 공유물 분할 청구권, 지분 매각 시 우선 매수권 등을 명확히 전달하고, 공유 관계 해소 방법을 설명해야 합니다. 베트남에서는 공유물 분할 시 현물 분할을 선호하나, 불가능한 경우 경매를 통한 대금 분할도 가능합니다.",
            "meaningVi": "Việc nhiều người cùng sở hữu một tài sản theo tỷ lệ phần. Mỗi người có quyền theo tỷ lệ của mình, có thể tự do định đoạt phần của mình nhưng việc định đoạt toàn bộ tài sản cần sự đồng ý của tất cả. Ví dụ điển hình là tài sản chung vợ chồng, tài sản thừa kế chưa chia. Có thể yêu cầu phân chia tài sản chung, ưu tiên chia thực hoặc bán đấu giá chia tiền.",
            "context": "부동산 공동 구매, 상속, 이혼 재산분할 시",
            "culturalNote": "한국은 공유 관계를 법률적으로 명확히 구분(공유, 합유, 총유)하지만, 베트남은 실무상 단순히 'sở hữu chung(공동 소유)'로 통칭하는 경우가 많아 통역 시 주의가 필요합니다. 베트남에서는 공유 부동산 관리 시 공유자 간 합의가 잘 안 되면 분쟁이 장기화되는 경우가 많으며, 통역사는 초기 단계에서 관리 규약을 명확히 작성하도록 조언해야 합니다. 베트남은 가족 중심 문화가 강해 형제자매 간 공유 부동산을 분할하지 않고 장기간 공동 사용하는 경향이 있어, 한국의 신속한 분할 문화와 차이가 있습니다. 통역 시 양국의 문화 차이를 이해하고, 공유자 간 갈등을 최소화할 수 있는 합리적 관리 방안을 제시해야 합니다.",
            "commonMistakes": [
                {
                    "mistake": "공유 지분을 마음대로 사용할 수 있다고 설명",
                    "correction": "지분은 관념적, 물건 전체를 지분 비율로 사용",
                    "explanation": "공유는 물건 특정 부분이 아닌 전체에 대한 비율적 권리"
                },
                {
                    "mistake": "공유자 과반수 동의로 매각 가능하다고 설명",
                    "correction": "매각은 공유자 전원 동의 필요",
                    "explanation": "변경행위는 전원 동의, 관리행위는 과반수 동의"
                },
                {
                    "mistake": "공유물 분할은 항상 현물 분할이라고 설명",
                    "correction": "현물 분할 불가 시 경매 후 대금 분할",
                    "explanation": "물건 성질상 분할 곤란하면 경매로 환가 후 분배"
                }
            ],
            "examples": [
                {
                    "ko": "이 아파트는 형제 3명이 각 1/3씩 공유하고 있습니다",
                    "vi": "Căn hộ này do 3 anh em cùng sở hữu, mỗi người 1/3",
                    "situation": "formal"
                },
                {
                    "ko": "공동 명의니까 한 사람이 혼자 팔 수는 없어요",
                    "vi": "Vì là tên chung nên một người không thể bán một mình",
                    "situation": "informal"
                },
                {
                    "ko": "현장 토지가 공유라면 전원 동의서 받아야 계약 진행됩니다",
                    "vi": "Nếu đất hiện trường là công hữu, cần có chữ ký đồng ý của tất cả mới tiến hành hợp đồng",
                    "situation": "onsite"
                }
            ],
            "relatedTerms": ["지분", "공유물분할", "합유", "총유"]
        },
        {
            "slug": "so-huu-phan-chia",
            "korean": "구분소유",
            "vietnamese": "Sở hữu phân chia",
            "hanja": "區分所有",
            "hanjaReading": "區(나눌 구) 分(나눌 분) 所(바 소) 有(있을 유)",
            "pronunciation": "구분소유",
            "meaningKo": "1동의 건물에서 구조상 구분된 여러 부분을 각각 소유권의 목적으로 하는 것입니다. 통역 시 구분소유는 아파트, 오피스텔 등 집합건물에서 전유부분과 공용부분을 구분하며, 전유부분은 각 소유자의 단독 소유이고 공용부분은 전체 소유자의 공유라는 점을 명확히 해야 합니다. 베트남 민법에서도 'sở hữu riêng và sở hữu chung trong chung cư(아파트의 전유부분과 공용부분)'로 규정하며, 한국과 유사한 제도를 운영합니다. 통역 시 관리비 부담, 공용부분 사용, 관리단 운영 등 실무적 사항을 명확히 전달하고, 구분소유자의 권리와 의무를 설명해야 합니다. 베트nam에서는 아파트 관리가 아직 체계화되지 않아 분쟁이 많으므로 통역사가 관리규약의 중요성을 강조해야 합니다.",
            "meaningVi": "Chế độ sở hữu trong đó các phần được phân chia theo cấu trúc của một tòa nhà (như chung cư, cao ốc văn phòng) đều là đối tượng của quyền sở hữu riêng. Phần riêng thuộc sở hữu riêng của từng chủ, phần chung (hành lang, thang máy, mái nhà) thuộc sở hữu chung của tất cả. Luật Việt Nam cũng quy định tương tự cho chung cư.",
            "context": "아파트 거래, 집합건물 관리, 재건축 논의 시",
            "culturalNote": "한국은 구분소유법이 정교하게 발달하여 아파트 관리가 체계적이지만, 베트남은 아파트 문화가 최근에 발달하여 관리 시스템이 미흡한 편입니다. 베트남에서는 아파트 공용부분 관리, 관리비 징수, 하자 책임 등에서 분쟁이 많으며, 통역사는 한국의 선진 관리 사례를 소개하며 체계적 관리의 중요성을 설명해야 합니다. 베트남은 아파트 관리조합 운영 경험이 부족하여 소수 입주자가 전횡하는 경우가 많고, 통역 시 민주적 의사결정 절차를 강조해야 합니다. 한국 기업이 베트남에 아파트를 분양할 때는 관리규약을 명확히 작성하고, 관리비 산정 기준, 공용부분 사용 규칙 등을 사전에 통역하여 입주자에게 공지해야 합니다. 베트남은 아파트 재건축 경험이 거의 없어 한국의 재건축 제도를 설명할 때 문화적 맥락을 고려해야 합니다.",
            "commonMistakes": [
                {
                    "mistake": "공용부분도 임의로 사용할 수 있다고 설명",
                    "correction": "공용부분은 규약에 따라 사용, 임의 변경 금지",
                    "explanation": "공용부분은 전체 소유자의 공유로 개인이 독점 사용 불가"
                },
                {
                    "mistake": "전유부분 구조 변경이 자유롭다고 설명",
                    "correction": "구조 변경은 관리단 동의 필요, 안전 위험",
                    "explanation": "전유부분이라도 건물 전체 안전에 영향 주는 변경은 제한"
                },
                {
                    "mistake": "관리비를 안 내도 된다고 설명",
                    "correction": "구분소유자는 관리비 납부 의무 있음",
                    "explanation": "공용부분 유지를 위한 관리비는 필수 의무"
                }
            ],
            "examples": [
                {
                    "ko": "이 아파트는 전유면적 85㎡, 공용면적 포함 총 110㎡입니다",
                    "vi": "Căn hộ này có diện tích riêng 85m², cộng phần chung tổng 110m²",
                    "situation": "formal"
                },
                {
                    "ko": "아파트는 내 집이지만 복도나 엘리베이터는 공용이라 마음대로 못 해요",
                    "vi": "Căn hộ là nhà tôi nhưng hành lang, thang máy là phần chung nên không thể tùy tiện",
                    "situation": "informal"
                },
                {
                    "ko": "현장 아파트 분양 시 전유부분과 공용부분 면적을 명확히 구분하세요",
                    "vi": "Khi bán chung cư tại hiện trường, hãy phân biệt rõ diện tích riêng và diện tích chung",
                    "situation": "onsite"
                }
            ],
            "relatedTerms": ["집합건물", "전유부분", "공용부분", "관리단"]
        },
        {
            "slug": "uy-탁-danh-nghia",
            "korean": "명의신탁",
            "vietnamese": "Ủy탁 danh nghĩa",
            "hanja": "名義信託",
            "hanjaReading": "名(이름 명) 義(옳을 의) 信(믿을 신) 託(맡길 탁)",
            "pronunciation": "명의신탁",
            "meaningKo": "실제 소유자와 명의자가 다른 경우로, 한국에서는 부동산실명법으로 금지되어 있습니다. 통역 시 명의신탁은 불법이며 명의신탁 약정은 무효이고, 실소유자는 소유권을 주장할 수 없다는 점을 명확히 해야 합니다. 베트남에서도 'ủy thác tên(명의 위탁)'은 법적으로 금지되나 실무상 빈번히 발생하며, 특히 외국인 투자 제한 회피 목적으로 사용되어 법적 문제가 심각합니다. 통역 시 명의신탁의 법적 위험성(소유권 상실, 형사 처벌, 세금 문제)을 강조하고, 합법적인 공동 소유나 법인 설립 등 대안을 제시해야 합니다. 베트남에서는 외국인이 베트남인 명의로 부동산을 취득하는 명의신탁이 많으나, 분쟁 시 외국인이 소유권을 주장할 수 없어 재산을 잃는 사례가 빈번하므로 통역사가 경고해야 합니다.",
            "meaningVi": "Trường hợp chủ sở hữu thực tế và người có tên trên giấy tờ khác nhau, ở Hàn Quốc bị cấm theo luật bất động sản thực danh. Thỏa thuận ủy thác tên vô hiệu, chủ thực không thể yêu cầu quyền sở hữu. Việt Nam cũng cấm nhưng trên thực tế vẫn xảy ra nhiều, đặc biệt là người nước ngoài lách luật hạn chế đầu tư. Rất rủi ro vì có thể mất tài sản khi tranh chấp.",
            "context": "부동산 거래, 외국인 투자, 탈세 조사 시",
            "culturalNote": "한국은 1995년 부동산실명법 시행 이후 명의신탁을 엄격히 단속하지만, 베트남은 법률은 있으나 집행이 느슨하여 명의신탁이 여전히 만연합니다. 베트남에서 외국인이 부동산 취득 제한을 회피하기 위해 베트남인 배우자나 친구 명의로 재산을 등록하는 경우가 많으나, 관계가 틀어지면 재산을 회수할 수 없어 막대한 손실을 입는 사례가 빈번합니다. 통역사는 명의신탁의 위험성을 강력히 경고하고, 외국인이 합법적으로 부동산을 소유할 수 있는 방법(아파트 구매, 법인 설립 등)을 안내해야 합니다. 베트남에서는 명의신탁이 발각되면 재산 몰수 및 강제 퇴거 조치를 받을 수 있으므로, 한국 교민에게 절대 명의신탁을 하지 말라고 통역사가 조언해야 합니다. 베트남 법원은 명의신탁 분쟁 시 명의자에게 유리하게 판결하는 경향이 있어 실소유자 보호가 거의 불가능합니다.",
            "commonMistakes": [
                {
                    "mistake": "명의신탁도 합의만 있으면 유효하다고 설명",
                    "correction": "명의신탁 약정은 무효, 법적 보호 안 됨",
                    "explanation": "한국·베트남 모두 명의신탁 금지, 약정 무효"
                },
                {
                    "mistake": "나중에 명의를 돌려받을 수 있다고 설명",
                    "correction": "명의자가 거부하면 소유권 주장 불가",
                    "explanation": "명의신탁 약정이 무효이므로 법적 청구권 없음"
                },
                {
                    "mistake": "외국인은 명의신탁으로 부동산 취득 가능하다고 설명",
                    "correction": "명의신탁은 불법, 발각 시 재산 몰수 위험",
                    "explanation": "외국인 투자 제한 회피 목적 명의신탁은 엄격히 처벌"
                }
            ],
            "examples": [
                {
                    "ko": "친구 명의로 부동산을 샀으나 명의신탁으로 무효이므로 소유권을 주장할 수 없습니다",
                    "vi": "Tôi mua bất động sản dưới tên bạn nhưng vì ủy thác danh nghĩa là vô hiệu nên không thể yêu cầu quyền sở hữu",
                    "situation": "formal"
                },
                {
                    "ko": "남 이름으로 집 사면 나중에 못 찾아요. 절대 하지 마세요",
                    "vi": "Nếu mua nhà dưới tên người khác, sau này không lấy lại được. Tuyệt đối đừng làm",
                    "situation": "informal"
                },
                {
                    "ko": "현장 부동산 거래 시 명의신탁 의심되면 계약 중단하고 법률 자문 받으세요",
                    "vi": "Nếu nghi ngờ ủy thác danh nghĩa khi giao dịch bất động sản tại hiện trường, hãy dừng hợp đồng và nhận tư vấn pháp lý",
                    "situation": "onsite"
                }
            ],
            "relatedTerms": ["부동산실명법", "소유권", "외국인투자", "탈세"]
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
