#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""건설분쟁법 용어 추가 스크립트 (v6-f)"""

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
            "slug": "khuyet-tat-xay-dung",
            "korean": "건설하자",
            "vietnamese": "Khuyết tật xây dựng",
            "hanja": "建設瑕疵",
            "hanjaReading": "建(세울 건) + 設(베풀 설) + 瑕(옥의 티 하) + 疵(허물 자)",
            "pronunciation": "끄웨뜨 땃 싸이 중",
            "meaningKo": "건설공사 완료 후 발견된 시공상의 결함이나 하자를 의미합니다. 통역 시 '하자보수책임기간'과 '하자담보책임'을 명확히 구분해야 하며, 베트남에서는 공사 종류에 따라 하자책임기간이 다르므로 주의가 필요합니다. 베트남 건설법에서는 일반 공사는 2년, 구조물은 5년의 하자책임기간을 규정하고 있어 한국의 기준과 차이가 있습니다. 하자의 범위와 보수책임 소재를 명확히 통역하는 것이 분쟁 예방에 중요합니다.",
            "meaningVi": "Khuyết tật xây dựng là những lỗi hoặc sai sót trong thi công được phát hiện sau khi hoàn thành công trình. Theo Luật Xây dựng Việt Nam, thời gian bảo hành công trình thông thường là 2 năm, công trình kết cấu là 5 năm. Việc xác định rõ phạm vi khuyết tật và trách nhiệm sửa chữa rất quan trọng để tránh tranh chấp.",
            "context": "건설 분쟁, 하자보수 협상, 건설 계약서",
            "culturalNote": "한국에서는 하자담보책임기간이 건축물 종류에 따라 1-10년으로 세분화되어 있지만, 베트남은 2년(일반)/5년(구조물)로 단순합니다. 통역 시 양국의 법적 기준 차이를 명확히 설명해야 하며, 특히 국제 건설 계약에서는 어느 국가의 기준을 따를지 사전 합의가 필수입니다. 베트남에서는 하자책임 입증 책임이 발주자에게 있는 경우가 많아 이 점도 주의해야 합니다.",
            "commonMistakes": [
                {
                    "mistake": "Lỗi xây dựng (단순 시공 오류)",
                    "correction": "Khuyết tật xây dựng (법적 하자)",
                    "explanation": "'Lỗi'는 일반적인 실수를 의미하지만, 'Khuyết tật'은 법적 책임을 수반하는 하자를 의미합니다."
                },
                {
                    "mistake": "하자보수와 하자담보를 구분 없이 'Sửa chữa khuyết tật'으로만 통역",
                    "correction": "하자보수는 'Sửa chữa khuyết tật', 하자담보는 'Bảo đảm khuyết tật'",
                    "explanation": "하자보수는 실제 수리 행위이고, 하자담보는 법적 책임 범위입니다."
                },
                {
                    "mistake": "Thời gian bảo hành 2 năm (모든 건축물에 동일하게 적용)",
                    "correction": "2년(일반 공사) 또는 5년(구조물)로 구분",
                    "explanation": "베트남 건설법은 공사 종류에 따라 보증기간을 구분합니다."
                }
            ],
            "examples": [
                {
                    "ko": "준공 후 6개월 이내에 발견된 건설하자는 시공사가 무상으로 보수해야 합니다.",
                    "vi": "Các khuyết tật xây dựng được phát hiện trong vòng 6 tháng sau khi nghiệm thu phải được nhà thầu sửa chữa miễn phí.",
                    "situation": "formal"
                },
                {
                    "ko": "외벽 균열은 구조적 하자로 판단되어 5년 보증 대상입니다.",
                    "vi": "Vết nứt tường ngoài được xác định là khuyết tật kết cấu, thuộc đối tượng bảo hành 5 năm.",
                    "situation": "onsite"
                },
                {
                    "ko": "하자보수 요청서에 사진과 상세 설명을 첨부하여 제출해 주시기 바랍니다.",
                    "vi": "Vui lòng gửi đơn yêu cầu sửa chữa khuyết tật kèm theo ảnh và mô tả chi tiết.",
                    "situation": "formal"
                }
            ],
            "relatedTerms": ["công-trình-xây-dựng", "hợp-đồng-xây-dựng", "nghiệm-thu-công-trình", "bảo-hành-công-trình"]
        },
        {
            "slug": "tien-cong-xay-dung",
            "korean": "공사대금",
            "vietnamese": "Tiền công xây dựng",
            "hanja": "工事代金",
            "hanjaReading": "工(장인 공) + 事(일 사) + 代(대신할 대) + 金(쇠 금)",
            "pronunciation": "띠엔 꽁 싸이 중",
            "meaningKo": "건설공사 수행에 대한 대가로 발주자가 시공사에게 지급하는 금액을 의미합니다. 통역 시 '선급금', '기성금', '잔금'의 구분이 중요하며, 베트남에서는 선급금 비율이 계약금액의 15-30%로 제한되는 경우가 많습니다. 공사대금 지급 조건과 시기를 명확히 통역해야 분쟁을 예방할 수 있으며, 특히 환율 변동에 따른 조정 조항은 세심한 주의가 필요합니다. 지연이자율도 양국이 다르므로 계약서에 명시해야 합니다.",
            "meaningVi": "Tiền công xây dựng là số tiền chủ đầu tư trả cho nhà thầu để thực hiện công trình. Thường được chia thành tiền tạm ứng (15-30% giá trị hợp đồng), tiền thanh toán theo khối lượng hoàn thành, và tiền thanh toán cuối cùng. Điều kiện và thời gian thanh toán phải được quy định rõ ràng trong hợp đồng để tránh tranh chấp.",
            "context": "건설 계약, 공사비 정산, 건설 클레임",
            "culturalNote": "한국에서는 공사대금을 계약금-중도금-잔금으로 구분하는 것이 일반적이지만, 베트남에서는 선급금(Tạm ứng)-기성금(Thanh toán theo khối lượng)-준공금(Thanh toán nghiệm thu)으로 표현합니다. 베트nam에서는 선급금 비율이 법적으로 제한되는 경우가 많아(보통 15-30%), 한국식 계약금 개념과 차이가 있습니다. 또한 베트남에서는 VAT(10%)를 별도로 표기하는 것이 일반적이므로 통역 시 세금 포함/불포함 여부를 명확히 해야 합니다.",
            "commonMistakes": [
                {
                    "mistake": "Giá xây dựng (건설 가격)",
                    "correction": "Tiền công xây dựng (공사대금)",
                    "explanation": "'Giá'는 가격을 의미하지만, 'Tiền công'은 실제 지급되는 대금을 의미합니다."
                },
                {
                    "mistake": "계약금을 'Tiền đặt cọc'으로 통역",
                    "correction": "계약금은 'Tiền tạm ứng' 또는 'Tiền ứng trước'",
                    "explanation": "'Đặt cọc'은 부동산 계약의 계약금이고, 건설에서는 'Tạm ứng'(선급금)을 사용합니다."
                },
                {
                    "mistake": "지급 금액에 VAT 포함 여부를 명시하지 않음",
                    "correction": "'Chưa bao gồm VAT'(VAT 불포함) 또는 'Đã bao gồm VAT'(VAT 포함) 명시",
                    "explanation": "베트남에서는 VAT 10%가 별도이므로 반드시 구분해야 합니다."
                }
            ],
            "examples": [
                {
                    "ko": "총 공사대금 100억 원 중 선급금으로 20억 원을 계약 후 7일 이내에 지급합니다.",
                    "vi": "Trong tổng tiền công xây dựng 10 tỷ won, tiền tạm ứng 2 tỷ won sẽ được thanh toán trong vòng 7 ngày sau khi ký hợp đồng.",
                    "situation": "formal"
                },
                {
                    "ko": "이번 달 기성금 청구액은 VAT 포함 5억 원입니다.",
                    "vi": "Số tiền thanh toán theo khối lượng hoàn thành tháng này là 500 triệu won đã bao gồm VAT.",
                    "situation": "onsite"
                },
                {
                    "ko": "공사대금 미지급으로 인한 지연이자는 연 12%를 적용합니다.",
                    "vi": "Lãi suất chậm trả do chưa thanh toán tiền công xây dựng được áp dụng 12%/năm.",
                    "situation": "formal"
                }
            ],
            "relatedTerms": ["hợp-đồng-xây-dựng", "khối-lượng-thi-công", "thanh-toán-xây-dựng", "nghiệm-thu-công-trình"]
        },
        {
            "slug": "thay-đổi-thiet-ke",
            "korean": "설계변경",
            "vietnamese": "Thay đổi thiết kế",
            "hanja": "設計變更",
            "hanjaReading": "設(베풀 설) + 計(셀 계) + 變(변할 변) + 更(다시 경)",
            "pronunciation": "타이 도이 티엣 께",
            "meaningKo": "공사 진행 중 원래 설계도면이나 시방서를 수정하는 것을 의미합니다. 통역 시 '발주자 요청 변경'과 '불가피한 변경'을 구분해야 하며, 설계변경으로 인한 공사비 증감과 공기 연장을 명확히 협의해야 합니다. 베트남에서는 설계변경 승인 절차가 까다로우므로 사전 협의가 중요하며, 변경 사유와 범위를 문서화하는 것이 분쟁 예방에 필수적입니다. 특히 구조 변경은 별도의 안전성 검토가 필요합니다.",
            "meaningVi": "Thay đổi thiết kế là việc sửa đổi bản vẽ thiết kế hoặc thuyết minh kỹ thuật ban đầu trong quá trình thi công. Cần phân biệt rõ thay đổi theo yêu cầu của chủ đầu tư và thay đổi bất khả kháng. Mọi thay đổi thiết kế phải được phê duyệt bằng văn bản và thỏa thuận rõ về điều chỉnh chi phí và tiến độ thi công.",
            "context": "건설 현장, 설계 협의, 계약 변경",
            "culturalNote": "한국에서는 설계변경이 비교적 유연하게 이루어지지만, 베트남에서는 변경 승인 절차가 매우 엄격합니다. 특히 정부 프로젝트의 경우 상급 기관의 승인이 필요할 수 있으며, 이로 인한 지연이 발생할 수 있습니다. 베트남에서는 설계변경으로 인한 공사비 증가가 원 계약금액의 20%를 초과하면 별도의 승인 절차가 필요한 경우가 많습니다. 통역 시 변경 사유를 명확히 설명하고, 비용과 일정에 미치는 영향을 구체적으로 전달해야 합니다.",
            "commonMistakes": [
                {
                    "mistake": "Sửa đổi thiết kế (단순 수정)",
                    "correction": "Thay đổi thiết kế (공식 설계변경)",
                    "explanation": "'Sửa đổi'는 일반적인 수정이지만, 'Thay đổi'는 공식적인 변경 절차를 의미합니다."
                },
                {
                    "mistake": "설계변경과 시공변경을 구분 없이 통역",
                    "correction": "설계변경은 'Thay đổi thiết kế', 시공변경은 'Thay đổi thi công'",
                    "explanation": "설계는 도면/시방서 변경이고, 시공은 현장 작업 방법 변경입니다."
                },
                {
                    "mistake": "변경 승인 절차를 'Phê duyệt đơn giản'(간단한 승인)으로 표현",
                    "correction": "'Thủ tục phê duyệt thay đổi thiết kế'(설계변경 승인 절차)로 정확히 표현",
                    "explanation": "베트남에서는 설계변경 승인이 복잡한 절차이므로 과소평가해서는 안 됩니다."
                }
            ],
            "examples": [
                {
                    "ko": "발주자 요청으로 인한 설계변경은 공사비 증액과 공기 연장 사유가 됩니다.",
                    "vi": "Thay đổi thiết kế theo yêu cầu của chủ đầu tư là căn cứ để điều chỉnh tăng chi phí và kéo dài tiến độ thi công.",
                    "situation": "formal"
                },
                {
                    "ko": "이 부분은 현장 여건상 설계변경이 불가피합니다.",
                    "vi": "Phần này bắt buộc phải thay đổi thiết kế do điều kiện thực tế hiện trường.",
                    "situation": "onsite"
                },
                {
                    "ko": "설계변경 승인서를 받기 전에는 해당 부분의 시공을 중단해 주십시오.",
                    "vi": "Vui lòng tạm dừng thi công phần này cho đến khi nhận được văn bản phê duyệt thay đổi thiết kế.",
                    "situation": "formal"
                }
            ],
            "relatedTerms": ["bản-vẽ-thiết-kế", "hợp-đồng-xây-dựng", "khối-lượng-thi-công", "tiến-độ-thi-công"]
        },
        {
            "slug": "cham-tiến-độ-thi-công",
            "korean": "공기지연",
            "vietnamese": "Chậm tiến độ thi công",
            "hanja": "工期遲延",
            "hanjaReading": "工(장인 공) + 期(기약할 기) + 遲(늦을 지) + 延(늘일 연)",
            "pronunciation": "참 띠엔 도 티 꽁",
            "meaningKo": "건설공사가 계약서에 명시된 완공 기한을 넘기는 것을 의미합니다. 통역 시 '시공사 귀책 지연'과 '발주자 귀책 지연', '불가항력 지연'을 명확히 구분해야 하며, 지연에 따른 지체상금 계산과 공기 연장 협의가 중요합니다. 베트남에서는 지체상금이 일반적으로 일 단위 계약금액의 0.05-0.1%이며, 최대 10-15%로 제한됩니다. 공기 연장 승인 절차와 증빙 서류를 명확히 통역해야 합니다.",
            "meaningVi": "Chậm tiến độ thi công là việc công trình không hoàn thành đúng thời hạn quy định trong hợp đồng. Cần phân biệt rõ chậm tiến độ do lỗi của nhà thầu, do lỗi của chủ đầu tư, hay do sự kiện bất khả kháng. Phạt chậm tiến độ thường được tính theo ngày chậm, khoảng 0.05-0.1% giá trị hợp đồng, tối đa 10-15%.",
            "context": "건설 현장, 공정 관리, 클레임 협상",
            "culturalNote": "한국에서는 공기 지연에 대한 지체상금률이 계약마다 다양하지만, 베트남에서는 일반적으로 일일 0.05-0.1%, 최대 총액 10-15%로 법적 제한이 있습니다. 베트남에서는 천재지변, 전쟁, 전염병 등이 불가항력 사유로 인정되며, COVID-19 기간 동안 많은 공사가 공기 연장을 받았습니다. 통역 시 지연 사유를 객관적으로 설명하고, 증빙 서류(사진, 일지, 공문 등)의 중요성을 강조해야 합니다. 베트남에서는 구두 합의보다 문서화된 증거가 분쟁 해결에 결정적입니다.",
            "commonMistakes": [
                {
                    "mistake": "Trễ hạn (단순 기한 초과)",
                    "correction": "Chậm tiến độ thi công (공기 지연)",
                    "explanation": "'Trễ hạn'은 일반적인 지연이고, 'Chậm tiến độ'는 공사 일정 지연을 의미합니다."
                },
                {
                    "mistake": "지체상금을 'Tiền phạt'(벌금)으로만 통역",
                    "correction": "'Tiền phạt chậm tiến độ' 또는 'Phạt vi phạm hợp đồng'",
                    "explanation": "단순 '벌금'이 아니라 계약 위반에 따른 손해배상금임을 명확히 해야 합니다."
                },
                {
                    "mistake": "불가항력을 'Không thể làm được'(할 수 없음)으로 표현",
                    "correction": "'Sự kiện bất khả kháng'(불가항력 사건)",
                    "explanation": "불가항력은 법적 용어이므로 정확한 표현을 사용해야 합니다."
                }
            ],
            "examples": [
                {
                    "ko": "우기로 인한 공사 중단은 불가항력 사유로 인정되어 공기 연장 대상입니다.",
                    "vi": "Việc tạm dừng thi công do mưa mùa được công nhận là sự kiện bất khả kháng, đủ điều kiện xin gia hạn tiến độ.",
                    "situation": "formal"
                },
                {
                    "ko": "자재 납품 지연으로 인해 준공이 15일 늦어질 것으로 예상됩니다.",
                    "vi": "Do chậm giao vật liệu, dự kiến việc nghiệm thu sẽ chậm 15 ngày.",
                    "situation": "onsite"
                },
                {
                    "ko": "공기 지연에 따른 지체상금은 일 500만 원씩 총 1억 원입니다.",
                    "vi": "Tiền phạt chậm tiến độ là 5 triệu won/ngày, tổng cộng 100 triệu won.",
                    "situation": "formal"
                }
            ],
            "relatedTerms": ["tiến-độ-thi-công", "hợp-đồng-xây-dựng", "bất-khả-kháng", "tiền-phạt-hợp-đồng"]
        },
        {
            "slug": "thau-phu",
            "korean": "하도급",
            "vietnamese": "Thầu phụ",
            "hanja": "下都給",
            "hanjaReading": "下(아래 하) + 都(도읍 도) + 給(줄 급)",
            "pronunciation": "타우 푸",
            "meaningKo": "원도급자가 공사의 일부를 다른 업체에 재위탁하는 것을 의미합니다. 통역 시 '적법 하도급'과 '불법 하도급'(일괄하도급)을 구분해야 하며, 베트남에서는 하도급 비율과 하도급자 자격에 대한 법적 제한이 있습니다. 하도급 계약서 작성과 대금 지급 구조를 명확히 통역해야 분쟁을 예방할 수 있으며, 특히 안전관리 책임 소재를 분명히 해야 합니다. 베트남에서는 하도급 승인 절차가 필요한 경우가 많습니다.",
            "meaningVi": "Thầu phụ là việc nhà thầu chính giao một phần công việc cho nhà thầu khác thực hiện. Theo pháp luật Việt Nam, việc thầu phụ phải được chủ đầu tư chấp thuận và nhà thầu phụ phải đáp ứng các điều kiện năng lực theo quy định. Trách nhiệm về chất lượng và an toàn lao động vẫn thuộc về nhà thầu chính.",
            "context": "건설 계약, 공사 관리, 안전 관리",
            "culturalNote": "한국에서는 '하도급'이라는 용어가 부정적인 이미지를 가질 수 있지만, 베트남에서는 'Thầu phụ'가 일반적인 건설 관행으로 받아들여집니다. 베트남에서는 하도급 비율이 법적으로 제한되는 경우가 있으며(예: 공공 공사는 전체 계약금액의 50% 이하), 하도급자의 자격(건설업 등록증, 기술인력 등)도 엄격히 관리됩니다. 일괄하도급(toàn bộ công việc giao thầu phụ)은 불법이므로 통역 시 주의해야 합니다. 하도급 대금 직불제도 베트남에 도입되고 있어, 이에 대한 이해가 필요합니다.",
            "commonMistakes": [
                {
                    "mistake": "Thầu phụ와 Nhà thầu phụ를 혼용",
                    "correction": "Thầu phụ는 '하도급(행위)', Nhà thầu phụ는 '하도급업체'",
                    "explanation": "행위와 주체를 명확히 구분해야 합니다."
                },
                {
                    "mistake": "일괄하도급을 단순히 'Giao toàn bộ cho thầu phụ'로만 표현",
                    "correction": "'Giao thầu phụ toàn bộ (bất hợp pháp)'로 불법임을 명시",
                    "explanation": "일괄하도급은 법적으로 금지되어 있음을 명확히 해야 합니다."
                },
                {
                    "mistake": "하도급 승인을 'Thông báo thầu phụ'(하도급 통보)로만 표현",
                    "correction": "'Xin phê duyệt thầu phụ'(하도급 승인 요청)",
                    "explanation": "베트남에서는 통보가 아니라 승인이 필요한 경우가 많습니다."
                }
            ],
            "examples": [
                {
                    "ko": "전기공사는 자격을 갖춘 전문업체에 하도급 발주할 예정입니다.",
                    "vi": "Công việc điện sẽ được giao thầu phụ cho đơn vị chuyên môn có đủ năng lực.",
                    "situation": "formal"
                },
                {
                    "ko": "하도급업체 선정 시 안전관리 능력을 우선적으로 검토해야 합니다.",
                    "vi": "Khi lựa chọn nhà thầu phụ, cần ưu tiên xem xét năng lực quản lý an toàn lao động.",
                    "situation": "onsite"
                },
                {
                    "ko": "하도급 계약서에는 안전사고 발생 시 책임 소재를 명확히 기재해야 합니다.",
                    "vi": "Hợp đồng thầu phụ phải ghi rõ trách nhiệm trong trường hợp xảy ra tai nạn lao động.",
                    "situation": "formal"
                }
            ],
            "relatedTerms": ["nhà-thầu-chính", "hợp-đồng-xây-dựng", "quản-lý-thi-công", "an-toàn-lao-động"]
        },
        {
            "slug": "tai-nạn-lao-động-xây-dựng",
            "korean": "안전사고",
            "vietnamese": "Tai nạn lao động xây dựng",
            "hanja": "安全事故",
            "hanjaReading": "安(편안할 안) + 全(온전할 전) + 事(일 사) + 故(연고 고)",
            "pronunciation": "따이 난 라오 동 싸이 중",
            "meaningKo": "건설 현장에서 발생하는 근로자의 부상, 사망 등의 산업재해를 의미합니다. 통역 시 '경미한 사고'와 '중대재해'를 구분해야 하며, 사고 발생 시 즉시 보고 의무와 조사 절차를 명확히 전달해야 합니다. 베트남에서는 안전사고 발생 시 지방 노동청에 24시간 이내 보고해야 하며, 중대재해는 공사 중단 명령이 내려질 수 있습니다. 안전관리자 배치 기준과 안전교육 의무를 명확히 통역하는 것이 중요합니다.",
            "meaningVi": "Tai nạn lao động xây dựng là các sự cố gây thương tích hoặc tử vong cho người lao động tại công trường. Theo quy định, mọi tai nạn phải được báo cáo cho Sở Lao động - Thương binh và Xã hội trong vòng 24 giờ. Tai nạn nghiêm trọng có thể dẫn đến lệnh đình chỉ thi công. Nhà thầu phải bố trí nhân viên an toàn lao động và tổ chức huấn luyện định kỳ.",
            "context": "건설 현장, 안전 관리, 사고 조사",
            "culturalNote": "한국에서는 중대재해처벌법으로 안전관리가 매우 엄격해졌지만, 베트남도 최근 안전 규제를 강화하고 있습니다. 베트남에서는 안전사고 발생 시 노동청 보고뿐만 아니라 건설청, 경찰에도 보고해야 하는 경우가 있으며, 사고 조사 기간 동안 해당 구역의 공사가 중단될 수 있습니다. 안전모, 안전화, 안전벨트 등 기본 보호구 착용이 의무이며, 미착용 시 현장 출입이 금지됩니다. 통역 시 안전 규정을 강조하고, 사고 예방의 중요성을 명확히 전달해야 합니다.",
            "commonMistakes": [
                {
                    "mistake": "Tai nạn (일반 사고)",
                    "correction": "Tai nạn lao động (산업재해)",
                    "explanation": "건설 현장의 사고는 '산업재해'로 법적 의미가 다릅니다."
                },
                {
                    "mistake": "사고 보고를 'Báo cáo sự cố'(일반 사고 보고)로만 표현",
                    "correction": "'Báo cáo tai nạn lao động theo quy định'(법정 산재 보고)",
                    "explanation": "법적 보고 의무임을 명확히 해야 합니다."
                },
                {
                    "mistake": "중대재해를 'Tai nạn lớn'(큰 사고)으로 표현",
                    "correction": "'Tai nạn lao động nghiêm trọng'(중대재해)",
                    "explanation": "법적 정의가 있는 용어이므로 정확히 사용해야 합니다."
                }
            ],
            "examples": [
                {
                    "ko": "추락 사고 예방을 위해 모든 근로자는 안전벨트를 착용해야 합니다.",
                    "vi": "Để phòng ngừa tai nạn rơi từ trên cao, tất cả người lao động phải đeo dây an toàn.",
                    "situation": "onsite"
                },
                {
                    "ko": "오늘 오후 안전사고가 발생하여 즉시 노동청에 보고하였습니다.",
                    "vi": "Chiều nay đã xảy ra tai nạn lao động, chúng tôi đã báo cáo ngay cho Sở Lao động.",
                    "situation": "formal"
                },
                {
                    "ko": "매주 월요일 아침 전체 근로자 대상 안전교육을 실시합니다.",
                    "vi": "Mỗi sáng thứ Hai tổ chức huấn luyện an toàn lao động cho toàn bộ công nhân.",
                    "situation": "onsite"
                }
            ],
            "relatedTerms": ["an-toàn-lao-động", "bảo-hộ-lao-động", "quản-lý-thi-công", "công-trường-xây-dựng"]
        },
        {
            "slug": "bảo-lãnh-thực-hiện-hợp-đồng",
            "korean": "건설보증",
            "vietnamese": "Bảo lãnh thực hiện hợp đồng",
            "hanja": "建設保證",
            "hanjaReading": "建(세울 건) + 設(베풀 설) + 保(지킬 보) + 證(증거 증)",
            "pronunciation": "바오 란 툭 히엔 혼 동",
            "meaningKo": "시공사가 계약 조건대로 공사를 완수할 것을 보증하기 위해 금융기관이 발행하는 보증서를 의미합니다. 통역 시 '이행보증', '선급금보증', '하자보수보증', '입찰보증'을 구분해야 하며, 각각의 발급 시기와 보증 비율을 명확히 전달해야 합니다. 베트남에서는 보증 비율이 계약금액의 3-10%이며, 보증서 발급 은행의 신용도도 중요한 계약 조건입니다. 보증 기간과 청구 조건을 정확히 통역해야 합니다.",
            "meaningVi": "Bảo lãnh thực hiện hợp đồng là thư bảo lãnh do ngân hàng phát hành để đảm bảo nhà thầu thực hiện đầy đủ các cam kết trong hợp đồng. Bao gồm bảo lãnh dự thầu, bảo lãnh thực hiện hợp đồng, bảo lãnh tạm ứng, và bảo lãnh bảo hành. Tỷ lệ bảo lãnh thường từ 3-10% giá trị hợp đồng, tùy loại và quy định cụ thể.",
            "context": "건설 계약, 금융, 입찰",
            "culturalNote": "한국에서는 건설공제조합이 보증의 주요 발급 기관이지만, 베트남에서는 상업은행이 주로 발급합니다. 베트남에서는 보증서 발급 은행의 신용등급(국제 신용평가 기관 기준)이 계약 조건에 명시되는 경우가 많으며, 외국계 은행 보증서를 요구하는 경우도 있습니다. 보증 수수료는 연 1-3%이며, 이는 공사비에 영향을 미칩니다. 통역 시 보증서의 종류와 유효기간, 청구 조건(조건부/무조건부)을 명확히 구분해야 하며, 베트남어로 '조건부 보증'은 'Bảo lãnh có điều kiện', '무조건부 보증'은 'Bảo lãnh vô điều kiện'입니다.",
            "commonMistakes": [
                {
                    "mistake": "Bảo hiểm (보험)",
                    "correction": "Bảo lãnh (보증)",
                    "explanation": "'Bảo hiểm'은 손해보험이고, 'Bảo lãnh'은 이행보증입니다."
                },
                {
                    "mistake": "모든 보증을 'Bảo lãnh hợp đồng'으로만 통역",
                    "correction": "종류별로 구분: 입찰보증(Bảo lãnh dự thầu), 이행보증(Bảo lãnh thực hiện), 선급금보증(Bảo lãnh tạm ứng), 하자보증(Bảo lãnh bảo hành)",
                    "explanation": "각 보증의 목적과 시기가 다르므로 정확히 구분해야 합니다."
                },
                {
                    "mistake": "보증 청구를 'Yêu cầu bảo lãnh'로만 표현",
                    "correction": "'Yêu cầu thanh toán theo bảo lãnh'(보증금 청구)",
                    "explanation": "보증서 발급 요청과 보증금 청구를 구분해야 합니다."
                }
            ],
            "examples": [
                {
                    "ko": "계약 체결 전에 계약금액의 10%에 해당하는 이행보증서를 제출해야 합니다.",
                    "vi": "Trước khi ký hợp đồng, phải nộp thư bảo lãnh thực hiện hợp đồng trị giá 10% giá trị hợp đồng.",
                    "situation": "formal"
                },
                {
                    "ko": "선급금 지급과 동시에 선급금보증서를 발급받았습니다.",
                    "vi": "Đồng thời với việc thanh toán tạm ứng, chúng tôi đã nhận được thư bảo lãnh tạm ứng.",
                    "situation": "formal"
                },
                {
                    "ko": "하자보수보증 기간은 준공일로부터 2년입니다.",
                    "vi": "Thời hạn bảo lãnh bảo hành là 2 năm kể từ ngày nghiệm thu.",
                    "situation": "onsite"
                }
            ],
            "relatedTerms": ["hợp-đồng-xây-dựng", "dự-thầu-xây-dựng", "ngân-hàng", "tạm-ứng"]
        },
        {
            "slug": "khiếu-nại-hợp-đồng",
            "korean": "건설클레임",
            "vietnamese": "Khiếu nại hợp đồng",
            "hanja": "建設Claim",
            "hanjaReading": "建(세울 건) + 設(베풀 설) + Claim(청구)",
            "pronunciation": "키에우 나이 혼 동",
            "meaningKo": "계약 조건 변경이나 예상치 못한 상황으로 인한 추가 비용이나 공기 연장을 요구하는 것을 의미합니다. 통역 시 클레임 사유를 명확히 분류하고(설계변경, 공기지연, 추가공사 등), 증빙 서류와 계산 근거를 정확히 전달해야 합니다. 베트남에서는 클레임 제기 기한이 계약서에 명시되어 있으며(보통 사유 발생 후 28일 이내), 이를 놓치면 권리를 상실할 수 있습니다. 클레임 협상 과정에서 감정적 대응을 피하고 객관적 근거를 제시하는 것이 중요합니다.",
            "meaningVi": "Khiếu nại hợp đồng là yêu cầu điều chỉnh chi phí hoặc thời gian thi công do thay đổi điều kiện hợp đồng hoặc các sự kiện không lường trước. Phải nộp khiếu nại trong thời hạn quy định (thường là 28 ngày kể từ khi phát sinh sự kiện) kèm theo đầy đủ chứng cứ và cơ sở tính toán. Quá trình đàm phán cần dựa trên cơ sở khách quan, tránh phản ứng cảm tính.",
            "context": "건설 분쟁, 계약 협상, 공사비 정산",
            "culturalNote": "한국에서는 '클레임'이라는 용어가 일반적이지만, 베트남에서는 'Khiếu nại'(이의 제기) 또는 'Yêu cầu điều chỉnh hợp đồng'(계약 조정 요구)으로 표현합니다. 베트남 건설 문화에서는 클레임이 적대적 행위로 인식될 수 있으므로, 통역 시 '협력적 문제 해결'의 맥락으로 전달하는 것이 효과적입니다. 베트남에서는 클레임 심사 위원회(Board of Claims)를 운영하는 대형 프로젝트도 있으며, 이 경우 절차가 매우 공식적입니다. 통역 시 클레임 금액뿐만 아니라 업무 관계 유지의 중요성도 함께 전달해야 합니다.",
            "commonMistakes": [
                {
                    "mistake": "Khiếu nại (단순 불만)",
                    "correction": "Khiếu nại hợp đồng (계약상 클레임)",
                    "explanation": "일반적인 불만과 계약상 권리 주장을 구분해야 합니다."
                },
                {
                    "mistake": "클레임을 'Yêu cầu bồi thường'(배상 요구)으로만 통역",
                    "correction": "'Yêu cầu điều chỉnh hợp đồng'(계약 조정 요구)로 협력적 표현 사용",
                    "explanation": "배상 요구는 적대적으로 들릴 수 있으므로 협력적 표현이 효과적입니다."
                },
                {
                    "mistake": "클레임 기한을 언급하지 않음",
                    "correction": "'Trong thời hạn 28 ngày kể từ khi phát sinh'(발생 후 28일 이내) 명시",
                    "explanation": "기한을 놓치면 권리를 상실하므로 반드시 언급해야 합니다."
                }
            ],
            "examples": [
                {
                    "ko": "설계변경으로 인한 추가 공사비 2억 원에 대해 클레임을 제기합니다.",
                    "vi": "Chúng tôi nộp khiếu nại về chi phí tăng thêm 200 triệu won do thay đổi thiết kế.",
                    "situation": "formal"
                },
                {
                    "ko": "클레임 서류에는 일일 공사 일지와 사진 증빙을 첨부해야 합니다.",
                    "vi": "Hồ sơ khiếu nại phải kèm theo nhật ký thi công hàng ngày và ảnh chứng minh.",
                    "situation": "formal"
                },
                {
                    "ko": "양측이 합의하지 못할 경우 중재로 해결하기로 했습니다.",
                    "vi": "Trường hợp hai bên không thỏa thuận được, sẽ giải quyết bằng trọng tài.",
                    "situation": "formal"
                }
            ],
            "relatedTerms": ["hợp-đồng-xây-dựng", "thay-đổi-thiết-kế", "điều-chỉnh-hợp-đồng", "trọng-tài"]
        },
        {
            "slug": "trọng-tài-xây-dựng",
            "korean": "건설중재",
            "vietnamese": "Trọng tài xây dựng",
            "hanja": "建設仲裁",
            "hanjaReading": "建(세울 건) + 設(베풀 설) + 仲(가운데 중) + 裁(마를 재)",
            "pronunciation": "쫑 따이 싸이 중",
            "meaningKo": "건설 분쟁을 법원이 아닌 중재기관을 통해 해결하는 절차를 의미합니다. 통역 시 '소송'과 '중재'의 차이를 명확히 설명하고, 중재 판정의 최종성과 집행력을 정확히 전달해야 합니다. 베트남에서는 VIAC(베트남국제중재센터)가 주요 중재기관이며, 국제 건설 계약에서는 SIAC(싱가포르) 또는 ICC(국제상업회의소) 중재를 선택하는 경우도 많습니다. 중재 비용과 절차, 중재인 선정 방법을 명확히 통역해야 합니다.",
            "meaningVi": "Trọng tài xây dựng là quá trình giải quyết tranh chấp xây dựng thông qua trung tâm trọng tài thay vì tòa án. Phán quyết trọng tài có tính chung thẩm và có thể thi hành như bản án của tòa. VIAC (Trung tâm Trọng tài Quốc tế Việt Nam) là trung tâm trọng tài chính tại Việt Nam. Với hợp đồng quốc tế, có thể chọn SIAC (Singapore) hoặc ICC (Paris).",
            "context": "건설 분쟁, 계약 협상, 법률 자문",
            "culturalNote": "한국에서는 대한상사중재원이 주요 중재기관이지만, 베트남에서는 VIAC(Vietnam International Arbitration Centre)가 가장 공신력 있는 기관입니다. 베트남에서는 중재가 소송보다 빠르고 비밀유지가 가능하며, 중재 판정이 외국에서도 집행 가능하다는 장점이 있어 국제 계약에서 선호됩니다. 중재 언어는 베트남어 또는 영어이며, 통역 비용은 당사자 부담입니다. 중재 비용은 분쟁 금액의 1-5%이며, 소송보다 저렴한 편입니다. 통역 시 중재 조항의 중요성을 강조하고, 계약서 작성 시 중재기관과 준거법을 명확히 명시해야 함을 전달해야 합니다.",
            "commonMistakes": [
                {
                    "mistake": "Kiện tụng (소송)",
                    "correction": "Trọng tài (중재)",
                    "explanation": "소송은 법원 절차이고, 중재는 사적 분쟁 해결 절차입니다."
                },
                {
                    "mistake": "중재 판정을 'Quyết định trọng tài'(중재 결정)로 표현",
                    "correction": "'Phán quyết trọng tài'(중재 판정)",
                    "explanation": "'Phán quyết'는 법적 구속력이 있는 판정을 의미합니다."
                },
                {
                    "mistake": "중재를 '조정'(Hòa giải)과 혼동",
                    "correction": "조정은 'Hòa giải', 중재는 'Trọng tài'로 구분",
                    "explanation": "조정은 합의를 도출하는 것이고, 중재는 판정을 내리는 것입니다."
                }
            ],
            "examples": [
                {
                    "ko": "계약서 제30조에 따라 이 분쟁은 VIAC 중재로 해결합니다.",
                    "vi": "Theo Điều 30 của hợp đồng, tranh chấp này sẽ được giải quyết bằng trọng tài tại VIAC.",
                    "situation": "formal"
                },
                {
                    "ko": "중재 판정은 최종적이며 양 당사자를 구속합니다.",
                    "vi": "Phán quyết trọng tài là chung thẩm và có hiệu lực ràng buộc đối với cả hai bên.",
                    "situation": "formal"
                },
                {
                    "ko": "중재인 3명으로 구성된 중재 판정부가 이 사건을 심리합니다.",
                    "vi": "Hội đồng trọng tài gồm 3 trọng tài viên sẽ xét xử vụ việc này.",
                    "situation": "formal"
                }
            ],
            "relatedTerms": ["tranh-chấp-xây-dựng", "hợp-đồng-xây-dựng", "tòa-án", "hòa-giải"]
        },
        {
            "slug": "giám-sát-thi-công",
            "korean": "건설감리",
            "vietnamese": "Giám sát thi công",
            "hanja": "建設監理",
            "hanjaReading": "建(세울 건) + 設(베풀 설) + 監(볼 감) + 理(다스릴 리)",
            "pronunciation": "잠 삿 티 꽁",
            "meaningKo": "발주자를 대신하여 설계도서대로 공사가 진행되는지 확인하고 품질을 관리하는 업무를 의미합니다. 통역 시 '감리자'와 '감독자'의 역할 차이를 명확히 구분해야 하며, 베트남에서는 감리가 의무인 공사 규모와 감리원 자격 기준이 법으로 정해져 있습니다. 감리 업무 범위(품질, 안전, 공정 관리 등)와 권한(시정 지시, 공사 중지 등)을 정확히 통역해야 하며, 감리 보고서 작성 주기와 내용도 계약 조건입니다.",
            "meaningVi": "Giám sát thi công là hoạt động thay mặt chủ đầu tư kiểm tra việc thi công đúng theo thiết kế và quản lý chất lượng công trình. Theo quy định, các công trình có quy mô nhất định bắt buộc phải có giám sát thi công, và giám sát viên phải có chứng chỉ hành nghề. Phạm vi công việc bao gồm quản lý chất lượng, an toàn, tiến độ, và có quyền yêu cầu khắc phục hoặc tạm dừng thi công nếu phát hiện vi phạm.",
            "context": "건설 현장, 품질 관리, 계약 관리",
            "culturalNote": "한국에서는 '감리'가 설계도서 검토와 시공 감독을 포괄하는 넓은 개념이지만, 베트남에서는 'Giám sát thi công'(시공 감독)과 'Tư vấn giám sát'(감리 컨설팅)으로 구분되는 경우가 있습니다. 베트남에서는 일정 규모 이상의 공사(예: 계약금액 50억 동 이상)는 의무적으로 감리를 배치해야 하며, 감리원은 건설부에서 발급한 자격증을 보유해야 합니다. 감리 비용은 공사비의 3-7%이며, 발주자가 부담합니다. 통역 시 감리의 독립성과 중립성을 강조하고, 감리 지적 사항은 반드시 이행해야 함을 명확히 전달해야 합니다.",
            "commonMistakes": [
                {
                    "mistake": "Giám sát (일반 감독)",
                    "correction": "Giám sát thi công (건설감리)",
                    "explanation": "'Giám sát'은 일반 감독이고, 'Giám sát thi công'은 전문 건설감리입니다."
                },
                {
                    "mistake": "감리와 시공 관리를 구분하지 않음",
                    "correction": "감리는 'Giám sát thi công'(발주자 측), 시공 관리는 'Quản lý thi công'(시공자 측)",
                    "explanation": "감리는 발주자를 대리하고, 시공 관리는 시공사의 자체 관리입니다."
                },
                {
                    "mistake": "감리 지적을 'Ý kiến giám sát'(감리 의견)으로만 표현",
                    "correction": "'Yêu cầu khắc phục của giám sát'(감리 시정 요구)",
                    "explanation": "단순 의견이 아니라 이행 의무가 있는 요구사항입니다."
                }
            ],
            "examples": [
                {
                    "ko": "감리자의 승인 없이는 다음 공정으로 진행할 수 없습니다.",
                    "vi": "Không được phép chuyển sang công đoạn tiếp theo nếu chưa có sự chấp thuận của giám sát.",
                    "situation": "onsite"
                },
                {
                    "ko": "감리 보고서는 매주 금요일에 발주자에게 제출됩니다.",
                    "vi": "Báo cáo giám sát được nộp cho chủ đầu tư vào mỗi thứ Sáu hàng tuần.",
                    "situation": "formal"
                },
                {
                    "ko": "이 부분은 감리 지적 사항이므로 즉시 재시공해야 합니다.",
                    "vi": "Phần này là yêu cầu khắc phục của giám sát, cần thi công lại ngay lập tức.",
                    "situation": "onsite"
                }
            ],
            "relatedTerms": ["chất-lượng-công-trình", "quản-lý-thi-công", "chủ-đầu-tư", "nhà-thầu"]
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
