#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
건설 수학/단위/측정 용어 추가 스크립트 (Construction Math, Units, Measurements)
Tier S 품질 기준 준수
"""

import json
import os

# 파일 경로 설정
file_path = os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', 'data', 'terms', 'construction.json')

# 기존 데이터 로드
with open(file_path, 'r', encoding='utf-8') as f:
    data = json.load(f)  # data is a LIST

# 기존 slug 추출
existing_slugs = {t['slug'] for t in data}

# 새 용어 정의
new_terms = [
    {
        "slug": "chieu-dai",
        "korean": "길이",
        "vietnamese": "chiều dài",
        "hanja": "長",
        "hanjaReading": "長(길 장)",
        "pronunciation": "지으다이",
        "meaningKo": "한 점에서 다른 점까지의 공간적 거리를 나타내는 기본 측정 단위. 건설 현장에서 가장 빈번하게 사용되는 측정값으로, 통역 시 베트남에서는 미터법(mét)을 표준으로 사용하지만 일부 현장에서 피트(feet)나 인치(inch) 단위도 혼용되므로 단위 확인이 필수입니다. 도면 검토 시 '길이'와 '폭'을 혼동하지 않도록 주의하며, 베트남어로는 chiều dài(길이), chiều rộng(폭), chiều cao(높이)를 명확히 구분해야 합니다.",
        "meaningVi": "Khoảng cách không gian từ điểm này đến điểm khác, là đơn vị đo lường cơ bản nhất trong xây dựng. Tại Việt Nam sử dụng hệ mét (mét, cm, mm) là chuẩn, nhưng một số công trình do nước ngoài đầu tư có thể dùng feet hoặc inch. Cần phân biệt rõ chiều dài, chiều rộng và chiều cao khi đọc bản vẽ để tránh nhầm lẫn trong thi công.",
        "context": "도면 검토, 자재 주문, 현장 측량, 시공 지시",
        "culturalNote": "한국은 미터법을 공식 사용하지만 건설 현장에서 '자(尺)', '치(寸)' 등 전통 단위를 구어로 쓰는 경우가 있습니다. 베트남은 프랑스 식민지 영향으로 미터법이 완전히 정착되어 전통 단위는 거의 사용되지 않으며, 'mét'(미터), 'cm'(센티미터)가 표준입니다. 한국인 발주자가 '3자 반'이라고 말하면 약 1.05m를 의미하므로, 통역 시 미터로 환산하여 전달해야 오해를 방지할 수 있습니다.",
        "commonMistakes": [
            {
                "mistake": "chiều dài를 '칭다이'로 발음",
                "correction": "'지으다이'로 발음 (성조 huyền on 'chiều')",
                "explanation": "베트nam어 성조를 무시하면 의미가 달라지거나 이해되지 않음"
            },
            {
                "mistake": "'길이'를 kích thước로 통역",
                "correction": "chiều dài (길이 자체) vs kích thước (치수/크기 전체)",
                "explanation": "kích thước는 길이, 폭, 높이를 포함하는 포괄적 개념"
            },
            {
                "mistake": "단위 없이 숫자만 전달 ('10'이라고만 말함)",
                "correction": "'10 mét' 또는 '10 cm'처럼 단위 명시",
                "explanation": "건설 현장에서 단위 누락은 치명적 시공 오류로 이어질 수 있음"
            }
        ],
        "examples": [
            {
                "ko": "이 보의 길이가 5미터인데, 실제로는 4.95미터밖에 안 돼요.",
                "vi": "Chiều dài của dầm này là 5 mét, nhưng thực tế chỉ có 4,95 mét thôi.",
                "situation": "onsite"
            },
            {
                "ko": "설계도상 기둥 간격은 6미터입니다.",
                "vi": "Theo bản vẽ thiết kế, khoảng cách giữa các cột là 6 mét.",
                "situation": "formal"
            },
            {
                "ko": "케이블 길이 좀 재봐. 모자랄 것 같아.",
                "vi": "Đo chiều dài cáp xem. Có vẻ thiếu đấy.",
                "situation": "informal"
            }
        ],
        "relatedTerms": ["chiều rộng (폭)", "chiều cao (높이)", "kích thước (치수)", "đơn vị đo (측정 단위)"]
    },
    {
        "slug": "dien-tich",
        "korean": "면적",
        "vietnamese": "diện tích",
        "hanja": "面積",
        "hanjaReading": "面(낯 면) + 積(쌓을 적)",
        "pronunciation": "지엔틱",
        "meaningKo": "2차원 평면의 넓이를 나타내는 측정값으로, 제곱미터(m²)로 표시됩니다. 건설 프로젝트에서 부지 면적, 건축 면적, 연면적, 전용 면적 등을 계산할 때 필수적으로 사용되며, 통역 시 '면적'과 '평수'를 혼동하지 않도록 주의해야 합니다. 한국에서는 관습적으로 '평(坪)'을 많이 쓰지만(1평 ≈ 3.3㎡), 베트남에서는 평 개념이 없고 제곱미터(m²)만 사용하므로, 한국인 발주자가 '50평'이라고 하면 약 165㎡로 환산하여 전달해야 합니다.",
        "meaningVi": "Độ lớn của bề mặt phẳng hai chiều, tính bằng mét vuông (m²). Trong xây dựng, diện tích được dùng để tính diện tích đất, diện tích xây dựng, diện tích sàn, diện tích sử dụng. Việt Nam chỉ dùng m² và ha (hecta), không có khái niệm 'bình' (평) như Hàn Quốc. Khi người Hàn nói '50 bình', cần quy đổi ra khoảng 165m² để tránh hiểu nhầm.",
        "context": "부지 측량, 면적 산정, 분양, 인허가 서류",
        "culturalNote": "한국은 부동산 거래에서 '평(坪)' 단위를 관습적으로 사용하며(1평=3.305785㎡), 법적으로는 제곱미터를 쓰지만 일상에서는 평이 더 익숙합니다. 베트남은 프랑스 식민지 영향으로 미터법만 사용하며, 토지 면적은 m²나 ha(헥타르)로만 표기합니다. 통역 시 한국 클라이언트가 평 단위로 말하면 즉시 m²로 환산해 전달해야 하며, 계약서에는 반드시 m²로 명시되어야 법적 분쟁을 피할 수 있습니다.",
        "commonMistakes": [
            {
                "mistake": "'면적'을 kích thước로 통역",
                "correction": "diện tích (면적) vs kích thước (치수)",
                "explanation": "diện tích는 2차원 넓이, kích thước는 길이/폭/높이 등 치수 전반"
            },
            {
                "mistake": "평(坪)을 그대로 'bình'로 옮김",
                "correction": "평을 m²로 환산하여 전달 (예: 30평 → 약 99㎡)",
                "explanation": "베트남에는 평 개념이 없어 환산 없이 전달하면 이해 불가"
            },
            {
                "mistake": "'제곱미터'를 mét로만 말함",
                "correction": "mét vuông 또는 m² (메뜨 붕)",
                "explanation": "mét는 길이 단위, mét vuông가 면적 단위"
            }
        ],
        "examples": [
            {
                "ko": "이 부지의 면적은 500제곱미터입니다.",
                "vi": "Diện tích của khu đất này là 500 mét vuông.",
                "situation": "formal"
            },
            {
                "ko": "30평짜리 아파트면 베트남에서는 몇 제곱미터예요?",
                "vi": "Căn hộ 30 bình thì ở Việt Nam là khoảng bao nhiêu mét vuông? (Khoảng 99m²)",
                "situation": "informal"
            },
            {
                "ko": "건축 면적과 연면적을 구분해서 보고해 주세요.",
                "vi": "Báo cáo riêng diện tích xây dựng và tổng diện tích sàn nhé.",
                "situation": "onsite"
            }
        ],
        "relatedTerms": ["chiều dài (길이)", "thể tích (체적)", "mét vuông (제곱미터)", "kích thước (치수)"]
    },
    {
        "slug": "the-tich",
        "korean": "체적",
        "vietnamese": "thể tích",
        "hanja": "體積",
        "hanjaReading": "體(몸 체) + 積(쌓을 적)",
        "pronunciation": "테틱",
        "meaningKo": "3차원 공간이 차지하는 부피를 나타내는 측정값으로, 세제곱미터(m³)로 표시됩니다. 건설 현장에서 콘크리트 타설량, 토공량, 자재 부피 등을 계산할 때 필수적이며, 통역 시 '체적'과 '용적'을 혼동하지 않도록 주의해야 합니다. 콘크리트 주문 시 베트남에서는 m³ 단위를 사용하며, 레미콘 1대(truck)의 용량이 보통 5~7m³임을 알아두면 현장 통역에 유용합니다. 한국에서 '입방미터' 또는 '세제곱미터'라고도 하며, 약어로 '㎥' 또는 'm³'를 씁니다.",
        "meaningVi": "Độ lớn của không gian ba chiều, tính bằng mét khối (m³). Trong xây dựng dùng để đo lượng bê tông đổ, khối lượng đào đắp đất, thể tích vật liệu. Việt Nam dùng m³ làm đơn vị chuẩn, xe trộn bê tông thường có dung tích 5-7m³. Cần phân biệt thể tích (không gian thực) và dung tích (khả năng chứa), tuy nhiên trong thực tế xây dựng hai thuật ngữ này thường dùng thay thế nhau.",
        "context": "콘크리트 주문, 토공량 산출, 자재 견적, 운반 계획",
        "culturalNote": "한국과 베트남 모두 체적 단위로 세제곱미터(m³)를 표준 사용하지만, 한국 현장에서는 '입방'이라는 표현을 더 자주 쓰고('콘크리트 10입방 쳐'), 베트남에서는 'khối' 또는 'm³'(메뜨 코이)라고 합니다. 레미콘 주문 시 한국은 '몇 대'보다 '몇 입방'으로 말하는 경우가 많고, 베트남은 '몇 xe'(차) 또는 '몇 m³'로 주문합니다. 통역 시 대수와 체적을 혼동하지 않도록 명확히 확인해야 합니다.",
        "commonMistakes": [
            {
                "mistake": "'체적'을 dung tích로만 통역",
                "correction": "thể tích (일반 부피) vs dung tích (용기의 수용 능력)",
                "explanation": "thể tích는 물체 자체의 부피, dung tích는 담을 수 있는 양"
            },
            {
                "mistake": "'입방미터'를 mét로만 말함",
                "correction": "mét khối 또는 m³ (메뜨 코이)",
                "explanation": "mét는 길이, mét khối가 부피 단위"
            },
            {
                "mistake": "콘크리트 '10대'를 '10m³'로 잘못 통역",
                "correction": "차량 대수와 체적을 구분하여 확인 후 통역",
                "explanation": "1대는 보통 5~7m³이므로 10대는 약 50~70m³"
            }
        ],
        "examples": [
            {
                "ko": "오늘 콘크리트 30입방 타설 예정입니다.",
                "vi": "Hôm nay dự kiến đổ 30 mét khối bê tông.",
                "situation": "formal"
            },
            {
                "ko": "레미콘 5대 오면 몇 입방이에요?",
                "vi": "5 xe trộn bê tông thì được khoảng bao nhiêu m³? (Khoảng 25-35m³)",
                "situation": "informal"
            },
            {
                "ko": "토공량 계산해서 내일까지 보고 좀 해줘.",
                "vi": "Tính khối lượng đất đào đắp rồi báo cáo trước ngày mai nhé.",
                "situation": "onsite"
            }
        ],
        "relatedTerms": ["diện tích (면적)", "khối lượng (물량)", "dung tích (용적)", "mét khối (세제곱미터)"]
    },
    {
        "slug": "don-vi-do",
        "korean": "측정 단위",
        "vietnamese": "đơn vị đo",
        "hanja": "測定單位",
        "hanjaReading": "測(헤아릴 측) + 定(정할 정) + 單(홑 단) + 位(자리 위)",
        "pronunciation": "던비도",
        "meaningKo": "물리량을 수치로 표현하기 위한 기준이 되는 단위로, 길이(m), 면적(m²), 부피(m³), 무게(kg), 압력(MPa) 등을 포함합니다. 건설 현장에서 측정 단위를 명확히 하지 않으면 시공 오류, 자재 낭비, 안전사고로 이어질 수 있으므로, 통역 시 반드시 단위를 함께 전달해야 합니다. 한국과 베트남 모두 SI 단위계(미터법)를 공식 사용하지만, 한국은 전통 단위(자, 치, 근)를 구어로 쓰는 경우가 있고, 베트남은 미터법이 완전히 정착되어 있어 통역 시 환산이 필요할 수 있습니다.",
        "meaningVi": "Tiêu chuẩn để biểu thị giá trị số của đại lượng vật lý, bao gồm chiều dài (m), diện tích (m²), thể tích (m³), khối lượng (kg), áp suất (MPa)... Trong xây dựng, nếu không nói rõ đơn vị đo có thể dẫn đến sai sót thi công, lãng phí vật liệu, tai nạn an toàn. Việt Nam dùng hệ đo lường quốc tế SI (hệ mét), không còn dùng đơn vị cũ, nên khi người Hàn dùng đơn vị truyền thống cần quy đổi sang hệ mét.",
        "context": "도면 검토, 자재 주문, 시공 지시, 검수",
        "culturalNote": "한국은 SI 단위계를 공식 채택했지만 건설 현장에서 '자(尺, 약 30.3cm)', '치(寸, 약 3.03cm)', '평(坪, 약 3.3m²)' 같은 전통 단위를 구어로 여전히 사용합니다. 베트남은 프랑스 식민지 시절부터 미터법이 정착되어 전통 단위는 거의 쓰이지 않으며, 'mét', 'kg', 'm²' 등만 사용합니다. 통역 시 한국 측이 전통 단위로 말하면 즉시 SI 단위로 환산하여 전달해야 하며, 계약서나 공식 문서에는 반드시 SI 단위로 명시해야 분쟁을 예방할 수 있습니다.",
        "commonMistakes": [
            {
                "mistake": "단위 없이 숫자만 통역 ('10'이라고만 말함)",
                "correction": "반드시 단위와 함께 전달 ('10 mét', '10 kg')",
                "explanation": "건설 현장에서 단위 누락은 치명적 오류의 원인"
            },
            {
                "mistake": "'자', '치', '평' 등 한국 전통 단위를 그대로 통역",
                "correction": "즉시 미터법으로 환산 (3자 → 약 0.9m)",
                "explanation": "베트남에서는 전통 단위 개념이 없어 이해 불가"
            },
            {
                "mistake": "mét와 mét vuông를 혼동",
                "correction": "mét (길이), mét vuông (면적), mét khối (부피) 구분",
                "explanation": "차원이 다른 단위를 혼동하면 계산 오류 발생"
            }
        ],
        "examples": [
            {
                "ko": "철근 직경은 밀리미터 단위로 표기합니다.",
                "vi": "Đường kính cốt thép được ký hiệu bằng đơn vị milimét.",
                "situation": "formal"
            },
            {
                "ko": "이 파이프 3자짜리로 주문해. (약 0.9m)",
                "vi": "Đặt ống loại khoảng 0,9 mét nhé.",
                "situation": "informal"
            },
            {
                "ko": "압력 단위 MPa로 써주세요, PSI 아니고요.",
                "vi": "Ghi đơn vị áp suất bằng MPa, không phải PSI.",
                "situation": "onsite"
            }
        ],
        "relatedTerms": ["chiều dài (길이)", "diện tích (면적)", "thể tích (체적)", "khối lượng (질량)"]
    },
    {
        "slug": "ti-le",
        "korean": "비율",
        "vietnamese": "tỉ lệ",
        "hanja": "比率",
        "hanjaReading": "比(견줄 비) + 率(비율 률)",
        "pronunciation": "띠레",
        "meaningKo": "두 수량 간의 상대적 크기를 나타내는 수치로, 건설 현장에서는 배합비(시멘트:모래:자갈), 경사비(높이:거리), 축척(도면:실제) 등에 사용됩니다. 통역 시 '비율'과 '비'를 혼동하지 않도록 주의하며, 베트남어로는 tỉ lệ라고 하지만 구체적 상황에 따라 tỷ lệ phối trộn(배합비), tỷ lệ dốc(경사비), tỷ lệ xích(축척) 등으로 세분화됩니다. 콘크리트 배합비는 품질에 직결되므로 숫자 하나라도 잘못 전달하면 구조적 결함으로 이어질 수 있어 각별한 주의가 필요합니다.",
        "meaningVi": "Giá trị tương đối giữa hai đại lượng, trong xây dựng dùng cho tỷ lệ phối trộn (xi măng:cát:đá), tỷ lệ dốc (chiều cao:khoảng cách ngang), tỷ lệ xích (bản vẽ:thực tế). Tỷ lệ phối trộn bê tông ảnh hưởng trực tiếp đến chất lượng công trình, nên cần thông dịch chính xác từng con số. Trong tiếng Việt, 'tỉ lệ' là thuật ngữ chung, nhưng tùy ngữ cảnh có thể thêm từ cụ thể như tỷ lệ phối trộn, tỷ lệ dốc, tỷ lệ xích.",
        "context": "콘크리트 배합, 경사 설계, 도면 축척, 품질 관리",
        "culturalNote": "한국과 베트남 모두 비율 표기는 콜론(:) 또는 대 기호를 사용하지만, 한국 현장에서는 '몇 대 몇'이라고 구어로 표현하고('1대3 배합'), 베트남에서는 '몇 나 몇'(một na ba) 또는 '1:3'으로 읽습니다. 콘크리트 배합비는 한국이 좀 더 엄격한 품질 기준을 요구하는 경향이 있어, 한국 감리자가 배합비 준수를 강조하면 베트남 현장 인력에게 중요성을 충분히 설명해야 합니다. 축척 표기는 양국 모두 1:50, 1:100 등으로 동일하게 씁니다.",
        "commonMistakes": [
            {
                "mistake": "'1:3 배합'을 '1-3 phối trộn'으로 통역",
                "correction": "tỷ lệ phối trộn 1 na 3 hoặc 1:3 (một chia ba)",
                "explanation": "'na' 또는 콜론(:)으로 비율 표현, 하이픈(-)은 범위 의미"
            },
            {
                "mistake": "경사 '1:10'을 10% 기울기로 환산 없이 통역",
                "correction": "độ dốc 1:10 (또는 10%) 명확히 구분하여 전달",
                "explanation": "1:10은 10% 기울기와 다름 (1:10 ≈ 5.7도, 10% ≈ 5.7도이지만 개념이 다름)"
            },
            {
                "mistake": "축척 '1:50'을 '50배'로 잘못 통역",
                "correction": "tỷ lệ xích 1:50 (một phần năm mươi, 축소)",
                "explanation": "축척은 축소 비율이므로 '50배 확대'가 아님"
            }
        ],
        "examples": [
            {
                "ko": "이 구간은 콘크리트 배합비를 1:2:4로 맞춰주세요.",
                "vi": "Đoạn này tỷ lệ phối trộn bê tông là 1:2:4 (xi măng:cát:đá) nhé.",
                "situation": "formal"
            },
            {
                "ko": "경사가 1:12 이상이면 안 돼요, 너무 급해요.",
                "vi": "Độ dốc không được quá 1:12, dốc quá nguy hiểm.",
                "situation": "onsite"
            },
            {
                "ko": "도면 축척 1:100이니까 실제로는 100배 크다는 거지?",
                "vi": "Tỷ lệ xích bản vẽ 1:100 nghĩa là thực tế lớn hơn 100 lần phải không?",
                "situation": "informal"
            }
        ],
        "relatedTerms": ["tỷ lệ phối trộn (배합비)", "tỷ lệ dốc (경사비)", "tỷ lệ xích (축척)", "phần trăm (백분율)"]
    },
    {
        "slug": "do-nghieng",
        "korean": "경사도",
        "vietnamese": "độ nghiêng",
        "hanja": "傾斜度",
        "hanjaReading": "傾(기울 경) + 斜(비낄 사) + 度(도 도)",
        "pronunciation": "도응이엥",
        "meaningKo": "수평면에 대한 기울어진 정도를 나타내는 측정값으로, 백분율(%), 각도(°), 비율(1:n) 등으로 표현됩니다. 건설 현장에서 도로, 배수로, 경사로, 지붕 등의 기울기를 설계하고 시공할 때 필수적이며, 통역 시 경사도 표현 방식(%, 각도, 비율)을 명확히 구분해야 합니다. 배수를 위한 최소 경사도(보통 0.5~1%), 휠체어 접근로 최대 경사도(8.33% = 1:12), 지붕 경사도(보통 15~45도) 등 용도별 기준이 다르므로 맥락에 맞게 통역해야 합니다.",
        "meaningVi": "Mức độ nghiêng so với mặt phẳng nằm ngang, biểu thị bằng phần trăm (%), góc độ (°), hoặc tỷ lệ (1:n). Trong xây dựng, độ nghiêng dùng cho đường, rãnh thoát nước, đường dốc, mái nhà. Cần phân biệt rõ cách biểu thị: % (phần trăm), độ (góc), tỷ lệ (ví dụ 1:12). Độ dốc tối thiểu cho thoát nước (0,5-1%), độ dốc tối đa cho đường dốc xe lăn (8,33% = 1:12), độ dốc mái (15-45 độ) đều có tiêu chuẩn riêng.",
        "context": "도로 설계, 배수 계획, 경사로 시공, 지붕 구조",
        "culturalNote": "한국과 베트남 모두 경사도를 백분율(%), 각도(도), 비율(1:n)로 표현하지만, 사용 관행이 다릅니다. 한국 건설 현장에서는 도로 경사를 주로 백분율(%)로 말하고('5% 경사'), 베트남에서는 비율(1:20) 또는 백분율을 혼용합니다. 지붕 경사는 양국 모두 각도(도)를 많이 쓰지만, 한국 전통 한옥에서는 '물매'라는 독특한 표현을 쓰기도 합니다. 통역 시 숫자만 전달하지 말고 단위(%, 도, 비율)를 반드시 명시해야 오해를 방지할 수 있습니다.",
        "commonMistakes": [
            {
                "mistake": "'5% 경사'를 góc 5 độ로 잘못 통역",
                "correction": "độ dốc 5% (phần trăm) hoặc góc khoảng 2,86 độ",
                "explanation": "5%는 백분율이고, 각도로는 약 2.86도 (tan⁻¹(0.05))"
            },
            {
                "mistake": "'1:10 경사'를 '1도에서 10도 사이'로 오해",
                "correction": "tỷ lệ dốc 1:10 (chiều cao 1, chiều ngang 10)",
                "explanation": "1:10은 비율 표기이지 각도 범위가 아님"
            },
            {
                "mistake": "độ nghiêng을 '도응이응'으로 잘못 발음",
                "correction": "'도응이엥' (nghiêng은 성조 huyền + thanh hỏi)",
                "explanation": "베트남어 성조를 틀리면 의미 전달 실패"
            }
        ],
        "examples": [
            {
                "ko": "이 배수로는 최소 1% 경사도를 유지해야 합니다.",
                "vi": "Rãnh thoát nước này phải giữ độ dốc tối thiểu 1%.",
                "situation": "formal"
            },
            {
                "ko": "경사로가 너무 가파른데, 1:12 맞아요?",
                "vi": "Đường dốc này quá dốc, đúng tỷ lệ 1:12 không?",
                "situation": "onsite"
            },
            {
                "ko": "지붕 경사를 30도로 해야 눈이 안 쌓여요.",
                "vi": "Mái phải dốc 30 độ thì tuyết mới không đọng.",
                "situation": "informal"
            }
        ],
        "relatedTerms": ["tỷ lệ (비율)", "góc (각도)", "mức độ (정도)", "đường dốc (경사로)"]
    },
    {
        "slug": "cuong-do",
        "korean": "강도",
        "vietnamese": "cường độ",
        "hanja": "強度",
        "hanjaReading": "強(강할 강) + 度(도 도)",
        "pronunciation": "끄엉도",
        "meaningKo": "재료가 외부 힘에 견디는 능력을 나타내는 측정값으로, 압축강도(MPa), 인장강도(MPa), 전단강도 등으로 구분됩니다. 건설 현장에서 콘크리트, 철근, 목재 등의 품질을 평가하는 핵심 지표이며, 통역 시 '강도'와 '경도(hardness)'를 혼동하지 않도록 주의해야 합니다. 콘크리트 강도는 보통 압축강도를 지칭하며, 한국에서는 '210', '240', '300' 등으로 약칭하고(단위 kg/cm²), 베트남에서는 MPa 단위를 표준 사용하므로(1 MPa ≈ 10.2 kg/cm²) 환산이 필요합니다.",
        "meaningVi": "Khả năng chịu lực của vật liệu khi bị tác động bên ngoài, bao gồm cường độ nén (MPa), cường độ kéo (MPa), cường độ cắt... Trong xây dựng, cường độ là chỉ tiêu quan trọng để đánh giá chất lượng bê tông, cốt thép, gỗ. Cần phân biệt cường độ (strength) và độ cứng (hardness). Cường độ bê tông thường chỉ cường độ nén, Việt Nam dùng đơn vị MPa (B15, B20, B25...), Hàn Quốc dùng kg/cm² (210, 240, 300) nên cần quy đổi.",
        "context": "콘크리트 품질 관리, 자재 검수, 구조 설계, 시험 결과",
        "culturalNote": "한국은 콘크리트 강도를 전통적으로 kg/cm² 단위로 표현하며(210, 240, 300 등), 일상 대화에서 '210짜리', '300짜리'라고 약칭합니다. 베트남은 SI 단위인 MPa를 표준 사용하며(B15, B20, B25 등, 여기서 숫자는 MPa), 공식 서류에도 MPa만 표기합니다. 통역 시 한국 측이 '210'이라고 하면 약 21MPa로 환산하여 전달해야 하며(정확히는 20.6MPa), 계약서에는 양국 단위를 병기하거나 MPa로 통일하는 것이 안전합니다.",
        "commonMistakes": [
            {
                "mistake": "'강도'를 độ cứng로 통역",
                "correction": "cường độ (강도, strength) vs độ cứng (경도, hardness)",
                "explanation": "강도는 하중 저항력, 경도는 긁힘/찍힘 저항력"
            },
            {
                "mistake": "'210 콘크리트'를 210 MPa로 잘못 통역",
                "correction": "210 kg/cm² ≈ 21 MPa (B20 bê tông)",
                "explanation": "한국의 kg/cm²를 MPa로 환산 필요 (÷10.2)"
            },
            {
                "mistake": "압축강도와 인장강도를 구분하지 않음",
                "correction": "cường độ nén (압축) vs cường độ kéo (인장) 명시",
                "explanation": "일반적으로 콘크리트는 압축강도, 철근은 인장강도가 중요"
            }
        ],
        "examples": [
            {
                "ko": "이 기둥은 300 콘크리트로 타설해야 합니다.",
                "vi": "Cột này phải đổ bê tông cường độ 300 kg/cm² (khoảng 30 MPa, B30).",
                "situation": "formal"
            },
            {
                "ko": "강도 시험 결과 나왔어? 210 나왔어?",
                "vi": "Kết quả thử cường độ ra chưa? Đạt 21 MPa không?",
                "situation": "informal"
            },
            {
                "ko": "이 철근 항복강도가 400MPa입니다.",
                "vi": "Cốt thép này có cường độ chảy 400 MPa.",
                "situation": "onsite"
            }
        ],
        "relatedTerms": ["áp lực (압력)", "tải trọng (하중)", "chất lượng (품질)", "độ bền (내구성)"]
    },
    {
        "slug": "tai-trong",
        "korean": "하중",
        "vietnamese": "tải trọng",
        "hanja": "荷重",
        "hanjaReading": "荷(짐 하) + 重(무거울 중)",
        "pronunciation": "따이쫑",
        "meaningKo": "구조물에 작용하는 힘이나 무게로, 고정하중(자중), 활하중(사람/물건), 풍하중(바람), 설하중(눈), 지진하중 등으로 구분됩니다. 구조 설계의 핵심 요소이며, 통역 시 하중의 종류와 크기를 정확히 전달하지 않으면 구조 안전성에 직접적인 영향을 미칠 수 있습니다. 단위는 주로 킬로뉴턴(kN) 또는 톤(ton)을 사용하며, 베트남에서는 tải trọng(하중 일반)과 trọng lượng(무게)을 구분하여 사용하므로 맥락에 맞게 통역해야 합니다.",
        "meaningVi": "Lực hoặc trọng lượng tác động lên kết cấu công trình, gồm tải trọng tĩnh (trọng lượng bản thân), tải trọng động (người, vật), tải trọng gió, tải trọng tuyết, tải trọng động đất. Là yếu tố then chốt trong thiết kế kết cấu, nếu thông dịch sai loại và độ lớn tải trọng có thể ảnh hưởng trực tiếp đến an toàn công trình. Đơn vị thường dùng kilonewton (kN) hoặc tấn (tấn). Cần phân biệt tải trọng (load) và trọng lượng (weight).",
        "context": "구조 설계, 안전성 검토, 내하력 평가, 시험",
        "culturalNote": "한국과 베트남 모두 하중 계산에 SI 단위(kN, kPa 등)를 사용하지만, 한국 현장에서는 '톤'(ton) 단위를 구어로 많이 쓰고('10톤 트럭', '20톤 크레인'), 베트남에서도 'tấn'을 일상적으로 씁니다. 다만 공식 설계 도서에는 kN(킬로뉴턴) 단위를 쓰므로, 통역 시 맥락에 따라 톤과 kN을 적절히 환산해야 합니다(1톤 ≈ 9.8kN). 지진 하중은 한국이 베트남보다 지진 설계 기준이 엄격하므로, 한국 설계자가 지진 하중을 강조하면 베트남 현장에 그 중요성을 충분히 설명해야 합니다.",
        "commonMistakes": [
            {
                "mistake": "'하중'을 trọng lượng로만 통역",
                "correction": "tải trọng (구조물에 작용하는 힘) vs trọng lượng (물체의 무게)",
                "explanation": "tải trọng은 설계 개념, trọng lượng은 물리적 무게"
            },
            {
                "mistake": "'10톤 하중'을 10 tấn tải trọng로만 말함",
                "correction": "10 tấn (khoảng 98 kN) 환산 값도 함께 전달",
                "explanation": "공식 설계 도서는 kN 단위 사용하므로 환산 필요"
            },
            {
                "mistake": "활하중과 고정하중을 구분하지 않음",
                "correction": "tải trọng tĩnh (고정하중) vs tải trọng động (활하중) 명시",
                "explanation": "설계 시 두 하중의 조합이 중요하므로 반드시 구분"
            }
        ],
        "examples": [
            {
                "ko": "이 슬라브는 활하중 5kN/m²까지 견딜 수 있습니다.",
                "vi": "Sàn này chịu được tải trọng động tới 5 kN/m².",
                "situation": "formal"
            },
            {
                "ko": "크레인 하중 계산 좀 다시 해봐, 이거 위험해 보여.",
                "vi": "Tính lại tải trọng cần trục xem, có vẻ nguy hiểm đấy.",
                "situation": "onsite"
            },
            {
                "ko": "지붕에 눈 쌓이면 설하중이 얼마나 되죠?",
                "vi": "Nếu tuyết phủ trên mái thì tải trọng tuyết là bao nhiêu?",
                "situation": "informal"
            }
        ],
        "relatedTerms": ["cường độ (강도)", "áp lực (압력)", "trọng lượng (무게)", "kết cấu (구조)"]
    },
    {
        "slug": "ap-luc",
        "korean": "압력",
        "vietnamese": "áp lực",
        "hanja": "壓力",
        "hanjaReading": "壓(누를 압) + 力(힘 력)",
        "pronunciation": "압륵",
        "meaningKo": "단위 면적당 작용하는 힘으로, 파스칼(Pa) 또는 메가파스칼(MPa)로 표시됩니다. 건설 현장에서는 토압(흙의 압력), 수압(물의 압력), 콘크리트 타설 시 거푸집 압력, 유압 장비의 작동 압력 등에 사용되며, 통역 시 압력의 종류와 측정 단위를 명확히 구분해야 합니다. 압력과 하중(힘)을 혼동하지 않도록 주의하며(압력 = 힘/면적), 베트남에서는 áp lực과 áp suất을 거의 같은 의미로 사용하지만, áp suất이 좀 더 기술적 용어입니다.",
        "meaningVi": "Lực tác dụng trên một đơn vị diện tích, đo bằng pascal (Pa) hoặc megapascal (MPa). Trong xây dựng dùng cho áp lực đất (土壓), áp lực nước (水壓), áp lực ván khuôn khi đổ bê tông, áp lực hoạt động của thiết bị thủy lực. Cần phân biệt áp lực (pressure = lực/diện tích) và tải trọng (load = lực). Trong tiếng Việt, áp lực và áp suất đồng nghĩa, nhưng áp suất mang tính kỹ thuật hơn.",
        "context": "토목 설계, 수압 계산, 유압 장비, 안전 관리",
        "culturalNote": "한국과 베트남 모두 압력 단위로 Pa, kPa, MPa를 표준 사용하지만, 한국에서는 구어로 'kg/cm²', 'bar' 등 비SI 단위를 현장에서 여전히 쓰는 경우가 많고('타이어 압력 2.5bar'), 베트남에서도 'bar'는 일상적으로 씁니다. 공식 도서에는 SI 단위(Pa)를 쓰므로 통역 시 환산이 필요할 수 있습니다(1 bar = 100 kPa). 토압은 옹벽, 지하실 설계에 중요하며, 수압은 지하 구조물, 댐, 상하수도 설계에 필수적이므로 맥락에 맞게 정확히 통역해야 합니다.",
        "commonMistakes": [
            {
                "mistake": "'압력'을 tải trọng로 통역",
                "correction": "áp lực/áp suất (단위면적당 힘) vs tải trọng (힘 자체)",
                "explanation": "압력 = 힘/면적, 하중 = 힘"
            },
            {
                "mistake": "'2.5bar'를 '2.5 MPa'로 환산 없이 통역",
                "correction": "2.5 bar = 0.25 MPa = 250 kPa",
                "explanation": "bar와 Pa 단위 환산 필요 (1 bar = 0.1 MPa)"
            },
            {
                "mistake": "토압(土壓)을 trọng lượng đất로 통역",
                "correction": "áp lực đất (토압) vs trọng lượng đất (흙의 무게)",
                "explanation": "토압은 흙이 옹벽에 가하는 압력, 흙의 무게와는 다름"
            }
        ],
        "examples": [
            {
                "ko": "이 지하실 벽체는 토압 50kPa를 견뎌야 합니다.",
                "vi": "Tường tầng hầm này phải chịu áp lực đất 50 kPa.",
                "situation": "formal"
            },
            {
                "ko": "유압 펌프 압력 체크했어? 정상이야?",
                "vi": "Kiểm tra áp lực bơm thủy lực chưa? Bình thường không?",
                "situation": "onsite"
            },
            {
                "ko": "수압 테스트에서 누수 발견됐어요.",
                "vi": "Phát hiện rò rỉ khi thử áp lực nước.",
                "situation": "informal"
            }
        ],
        "relatedTerms": ["tải trọng (하중)", "cường độ (강도)", "lực (힘)", "áp suất (압력, 동의어)"]
    },
    {
        "slug": "do-lun",
        "korean": "침하",
        "vietnamese": "độ lún",
        "hanja": "沈下",
        "hanjaReading": "沈(잠길 침) + 下(아래 하)",
        "pronunciation": "도룬",
        "meaningKo": "구조물이나 지반이 자중이나 외부 하중에 의해 아래로 가라앉는 현상으로, 밀리미터(mm) 또는 센티미터(cm) 단위로 측정됩니다. 건설 현장에서 기초 설계, 지반 조사, 시공 중 모니터링, 준공 후 유지관리에서 중요한 지표이며, 통역 시 '침하'와 '침강(sedimentation)'을 혼동하지 않도록 주의해야 합니다. 허용 침하량을 초과하면 균열, 기울음, 구조 손상으로 이어지므로, 침하 측정 결과를 정확히 전달하는 것이 안전에 직결됩니다.",
        "meaningVi": "Hiện tượng công trình hoặc nền đất chìm xuống do trọng lượng bản thân hoặc tải trọng bên ngoài, đo bằng milimét (mm) hoặc centimét (cm). Trong xây dựng, độ lún là chỉ tiêu quan trọng khi thiết kế móng, khảo sát địa chất, giám sát thi công, bảo trì sau hoàn công. Cần phân biệt độ lún (settlement, chìm của công trình) và lắng đọng (sedimentation, cặn lắng). Nếu độ lún vượt giới hạn cho phép sẽ gây nứt, nghiêng, hư hỏng kết cấu, nên phải thông dịch kết quả đo chính xác.",
        "context": "기초 설계, 지반 조사, 침하 모니터링, 안전 관리",
        "culturalNote": "한국과 베트남 모두 연약 지반이 많아 침하 문제가 빈번하며, 침하 측정은 공통적으로 중요한 관리 항목입니다. 한국은 연약 지반 개량 기술(SCP, PBD 등)이 발달했고, 베트남은 메콩 델타 등 지반이 약한 지역이 많아 침하 관리 경험이 축적되어 있습니다. 통역 시 한국 기술자가 '부등침하(differential settlement)'를 언급하면 베트남어로 độ lún lệch 또는 độ lún không đều라고 하며, 이는 구조물의 한쪽만 더 많이 침하하는 현상으로 매우 위험하므로 강조하여 전달해야 합니다.",
        "commonMistakes": [
            {
                "mistake": "'침하'를 chìm xuống로만 통역",
                "correction": "độ lún (전문 용어) vs chìm xuống (일반 표현)",
                "explanation": "độ lún은 건설 기술 용어, chìm xuống는 '가라앉다'는 일반 동사"
            },
            {
                "mistake": "'부등침하'를 độ lún khác nhau로 통역",
                "correction": "độ lún lệch 또는 độ lún không đều (불균등 침하)",
                "explanation": "부등침하는 구조물 각 부분의 침하량이 달라 위험한 상황"
            },
            {
                "mistake": "침하량 '5mm'를 '5cm'로 잘못 전달",
                "correction": "단위 확인 후 정확히 전달 (mm vs cm 차이는 10배)",
                "explanation": "침하량은 mm 단위가 많으므로 단위 혼동은 치명적"
            }
        ],
        "examples": [
            {
                "ko": "이 건물 기초의 허용 침하량은 25mm입니다.",
                "vi": "Độ lún cho phép của móng nhà này là 25 mm.",
                "situation": "formal"
            },
            {
                "ko": "침하 계측기 설치 위치 확인 좀 해줘.",
                "vi": "Kiểm tra vị trí đặt thiết bị đo độ lún giúp tớ.",
                "situation": "onsite"
            },
            {
                "ko": "저쪽 기둥이 더 많이 침하했는데, 위험한 거 아니에요?",
                "vi": "Cột bên kia lún nhiều hơn, có nguy hiểm không?",
                "situation": "informal"
            }
        ],
        "relatedTerms": ["nền móng (기초)", "địa chất (지질)", "tải trọng (하중)", "độ lún lệch (부등침하)"]
    }
]

# 중복 제거
new_terms_filtered = [t for t in new_terms if t['slug'] not in existing_slugs]

if not new_terms_filtered:
    print("⚠️  모든 용어가 이미 존재합니다. 추가할 항목이 없습니다.")
else:
    # 데이터 추가
    data.extend(new_terms_filtered)

    # 파일 저장
    with open(file_path, 'w', encoding='utf-8') as f:
        json.dump(data, f, ensure_ascii=False, indent=2)

    print(f"✅ {len(new_terms_filtered)}개 건설 수학/단위/측정 용어 추가 완료!")
    print(f"📂 파일: {file_path}")
    print(f"📊 총 용어 수: {len(data)}개")

    # 추가된 용어 목록
    print("\n추가된 용어:")
    for term in new_terms_filtered:
        print(f"  - {term['slug']}: {term['korean']} - {term['vietnamese']}")
