#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""스포츠/엔터법 용어 추가 (v9-g)"""
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
            "slug": "hop-dong-cau-thu",
            "korean": "선수계약",
            "vietnamese": "Hợp đồng cầu thủ",
            "hanja": "選手契約",
            "hanjaReading": "選(가릴 선) + 手(손 수) + 契(맺을 계) + 約(약속할 약)",
            "pronunciation": "선수계약",
            "meaningKo": "프로스포츠 선수와 구단 간의 근로계약으로, 연봉·계약기간·의무사항을 규정합니다. 통역 시 한국은 표준계약서를 사용하며 선수협과 협의하고, FA(자유계약) 제도로 이적 자유를 보장하며, 계약 위반 시 손해배상과 자격정지가 가능하고, 외국인 선수는 비자·세금 문제도 고려해야 한다는 점을 명확히 전달해야 합니다.",
            "meaningVi": "Hợp đồng lao động giữa vận động viên thể thao chuyên nghiệp và câu lạc bộ, quy định lương, thời hạn hợp đồng, nghĩa vụ. Ở Hàn Quốc sử dụng hợp đồng tiêu chuẩn được thỏa thuận với hiệp hội cầu thủ, chế độ FA (tự do hợp đồng) đảm bảo tự do chuyển nhượng, vi phạm hợp đồng có thể bồi thường thiệt hại và đình chỉ tư cách, cầu thủ nước ngoài phải xem xét visa và thuế.",
            "context": "선수 계약 협상 및 분쟁 조정 상황에서 사용",
            "culturalNote": "한국 프로스포츠는 야구·축구·농구·배구가 발달했으며, 선수 연봉은 협상으로 결정되고 최저연봉이 보장됩니다. FA 제도로 일정 기간 후 이적이 자유로우며, 외국인 선수는 쿼터제로 제한됩니다. 베트남은 프로스포츠가 발달하지 않아 통역 시 한국의 체계적 계약 시스템을 설명해야 합니다.",
            "commonMistakes": [
                {
                    "mistake": "hợp đồng thể thao",
                    "correction": "hợp đồng cầu thủ (선수 특화)",
                    "explanation": "'스포츠 계약'은 포괄적이며 선수 계약의 특수성이 약화됩니다"
                },
                {
                    "mistake": "hợp đồng lao động vận động viên",
                    "correction": "hợp đồng cầu thủ (간결한 공식 용어)",
                    "explanation": "'선수 근로계약'은 정확하지만 '선수계약'이 더 간결하고 일반적입니다"
                },
                {
                    "mistake": "ký hợp đồng đội",
                    "correction": "hợp đồng cầu thủ (법적 문서)",
                    "explanation": "'팀과 계약 서명'은 행위이며 계약서 자체를 지칭하지 못합니다"
                }
            ],
            "examples": [
                {
                    "ko": "이 선수는 연봉 10억 원에 3년 계약을 체결했습니다",
                    "vi": "Cầu thủ này ký hợp đồng 3 năm với lương 1 tỷ won",
                    "situation": "formal"
                },
                {
                    "ko": "계약 해지하려면 어떻게 해야 하나요?",
                    "vi": "Muốn chấm dứt hợp đồng phải làm sao?",
                    "situation": "onsite"
                },
                {
                    "ko": "선수계약 위반 시 위약금과 자격정지 처분을 받습니다",
                    "vi": "Vi phạm hợp đồng cầu thủ sẽ bị phạt vi phạm và đình chỉ tư cách",
                    "situation": "formal"
                }
            ],
            "relatedTerms": ["FA제도", "이적료", "연봉협상", "표준계약서"]
        },
        {
            "slug": "phi-chuyen-nhuong",
            "korean": "이적료",
            "vietnamese": "Phí chuyển nhượng",
            "hanja": "移籍料",
            "hanjaReading": "移(옮길 이) + 籍(책 적) + 料(헤아릴 료)",
            "pronunciation": "이적료",
            "meaningKo": "선수가 다른 구단으로 이적할 때 기존 구단에 지급하는 금전적 보상을 말합니다. 통역 시 한국은 계약 기간 중 이적 시 구단 간 협상으로 결정하며, FA 선수는 이적료가 없고, 국제 이적은 FIFA 규정을 따르며, 선수 육성 보상금 제도도 있고, 이적료 분쟁은 중재로 해결한다는 점을 명확히 전달해야 합니다.",
            "meaningVi": "Bồi thường bằng tiền trả cho câu lạc bộ cũ khi cầu thủ chuyển sang câu lạc bộ khác. Ở Hàn Quốc khi chuyển nhượng trong thời hạn hợp đồng được quyết định bằng đàm phán giữa các câu lạc bộ, cầu thủ FA không có phí chuyển nhượng, chuyển nhượng quốc tế theo quy định FIFA, cũng có chế độ bồi thường đào tạo cầu thủ, tranh chấp phí chuyển nhượng được giải quyết bằng trọng tài.",
            "context": "선수 이적 협상 및 이적료 분쟁 조정 상황에서 사용",
            "culturalNote": "한국 프로스포츠는 이적료 제도가 축구에서 주로 사용되며, 야구는 트레이드 중심입니다. 국제 이적은 FIFA 규정을 따르며, 이적료는 선수 가치·나이·실적에 따라 수억~수십억 원입니다. 베트남은 프로축구 이적료가 낮아 통역 시 한국의 높은 이적료 수준을 설명해야 합니다.",
            "commonMistakes": [
                {
                    "mistake": "tiền chuyển đội",
                    "correction": "phí chuyển nhượng (법적 용어)",
                    "explanation": "'팀 이동 비용'은 일상 표현이며 법률 용어로 부적절합니다"
                },
                {
                    "mistake": "giá cầu thủ",
                    "correction": "phí chuyển nhượng (구단 간 보상)",
                    "explanation": "'선수 가격'은 시장 가치이며 구단 간 보상인 이적료와 다릅니다"
                },
                {
                    "mistake": "phí mua cầu thủ",
                    "correction": "phí chuyển nhượng (공식 용어)",
                    "explanation": "'선수 구매비'는 비공식적이며 '이적료'가 정확합니다"
                }
            ],
            "examples": [
                {
                    "ko": "이 선수의 이적료는 50억 원으로 책정되었습니다",
                    "vi": "Phí chuyển nhượng của cầu thủ này được định giá 5 tỷ won",
                    "situation": "formal"
                },
                {
                    "ko": "FA 선수는 이적료 없이 이적할 수 있나요?",
                    "vi": "Cầu thủ FA có thể chuyển nhượng không phí không?",
                    "situation": "onsite"
                },
                {
                    "ko": "국제 이적료는 FIFA 분쟁해결위원회에서 중재합니다",
                    "vi": "Phí chuyển nhượng quốc tế được Ủy ban giải quyết tranh chấp FIFA trọng tài",
                    "situation": "formal"
                }
            ],
            "relatedTerms": ["선수계약", "FA제도", "FIFA규정", "트레이드"]
        },
        {
            "slug": "doping",
            "korean": "도핑",
            "vietnamese": "Doping",
            "hanja": None,
            "hanjaReading": None,
            "pronunciation": "도핑",
            "meaningKo": "경기력 향상을 위해 금지약물을 복용하거나 금지 방법을 사용하는 반도핑 규정 위반 행위를 말합니다. 통역 시 한국은 세계반도핑기구(WADA) 규정을 준수하며, 도핑 적발 시 2~4년 자격정지, 메달 박탈, 기록 말소가 되고, 고의성에 따라 처벌이 달라지며, 치료목적사용면책(TUE) 제도가 있다는 점을 명확히 전달해야 합니다.",
            "meaningVi": "Hành vi vi phạm quy định chống doping bằng cách sử dụng thuốc cấm hoặc phương pháp cấm để nâng cao thành tích thi đấu. Hàn Quốc tuân thủ quy định Cơ quan chống doping thế giới (WADA), khi phát hiện doping bị đình chỉ tư cách 2-4 năm, tước huy chương, xóa thành tích, hình phạt khác nhau theo tính cố ý, có chế độ miễn trừ sử dụng vì mục đích điều trị (TUE).",
            "context": "도핑 검사 및 위반 제재 상황에서 사용",
            "culturalNote": "한국은 도핑 단속을 엄격히 하며, 한국도핑방지위원회(KADA)가 검사를 실시합니다. 올림픽·아시안게임 등 국제대회에서 도핑 적발 시 국가 이미지에 큰 타격을 주어 사전 교육을 강화하고 있습니다. 베트남도 WADA 가입국이나 검사 빈도가 낮아 통역 시 한국의 엄격한 관리를 설명해야 합니다.",
            "commonMistakes": [
                {
                    "mistake": "dùng thuốc cấm",
                    "correction": "doping (국제 표준 용어)",
                    "explanation": "'금지약물 사용'은 번역이지만 도핑은 국제 표준 용어로 원어 사용이 원칙입니다"
                },
                {
                    "mistake": "gian lận thể thao",
                    "correction": "doping (약물 특화)",
                    "explanation": "'스포츠 사기'는 포괄적이며 약물 사용의 특수성이 누락됩니다"
                },
                {
                    "mistake": "chất kích thích",
                    "correction": "doping (금지약물 + 방법)",
                    "explanation": "'흥분제'는 약물의 일부이며 혈액도핑 등 다른 방법이 제외됩니다"
                }
            ],
            "examples": [
                {
                    "ko": "이 선수는 도핑 적발로 4년 자격정지 처분을 받았습니다",
                    "vi": "Cầu thủ này bị đình chỉ tư cách 4 năm vì phát hiện doping",
                    "situation": "formal"
                },
                {
                    "ko": "감기약도 도핑에 걸리나요?",
                    "vi": "Thuốc cảm cũng bị doping à?",
                    "situation": "onsite"
                },
                {
                    "ko": "치료 목적으로 금지약물을 사용하려면 TUE를 신청해야 합니다",
                    "vi": "Nếu muốn dùng thuốc cấm vì mục đích điều trị phải xin TUE",
                    "situation": "formal"
                }
            ],
            "relatedTerms": ["WADA", "자격정지", "TUE", "금지약물"]
        },
        {
            "slug": "trong-tai-the-thao",
            "korean": "스포츠중재",
            "vietnamese": "Trọng tài thể thao",
            "hanja": "仲裁",
            "hanjaReading": "仲(가운데 중) + 裁(재단할 재)",
            "pronunciation": "스포츠중재",
            "meaningKo": "스포츠 관련 분쟁을 법원 소송 대신 중재기관이 신속히 해결하는 제도입니다. 통역 시 한국은 대한체육중재위원회(STAK)가 운영하며, 선수 징계·도핑·계약 분쟁 등을 다루고, 중재 판정은 법원 판결과 동일한 효력을 가지며, 국제적으로는 스포츠중재재판소(CAS)가 최종 심급이라는 점을 명확히 전달해야 합니다.",
            "meaningVi": "Chế độ cơ quan trọng tài giải quyết nhanh tranh chấp liên quan thể thao thay vì kiện tụng tòa án. Ở Hàn Quốc do Ủy ban trọng tài thể thao Hàn Quốc (STAK) vận hành, xử lý kỷ luật cầu thủ, doping, tranh chấp hợp đồng, phán quyết trọng tài có hiệu lực như phán quyết tòa án, quốc tế Tòa án trọng tài thể thao (CAS) là cấp xét xử cuối cùng.",
            "context": "스포츠 분쟁 중재 신청 및 절차 안내 상황에서 사용",
            "culturalNote": "한국은 2007년 STAK를 설립하여 스포츠 분쟁을 신속히 해결하고 있습니다. 법원 소송보다 빠르고 전문성이 높아 활용도가 높으며, 도핑 사건은 1심으로 중재 필수입니다. 국제 분쟁은 CAS에 제소 가능합니다. 베트남은 스포츠 중재 제도가 미비해 통역 시 한국의 체계를 설명해야 합니다.",
            "commonMistakes": [
                {
                    "mistake": "tòa án thể thao",
                    "correction": "trọng tài thể thao (중재)",
                    "explanation": "'스포츠 법원'은 사법기관처럼 들리며 중재의 개념이 누락됩니다"
                },
                {
                    "mistake": "giải quyết tranh chấp thể thao",
                    "correction": "trọng tài thể thao (법적 제도)",
                    "explanation": "'스포츠 분쟁 해결'은 일반 설명이며 중재 제도의 법적 성격이 약화됩니다"
                },
                {
                    "mistake": "phân xử thể thao",
                    "correction": "trọng tài thể thao (공식 용어)",
                    "explanation": "'스포츠 판결'은 비공식적이며 법률 용어로 부적절합니다"
                }
            ],
            "examples": [
                {
                    "ko": "선수는 징계 처분에 불복하여 대한체육중재위원회에 중재를 신청했습니다",
                    "vi": "Cầu thủ không phục kỷ luật nên đã xin trọng tài tại Ủy ban trọng tài thể thao Hàn Quốc",
                    "situation": "formal"
                },
                {
                    "ko": "중재 결정에 불복하면 어떻게 하나요?",
                    "vi": "Nếu không phục quyết định trọng tài thì sao?",
                    "situation": "onsite"
                },
                {
                    "ko": "스포츠중재는 법원 소송보다 빠르고 전문적입니다",
                    "vi": "Trọng tài thể thao nhanh và chuyên môn hơn kiện tụng tòa án",
                    "situation": "formal"
                }
            ],
            "relatedTerms": ["STAK", "CAS", "중재판정", "분쟁해결"]
        },
        {
            "slug": "quyen-phat-song",
            "korean": "방송권",
            "vietnamese": "Quyền phát sống",
            "hanja": "放送權",
            "hanjaReading": "放(놓을 방) + 送(보낼 송) + 權(권리 권)",
            "pronunciation": "방송권",
            "meaningKo": "스포츠 경기를 TV·인터넷 등으로 중계할 수 있는 권리를 말합니다. 통역 시 한국은 리그가 독점 판매하거나 구단이 공동 판매하며, 방송권료는 구단 주요 수입원이고, 무단 중계 시 저작권법 위반으로 형사·민사 책임을 지며, OTT 플랫폼으로 시청 방식이 다양화되고 있다는 점을 명확히 전달해야 합니다.",
            "meaningVi": "Quyền phát sóng trận đấu thể thao qua TV, internet. Ở Hàn Quốc giải đấu bán độc quyền hoặc câu lạc bộ bán chung, tiền quyền phát sóng là nguồn thu nhập chính của câu lạc bộ, phát sóng không phép vi phạm Luật bản quyền chịu trách nhiệm hình sự và dân sự, cách xem đang đa dạng hóa sang nền tảng OTT.",
            "context": "방송권 계약 협상 및 무단 중계 단속 상황에서 사용",
            "culturalNote": "한국 프로스포츠는 방송권료가 주요 수입이며, KBO·K리그 등은 독점 계약으로 수백억 원을 받습니다. 최근 OTT 플랫폼(SPOTV·쿠팡플레이 등)이 방송권을 구매하며 시장이 확대되고 있습니다. 불법 중계 단속도 강화되고 있습니다. 베트남은 방송권 시장이 작아 통역 시 한국의 큰 시장 규모를 설명해야 합니다.",
            "commonMistakes": [
                {
                    "mistake": "quyền truyền hình",
                    "correction": "quyền phát sóng (TV + 인터넷)",
                    "explanation": "'방송권'은 TV만 의미하며 인터넷 중계가 누락됩니다"
                },
                {
                    "mistake": "bản quyền thể thao",
                    "correction": "quyền phát sóng (중계 권리)",
                    "explanation": "'스포츠 저작권'은 포괄적이며 중계권의 특수성이 약화됩니다"
                },
                {
                    "mistake": "quyền chiếu",
                    "correction": "quyền phát sóng (생중계)",
                    "explanation": "'상영권'은 영화처럼 들리며 생중계의 의미가 누락됩니다"
                }
            ],
            "examples": [
                {
                    "ko": "이 시즌 프로야구 방송권은 500억 원에 계약되었습니다",
                    "vi": "Quyền phát sóng bóng chày chuyên nghiệp mùa này được ký hợp đồng 50 tỷ won",
                    "situation": "formal"
                },
                {
                    "ko": "유튜브로 경기 중계하면 불법인가요?",
                    "vi": "Phát sóng trận đấu trên YouTube có bất hợp pháp không?",
                    "situation": "onsite"
                },
                {
                    "ko": "무단 방송권 침해 시 5년 이하 징역에 처해집니다",
                    "vi": "Vi phạm quyền phát sóng không phép bị phạt tù đến 5 năm",
                    "situation": "formal"
                }
            ],
            "relatedTerms": ["저작권", "독점계약", "OTT", "불법중계"]
        },
        {
            "slug": "quyen-hinh-anh",
            "korean": "초상권",
            "vietnamese": "Quyền hình ảnh",
            "hanja": "肖像權",
            "hanjaReading": "肖(닮을 초) + 像(형상 상) + 權(권리 권)",
            "pronunciation": "초상권",
            "meaningKo": "자신의 얼굴·모습을 함부로 촬영·공표·이용당하지 않을 권리입니다. 통역 시 연예인·운동선수는 초상권이 재산권으로 인정되어 광고·상품화에 활용하며, 무단 사용 시 민사 손해배상과 형사처벌(5년 이하 징역)이 가능하고, 공익적 보도는 예외이며, 초상권 계약은 전속계약에 포함된다는 점을 명확히 전달해야 합니다.",
            "meaningVi": "Quyền không bị chụp, công bố, sử dụng tùy tiện khuôn mặt, hình dáng của mình. Nghệ sĩ, vận động viên có quyền hình ảnh được công nhận là quyền tài sản nên được dùng cho quảng cáo, thương mại hóa, sử dụng không phép có thể bồi thường thiệt hại dân sự và xử phạt hình sự (tù 5 năm), báo đạo vì lợi ích công được miễn, hợp đồng quyền hình ảnh bao gồm trong hợp đồng độc quyền.",
            "context": "초상권 침해 소송 및 계약 협상 상황에서 사용",
            "culturalNote": "한국은 연예인·운동선수의 초상권을 강력히 보호하며, 광고·굿즈 판매에 초상권 계약이 필수입니다. 무단 도용 시 손해배상액이 수천만~수억 원에 달하며, SNS에서 무단 사용도 처벌됩니다. 베트남은 초상권 보호가 약해 통역 시 한국의 강력한 보호를 설명해야 합니다.",
            "commonMistakes": [
                {
                    "mistake": "quyền chân dung",
                    "correction": "quyền hình ảnh (초상권)",
                    "explanation": "'초상권'은 예술작품처럼 들리며 법적 권리로서의 초상권과 다릅니다"
                },
                {
                    "mistake": "quyền khuôn mặt",
                    "correction": "quyền hình ảnh (얼굴 + 모습)",
                    "explanation": "'얼굴 권리'는 얼굴만 의미하며 전체 모습이 누락됩니다"
                },
                {
                    "mistake": "bản quyền hình ảnh",
                    "correction": "quyền hình ảnh (초상권) vs bản quyền (저작권)",
                    "explanation": "'이미지 저작권'은 저작권과 혼동되며 초상권과 법적 성격이 다릅니다"
                }
            ],
            "examples": [
                {
                    "ko": "이 연예인은 초상권 무단 사용으로 1억 원 손해배상을 청구했습니다",
                    "vi": "Nghệ sĩ này yêu cầu bồi thường 100 triệu won vì sử dụng không phép quyền hình ảnh",
                    "situation": "formal"
                },
                {
                    "ko": "사진 찍어서 SNS에 올리면 초상권 침해인가요?",
                    "vi": "Chụp ảnh đăng SNS có vi phạm quyền hình ảnh không?",
                    "situation": "onsite"
                },
                {
                    "ko": "광고 계약에는 초상권 사용 조건이 명시되어야 합니다",
                    "vi": "Hợp đồng quảng cáo phải ghi rõ điều kiện sử dụng quyền hình ảnh",
                    "situation": "formal"
                }
            ],
            "relatedTerms": ["퍼블리시티권", "전속계약", "무단사용", "손해배상"]
        },
        {
            "slug": "quan-ly-nghe-si",
            "korean": "매니지먼트",
            "vietnamese": "Quản lý nghệ sĩ",
            "hanja": None,
            "hanjaReading": None,
            "pronunciation": "매니지먼트",
            "meaningKo": "연예인·운동선수의 활동을 대리하고 매니저가 관리하는 사업을 말합니다. 통역 시 한국은 연예인과 전속계약을 맺어 출연료·광고료의 일부를 수수료로 받으며, 부당한 전속계약(노예계약)은 무효이고, 불공정 계약은 공정위가 시정하며, 이중계약 분쟁이 빈번하다는 점을 명확히 전달해야 합니다.",
            "meaningVi": "Công việc đại diện hoạt động của nghệ sĩ, vận động viên và quản lý bởi manager. Ở Hàn Quốc ký hợp đồng độc quyền với nghệ sĩ và nhận một phần thù lao diễn, quảng cáo làm phí, hợp đồng độc quyền bất công (hợp đồng nô lệ) vô hiệu, hợp đồng không công bằng được Ủy ban công bằng cạnh tranh chỉnh sửa, tranh chấp hợp đồng kép thường xuyên.",
            "context": "연예인 매니지먼트 계약 및 분쟁 조정 상황에서 사용",
            "culturalNote": "한국 연예계는 대형 기획사(SM·JYP·YG 등)가 전속계약으로 연예인을 관리하며, 계약 기간은 7년 상한이 권고됩니다. 과거 불공정 계약이 많아 사회 문제가 되었고, 공정위가 표준계약서를 제정했습니다. 베트남도 연예계가 성장 중이나 계약 관행이 미비해 통역 시 한국의 표준을 설명해야 합니다.",
            "commonMistakes": [
                {
                    "mistake": "công ty quản lý",
                    "correction": "quản lý nghệ sĩ (매니지먼트 사업)",
                    "explanation": "'관리회사'는 조직이며 매니지먼트 사업의 개념이 약화됩니다"
                },
                {
                    "mistake": "đại diện nghệ sĩ",
                    "correction": "quản lý nghệ sĩ (포괄적 관리)",
                    "explanation": "'연예인 대리'는 법적 대리만 연상되며 전반적 관리가 누락됩니다"
                },
                {
                    "mistake": "kinh doanh nghệ sĩ",
                    "correction": "quản lý nghệ sĩ (법적 용어)",
                    "explanation": "'연예인 사업'은 비공식적이며 법률 용어로 부적절합니다"
                }
            ],
            "examples": [
                {
                    "ko": "이 연예인은 매니지먼트 계약 위반으로 기획사를 상대로 소송을 제기했습니다",
                    "vi": "Nghệ sĩ này đã kiện công ty vì vi phạm hợp đồng quản lý nghệ sĩ",
                    "situation": "formal"
                },
                {
                    "ko": "전속 기간은 보통 몇 년인가요?",
                    "vi": "Thời gian độc quyền thường bao lâu?",
                    "situation": "onsite"
                },
                {
                    "ko": "불공정 매니지먼트 계약은 공정거래위원회에 신고할 수 있습니다",
                    "vi": "Hợp đồng quản lý nghệ sĩ không công bằng có thể báo cáo Ủy ban công bằng cạnh tranh",
                    "situation": "formal"
                }
            ],
            "relatedTerms": ["전속계약", "표준계약서", "노예계약", "공정위"]
        },
        {
            "slug": "hop-dong-nghe-si",
            "korean": "연예인계약",
            "vietnamese": "Hợp đồng nghệ sĩ",
            "hanja": "演藝人契約",
            "hanjaReading": "演(베풀 연) + 藝(재주 예) + 人(사람 인) + 契(맺을 계) + 約(약속할 약)",
            "pronunciation": "연예인계약",
            "meaningKo": "연예인과 기획사 간의 전속계약으로, 활동 범위·수익 배분·계약 기간을 규정합니다. 통역 시 한국은 계약 기간 상한이 7년으로 권고되며, 수익 배분은 5:5~7:3이 일반적이고, 계약 해지 시 위약금이 수억~수십억 원이며, 표준계약서 사용이 권장되고, 불공정 조항은 무효라는 점을 명확히 전달해야 합니다.",
            "meaningVi": "Hợp đồng độc quyền giữa nghệ sĩ và công ty, quy định phạm vi hoạt động, phân chia lợi nhuận, thời hạn hợp đồng. Ở Hàn Quốc thời hạn hợp đồng khuyến cáo tối đa 7 năm, phân chia lợi nhuận thường 5:5 đến 7:3, chấm dứt hợp đồng phạt vi phạm từ vài trăm triệu đến hàng chục tỷ won, khuyến khích dùng hợp đồng tiêu chuẩn, điều khoản không công bằng vô hiệu.",
            "context": "연예인 계약 협상 및 분쟁 조정 상황에서 사용",
            "culturalNote": "한국 연예계는 전속계약이 일반적이며, 과거 불공정 계약으로 사회 문제가 되었습니다. 동방신기·JYJ·EXO 등 분쟁이 있었고, 공정위가 표준계약서를 제정하여 개선되었습니다. 최근 수익 배분이 연예인에게 유리하게 변화하고 있습니다. 베트남은 계약 관행이 미비해 통역 시 한국의 표준을 설명해야 합니다.",
            "commonMistakes": [
                {
                    "mistake": "hợp đồng biểu diễn",
                    "correction": "hợp đồng nghệ sĩ (전속계약)",
                    "explanation": "'공연 계약'은 개별 공연만 의미하며 전속계약의 포괄성이 누락됩니다"
                },
                {
                    "mistake": "hợp đồng độc quyền",
                    "correction": "hợp đồng nghệ sĩ (연예인 특화)",
                    "explanation": "'독점계약'은 일반 계약이며 연예인 계약의 특수성이 약화됩니다"
                },
                {
                    "mistake": "ký với công ty giải trí",
                    "correction": "hợp đồng nghệ sĩ (법적 문서)",
                    "explanation": "'연예기획사와 계약'은 행위이며 계약서 자체를 지칭하지 못합니다"
                }
            ],
            "examples": [
                {
                    "ko": "이 가수는 계약 기간 7년에 수익 6:4 배분으로 계약했습니다",
                    "vi": "Ca sĩ này ký hợp đồng 7 năm với phân chia lợi nhuận 6:4",
                    "situation": "formal"
                },
                {
                    "ko": "계약 중간에 해지하면 위약금 내야 하나요?",
                    "vi": "Chấm dứt giữa chừng hợp đồng có phải nộp phạt vi phạm không?",
                    "situation": "onsite"
                },
                {
                    "ko": "연예인계약은 표준계약서를 사용하면 분쟁을 줄일 수 있습니다",
                    "vi": "Hợp đồng nghệ sĩ dùng hợp đồng tiêu chuẩn có thể giảm tranh chấp",
                    "situation": "formal"
                }
            ],
            "relatedTerms": ["전속계약", "수익배분", "위약금", "표준계약서"]
        },
        {
            "slug": "quyen-nhan-cach-tac-gia",
            "korean": "저작인격권",
            "vietnamese": "Quyền nhân cách tác giả",
            "hanja": "著作人格權",
            "hanjaReading": "著(나타날 저) + 作(지을 작) + 人(사람 인) + 格(격식 격) + 權(권리 권)",
            "pronunciation": "저작인격권",
            "meaningKo": "저작물을 창작한 저작자의 인격적 이익을 보호하는 권리로, 공표권·성명표시권·동일성유지권을 포함합니다. 통역 시 저작재산권과 달리 양도·상속 불가능하며, 저작자 사후에도 보호되고, 무단 개작·변형은 침해이며, 연예인의 공연·음원도 보호 대상이고, 침해 시 형사처벌(5년 이하 징역)이 가능하다는 점을 명확히 전달해야 합니다.",
            "meaningVi": "Quyền bảo vệ lợi ích nhân cách của tác giả sáng tạo tác phẩm, bao gồm quyền công bố, quyền ghi tên, quyền duy trì đồng nhất. Khác với quyền tài sản tác giả không thể chuyển nhượng và thừa kế, được bảo vệ cả sau khi tác giả mất, sửa/biến dạng không phép là vi phạm, biểu diễn và âm nhạc của nghệ sĩ cũng là đối tượng bảo vệ, vi phạm có thể bị xử phạt hình sự (tù 5 năm).",
            "context": "저작인격권 침해 소송 및 권리 보호 상황에서 사용",
            "culturalNote": "한국은 저작인격권을 강력히 보호하며, 무단 개작·왜곡은 형사처벌 대상입니다. 연예인의 공연 영상을 편집·변형하는 것도 침해이며, AI로 목소리·얼굴을 합성하는 딥페이크도 침해입니다. 베트남은 저작인격권 개념이 약해 통역 시 한국의 강력한 보호를 설명해야 합니다.",
            "commonMistakes": [
                {
                    "mistake": "quyền tác giả",
                    "correction": "quyền nhân cách tác giả (인격권) vs quyền tác giả (전체)",
                    "explanation": "'저작권'은 포괄적이며 인격권과 재산권을 구분해야 합니다"
                },
                {
                    "mistake": "danh dự tác giả",
                    "correction": "quyền nhân cách tác giả (법적 권리)",
                    "explanation": "'작가 명예'는 일반 개념이며 법적 권리로서의 인격권과 다릅니다"
                },
                {
                    "mistake": "bản quyền cá nhân",
                    "correction": "quyền nhân cách tác giả (저작인격권)",
                    "explanation": "'개인 저작권'은 모호하며 저작인격권의 구체적 의미가 누락됩니다"
                }
            ],
            "examples": [
                {
                    "ko": "이 소설을 무단으로 각색하여 드라마로 만드는 것은 저작인격권 침해입니다",
                    "vi": "Chuyển thể tiểu thuyết này thành phim không phép là vi phạm quyền nhân cách tác giả",
                    "situation": "formal"
                },
                {
                    "ko": "내 작품을 마음대로 수정해도 되나요?",
                    "vi": "Tự ý sửa tác phẩm của tôi được không?",
                    "situation": "onsite"
                },
                {
                    "ko": "저작인격권은 저작자 사후에도 보호됩니다",
                    "vi": "Quyền nhân cách tác giả được bảo vệ cả sau khi tác giả mất",
                    "situation": "formal"
                }
            ],
            "relatedTerms": ["저작재산권", "공표권", "성명표시권", "동일성유지권"]
        },
        {
            "slug": "luat-bieu-dien",
            "korean": "공연법",
            "vietnamese": "Luật biểu diễn",
            "hanja": "公演法",
            "hanjaReading": "公(공평할 공) + 演(베풀 연) + 法(법 법)",
            "pronunciation": "공연법",
            "meaningKo": "공연의 허가·신고·안전·질서를 규율하는 법률로, 공연장 안전 기준과 관람객 보호를 규정합니다. 통역 시 한국은 대규모 공연은 사전 신고가 필요하며, 공연장 안전 점검이 의무화되고, 티켓 환불 규정이 있으며, 무허가 공연 시 과태료, 안전사고 시 형사처벌이 가능하다는 점을 명확히 전달해야 합니다.",
            "meaningVi": "Luật quy định cấp phép, khai báo, an toàn, trật tự biểu diễn, quy định tiêu chuẩn an toàn nhà hát và bảo vệ khán giả. Ở Hàn Quốc biểu diễn quy mô lớn phải khai báo trước, kiểm tra an toàn nhà hát bắt buộc, có quy định hoàn vé, biểu diễn không phép bị phạt tiền hành chính, tai nạn an toàn có thể bị xử lý hình sự.",
            "context": "공연 신고 및 안전 관리 상황에서 사용",
            "culturalNote": "한국은 대형 콘서트·뮤지컬이 활발하며, 공연법으로 안전을 관리합니다. 세월호 참사(2014) 이후 안전 규제가 강화되었고, 이태원 참사(2022)로 더욱 엄격해졌습니다. 티켓 환불은 공연 7일 전까지 가능하며, 공연 취소 시 전액 환불됩니다. 베트남은 공연법이 미비해 통역 시 한국의 체계를 설명해야 합니다.",
            "commonMistakes": [
                {
                    "mistake": "luật ca nhạc",
                    "correction": "luật biểu diễn (포괄적)",
                    "explanation": "'음악법'은 음악만 의미하며 연극·뮤지컬·무용이 누락됩니다"
                },
                {
                    "mistake": "quy định sân khấu",
                    "correction": "luật biểu diễn (법률)",
                    "explanation": "'무대 규정'은 행정규칙처럼 들리며 법률의 지위가 약화됩니다"
                },
                {
                    "mistake": "luật tổ chức sự kiện",
                    "correction": "luật biểu diễn (공연 특화)",
                    "explanation": "'이벤트 조직법'은 일반 행사이며 공연의 특수성이 누락됩니다"
                }
            ],
            "examples": [
                {
                    "ko": "1만 명 이상 콘서트는 공연법에 따라 사전 신고해야 합니다",
                    "vi": "Concert trên 10,000 người phải khai báo trước theo Luật biểu diễn",
                    "situation": "formal"
                },
                {
                    "ko": "공연 취소되면 환불받을 수 있나요?",
                    "vi": "Nếu hủy biểu diễn có được hoàn tiền không?",
                    "situation": "onsite"
                },
                {
                    "ko": "공연장 안전 점검을 소홀히 하면 형사처벌을 받습니다",
                    "vi": "Sơ suất kiểm tra an toàn nhà hát sẽ bị xử lý hình sự",
                    "situation": "formal"
                }
            ],
            "relatedTerms": ["공연신고", "공연장안전", "티켓환불", "과태료"]
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
    print(f"✅ Added {len(filtered)} terms (스포츠/엔터법). Total: {len(data)}")

if __name__ == '__main__':
    main()
