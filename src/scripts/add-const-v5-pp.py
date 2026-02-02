#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
건설(Construction) 도메인 용어 추가 스크립트 v5
테마: 건축자재/마감재 (ALC블록, 시멘트블록, 점토벽돌, 규조토, 타일, 포세린타일, 도기질타일, 모자이크타일, 인조대리석, 테라조)
총 10개 용어
Tier S 품질 기준 (90점 이상)
"""

import json
import os

# 추가할 용어 데이터 (Tier S 기준)
data = [
    {
        "id": 91,
        "slug": "gach-alc",
        "korean": "ALC블록",
        "vietnamese": "Gạch ALC",
        "hanja": None,
        "hanjaReading": None,
        "pronunciation": "에이엘씨블록",
        "meaningKo": "경량 기포 콘크리트(Autoclaved Lightweight Concrete) 블록. 통역 시 '경량블록'으로 단순화하면 일반 경량블록과 혼동 주의. ALC는 고온고압 양생으로 강도가 높고 단열성이 우수하여 외벽, 내벽, 지붕 등에 사용. 베트남에서는 '가익 ALC' 또는 '가익 닝(gạch nhẹ, 경량블록)'으로 불리나 ALC는 제조공정이 다른 특수 제품임을 강조. 현장에서 '가익 bông(기포블록)' 또는 '가익 xi măng nhẹ(경량시멘트블록)'로도 불림.",
        "meaningVi": "Gạch bê tông khí chưng áp (Autoclaved Lightweight Concrete). Được sản xuất bằng cách trộn xi măng, vôi, cát mịn với bột nhôm tạo bọt khí, sau đó chưng áp ở nhiệt độ cao. Có trọng lượng nhẹ (khoảng 1/4 gạch thường), cách nhiệt, cách âm tốt, chống cháy. Dùng cho tường ngoài, tường ngăn, mái.",
        "context": "외벽/내벽 시공, 단열재 선정, 경량구조 설계 시",
        "culturalNote": "한국에서는 ALC블록이 단독주택, 상업건물 외벽에 널리 사용되며 '헤벨', '이토오' 등 브랜드명으로도 불림. 베트남에서는 아직 일반 시멘트블록이나 점토벽돌 대비 보급률이 낮으나, 고급 빌라나 상업건물에서 단열성능 향상을 위해 채택 증가 중. 통역 시 'ALC'를 그대로 쓰거나 'gạch bê tông khí'로 풀어 설명. 'gạch nhẹ'로만 하면 일반 경량블록과 구분 안 됨.",
        "commonMistakes": [
            {
                "mistake": "ALC블록을 'gạch nhẹ'로만 번역",
                "correction": "'gạch ALC' 또는 'gạch bê tông khí chưng áp'",
                "explanation": "'gạch nhẹ'는 경량블록 전반을 의미해 ALC의 고압증기양생 특성이 누락됨"
            },
            {
                "mistake": "ALC를 '기포블록'으로 통역",
                "correction": "'ALC블록(gạch ALC)' 또는 '경량기포콘크리트블록'",
                "explanation": "기포블록은 일반 폼콘크리트 블록과도 혼동 가능. ALC는 제조공정(오토클레이브)이 특수함"
            },
            {
                "mistake": "'헤벨블록'을 고유명사로만 처리",
                "correction": "'ALC블록(헤벨 등 브랜드)' 설명 병기",
                "explanation": "한국에서는 브랜드명이 보통명사처럼 쓰이지만 베트남 현장에서는 ALC 개념 설명 필요"
            }
        ],
        "examples": [
            {
                "ko": "외벽은 200mm ALC블록으로 시공하여 단열성능을 확보합니다",
                "vi": "Tường ngoài thi công bằng gạch ALC dày 200mm để đảm bảo hiệu suất cách nhiệt",
                "situation": "formal"
            },
            {
                "ko": "ALC블록은 가볍고 시공이 빨라서 공기 단축에 유리합니다",
                "vi": "Gạch ALC nhẹ và thi công nhanh nên có lợi cho việc rút ngắn tiến độ",
                "situation": "onsite"
            },
            {
                "ko": "이 현장은 ALC 대신 일반 시멘트블록 쓰기로 했어요",
                "vi": "Công trường này quyết định dùng gạch xi măng thường thay vì gạch ALC",
                "situation": "informal"
            }
        ],
        "relatedTerms": ["시멘트블록", "경량블록", "단열재", "외벽마감"]
    },
    {
        "id": 92,
        "slug": "gach-xi-mang",
        "korean": "시멘트블록",
        "vietnamese": "Gạch xi măng",
        "hanja": None,
        "hanjaReading": None,
        "pronunciation": "시멘트블록",
        "meaningKo": "시멘트, 모래, 자갈 등을 혼합해 성형한 콘크리트 블록. 통역 시 '콘크리트블록'과 혼용되나 엄밀히는 시멘트가 주재료. 베트nam에서는 'gạch xi măng' 또는 'gạch block'으로 불림. 일반 시멘트블록은 속이 빈 'gạch rỗng'과 속이 찬 'gạch đặc'으로 나뉨. 한국에서는 '블록', '콘크리트블록', '시멘트벽돌' 등 다양하게 불리나 통역 시 'gạch xi măng'이 가장 명확. 현장에서 규격(190×190×390mm 등)을 함께 언급하면 혼동 방지.",
        "meaningVi": "Gạch được đúc từ hỗn hợp xi măng, cát, sỏi. Có loại đặc (gạch xi măng đặc) và loại rỗng (gạch block rỗng). Dùng xây tường chịu lực, tường ngăn. Ưu điểm: giá rẻ, sẵn có, thi công nhanh. Nhược điểm: nặng, cách nhiệt kém hơn gạch ALC, dễ nứt nếu không đảm bảo chất lượng vữa.",
        "context": "내력벽/비내력벽 시공, 가격 비교, 자재 선정 시",
        "culturalNote": "한국에서는 시멘트블록이 저층 건물, 담장, 창고 등에 많이 사용되며 '블록'으로 통칭. 베트남에서는 'gạch xi măng'이 가장 보편적인 벽체 재료로, 도시 주택부터 공장까지 광범위 사용. 통역 시 '블록'을 베트남어 'block'으로 그대로 쓰면 통하지만 'gạch xi măng'이 더 자연스럽고 명확. '벽돌'로 오해하지 않도록 주의.",
        "commonMistakes": [
            {
                "mistake": "시멘트블록을 'gạch gạch'으로 번역",
                "correction": "'gạch xi măng' 또는 'gạch block'",
                "explanation": "'gạch'만으로는 벽돌 일반을 의미해 재질이 불명확"
            },
            {
                "mistake": "'블록'을 'khối'로 직역",
                "correction": "'gạch xi măng' 또는 'gạch block'",
                "explanation": "'khối'는 덩어리/블록 일반이지 건축자재 의미 없음"
            },
            {
                "mistake": "속빈블록을 'gạch rỗng'으로만 하고 재질 생략",
                "correction": "'gạch xi măng rỗng' 또는 'gạch block rỗng'",
                "explanation": "재질 명시 없이 'rỗng'만 하면 다른 재질 블록과 혼동"
            }
        ],
        "examples": [
            {
                "ko": "내벽은 두께 100mm 시멘트블록으로 시공합니다",
                "vi": "Tường ngăn thi công bằng gạch xi măng dày 100mm",
                "situation": "formal"
            },
            {
                "ko": "블록 쌓기 전에 수평 먹줄 먼저 치세요",
                "vi": "Trước khi xây gạch xi măng, hãy căng dây먹 thủy bình trước",
                "situation": "onsite"
            },
            {
                "ko": "이 블록은 강도가 약해서 내력벽에는 못 써요",
                "vi": "Gạch xi măng này cường độ yếu nên không dùng cho tường chịu lực được",
                "situation": "informal"
            }
        ],
        "relatedTerms": ["ALC블록", "벽돌", "콘크리트", "내력벽"]
    },
    {
        "id": 93,
        "slug": "gach-dat-set",
        "korean": "점토벽돌",
        "vietnamese": "Gạch đất sét nung",
        "hanja": "粘土甓甎",
        "hanjaReading": "粘(찰 점) + 土(흙 토) + 甓(벽돌 벽) + 甎(벽돌 전)",
        "pronunciation": "점토벽돌",
        "meaningKo": "점토를 성형해 고온(900~1100℃)에서 구워 만든 전통 벽돌. 통역 시 '벽돌'만 하면 시멘트블록과 혼동되므로 '점토벽돌(gạch đất sét nung)' 명시 필요. 베트남에서는 'gạch đỏ(붉은 벽돌)' 또는 'gạch nung'으로도 불림. 한국에서는 '적벽돌', '소성벽돌', '진흙벽돌' 등으로도 불리나 공식 명칭은 '점토벽돌'. 내구성, 단열성, 흡음성이 우수하나 무겁고 시공 속도가 느림. 외장재로는 '치장벽돌(gạch ốp lát)'과 구분.",
        "meaningVi": "Gạch được làm từ đất sét, nung ở nhiệt độ cao (900~1100℃). Thường có màu đỏ hoặc nâu, bề mặt thô. Ưu điểm: bền, cách nhiệt tốt, chống ồn, thẩm mỹ tự nhiên. Nhược điểm: nặng, hút nước cao (cần chống thấm), thi công lâu hơn gạch xi măng.",
        "context": "외벽/내벽 시공, 전통 건축, 디자인 마감재 선정 시",
        "culturalNote": "한국에서는 점토벽돌이 1970~80년대 주택에 많이 쓰였으나 현재는 고급 외장재(치장벽돌)나 인테리어 악센트로 사용. 베트남에서는 'gạch đỏ'가 여전히 저층 주택, 농촌 건물의 주력 벽체 재료. 통역 시 '벽돌'을 'gạch'으로만 하면 시멘트블록도 포함되므로 'gạch đất sét' 또는 'gạch nung' 명시. 'gạch đỏ'는 구어체로 자연스러움.",
        "commonMistakes": [
            {
                "mistake": "점토벽돌을 'gạch'로만 번역",
                "correction": "'gạch đất sét nung' 또는 'gạch đỏ'",
                "explanation": "'gạch'만으로는 시멘트블록, 타일 등 모든 벽돌류 포함"
            },
            {
                "mistake": "'적벽돌'을 'gạch đỏ(붉은 벽돌)'로만 번역",
                "correction": "'gạch đất sét nung' (재질 명시)",
                "explanation": "'gạch đỏ'는 색깔 기준이라 페인트 칠한 블록도 포함될 수 있음"
            },
            {
                "mistake": "치장벽돌과 구조용 점토벽돌 구분 없이 통역",
                "correction": "구조용은 'gạch xây', 치장용은 'gạch ốp'",
                "explanation": "용도에 따라 베트남어 표현이 달라짐"
            }
        ],
        "examples": [
            {
                "ko": "외벽은 점토벽돌 치장쌓기로 마감합니다",
                "vi": "Tường ngoài hoàn thiện bằng cách ốp gạch đất sét nung",
                "situation": "formal"
            },
            {
                "ko": "붉은 벽돌로 쌓은 담장이 운치가 있네요",
                "vi": "Tường rào xây bằng gạch đỏ trông rất có duyên",
                "situation": "onsite"
            },
            {
                "ko": "이 벽돌은 흡수율이 높아서 방수 처리 필수예요",
                "vi": "Gạch đất sét này hút nước cao nên bắt buộc phải xử lý chống thấm",
                "situation": "informal"
            }
        ],
        "relatedTerms": ["시멘트블록", "치장벽돌", "적벽돌", "외벽마감"]
    },
    {
        "id": 94,
        "slug": "dat-diatomite",
        "korean": "규조토",
        "vietnamese": "Đất diatomite",
        "hanja": "珪藻土",
        "hanjaReading": "珪(구슬 규) + 藻(마름 조) + 土(흙 토)",
        "pronunciation": "규조토",
        "meaningKo": "규조류(珪藻, diatom) 화석이 퇴적된 천연 광물. 통역 시 '다이아토마이트(diatomite)' 또는 베트남어 'đất diatomite'로 표현. 미세한 기공(다공질)으로 습도 조절, 탈취, 단열 기능 우수. 내장재로는 규조토 벽지, 규조토 페인트, 규조토 타일 등 사용. 한국에서는 '규조토 벽지'가 아파트 인테리어에 인기. 베트남에서는 아직 낯선 소재지만 고급 인테리어에서 'đất sét diatomite' 또는 'vật liệu diatomite'로 소개됨. 통역 시 '습도조절 기능'을 강조하면 이해 빠름.",
        "meaningVi": "Đất hóa thạch từ tảo cремkremne (diatomite), có cấu trúc xốp với nhiều lỗ nhỏ. Có khả năng hút ẩm, khử mùi, cách nhiệt tự nhiên. Dùng làm vật liệu hoàn thiện nội thất: sơn diatomite, giấy dán tường diatomite, gạch ốp. Thân thiện môi trường, không độc hại.",
        "context": "내장재 선정, 습도 조절, 친환경 마감재 논의 시",
        "culturalNote": "한국에서는 규조토가 습기 많은 욕실, 주방, 지하실에 인기 있는 친환경 마감재. '규조토 바스매트', '규조토 벽지' 등 다양한 제품 보급. 베트남에서는 'đất diatomite'가 아직 대중화되지 않았으나, 고급 빌라나 에코 인테리어에서 관심 증가 중. 통역 시 '규조토'를 'đất sét diatomite' 또는 'vật liệu diatomite'로 하되, '습도 조절(điều hòa độ ẩm)' 기능을 함께 설명하면 이해 도움.",
        "commonMistakes": [
            {
                "mistake": "규조토를 'đất sét(점토)'로 번역",
                "correction": "'đất diatomite' 또는 'đất sét diatomite'",
                "explanation": "일반 점토와 달리 규조 화석 성분이 핵심이므로 'diatomite' 명시 필수"
            },
            {
                "mistake": "'규조토 벽지'를 'giấy dán tường đất sét'로만 번역",
                "correction": "'giấy dán tường diatomite' 또는 'giấy dán tường đất diatomite'",
                "explanation": "'đất sét'만으로는 일반 점토 벽지로 오해"
            },
            {
                "mistake": "습도 조절 기능 설명 없이 재질명만 통역",
                "correction": "'đất diatomite(điều hòa độ ẩm tự nhiên)'처럼 기능 병기",
                "explanation": "베트남에서 생소한 소재라 기능 설명 없으면 이해 어려움"
            }
        ],
        "examples": [
            {
                "ko": "욕실 벽면은 규조토 페인트로 마감하여 습도를 조절합니다",
                "vi": "Tường phòng tắm hoàn thiện bằng sơn diatomite để điều hòa độ ẩm",
                "situation": "formal"
            },
            {
                "ko": "규조토 바스매트는 물을 빨리 흡수해서 편해요",
                "vi": "Thảm phòng tắm diatomite hút nước nhanh nên rất tiện",
                "situation": "onsite"
            },
            {
                "ko": "이 벽지는 규조토 성분이 들어가서 냄새도 잡아줘요",
                "vi": "Giấy dán tường này có thành phần diatomite nên khử mùi được",
                "situation": "informal"
            }
        ],
        "relatedTerms": ["친환경자재", "내장재", "벽지", "습도조절"]
    },
    {
        "id": 95,
        "slug": "gach-op",
        "korean": "타일",
        "vietnamese": "Gạch ốp lát",
        "hanja": None,
        "hanjaReading": None,
        "pronunciation": "타일",
        "meaningKo": "벽이나 바닥을 덮는 판상 마감재. 통역 시 베트남어 'gạch ốp lát(붙이는 벽돌)'이 정확. '타일'은 외래어로 베트남어에서도 'tile'로 통하나 공식 표현은 'gạch ốp lát'. 벽 타일은 'gạch ốp tường', 바닥 타일은 'gạch lát nền'. 재질에 따라 도기질(gạch ceramic), 자기질(gạch sứ), 포세린(gạch Porcelain) 등으로 나뉨. 한국에서는 '타일'로 통칭하지만 베트남 현장에서는 재질과 용도를 명확히 구분해 부름. 통역 시 '세라믹 타일', '포세린 타일' 등 재질 병기 권장.",
        "meaningVi": "Vật liệu ốp tường, lát sàn dạng tấm mỏng. Gồm nhiều loại: gạch ceramic (đồ gốm), gạch sứ (tráng men), gạch Porcelain (sứ cứng), gạch đá tự nhiên, v.v. Ưu điểm: dễ vệ sinh, chống nước, đa dạng mẫu mã. Nhược điểm: lạnh, dễ nứt vỡ nếu thi công kém.",
        "context": "바닥/벽 마감재 선정, 욕실/주방 설계 시",
        "culturalNote": "한국에서는 '타일'이 욕실, 주방, 현관 등에 필수 마감재로 쓰이며, '타일 붙이기'는 전문 타일공 영역. 베트남에서는 'gạch ốp lát'이 주택부터 빌딩까지 광범위 사용되며, 'thợ lát gạch(타일공)'이 숙련 직종. 통역 시 '타일'을 베트남어 'tile'로 그대로 해도 통하지만 'gạch ốp lát'이 더 자연스럽고 공식적. '타일 종류'는 재질(ceramic, Porcelain, 대리석 등) 명시 필요.",
        "commonMistakes": [
            {
                "mistake": "타일을 'gạch'로만 번역",
                "correction": "'gạch ốp lát' 또는 'gạch ốp tường/lát nền'",
                "explanation": "'gạch'만으로는 벽돌, 블록 등 모든 벽돌류 포함"
            },
            {
                "mistake": "'세라믹 타일'을 'gạch sành'로 번역",
                "correction": "'gạch ceramic' 또는 'gạch gốm sứ'",
                "explanation": "'gạch sành'는 저급 도기를 의미해 고급 세라믹과 혼동"
            },
            {
                "mistake": "벽 타일과 바닥 타일 구분 없이 'gạch'로만 통역",
                "correction": "벽은 'gạch ốp tường', 바닥은 'gạch lát nền'",
                "explanation": "용도에 따라 베트남어 표현이 달라짐"
            }
        ],
        "examples": [
            {
                "ko": "욕실 바닥은 미끄럼 방지 타일로 시공합니다",
                "vi": "Sàn phòng tắm thi công bằng gạch lát chống trơn",
                "situation": "formal"
            },
            {
                "ko": "타일 줄눈이 삐뚤어졌으니 다시 해주세요",
                "vi": "Mạch nối gạch bị lệch rồi, làm lại giúp tôi",
                "situation": "onsite"
            },
            {
                "ko": "이 타일은 수입산이라 가격이 좀 비싸요",
                "vi": "Gạch ốp lát này nhập khẩu nên giá hơi đắt",
                "situation": "informal"
            }
        ],
        "relatedTerms": ["포세린타일", "도기질타일", "모자이크타일", "바닥재"]
    },
    {
        "id": 96,
        "slug": "gach-porcelain",
        "korean": "포세린타일",
        "vietnamese": "Gạch Porcelain",
        "hanja": None,
        "hanjaReading": None,
        "pronunciation": "포세린타일",
        "meaningKo": "고온(1200℃ 이상)에서 소성한 자기질 타일. 통역 시 베트남어 'gạch Porcelain' 또는 'gạch sứ cứng'으로 표현. 일반 세라믹 타일(gạch ceramic)보다 흡수율 낮고(0.5% 이하) 강도 높아 외부 바닥, 고급 내장재에 사용. 한국에서는 '포세린', '자기질 타일'로 불리며 아파트 거실 바닥재로 인기. 베트남에서는 'gạch Porcelain' 또는 'gạch lát nền cao cấp(고급 바닥타일)'로 불림. 통역 시 '세라믹 타일'과 구분하여 '흡수율 낮음(thấm nước thấp)' 강조.",
        "meaningVi": "Gạch sứ nung ở nhiệt độ cao (trên 1200℃), có độ hút nước rất thấp (dưới 0.5%), cường độ cao, chịu mài mòn tốt. Dùng cho sàn phòng khách, sảnh, ngoài trời. Bề mặt có thể bóng hoặc nhám, màu sắc đa dạng. Cao cấp hơn gạch ceramic thông thường.",
        "context": "고급 바닥재 선정, 외부 마감재, 내구성 논의 시",
        "culturalNote": "한국에서는 포세린타일이 아파트 거실, 상업공간 바닥재의 표준으로 자리잡음. '대리석 무늬 포세린', '우드 패턴 포세린' 등 다양한 디자인 제품 유통. 베트남에서는 'gạch Porcelain'이 고급 빌라, 호텔, 쇼핑몰에 사용되며, 'gạch ceramic'보다 비싸지만 내구성과 미관으로 선호도 증가 중. 통역 시 '포세린'을 'Porcelain'으로 그대로 쓰거나 'gạch sứ cứng' 설명 병기.",
        "commonMistakes": [
            {
                "mistake": "포세린타일을 'gạch ceramic'으로 번역",
                "correction": "'gạch Porcelain' 또는 'gạch sứ cứng'",
                "explanation": "'ceramic'은 일반 도기질 타일을 포함하므로 포세린의 고급 특성 누락"
            },
            {
                "mistake": "'자기질 타일'을 'gạch sứ'로만 번역",
                "correction": "'gạch Porcelain' 또는 'gạch sứ cứng(độ hút nước thấp)'",
                "explanation": "'gạch sứ'는 일반 유약 타일도 포함할 수 있어 흡수율 낮음 강조 필요"
            },
            {
                "mistake": "포세린과 세라믹 구분 없이 '고급 타일'로만 통역",
                "correction": "'gạch Porcelain(độ hút nước dưới 0.5%)'처럼 수치 병기",
                "explanation": "베트남 현장에서는 흡수율 기준으로 구분하므로 수치 명시가 명확"
            }
        ],
        "examples": [
            {
                "ko": "거실 바닥은 600×600mm 포세린타일로 시공합니다",
                "vi": "Sàn phòng khách thi công bằng gạch Porcelain 600×600mm",
                "situation": "formal"
            },
            {
                "ko": "포세린은 물 안 먹어서 야외 테라스에도 쓸 수 있어요",
                "vi": "Gạch Porcelain không thấm nước nên dùng cho sân thượng ngoài trời cũng được",
                "situation": "onsite"
            },
            {
                "ko": "이 포세린은 대리석 무늬라 고급스러워 보여요",
                "vi": "Gạch Porcelain này vân đá cẩm thạch nên trông sang trọng",
                "situation": "informal"
            }
        ],
        "relatedTerms": ["타일", "도기질타일", "세라믹타일", "바닥재"]
    },
    {
        "id": 97,
        "slug": "gach-do-gom",
        "korean": "도기질타일",
        "vietnamese": "Gạch ceramic đồ gốm",
        "hanja": "陶器質",
        "hanjaReading": "陶(질그릇 도) + 器(그릇 기) + 質(바탕 질)",
        "pronunciation": "도기질타일",
        "meaningKo": "상대적으로 낮은 온도(900~1100℃)에서 소성한 타일로 흡수율 10% 이상. 통역 시 베트남어 'gạch ceramic đồ gốm' 또는 'gạch gốm sứ'로 표현. 포세린타일(자기질)보다 흡수율 높고 강도 낮아 주로 내부 벽면(욕실, 주방)에 사용. 바닥재로는 내구성 부족. 한국에서는 '도기질', '일반 세라믹 타일'로 불리며 저가 내장재. 베트남에서는 'gạch ốp tường'으로 통칭되나 재질 구분 시 'gạch ceramic'과 'gạch Porcelain' 명시. 통역 시 '벽 타일'로 용도 한정하면 명확.",
        "meaningVi": "Gạch nung ở nhiệt độ thấp hơn (900~1100℃), độ hút nước cao (trên 10%), cường độ thấp hơn gạch Porcelain. Chủ yếu dùng ốp tường phòng tắm, bếp. Không nên dùng lát sàn vì dễ mòn, nứt. Giá rẻ hơn gạch Porcelain.",
        "context": "욕실/주방 벽 마감재 선정, 가격 비교 시",
        "culturalNote": "한국에서는 도기질타일이 저가 아파트, 다세대 주택 욕실 벽에 주로 사용되며 '욕실 타일'로 통칭. 포세린타일 대비 저렴하지만 흡수율 높아 방수 처리 중요. 베트남에서는 'gạch ốp tường'이 일반적이며, 'gạch ceramic'으로도 불림. 통역 시 '도기질'을 'đồ gốm' 또는 'ceramic đồ gốm'으로 하되, '벽 전용(chỉ dùng ốp tường)' 강조하면 바닥 타일과 혼동 방지.",
        "commonMistakes": [
            {
                "mistake": "도기질타일을 'gạch sứ'로 번역",
                "correction": "'gạch ceramic đồ gốm' 또는 'gạch gốm sứ'",
                "explanation": "'gạch sứ'는 자기질(포세린)을 연상시켜 흡수율 낮다는 오해 유발"
            },
            {
                "mistake": "'세라믹 타일'을 포세린과 도기질 구분 없이 통역",
                "correction": "도기질은 'gạch ceramic đồ gốm', 포세린은 'gạch Porcelain'",
                "explanation": "'ceramic'은 넓은 의미로 둘 다 포함하므로 재질 명시 필요"
            },
            {
                "mistake": "도기질타일을 바닥재로 제안",
                "correction": "'gạch ốp tường(벽 타일)'로만 권장",
                "explanation": "도기질은 흡수율 높고 강도 낮아 바닥재 부적합"
            }
        ],
        "examples": [
            {
                "ko": "욕실 벽은 도기질타일로 경제적으로 마감합니다",
                "vi": "Tường phòng tắm hoàn thiện tiết kiệm bằng gạch ceramic đồ gốm",
                "situation": "formal"
            },
            {
                "ko": "이 타일은 흡수율 높아서 방수 잘 해야 해요",
                "vi": "Gạch này độ hút nước cao nên phải chống thấm kỹ",
                "situation": "onsite"
            },
            {
                "ko": "도기질은 바닥에 쓰면 금방 깨져요",
                "vi": "Gạch đồ gốm dùng lát sàn thì nhanh vỡ lắm",
                "situation": "informal"
            }
        ],
        "relatedTerms": ["타일", "포세린타일", "세라믹타일", "욕실마감"]
    },
    {
        "id": 98,
        "slug": "gach-mosaic",
        "korean": "모자이크타일",
        "vietnamese": "Gạch mosaic",
        "hanja": None,
        "hanjaReading": None,
        "pronunciation": "모자이크타일",
        "meaningKo": "작은 조각(보통 25×25mm 이하)을 조합해 패턴을 만드는 타일. 통역 시 베트남어 'gạch mosaic'으로 표현. 유리, 도자기, 대리석, 금속 등 다양한 재질로 제작. 한국에서는 '모자이크'로 통칭하며 욕실, 수영장, 주방 포인트 벽에 사용. 베트남에서도 'gạch mosaic'이 고급 인테리어 악센트로 인기. 시트 단위(300×300mm 등)로 판매되어 시공 편리. 통역 시 '작은 타일 조각(mảnh gạch nhỏ)' 설명 병기하면 이해 빠름.",
        "meaningVi": "Gạch nhỏ (thường 25×25mm hoặc nhỏ hơn) ghép thành tấm, tạo hoa văn. Có nhiều chất liệu: thủy tinh, gốm sứ, đá tự nhiên, kim loại. Dùng ốp tường điểm nhấn phòng tắm, bể bơi, bếp. Bán theo tấm lưới (sheet) để dễ thi công.",
        "context": "욕실/주방 포인트 벽, 수영장 마감, 인테리어 악센트 시",
        "culturalNote": "한국에서는 모자이크타일이 욕실 샤워부스, 주방 싱크대 뒷벽 등 포인트 영역에 사용되며 '모자이크'로 통칭. 유리 모자이크, 대리석 모자이크 등 재질 다양. 베트남에서는 'gạch mosaic'이 고급 빌라, 호텔 욕실, 수영장에 쓰이며 인테리어 디자인 요소로 인기. 통역 시 '모자이크'를 'mosaic'으로 그대로 쓰면 통하지만 '작은 타일 조각 조합(ghép mảnh gạch nhỏ)' 설명 추가하면 명확.",
        "commonMistakes": [
            {
                "mistake": "모자이크타일을 'gạch nhỏ(작은 타일)'로만 번역",
                "correction": "'gạch mosaic' 또는 'gạch ghép hoa văn'",
                "explanation": "'gạch nhỏ'는 단순히 작은 타일이지 모자이크 패턴 의미 누락"
            },
            {
                "mistake": "'모자이크 패턴'을 'hoa văn gạch'로만 번역",
                "correction": "'gạch mosaic' 또는 'hoa văn mosaic'",
                "explanation": "'hoa văn gạch'는 일반 타일 무늬도 포함하므로 'mosaic' 명시 필요"
            },
            {
                "mistake": "유리 모자이크를 'gạch thủy tinh'으로만 통역",
                "correction": "'gạch mosaic thủy tinh' (재질 + 모자이크 병기)",
                "explanation": "'gạch thủy tinh'만으로는 일반 유리 타일로 오해"
            }
        ],
        "examples": [
            {
                "ko": "샤워부스 벽면은 유리 모자이크타일로 포인트를 줍니다",
                "vi": "Tường khu vực vòi sen điểm nhấn bằng gạch mosaic thủy tinh",
                "situation": "formal"
            },
            {
                "ko": "모자이크는 시트로 붙이니까 시공이 빨라요",
                "vi": "Gạch mosaic dán theo tấm lưới nên thi công nhanh",
                "situation": "onsite"
            },
            {
                "ko": "이 모자이크는 대리석 재질이라 고급스러워요",
                "vi": "Gạch mosaic này chất liệu đá cẩm thạch nên sang trọng",
                "situation": "informal"
            }
        ],
        "relatedTerms": ["타일", "유리타일", "욕실마감", "인테리어"]
    },
    {
        "id": 99,
        "slug": "da-nhan-tao",
        "korean": "인조대리석",
        "vietnamese": "Đá nhân tạo",
        "hanja": "人造大理石",
        "hanjaReading": "人(사람 인) + 造(지을 조) + 大(큰 대) + 理(다스릴 리) + 石(돌 석)",
        "pronunciation": "인조대리석",
        "meaningKo": "천연 대리석 대신 수지, 분말 등을 혼합해 인공 제작한 석재. 통역 시 베트남어 'đá nhân tạo' 또는 'đá nhân tạo marble'로 표현. 천연 대리석보다 저렴하고 무늬/색상 균일하며 가공 용이. 주방 상판(bàn bếp), 욕실 세면대(bàn lavabo), 벽 마감재로 사용. 한국에서는 '인조대리석', '엔지니어드 스톤(engineered stone)', '코리안(Corian, 상표명)' 등으로 불림. 베트남에서는 'đá nhân tạo', 'đá marble nhân tạo', 'đá thạch anh nhân tạo(인조석영석)' 등으로 구분. 통역 시 '천연 아님(không tự nhiên)' 명시.",
        "meaningVi": "Đá được tạo ra bằng cách trộn nhựa (resin) với bột đá tự nhiên (cẩm thạch, thạch anh, v.v.). Rẻ hơn đá tự nhiên, màu sắc đồng đều, dễ gia công. Dùng làm mặt bếp, lavabo, ốp tường. Loại phổ biến: đá marble nhân tạo, đá thạch anh nhân tạo (quartz).",
        "context": "주방 상판/욕실 마감재 선정, 가격 비교 시",
        "culturalNote": "한국에서는 인조대리석이 아파트 주방 상판의 표준 마감재로 자리잡았으며, '코리안', '하이맥스(Hi-Macs)' 등 브랜드명으로도 불림. 천연 대리석 대비 저렴하고 이음매 없는 시공 가능. 베트남에서는 'đá nhân tạo'가 중급 이상 주택 주방, 욕실에 쓰이며 'đá tự nhiên(천연석)'보다 저렴하지만 내구성은 떨어짐. 통역 시 '인조'를 'nhân tạo'로 명시하고, 'quartz(석영석)' 등 재질 구분 권장.",
        "commonMistakes": [
            {
                "mistake": "인조대리석을 'đá cẩm thạch(대리석)'로만 번역",
                "correction": "'đá nhân tạo' 또는 'đá marble nhân tạo'",
                "explanation": "'đá cẩm thạch'는 천연 대리석을 의미해 인조 여부 구분 필요"
            },
            {
                "mistake": "'코리안'을 'Corian'으로만 표기하고 설명 생략",
                "correction": "'đá nhân tạo(thương hiệu Corian)'처럼 설명 병기",
                "explanation": "베트남에서 브랜드명이 생소하므로 'đá nhân tạo' 설명 필요"
            },
            {
                "mistake": "인조석영석을 일반 인조대리석과 구분 없이 통역",
                "correction": "석영석은 'đá thạch anh nhân tạo(quartz)'",
                "explanation": "석영석은 경도 높고 가격 비싸므로 일반 인조대리석과 구분"
            }
        ],
        "examples": [
            {
                "ko": "주방 상판은 인조대리석으로 이음매 없이 시공합니다",
                "vi": "Mặt bếp thi công bằng đá nhân tạo liền khối không mối nối",
                "situation": "formal"
            },
            {
                "ko": "인조대리석은 천연보다 저렴하고 관리도 쉬워요",
                "vi": "Đá nhân tạo rẻ hơn đá tự nhiên và bảo dưỡng cũng dễ",
                "situation": "onsite"
            },
            {
                "ko": "이 상판은 코리안 제품이라 흠집 나도 연마하면 돼요",
                "vi": "Mặt bếp này sản phẩm Corian nên bị xước cũng chỉ cần đánh bóng lại",
                "situation": "informal"
            }
        ],
        "relatedTerms": ["천연대리석", "석영석", "주방상판", "욕실마감"]
    },
    {
        "id": 100,
        "slug": "da-terrazzo",
        "korean": "테라조",
        "vietnamese": "Đá terrazzo",
        "hanja": None,
        "hanjaReading": None,
        "pronunciation": "테라조",
        "meaningKo": "대리석, 화강암, 유리 등의 골재를 시멘트나 수지에 혼합해 갈아 광택을 낸 마감재. 통역 시 베트남어 'đá terrazzo' 또는 'gạch terrazzo'로 표현. 이탈리아 전통 바닥재로, 골재 크기와 색상에 따라 다양한 디자인 가능. 한국에서는 '테라조', '인조석(人造石)'으로 불리며 1970~80년대 건물 바닥재로 쓰였다가 최근 레트로 인테리어로 재유행. 베트남에서는 'đá terrazzo'가 전통 프랑스 양식 건물, 고급 카페, 빌라 바닥에 쓰이며 'gạch bông(꽃무늬 타일)'과 함께 인기. 통역 시 '갈아서 광택(mài bóng)' 공정 설명 추가.",
        "meaningVi": "Vật liệu hoàn thiện làm từ mảnh đá tự nhiên (cẩm thạch, đá granite, thủy tinh) trộn với xi măng hoặc nhựa, sau đó mài bóng bề mặt. Có hoa văn đẹp, bền, dùng lát sàn, ốp tường. Phổ biến ở kiến trúc cổ Pháp, hiện nay dùng cho nội thất cao cấp, phong cách retro.",
        "context": "바닥/벽 마감재 선정, 레트로/모던 인테리어 시",
        "culturalNote": "한국에서는 테라조가 과거 공공건물, 학교 복도 바닥재로 쓰였으나 최근 레트로 감성 인테리어로 재조명. 카페, 상업공간에서 '테라조 타일', '테라조 상판' 등으로 활용. 베트남에서는 'đá terrazzo'가 프랑스 식민지 시대 건축물에 많이 남아 있으며, 고급 인테리어 소재로 인기 재상승. 통역 시 '테라조'를 'terrazzo'로 그대로 쓰면 통하며, '골재 혼합 후 연마(trộn mảnh đá rồi mài bóng)' 설명 추가하면 명확.",
        "commonMistakes": [
            {
                "mistake": "테라조를 'đá nhân tạo(인조석)'로만 번역",
                "correction": "'đá terrazzo' 또는 'gạch terrazzo'",
                "explanation": "'đá nhân tạo'는 인조대리석 등도 포함하므로 'terrazzo' 명시 필요"
            },
            {
                "mistake": "'인조석'을 테라조, 인조대리석 구분 없이 통역",
                "correction": "테라조는 'đá terrazzo', 인조대리석은 'đá marble nhân tạo'",
                "explanation": "제조 방식과 용도가 다르므로 명확히 구분"
            },
            {
                "mistake": "테라조 타일을 'gạch đá'로만 번역",
                "correction": "'gạch terrazzo' 또는 'gạch đá terrazzo'",
                "explanation": "'gạch đá'는 일반 석재 타일을 의미해 테라조 특성 누락"
            }
        ],
        "examples": [
            {
                "ko": "로비 바닥은 테라조로 마감하여 고급스러운 느낌을 줍니다",
                "vi": "Sàn sảnh hoàn thiện bằng đá terrazzo tạo cảm giác sang trọng",
                "situation": "formal"
            },
            {
                "ko": "테라조는 시공 후 연마해야 광택이 나요",
                "vi": "Đá terrazzo sau khi thi công phải mài bóng mới có độ bóng",
                "situation": "onsite"
            },
            {
                "ko": "이 카페 바닥 테라조 패턴이 예쁘네요",
                "vi": "Sàn terrazzo quán cafe này hoa văn đẹp ghê",
                "situation": "informal"
            }
        ],
        "relatedTerms": ["인조대리석", "타일", "바닥재", "레트로인테리어"]
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

# 기존 파일 읽기
with open(file_path, "r", encoding="utf-8") as f:
    existing_data = json.load(f)

# 새 용어 추가
existing_data.extend(data)

# 파일 저장 (들여쓰기 2칸, 한글 그대로, 마지막 줄바꿈 없음)
with open(file_path, "w", encoding="utf-8") as f:
    json.dump(existing_data, f, ensure_ascii=False, indent=2)

print(f"✅ {len(data)}개 용어 추가 완료: {file_path}")
print(f"📊 총 용어 수: {len(existing_data)}개")
