#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
철도/지하철 건설 전문용어 추가 스크립트 (10개)
Tier S 품질 기준 준수
"""

import json
import os

# 추가할 용어 데이터 (Tier S 기준)
data = [
    {
        "slug": "duong-ray",
        "korean": "궤도",
        "vietnamese": "Đường ray",
        "hanja": "軌道",
        "hanjaReading": "車(수레 거) + 道(길 도)",
        "pronunciation": "귀도",
        "meaningKo": "철도 차량이 운행하는 레일과 침목, 도상으로 구성된 구조물입니다. 통역 시 '레일'과 혼동하지 않도록 주의하세요. 궤도는 레일, 침목, 도상, 체결장치를 포함한 전체 시스템을 의미하며, 레일은 그 중 차량이 직접 접촉하는 강재 부분만을 가리킵니다. 현장에서 '궤도 유지보수'라고 하면 레일 교체뿐 아니라 침목, 도상 정비까지 포함하므로, 베트남어로 번역할 때 'bảo trì đường ray'로 포괄적으로 표현해야 합니다.",
        "meaningVi": "Cấu trúc bao gồm ray, tà vẹt, và lớp ballast mà tàu hỏa chạy trên đó. Bao gồm toàn bộ hệ thống ray, tà vẹt, lớp đá ballast và các thiết bị kẹp chặt.",
        "context": "철도, 지하철 건설 및 유지보수",
        "culturalNote": "한국에서는 '궤도'와 '선로'를 구분하여 사용하는데, 궤도는 기술적 용어로 레일과 지지구조를 포함한 전체를 의미하고, 선로는 일반적으로 철도 노선을 의미합니다. 베트남에서는 'đường ray'가 두 의미를 모두 포괄하므로, 통역 시 문맥에 따라 'đường ray' 또는 'tuyến đường sắt'로 구분해야 합니다. 한국 철도 건설 현장에서는 KR(한국철도공사) 규격을 따르며, 궤도 간격은 표준궤(1,435mm)를 기본으로 합니다.",
        "commonMistakes": [
            {
                "mistake": "궤도를 'ray'로만 번역",
                "correction": "đường ray (전체 구조) 또는 ray (레일 부분)로 구분",
                "explanation": "궤도는 레일만이 아닌 침목, 도상 포함 전체 시스템"
            },
            {
                "mistake": "선로와 궤도를 같은 단어로 번역",
                "correction": "선로는 tuyến đường sắt, 궤도는 đường ray",
                "explanation": "선로는 노선, 궤도는 물리적 구조물"
            },
            {
                "mistake": "궤도 간격을 'khoảng cách ray'로 표현",
                "correction": "khổ đường ray 또는 gauge",
                "explanation": "궤도 간격은 고정된 기술 규격이므로 전문용어 사용"
            }
        ],
        "examples": [
            {
                "ko": "궤도 부설 작업이 내일 시작됩니다",
                "vi": "Công tác lắp đặt đường ray sẽ bắt đầu vào ngày mai",
                "situation": "onsite"
            },
            {
                "ko": "이 구간은 표준궤로 설계되었습니다",
                "vi": "Đoạn này được thiết kế theo khổ đường ray tiêu chuẩn",
                "situation": "formal"
            },
            {
                "ko": "궤도 점검 중이니 접근하지 마세요",
                "vi": "Đang kiểm tra đường ray, không được tiếp cận",
                "situation": "onsite"
            }
        ],
        "relatedTerms": ["레일", "침목", "도상", "선로", "체결장치"]
    },
    {
        "slug": "ta-vet",
        "korean": "침목",
        "vietnamese": "Tà vẹt",
        "hanja": "枕木",
        "hanjaReading": "枕(베개 침) + 木(나무 목)",
        "pronunciation": "침목",
        "meaningKo": "레일을 지지하고 고정하며 하중을 도상에 분산시키는 횡방향 부재입니다. 통역 시 '목침목', 'PC침목', '합성침목' 등 재질에 따른 구분이 중요합니다. 현장에서 '침목 교체'라고 하면 노후 침목을 새 것으로 바꾸는 작업을 의미하며, 베트남어로 'thay tà vẹt'로 번역합니다. 한국 철도 현장에서는 PC(프리스트레스트 콘크리트) 침목이 주로 사용되므로, 'tà vẹt bê tông dự ứng lực'로 정확히 표현해야 합니다.",
        "meaningVi": "Thanh ngang đỡ ray, cố định ray và phân tán tải trọng xuống lớp ballast. Có thể làm bằng gỗ, bê tông hoặc vật liệu tổng hợp.",
        "context": "철도 궤도 건설 및 유지보수",
        "culturalNote": "한국에서는 1990년대 이후 목침목에서 PC침목으로 전환이 완료되었으나, 베트남에서는 일부 구간에서 여전히 목침목을 사용합니다. 통역 시 침목의 재질과 수명을 명확히 구분해야 하며, 한국 기술자가 'PC침목'이라고 할 때 베트남어로 'tà vẹt bê tông'이 아닌 'tà vẹt bê tông dự ứng lực'로 정확히 번역해야 합니다. 침목 간격(tà vẹt spacing)은 열차 속도와 하중에 따라 달라지므로, 현장 지시 사항을 정확히 전달하는 것이 안전에 직결됩니다.",
        "commonMistakes": [
            {
                "mistake": "침목을 'gỗ đỡ ray'로 번역",
                "correction": "tà vẹt",
                "explanation": "tà vẹt은 철도 전문용어로 확립된 표현"
            },
            {
                "mistake": "PC침목을 'tà vẹt nhựa'로 오역",
                "correction": "tà vẹt bê tông dự ứng lực",
                "explanation": "PC는 Prestressed Concrete의 약자"
            },
            {
                "mistake": "침목 교체를 'sửa tà vẹt'로 표현",
                "correction": "thay tà vẹt",
                "explanation": "교체는 완전히 바꾸는 것이므로 'thay'"
            }
        ],
        "examples": [
            {
                "ko": "이 구간은 PC침목으로 시공됩니다",
                "vi": "Đoạn này sẽ thi công bằng tà vẹt bê tông dự ứng lực",
                "situation": "formal"
            },
            {
                "ko": "침목 간격이 규정보다 좁습니다",
                "vi": "Khoảng cách giữa các tà vẹt hẹp hơn quy định",
                "situation": "onsite"
            },
            {
                "ko": "노후 침목 500개를 교체해야 합니다",
                "vi": "Cần thay 500 tà vẹt cũ",
                "situation": "formal"
            }
        ],
        "relatedTerms": ["궤도", "레일", "도상", "체결장치", "PC침목"]
    },
    {
        "slug": "ray-tau",
        "korean": "레일",
        "vietnamese": "Ray tàu",
        "hanja": None,
        "hanjaReading": None,
        "pronunciation": "레일",
        "meaningKo": "철도 차량의 바퀴가 직접 접촉하며 주행하는 강재 부재입니다. 통역 시 레일의 중량(kg/m)과 길이를 정확히 전달해야 합니다. 한국에서는 주로 50kgN, 60kg 레일을 사용하며, 베트nam어로 'ray 50kg', 'ray 60kg'으로 표현합니다. 현장에서 '레일 이음매', '레일 용접', '레일 절단' 등의 작업 용어가 자주 사용되므로, 'mối nối ray', 'hàn ray', 'cắt ray'로 정확히 번역해야 합니다. 레일 온도 변화에 따른 신축을 고려한 '장대레일' 시공 시 'ray dài liên tục'로 표현합니다.",
        "meaningVi": "Thanh thép mà bánh xe tàu tiếp xúc trực tiếp khi chạy. Trọng lượng ray được tính theo kg/m (ví dụ: ray 50kg, ray 60kg).",
        "context": "철도 궤도 건설 및 유지보수",
        "culturalNote": "한국 철도는 주로 60kg 레일을 사용하며, 고속철도는 UIC60 규격을 따릅니다. 베트남에서는 구간에 따라 50kg 또는 43kg 레일을 사용하는 경우도 있으므로, 통역 시 레일 규격을 명확히 확인해야 합니다. 한국 현장에서 '장대레일'이라고 하면 200m 이상 용접된 레일을 의미하며, 온도 신축을 고려한 특수 시공법이 필요합니다. 베트남어로 'ray dài liên tục' 또는 'CWR(Continuous Welded Rail)'로 표현하며, 시공 시 주의사항을 정확히 전달하는 것이 안전에 중요합니다.",
        "commonMistakes": [
            {
                "mistake": "레일을 단순히 'ray'로만 번역",
                "correction": "ray tàu 또는 ray đường sắt",
                "explanation": "문맥에 따라 구체적으로 표현"
            },
            {
                "mistake": "레일 중량을 'cân nặng ray'로 표현",
                "correction": "ray 50kg, ray 60kg (중량은 단위면적당 무게 규격)",
                "explanation": "레일 중량은 기술 규격이므로 숫자로 표기"
            },
            {
                "mistake": "장대레일을 'ray dài'로만 표현",
                "correction": "ray dài liên tục 또는 CWR",
                "explanation": "장대레일은 용접으로 연결된 특수 구조"
            }
        ],
        "examples": [
            {
                "ko": "60kg 레일로 교체 작업을 진행합니다",
                "vi": "Tiến hành công tác thay ray 60kg",
                "situation": "onsite"
            },
            {
                "ko": "레일 용접부를 검사해 주세요",
                "vi": "Vui lòng kiểm tra mối hàn ray",
                "situation": "onsite"
            },
            {
                "ko": "이 구간은 장대레일로 시공됩니다",
                "vi": "Đoạn này sẽ thi công bằng ray dài liên tục",
                "situation": "formal"
            }
        ],
        "relatedTerms": ["궤도", "침목", "체결장치", "레일 이음매", "장대레일"]
    },
    {
        "slug": "day-dien-tram",
        "korean": "전차선",
        "vietnamese": "Dây điện trâm",
        "hanja": "電車線",
        "hanjaReading": "電(전기 전) + 車(수레 차) + 線(줄 선)",
        "pronunciation": "전차선",
        "meaningKo": "전기 철도 차량에 전력을 공급하는 가공 전선입니다. 통역 시 '강체 전차선'과 '가선 전차선'을 구분해야 합니다. 한국 지하철은 주로 강체 전차선(rigid conductor rail)을 사용하며, 베트남어로 'thanh dẫn điện cứng'로 표현합니다. 일반 철도는 가선 전차선(overhead catenary)을 사용하며, 'dây điện treo'로 번역합니다. 현장에서 '전차선 높이 조정', '전차선 장력 조절' 등의 작업 지시가 나올 때, 안전을 위해 '전원 차단 확인' 후 작업한다는 점을 반드시 강조해야 합니다.",
        "meaningVi": "Dây dẫn điện trên cao cấp điện cho tàu điện. Bao gồm loại cứng (thanh dẫn điện) và loại dây treo (catenary).",
        "context": "전기 철도, 지하철 전기 설비",
        "culturalNote": "한국 지하철은 DC 1,500V 또는 AC 25kV 시스템을 사용하며, 전차선 방식도 노선마다 다릅니다. 서울 지하철 1~4호선은 가공 전차선, 5~8호선은 강체 전차선을 사용합니다. 베트남 하노이 메트로는 가공 전차선 방식이므로, 한국 기술자가 강체 전차선 경험을 설명할 때 시스템 차이를 명확히 전달해야 합니다. 전차선 작업은 고압 전기 위험이 있으므로, '절연', '접지', '전원 차단' 등 안전 용어를 정확히 통역하는 것이 생명과 직결됩니다.",
        "commonMistakes": [
            {
                "mistake": "전차선을 'dây điện'로만 번역",
                "correction": "dây điện trâm 또는 catenary (시스템에 따라)",
                "explanation": "전차선은 일반 전선과 구분되는 전문용어"
            },
            {
                "mistake": "강체 전차선을 'dây điện cứng'로 표현",
                "correction": "thanh dẫn điện cứng 또는 rigid conductor rail",
                "explanation": "강체는 레일 형태이므로 'thanh'"
            },
            {
                "mistake": "전차선 높이를 'cao dây điện'으로 표현",
                "correction": "độ cao dây điện trâm",
                "explanation": "기술 규격이므로 정확한 용어 사용"
            }
        ],
        "examples": [
            {
                "ko": "전차선 점검 중이니 전원을 차단해 주세요",
                "vi": "Đang kiểm tra dây điện trâm, vui lòng cắt nguồn điện",
                "situation": "onsite"
            },
            {
                "ko": "이 노선은 강체 전차선 방식입니다",
                "vi": "Tuyến này sử dụng phương thức thanh dẫn điện cứng",
                "situation": "formal"
            },
            {
                "ko": "전차선 장력을 재조정해야 합니다",
                "vi": "Cần điều chỉnh lại lực căng dây điện trâm",
                "situation": "onsite"
            }
        ],
        "relatedTerms": ["팬터그래프", "가공 전차선", "강체 전차선", "절연구간", "급전"]
    },
    {
        "slug": "san-ga",
        "korean": "승강장",
        "vietnamese": "Sân ga",
        "hanja": "昇降場",
        "hanjaReading": "昇(오를 승) + 降(내릴 강) + 場(마당 장)",
        "pronunciation": "승강장",
        "meaningKo": "철도역에서 승객이 열차에 타고 내리는 플랫폼입니다. 통역 시 '상대식 승강장'과 '섬식 승강장'을 구분해야 합니다. 상대식은 양쪽에 승강장이 있는 구조로 베트남어로 'sân ga đối diện', 섬식은 가운데 승강장으로 'sân ga đảo'로 표현합니다. 현장에서 '승강장 높이'는 열차 바닥과의 단차를 최소화하기 위한 중요 규격이므로, 'chiều cao sân ga'로 정확히 전달해야 합니다. 한국 지하철은 보통 1,150mm 높이 기준이며, 스크린도어 설치 시 승강장 보강 작업이 필요합니다.",
        "meaningVi": "Khu vực hành khách lên xuống tàu tại ga. Có loại đối diện (hai bên ray) và loại đảo (giữa hai ray).",
        "context": "지하철 및 철도역 건설",
        "culturalNote": "한국 지하철 승강장은 대부분 스크린도어가 설치되어 있어 안전성이 높지만, 베트남에서는 아직 일부 노선만 설치되어 있습니다. 통역 시 '스크린도어', '승강장 안전문', '비상정지버튼' 등 안전 설비 용어를 정확히 전달해야 합니다. 한국 역무원이 '승강장 끝'이라고 할 때 베트남어로 'đầu/cuối sân ga'로 구분하며, '승강장 중앙'은 'giữa sân ga'로 표현합니다. 승강장 폭과 승객 동선 설계는 피크 시간대 혼잡도를 고려하므로, 설계 기준을 정확히 통역하는 것이 중요합니다.",
        "commonMistakes": [
            {
                "mistake": "승강장을 'platform'으로만 표현",
                "correction": "sân ga",
                "explanation": "베트남 철도에서 확립된 전문용어"
            },
            {
                "mistake": "섬식 승강장을 'sân ga ở giữa'로 표현",
                "correction": "sân ga đảo 또는 island platform",
                "explanation": "섬식은 기술 용어로 고정된 표현"
            },
            {
                "mistake": "승강장 높이를 'cao sân ga'로만 표현",
                "correction": "chiều cao sân ga (기준 높이 명시)",
                "explanation": "높이는 정확한 수치가 중요한 규격"
            }
        ],
        "examples": [
            {
                "ko": "이 역은 섬식 승강장 구조입니다",
                "vi": "Ga này có cấu trúc sân ga đảo",
                "situation": "formal"
            },
            {
                "ko": "승강장 높이를 1,150mm로 시공하세요",
                "vi": "Thi công chiều cao sân ga là 1.150mm",
                "situation": "onsite"
            },
            {
                "ko": "승강장 안전선 밖으로 나가지 마세요",
                "vi": "Không được ra ngoài vạch an toàn sân ga",
                "situation": "onsite"
            }
        ],
        "relatedTerms": ["스크린도어", "플랫폼", "역사", "대합실", "상대식 승강장"]
    },
    {
        "slug": "nha-ga",
        "korean": "정거장",
        "vietnamese": "Nhà ga",
        "hanja": "停車場",
        "hanjaReading": "停(머무를 정) + 車(수레 차) + 場(마당 장)",
        "pronunciation": "정거장",
        "meaningKo": "철도 차량이 정차하여 승객이 승하차하는 시설 전체를 의미합니다. 통역 시 '역'과 '정거장'은 같은 의미로 사용되나, 공식 문서에서는 '정거장'이 표준 용어입니다. 베트남어로 'nhà ga' 또는 'ga'로 표현하며, 역사 건물만을 가리킬 때는 'tòa nhà ga'로 구분합니다. 현장에서 '종착역', '환승역', '통과역' 등을 구분할 때, 각각 'ga cuối', 'ga chuyển tiếp', 'ga trung gian'으로 번역해야 합니다. 정거장 시설에는 승강장, 대합실, 개찰구, 매표소 등이 포함되므로, 전체 시설을 지칭할 때와 역사 건물만을 지칭할 때를 명확히 구분해야 합니다.",
        "meaningVi": "Toàn bộ cơ sở hạ tầng nơi tàu dừng và hành khách lên xuống, bao gồm sân ga, phòng chờ, cửa soát vé, v.v.",
        "context": "철도 및 지하철역 건설",
        "culturalNote": "한국에서는 '역'이 일반적 표현이지만, 철도 관련 법규와 기술 문서에서는 '정거장'이 공식 용어입니다. 베트남에서는 'ga' 또는 'nhà ga'를 일반적으로 사용하며, 기차역과 지하철역을 구분할 때 'ga xe lửa', 'ga tàu điện ngầm'으로 표현합니다. 한국 지하철역은 복합 시설로 발전하여 쇼핑몰, 환승센터 기능이 통합된 경우가 많으므로, 통역 시 '역사', '역세권 개발', '환승 통로' 등의 개념을 정확히 전달해야 합니다. 정거장 설계 시 승객 동선, 비상 대피로, 환기 시스템 등이 중요하므로, 관련 용어를 숙지해야 합니다.",
        "commonMistakes": [
            {
                "mistake": "정거장을 'trạm'으로 번역",
                "correction": "ga 또는 nhà ga",
                "explanation": "trạm은 버스 정류장, ga는 철도역"
            },
            {
                "mistake": "역과 정거장을 다른 의미로 구분",
                "correction": "같은 의미, 공식 문서에서는 정거장 사용",
                "explanation": "역은 일상어, 정거장은 기술 용어"
            },
            {
                "mistake": "환승역을 'ga thay đổi'로 표현",
                "correction": "ga chuyển tiếp 또는 ga nối",
                "explanation": "환승은 transfer의 의미"
            }
        ],
        "examples": [
            {
                "ko": "이 정거장은 3개 노선이 환승됩니다",
                "vi": "Ga này là điểm chuyển tiếp của 3 tuyến",
                "situation": "formal"
            },
            {
                "ko": "종착 정거장까지 20분 소요됩니다",
                "vi": "Mất 20 phút đến ga cuối",
                "situation": "informal"
            },
            {
                "ko": "정거장 시설물 점검을 실시합니다",
                "vi": "Tiến hành kiểm tra các thiết bị tại ga",
                "situation": "formal"
            }
        ],
        "relatedTerms": ["승강장", "역사", "환승역", "종착역", "대합실"]
    },
    {
        "slug": "duong-chuyen-tiep",
        "korean": "환승통로",
        "vietnamese": "Đường chuyển tiếp",
        "hanja": "換乘通路",
        "hanjaReading": "換(바꿀 환) + 乘(탈 승) + 通(통할 통) + 路(길 로)",
        "pronunciation": "환승통로",
        "meaningKo": "서로 다른 노선을 연결하여 승객이 환승할 수 있도록 만든 통로입니다. 통역 시 '환승통로 길이', '환승 소요시간', '환승 동선'을 정확히 전달해야 합니다. 한국 지하철 설계 기준에서는 환승 소요시간 5분 이내를 목표로 하므로, 베트남어로 'thời gian chuyển tiếp dưới 5 phút'로 표현합니다. 환승통로에는 무빙워크, 에스컬레이터, 엘리베이터가 설치되는 경우가 많으므로, 'thang cuốn', 'thang máy'로 구분해야 합니다. 현장에서 '환승 동선 개선'이라고 하면 승객 흐름을 원활하게 하기 위한 통로 배치 변경을 의미하며, 'cải thiện động tuyến chuyển tiếp'로 번역합니다.",
        "meaningVi": "Lối đi kết nối các tuyến khác nhau để hành khách chuyển tuyến. Thường có thang cuốn, thang máy để rút ngắn thời gian chuyển tiếp.",
        "context": "지하철 환승역 설계 및 시공",
        "culturalNote": "한국 주요 환승역(예: 서울역, 강남역, 홍대입구역)은 복잡한 환승통로로 유명하며, 일부는 500m 이상 걸어야 하는 경우도 있습니다. 베트남 하노이 메트로는 상대적으로 단순한 환승 구조를 가지고 있으므로, 한국 사례를 설명할 때 규모와 복잡도 차이를 명확히 해야 합니다. 환승통로 설계 시 고려 사항으로 '피크 시간대 혼잡도', '장애인 동선', '비상 대피로' 등이 있으며, 각각 'mật độ giờ cao điểm', 'động tuyến người khuyết tật', 'lối thoát hiểm'으로 표현합니다. 통역 시 환승통로의 폭, 경사도, 조명 등 세부 규격을 정확히 전달하는 것이 시공 품질에 중요합니다.",
        "commonMistakes": [
            {
                "mistake": "환승통로를 'đường đi giữa các ga'로 표현",
                "correction": "đường chuyển tiếp 또는 lối chuyển tuyến",
                "explanation": "환승은 transfer의 전문 용어"
            },
            {
                "mistake": "환승 소요시간을 'thời gian đi bộ'로 표현",
                "correction": "thời gian chuyển tiếp",
                "explanation": "환승은 단순 도보가 아닌 시스템 간 이동"
            },
            {
                "mistake": "무빙워크를 'thang máy'로 오역",
                "correction": "băng chuyền đi bộ 또는 moving walkway",
                "explanation": "thang máy는 엘리베이터, 무빙워크는 수평 이동"
            }
        ],
        "examples": [
            {
                "ko": "환승통로에 무빙워크를 설치합니다",
                "vi": "Lắp đặt băng chuyền đi bộ tại đường chuyển tiếp",
                "situation": "formal"
            },
            {
                "ko": "환승 소요시간을 3분으로 단축할 계획입니다",
                "vi": "Kế hoạch rút ngắn thời gian chuyển tiếp xuống 3 phút",
                "situation": "formal"
            },
            {
                "ko": "환승통로가 좁아서 혼잡합니다",
                "vi": "Đường chuyển tiếp hẹp nên đông đúc",
                "situation": "informal"
            }
        ],
        "relatedTerms": ["환승역", "무빙워크", "에스컬레이터", "승강장", "동선"]
    },
    {
        "slug": "cua-chan-san-ga",
        "korean": "스크린도어",
        "vietnamese": "Cửa chắn sân ga",
        "hanja": None,
        "hanjaReading": None,
        "pronunciation": "스크린도어",
        "meaningKo": "승강장과 선로를 분리하여 승객의 안전을 보호하는 자동문입니다. 통역 시 '전면형 스크린도어(PSD)'와 '반높이 스크린도어(PED)'를 구분해야 합니다. 전면형은 천장까지 닫히는 구조로 베트남어로 'cửa chắn toàn phần', 반높이는 허리 높이까지만 설치되어 'cửa chắn bán phần'로 표현합니다. 현장에서 '스크린도어 연동', '비상개방', '센서 오작동' 등의 문제가 발생할 때, 각각 'liên động cửa chắn', 'mở khẩn cấp', 'lỗi cảm biến'로 정확히 통역해야 합니다. 스크린도어는 열차 도어와 정확히 정렬되어야 하므로, 설치 허용오차를 mm 단위로 전달하는 것이 중요합니다.",
        "meaningVi": "Cửa tự động ngăn cách giữa sân ga và đường ray để bảo vệ an toàn hành khách. Có loại toàn phần (PSD) và bán phần (PED).",
        "context": "지하철 승강장 안전 설비",
        "culturalNote": "한국은 2000년대 이후 모든 지하철 신규 노선에 스크린도어를 의무화하였으며, 기존 노선도 점진적으로 설치 중입니다. 베트남 하노이 메트로도 스크린도어를 도입했으나, 일부 구간은 비용 문제로 반높이형을 사용합니다. 통역 시 '전면형'과 '반높이형'의 안전성 차이, 비용 차이를 명확히 설명해야 합니다. 스크린도어 고장 시 수동 개방 절차는 'quy trình mở thủ công'으로 표현하며, 역무원 교육 내용을 정확히 전달하는 것이 비상 상황 대응에 필수적입니다. 스크린도어와 열차 도어의 동기화는 'đồng bộ hóa cửa'로 표현합니다.",
        "commonMistakes": [
            {
                "mistake": "스크린도어를 'cửa tự động'로만 번역",
                "correction": "cửa chắn sân ga 또는 PSD/PED",
                "explanation": "일반 자동문과 구분되는 전문 안전설비"
            },
            {
                "mistake": "전면형을 'cửa đầy đủ'로 표현",
                "correction": "cửa chắn toàn phần (PSD)",
                "explanation": "기술 용어로 확립된 표현"
            },
            {
                "mistake": "비상개방을 'mở khẩn'으로 축약",
                "correction": "mở khẩn cấp 또는 emergency opening",
                "explanation": "안전 절차는 완전한 용어 사용"
            }
        ],
        "examples": [
            {
                "ko": "스크린도어 점검 중이니 잠시 대기하세요",
                "vi": "Đang kiểm tra cửa chắn sân ga, vui lòng đợi một chút",
                "situation": "onsite"
            },
            {
                "ko": "이 역은 전면형 스크린도어를 설치합니다",
                "vi": "Ga này sẽ lắp đặt cửa chắn toàn phần (PSD)",
                "situation": "formal"
            },
            {
                "ko": "스크린도어가 열리지 않으면 비상버튼을 누르세요",
                "vi": "Nếu cửa chắn không mở, nhấn nút khẩn cấp",
                "situation": "informal"
            }
        ],
        "relatedTerms": ["승강장", "안전문", "PSD", "PED", "센서"]
    },
    {
        "slug": "thiet-bi-tin-hieu",
        "korean": "신호설비",
        "vietnamese": "Thiết bị tín hiệu",
        "hanja": "信號設備",
        "hanjaReading": "信(믿을 신) + 號(부를 호) + 設(베풀 설) + 備(갖출 비)",
        "pronunciation": "신호설비",
        "meaningKo": "열차의 안전한 운행을 위해 열차 간 간격, 속도, 진로를 제어하는 설비입니다. 통역 시 '신호기', '궤도회로', 'ATS(자동열차정지장치)', 'ATP(자동열차방호장치)' 등 세부 장치를 구분해야 합니다. 한국 철도는 주로 ATP 시스템을 사용하며, 베트남어로 'hệ thống bảo vệ tàu tự động'으로 표현합니다. 현장에서 '신호 현시', '신호 전환', '신호 고장' 등의 용어가 나올 때, 각각 'hiển thị tín hiệu', 'chuyển đổi tín hiệu', 'sự cố tín hiệu'로 정확히 번역해야 합니다. 신호설비는 열차 안전의 핵심이므로, 오작동 시 즉시 보고하는 절차를 명확히 전달해야 합니다.",
        "meaningVi": "Thiết bị kiểm soát khoảng cách, tốc độ và lộ trình tàu để đảm bảo an toàn vận hành. Bao gồm đèn tín hiệu, mạch ray, ATS, ATP.",
        "context": "철도 신호 및 제어 시스템",
        "culturalNote": "한국 철도는 1990년대부터 전자연동장치와 ATP를 도입하여 자동화 수준이 높지만, 베트남 일부 구간은 여전히 기계식 신호기를 사용합니다. 통역 시 시스템 차이를 명확히 하고, '전자연동'은 'liên động điện tử', '기계식 신호'는 'tín hiệu cơ khí'로 구분해야 합니다. 한국 지하철은 무인 운전(ATO)도 도입되어 있어, 'vận hành tự động không người lái'로 설명할 수 있습니다. 신호설비 점검 시 '열차 운행 중단'이 필요한 경우가 많으므로, 'tạm dừng vận hành tàu'로 사전 공지하는 것이 중요합니다.",
        "commonMistakes": [
            {
                "mistake": "신호설비를 'đèn tín hiệu'로만 번역",
                "correction": "thiết bị tín hiệu (신호기는 그 중 일부)",
                "explanation": "신호설비는 신호기, 제어장치 등 전체 시스템"
            },
            {
                "mistake": "ATS를 'hệ thống dừng tự động'으로 오역",
                "correction": "thiết bị dừng tàu tự động (ATS)",
                "explanation": "ATS는 과속 시 자동 정지 장치"
            },
            {
                "mistake": "신호 현시를 'hiển thị đèn'으로 표현",
                "correction": "hiển thị tín hiệu",
                "explanation": "현시는 신호의 상태 표시"
            }
        ],
        "examples": [
            {
                "ko": "신호설비 점검을 위해 야간 작업을 진행합니다",
                "vi": "Tiến hành làm việc ban đêm để kiểm tra thiết bị tín hiệu",
                "situation": "formal"
            },
            {
                "ko": "ATP 시스템 오작동으로 열차가 정지했습니다",
                "vi": "Tàu dừng do sự cố hệ thống ATP",
                "situation": "onsite"
            },
            {
                "ko": "신호 전환 시간을 단축해야 합니다",
                "vi": "Cần rút ngắn thời gian chuyển đổi tín hiệu",
                "situation": "formal"
            }
        ],
        "relatedTerms": ["신호기", "ATS", "ATP", "궤도회로", "연동장치"]
    },
    {
        "slug": "ket-cau-ha-tang-duong-ray",
        "korean": "궤도하부",
        "vietnamese": "Kết cấu hạ tầng đường ray",
        "hanja": "軌道下部",
        "hanjaReading": "軌(수레 거) + 道(길 도) + 下(아래 하) + 部(부분 부)",
        "pronunciation": "궤도하부",
        "meaningKo": "궤도(레일, 침목, 도상)를 지지하는 하부 구조물로, 노반, 배수시설, 교량, 터널 등을 포함합니다. 통역 시 '노반', '도상', '배수로'를 구분해야 합니다. 노반은 'nền đường', 도상은 'lớp đá ballast', 배수로는 'rãnh thoát nước'로 표현합니다. 현장에서 '궤도하부 침하'는 궤도 아래 지반이 내려앉는 현상으로, 베트남어로 'sụt lún nền đường ray'로 번역합니다. 궤도하부 시공 품질은 열차 안전과 승차감에 직결되므로, '다짐도', '배수 경사' 등의 규격을 정확히 전달하는 것이 중요합니다. 한국 고속철도는 콘크리트 도상(무도상 궤도)을 사용하므로, 'đường ray không ballast'로 설명해야 합니다.",
        "meaningVi": "Cấu trúc phía dưới đỡ đường ray, bao gồm nền đường, lớp đá ballast, hệ thống thoát nước, cầu, hầm.",
        "context": "철도 토목 및 기초 시공",
        "culturalNote": "한국 고속철도(KTX)는 무도상 궤도(콘크리트 슬래브 궤도)를 사용하여 유지보수가 적고 승차감이 우수하지만, 베트남 기존 철도는 유도상 궤도(자갈 도상)를 사용합니다. 통역 시 두 시스템의 차이를 명확히 설명해야 하며, '무도상 궤도'는 'đường ray không ballast' 또는 'slab track', '유도상 궤도'는 'đường ray có ballast' 또는 'ballasted track'로 구분합니다. 궤도하부 침하는 열차 탈선 위험이 있으므로, 'sụt lún'을 발견 즉시 보고하는 절차를 강조해야 합니다. 배수 불량으로 인한 궤도하부 손상은 'hư hỏng do thoát nước kém'으로 표현합니다.",
        "commonMistakes": [
            {
                "mistake": "궤도하부를 'phần dưới đường ray'로만 번역",
                "correction": "kết cấu hạ tầng đường ray",
                "explanation": "하부 구조물 전체를 포함하는 전문용어"
            },
            {
                "mistake": "도상을 'đá'로만 표현",
                "correction": "lớp đá ballast",
                "explanation": "도상은 특정 규격의 자갈층"
            },
            {
                "mistake": "무도상 궤도를 'đường ray không đá'로 표현",
                "correction": "đường ray không ballast 또는 slab track",
                "explanation": "무도상은 콘크리트 슬래브 구조"
            }
        ],
        "examples": [
            {
                "ko": "궤도하부 침하가 발견되어 보수가 필요합니다",
                "vi": "Phát hiện sụt lún nền đường ray, cần sửa chữa",
                "situation": "onsite"
            },
            {
                "ko": "이 구간은 무도상 궤도로 시공됩니다",
                "vi": "Đoạn này sẽ thi công bằng đường ray không ballast",
                "situation": "formal"
            },
            {
                "ko": "배수로가 막혀서 궤도하부가 손상되었습니다",
                "vi": "Rãnh thoát nước bị tắc làm hư hỏng kết cấu hạ tầng đường ray",
                "situation": "onsite"
            }
        ],
        "relatedTerms": ["노반", "도상", "배수로", "무도상 궤도", "침하"]
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

    print(f"기존 용어 수: {len(existing_data)}")

    # 새 용어 추가
    existing_data.extend(data)

    print(f"추가 후 용어 수: {len(existing_data)}")

    # 파일 저장 (들여쓰기 2칸, 유니코드 그대로)
    with open(file_path, "w", encoding="utf-8") as f:
        json.dump(existing_data, f, ensure_ascii=False, indent=2)

    print(f"✅ {len(data)}개 용어 추가 완료")
    print(f"📁 저장 위치: {file_path}")

if __name__ == "__main__":
    main()
