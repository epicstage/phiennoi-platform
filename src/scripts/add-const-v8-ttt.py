#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Construction Surveying Terms Addition Script v8
Theme: Civil Engineering Surveying (토목측량상세)
- 기준점, 수준점, 삼각점, 종단측량, 횡단측량
- 지형측량, 평판측량, 토탈스테이션, GNSS, 라이다
Total: 10 terms, Tier S compliant
"""

import json
import os

# Tier S 품질 기준: 모든 필드 필수, meaningKo 200자+, culturalNote 100자+, examples/commonMistakes/relatedTerms 3개+
data = [
    {
        "slug": "diem-khong-che",
        "korean": "기준점",
        "vietnamese": "điểm khống chế",
        "hanja": "基準點",
        "hanjaReading": "기(기초 기) + 준(기준 준) + 점(점 점)",
        "pronunciation": "디엠 콩 체",
        "meaningKo": "측량 작업의 기준이 되는 좌표가 명확히 정해진 고정점으로, 삼각점·수준점·다각점 등이 포함됩니다. 국토지리정보원이 설치·관리하며, 모든 토목측량은 이 기준점을 기초로 수행됩니다. 통역 시 주의할 점은 베트남에서는 VN2000 좌표계, 한국은 세계측지계(GRS80 타원체)를 사용하므로 좌표 변환이 필수입니다. 또한 기준점 훼손 시 법적 책임이 있어 보호 의무를 강조해야 합니다.",
        "meaningVi": "Điểm cố định có tọa độ xác định rõ ràng, làm cơ sở cho công tác đo đạc, bao gồm điểm tam giác, điểm cao độ, điểm đa giác. Do Cục Thông tin Đất đai Quốc gia thiết lập và quản lý, mọi công tác đo đạc dân dụng đều dựa trên điểm khống chế này.",
        "context": "토목측량, 공사측량 기준",
        "contextVi": "Đo đạc dân dụng, cơ sở đo đạc công trình",
        "commonMistakes": [
            {
                "mistake": "\"기준점\"을 \"điểm chuẩn\"으로 번역",
                "correction": "\"điểm khống chế\"가 정확한 측량 전문용어",
                "explanation": "điểm chuẩn은 일반적 기준점, điểm khống chế는 측지학적 기준점을 의미"
            },
            {
                "mistake": "좌표계 차이를 언급하지 않고 수치만 통역",
                "correction": "VN2000 vs 세계측지계 차이를 명시",
                "explanation": "좌표계가 다르면 같은 수치도 다른 위치를 가리킬 수 있음"
            },
            {
                "mistake": "기준점 보호 의무를 단순 주의사항으로 전달",
                "correction": "법적 처벌 대상임을 강조",
                "explanation": "측량법상 기준점 훼손은 형사처벌 대상"
            }
        ],
        "culturalNote": "한국은 국가기준점이 매우 정밀하게 관리되며 GPS 상시관측소 네트워크가 촘촘합니다. 베트남은 지역에 따라 기준점 밀도 차이가 크고, 일부 산간지역은 기준점 접근이 어렵습니다. 한국 현장에서는 기준점 사용 전 반드시 점검측량을 하며, 베트남보다 정확도 허용오차가 엄격합니다.",
        "examples": [
            {
                "ko": "기준점 측량 성과를 확인한 후 공사측량을 시작하세요.",
                "vi": "Sau khi kiểm tra thành quả đo điểm khống chế, hãy bắt đầu đo đạc công trình.",
                "situation": "formal"
            },
            {
                "ko": "이 기준점 좌표 맞아? 옆 현장이랑 안 맞는데.",
                "vi": "Tọa độ điểm khống chế này đúng không? Không khớp với công trường bên cạnh.",
                "situation": "onsite"
            },
            {
                "ko": "국토지리정보원 홈페이지에서 기준점 성과를 조회할 수 있습니다.",
                "vi": "Có thể tra cứu thành quả điểm khống chế trên trang web Cục Thông tin Đất đai Quốc gia.",
                "situation": "formal"
            }
        ],
        "relatedTerms": [
            "삼각점",
            "수준점",
            "세계측지계"
        ]
    },
    {
        "slug": "diem-cao-do",
        "korean": "수준점",
        "vietnamese": "điểm cao độ",
        "hanja": "水準點",
        "hanjaReading": "수(물 수) + 준(기준 준) + 점(점 점)",
        "pronunciation": "디엠 까오 도",
        "meaningKo": "표고(해발고도)가 정확히 결정된 측량 기준점으로, 건축물·도로·상하수도 등의 높이 기준이 됩니다. 레벨측량을 통해 다른 지점의 표고를 산정하며, 1·2·3·4등 수준점으로 등급이 나뉩니다. 통역 시 주의점은 한국은 인천 평균해수면 기준(m), 베트nam은 Hon Dau 기준이므로 표고 기준면이 다릅니다. 또한 수준점 표석은 지반 침하나 융기를 감지하는 중요 자료이므로 보호가 필수입니다.",
        "meaningVi": "Điểm chuẩn đo đạc có độ cao (cao độ so với mực nước biển) được xác định chính xác, làm cơ sở độ cao cho công trình, đường, cấp thoát nước. Qua đo thủy chuẩn xác định cao độ các điểm khác, chia thành điểm cao độ hạng 1, 2, 3, 4.",
        "context": "레벨측량, 표고 기준",
        "contextVi": "Đo thủy chuẩn, cơ sở cao độ",
        "commonMistakes": [
            {
                "mistake": "\"수준점\"을 \"điểm ngang\"으로 번역",
                "correction": "\"điểm cao độ\" 또는 \"mốc cao độ\"가 정확",
                "explanation": "điểm ngang은 수평점을 의미, 수준점은 cao độ(표고)를 나타냄"
            },
            {
                "mistake": "표고 기준면 차이를 설명하지 않음",
                "correction": "인천 평균해수면 vs Hon Dau 기준 차이 명시",
                "explanation": "기준면이 다르면 같은 표고 수치도 실제 높이가 다름"
            },
            {
                "mistake": "수준점 등급(1~4등)을 단순 숫자로만 통역",
                "correction": "정확도·용도 차이를 함께 설명",
                "explanation": "1등 수준점(±0.5mm/km)과 4등(±10mm/km)은 용도가 완전히 다름"
            }
        ],
        "culturalNote": "한국은 전국에 약 15,000개의 수준점이 촘촘히 설치되어 있으며, 지반침하 모니터링에 활용됩니다. 베트남은 도시지역 위주로 수준점이 분포하며, 농촌지역은 밀도가 낮습니다. 한국 현장에서는 수준점 인근 공사 시 보호조치와 재측량이 의무화되어 있으나, 베트남은 상대적으로 관리가 느슨한 편입니다.",
        "examples": [
            {
                "ko": "이 수준점을 기준으로 건물 1층 바닥 높이를 결정합니다.",
                "vi": "Dựa vào điểm cao độ này để xác định độ cao sàn tầng 1 của tòa nhà.",
                "situation": "formal"
            },
            {
                "ko": "수준점이 움직였나? 전 측량값이랑 5cm나 차이나.",
                "vi": "Điểm cao độ bị dịch chuyển à? Chênh lệch với giá trị đo trước tới 5cm.",
                "situation": "onsite"
            },
            {
                "ko": "국가수준점 성과표를 확인 후 레벨측량을 시작하세요.",
                "vi": "Kiểm tra bảng thành quả điểm cao độ quốc gia rồi bắt đầu đo thủy chuẩn.",
                "situation": "formal"
            }
        ],
        "relatedTerms": [
            "레벨측량",
            "표고",
            "지반침하"
        ]
    },
    {
        "slug": "diem-tam-giac",
        "korean": "삼각점",
        "vietnamese": "điểm tam giác",
        "hanja": "三角點",
        "hanjaReading": "삼(석 삼) + 각(뿔 각) + 점(점 점)",
        "pronunciation": "디엠 땀 지악",
        "meaningKo": "삼각측량의 기준이 되는 점으로, 산 정상이나 고지대에 설치되어 넓은 지역의 위치 기준 역할을 합니다. 1·2·3·4등 삼각점으로 등급이 나뉘며, 1등 삼각점은 약 40km 간격으로 설치됩니다. 과거에는 망원경으로 관측했으나 현대에는 GNSS(GPS)로 대체되는 추세입니다. 통역 시 주의점은 삼각점이 단순 위치 기준이 아니라 국가좌표계의 골격이며, 훼손 시 측량법 위반임을 강조해야 합니다.",
        "meaningVi": "Điểm làm cơ sở cho đo tam giác, được đặt trên đỉnh núi hoặc vùng cao để làm chuẩn vị trí cho khu vực rộng. Chia thành điểm tam giác hạng 1, 2, 3, 4, điểm hạng 1 cách nhau khoảng 40km. Trước đây quan sát bằng kính thiên văn, hiện nay chuyển sang GNSS (GPS).",
        "context": "삼각측량, 국가좌표계",
        "contextVi": "Đo tam giác, hệ tọa độ quốc gia",
        "commonMistakes": [
            {
                "mistake": "\"삼각점\"을 \"điểm ba góc\"로 직역",
                "correction": "\"điểm tam giác\"이 표준 측량 용어",
                "explanation": "điểm ba góc는 의미는 맞지만 전문용어가 아님"
            },
            {
                "mistake": "GNSS와 GPS를 동일하게 취급",
                "correction": "GPS는 미국 시스템, GNSS는 모든 위성항법 시스템 통칭",
                "explanation": "한국은 GPS·GLONASS·Galileo·BeiDou를 모두 활용하므로 GNSS가 정확"
            },
            {
                "mistake": "삼각점 등급 차이를 설명하지 않음",
                "correction": "1등(국가 기본), 2등(지역), 3·4등(세부) 용도 구분 필요",
                "explanation": "등급에 따라 정확도·측량 범위·활용 목적이 완전히 다름"
            }
        ],
        "culturalNote": "한국은 전국에 약 3,200개의 삼각점이 설치되어 있으며, 국토지리정보원이 엄격히 관리합니다. 일제강점기 때 설치된 삼각점도 일부 현존하며 문화유산으로 간주됩니다. 베트남은 프랑스 식민지 시절 삼각점이 기초가 되었으나 전쟁으로 많이 소실되어 재정비 중입니다. 한국 현장에서는 삼각점 접근 시 허가가 필요한 경우가 많습니다.",
        "examples": [
            {
                "ko": "이 지역 측량은 북한산 삼각점을 기준으로 실시합니다.",
                "vi": "Công tác đo đạc khu vực này thực hiện dựa trên điểm tam giác núi Bukhan.",
                "situation": "formal"
            },
            {
                "ko": "삼각점 찾으러 산 올라가야 돼. GPS 좌표 찍어놨어.",
                "vi": "Phải lên núi tìm điểm tam giác. Đã chụp tọa độ GPS rồi.",
                "situation": "onsite"
            },
            {
                "ko": "1등 삼각점 성과는 ±5cm 이내 정확도를 보장합니다.",
                "vi": "Thành quả điểm tam giác hạng 1 đảm bảo độ chính xác trong ±5cm.",
                "situation": "formal"
            }
        ],
        "relatedTerms": [
            "삼각측량",
            "GNSS측량",
            "기준점"
        ]
    },
    {
        "slug": "do-mat-cat-dung",
        "korean": "종단측량",
        "vietnamese": "đo mặt cắt dọc",
        "hanja": "縱斷測量",
        "hanjaReading": "종(세로 종) + 단(끊을 단) + 측(헤아릴 측) + 량(헤아릴 량)",
        "pronunciation": "도 맛 껏 증",
        "meaningKo": "도로·철도·하천 등 선형 구조물의 진행방향(종방향) 단면을 측량하여 경사·구배·표고를 결정하는 작업입니다. 레벨과 스태프를 사용하며, 현대에는 토탈스테이션이나 GNSS로 수행합니다. 종단면도에는 지반선(GL)·계획고(PL)·토공량이 표시됩니다. 통역 시 주의점은 구배를 %(퍼센트)로 표현(한국)하는지 ‰(퍼밀)로 표현(일부 국제 기준)하는지 확인이 필요하며, 절토·성토 구간 구분을 명확히 해야 합니다.",
        "meaningVi": "Công tác đo đạc mặt cắt theo hướng tiến (dọc) của công trình tuyến tính như đường, đường sắt, sông để xác định độ dốc, gradient, cao độ. Sử dụng máy thủy chuẩn và thước tiêu, hiện nay dùng máy toàn đạc điện tử hoặc GNSS. Trên bản vẽ mặt cắt dọc thể hiện đường mặt đất (GL), đường thiết kế (PL), khối lượng đào đắp.",
        "context": "도로측량, 철도측량",
        "contextVi": "Đo đạc đường, đo đạc đường sắt",
        "commonMistakes": [
            {
                "mistake": "\"종단\"을 \"cuối cùng\"으로 오역",
                "correction": "\"dọc\"(세로방향) 또는 \"mặt cắt dọc\"이 정확",
                "explanation": "종단은 終端(끝)이 아니라 縱斷(세로 단면)"
            },
            {
                "mistake": "구배 %와 ‰를 혼동하여 통역",
                "correction": "5%는 50‰, 단위 변환 필수",
                "explanation": "구배 표현 방식이 다르면 공사 설계가 완전히 달라짐"
            },
            {
                "mistake": "절토와 성토를 단순히 \"đào\"와 \"đắp\"로만 번역",
                "correction": "절토량·성토량·토량 배분 개념까지 설명",
                "explanation": "토공량 계산은 공사비 산정의 핵심"
            }
        ],
        "culturalNote": "한국 도로는 설계속도에 따라 종단구배 제한(예: 80km/h → 5% 이하)이 엄격합니다. 베트남은 산악지형이 많아 일부 구간은 구배가 급한 편입니다. 한국 현장에서는 종단측량 데이터를 CAD와 연동하여 3D 지형모델을 즉시 생성하나, 베트남은 수작업 제도 병행이 많습니다.",
        "examples": [
            {
                "ko": "종단측량 결과, 이 구간은 성토 3m가 필요합니다.",
                "vi": "Kết quả đo mặt cắt dọc, đoạn này cần đắp cao 3m.",
                "situation": "formal"
            },
            {
                "ko": "종단 구배가 7%면 너무 급한 거 아냐? 설계 다시 봐야겠어.",
                "vi": "Gradient dọc 7% thì quá dốc phải không? Phải xem lại thiết kế.",
                "situation": "onsite"
            },
            {
                "ko": "종단면도에 지하매설물 위치를 표기하세요.",
                "vi": "Hãy đánh dấu vị trí công trình ngầm trên bản vẽ mặt cắt dọc.",
                "situation": "formal"
            }
        ],
        "relatedTerms": [
            "횡단측량",
            "구배",
            "절토·성토"
        ]
    },
    {
        "slug": "do-mat-cat-ngang",
        "korean": "횡단측량",
        "vietnamese": "đo mặt cắt ngang",
        "hanja": "橫斷測量",
        "hanjaReading": "횡(가로 횡) + 단(끊을 단) + 측(헤아릴 측) + 량(헤아릴 량)",
        "pronunciation": "도 맛 껏 응",
        "meaningKo": "도로·철도 등의 중심선에 직각 방향(횡방향)으로 지형 단면을 측량하여 도로폭·절토·성토 높이를 결정하는 작업입니다. 일정 간격(20m, 50m 등)마다 횡단면을 측량하며, 이를 통해 토공량·배수로·옹벽 등을 설계합니다. 통역 시 주의점은 도로 중심선 기준 좌·우측을 명확히 구분하고, 횡단구배(캠버)는 배수를 위해 2% 내외로 설계됨을 설명해야 합니다. 또한 편경사(super elevation) 구간은 별도 표시가 필요합니다.",
        "meaningVi": "Công tác đo đạc mặt cắt theo hướng vuông góc (ngang) với tâm đường, đường sắt để xác định độ rộng đường, chiều cao đào đắp. Đo mặt cắt ngang cách đều (20m, 50m...) để thiết kế khối lượng đào đắp, rãnh thoát nước, tường chắn. Trên bản vẽ mặt cắt ngang thể hiện độ dốc ngang (camber) khoảng 2% để thoát nước.",
        "context": "도로설계, 토공량 산정",
        "contextVi": "Thiết kế đường, tính khối lượng đào đắp",
        "commonMistakes": [
            {
                "mistake": "\"횡단\"을 \"băng qua\"(횡단보도)로 번역",
                "correction": "\"ngang\"(가로방향) 또는 \"mặt cắt ngang\"이 정확",
                "explanation": "횡단보도는 vạch sang đường, 측량 횡단은 mặt cắt ngang"
            },
            {
                "mistake": "좌·우측(trái·phải) 기준점을 명시하지 않음",
                "correction": "도로 진행방향 기준 좌·우를 먼저 정의",
                "explanation": "기준점이 불명확하면 좌·우 반대로 시공할 수 있음"
            },
            {
                "mistake": "횡단구배와 편경사를 구분하지 않음",
                "correction": "횡단구배(배수용 2%), 편경사(곡선부 최대 10%)는 다른 개념",
                "explanation": "편경사는 원심력 방지, 횡단구배는 배수 목적"
            }
        ],
        "culturalNote": "한국은 도로설계 시 횡단측량을 20m 간격으로 정밀하게 수행하며, 3D 스캐닝 기술도 도입 중입니다. 베트남은 간격이 50~100m로 넓은 경우가 많고, 급경사 지형에서는 옹벽·절개면 설계가 복잡합니다. 한국 현장에서는 횡단면도를 CAD로 즉시 제작하나, 베트남은 수작업 제도가 여전히 많습니다.",
        "examples": [
            {
                "ko": "이 구간은 20m마다 횡단측량을 실시하세요.",
                "vi": "Đoạn này hãy thực hiện đo mặt cắt ngang cách nhau 20m.",
                "situation": "formal"
            },
            {
                "ko": "횡단면 보니까 좌측이 3m 절토, 우측이 1m 성토네.",
                "vi": "Nhìn mặt cắt ngang thấy bên trái đào 3m, bên phải đắp 1m.",
                "situation": "onsite"
            },
            {
                "ko": "곡선 구간은 편경사 8%로 횡단측량하세요.",
                "vi": "Đoạn cong hãy đo mặt cắt ngang với siêu cao 8%.",
                "situation": "formal"
            }
        ],
        "relatedTerms": [
            "종단측량",
            "편경사",
            "토공량"
        ]
    },
    {
        "slug": "do-dia-hinh",
        "korean": "지형측량",
        "vietnamese": "đo địa hình",
        "hanja": "地形測量",
        "hanjaReading": "지(땅 지) + 형(모양 형) + 측(헤아릴 측) + 량(헤아릴 량)",
        "pronunciation": "도 디아 힌",
        "meaningKo": "지표면의 높낮이·형상·위치를 측량하여 지형도를 작성하는 작업으로, 축척·등고선 간격에 따라 정밀도가 결정됩니다. 토탈스테이션·GNSS·드론·라이다 등 다양한 장비를 사용하며, 측량 성과는 CAD나 GIS로 도면화됩니다. 통역 시 주의점은 축척(1:500, 1:1000 등)과 등고선 간격(0.5m, 1m, 5m 등)을 명확히 하고, 지형지물(건물·도로·수목 등)의 표기 기준을 확인해야 합니다.",
        "meaningVi": "Công tác đo đạc độ cao thấp, hình dạng, vị trí của mặt đất để lập bản đồ địa hình, độ chính xác phụ thuộc tỷ lệ và khoảng cách đường đồng mức. Sử dụng máy toàn đạc điện tử, GNSS, drone, lidar, thành quả đo được vẽ bằng CAD hoặc GIS.",
        "context": "설계 사전조사, 지형도 제작",
        "contextVi": "Khảo sát trước thiết kế, lập bản đồ địa hình",
        "commonMistakes": [
            {
                "mistake": "축척을 단순 \"tỷ lệ\"로만 번역",
                "correction": "\"tỷ lệ bản đồ\" 또는 \"tỷ lệ 1:500\"처럼 구체적 표현",
                "explanation": "축척 차이는 측량 정밀도·비용·기간에 직결"
            },
            {
                "mistake": "등고선을 \"đường bằng\"으로 오역",
                "correction": "\"đường đồng mức\" 또는 \"đường cong mức\"이 정확",
                "explanation": "đường bằng은 평탄한 선, 등고선은 같은 높이를 연결한 선"
            },
            {
                "mistake": "지형지물(地形地物) 범위를 좁게 해석",
                "correction": "자연지형 + 인공구조물 모두 포함",
                "explanation": "건물·도로·수목·전신주 등 모든 지물이 측량 대상"
            }
        ],
        "culturalNote": "한국은 국토지리정보원이 전국 수치지형도(1:5000)를 구축·공개하며, 민간 측량은 1:500~1:1000 상세도를 많이 사용합니다. 베트남은 도시지역만 상세 지형도가 있고, 농촌·산간지역은 1:25000 이상 축소도가 많습니다. 한국 현장에서는 드론 측량·3D 스캐닝이 일반화되었으나, 베트남은 전통 측량과 병행 중입니다.",
        "examples": [
            {
                "ko": "1:500 축척으로 지형측량을 수행하고 0.5m 간격 등고선을 표시하세요.",
                "vi": "Thực hiện đo địa hình tỷ lệ 1:500 và biểu thị đường đồng mức cách 0.5m.",
                "situation": "formal"
            },
            {
                "ko": "드론으로 지형측량 하면 일주일 걸릴 게 하루면 끝나.",
                "vi": "Đo địa hình bằng drone thì một tuần mới xong giờ một ngày là xong.",
                "situation": "onsite"
            },
            {
                "ko": "지형도에 기존 건물과 도로를 모두 표기하세요.",
                "vi": "Hãy đánh dấu tất cả công trình và đường hiện hữu trên bản đồ địa hình.",
                "situation": "formal"
            }
        ],
        "relatedTerms": [
            "등고선",
            "축척",
            "드론측량"
        ]
    },
    {
        "slug": "do-ban-do",
        "korean": "평판측량",
        "vietnamese": "đo bản đồ",
        "hanja": "平板測量",
        "hanjaReading": "평(평평할 평) + 판(널빤지 판) + 측(헤아릴 측) + 량(헤아릴 량)",
        "pronunciation": "도 반 도",
        "meaningKo": "평판·앨리데이드·구심기 등을 사용하여 현장에서 직접 도면을 작성하는 전통 측량 방법입니다. 도상에서 방향과 거리를 측정하며, 간단한 지형도 제작에 유용하나 정확도는 토탈스테이션에 비해 낮습니다. 현대에는 교육용·소규모 현장 외에는 거의 사용되지 않으며, GNSS와 전자평판으로 대체되고 있습니다. 통역 시 주의점은 평판측량은 구식 방법이므로 현장 상황상 불가피한 경우에만 사용됨을 설명해야 합니다.",
        "meaningVi": "Phương pháp đo đạc truyền thống sử dụng bàn đồ, thước ngắm, dây dọi để vẽ bản vẽ trực tiếp tại hiện trường. Đo hướng và khoảng cách trên bản vẽ, hữu ích cho bản đồ địa hình đơn giản nhưng độ chính xác thấp hơn máy toàn đạc. Hiện nay chỉ dùng trong giảng dạy hoặc công trình nhỏ, đang được thay thế bằng GNSS và bàn đồ điện tử.",
        "context": "전통 측량 교육, 소규모 현장",
        "contextVi": "Giảng dạy đo đạc truyền thống, công trường nhỏ",
        "commonMistakes": [
            {
                "mistake": "\"평판\"을 \"bản phẳng\"로 직역",
                "correction": "\"bàn đồ\" 또는 \"bàn đo\"가 측량 전문용어",
                "explanation": "bản phẳng은 평평한 판, 측량 평판은 bàn đồ"
            },
            {
                "mistake": "평판측량을 현대 측량과 동등하게 설명",
                "correction": "구식 방법이며 정밀도 한계가 있음을 명시",
                "explanation": "발주자가 평판측량 결과를 정밀측량으로 오해하면 문제 발생"
            },
            {
                "mistake": "앨리데이드(alidade)를 단순 \"자\"로 번역",
                "correction": "\"thước ngắm\" 또는 \"giác kế\"가 정확",
                "explanation": "앨리데이드는 방향과 각을 재는 정밀 장비"
            }
        ],
        "culturalNote": "한국은 1980년대까지 평판측량이 주류였으나, 현재는 토탈스테이션·GNSS로 완전히 대체되어 측량학과 실습용으로만 남아있습니다. 베트남은 일부 농촌지역에서 간단한 토지측량에 여전히 사용되기도 합니다. 한국 현장에서 평판측량을 요구하는 경우는 거의 없으며, 문화재 발굴 등 특수 상황에 한정됩니다.",
        "examples": [
            {
                "ko": "이 소규모 부지는 평판측량으로도 충분합니다.",
                "vi": "Lô đất nhỏ này đo bằng bàn đồ cũng đủ.",
                "situation": "formal"
            },
            {
                "ko": "요즘 누가 평판측량 해? 토탈스테이션 쓰지.",
                "vi": "Bây giờ ai dùng đo bàn đồ? Dùng máy toàn đạc chứ.",
                "situation": "onsite"
            },
            {
                "ko": "측량학 실습에서 평판측량 원리를 배웁니다.",
                "vi": "Trong thực hành môn đo đạc, học nguyên lý đo bàn đồ.",
                "situation": "formal"
            }
        ],
        "relatedTerms": [
            "토탈스테이션",
            "앨리데이드",
            "전통측량"
        ]
    },
    {
        "slug": "may-toan-dac-dien-tu",
        "korean": "토탈스테이션",
        "vietnamese": "máy toàn đạc điện tử",
        "hanja": None,
        "hanjaReading": None,
        "pronunciation": "마이 또안 닥 디엔 뜨",
        "meaningKo": "각도(수평각·연직각)와 거리를 전자적으로 측정하는 정밀 측량기기로, 현대 측량의 핵심 장비입니다. EDM(광파거리측정기)과 전자경위의가 결합된 형태이며, 측량 데이터는 내부 메모리나 블루투스로 저장·전송됩니다. 프리즘을 사용한 반사 측정(정밀)과 프리즘 없는 측정(간편) 모드가 있습니다. 통역 시 주의점은 기계 설치·정준(leveling)·시준(collimation) 용어와 측량 순서(후시→전시)를 정확히 전달해야 하며, 오차 허용범위를 명확히 해야 합니다.",
        "meaningVi": "Thiết bị đo đạc chính xác đo góc (góc ngang, góc đứng) và khoảng cách bằng điện tử, là thiết bị cốt lõi của đo đạc hiện đại. Kết hợp EDM (máy đo khoảng cách quang sóng) và máy kinh vĩ điện tử, dữ liệu đo được lưu trong bộ nhớ hoặc truyền qua Bluetooth. Có chế độ đo phản xạ dùng lăng kính (chính xác) và đo không lăng kính (tiện lợi).",
        "context": "현장 정밀측량 필수 장비",
        "contextVi": "Thiết bị bắt buộc cho đo đạc chính xác hiện trường",
        "commonMistakes": [
            {
                "mistake": "토탈스테이션을 단순 \"máy đo\"로 번역",
                "correction": "\"máy toàn đạc điện tử\" 또는 \"total station\"",
                "explanation": "máy đo는 모든 측정기를 의미, 토탈스테이션은 특정 장비"
            },
            {
                "mistake": "프리즘(prism)과 반사판(reflector)을 혼용",
                "correction": "프리즘은 lăng kính, 반사판은 tấm phản quang",
                "explanation": "프리즘은 유리제 정밀 광학기기, 반사판은 반사 시트"
            },
            {
                "mistake": "정준(整準)을 단순 \"수평 맞추기\"로 축소",
                "correction": "\"cân bằng máy\" 또는 \"đặt máy thủy bình\"",
                "explanation": "정준은 기포관·전자센서로 정밀하게 수평을 맞추는 과정"
            }
        ],
        "culturalNote": "한국은 Topcon·Trimble·Leica 등 외산 토탈스테이션을 주로 사용하며, 최신 모델은 자동 타겟 추적·블루투스 연동 기능이 표준입니다. 베트남은 일부 중국산·일본산 보급형도 많이 사용되며, 정밀도 차이가 있습니다. 한국 현장에서는 토탈스테이션 측량자 자격증(측량기능사 이상) 보유자만 운용하나, 베트남은 자격 요건이 느슨한 편입니다.",
        "examples": [
            {
                "ko": "토탈스테이션으로 기준점 좌표를 확인한 후 측량을 시작하세요.",
                "vi": "Sau khi kiểm tra tọa độ điểm khống chế bằng máy toàn đạc, hãy bắt đầu đo đạc.",
                "situation": "formal"
            },
            {
                "ko": "프리즘 들고 저기 서 있어. 토탈로 찍을게.",
                "vi": "Cầm lăng kính đứng đằng kia. Tôi sẽ bắn bằng máy toàn đạc.",
                "situation": "onsite"
            },
            {
                "ko": "이 토탈스테이션은 300m까지 프리즘 없이 측정 가능합니다.",
                "vi": "Máy toàn đạc này có thể đo không lăng kính tới 300m.",
                "situation": "formal"
            }
        ],
        "relatedTerms": [
            "프리즘",
            "정준",
            "EDM"
        ]
    },
    {
        "slug": "gnss",
        "korean": "GNSS",
        "vietnamese": "GNSS",
        "hanja": None,
        "hanjaReading": None,
        "pronunciation": "지 엔 엣 엣",
        "meaningKo": "Global Navigation Satellite System(전지구 위성항법 시스템)의 약어로, 미국 GPS, 러시아 GLONASS, 유럽 Galileo, 중국 BeiDou 등 모든 위성항법 시스템을 통칭합니다. 정지측량(Static)·RTK(Real-Time Kinematic)·PPP(Precise Point Positioning) 등 다양한 측량 모드가 있으며, RTK는 실시간 cm급 정밀도를 제공합니다. 통역 시 주의점은 단순히 GPS라고 하면 미국 시스템만 의미하므로 GNSS로 정확히 표현하고, RTK 기준국·이동국·보정 신호(VRS, FKP 등) 개념을 명확히 해야 합니다.",
        "meaningVi": "Viết tắt của Global Navigation Satellite System (Hệ thống định vị vệ tinh toàn cầu), bao gồm GPS (Mỹ), GLONASS (Nga), Galileo (EU), BeiDou (Trung Quốc). Có các chế độ đo tĩnh (Static), RTK (Real-Time Kinematic), PPP (Precise Point Positioning), RTK đạt độ chính xác cấp cm theo thời gian thực.",
        "context": "위성측량, 정밀 위치 결정",
        "contextVi": "Đo đạc vệ tinh, xác định vị trí chính xác",
        "commonMistakes": [
            {
                "mistake": "GNSS와 GPS를 동일하게 취급",
                "correction": "GPS는 미국 시스템, GNSS는 모든 위성항법 통칭",
                "explanation": "한국은 GPS·GLONASS·Galileo·BeiDou를 모두 활용하므로 GNSS가 정확"
            },
            {
                "mistake": "RTK를 단순 \"실시간 측량\"으로만 번역",
                "correction": "\"đo động học thời gian thực\" 또는 \"RTK\" 그대로 사용",
                "explanation": "RTK는 반송파 위상 측정 기반 고정밀 기술"
            },
            {
                "mistake": "VRS, FKP 등 보정 방식 차이를 설명하지 않음",
                "correction": "VRS(가상기준점), FKP(면적보정), NTRIP(인터넷 보정) 구분",
                "explanation": "보정 방식에 따라 정확도·통신 방식·비용이 다름"
            }
        ],
        "culturalNote": "한국은 국토지리정보원이 운영하는 VRS 네트워크(전국 약 100개 상시관측소)를 무료로 제공하며, 실시간 cm급 측량이 가능합니다. 베트남은 대도시 중심으로 VRS가 구축되어 있으나 전국망은 아직 완성되지 않았습니다. 한국 현장에서는 GNSS 측량이 일상화되어 있으나, 베트남은 통신 인프라 문제로 일부 지역은 Static 측량을 병행합니다.",
        "examples": [
            {
                "ko": "GNSS RTK 측량으로 기준점 좌표를 cm급 정밀도로 확인하세요.",
                "vi": "Hãy kiểm tra tọa độ điểm khống chế bằng đo GNSS RTK với độ chính xác cấp cm.",
                "situation": "formal"
            },
            {
                "ko": "여기 통신 안 터져서 RTK 안 돼. Static으로 해야겠어.",
                "vi": "Chỗ này không có sóng nên RTK không được. Phải đo tĩnh thôi.",
                "situation": "onsite"
            },
            {
                "ko": "VRS 보정 신호를 수신하려면 인터넷 연결이 필요합니다.",
                "vi": "Để nhận tín hiệu hiệu chỉnh VRS cần kết nối internet.",
                "situation": "formal"
            }
        ],
        "relatedTerms": [
            "RTK",
            "VRS",
            "GPS"
        ]
    },
    {
        "slug": "lidar",
        "korean": "라이다",
        "vietnamese": "lidar",
        "hanja": None,
        "hanjaReading": None,
        "pronunciation": "리다",
        "meaningKo": "Light Detection and Ranging의 약어로, 레이저 펄스를 발사하여 물체까지의 거리를 측정하고 3차원 점군 데이터를 생성하는 원격탐사 기술입니다. 지상 라이다(TLS), 항공 라이다(ALS), 모바일 라이다(MLS)로 구분되며, 수백만~수억 개의 점 데이터(Point Cloud)를 생성합니다. 통역 시 주의점은 라이다는 단순 측량 장비가 아니라 3D 모델링·BIM·디지털트윈 구축의 핵심 기술이며, 드론 라이다는 산림·지형 측량에, 지상 라이다는 건축물·터널 스캔에 사용됨을 명확히 해야 합니다.",
        "meaningVi": "Viết tắt của Light Detection and Ranging, công nghệ viễn thám phát xung laser để đo khoảng cách tới vật thể và tạo dữ liệu đám mây điểm 3D. Chia thành lidar mặt đất (TLS), lidar hàng không (ALS), lidar di động (MLS), tạo hàng triệu đến hàng tỷ điểm dữ liệu (Point Cloud).",
        "context": "3D 스캔, 정밀 지형모델",
        "contextVi": "Quét 3D, mô hình địa hình chính xác",
        "commonMistakes": [
            {
                "mistake": "라이다를 단순 \"máy quét laser\"로 번역",
                "correction": "\"lidar\" 또는 \"công nghệ quét laser 3D\"",
                "explanation": "laser scanner는 일반 스캐너, lidar는 항공·지상 모두 포함하는 기술"
            },
            {
                "mistake": "점군 데이터를 \"dữ liệu điểm\"로만 번역",
                "correction": "\"đám mây điểm\" 또는 \"point cloud\"",
                "explanation": "point cloud는 수백만 개 점의 집합을 의미하는 전문용어"
            },
            {
                "mistake": "드론 라이다와 지상 라이다 용도를 혼동",
                "correction": "항공(지형·산림), 지상(건물·터널) 용도 명확히 구분",
                "explanation": "장비와 용도가 완전히 다르며, 정밀도도 차이남"
            }
        ],
        "culturalNote": "한국은 국토교통부가 항공 라이다로 전국 정밀 수치표면모델(DSM)을 구축 중이며, 건설 현장에서는 BIM과 연계한 라이다 스캔이 확대되고 있습니다. 베트남은 대규모 인프라 사업(고속도로·댐)에서 라이다를 도입 중이나, 장비 비용과 기술 인력 부족으로 일반화되지는 않았습니다. 한국 현장에서는 라이다 데이터를 CAD·Revit·Civil 3D와 즉시 연동합니다.",
        "examples": [
            {
                "ko": "드론 라이다로 산악지형을 스캔하여 1:500 지형도를 제작합니다.",
                "vi": "Quét địa hình miền núi bằng lidar drone để lập bản đồ địa hình tỷ lệ 1:500.",
                "situation": "formal"
            },
            {
                "ko": "이 터널은 지상 라이다로 스캔해서 변형 체크해야 돼.",
                "vi": "Hầm này phải quét bằng lidar mặt đất để kiểm tra biến dạng.",
                "situation": "onsite"
            },
            {
                "ko": "라이다 점군 데이터를 BIM 모델로 변환하세요.",
                "vi": "Hãy chuyển đổi dữ liệu đám mây điểm lidar thành mô hình BIM.",
                "situation": "formal"
            }
        ],
        "relatedTerms": [
            "점군데이터",
            "3D스캔",
            "드론측량"
        ]
    }
]


def main():
    """
    Construction Surveying Terms Addition
    - Reads existing construction.json
    - Appends 10 new terms (Tier S)
    - Writes back to file
    """
    script_dir = os.path.dirname(os.path.abspath(__file__))
    project_root = os.path.dirname(script_dir)
    terms_file = os.path.join(project_root, "data", "terms", "construction.json")

    print(f"[INFO] Reading: {terms_file}")

    with open(terms_file, "r", encoding="utf-8") as f:
        existing_terms = json.load(f)

    print(f"[INFO] Current term count: {len(existing_terms)}")

    # Append new terms
    existing_terms.extend(data)

    print(f"[INFO] New term count: {len(existing_terms)}")
    print(f"[INFO] Writing back to: {terms_file}")

    with open(terms_file, "w", encoding="utf-8") as f:
        json.dump(existing_terms, f, ensure_ascii=False, indent=2)

    print("[SUCCESS] ✅ 10 construction surveying terms added (Tier S compliant)")
    print("\n[ADDED TERMS]")
    for idx, term in enumerate(data, 1):
        print(f"  {idx}. {term['korean']} ({term['slug']})")


if __name__ == "__main__":
    main()
