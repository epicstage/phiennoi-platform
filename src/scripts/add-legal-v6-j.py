#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""민사집행법 용어 추가 스크립트 (v6-j)"""

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
            "slug": "cuong-che-thi-hanh",
            "korean": "강제집행",
            "vietnamese": "Cưỡng chế thi hành",
            "hanja": "強制執行",
            "hanjaReading": "强(강할 강) + 制(제도 제) + 執(잡을 집) + 行(다닐 행)",
            "pronunciation": "꽝째 티 항",
            "meaningKo": "법원의 판결이나 집행권원에 기하여 채무자가 임의로 이행하지 않을 때 국가권력으로 강제로 채권을 실현하는 절차입니다. 통역 시 베트남에서는 'cưỡng chế'라는 표현이 경찰의 물리적 강제를 연상시킬 수 있으므로, 법적 절차임을 강조해야 합니다. 한국의 강제집행은 금전집행, 인도집행, 부작위집행 등으로 세분화되어 있으며, 베트남보다 집행절차가 엄격하고 채무자 권리 보호 장치가 많다는 점을 설명해야 합니다. '집행권원이 있어야 한다'는 전제조건을 반드시 명확히 해야 오해를 방지할 수 있습니다.",
            "meaningVi": "Thủ tục áp dụng quyền lực nhà nước để cưỡng bức thực hiện nghĩa vụ theo bản án hoặc quyết định thi hành của tòa án khi con nợ không tự nguyện thực hiện. Ở Hàn Quốc, cưỡng chế thi hành được phân loại thành thi hành tiền tệ, thi hành giao nộp tài sản, thi hành hành vi, với nhiều biện pháp bảo vệ quyền con nợ hơn Việt Nam.",
            "context": "민사소송 판결 확정 후 채무자가 이행하지 않는 경우 법원 집행관을 통해 진행",
            "culturalNote": "한국은 법원 집행관 중심의 강제집행 시스템이 발달해 있고, 채무자의 재산조사와 압류 절차가 체계적입니다. 베트남은 집행기관(cơ quan thi hành án)이 별도로 존재하며, 실제 집행률이 한국보다 낮고 시간이 오래 걸리는 편입니다. 한국에서는 집행불능 시 개인회생이나 파산 제도로 연결되지만, 베트남은 이러한 제도가 상대적으로 덜 발달했습니다. 통역 시 양국의 집행 실효성 차이를 염두에 두어야 합니다.",
            "commonMistakes": [
                {
                    "mistake": "cưỡng chế를 'khống chế'(억압, 통제)로 번역",
                    "correction": "cưỡng chế thi hành 또는 thi hành cưỡng chế",
                    "explanation": "khống chế는 경찰의 물리적 제압을 의미하므로 법률 절차와 맞지 않음"
                },
                {
                    "mistake": "강제집행을 '즉시 집행'으로 오해하여 'thực hiện ngay lập tức'로 통역",
                    "correction": "법적 절차를 거친 집행임을 명시: 'thi hành cưỡng chế theo quy định pháp luật'",
                    "explanation": "강제집행도 법정 절차와 유예기간이 있으므로 즉각 집행은 아님"
                },
                {
                    "mistake": "집행권원 없이도 가능한 것처럼 설명",
                    "correction": "반드시 'có căn cứ thi hành'(집행권원 보유)를 명시",
                    "explanation": "집행권원 없는 강제집행은 위법이므로 전제조건 설명 필수"
                }
            ],
            "examples": [
                {
                    "ko": "판결 확정 후 6개월이 지났는데도 채무자가 이행하지 않아 강제집행을 신청했습니다.",
                    "vi": "Sau 6 tháng kể từ khi bản án có hiệu lực, con nợ vẫn không thực hiện nên tôi đã nộp đơn xin cưỡng chế thi hành.",
                    "situation": "formal"
                },
                {
                    "ko": "부동산에 대한 강제집행은 경매 절차를 통해 진행됩니다.",
                    "vi": "Cưỡng chế thi hành đối với bất động sản được tiến hành thông qua thủ tục đấu giá.",
                    "situation": "formal"
                },
                {
                    "ko": "강제집행 과정에서 채무자가 재산을 은닉하면 처벌받을 수 있습니다.",
                    "vi": "Trong quá trình cưỡng chế thi hành, nếu con nợ giấu tài sản thì có thể bị xử phạt.",
                    "situation": "onsite"
                }
            ],
            "relatedTerms": ["집행권원", "압류", "경매", "집행불능"]
        },
        {
            "slug": "ap-luu",
            "korean": "압류",
            "vietnamese": "Áp lưu",
            "hanja": "押留",
            "hanjaReading": "押(누를 압) + 留(머무를 류)",
            "pronunciation": "압 류우",
            "meaningKo": "채무자의 재산을 법원이 강제집행의 목적으로 확보하여 처분을 금지하는 강제집행의 첫 단계 조치입니다. 통역 시 베트남어 'áp lưu'는 한자어 차용이지만 일상에서는 'tạm giữ tài sản'(재산 임시 보관)이라는 표현도 혼용되므로 맥락에 따라 선택해야 합니다. 한국에서는 부동산 압류는 등기부에 기재되고, 동산 압류는 현장에서 집행관이 직접 봉인하며, 채권 압류는 제3채무자에게 통지하는 방식으로 이루어집니다. 압류는 소유권을 박탈하는 것이 아니라 처분권만 제한한다는 점을 명확히 해야 합니다.",
            "meaningVi": "Biện pháp bảo toàn tài sản của con nợ do tòa án áp dụng nhằm cấm con nợ định đoạt tài sản, là bước đầu tiên của cưỡng chế thi hành. Áp lưu không tước quyền sở hữu mà chỉ hạn chế quyền định đoạt. Ở Hàn Quốc, bất động sản bị áp lưu được ghi vào sổ đăng ký, động sản được niêm phong tại chỗ, và yêu cầu nợ được thông báo cho người nợ thứ ba.",
            "context": "강제집행 절차에서 채무자 재산을 확보하기 위한 첫 단계",
            "culturalNote": "한국에서는 부동산 압류 시 등기부등본에 명시되어 공시되므로 투명하지만, 베트남은 압류 정보 접근이 상대적으로 제한적입니다. 한국은 인터넷뱅킹 계좌도 전자적으로 압류 가능하지만, 베트남은 아직 은행 계좌 압류 시스템이 덜 발달했습니다. 한국에서는 압류된 재산에서 최저생계비를 제외하는 등 채무자 보호 규정이 강하지만, 베트남은 이러한 제도가 약합니다. 통역 시 압류의 범위와 예외 조항을 정확히 전달해야 합니다.",
            "commonMistakes": [
                {
                    "mistake": "압류를 'tịch thu'(몰수)로 번역",
                    "correction": "áp lưu 또는 tạm giữ tài sản",
                    "explanation": "몰수는 소유권 박탈이지만 압류는 처분권 제한일 뿐임"
                },
                {
                    "mistake": "압류 즉시 소유권이 넘어간다고 설명",
                    "correction": "압류는 처분 금지일 뿐, 경매 후 배당 절차를 거쳐야 채권 회수",
                    "explanation": "압류는 보전 조치이지 소유권 이전이 아님"
                },
                {
                    "mistake": "가압류와 압류를 구분하지 않고 같은 용어로 번역",
                    "correction": "가압류는 'kê biên tài sản tạm thời', 압류는 'áp lưu/kê biên tài sản'",
                    "explanation": "가압류는 판결 전 보전조치, 압류는 판결 후 집행조치로 법적 성격이 다름"
                }
            ],
            "examples": [
                {
                    "ko": "채무자의 부동산에 대해 압류 등기를 완료했습니다.",
                    "vi": "Đã hoàn tất đăng ký áp lưu bất động sản của con nợ.",
                    "situation": "formal"
                },
                {
                    "ko": "은행 계좌가 압류되어 출금이 불가능합니다.",
                    "vi": "Tài khoản ngân hàng bị áp lưu nên không thể rút tiền.",
                    "situation": "onsite"
                },
                {
                    "ko": "압류 재산 목록에는 자동차와 예금이 포함되어 있습니다.",
                    "vi": "Danh mục tài sản bị áp lưu bao gồm ô tô và tiền gửi.",
                    "situation": "formal"
                }
            ],
            "relatedTerms": ["가압류", "강제집행", "경매", "채권압류"]
        },
        {
            "slug": "ga-ap-luu",
            "korean": "가압류",
            "vietnamese": "Kê biên tài sản tạm thời",
            "hanja": "假押留",
            "hanjaReading": "假(거짓 가) + 押(누를 압) + 留(머무를 류)",
            "pronunciation": "께 비엔 따이 산 땀 터이",
            "meaningKo": "금전채권에 대한 판결을 받기 전에 미리 채무자의 재산을 보전하는 민사보전절차입니다. 통역 시 베트남어로는 'tạm thời'(임시)를 강조하여 본압류와 구분해야 합니다. 한국에서는 가압류 신청 시 담보 제공이 필요하며, 피보전권리와 보전의 필요성을 소명해야 합니다. 가압류는 본안 소송 전 또는 소송 중에 신청 가능하며, 채무자의 재산 은닉을 방지하는 효과적인 수단입니다. 가압류 결정은 즉시 집행되지만, 채무자는 담보 제공으로 해방시킬 수 있다는 점을 설명해야 합니다.",
            "meaningVi": "Thủ tục bảo toàn dân sự nhằm bảo vệ tài sản của con nợ trước khi có bản án về quyền đòi nợ tiền. Khác với áp lưu chính thức, kê biên tạm thời được áp dụng khi chưa có phán quyết cuối cùng, nhằm ngăn con nợ che giấu tài sản. Ở Hàn Quốc, người xin kê biên phải cung cấp bảo lãnh và chứng minh sự cần thiết, con nợ có thể hủy bỏ bằng cách nộp bảo lãnh.",
            "context": "본안 소송 전후로 채무자의 재산 도피를 막기 위한 임시 조치",
            "culturalNote": "한국에서는 가압류가 매우 신속하게(긴급시 당일) 진행되며, 채무자에게 미리 통지하지 않고 집행할 수 있어 실효성이 높습니다. 베트남도 유사한 '재산 보전 조치'가 있지만, 절차가 한국보다 복잡하고 시간이 오래 걸립니다. 한국에서는 가압류를 남용하면 손해배상 책임이 있지만, 베트남은 이러한 규제가 약합니다. 한국 기업들이 베트남 거래처를 상대로 소송할 때 베트남 법원에 재산 보전을 신청하면 절차가 까다로워 한국만큼 신속하지 않다는 점을 통역 시 주의해야 합니다.",
            "commonMistakes": [
                {
                    "mistake": "가압류를 단순히 'áp lưu'로 번역하여 본압류와 구분 안 함",
                    "correction": "kê biên tài sản tạm thời 또는 áp lưu tạm thời",
                    "explanation": "가압류는 임시 조치이므로 'tạm thời' 명시 필수"
                },
                {
                    "mistake": "가압류가 확정 판결이라고 오해하여 설명",
                    "correction": "본안 소송 전 임시 보전 조치임을 명확히: 'biện pháp bảo toàn tạm thời trước khi có bản án'",
                    "explanation": "가압류는 판결이 아니라 절차적 보전일 뿐"
                },
                {
                    "mistake": "담보 제공 의무를 누락하고 통역",
                    "correction": "반드시 '담보 제공 필요'(cần cung cấp bảo lãnh) 언급",
                    "explanation": "가압류 신청자는 담보를 제공해야 하므로 중요한 조건"
                }
            ],
            "examples": [
                {
                    "ko": "소송 전에 채무자 재산에 가압류를 신청하여 재산 도피를 막았습니다.",
                    "vi": "Trước khi khởi kiện, tôi đã nộp đơn kê biên tạm thời tài sản con nợ để ngăn chặn việc chuyển dời tài sản.",
                    "situation": "formal"
                },
                {
                    "ko": "가압류 결정문을 받은 후 즉시 부동산 등기소에 제출했습니다.",
                    "vi": "Sau khi nhận quyết định kê biên tạm thời, tôi đã nộp ngay lên văn phòng đăng ký bất động sản.",
                    "situation": "onsite"
                },
                {
                    "ko": "가압류를 당한 채무자는 담보를 제공하면 해방시킬 수 있습니다.",
                    "vi": "Con nợ bị kê biên tạm thời có thể hủy bỏ bằng cách nộp bảo lãnh.",
                    "situation": "formal"
                }
            ],
            "relatedTerms": ["압류", "가처분", "담보제공", "본안소송"]
        },
        {
            "slug": "ga-cheo-bun",
            "korean": "가처분",
            "vietnamese": "Biện pháp khẩn cấp tạm thời",
            "hanja": "假處分",
            "hanjaReading": "假(거짓 가) + 處(처리할 처) + 分(나눌 분)",
            "pronunciation": "비엔 팝 칸 깝 땀 터이",
            "meaningKo": "권리관계에 대한 다툼이 있을 때 판결 확정 전에 임시로 권리를 보전하거나 현상을 유지하는 민사보전절차입니다. 통역 시 가압류(금전채권)와 가처분(비금전채권)의 차이를 명확히 해야 합니다. 한국에서는 부동산 처분금지 가처분, 점유이전금지 가처분, 임시의 지위를 정하는 가처분 등이 있습니다. 가처분은 긴급성이 인정될 때만 발령되며, 신청자는 담보를 제공해야 하고, 위반 시 간접강제나 형사처벌이 가능합니다. 베트남어로는 'biện pháp khẩn cấp'(긴급조치)를 강조하여 번역하는 것이 효과적입니다.",
            "meaningVi": "Thủ tục bảo toàn dân sự nhằm bảo vệ tạm thời quyền lợi hoặc duy trì hiện trạng trước khi có bản án cuối cùng khi có tranh chấp về quan hệ quyền. Khác với kê biên tạm thời (dành cho nợ tiền), biện pháp khẩn cấp tạm thời áp dụng cho các quyền không phải tiền tệ như cấm chuyển nhượng bất động sản, cấm thay đổi hiện trạng. Người xin phải chứng minh tính cấp thiết và cung cấp bảo lãnh.",
            "context": "권리침해가 임박하거나 현상 변경으로 회복 불가능한 손해가 예상될 때",
            "culturalNote": "한국에서는 부동산 거래 분쟁 시 처분금지 가처분이 매우 효과적으로 활용되며, 등기부에 즉시 등재되어 제3자에게도 대항할 수 있습니다. 베트남도 유사 제도가 있지만 집행력이 한국보다 약합니다. 한국에서는 노동 분쟁에서 '임시의 지위를 정하는 가처분'으로 해고 무효 확인 전에 임금을 받을 수 있지만, 베트남은 이런 신속한 구제가 어렵습니다. 한국 기업이 베트남에서 상표권 침해 대응 시 가처분 절차를 이해하지 못해 대응이 늦어지는 경우가 많으므로, 통역 시 양국 제도 차이를 설명해야 합니다.",
            "commonMistakes": [
                {
                    "mistake": "가처분을 가압류와 동일하게 번역",
                    "correction": "가압류는 kê biên tạm thời, 가처분은 biện pháp khẩn cấp tạm thời",
                    "explanation": "가압류는 금전채권, 가처분은 비금전적 권리로 적용 대상이 다름"
                },
                {
                    "mistake": "가처분을 '중재'(hòa giải)로 오역",
                    "correction": "법원의 강제력 있는 결정임을 명시",
                    "explanation": "가처분은 법원 명령이지 당사자 간 합의가 아님"
                },
                {
                    "mistake": "가처분 위반 시 처벌 없다고 설명",
                    "correction": "간접강제금 및 형사처벌 가능성을 명시: 'có thể bị phạt chấp hành gián tiếp và xử lý hình sự'",
                    "explanation": "가처분 위반은 법원 모욕죄로 처벌 가능"
                }
            ],
            "examples": [
                {
                    "ko": "부동산이 제3자에게 처분되는 것을 막기 위해 처분금지 가처분을 신청했습니다.",
                    "vi": "Để ngăn bất động sản bị chuyển nhượng cho bên thứ ba, tôi đã nộp đơn xin biện pháp cấm định đoạt tạm thời.",
                    "situation": "formal"
                },
                {
                    "ko": "부당해고에 대해 임시의 지위를 정하는 가처분으로 임금을 계속 받고 있습니다.",
                    "vi": "Đối với việc sa thải bất hợp lý, tôi vẫn nhận lương nhờ biện pháp xác định địa vị tạm thời.",
                    "situation": "onsite"
                },
                {
                    "ko": "가처분 명령을 위반하면 형사처벌을 받을 수 있습니다.",
                    "vi": "Nếu vi phạm lệnh biện pháp khẩn cấp tạm thời, có thể bị xử lý hình sự.",
                    "situation": "formal"
                }
            ],
            "relatedTerms": ["가압류", "담보제공", "처분금지", "임시의 지위"]
        },
        {
            "slug": "dau-gia",
            "korean": "경매",
            "vietnamese": "Đấu giá",
            "hanja": "競賣",
            "hanjaReading": "競(다툴 경) + 賣(팔 매)",
            "pronunciation": "다우 자",
            "meaningKo": "법원이 압류한 재산을 공개 입찰 방식으로 매각하여 채권자에게 배당하는 강제집행 절차입니다. 통역 시 한국의 경매는 법원 주도로 투명하게 진행되며, 인터넷으로 물건 정보를 공개하고, 낙찰자 선정이 공정하다는 점을 강조해야 합니다. 한국에서는 부동산 경매가 매우 활성화되어 있으며, 일반인도 투자 목적으로 참여할 수 있습니다. 경매는 최저가격(감정가의 80% 등)부터 시작하며, 유찰 시 가격을 낮춰 재경매합니다. 낙찰 후 잔금 납부하면 소유권이 이전되며, 기존 임차인이나 근저당권 등의 권리관계가 소멸되거나 인수되는 차이를 설명해야 합니다.",
            "meaningVi": "Thủ tục cưỡng chế thi hành mà tòa án bán đấu giá công khai tài sản đã bị áp lưu để phân chia cho các chủ nợ. Ở Hàn Quốc, đấu giá bất động sản được công khai trên internet, tiến hành công bằng và minh bạch, nhiều người tham gia với mục đích đầu tư. Sau khi trúng đấu giá và thanh toán đủ, quyền sở hữu được chuyển giao, và một số quyền liên quan như thế chấp sẽ bị xóa hoặc được kế thừa.",
            "context": "강제집행 절차에서 압류 재산을 현금화하는 단계",
            "culturalNote": "한국의 부동산 경매 시장은 매우 활성화되어 일반인도 대법원 경매정보 사이트를 통해 쉽게 참여할 수 있으며, 경매 물건이 투명하게 공개됩니다. 베트남은 경매 시스템이 덜 발달했고, 정보 접근성이 낮아 일반인 참여가 어렵습니다. 한국에서는 경매를 통한 부동산 투자가 하나의 재테크 수단으로 자리잡았지만, 베트남에서는 주로 채권 회수 목적으로만 사용됩니다. 한국의 경매는 법원 주도로 엄격하게 진행되어 사기 위험이 낮지만, 베트남은 절차상 투명성이 상대적으로 부족합니다. 통역 시 경매의 신뢰성과 안전성에 대한 인식 차이를 고려해야 합니다.",
            "commonMistakes": [
                {
                    "mistake": "경매를 '일반 매각'(bán thông thường)으로 번역",
                    "correction": "đấu giá 또는 bán đấu giá",
                    "explanation": "경매는 공개 입찰 방식의 특수한 매각이므로 구분 필요"
                },
                {
                    "mistake": "낙찰 즉시 소유권 이전된다고 설명",
                    "correction": "잔금 납부 후 소유권 이전: 'chuyển quyền sở hữu sau khi thanh toán đủ'",
                    "explanation": "낙찰은 계약일 뿐이고, 대금 완납 후에야 소유권 이전"
                },
                {
                    "mistake": "권리관계를 모두 승계한다고 잘못 설명",
                    "correction": "선순위 권리는 인수, 후순위는 소멸한다고 구체적으로 설명",
                    "explanation": "경매로 인한 권리 소멸과 인수는 순위에 따라 다름"
                }
            ],
            "examples": [
                {
                    "ko": "채무자 부동산에 대한 경매 절차가 진행 중이며, 다음 달 입찰이 예정되어 있습니다.",
                    "vi": "Thủ tục đấu giá bất động sản của con nợ đang được tiến hành, dự kiến đấu thầu vào tháng sau.",
                    "situation": "formal"
                },
                {
                    "ko": "경매로 낙찰받은 아파트는 기존 임차인이 있어도 인도명령으로 비울 수 있습니다.",
                    "vi": "Căn hộ trúng đấu giá có thể được trống bằng lệnh giao nộp ngay cả khi có người thuê cũ.",
                    "situation": "onsite"
                },
                {
                    "ko": "경매가 세 번 유찰되면 채권자가 직접 매수신청할 수 있습니다.",
                    "vi": "Nếu đấu giá thất bại ba lần, chủ nợ có thể nộp đơn mua trực tiếp.",
                    "situation": "formal"
                }
            ],
            "relatedTerms": ["압류", "배당", "낙찰", "유찰"]
        },
        {
            "slug": "boi-dang",
            "korean": "배당",
            "vietnamese": "Bồi đắp",
            "hanja": "配當",
            "hanjaReading": "配(나눌 배) + 當(마땅 당)",
            "pronunciation": "보이 덥",
            "meaningKo": "경매나 환가 절차를 통해 채무자 재산을 매각한 대금을 각 채권자에게 법정 순위에 따라 분배하는 절차입니다. 통역 시 배당은 단순 분배가 아니라 엄격한 법정 순위에 따른 분배임을 명확히 해야 합니다. 한국에서는 조세채권, 임금채권 등이 최우선 배당되고, 담보권자는 우선 배당, 일반 채권자는 안분 배당받습니다. 배당표 작성 후 이의 제기 기간이 있으며, 이의가 없으면 확정되어 실제 배당이 이루어집니다. 배당에서 제외되거나 소액만 받는 채권자가 많으므로, 채권 회수 가능성을 사전에 평가하는 것이 중요합니다.",
            "meaningVi": "Thủ tục phân chia tiền bán tài sản con nợ qua đấu giá cho các chủ nợ theo thứ tự ưu tiên pháp luật. Ở Hàn Quốc, các khoản nợ thuế, lương được ưu tiên hàng đầu, sau đó đến chủ nợ có bảo đảm, cuối cùng là chủ nợ thông thường chia đều. Sau khi lập bảng phân chia, có thời gian để khiếu nại, nếu không có khiếu nại thì bảng được xác định và tiến hành phân chia thực tế.",
            "context": "경매 매각대금을 여러 채권자에게 순위대로 분배하는 단계",
            "culturalNote": "한국의 배당 제도는 명확한 법정 순위가 확립되어 예측 가능성이 높습니다. 특히 근로자의 임금채권이 최우선 배당되는 점이 특징이며, 소액 임차인도 보증금을 우선 배당받을 수 있습니다. 베트남도 유사한 우선순위 제도가 있지만, 실제 집행에서 한국만큼 엄격하지 않아 분쟁이 많습니다. 한국에서는 배당표에 대한 이의 제기와 배당 이의의 소 제도가 발달해 있어 채권자 보호가 두텁지만, 베트남은 이러한 구제 수단이 제한적입니다. 통역 시 배당 순위와 이의 절차를 정확히 전달해야 합니다.",
            "commonMistakes": [
                {
                    "mistake": "배당을 '균등 분배'(chia đều)로 오해",
                    "correction": "법정 우선순위에 따른 분배: 'phân chia theo thứ tự ưu tiên pháp luật'",
                    "explanation": "배당은 순위에 따라 차등 분배되므로 균등 분배가 아님"
                },
                {
                    "mistake": "모든 채권자가 돈을 받는다고 설명",
                    "correction": "선순위 채권자가 우선이며, 매각대금 부족 시 후순위는 못 받을 수 있음을 명시",
                    "explanation": "배당액이 부족하면 후순위 채권자는 배당을 못 받을 수 있음"
                },
                {
                    "mistake": "배당표 확정 후 이의 제기 불가능하다고 설명",
                    "correction": "배당기일 전까지는 이의 제기 가능, 확정 후에도 배당이의의 소 가능",
                    "explanation": "배당 절차는 이의 제기 및 소송 가능성이 있음"
                }
            ],
            "examples": [
                {
                    "ko": "경매 대금 3억 원이 배당되었지만, 선순위 채권이 많아 후순위 채권자는 배당을 받지 못했습니다.",
                    "vi": "300 triệu won tiền đấu giá đã được phân chia, nhưng do nợ ưu tiên nhiều nên chủ nợ thứ cấp không nhận được phân chia.",
                    "situation": "formal"
                },
                {
                    "ko": "배당표에 이의가 있으면 배당기일 전까지 신청해야 합니다.",
                    "vi": "Nếu có khiếu nại về bảng phân chia, phải nộp đơn trước ngày phân chia.",
                    "situation": "onsite"
                },
                {
                    "ko": "임금채권자는 최우선 배당을 받을 수 있습니다.",
                    "vi": "Người có quyền đòi lương được nhận phân chia ưu tiên hàng đầu.",
                    "situation": "formal"
                }
            ],
            "relatedTerms": ["경매", "우선순위", "배당표", "배당이의"]
        },
        {
            "slug": "chae-gwon-chu-sim",
            "korean": "채권추심",
            "vietnamese": "Đòi nợ",
            "hanja": "債權追尋",
            "hanjaReading": "債(빚 채) + 權(권리 권) + 追(쫓을 추) + 尋(찾을 심)",
            "pronunciation": "도이 너",
            "meaningKo": "채권자가 채무자에게 채무 이행을 청구하고 변제받는 활동으로, 법적 절차뿐 아니라 임의 변제 유도도 포함됩니다. 통역 시 한국에서는 '채권추심'이 법적으로 규제되는 정당한 행위임을 강조해야 합니다. 채권추심업은 별도 법률(채권의 공정한 추심에 관한 법률)로 규제되며, 폭력, 협박, 허위 사실 유포 등은 불법입니다. 채권추심은 본인 채권 추심과 위임 추심으로 나뉘며, 전문 추심업체는 금융위원회 등록이 필요합니다. 베트남어로는 'đòi nợ'가 일반적이지만, 부정적 뉘앙스가 있어 'thu hồi nợ'(채권 회수)가 더 중립적입니다.",
            "meaningVi": "Hoạt động mà chủ nợ yêu cầu con nợ thực hiện nghĩa vụ và nhận thanh toán, bao gồm cả thủ tục pháp lý và thuyết phục tự nguyện thanh toán. Ở Hàn Quốc, đòi nợ được pháp luật điều chỉnh nghiêm ngặt (Luật về đòi nợ công bằng), cấm bạo lực, đe dọa, vu khống. Công ty đòi nợ chuyên nghiệp phải đăng ký với Ủy ban Dịch vụ Tài chính.",
            "context": "채권자가 소송 전후로 채무 변제를 요구하는 활동",
            "culturalNote": "한국에서는 채권추심업이 법으로 엄격히 규제되어, 불법 추심(일명 '사채업자' 스타일)은 형사처벌 대상입니다. 반면 베트남에서는 채권추심 규제가 상대적으로 느슨하여 폭력적 추심이 여전히 문제가 됩니다. 한국은 채권추심 시 야간 방문 금지, 반복 연락 제한 등 채무자 보호 규정이 강하지만, 베트남은 이런 보호가 약합니다. 한국의 금융기관들은 연체 채권을 전문 추심업체에 위탁하지만, 베트남은 아직 추심 산업이 덜 발달했습니다. 통역 시 한국의 '합법적 추심'과 '불법 사채'를 명확히 구분해 설명해야 오해를 막을 수 있습니다.",
            "commonMistakes": [
                {
                    "mistake": "채권추심을 'đòi nợ bất hợp pháp'(불법 추심)로 번역",
                    "correction": "thu hồi nợ 또는 đòi nợ hợp pháp (합법적 추심 명시)",
                    "explanation": "채권추심 자체는 합법 행위이므로 불법으로 오해하지 않도록 주의"
                },
                {
                    "mistake": "추심업체를 '사채업자'(cho vay nặng lãi)로 번역",
                    "correction": "công ty thu hồi nợ (등록된 합법 추심업체)",
                    "explanation": "정식 추심업체는 금융당국 등록을 받은 합법 기업"
                },
                {
                    "mistake": "추심 행위에 제한이 없다고 설명",
                    "correction": "야간 방문 금지, 폭력·협박 금지 등 법적 제한 명시",
                    "explanation": "한국은 채권추심법으로 엄격히 규제됨"
                }
            ],
            "examples": [
                {
                    "ko": "은행이 연체 채권을 전문 추심업체에 위탁했습니다.",
                    "vi": "Ngân hàng đã ủy thác khoản nợ quá hạn cho công ty thu hồi nợ chuyên nghiệp.",
                    "situation": "formal"
                },
                {
                    "ko": "채권추심 과정에서 폭력이나 협박을 당했다면 경찰에 신고할 수 있습니다.",
                    "vi": "Nếu bị bạo lực hoặc đe dọa trong quá trình đòi nợ, bạn có thể báo cảnh sát.",
                    "situation": "onsite"
                },
                {
                    "ko": "채권추심업체는 야간에 방문하거나 반복해서 전화할 수 없습니다.",
                    "vi": "Công ty thu hồi nợ không được phép thăm vào ban đêm hoặc gọi điện liên tục.",
                    "situation": "formal"
                }
            ],
            "relatedTerms": ["채권회수", "독촉", "지급명령", "소송"]
        },
        {
            "slug": "tap-hanh-gwon-won",
            "korean": "집행권원",
            "vietnamese": "Căn cứ thi hành",
            "hanja": "執行權原",
            "hanjaReading": "執(잡을 집) + 行(다닐 행) + 權(권리 권) + 原(근원 원)",
            "pronunciation": "껀 꾸 티 항",
            "meaningKo": "강제집행을 할 수 있는 법적 근거가 되는 공적 문서로, 확정판결, 집행증서, 조정조서 등이 해당합니다. 통역 시 집행권원이 없으면 아무리 빚이 명백해도 강제집행을 할 수 없다는 점을 강조해야 합니다. 한국에서는 판결문에 '집행문'을 부여받아야 집행 가능하며, 일부 집행권원(공정증서 등)은 소송 없이도 집행할 수 있습니다. 집행권원의 종류에 따라 집행력의 범위와 방법이 달라지므로, 어떤 집행권원을 확보했는지가 채권 회수에 결정적입니다. 베트남어로는 'văn bản có thể thi hành'이라고도 하지만, 'căn cứ thi hành'이 더 정확합니다.",
            "meaningVi": "Văn bản công có giá trị pháp lý làm căn cứ để cưỡng chế thi hành, bao gồm bản án có hiệu lực, văn bản thừa hành công chứng, biên bản hòa giải. Không có căn cứ thi hành thì không thể cưỡng chế dù nợ rõ ràng. Ở Hàn Quốc, bản án phải được cấp 'văn bản thi hành' (執行文) mới có thể thi hành, một số văn bản như công chứng có thể thi hành mà không cần kiện.",
            "context": "강제집행 신청의 전제 조건",
            "culturalNote": "한국에서는 집행권원 제도가 명확히 확립되어, 사인 간 차용증만으로는 강제집행이 불가능하고 반드시 법원 판결이나 공증을 받아야 합니다. 베트남도 유사하지만, 실무에서는 공증 문서의 집행력이 한국보다 약합니다. 한국은 조정조서나 화해권고결정도 집행권원이 되어 소송 없이 신속히 집행 가능하지만, 베트남은 이런 간이 절차가 덜 발달했습니다. 한국에서는 외국 판결도 승인 절차를 거쳐 집행권원이 될 수 있지만, 베트남과 한국 간에는 상호 승인 조약이 없어 외국 판결 집행이 어렵습니다. 통역 시 양국 간 판결 집행의 한계를 설명해야 합니다.",
            "commonMistakes": [
                {
                    "mistake": "차용증이나 계약서를 집행권원으로 오해",
                    "correction": "법원 판결, 공증 등 공적 문서만 집행권원임을 명시",
                    "explanation": "사인 간 문서는 증거일 뿐 집행권원이 아님"
                },
                {
                    "mistake": "판결문 자체로 바로 집행 가능하다고 설명",
                    "correction": "판결문에 집행문 부여받아야 집행 가능: 'phải được cấp văn bản thi hành'",
                    "explanation": "판결 확정 후 집행문 신청·부여 절차가 필요"
                },
                {
                    "mistake": "베트남 판결을 한국에서 바로 집행 가능하다고 설명",
                    "correction": "외국 판결은 승인 절차 필요, 한-베 간 상호 승인 조약 없음을 명시",
                    "explanation": "외국 판결은 별도 승인 절차를 거쳐야 하며, 한-베 간에는 조약이 없어 어려움"
                }
            ],
            "examples": [
                {
                    "ko": "판결이 확정되었으니 집행문을 부여받아 강제집행을 신청하겠습니다.",
                    "vi": "Bản án đã có hiệu lực, tôi sẽ xin cấp văn bản thi hành và nộp đơn cưỡng chế.",
                    "situation": "formal"
                },
                {
                    "ko": "공증받은 금전소비대차 계약서는 판결 없이도 집행권원이 됩니다.",
                    "vi": "Hợp đồng vay tiền đã công chứng trở thành căn cứ thi hành mà không cần bản án.",
                    "situation": "onsite"
                },
                {
                    "ko": "집행권원 없이는 아무리 빚이 확실해도 강제집행을 할 수 없습니다.",
                    "vi": "Không có căn cứ thi hành thì không thể cưỡng chế dù nợ rất rõ ràng.",
                    "situation": "formal"
                }
            ],
            "relatedTerms": ["강제집행", "집행문", "확정판결", "공정증서"]
        },
        {
            "slug": "tap-hanh-i-ui",
            "korean": "집행이의",
            "vietnamese": "Khiếu nại thi hành",
            "hanja": "執行異議",
            "hanjaReading": "執(잡을 집) + 行(다닐 행) + 異(다를 이) + 議(의논할 의)",
            "pronunciation": "키에우 나이 티 항",
            "meaningKo": "강제집행 절차나 방법이 부당하다고 주장하며 집행 정지 또는 취소를 구하는 채무자의 불복 수단입니다. 통역 시 집행이의는 집행의 적법성(절차)만 다투는 것이고, 판결 내용 자체는 다투지 못한다는 점을 명확히 해야 합니다. 한국에서는 집행이의 신청 시 법원이 집행정지 결정을 할 수 있으며, 채무자가 담보를 제공하면 집행을 일시 중단할 수 있습니다. 집행이의는 청구이의의 소(판결 내용 다툼)와 구별되므로, 무엇을 다투느냐에 따라 적절한 절차를 선택해야 합니다. 베트남어로는 'khiếu nại' 또는 'khiếu kiện'을 쓸 수 있지만, 맥락에 따라 구분해야 합니다.",
            "meaningVi": "Phương thức con nợ phản đối khi cho rằng thủ tục hoặc phương pháp cưỡng chế thi hành không hợp lý, yêu cầu đình chỉ hoặc hủy bỏ việc thi hành. Khiếu nại thi hành chỉ tranh chấp tính hợp pháp của việc thi hành (thủ tục), không tranh chấp nội dung bản án. Tòa án có thể quyết định đình chỉ thi hành, con nợ có thể tạm dừng thi hành nếu nộp bảo lãnh.",
            "context": "강제집행이 위법·부당하게 진행될 때 채무자의 구제 수단",
            "culturalNote": "한국에서는 집행이의 제도가 잘 발달되어, 집행 절차에 하자가 있으면 채무자가 신속히 구제받을 수 있습니다. 채무자는 집행이의와 동시에 집행정지 신청을 할 수 있어 실질적 보호를 받습니다. 베트남도 유사 제도가 있지만, 집행 정지가 한국만큼 쉽게 인정되지 않아 채무자 보호가 약합니다. 한국에서는 집행이의가 기각되면 즉시항고로 불복할 수 있어 다단계 구제가 가능하지만, 베트남은 이런 절차가 제한적입니다. 통역 시 집행이의(절차 하자)와 청구이의의 소(판결 내용 다툼)를 혼동하지 않도록 주의해야 합니다.",
            "commonMistakes": [
                {
                    "mistake": "집행이의로 판결 내용을 다툴 수 있다고 설명",
                    "correction": "집행이의는 절차만, 판결 내용은 청구이의의 소로 다퉈야 함",
                    "explanation": "집행이의는 집행의 적법성만 다루고, 실체 판단은 하지 않음"
                },
                {
                    "mistake": "집행이의 신청으로 집행이 자동 정지된다고 설명",
                    "correction": "집행정지는 별도 신청 필요, 법원 재량으로 결정됨",
                    "explanation": "집행이의 신청 자체로는 집행이 중단되지 않음"
                },
                {
                    "mistake": "집행이의를 'phản đối bản án'(판결 반대)로 번역",
                    "correction": "khiếu nại thi hành (절차에 대한 이의)",
                    "explanation": "판결 자체가 아니라 집행 절차를 문제 삼는 것"
                }
            ],
            "examples": [
                {
                    "ko": "집행관이 압류 금지 재산을 압류하여 집행이의를 신청했습니다.",
                    "vi": "Chấp hành viên đã áp lưu tài sản cấm áp lưu nên tôi đã nộp đơn khiếu nại thi hành.",
                    "situation": "formal"
                },
                {
                    "ko": "집행이의와 함께 집행정지 신청을 했고, 법원이 담보 제공 조건으로 정지 결정을 내렸습니다.",
                    "vi": "Tôi đã nộp khiếu nại thi hành cùng với đơn xin đình chỉ, tòa quyết định đình chỉ với điều kiện nộp bảo lãnh.",
                    "situation": "onsite"
                },
                {
                    "ko": "집행이의가 기각되면 즉시항고로 불복할 수 있습니다.",
                    "vi": "Nếu khiếu nại thi hành bị bác, có thể kháng cáo tức thời.",
                    "situation": "formal"
                }
            ],
            "relatedTerms": ["강제집행", "집행정지", "청구이의의 소", "담보제공"]
        },
        {
            "slug": "jae-san-myeong-si",
            "korean": "재산명시",
            "vietnamese": "Khai báo tài sản",
            "hanja": "財產明示",
            "hanjaReading": "財(재물 재) + 産(낳을 산) + 明(밝을 명) + 示(보일 시)",
            "pronunciation": "카이 바오 따이 산",
            "meaningKo": "강제집행이 불가능하거나 불충분할 때 채무자가 법원에 자신의 전체 재산 상황을 신고하도록 하는 제도입니다. 통역 시 재산명시는 채무자의 의무이며, 불이행 시 감치(유치)나 과태료 등 제재가 따른다는 점을 강조해야 합니다. 한국에서는 재산명시 신청 후 채무자가 정당한 사유 없이 불출석하거나 거짓 진술하면 감치(20일 이내 유치)될 수 있습니다. 재산명시를 통해 채권자는 채무자의 숨겨진 재산을 찾아낼 수 있으며, 이를 근거로 재산조회나 추가 압류를 진행할 수 있습니다. 베트남어로는 'công bố tài sản'보다 'khai báo tài sản'이 더 정확합니다.",
            "meaningVi": "Chế độ buộc con nợ phải khai báo tình hình tài sản toàn bộ cho tòa án khi cưỡng chế thi hành không thể thực hiện hoặc không đủ. Đây là nghĩa vụ của con nợ, nếu không thực hiện sẽ bị chế tài như giam giữ (lưu trí) hoặc phạt tiền. Ở Hàn Quốc, nếu con nợ không đến hoặc khai sai không có lý do chính đáng, có thể bị giam giữ đến 20 ngày. Chủ nợ có thể dựa vào thông tin này để điều tra tài sản hoặc áp lưu bổ sung.",
            "context": "집행불능 상태에서 채무자 재산을 파악하기 위한 절차",
            "culturalNote": "한국에서는 재산명시 제도가 채무자의 재산 은닉을 막는 효과적인 수단으로 활용되며, 법원 출석 의무와 진실 진술 의무가 엄격합니다. 불이행 시 감치라는 강력한 제재가 있어 실효성이 높습니다. 베트남에도 유사한 재산 신고 의무가 있지만, 한국만큼 엄격히 집행되지 않고 제재도 약합니다. 한국에서는 재산명시 후 재산조회 신청으로 국세청, 금융기관 등에 조회할 수 있지만, 베트남은 이런 조회 시스템이 덜 발달했습니다. 한국의 감치 제도는 베트남에 없는 강력한 강제 수단이므로, 통역 시 이를 명확히 설명해야 합니다.",
            "commonMistakes": [
                {
                    "mistake": "재산명시를 자발적 신고로 오해",
                    "correction": "법원 명령에 따른 강제적 의무임을 명시: 'nghĩa vụ cưỡng bức theo lệnh tòa'",
                    "explanation": "재산명시는 법원 결정에 따른 의무이지 자발적 신고가 아님"
                },
                {
                    "mistake": "불이행 시 제재가 없다고 설명",
                    "correction": "감치(lưu trí, giam giữ)와 과태료 부과를 명시",
                    "explanation": "정당한 사유 없는 불이행은 감치 등 형사적 제재 대상"
                },
                {
                    "mistake": "재산명시만으로 집행이 된다고 오해",
                    "correction": "재산명시는 정보 파악 단계, 이후 재산조회·압류 등 추가 절차 필요",
                    "explanation": "재산명시는 집행 준비 단계이지 집행 자체가 아님"
                }
            ],
            "examples": [
                {
                    "ko": "집행불능으로 재산명시 신청을 했고, 법원이 채무자에게 출석 명령을 내렸습니다.",
                    "vi": "Do không thể thi hành, tôi đã nộp đơn xin khai báo tài sản và tòa đã ra lệnh cho con nợ đến.",
                    "situation": "formal"
                },
                {
                    "ko": "채무자가 재산명시 기일에 출석하지 않아 감치 신청을 했습니다.",
                    "vi": "Con nợ không đến vào ngày khai báo tài sản nên tôi đã nộp đơn xin lưu trí.",
                    "situation": "onsite"
                },
                {
                    "ko": "재산명시를 통해 채무자의 숨겨진 예금 계좌를 발견하여 압류했습니다.",
                    "vi": "Qua khai báo tài sản, tôi đã phát hiện tài khoản tiền gửi bị giấu của con nợ và áp lưu.",
                    "situation": "formal"
                }
            ],
            "relatedTerms": ["강제집행", "집행불능", "감치", "재산조회"]
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
