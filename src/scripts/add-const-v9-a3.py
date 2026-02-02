#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Construction Formwork Terms Addition Script v9
Theme: Formwork Systems Detail (거푸집/폼워크상세)
- 알루미늄폼, 강재폼, 갱폼, 클라이밍폼, 슬립폼
- 플라잉폼, 터널폼, 테이블폼, 목재폼, 특수폼
Total: 10 terms, Tier S compliant
"""

import json
import os

# Tier S 품질 기준: 모든 필드 필수, meaningKo 200자+, culturalNote 100자+, examples/commonMistakes/relatedTerms 3개+
data = [
    {
        "slug": "gia-cong-nhom",
        "korean": "알루미늄폼",
        "vietnamese": "gia công nhôm",
        "hanja": None,
        "hanjaReading": None,
        "pronunciation": "지아 꽁 늄",
        "meaningKo": "알루미늄 합금으로 제작된 거푸집 시스템으로, 경량이면서도 강도가 높아 반복 사용이 가능합니다. 주로 공동주택·오피스텔 등 반복 평면 구조에 적합하며, 100회 이상 재사용 가능하여 장기적으로 경제적입니다. 조립·해체가 간편하고 콘크리트 표면 품질이 우수하나, 초기 투자비용이 높고 평면 변경에 대응하기 어렵습니다. 통역 시 주의점은 알루미늄폼은 시스템폼의 일종이며, 유로폼(합판+강재)과는 완전히 다른 공법임을 강조하고, 층고·벽두께 표준화가 필수 조건임을 설명해야 합니다.",
        "meaningVi": "Hệ thống ván khuôn làm bằng hợp kim nhôm, nhẹ nhưng cường độ cao nên có thể tái sử dụng nhiều lần. Chủ yếu phù hợp cho nhà chung cư, officetel có mặt bằng lặp lại, có thể tái sử dụng trên 100 lần nên kinh tế về lâu dài. Lắp ráp tháo dỡ đơn giản, chất lượng bề mặt bê tông tốt nhưng chi phí đầu tư ban đầu cao và khó thay đổi mặt bằng.",
        "context": "공동주택, 시스템폼",
        "contextVi": "Nhà chung cư, ván khuôn hệ thống",
        "commonMistakes": [
            {
                "mistake": "\"알루미늄폼\"을 \"ván khuôn nhôm\"으로만 번역",
                "correction": "\"gia công nhôm\" 또는 \"hệ thống ván khuôn nhôm\"",
                "explanation": "ván khuôn nhôm은 일반 명칭, gia công nhôm은 시스템 전체를 의미"
            },
            {
                "mistake": "유로폼과 알루미늄폼을 혼동",
                "correction": "유로폼은 합판+강재, 알루미늄폼은 알루미늄 합금 시스템",
                "explanation": "재료·공법·적용 구조가 완전히 다름"
            },
            {
                "mistake": "재사용 횟수를 과장 또는 축소",
                "correction": "통상 100~200회 재사용, 관리 상태에 따라 차이",
                "explanation": "재사용 횟수는 경제성 계산의 핵심 변수"
            }
        ],
        "culturalNote": "한국은 1990년대부터 대형 건설사가 자체 알루미늄폼 시스템을 개발하여 공동주택에 적용해왔으며, 현재는 20층 이상 고층 아파트의 표준 공법입니다. 베트남은 최근 10년간 한국·중국 기술이 도입되어 고층 아파트에 확대 중이나, 아직 유로폼 병행이 많습니다. 한국 현장에서는 알루미늄폼 전문 시공팀이 별도 운영되며, 베트남은 현지 인력 교육이 필요합니다.",
        "examples": [
            {
                "ko": "이 아파트는 알루미늄폼 공법으로 4일 1층 공정이 가능합니다.",
                "vi": "Chung cư này dùng gia công nhôm nên có thể hoàn thành 1 tầng trong 4 ngày.",
                "situation": "formal"
            },
            {
                "ko": "알폼 조립 끝났어? 배근 검사 들어가자.",
                "vi": "Lắp ván khuôn nhôm xong chưa? Vào kiểm tra cốt thép.",
                "situation": "onsite"
            },
            {
                "ko": "알루미늄폼은 초기 비용이 높지만 30층 이상이면 경제적입니다.",
                "vi": "Gia công nhôm tuy chi phí ban đầu cao nhưng từ 30 tầng trở lên thì kinh tế.",
                "situation": "formal"
            }
        ],
        "relatedTerms": [
            "시스템폼",
            "유로폼",
            "4일1층공정"
        ]
    },
    {
        "slug": "gia-cong-thep",
        "korean": "강재폼",
        "vietnamese": "gia công thép",
        "hanja": "鋼材form",
        "hanjaReading": "강(쇠 강) + 재(재료 재)",
        "pronunciation": "지아 꽁 티엡",
        "meaningKo": "강철 재료로 제작된 거푸집으로, 높은 강성과 내구성을 가지며 고하중·대형 구조물에 적합합니다. 교각·댐·옹벽·지하구조물 등 특수 구조에 주로 사용되며, 표면 정밀도가 요구되는 노출콘크리트에도 활용됩니다. 무게가 무거워 크레인 등 양중장비가 필수이며, 제작 비용이 높으나 수백 회 재사용 가능합니다. 통역 시 주의점은 강재폼은 단순 철판이 아니라 정밀 가공된 시스템이며, 조인트·타이볼트·와이어로프 연결 방식을 명확히 하고, 콘크리트 압력 계산이 중요함을 강조해야 합니다.",
        "meaningVi": "Ván khuôn làm bằng vật liệu thép, có độ cứng và độ bền cao, phù hợp cho kết cấu lớn chịu tải trọng cao. Chủ yếu dùng cho trụ cầu, đập, tường chắn, công trình ngầm, cũng dùng cho bê tông kiến trúc yêu cầu độ chính xác bề mặt. Nặng nên cần thiết bị nâng hạ như cần trục, chi phí chế tạo cao nhưng có thể tái sử dụng hàng trăm lần.",
        "context": "교량, 대형 구조물",
        "contextVi": "Cầu, công trình lớn",
        "commonMistakes": [
            {
                "mistake": "\"강재폼\"을 단순 \"ván khuôn sắt\"로 번역",
                "correction": "\"gia công thép\" 또는 \"hệ thống ván khuôn thép\"",
                "explanation": "sắt는 일반 철, thép는 강철·강재를 의미"
            },
            {
                "mistake": "콘크리트 압력(concrete pressure)을 고려하지 않음",
                "correction": "측압 계산·타이볼트 간격을 반드시 확인",
                "explanation": "압력 계산 오류는 거푸집 붕괴로 이어짐"
            },
            {
                "mistake": "노출콘크리트용 강재폼과 일반 강재폼을 동일시",
                "correction": "노출콘크리트용은 표면 정밀도·이음매 처리가 다름",
                "explanation": "노출콘크리트는 마감이 없어 거푸집 품질이 그대로 드러남"
            }
        ],
        "culturalNote": "한국은 교량·지하철·터널 등 인프라 공사에서 강재폼이 표준이며, 대형 건설사는 자체 강재폼 제작소를 운영합니다. 베트남은 대규모 인프라 프로젝트에서 한국·일본·중국 기술을 도입하며, 일부는 목재폼으로 대체하기도 합니다. 한국 현장에서는 강재폼 설계·제작·시공이 전문화되어 있으나, 베트남은 현지 제작 품질 편차가 큽니다.",
        "examples": [
            {
                "ko": "이 교각은 강재폼으로 15m 높이를 일체 타설합니다.",
                "vi": "Trụ cầu này dùng gia công thép đổ liền khối cao 15m.",
                "situation": "formal"
            },
            {
                "ko": "강재폼 무거워서 25톤 크레인 불러야 돼.",
                "vi": "Ván khuôn thép nặng phải gọi cần trục 25 tấn.",
                "situation": "onsite"
            },
            {
                "ko": "노출콘크리트용 강재폼은 표면 거칠기 Ra 3.2 이하로 제작하세요.",
                "vi": "Gia công thép cho bê tông kiến trúc chế tạo độ nhám bề mặt Ra 3.2 trở xuống.",
                "situation": "formal"
            }
        ],
        "relatedTerms": [
            "노출콘크리트",
            "타이볼트",
            "교각거푸집"
        ]
    },
    {
        "slug": "gia-cong-truot",
        "korean": "갱폼",
        "vietnamese": "gia công trượt",
        "hanja": None,
        "hanjaReading": None,
        "pronunciation": "지아 꽁 쭈엇",
        "meaningKo": "갱폼(Gang Form)은 대면적 벽체를 일체로 타설하기 위한 대형 패널 거푸집 시스템으로, 크레인으로 한 번에 탈형·이동·재설치가 가능합니다. 주로 아파트 측벽·코어·계단실 등 수직 반복 구조에 사용되며, 1회 타설 면적이 50~100㎡에 달합니다. 조립식이 아닌 일체형 패널이므로 이음매가 적어 콘크리트 표면 품질이 우수하나, 제작비가 높고 평면 변경에 취약합니다. 통역 시 주의점은 갱폼은 시스템폼의 일종이나 주로 벽체 전용이며, 슬래브는 별도 폼(테이블폼 등)과 조합하고, 크레인 양중 계획이 필수임을 강조해야 합니다.",
        "meaningVi": "Gang Form là hệ thống ván khuôn tấm lớn để đổ tường diện tích lớn một khối, có thể tháo khuôn, di chuyển, lắp lại bằng cần trục một lần. Chủ yếu dùng cho tường bên, lõi, cầu thang chung cư, diện tích đổ một lần đạt 50~100㎡. Là tấm liền khối không lắp ráp nên ít mối nối, chất lượng bề mặt bê tông tốt nhưng chi phí chế tạo cao và khó thay đổi mặt bằng.",
        "context": "아파트 벽체, 코어",
        "contextVi": "Tường chung cư, lõi",
        "commonMistakes": [
            {
                "mistake": "\"갱폼\"을 \"ván khuôn gang\"으로 오역",
                "correction": "\"gia công trượt\" 또는 \"gang form\"",
                "explanation": "gang은 주철을 의미, 갱폼은 Gang Form의 음차"
            },
            {
                "mistake": "갱폼과 유로폼을 혼동",
                "correction": "갱폼은 대형 일체 패널, 유로폼은 소형 조립식",
                "explanation": "시공 방법·크레인 사용·품질·속도가 완전히 다름"
            },
            {
                "mistake": "크레인 양중 계획 없이 갱폼 도입",
                "correction": "타워크레인 용량·위치·동선 사전 계획 필수",
                "explanation": "갱폼은 무게 5~10톤으로 크레인 없이 시공 불가"
            }
        ],
        "culturalNote": "한국은 1990년대부터 갱폼이 아파트 공사의 표준이 되었으며, 대형 건설사는 자체 갱폼을 보유합니다. 베트남은 최근 10년간 한국 기술이 도입되어 고층 아파트에 적용 중이나, 중저층은 여전히 유로폼이 주류입니다. 한국 현장에서는 갱폼 조립·탈형·이동을 전문팀이 수행하며, 4일 1층 공정과 연계됩니다.",
        "examples": [
            {
                "ko": "이 측벽은 갱폼으로 일체 타설하여 이음매를 최소화합니다.",
                "vi": "Tường bên này dùng gang form đổ liền khối để giảm mối nối.",
                "situation": "formal"
            },
            {
                "ko": "갱폼 탈형했어? 크레인으로 위층 올려.",
                "vi": "Tháo gang form xong chưa? Dùng cần trục nâng lên tầng trên.",
                "situation": "onsite"
            },
            {
                "ko": "갱폼 제작 시 층고·벽두께·개구부 위치를 정확히 반영하세요.",
                "vi": "Khi chế tạo gang form hãy phản ánh chính xác chiều cao tầng, chiều dày tường, vị trí lỗ mở.",
                "situation": "formal"
            }
        ],
        "relatedTerms": [
            "시스템폼",
            "테이블폼",
            "4일1층공정"
        ]
    },
    {
        "slug": "gia-cong-leo",
        "korean": "클라이밍폼",
        "vietnamese": "gia công leo",
        "hanja": None,
        "hanjaReading": None,
        "pronunciation": "지아 꽁 레오",
        "meaningKo": "클라이밍폼(Climbing Form)은 고층 건물·교각·굴뚝 등 수직 구조물 시공 시 거푸집을 크레인 없이 자체적으로 상승시키는 시스템입니다. 유압잭·가이드레일·플랫폼으로 구성되며, 콘크리트 양생 후 거푸집을 수직 이동시켜 다음 층을 시공합니다. 타워크레인 의존도를 줄이고 안전성이 높으나, 초기 설치비용이 크고 전문 기술이 필요합니다. 통역 시 주의점은 클라이밍폼은 단순 거푸집이 아니라 작업발판·안전난간·자재 적재 공간까지 포함한 통합 시스템이며, 상승 속도·안전 점검·유압 관리가 중요함을 강조해야 합니다.",
        "meaningVi": "Climbing Form là hệ thống nâng ván khuôn lên cao mà không cần cần trục khi thi công công trình thẳng đứng như cao ốc, trụ cầu, ống khói. Gồm kích thủy lực, ray dẫn hướng, sàn làm việc, sau khi bê tông đông cứng di chuyển ván khuôn lên trên để thi công tầng tiếp theo. Giảm phụ thuộc cần trục tháp và an toàn cao nhưng chi phí lắp đặt ban đầu lớn và cần kỹ thuật chuyên môn.",
        "context": "초고층, 교각, 수직 구조물",
        "contextVi": "Siêu cao tầng, trụ cầu, công trình thẳng đứng",
        "commonMistakes": [
            {
                "mistake": "\"클라이밍폼\"을 \"ván khuôn trèo\"로 직역",
                "correction": "\"gia công leo\" 또는 \"climbing form\"",
                "explanation": "trèo는 일상어, leo는 기술 용어"
            },
            {
                "mistake": "슬립폼과 클라이밍폼을 혼동",
                "correction": "슬립폼은 연속 상승, 클라이밍폼은 단계별 상승",
                "explanation": "슬립폼은 24시간 타설, 클라이밍폼은 양생 후 이동"
            },
            {
                "mistake": "유압잭 안전 점검을 소홀히 함",
                "correction": "상승 전 유압·볼트·가이드레일 필수 점검",
                "explanation": "유압 고장 시 거푸집 추락 위험"
            }
        ],
        "culturalNote": "한국은 롯데월드타워 등 초고층 건물과 인천대교 등 사장교 주탑 시공에 클라이밍폼을 표준 적용합니다. 베트남은 랜드마크81(81층) 등 초고층 프로젝트에서 한국·유럽 기술을 도입하며, 숙련 인력 확보가 과제입니다. 한국 현장에서는 클라이밍폼 전문 시공팀과 안전관리자가 상주하며, 일일 상승 기록을 의무화합니다.",
        "examples": [
            {
                "ko": "이 코어는 클라이밍폼으로 50층까지 연속 시공합니다.",
                "vi": "Lõi này dùng gia công leo thi công liên tục đến tầng 50.",
                "situation": "formal"
            },
            {
                "ko": "클폼 올리기 전에 유압 점검했어? 안전고리 다 걸었어?",
                "vi": "Trước khi nâng climbing form kiểm tra thủy lực chưa? Móc an toàn gài hết chưa?",
                "situation": "onsite"
            },
            {
                "ko": "클라이밍폼은 1회 상승 높이 3~4m로 설계되었습니다.",
                "vi": "Gia công leo được thiết kế chiều cao nâng một lần 3~4m.",
                "situation": "formal"
            }
        ],
        "relatedTerms": [
            "슬립폼",
            "자동상승거푸집",
            "초고층"
        ]
    },
    {
        "slug": "gia-cong-truot-lien-tuc",
        "korean": "슬립폼",
        "vietnamese": "gia công trượt liên tục",
        "hanja": None,
        "hanjaReading": None,
        "pronunciation": "지아 꽁 쭈엇 리엔 뚝",
        "meaningKo": "슬립폼(Slip Form)은 거푸집을 연속적으로 상승시키며 콘크리트를 24시간 타설하는 공법으로, 주로 사일로·굴뚝·교각·고층 코어 등 단면이 일정한 수직 구조물에 사용됩니다. 유압잭으로 시간당 20~30cm씩 천천히 상승하며, 하부 콘크리트가 양생되는 동안 상부에 새 콘크리트를 타설합니다. 이음매가 없어 구조적으로 유리하고 공기가 짧으나, 중단 없이 연속 작업이 필요하여 레미콘·인력·전력 공급이 24시간 안정적이어야 합니다. 통역 시 주의점은 슬립폼은 고도의 전문 기술이 필요하며, 콘크리트 배합·상승속도·온도관리가 성패를 좌우함을 강조해야 합니다.",
        "meaningVi": "Slip Form là công pháp nâng ván khuôn liên tục và đổ bê tông 24 giờ, chủ yếu dùng cho công trình thẳng đứng có mặt cắt đồng đều như silo, ống khói, trụ cầu, lõi cao tầng. Kích thủy lực nâng chậm 20~30cm/giờ, trong khi bê tông dưới đông cứng thì đổ bê tông mới ở trên. Không có mối nối nên có lợi về kết cấu và rút ngắn thời gian nhưng cần làm việc liên tục không dừng nên nguồn cung bê tông, nhân lực, điện phải ổn định 24 giờ.",
        "context": "사일로, 굴뚝, 연속 타설",
        "contextVi": "Silo, ống khói, đổ liên tục",
        "commonMistakes": [
            {
                "mistake": "\"슬립폼\"을 단순 \"ván khuôn trượt\"로 번역",
                "correction": "\"gia công trượt liên tục\" 또는 \"slip form\"",
                "explanation": "trượt는 미끄러짐, liên tục(연속)가 핵심"
            },
            {
                "mistake": "클라이밍폼과 슬립폼을 동일시",
                "correction": "슬립폼은 연속 상승·24시간 타설, 클라이밍폼은 단계별 이동",
                "explanation": "공법·장비·인력 운영이 완전히 다름"
            },
            {
                "mistake": "콘크리트 배합·슬럼프를 일반 공사와 동일하게 적용",
                "correction": "슬립폼 전용 배합(초결 지연, 슬럼프 15~18cm)",
                "explanation": "배합 오류 시 거푸집 탈형 불량·균열 발생"
            }
        ],
        "culturalNote": "한국은 1970~80년대 산업화 시기에 사일로·굴뚝 건설에 슬립폼을 많이 사용했으며, 현재는 초고층 코어 시공에 적용됩니다. 베트남은 시멘트 공장·화력발전소 굴뚝에 슬립폼을 사용하며, 한국·중국 전문팀이 투입됩니다. 한국 현장에서는 슬립폼 시공 중 비상 대응 매뉴얼과 백업 전원·레미콘 공급 계약이 필수입니다.",
        "examples": [
            {
                "ko": "이 굴뚝은 슬립폼으로 3일 만에 60m를 타설했습니다.",
                "vi": "Ống khói này dùng slip form đổ 60m trong 3 ngày.",
                "situation": "formal"
            },
            {
                "ko": "슬립폼 돌아가는데 레미콘 끊기면 안 돼. 24시간 공급 확실해?",
                "vi": "Slip form đang chạy mà bê tông thương phẩm bị đứt thì không được. Cung cấp 24 giờ chắc chắn chứ?",
                "situation": "onsite"
            },
            {
                "ko": "슬립폼 상승속도를 시간당 25cm로 유지하세요.",
                "vi": "Duy trì tốc độ nâng slip form 25cm/giờ.",
                "situation": "formal"
            }
        ],
        "relatedTerms": [
            "클라이밍폼",
            "연속타설",
            "사일로"
        ]
    },
    {
        "slug": "gia-cong-bay",
        "korean": "플라잉폼",
        "vietnamese": "gia công bay",
        "hanja": None,
        "hanjaReading": None,
        "pronunciation": "지아 꽁 바이",
        "meaningKo": "플라잉폼(Flying Form)은 슬래브·보 하부 거푸집을 일체형 테이블로 제작하여 크레인으로 층간 이동시키는 시스템입니다. 테이블폼과 유사하나 바퀴가 없고 전체를 공중으로 양중하여 이동하므로 '날아다니는 거푸집'이라 불립니다. 주로 고층 건물 슬래브 시공에 사용되며, 1개 테이블이 100~300㎡를 커버합니다. 조립·해체 시간이 짧아 공기 단축 효과가 크나, 타워크레인 의존도가 높고 평면 변경에 취약합니다. 통역 시 주의점은 플라잉폼은 갱폼(벽체)과 조합하여 사용하며, 크레인 양중 계획·안전 고리·하부 지지 구조를 반드시 확인해야 함을 강조해야 합니다.",
        "meaningVi": "Flying Form là hệ thống chế tạo ván khuôn dưới sàn, dầm thành bàn liền khối và di chuyển giữa các tầng bằng cần trục. Tương tự table form nhưng không có bánh xe và nâng toàn bộ lên không trung để di chuyển nên gọi là 'ván khuôn bay'. Chủ yếu dùng cho thi công sàn cao ốc, một bàn phủ 100~300㎡. Thời gian lắp tháo ngắn nên rút ngắn công kỳ nhưng phụ thuộc cao vào cần trục tháp và khó thay đổi mặt bằng.",
        "context": "고층 슬래브, 반복 평면",
        "contextVi": "Sàn cao ốc, mặt bằng lặp lại",
        "commonMistakes": [
            {
                "mistake": "\"플라잉폼\"을 \"ván khuôn bay\"로만 번역",
                "correction": "\"gia công bay\" 또는 \"flying form\"",
                "explanation": "ván khuôn bay는 직역, gia công bay가 시스템 명칭"
            },
            {
                "mistake": "테이블폼과 플라잉폼을 혼동",
                "correction": "테이블폼은 바퀴로 이동, 플라잉폼은 크레인 양중",
                "explanation": "이동 방식·크레인 의존도·적용 현장이 다름"
            },
            {
                "mistake": "안전 고리·와이어로프 점검을 소홀히 함",
                "correction": "양중 전 안전 고리 4개소 이상·와이어 손상 여부 필수 확인",
                "explanation": "양중 중 낙하 시 대형 안전사고"
            }
        ],
        "culturalNote": "한국은 1990년대부터 아파트·오피스 건설에 플라잉폼을 도입하여 4일 1층 공정 달성의 핵심 기술로 자리잡았습니다. 베트남은 최근 고층 빌딩 프로젝트에서 한국 기술을 도입 중이나, 타워크레인 대수·용량 부족으로 적용에 한계가 있습니다. 한국 현장에서는 플라잉폼 전용 양중팀과 안전관리자가 배치됩니다.",
        "examples": [
            {
                "ko": "이 층 슬래브는 플라잉폼 6개로 일괄 타설합니다.",
                "vi": "Sàn tầng này đổ hàng loạt bằng 6 flying form.",
                "situation": "formal"
            },
            {
                "ko": "플라잉폼 올리기 전에 안전고리 4개 다 걸었지?",
                "vi": "Trước khi nâng flying form móc an toàn 4 cái gài hết chưa?",
                "situation": "onsite"
            },
            {
                "ko": "플라잉폼은 크레인 1대로 하루 4~6개 이동 가능합니다.",
                "vi": "Flying form dùng 1 cần trục có thể di chuyển 4~6 cái trong một ngày.",
                "situation": "formal"
            }
        ],
        "relatedTerms": [
            "테이블폼",
            "갱폼",
            "타워크레인"
        ]
    },
    {
        "slug": "gia-cong-ham",
        "korean": "터널폼",
        "vietnamese": "gia công hầm",
        "hanja": None,
        "hanjaReading": None,
        "pronunciation": "지아 꽁 험",
        "meaningKo": "터널폼(Tunnel Form)은 벽체와 슬래브를 동시에 타설하는 일체형 거푸집으로, 단면이 터널처럼 생겨 이런 이름이 붙었습니다. 주로 공동주택·호텔 등 셀(Cell) 구조가 반복되는 건물에 적합하며, 1회 타설로 벽+바닥+천장이 완성되어 공기가 짧습니다. 강성이 높아 콘크리트 품질이 우수하고 내력벽 구조에 유리하나, 개구부·발코니 등 변형 평면에는 제약이 있습니다. 통역 시 주의점은 터널폼은 라멘 구조가 아닌 벽식 구조 전용이며, 1일 1층 또는 2일 1층 공정이 가능하나 평면 표준화가 필수 조건임을 강조해야 합니다.",
        "meaningVi": "Tunnel Form là ván khuôn liền khối đổ đồng thời tường và sàn, mặt cắt giống hầm nên có tên này. Chủ yếu phù hợp cho nhà chung cư, khách sạn có kết cấu ô (cell) lặp lại, một lần đổ hoàn thành tường + sàn + trần nên rút ngắn công kỳ. Độ cứng cao nên chất lượng bê tông tốt và có lợi cho kết cấu tường chịu lực nhưng có hạn chế với mặt bằng biến đổi như lỗ mở, ban công.",
        "context": "벽식구조, 반복 셀",
        "contextVi": "Kết cấu tường, ô lặp lại",
        "commonMistakes": [
            {
                "mistake": "\"터널폼\"을 \"ván khuôn đường hầm\"로 직역",
                "correction": "\"gia công hầm\" 또는 \"tunnel form\"",
                "explanation": "đường hầm은 도로 터널, 거푸집은 gia công hầm"
            },
            {
                "mistake": "라멘 구조(기둥·보)에 터널폼 적용",
                "correction": "터널폼은 벽식 구조 전용, 라멘은 갱폼·플라잉폼",
                "explanation": "구조 시스템이 다르면 거푸집도 다름"
            },
            {
                "mistake": "평면 변형(발코니 확장 등)을 터널폼으로 대응",
                "correction": "터널폼은 표준 평면에만 적합, 변형은 추가 거푸집 필요",
                "explanation": "평면 변형 시 터널폼 경제성 상실"
            }
        ],
        "culturalNote": "한국은 1980~90년대 아파트 건설 붐 때 터널폼이 많이 사용되었으나, 평면 다양화 요구로 현재는 알루미늄폼·갱폼으로 대체되었습니다. 베트남은 저가 공동주택 건설에 터널폼을 적용 중이며, 터키·중국 기술이 도입되고 있습니다. 한국 현장에서는 터널폼 적용 사례가 줄었으나, 베트남은 단순 반복 평면 프로젝트에 여전히 유효합니다.",
        "examples": [
            {
                "ko": "이 아파트는 터널폼으로 1일 1층 공정이 가능합니다.",
                "vi": "Chung cư này dùng tunnel form có thể hoàn thành 1 tầng trong 1 ngày.",
                "situation": "formal"
            },
            {
                "ko": "터널폼 들어가기 전에 배근 다 끝났어?",
                "vi": "Trước khi vào tunnel form cốt thép xong hết chưa?",
                "situation": "onsite"
            },
            {
                "ko": "터널폼은 벽두께 150mm, 슬래브 150mm 표준 단면으로 설계하세요.",
                "vi": "Tunnel form thiết kế mặt cắt tiêu chuẩn tường 150mm, sàn 150mm.",
                "situation": "formal"
            }
        ],
        "relatedTerms": [
            "벽식구조",
            "알루미늄폼",
            "1일1층공정"
        ]
    },
    {
        "slug": "gia-cong-san-ban",
        "korean": "테이블폼",
        "vietnamese": "gia công sàn bàn",
        "hanja": None,
        "hanjaReading": None,
        "pronunciation": "지아 꽁 산 반",
        "meaningKo": "테이블폼(Table Form)은 슬래브·보 하부 거푸집을 테이블 형태로 일체 조립하여 바퀴로 이동시키는 시스템입니다. 플라잉폼과 달리 크레인 없이 작업자가 밀어서 이동 가능하며, 조립·해체가 간편하고 반복 사용에 유리합니다. 주로 공동주택·오피스 슬래브 시공에 사용되며, 1개 테이블이 30~100㎡를 커버합니다. 콘크리트 양생 후 테이블을 낮춰 이동하므로 층고가 일정해야 하며, 계단·엘리베이터 구멍 등 개구부 위치를 고려한 설계가 필요합니다. 통역 시 주의점은 테이블폼 이동 시 바닥 평탄도·경사를 확인하고, 지지다리(shore leg) 안전성과 콘크리트 양생 강도를 반드시 체크해야 함을 강조해야 합니다.",
        "meaningVi": "Table Form là hệ thống lắp ráp liền khối ván khuôn dưới sàn, dầm thành hình bàn và di chuyển bằng bánh xe. Khác với flying form, không cần cần trục mà công nhân đẩy di chuyển được, lắp tháo đơn giản và có lợi khi tái sử dụng nhiều lần. Chủ yếu dùng cho thi công sàn chung cư, văn phòng, một bàn phủ 30~100㎡. Sau khi bê tông đông cứng hạ bàn xuống rồi di chuyển nên chiều cao tầng phải đồng đều, cần thiết kế xem xét vị trí lỗ mở như cầu thang, hố thang máy.",
        "context": "슬래브 시공, 반복 평면",
        "contextVi": "Thi công sàn, mặt bằng lặp lại",
        "commonMistakes": [
            {
                "mistake": "\"테이블폼\"을 단순 \"ván khuôn bàn\"로 번역",
                "correction": "\"gia công sàn bàn\" 또는 \"table form\"",
                "explanation": "ván khuôn bàn은 직역, gia công sàn bàn이 시스템 명칭"
            },
            {
                "mistake": "콘크리트 양생 강도 미확인하고 테이블 해체",
                "correction": "최소 5MPa(보통 3일) 이상 확인 후 해체",
                "explanation": "조기 해체 시 슬래브 처짐·균열 발생"
            },
            {
                "mistake": "바닥 경사·장애물 무시하고 테이블 이동",
                "correction": "이동 전 바닥 평탄도·경사·장애물 제거",
                "explanation": "경사 이동 시 테이블 전도 위험"
            }
        ],
        "culturalNote": "한국은 1990년대부터 테이블폼이 아파트·오피스 슬래브 시공의 표준이 되었으며, 대형 건설사는 자체 테이블폼을 보유합니다. 베트남은 최근 10년간 한국 기술 도입으로 고층 프로젝트에 적용 중이나, 유로폼 병행도 많습니다. 한국 현장에서는 테이블폼 조립·이동·해체를 전문팀이 수행하며, 안전 매뉴얼이 엄격합니다.",
        "examples": [
            {
                "ko": "이 슬래브는 테이블폼 12개로 시공하며, 3일 후 해체합니다.",
                "vi": "Sàn này thi công bằng 12 table form, sau 3 ngày tháo dỡ.",
                "situation": "formal"
            },
            {
                "ko": "테이블폼 밀기 전에 바닥 깨끗하게 치웠어?",
                "vi": "Trước khi đẩy table form dọn sạch sàn chưa?",
                "situation": "onsite"
            },
            {
                "ko": "테이블폼은 층고 3m 기준으로 설계되었으니 변경 시 재조정 필요합니다.",
                "vi": "Table form được thiết kế theo chiều cao tầng 3m nên khi thay đổi cần điều chỉnh lại.",
                "situation": "formal"
            }
        ],
        "relatedTerms": [
            "플라잉폼",
            "슬래브거푸집",
            "지지다리"
        ]
    },
    {
        "slug": "gia-cong-go",
        "korean": "목재폼",
        "vietnamese": "gia công gỗ",
        "hanja": "木材form",
        "hanjaReading": "목(나무 목) + 재(재료 재)",
        "pronunciation": "지아 꽁 고",
        "meaningKo": "목재(합판·각재·동바리)로 제작하는 전통적인 거푸집으로, 현장 맞춤 제작이 가능하여 복잡한 형상·곡선·특수 구조에 적합합니다. 유로폼도 목재폼의 일종이나, 여기서는 합판을 직접 재단·조립하는 재래식 방식을 의미합니다. 초기 비용이 낮고 시공이 유연하나, 재사용 횟수가 적고(5~10회) 정밀도가 떨어지며 인건비가 많이 듭니다. 통역 시 주의점은 목재폼은 시스템폼에 비해 정밀도·속도·안전성이 낮으므로 소규모 현장이나 특수 구조에 한정하고, 합판 두께·각재 간격·동바리 지지력을 반드시 확인해야 함을 강조해야 합니다.",
        "meaningVi": "Ván khuôn chế tạo bằng gỗ (ván ép, gỗ vuông, chống đỡ), có thể chế tạo theo yêu cầu hiện trường nên phù hợp cho hình dạng phức tạp, đường cong, kết cấu đặc biệt. Euroform cũng là loại ván khuôn gỗ nhưng ở đây chỉ cách truyền thống cắt, lắp ráp ván ép trực tiếp. Chi phí ban đầu thấp và thi công linh hoạt nhưng số lần tái sử dụng ít (5~10 lần), độ chính xác kém và tốn nhiều nhân công.",
        "context": "소규모 현장, 특수 구조",
        "contextVi": "Công trường nhỏ, kết cấu đặc biệt",
        "commonMistakes": [
            {
                "mistake": "\"목재폼\"을 단순 \"ván khuôn gỗ\"로만 번역",
                "correction": "\"gia công gỗ\" 또는 \"ván khuôn gỗ truyền thống\"",
                "explanation": "ván khuôn gỗ는 일반 명칭, 전통 방식임을 명시"
            },
            {
                "mistake": "시스템폼과 목재폼을 동등하게 비교",
                "correction": "목재폼은 정밀도·재사용성·속도가 낮음을 명시",
                "explanation": "목재폼은 보조·특수 구조용, 시스템폼이 주류"
            },
            {
                "mistake": "합판 두께·등급을 무시하고 시공",
                "correction": "콘크리트용 합판 12~18mm, KS 인증 확인",
                "explanation": "얇은 합판 사용 시 콘크리트 압력으로 변형·파손"
            }
        ],
        "culturalNote": "한국은 1990년대까지 목재폼이 주류였으나, 현재는 유로폼·시스템폼으로 대체되어 특수 구조·소규모 현장에만 사용됩니다. 베트남은 여전히 저층·농촌 건축에 목재폼이 많이 사용되며, 합판 품질 편차가 큽니다. 한국 현장에서는 목재폼 사용 시 안전 점검이 강화되며, 대형 현장에서는 거의 사용하지 않습니다.",
        "examples": [
            {
                "ko": "이 곡선 벽체는 목재폼으로 현장 제작하여 시공합니다.",
                "vi": "Tường cong này chế tạo ván khuôn gỗ tại chỗ để thi công.",
                "situation": "formal"
            },
            {
                "ko": "목재폼 쓰니까 인건비가 많이 나가네. 다음부턴 시스템폼 쓰자.",
                "vi": "Dùng ván khuôn gỗ nên nhân công tốn nhiều. Lần sau dùng system form.",
                "situation": "onsite"
            },
            {
                "ko": "목재폼 합판은 18mm 콘크리트용으로 준비하세요.",
                "vi": "Ván ép cho ván khuôn gỗ chuẩn bị loại 18mm cho bê tông.",
                "situation": "formal"
            }
        ],
        "relatedTerms": [
            "유로폼",
            "합판",
            "동바리"
        ]
    },
    {
        "slug": "gia-cong-dac-biet",
        "korean": "특수폼",
        "vietnamese": "gia công đặc biệt",
        "hanja": "特殊form",
        "hanjaReading": "특(특별할 특) + 수(특이할 수)",
        "pronunciation": "지아 꽁 닥 비엣",
        "meaningKo": "특수폼은 곡면·사선·조형 등 일반 거푸집으로 시공이 어려운 특수 형상을 위한 맞춤형 거푸집입니다. FRP(섬유강화플라스틱)·스티로폼·3D 프린팅·CNC 가공 등 다양한 재료와 기술을 활용하며, 랜드마크 건축물·공연장·미술관·교량 아치 등에 사용됩니다. 설계·제작·시공에 고도의 전문 기술이 필요하고 비용이 높으나, 건축적 완성도와 독창성을 구현할 수 있습니다. 통역 시 주의점은 특수폼은 구조 계산·시공 시뮬레이션·Mock-up 검증이 필수이며, 노출콘크리트인 경우 표면 마감 품질 관리가 매우 중요함을 강조해야 합니다.",
        "meaningVi": "Ván khuôn đặc biệt là ván khuôn gia công theo yêu cầu cho hình dạng đặc biệt khó thi công bằng ván khuôn thường như mặt cong, xiên, tạo hình. Sử dụng nhiều vật liệu và công nghệ như FRP (nhựa gia cường sợi thủy tinh), xốp, in 3D, gia công CNC, dùng cho công trình biểu tượng, nhà hát, bảo tàng, vòm cầu. Cần kỹ thuật chuyên môn cao trong thiết kế, chế tạo, thi công và chi phí cao nhưng có thể hiện thực hóa hoàn thiện kiến trúc và tính độc đáo.",
        "context": "조형 건축, 곡면 구조",
        "contextVi": "Kiến trúc tạo hình, kết cấu cong",
        "commonMistakes": [
            {
                "mistake": "\"특수폼\"을 단순 \"ván khuôn đặc biệt\"로만 번역",
                "correction": "\"gia công đặc biệt\" 또는 \"special formwork\"",
                "explanation": "ván khuôn đặc biệt은 직역, gia công이 시스템 개념"
            },
            {
                "mistake": "Mock-up 없이 본 시공 진행",
                "correction": "특수폼은 반드시 1:1 실물 Mock-up 검증 필수",
                "explanation": "복잡한 형상은 Mock-up 없이 품질 보장 불가"
            },
            {
                "mistake": "FRP·스티로폼 특수폼을 일반 거푸집처럼 취급",
                "correction": "재료별 콘크리트 압력 한계·탈형 시점 다름",
                "explanation": "FRP는 고압 가능, 스티로폼은 저압만 적용"
            }
        ],
        "culturalNote": "한국은 동대문디자인플라자·롯데월드타워 등 랜드마크 건축에 특수폼 기술이 축적되어 있으며, FRP·3D 프린팅 기술이 발전했습니다. 베트남은 특수폼 수요가 적고 대부분 외국 기술에 의존하며, 오페라하우스 등 일부 프로젝트에만 적용됩니다. 한국 현장에서는 특수폼 제작사와 설계사·시공사의 긴밀한 협업이 필수입니다.",
        "examples": [
            {
                "ko": "이 곡면 지붕은 FRP 특수폼으로 제작하여 노출콘크리트로 마감합니다.",
                "vi": "Mái cong này chế tạo bằng ván khuôn đặc biệt FRP và hoàn thiện bằng bê tông kiến trúc.",
                "situation": "formal"
            },
            {
                "ko": "특수폼 목업 검증 통과했어? 본 시공 들어가도 돼?",
                "vi": "Mock-up ván khuôn đặc biệt đã qua kiểm tra chưa? Vào thi công chính được chưa?",
                "situation": "onsite"
            },
            {
                "ko": "이 아치는 3D 스캔 데이터로 CNC 가공한 특수폼을 사용합니다.",
                "vi": "Vòm này dùng ván khuôn đặc biệt gia công CNC từ dữ liệu quét 3D.",
                "situation": "formal"
            }
        ],
        "relatedTerms": [
            "노출콘크리트",
            "FRP",
            "Mock-up"
        ]
    }
]


def main():
    """
    Construction Formwork Terms Addition
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

    print("[SUCCESS] ✅ 10 construction formwork terms added (Tier S compliant)")
    print("\n[ADDED TERMS]")
    for idx, term in enumerate(data, 1):
        print(f"  {idx}. {term['korean']} ({term['slug']})")


if __name__ == "__main__":
    main()
