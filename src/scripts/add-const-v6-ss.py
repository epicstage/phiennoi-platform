#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
건설 용어 추가 스크립트 v6 - 녹색건축/친환경 테마 (10개)
Tier S 기준 준수
"""

import json
import os

# 추가할 용어 데이터 (10개)
data = [
    {
        "slug": "chung-nhan-leed",
        "korean": "LEED인증",
        "vietnamese": "Chứng nhận LEED",
        "hanja": None,
        "hanjaReading": None,
        "pronunciation": "리드인증",
        "meaningKo": "Leadership in Energy and Environmental Design의 약자로, 미국 녹색건축위원회(USGBC)에서 개발한 친환경 건축물 인증제도입니다. 에너지 효율, 수자원 관리, 자재 선택, 실내 환경 등을 종합 평가하며, Platinum/Gold/Silver/Certified 등급으로 구분됩니다. 통역 시 '리드'로 발음하며, 한국의 녹색건축인증제(G-SEED)와 비교 설명이 필요합니다. 베트남에서는 최근 고급 오피스/주거 프로젝트에서 마케팅 포인트로 활용되고 있어, 인증 등급별 차이와 비용 대비 효과를 명확히 전달해야 합니다.",
        "meaningVi": "Chứng nhận về thiết kế năng lượng và môi trường tiên tiến do Hội đồng Công trình Xanh Hoa Kỳ phát triển. Đánh giá tổng hợp về hiệu quả năng lượng, quản lý nguồn nước, lựa chọn vật liệu và môi trường trong nhà.",
        "context": "국제 프로젝트, 친환경 건축 설계 회의, 인증 컨설팅",
        "culturalNote": "한국에서는 G-SEED(녹색건축인증)가 주로 사용되지만, 베트남에서는 국제 프로젝트를 중심으로 LEED 인증이 선호됩니다. 한국 건설사가 베트남에서 고급 프로젝트를 진행할 때 LEED 인증 취득이 마케팅 포인트가 되며, 인증 비용(약 2-5% 추가)과 장기 운영비 절감 효과를 함께 설명해야 합니다. 베트남에서는 LOTUS(베트남 친환경 인증)도 있지만 국제적 인지도는 LEED가 높습니다.",
        "commonMistakes": [
            {
                "mistake": "LEED를 '리드'가 아닌 '엘이이디'로 읽기",
                "correction": "'리드'로 발음",
                "explanation": "약어이지만 관용적으로 'lead'처럼 발음하는 것이 국제 표준입니다"
            },
            {
                "mistake": "G-SEED와 LEED를 동일 인증으로 설명",
                "correction": "별개의 인증체계임을 명시하고 평가 기준 차이 설명",
                "explanation": "한국 G-SEED는 국내 법규 기반, LEED는 미국 기준이며 평가 항목이 다릅니다"
            },
            {
                "mistake": "인증 등급을 한국어로만 설명",
                "correction": "Platinum/Gold/Silver/Certified로 원어 병기",
                "explanation": "국제 프로젝트에서는 영문 등급명이 공식 표기이기 때문입니다"
            }
        ],
        "examples": [
            {
                "ko": "이 프로젝트는 LEED Gold 인증을 목표로 설계되었습니다.",
                "vi": "Dự án này được thiết kế nhằm đạt chứng nhận LEED Gold.",
                "situation": "formal"
            },
            {
                "ko": "LEED 인증 취득을 위해 에너지 시뮬레이션 결과를 제출해야 합니다.",
                "vi": "Để đạt chứng nhận LEED, chúng ta cần nộp kết quả mô phỏng năng lượng.",
                "situation": "onsite"
            },
            {
                "ko": "LEED 인증 비용이 추가되지만 장기적으로 운영비가 절감됩니다.",
                "vi": "Chi phí chứng nhận LEED tăng thêm nhưng lâu dài sẽ tiết kiệm chi phí vận hành.",
                "situation": "formal"
            }
        ],
        "relatedTerms": ["녹색건축인증", "패시브하우스", "에너지성능등급", "제로에너지건축"]
    },
    {
        "slug": "nha-khong-nang-luong",
        "korean": "제로에너지건축",
        "vietnamese": "Nhà không năng lượng (Zero Energy Building)",
        "hanja": "零energy建築",
        "hanjaReading": "영(제로 영) + energy + 건(집 건) + 축(쌓을 축)",
        "pronunciation": "제로에너지건축",
        "meaningKo": "연간 에너지 소비량과 생산량이 같아 외부 에너지 공급이 필요 없는 건축물입니다. 고효율 단열, 기밀성 확보, 태양광 발전, 지열 시스템 등을 통합 적용하여 에너지 자립을 실현합니다. 통역 시 'Net Zero'와 'Nearly Zero' 개념 차이를 구분해야 하며, 한국의 제로에너지건축물 인증제도(ZEB 1~5등급)와 베트남의 관련 정책을 비교 설명할 수 있어야 합니다. 초기 투자비가 일반 건축 대비 10-20% 높지만, 장기 에너지 비용 절감 효과를 강조해야 합니다.",
        "meaningVi": "Công trình xây dựng có lượng năng lượng tiêu thụ hàng năm bằng với lượng sản xuất, không cần cung cấp năng lượng từ bên ngoài. Áp dụng tích hợp cách nhiệt hiệu quả cao, hệ thống điện mặt trời, địa nhiệt.",
        "context": "신재생에너지 설계, 공공건축 프로젝트, 에너지 정책 논의",
        "culturalNote": "한국은 2020년부터 공공건축물에 제로에너지건축 의무화를 단계적으로 시행 중이며, 2025년부터는 민간 건축물까지 확대 예정입니다. 베트남은 아직 의무화 단계는 아니지만, 하노이/호치민 등 대도시 중심으로 시범 프로젝트가 진행되고 있습니다. 한국 건설사가 베트남에 진출할 때 제로에너지 기술을 차별화 요소로 활용할 수 있으나, 베트남의 높은 일조량과 냉방 부하 특성을 고려한 설계 조정이 필요합니다.",
        "commonMistakes": [
            {
                "mistake": "'제로에너지'를 '에너지 사용 안 함'으로 오해",
                "correction": "'에너지 소비와 생산이 같음'으로 설명",
                "explanation": "에너지를 쓰지 않는 것이 아니라 생산량으로 상쇄하는 개념입니다"
            },
            {
                "mistake": "Net Zero와 Nearly Zero를 구분하지 않음",
                "correction": "Net Zero(100% 상쇄)와 Nearly Zero(거의 제로) 차이 명시",
                "explanation": "유럽과 미국에서 사용하는 개념이 다르기 때문에 정확한 구분이 필요합니다"
            },
            {
                "mistake": "제로에너지 인증등급을 생략",
                "correction": "한국 ZEB 1~5등급 체계 설명",
                "explanation": "등급에 따라 에너지 자립률이 20%~100%로 다르므로 명확히 해야 합니다"
            }
        ],
        "examples": [
            {
                "ko": "이 건물은 ZEB 1등급 제로에너지건축 인증을 받았습니다.",
                "vi": "Tòa nhà này đã đạt chứng nhận ZEB cấp 1 (Zero Energy Building).",
                "situation": "formal"
            },
            {
                "ko": "제로에너지 달성을 위해 옥상에 태양광 패널을 추가 설치합니다.",
                "vi": "Để đạt mục tiêu không năng lượng, chúng ta sẽ lắp thêm tấm pin mặt trời trên mái.",
                "situation": "onsite"
            },
            {
                "ko": "제로에너지 설계로 연간 전기료를 80% 절감할 수 있습니다.",
                "vi": "Với thiết kế không năng lượng, có thể tiết kiệm 80% chi phí điện hàng năm.",
                "situation": "formal"
            }
        ],
        "relatedTerms": ["패시브하우스", "태양광패널", "에너지성능등급", "신재생에너지"]
    },
    {
        "slug": "nha-passive",
        "korean": "패시브하우스",
        "vietnamese": "Nhà Passive (Nhà tiết kiệm năng lượng siêu cao)",
        "hanja": None,
        "hanjaReading": None,
        "pronunciation": "패시브하우스",
        "meaningKo": "독일에서 개발된 초저에너지 건축 기준으로, 연간 난방에너지 요구량이 15kWh/㎡ 이하인 건축물입니다. 고성능 단열재, 3중 유리창, 열회수 환기장치(HRV/ERV), 기밀시공 등을 통해 최소한의 냉난방으로 쾌적한 실내환경을 유지합니다. 통역 시 '액티브(기계설비 의존)'와 '패시브(건물 성능 의존)'의 대비를 명확히 하고, 한국의 패시브건축물 인증기준과 독일 Passivhaus Institut 기준의 차이를 설명할 수 있어야 합니다. 베트남의 고온다습 기후에서는 냉방 부하 저감이 핵심입니다.",
        "meaningVi": "Tiêu chuẩn xây dựng siêu tiết kiệm năng lượng phát triển tại Đức, với nhu cầu năng lượng sưởi ấm dưới 15kWh/㎡ mỗi năm. Sử dụng vật liệu cách nhiệt cao cấp, cửa kính 3 lớp, hệ thống thông gió thu hồi nhiệt.",
        "context": "친환경 주택 설계, 에너지 효율 컨설팅, 단열 시공 현장",
        "culturalNote": "독일/유럽에서 발전한 패시브하우스 개념은 추운 기후의 난방 절감에 최적화되어 있어, 베트남처럼 냉방 부하가 큰 열대 기후에서는 설계 방식을 조정해야 합니다. 한국에서는 2000년대 중반부터 도입되어 공동주택을 중심으로 확산되었으나, 베트남에서는 아직 초기 단계입니다. 통역 시 '패시브=수동적'이라는 일반 의미와 혼동하지 않도록 '초저에너지'로 부연 설명하고, 베트남 건설사에게는 차양/자연환기 등 열대 기후 특화 전략을 강조해야 합니다.",
        "commonMistakes": [
            {
                "mistake": "'패시브'를 '수동적'으로 직역",
                "correction": "'초저에너지 건축'으로 의미 설명",
                "explanation": "Passive는 기계설비가 아닌 건물 성능으로 에너지를 절약한다는 기술 용어입니다"
            },
            {
                "mistake": "패시브하우스와 제로에너지를 혼동",
                "correction": "패시브는 에너지 저감, 제로는 생산까지 포함",
                "explanation": "패시브하우스는 에너지 소비 최소화가 목표이고, 제로에너지는 생산으로 상쇄까지 포함합니다"
            },
            {
                "mistake": "한국/독일 기준을 구분 없이 사용",
                "correction": "Passivhaus Institut 기준과 한국 패시브건축물 인증 차이 명시",
                "explanation": "독일 기준이 더 엄격하며(15kWh/㎡), 한국은 완화된 기준을 적용합니다"
            }
        ],
        "examples": [
            {
                "ko": "이 주택은 패시브하우스 인증을 받아 냉난방비가 거의 들지 않습니다.",
                "vi": "Ngôi nhà này đạt chứng nhận Passive House nên chi phí sưởi và làm mát gần như bằng không.",
                "situation": "formal"
            },
            {
                "ko": "패시브하우스 시공을 위해 기밀테이프로 모든 틈새를 막아야 합니다.",
                "vi": "Để thi công nhà Passive, phải dùng băng kín khí bịt kín mọi khe hở.",
                "situation": "onsite"
            },
            {
                "ko": "패시브 설계로 에어컨 용량을 일반 주택의 절반으로 줄일 수 있습니다.",
                "vi": "Với thiết kế Passive, có thể giảm công suất máy lạnh xuống một nửa so với nhà thông thường.",
                "situation": "formal"
            }
        ],
        "relatedTerms": ["제로에너지건축", "고효율단열", "열회수환기", "기밀시공"]
    },
    {
        "slug": "tam-pin-mat-troi",
        "korean": "태양광패널",
        "vietnamese": "Tấm pin mặt trời",
        "hanja": "太陽光panel",
        "hanjaReading": "태(클 태) + 양(볕 양) + 광(빛 광) + panel",
        "pronunciation": "태양광패널",
        "meaningKo": "태양광을 전기로 변환하는 광전지 모듈로, 건축물의 에너지 자립과 신재생에너지 의무비율 충족을 위해 설치됩니다. 단결정/다결정/박막형 등 종류가 있으며, 설치 각도/방향/그늘 여부에 따라 발전 효율이 크게 달라집니다. 통역 시 '태양광(발전)'과 '태양열(온수)'을 명확히 구분하고, 한국의 REC(신재생에너지공급인증서) 제도와 베트남의 FIT(발전차액지원) 제도를 비교 설명할 수 있어야 합니다. 베트남은 일조량이 풍부해 투자 회수 기간이 한국보다 짧습니다.",
        "meaningVi": "Tấm quang điện chuyển đổi ánh sáng mặt trời thành điện năng, được lắp đặt để tự cung cấp năng lượng cho công trình và đáp ứng tỷ lệ năng lượng tái tạo bắt buộc. Hiệu suất phát điện thay đổi tùy góc lắp đặt, hướng và bóng mát.",
        "context": "신재생에너지 설계, 옥상 시공, 전기 설비 회의",
        "culturalNote": "한국은 태양광 보조금과 REC 거래 시장이 잘 갖춰져 있어 상업용 건물에 태양광 설치가 활발하나, 베트nam은 최근 FIT 제도가 축소되면서 투자 매력도가 다소 감소했습니다. 그러나 베트남의 높은 일조량(연간 1,600~2,700시간)은 한국(1,200~1,500시간)보다 유리하며, 자가소비 중심 설계 시 여전히 경제성이 높습니다. 통역 시 '태양광'과 '태양열'을 혼동하지 않도록 주의하고, 베트남어로는 'năng lượng mặt trời'(태양에너지)로 통칭되므로 'điện mặt trời'(태양광 전기)로 명확히 구분해야 합니다.",
        "commonMistakes": [
            {
                "mistake": "태양광과 태양열을 혼용",
                "correction": "태양광(điện mặt trời)은 전기, 태양열(nhiệt mặt trời)은 온수 생산",
                "explanation": "베트남어에서 모두 'năng lượng mặt trời'로 불리기 쉬우나 기술적으로 완전히 다릅니다"
            },
            {
                "mistake": "패널 효율을 %로만 표기",
                "correction": "효율(%)과 설치용량(kWp) 함께 명시",
                "explanation": "실제 발전량은 용량에 비례하므로 둘 다 중요합니다"
            },
            {
                "mistake": "REC/FIT 제도를 동일하게 설명",
                "correction": "한국 REC는 인증서 거래, 베트남 FIT는 발전차액 보전",
                "explanation": "제도 구조가 다르므로 수익 구조도 다릅니다"
            }
        ],
        "examples": [
            {
                "ko": "옥상에 100kWp 태양광패널을 설치하여 연간 전력 사용량의 30%를 충당합니다.",
                "vi": "Lắp đặt tấm pin mặt trời 100kWp trên mái để đáp ứng 30% lượng điện tiêu thụ hàng năm.",
                "situation": "formal"
            },
            {
                "ko": "태양광패널 설치 각도를 위도에 맞춰 조정해야 발전 효율이 최대화됩니다.",
                "vi": "Phải điều chỉnh góc lắp tấm pin mặt trời theo vĩ độ để tối đa hóa hiệu suất phát điện.",
                "situation": "onsite"
            },
            {
                "ko": "태양광 발전으로 REC를 확보하여 신재생에너지 의무비율을 충족했습니다.",
                "vi": "Phát điện mặt trời giúp đạt được REC và đáp ứng tỷ lệ năng lượng tái tạo bắt buộc.",
                "situation": "formal"
            }
        ],
        "relatedTerms": ["제로에너지건축", "신재생에너지", "ESS", "인버터"]
    },
    {
        "slug": "he-thong-su-dung-nuoc-mua",
        "korean": "빗물이용시스템",
        "vietnamese": "Hệ thống sử dụng nước mưa",
        "hanja": None,
        "hanjaReading": None,
        "pronunciation": "빈물이용시스템",
        "meaningKo": "지붕이나 포장면에 내린 빗물을 수집·저장하여 조경용수, 화장실 세정수, 청소용수 등 비음용수로 활용하는 시설입니다. 집수면적, 강우량, 저장탱크 용량을 계산하여 설계하며, 초기 우수(first flush) 배제 장치와 필터를 통해 수질을 관리합니다. 통역 시 중수(greywater)와 빗물(rainwater)을 구분하고, 한국의 빗물관리시설 설치 의무 대상(1,000㎡ 이상)과 베트남의 관련 규정을 비교할 수 있어야 합니다. 베트남은 우기에 집중 강우가 있어 저장 용량 설계가 중요합니다.",
        "meaningVi": "Hệ thống thu gom và lưu trữ nước mưa từ mái nhà hoặc bề mặt đường để sử dụng cho tưới cây, xả toilet, vệ sinh. Quản lý chất lượng nước qua thiết bị loại bỏ nước mưa đầu (first flush) và bộ lọc.",
        "context": "친환경 설비 설계, 수자원 절약 프로젝트, LEED 인증",
        "culturalNote": "한국은 서울 등 대도시에서 빗물관리시설 설치가 의무화되어 있으나, 베트남은 아직 법적 의무는 없고 자발적 설치가 대부분입니다. 베트남은 우기(5~10월)에 강우가 집중되어 연간 강우량은 한국보다 많지만(1,500~2,500mm vs 1,200~1,500mm), 건기에는 물 부족이 심각해 빗물 저장 시설의 경제성이 높습니다. 통역 시 '빗물이용'과 '중수이용'을 명확히 구분하고, 베트남의 우기/건기 특성에 맞는 탱크 용량 설계(건기 3~6개월 분)를 강조해야 합니다.",
        "commonMistakes": [
            {
                "mistake": "빗물과 중수를 혼동",
                "correction": "빗물(nước mưa)은 빗물, 중수(nước tái sử dụng)는 생활하수 재이용",
                "explanation": "수원과 처리 방법이 완전히 다릅니다"
            },
            {
                "mistake": "저장탱크 용량을 연간 평균 강우량으로 계산",
                "correction": "우기 집중 강우와 건기 사용량을 고려한 설계",
                "explanation": "베트남은 우기/건기 차이가 커서 평균값으로는 부족합니다"
            },
            {
                "mistake": "초기 우수(first flush) 처리 생략",
                "correction": "지붕 오염물 배제 장치 필수 설치",
                "explanation": "초기 빗물은 먼지/오염물이 많아 수질 문제가 발생합니다"
            }
        ],
        "examples": [
            {
                "ko": "이 건물은 50톤 용량의 빗물저장탱크로 연간 상수도 사용량을 20% 절감합니다.",
                "vi": "Tòa nhà này tiết kiệm 20% lượng nước máy hàng năm nhờ bể chứa nước mưa 50 tấn.",
                "situation": "formal"
            },
            {
                "ko": "빗물이용시스템에 초기 우수 배제 장치를 설치해야 수질이 확보됩니다.",
                "vi": "Phải lắp thiết bị loại bỏ nước mưa đầu trong hệ thống để đảm bảo chất lượng nước.",
                "situation": "onsite"
            },
            {
                "ko": "LEED 인증을 위해 빗물이용으로 조경용수 100%를 충당하는 설계입니다.",
                "vi": "Để đạt chứng nhận LEED, thiết kế sử dụng 100% nước mưa cho tưới cảnh quan.",
                "situation": "formal"
            }
        ],
        "relatedTerms": ["중수이용", "수자원절약", "LEED인증", "우수유출저감"]
    },
    {
        "slug": "he-thong-tai-su-dung-nuoc",
        "korean": "중수이용시스템",
        "vietnamese": "Hệ thống tái sử dụng nước (Nước trung)",
        "hanja": "中水利用system",
        "hanjaReading": "중(가운데 중) + 수(물 수) + 이(이로울 이) + 용(쓸 용) + system",
        "pronunciation": "중수이용시스템",
        "meaningKo": "세면·샤워·세탁 등에서 발생하는 생활하수(greywater)를 처리하여 화장실 세정수, 조경용수, 청소용수 등으로 재이용하는 시설입니다. 오수(blackwater, 변기 배수)와 구분하여 수집하며, 침전·여과·소독 과정을 거쳐 재이용 기준에 맞게 처리합니다. 통역 시 '중수'의 '중(中)'은 상수와 하수의 중간 수질이라는 의미임을 설명하고, 한국의 중수도 설치 의무 대상(연면적 3만㎡ 이상)과 베트남의 물 재이용 정책을 비교할 수 있어야 합니다. 베트남은 수자원 부족이 심각해 중수 재이용의 경제성이 높습니다.",
        "meaningVi": "Hệ thống xử lý nước thải sinh hoạt nhẹ (rửa mặt, tắm, giặt) để tái sử dụng cho xả toilet, tưới cây, vệ sinh. Thu gom riêng với nước đen (blackwater) và xử lý qua các giai đoạn lắng, lọc, khử trùng.",
        "context": "대형 건축물 설비, 수자원 절약, 환경영향평가",
        "culturalNote": "한국은 일정 규모 이상 건축물(연면적 3만㎡ 이상 또는 300세대 이상 공동주택)에 중수도 설치가 의무화되어 있으며, 베트남은 의무 규정은 없으나 호치민/하노이 등 대도시에서 물 부족 문제로 관심이 높아지고 있습니다. 베트남의 경우 상수도 요금이 한국보다 상대적으로 높고 물 부족이 심각해 중수 재이용의 경제성이 더 큽니다. 통역 시 'greywater'와 'blackwater'를 명확히 구분하고, 베트남 건설사에게는 초기 투자비 대비 장기 절감 효과(상수도 사용량 30~40% 절감)를 강조해야 합니다.",
        "commonMistakes": [
            {
                "mistake": "중수와 하수를 같은 것으로 설명",
                "correction": "중수(처리된 생활하수)와 하수(미처리 오염수) 구분",
                "explanation": "중수는 재이용 가능하게 처리된 물이며, 하수는 원수입니다"
            },
            {
                "mistake": "Greywater와 Blackwater를 구분 없이 사용",
                "correction": "Greywater(중수 원수)와 Blackwater(오수) 명확히 구분",
                "explanation": "변기 배수(blackwater)는 중수 원수로 사용 불가합니다"
            },
            {
                "mistake": "중수를 음용수로 설명",
                "correction": "비음용수(화장실, 조경)만 사용 가능",
                "explanation": "중수는 처리되었지만 음용 기준에는 미달입니다"
            }
        ],
        "examples": [
            {
                "ko": "이 빌딩은 중수이용시스템으로 화장실 세정수 100%를 충당합니다.",
                "vi": "Tòa nhà này sử dụng hệ thống nước trung để đáp ứng 100% nước xả toilet.",
                "situation": "formal"
            },
            {
                "ko": "중수처리장에서 생활하수를 침전·여과·소독 과정으로 처리합니다.",
                "vi": "Trạm xử lý nước trung xử lý nước thải sinh hoạt qua các giai đoạn lắng, lọc, khử trùng.",
                "situation": "onsite"
            },
            {
                "ko": "중수도 설치로 연간 상수도 사용량을 35% 절감할 수 있습니다.",
                "vi": "Lắp đặt hệ thống nước trung giúp tiết kiệm 35% lượng nước máy hàng năm.",
                "situation": "formal"
            }
        ],
        "relatedTerms": ["빗물이용", "수자원절약", "폐수처리", "생활하수"]
    },
    {
        "slug": "anh-sang-tu-nhien",
        "korean": "자연채광",
        "vietnamese": "Ánh sáng tự nhiên",
        "hanja": "自然採光",
        "hanjaReading": "자(스스로 자) + 연(그럴 연) + 채(캘 채) + 광(빛 광)",
        "pronunciation": "자연채광",
        "meaningKo": "창문, 천창, 라이트웰 등을 통해 자연광을 실내로 끌어들여 인공조명 사용을 줄이는 설계 기법입니다. 채광계수(daylight factor), 창면적비, 유리 투과율 등을 계산하여 건축법 기준(거실 바닥면적의 1/7 이상)을 충족하도록 설계하며, 과도한 직사광선에 의한 눈부심과 열부하를 제어하기 위해 루버, 블라인드, 로이유리 등을 적용합니다. 통역 시 '채광(자연광 유입)'과 '조명(인공조명)'을 구분하고, LEED의 Daylight Credit과 한국 건축법의 채광 기준을 비교 설명할 수 있어야 합니다.",
        "meaningVi": "Kỹ thuật thiết kế đưa ánh sáng tự nhiên vào trong nhà qua cửa sổ, cửa trời, giếng trời để giảm sử dụng đèn điện. Tính toán hệ số ánh sáng ban ngày, tỷ lệ diện tích cửa, độ truyền ánh sáng của kính.",
        "context": "건축 설계, 조명 계획, 에너지 효율 검토",
        "culturalNote": "한국 건축법은 거실 바닥면적의 1/7 이상을 채광을 위한 창으로 확보하도록 규정하며, 베트남도 유사한 규정(QCXDVN 01:2008)이 있으나 집행이 느슨한 편입니다. 베트남은 연중 일조량이 풍부하여 자연채광 설계 시 에너지 절감 효과가 크지만, 열대 기후 특성상 직사광선에 의한 열부하와 눈부심 문제가 심각해 차양 설계가 필수입니다. 통역 시 '채광'이 단순히 창을 크게 만드는 것이 아니라 적절한 빛의 질과 양을 확보하는 것임을 강조하고, 베트남의 높은 일조량을 활용하되 열부하를 차단하는 전략을 설명해야 합니다.",
        "commonMistakes": [
            {
                "mistake": "'채광'을 '조명'으로 번역",
                "correction": "채광(ánh sáng tự nhiên)은 자연광, 조명(chiếu sáng)은 인공조명",
                "explanation": "완전히 다른 개념이며, 에너지 소비와 직결됩니다"
            },
            {
                "mistake": "창면적만 크게 하면 된다고 설명",
                "correction": "채광계수, 유리 성능, 차양 설계 통합 필요",
                "explanation": "과도한 직사광선은 눈부심과 냉방부하 증가를 유발합니다"
            },
            {
                "mistake": "채광 기준을 면적비로만 설명",
                "correction": "채광계수(%), 조도(lux), UDI(Useful Daylight Illuminance) 함께 언급",
                "explanation": "LEED 등 국제 기준은 조도 성능까지 평가합니다"
            }
        ],
        "examples": [
            {
                "ko": "이 사무실은 자연채광으로 낮 시간 인공조명 사용을 70% 줄였습니다.",
                "vi": "Văn phòng này giảm 70% sử dụng đèn điện ban ngày nhờ ánh sáng tự nhiên.",
                "situation": "formal"
            },
            {
                "ko": "천창을 통한 자연채광으로 복도에도 충분한 밝기를 확보했습니다.",
                "vi": "Ánh sáng tự nhiên qua cửa trời giúp hành lang đủ sáng.",
                "situation": "onsite"
            },
            {
                "ko": "자연채광 설계로 LEED Daylight Credit을 획득했습니다.",
                "vi": "Thiết kế ánh sáng tự nhiên giúp đạt được LEED Daylight Credit.",
                "situation": "formal"
            }
        ],
        "relatedTerms": ["자연환기", "패시브디자인", "루버", "로이유리"]
    },
    {
        "slug": "thong-gio-tu-nhien",
        "korean": "자연환기",
        "vietnamese": "Thông gió tự nhiên",
        "hanja": "自然換氣",
        "hanjaReading": "자(스스로 자) + 연(그럴 연) + 환(바꿀 환) + 기(기운 기)",
        "pronunciation": "자연환기",
        "meaningKo": "기계환기 없이 실내외 온도차, 바람 압력차, 풍향 등을 이용해 자연스럽게 공기를 순환시키는 설계 기법입니다. Cross Ventilation(맞통풍), Stack Effect(굴뚝효과) 등의 원리를 활용하며, 창호 배치, 개구부 면적, 건물 방향 등을 종합적으로 설계합니다. 통역 시 '환기(ventilation)'와 '통풍(draft)'을 구분하고, 한국의 쾌적 환기 기준(1인당 30㎥/h)과 베트남의 고온다습 기후에 맞는 환기 전략을 비교해야 합니다. 베트남은 자연환기가 에너지 절감에 큰 효과가 있으나, 우기의 습도 관리가 과제입니다.",
        "meaningVi": "Kỹ thuật thiết kế tuần hoàn không khí tự nhiên mà không cần hệ thống thông gió cơ học, dựa vào chênh lệch nhiệt độ trong-ngoài, áp suất gió. Áp dụng nguyên lý thông gió chéo (Cross Ventilation) và hiệu ứng ống khói (Stack Effect).",
        "context": "건축 설계, 냉난방 계획, 실내공기질 관리",
        "culturalNote": "한국은 사계절이 뚜렷하고 난방 기간이 길어 자연환기보다 기계환기(열회수환기)를 선호하지만, 베트남은 연중 고온으로 자연환기가 에너지 절감과 쾌적성 확보에 매우 효과적입니다. 베트남 전통 가옥은 맞통풍 구조로 자연환기를 극대화하는 설계가 일반적이며, 현대 건축에서도 이를 적극 활용합니다. 통역 시 베트남의 높은 습도(연평균 80% 이상)로 인해 자연환기만으로는 곰팡이 문제가 발생할 수 있어, 필요 시 제습 설비를 병행해야 함을 강조해야 합니다. 한국 건설사는 밀폐형 설계에 익숙하므로 베트남의 개방형 설계 문화를 이해시키는 것이 중요합니다.",
        "commonMistakes": [
            {
                "mistake": "'환기'와 '통풍'을 같은 의미로 사용",
                "correction": "환기(thông gió)는 공기 교환, 통풍(gió lùa)은 바람 흐름",
                "explanation": "환기는 실내공기질 관리, 통풍은 체감온도 저하가 목적입니다"
            },
            {
                "mistake": "한국식 밀폐 설계를 베트남에 그대로 적용",
                "correction": "베트남 기후에 맞는 개방형 설계 권장",
                "explanation": "베트남은 연중 고온으로 자연환기가 필수적입니다"
            },
            {
                "mistake": "습도 관리를 고려하지 않은 자연환기",
                "correction": "우기(5~10월) 습도 조절 전략 필요",
                "explanation": "자연환기만으로는 높은 습도로 곰팡이 발생 위험이 있습니다"
            }
        ],
        "examples": [
            {
                "ko": "이 건물은 맞통풍 구조로 자연환기만으로 쾌적한 실내환경을 유지합니다.",
                "vi": "Tòa nhà này duy trì môi trường trong nhà thoải mái chỉ bằng thông gió tự nhiên nhờ cấu trúc thông gió chéo.",
                "situation": "formal"
            },
            {
                "ko": "자연환기를 위해 남북 방향으로 창을 대칭 배치했습니다.",
                "vi": "Để thông gió tự nhiên, đã bố trí cửa sổ đối xứng theo hướng Nam-Bắc.",
                "situation": "onsite"
            },
            {
                "ko": "자연환기 설계로 냉방 에너지를 40% 절감할 수 있습니다.",
                "vi": "Thiết kế thông gió tự nhiên giúp tiết kiệm 40% năng lượng làm mát.",
                "situation": "formal"
            }
        ],
        "relatedTerms": ["자연채광", "패시브디자인", "Cross Ventilation", "실내공기질"]
    },
    {
        "slug": "cach-nhiet-hieu-suat-cao",
        "korean": "고효율단열",
        "vietnamese": "Cách nhiệt hiệu suất cao",
        "hanja": "高效率斷熱",
        "hanjaReading": "고(높을 고) + 효(공 효) + 율(법 률) + 단(끊을 단) + 열(더울 열)",
        "pronunciation": "고효율단열",
        "meaningKo": "열관류율(U-value)이 낮은 고성능 단열재를 적용하여 건물 외피를 통한 열손실/열취득을 최소화하는 공법입니다. 압출법보온판(XPS), 비드법보온판(EPS), 폴리우레탄폼, 유리섬유 등 단열재의 두께와 열전도율을 설계하며, 열교(thermal bridge) 차단 디테일이 중요합니다. 통역 시 R-value(열저항)와 U-value(열관류율)를 구분하고, 한국의 건축물 에너지절약설계기준(지역별 0.15~0.36 W/㎡K)과 베트남의 기준을 비교해야 합니다. 베트남은 냉방 위주라 단열보다 차열(solar heat gain control)이 더 중요합니다.",
        "meaningVi": "Công pháp áp dụng vật liệu cách nhiệt hiệu suất cao với hệ số truyền nhiệt (U-value) thấp để tối thiểu hóa mất nhiệt/thu nhiệt qua vỏ công trình. Thiết kế độ dày và độ dẫn nhiệt của vật liệu như XPS, EPS, polyurethane, sợi thủy tinh.",
        "context": "에너지 설계, 외벽 시공, 패시브하우스",
        "culturalNote": "한국은 겨울 난방 에너지 절감을 위해 고효율 단열을 매우 중시하며(특히 북부 지역), 건축물 에너지절약설계기준이 엄격합니다. 반면 베트남은 연중 고온으로 난방이 거의 없고, 단열보다는 태양열 차단(차열)이 더 중요합니다. 베트남 건설에서 '단열'을 강조하면 시공사가 과잉 스펙으로 오해할 수 있으므로, '차열+적정 단열'로 구체화해야 합니다. 통역 시 한국의 '단열 두께 기준'을 베트남에 그대로 적용하지 말고, 냉방부하 저감 관점에서 최적 두께를 설명해야 합니다. 베트남은 습도가 높아 결로 방지보다 곰팡이 방지가 핵심입니다.",
        "commonMistakes": [
            {
                "mistake": "R-value와 U-value를 혼동",
                "correction": "R-value는 열저항(높을수록 좋음), U-value는 열관류율(낮을수록 좋음)",
                "explanation": "R-value = 1/U-value 관계이며, 국제 기준이 다릅니다"
            },
            {
                "mistake": "한국 단열 기준을 베트남에 그대로 적용",
                "correction": "베트남은 차열(단열 일부 + 반사/차양) 중심 설계",
                "explanation": "베트남은 냉방 위주이므로 과도한 단열은 비경제적입니다"
            },
            {
                "mistake": "열교(thermal bridge) 처리 생략",
                "correction": "기둥/보 접합부 단열 디테일 필수",
                "explanation": "열교 부위에서 에너지 손실이 집중되고 결로가 발생합니다"
            }
        ],
        "examples": [
            {
                "ko": "외벽에 200mm 고효율단열재를 시공하여 U-value 0.15를 달성했습니다.",
                "vi": "Thi công vật liệu cách nhiệt hiệu suất cao 200mm trên tường ngoài đạt U-value 0.15.",
                "situation": "formal"
            },
            {
                "ko": "고효율단열로 냉난방 에너지를 연간 30% 절감할 수 있습니다.",
                "vi": "Cách nhiệt hiệu suất cao giúp tiết kiệm 30% năng lượng sưởi và làm mát hàng năm.",
                "situation": "onsite"
            },
            {
                "ko": "패시브하우스 기준을 충족하기 위해 열교 부위까지 단열 처리했습니다.",
                "vi": "Để đáp ứng tiêu chuẩn Passive House, đã xử lý cách nhiệt cả vị trí cầu nhiệt (thermal bridge).",
                "situation": "formal"
            }
        ],
        "relatedTerms": ["패시브하우스", "열관류율", "열교차단", "에너지성능등급"]
    },
    {
        "slug": "dang-cap-hieu-nang-nang-luong",
        "korean": "에너지성능등급",
        "vietnamese": "Đẳng cấp hiệu năng năng lượng",
        "hanja": "energy性能等級",
        "hanjaReading": "energy + 성(본성 성) + 능(능할 능) + 등(무리 등) + 급(등급 급)",
        "pronunciation": "에너지성능등급",
        "meaningKo": "건축물의 에너지 효율을 평가하여 1+++~7등급(또는 A~G등급)으로 표시하는 인증제도입니다. 단위면적당 연간 1차 에너지소요량(kWh/㎡·년)을 기준으로 평가하며, 외피 단열성능, 냉난방 설비 효율, 신재생에너지 적용 등을 종합 평가합니다. 통역 시 한국의 건축물 에너지효율등급 인증제도와 유럽의 EPC(Energy Performance Certificate), 베트남의 에너지 라벨링 제도를 비교 설명할 수 있어야 합니다. 1등급 건물은 7등급 대비 에너지 비용이 60~70% 낮습니다.",
        "meaningVi": "Chế độ chứng nhận đánh giá hiệu suất năng lượng của công trình theo thang 1+++~7 (hoặc A~G). Đánh giá dựa trên lượng năng lượng sơ cấp tiêu thụ hàng năm trên đơn vị diện tích (kWh/㎡·năm), tổng hợp hiệu suất cách nhiệt vỏ công trình, hiệu suất thiết bị sưởi và làm mát.",
        "context": "건물 인증, 에너지 진단, 부동산 거래",
        "culturalNote": "한국은 2013년부터 공공건축물에 에너지효율등급 인증이 의무화되었고, 민간도 인센티브(용적률 완화 등)로 유도하고 있습니다. 베트남은 아직 의무 제도는 없으나, 건설부(Ministry of Construction)가 에너지 라벨링 제도를 도입 중이며 고급 주거/상업 프로젝트에서 자발적으로 인증을 받는 추세입니다. 통역 시 한국의 '1등급'과 유럽의 'A등급'이 유사하다는 점을 설명하고, 베트남 건설사에게는 에너지 등급이 건물 가치와 임대료에 직접 영향을 준다는 점(연구에 따르면 1등급 건물이 7등급 대비 임대료 10~15% 높음)을 강조해야 합니다.",
        "commonMistakes": [
            {
                "mistake": "등급을 숫자만으로 표기 (예: '1등급'만)",
                "correction": "1차 에너지소요량(kWh/㎡·년)과 함께 명시",
                "explanation": "등급 기준은 계속 강화되므로 절대값을 함께 제시해야 합니다"
            },
            {
                "mistake": "한국 등급 체계를 베트남에 그대로 적용",
                "correction": "베트남은 별도 기준 개발 중이며, 국제 기준 참조",
                "explanation": "베트남은 한국과 기후가 달라 등급 기준도 다릅니다"
            },
            {
                "mistake": "1차 에너지와 최종 에너지를 혼동",
                "correction": "1차 에너지(생산단계 포함)와 최종 에너지(사용단계) 구분",
                "explanation": "에너지효율등급은 1차 에너지 기준이며, 전기는 환산계수 2.75 적용됩니다"
            }
        ],
        "examples": [
            {
                "ko": "이 건물은 1등급 에너지성능 인증으로 연간 에너지 비용이 7등급 대비 65% 낮습니다.",
                "vi": "Tòa nhà này đạt chứng nhận hiệu năng năng lượng cấp 1, chi phí năng lượng hàng năm thấp hơn 65% so với cấp 7.",
                "situation": "formal"
            },
            {
                "ko": "에너지성능 1등급 취득을 위해 태양광 20kWp를 추가 설치합니다.",
                "vi": "Để đạt hiệu năng năng lượng cấp 1, sẽ lắp thêm 20kWp điện mặt trời.",
                "situation": "onsite"
            },
            {
                "ko": "에너지효율등급 인증으로 분양가 상승과 장기 운영비 절감 효과를 얻었습니다.",
                "vi": "Chứng nhận đẳng cấp hiệu suất năng lượng giúp tăng giá bán và tiết kiệm chi phí vận hành dài hạn.",
                "situation": "formal"
            }
        ],
        "relatedTerms": ["제로에너지건축", "LEED인증", "패시브하우스", "에너지진단"]
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

# 기존 데이터 로드
try:
    with open(file_path, "r", encoding="utf-8") as f:
        existing = json.load(f)
    print(f"✅ 기존 데이터 로드: {len(existing)}개")
except FileNotFoundError:
    existing = []
    print("⚠️ 기존 파일 없음. 새로 생성합니다.")

# 중복 체크 (slug 기준)
existing_slugs = {item["slug"] for item in existing}
new_items = [item for item in data if item["slug"] not in existing_slugs]

if not new_items:
    print("⚠️ 모든 용어가 이미 존재합니다.")
else:
    # 병합 및 저장
    merged = existing + new_items
    with open(file_path, "w", encoding="utf-8") as f:
        json.dump(merged, f, ensure_ascii=False, indent=2)
    print(f"✅ {len(new_items)}개 용어 추가 완료 (총 {len(merged)}개)")
    print(f"📂 저장 위치: {file_path}")

    # 추가된 용어 목록
    print("\n📋 추가된 용어:")
    for item in new_items:
        print(f"  - {item['korean']} ({item['slug']})")

print("\n⚠️ 실행 금지 - 스크립트만 생성됨")
