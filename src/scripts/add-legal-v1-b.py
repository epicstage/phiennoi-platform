#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
형법/형사소송 용어 추가 스크립트 (Criminal Law/Criminal Procedure)
Tier S 품질 기준 준수
"""

import json
import os

# 파일 경로 설정 (CRITICAL RULE #1)
file_path = os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', 'data', 'terms', 'legal.json')

# 기존 데이터 로드
with open(file_path, 'r', encoding='utf-8') as f:
    data = json.load(f)  # data is a LIST (CRITICAL RULE #2)

# 기존 slug 확인 (CRITICAL RULE #4)
existing_slugs = {t['slug'] for t in data}

# 새 용어 정의 (10개)
new_terms = [
    {
        "slug": "toi-pham",
        "korean": "범죄",
        "vietnamese": "tội phạm",
        "hanja": "犯罪",
        "hanjaReading": "犯(범할 범) + 罪(죄 죄)",
        "pronunciation": "뻬암",
        "meaningKo": "법률에서 금지하는 행위로서 형벌의 대상이 되는 행위. 통역 시 '범죄'와 '犯罪者(범죄자)'를 명확히 구분해야 하며, 베트nam에서는 'tội phạm'이 행위와 사람 모두를 지칭할 수 있어 맥락에 따라 'hành vi tội phạm'(범죄행위) 또는 'người phạm tội'(범죄자)로 구분해 통역하는 것이 정확합니다. 형사법 통역에서 가장 기본이 되는 용어로, 법정 통역 시 반드시 정확하게 전달해야 합니다.",
        "meaningVi": "Hành vi bị pháp luật cấm và phải chịu hình phạt. Tội phạm là vi phạm pháp luật hình sự nghiêm trọng, khác với vi phạm hành chính. Trong thực tiễn tư pháp Hàn Quốc, tội phạm được phân loại thành nhiều loại như tội phạm bạo lực, tội phạm kinh tế, tội phạm ma túy, v.v.",
        "context": "형사법, 법정 통역, 사법 절차",
        "culturalNote": "한국은 '범죄'와 '범죄자'를 언어적으로 명확히 구분하지만, 베트남어에서는 'tội phạm'이 두 의미를 모두 포함할 수 있습니다. 한국의 형사법 체계는 대륙법계를 따르며, 범죄의 성립요건(구성요건, 위법성, 책임)을 엄격하게 구분합니다. 베트남도 유사한 법체계를 가지고 있으나, 실무적 접근에서 차이가 있을 수 있습니다. 통역 시 법률 개념의 정확한 전달이 피고인의 권리 보호에 직결됩니다.",
        "commonMistakes": [
            {
                "mistake": "tội phạm을 무조건 '범죄자'로만 번역",
                "correction": "맥락에 따라 '범죄' 또는 '범죄자'로 구분",
                "explanation": "베트남어 tội phạm은 행위와 사람 모두를 지칭할 수 있으므로, 한국어로 통역 시 문맥 파악 필수"
            },
            {
                "mistake": "vi phạm(위반)과 tội phạm(범죄)을 혼동",
                "correction": "vi phạm은 행정 위반, tội phạm은 형사 범죄",
                "explanation": "법적 중요도와 처벌 수위가 완전히 다르므로 정확한 구분 필요"
            },
            {
                "mistake": "죄(tội)와 범죄(tội phạm)를 동일시",
                "correction": "죄는 넓은 의미, 범죄는 형법상 처벌 대상 행위",
                "explanation": "종교적/도덕적 '죄'와 법적 '범죄'는 개념이 다름"
            }
        ],
        "examples": [
            {
                "ko": "피고인은 특정범죄가중처벌법 위반으로 기소되었습니다.",
                "vi": "Bị cáo bị khởi tố về tội vi phạm Luật Tăng nặng hình phạt đối với tội phạm đặc biệt.",
                "situation": "formal"
            },
            {
                "ko": "범죄 현장에서 발견된 증거를 확보하세요.",
                "vi": "Hãy bảo quản chứng cứ được phát hiện tại hiện trường vụ án.",
                "situation": "onsite"
            },
            {
                "ko": "이 행위는 형법상 범죄에 해당하지 않습니다.",
                "vi": "Hành vi này không cấu thành tội phạm theo Bộ luật Hình sự.",
                "situation": "formal"
            }
        ],
        "relatedTerms": ["hinh-phat", "khoi-to", "bi-cao", "chung-cu"]
    },
    {
        "slug": "hinh-phat",
        "korean": "형벌",
        "vietnamese": "hình phạt",
        "hanja": "刑罰",
        "hanjaReading": "刑(형벌 형) + 罰(벌할 벌)",
        "pronunciation": "힝팟",
        "meaningKo": "범죄에 대한 법적 제재로서 국가가 범죄자에게 가하는 처벌. 통역 시 주의할 점은 한국의 형벌 체계(사형, 징역, 금고, 자격상실, 자격정지, 벌금, 구류, 과료, 몰수)를 베트남어로 정확히 전달하는 것입니다. 특히 '징역'과 '금고'의 차이(노역 의무 유무), '벌금'과 '과료'의 차이(금액 규모)를 명확히 구분해 통역해야 하며, 양형 기준 통역 시 피고인이 정확히 이해할 수 있도록 구체적으로 설명하는 것이 중요합니다.",
        "meaningVi": "Hình phạt là biện pháp chế재 pháp lý mà nhà nước áp dụng đối với người phạm tội. Hệ thống hình phạt ở Hàn Quốc bao gồm tử hình, tù giam, phạt kim, tịch thu tài sản, v.v. Mức độ hình phạt được quy định cụ thể theo từng loại tội và tình tiết giảm nhẹ hoặc tăng nặng.",
        "context": "형사법, 양형, 판결",
        "culturalNote": "한국의 형벌 체계는 주형(사형, 징역, 금고, 자격상실, 자격정지, 벌금, 구류, 과료)과 부가형(몰수)으로 구분됩니다. 베트남도 유사한 체계를 가지고 있으나, 구체적인 형량 기준과 집행 방식에서 차이가 있습니다. 한국에서는 '징역형'이 가장 일반적인 자유형인 반면, 베트남에서는 'tù giam'이 이에 해당합니다. 통역 시 양국의 형벌 체계 차이를 이해하고, 피고인이 한국 법체계를 정확히 이해할 수 있도록 설명하는 것이 중요합니다.",
        "commonMistakes": [
            {
                "mistake": "징역과 금고를 모두 'tù giam'으로 통역",
                "correction": "징역은 'tù có lao động', 금고는 'tù không lao động'",
                "explanation": "노역 의무 유무가 핵심 차이이므로 명확히 구분해야 함"
            },
            {
                "mistake": "벌금(phạt kim)과 과료를 구분하지 않음",
                "correction": "벌금은 'tiền phạt lớn', 과료는 'tiền phạt nhỏ'로 구분",
                "explanation": "금액 규모와 적용 범죄의 경중이 다름"
            },
            {
                "mistake": "집행유예를 hình phạt의 일종으로 설명",
                "correction": "집행유예는 형벌의 집행을 유예하는 제도(án treo)",
                "explanation": "형벌 자체가 아니라 형벌 집행의 유예이므로 개념 구분 필요"
            }
        ],
        "examples": [
            {
                "ko": "법원은 피고인에게 징역 3년을 선고했습니다.",
                "vi": "Tòa án tuyên phạt bị cáo 3 năm tù có lao động.",
                "situation": "formal"
            },
            {
                "ko": "이 범죄의 법정형은 5년 이하의 징역 또는 3천만 원 이하의 벌금입니다.",
                "vi": "Khung hình phạt pháp định cho tội này là tù không quá 5 năm hoặc phạt tiền không quá 30 triệu won.",
                "situation": "formal"
            },
            {
                "ko": "형벌이 너무 과중하다고 생각하여 항소하겠습니다.",
                "vi": "Tôi sẽ kháng cáo vì cho rằng hình phạt quá nặng.",
                "situation": "informal"
            }
        ],
        "relatedTerms": ["toi-pham", "tu-chung-than", "an-treo", "phat-kim"]
    },
    {
        "slug": "tu-chung-than",
        "korean": "무기징역",
        "vietnamese": "tù chung thân",
        "hanja": "無期懲役",
        "hanjaReading": "無(없을 무) + 期(기약할 기) + 懲(징계할 징) + 役(부릴 역)",
        "pronunciation": "뚜중턴",
        "meaningKo": "기간을 정하지 않고 종신토록 교도소에 수용하는 자유형. 통역 시 주의할 점은 '무기징역'이 실제로는 가석방 가능성이 있다는 점입니다. 한국에서 무기수는 20년 복역 후 가석방 심사 대상이 되며, 이를 베트남어로 설명할 때 'tù chung thân'이 문자 그대로 '평생 수감'을 의미하지만 실제로는 가석방 제도가 있다는 점을 명확히 전달해야 합니다. 특히 중대 범죄 판결 통역 시 피고인과 가족이 정확히 이해할 수 있도록 구체적인 설명이 필요합니다.",
        "meaningVi": "Hình phạt tù không xác định thời hạn, tức là phải ở tù suốt đời. Tuy nhiên, ở Hàn Quốc, người bị phạt tù chung thân có thể được xem xét ân xá hoặc giảm án sau khi chấp hành ít nhất 20 năm tù. Đây là hình phạt nghiêm khắc chỉ áp dụng cho các tội danh đặc biệt nghiêm trọng như giết người có tính chất tàn bạo, tội phạm chiến tranh, v.v.",
        "context": "중범죄, 양형, 판결",
        "culturalNote": "한국의 무기징역은 사형 다음으로 무거운 형벌로, 실무상 20년 이상 복역 후 가석방 심사가 가능합니다. 베트남의 'tù chung thân'도 유사한 개념이나, 가석방 기준과 실제 적용에서 차이가 있을 수 있습니다. 한국에서는 무기수의 가석방이 매우 엄격하게 심사되며, 특히 살인, 강도살인 등 강력범죄의 경우 실제 가석방 비율이 낮습니다. 통역 시 이러한 현실을 피고인이 이해할 수 있도록 설명하는 것이 중요합니다.",
        "commonMistakes": [
            {
                "mistake": "무기징역을 '평생 출소 불가능'으로 설명",
                "correction": "20년 후 가석방 가능성이 있다고 정확히 전달",
                "explanation": "법적으로 가석방 제도가 있으므로 오해 없이 설명해야 함"
            },
            {
                "mistake": "사형과 무기징역을 혼동",
                "correction": "사형은 tử hình, 무기징역은 tù chung thân으로 명확히 구분",
                "explanation": "생명 박탈 여부에서 근본적 차이가 있음"
            },
            {
                "mistake": "유기징역과의 차이를 설명하지 않음",
                "correction": "유기징역(tù có thời hạn)은 기간이 정해진 것, 무기징역은 기간 미정",
                "explanation": "형량의 성격이 근본적으로 다르므로 구분 필요"
            }
        ],
        "examples": [
            {
                "ko": "피고인은 살인죄로 무기징역을 선고받았습니다.",
                "vi": "Bị cáo bị tuyên án tù chung thân về tội giết người.",
                "situation": "formal"
            },
            {
                "ko": "무기수도 20년 복역 후 가석방 심사를 받을 수 있습니다.",
                "vi": "Người bị phạt tù chung thân cũng có thể được xem xét ân xá sau 20 năm chấp hành án.",
                "situation": "formal"
            },
            {
                "ko": "이 사건의 죄질이 매우 나쁘므로 무기징역이 적절합니다.",
                "vi": "Tính chất tội ác của vụ án này rất nghiêm trọng nên hình phạt tù chung thân là thích hợp.",
                "situation": "formal"
            }
        ],
        "relatedTerms": ["hinh-phat", "tu-hinh", "an-tu", "an-treo"]
    },
    {
        "slug": "an-treo",
        "korean": "집행유예",
        "vietnamese": "án treo",
        "hanja": "執行猶豫",
        "hanjaReading": "執(잡을 집) + 行(다닐 행) + 猶(오히려 유) + 豫(미리 예)",
        "pronunciation": "안째오",
        "meaningKo": "형의 선고를 유예하거나 형의 집행을 일정 기간 유예하는 제도. 통역 시 매우 중요한 점은 한국의 집행유예가 '유예기간 중 재범하지 않으면 형 확정 효력이 상실'된다는 점입니다. 베트남어 'án treo'는 문자 그대로 '매달린 판결'이라는 의미로, 조건부로 유예된다는 개념을 잘 표현합니다. 통역 시 유예기간, 유예조건, 위반 시 집행 등을 구체적으로 설명해야 하며, 특히 '집행유예=무죄'가 아니라 '유죄이지만 형 집행을 유예받은 것'임을 명확히 전달해야 합니다.",
        "meaningVi": "Án treo là chế độ tạm hoãn thi hành án phạt trong một thời gian nhất định. Nếu người bị kết án không vi phạm điều kiện án treo trong thời gian thử thách, họ sẽ không phải chấp hành hình phạt. Tuy nhiên, nếu tái phạm trong thời gian án treo, họ sẽ phải chấp hành cả hình phạt cũ và hình phạt mới.",
        "context": "양형, 판결, 갱생",
        "culturalNote": "한국의 집행유예 제도는 초범이거나 정상참작의 여지가 있는 경우 사회 복귀 기회를 주기 위한 제도입니다. 3년 이하 징역형이나 500만 원 이하 벌금형을 선고받을 경우 1~5년간 집행을 유예할 수 있습니다. 베트남에도 유사한 'án treo' 제도가 있으나, 적용 기준과 유예기간이 다를 수 있습니다. 통역 시 피고인이 집행유예의 의미와 준수사항을 정확히 이해하도록 하는 것이 재범 방지에 중요합니다.",
        "commonMistakes": [
            {
                "mistake": "집행유예를 무죄 석방으로 오해",
                "correction": "유죄이지만 형 집행을 유예받은 것임을 명확히 설명",
                "explanation": "전과 기록에 남으며, 재범 시 형이 집행됨"
            },
            {
                "mistake": "유예기간과 형기를 혼동",
                "correction": "유예기간은 집행을 유예하는 기간, 형기는 선고받은 징역 기간",
                "explanation": "'징역 2년에 집행유예 3년'에서 2년은 형기, 3년은 유예기간"
            },
            {
                "mistake": "보호관찰 조건을 설명하지 않음",
                "correction": "집행유예 시 보호관찰이 병과될 수 있음을 전달",
                "explanation": "보호관찰 조건 위반 시에도 집행유예 취소 가능"
            }
        ],
        "examples": [
            {
                "ko": "피고인에게 징역 2년에 집행유예 3년을 선고합니다.",
                "vi": "Tuyên phạt bị cáo 2 năm tù, cho hưởng án treo 3 năm.",
                "situation": "formal"
            },
            {
                "ko": "집행유예기간 중 재범하면 이전 형까지 함께 집행됩니다.",
                "vi": "Nếu tái phạm trong thời gian án treo, sẽ phải chấp hành cả hình phạt trước đó.",
                "situation": "formal"
            },
            {
                "ko": "초범이고 반성하는 태도를 보여 집행유예를 받았어요.",
                "vi": "Vì là lần đầu phạm tội và thể hiện sự ăn năn nên được hưởng án treo.",
                "situation": "informal"
            }
        ],
        "relatedTerms": ["hinh-phat", "tu-chung-than", "bao-ho-quan-sat", "tai-pham"]
    },
    {
        "slug": "bat-giam",
        "korean": "구속",
        "vietnamese": "bắt giam",
        "hanja": "拘束",
        "hanjaReading": "拘(잡을 구) + 束(묶을 속)",
        "pronunciation": "밧잠",
        "meaningKo": "피의자나 피고인의 신체를 강제로 구금하여 도주를 방지하고 수사 및 재판을 원활하게 하는 강제처분. 통역 시 중요한 점은 구속은 '유죄 확정' 이전의 조치이므로 무죄추정의 원칙이 적용된다는 점입니다. 한국에서는 영장주의 원칙에 따라 법관이 발부한 구속영장이 있어야 하며, 구속 사유(도주 우려, 증거인멸 우려)가 명확해야 합니다. 베트남어로 통역 시 'bắt giam'이 임시 구금이며, 재판 결과에 따라 석방될 수 있음을 명확히 전달해야 하고, 구속적부심 등 구제절차도 함께 안내하는 것이 중요합니다.",
        "meaningVi": "Bắt giam là biện pháp tạm giam người bị tình nghi hoặc bị cáo để phục vụ điều tra và xét xử, ngăn chặn nguy cơ bỏ trốn hoặc tiêu hủy chứng cứ. Việc bắt giam phải có lệnh của Thẩm phán và chỉ áp dụng khi có căn cứ rõ ràng. Người bị bắt giam vẫn được coi là vô tội cho đến khi có bản án có hiệu lực.",
        "context": "형사소송, 수사, 미결구금",
        "culturalNote": "한국의 구속 제도는 헌법상 영장주의를 엄격히 적용합니다. 경찰이 체포한 후 48시간 내 검사에게 송치하고, 검사는 24시간 내 법원에 구속영장을 청구해야 합니다. 법관은 피의자를 직접 심문(구속적부심사)한 후 구속 여부를 결정합니다. 베트남도 유사한 절차가 있으나 구체적인 시간 제한과 심사 절차에서 차이가 있을 수 있습니다. 통역 시 피의자/피고인이 자신의 권리(변호인 선임권, 구속적부심 청구권 등)를 정확히 이해하도록 하는 것이 매우 중요합니다.",
        "commonMistakes": [
            {
                "mistake": "체포(bắt)와 구속(bắt giam)을 혼동",
                "correction": "체포는 단기 신병 확보, 구속은 장기 구금",
                "explanation": "체포는 48시간 이내, 구속은 재판 전까지 지속될 수 있음"
            },
            {
                "mistake": "구속을 유죄 확정으로 오해하게 통역",
                "correction": "구속은 재판 전 임시 조치이며, 무죄추정 원칙 적용",
                "explanation": "구속 중이어도 무죄 판결 가능성이 있음을 명확히 전달"
            },
            {
                "mistake": "구속적부심 제도를 설명하지 않음",
                "correction": "구속에 불복할 경우 법원에 심사 청구 가능",
                "explanation": "피의자의 중요한 권리구제 수단이므로 반드시 안내"
            }
        ],
        "examples": [
            {
                "ko": "법원은 도주 우려가 있다는 이유로 피의자에 대한 구속영장을 발부했습니다.",
                "vi": "Tòa án đã ra lệnh bắt giam nghi phạm vì có nguy cơ bỏ trốn.",
                "situation": "formal"
            },
            {
                "ko": "구속 후 10일 이내에 구속적부심을 청구할 수 있습니다.",
                "vi": "Trong vòng 10 ngày sau khi bị bắt giam, có thể yêu cầu Tòa án xem xét tính hợp pháp của việc bắt giam.",
                "situation": "formal"
            },
            {
                "ko": "증거불충분으로 구속영장이 기각되어 석방되었습니다.",
                "vi": "Lệnh bắt giam bị bác do không đủ chứng cứ nên đã được thả.",
                "situation": "informal"
            }
        ],
        "relatedTerms": ["che-po", "khoi-to", "dieu-tra", "anh-truong-bat-giam"]
    },
    {
        "slug": "khoi-to",
        "korean": "기소",
        "vietnamese": "khởi tố",
        "hanja": "起訴",
        "hanjaReading": "起(일어날 기) + 訴(호소할 소)",
        "pronunciation": "코이또",
        "meaningKo": "검사가 범죄 혐의가 있다고 판단하여 법원에 재판을 청구하는 소송행위. 통역 시 핵심은 '기소=재판 시작'을 의미하며, 이후 정식 재판 절차가 진행된다는 점입니다. 한국에서는 검사만이 기소권을 가지며(기소독점주의), 기소 후에는 피의자에서 피고인으로 신분이 변경됩니다. 베트남어 'khởi tố'는 '소송을 제기하다'는 의미로 정확히 대응되며, 통역 시 기소장 내용(공소사실, 적용법조), 공판 일정, 변호인 선임 필요성 등을 구체적으로 설명하는 것이 중요합니다. 특히 '불기소 처분'도 함께 설명하여 기소의 의미를 명확히 해야 합니다.",
        "meaningVi": "Khởi tố là hành vi Viện Kiểm sát đưa vụ án ra Tòa án để xét xử khi xác định có đủ căn cứ chứng minh hành vi phạm tội. Sau khi khởi tố, người bị tình nghi trở thành bị cáo và phải tham gia phiên tòa chính thức. Ở Hàn Quốc, chỉ có Viện Kiểm sát mới có quyền khởi tố (nguyên tắc độc quyền khởi tố).",
        "context": "형사소송, 공판, 검찰",
        "culturalNote": "한국의 기소 제도는 검사의 기소독점주의와 기소편의주의를 채택하고 있습니다. 검사는 범죄 혐의가 인정되더라도 정상참작의 여지가 있으면 불기소 처분할 수 있습니다(기소유예, 혐의없음, 죄가안됨, 공소권없음 등). 기소된 사건은 약 99%의 높은 유죄율을 보이므로, 기소 자체가 매우 중요한 단계입니다. 베트남도 유사한 제도가 있으나, 기소율과 유죄율에서 차이가 있을 수 있습니다. 통역 시 피고인이 기소의 법적 의미와 이후 절차를 정확히 이해하도록 하는 것이 중요합니다.",
        "commonMistakes": [
            {
                "mistake": "기소와 유죄 판결을 동일시",
                "correction": "기소는 재판 시작, 유죄는 재판 결과",
                "explanation": "기소 후에도 무죄 판결 가능성이 있음을 명확히 전달"
            },
            {
                "mistake": "약식기소와 정식기소를 구분하지 않음",
                "correction": "약식은 서면 심리, 정식은 공개 재판",
                "explanation": "절차와 형량 제한이 다르므로 구분 필요"
            },
            {
                "mistake": "불기소 처분의 종류를 설명하지 않음",
                "correction": "혐의없음, 기소유예, 죄가안됨 등 세부 구분 전달",
                "explanation": "불기소 유형에 따라 재기소 가능성이 다름"
            }
        ],
        "examples": [
            {
                "ko": "검사는 피의자를 사기죄로 정식 기소했습니다.",
                "vi": "Viện Kiểm sát đã chính thức khởi tố nghi phạm về tội lừa đảo.",
                "situation": "formal"
            },
            {
                "ko": "증거 부족으로 불기소 처분되었습니다.",
                "vi": "Đã được quyết định không khởi tố do thiếu chứng cứ.",
                "situation": "formal"
            },
            {
                "ko": "기소장에 명시된 공소사실을 확인하세요.",
                "vi": "Hãy xác nhận nội dung tội danh được ghi trong cáo trạng.",
                "situation": "formal"
            }
        ],
        "relatedTerms": ["bat-giam", "bi-cao", "cong-to-vien", "phien-toa"]
    },
    {
        "slug": "dieu-tra",
        "korean": "수사",
        "vietnamese": "điều tra",
        "hanja": "搜査",
        "hanjaReading": "搜(찾을 수) + 査(조사할 사)",
        "pronunciation": "지으짜",
        "meaningKo": "범죄 혐의가 있는 사건에 대해 증거를 수집하고 범인을 찾는 일련의 수사기관 활동. 통역 시 중요한 점은 한국의 수사 구조가 '경찰 수사 → 검찰 보완수사 → 기소'의 단계로 진행되며, 피의자는 수사 과정에서 진술거부권, 변호인 선임권 등 중요한 권리를 가진다는 점입니다. 베트남어 'điều tra'는 '조사하다'는 의미로 정확히 대응되며, 통역 시 조사 절차(출석 요구, 압수수색, 진술 조서 작성), 피의자 권리, 변호인 참여권 등을 구체적으로 설명해야 합니다. 특히 진술 내용이 재판 증거로 사용될 수 있음을 명확히 전달하는 것이 중요합니다.",
        "meaningVi": "Điều tra là hoạt động của cơ quan điều tra nhằm thu thập chứng cứ, xác minh sự việc và tìm ra thủ phạm trong các vụ án hình sự. Quá trình điều tra bao gồm triệu tập, lấy lời khai, khám xét, thu giữ chứng cứ, v.v. Người bị điều tra có quyền im lặng, quyền thuê luật sư và các quyền cơ bản khác được pháp luật bảo vệ.",
        "context": "형사소송, 경찰, 검찰",
        "culturalNote": "한국의 수사 제도는 경찰과 검찰이 각각 1차, 2차 수사권을 가지며, 검찰이 기소 여부를 최종 결정합니다. 2021년 형사소송법 개정으로 경찰의 수사권이 강화되고 검경 수사권 조정이 이루어졌습니다. 수사 과정에서 피의자는 헌법상 권리(진술거부권, 변호인 조력권)를 보장받으며, 위법수집증거는 증거능력이 배제됩니다. 베트남도 유사한 수사 절차가 있으나, 기관별 권한과 절차에서 차이가 있을 수 있습니다. 통역 시 피의자가 자신의 권리를 정확히 이해하고 행사할 수 있도록 하는 것이 핵심입니다.",
        "commonMistakes": [
            {
                "mistake": "조사(điều tra)와 심문(thẩm vấn)을 혼용",
                "correction": "조사는 수사기관, 심문은 법정에서 진행",
                "explanation": "절차와 법적 성격이 다르므로 명확히 구분"
            },
            {
                "mistake": "피의자의 진술거부권을 고지하지 않음",
                "correction": "진술거부권이 있으며 불리한 진술 강요 불가",
                "explanation": "헌법상 기본권이므로 반드시 고지해야 함"
            },
            {
                "mistake": "압수수색과 임의제출을 구분하지 않음",
                "correction": "압수수색은 영장 필요, 임의제출은 동의 필요",
                "explanation": "법적 요건과 효력이 다름"
            }
        ],
        "examples": [
            {
                "ko": "경찰이 사건 수사를 위해 용의자를 소환했습니다.",
                "vi": "Cảnh sát đã triệu tập nghi phạm để điều tra vụ án.",
                "situation": "formal"
            },
            {
                "ko": "수사 과정에서 결정적 증거가 발견되었습니다.",
                "vi": "Trong quá trình điều tra đã phát hiện chứng cứ quyết định.",
                "situation": "onsite"
            },
            {
                "ko": "변호사 입회하에 조사받을 권리가 있습니다.",
                "vi": "Bạn có quyền được điều tra với sự có mặt của luật sư.",
                "situation": "formal"
            }
        ],
        "relatedTerms": ["khoi-to", "chung-cu", "nhan-chung", "ap-su-thau-sach"]
    },
    {
        "slug": "chung-cu",
        "korean": "증거",
        "vietnamese": "chứng cứ",
        "hanja": "證據",
        "hanjaReading": "證(증거 증) + 據(근거 거)",
        "pronunciation": "쯩꾸",
        "meaningKo": "범죄 사실의 존재 여부를 증명하기 위한 모든 자료. 통역 시 핵심은 한국 형사소송법상 증거의 종류(물적 증거, 인적 증거)와 증거능력의 개념입니다. 특히 '위법수집증거 배제법칙'이 적용되어 적법한 절차 없이 수집된 증거는 재판에서 사용할 수 없다는 점을 명확히 전달해야 합니다. 베트남어 'chứng cứ'는 '증명하는 근거'라는 의미로 정확히 대응되며, 통역 시 증거 종류(진술조서, 감정서, 압수물, CCTV 등), 증거조사 절차, 증거능력과 증명력의 차이를 구체적으로 설명하는 것이 중요합니다.",
        "meaningVi": "Chứng cứ là tất cả các tài liệu, vật chứng và lời khai được sử dụng để chứng minh sự tồn tại của tội phạm trong tố tụng hình sự. Chứng cứ phải được thu thập hợp pháp mới có giá trị pháp lý. Các loại chứng cứ bao gồm vật chứng, lời khai nhân chứng, giám định, hình ảnh camera, v.v.",
        "context": "형사소송, 재판, 입증",
        "culturalNote": "한국의 증거법은 '엄격한 증명'과 '자유로운 증명'을 구분하며, 범죄사실은 엄격한 증명(적법한 증거조사 절차 필수)의 대상입니다. 증거능력(법정에서 사용 가능 여부)과 증명력(얼마나 신빙성이 있는지)을 구분하며, 위법수집증거, 전문증거(hearsay) 등은 증거능력이 제한됩니다. 또한 '자백은 보강증거가 있어야 유죄의 증거가 된다'는 원칙(자백보강법칙)이 있습니다. 베트남도 유사한 증거법 체계가 있으나, 세부 규칙에서 차이가 있을 수 있습니다.",
        "commonMistakes": [
            {
                "mistake": "증거능력과 증명력을 혼동",
                "correction": "증거능력은 사용 가능 여부, 증명력은 신빙성 정도",
                "explanation": "법적 개념이 다르므로 명확히 구분해야 함"
            },
            {
                "mistake": "자백만으로 유죄 입증 가능하다고 설명",
                "correction": "자백은 보강증거가 있어야 유죄 인정 가능",
                "explanation": "자백보강법칙을 반드시 설명해야 함"
            },
            {
                "mistake": "위법수집증거도 사용 가능하다고 오해",
                "correction": "적법한 절차로 수집된 증거만 증거능력 인정",
                "explanation": "피의자 권리 보호를 위한 중요한 원칙"
            }
        ],
        "examples": [
            {
                "ko": "현장에서 발견된 지문이 결정적 증거가 되었습니다.",
                "vi": "Dấu vân tay phát hiện tại hiện trường đã trở thành chứng cứ quyết định.",
                "situation": "formal"
            },
            {
                "ko": "CCTV 영상은 중요한 물적 증거입니다.",
                "vi": "Video camera an ninh là chứng cứ vật chất quan trọng.",
                "situation": "onsite"
            },
            {
                "ko": "증거 불충분으로 무죄 판결이 났습니다.",
                "vi": "Đã có phán quyết vô tội do không đủ chứng cứ.",
                "situation": "formal"
            }
        ],
        "relatedTerms": ["dieu-tra", "nhan-chung", "vat-chung", "ap-su-thau-sach"]
    },
    {
        "slug": "nhan-chung",
        "korean": "증인",
        "vietnamese": "nhân chứng",
        "hanja": "證人",
        "hanjaReading": "證(증거 증) + 人(사람 인)",
        "pronunciation": "년쯩",
        "meaningKo": "범죄 사실이나 관련 정황에 대해 자신이 직접 경험한 사실을 진술하는 사람. 통역 시 핵심은 증인의 의무(출석의무, 선서의무, 증언의무)와 권리(증언거부권, 신변보호 요청권)입니다. 한국에서는 증인이 정당한 이유 없이 출석하지 않거나 위증할 경우 처벌받을 수 있으며, 특히 위증죄는 5년 이하 징역으로 처벌됩니다. 베트남어 'nhân chứng'은 '사람 증거'라는 의미로 정확히 대응되며, 통역 시 증인 선서 내용, 위증의 법적 결과, 증인 보호 제도 등을 구체적으로 설명하는 것이 중요합니다.",
        "meaningVi": "Nhân chứng là người trực tiếp chứng kiến hoặc biết được sự việc liên quan đến vụ án và phải khai báo sự thật trước Tòa án. Nhân chứng có nghĩa vụ ra tòa, tuyên thệ và khai thật. Nếu khai man (khai gian) sẽ bị xử phạt tội làm chứng gian. Nhân chứng cũng có quyền từ chối khai báo trong một số trường hợp đặc biệt (như người thân của bị cáo).",
        "context": "형사소송, 재판, 증거조사",
        "culturalNote": "한국의 증인 제도는 증인의 출석과 선서를 의무화하며, 증인 신문은 주신문(신청한 당사자), 반대신문(상대방), 재신문 순으로 진행됩니다. 증인은 자기 또는 가족이 형사처벌이나 형사소추를 받을 우려가 있는 사항에 대해 증언을 거부할 수 있습니다(증언거부권). 또한 성폭력 사건 피해자 등 보호가 필요한 증인에 대해서는 신변보호, 영상증언, 증인신문 비공개 등의 조치가 가능합니다. 베트남도 유사한 제도가 있으나 세부 절차에서 차이가 있을 수 있습니다.",
        "commonMistakes": [
            {
                "mistake": "참고인과 증인을 혼동",
                "correction": "참고인은 수사단계, 증인은 재판단계",
                "explanation": "법적 의무와 처벌 규정이 다름"
            },
            {
                "mistake": "증언거부권을 설명하지 않음",
                "correction": "가족 등 일정한 경우 증언 거부 가능",
                "explanation": "증인의 중요한 권리이므로 반드시 고지"
            },
            {
                "mistake": "위증죄의 처벌을 경고하지 않음",
                "correction": "위증 시 5년 이하 징역 처벌 가능",
                "explanation": "증인이 진실 증언의 중요성을 인식하도록 해야 함"
            }
        ],
        "examples": [
            {
                "ko": "사건 당시 현장에 있던 목격자를 증인으로 신청했습니다.",
                "vi": "Đã đề nghị triệu tập người chứng kiến hiện trường làm nhân chứng.",
                "situation": "formal"
            },
            {
                "ko": "증인은 선서 후 자신이 본 사실을 있는 그대로 진술해야 합니다.",
                "vi": "Nhân chứng sau khi tuyên thệ phải khai báo đúng sự thật mà mình đã chứng kiến.",
                "situation": "formal"
            },
            {
                "ko": "배우자는 증언을 거부할 수 있는 권리가 있습니다.",
                "vi": "Vợ/chồng có quyền từ chối làm chứng.",
                "situation": "formal"
            }
        ],
        "relatedTerms": ["chung-cu", "phien-toa", "vi-chung", "bao-ho-nhan-chung"]
    },
    {
        "slug": "bi-cao",
        "korean": "피고인",
        "vietnamese": "bị cáo",
        "hanja": "被告人",
        "hanjaReading": "被(입을 피) + 告(고할 고) + 人(사람 인)",
        "pronunciation": "비까오",
        "meaningKo": "기소되어 형사재판을 받고 있는 사람. 통역 시 매우 중요한 점은 피고인은 '유죄가 확정되지 않은 상태'이므로 무죄추정의 원칙이 적용된다는 점입니다. 피고인은 진술거부권, 변호인 조력권, 증거에 대한 반박권 등 헌법상 기본권을 보장받으며, 유죄 입증 책임은 검사에게 있습니다. 베트남어 'bị cáo'는 '고소당한 사람'이라는 의미로 정확히 대응되며, 통역 시 피고인의 권리(묵비권, 변론권, 최종진술권), 재판 절차, 판결의 종류(유죄/무죄/면소) 등을 구체적으로 설명하는 것이 중요합니다.",
        "meaningVi": "Bị cáo là người bị Viện Kiểm sát khởi tố và đang được Tòa án xét xử. Bị cáo được coi là vô tội cho đến khi có bản án có hiệu lực pháp luật (nguyên tắc suy đoán vô tội). Bị cáo có các quyền cơ bản như quyền im lặng, quyền được luật sư bảo vệ, quyền phản bác chứng cứ, quyền trình bày ý kiến cuối cùng trước khi tuyên án.",
        "context": "형사재판, 공판, 피고인 권리",
        "culturalNote": "한국 형사소송법은 피고인의 권리를 헌법적으로 두텁게 보호합니다. 무죄추정의 원칙(헌법 제27조4항)에 따라 유죄 판결이 확정되기 전까지는 무죄로 추정되며, '의심스러울 때는 피고인의 이익으로(in dubio pro reo)' 원칙이 적용됩니다. 피고인은 모든 공판기일에 출석하여 진술할 권리가 있으며, 최종진술권을 통해 재판부에 직접 호소할 기회를 갖습니다. 베트남도 유사한 피고인 권리 보장 체계가 있으나, 실무적 운영에서 차이가 있을 수 있습니다.",
        "commonMistakes": [
            {
                "mistake": "피의자와 피고인을 혼용",
                "correction": "피의자는 수사단계, 피고인은 재판단계",
                "explanation": "기소를 기준으로 명확히 구분해야 함"
            },
            {
                "mistake": "피고인을 범인으로 단정적으로 지칭",
                "correction": "무죄추정 원칙상 '혐의를 받는 사람'으로 표현",
                "explanation": "유죄 확정 전까지는 범인이 아님"
            },
            {
                "mistake": "피고인의 최종진술권을 고지하지 않음",
                "correction": "판결 전 최종진술 기회가 있음을 안내",
                "explanation": "피고인의 중요한 절차적 권리"
            }
        ],
        "examples": [
            {
                "ko": "피고인은 검사의 주장에 대해 반박할 권리가 있습니다.",
                "vi": "Bị cáo có quyền phản bác các cáo buộc của Viện Kiểm sát.",
                "situation": "formal"
            },
            {
                "ko": "피고인에게 최종진술 기회를 드리겠습니다.",
                "vi": "Tôi sẽ cho bị cáo cơ hội trình bày ý kiến cuối cùng.",
                "situation": "formal"
            },
            {
                "ko": "피고인은 유죄 판결이 확정될 때까지 무죄로 추정됩니다.",
                "vi": "Bị cáo được coi là vô tội cho đến khi bản án có tội có hiệu lực.",
                "situation": "formal"
            }
        ],
        "relatedTerms": ["khoi-to", "phien-toa", "luat-su-bao-chua", "ban-an"]
    }
]

# 중복 제거 (CRITICAL RULE #5)
filtered_terms = [term for term in new_terms if term['slug'] not in existing_slugs]

if not filtered_terms:
    print("⚠️  모든 용어가 이미 존재합니다. 추가할 항목이 없습니다.")
else:
    # 기존 데이터에 추가
    data.extend(filtered_terms)

    # 파일 저장
    with open(file_path, 'w', encoding='utf-8') as f:
        json.dump(data, f, ensure_ascii=False, indent=2)

    print(f"✅ {len(filtered_terms)}개 형법/형사소송 용어 추가 완료!")
    print(f"📊 총 용어 수: {len(data)}개")
    print("\n추가된 용어:")
    for term in filtered_terms:
        print(f"  - {term['slug']}: {term['korean']} ({term['vietnamese']})")
