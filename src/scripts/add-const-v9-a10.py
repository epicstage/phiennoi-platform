#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
현장보안/출입통제 테마 - Construction 용어 10개 추가
출입증, 방문자관리, 자재출입관리, 보안울타리, 감시카메라, 야간경비, 보안교육, 현장식별표지, 위험구역표시, 출입기록대장
"""

import json
import os

# 추가할 10개 용어 데이터 (Tier S 기준)
new_terms = [
    {
        "slug": "the-ra-vao",
        "korean": "출입증",
        "vietnamese": "Thẻ ra vào",
        "hanja": "出入證",
        "hanjaReading": "날 출(出) + 들 입(入) + 증거 증(證)",
        "pronunciation": "출리쁘쯩",
        "meaningKo": "건설 현장에 출입하는 모든 인원(근로자, 방문자, 협력업체 직원 등)에게 발급하는 신분 확인 및 출입 허가 증명 카드로, '출입 카드', '현장 카드', '패스'라고도 불립니다. 통역 시 주의할 점은 한국 건설 현장에서는 출입증 없이는 절대 현장 진입이 불가능하며, 출입증에는 사진, 이름, 소속, 출입 권한 구역, 유효 기간 등이 표기되어 있습니다. 베트남어로는 'thẻ ra vào', 'thẻ kiểm soát', 'thẻ nhận diện'으로 표현합니다. 출입증은 크게 상시 출입증(thẻ ra vào thường xuyên)과 임시 출입증(thẫ tạm thời)으로 구분되며, 근로자용, 방문자용, 차량용으로 나뉩니다. 한국 산업안전보건법과 건설기술진흥법에서는 현장 출입자 관리를 의무화하고 있으며, 출입증을 패용하지 않으면 현장 진입이 거부됩니다. 통역 시 출입증 분실 시 즉시 신고하고 재발급받아야 하며, 타인에게 양도하면 안 된다는 점을 명확히 전달해야 합니다. 출입증은 보안 목적뿐만 아니라 재해 발생 시 현장 인원 파악을 위한 중요한 안전 장치입니다.",
        "meaningVi": "Thẻ ra vào (출입증) là thẻ chứng minh danh tính và giấy phép ra vào được cấp cho tất cả nhân viên vào công trường xây dựng (công nhân, khách, nhân viên đối tác), còn gọi là thẻ kiểm soát hoặc thẻ nhận diện. Tại Hàn Quốc, không có thẻ ra vào tuyệt đối không được vào công trường, và trên thẻ có ghi ảnh, tên, đơn vị, khu vực được phép vào, thời hạn sử dụng. Thẻ ra vào chia làm hai loại: thẻ thường xuyên và thẻ tạm thời, và phân theo người lao động, khách và phương tiện. Theo luật An toàn lao động và Luật Xúc tiến Công nghệ Xây dựng Hàn Quốc, bắt buộc phải quản lý người ra vào công trường, không đeo thẻ sẽ bị từ chối vào. Nếu mất thẻ phải báo ngay và cấp lại, không được cho người khác mượn. Thẻ ra vào không chỉ phục vụ mục đích bảo mật mà còn là thiết bị an toàn quan trọng để xác định nhân sự tại hiện trường khi xảy ra tai nạn.",
        "context": "건설 현장 출입 통제, 신분 확인, 보안 관리, 재해 시 인원 파악",
        "culturalNote": "한국 건설 현장에서는 출입증 관리가 매우 엄격하게 이루어집니다. 대형 현장의 경우 출입구에 게이트와 보안 요원이 배치되어 있으며, 출입증을 RFID 리더기나 바코드 스캐너로 인식시켜야 출입문이 열립니다. 출입증은 목에 걸거나 가슴에 부착하여 항상 보이는 곳에 패용해야 하며, 미착용 시 경고를 받거나 퇴장 조치됩니다. 특히 안전모에 출입증 케이스를 부착하는 경우도 많습니다. 베트남에서는 출입증 관리가 상대적으로 느슨하여 출입증 없이도 현장 출입이 가능한 경우가 있으나, 한국에서는 이것이 절대 불가능하며 중대한 보안 위반임을 강조해야 합니다. 또한 한국에서는 출입증에 QR 코드나 바코드가 포함되어 있어 출퇴근 시간이 자동 기록되므로, 대리 출퇴근이 불가능하다는 점도 설명해야 합니다. 통역 시 출입증은 단순한 신분증이 아니라 현장 안전과 보안을 위한 필수 장비임을 명확히 전달해야 합니다.",
        "commonMistakes": [
            {
                "mistake": "'신분증' 또는 'giấy tờ tùy thân'으로 통역하여 일반 신분증과 혼동",
                "correction": "'출입증' 또는 'thẻ ra vào'로 명확히 구분",
                "explanation": "신분증은 개인 식별용이고, 출입증은 현장 출입 허가증이므로 다릅니다."
            },
            {
                "mistake": "출입증 패용 의무 강조 누락",
                "correction": "항상 보이는 곳에 착용 의무 및 미착용 시 처벌 명시",
                "explanation": "출입증 미착용은 안전 위반이므로 반드시 강조해야 합니다."
            },
            {
                "mistake": "출입증 종류(상시/임시/방문자) 구분 없이 통역",
                "correction": "출입증 유형별 권한과 용도 차이 설명",
                "explanation": "출입증 종류에 따라 출입 가능 구역과 기간이 다르므로 구분해야 합니다."
            }
        ],
        "examples": [
            {
                "ko": "현장 출입 시에는 반드시 출입증을 목에 걸고 보이는 곳에 패용해야 하며, 출입증이 없거나 미착용 시 현장 진입이 거부됩니다.",
                "vi": "Khi vào công trường bắt buộc phải đeo thẻ ra vào ở cổ hoặc nơi dễ nhìn thấy, nếu không có thẻ hoặc không đeo sẽ bị từ chối vào.",
                "situation": "formal"
            },
            {
                "ko": "출입증을 분실하셨다고요? 즉시 안전관리팀에 신고하시고 임시 출입증을 재발급받으셔야 합니다. 분실 신고 없이 사용하시면 보안 위반으로 처리됩니다.",
                "vi": "Bạn mất thẻ ra vào à? Phải báo ngay cho đội quản lý an toàn và cấp lại thẻ tạm thời. Nếu dùng mà không báo mất sẽ bị xử lý vi phạm bảo mật.",
                "situation": "onsite"
            },
            {
                "ko": "야, 카드 안 걸었네? 보안 아저씨한테 걸리면 쫓겨나. 얼른 가져와.",
                "vi": "Ê, không đeo thẻ à? Bác bảo vệ thấy là bị đuổi ra đấy. Lấy về nhanh đi.",
                "situation": "informal"
            }
        ],
        "relatedTerms": [
            "출입 통제",
            "신분 확인",
            "게이트 관리",
            "RFID 카드",
            "출퇴근 기록"
        ]
    },
    {
        "slug": "quan-ly-khach-tham-quan",
        "korean": "방문자 관리",
        "vietnamese": "Quản lý khách tham quan",
        "hanja": "訪問者管理",
        "hanjaReading": "찾아갈 방(訪) + 물을 문(問) + 사람 자(者) + 관리할 관(管) + 다스릴 리(理)",
        "pronunciation": "꾸안리 칵 탐꾸안",
        "meaningKo": "건설 현장을 방문하는 외부인(발주처 관계자, 감리단, 협력업체, 견학자 등)의 출입을 체계적으로 관리하는 절차와 시스템으로, '외부인 관리', '비상주 출입 관리'라고도 불립니다. 통역 시 주의할 점은 한국 건설 현장에서는 모든 방문자에 대해 사전 신청, 신분 확인, 안전 교육, 임시 출입증 발급, 동행 안내 등의 절차가 엄격하게 적용됩니다. 베트남어로는 'quản lý khách tham quan', 'kiểm soát người ngoài', 'quản lý khách ra vào'로 표현합니다. 방문자 관리는 보안 목적뿐만 아니라 안전사고 예방을 위해서도 필수적이며, 방문자에게는 안전모, 안전화, 안전조끼 등 개인보호구를 착용시키고 위험 구역 출입을 제한합니다. 한국 산업안전보건법에서는 현장 방문자에 대한 안전 교육과 보호구 착용을 의무화하고 있으며, 건설업 산업안전보건관리비 계상 및 사용 기준에서도 방문자 안전 관리 항목을 포함하고 있습니다. 통역 시 방문자는 반드시 지정된 안내자와 동행해야 하며, 혼자 현장을 돌아다니면 안 된다는 점을 명확히 전달해야 합니다.",
        "meaningVi": "Quản lý khách tham quan (방문자 관리) là quy trình và hệ thống quản lý có hệ thống việc ra vào của người bên ngoài đến công trường xây dựng (người liên quan bên đặt hàng, giám sát, đối tác, người tham quan). Tại Hàn Quốc, với mọi khách tham quan đều phải thực hiện nghiêm ngặt các thủ tục: đăng ký trước, xác minh danh tính, giáo dục an toàn, cấp thẻ ra vào tạm thời, hướng dẫn đi cùng. Quản lý khách không chỉ vì mục đích bảo mật mà còn bắt buộc để phòng ngừa tai nạn an toàn, khách phải đeo đồ bảo hộ cá nhân như mũ, giày, áo an toàn và hạn chế vào khu vực nguy hiểm. Theo Luật An toàn lao động Hàn Quốc, bắt buộc phải giáo dục an toàn và đeo đồ bảo hộ cho khách tham quan công trường. Khách bắt buộc phải đi cùng với người hướng dẫn được chỉ định, không được tự ý đi lại trong công trường.",
        "context": "건설 현장 보안, 외부인 출입 통제, 안전사고 예방, 방문 기록 관리",
        "culturalNote": "한국 건설 현장에서는 방문자 관리가 매우 체계적으로 이루어집니다. 방문 전날 또는 당일 오전에 방문자 명단을 사전 등록하고, 방문 시 현장 출입구에서 신분증을 제시하고 방문자 대장에 서명한 후 임시 출입증을 발급받습니다. 방문자에게는 간단한 안전 교육(5~10분)을 실시하고 안전 서약서에 서명받으며, 안전모, 안전화, 반광 조끼를 지급합니다. 방문자는 반드시 현장 담당자나 안전 관리자의 동행 하에 이동하며, 혼자 현장을 돌아다니는 것은 엄격히 금지됩니다. 특히 위험 구역(굴착, 고소작업, 중장비 작업)은 출입이 제한되며, 필요한 경우 안전 담당자의 특별 허가를 받아야 합니다. 베트남에서는 방문자 관리가 상대적으로 간소하여 현장을 자유롭게 돌아다니는 경우가 많으나, 한국에서는 이것이 중대한 안전 위반임을 강조해야 합니다. 또한 방문 종료 시 출입증과 보호구를 반납하고 방문 종료 서명을 해야 합니다. 통역 시 방문자 관리는 단순한 형식이 아니라 법적 의무이며, 방문자가 사고를 당할 경우 현장 관리자가 법적 책임을 지게 된다는 점을 명확히 전달해야 합니다.",
        "commonMistakes": [
            {
                "mistake": "'손님 관리' 또는 'tiếp khách'로 통역하여 일반 접객과 혼동",
                "correction": "'방문자 관리' 또는 'quản lý khách tham quan'으로 명시",
                "explanation": "현장 방문자는 손님이 아니라 안전 관리 대상이므로 구분해야 합니다."
            },
            {
                "mistake": "사전 등록 및 안전 교육 절차 설명 누락",
                "correction": "방문 전 등록, 신분 확인, 안전 교육, 보호구 착용 순서 설명",
                "explanation": "방문자 관리는 여러 단계의 절차가 있으므로 순서대로 설명해야 합니다."
            },
            {
                "mistake": "혼자 현장 이동 금지 사항 미전달",
                "correction": "반드시 안내자 동행 의무 및 위반 시 처벌 명시",
                "explanation": "무단 이동은 중대한 안전 위반이므로 금지 사항을 강조해야 합니다."
            }
        ],
        "examples": [
            {
                "ko": "내일 오전 10시에 발주처 관계자 5명이 현장을 방문하실 예정입니다. 방문자 명단을 사전 등록하시고 안전모와 안전조끼 5벌을 준비해 주십시오.",
                "vi": "Ngày mai lúc 10h sáng có 5 người liên quan bên đặt hàng sẽ đến thăm công trường. Vui lòng đăng ký danh sách khách trước và chuẩn bị 5 bộ mũ và áo an toàn.",
                "situation": "formal"
            },
            {
                "ko": "방문자는 현장을 혼자 돌아다닐 수 없습니다. 반드시 안내 담당자와 함께 이동하시고, 위험 구역 출입은 금지되어 있습니다.",
                "vi": "Khách tham quan không được tự ý đi lại trong công trường. Bắt buộc phải di chuyển cùng người hướng dẫn, và cấm vào khu vực nguy hiểm.",
                "situation": "onsite"
            },
            {
                "ko": "저기 손님들 오시는데, 안전모하고 조끼 챙겨서 정문으로 나가 있어.",
                "vi": "Khách đang đến kìa, lấy mũ với áo ra đợi ở cổng chính.",
                "situation": "informal"
            }
        ],
        "relatedTerms": [
            "출입증",
            "안전 교육",
            "동행 안내",
            "방문자 대장",
            "개인보호구"
        ]
    },
    {
        "slug": "quan-ly-ra-vao-vat-tu",
        "korean": "자재 출입 관리",
        "vietnamese": "Quản lý ra vào vật tư",
        "hanja": "資材出入管理",
        "hanjaReading": "재물 자(資) + 재목 재(材) + 날 출(出) + 들 입(入) + 관리할 관(管) + 다스릴 리(理)",
        "pronunciation": "꾸안리 자 바오 벗뜨",
        "meaningKo": "건설 현장에 반입되는 모든 자재와 장비, 그리고 반출되는 폐기물과 불용자재를 체계적으로 기록하고 관리하는 절차로, '자재 입출고 관리', '물품 반입 관리'라고도 불립니다. 통역 시 주의할 점은 한국 건설 현장에서는 모든 자재 출입에 대해 입고 전표, 출고 전표, 검수 기록을 작성하고 보관해야 하며, 자재 반입 시 품질 확인, 수량 확인, 규격 확인을 거쳐야 합니다. 베트남어로는 'quản lý ra vào vật tư', 'kiểm soát vật liệu', 'quản lý nhập xuất nguyên vật liệu'로 표현합니다. 자재 출입 관리는 크게 반입 관리(quản lý nhập)와 반출 관리(quản lý xuất)로 구분되며, 반입 시에는 납품 업체, 자재명, 수량, 규격, 입고 일시를 기록하고, 반출 시에는 반출 목적, 수량, 반출처, 승인자를 기록합니다. 한국 건설산업기본법과 건설기술진흥법에서는 주요 자재에 대한 품질 관리와 입출고 기록 보관을 의무화하고 있으며, 특히 구조 안전에 영향을 미치는 자재(철근, 레미콘, 철골 등)는 시험 성적서와 함께 기록을 보관해야 합니다. 통역 시 자재 무단 반입이나 무단 반출은 절도나 횡령으로 간주되어 법적 처벌을 받을 수 있다는 점을 명확히 전달해야 합니다.",
        "meaningVi": "Quản lý ra vào vật tư (자재 출입 관리) là quy trình ghi chép và quản lý có hệ thống tất cả vật tư, thiết bị được đưa vào công trường và phế thải, vật tư không dùng được đưa ra, còn gọi là quản lý nhập xuất vật tư. Tại Hàn Quốc, với mọi vật tư ra vào đều phải lập phiếu nhập, phiếu xuất, biên bản nghiệm thu và lưu trữ, khi nhập vật tư phải trải qua kiểm tra chất lượng, số lượng, quy cách. Quản lý ra vào vật tư chia làm quản lý nhập và quản lý xuất, khi nhập ghi nhà cung cấp, tên vật tư, số lượng, quy cách, thời gian nhập, khi xuất ghi mục đích xuất, số lượng, nơi xuất, người phê duyệt. Theo Luật Cơ bản Ngành Xây dựng và Luật Xúc tiến Công nghệ Xây dựng Hàn Quốc, bắt buộc phải quản lý chất lượng và lưu trữ sổ nhập xuất đối với vật tư chính, đặc biệt vật tư ảnh hưởng đến an toàn kết cấu (thép, bê tông, khung thép) phải lưu kèm giấy chứng nhận thử nghiệm. Nhập xuất vật tư trái phép có thể bị coi là trộm cắp hoặc biển thủ và bị xử lý theo pháp luật.",
        "context": "건설 현장 자재 관리, 입출고 기록, 품질 관리, 재고 관리, 도난 방지",
        "culturalNote": "한국 건설 현장에서는 자재 출입 관리가 매우 체계적으로 이루어지며, 대형 현장의 경우 전용 자재 게이트와 검수 구역이 별도로 마련되어 있습니다. 자재 반입 차량은 게이트에서 대기하여 납품 전표를 제출하고, 자재 담당자가 수량과 규격을 확인한 후 입고 승인을 받아야 현장에 진입할 수 있습니다. 주요 자재의 경우 품질 시험 성적서와 제조사 인증서를 함께 제출해야 하며, 이 서류가 없으면 반입이 거부됩니다. 자재 반출 시에는 반출 승인서에 현장 소장이나 공사 관리자의 서명을 받아야 하며, 무단 반출 시 도난으로 간주되어 경찰에 신고될 수 있습니다. 특히 철근, 동파이프, 전선 등 고가 자재는 별도의 보안 구역에 보관하고 출입을 통제합니다. 베트남에서는 자재 출입 관리가 상대적으로 느슨하여 구두 확인으로 자재를 반입/반출하는 경우가 많으나, 한국에서는 반드시 서류 기록을 남겨야 하며 사후 감사에서 기록이 없으면 횡령이나 부정으로 의심받을 수 있음을 강조해야 합니다. 통역 시 자재 출입 관리는 단순한 행정 업무가 아니라 공사 원가 관리와 법적 책임 문제와 직결되어 있음을 명확히 전달해야 합니다.",
        "commonMistakes": [
            {
                "mistake": "'자재 관리' 또는 'quản lý vật tư'로만 통역하여 출입 통제 의미 누락",
                "correction": "'자재 출입 관리' 또는 'quản lý ra vào vật tư'로 명시",
                "explanation": "출입 통제와 기록 관리가 핵심이므로 '출입'을 명확히 해야 합니다."
            },
            {
                "mistake": "반입/반출 승인 절차 설명 누락",
                "correction": "전표 제출, 검수, 승인 서명 등 단계별 절차 설명",
                "explanation": "자재 출입은 여러 단계의 승인 절차가 있으므로 순서대로 설명해야 합니다."
            },
            {
                "mistake": "무단 반출 시 법적 처벌 경고 미전달",
                "correction": "무단 반출은 절도/횡령으로 간주되어 형사 처벌 가능 명시",
                "explanation": "무단 반출의 심각성을 강조하기 위해 법적 처벌을 명시해야 합니다."
            }
        ],
        "examples": [
            {
                "ko": "자재 반입 시에는 납품 전표와 품질 시험 성적서를 함께 제출하시고, 자재 담당자의 검수 확인을 받으신 후에 하역해 주십시오.",
                "vi": "Khi nhập vật tư vui lòng nộp phiếu giao hàng và giấy chứng nhận thử nghiệm chất lượng, sau khi nhận xác nhận nghiệm thu của người phụ trách vật tư mới được dỡ hàng.",
                "situation": "formal"
            },
            {
                "ko": "현장에서 자재를 반출하려면 반출 승인서에 소장님 서명을 받아야 합니다. 승인 없이 자재를 가져가면 절도로 간주되어 경찰에 신고됩니다.",
                "vi": "Để xuất vật tư ra khỏi công trường phải có chữ ký của giám đốc công trường trên giấy phê duyệt xuất. Lấy vật tư ra ngoài khi chưa có phép sẽ bị coi là trộm cắp và báo công an.",
                "situation": "onsite"
            },
            {
                "ko": "야, 트럭 왔는데 전표 있어? 없으면 못 들어와. 먼저 사무실 가서 받아와.",
                "vi": "Ê, xe tải đến rồi có phiếu không? Không có thì không vào được. Lên văn phòng lấy trước đi.",
                "situation": "informal"
            }
        ],
        "relatedTerms": [
            "입고 전표",
            "출고 전표",
            "품질 검수",
            "재고 관리",
            "자재 게이트"
        ]
    },
    {
        "slug": "hang-rao-bao-mat",
        "korean": "보안 울타리",
        "vietnamese": "Hàng rào bảo mật",
        "hanja": "保安fence",
        "hanjaReading": "지킬 보(保) + 편안할 안(安) + fence",
        "pronunciation": "항자오 바오먿",
        "meaningKo": "건설 현장의 외곽 경계를 둘러싸고 설치하는 높이 2m 이상의 견고한 울타리로, 무단 출입과 외부 침입을 방지하고 현장 보안을 유지하는 시설이며, '가설 울타리', '가림막', '현장 펜스'라고도 불립니다. 통역 시 주의할 점은 한국 건설 현장에서는 공사 착공 전 가장 먼저 보안 울타리를 설치해야 하며, 울타리에는 공사 개요, 안전 표지판, 연락처 등을 부착합니다. 베트남어로는 'hàng rào bảo mật', 'hàng rào công trường', 'tường rào tạm'으로 표현합니다. 보안 울타리는 용도와 위치에 따라 여러 종류가 있는데, 도심지 현장에서는 방음벽 기능을 겸한 패널형 울타리를 사용하고, 외곽 지역에서는 철망 펜스를 주로 사용합니다. 한국 건설기술진흥법 시행령에서는 높이 2m 이상의 가설 울타리 설치를 의무화하고 있으며, 건축법에서는 도로변 울타리에 안전 표지와 조명 설치를 요구합니다. 통역 시 보안 울타리는 단순한 경계 표시가 아니라 법적 의무 시설이며, 미설치 시 공사 중지 명령을 받을 수 있다는 점을 명확히 전달해야 합니다. 울타리에는 출입문을 최소화하고 주 출입구 외에는 잠금장치를 설치하여 무단 출입을 방지합니다.",
        "meaningVi": "Hàng rào bảo mật (보안 울타리) là hàng rào kiên cố cao từ 2m trở lên được lắp đặt bao quanh ranh giới ngoài của công trường xây dựng, là thiết bị ngăn chặn ra vào trái phép và xâm nhập từ bên ngoài, duy trì bảo mật công trường. Tại Hàn Quốc, trước khi khởi công phải lắp đặt hàng rào bảo mật trước tiên, và trên hàng rào phải dán nội dung thi công, biển báo an toàn, số điện thoại liên lạc. Hàng rào bảo mật có nhiều loại tùy theo mục đích và vị trí, tại công trường nội thành dùng hàng rào tấm kiêm chức năng tường chắn âm, khu vực ngoại ô chủ yếu dùng hàng rào lưới sắt. Theo Nghị định thi hành Luật Xúc tiến Công nghệ Xây dựng Hàn Quốc, bắt buộc phải lắp đặt hàng rào tạm cao từ 2m trở lên, và Luật Xây dựng yêu cầu lắp đặt biển báo an toàn và đèn chiếu sáng tại hàng rào ven đường. Hàng rào bảo mật không chỉ là dấu hiệu ranh giới mà là thiết bị bắt buộc theo pháp luật, nếu không lắp có thể bị lệnh đình chỉ thi công. Cửa ra vào trên hàng rào phải tối thiểu hóa và ngoài cửa ra vào chính phải lắp khóa để ngăn ra vào trái phép.",
        "context": "건설 현장 경계 설정, 무단 출입 방지, 보안 유지, 소음·분진 차단",
        "culturalNote": "한국 건설 현장에서는 보안 울타리 설치가 공사 착공의 첫 단계로 매우 중요하게 여겨집니다. 특히 도심지 현장에서는 보안 울타리를 방음벽과 겸용으로 설치하여 소음 민원을 예방하며, 울타리 외벽에는 공사 현황판, 안전 표어, 비상 연락처를 부착합니다. 울타리에는 야간 조명을 설치하여 무단 침입을 방지하고, 주요 구간에는 CCTV를 설치하여 24시간 감시합니다. 출입문은 주 게이트 1~2개만 운영하고, 비상구는 평소에 잠가두었다가 비상시에만 사용합니다. 태풍이나 강풍에 대비하여 울타리 지주를 견고하게 고정하고, 넘어지지 않도록 정기적으로 점검합니다. 베트남에서는 보안 울타리를 간단한 철망이나 낮은 담장으로 설치하는 경우가 많으나, 한국에서는 2m 이상의 견고한 울타리가 법적 의무이며 미설치 시 공사 중지 명령을 받을 수 있음을 강조해야 합니다. 또한 울타리 훼손이나 무단 제거는 안전 위반으로 처벌받을 수 있습니다. 통역 시 보안 울타리는 공사 종료 시까지 유지해야 하며, 철거는 준공 검사 이후에만 가능하다는 점을 명확히 전달해야 합니다.",
        "commonMistakes": [
            {
                "mistake": "'울타리' 또는 'hàng rào'로만 통역하여 보안 기능 누락",
                "correction": "'보안 울타리' 또는 'hàng rào bảo mật'으로 명시",
                "explanation": "일반 울타리와 구분하기 위해 보안 기능을 명확히 해야 합니다."
            },
            {
                "mistake": "울타리 높이 및 설치 기준 설명 누락",
                "correction": "최소 높이 2m 이상, 견고한 재질, 조명 설치 등 기준 설명",
                "explanation": "법적 기준을 충족해야 하므로 구체적 기준을 설명해야 합니다."
            },
            {
                "mistake": "울타리에 부착하는 표지판 안내 누락",
                "correction": "공사 개요판, 안전 표어, 비상 연락처 부착 의무 명시",
                "explanation": "울타리는 단순 차단물이 아니라 정보 게시 공간이기도 하므로 설명해야 합니다."
            }
        ],
        "examples": [
            {
                "ko": "공사 착공 전에 현장 외곽에 높이 2.5m의 보안 울타리를 설치하고, 울타리에 공사 개요판과 안전 표지판을 부착해 주십시오.",
                "vi": "Trước khi khởi công vui lòng lắp đặt hàng rào bảo mật cao 2,5m ở ngoại vi công trường và dán bảng nội dung thi công cùng biển báo an toàn lên hàng rào.",
                "situation": "formal"
            },
            {
                "ko": "보안 울타리는 공사가 끝날 때까지 유지해야 하며, 훼손되거나 넘어진 부분이 있으면 즉시 보수해야 합니다. 울타리를 임의로 철거하면 안 됩니다.",
                "vi": "Hàng rào bảo mật phải duy trì cho đến khi thi công kết thúc, nếu có chỗ hư hỏng hoặc đổ phải sửa chữa ngay. Không được tự ý tháo dỡ hàng rào.",
                "situation": "onsite"
            },
            {
                "ko": "야, 펜스 쓰러졌는데 세워놔. 바람 불면 또 넘어져.",
                "vi": "Ê, hàng rào đổ rồi dựng lại đi. Gió thổi lại đổ nữa.",
                "situation": "informal"
            }
        ],
        "relatedTerms": [
            "가설 울타리",
            "방음벽",
            "안전 펜스",
            "출입 게이트",
            "현장 경계"
        ]
    },
    {
        "slug": "camera-giam-sat",
        "korean": "감시 카메라",
        "vietnamese": "Camera giám sát",
        "hanja": "監視camera",
        "hanjaReading": "볼 감(監) + 볼 시(視) + camera",
        "pronunciation": "까메라 잠샛",
        "meaningKo": "건설 현장의 주요 구역과 출입구, 위험 구역 등에 설치하여 24시간 영상을 녹화하고 실시간으로 모니터링하는 CCTV 장비로, 'CCTV', '보안 카메라', '안전 감시 카메라'라고도 불립니다. 통역 시 주의할 점은 한국 건설 현장에서는 보안 목적뿐만 아니라 안전사고 예방과 사고 발생 시 원인 분석을 위해 감시 카메라를 필수적으로 설치하며, 주요 게이트, 자재 야적장, 중장비 작업 구역, 고소작업 구역 등에 배치합니다. 베트남어로는 'camera giám sát', 'CCTV', 'camera an ninh'로 표현합니다. 감시 카메라는 설치 목적에 따라 여러 종류가 있는데, 출입 통제용 카메라(camera kiểm soát ra vào), 안전 감시용 카메라(camera giám sát an toàn), 도난 방지용 카메라(camera chống trộm) 등으로 구분됩니다. 한국 개인정보보호법에서는 감시 카메라 설치 시 안내문을 게시하고 촬영된 영상의 보관 기간과 열람 권한을 명시하도록 규정하고 있으며, 일반적으로 30~90일간 녹화 영상을 보관합니다. 통역 시 감시 카메라는 근로자를 감시하기 위한 것이 아니라 안전사고 예방과 현장 보안을 위한 것이며, 사고 발생 시 원인 규명에 중요한 증거 자료가 된다는 점을 명확히 전달해야 합니다.",
        "meaningVi": "Camera giám sát (감시 카메라) là thiết bị CCTV được lắp đặt tại các khu vực chính và cửa ra vào, khu vực nguy hiểm của công trường xây dựng để quay video 24 giờ và giám sát trực tuyến, còn gọi là camera an ninh. Tại Hàn Quốc, camera giám sát được lắp đặt bắt buộc không chỉ vì mục đích bảo mật mà còn để phòng ngừa tai nạn an toàn và phân tích nguyên nhân khi xảy ra tai nạn, được bố trí tại cổng chính, bãi chứa vật tư, khu vực máy móc hạng nặng, khu vực làm việc trên cao. Camera giám sát có nhiều loại tùy theo mục đích lắp đặt: camera kiểm soát ra vào, camera giám sát an toàn, camera chống trộm. Theo Luật Bảo vệ Thông tin Cá nhân Hàn Quốc, khi lắp đặt camera giám sát phải dán thông báo và ghi rõ thời gian lưu trữ video quay được cùng quyền xem, thường lưu trữ video quay được từ 30 đến 90 ngày. Camera giám sát không phải để giám sát người lao động mà để phòng ngừa tai nạn an toàn và bảo mật công trường, khi xảy ra tai nạn sẽ là tài liệu chứng cứ quan trọng để làm rõ nguyên nhân.",
        "context": "건설 현장 보안, 출입 통제, 안전사고 예방, 사고 원인 분석, 도난 방지",
        "culturalNote": "한국 건설 현장에서는 감시 카메라 설치가 매우 보편화되어 있으며, 대형 현장의 경우 수십 대의 카메라를 설치하여 현장 전체를 커버합니다. 카메라 영상은 현장 사무실의 모니터링실에서 실시간으로 확인하며, 보안 요원이나 안전 관리자가 24시간 교대로 감시합니다. 감시 카메라는 고정형과 회전형(PTZ)이 있으며, 주요 게이트와 위험 구역에는 회전형 카메라를 설치하여 넓은 범위를 감시합니다. 야간에도 촬영이 가능하도록 적외선 기능이 있는 카메라를 사용하며, 일부 현장에서는 AI 분석 기능이 있는 스마트 카메라를 도입하여 안전모 미착용, 위험 구역 출입 등을 자동으로 감지하여 경고를 보냅니다. 베트남에서는 감시 카메라가 근로자를 감시하는 부정적 이미지로 인식되는 경우가 있으나, 한국에서는 안전 관리의 필수 도구로 받아들여지며, 사고 발생 시 원인 규명과 책임 소재 파악에 결정적 증거가 된다는 점을 강조해야 합니다. 또한 촬영된 영상은 개인정보보호법에 따라 엄격하게 관리되며, 무단 열람이나 유출 시 법적 처벌을 받습니다. 통역 시 감시 카메라는 근로자를 불신하는 것이 아니라 모두의 안전을 위한 것임을 명확히 전달해야 합니다.",
        "commonMistakes": [
            {
                "mistake": "'카메라' 또는 'camera'로만 통역하여 감시 목적 누락",
                "correction": "'감시 카메라' 또는 'camera giám sát'으로 명시",
                "explanation": "일반 카메라와 구분하기 위해 감시 목적을 명확히 해야 합니다."
            },
            {
                "mistake": "카메라 설치 목적을 근로자 감시로만 설명",
                "correction": "안전사고 예방, 현장 보안, 사고 원인 분석 등 다목적 설명",
                "explanation": "감시 카메라는 부정적 의미가 아니라 안전 관리 도구임을 강조해야 합니다."
            },
            {
                "mistake": "개인정보 보호 규정 설명 누락",
                "correction": "영상 보관 기간, 열람 권한, 유출 금지 등 규정 명시",
                "explanation": "촬영된 영상은 개인정보이므로 보호 규정을 설명해야 합니다."
            }
        ],
        "examples": [
            {
                "ko": "현장 주요 출입구와 자재 야적장, 중장비 작업 구역에 감시 카메라를 설치하고, 카메라 설치 안내문을 게시해 주십시오. 녹화 영상은 60일간 보관됩니다.",
                "vi": "Vui lòng lắp đặt camera giám sát tại cửa ra vào chính, bãi chứa vật tư và khu vực máy móc hạng nặng, đồng thời dán thông báo lắp camera. Video quay được sẽ lưu trữ 60 ngày.",
                "situation": "formal"
            },
            {
                "ko": "감시 카메라는 여러분을 감시하려는 것이 아니라 안전사고를 예방하고 도난을 방지하기 위한 것입니다. 사고가 발생하면 카메라 영상이 원인을 밝히는 중요한 증거가 됩니다.",
                "vi": "Camera giám sát không phải để giám sát các bạn mà để phòng ngừa tai nạn an toàn và ngăn chặn trộm cắp. Khi xảy ra tai nạn, video camera sẽ là chứng cứ quan trọng để làm rõ nguyên nhân.",
                "situation": "onsite"
            },
            {
                "ko": "카메라 있으니까 조심해. 안전모 안 쓰고 다니면 딱 걸려.",
                "vi": "Có camera đấy cẩn thận. Đi không đội mũ là bị phát hiện ngay.",
                "situation": "informal"
            }
        ],
        "relatedTerms": [
            "CCTV",
            "보안 카메라",
            "모니터링",
            "녹화 영상",
            "출입 통제"
        ]
    },
    {
        "slug": "bao-ve-dem",
        "korean": "야간 경비",
        "vietnamese": "Bảo vệ đêm",
        "hanja": "夜間警備",
        "hanjaReading": "밤 야(夜) + 사이 간(間) + 경계할 경(警) + 갖출 비(備)",
        "pronunciation": "바오베 뎀",
        "meaningKo": "건설 현장에서 야간 시간대(일반적으로 오후 6시~익일 오전 6시)에 무단 침입, 도난, 화재 등을 방지하기 위해 보안 요원을 배치하여 순찰하고 감시하는 업무로, '야간 보안', '밤 경비', '당직 근무'라고도 불립니다. 통역 시 주의할 점은 한국 건설 현장에서는 야간 경비가 필수적으로 운영되며, 보안 업체와 계약하여 전문 경비원을 배치하거나 현장 직원이 교대로 당직 근무를 합니다. 베트남어로는 'bảo vệ đêm', 'canh gác ban đêm', 'tuần tra đêm'으로 표현합니다. 야간 경비의 주요 임무는 현장 순찰(tuần tra), 출입 통제(kiểm soát ra vào), 화재 감시(giám sát hỏa hoạn), 이상 상황 대응(ứng phó tình huống bất thường) 등이며, 2시간마다 순찰 일지를 작성하고 보고합니다. 한국 경비업법에서는 건설 현장 경비원의 자격과 교육을 규정하고 있으며, 야간 경비원은 경비 교육을 이수하고 자격증을 소지해야 합니다. 통역 시 야간 경비는 단순히 잠을 자지 않고 현장을 지키는 것이 아니라 정기적인 순찰과 기록이 필수이며, 이상 발견 시 즉시 현장 소장과 경찰에 신고해야 한다는 점을 명확히 전달해야 합니다.",
        "meaningVi": "Bảo vệ đêm (야간 경비) là công việc bố trí nhân viên bảo vệ để tuần tra và giám sát trong thời gian đêm (thường từ 18h đến 6h sáng hôm sau) tại công trường xây dựng nhằm ngăn chặn xâm nhập trái phép, trộm cắp, hỏa hoạn, còn gọi là canh gác ban đêm hoặc trực đêm. Tại Hàn Quốc, bảo vệ đêm được vận hành bắt buộc, ký hợp đồng với công ty bảo vệ để bố trí nhân viên bảo vệ chuyên nghiệp hoặc nhân viên công trường trực đêm thay phiên nhau. Nhiệm vụ chính của bảo vệ đêm là tuần tra công trường, kiểm soát ra vào, giám sát hỏa hoạn, ứng phó tình huống bất thường, cứ 2 tiếng phải viết nhật ký tuần tra và báo cáo. Theo Luật Nghiệp vụ Bảo vệ Hàn Quốc, quy định về trình độ và giáo dục của nhân viên bảo vệ công trường, nhân viên bảo vệ đêm phải hoàn thành khóa đào tạo bảo vệ và có chứng chỉ. Bảo vệ đêm không chỉ đơn thuần là không ngủ mà canh giữ công trường, mà phải tuần tra định kỳ và ghi chép, khi phát hiện bất thường phải báo ngay cho giám đốc công trường và công an.",
        "context": "건설 현장 보안, 도난 방지, 화재 감시, 무단 침입 차단, 비상 대응",
        "culturalNote": "한국 건설 현장에서는 야간 경비가 매우 체계적으로 운영됩니다. 대형 현장의 경우 2~3명의 경비원이 교대로 근무하며, 소형 현장은 1명이 당직 근무를 합니다. 야간 경비원은 현장 전체를 2시간마다 순찰하며, 순찰 지점마다 설치된 NFC 태그나 QR 코드를 스캔하여 순찰 기록을 남깁니다. 이 기록은 스마트폰 앱이나 전용 단말기로 자동 저장되어 경비 실태를 확인할 수 있습니다. 야간 경비원은 손전등, 호루라기, 비상벨, 소화기 등을 휴대하고 순찰하며, 이상 상황 발견 시 즉시 현장 소장에게 전화로 보고하고 필요 시 경찰이나 소방서에 신고합니다. 특히 겨울철에는 동파 방지를 위해 보일러와 수도 배관을 점검하고, 여름철에는 태풍 대비 시설물 고정 상태를 확인합니다. 베트남에서는 야간 경비가 주로 문 앞에 앉아서 출입만 통제하는 경우가 많으나, 한국에서는 정기적인 순찰과 기록이 필수이며, 순찰 기록이 없으면 경비 업무를 제대로 수행하지 않은 것으로 간주되어 계약 해지나 임금 삭감의 사유가 될 수 있음을 강조해야 합니다. 통역 시 야간 경비는 현장 안전과 재산 보호를 위한 중요한 업무이며, 졸음 운전처럼 졸면서 근무하면 안 된다는 점을 명확히 전달해야 합니다.",
        "commonMistakes": [
            {
                "mistake": "'경비' 또는 'bảo vệ'로만 통역하여 야간 시간대 명시 누락",
                "correction": "'야간 경비' 또는 'bảo vệ đêm'으로 시간대 명시",
                "explanation": "주간 경비와 구분하기 위해 야간 시간대를 명확히 해야 합니다."
            },
            {
                "mistake": "순찰 및 기록 의무 설명 누락",
                "correction": "2시간마다 순찰, 순찰 지점 기록, 일지 작성 의무 명시",
                "explanation": "야간 경비는 단순 대기가 아니라 정기 순찰이 필수임을 강조해야 합니다."
            },
            {
                "mistake": "이상 상황 발견 시 대응 절차 미전달",
                "correction": "현장 소장 보고, 경찰/소방서 신고 등 단계별 대응 절차 설명",
                "explanation": "비상 상황에 신속히 대응할 수 있도록 절차를 명확히 해야 합니다."
            }
        ],
        "examples": [
            {
                "ko": "야간 경비원은 2시간마다 현장을 순찰하고 각 순찰 지점의 QR 코드를 스캔하여 순찰 기록을 남겨야 합니다. 이상 상황 발견 시 즉시 소장님께 보고하십시오.",
                "vi": "Nhân viên bảo vệ đêm phải tuần tra công trường cứ 2 tiếng một lần và quét mã QR tại mỗi điểm tuần tra để lưu lại hồ sơ tuần tra. Khi phát hiện tình huống bất thường phải báo cáo ngay cho giám đốc.",
                "situation": "formal"
            },
            {
                "ko": "야간 경비 중에 졸면 안 됩니다. 순찰을 돌면서 화재나 침입자가 없는지 확인하고, 이상이 있으면 경찰에 신고해야 합니다.",
                "vi": "Trong khi bảo vệ đêm không được ngủ gật. Phải đi tuần tra kiểm tra có hỏa hoạn hay kẻ xâm nhập không, nếu có bất thường phải báo công an.",
                "situation": "onsite"
            },
            {
                "ko": "밤에 당직 서는데 2시간마다 한 바퀴 돌아야 해. 그냥 앉아있으면 안 돼.",
                "vi": "Trực đêm phải đi một vòng cứ 2 tiếng. Ngồi im không được đâu.",
                "situation": "informal"
            }
        ],
        "relatedTerms": [
            "순찰",
            "당직 근무",
            "보안 요원",
            "출입 통제",
            "화재 감시"
        ]
    },
    {
        "slug": "giao-duc-bao-mat",
        "korean": "보안 교육",
        "vietnamese": "Giáo dục bảo mật",
        "hanja": "保安敎育",
        "hanjaReading": "지킬 보(保) + 편안할 안(安) + 가르칠 교(敎) + 기를 육(育)",
        "pronunciation": "자오육 바오먿",
        "meaningKo": "건설 현장에 신규 투입되는 모든 인원(근로자, 협력업체 직원, 관리자)에게 현장 출입 규칙, 보안 수칙, 비밀 유지, 사진 촬영 금지 등 현장 보안에 관한 사항을 교육하는 과정으로, '보안 안전 교육', '현장 보안 수칙 교육'이라고도 불립니다. 통역 시 주의할 점은 한국 건설 현장에서는 보안 교육이 안전 교육과 함께 필수적으로 실시되며, 교육을 이수하지 않으면 현장 출입이 불가능합니다. 베트남어로는 'giáo dục bảo mật', 'huấn luyện an ninh', 'đào tạo quy định bảo mật'으로 표현합니다. 보안 교육의 주요 내용은 출입증 관리(quản lý thẻ ra vào), 출입 통제 구역(khu vực hạn chế ra vào), 사진·영상 촬영 금지(cấm chụp ảnh/quay video), 외부인 동행 규칙(quy tắc đi cùng người ngoài), 정보 유출 금지(cấm tiết lộ thông tin), 비상 연락망(mạng liên lạc khẩn cấp) 등이며, 일반적으로 20~30분간 진행됩니다. 한국 산업보안법과 개인정보보호법에서는 현장 보안 교육을 의무화하고 있으며, 특히 국가 중요 시설이나 국방 관련 공사 현장에서는 보안 서약서를 작성해야 합니다. 통역 시 보안 교육은 형식적 절차가 아니라 법적 의무이며, 보안 수칙 위반 시 현장 퇴출이나 법적 처벌을 받을 수 있다는 점을 명확히 전달해야 합니다.",
        "meaningVi": "Giáo dục bảo mật (보안 교육) là khóa học giáo dục về các vấn đề bảo mật công trường như quy định ra vào công trường, quy tắc bảo mật, bảo mật bí mật, cấm chụp ảnh cho tất cả nhân viên mới (công nhân, nhân viên đối tác, quản lý) được đưa vào công trường xây dựng, còn gọi là giáo dục an toàn bảo mật. Tại Hàn Quốc, giáo dục bảo mật được thực hiện bắt buộc cùng với giáo dục an toàn, nếu không hoàn thành khóa học sẽ không được vào công trường. Nội dung chính của giáo dục bảo mật là quản lý thẻ ra vào, khu vực hạn chế ra vào, cấm chụp ảnh/quay video, quy tắc đi cùng người ngoài, cấm tiết lộ thông tin, mạng liên lạc khẩn cấp, thường diễn ra từ 20 đến 30 phút. Theo Luật Bảo mật Công nghiệp và Luật Bảo vệ Thông tin Cá nhân Hàn Quốc, bắt buộc phải có giáo dục bảo mật công trường, đặc biệt tại công trường cơ sở quan trọng quốc gia hoặc liên quan quốc phòng phải viết cam kết bảo mật. Giáo dục bảo mật không phải thủ tục hình thức mà là nghĩa vụ pháp lý, vi phạm quy tắc bảo mật có thể bị đuổi khỏi công trường hoặc xử lý theo pháp luật.",
        "context": "건설 현장 신규 투입, 보안 수칙 전달, 정보 유출 방지, 출입 통제 교육",
        "culturalNote": "한국 건설 현장에서는 보안 교육이 안전 교육만큼 중요하게 여겨지며, 특히 대형 프로젝트나 보안이 중요한 시설(공항, 군사 시설, 발전소 등)의 경우 보안 교육이 더욱 강화됩니다. 보안 교육은 일반적으로 안전 교육과 함께 진행되며, 안전 교육 후반부에 20~30분간 보안 수칙을 설명합니다. 교육 내용에는 출입증 패용 의무, 출입 통제 구역 안내, 사진·영상 촬영 금지 구역 표시, 외부인 발견 시 신고 방법, SNS 게시 금지 사항, 도면이나 자료 유출 금지 등이 포함됩니다. 교육 후에는 보안 서약서에 서명하고, 위반 시 법적 책임을 지겠다는 내용에 동의해야 합니다. 특히 사진 촬영 금지는 매우 엄격하게 적용되어, 허가 없이 현장 사진을 찍거나 SNS에 올리면 즉시 현장에서 퇴출되고 법적 조치를 받을 수 있습니다. 베트남에서는 현장 보안에 대한 인식이 상대적으로 낮아 현장 사진을 자유롭게 찍어 SNS에 올리는 경우가 많으나, 한국에서는 이것이 중대한 보안 위반이며 회사 기밀 유출로 간주되어 형사 처벌까지 받을 수 있음을 강조해야 합니다. 통역 시 보안 교육은 단순한 주의 사항이 아니라 법적 책임이 따르는 서약이며, 위반 시 본인뿐만 아니라 소속 회사까지 책임을 질 수 있다는 점을 명확히 전달해야 합니다.",
        "commonMistakes": [
            {
                "mistake": "'교육' 또는 'giáo dục'으로만 통역하여 보안 내용 누락",
                "correction": "'보안 교육' 또는 'giáo dục bảo mật'으로 명시",
                "explanation": "안전 교육과 구분하기 위해 보안 내용을 명확히 해야 합니다."
            },
            {
                "mistake": "사진 촬영 금지 및 SNS 게시 금지 경고 미전달",
                "correction": "허가 없는 촬영 금지, SNS 게시 금지, 위반 시 퇴출 및 처벌 명시",
                "explanation": "사진 촬영 금지는 가장 빈번히 위반되는 항목이므로 강조해야 합니다."
            },
            {
                "mistake": "보안 서약서 서명의 법적 의미 설명 누락",
                "correction": "서약서는 법적 효력이 있으며 위반 시 민·형사 책임 발생 명시",
                "explanation": "서약서가 단순 형식이 아니라 법적 책임을 지는 문서임을 강조해야 합니다."
            }
        ],
        "examples": [
            {
                "ko": "현장 투입 전에 보안 교육을 필수로 이수하셔야 합니다. 교육에서는 출입 통제, 사진 촬영 금지, 정보 유출 금지 등을 안내하며, 교육 후 보안 서약서에 서명하셔야 합니다.",
                "vi": "Trước khi vào làm việc tại công trường bắt buộc phải hoàn thành giáo dục bảo mật. Trong khóa học sẽ hướng dẫn về kiểm soát ra vào, cấm chụp ảnh, cấm tiết lộ thông tin, sau đó phải ký cam kết bảo mật.",
                "situation": "formal"
            },
            {
                "ko": "현장에서 사진을 찍거나 SNS에 올리는 것은 절대 금지입니다. 적발되면 즉시 현장에서 퇴출되고 법적 조치를 받을 수 있습니다.",
                "vi": "Tại công trường tuyệt đối cấm chụp ảnh hoặc đăng lên mạng xã hội. Nếu bị phát hiện sẽ bị đuổi khỏi công trường ngay và có thể bị xử lý theo pháp luật.",
                "situation": "onsite"
            },
            {
                "ko": "야, 여기서 사진 찍지 마. 걸리면 너 잘린다.",
                "vi": "Ê, đừng chụp ảnh ở đây. Bị phát hiện là bị sa thải đấy.",
                "situation": "informal"
            }
        ],
        "relatedTerms": [
            "보안 서약서",
            "출입 통제",
            "촬영 금지",
            "정보 유출 방지",
            "안전 교육"
        ]
    },
    {
        "slug": "bien-nhan-dien-cong-truong",
        "korean": "현장 식별 표지",
        "vietnamese": "Biển nhận diện công trường",
        "hanja": "現場識別標識",
        "hanjaReading": "나타날 현(現) + 터 장(場) + 알 식(識) + 나눌 별(別) + 표할 표(標) + 알 식(識)",
        "pronunciation": "비엔 년지엔 꽁쯩",
        "meaningKo": "건설 현장의 입구나 주요 위치에 설치하여 공사명, 발주처, 시공사, 공사 기간, 현장 소장, 안전 관리자, 비상 연락처 등을 표시하는 대형 안내판으로, '현장 게시판', '공사 표지판', '현장 안내판'이라고도 불립니다. 통역 시 주의할 점은 한국 건설 현장에서는 현장 식별 표지 설치가 법적 의무이며, 표지판의 크기, 내용, 설치 위치가 건설기술진흥법 시행규칙에 규정되어 있습니다. 베트남어로는 'biển nhận diện công trường', 'bảng thông tin công trình', 'biển công trình'으로 표현합니다. 현장 식별 표지에는 필수 기재 사항이 있는데, 공사명(tên công trình), 발주자(chủ đầu tư), 시공사(nhà thầu thi công), 감리단(giám sát), 공사 기간(thời gian thi công), 연락처(số điện thoại liên lạc), 안전 관리자(người quản lý an toàn) 등을 명시해야 합니다. 대형 현장의 경우 표지판 크기가 가로 5m, 세로 3m 이상이며, 야간에도 식별 가능하도록 조명을 설치합니다. 한국 건축법과 건설기술진흥법에서는 현장 식별 표지 미설치 시 과태료를 부과하며, 표지판 내용이 부정확하면 시정 명령을 받습니다. 통역 시 현장 식별 표지는 단순한 안내판이 아니라 현장의 공식 신분증이며, 민원이나 사고 발생 시 책임 소재를 명확히 하는 법적 문서임을 명확히 전달해야 합니다.",
        "meaningVi": "Biển nhận diện công trường (현장 식별 표지) là bảng hướng dẫn cỡ lớn được lắp đặt tại cổng vào hoặc vị trí chính của công trường xây dựng để ghi tên công trình, chủ đầu tư, nhà thầu, thời gian thi công, giám đốc công trường, người quản lý an toàn, số điện thoại khẩn cấp, còn gọi là bảng thông tin công trình. Tại Hàn Quốc, lắp đặt biển nhận diện công trường là nghĩa vụ pháp lý, kích thước, nội dung, vị trí lắp đặt được quy định trong Quy tắc thi hành Luật Xúc tiến Công nghệ Xây dựng. Trên biển nhận diện công trường có các mục bắt buộc phải ghi: tên công trình, chủ đầu tư, nhà thầu thi công, giám sát, thời gian thi công, số điện thoại liên lạc, người quản lý an toàn. Công trường lớn có biển rộng từ 5m, cao từ 3m trở lên, và lắp đèn chiếu sáng để nhận diện được cả ban đêm. Theo Luật Xây dựng và Luật Xúc tiến Công nghệ Xây dựng Hàn Quốc, nếu không lắp biển nhận diện công trường sẽ bị phạt tiền, nội dung trên biển không chính xác sẽ nhận lệnh sửa chữa. Biển nhận diện công trường không chỉ là bảng hướng dẫn đơn thuần mà là chứng minh thư chính thức của công trường, là văn bản pháp lý làm rõ trách nhiệm khi có khiếu nại hoặc tai nạn.",
        "context": "건설 현장 정보 제공, 법적 의무 사항, 민원 대응, 책임 소재 명시",
        "culturalNote": "한국 건설 현장에서는 현장 식별 표지가 현장의 얼굴이자 공식 신분증으로 여겨지며, 표지판 디자인과 내용에 많은 신경을 씁니다. 대형 건설사의 경우 회사 CI(Corporate Identity)를 적용한 통일된 디자인의 표지판을 사용하며, 표지판에 회사 로고와 슬로건을 함께 표시하여 브랜드 이미지를 강화합니다. 표지판은 일반적으로 현장 정문 바로 옆 또는 보안 울타리에 부착하며, 도로에서 잘 보이는 위치에 설치합니다. 표지판에는 공사 개요 외에도 안전 표어('안전 제일', '무재해 현장'), 현장 목표('품질 최우선', '준공 기한 준수'), 환경 관리 사항('소음 최소화', '분진 저감') 등을 함께 표시합니다. 일부 현장에서는 디지털 전광판을 설치하여 공사 진행률, 안전 무재해 일수, 날씨 정보 등을 실시간으로 표시하기도 합니다. 베트남에서는 현장 표지판이 간단한 플래카드 정도로 설치되는 경우가 많으나, 한국에서는 법적 필수 사항이 모두 포함된 정식 표지판이 필수이며, 내용이 누락되거나 부정확하면 과태료를 부과받을 수 있음을 강조해야 합니다. 또한 표지판 정보는 정기적으로 업데이트해야 하며, 공사 기간 변경이나 담당자 교체 시 표지판도 즉시 수정해야 합니다. 통역 시 현장 식별 표지는 현장의 공식 정보이므로 항상 정확하고 최신 상태를 유지해야 하며, 허위 정보 기재 시 법적 책임을 질 수 있다는 점을 명확히 전달해야 합니다.",
        "commonMistakes": [
            {
                "mistake": "'표지판' 또는 'biển báo'로만 통역하여 식별 기능 누락",
                "correction": "'현장 식별 표지' 또는 'biển nhận diện công trường'으로 명시",
                "explanation": "일반 표지판과 구분하기 위해 현장 식별 기능을 명확히 해야 합니다."
            },
            {
                "mistake": "필수 기재 사항 설명 누락",
                "correction": "공사명, 발주처, 시공사, 기간, 연락처 등 필수 항목 열거",
                "explanation": "법적 의무 사항이므로 필수 기재 항목을 명확히 해야 합니다."
            },
            {
                "mistake": "미설치 또는 허위 기재 시 처벌 경고 미전달",
                "correction": "미설치 시 과태료, 허위 기재 시 법적 책임 명시",
                "explanation": "법적 의무 사항임을 강조하기 위해 처벌 내용을 명시해야 합니다."
            }
        ],
        "examples": [
            {
                "ko": "현장 정문에 가로 5m, 세로 3m 크기의 현장 식별 표지를 설치하고, 공사명, 발주처, 시공사, 공사 기간, 현장 소장 이름, 비상 연락처를 명시해 주십시오.",
                "vi": "Vui lòng lắp đặt biển nhận diện công trường kích thước rộng 5m, cao 3m tại cổng chính, ghi rõ tên công trình, chủ đầu tư, nhà thầu, thời gian thi công, tên giám đốc công trường, số điện thoại khẩn cấp.",
                "situation": "formal"
            },
            {
                "ko": "현장 식별 표지는 공사 기간 내내 유지해야 하며, 담당자가 바뀌거나 공사 기간이 연장되면 표지판 내용도 즉시 수정해야 합니다.",
                "vi": "Biển nhận diện công trường phải duy trì trong suốt thời gian thi công, nếu thay người phụ trách hoặc gia hạn thời gian thi công phải sửa nội dung biển ngay.",
                "situation": "onsite"
            },
            {
                "ko": "야, 현판 달았어? 안 달면 과태료 나와.",
                "vi": "Ê, treo biển chưa? Không treo là bị phạt đấy.",
                "situation": "informal"
            }
        ],
        "relatedTerms": [
            "공사 개요판",
            "안내 표지판",
            "현장 게시판",
            "비상 연락망",
            "공사 정보"
        ]
    },
    {
        "slug": "danh-dau-khu-vuc-nguy-hiem",
        "korean": "위험 구역 표시",
        "vietnamese": "Đánh dấu khu vực nguy hiểm",
        "hanja": "危險區域標示",
        "hanjaReading": "위태할 위(危) + 험할 험(險) + 구역 구(區) + 지경 역(域) + 표할 표(標) + 보일 시(示)",
        "pronunciation": "다인저우 쿠벽 응우이힘",
        "meaningKo": "건설 현장 내에서 낙하물, 굴착, 고소작업, 중장비 운행 등으로 인해 위험이 예상되는 구역을 눈에 띄는 색상의 표지판, 바리케이드, 안전 테이프 등으로 명확하게 표시하여 근로자와 방문자가 위험을 인지하고 출입을 통제하는 조치로, '위험 구역 설정', '출입 금지 구역 표시'라고도 불립니다. 통역 시 주의할 점은 한국 건설 현장에서는 위험 구역 표시가 법적 의무이며, 표시 방법과 색상이 산업안전보건 기준에 규칙에 규정되어 있습니다(노란색·검은색 줄무늬 또는 빨간색). 베트남어로는 'đánh dấu khu vực nguy hiểm', 'phân vùng nguy hiểm', 'cảnh báo khu vực nguy hiểm'으로 표현합니다. 위험 구역 표시는 종류에 따라 여러 방식이 있는데, 낙하물 위험 구역(khu vực rơi vật), 굴착 위험 구역(khu vực đào đất nguy hiểm), 고소작업 위험 구역(khu vực làm việc trên cao), 중장비 운행 구역(khu vực máy móc hạng nặng hoạt động), 화재 위험 구역(khu vực nguy cơ hỏa hoạn) 등으로 구분되며 각각 해당하는 표지판과 색상을 사용합니다. 한국 산업안전보건법에서는 위험 구역 미표시 시 사업주에게 과태료를 부과하며, 위험 구역 표시 무시하고 출입한 근로자에게도 징계나 처벌을 내릴 수 있습니다. 통역 시 위험 구역 표시는 단순한 경고가 아니라 법적 출입 금지 명령이며, 무시하면 안전사고로 이어질 수 있고 사고 발생 시 근로자 본인의 과실로 간주되어 산재 보상이 제한될 수 있다는 점을 명확히 전달해야 합니다.",
        "meaningVi": "Đánh dấu khu vực nguy hiểm (위험 구역 표시) là biện pháp đánh dấu rõ ràng các khu vực có nguy cơ nguy hiểm do rơi vật, đào đất, làm việc trên cao, máy móc hạng nặng hoạt động trong công trường xây dựng bằng biển báo màu sắc nổi bật, rào chắn, băng keo an toàn để công nhân và khách nhận biết nguy hiểm và kiểm soát ra vào, còn gọi là thiết lập khu vực nguy hiểm, đánh dấu khu vực cấm vào. Tại Hàn Quốc, đánh dấu khu vực nguy hiểm là nghĩa vụ pháp lý, phương pháp đánh dấu và màu sắc được quy định trong Quy tắc Tiêu chuẩn An toàn lao động Công nghiệp (sọc vàng đen hoặc màu đỏ). Đánh dấu khu vực nguy hiểm có nhiều cách tùy theo loại: khu vực rơi vật, khu vực đào đất nguy hiểm, khu vực làm việc trên cao, khu vực máy móc hạng nặng hoạt động, khu vực nguy cơ hỏa hoạn, mỗi loại dùng biển báo và màu sắc tương ứng. Theo Luật An toàn lao động Công nghiệp Hàn Quốc, nếu không đánh dấu khu vực nguy hiểm sẽ phạt tiền chủ doanh nghiệp, công nhân vào khu vực nguy hiểm mà bỏ qua đánh dấu cũng có thể bị kỷ luật hoặc xử phạt. Đánh dấu khu vực nguy hiểm không chỉ là cảnh báo đơn thuần mà là lệnh cấm vào theo pháp luật, nếu bỏ qua có thể dẫn đến tai nạn an toàn và khi xảy ra tai nạn sẽ bị coi là lỗi của công nhân và có thể hạn chế bồi thường tai nạn lao động.",
        "context": "건설 현장 안전 관리, 출입 통제, 사고 예방, 법적 책임 명시",
        "culturalNote": "한국 건설 현장에서는 위험 구역 표시가 매우 체계적이고 엄격하게 이루어집니다. 위험 구역은 작업 시작 전 안전 담당자가 위험성 평가를 실시하여 선정하고, 선정된 구역에는 즉시 표지판과 바리케이드를 설치합니다. 표지판에는 위험 내용을 명확히 표시하는데, '낙하물 위험', '굴착 구역 출입금지', '고소작업 중', '중장비 운행 구역' 등 구체적인 문구를 사용합니다. 바리케이드는 노란색과 검은색 줄무늬 또는 빨간색과 흰색 줄무늬를 사용하여 원거리에서도 식별 가능하도록 하며, 야간에는 야광 테이프나 경고등을 설치하여 가시성을 높입니다. 특히 위험도가 높은 구역(깊이 2m 이상 굴착, 높이 2m 이상 고소작업)은 이중 바리케이드를 설치하고 출입구에 안전 요원을 배치하여 출입을 통제합니다. 베트남에서는 위험 구역 표시가 간단한 줄이나 표지판 정도로 이루어지고 작업상 불편하면 임의로 치우는 경우가 많으나, 한국에서는 위험 구역 표시 무시하고 출입하는 것이 중대한 안전 위반이며, 사고 발생 시 근로자 본인의 과실로 간주되어 산재 보상이 감액되거나 거부될 수 있음을 강조해야 합니다. 또한 위험 구역 표시를 임의로 이동하거나 제거하면 안전 담당자의 승인 없이는 불가능하며, 위반 시 징계 처분을 받습니다. 통역 시 위험 구역 표시는 생명을 보호하는 마지막 경고선이므로 절대로 무시하거나 넘어서는 안 된다는 점을 명확히 전달해야 합니다.",
        "commonMistakes": [
            {
                "mistake": "'위험 표시' 또는 'cảnh báo nguy hiểm'으로만 통역하여 구역 설정 의미 누락",
                "correction": "'위험 구역 표시' 또는 'đánh dấu khu vực nguy hiểm'으로 명시",
                "explanation": "단순 경고가 아니라 구역 출입 통제임을 명확히 해야 합니다."
            },
            {
                "mistake": "위험 구역 종류별 표시 방법 설명 누락",
                "correction": "낙하물/굴착/고소/중장비 등 유형별 표지판과 색상 구분",
                "explanation": "위험 유형에 따라 표시 방법이 다르므로 구분해서 설명해야 합니다."
            },
            {
                "mistake": "무단 출입 시 법적 책임 및 산재 보상 제한 경고 미전달",
                "correction": "무단 출입은 안전 위반, 사고 시 근로자 과실로 간주, 산재 보상 제한 명시",
                "explanation": "위험 구역 표시 무시의 심각성을 강조하기 위해 법적 책임을 명시해야 합니다."
            }
        ],
        "examples": [
            {
                "ko": "굴착 작업 구역 주변 2m 이내에 노란색 바리케이드를 설치하고 '출입금지 - 굴착 위험' 표지판을 부착해 주십시오. 야간 작업 시에는 경고등도 함께 설치하십시오.",
                "vi": "Vui lòng lắp rào chắn màu vàng trong phạm vi 2m xung quanh khu vực đào đất và dán biển 'Cấm vào - Nguy hiểm đào đất'. Khi làm việc ban đêm phải lắp thêm đèn cảnh báo.",
                "situation": "formal"
            },
            {
                "ko": "위험 구역 표시를 무시하고 출입하면 절대 안 됩니다. 사고가 발생하면 본인의 과실로 간주되어 산재 보상을 받지 못할 수 있습니다.",
                "vi": "Tuyệt đối không được bỏ qua đánh dấu khu vực nguy hiểm mà vào. Nếu xảy ra tai nạn sẽ bị coi là lỗi của bản thân và có thể không được bồi thường tai nạn lao động.",
                "situation": "onsite"
            },
            {
                "ko": "야, 빨간 줄 넘지 마. 거기 들어가면 큰일 나.",
                "vi": "Ê, đừng vượt qua sọc đỏ. Vào đó là gặp chuyện to.",
                "situation": "informal"
            }
        ],
        "relatedTerms": [
            "바리케이드",
            "안전 표지판",
            "출입 금지",
            "위험 구역",
            "안전 테이프"
        ]
    },
    {
        "slug": "so-ghi-chep-ra-vao",
        "korean": "출입 기록 대장",
        "vietnamese": "Sổ ghi chép ra vào",
        "hanja": "出入記錄臺帳",
        "hanjaReading": "날 출(出) + 들 입(入) + 기록할 기(記) + 기록할 록(錄) + 대 대(臺) + 장부 장(帳)",
        "pronunciation": "소 기쩹 자바오",
        "meaningKo": "건설 현장에 출입하는 모든 인원(근로자, 방문자, 차량)의 출입 일시, 성명, 소속, 출입 목적 등을 시간순으로 기록하는 장부로, '출입자 명부', '출입 관리 대장', '방문자 기록부'라고도 불립니다. 통역 시 주의할 점은 한국 건설 현장에서는 출입 기록 대장 작성이 법적 의무이며, 근로자는 매일 출퇴근 시 서명하고, 방문자는 출입 시마다 기록을 남겨야 합니다. 베트남어로는 'sổ ghi chép ra vào', 'sổ kiểm soát ra vào', 'sổ quản lý người vào ra'로 표현합니다. 출입 기록 대장은 용도에 따라 여러 종류가 있는데, 근로자용(sổ công nhân), 방문자용(sổ khách), 차량용(sổ xe), 자재용(sổ vật tư)으로 구분되며 각각 별도로 관리합니다. 대장에는 필수 기재 사항으로 출입 일시(ngày giờ ra vào), 성명(họ tên), 소속/회사(đơn vị/công ty), 출입 목적(mục đích), 동행자(người đi cùng), 서명(chữ ký) 등을 기록합니다. 한국 산업안전보건법과 건설기술진흥법에서는 현장 출입자 기록 보관을 의무화하고 있으며, 일반적으로 공사 종료 후 3~5년간 보관해야 합니다. 출입 기록은 재해 발생 시 현장 인원 파악, 노무비 정산, 보안 사고 조사 등에 중요한 증빙 자료가 됩니다. 통역 시 출입 기록 대장은 단순한 행정 서류가 아니라 법적 증빙 자료이며, 허위 기재나 대리 서명 시 처벌받을 수 있다는 점을 명확히 전달해야 합니다.",
        "meaningVi": "Sổ ghi chép ra vào (출입 기록 대장) là sổ ghi chép theo thứ tự thời gian ngày giờ ra vào, họ tên, đơn vị, mục đích ra vào của tất cả nhân viên (công nhân, khách, phương tiện) vào công trường xây dựng, còn gọi là danh sách người ra vào, sổ quản lý ra vào. Tại Hàn Quốc, lập sổ ghi chép ra vào là nghĩa vụ pháp lý, công nhân phải ký tên mỗi ngày khi ra vào làm việc, khách phải để lại ghi chép mỗi lần vào. Sổ ghi chép ra vào có nhiều loại tùy theo mục đích: sổ công nhân, sổ khách, sổ xe, sổ vật tư, mỗi loại quản lý riêng. Trên sổ phải ghi các mục bắt buộc: ngày giờ ra vào, họ tên, đơn vị/công ty, mục đích, người đi cùng, chữ ký. Theo Luật An toàn lao động Công nghiệp và Luật Xúc tiến Công nghệ Xây dựng Hàn Quốc, bắt buộc phải lưu trữ sổ ghi chép người ra vào công trường, thường phải lưu từ 3 đến 5 năm sau khi thi công kết thúc. Sổ ghi chép ra vào là tài liệu chứng minh quan trọng khi xảy ra tai nạn để xác định nhân sự tại hiện trường, quyết toán tiền công, điều tra sự cố bảo mật. Sổ ghi chép ra vào không chỉ là giấy tờ hành chính đơn thuần mà là tài liệu chứng minh pháp lý, ghi chép sai hoặc ký thay có thể bị xử phạt.",
        "context": "건설 현장 출입 관리, 인원 파악, 보안 관리, 노무비 정산, 재해 조사",
        "culturalNote": "한국 건설 현장에서는 출입 기록 대장 관리가 매우 체계적으로 이루어집니다. 대형 현장의 경우 전자 출입 시스템(RFID, 바코드, 안면 인식)을 도입하여 출입증을 단말기에 인식시키면 자동으로 출입 기록이 저장됩니다. 소형 현장은 수기 대장을 사용하며, 출입구에 비치된 대장에 매일 서명합니다. 근로자는 출근 시와 퇴근 시 각각 서명하며, 이 기록은 근무 시간 확인과 노무비 정산의 근거가 됩니다. 방문자는 출입 시 신분증을 제시하고 대장에 이름, 소속, 방문 목적, 연락처를 기재한 후 서명하며, 퇴장 시에도 퇴장 시간을 기록합니다. 차량은 차량 번호, 운전자 이름, 적재 물품, 출입 목적을 기재합니다. 출입 기록은 보안 목적뿐만 아니라 재해 발생 시 현장 인원을 신속하게 파악하여 구조 활동에 활용되므로 정확성이 매우 중요합니다. 베트남에서는 출입 기록을 형식적으로 작성하거나 누락하는 경우가 많으나, 한국에서는 출입 기록 미작성 시 현장 출입이 거부되고, 허위 기재나 대리 서명 시 현장 퇴출이나 계약 해지의 사유가 될 수 있음을 강조해야 합니다. 또한 출입 기록은 개인정보이므로 외부 유출이 금지되며, 무단 열람이나 복사 시 개인정보보호법 위반으로 처벌받습니다. 통역 시 출입 기록 대장은 단순한 서명이 아니라 법적 책임을 지는 문서이며, 정확하고 성실하게 작성해야 한다는 점을 명확히 전달해야 합니다.",
        "commonMistakes": [
            {
                "mistake": "'출입 명부' 또는 'danh sách ra vào'로만 통역하여 기록 관리 의미 누락",
                "correction": "'출입 기록 대장' 또는 'sổ ghi chép ra vào'로 명시",
                "explanation": "단순 명단이 아니라 시간순 기록 장부임을 명확히 해야 합니다."
            },
            {
                "mistake": "필수 기재 항목 설명 누락",
                "correction": "출입 일시, 성명, 소속, 목적, 서명 등 필수 항목 열거",
                "explanation": "법적 효력을 위해 필수 기재 항목을 명확히 해야 합니다."
            },
            {
                "mistake": "대리 서명 및 허위 기재 금지 경고 미전달",
                "correction": "본인만 서명 가능, 대리 서명 및 허위 기재 시 퇴출 및 처벌 명시",
                "explanation": "출입 기록의 정확성을 강조하기 위해 금지 사항을 명시해야 합니다."
            }
        ],
        "examples": [
            {
                "ko": "출근 시와 퇴근 시에 반드시 출입 기록 대장에 본인이 직접 서명하셔야 합니다. 대리 서명은 절대 금지되며, 적발 시 현장에서 퇴출됩니다.",
                "vi": "Khi đến và khi về bắt buộc phải tự tay ký tên vào sổ ghi chép ra vào. Tuyệt đối cấm ký thay, nếu bị phát hiện sẽ bị đuổi khỏi công trường.",
                "situation": "formal"
            },
            {
                "ko": "방문자는 출입 기록 대장에 이름, 소속, 방문 목적, 연락처를 기재하고 서명하신 후 임시 출입증을 받으시면 됩니다. 퇴장 시에도 퇴장 시간을 기록해 주십시오.",
                "vi": "Khách vui lòng ghi họ tên, đơn vị, mục đích thăm, số điện thoại vào sổ ghi chép ra vào và ký tên, sau đó nhận thẻ ra vào tạm thời. Khi ra về cũng vui lòng ghi giờ ra.",
                "situation": "onsite"
            },
            {
                "ko": "야, 출근부 써. 안 쓰면 일당 못 받아.",
                "vi": "Ê, ký sổ ra vào đi. Không ký là không nhận lương đâu.",
                "situation": "informal"
            }
        ],
        "relatedTerms": [
            "출입증",
            "출퇴근 기록",
            "방문자 대장",
            "근태 관리",
            "노무비 정산"
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

# 기존 JSON 파일 읽기
with open(file_path, "r", encoding="utf-8") as f:
    existing_data = json.load(f)

# 새 용어 추가
existing_data.extend(new_terms)

# 파일 저장
with open(file_path, "w", encoding="utf-8") as f:
    json.dump(existing_data, f, ensure_ascii=False, indent=2)

print(f"✅ {len(new_terms)}개 용어 추가 완료")
print(f"📁 파일: {file_path}")
print(f"📊 총 용어 수: {len(existing_data)}개")
