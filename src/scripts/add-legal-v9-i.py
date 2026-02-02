#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""기후변화/에너지법 용어 추가 (v9-i)"""
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
            "slug": "trung-hoa-carbon",
            "korean": "탄소중립",
            "vietnamese": "Trung hòa carbon",
            "hanja": "炭素中立",
            "hanjaReading": "炭(숯 탄) + 素(본디 소) + 中(가운데 중) + 立(설 립)",
            "pronunciation": "탄소중립",
            "meaningKo": "온실가스 배출량과 흡수량을 같게 하여 순배출량을 0으로 만드는 것을 말합니다. 통역 시 한국은 2050 탄소중립을 목표로 법제화했으며, 기후위기대응법으로 온실가스 감축 의무화, 탄소중립위원회 설치, 기업의 탄소배출 공시 의무, 위반 시 과태료와 형사처벌이 가능하다는 점을 명확히 전달해야 합니다.",
            "meaningVi": "Làm cho lượng phát thải khí nhà kính và lượng hấp thụ bằng nhau để lượng phát thải ròng bằng 0. Hàn Quốc pháp điển hóa mục tiêu trung hòa carbon 2050, Luật ứng phó khủng hoảng khí hậu bắt buộc giảm khí nhà kính, thành lập Ủy ban trung hòa carbon, nghĩa vụ công bố phát thải carbon của doanh nghiệp, vi phạm có thể bị phạt tiền hành chính và xử lý hình sự.",
            "context": "탄소중립 정책 수립 및 기업 감축 의무 상황에서 사용",
            "culturalNote": "한국은 2020년 탄소중립을 선언하고 2050년까지 달성을 목표로 합니다. 주요 정책은 재생에너지 확대, 전기차·수소차 보급, 석탄발전 축소이며, 철강·화학 등 탄소다배출 기업의 부담이 큽니다. 베트남도 2050 탄소중립을 선언했으나 석탄 의존도가 높아 통역 시 한국의 법적 의무화를 강조해야 합니다.",
            "commonMistakes": [
                {
                    "mistake": "carbon 0",
                    "correction": "trung hòa carbon (중립)",
                    "explanation": "'탄소 0'은 직역이며 배출과 흡수의 균형이라는 의미가 누락됩니다"
                },
                {
                    "mistake": "không phát thải carbon",
                    "correction": "trung hòa carbon (배출=흡수)",
                    "explanation": "'탄소 배출 안 함'은 완전 제로이며 흡수로 상쇄하는 중립과 다릅니다"
                },
                {
                    "mistake": "giảm khí thải",
                    "correction": "trung hòa carbon (순배출 0)",
                    "explanation": "'배출 감소'는 줄이기만 하며 순배출 0의 목표가 누락됩니다"
                }
            ],
            "examples": [
                {
                    "ko": "한국은 2050년까지 탄소중립을 달성하겠다고 법제화했습니다",
                    "vi": "Hàn Quốc đã pháp điển hóa đạt trung hòa carbon đến năm 2050",
                    "situation": "formal"
                },
                {
                    "ko": "우리 회사도 탄소중립 해야 하나요?",
                    "vi": "Công ty chúng tôi cũng phải trung hòa carbon à?",
                    "situation": "onsite"
                },
                {
                    "ko": "탄소중립은 배출 감축과 흡수 증대를 함께 추진해야 합니다",
                    "vi": "Trung hòa carbon phải cùng thúc đẩy giảm phát thải và tăng hấp thụ",
                    "situation": "formal"
                }
            ],
            "relatedTerms": ["온실가스", "기후위기대응법", "2050목표", "탄소배출권"]
        },
        {
            "slug": "giao-dich-quyen-phat-thai",
            "korean": "배출권거래",
            "vietnamese": "Giao dịch quyền phát thải",
            "hanja": "排出權去來",
            "hanjaReading": "排(배출할 배) + 出(날 출) + 權(권리 권) + 去(갈 거) + 來(올 래)",
            "pronunciation": "배출권거래",
            "meaningKo": "기업에 온실가스 배출 허용량을 할당하고 초과·부족분을 시장에서 거래하는 제도입니다. 통역 시 한국은 2015년부터 시행하며 600여 기업이 참여, 배출량을 초과하면 배출권을 구매해야 하고, 부족하면 판매 가능, 미이행 시 최대 3배 과징금, 배출권 가격은 시장에서 형성된다는 점을 명확히 전달해야 합니다.",
            "meaningVi": "Chế độ phân bổ hạn mức phát thải khí nhà kính cho doanh nghiệp và giao dịch phần vượt/thiếu trên thị trường. Hàn Quốc thực hiện từ 2015, khoảng 600 doanh nghiệp tham gia, vượt lượng phát thải phải mua quyền phát thải, thiếu có thể bán, không tuân thủ phạt tiền tối đa gấp 3 lần, giá quyền phát thải hình thành trên thị trường.",
            "context": "배출권 할당 및 거래 시장 운영 상황에서 사용",
            "culturalNote": "한국 배출권 시장은 아시아 최대 규모이며, 철강·시멘트·석유화학 등 탄소다배출 기업이 주요 참여자입니다. 배출권 가격은 톤당 1~3만 원 수준이며, 기업은 에너지 효율을 높여 배출권을 줄이거나 신재생에너지를 사용합니다. 베트남은 배출권 거래제가 없어 통역 시 한국의 시장 메커니즘을 설명해야 합니다.",
            "commonMistakes": [
                {
                    "mistake": "mua bán khí thải",
                    "correction": "giao dịch quyền phát thải (권리 거래)",
                    "explanation": "'배출 매매'는 오염물질 자체를 사고파는 것처럼 오해됩니다"
                },
                {
                    "mistake": "thị trường carbon",
                    "correction": "giao dịch quyền phát thải (공식 용어)",
                    "explanation": "'탄소시장'은 일반 명칭이며 '배출권거래'가 법률 용어입니다"
                },
                {
                    "mistake": "quyền ô nhiễm",
                    "correction": "quyền phát thải (온실가스)",
                    "explanation": "'오염권'은 부정적이며 온실가스 배출권의 의미가 왜곡됩니다"
                }
            ],
            "examples": [
                {
                    "ko": "이 기업은 배출량을 초과하여 배출권 100만 톤을 구매했습니다",
                    "vi": "Doanh nghiệp này vượt lượng phát thải nên đã mua 1 triệu tấn quyền phát thải",
                    "situation": "formal"
                },
                {
                    "ko": "배출권 가격이 오르면 어떻게 되나요?",
                    "vi": "Nếu giá quyền phát thải tăng thì sao?",
                    "situation": "onsite"
                },
                {
                    "ko": "배출권 미이행 시 최대 3배 과징금이 부과됩니다",
                    "vi": "Không tuân thủ quyền phát thải sẽ bị phạt tiền tối đa gấp 3 lần",
                    "situation": "formal"
                }
            ],
            "relatedTerms": ["온실가스", "탄소시장", "할당량", "과징금"]
        },
        {
            "slug": "nang-luong-tai-tao",
            "korean": "신재생에너지",
            "vietnamese": "Năng lượng tái tạo",
            "hanja": "新再生에너지",
            "hanjaReading": "新(새 신) + 再(다시 재) + 生(날 생) + 에너지",
            "pronunciation": "신재생에너지",
            "meaningKo": "태양광·풍력·수력 등 재생 가능하고 환경친화적인 에너지를 말합니다. 통역 시 한국은 신재생에너지법으로 보급을 지원하며, 의무할당제(RPS)로 발전사에 일정 비율 신재생 사용 의무화, 보조금·세제 혜택 제공, 2030년까지 전력의 30%를 신재생으로 목표, 태양광·풍력이 주력이라는 점을 명확히 전달해야 합니다.",
            "meaningVi": "Năng lượng có thể tái tạo và thân thiện môi trường như năng lượng mặt trời, gió, thủy điện. Hàn Quốc Luật năng lượng tái tạo hỗ trợ phổ cập, chế độ hạn ngạch bắt buộc (RPS) bắt buộc công ty phát điện dùng tỷ lệ nhất định năng lượng tái tạo, cung cấp trợ cấp và ưu đãi thuế, mục tiêu 30% điện năng là năng lượng tái tạo đến 2030, chủ yếu là mặt trời và gió.",
            "context": "신재생에너지 정책 및 발전사업 인허가 상황에서 사용",
            "culturalNote": "한국은 탈원전 정책으로 신재생에너지 확대를 추진했으나 최근 원전 회귀로 정책이 혼란스럽습니다. 태양광은 산지 훼손 논란이 있고, 해상풍력은 어민 반발로 어려움을 겪습니다. RPS로 발전사는 신재생 의무 비율을 채워야 하며 미이행 시 과징금을 냅니다. 베트남은 태양광·풍력이 급증하나 송전망 부족으로 통역 시 한국의 인프라 문제를 설명해야 합니다.",
            "commonMistakes": [
                {
                    "mistake": "năng lượng sạch",
                    "correction": "năng lượng tái tạo (재생 가능)",
                    "explanation": "'청정에너지'는 원자력도 포함되며 재생 가능 에너지와 다릅니다"
                },
                {
                    "mistake": "năng lượng xanh",
                    "correction": "năng lượng tái tạo (공식 용어)",
                    "explanation": "'그린에너지'는 비공식적이며 법률 용어로 '재생에너지'가 정확합니다"
                },
                {
                    "mistake": "điện mặt trời",
                    "correction": "năng lượng tái tạo (태양광은 일부)",
                    "explanation": "'태양광 전기'는 신재생에너지의 한 종류이며 전체를 대표하지 못합니다"
                }
            ],
            "examples": [
                {
                    "ko": "한국은 2030년까지 신재생에너지 비중을 30%로 높이겠다고 선언했습니다",
                    "vi": "Hàn Quốc tuyên bố tăng tỷ trọng năng lượng tái tạo lên 30% đến 2030",
                    "situation": "formal"
                },
                {
                    "ko": "태양광 패널 설치하면 보조금 받나요?",
                    "vi": "Lắp tấm năng lượng mặt trời có được trợ cấp không?",
                    "situation": "onsite"
                },
                {
                    "ko": "발전사는 RPS로 일정 비율 신재생에너지를 의무적으로 사용해야 합니다",
                    "vi": "Công ty phát điện phải bắt buộc dùng tỷ lệ nhất định năng lượng tái tạo theo RPS",
                    "situation": "formal"
                }
            ],
            "relatedTerms": ["태양광", "풍력", "RPS", "탈원전"]
        },
        {
            "slug": "kien-khi-hau",
            "korean": "기후소송",
            "vietnamese": "Kiện khí hậu",
            "hanja": "氣候訴訟",
            "hanjaReading": "氣(기운 기) + 候(기후 후) + 訴(하소연할 소) + 訟(송사할 송)",
            "pronunciation": "기후소송",
            "meaningKo": "정부나 기업의 기후변화 대응 부족을 이유로 제기하는 소송을 말합니다. 통역 시 한국은 청소년들이 정부를 상대로 탄소중립 목표 미흡을 소송했으며, 헌법상 환경권과 미래세대 권리가 쟁점이고, 기업의 그린워싱(위장 환경주의) 소송도 증가하며, 해외는 승소 사례가 많으나 한국은 초기 단계라는 점을 명확히 전달해야 합니다.",
            "meaningVi": "Kiện tụng do chính phủ hoặc doanh nghiệp ứng phó thiếu sót với biến đổi khí hậu. Ở Hàn Quốc thanh thiếu niên đã kiện chính phủ vì mục tiêu trung hòa carbon không đủ, quyền môi trường theo hiến pháp và quyền thế hệ tương lai là điểm tranh luận, kiện tụng greenwashing (chủ nghĩa môi trường giả trang) của doanh nghiệp cũng tăng, nước ngoài có nhiều vụ thắng kiện nhưng Hàn Quốc còn giai đoạn đầu.",
            "context": "기후소송 제기 및 법정 공방 상황에서 사용",
            "culturalNote": "한국은 2020년 청소년들이 '청소년기후행동'으로 탄소중립 목표가 미흡하다며 헌법소원을 제기했으며, 현재 재판 진행 중입니다. 네덜란드·독일 등은 정부가 패소하여 감축 목표를 상향했습니다. 기업의 그린워싱도 소송 대상이며, 환경단체가 적극 제소하고 있습니다. 베트남은 기후소송이 없어 통역 시 한국의 선구적 사례를 설명해야 합니다.",
            "commonMistakes": [
                {
                    "mistake": "kiện môi trường",
                    "correction": "kiện khí hậu (기후변화 특화)",
                    "explanation": "'환경 소송'은 포괄적이며 기후변화 대응의 특수성이 약화됩니다"
                },
                {
                    "mistake": "kiện chính phủ về khí hậu",
                    "correction": "kiện khí hậu (법적 용어)",
                    "explanation": "'정부 상대 기후 소송'은 설명이며 '기후소송'이 법률 용어입니다"
                },
                {
                    "mistake": "tố cáo biến đổi khí hậu",
                    "correction": "kiện khí hậu (소송)",
                    "explanation": "'기후변화 고발'은 형사고발처럼 들리며 민사소송과 다릅니다"
                }
            ],
            "examples": [
                {
                    "ko": "청소년들은 정부의 탄소중립 목표가 미흡하다며 기후소송을 제기했습니다",
                    "vi": "Thanh thiếu niên đã kiện khí hậu vì mục tiêu trung hòa carbon của chính phủ không đủ",
                    "situation": "formal"
                },
                {
                    "ko": "기업이 거짓으로 친환경 광고하면 소송당할 수 있나요?",
                    "vi": "Doanh nghiệp quảng cáo thân thiện môi trường giả có thể bị kiện không?",
                    "situation": "onsite"
                },
                {
                    "ko": "기후소송은 미래세대의 환경권을 보호하기 위한 법적 수단입니다",
                    "vi": "Kiện khí hậu là công cụ pháp lý để bảo vệ quyền môi trường thế hệ tương lai",
                    "situation": "formal"
                }
            ],
            "relatedTerms": ["환경권", "미래세대", "그린워싱", "헌법소원"]
        },
        {
            "slug": "danh-gia-tac-dong-moi-truong",
            "korean": "환경영향평가",
            "vietnamese": "Đánh giá tác động môi trường",
            "hanja": "環境影響評價",
            "hanjaReading": "環(고리 환) + 境(지경 경) + 影(그림자 영) + 響(울릴 향) + 評(평가할 평) + 價(값 가)",
            "pronunciation": "환경영향평가",
            "meaningKo": "대규모 개발사업이 환경에 미치는 영향을 사전에 조사·평가하는 제도입니다. 통역 시 한국은 환경영향평가법으로 도로·댐·공장 등 사업 전 의무 시행, 주민 의견 수렴 필수, 평가서 거짓 작성 시 3년 이하 징역, 미이행 시 사업 승인 취소, 부실 평가로 환경 피해 발생 시 손해배상 책임이 있다는 점을 명확히 전달해야 합니다.",
            "meaningVi": "Chế độ điều tra và đánh giá trước tác động của dự án phát triển quy mô lớn lên môi trường. Hàn Quốc Luật đánh giá tác động môi trường bắt buộc thực hiện trước dự án như đường, đập, nhà máy, bắt buộc lấy ý kiến dân, viết sai báo cáo đánh giá bị phạt tù 3 năm, không tuân thủ sẽ thu hồi phê duyệt dự án, đánh giá kém gây thiệt hại môi trường phải chịu trách nhiệm bồi thường.",
            "context": "개발사업 환경영향평가 실시 및 승인 절차에서 사용",
            "culturalNote": "한국은 1970년대 개발 우선 정책으로 환경이 파괴되어 1993년 환경영향평가 제도를 법제화했습니다. 4대강 사업·새만금 간척 등 대규모 사업에서 평가가 부실하다는 논란이 많았으며, 최근 주민 참여와 전문성이 강화되고 있습니다. 베트남도 환경영향평가 제도가 있으나 부실 평가가 많아 통역 시 한국의 엄격한 절차를 설명해야 합니다.",
            "commonMistakes": [
                {
                    "mistake": "kiểm tra môi trường",
                    "correction": "đánh giá tác động môi trường (사전 평가)",
                    "explanation": "'환경 검사'는 사후 점검이며 사전 영향 평가와 다릅니다"
                },
                {
                    "mistake": "báo cáo môi trường",
                    "correction": "đánh giá tác động môi trường (법적 제도)",
                    "explanation": "'환경 보고서'는 일반 문서이며 법적 제도로서의 영향평가와 다릅니다"
                },
                {
                    "mistake": "thẩm định môi trường",
                    "correction": "đánh giá tác động môi trường (공식 용어)",
                    "explanation": "'환경 심사'는 비공식적이며 법률 용어로 부적절합니다"
                }
            ],
            "examples": [
                {
                    "ko": "이 도로 건설은 환경영향평가를 받지 않아 사업 승인이 취소되었습니다",
                    "vi": "Xây dựng đường này bị thu hồi phê duyệt vì không thực hiện đánh giá tác động môi trường",
                    "situation": "formal"
                },
                {
                    "ko": "공장 짓는데 환경영향평가 꼭 해야 하나요?",
                    "vi": "Xây nhà máy có bắt buộc đánh giá tác động môi trường không?",
                    "situation": "onsite"
                },
                {
                    "ko": "환경영향평가는 주민 의견을 반드시 수렴해야 합니다",
                    "vi": "Đánh giá tác động môi trường phải lấy ý kiến dân",
                    "situation": "formal"
                }
            ],
            "relatedTerms": ["환경영향평가법", "개발사업", "주민참여", "사전예방"]
        },
        {
            "slug": "thoa-thuan-xanh-moi",
            "korean": "그린뉴딜",
            "vietnamese": "Thỏa thuận xanh mới",
            "hanja": None,
            "hanjaReading": None,
            "pronunciation": "그린뉴딜",
            "meaningKo": "저탄소 경제로 전환하며 일자리를 창출하는 정부 정책을 말합니다. 통역 시 한국은 2020년 한국판 뉴딜로 그린뉴딜을 추진하며, 신재생에너지·전기차·그린리모델링에 160조 원 투자, 녹색 일자리 66만 개 창출 목표, 탄소중립과 경제성장을 동시 달성이 목표이며, 정부 주도 대규모 투자가 특징이라는 점을 명확히 전달해야 합니다.",
            "meaningVi": "Chính sách chính phủ chuyển đổi sang nền kinh tế carbon thấp đồng thời tạo việc làm. Hàn Quốc thúc đẩy Green New Deal trong bản New Deal Hàn Quốc 2020, đầu tư 160 nghìn tỷ won vào năng lượng tái tạo, xe điện, cải tạo xanh, mục tiêu tạo 660,000 việc làm xanh, mục tiêu đồng thời đạt trung hòa carbon và tăng trưởng kinh tế, đặc trưng là đầu tư quy mô lớn do chính phủ chủ đạo.",
            "context": "그린뉴딜 정책 수립 및 예산 집행 상황에서 사용",
            "culturalNote": "한국은 코로나19 경제위기와 기후위기를 동시 극복하기 위해 그린뉴딜을 추진했습니다. 주요 사업은 태양광 발전, 전기차 충전소, 노후 건물 에너지 효율화 등이며, 정부가 재정을 투입하여 일자리를 창출합니다. 미국·EU도 유사 정책을 추진 중입니다. 베트남은 그린뉴딜 개념이 없어 통역 시 한국의 포괄적 정책을 설명해야 합니다.",
            "commonMistakes": [
                {
                    "mistake": "chính sách xanh",
                    "correction": "thỏa thuận xanh mới (뉴딜 강조)",
                    "explanation": "'녹색 정책'은 일반 환경정책이며 뉴딜의 경제·고용 정책 성격이 누락됩니다"
                },
                {
                    "mistake": "New Deal xanh",
                    "correction": "thỏa thuận xanh mới (베트남어 용어)",
                    "explanation": "영어를 그대로 쓰지 말고 베트남어로 번역해야 합니다"
                },
                {
                    "mistake": "đầu tư môi trường",
                    "correction": "thỏa thuận xanh mới (포괄 정책)",
                    "explanation": "'환경 투자'는 일부이며 뉴딜의 포괄적 정책이 누락됩니다"
                }
            ],
            "examples": [
                {
                    "ko": "한국판 뉴딜은 그린뉴딜과 디지털뉴딜을 양대 축으로 합니다",
                    "vi": "New Deal Hàn Quốc lấy Thỏa thuận xanh mới và Digital New Deal làm hai trục chính",
                    "situation": "formal"
                },
                {
                    "ko": "그린뉴딜로 어떤 일자리가 생기나요?",
                    "vi": "Thỏa thuận xanh mới tạo việc làm gì?",
                    "situation": "onsite"
                },
                {
                    "ko": "그린뉴딜은 탄소중립과 경제성장을 동시에 추구합니다",
                    "vi": "Thỏa thuận xanh mới đồng thời theo đuổi trung hòa carbon và tăng trưởng kinh tế",
                    "situation": "formal"
                }
            ],
            "relatedTerms": ["한국판뉴딜", "녹색일자리", "저탄소경제", "재정투자"]
        },
        {
            "slug": "chuyen-doi-nang-luong",
            "korean": "에너지전환",
            "vietnamese": "Chuyển đổi năng lượng",
            "hanja": None,
            "hanjaReading": None,
            "pronunciation": "에너지전환",
            "meaningKo": "화석연료 중심에서 신재생에너지 중심으로 에너지 시스템을 전환하는 것을 말합니다. 통역 시 한국은 탈석탄·탈원전을 추진했으나 최근 원전 회귀로 정책이 변화하며, 태양광·풍력 확대, 전기차·수소차 보급, 에너지 효율 향상이 핵심이고, 전력 시장 개편과 송전망 확충이 과제라는 점을 명확히 전달해야 합니다.",
            "meaningVi": "Chuyển đổi hệ thống năng lượng từ trung tâm nhiên liệu hóa thạch sang trung tâm năng lượng tái tạo. Hàn Quốc đã thúc đẩy rời khỏi than đá và hạt nhân nhưng gần đây chính sách thay đổi vì quay lại hạt nhân, cốt lõi là mở rộng mặt trời, gió, phổ cập xe điện, xe hydro, nâng cao hiệu suất năng lượng, cải tổ thị trường điện và mở rộng lưới truyền tải là vấn đề.",
            "context": "에너지 정책 수립 및 전력 시장 개편 논의 상황에서 사용",
            "culturalNote": "한국은 문재인 정부 시절 탈원전·탈석탄으로 에너지전환을 추진했으나, 윤석열 정부는 원전 비중을 높이는 방향으로 선회했습니다. 태양광·풍력은 간헐성 문제로 전력망 안정이 어렵고, 송전망 부족으로 신재생 발전소가 출력 제한을 받습니다. 베트남도 석탄 의존도가 높아 통역 시 한국의 정책 변화를 설명해야 합니다.",
            "commonMistakes": [
                {
                    "mistake": "thay đổi năng lượng",
                    "correction": "chuyển đổi năng lượng (전환 정책)",
                    "explanation": "'에너지 변경'은 일상 표현이며 전환 정책의 법적 개념이 약화됩니다"
                },
                {
                    "mistake": "năng lượng mới",
                    "correction": "chuyển đổi năng lượng (시스템 전환)",
                    "explanation": "'신에너지'는 에너지 종류이며 시스템 전환의 의미가 누락됩니다"
                },
                {
                    "mistake": "bỏ nhiên liệu hóa thạch",
                    "correction": "chuyển đổi năng lượng (포괄 개념)",
                    "explanation": "'화석연료 폐기'는 일부이며 신재생 확대 등 전체 전환이 누락됩니다"
                }
            ],
            "examples": [
                {
                    "ko": "에너지전환은 탄소중립 달성을 위한 핵심 과제입니다",
                    "vi": "Chuyển đổi năng lượng là vấn đề cốt lõi để đạt trung hòa carbon",
                    "situation": "formal"
                },
                {
                    "ko": "석탄발전소는 언제 없어지나요?",
                    "vi": "Nhà máy điện than khi nào hết?",
                    "situation": "onsite"
                },
                {
                    "ko": "에너지전환은 송전망 확충과 전력 시장 개편이 함께 이루어져야 합니다",
                    "vi": "Chuyển đổi năng lượng phải cùng thực hiện mở rộng lưới truyền tải và cải tổ thị trường điện",
                    "situation": "formal"
                }
            ],
            "relatedTerms": ["탈석탄", "탈원전", "신재생", "전력망"]
        },
        {
            "slug": "thue-carbon",
            "korean": "탄소세",
            "vietnamese": "Thuế carbon",
            "hanja": "炭素稅",
            "hanjaReading": "炭(숯 탄) + 素(본디 소) + 稅(세금 세)",
            "pronunciation": "탄소세",
            "meaningKo": "화석연료 사용이나 탄소 배출에 부과하는 세금으로, 배출 감축을 유도합니다. 통역 시 한국은 아직 도입하지 않았으나 검토 중이며, 배출권거래제와 중복 우려, 기업 부담 증가 반발, 탄소국경세(EU CBAM) 대응 필요, 도입 시 휘발유·경유·석탄 등에 부과 예정이라는 점을 명확히 전달해야 합니다.",
            "meaningVi": "Thuế đánh vào sử dụng nhiên liệu hóa thạch hoặc phát thải carbon, khuyến khích giảm phát thải. Hàn Quốc chưa áp dụng nhưng đang xem xét, lo ngại trùng lặp với chế độ giao dịch quyền phát thải, phản đối vì tăng gánh nặng doanh nghiệp, cần ứng phó thuế biên giới carbon (EU CBAM), nếu áp dụng dự kiến đánh vào xăng, dầu diesel, than đá.",
            "context": "탄소세 도입 논의 및 기업 영향 평가 상황에서 사용",
            "culturalNote": "한국은 배출권거래제를 운영하고 있어 탄소세 도입 시 이중 부담 논란이 있습니다. EU는 탄소국경세로 탄소세가 없는 국가의 수입품에 관세를 부과할 예정이어서 한국도 도입 압력이 큽니다. 철강·시멘트·화학 등 수출 기업의 반발이 크며, 정치적으로 민감합니다. 베트남은 탄소세가 없어 통역 시 국제적 도입 추세를 설명해야 합니다.",
            "commonMistakes": [
                {
                    "mistake": "thuế khí thải",
                    "correction": "thuế carbon (탄소 특화)",
                    "explanation": "'배출세'는 포괄적이며 탄소 배출세의 의미가 약화됩니다"
                },
                {
                    "mistake": "thuế môi trường",
                    "correction": "thuế carbon (탄소 특정)",
                    "explanation": "'환경세'는 일반 환경 과세이며 탄소세와 구분됩니다"
                },
                {
                    "mistake": "thuế ô nhiễm",
                    "correction": "thuế carbon (온실가스)",
                    "explanation": "'오염세'는 일반 오염이며 온실가스 배출세의 의미가 누락됩니다"
                }
            ],
            "examples": [
                {
                    "ko": "탄소세 도입은 기업의 반발로 지연되고 있습니다",
                    "vi": "Áp dụng thuế carbon bị chậm trễ do phản đối của doanh nghiệp",
                    "situation": "formal"
                },
                {
                    "ko": "탄소세 생기면 휘발유 값이 오르나요?",
                    "vi": "Có thuế carbon thì giá xăng tăng à?",
                    "situation": "onsite"
                },
                {
                    "ko": "EU 탄소국경세 대응을 위해 탄소세 도입이 필요합니다",
                    "vi": "Cần áp dụng thuế carbon để ứng phó thuế biên giới carbon EU",
                    "situation": "formal"
                }
            ],
            "relatedTerms": ["배출권거래", "탄소국경세", "EU CBAM", "기업부담"]
        },
        {
            "slug": "nan-dan-khi-hau",
            "korean": "기후난민",
            "vietnamese": "Nạn dân khí hậu",
            "hanja": "氣候難民",
            "hanjaReading": "氣(기운 기) + 候(기후 후) + 難(어려울 난) + 民(백성 민)",
            "pronunciation": "기후난민",
            "meaningKo": "기후변화로 생존이 불가능해져 고향을 떠나는 사람들을 말합니다. 통역 시 한국은 난민법상 기후난민을 인정하지 않으며, 국제법상으로도 법적 지위가 없고, 해수면 상승·사막화·극한 기상으로 발생하며, 2050년까지 2억 명 예상, 인도적 체류 허가 가능성은 있으나 권리 보장은 미약하다는 점을 명확히 전달해야 합니다.",
            "meaningVi": "Người rời bỏ quê hương vì biến đổi khí hậu khiến không thể sống. Hàn Quốc Luật tị nạn không công nhận nạn dân khí hậu, theo luật quốc tế cũng không có tư cách pháp lý, xảy ra do mực nước biển dâng, sa mạc hóa, thời tiết cực đoan, dự kiến 200 triệu người đến 2050, có khả năng cho phép lưu trú nhân đạo nhưng đảm bảo quyền lợi yếu.",
            "context": "기후난민 보호 및 국제 협력 논의 상황에서 사용",
            "culturalNote": "한국은 기후난민을 법적으로 인정하지 않으며, 국제적으로도 난민협약이 기후난민을 포함하지 않아 보호 공백이 있습니다. 투발루·몰디브 등 섬나라는 해수면 상승으로 국가 존망이 위협받으며, 아프리카는 사막화로 대규모 이주가 예상됩니다. 베트남도 메콩델타 해수면 상승 위협이 커서 통역 시 양국의 기후 위험을 설명해야 합니다.",
            "commonMistakes": [
                {
                    "mistake": "người di cư khí hậu",
                    "correction": "nạn dân khí hậu (난민 지위)",
                    "explanation": "'기후 이주자'는 자발적 이주처럼 들리며 강제 이주의 난민 성격이 약화됩니다"
                },
                {
                    "mistake": "tị nạn môi trường",
                    "correction": "nạn dân khí hậu (기후변화 특화)",
                    "explanation": "'환경 난민'은 포괄적이며 기후변화 난민의 특수성이 누락됩니다"
                },
                {
                    "mistake": "người phải rời bỏ nhà",
                    "correction": "nạn dân khí hậu (법적 개념)",
                    "explanation": "'집 떠난 사람'은 일상 표현이며 난민의 법적 개념이 약화됩니다"
                }
            ],
            "examples": [
                {
                    "ko": "투발루는 해수면 상승으로 국민 전체가 기후난민이 될 위기입니다",
                    "vi": "Tuvalu đang trong khủng hoảng toàn bộ quốc dân trở thành nạn dân khí hậu vì mực nước biển dâng",
                    "situation": "formal"
                },
                {
                    "ko": "기후난민도 한국에서 보호받을 수 있나요?",
                    "vi": "Nạn dân khí hậu có được bảo vệ ở Hàn Quốc không?",
                    "situation": "onsite"
                },
                {
                    "ko": "기후난민은 국제법상 법적 지위가 없어 보호 공백이 있습니다",
                    "vi": "Nạn dân khí hậu không có tư cách pháp lý theo luật quốc tế nên có khoảng trống bảo vệ",
                    "situation": "formal"
                }
            ],
            "relatedTerms": ["난민협약", "해수면상승", "사막화", "인도적체류"]
        },
        {
            "slug": "quan-tri-ESG",
            "korean": "ESG경영",
            "vietnamese": "Quản trị ESG",
            "hanja": None,
            "hanjaReading": None,
            "pronunciation": "이에스지경영",
            "meaningKo": "환경(E)·사회(S)·지배구조(G)를 고려하는 지속 가능 경영을 말합니다. 통역 시 한국은 상장사 ESG 공시 의무화를 추진하며, 탄소배출·안전·인권·이사회 독립성 등을 평가하고, ESG 등급이 투자·금융에 영향, 그린워싱 방지 위해 검증 강화, ESG 채권 발행 증가 중이라는 점을 명확히 전달해야 합니다.",
            "meaningVi": "Quản trị bền vững xem xét môi trường (E), xã hội (S), cấu trúc quản trị (G). Hàn Quốc đang thúc đẩy bắt buộc công bố ESG của công ty niêm yết, đánh giá phát thải carbon, an toàn, nhân quyền, tính độc lập hội đồng quản trị, cấp độ ESG ảnh hưởng đầu tư và tài chính, tăng cường xác minh để ngăn greenwashing, đang tăng phát hành trái phiếu ESG.",
            "context": "기업 ESG 경영 전략 수립 및 공시 의무 상황에서 사용",
            "culturalNote": "한국은 대기업 중심으로 ESG 경영이 확산되고 있으며, 국민연금 등 기관투자자가 ESG를 투자 기준으로 삼습니다. 삼성·현대차 등은 RE100(재생에너지 100%)에 가입했으며, ESG 채권 발행도 증가합니다. 중소기업은 부담이 커서 지원이 필요합니다. 베트남은 ESG 개념이 생소해 통역 시 한국의 선도 사례를 설명해야 합니다.",
            "commonMistakes": [
                {
                    "mistake": "quản lý môi trường xã hội",
                    "correction": "quản trị ESG (E+S+G)",
                    "explanation": "'환경사회 관리'는 G(지배구조)가 누락되며 ESG의 포괄성이 약화됩니다"
                },
                {
                    "mistake": "kinh doanh bền vững",
                    "correction": "quản trị ESG (구체적 기준)",
                    "explanation": "'지속가능 경영'은 일반 개념이며 ESG의 구체적 기준이 누락됩니다"
                },
                {
                    "mistake": "trách nhiệm xã hội doanh nghiệp",
                    "correction": "quản trị ESG (E+S+G)",
                    "explanation": "'기업 사회책임'은 S만 의미하며 E·G가 제외됩니다"
                }
            ],
            "examples": [
                {
                    "ko": "상장사는 2025년부터 ESG 정보를 의무적으로 공시해야 합니다",
                    "vi": "Công ty niêm yết từ 2025 phải bắt buộc công bố thông tin ESG",
                    "situation": "formal"
                },
                {
                    "ko": "ESG 잘하면 투자 유치가 쉬워지나요?",
                    "vi": "Làm ESG tốt thì thu hút đầu tư dễ à?",
                    "situation": "onsite"
                },
                {
                    "ko": "ESG 경영은 장기적 기업 가치를 높이는 전략입니다",
                    "vi": "Quản trị ESG là chiến lược nâng cao giá trị doanh nghiệp dài hạn",
                    "situation": "formal"
                }
            ],
            "relatedTerms": ["지속가능경영", "ESG공시", "RE100", "ESG채권"]
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
    print(f"✅ Added {len(filtered)} terms (기후변화/에너지법). Total: {len(data)}")

if __name__ == '__main__':
    main()
