#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""부동산등기법 용어 추가 스크립트 (v7-c)"""

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
            "slug": "so-huu-quyen-chuyen-nhuong-dang-ky",
            "korean": "소유권이전등기",
            "vietnamese": "Đăng ký chuyển nhượng quyền sở hữu",
            "hanja": "所有權移轉登記",
            "hanjaReading": "所(바 소) + 有(있을 유) + 權(권세 권) + 移(옮길 이) + 轉(구를 전) + 登(오를 등) + 記(기록할 기)",
            "pronunciation": "소유꿘니전등기",
            "meaningKo": "부동산의 소유권이 매매, 증여, 상속 등으로 인해 다른 사람에게 이전될 때 이를 등기부에 기재하는 절차입니다. 통역 시 주의할 점은 한국에서는 등기를 해야만 소유권이 완전히 이전되지만(대항력 취득), 베트남에서는 Giấy chứng nhận quyền sử dụng đất(토지사용권증서) 발급이 핵심이라는 점을 구분해야 합니다. 한국의 '등기 완료=소유권 확정'이라는 개념이 베트남에서는 토지사용권 중심으로 이해되므로, 이 차이를 명확히 설명하지 않으면 법적 오해가 발생할 수 있습니다.",
            "meaningVi": "Thủ tục ghi chép vào sổ đăng ký khi quyền sở hữu bất động sản được chuyển từ người này sang người khác do mua bán, tặng cho, thừa kế, v.v. Ở Hàn Quốc, quyền sở hữu chỉ có hiệu lực pháp lý đầy đủ sau khi hoàn tất đăng ký chuyển nhượng.",
            "context": "부동산 거래, 상속, 증여 계약 통역",
            "culturalNote": "한국의 부동산 등기제도는 토지와 건물을 각각 등기하는 이원적 구조이며, 등기를 통해 제3자에 대한 대항력을 갖습니다. 반면 베트남은 토지는 국가 소유이므로 사용권만 등기되고, 건물은 소유권 등기가 가능합니다. 한국 통역사는 '소유권'과 '사용권'의 차이를 명확히 구분하여 통역해야 하며, 특히 부동산 투자 관련 통역에서 이 개념 혼동이 법적 분쟁으로 이어질 수 있음을 주의해야 합니다.",
            "commonMistakes": [
                {
                    "mistake": "Đăng ký tài sản",
                    "correction": "Đăng ký chuyển nhượng quyền sở hữu",
                    "explanation": "'재산등기'로 번역하면 너무 포괄적이며, 소유권 '이전' 개념이 빠집니다."
                },
                {
                    "mistake": "Chuyển tên sở hữu",
                    "correction": "Đăng ký chuyển nhượng quyền sở hữu",
                    "explanation": "'명의변경'은 행정적 표현이고, 법률 용어로는 정식 등기 절차를 명시해야 합니다."
                },
                {
                    "mistake": "등기=사용권증서 발급으로 번역",
                    "correction": "한국의 등기제도와 베트남의 토지사용권증서 제도는 별개임을 설명",
                    "explanation": "두 나라의 부동산 법체계 차이를 무시하면 법적 오해 발생"
                }
            ],
            "examples": [
                {
                    "ko": "매매계약 후 30일 이내에 소유권이전등기를 신청해야 합니다.",
                    "vi": "Phải nộp đơn đăng ký chuyển nhượng quyền sở hữu trong vòng 30 ngày sau khi ký hợp đồng mua bán.",
                    "situation": "formal"
                },
                {
                    "ko": "등기 안 하면 나중에 분쟁 생길 수 있어요.",
                    "vi": "Nếu không đăng ký thì sau này có thể phát sinh tranh chấp đấy.",
                    "situation": "informal"
                },
                {
                    "ko": "소유권이전등기 완료 시 취득세를 납부하셔야 합니다.",
                    "vi": "Khi hoàn tất đăng ký chuyển nhượng quyền sở hữu, quý vị phải nộp thuế thu nhập.",
                    "situation": "onsite"
                }
            ],
            "relatedTerms": ["등기부등본", "근저당권설정등기", "가등기", "말소등기"]
        },
        {
            "slug": "can-the-chap",
            "korean": "근저당권",
            "vietnamese": "Quyền cầm cố thế chấp",
            "hanja": "根抵當權",
            "hanjaReading": "根(뿌리 근) + 抵(막을 저) + 當(마땅할 당) + 權(권세 권)",
            "pronunciation": "근저당꿘",
            "meaningKo": "채무자가 여러 번에 걸쳐 발생하는 불특정 채무를 담보하기 위해 미리 최고액을 정하여 부동산에 설정하는 저당권입니다. 일반 저당권과 달리 계속적 거래관계에서 발생하는 채무를 포괄적으로 담보하며, 은행 대출 시 가장 흔히 사용됩니다. 통역 시 주의할 점은 한국에서는 근저당권이 매우 보편적인 담보 방식이지만, 베트남에서는 Quyền thế chấp(일반 저당권)이 더 일반적이며, 근저당권 개념이 생소할 수 있다는 점입니다. 특히 '최고액'과 '실제 채무액'의 차이를 명확히 설명해야 합니다.",
            "meaningVi": "Quyền thế chấp được thiết lập trên bất động sản với mức tối đa nhất định để đảm bảo cho các khoản nợ không xác định phát sinh nhiều lần theo thời gian. Khác với quyền thế chấp thông thường, quyền này bảo đảm toàn diện cho các khoản nợ phát sinh từ quan hệ giao dịch liên tục.",
            "context": "은행 대출, 부동산 담보 계약 통역",
            "culturalNote": "한국에서는 부동산 담보 대출의 대부분이 근저당권 방식으로 이루어지며, 한 번 설정으로 여러 번의 대출과 상환이 가능합니다. 베트남에서는 이러한 포괄적 담보 개념이 덜 발달되어 있고, 개별 대출마다 별도 담보 설정을 하는 경우가 많습니다. 통역사는 한국의 금융 관행과 베트남의 담보 제도 차이를 이해하고, 특히 '최고액 2억 원'이 '실제 대출액 2억 원'이 아님을 명확히 전달해야 합니다.",
            "commonMistakes": [
                {
                    "mistake": "Quyền thế chấp",
                    "correction": "Quyền cầm cố thế chấp (근저당권) / Quyền thế chấp tối đa",
                    "explanation": "일반 저당권과 구분 없이 번역하면 법적 성격이 달라집니다."
                },
                {
                    "mistake": "최고액을 '대출 한도'로만 설명",
                    "correction": "담보 가능한 최대 채권액이며, 실제 대출액과는 다름을 명시",
                    "explanation": "최고액과 실제 채무액의 차이를 이해하지 못하면 담보 가치 오판 가능"
                },
                {
                    "mistake": "Thế chấp liên tục",
                    "correction": "Quyền cầm cố thế chấp / Quyền thế chấp bảo đảm khoản nợ tối đa",
                    "explanation": "'연속 저당'은 법률 용어가 아니며, 정확한 법적 명칭 사용 필요"
                }
            ],
            "examples": [
                {
                    "ko": "이 부동산에는 최고액 3억 원의 근저당권이 설정되어 있습니다.",
                    "vi": "Bất động sản này đã được thiết lập quyền cầm cố thế chấp với mức tối đa 300 triệu won.",
                    "situation": "formal"
                },
                {
                    "ko": "근저당 풀어야 매매가 가능해요.",
                    "vi": "Phải gỡ quyền cầm cố thế chấp thì mới bán được.",
                    "situation": "informal"
                },
                {
                    "ko": "근저당권 말소를 위해서는 채무 전액 상환이 필요합니다.",
                    "vi": "Để xóa bỏ quyền cầm cố thế chấp cần phải trả hết nợ.",
                    "situation": "onsite"
                }
            ],
            "relatedTerms": ["저당권", "소유권이전등기", "말소등기", "우선변제권"]
        },
        {
            "slug": "quyen-su-dung-mat-dat",
            "korean": "지상권",
            "vietnamese": "Quyền sử dụng mặt đất",
            "hanja": "地上權",
            "hanjaReading": "地(땅 지) + 上(위 상) + 權(권세 권)",
            "pronunciation": "지상꿘",
            "meaningKo": "타인의 토지에 건물이나 그 밖의 공작물이나 수목을 소유하기 위하여 그 토지를 사용할 수 있는 물권입니다. 소유권과 달리 토지 자체는 타인의 소유이지만, 지상권자는 그 위에 건물을 짓고 사용할 권리가 있습니다. 통역 시 주의할 점은 한국에서는 토지와 건물의 소유권이 분리될 수 있지만(일물일권주의 예외), 베트남에서는 토지는 국가 소유이므로 사용권만 존재하며, 이 개념 차이를 명확히 해야 합니다. 특히 공장용지나 송전탑 부지 등에서 자주 사용되는 권리입니다.",
            "meaningVi": "Quyền vật quyền cho phép sử dụng đất của người khác để xây dựng nhà cửa hoặc công trình kiến trúc, cây cối. Khác với quyền sở hữu, người có quyền sử dụng mặt đất không sở hữu đất nhưng có quyền xây dựng và sử dụng mặt đất đó.",
            "context": "부동산 임대차, 토지 사용 계약 통역",
            "culturalNote": "한국에서는 토지 소유자와 건물 소유자가 다를 수 있으며, 지상권은 이를 법적으로 보장하는 제도입니다. 전통적으로 타인의 토지에 건물을 짓고 오랫동안 사용하는 경우 관습법적 지상권이 인정되기도 합니다. 베트남에서는 모든 토지가 국가 소유이므로, 한국의 지상권 개념이 직접 대응되지 않습니다. 통역 시 '토지 소유권'이 아닌 '토지 사용권' 위에 설정되는 권리임을 명확히 해야 하며, 양국의 토지 제도 차이를 설명하는 것이 필수적입니다.",
            "commonMistakes": [
                {
                    "mistake": "Quyền đất",
                    "correction": "Quyền sử dụng mặt đất",
                    "explanation": "'토지권'은 너무 포괄적이며, 법률상 정확한 명칭이 아닙니다."
                },
                {
                    "mistake": "Quyền thuê đất",
                    "correction": "Quyền sử dụng mặt đất (물권) vs Quyền thuê (채권)",
                    "explanation": "지상권은 물권이고 임차권은 채권으로, 법적 성격이 완전히 다릅니다."
                },
                {
                    "mistake": "지상권을 단순 '토지 사용권'으로 번역",
                    "correction": "타인 토지에 건물 등을 소유하기 위한 특수한 권리임을 명시",
                    "explanation": "일반적인 토지 사용과 법적 개념이 다름"
                }
            ],
            "examples": [
                {
                    "ko": "송전탑 부지에 대해 한전이 지상권을 설정했습니다.",
                    "vi": "Tổng công ty điện lực đã thiết lập quyền sử dụng mặt đất cho khu vực cột điện cao thế.",
                    "situation": "formal"
                },
                {
                    "ko": "남의 땅인데 건물은 내 거예요. 지상권 있어요.",
                    "vi": "Đất của người khác nhưng nhà là của tôi. Tôi có quyền sử dụng mặt đất.",
                    "situation": "informal"
                },
                {
                    "ko": "지상권 존속기간은 30년으로 설정되었습니다.",
                    "vi": "Thời hạn tồn tại của quyền sử dụng mặt đất được thiết lập là 30 năm.",
                    "situation": "onsite"
                }
            ],
            "relatedTerms": ["지역권", "전세권", "임차권", "물권"]
        },
        {
            "slug": "quyen-su-dung-dat-cua-nguoi-khac",
            "korean": "지역권",
            "vietnamese": "Quyền sử dụng đất của người khác",
            "hanja": "地役權",
            "hanjaReading": "地(땅 지) + 役(부릴 역) + 權(권세 권)",
            "pronunciation": "지역꿘",
            "meaningKo": "자기 토지의 편익을 위하여 타인의 토지를 일정한 목적으로 사용할 수 있는 물권입니다. 예를 들어 도로가 없는 토지의 소유자가 이웃 토지를 통행할 권리나, 용수를 끌어올 권리 등이 지역권에 해당합니다. 통역 시 주의할 점은 지역권은 특정 토지의 이용 편의를 위한 것으로, 지상권처럼 건물을 짓는 권리가 아니라는 점입니다. 한국에서는 통행지역권, 인수지역권 등이 실무에서 자주 문제되며, 베트남에서도 Quyền đi lại 등 유사 개념이 있으나 법적 체계는 다릅니다.",
            "meaningVi": "Quyền vật quyền cho phép sử dụng đất của người khác với mục đích nhất định để phục vụ lợi ích cho đất của mình. Ví dụ: quyền đi lại qua đất của người khác khi đất mình không có đường, quyền lấy nước, v.v.",
            "context": "토지 분쟁, 인접 토지 권리 관계 통역",
            "culturalNote": "한국에서는 맹지(도로에 접하지 않은 토지) 문제로 인한 통행지역권 분쟁이 매우 흔합니다. 민법상 주위토지통행권도 인정되지만, 지역권 등기를 하면 더 강력한 법적 보호를 받습니다. 베트남에서도 농촌 지역에서 유사한 통행권 문제가 발생하나, 관습적으로 해결되는 경우가 많고 등기 제도가 덜 발달되어 있습니다. 통역사는 한국의 명확한 물권 체계와 베트남의 상대적으로 유연한 관습 사이의 차이를 이해하고 전달해야 합니다.",
            "commonMistakes": [
                {
                    "mistake": "Quyền đi lại",
                    "correction": "Quyền sử dụng đất của người khác (포괄) / Quyền đi lại (통행지역권, 일부)",
                    "explanation": "'통행권'은 지역권의 한 종류일 뿐, 전체를 대표하지 못합니다."
                },
                {
                    "mistake": "지역권을 지상권과 혼동",
                    "correction": "지상권=건물 소유, 지역권=토지 이용 편의",
                    "explanation": "두 권리의 목적과 내용이 완전히 다릅니다."
                },
                {
                    "mistake": "Quyền sử dụng chung",
                    "correction": "Quyền sử dụng đất của người khác vì lợi ích đất mình",
                    "explanation": "'공동 사용권'은 지역권의 종속성(특정 토지 편익 목적) 개념이 없습니다."
                }
            ],
            "examples": [
                {
                    "ko": "우리 집은 맹지라서 옆집 땅에 통행지역권을 설정했습니다.",
                    "vi": "Nhà tôi không có đường nên đã thiết lập quyền đi lại qua đất nhà bên cạnh.",
                    "situation": "formal"
                },
                {
                    "ko": "물 끌어다 쓸 수 있게 지역권 등기 해뒀어요.",
                    "vi": "Đã đăng ký quyền lấy nước để có thể dùng nước.",
                    "situation": "informal"
                },
                {
                    "ko": "지역권 설정으로 인한 손실은 보상을 받으실 수 있습니다.",
                    "vi": "Quý vị có thể nhận được bồi thường cho thiệt hại do việc thiết lập quyền sử dụng đất.",
                    "situation": "onsite"
                }
            ],
            "relatedTerms": ["지상권", "통행권", "맹지", "주위토지통행권"]
        },
        {
            "slug": "quyen-thue-nha",
            "korean": "전세권",
            "vietnamese": "Quyền thuê nhà trọn gói",
            "hanja": "傳貰權",
            "hanjaReading": "傳(전할 전) + 貰(살 세) + 權(권세 권)",
            "pronunciation": "전세꿘",
            "meaningKo": "전세금을 지급하고 타인의 부동산을 점유하여 사용·수익하며, 그 부동산 전부에 대하여 후순위권리자나 기타 채권자보다 전세금을 우선변제받을 수 있는 물권입니다. 한국 특유의 제도로, 월세와 달리 목돈을 맡기고 이자 대신 거주하며, 계약 종료 시 전액 반환받습니다. 통역 시 가장 주의해야 할 점은 베트남에는 전세 개념이 전혀 없다는 것입니다. 베트남 사람들은 보통 월세(thuê nhà theo tháng)나 매매만 알고 있어, 전세 시스템 자체를 상세히 설명해야 합니다.",
            "meaningVi": "Quyền vật quyền độc đáo của Hàn Quốc, cho phép người thuê trả một khoản tiền lớn (tiền đặt cọc Jeonse) để chiếm hữu và sử dụng bất động sản, sau khi hết hợp đồng nhận lại toàn bộ số tiền đó thay vì trả tiền thuê hàng tháng. Người có quyền Jeonse có quyền ưu tiên được hoàn trả tiền trước các chủ nợ khác.",
            "context": "부동산 임대차 계약, 주거 계약 통역",
            "culturalNote": "전세는 한국의 독특한 주거 문화로, 집주인은 전세금을 운용하여 수익을 얻고 세입자는 월세 부담 없이 거주합니다. 베트남에는 이러한 제도가 없으며, 대부분 월세(Thuê trả hàng tháng) 또는 보증금+월세(Tiền cọc + Tiền thuê) 방식입니다. 통역 시 전세 시스템, 전세금 반환 보장(우선변제권), 깡통전세 위험 등을 모두 설명해야 하며, 베트남인이 이해하기 어려운 개념이므로 충분한 부연 설명이 필수입니다. '이자 없이 빌려주는 대출'로 비유하면 이해가 쉽습니다.",
            "commonMistakes": [
                {
                    "mistake": "Thuê nhà",
                    "correction": "Quyền thuê nhà trọn gói (Jeonse) - trả tiền lớn 1 lần, không trả tiền hàng tháng",
                    "explanation": "단순 '임대'로 번역하면 월세와 구분되지 않습니다."
                },
                {
                    "mistake": "Tiền cọc",
                    "correction": "Tiền Jeonse (전세금) - số tiền lớn được hoàn trả 100%",
                    "explanation": "'보증금'과 '전세금'은 성격과 금액이 완전히 다릅니다."
                },
                {
                    "mistake": "전세를 월세의 일종으로 설명",
                    "correction": "전세는 물권이고 월세는 채권, 법적 성격이 다름",
                    "explanation": "전세권은 등기 가능한 물권이고, 임차권은 채권입니다."
                }
            ],
            "examples": [
                {
                    "ko": "이 아파트는 전세 2억 원입니다.",
                    "vi": "Căn hộ này có giá Jeonse 200 triệu won (trả 1 lần, sau 2 năm nhận lại đủ).",
                    "situation": "formal"
                },
                {
                    "ko": "전세 살아요. 월세 안 내요.",
                    "vi": "Tôi thuê Jeonse. Không phải trả tiền hàng tháng.",
                    "situation": "informal"
                },
                {
                    "ko": "전세권 설정등기를 하시면 우선변제권이 생깁니다.",
                    "vi": "Nếu đăng ký quyền Jeonse, quý vị sẽ có quyền được hoàn trả tiền ưu tiên.",
                    "situation": "onsite"
                }
            ],
            "relatedTerms": ["임차권", "우선변제권", "전세금", "보증금"]
        },
        {
            "slug": "ban-sao-so-dang-ky-bat-dong-san",
            "korean": "등기부등본",
            "vietnamese": "Bản sao sổ đăng ký bất động sản",
            "hanja": "登記簿謄本",
            "hanjaReading": "登(오를 등) + 記(기록할 기) + 簿(문서 부) + 謄(베낄 등) + 本(근본 본)",
            "pronunciation": "등기부등본",
            "meaningKo": "부동산 등기부에 기록된 내용을 그대로 베껴서 발급한 공적 증명서로, 해당 부동산의 소유권 현황, 권리관계(근저당권, 전세권 등), 제한사항 등을 확인할 수 있는 중요한 서류입니다. 통역 시 주의할 점은 등기부등본이 법적 공신력을 가진 공적 장부라는 점과, 표제부(물리적 현황), 갑구(소유권), 을구(소유권 외 권리)로 구성된다는 점을 설명해야 합니다. 베트남의 Giấy chứng nhận quyền sử dụng đất와 유사하지만, 한국 등기부등본은 모든 권리변동이 기록되는 반면 베트남 증서는 현재 상태만 표시한다는 차이가 있습니다.",
            "meaningVi": "Bản sao chính thức ghi chép đầy đủ nội dung trong sổ đăng ký bất động sản, cho phép xác nhận tình trạng quyền sở hữu, các quyền liên quan (thế chấp, Jeonse, v.v.), và các hạn chế đối với bất động sản đó. Đây là tài liệu quan trọng có giá trị pháp lý cao.",
            "context": "부동산 거래, 대출 신청, 권리 확인 통역",
            "culturalNote": "한국에서는 부동산 거래 전 반드시 등기부등본을 확인하여 소유권, 근저당권, 가압류, 가처분 등을 체크합니다. 인터넷으로 즉시 발급 가능하며(대법원 인터넷등기소), 수수료는 1,000원 정도로 매우 저렴합니다. 베트nam에서는 Sổ đỏ(빨간 책)라 불리는 토지사용권증서가 유사한 역할을 하지만, 모든 권리변동 이력이 기록되지는 않습니다. 통역사는 한국의 등기부등본이 '거래 안전의 핵심 도구'라는 점과, 3개 부분(표제부, 갑구, 을구)의 구조를 설명할 수 있어야 합니다.",
            "commonMistakes": [
                {
                    "mistake": "Giấy tờ nhà đất",
                    "correction": "Bản sao sổ đăng ký bất động sản (등기부등본)",
                    "explanation": "'부동산 서류'는 너무 포괄적이며, 공적 장부의 특성이 드러나지 않습니다."
                },
                {
                    "mistake": "Sổ đỏ로만 번역",
                    "correction": "한국 등기부등본 ≠ 베트남 Sổ đỏ, 기능 유사하나 구조 다름",
                    "explanation": "Sổ đỏ는 현재 권리만 표시, 등기부등본은 모든 권리변동 기록"
                },
                {
                    "mistake": "등본과 초본 구분 없이 번역",
                    "correction": "등본(Bản sao đầy đủ) vs 초본(Bản trích lục)",
                    "explanation": "등본은 전체 내용, 초본은 일부 발췌본"
                }
            ],
            "examples": [
                {
                    "ko": "계약 전에 등기부등본을 반드시 확인하셔야 합니다.",
                    "vi": "Trước khi ký hợp đồng, quý vị nhất định phải kiểm tra bản sao sổ đăng ký bất động sản.",
                    "situation": "formal"
                },
                {
                    "ko": "등본 떼서 근저당 확인했어요.",
                    "vi": "Đã lấy bản sao sổ đăng ký và kiểm tra quyền thế chấp rồi.",
                    "situation": "informal"
                },
                {
                    "ko": "등기부등본 을구에 전세권 설정 기록이 있습니다.",
                    "vi": "Ở phần quyền khác (을구) của bản sao sổ đăng ký có ghi chép về quyền Jeonse.",
                    "situation": "onsite"
                }
            ],
            "relatedTerms": ["등기사항증명서", "소유권이전등기", "근저당권", "가압류"]
        },
        {
            "slug": "dang-ky-tam-thoi",
            "korean": "가등기",
            "vietnamese": "Đăng ký tạm thời",
            "hanja": "假登記",
            "hanjaReading": "假(거짓 가) + 登(오를 등) + 記(기록할 기)",
            "pronunciation": "가등기",
            "meaningKo": "본등기를 할 수 없는 사유가 있을 때 장래 본등기의 순위를 보전하기 위하여 미리 하는 예비적 등기입니다. 예를 들어 매매대금을 완납하지 못했거나 소유권이전에 필요한 서류가 미비한 경우, 가등기를 해두면 나중에 본등기를 할 때 가등기 시점의 순위를 주장할 수 있습니다. 통역 시 주의할 점은 가등기는 '완전한 권리'가 아니라 '순위 보전용'이라는 점과, 가등기 후 제3자가 본등기를 해도 나중에 가등기를 본등기로 전환하면 우선권을 갖는다는 것을 명확히 해야 합니다.",
            "meaningVi": "Đăng ký dự phòng được thực hiện trước khi có thể làm đăng ký chính thức, nhằm bảo toàn thứ tự ưu tiên cho việc đăng ký chính thức trong tương lai. Ví dụ: khi chưa thanh toán hết tiền mua bán hoặc thiếu giấy tờ, có thể làm đăng ký tạm thời để giữ quyền ưu tiên.",
            "context": "부동산 매매 계약, 권리 보전 통역",
            "culturalNote": "한국에서는 부동산 거래 시 가등기를 자주 활용합니다. 특히 분양권 전매, 재개발 지역 부동산 거래 등에서 가등기를 통해 권리를 보전하는 경우가 많습니다. 가등기담보권도 실무에서 중요한데, 이는 담보 목적의 가등기로 채무 불이행 시 소유권을 취득할 수 있습니다. 베트남에는 명확한 가등기 제도가 없으며, 통역사는 '순위 보전'이라는 개념과 가등기의 법적 효력(순위 확보 vs 완전한 권리 X)을 정확히 전달해야 합니다.",
            "commonMistakes": [
                {
                    "mistake": "Đăng ký giả",
                    "correction": "Đăng ký tạm thời / Đăng ký dự phòng",
                    "explanation": "'가짜 등기'로 직역하면 부정적 의미가 되어 법적 제도의 성격이 왜곡됩니다."
                },
                {
                    "mistake": "가등기를 '미완료 등기'로 설명",
                    "correction": "순위 보전을 위한 예비적 등기",
                    "explanation": "가등기는 목적이 순위 확보이지, 단순히 미완료 상태가 아닙니다."
                },
                {
                    "mistake": "Đăng ký không chính thức",
                    "correction": "Đăng ký tạm thời có giá trị pháp lý về thứ tự ưu tiên",
                    "explanation": "가등기는 법적 효력이 있으며, '비공식'이 아닙니다."
                }
            ],
            "examples": [
                {
                    "ko": "계약금만 지불한 상태에서 가등기를 했습니다.",
                    "vi": "Đã làm đăng ký tạm thời trong tình trạng mới trả tiền đặt cọc.",
                    "situation": "formal"
                },
                {
                    "ko": "가등기 해놓으면 나중에 우선권 있어요.",
                    "vi": "Nếu làm đăng ký tạm thời thì sau này có quyền ưu tiên.",
                    "situation": "informal"
                },
                {
                    "ko": "가등기를 본등기로 전환하시면 소유권이 확정됩니다.",
                    "vi": "Khi chuyển đổi đăng ký tạm thời thành đăng ký chính thức, quyền sở hữu sẽ được xác định.",
                    "situation": "onsite"
                }
            ],
            "relatedTerms": ["본등기", "소유권이전등기", "순위보전", "가등기담보"]
        },
        {
            "slug": "xoa-bo-dang-ky",
            "korean": "말소등기",
            "vietnamese": "Xóa bỏ đăng ký",
            "hanja": "抹消登記",
            "hanjaReading": "抹(지울 말) + 消(사라질 소) + 登(오를 등) + 記(기록할 기)",
            "pronunciation": "말소등기",
            "meaningKo": "등기부에 이미 기재된 등기사항이 원인의 소멸, 무효 등으로 인하여 그 효력을 잃게 된 경우 이를 등기부에서 지우는 등기입니다. 예를 들어 대출을 모두 갚아 근저당권이 소멸하면 말소등기를 하여 등기부에서 그 기록을 지웁니다. 통역 시 주의할 점은 말소등기는 '완전히 삭제'가 아니라 '효력 상실 표시'(붉은 줄 표시)라는 점과, 채무 변제 후 채권자(은행)가 말소서류를 주어야 말소등기가 가능하다는 점을 설명해야 합니다.",
            "meaningVi": "Đăng ký xóa bỏ những nội dung đã ghi chép trong sổ đăng ký khi các quyền đó hết hiệu lực do nguyên nhân mất đi, vô hiệu, v.v. Ví dụ: khi trả hết nợ ngân hàng, quyền thế chấp sẽ được xóa bỏ khỏi sổ đăng ký.",
            "context": "대출 상환, 담보 해제 통역",
            "culturalNote": "한국에서는 대출 상환 후 반드시 근저당권 말소등기를 해야 깨끗한 등기부를 유지할 수 있습니다. 은행에서 말소서류(근저당권설정계약서, 위임장, 인감증명서 등)를 받아 법무사를 통해 또는 본인이 직접 등기소에 신청합니다. 말소등기를 하지 않으면 부동산 매매 시 문제가 되므로 주의가 필요합니다. 베트남에서도 유사한 절차가 있으나, 은행과 등기소 간 전산 연계가 덜 발달되어 수동 처리가 많습니다. 통역사는 말소 절차와 필요 서류를 명확히 설명해야 합니다.",
            "commonMistakes": [
                {
                    "mistake": "Xóa đăng ký",
                    "correction": "Xóa bỏ đăng ký (말소등기) / Đăng ký việc xóa bỏ",
                    "explanation": "단순 '삭제'가 아니라 '말소를 등기하는 것'이므로 정확한 법률 용어 필요"
                },
                {
                    "mistake": "말소등기를 '기록 삭제'로만 설명",
                    "correction": "효력 상실을 표시하는 등기 절차",
                    "explanation": "말소등기는 기록이 완전히 사라지는 게 아니라 효력 없음을 표시(붉은 줄)"
                },
                {
                    "mistake": "Hủy đăng ký",
                    "correction": "Xóa bỏ đăng ký (말소) vs Hủy (취소)",
                    "explanation": "'취소'는 처음부터 무효, '말소'는 효력 소멸"
                }
            ],
            "examples": [
                {
                    "ko": "대출 다 갚았으니 근저당권 말소등기 해야죠.",
                    "vi": "Đã trả hết nợ rồi thì phải làm đăng ký xóa bỏ quyền thế chấp.",
                    "situation": "formal"
                },
                {
                    "ko": "말소 안 하면 집 팔 때 문제 생겨요.",
                    "vi": "Nếu không xóa bỏ thì khi bán nhà sẽ có vấn đề.",
                    "situation": "informal"
                },
                {
                    "ko": "은행에서 말소서류 받으셨으면 법무사에게 의뢰하시면 됩니다.",
                    "vi": "Nếu đã nhận giấy tờ xóa bỏ từ ngân hàng, quý vị có thể nhờ luật sư đăng ký viên.",
                    "situation": "onsite"
                }
            ],
            "relatedTerms": ["근저당권", "전세권", "소유권이전등기", "말소서류"]
        },
        {
            "slug": "dang-ky-uy-탁",
            "korean": "신탁등기",
            "vietnamese": "Đăng ký ủy thác",
            "hanja": "信託登記",
            "hanjaReading": "信(믿을 신) + 託(맡길 탁) + 登(오를 등) + 記(기록할 기)",
            "pronunciation": "신탁등기",
            "meaningKo": "부동산의 소유권을 신탁회사에 이전하되, 신탁 목적에 따라 관리·운영하고 수익은 수익자(보통 원소유자)가 받는 방식의 등기입니다. 신탁등기가 되면 등기부상 소유자는 신탁회사로 표시되며, 신탁원부에 위탁자와 수익자가 기재됩니다. 통역 시 주의할 점은 신탁등기는 단순 위임이 아니라 소유권 자체가 신탁회사로 이전된다는 점과, 채권자로부터 보호받을 수 있다는 신탁의 도산격리 효과를 설명해야 합니다. 부동산 개발, 재건축 등에서 자주 사용됩니다.",
            "meaningVi": "Đăng ký chuyển quyền sở hữu bất động sản cho công ty ủy thác (신탁회사), nhưng công ty này chỉ quản lý và vận hành theo mục đích ủy thác, còn người thụ hưởng (thường là chủ sở hữu ban đầu) nhận lợi ích. Trên sổ đăng ký, chủ sở hữu sẽ hiển thị là công ty ủy thác.",
            "context": "부동산 개발, 분양, 재건축 통역",
            "culturalNote": "한국에서는 아파트 분양, 재건축·재개발 사업에서 신탁등기가 매우 보편적입니다. 시행사나 건설사가 부도나도 신탁등기된 부동산은 보호받을 수 있어 수분양자(입주 예정자)를 보호하는 장치로 활용됩니다. 베트남에서는 신탁 제도가 발달하지 않았으며, 유사한 개념을 설명하기 어려울 수 있습니다. 통역사는 '소유권 이전'과 '관리 위탁'의 차이, 그리고 신탁의 법적 보호 효과(도산격리)를 명확히 전달해야 합니다.",
            "commonMistakes": [
                {
                    "mistake": "Đăng ký ủy quyền",
                    "correction": "Đăng ký ủy thác (소유권 이전)",
                    "explanation": "'위임'은 소유권 이전 없이 권한만 주는 것, '신탁'은 소유권이 이전됨"
                },
                {
                    "mistake": "신탁을 단순 '관리 맡김'으로 설명",
                    "correction": "소유권이 신탁회사로 이전되며, 도산격리 효과 있음",
                    "explanation": "신탁의 핵심은 소유권 이전과 법적 보호"
                },
                {
                    "mistake": "Đăng ký quản lý",
                    "correction": "Đăng ký ủy thác - chuyển quyền sở hữu để bảo vệ pháp lý",
                    "explanation": "'관리 등기'는 신탁의 법적 성격을 표현하지 못함"
                }
            ],
            "examples": [
                {
                    "ko": "이 아파트는 신탁등기가 되어 있어 안전합니다.",
                    "vi": "Căn hộ này đã có đăng ký ủy thác nên an toàn.",
                    "situation": "formal"
                },
                {
                    "ko": "신탁 걸려있으면 건설사 망해도 보호받아요.",
                    "vi": "Nếu có ủy thác thì dù công ty xây dựng phá sản cũng được bảo vệ.",
                    "situation": "informal"
                },
                {
                    "ko": "신탁등기 말소는 사업 완료 후 이루어집니다.",
                    "vi": "Việc xóa bỏ đăng ký ủy thác sẽ được thực hiện sau khi hoàn thành dự án.",
                    "situation": "onsite"
                }
            ],
            "relatedTerms": ["신탁회사", "수익자", "도산격리", "분양보증"]
        },
        {
            "slug": "so-dat-dai",
            "korean": "토지대장",
            "vietnamese": "Sổ đất đai",
            "hanja": "土地臺帳",
            "hanjaReading": "土(흙 토) + 地(땅 지) + 臺(대 대) + 帳(장부 장)",
            "pronunciation": "토지대장",
            "meaningKo": "토지의 물리적 현황(지번, 지목, 면적, 소재지 등)을 기록한 공적 장부로, 토지의 표시에 관한 사항을 증명하는 서류입니다. 등기부등본이 '권리관계'를 보여준다면, 토지대장은 '물리적 상태'를 보여줍니다. 통역 시 주의할 점은 토지대장과 등기부가 일치하지 않을 수 있으며(예: 지목 변경 미반영), 실제 토지 거래 시 두 서류를 모두 확인해야 한다는 점입니다. 베트남에서는 Sổ đỏ에 토지 정보와 권리 정보가 함께 기재되므로, 한국의 이원적 시스템(등기부+토지대장)을 설명해야 합니다.",
            "meaningVi": "Sổ công khai ghi chép tình trạng vật lý của đất đai (số thửa, mục đích sử dụng đất, diện tích, vị trí, v.v.), là tài liệu chứng minh các thông tin về hiện trạng đất. Nếu sổ đăng ký (등기부) ghi chép về quyền lợi thì sổ đất đai ghi chép về tình trạng vật lý.",
            "context": "토지 거래, 개발 허가 통역",
            "culturalNote": "한국에서는 토지와 건물의 등기가 분리되어 있고, 토지의 물리적 현황은 토지대장에, 권리관계는 등기부에 각각 기재됩니다. 지목(전, 답, 대지, 임야 등)에 따라 용도와 세금이 달라지므로 토지대장 확인이 중요합니다. 베트남의 Sổ đỏ는 토지 정보와 권리 정보를 통합 관리하므로, 한국의 이원 시스템을 이해시키기 위해서는 '등기부=권리, 토지대장=물리적 현황'이라는 구분을 명확히 해야 합니다.",
            "commonMistakes": [
                {
                    "mistake": "Sổ đăng ký đất",
                    "correction": "Sổ đất đai (토지대장) vs Sổ đăng ký (등기부)",
                    "explanation": "'등기부'와 '토지대장'은 별개의 장부입니다."
                },
                {
                    "mistake": "토지대장을 Sổ đỏ로 번역",
                    "correction": "Sổ đỏ = 등기부+토지대장 통합, 한국은 분리 시스템",
                    "explanation": "베트남 Sổ đỏ는 통합 장부, 한국은 이원 시스템"
                },
                {
                    "mistake": "Danh sách đất",
                    "correction": "Sổ đất đai (공적 장부)",
                    "explanation": "'토지 목록'은 공적 장부의 법적 성격을 표현하지 못함"
                }
            ],
            "examples": [
                {
                    "ko": "토지대장을 확인해보니 지목이 전으로 되어 있네요.",
                    "vi": "Kiểm tra sổ đất đai thì thấy mục đích sử dụng là ruộng.",
                    "situation": "formal"
                },
                {
                    "ko": "대장이랑 등기부 면적이 다르면 측량해야 해요.",
                    "vi": "Nếu diện tích trên sổ đất đai và sổ đăng ký khác nhau thì phải đo đạc.",
                    "situation": "informal"
                },
                {
                    "ko": "토지대장등본은 주민센터에서 발급받으실 수 있습니다.",
                    "vi": "Bản sao sổ đất đai có thể xin cấp tại văn phòng hành chính.",
                    "situation": "onsite"
                }
            ],
            "relatedTerms": ["등기부등본", "지목", "지번", "건축물대장"]
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
