#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
건설 용어 추가 스크립트 - 상하수도/환경설비 (Water & Sewage)
테마: 정수장, 하수처리, 오수관, 우수관, 맨홀뚜껑, 물탱크, 급수관, 배수펌프, 오폐수처리, 중수도
Tier S 품질 기준 (90점 이상)
"""

import json
import os

# 추가할 용어 데이터 (10개)
data = [
    {
        "slug": "tram-xu-ly-nuoc-thai",
        "korean": "하수처리장",
        "vietnamese": "Trạm xử lý nước thải",
        "hanja": "下水處理場",
        "hanjaReading": "下(아래 하) + 水(물 수) + 處(곳 처) + 理(다스릴 리) + 場(마당 장)",
        "pronunciation": "짬 쓸리 느억 타이",
        "meaningKo": "생활하수나 산업폐수를 정화하여 방류하는 시설로, 베트남어로는 'Trạm xử lý nước thải'라고 합니다. 통역 시 주의할 점은 '정수장(Nhà máy nước sạch)'과 명확히 구분해야 하며, 처리 공정(xử lý sơ bộ/차처리, xử lý thứ cấp/2차처리, xử lý nâng cao/고도처리)을 정확히 이해해야 합니다. 베트남 현장에서는 'Nhà máy xử lý nước thải'로도 불리며, 규모에 따라 'trạm'(소규모)과 'nhà máy'(대규모)를 구분합니다.",
        "meaningVi": "Cơ sở xử lý nước thải sinh hoạt hoặc công nghiệp trước khi xả ra môi trường. Bao gồm các công đoạn xử lý sơ bộ, thứ cấp và nâng cao để loại bỏ chất ô nhiễm, đảm bảo tiêu chuẩn môi trường.",
        "context": "환경설비, 도시계획, 인프라 시공 현장",
        "culturalNote": "한국의 하수처리장은 악취 제거와 주변 환경 조화에 중점을 두며 지하화/공원화가 일반적이나, 베트남은 예산 제약으로 노천 시설이 많고 냄새 민원이 빈번합니다. 베트남 현장에서는 'BOD, COD, SS' 등 수질 지표를 영어 약자로 소통하며, 방류수 기준(QCVN 14:2008)이 한국보다 완화되어 있어 통역 시 기준치 차이를 명확히 전달해야 합니다.",
        "commonMistakes": [
            {
                "mistake": "정수장과 하수처리장을 혼동하여 'Nhà máy nước sạch'로 번역",
                "correction": "'Trạm xử lý nước thải' 또는 'Nhà máy xử lý nước thải'",
                "explanation": "정수장(Nhà máy nước sạch)은 먹는 물을 만드는 시설이고, 하수처리장은 오염된 물을 정화하는 시설이므로 완전히 다른 개념입니다."
            },
            {
                "mistake": "'하수처리'를 단순히 'xử lý nước'로 번역",
                "correction": "'xử lý nước thải' (폐수처리) 또는 'xử lý nước cống' (하수처리)",
                "explanation": "'nước thải'가 없으면 일반적인 물 처리로 오해될 수 있으며, 'nước cống'은 구체적으로 하수를 의미합니다."
            },
            {
                "mistake": "처리 단계를 'bước 1, bước 2'로 번역",
                "correction": "'xử lý sơ bộ (1차), xử lý thứ cấp (2차), xử lý nâng cao (고도)'",
                "explanation": "하수처리는 표준화된 단계 용어가 있으므로 공식 명칭을 사용해야 기술적 소통이 정확합니다."
            }
        ],
        "examples": [
            {
                "ko": "이 하수처리장은 일 처리용량 10만 톤 규모로 설계되었습니다.",
                "vi": "Trạm xử lý nước thải này được thiết kế với công suất 100.000 tấn/ngày.",
                "situation": "formal"
            },
            {
                "ko": "2차 처리 공정에서 생물학적 방법으로 유기물을 제거합니다.",
                "vi": "Trong công đoạn xử lý thứ cấp, sử dụng phương pháp sinh học để loại bỏ chất hữu cơ.",
                "situation": "onsite"
            },
            {
                "ko": "방류수 수질이 기준치를 초과하면 운영을 중단해야 합니다.",
                "vi": "Nếu chất lượng nước thải sau xử lý vượt tiêu chuẩn, phải dừng vận hành.",
                "situation": "formal"
            }
        ],
        "relatedTerms": ["정수장", "배수펌프", "오수관", "중수도", "폐수처리"]
    },
    {
        "slug": "ong-o-su",
        "korean": "오수관",
        "vietnamese": "Ống ô su (Ống nước thải)",
        "hanja": "汚水管",
        "hanjaReading": "汚(더러울 오) + 水(물 수) + 管(대롱 관)",
        "pronunciation": "옹 오 쑤 (옹 느억 타이)",
        "meaningKo": "생활하수나 오염된 물을 배출하는 관로로, 베트남어로는 'Ống ô su' 또는 'Ống nước thải'라고 합니다. 통역 시 중요한 점은 우수관(Ống thoát nước mưa)과 명확히 구분해야 하며, 합류식/분류식 하수도 시스템(hệ thống thoát nước hợp lưu/phân lưu)에 따라 용어가 달라집니다. 베트nam 현장에서는 재료에 따라 PVC, HDPE, 콘크리트관 등을 구분하여 지칭합니다.",
        "meaningVi": "Đường ống dẫn nước thải sinh hoạt và nước bẩn. Thường làm bằng PVC, HDPE hoặc bê tông, được chôn dưới đất với độ dốc nhất định để nước chảy tự nhiên về trạm xử lý.",
        "context": "상하수도 설계, 도로 매설 공사, 배관 시공",
        "culturalNote": "한국은 대부분 분류식 하수도(오수관/우수관 분리)를 채택하나, 베트남은 구도심에 합류식이 많아 우기 시 하수처리장 과부하가 빈번합니다. 베트남 현장에서는 관경을 'Ø300, Ø400'으로 표기하며, 한국식 'DN300'과 다르게 외경 기준입니다. 통역 시 관경 단위를 명확히 확인해야 오시공을 방지할 수 있습니다.",
        "commonMistakes": [
            {
                "mistake": "우수관과 오수관을 모두 'ống thoát nước'로 통칭",
                "correction": "오수관은 'ống ô su/nước thải', 우수관은 'ống thoát nước mưa'",
                "explanation": "베트남은 분류식 시스템에서 두 관을 엄격히 구분하므로 통역 시 혼동하면 시공 오류로 이어집니다."
            },
            {
                "mistake": "'오수'를 단순히 'nước bẩn'으로 번역",
                "correction": "'nước thải' (폐수) 또는 'nước ô nhiễm' (오염수)",
                "explanation": "'nước bẩn'은 구어체로 부정확하며, 'nước thải'가 공식 기술 용어입니다."
            },
            {
                "mistake": "관경을 'DN300'으로 그대로 전달",
                "correction": "'Ø300' 또는 'đường kính 300mm' (베트남 기준 확인 필수)",
                "explanation": "베트남은 외경 기준이므로 한국의 DN(공칭 지름)과 다를 수 있어 도면 기준을 명확히 해야 합니다."
            }
        ],
        "examples": [
            {
                "ko": "이 구역은 분류식 하수도로 오수관과 우수관을 별도로 매설합니다.",
                "vi": "Khu vực này áp dụng hệ thống thoát nước phân lưu, chôn riêng ống ô su và ống thoát nước mưa.",
                "situation": "formal"
            },
            {
                "ko": "오수관 접합부에 누수가 발생하여 보수가 필요합니다.",
                "vi": "Mối nối ống ô su bị rò rỉ, cần sửa chữa.",
                "situation": "onsite"
            },
            {
                "ko": "PVC 오수관 300mm를 100m 구간에 설치하세요.",
                "vi": "Lắp đặt ống ô su PVC Ø300mm cho đoạn 100m.",
                "situation": "onsite"
            }
        ],
        "relatedTerms": ["우수관", "맨홀", "배수펌프", "하수처리장", "배관"]
    },
    {
        "slug": "ong-thoat-nuoc-mua",
        "korean": "우수관",
        "vietnamese": "Ống thoát nước mưa",
        "hanja": "雨水管",
        "hanjaReading": "雨(비 우) + 水(물 수) + 管(대롱 관)",
        "pronunciation": "옹 토앗 느억 므어",
        "meaningKo": "빗물을 배수하는 관로로, 베트남어로는 'Ống thoát nước mưa'라고 합니다. 통역 시 오수관(Ống ô su)과 구분이 핵심이며, 베트남은 우기 집중호우로 우수관 용량 산정이 매우 중요합니다. 현장에서는 'cống thoát nước'(배수로)와도 연계되므로, 관과 개거(open channel)를 명확히 구분해야 합니다.",
        "meaningVi": "Đường ống dẫn nước mưa từ mái nhà, đường phố về sông, hồ hoặc hệ thống thoát nước. Thường có đường kính lớn hơn ống ô su do lưu lượng mưa lớn ở Việt Nam.",
        "context": "도로공사, 건물 외부 배수, 우수 배수 시스템",
        "culturalNote": "베트남은 우기(5~10월) 강우량이 연간의 80% 이상 집중되어 우수관 설계 시 한국보다 큰 관경과 여유율이 필요합니다. 호치민 등 저지대 도시는 침수가 빈번하여 우수펌프장(trạm bơm nước mưa)과 연계 설계가 필수입니다. 한국은 확률강우량 10년 빈도가 일반적이나, 베트남은 지역에 따라 20~50년 빈도를 적용하기도 합니다.",
        "commonMistakes": [
            {
                "mistake": "'우수관'을 'ống nước mưa'로만 번역",
                "correction": "'Ống thoát nước mưa' (배수 기능 강조)",
                "explanation": "'ống nước mưa'는 빗물 관이라는 뜻이지만, 'thoát'(배수)이 없으면 단순 저장관으로 오해될 수 있습니다."
            },
            {
                "mistake": "배수로(cống)와 우수관(ống)을 혼동",
                "correction": "지하 매설관은 'ống', 개거는 'cống' 또는 'rãnh thoát nước'",
                "explanation": "베트남 현장에서는 개거와 관로를 명확히 구분하므로 통역 시 주의해야 합니다."
            },
            {
                "mistake": "우수관 규격을 한국 기준으로만 전달",
                "correction": "베트남 강우 강도 반영 여부 확인 후 전달",
                "explanation": "베트남은 시간당 강우량이 100mm를 초과하는 경우가 많아 한국 기준을 그대로 적용하면 침수 위험이 있습니다."
            }
        ],
        "examples": [
            {
                "ko": "이 건물은 우수관을 통해 빗물을 지하 저류조로 보냅니다.",
                "vi": "Tòa nhà này dẫn nước mưa qua ống thoát nước mưa về bể chứa ngầm.",
                "situation": "formal"
            },
            {
                "ko": "우수관 막힘으로 침수가 발생했으니 긴급 준설하세요.",
                "vi": "Ống thoát nước mưa bị tắc gây ngập, cần nạo vét khẩn cấp.",
                "situation": "onsite"
            },
            {
                "ko": "우수관 600mm를 도로 양측에 매설 완료했습니다.",
                "vi": "Đã hoàn thành chôn ống thoát nước mưa Ø600mm hai bên đường.",
                "situation": "onsite"
            }
        ],
        "relatedTerms": ["오수관", "배수펌프", "맨홀", "빗물저류조", "침수방지"]
    },
    {
        "slug": "nap-cong",
        "korean": "맨홀뚜껑",
        "vietnamese": "Nắp cống",
        "hanja": None,
        "hanjaReading": None,
        "pronunciation": "넙 꽁",
        "meaningKo": "하수도나 전력/통신 케이블 점검구 상부를 덮는 뚜껑으로, 베트남어로는 'Nắp cống'이라고 합니다. 통역 시 주의할 점은 재질(gang/주철, composite/복합재, bê tông/콘크리트)과 하중 등급(A15~E600)을 정확히 전달해야 하며, 베트남 현장에서는 도난 방지(chống trộm)와 미끄럼 방지(chống trượt) 기능이 중요하게 다뤄집니다.",
        "meaningVi": "Nắp đậy hố ga, cống thoát nước hoặc hầm kỹ thuật. Thường làm bằng gang, composite hoặc bê tông, có các mức tải trọng khác nhau tùy vị trí lắp đặt (vỉa hè, đường xe, sân bay).",
        "context": "도로 시공, 상하수도 유지보수, 안전 점검",
        "culturalNote": "한국은 주철(gang) 맨홀뚜껑이 주류이나 도난이 빈번해지면서 잠금장치 부착이 일반화되었습니다. 베트남은 더욱 도난이 심각하여 복합재(composite) 또는 콘크리트 제품 사용이 증가하고 있으며, 현장에서는 'nắp cống chống trộm'(도난방지 맨홀뚜껑)을 명시적으로 요구합니다. 또한 베트남은 우기 시 맨홀 역류(tràn ngược)가 빈번하여 역류방지 기능이 중요합니다.",
        "commonMistakes": [
            {
                "mistake": "'맨홀'을 그대로 'manhole'로 발음하여 전달",
                "correction": "'Nắp cống' (뚜껑) 또는 'Hố ga' (맨홀 구조물)",
                "explanation": "베트남 현장에서는 'manhole'을 쓰지 않으며, nắp(뚜껑)과 hố(구멍)를 구분합니다."
            },
            {
                "mistake": "하중 등급을 'A15, B125' 등 유럽 기준만 전달",
                "correction": "베트남 기준(TCVN) 또는 현장 실제 사용 위치 설명 병행",
                "explanation": "베트남 시공자는 유럽 기준에 익숙하지 않으므로 '인도용/차도용' 등 구체적 설명이 필요합니다."
            },
            {
                "mistake": "'주철'을 단순히 'sắt'(철)로 번역",
                "correction": "'gang' (주철) 또는 'gang cầu' (구상흑연주철)",
                "explanation": "'sắt'는 일반 철이고, 'gang'이 주철의 정확한 베트남어입니다."
            }
        ],
        "examples": [
            {
                "ko": "이 도로는 하중 등급 D400 맨홀뚜껑을 사용합니다.",
                "vi": "Đường này sử dụng nắp cống cấp tải trọng D400.",
                "situation": "formal"
            },
            {
                "ko": "맨홀뚜껑이 파손되어 보행자 안전에 위험하니 즉시 교체하세요.",
                "vi": "Nắp cống bị hỏng, nguy hiểm cho người đi bộ, cần thay ngay.",
                "situation": "onsite"
            },
            {
                "ko": "도난 방지용 잠금장치가 있는 복합재 맨홀뚜껑으로 교체 완료했습니다.",
                "vi": "Đã hoàn thành thay nắp cống composite có khóa chống trộm.",
                "situation": "onsite"
            }
        ],
        "relatedTerms": ["맨홀", "하수관", "배수로", "점검구", "주철"]
    },
    {
        "slug": "bon-nuoc",
        "korean": "물탱크",
        "vietnamese": "Bồn nước",
        "hanja": None,
        "hanjaReading": None,
        "pronunciation": "본 느억",
        "meaningKo": "음용수나 소방용수를 저장하는 탱크로, 베트남어로는 'Bồn nước'라고 합니다. 통역 시 중요한 점은 용도별 구분(급수용/소방용/중수용)과 재질(inox/스테인리스, nhựa/플라스틱, bê tông/콘크리트)을 명확히 해야 하며, 베트남 현장에서는 위생 기준(QCVN 01:2009)과 내진 설계가 점점 중요해지고 있습니다.",
        "meaningVi": "Bể chứa nước sinh hoạt, nước cứu hỏa hoặc nước tái sử dụng. Có thể đặt trên cao (bồn nước trên cao) hoặc dưới đất (bể ngầm), làm bằng inox, nhựa hoặc bê tông cốt thép.",
        "context": "건물 급배수 설비, 소방 시설, 고층 빌딩",
        "culturalNote": "한국은 대부분 건물 옥상에 고가 탱크(bồn nước trên cao)를 설치하고 가압 급수하나, 베트남은 정전 빈도가 높아 중력식 급수를 병행합니다. 베트남 현장에서는 'bồn nước inox'(스테인리스 탱크)가 위생상 선호되며, 플라스틱 탱크는 열대 기후에서 조류 번식 위험이 있어 정기 청소가 필수입니다. 또한 호치민 등 연약지반 지역은 지하 탱크 부력(lực nổi) 계산이 중요합니다.",
        "commonMistakes": [
            {
                "mistake": "'물탱크'를 'bình nước'로 번역",
                "correction": "'Bồn nước' (큰 탱크) 또는 'Bể chứa nước' (저수조)",
                "explanation": "'bình nước'는 물병이나 작은 용기를 뜻하며, 건축 설비용 탱크는 'bồn' 또는 'bể'를 씁니다."
            },
            {
                "mistake": "급수 탱크와 소방 탱크를 구분 없이 'bồn nước'로만 지칭",
                "correction": "'bồn nước sinh hoạt' (급수용), 'bồn nước chữa cháy' (소방용)",
                "explanation": "소방법상 소방용수는 별도 용량과 유지 관리 기준이 있으므로 반드시 구분해야 합니다."
            },
            {
                "mistake": "탱크 용량을 'lít'(리터)로만 전달",
                "correction": "'m³' (세제곱미터) 또는 'tấn' (톤, 1m³≈1톤) 병행",
                "explanation": "베트남 현장에서는 큰 탱크는 'm³' 또는 'tấn'으로 표기하는 것이 일반적입니다."
            }
        ],
        "examples": [
            {
                "ko": "이 건물은 옥상에 50톤 급수 탱크를 설치합니다.",
                "vi": "Tòa nhà này lắp bồn nước sinh hoạt 50 tấn trên mái.",
                "situation": "formal"
            },
            {
                "ko": "물탱크 내부 청소를 분기마다 실시해야 합니다.",
                "vi": "Phải vệ sinh bên trong bồn nước mỗi quý.",
                "situation": "onsite"
            },
            {
                "ko": "지하 소방 탱크 200m³ 시공이 완료되었습니다.",
                "vi": "Đã hoàn thành thi công bể nước chữa cháy ngầm 200m³.",
                "situation": "onsite"
            }
        ],
        "relatedTerms": ["급수관", "배수펌프", "소방설비", "저수조", "고가탱크"]
    },
    {
        "slug": "ong-cap-nuoc",
        "korean": "급수관",
        "vietnamese": "Ống cấp nước",
        "hanja": "給水管",
        "hanjaReading": "給(줄 급) + 水(물 수) + 管(대롱 관)",
        "pronunciation": "옹 껍 느억",
        "meaningKo": "건물이나 시설에 물을 공급하는 관로로, 베트남어로는 'Ống cấp nước'라고 합니다. 통역 시 중요한 점은 배수관(ống thoát nước)과 명확히 구분하고, 재질(PPR, PVC, đồng/구리, inox)과 압력 등급(PN10, PN16)을 정확히 전달해야 합니다. 베트남 현장에서는 수질(chất lượng nước)과 수압(áp lực nước) 문제로 필터와 가압펌프가 자주 언급됩니다.",
        "meaningVi": "Đường ống dẫn nước sạch từ nguồn (máy bơm, bồn nước) đến điểm sử dụng. Thường làm bằng PPR, PVC, đồng hoặc inox, có các mức áp lực khác nhau (PN10, PN16, PN20).",
        "context": "건물 설비, 급배수 시공, 배관 공사",
        "culturalNote": "한국은 아파트 급수에 동관(ống đồng)이나 스테인리스관(ống inox)을 선호하나, 베트남은 경제성으로 PPR관(ống PPR)이 주류입니다. 베트남은 상수도 수질이 불안정하여 각 가정/건물에 필터(bộ lọc nước) 설치가 일반화되어 있으며, 고층 건물은 수압 부족으로 증압펌프(máy bơm tăng áp)가 필수입니다. 통역 시 관 색상 코드(파란색=냉수, 빨간색=온수)는 양국이 동일합니다.",
        "commonMistakes": [
            {
                "mistake": "'급수관'과 '배수관'을 모두 'ống nước'로 통칭",
                "correction": "급수관='ống cấp nước', 배수관='ống thoát nước'",
                "explanation": "cấp(공급)과 thoát(배출)의 차이를 명확히 해야 시공 오류를 방지할 수 있습니다."
            },
            {
                "mistake": "PPR관을 'ống nhựa'로만 번역",
                "correction": "'Ống PPR' (폴리프로필렌 랜덤 코폴리머)",
                "explanation": "'ống nhựa'는 모든 플라스틱 관을 뜻하므로, PPR은 고유명사로 써야 합니다."
            },
            {
                "mistake": "압력 등급 'PN16'을 설명 없이 전달",
                "correction": "'PN16 (chịu áp lực 16 bar)' 또는 '16 kg/cm²'",
                "explanation": "베트남 시공자는 PN 표기에 익숙하지 않을 수 있으므로 구체적 압력 값을 병기하면 좋습니다."
            }
        ],
        "examples": [
            {
                "ko": "이 건물은 급수관으로 PPR PN16 관을 사용합니다.",
                "vi": "Tòa nhà này dùng ống cấp nước PPR PN16.",
                "situation": "formal"
            },
            {
                "ko": "급수관 접합부에서 누수가 발생하니 즉시 수리하세요.",
                "vi": "Mối nối ống cấp nước bị rò rỉ, sửa ngay.",
                "situation": "onsite"
            },
            {
                "ko": "고층부 급수를 위해 증압펌프를 5층마다 설치합니다.",
                "vi": "Lắp máy bơm tăng áp mỗi 5 tầng để cấp nước tầng cao.",
                "situation": "formal"
            }
        ],
        "relatedTerms": ["배수관", "물탱크", "배수펌프", "수압", "PPR관"]
    },
    {
        "slug": "may-bom-nuoc",
        "korean": "배수펌프",
        "vietnamese": "Máy bơm nước",
        "hanja": "排水pump",
        "hanjaReading": "排(물리칠 배) + 水(물 수) + pump(펌프)",
        "pronunciation": "마이 범 느억",
        "meaningKo": "물을 배출하거나 이송하는 펌프로, 베트남어로는 'Máy bơm nước'라고 합니다. 통역 시 중요한 점은 용도별 구분(배수용/급수용/오수용)과 형식(원심/수중/터빈)을 명확히 해야 하며, 베트남 현장에서는 양정(cột áp/H), 유량(lưu lượng/Q), 동력(công suất)을 반드시 확인합니다. 또한 정전 시 자동 작동을 위한 발전기 연계가 자주 요구됩니다.",
        "meaningVi": "Thiết bị bơm nước phục vụ cấp nước, thoát nước hoặc xử lý nước thải. Có nhiều loại: bơm ly tâm, bơm chìm, bơm tăng áp, với các thông số quan trọng như cột áp (H), lưu lượng (Q), công suất (kW).",
        "context": "건물 설비, 하수처리장, 빌딩 급수 시스템",
        "culturalNote": "베트남은 정전 빈도가 높아 배수펌프는 자동 절체 기능(chuyển đổi tự động)과 발전기 백업이 중요합니다. 한국은 펌프실(phòng bơm)을 지하에 두는 것이 일반적이나, 베트남은 침수 위험으로 1층 이상 설치를 권장합니다. 또한 베트남 현장에서는 펌프 브랜드(Pentax, Ebara 등)를 중요시하며, 중국산 저가 펌프는 내구성 문제로 기피됩니다.",
        "commonMistakes": [
            {
                "mistake": "'배수펌프'를 단순히 'máy bơm'으로만 번역",
                "correction": "'Máy bơm nước' (물펌프) 또는 용도별 'máy bơm thoát nước' (배수펌프)",
                "explanation": "'máy bơm'만으로는 공기/오일 펌프 등과 구분이 안 되므로 'nước'를 명시해야 합니다."
            },
            {
                "mistake": "양정을 'độ cao'로 번역",
                "correction": "'Cột áp' (수두) 또는 'chiều cao bơm' (양정)",
                "explanation": "'độ cao'는 단순 높이고, 'cột áp'이 펌프 성능 지표인 양정의 정확한 용어입니다."
            },
            {
                "mistake": "펌프 용량을 'kW'로만 전달",
                "correction": "'công suất [X] kW, lưu lượng [Y] m³/h, cột áp [Z] m' 세트로 전달",
                "explanation": "베트남 현장에서는 동력뿐 아니라 유량과 양정을 함께 확인해야 적합한 펌프를 선정할 수 있습니다."
            }
        ],
        "examples": [
            {
                "ko": "지하 배수펌프 2대를 교대 운전 방식으로 설치합니다.",
                "vi": "Lắp 2 máy bơm thoát nước ngầm vận hành luân phiên.",
                "situation": "formal"
            },
            {
                "ko": "펌프가 과부하로 정지했으니 모터를 점검하세요.",
                "vi": "Máy bơm dừng do quá tải, kiểm tra động cơ.",
                "situation": "onsite"
            },
            {
                "ko": "이 펌프는 유량 50m³/h, 양정 20m, 동력 7.5kW입니다.",
                "vi": "Máy bơm này có lưu lượng 50m³/h, cột áp 20m, công suất 7,5kW.",
                "situation": "formal"
            }
        ],
        "relatedTerms": ["급수관", "물탱크", "하수처리장", "양정", "수중펌프"]
    },
    {
        "slug": "xu-ly-nuoc-thai",
        "korean": "오폐수처리",
        "vietnamese": "Xử lý nước thải",
        "hanja": "汚廢水處理",
        "hanjaReading": "汚(더러울 오) + 廢(버릴 폐) + 水(물 수) + 處(곳 처) + 理(다스릴 리)",
        "pronunciation": "쓸리 느억 타이",
        "meaningKo": "생활하수나 산업폐수를 정화하여 방류 기준에 맞게 처리하는 공정으로, 베트남어로는 'Xử lý nước thải'라고 합니다. 통역 시 중요한 점은 처리 방식(물리적/화학적/생물학적)과 방류 기준(QCVN 14:2008 등)을 정확히 이해해야 하며, 베트남 현장에서는 BOD, COD, SS 등 수질 지표를 영어 약자로 소통합니다.",
        "meaningVi": "Quá trình làm sạch nước thải sinh hoạt hoặc công nghiệp thông qua các phương pháp vật lý, hóa học và sinh học, đảm bảo đạt tiêu chuẩn xả thải theo quy định (QCVN 14:2008, QCVN 40:2011).",
        "context": "환경설비, 공장 폐수처리, 건물 오수처리",
        "culturalNote": "베트남의 폐수 방류 기준은 한국보다 완화되어 있으나, 외국 투자 기업에는 본국 기준 적용을 요구하는 경우가 많아 통역 시 기준 혼동 주의가 필요합니다. 베트남은 환경 단속이 강화되면서 불시 점검(kiểm tra đột xuất)과 과태료(phạt)가 증가하고 있으며, 처리 시설 고장 시에도 방류 중단 없이 우회 방류하는 사례가 있어 환경법 위반 위험이 큽니다.",
        "commonMistakes": [
            {
                "mistake": "'오폐수'를 'nước bẩn'으로 번역",
                "correction": "'Nước thải' (폐수) 또는 'nước ô nhiễm' (오염수)",
                "explanation": "'nước bẩn'은 구어체로 기술 문서나 공식 소통에서는 부적절합니다."
            },
            {
                "mistake": "BOD, COD를 베트남어로 번역 시도",
                "correction": "영어 약자 그대로 'BOD, COD, SS' 사용",
                "explanation": "베트남 현장에서는 수질 지표를 영어 약자로 쓰며, 번역하면 오히려 혼란을 줍니다."
            },
            {
                "mistake": "처리 단계를 '1차, 2차, 3차'로만 번역",
                "correction": "'xử lý sơ bộ, xử lý thứ cấp, xử lý nâng cao'",
                "explanation": "베트남에서는 각 단계를 고유 용어로 부르므로 숫자만으로는 정확한 의미 전달이 어렵습니다."
            }
        ],
        "examples": [
            {
                "ko": "이 공장은 하루 500m³의 산업폐수를 처리합니다.",
                "vi": "Nhà máy này xử lý 500m³ nước thải công nghiệp mỗi ngày.",
                "situation": "formal"
            },
            {
                "ko": "방류수 BOD가 기준치를 초과하여 환경청에 보고해야 합니다.",
                "vi": "BOD nước thải sau xử lý vượt tiêu chuẩn, phải báo cáo Sở Tài nguyên Môi trường.",
                "situation": "formal"
            },
            {
                "ko": "생물학적 처리 공정에서 미생물 농도가 부족하니 슬러지를 추가하세요.",
                "vi": "Trong công đoạn xử lý sinh học, nồng độ vi sinh vật thấp, cần bổ sung bùn hoạt tính.",
                "situation": "onsite"
            }
        ],
        "relatedTerms": ["하수처리장", "배수펌프", "정수장", "중수도", "방류수"]
    },
    {
        "slug": "he-thong-nuoc-trung-thuy",
        "korean": "중수도",
        "vietnamese": "Hệ thống nước trung thủy (Nước tái sử dụng)",
        "hanja": "中水道",
        "hanjaReading": "中(가운데 중) + 水(물 수) + 道(길 도)",
        "pronunciation": "헤 통 느억 쭝 투이",
        "meaningKo": "생활하수를 처리하여 화장실 용수, 조경용수 등 비음용 목적으로 재사용하는 시스템으로, 베트남어로는 'Hệ thống nước trung thủy' 또는 'Nước tái sử dụng'라고 합니다. 통역 시 중요한 점은 중수도는 먹을 수 없다는 점(không uống được)과 용도 제한(toilet, tưới cây/조경, làm mát/냉각)을 명확히 해야 하며, 베트남은 아직 중수도 개념이 생소하여 설명이 필요합니다.",
        "meaningVi": "Hệ thống xử lý và tái sử dụng nước thải sinh hoạt đã qua xử lý cho các mục đích không uống như xả toilet, tưới cây, làm mát, giúp tiết kiệm nước sạch và bảo vệ môi trường.",
        "context": "친환경 건축, 고급 빌딩, 수자원 절약",
        "culturalNote": "한국은 대형 건물에 중수도 설치가 법적으로 의무화된 경우가 많으나, 베트남은 아직 법규가 미비하고 인식도 낮아 고급 빌딩이나 친환경 프로젝트에만 제한적으로 적용됩니다. 베트남 현장에서는 'nước tái chế'(재활용수)로도 불리며, 상수도 요금(tiền nước sạch)이 저렴하여 경제적 동기가 약한 편입니다. 통역 시 중수도 도입의 환경적 가치를 강조하는 것이 효과적입니다.",
        "commonMistakes": [
            {
                "mistake": "'중수도'를 단순히 'nước tái chế'로만 번역",
                "correction": "'Hệ thống nước trung thủy' 또는 'Nước tái sử dụng (không uống được)' (음용 불가 명시)",
                "explanation": "'nước tái chế'는 일반적인 재활용수이고, 중수도는 특정 용도의 시스템이므로 구분이 필요합니다."
            },
            {
                "mistake": "중수도를 정수(nước sạch)와 혼동",
                "correction": "중수='nước trung thủy' (비음용), 정수='nước sạch' (음용 가능)",
                "explanation": "중수도는 절대 마실 수 없으므로 혼동 시 심각한 건강 문제가 발생할 수 있습니다."
            },
            {
                "mistake": "중수도 용도를 제한 없이 설명",
                "correction": "'Chỉ dùng cho xả toilet, tưới cây, làm mát - KHÔNG uống'",
                "explanation": "베트남에서는 중수도 개념이 생소하여 용도를 명확히 제한하지 않으면 오용 위험이 있습니다."
            }
        ],
        "examples": [
            {
                "ko": "이 빌딩은 중수도 시스템으로 하루 50톤의 물을 절약합니다.",
                "vi": "Tòa nhà này tiết kiệm 50 tấn nước mỗi ngày nhờ hệ thống nước trung thủy.",
                "situation": "formal"
            },
            {
                "ko": "중수도는 화장실과 조경용으로만 사용하며 절대 마시면 안 됩니다.",
                "vi": "Nước trung thủy chỉ dùng cho toilet và tưới cây, KHÔNG được uống.",
                "situation": "onsite"
            },
            {
                "ko": "중수 처리 시설에서 필터 교체 작업을 진행합니다.",
                "vi": "Tiến hành thay bộ lọc tại hệ thống xử lý nước tái sử dụng.",
                "situation": "onsite"
            }
        ],
        "relatedTerms": ["하수처리", "물탱크", "급수관", "정수장", "재활용수"]
    },
    {
        "slug": "nha-may-nuoc-sach",
        "korean": "정수장",
        "vietnamese": "Nhà máy nước sạch",
        "hanja": "淨水場",
        "hanjaReading": "淨(깨끗할 정) + 水(물 수) + 場(마당 장)",
        "pronunciation": "냐 마이 느억 삭",
        "meaningKo": "강물이나 지하수를 정화하여 먹는 물로 공급하는 시설로, 베트남어로는 'Nhà máy nước sạch'라고 합니다. 통역 시 가장 중요한 점은 하수처리장(Trạm xử lý nước thải)과 절대 혼동하지 않는 것이며, 정수 공정(lắng, lọc, khử trùng/침전, 여과, 살균)을 정확히 이해해야 합니다. 베트남 현장에서는 수질 기준(QCVN 01:2009)과 염소 농도(nồng độ clo)가 자주 언급됩니다.",
        "meaningVi": "Nhà máy xử lý nước thô từ sông, hồ hoặc nước ngầm thành nước sạch đạt tiêu chuẩn sinh hoạt, qua các công đoạn lắng, lọc và khử trùng. Cung cấp nước sạch cho dân cư và doanh nghiệp.",
        "context": "상수도 인프라, 도시 개발, 환경 시설",
        "culturalNote": "베트남의 정수장 기술은 지역별 격차가 커서, 하노이/호치민은 현대화되어 있으나 지방은 노후 시설이 많고 수질 신뢰도가 낮아 가정용 정수기(máy lọc nước) 보급률이 매우 높습니다. 한국과 달리 베트남은 수돗물을 바로 마시지 않고 끓이거나 정수기를 거치는 것이 일반적입니다. 통역 시 '먹는 물'(nước uống)과 '수돗물'(nước máy)을 구분하면 오해를 줄일 수 있습니다.",
        "commonMistakes": [
            {
                "mistake": "정수장과 하수처리장을 혼동하여 'Trạm xử lý nước'로 통칭",
                "correction": "정수장='Nhà máy nước sạch', 하수처리장='Trạm xử lý nước thải'",
                "explanation": "정수장은 깨끗한 물을 만들고, 하수처리장은 더러운 물을 정화하는 전혀 다른 시설입니다."
            },
            {
                "mistake": "'정수'를 'nước lọc'로만 번역",
                "correction": "'Nước sạch' (깨끗한 물) 또는 'nước máy đạt tiêu chuẩn' (기준 충족 수돗물)",
                "explanation": "'nước lọc'는 여과수 일반이고, 정수장의 산출물은 'nước sạch'가 공식 용어입니다."
            },
            {
                "mistake": "염소 소독을 'sát trùng bằng thuốc'로 애매하게 번역",
                "correction": "'Khử trùng bằng clo' (염소 소독)",
                "explanation": "정수장에서는 염소(clo)를 사용하므로 구체적으로 명시해야 합니다."
            }
        ],
        "examples": [
            {
                "ko": "이 정수장은 하루 20만 톤의 정수를 생산합니다.",
                "vi": "Nhà máy nước sạch này sản xuất 200.000 tấn nước sạch mỗi ngày.",
                "situation": "formal"
            },
            {
                "ko": "정수장 여과지에서 모래 교체 작업을 실시합니다.",
                "vi": "Tiến hành thay cát tại bể lọc của nhà máy nước sạch.",
                "situation": "onsite"
            },
            {
                "ko": "수질 검사 결과 염소 농도가 기준치 이하입니다.",
                "vi": "Kết quả kiểm tra cho thấy nồng độ clo dưới tiêu chuẩn.",
                "situation": "formal"
            }
        ],
        "relatedTerms": ["하수처리장", "물탱크", "급수관", "중수도", "수질검사"]
    }
]

# 저장 경로
base_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
target_file = os.path.join(base_dir, "data", "terms", "construction.json")

# 기존 파일 읽기
with open(target_file, "r", encoding="utf-8") as f:
    existing_data = json.load(f)

print(f"기존 용어 수: {len(existing_data)}")

# 새 용어 추가
existing_data.extend(data)

print(f"추가 후 용어 수: {len(existing_data)}")

# 저장
with open(target_file, "w", encoding="utf-8") as f:
    json.dump(existing_data, f, ensure_ascii=False, indent=2)

print(f"✅ 완료: {len(data)}개 용어 추가됨 → {target_file}")
