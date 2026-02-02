#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""금융규제법 용어 추가 스크립트 (v6-g)"""

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
            "slug": "phong-chong-rua-tien",
            "korean": "자금세탁방지",
            "vietnamese": "Phòng chống rửa tiền",
            "hanja": "資金洗濯防止",
            "hanjaReading": "資(재물 자) + 金(쇠 금) + 洗(씻을 세) + 濯(빨 탁) + 防(막을 방) + 止(그칠 지)",
            "pronunciation": "퐁총주아띠엔",
            "meaningKo": "불법적으로 취득한 자금의 출처를 숨기고 합법적인 자금인 것처럼 위장하는 행위를 방지하는 제도입니다. 통역 시 주의할 점은 한국의 '특정 금융거래정보의 보고 및 이용 등에 관한 법률'과 베트남의 'Luật phòng, chống rửa tiền'은 규제 강도와 보고 의무 범위가 다르므로 금융기관의 의무사항을 정확히 구분해야 합니다. 한국은 금융정보분석원(FIU)이, 베트남은 국가은행 산하 자금세탁방지위원회가 담당하므로 기관명 혼동에 주의하세요.",
            "meaningVi": "Hệ thống pháp lý nhằm ngăn chặn hành vi che giấu nguồn gốc tài sản thu được từ hoạt động bất hợp pháp và biến chúng thành tài sản hợp pháp. Các tổ chức tài chính phải thực hiện nghĩa vụ báo cáo giao dịch khả nghi và xác minh danh tính khách hàng theo quy định.",
            "context": "금융기관 컴플라이언스, 금융거래 모니터링, 고객확인제도(KYC) 설명",
            "culturalNote": "한국은 2001년부터 본격적인 자금세탁방지 제도를 시행했으며 FATF(국제자금세탁방지기구) 회원국으로서 높은 수준의 규제를 유지합니다. 베트남은 2012년 자금세탁방지법을 제정했으나 아직 이행 수준이 발전 중이며, 현금 거래 비중이 높아 감시가 어려운 상황입니다. 통역 시 양국의 제도 성숙도 차이를 고려하여 설명해야 하며, 한국 금융기관이 베트남 진출 시 현지 규제 준수 부담을 정확히 전달하는 것이 중요합니다.",
            "commonMistakes": [
                {
                    "mistake": "자금세탁을 'giặt tiền'(돈 빨래)로 직역",
                    "correction": "'rửa tiền'가 정확한 법률 용어",
                    "explanation": "giặt는 옷 빨래에만 쓰이고 rửa tiền이 공식 법률 용어입니다."
                },
                {
                    "mistake": "KYC를 그냥 음차해서 '케이와이씨'로 통역",
                    "correction": "'Xác minh danh tính khách hàng' 또는 'Know Your Customer'로 설명",
                    "explanation": "약어를 그대로 쓰면 이해가 어렵고 법적 의무의 핵심을 놓칩니다."
                },
                {
                    "mistake": "금융정보분석원을 '금융정보분석소'로 번역",
                    "correction": "'Cơ quan Tình báo Tài chính (FIU)' 사용",
                    "explanation": "FIU는 국제적으로 통용되는 명칭이므로 병기하는 것이 좋습니다."
                }
            ],
            "examples": [
                {
                    "ko": "금융회사는 의심거래를 24시간 이내에 금융정보분석원에 보고해야 합니다.",
                    "vi": "Các tổ chức tài chính phải báo cáo giao dịch khả nghi cho Cơ quan Tình báo Tài chính (FIU) trong vòng 24 giờ.",
                    "situation": "formal"
                },
                {
                    "ko": "고객확인제도(KYC)에 따라 신분증과 거래 목적을 확인하겠습니다.",
                    "vi": "Theo quy định xác minh danh tính khách hàng (KYC), chúng tôi cần xác nhận giấy tờ tùy thân và mục đích giao dịch.",
                    "situation": "formal"
                },
                {
                    "ko": "이 거래는 자금세탁 의심 사유에 해당하여 추가 심사가 필요합니다.",
                    "vi": "Giao dịch này có dấu hiệu nghi ngờ rửa tiền nên cần thẩm tra bổ sung.",
                    "situation": "formal"
                }
            ],
            "relatedTerms": ["고객확인제도", "금융정보분석원", "의심거래보고", "실소유자확인", "금융거래제한"]
        },
        {
            "slug": "giam-sat-tai-chinh",
            "korean": "금융감독",
            "vietnamese": "Giám sát tài chính",
            "hanja": "金融監督",
            "hanjaReading": "金(쇠 금) + 融(녹을 융) + 監(볼 감) + 督(칠 독)",
            "pronunciation": "감삿따이찐",
            "meaningKo": "금융시장의 안정성과 건전성을 유지하기 위해 금융기관과 금융거래를 감시·규제하는 행정작용입니다. 통역 시 한국의 금융감독원(FSS)과 금융위원회(FSC)의 이원화된 감독 체계와 베트남의 국가은행(SBV) 중심 일원화 체계를 명확히 구분해야 합니다. 특히 한국은 검사·제재 권한이 분리되어 있고 베트남은 통합되어 있으므로 감독 절차를 설명할 때 혼동하지 않도록 주의하세요.",
            "meaningVi": "Hoạt động giám sát, kiểm tra và điều chỉnh các tổ chức tài chính và giao dịch tài chính nhằm đảm bảo sự ổn định và lành mạnh của thị trường tài chính. Bao gồm giám sát ngân hàng, chứng khoán, bảo hiểm và các định chế tài chính khác.",
            "context": "금융기관 검사, 건전성 규제, 금융위기 예방",
            "culturalNote": "한국은 1997년 외환위기 이후 금융감독 체계를 대폭 강화하여 금융위원회와 금융감독원의 이원 체계를 확립했습니다. 베트남은 국가은행이 중앙은행과 감독기구 역할을 동시에 수행하며, 증권위원회(SSC)가 자본시장을 별도 감독합니다. 한국의 감독 시스템이 더 선진화되어 있고 독립성이 높으나, 베트남은 정부 영향력이 강하고 감독 인력·기술이 부족한 상황입니다. 통역 시 양국 감독기관의 권한과 역할 차이를 명확히 해야 합니다.",
            "commonMistakes": [
                {
                    "mistake": "금융감독원을 'Viện giám sát tài chính'로 직역",
                    "correction": "'Cơ quan Giám sát Tài chính (FSS)' 사용",
                    "explanation": "FSS는 고유명사이므로 약어를 병기하는 것이 정확합니다."
                },
                {
                    "mistake": "감독과 검사를 구분 없이 모두 'giám sát'로 번역",
                    "correction": "검사는 'kiểm tra', 감독은 'giám sát'로 구분",
                    "explanation": "검사는 구체적 조사 행위, 감독은 지속적 관리 행위로 법적 의미가 다릅니다."
                },
                {
                    "mistake": "건전성 규제를 'quy định an toàn'으로 번역",
                    "correction": "'quy định thận trọng' 또는 'quy định lành mạnh' 사용",
                    "explanation": "prudential regulation의 정확한 번역은 건전성을 의미하는 thận trọng입니다."
                }
            ],
            "examples": [
                {
                    "ko": "금융감독원이 다음 달 종합검사를 실시할 예정입니다.",
                    "vi": "Cơ quan Giám sát Tài chính (FSS) sẽ tiến hành kiểm tra toàn diện vào tháng tới.",
                    "situation": "formal"
                },
                {
                    "ko": "건전성 규제 비율을 준수하지 못하면 제재를 받을 수 있습니다.",
                    "vi": "Nếu không tuân thủ tỷ lệ quy định thận trọng, có thể bị xử phạt.",
                    "situation": "formal"
                },
                {
                    "ko": "금융위원회가 신규 핀테크 기업에 대한 감독 방안을 발표했습니다.",
                    "vi": "Ủy ban Dịch vụ Tài chính (FSC) đã công bố phương án giám sát các công ty fintech mới.",
                    "situation": "formal"
                }
            ],
            "relatedTerms": ["금융위원회", "금융감독원", "건전성규제", "금융검사", "시정명령"]
        },
        {
            "slug": "quan-ly-ngoai-hoi",
            "korean": "외환관리",
            "vietnamese": "Quản lý ngoại hối",
            "hanja": "外換管理",
            "hanjaReading": "外(바깥 외) + 換(바꿀 환) + 管(대통 관) + 理(다스릴 리)",
            "pronunciation": "꽌리응아이호이",
            "meaningKo": "국가가 외환의 수급과 거래를 규제하고 관리하는 제도로, 환율 안정과 외환보유고 유지를 목적으로 합니다. 통역 시 한국의 '외국환거래법'과 베트남의 '외환관리법'은 자유화 수준이 크게 다르므로 주의해야 합니다. 한국은 경상거래는 완전 자유화되었으나 자본거래는 신고제이고, 베트남은 경상거래도 일부 제한이 있으며 자본거래는 엄격히 통제됩니다. 송금 한도, 외화 예금 제한 등 구체적 규제를 정확히 전달하는 것이 중요합니다.",
            "meaningVi": "Chế độ mà nhà nước kiểm soát và điều tiết việc cung cấp, sử dụng ngoại tệ nhằm ổn định tỷ giá và duy trì dự trữ ngoại hối. Bao gồm các quy định về giao dịch vãng lai, giao dịch vốn, chuyển tiền ra nước ngoài và mở tài khoản ngoại tệ.",
            "context": "국제송금, 외화예금, 해외투자, 외환거래 신고",
            "culturalNote": "한국은 1997년 외환위기 이후 점진적으로 외환 자유화를 추진하여 현재 경상거래는 완전 자유화, 자본거래는 신고 후 허용 원칙입니다. 베트남은 아직 엄격한 외환통제를 유지하며, 외화 예금 이자 지급 금지, 외화 결제 제한, 송금 시 서류 요구 등이 까다롭습니다. 한국 기업이 베트남에서 사업할 때 배당금 송금, 차입금 상환 등에서 어려움을 겪는 경우가 많으므로 통역 시 이러한 실무적 제약을 정확히 전달해야 합니다.",
            "commonMistakes": [
                {
                    "mistake": "외환을 'ngoại hối' 대신 'ngoại tệ'로만 표현",
                    "correction": "외환 시스템은 'ngoại hối', 외화는 'ngoại tệ'로 구분",
                    "explanation": "ngoại hối는 외환 거래·관리 시스템, ngoại tệ는 외국 통화 자체를 의미합니다."
                },
                {
                    "mistake": "외국환거래법을 '외환거래법'으로 축약",
                    "correction": "'Luật Quản lý ngoại hối' 또는 'Foreign Exchange Transaction Act' 병기",
                    "explanation": "법률명은 정확히 번역하고 영문 약어를 병기하는 것이 혼동을 줄입니다."
                },
                {
                    "mistake": "신고와 허가를 구분 없이 'báo cáo'로 통역",
                    "correction": "신고는 'báo cáo', 허가는 'cấp phép'로 구분",
                    "explanation": "신고제는 사후 통지, 허가제는 사전 승인으로 법적 효력이 완전히 다릅니다."
                }
            ],
            "examples": [
                {
                    "ko": "해외 부동산 취득은 외국환거래법에 따라 신고해야 합니다.",
                    "vi": "Việc mua bất động sản ở nước ngoài phải báo cáo theo Luật Quản lý ngoại hối.",
                    "situation": "formal"
                },
                {
                    "ko": "외환 송금 한도는 연간 5만 달러입니다.",
                    "vi": "Hạn mức chuyển tiền ra nước ngoài là 50,000 USD mỗi năm.",
                    "situation": "formal"
                },
                {
                    "ko": "국가은행이 외환보유고 관리를 담당합니다.",
                    "vi": "Ngân hàng Nhà nước chịu trách nhiệm quản lý dự trữ ngoại hối.",
                    "situation": "formal"
                }
            ],
            "relatedTerms": ["외국환거래법", "외환보유고", "환율", "국제송금", "자본거래"]
        },
        {
            "slug": "quy-dinh-chung-khoan",
            "korean": "증권규제",
            "vietnamese": "Quy định chứng khoán",
            "hanja": "證券規制",
            "hanjaReading": "證(증거 증) + 券(문서 권) + 規(법 규) + 制(만들 제)",
            "pronunciation": "꾸이딘쯩코안",
            "meaningKo": "주식, 채권 등 증권의 발행과 거래를 규제하여 투자자를 보호하고 시장의 공정성을 확보하는 법률 체계입니다. 통역 시 한국의 '자본시장법'과 베트남의 '증권법'은 공시 의무, 불공정거래 처벌, 투자자 보호 수준이 다르므로 주의해야 합니다. 한국은 집합투자·파생상품까지 포괄하는 통합 법제이나 베트남은 증권 거래에 국한되며, 내부자거래·시세조종 처벌이 상대적으로 약합니다. IPO 절차, 공시 의무, 감사 기준 등에서 차이를 명확히 전달하세요.",
            "meaningVi": "Hệ thống pháp luật điều chỉnh việc phát hành và giao dịch chứng khoán như cổ phiếu, trái phiếu nhằm bảo vệ nhà đầu tư và đảm bảo tính công bằng, minh bạch của thị trường. Bao gồm quy định về công bố thông tin, giao dịch nội gián, thao túng thị trường và bảo vệ nhà đầu tư nhỏ lẻ.",
            "context": "IPO, 공시 의무, 불공정거래, 투자자 보호",
            "culturalNote": "한국 증권시장은 1990년대 개방 이후 선진화되었고 자본시장법(2009)으로 규제가 통합·강화되었습니다. 베트남 증권시장은 2000년 개설되어 역사가 짧고, 시가총액 대비 외국인 투자 비중이 높으나 정보 비대칭과 투명성 문제가 여전합니다. 한국은 전자공시(DART)가 의무화되어 있으나 베트남은 공시 지연·누락이 흔하며, 내부자거래 적발·처벌이 미흡합니다. 통역 시 한국 투자자가 베트남 시장에 진입할 때 이러한 리스크를 명확히 인지하도록 해야 합니다.",
            "commonMistakes": [
                {
                    "mistake": "자본시장법을 '증권거래법'으로 번역",
                    "correction": "'Luật Thị trường chứng khoán' 또는 'Capital Markets Act' 사용",
                    "explanation": "2009년 통합 이후 자본시장법이 정식 명칭이며 범위가 더 넓습니다."
                },
                {
                    "mistake": "공시를 'công bố'와 'công khai'를 혼용",
                    "correction": "법정 공시는 'công bố thông tin'이 정확",
                    "explanation": "công khai는 일반적 공개, công bố thông tin은 법정 의무 공시입니다."
                },
                {
                    "mistake": "내부자거래를 'giao dịch nội bộ'로 직역",
                    "correction": "'giao dịch nội gián' 사용",
                    "explanation": "insider trading의 정확한 법률 용어는 giao dịch nội gián입니다."
                }
            ],
            "examples": [
                {
                    "ko": "상장사는 분기마다 재무제표를 공시해야 합니다.",
                    "vi": "Công ty niêm yết phải công bố báo cáo tài chính hàng quý.",
                    "situation": "formal"
                },
                {
                    "ko": "내부자거래 혐의로 검찰 조사를 받고 있습니다.",
                    "vi": "Đang bị cơ quan công tố điều tra với cáo buộc giao dịch nội gián.",
                    "situation": "formal"
                },
                {
                    "ko": "증권선물위원회가 시세조종 사건을 조사 중입니다.",
                    "vi": "Ủy ban Chứng khoán Nhà nước đang điều tra vụ thao túng giá.",
                    "situation": "formal"
                }
            ],
            "relatedTerms": ["자본시장법", "내부자거래", "시세조종", "공시의무", "증권선물위원회"]
        },
        {
            "slug": "giam-sat-bao-hiem",
            "korean": "보험감독",
            "vietnamese": "Giám sát bảo hiểm",
            "hanja": "保險監督",
            "hanjaReading": "保(지킬 보) + 險(험할 험) + 監(볼 감) + 督(칠 독)",
            "pronunciation": "감삿바오히엠",
            "meaningKo": "보험회사의 건전한 경영과 보험계약자 보호를 위해 보험업을 감독·규제하는 행정작용입니다. 통역 시 한국의 보험업법과 베트남의 보험업법은 지급여력비율(RBC) 기준, 상품 인가 절차, 모집 규제 등에서 차이가 있으므로 주의하세요. 한국은 RBC 비율 100% 이상 유지가 의무이고 위반 시 즉시 제재되나, 베트남은 기준이 낮고 집행이 느슨합니다. 또한 한국은 변액보험 등 복잡한 상품이 많으나 베트남은 단순 생명보험·손해보험 중심이므로 상품 설명 시 난이도를 조절하세요.",
            "meaningVi": "Hoạt động giám sát và quản lý các doanh nghiệp bảo hiểm nhằm đảm bảo hoạt động kinh doanh lành mạnh và bảo vệ quyền lợi của người tham gia bảo hiểm. Bao gồm giám sát khả năng thanh toán, phê duyệt sản phẩm, quản lý đại lý và xử lý khiếu nại.",
            "context": "보험사 인허가, 지급여력비율, 보험상품 심사, 모집인 관리",
            "culturalNote": "한국 보험시장은 세계 10위권 규모로 성숙했으며, 금융감독원이 엄격하게 감독합니다. 지급여력비율(RBC) 제도가 정착되어 자본 건전성이 높고, 보험계약자 보호를 위한 예금자보호제도(최고 5천만원)가 있습니다. 베트남은 보험 가입률이 낮고(인구 대비 5% 미만) 시장이 미성숙하며, 보험사 자본금 기준이 낮고 감독이 느슨합니다. 또한 보험금 지급 분쟁이 잦고 해결 기간이 길어 소비자 신뢰가 낮습니다. 통역 시 이러한 시장 성숙도 차이를 고려하여 한국 기준을 베트남에 그대로 적용하기 어렵다는 점을 전달하세요.",
            "commonMistakes": [
                {
                    "mistake": "지급여력비율을 '지불능력비율'로 번역",
                    "correction": "'tỷ lệ khả năng thanh toán' 또는 'RBC ratio' 사용",
                    "explanation": "지급여력은 solvency의 정확한 번역이고 RBC 약어를 병기하면 명확합니다."
                },
                {
                    "mistake": "보험모집인을 '보험판매원'으로 번역",
                    "correction": "'đại lý bảo hiểm' 또는 'người môi giới bảo hiểm' 구분 사용",
                    "explanation": "모집인은 법적 지위가 있는 전문 용어이고 đại lý(대리점)와 môi giới(중개인)를 구분해야 합니다."
                },
                {
                    "mistake": "변액보험을 '변동보험'으로 직역",
                    "correction": "'bảo hiểm liên kết đơn vị' 또는 'unit-linked insurance' 사용",
                    "explanation": "variable insurance의 정확한 법적 용어는 bảo hiểm liên kết đơn vị입니다."
                }
            ],
            "examples": [
                {
                    "ko": "이 보험사는 지급여력비율이 150%로 건전성이 우수합니다.",
                    "vi": "Công ty bảo hiểm này có tỷ lệ khả năng thanh toán (RBC) đạt 150%, cho thấy tính lành mạnh cao.",
                    "situation": "formal"
                },
                {
                    "ko": "신규 보험상품은 금융감독원의 사전 심사를 받아야 합니다.",
                    "vi": "Sản phẩm bảo hiểm mới phải được Cơ quan Giám sát Tài chính thẩm định trước.",
                    "situation": "formal"
                },
                {
                    "ko": "보험모집인은 등록증을 소지하고 모집 활동을 해야 합니다.",
                    "vi": "Đại lý bảo hiểm phải có giấy chứng nhận đăng ký khi thực hiện hoạt động môi giới.",
                    "situation": "formal"
                }
            ],
            "relatedTerms": ["보험업법", "지급여력비율", "보험모집인", "변액보험", "예금자보호"]
        },
        {
            "slug": "bao-ve-nguoi-tieu-dung-tai-chinh",
            "korean": "금융소비자보호",
            "vietnamese": "Bảo vệ người tiêu dùng tài chính",
            "hanja": "金融消費者保護",
            "hanjaReading": "金(쇠 금) + 融(녹을 융) + 消(사라질 소) + 費(쓸 비) + 者(놈 자) + 保(지킬 보) + 護(도울 호)",
            "pronunciation": "바오베응어이띠에우중따이찐",
            "meaningKo": "금융상품 거래에서 정보·협상력이 약한 소비자의 권익을 보호하기 위한 제도입니다. 통역 시 한국의 '금융소비자보호법'(2021년 시행)은 설명의무, 적합성·적정성 원칙, 위법계약 해지권 등을 명시하고 있으나 베트남에는 이에 상응하는 통합법이 없고 개별 법령에 산재되어 있어 보호 수준이 낮습니다. 특히 한국은 6개월 내 청약철회권, 금융분쟁조정제도가 확립되어 있으나 베트남은 이러한 제도가 미비하므로 소비자 권리 범위를 정확히 전달하세요.",
            "meaningVi": "Hệ thống pháp lý nhằm bảo vệ quyền và lợi ích của người tiêu dùng trong giao dịch sản phẩm tài chính, do sự bất cân xứng thông tin và năng lực đàm phán. Bao gồm nghĩa vụ giải thích sản phẩm, nguyên tắc phù hợp, quyền hủy hợp đồng và cơ chế giải quyết tranh chấp.",
            "context": "금융상품 판매, 불완전판매, 청약철회, 금융분쟁조정",
            "culturalNote": "한국은 2008년 금융위기 이후 라임·옵티머스 사태 등을 거치며 금융소비자보호법을 제정(2021)하여 선진적 보호 체계를 갖췄습니다. 설명의무 위반 시 계약 취소, 손해배상 책임이 명확하며, 금융감독원 산하 금융소비자보호처가 분쟁을 조정합니다. 베트남은 소비자보호법에 금융 관련 조항이 일부 있으나 구체성이 부족하고, 금융회사의 설명 의무가 약하며, 분쟁 시 법원 소송에 의존해야 해 시간과 비용이 많이 듭니다. 통역 시 한국 수준의 보호를 기대하기 어렵다는 점을 명확히 해야 합니다.",
            "commonMistakes": [
                {
                    "mistake": "적합성 원칙을 '적절성 원칙'으로 혼용",
                    "correction": "적합성(suitability)은 'nguyên tắc phù hợp', 적정성(appropriateness)은 'nguyên tắc thích hợp'로 구분",
                    "explanation": "적합성은 투자권유 시, 적정성은 비권유 거래 시 적용되는 별개 개념입니다."
                },
                {
                    "mistake": "청약철회를 '계약해지'로 번역",
                    "correction": "'quyền rút lại đơn đăng ký' 또는 'cooling-off period' 사용",
                    "explanation": "청약철회는 무조건 취소 가능, 계약해지는 위약금 발생 가능으로 다릅니다."
                },
                {
                    "mistake": "설명의무를 '정보제공의무'로 축소",
                    "correction": "'nghĩa vụ giải thích' 사용",
                    "explanation": "단순 정보 제공이 아니라 이해할 때까지 설명해야 하는 적극적 의무입니다."
                }
            ],
            "examples": [
                {
                    "ko": "이 펀드는 고위험 상품이므로 적합성 평가가 필요합니다.",
                    "vi": "Quỹ này là sản phẩm rủi ro cao nên cần đánh giá nguyên tắc phù hợp.",
                    "situation": "formal"
                },
                {
                    "ko": "계약 체결 후 14일 이내에 청약을 철회할 수 있습니다.",
                    "vi": "Quý khách có thể rút lại đơn đăng ký trong vòng 14 ngày sau khi ký hợp đồng.",
                    "situation": "formal"
                },
                {
                    "ko": "불완전판매로 인한 손해는 금융회사가 배상합니다.",
                    "vi": "Thiệt hại do bán hàng không đúng quy định sẽ do tổ chức tài chính bồi thường.",
                    "situation": "formal"
                }
            ],
            "relatedTerms": ["금융소비자보호법", "적합성원칙", "청약철회권", "불완전판매", "금융분쟁조정"]
        },
        {
            "slug": "quy-dinh-fintech",
            "korean": "핀테크규제",
            "vietnamese": "Quy định fintech",
            "hanja": None,
            "hanjaReading": None,
            "pronunciation": "꾸이딘핀텍",
            "meaningKo": "금융과 기술이 결합한 핀테크 서비스를 규율하는 법규로, 전통 금융규제와 혁신 육성 사이의 균형을 추구합니다. 통역 시 한국의 '혁신금융서비스' 지정제도와 베트남의 핀테크 정책은 접근 방식이 다르므로 주의하세요. 한국은 규제샌드박스를 통해 한시적 특례를 부여하고 이후 정식 인가로 전환하는 체계이나, 베트남은 명확한 규제 프레임워크가 없어 사업자가 불확실성을 겪습니다. 간편송금, 로보어드바이저, P2P 대출 등 서비스별 규제 수준을 정확히 비교하여 전달하세요.",
            "meaningVi": "Các quy định pháp luật điều chỉnh dịch vụ fintech - sự kết hợp giữa tài chính và công nghệ, nhằm cân bằng giữa quản lý rủi ro và khuyến khích đổi mới. Bao gồm quy định về thanh toán điện tử, cho vay P2P, tư vấn robo, blockchain và tiền mã hóa.",
            "context": "간편송금, P2P대출, 로보어드바이저, 블록체인, 규제샌드박스",
            "culturalNote": "한국은 2019년 금융혁신법을 제정하여 규제샌드박스를 도입했고, 카카오페이·토스 등 핀테크 유니콘이 성장했습니다. 금융당국이 혁신과 소비자보호를 동시에 추구하며 단계적으로 규제를 완화하고 있습니다. 베트남은 스마트폰 보급률이 높아 모바일 결제가 빠르게 확산되고 있으나(MoMo, ZaloPay 등) 법제도가 뒤따라가지 못하고 있습니다. P2P 대출은 사실상 무규제 상태이고, 가상자산은 거래가 금지되어 있습니다. 통역 시 한국의 선진 사례를 소개하되 베트남의 법적 제약을 명확히 해야 합니다.",
            "commonMistakes": [
                {
                    "mistake": "핀테크를 '금융기술'로 번역",
                    "correction": "'fintech' 그대로 사용하고 필요시 'công nghệ tài chính' 병기",
                    "explanation": "fintech는 국제적으로 통용되는 고유 용어이므로 음차가 자연스럽습니다."
                },
                {
                    "mistake": "규제샌드박스를 'hộp cát quy định'으로 직역",
                    "correction": "'chương trình thí điểm đổi mới tài chính' 또는 'regulatory sandbox' 병기",
                    "explanation": "직역하면 의미가 불명확하므로 설명적 번역과 영어를 함께 쓰는 것이 좋습니다."
                },
                {
                    "mistake": "간편송금을 'chuyển tiền đơn giản'으로 번역",
                    "correction": "'dịch vụ chuyển tiền nhanh' 또는 'instant payment' 사용",
                    "explanation": "simple transfer가 아니라 instant/real-time의 뉘앙스가 중요합니다."
                }
            ],
            "examples": [
                {
                    "ko": "이 서비스는 혁신금융서비스로 지정받아 2년간 특례를 적용받습니다.",
                    "vi": "Dịch vụ này được chỉ định là dịch vụ tài chính đổi mới và được hưởng ưu đãi đặc biệt trong 2 năm.",
                    "situation": "formal"
                },
                {
                    "ko": "P2P 대출 플랫폼은 온라인투자연계금융업법의 규제를 받습니다.",
                    "vi": "Nền tảng cho vay P2P chịu sự điều chỉnh của Luật Kinh doanh kết nối đầu tư trực tuyến.",
                    "situation": "formal"
                },
                {
                    "ko": "로보어드바이저는 투자자문업 등록이 필요합니다.",
                    "vi": "Dịch vụ tư vấn robo cần đăng ký kinh doanh tư vấn đầu tư.",
                    "situation": "formal"
                }
            ],
            "relatedTerms": ["규제샌드박스", "간편송금", "P2P대출", "로보어드바이저", "혁신금융서비스"]
        },
        {
            "slug": "tien-ma-hoa",
            "korean": "가상화폐",
            "vietnamese": "Tiền mã hóa",
            "hanja": "假想貨幣",
            "hanjaReading": "假(거짓 가) + 想(생각 상) + 貨(재물 화) + 幣(돈 폐)",
            "pronunciation": "띠엔마호아",
            "meaningKo": "블록체인 기술을 기반으로 암호화 방식으로 생성·관리되는 디지털 자산으로, 법정화폐가 아닌 민간 발행 가치 저장 수단입니다. 통역 시 한국에서는 '가상자산'이 공식 용어이고 '가상화폐'는 일상 용어임을 구분하고, 베트남은 거래가 금지되어 있어 법적 지위가 없다는 점을 명확히 해야 합니다. 한국은 특정금융정보법 개정(2021)으로 거래소 신고제를 도입했으나 베트남은 모든 가상자산 거래를 불법으로 간주하며 결제 수단 사용이 금지되어 있습니다.",
            "meaningVi": "Tài sản số được tạo ra và quản lý bằng công nghệ mã hóa dựa trên blockchain, không phải là tiền tệ hợp pháp do chính phủ phát hành. Ở Việt Nam, giao dịch và thanh toán bằng tiền mã hóa bị cấm theo quyết định của Ngân hàng Nhà nước và Chính phủ.",
            "context": "비트코인, 이더리움, 가상자산거래소, 블록체인",
            "culturalNote": "한국은 2017년 가상화폐 열풍 이후 단계적으로 규제를 도입하여 2021년 특정금융정보법 개정으로 거래소에 신고제를 시행하고 실명 계좌를 의무화했습니다. 가상자산은 '화폐'가 아닌 '자산'으로 분류되며 자본이득세(2025년 예정)가 부과될 예정입니다. 베트남은 국가은행이 가상화폐를 결제 수단으로 인정하지 않으며, 2018년부터 모든 발행·거래·중개를 금지했습니다. 다만 블록체인 기술 자체는 연구·개발이 허용됩니다. 통역 시 한국 투자자가 베트남에서 가상자산 사업을 하는 것은 불법임을 명확히 전달하세요.",
            "commonMistakes": [
                {
                    "mistake": "가상화폐와 가상자산을 구분 없이 사용",
                    "correction": "법률 문서에서는 'tài sản ảo'(가상자산), 일상에서는 'tiền mã hóa'(가상화폐)",
                    "explanation": "한국 법에서는 가상자산이 정식 용어이고 화폐는 일상 표현입니다."
                },
                {
                    "mistake": "암호화폐를 'tiền mật mã'로 번역",
                    "correction": "'tiền mã hóa' 또는 'cryptocurrency' 사용",
                    "explanation": "tiền mã hóa가 베트남에서 일반적으로 쓰이는 용어입니다."
                },
                {
                    "mistake": "베트남에서 가상화폐 거래가 '규제'된다고 표현",
                    "correction": "'cấm'(금지)가 정확한 표현",
                    "explanation": "규제는 허용 후 관리, 금지는 원천 불허로 법적 의미가 완전히 다릅니다."
                }
            ],
            "examples": [
                {
                    "ko": "가상자산 거래소는 특정금융정보법에 따라 신고해야 합니다.",
                    "vi": "Sàn giao dịch tài sản ảo phải đăng ký theo Luật Thông tin Giao dịch Tài chính cụ thể (Hàn Quốc).",
                    "situation": "formal"
                },
                {
                    "ko": "베트남에서는 가상화폐 거래가 금지되어 있습니다.",
                    "vi": "Ở Việt Nam, giao dịch tiền mã hóa bị cấm hoàn toàn.",
                    "situation": "formal"
                },
                {
                    "ko": "가상자산 소득에 대해 20% 세율이 적용될 예정입니다.",
                    "vi": "Thu nhập từ tài sản ảo sẽ bị đánh thuế với mức 20% (Hàn Quốc).",
                    "situation": "formal"
                }
            ],
            "relatedTerms": ["블록체인", "비트코인", "이더리움", "가상자산거래소", "특정금융정보법"]
        },
        {
            "slug": "xep-hang-tin-dung",
            "korean": "신용등급",
            "vietnamese": "Xếp hạng tín dụng",
            "hanja": "信用等級",
            "hanjaReading": "信(믿을 신) + 用(쓸 용) + 等(무리 등) + 級(등급 급)",
            "pronunciation": "쎕항띤중",
            "meaningKo": "개인이나 기업의 채무상환능력을 평가하여 등급으로 표시한 것으로, 대출 금리와 한도를 결정하는 핵심 지표입니다. 통역 시 한국의 신용평가 체계(NICE, 코리아크레딧뷰로 등)와 베트남의 신용정보센터(CIC) 시스템은 데이터 범위와 정확도에서 큰 차이가 있음을 주의하세요. 한국은 1~10등급 또는 1,000점 만점 체계로 상세하고, 금융거래·통신요금·공과금 연체 등이 모두 반영되나, 베트남은 은행 대출 기록 중심이고 비금융 정보는 거의 반영되지 않아 정확도가 낮습니다.",
            "meaningVi": "Đánh giá khả năng trả nợ của cá nhân hoặc doanh nghiệp được biểu thị bằng cấp độ, là chỉ số quan trọng quyết định lãi suất và hạn mức vay. Ở Việt Nam, Trung tâm Thông tin Tín dụng (CIC) thuộc Ngân hàng Nhà nước quản lý hệ thống xếp hạng tín dụng, nhưng dữ liệu chủ yếu từ khoản vay ngân hàng.",
            "context": "대출 심사, 금리 산정, 신용카드 발급, 신용회복",
            "culturalNote": "한국은 1990년대 후반부터 민간 신용평가사가 발달하여 거의 모든 성인이 신용등급을 보유하고 있으며, 금융거래뿐 아니라 취업·결혼에도 영향을 미칠 정도로 중요합니다. 신용점수가 낮으면 대출이 거절되거나 고금리가 적용되며, 신용회복 제도가 체계적으로 운영됩니다. 베트남은 신용평가 제도가 초기 단계로, 많은 국민이 신용기록이 없고(credit invisible), 은행 간 정보 공유가 원활하지 않아 다중채무 문제가 발생합니다. 통역 시 한국 기준으로 설명하면 베트남 청중이 이해하기 어려우므로 신용평가의 기본 개념부터 설명해야 합니다.",
            "commonMistakes": [
                {
                    "mistake": "신용등급을 '신용점수'와 혼용",
                    "correction": "등급은 'xếp hạng'(1~10등급), 점수는 'điểm số'(1,000점 만점)",
                    "explanation": "한국은 등급과 점수 체계가 병행되므로 문맥에 맞게 구분해야 합니다."
                },
                {
                    "mistake": "신용평가사를 '신용평가회사'로 번역",
                    "correction": "'công ty xếp hạng tín dụng' 또는 'credit bureau' 사용",
                    "explanation": "credit rating agency와 credit bureau는 다르나 한국에서는 혼용되므로 맥락 확인 필요."
                },
                {
                    "mistake": "연체 정보를 '지연 정보'로 완곡하게 번역",
                    "correction": "'thông tin quá hạn' 또는 'delinquency' 사용",
                    "explanation": "연체는 법적으로 명확한 부정적 정보이므로 완곡어를 쓰면 오해를 줍니다."
                }
            ],
            "examples": [
                {
                    "ko": "신용등급 1등급은 금리 우대를 받을 수 있습니다.",
                    "vi": "Xếp hạng tín dụng cấp 1 có thể được hưởng lãi suất ưu đãi.",
                    "situation": "formal"
                },
                {
                    "ko": "연체 기록이 있으면 신용점수가 큰 폭으로 하락합니다.",
                    "vi": "Nếu có lịch sử quá hạn, điểm tín dụng sẽ giảm mạnh.",
                    "situation": "formal"
                },
                {
                    "ko": "신용정보조회 동의서에 서명해주세요.",
                    "vi": "Vui lòng ký vào giấy đồng ý tra cứu thông tin tín dụng.",
                    "situation": "formal"
                }
            ],
            "relatedTerms": ["신용평가사", "신용점수", "연체기록", "신용회복", "신용정보원"]
        },
        {
            "slug": "che-tai-tai-chinh",
            "korean": "금융제재",
            "vietnamese": "Chế tài tài chính",
            "hanja": "金融制裁",
            "hanjaReading": "金(쇠 금) + 融(녹을 융) + 制(만들 제) + 裁(마를 재)",
            "pronunciation": "쩨따이따이찐",
            "meaningKo": "국제법 위반이나 안보 위협 국가·개인에 대해 금융거래를 제한하는 경제적 압박 수단입니다. 통역 시 한국의 '대외무역법'과 '외국환거래법'에 따른 제재와 베트남의 제재 이행 수준은 차이가 있으므로 주의하세요. 한국은 유엔 안보리 결의와 미국 독자 제재를 대부분 이행하나, 베트남은 유엔 결의는 따르지만 미국 독자 제재는 선택적으로 적용합니다. 북한·이란·러시아 등에 대한 제재 시 양국의 입장 차이가 있으므로 민감한 사안임을 인지하고 통역하세요.",
            "meaningVi": "Biện pháp áp lực kinh tế bằng cách hạn chế giao dịch tài chính đối với quốc gia, tổ chức hoặc cá nhân vi phạm luật quốc tế hoặc đe dọa an ninh. Việt Nam tuân thủ các nghị quyết trừng phạt của Hội đồng Bảo an Liên Hợp Quốc nhưng không tham gia các biện pháp trừng phạt đơn phương của Mỹ.",
            "context": "국제 제재, 자산 동결, 송금 차단, 무역 금지",
            "culturalNote": "한국은 미국과 동맹 관계로 대북 제재를 엄격히 이행하며, 5·24 조치(2010) 이후 남북 교역이 사실상 중단되었습니다. 또한 이란·러시아에 대한 제재도 국제 공조에 따라 이행하고 있습니다. 금융회사는 제재 대상자 명단(SDN List 등)을 상시 모니터링하며 거래 시 자동 차단 시스템을 운영합니다. 베트남은 북한과 전통적 우호 관계를 유지해왔으나 유엔 결의는 준수하고 있으며, 미국과의 관계 개선으로 제재 이행 수준이 높아지고 있습니다. 통역 시 제재 대상국에 대한 양국의 정치적 입장 차이를 고려하여 중립적으로 표현하세요.",
            "commonMistakes": [
                {
                    "mistake": "제재를 '처벌'로 번역",
                    "correction": "'chế tài'(제재)와 'trừng phạt'(처벌)은 다른 개념",
                    "explanation": "제재는 예방적·강제적 조치, 처벌은 사후적 형벌로 법적 성격이 다릅니다."
                },
                {
                    "mistake": "유엔 제재와 미국 독자 제재를 구분 없이 '국제 제재'로 통칭",
                    "correction": "'nghị quyết HĐBA LHQ'(유엔 안보리 결의)와 'chế tài đơn phương của Mỹ'(미국 독자 제재) 구분",
                    "explanation": "베트남은 유엔 결의만 이행하므로 구분이 중요합니다."
                },
                {
                    "mistake": "자산동결을 '자산압류'로 번역",
                    "correction": "'đóng băng tài sản'(동결)과 'tịch thu tài sản'(압류) 구분",
                    "explanation": "동결은 거래 금지, 압류는 소유권 박탈로 법적 효과가 다릅니다."
                }
            ],
            "examples": [
                {
                    "ko": "이 기업은 유엔 제재 대상 명단에 포함되어 있어 거래가 금지됩니다.",
                    "vi": "Doanh nghiệp này nằm trong danh sách chế tài của Liên Hợp Quốc nên bị cấm giao dịch.",
                    "situation": "formal"
                },
                {
                    "ko": "미국 재무부 OFAC 제재를 위반하면 거액의 벌금이 부과될 수 있습니다.",
                    "vi": "Vi phạm chế tài OFAC của Bộ Tài chính Mỹ có thể bị phạt tiền rất lớn.",
                    "situation": "formal"
                },
                {
                    "ko": "대북 제재로 인해 북한과의 금융거래가 전면 중단되었습니다.",
                    "vi": "Do chế tài đối với Triều Tiên, mọi giao dịch tài chính với Triều Tiên đã bị ngừng hoàn toàn.",
                    "situation": "formal"
                }
            ],
            "relatedTerms": ["유엔제재", "자산동결", "금융거래차단", "제재대상자명단", "수출통제"]
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
