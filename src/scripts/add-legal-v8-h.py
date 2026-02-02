#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
증권/자본시장법 용어 추가 스크립트 (legal-v8-h)
테마: 내부자거래, 시세조종, 공시의무, IPO, M&A, 주주대표소송, 의결권, 집합투자, 파생상품, 금융투자업
"""

import json
import os

# 추가할 용어 데이터
new_terms = [
    {
        "slug": "giao-dich-noi-bo",
        "korean": "내부자거래",
        "vietnamese": "Giao dịch nội bộ",
        "hanja": "內部者去來",
        "hanjaReading": "內(안 내) + 部(부분 부) + 者(놈 자) + 去(갈 거) + 來(올 래)",
        "pronunciation": "네부자거래",
        "meaningKo": "회사의 임직원이나 주요 주주 등이 직무상 알게 된 미공개 중요정보를 이용하여 주식 등을 매매하는 불공정거래 행위를 의미합니다. 자본시장법에서 엄격히 금지하며, 통역 시 '부당한 이익 취득 목적'과 '정보의 중요성·비공개성' 두 요소를 명확히 구분해야 합니다. 베트남에서는 'giao dịch nội gián'으로 혼동될 수 있으나, 'nội bộ'는 '내부자', 'nội gián'은 '내부 스파이'를 뜻하므로 주의가 필요합니다.",
        "meaningVi": "Hành vi giao dịch chứng khoán bất hợp pháp khi người nội bộ công ty (임원, ban giám đốc) sử dụng thông tin trọng yếu chưa được công bố để mua bán cổ phiếu nhằm thu lợi bất chính. Đây là hành vi bị nghiêm cấm trong luật thị trường vốn Hàn Quốc.",
        "context": "증권거래소 조사, 금융감독원 제재, 자본시장법 위반 사건",
        "culturalNote": "한국은 내부자거래 처벌이 매우 엄격하여 징역형과 과징금이 함께 부과되며, 미국 SEC 수준의 강력한 규제를 시행합니다. 베트남은 증권시장 역사가 짧아 내부자거래 처벌 사례가 적고, 입증 기준도 상대적으로 느슨합니다. 통역 시 한국의 '미공개 중요정보' 개념을 'thông tin trọng yếu chưa công bố'로 정확히 전달해야 합니다.",
        "commonMistakes": [
            {
                "mistake": "giao dịch nội gián",
                "correction": "giao dịch nội bộ",
                "explanation": "'nội gián'은 스파이를 뜻하며, 내부자거래는 'nội bộ'(내부자)를 사용해야 함"
            },
            {
                "mistake": "thông tin bí mật",
                "correction": "thông tin chưa công bố / thông tin nội bộ",
                "explanation": "'비밀정보'가 아니라 '미공개정보'이므로 'chưa công bố'가 정확함"
            },
            {
                "mistake": "người trong công ty",
                "correction": "người nội bộ / nội gián viên",
                "explanation": "법률 용어로는 'người nội bộ'가 공식 표현임"
            }
        ],
        "examples": [
            {
                "ko": "피고인은 합병 발표 전 내부정보를 이용해 주식 5만 주를 매수한 혐의로 기소되었습니다.",
                "vi": "Bị cáo bị truy tố với cáo buộc đã mua 50.000 cổ phiếu bằng cách sử dụng thông tin nội bộ trước khi công bố sáp nhập.",
                "situation": "formal"
            },
            {
                "ko": "내부자거래 혐의가 인정되면 부당이득의 3배까지 과징금이 부과됩니다.",
                "vi": "Nếu bị kết tội giao dịch nội bộ, có thể bị phạt tiền lên đến gấp 3 lần số tiền thu lợi bất chính.",
                "situation": "formal"
            },
            {
                "ko": "이 사건은 전형적인 내부자거래 유형으로, CFO가 실적 발표 전에 주식을 처분했습니다.",
                "vi": "Đây là trường hợp điển hình về giao dịch nội bộ, khi CFO đã bán cổ phiếu trước khi công bố kết quả kinh doanh.",
                "situation": "formal"
            }
        ],
        "relatedTerms": ["시세조종", "불공정거래", "미공개정보", "자본시장법"]
    },
    {
        "slug": "조-tac-gia",
        "korean": "시세조종",
        "vietnamese": "Thao túng giá / Điều khiển thị giá",
        "hanja": "時勢操縱",
        "hanjaReading": "時(때 시) + 勢(형세 세) + 操(잡을 조) + 縱(세로 종)",
        "pronunciation": "시세조종",
        "meaningKo": "인위적으로 주가나 거래량을 조작하여 다른 투자자를 속이고 부당한 이익을 얻는 불공정거래 행위입니다. 허위 주문, 가장 매매, 시세 고정 등 다양한 수법이 있으며, 자본시장법상 형사처벌 대상입니다. 통역 시 '인위적 조작'과 '투자자 기망' 두 요소를 강조해야 하며, 베트남어로 'thao túng'(조종) 또는 'điều khiển'(컨트롤) 모두 사용 가능하나, 법률 문서에서는 'thao túng giá'가 더 공식적입니다.",
        "meaningVi": "Hành vi bất hợp pháp nhằm tác động giả tạo vào giá cổ phiếu hoặc khối lượng giao dịch để lừa gạt nhà đầu tư khác và thu lợi bất chính. Các thủ đoạn bao gồm đặt lệnh ảo, giao dịch khống, cố định giá. Bị truy cứu hình sự theo luật thị trường vốn Hàn Quốc.",
        "context": "증권범죄 수사, 금융감독원 제재, 집단소송",
        "culturalNote": "한국은 시세조종에 대한 처벌이 매우 강력하며, 최근 'VIP 리딩방' 등 SNS를 통한 시세조종이 사회문제로 대두되고 있습니다. 베트nam은 개인투자자 비중이 높아 시세조종이 빈번하나, 감독 역량 부족으로 적발이 어렵습니다. 통역 시 한국의 '가장매매', '허수주문' 등 구체적 수법을 베트남어로 정확히 설명하는 것이 중요합니다.",
        "commonMistakes": [
            {
                "mistake": "điều khiển thị trường",
                "correction": "thao túng giá / thao túng thị giá",
                "explanation": "'시장 조종'이 아니라 '시세(가격) 조종'이므로 'giá'를 명시해야 함"
            },
            {
                "mistake": "gian lận giá cả",
                "correction": "thao túng giá",
                "explanation": "'가격 사기'가 아니라 법률 용어인 '시세조종'으로 표현해야 함"
            },
            {
                "mistake": "lừa đảo chứng khoán",
                "correction": "thao túng giá chứng khoán",
                "explanation": "일반 '증권사기'와 구분하여 '시세조종'이라는 특정 범죄로 표현해야 함"
            }
        ],
        "examples": [
            {
                "ko": "피고인은 허수 매수주문을 반복적으로 제출하여 주가를 인위적으로 상승시킨 시세조종 혐의를 받고 있습니다.",
                "vi": "Bị cáo bị cáo buộc thao túng giá bằng cách liên tục đặt lệnh mua ảo để đẩy giá cổ phiếu lên một cách giả tạo.",
                "situation": "formal"
            },
            {
                "ko": "금감원은 이 종목에 대한 시세조종 의혹을 포착하고 조사에 착수했습니다.",
                "vi": "Ủy ban giám sát tài chính đã phát hiện nghi vấn thao túng giá đối với cổ phiếu này và bắt đầu điều tra.",
                "situation": "formal"
            },
            {
                "ko": "시세조종으로 얻은 부당이득은 전액 환수되며, 징역형도 선고될 수 있습니다.",
                "vi": "Toàn bộ lợi nhuận bất chính từ thao túng giá sẽ bị tịch thu và có thể bị kết án tù.",
                "situation": "formal"
            }
        ],
        "relatedTerms": ["내부자거래", "불공정거래", "가장매매", "허수주문"]
    },
    {
        "slug": "nghia-vu-cong-bo",
        "korean": "공시의무",
        "vietnamese": "Nghĩa vụ công bố / Nghĩa vụ công khai thông tin",
        "hanja": "公示義務",
        "hanjaReading": "公(공평할 공) + 示(보일 시) + 義(옳을 의) + 務(힘쓸 무)",
        "pronunciation": "공시의무",
        "meaningKo": "상장회사가 투자자 보호를 위해 중요한 경영정보를 법정 기한 내에 공개해야 할 법적 의무를 말합니다. 정기공시(사업보고서, 분기보고서)와 수시공시(주요 경영사항 변동)로 구분되며, 위반 시 과징금과 임원 제재를 받습니다. 통역 시 '공시'는 단순 발표가 아니라 '법정 의무에 따른 공개'임을 강조해야 하며, 베트남어 'công bố'는 일반 발표, 'công khai thông tin'은 정보 공개를 뜻하므로 맥락에 따라 선택해야 합니다.",
        "meaningVi": "Nghĩa vụ pháp lý của công ty niêm yết phải công khai các thông tin kinh doanh quan trọng trong thời hạn quy định để bảo vệ nhà đầu tư. Bao gồm công bố định kỳ (báo cáo kinh doanh, báo cáo quý) và công bố bất thường (thay đổi sự kiện quan trọng). Vi phạm sẽ bị phạt tiền và xử lý cán bộ quản lý.",
        "context": "상장회사 IR, 증권신고서 제출, 금융감독원 공시",
        "culturalNote": "한국은 공시의무 위반에 대한 처벌이 엄격하여, 지연공시도 즉시 과징금 대상이 되며, 고의적 미공시는 형사처벌을 받습니다. 베트남은 공시 시스템이 발전 중이나, 시한 준수 의식이 약하고 사후 제재도 미약합니다. 통역 시 한국의 '적시공시' 개념을 'công bố kịp thời'로 정확히 전달해야 합니다.",
        "commonMistakes": [
            {
                "mistake": "nghĩa vụ thông báo",
                "correction": "nghĩa vụ công bố / nghĩa vụ công khai",
                "explanation": "'통지 의무'가 아니라 '공시(공개) 의무'이므로 'công bố/công khai' 사용"
            },
            {
                "mistake": "công bố tự nguyện",
                "correction": "nghĩa vụ công bố / công bố bắt buộc",
                "explanation": "'자발적 공시'가 아니라 '법적 의무'이므로 'bắt buộc' 강조 필요"
            },
            {
                "mistake": "báo cáo cho cổ đông",
                "correction": "công bố thông tin cho thị trường",
                "explanation": "주주보고가 아니라 시장 전체에 대한 공시임"
            }
        ],
        "examples": [
            {
                "ko": "당사는 자본시장법에 따라 합병 결정 사실을 즉시 공시할 의무가 있습니다.",
                "vi": "Công ty chúng tôi có nghĩa vụ công bố ngay lập tức về quyết định sáp nhập theo luật thị trường vốn.",
                "situation": "formal"
            },
            {
                "ko": "공시의무 위반으로 대표이사가 금융감독원으로부터 경고 조치를 받았습니다.",
                "vi": "Tổng giám đốc đã bị Ủy ban giám sát tài chính cảnh cáo do vi phạm nghĩa vụ công bố thông tin.",
                "situation": "formal"
            },
            {
                "ko": "분기보고서 제출이 지연되면 공시의무 위반으로 과징금이 부과됩니다.",
                "vi": "Nếu chậm nộp báo cáo quý, sẽ bị phạt tiền do vi phạm nghĩa vụ công bố.",
                "situation": "formal"
            }
        ],
        "relatedTerms": ["적시공시", "정기공시", "수시공시", "공정공시"]
    },
    {
        "slug": "niem-yet-lan-dau-ra-cong-chung",
        "korean": "기업공개",
        "vietnamese": "Niêm yết lần đầu ra công chúng (IPO)",
        "hanja": "企業公開",
        "hanjaReading": "企(꾀할 기) + 業(업 업) + 公(공평할 공) + 開(열 개)",
        "pronunciation": "기업공개",
        "meaningKo": "비상장 기업이 주식시장에 상장하여 일반 투자자에게 주식을 공개 매각하는 절차를 의미하며, 영어로는 IPO(Initial Public Offering)라고 합니다. 증권신고서 제출, 공모가 확정, 청약, 배정, 상장의 단계를 거치며, 통역 시 '공모'와 '상장'을 구분해야 합니다. 베트남어로는 'niêm yết lần đầu'가 정확하나, 실무에서는 영어 'IPO'를 그대로 사용하는 경우도 많습니다.",
        "meaningVi": "Quá trình công ty chưa niêm yết lên sàn chứng khoán và bán cổ phiếu cho công chúng lần đầu tiên, gọi tắt là IPO. Trải qua các giai đoạn: nộp hồ sơ đăng ký chứng khoán, xác định giá chào bán, đăng ký mua, phân bổ, niêm yết. Cần phân biệt giữa 'chào bán công khai' (공모) và 'niêm yết' (상장).",
        "context": "증권사 인수심사, 공모주 청약, 코스피/코스닥 상장",
        "culturalNote": "한국은 IPO 시 공모가 결정에 수요예측 제도를 활용하며, 기관투자자 중심으로 가격이 형성됩니다. 베트남은 IPO 규모가 작고, 정부 지분 매각(민영화) 형태의 IPO가 많습니다. 통역 시 한국의 '의무보유확약', '구주매출' 등 제도를 설명할 때 베트남과의 차이를 보충 설명해야 합니다.",
        "commonMistakes": [
            {
                "mistake": "lên sàn chứng khoán",
                "correction": "niêm yết lần đầu ra công chúng / IPO",
                "explanation": "'상장'만 뜻하는 게 아니라 '공모+상장' 전체 과정을 포괄함"
            },
            {
                "mistake": "bán cổ phiếu lần đầu",
                "correction": "chào bán công khai lần đầu / IPO",
                "explanation": "단순 판매가 아니라 공개시장을 통한 공모 절차임"
            },
            {
                "mistake": "công ty mở bán cổ phiếu",
                "correction": "công ty niêm yết / công ty IPO",
                "explanation": "'주식 판매'가 아니라 '기업공개'라는 공식 용어 사용 필요"
            }
        ],
        "examples": [
            {
                "ko": "이번 기업공개를 통해 1조 원 규모의 자금을 조달할 계획입니다.",
                "vi": "Thông qua IPO này, chúng tôi dự định huy động 1 nghìn tỷ won (khoảng 20 triệu USD).",
                "situation": "formal"
            },
            {
                "ko": "공모가는 수요예측 결과를 반영하여 주당 5만 원으로 확정되었습니다.",
                "vi": "Giá chào bán được xác định là 50.000 won/cổ phiếu dựa trên kết quả thăm dò nhu cầu.",
                "situation": "formal"
            },
            {
                "ko": "기업공개 후 상장 첫날 공모가 대비 50% 상승했습니다.",
                "vi": "Sau IPO, ngày đầu niêm yết giá tăng 50% so với giá chào bán.",
                "situation": "formal"
            }
        ],
        "relatedTerms": ["공모주", "수요예측", "상장", "증권신고서"]
    },
    {
        "slug": "sap-nhap-va-mua-lai",
        "korean": "인수합병",
        "vietnamese": "Sáp nhập và mua lại (M&A)",
        "hanja": "引受合倂",
        "hanjaReading": "引(끌 인) + 受(받을 수) + 合(합할 합) + 倂(아울러 병)",
        "pronunciation": "인수합병",
        "meaningKo": "기업 간 결합을 통해 사업을 확장하거나 시너지를 창출하는 거래로, 인수(M&A의 A, Acquisition)와 합병(M&A의 M, Merger)을 포괄합니다. 주식 취득, 영업양도, 합병 등 다양한 방식이 있으며, 통역 시 적대적/우호적 인수, 수평/수직 합병 등 유형을 구분해야 합니다. 베트남어로는 'M&A'를 그대로 사용하거나 'sáp nhập và mua lại'로 풀어서 표현합니다.",
        "meaningVi": "Giao dịch kết hợp doanh nghiệp để mở rộng kinh doanh hoặc tạo hiệu ứng cộng hưởng, bao gồm mua lại (Acquisition) và sáp nhập (Merger). Có nhiều hình thức như mua cổ phần, chuyển nhượng kinh doanh, sáp nhập. Cần phân biệt loại thù địch/hữu nghị, sáp nhập ngang/dọc.",
        "context": "기업 실사, 주식양수도 계약, 공정거래위원회 심사",
        "culturalNote": "한국은 대기업 총수 일가의 지배권 승계를 위한 M&A가 많으며, 공정거래법상 대규모 M&A는 사전 신고가 필수입니다. 베트남은 외국인 지분 제한이 있어 M&A 시 정부 승인 절차가 복잡하며, 국영기업 민영화 M&A가 빈번합니다. 통역 시 한국의 '경영권 프리미엄' 개념을 설명할 때 주의가 필요합니다.",
        "commonMistakes": [
            {
                "mistake": "mua và bán công ty",
                "correction": "sáp nhập và mua lại / M&A",
                "explanation": "'회사 매매'가 아니라 전략적 결합을 의미하는 M&A 용어 사용"
            },
            {
                "mistake": "hợp nhất doanh nghiệp",
                "correction": "sáp nhập (merger) / M&A",
                "explanation": "'통합'만이 아니라 인수+합병 전체를 포괄하는 용어 필요"
            },
            {
                "mistake": "thôn tính công ty",
                "correction": "mua lại / thâu tóm",
                "explanation": "'집어삼키다'는 부정적 뉘앙스이므로 중립적 표현 사용"
            }
        ],
        "examples": [
            {
                "ko": "A사는 B사를 3조 원에 인수하여 시장 점유율 1위를 달성했습니다.",
                "vi": "Công ty A đã mua lại công ty B với giá 3 nghìn tỷ won và đạt thị phần số 1.",
                "situation": "formal"
            },
            {
                "ko": "이번 합병은 공정거래위원회의 승인을 받아야 최종 완료됩니다.",
                "vi": "Vụ sáp nhập này cần được Ủy ban cạnh tranh công bằng phê duyệt mới hoàn tất.",
                "situation": "formal"
            },
            {
                "ko": "적대적 M&A를 막기 위해 우리사주조합이 백기사로 나섰습니다.",
                "vi": "Để ngăn chặn M&A thù địch, hiệp hội cổ đông nhân viên đã đóng vai 'hiệp sĩ áo trắng' (white knight).",
                "situation": "formal"
            }
        ],
        "relatedTerms": ["적대적인수", "실사", "경영권프리미엄", "공정거래법"]
    },
    {
        "slug": "kien-dai-dien-co-dong",
        "korean": "주주대표소송",
        "vietnamese": "Kiện đại diện cổ đông / Kiện thay mặt công ty",
        "hanja": "株主代表訴訟",
        "hanjaReading": "株(그루 주) + 主(주인 주) + 代(대신할 대) + 表(나타낼 표) + 訴(호소할 소) + 訟(송사 송)",
        "pronunciation": "주주대표소송",
        "meaningKo": "이사의 위법행위로 회사가 손해를 입었으나 회사가 직접 소송을 제기하지 않을 때, 주주가 회사를 대신하여 이사에게 손해배상을 청구하는 제도입니다. 6개월 이상 주식 보유 주주만 제기할 수 있으며, 통역 시 '대표소송'은 '집단소송(class action)'과 다른 개념임을 명확히 해야 합니다. 베트남어로는 'kiện đại diện'(대표 소송) 또는 'kiện thay mặt công ty'(회사 대신 소송)로 표현합니다.",
        "meaningVi": "Chế độ cho phép cổ đông kiện giám đốc thay mặt công ty khi giám đốc vi phạm pháp luật gây thiệt hại cho công ty nhưng công ty không tự khởi kiện. Chỉ cổ đông nắm giữ cổ phần trên 6 tháng mới được quyền khởi kiện. Cần phân biệt với 'kiện tập thể' (class action) - đây là khái niệm khác.",
        "context": "상법 소송, 이사 배임 사건, 지배구조 분쟁",
        "culturalNote": "한국은 주주대표소송 제도가 활성화되어 있으며, 소액주주운동 단체들이 적극적으로 활용합니다. 특히 재벌 총수의 배임·횡령 사건에서 자주 제기됩니다. 베트남은 주주대표소송 개념이 생소하며, 이사 책임 추궁이 실무적으로 어렵습니다. 통역 시 '간접 손해'와 '직접 손해'의 차이를 설명해야 합니다.",
        "commonMistakes": [
            {
                "mistake": "kiện tập thể cổ đông",
                "correction": "kiện đại diện cổ đông / kiện phái sinh",
                "explanation": "'집단소송'이 아니라 '대표소송'이므로 'đại diện' 사용"
            },
            {
                "mistake": "cổ đông kiện công ty",
                "correction": "cổ đông kiện giám đốc thay mặt công ty",
                "explanation": "회사를 고소하는 게 아니라 회사를 대신하여 임원을 고소하는 것임"
            },
            {
                "mistake": "kiện bồi thường cho cổ đông",
                "correction": "kiện bồi thường cho công ty",
                "explanation": "배상금은 주주가 아닌 회사가 받음"
            }
        ],
        "examples": [
            {
                "ko": "소액주주들이 대표이사의 배임행위에 대해 주주대표소송을 제기했습니다.",
                "vi": "Các cổ đông nhỏ đã khởi kiện đại diện cổ đông đối với hành vi phản bội tín nhiệm của tổng giám đốc.",
                "situation": "formal"
            },
            {
                "ko": "주주대표소송에서 승소하면 손해배상금은 회사에 귀속됩니다.",
                "vi": "Nếu thắng kiện đại diện cổ đông, tiền bồi thường sẽ thuộc về công ty.",
                "situation": "formal"
            },
            {
                "ko": "이사의 충실의무 위반을 이유로 주주대표소송이 계속 증가하고 있습니다.",
                "vi": "Số vụ kiện đại diện cổ đông ngày càng tăng do giám đốc vi phạm nghĩa vụ trung thành.",
                "situation": "formal"
            }
        ],
        "relatedTerms": ["소액주주권", "이사배임", "충실의무", "집단소송"]
    },
    {
        "slug": "quyen-bieu-quyet",
        "korean": "의결권",
        "vietnamese": "Quyền biểu quyết / Quyền bỏ phiếu",
        "hanja": "議決權",
        "hanjaReading": "議(의논할 의) + 決(결단할 결) + 權(권세 권)",
        "pronunciation": "의결권",
        "meaningKo": "주주총회에서 회사의 중요 사항을 결정할 때 주주가 행사하는 투표권을 의미합니다. 원칙적으로 1주 1의결권이며, 보통주는 의결권이 있고 우선주는 통상 의결권이 없습니다. 통역 시 '의결권 행사'와 '위임장 권유', '의결권 제한' 등 관련 개념을 함께 설명해야 하며, 베트남어로는 'quyền biểu quyết'(표결권) 또는 'quyền bỏ phiếu'(투표권)를 사용합니다.",
        "meaningVi": "Quyền bỏ phiếu của cổ đông khi quyết định các vấn đề quan trọng của công ty tại đại hội cổ đông. Nguyên tắc 1 cổ phiếu = 1 phiếu. Cổ phiếu thường có quyền biểu quyết, cổ phiếu ưu đãi thường không có. Cần hiểu 'thực hiện quyền biểu quyết', 'ủy quyền biểu quyết', 'hạn chế quyền biểu quyết'.",
        "context": "주주총회, 경영권 분쟁, 적대적 인수방어",
        "culturalNote": "한국은 대주주의 의결권 제한 제도가 있어, 특정 안건에서는 지배주주의 의결권이 3%로 제한됩니다. 또한 재벌 총수 일가의 순환출자 구조로 인한 의결권 왜곡이 사회문제입니다. 베트남은 국영기업의 경우 정부가 황금주(golden share)를 보유하여 중요 결정을 거부할 수 있습니다. 통역 시 '의결권 대리행사' 개념을 정확히 전달해야 합니다.",
        "commonMistakes": [
            {
                "mistake": "quyền quyết định",
                "correction": "quyền biểu quyết",
                "explanation": "'결정권' 일반이 아니라 '의결권'이라는 법적 권리임"
            },
            {
                "mistake": "quyền bầu cử",
                "correction": "quyền biểu quyết / quyền bỏ phiếu",
                "explanation": "'선거권'이 아니라 주주총회에서의 '표결권'임"
            },
            {
                "mistake": "phiếu của cổ đông",
                "correction": "quyền biểu quyết của cổ đông",
                "explanation": "단순 '표'가 아니라 '의결권'이라는 권리로 표현해야 함"
            }
        ],
        "examples": [
            {
                "ko": "대주주는 전체 의결권의 51%를 보유하여 경영권을 장악하고 있습니다.",
                "vi": "Cổ đông lớn nắm giữ 51% quyền biểu quyết và kiểm soát quyền quản lý công ty.",
                "situation": "formal"
            },
            {
                "ko": "우선주는 배당을 더 받지만 의결권은 없습니다.",
                "vi": "Cổ phiếu ưu đãi nhận được cổ tức cao hơn nhưng không có quyền biểu quyết.",
                "situation": "formal"
            },
            {
                "ko": "주주총회에서 이사 선임 안건이 의결권의 과반수 찬성으로 가결되었습니다.",
                "vi": "Tại đại hội cổ đông, nghị án bổ nhiệm giám đốc đã được thông qua với đa số quyền biểu quyết tán thành.",
                "situation": "formal"
            }
        ],
        "relatedTerms": ["주주총회", "위임장권유", "경영권", "보통주"]
    },
    {
        "slug": "quy-dau-tu-tap-hop",
        "korean": "집합투자",
        "vietnamese": "Quỹ đầu tư tập hợp / Đầu tư chung",
        "hanja": "集合投資",
        "hanjaReading": "集(모을 집) + 合(합할 합) + 投(던질 투) + 資(재물 자)",
        "pronunciation": "집합투자",
        "meaningKo": "다수의 투자자로부터 자금을 모아 전문가가 운용하여 수익을 배분하는 투자 방식으로, 펀드(fund)라고도 합니다. 공모펀드와 사모펀드로 구분되며, 주식형·채권형·혼합형 등 다양한 유형이 있습니다. 통역 시 '집합투자기구'(펀드 자체), '집합투자업자'(운용사), '수익자'(투자자)를 구분해야 하며, 베트남어로는 'quỹ đầu tư'(펀드) 또는 'đầu tư tập hợp'(집합투자)을 사용합니다.",
        "meaningVi": "Phương thức đầu tư huy động vốn từ nhiều nhà đầu tư, do chuyên gia quản lý và phân chia lợi nhuận, còn gọi là quỹ (fund). Chia thành quỹ công mộ và quỹ tư nhân, có nhiều loại như quỹ cổ phiếu, quỹ trái phiếu, quỹ hỗn hợp. Cần phân biệt 'tổ chức đầu tư tập hợp' (quỹ), 'công ty quản lý quỹ', 'người thụ hưởng' (nhà đầu tư).",
        "context": "자산운용사, 펀드 판매, 금융투자협회",
        "culturalNote": "한국은 1990년대 후반 외환위기 이후 집합투자 시장이 급성장했으며, 퇴직연금 펀드가 큰 비중을 차지합니다. 베트남은 펀드 시장이 초기 단계로, 은행 예금 선호도가 높아 펀드 투자가 활성화되지 않았습니다. 통역 시 한국의 '판매보수', '환매' 등 수수료 체계를 설명할 때 주의가 필요합니다.",
        "commonMistakes": [
            {
                "mistake": "đầu tư chung của nhiều người",
                "correction": "quỹ đầu tư tập hợp / đầu tư tập hợp",
                "explanation": "일반적 표현보다는 법률 용어 '집합투자' 사용"
            },
            {
                "mistake": "quỹ đầu tư nhóm",
                "correction": "quỹ đầu tư tập hợp",
                "explanation": "'그룹 펀드'가 아니라 공식 용어 '집합투자' 사용"
            },
            {
                "mistake": "công ty đầu tư",
                "correction": "quỹ đầu tư / tổ chức đầu tư tập hợp",
                "explanation": "'투자회사'와 '집합투자기구'는 다른 개념임"
            }
        ],
        "examples": [
            {
                "ko": "이 펀드는 국내 우량 주식에 집합투자하여 안정적인 수익을 추구합니다.",
                "vi": "Quỹ này đầu tư tập hợp vào cổ phiếu ưu lượng trong nước để tìm kiếm lợi nhuận ổn định.",
                "situation": "formal"
            },
            {
                "ko": "집합투자증권을 환매하려면 영업일 기준 3일이 소요됩니다.",
                "vi": "Để hoàn lại (환매) chứng chỉ quỹ đầu tư tập hợp cần 3 ngày làm việc.",
                "situation": "formal"
            },
            {
                "ko": "자본시장법에 따라 집합투자업자는 금융감독원에 등록해야 합니다.",
                "vi": "Theo luật thị trường vốn, công ty quản lý quỹ phải đăng ký với Ủy ban giám sát tài chính.",
                "situation": "formal"
            }
        ],
        "relatedTerms": ["펀드", "자산운용", "공모펀드", "사모펀드"]
    },
    {
        "slug": "san-pham-phai-sinh",
        "korean": "파생상품",
        "vietnamese": "Sản phẩm phái sinh / Công cụ phái sinh",
        "hanja": "派生商品",
        "hanjaReading": "派(갈래 파) + 生(날 생) + 商(장사 상) + 品(물건 품)",
        "pronunciation": "파생상품",
        "meaningKo": "주식, 채권, 통화, 원자재 등 기초자산의 가격 변동에 따라 가치가 결정되는 금융상품으로, 선물·옵션·스왑 등이 대표적입니다. 헤지(위험 회피)와 투기 목적으로 사용되며, 레버리지 효과로 큰 수익과 손실이 가능합니다. 통역 시 '기초자산', '만기일', '행사가격' 등 용어를 정확히 전달해야 하며, 베트남어로는 'sản phẩm phái sinh' 또는 'công cụ phái sinh'을 사용합니다.",
        "meaningVi": "Sản phẩm tài chính có giá trị phụ thuộc vào biến động giá của tài sản cơ sở (cổ phiếu, trái phiếu, ngoại tệ, hàng hóa), bao gồm hợp đồng tương lai, quyền chọn, hoán đổi. Dùng để phòng ngừa rủi ro (hedge) hoặc đầu cơ. Có hiệu ứng đòn bẩy (leverage) nên có thể lãi lỗ lớn. Cần hiểu 'tài sản cơ sở', 'ngày đáo hạn', 'giá thực hiện'.",
        "context": "선물거래소, 파생상품 거래, 리스크관리",
        "culturalNote": "한국은 KOSPI200 선물·옵션 시장이 세계적으로 활성화되어 있으며, 개인투자자의 파생상품 거래 비중이 높습니다. 베트남은 파생상품 시장이 2017년에야 개설되어 거래 규모가 작고, 개인투자자의 이해도가 낮습니다. 통역 시 '증거금', '콜마진' 등 위험관리 개념을 충분히 설명해야 합니다.",
        "commonMistakes": [
            {
                "mistake": "sản phẩm tài chính cao cấp",
                "correction": "sản phẩm phái sinh",
                "explanation": "'고급 금융상품'이 아니라 '파생상품'이라는 특정 개념임"
            },
            {
                "mistake": "hợp đồng tương lai",
                "correction": "sản phẩm phái sinh (hợp đồng tương lai là một loại)",
                "explanation": "'선물'은 파생상품의 한 종류일 뿐, 전체를 대표하지 않음"
            },
            {
                "mistake": "công cụ đầu cơ",
                "correction": "sản phẩm phái sinh",
                "explanation": "'투기 도구'는 부정적 표현이므로 중립적 용어 사용"
            }
        ],
        "examples": [
            {
                "ko": "파생상품 거래는 증거금만 있으면 가능하여 레버리지 효과가 큽니다.",
                "vi": "Giao dịch sản phẩm phái sinh chỉ cần ký quỹ nên có hiệu ứng đòn bẩy lớn.",
                "situation": "formal"
            },
            {
                "ko": "환율 변동 위험을 헤지하기 위해 통화 스왑 파생상품을 활용했습니다.",
                "vi": "Để phòng ngừa rủi ro tỷ giá, chúng tôi sử dụng sản phẩm phái sinh hoán đổi ngoại tệ.",
                "situation": "formal"
            },
            {
                "ko": "개인투자자의 파생상품 거래 손실이 증가하여 투자자 보호가 시급합니다.",
                "vi": "Tổn thất từ giao dịch sản phẩm phái sinh của nhà đầu tư cá nhân tăng cao, cần bảo vệ nhà đầu tư khẩn cấp.",
                "situation": "formal"
            }
        ],
        "relatedTerms": ["선물", "옵션", "기초자산", "헤지"]
    },
    {
        "slug": "nghiep-dau-tu-tai-chinh",
        "korean": "금융투자업",
        "vietnamese": "Nghiệp đầu tư tài chính / Kinh doanh đầu tư tài chính",
        "hanja": "金融投資業",
        "hanjaReading": "金(쇠 금) + 融(녹을 융) + 投(던질 투) + 資(재물 자) + 業(업 업)",
        "pronunciation": "금융투자업",
        "meaningKo": "자본시장법상 투자매매업, 투자중개업, 집합투자업, 투자자문업, 투자일임업, 신탁업을 포괄하는 개념으로, 금융투자상품을 취급하는 사업을 의미합니다. 증권사, 자산운용사, 투자자문사 등이 여기에 속하며, 금융감독원의 허가를 받아야 영업할 수 있습니다. 통역 시 각 업종의 차이를 명확히 설명해야 하며, 베트남어로는 'nghiệp đầu tư tài chính' 또는 'kinh doanh đầu tư tài chính'을 사용합니다.",
        "meaningVi": "Khái niệm bao gồm kinh doanh mua bán đầu tư, môi giới đầu tư, quản lý quỹ, tư vấn đầu tư, quản lý danh mục ủy thác, nghiệp tín thác theo luật thị trường vốn Hàn Quốc. Các công ty chứng khoán, công ty quản lý tài sản, công ty tư vấn đầu tư thuộc lĩnh vực này. Cần giấy phép từ Ủy ban giám sát tài chính. Cần phân biệt rõ từng loại hình kinh doanh.",
        "context": "증권사 인가, 자본시장법 규제, 금융투자협회",
        "culturalNote": "한국은 2009년 자본시장법 시행으로 증권·선물·자산운용·신탁을 금융투자업으로 통합하여, 업권별 칸막이 규제를 완화했습니다. 베트남은 증권업과 자산운용업이 분리되어 있으며, 외국인의 금융투자업 진출에 제한이 많습니다. 통역 시 한국의 '종합금융투자사업자' 개념을 설명할 때 주의가 필요합니다.",
        "commonMistakes": [
            {
                "mistake": "công ty chứng khoán",
                "correction": "nghiệp đầu tư tài chính (증권사는 한 종류일 뿐)",
                "explanation": "'증권사'만이 아니라 더 넓은 개념인 '금융투자업' 전체를 뜻함"
            },
            {
                "mistake": "ngành tài chính đầu tư",
                "correction": "nghiệp đầu tư tài chính",
                "explanation": "'금융투자 산업'보다는 법적 개념인 '금융투자업' 사용"
            },
            {
                "mistake": "kinh doanh chứng khoán",
                "correction": "nghiệp đầu tư tài chính",
                "explanation": "'증권 거래'가 아니라 '금융투자업' 전체를 포괄하는 용어"
            }
        ],
        "examples": [
            {
                "ko": "금융투자업 인가를 받으려면 최소자본금 700억 원이 필요합니다.",
                "vi": "Để nhận giấy phép nghiệp đầu tư tài chính cần vốn tối thiểu 70 tỷ won.",
                "situation": "formal"
            },
            {
                "ko": "자본시장법은 금융투자업자의 건전성 규제를 강화했습니다.",
                "vi": "Luật thị trường vốn đã tăng cường quy định về tính lành mạnh của doanh nghiệp đầu tư tài chính.",
                "situation": "formal"
            },
            {
                "ko": "금융투자업 등록 취소 사유에는 자본금 미달, 부실경영 등이 있습니다.",
                "vi": "Lý do thu hồi đăng ký nghiệp đầu tư tài chính bao gồm thiếu vốn, quản lý kém.",
                "situation": "formal"
            }
        ],
        "relatedTerms": ["투자매매업", "투자중개업", "집합투자업", "자본시장법"]
    }
]

def main():
    # 파일 경로
    legal_file = "/Users/mac/Documents/claude_code/projects/vn.epicstage.co.kr/src/data/terms/legal.json"

    # 기존 데이터 읽기
    with open(legal_file, 'r', encoding='utf-8') as f:
        data = json.load(f)

    print(f"기존 용어 수: {len(data)}")

    # 새 용어 추가
    data.extend(new_terms)

    print(f"추가된 용어 수: {len(new_terms)}")
    print(f"총 용어 수: {len(data)}")

    # 파일에 저장 (indent=2, ensure_ascii=False)
    with open(legal_file, 'w', encoding='utf-8') as f:
        json.dump(data, f, ensure_ascii=False, indent=2)

    print(f"\n✅ {legal_file} 업데이트 완료!")
    print("\n추가된 용어:")
    for term in new_terms:
        print(f"  - {term['korean']} ({term['vietnamese']})")

if __name__ == "__main__":
    main()
