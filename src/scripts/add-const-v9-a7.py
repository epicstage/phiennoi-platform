#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
건설 용어 추가 스크립트 - 현장조직/직책 테마
현장소장, 공사부장, 공무과장, 안전과장, 품질관리자, 환경관리자, 감리원, 감독관, 시공기술자, 건설사업관리자
"""

import json
import os

# 현장조직/직책 테마 용어 10개 (Tier S 기준)
data = [
    {
        "slug": "chi-huy-truong-cong-truong",
        "korean": "현장소장",
        "vietnamese": "chỉ huy trưởng công trường",
        "hanja": "現場所長",
        "hanjaReading": "현(나타날 현) + 장(마당 장) + 소(바 소) + 장(어른 장)",
        "pronunciation": "찌 후이 쯩 꽁 쯩",
        "meaningKo": "건설 현장의 최고 책임자로, 공사 전반의 시공·안전·품질·공정·인력·예산을 총괄 관리하는 직책입니다. 통역 시 '현장소장'은 'chỉ huy trưởng công trường' 또는 'giám đốc công trường'로 표현하며, 프로젝트 매니저(PM)와 구분해야 합니다. PM은 설계·계약·예산 등 프로젝트 전체를 관리하고, 현장소장은 시공 현장만을 책임집니다. 현장소장은 건설업법상 '건설기술인(기술사, 기사 등)' 자격을 보유해야 하며, 일정 규모 이상 공사는 전임 배치가 의무입니다. 현장소장의 주요 업무는: (1) 공정관리(일정 준수), (2) 품질관리(시공 품질 확보), (3) 안전관리(재해 예방), (4) 인력관리(협력업체 조율), (5) 대외협력(발주자·감리·인허가 기관 소통)입니다. 현장소장은 작업중지권을 가지며, 중대재해 발생 시 형사책임을 질 수 있습니다. 한국 건설업법 제28조에 따라 현장소장은 '건설공사의 기술관리'를 담당하며, 부실시공 방지 의무가 있습니다.",
        "meaningVi": "Chỉ huy trưởng công trường (giám đốc công trường) là người chịu trách nhiệm cao nhất tại công trường xây dựng, quản lý toàn diện thi công, an toàn, chất lượng, tiến độ, nhân lực, ngân sách. Khác với PM (quản lý toàn dự án), chỉ huy trưởng chỉ quản lý công trường. Phải có bằng kỹ thuật viên xây dựng, công trường lớn phải bố trí toàn thời gian. Có quyền dừng thi công, chịu trách nhiệm hình sự khi xảy ra tai nạn nghiêm trọng.",
        "context": "건설현장, 조직관리, 시공관리",
        "culturalNote": "한국 현장소장은 강력한 권한과 막중한 책임을 동시에 갖습니다. 작업중지권을 행사하여 위험 작업을 즉시 중단시킬 수 있으며, 중대재해처벌법에 따라 안전 의무를 위반하면 형사처벌(징역, 벌금)을 받습니다. 현장소장은 매일 아침 조회에서 작업 지시와 안전 교육을 실시하고, 매주 공정회의를 주재하며, 발주자·감리와 협의하여 현장 문제를 해결합니다. 한국 건설업계는 현장소장을 '현장의 왕'으로 부를 만큼 권한이 크지만, 책임도 그만큼 무겁습니다. 베트남은 'chỉ huy trưởng' 또는 'giám đốc công trường'이 한국 현장소장과 유사하지만, 권한과 책임이 한국보다 약합니다. 베트남 현장소장은 주로 공정과 인력 관리를 하고, 안전·품질은 별도 부서가 담당하는 경우가 많습니다. 한국식 '전권형 현장소장' 개념이 낯설어, 통역 시 현장소장의 권한(작업중지권, 인력 배치권)과 책임(안전·품질 책임)을 명확히 전달해야 합니다.",
        "commonMistakes": [
            {
                "mistake": "'현장소장'을 'quản lý công trường'(현장관리자)로 번역",
                "correction": "'chỉ huy trưởng công trường' 또는 'giám đốc công trường' 사용",
                "explanation": "'quản lý'는 일반 관리자, 'chỉ huy trưởng'은 최고 책임자를 의미"
            },
            {
                "mistake": "PM(Project Manager)과 현장소장을 구분 없이 번역",
                "correction": "PM은 'quản lý dự án', 현장소장은 'chỉ huy trưởng công trường'으로 명확히 구분",
                "explanation": "PM은 프로젝트 전체 관리, 현장소장은 시공 현장만 책임"
            },
            {
                "mistake": "'작업중지권'을 'quyền dừng việc'(일 중지권)으로 직역",
                "correction": "'quyền dừng thi công khi có nguy hiểm' 사용",
                "explanation": "작업중지권은 안전 위험 시 시공을 즉시 중단할 수 있는 법적 권한"
            }
        ],
        "examples": [
            {
                "ko": "현장소장은 매일 아침 조회에서 안전 수칙을 강조하고 작업 지시를 내립니다.",
                "vi": "Chỉ huy trưởng công trường nhấn mạnh quy định an toàn và chỉ thị công việc tại buổi điểm danh sáng hàng ngày.",
                "situation": "formal"
            },
            {
                "ko": "위험한 작업이 있으면 현장소장에게 즉시 보고하세요.",
                "vi": "Nếu có công việc nguy hiểm, hãy báo cáo ngay cho chỉ huy trưởng công trường.",
                "situation": "onsite"
            },
            {
                "ko": "현장소장님, 이번 주 공정이 지연되고 있는데 대책이 필요합니다.",
                "vi": "Chỉ huy trưởng, tiến độ tuần này bị chậm, cần có biện pháp.",
                "situation": "informal"
            }
        ],
        "relatedTerms": [
            "공사부장",
            "공무과장",
            "안전관리자",
            "감리원",
            "프로젝트매니저"
        ]
    },
    {
        "slug": "truong-phong-thi-cong",
        "korean": "공사부장",
        "vietnamese": "trưởng phòng thi công",
        "hanja": "工事部長",
        "hanjaReading": "공(장인 공) + 사(일 사) + 부(나눌 부) + 장(어른 장)",
        "pronunciation": "쯩 퐁 티 꽁",
        "meaningKo": "건설 현장에서 시공 업무를 총괄하는 중간관리자로, 현장소장을 보좌하며 각 공종(토목, 건축, 설비 등)의 시공을 조율하고 관리하는 직책입니다. 통역 시 '공사부장'은 'trưởng phòng thi công' 또는 'phó chỉ huy trưởng thi công'으로 표현하며, '공무과장'과 구분해야 합니다. 공사부장은 시공(thi công)을, 공무과장은 행정·자재(hành chính, vật tư)를 담당합니다. 공사부장의 주요 업무는: (1) 공정 계획 수립 및 관리, (2) 공종별 작업 조율(토목→건축→설비 순서), (3) 협력업체(하도급) 관리 및 작업 지시, (4) 시공 품질 검수, (5) 현장소장 보고 및 회의 참석입니다. 공사부장은 현장에서 가장 바쁜 직책으로, 매일 작업 계획을 세우고, 인력·장비를 배치하며, 돌발 상황(날씨, 자재 부족, 장비 고장)에 대응합니다. 한국 중대형 현장은 여러 명의 공사부장(토목 공사부장, 건축 공사부장, 기계설비 공사부장 등)을 두어 분야별로 관리합니다.",
        "meaningVi": "Trưởng phòng thi công (phó chỉ huy trưởng thi công) là quản lý trung gian phụ trách toàn bộ công tác thi công tại công trường, hỗ trợ chỉ huy trưởng và điều phối các công trình (thổ công, kiến trúc, hệ thống). Khác với trưởng phòng công vụ (phụ trách hành chính, vật tư), trưởng phòng thi công tập trung vào thi công hiện trường. Nhiệm vụ chính: lập kế hoạch tiến độ, điều phối công trình, quản lý nhà thầu phụ, kiểm tra chất lượng.",
        "context": "건설현장, 조직관리, 시공관리",
        "culturalNote": "한국 공사부장은 '현장의 실무 책임자'로, 새벽부터 저녁까지 현장을 누비며 작업을 지휘합니다. 아침 조회 후 각 공종별 팀장에게 작업 지시를 내리고, 작업 중 발생하는 문제(자재 부족, 장비 고장, 인력 부족)를 즉시 해결합니다. 한국 건설업계는 공사부장을 '현장의 허리'로 부르며, 공사부장이 우수하면 공사가 원활하게 진행됩니다. 공사부장은 보통 10~20년 경력의 베테랑 기술자이며, 건설기사 또는 산업기사 자격을 보유합니다. 베트남은 'trưởng phòng thi công' 또는 'phó giám đốc thi công'이 유사하지만, 한국보다 권한이 약하고 현장소장의 지시를 받는 비중이 큽니다. 베트남 공사부장은 주로 공정 진도 확인과 보고 업무를 하고, 실제 작업 지시는 각 공종 팀장(đội trưởng)이 하는 경우가 많습니다. 통역 시 한국 공사부장의 역할(작업 조율, 인력 배치, 품질 검수)을 구체적으로 설명해야 합니다.",
        "commonMistakes": [
            {
                "mistake": "'공사부장'을 'giám đốc công trình'(공사 감독)으로 번역",
                "correction": "'trưởng phòng thi công' 또는 'phó chỉ huy trưởng thi công' 사용",
                "explanation": "'giám đốc'은 감독(감리)과 혼동될 수 있음"
            },
            {
                "mistake": "'공사부장'과 '공무과장'을 구분 없이 번역",
                "correction": "공사부장='thi công'(시공), 공무과장='hành chính'(행정)로 명확히 구분",
                "explanation": "공사부장은 시공 관리, 공무과장은 행정·자재 관리"
            },
            {
                "mistake": "'협력업체'를 'công ty hợp tác'(협력회사)로 직역",
                "correction": "'nhà thầu phụ' 또는 'đơn vị thi công phụ' 사용",
                "explanation": "협력업체는 하도급업체(subcontractor)를 의미"
            }
        ],
        "examples": [
            {
                "ko": "공사부장은 매일 공정회의에서 작업 진도를 보고하고 다음 주 계획을 조율합니다.",
                "vi": "Trưởng phòng thi công báo cáo tiến độ tại cuộc họp tiến độ hàng ngày và điều phối kế hoạch tuần sau.",
                "situation": "formal"
            },
            {
                "ko": "공사부장님, 오늘 콘크리트 타설이 늦어지고 있는데 장비를 추가 투입해야 할까요?",
                "vi": "Trưởng phòng, đổ bê tông hôm nay bị chậm, có cần thêm thiết bị không ạ?",
                "situation": "informal"
            },
            {
                "ko": "공사부장은 토목 팀장과 건축 팀장에게 작업 순서를 조율하도록 지시했습니다.",
                "vi": "Trưởng phòng thi công chỉ thị đội trưởng thổ công và đội trưởng kiến trúc điều phối thứ tự công việc.",
                "situation": "onsite"
            }
        ],
        "relatedTerms": [
            "현장소장",
            "공무과장",
            "팀장",
            "협력업체",
            "공정관리"
        ]
    },
    {
        "slug": "truong-phong-cong-vu",
        "korean": "공무과장",
        "vietnamese": "trưởng phòng công vụ",
        "hanja": "工務課長",
        "hanjaReading": "공(장인 공) + 무(일 무) + 과(과녁 과) + 장(어른 장)",
        "pronunciation": "쯩 퐁 꽁 부",
        "meaningKo": "건설 현장에서 행정·자재·문서·계약 업무를 총괄하는 중간관리자로, 현장소장을 보좌하며 공사의 뒷받침(후방 지원) 업무를 담당하는 직책입니다. 통역 시 '공무과장'은 'trưởng phòng công vụ' 또는 'trưởng phòng hành chính'으로 표현하며, '공사부장'과 구분해야 합니다. 공무과장은 행정·자재를, 공사부장은 시공 현장을 담당합니다. 공무과장의 주요 업무는: (1) 자재 발주 및 입고 관리, (2) 장비 임대 및 유지관리, (3) 근로자 근태 및 급여 관리, (4) 인허가 및 민원 처리, (5) 도면·시방서·계약서 관리입니다. 공무과장은 현장소장과 공사부장이 시공에만 집중할 수 있도록 행정·자재·문서 업무를 처리하며, 발주자·감리와의 문서 소통(공문, 보고서, 검수 요청)도 담당합니다. 한국 건설현장은 공무과 인원이 많아(자재팀, 행정팀, 안전팀, 환경팀), 공무과장은 이들을 총괄 관리합니다.",
        "meaningVi": "Trưởng phòng công vụ (trưởng phòng hành chính) là quản lý trung gian phụ trách toàn bộ công tác hành chính, vật tư, tài liệu, hợp đồng tại công trường, hỗ trợ chỉ huy trưởng và đảm bảo hậu cần. Khác với trưởng phòng thi công (phụ trách hiện trường), trưởng phòng công vụ tập trung vào hành chính, vật tư. Nhiệm vụ chính: đặt hàng vật tư, thuê thiết bị, quản lý nhân sự, xử lý giấy phép, quản lý hồ sơ.",
        "context": "건설현장, 조직관리, 행정관리",
        "culturalNote": "한국 공무과장은 '현장의 뒷문 책임자'로, 시공에 필요한 모든 자원(자재, 장비, 인력)을 적시에 공급하여 공사가 중단되지 않도록 합니다. 공무과장은 매일 자재 입고 현황을 확인하고, 부족 자재를 긴급 발주하며, 장비 고장 시 즉시 수리·대체를 조치합니다. 한국 건설업계는 공무과장을 '현장의 물주'로 부르며, 공무과장이 유능하면 현장이 원활하게 돌아갑니다. 공무과장은 보통 경영학, 경제학, 토목공학 전공자이며, 자재·계약·인사 실무 경험이 풍부합니다. 베트남은 'trưởng phòng công vụ' 또는 'trưởng phòng hành chính' 개념이 있지만, 한국만큼 체계적이지 않고 각 업무(자재, 행정, 인사)를 별도 담당자가 처리하는 경우가 많습니다. 베트남 공무과장은 주로 문서 작성과 보고 업무를 하고, 자재 발주는 자재팀장(trưởng bộ phận vật tư), 인사는 인사팀장(trưởng bộ phận nhân sự)이 따로 하는 경우가 흔합니다. 통역 시 한국 공무과장의 역할(자재·장비·인사·인허가 총괄)을 구체적으로 설명해야 합니다.",
        "commonMistakes": [
            {
                "mistake": "'공무과장'을 'trưởng phòng công chính'(공정과장)으로 오역",
                "correction": "'trưởng phòng công vụ' 또는 'trưởng phòng hành chính' 사용",
                "explanation": "'công chính'은 공정(fairness), 'công vụ'는 업무(administration)"
            },
            {
                "mistake": "'공무과장'과 '공사부장'을 혼동하여 번역",
                "correction": "공무과장='hành chính, vật tư', 공사부장='thi công hiện trường'으로 명확히 구분",
                "explanation": "공무과장은 후방 지원, 공사부장은 현장 시공"
            },
            {
                "mistake": "'자재 발주'를 'đặt hàng nguyên liệu'(원료 주문)로 번역",
                "correction": "'đặt hàng vật tư' 또는 'đặt mua vật liệu xây dựng' 사용",
                "explanation": "'nguyên liệu'는 제조업 원료, 'vật tư'는 건설 자재"
            }
        ],
        "examples": [
            {
                "ko": "공무과장은 이번 주 자재 입고 계획을 보고하고, 부족한 자재를 긴급 발주했습니다.",
                "vi": "Trưởng phòng công vụ báo cáo kế hoạch nhập vật tư tuần này và đặt hàng khẩn vật tư thiếu.",
                "situation": "formal"
            },
            {
                "ko": "공무과장님, 크레인 임대 계약이 만료되는데 연장해야 할까요?",
                "vi": "Trưởng phòng, hợp đồng thuê cần cẩu sắp hết hạn, có cần gia hạn không ạ?",
                "situation": "informal"
            },
            {
                "ko": "공무과장은 발주자에게 제출할 준공 서류를 준비하고 있습니다.",
                "vi": "Trưởng phòng công vụ đang chuẩn bị hồ sơ nghiệm thu để nộp cho chủ đầu tư.",
                "situation": "onsite"
            }
        ],
        "relatedTerms": [
            "현장소장",
            "공사부장",
            "자재관리",
            "인허가",
            "행정업무"
        ]
    },
    {
        "slug": "truong-phong-an-toan",
        "korean": "안전과장",
        "vietnamese": "trưởng phòng an toàn",
        "hanja": "安全課長",
        "hanjaReading": "안(편안할 안) + 전(온전할 전) + 과(과녁 과) + 장(어른 장)",
        "pronunciation": "쯩 퐁 안 토안",
        "meaningKo": "건설 현장에서 안전 업무를 총괄하는 중간관리자로, 현장소장을 보좌하며 재해 예방, 안전 교육, 안전 점검을 담당하는 직책입니다. 통역 시 '안전과장'은 'trưởng phòng an toàn' 또는 'chuyên viên an toàn lao động'으로 표현하며, '안전관리자(giám sát an toàn)'와 구분해야 합니다. 안전관리자는 법적 선임 의무가 있는 자격자(산업안전기사 등)이고, 안전과장은 안전팀을 이끄는 관리자입니다. 안전과장의 주요 업무는: (1) 안전 교육 실시(신규 근로자, 일일 안전 조회), (2) 위험성 평가 및 안전 점검(추락, 붕괴, 전기 감전), (3) 보호구 지급 및 착용 관리(안전모, 안전대, 안전화), (4) 사고 발생 시 초동 조치 및 보고, (5) 안전보건관리비 집행 관리입니다. 안전과장은 작업중지권을 가지며, 위험한 작업을 발견하면 즉시 중단시킬 수 있습니다. 한국은 「중대재해처벌법」 시행 이후 안전과장의 권한과 책임이 크게 강화되었으며, 안전 의무 위반 시 현장소장과 함께 처벌될 수 있습니다.",
        "meaningVi": "Trưởng phòng an toàn (chuyên viên an toàn lao động) là quản lý trung gian phụ trách toàn bộ công tác an toàn tại công trường, hỗ trợ chỉ huy trưởng, phòng ngừa tai nạn, giáo dục an toàn, kiểm tra an toàn. Khác với giám sát an toàn (người có chứng chỉ an toàn lao động), trưởng phòng an toàn là người quản lý đội an toàn. Có quyền dừng thi công khi có nguy hiểm. Sau khi có Luật trừng phạt tai nạn nghiêm trọng, quyền và trách nhiệm được tăng cường.",
        "context": "건설현장, 안전관리, 조직관리",
        "culturalNote": "한국 안전과장은 '현장의 안전 지킴이'로, 매일 아침 조회에서 안전 교육을 실시하고, 현장을 순찰하며 위험 요소를 찾아냅니다. 안전과장은 추락 방지 안전난간, 낙하물 방지망, 전기 감전 방지 접지, 화재 예방 소화기 등을 점검하고, 미비 사항을 즉시 시정 조치합니다. 한국 건설업계는 안전과장을 '현장의 경찰'로 부르며, 안전과장의 지시를 무시하면 작업이 중단됩니다. 안전과장은 보통 산업안전기사 또는 건설안전기사 자격을 보유하며, 10년 이상 현장 경험이 있습니다. 베트남은 'trưởng phòng an toàn' 또는 'chuyên viên an toàn lao động' 개념이 있지만, 한국만큼 권한이 크지 않고 안전 점검보다 서류 작성에 치중하는 경우가 많습니다. 베트남 안전과장은 주로 안전 교육 기록, 사고 보고서 작성을 하고, 실제 안전 점검은 각 팀장이 자율적으로 하는 경우가 흔합니다. 한국 감리는 안전과장의 점검 기록(체크리스트, 사진)을 세밀히 확인하지만, 베트남 현장은 형식적 기록만 남기는 경우가 많아 통역 시 안전과장의 역할(위험 발견, 시정 조치, 작업중지)을 강조해야 합니다.",
        "commonMistakes": [
            {
                "mistake": "'안전과장'을 'giám sát an toàn'(안전 감독)으로 번역",
                "correction": "'trưởng phòng an toàn' 또는 'chuyên viên an toàn lao động' 사용",
                "explanation": "'giám sát'은 감독(감리)과 혼동될 수 있음"
            },
            {
                "mistake": "'안전관리자'와 '안전과장'을 구분 없이 번역",
                "correction": "안전관리자='có chứng chỉ an toàn'(자격자), 안전과장='quản lý đội an toàn'(팀 관리자)로 구분",
                "explanation": "안전관리자는 법적 자격자, 안전과장은 조직 관리자"
            },
            {
                "mistake": "'보호구'를 'thiết bị bảo vệ'(보호 장비)로 직역",
                "correction": "'đồ bảo hộ lao động' 사용",
                "explanation": "베트남에서는 '보호구=đồ bảo hộ'가 표준 용어"
            }
        ],
        "examples": [
            {
                "ko": "안전과장은 매일 아침 조회에서 추락 방지 안전대 착용을 강조합니다.",
                "vi": "Trưởng phòng an toàn nhấn mạnh đeo dây an toàn chống rơi tại buổi điểm danh sáng hàng ngày.",
                "situation": "onsite"
            },
            {
                "ko": "안전과장님, 3층 작업장에 안전난간이 없는데 즉시 설치해야 합니다.",
                "vi": "Trưởng phòng an toàn, khu làm việc tầng 3 không có lan can an toàn, cần lắp ngay.",
                "situation": "informal"
            },
            {
                "ko": "안전과장은 위험한 작업을 발견하고 작업중지 명령을 내렸습니다.",
                "vi": "Trưởng phòng an toàn phát hiện công việc nguy hiểm và ra lệnh dừng thi công.",
                "situation": "formal"
            }
        ],
        "relatedTerms": [
            "안전관리자",
            "안전교육",
            "보호구",
            "작업중지권",
            "중대재해처벌법"
        ]
    },
    {
        "slug": "nhan-vien-kiem-soat-chat-luong",
        "korean": "품질관리자",
        "vietnamese": "nhân viên kiểm soát chất lượng",
        "hanja": "品質管理者",
        "hanjaReading": "품(물건 품) + 질(바탕 질) + 관(관청 관) + 리(다스릴 리) + 자(사람 자)",
        "pronunciation": "년 비엔 끼엠 소앗 짯 르엉",
        "meaningKo": "건설 현장에서 시공 품질을 검사·관리하는 전문 인력으로, 설계도서와 시방서에 따라 시공이 올바르게 이루어지는지 확인하고 불량을 시정하는 직책입니다. 통역 시 '품질관리자'는 'nhân viên kiểm soát chất lượng' 또는 'quản lý chất lượng'으로 표현하며, '감리원(giám lý)'과 구분해야 합니다. 감리원은 발주자 측 제3자 검수 기관이고, 품질관리자는 시공사 내부의 자체 검수 인력입니다. 품질관리자의 주요 업무는: (1) 자재 품질 검사(콘크리트 강도, 철근 규격, 시멘트 성분), (2) 시공 품질 검사(두께, 치수, 정렬, 마감), (3) 시험·측정(슬럼프 시험, 압축강도 시험, 누수 시험), (4) 불량 발견 시 시정 조치 요구, (5) 품질 기록 작성 및 보고입니다. 품질관리자는 건설기술인(기사, 산업기사) 또는 품질관리 자격(품질경영기사)을 보유해야 하며, 일정 규모 이상 공사는 전임 배치가 의무입니다. 한국 건설업법 제29조에 따라 품질관리자는 '품질시험 및 검사' 업무를 수행하며, 부실시공 방지 의무가 있습니다.",
        "meaningVi": "Nhân viên kiểm soát chất lượng (quản lý chất lượng) là chuyên gia kiểm tra, quản lý chất lượng thi công tại công trường, xác nhận thi công tuân theo bản vẽ và tiêu chuẩn kỹ thuật, sửa chữa lỗi. Khác với giám lý (đại diện chủ đầu tư, bên thứ ba), nhân viên kiểm soát chất lượng là nhân viên nội bộ nhà thầu. Nhiệm vụ chính: kiểm tra chất lượng vật tư, kiểm tra chất lượng thi công, thí nghiệm đo đạc, yêu cầu sửa chữa lỗi, lập hồ sơ chất lượng.",
        "context": "건설현장, 품질관리, 시공관리",
        "culturalNote": "한국 품질관리자는 '현장의 품질 파수꾼'으로, 매일 시공 중인 구간을 점검하고 불량을 찾아냅니다. 품질관리자는 콘크리트 타설 전 슬럼프 시험(slump test)을 실시하고, 타설 후 공시체를 채취하여 압축강도 시험을 의뢰하며, 철근 배근 상태를 줄자로 측정하고 사진을 촬영하여 기록으로 남깁니다. 한국 건설업계는 품질관리자를 '현장의 검사관'으로 부르며, 품질관리자가 승인하지 않으면 다음 공정으로 진행할 수 없습니다. 품질관리자는 보통 건설재료시험기사, 콘크리트기사, 토목기사 자격을 보유하며, 시험 장비(슬럼프콘, 슈미트해머, 줄자, 수평계)를 항상 휴대합니다. 베트남은 'nhân viên kiểm soát chất lượng' 또는 'kỹ sư chất lượng' 개념이 있지만, 한국만큼 엄격하지 않고 시험 장비가 부족하여 육안 검사에 의존하는 경우가 많습니다. 베트남 품질관리자는 주로 감리원의 지적 사항을 기록하고 시정 조치를 확인하는 업무를 하며, 자체적으로 시험·측정을 하는 경우는 드뭅니다. 한국 감리는 품질관리자의 시험 기록(시험성적서, 사진)을 세밀히 확인하지만, 베트남 현장은 시험 없이 형식적 기록만 남기는 경우가 많아 통역 시 품질관리자의 역할(시험·측정, 불량 발견, 시정 조치)을 구체적으로 설명해야 합니다.",
        "commonMistakes": [
            {
                "mistake": "'품질관리자'를 'người quản lý chất lượng'로 직역",
                "correction": "'nhân viên kiểm soát chất lượng' 또는 'kỹ sư chất lượng' 사용",
                "explanation": "'kiểm soát'(검사)이 품질관리자의 핵심 업무를 더 명확히 표현"
            },
            {
                "mistake": "'품질관리자'와 '감리원'을 구분 없이 번역",
                "correction": "품질관리자='nhân viên nội bộ nhà thầu'(시공사 내부), 감리원='giám lý, bên thứ ba'(제3자)로 구분",
                "explanation": "품질관리자는 시공사 직원, 감리원은 발주자 측 감독"
            },
            {
                "mistake": "'슬럼프 시험'을 'thí nghiệm độ lún'(침하 시험)으로 오역",
                "correction": "'thí nghiệm độ sụt' 또는 'slump test' 사용",
                "explanation": "슬럼프 시험은 콘크리트 유동성 측정(slump), 침하는 지반 가라앉음(settlement)"
            }
        ],
        "examples": [
            {
                "ko": "품질관리자는 콘크리트 타설 전 슬럼프 시험을 실시하여 유동성을 확인했습니다.",
                "vi": "Nhân viên kiểm soát chất lượng thực hiện thí nghiệm độ sụt trước đổ bê tông để xác nhận độ lưu động.",
                "situation": "formal"
            },
            {
                "ko": "품질관리자님, 이 철근 간격이 도면과 다른데 확인해주세요.",
                "vi": "Kỹ sư chất lượng, khoảng cách thép này khác với bản vẽ, vui lòng kiểm tra.",
                "situation": "informal"
            },
            {
                "ko": "품질관리자는 불량 부위를 발견하고 재시공을 요구했습니다.",
                "vi": "Nhân viên kiểm soát chất lượng phát hiện lỗi và yêu cầu thi công lại.",
                "situation": "onsite"
            }
        ],
        "relatedTerms": [
            "감리원",
            "시험",
            "검사",
            "슬럼프시험",
            "압축강도"
        ]
    },
    {
        "slug": "nhan-vien-quan-ly-moi-truong",
        "korean": "환경관리자",
        "vietnamese": "nhân viên quản lý môi trường",
        "hanja": "環境管理者",
        "hanjaReading": "환(고리 환) + 경(지경 경) + 관(관청 관) + 리(다스릴 리) + 자(사람 자)",
        "pronunciation": "년 비엔 꽌 리 모이 쯩",
        "meaningKo": "건설 현장에서 환경 오염 방지와 환경 법규 준수를 관리하는 전문 인력으로, 소음·진동·분진·폐기물·수질 오염을 예방하고 민원을 관리하는 직책입니다. 통역 시 '환경관리자'는 'nhân viên quản lý môi trường' 또는 'chuyên viên môi trường'으로 표현하며, '안전관리자'와 구분해야 합니다. 안전관리자는 근로자 안전을, 환경관리자는 주변 환경 보호를 담당합니다. 환경관리자의 주요 업무는: (1) 소음·진동 측정 및 저감 대책(방음벽, 작업 시간 제한), (2) 분진 발생 억제(살수, 방진망), (3) 폐기물 분리·보관·처리(건설폐기물, 위험물), (4) 수질 오염 방지(침전조, 오탁 방지막), (5) 민원 대응 및 관계 기관 협의입니다. 환경관리자는 환경 관련 자격(대기환경기사, 수질환경기사, 폐기물처리기사)을 보유하거나, 환경공학 전공자로 일정 경력을 갖춰야 합니다. 한국은 「환경영향평가법」, 「소음·진동관리법」, 「대기환경보전법」 등 환경 법규가 엄격하며, 환경관리자는 이를 준수하여 과태료와 민원을 예방합니다.",
        "meaningVi": "Nhân viên quản lý môi trường (chuyên viên môi trường) là chuyên gia quản lý phòng ngừa ô nhiễm môi trường và tuân thủ pháp luật môi trường tại công trường, phòng ngừa tiếng ồn, rung động, bụi, chất thải, ô nhiễm nước, quản lý khiếu nại. Khác với nhân viên an toàn (bảo vệ công nhân), nhân viên môi trường bảo vệ môi trường xung quanh. Nhiệm vụ chính: đo tiếng ồn, rung động, giảm bụi, phân loại chất thải, phòng ngừa ô nhiễm nước, xử lý khiếu nại.",
        "context": "건설현장, 환경관리, 법규준수",
        "culturalNote": "한국 환경관리자는 '현장의 환경 지킴이'로, 매일 소음·분진 측정을 하고, 기준치를 초과하면 즉시 저감 조치(방음벽 설치, 살수 차량 투입)를 합니다. 환경관리자는 주변 주민의 민원(소음, 먼지, 악취)에 대응하고, 환경청·지자체의 점검에 협조하며, 환경 법규 위반 시 과태료(수백만~수천만 원)가 부과되므로 예방 활동을 철저히 합니다. 한국 건설업계는 환경관리자를 '현장의 민원 담당'으로 부르며, 환경관리자가 우수하면 민원이 줄어들고 공사가 원활하게 진행됩니다. 환경관리자는 보통 환경공학 전공자이며, 소음계, 분진측정기, pH 측정기 등 측정 장비를 사용합니다. 베트남은 'nhân viên quản lý môi trường' 개념이 있지만, 한국만큼 엄격하지 않고 환경 법규 집행이 느슨하여 형식적 관리에 그치는 경우가 많습니다. 베트남 환경관리자는 주로 환경 보고서 작성과 서류 제출 업무를 하고, 실제 측정과 저감 대책은 소홀한 경우가 흔합니다. 한국 감리는 환경관리자의 측정 기록(소음·분진 측정표, 사진)을 세밀히 확인하지만, 베트남 현장은 측정 없이 형식적 기록만 남기는 경우가 많아 통역 시 환경관리자의 역할(측정, 저감 대책, 민원 대응)을 구체적으로 설명해야 합니다.",
        "commonMistakes": [
            {
                "mistake": "'환경관리자'를 'người quản lý môi trường'로 직역",
                "correction": "'nhân viên quản lý môi trường' 또는 'chuyên viên môi trường' 사용",
                "explanation": "'nhân viên'(직원) 또는 'chuyên viên'(전문가)이 직책을 명확히 표현"
            },
            {
                "mistake": "'분진'을 'bụi'(먼지)로만 번역",
                "correction": "'bụi xây dựng' 또는 'bụi công trường' 사용",
                "explanation": "건설 현장 분진은 일반 먼지보다 입자가 크고 건강 위해가 큼"
            },
            {
                "mistake": "'민원'을 'khiếu nại'(불만)로만 번역",
                "correction": "'khiếu nại của dân cư xung quanh' 사용",
                "explanation": "민원은 주변 주민의 불만·요구를 의미"
            }
        ],
        "examples": [
            {
                "ko": "환경관리자는 매일 오전 소음을 측정하고, 기준치를 초과하면 방음벽을 추가 설치합니다.",
                "vi": "Nhân viên quản lý môi trường đo tiếng ồn mỗi sáng và lắp thêm tường chắn âm nếu vượt mức.",
                "situation": "formal"
            },
            {
                "ko": "환경관리자님, 주변 주민이 분진 민원을 제기했는데 살수 차량을 투입해야 할까요?",
                "vi": "Chuyên viên môi trường, dân cư xung quanh khiếu nại bụi, có cần xe phun nước không ạ?",
                "situation": "informal"
            },
            {
                "ko": "환경관리자는 폐기물을 종류별로 분리하여 보관하고 처리 업체에 인계했습니다.",
                "vi": "Nhân viên quản lý môi trường phân loại chất thải theo loại, bảo quản và chuyển giao cho đơn vị xử lý.",
                "situation": "onsite"
            }
        ],
        "relatedTerms": [
            "소음진동",
            "분진",
            "폐기물",
            "민원",
            "환경영향평가"
        ]
    },
    {
        "slug": "giam-ly",
        "korean": "감리원",
        "vietnamese": "giám lý",
        "hanja": "監理員",
        "hanjaReading": "감(볼 감) + 리(다스릴 리) + 원(인원 원)",
        "pronunciation": "잠 리",
        "meaningKo": "발주자를 대신하여 건설 공사의 시공 과정을 감독하고 품질을 검사하는 제3자 전문 기술자입니다. 통역 시 '감리원'은 'giám lý' 또는 'kỹ sư giám sát'으로 표현하며, 시공사의 '품질관리자'와 명확히 구분해야 합니다. 감리원은 발주자 측 독립 기관(감리회사) 소속이고, 품질관리자는 시공사 내부 직원입니다. 감리원의 주요 업무는: (1) 설계도서 및 시방서 준수 여부 확인, (2) 시공 품질 검사 및 승인(콘크리트 타설, 철근 배근, 마감), (3) 공정 관리 및 지연 원인 파악, (4) 설계 변경 검토 및 승인, (5) 준공 검사 및 하자 확인입니다. 감리원은 부실시공을 발견하면 시정 지시를 내리며, 시공사가 따르지 않으면 공사를 중지시킬 수 있는 강력한 권한을 가집니다. 한국 건설산업기본법 제2조에 따라 감리는 '건설공사가 관계 법령 등에 따라 적법하고 적정하게 시행될 수 있도록 관리하는 것'으로 정의됩니다. 감리원은 건설기술인(건축사, 기술사, 특급기술자, 고급기술자) 자격을 보유해야 하며, 일정 규모 이상 공사는 상주 감리가 의무입니다.",
        "meaningVi": "Giám lý (kỹ sư giám sát) là kỹ thuật viên chuyên nghiệp bên thứ ba đại diện chủ đầu tư giám sát quá trình thi công và kiểm tra chất lượng công trình xây dựng. Khác với nhân viên kiểm soát chất lượng (nhân viên nội bộ nhà thầu), giám lý là nhân viên công ty giám sát độc lập, đại diện chủ đầu tư. Nhiệm vụ chính: xác nhận tuân thủ bản vẽ, kiểm tra và phê duyệt chất lượng thi công, quản lý tiến độ, xem xét thay đổi thiết kế, nghiệm thu và xác nhận hư hỏng. Có quyền dừng công trình nếu phát hiện thi công kém chất lượng.",
        "context": "건설현장, 감리, 품질관리",
        "culturalNote": "한국 감리원은 '발주자의 눈'으로, 시공 과정을 세밀히 감독하고 불량을 찾아냅니다. 감리원은 매일 현장을 순찰하고, 주요 공정(철근 배근, 콘크리트 타설, 방수, 마감)에는 반드시 입회하여 검사합니다. 감리원이 승인하지 않으면 다음 공정으로 진행할 수 없으며, 시공사는 감리원의 지적 사항을 반드시 시정해야 합니다. 한국 건설업계는 감리원을 '현장의 심판'으로 부르며, 감리원과 시공사의 관계는 긴장감이 있습니다. 감리원은 보통 20년 이상 경력의 건축사, 기술사, 특급기술자이며, 발주자에게 감리보고서를 제출하여 공사 진행 상황을 보고합니다. 베트남은 'giám lý' 또는 'tư vấn giám sát' 개념이 있지만, 한국만큼 권한이 강하지 않고 시공사와 협의·조정하는 역할에 가깝습니다. 베트남 감리원은 주로 서류 검토와 보고서 작성을 하고, 실제 시공 현장 검사는 소홀한 경우가 많습니다. 한국 감리원은 시정 지시(RFI, Request for Information)를 문서로 발행하고 시공사의 시정 조치를 확인하지만, 베트남 감리원은 구두 지적만 하는 경우가 흔합니다. 통역 시 한국 감리원의 권한(공사 중지, 재시공 요구)과 책임(부실시공 방치 시 연대 책임)을 명확히 전달해야 합니다.",
        "commonMistakes": [
            {
                "mistake": "'감리원'을 'người giám sát'(감독자)로 번역",
                "correction": "'giám lý' 또는 'kỹ sư giám sát' 사용",
                "explanation": "'giám lý'가 베트남에서 건설 감리를 지칭하는 표준 용어"
            },
            {
                "mistake": "'감리원'과 '감독관'을 구분 없이 번역",
                "correction": "감리원='giám lý, bên thứ ba'(독립 기관), 감독관='giám đốc, chủ đầu tư'(발주자 직원)로 구분",
                "explanation": "감리원은 감리회사 소속, 감독관은 발주자 소속"
            },
            {
                "mistake": "'시정 지시'를 'chỉ thị sửa chữa'(수리 지시)로 직역",
                "correction": "'yêu cầu khắc phục' 또는 'chỉ thị điều chỉnh' 사용",
                "explanation": "시정 지시는 불량·오류를 바로잡는 공식 요구"
            }
        ],
        "examples": [
            {
                "ko": "감리원은 철근 배근 상태를 확인하고 콘크리트 타설을 승인했습니다.",
                "vi": "Giám lý xác nhận tình trạng bố trí thép và phê duyệt đổ bê tông.",
                "situation": "formal"
            },
            {
                "ko": "감리원님, 이 벽체 두께가 도면과 다른데 확인해주세요.",
                "vi": "Giám lý, độ dày tường này khác với bản vẽ, vui lòng kiểm tra.",
                "situation": "informal"
            },
            {
                "ko": "감리원은 방수층 시공이 불량하다고 판단하여 재시공을 지시했습니다.",
                "vi": "Giám lý đánh giá lớp chống thấm thi công kém chất lượng và chỉ thị thi công lại.",
                "situation": "onsite"
            }
        ],
        "relatedTerms": [
            "감독관",
            "품질관리자",
            "시정지시",
            "검사",
            "승인"
        ]
    },
    {
        "slug": "giam-doc-cong-trinh",
        "korean": "감독관",
        "vietnamese": "giám đốc công trình",
        "hanja": "監督官",
        "hanjaReading": "감(볼 감) + 독(살필 독) + 관(벼슬 관)",
        "pronunciation": "잠 독 꽁 찡",
        "meaningKo": "발주자(건축주, 국가기관, 공공기관) 소속으로 건설 공사를 직접 관리·감독하는 공무원 또는 직원입니다. 통역 시 '감독관'은 'giám đốc công trình' 또는 'cán bộ giám sát'으로 표현하며, '감리원'과 명확히 구분해야 합니다. 감독관은 발주자 소속 직원이고, 감리원은 독립 감리회사 소속 기술자입니다. 감독관의 주요 업무는: (1) 발주자를 대표하여 시공사·감리사 관리, (2) 공사비 집행 및 기성 검사, (3) 설계 변경 검토 및 승인, (4) 공사 계약 이행 감독(일정, 품질, 안전), (5) 준공 검사 및 하자 보증 관리입니다. 감독관은 공사 계약의 발주자 대리인으로, 시공사에 공사비를 지급하고, 설계 변경을 승인하며, 공사 지연·부실 시 계약 위반 조치(벌칙금, 계약 해지)를 취할 수 있는 강력한 권한을 가집니다. 한국 국가계약법에 따라 공공 공사는 발주 기관의 공무원이 감독관으로 지정되며, 민간 공사는 건축주가 자체 직원 또는 외부 CM(건설사업관리) 업체를 감독관으로 지정합니다.",
        "meaningVi": "Giám đốc công trình (cán bộ giám sát) là công chức hoặc nhân viên thuộc chủ đầu tư (chủ nhà, cơ quan nhà nước, cơ quan công) trực tiếp quản lý, giám sát công trình xây dựng. Khác với giám lý (nhân viên công ty giám sát độc lập), giám đốc công trình là nhân viên nội bộ chủ đầu tư. Nhiệm vụ chính: đại diện chủ đầu tư quản lý nhà thầu và giám lý, kiểm tra chi phí và khối lượng hoàn thành, xem xét thay đổi thiết kế, giám sát thực hiện hợp đồng, nghiệm thu và quản lý bảo hành. Là đại diện chủ đầu tư trong hợp đồng, có quyền thanh toán, phê duyệt thay đổi, xử phạt vi phạm hợp đồng.",
        "context": "건설현장, 발주자, 계약관리",
        "culturalNote": "한국 감독관은 '발주자의 대리인'으로, 공사 계약의 실질적 권한을 행사합니다. 감독관은 매주 공정회의를 주재하고, 기성 검사(출래공 공정률 확인)를 하여 공사비를 지급하며, 시공사·감리사의 보고를 받고 문제를 해결합니다. 한국 공공 공사는 발주 기관(국토부, 지자체, 공기업)의 공무원이 감독관으로 지정되며, 토목·건축·전기·기계 등 분야별로 여러 명의 감독관이 배치됩니다. 민간 공사는 건축주가 자체 직원을 감독관으로 지정하거나, CM(건설사업관리) 업체에 위탁하여 감독관 역할을 대행시킵니다. 한국 건설업계는 감독관을 '돈 줄을 쥔 사람'으로 부르며, 시공사는 감독관의 승인을 받아야 공사비를 받을 수 있습니다. 베트남은 'giám đốc công trình' 또는 'ban quản lý dự án' 개념이 있으며, 한국과 유사하게 발주자를 대표합니다. 그러나 베트남 감독관은 주로 서류 승인과 보고 업무를 하고, 현장 관리는 감리사(tư vấn giám sát)에게 위임하는 경우가 많습니다. 한국 감독관은 현장을 자주 방문하고 직접 검수하지만, 베트남 감독관은 사무실에서 보고서를 검토하는 경우가 흔합니다. 통역 시 한국 감독관의 권한(공사비 지급, 설계 변경 승인, 계약 위반 조치)과 역할(발주자 대리인)을 명확히 전달해야 합니다.",
        "commonMistakes": [
            {
                "mistake": "'감독관'을 'người giám sát'(감독자)로 번역",
                "correction": "'giám đốc công trình' 또는 'cán bộ giám sát chủ đầu tư' 사용",
                "explanation": "'giám đốc công trình'이 발주자 측 감독관을 명확히 표현"
            },
            {
                "mistake": "'감독관'과 '감리원'을 구분 없이 번역",
                "correction": "감독관='giám đốc công trình, chủ đầu tư'(발주자), 감리원='giám lý, bên thứ ba'(독립 기관)으로 구분",
                "explanation": "감독관은 발주자 직원, 감리원은 감리회사 직원"
            },
            {
                "mistake": "'기성 검사'를 'kiểm tra hoàn thành'(완료 검사)로 번역",
                "correction": "'kiểm tra khối lượng hoàn thành' 또는 'kiểm tra giá trị hoàn thành' 사용",
                "explanation": "기성 검사는 일정 기간 완료된 공정량을 확인하여 공사비를 지급하는 절차"
            }
        ],
        "examples": [
            {
                "ko": "감독관은 이번 달 기성 검사를 실시하고 공사비 지급을 승인했습니다.",
                "vi": "Giám đốc công trình thực hiện kiểm tra khối lượng hoàn thành tháng này và phê duyệt thanh toán.",
                "situation": "formal"
            },
            {
                "ko": "감독관님, 설계 변경이 필요한데 승인해주실 수 있나요?",
                "vi": "Giám đốc công trình, cần thay đổi thiết kế, anh có thể phê duyệt không ạ?",
                "situation": "informal"
            },
            {
                "ko": "감독관은 공사가 지연되고 있어 시공사에 벌칙금을 부과하기로 했습니다.",
                "vi": "Giám đốc công trình quyết định phạt nhà thầu vì công trình bị chậm tiến độ.",
                "situation": "onsite"
            }
        ],
        "relatedTerms": [
            "감리원",
            "발주자",
            "기성검사",
            "설계변경",
            "계약관리"
        ]
    },
    {
        "slug": "ky-su-thi-cong",
        "korean": "시공기술자",
        "vietnamese": "kỹ sư thi công",
        "hanja": "施工技術者",
        "hanjaReading": "시(베풀 시) + 공(장인 공) + 기(기술 기) + 술(재주 술) + 자(사람 자)",
        "pronunciation": "끼 슈 티 꽁",
        "meaningKo": "건설 현장에서 설계도서와 시방서에 따라 실제 시공을 수행하는 기술 인력으로, 건설기술인 자격(기술사, 기사, 산업기사, 기능사)을 보유한 전문가입니다. 통역 시 '시공기술자'는 'kỹ sư thi công' 또는 'kỹ thuật viên thi công'으로 표현하며, '일반 근로자(công nhân)'와 구분해야 합니다. 시공기술자는 기술 자격을 보유하고 시공을 지휘·관리하는 사람이고, 근로자는 기능만 보유하고 작업을 수행하는 사람입니다. 시공기술자의 주요 업무는: (1) 설계도서 검토 및 시공 계획 수립, (2) 작업 지시 및 근로자 관리, (3) 자재·장비 선정 및 품질 확인, (4) 시공 품질 자체 검사, (5) 감리원·감독관 협의 및 보고입니다. 시공기술자는 건설기술진흥법에 따라 공종별로 배치 의무가 있으며, 토목, 건축, 전기, 기계, 조경, 안전 등 분야별로 전문성을 갖춥니다. 한국 건설산업기본법 제41조에 따라 시공기술자는 '건설공사의 시공 관리'를 담당하며, 부실시공 방지 의무가 있습니다.",
        "meaningVi": "Kỹ sư thi công (kỹ thuật viên thi công) là nhân lực kỹ thuật thực hiện thi công thực tế theo bản vẽ và tiêu chuẩn kỹ thuật tại công trường, chuyên gia có bằng kỹ thuật viên xây dựng (kỹ sư, kỹ thuật viên cao cấp, trung cấp, sơ cấp). Khác với công nhân thường (không có chứng chỉ), kỹ sư thi công có bằng kỹ thuật và chỉ huy, quản lý thi công. Nhiệm vụ chính: xem xét bản vẽ, lập kế hoạch thi công, chỉ thị công nhân, chọn vật tư thiết bị, kiểm tra chất lượng tự thể, trao đổi và báo cáo với giám lý, giám đốc công trình.",
        "context": "건설현장, 시공관리, 기술자격",
        "culturalNote": "한국 시공기술자는 '현장의 기술 전문가'로, 설계도서를 이해하고 현장 여건에 맞게 시공 방법을 결정합니다. 시공기술자는 보통 건설기사, 산업기사, 기능사 자격을 보유하며, 토목, 건축, 전기, 기계, 조경 등 전문 분야를 갖습니다. 한국 건설현장은 공종별로 시공기술자를 배치해야 하며, 배치 기준은 공사 규모와 난이도에 따라 건설기술진흥법 시행령으로 규정됩니다. 시공기술자는 근로자에게 작업 지시를 내리고, 시공 중 발생하는 문제(자재 부족, 도면 불명확, 장비 고장)를 해결하며, 감리원의 검수를 받습니다. 한국 건설업계는 시공기술자를 '현장의 실무자'로 부르며, 시공기술자가 우수하면 공사 품질이 높고 일정이 준수됩니다. 베트남은 'kỹ sư thi công' 또는 'kỹ thuật viên thi công' 개념이 있으며, 한국과 유사하게 기술 자격을 보유한 전문가를 지칭합니다. 그러나 베트남은 자격증 취득이 한국보다 쉽고, 자격증 없이 경험만으로 시공기술자 역할을 하는 경우도 많습니다. 한국은 자격증 없이 시공기술자로 인정받을 수 없으며, 무자격자가 시공을 지휘하면 건설업법 위반으로 처벌됩니다. 통역 시 한국 시공기술자의 자격 요건(기술사, 기사, 산업기사)과 역할(시공 계획, 작업 지시, 품질 검사)을 명확히 전달해야 합니다.",
        "commonMistakes": [
            {
                "mistake": "'시공기술자'를 'công nhân thi công'(시공 근로자)으로 번역",
                "correction": "'kỹ sư thi công' 또는 'kỹ thuật viên thi công' 사용",
                "explanation": "'công nhân'은 일반 근로자, 'kỹ sư/kỹ thuật viên'은 기술 자격 보유자"
            },
            {
                "mistake": "'건설기술인'을 'người kỹ thuật xây dựng'로 직역",
                "correction": "'kỹ sư xây dựng có chứng chỉ' 사용",
                "explanation": "건설기술인은 법정 자격(기술사, 기사 등)을 보유한 사람"
            },
            {
                "mistake": "'공종'을 'loại công việc'(작업 종류)로 직역",
                "correction": "'chuyên ngành thi công' 또는 'loại công trình' 사용",
                "explanation": "공종은 토목, 건축, 전기 등 시공 전문 분야를 의미"
            }
        ],
        "examples": [
            {
                "ko": "시공기술자는 설계도서를 검토하고 철근 배근 계획을 수립했습니다.",
                "vi": "Kỹ sư thi công xem xét bản vẽ và lập kế hoạch bố trí thép.",
                "situation": "formal"
            },
            {
                "ko": "시공기술자님, 이 부위 콘크리트 강도가 부족한데 어떻게 해야 할까요?",
                "vi": "Kỹ sư thi công, bộ phận này cường độ bê tông không đủ, nên xử lý thế nào ạ?",
                "situation": "informal"
            },
            {
                "ko": "시공기술자는 근로자에게 안전 수칙을 교육하고 작업을 지시했습니다.",
                "vi": "Kỹ sư thi công giáo dục công nhân về quy định an toàn và chỉ thị công việc.",
                "situation": "onsite"
            }
        ],
        "relatedTerms": [
            "건설기술인",
            "건설기사",
            "산업기사",
            "공종",
            "시공계획"
        ]
    },
    {
        "slug": "nha-quan-ly-du-an-xay-dung",
        "korean": "건설사업관리자",
        "vietnamese": "nhà quản lý dự án xây dựng",
        "hanja": "建設事業管理者",
        "hanjaReading": "건(세울 건) + 설(베풀 설) + 사(일 사) + 업(업 업) + 관(관청 관) + 리(다스릴 리) + 자(사람 자)",
        "pronunciation": "냐 꽌 리 주 안 사이 증",
        "meaningKo": "발주자를 대신하여 건설 프로젝트 전반(기획, 설계, 시공, 유지관리)을 종합적으로 관리하는 전문 기술자 또는 업체(CM, Construction Management)입니다. 통역 시 '건설사업관리자'는 'nhà quản lý dự án xây dựng' 또는 'đơn vị quản lý dự án (CM)'로 표현하며, '감리원'과 구분해야 합니다. 감리원은 시공 단계의 품질·안전만 감독하고, 건설사업관리자는 기획부터 유지관리까지 프로젝트 전체를 관리합니다. 건설사업관리자의 주요 업무는: (1) 사업 기획 및 타당성 검토, (2) 설계 관리 및 VE(가치공학) 제안, (3) 시공 관리(공정, 품질, 안전, 계약), (4) 비용 관리 및 원가 절감, (5) 유지관리 계획 수립입니다. 건설사업관리자는 발주자의 '총괄 대리인'으로, 설계사·시공사·감리사를 조율하고, 프로젝트 목표(기한, 예산, 품질)를 달성하도록 관리합니다. 한국 건설기술진흥법 제2조에 따라 건설사업관리는 '건설공사에 관한 기획, 타당성 조사, 분석, 설계, 조달, 계약, 시공관리, 감리, 평가 또는 사후관리 등에 관한 관리 업무의 전부 또는 일부'로 정의됩니다. 한국은 대형 공공 공사(500억 원 이상)에 건설사업관리(CM) 적용을 의무화하고 있습니다.",
        "meaningVi": "Nhà quản lý dự án xây dựng (đơn vị quản lý dự án, CM) là kỹ thuật viên hoặc đơn vị chuyên nghiệp đại diện chủ đầu tư quản lý toàn diện dự án xây dựng (lập kế hoạch, thiết kế, thi công, bảo trì). Khác với giám lý (chỉ giám sát chất lượng, an toàn giai đoạn thi công), nhà quản lý dự án xây dựng quản lý toàn bộ dự án từ lập kế hoạch đến bảo trì. Nhiệm vụ chính: lập kế hoạch dự án, xem xét khả thi, quản lý thiết kế, đề xuất VE, quản lý thi công (tiến độ, chất lượng, an toàn, hợp đồng), quản lý chi phí, lập kế hoạch bảo trì. Là đại diện tổng thể chủ đầu tư, điều phối nhà thiết kế, nhà thầu, giám lý.",
        "context": "건설사업, 프로젝트관리, CM",
        "culturalNote": "한국 건설사업관리자(CM)는 '발주자의 두뇌'로, 프로젝트 전 단계에서 의사결정을 지원하고 문제를 해결합니다. CM은 발주자가 건설 전문성이 부족할 때 고용하는 외부 전문가이며, 설계 단계에서는 설계 적정성을 검토하고 VE(가치공학)로 원가를 절감하며, 시공 단계에서는 공정·품질·안전을 관리하고, 준공 후에는 하자 관리와 유지관리 계획을 수립합니다. 한국 공공 공사는 발주자(국토부, 지자체, 공기업)가 CM 업체를 선정하여 프로젝트 관리를 위임하며, 민간 공사도 대형 프로젝트(빌딩, 공장, 리조트)는 CM을 고용하는 경우가 많습니다. 한국 건설업계는 CM을 '프로젝트 매니저(PM)'로 부르기도 하며, CM과 PM은 유사한 역할을 합니다. 베트남은 'nhà quản lý dự án' 또는 'đơn vị tư vấn quản lý dự án' 개념이 있으며, 대형 프로젝트에서 활용되고 있습니다. 그러나 베트남 CM은 주로 공정 관리와 보고 업무를 하고, 설계 관리나 VE 제안은 드뭅니다. 한국 CM은 발주자를 대신하여 설계사·시공사와 협상하고, 계약 변경·클레임을 처리하지만, 베트남 CM은 조정·중재 역할에 그치는 경우가 많습니다. 통역 시 한국 CM의 역할(기획~유지관리 전 단계 관리)과 권한(설계사·시공사 조율, 의사결정 지원)을 명확히 전달해야 합니다.",
        "commonMistakes": [
            {
                "mistake": "'건설사업관리자'를 'người quản lý công trình'(공사 관리자)로 번역",
                "correction": "'nhà quản lý dự án xây dựng' 또는 'đơn vị quản lý dự án (CM)' 사용",
                "explanation": "건설사업관리자는 프로젝트 전체를 관리하는 PM/CM 역할"
            },
            {
                "mistake": "'건설사업관리자'와 '감리원'을 구분 없이 번역",
                "correction": "건설사업관리자='quản lý toàn bộ dự án'(전 단계 관리), 감리원='giám sát thi công'(시공 감독)으로 구분",
                "explanation": "건설사업관리자는 기획~유지관리, 감리원은 시공 단계만 담당"
            },
            {
                "mistake": "'VE(가치공학)'를 번역 없이 영문 약어만 사용",
                "correction": "'kỹ thuật giá trị' 또는 'Value Engineering (VE)' 병기",
                "explanation": "베트남 기술자는 VE 용어에 익숙하지 않음"
            }
        ],
        "examples": [
            {
                "ko": "건설사업관리자는 설계 단계에서 VE 제안을 통해 공사비를 10% 절감했습니다.",
                "vi": "Nhà quản lý dự án xây dựng giảm 10% chi phí công trình qua đề xuất VE trong giai đoạn thiết kế.",
                "situation": "formal"
            },
            {
                "ko": "건설사업관리자님, 설계 변경이 공사비에 미치는 영향을 검토해주세요.",
                "vi": "Nhà quản lý dự án, vui lòng xem xét ảnh hưởng của thay đổi thiết kế đến chi phí công trình.",
                "situation": "informal"
            },
            {
                "ko": "건설사업관리자는 발주자를 대신하여 시공사와 공정 지연 문제를 협의했습니다.",
                "vi": "Nhà quản lý dự án đại diện chủ đầu tư trao đổi với nhà thầu về vấn đề chậm tiến độ.",
                "situation": "onsite"
            }
        ],
        "relatedTerms": [
            "CM",
            "프로젝트매니저",
            "감리원",
            "VE",
            "공정관리"
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
