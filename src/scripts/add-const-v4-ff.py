#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Construction 용어 추가 스크립트 v4-ff
테마: 커튼월/외장 (Curtain Wall & Facade)
대상: construction.json
개수: 10개
"""

import json
import os

# 추가할 용어 데이터 (Tier S 기준)
data = [
    {
        "slug": "tuong-rem-don-vi",
        "korean": "유닛 커튼월",
        "vietnamese": "Tường rèm đơn vị",
        "hanja": None,
        "hanjaReading": None,
        "pronunciation": "유닛 커튼월",
        "meaningKo": "공장에서 미리 제작된 패널 단위로 현장에서 조립하는 커튼월 시스템. 품질 균일성이 높고 공기 단축이 가능하지만 운송과 양중 계획이 중요합니다. 통역 시 '유닛 방식'과 '스틱 방식'을 명확히 구분해야 하며, 베트남 현장에서는 운송 여건상 스틱 방식을 선호하는 경우가 많으므로 시공법 선택 배경을 설명할 때 주의가 필요합니다.",
        "meaningVi": "Hệ thống tường rèm được lắp ráp từ các tấm panel đã được gia công sẵn tại nhà máy. Ưu điểm là chất lượng đồng đều và rút ngắn thời gian thi công.",
        "context": "건축외장, 초고층건물, 공장제작",
        "culturalNote": "한국은 공기 단축과 품질 관리를 위해 유닛 커튼월을 선호하지만, 베트남은 운송비와 현장 여건 때문에 스틱 커튼월을 더 많이 사용합니다. 유닛 방식 제안 시 물류 비용과 양중 계획을 함께 설명해야 합니다.",
        "commonMistakes": [
            {
                "mistake": "Tường rèm조립식",
                "correction": "Tường rèm đơn vị 또는 Unitized curtain wall",
                "explanation": "unit을 '조립식'으로 번역하면 의미가 모호해집니다"
            },
            {
                "mistake": "유닛월을 '빠른 공법'으로만 설명",
                "correction": "공장 제작 → 운송 → 양중 → 설치 전 과정 설명",
                "explanation": "속도만 강조하면 운송/양중 리스크를 간과합니다"
            },
            {
                "mistake": "Stick 커튼월과 혼동",
                "correction": "Unit = 패널 단위, Stick = 부재 단위",
                "explanation": "시공 방식의 근본적 차이를 명확히 구분해야 합니다"
            }
        ],
        "examples": [
            {
                "ko": "유닛 커튼월 양중 계획서를 검토해 주세요.",
                "vi": "Vui lòng xem xét kế hoạch nâng hạ tường rèm đơn vị.",
                "situation": "formal"
            },
            {
                "ko": "유닛 크기가 크면 운송비가 증가합니다.",
                "vi": "Nếu kích thước đơn vị lớn, chi phí vận chuyển sẽ tăng.",
                "situation": "onsite"
            },
            {
                "ko": "공장 생산 단계부터 품질 관리를 시작합니다.",
                "vi": "Chúng tôi bắt đầu kiểm soát chất lượng ngay từ giai đoạn sản xuất tại nhà máy.",
                "situation": "formal"
            }
        ],
        "relatedTerms": ["스틱 커튼월", "멀리언", "트랜섬", "양중계획"]
    },
    {
        "slug": "tuong-rem-thanh-cau-kien",
        "korean": "스틱 커튼월",
        "vietnamese": "Tường rèm thanh cấu kiện",
        "hanja": None,
        "hanjaReading": None,
        "pronunciation": "스틱 커튼월",
        "meaningKo": "현장에서 멀리언, 트랜섬 등의 부재를 하나씩 조립하는 커튼월 시스템. 유닛 방식보다 운송이 용이하고 현장 대응력이 높지만 시공 정밀도 관리가 어렵습니다. 통역 시 '현장 조립'이라는 특성을 강조하고, 베트남 현장에서 선호되는 이유(운송비 절감, 현지 인력 활용)를 설명할 수 있어야 합니다.",
        "meaningVi": "Hệ thống tường rèm được lắp ráp trực tiếp tại công trường từng thanh cấu kiện như mullion, transom. Dễ vận chuyển nhưng yêu cầu độ chính xác cao khi thi công.",
        "context": "건축외장, 현장시공, 정밀시공",
        "culturalNote": "베트남 현장에서는 운송비와 현지 인력 활용 측면에서 스틱 방식을 선호하는 경향이 있습니다. 한국은 품질과 공기를 우선하지만, 베트남은 경제성과 유연성을 중시하므로 방식 선택 시 이러한 차이를 고려해야 합니다.",
        "commonMistakes": [
            {
                "mistake": "Stick을 '막대기'로 직역",
                "correction": "Thanh cấu kiện (부재) 또는 Stick system",
                "explanation": "전문 용어로서의 의미를 유지해야 합니다"
            },
            {
                "mistake": "유닛월보다 품질이 낮다고 설명",
                "correction": "시공 방식의 차이이며 품질은 시공 정밀도에 달림",
                "explanation": "방식 자체의 우열이 아닌 관리 수준의 문제입니다"
            },
            {
                "mistake": "현장 조립을 '간단한 작업'으로 표현",
                "correction": "높은 정밀도와 숙련도가 요구되는 작업",
                "explanation": "난이도를 과소평가하면 품질 문제가 발생합니다"
            }
        ],
        "examples": [
            {
                "ko": "스틱 커튼월은 현장 여건에 유연하게 대응할 수 있습니다.",
                "vi": "Tường rèm thanh cấu kiện có thể linh hoạt ứng phó với điều kiện công trường.",
                "situation": "formal"
            },
            {
                "ko": "멀리언 조립 정밀도를 수시로 확인하세요.",
                "vi": "Hãy kiểm tra độ chính xác lắp ráp mullion thường xuyên.",
                "situation": "onsite"
            },
            {
                "ko": "운송비를 절감하기 위해 스틱 방식을 선택했습니다.",
                "vi": "Chúng tôi đã chọn phương pháp stick để giảm chi phí vận chuyển.",
                "situation": "formal"
            }
        ],
        "relatedTerms": ["유닛 커튼월", "멀리언", "트랜섬", "현장조립"]
    },
    {
        "slug": "spandrel",
        "korean": "스팬드럴",
        "vietnamese": "Spandrel",
        "hanja": None,
        "hanjaReading": None,
        "pronunciation": "스팬드럴",
        "meaningKo": "커튼월에서 층간 구조체를 가리는 불투명한 패널 부분. 단열재와 방화 성능이 중요하며, 시각적으로 비전(Vision) 부분과 구분됩니다. 통역 시 '층간 가림 패널' 또는 '불투명 부분'으로 풀어 설명하고, 베트남 현장에서는 방화 기준이 다를 수 있으므로 한국 기준과 비교 설명이 필요합니다.",
        "meaningVi": "Phần panel không trong suốt của tường rèm, che khuất kết cấu giữa các tầng. Có vai trò quan trọng về cách nhiệt và chống cháy.",
        "context": "커튼월, 외벽마감, 방화설계",
        "culturalNote": "한국은 스팬드럴 부분의 방화 및 단열 성능을 엄격하게 관리하지만, 베트남은 기준이 상대적으로 느슨할 수 있습니다. 한국 기준 적용 시 현지 인허가 과정에서 과다 설계로 보일 수 있으니 기준 차이를 사전에 설명해야 합니다.",
        "commonMistakes": [
            {
                "mistake": "Spandrel을 '장식 패널'로 번역",
                "correction": "층간 가림 패널 또는 불투명 패널",
                "explanation": "구조적 기능을 간과하면 안 됩니다"
            },
            {
                "mistake": "Vision과 Spandrel을 외관으로만 구분",
                "correction": "성능(투명/불투명, 방화, 단열)으로 구분",
                "explanation": "기능적 차이를 명확히 해야 합니다"
            },
            {
                "mistake": "방화 성능 미언급",
                "correction": "Spandrel은 방화 구획의 일부임을 강조",
                "explanation": "안전 기준과 직결된 사항입니다"
            }
        ],
        "examples": [
            {
                "ko": "스팬드럴 부분의 단열재 두께를 확인해 주세요.",
                "vi": "Vui lòng kiểm tra độ dày vật liệu cách nhiệt tại phần spandrel.",
                "situation": "onsite"
            },
            {
                "ko": "비전과 스팬드럴의 색상 조화를 맞춰야 합니다.",
                "vi": "Cần phải điều chỉnh sự hài hòa màu sắc giữa phần vision và spandrel.",
                "situation": "formal"
            },
            {
                "ko": "스팬드럴 방화 성능은 1시간 이상이어야 합니다.",
                "vi": "Hiệu năng chống cháy của spandrel phải đạt tối thiểu 1 giờ.",
                "situation": "formal"
            }
        ],
        "relatedTerms": ["비전글라스", "커튼월", "방화구획", "단열재"]
    },
    {
        "slug": "mullion",
        "korean": "멀리언",
        "vietnamese": "Mullion",
        "hanja": None,
        "hanjaReading": None,
        "pronunciation": "멀리언",
        "meaningKo": "커튼월에서 수직 방향으로 설치되는 주요 구조 부재. 유리와 패널을 지지하며, 정밀한 수직도 관리가 필수입니다. 통역 시 '수직 프레임' 또는 '세로 지지대'로 풀어 설명하고, 트랜섬(가로재)과의 연결 방식을 명확히 구분해야 합니다. 베트남 현장에서는 알루미늄 부재 품질 차이로 인한 변형 문제가 발생할 수 있어 재질 기준을 강조해야 합니다.",
        "meaningVi": "Cấu kiện chính lắp đặt theo phương thẳng đứng trong hệ thống tường rèm, đỡ kính và panel. Yêu cầu quản lý độ thẳng đứng chính xác.",
        "context": "커튼월시공, 구조부재, 정밀시공",
        "culturalNote": "한국은 멀리언의 수직도를 밀리미터 단위로 관리하지만, 베트남 현장에서는 측정 장비와 숙련도 부족으로 정밀도가 낮을 수 있습니다. 시공 초기부터 수직도 관리 방법을 교육하고, 측정 기준을 명확히 제시해야 합니다.",
        "commonMistakes": [
            {
                "mistake": "Mullion을 '기둥'으로 번역",
                "correction": "커튼월 수직재 또는 Mullion 그대로 사용",
                "explanation": "구조 기둥과 혼동될 수 있습니다"
            },
            {
                "mistake": "트랜섬과 명확히 구분하지 않음",
                "correction": "Mullion = 수직, Transom = 수평",
                "explanation": "방향성을 명확히 해야 조립 오류를 방지합니다"
            },
            {
                "mistake": "수직도 관리를 '대충 직각'으로 표현",
                "correction": "레이저 측정기로 ±2mm 이내 관리",
                "explanation": "정밀도 기준을 구체적으로 제시해야 합니다"
            }
        ],
        "examples": [
            {
                "ko": "멀리언 설치 후 레이저로 수직도를 측정하세요.",
                "vi": "Sau khi lắp mullion, hãy đo độ thẳng đứng bằng laser.",
                "situation": "onsite"
            },
            {
                "ko": "멀리언과 트랜섬의 연결부 실링을 확인해 주세요.",
                "vi": "Vui lòng kiểm tra phần seal tại mối nối mullion và transom.",
                "situation": "onsite"
            },
            {
                "ko": "멀리언 재질은 고강도 알루미늄을 사용합니다.",
                "vi": "Chúng tôi sử dụng nhôm cường độ cao cho mullion.",
                "situation": "formal"
            }
        ],
        "relatedTerms": ["트랜섬", "커튼월", "수직도", "알루미늄프레임"]
    },
    {
        "slug": "transom",
        "korean": "트랜섬",
        "vietnamese": "Transom",
        "hanja": None,
        "hanjaReading": None,
        "pronunciation": "트랜섬",
        "meaningKo": "커튼월에서 수평 방향으로 설치되는 구조 부재. 멀리언과 함께 커튼월의 골조를 형성하며, 층간 높이 조절과 패널 분할 역할을 합니다. 통역 시 '수평 프레임' 또는 '가로재'로 설명하고, 멀리언과의 조립 순서를 명확히 전달해야 합니다. 베트남 현장에서는 수평도 관리 미흡으로 처짐이 발생할 수 있으니 주의가 필요합니다.",
        "meaningVi": "Cấu kiện lắp đặt theo phương ngang trong hệ thống tường rèm, tạo thành khung cùng với mullion. Có vai trò điều chỉnh chiều cao tầng và phân chia panel.",
        "context": "커튼월시공, 골조설치, 수평관리",
        "culturalNote": "한국은 트랜섬 설치 시 수평도를 정밀하게 관리하지만, 베트남 현장에서는 장비 부족으로 육안 확인에 의존하는 경우가 많습니다. 수평 레이저 등 측정 장비 사용을 의무화하고, 처짐 방지 대책을 사전에 수립해야 합니다.",
        "commonMistakes": [
            {
                "mistake": "Transom을 '보'로 번역",
                "correction": "커튼월 수평재 또는 Transom 그대로 사용",
                "explanation": "구조 보와 혼동될 수 있습니다"
            },
            {
                "mistake": "멀리언과 트랜섬 조립 순서 혼동",
                "correction": "일반적으로 멀리언 선설치 → 트랜섬 후설치",
                "explanation": "조립 순서가 바뀌면 정밀도가 떨어집니다"
            },
            {
                "mistake": "수평도 측정 없이 설치",
                "correction": "레이저 수평계로 ±2mm 이내 확인",
                "explanation": "처짐은 누수와 외관 문제를 유발합니다"
            }
        ],
        "examples": [
            {
                "ko": "트랜섬 설치 전에 수평 기준선을 확인하세요.",
                "vi": "Trước khi lắp transom, hãy kiểm tra đường chuẩn ngang.",
                "situation": "onsite"
            },
            {
                "ko": "트랜섬과 멀리언의 조인트 부위를 밀봉해야 합니다.",
                "vi": "Cần phải seal kín tại vị trí mối nối giữa transom và mullion.",
                "situation": "onsite"
            },
            {
                "ko": "트랜섬 간격은 층고에 따라 조정됩니다.",
                "vi": "Khoảng cách transom được điều chỉnh theo chiều cao tầng.",
                "situation": "formal"
            }
        ],
        "relatedTerms": ["멀리언", "커튼월", "수평도", "조인트"]
    },
    {
        "slug": "sealing-cua-tuong-rem",
        "korean": "커튼월 실링",
        "vietnamese": "Sealing của tường rèm",
        "hanja": None,
        "hanjaReading": None,
        "pronunciation": "커튼월 실링",
        "meaningKo": "커튼월 부재 간 또는 유리와 프레임 사이의 기밀·수밀 처리. 구조 실란트와 웨더 실란트로 구분되며, 시공 순서와 양생 시간 관리가 중요합니다. 통역 시 '방수·방풍 처리' 또는 '밀봉'으로 설명하고, 베트남의 높은 습도 환경에서 실란트 양생이 더디므로 공기 계획 시 여유를 두어야 합니다.",
        "meaningVi": "Xử lý kín khí và kín nước giữa các cấu kiện tường rèm hoặc giữa kính và khung. Phân biệt structural sealant và weather sealant, cần quản lý thứ tự thi công và thời gian bảo dưỡng.",
        "context": "커튼월마감, 방수공사, 실란트작업",
        "culturalNote": "한국은 실란트 종류와 시공 조건을 엄격히 관리하지만, 베트남 현장에서는 저가 실란트 사용으로 내구성 문제가 발생할 수 있습니다. 또한 고온다습한 기후로 인해 양생 시간이 길어지므로, 공정 계획 시 날씨 조건을 고려해야 합니다.",
        "commonMistakes": [
            {
                "mistake": "Sealing을 단순 '접착제'로 번역",
                "correction": "기밀·수밀용 실란트 (Sealant)",
                "explanation": "접착이 아닌 밀봉이 주 목적입니다"
            },
            {
                "mistake": "구조 실란트와 웨더 실란트 구분 안 함",
                "correction": "구조용 = 하중 지지, 웨더용 = 기후 차단",
                "explanation": "용도가 다르므로 재질과 시공법도 다릅니다"
            },
            {
                "mistake": "양생 시간 무시하고 다음 공정 진행",
                "correction": "제조사 지침에 따라 최소 24~48시간 양생",
                "explanation": "조기 하중 발생 시 실란트가 파손됩니다"
            }
        ],
        "examples": [
            {
                "ko": "구조 실란트 양생 후 웨더 실란트를 시공하세요.",
                "vi": "Sau khi bảo dưỡng structural sealant, hãy thi công weather sealant.",
                "situation": "onsite"
            },
            {
                "ko": "습도가 높으면 실란트 양생이 지연됩니다.",
                "vi": "Nếu độ ẩm cao, quá trình bảo dưỡng sealant sẽ bị chậm lại.",
                "situation": "onsite"
            },
            {
                "ko": "실링 작업 전에 표면 청소가 필수입니다.",
                "vi": "Trước khi làm seal, bắt buộc phải làm sạch bề mặt.",
                "situation": "formal"
            }
        ],
        "relatedTerms": ["실란트", "구조실란트", "웨더실란트", "양생시간"]
    },
    {
        "slug": "vat-lieu-dem-long",
        "korean": "백업재",
        "vietnamese": "Vật liệu đệm lỗng",
        "hanja": None,
        "hanjaReading": None,
        "pronunciation": "백업재",
        "meaningKo": "실링 작업 시 조인트 깊이를 조절하고 3면 접착을 방지하기 위해 삽입하는 폼 재질의 충전재. 실란트의 신축 성능을 확보하는 데 필수적입니다. 통역 시 '조인트 충전재' 또는 '밑받침재'로 설명하고, 베트남 현장에서는 생략하는 경우가 많으므로 반드시 사용해야 하는 이유(3면 접착 방지)를 명확히 전달해야 합니다.",
        "meaningVi": "Vật liệu xốp được chèn vào để điều chỉnh độ sâu mối nối và ngăn hiện tượng dính 3 mặt khi làm seal. Cần thiết để đảm bảo khả năng co giãn của sealant.",
        "context": "실링작업, 조인트시공, 방수공사",
        "culturalNote": "한국 현장에서는 백업재 사용이 표준 공정이지만, 베트남에서는 비용 절감을 위해 생략하는 사례가 많습니다. 3면 접착 시 실란트가 신축하지 못해 균열이 발생하므로, 백업재의 필요성을 비용 대비 효과로 설명하는 것이 효과적입니다.",
        "commonMistakes": [
            {
                "mistake": "백업재를 '스티로폼'으로 표현",
                "correction": "폴리에틸렌 폼 백업재 (PE foam backer rod)",
                "explanation": "재질이 다르며 용도에 맞는 제품을 사용해야 합니다"
            },
            {
                "mistake": "백업재 없이 실란트만 충전",
                "correction": "백업재 삽입 → 실란트 충전 (2면 접착)",
                "explanation": "3면 접착 시 실란트가 신축하지 못합니다"
            },
            {
                "mistake": "백업재 직경을 임의로 선택",
                "correction": "조인트 폭의 1.2~1.5배 직경 사용",
                "explanation": "적정 직경이 아니면 밀착 효과가 없습니다"
            }
        ],
        "examples": [
            {
                "ko": "백업재를 먼저 삽입한 후 실란트를 충전하세요.",
                "vi": "Hãy chèn vật liệu đệm trước, sau đó mới đổ sealant.",
                "situation": "onsite"
            },
            {
                "ko": "조인트 폭이 20mm면 백업재는 25~30mm를 사용합니다.",
                "vi": "Nếu chiều rộng mối nối là 20mm, sử dụng vật liệu đệm 25~30mm.",
                "situation": "onsite"
            },
            {
                "ko": "백업재 없이 시공하면 실란트가 빨리 손상됩니다.",
                "vi": "Nếu thi công không có vật liệu đệm, sealant sẽ hư hỏng nhanh.",
                "situation": "formal"
            }
        ],
        "relatedTerms": ["실란트", "조인트", "3면접착", "실링"]
    },
    {
        "slug": "tam-nhua-nhom-acm",
        "korean": "ACM 패널",
        "vietnamese": "Tấm nhựa nhôm ACM",
        "hanja": None,
        "hanjaReading": None,
        "pronunciation": "에이씨엠 패널",
        "meaningKo": "알루미늄 복합 패널(Aluminum Composite Material)의 약어로, 두 장의 알루미늄 판 사이에 폴리에틸렌 심재를 삽입한 외장재. 경량이면서도 다양한 색상과 형태 가공이 가능하지만, 화재 시 심재가 연소될 위험이 있어 방화 등급 확인이 필수입니다. 통역 시 '알루미늄 복합 패널'로 풀어 설명하고, 베트난에서는 저가 ACM 사용으로 화재 위험이 있으므로 방화 등급(A1, A2, B 등)을 반드시 확인해야 합니다.",
        "meaningVi": "Tấm panel phức hợp nhôm, viết tắt của Aluminum Composite Material. Được tạo bởi 2 lớp nhôm夹 lõi polyethylene. Nhẹ và dễ gia công nhưng cần kiểm tra cấp độ chống cháy.",
        "context": "외장마감, 건축마감재, 방화안전",
        "culturalNote": "한국은 그렌펠 타워 화재 이후 ACM 패널의 방화 등급을 엄격히 관리하지만, 베트남에서는 여전히 저가 제품이 많이 유통됩니다. A2 등급 이상(난연성) ACM 사용을 명시하고, 현지 조달 시 시험 성적서를 반드시 확인해야 합니다.",
        "commonMistakes": [
            {
                "mistake": "ACM을 '알루미늄 판'으로 번역",
                "correction": "알루미늄 복합 패널 (Composite)",
                "explanation": "단순 금속판이 아닌 복합 구조입니다"
            },
            {
                "mistake": "방화 등급 확인 없이 시공",
                "correction": "A2 등급 이상(난연) 제품 사용",
                "explanation": "화재 시 심재가 연소되어 대형 사고로 이어집니다"
            },
            {
                "mistake": "모든 ACM이 동일하다고 설명",
                "correction": "심재 재질에 따라 FR(방화), PE(일반) 구분",
                "explanation": "용도와 안전 기준에 따라 선택해야 합니다"
            }
        ],
        "examples": [
            {
                "ko": "ACM 패널은 A2 등급 이상으로 선정하세요.",
                "vi": "Hãy chọn tấm ACM cấp độ A2 trở lên.",
                "situation": "formal"
            },
            {
                "ko": "심재가 난연성인지 시험 성적서를 확인해 주세요.",
                "vi": "Vui lòng kiểm tra chứng nhận thí nghiệm xem lõi có chống cháy không.",
                "situation": "onsite"
            },
            {
                "ko": "ACM 패널 고정 브라켓 간격은 600mm입니다.",
                "vi": "Khoảng cách giữa các bracket cố định tấm ACM là 600mm.",
                "situation": "onsite"
            }
        ],
        "relatedTerms": ["외장패널", "알루미늄패널", "방화등급", "복합패널"]
    },
    {
        "slug": "tam-op-terracotta",
        "korean": "테라코타 패널",
        "vietnamese": "Tấm ốp terracotta",
        "hanja": None,
        "hanjaReading": None,
        "pronunciation": "테라코타 패널",
        "meaningKo": "고온에서 구운 점토 기반의 외장 패널로, 자연스러운 질감과 내구성, 친환경성이 장점입니다. 무게가 있어 골조 하중 검토가 필요하며, 습식 시공 시 백화 현상에 주의해야 합니다. 통역 시 '점토 소성 패널' 또는 '도기 외장재'로 설명하고, 베트남에서는 고온다습한 기후로 인해 백화가 자주 발생하므로 건식 시공법을 권장합니다.",
        "meaningVi": "Tấm panel ngoại thất làm từ đất sét nung ở nhiệt độ cao. Có kết cấu tự nhiên, bền và thân thiện môi trường nhưng nặng, cần kiểm tra tải trọng khung.",
        "context": "외장마감, 친환경건축, 고급마감",
        "culturalNote": "한국에서는 테라코타 패널이 고급 마감재로 인식되지만, 베트남에서는 점토 타일(gạch nung)과 혼동될 수 있습니다. 또한 습식 시공 시 백화 현상이 자주 발생하므로, 건식 앵커 공법을 추천하고 시공 전 목업 테스트를 강조해야 합니다.",
        "commonMistakes": [
            {
                "mistake": "Terracotta를 '붉은 벽돌'로 번역",
                "correction": "점토 소성 외장 패널",
                "explanation": "구조용 벽돌이 아닌 마감재입니다"
            },
            {
                "mistake": "습식 시공만 가능하다고 설명",
                "correction": "건식(앵커) 또는 습식(모르타르) 선택 가능",
                "explanation": "백화 방지를 위해 건식 공법을 권장합니다"
            },
            {
                "mistake": "골조 하중 검토 생략",
                "correction": "패널 무게 = 30~60kg/㎡, 구조 검토 필수",
                "explanation": "경량 패널이 아니므로 구조 안전 확인이 중요합니다"
            }
        ],
        "examples": [
            {
                "ko": "테라코타 패널은 건식 앵커 방식으로 시공하세요.",
                "vi": "Hãy thi công tấm terracotta bằng phương pháp neo khô.",
                "situation": "onsite"
            },
            {
                "ko": "습식 시공 시 백화 방지제를 사용해야 합니다.",
                "vi": "Khi thi công ướt, phải sử dụng chất chống muối bám trắng.",
                "situation": "formal"
            },
            {
                "ko": "테라코타는 자연 소재라 색상 편차가 있을 수 있습니다.",
                "vi": "Terracotta là vật liệu tự nhiên nên có thể có sự khác biệt màu sắc.",
                "situation": "formal"
            }
        ],
        "relatedTerms": ["외장패널", "친환경마감", "백화현상", "건식공법"]
    },
    {
        "slug": "chia-khung-tuong-rem",
        "korean": "커튼월 분할",
        "vietnamese": "Chia khung tường rèm",
        "hanja": None,
        "hanjaReading": None,
        "pronunciation": "커튼월 분할",
        "meaningKo": "커튼월의 멀리언과 트랜섬 간격을 결정하여 유리 및 패널의 크기와 배치를 계획하는 설계 과정. 구조 안전, 시공성, 경제성, 미관을 종합적으로 고려해야 합니다. 통역 시 '프레임 간격 계획' 또는 '유닛 분할 설계'로 설명하고, 베트남 현장에서는 유리 규격과 운송 조건에 따라 분할 방식을 조정해야 하므로 현지 여건을 사전에 파악해야 합니다.",
        "meaningVi": "Quá trình thiết kế quyết định khoảng cách mullion và transom để lên kế hoạch kích thước và bố trí kính, panel. Cần cân nhắc tổng hợp về an toàn kết cấu, thi công, kinh tế và thẩm mỹ.",
        "context": "커튼월설계, 외장계획, 구조설계",
        "culturalNote": "한국은 대형 유리 사용으로 분할을 최소화하는 경향이 있지만, 베트남은 유리 운송과 양중 여건상 소형 분할을 선호합니다. 설계 단계에서 현지 유리 공급 가능 규격과 운송 경로를 확인하고, 분할 계획을 조정하는 것이 경제적입니다.",
        "commonMistakes": [
            {
                "mistake": "분할을 '나누기'로만 번역",
                "correction": "커튼월 프레임 분할 설계 (Module planning)",
                "explanation": "설계 개념임을 명확히 해야 합니다"
            },
            {
                "mistake": "미관만 고려하여 분할 결정",
                "correction": "구조 안전 → 시공성 → 경제성 → 미관 순으로 검토",
                "explanation": "우선순위를 무시하면 시공 단계에서 문제 발생"
            },
            {
                "mistake": "현지 유리 규격 미확인",
                "correction": "베트남 공급 가능 최대 유리 규격 사전 조사",
                "explanation": "분할 후 유리 조달이 불가능하면 재설계 필요"
            }
        ],
        "examples": [
            {
                "ko": "커튼월 분할은 층고와 유리 최대 크기를 고려해야 합니다.",
                "vi": "Chia khung tường rèm phải xem xét chiều cao tầng và kích thước kính tối đa.",
                "situation": "formal"
            },
            {
                "ko": "분할 간격이 넓으면 멀리언 단면이 커집니다.",
                "vi": "Nếu khoảng cách chia rộng, tiết diện mullion sẽ lớn hơn.",
                "situation": "onsite"
            },
            {
                "ko": "경제성을 위해 표준 유리 규격에 맞춰 분할하세요.",
                "vi": "Để tiết kiệm, hãy chia theo quy cách kính tiêu chuẩn.",
                "situation": "formal"
            }
        ],
        "relatedTerms": ["멀리언", "트랜섬", "유닛분할", "모듈설계"]
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

# 새 용어 추가
existing_data.extend(data)

# 파일 저장
with open(file_path, "w", encoding="utf-8") as f:
    json.dump(existing_data, f, ensure_ascii=False, indent=2)

print(f"✅ {len(data)}개 용어 추가 완료 → {file_path}")
print(f"📊 현재 총 용어 수: {len(existing_data)}개")
