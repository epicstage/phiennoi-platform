#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Construction 용어 추가 스크립트 v6 (타일/석재 시공)
Tier S 기준 준수 (90점 이상)
"""

import json
import os

# 추가할 용어 데이터 (10개)
new_terms = [
    {
        "slug": "thi-cong-uot",
        "korean": "습식공법",
        "vietnamese": "Thi công ướt",
        "hanja": "濕式工法",
        "hanjaReading": "濕(습할 습) + 式(법 식) + 工(장인 공) + 法(법 법)",
        "pronunciation": "습식공법",
        "meaningKo": "시멘트 모르타르를 사용하여 타일이나 석재를 바닥이나 벽에 붙이는 전통적인 시공 방법입니다. 물과 시멘트를 혼합한 모르타르 반죽을 두껍게 깔고 그 위에 자재를 눌러 붙이는 방식으로, 접착력이 강하고 내구성이 우수합니다. 통역 시 '건식공법'과 명확히 구분해야 하며, 베트남 현장에서는 전통 공법으로 여전히 많이 사용되지만 한국에서는 접착제 공법으로 대체되는 추세임을 설명해야 합니다. '습식'을 'ướt(젖은)'으로 직역하면 이해가 쉽습니다.",
        "meaningVi": "Phương pháp thi công truyền thống sử dụng vữa xi măng để dán gạch hoặc đá lên sàn và tường. Trộn xi măng với nước tạo thành vữa rồi phết dày lên bề mặt, sau đó ép gạch/đá vào. Phương pháp này có độ bám dính cao, độ bền tốt nhưng tốn thời gian thi công và cần thời gian dưỡng hộ.",
        "context": "타일시공, 석재시공, 공법비교, 현장감리",
        "culturalNote": "한국은 1990년대 후반부터 접착제를 이용한 건식공법이 주류가 되었지만, 베트남 건설 현장에서는 여전히 습식공법이 기본으로 사용됩니다. 인건비가 저렴하고 재료를 구하기 쉬우며, 오래된 기술이라 숙련공이 많기 때문입니다. 한국 발주처가 '접착제 붙이기'를 요구할 때 베트남 현장 인력이 익숙하지 않아 시공 품질 문제가 발생할 수 있으므로, 통역 시 공법 교육과 시공 지침을 명확히 전달해야 합니다.",
        "commonMistakes": [
            {
                "mistake": "'습식'을 '젖은 공사'로 직역",
                "correction": "'Thi công ướt' 또는 'Công pháp dán ướt'",
                "explanation": "베트남어로도 '젖은 공법'이라는 의미로 통용되므로 직역이 가능하지만, 건설 용어로서 정식 표현을 사용해야 합니다."
            },
            {
                "mistake": "'모르타르 바르기'와 혼동",
                "correction": "습식공법은 타일/석재 붙이는 전체 공정, 모르타르는 재료",
                "explanation": "습식공법은 시공 방법론이고 모르타르는 그 안에서 사용되는 접착 재료입니다."
            },
            {
                "mistake": "건식공법과 시공 순서를 동일하게 설명",
                "correction": "습식은 모르타르 양생 시간 필요, 건식은 즉시 다음 공정 가능",
                "explanation": "시공 후 양생(dưỡng hộ) 기간이 필요한지 여부가 중요한 차이점입니다."
            }
        ],
        "examples": [
            {
                "ko": "1층 로비 바닥은 습식공법으로 대리석을 시공합니다.",
                "vi": "Sàn tầng 1 thi công đá marble bằng công pháp dán ướt.",
                "situation": "formal"
            },
            {
                "ko": "습식 작업이라 최소 3일은 양생해야 해요.",
                "vi": "Vì thi công ướt nên phải dưỡng hộ tối thiểu 3 ngày.",
                "situation": "onsite"
            },
            {
                "ko": "습식공법은 접착력은 좋지만 공기가 오래 걸립니다.",
                "vi": "Thi công ướt có độ bám dính tốt nhưng mất nhiều thời gian.",
                "situation": "formal"
            }
        ],
        "relatedTerms": ["건식공법", "모르타르", "떠붙이기", "줄눈", "양생"]
    },
    {
        "slug": "thi-cong-kho",
        "korean": "건식공법",
        "vietnamese": "Thi công khô",
        "hanja": "乾式工法",
        "hanjaReading": "乾(마를 건) + 式(법 식) + 工(장인 공) + 法(법 법)",
        "pronunciation": "건식공법",
        "meaningKo": "접착제나 앵커 등을 사용하여 물(모르타르)을 사용하지 않고 타일이나 석재를 시공하는 현대적 공법입니다. 시공 속도가 빠르고 양생 기간이 필요 없으며, 경량화가 가능하여 고층 건물이나 리모델링 공사에 유리합니다. 통역 시 베트남 현장에서는 '접착제 붙이기(dán keo)'로 설명하면 이해가 빠르지만, 정식 시공 용어로는 'thi công khô'를 사용해야 합니다. 한국에서는 주로 타일 전용 접착제를 사용하고, 베트남에서는 아직 숙련공이 부족하므로 시공 교육이 필요함을 주의해야 합니다.",
        "meaningVi": "Phương pháp thi công hiện đại sử dụng keo dán hoặc neo đá không dùng vữa ướt. Tốc độ thi công nhanh, không cần thời gian dưỡng hộ, trọng lượng nhẹ nên phù hợp với công trình cao tầng và cải tạo. Yêu cầu tay nghề cao và vật liệu chuyên dụng.",
        "context": "타일시공, 리모델링, 커튼월석재, 공기단축",
        "culturalNote": "한국 건설 현장에서는 1990년대 후반부터 건식공법이 표준이 되었으며, 타일 전용 접착제 시장이 발달해 있습니다. 반면 베트남에서는 아직 습식공법이 주류이고 건식공법은 고급 프로젝트나 외국 시공사가 참여하는 현장에서만 사용됩니다. 건식공법 전환 시 베트남 인력 재교육이 필요하며, 접착제 품질 관리가 중요합니다. 통역 시 단순히 공법만 전달하는 것이 아니라 필요한 재료(keo dán chuyên dụng)와 시공 절차를 함께 설명해야 합니다.",
        "commonMistakes": [
            {
                "mistake": "'마른 공사'로 직역하여 혼란 초래",
                "correction": "'Thi công khô' 또는 'Dán khô'",
                "explanation": "'건조한 시공'이 아니라 '물 없이 시공하는 방법'이라는 의미를 전달해야 합니다."
            },
            {
                "mistake": "모든 접착제 시공을 건식공법이라고 표현",
                "correction": "타일/석재 시공에만 사용하는 용어",
                "explanation": "목재나 금속 접착은 다른 용어를 사용합니다."
            },
            {
                "mistake": "습식공법보다 품질이 낮다고 오해",
                "correction": "공법의 차이일 뿐, 품질은 재료와 시공 기술에 달려 있음",
                "explanation": "베트남 현장에서 습식공법 선호 경향이 있지만, 건식이 현대적이고 효율적인 공법임을 설명해야 합니다."
            }
        ],
        "examples": [
            {
                "ko": "외벽 화강석은 건식공법으로 앵커 고정합니다.",
                "vi": "Đá granite tường ngoài thi công khô bằng neo cố định.",
                "situation": "formal"
            },
            {
                "ko": "이 접착제는 건식 전용이에요. 모르타르랑 같이 쓰면 안 돼요.",
                "vi": "Keo này dùng cho thi công khô. Không được trộn với vữa.",
                "situation": "onsite"
            },
            {
                "ko": "리모델링이라 건식공법으로 빠르게 진행합니다.",
                "vi": "Vì là cải tạo nên thi công khô để tiến độ nhanh.",
                "situation": "formal"
            }
        ],
        "relatedTerms": ["습식공법", "타일접착제", "앵커고정", "커튼월", "속시공"]
    },
    {
        "slug": "dan-ap",
        "korean": "떠붙이기",
        "vietnamese": "Dán áp",
        "hanja": None,
        "hanjaReading": None,
        "pronunciation": "떠붙이기",
        "meaningKo": "타일이나 석재를 시공할 때 모르타르나 접착제를 재료 뒷면에 발라서 벽이나 바닥에 눌러 붙이는 시공 방식입니다. 전통적인 습식공법의 한 종류로, 모르타르를 바닥/벽에 넓게 바르는 것이 아니라 타일 뒷면에 직접 바르는 것이 특징입니다. 통역 시 '접착제 붙이기(dán keo)'와 구분하여, 모르타르를 사용한 전통 공법임을 명확히 해야 합니다. 베트남에서는 'phương pháp dán trực tiếp'이라고도 하지만, 'dán áp'이 현장에서 더 통용됩니다.",
        "meaningVi": "Phương pháp thi công bằng cách phết vữa hoặc keo trực tiếp lên mặt sau của gạch/đá rồi ép lên tường hoặc sàn. Thuộc công pháp truyền thống (ướt) nhưng khác với cách phết vữa lên bề mặt. Phù hợp với gạch kích thước nhỏ, tốc độ thi công nhanh hơn.",
        "context": "타일시공, 습식공법, 내부마감, 현장용어",
        "culturalNote": "한국 건설 현장에서 '떠붙이기'는 숙련된 타일공들이 사용하는 전통 기법으로, 빠른 시공이 가능하지만 평탄도 확보가 어려워 점차 사용이 줄고 있습니다. 베트남에서는 아직도 많이 사용되며, 인건비가 저렴하여 소규모 공사나 보수 공사에 선호됩니다. 통역 시 '떠붙이기' 공법의 한계(평탄도, 접착력 부족)를 명확히 전달하고, 한국 감리자가 요구하는 품질 기준(레벨 측정, 접착제 사용)을 정확히 설명해야 시공 분쟁을 방지할 수 있습니다.",
        "commonMistakes": [
            {
                "mistake": "'뜬 것'으로 오역하여 불량 시공으로 오해",
                "correction": "'Dán áp'은 정식 시공 방법",
                "explanation": "'떠붙이기'는 시공 기법 이름이지 불량을 의미하지 않습니다."
            },
            {
                "mistake": "접착제 공법과 같다고 설명",
                "correction": "모르타르를 사용하는 습식 공법의 일종",
                "explanation": "재료(vữa vs keo)와 공법의 차이를 명확히 해야 합니다."
            },
            {
                "mistake": "모든 타일에 적용 가능하다고 설명",
                "correction": "대형 타일이나 무거운 석재는 부적합",
                "explanation": "크기 제한(보통 300×300mm 이하)을 설명해야 합니다."
            }
        ],
        "examples": [
            {
                "ko": "화장실 벽 타일은 떠붙이기로 빠르게 진행하세요.",
                "vi": "Gạch tường nhà vệ sinh thi công bằng phương pháp dán áp cho nhanh.",
                "situation": "onsite"
            },
            {
                "ko": "떠붙이기는 평탄도 확보가 어려워서 감리가 승인 안 해줄 거예요.",
                "vi": "Dán áp khó đảm bảo độ phẳng nên giám sát sẽ không chấp nhận.",
                "situation": "onsite"
            },
            {
                "ko": "소형 타일은 떠붙이기 공법이 경제적입니다.",
                "vi": "Gạch kích thước nhỏ dùng phương pháp dán áp sẽ tiết kiệm.",
                "situation": "formal"
            }
        ],
        "relatedTerms": ["습식공법", "모르타르", "타일시공", "평탄도", "줄눈"]
    },
    {
        "slug": "keo-dan-gach",
        "korean": "접착제붙이기",
        "vietnamese": "Keo dán gạch",
        "hanja": None,
        "hanjaReading": None,
        "pronunciation": "접착제붙이기",
        "meaningKo": "타일이나 석재를 벽이나 바닥에 붙일 때 시멘트 모르타르 대신 전용 접착제를 사용하는 건식공법 시공 방식입니다. 접착력이 우수하고 시공 속도가 빠르며, 양생 시간이 짧고 수축·팽창에 강해 균열이 적습니다. 통역 시 일반 접착제가 아닌 '타일 전용 접착제(keo dán gạch chuyên dụng)'임을 강조해야 하며, 베트남 현장에서는 저가 접착제를 사용하려는 경향이 있으므로 품질 기준(C1, C2 등급)을 명확히 전달해야 합니다. 한국 시방서는 보통 KS 인증 제품을 요구하므로 동등 품질 확인이 필요합니다.",
        "meaningVi": "Phương pháp thi công dán gạch hoặc đá bằng keo chuyên dụng thay vì vữa xi măng (công pháp khô). Độ bám dính cao, tốc độ thi công nhanh, thời gian dưỡng hộ ngắn, chịu co giãn tốt nên ít nứt. Yêu cầu dùng keo chuyên dụng có chuẩn chất lượng (C1, C2).",
        "context": "타일시공, 건식공법, 자재선정, 품질관리",
        "culturalNote": "한국은 1990년대 후반부터 타일 접착제 시장이 성숙하여 다양한 등급(C1, C2, S1, S2)과 용도별(내외부, 대형 타일용, 석재용) 제품이 있습니다. 베트남에서는 아직 시장이 형성 단계라 고급 접착제는 수입에 의존하고 있으며, 현지 제품은 품질 편차가 큽니다. 한국 발주처가 '타일 접착제 시공'을 요구할 때 베트남 현장에서는 가격 부담으로 저가 제품을 사용하려 하거나, 접착제 양을 줄여 시공하는 경우가 있어 품질 문제가 발생합니다. 통역 시 제품 사양서(technical datasheet)를 함께 확인하고, 도포량(kg/m²)까지 명확히 전달해야 합니다.",
        "commonMistakes": [
            {
                "mistake": "일반 건축용 접착제와 혼동",
                "correction": "타일 전용 접착제는 수분·하중·온도 변화에 강한 특수 제품",
                "explanation": "'keo dán' 일반 용어가 아니라 'keo dán gạch chuyên dụng'을 사용해야 합니다."
            },
            {
                "mistake": "'접착제 = 간편한 시공'으로 오해",
                "correction": "접착제 시공도 바탕면 처리, 도포량, 압착 시간 등 정밀 공정 필요",
                "explanation": "오히려 숙련도가 요구되며, 부실 시공 시 탈락 위험이 큽니다."
            },
            {
                "mistake": "저가 접착제 사용해도 된다고 설명",
                "correction": "C1 이상 등급, 접착력 시험 성적서 필수",
                "explanation": "품질 기준을 타협하면 하자 발생 시 책임 문제가 됩니다."
            }
        ],
        "examples": [
            {
                "ko": "외부 타일은 C2급 접착제로 시공하세요. 서리 저항성이 필요합니다.",
                "vi": "Gạch ngoài trời dùng keo cấp C2, cần chống sương giá.",
                "situation": "formal"
            },
            {
                "ko": "접착제 붙이기는 모르타르보다 빠르지만 재료비가 좀 나가요.",
                "vi": "Dán keo nhanh hơn vữa nhưng chi phí vật liệu cao hơn.",
                "situation": "onsite"
            },
            {
                "ko": "대형 타일이라 접착제 도포량을 늘려야 합니다.",
                "vi": "Gạch cỡ lớn nên phải tăng lượng keo phết.",
                "situation": "formal"
            }
        ],
        "relatedTerms": ["건식공법", "타일접착제", "C2등급", "도포량", "양생기간"]
    },
    {
        "slug": "neo-co-dinh-da",
        "korean": "석재앵커",
        "vietnamese": "Neo cố định đá",
        "hanja": "石材anchor",
        "hanjaReading": "石(돌 석) + 材(재목 재) + [영어: 앵커]",
        "pronunciation": "석재앵커",
        "meaningKo": "무거운 석재(화강석, 대리석 등)를 외벽이나 내벽에 고정할 때 사용하는 금속 고정장치입니다. 건식공법의 핵심 부재로, 석재에 구멍을 뚫고 앵커를 삽입하여 구조체에 고정합니다. 재질은 주로 스테인리스강(STS304, STS316)을 사용하며, 부식 방지와 내하중 성능이 중요합니다. 통역 시 '앵커 볼트(bu lông neo)'와 구분하여 석재 전용 앵커임을 명확히 하고, 시공 시 석재 파손 방지를 위한 드릴링 방법과 에폭시 충전 절차를 정확히 전달해야 합니다.",
        "meaningVi": "Thiết bị cố định bằng kim loại dùng để gắn đá nặng (đá granite, marble...) lên tường ngoài hoặc trong. Là bộ phận cốt lõi của công pháp khô, khoan lỗ trên đá rồi lắp neo vào kết cấu. Chất liệu thường dùng inox (STS304, STS316), quan trọng là chống ăn mòn và chịu tải.",
        "context": "석재시공, 외벽마감, 커튼월, 구조안전",
        "culturalNote": "한국 건설 현장에서는 석재 앵커 시공이 표준화되어 있으며, 시공 상세도(shop drawing)에 앵커 위치, 개수, 사이즈가 명확히 표시됩니다. 베트남에서는 고급 프로젝트 외에는 석재 앵커 시공 경험이 적고, 숙련공이 부족하여 드릴링 시 석재 파손 사고가 자주 발생합니다. 통역 시 단순히 '앵커로 고정한다'가 아니라, 드릴 비트 종류(diamond core bit), 드릴 속도, 구멍 깊이, 에폭시 주입량까지 구체적으로 설명해야 합니다. 특히 앵커 재질(STS316 = inox 316) 용어를 정확히 전달해야 저가 철제 앵커 사용을 방지할 수 있습니다.",
        "commonMistakes": [
            {
                "mistake": "'앵커 볼트'와 같다고 설명",
                "correction": "석재 앵커는 석재 전용, 앵커 볼트는 구조체 고정용",
                "explanation": "용도와 형상이 다르며, 석재 앵커는 팽창식 또는 화학식 고정 방식을 사용합니다."
            },
            {
                "mistake": "철제 앵커 사용 가능하다고 설명",
                "correction": "반드시 스테인리스강(STS304 이상) 사용",
                "explanation": "철제는 녹이 슬어 석재에 얼룩이 생기고 강도가 약해집니다."
            },
            {
                "mistake": "석재에 구멍만 뚫으면 된다고 설명",
                "correction": "에폭시 충전 후 앵커 삽입, 양생 필요",
                "explanation": "화학식 앵커는 에폭시가 굳는 시간이 필요하며, 즉시 하중을 가하면 안 됩니다."
            }
        ],
        "examples": [
            {
                "ko": "외벽 화강석은 STS316 석재 앵커로 1㎡당 4개 고정합니다.",
                "vi": "Đá granite tường ngoài dùng neo đá inox 316, 4 cái mỗi mét vuông.",
                "situation": "formal"
            },
            {
                "ko": "석재 앵커 구멍 뚫을 때 천천히 해야 돌 안 깨져요.",
                "vi": "Khi khoan lỗ neo đá phải từ từ mới không vỡ đá.",
                "situation": "onsite"
            },
            {
                "ko": "앵커 에폭시가 완전히 굳을 때까지 24시간 기다리세요.",
                "vi": "Đợi 24 giờ cho keo epoxy neo đá khô hẳn.",
                "situation": "onsite"
            }
        ],
        "relatedTerms": ["건식공법", "스테인리스강", "에폭시", "커튼월", "화강석"]
    },
    {
        "slug": "vat-lieu-lot-mach",
        "korean": "실링백업재",
        "vietnamese": "Vật liệu lót mạch",
        "hanja": None,
        "hanjaReading": None,
        "pronunciation": "실링백업재",
        "meaningKo": "석재나 타일 줄눈, 창호와 벽체 사이 틈새에 실링재(씰란트)를 주입하기 전에 먼저 채우는 완충 재료입니다. 주로 폼 재질(PE 폼, 우레탄 폼)을 사용하며, 실링재의 깊이를 조절하고 3면 접착을 방지하여 신축·수축 시 실링재가 찢어지지 않도록 합니다. 통역 시 '백업재'만 말하면 이해가 어려우므로 'vật liệu lót(밑받침재)' 또는 'thanh xốp lót mạch(줄눈 밑 폼바)'로 설명하면 명확합니다. 베트남 현장에서는 백업재를 생략하고 실링재만 주입하는 경우가 많아, 하자 예방을 위해 시공 순서를 정확히 전달해야 합니다.",
        "meaningVi": "Vật liệu đệm (thường là xốp PE hoặc polyurethane) được lót vào mạch nối trước khi bơm silicone/sealant. Mục đích là điều chỉnh độ sâu của sealant và tránh hiện tượng dính 3 mặt (3-sided adhesion), giúp sealant không bị rách khi co giãn. Nếu bỏ qua bước này, sealant dễ bị hư hại.",
        "context": "줄눈시공, 실링공사, 방수공사, 외벽마감",
        "culturalNote": "한국 건설 현장에서는 '백업재 설치 → 프라이머 도포 → 실링재 주입'이 표준 공정이며, 특히 외벽 석재 줄눈이나 창호 실링에서 백업재는 필수입니다. 베트남 현장에서는 백업재를 사용하지 않거나, 신문지나 스티로폼 조각으로 대체하는 경우가 많아 실링재가 조기에 찢어지는 하자가 빈번합니다. 통역 시 백업재의 역할(깊이 조절, 3면 접착 방지)을 명확히 설명하고, 저가 대체재 사용을 금지해야 합니다. 'thanh xốp'(폼 바)라는 표현이 현장에서 가장 잘 통합니다.",
        "commonMistakes": [
            {
                "mistake": "'백업재' 직역하여 '예비재료'로 오해",
                "correction": "'Vật liệu lót mạch' 또는 'Thanh xốp lót'",
                "explanation": "예비가 아니라 줄눈 밑에 깔아주는 필수 재료입니다."
            },
            {
                "mistake": "아무 스티로폼이나 사용 가능하다고 설명",
                "correction": "PE 폼 또는 우레탄 폼 전용 제품 사용",
                "explanation": "일반 스티로폼은 실링재 용제에 녹거나 압축 복원력이 없어 부적합합니다."
            },
            {
                "mistake": "백업재 없이 실링재만 두껍게 채우면 된다고 설명",
                "correction": "3면 접착되면 신축 시 찢어짐 발생",
                "explanation": "백업재는 실링재가 2면에만 접착되도록 하는 역할을 합니다."
            }
        ],
        "examples": [
            {
                "ko": "석재 줄눈 폭이 20mm니까 백업재는 지름 25mm로 사용하세요.",
                "vi": "Mạch đá rộng 20mm thì dùng thanh xốp lót đường kính 25mm.",
                "situation": "formal"
            },
            {
                "ko": "백업재 안 넣으면 실링재가 금방 찢어져요.",
                "vi": "Không lót thanh xốp thì silicone dễ rách.",
                "situation": "onsite"
            },
            {
                "ko": "백업재는 줄눈 깊이의 절반 위치에 설치합니다.",
                "vi": "Thanh xốp lót đặt ở vị trí giữa độ sâu mạch.",
                "situation": "formal"
            }
        ],
        "relatedTerms": ["실링재", "줄눈", "3면접착", "석재시공", "방수공사"]
    },
    {
        "slug": "vua-mach-noi",
        "korean": "줄눈모르타르",
        "vietnamese": "Vữa mạch nối",
        "hanja": None,
        "hanjaReading": None,
        "pronunciation": "줄눈모르타르",
        "meaningKo": "타일이나 석재를 시공한 후 자재 사이의 틈(줄눈)을 메우는 전용 모르타르입니다. 일반 시멘트 모르타르와 달리 내수성, 내구성, 색상 안정성이 우수하며, 줄눈 폭과 용도에 따라 다양한 제품이 있습니다. 통역 시 '시멘트로 틈새 메우기'가 아니라 '전용 줄눈재(vữa mạch chuyên dụng)'임을 강조해야 하며, 색상 지정(màu trắng, màu xám 등)과 방수형·비방수형 구분을 명확히 전달해야 합니다. 베트남 현장에서는 일반 시멘트를 희석하여 사용하는 경우가 많아, 시방서대로 전용 제품 사용을 강조해야 합니다.",
        "meaningVi": "Vữa chuyên dụng để lấp đầy khe hở (mạch nối) giữa các viên gạch hoặc tấm đá sau khi thi công. Khác với vữa xi măng thường, loại này có độ chống nước, độ bền và màu sắc ổn định cao. Có nhiều loại tùy theo độ rộng mạch và mục đích sử dụng (chống thấm, không chống thấm).",
        "context": "타일시공, 줄눈공사, 마감공사, 품질관리",
        "culturalNote": "한국에서는 1990년대부터 줄눈 전용 제품(그라우트) 시장이 발달하여 색상, 방수 기능, 항균 기능 등 다양한 제품이 있습니다. 베트남 현장에서는 아직 고급 현장 외에는 일반 시멘트에 백시멘트를 섞어 사용하는 경우가 많고, 색상 변색이나 균열 문제가 빈번합니다. 한국 감리자가 줄눈재 색상 샘플 승인을 요구할 때 베트남 현장에서는 '그냥 흰색 시멘트'로 이해하는 경우가 많아, 전용 제품 샘플(sample màu vữa mạch)을 제출해야 한다는 것을 명확히 통역해야 합니다.",
        "commonMistakes": [
            {
                "mistake": "'줄눈'을 '금 간 곳'으로 오해",
                "correction": "'Mạch nối'는 설계상 의도된 틈새",
                "explanation": "균열(vết nứt)과 줄눈(mạch nối)은 완전히 다른 개념입니다."
            },
            {
                "mistake": "일반 시멘트로 대체 가능하다고 설명",
                "correction": "전용 줄눈재(grout chuyên dụng) 필수",
                "explanation": "일반 시멘트는 변색, 균열, 탈락이 쉽게 발생합니다."
            },
            {
                "mistake": "줄눈 폭에 관계없이 같은 재료 사용",
                "correction": "2mm 이하는 미세 줄눈재, 그 이상은 일반 줄눈재",
                "explanation": "줄눈 폭에 따라 제품 입자 크기가 다릅니다."
            }
        ],
        "examples": [
            {
                "ko": "욕실 바닥 타일은 방수형 줄눈모르타르로 시공하세요.",
                "vi": "Gạch sàn nhà vệ sinh dùng vữa mạch chống thấm.",
                "situation": "formal"
            },
            {
                "ko": "줄눈 색이 지정된 거 있어요. 샘플 확인 후 시공해야 해요.",
                "vi": "Có màu vữa mạch chỉ định. Phải kiểm tra mẫu trước khi thi công.",
                "situation": "onsite"
            },
            {
                "ko": "줄눈 너비가 3mm니까 미세 줄눈재를 사용합니다.",
                "vi": "Mạch rộng 3mm nên dùng vữa mạch mịn.",
                "situation": "formal"
            }
        ],
        "relatedTerms": ["타일시공", "그라우트", "줄눈폭", "방수공사", "색상샘플"]
    },
    {
        "slug": "gach-chong-truot",
        "korean": "논슬립타일",
        "vietnamese": "Gạch chống trượt",
        "hanja": "non-slip타일",
        "hanjaReading": "[영어: non-slip] + [영어: 타일]",
        "pronunciation": "논슬립타일",
        "meaningKo": "표면에 요철이나 특수 마감 처리가 되어 있어 미끄럼을 방지하는 타일입니다. 욕실, 계단, 경사로, 주방 등 물기가 있거나 안전이 중요한 곳에 사용하며, 미끄럼 저항 계수(COF, Coefficient of Friction)로 성능을 평가합니다. 통역 시 '미끄럼방지 타일'보다 '논슬립타일'이라는 용어가 한국 현장에서 표준이므로, 베트남어로는 'gạch chống trượt' 또는 'gạch nhám'으로 설명하되, 성능 기준(COF 0.6 이상)을 함께 전달해야 합니다. 베트남 현장에서는 저가 타일을 '논슬립'이라고 판매하는 경우가 많아, 시험 성적서 확인이 필요합니다.",
        "meaningVi": "Gạch có bề mặt nhám hoặc xử lý đặc biệt để chống trơn trượt. Dùng cho nhà vệ sinh, cầu thang, dốc, bếp... nơi có nước hoặc cần an toàn. Hiệu suất đánh giá bằng hệ số chống trượt (COF - Coefficient of Friction), tiêu chuẩn tốt là COF ≥ 0.6.",
        "context": "타일선정, 안전시설, 욕실공사, 장애인시설",
        "culturalNote": "한국 건축법규에서는 욕실, 계단, 장애인 시설 등에 미끄럼 저항 성능 기준을 명시하고 있으며, 감리 시 COF 시험 성적서를 요구합니다. 베트남에서는 안전 규정이 느슨하여 논슬립타일 사용이 권장 사항에 그치는 경우가 많고, 시험 성적서 없이 '표면이 거칠면 논슬립'이라고 판단하는 경향이 있습니다. 통역 시 단순히 '미끄럼방지'가 아니라 COF 수치와 시험 방법(습식 상태, 건조 상태)을 설명해야 하며, 한국 발주처가 요구하는 KS 인증 제품 또는 동등 품질을 명확히 전달해야 합니다.",
        "commonMistakes": [
            {
                "mistake": "'표면이 거칠면 논슬립'이라고 설명",
                "correction": "COF 시험 성적서로 입증된 제품만 논슬립",
                "explanation": "시각적으로만 판단하면 안 되며, 정량적 성능 확인이 필요합니다."
            },
            {
                "mistake": "'논슬립 = 무광 타일'로 오해",
                "correction": "광택과 무관하게 표면 처리 방식에 따라 결정",
                "explanation": "유광 타일 중에도 특수 코팅으로 논슬립 성능을 갖춘 제품이 있습니다."
            },
            {
                "mistake": "모든 바닥 타일을 논슬립으로 지정",
                "correction": "필요한 구역만 지정 (비용, 청소 난이도 고려)",
                "explanation": "논슬립타일은 가격이 높고 청소가 어려워 필요한 곳에만 사용합니다."
            }
        ],
        "examples": [
            {
                "ko": "욕실 바닥은 COF 0.6 이상 논슬립타일로 시공하세요.",
                "vi": "Sàn nhà vệ sinh dùng gạch chống trượt COF từ 0.6 trở lên.",
                "situation": "formal"
            },
            {
                "ko": "계단은 논슬립 필수예요. 안전 검사 통과 못 해요.",
                "vi": "Cầu thang bắt buộc dùng gạch chống trượt. Không qua kiểm tra an toàn.",
                "situation": "onsite"
            },
            {
                "ko": "이 타일 논슬립이라는데, 시험 성적서 있나요?",
                "vi": "Gạch này nói là chống trượt, có giấy chứng nhận thử nghiệm không?",
                "situation": "onsite"
            }
        ],
        "relatedTerms": ["타일시공", "미끄럼저항", "COF", "안전시설", "욕실공사"]
    },
    {
        "slug": "may-cat-gach",
        "korean": "타일절단기",
        "vietnamese": "Máy cắt gạch",
        "hanja": None,
        "hanjaReading": None,
        "pronunciation": "타일절단기",
        "meaningKo": "타일이나 석재를 원하는 크기와 형태로 자르는 전동 공구입니다. 수동식(스코어 커터)과 전동식(습식 절단기)이 있으며, 현장에서는 다이아몬드 날을 장착한 습식 절단기가 주로 사용됩니다. 통역 시 '톱(cưa)'과 구분하여 '전용 절단기(máy cắt chuyên dụng)'임을 명확히 해야 하며, 안전 장비(보안경, 귀마개, 방진마스크) 착용과 물 공급(냉각·분진 방지)을 함께 설명해야 합니다. 베트남 현장에서는 안전 수칙 미준수로 절단 중 파편에 의한 부상이 빈번하므로, 안전 교육을 반드시 병행해야 합니다.",
        "meaningVi": "Máy công cụ điện dùng để cắt gạch hoặc đá theo kích thước và hình dạng mong muốn. Có loại thủ công (dao cắt rạch) và loại điện (máy cắt ướt), hiện trường thường dùng máy cắt ướt gắn lưỡi kim cương. Phải đeo bảo hộ (kính, bịt tai, khẩu trang) và cấp nước (làm mát, chống bụi).",
        "context": "타일시공, 장비운용, 안전관리, 현장작업",
        "culturalNote": "한국 건설 현장에서는 타일 절단 시 습식 절단기 사용이 표준이며, 안전 수칙(물 공급, 보안경 착용, 분진 마스크)이 엄격히 적용됩니다. 베트남 현장에서는 수동식 절단기를 많이 사용하고, 전동 절단기 사용 시에도 물 공급을 생략하거나 안전 장비 미착용으로 분진 흡입 및 파편 사고가 빈번합니다. 통역 시 단순히 '타일 자르는 기계'가 아니라, 안전 절차(lưỡi cắt kim cương, cấp nước liên tục, đeo kính bảo hộ)를 함께 설명해야 하며, 특히 대형 석재 절단 시 장비 고정과 2인 작업을 강조해야 합니다.",
        "commonMistakes": [
            {
                "mistake": "일반 '톱'으로 번역하여 목공 톱과 혼동",
                "correction": "'Máy cắt gạch' 또는 'Máy cắt gạch chuyên dụng'",
                "explanation": "타일/석재 전용 절단기는 다이아몬드 날과 물 공급 장치가 있는 특수 장비입니다."
            },
            {
                "mistake": "물 공급 없이 건식 절단 가능하다고 설명",
                "correction": "습식 절단 필수 (냉각, 분진 방지)",
                "explanation": "건식 절단은 날 과열과 폐질환 유발 분진 발생으로 금지됩니다."
            },
            {
                "mistake": "안전 장비 없이 작업 가능하다고 설명",
                "correction": "보안경, 방진마스크, 귀마개 필수",
                "explanation": "파편에 의한 실명, 분진 흡입, 소음성 난청 위험이 있습니다."
            }
        ],
        "examples": [
            {
                "ko": "타일 절단기는 반드시 물을 공급하면서 사용하세요. 분진이 위험합니다.",
                "vi": "Máy cắt gạch bắt buộc phải cấp nước khi dùng. Bụi rất nguy hiểm.",
                "situation": "onsite"
            },
            {
                "ko": "이 석재는 두께가 30mm라 대형 절단기로 작업해야 해요.",
                "vi": "Đá này dày 30mm nên phải dùng máy cắt cỡ lớn.",
                "situation": "onsite"
            },
            {
                "ko": "절단기 날이 무뎌지면 즉시 교체하세요. 파손 위험 있어요.",
                "vi": "Lưỡi cắt cùn thì đổi ngay. Có nguy cơ vỡ.",
                "situation": "onsite"
            }
        ],
        "relatedTerms": ["타일시공", "다이아몬드날", "습식절단", "안전장비", "분진방지"]
    },
    {
        "slug": "neo-dinh-ket-cau",
        "korean": "앵커고정",
        "vietnamese": "Neo định kết cấu",
        "hanja": "anchor固定",
        "hanjaReading": "[영어: 앵커] + 固(굳을 고) + 定(정할 정)",
        "pronunciation": "앵커고정",
        "meaningKo": "무거운 부재(석재, 설비, 구조물)를 콘크리트나 구조체에 고정할 때 앵커를 사용하여 결합하는 공법입니다. 기계식 앵커(팽창식, 언더컷식)와 화학식 앵커(에폭시, 레진)로 구분되며, 하중과 용도에 따라 적합한 앵커를 선정해야 합니다. 통역 시 '앵커 볼트(bu lông neo)'와 혼동하지 않도록 하며, 앵커의 종류, 매입 깊이, 인발 시험 등 기술 용어를 정확히 전달해야 합니다. 베트남 현장에서는 앵커 타입 선정이 부적절하거나 천공 깊이가 부족하여 하중 시험에서 탈락하는 사례가 많으므로, 시공 사양을 명확히 전달해야 합니다.",
        "meaningVi": "Công pháp cố định cấu kiện nặng (đá, thiết bị, kết cấu) vào bê tông hoặc kết cấu bằng neo. Chia làm neo cơ học (dãn nở, undercut) và neo hóa học (epoxy, resin), chọn loại neo phù hợp theo tải trọng và mục đích. Phải đảm bảo độ sâu chôn và thử nghiệm kéo nhổ.",
        "context": "석재시공, 설비고정, 구조보강, 안전점검",
        "culturalNote": "한국 건설 현장에서는 앵커 시공 시 구조 계산에 따라 앵커 타입, 개수, 배치가 정해지며, 시공 후 인발 시험(pull-out test)으로 성능을 검증합니다. 베트남 현장에서는 앵커 선정이 경험에 의존하고, 인발 시험을 생략하는 경우가 많아 추후 하중 증가 시 탈락 사고가 발생합니다. 통역 시 앵커 타입(neo giãn nở, neo hóa học)과 시험 기준(lực kéo nhổ)을 명확히 전달하고, 특히 외벽 석재나 중량 설비의 경우 시험 성적서 제출을 명시해야 합니다. '앵커'를 단순히 'bu lông'으로 번역하면 일반 볼트와 혼동되므로 'neo kết cấu'로 구분해야 합니다.",
        "commonMistakes": [
            {
                "mistake": "'앵커'를 일반 '볼트'로 번역",
                "correction": "'Neo kết cấu' 또는 'Neo định vị'",
                "explanation": "앵커는 콘크리트에 매입하는 특수 고정구로, 일반 볼트와 원리가 다릅니다."
            },
            {
                "mistake": "모든 앵커가 같다고 설명",
                "correction": "기계식, 화학식 앵커는 용도와 하중이 다름",
                "explanation": "타입별 적용 범위와 시공 방법이 완전히 다릅니다."
            },
            {
                "mistake": "천공 깊이는 대충 깊게만 뚫으면 된다고 설명",
                "correction": "설계 도면에 명시된 매입 깊이 정확히 준수",
                "explanation": "너무 얕으면 인발되고, 너무 깊으면 콘크리트 파손 위험이 있습니다."
            }
        ],
        "examples": [
            {
                "ko": "외벽 석재는 화학식 앵커로 고정하고 인발 시험 받으세요.",
                "vi": "Đá tường ngoài dùng neo hóa học và phải thử nghiệm kéo nhổ.",
                "situation": "formal"
            },
            {
                "ko": "이 앵커는 10kN까지 견뎌야 해요. 시험 성적서 필요합니다.",
                "vi": "Neo này phải chịu được 10kN. Cần giấy chứng nhận thử nghiệm.",
                "situation": "formal"
            },
            {
                "ko": "앵커 구멍은 지름 12mm, 깊이 100mm로 천공하세요.",
                "vi": "Khoan lỗ neo đường kính 12mm, sâu 100mm.",
                "situation": "onsite"
            }
        ],
        "relatedTerms": ["석재앵커", "기계식앵커", "화학식앵커", "인발시험", "구조안전"]
    }
]

def main():
    # 파일 경로 설정
    base_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    file_path = os.path.join(base_dir, "data", "terms", "construction.json")

    # 기존 파일 읽기
    with open(file_path, 'r', encoding='utf-8') as f:
        data = json.load(f)

    # 기존 용어 개수 확인
    original_count = len(data)
    print(f"기존 용어 개수: {original_count}개")

    # 새 용어 추가
    data.extend(new_terms)

    # 새 파일로 저장
    with open(file_path, 'w', encoding='utf-8') as f:
        json.dump(data, f, ensure_ascii=False, indent=2)

    print(f"✅ {len(new_terms)}개 용어 추가 완료")
    print(f"총 용어 개수: {len(data)}개")
    print(f"저장 위치: {file_path}")

if __name__ == "__main__":
    main()
