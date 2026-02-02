#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
건설현장 안전장비/PPE 용어 추가 스크립트
테마: 안전화, 보안경, 방진마스크, 귀마개, 안전장갑, 반사조끼, 안전고리, 안전표지판, 경고등, 바리케이드
"""

import json
import os

# Tier S 기준 충족 용어 데이터
data = [
    {
        "slug": "giay-bao-ho-lao-dong",
        "korean": "안전화",
        "vietnamese": "Giày bảo hộ lao động",
        "hanja": "安全靴",
        "hanjaReading": "安(편안할 안) + 全(온전할 전) + 靴(신 화)",
        "pronunciation": "안전화",
        "meaningKo": "건설 현장에서 발을 보호하기 위해 착용하는 작업용 신발로, 발가락 부분에 강철 또는 합성수지 재질의 안전캡이 내장되어 있고 바닥은 미끄럼 방지 처리가 되어 있습니다. 통역 시 주의할 점은 베트남어로 단순히 'giày' (신발)가 아니라 'giày bảo hộ lao động'으로 정확히 표현해야 하며, 한국에서는 '안전화' 또는 '안전 작업화'로 통일해서 사용합니다. 현장에서 '작업화'라고만 하면 안전 기능이 없는 일반 작업용 신발로 오해될 수 있으므로 반드시 '안전'을 강조해야 합니다. 베트남 현장에서는 'giày sắt'(철 신발)이라고 구어체로 부르기도 하지만 공식 문서에서는 'giày bảo hộ'를 사용합니다.",
        "meaningVi": "Giày bảo hộ lao động là loại giày chuyên dụng được thiết kế để bảo vệ bàn chân của công nhân tại công trường xây dựng. Đặc điểm quan trọng là có đầu giày làm bằng thép hoặc vật liệu tổng hợp để chống đập, đế chống trượt và có khả năng chống đinh xuyên thủng. Tại Hàn Quốc, loại giày này được gọi là '안전화' (an-jeon-hwa) và là trang bị bắt buộc tại mọi công trường.",
        "context": "건설 현장 안전 교육, PPE 지급 및 착용 점검, 산업안전보건법 준수",
        "culturalNote": "한국 건설 현장에서는 안전화 착용이 법적 의무사항이며 착용하지 않으면 현장 출입이 불가능합니다. 안전화 규격(KS M 6685)을 준수해야 하며 정기적인 점검이 필요합니다. 베트남에서도 최근 안전 규정이 강화되고 있지만 한국만큼 엄격하지는 않습니다. 통역 시 한국의 높은 안전 기준을 강조하고, 베트남 근로자들에게 착용 의무를 명확히 전달해야 합니다. 한국에서는 회사에서 지급하는 것이 일반적이지만 베트남에서는 개인이 구매하는 경우도 있어 이 차이를 설명해야 합니다.",
        "commonMistakes": [
            {
                "mistake": "'작업화'로만 통역",
                "correction": "'안전화' 또는 '안전 작업화'",
                "explanation": "단순 작업화는 안전 기능이 없을 수 있으므로 '안전'을 반드시 명시해야 합니다."
            },
            {
                "mistake": "'giày sắt'로 통역",
                "correction": "'giày bảo hộ lao động'",
                "explanation": "'giày sắt'는 구어체로 공식 안전 교육이나 문서에서는 부적절합니다."
            },
            {
                "mistake": "안전화 규격 설명 생략",
                "correction": "KS 규격 및 안전 등급 설명 포함",
                "explanation": "한국은 규격을 매우 중요하게 여기므로 통역 시 반드시 언급해야 합니다."
            }
        ],
        "examples": [
            {
                "ko": "현장 출입 전 반드시 안전화를 착용하고 끈을 단단히 묶으십시오.",
                "vi": "Trước khi vào công trường, bắt buộc phải đi giày bảo hộ lao động và thắt dây chặt.",
                "situation": "onsite"
            },
            {
                "ko": "안전화는 6개월마다 상태를 점검하고 손상된 경우 즉시 교체해야 합니다.",
                "vi": "Giày bảo hộ phải được kiểm tra tình trạng 6 tháng một lần và thay thế ngay nếu bị hư hỏng.",
                "situation": "formal"
            },
            {
                "ko": "오늘 안전화 안 신고 들어온 사람 있어? 다시 나가서 신고 와.",
                "vi": "Hôm nay có ai vào mà không đi giày bảo hộ không? Ra ngoài đi lại đi.",
                "situation": "informal"
            }
        ],
        "relatedTerms": ["안전모", "안전 장갑", "작업복", "개인 보호 장비", "산업안전보건법"]
    },
    {
        "slug": "kinh-bao-ho",
        "korean": "보안경",
        "vietnamese": "Kính bảo hộ",
        "hanja": "保眼鏡",
        "hanjaReading": "保(지킬 보) + 眼(눈 안) + 鏡(거울 경)",
        "pronunciation": "보안경",
        "meaningKo": "건설 현장에서 비산물, 먼지, 화학물질, 용접 불꽃 등으로부터 눈을 보호하기 위해 착용하는 안전 장비입니다. 통역 시 주의할 점은 한국에서 '보안경'과 '안전 고글'을 구분하여 사용하는데, 보안경은 일반 안경 형태이고 고글은 얼굴에 밀착되는 형태입니다. 베트남어로는 보안경을 'kính bảo hộ', 고글을 'kính chống bụi'로 구분하지만 현장에서는 혼용되기도 합니다. 용접 작업 시에는 일반 보안경이 아닌 용접용 보안경(kính hàn)을 착용해야 하며 이를 명확히 구분해 통역해야 합니다. 한국 산업안전보건 기준에서는 작업 종류에 따라 보안경 등급이 다르므로 이를 정확히 전달하는 것이 중요합니다.",
        "meaningVi": "Kính bảo hộ là thiết bị an toàn được đeo để bảo vệ mắt khỏi các mảnh vụn bay, bụi, hóa chất và tia lửa hàn tại công trường xây dựng. Có nhiều loại kính bảo hộ khác nhau tùy theo loại công việc: kính bảo hộ thông thường cho công việc chung, kính chống bụi kín cho môi trường nhiều bụi, và kính hàn cho công việc hàn điện. Tại Hàn Quốc, việc đeo kính bảo hộ là bắt buộc theo luật an toàn lao động.",
        "context": "건설 현장 안전 교육, 용접 작업, 연삭 작업, 화학물질 취급",
        "culturalNote": "한국 건설 현장에서는 작업 특성에 따라 보안경 종류를 엄격히 구분하며, 특히 용접 작업 시 일반 보안경 착용은 금지됩니다. 보안경 착용을 거부하거나 규격에 맞지 않는 제품 사용 시 작업 중지 조치가 내려집니다. 베트남에서는 보안경 착용 문화가 한국만큼 정착되지 않아 근로자들이 불편함을 이유로 착용을 꺼리는 경우가 많습니다. 통역 시 한국의 안전 기준이 매우 엄격하며 위반 시 개인과 회사 모두에게 법적 처벌이 있다는 점을 강조해야 합니다.",
        "commonMistakes": [
            {
                "mistake": "'안경'으로만 통역",
                "correction": "'보안경' 또는 '안전 보안경'",
                "explanation": "일반 안경과 구분하기 위해 '보안경'이라는 용어를 정확히 사용해야 합니다."
            },
            {
                "mistake": "고글과 보안경을 혼용",
                "correction": "형태에 따라 명확히 구분",
                "explanation": "보안경(안경형)과 고글(밀착형)은 용도가 다르므로 정확히 구분해야 합니다."
            },
            {
                "mistake": "용접용 보안경을 일반 보안경으로 통역",
                "correction": "'용접용 보안경' 또는 'kính hàn'으로 명시",
                "explanation": "용접 작업은 특수 보안경이 필요하므로 반드시 구분해야 합니다."
            }
        ],
        "examples": [
            {
                "ko": "연삭 작업 시에는 반드시 측면 보호대가 있는 보안경을 착용하세요.",
                "vi": "Khi làm công việc mài, bắt buộc phải đeo kính bảo hộ có tấm chắn bên hông.",
                "situation": "onsite"
            },
            {
                "ko": "보안경이 흠집이 나거나 깨진 경우 즉시 새 것으로 교체해야 합니다.",
                "vi": "Nếu kính bảo hộ bị xước hoặc vỡ, phải thay ngay bằng kính mới.",
                "situation": "formal"
            },
            {
                "ko": "야, 보안경 안 쓰고 뭐 하는 거야? 당장 쓰고 와!",
                "vi": "Này, làm gì mà không đeo kính bảo hộ? Đeo ngay đi!",
                "situation": "informal"
            }
        ],
        "relatedTerms": ["안전 고글", "용접 마스크", "개인 보호 장비", "안전화", "안전모"]
    },
    {
        "slug": "khau-trang-chong-bui",
        "korean": "방진마스크",
        "vietnamese": "Khẩu trang chống bụi",
        "hanja": "防塵mask",
        "hanjaReading": "防(막을 방) + 塵(티끌 진) + mask(외래어)",
        "pronunciation": "방진마스크",
        "meaningKo": "건설 현장에서 비산 먼지, 분진, 유해 가스 등을 차단하여 호흡기를 보호하는 안전 장비로, 일회용과 재사용 가능한 타입으로 구분됩니다. 통역 시 주의할 점은 한국에서는 '방진마스크', '방독면', '분진마스크'를 작업 환경에 따라 구분하여 사용하는데, 방진마스크는 고체 분진 차단용, 방독면은 가스/증기 차단용입니다. 베트남어로는 'khẩu trang chống bụi'(방진), 'mặt nạ phòng độc'(방독)으로 구분합니다. 한국의 KF(Korea Filter) 등급 체계를 베트nam 근로자에게 설명할 때는 'KF94는 미세먼지 94% 차단'처럼 구체적 수치로 전달해야 이해가 쉽습니다. 석면 작업이나 유해 화학물질 작업 시에는 일반 방진마스크가 아닌 특급 또는 방독면을 착용해야 하며 이를 명확히 구분해 통역해야 합니다.",
        "meaningVi": "Khẩu trang chống bụi là thiết bị bảo vệ hô hấp nhằm ngăn chặn bụi, phấn và khí độc hại tại công trường xây dựng. Có hai loại chính: khẩu trang dùng một lần và khẩu trang có thể tái sử dụng với bộ lọc thay thế. Tại Hàn Quốc, khẩu trang được phân loại theo tiêu chuẩn KF (Korea Filter) với các cấp độ lọc khác nhau: KF80, KF94, KF99. Đối với công việc tiếp xúc với amiăng hoặc hóa chất độc hại, phải sử dụng mặt nạ phòng độc thay vì khẩu trang thông thường.",
        "context": "건설 현장 분진 작업, 해체 작업, 도장 작업, 석면 제거 작업",
        "culturalNote": "한국 건설 현장에서는 미세먼지 농도가 높은 날이나 분진 발생 작업 시 방진마스크 착용이 의무화되어 있으며, 작업 특성에 따라 최소 KF 등급이 정해져 있습니다. 특히 석면 작업은 특급 방진마스크 또는 전면형 방독면을 착용해야 합니다. 베트남에서는 마스크 착용 문화가 비교적 친숙하지만(오토바이 운전 시 착용) 작업용 고등급 방진마스크에 대한 인식은 낮은 편입니다. 통역 시 한국의 엄격한 분진 관리 기준과 등급별 차이를 명확히 설명하고, 일회용 마스크의 교체 주기(보통 8시간 또는 하루)를 강조해야 합니다.",
        "commonMistakes": [
            {
                "mistake": "일반 마스크를 방진마스크로 통역",
                "correction": "KF 등급이 있는 방진마스크로 명시",
                "explanation": "일반 의료용 마스크는 분진 차단 효과가 없으므로 작업용 방진마스크와 구분해야 합니다."
            },
            {
                "mistake": "방진마스크와 방독면을 혼용",
                "correction": "먼지 차단은 방진마스크, 가스 차단은 방독면으로 구분",
                "explanation": "차단 대상이 다르므로 작업 환경에 맞는 장비를 명확히 통역해야 합니다."
            },
            {
                "mistake": "KF 등급 설명 생략",
                "correction": "등급별 차단율을 구체적으로 설명",
                "explanation": "베트남 근로자가 등급의 중요성을 이해하도록 수치로 설명해야 합니다."
            }
        ],
        "examples": [
            {
                "ko": "해체 작업 시 KF94 이상 방진마스크를 착용하고 8시간마다 교체하십시오.",
                "vi": "Khi làm công việc phá dỡ, phải đeo khẩu trang chống bụi KF94 trở lên và thay mới sau mỗi 8 giờ.",
                "situation": "onsite"
            },
            {
                "ko": "석면 제거 작업에는 일반 방진마스크가 아닌 전면형 방독면을 착용해야 합니다.",
                "vi": "Đối với công việc tháo dỡ amiăng, phải sử dụng mặt nạ phòng độc toàn mặt, không được dùng khẩu trang chống bụi thông thường.",
                "situation": "formal"
            },
            {
                "ko": "먼지 많이 나니까 마스크 꼭 끼고 작업해. 안 그러면 폐 망가져.",
                "vi": "Bụi nhiều lắm nên nhớ đeo khẩu trang khi làm việc nhé. Không là phổi hỏng đấy.",
                "situation": "informal"
            }
        ],
        "relatedTerms": ["방독면", "분진마스크", "개인 보호 장비", "석면 작업", "KF등급"]
    },
    {
        "slug": "nut-tai-chong-on",
        "korean": "귀마개",
        "vietnamese": "Nút tai chống ồn",
        "hanja": None,
        "hanjaReading": None,
        "pronunciation": "귀마개",
        "meaningKo": "건설 현장에서 과도한 소음으로부터 청력을 보호하기 위해 귀에 삽입하거나 귀를 덮는 형태의 안전 장비입니다. 통역 시 주의할 점은 한국에서 '귀마개'와 '귀덮개(이어머프)'를 형태에 따라 구분하는데, 귀마개는 귀 안에 삽입하는 폼 타입 또는 실리콘 타입이고 귀덮개는 헤드셋처럼 귀를 덮는 형태입니다. 베트남어로는 귀마개를 'nút tai'(삽입형), 귀덮개를 'ốp tai' 또는 'bịt tai kiểu vòng đeo'로 구분합니다. 한국 산업안전보건 기준에서는 85dB 이상의 소음 작업장에서는 청력 보호구 착용이 의무이며, 소음 수준에 따라 요구되는 차음 등급(NRR: Noise Reduction Rating)이 다릅니다. 통역 시 dB(데시벨)과 NRR 수치를 정확히 전달하고, 귀마개를 올바르게 착용하지 않으면 보호 효과가 크게 떨어진다는 점을 강조해야 합니다.",
        "meaningVi": "Nút tai chống ồn là thiết bị bảo vệ thính giác được đeo để giảm thiểu tiếng ồn quá mức tại công trường xây dựng. Có hai loại chính: nút tai (loại bỏ vào trong tai, làm bằng xốp hoặc silicone) và ốp tai (loại đeo như tai nghe, bao bọc toàn bộ tai). Tại Hàn Quốc, theo luật an toàn lao động, bắt buộc phải đeo thiết bị bảo vệ thính giác khi làm việc trong môi trường có độ ồn từ 85dB trở lên. Hiệu quả chống ồn được đánh giá bằng chỉ số NRR (Noise Reduction Rating).",
        "context": "건설 현장 소음 작업, 천공 작업, 발파 작업, 중장비 운전",
        "culturalNote": "한국 건설 현장에서는 소음 측정을 정기적으로 실시하며 85dB 이상 구역에는 경고 표지판을 설치하고 청력 보호구 착용을 의무화합니다. 특히 항타기, 브레이커, 절단기 등을 사용하는 작업에서는 귀마개와 귀덮개를 동시 착용하기도 합니다. 베트남 근로자들은 소음에 대한 위험 인식이 낮아 귀마개 착용을 불편하다는 이유로 거부하는 경우가 많습니다. 통역 시 청력 손상은 비가역적이며 한번 손상되면 회복되지 않는다는 점을 강조하고, 한국의 정기 청력 검사 제도를 설명해야 합니다. 귀마개는 개인위생 용품이므로 공유 금지 원칙도 전달해야 합니다.",
        "commonMistakes": [
            {
                "mistake": "귀마개와 귀덮개를 구분하지 않음",
                "correction": "형태에 따라 'nút tai'와 'ốp tai'로 정확히 구분",
                "explanation": "형태가 다르고 사용 상황도 다르므로 명확히 구분해야 합니다."
            },
            {
                "mistake": "소음 기준(dB)과 차음 등급(NRR) 설명 생략",
                "correction": "수치와 의미를 구체적으로 설명",
                "explanation": "베트남 근로자가 기준을 이해하도록 수치의 의미를 설명해야 합니다."
            },
            {
                "mistake": "올바른 착용법 설명 누락",
                "correction": "삽입형 귀마개의 정확한 착용법 시연 및 설명",
                "explanation": "잘못 착용하면 보호 효과가 없으므로 착용법을 반드시 전달해야 합니다."
            }
        ],
        "examples": [
            {
                "ko": "항타 작업 구역은 소음이 100dB을 초과하므로 귀마개와 귀덮개를 모두 착용하십시오.",
                "vi": "Khu vực đóng cọc có độ ồn vượt 100dB nên phải đeo cả nút tai và ốp tai.",
                "situation": "onsite"
            },
            {
                "ko": "귀마개는 개인 위생용품이므로 다른 사람과 공유해서는 안 됩니다.",
                "vi": "Nút tai là đồ vệ sinh cá nhân nên không được dùng chung với người khác.",
                "situation": "formal"
            },
            {
                "ko": "귀마개 안 끼면 나중에 귀 먹어. 꼭 껴.",
                "vi": "Không đeo nút tai sau này điếc đấy. Nhớ đeo nhé.",
                "situation": "informal"
            }
        ],
        "relatedTerms": ["귀덮개", "소음 측정", "청력 보호구", "데시벨", "NRR"]
    },
    {
        "slug": "gang-tay-bao-ho",
        "korean": "안전장갑",
        "vietnamese": "Găng tay bảo hộ",
        "hanja": "安全裝甲",
        "hanjaReading": "安(편안할 안) + 全(온전할 전) + 裝(꾸밀 장) + 甲(갑옷 갑)",
        "pronunciation": "안전장갑",
        "meaningKo": "건설 현장에서 손을 보호하기 위해 착용하는 작업용 장갑으로, 작업 특성에 따라 면장갑, 코팅장갑, 가죽장갑, 방진장갑, 절연장갑 등 다양한 종류가 있습니다. 통역 시 주의할 점은 한국에서 안전장갑을 작업별로 매우 세분화하여 구분하는데, 일반 작업용 '면장갑', 미끄럼 방지 '코팅장갑', 절단 작업용 '방진장갑(cut-resistant glove)', 전기 작업용 '절연장갑', 용접용 '가죽장갑' 등이 있으며 각각 베트남어로 'găng tay vải', 'găng tay phủ cao su', 'găng tay chống cắt', 'găng tay cách điện', 'găng tay da hàn'으로 구분됩니다. 특히 회전 기계 작업 시에는 장갑 착용이 오히려 위험할 수 있어 착용 금지되는 경우가 있으므로 이를 명확히 전달해야 합니다. 한국에서는 작업별 적합한 장갑 착용을 법으로 규정하고 있어 잘못된 장갑 사용도 안전 위반에 해당합니다.",
        "meaningVi": "Găng tay bảo hộ là thiết bị bảo vệ bàn tay khi làm việc tại công trường, có nhiều loại khác nhau tùy theo tính chất công việc: găng tay vải cho công việc chung, găng tay phủ cao su chống trượt, găng tay chống cắt cho công việc có nguy cơ bị thương, găng tay cách điện cho thợ điện, găng tay da cho thợ hàn. Tại Hàn Quốc, việc lựa chọn đúng loại găng tay theo công việc là yêu cầu bắt buộc theo luật an toàn lao động. Lưu ý: khi vận hành máy móc quay, việc đeo găng tay có thể gây nguy hiểm và bị cấm.",
        "context": "건설 현장 일반 작업, 중량물 취급, 전기 작업, 용접 작업, 절단 작업",
        "culturalNote": "한국 건설 현장에서는 작업 특성에 따라 적합한 안전장갑을 선택하는 것이 매우 중요하며, 관리감독자가 장갑 종류를 확인합니다. 특히 전기 작업 시 절연장갑 미착용은 중대재해로 이어질 수 있어 엄격히 관리됩니다. 회전체(그라인더, 선반 등) 작업 시에는 장갑이 말려들어갈 위험이 있어 착용을 금지하는데, 이 점을 베트남 근로자에게 명확히 설명하지 않으면 안전 수칙 위반으로 오해할 수 있습니다. 베트남에서는 면장갑을 만능으로 사용하는 경향이 있어, 한국의 작업별 장갑 분류 체계를 교육할 때 실물과 함께 설명하는 것이 효과적입니다.",
        "commonMistakes": [
            {
                "mistake": "모든 장갑을 'găng tay'로만 통역",
                "correction": "작업별로 장갑 종류를 구체적으로 명시",
                "explanation": "장갑 종류에 따라 보호 기능이 다르므로 정확히 구분해야 합니다."
            },
            {
                "mistake": "회전체 작업 시 장갑 착용 금지 사항 누락",
                "correction": "장갑 착용이 위험한 작업을 명확히 설명",
                "explanation": "장갑 착용이 오히려 위험한 경우가 있음을 반드시 알려야 합니다."
            },
            {
                "mistake": "절연장갑 등급 설명 생략",
                "correction": "전압별 절연장갑 등급(Class 00~4) 설명",
                "explanation": "전기 작업은 전압에 맞는 등급의 장갑을 착용해야 하므로 등급을 명시해야 합니다."
            }
        ],
        "examples": [
            {
                "ko": "중량물을 취급할 때는 코팅장갑을 착용하여 미끄러짐을 방지하십시오.",
                "vi": "Khi vận chuyển vật nặng, phải đeo găng tay phủ cao su để chống trượt.",
                "situation": "onsite"
            },
            {
                "ko": "전기 작업 시에는 절연장갑과 절연화를 반드시 함께 착용해야 합니다.",
                "vi": "Khi làm công việc điện, bắt buộc phải đeo cả găng tay cách điện và giày cách điện.",
                "situation": "formal"
            },
            {
                "ko": "그라인더 쓸 때는 장갑 벗어. 말려들어가면 손가락 다 날아가.",
                "vi": "Khi dùng máy mài thì cởi găng tay ra. Bị cuốn vào là bay hết ngón tay.",
                "situation": "informal"
            }
        ],
        "relatedTerms": ["면장갑", "코팅장갑", "방진장갑", "절연장갑", "개인 보호 장비"]
    },
    {
        "slug": "ao-phan-quang",
        "korean": "반사조끼",
        "vietnamese": "Áo phản quang",
        "hanja": "反射조끼",
        "hanjaReading": "反(돌이킬 반) + 射(쏠 사) + 조끼(순우리말)",
        "pronunciation": "반사조끼",
        "meaningKo": "건설 현장이나 도로 작업 시 작업자의 위치를 명확히 식별할 수 있도록 형광색 배경에 반사 테이프가 부착된 조끼입니다. 통역 시 주의할 점은 한국에서 '반사조끼', '안전조끼', '형광조끼'를 거의 같은 의미로 사용하지만 공식 명칭은 '안전 반사복' 또는 '고휘도 안전복'입니다. 베트남어로는 'áo phản quang'이 가장 일반적이며 'áo ghi-lê an toàn'으로도 불립니다. 한국 산업안전보건 기준에서는 야간 작업, 도로 작업, 중장비 작업 구역에서 반사조끼 착용을 의무화하고 있으며, 반사 성능에 따라 등급(Class 1~3)이 나뉩니다. Class 3이 가장 높은 등급으로 고속도로 등 고위험 구역에서 사용됩니다. 통역 시 단순히 '착용'만 전달하지 말고 반사 테이프가 손상되거나 오염되면 교체해야 한다는 점, 조끼를 접거나 구겨서 착용하면 안 된다는 점도 함께 전달해야 합니다.",
        "meaningVi": "Áo phản quang là loại áo ghi-lê có màu huỳnh quang với các dải băng phản quang, giúp nhận diện rõ ràng vị trí của người lao động tại công trường hoặc khi làm việc trên đường. Tại Hàn Quốc, theo quy định an toàn lao động, bắt buộc phải mặc áo phản quang khi làm việc ban đêm, trên đường hoặc trong khu vực có thiết bị hạng nặng hoạt động. Áo phản quang được phân loại theo hiệu suất phản xạ từ Class 1 đến Class 3, trong đó Class 3 có hiệu suất cao nhất và được sử dụng cho khu vực nguy hiểm như đường cao tốc.",
        "context": "건설 현장 야간 작업, 도로 보수 작업, 중장비 작업 구역, 교통 통제",
        "culturalNote": "한국 건설 현장에서는 반사조끼가 현장 출입증만큼이나 필수적인 안전 장비로 인식됩니다. 특히 중장비가 많은 현장이나 야간 작업 시에는 조끼 미착용자는 즉시 작업 중지 조치를 받습니다. 반사조끼 색상도 의미가 있어 일반 작업자는 형광 노랑/주황, 관리자는 빨강, 방문객은 초록을 착용하는 경우가 많습니다. 베트남에서는 반사조끼가 교통경찰이나 오토바이 라이더가 착용하는 이미지가 강하지만, 한국 건설 현장에서는 모든 작업자의 필수 장비임을 강조해야 합니다. 통역 시 조끼의 색상 구분 체계가 있다면 이를 명확히 전달하고, 더러워지거나 반사 기능이 떨어진 조끼는 즉시 교체해야 한다는 점을 강조해야 합니다.",
        "commonMistakes": [
            {
                "mistake": "'옷'이나 '조끼'로만 통역",
                "correction": "'안전 반사조끼' 또는 'áo phản quang'으로 정확히 표현",
                "explanation": "일반 조끼와 구분하기 위해 '반사' 또는 '안전' 기능을 명시해야 합니다."
            },
            {
                "mistake": "색상별 구분 설명 누락",
                "correction": "색상에 따른 직급/역할 구분 설명",
                "explanation": "현장에 색상 체계가 있다면 혼란 방지를 위해 설명해야 합니다."
            },
            {
                "mistake": "등급(Class) 설명 생략",
                "correction": "작업 위험도에 따른 등급 요구사항 설명",
                "explanation": "고위험 작업은 고등급 조끼가 필요하므로 등급을 명시해야 합니다."
            }
        ],
        "examples": [
            {
                "ko": "야간 작업 시에는 Class 3 등급의 반사조끼를 착용하고 조끼가 구겨지지 않도록 주의하십시오.",
                "vi": "Khi làm việc ban đêm, phải mặc áo phản quang cấp Class 3 và chú ý không để áo bị nhăn.",
                "situation": "onsite"
            },
            {
                "ko": "중장비 작업 구역에서는 형광 주황색 반사조끼가 필수이며, 반사 테이프가 손상된 조끼는 사용 금지입니다.",
                "vi": "Trong khu vực có thiết bị hạng nặng hoạt động, bắt buộc phải mặc áo phản quang màu cam huỳnh quang, và cấm sử dụng áo có băng phản quang bị hư hỏng.",
                "situation": "formal"
            },
            {
                "ko": "조끼 안 입으면 현장 못 들어가. 저기 가서 받아 입어.",
                "vi": "Không mặc áo phản quang thì không vào được công trường. Qua đó mà nhận áo mặc vào.",
                "situation": "informal"
            }
        ],
        "relatedTerms": ["안전조끼", "형광조끼", "고휘도 안전복", "야간 작업", "교통 통제"]
    },
    {
        "slug": "day-an-toan",
        "korean": "안전고리",
        "vietnamese": "Dây an toàn",
        "hanja": "安全고리",
        "hanjaReading": "安(편안할 안) + 全(온전할 전) + 고리(순우리말)",
        "pronunciation": "안전고리",
        "meaningKo": "고소 작업 시 추락을 방지하기 위해 안전대(안전벨트)와 구조물을 연결하는 줄 또는 와이어로, '안전걸이줄' 또는 '랜야드(lanyard)'라고도 불립니다. 통역 시 주의할 점은 한국에서 '안전고리', '안전걸이줄', '랜야드'를 혼용하지만 가장 정확한 용어는 '안전걸이줄'이며, 이는 안전대 본체와는 별개의 부속품입니다. 베트남어로는 'dây an toàn' 또는 'dây đai an toàn'으로 표현하는데, 'dây đai'는 안전대 본체를 의미하고 'dây an toàn'은 연결줄을 의미하므로 구분이 필요합니다. 안전고리에는 충격 흡수 장치(shock absorber)가 내장된 타입과 일반 타입이 있으며, 한국 법규상 2m 이상 고소 작업 시에는 충격 흡수형을 사용해야 합니다. 통역 시 단순히 '줄'이라고 하지 말고 '안전걸이줄' 또는 '추락 방지 연결줄'로 명확히 표현하고, 걸이점(고정점)의 강도 요구사항(최소 2,300kg)도 함께 전달해야 합니다.",
        "meaningVi": "Dây an toàn (còn gọi là lanyard) là dây hoặc cáp kết nối giữa đai an toàn và cấu trúc công trình, nhằm ngăn ngừa rơi ngã khi làm việc trên cao. Tại Hàn Quốc, khi làm việc ở độ cao từ 2m trở lên, bắt buộc phải sử dụng dây an toàn có thiết bị giảm chấn (shock absorber). Dây an toàn phải được kiểm tra trước mỗi ca làm việc và thay thế ngay nếu có dấu hiệu hư hỏng như sờn, rách, hoặc biến dạng. Điểm móc (điểm neo) phải có độ bền tối thiểu 2.300kg.",
        "context": "고소 작업, 비계 작업, 철골 작업, 외벽 작업, 지붕 작업",
        "culturalNote": "한국 건설 현장에서는 2m 이상 높이에서 작업 시 안전대와 안전고리 착용이 법적 의무이며, 이를 위반하면 작업 중지 및 벌금이 부과됩니다. 안전고리의 걸이점은 반드시 작업자의 어깨 높이 이상이어야 하며(수평 또는 위쪽), 발밑이나 허리 높이에 거는 것은 금지됩니다. 베트남 근로자들은 안전대를 착용하더라도 안전고리를 제대로 걸지 않거나 이동 시 풀어놓는 경우가 많아 이에 대한 교육이 중요합니다. 통역 시 '안전고리 1개당 1명만 사용', '걸이점 이동 시에도 반드시 연결 유지(더블 랜야드 사용)', '안전고리 길이는 최대 2m 이하'와 같은 구체적인 규칙을 명확히 전달해야 합니다.",
        "commonMistakes": [
            {
                "mistake": "'줄'이나 '로프'로만 통역",
                "correction": "'안전걸이줄' 또는 'dây an toàn'으로 정확히 표현",
                "explanation": "일반 줄과 구분하기 위해 '안전' 기능을 명시해야 합니다."
            },
            {
                "mistake": "안전대와 안전고리를 혼동",
                "correction": "안전대(몸에 착용)와 안전고리(구조물 연결줄) 구분",
                "explanation": "두 장비는 함께 사용되지만 별개의 부품이므로 구분해야 합니다."
            },
            {
                "mistake": "걸이점 위치 요구사항 설명 누락",
                "correction": "어깨 높이 이상, 2,300kg 이상 강도 요구사항 명시",
                "explanation": "잘못된 위치에 걸면 추락 방지 효과가 없으므로 반드시 설명해야 합니다."
            }
        ],
        "examples": [
            {
                "ko": "비계 위에서 이동할 때는 더블 랜야드를 사용하여 항상 한 개 이상의 안전고리가 연결된 상태를 유지하십시오.",
                "vi": "Khi di chuyển trên giàn giáo, phải sử dụng lanyard kép để luôn duy trì ít nhất một dây an toàn được kết nối.",
                "situation": "onsite"
            },
            {
                "ko": "안전고리의 걸이점은 작업자 어깨보다 높은 위치여야 하며, 구조물 강도는 최소 2,300kg을 견딜 수 있어야 합니다.",
                "vi": "Điểm móc dây an toàn phải ở vị trí cao hơn vai người lao động và cấu trúc phải chịu được tối thiểu 2.300kg.",
                "situation": "formal"
            },
            {
                "ko": "고리 안 걸고 올라가면 떨어져 죽어. 꼭 걸어.",
                "vi": "Lên cao mà không móc dây an toàn thì rơi chết đấy. Nhớ móc vào nhé.",
                "situation": "informal"
            }
        ],
        "relatedTerms": ["안전대", "안전벨트", "랜야드", "고소작업", "추락방지"]
    },
    {
        "slug": "bien-bao-an-toan",
        "korean": "안전표지판",
        "vietnamese": "Biển báo an toàn",
        "hanja": "安全標識板",
        "hanjaReading": "安(편안할 안) + 全(온전할 전) + 標(표 표) + 識(알 식) + 板(널빤지 판)",
        "pronunciation": "안전표지판",
        "meaningKo": "건설 현장에서 위험 구역, 주의 사항, 금지 사항, 비상구 등을 시각적으로 알리는 표지판으로, 색상과 형태에 따라 의미가 정해져 있습니다. 통역 시 주의할 점은 한국 산업안전보건법에서 정한 표지판 체계를 이해해야 하는데, 빨간색 원형은 금지, 노란색 삼각형은 경고, 파란색 원형은 지시, 초록색 사각형은 안내를 의미합니다. 베트남어로는 'biển báo an toàn', 'biển báo cảnh báo', 'biển cấm', 'biển chỉ dẫn' 등으로 종류별로 구분하여 표현합니다. 한국 현장에서는 국제 표준 픽토그램(ISO 7010)과 한글 문구를 함께 사용하는데, 베트남 근로자를 위해 베트남어 병기가 필요한 경우도 있습니다. 통역 시 단순히 '표지판'이라고만 하지 말고 '관계자외 출입금지', '낙하물 주의', '안전모 착용 구역'처럼 구체적인 의미를 정확히 전달해야 하며, 표지판을 무시하거나 훼손하는 행위는 법적 처벌 대상임을 강조해야 합니다.",
        "meaningVi": "Biển báo an toàn là bảng chỉ dẫn trực quan được đặt tại công trường xây dựng để thông báo về khu vực nguy hiểm, lưu ý cần thiết, điều cấm và lối thoát hiểm. Tại Hàn Quốc, hệ thống biển báo được quy định theo Luật An toàn và Sức khỏe Lao động với màu sắc và hình dạng chuẩn: vòng tròn đỏ (cấm), tam giác vàng (cảnh báo), vòng tròn xanh (chỉ thị), hình chữ nhật xanh lá (hướng dẫn). Biển báo thường sử dụng ký hiệu quốc tế (ISO 7010) kèm chữ Hàn Quốc. Việc phớt lờ hoặc làm hỏng biển báo an toàn có thể bị xử phạt theo pháp luật.",
        "context": "건설 현장 안전 관리, 위험 구역 표시, 출입 통제, 비상 대피",
        "culturalNote": "한국 건설 현장에서는 안전표지판을 매우 중요하게 다루며, 표지판의 크기, 위치, 조명(야간용) 등이 법으로 세세히 규정되어 있습니다. 특히 '출입금지', '고압전기', '낙하물 주의' 등의 표지판이 있는 구역에 무단 출입하면 중대한 안전 위반으로 간주됩니다. 베트남 근로자들이 한글을 읽지 못해 표지판의 의미를 파악하지 못하는 경우가 많으므로, 안전 교육 시 그림 기호(픽토그램)의 의미를 자세히 설명하고 주요 표지판에 대해서는 베트남어 스티커를 추가로 부착하는 것이 효과적입니다. 통역 시 색상과 형태의 의미 체계를 먼저 설명한 후 개별 표지판의 내용을 전달하면 이해도가 높아집니다.",
        "commonMistakes": [
            {
                "mistake": "'biển báo'로만 통역하여 종류 구분 없이 사용",
                "correction": "금지/경고/지시/안내를 구분하여 통역",
                "explanation": "표지판 종류에 따라 의미가 다르므로 정확히 구분해야 합니다."
            },
            {
                "mistake": "색상과 형태의 의미 체계 설명 누락",
                "correction": "빨강=금지, 노랑=경고, 파랑=지시, 초록=안내 설명",
                "explanation": "색상 체계를 이해하면 새로운 표지판도 직관적으로 파악할 수 있습니다."
            },
            {
                "mistake": "표지판 무시 시 처벌 사항 미전달",
                "correction": "법적 처벌 대상임을 명확히 설명",
                "explanation": "표지판 준수의 중요성을 강조하기 위해 처벌 사항을 알려야 합니다."
            }
        ],
        "examples": [
            {
                "ko": "이 구역은 낙하물 위험 구역입니다. 노란색 삼각형 표지판이 보이면 반드시 안전모를 착용하고 신속히 통과하십시오.",
                "vi": "Khu vực này có nguy cơ vật rơi. Khi nhìn thấy biển báo tam giác màu vàng, bắt buộc phải đội mũ bảo hộ và đi qua nhanh chóng.",
                "situation": "onsite"
            },
            {
                "ko": "빨간색 원형 표지판은 금지 표시이므로 해당 구역에서는 표지판에 명시된 행위를 절대 해서는 안 됩니다.",
                "vi": "Biển báo hình tròn màu đỏ là dấu hiệu cấm, tuyệt đối không được thực hiện hành vi ghi trên biển trong khu vực đó.",
                "situation": "formal"
            },
            {
                "ko": "저기 빨간 표지판 보여? 거기 들어가면 안 돼.",
                "vi": "Thấy biển đỏ kia không? Vào đó là không được đâu.",
                "situation": "informal"
            }
        ],
        "relatedTerms": ["경고표지", "금지표지", "안내표지", "픽토그램", "ISO 7010"]
    },
    {
        "slug": "den-canh-bao",
        "korean": "경고등",
        "vietnamese": "Đèn cảnh báo",
        "hanja": "警告燈",
        "hanjaReading": "警(경계할 경) + 告(고할 고) + 燈(등불 등)",
        "pronunciation": "경고등",
        "meaningKo": "건설 현장에서 위험 구역, 작업 중인 장비, 차량 등을 시각적으로 경고하기 위해 설치하는 점멸등 또는 회전등으로, 주로 빨간색, 노란색, 파란색을 사용합니다. 통역 시 주의할 점은 한국에서 '경고등', '회전등', '경광등', '비상등'을 상황에 따라 구분하여 사용하는데, 경고등은 일반적인 위험 알림, 회전등은 차량이나 장비용, 경광등은 경찰/소방 차량용, 비상등은 비상 상황용입니다. 베트남어로는 'đèn cảnh báo'가 가장 일반적이며, 'đèn quay'(회전등), 'đèn nháy'(점멸등)으로 세분화할 수 있습니다. 한국 건설 현장에서는 야간 작업, 굴착 작업, 중장비 후진 등의 상황에서 경고등 사용이 의무화되어 있으며, 경고등 색상도 의미가 있어 빨강은 즉각적 위험, 노랑/주황은 주의, 파랑은 안내를 나타냅니다. 통역 시 경고등이 켜진 구역에는 접근 금지 또는 주의가 필요하다는 점을 명확히 전달해야 합니다.",
        "meaningVi": "Đèn cảnh báo là đèn nhấp nháy hoặc đèn quay được lắp đặt tại công trường xây dựng để cảnh báo trực quan về khu vực nguy hiểm, thiết bị đang hoạt động hoặc phương tiện. Màu sắc thường dùng là đỏ, vàng và xanh dương. Tại Hàn Quốc, việc sử dụng đèn cảnh báo là bắt buộc trong các tình huống như làm việc ban đêm, đào đất hoặc khi xe hạng nặng lùi. Màu sắc đèn cũng có ý nghĩa: đỏ là nguy hiểm trực tiếp, vàng/cam là cần thận trọng, xanh dương là hướng dẫn.",
        "context": "건설 현장 야간 작업, 굴착 작업, 중장비 작업, 도로 작업, 위험 구역 표시",
        "culturalNote": "한국 건설 현장에서는 야간 작업 시 경고등 설치가 법적 의무이며, 특히 도로변 작업이나 중장비 작업 구역에서는 50m 간격으로 경고등을 배치해야 합니다. 중장비(굴착기, 덤프트럭 등)에는 후진 시 자동으로 켜지는 회전등과 후진 경보음이 함께 작동하도록 규정되어 있습니다. 베트남에서는 경고등 사용이 한국만큼 체계적이지 않아, 베트남 근로자들이 경고등의 중요성을 낮게 평가하는 경우가 있습니다. 통역 시 경고등은 단순 안내가 아닌 '생명을 지키는 신호'임을 강조하고, 경고등이 켜진 구역 접근 시 반드시 안전 담당자의 허가를 받아야 한다는 점을 명확히 전달해야 합니다.",
        "commonMistakes": [
            {
                "mistake": "'đèn'으로만 통역하여 일반 조명과 혼동",
                "correction": "'đèn cảnh báo' 또는 'đèn an toàn'으로 명시",
                "explanation": "일반 조명과 구분하기 위해 '경고' 기능을 명확히 해야 합니다."
            },
            {
                "mistake": "색상별 의미 설명 누락",
                "correction": "빨강/노랑/파랑 색상의 의미 구분 설명",
                "explanation": "색상에 따라 위험 수준이 다르므로 의미를 전달해야 합니다."
            },
            {
                "mistake": "경고등 무시 시 위험성 강조 부족",
                "correction": "경고등 구역 접근 시 안전 수칙 및 허가 절차 명시",
                "explanation": "경고등을 단순 표시로 여기지 않도록 위험성을 강조해야 합니다."
            }
        ],
        "examples": [
            {
                "ko": "굴착기 후진 시 노란색 회전등이 켜집니다. 이 신호를 보면 즉시 안전거리를 확보하십시오.",
                "vi": "Khi máy xúc lùi, đèn quay màu vàng sẽ sáng. Khi thấy tín hiệu này, hãy lập tức di chuyển ra khoảng cách an toàn.",
                "situation": "onsite"
            },
            {
                "ko": "야간 작업 구역에는 50m 간격으로 경고등을 설치하고, 전원을 확인하여 작동 상태를 유지해야 합니다.",
                "vi": "Tại khu vực làm việc ban đêm, phải lắp đặt đèn cảnh báo cách nhau 50m và kiểm tra nguồn điện để đảm bảo đèn hoạt động liên tục.",
                "situation": "formal"
            },
            {
                "ko": "저기 빨간 불 깜빡이는 데 가지 마. 위험해.",
                "vi": "Đừng vào chỗ đèn đỏ nhấp nháy kia. Nguy hiểm lắm.",
                "situation": "informal"
            }
        ],
        "relatedTerms": ["회전등", "경광등", "비상등", "안전표지판", "야간작업"]
    },
    {
        "slug": "rao-chan",
        "korean": "바리케이드",
        "vietnamese": "Rào chắn",
        "hanja": "barricade",
        "hanjaReading": None,
        "pronunciation": "바리케이드",
        "meaningKo": "건설 현장에서 위험 구역이나 출입 금지 구역을 물리적으로 차단하기 위해 설치하는 이동식 펜스나 차단막으로, '안전 펜스', '가설 울타리', '차단막'이라고도 불립니다. 통역 시 주의할 점은 한국에서 'barricade'를 외래어 그대로 '바리케이드'로 사용하지만, 공식 용어는 '안전 차단시설' 또는 '가설 울타리'이며, 베트남어로는 'rào chắn', 'hàng rào an toàn', 'vật chắn'으로 표현합니다. 바리케이드에는 여러 종류가 있는데, 플라스틱 펜스(rào nhựa), 철제 펜스(rào sắt), 안전망(lưới an toàn), 차단봉(thanh chắn) 등이 있으며 용도에 따라 구분하여 사용합니다. 한국 산업안전보건 기준에서는 낙하물 위험 구역, 굴착 구역, 위험 기계 주변 등에 바리케이드 설치를 의무화하고 있으며, 높이와 강도에 대한 규정도 있습니다(일반적으로 최소 1.2m 높이). 통역 시 바리케이드는 단순한 표시가 아니라 물리적 차단 장치이므로 임의로 이동하거나 제거하면 안 된다는 점을 강조해야 합니다.",
        "meaningVi": "Rào chắn (barricade) là hàng rào di động hoặc tấm chắn được lắp đặt tại công trường xây dựng để ngăn cách vật lý các khu vực nguy hiểm hoặc khu vực cấm vào. Có nhiều loại rào chắn: rào nhựa, rào sắt, lưới an toàn, thanh chắn, tùy theo mục đích sử dụng. Tại Hàn Quốc, theo quy định an toàn lao động, bắt buộc phải lắp rào chắn tại khu vực có nguy cơ rơi vật, khu đào đất và xung quanh máy móc nguy hiểm, với chiều cao tối thiểu thường là 1,2m. Rào chắn không chỉ là dấu hiệu mà là thiết bị ngăn cản vật lý, không được tự ý di chuyển hoặc tháo bỏ.",
        "context": "건설 현장 위험 구역 차단, 출입 통제, 낙하물 방지, 굴착 작업 보호",
        "culturalNote": "한국 건설 현장에서는 바리케이드 설치가 매우 체계적으로 이루어지며, 작업 시작 전 위험성 평가를 통해 바리케이드 필요 구역을 선정합니다. 특히 지하 굴착 구역에는 야광 테이프가 부착된 바리케이드를 설치하여 야간에도 식별 가능하도록 합니다. 바리케이드에는 '출입금지', '위험', '낙하물 주의' 등의 표지판을 함께 부착하여 위험 내용을 명확히 알립니다. 베트남에서는 바리케이드를 일시적인 표시 정도로 인식하여 이동이 불편하면 임의로 치우는 경우가 있는데, 한국에서는 이것이 중대한 안전 위반임을 강조해야 합니다. 통역 시 바리케이드를 이동해야 할 경우 반드시 안전 담당자의 허가를 받고 작업 후 원위치해야 한다는 점을 명확히 전달해야 합니다.",
        "commonMistakes": [
            {
                "mistake": "'울타리' 또는 'rào'로만 통역하여 일반 울타리와 혼동",
                "correction": "'안전 바리케이드' 또는 'rào chắn an toàn'으로 명시",
                "explanation": "일반 울타리와 구분하기 위해 '안전' 기능을 명확히 해야 합니다."
            },
            {
                "mistake": "바리케이드 임의 이동 금지 사항 미전달",
                "correction": "허가 없이 이동/제거 금지 및 위반 시 처벌 명시",
                "explanation": "무단 이동은 중대한 안전 위반이므로 금지 사항을 강조해야 합니다."
            },
            {
                "mistake": "바리케이드 종류별 용도 설명 누락",
                "correction": "플라스틱/철제/안전망 등 종류별 용도 구분",
                "explanation": "상황에 맞는 바리케이드를 사용해야 하므로 종류를 설명해야 합니다."
            }
        ],
        "examples": [
            {
                "ko": "굴착 작업 중에는 구덩이 주변 1.5m 이내에 높이 1.2m 이상의 바리케이드를 설치하고 야간에는 경고등을 함께 배치하십시오.",
                "vi": "Trong khi đào đất, phải lắp rào chắn cao tối thiểu 1,2m trong phạm vi 1,5m xung quanh hố đào và bố trí thêm đèn cảnh báo vào ban đêm.",
                "situation": "onsite"
            },
            {
                "ko": "바리케이드는 안전 차단 시설이므로 허가 없이 이동하거나 제거할 수 없으며, 위반 시 작업 중지 및 벌금이 부과됩니다.",
                "vi": "Rào chắn là thiết bị ngăn cách an toàn nên không được di chuyển hoặc tháo bỏ khi chưa có phép, vi phạm sẽ bị đình chỉ công việc và phạt tiền.",
                "situation": "formal"
            },
            {
                "ko": "저기 노란 울타리 치워놨네? 누가 치웠어? 다시 설치해.",
                "vi": "Rào vàng kia bị dỡ rồi à? Ai dỡ vậy? Lắp lại đi.",
                "situation": "informal"
            }
        ],
        "relatedTerms": ["안전 펜스", "가설 울타리", "차단막", "안전망", "출입통제"]
    }
]

# 대상 파일 경로
file_path = os.path.join(
    os.path.expanduser("~"),
    "Documents/claude_code/projects/vn.epicstage.co.kr/src/data/terms/construction.json"
)

# 기존 파일 읽기
with open(file_path, 'r', encoding='utf-8') as f:
    existing_data = json.load(f)

# 새 용어 추가
existing_data.extend(data)

# 파일 저장
with open(file_path, 'w', encoding='utf-8') as f:
    json.dump(existing_data, f, ensure_ascii=False, indent=2)

print(f"✅ {len(data)}개 용어 추가 완료")
print(f"📁 파일: {file_path}")
print(f"📊 총 용어 수: {len(existing_data)}개")
