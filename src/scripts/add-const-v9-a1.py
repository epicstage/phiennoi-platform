#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
건설(construction) 용어 추가 스크립트 v9-a1
테마: 건축음향/소음 (차음, 흡음계수, 충격음, 바닥충격음, 차음등급, 방음문, 이중바닥, 이중벽, 공명흡음, 소음기준)
"""

import json
import os

# 추가할 용어 데이터 (배열 형태)
data = [
    {
        "slug": "cach-am",
        "korean": "차음",
        "vietnamese": "Cách âm",
        "hanja": "遮音",
        "hanjaReading": "가릴 차(遮) + 소리 음(音)",
        "pronunciation": "차음",
        "meaningKo": "건축에서 소음이 벽, 바닥, 천장 등의 구조물을 통해 다른 공간으로 전달되는 것을 차단하는 기술 또는 성능을 의미하며, '차단음', '방음'과 유사하지만 엄밀히는 구분됩니다. 통역 시 주의할 점은 '차음'은 소리의 투과를 막는 것이고, '흡음'은 반사음을 줄이는 것으로 목적이 다릅니다. 한국의 공동주택 층간소음 기준(「공동주택 바닥충격음 차단구조 인정 및 관리기준」)에서는 경량충격음 58dB 이하, 중량충격음 50dB 이하를 요구하며, 차음 성능이 이를 만족해야 입주가 가능합니다. 차음 방법에는 질량 증가(콘크리트 두께), 이중벽 구조, 차음재 삽입 등이 있으며, 주파수 대역에 따라 효과가 다릅니다. 통역 시 차음등급(STC, Sound Transmission Class)과 충격음 저감 등급(ΔL)을 혼동하지 않도록 주의해야 합니다.",
        "meaningVi": "Cách âm (차음) là kỹ thuật hoặc hiệu năng ngăn chặn tiếng ồn truyền qua tường, sàn, trần và các kết cấu khác sang không gian khác trong xây dựng. Cần phân biệt với 'hấp thụ âm' (흡음) - cách âm là ngăn âm thanh xuyên qua, còn hấp thụ âm là giảm âm phản xạ. Tại Hàn Quốc, theo tiêu chuẩn tiếng ồn tầng trong chung cư, âm va chạm nhẹ phải ≤58dB, âm va chạm nặng ≤50dB. Phương pháp cách âm bao gồm tăng khối lượng (tăng độ dày bê tông), kết cấu tường kép, chèn vật liệu cách âm, hiệu quả khác nhau tùy dải tần số. Khi phiên dịch, không được nhầm lẫn giữa cấp cách âm (STC) và cấp giảm âm va chạm (ΔL).",
        "context": "공동주택 층간소음, 방송국/녹음실 설계, 호텔/병원 차음 설계",
        "culturalNote": "한국에서는 2005년 이후 층간소음 민원이 급증하면서 차음 성능이 건축 설계의 핵심 요소가 되었고, 2013년부터 바닥충격음 차단구조 인정제도가 강화되었습니다. 입주 전 바닥충격음 성능 인증서를 제출해야 하며, 기준 미달 시 입주가 불가능합니다. 한국 주민들은 층간소음에 매우 민감하여 법적 분쟁까지 이어지는 경우가 많습니다. 베트남에서는 차음 개념이 상대적으로 덜 중요하게 여겨지며, 이중벽이나 차음재 시공이 필수가 아닌 경우가 많습니다. 통역 시 한국의 엄격한 차음 기준과 법적 의무를 명확히 전달하고, 시공 단계별로 차음 성능 검증이 이루어진다는 점을 강조해야 합니다.",
        "commonMistakes": [
            {
                "mistake": "'cách âm'과 'hấp thụ âm'(흡음)을 혼동하여 사용",
                "correction": "차음은 'cách âm'(투과 차단), 흡음은 'hấp thụ âm'(반사 감소)",
                "explanation": "차음과 흡음은 원리와 목적이 다른 별개 기술입니다."
            },
            {
                "mistake": "차음등급(STC)과 충격음등급(ΔL)을 같은 것으로 통역",
                "correction": "STC는 공기전달음 차단 성능, ΔL는 충격음 저감 성능",
                "explanation": "평가 대상 소음 종류가 다르므로 구분해야 합니다."
            },
            {
                "mistake": "차음 기준 미달의 법적 결과(입주 불가) 미전달",
                "correction": "기준 미달 시 입주 금지 및 재시공 의무 명시",
                "explanation": "차음 성능은 선택이 아닌 법적 필수 요건임을 강조해야 합니다."
            }
        ],
        "examples": [
            {
                "ko": "이 벽체의 차음 성능은 STC 55 등급으로, 일반 대화 소리는 거의 들리지 않는 수준입니다.",
                "vi": "Hiệu năng cách âm của bức tường này là cấp STC 55, mức độ gần như không nghe thấy tiếng nói chuyện thường.",
                "situation": "formal"
            },
            {
                "ko": "바닥 차음 구조는 콘크리트 슬래브 위에 완충재, 경량기포 콘크리트, 마감 몰탈 순으로 시공합니다.",
                "vi": "Kết cấu cách âm sàn được thi công theo thứ tự: tấm bê tông sàn, vật liệu đệm, bê tông bọt nhẹ, vữa hoàn thiện.",
                "situation": "onsite"
            },
            {
                "ko": "윗집 발소리가 다 들려. 차음이 제대로 안 됐나봐.",
                "vi": "Nghe cả tiếng bước chân tầng trên. Có vẻ cách âm không được làm đúng.",
                "situation": "informal"
            }
        ],
        "relatedTerms": [
            "흡음",
            "바닥충격음",
            "차음등급",
            "이중벽",
            "완충재"
        ]
    },
    {
        "slug": "he-so-hap-thu-am",
        "korean": "흡음계수",
        "vietnamese": "Hệ số hấp thụ âm",
        "hanja": "吸音係數",
        "hanjaReading": "빨아들일 흡(吸) + 소리 음(音) + 맺을 계(係) + 셈 수(數)",
        "pronunciation": "흡음계수",
        "meaningKo": "재료 표면에 입사한 음파 에너지 중 반사되지 않고 흡수되는 비율을 나타내는 무차원 수치로, 0(완전 반사)에서 1(완전 흡수) 사이 값을 가지며, 주파수별로 다른 값을 갖습니다. 통역 시 주의할 점은 흡음계수가 높다고 차음 성능이 좋은 것은 아니며, 흡음은 실내 반향(잔향시간)을 줄이는 데 목적이 있고 차음은 소리의 투과를 막는 데 목적이 있습니다. 한국 건축음향 설계에서는 주로 125Hz, 250Hz, 500Hz, 1kHz, 2kHz, 4kHz의 6개 옥타브 밴드 주파수에서 흡음계수를 측정하며, KS F 2805(잔향실법)와 KS F 2814(관 내 측정법) 표준을 사용합니다. 일반적으로 다공성 재료(글라스울, 암면)는 고주파 흡음에 유리하고, 공명 흡음 구조는 저주파 흡음에 효과적입니다. 통역 시 흡음계수 NRC(Noise Reduction Coefficient, 소음감소계수) 값도 함께 사용되는데, 이는 250~2kHz의 평균값을 의미합니다.",
        "meaningVi": "Hệ số hấp thủ âm (흡음계수) là giá trị vô thứ nguyên biểu thị tỷ lệ năng lượng sóng âm chiếu vào bề mặt vật liệu bị hấp thụ (không phản xạ), có giá trị từ 0 (phản xạ hoàn toàn) đến 1 (hấp thụ hoàn toàn), khác nhau theo tần số. Cần lưu ý: hệ số hấp thụ âm cao không có nghĩa là hiệu năng cách âm tốt - hấp thụ âm nhằm giảm tiếng vang trong phòng, còn cách âm nhằm ngăn âm xuyên qua. Trong thiết kế âm thanh kiến trúc Hàn Quốc, đo hệ số hấp thụ âm tại 6 tần số octave: 125Hz, 250Hz, 500Hz, 1kHz, 2kHz, 4kHz theo tiêu chuẩn KS F 2805 và KS F 2814. Vật liệu xốp (bông thủy tinh, bông khoáng) có lợi cho hấp thụ tần số cao, cấu trúc cộng hưởng hiệu quả với tần số thấp. Cũng sử dụng giá trị NRC (Noise Reduction Coefficient) - trung bình từ 250~2kHz.",
        "context": "강당/극장 음향 설계, 녹음실/방송국 설계, 사무실 소음 저감",
        "culturalNote": "한국의 건축음향 설계에서는 용도별로 흡음계수 기준이 세밀하게 정해져 있습니다. 예를 들어 음악당은 잔향시간 1.8~2.2초를 위해 부분적 흡음재를 사용하고, 회의실은 명료도를 위해 0.6~0.8초로 짧게 설계하며, 녹음실은 0.3초 이하로 매우 짧게 만듭니다. 최근에는 오픈 오피스가 증가하면서 천장 흡음재(흡음 텍스 등)와 파티션 흡음 패널이 필수가 되었습니다. 베트남 건설 현장에서는 흡음과 차음을 구분하지 않고 '방음'으로 통칭하는 경우가 많아 혼란이 생기므로, 통역 시 'hấp thụ âm'(흡음)과 'cách âm'(차음)을 명확히 구분하고, 각각의 목적과 재료가 다름을 반드시 설명해야 합니다.",
        "commonMistakes": [
            {
                "mistake": "흡음계수를 차음 성능 지표로 잘못 설명",
                "correction": "흡음은 반향 감소, 차음은 투과 차단으로 목적 구분",
                "explanation": "흡음과 차음은 완전히 다른 개념이므로 혼동하면 안 됩니다."
            },
            {
                "mistake": "NRC를 '소음 제거율'로 오역",
                "correction": "NRC는 '소음감소계수' 또는 '평균 흡음계수'",
                "explanation": "NRC는 흡음 성능의 평균값이지 소음 제거율이 아닙니다."
            },
            {
                "mistake": "주파수별 차이 설명 누락",
                "correction": "저주파/고주파별로 흡음계수가 다르다고 명시",
                "explanation": "재료마다 주파수별 흡음 특성이 다르므로 설명 필요합니다."
            }
        ],
        "examples": [
            {
                "ko": "이 글라스울 흡음재는 500Hz에서 흡음계수 0.85, NRC 0.75로 중고음역 흡음에 매우 효과적입니다.",
                "vi": "Vật liệu hấp thụ âm bông thủy tinh này có hệ số hấp thụ âm 0,85 tại 500Hz, NRC 0,75, rất hiệu quả với âm tần trung-cao.",
                "situation": "formal"
            },
            {
                "ko": "회의실 천장에 흡음 텍스를 시공하여 잔향시간을 1.2초에서 0.7초로 단축했습니다.",
                "vi": "Đã thi công tấm hấp thụ âm trên trần phòng họp, rút ngắn thời gian vang từ 1,2 giây xuống 0,7 giây.",
                "situation": "formal"
            },
            {
                "ko": "여기 울림이 심하네. 천장에 흡음재 좀 달아야겠어.",
                "vi": "Chỗ này vang nhiều quá. Phải gắn vật liệu hấp âm lên trần.",
                "situation": "informal"
            }
        ],
        "relatedTerms": [
            "차음",
            "잔향시간",
            "NRC",
            "글라스울",
            "흡음재"
        ]
    },
    {
        "slug": "am-va-cham",
        "korean": "충격음",
        "vietnamese": "Âm va chạm",
        "hanja": "衝擊音",
        "hanjaReading": "찌를 충(衝) + 칠 격(擊) + 소리 음(音)",
        "pronunciation": "충격음",
        "meaningKo": "물체가 바닥, 벽 등의 구조물에 충돌할 때 구조물을 직접 가진시켜 발생하는 고체전달음으로, 공기를 통해 전달되는 공기전달음과 구분되며, 아파트 층간소음의 주요 원인입니다. 통역 시 주의할 점은 충격음에는 '경량충격음'(가볍고 날카로운 소리, 슬리퍼 소리)과 '중량충격음'(무겁고 둔탁한 소리, 어린이 뛰는 소리)이 있으며 각각 저감 방법이 다릅니다. 한국의 「공동주택 바닥충격음 차단구조 인정 및 관리기준」에서는 경량충격음 58dB 이하, 중량충격음 50dB 이하를 요구하며, 준공 전 성능 인증이 필수입니다. 충격음 저감을 위해서는 바닥 완충재(쿠션), 뜬바닥(이중바닥) 구조, 슬래브 두께 증가 등의 방법을 사용하며, 경량충격음은 완충재로, 중량충격음은 슬래브 질량 증가로 대응합니다. 통역 시 충격음 레벨(dB)이 낮을수록 성능이 좋다는 점을 명확히 해야 합니다.",
        "meaningVi": "Âm va chạm (충격음) là âm truyền qua vật rắn phát sinh khi vật thể va chạm trực tiếp vào sàn, tường và làm rung động kết cấu, khác với âm truyền qua không khí, là nguyên nhân chính gây tiếng ồn tầng trong chung cư. Có hai loại: 'âm va chạm nhẹ' (tiếng nhẹ sắc, như tiếng dép lê) và 'âm va chạm nặng' (tiếng nặng trầm, như trẻ em chạy nhảy), mỗi loại có phương pháp giảm khác nhau. Tại Hàn Quốc, tiêu chuẩn chung cư yêu cầu âm va chạm nhẹ ≤58dB, âm va chạm nặng ≤50dB, phải có chứng nhận hiệu năng trước khi nghiệm thu. Phương pháp giảm âm va chạm: vật liệu đệm sàn, cấu trúc sàn nổi (sàn kép), tăng độ dày sàn bê tông. Âm va chạm nhẹ giảm bằng vật liệu đệm, âm va chạm nặng giảm bằng tăng khối lượng sàn. Lưu ý: mức âm va chạm (dB) càng thấp thì hiệu năng càng tốt.",
        "context": "공동주택 층간소음, 호텔/병원 바닥 설계, 사무실 충격음 저감",
        "culturalNote": "한국에서는 2000년대 중반 이후 아파트 층간소음 분쟁이 사회 문제화되면서 충격음 기준이 계속 강화되었습니다. 2013년 이전에는 경량충격음만 규제했으나, 현재는 중량충격음까지 법적 기준이 있으며, 입주 전 현장 측정을 통해 인증을 받아야 합니다. 측정은 ISO 16283-2(현장측정법) 기준을 따르며, 태핑머신(경량)과 뱅머신(중량)을 사용합니다. 베트남에서는 충격음 개념이 생소하여 단순히 '시끄럽다/조용하다'로만 판단하는 경향이 있으므로, 통역 시 경량/중량 충격음의 차이, dB 수치의 의미(낮을수록 좋음), 법적 기준과 인증 절차를 구체적으로 설명해야 합니다.",
        "commonMistakes": [
            {
                "mistake": "경량충격음과 중량충격음을 구분하지 않고 통역",
                "correction": "'âm va chạm nhẹ'와 'âm va chạm nặng'으로 명확히 구분",
                "explanation": "소음 특성과 저감 방법이 완전히 다르므로 구분 필수입니다."
            },
            {
                "mistake": "충격음 dB 수치가 높을수록 좋다고 오해",
                "correction": "dB 수치가 낮을수록 충격음이 작아 성능이 좋음",
                "explanation": "dB는 소음 크기이므로 낮을수록 조용한 것입니다."
            },
            {
                "mistake": "충격음과 공기전달음을 혼동",
                "correction": "충격음은 구조 진동, 공기전달음은 공기 전파로 구분",
                "explanation": "전달 경로와 저감 방법이 다르므로 구분해야 합니다."
            }
        ],
        "examples": [
            {
                "ko": "이 현장의 바닥충격음 측정 결과는 경량충격음 55dB, 중량충격음 48dB로 기준을 만족합니다.",
                "vi": "Kết quả đo âm va chạm sàn tại hiện trường này: âm va chạm nhẹ 55dB, âm va chạm nặng 48dB, đạt tiêu chuẩn.",
                "situation": "formal"
            },
            {
                "ko": "중량충격음 저감을 위해 슬래브 두께를 210mm에서 240mm로 증가시켰습니다.",
                "vi": "Để giảm âm va chạm nặng, đã tăng độ dày sàn bê tông từ 210mm lên 240mm.",
                "situation": "onsite"
            },
            {
                "ko": "윗집 애들 뛰는 소리가 너무 시끄러워. 충격음 기준 넘는 거 아니야?",
                "vi": "Tiếng애em tầng trên chạy nhảy ồn quá. Có vượt chuẩn âm va chạm không nhỉ?",
                "situation": "informal"
            }
        ],
        "relatedTerms": [
            "경량충격음",
            "중량충격음",
            "바닥충격음",
            "완충재",
            "뜬바닥"
        ]
    },
    {
        "slug": "am-va-cham-san",
        "korean": "바닥충격음",
        "vietnamese": "Âm va chạm sàn",
        "hanja": "床衝擊音",
        "hanjaReading": "마루 상(床) + 찌를 충(衝) + 칠 격(擊) + 소리 음(音)",
        "pronunciation": "바닥충격음",
        "meaningKo": "바닥 슬래브에 충격이 가해질 때 발생하는 충격음으로, 공동주택에서 층간소음의 가장 큰 원인이며, 한국에서는 법적으로 엄격하게 규제되는 건축 성능 지표입니다. 통역 시 주의할 점은 바닥충격음은 단순히 '층간소음' 전체를 의미하는 것이 아니라 바닥을 통해 전달되는 충격음만을 지칭하며, 벽을 통한 소음(공기전달음)은 포함하지 않습니다. 「주택건설기준 등에 관한 규정」 제14조의2에 따라 공동주택은 바닥충격음 차단 성능을 인정받아야 하며, 경량충격음 58dB 이하, 중량충격음 50dB 이하 기준을 충족해야 입주가 가능합니다. 바닥충격음 저감 구조로는 완충재 + 경량기포콘크리트 + 마감 몰탈의 뜬바닥 구조, 슬래브 두께 증가(210mm 이상), 천장 흡음재 등이 사용됩니다. 통역 시 준공 전 현장 측정 의무와 기준 미달 시 재시공 책임을 명확히 전달해야 합니다.",
        "meaningVi": "Âm va chạm sàn (바닥충격음) là âm va chạm phát sinh khi sàn bê tông chịu lực va chạm, là nguyên nhân chính gây tiếng ồn tầng trong chung cư, là chỉ tiêu hiệu năng xây dựng được quy định pháp luật nghiêm ngặt tại Hàn Quốc. Cần lưu ý: âm va chạm sàn không phải là toàn bộ 'tiếng ồn tầng' mà chỉ là âm va chạm truyền qua sàn, không bao gồm tiếng ồn qua tường (âm truyền không khí). Theo Quy định Tiêu chuẩn Xây dựng Nhà ở Điều 14-2, chung cư phải được công nhận hiệu năng cách âm va chạm sàn: âm va chạm nhẹ ≤58dB, âm va chạm nặng ≤50dB mới được cho nhập cư. Cấu trúc giảm âm va chạm sàn: sàn nổi (vật liệu đệm + bê tông bọt nhẹ + vữa hoàn thiện), tăng độ dày sàn (≥210mm), vật liệu hấp thụ âm trần. Khi phiên dịch, phải nói rõ nghĩa vụ đo lường hiện trường trước nghiệm thu và trách nhiệm thi công lại nếu không đạt chuẩn.",
        "context": "공동주택 설계/시공, 층간소음 분쟁, 입주 전 성능 인증",
        "culturalNote": "한국의 바닥충격음 규제는 세계에서 가장 엄격한 수준으로, 2005년 층간소음 이웃 간 폭행 사건 이후 사회적 관심이 급증하면서 법제화되었습니다. 2013년부터는 입주 전 현장 측정을 통한 성능 인증이 의무화되었고, 기준 미달 시 시공사가 재시공 책임을 집니다. 측정은 세대당 최소 3곳 이상에서 실시하며, 공인기관의 인증서가 필요합니다. 최근에는 50dB/58dB 기준보다 더 엄격한 '최상급' 인증(중량 43dB, 경량 50dB)을 받는 아파트가 고급 단지의 마케팅 포인트가 되었습니다. 베트남에서는 바닥충격음 개념 자체가 생소하므로, 통역 시 한국의 엄격한 법적 기준, 인증 절차, 기준 미달 시 입주 불가 및 재시공 의무를 구체적으로 설명해야 합니다.",
        "commonMistakes": [
            {
                "mistake": "'층간소음'과 '바닥충격음'을 같은 의미로 사용",
                "correction": "바닥충격음은 층간소음의 일부(바닥 전달음만)",
                "explanation": "층간소음에는 벽 전달음도 포함되므로 구분 필요합니다."
            },
            {
                "mistake": "경량/중량 충격음 기준을 하나로 통합하여 전달",
                "correction": "경량 58dB, 중량 50dB를 각각 명시",
                "explanation": "각각 다른 기준이므로 따로 전달해야 합니다."
            },
            {
                "mistake": "현장 측정 의무와 인증 절차 설명 누락",
                "correction": "준공 전 공인기관 측정 및 인증서 제출 의무 명시",
                "explanation": "법적 의무 사항이므로 반드시 전달해야 합니다."
            }
        ],
        "examples": [
            {
                "ko": "이 단지는 바닥충격음 최상급 인증을 받아 중량충격음 43dB, 경량충격음 50dB을 달성했습니다.",
                "vi": "Khu này đạt chứng nhận âm va chạm sàn cấp cao nhất với âm va chạm nặng 43dB, âm va chạm nhẹ 50dB.",
                "situation": "formal"
            },
            {
                "ko": "바닥충격음 현장 측정은 세대당 3곳 이상, 공인 측정기관이 실시합니다.",
                "vi": "Đo âm va chạm sàn tại hiện trường tối thiểu 3 vị trí mỗi căn, do cơ quan đo lường được công nhận thực hiện.",
                "situation": "onsite"
            },
            {
                "ko": "바닥충격음 기준 통과 못 하면 입주 못 한대. 재시공해야 한대.",
                "vi": "Nghe nói nếu không qua chuẩn âm va chạm sàn thì không được nhập cư. Phải thi công lại.",
                "situation": "informal"
            }
        ],
        "relatedTerms": [
            "충격음",
            "층간소음",
            "뜬바닥",
            "완충재",
            "차음등급"
        ]
    },
    {
        "slug": "cap-cach-am",
        "korean": "차음등급",
        "vietnamese": "Cấp cách âm",
        "hanja": "遮音等級",
        "hanjaReading": "가릴 차(遮) + 소리 음(音) + 무리 등(等) + 등급 급(級)",
        "pronunciation": "차음등급",
        "meaningKo": "벽, 바닥, 문 등의 구조물이 공기를 통해 전달되는 소음을 차단하는 성능을 나타내는 등급으로, 주로 STC(Sound Transmission Class) 값으로 표시되며 숫자가 클수록 차음 성능이 우수합니다. 통역 시 주의할 점은 차음등급(STC)은 공기전달음(말소리, TV 소리 등) 차단 성능을 평가하는 것이고, 바닥충격음 저감 등급(ΔL, 델타L)은 충격음 차단 성능을 평가하는 것으로 서로 다른 개념입니다. 한국 건축음향 설계에서 일반적으로 아파트 세대 간 벽체는 STC 50 이상, 호텔 객실 간 벽체는 STC 55 이상, 녹음실/방송국은 STC 60 이상을 요구합니다. STC 25는 일반 대화가 명확히 들리고, STC 35는 큰 소리가 들리며, STC 45는 큰 소리가 희미하게 들리고, STC 50 이상은 일반 소음이 거의 들리지 않는 수준입니다. 통역 시 차음등급은 벽/문/창호의 성능 지표이며, 시공 품질에 따라 실제 성능이 달라질 수 있다는 점을 강조해야 합니다.",
        "meaningVi": "Cấp cách âm (차음등급) là cấp độ biểu thị hiệu năng ngăn chặn tiếng ồn truyền qua không khí của tường, sàn, cửa và các kết cấu, chủ yếu dùng giá trị STC (Sound Transmission Class), số càng lớn thì hiệu năng cách âm càng tốt. Cần phân biệt: cấp cách âm (STC) đánh giá hiệu năng ngăn âm truyền không khí (tiếng nói, TV...), còn cấp giảm âm va chạm (ΔL, delta L) đánh giá hiệu năng ngăn âm va chạm. Trong thiết kế âm thanh kiến trúc Hàn Quốc, thường yêu cầu: tường giữa các căn chung cư ≥STC 50, tường giữa phòng khách sạn ≥STC 55, phòng thu/đài phát thanh ≥STC 60. STC 25: nghe rõ nói chuyện thường, STC 35: nghe tiếng lớn, STC 45: tiếng lớn nghe mờ, STC ≥50: hầu như không nghe tiếng ồn thường. Khi phiên dịch, cần nhấn mạnh cấp cách âm là chỉ tiêu của tường/cửa/cửa sổ, hiệu năng thực tế có thể khác tùy chất lượng thi công.",
        "context": "아파트/호텔 벽체 설계, 방음문/방음창 성능, 녹음실 설계",
        "culturalNote": "한국에서는 공동주택 세대 간 경계벽의 차음등급이 법적으로 규제되며, 「주택건설기준 등에 관한 규정」에서 공동주택 경계벽은 차음등급 2등급 이상(대략 STC 50 이상)을 요구합니다. 특히 고급 주택이나 호텔에서는 STC 55~60의 높은 차음 성능을 마케팅 포인트로 활용합니다. 차음등급을 높이기 위해서는 벽체 질량 증가(이중벽, 콘크리트 두께 증가), 공기층 확보, 차음재 삽입 등의 방법을 사용합니다. 베트남에서는 STC 개념이 생소하고 단순히 '두꺼운 벽 = 조용하다'로 이해하는 경향이 있으므로, 통역 시 STC 수치와 실제 소음 차단 효과의 관계(예: STC 50은 일반 대화 안 들림)를 구체적 예시로 설명하고, 시공 품질(틈새, 접합부)이 중요함을 강조해야 합니다.",
        "commonMistakes": [
            {
                "mistake": "STC를 충격음 저감 등급(ΔL)과 혼동",
                "correction": "STC는 공기전달음 차단, ΔL는 충격음 저감",
                "explanation": "평가 대상 소음 종류가 다르므로 명확히 구분해야 합니다."
            },
            {
                "mistake": "STC 수치만 전달하고 실제 의미 설명 누락",
                "correction": "STC 50 = 일반 대화 안 들림 등 구체적 설명 추가",
                "explanation": "숫자만으로는 실제 성능을 이해하기 어렵습니다."
            },
            {
                "mistake": "설계 STC와 실제 시공 성능을 동일하게 전달",
                "correction": "시공 품질(틈새, 접합부)에 따라 실제 성능 차이 발생",
                "explanation": "이론값과 실측값에 차이가 있을 수 있음을 알려야 합니다."
            }
        ],
        "examples": [
            {
                "ko": "이 경계벽은 240mm 콘크리트 + 50mm 공기층 + 100mm 경량벽체로 STC 52 등급을 달성합니다.",
                "vi": "Bức tường ngăn này đạt cấp STC 52 với cấu tạo: bê tông 240mm + khoảng không khí 50mm + tường nhẹ 100mm.",
                "situation": "formal"
            },
            {
                "ko": "방음문 교체 후 차음등급이 STC 30에서 STC 45로 향상되어 복도 소음이 현저히 감소했습니다.",
                "vi": "Sau khi thay cửa cách âm, cấp cách âm tăng từ STC 30 lên STC 45, tiếng ồn hành lang giảm đáng kể.",
                "situation": "onsite"
            },
            {
                "ko": "옆집 TV 소리 들려. 차음등급이 낮나봐.",
                "vi": "Nghe tiếng TV nhà bên. Có vẻ cấp cách âm thấp.",
                "situation": "informal"
            }
        ],
        "relatedTerms": [
            "STC",
            "차음",
            "이중벽",
            "방음문",
            "공기전달음"
        ]
    },
    {
        "slug": "cua-cach-am",
        "korean": "방음문",
        "vietnamese": "Cửa cách âm",
        "hanja": "防音門",
        "hanjaReading": "막을 방(防) + 소리 음(音) + 문 문(門)",
        "pronunciation": "방음문",
        "meaningKo": "소음 차단을 목적으로 특수 설계된 문으로, 일반 문보다 두껍고 무거우며 문틀과의 밀착을 위한 기밀 패킹(seal)이 부착되어 있어 공기전달음을 효과적으로 차단합니다. 통역 시 주의할 점은 방음문의 성능은 STC(차음등급) 값으로 표시되며, 일반 문은 STC 20~25, 표준 방음문은 STC 30~35, 고성능 방음문은 STC 40~50 수준입니다. 방음문은 문짝(door leaf)의 차음 성능뿐 아니라 문틀과의 틈새, 문턱(threshold), 경첩(hinge) 부위의 기밀성이 매우 중요하며, 이 중 하나라도 불량하면 전체 성능이 크게 저하됩니다. 한국 건축에서는 녹음실, 방송국, 영화관, 호텔 객실, 병원 진료실 등에 방음문이 필수적으로 사용되며, 최근에는 주택 안방이나 공부방에도 방음문 수요가 증가하고 있습니다. 통역 시 방음문은 항상 닫혀 있어야 효과가 있으며, 문턱이나 하부 씰을 제거하면 성능이 사라진다는 점을 강조해야 합니다.",
        "meaningVi": "Cửa cách âm (방음문) là cửa được thiết kế đặc biệt để ngăn tiếng ồn, dày và nặng hơn cửa thường, có gioăng kín khí (seal) để bám sát với khung cửa nhằm ngăn chặn âm truyền không khí hiệu quả. Hiệu năng cửa cách âm biểu thị bằng giá trị STC (cấp cách âm): cửa thường STC 20~25, cửa cách âm tiêu chuẩn STC 30~35, cửa cách âm cao cấp STC 40~50. Hiệu năng cửa cách âm không chỉ phụ thuộc vào cánh cửa mà còn vào độ kín khe hở với khung, ngưỡng cửa (threshold), bản lề (hinge) - một trong số này kém thì toàn bộ hiệu năng giảm mạnh. Tại Hàn Quốc, cửa cách âm là thiết bị bắt buộc tại phòng thu, đài phát thanh, rạp phim, phòng khách sạn, phòng khám bệnh viện, gần đây nhu cầu lắp cửa cách âm tại phòng ngủ chính và phòng học ở nhà cũng tăng. Khi phiên dịch, cần nhấn mạnh cửa cách âm chỉ có hiệu quả khi luôn đóng, nếu tháo ngưỡng cửa hoặc gioăng dưới thì mất hiệu năng.",
        "context": "녹음실/방송국 설계, 호텔/병원 객실, 주택 방음 개조",
        "culturalNote": "한국에서는 층간소음 및 생활소음에 대한 민감도가 높아지면서 방음문 시장이 크게 성장했습니다. 특히 재택근무와 온라인 수업이 증가하면서 가정용 방음문 수요가 급증했고, DIY 방음문 개조 제품도 인기를 끌고 있습니다. 전문 방음문은 문짝 내부에 차음재(고무, 흡음재, 공기층)를 다층으로 삽입하고, 문틀 전체에 기밀 패킹을 부착하며, 문 하부에는 자동 강하 씰(automatic drop seal)을 장착하여 문을 닫으면 자동으로 내려와 바닥과 틈새를 막습니다. 베트남에서는 방음문 개념이 생소하여 일반 철문이나 목문을 사용하는 경우가 많으므로, 통역 시 방음문의 구조(다층 구조, 기밀 패킹, 자동 씰), STC 성능 차이, 설치 후 유지관리(패킹 교체, 씰 점검)의 중요성을 구체적으로 설명해야 합니다.",
        "commonMistakes": [
            {
                "mistake": "'cửa dày'(두꺼운 문)로만 통역하여 일반 철문과 혼동",
                "correction": "'cửa cách âm chuyên dụng' (전문 방음문)으로 명시",
                "explanation": "단순 두께가 아닌 차음 설계가 핵심임을 강조해야 합니다."
            },
            {
                "mistake": "문짝 성능만 설명하고 문틀/씰/문턱 중요성 누락",
                "correction": "기밀 패킹, 문턱, 씰이 성능에 핵심적임을 명시",
                "explanation": "틈새가 있으면 문짝이 아무리 좋아도 소용없습니다."
            },
            {
                "mistake": "방음문을 열어놓거나 문턱 제거 시 영향 미전달",
                "correction": "열어두면 효과 없음, 문턱 제거 시 성능 상실",
                "explanation": "사용 방법과 유지관리가 성능에 직결됩니다."
            }
        ],
        "examples": [
            {
                "ko": "이 녹음실 방음문은 STC 48 등급으로, 60mm 두께의 다층 차음 구조와 자동 강하 씰이 적용되었습니다.",
                "vi": "Cửa cách âm phòng thu này cấp STC 48, áp dụng cấu trúc cách âm đa lớp dày 60mm và gioăng tự động hạ xuống.",
                "situation": "formal"
            },
            {
                "ko": "방음문 하부 씰이 손상되어 교체했고, 문틀 패킹도 전체적으로 점검했습니다.",
                "vi": "Đã thay gioăng dưới cửa cách âm do hư hỏng và kiểm tra toàn bộ gioăng khung cửa.",
                "situation": "onsite"
            },
            {
                "ko": "방음문 달았는데 문 밑에 틈 있으면 소용없어. 문턱 달아야 해.",
                "vi": "Lắp cửa cách âm rồi mà có khe dưới cửa thì vô ích. Phải lắp ngưỡng cửa.",
                "situation": "informal"
            }
        ],
        "relatedTerms": [
            "차음등급",
            "STC",
            "기밀패킹",
            "자동씰",
            "방음창"
        ]
    },
    {
        "slug": "san-kep",
        "korean": "이중바닥",
        "vietnamese": "Sàn kép",
        "hanja": "二重床",
        "hanjaReading": "두 이(二) + 무거울 중(重) + 마루 상(床)",
        "pronunciation": "이중바닥",
        "meaningKo": "구조 슬래브 위에 완충재나 공기층을 두고 그 위에 다시 마감 바닥을 시공하는 이중 구조로, 바닥충격음 저감과 배관/배선 공간 확보를 목적으로 하며, '뜬바닥', '부유바닥'이라고도 불립니다. 통역 시 주의할 점은 이중바닥에는 두 가지 방식이 있는데, 하나는 완충재(고무, 글라스울 등)를 깔고 경량기포 콘크리트 + 마감 몰탈을 타설하는 '습식 이중바닥'이고, 다른 하나는 지지대(pedestal)를 설치하고 그 위에 패널을 얹는 '건식 이중바닥(raised floor)'입니다. 한국 공동주택에서는 습식 이중바닥이 표준이며, 완충재 두께 20~30mm, 경량기포 콘크리트 40~50mm, 마감 몰탈 40~50mm로 총 100~130mm의 마감 두께를 가집니다. 이중바닥은 바닥충격음(특히 경량충격음) 저감에 매우 효과적이지만, 시공 품질(완충재 이음부 처리, 기포콘크리트 양생)이 중요하며, 불량 시 소음 저감 효과가 크게 떨어집니다. 통역 시 이중바닥 시공 후 양생 기간(최소 7일)과 하중 제한을 명확히 전달해야 합니다.",
        "meaningVi": "Sàn kép (이중바닥) là kết cấu hai lớp: trên sàn bê tông kết cấu đặt vật liệu đệm hoặc khoảng không khí, rồi thi công lớp sàn hoàn thiện phía trên, nhằm giảm âm va chạm sàn và tạo không gian cho đường ống/dây điện, còn gọi là 'sàn nổi', 'sàn treo'. Có hai phương pháp: một là 'sàn kép ướt' - trải vật liệu đệm (cao su, bông thủy tinh...) rồi đổ bê tông bọt nhẹ + vữa hoàn thiện, hai là 'sàn kép khô (raised floor)' - lắp giá đỡ (pedestal) rồi đặt tấm panel lên trên. Tại chung cư Hàn Quốc, sàn kép ướt là tiêu chuẩn với độ dày: vật liệu đệm 20~30mm, bê tông bọt nhẹ 40~50mm, vữa hoàn thiện 40~50mm, tổng 100~130mm. Sàn kép rất hiệu quả giảm âm va chạm (đặc biệt âm va chạm nhẹ), nhưng chất lượng thi công (xử lý mối nối vật liệu đệm, dưỡng hộ bê tông bọt) rất quan trọng, nếu kém thì hiệu quả giảm tiếng ồn giảm mạnh. Khi phiên dịch, phải nói rõ thời gian dưỡng hộ sau thi công sàn kép (tối thiểu 7 ngày) và giới hạn tải trọng.",
        "context": "공동주택 바닥 시공, 사무실 OA 플로어, 데이터센터 바닥",
        "culturalNote": "한국에서는 2000년대 중반 이후 바닥충격음 규제가 강화되면서 이중바닥이 공동주택의 표준 시공법이 되었고, 현재는 거의 모든 아파트가 이중바닥 구조를 채택하고 있습니다. 완충재는 초기에는 고무 패드, 펠트를 사용했으나 최근에는 글라스울, 암면, 폴리에스터 등 다양한 고성능 완충재가 사용됩니다. 경량기포 콘크리트는 일반 콘크리트보다 가벼워 건물 하중을 줄이면서도 충격음 저감 효과가 있어 필수적으로 사용됩니다. 시공 시 주의할 점은 완충재 이음부를 테이프로 완전히 밀봉해야 하고, 슬래브와 벽체 접합부에는 완충재를 수직으로 세워 측면 전달음을 차단해야 합니다. 베트남에서는 이중바닥 개념이 생소하여 단순히 '바닥을 두 번 친다'로 오해할 수 있으므로, 통역 시 완충재의 역할, 경량기포 콘크리트의 특성, 이음부 처리의 중요성을 구체적으로 설명해야 합니다.",
        "commonMistakes": [
            {
                "mistake": "습식/건식 이중바닥을 구분하지 않고 통역",
                "correction": "'sàn kép ướt'와 'sàn kép khô'로 명확히 구분",
                "explanation": "구조와 용도가 완전히 다르므로 구분 필수입니다."
            },
            {
                "mistake": "완충재 이음부 처리 중요성 미전달",
                "correction": "이음부 밀봉 불량 시 소음 저감 효과 상실",
                "explanation": "작은 틈새도 소음 전달 경로가 되어 성능이 떨어집니다."
            },
            {
                "mistake": "경량기포 콘크리트 양생 기간 설명 누락",
                "correction": "최소 7일 양생 및 조기 하중 금지 명시",
                "explanation": "양생 불충분 시 강도 부족과 균열이 발생합니다."
            }
        ],
        "examples": [
            {
                "ko": "이중바닥 시공 순서는 슬래브 청소, 완충재 깔기, 이음부 밀봉, 경량기포 콘크리트 타설, 양생, 마감 몰탈 순입니다.",
                "vi": "Trình tự thi công sàn kép: lau sàn bê tông, trải vật liệu đệm, kín mối nối, đổ bê tông bọt nhẹ, dưỡng hộ, vữa hoàn thiện.",
                "situation": "onsite"
            },
            {
                "ko": "이 현장은 완충재 30mm + 경량기포 50mm + 마감 몰탈 50mm의 이중바닥으로 중량충격음 47dB을 달성했습니다.",
                "vi": "Hiện trường này đạt âm va chạm nặng 47dB với sàn kép: đệm 30mm + bê tông bọt 50mm + vữa hoàn thiện 50mm.",
                "situation": "formal"
            },
            {
                "ko": "이중바닥 시공 중이니까 일주일 동안 위로 올라가지 마.",
                "vi": "Đang thi công sàn kép nên một tuần không được lên trên.",
                "situation": "informal"
            }
        ],
        "relatedTerms": [
            "뜬바닥",
            "완충재",
            "경량기포콘크리트",
            "바닥충격음",
            "raised floor"
        ]
    },
    {
        "slug": "tuong-kep",
        "korean": "이중벽",
        "vietnamese": "Tường kép",
        "hanja": "二重壁",
        "hanjaReading": "두 이(二) + 무거울 중(重) + 벽 벽(壁)",
        "pronunciation": "이중벽",
        "meaningKo": "두 개의 벽체 사이에 공기층이나 흡음재를 두고 시공하는 차음 벽체 구조로, 단일 벽보다 훨씬 우수한 차음 성능을 제공하며, 녹음실, 호텔, 병원 등에서 필수적으로 사용됩니다. 통역 시 주의할 점은 이중벽의 차음 원리는 두 벽 사이의 공기층이 음파를 감쇠시키고, 두 벽이 구조적으로 분리되어 진동 전달을 차단하는 것이며, 단순히 벽을 두 번 쌓는 것과는 다릅니다. 한국 건축에서는 일반적으로 100mm 콘크리트 벽 + 50~100mm 공기층 + 100mm 경량벽체(스터드 + 석고보드) 구조를 사용하며, 공기층에 흡음재(글라스울, 암면)를 충전하면 차음 성능이 더욱 향상됩니다(STC 55~65). 이중벽 시공 시 주의할 점은 두 벽이 천장이나 바닥, 측벽에서 구조적으로 연결되면 '음향 단락(sound bridge)'이 발생하여 차음 성능이 크게 저하되므로, 완전히 분리되도록 시공해야 합니다. 통역 시 이중벽은 공간을 많이 차지하므로 설계 단계에서 평면 계획에 반영해야 한다는 점을 강조해야 합니다.",
        "meaningVi": "Tường kép (이중벽) là kết cấu tường cách âm với hai lớp tường có khoảng không khí hoặc vật liệu hấp thụ âm ở giữa, cung cấp hiệu năng cách âm vượt trội hơn tường đơn, là thiết bị bắt buộc tại phòng thu, khách sạn, bệnh viện. Nguyên lý cách âm của tường kép: khoảng không khí giữa hai tường làm suy giảm sóng âm, hai tường tách rời về mặt kết cấu để ngăn truyền rung động, khác với việc đơn giản xây tường hai lần. Trong xây dựng Hàn Quốc, thường dùng cấu trúc: tường bê tông 100mm + khoảng không khí 50~100mm + tường nhẹ 100mm (khung + tấm thạch cao), nếu lấp đầy khoảng không khí bằng vật liệu hấp âm (bông thủy tinh, bông khoáng) thì hiệu năng cách âm tăng hơn (STC 55~65). Khi thi công tường kép, cần lưu ý nếu hai tường kết nối về mặt kết cấu tại trần, sàn, tường bên thì xảy ra 'cầu âm thanh (sound bridge)' làm hiệu năng cách âm giảm mạnh, phải thi công hoàn toàn tách rời. Khi phiên dịch, cần nhấn mạnh tường kép chiếm nhiều diện tích nên phải phản ánh vào kế hoạch mặt bằng từ giai đoạn thiết kế.",
        "context": "녹음실/방송국 설계, 호텔 객실 간 벽체, 병원 진료실 차음",
        "culturalNote": "한국의 고급 건축물에서는 프라이버시와 음향 품질을 위해 이중벽이 필수적으로 사용되며, 특히 호텔 객실 간 벽체는 STC 55 이상을 요구하므로 이중벽 구조가 표준입니다. 녹음실과 방송국은 외부 소음 차단과 내부 음향 제어를 위해 이중벽뿐 아니라 이중 천장, 이중 바닥까지 적용한 '박스 인 박스(box in box)' 구조를 사용합니다. 이중벽 시공에서 가장 중요한 것은 '음향 단락' 방지인데, 전기 배선이나 배관이 두 벽을 관통하거나, 천장 석고보드가 두 벽에 걸쳐 시공되면 진동이 전달되어 차음 효과가 사라집니다. 베트남에서는 이중벽 개념이 생소하고 공간 손실과 비용 증가를 우려하여 단일 벽을 선호하므로, 통역 시 이중벽의 차음 원리, STC 성능 차이(단일벽 STC 40 vs 이중벽 STC 60), 음향 단락 방지의 중요성을 구체적으로 설명하고, 공간 손실보다 음향 품질이 더 중요한 용도임을 강조해야 합니다.",
        "commonMistakes": [
            {
                "mistake": "이중벽을 단순히 '벽 두 번 쌓기'로 설명",
                "correction": "구조적으로 분리된 두 벽 + 공기층 구조로 설명",
                "explanation": "분리와 공기층이 핵심이지 단순 두께가 아닙니다."
            },
            {
                "mistake": "음향 단락(sound bridge) 개념 미전달",
                "correction": "두 벽 연결 시 진동 전달로 성능 상실",
                "explanation": "음향 단락 방지가 이중벽 시공의 핵심입니다."
            },
            {
                "mistake": "공간 손실 및 설계 단계 반영 필요성 누락",
                "correction": "이중벽은 100~200mm 공간 차지, 평면 설계 시 고려",
                "explanation": "시공 단계에서 공간 부족으로 변경 불가능합니다."
            }
        ],
        "examples": [
            {
                "ko": "이 녹음실은 200mm 콘크리트 벽 + 100mm 공기층(글라스울 충전) + 100mm 스터드벽으로 STC 62를 달성했습니다.",
                "vi": "Phòng thu này đạt STC 62 với tường bê tông 200mm + khoảng không khí 100mm (lấp bông thủy tinh) + tường khung 100mm.",
                "situation": "formal"
            },
            {
                "ko": "이중벽 시공 시 전기 박스는 두 벽에 각각 별도로 설치하고, 절대 관통하지 마십시오.",
                "vi": "Khi thi công tường kép, hộp điện phải lắp riêng biệt trên từng tường, tuyệt đối không xuyên qua.",
                "situation": "onsite"
            },
            {
                "ko": "이중벽 하니까 공간이 좁아지네. 차라리 두꺼운 벽 하나 치지.",
                "vi": "Làm tường kép thì không gian hẹp. Thà xây một tường dày.",
                "situation": "informal"
            }
        ],
        "relatedTerms": [
            "차음",
            "차음등급",
            "음향단락",
            "박스인박스",
            "STC"
        ]
    },
    {
        "slug": "hap-thu-am-cong-huong",
        "korean": "공명흡음",
        "vietnamese": "Hấp thụ âm cộng hưởng",
        "hanja": "共鳴吸音",
        "hanjaReading": "한가지 공(共) + 울릴 명(鳴) + 빨아들일 흡(吸) + 소리 음(音)",
        "pronunciation": "공명흡음",
        "meaningKo": "공기층과 개구부(구멍)를 가진 구조물이 특정 주파수에서 공명(resonance)하여 음파 에너지를 열에너지로 변환시켜 흡수하는 흡음 방식으로, 주로 저주파 소음 제어에 효과적이며 헬름홀츠 공명기(Helmholtz resonator) 원리를 응용합니다. 통역 시 주의할 점은 일반 다공성 흡음재(글라스울, 암면)는 고주파 흡음에 유리하지만 저주파(125~250Hz)에는 효과가 적은 반면, 공명흡음 구조는 설계 주파수(보통 125~500Hz)에서 높은 흡음 성능을 발휘합니다. 한국 건축음향 설계에서는 강당, 체육관, 지하철역 등 저주파 소음이 문제가 되는 공간에 공명흡음 패널을 사용하며, 대표적으로 유공판(천공률 5~30%) + 공기층(50~200mm) 구조를 채택합니다. 공명 주파수는 구멍 크기, 개구율, 공기층 두께로 조절되며, 정확한 설계를 위해서는 음향 시뮬레이션이 필요합니다. 통역 시 공명흡음은 특정 주파수 대역에만 효과적이므로 광대역 흡음을 위해서는 일반 흡음재와 병행해야 한다는 점을 강조해야 합니다.",
        "meaningVi": "Hấp thụ âm cộng hưởng (공명흡음) là phương pháp hấp thụ âm bằng cách kết cấu có khoảng không khí và lỗ mở cộng hưởng (resonance) tại tần số đặc biệt, chuyển đổi năng lượng sóng âm thành nhiệt năng, chủ yếu hiệu quả với tiếng ồn tần số thấp, ứng dụng nguyên lý bộ cộng hưởng Helmholtz. Vật liệu hấp thụ âm xốp thông thường (bông thủy tinh, bông khoáng) có lợi cho hấp thụ tần số cao nhưng ít hiệu quả với tần số thấp (125~250Hz), trong khi cấu trúc hấp thụ âm cộng hưởng phát huy hiệu năng hấp thụ cao tại tần số thiết kế (thường 125~500Hz). Trong thiết kế âm thanh kiến trúc Hàn Quốc, sử dụng tấm hấp thụ âm cộng hưởng tại hội trường, nhà thi đấu, ga tàu điện ngầm nơi có vấn đề tiếng ồn tần số thấp, điển hình là cấu trúc tấm đục lỗ (tỷ lệ lỗ 5~30%) + khoảng không khí (50~200mm). Tần số cộng hưởng điều chỉnh bằng kích thước lỗ, tỷ lệ lỗ mở, độ dày khoảng không khí, cần mô phỏng âm thanh để thiết kế chính xác. Khi phiên dịch, cần nhấn mạnh hấp thụ âm cộng hưởng chỉ hiệu quả với dải tần số nhất định nên để hấp thụ âm băng rộng phải kết hợp với vật liệu hấp thụ âm thông thường.",
        "context": "강당/체육관 음향 설계, 지하철역/터널 소음 제어, 공장 저주파 소음",
        "culturalNote": "한국에서는 1990년대 이후 대형 공공건물과 지하철역에 공명흡음 구조가 본격적으로 도입되었고, 최근에는 디자인과 흡음 성능을 결합한 목재 유공판(wooden perforated panel)과 알루미늄 유공판이 인테리어 마감재로 인기를 얻고 있습니다. 특히 공연장과 강당에서는 무대 뒤쪽 저음 증폭을 제어하기 위해 공명흡음 패널을 설치하며, 주파수별 흡음 특성을 정밀하게 설계합니다. 공명흡음 구조는 설계가 복잡하고 제작 비용이 높지만, 저주파 제어에는 다른 방법이 없어 고급 건축물에서 필수적으로 사용됩니다. 베트남에서는 공명흡음 개념이 생소하여 단순히 '구멍 뚫린 판'으로 인식할 수 있으므로, 통역 시 공명 원리(특정 주파수에서 진동), 저주파 흡음의 중요성(저음은 일반 흡음재로 제어 불가), 설계 변수(구멍 크기, 공기층 두께)를 구체적으로 설명하고, 음향 전문가의 설계가 필수임을 강조해야 합니다.",
        "commonMistakes": [
            {
                "mistake": "공명흡음을 일반 흡음재와 동일하게 설명",
                "correction": "공명흡음은 저주파 전용, 일반 흡음재는 고주파 전용",
                "explanation": "주파수 대역과 흡음 원리가 완전히 다릅니다."
            },
            {
                "mistake": "유공판만 달면 흡음된다고 설명",
                "correction": "뒷면 공기층 두께와 구멍 크기가 설계되어야 함",
                "explanation": "단순 구멍만으로는 공명 효과가 없습니다."
            },
            {
                "mistake": "공명 주파수 설계의 중요성 미전달",
                "correction": "설계 주파수 외에는 효과 적어 음향 설계 필수",
                "explanation": "임의 시공 시 효과가 없거나 미미합니다."
            }
        ],
        "examples": [
            {
                "ko": "이 강당은 200Hz 저음 제어를 위해 직경 10mm, 개구율 15%, 공기층 100mm의 공명흡음 패널을 설치했습니다.",
                "vi": "Hội trường này lắp tấm hấp thụ âm cộng hưởng: đường kính lỗ 10mm, tỷ lệ mở 15%, khoảng không khí 100mm để điều khiển âm trầm 200Hz.",
                "situation": "formal"
            },
            {
                "ko": "지하철역 소음 중 250Hz 이하 저주파가 문제여서 공명흡음 구조를 천장에 적용했습니다.",
                "vi": "Tần số thấp dưới 250Hz là vấn đề trong tiếng ồn ga tàu điện ngầm nên áp dụng cấu trúc hấp thụ âm cộng hưởng lên trần.",
                "situation": "formal"
            },
            {
                "ko": "공명흡음 판 달았는데 고음은 그대로네. 저음만 줄어들어.",
                "vi": "Lắp tấm hấp âm cộng hưởng mà âm cao vẫn vậy. Chỉ âm trầm giảm.",
                "situation": "informal"
            }
        ],
        "relatedTerms": [
            "흡음계수",
            "저주파",
            "헬름홀츠공명기",
            "유공판",
            "공기층"
        ]
    },
    {
        "slug": "tieu-chuan-tieng-on",
        "korean": "소음기준",
        "vietnamese": "Tiêu chuẩn tiếng ồn",
        "hanja": "騷音基準",
        "hanjaReading": "시끄러울 소(騷) + 소리 음(音) + 터 기(基) + 기준 준(準)",
        "pronunciation": "소음기준",
        "meaningKo": "건축물의 용도와 구역에 따라 허용되는 소음의 최대 수준을 규정한 법적 기준으로, 한국에서는 「환경정책기본법」, 「소음·진동관리법」, 「주택건설기준 등에 관한 규정」 등에서 상세히 규정하고 있습니다. 통역 시 주의할 점은 소음기준에는 크게 세 가지가 있는데, 첫째는 '환경소음 기준'(도로, 철도, 항공기 등 외부 소음, 주간 55~70dB, 야간 45~65dB), 둘째는 '건물 내부 소음기준'(학교, 병원, 주택 등 실내 허용 소음, 30~50dB), 셋째는 '층간소음 기준'(공동주택 바닥충격음, 경량 58dB, 중량 50dB)이며, 각각 측정 방법과 기준값이 다릅니다. 한국 건축 설계에서는 외부 소음원(도로, 철도) 인근 건물은 외벽 차음 설계와 환기 시스템(소음 차단형 환기구)을 적용해야 하고, 공동주택은 바닥충격음 기준을 만족해야 입주가 가능합니다. 통역 시 소음기준 초과는 법적 처벌(과태료, 공사 중지) 대상이며, 주민 민원과 소송으로 이어질 수 있다는 점을 강조해야 합니다.",
        "meaningVi": "Tiêu chuẩn tiếng ồn (소음기준) là tiêu chuẩn pháp lý quy định mức tiếng ồn tối đa cho phép theo mục đích sử dụng và khu vực của công trình, tại Hàn Quốc được quy định chi tiết trong 「Luật Chính sách Môi trường cơ bản」, 「Luật Quản lý Tiếng ồn và Rung động」, 「Quy định Tiêu chuẩn Xây dựng Nhà ở」. Có ba loại tiêu chuẩn tiếng ồn: một là 'tiêu chuẩn tiếng ồn môi trường' (tiếng ồn ngoài từ đường, đường sắt, máy bay, ban ngày 55~70dB, ban đêm 45~65dB), hai là 'tiêu chuẩn tiếng ồn bên trong tòa nhà' (tiếng ồn cho phép trong phòng trường học, bệnh viện, nhà ở, 30~50dB), ba là 'tiêu chuẩn tiếng ồn tầng' (âm va chạm sàn chung cư, nhẹ 58dB, nặng 50dB), mỗi loại có phương pháp đo và giá trị chuẩn khác nhau. Trong thiết kế kiến trúc Hàn Quốc, công trình gần nguồn ồn ngoài (đường, đường sắt) phải áp dụng thiết kế cách âm tường ngoài và hệ thống thông gió (cửa gió chống ồn), chung cư phải đạt tiêu chuẩn âm va chạm sàn mới được cho nhập cư. Khi phiên dịch, cần nhấn mạnh vượt tiêu chuẩn tiếng ồn bị xử phạt pháp luật (phạt tiền, đình chỉ công trình), có thể dẫn đến khiếu nại dân cư và kiện tụng.",
        "context": "건축 설계 소음 평가, 공사장 소음 관리, 공동주택 입주 전 검사",
        "culturalNote": "한국은 세계에서 가장 엄격한 소음 규제 국가 중 하나로, 특히 공동주택 밀집 지역에서 소음 민원이 매우 빈번합니다. 환경소음 기준은 지역별로 차등 적용되는데, 주거 지역은 가장 엄격하고(주간 55dB, 야간 45dB), 상업 지역은 상대적으로 완화됩니다(주간 70dB, 야간 60dB). 건물 내부 소음기준은 용도별로 다르며, 학교 교실 40dB, 병원 병실 35dB, 호텔 객실 40dB, 주택 거실 45dB 등으로 규정되어 있습니다. 2013년 이후 층간소음 기준이 법제화되면서 공동주택 시공사는 준공 전 반드시 바닥충격음 성능 인증을 받아야 하며, 미달 시 입주가 불가능합니다. 최근에는 생활소음(악기 연주, 반려동물, 청소기) 민원도 증가하여 공동주택 관리 규약에 '소음 금지 시간대'를 명시하는 경우가 많습니다. 베트남에서는 소음 규제가 상대적으로 느슨하고 단속도 드물므로, 통역 시 한국의 엄격한 소음기준, 측정 방법, 법적 처벌, 주민 민원의 심각성을 구체적으로 설명해야 합니다.",
        "commonMistakes": [
            {
                "mistake": "환경소음, 실내소음, 층간소음을 구분하지 않고 통역",
                "correction": "세 가지 소음기준을 각각 명시하고 기준값 구분",
                "explanation": "각각 다른 법령과 기준을 적용하므로 구분 필수입니다."
            },
            {
                "mistake": "주간/야간 기준 차이 설명 누락",
                "correction": "야간(22:00~07:00) 기준이 주간보다 10dB 낮음",
                "explanation": "야간 소음은 더 엄격하게 규제됩니다."
            },
            {
                "mistake": "기준 초과 시 법적 결과(처벌, 공사 중지) 미전달",
                "correction": "과태료, 공사 중지 명령, 민사 소송 가능성 명시",
                "explanation": "법적 책임이 크므로 반드시 전달해야 합니다."
            }
        ],
        "examples": [
            {
                "ko": "이 부지는 간선도로에서 50m 이내이므로 외벽 차음 설계를 통해 실내소음기준 45dB 이하를 만족해야 합니다.",
                "vi": "Lô đất này trong phạm vi 50m từ đường chính nên phải đạt tiêu chuẩn tiếng ồn trong phòng ≤45dB thông qua thiết kế cách âm tường ngoài.",
                "situation": "formal"
            },
            {
                "ko": "공사장 소음측정 결과 주간 75dB로 기준(70dB)을 5dB 초과하여 방음 펜스 추가 설치가 필요합니다.",
                "vi": "Kết quả đo tiếng ồn công trường ban ngày 75dB, vượt chuẩn (70dB) 5dB, cần lắp thêm hàng rào cách âm.",
                "situation": "onsite"
            },
            {
                "ko": "밤 11시에 시끄럽게 하면 소음기준 위반이야. 민원 들어오면 큰일 나.",
                "vi": "Làm ồn lúc 11 giờ đêm là vi phạm tiêu chuẩn tiếng ồn. Nếu có khiếu nại thì to chuyện.",
                "situation": "informal"
            }
        ],
        "relatedTerms": [
            "환경소음",
            "층간소음",
            "바닥충격음",
            "차음",
            "소음측정"
        ]
    }
]

# 파일 경로 설정
file_path = os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', 'data', 'terms', 'construction.json')

# 기존 파일 읽기
with open(file_path, 'r', encoding='utf-8') as f:
    existing_data = json.load(f)

# 새 용어 추가
existing_data.extend(data)

# 파일 저장
with open(file_path, 'w', encoding='utf-8') as f:
    json.dump(existing_data, f, ensure_ascii=False, indent=2)

print(f"✅ {len(data)}개 용어가 {file_path}에 추가되었습니다.")
print("추가된 용어:", [term['korean'] for term in data])
