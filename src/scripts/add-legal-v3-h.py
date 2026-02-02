#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
통관법/수출입규제 용어 추가 스크립트
Theme: Customs Law/Import-Export Regulation
"""

import json
import os

# 파일 경로 설정
file_path = os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', 'data', 'terms', 'legal.json')

# 기존 데이터 로드
with open(file_path, 'r', encoding='utf-8') as f:
    data = json.load(f)  # data is a LIST

# 기존 slug 추출
existing_slugs = {t['slug'] for t in data}

# 새 용어 데이터
new_terms = [
    {
        "slug": "hai-quan",
        "korean": "세관",
        "vietnamese": "Hải quan",
        "hanja": "稅關",
        "hanjaReading": "稅(세 세) + 關(관문 관)",
        "pronunciation": "하이 꾸안",
        "meaningKo": "국가의 관세 영역을 출입하는 물품을 관리하고 관세를 징수하는 국가 행정기관입니다. 통역 시 주의할 점은 베트남의 세관(Hải quan)은 재정부 산하 조직으로 한국의 관세청과 유사하지만, 조직 구조와 권한 범위에 차이가 있다는 점입니다. 특히 베트남 세관은 밀수 단속뿐만 아니라 수출입 통계 관리까지 담당하므로, 맥락에 따라 '관세청', '세관', '세관당국' 등으로 구분하여 통역해야 합니다. 현장에서는 '세관 통과' 같은 표현이 자주 사용되므로 'đi qua hải quan', 'thông qua hải quan' 등의 표현도 숙지해야 합니다.",
        "meaningVi": "Cơ quan hành chính nhà nước quản lý hàng hóa xuất nhập khẩu qua biên giới và thu thuế quan. Hải quan Việt Nam trực thuộc Bộ Tài chính, có nhiệm vụ kiểm tra, giám sát hàng hóa xuất nhập khẩu, thu thuế, chống buôn lậu và lập thống kê thương mại quốc tế.",
        "context": "공항, 항구, 국경에서의 물품 검사 및 통관 절차",
        "culturalNote": "한국의 관세청은 독립된 중앙행정기관이지만, 베트남의 세관(Tổng cục Hải quan)은 재정부 산하 조직입니다. 베트남에서는 세관 공무원의 재량권이 상대적으로 크고, 인적 네트워크가 통관 절차에 영향을 미칠 수 있어 한국 기업들이 현지 관행을 이해하는 것이 중요합니다. 또한 베트남 세관은 HS Code 분류나 원산지 판정에서 한국보다 엄격한 경우가 많아 사전 확인이 필수적입니다.",
        "commonMistakes": [
            {
                "mistake": "Hải quan을 '해관'으로 직역",
                "correction": "'세관'으로 번역",
                "explanation": "한국에서는 '세관'이라는 용어가 확립되어 있으므로, 한자 직역인 '해관'은 사용하지 않습니다."
            },
            {
                "mistake": "Cục Hải quan과 Tổng cục Hải quan을 구분하지 않음",
                "correction": "Cục = 지방세관, Tổng cục = 관세청(중앙)",
                "explanation": "Cục Hải quan은 성/시 단위 세관이고, Tổng cục Hải quan은 중앙 총국이므로 맥락에 따라 정확히 구분해야 합니다."
            },
            {
                "mistake": "'세관을 통과하다'를 'qua hải quan'으로만 번역",
                "correction": "'thông quan' 또는 'làm thủ tục hải quan'",
                "explanation": "단순 통과가 아닌 통관 절차를 의미할 때는 'thông quan'이 더 정확한 표현입니다."
            }
        ],
        "examples": [
            {
                "ko": "수입 물품이 세관에 도착하면 24시간 이내에 신고해야 합니다.",
                "vi": "Khi hàng hóa nhập khẩu đến hải quan, phải khai báo trong vòng 24 giờ.",
                "situation": "formal"
            },
            {
                "ko": "세관 검사가 엄격해서 통관에 시간이 걸릴 수 있습니다.",
                "vi": "Việc kiểm tra của hải quan nghiêm ngặt nên có thể mất thời gian để thông quan.",
                "situation": "onsite"
            },
            {
                "ko": "세관 공무원이 원산지 증명서를 요청했습니다.",
                "vi": "Cán bộ hải quan đã yêu cầu giấy chứng nhận xuất xứ.",
                "situation": "formal"
            }
        ],
        "relatedTerms": ["thong-quan", "to-khai-hai-quan", "thue-nhap-khau", "kiem-tra-hai-quan"]
    },
    {
        "slug": "thong-quan",
        "korean": "통관",
        "vietnamese": "Thông quan",
        "hanja": "通關",
        "hanjaReading": "通(통할 통) + 關(관문 관)",
        "pronunciation": "통 꾸안",
        "meaningKo": "세관의 허가를 받아 물품이 국경을 통과하는 절차를 말합니다. 통역 시 주의할 점은 '통관'이라는 용어가 단순한 검사가 아니라 신고, 심사, 검사, 세금 납부, 반출입 허가까지 포함하는 전체 프로세스를 의미한다는 것입니다. 베트남어로는 'thông quan' 외에도 'làm thủ tục hải quan(통관 절차를 하다)'라는 표현이 자주 사용되므로 맥락에 따라 적절히 선택해야 합니다. 현장에서는 '통관이 늦어지다', '통관이 막히다' 같은 표현이 빈번하므로 'thông quan bị chậm', 'thông quan bị tắc nghẽn' 등의 표현도 익혀두어야 합니다.",
        "meaningVi": "Quá trình hoàn tất các thủ tục hải quan để hàng hóa được phép xuất nhập khẩu qua biên giới. Bao gồm khai báo, kiểm tra, nộp thuế và nhận giấy phép thông quan từ cơ quan hải quan.",
        "context": "수출입 업무, 물류, 무역 계약 이행",
        "culturalNote": "한국은 전자통관시스템(UNI-PASS)이 고도로 발달하여 대부분의 통관이 자동화되어 있지만, 베트Nam은 여전히 서류 제출과 대면 확인이 많이 필요합니다. 베트Nam에서는 통관 브로커(관세사)의 역할이 매우 중요하며, 현지 인맥과 경험이 통관 속도를 크게 좌우합니다. 또한 베트Nam은 HS Code 해석이나 과세가격 산정에서 세관의 재량이 크기 때문에, 사전에 충분히 협의하고 필요 서류를 완벽히 준비하는 것이 중요합니다.",
        "commonMistakes": [
            {
                "mistake": "Thông quan을 '통과'로 번역",
                "correction": "'통관'으로 번역",
                "explanation": "'통과'는 단순히 지나가는 것이지만, '통관'은 세관의 공식 절차를 거쳐 허가를 받는 행정 행위입니다."
            },
            {
                "mistake": "'통관하다'를 'thông quan'으로만 번역",
                "correction": "'làm thủ tục thông quan' 또는 'hoàn thành thông quan'",
                "explanation": "Thông quan은 명사이므로, 동사로 사용할 때는 'làm thủ tục' 등을 함께 써야 자연스럽습니다."
            },
            {
                "mistake": "'통관 지연'을 'chậm thông quan'으로 번역",
                "correction": "'thông quan bị chậm trễ' 또는 'việc thông quan bị chậm'",
                "explanation": "베트Nam어에서는 'bị'를 사용하여 피동 표현을 명확히 하는 것이 자연스럽습니다."
            }
        ],
        "examples": [
            {
                "ko": "통관 절차가 완료되면 물품을 인수하실 수 있습니다.",
                "vi": "Khi hoàn tất thủ tục thông quan, quý khách có thể nhận hàng.",
                "situation": "formal"
            },
            {
                "ko": "서류가 미비해서 통관이 지연되고 있습니다.",
                "vi": "Do thiếu giấy tờ nên việc thông quan đang bị chậm trễ.",
                "situation": "onsite"
            },
            {
                "ko": "긴급 통관을 신청하려면 추가 수수료가 필요합니다.",
                "vi": "Để xin thông quan khẩn cấp cần nộp thêm phí.",
                "situation": "formal"
            }
        ],
        "relatedTerms": ["hai-quan", "to-khai-hai-quan", "kiem-tra-hai-quan", "khu-vuc-hai-quan"]
    },
    {
        "slug": "to-khai-hai-quan",
        "korean": "세관신고서",
        "vietnamese": "Tờ khai hải quan",
        "hanja": "稅關申告書",
        "hanjaReading": "稅(세 세) + 關(관문 관) + 申(펼 신) + 告(고할 고) + 書(글 서)",
        "pronunciation": "또 카이 하이 꾸안",
        "meaningKo": "수출입 물품에 대한 정보를 세관에 신고하기 위해 작성하는 공식 문서입니다. 통역 시 주의할 점은 베트Nam에서는 단순히 'tờ khai'라고 줄여 말하는 경우가 많지만, 맥락에 따라 수입신고서(tờ khai nhập khẩu), 수출신고서(tờ khai xuất khẩu)를 명확히 구분해야 한다는 것입니다. 또한 베트Nam은 종이 서류와 전자 신고를 병행하고 있어, '전자 세관신고'는 'tờ khai hải quan điện tử'로 표현해야 합니다. 현장에서는 HS Code, 품명, 수량, 가격, 원산지 등 핵심 항목의 정확한 기재가 중요하므로 관련 용어를 숙지해야 합니다.",
        "meaningVi": "Bản khai báo chính thức về thông tin hàng hóa xuất nhập khẩu nộp cho cơ quan hải quan. Tờ khai hải quan bao gồm các thông tin về mã HS, tên hàng, số lượng, trị giá, xuất xứ và các chứng từ đi kèm theo quy định pháp luật.",
        "context": "수출입 통관 절차, 세관 신고 업무",
        "culturalNote": "한국은 전자통관시스템이 발달하여 대부분 온라인으로 신고하지만, 베트Nam은 아직 종이 서류 제출이 필요한 경우가 많습니다. 특히 초보 수출입업자는 관세사(customs broker)를 통해 신고서를 작성하는 것이 일반적입니다. 베트Nam에서는 신고서 작성 오류 시 통관 지연은 물론 벌금이 부과될 수 있어, 정확한 정보 기재가 매우 중요합니다. 또한 베트Nam 세관은 신고 내용과 실물이 불일치할 경우 엄격하게 제재하므로 사전 확인이 필수입니다.",
        "commonMistakes": [
            {
                "mistake": "Tờ khai hải quan을 '세관 신고'로 번역",
                "correction": "'세관신고서' 또는 '통관신고서'로 번역",
                "explanation": "'Tờ khai'는 서류(문서)를 의미하므로 '~서'를 붙여야 정확합니다."
            },
            {
                "mistake": "'신고서를 제출하다'를 'nộp tờ khai'로만 번역",
                "correction": "'nộp tờ khai hải quan' 또는 'nộp bản khai hải quan'",
                "explanation": "공식 문서이므로 'hải quan'을 명시하는 것이 더 정확하고 격식 있는 표현입니다."
            },
            {
                "mistake": "수입/수출 신고서를 구분하지 않음",
                "correction": "nhập khẩu(수입) / xuất khẩu(수출) 명시",
                "explanation": "맥락에 따라 'tờ khai nhập khẩu' 또는 'tờ khai xuất khẩu'로 정확히 구분해야 합니다."
            }
        ],
        "examples": [
            {
                "ko": "세관신고서를 작성할 때 HS Code를 정확히 기재해야 합니다.",
                "vi": "Khi điền tờ khai hải quan phải ghi chính xác mã HS.",
                "situation": "formal"
            },
            {
                "ko": "신고서에 원산지 증명서를 첨부해 주세요.",
                "vi": "Vui lòng đính kèm giấy chứng nhận xuất xứ vào tờ khai.",
                "situation": "onsite"
            },
            {
                "ko": "전자 세관신고 시스템을 통해 온라인으로 제출할 수 있습니다.",
                "vi": "Có thể nộp trực tuyến qua hệ thống tờ khai hải quan điện tử.",
                "situation": "formal"
            }
        ],
        "relatedTerms": ["hai-quan", "thong-quan", "ma-so-hs-code", "giay-phep-nhap-khau"]
    },
    {
        "slug": "hang-cam-xuat-nhap",
        "korean": "수출입금지품",
        "vietnamese": "Hàng cấm xuất nhập",
        "hanja": "輸出入禁止品",
        "hanjaReading": "輸(보낼 수) + 出(날 출) + 入(들 입) + 禁(금할 금) + 止(그칠 지) + 品(물건 품)",
        "pronunciation": "항 껌 쑤엣 늡",
        "meaningKo": "법률에 의해 수출 또는 수입이 금지된 물품을 말합니다. 통역 시 주의할 점은 베트Nam과 한국의 금지품 목록이 다를 수 있으며, 특히 문화재, 약물, 무기류, 특정 농산물 등은 양국 모두 엄격하게 규제한다는 점입니다. 베트Nam에서는 '마약류(ma túy)', '무기(vũ khí)', '문화재(di sản văn hóa)', '멸종위기종(động vật quý hiếm)' 등 구체적인 품목명도 함께 설명해야 오해가 없습니다. 현장에서는 금지품과 규제품(hàng hạn chế)을 명확히 구분해야 하며, 규제품은 허가를 받으면 가능하지만 금지품은 절대 불가능함을 강조해야 합니다.",
        "meaningVi": "Hàng hóa bị cấm xuất khẩu hoặc nhập khẩu theo quy định pháp luật. Bao gồm ma túy, vũ khí, văn hóa phẩm độc hại, động thực vật quý hiếm, hàng giả, hàng vi phạm sở hữu trí tuệ và các mặt hàng khác theo danh mục do Nhà nước quy định.",
        "context": "통관 검사, 밀수 단속, 법규 준수 교육",
        "culturalNote": "베트Nam은 한국보다 담배, 술 등의 면세 한도가 훨씬 낮고, 전자담배(thuốc lá điện tử)는 완전히 금지되어 있어 한국인 여행자들이 자주 적발됩니다. 또한 베트Nam은 정치적으로 민감한 출판물, 종교 서적, 베트Nam 정부를 비판하는 내용물도 금지품으로 분류할 수 있어 주의가 필요합니다. 반대로 한국은 북한산 물품, 위조품, 음란물 등을 엄격히 규제합니다. 수출입업자는 양국의 최신 금지품 목록을 정기적으로 확인해야 하며, 세관 신고 시 의심스러운 물품은 반드시 사전 문의해야 합니다.",
        "commonMistakes": [
            {
                "mistake": "Hàng cấm을 '금지 물품'으로 번역",
                "correction": "'수출입금지품' 또는 '금지품'",
                "explanation": "공식 용어는 '수출입금지품'이며, 일상에서는 '금지품'으로 줄여 쓸 수 있습니다."
            },
            {
                "mistake": "금지품(hàng cấm)과 규제품(hàng hạn chế)을 혼동",
                "correction": "금지품=절대 불가, 규제품=허가 시 가능",
                "explanation": "금지품은 어떤 경우에도 불가능하지만, 규제품은 정부 허가를 받으면 수출입이 가능합니다."
            },
            {
                "mistake": "'수출금지품'과 '수입금지품'을 구분하지 않음",
                "correction": "hàng cấm xuất khẩu(수출금지품) / hàng cấm nhập khẩu(수입금지품)",
                "explanation": "맥락에 따라 수출 금지인지 수입 금지인지 명확히 해야 합니다."
            }
        ],
        "examples": [
            {
                "ko": "마약류는 수출입금지품이므로 절대 반입할 수 없습니다.",
                "vi": "Ma túy là hàng cấm xuất nhập nên tuyệt đối không được mang vào.",
                "situation": "formal"
            },
            {
                "ko": "금지품을 소지한 경우 형사 처벌을 받을 수 있습니다.",
                "vi": "Nếu mang theo hàng cấm có thể bị xử lý hình sự.",
                "situation": "formal"
            },
            {
                "ko": "전자담배는 베트남에서 수입금지품입니다.",
                "vi": "Thuốc lá điện tử là hàng cấm nhập khẩu tại Việt Nam.",
                "situation": "onsite"
            }
        ],
        "relatedTerms": ["hai-quan", "kiem-tra-hai-quan", "hang-hoa-nhap-khau", "vi-pham-phap-luat"]
    },
    {
        "slug": "kiem-tra-hai-quan",
        "korean": "세관검사",
        "vietnamese": "Kiểm tra hải quan",
        "hanja": "稅關檢査",
        "hanjaReading": "稅(세 세) + 關(관문 관) + 檢(조사할 검) + 査(조사할 사)",
        "pronunciation": "끼엠 짜 하이 꾸안",
        "meaningKo": "수출입 물품이 신고 내용과 일치하는지, 금지품이나 규제품이 포함되어 있지 않은지 확인하기 위해 세관에서 실시하는 검사입니다. 통역 시 주의할 점은 검사 방식에 따라 '서류검사(kiểm tra giấy tờ)', '현물검사(kiểm tra thực tế)', 'X선 검사(kiểm tra bằng máy X-quang)'로 구분된다는 것입니다. 베트Nam 세관은 무작위 검사(kiểm tra ngẫu nhiên)와 위험도 기반 검사(kiểm tra theo đánh giá rủi ro)를 병행하고 있으며, 위험도가 높은 화물일수록 현물검사 비율이 높습니다. 현장에서는 '컨테이너 개봉', '샘플 채취', '무게 확인' 등 구체적인 검사 항목도 통역해야 하므로 관련 표현을 숙지해야 합니다.",
        "meaningVi": "Việc kiểm tra hàng hóa xuất nhập khẩu của cơ quan hải quan để xác minh sự phù hợp giữa khai báo và thực tế, phát hiện hàng cấm, hàng lậu hoặc vi phạm. Kiểm tra hải quan bao gồm kiểm tra giấy tờ, kiểm tra thực tế hàng hóa và kiểm tra bằng thiết bị chuyên dụng.",
        "context": "통관 절차, 화물 인도 전 검사, 밀수 적발",
        "culturalNote": "한국은 위험도 분석 시스템(Risk Management System)이 발달하여 대부분의 화물이 서류 검사만으로 통관되지만, 베트Nam은 여전히 현물검사 비율이 높습니다. 베트Nam 세관 검사는 예측이 어렵고, 같은 물품도 세관원에 따라 판단이 달라질 수 있어 현지 관세사의 조언이 중요합니다. 검사 중 문제가 발견되면 추가 서류 제출, 세금 추징, 심지어 화물 압류까지 가능하므로 사전에 완벽한 서류 준비가 필수입니다. 또한 베트Nam에서는 검사 과정에서 '비공식 비용(chi phí không chính thức)'을 요구받는 사례가 있어, 투명한 절차 준수가 중요합니다.",
        "commonMistakes": [
            {
                "mistake": "Kiểm tra hải quan을 '세관 확인'으로 번역",
                "correction": "'세관검사' 또는 '통관검사'",
                "explanation": "'검사'는 공식적인 행정 행위이므로 '확인'보다 '검사'가 정확합니다."
            },
            {
                "mistake": "서류검사와 현물검사를 구분하지 않음",
                "correction": "kiểm tra giấy tờ(서류검사) / kiểm tra thực tế(현물검사)",
                "explanation": "검사 방식에 따라 소요 시간과 절차가 크게 다르므로 명확히 구분해야 합니다."
            },
            {
                "mistake": "'검사를 받다'를 'kiểm tra'로만 번역",
                "correction": "'được kiểm tra' 또는 'chịu sự kiểm tra'",
                "explanation": "베트Nam어에서는 피동 표현을 명확히 하기 위해 'được' 또는 'chịu'를 사용합니다."
            }
        ],
        "examples": [
            {
                "ko": "무작위로 선정된 화물은 현물검사를 받게 됩니다.",
                "vi": "Hàng hóa được chọn ngẫu nhiên sẽ phải chịu kiểm tra thực tế.",
                "situation": "formal"
            },
            {
                "ko": "세관검사 결과 신고 내용과 실제가 달라서 추가 세금이 부과되었습니다.",
                "vi": "Kết quả kiểm tra hải quan cho thấy nội dung khai báo khác với thực tế nên bị truy thu thuế.",
                "situation": "onsite"
            },
            {
                "ko": "X선 검사로 의심스러운 물품이 발견되었습니다.",
                "vi": "Kiểm tra bằng máy X-quang phát hiện hàng hóa khả nghi.",
                "situation": "formal"
            }
        ],
        "relatedTerms": ["hai-quan", "thong-quan", "hang-cam-xuat-nhap", "kiem-dich-dong-thuc-vat"]
    },
    {
        "slug": "thue-nhap-khau",
        "korean": "수입관세",
        "vietnamese": "Thuế nhập khẩu",
        "hanja": "輸入關稅",
        "hanjaReading": "輸(보낼 수) + 入(들 입) + 關(관문 관) + 稅(세금 세)",
        "pronunciation": "투에 늡 카우",
        "meaningKo": "외국에서 물품을 수입할 때 부과되는 세금으로, 국내 산업 보호와 재정 수입 확보를 목적으로 합니다. 통역 시 주의할 점은 관세율이 품목(HS Code), 원산지, 무역협정(FTA) 적용 여부에 따라 크게 달라진다는 것입니다. 베트Nam은 한-아세안 FTA, RCEP 등 다양한 협정을 체결하고 있어, 원산지 증명서(C/O)를 제출하면 관세 감면 혜택을 받을 수 있습니다. 현장에서는 '관세율(thuế suất)', '과세가격(trị giá tính thuế)', '감면(miễn giảm)' 등의 용어를 정확히 구사해야 하며, 세관의 과세가격 산정 방식을 이해하는 것이 중요합니다.",
        "meaningVi": "Loại thuế áp dụng đối với hàng hóa nhập khẩu từ nước ngoài, nhằm bảo vệ sản xuất trong nước và tạo nguồn thu cho ngân sách nhà nước. Mức thuế nhập khẩu phụ thuộc vào mã HS, xuất xứ hàng hóa và các hiệp định thương mại tự do (FTA) được áp dụng.",
        "context": "수입 통관, 무역 계약, 원가 계산",
        "culturalNote": "베트Nam의 평균 수입관세율은 한국보다 높지만, FTA를 적극 활용하면 관세 부담을 크게 줄일 수 있습니다. 특히 한-베트Nam FTA(VKFTA)가 발효되면서 많은 품목이 관세 인하 또는 철폐 혜택을 받고 있습니다. 그러나 베트Nam 세관은 원산지 판정이 까다롭고, C/O가 미비하거나 원산지 기준을 충족하지 못하면 일반 관세율(MFN)을 적용하므로 주의가 필요합니다. 또한 베트Nam은 과세가격 산정 시 운임, 보험료 등을 포함한 CIF 가격을 기준으로 하며, 신고 가격이 너무 낮으면 세관이 재조사할 수 있습니다.",
        "commonMistakes": [
            {
                "mistake": "Thuế nhập khẩu를 '수입세'로 번역",
                "correction": "'수입관세' 또는 '관세'",
                "explanation": "공식 용어는 '수입관세'이며, 단순히 '세금'이 아닌 '관세'임을 명확히 해야 합니다."
            },
            {
                "mistake": "관세율(thuế suất)과 관세액(số tiền thuế)을 혼동",
                "correction": "thuế suất = 세율(%), số tiền thuế = 세액(금액)",
                "explanation": "세율은 비율(%)이고 세액은 실제 납부 금액이므로 명확히 구분해야 합니다."
            },
            {
                "mistake": "'관세를 내다'를 'nộp thuế nhập khẩu'로만 번역",
                "correction": "'nộp thuế nhập khẩu' 또는 'đóng thuế nhập khẩu'",
                "explanation": "'Nộp'와 'đóng' 모두 사용 가능하며, 'nộp'이 좀 더 공식적입니다."
            }
        ],
        "examples": [
            {
                "ko": "FTA 적용 시 수입관세가 면제되거나 감면됩니다.",
                "vi": "Khi áp dụng FTA, thuế nhập khẩu được miễn hoặc giảm.",
                "situation": "formal"
            },
            {
                "ko": "이 품목의 수입관세율은 10%입니다.",
                "vi": "Thuế suất nhập khẩu của mặt hàng này là 10%.",
                "situation": "onsite"
            },
            {
                "ko": "과세가격에 따라 납부할 관세액이 결정됩니다.",
                "vi": "Số tiền thuế phải nộp được xác định dựa trên trị giá tính thuế.",
                "situation": "formal"
            }
        ],
        "relatedTerms": ["hai-quan", "thong-quan", "xuat-xu-hang-hoa", "co-form"]
    },
    {
        "slug": "xuat-xu-hang-hoa",
        "korean": "원산지",
        "vietnamese": "Xuất xứ hàng hóa",
        "hanja": "原產地",
        "hanjaReading": "原(근원 원) + 産(날 산) + 地(땅 지)",
        "pronunciation": "쑤엣 쑤 항 호아",
        "meaningKo": "상품이 생산, 제조, 가공된 국가나 지역을 의미하며, 관세 적용과 무역협정 혜택 판단의 핵심 기준이 됩니다. 통역 시 주의할 점은 단순히 '어디서 왔는가'가 아니라 FTA 등 특혜 관세를 받기 위한 법적 요건으로서의 원산지 판정 기준을 이해해야 한다는 것입니다. 베트Nam과 한국 모두 '실질적 변형(substantial transformation)' 기준을 적용하며, HS Code 4단위 변경, 부가가치 기준(RVC), 특정 공정 기준 등을 사용합니다. 현장에서는 '원산지 증명서(C/O)', '원산지 표시', '원산지 확인서' 등 관련 서류와 표현을 정확히 통역해야 합니다.",
        "meaningVi": "Quốc gia hoặc vùng lãnh thổ nơi hàng hóa được sản xuất, chế tạo hoặc gia công. Xuất xứ hàng hóa là tiêu chí quan trọng để xác định thuế suất và hưởng ưu đãi thuế quan theo các hiệp định thương mại tự do (FTA).",
        "context": "FTA 적용, 관세 감면, 원산지 증명",
        "culturalNote": "한국과 베트Nam은 다수의 FTA를 체결하고 있어, 정확한 원산지 판정이 기업의 수출입 비용을 크게 좌우합니다. 베트Nam은 원산지 증명을 위해 Form E(ASEAN), Form AK(한-ASEAN FTA), Form VKFTA(한-베트Nam FTA) 등 다양한 양식을 사용하며, 각 협정마다 요구 사항이 다릅니다. 베트Nam 세관은 원산지 증명서 검증에 엄격하며, 사후 검증(post-verification)도 실시하므로 허위 신고 시 관세 추징과 벌금이 부과됩니다. 또한 '메이드 인 차이나(Made in China)' 제품을 베트Nam 경유로 원산지를 우회하는 행위를 방지하기 위해 감시를 강화하고 있습니다.",
        "commonMistakes": [
            {
                "mistake": "Xuất xứ를 '출처'로 번역",
                "correction": "'원산지'로 번역",
                "explanation": "무역 및 관세 맥락에서는 반드시 '원산지'라는 공식 용어를 사용해야 합니다."
            },
            {
                "mistake": "'원산지'와 '제조국'을 같은 것으로 취급",
                "correction": "원산지=법적 판정 기준, 제조국=실제 생산지",
                "explanation": "제조국과 원산지가 다를 수 있으며(예: 중국에서 조립, 한국 원산지), FTA 적용 시 원산지 판정 기준이 중요합니다."
            },
            {
                "mistake": "'원산지 증명서'를 'chứng nhận xuất xứ'로만 번역",
                "correction": "'Giấy chứng nhận xuất xứ' (C/O - Certificate of Origin)",
                "explanation": "'Giấy'를 붙여야 공식 서류임을 명확히 할 수 있으며, 약어 C/O도 함께 설명하면 좋습니다."
            }
        ],
        "examples": [
            {
                "ko": "이 제품은 한국 원산지로 FTA 특혜 관세를 적용받을 수 있습니다.",
                "vi": "Sản phẩm này có xuất xứ Hàn Quốc nên có thể hưởng thuế suất ưu đãi FTA.",
                "situation": "formal"
            },
            {
                "ko": "원산지 증명서를 제출하지 않으면 일반 관세율이 적용됩니다.",
                "vi": "Nếu không nộp giấy chứng nhận xuất xứ sẽ áp dụng thuế suất thông thường.",
                "situation": "onsite"
            },
            {
                "ko": "세관이 원산지 확인을 위해 공장 실사를 요청할 수 있습니다.",
                "vi": "Hải quan có thể yêu cầu kiểm tra thực tế nhà máy để xác minh xuất xứ.",
                "situation": "formal"
            }
        ],
        "relatedTerms": ["co-form", "thue-nhap-khau", "fta", "hai-quan"]
    },
    {
        "slug": "co-form",
        "korean": "원산지증명서",
        "vietnamese": "C/O (Certificate of Origin)",
        "hanja": "原產地證明書",
        "hanjaReading": "原(근원 원) + 産(날 산) + 地(땅 지) + 證(증거 증) + 明(밝을 명) + 書(글 서)",
        "pronunciation": "씨오 (또는 써-띠-삐-깟 옵 오-리-진)",
        "meaningKo": "수출 물품의 원산지가 특정 국가임을 공식적으로 증명하는 서류로, FTA 특혜 관세를 받기 위해 필수적으로 제출해야 하는 문서입니다. 통역 시 주의할 점은 C/O의 종류가 협정마다 다르며(Form E, Form AK, Form VKFTA 등), 발급 기관과 유효기간도 각각 다르다는 것입니다. 베트Nam에서는 상공회의소(VCCI)나 산업무역부(MOIT)에서 C/O를 발급하며, 한국은 세관, 상공회의소, 관세사 등이 발급합니다. 현장에서는 'C/O 없음', 'C/O 만료', 'C/O 내용 불일치' 같은 문제 상황을 정확히 통역하고, 해결 방법을 제시할 수 있어야 합니다.",
        "meaningVi": "Giấy chứng nhận xuất xứ hàng hóa, là chứng từ chính thức xác nhận hàng hóa có xuất xứ từ một quốc gia cụ thể, cần thiết để hưởng ưu đãi thuế quan theo FTA. Ở Việt Nam, C/O được cấp bởi VCCI (Phòng Thương mại và Công nghiệp Việt Nam) hoặc Bộ Công Thương.",
        "context": "FTA 적용, 특혜 관세 신청, 수출입 서류",
        "culturalNote": "한국과 베트Nam 간 무역에서는 주로 Form E(ASEAN 역내), Form AK(한-ASEAN FTA), Form VKFTA(한-베트Nam FTA)가 사용됩니다. 각 협정마다 원산지 기준, 누적 규정, 미소기준(de minimis) 등이 다르므로, 기업은 자사 제품에 가장 유리한 협정을 선택해야 합니다. 베트Nam은 전자 C/O(e-C/O) 시스템을 도입하여 온라인 발급이 가능하지만, 한국 세관에서 인정 여부를 확인해야 합니다. C/O는 일반적으로 선적일로부터 1년 이내에 사용해야 하며, 사후 발급(retroactive issuance)도 가능하지만 추가 수수료가 부과될 수 있습니다.",
        "commonMistakes": [
            {
                "mistake": "C/O를 '증명서'로만 번역",
                "correction": "'원산지증명서'로 번역",
                "explanation": "C/O는 Certificate of Origin의 약자이므로 풀어서 '원산지증명서'로 번역해야 합니다."
            },
            {
                "mistake": "모든 C/O를 같은 것으로 취급",
                "correction": "Form E, Form AK, Form VKFTA 등 협정별로 구분",
                "explanation": "각 FTA마다 요구하는 C/O 양식과 기재 사항이 다르므로 명확히 구분해야 합니다."
            },
            {
                "mistake": "'C/O를 발급받다'를 'lấy C/O'로 번역",
                "correction": "'được cấp C/O' 또는 'xin cấp C/O'",
                "explanation": "'Lấy'는 너무 일상적이므로 공식 문서 발급 시에는 'được cấp' 또는 'xin cấp'를 사용합니다."
            }
        ],
        "examples": [
            {
                "ko": "FTA 혜택을 받으려면 원산지증명서를 세관에 제출해야 합니다.",
                "vi": "Để được hưởng ưu đãi FTA phải nộp giấy chứng nhận xuất xứ (C/O) cho hải quan.",
                "situation": "formal"
            },
            {
                "ko": "이 제품은 Form AK로 발급받으시면 됩니다.",
                "vi": "Sản phẩm này có thể xin cấp theo Form AK.",
                "situation": "onsite"
            },
            {
                "ko": "원산지증명서가 만료되어 특혜 관세를 적용받을 수 없습니다.",
                "vi": "C/O đã hết hạn nên không thể áp dụng thuế suất ưu đãi.",
                "situation": "formal"
            }
        ],
        "relatedTerms": ["xuat-xu-hang-hoa", "thue-nhap-khau", "fta", "hai-quan"]
    },
    {
        "slug": "khu-vuc-hai-quan",
        "korean": "보세구역",
        "vietnamese": "Khu vực hải quan",
        "hanja": "保稅區域",
        "hanjaReading": "保(지킬 보) + 稅(세금 세) + 區(구역 구) + 域(지역 역)",
        "pronunciation": "쿠 붜 하이 꾸안",
        "meaningKo": "관세가 유보된 상태로 외국 물품을 장치, 보관, 전시, 제조, 가공할 수 있는 특정 지역을 말합니다. 통역 시 주의할 점은 보세구역 내에서는 통관 전이므로 관세가 부과되지 않으며, 물품을 국내로 반입할 때 비로소 수입 신고와 관세 납부가 이루어진다는 것입니다. 베트Nam어로는 'khu vực hải quan', 'khu phi thuế quan', 'khu chế xuất' 등 다양하게 불리며, 맥락에 따라 구분해야 합니다. 현장에서는 '보세창고(kho ngoại quan)', '보세공장(nhà máy trong khu chế xuất)', '자유무역지대(khu thương mại tự do)' 등 구체적인 시설명도 함께 사용됩니다.",
        "meaningVi": "Khu vực được hải quan giám sát, nơi hàng hóa nước ngoài có thể lưu kho, bảo quản, trưng bày, chế biến mà chưa phải nộp thuế nhập khẩu. Thuế chỉ được tính khi hàng hóa xuất ra khỏi khu vực hải quan để tiêu thụ nội địa.",
        "context": "물류, 제조업, 수출입 업무",
        "culturalNote": "한국은 보세창고, 보세공장, 보세전시장, 보세판매장 등 다양한 형태의 보세구역이 발달해 있으며, 인천공항 면세점도 보세판매장의 일종입니다. 베트Nam도 최근 수출가공구역(EPZ), 경제특구(SEZ) 등을 확대하고 있으며, 외국인 투자 기업들이 보세구역에 공장을 설립하여 원자재를 무관세로 수입해 제품을 생산한 후 수출하는 방식이 일반적입니다. 보세구역 내에서는 일반적으로 부가가치세(VAT)도 면제되지만, 국내 판매 시에는 수입 통관과 함께 VAT를 납부해야 합니다. 베트Nam의 경우 보세구역 관리가 까다롭고, 물품 반출입 시 세관 승인이 필요하므로 절차를 정확히 이해해야 합니다.",
        "commonMistakes": [
            {
                "mistake": "Khu vực hải quan을 '세관 지역'으로 번역",
                "correction": "'보세구역' 또는 '관세 유보 지역'",
                "explanation": "공식 용어는 '보세구역'이며, 관세가 유보된 특별한 법적 지위를 가진 구역입니다."
            },
            {
                "mistake": "보세구역(khu vực hải quan)과 자유무역지대(khu thương mại tự do)를 혼동",
                "correction": "보세구역=관세 유보, 자유무역지대=더 광범위한 규제 완화",
                "explanation": "자유무역지대는 관세뿐 아니라 외환, 투자 규제도 완화된 지역으로 보세구역보다 넓은 개념입니다."
            },
            {
                "mistake": "'보세창고'와 '일반창고'를 구분하지 않음",
                "correction": "kho ngoại quan(보세창고) / kho thông thường(일반창고)",
                "explanation": "보세창고는 세관 감독 하에 있으며 통관 전 물품을 보관할 수 있지만, 일반창고는 이미 통관된 물품만 보관 가능합니다."
            }
        ],
        "examples": [
            {
                "ko": "보세구역 내에서는 관세를 납부하지 않고 물품을 보관할 수 있습니다.",
                "vi": "Trong khu vực hải quan có thể bảo quản hàng hóa mà không phải nộp thuế quan.",
                "situation": "formal"
            },
            {
                "ko": "보세공장에서 생산된 제품을 수출하면 관세 혜택을 받습니다.",
                "vi": "Sản phẩm sản xuất tại nhà máy trong khu chế xuất khi xuất khẩu sẽ được hưởng ưu đãi thuế quan.",
                "situation": "onsite"
            },
            {
                "ko": "보세구역에서 국내로 반출할 때 수입 신고를 해야 합니다.",
                "vi": "Khi xuất hàng từ khu vực hải quan ra nội địa phải làm thủ tục khai báo nhập khẩu.",
                "situation": "formal"
            }
        ],
        "relatedTerms": ["kho-ngoai-quan", "hai-quan", "thong-quan", "khu-che-xuat"]
    },
    {
        "slug": "kho-ngoai-quan",
        "korean": "보세창고",
        "vietnamese": "Kho ngoại quan",
        "hanja": "保稅倉庫",
        "hanjaReading": "保(지킬 보) + 稅(세금 세) + 倉(곳집 창) + 庫(곳집 고)",
        "pronunciation": "코 응오아이 꾸안",
        "meaningKo": "수입 물품을 통관하기 전에 일정 기간 장치할 수 있도록 세관장의 허가를 받은 창고로, 관세 납부가 유예되는 시설입니다. 통역 시 주의할 점은 보세창고는 단순한 물류 창고가 아니라 세관의 감독을 받는 특수 시설이며, 물품의 반입·반출 시 세관 신고가 필요하다는 것입니다. 베트Nam에서는 'kho ngoại quan' 외에도 'kho bảo thuế'라는 표현도 사용되며, 보세창고 운영 허가는 세관으로부터 받아야 합니다. 현장에서는 '장치 기간(thời hạn lưu kho)', '창고료(phí lưu kho)', '화물 입출고(nhập/xuất kho)' 등의 용어를 정확히 통역해야 합니다.",
        "meaningVi": "Kho được hải quan cấp phép để lưu giữ hàng hóa nhập khẩu chưa thông quan trong một thời gian nhất định mà không phải nộp thuế ngay. Kho ngoại quan chịu sự giám sát của hải quan và phải tuân thủ các quy định về quản lý hàng hóa xuất nhập kho.",
        "context": "물류, 수입 통관 절차, 재고 관리",
        "culturalNote": "한국의 보세창고는 인천항, 부산항 등 주요 항구와 공항 주변에 집중되어 있으며, 장치 기간은 통상 6개월입니다. 베트Nam도 하노이, 호치민, 하이퐁 등 주요 도시에 보세창고가 있으며, 장치 기간은 일반적으로 90일이지만 연장 가능합니다. 베트Nam에서는 보세창고 이용 시 세관 공무원의 검사가 수시로 있을 수 있으며, 재고 관리가 정확하지 않으면 문제가 될 수 있습니다. 또한 보세창고에서 국내로 물품을 반출할 때는 수입 통관 절차를 거쳐야 하며, 이때 비로소 관세와 부가가치세를 납부합니다. 기업들은 보세창고를 활용하여 자금 흐름을 관리하고, 필요한 시점에 통관하여 재고 비용을 절감할 수 있습니다.",
        "commonMistakes": [
            {
                "mistake": "Kho ngoại quan을 '외관 창고'로 직역",
                "correction": "'보세창고'로 번역",
                "explanation": "'보세창고'는 확립된 무역 용어이므로, 한자 직역인 '외관 창고'는 사용하지 않습니다."
            },
            {
                "mistake": "보세창고(kho ngoại quan)와 일반창고(kho thông thường)를 구분하지 않음",
                "correction": "보세창고=관세 유보, 세관 감독 / 일반창고=통관 완료 물품",
                "explanation": "보세창고는 통관 전 물품을 보관하며 세관 감독을 받지만, 일반창고는 이미 통관된 물품만 보관합니다."
            },
            {
                "mistake": "'창고에 보관하다'를 'giữ trong kho'로만 번역",
                "correction": "'lưu kho' 또는 'lưu giữ tại kho ngoại quan'",
                "explanation": "보세창고 맥락에서는 'lưu kho'가 더 전문적이고 정확한 표현입니다."
            }
        ],
        "examples": [
            {
                "ko": "수입 물품을 보세창고에 보관한 후 필요할 때 통관할 수 있습니다.",
                "vi": "Có thể lưu hàng nhập khẩu tại kho ngoại quan rồi thông quan khi cần.",
                "situation": "formal"
            },
            {
                "ko": "보세창고 장치 기간이 초과되면 벌금이 부과됩니다.",
                "vi": "Nếu quá thời hạn lưu kho ngoại quan sẽ bị phạt.",
                "situation": "onsite"
            },
            {
                "ko": "보세창고에서 물품을 반출할 때는 세관 신고가 필요합니다.",
                "vi": "Khi xuất hàng từ kho ngoại quan phải khai báo với hải quan.",
                "situation": "formal"
            }
        ],
        "relatedTerms": ["khu-vuc-hai-quan", "hai-quan", "thong-quan", "hang-hoa-nhap-khau"]
    }
]

# 중복 제거 및 추가
new_slugs = [term['slug'] for term in new_terms]
filtered_terms = [term for term in new_terms if term['slug'] not in existing_slugs]

if not filtered_terms:
    print("⚠️  모든 용어가 이미 존재합니다. 추가할 항목이 없습니다.")
else:
    data.extend(filtered_terms)

    # 파일 저장
    with open(file_path, 'w', encoding='utf-8') as f:
        json.dump(data, f, ensure_ascii=False, indent=2)

    print(f"✅ {len(filtered_terms)}개 용어 추가 완료!")
    print(f"📊 총 용어 수: {len(data)}개")
    print(f"\n추가된 용어:")
    for term in filtered_terms:
        print(f"  - {term['slug']} ({term['korean']} / {term['vietnamese']})")

    if len(filtered_terms) < len(new_terms):
        skipped = len(new_terms) - len(filtered_terms)
        print(f"\n⚠️  {skipped}개 중복 용어 제외됨")
