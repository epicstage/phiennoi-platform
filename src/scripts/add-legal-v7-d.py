#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""출입국관리법 심화 용어 추가 스크립트 (v7-d)"""

import json
import os

def load_existing_terms():
    """기존 법률 용어 데이터 로드"""
    file_path = os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', 'data', 'terms', 'legal.json')
    with open(file_path, 'r', encoding='utf-8') as f:
        data = json.load(f)
    return data, file_path

def create_legal_terms():
    """출입국관리법 심화 용어 10개 생성"""
    terms = [
        {
            "id": "legal-immigration-301",
            "slug": "luu-tru-bat-hop-phap",
            "korean": "불법체류",
            "vietnamese": "Lưu trú bất hợp pháp",
            "hanja": "不法滯留",
            "hanjaReading": "不(아닐 불) + 法(법 법) + 滯(머무를 체) + 留(머무를 류)",
            "pronunciation": "불법체류",
            "meaningKo": "외국인이 허가된 체류기간을 초과하거나 체류자격 없이 한국에 머무르는 것을 의미합니다. 통역 시 '불법'이라는 표현이 베트남어에서 매우 강한 범죄적 뉘앙스를 가지므로, 맥락에 따라 'quá hạn lưu trú'(체류기간 초과)와 구분하여 번역해야 합니다. 행정처분과 형사처벌을 구분하여 설명하는 것이 중요하며, 자진출국과 강제퇴거의 차이를 명확히 전달해야 합니다.",
            "meaningVi": "Việc người nước ngoài lưu trú tại Hàn Quốc quá thời hạn được phép hoặc không có tư cách lưu trú hợp pháp. Có thể bị xử phạt hành chính hoặc bị truy cứu trách nhiệm hình sự tùy theo mức độ vi phạm.",
            "context": "출입국관리, 외국인 단속, 체류자격 심사 상황에서 사용",
            "culturalNote": "한국에서는 '불법체류자'를 단속 대상으로 엄격히 관리하지만, 베트남에서는 이웃 국가와의 국경 관리가 상대적으로 느슨한 편입니다. 한국의 출입국관리법 위반에 대한 처벌 수위(최대 3년 이하 징역, 입국금지 등)를 정확히 전달하여 오해가 없도록 해야 합니다. 또한 자진출국 시 불이익 감면 제도에 대해서도 설명이 필요합니다.",
            "commonMistakes": [
                {
                    "mistake": "모든 체류기간 초과를 'bất hợp pháp'로 번역",
                    "correction": "경미한 초과는 'quá hạn', 의도적/장기는 'bất hợp pháp'로 구분",
                    "explanation": "베트남어에서 'bất hợp pháp'은 심각한 범죄를 의미하므로 과잉 번역 주의"
                },
                {
                    "mistake": "'불법체류자'를 'người nhập cư trái phép'로 번역",
                    "correction": "'người lưu trú bất hợp pháp' 또는 'người quá hạn lưu trú'",
                    "explanation": "'nhập cư'는 이민을 의미하므로 일시 체류와 혼동됨"
                },
                {
                    "mistake": "행정처분과 형사처벌을 구분하지 않고 통역",
                    "correction": "'xử phạt hành chính'(과태료)와 'truy cứu hình sự'(형사처벌) 명확히 구분",
                    "explanation": "법적 결과가 완전히 다르므로 정확한 구분 필수"
                }
            ],
            "examples": [
                {
                    "ko": "비자 만료 후 6개월 이상 불법체류한 경우 강제퇴거 대상이 됩니다.",
                    "vi": "Trường hợp lưu trú bất hợp pháp trên 6 tháng sau khi visa hết hạn sẽ là đối tượng bị trục xuất bắt buộc.",
                    "situation": "formal"
                },
                {
                    "ko": "불법체류자는 자진출국하면 입국금지 기간이 단축될 수 있습니다.",
                    "vi": "Người lưu trú bất hợp pháp nếu tự nguyện xuất cảnh có thể được rút ngắn thời gian cấm nhập cảnh.",
                    "situation": "formal"
                },
                {
                    "ko": "현장에서 불법체류자로 적발되면 즉시 보호조치됩니다.",
                    "vi": "Nếu bị phát hiện là người lưu trú bất hợp pháp tại hiện trường sẽ bị áp dụng biện pháp bảo vệ ngay lập tức.",
                    "situation": "onsite"
                }
            ],
            "relatedTerms": ["강제퇴거", "출국명령", "보호", "자진출국"]
        },
        {
            "id": "legal-immigration-302",
            "slug": "truc-xuat-bat-buoc",
            "korean": "강제퇴거",
            "vietnamese": "Trục xuất bắt buộc",
            "hanja": "強制退去",
            "hanjaReading": "強(강할 강) + 制(제도 제) + 退(물러날 퇴) + 去(갈 거)",
            "pronunciation": "강제퇴거",
            "meaningKo": "출입국관리법 위반 외국인을 강제로 한국 밖으로 내보내는 행정처분입니다. 통역 시 'trục xuất'(추방)과 'trục xuất bắt buộc'(강제퇴거)의 차이를 명확히 해야 하며, 절차적 권리(이의신청, 변호인 조력)를 정확히 전달해야 합니다. 강제퇴거 사유, 보호 기간, 출국 후 입국금지 기간 등 구체적 정보를 누락 없이 통역하는 것이 중요합니다.",
            "meaningVi": "Biện pháp hành chính cưỡng chế đưa người nước ngoài vi phạm Luật xuất nhập cảnh ra khỏi lãnh thổ Hàn Quốc. Sau khi bị trục xuất bắt buộc, người đó sẽ bị cấm nhập cảnh trong một thời gian nhất định (1~10 năm tùy mức độ vi phạm).",
            "context": "출입국관리소, 외국인보호소, 법원 행정소송 상황에서 사용",
            "culturalNote": "한국의 강제퇴거 절차는 법적 권리 보장이 명확한 반면, 베트남에서는 행정절차가 상대적으로 간소합니다. 한국에서는 강제퇴거 명령에 대해 이의신청(7일 이내), 행정소송 제기가 가능하며, 변호인의 조력을 받을 권리가 있음을 반드시 고지해야 합니다. 베트남 통역사는 이러한 절차적 권리를 빠짐없이 전달해야 합니다.",
            "commonMistakes": [
                {
                    "mistake": "'강제퇴거'를 'bị đuổi về nước'(쫓겨남)로 번역",
                    "correction": "'trục xuất bắt buộc' 사용",
                    "explanation": "'đuổi'는 비격식적이고 모욕적 뉘앙스가 있음"
                },
                {
                    "mistake": "출국명령과 강제퇴거를 동일하게 번역",
                    "correction": "출국명령은 'lệnh xuất cảnh', 강제퇴거는 'trục xuất bắt buộc'",
                    "explanation": "법적 효력과 절차가 완전히 다름"
                },
                {
                    "mistake": "이의신청 기한을 통역하지 않음",
                    "correction": "'trong vòng 7 ngày'(7일 이내) 명확히 전달",
                    "explanation": "기한 경과 시 권리 상실되므로 정확한 통역 필수"
                }
            ],
            "examples": [
                {
                    "ko": "불법취업으로 강제퇴거 명령을 받으면 5년간 입국이 금지됩니다.",
                    "vi": "Nếu nhận lệnh trục xuất bắt buộc vì làm việc bất hợp pháp sẽ bị cấm nhập cảnh trong 5 năm.",
                    "situation": "formal"
                },
                {
                    "ko": "강제퇴거 명령에 불복하시면 7일 이내에 이의신청을 하셔야 합니다.",
                    "vi": "Nếu không đồng ý với lệnh trục xuất bắt buộc, anh/chị phải nộp đơn khiếu nại trong vòng 7 ngày.",
                    "situation": "formal"
                },
                {
                    "ko": "강제퇴거 집행까지 보호시설에 수용될 수 있습니다.",
                    "vi": "Có thể bị giam giữ tại cơ sở bảo vệ cho đến khi thi hành trục xuất bắt buộc.",
                    "situation": "onsite"
                }
            ],
            "relatedTerms": ["보호", "출국명령", "이의신청", "입국금지"]
        },
        {
            "id": "legal-immigration-303",
            "slug": "cam-xuat-canh",
            "korean": "출국금지",
            "vietnamese": "Cấm xuất cảnh",
            "hanja": "出國禁止",
            "hanjaReading": "出(날 출) + 國(나라 국) + 禁(금할 금) + 止(그칠 지)",
            "pronunciation": "출국금지",
            "meaningKo": "형사사건 수사, 재판 진행, 또는 국가안보를 위해 법무부장관이 특정인의 출국을 금지하는 조치입니다. 통역 시 출국금지의 법적 근거(형사소송법, 출입국관리법 등), 기간, 해제 조건을 정확히 전달해야 하며, 여권 압류와는 다른 개념임을 명확히 해야 합니다. 출국금지 통보 방식과 이의제기 절차도 중요한 통역 포인트입니다.",
            "meaningVi": "Biện pháp do Bộ trưởng Bộ Tư pháp ra quyết định cấm một người cụ thể xuất cảnh khỏi Hàn Quốc, nhằm phục vụ điều tra hình sự, xét xử hoặc vì lý do an ninh quốc gia. Thời hạn cấm xuất cảnh thường là 6 tháng và có thể gia hạn.",
            "context": "형사사건, 민사소송, 국가안보 관련 상황에서 사용",
            "culturalNote": "한국에서는 형사피의자뿐 아니라 증인, 민사채무자도 출국금지 대상이 될 수 있는데, 베트남에서는 주로 형사범에게만 적용됩니다. 한국의 출국금지는 법원 영장 없이 행정조치로 가능하지만, 통보 의무와 이의신청 권리가 보장됩니다. 베트남 통역사는 당사자가 공항에서 출국을 거부당하는 상황에서 패닉하지 않도록 사전 통보 제도와 확인 방법을 안내할 수 있어야 합니다.",
            "commonMistakes": [
                {
                    "mistake": "'출국금지'를 'cấm rời khỏi đất nước'로 번역",
                    "correction": "'cấm xuất cảnh' 사용",
                    "explanation": "법률 용어로 'xuất cảnh'이 정확한 표현"
                },
                {
                    "mistake": "여권 압류와 출국금지를 혼동하여 통역",
                    "correction": "여권 압류는 'tịch thu hộ chiếu', 출국금지는 'cấm xuất cảnh'로 구분",
                    "explanation": "여권이 있어도 출국금지 상태일 수 있음"
                },
                {
                    "mistake": "출국금지 기간을 통역하지 않음",
                    "correction": "'6 tháng'(6개월) 등 구체적 기간 명시",
                    "explanation": "기간 정보는 당사자에게 매우 중요함"
                }
            ],
            "examples": [
                {
                    "ko": "형사사건 피의자로서 출국금지 조치가 내려졌습니다.",
                    "vi": "Với tư cách là nghi phạm vụ án hình sự, anh/chị đã bị áp dụng biện pháp cấm xuất cảnh.",
                    "situation": "formal"
                },
                {
                    "ko": "출국금지 여부는 법무부 출입국 홈페이지에서 확인할 수 있습니다.",
                    "vi": "Có thể kiểm tra tình trạng cấm xuất cảnh trên trang web Cục xuất nhập cảnh Bộ Tư pháp.",
                    "situation": "formal"
                },
                {
                    "ko": "출국금지 해제 신청은 담당 검사에게 하셔야 합니다.",
                    "vi": "Đơn xin dỡ bỏ lệnh cấm xuất cảnh phải nộp cho kiểm sát viên phụ trách.",
                    "situation": "onsite"
                }
            ],
            "relatedTerms": ["여권압류", "보석", "도주우려", "인도"]
        },
        {
            "id": "legal-immigration-304",
            "slug": "cong-nhan-ti-nan",
            "korean": "난민인정",
            "vietnamese": "Công nhận tị nạn",
            "hanja": "難民認定",
            "hanjaReading": "難(어려울 난) + 民(백성 민) + 認(알 인) + 定(정할 정)",
            "pronunciation": "난민인정",
            "meaningKo": "인종, 종교, 국적, 정치적 견해 등을 이유로 박해받을 위험이 있어 자국을 떠난 외국인에게 난민 지위를 부여하는 것입니다. 통역 시 난민신청 절차, 심사 기준, 인정 시 혜택(체류자격, 취업허가, 사회보장 등)을 정확히 전달해야 하며, 인도적체류허가와의 차이를 명확히 설명해야 합니다. 난민 면접 통역은 매우 민감하므로 중립성과 정확성이 생명입니다.",
            "meaningVi": "Việc cấp cho người nước ngoài đã rời bỏ quốc gia của mình do có nguy cơ bị bức hại vì lý do chủng tộc, tôn giáo, quốc tịch, quan điểm chính trị,... địa vị người tị nạn. Người được công nhận tị nạn có quyền cư trú, làm việc và được hưởng các chế độ bảo trợ xã hội tại Hàn Quốc.",
            "context": "출입국·외국인청, 난민위원회, 인권단체 상담 상황에서 사용",
            "culturalNote": "한국의 난민인정률은 매우 낮은 편(약 2~4%)으로, 베트남을 포함한 다른 나라와 큰 차이가 있습니다. 한국에서는 난민신청 후 심사 기간이 매우 길고(평균 1~3년), 그 동안 취업이 제한될 수 있음을 정확히 알려야 합니다. 베트남 통역사는 난민 신청자의 트라우마와 문화적 배경을 이해하고, 면접에서 핵심 박해 사실을 정확히 전달할 수 있어야 합니다.",
            "commonMistakes": [
                {
                    "mistake": "'난민'을 'người di cư'(이주자)로 번역",
                    "correction": "'người tị nạn' 또는 'người xin tị nạn'",
                    "explanation": "이주와 난민은 법적 지위가 완전히 다름"
                },
                {
                    "mistake": "인도적체류허가를 난민인정으로 통역",
                    "correction": "인도적체류는 'cho phép lưu trú vì lý do nhân đạo'로 구분",
                    "explanation": "법적 권리와 혜택이 다름"
                },
                {
                    "mistake": "난민 면접에서 신청자의 감정적 진술을 요약하여 통역",
                    "correction": "모든 진술을 축자 통역(verbatim)으로 전달",
                    "explanation": "사소한 디테일이 심사 결과에 영향을 줄 수 있음"
                }
            ],
            "examples": [
                {
                    "ko": "난민인정을 받으면 F-2 체류자격이 부여되어 합법적으로 취업할 수 있습니다.",
                    "vi": "Nếu được công nhận tị nạn sẽ được cấp tư cách lưu trú F-2 và có thể làm việc hợp pháp.",
                    "situation": "formal"
                },
                {
                    "ko": "난민신청이 불허되면 이의신청 또는 행정소송을 제기할 수 있습니다.",
                    "vi": "Nếu đơn xin tị nạn bị từ chối, có thể nộp đơn khiếu nại hoặc khởi kiện hành chính.",
                    "situation": "formal"
                },
                {
                    "ko": "난민 면접에서 박해받은 구체적 사실을 진술하셔야 합니다.",
                    "vi": "Trong phỏng vấn tị nạn, anh/chị phải trình bày cụ thể những sự việc đã bị bức hại.",
                    "situation": "onsite"
                }
            ],
            "relatedTerms": ["인도적체류허가", "난민신청", "박해", "송환금지원칙"]
        },
        {
            "id": "legal-immigration-305",
            "slug": "thay-doi-tu-cach-luu-tru",
            "korean": "체류자격변경",
            "vietnamese": "Thay đổi tư cách lưu trú",
            "hanja": "滯留資格變更",
            "hanjaReading": "滯(머무를 체) + 留(머무를 류) + 資(재물 자) + 格(격식 격) + 變(변할 변) + 更(고칠 경)",
            "pronunciation": "체류자격변경",
            "meaningKo": "외국인이 한국에 체류하면서 기존의 체류자격을 다른 자격으로 바꾸는 것을 의미합니다. 통역 시 변경 가능한 자격의 종류, 신청 시기(체류기간 만료 전), 필요 서류, 심사 기준을 정확히 전달해야 합니다. 특히 유학생의 취업 비자 변경, 결혼이민 등 실제 수요가 많은 케이스에 대한 구체적 정보 제공이 중요합니다.",
            "meaningVi": "Việc người nước ngoài đang lưu trú tại Hàn Quốc thay đổi tư cách lưu trú hiện tại sang tư cách khác. Ví dụ: thay đổi từ visa du học (D-2) sang visa làm việc (E-7), từ visa kết hôn (F-6) sang visa cư trú lâu dài (F-5). Cần nộp đơn trước khi hết hạn lưu trú.",
            "context": "출입국관리사무소, 비자 상담, 취업 준비 상황에서 사용",
            "culturalNote": "한국에서는 체류자격 변경이 까다롭고 심사 기간이 길어(보통 1~3개월), 베트남에서처럼 간단히 처리되지 않습니다. 특히 단순노무 비자(E-9)에서 다른 비자로 변경이 원칙적으로 불가능한 점, 유학생이 졸업 전 구직비자(D-10)로 변경해야 취업 활동이 가능한 점 등을 명확히 안내해야 합니다. 베트남 통역사는 변경 불가 사유를 정확히 전달하여 불필요한 신청을 방지해야 합니다.",
            "commonMistakes": [
                {
                    "mistake": "'체류자격변경'을 'đổi visa'로 번역",
                    "correction": "'thay đổi tư cách lưu trú' 사용",
                    "explanation": "비자와 체류자격은 법적으로 다른 개념"
                },
                {
                    "mistake": "모든 체류자격이 변경 가능하다고 통역",
                    "correction": "변경 가능 여부와 조건을 명확히 확인 후 통역",
                    "explanation": "E-9, H-2 등 일부 자격은 변경 제한이 있음"
                },
                {
                    "mistake": "체류기간 연장과 체류자격 변경을 혼동",
                    "correction": "연장은 'gia hạn', 변경은 'thay đổi tư cách'로 구분",
                    "explanation": "신청 서류와 절차가 완전히 다름"
                }
            ],
            "examples": [
                {
                    "ko": "유학 비자에서 취업 비자로 체류자격을 변경하려면 학사 학위 이상이 필요합니다.",
                    "vi": "Để thay đổi tư cách lưu trú từ visa du học sang visa làm việc cần có bằng cử nhân trở lên.",
                    "situation": "formal"
                },
                {
                    "ko": "체류자격변경 신청은 체류기간 만료 4개월 전부터 가능합니다.",
                    "vi": "Có thể nộp đơn xin thay đổi tư cách lưu trú từ 4 tháng trước khi hết hạn lưu trú.",
                    "situation": "formal"
                },
                {
                    "ko": "E-9 비자는 원칙적으로 다른 체류자격으로 변경이 안 됩니다.",
                    "vi": "Nguyên tắc visa E-9 không thể thay đổi sang tư cách lưu trú khác.",
                    "situation": "onsite"
                }
            ],
            "relatedTerms": ["체류기간연장", "체류자격", "비자", "자격외활동허가"]
        },
        {
            "id": "legal-immigration-306",
            "slug": "giay-phep-nhap-canh-lai",
            "korean": "재입국허가",
            "vietnamese": "Giấy phép nhập cảnh lại",
            "hanja": "再入國許可",
            "hanjaReading": "再(다시 재) + 入(들 입) + 國(나라 국) + 許(허락할 허) + 可(옳을 가)",
            "pronunciation": "재입국허가",
            "meaningKo": "한국에 합법적으로 체류 중인 외국인이 일시 출국 후 다시 입국하기 위해 받아야 하는 허가입니다. 통역 시 단수 재입국허가와 복수 재입국허가의 차이, 유효기간, 신청 시기와 장소를 정확히 전달해야 합니다. 재입국허가 없이 출국하면 체류자격이 자동 소멸되므로 이 점을 강조하여 통역하는 것이 중요합니다.",
            "meaningVi": "Giấy phép mà người nước ngoài đang lưu trú hợp pháp tại Hàn Quốc phải xin để có thể xuất cảnh tạm thời rồi nhập cảnh trở lại. Có 2 loại: giấy phép nhập cảnh lại một lần (đơn) và nhiều lần (đa). Nếu xuất cảnh không xin giấy phép, tư cách lưu trú sẽ tự động bị hủy.",
            "context": "공항 출입국 심사, 출입국관리사무소 민원 상황에서 사용",
            "culturalNote": "한국에서는 재입국허가 제도가 엄격하게 적용되는 반면, 베트남을 포함한 동남아 국가들은 상대적으로 자유롭습니다. 특히 영주권자(F-5)도 2년 이상 출국 시 재입국허가가 필요하며, 장기 체류자가 무심코 재입국허가 없이 출국했다가 입국이 거부되는 사례가 많습니다. 베트남 통역사는 공항에서의 긴급 상황 대처 방법도 숙지해야 합니다.",
            "commonMistakes": [
                {
                    "mistake": "'재입국허가'를 'visa nhập cảnh lại'로 번역",
                    "correction": "'giấy phép nhập cảnh lại' 사용",
                    "explanation": "비자와 재입국허가는 별개의 허가"
                },
                {
                    "mistake": "영주권자는 재입국허가 불필요하다고 통역",
                    "correction": "2년 이상 출국 시 영주권자도 재입국허가 필요",
                    "explanation": "조건부 필요성을 정확히 전달해야 함"
                },
                {
                    "mistake": "재입국허가 유효기간을 통역하지 않음",
                    "correction": "단수는 '1 năm', 복수는 '체류기간 내'로 명시",
                    "explanation": "기간 경과 시 효력 상실되므로 중요"
                }
            ],
            "examples": [
                {
                    "ko": "복수 재입국허가를 받으면 체류기간 내에는 자유롭게 출입국할 수 있습니다.",
                    "vi": "Nếu nhận giấy phép nhập cảnh lại nhiều lần, có thể xuất nhập cảnh tự do trong thời hạn lưu trú.",
                    "situation": "formal"
                },
                {
                    "ko": "재입국허가는 공항 출국장이나 출입국관리사무소에서 신청할 수 있습니다.",
                    "vi": "Có thể xin giấy phép nhập cảnh lại tại khu vực xuất cảnh sân bay hoặc Cục xuất nhập cảnh.",
                    "situation": "formal"
                },
                {
                    "ko": "재입국허가 없이 나가시면 비자가 취소돼서 다시 못 들어오십니다.",
                    "vi": "Nếu xuất cảnh không có giấy phép nhập cảnh lại, visa sẽ bị hủy và không thể nhập cảnh lại.",
                    "situation": "onsite"
                }
            ],
            "relatedTerms": ["출국", "입국", "체류자격", "영주권"]
        },
        {
            "id": "legal-immigration-307",
            "slug": "dang-ky-nguoi-nuoc-ngoai",
            "korean": "외국인등록",
            "vietnamese": "Đăng ký người nước ngoài",
            "hanja": "外國人登錄",
            "hanjaReading": "外(밖 외) + 國(나라 국) + 人(사람 인) + 登(오를 등) + 錄(기록할 록)",
            "pronunciation": "외국인등록",
            "meaningKo": "한국에 90일 이상 장기 체류하는 외국인이 의무적으로 해야 하는 신고입니다. 통역 시 등록 기한(입국 후 90일 이내), 등록 장소(관할 출입국·외국인청), 필요 서류, 외국인등록증 발급 절차와 기간을 정확히 안내해야 합니다. 미등록 시 과태료 부과를 명확히 전달하여 기한 내 등록을 유도하는 것이 중요합니다.",
            "meaningVi": "Việc khai báo bắt buộc đối với người nước ngoài lưu trú dài hạn trên 90 ngày tại Hàn Quốc. Phải đăng ký trong vòng 90 ngày kể từ ngày nhập cảnh tại Cục xuất nhập cảnh có thẩm quyền. Sau khi đăng ký sẽ nhận được thẻ đăng ký người nước ngoài (외국인등록증).",
            "context": "출입국관리사무소, 구청 민원실, 학교 행정실에서 사용",
            "culturalNote": "한국의 외국인등록 제도는 베트남의 임시거주등록(Tạm trú)과 유사하지만, 훨씬 체계적이고 디지털화되어 있습니다. 외국인등록증은 사실상 신분증 역할을 하여 은행 계좌 개설, 휴대폰 가입, 인터넷 쇼핑 등 일상생활에 필수입니다. 베트남 통역사는 등록증의 중요성과 분실 시 재발급 절차, 체류지 변경 시 신고 의무 등을 상세히 안내할 수 있어야 합니다.",
            "commonMistakes": [
                {
                    "mistake": "'외국인등록'을 'đăng ký visa'로 번역",
                    "correction": "'đăng ký người nước ngoài' 사용",
                    "explanation": "비자 신청과는 별개의 절차"
                },
                {
                    "mistake": "등록 기한 90일을 입국일로부터가 아닌 비자 발급일로 계산",
                    "correction": "'từ ngày nhập cảnh'(입국일로부터) 명확히 강조",
                    "explanation": "기산일 착오로 과태료 부과될 수 있음"
                },
                {
                    "mistake": "외국인등록증과 여권을 동일하게 취급",
                    "correction": "등록증은 'thẻ đăng ký', 여권은 'hộ chiếu'로 구분",
                    "explanation": "기능과 용도가 다름"
                }
            ],
            "examples": [
                {
                    "ko": "입국 후 90일 이내에 외국인등록을 하지 않으면 100만 원 이하의 과태료가 부과됩니다.",
                    "vi": "Nếu không đăng ký người nước ngoài trong vòng 90 ngày sau khi nhập cảnh sẽ bị phạt tiền dưới 1 triệu won.",
                    "situation": "formal"
                },
                {
                    "ko": "외국인등록증은 신청 후 약 2주 내에 발급됩니다.",
                    "vi": "Thẻ đăng ký người nước ngoài sẽ được cấp trong khoảng 2 tuần sau khi nộp đơn.",
                    "situation": "formal"
                },
                {
                    "ko": "주소가 바뀌면 14일 이내에 관할 출입국사무소에 신고하셔야 합니다.",
                    "vi": "Nếu thay đổi địa chỉ phải khai báo với Cục xuất nhập cảnh có thẩm quyền trong vòng 14 ngày.",
                    "situation": "onsite"
                }
            ],
            "relatedTerms": ["외국인등록증", "체류지변경신고", "체류자격", "여권"]
        },
        {
            "id": "legal-immigration-308",
            "slug": "di-tru-ket-hon",
            "korean": "결혼이민",
            "vietnamese": "Di trú kết hôn",
            "hanja": "結婚移民",
            "hanjaReading": "結(맺을 결) + 婚(혼인할 혼) + 移(옮길 이) + 民(백성 민)",
            "pronunciation": "결혼이민",
            "meaningKo": "한국 국민과 혼인한 외국인이 한국에 이주하여 정착하는 것을 의미합니다. 통역 시 결혼이민 비자(F-6) 신청 요건, 심사 절차, 위장결혼 방지를 위한 심층 면접, 영주권 및 국적 취득 경로를 정확히 안내해야 합니다. 가정폭력, 이혼 시 체류자격 유지 조건 등 민감한 이슈에 대한 정확한 정보 제공이 중요합니다.",
            "meaningVi": "Việc người nước ngoài kết hôn với công dân Hàn Quốc và di cư để định cư tại Hàn Quốc. Được cấp visa kết hôn (F-6), sau 2 năm có thể xin cư trú lâu dài (F-5), sau 3 năm có thể xin nhập quốc tịch. Có chế độ hỗ trợ hội nhập như lớp học tiếng Hàn, tư vấn văn hóa.",
            "context": "출입국관리사무소, 다문화가족지원센터, 법률상담소에서 사용",
            "culturalNote": "한국의 결혼이민 제도는 베트남 배우자가 가장 많은 비중을 차지하는 만큼, 양국 간 문화 차이와 갈등 요소를 잘 이해하는 통역사가 필요합니다. 한국에서는 위장결혼 단속이 강화되어 실질적 혼인관계 입증이 까다로우며, 이혼 시 체류자격 상실 우려로 가정폭력을 참는 경우가 많습니다. 베트남 통역사는 이혼 후에도 자녀 양육 등의 사유로 체류 가능함을 알리고, 다문화가족지원센터 등 지원 기관을 연결할 수 있어야 합니다.",
            "commonMistakes": [
                {
                    "mistake": "'결혼이민'을 'kết hôn với người Hàn'으로만 번역",
                    "correction": "'di trú kết hôn' 또는 'kết hôn quốc tế'",
                    "explanation": "단순 결혼이 아닌 이민 절차임을 명확히"
                },
                {
                    "mistake": "F-6 비자로 바로 취업 가능하다고 통역",
                    "correction": "취업 활동은 제한 없지만, 자격외활동허가와 혼동 방지",
                    "explanation": "F-6는 체류자격 제한 없음을 정확히 전달"
                },
                {
                    "mistake": "이혼 시 무조건 출국해야 한다고 통역",
                    "correction": "자녀 양육, 가정폭력 피해 등 예외 조건 설명",
                    "explanation": "잘못된 정보로 인한 인권 침해 방지"
                }
            ],
            "examples": [
                {
                    "ko": "결혼이민 비자로 2년 이상 체류하면 영주권을 신청할 수 있습니다.",
                    "vi": "Nếu lưu trú trên 2 năm với visa kết hôn có thể xin cư trú lâu dài.",
                    "situation": "formal"
                },
                {
                    "ko": "배우자의 가정폭력으로 이혼해도 자녀를 양육하면 체류자격이 유지됩니다.",
                    "vi": "Ngay cả khi ly hôn do bạo lực gia đình của vợ/chồng, nếu nuôi con thì vẫn giữ được tư cách lưu trú.",
                    "situation": "formal"
                },
                {
                    "ko": "결혼이민자는 다문화가족지원센터에서 무료로 한국어를 배울 수 있습니다.",
                    "vi": "Người di trú kết hôn có thể học tiếng Hàn miễn phí tại Trung tâm hỗ trợ gia đình đa văn hóa.",
                    "situation": "onsite"
                }
            ],
            "relatedTerms": ["F-6비자", "다문화가족", "영주권", "귀화"]
        },
        {
            "id": "legal-immigration-309",
            "slug": "di-tru-dau-tu",
            "korean": "투자이민",
            "vietnamese": "Di trú đầu tư",
            "hanja": "投資移民",
            "hanjaReading": "投(던질 투) + 資(재물 자) + 移(옮길 이) + 民(백성 민)",
            "pronunciation": "투자이민",
            "meaningKo": "일정 금액 이상을 한국에 투자하여 체류자격을 취득하는 제도입니다. 통역 시 투자 금액(최소 5억 원), 투자 대상(부동산, 기업 등), 체류자격 종류(D-8, F-2, F-5), 고용 창출 요건, 실거주 의무 등을 정확히 전달해야 합니다. 투자 사기 예방을 위한 주의사항도 중요한 통역 포인트입니다.",
            "meaningVi": "Chế độ cho phép người nước ngoài nhận tư cách lưu trú thông qua việc đầu tư một số tiền nhất định vào Hàn Quốc. Đầu tư tối thiểu 500 triệu won (D-8) hoặc 1,5 tỷ won (F-5 điều kiện). Có thể đầu tư vào bất động sản, thành lập doanh nghiệp, hoặc mua trái phiếu chính phủ.",
            "context": "출입국관리사무소, 투자이민 상담, 부동산 거래 상황에서 사용",
            "culturalNote": "한국의 투자이민 제도는 중국 부유층을 주 타깃으로 설계되어, 베트남 투자자에게는 진입장벽이 높은 편입니다. 특히 제주도 투자이민의 경우 부동산 투자금이 5억 원으로 낮지만, 실거주 의무와 투자금 유지 의무가 까다롭습니다. 베트남 통역사는 투자이민 브로커의 과장 광고를 경계하고, 투자금 회수 가능성, 세금 문제, 영주권 취득 후 의무사항 등을 정확히 안내해야 합니다.",
            "commonMistakes": [
                {
                    "mistake": "'투자이민'을 'đầu tư kinh doanh'(투자 사업)로 번역",
                    "correction": "'di trú đầu tư' 또는 'nhập cư đầu tư'",
                    "explanation": "사업 투자가 아닌 이민 목적 투자"
                },
                {
                    "mistake": "투자 금액만 강조하고 고용 창출 요건 누락",
                    "correction": "D-8은 '2명 이상 고용' 조건 명시",
                    "explanation": "요건 미충족 시 체류자격 취소될 수 있음"
                },
                {
                    "mistake": "부동산 투자 시 즉시 영주권 가능하다고 통역",
                    "correction": "F-5는 5년 이상 투자 유지 + 실거주 조건",
                    "explanation": "즉시 영주권은 허위 정보"
                }
            ],
            "examples": [
                {
                    "ko": "5억 원 이상을 한국 기업에 투자하면 D-8 투자 비자를 받을 수 있습니다.",
                    "vi": "Nếu đầu tư trên 500 triệu won vào doanh nghiệp Hàn Quốc có thể nhận visa đầu tư D-8.",
                    "situation": "formal"
                },
                {
                    "ko": "제주도 부동산에 5억 원 투자 시 5년 후 영주권 신청이 가능합니다.",
                    "vi": "Khi đầu tư 500 triệu won vào bất động sản Jeju, có thể xin cư trú lâu dài sau 5 năm.",
                    "situation": "formal"
                },
                {
                    "ko": "투자이민은 투자금을 계속 유지해야 하고, 중간에 회수하면 비자가 취소됩니다.",
                    "vi": "Di trú đầu tư phải duy trì số tiền đầu tư, nếu thu hồi giữa chừng visa sẽ bị hủy.",
                    "situation": "onsite"
                }
            ],
            "relatedTerms": ["D-8비자", "F-5비자", "부동산투자", "고용창출"]
        },
        {
            "id": "legal-immigration-310",
            "slug": "cu-tru-lau-dai",
            "korean": "영주권",
            "vietnamese": "Cư trú lâu dài",
            "hanja": "永住權",
            "hanjaReading": "永(길 영) + 住(살 주) + 權(권세 권)",
            "pronunciation": "영주권",
            "meaningKo": "외국인이 한국에 기간 제한 없이 체류할 수 있는 자격(F-5)입니다. 통역 시 영주권 취득 요건(체류 기간, 소득, 한국어 능력, 품행), 신청 절차, 심사 기간, 영주권자의 권리와 의무(병역 면제, 참정권 제한, 국민건강보험 가입 등)를 정확히 전달해야 합니다. 영주권 취소 사유도 중요한 통역 포인트입니다.",
            "meaningVi": "Tư cách lưu trú (F-5) cho phép người nước ngoài cư trú tại Hàn Quốc không giới hạn thời gian. Điều kiện: lưu trú hợp pháp trên 5 năm, thu nhập ổn định, đạt trình độ tiếng Hàn TOPIK 2급 trở lên, không có tiền án. Người có cư trú lâu dài có quyền làm việc tự do, nhưng không có quyền bầu cử.",
            "context": "출입국관리사무소, 법무법인, 이민 상담 상황에서 사용",
            "culturalNote": "한국의 영주권은 일본, 미국 등에 비해 취득 조건이 까다롭고, 취득 후에도 장기 출국 시 자동 소멸 위험이 있어 베트남 이민자들이 종종 오해하는 부분입니다. 특히 영주권과 국적의 차이(선거권, 병역, 여권 등)를 명확히 설명해야 하며, 영주권자도 범죄 시 강제퇴거 대상이 될 수 있음을 안내해야 합니다. 베트남 통역사는 영주권 심사 면접에서 한국어 능력, 소득 증빙, 정착 의지를 효과적으로 전달하는 역할이 중요합니다.",
            "commonMistakes": [
                {
                    "mistake": "'영주권'을 'quyền công dân'(시민권)으로 번역",
                    "correction": "'cư trú lâu dài' 또는 'thẻ xanh'(영주권 카드)",
                    "explanation": "시민권(국적)과 영주권은 완전히 다른 개념"
                },
                {
                    "mistake": "영주권자는 한국인과 동일한 권리를 갖는다고 통역",
                    "correction": "참정권 없음, 일부 공무원 임용 제한 등 차이 명시",
                    "explanation": "권리 범위를 정확히 전달해야 함"
                },
                {
                    "mistake": "영주권은 영구적이라고 통역",
                    "correction": "2년 이상 출국 시 재입국허가 필요, 범죄 시 취소 가능",
                    "explanation": "조건부 영구성을 명확히 해야 함"
                }
            ],
            "examples": [
                {
                    "ko": "F-2 비자로 3년 이상 체류하고 소득 요건을 충족하면 영주권을 신청할 수 있습니다.",
                    "vi": "Nếu lưu trú trên 3 năm với visa F-2 và đáp ứng điều kiện thu nhập có thể xin cư trú lâu dài.",
                    "situation": "formal"
                },
                {
                    "ko": "영주권자는 체류기간 연장 없이 한국에서 계속 살 수 있지만, 참정권은 없습니다.",
                    "vi": "Người có cư trú lâu dài có thể sống tiếp tại Hàn Quốc mà không cần gia hạn thời hạn lưu trú, nhưng không có quyền bầu cử.",
                    "situation": "formal"
                },
                {
                    "ko": "영주권이 있어도 마약 범죄로 유죄 판결받으면 강제퇴거될 수 있습니다.",
                    "vi": "Ngay cả khi có cư trú lâu dài, nếu bị kết án vì tội ma túy có thể bị trục xuất bắt buộc.",
                    "situation": "onsite"
                }
            ],
            "relatedTerms": ["F-5비자", "귀화", "국적", "체류자격"]
        }
    ]
    return terms

def main():
    """메인 실행 함수"""
    data, file_path = load_existing_terms()
    existing_slugs = {t['slug'] for t in data}
    new_terms = create_legal_terms()

    # 중복 제거
    filtered = [t for t in new_terms if t['slug'] not in existing_slugs]

    # 기존 데이터에 추가
    data.extend(filtered)

    # 파일 저장
    with open(file_path, 'w', encoding='utf-8') as f:
        json.dump(data, f, ensure_ascii=False, indent=2)

    print(f"✅ Added {len(filtered)} terms. Total: {len(data)}")

if __name__ == '__main__':
    main()
