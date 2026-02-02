#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
국제법/통상법 용어 추가 스크립트 (Tier S 품질)
Theme: International Law/Trade Law
"""

import json
import os

def main():
    # 1. 파일 경로 설정
    file_path = os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', 'data', 'terms', 'legal.json')

    # 2. 기존 데이터 로드
    with open(file_path, 'r', encoding='utf-8') as f:
        data = json.load(f)  # data is a LIST

    # 3. 기존 slug 추출
    existing_slugs = {t['slug'] for t in data}

    # 4. 신규 용어 정의 (10개)
    new_terms = [
        {
            "slug": "dieu-uoc-quoc-te",
            "korean": "국제조약",
            "vietnamese": "điều ước quốc tế",
            "hanja": "國際條約",
            "hanjaReading": "國(나라 국) + 際(사이 제) + 條(가지 조) + 約(맺을 약)",
            "pronunciation": "디에우억 꾸억떼",
            "meaningKo": "국가 간에 체결되는 문서 형식의 합의로, 조약·협정·의정서·규약 등 다양한 명칭으로 불립니다. 통역 시 주의할 점은 베트남어에서 'hiệp định'(협정), 'công ước'(협약), 'nghị định thư'(의정서) 등 구체적 명칭이 있으므로 문맥에 따라 정확히 구분해야 합니다. 한국에서는 국회 비준 여부로 조약과 협정을 구분하지만, 베트남은 국제법상 효력은 동일하게 봅니다. 통역 현장에서 조약 명칭 번역 시 공식 외교부 문서를 반드시 참조하세요.",
            "meaningVi": "Thỏa thuận bằng văn bản giữa các quốc gia, có thể gọi là hiệp định, công ước, nghị định thư, điều ước tùy theo nội dung và hình thức. Việt Nam phân biệt điều ước quốc tế cần phê chuẩn của Quốc hội và điều ước không cần phê chuẩn.",
            "context": "국제법, 외교, 통상협상",
            "culturalNote": "한국은 조약 체결 시 국회 동의를 헌법에서 명시하며, 국회 비준 여부로 조약과 협정을 구분합니다. 베트남도 Quốc hội(국회) 비준이 필요하나, 명칭 구분보다 내용에 따른 절차 차이가 큽니다. 통역 시 양국의 입법 절차 차이를 이해하고 설명할 수 있어야 하며, 특히 조약 발효 시점(한국: 공포일/베트남: ký kết 및 phê chuẩn 완료 후)의 차이를 명확히 해야 합니다.",
            "commonMistakes": [
                {
                    "mistake": "모든 조약을 'hiệp định'으로 통칭",
                    "correction": "조약 유형에 따라 'công ước'(다자협약), 'hiệp định'(양자협정), 'nghị định thư'(의정서) 구분",
                    "explanation": "국제법상 조약의 형식과 내용에 따라 베트남어 명칭이 다르므로 정확히 구분해야 합니다."
                },
                {
                    "mistake": "'조약 체결'을 'ký kết điều ước'으로만 번역",
                    "correction": "'ký kết'(서명) + 'phê chuẩn'(비준) 단계 구분",
                    "explanation": "조약 체결은 서명과 비준 두 단계로 나뉘며, 베트남어에서도 이를 명확히 구분합니다."
                },
                {
                    "mistake": "'국회 비준'을 'Quốc hội phê duyệt'로 번역",
                    "correction": "'Quốc hội phê chuẩn'이 정확한 법률 용어",
                    "explanation": "'Phê chuẩn'은 조약 비준의 공식 용어이며, 'phê duyệt'은 일반 승인을 의미합니다."
                }
            ],
            "examples": [
                {
                    "ko": "이 국제조약은 국회의 비준을 거쳐 발효됩니다.",
                    "vi": "Điều ước quốc tế này sẽ có hiệu lực sau khi được Quốc hội phê chuẩn.",
                    "situation": "formal"
                },
                {
                    "ko": "양국은 자유무역협정이라는 국제조약을 체결했습니다.",
                    "vi": "Hai nước đã ký kết điều ước quốc tế là Hiệp định Thương mại Tự do.",
                    "situation": "formal"
                },
                {
                    "ko": "이 조약의 의정서는 별도로 비준받아야 합니다.",
                    "vi": "Nghị định thư của điều ước này cần được phê chuẩn riêng.",
                    "situation": "formal"
                }
            ],
            "relatedTerms": ["hiep-dinh-thuong-mai", "trong-tai-quoc-te", "cong-phap-quoc-te"]
        },
        {
            "slug": "cong-phap-quoc-te",
            "korean": "국제공법",
            "vietnamese": "công pháp quốc tế",
            "hanja": "國際公法",
            "hanjaReading": "國(나라 국) + 際(사이 제) + 公(공평할 공) + 法(법 법)",
            "pronunciation": "꽁팝 꾸억떼",
            "meaningKo": "국가 간의 관계를 규율하는 법으로, 조약·국제관습법·법의 일반원칙 등을 포함합니다. 통역 시 '국제사법'(tư pháp quốc tế, 섭외사법)과 혼동하지 않도록 주의해야 합니다. 국제공법은 국가·국제기구가 주체인 반면, 국제사법은 개인·법인의 섭외 사건을 다룹니다. 베트남 법조계에서는 'luật quốc tế công'이라고도 하며, 통역 현장에서 맥락에 따라 정확히 구분하는 것이 중요합니다. 특히 국제재판소 판례나 UN 결의 등을 언급할 때는 국제공법 영역임을 명확히 해야 합니다.",
            "meaningVi": "Ngành luật điều chỉnh quan hệ giữa các quốc gia, tổ chức quốc tế, bao gồm điều ước quốc tế, tập quán quốc tế, và nguyên tắc chung của pháp luật. Khác với tư pháp quốc tế (luật áp dụng cho quan hệ tư nhân có yếu tố nước ngoài).",
            "context": "국제법 이론, 외교, 국제분쟁",
            "culturalNote": "한국 법학에서는 국제공법과 국제사법을 명확히 구분하여 가르치며, 사법시험에서도 별도 과목으로 존재했습니다. 베트남도 'Công pháp quốc tế'와 'Tư pháp quốc tế'를 구분하지만, 실무에서는 'Luật quốc tế'로 통칭하는 경우가 많습니다. 통역 시 학술적 맥락에서는 정확히 구분하되, 일반 대중을 대상으로 할 때는 'luật quốc tế'로 풀어 설명하는 것이 효과적입니다.",
            "commonMistakes": [
                {
                    "mistake": "'국제공법'을 'luật quốc tế công'으로만 번역",
                    "correction": "'Công pháp quốc tế'가 학술적으로 정확한 표현",
                    "explanation": "'Luật quốc tế công'도 쓰이지만, 법학 전문 용어로는 'công pháp quốc tế'가 표준입니다."
                },
                {
                    "mistake": "'국제공법'과 '국제사법'을 구분하지 않고 'luật quốc tế'로 통칭",
                    "correction": "Công pháp(공법) vs Tư pháp(사법) 명확히 구분",
                    "explanation": "법의 주체와 대상이 다르므로 반드시 구분해야 합니다."
                },
                {
                    "mistake": "'국제관습법'을 'tập quán thương mại quốc tế'로 번역",
                    "correction": "'Tập quán quốc tế' 또는 'luật tập quán quốc tế'",
                    "explanation": "'Thương mại'를 붙이면 상관습으로 오해될 수 있습니다."
                }
            ],
            "examples": [
                {
                    "ko": "국제공법은 주권평등의 원칙에 기초합니다.",
                    "vi": "Công pháp quốc tế dựa trên nguyên tắc bình đẳng chủ quyền.",
                    "situation": "formal"
                },
                {
                    "ko": "이 사건은 국제공법이 아니라 국제사법 문제입니다.",
                    "vi": "Vụ việc này là vấn đề tư pháp quốc tế chứ không phải công pháp quốc tế.",
                    "situation": "formal"
                },
                {
                    "ko": "국제공법의 법원은 조약, 국제관습법, 법의 일반원칙입니다.",
                    "vi": "Nguồn của công pháp quốc tế là điều ước, tập quán quốc tế, và nguyên tắc chung của pháp luật.",
                    "situation": "formal"
                }
            ],
            "relatedTerms": ["tu-phap-quoc-te", "dieu-uoc-quoc-te", "trong-tai-quoc-te"]
        },
        {
            "slug": "tu-phap-quoc-te",
            "korean": "국제사법",
            "vietnamese": "tư pháp quốc tế",
            "hanja": "國際私法",
            "hanjaReading": "國(나라 국) + 際(사이 제) + 私(사사로울 사) + 法(법 법)",
            "pronunciation": "뜨팝 꾸억떼",
            "meaningKo": "섭외적 사건(외국적 요소가 있는 민사 사건)에 적용할 법을 결정하는 법으로, '국제사법'이라는 명칭 때문에 국제공법과 혼동되기 쉽습니다. 통역 시 반드시 구분해야 하며, 베트남어로는 'tư pháp quốc tế' 또는 'luật xung đột pháp luật'(법률충돌법)로 표현합니다. 실무에서는 국제결혼, 섭외계약, 국제거래 등 개인이나 법인의 권리의무를 다루는 영역입니다. 한국의 '국제사법'과 베트남의 'tư pháp quốc tế'는 거의 동일한 개념이지만, 준거법 선택 기준이 다를 수 있으므로 통역 시 주의가 필요합니다.",
            "meaningVi": "Ngành luật xác định luật nào được áp dụng cho các quan hệ dân sự có yếu tố nước ngoài (như hôn nhân quốc tế, hợp đồng thương mại xuyên quốc gia). Còn gọi là luật xung đột pháp luật hoặc luật áp dụng.",
            "context": "섭외 민사, 국제거래, 국제가족법",
            "culturalNote": "한국은 '국제사법'이라는 독립된 법률이 있어 준거법 결정 규칙을 명시하고 있습니다. 베트남은 'Luật Tư pháp quốc tế'(국제사법법)이 별도로 존재하지 않고, 민법·상법·가족혼인법 등에 섭외 조항이 분산되어 있습니다. 통역 시 한국의 '국제사법' 조문을 언급할 때 베트남에는 대응하는 단일 법률이 없음을 설명할 필요가 있으며, 해당 조항이 베트남의 어느 법률에 해당하는지 확인해야 합니다.",
            "commonMistakes": [
                {
                    "mistake": "'국제사법'을 'luật quốc tế'로 번역",
                    "correction": "'Tư pháp quốc tế' 또는 'luật xung đột pháp luật'",
                    "explanation": "'Luật quốc tế'는 국제법 전반을 의미하므로 부정확합니다."
                },
                {
                    "mistake": "'준거법'을 'luật cơ bản'으로 번역",
                    "correction": "'Luật được áp dụng' 또는 'luật điều chỉnh'",
                    "explanation": "'Luật cơ bản'은 기본법이라는 의미로 오해될 수 있습니다."
                },
                {
                    "mistake": "'섭외사건'을 'vụ việc nước ngoài'로 번역",
                    "correction": "'Quan hệ dân sự có yếu tố nước ngoài'",
                    "explanation": "베트남 법률 용어로 정확히 표현해야 합니다."
                }
            ],
            "examples": [
                {
                    "ko": "이 계약의 준거법은 국제사법에 따라 결정됩니다.",
                    "vi": "Luật được áp dụng cho hợp đồng này sẽ được xác định theo tư pháp quốc tế.",
                    "situation": "formal"
                },
                {
                    "ko": "국제사법은 어느 나라 법을 적용할지를 정하는 법입니다.",
                    "vi": "Tư pháp quốc tế là ngành luật xác định luật của nước nào được áp dụng.",
                    "situation": "formal"
                },
                {
                    "ko": "국제결혼의 법률관계는 국제사법으로 해결합니다.",
                    "vi": "Quan hệ pháp luật trong hôn nhân quốc tế được giải quyết theo tư pháp quốc tế.",
                    "situation": "formal"
                }
            ],
            "relatedTerms": ["cong-phap-quoc-te", "dieu-uoc-quoc-te", "trong-tai-quoc-te"]
        },
        {
            "slug": "trong-tai-quoc-te",
            "korean": "국제중재",
            "vietnamese": "trọng tài quốc tế",
            "hanja": "國際仲裁",
            "hanjaReading": "國(나라 국) + 際(사이 제) + 仲(가운데 중) + 裁(재판할 재)",
            "pronunciation": "쫑따이 꾸억떼",
            "meaningKo": "국제 상사 분쟁을 법원이 아닌 사적 중재기관에서 해결하는 제도로, 뉴욕협약에 따라 중재판정의 국제적 승인·집행이 보장됩니다. 통역 시 주의할 점은 '중재'(trọng tài)와 '조정'(hòa giải)을 명확히 구분해야 한다는 것입니다. 중재는 판정에 법적 구속력이 있지만, 조정은 합의 도출이 목적입니다. 한국과 베트남 모두 UNCITRAL 모델법을 기초로 중재법을 제정했으나, 중재절차와 중재인 선정 방식에 차이가 있으므로 통역 현장에서 양국 제도를 비교 설명할 수 있어야 합니다.",
            "meaningVi": "Giải quyết tranh chấp thương mại quốc tế thông qua trọng tài tư nhân thay vì tòa án, với phán quyết được công nhận và thi hành quốc tế theo Công ước New York. Việt Nam có Luật Trọng tài Thương mại và tham gia nhiều hiệp định trọng tài quốc tế.",
            "context": "국제계약, 통상분쟁, 투자분쟁",
            "culturalNote": "한국은 대한상사중재원(KCAB)이 국제중재를 주로 담당하며, 영어 중재가 일반적입니다. 베트남은 VIAC(베트남국제중재센터)가 있으며, 베트남어와 영어 중재가 모두 가능합니다. 통역 시 중재지(place of arbitration)와 중재언어(language of arbitration)를 명확히 구분해야 하며, 중재합의서(arbitration agreement) 작성 시 양국 법률의 강행규정을 확인해야 합니다. 또한 중재판정 불복 사유가 양국에서 다르므로 이를 설명할 수 있어야 합니다.",
            "commonMistakes": [
                {
                    "mistake": "'중재'와 '조정'을 구분하지 않고 모두 'trọng tài'로 번역",
                    "correction": "중재는 'trọng tài', 조정은 'hòa giải'",
                    "explanation": "중재는 구속력 있는 판정, 조정은 합의 도출로 법적 성격이 다릅니다."
                },
                {
                    "mistake": "'중재판정'을 'quyết định trọng tài'로 번역",
                    "correction": "'Phán quyết trọng tài'가 정확한 법률 용어",
                    "explanation": "'Quyết định'은 행정결정, 'phán quyết'은 사법판단을 의미합니다."
                },
                {
                    "mistake": "'중재합의'를 'thỏa thuận trọng tài'로만 번역",
                    "correction": "'Thỏa thuận trọng tài' 또는 'điều khoản trọng tài'",
                    "explanation": "계약 조항인 경우 'điều khoản'을 사용하는 것이 적절합니다."
                }
            ],
            "examples": [
                {
                    "ko": "이 계약의 분쟁은 싱가포르 국제중재센터에서 해결합니다.",
                    "vi": "Tranh chấp của hợp đồng này sẽ được giải quyết tại Trung tâm Trọng tài Quốc tế Singapore.",
                    "situation": "formal"
                },
                {
                    "ko": "중재판정은 법원 판결과 동일한 효력을 가집니다.",
                    "vi": "Phán quyết trọng tài có hiệu lực tương đương bản án của tòa án.",
                    "situation": "formal"
                },
                {
                    "ko": "국제중재는 소송보다 신속하고 비밀이 보장됩니다.",
                    "vi": "Trọng tài quốc tế nhanh hơn và bảo mật hơn so với tố tụng.",
                    "situation": "formal"
                }
            ],
            "relatedTerms": ["dieu-uoc-quoc-te", "hiep-dinh-thuong-mai", "tu-phap-quoc-te"]
        },
        {
            "slug": "hiep-dinh-thuong-mai",
            "korean": "통상협정",
            "vietnamese": "hiệp định thương mại",
            "hanja": "通商協定",
            "hanjaReading": "通(통할 통) + 商(장사 상) + 協(화합할 협) + 定(정할 정)",
            "pronunciation": "히업딘 투엉마이",
            "meaningKo": "국가 간 무역과 투자를 촉진하기 위한 협정으로, 관세 인하, 시장 개방, 통관 절차 간소화 등을 규정합니다. 통역 시 FTA(자유무역협정), EPA(경제동반자협정), CEPA(포괄적경제동반자협정) 등 다양한 형태를 구분해야 합니다. 한국은 미국, EU, ASEAN 등과 FTA를 체결했으며, 베트남도 CPTPP, EVFTA 등 다수의 통상협정을 체결했습니다. 통역 현장에서는 특정 협정의 정식 명칭을 정확히 알고 있어야 하며, 원산지규정(rules of origin), 양허표(tariff schedule) 등 기술적 용어에 익숙해야 합니다.",
            "meaningVi": "Hiệp định giữa các quốc gia nhằm thúc đẩy thương mại và đầu tư, quy định về giảm thuế quan, mở cửa thị trường, đơn giản hóa thủ tục hải quan. Việt Nam đã ký nhiều hiệp định như CPTPP, EVFTA, RCEP.",
            "context": "국제무역, 외교, 경제정책",
            "culturalNote": "한국은 통상협정 협상 시 국내 산업 보호와 개방의 균형을 중시하며, 민감 품목(쌀, 자동차 등)에 대해 장기 관세 철폐 일정을 협상합니다. 베트남은 개방 속도가 빠른 편이나, 섬유·신발 등 주력 산업에서는 원산지규정 완화를 강하게 요구합니다. 통역 시 양국의 협상 전략 차이를 이해하고, 민감 품목 목록을 숙지해야 하며, 관세 양허 단계(즉시철폐, 5년, 10년 등)를 정확히 전달해야 합니다.",
            "commonMistakes": [
                {
                    "mistake": "모든 통상협정을 'hiệp định thương mại tự do'(FTA)로 번역",
                    "correction": "협정 유형에 따라 정확한 명칭 사용 (EPA, CEPA 등)",
                    "explanation": "FTA는 통상협정의 한 형태일 뿐이며, 협정마다 공식 명칭이 다릅니다."
                },
                {
                    "mistake": "'원산지규정'을 'quy định nguồn gốc'으로만 번역",
                    "correction": "'Quy tắc xuất xứ' 또는 'Rules of Origin'",
                    "explanation": "'Quy tắc xuất xứ'가 통상 전문 용어로 정확합니다."
                },
                {
                    "mistake": "'양허표'를 'bảng nhượng bộ'로 직역",
                    "correction": "'Biểu thuế ưu đãi' 또는 'Tariff Schedule'",
                    "explanation": "'Nhượng bộ'는 정치적 양보를 의미하므로 부적절합니다."
                }
            ],
            "examples": [
                {
                    "ko": "한-베 FTA는 양국 교역을 크게 증가시켰습니다.",
                    "vi": "Hiệp định Thương mại Tự do Hàn-Việt đã tăng đáng kể kim ngạch thương mại hai nước.",
                    "situation": "formal"
                },
                {
                    "ko": "이 품목은 통상협정에 따라 관세가 면제됩니다.",
                    "vi": "Mặt hàng này được miễn thuế theo hiệp định thương mại.",
                    "situation": "formal"
                },
                {
                    "ko": "통상협정 협상에서 원산지규정이 쟁점입니다.",
                    "vi": "Quy tắc xuất xứ là tranh điểm trong đàm phán hiệp định thương mại.",
                    "situation": "formal"
                }
            ],
            "relatedTerms": ["dieu-uoc-quoc-te", "chong-ban-pha-gia", "bien-phap-tu-ve"]
        },
        {
            "slug": "chong-ban-pha-gia",
            "korean": "반덤핑",
            "vietnamese": "chống bán phá giá",
            "hanja": "反Dumping",
            "hanjaReading": "反(반대할 반) + Dumping(영어)",
            "pronunciation": "쫑반파쟈",
            "meaningKo": "외국 기업이 정상가격보다 낮은 가격으로 수출하여 국내 산업에 피해를 주는 것을 방지하기 위한 무역구제 조치입니다. 통역 시 'dumping'(덤핑), 'anti-dumping duty'(반덤핑관세), 'injury'(피해), 'normal value'(정상가격) 등 기술적 용어를 정확히 전달해야 합니다. WTO 반덤핑협정에 따라 조사·판정·부과 절차가 진행되며, 한국은 무역위원회가, 베트남은 무역구제국(Trade Remedies Authority)이 담당합니다. 통역 현장에서는 조사 단계(preliminary/final determination)와 부과율 계산 방식(dumping margin)을 설명할 수 있어야 합니다.",
            "meaningVi": "Biện pháp phòng vệ thương mại nhằm chống lại hành vi xuất khẩu hàng hóa với giá thấp hơn giá trị bình thường, gây thiệt hại cho ngành sản xuất trong nước. Cơ quan Phòng vệ Thương mại Việt Nam chịu trách nhiệm điều tra và áp thuế chống bán phá giá.",
            "context": "무역구제, 수입규제, WTO",
            "culturalNote": "한국은 철강·화학 등 중공업 분야에서 반덤핑 조사를 많이 받아온 역사가 있으며, 반덤핑 대응 전문가가 많습니다. 베트남은 최근 제조업이 성장하면서 반덤핑 제소가 증가하고 있으며, 철강·알루미늄 등에서 미국·EU로부터 조사를 받고 있습니다. 통역 시 양국 간 반덤핑 이슈(예: 한국산 철강의 베트남 수출)가 발생할 수 있으므로, 민감한 사안임을 인지하고 객관적으로 통역해야 합니다.",
            "commonMistakes": [
                {
                    "mistake": "'덤핑'을 'giảm giá'로 번역",
                    "correction": "'Bán phá giá' 또는 'dumping'",
                    "explanation": "'Giảm giá'는 일반 할인, 'bán phá giá'는 불공정 가격 책정을 의미합니다."
                },
                {
                    "mistake": "'반덤핑관세'를 'thuế chống dumping'으로만 번역",
                    "correction": "'Thuế chống bán phá giá'가 정확한 법률 용어",
                    "explanation": "베트남 법률에서는 'thuế chống bán phá giá'로 명시되어 있습니다."
                },
                {
                    "mistake": "'정상가격'을 'giá bình thường'으로 번역",
                    "correction": "'Giá trị bình thường' 또는 'normal value'",
                    "explanation": "'Giá trị'는 가치, 'giá'는 가격으로, 법률 용어로는 'giá trị'가 적절합니다."
                }
            ],
            "examples": [
                {
                    "ko": "중국산 철강에 대해 반덤핑관세가 부과되었습니다.",
                    "vi": "Thép Trung Quốc đã bị áp thuế chống bán phá giá.",
                    "situation": "formal"
                },
                {
                    "ko": "반덤핑 조사는 국내 산업의 피해를 입증해야 합니다.",
                    "vi": "Điều tra chống bán phá giá cần chứng minh thiệt hại cho ngành sản xuất trong nước.",
                    "situation": "formal"
                },
                {
                    "ko": "덤핑마진이 20%로 판정되어 관세가 부과됩니다.",
                    "vi": "Biên độ phá giá được xác định là 20% nên sẽ áp thuế.",
                    "situation": "formal"
                }
            ],
            "relatedTerms": ["bien-phap-tu-ve", "hiep-dinh-thuong-mai", "dieu-uoc-quoc-te"]
        },
        {
            "slug": "bien-phap-tu-ve",
            "korean": "세이프가드",
            "vietnamese": "biện pháp tự vệ",
            "hanja": "Safeguard",
            "hanjaReading": "영어 차용어 (자위조치)",
            "pronunciation": "비엔팝뜨베",
            "meaningKo": "특정 품목의 수입이 급증하여 국내 산업에 심각한 피해를 주거나 줄 우려가 있을 때 취하는 긴급 수입제한 조치입니다. 통역 시 반덤핑·상계관세와 구분해야 하며, 세이프가드는 불공정 행위 없이도 발동 가능하다는 점이 특징입니다. WTO 세이프가드협정에 따라 일시적·투명한 조치여야 하며, 영향 받는 국가와 협의 또는 보상 제공이 필요합니다. 한국은 농산물(마늘, 고추 등)에서, 베트남은 공산품에서 세이프가드를 발동한 사례가 있으며, 통역 시 발동 요건과 절차를 정확히 설명해야 합니다.",
            "meaningVi": "Biện pháp hạn chế nhập khẩu khẩn cấp khi hàng hóa nhập khẩu tăng đột biến gây thiệt hại nghiêm trọng hoặc đe dọa ngành sản xuất trong nước. Không cần chứng minh hành vi không công bằng như chống bán phá giá, nhưng phải tạm thời và minh bạch theo WTO.",
            "context": "무역구제, 긴급수입제한, WTO",
            "culturalNote": "한국은 1990년대 IMF 위기 이후 세이프가드를 신중하게 사용하며, 주로 농산물 분야에서 발동했습니다. 베트남은 국내 산업 보호를 위해 철강·전자제품 등에서 세이프가드를 적극 활용합니다. 통역 시 세이프가드 발동이 국제적 무역 갈등을 초래할 수 있으므로, WTO 규정 준수 여부와 보상 협상 과정을 명확히 전달해야 합니다. 또한 한-베 FTA 등 통상협정에서 세이프가드 발동 요건이 더 엄격할 수 있음을 주의해야 합니다.",
            "commonMistakes": [
                {
                    "mistake": "'세이프가드'를 'biện pháp bảo vệ'로 번역",
                    "correction": "'Biện pháp tự vệ' 또는 'safeguard'",
                    "explanation": "'Bảo vệ'는 일반 보호, 'tự vệ'는 긴급 자구책을 의미합니다."
                },
                {
                    "mistake": "세이프가드와 반덤핑을 구분하지 않고 'biện pháp phòng vệ'로 통칭",
                    "correction": "세이프가드는 'biện pháp tự vệ', 반덤핑은 'chống bán phá giá'",
                    "explanation": "발동 요건과 법적 근거가 다르므로 명확히 구분해야 합니다."
                },
                {
                    "mistake": "'긴급관세'를 'thuế khẩn cấp'으로만 번역",
                    "correction": "'Thuế tự vệ' 또는 'safeguard duty'",
                    "explanation": "세이프가드 조치로 부과되는 관세는 'thuế tự vệ'로 표현합니다."
                }
            ],
            "examples": [
                {
                    "ko": "수입 급증으로 세이프가드 조치가 발동되었습니다.",
                    "vi": "Biện pháp tự vệ đã được kích hoạt do nhập khẩu tăng đột biến.",
                    "situation": "formal"
                },
                {
                    "ko": "세이프가드는 반덤핑과 달리 불공정 행위 입증이 불필요합니다.",
                    "vi": "Biện pháp tự vệ không cần chứng minh hành vi không công bằng như chống bán phá giá.",
                    "situation": "formal"
                },
                {
                    "ko": "세이프가드 발동 시 영향 받는 국가에 보상을 제공해야 합니다.",
                    "vi": "Khi áp biện pháp tự vệ, phải cung cấp bồi thường cho các nước bị ảnh hưởng.",
                    "situation": "formal"
                }
            ],
            "relatedTerms": ["chong-ban-pha-gia", "hiep-dinh-thuong-mai", "dieu-uoc-quoc-te"]
        },
        {
            "slug": "quyen-mien-tru-ngoai-giao",
            "korean": "외교면제특권",
            "vietnamese": "quyền miễn trừ ngoại giao",
            "hanja": "外交免除特權",
            "hanjaReading": "外(밖 외) + 交(사귈 교) + 免(면할 면) + 除(덜 제) + 特(특별할 특) + 權(권세 권)",
            "pronunciation": "꿴미엔뜨 응와이지아오",
            "meaningKo": "외교관과 그 가족이 접수국의 형사·민사 재판권 및 행정관할권으로부터 면제되는 특권으로, 비엔나협약에 규정되어 있습니다. 통역 시 주의할 점은 면제 범위가 외교관의 직급과 가족관계에 따라 다르며, 접수국이 면제를 포기하도록 요청할 수 있다는 것입니다. 한국과 베트남 모두 비엔나협약 당사국이지만, 외교관 특권 남용 사례(교통사고, 체납 등)에 대한 사회적 논란이 있으므로 통역 시 민감하게 다뤄야 합니다. 외교면제특권은 영사관까지 확대되지 않으며, 영사는 제한적 면제만 누린다는 점도 설명할 수 있어야 합니다.",
            "meaningVi": "Đặc quyền miễn trừ khỏi quyền tài phán hình sự, dân sự và hành chính của nước tiếp nhận, dành cho nhà ngoại giao và gia đình theo Công ước Vienna. Phạm vi miễn trừ phụ thuộc vào cấp bậc ngoại giao và không áp dụng cho lãnh sự (chỉ miễn trừ hạn chế).",
            "context": "외교, 국제법, 영사업무",
            "culturalNote": "한국에서는 외교관의 교통법규 위반이나 주차위반 등 경미한 위반 사례가 언론에 자주 보도되며, 외교부가 해당 공관에 시정을 요청합니다. 베트남도 유사한 문제가 있으나, 외교 관례상 공개적 비판보다는 외교 경로를 통한 조용한 해결을 선호합니다. 통역 시 외교면제특권 남용 사례를 언급할 때는 외교적 표현을 사용하고, 파견국이 자발적으로 면제를 포기하거나 외교관을 소환할 수 있음을 설명해야 합니다.",
            "commonMistakes": [
                {
                    "mistake": "'외교면제특권'을 'quyền đặc quyền ngoại giao'로 번역",
                    "correction": "'Quyền miễn trừ ngoại giao' 또는 'đặc quyền miễn trừ ngoại giao'",
                    "explanation": "'Đặc quyền'은 특권, 'miễn trừ'는 면제로, 정확히는 'miễn trừ'를 포함해야 합니다."
                },
                {
                    "mistake": "모든 대사관 직원이 면제특권을 누린다고 번역",
                    "correction": "외교관 직급과 행정·기술직 구분 필요",
                    "explanation": "행정직원은 제한적 면제만 누리며, 현지 채용 직원은 면제 대상이 아닙니다."
                },
                {
                    "mistake": "'영사'와 '외교관'의 면제 범위를 동일하게 번역",
                    "correction": "외교관은 포괄적 면제, 영사는 직무 관련 행위만 면제",
                    "explanation": "비엔나 외교관계협약과 영사관계협약의 규정이 다릅니다."
                }
            ],
            "examples": [
                {
                    "ko": "외교관은 외교면제특권으로 형사소추가 면제됩니다.",
                    "vi": "Nhà ngoại giao được miễn truy tố hình sự nhờ quyền miễn trừ ngoại giao.",
                    "situation": "formal"
                },
                {
                    "ko": "접수국은 외교관의 면제 포기를 요청할 수 있습니다.",
                    "vi": "Nước tiếp nhận có thể yêu cầu nước cử từ bỏ quyền miễn trừ của nhà ngoại giao.",
                    "situation": "formal"
                },
                {
                    "ko": "외교면제특권은 비엔나협약에 따라 보장됩니다.",
                    "vi": "Quyền miễn trừ ngoại giao được đảm bảo theo Công ước Vienna.",
                    "situation": "formal"
                }
            ],
            "relatedTerms": ["dieu-uoc-quoc-te", "cong-phap-quoc-te", "dan-do-toi-pham"]
        },
        {
            "slug": "dan-do-toi-pham",
            "korean": "범죄인인도",
            "vietnamese": "dẫn độ tội phạm",
            "hanja": "犯罪人引渡",
            "hanjaReading": "犯(범할 범) + 罪(허물 죄) + 人(사람 인) + 引(끌 인) + 渡(건널 도)",
            "pronunciation": "잔도또이팜",
            "meaningKo": "한 국가의 영역 내에 있는 범죄 혐의자나 기결수를 다른 국가의 요청에 따라 인도하는 제도로, 양국 간 범죄인인도조약이 체결되어 있어야 합니다. 통역 시 정치범 불인도 원칙, 자국민 불인도 원칙, 쌍방가벌성 원칙 등 인도 요건을 정확히 설명해야 합니다. 한국과 베트남은 범죄인인도조약을 체결하지 않았으나, UN 범죄방지협약 등 다자조약을 통해 제한적으로 인도가 가능합니다. 통역 현장에서는 도주범 인도 절차와 법원 심사 과정을 설명할 수 있어야 하며, 사형제도 차이로 인한 인도 거부 가능성도 언급해야 합니다.",
            "meaningVi": "Chế độ giao nộp người bị cáo buộc hoặc đã bị kết án tội phạm cho nước yêu cầu, căn cứ vào hiệp ước dẫn độ song phương. Nguyên tắc không dẫn độ tội phạm chính trị, công dân, và phạm tội phải bị trừng phạt ở cả hai nước (nguyên tắc hai bên cùng trừng phạt).",
            "context": "형사사법공조, 국제범죄, 도주범",
            "culturalNote": "한국은 미국·일본 등과 범죄인인도조약을 체결했으나, 자국민 불인도 원칙(헌법 제2조)으로 한국인은 원칙적으로 인도하지 않습니다. 베트남도 자국민 불인도 원칙을 채택하며, 사형제도를 유지하므로 사형 가능성이 있는 사건은 인도를 거부할 수 있습니다. 통역 시 양국의 인도 요건 차이를 설명하고, 대체 방안(형사사법공조, 정보 공유)을 제시할 수 있어야 합니다.",
            "commonMistakes": [
                {
                    "mistake": "'범죄인인도'를 'bàn giao tội phạm'으로 번역",
                    "correction": "'Dẫn độ tội phạm' 또는 'extradition'",
                    "explanation": "'Bàn giao'는 일반 인계, 'dẫn độ'는 법적 절차에 따른 인도를 의미합니다."
                },
                {
                    "mistake": "'정치범 불인도'를 'không dẫn độ tội phạm chính trị'로만 번역",
                    "correction": "'Nguyên tắc không dẫn độ tội phạm chính trị'",
                    "explanation": "국제법상 확립된 원칙임을 명확히 해야 합니다."
                },
                {
                    "mistake": "'쌍방가벌성'을 'hai bên đều trừng phạt'로 직역",
                    "correction": "'Nguyên tắc hai bên cùng trừng phạt' 또는 'dual criminality'",
                    "explanation": "법률 용어로 정확히 표현해야 합니다."
                }
            ],
            "examples": [
                {
                    "ko": "범죄인인도조약이 없으면 도주범을 인도할 수 없습니다.",
                    "vi": "Nếu không có hiệp ước dẫn độ, không thể giao nộp người trốn tội.",
                    "situation": "formal"
                },
                {
                    "ko": "정치범은 범죄인인도 대상에서 제외됩니다.",
                    "vi": "Tội phạm chính trị không thuộc đối tượng dẫn độ.",
                    "situation": "formal"
                },
                {
                    "ko": "쌍방가벌성 원칙에 따라 양국 모두 처벌 가능한 범죄만 인도됩니다.",
                    "vi": "Theo nguyên tắc hai bên cùng trừng phạt, chỉ dẫn độ tội phạm bị trừng phạt ở cả hai nước.",
                    "situation": "formal"
                }
            ],
            "relatedTerms": ["quyen-mien-tru-ngoai-giao", "dieu-uoc-quoc-te", "cong-phap-quoc-te"]
        },
        {
            "slug": "hiep-dinh-tranh-thue-kep",
            "korean": "이중과세방지협정",
            "vietnamese": "hiệp định tránh thuế kép",
            "hanja": "二重課稅防止協定",
            "hanjaReading": "二(두 이) + 重(무거울 중) + 課(과할 과) + 稅(세금 세) + 防(막을 방) + 止(그칠 지) + 協(화합할 협) + 定(정할 정)",
            "pronunciation": "히업딘짜인투에껩",
            "meaningKo": "양국에서 동일 소득에 대해 중복 과세되는 것을 방지하기 위한 조약으로, OECD 모델과 UN 모델을 기초로 체결됩니다. 통역 시 거주지국 과세 원칙, 원천지국 과세 원칙, 고정사업장(PE) 개념, 배당·이자·사용료의 원천징수세율 등 기술적 내용을 정확히 전달해야 합니다. 한국과 베트남은 이중과세방지협정을 체결했으며, 투자·무역 증가로 협정 해석과 적용 사례가 늘고 있습니다. 통역 현장에서는 특정 소득 유형(사업소득, 급여소득, 양도소득 등)의 과세권 배분 규칙을 설명할 수 있어야 합니다.",
            "meaningVi": "Hiệp định nhằm tránh việc đánh thuế hai lần đối với cùng một khoản thu nhập ở hai nước, dựa trên mô hình OECD và UN. Quy định về quyền đánh thuế theo nước cư trú và nước nguồn, khái niệm cơ sở thường trú (PE), và thuế suất khấu trừ đối với cổ tức, lãi, phí bản quyền.",
            "context": "국제조세, 외국인투자, 국제거래",
            "culturalNote": "한국은 OECD 회원국으로 OECD 모델을 선호하며, 거주지국 과세를 강조합니다. 베트남은 개발도상국으로 UN 모델을 선호하며, 원천지국(베트남) 과세권을 더 많이 확보하려 합니다. 통역 시 협정 개정 협상에서 이러한 입장 차이가 드러날 수 있으므로, 양국의 조세 정책 방향을 이해해야 합니다. 또한 고정사업장(PE) 인정 기준이 양국에서 다를 수 있으므로, 구체적 사례를 들어 설명하는 것이 효과적입니다.",
            "commonMistakes": [
                {
                    "mistake": "'이중과세'를 'đánh thuế hai lần'으로만 번역",
                    "correction": "'Thuế kép' 또는 'double taxation'",
                    "explanation": "'Thuế kép'이 국제조세 전문 용어입니다."
                },
                {
                    "mistake": "'고정사업장'을 'địa điểm kinh doanh cố định'으로 번역",
                    "correction": "'Cơ sở thường trú' 또는 'Permanent Establishment (PE)'",
                    "explanation": "협정상 정의된 용어는 'cơ sở thường trú'입니다."
                },
                {
                    "mistake": "'원천징수'를 'khấu trừ nguồn'으로 번역",
                    "correction": "'Khấu trừ tại nguồn' 또는 'withholding tax'",
                    "explanation": "'Tại nguồn'을 붙여 원천에서 공제한다는 의미를 명확히 해야 합니다."
                }
            ],
            "examples": [
                {
                    "ko": "이중과세방지협정에 따라 배당소득의 원천징수세율은 10%입니다.",
                    "vi": "Theo hiệp định tránh thuế kép, thuế suất khấu trừ tại nguồn đối với thu nhập cổ tức là 10%.",
                    "situation": "formal"
                },
                {
                    "ko": "고정사업장이 없으면 사업소득은 거주지국에서만 과세됩니다.",
                    "vi": "Nếu không có cơ sở thường trú, thu nhập kinh doanh chỉ bị đánh thuế ở nước cư trú.",
                    "situation": "formal"
                },
                {
                    "ko": "한-베 이중과세방지협정은 투자자 보호에 중요한 역할을 합니다.",
                    "vi": "Hiệp định tránh thuế kép Hàn-Việt đóng vai trò quan trọng trong bảo vệ nhà đầu tư.",
                    "situation": "formal"
                }
            ],
            "relatedTerms": ["dieu-uoc-quoc-te", "hiep-dinh-thuong-mai", "tu-phap-quoc-te"]
        }
    ]

    # 5. 중복 필터링
    new_terms_filtered = [t for t in new_terms if t['slug'] not in existing_slugs]

    # 6. 데이터 추가
    if new_terms_filtered:
        data.extend(new_terms_filtered)
        print(f"✅ {len(new_terms_filtered)}개 용어 추가됨")
    else:
        print("⚠️ 모든 용어가 이미 존재함 (중복)")

    # 7. 파일 저장
    with open(file_path, 'w', encoding='utf-8') as f:
        json.dump(data, f, ensure_ascii=False, indent=2)

    print(f"💾 저장 완료: {file_path}")
    print(f"📊 총 용어 수: {len(data)}개")

if __name__ == "__main__":
    main()
