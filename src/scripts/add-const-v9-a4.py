#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
건설 용어 추가 스크립트 - 운반/양중 테마
타워크레인, 호이스트, 리프트카, 양중계획서, 신호수, 줄걸이, 샤클, 와이어로프, 체인블록, 수동호이스트
"""

import json
import os

# 운반/양중 테마 용어 10개 (Tier S 기준)
data = [
    {
        "slug": "cau-truc-thap",
        "korean": "타워크레인",
        "vietnamese": "cẩu tháp",
        "hanja": None,
        "hanjaReading": None,
        "pronunciation": "꺼우 탑",
        "meaningKo": "건설 현장에서 수직·수평으로 자재와 장비를 운반하는 대형 양중장비로, 높은 탑(mast)과 긴 붐(jib)으로 구성되어 고층 건물 시공에 필수적입니다. 통역 시 '타워크레인'은 'cẩu tháp' 또는 'cần cẩu tháp'으로 표현하며, 일반 이동식 크레인(mobile crane)과 구분해야 합니다. 타워크레인은 설치 방식에 따라 '정치식(고정식)'과 '레일식(주행식)'으로 나뉘며, 지지 방식에 따라 '독립식(free-standing)'과 '건물지지식(building-supported)'으로 구분됩니다. 한국 산업안전보건법에 따라 타워크레인은 설치·해체 시 작업계획서 제출, 안전검사(설치 후 1개월 이내), 월례 정기점검이 의무입니다. 주요 사양은 최대 인양하중(ton), 작업반경(m), 양정(m)으로 표시되며, 예를 들어 '10ton × 50m × 60m'는 최대 10톤을 50m 반경에서 60m 높이까지 인양 가능함을 의미합니다. 통역 시 운전원 자격(타워크레인운전기능사), 신호수 배치, 과부하방지장치, 권과방지장치 등 안전장치 작동 확인이 중요합니다.",
        "meaningVi": "Cẩu tháp (cần cẩu tháp) là thiết bị nâng hạ lớn dùng vận chuyển vật liệu và thiết bị theo phương dọc và ngang tại công trường, gồm cột tháp cao (mast) và tay cẩu dài (jib), thiết yếu cho thi công nhà cao tầng. Khác với cẩu di động (mobile crane), cẩu tháp cố định tại công trường. Theo cách lắp: cố định và di chuyển trên ray. Theo cách đỡ: độc lập và tựa vào tòa nhà. Thông số: tải trọng tối đa (ton), bán kính làm việc (m), độ cao nâng (m).",
        "context": "고층건축, 양중작업, 건설안전",
        "culturalNote": "한국은 타워크레인 안전관리를 매우 엄격하게 시행하며, 설치·해체 시 전문 업체(타워크레인 전문건설업) 의무 사용, 작업계획서 제출, 관할 관청 신고가 필수입니다. 월례 점검은 와이어로프 마모 상태, 브레이크 작동, 과부하방지장치, 권과방지장치를 중점 확인하며, 점검 기록을 5년간 보관합니다. 태풍·강풍 예보 시 타워크레인 작업을 즉시 중단하고, 붐을 바람 방향으로 자유회전(free slewing) 설정하여 전도를 방지합니다. 베트남은 타워크레인 안전관리가 느슨하며, 설치 시 구조계산서를 생략하거나 부적절한 앵커(anchor) 설치로 전도 사고가 빈발합니다. 운전원 자격증 없이 작업하는 경우도 많고, 과부하 운전, 신호수 없이 운전, 야간 조명 부족 등 안전 위반이 일상화되어 있습니다. 한국 감리는 타워크레인 안전검사증, 운전원 자격증, 월례 점검 기록을 철저히 확인하지만, 베트남 현장은 서류만 구비하고 실제 점검을 하지 않는 경우가 많아 통역 시 실제 점검 실시를 강력히 요구해야 합니다.",
        "commonMistakes": [
            {
                "mistake": "'타워크레인'을 'cần cẩu'(크레인 일반)로만 번역",
                "correction": "'cẩu tháp' 또는 'cần cẩu tháp' 사용",
                "explanation": "타워크레인은 탑 구조를 가진 특수 크레인으로, 일반 크레인과 구분 필요"
            },
            {
                "mistake": "'양정(揚程)'을 'chiều cao'(높이)로 번역",
                "correction": "'độ cao nâng' 또는 'chiều cao nâng hàng' 사용",
                "explanation": "양정은 화물을 들어 올릴 수 있는 최대 높이를 의미"
            },
            {
                "mistake": "'권과방지장치'를 번역 없이 생략",
                "correction": "'thiết bị chống quấn dây cáp' 또는 'bộ phận ngăn cáp vượt quá giới hạn' 사용",
                "explanation": "와이어로프가 권상 드럼에 과도하게 감기는 것을 방지하는 안전장치"
            }
        ],
        "examples": [
            {
                "ko": "타워크레인 10ton을 현장 중앙에 설치하고, 안전검사를 받으세요.",
                "vi": "Lắp cẩu tháp 10 tấn ở trung tâm công trường và tiến hành kiểm tra an toàn.",
                "situation": "onsite"
            },
            {
                "ko": "타워크레인 작업반경 내에는 출입을 금지하고 안전펜스를 설치합니다.",
                "vi": "Cấm ra vào trong bán kính làm việc của cẩu tháp và lắp hàng rào an toàn.",
                "situation": "formal"
            },
            {
                "ko": "태풍 예보가 있으니 타워크레인 붐을 자유회전으로 풀어두세요.",
                "vi": "Có dự báo bão nên để tay cẩu tháp ở chế độ xoay tự do.",
                "situation": "informal"
            }
        ],
        "relatedTerms": [
            "이동식크레인",
            "양중기",
            "신호수",
            "와이어로프",
            "과부하방지장치"
        ]
    },
    {
        "slug": "pa-lang",
        "korean": "호이스트",
        "vietnamese": "pa-lăng",
        "hanja": None,
        "hanjaReading": None,
        "pronunciation": "빠랑",
        "meaningKo": "전기·공압·수동 동력을 이용하여 화물을 수직으로 들어 올리는 양중장비로, 체인 또는 와이어로프로 화물을 인양합니다. 통역 시 '호이스트'는 'pa-lăng' 또는 'tời nâng'으로 표현하며, 동력 방식에 따라 '전기호이스트(pa-lăng điện)', '공압호이스트(pa-lăng khí nén)', '수동호이스트(pa-lăng tay)'로 구분합니다. 호이스트는 크레인의 권상장치로 사용되거나, 단독으로 빔(beam)이나 레일에 고정하여 사용합니다. 한국 산업안전보건법에 따라 호이스트는 정격하중 표시, 과부하방지장치, 비상정지장치, 권과방지장치를 의무 설치해야 하며, 사용 전 무부하·정격하중 시험을 실시합니다. 주요 사양은 정격하중(ton), 양정(m), 속도(m/min)로 표시되며, 예를 들어 '5ton × 10m × 8m/min'는 5톤을 10m 높이까지 분당 8m 속도로 인양 가능함을 의미합니다. 체인호이스트는 소형(0.5~5ton), 와이어호이스트는 대형(3~50ton)에 주로 사용됩니다.",
        "meaningVi": "Pa-lăng (tời nâng) là thiết bị nâng hạ dùng động lực điện, khí nén hoặc tay để nâng hàng theo phương đứng bằng xích hoặc cáp thép. Theo động lực: pa-lăng điện, pa-lăng khí nén, pa-lăng tay. Pa-lăng dùng làm bộ phận nâng của cẩu hoặc lắp độc lập trên dầm/ray. Thông số: tải trọng định mức (ton), độ cao nâng (m), tốc độ (m/phút). Pa-lăng xích dùng cho tải nhỏ (0.5~5 tấn), pa-lăng cáp cho tải lớn (3~50 tấn).",
        "context": "양중작업, 기계설비, 건설안전",
        "culturalNote": "한국은 호이스트를 리프팅 작업의 핵심 장비로 간주하며, 정기 점검(월 1회), 정밀 안전검사(2년마다), 작업 전 점검(일일)을 의무화합니다. 호이스트 조작은 자격(양중기운전기능사) 보유자만 가능하며, 작업 시 신호수와 협업하여 안전을 확보합니다. 호이스트 체인·와이어로프는 마모 상태를 육안 점검하고, 한계 마모(직경 7% 감소) 시 즉시 교체합니다. 후크(hook)는 변형·균열 검사를 실시하며, 안전걸쇠(safety latch)가 정상 작동하는지 확인합니다. 베트남은 호이스트 관리가 느슨하며, 체인·와이어로프가 심하게 부식·마모된 상태로 사용하거나, 정격하중을 초과하여 사용하는 경우가 많습니다. 과부하방지장치를 임의로 해제하거나, 비상정지장치가 고장 난 상태로 작업하는 위험한 관행이 있습니다. 한국 감리는 호이스트 안전검사증, 점검 기록, 와이어로프 교체 이력을 철저히 확인하지만, 베트남 현장은 서류만 구비하고 실제 장비는 불량인 경우가 많아 통역 시 현장 육안 점검을 병행할 것을 요구해야 합니다.",
        "commonMistakes": [
            {
                "mistake": "'호이스트'를 'máy nâng'(양중기)로 일반화",
                "correction": "'pa-lăng' 또는 'tời nâng' 사용",
                "explanation": "호이스트는 수직 인양 전용 장비로, 일반 양중기와 구분 필요"
            },
            {
                "mistake": "'체인호이스트'를 'pa-lăng dây xích'(체인 로프 호이스트)로 번역",
                "correction": "'pa-lăng xích' 사용",
                "explanation": "체인(xích)은 로프(dây)가 아닌 금속 고리 연결 구조"
            },
            {
                "mistake": "'과부하방지장치'를 'thiết bị chống quá tải'로만 번역하고 기능 설명 생략",
                "correction": "'thiết bị chống quá tải (tự động dừng khi vượt tải trọng định mức)' 병기",
                "explanation": "베트남 작업자는 과부하방지장치의 작동 원리를 잘 모름"
            }
        ],
        "examples": [
            {
                "ko": "5톤 전기호이스트를 빔에 설치하고, 정격하중 시험을 실시하세요.",
                "vi": "Lắp pa-lăng điện 5 tấn lên dầm và tiến hành thử tải trọng định mức.",
                "situation": "onsite"
            },
            {
                "ko": "호이스트 작업 전에 체인 마모 상태와 후크 안전걸쇠를 점검합니다.",
                "vi": "Trước khi dùng pa-lăng, kiểm tra mòn xích và chốt an toàn móc.",
                "situation": "formal"
            },
            {
                "ko": "호이스트가 과부하 경보를 울리면 즉시 작업을 중단하세요.",
                "vi": "Nếu pa-lăng báo quá tải thì dừng ngay.",
                "situation": "informal"
            }
        ],
        "relatedTerms": [
            "체인블록",
            "와이어로프",
            "크레인",
            "양중기",
            "권상장치"
        ]
    },
    {
        "slug": "thang-may-cong-trinh",
        "korean": "리프트카",
        "vietnamese": "thang máy công trình",
        "hanja": None,
        "hanjaReading": None,
        "pronunciation": "탕 마이 꽁 찡",
        "meaningKo": "건설 현장에서 인원과 자재를 수직으로 운반하는 임시 승강기로, 외부 가이드 레일(guide rail)을 따라 상하로 이동하는 간이 엘리베이터입니다. 통역 시 '리프트카'는 'thang máy công trình' 또는 'thang nâng hàng công trường'로 표현하며, 일반 승객용 엘리베이터(thang máy)와 구분해야 합니다. 리프트카는 용도에 따라 '인화물용(인원+자재)', '화물전용(자재만)'으로 나뉘며, 속도는 30~60m/min, 적재하중은 1~3ton이 일반적입니다. 한국 산업안전보건법에 따라 리프트카는 설치 후 1개월 이내 안전검사, 월례 자체점검, 작업 시작 전 점검이 의무입니다. 주요 안전장치는 과부하방지장치, 비상정지장치, 추락방지장치(안티폴백, anti-fall back), 층간 안전문입니다. 리프트카는 건물 외벽에 브래킷(bracket)과 앵커로 고정하며, 3개 층마다 또는 9m마다 타이백(tie-back) 고정이 필수입니다. 한국은 리프트카 추락 사고 방지를 위해 2중 브레이크, 낙하방지장치를 의무 설치하고 있습니다.",
        "meaningVi": "Thang máy công trình (thang nâng hàng công trường) là thang máy tạm thời vận chuyển người và vật liệu theo phương đứng tại công trường, di chuyển dọc theo ray dẫn hướng bên ngoài như thang máy đơn giản. Khác với thang máy hành khách (thang máy), thang máy công trình là thiết bị tạm. Theo mục đích: người+hàng, chỉ hàng. Tốc độ 30~60m/phút, tải trọng 1~3 tấn. Các thiết bị an toàn: chống quá tải, dừng khẩn cấp, chống rơi (anti-fall back), cửa an toàn tầng. Cố định bằng khung giá (bracket) và neo vào tường, mỗi 3 tầng hoặc 9m phải buộc chằng (tie-back).",
        "context": "고층건축, 가설공사, 건설안전",
        "culturalNote": "한국은 리프트카 안전관리를 매우 중시하며, 설치 시 구조계산서 제출, 가이드 레일 수직도 검사, 브래킷 용접 검사를 의무화합니다. 리프트카 운전원은 건설기계조종사(건설용 리프트) 자격을 보유해야 하며, 탑승 정원을 초과하거나 적재하중을 초과하면 즉시 작동을 중단합니다. 월례 점검은 와이어로프 마모, 브레이크 작동, 추락방지장치, 층간 안전문을 중점 확인하며, 점검 기록을 보관합니다. 태풍·강풍 시 리프트카 사용을 중단하고, 카(car)를 최하층에 내려놓습니다. 베트남은 리프트카 안전관리가 매우 취약하며, 구조계산 없이 임의 설치, 브래킷 용접 불량, 타이백 누락 등으로 리프트카 붕괴·추락 사고가 빈발합니다. 과부하 운전, 낙하방지장치 고장 상태 사용, 층간 안전문 미설치 등 안전 위반이 일상화되어 있습니다. 한국 감리는 리프트카 안전검사증, 구조계산서, 월례 점검 기록을 철저히 확인하고 현장 육안 검사를 병행하지만, 베트남 현장은 서류만 구비하고 실제 안전 상태는 불량인 경우가 많아 통역 시 실제 점검 실시와 시정 조치를 강력히 요구해야 합니다.",
        "commonMistakes": [
            {
                "mistake": "'리프트카'를 'thang máy'(엘리베이터)로만 번역",
                "correction": "'thang máy công trình' 또는 'thang nâng công trường' 사용",
                "explanation": "리프트카는 건설 현장 임시 승강기로, 일반 엘리베이터와 구분 필요"
            },
            {
                "mistake": "'추락방지장치'를 'thiết bị chống rơi'로만 번역하고 원리 설명 생략",
                "correction": "'thiết bị chống rơi (kẹp tự động khi cáp đứt)' 병기",
                "explanation": "추락방지장치는 와이어 로프 파단 시 가이드 레일을 물어 추락을 방지하는 안전장치"
            },
            {
                "mistake": "'타이백(tie-back)'을 'buộc chặt'(단단히 묶기)로 직역",
                "correction": "'buộc chằng vào tòa nhà' 또는 'neo chắc vào cấu kiện' 사용",
                "explanation": "타이백은 리프트카 가이드 레일을 건물 구조체에 고정하는 것"
            }
        ],
        "examples": [
            {
                "ko": "리프트카를 15층 높이까지 설치하고, 3개 층마다 타이백으로 고정하세요.",
                "vi": "Lắp thang máy công trình lên độ cao 15 tầng và cố định bằng buộc chằng mỗi 3 tầng.",
                "situation": "onsite"
            },
            {
                "ko": "리프트카 탑승 인원은 최대 10명이며, 적재하중 2톤을 초과해서는 안 됩니다.",
                "vi": "Số người lên thang máy công trình tối đa 10 người, không vượt quá tải trọng 2 tấn.",
                "situation": "formal"
            },
            {
                "ko": "리프트카 와이어로프가 마모됐으니 교체가 필요해요.",
                "vi": "Cáp thang máy công trình bị mòn nên cần thay.",
                "situation": "informal"
            }
        ],
        "relatedTerms": [
            "가설승강기",
            "가이드레일",
            "추락방지장치",
            "타이백",
            "브래킷"
        ]
    },
    {
        "slug": "ke-hoach-nang-hang",
        "korean": "양중계획서",
        "vietnamese": "kế hoạch nâng hàng",
        "hanja": "揚重計劃書",
        "hanjaReading": "양(오를 양) + 중(무거울 중) + 계(셀 계) + 획(그을 획) + 서(글 서)",
        "pronunciation": "께 호억 낭 항",
        "meaningKo": "건설 현장에서 중량물을 인양·운반하는 작업의 안전을 확보하기 위해 사전에 수립하는 계획서로, 양중장비 선정, 작업 절차, 안전대책을 포함합니다. 통역 시 '양중계획서'는 'kế hoạch nâng hàng' 또는 'phương án nâng hạ'로 표현하며, 한국 산업안전보건법에 따라 2톤 이상 중량물 인양 작업 시 의무 작성·제출해야 합니다. 양중계획서는 (1) 작업 개요(인양물 중량, 치수, 수량), (2) 양중장비 선정(크레인 용량, 작업반경), (3) 작업 순서(인양→이동→설치), (4) 안전대책(지반 보강, 신호수 배치, 출입 통제), (5) 비상 대응 절차로 구성됩니다. 양중계획서는 양중작업 3일 전까지 안전관리자·감리자 검토를 받아야 하며, 타워크레인·이동식 크레인 등 대형 장비 사용 시 구조계산서와 지반 지지력 검토서를 첨부해야 합니다. 한국은 양중계획서를 리프팅 작업의 '안전 설계도'로 간주하며, 계획서 없이 작업 시 작업 중지 조치를 받습니다. 양중계획서는 현장에 비치하여 작업자가 열람할 수 있도록 해야 합니다.",
        "meaningVi": "Kế hoạch nâng hàng (phương án nâng hạ) là kế hoạch lập trước để đảm bảo an toàn khi nâng và vận chuyển vật nặng tại công trường, bao gồm lựa chọn thiết bị nâng, quy trình làm việc, biện pháp an toàn. Theo luật an toàn Hàn Quốc, bắt buộc lập và nộp khi nâng vật nặng từ 2 tấn trở lên. Kế hoạch gồm: (1) tổng quan công việc, (2) chọn thiết bị nâng, (3) trình tự làm việc, (4) biện pháp an toàn, (5) xử lý khẩn cấp. Phải được người quản lý an toàn và giám sát duyệt trước 3 ngày. Khi dùng thiết bị lớn cần kèm tính toán kết cấu và kiểm tra sức chịu tải nền.",
        "context": "양중작업, 건설안전, 작업계획",
        "culturalNote": "한국은 양중계획서를 중대재해 예방의 핵심 수단으로 간주하며, 계획서 작성을 전문가(안전관리자, 건설기술인)에게 위임하거나 외부 컨설팅을 받는 경우도 많습니다. 양중계획서는 단순히 서류가 아니라 실제 작업의 '시나리오'로 활용되며, 작업 전 TBM(Tool Box Meeting)에서 전 작업자에게 공유합니다. 양중계획서에는 지반 조건, 기상 조건(풍속 제한), 장비 배치도, 인양 경로, 신호수 위치, 비상 연락망이 상세히 기재됩니다. 베트남은 양중계획서 작성 의무가 없거나 있어도 형식적으로만 작성하는 경우가 많습니다. 계획서 없이 즉흥적으로 작업하거나, 계획서와 실제 작업이 다른 경우가 빈번합니다. 한국 감리가 양중계획서를 요구하면 베트남 시공사는 '시간 낭비', '불필요한 서류'라고 반발하는 경우가 있어, 통역 시 양중계획서의 안전 효과(사고 예방, 책임 소재 명확화, 비상 대응 신속화)를 설명하여 필요성을 설득해야 합니다.",
        "commonMistakes": [
            {
                "mistake": "'양중계획서'를 'kế hoạch công việc'(작업 계획서)로 일반화",
                "correction": "'kế hoạch nâng hàng' 또는 'phương án nâng hạ vật nặng' 사용",
                "explanation": "양중계획서는 중량물 인양 전용 계획서로, 일반 작업 계획서와 구분 필요"
            },
            {
                "mistake": "'지반 지지력'을 'độ cứng nền'(지반 경도)로 번역",
                "correction": "'sức chịu tải của nền' 또는 'khả năng chịu lực của nền đất' 사용",
                "explanation": "지지력(bearing capacity)은 지반이 하중을 견딜 수 있는 능력"
            },
            {
                "mistake": "양중계획서 내용 요소를 나열하지 않고 '계획서'로만 번역",
                "correction": "작업 개요, 장비 선정, 작업 순서, 안전대책, 비상 대응을 명시",
                "explanation": "베트남 기술자는 양중계획서에 무엇을 포함해야 하는지 잘 모름"
            }
        ],
        "examples": [
            {
                "ko": "15톤 철골 인양 전에 양중계획서를 작성하여 감리에게 제출하세요.",
                "vi": "Trước khi nâng thép 15 tấn, lập kế hoạch nâng hàng và nộp cho giám sát.",
                "situation": "onsite"
            },
            {
                "ko": "양중계획서에는 크레인 용량, 작업반경, 지반 보강 방법을 명시해야 합니다.",
                "vi": "Trong kế hoạch nâng hàng phải ghi rõ dung lượng cẩu, bán kính làm việc, phương pháp gia cố nền.",
                "situation": "formal"
            },
            {
                "ko": "양중계획서 없이 작업하면 안전사고 책임이 커져요.",
                "vi": "Nếu làm việc không có kế hoạch nâng hàng thì trách nhiệm tai nạn sẽ lớn.",
                "situation": "informal"
            }
        ],
        "relatedTerms": [
            "작업계획서",
            "안전대책",
            "크레인",
            "신호수",
            "지반보강"
        ]
    },
    {
        "slug": "nguoi-chi-huy-nang-hang",
        "korean": "신호수",
        "vietnamese": "người chỉ huy nâng hàng",
        "hanja": "信號手",
        "hanjaReading": "신(믿을 신) + 호(부를 호) + 수(손 수)",
        "pronunciation": "응으이 찌 후이 낭 항",
        "meaningKo": "크레인·호이스트 등 양중장비 작업 시 운전원과 작업자 사이에서 수신호·깃발·무전기로 작업 지시를 전달하는 안전 담당자입니다. 통역 시 '신호수'는 'người chỉ huy nâng hàng' 또는 'người phát tín hiệu nâng hạ'로 표현하며, 한국 산업안전보건법에 따라 양중작업 시 신호수 배치가 의무입니다. 신호수는 (1) 인양물 중량·치수 확인, (2) 인양 경로 안전 확인, (3) 운전원에게 정확한 신호 전달, (4) 작업자 안전 감시, (5) 비상 시 작업 중지 권한을 가집니다. 신호수는 양중기 신호수 자격교육(4시간) 이수가 필수이며, 표준 수신호(올려, 내려, 좌우 이동, 정지, 비상정지)를 숙지해야 합니다. 한국은 신호수가 형광색 조끼, 안전모, 신호용 깃발을 착용·소지하며, 운전원 시야 내에서 신호를 보내야 합니다. 신호수는 양중작업의 '교통경찰' 역할을 하며, 신호수 없이 작업 시 즉시 중지됩니다.",
        "meaningVi": "Người chỉ huy nâng hàng (người phát tín hiệu nâng hạ) là người chịu trách nhiệm an toàn truyền đạt lệnh làm việc giữa người lái cẩu/tời và công nhân bằng tín hiệu tay, cờ, bộ đàm khi vận hành thiết bị nâng. Theo luật an toàn Hàn Quốc, bắt buộc bố trí người chỉ huy khi nâng hàng. Nhiệm vụ: (1) xác nhận trọng lượng và kích thước hàng, (2) kiểm tra an toàn đường nâng, (3) truyền tín hiệu chính xác cho lái xe, (4) giám sát an toàn công nhân, (5) quyền dừng khẩn cấp. Phải qua đào tạo 4 giờ và nắm vững tín hiệu chuẩn (nâng, hạ, trái phải, dừng, dừng khẩn cấp). Mặc áo phản quang, mũ an toàn, cầm cờ hiệu, phải ở trong tầm nhìn của lái xe.",
        "context": "양중작업, 건설안전, 작업 관리",
        "culturalNote": "한국은 신호수를 양중작업의 핵심 안전 인력으로 간주하며, 신호수 배치 없이 작업 시 안전관리자·감리자가 즉시 작업 중지를 명령합니다. 신호수는 표준 수신호를 사용하며, 현장마다 고유한 신호는 사전에 TBM에서 공유합니다. 소음이 심한 현장은 무전기를 사용하고, 시야가 확보되지 않는 경우 CCTV를 설치하여 신호수가 모니터로 작업을 감시합니다. 신호수는 인양물이 사람 위를 지나가지 않도록 경로를 통제하고, 바람이 강할 때는 작업을 중단할 권한을 가집니다. 베트남은 신호수 개념이 약하며, 신호수 없이 운전원과 작업자가 직접 소통하거나, 비전문가가 즉흥적으로 신호를 보내는 경우가 많습니다. 표준 수신호 교육이 없어 신호 오해로 인한 사고가 빈발하고, 신호수가 안전 장비(조끼, 깃발)를 착용하지 않아 운전원이 신호수를 식별하지 못하는 경우도 있습니다. 한국 감리는 신호수 자격증, 신호 숙지 여부를 확인하고 현장에서 신호 시연을 요구하지만, 베트남 현장은 형식적으로만 신호수를 배치하고 실제 작동하지 않는 경우가 많아 통역 시 신호수의 역할과 책임을 명확히 전달해야 합니다.",
        "commonMistakes": [
            {
                "mistake": "'신호수'를 'người phát tín hiệu'(신호 보내는 사람)로만 번역",
                "correction": "'người chỉ huy nâng hàng'(양중 작업 지휘자) 사용",
                "explanation": "신호수는 단순 신호 전달이 아닌 작업 전체를 감시·통제하는 안전 책임자"
            },
            {
                "mistake": "'수신호'를 'tín hiệu bằng tay'(손 신호)로만 번역하고 표준 신호 설명 생략",
                "correction": "올려(nâng lên), 내려(hạ xuống), 정지(dừng), 비상정지(dừng khẩn cấp) 등 구체적 신호 명시",
                "explanation": "베트남 작업자는 표준 수신호를 모르는 경우가 많음"
            },
            {
                "mistake": "신호수 배치 의무를 설명하지 않고 '신호수'로만 번역",
                "correction": "'bắt buộc bố trí người chỉ huy'(신호수 배치 의무) 강조",
                "explanation": "베트남 현장은 신호수 배치를 선택사항으로 인식하는 경우가 많음"
            }
        ],
        "examples": [
            {
                "ko": "크레인 작업 시 반드시 신호수를 배치하고, 표준 수신호를 사용하세요.",
                "vi": "Khi vận hành cẩu phải bố trí người chỉ huy nâng hàng và dùng tín hiệu tay chuẩn.",
                "situation": "onsite"
            },
            {
                "ko": "신호수는 인양물이 사람 위를 지나가지 않도록 경로를 통제해야 합니다.",
                "vi": "Người chỉ huy nâng hàng phải kiểm soát đường đi để hàng không đi qua đầu người.",
                "situation": "formal"
            },
            {
                "ko": "신호수가 없으면 크레인 작업을 못 해요.",
                "vi": "Không có người chỉ huy thì không được làm việc với cẩu.",
                "situation": "informal"
            }
        ],
        "relatedTerms": [
            "크레인",
            "호이스트",
            "양중작업",
            "수신호",
            "안전관리"
        ]
    },
    {
        "slug": "buoc-day-cap",
        "korean": "줄걸이",
        "vietnamese": "buộc dây cáp",
        "hanja": None,
        "hanjaReading": None,
        "pronunciation": "북 자이 깝",
        "meaningKo": "크레인이나 호이스트로 화물을 인양하기 위해 와이어로프·슬링(sling)·샤클 등을 사용하여 화물에 고정하는 작업 및 그 작업자를 지칭합니다. 통역 시 '줄걸이'는 'buộc dây cáp', 'công nhân buộc cáp', 또는 'người móc cáp'로 표현하며, 한국 산업안전보건법에 따라 줄걸이 작업자는 '줄걸이 작업 안전교육(4시간)' 이수가 의무입니다. 줄걸이 작업은 (1) 화물 무게중심 확인, (2) 적절한 슬링 선택, (3) 슬링 걸기 방법 결정(수직걸기, 바구니걸기, 초크걸기), (4) 샤클·후크 연결, (5) 하중 분산 확인 순서로 진행됩니다. 줄걸이는 양중작업의 '시작점'으로, 줄걸이가 잘못되면 화물 낙하, 슬링 파단, 화물 손상 등 중대 사고로 이어집니다. 슬링 걸기 각도(sling angle)는 60도 이상 유지해야 하며, 각도가 작아질수록 슬링에 걸리는 장력(tension)이 급증합니다. 한국은 줄걸이 작업 전 슬링·샤클 상태를 육안 점검하고, 화물 무게와 슬링 정격하중을 대조하여 안전율을 확인합니다.",
        "meaningVi": "Buộc dây cáp (móc cáp) là công việc và người công nhân cố định hàng hóa bằng cáp thép, dây cáp (sling), khóa nối (shackle) để nâng bằng cẩu hoặc tời. Theo luật an toàn Hàn Quốc, người buộc cáp phải qua đào tạo 4 giờ. Trình tự: (1) xác định trọng tâm hàng, (2) chọn dây cáp phù hợp, (3) quyết định cách buộc (thẳng đứng, giỏ, chữ V), (4) nối khóa và móc, (5) kiểm tra phân bổ tải. Buộc cáp là điểm bắt đầu của nâng hàng, nếu buộc sai sẽ gây rơi hàng, đứt dây, hỏng hàng. Góc dây cáp (sling angle) phải giữ từ 60 độ trở lên, góc nhỏ sẽ tăng lực căng dây.",
        "context": "양중작업, 건설안전, 기계작업",
        "culturalNote": "한국은 줄걸이 작업을 전문 기능으로 인정하며, 숙련된 줄걸이 작업자를 '줄걸이 기능공'으로 우대합니다. 줄걸이는 화물의 형태(긴 것, 무거운 것, 불균형한 것)에 따라 최적의 슬링 걸기 방법을 선택하며, 2점 걸기, 4점 걸기, 보조 슬링 사용 등 다양한 기법을 구사합니다. 줄걸이 작업 시 슬링이 화물 모서리에 닿아 손상되지 않도록 코너 보호대(corner protector)를 설치하고, 슬링이 꼬이지 않도록 주의합니다. 줄걸이 완료 후 신호수가 최종 확인하고, 운전원에게 '인양 가능' 신호를 보냅니다. 베트남은 줄걸이 작업을 단순 노무로 취급하며, 비숙련 작업자가 즉흥적으로 줄걸이를 하는 경우가 많습니다. 슬링 각도를 고려하지 않고, 슬링이 부식·마모된 상태로 사용하거나, 화물 무게중심을 확인하지 않아 인양 중 화물이 기울어지는 사고가 빈발합니다. 한국 감리는 줄걸이 작업 전 슬링 상태, 샤클 핀 고정, 슬링 각도를 육안 확인하지만, 베트남 현장은 확인 절차를 생략하는 경우가 많아 통역 시 줄걸이 검수 절차를 상세히 전달하고 준수를 요구해야 합니다.",
        "commonMistakes": [
            {
                "mistake": "'줄걸이'를 'buộc dây'(줄 묶기)로만 번역",
                "correction": "'buộc dây cáp nâng hàng' 또는 'móc cáp'(케이블 후킹) 사용",
                "explanation": "줄걸이는 단순 묶기가 아닌 화물을 안전하게 인양하기 위한 전문 작업"
            },
            {
                "mistake": "'슬링(sling)'을 'dây cáp'(와이어로프)로만 번역",
                "correction": "'dây cáp mềm' 또는 'dây cáp nâng hàng' 사용",
                "explanation": "슬링은 화물 인양 전용 유연한 와이어로프 또는 섬유 로프"
            },
            {
                "mistake": "'슬링 각도'를 'góc dây'로만 번역하고 중요성 설명 생략",
                "correction": "'góc dây cáp (ít nhất 60 độ, góc nhỏ tăng lực căng)' 병기",
                "explanation": "슬링 각도가 작아지면 장력이 급증하여 슬링 파단 위험이 커짐"
            }
        ],
        "examples": [
            {
                "ko": "철골 인양 전에 줄걸이가 4점 걸기로 정확하게 되었는지 확인하세요.",
                "vi": "Trước khi nâng thép kiểm tra xem đã buộc dây cáp 4 điểm chính xác chưa.",
                "situation": "onsite"
            },
            {
                "ko": "줄걸이 시 슬링 각도를 60도 이상 유지하여 장력을 분산해야 합니다.",
                "vi": "Khi buộc cáp phải giữ góc dây cáp từ 60 độ trở lên để phân tán lực căng.",
                "situation": "formal"
            },
            {
                "ko": "줄걸이가 잘못되면 화물이 떨어질 수 있으니 조심하세요.",
                "vi": "Nếu buộc cáp sai thì hàng có thể rơi nên cẩn thận.",
                "situation": "informal"
            }
        ],
        "relatedTerms": [
            "슬링",
            "샤클",
            "와이어로프",
            "크레인",
            "신호수"
        ]
    },
    {
        "slug": "khoa-noi-cap",
        "korean": "샤클",
        "vietnamese": "khóa nối cáp",
        "hanja": None,
        "hanjaReading": None,
        "pronunciation": "코아 노이 깝",
        "meaningKo": "와이어로프, 슬링, 체인 등을 연결하거나 화물에 고정하기 위해 사용하는 U자형 금속 연결 고리로, 핀(pin) 또는 볼트로 개폐가 가능한 양중 부속품입니다. 통역 시 '샤클'은 'khóa nối cáp', 'móc nối', 또는 'shackle'(베트남에서도 영어 그대로 사용)로 표현합니다. 샤클은 형태에 따라 'D형 샤클(bow shackle, 활 모양)', '직선형 샤클(dee shackle, D 모양)'로 나뉘며, 핀 고정 방식에 따라 '볼트형(볼트와 너트)', '스크류형(나사 핀)', '안전핀형(핀+고정 핀)'으로 구분됩니다. 샤클의 안전작업하중(SWL, Safe Working Load)은 샤클 몸체에 각인되어 있으며, 이 하중을 초과하여 사용하면 파손 위험이 있습니다. 한국 산업안전보건법에 따라 샤클은 사용 전 육안 점검(균열, 변형, 마모), 핀 고정 상태 확인이 의무입니다. 샤클은 경사 하중(side load)을 받지 않도록 설치해야 하며, 하중 방향은 샤클 개구부(opening)와 일치해야 합니다.",
        "meaningVi": "Khóa nối cáp (móc nối, shackle) là vòng kim loại hình chữ U dùng nối cáp thép, dây cáp, xích hoặc cố định vào hàng, mở đóng bằng chốt (pin) hoặc bu-lông, là phụ kiện nâng hàng. Theo hình dạng: shackle hình cung (bow shackle), shackle chữ D (dee shackle). Theo cách cố định chốt: loại bu-lông (bu-lông + đai ốc), loại vít (chốt ren), loại chốt an toàn (chốt + chốt cố định). Tải trọng làm việc an toàn (SWL, Safe Working Load) được khắc trên thân shackle, vượt quá sẽ nguy cơ vỡ. Trước khi dùng phải kiểm tra mắt thường (nứt, biến dạng, mòn), kiểm tra chốt cố định. Shackle không được chịu lực xiên (side load), hướng lực phải trùng với miệng shackle.",
        "context": "양중작업, 줄걸이, 건설안전",
        "culturalNote": "한국은 샤클을 정밀 안전 부품으로 취급하며, 정품(KS 인증, CE 인증) 사용을 원칙으로 합니다. 샤클은 6개월마다 정밀 검사를 실시하고, 균열·변형이 발견되면 즉시 폐기합니다. 샤클 핀은 완전히 조여져야 하며, 핀이 느슨하면 작업 중 빠질 위험이 있어 안전핀 또는 와이어로 고정합니다. 샤클은 다방향 하중을 받지 않도록 설계되었으므로, 여러 방향에서 힘이 가해지면 파손될 수 있습니다. 한국 현장은 샤클 SWL을 준수하고, 여유율(안전계수)을 고려하여 정격하중의 70~80%만 사용합니다. 베트남은 샤클 관리가 느슨하며, 저가 모조품을 사용하거나 SWL 표시가 없는 샤클을 사용하는 경우가 많습니다. 샤클 핀이 부식되어 조이지 않거나, 핀을 분실하여 철사로 대체하는 등 위험한 관행이 있습니다. 샤클 파손으로 인한 화물 낙하 사고가 빈발하며, 한국 감리는 샤클 상태를 육안 검사하고 SWL을 확인하지만, 베트남 현장은 샤클을 소모품으로 취급하여 관리하지 않는 경우가 많아 통역 시 샤클의 중요성과 검수 방법을 강조해야 합니다.",
        "commonMistakes": [
            {
                "mistake": "'샤클'을 'móc'(후크)로 번역",
                "correction": "'khóa nối cáp' 또는 'shackle' 사용",
                "explanation": "샤클은 연결 고리이고, 후크(móc)는 걸쇠 형태로 다른 부품"
            },
            {
                "mistake": "'SWL(Safe Working Load)'을 번역 없이 영문 약어만 사용",
                "correction": "'tải trọng làm việc an toàn' 또는 'tải trọng an toàn' 병기",
                "explanation": "베트남 작업자는 SWL 약어에 익숙하지 않음"
            },
            {
                "mistake": "'경사 하중(side load)'을 'tải nghiêng'(기울어진 하중)으로 번역",
                "correction": "'tải trọng xiên' 또는 'lực tác động nghiêng' 사용",
                "explanation": "경사 하중은 샤클 개구부와 다른 방향에서 가해지는 하중"
            }
        ],
        "examples": [
            {
                "ko": "샤클 SWL 5톤을 사용하여 3톤 화물을 인양하세요.",
                "vi": "Dùng khóa nối cáp SWL 5 tấn để nâng hàng 3 tấn.",
                "situation": "onsite"
            },
            {
                "ko": "샤클 핀이 완전히 조여졌는지 확인하고, 안전핀으로 고정합니다.",
                "vi": "Kiểm tra chốt shackle đã vặn chặt chưa và cố định bằng chốt an toàn.",
                "situation": "formal"
            },
            {
                "ko": "샤클이 변형됐으니 새 것으로 교체하세요.",
                "vi": "Shackle bị biến dạng nên thay cái mới.",
                "situation": "informal"
            }
        ],
        "relatedTerms": [
            "슬링",
            "와이어로프",
            "후크",
            "줄걸이",
            "정격하중"
        ]
    },
    {
        "slug": "cap-thep",
        "korean": "와이어로프",
        "vietnamese": "cáp thép",
        "hanja": None,
        "hanjaReading": None,
        "pronunciation": "깝 텝",
        "meaningKo": "여러 가닥의 강선(steel wire)을 꼬아 만든 로프로, 크레인·호이스트·엘리베이터 등 양중장비의 인양·견인에 사용되는 고강도 케이블입니다. 통역 시 '와이어로프'는 'cáp thép' 또는 'dây cáp thép'로 표현하며, 섬유 로프(dây thừng sợi)와 명확히 구분해야 합니다. 와이어로프는 구조에 따라 '꼬임 방향(오른 꼬임, 왼 꼬임)', '심재(fiber core, steel core)', '가닥 수(6×19, 6×37 등)'로 분류됩니다. 예를 들어 '6×37 FC IWRC'는 6가닥×37개 강선, 섬유 심재(Fiber Core), 독립 와이어 로프 심재(Independent Wire Rope Core)를 의미합니다. 한국 산업안전보건법에 따라 와이어로프는 월례 점검(마모, 부식, 소선 절단, 킹크, 변형) 의무이며, 폐기 기준은 (1) 직경 7% 감소, (2) 한 꼬임 길이 내 소선 절단 10% 이상, (3) 킹크·변형·심한 부식 발생 시입니다. 와이어로프 교체 시 크레인 용량, 사용 조건(굽힘, 마모, 충격)을 고려하여 적합한 로프를 선정해야 합니다.",
        "meaningVi": "Cáp thép (dây cáp thép) là dây thừng làm bằng nhiều sợi thép xoắn lại, dùng nâng hạ và kéo cho thiết bị nâng như cẩu, tời, thang máy, là cáp cường độ cao. Khác với dây thừng sợi (fiber rope), cáp thép chịu lực lớn. Cấu trúc: hướng xoắn (phải, trái), lõi (sợi, thép), số sợi (6×19, 6×37). Ví dụ '6×37 FC IWRC' nghĩa là 6 bó×37 sợi thép, lõi sợi (Fiber Core), lõi cáp thép độc lập (Independent Wire Rope Core). Kiểm tra hàng tháng (mòn, gỉ, đứt sợi, xoắn, biến dạng), tiêu chuẩn loại bỏ: (1) đường kính giảm 7%, (2) trong một đoạn xoắn có từ 10% sợi đứt trở lên, (3) xoắn, biến dạng, gỉ nặng. Khi thay cáp phải chọn phù hợp với dung lượng cẩu, điều kiện sử dụng (uốn, mòn, va đập).",
        "context": "양중작업, 크레인, 건설안전",
        "culturalNote": "한국은 와이어로프를 양중작업의 생명선으로 간주하며, 로프 관리를 매우 엄격하게 시행합니다. 와이어로프는 사용 전 점검(육안, 소선 절단 확인)과 사용 중 점검(월 1회)을 의무 실시하며, 점검 기록을 보관합니다. 와이어로프는 윤활유(그리스)를 도포하여 부식·마모를 방지하고, 권상 드럼에 감길 때 겹치지 않도록 정렬합니다. 폐기된 와이어로프는 절단하여 재사용을 방지하고, 새 로프 설치 시 제조사 인증서, 시험성적서를 확인합니다. 한국 현장은 와이어로프 직경, 꼬임 방향, 파단하중을 정확히 기록하고, 교체 주기를 준수합니다. 베트남은 와이어로프 관리가 매우 취약하며, 소선이 다수 절단되거나 심하게 부식된 상태로 사용하는 경우가 많습니다. 킹크(꼬임)가 발생한 로프를 펴서 재사용하거나, 로프 직경이 한계 이하로 감소해도 교체하지 않는 위험한 관행이 있습니다. 와이어로프 파단으로 인한 화물 낙하, 인명 사고가 빈발하며, 한국 감리는 와이어로프 상태를 육안 검사하고 직경을 측정하여 폐기 기준을 확인하지만, 베트남 현장은 로프를 소모품으로 취급하여 한계까지 사용하는 경우가 많아 통역 시 와이어로프 폐기 기준과 안전 중요성을 강력히 전달해야 합니다.",
        "commonMistakes": [
            {
                "mistake": "'와이어로프'를 'dây thép'(철선)으로만 번역",
                "correction": "'cáp thép' 또는 'dây cáp thép' 사용",
                "explanation": "와이어로프는 여러 강선을 꼬아 만든 로프로, 단순 철선과 다름"
            },
            {
                "mistake": "'소선 절단'을 'đứt dây'(줄 끊김)로만 번역하고 기준 설명 생략",
                "correction": "'đứt sợi thép trong cáp (10% trong một đoạn xoắn → loại bỏ)' 병기",
                "explanation": "소선 절단 개수가 폐기 기준이므로 기준을 명확히 해야 함"
            },
            {
                "mistake": "'킹크(kink)'를 'gấp khúc'(구부러짐)로 번역",
                "correction": "'xoắn lại' 또는 'vặn lại bất thường' 사용",
                "explanation": "킹크는 로프가 과도하게 꼬여 영구 변형된 상태"
            }
        ],
        "examples": [
            {
                "ko": "크레인 와이어로프를 점검하여 소선 절단이 10개 이상이면 교체하세요.",
                "vi": "Kiểm tra cáp thép cẩu, nếu có từ 10 sợi đứt trở lên thì thay.",
                "situation": "onsite"
            },
            {
                "ko": "와이어로프 직경이 7% 감소하면 폐기 기준에 도달한 것입니다.",
                "vi": "Nếu đường kính cáp thép giảm 7% thì đã đạt tiêu chuẩn loại bỏ.",
                "situation": "formal"
            },
            {
                "ko": "와이어로프가 킹크됐으니 새 것으로 교체해야 해요.",
                "vi": "Cáp thép bị xoắn lại nên phải thay mới.",
                "situation": "informal"
            }
        ],
        "relatedTerms": [
            "크레인",
            "호이스트",
            "슬링",
            "샤클",
            "소선"
        ]
    },
    {
        "slug": "pa-lang-xich",
        "korean": "체인블록",
        "vietnamese": "pa-lăng xích",
        "hanja": None,
        "hanjaReading": None,
        "pronunciation": "빠랑 씩",
        "meaningKo": "수동으로 체인을 당겨 화물을 들어 올리는 소형 호이스트로, 전기나 공압 동력 없이 사람의 힘만으로 작동하는 간이 양중장비입니다. 통역 시 '체인블록'은 'pa-lăng xích' 또는 'tời xích tay'로 표현하며, 전기호이스트와 명확히 구분해야 합니다. 체인블록은 '손잡이 체인(load chain)'을 당기면 내부 기어가 회전하여 '인양 체인(hoist chain)'이 감기며 화물을 들어 올리는 원리입니다. 정격하중은 0.5~10ton이 일반적이며, 소형(0.5~2ton)은 건설 현장, 정비소, 창고에서 널리 사용됩니다. 체인블록은 (1) 브레이크 기능(화물을 원하는 높이에 고정), (2) 과부하 방지 장치(정격하중 초과 시 작동 불가), (3) 역회전 방지 장치를 기본 장착합니다. 한국 산업안전보건법에 따라 체인블록은 사용 전 점검(체인 마모, 후크 변형, 브레이크 작동), 월례 점검이 의무이며, 체인이 꼬이거나 녹슬면 즉시 교체해야 합니다. 체인블록은 수직 인양만 가능하며, 사선 방향으로 당기면 체인이 손상되거나 화물이 흔들려 위험합니다.",
        "meaningVi": "Pa-lăng xích (tời xích tay) là tời nhỏ nâng hàng bằng cách kéo xích tay, không cần điện hay khí nén, chỉ dùng sức người, là thiết bị nâng đơn giản. Khác với pa-lăng điện, pa-lăng xích hoạt động thủ công. Kéo xích tay (load chain) làm bánh răng trong quay, xích nâng (hoist chain) cuốn lại và nâng hàng. Tải trọng định mức 0.5~10 tấn, loại nhỏ (0.5~2 tấn) dùng nhiều ở công trường, xưởng sửa chữa, kho. Tính năng: (1) phanh (giữ hàng ở độ cao mong muốn), (2) chống quá tải (không hoạt động khi vượt tải), (3) chống xoay ngược. Kiểm tra trước khi dùng (mòn xích, biến dạng móc, phanh), kiểm tra hàng tháng, nếu xích bị xoắn hoặc gỉ phải thay ngay. Pa-lăng xích chỉ nâng thẳng đứng, nếu kéo xiên xích sẽ hỏng hoặc hàng lung lay nguy hiểm.",
        "context": "양중작업, 기계정비, 소형 인양",
        "culturalNote": "한국은 체인블록을 소형 양중작업의 표준 도구로 간주하며, 건설 현장, 기계 설치, 유지보수 현장에서 필수 장비로 사용합니다. 체인블록은 전기 없이 작동하므로 정전 시에도 사용 가능하고, 이동이 간편하여 좁은 공간에서 유용합니다. 체인블록 사용 시 작업자는 손잡이 체인을 수직으로 당기며, 화물을 천천히 들어 올립니다. 브레이크는 자동으로 작동하여 손을 놓아도 화물이 떨어지지 않지만, 브레이크 고장 시 화물 낙하 위험이 있어 사용 전 브레이크 시험을 의무 실시합니다. 한국 현장은 체인블록 정격하중을 준수하고, 여유율을 두어 정격의 70% 이하로 사용합니다. 베트남은 체인블록 관리가 느슨하며, 체인이 녹슬거나 마모된 상태로 사용하는 경우가 많습니다. 브레이크가 고장 났거나 과부하 방지 장치가 작동하지 않는 상태로 사용하여 화물 낙하 사고가 빈발합니다. 체인블록을 사선 방향으로 사용하거나, 여러 개의 체인블록을 동시에 사용하여 불균형 인양을 하는 위험한 관행이 있습니다. 한국 감리는 체인블록 상태를 육안 검사하고 브레이크 작동 시험을 요구하지만, 베트남 현장은 체인블록을 소모품으로 취급하여 관리하지 않는 경우가 많아 통역 시 체인블록의 안전 중요성과 점검 방법을 강조해야 합니다.",
        "commonMistakes": [
            {
                "mistake": "'체인블록'을 'pa-lăng'(호이스트 일반)로만 번역",
                "correction": "'pa-lăng xích' 또는 'tời xích tay' 사용",
                "explanation": "체인블록은 수동 체인 호이스트로, 전기호이스트와 구분 필요"
            },
            {
                "mistake": "'손잡이 체인'과 '인양 체인'을 구분하지 않고 'xích'(체인)로만 번역",
                "correction": "'xích tay'(손잡이 체인), 'xích nâng'(인양 체인)으로 구분",
                "explanation": "손잡이 체인은 사람이 당기는 체인, 인양 체인은 화물을 매다는 체인"
            },
            {
                "mistake": "체인블록 브레이크 기능을 설명 없이 생략",
                "correction": "'có phanh tự động giữ hàng'(자동 브레이크로 화물 고정) 강조",
                "explanation": "브레이크는 체인블록의 핵심 안전 기능으로, 작동 원리를 명확히 해야 함"
            }
        ],
        "examples": [
            {
                "ko": "체인블록 2톤을 사용하여 엔진을 들어 올리고, 브레이크가 작동하는지 확인하세요.",
                "vi": "Dùng pa-lăng xích 2 tấn nâng động cơ và kiểm tra phanh có hoạt động không.",
                "situation": "onsite"
            },
            {
                "ko": "체인블록은 수직으로만 인양하고, 사선 방향으로 당기지 마세요.",
                "vi": "Pa-lăng xích chỉ nâng thẳng đứng, không kéo xiên.",
                "situation": "formal"
            },
            {
                "ko": "체인블록 체인이 녹슬었으니 교체해야 해요.",
                "vi": "Xích pa-lăng bị gỉ nên phải thay.",
                "situation": "informal"
            }
        ],
        "relatedTerms": [
            "호이스트",
            "체인",
            "수동호이스트",
            "양중기",
            "브레이크"
        ]
    },
    {
        "slug": "pa-lang-tay",
        "korean": "수동호이스트",
        "vietnamese": "pa-lăng tay",
        "hanja": "手動호이스트",
        "hanjaReading": "수(손 수) + 동(움직일 동)",
        "pronunciation": "빠랑 타이",
        "meaningKo": "전기나 공압 동력 없이 사람의 힘으로 레버나 체인을 조작하여 화물을 들어 올리는 양중장비의 총칭으로, 체인블록, 레버블록(lever hoist), 수동 윈치 등이 포함됩니다. 통역 시 '수동호이스트'는 'pa-lăng tay' 또는 'tời nâng thủ công'으로 표현하며, 전기호이스트·공압호이스트와 명확히 구분해야 합니다. 수동호이스트는 (1) 전기 없이 작동 가능, (2) 이동 간편, (3) 소형·경량, (4) 유지보수 단순의 장점이 있어 건설 현장, 농어촌, 정비소에서 널리 사용됩니다. 수동호이스트는 정격하중이 작아(0.25~10ton) 소형 인양 작업에 적합하며, 대형 인양은 전기호이스트나 크레인을 사용해야 합니다. 한국 산업안전보건법에 따라 수동호이스트도 양중기로 분류되어 사용 전 점검, 월례 점검이 의무이며, 체인·와이어로프 마모, 후크 변형, 브레이크 작동을 확인해야 합니다. 수동호이스트는 작업 속도가 느리고 작업자 체력 소모가 크므로, 반복 작업이나 대량 인양 시 전기호이스트로 대체하는 것이 권장됩니다.",
        "meaningVi": "Pa-lăng tay (tời nâng thủ công) là tổng hợp thiết bị nâng hạ dùng sức người thao tác đòn bẩy hoặc xích không cần điện hay khí nén, bao gồm pa-lăng xích, pa-lăng đòn (lever hoist), tời tay. Khác với pa-lăng điện, pa-lăng khí nén, pa-lăng tay không cần động lực. Ưu điểm: (1) hoạt động không cần điện, (2) di chuyển dễ, (3) nhỏ nhẹ, (4) bảo trì đơn giản, dùng nhiều ở công trường, nông thôn, xưởng sửa chữa. Tải trọng định mức nhỏ (0.25~10 tấn), phù hợp nâng vật nhỏ, nâng lớn dùng pa-lăng điện hoặc cẩu. Cũng là thiết bị nâng nên phải kiểm tra trước khi dùng, kiểm tra hàng tháng (mòn xích/cáp, biến dạng móc, phanh). Pa-lăng tay tốc độ chậm, tốn sức, nên nhiều lần hoặc nâng khối lượng lớn nên thay pa-lăng điện.",
        "context": "양중작업, 소형 인양, 건설안전",
        "culturalNote": "한국은 수동호이스트를 보조 양중장비로 활용하며, 전기 공급이 어려운 곳(야외, 산간, 선박)에서 필수 장비로 간주합니다. 수동호이스트는 정전 시 비상 양중장비로도 사용되며, 안전 비축 장비로 현장에 상시 보관합니다. 수동호이스트 사용 시 작업자는 무리한 힘을 가하지 않도록 주의하며, 2명 이상 협력하여 작업합니다. 수동호이스트는 브레이크가 자동으로 작동하여 화물을 원하는 높이에 고정할 수 있지만, 브레이크 고장 시 화물 낙하 위험이 있어 사용 전 브레이크 시험을 의무 실시합니다. 베트남은 수동호이스트를 주 양중장비로 사용하는 경우가 많으며, 전기 공급 불안정, 전기료 절감을 이유로 전기호이스트 대신 수동호이스트를 선호합니다. 수동호이스트를 정격하중 이상으로 무리하게 사용하거나, 여러 명이 동시에 체인을 당겨 과부하를 가하는 위험한 관행이 있습니다. 수동호이스트 체인·와이어가 심하게 마모되거나 부식된 상태로 사용하여 파단 사고가 빈발합니다. 한국 감리는 수동호이스트도 전기호이스트와 동일한 기준으로 점검을 요구하지만, 베트남 현장은 수동호이스트를 단순 공구로 취급하여 관리하지 않는 경우가 많아 통역 시 수동호이스트도 양중기로서 안전 점검이 필수임을 강조해야 합니다.",
        "commonMistakes": [
            {
                "mistake": "'수동호이스트'를 'pa-lăng'(호이스트)로만 번역하고 '수동' 강조 누락",
                "correction": "'pa-lăng tay' 또는 'pa-lăng thủ công' 사용",
                "explanation": "수동호이스트는 동력 방식이 핵심이므로 '수동(tay, thủ công)' 명시 필요"
            },
            {
                "mistake": "수동호이스트와 전기호이스트의 차이를 설명하지 않고 번역",
                "correction": "동력원(전기 vs 사람), 정격하중, 작업 속도, 사용 환경 차이 명시",
                "explanation": "베트남 작업자는 수동호이스트의 한계를 잘 모르고 무리하게 사용"
            },
            {
                "mistake": "'레버블록(lever hoist)'을 번역 없이 생략",
                "correction": "'pa-lăng đòn' 또는 'tời đòn bẩy' 병기",
                "explanation": "레버블록은 레버를 반복 조작하여 인양하는 수동호이스트의 한 종류"
            }
        ],
        "examples": [
            {
                "ko": "전기가 없는 곳이니 수동호이스트 1톤을 사용하여 자재를 인양하세요.",
                "vi": "Chỗ này không có điện nên dùng pa-lăng tay 1 tấn để nâng vật liệu.",
                "situation": "onsite"
            },
            {
                "ko": "수동호이스트는 작업 속도가 느리므로 대량 인양 시 전기호이스트를 사용합니다.",
                "vi": "Pa-lăng tay tốc độ chậm nên nâng khối lượng lớn dùng pa-lăng điện.",
                "situation": "formal"
            },
            {
                "ko": "수동호이스트도 정기 점검이 필요해요.",
                "vi": "Pa-lăng tay cũng cần kiểm tra định kỳ.",
                "situation": "informal"
            }
        ],
        "relatedTerms": [
            "체인블록",
            "레버블록",
            "전기호이스트",
            "양중기",
            "수동윈치"
        ]
    }
]

# 저장 경로
output_path = os.path.join(
    os.path.dirname(os.path.abspath(__file__)),
    "..",
    "data",
    "terms",
    "construction.json"
)

print(f"저장 경로: {output_path}")
print(f"추가할 용어 개수: {len(data)}개")
print("\n추가할 용어 목록:")
for i, term in enumerate(data, 1):
    print(f"{i}. {term['korean']} ({term['vietnamese']})")

# 실행 금지 - 스크립트만 생성
print("\n⚠️  이 스크립트는 실행하지 마세요. Write만 하고 종료합니다.")

# === Merge Logic ===
import json as _json
with open(output_path, 'r', encoding='utf-8') as _f:
    _existing = _json.load(_f)
_existing_slugs = {t['slug'] for t in _existing}
_filtered = [t for t in data if t['slug'] not in _existing_slugs]
_existing.extend(_filtered)
with open(output_path, 'w', encoding='utf-8') as _f:
    _json.dump(_existing, _f, ensure_ascii=False, indent=2)
print(f"Added {len(_filtered)} terms. Total: {len(_existing)}")
