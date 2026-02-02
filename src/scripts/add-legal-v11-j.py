#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Legal Domain Terms - Batch 11J: Sports Law/Entertainment Law
스포츠법/엔터테인먼트법 관련 전문용어 10개 추가

Theme: Sports Law, Entertainment Law, Athlete Contracts, Media Rights
"""

import json
import os

# 스크립트의 절대 경로 기준으로 legal.json 경로 설정
SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
PROJECT_ROOT = os.path.dirname(os.path.dirname(SCRIPT_DIR))
JSON_FILE = os.path.join(PROJECT_ROOT, "src", "data", "terms", "legal.json")

# 추가할 10개 용어 (Tier S 기준)
NEW_TERMS = [
    {
        "slug": "hop-dong-chuyen-nhuong-cau-thu",
        "korean": "선수 이적 계약",
        "vietnamese": "Hợp đồng chuyển nhượng cầu thủ",
        "hanja": "選手移籍契約",
        "hanjaReading": "選(가릴 선) + 手(손 수) + 移(옮길 이) + 籍(문서 적) + 契(맺을 계) + 約(맺을 약)",
        "pronunciation": "선수 이적 계약",
        "meaningKo": "프로 스포츠에서 선수가 한 구단에서 다른 구단으로 이적할 때 체결하는 계약으로, 이적료, 연봉, 계약 기간, 성과 보너스, 바이아웃 조항 등을 포함합니다. 통역 시 베트남에서는 축구 이적 시장이 활발하므로 'phí chuyển nhượng'(이적료)와 'lương cơ bản'(기본급)의 구분을 명확히 해야 하며, 한국의 FA 제도와 베트남의 자유계약 시스템 차이를 설명할 수 있어야 합니다. 특히 유소년 선수 이적 시 FIFA 규정에 따른 제한사항을 정확히 전달하는 것이 중요합니다.",
        "meaningVi": "Hợp đồng được ký kết khi một cầu thủ chuyển từ câu lạc bộ này sang câu lạc bộ khác, bao gồm phí chuyển nhượng, mức lương, thời hạn hợp đồng, thưởng thành tích và các điều khoản mua đứt. Trong thực tế, cần phân biệt rõ giữa 'phí chuyển nhượng' (số tiền câu lạc bộ mới trả cho câu lạc bộ cũ) và 'mức lương' (số tiền cầu thủ nhận được). Đặc biệt quan trọng là các quy định FIFA về chuyển nhượng cầu thủ trẻ dưới 18 tuổi.",
        "context": "스포츠법, 프로스포츠 계약, 선수 이적 협상, 에이전트 업무",
        "culturalNote": "한국의 프로스포츠는 KBO(야구), K리그(축구), KBL(농구) 등 리그별로 이적 규정이 다르며 FA 제도가 확립되어 있습니다. 베트남은 V리그(축구)를 중심으로 이적 시장이 형성되어 있으나 한국보다 시장 규모가 작고 이적료 수준이 낮습니다. 통역 시 양국의 리그 시스템, 선수 연봉 수준, 이적 시장 관행의 차이를 고려해야 하며, 특히 동남아시아 지역 내 선수 이동이 활발한 베트남의 특성을 이해해야 합니다.",
        "commonMistakes": [
            {
                "mistake": "'이적료'를 'lương chuyển nhượng'로 번역",
                "correction": "'phí chuyển nhượng' 또는 'giá chuyển nhượng'로 표현",
                "explanation": "이적료는 구단 간 거래 금액이지 선수 개인의 급여가 아니므로 'lương'(급여) 대신 'phí'(비용)를 사용해야 합니다."
            },
            {
                "mistake": "'FA(자유계약선수)'를 그대로 'FA'로 표현",
                "correction": "'cầu thủ tự do' 또는 'free agent'로 설명",
                "explanation": "베트남에서는 FA 제도가 한국처럼 체계화되지 않았으므로 개념을 설명하는 것이 필요합니다."
            },
            {
                "mistake": "'바이아웃 조항'을 직역하여 혼란 초래",
                "correction": "'điều khoản mua đứt hợp đồng' 또는 'phí phá vỡ hợp đồng'로 설명",
                "explanation": "바이아웃은 계약 해지를 위해 지불하는 위약금 개념으로, 베트남 축구에서도 이해 가능한 용어로 풀어 설명해야 합니다."
            }
        ],
        "examples": [
            {
                "ko": "이번 이적 계약에는 300억 원의 이적료와 연봉 150억 원이 포함되어 있으며, 성과 보너스 조항도 명시되어 있습니다.",
                "vi": "Hợp đồng chuyển nhượng này bao gồm phí chuyển nhượng 30 triệu USD, mức lương 15 triệu USD mỗi năm, và có ghi rõ điều khoản thưởng thành tích.",
                "situation": "formal"
            },
            {
                "ko": "선수가 계약 기간 중 이적을 원할 경우 바이아웃 조항에 따라 500억 원을 지불해야 합니다.",
                "vi": "Nếu cầu thủ muốn chuyển nhượng trong thời gian hợp đồng, phải trả phí phá vỡ hợp đồng là 50 triệu USD theo điều khoản mua đứt.",
                "situation": "formal"
            },
            {
                "ko": "이적 협상 시 선수 에이전트가 개입하여 계약 조건을 조율했습니다.",
                "vi": "Trong đàm phán chuyển nhượng, đại diện của cầu thủ đã tham gia để điều chỉnh các điều khoản hợp đồng.",
                "situation": "onsite"
            }
        ],
        "relatedTerms": ["계약 해지", "성과 보너스", "초상권", "에이전트 수수료"]
    },
    {
        "slug": "ban-quyen-truyen-hinh",
        "korean": "방송 중계권",
        "vietnamese": "Bản quyền truyền hình",
        "hanja": "放送中繼權",
        "hanjaReading": "放(놓을 방) + 送(보낼 송) + 中(가운데 중) + 繼(이을 계) + 權(권세 권)",
        "pronunciation": "방송 중계권",
        "meaningKo": "스포츠 경기나 엔터테인먼트 콘텐츠를 텔레비전, 인터넷, 모바일 등의 매체를 통해 중계할 수 있는 독점적 또는 비독점적 권리로, 지역별, 플랫폼별로 세분화되며 막대한 수익을 창출합니다. 통역 시 한국의 지상파(KBS, MBC, SBS)와 케이블(SPOTV 등) 방송사 간의 중계권 경쟁, 그리고 OTT 플랫폼(네이버, 쿠팡플레이)의 부상을 설명할 수 있어야 하며, 베트남에서는 VTV(국영방송)의 독점적 지위와 지역 케이블 채널의 역할을 이해해야 합니다. 특히 국제 스포츠 대회의 경우 FIFA, IOC 등 국제기구의 중계권 정책을 정확히 전달하는 것이 중요합니다.",
        "meaningVi": "Quyền độc quyền hoặc không độc quyền để phát sóng trực tiếp các sự kiện thể thao hoặc nội dung giải trí qua truyền hình, internet, và thiết bị di động. Bản quyền này được phân chia theo khu vực địa lý và nền tảng phát sóng, tạo ra nguồn doanh thu khổng lồ. Ở Việt Nam, VTV (đài truyền hình quốc gia) thường nắm giữ bản quyền các sự kiện thể thao lớn, trong khi các kênh truyền hình cáp và nền tảng OTT đang ngày càng tham gia mua bản quyền các giải đấu quốc tế.",
        "context": "스포츠법, 미디어법, 콘텐츠 산업, 스포츠 마케팅",
        "culturalNote": "한국은 프로야구, 프로축구, 프로농구 등 국내 리그의 중계권이 체계적으로 관리되며, 최근 OTT 플랫폼이 적극적으로 중계권을 확보하고 있습니다. 베트남은 VTV가 국가 대표팀 경기와 주요 국제 대회 중계권을 독점하는 경향이 있으며, K리그나 프리미어리그 같은 해외 리그는 케이블 채널이나 온라인 플랫폼을 통해 방송됩니다. 통역 시 양국의 방송 시장 구조, 중계권료 수준, 시청자 선호도 차이를 고려해야 하며, 베트남 축구 대표팀 경기는 국민적 관심사임을 이해해야 합니다.",
        "commonMistakes": [
            {
                "mistake": "'중계권'을 단순히 'quyền phát sóng'로만 표현",
                "correction": "'bản quyền truyền hình' 또는 'quyền phát sóng trực tiếp'로 명확히 표현",
                "explanation": "중계권은 단순 방송권이 아닌 실시간 생중계 권리를 의미하므로 'trực tiếp'(직접)을 포함해야 합니다."
            },
            {
                "mistake": "'독점 중계권'과 '비독점 중계권' 구분 없이 표현",
                "correction": "'bản quyền độc quyền'과 'bản quyền không độc quyền'으로 구분",
                "explanation": "독점 여부는 계약 조건과 금액에 큰 영향을 미치므로 명확히 구분해야 합니다."
            },
            {
                "mistake": "'OTT 플랫폼'을 설명 없이 사용",
                "correction": "'nền tảng OTT (over-the-top)' 또는 'nền tảng phát trực tuyến'으로 설명",
                "explanation": "베트남에서는 OTT 개념이 덜 보편화되어 있으므로 풀어서 설명하는 것이 좋습니다."
            }
        ],
        "examples": [
            {
                "ko": "국내 프로야구 10년간 독점 방송 중계권을 3,000억 원에 계약했습니다.",
                "vi": "Đã ký hợp đồng bản quyền truyền hình độc quyền bóng chày chuyên nghiệp trong nước trong 10 năm với giá 300 triệu USD.",
                "situation": "formal"
            },
            {
                "ko": "이번 월드컵 중계권은 지상파 3사가 공동으로 확보했으며, OTT 플랫폼에도 부분 중계권이 판매되었습니다.",
                "vi": "Bản quyền World Cup lần này được 3 đài truyền hình mặt đất liên kết mua, và một phần bản quyền cũng được bán cho các nền tảng phát trực tuyến.",
                "situation": "formal"
            },
            {
                "ko": "중계권 협상에서 모바일 스트리밍 권리가 핵심 쟁점이었습니다.",
                "vi": "Trong đàm phán bản quyền, quyền phát trực tuyến trên thiết bị di động là vấn đề then chốt.",
                "situation": "onsite"
            }
        ],
        "relatedTerms": ["초상권", "저작권", "스폰서십", "PPV(유료 중계)"]
    },
    {
        "slug": "cho-sang-quyen-su-dung-hinh-anh",
        "korean": "초상권",
        "vietnamese": "Chân dung quyền / Quyền sử dụng hình ảnh",
        "hanja": "肖像權",
        "hanjaReading": "肖(닮을 초) + 像(형상 상) + 權(권세 권)",
        "pronunciation": "초상권",
        "meaningKo": "개인의 얼굴, 모습, 성명, 음성 등 개인을 식별할 수 있는 특징을 상업적 또는 공적 목적으로 사용할 수 있는 권리로, 연예인, 운동선수, 공인의 경우 재산권적 가치가 매우 큽니다. 통역 시 한국에서는 초상권 침해 소송이 빈번하며 특히 SNS상의 무단 사용이 문제되는 경우가 많고, 베트남에서도 유명인의 이미지 도용이 법적 분쟁으로 이어질 수 있음을 설명해야 합니다. 초상권 계약 시 사용 기간, 매체, 지역 범위를 명확히 해야 하며, 특히 AI 딥페이크 기술로 인한 초상권 침해 우려가 증가하고 있음을 주의해야 합니다.",
        "meaningVi": "Quyền được kiểm soát việc sử dụng khuôn mặt, hình ảnh, tên tuổi, giọng nói và các đặc điểm nhận diện cá nhân cho mục đích thương mại hoặc công cộng. Đối với người nổi tiếng, vận động viên, quyền này có giá trị tài sản rất lớn. Ở Việt Nam, việc sử dụng hình ảnh người nổi tiếng trái phép trên mạng xã hội hoặc quảng cáo đang ngày càng dẫn đến tranh chấp pháp lý. Khi ký hợp đồng quyền sử dụng hình ảnh, cần ghi rõ thời hạn, phương tiện truyền thông, và phạm vi địa lý.",
        "context": "엔터테인먼트법, 광고 계약, 스포츠 마케팅, 개인정보보호",
        "culturalNote": "한국은 연예인의 초상권 보호가 강력하며, CF(광고) 계약 시 초상권 사용료가 수억 원에 달하는 경우가 많습니다. 베트남도 최근 연예계가 성장하면서 초상권 인식이 높아졌으나 한국만큼 체계적이지 않습니다. 통역 시 한국의 CF 계약 관행(전속 모델, 단발 모델), 초상권 분쟁 판례, 그리고 베트남의 광고 시장에서 K-pop 스타들의 초상권 활용 사례를 이해해야 합니다. 특히 SNS 시대에 무단 도용 문제가 심각하므로 디지털 환경에서의 초상권 보호 방안을 설명할 수 있어야 합니다.",
        "commonMistakes": [
            {
                "mistake": "'초상권'을 'quyền chân dung'로만 번역",
                "correction": "'quyền sử dụng hình ảnh' 또는 'quyền hình ảnh cá nhân'로 보충 설명",
                "explanation": "'chân dung quyền'은 문어체이고 일반인에게 생소하므로 '이미지 사용권'이라는 실용적 표현을 병행해야 합니다."
            },
            {
                "mistake": "초상권 침해와 저작권 침해를 혼동",
                "correction": "초상권은 인물 이미지, 저작권은 창작물에 대한 권리로 명확히 구분",
                "explanation": "사진 속 인물의 초상권과 사진 자체의 저작권은 별개이므로 구분해서 설명해야 합니다."
            },
            {
                "mistake": "'퍼블리시티권'을 설명 없이 사용",
                "correction": "'quyền công khai' 또는 '상업적 초상권'으로 풀어서 설명",
                "explanation": "퍼블리시티권은 초상권의 재산권적 측면으로, 베트남에서는 별도 용어가 확립되지 않았습니다."
            }
        ],
        "examples": [
            {
                "ko": "이 광고 모델 계약에는 1년간 국내 TV, 온라인, 인쇄 매체에 대한 초상권 사용이 포함되며, 계약료는 10억 원입니다.",
                "vi": "Hợp đồng người mẫu quảng cáo này bao gồm quyền sử dụng hình ảnh trên TV trong nước, trực tuyến và phương tiện in ấn trong 1 năm, với mức phí 1 triệu USD.",
                "situation": "formal"
            },
            {
                "ko": "SNS에 유명인의 사진을 무단으로 게시하여 초상권 침해로 고소당했습니다.",
                "vi": "Đã bị kiện vi phạm quyền hình ảnh vì đăng ảnh người nổi tiếng trên mạng xã hội mà không được phép.",
                "situation": "formal"
            },
            {
                "ko": "선수의 초상권 수익은 구단과 7:3으로 배분하기로 계약했습니다.",
                "vi": "Hợp đồng quy định doanh thu từ quyền hình ảnh của cầu thủ sẽ được chia 70% cho cầu thủ và 30% cho câu lạc bộ.",
                "situation": "onsite"
            }
        ],
        "relatedTerms": ["저작권", "퍼블리시티권", "개인정보보호", "광고 계약"]
    },
    {
        "slug": "hop-dong-tai-tro-the-thao",
        "korean": "스폰서십 계약",
        "vietnamese": "Hợp đồng tài trợ thể thao",
        "hanja": None,
        "hanjaReading": None,
        "pronunciation": "스폰서십 계약",
        "meaningKo": "기업이 스포츠 팀, 선수, 대회 등에 자금이나 물품을 지원하고 그 대가로 브랜드 노출, 마케팅 권리, 티켓 할당 등의 혜택을 받는 계약으로, 네이밍 라이트, 유니폼 광고, 경기장 내 광고판 등 다양한 형태가 있습니다. 통역 시 한국의 대기업 스포츠 스폰서십 관행(삼성 라이온즈, SK 와이번스 등 기업 구단), 베트남의 주요 기업(Viettel, Vinamilk) 스포츠 마케팅 전략을 이해해야 하며, 스폰서 로고 노출 시간, 위치, 크기 등 세부 조건이 계약 금액에 미치는 영향을 설명할 수 있어야 합니다. 특히 국제 대회 스폰서는 IOC, FIFA 등의 엄격한 규정을 준수해야 합니다.",
        "meaningVi": "Hợp đồng mà doanh nghiệp cung cấp tiền hoặc hàng hóa cho đội thể thao, vận động viên, hoặc giải đấu, và đổi lại nhận được quyền quảng bá thương hiệu, quyền marketing, phân bổ vé và các quyền lợi khác. Có nhiều hình thức như quyền đặt tên (naming rights), quảng cáo trên áo đấu, bảng quảng cáo trong sân. Ở Việt Nam, các tập đoàn lớn như Viettel, Vinamilk thường tài trợ cho các đội tuyển quốc gia và giải đấu trong nước, trong khi các thương hiệu quốc tế tài trợ cho giải đấu khu vực.",
        "context": "스포츠 마케팅, 광고법, 기업 홍보, 계약 협상",
        "culturalNote": "한국은 기업이 직접 프로스포츠 구단을 소유하는 전통이 있어(삼성, SK, LG 등) 스폰서십이 소유권과 결합된 경우가 많습니다. 베트남은 국영 기업(Viettel)이나 대기업(Vingroup)이 스포츠팀을 후원하지만 한국처럼 기업명을 구단명에 사용하는 경우는 적습니다. 통역 시 한국의 '타이틀 스폰서' 개념, 베트남의 국가 대표팀 후원 문화, 그리고 동남아시아 지역 내 스포츠 마케팅 트렌드를 이해해야 합니다. 특히 월드컵, 올림픽 같은 국제 대회는 앰부시 마케팅 금지 규정이 엄격합니다.",
        "commonMistakes": [
            {
                "mistake": "'스폰서'를 'nhà tài trợ'로만 표현하고 스폰서십의 상호 혜택 설명 누락",
                "correction": "'đối tác tài trợ'로 표현하고 쌍방 혜택 강조",
                "explanation": "스폰서십은 단순 기부가 아닌 상호 이익을 위한 전략적 파트너십이므로 이를 명확히 해야 합니다."
            },
            {
                "mistake": "'네이밍 라이트'를 직역하여 혼란 초래",
                "correction": "'quyền đặt tên' 또는 'quyền mang tên thương hiệu'로 설명",
                "explanation": "경기장이나 대회에 기업명을 붙이는 권리로, 구체적 예시와 함께 설명해야 합니다."
            },
            {
                "mistake": "'앰부시 마케팅'을 설명 없이 사용",
                "correction": "'marketing phục kích' 또는 '비공식 스폰서의 무단 마케팅'으로 설명",
                "explanation": "공식 스폰서가 아닌 기업이 대회를 이용해 마케팅하는 행위로, 금지 대상임을 명확히 해야 합니다."
            }
        ],
        "examples": [
            {
                "ko": "이번 프로축구 리그 타이틀 스폰서십 계약은 3년간 500억 원 규모입니다.",
                "vi": "Hợp đồng tài trợ chính (title sponsor) cho giải bóng đá chuyên nghiệp này trị giá 50 triệu USD trong 3 năm.",
                "situation": "formal"
            },
            {
                "ko": "경기장 네이밍 라이트 계약으로 향후 10년간 경기장 명칭에 기업명이 포함됩니다.",
                "vi": "Theo hợp đồng quyền đặt tên sân vận động, tên doanh nghiệp sẽ được gắn vào tên sân trong 10 năm tới.",
                "situation": "formal"
            },
            {
                "ko": "유니폼 가슴 스폰서 로고는 경기당 평균 90초 노출되어 높은 광고 효과를 냅니다.",
                "vi": "Logo nhà tài trợ trên ngực áo đấu được hiển thị trung bình 90 giây mỗi trận, mang lại hiệu quả quảng cáo cao.",
                "situation": "onsite"
            }
        ],
        "relatedTerms": ["방송 중계권", "광고 계약", "네이밍 라이트", "마케팅 권"]
    },
    {
        "slug": "dieu-khoan-cam-thi-dau",
        "korean": "출전 금지 조항",
        "vietnamese": "Điều khoản cấm thi đấu",
        "hanja": "出戰禁止條項",
        "hanjaReading": "出(날 출) + 戰(싸울 전) + 禁(금할 금) + 止(그칠 지) + 條(가지 조) + 項(항목 항)",
        "pronunciation": "출전 금지 조항",
        "meaningKo": "선수가 특정 기간 동안 경기에 출전할 수 없도록 하는 계약 조항 또는 징계 조치로, 도핑 위반, 폭력 행위, 승부조작 연루 등 심각한 규정 위반 시 부과되며, 기간은 경고부터 영구 제명까지 다양합니다. 통역 시 한국의 KBO(야구), K리그(축구) 등 리그별 징계 규정, 대한체육회와 국제경기연맹(FIFA, IOC)의 출전 정지 기준을 이해해야 하며, 베트남에서도 VFF(축구협회)의 징계 절차를 설명할 수 있어야 합니다. 특히 도핑 위반은 국제적으로 통일된 제재가 적용되므로 WADA 규정을 정확히 전달하는 것이 중요합니다.",
        "meaningVi": "Điều khoản hợp đồng hoặc biện pháp kỷ luật cấm vận động viên tham gia thi đấu trong một khoảng thời gian nhất định, được áp dụng khi vi phạm quy định nghiêm trọng như doping, bạo lực, hoặc dàn xếp tỷ số. Thời gian cấm thi đấu có thể từ vài trận đến cấm thi đấu vĩnh viễn. Ở Việt Nam, VFF (Liên đoàn Bóng đá Việt Nam) có quy định kỷ luật riêng, trong khi các vi phạm doping tuân theo tiêu chuẩn quốc tế WADA.",
        "context": "스포츠법, 선수 징계, 도핑 규제, 스포츠 윤리",
        "culturalNote": "한국은 스포츠 비리(승부조작, 도핑)에 대해 엄격한 제재를 가하며, 특히 프로야구와 축구에서 과거 대규모 승부조작 사건 이후 징계가 강화되었습니다. 베트남도 국제 대회 참가를 위해 도핑 규제를 강화하고 있으나, 선수 폭력이나 관중 난동에 대한 제재는 한국보다 느슨한 편입니다. 통역 시 양국의 스포츠 문화, 징계 수위, 그리고 국제 대회 출전 자격에 미치는 영향을 고려해야 하며, 선수의 경력과 수입에 치명적인 영향을 미치는 만큼 신중한 언어 선택이 필요합니다.",
        "commonMistakes": [
            {
                "mistake": "'출전 정지'와 '자격 정지'를 혼용",
                "correction": "'cấm thi đấu'(출전 금지)와 'đình chỉ tư cách'(자격 정지)로 구분",
                "explanation": "출전 정지는 경기 참가 금지, 자격 정지는 선수 등록 자체가 취소되는 더 강한 징계입니다."
            },
            {
                "mistake": "'도핑'을 'doping'으로만 표현",
                "correction": "'sử dụng chất cấm' 또는 'vi phạm doping'로 설명",
                "explanation": "베트남에서도 'doping'이 통하지만 '금지약물 사용'으로 풀어 설명하면 더 명확합니다."
            },
            {
                "mistake": "'영구 제명'을 '평생 금지'로 직역",
                "correction": "'cấm thi đấu vĩnh viễn' 또는 'truất quyền thi đấu'로 표현",
                "explanation": "'영구 제명'은 선수 자격을 박탈하는 가장 강력한 징계로, 법적 무게감이 있는 용어를 사용해야 합니다."
            }
        ],
        "examples": [
            {
                "ko": "도핑 검사 양성 반응으로 선수에게 2년간 출전 금지 처분이 내려졌습니다.",
                "vi": "Vận động viên bị cấm thi đấu 2 năm do có kết quả dương tính với chất cấm trong xét nghiệm doping.",
                "situation": "formal"
            },
            {
                "ko": "경기 중 폭력 행위로 6개월 출전 정지 및 벌금 5천만 원이 부과되었습니다.",
                "vi": "Do hành vi bạo lực trong trận đấu, cầu thủ bị cấm thi đấu 6 tháng và phạt tiền 50,000 USD.",
                "situation": "formal"
            },
            {
                "ko": "승부조작 연루 혐의로 영구 제명되어 더 이상 프로 리그에 출전할 수 없습니다.",
                "vi": "Do liên quan đến dàn xếp tỷ số, cầu thủ bị truất quyền thi đấu vĩnh viễn và không thể tham gia giải chuyên nghiệp nữa.",
                "situation": "formal"
            }
        ],
        "relatedTerms": ["도핑 검사", "징계 위원회", "승부조작", "선수 자격"]
    },
    {
        "slug": "hop-dong-sang-tac-noi-dung",
        "korean": "콘텐츠 제작 계약",
        "vietnamese": "Hợp đồng sáng tạo nội dung",
        "hanja": None,
        "hanjaReading": None,
        "pronunciation": "콘텐츠 제작 계약",
        "meaningKo": "영화, 드라마, 예능, 다큐멘터리 등 엔터테인먼트 콘텐츠를 제작하기 위해 제작사, 방송사, OTT 플랫폼, 출연진, 제작진 간에 체결하는 계약으로, 제작비, 저작권 귀속, 수익 배분, 2차 저작물 권리 등을 명시합니다. 통역 시 한국의 드라마 제작 시스템(외주 제작사와 방송사 관계), 넷플릭스·디즈니플러스 같은 글로벌 OTT의 한국 콘텐츠 투자 확대, 그리고 베트남의 로컬 콘텐츠 제작 환경(VTV 자체 제작, 외주 비율)을 이해해야 합니다. 특히 K-드라마의 해외 판권 수출이 주요 수익원이므로 해외 배급 조건을 정확히 전달하는 것이 중요합니다.",
        "meaningVi": "Hợp đồng được ký giữa nhà sản xuất, đài truyền hình, nền tảng OTT, diễn viên và đoàn làm phim để sản xuất nội dung giải trí như phim, phim truyền hình, chương trình giải trí, phim tài liệu. Hợp đồng quy định ngân sách sản xuất, quyền sở hữu bản quyền, phân chia doanh thu, và quyền sử dụng sản phẩm phái sinh. Ở Việt Nam, VTV thường tự sản xuất hoặc đặt hàng các công ty sản xuất nội dung, trong khi các nền tảng quốc tế như Netflix đang đầu tư mạnh vào nội dung gốc Việt Nam.",
        "context": "엔터테인먼트법, 방송법, 영상 산업, 저작권법",
        "culturalNote": "한국은 드라마, 예능 등 방송 콘텐츠 산업이 고도로 발달했으며, '한류' 덕분에 해외 판권 수출이 핵심 수익원입니다. 베트남은 VTV가 제작의 중심이며, 최근 Netflix가 베트남 오리지널 콘텐츠에 투자하면서 제작 환경이 변화하고 있습니다. 통역 시 한국의 제작비 규모(드라마 회당 5억~10억 원), 베트남의 제작비 수준, 그리고 양국 간 협업 드라마 제작 사례를 이해해야 합니다. 특히 출연료, 저작권 귀속, 넷플릭스 같은 글로벌 플랫폼의 독점 권리 등 민감한 조건을 정확히 전달해야 합니다.",
        "commonMistakes": [
            {
                "mistake": "'제작사'와 '방송사'를 혼동",
                "correction": "'nhà sản xuất'(제작사)와 'đài truyền hình'(방송사)로 명확히 구분",
                "explanation": "제작사는 콘텐츠를 만들고, 방송사는 이를 송출하는 역할로 구분됩니다."
            },
            {
                "mistake": "'2차 저작물'을 설명 없이 사용",
                "correction": "'sản phẩm phái sinh' 또는 '파생 상품(게임, 굿즈 등)'으로 설명",
                "explanation": "2차 저작물은 원작 기반 리메이크, 게임, 캐릭터 상품 등을 의미하므로 예시를 들어 설명해야 합니다."
            },
            {
                "mistake": "'OTT 독점 계약'의 의미를 충분히 설명하지 않음",
                "correction": "'hợp đồng độc quyền với OTT' - 다른 플랫폼 방송 금지 조건 명시",
                "explanation": "넷플릭스 독점 계약은 다른 곳에서 볼 수 없음을 의미하므로 이를 분명히 해야 합니다."
            }
        ],
        "examples": [
            {
                "ko": "이번 드라마 제작 계약은 총제작비 200억 원, 16부작으로 넷플릭스 독점 공개됩니다.",
                "vi": "Hợp đồng sản xuất phim truyền hình này có tổng ngân sách 20 triệu USD, gồm 16 tập, và được phát hành độc quyền trên Netflix.",
                "situation": "formal"
            },
            {
                "ko": "저작권은 제작사가 보유하되, 방송사는 국내 방송권을 5년간 독점합니다.",
                "vi": "Bản quyền thuộc về nhà sản xuất, nhưng đài truyền hình có quyền phát sóng độc quyền trong nước trong 5 năm.",
                "situation": "formal"
            },
            {
                "ko": "웹툰 원작의 드라마화 계약으로 원작자에게 수익의 10%가 배분됩니다.",
                "vi": "Theo hợp đồng chuyển thể webtoon thành phim truyền hình, tác giả gốc nhận 10% doanh thu.",
                "situation": "onsite"
            }
        ],
        "relatedTerms": ["저작권", "방송 중계권", "2차 저작물", "출연 계약"]
    },
    {
        "slug": "dieu-khoan-bao-mat-noi-dung",
        "korean": "콘텐츠 유출 방지 조항",
        "vietnamese": "Điều khoản bảo mật nội dung",
        "hanja": None,
        "hanjaReading": None,
        "pronunciation": "콘텐츠 유출 방지 조항",
        "meaningKo": "영화, 드라마, 음악 등 엔터테인먼트 콘텐츠가 공식 발매 전에 불법으로 유출되거나 무단 복제되는 것을 막기 위한 계약 조항으로, 출연진, 제작진, 협력사 등에게 비밀유지 의무를 부과하고 위반 시 손해배상 책임을 명시합니다. 통역 시 한국의 온라인 불법 다운로드 문제, 사전 녹화 방송의 스포일러 유출 우려, 그리고 베트남에서도 K-드라마의 불법 자막 유포가 심각한 문제임을 설명해야 합니다. 특히 넷플릭스 같은 글로벌 플랫폼은 DRM(디지털 저작권 관리) 기술을 적용하며, 계약 시 유출 방지 의무를 강조하는 추세입니다.",
        "meaningVi": "Điều khoản hợp đồng nhằm ngăn chặn việc nội dung giải trí như phim, phim truyền hình, âm nhạc bị rò rỉ hoặc sao chép trái phép trước khi phát hành chính thức. Điều khoản này áp đặt nghĩa vụ bảo mật cho diễn viên, đoàn làm phim, và các đối tác, đồng thời quy định trách nhiệm bồi thường thiệt hại nếu vi phạm. Ở Việt Nam, vấn đề phim Hàn Quốc bị phát tán phụ đề lậu và tải xuống bất hợp pháp rất nghiêm trọng, trong khi các nền tảng quốc tế như Netflix áp dụng công nghệ DRM để bảo vệ nội dung.",
        "context": "엔터테인먼트법, 저작권 보호, 비밀유지 계약, 사이버 보안",
        "culturalNote": "한국은 드라마·영화 사전 제작 방식이 늘면서 유출 방지가 중요해졌고, 최근 넷플릭스 오리지널 한국 콘텐츠의 글로벌 인기로 유출 시 손실이 막대합니다. 베트남은 온라인 해적판 시장이 크고, 공식 OTT 가입률이 낮아 불법 다운로드가 만연합니다. 통역 시 한국의 엄격한 저작권 보호 법규(저작권법, 정보통신망법), 베트남의 불법 복제 단속 현황, 그리고 국제 협력(INTERPOL, 국경 간 저작권 보호)을 이해해야 합니다. 특히 스포일러 유출도 계약 위반으로 간주될 수 있음을 명확히 해야 합니다.",
        "commonMistakes": [
            {
                "mistake": "'유출'을 단순히 'rò rỉ'로만 표현",
                "correction": "'rò rỉ nội dung' 또는 'phát tán trái phép'로 구체화",
                "explanation": "'유출'은 의도적 배포와 실수로 인한 노출을 모두 포함하므로 맥락에 따라 표현을 달리해야 합니다."
            },
            {
                "mistake": "'스포일러'를 'spoiler'로만 사용",
                "correction": "'tiết lộ nội dung trước' 또는 '줄거리 누설'로 설명",
                "explanation": "베트남에서도 'spoiler'가 통하지만 계약상 법적 의미를 명확히 하려면 풀어 설명해야 합니다."
            },
            {
                "mistake": "'DRM'을 설명 없이 사용",
                "correction": "'công nghệ quản lý bản quyền số (DRM)'로 설명",
                "explanation": "DRM은 기술적 보호조치로, 일반인에게 생소하므로 '디지털 복사 방지 기술'로 풀어야 합니다."
            }
        ],
        "examples": [
            {
                "ko": "모든 출연진과 제작진은 촬영 현장 사진 및 대본 내용을 외부에 공개하지 않기로 서약했습니다.",
                "vi": "Toàn bộ diễn viên và đoàn làm phim đã cam kết không tiết lộ ảnh hiện trường quay và nội dung kịch bản ra bên ngoài.",
                "situation": "formal"
            },
            {
                "ko": "사전 녹화 방송의 결과가 유출될 경우 위반자에게 5억 원의 손해배상이 청구됩니다.",
                "vi": "Nếu kết quả của chương trình ghi hình trước bị rò rỉ, người vi phạm sẽ phải bồi thường 500,000 USD.",
                "situation": "formal"
            },
            {
                "ko": "넷플릭스는 DRM 기술로 콘텐츠를 보호하며, 불법 다운로드 발견 시 법적 조치를 취합니다.",
                "vi": "Netflix bảo vệ nội dung bằng công nghệ DRM và sẽ có biện pháp pháp lý nếu phát hiện tải xuống bất hợp pháp.",
                "situation": "onsite"
            }
        ],
        "relatedTerms": ["저작권", "비밀유지 계약", "불법 복제", "스포일러"]
    },
    {
        "slug": "hop-dong-quan-ly-nghe-si",
        "korean": "연예인 매니지먼트 계약",
        "vietnamese": "Hợp đồng quản lý nghệ sĩ",
        "hanja": "演藝人-契約",
        "hanjaReading": "演(놀 연) + 藝(재주 예) + 人(사람 인) + 契(맺을 계) + 約(맺을 약)",
        "pronunciation": "연예인 매니지먼트 계약",
        "meaningKo": "연예인이 기획사에 소속되어 활동하는 동안 기획사가 스케줄 관리, 홍보, 계약 중개 등을 담당하고 그 대가로 수익을 배분받는 계약으로, 전속 기간, 수익 배분율, 투자금 회수, 위약금 등을 명시하며, 한국에서는 '노예 계약' 논란으로 공정성 강화가 이뤄지고 있습니다. 통역 시 한국의 아이돌 연습생 시스템, 데뷔 전 투자비(수억 원), 7:3 또는 6:4 같은 수익 배분 관행, 그리고 베트남의 연예 기획사 시스템(덜 체계적)을 설명해야 합니다. 특히 계약 기간이 지나치게 길거나 수익 배분이 불공정하면 법적 분쟁으로 이어질 수 있으므로 공정거래위원회 가이드라인을 참고해야 합니다.",
        "meaningVi": "Hợp đồng mà nghệ sĩ gia nhập công ty giải trí, và công ty chịu trách nhiệm quản lý lịch trình, quảng bá, và môi giới hợp đồng, đổi lại được chia sẻ doanh thu. Hợp đồng ghi rõ thời hạn độc quyền, tỷ lệ phân chia doanh thu, thu hồi chi phí đầu tư, và phí vi phạm hợp đồng. Ở Hàn Quốc, do tranh cãi về 'hợp đồng nô lệ', các quy định về công bằng đã được tăng cường. Ở Việt Nam, hệ thống công ty giải trí còn kém phát triển hơn, và tỷ lệ chia sẻ doanh thu thường được thương lượng linh hoạt.",
        "context": "엔터테인먼트법, 노동법, 공정거래, 연예계 관행",
        "culturalNote": "한국은 K-pop 아이돌 중심의 체계적인 기획사 시스템(SM, JYP, YG, HYBE)이 있으며, 연습생 때부터 수년간 투자하고 데뷔 후 수익을 회수하는 구조입니다. 베트남은 기획사 개념이 약하고 개인 매니저나 소규모 에이전시가 관리하는 경우가 많습니다. 통역 시 한국의 '전속 계약' 기간(보통 7년), '투자금 회수' 조항, 그리고 베트남에서는 연예인이 더 독립적으로 활동하는 경향을 이해해야 합니다. 특히 '위약금' 분쟁이 빈번하므로 계약 해지 조건을 명확히 전달하는 것이 중요합니다.",
        "commonMistakes": [
            {
                "mistake": "'전속 계약'을 단순히 'hợp đồng độc quyền'로만 표현",
                "correction": "'hợp đồng quản lý toàn diện' 또는 '전속 매니지먼트 계약'으로 설명",
                "explanation": "전속 계약은 연예인의 모든 활동을 기획사가 관리한다는 의미로, 단순 독점 계약보다 포괄적입니다."
            },
            {
                "mistake": "'투자금 회수'를 '대출 상환'으로 오해",
                "correction": "'thu hồi chi phí đầu tư' - 기획사가 투자한 비용을 수익에서 차감하는 개념",
                "explanation": "투자금 회수는 대출이 아니라 데뷔 비용, 앨범 제작비 등을 수익에서 먼저 회수하는 것입니다."
            },
            {
                "mistake": "'노예 계약'을 직역하여 부정적 뉘앙스 과도",
                "correction": "'hợp đồng bất công' 또는 '불공정 계약'으로 순화",
                "explanation": "'노예 계약'은 언론 용어이므로 법률 통역에서는 중립적 표현을 사용해야 합니다."
            }
        ],
        "examples": [
            {
                "ko": "이 계약은 7년 전속 계약으로, 수익 배분은 기획사 7, 아티스트 3으로 하되, 3년 후 재협상 가능합니다.",
                "vi": "Hợp đồng này là hợp đồng độc quyền 7 năm, với tỷ lệ chia sẻ doanh thu là 70% cho công ty và 30% cho nghệ sĩ, có thể đàm phán lại sau 3 năm.",
                "situation": "formal"
            },
            {
                "ko": "데뷔 전 투자한 5억 원은 앨범 판매 및 공연 수익에서 우선 회수됩니다.",
                "vi": "Chi phí đầu tư 500,000 USD trước khi ra mắt sẽ được thu hồi ưu tiên từ doanh thu bán album và biểu diễn.",
                "situation": "formal"
            },
            {
                "ko": "계약 위반 시 위약금 10억 원이 부과되며, 이는 과도한 경우 법원에서 감액될 수 있습니다.",
                "vi": "Nếu vi phạm hợp đồng, phí vi phạm là 1 triệu USD, nhưng tòa án có thể giảm nếu thấy quá cao.",
                "situation": "onsite"
            }
        ],
        "relatedTerms": ["전속 계약", "수익 배분", "위약금", "초상권"]
    },
    {
        "slug": "kiem-duyet-noi-dung",
        "korean": "콘텐츠 심의",
        "vietnamese": "Kiểm duyệt nội dung",
        "hanja": "審議",
        "hanjaReading": "審(살필 심) + 議(의논할 의)",
        "pronunciation": "콘텐츠 심의",
        "meaningKo": "방송, 영화, 게임, 음악 등의 콘텐츠가 공개되기 전에 정부 기관이나 자율 심의 기구가 내용의 적법성, 윤리성, 연령 적합성을 평가하는 절차로, 한국은 방송통신심의위원회, 영상물등급위원회 등이 담당하며, 등급(전체 관람가, 12세, 15세, 청불 등)을 부여합니다. 통역 시 한국의 방송 심의 기준(폭력, 선정성, 욕설, 흡연 장면 등), 영화 등급 분류 체계, 그리고 베트남의 문화체육관광부(Bộ VHTTDL) 심의 절차를 이해해야 합니다. 특히 베트남은 정치적 내용에 대한 검열이 엄격하므로 양국의 심의 기준 차이를 명확히 전달해야 합니다.",
        "meaningVi": "Quy trình đánh giá tính hợp pháp, đạo đức và độ tuổi phù hợp của nội dung truyền hình, phim, game, âm nhạc trước khi phát hành, do cơ quan nhà nước hoặc tổ chức tự quản thực hiện. Ở Hàn Quốc, Ủy ban Kiểm duyệt Truyền thông và Ủy ban Phân loại Phim chịu trách nhiệm xếp hạng (mọi lứa tuổi, 12+, 15+, 19+). Ở Việt Nam, Bộ Văn hóa Thể thao và Du lịch thực hiện kiểm duyệt, và đặc biệt nghiêm ngặt với nội dung chính trị.",
        "context": "방송법, 영화법, 미디어 규제, 표현의 자유",
        "culturalNote": "한국은 민주적 심의 절차를 거치며 방송사 자율 심의가 먼저 이뤄지고, 사후 심의 시 과태료나 방송 정지가 가능합니다. 베트남은 사전 검열이 강하고, 특히 정치·종교·사회 비판 콘텐츠는 엄격히 통제됩니다. 통역 시 한국의 '등급 분류'(영화, 게임)와 베트남의 '검열'(censorship) 개념의 차이를 이해하고, 한국 콘텐츠를 베트남에 수출할 때 심의 통과 가능성을 사전에 검토해야 함을 설명할 수 있어야 합니다. 특히 K-드라마의 키스 신, 폭력 장면은 베트남에서 편집될 수 있습니다.",
        "commonMistakes": [
            {
                "mistake": "'심의'와 '검열'을 혼용",
                "correction": "'심의(kiểm duyệt)'는 등급 분류, '검열(kiểm duyệt chính trị)'은 내용 차단",
                "explanation": "한국은 '심의'(내용 평가 후 등급 부여), 베트남은 '검열'(부적절 내용 삭제·금지)에 가깝습니다."
            },
            {
                "mistake": "'청불'을 '18세 이상'으로 번역",
                "correction": "'19세 이상' 또는 '19+'로 정확히 표현",
                "explanation": "한국의 청소년관람불가는 만 19세 이상으로, 18세와는 다릅니다."
            },
            {
                "mistake": "베트남의 정치적 검열을 과소평가",
                "correction": "정치·종교·사회 비판 콘텐츠는 베트남에서 엄격히 통제됨을 명시",
                "explanation": "베트남은 표현의 자유가 제한적이므로 한국 콘텐츠 수출 시 주의가 필요합니다."
            }
        ],
        "examples": [
            {
                "ko": "이 드라마는 방송심의를 통과했으며 15세 이상 관람가 등급을 받았습니다.",
                "vi": "Phim truyền hình này đã qua kiểm duyệt và được xếp hạng dành cho khán giả từ 15 tuổi trở lên.",
                "situation": "formal"
            },
            {
                "ko": "폭력 장면이 과도하여 영상물등급위원회로부터 청불 등급을 받았습니다.",
                "vi": "Do cảnh bạo lực quá mức, phim đã nhận được xếp hạng 19+ từ Ủy ban Phân loại Phim.",
                "situation": "formal"
            },
            {
                "ko": "베트남 수출을 위해 일부 장면을 편집하여 재심의를 받았습니다.",
                "vi": "Để xuất khẩu sang Việt Nam, một số cảnh đã được chỉnh sửa và phim được kiểm duyệt lại.",
                "situation": "onsite"
            }
        ],
        "relatedTerms": ["등급 분류", "방송 규제", "표현의 자유", "콘텐츠 제작 계약"]
    },
    {
        "slug": "hop-dong-lien-ket-thuong-hieu",
        "korean": "브랜드 콜라보레이션 계약",
        "vietnamese": "Hợp đồng liên kết thương hiệu",
        "hanja": None,
        "hanjaReading": None,
        "pronunciation": "브랜드 콜라보레이션 계약",
        "meaningKo": "두 개 이상의 브랜드 또는 연예인과 브랜드가 협력하여 공동 제품을 개발하거나 공동 마케팅 캠페인을 진행하는 계약으로, 수익 배분, 브랜드 이미지 사용 권한, 협업 기간, 독점 조건 등을 명시합니다. 통역 시 한국의 K-pop 아이돌과 명품 브랜드 콜라보(BTS×루이비통, 블랙핑크×샤넬), 스포츠 브랜드와 스타 선수 시그니처 제품(손흥민×아디다스) 사례를 이해해야 하며, 베트남에서도 로컬 브랜드가 한류 스타를 활용한 콜라보를 시도하는 추세입니다. 특히 콜라보 제품의 수익 배분, 브랜드 이미지 손상 시 책임 소재를 명확히 하는 것이 중요합니다.",
        "meaningVi": "Hợp đồng hợp tác giữa hai hoặc nhiều thương hiệu, hoặc giữa người nổi tiếng và thương hiệu, để phát triển sản phẩm chung hoặc thực hiện chiến dịch marketing chung. Hợp đồng ghi rõ phân chia doanh thu, quyền sử dụng hình ảnh thương hiệu, thời hạn hợp tác, và điều kiện độc quyền. Ở Hàn Quốc, các idol K-pop thường hợp tác với thương hiệu xa xỉ (BTS×Louis Vuitton, BlackPink×Chanel), còn ở Việt Nam, các thương hiệu địa phương ngày càng hợp tác với ngôi sao Hàn Quốc để tăng sức hút.",
        "context": "마케팅법, 브랜드 전략, 엔터테인먼트 비즈니스, 라이선싱",
        "culturalNote": "한국은 한류 스타의 글로벌 영향력으로 해외 명품 브랜드와의 콜라보가 활발하며, 이는 브랜드와 스타 모두에게 윈윈입니다. 베트남은 한류 팬덤이 크지만 아직 대규모 콜라보는 적고, 주로 화장품, 패션 브랜드가 한국 스타를 광고 모델로 기용하는 수준입니다. 통역 시 '콜라보'와 '단순 광고 모델'의 차이(콜라보는 공동 개발), 수익 배분 구조, 그리고 브랜드 이미지 일치성(fit) 중요성을 설명할 수 있어야 합니다. 특히 명품 브랜드는 이미지 관리가 엄격하므로 스캔들 발생 시 계약 해지 조항을 포함합니다.",
        "commonMistakes": [
            {
                "mistake": "'콜라보'를 단순히 'hợp tác'으로만 표현",
                "correction": "'liên kết thương hiệu' 또는 'hợp tác phát triển sản phẩm chung'으로 구체화",
                "explanation": "콜라보는 단순 협력이 아닌 공동 창조이므로 이를 명확히 해야 합니다."
            },
            {
                "mistake": "콜라보와 광고 모델을 혼동",
                "correction": "콜라보는 제품 개발 참여, 광고 모델은 홍보만 담당으로 구분",
                "explanation": "콜라보는 기획 단계부터 참여하지만 광고 모델은 완성된 제품을 홍보합니다."
            },
            {
                "mistake": "'시그니처 제품'을 설명 없이 사용",
                "correction": "'sản phẩm mang dấu ấn cá nhân' 또는 '스타 전용 디자인 제품'으로 설명",
                "explanation": "시그니처 제품은 스타의 이름이나 스타일이 반영된 특별 제품임을 설명해야 합니다."
            }
        ],
        "examples": [
            {
                "ko": "이번 아이돌 그룹과 명품 브랜드의 콜라보는 한정판 가방 시리즈를 출시하며, 수익의 20%가 아티스트에게 배분됩니다.",
                "vi": "Hợp tác giữa nhóm idol và thương hiệu xa xỉ lần này sẽ ra mắt dòng túi giới hạn, với 20% doanh thu được chia cho nghệ sĩ.",
                "situation": "formal"
            },
            {
                "ko": "유명 축구 선수의 시그니처 축구화는 그의 등번호와 로고가 새겨진 특별 디자인입니다.",
                "vi": "Giày bóng đá mang dấu ấn của cầu thủ nổi tiếng có thiết kế đặc biệt với số áo và logo của anh ấy.",
                "situation": "onsite"
            },
            {
                "ko": "브랜드 이미지 손상 시 계약이 즉시 해지되며, 위약금 50억 원이 부과됩니다.",
                "vi": "Nếu hình ảnh thương hiệu bị tổn hại, hợp đồng sẽ chấm dứt ngay và phí vi phạm là 5 triệu USD.",
                "situation": "formal"
            }
        ],
        "relatedTerms": ["광고 계약", "초상권", "브랜드 라이선싱", "스폰서십"]
    }
]

def load_existing_terms():
    """기존 legal.json 파일 로드"""
    try:
        with open(JSON_FILE, 'r', encoding='utf-8') as f:
            data = json.load(f)
            if isinstance(data, dict) and "terms" in data:
                print("⚠️  WARNING: JSON has {\"terms\": [...]} structure")
                return data
            elif isinstance(data, list):
                return data
            else:
                print("❌ ERROR: Unexpected JSON structure")
                return []
    except FileNotFoundError:
        print(f"❌ ERROR: {JSON_FILE} not found")
        return []
    except json.JSONDecodeError as e:
        print(f"❌ ERROR: Invalid JSON - {e}")
        return []

def save_terms(terms):
    """FLAT ARRAY 형식으로 저장"""
    with open(JSON_FILE, 'w', encoding='utf-8') as f:
        json.dump(terms, f, ensure_ascii=False, indent=2)
    print(f"✅ Saved {len(terms)} terms to {JSON_FILE}")

def add_new_terms():
    """신규 용어 추가 (중복 체크)"""
    existing = load_existing_terms()
    existing_slugs = {term.get("slug") for term in existing}

    added_count = 0
    skipped_count = 0

    for term in NEW_TERMS:
        if term["slug"] in existing_slugs:
            print(f"⏭️  SKIP (duplicate): {term['slug']}")
            skipped_count += 1
        else:
            existing.append(term)
            print(f"✅ ADDED: {term['slug']} - {term['korean']}")
            added_count += 1

    if added_count > 0:
        save_terms(existing)

    print(f"\n📊 Summary: {added_count} added, {skipped_count} skipped, {len(existing)} total")

if __name__ == "__main__":
    print("=" * 60)
    print("Legal Domain - Batch 11J: Sports/Entertainment Law")
    print("스포츠법/엔터테인먼트법 전문용어 10개 추가")
    print("=" * 60)
    add_new_terms()
