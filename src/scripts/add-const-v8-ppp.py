#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Construction 용어 추가 스크립트 v8
테마: 시멘트/혼화재/첨가제
Tier S 기준 준수
"""

import json
import os

# 추가할 용어 데이터 (10개)
data = [
    {
        "slug": "xi-mang-portland",
        "korean": "포틀랜드시멘트",
        "vietnamese": "Xi măng Portland",
        "hanja": "포틀랜드시멘트",
        "hanjaReading": None,
        "pronunciation": "포틀랜드시멘트",
        "meaningKo": "석회석과 점토를 주원료로 소성하여 만든 가장 보편적인 시멘트. 영국 포틀랜드섬의 석재 색과 유사해 이 이름이 붙었습니다. 통역 시 주의할 점은 '포틀랜드시멘트'를 단순히 '시멘트'로 축약하면 안 되며, 고로슬래그시멘트나 플라이애시시멘트와 명확히 구분해야 합니다. 건설 현장에서 '일반시멘트'라고 부르는 경우가 많은데, 베트남어로는 반드시 'Xi măng Portland'로 정확히 전달해야 혼선을 방지할 수 있습니다. 강도 발현 속도와 발열 특성이 중요한 품질 기준입니다.",
        "meaningVi": "Xi măng phổ biến nhất được sản xuất từ đá vôi và đất sét nung. Tên gọi xuất phát từ màu sắc giống đá ở đảo Portland, Anh. Đây là loại xi măng cơ bản nhất trong xây dựng, có khả năng đông kết và phát triển cường độ tốt. Thường được gọi tắt là 'xi măng thường' nhưng cần phân biệt rõ với xi măng xỉ lò cao hoặc xi măng tro bay.",
        "context": "콘크리트 배합 설계 시 시멘트 종류 선정, 시방서 작성, 품질 관리",
        "culturalNote": "한국에서는 KS L 5201 규격에 따라 1종부터 5종까지 분류하며, 주로 1종(보통)과 3종(조강)이 사용됩니다. 베트남은 TCVN 2682 규격을 따르며, 강도 등급을 PCB(Bền chịu nén - 압축강도) 30, 40, 50으로 표기합니다. 한국 현장에서 '1종 시멘트'라고 하면 베트남에서는 'Xi măng PCB 40'에 해당하는 경우가 많으므로, 단순 명칭이 아닌 강도 등급 기준으로 대조해 통역해야 오주문을 방지할 수 있습니다. 양국 모두 회색 시멘트가 주류이나, 베트nam에서는 흰색 포틀랜드시멘트(Xi măng trắng) 수요도 상당합니다.",
        "commonMistakes": [
            {
                "mistake": "그냥 '시멘트'로만 통역",
                "correction": "Xi măng Portland (포틀랜드시멘트)",
                "explanation": "베트남 현장에서도 여러 종류 시멘트를 사용하므로, 종류를 명확히 해야 혼선 방지"
            },
            {
                "mistake": "Portland를 '포틀랜드섬 제조'로 오해",
                "correction": "영국 지명에서 유래한 명칭일 뿐, 생산지와 무관",
                "explanation": "역사적 배경 설명 시 혼동 방지 필요"
            },
            {
                "mistake": "1종 시멘트 = PCB 30으로 직역",
                "correction": "한국 1종(보통) ≈ 베트남 PCB 40 수준으로 강도 기준 대조",
                "explanation": "규격 체계가 달라 단순 번호 대응은 위험"
            }
        ],
        "examples": [
            {
                "ko": "이번 공사에는 1종 포틀랜드시멘트를 사용합니다.",
                "vi": "Công trình này sử dụng xi măng Portland PCB 40.",
                "situation": "formal"
            },
            {
                "ko": "포틀랜드시멘트 10포대 입고 확인했습니다.",
                "vi": "Đã xác nhận nhập kho 10 bao xi măng Portland.",
                "situation": "onsite"
            },
            {
                "ko": "고로슬래그시멘트 대신 포틀랜드시멘트로 변경 필요합니다.",
                "vi": "Cần thay đổi từ xi măng xỉ lò cao sang xi măng Portland.",
                "situation": "formal"
            }
        ],
        "relatedTerms": ["시멘트", "콘크리트", "고로슬래그시멘트", "혼화재"]
    },
    {
        "slug": "xi-xi-lo-cao",
        "korean": "고로슬래그",
        "vietnamese": "Xỉ lò cao",
        "hanja": "高爐슬래그",
        "hanjaReading": "高(높을 고) 爐(화덕 로)",
        "pronunciation": "고로슬래그",
        "meaningKo": "제철소의 용광로(고로)에서 선철 생산 시 발생하는 부산물로, 미세하게 분쇄하여 시멘트 혼화재로 사용합니다. 통역 시 주의할 점은 '슬래그'를 그냥 'slag'로 음차하면 베트남 현장 근로자들이 이해하지 못하므로, 반드시 'xỉ lò cao'로 명확히 전달해야 합니다. 고로슬래그 미분말(GGBFS)은 콘크리트의 장기 강도 향상과 수화열 저감에 효과적이며, 친환경 콘크리트 배합에 필수 재료입니다. 포틀랜드시멘트와 혼합 비율이 중요하므로 배합 지시 시 정확한 수치 전달이 필수입니다.",
        "meaningVi": "Phụ phẩm từ lò cao sản xuất gang thép, được nghiền mịn để dùng làm phụ gia khoáng cho xi măng và bê tông. Xỉ lò cao nghiền mịn (GGBFS) giúp tăng cường độ dài ngày, giảm nhiệt thủy hóa, và cải thiện tính chống thấm cho bê tông. Đây là nguyên liệu quan trọng trong sản xuất bê tông xanh, thân thiện môi trường.",
        "context": "콘크리트 혼화재 배합, 친환경 건축 자재, 매스콘크리트 공사",
        "culturalNote": "한국은 포스코, 현대제철 등 대형 제철소에서 고로슬래그를 대량 생산하며, 시멘트 업체들이 이를 활용해 고로슬래그시멘트(KS L 5210)를 생산합니다. 베트남도 Hòa Phát, Formosa 등 제철소가 있어 고로슬래그를 생산하지만, 한국만큼 시멘트 혼화재로 활용이 보편화되지 않았습니다. 한국 현장에서 '고로시멘트'라고 줄여 부르는 경우가 많은데, 베트남어로는 'Xi măng xỉ lò cao' 전체를 명확히 발음해야 합니다. 환경 규제 강화로 양국 모두 재활용 자재로서 고로슬래그 활용이 증가 추세입니다.",
        "commonMistakes": [
            {
                "mistake": "slag를 '쓰레기', 'rác thải'로 오역",
                "correction": "Xỉ lò cao (고로슬래그)",
                "explanation": "부산물이지만 유용한 재료이므로 폐기물로 표현하면 안 됨"
            },
            {
                "mistake": "고로슬래그시멘트와 고로슬래그 미분말을 혼동",
                "correction": "시멘트 = Xi măng xỉ lò cao, 미분말 = Bột xỉ lò cao nghiền mịn (GGBFS)",
                "explanation": "용도와 형태가 다르므로 명확히 구분 필요"
            },
            {
                "mistake": "'슬래그'를 베트남어 음차로 통역",
                "correction": "반드시 'Xỉ lò cao'로 번역",
                "explanation": "현장 근로자들이 영어 음차를 이해하지 못함"
            }
        ],
        "examples": [
            {
                "ko": "이 배합은 고로슬래그 미분말 30% 치환입니다.",
                "vi": "Công thức này thay thế 30% bằng bột xỉ lò cao nghiền mịn.",
                "situation": "formal"
            },
            {
                "ko": "고로슬래그 들어간 콘크리트는 초기 강도가 낮으니 양생 기간 늘려야 해요.",
                "vi": "Bê tông có xỉ lò cao có cường độ đầu thấp nên phải kéo dài thời gian bảo dưỡng.",
                "situation": "onsite"
            },
            {
                "ko": "친환경 인증을 위해 고로슬래그 혼입률을 높였습니다.",
                "vi": "Đã tăng tỷ lệ xỉ lò cao để đạt chứng nhận xanh.",
                "situation": "formal"
            }
        ],
        "relatedTerms": ["포틀랜드시멘트", "플라이애시", "혼화재", "매스콘크리트"]
    },
    {
        "slug": "chat-no-gian",
        "korean": "팽창제",
        "vietnamese": "Chất nở giãn",
        "hanja": "膨脹劑",
        "hanjaReading": "膨(부풀 팽) 脹(불룩할 창) 劑(약제 제)",
        "pronunciation": "팽창제",
        "meaningKo": "콘크리트 경화 과정에서 수축을 보상하기 위해 미세한 팽창을 일으키는 혼화재료입니다. 통역 시 주의할 점은 '팽창'을 단순히 '부풀다(phồng lên)'로 번역하면 안 되며, 'nở giãn'으로 정확히 전달해야 합니다. 균열 방지와 수밀성 향상이 목적이며, 지하 구조물이나 수조 공사에서 필수적으로 사용됩니다. 과다 투입 시 오히려 균열을 유발할 수 있으므로, 배합 비율 지시 시 정확한 수치 전달이 매우 중요합니다. 팽창 타이밍과 양생 조건도 함께 설명해야 합니다.",
        "meaningVi": "Phụ gia khoáng gây nở giãn nhẹ trong quá trình đông cứng bê tông để bù trừ co ngót. Mục đích chính là ngăn ngừa nứt và tăng độ kín nước, thường dùng trong công trình ngầm, bể chứa. Việc kiểm soát liều lượng rất quan trọng vì dùng quá nhiều sẽ gây nứt ngược lại.",
        "context": "무수축 콘크리트 타설, 지하 방수 공사, 균열 저감 공법",
        "culturalNote": "한국에서는 KS F 2562 규격에 따라 팽창률을 관리하며, 주로 에트린자이트(ettringite) 생성형 팽창제를 사용합니다. 베트남 현장에서는 팽창제 사용이 한국만큼 보편화되지 않아, 한국 기술자가 팽창제 사용을 지시할 때 베트남 현장 근로자들이 그 필요성을 이해하지 못하는 경우가 많습니다. 따라서 '균열 방지용'이라는 목적을 반드시 함께 설명해야 합니다. 또한 한국에서는 '무수축 몰탈', '무수축 그라우트'라는 용어로 팽창제 혼입 제품을 부르는데, 베트nam에서는 'Vữa không co ngót'으로 직역해야 통합니다.",
        "commonMistakes": [
            {
                "mistake": "팽창제를 'chất phồng lên'으로 직역",
                "correction": "Chất nở giãn (팽창제)",
                "explanation": "'phồng lên'은 부정확한 뉘앙스, 전문 용어는 'nở giãn'"
            },
            {
                "mistake": "팽창제를 '수축 방지제'로만 설명",
                "correction": "미세 팽창으로 수축 보상하는 원리까지 설명",
                "explanation": "작동 원리를 이해해야 적절한 사용 가능"
            },
            {
                "mistake": "투입량을 '적당히'로 모호하게 전달",
                "correction": "시멘트 대비 % 또는 kg/m³ 단위로 정확히",
                "explanation": "과소/과다 투입 모두 문제 발생 가능"
            }
        ],
        "examples": [
            {
                "ko": "지하 외벽 콘크리트에 팽창제 8% 혼입하세요.",
                "vi": "Trộn 8% chất nở giãn vào bê tông tường ngoài ngầm.",
                "situation": "onsite"
            },
            {
                "ko": "무수축 그라우트에는 팽창제가 이미 포함되어 있습니다.",
                "vi": "Vữa grouting không co ngót đã có sẵn chất nở giãn.",
                "situation": "formal"
            },
            {
                "ko": "팽창제 쓰면 초기 양생이 더 중요해요.",
                "vi": "Khi dùng chất nở giãn thì bảo dưỡng đầu càng quan trọng.",
                "situation": "onsite"
            }
        ],
        "relatedTerms": ["무수축콘크리트", "그라우트", "수축저감제", "균열"]
    },
    {
        "slug": "chat-chong-tham",
        "korean": "방수제",
        "vietnamese": "Chất chống thấm",
        "hanja": "防水劑",
        "hanjaReading": "防(막을 방) 水(물 수) 劑(약제 제)",
        "pronunciation": "방수제",
        "meaningKo": "콘크리트나 모르타르의 수밀성을 높여 물의 침투를 막는 혼화제입니다. 통역 시 주의할 점은 방수제와 방수공법을 구분해야 하며, 혼화제 방수와 도막 방수는 완전히 다른 공법임을 명확히 해야 합니다. 결정질계, 발수계, 친수계 등 종류가 다양하므로 어떤 타입인지 반드시 확인 후 통역해야 합니다. 지하 구조물, 수조, 화장실 등에서 필수적이며, 특히 지하수위가 높은 현장에서는 배합 비율과 시공 방법에 대한 정확한 지시 전달이 중요합니다.",
        "meaningVi": "Phụ gia tăng tính kín nước cho bê tông và vữa, ngăn nước thấm vào. Có nhiều loại như tinh thể hóa, kỵ nước, ưa nước. Dùng trong công trình ngầm, bể chứa, phòng vệ sinh. Cần phân biệt rõ với các phương pháp chống thấm bề mặt khác.",
        "context": "지하 구조물 방수, 수조 공사, 콘크리트 배합 설계",
        "culturalNote": "한국에서는 KS F 2568 규격에 따라 방수제 성능을 평가하며, 액상형과 분말형이 모두 사용됩니다. 베트남 현장에서는 '방수(chống thấm)'라는 개념이 주로 외부 도막 방수를 의미하므로, 콘크리트 자체에 혼입하는 방수제를 설명할 때는 'phụ gia chống thấm trộn vào bê tông'처럼 명확히 해야 합니다. 한국에서는 아파트 지하주차장, 화장실 등에 방수제 혼입이 표준화되어 있지만, 베트남에서는 아직 외부 방수 시공에 더 의존하는 경향이 있습니다. '투과성 방수'와 '차단성 방수' 개념 차이도 설명이 필요합니다.",
        "commonMistakes": [
            {
                "mistake": "방수제를 '방수 페인트(sơn chống thấm)'로 혼동",
                "correction": "Phụ gia chống thấm (콘크리트 혼입용 방수제)",
                "explanation": "혼화제와 도막재는 완전히 다른 제품"
            },
            {
                "mistake": "모든 방수제를 하나로 통칭",
                "correction": "결정질계, 발수계 등 종류 명시 필요",
                "explanation": "작동 원리가 다르므로 구분 필수"
            },
            {
                "mistake": "'방수'와 '수밀'을 동일시",
                "correction": "방수 = chống thấm, 수밀 = kín nước (미세 차이 있음)",
                "explanation": "수밀은 물리적 치밀성, 방수는 침투 차단"
            }
        ],
        "examples": [
            {
                "ko": "지하 외벽에는 결정질계 방수제를 사용합니다.",
                "vi": "Tường ngoài ngầm dùng phụ gia chống thấm loại tinh thể hóa.",
                "situation": "formal"
            },
            {
                "ko": "방수제 넣었으니 별도 방수 공사 안 해도 돼요?",
                "vi": "Đã cho phụ gia chống thấm thì không cần thi công chống thấm riêng à?",
                "situation": "onsite"
            },
            {
                "ko": "액상 방수제 1리터당 시멘트 50kg 기준입니다.",
                "vi": "Phụ gia chống thấm dạng lỏng 1 lít cho 50kg xi măng.",
                "situation": "formal"
            }
        ],
        "relatedTerms": ["수밀콘크리트", "방수공법", "지하방수", "균열"]
    },
    {
        "slug": "chat-dong-cung-nhanh",
        "korean": "급결제",
        "vietnamese": "Chất đông cứng nhanh",
        "hanja": "急結劑",
        "hanjaReading": "急(급할 급) 結(맺을 결) 劑(약제 제)",
        "pronunciation": "급결제",
        "meaningKo": "콘크리트나 모르타르의 응결 시간을 단축시켜 빠른 경화를 유도하는 혼화제입니다. 통역 시 주의할 점은 '급결'을 단순히 '빠른 응결'로만 설명하면 안 되며, 터널 숏크리트, 누수 보수, 긴급 공사 등 특수 목적임을 명확히 해야 합니다. 일반 레미콘에 급결제를 사용하면 시공 중 굳어버려 큰 사고가 날 수 있으므로, 사용 목적과 대상을 정확히 확인 후 통역하는 것이 매우 중요합니다. 분사 시공(shotcrete) 시 필수이며, 리바운드(튀어나온 재료) 발생률도 함께 고려해야 합니다.",
        "meaningVi": "Phụ gia rút ngắn thời gian đông kết của bê tông và vữa. Dùng trong thi công phun bê tông (shotcrete) ở hầm đường, sửa chữa thấm khẩn cấp. Nếu dùng nhầm cho bê tông thường sẽ gây đông cứng giữa chừng, rất nguy hiểm. Cần kiểm soát chặt chẽ đối tượng và mục đích sử dụng.",
        "context": "터널 숏크리트, 누수 보수, 긴급 공사, 내화 피복",
        "culturalNote": "한국에서는 NATM(New Austrian Tunneling Method) 터널 공사에서 숏크리트에 급결제를 표준으로 사용하며, 지하철 공사 현장에서 매우 흔합니다. 베트남도 하노이, 호치민 지하철 공사가 진행되며 숏크리트 공법이 도입되었지만, 급결제 사용 경험이 한국만큼 축적되지 않아 혼란이 발생할 수 있습니다. 한국 기술자가 '급결제'라고 지시하면, 베트남 현장에서는 반드시 'phun bê tông(숏크리트)'와 연결해 설명해야 오사용을 방지할 수 있습니다. 알칼리 급결제와 무알칼리 급결제의 차이도 중요합니다.",
        "commonMistakes": [
            {
                "mistake": "급결제를 '조강제(chất tăng cường độ sớm)'와 혼동",
                "correction": "급결 = 응결 시간 단축, 조강 = 강도 발현 촉진 (다른 개념)",
                "explanation": "용도와 효과가 완전히 다름"
            },
            {
                "mistake": "일반 콘크리트에 급결제 사용 지시로 오해",
                "correction": "숏크리트 전용임을 명확히 전달",
                "explanation": "일반 타설에는 절대 사용 금지"
            },
            {
                "mistake": "'빨리 마르는 제(chất khô nhanh)'로 번역",
                "correction": "Chất đông cứng nhanh (급결제)",
                "explanation": "'마르다'는 건조를 의미해 부정확"
            }
        ],
        "examples": [
            {
                "ko": "터널 막장에 숏크리트 칠 때 급결제 5% 혼입하세요.",
                "vi": "Khi phun bê tông mặt hầm thì trộn 5% chất đông cứng nhanh.",
                "situation": "onsite"
            },
            {
                "ko": "이 급결제는 알칼리프리 제품이라 철근 부식 걱정 없습니다.",
                "vi": "Chất đông cứng nhanh này không kiềm nên không lo ăn mòn cốt thép.",
                "situation": "formal"
            },
            {
                "ko": "누수 부위 긴급 보수용으로 급결 모르타르 준비해주세요.",
                "vi": "Chuẩn bị vữa đông cứng nhanh để sửa thấm khẩn cấp.",
                "situation": "onsite"
            }
        ],
        "relatedTerms": ["숏크리트", "조강제", "지연제", "터널공사"]
    },
    {
        "slug": "chat-cham-dong-cung",
        "korean": "지연제",
        "vietnamese": "Chất chậm đông cứng",
        "hanja": "遲延劑",
        "hanjaReading": "遲(더딜 지) 延(늘일 연) 劑(약제 제)",
        "pronunciation": "지연제",
        "meaningKo": "콘크리트의 응결 시간을 늦춰 타설 가능 시간을 연장하는 혼화제입니다. 통역 시 주의할 점은 '지연'을 단순히 '늦춘다'로만 설명하면 안 되며, 장거리 운송, 더운 날씨, 대규모 타설 등 사용 목적을 명확히 해야 합니다. 레미콘 운송 시간이 길거나, 하절기 서중 콘크리트 타설 시 필수적이며, 투입량에 따라 지연 시간이 달라지므로 정확한 배합 지시가 중요합니다. 과다 투입 시 응결 불량이나 초기 강도 저하가 발생할 수 있어, 기상 조건과 운송 시간을 고려한 섬세한 판단이 필요합니다.",
        "meaningVi": "Phụ gia kéo dài thời gian đông kết của bê tông, giữ được độ sệt lâu hơn. Dùng khi vận chuyển xa, đổ bê tông khối lượng lớn, thời tiết nóng. Liều lượng quyết định thời gian chậm, nếu cho quá nhiều sẽ gây đông cứng không tốt hoặc giảm cường độ đầu.",
        "context": "레미콘 장거리 운송, 하절기 공사, 매스콘크리트 타설",
        "culturalNote": "한국에서는 레미콘 운송 시간이 1.5시간 이상 걸리는 경우 지연제를 표준으로 사용하며, 여름철에는 거의 필수입니다. 베트남은 연중 고온다습하여 콘크리트 응결이 빨라지는 문제가 상시 발생하므로, 지연제 사용 빈도가 한국보다 높습니다. 하노이는 여름 40도를 넘어가므로, 한국 기술자가 한국 기준으로 지연제 배합을 지시하면 부족할 수 있습니다. 베트남 현장에서는 'Phụ gia giữ sệt'이라는 표현도 함께 사용되는데, 이는 '슬럼프 유지제'에 가까우므로 엄밀히는 지연제와 다른 개념임을 구분해야 합니다.",
        "commonMistakes": [
            {
                "mistake": "지연제를 '경화 방지제'로 오해",
                "correction": "응결 시간 연장일 뿐, 경화는 정상 진행",
                "explanation": "지연제도 결국 굳으므로 '방지'는 틀린 표현"
            },
            {
                "mistake": "슬럼프 유지제(giữ sệt)와 지연제 혼동",
                "correction": "슬럼프 유지는 유동성, 지연은 응결 시간 (목적 다름)",
                "explanation": "기능이 겹치지만 원리와 목적이 다른 첨가제"
            },
            {
                "mistake": "'느리게 하는 제(chất làm chậm)'로 모호하게 번역",
                "correction": "Chất chậm đông cứng (응결 지연제)",
                "explanation": "무엇을 늦추는지 명확히 해야 함"
            }
        ],
        "examples": [
            {
                "ko": "운송 시간 2시간이니 지연제 0.3% 투입하세요.",
                "vi": "Thời gian vận chuyển 2 tiếng nên cho 0.3% chất chậm đông cứng.",
                "situation": "formal"
            },
            {
                "ko": "오늘 너무 더워서 지연제 좀 더 넣어야 할 것 같아요.",
                "vi": "Hôm nay nóng quá nên có lẽ phải cho chất chậm đông cứng nhiều hơn.",
                "situation": "onsite"
            },
            {
                "ko": "매스콘크리트 타설이라 지연제로 수화열 조절합니다.",
                "vi": "Đổ bê tông khối lớn nên dùng chất chậm đông cứng để kiểm soát nhiệt thủy hóa.",
                "situation": "formal"
            }
        ],
        "relatedTerms": ["급결제", "유동화제", "서중콘크리트", "레미콘"]
    },
    {
        "slug": "chat-luu-dong-hoa",
        "korean": "유동화제",
        "vietnamese": "Chất siêu dẻo / Chất lưu động hóa",
        "hanja": "流動化劑",
        "hanjaReading": "流(흐를 류/유) 動(움직일 동) 化(될 화) 劑(약제 제)",
        "pronunciation": "유동화제",
        "meaningKo": "물-시멘트비를 낮추면서도 콘크리트의 유동성을 크게 향상시키는 고성능 감수제입니다. 통역 시 주의할 점은 일반 감수제(AE제)와 명확히 구분해야 하며, '고성능 감수제'라는 표현을 함께 사용해야 합니다. 베트남어로는 'Chất siêu dẻo'(슈퍼플라스티사이저 음차) 또는 'Chất lưu động hóa'로 번역하는데, 현장에서는 'siêu dẻo'가 더 통용됩니다. 고강도 콘크리트, 자기충전 콘크리트(SCC), 고유동 콘크리트에 필수이며, 투입 타이밍과 투입량이 매우 중요해 정확한 지시 전달이 필수입니다.",
        "meaningVi": "Phụ gia giảm nước cao cấp (siêu dẻo), tăng khả năng lưu động của bê tông mà không cần tăng nước. Thiết yếu cho bê tông cường độ cao, bê tông tự đầm (SCC). Thường gọi là 'phụ gia siêu dẻo' trong công trường. Thời điểm và liều lượng cho rất quan trọng.",
        "context": "고강도 콘크리트, 자기충전 콘크리트, 펌프 타설, 좁은 거푸집",
        "culturalNote": "한국에서는 폴리카본산계(PCE) 유동화제가 주류이며, 레미콘 공장에서 표준으로 사용됩니다. 베트남도 최근 고층 건물 증가로 유동화제 사용이 늘었지만, 한국만큼 보편화되지 않아 현장 근로자들이 일반 감수제와 혼동하는 경우가 많습니다. 한국에서 '유동화제'라고 하면 베트남 현장에서는 'Phụ gia siêu dẻo'로 명확히 전달해야 하며, 'siêu'(슈퍼)가 빠지면 일반 감수제로 오해됩니다. 또한 한국에서는 레미콘 현장 도착 후 추가 투입(후첨가)하는 경우가 많은데, 베트남에서는 이 관행이 덜 일반화되어 설명이 필요합니다.",
        "commonMistakes": [
            {
                "mistake": "유동화제를 일반 감수제(chất giảm nước)로 번역",
                "correction": "Chất siêu dẻo 또는 Chất lưu động hóa (고성능 감수제)",
                "explanation": "성능 차이가 크므로 '슈퍼' 표현 필수"
            },
            {
                "mistake": "유동화제를 '물 대신 넣는 것'으로 설명",
                "correction": "물-시멘트비 낮추면서 유동성 확보",
                "explanation": "물 대체가 아니라 성능 향상 목적"
            },
            {
                "mistake": "투입 시점을 모호하게 전달",
                "correction": "공장 투입인지, 현장 후첨가인지 명확히",
                "explanation": "투입 시점에 따라 효과 달라짐"
            }
        ],
        "examples": [
            {
                "ko": "60MPa 콘크리트라 유동화제 2% 사용합니다.",
                "vi": "Bê tông 60MPa nên dùng 2% chất siêu dẻo.",
                "situation": "formal"
            },
            {
                "ko": "펌프카 올리기 전에 유동화제 현장에서 추가 투입하세요.",
                "vi": "Trước khi bơm lên thì cho thêm chất siêu dẻo tại hiện trường.",
                "situation": "onsite"
            },
            {
                "ko": "자기충전 콘크리트는 유동화제 없으면 안 돼요.",
                "vi": "Bê tông tự đầm không thể thiếu chất siêu dẻo.",
                "situation": "onsite"
            }
        ],
        "relatedTerms": ["감수제", "고강도콘크리트", "자기충전콘크리트", "슬럼프"]
    },
    {
        "slug": "chat-giam-co-ngot",
        "korean": "수축저감제",
        "vietnamese": "Chất giảm co ngót",
        "hanja": "收縮低減劑",
        "hanjaReading": "收(거둘 수) 縮(줄일 축) 低(낮을 저) 減(덜 감) 劑(약제 제)",
        "pronunciation": "수축저감제",
        "meaningKo": "콘크리트 건조 수축을 억제하여 균열 발생을 줄이는 혼화제입니다. 통역 시 주의할 점은 팽창제와 혼동하지 말아야 하며, 수축저감제는 수축 자체를 줄이는 반면 팽창제는 팽창으로 수축을 보상하는 원리임을 명확히 해야 합니다. 특히 슬래브, 바닥 콘크리트, 대면적 타설에서 균열 방지 목적으로 사용되며, 양생 방법과 연계해 설명해야 효과적입니다. 표면 마감이 중요한 공사에서 필수적이며, 장기 내구성 향상 효과도 있습니다.",
        "meaningVi": "Phụ gia ức chế co ngót khô của bê tông, giảm nứt. Khác với chất nở giãn - chất giảm co ngót làm giảm bản thân sự co ngót, còn chất nở giãn dùng nở để bù co. Dùng cho sàn, bê tông diện tích lớn, quan trọng cho hoàn thiện bề mặt và độ bền lâu dài.",
        "context": "슬래브 공사, 바닥 마감, 대면적 콘크리트, 균열 제어",
        "culturalNote": "한국에서는 아파트 바닥 슬래브 균열 민원이 많아 수축저감제 사용이 증가하는 추세이며, 특히 건조한 겨울철 실내 난방으로 인한 급격한 수축을 방지하기 위해 사용됩니다. 베트남은 고온다습 기후라 한국만큼 건조 수축이 심하지 않지만, 에어컨 사용으로 실내외 온습도 차가 크면 균열이 발생할 수 있습니다. 한국 기술자가 '수축저감제'를 지시할 때, 베트남 현장에서는 'chất giảm co ngót'으로 정확히 전달하되, 팽창제(chất nở giãn)와 혼동하지 않도록 작동 원리까지 설명하는 것이 좋습니다. '크랙 방지제'라는 통칭도 사용되지만, 이는 부정확한 표현입니다.",
        "commonMistakes": [
            {
                "mistake": "수축저감제를 팽창제(chất nở giãn)와 혼동",
                "correction": "수축 억제 vs 팽창 보상, 원리가 다름",
                "explanation": "두 제품 모두 균열 방지 목적이지만 메커니즘이 다름"
            },
            {
                "mistake": "'크랙 방지제(chất chống nứt)'로 통칭",
                "correction": "Chất giảm co ngót (수축저감제)",
                "explanation": "균열 원인이 다양하므로 정확한 명칭 사용 필요"
            },
            {
                "mistake": "수축저감제만 사용하면 균열 안 생긴다고 설명",
                "correction": "양생 관리 병행 필수",
                "explanation": "혼화제만으로는 부족, 시공 관리도 중요"
            }
        ],
        "examples": [
            {
                "ko": "이번 슬래브 타설에는 수축저감제 3kg/m³ 사용합니다.",
                "vi": "Đổ sàn lần này dùng 3kg/m³ chất giảm co ngót.",
                "situation": "formal"
            },
            {
                "ko": "수축저감제 넣었어도 양생 철저히 해야 균열 안 가요.",
                "vi": "Dù có cho chất giảm co ngót vẫn phải bảo dưỡng kỹ mới không nứt.",
                "situation": "onsite"
            },
            {
                "ko": "마감이 중요한 곳이라 수축저감제 추가했습니다.",
                "vi": "Chỗ này hoàn thiện quan trọng nên đã thêm chất giảm co ngót.",
                "situation": "formal"
            }
        ],
        "relatedTerms": ["팽창제", "균열", "양생", "슬래브"]
    },
    {
        "slug": "xi-mang-polymer",
        "korean": "폴리머시멘트",
        "vietnamese": "Xi măng polymer",
        "hanja": "폴리머시멘트",
        "hanjaReading": None,
        "pronunciation": "폴리머시멘트",
        "meaningKo": "시멘트에 폴리머(고분자) 수지를 혼합하여 접착력, 방수성, 내구성을 향상시킨 특수 시멘트입니다. 통역 시 주의할 점은 '폴리머'를 베트남어로 그대로 'polymer'로 음차하되, 일반 시멘트와 완전히 다른 제품임을 강조해야 합니다. 주로 타일 접착, 방수층, 보수 모르타르에 사용되며, 일반 시멘트로 대체할 수 없는 전문 재료입니다. 액상형(에멀젼)과 분말형(재유화형 분말)이 있으며, 용도에 따라 선택이 달라지므로 정확한 제품 정보 전달이 중요합니다.",
        "meaningVi": "Xi măng pha với nhựa polymer (polyme) để tăng độ bám dính, chống thấm và độ bền. Dùng cho dán gạch, lớp chống thấm, vữa sửa chữa. Không thể thay thế bằng xi măng thường. Có dạng lỏng (nhũ tương) và dạng bột (bột tái nhũ hóa).",
        "context": "타일 시공, 방수층 형성, 보수 공사, 바닥 마감",
        "culturalNote": "한국에서는 욕실, 주방 타일 시공 시 폴리머시멘트 사용이 표준화되어 있으며, 아파트 건설에서 필수 자재입니다. 베트남도 타일 시공에 폴리머 접착제를 사용하지만, 한국처럼 시멘트 기반 제품보다는 아크릴 본드형 접착제를 선호하는 경향이 있습니다. 한국 기술자가 '폴리머시멘트'를 지시하면, 베트남 현장에서는 'Xi măng polymer' 또는 'Keo dán gạch polymer'로 명확히 전달해야 하며, 일반 시멘트 모르타르에 본드를 섞는 재래식 공법과 구분해야 합니다. 제품 브랜드명으로 통칭되는 경우도 많아, 성분 기준 설명이 필요합니다.",
        "commonMistakes": [
            {
                "mistake": "폴리머시멘트를 일반 시멘트에 본드 섞은 것으로 오해",
                "correction": "공장에서 배합된 전문 제품, 현장 혼합과 다름",
                "explanation": "성능과 품질이 완전히 다름"
            },
            {
                "mistake": "타일 접착제(keo dán gạch)와 폴리머시멘트 혼동",
                "correction": "타일 접착제 중 시멘트 기반 제품이 폴리머시멘트",
                "explanation": "타일 접착제는 더 넓은 개념"
            },
            {
                "mistake": "'플라스틱 시멘트'로 오역",
                "correction": "Xi măng polymer (폴리머시멘트)",
                "explanation": "폴리머와 플라스틱은 다른 개념"
            }
        ],
        "examples": [
            {
                "ko": "욕실 바닥 타일은 폴리머시멘트로 시공하세요.",
                "vi": "Gạch sàn phòng tắm thi công bằng xi măng polymer.",
                "situation": "onsite"
            },
            {
                "ko": "이 방수층은 폴리머시멘트 2회 도포입니다.",
                "vi": "Lớp chống thấm này phết xi măng polymer 2 lần.",
                "situation": "formal"
            },
            {
                "ko": "균열 보수는 일반 시멘트 말고 폴리머시멘트 써야 해요.",
                "vi": "Sửa vết nứt phải dùng xi măng polymer chứ không dùng xi măng thường.",
                "situation": "onsite"
            }
        ],
        "relatedTerms": ["타일시공", "방수제", "접착제", "보수모르타르"]
    },
    {
        "slug": "vua-grouting",
        "korean": "그라우트재",
        "vietnamese": "Vữa grouting / Vữa chèn kín",
        "hanja": "그라우트材",
        "hanjaReading": None,
        "pronunciation": "그라우트재",
        "meaningKo": "기초, 앵커볼트, 기계 하부, 균열 등에 주입하여 공극을 채우고 고정하는 특수 모르타르입니다. 통역 시 주의할 점은 'grouting'을 베트남어로 음차할 수도 있지만, 'vữa chèn kín'(틈새 메우는 모르타르)처럼 기능을 설명하는 표현을 병행해야 현장 근로자들이 이해하기 쉽습니다. 무수축(팽창) 그라우트와 일반 그라우트를 구분해야 하며, 유동성이 매우 중요하므로 배합 비율과 주입 방법을 정확히 전달해야 합니다. 기계 기초, 프리캐스트 접합부, 포스트텐션 공사에서 필수적입니다.",
        "meaningVi": "Vữa đặc biệt dùng để đổ chèn vào móng, bu lông neo, đáy máy móc, vết nứt nhằm lấp kín khe hở và cố định. Cần phân biệt grouting không co ngót (có nở) và grouting thường. Tính lưu động rất quan trọng. Dùng cho móng máy, mối nối precast, công trình căng sau.",
        "context": "기계 기초 공사, 앵커볼트 고정, 프리캐스트 접합, 균열 주입",
        "culturalNote": "한국에서는 공장, 발전소 등 중장비 설치 시 무수축 그라우트가 표준이며, 제품명으로 통칭되는 경우가 많습니다(예: '마스터플로우', '유코그라우트'). 베트남도 산업 시설 증가로 그라우팅 공사가 늘었지만, 한국만큼 전문화되지 않아 일반 모르타르와 혼동하는 경우가 있습니다. 한국 기술자가 '그라우트 쳐라'고 지시하면, 베트남 현장에서는 'đổ vữa grouting' 또는 'bơm vữa chèn kín'으로 명확히 전달하되, 무수축 여부를 반드시 확인해야 합니다. 또한 'grouting'은 재료와 공법 모두를 지칭할 수 있으므로, 맥락에 따라 해석해야 합니다.",
        "commonMistakes": [
            {
                "mistake": "그라우트를 일반 모르타르(vữa thường)로 오해",
                "correction": "특수 배합된 무수축 또는 고유동 모르타르",
                "explanation": "일반 모르타르는 수축해 틈새 발생"
            },
            {
                "mistake": "grouting을 '주입(bơm)'으로만 번역",
                "correction": "재료(vữa grouting) + 공법(bơm chèn) 구분",
                "explanation": "재료명인지 공법명인지 맥락 파악 필요"
            },
            {
                "mistake": "무수축 그라우트와 일반 그라우트 구분 안 함",
                "correction": "Grouting không co ngót vs Grouting thường",
                "explanation": "용도와 성능이 완전히 다름"
            }
        ],
        "examples": [
            {
                "ko": "기계 하부는 무수축 그라우트로 충전하세요.",
                "vi": "Đáy máy móc phải đổ đầy bằng vữa grouting không co ngót.",
                "situation": "onsite"
            },
            {
                "ko": "앵커볼트 구멍에 그라우트 주입 완료했습니다.",
                "vi": "Đã bơm vữa grouting vào lỗ bu lông neo xong.",
                "situation": "formal"
            },
            {
                "ko": "PC 부재 접합부 그라우팅 전에 물 빼야 해요.",
                "vi": "Trước khi grouting mối nối PC phải tháo nước.",
                "situation": "onsite"
            }
        ],
        "relatedTerms": ["무수축콘크리트", "팽창제", "앵커볼트", "프리캐스트"]
    }
]

# 파일 경로
construction_file = os.path.join(
    os.path.dirname(__file__),
    "..",
    "data",
    "terms",
    "construction.json"
)

# 기존 데이터 로드
with open(construction_file, "r", encoding="utf-8") as f:
    existing_data = json.load(f)

# 새 데이터 추가
existing_data.extend(data)

# 파일 저장
with open(construction_file, "w", encoding="utf-8") as f:
    json.dump(existing_data, f, ensure_ascii=False, indent=2)

print(f"✅ {len(data)}개 용어 추가 완료")
print(f"📂 총 {len(existing_data)}개 용어")
