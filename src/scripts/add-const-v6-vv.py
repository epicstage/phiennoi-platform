#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
건설(Construction) 용어 추가 스크립트 - 바닥/미장공사 테마
테마: 셀프레벨링, 미장, 뿜칠, 기계미장, 바닥레벨, 수평, 레벨기포, 방통, 온돌, 충전재
"""

import json
import os

# 추가할 10개 용어 (Tier S 기준)
new_terms = [
    {
        "slug": "san-tu-san-phang",
        "korean": "셀프레벨링",
        "vietnamese": "Sàn tự san phẳng",
        "hanja": None,
        "hanjaReading": None,
        "pronunciation": "셀프레벨링",
        "meaningKo": "자동으로 수평을 잡아주는 바닥 마감재로, 시멘트 기반의 유동성 높은 몰탈을 바닥에 부어 중력에 의해 스스로 평탄하게 펴지는 공법입니다. 통역 시 '자기평활성 몰탈'과 혼용되므로 맥락 확인이 중요하며, 베트남 현장에서는 시공 속도와 평탄도를 강조할 때 사용됩니다. 건조 시간(thời gian khô)과 보행 가능 시간(thời gian có thể đi lại)을 명확히 구분해야 합니다.",
        "meaningVi": "Vật liệu hoàn thiện sàn tự động san bằng, được làm từ vữa xi măng có tính chất lỏng cao, đổ lên sàn và tự động lan phẳng nhờ trọng lực. Thường dùng khi cần độ phẳng cao và thi công nhanh.",
        "context": "바닥공사, 평탄도 확보, 마감 전 처리",
        "culturalNote": "한국에서는 바닥난방(온돌) 위에 셀프레벨링 시공이 일반적이나, 베트남에서는 타일 직접 시공이 많아 셀프레벨링 필요성을 설명해야 할 수 있습니다. 한국 현장은 ±2mm 이내 평탄도를 요구하지만 베트남은 ±3~5mm도 허용하는 경우가 많아 품질 기준 통역 시 주의가 필요합니다.",
        "commonMistakes": [
            {
                "mistake": "Self-leveling을 '자동 레벨링'으로 직역",
                "correction": "셀프레벨링 또는 자기평활성 몰탈",
                "explanation": "고유명사처럼 굳어진 용어이므로 원어 그대로 사용하는 것이 현장에서 통용됨"
            },
            {
                "mistake": "Sàn tự động을 '자동 바닥'으로 역번역",
                "correction": "Sàn tự san phẳng (자기평활 바닥)",
                "explanation": "tự động(자동)이 아닌 tự san phẳng(스스로 평평해지는)이 정확한 표현"
            },
            {
                "mistake": "건조시간을 '마르는 시간'으로 통역",
                "correction": "thời gian khô hoàn toàn (완전 건조 시간) vs thời gian có thể thi công tiếp (후속 공정 가능 시간)",
                "explanation": "표면 건조와 완전 건조, 보행 가능 시점을 구분해야 공정 관리 오류 방지"
            }
        ],
        "examples": [
            {
                "ko": "셀프레벨링 시공 후 24시간 양생이 필요합니다",
                "vi": "Sau khi thi công sàn tự san phẳng cần bảo dưỡng 24 giờ",
                "situation": "formal"
            },
            {
                "ko": "레벨링 두께가 3mm 이하면 균열 위험이 있어요",
                "vi": "Nếu độ dày lớp san phẳng dưới 3mm có nguy cơ nứt vỡ",
                "situation": "onsite"
            },
            {
                "ko": "셀프레벨링 전에 프라이머 도포는 필수입니다",
                "vi": "Trước khi thi công sàn tự san phẳng bắt buộc phải quét lớp primer",
                "situation": "formal"
            }
        ],
        "relatedTerms": ["미장", "평탄도", "몰탈", "바닥공사", "양생"]
    },
    {
        "slug": "mi-truot",
        "korean": "미장",
        "vietnamese": "Mí trượt",
        "hanja": "美粧",
        "hanjaReading": "아름다울 미(美) + 꾸밀 장(粧)",
        "pronunciation": "미장",
        "meaningKo": "벽이나 천장 표면을 평평하고 매끄럽게 마감하는 작업으로, 석고나 시멘트 몰탈을 바르는 공정입니다. 통역 시 '바름', '회반죽', '플라스터링'과 혼용되므로 주의가 필요하며, 한국은 주로 기계미장이나 뿜칠미장을 많이 사용하지만 베트남은 수작업 미장(mí trượt thủ công)이 여전히 많습니다. 두께(độ dày), 평활도(độ phẳng), 마감등급(cấp độ hoàn thiện)을 명확히 구분해야 합니다.",
        "meaningVi": "Công việc hoàn thiện bề mặt tường hoặc trần bằng cách trét vữa thạch cao hoặc xi măng để tạo bề mặt phẳng và nhẵn. Là công đoạn quan trọng trước khi sơn hoặc dán giấy dán tường.",
        "context": "벽체공사, 마감공사, 내장공사",
        "culturalNote": "한국에서는 '미장'이 표준 용어이나 베트남에서는 'mí trượt', 'trét tường', 'trát tường' 등 지역마다 다른 표현을 쓰므로 통역 시 확인이 필요합니다. 한국은 두께 10~15mm가 표준이나 베트nam은 5~10mm로 더 얇게 시공하는 경향이 있어 품질 기준 통역 시 오해 소지가 있습니다.",
        "commonMistakes": [
            {
                "mistake": "Mí trượt을 '눈꺼풀'로 오역",
                "correction": "미장 (벽 마감 작업)",
                "explanation": "mí는 베트남어로 눈꺼풀 의미도 있으나 건설 용어로는 미장을 뜻하는 고유 표현"
            },
            {
                "mistake": "'바르다'를 trát으로만 번역",
                "correction": "mí trượt (미장) / trét vữa (몰탈 바르기) / quét (칠하기) 구분",
                "explanation": "바르는 재료와 방식에 따라 다른 동사를 사용해야 정확함"
            },
            {
                "mistake": "초벌미장을 '첫 번째 미장'으로 직역",
                "correction": "lớp mí lót (바탕 미장) 또는 lớp thô (초벌층)",
                "explanation": "공정 순서가 아닌 역할을 표현하는 것이 현장에서 명확함"
            }
        ],
        "examples": [
            {
                "ko": "미장 작업 전에 벽면의 먼지를 제거하세요",
                "vi": "Trước khi mí trượt cần loại bỏ bụi bẩn trên bề mặt tường",
                "situation": "onsite"
            },
            {
                "ko": "이 구역은 고급 미장 마감이 필요합니다",
                "vi": "Khu vực này cần hoàn thiện mí trượt cấp cao",
                "situation": "formal"
            },
            {
                "ko": "미장 두께가 불균일하면 재시공 해야 해요",
                "vi": "Nếu độ dày lớp mí không đều phải thi công lại",
                "situation": "onsite"
            }
        ],
        "relatedTerms": ["뿜칠", "평활도", "초벌", "재벌", "몰탈"]
    },
    {
        "slug": "phun-vua",
        "korean": "뿜칠",
        "vietnamese": "Phun vữa",
        "hanja": None,
        "hanjaReading": None,
        "pronunciation": "뿜칠",
        "meaningKo": "압축공기를 이용해 몰탈이나 콘크리트를 고압으로 분사하여 벽이나 천장에 부착시키는 공법입니다. 통역 시 '숏크리트(shotcrete)', '취부공법'과 혼용되므로 주의가 필요하며, 터널이나 지하 공사에서는 구조적 기능을, 마감공사에서는 속도와 평활도를 강조합니다. 베트남에서는 분사 압력(áp lực phun), 반발률(tỷ lệ bật ra), 부착력(độ bám dính)을 중요 품질 지표로 봅니다.",
        "meaningVi": "Công pháp sử dụng khí nén để phun vữa hoặc bê tông áp lực cao lên tường hoặc trần. Thường dùng trong công trình hầm, ngầm hoặc để tăng tốc độ thi công hoàn thiện.",
        "context": "마감공사, 터널공사, 보강공사",
        "culturalNote": "한국에서는 뿜칠미장이 일반 주거 건축에서도 많이 사용되나, 베트남에서는 주로 대형 공사나 터널에서만 쓰이고 주거 건축은 여전히 수작업 미장이 많습니다. 한국 현장에서 '뿜칠'은 마감 개념이 강하나 베트남에서는 '구조 보강' 개념으로 인식하는 경우가 많아 용도 설명이 필요합니다.",
        "commonMistakes": [
            {
                "mistake": "Phun vữa를 '몰탈 뿌리기'로 직역",
                "correction": "뿜칠 또는 숏크리트 공법",
                "explanation": "'뿌리다'는 단순 살포를 의미하나 뿜칠은 고압 분사로 부착시키는 기술적 공법"
            },
            {
                "mistake": "습식뿜칠과 건식뿜칠을 구분하지 않음",
                "correction": "phun ướt (습식) vs phun khô (건식) 명확히 구분",
                "explanation": "물 첨가 시점과 장비가 달라 공법 선택 시 중요한 구분"
            },
            {
                "mistake": "Shotcrete를 '쇼트크리트'로만 음차",
                "correction": "숏크리트 (뿜칠 콘크리트)",
                "explanation": "한국어 표기는 '숏크리트'가 표준이며 뿜칠과 병기하는 것이 명확함"
            }
        ],
        "examples": [
            {
                "ko": "이번 구간은 습식 뿜칠로 진행합니다",
                "vi": "Đoạn này tiến hành phun vữa ướt",
                "situation": "onsite"
            },
            {
                "ko": "뿜칠 후 반발률이 15%를 초과하면 재시공입니다",
                "vi": "Sau khi phun vữa nếu tỷ lệ bật ra vượt quá 15% phải thi công lại",
                "situation": "formal"
            },
            {
                "ko": "천장 뿜칠은 두께 관리가 어려워요",
                "vi": "Phun vữa trần khó kiểm soát độ dày",
                "situation": "onsite"
            }
        ],
        "relatedTerms": ["숏크리트", "미장", "압송", "몰탈", "반발률"]
    },
    {
        "slug": "mi-bang-may",
        "korean": "기계미장",
        "vietnamese": "Mí bằng máy",
        "hanja": "機械美粧",
        "hanjaReading": "기계 기(機) + 틀 계(械) + 아름다울 미(美) + 꾸밀 장(粧)",
        "pronunciation": "기계미장",
        "meaningKo": "펌프와 호스를 이용해 몰탈을 벽면에 분사하고 기계로 평탄하게 고르는 미장 공법입니다. 통역 시 수작업 미장(mí thủ công)과 명확히 구분해야 하며, 시공 속도, 평활도, 인건비 절감을 주요 장점으로 설명합니다. 베트남 현장에서는 장비 임대료(chi phí thuê máy)와 숙련공 필요성(yêu cầu thợ có tay nghề)을 함께 고려해야 합니다.",
        "meaningVi": "Công pháp mí trượt sử dụng máy bơm và vòi phun để phun vữa lên tường, sau đó dùng máy làm phẳng. Giúp tăng tốc độ thi công và đảm bảo độ phẳng đồng đều.",
        "context": "내장공사, 대규모 마감공사, 공기 단축",
        "culturalNote": "한국에서는 기계미장이 표준이 된 지 오래지만, 베트남에서는 여전히 수작업 미장이 많아 기계미장의 효율성을 설명해야 할 때가 많습니다. 한국 현장은 인건비가 높아 기계미장이 경제적이나 베트남은 인건비가 낮아 소규모 공사에서는 수작업이 더 저렴할 수 있어 비용 비교 시 주의가 필요합니다.",
        "commonMistakes": [
            {
                "mistake": "Machine plastering을 '기계 플라스터'로 직역",
                "correction": "기계미장 또는 기계식 미장",
                "explanation": "한국 건설 용어로는 '기계미장'이 표준 용어"
            },
            {
                "mistake": "Mí bằng máy를 '기계로 된 미장'으로 오역",
                "correction": "기계로 시공하는 미장",
                "explanation": "bằng máy는 '기계를 사용하여'라는 방법을 나타냄"
            },
            {
                "mistake": "뿜칠과 기계미장을 같은 것으로 설명",
                "correction": "뿜칠은 고압 분사, 기계미장은 펌프 압송 + 기계 평탄",
                "explanation": "두 공법의 장비와 마감 방식이 다르므로 구분 필요"
            }
        ],
        "examples": [
            {
                "ko": "기계미장은 하루 100㎡ 이상 시공 가능합니다",
                "vi": "Mí bằng máy có thể thi công trên 100㎡ mỗi ngày",
                "situation": "formal"
            },
            {
                "ko": "기계미장기 호스가 막혔어요, 청소해야 해요",
                "vi": "Vòi máy mí bị tắc, cần phải vệ sinh",
                "situation": "onsite"
            },
            {
                "ko": "이 현장은 공기가 촉박해서 기계미장으로 진행합니다",
                "vi": "Công trường này tiến độ gấp nên tiến hành mí bằng máy",
                "situation": "onsite"
            }
        ],
        "relatedTerms": ["미장", "뿜칠", "평활도", "펌프", "압송"]
    },
    {
        "slug": "muc-san",
        "korean": "바닥레벨",
        "vietnamese": "Mức sàn",
        "hanja": None,
        "hanjaReading": None,
        "pronunciation": "바닥레벨",
        "meaningKo": "바닥의 높이 기준점으로, 건물 각 층의 마감 바닥면 높이를 의미합니다. 통역 시 층고(tầng cao), 구조체 레벨(cao độ kết cấu), 마감 레벨(cao độ hoàn thiện)을 명확히 구분해야 하며, 도면에서 FL(Finished Level)이나 ±0 기준을 설명할 때 자주 사용됩니다. 베트남 현장에서는 기준점(điểm chuẩn), 오차 허용범위(dung sai)를 함께 확인해야 합니다.",
        "meaningVi": "Điểm chuẩn độ cao của sàn, chỉ độ cao mặt sàn hoàn thiện của mỗi tầng trong công trình. Thường được ký hiệu là FL hoặc ±0 trong bản vẽ.",
        "context": "측량, 바닥공사, 도면 검토",
        "culturalNote": "한국 도면에서는 FL(Finished Level) 표기가 표준이나, 베트남 도면에서는 'Cao độ sàn' 또는 '+/- 0.00'으로 표기하는 경우가 많아 혼선이 있을 수 있습니다. 한국은 mm 단위까지 정밀하게 관리하나 베트남은 cm 단위로 관리하는 현장도 있어 정밀도 기준을 명확히 해야 합니다.",
        "commonMistakes": [
            {
                "mistake": "Floor level을 '바닥 수준'으로 직역",
                "correction": "바닥레벨 또는 바닥 기준높이",
                "explanation": "'레벨'은 건설 용어로 고유하게 사용되므로 그대로 쓰는 것이 명확함"
            },
            {
                "mistake": "Mức sàn을 '바닥 정도'로 오역",
                "correction": "바닥레벨 (바닥 높이 기준)",
                "explanation": "mức은 '수준, 레벨'을 의미하며 건설에서는 높이 기준을 뜻함"
            },
            {
                "mistake": "구조체 레벨과 마감 레벨을 구분하지 않음",
                "correction": "cao độ kết cấu (구조체 레벨) vs cao độ hoàn thiện (마감 레벨)",
                "explanation": "콘크리트 타설면과 마감 바닥면은 높이가 다르므로 명확히 구분 필요"
            }
        ],
        "examples": [
            {
                "ko": "1층 바닥레벨을 기준점으로 설정합니다",
                "vi": "Lấy mức sàn tầng 1 làm điểm chuẩn",
                "situation": "formal"
            },
            {
                "ko": "이 방 바닥레벨이 2cm 낮아요, 조정이 필요합니다",
                "vi": "Mức sàn phòng này thấp hơn 2cm, cần điều chỉnh",
                "situation": "onsite"
            },
            {
                "ko": "도면상 바닥레벨 FL+1.2m입니다",
                "vi": "Theo bản vẽ mức sàn là FL+1.2m",
                "situation": "formal"
            }
        ],
        "relatedTerms": ["수평", "레벨기", "측량", "기준점", "평탄도"]
    },
    {
        "slug": "thuy-binh",
        "korean": "수평",
        "vietnamese": "Thủy bình",
        "hanja": "水平",
        "hanjaReading": "물 수(水) + 평평할 평(平)",
        "pronunciation": "수평",
        "meaningKo": "바닥이나 구조물이 기울지 않고 수평선과 평행한 상태를 의미하며, 건설 현장에서는 수평 측정과 조정이 모든 공정의 기본입니다. 통역 시 수직(thẳng đứng), 평행(song song), 평탄(phẳng)과 명확히 구분해야 하며, 레벨기(máy thủy bình), 레이저레벨(máy cân mực laser)을 이용한 측정 방법을 함께 설명합니다. 허용 오차(sai số cho phép)는 공정마다 다르므로 기준을 명확히 해야 합니다.",
        "meaningVi": "Trạng thái song song với đường chân trời, không bị nghiêng. Trong xây dựng, việc đảm bảo thủy bình là cơ bản cho mọi công đoạn thi công.",
        "context": "측량, 품질관리, 모든 공정",
        "culturalNote": "한국 현장에서는 디지털 레벨기와 레이저 장비가 표준이나, 베트남 소규모 현장에서는 여전히 아날로그 수평기(thủy bình bọt khí)를 많이 사용합니다. 한국은 ±1mm 이내 정밀도를 요구하는 경우가 많으나 베트남은 ±3mm도 허용하는 현장이 있어 품질 기준 통역 시 주의가 필요합니다.",
        "commonMistakes": [
            {
                "mistake": "Horizontal을 '가로'로 번역",
                "correction": "수평 (기울지 않은 평평한 상태)",
                "explanation": "'가로'는 방향을 의미하나 '수평'은 기울기 없음을 의미"
            },
            {
                "mistake": "Thủy bình을 '물병'으로 오역",
                "correction": "수평 또는 레벨",
                "explanation": "thủy bình은 한자어 수평(水平)의 베트남어 음차로 건설 용어"
            },
            {
                "mistake": "'평평하다'와 '수평이다'를 혼용",
                "correction": "phẳng (평평함, 굴곡 없음) vs thủy bình (수평, 기울지 않음)",
                "explanation": "평평은 표면 상태, 수평은 기울기 상태로 다른 개념"
            }
        ],
        "examples": [
            {
                "ko": "레벨기로 바닥 수평을 확인하세요",
                "vi": "Dùng máy thủy bình kiểm tra mức độ thủy bình của sàn",
                "situation": "onsite"
            },
            {
                "ko": "이 보는 수평이 안 맞아서 조정이 필요합니다",
                "vi": "Dầm này không thủy bình cần điều chỉnh",
                "situation": "onsite"
            },
            {
                "ko": "수평 오차가 3mm 이내여야 합격입니다",
                "vi": "Sai số thủy bình phải trong phạm vi 3mm mới đạt",
                "situation": "formal"
            }
        ],
        "relatedTerms": ["수직", "레벨기", "측량", "평탄도", "기포"]
    },
    {
        "slug": "may-thuy-binh-bot-khi",
        "korean": "레벨기포",
        "vietnamese": "Máy thủy bình bọt khí",
        "hanja": None,
        "hanjaReading": None,
        "pronunciation": "레벨기포",
        "meaningKo": "수평을 측정하는 간단한 도구로, 투명한 액체가 든 관 안의 기포 위치로 수평 여부를 판단합니다. 통역 시 정밀 레벨기(máy thủy bình chính xác), 레이저레벨(máy cân mực laser)과 구분해야 하며, 현장에서는 '수평기', '수평자', '레벨'로도 불립니다. 기포가 중앙에 오면 수평, 좌우로 치우치면 기울어진 것을 의미하며, 정밀도는 ±0.5mm/m 수준입니다.",
        "meaningVi": "Dụng cụ đơn giản để đo thủy bình, sử dụng bọt khí trong ống chứa chất lỏng trong suốt để xác định độ nghiêng. Khi bọt khí ở chính giữa nghĩa là thủy bình.",
        "context": "간이측량, 소규모 공사, 수평 확인",
        "culturalNote": "한국 현장에서는 디지털 수평기나 레이저 레벨이 주류이나 여전히 기포 수평기를 보조 도구로 많이 사용합니다. 베트남 소규모 현장에서는 기포 수평기가 주요 측정 도구인 경우가 많아, 정밀 공사에서는 더 정확한 장비 사용을 권고해야 할 수 있습니다.",
        "commonMistakes": [
            {
                "mistake": "Spirit level을 '정신 수준'으로 직역",
                "correction": "수평기 또는 레벨기포",
                "explanation": "spirit은 알코올을 의미하며 기포관에 든 액체를 지칭"
            },
            {
                "mistake": "Bọt khí를 '거품'으로만 번역",
                "correction": "기포 (공기 방울)",
                "explanation": "건설 용어로는 '기포'가 정확하며 비누거품 등과 구분됨"
            },
            {
                "mistake": "'수평자'와 '수직자'를 혼동",
                "correction": "thước thủy bình (수평자) vs thước đứng (수직자/다림추)",
                "explanation": "측정 방향이 다른 별개의 도구"
            }
        ],
        "examples": [
            {
                "ko": "레벨기포로 대략적인 수평을 맞춰주세요",
                "vi": "Dùng máy thủy bình bọt khí chỉnh sơ bộ mức độ thủy bình",
                "situation": "onsite"
            },
            {
                "ko": "기포가 한쪽으로 치우쳐 있어요, 조정하세요",
                "vi": "Bọt khí lệch về một bên, điều chỉnh lại",
                "situation": "onsite"
            },
            {
                "ko": "정밀 측정은 레이저로, 간단한 확인은 기포 레벨로 합니다",
                "vi": "Đo chính xác dùng laser, kiểm tra đơn giản dùng thủy bình bọt khí",
                "situation": "formal"
            }
        ],
        "relatedTerms": ["수평", "레벨기", "레이저레벨", "측량", "기포"]
    },
    {
        "slug": "san-bang-thanh-chong",
        "korean": "방통",
        "vietnamese": "Sàn bằng thanh chống",
        "hanja": "防通",
        "hanjaReading": "막을 방(防) + 통할 통(通)",
        "pronunciation": "방통",
        "meaningKo": "나무 각재를 격자 형태로 설치하여 바닥 단열재나 배관을 지지하고 그 위에 마루판을 까는 전통적인 한국식 바닥 구조입니다. 통역 시 온돌(sàn nóng truyền thống), 장선(xà gồ), 멍에(thanh ngang) 개념을 함께 설명해야 하며, 현대에는 단열재와 함께 시공하여 바닥난방 효율을 높이는 용도로 많이 사용됩니다. 베트남에는 유사 개념이 없어 구조와 목적을 상세히 설명해야 합니다.",
        "meaningVi": "Kết cấu sàn truyền thống Hàn Quốc sử dụng thanh gỗ xếp theo hình lưới để đỡ vật liệu cách nhiệt hoặc đường ống, sau đó lát ván sàn lên trên. Giúp cách nhiệt và tạo khoảng trống cho hệ thống sưởi sàn.",
        "context": "바닥공사, 한옥, 온돌, 단열공사",
        "culturalNote": "방통은 한국 전통 건축 고유의 바닥 구조로, 베트남에는 이에 해당하는 개념이 없습니다. 베트남은 바닥을 직접 타일이나 시멘트로 마감하는 반면, 한국은 방통 위에 마루나 장판을 시공하는 이중 구조가 일반적이었습니다. 현대 건축에서는 온돌 배관과 단열재를 설치하는 공간으로 변형되어 사용되므로, 전통과 현대 용법을 모두 설명해야 할 수 있습니다.",
        "commonMistakes": [
            {
                "mistake": "防通을 '방수+통풍'으로 오역",
                "correction": "방통 (바닥 지지 구조)",
                "explanation": "한자 의미와 무관하게 고유한 건축 용어로 굳어진 표현"
            },
            {
                "mistake": "Thanh chống을 '지지대'로만 번역",
                "correction": "방통 (격자형 바닥 지지 구조)",
                "explanation": "단순 지지대가 아닌 특정한 격자 구조 시스템을 의미"
            },
            {
                "mistake": "장선(joist)과 방통을 같은 것으로 설명",
                "correction": "장선은 서양식 바닥 구조, 방통은 한국식 격자 구조",
                "explanation": "구조와 시공 방식이 다르므로 혼동 주의"
            }
        ],
        "examples": [
            {
                "ko": "한옥 복원 시 방통을 전통 방식으로 시공합니다",
                "vi": "Khi phục hồi nhà truyền thống Hàn Quốc thi công sàn bằng thanh chống theo cách truyền thống",
                "situation": "formal"
            },
            {
                "ko": "방통 간격이 너무 넓으면 바닥이 흔들려요",
                "vi": "Nếu khoảng cách thanh chống quá rộng sàn sẽ bị rung",
                "situation": "onsite"
            },
            {
                "ko": "방통 위에 단열재를 깔고 그 위에 온돌 배관을 설치합니다",
                "vi": "Lát vật liệu cách nhiệt trên thanh chống rồi lắp đường ống sưởi sàn lên trên",
                "situation": "formal"
            }
        ],
        "relatedTerms": ["온돌", "장선", "단열재", "마루", "바닥난방"]
    },
    {
        "slug": "ondol",
        "korean": "온돌",
        "vietnamese": "Ondol",
        "hanja": "溫突",
        "hanjaReading": "따뜻할 온(溫) + 돌출할 돌(突)",
        "pronunciation": "온돌",
        "meaningKo": "한국 전통 난방 방식으로, 아궁이의 열기를 바닥 아래로 통과시켜 방을 데우는 구조입니다. 현대에는 온수 배관을 바닥에 설치하는 '바닥난방' 또는 '마루밑난방'으로 발전했으며, 통역 시 전통 온돌(ondol truyền thống)과 현대식 바닥난방(sưởi sàn nước nóng)을 구분해야 합니다. 베트남에는 난방 문화가 거의 없어 개념 설명부터 필요하며, 열효율(hiệu suất nhiệt), 배관 시공(thi công đường ống), 보일러 연결(kết nối nồi hơi) 등을 상세히 설명해야 합니다.",
        "meaningVi": "Hệ thống sưởi truyền thống Hàn Quốc, dẫn nhiệt từ lò đi qua dưới nền nhà để sưởi ấm phòng. Ngày nay phát triển thành hệ thống sưởi sàn nước nóng với ống nước được lắp dưới sàn.",
        "context": "난방, 한국 문화, 바닥공사",
        "culturalNote": "온돌은 한국 주거 문화의 핵심이나 베트남에는 난방 개념 자체가 생소합니다. 베트남 북부는 겨울에 춥지만 난방 시설 없이 지내는 경우가 대부분이므로, 한국 시공사가 베트남에서 건축 시 난방 시스템 설치 필요성과 비용을 설명해야 합니다. '바닥이 따뜻하다'는 개념 자체를 이해시키는 것부터 시작해야 할 수 있습니다.",
        "commonMistakes": [
            {
                "mistake": "Ondol을 베트남어로 번역 시도",
                "correction": "Ondol (온돌) 고유명사로 사용 + 설명 추가",
                "explanation": "베트남에 없는 개념이므로 음차 후 '한국식 바닥난방'으로 부연"
            },
            {
                "mistake": "Sưởi sàn을 '바닥 난방기'로 역번역",
                "correction": "바닥난방 또는 온돌 (현대식)",
                "explanation": "sưởi sàn은 underfloor heating을 의미하며 온돌의 현대적 형태"
            },
            {
                "mistake": "전통 온돌과 현대식 바닥난방을 구분하지 않음",
                "correction": "ondol truyền thống (아궁이식) vs sưởi sàn nước nóng (온수식)",
                "explanation": "구조와 에너지원이 완전히 다르므로 명확히 구분 필요"
            }
        ],
        "examples": [
            {
                "ko": "한국 아파트는 대부분 온돌 바닥난방이 설치되어 있습니다",
                "vi": "Hầu hết chung cư Hàn Quốc đều có lắp hệ thống sưởi sàn ondol",
                "situation": "formal"
            },
            {
                "ko": "온돌 배관 시공 후 반드시 수압 테스트를 해야 해요",
                "vi": "Sau khi lắp ống ondol bắt buộc phải thử áp lực nước",
                "situation": "onsite"
            },
            {
                "ko": "이 프로젝트는 베트남에서 온돌 시공 경험이 처음입니다",
                "vi": "Dự án này là lần đầu tiên thi công hệ thống ondol tại Việt Nam",
                "situation": "formal"
            }
        ],
        "relatedTerms": ["바닥난방", "보일러", "방통", "난방배관", "마루"]
    },
    {
        "slug": "vat-lieu-xop",
        "korean": "충전재",
        "vietnamese": "Vật liệu xốp",
        "hanja": "充塡材",
        "hanjaReading": "채울 충(充) + 메울 전(塡) + 재료 재(材)",
        "pronunciation": "충전재",
        "meaningKo": "건축물의 빈 공간이나 틈을 메우는 재료로, 단열, 방음, 방수, 또는 구조적 지지 목적으로 사용됩니다. 통역 시 용도에 따라 단열충전재(vật liệu cách nhiệt), 방음충전재(vật liệu cách âm), 발포충전재(vật liệu xốp phồng)로 구분해야 하며, 대표적으로 우레탄폼(xốp polyurethane), 암면(bông khoáng), 글라스울(bông thủy tinh)이 있습니다. 시공 시 밀도(khối lượng riêng), 두께(độ dày), 열전도율(hệ số dẫn nhiệt)을 명확히 지정해야 합니다.",
        "meaningVi": "Vật liệu dùng để lấp đầy khoảng trống hoặc khe hở trong công trình, phục vụ mục đích cách nhiệt, cách âm, chống thấm hoặc hỗ trợ kết cấu. Bao gồm xốp polyurethane, bông khoáng, bông thủy tinh, v.v.",
        "context": "단열공사, 방음공사, 방수공사",
        "culturalNote": "한국에서는 에너지 절약을 위해 충전재 시공이 의무화되어 있으나, 베트남은 열대/아열대 기후라 단열 개념이 약하고 충전재 사용이 선택적입니다. 한국 현장에서는 충전재 두께와 밀도가 법규로 정해져 있으나 베트남은 기준이 느슨해 품질 관리 시 한국 기준을 명확히 전달해야 합니다.",
        "commonMistakes": [
            {
                "mistake": "Filler를 '필러'로만 음차",
                "correction": "충전재 (빈 공간을 채우는 재료)",
                "explanation": "건설 용어로는 '충전재'가 표준이며 용도를 함께 설명하는 것이 명확"
            },
            {
                "mistake": "Vật liệu xốp을 '스펀지 재료'로 오역",
                "correction": "발포 충전재 또는 기포 충전재",
                "explanation": "xốp은 '다공성, 기포가 있는'을 의미하며 스펀지와는 다름"
            },
            {
                "mistake": "단열재와 충전재를 같은 것으로 설명",
                "correction": "vật liệu cách nhiệt (단열재, 목적 명시) vs vật liệu xốp (충전재, 일반 명칭)",
                "explanation": "충전재는 포괄적 용어, 단열재는 목적 특정 용어"
            }
        ],
        "examples": [
            {
                "ko": "벽체 사이 빈 공간에 충전재를 채워주세요",
                "vi": "Lấp đầy vật liệu xốp vào khoảng trống giữa các bức tường",
                "situation": "onsite"
            },
            {
                "ko": "이 구간은 방음 충전재로 암면을 사용합니다",
                "vi": "Đoạn này sử dụng bông khoáng làm vật liệu cách âm",
                "situation": "formal"
            },
            {
                "ko": "우레탄폼 충전 시 팽창률을 고려해야 해요",
                "vi": "Khi bơm xốp polyurethane phải tính đến tỷ lệ nở",
                "situation": "onsite"
            }
        ],
        "relatedTerms": ["단열재", "우레탄폼", "암면", "발포", "기밀"]
    }
]

def main():
    # 파일 경로
    base_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    data_dir = os.path.join(base_dir, "data", "terms")
    file_path = os.path.join(data_dir, "construction.json")

    # 기존 파일 읽기
    with open(file_path, "r", encoding="utf-8") as f:
        data = json.load(f)

    # 새 용어 추가
    data.extend(new_terms)

    # 파일 저장
    with open(file_path, "w", encoding="utf-8") as f:
        json.dump(data, f, ensure_ascii=False, indent=2)

    print(f"✅ {len(new_terms)}개 용어 추가 완료")
    print(f"📁 파일: {file_path}")
    print(f"📊 총 용어 수: {len(data)}개")

if __name__ == "__main__":
    main()
