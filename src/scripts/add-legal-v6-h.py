#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""보험법 심화 용어 추가 스크립트 (v6-h)"""

import json
import os

def load_existing_terms():
    file_path = os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', 'data', 'terms', 'legal.json')
    with open(file_path, 'r', encoding='utf-8') as f:
        data = json.load(f)
    return data, file_path

def create_legal_terms():
    terms = [
        {
            "slug": "gian-lan-bao-hiem",
            "korean": "보험사기",
            "vietnamese": "Gian lận bảo hiểm",
            "hanja": "保險詐欺",
            "hanjaReading": "保(지킬 보) 險(험할 험) 詐(속일 사) 欺(속일 기)",
            "pronunciation": "지안 런 바오 히엠",
            "meaningKo": "보험금을 부정하게 취득하거나 보험료를 편취할 목적으로 고의로 사고를 일으키거나 허위사실을 신고하는 범죄행위. 통역 시 베트남에서는 'lừa đảo bảo hiểm'과 혼용되나 법률 용어로는 'gian lận'이 정확하며, 형사처벌 대상임을 명확히 전달해야 함. 보험사기 적발 시 보험금 부지급뿐 아니라 형사고소 가능성도 설명 필요.",
            "meaningVi": "Hành vi phạm tội có chủ ý gây ra tai nạn hoặc khai báo sai sự thật nhằm mục đích chiếm đoạt tiền bảo hiểm hoặc lừa đảo phí bảo hiểm một cách bất hợp pháp.",
            "context": "형사법, 보험계약법",
            "culturalNote": "한국은 보험사기방지특별법으로 엄격히 처벌하며 보험사기 적발 시스템이 고도화되어 있으나, 베트남은 보험시장 발전 초기 단계로 적발 인프라가 상대적으로 미흡함. 한국에서는 경미한 과장도 사기로 간주될 수 있어 베트남 통역 시 처벌 수위 차이를 설명해야 함.",
            "commonMistakes": [
                {
                    "mistake": "lừa đảo bảo hiểm (속임수 보험)",
                    "correction": "gian lận bảo hiểm (보험사기)",
                    "explanation": "'lừa đảo'는 일반 사기, 'gian lận'은 법률상 부정행위로 더 정확한 법률 용어"
                },
                {
                    "mistake": "trục lợi bảo hiểm (부당이득)",
                    "correction": "gian lận bảo hiểm (보험사기)",
                    "explanation": "'trục lợi'는 부당이득 일반, 보험사기는 형사처벌 대상인 범죄행위"
                },
                {
                    "mistake": "vi phạm hợp đồng bảo hiểm (계약 위반)",
                    "correction": "gian lận bảo hiểm (보험사기)",
                    "explanation": "단순 계약 위반은 민사, 보험사기는 형사처벌 대상으로 법적 성격이 다름"
                }
            ],
            "examples": [
                {
                    "ko": "보험사기 혐의로 검찰에 고발되었습니다.",
                    "vi": "Đã bị tố cáo lên viện kiểm sát với cáo buộc gian lận bảo hiểm.",
                    "situation": "formal"
                },
                {
                    "ko": "고의 사고로 보험사기가 인정되어 보험금이 부지급 처리되었습니다.",
                    "vi": "Do tai nạn cố ý được xác định là gian lận bảo hiểm nên tiền bảo hiểm đã bị từ chối chi trả.",
                    "situation": "formal"
                },
                {
                    "ko": "병원과 공모한 보험사기 조직이 적발되었습니다.",
                    "vi": "Tổ chức gian lận bảo hiểm câu kết với bệnh viện đã bị phát hiện.",
                    "situation": "onsite"
                }
            ],
            "relatedTerms": ["보험금청구", "면책조항", "보험분쟁"]
        },
        {
            "slug": "yeu-cau-boi-thuong-bao-hiem",
            "korean": "보험금청구",
            "vietnamese": "Yêu cầu bồi thường bảo hiểm",
            "hanja": "保險金請求",
            "hanjaReading": "保(지킬 보) 險(험할 험) 金(쇠 금) 請(청할 청) 求(구할 구)",
            "pronunciation": "이에우 까우 보이 투엉 바오 히엠",
            "meaningKo": "보험사고 발생 시 보험계약자나 피보험자가 보험회사에 보험금 지급을 요구하는 법률행위. 통역 시 'yêu cầu'는 요구, 'bồi thường'은 보상을 의미하며, 청구 절차와 필요 서류를 정확히 전달해야 함. 청구권 소멸시효(한국 3년)와 베트남(2-3년) 차이를 설명하고, 청구 지연 시 불이익 발생 가능성을 명확히 안내 필요.",
            "meaningVi": "Hành vi pháp lý mà bên mua bảo hiểm hoặc người được bảo hiểm yêu cầu công ty bảo hiểm chi trả tiền bảo hiểm khi xảy ra sự kiện bảo hiểm.",
            "context": "보험계약법, 민사소송법",
            "culturalNote": "한국은 청구서류가 표준화되어 있고 온라인 청구 시스템이 발달했으나, 베트남은 서류 중심의 대면 청구가 일반적. 한국에서는 보험금 지급 거부 시 금융감독원 분쟁조정 제도가 활성화되어 있어 통역 시 이러한 권리 구제 수단 차이를 설명해야 함.",
            "commonMistakes": [
                {
                    "mistake": "đòi tiền bảo hiểm (돈 요구)",
                    "correction": "yêu cầu bồi thường bảo hiểm (보험금 청구)",
                    "explanation": "'đòi'는 구어체 표현으로 무례하게 들릴 수 있어 법률 문서에서는 'yêu cầu' 사용"
                },
                {
                    "mistake": "xin tiền bảo hiểm (돈 부탁)",
                    "correction": "yêu cầu bồi thường bảo hiểm (보험금 청구)",
                    "explanation": "'xin'은 간청의 의미로 계약상 권리 행사인 청구와는 뉘앙스가 다름"
                },
                {
                    "mistake": "thanh toán bảo hiểm (보험 지급)",
                    "correction": "yêu cầu bồi thường bảo hiểm (보험금 청구)",
                    "explanation": "'thanh toán'은 지급 행위를 의미하나, 청구는 지급 요구 행위"
                }
            ],
            "examples": [
                {
                    "ko": "교통사고 발생 후 30일 이내에 보험금을 청구해야 합니다.",
                    "vi": "Phải yêu cầu bồi thường bảo hiểm trong vòng 30 ngày sau khi xảy ra tai nạn giao thông.",
                    "situation": "formal"
                },
                {
                    "ko": "진단서와 영수증을 첨부하여 보험금청구서를 제출하세요.",
                    "vi": "Hãy nộp đơn yêu cầu bồi thường bảo hiểm kèm theo giấy chẩn đoán và hóa đơn.",
                    "situation": "onsite"
                },
                {
                    "ko": "보험금청구가 반려되면 이의신청을 할 수 있습니다.",
                    "vi": "Nếu yêu cầu bồi thường bảo hiểm bị từ chối, có thể nộp đơn khiếu nại.",
                    "situation": "formal"
                }
            ],
            "relatedTerms": ["보험사기", "면책조항", "보험약관"]
        },
        {
            "slug": "dieu-khoan-mien-trach-nhiem",
            "korean": "면책조항",
            "vietnamese": "Điều khoản miễn trách nhiệm",
            "hanja": "免責條項",
            "hanjaReading": "免(면할 면) 責(꾸짖을 책) 條(가지 조) 項(항목 항)",
            "pronunciation": "디에우 코안 미엔 짝 니엠",
            "meaningKo": "보험사고가 발생해도 보험회사가 보험금 지급 의무를 면하는 경우를 규정한 보험약관 조항. 통역 시 'miễn trách nhiệm'은 책임 면제를 의미하며, 고의·중과실·전쟁 등 일반적 면책사유를 구체적으로 설명해야 함. 약관 해석 분쟁 시 보험계약자에게 유리하게 해석되는 원칙을 안내하고, 면책조항의 법적 효력 범위를 정확히 전달 필요.",
            "meaningVi": "Điều khoản trong hợp đồng bảo hiểm quy định các trường hợp công ty bảo hiểm được miễn trừ nghĩa vụ chi trả tiền bảo hiểm ngay cả khi sự kiện bảo hiểm xảy ra.",
            "context": "보험계약법, 약관규제법",
            "culturalNote": "한국은 약관규제법으로 불공정 면책조항을 무효화하며 보험업법상 표준약관 제도가 정착되어 있으나, 베트남은 약관 투명성이 상대적으로 낮아 분쟁 소지가 많음. 한국에서는 면책조항을 굵은 글씨로 명시하도록 의무화되어 있어 통역 시 약관 고지 의무 차이를 설명해야 함.",
            "commonMistakes": [
                {
                    "mistake": "không chịu trách nhiệm (책임 안 짐)",
                    "correction": "điều khoản miễn trách nhiệm (면책조항)",
                    "explanation": "구어적 표현보다는 법률 용어인 'điều khoản miễn trách nhiệm' 사용이 정확"
                },
                {
                    "mistake": "loại trừ bảo hiểm (보험 제외)",
                    "correction": "điều khoản miễn trách nhiệm (면책조항)",
                    "explanation": "'loại trừ'는 일반적 제외, 면책조항은 법정 요건을 갖춘 약관 조항"
                },
                {
                    "mistake": "từ chối bồi thường (보상 거절)",
                    "correction": "điều khoản miễn trách nhiệm (면책조항)",
                    "explanation": "거절은 결과, 면책조항은 거절 근거가 되는 법률 조항"
                }
            ],
            "examples": [
                {
                    "ko": "고의 사고는 면책조항에 해당하여 보험금이 지급되지 않습니다.",
                    "vi": "Tai nạn cố ý thuộc điều khoản miễn trách nhiệm nên không được chi trả tiền bảo hiểm.",
                    "situation": "formal"
                },
                {
                    "ko": "면책조항은 계약서 5조에 상세히 명시되어 있습니다.",
                    "vi": "Điều khoản miễn trách nhiệm được quy định chi tiết tại điều 5 của hợp đồng.",
                    "situation": "formal"
                },
                {
                    "ko": "전쟁과 내란은 일반적인 면책사유입니다.",
                    "vi": "Chiến tranh và nội loạn là các trường hợp miễn trách nhiệm thông thường.",
                    "situation": "onsite"
                }
            ],
            "relatedTerms": ["보험약관", "보험금청구", "보험계리"]
        },
        {
            "slug": "tinh-toan-bao-hiem",
            "korean": "보험계리",
            "vietnamese": "Tính toán bảo hiểm",
            "hanja": "保險計理",
            "hanjaReading": "保(지킬 보) 險(험할 험) 計(셀 계) 理(다스릴 리)",
            "pronunciation": "틴 또안 바오 히엠",
            "meaningKo": "보험료 산정과 책임준비금 계산 등 보험 수리적 업무를 수행하는 전문 영역. 통역 시 'tính toán'은 계산, 'bảo hiểm'은 보험을 의미하나, 베트남에서는 'chuyên gia bảo hiểm toán học(보험수리 전문가)'로도 표현. 보험계리사(actuary) 자격 제도가 한국과 베트nam에서 다르므로 자격 인정 범위를 명확히 안내하고, 계리 보고서의 법적 효력을 정확히 전달 필요.",
            "meaningVi": "Lĩnh vực chuyên môn thực hiện các công việc toán học bảo hiểm như tính phí bảo hiểm và dự phòng nghĩa vụ bảo hiểm.",
            "context": "보험업법, 금융규제법",
            "culturalNote": "한국은 보험계리사 제도가 법정화되어 있고 계리 보고서가 금융당국 감독 대상이나, 베트남은 보험시장 역사가 짧아 계리 전문성이 발전 단계. 한국에서는 계리사 서명이 법정 요건인 경우가 많아 통역 시 계리 보고서의 법적 지위 차이를 설명해야 함.",
            "commonMistakes": [
                {
                    "mistake": "toán học bảo hiểm (보험 수학)",
                    "correction": "tính toán bảo hiểm (보험계리)",
                    "explanation": "'toán học'은 학문 분야, 'tính toán'은 실무 업무 영역"
                },
                {
                    "mistake": "kế toán bảo hiểm (보험 회계)",
                    "correction": "tính toán bảo hiểm (보험계리)",
                    "explanation": "회계(kế toán)와 계리(tính toán)는 별개 전문 영역"
                },
                {
                    "mistake": "phân tích bảo hiểm (보험 분석)",
                    "correction": "tính toán bảo hiểm (보험계리)",
                    "explanation": "분석은 일반적 용어, 계리는 수리적 전문 업무"
                }
            ],
            "examples": [
                {
                    "ko": "보험계리 보고서에 따라 보험료가 인상됩니다.",
                    "vi": "Phí bảo hiểm sẽ tăng theo báo cáo tính toán bảo hiểm.",
                    "situation": "formal"
                },
                {
                    "ko": "보험계리사의 검증을 거쳐 책임준비금이 산정되었습니다.",
                    "vi": "Dự phòng nghĩa vụ bảo hiểm đã được tính toán sau khi thẩm định của chuyên gia bảo hiểm toán học.",
                    "situation": "formal"
                },
                {
                    "ko": "보험계리 기준이 국제 표준에 부합하는지 검토 중입니다.",
                    "vi": "Đang xem xét xem tiêu chuẩn tính toán bảo hiểm có phù hợp với chuẩn mực quốc tế hay không.",
                    "situation": "onsite"
                }
            ],
            "relatedTerms": ["재보험", "보험약관", "보험규제"]
        },
        {
            "slug": "tai-bao-hiem",
            "korean": "재보험",
            "vietnamese": "Tái bảo hiểm",
            "hanja": "再保險",
            "hanjaReading": "再(다시 재) 保(지킬 보) 險(험할 험)",
            "pronunciation": "따이 바오 히엠",
            "meaningKo": "보험회사가 인수한 보험 위험의 일부 또는 전부를 다른 보험회사에 전가하는 보험 거래. 통역 시 'tái'는 '재(再)'의 의미로 다시 보험을 드는 것을 의미하며, 원수보험과 재보험의 법률관계가 독립적임을 명확히 설명해야 함. 재보험 계약이 원계약자의 권리에 영향을 주지 않음을 안내하고, 국제재보험 시 준거법과 관할 합의 조항의 중요성을 강조 필요.",
            "meaningVi": "Giao dịch bảo hiểm mà công ty bảo hiểm chuyển giao một phần hoặc toàn bộ rủi ro bảo hiểm đã nhận cho công ty bảo hiểm khác.",
            "context": "보험업법, 국제계약법",
            "culturalNote": "한국 보험사는 글로벌 재보험사(Munich Re, Swiss Re 등)와 거래가 활발하나, 베트남은 재보험 시장이 발달 초기 단계. 한국에서는 거대재해 대비 재보험 비율이 법정되어 있어 통역 시 재보험 규제 차이를 설명해야 함.",
            "commonMistakes": [
                {
                    "mistake": "bảo hiểm lại (다시 보험)",
                    "correction": "tái bảo hiểm (재보험)",
                    "explanation": "구어적 표현보다는 법률 용어인 'tái bảo hiểm' 사용이 정확"
                },
                {
                    "mistake": "bảo hiểm phụ (부보험)",
                    "correction": "tái bảo hiểm (재보험)",
                    "explanation": "'phụ'는 부수적 의미로 재보험의 법적 성격과 다름"
                },
                {
                    "mistake": "bảo hiểm cho công ty bảo hiểm (보험사 보험)",
                    "correction": "tái bảo hiểm (재보험)",
                    "explanation": "설명적 표현보다는 법률 용어 'tái bảo hiểm' 사용"
                }
            ],
            "examples": [
                {
                    "ko": "대형 사고에 대비하여 재보험 계약을 체결했습니다.",
                    "vi": "Đã ký hợp đồng tái bảo hiểm để phòng ngừa các tai nạn lớn.",
                    "situation": "formal"
                },
                {
                    "ko": "재보험료는 원수보험료의 30%입니다.",
                    "vi": "Phí tái bảo hiểm là 30% của phí bảo hiểm gốc.",
                    "situation": "formal"
                },
                {
                    "ko": "재보험사의 지급불능은 원수보험사의 지급 의무에 영향을 주지 않습니다.",
                    "vi": "Việc công ty tái bảo hiểm mất khả năng thanh toán không ảnh hưởng đến nghĩa vụ chi trả của công ty bảo hiểm gốc.",
                    "situation": "onsite"
                }
            ],
            "relatedTerms": ["보험계리", "보험규제", "보험약관"]
        },
        {
            "slug": "dieu-khoan-bao-hiem",
            "korean": "보험약관",
            "vietnamese": "Điều khoản bảo hiểm",
            "hanja": "保險約款",
            "hanjaReading": "保(지킬 보) 險(험할 험) 約(맺을 약) 款(조목 관)",
            "pronunciation": "디에우 코안 바오 히엠",
            "meaningKo": "보험계약의 내용을 미리 정형화한 계약 조건. 통역 시 'điều khoản'은 조항, 'bảo hiểm'은 보험을 의미하며, 약관의 법적 구속력과 해석 원칙을 명확히 전달해야 함. 약관의 불명확한 부분은 작성자(보험사)에게 불리하게 해석되는 원칙과 설명의무 위반 시 효과를 정확히 안내하고, 약관 변경 시 계약자 동의 절차를 명시 필요.",
            "meaningVi": "Điều kiện hợp đồng đã được chuẩn hóa trước về nội dung của hợp đồng bảo hiểm.",
            "context": "보험계약법, 약관규제법",
            "culturalNote": "한국은 약관규제법으로 불공정 조항 통제가 엄격하고 금융감독원의 표준약관 승인제도가 있으나, 베트남은 약관 규제가 상대적으로 느슨함. 한국에서는 약관 교부·설명 의무 위반 시 민·형사 책임이 있어 통역 시 약관 설명의무의 법적 중요성을 강조해야 함.",
            "commonMistakes": [
                {
                    "mistake": "hợp đồng bảo hiểm (보험 계약)",
                    "correction": "điều khoản bảo hiểm (보험약관)",
                    "explanation": "계약(hợp đồng)은 개별 합의, 약관(điều khoản)은 정형화된 조건"
                },
                {
                    "mistake": "quy định bảo hiểm (보험 규정)",
                    "correction": "điều khoản bảo hiểm (보험약관)",
                    "explanation": "'quy định'은 법령상 규정, 약관은 계약상 조건"
                },
                {
                    "mistake": "nội dung bảo hiểm (보험 내용)",
                    "correction": "điều khoản bảo hiểm (보험약관)",
                    "explanation": "일반적 내용보다는 법률 용어인 '약관' 사용이 정확"
                }
            ],
            "examples": [
                {
                    "ko": "보험약관을 꼼꼼히 읽어보시고 서명하세요.",
                    "vi": "Hãy đọc kỹ điều khoản bảo hiểm trước khi ký.",
                    "situation": "onsite"
                },
                {
                    "ko": "보험약관에 명시되지 않은 사항은 상법을 따릅니다.",
                    "vi": "Các vấn đề không được quy định trong điều khoản bảo hiểm sẽ tuân theo Luật thương mại.",
                    "situation": "formal"
                },
                {
                    "ko": "보험약관 변경 시 계약자의 서면 동의가 필요합니다.",
                    "vi": "Khi thay đổi điều khoản bảo hiểm cần có sự đồng ý bằng văn bản của bên mua bảo hiểm.",
                    "situation": "formal"
                }
            ],
            "relatedTerms": ["면책조항", "보험금청구", "보험모집"]
        },
        {
            "slug": "mo-gioi-bao-hiem",
            "korean": "보험모집",
            "vietnamese": "Môi giới bảo hiểm",
            "hanja": "保險募集",
            "hanjaReading": "保(지킬 보) 險(험할 험) 募(모을 모) 集(모을 집)",
            "pronunciation": "머이 지어이 바오 히엠",
            "meaningKo": "보험계약 체결을 중개하거나 대리하는 영업 행위. 통역 시 'môi giới'는 중개를 의미하며, 보험설계사·대리점·중개사의 법적 지위 차이를 명확히 구분해야 함. 불완전판매 방지를 위한 설명의무와 적합성 원칙을 정확히 전달하고, 모집 수수료 체계와 위법 모집 시 처벌(등록취소, 벌금) 내용을 명시 필요.",
            "meaningVi": "Hoạt động kinh doanh trung gian hoặc đại diện cho việc ký kết hợp đồng bảo hiểm.",
            "context": "보험업법, 금융소비자보호법",
            "culturalNote": "한국은 보험모집인 등록제도와 교육 의무가 엄격하고 금융소비자보호법으로 불완전판매 책임이 강화되었으나, 베트남은 모집인 관리 체계가 발달 단계. 한국에서는 설명의무 위반 시 손해배상 책임이 있어 통역 시 모집인의 법적 책임 범위를 명확히 설명해야 함.",
            "commonMistakes": [
                {
                    "mistake": "bán bảo hiểm (보험 판매)",
                    "correction": "môi giới bảo hiểm (보험모집)",
                    "explanation": "'bán'은 일반 판매, 모집은 중개·대리 행위로 법적 성격이 다름"
                },
                {
                    "mistake": "giới thiệu bảo hiểm (보험 소개)",
                    "correction": "môi giới bảo hiểm (보험모집)",
                    "explanation": "단순 소개가 아닌 계약 체결 중개 행위를 의미"
                },
                {
                    "mistake": "tư vấn bảo hiểm (보험 상담)",
                    "correction": "môi giới bảo hiểm (보험모집)",
                    "explanation": "상담은 부분 행위, 모집은 계약 체결까지 포함하는 전체 영업 행위"
                }
            ],
            "examples": [
                {
                    "ko": "보험모집인은 상품 설명의무를 충실히 이행해야 합니다.",
                    "vi": "Người môi giới bảo hiểm phải thực hiện đầy đủ nghĩa vụ giải thích về sản phẩm.",
                    "situation": "formal"
                },
                {
                    "ko": "무등록 보험모집 행위는 5년 이하 징역에 처합니다.",
                    "vi": "Hành vi môi giới bảo hiểm không đăng ký bị phạt tù đến 5 năm.",
                    "situation": "formal"
                },
                {
                    "ko": "보험모집 수수료는 계약 유지율에 따라 차등 지급됩니다.",
                    "vi": "Hoa hồng môi giới bảo hiểm được chi trả theo tỷ lệ duy trì hợp đồng.",
                    "situation": "onsite"
                }
            ],
            "relatedTerms": ["보험약관", "보험분쟁", "보험규제"]
        },
        {
            "slug": "tranh-chap-bao-hiem",
            "korean": "보험분쟁",
            "vietnamese": "Tranh chấp bảo hiểm",
            "hanja": "保險紛爭",
            "hanjaReading": "保(지킬 보) 險(험할 험) 紛(어지러울 분) 爭(다툴 쟁)",
            "pronunciation": "짱 잡 바오 히엠",
            "meaningKo": "보험계약 해석, 보험금 지급, 면책 여부 등을 둘러싼 당사자 간 법적 다툼. 통역 시 'tranh chấp'은 분쟁을 의미하며, 조정·중재·소송의 단계별 해결 절차를 구체적으로 설명해야 함. 금융감독원 분쟁조정제도(한국)와 베트남 보험협회 조정제도의 차이를 명확히 하고, 소송 전 조정 전치주의 적용 여부와 조정 결과의 법적 효력을 정확히 전달 필요.",
            "meaningVi": "Tranh chấp pháp lý giữa các bên về việc giải thích hợp đồng bảo hiểm, chi trả tiền bảo hiểm, áp dụng điều khoản miễn trách nhiệm, v.v.",
            "context": "보험계약법, 민사소송법, 중재법",
            "culturalNote": "한국은 금융감독원 금융분쟁조정위원회의 조정 제도가 활성화되어 있고 조정 결과가 재판상 화해와 동일한 효력이 있으나, 베트남은 법원 소송 중심. 한국에서는 소액(2천만원 이하) 분쟁은 조정 전치주의가 적용되어 통역 시 강제조정 절차를 명확히 설명해야 함.",
            "commonMistakes": [
                {
                    "mistake": "kiện tụng bảo hiểm (보험 소송)",
                    "correction": "tranh chấp bảo hiểm (보험분쟁)",
                    "explanation": "소송(kiện tụng)은 분쟁 해결 수단 중 하나, 분쟁(tranh chấp)이 포괄 개념"
                },
                {
                    "mistake": "xung đột bảo hiểm (보험 갈등)",
                    "correction": "tranh chấp bảo hiểm (보험분쟁)",
                    "explanation": "'xung đột'은 일반 갈등, 'tranh chấp'은 법적 분쟁"
                },
                {
                    "mistake": "khiếu nại bảo hiểm (보험 민원)",
                    "correction": "tranh chấp bảo hiểm (보험분쟁)",
                    "explanation": "민원(khiếu nại)은 불만 제기, 분쟁은 법적 다툼"
                }
            ],
            "examples": [
                {
                    "ko": "보험분쟁이 발생하면 먼저 금융감독원에 조정을 신청하세요.",
                    "vi": "Khi xảy ra tranh chấp bảo hiểm, hãy nộp đơn hòa giải lên Cơ quan Giám sát Tài chính trước.",
                    "situation": "formal"
                },
                {
                    "ko": "보험금 지급 거부를 둘러싼 보험분쟁이 증가하고 있습니다.",
                    "vi": "Tranh chấp bảo hiểm liên quan đến việc từ chối chi trả tiền bảo hiểm đang gia tăng.",
                    "situation": "formal"
                },
                {
                    "ko": "조정이 실패하면 법원에 소송을 제기할 수 있습니다.",
                    "vi": "Nếu hòa giải không thành công, có thể khởi kiện tại tòa án.",
                    "situation": "onsite"
                }
            ],
            "relatedTerms": ["보험금청구", "면책조항", "보험모집"]
        },
        {
            "slug": "giam-sat-bao-hiem",
            "korean": "보험규제",
            "vietnamese": "Giám sát bảo hiểm",
            "hanja": "保險規制",
            "hanjaReading": "保(지킬 보) 險(험할 험) 規(법 규) 制(만들 제)",
            "pronunciation": "잠 샛 바오 히엠",
            "meaningKo": "보험업의 건전성 확보와 소비자 보호를 위해 정부가 보험회사에 가하는 각종 법적 통제. 통역 시 'giám sát'은 감독을 의미하며, 지급여력비율(RBC), 자산운용 규제, 상품 인가제 등 구체적 규제 내용을 명확히 전달해야 함. 한국 금융위원회·금융감독원의 2원 체계와 베트남 재무부 산하 보험감독청의 1원 체계 차이를 설명하고, 규제 위반 시 제재 수위를 정확히 안내 필요.",
            "meaningVi": "Các biện pháp kiểm soát pháp lý mà chính phủ áp dụng đối với các công ty bảo hiểm nhằm đảm bảo tính lành mạnh của ngành bảo hiểm và bảo vệ người tiêu dùng.",
            "context": "보험업법, 금융규제법",
            "culturalNote": "한국은 위험기준 자기자본(RBC) 비율 등 정량 규제가 엄격하고 소비자 보호 규제가 강화되는 추세나, 베트남은 규제 체계가 발전 단계로 유예 기간이 긴 편. 한국에서는 상품 사전승인제가 폐지되고 사후보고제로 전환되어 통역 시 규제 패러다임 변화를 설명해야 함.",
            "commonMistakes": [
                {
                    "mistake": "quản lý bảo hiểm (보험 관리)",
                    "correction": "giám sát bảo hiểm (보험규제)",
                    "explanation": "'quản lý'는 일반 관리, 'giám sát'은 감독 기관의 공적 규제"
                },
                {
                    "mistake": "kiểm tra bảo hiểm (보험 검사)",
                    "correction": "giám sát bảo hiểm (보험규제)",
                    "explanation": "검사는 규제 수단 중 하나, 규제가 포괄 개념"
                },
                {
                    "mistake": "luật bảo hiểm (보험법)",
                    "correction": "giám sát bảo hiểm (보험규제)",
                    "explanation": "법(luật)은 입법, 규제(giám sát)는 행정 감독"
                }
            ],
            "examples": [
                {
                    "ko": "보험규제가 강화되면서 자본금 요건이 상향되었습니다.",
                    "vi": "Khi giám sát bảo hiểm được tăng cường, yêu cầu về vốn điều lệ đã được nâng cao.",
                    "situation": "formal"
                },
                {
                    "ko": "보험회사는 매 분기 지급여력비율을 금융감독원에 보고해야 합니다.",
                    "vi": "Các công ty bảo hiểm phải báo cáo tỷ lệ khả năng thanh toán cho Cơ quan Giám sát Tài chính hàng quý.",
                    "situation": "formal"
                },
                {
                    "ko": "보험규제 위반 시 영업정지 처분을 받을 수 있습니다.",
                    "vi": "Nếu vi phạm giám sát bảo hiểm có thể bị đình chỉ hoạt động kinh doanh.",
                    "situation": "onsite"
                }
            ],
            "relatedTerms": ["보험계리", "재보험", "보험분쟁"]
        },
        {
            "slug": "bao-hiem-xa-hoi",
            "korean": "사회보험",
            "vietnamese": "Bảo hiểm xã hội",
            "hanja": "社會保險",
            "hanjaReading": "社(모일 사) 會(모일 회) 保(지킬 보) 險(험할 험)",
            "pronunciation": "바오 히엠 싸 호이",
            "meaningKo": "국가가 법률로 강제하는 공적 보험 제도로 국민연금, 건강보험, 고용보험, 산재보험 등을 포괄. 통역 시 'bảo hiểm xã hội'는 사회보험을 의미하며, 한국의 4대보험 체계와 베트남의 3대보험(사회보험, 건강보험, 실업보험) 체계 차이를 명확히 구분해야 함. 강제가입 대상과 보험료율, 급여 수준의 차이를 정확히 전달하고, 외국인 근로자의 가입 의무와 환급 규정을 상세히 안내 필요.",
            "meaningVi": "Chế độ bảo hiểm công cộng do nhà nước bắt buộc theo luật, bao gồm bảo hiểm hưu trí, bảo hiểm y tế, bảo hiểm thất nghiệp, bảo hiểm tai nạn lao động, v.v.",
            "context": "사회보험법, 노동법",
            "culturalNote": "한국은 국민연금(노령), 건강보험(질병), 고용보험(실업), 산재보험(재해)으로 세분화되어 있으나 베트남은 사회보험에 노령·질병·출산·산재·사망을 통합하고 별도로 건강보험과 실업보험 운영. 한국에서는 외국인도 1년 이상 근무 시 국민연금 가입 의무가 있어 통역 시 외국인 적용 범위 차이를 명확히 설명해야 함.",
            "commonMistakes": [
                {
                    "mistake": "bảo hiểm nhà nước (국가 보험)",
                    "correction": "bảo hiểm xã hội (사회보험)",
                    "explanation": "국가보험은 일반 표현, 사회보험이 법률 용어"
                },
                {
                    "mistake": "bảo hiểm công (공공 보험)",
                    "correction": "bảo hiểm xã hội (사회보험)",
                    "explanation": "'công'은 공공 일반, 'xã hội'는 사회보험 제도 특정"
                },
                {
                    "mistake": "bảo hiểm bắt buộc (강제 보험)",
                    "correction": "bảo hiểm xã hội (사회보험)",
                    "explanation": "강제보험은 특성 설명, 사회보험이 제도 명칭"
                }
            ],
            "examples": [
                {
                    "ko": "사업주는 근로자를 채용하면 즉시 사회보험에 가입시켜야 합니다.",
                    "vi": "Người sử dụng lao động phải đăng ký bảo hiểm xã hội ngay khi tuyển dụng người lao động.",
                    "situation": "formal"
                },
                {
                    "ko": "사회보험료는 사업주와 근로자가 분담하여 납부합니다.",
                    "vi": "Phí bảo hiểm xã hội được người sử dụng lao động và người lao động cùng đóng góp.",
                    "situation": "formal"
                },
                {
                    "ko": "15년 이상 사회보험에 가입하면 연금 수급 자격이 생깁니다.",
                    "vi": "Khi tham gia bảo hiểm xã hội từ 15 năm trở lên sẽ có quyền hưởng lương hưu.",
                    "situation": "onsite"
                }
            ],
            "relatedTerms": ["보험규제", "보험약관", "보험분쟁"]
        }
    ]
    return terms

def main():
    data, file_path = load_existing_terms()
    existing_slugs = {t['slug'] for t in data}
    new_terms = create_legal_terms()
    filtered = [t for t in new_terms if t['slug'] not in existing_slugs]
    data.extend(filtered)
    with open(file_path, 'w', encoding='utf-8') as f:
        json.dump(data, f, ensure_ascii=False, indent=2)
    print(f"Added {len(filtered)} terms. Total: {len(data)}")

if __name__ == '__main__':
    main()
