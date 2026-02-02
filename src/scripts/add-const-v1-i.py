#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
건설(Construction) 도메인 용어 추가 스크립트 - v1-i
테마: 도로/교량/포장 (Road, Bridge & Pavement)
생성일: 2025-02-02
"""

import json
import os

# 프로젝트 루트 기준 상대 경로
script_dir = os.path.dirname(os.path.abspath(__file__))
project_root = os.path.abspath(os.path.join(script_dir, "..", ".."))
file_path = os.path.join(project_root, "src", "data", "terms", "construction.json")

# 신규 용어 10개 (도로/교량/포장)
new_terms = [
    {
        "slug": "mat-duong-asphalt",
        "korean": "아스팔트",
        "vietnamese": "Bê tông nhựa",
        "hanja": "瀝靑",
        "hanjaReading": "瀝(물방울 력) 靑(푸를 청)",
        "pronunciation": "아스팔트",
        "meaningKo": "원유를 증류하여 얻는 검은색 점성 물질로, 도로 포장재로 널리 사용됩니다. 통역 시 '아스팔트'와 '역청(瀝靑)'을 혼용하는 경우가 있으니 주의가 필요합니다. 한국에서는 '아스팔트 콘크리트(Asphalt Concrete)'를 줄여 '아스콘'이라 부르며, 베트남에서는 'Bê tông nhựa' 또는 'Nhựa đường'으로 표현합니다. 시공 온도, 배합 비율, 다짐 방법 등 기술적 세부사항을 정확히 통역해야 하며, 특히 품질 기준(KS, TCVN)의 차이를 구분해야 합니다.",
        "meaningVi": "Chất kết dính màu đen có tính nhớt, thu được từ quá trình chưng cất dầu mỏ, được sử dụng rộng rãi làm vật liệu lát mặt đường. Còn gọi là 'nhựa đường' trong ngữ cảnh thi công.",
        "context": "도로 포장, 아스팔트 플랜트, 포장 시공 현장에서 사용",
        "difficulty": "medium",
        "culturalNote": "한국은 아스팔트 포장 도로가 98% 이상으로 매우 높은 반면, 베트남은 콘크리트 포장과 아스팔트 포장이 혼재되어 있습니다. 한국의 '아스콘' 용어는 베트남에서 통용되지 않으며, 'Bê tông nhựa' 또는 'Nhựa đường'으로 명확히 구분해야 합니다. 또한 열대 기후인 베트남은 고온에 강한 개질 아스팔트(Nhựa đường cải tiến)를 많이 사용하는 반면, 한국은 사계절 온도 변화에 대응하는 배합을 사용합니다.",
        "commonMistakes": [
            {
                "mistake": "아스팔트를 'Nhựa' 하나로만 번역",
                "correction": "'Bê tông nhựa' 또는 'Nhựa đường'으로 완전히 표현",
                "explanation": "'Nhựa'만으로는 '플라스틱'으로 오해될 수 있음"
            },
            {
                "mistake": "아스콘을 베트남어로 음차 그대로 번역",
                "correction": "맥락에 따라 'Bê tông nhựa' 또는 'Asphalt Concrete' 병기",
                "explanation": "베트남에서는 '아스콘'이라는 약어가 통용되지 않음"
            },
            {
                "mistake": "개질 아스팔트를 일반 아스팔트와 구분하지 않음",
                "correction": "'Nhựa đường cải tiến' 또는 'SBS 개질 아스팔트' 등 명확히 구분",
                "explanation": "품질과 단가가 크게 다르므로 계약서에서 명확히 구분 필수"
            }
        ],
        "examples": [
            {
                "ko": "아스팔트 포장은 150도 이상의 고온에서 시공됩니다.",
                "vi": "Lát mặt đường bê tông nhựa được thi công ở nhiệt độ trên 150°C.",
                "situation": "onsite"
            },
            {
                "ko": "개질 아스팔트는 일반 아스팔트 대비 내구성이 30% 향상됩니다.",
                "vi": "Nhựa đường cải tiến có độ bền tăng 30% so với nhựa đường thông thường.",
                "situation": "formal"
            },
            {
                "ko": "오늘 아스콘 300톤 들어올 예정입니다.",
                "vi": "Hôm nay dự kiến nhận 300 tấn bê tông nhựa (Asphalt Concrete).",
                "situation": "informal"
            }
        ],
        "relatedTerms": ["포장", "교량", "도로", "콘크리트"]
    },
    {
        "slug": "mat-duong-pho-trang",
        "korean": "포장",
        "vietnamese": "Mặt đường",
        "hanja": "鋪裝",
        "hanjaReading": "鋪(펼 포) 裝(꾸밀 장)",
        "pronunciation": "포장",
        "meaningKo": "도로나 광장의 표면을 아스팔트, 콘크리트 등으로 덮어 평탄하고 견고하게 만드는 작업 또는 그 결과물입니다. 통역 시 '포장'은 단순히 표면을 덮는 것이 아니라, 노반-노상-기층-표층의 다층 구조를 의미하므로 각 층의 역할을 이해해야 합니다. 한국에서는 '아스팔트 포장(Asphalt Pavement)', '콘크리트 포장(Concrete Pavement)', '블록 포장(Block Pavement)' 등으로 구분하며, 베트남에서도 'Mặt đường nhựa', 'Mặt đường bê tông', 'Gạch lát' 등으로 세분화됩니다. 시공 순서와 품질 기준을 정확히 전달해야 합니다.",
        "meaningVi": "Công tác hoặc kết quả của việc bao phủ bề mặt đường hoặc quảng trường bằng vật liệu như nhựa đường, bê tông để tạo bề mặt phẳng và kiên cố.",
        "context": "도로 건설, 토목 설계, 시공 현장, 유지 관리에서 사용",
        "difficulty": "medium",
        "culturalNote": "한국은 아스팔트 포장이 대부분이며 20-30년 주기로 재포장을 실시하는 반면, 베트남은 콘크리트 포장 비율이 상대적으로 높고 유지 관리 주기가 짧습니다. 한국의 '포장 파손'은 주로 동결융해에 의한 균열인 반면, 베트남은 고온과 다습으로 인한 소성변형(Biến dạng dẻo)이 주요 문제입니다. 또한 한국은 '포장 두께 설계'에 AASHTO 기준을 많이 사용하나, 베트남은 자체 TCVN 기준을 따르므로 설계 기준의 차이를 명확히 해야 합니다.",
        "commonMistakes": [
            {
                "mistake": "포장을 'Đóng gói'(포장/포장재)로 번역",
                "correction": "'Mặt đường' 또는 'Lớp mặt' 사용",
                "explanation": "'Đóng gói'는 물건을 싸는 포장을 의미하며 도로 포장과 무관"
            },
            {
                "mistake": "포장 재시공을 'Sửa chữa'(수리)로만 표현",
                "correction": "'Tái lát mặt đường' 또는 'Phục hồi mặt đường'으로 구체화",
                "explanation": "단순 수리와 전면 재시공은 공법과 비용이 전혀 다름"
            },
            {
                "mistake": "포장 두께를 단순 '두께(Độ dày)'로만 표현",
                "correction": "'Chiều dày lớp mặt' 또는 'Chiều dày kết cấu áo đường'",
                "explanation": "포장은 다층 구조이므로 어느 층의 두께인지 명확히 해야 함"
            }
        ],
        "examples": [
            {
                "ko": "이 도로는 아스팔트 포장으로 총 연장 5km입니다.",
                "vi": "Con đường này có mặt đường nhựa với tổng chiều dài 5km.",
                "situation": "formal"
            },
            {
                "ko": "포장 두께는 표층 5cm, 기층 15cm로 설계되었습니다.",
                "vi": "Chiều dày mặt đường được thiết kế lớp mặt 5cm, lớp móng 15cm.",
                "situation": "formal"
            },
            {
                "ko": "포장 파손이 심해서 내일부터 재포장 공사 들어갑니다.",
                "vi": "Do mặt đường hư hỏng nghiêm trọng, từ ngày mai sẽ bắt đầu công tác tái lát mặt đường.",
                "situation": "onsite"
            }
        ],
        "relatedTerms": ["아스팔트", "콘크리트", "도로", "교량"]
    },
    {
        "slug": "tru-cau-giao-gak",
        "korean": "교각",
        "vietnamese": "Trụ cầu",
        "hanja": "橋脚",
        "hanjaReading": "橋(다리 교) 脚(다리 각)",
        "pronunciation": "교각",
        "meaningKo": "교량의 상부 구조를 지지하기 위해 하부에 설치하는 수직 또는 경사 구조물로, 교량의 하중을 기초로 전달하는 역할을 합니다. 통역 시 교각(橋脚)과 교대(橋臺, Mố cầu)를 명확히 구분해야 하며, 교각은 중간 지점의 '기둥'이고 교대는 양 끝단의 '받침대' 역할입니다. 한국에서는 T형 교각, 벽식 교각, 라멘 교각 등 형식을 세분화하고, 베트남에서도 'Trụ cầu chữ T', 'Trụ cầu tường', 'Trụ cầu khung' 등으로 구분합니다. 내진 설계, 세굴(Xói lở) 방지 등 안전 관련 용어를 정확히 전달해야 합니다.",
        "meaningVi": "Cấu trúc dọc hoặc nghiêng được lắp đặt ở phần dưới để đỡ kết cấu phần trên của cầu, truyền tải trọng xuống móng.",
        "context": "교량 건설, 구조 설계, 시공 현장, 유지 관리에서 사용",
        "difficulty": "medium",
        "culturalNote": "한국은 지진 대비 내진 설계를 필수로 적용하며, 교각의 연성(Độ dẻo)과 탄성(Độ đàn hồi)을 중시합니다. 반면 베트남은 지진 빈도가 낮아 내진 설계보다는 홍수와 세굴(Xói lở) 방지에 더 중점을 둡니다. 한국의 교각은 주로 철근콘크리트(BTCT) 또는 PSC(Bê tông ứng suất trước)로 시공되며, 베트남도 유사하나 시공 품질 관리 기준에 차이가 있습니다. 또한 한국은 '교각 번호(Pier No.)'를 P1, P2 형식으로 표기하나, 베트남은 'Trụ T1, T2' 등으로 표기하는 경우가 많아 도면 해석 시 주의가 필요합니다.",
        "commonMistakes": [
            {
                "mistake": "교각과 교대를 모두 'Trụ cầu'로만 번역",
                "correction": "교각은 'Trụ cầu', 교대는 'Mố cầu'로 구분",
                "explanation": "교각은 중간 지지 기둥, 교대는 양 끝단 받침대로 구조와 역할이 다름"
            },
            {
                "mistake": "교각 형식을 단순히 '종류(Loại)'로만 표현",
                "correction": "'Dạng trụ cầu' 또는 'Kiểu trụ cầu'로 구체화",
                "explanation": "T형, 벽식, 라멘 등 형식별로 시공법과 비용이 크게 다름"
            },
            {
                "mistake": "세굴을 'Xói mòn'(침식)으로 표현",
                "correction": "'Xói lở' 또는 'Xói lòng sông'으로 정확히 표현",
                "explanation": "'Xói lở'는 물 흐름에 의한 교각 기초 유실을 의미하며, 단순 침식과 다름"
            }
        ],
        "examples": [
            {
                "ko": "이 교량은 총 5개의 교각으로 지지됩니다.",
                "vi": "Cây cầu này được đỡ bởi tổng cộng 5 trụ cầu.",
                "situation": "formal"
            },
            {
                "ko": "교각의 세굴 방지를 위해 석축(Đá gia cố) 보강이 필요합니다.",
                "vi": "Cần gia cố đá để chống xói lở cho trụ cầu.",
                "situation": "formal"
            },
            {
                "ko": "P3 교각 콘크리트 타설 내일 오전에 시작합니다.",
                "vi": "Đổ bê tông trụ cầu P3 bắt đầu vào sáng mai.",
                "situation": "onsite"
            }
        ],
        "relatedTerms": ["교량", "교대", "콘크리트", "기초"]
    },
    {
        "slug": "mo-cau-gyo-dae",
        "korean": "교대",
        "vietnamese": "Mố cầu",
        "hanja": "橋臺",
        "hanjaReading": "橋(다리 교) 臺(대 대)",
        "pronunciation": "교대",
        "meaningKo": "교량의 양 끝단에 위치하여 상부 구조물을 받치고, 토압을 지지하며, 도로와 교량을 연결하는 구조물입니다. 통역 시 교대(橋臺)는 교각(橋脚, Trụ cầu)과 달리 '측면 토압'을 견뎌야 하므로 구조적 기능이 다릅니다. 한국에서는 중력식 교대(Mố cầu trọng lực), 역T형 교대(Mố cầu chữ T ngược), 라멘 교대 등으로 구분하며, 베트남에서도 유사한 분류를 사용합니다. 뒤채움(Đắp lưng), 배수(Thoát nước), 신축이음(Khe co giãn) 등 연관 시공 요소를 함께 이해해야 합니다.",
        "meaningVi": "Cấu trúc nằm ở hai đầu cầu, đỡ kết cấu phần trên, chịu áp lực đất và kết nối đường với cầu.",
        "context": "교량 건설, 토목 설계, 시공 현장에서 사용",
        "difficulty": "medium",
        "culturalNote": "한국은 교대 설계 시 동결심도(Độ sâu đóng băng)를 고려하여 기초 깊이를 결정하지만, 베트남은 동결 문제가 없어 이를 고려하지 않습니다. 대신 베트남은 연약 지반(Nền đất yếu)과 침하(Lún) 문제가 많아 교대 침하 방지 대책이 더 중요합니다. 또한 한국은 교대 뒤채움을 양질토(Đất tốt)로 다짐 시공하지만, 베트남은 뒤채움 재료와 다짐 품질이 불량한 경우가 많아 침하 사고가 빈발합니다. 통역 시 '뒤채움 다짐도(Độ chặt đắp lưng)' 기준을 명확히 전달해야 합니다.",
        "commonMistakes": [
            {
                "mistake": "교대를 'Trụ cầu'로 번역",
                "correction": "'Mố cầu'로 정확히 표현",
                "explanation": "교대(Mố cầu)는 양 끝단, 교각(Trụ cầu)은 중간 지지물"
            },
            {
                "mistake": "뒤채움을 'Lấp đất'(흙 덮기)로만 표현",
                "correction": "'Đắp lưng mố cầu' 또는 'Đắp đất sau mố'",
                "explanation": "단순 흙 덮기가 아니라 다짐과 배수를 포함한 기술적 시공"
            },
            {
                "mistake": "교대 침하를 'Lún'(일반 침하)로만 표현",
                "correction": "'Lún mố cầu' 또는 'Lún kết cấu mố'로 구체화",
                "explanation": "교대 침하는 교량 전체 안전에 치명적이므로 명확히 구분"
            }
        ],
        "examples": [
            {
                "ko": "A1 교대는 중력식으로 설계되었습니다.",
                "vi": "Mố cầu A1 được thiết kế dạng trọng lực.",
                "situation": "formal"
            },
            {
                "ko": "교대 뒤채움은 다짐도 95% 이상으로 시공해야 합니다.",
                "vi": "Đắp lưng mố cầu phải thi công với độ chặt trên 95%.",
                "situation": "formal"
            },
            {
                "ko": "교대 콘크리트 양생 끝나면 뒤채움 시작합니다.",
                "vi": "Sau khi bê tông mố cầu dưỡng hộ xong sẽ bắt đầu đắp lưng.",
                "situation": "onsite"
            }
        ],
        "relatedTerms": ["교각", "교량", "콘크리트", "기초"]
    },
    {
        "slug": "day-psc-girder",
        "korean": "PSC거더",
        "vietnamese": "Dầm PSC",
        "hanja": None,
        "hanjaReading": None,
        "pronunciation": "피에스씨 거더",
        "meaningKo": "Pre-Stressed Concrete Girder의 약어로, 미리 응력을 가한 프리스트레스 콘크리트 보를 의미합니다. 통역 시 PSC는 'Bê tông ứng suất trước'이며, 일반 철근콘크리트(RC)와 달리 인장력을 미리 가해 균열을 방지하고 더 긴 경간(Nhịp)을 지지할 수 있습니다. 한국에서는 교량 상부 구조로 PSC거더를 널리 사용하며, I형, Box형, T형 등 단면 형식이 다양합니다. 베트남에서도 'Dầm PSC' 또는 'Dầm bê tông ứng suất trước'로 표현하며, 프리텐션(Tiền ứng lực) 방식과 포스트텐션(Hậu ứng lực) 방식을 구분해야 합니다.",
        "meaningVi": "Viết tắt của Pre-Stressed Concrete Girder, là dầm bê tông được căng ứng suất trước để chống nứt và chịu được nhịp dài hơn.",
        "context": "교량 건설, 구조 설계, PSC 제작장에서 사용",
        "difficulty": "hard",
        "culturalNote": "한국은 PSC거더 제작을 전문 공장(Nhà máy)에서 표준화된 품질 관리 하에 생산하며, 현장까지 트레일러로 운송합니다. 반면 베트남은 현장 제작(Chế tạo tại chỗ)이 많고, 품질 관리 수준이 공장 제작보다 낮은 경우가 있습니다. 한국은 PSC거더 길이가 40m 이상인 경우가 많으나, 베트남은 운송 여건상 30m 이하가 대부분입니다. 또한 한국은 '프리스트레스 도입(Căng ứng suất)' 작업을 유압잭(Kích thủy lực)으로 정밀하게 수행하지만, 베트남은 장비와 기술 수준의 차이로 품질 편차가 큽니다.",
        "commonMistakes": [
            {
                "mistake": "PSC를 음차 그대로 'PSC' 또는 '피에스씨'로 발음",
                "correction": "'Dầm PSC' 또는 'Dầm bê tông ứng suất trước'로 설명",
                "explanation": "베트남 현장에서는 약어만으로는 이해하지 못하는 경우 많음"
            },
            {
                "mistake": "프리텐션과 포스트텐션을 구분하지 않음",
                "correction": "프리텐션은 'Tiền ứng lực', 포스트텐션은 'Hậu ứng lực'",
                "explanation": "시공 순서와 품질 관리 방법이 완전히 다름"
            },
            {
                "mistake": "긴장재를 'Thép căng'(인장 강재)로만 표현",
                "correction": "'Cáp dự ứng lực' 또는 'Thép cường độ cao'",
                "explanation": "일반 철근과 고강도 긴장재는 재질과 용도가 다름"
            }
        ],
        "examples": [
            {
                "ko": "이번 교량은 40m PSC거더를 사용합니다.",
                "vi": "Cây cầu này sử dụng dầm PSC dài 40m.",
                "situation": "formal"
            },
            {
                "ko": "PSC거더 긴장 작업은 콘크리트 강도가 40MPa 이상일 때 실시합니다.",
                "vi": "Công tác căng ứng suất dầm PSC được thực hiện khi cường độ bê tông đạt trên 40MPa.",
                "situation": "formal"
            },
            {
                "ko": "내일 PSC거더 5개 현장 반입됩니다.",
                "vi": "Ngày mai sẽ vận chuyển 5 dầm PSC vào công trường.",
                "situation": "onsite"
            }
        ],
        "relatedTerms": ["교량", "콘크리트", "프리스트레스", "거더"]
    },
    {
        "slug": "ung-suat-truoc-psc",
        "korean": "프리스트레스",
        "vietnamese": "Ứng suất trước",
        "hanja": None,
        "hanjaReading": None,
        "pronunciation": "프리스트레스",
        "meaningKo": "콘크리트에 하중이 작용하기 전에 미리 압축 응력을 가하여, 인장 응력을 상쇄시키고 균열을 방지하는 기술입니다. 통역 시 'Pre-stress'는 'Ứng suất trước'이며, PSC(Pre-Stressed Concrete) 구조물의 핵심 원리입니다. 한국에서는 프리텐션(Tiền ứng lực) 방식과 포스트텐션(Hậu ứng lực) 방식으로 구분하며, 긴장재(Cáp dự ứng lực)를 사용해 응력을 도입(Căng ứng suất)합니다. 베트남에서도 'Căng ứng suất trước' 또는 'Dự ứng lực'으로 표현하며, 긴장력(Lực căng), 정착(Neo cố định), 그라우팅(Phun vữa) 등 세부 용어를 정확히 알아야 합니다.",
        "meaningVi": "Kỹ thuật tạo ứng suất nén trước trong bê tông để triệt tiêu ứng suất kéo và chống nứt khi chịu tải trọng.",
        "context": "PSC 구조물 설계, 제작, 시공 현장에서 사용",
        "difficulty": "hard",
        "culturalNote": "한국은 프리스트레스 기술이 1970년대부터 도입되어 표준화되었으며, 고속도로 교량 대부분이 PSC 구조입니다. 반면 베트남은 2000년대 이후 본격 도입되어 기술 숙련도가 상대적으로 낮고, 긴장재 정착(Neo cố định) 불량이나 그라우팅(Phun vữa) 미흡으로 인한 품질 문제가 종종 발생합니다. 한국은 긴장 작업을 유압잭(Kích thủy lực)과 전자 제어 시스템으로 정밀하게 수행하지만, 베트남은 수동 작업이 많아 긴장력 편차가 큽니다. 통역 시 '긴장 순서(Trình tự căng)'와 '긴장력 관리(Quản lý lực căng)'의 중요성을 강조해야 합니다.",
        "commonMistakes": [
            {
                "mistake": "프리스트레스를 'Căng trước'(미리 당김)로 단순 번역",
                "correction": "'Ứng suất trước' 또는 'Dự ứng lực'으로 기술 용어 사용",
                "explanation": "'Căng trước'는 일반적 표현이며 공학적 의미 전달 불가"
            },
            {
                "mistake": "긴장재를 '철근(Thép)'으로 표현",
                "correction": "'Cáp dự ứng lực' 또는 'Thép cường độ cao'",
                "explanation": "일반 철근과 고강도 긴장재는 재질, 강도, 용도가 다름"
            },
            {
                "mistake": "긴장력 손실을 '손실(Mất mát)'로만 표현",
                "correction": "'Mất mát ứng suất' 또는 'Suy giảm lực căng'",
                "explanation": "긴장력 손실은 설계에 반드시 반영해야 할 기술적 요소"
            }
        ],
        "examples": [
            {
                "ko": "프리스트레스 도입은 콘크리트 강도가 설계 기준에 도달한 후 실시합니다.",
                "vi": "Căng ứng suất trước được thực hiện sau khi cường độ bê tông đạt tiêu chuẩn thiết kế.",
                "situation": "formal"
            },
            {
                "ko": "긴장력 손실을 고려하여 초기 긴장력을 10% 높게 설정합니다.",
                "vi": "Xét đến mất mát ứng suất, lực căng ban đầu được thiết lập cao hơn 10%.",
                "situation": "formal"
            },
            {
                "ko": "내일 오전에 1차 긴장 작업 시작합니다.",
                "vi": "Sáng mai bắt đầu công tác căng giai đoạn 1.",
                "situation": "onsite"
            }
        ],
        "relatedTerms": ["PSC거더", "콘크리트", "교량", "거더"]
    },
    {
        "slug": "cong-tac-tam-ga-si-seol",
        "korean": "가시설",
        "vietnamese": "Công trình tạm",
        "hanja": "假施設",
        "hanjaReading": "假(거짓 가) 施(베풀 시) 設(베풀 설)",
        "pronunciation": "가시설",
        "meaningKo": "건설 공사를 위해 임시로 설치하는 구조물이나 설비로, 공사 완료 후 철거됩니다. 통역 시 가시설(假施設)은 영구 구조물이 아닌 '임시 시설'이며, 흙막이(Tường chắn đất tạm), 동바리(Cột chống), 비계(Giàn giáo), 가설 도로(Đường tạm), 가설 사무소(Văn phòng tạm) 등을 포함합니다. 한국에서는 가시설 설계 시 안전 기준을 엄격히 적용하며, 베트남에서는 'Công trình tạm' 또는 'Kết cấu phụ tạm thời'로 표현합니다. 가시설 붕괴 사고가 빈번하므로 안전 관리와 정기 점검의 중요성을 강조해야 합니다.",
        "meaningVi": "Cấu trúc hoặc thiết bị được lắp đặt tạm thời để phục vụ thi công, sẽ được tháo dỡ sau khi hoàn thành công trình.",
        "context": "건설 현장, 토목 공사, 안전 관리에서 사용",
        "difficulty": "medium",
        "culturalNote": "한국은 가시설 설계 시 구조 계산과 안전 검토를 필수로 수행하며, 붕괴 사고 시 중대재해법 적용 대상입니다. 반면 베트남은 가시설을 '임시'로 간주하여 설계와 안전 관리가 소홀한 경우가 많고, 붕괴 사고 빈도가 높습니다. 한국은 가설 구조물 설치 전 '가설 계획서(Bản thiết kế tạm)'와 '구조 검토서(Báo cáo kiểm tra kết cấu)'를 제출해야 하지만, 베트남은 이러한 절차가 형식적인 경우가 많습니다. 통역 시 '가설 안전 점검(Kiểm tra an toàn công trình tạm)' 주기와 책임자를 명확히 해야 합니다.",
        "commonMistakes": [
            {
                "mistake": "가시설을 'Thiết bị tạm'(임시 장비)로 번역",
                "correction": "'Công trình tạm' 또는 'Kết cấu phụ tạm thời'",
                "explanation": "장비가 아닌 구조물을 의미하므로 'Công trình' 사용"
            },
            {
                "mistake": "비계를 'Thang'(사다리)으로 번역",
                "correction": "'Giàn giáo'로 정확히 표현",
                "explanation": "비계는 작업 발판이 있는 구조물이며, 사다리와 다름"
            },
            {
                "mistake": "동바리를 'Cột'(기둥)으로만 표현",
                "correction": "'Cột chống' 또는 'Giá đỡ tạm thời'",
                "explanation": "영구 기둥과 임시 지지 동바리는 구조와 용도가 다름"
            }
        ],
        "examples": [
            {
                "ko": "가시설 설치 후 구조 안전성 검토를 실시합니다.",
                "vi": "Sau khi lắp đặt công trình tạm, tiến hành kiểm tra an toàn kết cấu.",
                "situation": "formal"
            },
            {
                "ko": "이번 교량 공사는 가시설 비용이 총 공사비의 15%를 차지합니다.",
                "vi": "Trong công trình cầu này, chi phí công trình tạm chiếm 15% tổng chi phí xây dựng.",
                "situation": "formal"
            },
            {
                "ko": "가설 흙막이 철거는 다음 주부터 시작합니다.",
                "vi": "Tháo dỡ tường chắn đất tạm bắt đầu từ tuần sau.",
                "situation": "onsite"
            }
        ],
        "relatedTerms": ["동바리", "비계", "흙막이", "안전"]
    },
    {
        "slug": "cot-chong-dong-ba-ri",
        "korean": "동바리",
        "vietnamese": "Cột chống",
        "hanja": None,
        "hanjaReading": None,
        "pronunciation": "동바리",
        "meaningKo": "콘크리트 슬래브나 보를 타설할 때 거푸집을 지지하기 위해 임시로 설치하는 수직 지지대입니다. 통역 시 동바리는 'Cột chống' 또는 'Giá đỡ tạm thời'이며, 가시설의 일종입니다. 한국에서는 강재 동바리(Cột chống thép), 목재 동바리(Cột chống gỗ), 시스템 동바리(Cột chống hệ thống) 등으로 구분하며, 베트남에서도 유사한 분류를 사용합니다. 동바리 붕괴는 중대 사고로 이어지므로 설치 간격(Khoảng cách), 허용 하중(Tải trọng cho phép), 정기 점검(Kiểm tra định kỳ) 등을 정확히 전달해야 합니다.",
        "meaningVi": "Giá đỡ dọc lắp đặt tạm thời để chống đỡ ván khuôn khi đổ bê tông sàn hoặc dầm.",
        "context": "콘크리트 타설, 거푸집 공사, 건설 현장에서 사용",
        "difficulty": "medium",
        "culturalNote": "한국은 동바리 설치 시 구조 계산을 통해 간격과 하중을 정밀하게 설계하며, 시스템 동바리(Cột chống hệ thống)를 많이 사용합니다. 반면 베트남은 목재 동바리를 여전히 많이 사용하고, 간격과 하중 관리가 느슨하여 붕괴 사고가 빈번합니다. 한국은 동바리 제거 시 콘크리트 강도가 설계 기준(보통 70% 이상)에 도달해야 하며, 단계적으로 제거하지만, 베트남은 양생 기간을 충분히 지키지 않아 조기 붕괴 위험이 높습니다. 통역 시 '동바리 제거 시기(Thời điểm tháo cột chống)'와 '콘크리트 강도 확인(Kiểm tra cường độ bê tông)'의 중요성을 강조해야 합니다.",
        "commonMistakes": [
            {
                "mistake": "동바리를 'Cột'(기둥)으로만 번역",
                "correction": "'Cột chống' 또는 'Giá đỡ tạm thời'",
                "explanation": "영구 기둥과 임시 지지 동바리는 구조와 용도가 다름"
            },
            {
                "mistake": "동바리 간격을 단순 '간격(Khoảng cách)'으로만 표현",
                "correction": "'Khoảng cách cột chống' 또는 'Bước cột'",
                "explanation": "동바리 간격은 구조 안전에 직결되므로 명확히 구체화 필요"
            },
            {
                "mistake": "동바리 제거를 'Phá dỡ'(해체)로 표현",
                "correction": "'Tháo cột chống' 또는 'Gỡ giá đỡ'",
                "explanation": "'Phá dỡ'는 파괴적 해체를 의미하며, 동바리는 재사용 가능하므로 'Tháo' 사용"
            }
        ],
        "examples": [
            {
                "ko": "동바리 간격은 설계도에 따라 1.5m로 설치합니다.",
                "vi": "Khoảng cách cột chống được lắp đặt 1,5m theo bản vẽ thiết kế.",
                "situation": "formal"
            },
            {
                "ko": "콘크리트 강도가 70% 도달하면 동바리를 제거할 수 있습니다.",
                "vi": "Khi cường độ bê tông đạt 70%, có thể tháo cột chống.",
                "situation": "formal"
            },
            {
                "ko": "동바리 설치 끝나면 안전 점검 실시합니다.",
                "vi": "Sau khi lắp xong cột chống sẽ tiến hành kiểm tra an toàn.",
                "situation": "onsite"
            }
        ],
        "relatedTerms": ["가시설", "거푸집", "콘크리트", "안전"]
    },
    {
        "slug": "nhip-cau-ji-gan",
        "korean": "지간",
        "vietnamese": "Nhịp cầu",
        "hanja": "支間",
        "hanjaReading": "支(지탱할 지) 間(사이 간)",
        "pronunciation": "지간",
        "meaningKo": "교량에서 두 개의 지점(교각 또는 교대) 사이의 거리를 의미하며, 상부 구조물이 지지되는 구간입니다. 통역 시 지간(支間)은 'Nhịp cầu'이며, 교량 설계에서 가장 중요한 치수입니다. 한국에서는 '단경간(Nhịp đơn)', '연속경간(Nhịp liên tục)', '최대 지간(Nhịp lớn nhất)' 등으로 구분하며, 베트남에서도 'Nhịp đơn', 'Nhịp liên tục', 'Nhịp chính' 등으로 표현합니다. 지간 길이에 따라 상부 구조 형식(PSC거더, 강거더, 케이블 등)이 결정되므로, 설계와 시공에서 핵심적인 용어입니다.",
        "meaningVi": "Khoảng cách giữa hai điểm tựa (trụ cầu hoặc mố cầu) trên cầu, là đoạn mà kết cấu phần trên được đỡ.",
        "context": "교량 설계, 시공, 구조 계산에서 사용",
        "difficulty": "medium",
        "culturalNote": "한국은 고속도로 교량의 표준 지간이 40m 내외이며, 케이블교(Cầu dây văng)나 현수교(Cầu treo)의 경우 수백 미터에 달합니다. 반면 베트남은 지반 여건과 시공 능력 제약으로 30m 이하 지간이 대부분이며, 장대 교량은 주로 외국 기술 지원으로 건설됩니다. 한국은 '등간격 배치(Bố trí đều nhịp)'를 선호하여 시공 효율을 높이지만, 베트남은 지형과 지반 조건에 따라 불규칙한 지간 배치가 많습니다. 통역 시 '유효 지간(Nhịp thực tế)'과 '계산 지간(Nhịp tính toán)'의 차이를 명확히 해야 합니다.",
        "commonMistakes": [
            {
                "mistake": "지간을 'Khoảng cách'(일반 거리)로만 번역",
                "correction": "'Nhịp cầu' 또는 'Khoảng cách nhịp'",
                "explanation": "교량 구조에서 지간은 기술 용어이므로 'Nhịp' 사용 필수"
            },
            {
                "mistake": "경간과 지간을 구분하지 않음",
                "correction": "지간(Nhịp)은 구조적 거리, 경간(Khoảng nhịp)은 일반적 거리",
                "explanation": "설계 문서에서는 두 용어를 엄격히 구분"
            },
            {
                "mistake": "최대 지간을 'Nhịp lớn'으로만 표현",
                "correction": "'Nhịp lớn nhất' 또는 'Nhịp chính'",
                "explanation": "교량 전체에서 가장 긴 지간을 명확히 표현해야 함"
            }
        ],
        "examples": [
            {
                "ko": "이 교량은 40m 단순 지간 5개로 구성됩니다.",
                "vi": "Cây cầu này gồm 5 nhịp đơn 40m.",
                "situation": "formal"
            },
            {
                "ko": "최대 지간은 80m로 PSC Box Girder를 사용합니다.",
                "vi": "Nhịp lớn nhất là 80m, sử dụng dầm hộp PSC.",
                "situation": "formal"
            },
            {
                "ko": "지간이 길어서 추가 교각 설치가 필요합니다.",
                "vi": "Do nhịp dài nên cần lắp thêm trụ cầu.",
                "situation": "onsite"
            }
        ],
        "relatedTerms": ["교량", "교각", "PSC거더", "상부구조"]
    },
    {
        "slug": "chong-tham-mat-cau-gyo-myeon-bang-su",
        "korean": "교면방수",
        "vietnamese": "Chống thấm mặt cầu",
        "hanja": "橋面防水",
        "hanjaReading": "橋(다리 교) 面(낯 면) 防(막을 방) 水(물 수)",
        "pronunciation": "교면방수",
        "meaningKo": "교량 바닥판(슬래브)의 표면에 방수층을 설치하여 빗물이나 제설제가 콘크리트 내부로 침투하는 것을 방지하는 공법입니다. 통역 시 교면방수(橋面防水)는 'Chống thấm mặt cầu' 또는 'Lớp chống thấm sàn cầu'이며, 교량의 내구성(Độ bền)과 수명(Tuổi thọ)에 직결됩니다. 한국에서는 시트 방수(Chống thấm màng), 도막 방수(Chống thấm sơn), 침투성 방수(Chống thấm thấm sâu) 등 다양한 공법을 사용하며, 베트남에서도 유사한 분류가 있으나 시공 품질 관리가 중요합니다. 방수층 파손 시 콘크리트 열화(Lão hóa)와 철근 부식(Ăn mòn thép)이 발생하므로 시공과 검사의 중요성을 강조해야 합니다.",
        "meaningVi": "Công pháp lắp đặt lớp chống thấm trên bề mặt sàn cầu để ngăn nước mưa hoặc hóa chất tan băng thấm vào bê tông.",
        "context": "교량 건설, 포장 공사, 유지 관리에서 사용",
        "difficulty": "medium",
        "culturalNote": "한국은 겨울철 제설제(Hóa chất tan băng) 사용이 많아 교면방수를 필수로 시공하며, 방수층 손상 시 즉시 보수합니다. 반면 베트남은 제설제를 사용하지 않지만, 고온다습한 기후로 인해 빗물 침투와 콘크리트 열화 문제가 심각합니다. 한국은 방수층 시공 후 접착력(Lực dính) 시험과 수밀성(Độ kín nước) 시험을 필수로 실시하지만, 베트남은 이러한 품질 검사가 형식적인 경우가 많습니다. 또한 한국은 방수층 위에 아스팔트 포장을 2-3cm 두께로 시공하지만, 베트남은 포장 두께가 얇거나 없는 경우도 있어 방수층이 조기 파손됩니다.",
        "commonMistakes": [
            {
                "mistake": "교면방수를 'Chống thấm cầu'로만 번역",
                "correction": "'Chống thấm mặt cầu' 또는 'Lớp chống thấm sàn cầu'",
                "explanation": "교량 전체가 아닌 바닥판 표면 방수를 의미"
            },
            {
                "mistake": "방수층을 '방수(Chống thấm)'로만 표현",
                "correction": "'Lớp chống thấm' 또는 'Màng chống thấm'",
                "explanation": "방수는 개념이며, 방수층은 물리적 층(layer)을 의미"
            },
            {
                "mistake": "접착력을 'Dính'(붙음)로만 표현",
                "correction": "'Lực dính' 또는 'Độ bám dính'",
                "explanation": "접착력은 정량적 수치이므로 단순 형용사로는 부족"
            }
        ],
        "examples": [
            {
                "ko": "교면방수는 콘크리트 양생 완료 후 즉시 시공합니다.",
                "vi": "Lớp chống thấm mặt cầu được thi công ngay sau khi bê tông dưỡng hộ xong.",
                "situation": "formal"
            },
            {
                "ko": "방수층 시공 후 48시간 양생 후 포장 작업을 시작합니다.",
                "vi": "Sau khi thi công lớp chống thấm, dưỡng hộ 48 giờ rồi bắt đầu lát mặt đường.",
                "situation": "formal"
            },
            {
                "ko": "교면방수 접착력 시험 내일 오전에 실시합니다.",
                "vi": "Ngày mai sáng sẽ thực hiện thí nghiệm lực dính lớp chống thấm mặt cầu.",
                "situation": "onsite"
            }
        ],
        "relatedTerms": ["교량", "포장", "콘크리트", "방수"]
    }
]

def main():
    """메인 실행 함수"""
    try:
        # 기존 JSON 파일 읽기
        with open(file_path, "r", encoding="utf-8") as f:
            data = json.load(f)

        print(f"✅ 기존 파일 로드 완료: {len(data)} 용어")

        # 신규 용어 추가
        data.extend(new_terms)
        print(f"✅ 신규 용어 10개 추가 완료 (도로/교량/포장)")

        # JSON 파일 저장 (UTF-8, 들여쓰기 2칸, 한글 유지)
        with open(file_path, "w", encoding="utf-8") as f:
            json.dump(data, f, ensure_ascii=False, indent=2)

        print(f"✅ 파일 저장 완료: {file_path}")
        print(f"📊 총 용어 수: {len(data)}")

    except FileNotFoundError:
        print(f"❌ 파일을 찾을 수 없습니다: {file_path}")
    except json.JSONDecodeError:
        print(f"❌ JSON 파싱 오류: {file_path}")
    except Exception as e:
        print(f"❌ 오류 발생: {str(e)}")

if __name__ == "__main__":
    main()
