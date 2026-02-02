#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
건설(Construction) 도메인 용어 추가 스크립트 v1-g
테마: 측량/품질관리 (Survey & Quality Control)
"""

import json
import os

# 프로젝트 루트 기준 경로
file_path = os.path.join(
    os.path.dirname(__file__),
    "..", "data", "terms", "construction.json"
)

# 신규 용어 10개 (측량/품질관리)
new_terms = [
    {
        "slug": "kinh-vi",
        "korean": "트랜싯",
        "vietnamese": "Kinh vĩ",
        "hanja": None,
        "hanjaReading": None,
        "pronunciation": "트랜시트",
        "meaningKo": "각도를 정밀하게 측정하는 측량 기기로, 수평각과 연직각을 동시에 측정할 수 있습니다. 현대에는 토탈 스테이션으로 대체되고 있지만 기본 측량 원리를 설명할 때 여전히 중요합니다. 통역 시 베트남 현장에서는 'máy kinh vĩ'로 부르며, 일본식 측량 용어가 많이 남아있어 'teodolít'(테오도라이트)라는 러시아식 용어도 혼용됩니다. 측량 장비 교육이나 매뉴얼 통역 시 양국의 측량 기술 세대 차이를 고려해 설명해야 합니다.",
        "meaningVi": "Thiết bị đo đạc dùng để đo góc ngang và góc đứng với độ chính xác cao. Trong tiếng Việt, thiết bị này còn được gọi là 'teodolít' (theo từ tiếng Nga), và hiện nay đang dần được thay thế bằng máy toàn đạc điện tử (Total Station). Kinh vĩ là công cụ cơ bản trong trắc địa xây dựng.",
        "context": "측량 작업, 건설 현장 측량, 측량 교육",
        "culturalNote": "한국에서는 1990년대 이후 토탈 스테이션으로 급속히 전환되었지만, 베트남 일부 중소 현장에서는 여전히 광학식 트랜싯을 사용하는 경우가 있습니다. 한국 측량기사 자격증 시험에서는 이론으로만 다루지만, 베트남에서는 실무 장비로 남아있는 경우가 많아 기술 이전 프로젝트에서 세대 차이를 고려한 통역이 필요합니다.",
        "commonMistakes": [
            {
                "mistake": "teodolít를 '테오도라이트'로만 번역",
                "correction": "'kinh vĩ' 또는 'máy kinh vĩ'로 번역",
                "explanation": "베트남에서 teodolít는 러시아식 측량 용어로, 공식 베트남어는 'kinh vĩ'입니다."
            },
            {
                "mistake": "Total Station과 구분 없이 '측량기'로 통칭",
                "correction": "트랜싯(kinh vĩ)과 토탈스테이션(máy toàn đạc) 명확히 구분",
                "explanation": "두 장비는 기능과 세대가 다르므로 명확한 구분이 필요합니다."
            },
            {
                "mistake": "'transit'를 그대로 '트랜짓'으로 음차",
                "correction": "'kinh vĩ' 사용",
                "explanation": "베트남어에는 정식 명칭이 있으므로 음차보다 현지 용어 사용이 적절합니다."
            }
        ],
        "examples": [
            {
                "ko": "트랜싯을 이용해 기준점으로부터 수평각을 측정하세요.",
                "vi": "Hãy dùng kinh vĩ để đo góc ngang từ điểm chuẩn.",
                "situation": "onsite"
            },
            {
                "ko": "구형 트랜싯 장비는 정기 검교정이 필수입니다.",
                "vi": "Thiết bị kinh vĩ cũ cần được kiểm định và hiệu chuẩn định kỳ.",
                "situation": "formal"
            },
            {
                "ko": "요즘은 트랜싯보다 토탈스테이션 쓰죠.",
                "vi": "Hiện nay người ta dùng máy toàn đạc nhiều hơn kinh vĩ.",
                "situation": "informal"
            }
        ],
        "relatedTerms": ["토탈스테이션", "수준측량", "레벨", "GPS측량"],
        "difficulty": "intermediate",
        "importance": "high",
        "frequency": "medium"
    },
    {
        "slug": "do-thuy-chuan",
        "korean": "수준측량",
        "vietnamese": "Đo thủy chuẩn",
        "hanja": "水準測量",
        "hanjaReading": "水(물 수) + 準(준할 준) + 測(잴 측) + 量(헤아릴 량)",
        "pronunciation": "수준측량",
        "meaningKo": "기준점으로부터 각 지점의 높이를 측정하는 측량 작업입니다. 수준기(레벨)와 표척을 사용해 고저차를 정밀하게 측정하며, 건설 현장에서 기초 레벨 설정, 배수 구배 확인, 층고 관리 등에 필수적입니다. 통역 시 주의할 점은 베트nam에서는 'đo cao'(높이 측정)라는 일반 용어와 'đo thủy chuẩn'(정밀 수준측량)을 구분해서 사용한다는 것입니다. 고급 측량 용역 계약서에서는 정확도 등급(I급, II급 등)을 명시하므로 양국 측량 기준의 차이를 이해해야 합니다.",
        "meaningVi": "Công tác đo đạc nhằm xác định chênh lệch độ cao giữa các điểm so với mốc chuẩn. Sử dụng máy thủy chuẩn (mức) và thước đo để đo chênh cao với độ chính xác cao. Đây là công việc cơ bản trong xây dựng để kiểm soát độ cao móng, độ dốc thoát nước, và cao trình các tầng.",
        "context": "측량 작업, 기초 공사, 토목 공사, 품질 검사",
        "culturalNote": "한국의 국가기준점은 인천 평균해수면 기준이고, 베트남은 Hòn Dấu(혼저우) 해수면 기준입니다. 국제 프로젝트에서 측량 기준점 조율 시 이 차이를 명확히 해야 하며, 베트남은 프랑스 측량 체계의 영향을 받아 용어와 표기법에 차이가 있습니다.",
        "commonMistakes": [
            {
                "mistake": "'leveling'을 '레벨링'으로 음차",
                "correction": "'đo thủy chuẩn' 사용",
                "explanation": "베트남어 정식 측량 용어를 사용해야 전문성이 유지됩니다."
            },
            {
                "mistake": "'đo cao'로만 번역",
                "correction": "정밀 측량은 'đo thủy chuẩn', 일반 높이 측정은 'đo cao'",
                "explanation": "측량의 정밀도와 목적에 따라 용어를 구분해야 합니다."
            },
            {
                "mistake": "측량 기준점 차이를 고려하지 않고 수치만 통역",
                "correction": "양국 기준점 차이 명시 후 통역",
                "explanation": "국제 프로젝트에서는 기준점 체계 차이가 오차로 이어질 수 있습니다."
            }
        ],
        "examples": [
            {
                "ko": "터파기 전에 수준측량을 실시하여 기준 레벨을 확인하겠습니다.",
                "vi": "Trước khi đào đất, chúng tôi sẽ tiến hành đo thủy chuẩn để xác định cao trình chuẩn.",
                "situation": "formal"
            },
            {
                "ko": "레벨 가져와서 이 구간 수준측량 다시 해봐.",
                "vi": "Lấy máy thủy chuẩn lại đây, đo lại đoạn này.",
                "situation": "onsite"
            },
            {
                "ko": "수준측량 정확도가 ±3mm 이내여야 합니다.",
                "vi": "Độ chính xác đo thủy chuẩn phải trong phạm vi ±3mm.",
                "situation": "formal"
            }
        ],
        "relatedTerms": ["레벨", "트랜싯", "기준점", "토탈스테이션"],
        "difficulty": "intermediate",
        "importance": "high",
        "frequency": "high"
    },
    {
        "slug": "may-thuy-chuan",
        "korean": "레벨",
        "vietnamese": "Máy thủy chuẩn",
        "hanja": None,
        "hanjaReading": None,
        "pronunciation": "레벨",
        "meaningKo": "수준측량에 사용하는 측량 기기로, 수평선을 기준으로 표척의 눈금을 읽어 고저차를 측정합니다. 자동 레벨, 틸팅 레벨, 디지털 레벨 등 종류가 다양하며, 현장에서는 줄여서 '레벨'이라고 부릅니다. 통역 시 주의할 점은 'level'이라는 단어가 '수평'이라는 의미와 '측량기'라는 의미로 이중으로 사용되므로 문맥에 따라 정확히 구분해야 한다는 것입니다. 베트남 현장에서는 'máy mức', 'máy thủy bình' 등으로도 불리므로 현지 관행을 파악하는 것이 중요합니다.",
        "meaningVi": "Thiết bị đo đạc dùng trong đo thủy chuẩn, hoạt động dựa trên nguyên lý đường ngắm ngang để đọc số liệu trên thước đo và xác định chênh cao. Có nhiều loại như máy thủy chuẩn tự động, máy nghiêng, và máy số. Trong công trường thường gọi tắt là 'mức' hoặc 'máy thủy bình'.",
        "context": "측량 작업, 건설 현장, 토목 공사",
        "culturalNote": "한국 현장에서는 '레벨'이라는 외래어가 완전히 정착되어 '수준기'라는 순우리말보다 더 많이 쓰입니다. 베트남에서는 'máy thủy chuẩn'이 공식 용어이지만 현장에서는 'máy mức'(레벨기)로 줄여 부르는 경우가 많습니다. 장비 대여나 구매 계약 시 정확한 장비 사양(자동/디지털)을 명시해야 합니다.",
        "commonMistakes": [
            {
                "mistake": "'level'을 항상 'mức'로만 번역",
                "correction": "측량 기기는 'máy thủy chuẩn', 수평 상태는 'mức ngang' 또는 'thăng bằng'",
                "explanation": "단어의 의미와 문맥에 따라 번역어가 달라집니다."
            },
            {
                "mistake": "'레벨기'를 'máy cấp độ'로 번역",
                "correction": "'máy thủy chuẩn' 또는 'máy mức' 사용",
                "explanation": "'cấp độ'는 '등급'을 의미하므로 측량 기기 명칭으로 부적절합니다."
            },
            {
                "mistake": "자동레벨과 디지털레벨 구분 없이 통역",
                "correction": "자동레벨(máy tự động), 디지털레벨(máy số) 명확히 구분",
                "explanation": "장비 사양이 측량 정확도와 작업 효율에 직접 영향을 줍니다."
            }
        ],
        "examples": [
            {
                "ko": "레벨과 표척을 준비해서 기초 레벨을 잡으세요.",
                "vi": "Chuẩn bị máy thủy chuẩn và thước đo để xác định cao trình móng.",
                "situation": "onsite"
            },
            {
                "ko": "이번 현장에는 디지털 레벨을 투입합니다.",
                "vi": "Công trường này chúng tôi sẽ sử dụng máy thủy chuẩn số.",
                "situation": "formal"
            },
            {
                "ko": "레벨 좀 맞춰봐, 기포가 안 맞네.",
                "vi": "Điều chỉnh máy mức đi, bọt khí chưa thẳng.",
                "situation": "informal"
            }
        ],
        "relatedTerms": ["수준측량", "표척", "트랜싯", "토탈스테이션"],
        "difficulty": "beginner",
        "importance": "high",
        "frequency": "high"
    },
    {
        "slug": "do-gps",
        "korean": "GPS측량",
        "vietnamese": "Đo GPS",
        "hanja": None,
        "hanjaReading": None,
        "pronunciation": "지피에스측량",
        "meaningKo": "위성항법시스템(GPS)을 이용한 측량 방식으로, 인공위성 신호를 수신하여 정확한 위치 좌표를 측정합니다. RTK-GPS, DGPS 등 다양한 방식이 있으며, 넓은 지역의 기준점 측량이나 지적 측량에 많이 사용됩니다. 통역 시 주의할 점은 베트남에서 GPS라는 용어가 미국 시스템만을 가리키는 경우가 많아, 러시아의 GLONASS, 유럽의 Galileo를 포함한 GNSS(위성항법시스템) 개념과 구분해서 설명해야 한다는 것입니다. 또한 베트남은 좌표계가 VN2000을 사용하므로 한국의 세계측지계(GRS80)와 변환 과정이 필요합니다.",
        "meaningVi": "Phương pháp đo đạc sử dụng hệ thống định vị toàn cầu (GPS) để xác định tọa độ chính xác thông qua tín hiệu vệ tinh. Có nhiều phương pháp như RTK-GPS, DGPS, được ứng dụng rộng rãi trong đo đạc điểm khống chế trên diện rộng và đo địa chính. Hiện nay khái niệm GNSS (bao gồm GPS, GLONASS, Galileo) đang được sử dụng phổ biến hơn.",
        "context": "측량 작업, 지적 측량, 대규모 현장",
        "culturalNote": "한국에서는 국토지리정보원의 VRS(가상기준점) 서비스가 잘 구축되어 있어 RTK-GPS 측량이 보편화되었지만, 베트남은 지역에 따라 기준점 인프라 수준이 다릅니다. 국제 프로젝트에서 GPS 측량 시 양국의 좌표계 차이(한국: GRS80/UTM-K, 베트남: VN2000)를 반드시 조율해야 하며, 측량 성과물의 좌표 변환 절차를 계약서에 명시하는 것이 중요합니다.",
        "commonMistakes": [
            {
                "mistake": "GPS와 GNSS를 구분하지 않고 사용",
                "correction": "GPS는 미국 시스템, GNSS는 전체 위성항법시스템",
                "explanation": "기술적 정확성과 국제 표준 준수를 위해 구분이 필요합니다."
            },
            {
                "mistake": "'đo vệ tinh'(위성 측량)로만 번역",
                "correction": "'đo GPS' 또는 'đo GNSS' 사용",
                "explanation": "베트남 측량 실무에서 GPS/GNSS가 표준 용어입니다."
            },
            {
                "mistake": "좌표계 차이를 고려하지 않고 GPS 좌표 그대로 전달",
                "correction": "VN2000과 GRS80 좌표계 변환 필요성 명시",
                "explanation": "좌표계 차이를 무시하면 수십 미터의 오차가 발생할 수 있습니다."
            }
        ],
        "examples": [
            {
                "ko": "이번 부지 측량은 RTK-GPS로 진행하겠습니다.",
                "vi": "Công tác đo đạc khu đất này chúng tôi sẽ thực hiện bằng RTK-GPS.",
                "situation": "formal"
            },
            {
                "ko": "GPS 좌표를 VN2000 좌표계로 변환해야 합니다.",
                "vi": "Cần chuyển đổi tọa độ GPS sang hệ tọa độ VN2000.",
                "situation": "formal"
            },
            {
                "ko": "GPS 안테나 세워놓고 30분 이상 측정하세요.",
                "vi": "Dựng ăng-ten GPS lên và đo ít nhất 30 phút.",
                "situation": "onsite"
            }
        ],
        "relatedTerms": ["RTK", "GNSS", "기준점", "좌표계"],
        "difficulty": "advanced",
        "importance": "high",
        "frequency": "medium"
    },
    {
        "slug": "bua-schmidt",
        "korean": "슈미트해머",
        "vietnamese": "Búa Schmidt",
        "hanja": None,
        "hanjaReading": None,
        "pronunciation": "슈미트해머",
        "meaningKo": "콘크리트 표면 강도를 비파괴적으로 측정하는 반발 경도 시험기입니다. 스프링으로 가압된 해머를 콘크리트 표면에 타격하고 반발 높이를 측정하여 압축강도를 추정합니다. 현장에서 신속하게 콘크리트 품질을 확인할 수 있어 구조물 안전진단, 품질 검사에 널리 사용됩니다. 통역 시 주의할 점은 베트남에서는 '반발경도시험'을 'thí nghiệm độ cứng nẩy'라고 하며, 슈미트해머는 스위스 제조사 이름에서 유래했으므로 'búa Schmidt' 또는 'búa đo cường độ bê tông'으로 번역한다는 것입니다. 시험 결과는 KS 기준과 베트남 TCVN 기준이 다를 수 있어 환산표를 참조해야 합니다.",
        "meaningVi": "Thiết bị thử nghiệm không phá hủy dùng để đo cường độ bề mặt bê tông thông qua phương pháp đo độ nẩy. Búa được ép bằng lò xo đập vào bề mặt bê tông, sau đó đo độ cao nẩy lại để ước tính cường độ chịu nén. Đây là phương pháp nhanh chóng để kiểm tra chất lượng bê tông tại công trường, được sử dụng rộng rãi trong giám định an toàn công trình và kiểm tra chất lượng.",
        "context": "콘크리트 품질 검사, 구조물 진단, 현장 시험",
        "culturalNote": "한국에서는 콘크리트 품질 관리가 매우 엄격하여 슈미트해머 시험이 정기적으로 이루어지지만, 베트남 중소 현장에서는 장비 보유율이 낮아 외부 시험 용역에 의존하는 경우가 많습니다. 국제 프로젝트에서는 시험 주기와 허용 기준을 계약서에 명시해야 하며, 한국 기준(KS F 2730)과 베트남 기준(TCVN 9357)의 차이를 조율해야 합니다.",
        "commonMistakes": [
            {
                "mistake": "'hammer test'를 '해머 테스트'로 음차",
                "correction": "'thí nghiệm búa Schmidt' 또는 'thí nghiệm độ cứng nẩy' 사용",
                "explanation": "베트남어 정식 시험 명칭을 사용해야 합니다."
            },
            {
                "mistake": "반발경도와 압축강도를 같은 것으로 설명",
                "correction": "반발경도는 압축강도 '추정'값임을 명시",
                "explanation": "슈미트해머는 간접 시험법이므로 정확도에 한계가 있습니다."
            },
            {
                "mistake": "시험 기준 차이를 고려하지 않고 수치만 통역",
                "correction": "KS 기준인지 TCVN 기준인지 명시",
                "explanation": "기준이 다르면 같은 수치도 다른 의미를 가질 수 있습니다."
            }
        ],
        "examples": [
            {
                "ko": "슈미트해머로 이 기둥의 콘크리트 강도를 측정하겠습니다.",
                "vi": "Chúng tôi sẽ dùng búa Schmidt để đo cường độ bê tông của cột này.",
                "situation": "formal"
            },
            {
                "ko": "슈미트해머 값이 기준 미달이면 코어 채취해야 해요.",
                "vi": "Nếu giá trị búa Schmidt dưới tiêu chuẩn thì phải khoan lấy mẫu lõi.",
                "situation": "onsite"
            },
            {
                "ko": "반발경도 평균값이 28입니다.",
                "vi": "Giá trị trung bình độ cứng nẩy là 28.",
                "situation": "formal"
            }
        ],
        "relatedTerms": ["코어채취", "비파괴검사", "압축강도", "품질시험"],
        "difficulty": "intermediate",
        "importance": "high",
        "frequency": "high"
    },
    {
        "slug": "khoan-lay-loi",
        "korean": "코어채취",
        "vietnamese": "Khoan lấy lõi",
        "hanja": None,
        "hanjaReading": None,
        "pronunciation": "코어채취",
        "meaningKo": "경화된 콘크리트 구조물에서 원통형 공시체(코어)를 채취하여 압축강도 등을 시험하는 방법입니다. 다이아몬드 비트가 장착된 코어 드릴로 직경 100mm 전후의 원기둥 시료를 채취하며, 슈미트해머 등 비파괴 시험 결과가 의심스러울 때나 구조물 안전진단 시 실시합니다. 통역 시 주의할 점은 '코어(core)'라는 용어가 '철근 코어', '구조 코어' 등 다양한 의미로 쓰이므로 'core sampling'은 반드시 'khoan lấy lõi bê tông'으로 명확히 해야 한다는 것입니다. 채취 위치와 개수는 구조 안전에 영향을 주므로 구조기술사의 승인을 받아야 합니다.",
        "meaningVi": "Phương pháp lấy mẫu hình trụ (lõi) từ kết cấu bê tông đã đông cứng để thử nghiệm cường độ chịu nén. Sử dụng mũi khoan kim cương để khoan lấy mẫu hình trụ đường kính khoảng 100mm. Phương pháp này được áp dụng khi kết quả thử nghiệm không phá hủy (như búa Schmidt) đáng ngờ hoặc khi giám định an toàn công trình. Vị trí và số lượng lấy mẫu phải được kỹ sư kết cấu phê duyệt.",
        "context": "콘크리트 품질 검사, 구조물 진단, 안전진단",
        "culturalNote": "한국에서는 코어 채취 후 구멍을 무수축 모르타르로 충전하는 것이 표준이지만, 베트남 일부 현장에서는 보수 절차가 생략되는 경우가 있어 품질 기준을 명확히 해야 합니다. 또한 한국은 코어 채취를 '파괴 시험'으로 분류하지만 베트남에서는 '반파괴 시험'으로 보는 경향이 있어 계약서 작성 시 시험 범위를 명확히 정의해야 합니다.",
        "commonMistakes": [
            {
                "mistake": "'core sampling'을 '코어 샘플링'으로 음차",
                "correction": "'khoan lấy lõi bê tông' 사용",
                "explanation": "베트남어 정식 시험 명칭을 사용해야 전문성이 유지됩니다."
            },
            {
                "mistake": "'lõi'만으로 번역하여 철근 코어와 혼동",
                "correction": "'lõi bê tông'으로 명확히 표기",
                "explanation": "건설 현장에서 '코어'는 다양한 의미로 쓰이므로 구체적 표현이 필요합니다."
            },
            {
                "mistake": "채취 후 보수 절차를 언급하지 않음",
                "correction": "코어 구멍 충전(lấp đầy lỗ khoan) 절차 포함",
                "explanation": "보수 절차는 구조 안전과 직결되므로 반드시 명시해야 합니다."
            }
        ],
        "examples": [
            {
                "ko": "슈미트해머 결과가 미달이므로 3개소에서 코어를 채취하겠습니다.",
                "vi": "Do kết quả búa Schmidt không đạt, chúng tôi sẽ khoan lấy lõi tại 3 vị trí.",
                "situation": "formal"
            },
            {
                "ko": "코어 채취 후에는 무수축 모르타르로 즉시 보수해야 합니다.",
                "vi": "Sau khi khoan lấy lõi phải lấp đầy ngay bằng vữa không co ngót.",
                "situation": "formal"
            },
            {
                "ko": "코어 뽑아서 시험실로 보내.",
                "vi": "Khoan lấy lõi xong gửi lên phòng thí nghiệm.",
                "situation": "informal"
            }
        ],
        "relatedTerms": ["슈미트해머", "압축강도시험", "비파괴검사", "품질시험"],
        "difficulty": "intermediate",
        "importance": "high",
        "frequency": "medium"
    },
    {
        "slug": "kiem-tra-khong-pha-huy",
        "korean": "비파괴검사",
        "vietnamese": "Kiểm tra không phá hủy",
        "hanja": "非破壞檢査",
        "hanjaReading": "非(아닐 비) + 破(깨뜨릴 파) + 壞(무너질 괴) + 檢(검사할 검) + 査(조사할 사)",
        "pronunciation": "비파괴검사",
        "meaningKo": "재료나 구조물을 파괴하지 않고 결함이나 품질을 검사하는 방법의 총칭입니다. 초음파탐상, 방사선투과, 자분탐상, 침투탐상 등 다양한 방법이 있으며, 건설 분야에서는 콘크리트 강도 추정(슈미트해머, 초음파), 철근 배근 확인(전자기파), 용접부 검사(초음파, 방사선) 등에 활용됩니다. 통역 시 주의할 점은 베트남어 'kiểm tra không phá hủy'는 직역이지만, 실무에서는 영어 약자 NDT(Non-Destructive Testing)를 그대로 쓰는 경우가 많다는 것입니다. 각 검사 방법의 원리와 적용 범위가 다르므로 구체적인 검사법을 명시해야 합니다.",
        "meaningVi": "Tổng hợp các phương pháp kiểm tra khuyết tật hoặc chất lượng vật liệu, kết cấu mà không làm hư hại đối tượng kiểm tra. Bao gồm nhiều phương pháp như siêu âm, tia X, từ tính, thấm màu, v.v. Trong xây dựng, được ứng dụng để đánh giá cường độ bê tông (búa Schmidt, siêu âm), kiểm tra cốt thép (sóng điện từ), kiểm tra mối hàn (siêu âm, tia X). Trong thực tế, thuật ngữ tiếng Anh NDT cũng được sử dụng phổ biến.",
        "context": "품질 검사, 안전진단, 용접 검사, 구조물 진단",
        "culturalNote": "한국에서는 비파괴검사 전문 자격증(비파괴검사기사) 제도가 잘 확립되어 있고, 주요 현장에는 NDT 전문 업체가 상주하는 경우가 많습니다. 베트남은 자격 제도가 한국만큼 엄격하지 않아 검사 품질 편차가 크므로, 국제 프로젝트에서는 검사 업체의 자격(ASNT, EN ISO 9712 등) 기준을 계약서에 명시하는 것이 중요합니다.",
        "commonMistakes": [
            {
                "mistake": "모든 비파괴검사를 'NDT'로만 표기",
                "correction": "공식 문서는 'kiểm tra không phá hủy', 구두는 'NDT' 병용",
                "explanation": "문서와 구두 상황에 따라 용어를 선택하는 것이 적절합니다."
            },
            {
                "mistake": "검사 방법을 구체적으로 명시하지 않음",
                "correction": "초음파(siêu âm), 방사선(tia X) 등 구체적 방법 명시",
                "explanation": "각 검사법의 목적과 적용 범위가 다르므로 구분이 필요합니다."
            },
            {
                "mistake": "'비파괴'를 'không hủy'로 번역",
                "correction": "'không phá hủy' 사용",
                "explanation": "'phá hủy'가 '파괴'의 정확한 베트남어 표현입니다."
            }
        ],
        "examples": [
            {
                "ko": "용접부는 초음파 비파괴검사로 품질을 확인합니다.",
                "vi": "Chất lượng mối hàn sẽ được kiểm tra bằng phương pháp siêu âm không phá hủy.",
                "situation": "formal"
            },
            {
                "ko": "NDT 업체한테 연락해서 내일 검사 일정 잡아.",
                "vi": "Liên hệ công ty NDT đặt lịch kiểm tra ngày mai.",
                "situation": "informal"
            },
            {
                "ko": "이 구조물은 비파괴검사 대상입니다.",
                "vi": "Kết cấu này thuộc đối tượng kiểm tra không phá hủy.",
                "situation": "formal"
            }
        ],
        "relatedTerms": ["초음파탐상", "슈미트해머", "방사선투과검사", "품질검사"],
        "difficulty": "advanced",
        "importance": "high",
        "frequency": "medium"
    },
    {
        "slug": "o-tai",
        "korean": "로드셀",
        "vietnamese": "Ô tải",
        "hanja": None,
        "hanjaReading": None,
        "pronunciation": "로드셀",
        "meaningKo": "하중(荷重, load)을 전기 신호로 변환하여 측정하는 센서입니다. 건설 현장에서는 PC강선 긴장 시 긴장력 측정, 크레인 과부하 방지, 구조물 하중 모니터링 등에 사용됩니다. 통역 시 주의할 점은 '로드셀(load cell)'이 베트남어로 'ô tải'(하중 셀) 또는 'cảm biến lực'(힘 센서)로 번역되며, 프리스트레스 콘크리트(PSC) 공사에서는 긴장력 측정 장비로 매우 중요하다는 것입니다. 한국은 로드셀 검교정이 엄격하지만 베트남은 상대적으로 느슨하므로, 국제 프로젝트에서는 검교정 주기와 허용 오차 범위를 계약서에 명시해야 합니다.",
        "meaningVi": "Cảm biến chuyển đổi tải trọng (lực) thành tín hiệu điện để đo lường. Trong công trường xây dựng, được sử dụng để đo lực căng thép PC, phòng ngừa quá tải cần trục, giám sát tải trọng kết cấu. Trong tiếng Việt còn gọi là 'cảm biến lực'. Đây là thiết bị rất quan trọng trong thi công bê tông ứng lực trước (PSC) để đo lực căng.",
        "context": "PSC 공사, 계측 관리, 안전 관리",
        "culturalNote": "한국에서는 PSC 공사 시 로드셀과 압력계를 동시에 사용하여 이중 확인하는 것이 표준이지만, 베트남 일부 현장에서는 압력계만 사용하는 경우가 있어 품질 기준 조율이 필요합니다. 또한 로드셀의 정기 검교정은 한국에서는 법적 의무사항이지만 베트남은 권고사항으로 되어 있어, 국제 프로젝트에서는 한국 수준의 검교정 기준을 계약서에 반영하는 것이 안전합니다.",
        "commonMistakes": [
            {
                "mistake": "'load cell'을 '로드 셀'로 음차",
                "correction": "'ô tải' 또는 'cảm biến lực' 사용",
                "explanation": "베트남어 정식 명칭을 사용해야 전문성이 유지됩니다."
            },
            {
                "mistake": "로드셀과 압력계를 같은 것으로 설명",
                "correction": "로드셀(ô tải)은 하중 센서, 압력계(đồng hồ áp suất)는 유압 측정",
                "explanation": "두 장비는 측정 원리와 대상이 다릅니다."
            },
            {
                "mistake": "검교정 주기를 언급하지 않음",
                "correction": "로드셀 검교정 주기(chu kỳ hiệu chuẩn) 명시",
                "explanation": "검교정은 측정 정확도와 안전에 직결됩니다."
            }
        ],
        "examples": [
            {
                "ko": "PC강선 긴장 시 로드셀로 긴장력을 확인하세요.",
                "vi": "Khi căng thép PC, hãy kiểm tra lực căng bằng ô tải.",
                "situation": "onsite"
            },
            {
                "ko": "로드셀 검교정 성적서를 제출해 주시기 바랍니다.",
                "vi": "Vui lòng nộp giấy chứng nhận hiệu chuẩn ô tải.",
                "situation": "formal"
            },
            {
                "ko": "로드셀 값이 설계 긴장력에 도달했습니다.",
                "vi": "Giá trị ô tải đã đạt lực căng thiết kế.",
                "situation": "formal"
            }
        ],
        "relatedTerms": ["긴장력", "PC강선", "압력계", "계측관리"],
        "difficulty": "advanced",
        "importance": "high",
        "frequency": "medium"
    },
    {
        "slug": "thi-nghiem-tai-cho",
        "korean": "현장시험",
        "vietnamese": "Thí nghiệm tại chỗ",
        "hanja": "現場試驗",
        "hanjaReading": "現(나타날 현) + 場(마당 장) + 試(시험할 시) + 驗(시험할 험)",
        "pronunciation": "현장시험",
        "meaningKo": "건설 현장에서 직접 실시하는 각종 시험의 총칭입니다. 실내 시험실에서 하는 '실내시험'과 대비되는 개념으로, 지반의 평판재하시험, 콘크리트 슬럼프 시험, 다짐도 시험 등이 대표적입니다. 통역 시 주의할 점은 베트남어 'thí nghiệm tại chỗ'가 직역이지만, 실무에서는 'thí nghiệm hiện trường'(현장 시험)도 많이 쓰인다는 것입니다. 각 시험의 목적과 방법이 다르므로 구체적인 시험명을 명시하는 것이 중요하며, 한국 KS 기준과 베트남 TCVN 기준의 차이를 확인해야 합니다.",
        "meaningVi": "Tổng hợp các loại thí nghiệm được thực hiện trực tiếp tại công trường. Khái niệm này được phân biệt với 'thí nghiệm trong phòng' (thực hiện ở phòng thí nghiệm). Các thí nghiệm điển hình bao gồm thí nghiệm tải trọng nền, thí nghiệm sụt bê tông, thí nghiệm độ chặt đầm. Trong thực tế, thuật ngữ 'thí nghiệm hiện trường' cũng được sử dụng phổ biến.",
        "context": "품질 관리, 지반 조사, 콘크리트 공사",
        "culturalNote": "한국에서는 품질 관리를 위한 현장시험 빈도가 매우 높고 시험 기사가 상주하는 경우가 많지만, 베트남은 현장 여건에 따라 시험 주기가 유연한 편입니다. 국제 프로젝트에서는 시험 주기, 시험 방법(KS vs TCVN), 불합격 시 조치 등을 계약서에 구체적으로 명시하는 것이 분쟁을 예방하는 데 중요합니다.",
        "commonMistakes": [
            {
                "mistake": "'field test'를 '필드 테스트'로 음차",
                "correction": "'thí nghiệm tại chỗ' 또는 'thí nghiệm hiện trường' 사용",
                "explanation": "베트남어 정식 용어를 사용해야 전문성이 유지됩니다."
            },
            {
                "mistake": "현장시험과 실내시험을 구분하지 않음",
                "correction": "현장시험(tại chỗ/hiện trường), 실내시험(trong phòng) 명확히 구분",
                "explanation": "시험 장소와 방법에 따라 의미가 완전히 다릅니다."
            },
            {
                "mistake": "시험 기준(KS/TCVN)을 명시하지 않음",
                "correction": "적용 기준을 명확히 표기",
                "explanation": "기준이 다르면 시험 방법과 허용치가 달라질 수 있습니다."
            }
        ],
        "examples": [
            {
                "ko": "내일 오전에 뒤채움 다짐도 현장시험을 실시합니다.",
                "vi": "Sáng mai sẽ tiến hành thí nghiệm độ chặt đầm đất lấp tại chỗ.",
                "situation": "formal"
            },
            {
                "ko": "슬럼프 현장시험 결과 18cm로 적합합니다.",
                "vi": "Kết quả thí nghiệm sụt hiện trường là 18cm, đạt yêu cầu.",
                "situation": "formal"
            },
            {
                "ko": "현장시험 불합격이면 재시공이야.",
                "vi": "Nếu thí nghiệm tại chỗ không đạt thì phải thi công lại.",
                "situation": "informal"
            }
        ],
        "relatedTerms": ["슬럼프시험", "다짐도시험", "평판재하시험", "품질시험"],
        "difficulty": "beginner",
        "importance": "high",
        "frequency": "high"
    },
    {
        "slug": "thi-nghiem-chat-luong",
        "korean": "품질시험",
        "vietnamese": "Thí nghiệm chất lượng",
        "hanja": "品質試驗",
        "hanjaReading": "品(물건 품) + 質(바탕 질) + 試(시험할 시) + 驗(시험할 험)",
        "pronunciation": "품질시험",
        "meaningKo": "건설 자재 및 구조물의 품질을 확인하기 위해 실시하는 시험의 총칭입니다. 콘크리트 압축강도 시험, 철근 인장강도 시험, 토양 다짐도 시험, 아스팔트 밀도 시험 등이 포함됩니다. 통역 시 주의할 점은 '품질시험'이 매우 포괄적인 용어이므로, 실제 통역에서는 반드시 구체적인 시험명을 명시해야 한다는 것입니다. 베트남어 'thí nghiệm chất lượng'도 광범위하므로, 'thí nghiệm cường độ bê tông'(콘크리트 강도 시험) 등으로 구체화하는 것이 오해를 방지합니다. 또한 한국과 베트남의 품질 기준(KS vs TCVN)이 다르므로 계약 단계에서 적용 기준을 명확히 해야 합니다.",
        "meaningVi": "Tổng hợp các loại thí nghiệm nhằm xác minh chất lượng vật liệu xây dựng và công trình. Bao gồm thí nghiệm cường độ chịu nén bê tông, thí nghiệm kéo thép, thí nghiệm độ chặt đất, thí nghiệm mật độ asphalt, v.v. Vì đây là thuật ngữ rất rộng, trong thông dịch cần nêu rõ tên thí nghiệm cụ thể để tránh hiểu nhầm. Cần xác định rõ tiêu chuẩn áp dụng (KS Hàn Quốc hay TCVN Việt Nam) ngay từ giai đoạn ký hợp đồng.",
        "context": "품질 관리, 시험 계획, 검사 보고서",
        "culturalNote": "한국 건설 현장은 품질시험 빈도가 매우 높고 제3자 검증 기관(KS 인증 시험실)을 통한 시험이 의무화되어 있지만, 베트남은 자체 시험실을 운영하는 경우가 많아 객관성 논란이 있을 수 있습니다. 국제 프로젝트에서는 품질시험 주기, 시험 기관의 자격, 불합격 시 재시험 절차 등을 계약서에 상세히 규정하는 것이 분쟁을 예방하는 핵심입니다.",
        "commonMistakes": [
            {
                "mistake": "'quality test'를 '퀄리티 테스트'로 음차",
                "correction": "'thí nghiệm chất lượng' 사용",
                "explanation": "베트남어 정식 용어를 사용해야 합니다."
            },
            {
                "mistake": "구체적 시험명 없이 '품질시험'으로만 통역",
                "correction": "구체적 시험명 명시 (예: 콘크리트 강도 시험, 철근 인장 시험)",
                "explanation": "품질시험은 범위가 넓으므로 구체화가 필요합니다."
            },
            {
                "mistake": "KS와 TCVN 기준 차이를 설명하지 않음",
                "correction": "적용 기준과 양국 기준 차이 명시",
                "explanation": "기준이 다르면 합격/불합격 판정이 달라질 수 있습니다."
            }
        ],
        "examples": [
            {
                "ko": "품질시험 계획서를 작성하여 제출해 주시기 바랍니다.",
                "vi": "Vui lòng lập và nộp kế hoạch thí nghiệm chất lượng.",
                "situation": "formal"
            },
            {
                "ko": "품질시험 불합격 시 해당 부분은 재시공입니다.",
                "vi": "Nếu thí nghiệm chất lượng không đạt, phần đó phải thi công lại.",
                "situation": "formal"
            },
            {
                "ko": "품질시험 결과 나왔어? 언제 나와?",
                "vi": "Kết quả thí nghiệm chất lượng ra chưa? Khi nào ra?",
                "situation": "informal"
            }
        ],
        "relatedTerms": ["압축강도시험", "슬럼프시험", "현장시험", "KS인증"],
        "difficulty": "beginner",
        "importance": "high",
        "frequency": "high"
    }
]

# 기존 데이터 읽기
with open(file_path, "r", encoding="utf-8") as f:
    data = json.load(f)

# 신규 용어 추가
data.extend(new_terms)

# 파일 저장
with open(file_path, "w", encoding="utf-8") as f:
    json.dump(data, f, ensure_ascii=False, indent=2)

print(f"✅ {len(new_terms)}개 용어 추가 완료")
print(f"📂 파일: {file_path}")
print(f"📊 총 용어 수: {len(data)}개")
