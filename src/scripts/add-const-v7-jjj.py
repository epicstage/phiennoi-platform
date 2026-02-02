#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Construction 용어 추가 - 조적/석공/벽체 테마 (10개)
Tier S 기준 준수
"""

import json
import os

# 추가할 용어 데이터 (10개)
data = [
    {
        "slug": "vua-xi-mang",
        "korean": "시멘트모르타르",
        "vietnamese": "Vữa xi măng",
        "hanja": "水泥mortar",
        "hanjaReading": "水(물 수) + 泥(진흙 니) + mortar(영어)",
        "pronunciation": "비어 시 망",
        "meaningKo": "시멘트, 모래, 물을 혼합한 결합재로 벽돌이나 블록을 접착하거나 표면을 마감하는 데 사용됩니다. 통역 시 '모르타르'를 단순히 '시멘트'로만 번역하면 콘크리트와 혼동될 수 있으므로 반드시 '시멘트모르타르' 또는 '접착용 시멘트 혼합물'로 구분해야 합니다. 배합 비율과 용도에 따라 일반 모르타르, 방수 모르타르, 단열 모르타르 등으로 나뉘며, 현장에서는 강도와 작업성을 고려한 정확한 배합이 중요합니다.",
        "meaningVi": "Hỗn hợp xi măng, cát và nước dùng để dán gạch, khối xây hoặc hoàn thiện bề mặt. Tỷ lệ phối trộn và ứng dụng quyết định loại vữa (vữa thường, vữa chống thấm, vữa cách nhiệt).",
        "context": "조적공사, 타일공사, 미장공사에서 접착재 또는 마감재로 사용",
        "culturalNote": "한국에서는 시멘트와 모르타르를 엄격히 구분하지만, 베트남 현장에서는 'xi măng'이라는 용어가 시멘트와 모르타르 모두를 지칭하는 경우가 많습니다. 따라서 통역 시 'vữa xi măng'으로 명확히 표현하거나, 필요 시 '시멘트 혼합물(hỗn hợp xi măng)'로 부연 설명해야 혼선을 방지할 수 있습니다. 배합 비율도 한국은 부피비, 베트남은 중량비를 많이 쓰므로 주의가 필요합니다.",
        "commonMistakes": [
            {
                "mistake": "모르타르를 'xi măng'으로만 번역",
                "correction": "vữa xi măng",
                "explanation": "시멘트 자체와 혼동될 수 있어 '모르타르'임을 명시해야 함"
            },
            {
                "mistake": "콘크리트와 혼용",
                "correction": "콘크리트는 'bê tông', 모르타르는 'vữa'",
                "explanation": "콘크리트는 굵은 골재 포함, 모르타르는 미세 골재만 사용"
            },
            {
                "mistake": "배합비를 부피로만 설명",
                "correction": "부피비 또는 중량비 명시",
                "explanation": "베트남 현장은 중량비를 많이 사용하므로 단위 확인 필수"
            }
        ],
        "examples": [
            {
                "ko": "벽돌 쌓기용 시멘트모르타르는 1:3 배합으로 준비하세요.",
                "vi": "Vữa xi măng cho xây gạch cần trộn theo tỷ lệ 1:3.",
                "situation": "onsite"
            },
            {
                "ko": "방수 모르타르를 사용하여 욕실 바닥을 마감합니다.",
                "vi": "Hoàn thiện sàn nhà vệ sinh bằng vữa chống thấm.",
                "situation": "formal"
            },
            {
                "ko": "모르타르가 굳기 전에 줄눈을 정리하세요.",
                "vi": "Hoàn thiện mạch nối trước khi vữa đông cứng.",
                "situation": "onsite"
            }
        ],
        "relatedTerms": ["콘크리트", "배합비", "줄눈", "미장공사"]
    },
    {
        "slug": "vua-hon-hop",
        "korean": "혼화모르타르",
        "vietnamese": "Vữa hỗn hợp",
        "hanja": "混和mortar",
        "hanjaReading": "混(섞을 혼) + 和(화할 화) + mortar(영어)",
        "pronunciation": "비어 혼 험",
        "meaningKo": "시멘트모르타르에 혼화제(혼화재)를 첨가하여 작업성, 접착성, 내구성 등을 개선한 모르타르입니다. 통역 시 '혼화제(phụ gia)'와 '혼화재(vật liệu phụ gia)'를 구분하고, 화학 혼화제는 'phụ gia hóa học', 광물질 혼화재는 'vật liệu khoáng'으로 세분화하여 전달해야 합니다. 현장에서 흔히 사용하는 AE제, 감수제, 방수제 등의 기능을 명확히 설명해야 실수를 방지할 수 있습니다.",
        "meaningVi": "Vữa xi măng có thêm phụ gia để cải thiện tính năng như tính công tác, độ bám dính, độ bền. Phụ gia hóa học (AE제, giảm nước) và vật liệu khoáng (tro bay, xỉ) được phân biệt rõ.",
        "context": "특수 공사, 타일 붙임, 방수 공사 등에서 성능 향상 목적",
        "culturalNote": "한국에서는 혼화제와 혼화재를 KS 규격으로 엄격히 구분하지만, 베트남 현장에서는 'phụ gia'라는 용어로 통칭하는 경우가 많습니다. 통역 시 화학 혼화제(AE제, 감수제)는 'phụ gia hóa học', 광물질 혼화재(플라이애시, 슬래그)는 'vật liệu khoáng phụ gia'로 명확히 구분해야 혼선을 방지할 수 있습니다. 또한 베트남은 혼화제 사용 기준이 다를 수 있으므로 현지 규정 확인이 필요합니다.",
        "commonMistakes": [
            {
                "mistake": "혼화제와 혼화재를 'phụ gia'로 통칭",
                "correction": "혼화제는 'phụ gia hóa học', 혼화재는 'vật liệu khoáng phụ gia'",
                "explanation": "성질과 기능이 다르므로 구분 필수"
            },
            {
                "mistake": "AE제를 단순히 'chất phụ gia'로만 번역",
                "correction": "chất phụ gia tạo bọt khí (공기연행제)",
                "explanation": "기능을 명시해야 현장에서 이해 가능"
            },
            {
                "mistake": "첨가량 단위 혼동",
                "correction": "중량비(%) 또는 용량(lít/m³) 명시",
                "explanation": "베트남은 용량 단위도 많이 사용하므로 확인 필요"
            }
        ],
        "examples": [
            {
                "ko": "혼화모르타르에 방수제를 첨가하여 접착력을 높입니다.",
                "vi": "Thêm chất chống thấm vào vữa hỗn hợp để tăng độ bám dính.",
                "situation": "formal"
            },
            {
                "ko": "AE제를 0.5% 첨가한 혼화모르타르를 사용하세요.",
                "vi": "Sử dụng vữa hỗn hợp với 0.5% chất tạo bọt khí.",
                "situation": "onsite"
            },
            {
                "ko": "현장에서 혼화제 혼합 비율을 정확히 지켜야 합니다.",
                "vi": "Cần tuân thủ chính xác tỷ lệ phụ gia hóa học tại công trường.",
                "situation": "formal"
            }
        ],
        "relatedTerms": ["시멘트모르타르", "혼화제", "방수제", "감수제"]
    },
    {
        "slug": "khoi-gach-co-cot-thep",
        "korean": "보강블록",
        "vietnamese": "Khối gạch có cốt thép",
        "hanja": "補強block",
        "hanjaReading": "補(도울 보) + 強(강할 강) + block(영어)",
        "pronunciation": "코이 자익 꼬 꼳 텝",
        "meaningKo": "내부에 철근을 배근하고 콘크리트를 채워 넣어 구조적 강도를 높인 조적용 블록입니다. 통역 시 '보강블록'과 '일반 블록(gạch không xây)'을 명확히 구분하고, 철근 배근 위치와 콘크리트 충전 방법을 정확히 전달해야 합니다. 주의할 점은 한국에서는 '블록', 베트남에서는 '가익(gạch)' 또는 '코이(khối)'로 표현하는 차이가 있으므로, 현장에서는 '코이 자익 꼬 꼳 텝' 또는 '가익 보 깡'으로 소통하는 것이 자연스럽습니다.",
        "meaningVi": "Khối xây có lỗ rỗng, được đặt cốt thép bên trong và đổ bê tông để tăng cường độ chịu lực. Phân biệt rõ với gạch xây thường (không cốt thép).",
        "context": "내력벽, 옹벽, 경계벽 등 구조체 시공",
        "culturalNote": "한국에서는 '보강블록'이라는 용어가 일반적이지만, 베트남 현장에서는 'khối gạch rỗng có cốt thép' 또는 'gạch block cốt thép'로 표현합니다. 또한 블록의 규격(200×200×400 등)과 공칭두께를 명시하지 않으면 일반 블록과 혼동될 수 있으므로 주의가 필요합니다. 베트남은 블록보다 벽돌(gạch đỏ)을 더 많이 사용하는 경향이 있어, 보강블록 시공 시 철근 간격과 콘크리트 타설 방법을 현지 인부에게 명확히 설명해야 합니다.",
        "commonMistakes": [
            {
                "mistake": "블록을 'gạch'으로만 번역",
                "correction": "khối gạch 또는 gạch block",
                "explanation": "일반 벽돌과 혼동 방지"
            },
            {
                "mistake": "보강블록과 일반 블록 구분 없이 사용",
                "correction": "khối gạch có cốt thép (보강) vs gạch xây thường (일반)",
                "explanation": "구조적 기능이 다르므로 명확한 구분 필수"
            },
            {
                "mistake": "철근 배근을 '넣는다(bỏ vào)'로만 표현",
                "correction": "đặt cốt thép và đổ bê tông (철근 배치 후 콘크리트 타설)",
                "explanation": "공정 순서를 명시해야 시공 오류 방지"
            }
        ],
        "examples": [
            {
                "ko": "내력벽에는 반드시 보강블록을 사용하세요.",
                "vi": "Tường chịu lực phải dùng khối gạch có cốt thép.",
                "situation": "formal"
            },
            {
                "ko": "보강블록 내부에 D10 철근을 수직으로 배근합니다.",
                "vi": "Đặt cốt thép D10 theo phương thẳng đứng bên trong khối gạch.",
                "situation": "onsite"
            },
            {
                "ko": "블록 내부를 콘크리트로 충전한 후 다음 단을 쌓으세요.",
                "vi": "Sau khi đổ bê tông đầy khối gạch, tiếp tục xây tầng trên.",
                "situation": "onsite"
            }
        ],
        "relatedTerms": ["조적공사", "내력벽", "철근배근", "콘크리트충전"]
    },
    {
        "slug": "xay-gach",
        "korean": "벽돌쌓기",
        "vietnamese": "Xây gạch",
        "hanja": "壁돌쌓기",
        "hanjaReading": "壁(벽 벽) + 돌쌓기(순우리말)",
        "pronunciation": "싸이 자익",
        "meaningKo": "벽돌을 모르타르로 접착하여 벽체를 조성하는 공정입니다. 통역 시 쌓기 방식(영식쌓기, 화란식쌓기 등)과 줄눈 두께, 수평·수직 정렬을 정확히 전달해야 하며, '쌓기(xây)'와 '붙이기(dán)'를 혼동하지 않도록 주의해야 합니다. 특히 한국에서는 줄눈 두께를 10mm로 표준화하는 경우가 많지만, 베트남에서는 15mm까지 허용하는 경우도 있어 규격 확인이 필수입니다.",
        "meaningVi": "Công việc dùng vữa để dán gạch thành tường. Phương pháp xây (xây kiểu Anh, kiểu Hà Lan), độ dày mạch, căn chỉnh ngang dọc là yếu tố quan trọng.",
        "context": "조적공사 전반, 내외벽 시공",
        "culturalNote": "한국에서는 벽돌쌓기를 기능공이 담당하지만, 베트nam에서는 'thợ xây'(조적공)이 벽돌과 블록, 타일까지 통합 시공하는 경우가 많습니다. 또한 한국은 수평·수직 정렬을 엄격히 관리하지만, 베트남 현장에서는 줄눈 두께와 정렬이 다소 느슨할 수 있어 통역 시 '수평계(thước thủy) 사용', '줄눈 두께 10mm 엄수(mạch dày 10mm)'를 명시해야 품질을 확보할 수 있습니다.",
        "commonMistakes": [
            {
                "mistake": "'쌓기'를 'dán'(붙이기)으로 번역",
                "correction": "xây (쌓기)",
                "explanation": "벽돌쌓기는 구조체 형성, 타일붙임은 마감재 부착으로 의미가 다름"
            },
            {
                "mistake": "영식쌓기를 설명 없이 'kiểu Anh'로만 표현",
                "correction": "xây kiểu Anh (gạch ngang và dọc xen kẽ)",
                "explanation": "현지 인부가 이해하도록 쌓기 방식 설명 필요"
            },
            {
                "mistake": "줄눈 두께를 단순히 'dày'로만 표현",
                "correction": "độ dày mạch nối (줄눈 두께) + 수치(mm)",
                "explanation": "정확한 수치 전달로 품질 확보"
            }
        ],
        "examples": [
            {
                "ko": "벽돌을 영식쌓기로 시공하고, 줄눈 두께는 10mm로 맞추세요.",
                "vi": "Xây gạch kiểu Anh, độ dày mạch nối 10mm.",
                "situation": "onsite"
            },
            {
                "ko": "수평계로 수평을 확인하면서 벽돌을 쌓아야 합니다.",
                "vi": "Phải kiểm tra thủy bình bằng thước thủy khi xây gạch.",
                "situation": "formal"
            },
            {
                "ko": "첫 단 벽돌은 정확히 수평을 맞춰 쌓으세요.",
                "vi": "Tầng gạch đầu tiên phải xây thẳng hoàn toàn theo thủy bình.",
                "situation": "onsite"
            }
        ],
        "relatedTerms": ["조적공사", "줄눈", "영식쌓기", "수평계"]
    },
    {
        "slug": "cot-thep-ngang",
        "korean": "가로근",
        "vietnamese": "Cốt thép ngang",
        "hanja": "횡근",
        "hanjaReading": "횫(가로 횡) + 根(뿌리 근)",
        "pronunciation": "꼳 텝 낭",
        "meaningKo": "수평 방향으로 배치되는 철근으로, 보나 슬래브에서 전단력을 분담하거나 벽체에서 수평 보강 역할을 합니다. 통역 시 '가로근(cốt thép ngang)'과 '세로근(cốt thép dọc)'을 명확히 구분하고, 철근 직경(D10, D13 등)과 간격(mm)을 정확히 전달해야 합니다. 주의할 점은 한국에서는 '스터럽(stirrup)'을 가로근의 일종으로 보지만, 베트남에서는 'đai' 또는 'cốt đai'로 별도 구분하는 경우가 많으므로 용어 정리가 필요합니다.",
        "meaningVi": "Cốt thép bố trí theo phương ngang, chịu lực cắt trong dầm, sàn, hoặc gia cố tường theo phương ngang. Phân biệt rõ với cốt thép dọc (thẳng đứng).",
        "context": "철근콘크리트 구조, 벽체 보강, 슬래브 배근",
        "culturalNote": "한국에서는 가로근을 '전단 보강근' 또는 '스터럽'으로 부르기도 하지만, 베트남에서는 'cốt thép ngang'(수평 철근)과 'cốt đai'(띠철근, 스터럽)를 명확히 구분합니다. 통역 시 철근의 기능(전단 보강, 횡방향 구속 등)을 함께 설명하고, 배근 간격과 직경을 명시해야 시공 오류를 방지할 수 있습니다. 또한 베트남은 철근 규격이 다를 수 있으므로 도면과 현장 확인이 필수입니다.",
        "commonMistakes": [
            {
                "mistake": "가로근과 스터럽을 혼용",
                "correction": "가로근은 cốt thép ngang, 스터럽은 cốt đai",
                "explanation": "기능과 형태가 다르므로 구분 필수"
            },
            {
                "mistake": "철근 간격을 '멀리(xa)'로만 표현",
                "correction": "khoảng cách (간격) + 수치(mm)",
                "explanation": "정확한 수치로 시공 정확도 확보"
            },
            {
                "mistake": "철근 직경을 단순히 'dày'(두꺼운)로 표현",
                "correction": "đường kính (직경) + D10, D13 등 규격",
                "explanation": "철근 규격 혼동 방지"
            }
        ],
        "examples": [
            {
                "ko": "보에 D10 가로근을 200mm 간격으로 배근하세요.",
                "vi": "Bố trí cốt thép ngang D10 trong dầm với khoảng cách 200mm.",
                "situation": "onsite"
            },
            {
                "ko": "벽체 가로근은 수직근과 철사로 결속합니다.",
                "vi": "Cốt thép ngang tường buộc với cốt thép dọc bằng dây thép.",
                "situation": "formal"
            },
            {
                "ko": "가로근 간격이 도면과 다르면 감리자에게 보고하세요.",
                "vi": "Nếu khoảng cách cốt thép ngang khác với bản vẽ, báo cáo cho giám sát.",
                "situation": "onsite"
            }
        ],
        "relatedTerms": ["세로근", "철근배근", "스터럽", "전단력"]
    },
    {
        "slug": "cot-thep-doc",
        "korean": "세로근",
        "vietnamese": "Cốt thép dọc",
        "hanja": "종근",
        "hanjaReading": "縱(세로 종) + 根(뿌리 근)",
        "pronunciation": "꼳 텝 족",
        "meaningKo": "수직 또는 길이 방향으로 배치되는 주철근으로, 기둥이나 보에서 압축력과 인장력을 주로 부담합니다. 통역 시 '세로근(cốt thép dọc)'과 '가로근(cốt thép ngang)'을 명확히 구분하고, 주근(cốt chính)과 배력근(cốt phân bố)의 차이를 설명해야 합니다. 특히 베트남 현장에서는 '세로'를 'dọc'(길이 방향) 또는 'thẳng đứng'(수직)으로 표현하는데, 문맥에 따라 달라지므로 주의가 필요합니다.",
        "meaningVi": "Cốt thép bố trí theo phương dọc (thẳng đứng hoặc dọc chiều dài), chịu lực nén và kéo chính trong cột, dầm. Phân biệt rõ với cốt thép ngang và cốt phân bố.",
        "context": "기둥, 보, 벽체의 주요 철근 배근",
        "culturalNote": "한국에서는 '세로근'을 기둥에서는 '주근', 보에서는 '주철근' 또는 '상·하부근'으로 부르지만, 베트남에서는 'cốt thép dọc'으로 통칭하고 위치에 따라 'cốt thép cột'(기둥 철근), 'cốt thép dầm'(보 철근)으로 세분합니다. 통역 시 철근의 위치(상부, 하부, 중앙)와 개수를 명확히 전달하고, 도면 기호(예: 4-D16)를 함께 설명하면 혼선을 줄일 수 있습니다.",
        "commonMistakes": [
            {
                "mistake": "세로근을 '수직(thẳng đứng)'으로만 번역",
                "correction": "cốt thép dọc (길이 방향 철근) 또는 상황에 따라 'thẳng đứng' 병기",
                "explanation": "보에서는 수직이 아니라 길이 방향이므로 문맥 고려 필수"
            },
            {
                "mistake": "주근과 배력근을 구분 없이 'cốt thép dọc'로 통칭",
                "correction": "주근은 cốt chính, 배력근은 cốt phân bố",
                "explanation": "기능이 다르므로 명확한 구분 필요"
            },
            {
                "mistake": "철근 개수를 '많이(nhiều)'로만 표현",
                "correction": "수량 명시 (4 thanh, 6 thanh 등)",
                "explanation": "시공 정확도를 위해 구체적 개수 전달 필수"
            }
        ],
        "examples": [
            {
                "ko": "기둥 세로근은 4-D16으로 배근합니다.",
                "vi": "Cốt thép dọc cột là 4 thanh D16.",
                "situation": "formal"
            },
            {
                "ko": "보 상부에 세로근 3개를 배치하세요.",
                "vi": "Bố trí 3 thanh cốt thép dọc ở phía trên dầm.",
                "situation": "onsite"
            },
            {
                "ko": "세로근과 가로근을 철사로 단단히 결속하세요.",
                "vi": "Buộc chặt cốt thép dọc và cốt thép ngang bằng dây thép.",
                "situation": "onsite"
            }
        ],
        "relatedTerms": ["가로근", "주근", "배력근", "철근배근"]
    },
    {
        "slug": "nut-tuong",
        "korean": "벽체균열",
        "vietnamese": "Nứt tường",
        "hanja": "壁體龜裂",
        "hanjaReading": "壁(벽 벽) + 體(몸 체) + 龜(거북 구) + 裂(찢어질 열)",
        "pronunciation": "늣 뜨엉",
        "meaningKo": "벽체에 발생하는 균열로, 건조수축, 온도변화, 구조적 결함 등이 원인입니다. 통역 시 균열의 종류(헤어크랙, 구조균열)와 폭(mm), 방향(수평, 수직, 사선)을 정확히 전달해야 하며, 단순 미장 균열과 구조 균열을 혼동하지 않도록 주의해야 합니다. 베트남 현장에서는 균열을 'nứt'(갈라짐), 'vết nứt'(균열 자국), 'vết rạn'(미세균열)로 구분하므로, 상황에 맞게 용어를 선택해야 정확한 소통이 가능합니다.",
        "meaningVi": "Vết nứt trên tường do co ngót, thay đổi nhiệt độ, hoặc khuyết tật kết cấu. Phân loại: nứt tóc (hairline crack), nứt kết cấu (structural crack), và ghi rõ chiều rộng (mm), hướng (ngang, dọc, chéo).",
        "context": "구조 안전 점검, 하자 보수, 품질 관리",
        "culturalNote": "한국에서는 균열 폭 0.3mm 이상을 구조 균열로 보고 보수가 필요하지만, 베트남에서는 기준이 다를 수 있어 현지 규정을 확인해야 합니다. 또한 한국은 균열 보수를 전문 업체에 맡기지만, 베트남은 일반 미장공이 처리하는 경우가 많아 보수 방법(에폭시 주입, U컷 실링 등)을 명확히 지시해야 재발을 방지할 수 있습니다. 통역 시 '헤어크랙(nứt tóc)'과 '구조균열(nứt kết cấu)'을 구분하는 것이 핵심입니다.",
        "commonMistakes": [
            {
                "mistake": "모든 균열을 'nứt'로만 번역",
                "correction": "미세균열(nứt tóc), 구조균열(nứt kết cấu) 구분",
                "explanation": "보수 방법과 긴급도가 다르므로 분류 필수"
            },
            {
                "mistake": "균열 폭을 '크다(lớn)'로만 표현",
                "correction": "chiều rộng vết nứt (균열 폭) + 수치(mm)",
                "explanation": "정확한 측정값으로 심각도 판단"
            },
            {
                "mistake": "균열 원인을 설명 없이 넘김",
                "correction": "do co ngót (건조수축), do nhiệt độ (온도), do kết cấu (구조)",
                "explanation": "원인 파악으로 재발 방지 대책 수립 가능"
            }
        ],
        "examples": [
            {
                "ko": "벽체에 폭 0.5mm의 수직 균열이 발견되었습니다.",
                "vi": "Phát hiện vết nứt dọc rộng 0.5mm trên tường.",
                "situation": "formal"
            },
            {
                "ko": "헤어크랙은 미장 보수로 처리하고, 구조균열은 에폭시 주입하세요.",
                "vi": "Nứt tóc xử lý bằng vữa trét, nứt kết cấu bơm epoxy.",
                "situation": "onsite"
            },
            {
                "ko": "균열 발생 위치와 방향을 사진으로 기록하세요.",
                "vi": "Chụp ảnh ghi lại vị trí và hướng vết nứt.",
                "situation": "formal"
            }
        ],
        "relatedTerms": ["헤어크랙", "구조균열", "에폭시주입", "미장보수"]
    },
    {
        "slug": "rot-mach-noi",
        "korean": "줄눈채움",
        "vietnamese": "Rót mạch nối",
        "hanja": "줄눈充塡",
        "hanjaReading": "줄눈(순우리말) + 充(채울 충) + 塡(메울 전)",
        "pronunciation": "족 마익 노이",
        "meaningKo": "벽돌이나 블록, 타일 사이의 줄눈을 모르타르 또는 실링재로 채우는 작업입니다. 통역 시 '줄눈채움(rót mạch)'과 '줄눈치기(trét mạch)'를 구분하고, 채움재의 종류(시멘트 모르타르, 실링재, 그라우트)를 명확히 전달해야 합니다. 베트남 현장에서는 'rót'(붓다)와 'trét'(바르다)를 혼용하는 경우가 많아, 작업 방법을 구체적으로 설명해야 실수를 방지할 수 있습니다.",
        "meaningVi": "Công việc đổ đầy vữa hoặc vật liệu trám kín vào mạch nối giữa gạch, block, gạch ốp. Phân biệt rõ rót mạch (đổ đầy) và trét mạch (phủ bề mặt).",
        "context": "조적공사, 타일공사, 방수공사",
        "culturalNote": "한국에서는 줄눈채움과 줄눈치기를 공정으로 명확히 분리하지만, 베트남에서는 'rót mạch'(줄눈 채우기)로 통칭하는 경우가 많습니다. 통역 시 시멘트 모르타르로 채우는 것(rót vữa xi măng)과 실링재로 마감하는 것(trám kín bằng silicone)을 구분하고, 외벽 방수 줄눈은 'mạch chống thấm'으로 명시해야 혼선을 줄일 수 있습니다. 또한 줄눈 두께와 깊이를 정확히 전달해야 품질을 확보할 수 있습니다.",
        "commonMistakes": [
            {
                "mistake": "줄눈채움을 'trét'(바르기)로만 번역",
                "correction": "rót mạch (채움) vs trét mạch (마감)",
                "explanation": "작업 공정이 다르므로 구분 필수"
            },
            {
                "mistake": "채움재를 명시하지 않고 '모르타르'로만 표현",
                "correction": "vữa xi măng (시멘트 모르타르), silicone (실링재), vữa trám (그라우트)",
                "explanation": "용도에 따라 재료가 다르므로 정확한 지정 필요"
            },
            {
                "mistake": "줄눈 깊이를 '깊게(sâu)'로만 표현",
                "correction": "độ sâu mạch (줄눈 깊이) + 수치(mm)",
                "explanation": "정확한 수치로 시공 품질 확보"
            }
        ],
        "examples": [
            {
                "ko": "벽돌 줄눈을 시멘트 모르타르로 채우세요.",
                "vi": "Rót mạch nối gạch bằng vữa xi măng.",
                "situation": "onsite"
            },
            {
                "ko": "타일 줄눈은 방수 그라우트를 사용합니다.",
                "vi": "Mạch nối gạch ốp dùng vữa trám chống thấm.",
                "situation": "formal"
            },
            {
                "ko": "외벽 줄눈은 실링재로 마감하여 방수 처리하세요.",
                "vi": "Hoàn thiện mạch nối tường ngoài bằng silicone chống thấm.",
                "situation": "formal"
            }
        ],
        "relatedTerms": ["줄눈", "줄눈치기", "그라우트", "실링재"]
    },
    {
        "slug": "tuong-chong",
        "korean": "부벽",
        "vietnamese": "Tường chống",
        "hanja": "扶壁",
        "hanjaReading": "扶(도울 부) + 壁(벽 벽)",
        "pronunciation": "뜨엉 총",
        "meaningKo": "벽체의 횡방향 하중을 지지하거나 안정성을 높이기 위해 벽면에 수직으로 설치하는 보강 구조입니다. 통역 시 '부벽(tường chống)'과 '옹벽(tường chắn)'을 혼동하지 않도록 주의하고, 부벽의 위치(내부/외부), 간격, 두께를 명확히 전달해야 합니다. 베트남 현장에서는 부벽을 'tường đỡ' 또는 'tường gia cố'로도 부르므로, 도면과 함께 설명하면 이해가 빠릅니다.",
        "meaningVi": "Kết cấu tường đứng vuông góc với tường chính để chống đỡ tải trọng ngang và tăng ổn định. Phân biệt rõ với tường chắn (retaining wall).",
        "context": "높은 벽체, 옹벽, 저수조 등의 구조 보강",
        "culturalNote": "한국에서는 '부벽'이라는 용어가 명확하지만, 베트남에서는 'tường chống'(지지벽), 'tường đỡ'(받침벽), 'tường gia cố'(보강벽)로 다양하게 표현합니다. 통역 시 부벽의 기능(횡방향 지지, 전도 방지)을 설명하고, 옹벽(tường chắn đất)과 혼동하지 않도록 '지지용 보강벽(tường đỡ gia cố)'으로 부연 설명하는 것이 효과적입니다. 또한 부벽 간격과 두께를 도면 기준으로 정확히 전달해야 시공 오류를 방지할 수 있습니다.",
        "commonMistakes": [
            {
                "mistake": "부벽을 옹벽(tường chắn)으로 혼동",
                "correction": "부벽은 tường chống/tường đỡ, 옹벽은 tường chắn đất",
                "explanation": "기능과 설치 위치가 다름"
            },
            {
                "mistake": "부벽 위치를 '옆(bên)'으로만 표현",
                "correction": "tường chống vuông góc với tường chính (주벽에 수직)",
                "explanation": "정확한 위치 관계 전달로 시공 오류 방지"
            },
            {
                "mistake": "부벽 간격을 '멀리(xa)'로만 표현",
                "correction": "khoảng cách giữa các tường chống (부벽 간 간격) + 수치(m)",
                "explanation": "구조 안정성을 위해 정확한 간격 명시 필수"
            }
        ],
        "examples": [
            {
                "ko": "3m 높이 벽에는 2m 간격으로 부벽을 설치하세요.",
                "vi": "Tường cao 3m cần đặt tường chống cách nhau 2m.",
                "situation": "formal"
            },
            {
                "ko": "부벽 두께는 주벽의 1/3 이상으로 하세요.",
                "vi": "Độ dày tường chống phải từ 1/3 độ dày tường chính trở lên.",
                "situation": "formal"
            },
            {
                "ko": "외부에 노출된 부벽은 방수 처리가 필요합니다.",
                "vi": "Tường chống phía ngoài cần xử lý chống thấm.",
                "situation": "onsite"
            }
        ],
        "relatedTerms": ["옹벽", "횡력", "구조보강", "전도방지"]
    },
    {
        "slug": "tuong-chiu-luc",
        "korean": "내력벽",
        "vietnamese": "Tường chịu lực",
        "hanja": "耐力壁",
        "hanjaReading": "耐(견딜 내) + 力(힘 력) + 壁(벽 벽)",
        "pronunciation": "뜨엉 찌우 릭",
        "meaningKo": "건물의 수직 하중과 수평 하중을 지지하는 구조벽으로, 제거하거나 개구부를 만들 때 구조 검토가 필수입니다. 통역 시 '내력벽(tường chịu lực)'과 '비내력벽(tường ngăn, 칸막이벽)'을 명확히 구분하고, 철거나 개구부 설치 시 구조 보강 방법을 정확히 전달해야 합니다. 베트남 현장에서는 내력벽을 임의로 철거하는 사례가 많아, 통역 시 '구조 안전 검토 필수(kiểm tra kết cấu bắt buộc)'를 강조해야 안전사고를 예방할 수 있습니다.",
        "meaningVi": "Tường kết cấu chịu tải trọng đứng và ngang của công trình. Không được phá dỡ hoặc khoét lỗ khi chưa kiểm tra kết cấu. Phân biệt rõ với tường ngăn (không chịu lực).",
        "context": "구조 설계, 리모델링, 증축 공사",
        "culturalNote": "한국에서는 내력벽 철거 시 구조 기술사의 검토와 승인을 받지만, 베트남에서는 이러한 절차가 덜 엄격할 수 있어 통역 시 '반드시 구조 엔지니어 승인(phải được kỹ sư kết cấu phê duyệt)'을 명시해야 합니다. 또한 내력벽과 비내력벽을 구분하지 못하는 경우가 많으므로, 도면에서 'tường chịu lực'로 표시된 벽은 철거 금지임을 반복 강조하고, 개구부 설치 시 보(dầm) 또는 린텔(lintel) 보강이 필수임을 전달해야 합니다.",
        "commonMistakes": [
            {
                "mistake": "내력벽을 단순히 'tường'(벽)으로만 번역",
                "correction": "tường chịu lực (내력벽) vs tường ngăn (비내력벽/칸막이)",
                "explanation": "구조적 역할이 다르므로 명확한 구분 필수"
            },
            {
                "mistake": "철거 가능 여부를 명시하지 않음",
                "correction": "không được phá dỡ (철거 금지) 또는 cần kiểm tra kết cấu (검토 필수)",
                "explanation": "안전사고 예방을 위해 철거 제한 명시 필요"
            },
            {
                "mistake": "개구부 설치 시 보강 방법 미고지",
                "correction": "cần đặt dầm hoặc lintel (보 또는 린텔 설치 필수)",
                "explanation": "개구부 상부 하중 지지 방법 명시로 구조 안전 확보"
            }
        ],
        "examples": [
            {
                "ko": "이 벽은 내력벽이므로 임의로 철거할 수 없습니다.",
                "vi": "Tường này là tường chịu lực, không được phá dỡ tùy ý.",
                "situation": "formal"
            },
            {
                "ko": "내력벽에 문을 만들려면 상부에 보를 설치해야 합니다.",
                "vi": "Muốn khoét cửa trên tường chịu lực, phải đặt dầm phía trên.",
                "situation": "onsite"
            },
            {
                "ko": "리모델링 전에 내력벽 위치를 도면으로 확인하세요.",
                "vi": "Trước khi cải tạo, kiểm tra vị trí tường chịu lực trên bản vẽ.",
                "situation": "formal"
            }
        ],
        "relatedTerms": ["비내력벽", "구조벽", "보강", "린텔"]
    }
]

# 파일 경로
file_path = os.path.join(
    os.path.dirname(__file__),
    "..",
    "data",
    "terms",
    "construction.json"
)

# 기존 데이터 읽기
with open(file_path, "r", encoding="utf-8") as f:
    existing_data = json.load(f)

# 신규 용어 추가
existing_data.extend(data)

# 저장
with open(file_path, "w", encoding="utf-8") as f:
    json.dump(existing_data, f, ensure_ascii=False, indent=2)

print(f"✅ {len(data)}개 용어 추가 완료: {file_path}")
print("추가된 용어:")
for term in data:
    print(f"  - {term['korean']} ({term['vietnamese']})")
