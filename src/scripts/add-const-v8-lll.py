#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
건설 용어 추가 스크립트 - 지하매설물/유틸리티 테마
테마: 가스배관, 통신관로, 전력관로, 상수도관, 하수도관, 공동구, 한전인입, 통신인입, 도시가스인입, 지하매설물탐사
"""

import json
import os

# 추가할 용어 데이터 (10개)
data = [
    {
        "slug": "ong-dan-khi-dot",
        "korean": "가스배관",
        "vietnamese": "Ống dẫn khí đốt",
        "hanja": "gas配管",
        "hanjaReading": None,
        "pronunciation": "가스배관",
        "meaningKo": "도시가스를 공급하기 위한 배관 시설로, PE(폴리에틸렌)관 또는 강관을 주로 사용합니다. 통역 시 '도시가스'는 'khí đốt đô thị', '중압관'은 'đường ống áp lực trung bình', '저압관'은 'đường ống áp lực thấp'로 표현합니다. 가스배관은 폭발 위험이 있어 안전거리 확보가 필수이며, 한국 기준으로 건물 외벽에서 최소 60cm 이격, 다른 매설물과는 30cm 이상 이격해야 합니다. 굴착 시 가스배관 손상은 대형 사고로 이어질 수 있어 탐사 장비로 정확한 위치를 확인한 후 수작업으로 조심스럽게 노출시켜야 하며, 베트남 현장에서는 이러한 안전 절차가 소홀히 되는 경우가 많아 통역사는 위험성을 강조해야 합니다.",
        "meaningVi": "Ống dẫn khí đốt là hệ thống ống cung cấp gas đô thị, chủ yếu dùng ống PE (polyethylene) hoặc ống thép. Ống gas rất nguy hiểm khi thi công, phải giữ khoảng cách an toàn 60cm với tường nhà, 30cm với đường ống khác. Khi đào đất phải dùng máy dò xác định vị trí chính xác và lộ ống bằng tay để tránh nổ.",
        "context": "지하매설물, 안전관리, 굴착공사",
        "culturalNote": "한국은 가스배관 시공과 관리가 법으로 엄격히 규제되며, 가스안전공사의 검사를 필수로 받아야 하고, 배관 색상(노란색)과 표지판 설치가 의무화되어 있습니다. 굴착 공사 전 가스회사에 사전 통보하고 입회하에 작업하는 것이 일반적입니다. 베트남은 도시가스 보급률이 낮고 대부분 LPG 통을 사용하며, 일부 신도시에만 도시가스 배관이 있어 관리 경험이 부족합니다. 한국 기술자는 가스배관을 가장 위험한 매설물로 인식하지만, 베트남 현장에서는 중요도가 상대적으로 낮게 취급되는 경향이 있어 통역 시 안전 기준의 차이를 명확히 전달해야 합니다.",
        "commonMistakes": [
            {
                "mistake": "'가스배관'을 'ống gas'로만 번역",
                "correction": "'ống dẫn khí đốt' 또는 'đường ống gas đô thị' 사용",
                "explanation": "도시가스 공급용 배관임을 명확히 해야 LPG 배관과 구분"
            },
            {
                "mistake": "'중압/저압'을 'cao áp/hạ áp'(고압/저압)로 번역",
                "correction": "'áp lực trung bình/áp lực thấp' 사용",
                "explanation": "가스배관의 압력 등급 체계는 고압/중압/저압으로 구분"
            },
            {
                "mistake": "안전거리를 구체적 수치 없이 '충분히 떨어뜨려라'로 전달",
                "correction": "60cm, 30cm 등 구체적 이격거리 명시",
                "explanation": "안전 기준은 정량적으로 전달해야 준수 가능"
            }
        ],
        "examples": [
            {
                "ko": "이 구역에 중압 가스배관이 매설되어 있으니 굴착 전 가스공사 입회가 필수입니다.",
                "vi": "Khu vực này có ống dẫn khí đốt áp lực trung bình ngầm, bắt buộc phải có đại diện công ty gas giám sát trước khi đào.",
                "situation": "onsite"
            },
            {
                "ko": "가스배관으로부터 최소 60cm 이격하여 전력 케이블을 설치해 주세요.",
                "vi": "Hãy lắp cáp điện cách ống khí đốt tối thiểu 60cm.",
                "situation": "onsite"
            },
            {
                "ko": "굴착 중 PE 가스관이 노출되었으니 즉시 작업 중단하고 가스회사에 연락하세요.",
                "vi": "Phát hiện ống gas PE khi đào, dừng ngay và liên hệ công ty khí đốt.",
                "situation": "onsite"
            }
        ],
        "relatedTerms": ["도시가스", "PE관", "중압관", "지하매설물", "안전이격거리"]
    },
    {
        "slug": "cong-thong-tin-ngam",
        "korean": "통신관로",
        "vietnamese": "Cống thông tin ngầm",
        "hanja": "通信管路",
        "hanjaReading": "通(통할 통) + 信(믿을 신) + 管(대롱 관) + 路(길 로)",
        "pronunciation": "통신관로",
        "meaningKo": "통신 케이블(전화, 인터넷, 광케이블 등)을 보호하고 유지관리하기 위한 지하 관로 시설입니다. 통역 시 '통신관로'는 'cống thông tin ngầm', '맨홀'은 'hố ga thông tin', '핸드홀'은 'hố hand hole'로 표현합니다. 통신관로는 주로 PVC관이나 HDPE관을 사용하며, 50~100mm 직경의 다공(multi-duct)으로 설치하여 향후 증설을 대비합니다. 한국에서는 통신관로 설치 시 통신사(KT, SKT, LG U+ 등)와 협의하여 공동 활용하는 경우가 많으며, 관로 내부에 광케이블, 동축케이블 등을 통과시킵니다. 굴착 시 통신 케이블 절단은 대규모 통신 장애를 유발할 수 있어 주의가 필요합니다.",
        "meaningVi": "Cống thông tin ngầm là hệ thống ống ngầm bảo vệ cáp thông tin (điện thoại, internet, cáp quang). Chủ yếu dùng ống PVC hoặc HDPE đường kính 50-100mm, lắp đặt nhiều ống (multi-duct) để dự phòng mở rộng sau này. Việt Nam thường dùng hố ga thông tin để kéo cáp, cần phối hợp với các nhà mạng khi thi công để tránh cắt cáp gây sự cố.",
        "context": "지하매설물, 통신설비, 인프라",
        "culturalNote": "한국은 통신관로가 체계적으로 관리되며, 각 통신사별로 관로 대장과 준공도면이 잘 정비되어 있어 굴착 전 정확한 위치 파악이 가능합니다. 통신관로는 주로 도로 한쪽에 집약 설치되며, 맨홀 뚜껑에 'T' 또는 '통신' 표시가 있습니다. 베트남은 통신관로가 체계적이지 못하고, 여러 통신사가 개별적으로 케이블을 무분별하게 매설하여 지하가 복잡하며, 도면과 실제 위치가 다른 경우가 많습니다. 한국 현장에서는 통신 케이블 절단 시 배상 책임이 크지만, 베트남은 책임 소재가 불명확한 경우가 많습니다. 통역사는 통신 장애의 사회적 파급력을 강조하여 안전 시공을 유도해야 합니다.",
        "commonMistakes": [
            {
                "mistake": "'통신관로'를 'đường cáp thông tin'(통신 케이블)로 번역",
                "correction": "'cống thông tin ngầm' 또는 'hệ thống ống ngầm thông tin' 사용",
                "explanation": "케이블과 그것을 보호하는 관로는 별개 개념"
            },
            {
                "mistake": "'맨홀'을 'nắp hố'(뚜껑)으로만 번역",
                "correction": "'hố ga thông tin' (통신 맨홀) 사용",
                "explanation": "맨홀은 뚜껑이 아닌 지하 점검구 전체를 지칭"
            },
            {
                "mistake": "관로 직경을 '인치'로만 표기하고 mm 환산 없음",
                "correction": "베트남 기술자에게는 mm 단위 병기 필수",
                "explanation": "베트남은 미터법 사용, 인치 단위에 익숙하지 않음"
            }
        ],
        "examples": [
            {
                "ko": "이 구간에는 KT와 SKT 통신관로가 병렬로 설치되어 있으니 양쪽 모두 확인 필요합니다.",
                "vi": "Đoạn này có cống thông tin KT và SKT song song, cần kiểm tra cả hai bên.",
                "situation": "onsite"
            },
            {
                "ko": "통신 맨홀 위치를 피해서 굴착하되, 부득이하면 맨홀을 이설하겠습니다.",
                "vi": "Đào tránh vị trí hố ga thông tin, nếu không được thì di dời hố ga.",
                "situation": "formal"
            },
            {
                "ko": "광케이블이 통과하는 관로이므로 진동 발생 작업 시 특히 주의하세요.",
                "vi": "Đây là ống có cáp quang nên đặc biệt cẩn thận khi có rung động.",
                "situation": "onsite"
            }
        ],
        "relatedTerms": ["광케이블", "맨홀", "핸드홀", "통신사", "지하매설물"]
    },
    {
        "slug": "cong-cap-dien-ngam",
        "korean": "전력관로",
        "vietnamese": "Cống cáp điện ngầm",
        "hanja": "電力管路",
        "hanjaReading": "電(번개 전) + 力(힘 력) + 管(대롱 관) + 路(길 로)",
        "pronunciation": "전력관로",
        "meaningKo": "전력 케이블을 매설하기 위한 지하 관로 시설로, 고압 전력을 안전하게 공급하는 통로 역할을 합니다. 통역 시 '전력관로'는 'cống cáp điện ngầm', '고압 케이블'은 'cáp cao áp', 'cable duct'는 'ống bảo vệ cáp'로 표현합니다. 전력관로는 주로 PVC 또는 HDPE 재질의 대구경 관(100~200mm)을 사용하며, 전력 케이블은 발열하므로 관 내부에 여유 공간을 두어 통풍이 되도록 설계합니다. 한국에서는 22.9kV 배전선로가 지중화율이 높아 도심지 대부분이 전력관로로 공급되며, 한전(KEPCO)이 통합 관리합니다. 굴착 시 고압 케이블 손상은 감전 사고와 대규모 정전을 유발하므로 반드시 한전 입회하에 작업해야 합니다.",
        "meaningVi": "Cống cáp điện ngầm là hệ thống ống ngầm bảo vệ cáp điện lực, truyền tải điện cao áp an toàn. Dùng ống PVC hoặc HDPE đường kính 100-200mm, phải có khoảng trống bên trong để tản nhiệt vì cáp điện phát nhiệt. Khi đào phải có đại diện điện lực giám sát vì hư cáp cao áp gây tai nạn điện giật và mất điện diện rộng.",
        "context": "지하매설물, 전력설비, 배전",
        "culturalNote": "한국은 전력관로가 한전에 의해 체계적으로 관리되며, 지중 배전 선로 도면이 정확하고, '전력구'(대형 터널형 공동 관로)도 많이 설치되어 있습니다. 전력관로는 빨간색 표지판으로 표시되며, 매설 깊이는 일반적으로 1.2m 이상입니다. 베트남은 전력관로보다 가공 전선(전신주)이 여전히 많으며, 지중 전력 케이블은 주요 도심이나 신도시에만 제한적으로 설치되어 있습니다. 한국 기술자는 전력 케이블을 가스배관만큼 위험하게 인식하지만, 베트남 현장에서는 상대적으로 경시되는 경향이 있습니다. 통역사는 고압 전력의 위험성과 정전 시 사회적 영향을 강조해야 합니다.",
        "commonMistakes": [
            {
                "mistake": "'전력관로'를 'cáp điện ngầm'(지중 전력 케이블)로 번역",
                "correction": "'cống cáp điện ngầm' (전력 케이블 보호 관로) 사용",
                "explanation": "케이블 자체와 그것을 보호하는 관로를 구분"
            },
            {
                "mistake": "'고압'을 'điện áp cao'로만 표기하고 구체적 전압(22.9kV 등) 명시 없음",
                "correction": "전압 등급(22.9kV, 154kV 등) 구체적으로 병기",
                "explanation": "전압 등급에 따라 안전 조치와 작업 방법이 달라짐"
            },
            {
                "mistake": "전력관로와 통신관로를 '지하 케이블'로 통칭",
                "correction": "전력과 통신을 명확히 구분하여 표현",
                "explanation": "위험도와 관리 주체가 다르므로 혼동 방지 필수"
            }
        ],
        "examples": [
            {
                "ko": "이 구간은 22.9kV 고압 케이블이 매설되어 있으니 굴착 전 한전 입회 요청하세요.",
                "vi": "Đoạn này có cáp cao áp 22.9kV ngầm, hãy yêu cầu điện lực giám sát trước khi đào.",
                "situation": "onsite"
            },
            {
                "ko": "전력관로는 최소 1.2m 깊이로 매설되어야 하며, 상부에 보호판을 설치합니다.",
                "vi": "Cống cáp điện phải chôn sâu tối thiểu 1.2m và lắp tấm bảo vệ phía trên.",
                "situation": "formal"
            },
            {
                "ko": "전력 케이블 절단 시 인근 500세대가 정전될 수 있으니 각별히 주의하세요.",
                "vi": "Nếu cắt cáp điện, 500 hộ xung quanh có thể mất điện, phải đặc biệt cẩn thận.",
                "situation": "onsite"
            }
        ],
        "relatedTerms": ["고압 케이블", "한전", "배전선로", "전력구", "지하매설물"]
    },
    {
        "slug": "ong-cap-nuoc",
        "korean": "상수도관",
        "vietnamese": "Ống cấp nước",
        "hanja": "上水道管",
        "hanjaReading": "上(위 상) + 水(물 수) + 道(길 도) + 管(대롱 관)",
        "pronunciation": "상수도관",
        "meaningKo": "깨끗한 물을 공급하기 위한 배관 시설로, 주로 주철관(DIP), PVC관, PE관을 사용합니다. 통역 시 '상수도'는 'cấp nước sạch', '배수관'은 'ống phân phối', '급수관'은 'ống cấp nước'으로 표현합니다. 상수도관은 직경에 따라 본관(DN300 이상), 지선(DN100~300), 급수관(DN100 이하)으로 구분되며, 관 내부는 항상 정압(0.2~0.5MPa)을 유지합니다. 굴착 시 상수도관 손상은 용수 공급 중단과 도로 침수를 유발하므로, 수도 계량기 위치와 제수변(밸브) 위치를 먼저 파악하고, 상수도 사업소 입회하에 작업하는 것이 안전합니다. 한국에서는 상수도관 노후화로 인한 누수 문제가 사회적 이슈이며, 베트남은 수압이 불안정하고 단수가 빈번한 편입니다.",
        "meaningVi": "Ống cấp nước là hệ thống ống dẫn nước sạch, chủ yếu dùng ống gang dẻo (DIP), PVC, PE. Phân loại: ống chính (DN300 trở lên), ống nhánh (DN100-300), ống cấp (dưới DN100). Áp lực trong ống 0.2-0.5MPa. Khi đào đất phải xác định vị trí đồng hồ nước và van khóa trước, có đại diện cấp nước giám sát để tránh vỡ ống gây mất nước và ngập đường.",
        "context": "지하매설물, 상하수도, 급수설비",
        "culturalNote": "한국은 상수도 보급률이 거의 100%이며, 수도관이 정밀하게 관리되고 있어 누수 발생 시 신속한 복구가 이루어집니다. 상수도관은 동파 방지를 위해 동결심도(약 1m) 이하로 매설되며, 내진 설계가 적용됩니다. 베트남은 상수도 보급률이 도시 70%, 농촌 30% 수준이며, 관로 노후화와 수압 부족 문제가 심각합니다. 한국 현장에서는 상수도관 이설 시 수도 사업소의 정식 허가가 필요하지만, 베트남은 절차가 느슨한 편입니다. 통역사는 상수도관 손상 시 주민 불편과 보상 문제를 강조하여 신중한 시공을 유도해야 합니다.",
        "commonMistakes": [
            {
                "mistake": "'상수도관'을 'ống nước'로만 번역",
                "correction": "'ống cấp nước sạch' 또는 'ống cấp nước' 사용",
                "explanation": "하수도관(ống thoát nước)과 명확히 구분 필요"
            },
            {
                "mistake": "관 직경을 '인치'로만 표기",
                "correction": "DN(공칭직경) 표기법 사용 (예: DN150)",
                "explanation": "국제 표준은 DN(Diameter Nominal) 표기법"
            },
            {
                "mistake": "'밸브'를 'van'으로만 번역하고 종류 구분 없음",
                "correction": "제수변(van khóa), 역류방지밸브(van chống ngược) 등 구체적 명칭 사용",
                "explanation": "밸브 종류에 따라 기능과 조작법이 다름"
            }
        ],
        "examples": [
            {
                "ko": "이 상수도 본관은 DN300 주철관으로 수압이 높으니 손상 시 대량 용수 분출 위험이 있습니다.",
                "vi": "Ống cấp nước chính này là ống gang DN300 với áp lực cao, nếu vỡ sẽ phun nước mạnh.",
                "situation": "onsite"
            },
            {
                "ko": "굴착 전 제수변을 잠가서 해당 구간 용수 공급을 차단한 후 작업하세요.",
                "vi": "Trước khi đào, hãy khóa van để cắt cấp nước đoạn đó rồi mới làm việc.",
                "situation": "onsite"
            },
            {
                "ko": "상수도관 매설 깊이는 동결심도 이하인 1.2m로 계획되었습니다.",
                "vi": "Độ sâu chôn ống cấp nước được thiết kế 1.2m, dưới độ sâu đóng băng.",
                "situation": "formal"
            }
        ],
        "relatedTerms": ["급수관", "배수관", "제수변", "동결심도", "지하매설물"]
    },
    {
        "slug": "ong-thoat-nuoc",
        "korean": "하수도관",
        "vietnamese": "Ống thoát nước",
        "hanja": "下水道管",
        "hanjaReading": "下(아래 하) + 水(물 수) + 道(길 도) + 管(대롱 관)",
        "pronunciation": "하수도관",
        "meaningKo": "오수와 우수를 배출하기 위한 배관 시설로, 주로 콘크리트관(흄관), PVC관, HDPE관을 사용합니다. 통역 시 '하수도'는 'thoát nước thải', '오수관'은 'ống nước thải', '우수관'은 'ống thoát nước mưa'로 구분합니다. 하수도관은 합류식(오수+우수 통합)과 분류식(오수/우수 분리)으로 나뉘며, 한국 신도시는 대부분 분류식을 채택합니다. 하수도관은 중력 배수 방식으로 기울기(보통 1/100~1/200)를 주어 설치하며, 맨홀 간격은 50~100m마다 설치하여 유지관리가 가능하도록 합니다. 굴착 시 하수관 손상은 악취와 오염수 누출을 유발하므로 신속한 복구가 필요합니다.",
        "meaningVi": "Ống thoát nước là hệ thống ống dẫn nước thải và nước mưa, chủ yếu dùng ống bê tông (hume), PVC, HDPE. Phân loại: hệ thống hợp lưu (nước thải + mưa chung) và phân lưu (tách riêng). Ống thoát nước lắp có độ dốc 1/100~1/200 để nước chảy tự nhiên, cứ 50-100m có một hố ga để bảo trì. Nếu vỡ ống sẽ có mùi hôi và nước thải tràn ra.",
        "context": "지하매설물, 상하수도, 배수설비",
        "culturalNote": "한국은 하수도 보급률이 95% 이상이며, 하수 처리장으로 모두 연결되어 환경 오염을 방지합니다. 하수관은 내구성과 내부식성이 중요하여 PVC나 PE 재질을 많이 사용하며, 대구경 간선은 콘크리트 흄관을 사용합니다. 베트남은 하수도 보급률이 도시 50%, 농촌 10% 수준으로 낮으며, 많은 지역이 개별 정화조나 직접 하천 방류 방식을 사용합니다. 한국 현장에서는 하수관 파손 시 환경 오염 문제로 즉시 복구하지만, 베트남은 복구가 지연되는 경우가 많습니다. 통역사는 하수관 손상의 위생 및 환경 문제를 강조하여 안전 시공을 유도해야 합니다.",
        "commonMistakes": [
            {
                "mistake": "'하수도관'을 'ống nước bẩn'(더러운 물 배관)으로 번역",
                "correction": "'ống thoát nước thải' 사용",
                "explanation": "'nước bẩn'은 비공식적 표현, 기술 용어는 'nước thải'"
            },
            {
                "mistake": "오수관과 우수관을 구분하지 않고 '하수관'으로 통칭",
                "correction": "'ống nước thải'(오수관)와 'ống nước mưa'(우수관) 명확히 구분",
                "explanation": "분류식 하수도에서는 두 관이 별도로 설치됨"
            },
            {
                "mistake": "관 기울기를 '퍼센트'로 표기",
                "correction": "'1/100' 또는 '1%' 병기 (베트남은 1/100 표기 선호)",
                "explanation": "기울기 표기법은 국가별로 관행이 다름"
            }
        ],
        "examples": [
            {
                "ko": "이 구간은 분류식 하수도로 오수관과 우수관이 별도로 설치되어 있습니다.",
                "vi": "Đoạn này là hệ thống thoát nước phân lưu, có ống nước thải và ống nước mưa riêng biệt.",
                "situation": "formal"
            },
            {
                "ko": "하수관은 1/150 기울기로 설치하여 자연 유하가 되도록 해 주세요.",
                "vi": "Ống thoát nước lắp với độ dốc 1/150 để nước chảy tự nhiên.",
                "situation": "formal"
            },
            {
                "ko": "하수 맨홀에서 악취가 나므로 작업자는 마스크 착용이 필수입니다.",
                "vi": "Hố ga nước thải có mùi hôi nên công nhân phải đeo khẩu trang.",
                "situation": "onsite"
            }
        ],
        "relatedTerms": ["오수관", "우수관", "맨홀", "흄관", "지하매설물"]
    },
    {
        "slug": "cong-dong-tien-ich",
        "korean": "공동구",
        "vietnamese": "Cống đồng tiện ích",
        "hanja": "共同溝",
        "hanjaReading": "共(한가지 공) + 同(한가지 동) + 溝(도랑 구)",
        "pronunciation": "공동구",
        "meaningKo": "전력, 통신, 상하수도, 가스 등 각종 매설물을 하나의 대형 지하 터널에 통합 수용하는 시설로, 'utility tunnel' 또는 'common utility duct'라고도 합니다. 통역 시 '공동구'는 'cống đồng tiện ích' 또는 'hầm tiện ích chung'으로 표현하며, 단순 배관이 아닌 사람이 들어가 유지보수할 request 공간임을 강조해야 합니다. 공동구는 폭 2~4m, 높이 2~3m의 터널 형태로, 내부에 조명, 환기, 배수 시설을 갖추고 있으며, 각 매설물별로 구획된 선반(rack)에 정돈되어 설치됩니다. 한국에서는 대도시 주요 간선도로와 신도시에 공동구가 많이 설치되어 있어 도로 굴착을 최소화하고, 매설물 유지보수가 용이합니다.",
        "meaningVi": "Cống đồng tiện ích là hầm ngầm lớn chứa chung nhiều loại đường ống: điện, thông tin, cấp thoát nước, gas. Có dạng hầm rộng 2-4m, cao 2-3m, người vào được để bảo trì. Bên trong có đèn, thông gió, thoát nước, các đường ống được sắp xếp ngăn nắp trên giá đỡ. Giúp giảm đào đường và bảo trì dễ dàng.",
        "context": "지하 인프라, 도시계획, 유지관리",
        "culturalNote": "한국은 1990년대부터 공동구 건설이 본격화되어 서울, 부산 등 대도시 주요 도로에 광범위하게 설치되어 있으며, 공동구법으로 체계적으로 관리됩니다. 공동구 내부는 CCTV, 센서로 24시간 모니터링되며, 화재·침수 등 비상 상황에 대비한 안전 시스템을 갖추고 있습니다. 베트남은 공동구 개념이 생소하며, 하노이와 호치민 일부 신도시에만 시범적으로 도입되었고, 대부분 지역은 매설물이 개별 매설되어 있습니다. 한국 기술자는 공동구를 선진 인프라로 인식하지만, 베트남 발주처는 초기 투자 비용이 높아 도입을 꺼리는 경향이 있습니다. 통역사는 공동구의 장기적 경제성과 유지보수 편의성을 설명해야 합니다.",
        "commonMistakes": [
            {
                "mistake": "'공동구'를 'ống chung'(공용 배관)으로 번역",
                "correction": "'cống đồng tiện ích' 또는 'hầm tiện ích chung' 사용",
                "explanation": "공동구는 단순 배관이 아닌 사람이 들어갈 수 있는 터널 구조물"
            },
            {
                "mistake": "공동구와 전력구를 혼동하여 사용",
                "correction": "전력구(hầm cáp điện)는 전력만, 공동구는 모든 매설물 수용",
                "explanation": "공동구가 더 포괄적인 개념"
            },
            {
                "mistake": "공동구 크기를 '배관 직경'으로 표현",
                "correction": "터널 단면(폭×높이)으로 표현 (예: 2.5m×2.2m)",
                "explanation": "공동구는 사람이 통행하는 공간이므로 터널 크기로 표기"
            }
        ],
        "examples": [
            {
                "ko": "이 도로는 공동구가 설치되어 있어 향후 매설물 증설 시 도로 굴착이 불필요합니다.",
                "vi": "Con đường này có cống đồng tiện ích nên sau này mở rộng đường ống không cần đào đường.",
                "situation": "formal"
            },
            {
                "ko": "공동구 내부는 환기 시스템이 있어 작업자가 안전하게 점검할 수 있습니다.",
                "vi": "Bên trong cống đồng có hệ thống thông gió nên công nhân kiểm tra an toàn.",
                "situation": "formal"
            },
            {
                "ko": "공동구 출입구는 50m마다 설치되며, 비상 시 대피로로 활용됩니다.",
                "vi": "Cửa vào cống đồng lắp cứ 50m, dùng làm lối thoát hiểm khi khẩn cấp.",
                "situation": "formal"
            }
        ],
        "relatedTerms": ["전력구", "지하매설물", "유틸리티", "인프라", "유지보수"]
    },
    {
        "slug": "dau-noi-dien-luc",
        "korean": "한전인입",
        "vietnamese": "Đấu nối điện lực",
        "hanja": "韓電引入",
        "hanjaReading": "韓(나라이름 한) + 電(번개 전) + 引(끌 인) + 入(들 입)",
        "pronunciation": "한전인입",
        "meaningKo": "한국전력공사(KEPCO)의 배전 선로에서 건물로 전력을 끌어들이는 인입 공사를 의미하며, 'electric service connection' 또는 'power supply connection'이라고도 합니다. 통역 시 '한전인입'은 'đấu nối điện lực' 또는 'kéo điện vào công trình'으로 표현하며, '인입선'은 'đường dây dẫn vào', '인입개폐기'는 'tủ cắt điện đầu vào'로 번역합니다. 한전인입은 한전의 정식 허가와 시공이 필요하며, 인입 용량(kVA)에 따라 단상(220V) 또는 3상(380V) 방식이 결정됩니다. 베트남에서는 전력공사(EVN)에서 동일한 역할을 하며, 'đấu nối lưới điện'이라는 표현도 사용됩니다.",
        "meaningVi": "Đấu nối điện lực là công tác kéo điện từ lưới điện của công ty điện lực (KEPCO ở Hàn Quốc, EVN ở Việt Nam) vào công trình xây dựng. Cần có giấy phép chính thức và thi công bởi điện lực. Tùy công suất (kVA) mà dùng điện 1 pha (220V) hoặc 3 pha (380V). Có đường dây dẫn vào và tủ cắt điện đầu vào.",
        "context": "전력설비, 건축공사, 인프라",
        "culturalNote": "한국은 한전인입이 체계적으로 관리되며, 신청부터 준공까지 약 2~4주 소요되고, 모든 절차가 온라인으로 가능합니다. 한전은 인입 공사비를 고객 부담 원칙으로 하되, 일정 거리(20m) 이내는 무상 지원합니다. 공사 완료 후 한전 검사에 합격해야 전력 공급이 시작됩니다. 베트남은 EVN 인입 절차가 복잡하고 시간이 오래 걸리며(1~3개월), 인입 거리가 멀면 고객이 전봇대 설치 비용까지 부담해야 하는 경우가 많습니다. 한국 기술자는 한전인입을 단순 행정 절차로 인식하지만, 베트남에서는 프로젝트 일정에 큰 영향을 미치는 중요 변수입니다. 통역사는 인입 절차의 소요 기간과 비용을 사전에 명확히 해야 합니다.",
        "commonMistakes": [
            {
                "mistake": "'한전'을 'điện lực Hàn Quốc'로 직역",
                "correction": "'KEPCO' 그대로 사용하거나 'công ty điện lực'로 일반화",
                "explanation": "베트남에서는 한국 기업명보다 기능(전력회사)으로 이해하는 것이 효과적"
            },
            {
                "mistake": "'인입'을 'vào'(들어오다)로만 번역",
                "correction": "'đấu nối' (연결) 또는 'kéo điện vào' (전기 끌어들임) 사용",
                "explanation": "인입은 단순 진입이 아닌 전력 연결 공사"
            },
            {
                "mistake": "인입 용량을 'W'(와트)로만 표기",
                "correction": "'kVA' (킬로볼트암페어) 단위 사용",
                "explanation": "전력 인입 용량은 kVA로 표기하는 것이 국제 표준"
            }
        ],
        "examples": [
            {
                "ko": "이 현장은 100kVA 용량으로 한전인입 신청을 완료했으며, 2주 후 공급 예정입니다.",
                "vi": "Công trường này đã hoàn thành đăng ký đấu nối điện 100kVA, dự kiến cấp điện sau 2 tuần.",
                "situation": "formal"
            },
            {
                "ko": "한전인입 위치는 건물 외벽에서 가장 가까운 전봇대로 결정됩니다.",
                "vi": "Vị trí đấu nối điện được quyết định ở cột điện gần tường nhà nhất.",
                "situation": "formal"
            },
            {
                "ko": "임시 전력은 30kVA로 인입하고, 준공 후 정식 인입으로 전환하겠습니다.",
                "vi": "Điện tạm thời kéo vào 30kVA, sau khi hoàn công sẽ chuyển sang đấu nối chính thức.",
                "situation": "onsite"
            }
        ],
        "relatedTerms": ["전력 인입", "인입선", "한전", "배전", "전력 용량"]
    },
    {
        "slug": "dau-noi-thong-tin",
        "korean": "통신인입",
        "vietnamese": "Đấu nối thông tin",
        "hanja": "通信引入",
        "hanjaReading": "通(통할 통) + 信(믿을 신) + 引(끌 인) + 入(들 입)",
        "pronunciation": "통신인입",
        "meaningKo": "통신사(KT, SKT, LG U+ 등)의 통신망에서 건물로 통신 회선을 끌어들이는 인입 공사를 의미하며, 'telecommunication service connection'이라고도 합니다. 통역 시 '통신인입'은 'đấu nối thông tin' 또는 'kéo cáp thông tin vào', '광케이블 인입'은 'đấu nối cáp quang'으로 표현합니다. 통신인입은 전화, 인터넷, CCTV 등을 위한 필수 인프라이며, 최근에는 광케이블(fiber optic) 인입이 표준입니다. 건물 외벽에 통신 인입함(telecommunication inlet box)을 설치하고, 여기서 건물 내부 MDF(main distribution frame)까지 연결합니다. 베트남에서도 VNPT, Viettel, FPT 등 통신사가 동일한 서비스를 제공합니다.",
        "meaningVi": "Đấu nối thông tin là công tác kéo đường truyền thông tin từ mạng lưới nhà mạng (KT, SKT, LG U+ ở Hàn Quốc / VNPT, Viettel, FPT ở Việt Nam) vào tòa nhà. Hiện nay chủ yếu là đấu nối cáp quang (fiber optic) phục vụ điện thoại, internet, camera. Lắp hộp đấu nối thông tin ở tường ngoài, từ đó dẫn vào tủ phân phối chính (MDF) trong nhà.",
        "context": "통신설비, 건축공사, 인프라",
        "culturalNote": "한국은 통신인입이 매우 신속하며, 신청 후 1~2주 이내에 설치되고, 여러 통신사 중 선택이 가능합니다. 아파트나 오피스텔은 입주 전 통신 3사 인입이 모두 완료되어 입주자가 원하는 통신사를 선택할 수 있습니다. 통신인입 공사는 대부분 무상이며, 통신사가 비용을 부담합니다. 베트남은 통신인입 절차가 다소 복잡하고, 인입 비용을 고객이 일부 부담하는 경우가 있으며, 통신사별로 커버리지가 다릅니다. 한국 기술자는 통신인입을 당연한 기본 인프라로 인식하지만, 베트남 현장에서는 통신사 선정과 인입 일정 조율이 필요합니다. 통역사는 통신인입의 중요성과 프로젝트 일정 영향을 사전에 공유해야 합니다.",
        "commonMistakes": [
            {
                "mistake": "'통신인입'을 'lắp đặt internet'(인터넷 설치)로만 번역",
                "correction": "'đấu nối thông tin' 사용 (전화·인터넷·CCTV 모두 포함)",
                "explanation": "통신인입은 인터넷뿐 아니라 모든 통신 서비스 인입"
            },
            {
                "mistake": "'광케이블'을 'cáp sợi'(섬유 케이블)로 직역",
                "correction": "'cáp quang' 또는 'cáp fiber optic' 사용",
                "explanation": "'cáp quang'은 베트남 통신 업계 표준 용어"
            },
            {
                "mistake": "통신인입함을 '박스'로만 표현",
                "correction": "'hộp đấu nối thông tin' 또는 'tủ telecom' 사용",
                "explanation": "정식 명칭 사용이 혼동 방지에 효과적"
            }
        ],
        "examples": [
            {
                "ko": "이 건물은 KT, SKT, LG U+ 3개 통신사 광케이블이 모두 인입되어 입주자가 선택할 수 있습니다.",
                "vi": "Tòa nhà này đã đấu nối cáp quang của 3 nhà mạng KT, SKT, LG U+ để người vào ở lựa chọn.",
                "situation": "formal"
            },
            {
                "ko": "통신인입함은 1층 외벽에 설치하고, 여기서 각 층 MDF로 분배합니다.",
                "vi": "Hộp đấu nối thông tin lắp ở tường ngoài tầng 1, từ đây phân phối đến MDF các tầng.",
                "situation": "formal"
            },
            {
                "ko": "통신인입 공사는 통신사에서 무상으로 진행하니 준공 전에 신청해 주세요.",
                "vi": "Công tác đấu nối thông tin do nhà mạng làm miễn phí, hãy đăng ký trước khi hoàn công.",
                "situation": "onsite"
            }
        ],
        "relatedTerms": ["광케이블", "통신사", "MDF", "통신 인입함", "인프라"]
    },
    {
        "slug": "dau-noi-khi-dot-do-thi",
        "korean": "도시가스인입",
        "vietnamese": "Đấu nối khí đốt đô thị",
        "hanja": "都市gas引入",
        "hanjaReading": None,
        "pronunciation": "도시가스인입",
        "meaningKo": "도시가스 공급 배관에서 건물로 가스를 끌어들이는 인입 공사를 의미하며, 'city gas service connection'이라고도 합니다. 통역 시 '도시가스인입'은 'đấu nối khí đốt đô thị', '가스 계량기'는 'đồng hồ gas', '중압 인입'은 'đấu nối áp lực trung bình'으로 표현합니다. 도시가스인입은 가스 안전 규정이 매우 엄격하여 반드시 가스공사 또는 도시가스 회사(서울도시가스, 삼천리, 대성에너지 등)의 시공과 검사를 받아야 하며, PE관 용접 및 기밀 시험이 필수입니다. 건물 외벽에 가스 계량기함을 설치하고, 내부로 저압 가스를 공급합니다. 베트남은 도시가스 보급률이 낮아 대부분 LPG 통을 사용하며, 일부 신도시에만 도시가스가 공급됩니다.",
        "meaningVi": "Đấu nối khí đốt đô thị là công tác kéo gas từ đường ống gas đô thị vào tòa nhà. Quy định an toàn rất nghiêm ngặt, phải do công ty gas thi công và kiểm tra, hàn ống PE và thử kín bắt buộc. Lắp hộp đồng hồ gas ở tường ngoài, cấp gas áp lực thấp vào trong nhà. Việt Nam tỷ lệ dùng gas đô thị thấp, chủ yếu dùng bình LPG, chỉ một số khu đô thị mới có gas đường ống.",
        "context": "가스설비, 건축공사, 인프라",
        "culturalNote": "한국은 도시가스 보급률이 80% 이상으로 매우 높으며, 아파트와 주택 대부분이 도시가스를 사용합니다. 도시가스 인입은 가스안전공사의 엄격한 검사를 거쳐야 하며, 배관 용접사는 자격증 소지자만 작업할 수 있습니다. 가스 계량기는 검침이 용이하도록 외벽에 노출 설치하는 것이 일반적입니다. 베트남은 도시가스 보급률이 10% 미만이며, 하노이와 호치민의 일부 신도시 지역에만 제한적으로 공급됩니다. 대부분 가정은 LPG 통을 사용하며, 도시가스 개념 자체가 생소한 경우가 많습니다. 한국 기술자는 도시가스를 당연한 인프라로 인식하지만, 베트남 현장에서는 도시가스 가용 여부를 사전에 확인해야 합니다.",
        "commonMistakes": [
            {
                "mistake": "'도시가스'를 'gas trong thành phố'로 직역",
                "correction": "'khí đốt đô thị' 또는 'gas đường ống' 사용",
                "explanation": "'khí đốt đô thị'는 공식 용어이며, 'gas đường ống'도 이해 용이"
            },
            {
                "mistake": "도시가스와 LPG를 'gas'로 통칭",
                "correction": "도시가스(khí đốt đô thị)와 LPG(gas chai/bình gas) 명확히 구분",
                "explanation": "두 가스는 공급 방식과 압력, 성분이 완전히 다름"
            },
            {
                "mistake": "'계량기함'을 'hộp'(박스)으로만 번역",
                "correction": "'hộp đồng hồ gas' 또는 'tủ đồng hồ khí đốt' 사용",
                "explanation": "용도가 명확한 정식 명칭 사용"
            }
        ],
        "examples": [
            {
                "ko": "이 아파트 단지는 중압 도시가스를 인입하여 각 세대에 저압으로 공급합니다.",
                "vi": "Khu chung cư này đấu nối khí đốt áp lực trung bình, cấp áp lực thấp cho từng hộ.",
                "situation": "formal"
            },
            {
                "ko": "도시가스인입 공사는 가스안전공사 검사 합격 후 사용 가능합니다.",
                "vi": "Công trình đấu nối gas chỉ sử dụng được sau khi kiểm tra an toàn gas thông qua.",
                "situation": "formal"
            },
            {
                "ko": "가스 계량기함은 외벽 1층에 설치하여 검침이 용이하도록 합니다.",
                "vi": "Hộp đồng hồ gas lắp ở tường ngoài tầng 1 để tiện đọc số.",
                "situation": "onsite"
            }
        ],
        "relatedTerms": ["도시가스", "LPG", "가스 계량기", "PE관", "인프라"]
    },
    {
        "slug": "tham-do-duong-ong-ngam",
        "korean": "지하매설물탐사",
        "vietnamese": "Thăm dò đường ống ngầm",
        "hanja": "地下埋設物探査",
        "hanjaReading": "地(땅 지) + 下(아래 하) + 埋(묻을 매) + 設(베풀 설) + 物(물건 물) + 探(찾을 탐) + 査(살필 사)",
        "pronunciation": "지하매설물탐사",
        "meaningKo": "지중에 매설된 각종 매설물(전력, 통신, 가스, 상하수도 등)의 위치와 깊이를 탐지하는 작업으로, 'underground utility detection' 또는 'utility locating'이라고도 합니다. 통역 시 '지하매설물탐사'는 'thăm dò đường ống ngầm' 또는 'khảo sát vật chôn ngầm', '탐사 장비'는 'máy dò đường ống', '전자파 탐지'는 'phát hiện sóng điện từ'로 표현합니다. 탐사 장비로는 전자기 유도식(금속 배관용), 지중 레이더(GPR, 비금속 배관용), 음파 탐지기 등을 사용하며, 탐사 결과는 평면도에 표시하여 굴착 계획에 반영합니다. 한국에서는 굴착 공사 전 지하매설물탐사를 법적으로 의무화하고 있으며, 미시행 시 사고 발생 시 책임이 가중됩니다.",
        "meaningVi": "Thăm dò đường ống ngầm là công tác phát hiện vị trí và độ sâu các vật chôn ngầm (điện, thông tin, gas, nước) bằng thiết bị chuyên dụng. Dùng máy dò sóng điện từ (cho ống kim loại), radar xuyên đất GPR (cho ống phi kim loại), máy dò âm thanh. Kết quả đánh dấu trên bản vẽ mặt bằng để lập kế hoạch đào đất. Ở Hàn Quốc bắt buộc phải thăm dò trước khi đào, nếu không làm sẽ chịu trách nhiệm nặng khi có sự cố.",
        "context": "굴착공사, 안전관리, 지하매설물",
        "culturalNote": "한국은 지하매설물탐사를 매우 중시하며, 전문 탐사 업체가 많고 탐사 기술이 발달했습니다. 굴착 허가 신청 시 반드시 탐사 결과를 첨부해야 하며, 주요 매설물 관리 기관(한전, 가스공사, 수도사업소, 통신사)에 사전 협의하여 도면을 받습니다. 탐사 후에도 시험 굴착(test pit)을 통해 실제 위치를 재확인하는 것이 일반적입니다. 베트남은 지하매설물 관리가 체계적이지 못하고, 도면이 부정확하거나 없는 경우가 많아 탐사의 중요성이 더욱 큽니다. 하지만 탐사 비용 절감을 위해 생략하는 경우가 많아 사고 위험이 높습니다. 통역사는 탐사 비용보다 사고 발생 시 손실이 훨씬 크다는 점을 강조해야 합니다.",
        "commonMistakes": [
            {
                "mistake": "'탐사'를 'tìm kiếm'(찾기)으로 번역",
                "correction": "'thăm dò' 또는 'khảo sát' 사용",
                "explanation": "'thăm dò'는 기술적 탐지, 'tìm kiếm'은 일반적 찾기"
            },
            {
                "mistake": "'GPR'을 번역하지 않고 약어만 사용",
                "correction": "'radar xuyên đất GPR' 또는 'Ground Penetrating Radar' 병기",
                "explanation": "베트남 현장에서는 GPR이 생소할 수 있어 풀네임 필요"
            },
            {
                "mistake": "탐사 결과를 '구두'로만 전달",
                "correction": "평면도에 색깔별로 표시하여 문서화",
                "explanation": "시각적 자료가 굴착 작업자의 이해도를 높임"
            }
        ],
        "examples": [
            {
                "ko": "굴착 전 지하매설물탐사를 실시하여 전력 케이블과 가스배관 위치를 확인했습니다.",
                "vi": "Trước khi đào đã thăm dò đường ống ngầm, xác định vị trí cáp điện và ống gas.",
                "situation": "formal"
            },
            {
                "ko": "GPR 탐사 결과 GL-1.5m에 콘크리트관이 탐지되었으니 수작업으로 노출시키세요.",
                "vi": "Kết quả GPR phát hiện ống bê tông ở GL-1.5m, hãy lộ ra bằng tay.",
                "situation": "onsite"
            },
            {
                "ko": "탐사 장비로도 확인이 어려운 구간은 시험 굴착으로 실제 위치를 파악하겠습니다.",
                "vi": "Đoạn khó xác định bằng máy dò sẽ đào thử để biết vị trí thực tế.",
                "situation": "onsite"
            }
        ],
        "relatedTerms": ["GPR", "전자기 탐지", "시험 굴착", "매설물 도면", "안전관리"]
    }
]

def main():
    # 파일 경로 설정
    file_path = os.path.join(
        os.path.dirname(os.path.abspath(__file__)),
        '..',
        'data',
        'terms',
        'construction.json'
    )

    # 기존 데이터 읽기
    with open(file_path, 'r', encoding='utf-8') as f:
        existing_data = json.load(f)

    print(f"기존 용어 수: {len(existing_data)}")

    # 새 용어 추가
    existing_data.extend(data)

    print(f"추가 후 용어 수: {len(existing_data)}")

    # 파일에 저장
    with open(file_path, 'w', encoding='utf-8') as f:
        json.dump(existing_data, f, ensure_ascii=False, indent=2)

    print(f"✅ {len(data)}개 용어가 추가되었습니다.")
    print("\n추가된 용어:")
    for term in data:
        print(f"  - {term['korean']} ({term['vietnamese']})")

if __name__ == "__main__":
    main()
