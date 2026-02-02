#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""국제무역법 용어 추가 (v8-a)"""
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
            "slug": "to-chuc-thuong-mai-the-gioi",
            "korean": "세계무역기구",
            "vietnamese": "Tổ chức Thương mại Thế giới (WTO)",
            "hanja": "世界貿易機構",
            "hanjaReading": "世(세상 세) + 界(지경 계) + 貿(무역할 무) + 易(바꿀 역) + 機(틀 기) + 構(얽을 구)",
            "pronunciation": "세계무역기구 (WTO)",
            "meaningKo": "세계 무역 질서를 규율하는 국제기구로, 1995년 설립되어 회원국 간 무역 규범을 관리하고 분쟁을 해결합니다. 통역 시 주의할 점은 'WTO 규범', 'WTO 협정', 'WTO 분쟁해결기구(DSB)' 등을 명확히 구분해야 하며, 베트nam은 2007년 가입국이므로 가입 전후 맥락을 구분해야 합니다. 한국은 1995년 창설 회원국이므로 양국의 WTO 이행 경험 차이를 인지하고 통역해야 합니다.",
            "meaningVi": "Tổ chức quốc tế điều chỉnh trật tự thương mại toàn cầu, được thành lập năm 1995 để quản lý các quy phạm thương mại và giải quyết tranh chấp giữa các quốc gia thành viên. Việt Nam gia nhập WTO năm 2007, trong khi Hàn Quốc là thành viên sáng lập.",
            "context": "국제통상 협상, 무역분쟁 해결, 다자간 무역협정",
            "culturalNote": "한국은 WTO 창설 회원국으로 다자무역체제의 적극적 옹호자이며, 통상분쟁에서 WTO 규범을 자주 인용합니다. 베트남은 2007년 가입 이후 급속한 무역 자유화를 경험했으며, 한국 기업들이 베트남 WTO 가입을 계기로 대거 진출했습니다. 통역 시 양국의 WTO 가입 시점 차이(12년)로 인한 제도적 성숙도 격차를 고려해야 합니다.",
            "commonMistakes": [
                {
                    "mistake": "WTO를 '세계무역기관'으로 번역",
                    "correction": "세계무역기구 (Tổ chức Thương mại Thế giới)",
                    "explanation": "'기관'은 agency를 의미하므로 국제기구를 뜻하는 '기구(tổ chức)'가 정확"
                },
                {
                    "mistake": "DSB를 '분쟁해결위원회'로 오역",
                    "correction": "분쟁해결기구 (Cơ quan Giải quyết Tranh chấp)",
                    "explanation": "Dispute Settlement Body는 위원회(committee)가 아닌 독립 기구(body)"
                },
                {
                    "mistake": "베트남 WTO 가입 시점을 2006년으로 잘못 언급",
                    "correction": "2007년 1월 11일 정식 가입",
                    "explanation": "협상 타결은 2006년이지만 정식 가입은 2007년이므로 명확한 구분 필요"
                }
            ],
            "examples": [
                {
                    "ko": "한국과 베트남 모두 WTO 회원국으로서 최혜국대우 원칙을 준수해야 합니다.",
                    "vi": "Cả Hàn Quốc và Việt Nam đều là thành viên WTO nên phải tuân thủ nguyên tắc đối xử tối huệ quốc (MFN).",
                    "situation": "formal"
                },
                {
                    "ko": "이 사안은 WTO 분쟁해결기구에 회부할 수 있습니다.",
                    "vi": "Vấn đề này có thể được chuyển lên Cơ quan Giải quyết Tranh chấp của WTO.",
                    "situation": "formal"
                },
                {
                    "ko": "베트남의 WTO 가입 이후 양국 교역량이 5배 증가했습니다.",
                    "vi": "Sau khi Việt Nam gia nhập WTO, kim ngạch thương mại song phương đã tăng gấp 5 lần.",
                    "situation": "onsite"
                }
            ],
            "relatedTerms": ["자유무역협정", "최혜국대우", "무역분쟁해결", "관세인하"]
        },
        {
            "slug": "hiep-dinh-thuong-mai-tu-do",
            "korean": "자유무역협정",
            "vietnamese": "Hiệp định Thương mại Tự do (FTA)",
            "hanja": "自由貿易協定",
            "hanjaReading": "自(스스로 자) + 由(말미암을 유) + 貿(무역할 무) + 易(바꿀 역) + 協(화할 협) + 定(정할 정)",
            "pronunciation": "자유무역협정 (FTA)",
            "meaningKo": "둘 이상의 국가가 상호 간 관세 및 비관세 장벽을 철폐하여 무역 자유화를 실현하는 국제협정입니다. 통역 시 한-베 FTA(2015년 발효)의 구체적 내용을 숙지해야 하며, 특히 '즉시 철폐', '5년 철폐', '10년 철폐' 등 관세 철폐 일정을 정확히 구분해야 합니다. 또한 원산지규정, 상품·서비스 양허, 투자 보호 조항 등 FTA의 다층적 구조를 이해하고 통역해야 합니다.",
            "meaningVi": "Hiệp định quốc tế giữa hai hoặc nhiều quốc gia nhằm xóa bỏ rào cản thuế quan và phi thuế quan để tự do hóa thương mại. Hiệp định FTA Hàn-Việt có hiệu lực từ năm 2015, với lộ trình xóa bỏ thuế quan phân theo giai đoạn (ngay lập tức, 5 năm, 10 năm).",
            "context": "통상협상, 관세 감축, 무역 자유화",
            "culturalNote": "한국은 세계에서 가장 많은 FTA 네트워크를 보유한 국가 중 하나로, FTA를 경제외교의 핵심 수단으로 활용합니다. 베트남은 ASEAN 회원국으로서 다수의 지역 FTA에 참여하며, 특히 RCEP, CPTPP 등 메가 FTA에 적극적입니다. 한-베 FTA는 베트남이 한국과 체결한 최초의 양자 FTA로, 양국 경제관계에서 역사적 의미를 가집니다.",
            "commonMistakes": [
                {
                    "mistake": "FTA를 '자유무역협약'으로 번역",
                    "correction": "자유무역협정 (Hiệp định, không phải Hiệp ước)",
                    "explanation": "Agreement는 협정, Treaty는 협약이므로 법적 위상이 다름"
                },
                {
                    "mistake": "한-베 FTA 발효일을 2014년으로 잘못 언급",
                    "correction": "2015년 12월 20일 발효",
                    "explanation": "서명은 2014년이지만 발효는 2015년"
                },
                {
                    "mistake": "관세 철폐를 '즉시 폐지'로 단순화",
                    "correction": "품목별 철폐 일정 구분 필요 (즉시/5년/10년/예외)",
                    "explanation": "FTA는 민감 품목에 따라 차등적 철폐 일정 적용"
                }
            ],
            "examples": [
                {
                    "ko": "한-베 FTA 체결로 양국 교역량이 매년 15% 이상 증가하고 있습니다.",
                    "vi": "Nhờ FTA Hàn-Việt, kim ngạch thương mại song phương tăng trên 15% mỗi năm.",
                    "situation": "formal"
                },
                {
                    "ko": "이 제품은 FTA 원산지 증명서가 있으면 무관세 혜택을 받을 수 있습니다.",
                    "vi": "Sản phẩm này được miễn thuế nếu có Giấy chứng nhận xuất xứ FTA (C/O).",
                    "situation": "onsite"
                },
                {
                    "ko": "FTA 특혜관세 적용을 위해서는 원산지 기준을 충족해야 합니다.",
                    "vi": "Để được áp dụng thuế suất ưu đãi FTA, cần đáp ứng quy tắc xuất xứ.",
                    "situation": "formal"
                }
            ],
            "relatedTerms": ["원산지규정", "관세철폐", "특혜관세", "통상협상"]
        },
        {
            "slug": "chong-ban-pha-gia",
            "korean": "반덤핑",
            "vietnamese": "Chống bán phá giá",
            "hanja": "反damping",
            "hanjaReading": "反(돌이킬 반) + damping(영어 외래어)",
            "pronunciation": "반덤핑",
            "meaningKo": "수출국 기업이 정상가격보다 낮은 가격으로 제품을 수출하여 수입국 산업에 피해를 주는 행위를 방지하기 위해 부과하는 관세입니다. 통역 시 '덤핑 마진', '정상가격', '국내산업 피해' 등 반덤핑 조사의 3대 요건을 명확히 구분해야 하며, WTO 반덤핑협정에 따른 절차적 요건(조사 개시, 잠정조치, 최종판정, 일몰재심)을 정확히 전달해야 합니다. 한국은 철강, 화학 등에서 반덤핑 조사를 자주 받는 국가입니다.",
            "meaningVi": "Thuế được áp dụng để ngăn chặn hành vi bán sản phẩm dưới giá bình thường, gây thiệt hại cho ngành công nghiệp trong nước. Điều tra chống bán phá giá phải chứng minh 3 yếu tố: chênh lệch giá (dumping margin), giá bình thường, và thiệt hại cho ngành nội địa. Hàn Quốc thường xuyên bị điều tra chống bán phá giá trong lĩnh vực thép và hóa chất.",
            "context": "무역구제, WTO 규범, 수입규제",
            "culturalNote": "한국은 과거 철강, 전자제품 등에서 미국, EU로부터 빈번한 반덤핑 조사를 받았으며, 이를 계기로 공정무역 규범에 대한 이해가 깊습니다. 베트남은 최근 수산물, 철강 등에서 반덤핑 조사를 받는 사례가 증가하고 있어, 한국의 대응 경험이 유용한 참고자료가 됩니다. 통역 시 양국 모두 반덤핑 피소 경험이 있음을 염두에 두어야 합니다.",
            "commonMistakes": [
                {
                    "mistake": "덤핑을 '불공정 거래'로 포괄적으로 번역",
                    "correction": "덤핑은 '정상가격 이하 판매' (bán dưới giá bình thường)",
                    "explanation": "덤핑은 불공정거래의 한 유형일 뿐, 동의어가 아님"
                },
                {
                    "mistake": "반덤핑 관세를 '징벌적 관세'로 오역",
                    "correction": "반덤핑 관세 (thuế chống bán phá giá), 징벌 관세는 별개",
                    "explanation": "징벌 관세(punitive tariff)는 정치적 제재이고, 반덤핑은 무역구제 수단"
                },
                {
                    "mistake": "덤핑 마진 계산 방식을 생략",
                    "correction": "'정상가격 - 수출가격'의 차이로 명확히 설명",
                    "explanation": "법률 통역에서는 기술적 계산 방식도 정확히 전달 필요"
                }
            ],
            "examples": [
                {
                    "ko": "미국이 한국산 철강에 대해 반덤핑 관세 25%를 부과했습니다.",
                    "vi": "Mỹ áp thuế chống bán phá giá 25% đối với thép Hàn Quốc.",
                    "situation": "formal"
                },
                {
                    "ko": "반덤핑 조사는 통상 1년 이내에 완료되어야 합니다.",
                    "vi": "Điều tra chống bán phá giá phải hoàn thành trong vòng 1 năm.",
                    "situation": "formal"
                },
                {
                    "ko": "덤핑 마진이 2% 미만이면 반덤핑 조치가 종료됩니다.",
                    "vi": "Nếu chênh lệch giá dưới 2%, biện pháp chống bán phá giá sẽ được chấm dứt.",
                    "situation": "onsite"
                }
            ],
            "relatedTerms": ["상계관세", "세이프가드", "무역구제", "WTO협정"]
        },
        {
            "slug": "thue-chong-tro-cap",
            "korean": "상계관세",
            "vietnamese": "Thuế chống trợ cấp",
            "hanja": "相計關稅",
            "hanjaReading": "相(서로 상) + 計(셀 계) + 關(관문 관) + 稅(세금 세)",
            "pronunciation": "상계관세",
            "meaningKo": "수출국 정부가 자국 기업에 보조금을 지급하여 불공정한 경쟁우위를 제공할 때, 수입국이 그 효과를 상쇄하기 위해 부과하는 관세입니다. 통역 시 주의할 점은 '금지보조금', '조치가능보조금', '허용보조금'의 3대 분류를 명확히 구분해야 하며, 특히 R&D 지원, 환경보조금 등 허용보조금과 수출보조금의 차이를 정확히 전달해야 합니다. WTO 보조금협정(SCM Agreement)의 기준을 숙지해야 합니다.",
            "meaningVi": "Thuế được áp dụng để triệt tiêu lợi thế cạnh tranh bất công khi chính phủ nước xuất khẩu trợ cấp cho doanh nghiệp. Theo Hiệp định SCM của WTO, trợ cấp được phân loại thành 3 loại: trợ cấp bị cấm (đỏ), trợ cấp có thể kiện (vàng), và trợ cấp được phép (xanh). Cần phân biệt rõ trợ cấp xuất khẩu và trợ cấp R&D, môi trường.",
            "context": "무역구제, 보조금 규제, WTO 분쟁",
            "culturalNote": "한국은 조선, 반도체 등 전략산업에 대한 정부 지원이 많아 미국, EU로부터 상계관세 조사를 자주 받습니다. 베트남도 국영기업에 대한 정부 지원이 많아 향후 상계관세 이슈가 증가할 가능성이 있습니다. 통역 시 양국 모두 산업정책과 WTO 규범 간 긴장관계를 경험하고 있음을 인지해야 합니다.",
            "commonMistakes": [
                {
                    "mistake": "상계관세를 '보복관세'로 오역",
                    "correction": "상계관세 (thuế chống trợ cấp), 보복관세는 별개",
                    "explanation": "보복관세는 정치적 대응이고, 상계관세는 보조금 상쇄 목적"
                },
                {
                    "mistake": "모든 정부 지원을 '금지보조금'으로 단순화",
                    "correction": "3대 분류(금지/조치가능/허용) 구분 필수",
                    "explanation": "R&D, 환경 보조금 등은 허용되므로 정확한 분류 필요"
                },
                {
                    "mistake": "상계관세와 반덤핑 관세를 혼동",
                    "correction": "상계는 정부 보조금, 반덤핑은 기업의 저가 판매",
                    "explanation": "원인과 대상이 다른 별개의 무역구제 수단"
                }
            ],
            "examples": [
                {
                    "ko": "EU가 한국 조선업에 대한 정부 보조금을 문제삼아 상계관세 조사를 개시했습니다.",
                    "vi": "EU khởi động điều tra thuế chống trợ cấp đối với ngành đóng tàu Hàn Quốc do trợ cấp của chính phủ.",
                    "situation": "formal"
                },
                {
                    "ko": "이 지원금은 R&D 목적이므로 허용보조금에 해당합니다.",
                    "vi": "Khoản hỗ trợ này nhằm mục đích R&D nên thuộc trợ cấp được phép (Green Box).",
                    "situation": "onsite"
                },
                {
                    "ko": "수출보조금은 WTO에서 명백히 금지하는 적색등 보조금입니다.",
                    "vi": "Trợ cấp xuất khẩu là trợ cấp đèn đỏ bị WTO cấm rõ ràng.",
                    "situation": "formal"
                }
            ],
            "relatedTerms": ["반덤핑", "보조금협정", "무역구제", "산업정책"]
        },
        {
            "slug": "bien-phap-bao-ho-khan-cap",
            "korean": "세이프가드",
            "vietnamese": "Biện pháp bảo hộ khẩn cấp (Safeguard)",
            "hanja": "緊急輸入制限措置",
            "hanjaReading": "緊(급할 긴) + 急(급할 급) + 輸(보낼 수) + 入(들 입) + 制(제어할 제) + 限(한정할 한) + 措(둘 조) + 置(둘 치)",
            "pronunciation": "세이프가드 / 긴급수입제한조치",
            "meaningKo": "특정 물품의 수입이 급증하여 국내 산업에 심각한 피해를 초래하거나 우려가 있을 때, 일시적으로 수입을 제한하는 긴급 무역구제 조치입니다. 통역 시 주의할 점은 반덤핑·상계관세와 달리 '불공정 무역행위'가 없어도 발동 가능하며, 대신 '보상 협상' 의무가 있다는 점을 명확히 해야 합니다. 또한 최대 발동 기간(4년+연장 4년), MFN 원칙 적용 등 WTO 세이프가드협정의 요건을 정확히 전달해야 합니다.",
            "meaningVi": "Biện pháp hạn chế nhập khẩu tạm thời khi nhập khẩu gia tăng đột ngột gây thiệt hại nghiêm trọng cho ngành công nghiệp trong nước. Khác với chống bán phá giá và chống trợ cấp, safeguard không yêu cầu chứng minh hành vi thương mại bất công, nhưng phải đàm phán bồi thường với nước xuất khẩu. Thời hạn tối đa là 4 năm (có thể gia hạn thêm 4 năm).",
            "context": "무역구제, 수입급증 대응, 산업보호",
            "culturalNote": "한국은 2018년 중국산 마늘에 대한 세이프가드 발동 등 농산물 분야에서 세이프가드를 활용한 경험이 있습니다. 베트남도 철강, 섬유 등에서 세이프가드 조사를 고려한 사례가 있습니다. 통역 시 세이프가드는 정치적으로 민감한 이슈로, 양국 간 통상 마찰로 비화될 수 있음을 염두에 두어야 합니다.",
            "commonMistakes": [
                {
                    "mistake": "세이프가드를 '긴급 관세'로 단순 번역",
                    "correction": "긴급수입제한조치 또는 세이프가드 (Biện pháp bảo hộ khẩn cấp)",
                    "explanation": "관세 인상뿐 아니라 수량제한, TRQ 등 다양한 수단 포함"
                },
                {
                    "mistake": "세이프가드 발동 시 보상 협상 의무를 누락",
                    "correction": "피해국은 보상 협상 또는 보복관세 권리 보유",
                    "explanation": "반덤핑과 달리 세이프가드는 공정한 무역에 대한 제한이므로 보상 필요"
                },
                {
                    "mistake": "FTA 체약국에도 자동 적용된다고 오해",
                    "correction": "FTA 세이프가드는 별도 규정 확인 필요 (일반 세이프가드와 다름)",
                    "explanation": "한-베 FTA에는 양자 세이프가드 조항이 별도로 존재"
                }
            ],
            "examples": [
                {
                    "ko": "정부는 수입 철강에 대해 200일간 세이프가드 조사를 실시하고 있습니다.",
                    "vi": "Chính phủ đang tiến hành điều tra safeguard đối với thép nhập khẩu trong 200 ngày.",
                    "situation": "formal"
                },
                {
                    "ko": "세이프가드 발동 시 수출국과 보상 협상을 진행해야 합니다.",
                    "vi": "Khi phát động safeguard, phải đàm phán bồi thường với nước xuất khẩu.",
                    "situation": "formal"
                },
                {
                    "ko": "이 조치는 MFN 원칙에 따라 모든 수출국에 동등하게 적용됩니다.",
                    "vi": "Biện pháp này được áp dụng công bằng cho tất cả nước xuất khẩu theo nguyên tắc MFN.",
                    "situation": "onsite"
                }
            ],
            "relatedTerms": ["반덤핑", "무역구제", "긴급관세", "수입쿼터"]
        },
        {
            "slug": "quy-tac-xuat-xu",
            "korean": "원산지규정",
            "vietnamese": "Quy tắc xuất xứ",
            "hanja": "原產地規定",
            "hanjaReading": "原(근본 원) + 產(날 산) + 地(땅 지) + 規(법 규) + 定(정할 정)",
            "pronunciation": "원산지규정",
            "meaningKo": "특정 상품이 어느 국가에서 생산되었는지를 판정하는 기준으로, FTA 특혜관세 적용의 핵심 요건입니다. 통역 시 '완전생산기준(WO)', '실질적 변형기준(CTC, RVC, SP)' 등 원산지 결정 기준을 명확히 구분해야 하며, 특히 부가가치비율(RVC) 계산 방식(공제법 vs 집적법)을 정확히 전달해야 합니다. 한-베 FTA에서는 대부분 품목이 40% RVC 또는 세번변경기준(CTH)을 적용합니다.",
            "meaningVi": "Tiêu chí xác định quốc gia sản xuất của sản phẩm, là yêu cầu cốt lõi để hưởng thuế suất ưu đãi FTA. Bao gồm tiêu chí sản xuất hoàn toàn (WO) và tiêu chí chuyển đổi thực chất (CTC, RVC, SP). Trong FTA Hàn-Việt, hầu hết mặt hàng áp dụng tiêu chí tỷ lệ giá trị gia tăng (RVC) 40% hoặc thay đổi mã HS (CTH).",
            "context": "FTA 활용, 관세 혜택, 무역실무",
            "culturalNote": "한국 기업들은 원산지규정을 전략적으로 활용하여 FTA 혜택을 극대화하는 데 능숙합니다. 베트남은 외국인 투자기업이 많아 원자재 수입 비중이 높아 원산지 충족이 어려운 경우가 많습니다. 통역 시 한국 기업의 원산지 관리 노하우와 베트남의 원산지 충족 애로사항 간 정보 격차를 고려해야 합니다.",
            "commonMistakes": [
                {
                    "mistake": "원산지를 단순히 '생산국'으로 번역",
                    "correction": "원산지는 법적 개념으로 '원산지 결정 기준' 충족 국가",
                    "explanation": "최종 생산국과 원산지는 다를 수 있음 (예: 중국 생산품도 베트남 원산지 가능)"
                },
                {
                    "mistake": "RVC 계산에서 공제법과 집적법을 혼동",
                    "correction": "공제법 RVC = (FOB-VNM)/FOB × 100, 집적법 RVC = VOM/FOB × 100",
                    "explanation": "계산 방식에 따라 원산지 충족 여부가 달라지므로 정확한 구분 필수"
                },
                {
                    "mistake": "원산지 증명서와 원산지 표시를 혼동",
                    "correction": "증명서는 FTA 특혜용, 표시는 소비자 정보 제공용",
                    "explanation": "목적과 법적 근거가 다른 별개 제도"
                }
            ],
            "examples": [
                {
                    "ko": "이 제품은 베트남산 부품이 60%이므로 한-베 FTA 원산지 기준을 충족합니다.",
                    "vi": "Sản phẩm này có 60% linh kiện Việt Nam nên đáp ứng quy tắc xuất xứ FTA Hàn-Việt.",
                    "situation": "onsite"
                },
                {
                    "ko": "원산지 증명서는 선적 후 1년 이내 소급 발급이 가능합니다.",
                    "vi": "Giấy chứng nhận xuất xứ (C/O) có thể cấp hồi tố trong vòng 1 năm sau khi xuất hàng.",
                    "situation": "formal"
                },
                {
                    "ko": "세번변경기준을 충족하려면 HS 6단위가 변경되어야 합니다.",
                    "vi": "Để đáp ứng tiêu chí thay đổi mã HS, cần thay đổi ở cấp 6 số.",
                    "situation": "onsite"
                }
            ],
            "relatedTerms": ["자유무역협정", "특혜관세", "원산지증명서", "부가가치비율"]
        },
        {
            "slug": "giai-quyet-tranh-chap-thuong-mai",
            "korean": "무역분쟁해결",
            "vietnamese": "Giải quyết tranh chấp thương mại",
            "hanja": "貿易紛爭解決",
            "hanjaReading": "貿(무역할 무) + 易(바꿀 역) + 紛(어지러울 분) + 爭(다툴 쟁) + 解(풀 해) + 決(결단할 결)",
            "pronunciation": "무역분쟁해결",
            "meaningKo": "국가 간 무역 관련 분쟁을 WTO, FTA, 또는 중재를 통해 해결하는 절차입니다. 통역 시 WTO 분쟁해결절차의 단계별 프로세스(협의 요청 → 패널 설치 → 패널 보고서 → 상소기구 → 이행 감시)를 정확히 구분해야 하며, 특히 '패널(Panel)'과 '상소기구(AB)', 'DSB 채택' 등 법적 용어를 명확히 전달해야 합니다. 또한 이행 기간, 보복조치 등 판정 후 절차도 숙지해야 합니다.",
            "meaningVi": "Quy trình giải quyết tranh chấp thương mại giữa các quốc gia thông qua WTO, FTA hoặc trọng tài. Quy trình giải quyết tranh chấp WTO gồm các bước: yêu cầu tham vấn → thành lập ban hội thẩm (Panel) → báo cáo Panel → cơ quan phúc thẩm (AB) → giám sát thực thi. Cần phân biệt rõ Panel và AB, cũng như thời hạn thực thi và biện pháp trả đũa.",
            "context": "WTO 분쟁, 통상 마찰, 국제중재",
            "culturalNote": "한국은 WTO 분쟁해결절차를 적극 활용하는 국가로, 특히 일본과의 반도체 수출규제 분쟁 등에서 WTO 제소 경험이 있습니다. 베트남은 아직 WTO 분쟁 경험이 적지만, 향후 무역량 증가에 따라 분쟁이 늘어날 것으로 예상됩니다. 통역 시 한국의 분쟁 대응 노하우가 베트남에 유용한 참고자료가 될 수 있음을 인지해야 합니다.",
            "commonMistakes": [
                {
                    "mistake": "패널을 '위원회'로 번역",
                    "correction": "패널 또는 분쟁해결 패널 (Ban hội thẩm)",
                    "explanation": "Panel은 준사법기구로 위원회(committee)와는 법적 위상이 다름"
                },
                {
                    "mistake": "상소기구(AB)를 '항소법원'으로 오역",
                    "correction": "상소기구 (Cơ quan Phúc thẩm, Appellate Body)",
                    "explanation": "법원이 아닌 WTO 내부 상설 기구"
                },
                {
                    "mistake": "분쟁 해결 기간을 누락",
                    "correction": "패널은 6개월, 상소는 90일 이내 (총 1년 목표)",
                    "explanation": "법적 예측가능성을 위해 기간 명시 필수"
                }
            ],
            "examples": [
                {
                    "ko": "한국은 일본의 수출규제 조치에 대해 WTO에 분쟁해결을 요청했습니다.",
                    "vi": "Hàn Quốc đã yêu cầu WTO giải quyết tranh chấp về biện pháp hạn chế xuất khẩu của Nhật Bản.",
                    "situation": "formal"
                },
                {
                    "ko": "패널 보고서가 채택되면 60일 이내에 상소할 수 있습니다.",
                    "vi": "Sau khi báo cáo Panel được thông qua, có thể kháng cáo trong vòng 60 ngày.",
                    "situation": "formal"
                },
                {
                    "ko": "패소국이 판정을 이행하지 않으면 승소국은 보복조치를 취할 수 있습니다.",
                    "vi": "Nếu nước thua kiện không thực thi phán quyết, nước thắng có thể áp biện pháp trả đũa.",
                    "situation": "onsite"
                }
            ],
            "relatedTerms": ["WTO협정", "패널", "상소기구", "무역보복"]
        },
        {
            "slug": "dam-phan-thuong-mai",
            "korean": "통상교섭",
            "vietnamese": "Đàm phán thương mại",
            "hanja": "通商交涉",
            "hanjaReading": "通(통할 통) + 商(장사 상) + 交(사귈 교) + 涉(건널 섭)",
            "pronunciation": "통상교섭",
            "meaningKo": "국가 간 무역 관련 협정, 규범, 분쟁 등을 협상하는 외교 활동으로, FTA 체결, WTO 다자협상, 양자 통상 현안 해결 등을 포함합니다. 통역 시 주의할 점은 '양허(concession)', '유보(reservation)', '최혜국대우(MFN)', '내국민대우(NT)' 등 통상 핵심 용어를 정확히 전달해야 하며, 협상 단계(탐색 → 실무 → 수석대표 → 장관급)에 따른 의사결정 구조를 이해해야 합니다.",
            "meaningVi": "Hoạt động ngoại giao đàm phán về hiệp định, quy phạm, tranh chấp thương mại giữa các quốc gia, bao gồm ký kết FTA, đàm phán đa phương WTO, giải quyết vấn đề song phương. Cần nắm vững các thuật ngữ cốt lõi như nhượng bộ (concession), dành riêng (reservation), đối xử tối huệ quốc (MFN), đối xử quốc gia (NT), và hiểu cấu trúc quyết định theo các cấp đàm phán.",
            "context": "FTA 협상, WTO 라운드, 양자 통상",
            "culturalNote": "한국은 통상교섭본부를 산업통상자원부 산하에 두고 전문 협상단을 운영하며, 공격적 통상정책을 추진합니다. 베트남은 상공부(MOIT)가 통상교섭을 담당하며, 최근 CPTPP, EVFTA 등 메가 FTA 협상에서 적극적인 모습을 보였습니다. 통역 시 양국 모두 통상을 경제외교의 핵심 수단으로 활용함을 인지해야 합니다.",
            "commonMistakes": [
                {
                    "mistake": "통상교섭을 단순 '무역 협상'으로 번역",
                    "correction": "통상교섭 (Đàm phán thương mại) - 외교적 뉘앙스 포함",
                    "explanation": "교섭은 단순 협상을 넘어 국가 간 외교 행위"
                },
                {
                    "mistake": "양허(concession)를 '양보'로 오역",
                    "correction": "양허 - 상호 이익을 위한 개방 약속 (nhượng bộ có đi có lại)",
                    "explanation": "일방적 양보가 아닌 상호주의적 개방 약속"
                },
                {
                    "mistake": "협상 단계별 권한을 명확히 하지 않음",
                    "correction": "실무급은 논의, 수석대표급은 조율, 장관급은 타결",
                    "explanation": "각 단계의 의사결정 권한이 다름을 명시 필요"
                }
            ],
            "examples": [
                {
                    "ko": "한-베 FTA 통상교섭은 2012년부터 2014년까지 9차례 진행되었습니다.",
                    "vi": "Đàm phán thương mại FTA Hàn-Việt diễn ra 9 vòng từ 2012 đến 2014.",
                    "situation": "formal"
                },
                {
                    "ko": "민감 품목에 대한 양허안은 수석대표 회의에서 논의됩니다.",
                    "vi": "Phương án nhượng bộ đối với mặt hàng nhạy cảm được thảo luận ở cấp Trưởng đoàn đàm phán.",
                    "situation": "formal"
                },
                {
                    "ko": "통상교섭은 국익을 위한 치밀한 전략과 협상력이 필요합니다.",
                    "vi": "Đàm phán thương mại đòi hỏi chiến lược tỉ mỉ và khả năng thương thuyết vì lợi ích quốc gia.",
                    "situation": "onsite"
                }
            ],
            "relatedTerms": ["자유무역협정", "양허안", "최혜국대우", "내국민대우"]
        },
        {
            "slug": "kiem-soat-xuat-khau",
            "korean": "수출통제",
            "vietnamese": "Kiểm soát xuất khẩu",
            "hanja": "輸出統制",
            "hanjaReading": "輸(보낼 수) + 出(날 출) + 統(거느릴 통) + 制(제어할 제)",
            "pronunciation": "수출통제",
            "meaningKo": "국가안보, 국제평화, 대량살상무기 확산 방지 등을 위해 전략물자, 기술의 수출을 정부가 규제하는 제도입니다. 통역 시 '전략물자', '이중용도품목', '캐치올(catch-all)', '최종사용자 확인서' 등 수출통제 핵심 용어를 정확히 전달해야 하며, 특히 바세나르체제, 미사일기술통제체제(MTCR) 등 국제 수출통제 레짐의 차이를 명확히 해야 합니다. 최근 반도체, AI 칩 등 첨단기술 통제가 강화되고 있습니다.",
            "meaningVi": "Chế độ quản lý xuất khẩu của chính phủ đối với hàng hóa, công nghệ chiến lược nhằm bảo vệ an ninh quốc gia, hòa bình quốc tế, ngăn chặn phổ biến vũ khí hủy diệt hàng loạt. Bao gồm hàng hóa chiến lược, mặt hàng hai mục đích sử dụng (dual-use), điều khoản bắt tất cả (catch-all), giấy xác nhận người dùng cuối. Kiểm soát công nghệ tiên tiến như bán dẫn, chip AI đang được tăng cường.",
            "context": "전략물자 관리, 기술 수출, 안보 규제",
            "culturalNote": "한국은 2019년 일본의 반도체 소재 수출규제를 경험하며 수출통제의 정치적 무기화를 체감했습니다. 베트남은 아직 수출통제 체계가 발전 단계에 있으며, 첨단기술 재수출 규제 등에서 한국의 경험이 유용할 수 있습니다. 통역 시 수출통제가 무역과 안보의 교차점에 있는 민감한 이슈임을 인지해야 합니다.",
            "commonMistakes": [
                {
                    "mistake": "수출통제를 '수출 금지'로 단순화",
                    "correction": "수출통제는 허가제 (cấp phép), 금지는 일부만",
                    "explanation": "대부분은 사전 허가로 수출 가능, 전면 금지는 극소수"
                },
                {
                    "mistake": "이중용도품목을 '군사용'으로 오해",
                    "correction": "민수·군수 겸용 (dual-use) 품목",
                    "explanation": "민간용으로도 사용 가능하나 군사 전용 우려"
                },
                {
                    "mistake": "캐치올 조항을 누락",
                    "correction": "전략물자 목록에 없어도 WMD 우려 시 통제",
                    "explanation": "포괄적 통제 조항으로 목록 외 품목도 규제 가능"
                }
            ],
            "examples": [
                {
                    "ko": "이 반도체 장비는 전략물자이므로 수출 전 산업부 허가가 필요합니다.",
                    "vi": "Thiết bị bán dẫn này là hàng hóa chiến lược nên cần giấy phép của Bộ Công Thương trước khi xuất khẩu.",
                    "situation": "onsite"
                },
                {
                    "ko": "캐치올 조항에 따라 최종용도가 의심되면 수출을 불허할 수 있습니다.",
                    "vi": "Theo điều khoản catch-all, có thể từ chối xuất khẩu nếu nghi ngờ mục đích sử dụng cuối.",
                    "situation": "formal"
                },
                {
                    "ko": "한국은 2019년 일본의 전략물자 수출규제로 공급망 위기를 겪었습니다.",
                    "vi": "Hàn Quốc đã trải qua khủng hoảng chuỗi cung ứng do Nhật Bản kiểm soát xuất khẩu hàng chiến lược năm 2019.",
                    "situation": "formal"
                }
            ],
            "relatedTerms": ["전략물자", "이중용도품목", "바세나르체제", "기술이전"]
        },
        {
            "slug": "cuu-te-thuong-mai",
            "korean": "무역구제",
            "vietnamese": "Cứu tế thương mại",
            "hanja": "貿易救濟",
            "hanjaReading": "貿(무역할 무) + 易(바꿀 역) + 救(구원할 구) + 濟(건널 제)",
            "pronunciation": "무역구제",
            "meaningKo": "불공정 무역행위나 수입 급증으로부터 국내 산업을 보호하기 위한 법적 조치로, 반덤핑, 상계관세, 세이프가드를 통칭합니다. 통역 시 주의할 점은 각 조치의 발동 요건(덤핑/보조금/수입급증)과 법적 근거(WTO 협정)를 명확히 구분해야 하며, 특히 조사 절차(신청 → 개시 → 잠정 → 최종), 이해관계인 참여, 일몰재심 등 절차적 권리를 정확히 전달해야 합니다.",
            "meaningVi": "Biện pháp pháp lý bảo vệ ngành công nghiệp trong nước khỏi hành vi thương mại bất công hoặc gia tăng nhập khẩu đột ngột, bao gồm chống bán phá giá, chống trợ cấp, và biện pháp bảo hộ khẩn cấp. Cần phân biệt rõ điều kiện phát động (dumping/trợ cấp/nhập khẩu tăng đột biến) và quy trình điều tra (đơn → khởi động → tạm thời → cuối cùng), quyền tham gia của bên liên quan, và rà soát định kỳ (sunset review).",
            "context": "무역정책, 산업보호, WTO 규범",
            "culturalNote": "한국은 1980년대부터 무역구제 제도를 운영하며 철강, 화학 등에서 조사 경험이 풍부합니다. 베트남은 2000년대 들어 무역구제 제도를 도입했으며, 최근 철강, 화학 등에서 조사를 늘리고 있습니다. 통역 시 한국의 무역구제 노하우가 베트남 제도 발전에 참고가 될 수 있음을 인지해야 합니다.",
            "commonMistakes": [
                {
                    "mistake": "무역구제를 '무역 보호'로 오역",
                    "correction": "무역구제 (Cứu tế thương mại) - WTO 합법적 조치",
                    "explanation": "보호주의와 달리 WTO 규범 내 정당한 권리"
                },
                {
                    "mistake": "3대 조치(반덤핑/상계/세이프가드)를 혼용",
                    "correction": "각 조치의 발동 요건과 절차를 명확히 구분",
                    "explanation": "법적 근거와 효과가 다른 별개의 제도"
                },
                {
                    "mistake": "일몰재심(sunset review)을 누락",
                    "correction": "반덤핑·상계관세는 5년 후 자동 종료 (재심 없으면)",
                    "explanation": "무역구제는 임시 조치이며 정기 재검토 필수"
                }
            ],
            "examples": [
                {
                    "ko": "국내 업계는 중국산 철강에 대해 무역구제 조사를 신청했습니다.",
                    "vi": "Ngành trong nước đã đề nghị điều tra cứu tế thương mại đối với thép Trung Quốc.",
                    "situation": "formal"
                },
                {
                    "ko": "무역구제 조사는 통상 1년 이내에 완료되어야 합니다.",
                    "vi": "Điều tra cứu tế thương mại phải hoàn thành trong vòng 1 năm.",
                    "situation": "formal"
                },
                {
                    "ko": "이 반덤핑 관세는 5년 후 일몰재심을 거쳐 연장 여부가 결정됩니다.",
                    "vi": "Thuế chống bán phá giá này sẽ được xem xét gia hạn qua rà soát định kỳ sau 5 năm.",
                    "situation": "onsite"
                }
            ],
            "relatedTerms": ["반덤핑", "상계관세", "세이프가드", "WTO협정"]
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
