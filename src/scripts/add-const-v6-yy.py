#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
건설(Construction) 용어 추가 스크립트 v6-yy
테마: 시운전/하자/유지보수
- 시운전, TAB, 커미셔닝, 하자점검, 누수, 곰팡이, 결로, 크랙보수, 실란트교체, 유지보수계획
"""

import json
import os

# 추가할 용어 데이터 (10개)
data = [
    {
        "slug": "chay-thu",
        "domain": "construction",
        "korean": "시운전",
        "vietnamese": "Chạy thử",
        "hanja": "試運轉",
        "hanjaReading": "試(시험할 시) + 運(운전할 운) + 轉(구를 전)",
        "pronunciation": "짜이 투",
        "meaningKo": "건축물이나 설비의 완공 후 정상 작동 여부를 확인하기 위해 실제 가동해보는 과정입니다. 통역 시 'commissioning'과 혼동하지 않도록 주의하세요. 'chạy thử'는 단순 테스트 가동이고, 'commissioning'은 성능 검증을 포함한 포괄적 개념입니다. 베트남 현장에서는 '짜이 투 헤 통'(hệ thống, 시스템 시운전)처럼 설비명을 함께 명시하는 것이 일반적입니다.",
        "meaningVi": "Quá trình vận hành thử nghiệm công trình hoặc thiết bị sau khi hoàn thành để kiểm tra hoạt động bình thường. Thường thực hiện trước khi bàn giao công trình, bao gồm chạy thử từng hệ thống (điện, nước, HVAC) để phát hiện sai sót.",
        "context": "준공, 설비, 검수",
        "culturalNote": "한국에서는 시운전을 준공 검사 전 필수 절차로 보는 반면, 베트남에서는 하자보증기간 중 점진적으로 문제를 발견하고 수정하는 경우가 많습니다. 한국 발주처는 시운전 기간을 길게(1~3개월) 요구하지만, 베트남에서는 짧은 테스트(1~2주)로 진행하는 경우가 흔합니다. 통역 시 'thời gian chạy thử'(시운전 기간) 조율이 중요한 쟁점이 됩니다.",
        "commonMistakes": [
            {
                "mistake": "chạy thử를 kiểm tra(검사)로 오역",
                "correction": "시운전은 '가동'이고 검사는 '확인'",
                "explanation": "chạy thử는 actual operation test, kiểm tra는 inspection만 의미"
            },
            {
                "mistake": "commissioning과 구분 없이 통역",
                "correction": "commissioning은 'vận hành thử nghiệm và chứng nhận'",
                "explanation": "시운전은 테스트, 커미셔닝은 성능 검증+인증 포함"
            },
            {
                "mistake": "'시운전 완료'를 'hoàn thành chạy thử'만으로 통역",
                "correction": "'đã hoàn thành chạy thử và xác nhận hoạt động ổn định'",
                "explanation": "완료는 단순 종료가 아니라 정상 작동 확인을 의미"
            }
        ],
        "examples": [
            {
                "ko": "HVAC 시스템 시운전을 3주간 실시합니다",
                "vi": "Tiến hành chạy thử hệ thống HVAC trong 3 tuần",
                "situation": "formal"
            },
            {
                "ko": "시운전 중 냉각수 누수가 발견됐어요",
                "vi": "Phát hiện rò rỉ nước làm mát trong quá trình chạy thử",
                "situation": "onsite"
            },
            {
                "ko": "시운전 완료 후 성능 보고서를 제출하겠습니다",
                "vi": "Sau khi hoàn thành chạy thử sẽ nộp báo cáo hiệu suất",
                "situation": "formal"
            }
        ],
        "relatedTerms": [
            "commissioning",
            "준공검사",
            "성능시험",
            "하자점검"
        ]
    },
    {
        "slug": "tab-can-bang-khong-khi",
        "domain": "construction",
        "korean": "TAB (공조설비 시험 및 조정)",
        "vietnamese": "TAB (Testing, Adjusting and Balancing)",
        "hanja": None,
        "hanjaReading": None,
        "pronunciation": "티-에이-비, 깐 방 콩 키",
        "meaningKo": "공조(HVAC) 시스템의 공기 유량, 수량, 압력 등을 측정하고 설계값에 맞게 조정하는 작업입니다. 통역 시 '테이비'로 발음하지 말고 'Testing, Adjusting, Balancing'의 풀네임을 최소 1회 언급한 후 약어를 사용하세요. 베트nam에서는 'cân bằng không khí'(공기 균형)로만 번역하면 범위가 축소되므로 반드시 풀네임을 병기해야 합니다. 한국에서는 TAB 전문업체가 독립적으로 수행하지만, 베트남에서는 설비 시공사가 자체적으로 진행하는 경우가 많아 품질 차이가 발생합니다.",
        "meaningVi": "Công tác đo lường, điều chỉnh và cân bằng các thông số như lưu lượng gió, nước, áp suất trong hệ thống HVAC để đảm bảo hoạt động đúng thiết kế. Đây là công việc chuyên môn cao, thường do đơn vị độc lập thực hiện.",
        "context": "공조, 설비, 성능",
        "culturalNote": "한국에서는 TAB를 준공 필수 조건으로 보고 공인 보고서를 요구하지만, 베트남에서는 선택적 서비스로 인식되는 경우가 많습니다. 한국 발주처는 TAB 비용을 별도 책정하지만, 베트남 현지 업체는 설비 공사비에 포함된 것으로 이해하는 경우가 있어 분쟁의 소지가 있습니다. 통역 시 'báo cáo TAB chính thức'(공식 TAB 보고서)인지 확인이 필요합니다.",
        "commonMistakes": [
            {
                "mistake": "TAB를 '공기 균형'만으로 통역",
                "correction": "'kiểm tra, điều chỉnh và cân bằng hệ thống HVAC'",
                "explanation": "공기뿐 아니라 물, 압력 등 전체 시스템 포함"
            },
            {
                "mistake": "'TAB 완료'를 '측정 완료'로 오역",
                "correction": "'hoàn thành TAB với các giá trị đạt thiết kế'",
                "explanation": "측정뿐 아니라 조정+검증까지 포함"
            },
            {
                "mistake": "TAB와 commissioning을 같은 것으로 통역",
                "correction": "TAB는 commissioning의 일부",
                "explanation": "commissioning은 전체 성능 검증, TAB는 공조 특화"
            }
        ],
        "examples": [
            {
                "ko": "TAB 보고서 제출 후 준공검사를 받겠습니다",
                "vi": "Sau khi nộp báo cáo TAB sẽ tiến hành nghiệm thu hoàn công",
                "situation": "formal"
            },
            {
                "ko": "TAB 작업 중 덕트 누기가 심해서 보완이 필요합니다",
                "vi": "Trong quá trình TAB phát hiện rò rỉ ống gió nghiêm trọng cần khắc phục",
                "situation": "onsite"
            },
            {
                "ko": "각 층별 풍량 측정 및 조정을 완료했습니다",
                "vi": "Đã hoàn thành đo và điều chỉnh lưu lượng gió từng tầng",
                "situation": "formal"
            }
        ],
        "relatedTerms": [
            "commissioning",
            "덕트",
            "풍량",
            "HVAC"
        ]
    },
    {
        "slug": "commissioning",
        "domain": "construction",
        "korean": "커미셔닝",
        "vietnamese": "Commissioning (vận hành thử nghiệm và chứng nhận)",
        "hanja": None,
        "hanjaReading": None,
        "pronunciation": "커-미-셔-닝, 번 한 투 응험 바 쯩 녠",
        "meaningKo": "건축물의 모든 시스템과 설비가 설계 의도대로 작동하는지 종합적으로 검증하고 인증하는 프로세스입니다. 단순 시운전(chạy thử)과 달리 성능 기준 충족, 운영 매뉴얼, 교육까지 포함하는 포괄적 개념입니다. 통역 시 '커미셔닝'을 베트남어로 단순 번역하지 말고 영문 원어를 유지하면서 'vận hành thử nghiệm và chứng nhận'으로 설명을 덧붙이는 것이 정확합니다. LEED 인증 프로젝트에서는 필수 절차이지만, 베트남 일반 현장에서는 생소한 개념이므로 범위를 명확히 설명해야 합니다.",
        "meaningVi": "Quy trình kiểm tra và xác nhận toàn diện rằng tất cả hệ thống và thiết bị trong công trình hoạt động đúng với ý đồ thiết kế, bao gồm kiểm tra hiệu suất, đào tạo vận hành và bàn giao tài liệu. Đây là tiêu chuẩn bắt buộc trong các dự án LEED.",
        "context": "준공, 성능, LEED",
        "culturalNote": "한국에서는 주요 프로젝트에서 commissioning agent를 별도로 고용하지만, 베트남에서는 감리사가 겸임하는 경우가 많습니다. 한국 발주처는 commissioning 보고서를 준공 필수 서류로 요구하지만, 베트남 현지 인허가에서는 요구하지 않는 경우가 대부분입니다. 통역 시 'dịch vụ commissioning độc lập'(독립 커미셔닝 서비스)인지 감리 포함인지 확인이 필요합니다.",
        "commonMistakes": [
            {
                "mistake": "commissioning을 '시운전'으로만 통역",
                "correction": "'quy trình commissioning bao gồm kiểm tra, xác nhận và đào tạo'",
                "explanation": "시운전보다 훨씬 넓은 범위의 검증 프로세스"
            },
            {
                "mistake": "'commissioning agent'를 '시운전 담당자'로 통역",
                "correction": "'chuyên gia commissioning độc lập'",
                "explanation": "전문 자격을 가진 독립적인 제3자 검증 전문가"
            },
            {
                "mistake": "commissioning과 준공검사를 동일시",
                "correction": "commissioning은 준공검사 전 선행 절차",
                "explanation": "준공검사는 법적 절차, commissioning은 기술 검증"
            }
        ],
        "examples": [
            {
                "ko": "LEED 인증을 위해 commissioning이 필수입니다",
                "vi": "Commissioning là bắt buộc để được chứng nhận LEED",
                "situation": "formal"
            },
            {
                "ko": "커미셔닝 에이전트가 성능 미달을 지적했습니다",
                "vi": "Chuyên gia commissioning đã chỉ ra hiệu suất không đạt yêu cầu",
                "situation": "onsite"
            },
            {
                "ko": "커미셔닝 보고서를 제출하고 운영팀 교육을 완료했습니다",
                "vi": "Đã nộp báo cáo commissioning và hoàn thành đào tạo đội vận hành",
                "situation": "formal"
            }
        ],
        "relatedTerms": [
            "시운전",
            "TAB",
            "준공검사",
            "LEED"
        ]
    },
    {
        "slug": "kiem-tra-khiem-khuyet",
        "domain": "construction",
        "korean": "하자점검",
        "vietnamese": "Kiểm tra khiếm khuyết",
        "hanja": "瑕疵點檢",
        "hanjaReading": "瑕(옥에 티 하) + 疵(흠 자) + 點(점 점) + 檢(검사할 검)",
        "pronunciation": "끼엠 짜 킴 쿠엣",
        "meaningKo": "공사 완료 후 발생한 결함이나 하자를 확인하고 목록화하는 작업입니다. 통역 시 '하자'는 'khiếm khuyết'(결함), 'lỗi thi công'(시공 오류), 'sai sót'(실수) 등으로 표현할 수 있지만, 법적 책임이 따르는 공식 문서에서는 'khiếm khuyết'이 가장 정확합니다. 베트남에서는 '프엉 깐'(phòng không, 빈 방)이라는 구어로 입주 전 점검을 지칭하기도 합니다. 한국처럼 체계적인 하자점검 프로세스가 정착되지 않은 경우가 많아, 점검 기준과 보수 기한을 명확히 합의하는 것이 중요합니다.",
        "meaningVi": "Công tác kiểm tra và lập danh sách các khiếm khuyết, lỗi thi công sau khi hoàn thành công trình. Thường thực hiện trước bàn giao và trong thời gian bảo hành để đảm bảo chất lượng công trình.",
        "context": "준공, 하자보수, 품질",
        "culturalNote": "한국에서는 하자점검을 시행사-시공사-감리가 공동으로 진행하며 상세한 목록을 작성하지만, 베트남에서는 발주처가 단독으로 점검하고 구두로 지적하는 경우가 많습니다. 한국의 하자보증기간(1~10년)에 비해 베트남은 통상 1~2년으로 짧고, 하자 범위 해석도 느슨합니다. 통역 시 'danh sách punch list'(펀치 리스트)라는 용어를 함께 사용하면 이해가 빠릅니다.",
        "commonMistakes": [
            {
                "mistake": "하자를 'lỗi'(에러)로만 통역",
                "correction": "'khiếm khuyết thi công' 또는 'hư hỏng'",
                "explanation": "lỗi는 단순 실수, 하자는 구조적/기능적 결함 포함"
            },
            {
                "mistake": "'하자점검'을 'kiểm tra lỗi'로 통역",
                "correction": "'kiểm tra và lập danh sách khiếm khuyết'",
                "explanation": "점검은 단순 확인이 아니라 목록화까지 포함"
            },
            {
                "mistake": "punch list를 '펀치 리스트'로만 발음",
                "correction": "'danh sách khiếm khuyết cần khắc phục (punch list)'",
                "explanation": "베트남어 설명 없이 영어만 쓰면 이해 어려움"
            }
        ],
        "examples": [
            {
                "ko": "입주 전 하자점검을 실시하겠습니다",
                "vi": "Sẽ tiến hành kiểm tra khiếm khuyết trước khi bàn giao",
                "situation": "formal"
            },
            {
                "ko": "하자 목록 120건 중 80건 보수 완료했어요",
                "vi": "Đã khắc phục 80/120 khiếm khuyết trong danh sách",
                "situation": "onsite"
            },
            {
                "ko": "하자점검 결과를 보고서로 제출하겠습니다",
                "vi": "Sẽ nộp báo cáo kết quả kiểm tra khiếm khuyết",
                "situation": "formal"
            }
        ],
        "relatedTerms": [
            "하자보수",
            "준공검사",
            "입주점검",
            "AS"
        ]
    },
    {
        "slug": "ro-ri-nuoc",
        "domain": "construction",
        "korean": "누수",
        "vietnamese": "Rò rỉ nước",
        "hanja": "漏水",
        "hanjaReading": "漏(샐 루) + 水(물 수)",
        "pronunciation": "조 지 느억",
        "meaningKo": "배관, 지붕, 외벽 등에서 물이 새는 현상입니다. 통역 시 '누수'는 'rò rỉ nước'가 가장 일반적이지만, 심각도에 따라 'thấm nước'(스며듦), 'dột nước'(지붕 누수), 'chảy nước'(물이 흐름) 등으로 구분해서 표현해야 정확합니다. 베트남 건설 현장에서 가장 빈번한 하자 중 하나이며, 우기(5~10월)에 특히 많이 발생합니다. 한국에서는 누수를 중대 하자로 보지만, 베트남에서는 보수 긴급성이 낮게 인식되는 경우가 있어 통역 시 심각성을 강조해야 합니다.",
        "meaningVi": "Hiện tượng nước rò rỉ, thấm qua đường ống, mái nhà, tường ngoài. Đây là khiếm khuyết phổ biến nhất trong xây dựng, đặc biệt nghiêm trọng trong mùa mưa và cần xử lý ngay để tránh hư hỏng kết cấu.",
        "context": "하자, 방수, 보수",
        "culturalNote": "한국에서는 누수 발생 시 즉시 원인 파악 및 전면 보수를 진행하지만, 베트남에서는 임시 방편(실리콘 주입)으로 처리하고 재발 시 재보수하는 관행이 있습니다. 한국은 누수를 시공사 책임으로 보지만, 베트남에서는 사용자 관리 소홀로 책임을 전가하는 경우도 있습니다. 통역 시 'rò rỉ do lỗi thi công'(시공 오류로 인한 누수)인지 명확히 해야 합니다.",
        "commonMistakes": [
            {
                "mistake": "모든 누수를 'rò rỉ'로만 통역",
                "correction": "지붕은 'dột', 스며듦은 'thấm', 흐름은 'chảy'",
                "explanation": "누수 유형과 심각도에 따라 다른 용어 사용"
            },
            {
                "mistake": "'누수 원인'을 'lý do rò rỉ'로 통역",
                "correction": "'nguyên nhân rò rỉ'",
                "explanation": "lý do는 이유, nguyên nhân은 원인(기술적)"
            },
            {
                "mistake": "'누수 보수'를 'sửa rò rỉ'로만 통역",
                "correction": "'khắc phục rò rỉ và chống thấm lại'",
                "explanation": "보수는 단순 수리가 아니라 재방수 포함"
            }
        ],
        "examples": [
            {
                "ko": "지하주차장 천장에서 누수가 발생했습니다",
                "vi": "Phát hiện rò rỉ nước tại trần tầng hầm để xe",
                "situation": "formal"
            },
            {
                "ko": "누수 원인은 방수층 시공 불량입니다",
                "vi": "Nguyên nhân rò rỉ là thi công lớp chống thấm kém chất lượng",
                "situation": "onsite"
            },
            {
                "ko": "우기 전에 누수 보수를 완료해야 합니다",
                "vi": "Phải hoàn thành khắc phục rò rỉ trước mùa mưa",
                "situation": "formal"
            }
        ],
        "relatedTerms": [
            "방수",
            "하자보수",
            "균열",
            "결로"
        ]
    },
    {
        "slug": "moc-nam",
        "domain": "construction",
        "korean": "곰팡이",
        "vietnamese": "Mốc, nấm",
        "hanja": None,
        "hanjaReading": None,
        "pronunciation": "목, 넘",
        "meaningKo": "습기가 많은 환경에서 발생하는 미생물로, 벽체, 천장, 욕실 등에 검은 반점이나 얼룩으로 나타납니다. 통역 시 'mốc'은 곰팡이 일반을 지칭하고, 'nấm'은 균류를 의미하는데, 건설 현장에서는 보통 'mốc'을 씁니다. 베트남의 고온다습한 기후 특성상 한국보다 곰팡이 발생이 훨씬 빈번하며, 방치 시 구조체까지 손상시킬 수 있습니다. 통역 시 곰팡이를 단순 미관 문제가 아닌 '건강 위해 요소'(yếu tố gây hại sức khỏe)로 설명해야 보수 우선순위가 올라갑니다.",
        "meaningVi": "Vi sinh vật phát triển trong môi trường ẩm ướt, xuất hiện dưới dạng vết đen hoặc vết ố trên tường, trần, nhà tắm. Không chỉ ảnh hưởng mỹ quan mà còn gây hại cho sức khỏe và kết cấu công trình nếu không xử lý kịp thời.",
        "context": "하자, 환기, 방수",
        "culturalNote": "한국에서는 곰팡이를 심각한 하자로 인식하고 즉시 제거 및 원인 해결을 요구하지만, 베트남에서는 기후상 불가피한 현상으로 여기는 경향이 있습니다. 한국 입주자는 곰팡이 발생 시 시공사 책임을 추궁하지만, 베트남에서는 환기 부족 등 사용자 책임으로 보는 경우가 많습니다. 통역 시 'mốc do lỗi thi công'(시공 오류로 인한 곰팡이)와 'mốc do không thông gió'(환기 부족)를 구분해야 합니다.",
        "commonMistakes": [
            {
                "mistake": "곰팡이를 'vi khuẩn'(박테리아)로 통역",
                "correction": "'mốc' 또는 'nấm mốc'",
                "explanation": "vi khuẩn은 세균, mốc은 곰팡이(진균류)"
            },
            {
                "mistake": "'곰팡이 제거'를 'xóa mốc'로 통역",
                "correction": "'loại bỏ mốc và xử lý chống mốc'",
                "explanation": "제거는 단순 청소가 아니라 재발 방지 처리 포함"
            },
            {
                "mistake": "곰팡이 원인을 '습기'로만 단순화",
                "correction": "'ẩm ướt do rò rỉ, ngưng tụ hoặc thông gió kém'",
                "explanation": "누수, 결로, 환기 부족 등 구체적 원인 명시 필요"
            }
        ],
        "examples": [
            {
                "ko": "욕실 천장에 곰팡이가 심하게 발생했습니다",
                "vi": "Trần nhà tắm bị mốc nghiêm trọng",
                "situation": "formal"
            },
            {
                "ko": "곰팡이 원인은 환기 부족과 결로입니다",
                "vi": "Nguyên nhân mốc là do thông gió kém và ngưng tụ hơi nước",
                "situation": "onsite"
            },
            {
                "ko": "곰팡이 제거 후 방습 페인트를 칠하겠습니다",
                "vi": "Sau khi loại bỏ mốc sẽ sơn lại bằng sơn chống ẩm",
                "situation": "formal"
            }
        ],
        "relatedTerms": [
            "결로",
            "환기",
            "방수",
            "하자보수"
        ]
    },
    {
        "slug": "ngung-tu",
        "domain": "construction",
        "korean": "결로",
        "vietnamese": "Ngưng tụ (hơi nước)",
        "hanja": "結露",
        "hanjaReading": "結(맺을 결) + 露(이슬 로)",
        "pronunciation": "응엉 뚜 (허이 느억)",
        "meaningKo": "실내외 온도차로 인해 공기 중 수증기가 차가운 표면에 물방울로 맺히는 현상입니다. 통역 시 'ngưng tụ'는 응축, 'hơi nước'는 수증기이므로 함께 써서 'ngưng tụ hơi nước'로 표현하는 것이 명확합니다. 베트남의 고온다습한 기후에서는 냉방 건물에서 결로가 자주 발생하며, 단열재 시공 불량이 주요 원인입니다. 한국에서는 겨울철 난방 시 문제가 되지만, 베트남에서는 냉방 시 외벽과 천장에 결로가 생기는 패턴이 다릅니다. 통역 시 '이슬 맺힘' 정도로 가볍게 설명하지 말고, '습기 축적으로 인한 곰팡이 및 구조 손상 위험'까지 강조해야 합니다.",
        "meaningVi": "Hiện tượng hơi nước trong không khí ngưng tụ thành giọt nước trên bề mặt lạnh do chênh lệch nhiệt độ giữa trong và ngoài. Thường xảy ra tại tường, trần, cửa sổ và gây ra mốc, hư hỏng nếu không xử lý.",
        "context": "하자, 단열, 환기",
        "culturalNote": "한국에서는 결로를 단열 시공 불량의 증거로 보고 시공사 책임을 추궁하지만, 베트남에서는 사용자의 환기 부족으로 치부하는 경우가 많습니다. 한국은 이중창과 단열재로 결로를 예방하지만, 베트남은 단일창과 얇은 단열재 사용으로 결로가 만성적입니다. 통역 시 'do thi công cách nhiệt kém'(단열 시공 불량) vs 'do sử dụng máy lạnh quá mạnh'(냉방 과도)를 구분해야 책임 소재가 명확해집니다.",
        "commonMistakes": [
            {
                "mistake": "결로를 '이슬'(sương)로만 통역",
                "correction": "'ngưng tụ hơi nước do chênh lệch nhiệt độ'",
                "explanation": "sương은 자연 현상, 결로는 건축 하자의 징후"
            },
            {
                "mistake": "'결로 방지'를 'chống sương'으로 통역",
                "correction": "'ngăn ngừa ngưng tụ bằng cách nhiệt và thông gió'",
                "explanation": "방지 방법(단열, 환기)까지 명시해야 함"
            },
            {
                "mistake": "결로와 누수를 혼동",
                "correction": "결로는 'ngưng tụ từ không khí', 누수는 'rò rỉ từ đường ống'",
                "explanation": "원인이 다르므로 해결책도 다름"
            }
        ],
        "examples": [
            {
                "ko": "외벽 단열재 부실로 결로가 발생하고 있습니다",
                "vi": "Xảy ra ngưng tụ hơi nước do thi công cách nhiệt tường ngoài kém chất lượng",
                "situation": "formal"
            },
            {
                "ko": "결로 때문에 벽지가 들뜨고 곰팡이가 생겼어요",
                "vi": "Giấy dán tường bị phồng và mốc do ngưng tụ hơi nước",
                "situation": "onsite"
            },
            {
                "ko": "결로 방지를 위해 단열재를 보강하겠습니다",
                "vi": "Sẽ tăng cường lớp cách nhiệt để ngăn ngừa ngưng tụ",
                "situation": "formal"
            }
        ],
        "relatedTerms": [
            "단열",
            "곰팡이",
            "환기",
            "누수"
        ]
    },
    {
        "slug": "sua-chua-vet-nut",
        "domain": "construction",
        "korean": "크랙보수",
        "vietnamese": "Sửa chữa vết nứt",
        "hanja": None,
        "hanjaReading": None,
        "pronunciation": "스어 쯔어 벳 눗",
        "meaningKo": "콘크리트, 벽체, 바닥 등에 발생한 균열(크랙)을 메우고 보강하는 작업입니다. 통역 시 '크랙'을 'crack'으로만 발음하지 말고 'vết nứt'(균열)로 번역하고, 보수는 'sửa chữa'가 일반적이지만 심각도에 따라 'trám'(메우기), 'gia cố'(보강), 'chống nứt'(균열 방지)로 구분해야 합니다. 베트남에서는 헤어크랙(hairline crack, vết nứt tóc)을 대수롭지 않게 여기지만, 한국에서는 구조 안전성 검토 대상으로 봅니다. 통역 시 균열 폭(độ rộng vết nứt)과 깊이(độ sâu)를 수치로 명시해야 심각성이 전달됩니다.",
        "meaningVi": "Công tác lấp đầy và gia cố các vết nứt trên bê tông, tường, sàn. Tùy mức độ nghiêm trọng mà áp dụng các phương pháp như trám epoxy, chèn vữa, hoặc gia cố kết cấu.",
        "context": "하자, 보수, 구조",
        "culturalNote": "한국에서는 크랙을 구조적 위험 신호로 보고 원인 분석 후 근본적 보수를 진행하지만, 베트남에서는 표면만 메우는 임시 처리가 일반적입니다. 한국은 에폭시 주입 등 전문 공법을 쓰지만, 베트남은 시멘트 몰탈로 단순 충진하는 경우가 많습니다. 통역 시 'sửa tạm thời'(임시 보수) vs 'sửa chữa căn bản'(근본 보수)를 구분하고, 'theo dõi vết nứt'(균열 모니터링) 필요성을 강조해야 합니다.",
        "commonMistakes": [
            {
                "mistake": "모든 크랙을 'crack'으로만 발음",
                "correction": "'vết nứt' + 크랙 유형 명시 (tóc, lớn, xuyên suốt)",
                "explanation": "헤어크랙, 큰 균열, 관통 균열 등 구분 필요"
            },
            {
                "mistake": "'크랙보수'를 'sửa crack'으로 통역",
                "correction": "'sửa chữa vết nứt bằng [공법]'",
                "explanation": "보수 방법(epoxy, 몰탈 등) 명시 필요"
            },
            {
                "mistake": "균열 폭을 mm 단위로만 말함",
                "correction": "'vết nứt rộng X mm, sâu Y mm'",
                "explanation": "폭과 깊이 모두 명시해야 심각도 판단 가능"
            }
        ],
        "examples": [
            {
                "ko": "외벽에 폭 5mm 균열이 발견되어 보수가 필요합니다",
                "vi": "Phát hiện vết nứt rộng 5mm tại tường ngoài cần sửa chữa",
                "situation": "formal"
            },
            {
                "ko": "에폭시 주입 공법으로 크랙보수를 진행하겠습니다",
                "vi": "Sẽ tiến hành sửa chữa vết nứt bằng phương pháp chèn epoxy",
                "situation": "onsite"
            },
            {
                "ko": "헤어크랙은 모니터링하고, 큰 균열은 즉시 보수하겠습니다",
                "vi": "Vết nứt tóc sẽ theo dõi, vết nứt lớn sẽ sửa chữa ngay",
                "situation": "formal"
            }
        ],
        "relatedTerms": [
            "균열",
            "에폭시",
            "구조보강",
            "하자보수"
        ]
    },
    {
        "slug": "thay-sealant",
        "domain": "construction",
        "korean": "실란트교체",
        "vietnamese": "Thay sealant (trám kín)",
        "hanja": None,
        "hanjaReading": None,
        "pronunciation": "타이 실-란트 (짬 낀)",
        "pronunciation": "타이 실-란트 (짬 낀)",
        "meaningKo": "창호, 외벽 조인트, 욕실 등의 방수·기밀을 위해 주입한 실란트(씰링재)가 노화되어 교체하는 작업입니다. 통역 시 'sealant'를 영어 그대로 쓰되 베트남어 설명 'chất trám kín chống thấm'(방수 충진재)을 덧붙여야 합니다. 베트남의 강한 자외선과 고온으로 실란트 노화가 한국보다 2배 빠르므로(보통 2~3년), 교체 주기를 명확히 안내해야 합니다. 한국에서는 실리콘, 폴리우레탄 등 용도별로 구분하지만, 베트nam에서는 'keo silicon'(실리콘 본드)로 통칭하는 경우가 많아 혼동의 여지가 있습니다.",
        "meaningVi": "Công tác thay thế chất trám kín (sealant) đã lão hóa tại cửa, mối nối tường ngoài, nhà tắm để đảm bảo chống thấm và kín khí. Do điều kiện thời tiết khắc nghiệt, sealant thường cần thay sau 2-3 năm.",
        "context": "하자, 방수, 유지보수",
        "culturalNote": "한국에서는 실란트 교체를 전문 방수업체에 맡기지만, 베트남에서는 일반 미장공이 실리콘 건으로 간단히 처리하는 경우가 많아 품질 차이가 큽니다. 한국은 교체 시 기존 실란트를 완전 제거 후 프라이머 도포, 재시공하지만, 베트남은 기존 것 위에 덧바르는 경우가 있어 조기 탈락 위험이 있습니다. 통역 시 'loại bỏ sealant cũ hoàn toàn'(기존 실란트 완전 제거)를 강조해야 합니다.",
        "commonMistakes": [
            {
                "mistake": "실란트를 'keo dán'(접착제)로 통역",
                "correction": "'sealant (chất trám kín chống thấm)'",
                "explanation": "접착이 아닌 방수·기밀이 주 목적"
            },
            {
                "mistake": "'실란트 교체'를 'thay keo'로만 통역",
                "correction": "'tháo sealant cũ và trám mới theo đúng kỹ thuật'",
                "explanation": "공정(제거→청소→프라이머→재시공) 명시 필요"
            },
            {
                "mistake": "실리콘과 실란트를 동일시",
                "correction": "실리콘은 실란트의 한 종류",
                "explanation": "폴리우레탄, 아크릴 등 다른 종류도 있음"
            }
        ],
        "examples": [
            {
                "ko": "창호 주변 실란트가 갈라져서 교체가 필요합니다",
                "vi": "Sealant quanh cửa bị nứt cần thay mới",
                "situation": "formal"
            },
            {
                "ko": "기존 실란트 제거 후 프라이머 도포하고 재시공하겠습니다",
                "vi": "Sau khi tháo sealant cũ sẽ sơn lớp lót và trám lại",
                "situation": "onsite"
            },
            {
                "ko": "실란트 수명은 약 3년이니 정기 점검하시기 바랍니다",
                "vi": "Tuổi thọ sealant khoảng 3 năm, vui lòng kiểm tra định kỳ",
                "situation": "formal"
            }
        ],
        "relatedTerms": [
            "방수",
            "창호",
            "조인트",
            "코킹"
        ]
    },
    {
        "slug": "ke-hoach-bao-duong",
        "domain": "construction",
        "korean": "유지보수계획",
        "vietnamese": "Kế hoạch bảo dưỡng",
        "hanja": "維持補修計劃",
        "hanjaReading": "維(보전할 유) + 持(가질 지) + 補(기울 보) + 修(닦을 수) + 計(셀 계) + 劃(그을 획)",
        "pronunciation": "께 호악 바오 즈엉",
        "meaningKo": "건축물과 설비의 성능을 유지하기 위해 정기적으로 점검하고 보수하는 활동을 계획한 문서입니다. 통역 시 '유지보수'는 'bảo dưỡng'(보수), 'bảo trì'(유지)로 표현할 수 있는데, 베트nam에서는 보통 'bảo dưỡng'을 더 많이 씁니다. 한국에서는 법적으로 건축물 유지관리 계획서 제출이 의무이지만, 베트남에서는 권장 사항으로 인식되는 경우가 많습니다. 통역 시 'kế hoạch bảo dưỡng định kỳ'(정기 유지보수 계획)와 일회성 수리를 구분하고, 'dự phòng'(예방) vs 'khắc phục'(사후 수리) 개념을 명확히 해야 합니다.",
        "meaningVi": "Tài liệu lập kế hoạch các hoạt động kiểm tra và sửa chữa định kỳ nhằm duy trì hiệu suất của công trình và thiết bị. Bao gồm lịch trình, nội dung, chi phí dự kiến cho từng hạng mục bảo dưỡng.",
        "context": "유지관리, 시설, 준공",
        "culturalNote": "한국에서는 FM(시설관리) 전문 업체가 체계적인 유지보수를 진행하지만, 베트남에서는 관리사무소가 필요시 업체를 부르는 사후 대응 방식이 일반적입니다. 한국은 예방 정비(preventive maintenance) 개념이 정착됐지만, 베트남은 고장 나면 고치는 사후 정비(corrective maintenance) 위주입니다. 통역 시 'bảo dưỡng dự phòng'(예방 보수)의 경제성을 강조하고, 'giảm chi phí sửa chữa lớn'(큰 수리비 절감) 효과를 설명해야 수용도가 높습니다.",
        "commonMistakes": [
            {
                "mistake": "유지보수를 'sửa chữa'(수리)로만 통역",
                "correction": "'bảo dưỡng định kỳ để duy trì hiệu suất'",
                "explanation": "수리는 사후 대응, 유지보수는 예방+유지"
            },
            {
                "mistake": "'유지보수계획'을 'kế hoạch sửa'로 통역",
                "correction": "'kế hoạch bảo dưỡng định kỳ'",
                "explanation": "정기성과 체계성 강조 필요"
            },
            {
                "mistake": "bảo dưỡng과 bảo trì를 혼용",
                "correction": "bảo dưỡng은 설비 중심, bảo trì는 건물 전체",
                "explanation": "대상에 따라 용어 선택"
            }
        ],
        "examples": [
            {
                "ko": "준공 후 5년간 유지보수계획을 수립하겠습니다",
                "vi": "Sẽ lập kế hoạch bảo dưỡng cho 5 năm sau nghiệm thu",
                "situation": "formal"
            },
            {
                "ko": "연 2회 정기점검과 월 1회 소모품 교체를 계획했습니다",
                "vi": "Đã lên kế hoạch kiểm tra định kỳ 2 lần/năm và thay vật tư tiêu hao 1 lần/tháng",
                "situation": "onsite"
            },
            {
                "ko": "예방 정비로 장기적으로 비용을 절감할 수 있습니다",
                "vi": "Bảo dưỡng dự phòng giúp tiết kiệm chi phí lâu dài",
                "situation": "formal"
            }
        ],
        "relatedTerms": [
            "시설관리",
            "정기점검",
            "하자보수",
            "AS"
        ]
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

def main():
    """메인 실행 함수"""
    # 기존 파일 읽기
    with open(file_path, "r", encoding="utf-8") as f:
        existing_data = json.load(f)

    print(f"✅ 기존 용어 수: {len(existing_data)}개")

    # 새 용어 추가
    existing_data.extend(data)

    print(f"➕ 추가할 용어 수: {len(data)}개")
    print(f"📊 최종 용어 수: {len(existing_data)}개")

    # 파일 저장
    with open(file_path, "w", encoding="utf-8") as f:
        json.dump(existing_data, f, ensure_ascii=False, indent=2)

    print(f"💾 저장 완료: {file_path}")
    print("\n📋 추가된 용어:")
    for term in data:
        print(f"  - {term['korean']} ({term['vietnamese']})")

if __name__ == "__main__":
    main()
