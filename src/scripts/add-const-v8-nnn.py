#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Construction 용어 추가 스크립트 v8: 특수구조/대공간 테마
- 쉘구조, 막구조, 케이블구조, 돔, 아치, 공간트러스, 현수구조, 사장교, 면진구조, 제진장치
"""

import os
import json

# Tier S 기준: 10개 특수구조/대공간 용어
data = [
    {
        "slug": "ket-cau-vo",
        "korean": "쉘구조",
        "vietnamese": "Kết cấu vỏ",
        "hanja": "殼構造",
        "hanjaReading": "殼(껍질 각) + 構(얽을 구) + 造(지을 조)",
        "pronunciation": "껏꾸쩌우 버",
        "meaningKo": "얇은 곡면판으로 이루어진 구조로, 형태 자체가 하중을 지탱하는 시스템. 콘크리트 쉘, 강재 쉘 등이 있으며, 최소 재료로 넓은 공간을 덮을 수 있어 체육관, 전시장, 극장 등 대공간 건축에 주로 사용됩니다. 통역 시 '얇은 껍질처럼 생긴 구조'라고 설명하면 이해가 빠릅니다. 시공 난이도가 높아 전문 기술이 필요하며, 설계 단계부터 면밀한 구조 검토가 필수입니다.",
        "meaningVi": "Kết cấu tấm cong mỏng chịu lực nhờ hình dạng của nó, được dùng cho không gian lớn như nhà thi đấu, nhà triển lãm. Vật liệu thường là bê tông hoặc thép.",
        "context": "특수구조 설계 및 대공간 건축 시공",
        "culturalNote": "한국에서는 1970-80년대 대형 체육시설(올림픽 경기장 등) 건설 시 도입되어 '쉘구조', '쉘 지붕'이라는 용어가 정착했습니다. 베트남에서는 현대식 전시장, 공항 터미널 등에 적용되며 'vỏ mỏng' (얇은 껍질)이라는 설명을 덧붙이면 현장 이해도가 높아집니다. 통역 시 '형태가 구조'라는 개념을 강조하세요.",
        "commonMistakes": [
            {
                "mistake": "Vỏ kết cấu (어순 오류)",
                "correction": "Kết cấu vỏ",
                "explanation": "베트남어는 명사+수식어 순서. '구조'가 중심 명사, '쉘/껍질'이 수식어입니다."
            },
            {
                "mistake": "'Shell structure'를 '조개껍질 구조'로 직역",
                "correction": "곡면 구조 시스템으로 설명",
                "explanation": "엔지니어가 아닌 일반 관계자에게는 '조개껍질 모양' 설명이 오해를 부릅니다."
            },
            {
                "mistake": "Kết cấu mỏng (얇은 구조) - 불충분한 표현",
                "correction": "Kết cấu vỏ (쉘구조) 또는 Kết cấu tấm cong",
                "explanation": "'얇다'는 특징만 강조하면 구조 방식을 오인할 수 있습니다."
            }
        ],
        "examples": [
            {
                "ko": "이 전시장은 철근콘크리트 쉘구조로 설계되어 중간 기둥 없이 넓은 공간을 확보했습니다.",
                "vi": "Nhà triển lãm này được thiết kế bằng kết cấu vỏ bê tông cốt thép, không cần cột giữa để tạo không gian rộng.",
                "situation": "formal"
            },
            {
                "ko": "쉘구조 시공 시 거푸집 정밀도가 매우 중요합니다.",
                "vi": "Khi thi công kết cấu vỏ, độ chính xác của ván khuôn rất quan trọng.",
                "situation": "onsite"
            },
            {
                "ko": "곡률 반경이 작을수록 쉘구조의 강성이 증가합니다.",
                "vi": "Bán kính cong càng nhỏ thì độ cứng của kết cấu vỹ càng tăng.",
                "situation": "formal"
            }
        ],
        "relatedTerms": ["막구조 (kết cấu màng)", "공간트러스 (dàn không gian)", "현수구조 (kết cấu treo)", "대공간구조 (kết cấu không gian lớn)"]
    },
    {
        "slug": "ket-cau-mang",
        "korean": "막구조",
        "vietnamese": "Kết cấu màng",
        "hanja": "膜構造",
        "hanjaReading": "膜(얇은 막 막) + 構(얽을 구) + 造(지을 조)",
        "pronunciation": "껏꾸쩌우 망",
        "meaningKo": "직물이나 필름 등 막재료를 인장력으로 지지하여 공간을 덮는 구조. 경량이며 자유로운 형태 구현이 가능해 스타디움, 전시장, 임시 구조물 등에 활용됩니다. 통역 시 '천막처럼 당겨서 지탱하는 구조'라고 설명하면 직관적입니다. 막재의 내구성, 방화성능, 인장강도 등이 설계의 핵심 요소이며, 유지보수 계획도 중요합니다.",
        "meaningVi": "Kết cấu sử dụng vật liệu màng (vải, màng phủ) được căng bằng lực kéo để che phủ không gian. Nhẹ, linh hoạt, dùng cho sân vận động, nhà triển lãm.",
        "context": "특수구조 설계 및 대공간/임시 건축",
        "culturalNote": "한국에서는 2002 월드컵 경기장(수원 등) 지붕에 막구조가 적용되며 대중화되었고, '막구조', '텐트구조'라는 용어가 혼용됩니다. 베트남에서는 'kết cấu màng'이 정식 용어이나, 현장에서는 'mái bạt căng' (텐트 지붕)으로 설명하기도 합니다. 통역 시 재질(PTFE, ETFE 등)을 구체적으로 명시하세요.",
        "commonMistakes": [
            {
                "mistake": "Cấu trúc màng (구조 막 - 어순 오류)",
                "correction": "Kết cấu màng",
                "explanation": "'Kết cấu'가 명사, 'màng'이 수식어. 베트남어 어순을 따라야 합니다."
            },
            {
                "mistake": "막구조를 '천막'으로만 번역",
                "correction": "인장막 구조 시스템으로 설명",
                "explanation": "단순 천막이 아닌 고강도 막재 + 구조 시스템임을 명확히 해야 합니다."
            },
            {
                "mistake": "Kết cấu vải (직물 구조) - 재질만 강조",
                "correction": "Kết cấu màng căng (인장막 구조)",
                "explanation": "'인장력'이 핵심이므로 'căng' (당기다) 개념을 포함해야 합니다."
            }
        ],
        "examples": [
            {
                "ko": "이 야외 공연장은 PTFE 막구조로 설계되어 자연채광과 차양을 동시에 해결했습니다.",
                "vi": "Nhà hát ngoài trời này được thiết kế bằng kết cấu màng PTFE, giải quyết đồng thời ánh sáng tự nhiên và che bóng.",
                "situation": "formal"
            },
            {
                "ko": "막구조 시공 전 막재 인장강도 시험이 필수입니다.",
                "vi": "Trước khi thi công kết cấu màng, phải kiểm tra cường độ kéo của vật liệu màng.",
                "situation": "onsite"
            },
            {
                "ko": "막구조는 경량이라 기초 하중이 작아 공사비를 절감할 수 있습니다.",
                "vi": "Kết cấu màng nhẹ nên tải trọng móng nhỏ, giúp tiết kiệm chi phí xây dựng.",
                "situation": "formal"
            }
        ],
        "relatedTerms": ["쉘구조 (kết cấu vỏ)", "케이블구조 (kết cấu cáp)", "공간트러스 (dàn không gian)", "PTFE막 (màng PTFE)"]
    },
    {
        "slug": "ket-cau-cap",
        "korean": "케이블구조",
        "vietnamese": "Kết cấu cáp",
        "hanja": None,
        "hanjaReading": None,
        "pronunciation": "껏꾸쩌우 깝",
        "meaningKo": "강재 케이블을 주요 구조재로 사용하여 인장력으로 하중을 지탱하는 구조. 현수교, 사장교, 케이블 지붕 등이 대표적이며, 경량이면서도 큰 스팬을 구현할 수 있어 대공간 건축과 교량에 널리 쓰입니다. 통역 시 '강철 줄로 매달아 지탱하는 구조'라고 설명하면 이해가 빠릅니다. 케이블 장력 관리와 부식 방지가 유지보수의 핵심입니다.",
        "meaningVi": "Kết cấu sử dụng cáp thép làm bộ phận chịu lực chính, chịu kéo để đỡ tải. Dùng cho cầu treo, mái nhà lớn, không gian rộng.",
        "context": "특수구조 설계, 교량 및 대공간 건축",
        "culturalNote": "한국에서는 인천대교, 이순신대교 등 대형 사장교 건설이 활발하며 '케이블구조', '케이블 지붕'이라는 용어가 일반화되었습니다. 베트남에서는 'cầu dây văng' (사장교), 'kết cấu cáp'이 표준 용어이며, 통역 시 'cáp thép' (강재 케이블)을 명시하면 명확합니다. 장력 조정(căng lực cáp)이 시공의 핵심입니다.",
        "commonMistakes": [
            {
                "mistake": "Kết cấu dây (줄 구조) - 모호한 표현",
                "correction": "Kết cấu cáp (케이블구조)",
                "explanation": "'dây'는 일반 줄, 'cáp'은 강재 케이블. 구조용은 반드시 'cáp'을 사용해야 합니다."
            },
            {
                "mistake": "케이블을 '전선'으로 오인",
                "correction": "구조용 강재 케이블로 명확히 설명",
                "explanation": "전기 케이블과 혼동되지 않도록 'cáp kết cấu' (구조 케이블)로 표현하세요."
            },
            {
                "mistake": "Cấu trúc cáp (구조 케이블 - 어순 오류)",
                "correction": "Kết cấu cáp",
                "explanation": "베트남어 어순은 명사(kết cấu) + 수식어(cáp) 입니다."
            }
        ],
        "examples": [
            {
                "ko": "이 체육관 지붕은 방사형 케이블구조로 설계되어 중앙 기둥 없이 넓은 공간을 확보했습니다.",
                "vi": "Mái nhà thể thao này được thiết kế bằng kết cấu cáp hình tia, không cần cột giữa để tạo không gian rộng.",
                "situation": "formal"
            },
            {
                "ko": "케이블구조 시공 시 케이블 장력 조정이 매우 중요합니다.",
                "vi": "Khi thi công kết cấu cáp, việc điều chỉnh lực căng cáp rất quan trọng.",
                "situation": "onsite"
            },
            {
                "ko": "현수교는 대표적인 케이블구조 교량입니다.",
                "vi": "Cầu treo là loại cầu kết cấu cáp điển hình.",
                "situation": "formal"
            }
        ],
        "relatedTerms": ["현수구조 (kết cấu treo)", "사장교 (cầu dây văng)", "막구조 (kết cấu màng)", "공간트러스 (dàn không gian)"]
    },
    {
        "slug": "mam-dom",
        "korean": "돔",
        "vietnamese": "Mái vòm (Dome)",
        "hanja": None,
        "hanjaReading": None,
        "pronunciation": "마이 붐 (돔)",
        "meaningKo": "반구형 또는 곡면 지붕 구조로, 하중이 곡면을 따라 기초로 전달되어 넓은 무주공간을 만들 수 있는 구조. 콘크리트, 강재, 목재 등 다양한 재료로 시공 가능하며, 체육관, 천문관, 전시장 등에 주로 사용됩니다. 통역 시 '반구 모양 지붕'이라고 설명하면 직관적입니다. 형태 자체가 구조적 안정성을 제공하여 재료 효율이 높습니다.",
        "meaningVi": "Mái hình bán cầu hoặc vòm cong, tải trọng truyền qua bề mặt cong xuống móng, tạo không gian rộng không cột. Dùng cho nhà thi đấu, bảo tàng, triển lãm.",
        "context": "대공간 건축 설계 및 특수구조",
        "culturalNote": "한국에서는 '돔 경기장', '돔 지붕'이라는 용어가 일반화되어 있고, 잠실 야구장 등 대형 스포츠 시설에 적용되었습니다. 베트남에서는 'mái vòm' (둥근 지붕)이 일반 용어이나, 전문 분야에서는 'dome' 영어 표현도 병기합니다. 통역 시 구조 방식(쉘, 트러스, 막 등)을 함께 명시하세요.",
        "commonMistakes": [
            {
                "mistake": "Vòm (아치만 지칭)",
                "correction": "Mái vòm (dome, 돔)",
                "explanation": "'Vòm'은 아치 일반, 'mái vòm'은 지붕 돔. 문맥에 따라 구분해야 합니다."
            },
            {
                "mistake": "돔을 '둥근 지붕'으로만 설명",
                "correction": "반구형 구조 시스템으로 설명",
                "explanation": "단순 형태가 아닌 구조 원리를 설명해야 엔지니어에게 명확합니다."
            },
            {
                "mistake": "Mái bán cầu (반구 지붕) - 너무 직역",
                "correction": "Mái vòm (dome) 또는 Kết cấu vòm",
                "explanation": "'Mái vòm'이 표준 용어이며, 현장에서 통용됩니다."
            }
        ],
        "examples": [
            {
                "ko": "이 전시장은 철골 트러스 돔 구조로 설계되어 100m 스팬을 실현했습니다.",
                "vi": "Nhà triển lãm này được thiết kế bằng kết cấu mái vòm dàn thép, đạt nhịp 100m.",
                "situation": "formal"
            },
            {
                "ko": "돔 구조는 지진에 강하고 내구성이 뛰어납니다.",
                "vi": "Kết cấu mái vòm chống động đất tốt và bền vững.",
                "situation": "formal"
            },
            {
                "ko": "돔 시공 시 중앙부터 원형으로 확장하는 공법을 사용합니다.",
                "vi": "Khi thi công mái vòm, dùng phương pháp mở rộng từ trung tâm ra xung quanh.",
                "situation": "onsite"
            }
        ],
        "relatedTerms": ["쉘구조 (kết cấu vỏ)", "공간트러스 (dàn không gian)", "아치구조 (kết cấu vòm)", "대공간구조 (kết cấu không gian lớn)"]
    },
    {
        "slug": "ket-cau-vom",
        "korean": "아치구조",
        "vietnamese": "Kết cấu vòm (Arch)",
        "hanja": None,
        "hanjaReading": None,
        "pronunciation": "껏꾸쩌우 붐 (아치)",
        "meaningKo": "곡선 형태로 하중을 지탱하는 구조로, 압축력을 통해 하중을 양단 기초로 전달합니다. 교량, 터널, 건축물 입구 등에 사용되며, 석재, 콘크리트, 강재 등으로 시공 가능합니다. 통역 시 '무지개 모양 구조'라고 설명하면 직관적이며, 압축력 집중으로 인한 기초 설계가 중요함을 강조하세요. 역사적으로 오랜 기간 검증된 구조 방식입니다.",
        "meaningVi": "Kết cấu hình cong chịu lực nén, truyền tải xuống hai đầu móng. Dùng cho cầu, hầm, cổng vào, chịu lực nén tốt.",
        "context": "교량, 터널, 건축물 입구 설계",
        "culturalNote": "한국에서는 '아치교', '아치형 입구'라는 표현이 일반적이며, 석조 아치, 콘크리트 아치 등으로 구분합니다. 베트남에서는 'kết cấu vòm' (아치구조), 'cầu vòm' (아치교)이 표준 용어이며, 통역 시 '압축력 전달'(lực nén truyền xuống)을 강조하세요. 기초부의 수평력 처리가 설계 핵심입니다.",
        "commonMistakes": [
            {
                "mistake": "Vòm (아치 일반)",
                "correction": "Kết cấu vòm (아치구조)",
                "explanation": "'Vòm'만으로는 구조 시스템인지 형태인지 불명확. 'kết cấu'를 붙여야 합니다."
            },
            {
                "mistake": "아치를 '둥근 모양'으로만 설명",
                "correction": "압축력 전달 시스템으로 설명",
                "explanation": "형태가 아닌 구조 원리(압축력)를 명확히 해야 합니다."
            },
            {
                "mistake": "Kết cấu cong (곡선 구조) - 모호함",
                "correction": "Kết cấu vòm (아치구조)",
                "explanation": "'vòm'이 표준 용어이며, 'cong'은 단순 곡선을 의미합니다."
            }
        ],
        "examples": [
            {
                "ko": "이 다리는 3경간 연속 아치구조로 설계되어 경관과 구조적 안정성을 동시에 확보했습니다.",
                "vi": "Cầu này được thiết kế bằng kết cấu vòm liên tục 3 nhịp, đảm bảo đồng thời cảnh quan và ổn định kết cấu.",
                "situation": "formal"
            },
            {
                "ko": "아치구조는 기초에 큰 수평력이 작용하므로 지반 조사가 필수입니다.",
                "vi": "Kết cấu vòm tác dụng lực ngang lớn lên móng, nên khảo sát nền đất là bắt buộc.",
                "situation": "onsite"
            },
            {
                "ko": "석조 아치는 수백 년간 유지될 수 있는 내구성이 있습니다.",
                "vi": "Vòm đá có độ bền có thể duy trì hàng trăm năm.",
                "situation": "formal"
            }
        ],
        "relatedTerms": ["돔 (mái vòm dome)", "쉘구조 (kết cấu vỏ)", "압축력 (lực nén)", "교량구조 (kết cấu cầu)"]
    },
    {
        "slug": "dan-khong-gian",
        "korean": "공간트러스",
        "vietnamese": "Dàn không gian",
        "hanja": "空間truss",
        "hanjaReading": "空(빌 공) + 間(사이 간)",
        "pronunciation": "잔 콩잔",
        "meaningKo": "3차원 입체 형태로 조립된 트러스 구조로, 평면 트러스보다 큰 강성과 하중 분산 능력을 가지며 대공간 지붕에 주로 사용됩니다. 체육관, 전시장, 공항 터미널 등에 적용되며, 통역 시 '입체 철골 뼈대'라고 설명하면 이해가 빠릅니다. 부재 수가 많아 접합부 설계와 시공 정밀도가 중요하며, 경량이면서도 큰 스팬을 구현할 수 있는 장점이 있습니다.",
        "meaningVi": "Dàn kết cấu lắp ghép không gian 3 chiều, có độ cứng và khả năng phân tán tải lớn hơn dàn phẳng. Dùng cho mái nhà lớn, sân bay, nhà thi đấu.",
        "context": "대공간 건축 지붕 구조 설계",
        "culturalNote": "한국에서는 1980년대 대형 체육시설(올림픽 체조경기장 등) 건설 시 공간트러스가 도입되어 '공간 트러스', '스페이스 프레임'이라는 용어가 혼용됩니다. 베트남에서는 'dàn không gian'이 표준 용어이며, 통역 시 'dàn 3D' (3차원 트러스)로 쉽게 설명할 수 있습니다. 볼트 접합부(mối nối bu lông) 시공 정밀도가 핵심입니다.",
        "commonMistakes": [
            {
                "mistake": "Dàn 3 chiều (3차원 트러스) - 직역",
                "correction": "Dàn không gian (공간트러스)",
                "explanation": "'Dàn không gian'이 표준 용어이며, 현장에서 통용됩니다."
            },
            {
                "mistake": "Space frame을 '공간 틀'로 번역",
                "correction": "공간트러스 또는 입체 트러스로 설명",
                "explanation": "'틀'은 모호한 표현. 트러스 구조 시스템임을 명확히 해야 합니다."
            },
            {
                "mistake": "Dàn không (공기 트러스) - 오타",
                "correction": "Dàn không gian (공간트러스)",
                "explanation": "'gian' (간, 사이)을 빼먹으면 의미가 완전히 달라집니다."
            }
        ],
        "examples": [
            {
                "ko": "이 체육관 지붕은 더블레이어 공간트러스로 설계되어 80m 무주공간을 실현했습니다.",
                "vi": "Mái nhà thể thao này được thiết kế bằng dàn không gian hai lớp, đạt không gian không cột 80m.",
                "situation": "formal"
            },
            {
                "ko": "공간트러스 시공 시 볼트 조임 순서가 변형 방지의 핵심입니다.",
                "vi": "Khi thi công dàn không gian, thứ tự xiết bu lông là yếu tố then chốt để tránh biến dạng.",
                "situation": "onsite"
            },
            {
                "ko": "공간트러스는 평면 트러스보다 30% 이상 가벼우면서도 강성이 높습니다.",
                "vi": "Dàn không gian nhẹ hơn dàn phẳng 30% nhưng độ cứng cao hơn.",
                "situation": "formal"
            }
        ],
        "relatedTerms": ["평면트러스 (dàn phẳng)", "쉘구조 (kết cấu vỏ)", "막구조 (kết cấu màng)", "대공간구조 (kết cấu không gian lớn)"]
    },
    {
        "slug": "ket-cau-treo",
        "korean": "현수구조",
        "vietnamese": "Kết cấu treo",
        "hanja": "懸垂構造",
        "hanjaReading": "懸(매달 현) + 垂(드리울 수) + 構(얽을 구) + 造(지을 조)",
        "pronunciation": "껏꾸쩌우 쩨오",
        "meaningKo": "케이블이나 강재를 매달아 인장력으로 하중을 지탱하는 구조. 현수교가 대표적이며, 건축에서는 지붕이나 플로어를 케이블로 매달아 지지하는 방식으로 사용됩니다. 통역 시 '매달아서 지탱하는 구조'라고 설명하면 직관적이며, 케이블 장력 관리와 풍하중 대응이 설계의 핵심입니다. 경량이면서도 장스팬 구현이 가능합니다.",
        "meaningVi": "Kết cấu treo bằng cáp hoặc thanh thép, chịu lực kéo để đỡ tải. Dùng cho cầu treo, mái nhà hoặc sàn treo.",
        "context": "교량 및 대공간 건축 설계",
        "culturalNote": "한국에서는 '현수교', '현수 지붕'이라는 용어가 일반적이며, 광안대교 등 대형 교량에 적용되었습니다. 베트남에서는 'kết cấu treo', 'cầu treo'가 표준 용어이며, 통역 시 'treo bằng cáp' (케이블로 매달다)를 강조하세요. 풍하중(tải trọng gió)에 대한 처리가 중요합니다.",
        "commonMistakes": [
            {
                "mistake": "Kết cấu treo (매달다) vs Kết cấu cáp (케이블) 혼동",
                "correction": "현수구조 = kết cấu treo, 케이블구조 = kết cấu cáp",
                "explanation": "현수는 매달림 방식, 케이블은 재료. 문맥에 따라 구분해야 합니다."
            },
            {
                "mistake": "Treo (매달다)만으로 표현 - 불충분",
                "correction": "Kết cấu treo (현수구조)",
                "explanation": "동사만으로는 구조 시스템인지 불명확. 'kết cấu'를 붙여야 합니다."
            },
            {
                "mistake": "현수교를 '줄다리'로 비유",
                "correction": "인장 케이블 시스템으로 설명",
                "explanation": "비유보다는 구조 원리를 정확히 설명해야 엔지니어에게 명확합니다."
            }
        ],
        "examples": [
            {
                "ko": "이 다리는 주케이블로 상판을 매달아 지지하는 현수구조입니다.",
                "vi": "Cầu này là kết cấu treo, mặt cầu được đỡ bằng cáp chính.",
                "situation": "formal"
            },
            {
                "ko": "현수구조 시공 시 케이블 장력 조정과 앵커리지 설계가 핵심입니다.",
                "vi": "Khi thi công kết cấu treo, điều chỉnh lực căng cáp và thiết kế neo cáp là then chốt.",
                "situation": "onsite"
            },
            {
                "ko": "현수교는 세계에서 가장 긴 스팬의 교량 형식입니다.",
                "vi": "Cầu treo là loại cầu có nhịp dài nhất thế giới.",
                "situation": "formal"
            }
        ],
        "relatedTerms": ["케이블구조 (kết cấu cáp)", "사장교 (cầu dây văng)", "인장력 (lực kéo)", "교량구조 (kết cấu cầu)"]
    },
    {
        "slug": "cau-day-vang",
        "korean": "사장교",
        "vietnamese": "Cầu dây văng",
        "hanja": "斜張橋",
        "hanjaReading": "斜(비낄 사) + 張(베풀 장) + 橋(다리 교)",
        "pronunciation": "꺼우 짜이 방",
        "meaningKo": "교량 상판을 주탑에서 뻗어나온 사재(케이블)로 직접 지지하는 구조. 현수교와 달리 주탑이 하중을 직접 받아 전달하며, 중장스팬 교량에 경제적입니다. 통역 시 '탑에서 줄로 직접 매단 다리'라고 설명하면 직관적이며, 케이블 배치 방식(팬형, 하프형, 방사형 등)이 설계의 핵심입니다. 인천대교, 이순신대교가 대표적 사례입니다.",
        "meaningVi": "Cầu có mặt cầu được treo trực tiếp bằng dây cáp từ trụ tháp. Khác với cầu treo, tháp chịu lực trực tiếp. Kinh tế cho nhịp trung bình.",
        "context": "교량 설계 및 시공",
        "culturalNote": "한국에서는 '사장교'라는 한자어가 정착되어 있으며, 인천대교, 부산 광안대교 등 대형 프로젝트로 대중화되었습니다. 베트남에서는 'cầu dây văng' (케이블이 비스듬히 뻗은 다리)가 표준 용어이며, 통역 시 'cáp nghiêng' (비스듬한 케이블)로 설명하면 명확합니다. 케이블 장력 조정이 시공 핵심입니다.",
        "commonMistakes": [
            {
                "mistake": "Cầu cáp (케이블 다리) - 너무 일반적",
                "correction": "Cầu dây văng (사장교)",
                "explanation": "'dây văng'이 사장교 고유 표현. 일반 케이블 교량과 구분해야 합니다."
            },
            {
                "mistake": "사장교를 현수교로 혼동",
                "correction": "주탑에서 직접 지지하는 구조로 명확히 구분",
                "explanation": "현수교는 주케이블이 상판을 매달고, 사장교는 주탑에서 직접 지지합니다."
            },
            {
                "mistake": "Cầu treo nghiêng (경사 현수교) - 오류",
                "correction": "Cầu dây văng (사장교)",
                "explanation": "사장교는 현수교의 변형이 아닌 별도 구조 형식입니다."
            }
        ],
        "examples": [
            {
                "ko": "이 사장교는 팬형 케이블 배치로 설계되어 주탑 하중을 분산했습니다.",
                "vi": "Cầu dây văng này được thiết kế bằng bố trí cáp hình quạt, phân tán tải trọng trụ tháp.",
                "situation": "formal"
            },
            {
                "ko": "사장교 시공 시 케이블 장력을 단계적으로 조정합니다.",
                "vi": "Khi thi công cầu dây văng, điều chỉnh lực căng cáp từng giai đoạn.",
                "situation": "onsite"
            },
            {
                "ko": "사장교는 300~600m 스팬에서 가장 경제적인 교량 형식입니다.",
                "vi": "Cầu dây văng là loại cầu kinh tế nhất cho nhịp 300-600m.",
                "situation": "formal"
            }
        ],
        "relatedTerms": ["현수교 (cầu treo)", "케이블구조 (kết cấu cáp)", "주탑 (trụ tháp)", "교량구조 (kết cấu cầu)"]
    },
    {
        "slug": "ket-cau-cach-chan",
        "korean": "면진구조",
        "vietnamese": "Kết cấu cách chấn",
        "hanja": "免震構造",
        "hanjaReading": "免(면할 면) + 震(흔들 진) + 構(얽을 구) + 造(지을 조)",
        "pronunciation": "껏꾸쩌우 각 쩐",
        "meaningKo": "건물과 지반 사이에 면진장치를 설치하여 지진 에너지를 흡수·차단하는 구조 시스템. 건물에 전달되는 지진력을 크게 줄여 구조물과 내부 시설을 보호합니다. 통역 시 '지진을 흡수하는 장치'라고 설명하면 직관적이며, 납-고무 베어링, 마찰진자 등이 주요 장치입니다. 초고층 건물, 병원, 데이터센터 등 중요 시설에 필수적으로 적용됩니다.",
        "meaningVi": "Hệ thống kết cấu lắp thiết bị cách chấn giữa móng và công trình để hấp thụ và cách ly năng lượng động đất, bảo vệ kết cấu và thiết bị bên trong.",
        "context": "내진설계 및 중요 시설 건축",
        "culturalNote": "한국에서는 2010년대 이후 지진 대비 강화로 '면진구조', '면진장치'라는 용어가 일반화되었으며, 원전, 병원 등에 의무 적용됩니다. 베트남에서는 'kết cấu cách chấn' (진동 차단 구조)이 표준 용어이며, 통역 시 'thiết bị giảm chấn' (감진장치)과 구분해야 합니다. 면진은 '차단', 제진은 '감쇠'입니다.",
        "commonMistakes": [
            {
                "mistake": "Cách chấn (면진) vs Giảm chấn (제진) 혼동",
                "correction": "면진 = 차단(cách), 제진 = 감쇠(giảm)",
                "explanation": "면진은 지진력 전달 차단, 제진은 에너지 흡수. 원리가 다릅니다."
            },
            {
                "mistake": "Kết cấu chống động đất (내진구조) - 다른 개념",
                "correction": "Kết cấu cách chấn (면진구조)",
                "explanation": "내진은 구조 강화, 면진은 장치로 차단. 명확히 구분해야 합니다."
            },
            {
                "mistake": "면진을 '지진 방지'로 설명",
                "correction": "지진력 전달 차단 시스템으로 설명",
                "explanation": "지진 자체를 막는 게 아닌, 건물로의 전달을 차단하는 것입니다."
            }
        ],
        "examples": [
            {
                "ko": "이 병원은 납-고무 베어링 면진장치로 설계되어 지진 시에도 기능을 유지합니다.",
                "vi": "Bệnh viện này được thiết kế bằng thiết bị cách chấn gối cao su chì, duy trì chức năng khi động đất.",
                "situation": "formal"
            },
            {
                "ko": "면진구조 건물은 지진 시 1~2초 주기로 천천히 흔들립니다.",
                "vi": "Công trình kết cấu cách chấn rung chậm với chu kỳ 1-2 giây khi động đất.",
                "situation": "formal"
            },
            {
                "ko": "면진장치 설치 후 정기적인 점검과 유지보수가 필수입니다.",
                "vi": "Sau khi lắp thiết bị cách chấn, kiểm tra và bảo trì định kỳ là bắt buộc.",
                "situation": "onsite"
            }
        ],
        "relatedTerms": ["제진구조 (kết cấu giảm chấn)", "내진설계 (thiết kế chống động đất)", "면진장치 (thiết bị cách chấn)", "지진하중 (tải trọng động đất)"]
    },
    {
        "slug": "thiet-bi-giam-chan",
        "korean": "제진장치",
        "vietnamese": "Thiết bị giảm chấn",
        "hanja": "制震裝置",
        "hanjaReading": "制(다스릴 제) + 震(흔들 진) + 裝(꾸밀 장) + 置(둘 치)",
        "pronunciation": "티엣 비 잠 쩐",
        "meaningKo": "건물 내부에 설치하여 지진이나 바람에 의한 진동 에너지를 흡수·감쇠시키는 장치. 댐퍼, 제진벽 등이 있으며, 건물의 흔들림을 줄여 구조적 손상과 거주자 불편을 감소시킵니다. 통역 시 '흔들림을 줄이는 장치'라고 설명하면 직관적이며, 면진과 달리 건물 내부에 설치되어 에너지를 흡수하는 방식입니다. 초고층 건물에 필수적입니다.",
        "meaningVi": "Thiết bị lắp bên trong công trình để hấp thụ và giảm năng lượng rung động do động đất hoặc gió. Gồm giảm chấn (damper), tường giảm chấn, làm giảm rung và bảo vệ kết cấu.",
        "context": "내진설계 및 초고층 건물",
        "culturalNote": "한국에서는 '제진장치', '댐퍼'라는 용어가 일반화되어 있으며, 롯데타워 등 초고층 건물에 TMD(질량댐퍼) 등이 적용되었습니다. 베트남에서는 'thiết bị giảm chấn' (진동 감쇠 장치)이 표준 용어이며, 통역 시 'damper' 영어 표현도 병기하면 명확합니다. 면진(cách chấn)과 제진(giảm chấn)을 구분하세요.",
        "commonMistakes": [
            {
                "mistake": "Giảm chấn (제진) vs Cách chấn (면진) 혼동",
                "correction": "제진 = 에너지 흡수(giảm), 면진 = 전달 차단(cách)",
                "explanation": "제진은 건물 내 장치, 면진은 기초부 장치. 위치와 원리가 다릅니다."
            },
            {
                "mistake": "Thiết bị chống rung (진동 방지 장치) - 모호함",
                "correction": "Thiết bị giảm chấn (제진장치)",
                "explanation": "'giảm chấn'이 지진 대응 표준 용어입니다."
            },
            {
                "mistake": "제진을 '떨림 제거'로 설명",
                "correction": "진동 에너지 흡수 시스템으로 설명",
                "explanation": "완전 제거가 아닌 감쇠임을 명확히 해야 합니다."
            }
        ],
        "examples": [
            {
                "ko": "이 건물 최상층에는 질량댐퍼 제진장치가 설치되어 바람에 의한 흔들림을 80% 감소시킵니다.",
                "vi": "Tầng cao nhất của tòa nhà này có thiết bị giảm chấn khối lượng (TMD), giảm 80% rung do gió.",
                "situation": "formal"
            },
            {
                "ko": "점성 댐퍼는 가장 널리 사용되는 제진장치입니다.",
                "vi": "Giảm chấn nhớt (viscous damper) là thiết bị giảm chấn phổ biến nhất.",
                "situation": "formal"
            },
            {
                "ko": "제진장치 설치 후 지진 시뮬레이션으로 성능을 검증합니다.",
                "vi": "Sau khi lắp thiết bị giảm chấn, kiểm chứng hiệu quả bằng mô phỏng động đất.",
                "situation": "onsite"
            }
        ],
        "relatedTerms": ["면진구조 (kết cấu cách chấn)", "댐퍼 (damper giảm chấn)", "내진설계 (thiết kế chống động đất)", "질량댐퍼 (TMD - giảm chấn khối lượng)"]
    }
]

# 저장 경로
file_path = os.path.join(
    os.path.dirname(__file__),
    "..",
    "data",
    "terms",
    "construction.json"
)

# 기존 파일 읽기
with open(file_path, "r", encoding="utf-8") as f:
    existing_data = json.load(f)

# 신규 용어 추가
existing_data.extend(data)

# 저장
with open(file_path, "w", encoding="utf-8") as f:
    json.dump(existing_data, f, ensure_ascii=False, indent=2)

print(f"✅ 10개 특수구조/대공간 용어 추가 완료")
print(f"📂 {file_path}")
print(f"📊 총 {len(existing_data)}개 용어")
