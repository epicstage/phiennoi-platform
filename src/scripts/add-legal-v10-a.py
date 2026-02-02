#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""계약법 심화 용어 추가 (v10-A)"""
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
            "slug": "dam-bao-thuc-hien",
            "korean": "이행보증",
            "vietnamese": "Đảm bảo thực hiện",
            "hanja": "履行保證",
            "hanjaReading": "履(밟을 리) 行(다닐 행) 保(지킬 보) 證(증거 증)",
            "pronunciation": "이행보증",
            "meaningKo": "계약상 채무를 이행할 것을 담보하기 위해 제공하는 보증을 의미합니다. 통역 시 베트남에서는 은행보증서(thư bảo lãnh ngân hàng)와 현금담보(tiền đặt cọc)를 엄격히 구분하므로, 보증의 형태를 명확히 확인해야 합니다. 건설계약에서 이행보증금은 계약금액의 10% 내외로 설정되며, 공사 완료 후 반환됩니다. 계약 미이행 시 보증금이 몰수되므로 통역 시 이행의무 범위를 정확히 전달해야 합니다.",
            "meaningVi": "Bảo đảm được cung cấp để đảm bảo việc thực hiện nghĩa vụ hợp đồng. Thường được thực hiện thông qua thư bảo lãnh ngân hàng hoặc tiền đặt cọc. Trong hợp đồng xây dựng, tiền bảo lãnh thực hiện thường chiếm khoảng 10% giá trị hợp đồng.",
            "context": "계약 체결, 공사 입찰, 건설 계약서 작성 시",
            "culturalNote": "한국은 이행보증보험이 발달했지만 베트남은 은행보증서가 주류입니다. 베트남에서 보증서 발급 비용은 보증금액의 1-2%이며, 한국보다 발급 절차가 까다롭습니다. 베트남 기업들은 현금 담보를 선호하는 경향이 있어 협상 시 이 차이를 이해하고 통역해야 합니다. 또한 베트남에서는 이행보증이 지연될 경우 계약 자체가 무효화될 수 있어 주의가 필요합니다.",
            "commonMistakes": [
                {
                    "mistake": "bảo hiểm thực hiện",
                    "correction": "đảm bảo thực hiện (bảo lãnh thực hiện)",
                    "explanation": "bảo hiểm은 보험(insurance)을 의미하므로 보증(guarantee)과 혼동하면 안 됨. bảo lãnh이 정확한 법률용어"
                },
                {
                    "mistake": "tiền đặt cọc와 혼동",
                    "correction": "đặt cọc은 계약금, bảo lãnh은 이행보증",
                    "explanation": "계약금은 계약 체결의 증표이고 이행보증은 이행 담보 수단으로 법적 성격이 다름"
                },
                {
                    "mistake": "보증 만료일을 명시하지 않음",
                    "correction": "ngày hết hiệu lực bảo lãnh 반드시 명시",
                    "explanation": "베트남 은행보증서는 유효기간이 엄격하므로 만료일을 정확히 통역해야 함"
                }
            ],
            "examples": [
                {
                    "ko": "낙찰자는 계약체결 후 7일 이내에 계약금액의 10%에 해당하는 이행보증서를 제출해야 합니다",
                    "vi": "Bên trúng thầu phải nộp thư bảo lãnh thực hiện tương đương 10% giá trị hợp đồng trong vòng 7 ngày sau khi ký hợp đồng",
                    "situation": "formal"
                },
                {
                    "ko": "현장에서 이행보증금 반환 요청하실 때는 준공확인서 원본을 가져오셔야 합니다",
                    "vi": "Khi yêu cầu hoàn trả tiền bảo lãnh thực hiện tại hiện trường, anh phải mang theo bản gốc biên bản nghiệm thu hoàn thành",
                    "situation": "onsite"
                },
                {
                    "ko": "이행보증 없이 계약 진행하면 나중에 문제 생길 수 있어요",
                    "vi": "Nếu tiến hành hợp đồng mà không có bảo lãnh thực hiện thì sau này có thể gặp vấn đề đấy",
                    "situation": "informal"
                }
            ],
            "relatedTerms": ["계약보증금", "하자보증", "선급금보증", "유치권"]
        },
        {
            "slug": "tien-boi-thuong-thoa-thuan-truoc",
            "korean": "손해배상예정",
            "vietnamese": "Tiền bồi thường thỏa thuận trước",
            "hanja": "損害賠償豫定",
            "hanjaReading": "損(덜 손) 害(해칠 해) 賠(갚을 배) 償(갚을 상) 豫(미리 예) 定(정할 정)",
            "pronunciation": "손해배상예정",
            "meaningKo": "계약 위반 시 발생할 손해배상액을 미리 약정하는 조항입니다. 통역 시 베트남에서는 이를 '위약금(tiền phạt vi phạm)'과 혼동하기 쉬우나, 손해배상예정은 실제 손해를 전보하는 성격이 강하고 위약금은 제재적 성격이 강하다는 차이를 명확히 해야 합니다. 베트남 민법은 손해배상예정액이 과도할 경우 법원이 감액할 수 있다고 규정하므로, 통역 시 합리적 범위를 논의할 때 이 점을 고려해야 합니다.",
            "meaningVi": "Điều khoản thỏa thuận trước về số tiền bồi thường thiệt hại khi vi phạm hợp đồng. Khác với tiền phạt vi phạm (mang tính chế재), tiền bồi thường thỏa thuận trước nhằm bù đắp thiệt hại thực tế. Theo luật Việt Nam, tòa án có quyền giảm mức bồi thường nếu thấy quá cao.",
            "context": "계약서 작성, 계약 위반 분쟁, 손해배상 협상 시",
            "culturalNote": "한국은 손해배상예정액을 상당히 높게 책정하는 관행이 있으나, 베트남은 실제 손해에 근접한 수준을 선호합니다. 베트남 법원은 과도한 배상예정액을 직권으로 감액할 수 있어 한국 기업들이 예상보다 낮은 배상을 받는 경우가 많습니다. 통역 시 양 당사자에게 이 문화적 차이를 설명하고, 합리적 수준의 배상액 협상을 돕는 것이 중요합니다. 베트남에서는 보통 계약금액의 5-10% 범위가 적정선으로 인정됩니다.",
            "commonMistakes": [
                {
                    "mistake": "tiền phạt hợp đồng으로 번역",
                    "correction": "tiền bồi thường thỏa thuận trước (liquidated damages)",
                    "explanation": "phạt(벌금)은 제재적 성격, bồi thường(배상)은 손해 전보 성격으로 법적 의미가 다름"
                },
                {
                    "mistake": "실손해 입증 없이 청구 가능하다고 설명",
                    "correction": "베트남에서는 과도한 경우 법원이 감액 가능",
                    "explanation": "한국과 달리 베트남은 손해배상예정도 비례성 원칙 적용"
                },
                {
                    "mistake": "손해배상예정과 위약금을 동시 청구 가능하다고 설명",
                    "correction": "중복 청구 불가, 하나만 선택",
                    "explanation": "베트남 민법은 손해배상과 위약금의 중복 청구를 금지함"
                }
            ],
            "examples": [
                {
                    "ko": "납기 지연 시 1일당 계약금액의 0.1%를 손해배상예정액으로 합니다",
                    "vi": "Trong trường hợp chậm thời hạn giao hàng, tiền bồi thường thỏa thuận trước là 0.1% giá trị hợp đồng cho mỗi ngày chậm",
                    "situation": "formal"
                },
                {
                    "ko": "손해배상예정액은 실제 손해와 관계없이 청구할 수 있지만, 너무 과하면 법원이 깎을 수 있어요",
                    "vi": "Tiền bồi thường thỏa thuận trước có thể yêu cầu không cần chứng minh thiệt hại thực tế, nhưng nếu quá cao thì tòa có thể giảm",
                    "situation": "informal"
                },
                {
                    "ko": "현장에서 지연 발생 시 일일 배상액이 자동으로 누적되니까 공기 관리 철저히 하셔야 합니다",
                    "vi": "Khi có chậm tiến độ tại hiện trường, tiền bồi thường hàng ngày sẽ tự động cộng dồn, nên anh phải quản lý tiến độ nghiêm ngặt",
                    "situation": "onsite"
                }
            ],
            "relatedTerms": ["위약금", "지체상금", "손해배상", "계약해제"]
        },
        {
            "slug": "tien-phat-vi-pham",
            "korean": "위약금",
            "vietnamese": "Tiền phạt vi phạm",
            "hanja": "違約金",
            "hanjaReading": "違(어긋날 위) 約(맺을 약) 金(쇠 금)",
            "pronunciation": "위약금",
            "meaningKo": "계약을 위반한 경우 지급하는 제재적 성격의 금전을 말합니다. 통역 시 손해배상예정액과 구분해야 하며, 위약금은 계약 위반 자체에 대한 제재이고 손해배상은 손해 전보라는 차이를 명확히 해야 합니다. 베트남에서는 위약금을 '계약위반벌금(tiền phạt vi phạm hợp đồng)'으로 이해하며, 일반적으로 계약금액의 10%를 초과할 수 없습니다. 통역 시 한국 계약서의 높은 위약금 조항이 베트남 법원에서 감액될 수 있음을 설명해야 합니다.",
            "meaningVi": "Khoản tiền mang tính chất chế tài phải trả khi vi phạm hợp đồng. Khác với tiền bồi thường thiệt hại (nhằm bù đắp tổn thất), tiền phạt vi phạm là hình thức trừng phạt hành vi vi phạm. Theo pháp luật Việt Nam, tiền phạt vi phạm thường không vượt quá 10% giá trị hợp đồng.",
            "context": "계약 위반, 계약 해제, 분쟁 조정 시",
            "culturalNote": "한국은 위약금을 높게 책정하여 계약 준수를 강제하는 문화가 있으나, 베트남은 과도한 위약금을 법원이 직권으로 감액하는 경향이 강합니다. 베트남 상관습상 위약금은 계약금액의 5-10%가 적정하며, 20%를 초과하면 거의 항상 감액됩니다. 통역 시 한국 기업에게는 베트남의 감액 관행을 사전에 알려주고, 베트남 기업에게는 한국 계약서의 높은 위약금 조항이 한국 문화권에서는 일반적이라는 점을 설명하여 오해를 방지해야 합니다.",
            "commonMistakes": [
                {
                    "mistake": "손해배상과 위약금을 동일하게 번역",
                    "correction": "손해배상은 bồi thường thiệt hại, 위약금은 tiền phạt vi phạm",
                    "explanation": "법적 성격이 다르므로 명확히 구분해야 함. 손해배상은 전보, 위약금은 제재"
                },
                {
                    "mistake": "위약금을 실손해와 별도로 청구 가능하다고 설명",
                    "correction": "베트남은 위약금과 손해배상 중 선택해야 함",
                    "explanation": "베트남 민법 제423조는 위약금과 손해배상의 중복 청구를 제한함"
                },
                {
                    "mistake": "한국 수준의 위약금(30-50%)을 그대로 적용",
                    "correction": "베트남은 10-15%가 적정선, 초과 시 감액 위험",
                    "explanation": "베트남 법원은 과도한 위약금을 직권 감액하므로 현지 기준 고려 필요"
                }
            ],
            "examples": [
                {
                    "ko": "계약 일방이 정당한 사유 없이 계약을 해제하는 경우 계약금액의 15%를 위약금으로 지급합니다",
                    "vi": "Trong trường hợp một bên đơn phương chấm dứt hợp đồng không có lý do chính đáng, bên đó phải trả tiền phạt vi phạm tương đương 15% giá trị hợp đồng",
                    "situation": "formal"
                },
                {
                    "ko": "위약금은 손해배상과 별개로 청구할 수 있나요? - 아니요, 베트남에서는 둘 중 하나만 선택해야 합니다",
                    "vi": "Tiền phạt vi phạm có thể yêu cầu riêng biệt với bồi thường thiệt hại không? - Không, ở Việt Nam chỉ được chọn một trong hai",
                    "situation": "informal"
                },
                {
                    "ko": "현장에서 일방적으로 계약 파기하시면 위약금 물어야 하니까 신중하게 결정하세요",
                    "vi": "Nếu anh đơn phương hủy hợp đồng tại hiện trường thì phải trả tiền phạt vi phạm, nên quyết định thận trọng",
                    "situation": "onsite"
                }
            ],
            "relatedTerms": ["손해배상예정", "계약해제", "계약금몰수", "지체상금"]
        },
        {
            "slug": "cham-dut-hop-dong",
            "korean": "계약해제",
            "vietnamese": "Chấm dứt hợp đồng",
            "hanja": "契約解除",
            "hanjaReading": "契(맺을 계) 約(맺을 약) 解(풀 해) 除(덜 제)",
            "pronunciation": "계약해제",
            "meaningKo": "계약 체결 후 일방 또는 쌍방의 의사표시로 계약을 소급적으로 소멸시키는 것입니다. 통역 시 '계약해지(chấm dứt hợp đồng từ thời điểm hiện tại)'와 구분해야 하며, 해제는 계약이 처음부터 없었던 것처럼 원상회복되고 해지는 장래를 향해 소멸한다는 차이를 명확히 해야 합니다. 베트남 민법은 해제 시 원상회복 의무를 엄격히 규정하므로, 이미 이행된 부분의 반환 방법을 명확히 통역해야 합니다. 계약해제는 상대방의 계약 위반, 불가항력, 쌍방 합의 등의 사유로 가능합니다.",
            "meaningVi": "Việc chấm dứt hợp đồng có hiệu lực hồi tố, khôi phục lại tình trạng ban đầu như thể hợp đồng chưa từng được ký kết. Khác với chấm dứt hợp đồng về sau (hủy hợp đồng từ thời điểm hiện tại), việc giải제 hợp đồng đòi hỏi hoàn trả những gì đã nhận. Có thể thực hiện khi có vi phạm hợp đồng, bất khả kháng hoặc thỏa thuận hai bên.",
            "context": "계약 위반 시, 불가항력 발생 시, 계약 분쟁 시",
            "culturalNote": "한국은 계약해제와 해지를 법률적으로 엄격히 구분하나, 베트남은 실무상 'chấm dứt hợp đồng(계약 종료)'라는 포괄 용어를 자주 사용하여 통역 시 혼란이 생길 수 있습니다. 통역사는 소급효 유무를 명확히 확인하여 해제인지 해지인지 판단해야 합니다. 베트남에서는 계약해제 시 위약금보다 실손해 배상을 우선하는 경향이 있으며, 한국처럼 높은 위약금으로 해결하는 문화가 아니므로 이 차이를 설명해야 합니다. 또한 베트남은 계약해제 통지를 서면으로 엄격히 요구하므로 구두 통지는 효력이 없을 수 있습니다.",
            "commonMistakes": [
                {
                    "mistake": "hủy hợp đồng과 chấm dứt hợp đồng을 구분 없이 사용",
                    "correction": "hủy bỏ hợp đồng(해제, 소급효), chấm dứt từ nay(해지, 장래효)",
                    "explanation": "소급효 유무가 법적 효과에 큰 차이를 만들므로 명확히 구분 필요"
                },
                {
                    "mistake": "구두로 계약해제 통지해도 된다고 설명",
                    "correction": "베트남은 서면 통지 필수, 구두는 효력 없음",
                    "explanation": "베트남 민법은 중요한 의사표시는 서면 원칙"
                },
                {
                    "mistake": "계약해제 시 위약금만 지급하면 끝이라고 설명",
                    "correction": "원상회복 + 손해배상 의무 별도 발생 가능",
                    "explanation": "해제는 위약금과 별개로 원상회복 및 실손해 배상 의무가 있음"
                }
            ],
            "examples": [
                {
                    "ko": "귀사의 중대한 계약 위반으로 인해 본 계약을 해제하고 원상회복을 청구합니다",
                    "vi": "Do công ty quý vị vi phạm hợp đồng nghiêm trọng, chúng tôi chấm dứt hợp đồng này có hiệu lực hồi tố và yêu cầu khôi phục nguyên trạng",
                    "situation": "formal"
                },
                {
                    "ko": "계약 해제하면 지금까지 받은 돈 다 돌려줘야 해요",
                    "vi": "Nếu giải제 hợp đồng thì phải hoàn trả toàn bộ số tiền đã nhận",
                    "situation": "informal"
                },
                {
                    "ko": "현장에서 계약 해제 통지서 받으셨으면 즉시 작업 중단하시고 본사에 보고하세요",
                    "vi": "Nếu nhận được thông báo chấm dứt hợp đồng tại hiện trường, anh hãy dừng công việc ngay và báo cáo cho trụ sở chính",
                    "situation": "onsite"
                }
            ],
            "relatedTerms": ["계약해지", "원상회복", "위약금", "손해배상"]
        },
        {
            "slug": "cham-dut-hop-dong-tu-nay",
            "korean": "계약해지",
            "vietnamese": "Chấm dứt hợp đồng từ nay",
            "hanja": "契約解止",
            "hanjaReading": "契(맺을 계) 約(맺을 약) 解(풀 해) 止(그칠 지)",
            "pronunciation": "계약해지",
            "meaningKo": "계약의 효력을 장래를 향해 소멸시키는 것으로, 이미 이행된 부분은 유효하게 존속하고 앞으로의 이행 의무만 소멸합니다. 통역 시 계약해제와의 차이를 명확히 해야 하며, 해지는 원상회복 의무가 없고 이미 이행된 부분의 대가는 반환하지 않는다는 점을 설명해야 합니다. 베트남에서는 'chấm dứt hợp đồng từ thời điểm hiện tại' 또는 'hủy bỏ từ nay về sau'라고 표현하며, 계속적 계약(임대차, 고용 등)에서 주로 사용됩니다. 통역 시 해지 사유, 해지 통지 기간, 정산 방법을 명확히 전달해야 합니다.",
            "meaningVi": "Chấm dứt hiệu lực hợp đồng từ thời điểm hiện tại trở đi, phần đã thực hiện vẫn có hiệu lực và không cần hoàn trả. Khác với giải제 hợp đồng (có hiệu lực hồi tố), việc chấm dứt hợp đồng về sau chỉ ảnh hưởng đến nghĩa vụ tương lai. Thường áp dụng cho hợp đồng liên tục như thuê nhà, lao động.",
            "context": "임대차 계약, 고용 계약, 장기 공급 계약 종료 시",
            "culturalNote": "한국은 법률적으로 해제와 해지를 엄격히 구분하지만, 베트남 실무에서는 두 개념을 혼용하는 경우가 많아 통역 시 주의가 필요합니다. 베트남에서는 계약해지 시 통지 기간을 중시하며, 특히 고용계약은 최소 30일 전 통지가 필요합니다. 한국은 즉시 해지 관행이 있으나 베트남은 통지 기간 미준수 시 손해배상 의무가 발생할 수 있습니다. 통역 시 양국의 통지 기간 차이를 설명하고, 충분한 여유를 두고 해지 절차를 밟도록 조언해야 합니다.",
            "commonMistakes": [
                {
                    "mistake": "해제와 해지를 구분하지 않고 모두 hủy hợp đồng으로 번역",
                    "correction": "해제는 hủy có hiệu lực hồi tố, 해지는 chấm dứt từ nay",
                    "explanation": "원상회복 의무 유무가 달라지므로 정확한 구분 필수"
                },
                {
                    "mistake": "해지 통지 없이 일방적으로 중단 가능하다고 설명",
                    "correction": "베트남은 사전 통지 기간 필수, 위반 시 배상 책임",
                    "explanation": "베트남 민법은 일방 당사자 보호를 위해 통지 기간을 엄격히 규정"
                },
                {
                    "mistake": "해지 후 이미 받은 대가를 반환해야 한다고 설명",
                    "correction": "해지는 장래효만 있어 이미 이행된 부분은 유효",
                    "explanation": "해지는 원상회복 의무가 없으므로 과거 대가는 반환 불요"
                }
            ],
            "examples": [
                {
                    "ko": "본 계약은 일방 당사자가 30일 전 서면 통지로 해지할 수 있습니다",
                    "vi": "Hợp đồng này có thể được chấm dứt bởi một bên thông qua thông báo bằng văn bản trước 30 ngày",
                    "situation": "formal"
                },
                {
                    "ko": "계약 해지해도 이미 일한 달 월급은 받을 수 있어요",
                    "vi": "Dù chấm dứt hợp đồng, anh vẫn được nhận lương tháng đã làm việc",
                    "situation": "informal"
                },
                {
                    "ko": "현장 작업 중단하려면 30일 전에 해지 통지서 보내셔야 합니다",
                    "vi": "Để dừng công việc tại hiện trường, anh phải gửi thông báo chấm dứt trước 30 ngày",
                    "situation": "onsite"
                }
            ],
            "relatedTerms": ["계약해제", "통지기간", "임대차계약", "고용계약"]
        },
        {
            "slug": "thuc-hien-dong-thoi",
            "korean": "동시이행",
            "vietnamese": "Thực hiện đồng thời",
            "hanja": "同時履行",
            "hanjaReading": "同(한가지 동) 時(때 시) 履(밟을 리) 行(다닐 행)",
            "pronunciation": "동시이행",
            "meaningKo": "쌍무계약에서 양 당사자의 채무를 동시에 이행하도록 하는 원칙입니다. 통역 시 '상대방이 이행하기 전까지 나도 이행하지 않을 수 있다'는 동시이행 항변권의 개념을 명확히 전달해야 합니다. 베트남 민법에서도 'quyền từ chối thực hiện nghĩa vụ(의무 이행 거절권)'으로 유사한 제도가 있으나, 한국보다 요건이 까다로우므로 통역 시 주의가 필요합니다. 매매계약에서 물건 인도와 대금 지급의 동시이행이 대표적 사례이며, 어느 한쪽이 먼저 이행하지 않으면 상대방도 이행을 거절할 수 있습니다.",
            "meaningVi": "Nguyên tắc thực hiện nghĩa vụ đồng thời trong hợp đồng song vụ. Nếu một bên không thực hiện nghĩa vụ, bên kia có quyền từ chối thực hiện nghĩa vụ của mình (quyền kháng biện đồng thời). Trong hợp đồng mua bán, giao hàng và thanh toán tiền thường được thực hiện đồng thời theo nguyên tắc này.",
            "context": "매매계약, 물건 인도, 대금 지급 협상 시",
            "culturalNote": "한국은 동시이행 원칙이 강하게 적용되어 '물건 주면 돈 주고, 돈 주면 물건 준다'는 인식이 강하지만, 베트남은 선이행 관행이 많아 통역 시 이 차이를 설명해야 합니다. 특히 건설 현장에서 한국 기업은 기성금 지급 후 작업을 기대하지만, 베트남 하청업체는 작업 완료 후 대금 지급을 기대하는 경우가 많아 분쟁이 발생합니다. 통역사는 동시이행 조건을 명확히 문서화하고, 중간 검수 단계를 두어 양측의 리스크를 줄이도록 조율해야 합니다. 베트남에서는 신뢰 관계가 형성되기 전까지는 은행 보증 등을 통한 동시이행을 선호합니다.",
            "commonMistakes": [
                {
                    "mistake": "상대방이 먼저 이행해야 한다고 주장",
                    "correction": "동시이행 원칙상 양쪽이 동시에 이행",
                    "explanation": "계약서에 특별한 약정이 없으면 쌍방이 동시에 이행하는 것이 원칙"
                },
                {
                    "mistake": "동시이행 항변을 일방적 계약 거부로 오해",
                    "correction": "상대방 미이행 시 정당한 이행 거절권",
                    "explanation": "동시이행 항변권은 계약 위반이 아닌 정당한 권리 행사"
                },
                {
                    "mistake": "구두 약속으로 선이행 합의했다고 주장",
                    "correction": "선이행 약정은 반드시 서면으로 명시",
                    "explanation": "베트남 법원은 구두 선이행 약정을 인정하지 않는 경향"
                }
            ],
            "examples": [
                {
                    "ko": "본 계약은 동시이행 조건으로, 물품 인도와 대금 지급을 동시에 진행합니다",
                    "vi": "Hợp đồng này thực hiện theo điều kiện đồng thời, việc giao hàng và thanh toán tiền được tiến hành cùng lúc",
                    "situation": "formal"
                },
                {
                    "ko": "당신이 돈 안 주면 저도 물건 안 줘도 됩니다. 동시이행 원칙이에요",
                    "vi": "Nếu anh không trả tiền thì tôi cũng có quyền không giao hàng. Đó là nguyên tắc thực hiện đồng thời",
                    "situation": "informal"
                },
                {
                    "ko": "현장에서 인도증과 입금 확인을 동시에 교환합시다",
                    "vi": "Tại hiện trường, chúng ta hãy trao đổi biên bản giao nhận và xác nhận chuyển tiền đồng thời",
                    "situation": "onsite"
                }
            ],
            "relatedTerms": ["선이행", "이행거절", "쌍무계약", "대금지급"]
        },
        {
            "slug": "thuc-hien-truoc",
            "korean": "선이행",
            "vietnamese": "Thực hiện trước",
            "hanja": "先履行",
            "hanjaReading": "先(먼저 선) 履(밟을 리) 行(다닐 행)",
            "pronunciation": "선이행",
            "meaningKo": "계약 당사자 중 한쪽이 먼저 채무를 이행하는 것을 말합니다. 통역 시 선이행 의무자는 상대방의 이행을 기다리지 않고 먼저 이행해야 하며, 동시이행 항변권을 주장할 수 없다는 점을 명확히 해야 합니다. 베트남 상거래에서는 선이행 당사자가 높은 리스크를 부담하므로, 은행 보증이나 에스크로 등의 담보 수단을 함께 통역해야 합니다. 건설계약에서는 발주자가 선금(ứng trước)을 지급하는 것이 선이행의 대표적 사례이며, 계약서에 선이행 조건이 명시되지 않으면 동시이행이 원칙입니다.",
            "meaningVi": "Việc một bên thực hiện nghĩa vụ trước khi bên kia thực hiện. Bên thực hiện trước phải hoàn thành nghĩa vụ mà không chờ đợi bên kia, và không có quyền kháng biện đồng thời. Do rủi ro cao, thường cần có biện pháp đảm bảo như bảo lãnh ngân hàng hoặc escrow. Trong hợp đồng xây dựng, việc chủ đầu tư trả tiền ứng trước là ví dụ điển hình.",
            "context": "계약 체결, 대금 지급 조건 협상, 리스크 관리 시",
            "culturalNote": "한국은 계약서에 명시된 경우에만 선이행을 하는 반면, 베트남은 거래 관계 초기에는 선이행을 요구하는 경우가 많아 한국 기업들이 불리함을 느낍니다. 베트남 기업들은 신뢰가 쌓이기 전까지는 위험 부담이 적은 후불 방식을 선호하며, 통역사는 이러한 문화 차이를 조율하여 선금 지급 + 은행 보증 등의 절충안을 제시해야 합니다. 베트남에서는 선이행 당사자가 계약 위반 시 손해배상 청구가 어려울 수 있어, 통역 시 보증 조항을 강화하는 것이 중요합니다. 한국 기업은 선이행 리스크를 줄이기 위해 단계별 지급 방식을 선호하므로 이를 명확히 통역해야 합니다.",
            "commonMistakes": [
                {
                    "mistake": "선이행 의무 있는데 동시이행 주장",
                    "correction": "계약서에 선이행 명시 시 항변권 없음",
                    "explanation": "선이행 약정은 동시이행 원칙의 예외로, 먼저 이행해야 함"
                },
                {
                    "mistake": "선이행했으니 무조건 돈 받을 수 있다고 설명",
                    "correction": "선이행해도 하자 있으면 대금 감액 가능",
                    "explanation": "선이행은 순서의 문제일 뿐, 하자 담보 책임은 별개"
                },
                {
                    "mistake": "선이행 조건을 구두로만 합의",
                    "correction": "선이행 약정은 반드시 계약서에 명시",
                    "explanation": "베트남 법원은 구두 선이행 약정을 인정하지 않는 경우가 많음"
                }
            ],
            "examples": [
                {
                    "ko": "본 계약에서 갑은 을의 작업 완료 전에 계약금액의 30%를 선이행으로 지급합니다",
                    "vi": "Trong hợp đồng này, bên Giáp sẽ thanh toán trước 30% giá trị hợp đồng trước khi bên Ất hoàn thành công việc",
                    "situation": "formal"
                },
                {
                    "ko": "선금 주는 조건이니까 은행 보증서 꼭 받으세요",
                    "vi": "Vì là điều kiện ứng trước, anh nhớ nhận thư bảo lãnh ngân hàng nhé",
                    "situation": "informal"
                },
                {
                    "ko": "현장에서 선이행으로 자재비 먼저 드릴 테니 영수증 챙겨주세요",
                    "vi": "Tại hiện trường, chúng tôi sẽ trả trước tiền vật liệu, anh nhớ giữ hóa đơn",
                    "situation": "onsite"
                }
            ],
            "relatedTerms": ["동시이행", "선급금", "이행보증", "에스크로"]
        },
        {
            "slug": "hop-dong-vi-loi-ich-ben-thu-ba",
            "korean": "제3자를위한계약",
            "vietnamese": "Hợp đồng vì lợi ích bên thứ ba",
            "hanja": "第三者為約",
            "hanjaReading": "第(버금 제) 三(석 삼) 者(놈 자) 為(할 위) 約(맺을 약)",
            "pronunciation": "제삼자를위한계약",
            "meaningKo": "계약 당사자가 아닌 제3자에게 이익을 주기로 약정한 계약입니다. 통역 시 계약 당사자(낙약자, 요약자)와 수익자(제3자)의 관계를 명확히 구분하고, 제3자가 직접 이행을 청구할 수 있는지 여부를 설명해야 합니다. 베트남 민법에서도 'hợp đồng vì lợi ích người thứ ba'로 인정되지만, 제3자의 권리 취득 시점에 대한 해석이 한국과 다를 수 있어 주의가 필요합니다. 생명보험계약(보험금 수령자는 제3자)이 대표적 사례이며, 부동산 매매에서 매수인이 제3자에게 소유권 이전을 요청하는 경우도 해당합니다.",
            "meaningVi": "Hợp đồng mà các bên ký kết nhằm mang lại lợi ích cho người thứ ba không phải là bên hợp đồng. Người thứ ba (người thụ hưởng) có thể trực tiếp yêu cầu thực hiện nghĩa vụ. Ví dụ điển hình là hợp đồng bảo hiểm nhân thọ (người nhận tiền bảo hiểm là bên thứ ba) hoặc hợp đồng mua bán bất động sản mà bên mua yêu cầu chuyển quyền sở hữu cho người khác.",
            "context": "보험계약, 부동산 거래, 증여 계약 시",
            "culturalNote": "한국은 제3자를 위한 계약이 법률적으로 명확히 인정되지만, 베트남은 실무상 혼란이 있어 제3자의 권리 행사가 거부되는 경우가 있습니다. 베트남에서는 제3자가 계약서에 명시되지 않으면 권리 주장이 어려우므로, 통역 시 제3자의 신상정보와 권리 범위를 계약서에 명확히 기재하도록 조언해야 합니다. 특히 부동산 거래에서 매수인이 가족에게 소유권을 이전하려는 경우, 베트남은 증여세와 양도세 문제가 복잡하므로 세무 상담을 권장하는 것이 좋습니다. 통역 시 제3자의 동의 없이도 계약 변경이 가능한지 여부를 명확히 확인해야 합니다.",
            "commonMistakes": [
                {
                    "mistake": "제3자가 계약 당사자라고 설명",
                    "correction": "제3자는 당사자 아니고 수익자일 뿐",
                    "explanation": "제3자는 계약 체결에 참여하지 않았으나 이익을 받는 자"
                },
                {
                    "mistake": "제3자가 계약서에 서명 안 해도 된다고 설명",
                    "correction": "베트남은 제3자 정보를 계약서에 명시 필요",
                    "explanation": "베트남은 제3자 명시가 없으면 권리 인정이 어려울 수 있음"
                },
                {
                    "mistake": "제3자가 계약 변경을 요구할 수 있다고 설명",
                    "correction": "제3자는 수익만 받을 뿐, 계약 변경권은 없음",
                    "explanation": "계약 변경은 원칙적으로 당사자만 가능"
                }
            ],
            "examples": [
                {
                    "ko": "본 생명보험 계약의 보험금 수령인은 피보험자의 배우자로 지정합니다",
                    "vi": "Người thụ hưởng tiền bảo hiểm trong hợp đồng bảo hiểm nhân thọ này được chỉ định là người phối ngẫu của người được bảo hiểm",
                    "situation": "formal"
                },
                {
                    "ko": "제가 계약자인데 보험금은 제 아들이 받도록 하고 싶어요",
                    "vi": "Tôi là người ký hợp đồng nhưng muốn con trai tôi nhận tiền bảo hiểm",
                    "situation": "informal"
                },
                {
                    "ko": "현장에서 제3자에게 직접 지급하려면 위임장이 필요합니다",
                    "vi": "Để thanh toán trực tiếp cho bên thứ ba tại hiện trường, cần có giấy ủy quyền",
                    "situation": "onsite"
                }
            ],
            "relatedTerms": ["생명보험", "수익자", "낙약자", "요약자"]
        },
        {
            "slug": "thay-doi-tinh-huong",
            "korean": "사정변경",
            "vietnamese": "Thay đổi tình huống",
            "hanja": "事情變更",
            "hanjaReading": "事(일 사) 情(뜻 정) 變(변할 변) 更(고칠 경)",
            "pronunciation": "사정변경",
            "meaningKo": "계약 체결 당시 예상하지 못한 사정의 현저한 변경으로 계약 내용을 그대로 유지하는 것이 불공정한 경우, 계약 내용의 변경이나 해제를 인정하는 원칙입니다. 통역 시 단순한 경제적 손실은 사정변경에 해당하지 않으며, 전쟁, 천재지변, 법령 변경 등 예외적 사태만 인정된다는 점을 명확히 해야 합니다. 베트남 민법도 'nguyên tắc thay đổi hoàn cảnh(정황변경 원칙)'을 인정하지만, 법원이 이를 인정하는 비율은 매우 낮으므로 통역 시 과도한 기대를 갖지 않도록 주의시켜야 합니다. 통역사는 불가항력과 사정변경의 차이를 설명하고, 계약서에 사정변경 조항을 명시하도록 권장해야 합니다.",
            "meaningVi": "Nguyên tắc cho phép thay đổi hoặc chấm dứt hợp đồng khi có sự thay đổi trọng yếu về hoàn cảnh mà các bên không thể lường trước khi ký hợp đồng, khiến việc tiếp tục thực hiện hợp đồng trở nên bất công. Chỉ áp dụng trong các tình huống ngoại lệ như chiến tranh, thiên tai, thay đổi pháp luật. Tòa án Việt Nam rất ít khi chấp nhận lý do thay đổi tình huống.",
            "context": "장기 계약, 대규모 프로젝트, 경제 위기 시",
            "culturalNote": "한국은 사정변경 원칙을 비교적 폭넓게 인정하는 판례가 많지만, 베트남은 계약의 구속력을 더 중시하여 사정변경을 인정하는 사례가 드뭅니다. 베트남 법원은 '예측 가능성'을 엄격히 판단하여, 원자재 가격 변동이나 환율 변동 등은 예측 가능한 위험으로 보아 사정변경을 인정하지 않습니다. 통역 시 한국 기업에게는 베트남의 엄격한 기준을 사전에 알리고, 계약서에 가격 조정 조항(escalation clause)을 명시하도록 조언해야 합니다. 베트남에서는 정부 정책 변경이나 법령 개정도 기업이 감수해야 할 위험으로 보는 경향이 있어, 통역 시 이를 명확히 전달해야 합니다.",
            "commonMistakes": [
                {
                    "mistake": "물가 상승을 사정변경으로 주장",
                    "correction": "물가 상승은 예측 가능한 위험으로 사정변경 아님",
                    "explanation": "베트남 법원은 일반적 경제 변동은 사정변경으로 인정 안 함"
                },
                {
                    "mistake": "사정변경과 불가항력을 동일하게 설명",
                    "correction": "불가항력은 이행 불능, 사정변경은 이행 곤란",
                    "explanation": "불가항력은 객관적 불능, 사정변경은 주관적 곤란으로 법적 효과 다름"
                },
                {
                    "mistake": "사정변경 주장 시 자동으로 계약 변경된다고 설명",
                    "correction": "법원 판단 필요, 당사자 합의 또는 판결로만 변경",
                    "explanation": "사정변경은 당사자 일방이 임의로 주장할 수 없고 법적 절차 필요"
                }
            ],
            "examples": [
                {
                    "ko": "COVID-19로 인한 국경 봉쇄는 사정변경 사유로 계약 변경을 청구할 수 있습니다",
                    "vi": "Việc phong tỏa biên giới do COVID-19 có thể được coi là lý do thay đổi tình huống để yêu cầu thay đổi hợp đồng",
                    "situation": "formal"
                },
                {
                    "ko": "원자재 값이 두 배로 올랐는데 계약 그대로 하기 힘들어요 - 이건 사정변경으로 인정받기 어렵습니다",
                    "vi": "Giá nguyên liệu tăng gấp đôi, khó thực hiện hợp đồng như cũ - Trường hợp này khó được công nhận là thay đổi tình huống",
                    "situation": "informal"
                },
                {
                    "ko": "현장에서 법령 개정으로 공사 방법을 바꿔야 한다면 사정변경 협의 요청하세요",
                    "vi": "Nếu tại hiện trường phải thay đổi phương pháp thi công do sửa đổi pháp luật, hãy yêu cầu thương lượng thay đổi tình huống",
                    "situation": "onsite"
                }
            ],
            "relatedTerms": ["불가항력", "계약변경", "경제사정", "정황변경"]
        },
        {
            "slug": "bat-kha-khang",
            "korean": "불가항력",
            "vietnamese": "Bất khả kháng",
            "hanja": "不可抗力",
            "hanjaReading": "不(아닐 불) 可(옳을 가) 抗(막을 항) 力(힘 력)",
            "pronunciation": "불가항력",
            "meaningKo": "당사자가 예견할 수 없고 회피할 수 없으며 극복할 수 없는 객관적 사정으로 인해 계약 이행이 불가능한 경우를 말합니다. 통역 시 불가항력 사유 발생 시 채무 불이행 책임이 면제된다는 점을 명확히 해야 하며, 단순한 이행 곤란은 불가항력이 아님을 설명해야 합니다. 베트남 민법은 전쟁, 천재지변, 정부 명령 등을 불가항력으로 규정하며, 당사자는 불가항력 발생 후 즉시 상대방에게 통지해야 합니다. 통역 시 불가항력 조항의 범위, 통지 의무, 입증 책임을 명확히 전달하고, 가능하면 국제상공회의소(ICC) 불가항력 조항을 준용하도록 권장해야 합니다.",
            "meaningVi": "Sự kiện khách quan mà các bên không thể lường trước, không thể tránh được và không thể khắc phục, dẫn đến không thể thực hiện hợp đồng. Khi xảy ra bất khả kháng, bên vi phạm được miễn trách nhiệm. Luật Việt Nam quy định chiến tranh, thiên tai, lệnh của cơ quan nhà nước là bất khả kháng. Bên gặp bất khả kháng phải thông báo ngay cho bên kia.",
            "context": "계약 이행 불능, 천재지변, 전쟁, 정부 명령 시",
            "culturalNote": "한국은 불가항력 인정 범위가 좁고 엄격하지만, 베트남은 비교적 폭넓게 인정하는 경향이 있습니다. 특히 베트남은 정부의 행정 명령이나 허가 지연도 불가항력으로 주장하는 경우가 많아, 한국 기업이 예상치 못한 계약 지연을 겪을 수 있습니다. 통역 시 불가항력 조항에 '정부 허가 지연'을 포함할지 여부를 명확히 협상하고, 지연 시 책임 소재를 정해두는 것이 중요합니다. 베트남에서는 불가항력 입증을 위해 관할 기관의 확인서(giấy xác nhận)가 필요하므로, 통역 시 이 절차를 설명하고 신속히 확인서를 받도록 조언해야 합니다. COVID-19 팬데믹 기간 베트남 정부는 불가항력 확인서를 적극 발급했으나, 한국은 인정 사례가 적었던 차이가 있습니다.",
            "commonMistakes": [
                {
                    "mistake": "경제적 어려움을 불가항력으로 주장",
                    "correction": "경제 위기는 예측 가능한 위험, 불가항력 아님",
                    "explanation": "불가항력은 객관적 불능이며, 주관적 곤란은 해당 안 됨"
                },
                {
                    "mistake": "불가항력 발생 후 통지 안 해도 된다고 설명",
                    "correction": "즉시 서면 통지 필수, 통지 안 하면 면책 안 됨",
                    "explanation": "베트남 민법은 신속한 통지를 불가항력 면책의 요건으로 규정"
                },
                {
                    "mistake": "불가항력이면 계약이 자동 해제된다고 설명",
                    "correction": "불가항력은 일시적 면책, 계약 해제는 별도 절차",
                    "explanation": "불가항력이 지속되어 계약 목적 달성 불가 시에만 해제 가능"
                }
            ],
            "examples": [
                {
                    "ko": "태풍으로 인한 공사 중단은 불가항력 사유로 공기 연장을 청구합니다",
                    "vi": "Việc tạm dừng thi công do bão là sự kiện bất khả kháng, chúng tôi yêu cầu gia hạn tiến độ",
                    "situation": "formal"
                },
                {
                    "ko": "불가항력 발생하면 24시간 내에 서면으로 통지해야 면책 받을 수 있어요",
                    "vi": "Khi xảy ra bất khả kháng, phải thông báo bằng văn bản trong 24 giờ mới được miễn trách nhiệm",
                    "situation": "informal"
                },
                {
                    "ko": "현장에서 정부 명령으로 작업 중단되면 불가항력 확인서 빨리 받으세요",
                    "vi": "Nếu công việc tại hiện trường bị đình chỉ do lệnh của chính phủ, hãy nhanh chóng xin giấy xác nhận bất khả kháng",
                    "situation": "onsite"
                }
            ],
            "relatedTerms": ["사정변경", "면책조항", "천재지변", "계약해제"]
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
