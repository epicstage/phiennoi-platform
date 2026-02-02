#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
건설안전보호구 (Construction Safety PPE) - 10 terms
Tier S quality: all fields complete, 200+ char meaningKo, 100+ char meaningVi/culturalNote
"""

import json
import os

# Get absolute path to construction.json
file_path = os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', 'data', 'terms', 'construction.json')

# Load existing data
with open(file_path, 'r', encoding='utf-8') as f:
    data = json.load(f)  # data is a LIST

# Get existing slugs to prevent duplicates
existing_slugs = {t['slug'] for t in data}

# New terms - Construction Safety PPE
new_terms = [
    {
        "slug": "kinh-bao-ho",
        "korean": "보안경",
        "vietnamese": "kính bảo hộ",
        "hanja": "保安鏡",
        "hanjaReading": "保(지킬 보) + 安(편안할 안) + 鏡(거울 경)",
        "pronunciation": "낀 바오 호",
        "meaningKo": "눈을 보호하기 위한 안전 보호구로, 건설 현장에서 비산물, 먼지, 화학물질, 강한 빛 등으로부터 시력을 보호합니다. 통역 시 '안경'과 혼동하지 않도록 주의하세요. '고글(goggles)'과 구분하여 일반 안전경은 'kính bảo hộ', 밀폐형 고글은 'kính bảo hộ kín'으로 구분합니다. 용접작업용은 'kính hàn', 레이저 작업용은 'kính chống laser'처럼 용도별로 명확히 구분해야 합니다. 착용 의무 위반 시 산업안전보건법상 처벌 대상이므로 안전교육에서 반드시 강조해야 합니다.",
        "meaningVi": "Thiết bị bảo vệ mắt khỏi các tác nhân nguy hiểm như mảnh vỡ, bụi, hóa chất, ánh sáng mạnh tại công trường xây dựng. Phải đạt tiêu chuẩn TCVN hoặc quốc tế (ANSI Z87.1, EN 166). Có nhiều loại: kính chống bụi, kính hàn, kính chống tia UV, kính kín bảo vệ toàn bộ vùng mắt.",
        "context": "건설 현장 안전교육, 개인보호구 지급, 작업 전 점검",
        "culturalNote": "베트남 건설 현장에서는 착용률이 한국보다 낮은 편이며, 특히 소규모 현장에서는 관리가 느슨합니다. 한국은 '안전보건관리책임자'가 착용 여부를 엄격히 점검하지만, 베트남에서는 'giám sát an toàn lao động'의 권한이 상대적으로 약한 편입니다. 통역 시 한국 기업의 안전 기준을 명확히 전달하고, 착용 의무를 강조해야 합니다. 베트남 근로자들은 더운 날씨로 인해 착용을 꺼리는 경우가 많으므로, 통풍이 잘 되는 제품 선택과 휴식 시간 보장을 함께 안내하는 것이 효과적입니다.",
        "commonMistakes": [
            {
                "mistake": "kính mắt bảo hộ",
                "correction": "kính bảo hộ",
                "explanation": "'kính mắt'는 일반 안경을 의미하므로 불필요. 'kính bảo hộ'만으로 충분"
            },
            {
                "mistake": "kính an toàn",
                "correction": "kính bảo hộ",
                "explanation": "'an toàn'은 일반적 안전, 'bảo hộ'는 산업안전 보호구에 특화된 용어"
            },
            {
                "mistake": "mắt kính bảo hộ",
                "correction": "kính bảo hộ",
                "explanation": "베트남어 어순 오류. 'mắt kính'는 잘못된 표현"
            }
        ],
        "examples": [
            {
                "ko": "모든 작업자는 작업장 출입 시 보안경을 착용해야 합니다.",
                "vi": "Mọi công nhân phải đeo kính bảo hộ khi vào khu vực làm việc.",
                "situation": "formal"
            },
            {
                "ko": "용접할 때는 일반 보안경 말고 용접용 보안경 써야 돼.",
                "vi": "Khi hàn phải đeo kính hàn chứ không phải kính bảo hộ thường.",
                "situation": "onsite"
            },
            {
                "ko": "보안경이 긁혀서 잘 안 보이면 새 걸로 교체 신청하세요.",
                "vi": "Nếu kính bảo hộ bị xước không nhìn rõ thì đề nghị cấp mới.",
                "situation": "informal"
            }
        ],
        "relatedTerms": ["안전모", "안전화", "보호구", "용접면"]
    },
    {
        "slug": "khau-trang-chong-bui",
        "korean": "방진마스크",
        "vietnamese": "khẩu trang chống bụi",
        "hanja": "防塵mask",
        "hanjaReading": "防(막을 방) + 塵(티끌 진)",
        "pronunciation": "카우짱 쫑 부이",
        "meaningKo": "미세먼지, 분진, 석면 등 유해 입자로부터 호흡기를 보호하는 마스크입니다. 통역 시 일반 위생마스크(khẩu trang y tế)와 명확히 구분해야 합니다. 등급별로 KF80, KF94, KF99가 있으며, 베트남에서는 N95, FFP2 등의 표기를 사용합니다. 건설 현장에서는 최소 KF94 이상 착용을 권장하며, 석면 해체 작업 시에는 전동식 방진마스크(khẩu trang chống bụi có quạt) 착용이 법적으로 강제됩니다. 통역 시 '방독면(mặt nạ phòng độc)'과 혼동하지 않도록 주의하세요. 방진은 입자 차단, 방독은 유독가스 차단입니다.",
        "meaningVi": "Khẩu trang lọc bụi mịn, phòng ngừa hít phải các hạt có hại như bụi xi măng, bụi gỗ, thạch miên. Phân loại theo hiệu suất lọc: N95 (95%), N99 (99%), FFP2, FFP3. Phải thay định kỳ và kiểm tra độ kín khít trước khi làm việc. Không dùng khẩu trang y tế thay thế tại công trường.",
        "context": "해체 작업, 연마 작업, 콘크리트 절단, 석면 제거",
        "culturalNote": "베트남 건설 현장에서는 방진마스크 대신 일반 면 마스크나 수건으로 대체하는 경우가 많아 한국 안전관리자들이 가장 시정하기 어려워하는 항목 중 하나입니다. 통역 시 '저렴한 면 마스크는 효과 없음', '법적 의무 사항', '폐질환 위험'을 강조해야 합니다. 베트남 근로자들은 마스크 착용 시 답답함과 더위를 호소하므로, 밸브형(có van thở) 제품을 선택하거나 작업 시간 조정을 함께 제안하면 수용도가 높습니다. 한국에서는 '보건용 마스크'라는 용어도 사용하지만, 베트남에서는 산업용과 의료용을 엄격히 구분합니다.",
        "commonMistakes": [
            {
                "mistake": "khẩu trang bảo hộ",
                "correction": "khẩu trang chống bụi",
                "explanation": "'bảo hộ'는 너무 포괄적. 방진 기능을 명시하는 'chống bụi'가 정확"
            },
            {
                "mistake": "khẩu trang lọc bụi",
                "correction": "khẩu trang chống bụi",
                "explanation": "통용되지만 공식 문서에서는 'chống bụi'가 표준"
            },
            {
                "mistake": "mặt nạ bụi",
                "correction": "khẩu trang chống bụi",
                "explanation": "'mặt nạ'는 전면 마스크(방독면)를 의미. 반면형은 'khẩu trang'"
            }
        ],
        "examples": [
            {
                "ko": "분진 발생 작업장에서는 KF94 이상 방진마스크를 착용하세요.",
                "vi": "Tại khu vực có bụi phải đeo khẩu trang chống bụi cấp KF94 trở lên.",
                "situation": "formal"
            },
            {
                "ko": "마스크 새 걸로 갈아껴. 저거 필터 다 막혔어.",
                "vi": "Thay khẩu trang mới đi. Cái đó lõi lọc đã tắc rồi.",
                "situation": "onsite"
            },
            {
                "ko": "석면 작업할 때는 일회용 마스크 말고 전동식 써야 됩니다.",
                "vi": "Khi tháo dỡ vật liệu có thạch miên phải dùng khẩu trang có quạt, không được dùng loại dùng một lần.",
                "situation": "formal"
            }
        ],
        "relatedTerms": ["방독면", "보호구", "안전모", "석면"]
    },
    {
        "slug": "that-lung-an-toan",
        "korean": "안전벨트",
        "vietnamese": "thắt lưng an toàn",
        "hanja": "安全belt",
        "hanjaReading": "安(편안할 안) + 全(온전할 전)",
        "pronunciation": "탓 룽 안 또안",
        "meaningKo": "고소작업 시 추락을 방지하기 위해 착용하는 개인보호구로, 공식 용어는 '안전대'이지만 현장에서는 '안전벨트'로 더 많이 불립니다. 통역 시 주의할 점은 베트남어로 'dây an toàn'(안전줄)과 'thắt lưng an toàn'(안전벨트/안전대)를 명확히 구분해야 한다는 것입니다. 안전벨트는 몸에 착용하는 하네스(harness)와 추락 방지를 위한 랜야드(dây nối), 그리고 고정점(điểm neo)으로 구성됩니다. 2m 이상 고소작업 시 착용 의무가 있으며, 6개월마다 정기점검을 받아야 합니다. 베트남 현장에서는 '후크(móc)'만 걸고 벨트를 느슨하게 착용하는 경우가 많으므로, 통역 시 '몸에 밀착', '조임 상태 확인'을 반드시 강조하세요.",
        "meaningVi": "Thiết bị bảo vệ cá nhân chống rơi ngã khi làm việc trên cao, bao gồm dây đai toàn thân (full body harness), dây nối (lanyard) và móc khóa (karabiner). Theo quy định phải sử dụng khi làm việc từ 2m trở lên. Phải kiểm tra trước mỗi ca và bảo dưỡng định kỳ 6 tháng/lần.",
        "context": "고소작업, 비계 설치, 철골 조립, 외벽 작업",
        "culturalNote": "베트남 건설 현장에서 안전벨트 착용률은 50% 미만으로 추정되며, 특히 중소형 현장과 베트남 업체에서는 관리가 매우 느슨합니다. 한국 기업 현장에서 가장 많이 충돌하는 안전 이슈 중 하나입니다. 베트남 근로자들은 '움직임이 불편하다', '작업 속도가 느려진다', '걸리적거린다'는 이유로 착용을 거부하는 경우가 많습니다. 통역 시에는 추락 사고의 심각성, 한국 본사의 안전 기준, 법적 처벌을 명확히 전달하되, 일방적 강요보다는 '가족을 위해', '생명 보호'와 같은 감성적 접근이 효과적입니다. 또한 더운 날씨에 착용감이 좋은 메쉬형 제품을 선택하고, 작업 동선에 고정점을 충분히 설치하는 등 환경 개선을 함께 제안하면 수용도가 높아집니다.",
        "commonMistakes": [
            {
                "mistake": "dây an toàn",
                "correction": "thắt lưng an toàn",
                "explanation": "'dây an toàn'은 구명줄/랜야드를 의미. 착용하는 벨트는 'thắt lưng an toàn'"
            },
            {
                "mistake": "đai an toàn",
                "correction": "thắt lưng an toàn",
                "explanation": "'đai'는 단순 띠. 건설 안전용어로는 'thắt lưng'이 표준"
            },
            {
                "mistake": "dây đai bảo hộ",
                "correction": "thắt lưng an toàn",
                "explanation": "혼합된 표현. 공식 용어는 'thắt lưng an toàn'"
            }
        ],
        "examples": [
            {
                "ko": "2미터 이상 높이에서 작업할 때는 반드시 안전벨트를 착용하고 고정점에 연결하세요.",
                "vi": "Khi làm việc trên cao từ 2m trở lên bắt buộc phải đeo thắt lưng an toàn và móc vào điểm neo cố định.",
                "situation": "formal"
            },
            {
                "ko": "벨트 채웠어? 후크 제대로 걸렸나 확인해봐.",
                "vi": "Đã thắt dây chưa? Kiểm tra móc đã khóa chắc chưa.",
                "situation": "onsite"
            },
            {
                "ko": "안전벨트가 헐렁하면 소용없어요. 몸에 꽉 맞게 조여야 합니다.",
                "vi": "Thắt lưng an toàn lỏng lẻo thì vô dụng. Phải thắt chặt vào người mới được.",
                "situation": "informal"
            }
        ],
        "relatedTerms": ["구명줄", "안전고리", "고정점", "추락방지"]
    },
    {
        "slug": "day-cuu-sinh",
        "korean": "구명줄",
        "vietnamese": "dây cứu sinh",
        "hanja": "救命줄",
        "hanjaReading": "救(구할 구) + 命(목숨 명)",
        "pronunciation": "자이 끄우 신",
        "meaningKo": "고소작업 시 안전벨트에 연결하여 추락을 방지하거나, 수상작업 시 인명 구조에 사용하는 줄입니다. 건설 현장에서는 주로 안전벨트의 랜야드(lanyard)를 지칭하며, '안전줄'이라고도 부릅니다. 통역 시 주의할 점은 베트남어로 'dây cứu sinh'는 수상 구조용 로프와 고소작업용 랜야드를 모두 포괄하는 용어라는 점입니다. 명확한 구분이 필요한 경우 고소작업용은 'dây nối an toàn' 또는 'dây lanyard', 수상용은 'dây cứu sinh trên nước'로 구분합니다. 내하중, 길이, 충격흡수장치(giảm sóc) 유무를 확인해야 하며, 사용 전 마모나 손상 여부를 반드시 점검해야 합니다. 추락 사고 발생 시 충격 하중을 받은 구명줄은 폐기해야 합니다.",
        "meaningVi": "Dây nối giữa thắt lưng an toàn và điểm neo, có tác dụng ngăn người lao động rơi xuống khi làm việc trên cao. Thường có thiết bị giảm sóc (shock absorber) để giảm lực va đập khi rơi. Độ dài tiêu chuẩn 1.5m - 2m, chịu tải tối thiểu 22kN.",
        "context": "고소작업, 비계 설치, 철골 작업, 수상 구조",
        "culturalNote": "베트남 건설 현장에서는 구명줄(랜야드)의 길이 조절과 충격흡수장치 확인을 소홀히 하는 경우가 많습니다. 한국에서는 작업 높이에 따라 짧은 줄을 사용하여 추락 거리를 최소화하지만, 베트남 현장에서는 긴 줄을 그대로 사용하여 위험성이 높습니다. 통역 시 '추락 거리 = 줄 길이 + 충격흡수장치 작동거리 + 신장'을 설명하고, 하부 공간이 충분한지 계산하도록 안내해야 합니다. 또한 베트남에서는 나일론 로프를 임의로 잘라 사용하는 경우도 있는데, 이는 매우 위험하므로 '인증된 제품만 사용', '임의 개조 금지'를 명확히 전달해야 합니다.",
        "commonMistakes": [
            {
                "mistake": "dây thừng an toàn",
                "correction": "dây cứu sinh / dây nối an toàn",
                "explanation": "'dây thừng'은 일반 로프. 안전용품은 'dây cứu sinh' 또는 'dây nối'"
            },
            {
                "mistake": "dây kéo",
                "correction": "dây cứu sinh",
                "explanation": "'dây kéo'는 견인줄. 구명/안전 기능이 없는 표현"
            },
            {
                "mistake": "dây bảo vệ",
                "correction": "dây cứu sinh",
                "explanation": "너무 일반적인 표현. 'cứu sinh'이 생명 보호 의미를 명확히 전달"
            }
        ],
        "examples": [
            {
                "ko": "구명줄을 안전벨트와 고정점에 확실히 연결한 후 작업을 시작하세요.",
                "vi": "Kết nối chắc chắn dây cứu sinh với thắt lưng an toàn và điểm neo trước khi bắt đầu làm việc.",
                "situation": "formal"
            },
            {
                "ko": "줄 길이가 너무 길어. 떨어지면 밑에 부딪힐 수 있어.",
                "vi": "Dây dài quá. Nếu rơi có thể va vào bên dưới.",
                "situation": "onsite"
            },
            {
                "ko": "이 구명줄 충격흡수장치 있나요? 없으면 못 써요.",
                "vi": "Dây này có thiết bị giảm sóc không? Không có thì không dùng được.",
                "situation": "informal"
            }
        ],
        "relatedTerms": ["안전벨트", "안전고리", "충격흡수장치", "추락방지"]
    },
    {
        "slug": "luoi-an-toan",
        "korean": "안전네트",
        "vietnamese": "lưới an toàn",
        "hanja": "安全net",
        "hanjaReading": "安(편안할 안) + 全(온전할 전)",
        "pronunciation": "루어이 안 또안",
        "meaningKo": "고소작업 중 사람이나 자재가 추락할 경우 충격을 흡수하여 피해를 최소화하는 그물망입니다. 통역 시 '추락방지망', '낙하물방지망'과 혼동하지 않도록 주의하세요. 베트남어로 모두 'lưới an toàn'이지만, 명확한 구분이 필요한 경우 'lưới chống rơi người'(추락방지), 'lưới chống rơi vật liệu'(낙하물방지)로 구분합니다. 설치 높이, 처짐량, 고정 간격, 망눈 크기 등 기술 기준이 있으며, 3개월마다 정기점검을 실시해야 합니다. 통역 시 '1차 방호: 안전벨트, 2차 방호: 안전네트'라는 개념을 설명하면 이해도가 높아집니다. 충격을 받았거나 자외선에 장기간 노출된 네트는 강도가 저하되므로 교체해야 합니다.",
        "meaningVi": "Lưới bảo vệ được căng dưới khu vực làm việc trên cao để đỡ người hoặc vật rơi xuống. Phân loại: lưới chống rơi người (đỡ người), lưới chống rơi vật liệu (đỡ vật), lưới che chắn (ngăn rơi ra ngoài). Kích thước mắt lưới, độ võng, điểm neo phải đạt tiêu chuẩn. Kiểm tra định kỳ 3 tháng/lần.",
        "context": "비계 작업, 철골 조립, 외벽 작업, 내부 개구부",
        "culturalNote": "베트남 건설 현장에서 안전네트 설치율은 매우 낮으며, 설치하더라도 품질이 낮거나 고정이 불량한 경우가 많습니다. 한국 현장에서는 층별로 촘촘하게 설치하지만, 베트남 현장에서는 비용 절감을 이유로 최소한만 설치하거나 아예 생략하는 경우도 있습니다. 통역 시 안전네트의 중요성과 법적 의무를 강조하되, '한국 기준'과 '베트남 최소 기준'을 구분하여 설명하면 협상이 수월합니다. 또한 베트남에서는 낙하물방지망과 추락방지망을 구분하지 않고 같은 제품을 사용하는 경우가 있는데, 이는 위험하므로 '용도별 전용 제품 사용'을 권장해야 합니다. 중고 제품 사용도 많으므로 '신품 또는 인증된 제품' 사용을 명시하세요.",
        "commonMistakes": [
            {
                "mistake": "lưới bảo vệ",
                "correction": "lưới an toàn",
                "explanation": "'bảo vệ'는 일반 보호. 산업안전용어는 'an toàn'"
            },
            {
                "mistake": "lưới bảo hộ",
                "correction": "lưới an toàn",
                "explanation": "'bảo hộ'는 개인보호구. 시설물은 'an toàn'"
            },
            {
                "mistake": "lưới chắn",
                "correction": "lưới an toàn",
                "explanation": "'chắn'은 차단/차폐. 안전망은 'an toàn'으로 구분"
            }
        ],
        "examples": [
            {
                "ko": "비계 설치 후 각 층마다 안전네트를 빠짐없이 설치하세요.",
                "vi": "Sau khi dựng giàn giáo phải lắp lưới an toàn đầy đủ ở mỗi tầng.",
                "situation": "formal"
            },
            {
                "ko": "네트 처진 데 없나 확인해. 너무 느슨하면 소용없어.",
                "vi": "Kiểm tra lưới có chỗ nào võng không. Lỏng quá thì vô dụng.",
                "situation": "onsite"
            },
            {
                "ko": "이 안전네트 망눈이 너무 큰 것 같은데, 자재가 빠져나갈 수 있어요.",
                "vi": "Lưới này mắt to quá, vật liệu có thể rơi qua được.",
                "situation": "informal"
            }
        ],
        "relatedTerms": ["추락방지", "낙하물방지망", "비계", "개구부"]
    },
    {
        "slug": "ao-phan-quang",
        "korean": "반사조끼",
        "vietnamese": "áo phản quang",
        "hanja": "反射조끼",
        "hanjaReading": "反(돌이킬 반) + 射(쏠 사)",
        "pronunciation": "아오 판 꽝",
        "meaningKo": "어두운 환경이나 차량 통행이 있는 장소에서 작업자의 시인성을 높이기 위해 착용하는 형광색 조끼로, 재귀반사 테이프가 부착되어 있습니다. 통역 시 주의할 점은 '형광조끼'와 '반사조끼'를 구분해야 한다는 것입니다. 형광색만 있는 것은 'áo huỳnh quang', 반사테이프가 있는 것은 'áo phản quang'입니다. 건설 현장에서는 반드시 반사테이프가 있는 제품을 착용해야 하며, 야간 작업 시 필수입니다. 색상은 주로 주황색(màu cam), 노란색(màu vàng), 빨간색(màu đỏ)을 사용하며, 한국에서는 주황색이 표준이지만 베트남에서는 색상 규정이 느슨한 편입니다. 세탁 시 반사 성능이 저하되므로 정기적으로 교체해야 합니다.",
        "meaningVi": "Áo có màu huỳnh quang và dải phản quang giúp người lao động dễ nhìn thấy trong điều kiện thiếu sáng hoặc khi có xe cộ qua lại. Áo phải đạt chuẩn EN 471 hoặc ANSI/ISEA 107. Phân loại: Class 1 (rủi ro thấp), Class 2 (rủi ro trung bình), Class 3 (rủi ro cao - đường cao tốc, ban đêm).",
        "context": "도로 공사, 야간 작업, 중장비 작업 구역, 교통 통제",
        "culturalNote": "베트남 건설 현장에서 반사조끼 착용률은 비교적 높은 편이지만, 품질이 낮은 제품을 사용하거나 반사테이프가 없는 단순 형광조끼를 착용하는 경우가 많습니다. 한국 현장에서는 모든 작업자가 출입 시 착용하지만, 베트남 현장에서는 중장비 운전자나 교통 통제 인력만 착용하는 경우도 있습니다. 통역 시 '모든 작업자 착용 의무', '반사테이프 필수', '오염/파손 시 교체'를 명확히 전달해야 합니다. 베트남의 더운 날씨 때문에 메쉬형 제품을 선호하며, 여름철에는 착용을 꺼리는 경우가 있으므로 통풍이 잘 되는 제품 선택을 권장하세요.",
        "commonMistakes": [
            {
                "mistake": "áo huỳnh quang",
                "correction": "áo phản quang",
                "explanation": "'huỳnh quang'은 형광만 있는 것. 반사테이프 있으면 'phản quang'"
            },
            {
                "mistake": "áo bảo hộ",
                "correction": "áo phản quang",
                "explanation": "'bảo hộ'는 너무 포괄적. 시인성 조끼는 'phản quang'"
            },
            {
                "mistake": "áo ghi lê phản quang",
                "correction": "áo phản quang",
                "explanation": "'ghi lê'는 영어 'gilet'. 베트남어로는 'áo'만으로 충분"
            }
        ],
        "examples": [
            {
                "ko": "현장에 들어올 때는 모든 사람이 반사조끼를 착용해야 합니다.",
                "vi": "Khi vào công trường tất cả mọi người phải mặc áo phản quang.",
                "situation": "formal"
            },
            {
                "ko": "조끼 입고 다녀. 포크레인이 너 못 볼 수 있어.",
                "vi": "Mặc áo vào. Xe xúc có thể không nhìn thấy anh.",
                "situation": "onsite"
            },
            {
                "ko": "이 조끼 반사가 잘 안 돼요. 새 걸로 주세요.",
                "vi": "Áo này phản quang kém. Cho tôi cái mới.",
                "situation": "informal"
            }
        ],
        "relatedTerms": ["안전모", "안전화", "보호구", "시인성"]
    },
    {
        "slug": "mu-han",
        "korean": "용접면",
        "vietnamese": "mũ hàn",
        "hanja": "鎔接面",
        "hanjaReading": "鎔(녹일 용) + 接(이을 접) + 面(낯 면)",
        "pronunciation": "무 한",
        "meaningKo": "용접 작업 시 강한 자외선, 적외선, 불꽃, 비산물로부터 얼굴과 눈을 보호하는 보호구입니다. 통역 시 '용접마스크', '용접헬멧'이라고도 부르지만, 공식 용어는 '용접면'입니다. 베트남어로는 'mũ hàn'(용접 모자) 또는 'mặt nạ hàn'(용접 마스크)을 사용하며, 두 용어 모두 통용됩니다. 수동식(mũ hàn thủ công)과 자동 차광식(mũ hàn tự động tối) 두 종류가 있으며, 최근에는 자동 차광식이 표준이 되어가고 있습니다. 차광도(số bóng tối) 선택이 중요하며, 일반 용접은 11~13번, TIG 용접은 9~11번을 사용합니다. 통역 시 '보안경만으로는 불충분', '전체 얼굴 보호 필수'를 강조해야 합니다.",
        "meaningVi": "Thiết bị bảo vệ mặt và mắt khi hàn, chống tia UV, IR, tia lửa và mảnh vật bay. Có 2 loại: mũ hàn thủ công (phải lật tay) và mũ hàn tự động tối (tự điều chỉnh độ tối khi hàn). Số bóng tối từ 9-13 tùy loại hàn.",
        "context": "용접 작업, 절단 작업, 금속 가공",
        "culturalNote": "베트남 건설 현장에서 용접면 착용률은 높은 편이지만, 구형 수동식 제품을 사용하거나 차광 필터가 손상된 제품을 계속 사용하는 경우가 많습니다. 한국에서는 대부분 자동 차광식을 사용하지만, 베트nam에서는 가격 문제로 수동식을 선호합니다. 통역 시 '자동 차광식이 안전하고 작업 효율도 높음'을 설명하되, 비용 부담이 크다면 최소한 '차광 필터 정기 교체', '파손 즉시 교체'를 강조하세요. 베트남 용접공들은 짧은 작업 시에는 용접면 없이 고개를 돌리거나 손으로 가리는 경우가 있는데, 이는 매우 위험하므로 '짧은 작업도 반드시 착용'을 명확히 전달해야 합니다.",
        "commonMistakes": [
            {
                "mistake": "mặt nạ bảo hộ hàn",
                "correction": "mũ hàn / mặt nạ hàn",
                "explanation": "'bảo hộ' 불필요. 'mũ hàn' 또는 'mặt nạ hàn'이 표준"
            },
            {
                "mistake": "kính hàn",
                "correction": "mũ hàn",
                "explanation": "'kính'는 안경. 전면 보호는 'mũ' 또는 'mặt nạ'"
            },
            {
                "mistake": "mũ bảo vệ hàn",
                "correction": "mũ hàn",
                "explanation": "'bảo vệ' 불필요. 'mũ hàn'만으로 충분"
            }
        ],
        "examples": [
            {
                "ko": "용접 작업 시에는 자동 차광식 용접면을 착용하고 작업하세요.",
                "vi": "Khi hàn phải đeo mũ hàn tự động tối.",
                "situation": "formal"
            },
            {
                "ko": "용접면 필터 깨졌네. 새 거 가져와.",
                "vi": "Kính lọc mũ hàn vỡ rồi. Lấy cái mới.",
                "situation": "onsite"
            },
            {
                "ko": "짧게 용접할 때도 용접면 꼭 써야 돼요. 눈 상할 수 있어요.",
                "vi": "Ngay cả hàn tí cũng phải đeo mũ hàn. Có thể hỏng mắt.",
                "situation": "informal"
            }
        ],
        "relatedTerms": ["용접", "보안경", "보호구", "차광"]
    },
    {
        "slug": "bao-tay-cach-dien",
        "korean": "절연장갑",
        "vietnamese": "bao tay cách điện",
        "hanja": "絕緣장갑",
        "hanjaReading": "絕(끊을 절) + 緣(인연 연)",
        "pronunciation": "바오 따이 까익 지엔",
        "meaningKo": "전기 작업 시 감전을 방지하기 위해 착용하는 고무 재질의 장갑으로, 절연 등급에 따라 사용 가능한 전압이 다릅니다. 통역 시 주의할 점은 일반 작업용 장갑과 명확히 구분해야 한다는 것입니다. 베트남어로 일반 장갑은 'găng tay', 절연장갑은 'bao tay cách điện' 또는 'găng tay cách điện'입니다. 절연 등급은 Class 00(500V), Class 0(1,000V), Class 1(7,500V), Class 2(17,000V) 등이 있으며, 작업 전압보다 높은 등급을 선택해야 합니다. 통역 시 '전압 확인', '등급 선택', '외관 점검', '6개월 내압시험'을 강조하세요. 절연장갑만으로는 불충분하며, 그 위에 보호용 가죽장갑(găng tay bảo vệ da)을 착용하는 것이 표준입니다.",
        "meaningVi": "Găng tay cao su cách điện bảo vệ khỏi điện giật khi làm việc với thiết bị điện. Phân loại theo điện áp: Class 00 (500V), Class 0 (1000V), Class 1 (7500V), Class 2 (17kV). Phải kiểm tra trước mỗi lần dùng và thử nghiệm chịu áp 6 tháng/lần.",
        "context": "전기 공사, 배전반 작업, 활선 작업, 점검 작업",
        "culturalNote": "베트남 건설 현장에서 전기 작업 시 절연장갑 착용률은 매우 낮으며, 일반 작업용 장갑이나 맨손으로 작업하는 경우가 많습니다. 특히 소규모 현장이나 긴급 수리 시에는 안전 수칙을 무시하는 경우가 빈번합니다. 한국 안전관리자들이 가장 우려하는 부분 중 하나로, 통역 시 '감전 사망 사고의 심각성', '법적 처벌', '작업 중지 권한'을 명확히 전달해야 합니다. 베트남 전기공들은 '경험으로 알아서 한다', '저전압은 괜찮다'는 잘못된 인식을 가진 경우가 많으므로, '전압 무관 착용 의무', '단 한 번의 실수가 생명'을 강조해야 합니다. 또한 절연장갑의 외관 점검(공기 주입 테스트) 방법을 교육하면 실효성이 높아집니다.",
        "commonMistakes": [
            {
                "mistake": "găng tay điện",
                "correction": "bao tay cách điện",
                "explanation": "'găng tay điện'은 불명확. 정확한 용어는 'bao tay cách điện'"
            },
            {
                "mistake": "găng tay cao su",
                "correction": "bao tay cách điện",
                "explanation": "'cao su'는 재질만 표현. 절연 기능을 명시해야 함"
            },
            {
                "mistake": "bao tay bảo hộ điện",
                "correction": "bao tay cách điện",
                "explanation": "'bảo hộ điện'은 어색한 표현. 'cách điện'이 표준"
            }
        ],
        "examples": [
            {
                "ko": "저압 배전반 작업 시에는 최소 Class 0 절연장갑을 착용하세요.",
                "vi": "Khi làm việc với tủ điện hạ áp phải đeo bao tay cách điện tối thiểu Class 0.",
                "situation": "formal"
            },
            {
                "ko": "장갑에 구멍 없나 확인하고 써. 감전되면 큰일이야.",
                "vi": "Kiểm tra găng không thủng rồi mới đeo. Bị điện giật thì nguy hiểm lắm.",
                "situation": "onsite"
            },
            {
                "ko": "절연장갑만 끼지 말고 그 위에 가죽장갑도 같이 껴야 합니다.",
                "vi": "Không chỉ đeo găng cách điện mà phải đeo thêm găng da bên ngoài.",
                "situation": "informal"
            }
        ],
        "relatedTerms": ["절연화", "감전방지", "활선작업", "전기안전"]
    },
    {
        "slug": "giay-chong-dinh",
        "korean": "방정전화",
        "vietnamese": "giày chống tĩnh điện",
        "hanja": "防靜電靴",
        "hanjaReading": "防(막을 방) + 靜(고요할 정) + 電(번개 전) + 靴(신 화)",
        "pronunciation": "자이 쫑 띵 지엔",
        "meaningKo": "정전기 발생을 방지하고 인체에 축적된 정전기를 안전하게 방전시키는 안전화입니다. 통역 시 주의할 점은 '절연화(giày cách điện)'와 명확히 구분해야 한다는 것입니다. 절연화는 감전을 막기 위해 전기를 차단하지만, 방정전화는 정전기를 땅으로 흘려보냅니다. 반도체 공장, 화학 플랜트, 폭발 위험 구역에서 필수이며, 표면저항이 10^6~10^8 Ω 범위여야 합니다. 베트남어로 'giày chống tĩnh điện' 또는 'giày ESD'(Electrostatic Discharge)로 불립니다. 일반 안전화와 외관상 구분이 어려우므로, 통역 시 'ESD 마크 확인', '정기 저항 측정'을 강조하세요. 건조한 환경에서 특히 중요하며, 바닥도 도전성 바닥재(sàn chống tĩnh điện)여야 효과가 있습니다.",
        "meaningVi": "Giày có khả năng dẫn điện tĩnh từ cơ thể xuống đất, ngăn tích tụ điện tích và phóng tia lửa. Bắt buộc tại khu vực có nguy cơ cháy nổ, nhà máy điện tử, hóa chất. Điện trở bề mặt: 10^6 - 10^8 Ω. Phải kiểm tra định kỳ bằng máy đo điện trở.",
        "context": "정유 공장, 화학 플랜트, 전자 공장, 도장 작업장",
        "culturalNote": "베트남 건설 및 제조 현장에서 방정전화의 개념이 잘 알려져 있지 않으며, 일반 안전화로 대체하는 경우가 많습니다. 한국 기업이 베트남에 전자 공장이나 화학 플랜트를 운영할 때 가장 많이 부딪히는 문제 중 하나입니다. 통역 시 '정전기 불꽃으로 인한 폭발 위험', '전자 제품 손상', 'ESD 규정 준수'를 명확히 설명해야 합니다. 베트남 근로자들은 방정전화와 일반 안전화의 차이를 이해하지 못하는 경우가 많으므로, '전기가 흐르는 신발', '정전기를 땅으로 보내는 신발'처럼 쉬운 용어로 설명하고, 실제 저항 측정 시연을 통해 이해도를 높이는 것이 효과적입니다.",
        "commonMistakes": [
            {
                "mistake": "giày an toàn điện",
                "correction": "giày chống tĩnh điện",
                "explanation": "'an toàn điện'은 모호함. 정전기 방지 기능을 명시해야 함"
            },
            {
                "mistake": "giày cách điện",
                "correction": "giày chống tĩnh điện",
                "explanation": "'cách điện'은 절연화(감전 방지). 방정전화는 'chống tĩnh điện'"
            },
            {
                "mistake": "giày điện",
                "correction": "giày chống tĩnh điện",
                "explanation": "너무 축약된 표현. 정확한 기능 명시 필요"
            }
        ],
        "examples": [
            {
                "ko": "폭발 위험 구역에 출입할 때는 방정전화를 착용하고 저항값을 측정해야 합니다.",
                "vi": "Khi vào khu vực nguy hiểm cháy nổ phải đi giày chống tĩnh điện và đo giá trị điện trở.",
                "situation": "formal"
            },
            {
                "ko": "이 신발 ESD 마크 있어? 없으면 못 들어가.",
                "vi": "Giày này có nhãn ESD không? Không có thì không được vào.",
                "situation": "onsite"
            },
            {
                "ko": "방정전화 신고 도전성 바닥에서만 효과 있어요. 일반 바닥은 소용없어요.",
                "vi": "Giày chống tĩnh điện chỉ có tác dụng trên sàn dẫn điện. Sàn thường thì vô ích.",
                "situation": "informal"
            }
        ],
        "relatedTerms": ["절연화", "안전화", "정전기", "폭발방지"]
    },
    {
        "slug": "mat-na-phong-doc",
        "korean": "방독면",
        "vietnamese": "mặt nạ phòng độc",
        "hanja": "防毒面",
        "hanjaReading": "防(막을 방) + 毒(독 독) + 面(낯 면)",
        "pronunciation": "맛 나 퐁 독",
        "meaningKo": "유해 가스, 증기, 분진 등으로부터 호흡기를 보호하는 보호구로, 정화통(lọc khí) 또는 공기 공급 장치가 있습니다. 통역 시 '방진마스크(khẩu trang chống bụi)'와 명확히 구분해야 합니다. 방진마스크는 입자를 걸러내지만, 방독면은 화학물질 가스를 정화합니다. 베트남어로 'mặt nạ phòng độc' 또는 'mặt nạ lọc khí'를 사용하며, 종류에 따라 반면형(nửa mặt), 전면형(toàn mặt), 송기식(cấp khí), 자급식(tự cấp khí)으로 구분됩니다. 정화통은 유해물질 종류에 따라 색상 코드(màu lọc)가 있으며, 사용 시간 제한이 있습니다. 통역 시 '정화통 종류 확인', '교체 주기 준수', '밀착 테스트 필수'를 강조하세요. 산소 농도 18% 미만 환경에서는 송기식/자급식만 사용 가능합니다.",
        "meaningVi": "Thiết bị bảo vệ hô hấp chống khí độc, hơi hóa chất. Có 2 loại chính: mặt nạ lọc khí (dùng phin lọc) và mặt nạ cấp khí (cấp khí sạch từ bên ngoài). Phin lọc có mã màu theo loại hóa chất: nâu (hữu cơ), xám (vô cơ), vàng (axit), xanh (amoniac), đỏ (CO).",
        "context": "화학물질 취급, 도장 작업, 밀폐 공간 작업, 가스 누출",
        "culturalNote": "베트남 건설 현장에서 방독면 사용은 매우 제한적이며, 화학물질 작업 시에도 방진마스크나 일반 마스크로 대체하는 경우가 많습니다. 한국 기업이 운영하는 공장이나 대형 건설 현장에서 가장 큰 안전 격차를 보이는 항목 중 하나입니다. 통역 시 '방진마스크는 가스 차단 불가', '화학물질별 정화통 선택', '밀폐 공간 작업 시 송기식 필수'를 명확히 전달해야 합니다. 베트남 근로자들은 방독면 착용 시 호흡 곤란과 답답함을 호소하므로, 사전 훈련과 적응 시간 제공, 작업 시간 조정이 필요합니다. 또한 정화통 교체 시기를 놓치는 경우가 많으므로, '사용 시간 기록', '냄새 감지 시 즉시 교체', '예비 정화통 준비'를 강조하세요.",
        "commonMistakes": [
            {
                "mistake": "khẩu trang phòng độc",
                "correction": "mặt nạ phòng độc",
                "explanation": "'khẩu trang'은 반면형 마스크. 방독면은 'mặt nạ'"
            },
            {
                "mistake": "mặt nạ chống khí độc",
                "correction": "mặt nạ phòng độc",
                "explanation": "통용되지만 공식 용어는 'phòng độc'"
            },
            {
                "mistake": "mặt nạ hóa chất",
                "correction": "mặt nạ phòng độc",
                "explanation": "너무 일반적. '방독(phòng độc)'이 표준 용어"
            }
        ],
        "examples": [
            {
                "ko": "화학물질 저장 탱크 내부 작업 시에는 송기식 방독면을 착용해야 합니다.",
                "vi": "Khi làm việc bên trong bể chứa hóa chất phải đeo mặt nạ phòng độc cấp khí.",
                "situation": "formal"
            },
            {
                "ko": "페인트 냄새 나면 정화통 갈아야 돼. 계속 쓰면 안 돼.",
                "vi": "Ngửi thấy mùi sơn thì phải thay phin lọc. Không được dùng tiếp.",
                "situation": "onsite"
            },
            {
                "ko": "방독면 쓰기 전에 밀착 테스트 꼭 해야 돼요. 새는 곳 있으면 소용없어요.",
                "vi": "Trước khi đeo phải test độ kín. Nếu rò khí thì vô dụng.",
                "situation": "informal"
            }
        ],
        "relatedTerms": ["방진마스크", "정화통", "송기식", "밀폐공간"]
    }
]

# Filter out duplicates
new_terms_to_add = [t for t in new_terms if t['slug'] not in existing_slugs]

if not new_terms_to_add:
    print("⚠️  All terms already exist. No new terms added.")
else:
    # Add new terms
    data.extend(new_terms_to_add)

    # Save back to file
    with open(file_path, 'w', encoding='utf-8') as f:
        json.dump(data, f, ensure_ascii=False, indent=2)

    print(f"✅ Added {len(new_terms_to_add)} new construction safety PPE terms")
    print(f"📊 Total terms in construction.json: {len(data)}")
    for term in new_terms_to_add:
        print(f"   - {term['slug']} ({term['korean']})")
