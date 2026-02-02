#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import json
import os

# Construction Guarantees/Bidding Theme - 10 Terms

new_terms = [
    {
        "slug": "bao-lanh-du-thau",
        "korean": "입찰보증",
        "vietnamese": "bảo lãnh dự thầu",
        "hanja": "入札保證",
        "hanjaReading": "入(들 입) + 札(찰 찰) + 保(지킬 보) + 證(증거 증)",
        "pronunciation": "잎찰보쯩",
        "meaningKo": "공사 입찰 시 입찰자가 입찰 후 계약 체결을 보증하기 위해 제출하는 보증서입니다. 베트남에서는 'bảo lãnh dự thầu'라고 하며, 통역 시 주의할 점은 이 보증금이 입찰 포기 시 몰수된다는 것을 명확히 전달해야 합니다. 한국은 대개 입찰금액의 5% 수준이지만 베트남은 프로젝트에 따라 1-5%로 차이가 있어 비율을 정확히 확인해야 합니다. 입찰 단계에서 발주자의 재정적 리스크를 줄이기 위한 필수 서류이며, 보증 기관(은행, 보험사)이 발행합니다.",
        "meaningVi": "Bảo lãnh dự thầu là giấy bảo lãnh do nhà thầu nộp khi tham gia đấu thầu để đảm bảo rằng họ sẽ ký kết hợp đồng nếu trúng thầu. Đây là một yêu cầu bắt buộc trong hầu hết các dự án xây dựng ở Việt Nam. Giá trị bảo lãnh thường dao động từ 1-5% giá trị gói thầu và sẽ bị mất nếu nhà thầu từ chối ký hợp đồng sau khi trúng thầu. Bảo lãnh được cấp bởi ngân hàng hoặc công ty bảo hiểm có uy tín.",
        "context": "입찰 서류 준비 단계, 발주처와의 계약 협상, 금융기관 보증서 발급 업무",
        "culturalNote": "한국은 입찰보증을 현금, 보증보험, 은행보증 등 다양한 형태로 인정하지만 베트남은 주로 은행보증서(bảo lãnh ngân hàng)를 요구합니다. 또한 베트남에서는 외국 기업이 입찰 시 베트남 현지 은행의 보증서를 요구하는 경우가 많아 사전 준비가 필수입니다. 보증 기간도 한국보다 길게 설정되는 경향이 있으며, 입찰 공고일로부터 계약 체결 후 일정 기간까지 유효해야 합니다.",
        "commonMistakes": [
            {
                "mistake": "bảo hiểm dự thầu",
                "correction": "bảo lãnh dự thầu",
                "explanation": "'bảo hiểm'은 보험을 의미하지만, 입찰보증은 '보증(bảo lãnh)'의 개념이므로 혼동하지 말아야 합니다."
            },
            {
                "mistake": "입찰금",
                "correction": "입찰보증 또는 입찰보증금",
                "explanation": "입찰금은 입찰가격을 의미할 수 있어 혼동될 수 있으므로 '입찰보증'이라고 명확히 표현해야 합니다."
            },
            {
                "mistake": "tiền đặt cọc dự thầu",
                "correction": "bảo lãnh dự thầu",
                "explanation": "'tiền đặt cọc'은 단순 보증금이지만 'bảo lãnh'은 은행/보험사가 발행하는 공식 보증서로 법적 성격이 다릅니다."
            }
        ],
        "examples": [
            {
                "ko": "입찰에 참여하려면 공사금액의 5% 입찰보증을 제출해야 합니다.",
                "vi": "Để tham gia đấu thầu, bạn phải nộp bảo lãnh dự thầu trị giá 5% giá trị công trình.",
                "situation": "formal"
            },
            {
                "ko": "입찰보증 유효기간이 다음 주에 만료되니까 연장 신청해주세요.",
                "vi": "Thời hạn hiệu lực của bảo lãnh dự thầu sẽ hết vào tuần tới, vui lòng làm thủ tục gia hạn.",
                "situation": "onsite"
            },
            {
                "ko": "낙찰자가 계약을 거부해서 입찰보증이 몰수되었습니다.",
                "vi": "Nhà thầu trúng thầu đã từ chối ký hợp đồng nên bảo lãnh dự thầu bị tịch thu.",
                "situation": "formal"
            }
        ],
        "relatedTerms": ["bao-lanh-thuc-hien", "ho-so-du-thau", "trung-thau"]
    },
    {
        "slug": "bao-lanh-thuc-hien",
        "korean": "이행보증",
        "vietnamese": "bảo lãnh thực hiện",
        "hanja": "履行保證",
        "hanjaReading": "履(밟을 이) + 行(다닐 행) + 保(지킬 보) + 證(증거 증)",
        "pronunciation": "바오 란 턱 히엔",
        "meaningKo": "계약자가 공사 계약 조건을 충실히 이행할 것을 보증하는 서류로, 베트남어로는 'bảo lãnh thực hiện' 또는 'bảo lãnh hợp đồng'이라고 합니다. 통역 시 주의할 점은 이 보증서가 계약 체결 후 즉시 제출되며 공사 완료 시점까지 유효하다는 것을 명확히 해야 합니다. 한국과 베트남 모두 계약금액의 10% 수준이 일반적이지만, 베트남에서는 국가 프로젝트의 경우 더 높은 비율을 요구할 수 있습니다. 계약 불이행 시 발주자는 이 보증금을 청구할 수 있으며, 이는 공사 품질과 일정 준수를 담보하는 핵심 장치입니다.",
        "meaningVi": "Bảo lãnh thực hiện (hay bảo lãnh hợp đồng) là giấy bảo lãnh do nhà thầu nộp sau khi ký hợp đồng để đảm bảo việc thực hiện đầy đủ các nghĩa vụ theo hợp đồng xây dựng. Thường có giá trị 10% giá trị hợp đồng và có hiệu lực từ ngày ký hợp đồng đến khi nghiệm thu hoàn thành công trình. Nếu nhà thầu vi phạm hợp đồng, chủ đầu tư có quyền yêu cầu ngân hàng chi trả số tiền bảo lãnh để bù đắp thiệt hại.",
        "context": "계약 체결 단계, 공사 진행 중 발주처 보고, 준공 후 보증 반환 절차",
        "culturalNote": "한국에서는 이행보증을 '계약보증금' 또는 '계약이행보증'이라고도 부르며, 베트남에서는 'bảo lãnh hợp đồng'과 'bảo lãnh thực hiện'을 혼용합니다. 베트남 현장에서는 공사 지연이나 품질 문제 발생 시 이 보증금 청구가 한국보다 더 엄격하게 적용되는 경향이 있습니다. 또한 베트남에서는 국영 프로젝트의 경우 이행보증 외에도 추가 담보를 요구하는 경우가 많아 계약 전 정확한 확인이 필요합니다.",
        "commonMistakes": [
            {
                "mistake": "bảo lãnh công trình",
                "correction": "bảo lãnh thực hiện",
                "explanation": "'bảo lãnh công trình'은 공사 전체에 대한 보증으로 오해될 수 있으나, 정확한 용어는 'bảo lãnh thực hiện'입니다."
            },
            {
                "mistake": "계약금",
                "correction": "이행보증 또는 이행보증금",
                "explanation": "계약금(tiền đặt cọc)은 계약 체결 시 지불하는 금액이고, 이행보증은 계약 이행을 담보하는 보증서로 개념이 다릅니다."
            },
            {
                "mistake": "bảo lãnh sau khi hoàn thành",
                "correction": "bảo lãnh thực hiện (có hiệu lực đến khi hoàn thành)",
                "explanation": "이행보증은 완료 후가 아니라 계약 체결부터 완료 시점까지 유효한 보증입니다."
            }
        ],
        "examples": [
            {
                "ko": "계약 체결 후 7일 내에 계약금액의 10% 이행보증서를 제출하세요.",
                "vi": "Sau khi ký hợp đồng, trong vòng 7 ngày phải nộp bảo lãnh thực hiện trị giá 10% giá trị hợp đồng.",
                "situation": "formal"
            },
            {
                "ko": "공사가 지연되면 발주처에서 이행보증을 청구할 수 있습니다.",
                "vi": "Nếu công trình bị chậm tiến độ, chủ đầu tư có thể yêu cầu chi trả bảo lãnh thực hiện.",
                "situation": "onsite"
            },
            {
                "ko": "준공 검사가 완료되어 이행보증서를 반환받았습니다.",
                "vi": "Công trình đã được nghiệm thu xong nên chúng tôi đã nhận lại bảo lãnh thực hiện.",
                "situation": "formal"
            }
        ],
        "relatedTerms": ["bao-lanh-du-thau", "bao-lanh-bao-hanh", "hop-dong-thi-cong"]
    },
    {
        "slug": "bao-lanh-tam-ung",
        "korean": "선급금보증",
        "vietnamese": "bảo lãnh tạm ứng",
        "hanja": "先給金保證",
        "hanjaReading": "先(먼저 선) + 給(줄 급) + 金(쇠 금) + 保(지킬 보) + 證(증거 증)",
        "pronunciation": "바오 란 땀 응",
        "meaningKo": "발주자가 시공사에게 공사 착수 전 또는 공사 중 선금을 지급할 때, 시공사가 이를 부당하게 사용하지 않고 공사에 투입할 것을 보증하는 서류입니다. 베트남어로는 'bảo lãnh tạm ứng'이라고 하며, 통역 시 주의할 점은 선급금 비율과 정산 방식을 명확히 전달해야 합니다. 한국에서는 계약금액의 30-50%를 선급금으로 지급하는 경우가 많지만, 베트남에서는 20-30% 수준이 일반적입니다. 선급금보증서는 선급금 전액에 대해 발행되며, 공사 진행에 따라 선급금이 정산되면 보증액도 감액됩니다.",
        "meaningVi": "Bảo lãnh tạm ứng là giấy bảo lãnh do nhà thầu cung cấp khi nhận tiền tạm ứng từ chủ đầu tư để đảm bảo số tiền này sẽ được sử dụng đúng mục đích xây dựng. Giá trị bảo lãnh bằng với số tiền tạm ứng (thường 20-30% giá trị hợp đồng) và sẽ được giảm dần theo tiến độ thanh toán. Nếu nhà thầu sử dụng sai mục đích hoặc không hoàn thành công việc, chủ đầu tư có quyền thu hồi tiền tạm ứng thông qua bảo lãnh này.",
        "context": "선급금 지급 협상, 자금 관리 회의, 공사비 정산 업무",
        "culturalNote": "한국에서는 선급금보증을 '선수금보증'이라고도 부르며, 대형 공사에서 자금 유동성을 위해 흔히 사용됩니다. 베트남에서는 선급금 비율이 한국보다 낮고, 외국 기업의 경우 선급금 지급이 까다로운 편입니다. 또한 베트남에서는 선급금을 받기 위해 별도의 승인 절차가 필요한 경우가 많아 계약서에 명확히 규정해야 합니다. 선급금 정산 방식도 한국과 베트남이 다를 수 있어 통역 시 세부 조건을 정확히 확인해야 합니다.",
        "commonMistakes": [
            {
                "mistake": "bảo lãnh tiền ứng trước",
                "correction": "bảo lãnh tạm ứng",
                "explanation": "'tiền ứng trước'는 구어적 표현이고, 공식 용어는 'tạm ứng' 또는 'tiền tạm ứng'입니다."
            },
            {
                "mistake": "계약금보증",
                "correction": "선급금보증",
                "explanation": "계약금은 계약 체결 시 지급하는 금액이고, 선급금은 공사 착수 전후에 지급하는 공사비의 일부로 개념이 다릅니다."
            },
            {
                "mistake": "bảo lãnh thanh toán trước",
                "correction": "bảo lãnh tạm ứng",
                "explanation": "'thanh toán trước'는 선불을 의미하지만, 선급금은 'tạm ứng'이라는 공식 용어를 사용해야 합니다."
            }
        ],
        "examples": [
            {
                "ko": "계약금액의 30%를 선급금으로 지급하니 선급금보증서를 제출해주세요.",
                "vi": "Chúng tôi sẽ chi trả 30% giá trị hợp đồng làm tiền tạm ứng, vui lòng nộp bảo lãnh tạm ứng.",
                "situation": "formal"
            },
            {
                "ko": "이번 달 기성금 받으면 선급금보증 금액이 줄어들어요.",
                "vi": "Khi nhận tiền thanh toán khối lượng tháng này, giá trị bảo lãnh tạm ứng sẽ giảm xuống.",
                "situation": "onsite"
            },
            {
                "ko": "선급금을 공사비로 사용하지 않으면 보증금이 청구됩니다.",
                "vi": "Nếu không sử dụng tiền tạm ứng đúng mục đích thi công, bảo lãnh sẽ bị yêu cầu chi trả.",
                "situation": "formal"
            }
        ],
        "relatedTerms": ["bao-lanh-thuc-hien", "hop-dong-thi-cong", "gia-du-thau"]
    },
    {
        "slug": "bao-lanh-bao-hanh",
        "korean": "하자보증",
        "vietnamese": "bảo lãnh bảo hành",
        "hanja": "瑕疵保證",
        "hanjaReading": "瑕(옥에티 하) + 疵(흠 자) + 保(지킬 보) + 證(증거 증)",
        "pronunciation": "바오 란 바오 한",
        "meaningKo": "공사 완료 후 하자보수 기간 동안 발생할 수 있는 하자를 시공사가 책임지고 보수할 것을 보증하는 서류입니다. 베트남어로는 'bảo lãnh bảo hành'이라고 하며, 통역 시 주의할 점은 하자보수 기간과 범위를 명확히 전달해야 합니다. 한국에서는 건축물 종류에 따라 2-10년의 하자보수 기간이 있지만, 베트남에서는 일반적으로 1-2년이며 건물 유형에 따라 최대 5년까지 연장될 수 있습니다. 하자보증금은 통상 계약금액의 3-5% 수준이며, 하자보수 기간 만료 후 반환됩니다. 하자 발생 시 발주자는 이 보증금으로 보수 비용을 충당할 수 있습니다.",
        "meaningVi": "Bảo lãnh bảo hành là giấy bảo lãnh do nhà thầu cung cấp sau khi hoàn thành công trình để đảm bảo sẽ khắc phục các lỗi kỹ thuật phát sinh trong thời gian bảo hành. Thời gian bảo hành thường từ 1-2 năm (có thể lên đến 5 năm tùy loại công trình) và giá trị bảo lãnh thường bằng 3-5% giá trị hợp đồng. Nếu nhà thầu không thực hiện nghĩa vụ bảo hành, chủ đầu tư có quyền sử dụng bảo lãnh này để thuê đơn vị khác sửa chữa.",
        "context": "준공 단계, 하자보수 기간 관리, 인수인계 절차",
        "culturalNote": "한국에서는 하자보증을 '하자보수보증금'이라고도 하며, 건축법에 따라 의무 기간이 정해져 있습니다. 베트남에서는 하자보수 기간이 한국보다 짧고 강제력이 약한 편이지만, 최근에는 법규가 강화되는 추세입니다. 베트남에서는 하자의 범위를 계약서에 명확히 정의하지 않으면 분쟁이 발생할 수 있으므로 주의가 필요합니다. 또한 베트남에서는 하자보증서 대신 현금을 예치하는 경우도 있어 계약 시 협의가 필요합니다.",
        "commonMistakes": [
            {
                "mistake": "bảo lãnh sửa chữa",
                "correction": "bảo lãnh bảo hành",
                "explanation": "'sửa chữa'는 일반적인 수리를 의미하지만, 하자보수는 'bảo hành'이라는 공식 용어를 사용해야 합니다."
            },
            {
                "mistake": "하자보수금",
                "correction": "하자보증 또는 하자보수보증금",
                "explanation": "하자보수금은 실제 보수에 드는 비용이고, 하자보증은 그것을 담보하는 보증금으로 개념이 다릅니다."
            },
            {
                "mistake": "bảo hành công trình",
                "correction": "bảo lãnh bảo hành",
                "explanation": "'bảo hành công trình'은 하자보수 행위 자체를 의미하고, 'bảo lãnh bảo hành'은 그것을 보증하는 금융 문서입니다."
            }
        ],
        "examples": [
            {
                "ko": "준공 후 2년간 하자보수 책임이 있으니 하자보증서를 제출하세요.",
                "vi": "Sau khi hoàn thành công trình, bạn có trách nhiệm bảo hành trong 2 năm nên phải nộp bảo lãnh bảo hành.",
                "situation": "formal"
            },
            {
                "ko": "하자보수 기간이 지나서 하자보증금을 돌려받았습니다.",
                "vi": "Thời gian bảo hành đã hết nên chúng tôi đã nhận lại tiền bảo lãnh bảo hành.",
                "situation": "onsite"
            },
            {
                "ko": "균열이 발생했는데 시공사가 보수를 안 해서 하자보증금으로 처리했어요.",
                "vi": "Xuất hiện vết nứt nhưng nhà thầu không sửa chữa nên chúng tôi đã dùng bảo lãnh bảo hành để xử lý.",
                "situation": "informal"
            }
        ],
        "relatedTerms": ["bao-lanh-thuc-hien", "hop-dong-thi-cong", "xet-thau"]
    },
    {
        "slug": "ho-so-du-thau",
        "korean": "입찰서류",
        "vietnamese": "hồ sơ dự thầu",
        "hanja": "入札書類",
        "hanjaReading": "入(들 입) + 札(찰 찰) + 書(글 서) + 類(무리 류)",
        "pronunciation": "호 소 주 타우",
        "meaningKo": "공사 입찰에 참여하기 위해 제출하는 모든 서류를 총칭하는 용어로, 베트남어로는 'hồ sơ dự thầu'라고 합니다. 통역 시 주의할 점은 한국과 베트남의 입찰서류 구성이 다르므로 필수 서류 목록을 정확히 확인해야 합니다. 일반적으로 입찰신청서, 기술제안서, 가격제안서, 입찰보증서, 사업자등록증, 면허증, 실적증명서, 재무제표 등이 포함됩니다. 베트남에서는 서류의 공증과 번역본 제출을 요구하는 경우가 많아 준비 기간이 더 길어질 수 있습니다. 서류 누락이나 오류는 입찰 자격 상실로 이어질 수 있어 철저한 검토가 필요합니다.",
        "meaningVi": "Hồ sơ dự thầu là toàn bộ tài liệu mà nhà thầu phải nộp khi tham gia đấu thầu công trình xây dựng. Bao gồm đơn dự thầu, đề xuất kỹ thuật, đề xuất giá, bảo lãnh dự thầu, giấy phép kinh doanh, giấy phép hoạt động xây dựng, chứng chỉ năng lực, báo cáo tài chính và các tài liệu khác theo yêu cầu của chủ đầu tư. Hồ sơ phải được chuẩn bị đầy đủ, chính xác và nộp đúng thời hạn, nếu thiếu hoặc sai sót sẽ bị loại ngay từ vòng sơ tuyển.",
        "context": "입찰 공고 검토, 서류 준비 회의, 입찰 제출 절차",
        "culturalNote": "한국에서는 전자입찰시스템(나라장터)을 통해 온라인으로 제출하는 것이 일반적이지만, 베트남에서는 아직도 종이 서류를 요구하는 경우가 많습니다. 베트남에서는 외국 기업이 입찰할 때 베트남어 번역본과 공증을 요구하므로 시간과 비용이 추가로 발생합니다. 또한 베트남에서는 입찰서류의 봉인과 제출 방식에 대한 규정이 엄격하여 절차를 정확히 따르지 않으면 무효 처리될 수 있습니다.",
        "commonMistakes": [
            {
                "mistake": "giấy tờ dự thầu",
                "correction": "hồ sơ dự thầu",
                "explanation": "'giấy tờ'는 일반적인 서류를 의미하지만, 입찰서류는 'hồ sơ'라는 공식 용어를 사용합니다."
            },
            {
                "mistake": "입찰문서",
                "correction": "입찰서류",
                "explanation": "입찰문서는 입찰 공고나 규정을 의미할 수 있어, 응찰자가 제출하는 것은 '입찰서류'라고 해야 명확합니다."
            },
            {
                "mistake": "tài liệu đấu thầu",
                "correction": "hồ sơ dự thầu",
                "explanation": "'tài liệu đấu thầu'는 입찰 관련 자료 전반을 의미하지만, 응찰자가 제출하는 것은 'hồ sơ dự thầu'입니다."
            }
        ],
        "examples": [
            {
                "ko": "입찰서류는 다음 주 금요일 오후 5시까지 제출해야 합니다.",
                "vi": "Hồ sơ dự thầu phải được nộp trước 5 giờ chiều thứ Sáu tuần tới.",
                "situation": "formal"
            },
            {
                "ko": "입찰서류에 실적증명서가 빠져서 탈락했어요.",
                "vi": "Hồ sơ dự thầu thiếu chứng chỉ năng lực nên bị loại.",
                "situation": "onsite"
            },
            {
                "ko": "입찰서류를 두 부 준비해서 봉인해주세요.",
                "vi": "Vui lòng chuẩn bị hai bộ hồ sơ dự thầu và niêm phong lại.",
                "situation": "formal"
            }
        ],
        "relatedTerms": ["bao-lanh-du-thau", "gia-du-thau", "mo-thau"]
    },
    {
        "slug": "gia-du-thau",
        "korean": "입찰가격",
        "vietnamese": "giá dự thầu",
        "hanja": "入札價格",
        "hanjaReading": "入(들 입) + 札(찰 찰) + 價(값 가) + 格(격식 격)",
        "pronunciation": "자 주 타우",
        "meaningKo": "입찰 참여 시 제출하는 공사 가격으로, 베트남어로는 'giá dự thầu'라고 합니다. 통역 시 주의할 점은 입찰가격이 예정가격, 원가, 최저가 등 여러 개념과 혼동될 수 있으므로 명확히 구분해야 합니다. 입찰가격은 직접공사비, 간접공사비, 일반관리비, 이윤 등을 포함한 총액이며, 부가가치세 포함 여부를 반드시 확인해야 합니다. 한국에서는 최저가 낙찰제와 적격심사제가 있지만, 베트남에서는 '가격 대비 품질(giá và chất lượng)' 방식이 일반적입니다. 입찰가격은 공사 수주의 핵심 경쟁 요소이므로 원가 계산과 전략적 가격 책정이 중요합니다.",
        "meaningVi": "Giá dự thầu là mức giá mà nhà thầu đề xuất để thực hiện công trình trong hồ sơ dự thầu. Giá này bao gồm chi phí trực tiếp, chi phí gián tiếp, chi phí quản lý và lợi nhuận. Giá dự thầu phải cạnh tranh nhưng vẫn đảm bảo khả năng thực hiện chất lượng công trình. Tại Việt Nam, giá dự thầu thường được đánh giá kết hợp với năng lực kỹ thuật, không chỉ chọn giá thấp nhất. Giá phải được trình bày rõ ràng, có phân tích chi tiết và phù hợp với dự toán được phê duyệt.",
        "context": "입찰가 산정 회의, 원가 분석, 가격 제안서 작성",
        "culturalNote": "한국에서는 공공공사의 경우 예정가격 대비 입찰가격의 비율이 낙찰에 중요한 영향을 미치지만, 베트남에서는 기술 평가 점수와 가격 점수를 합산하여 평가하는 방식이 일반적입니다. 베트남에서는 입찰가격이 예정가격보다 낮아도 비정상적으로 낮으면(bất thường thấp) 탈락될 수 있어 적정 수준의 가격 책정이 필요합니다. 또한 베트남에서는 가격 조정 조항(điều chỉnh giá)이 계약서에 포함되는 경우가 많아 인플레이션이나 환율 변동에 대비할 수 있습니다.",
        "commonMistakes": [
            {
                "mistake": "giá đấu thầu",
                "correction": "giá dự thầu",
                "explanation": "'đấu thầu'는 입찰 행위 전체를 의미하고, 응찰자가 제시하는 가격은 'giá dự thầu'입니다."
            },
            {
                "mistake": "예정가격",
                "correction": "입찰가격",
                "explanation": "예정가격(giá dự toán)은 발주자가 정한 기준 가격이고, 입찰가격은 입찰자가 제시하는 가격으로 다릅니다."
            },
            {
                "mistake": "giá chào thầu",
                "correction": "giá dự thầu",
                "explanation": "'chào thầu'는 구어적 표현이고, 공식 용어는 'dự thầu'입니다."
            }
        ],
        "examples": [
            {
                "ko": "우리 입찰가격은 500억 원으로 예정가격보다 5% 낮습니다.",
                "vi": "Giá dự thầu của chúng tôi là 500 tỷ đồng, thấp hơn 5% so với giá dự toán.",
                "situation": "formal"
            },
            {
                "ko": "입찰가격을 너무 낮게 썼더니 원가 분석에서 탈락했어요.",
                "vi": "Giá dự thầu của chúng tôi quá thấp nên bị loại ở khâu phân tích chi phí.",
                "situation": "onsite"
            },
            {
                "ko": "입찰가격에 부가세가 포함되어 있나요?",
                "vi": "Giá dự thầu đã bao gồm thuế VAT chưa?",
                "situation": "formal"
            }
        ],
        "relatedTerms": ["ho-so-du-thau", "xet-thau", "trung-thau"]
    },
    {
        "slug": "mo-thau",
        "korean": "개찰",
        "vietnamese": "mở thầu",
        "hanja": "開札",
        "hanjaReading": "開(열 개) + 札(찰 찰)",
        "pronunciation": "머 타우",
        "meaningKo": "입찰 마감 후 제출된 입찰서류의 봉인을 개봉하여 입찰가격과 내용을 공개하는 절차로, 베트남어로는 'mở thầu'라고 합니다. 통역 시 주의할 점은 개찰이 공개적으로 진행되며 입찰 참가자들이 참관할 수 있다는 것을 명확히 전달해야 합니다. 한국에서는 전자입찰의 경우 자동으로 개찰되지만, 베트남에서는 아직도 현장에서 물리적으로 봉투를 개봉하는 경우가 많습니다. 개찰 시 입찰서류의 적격성이 먼저 검토되고, 부적격 서류는 즉시 배제됩니다. 개찰 후에는 개찰조서가 작성되어 모든 입찰자에게 공개됩니다.",
        "meaningVi": "Mở thầu là quá trình mở niêm phong hồ sơ dự thầu sau khi hết hạn nộp để công khai giá dự thầu và nội dung đề xuất của các nhà thầu. Đây là một thủ tục công khai, có sự chứng kiến của đại diện các nhà thầu tham gia và cơ quan quản lý. Trong quá trình mở thầu, ban mở thầu sẽ kiểm tra tính hợp lệ của hồ sơ (niêm phong đúng quy định, đầy đủ tài liệu) trước khi công bố giá. Sau khi mở thầu, biên bản mở thầu sẽ được lập và gửi cho tất cả nhà thầu.",
        "context": "입찰 절차 안내, 개찰 참관, 입찰 결과 확인",
        "culturalNote": "한국에서는 공공공사의 경우 나라장터를 통한 전자개찰이 일반화되어 있지만, 베트남에서는 여전히 오프라인 개찰이 많이 이루어집니다. 베트남에서는 개찰 시 모든 입찰자가 참석하여 상호 감시하는 것이 관례이며, 불참 시 이의 제기가 어려울 수 있습니다. 또한 베트남에서는 개찰과 심사가 분리되어 진행되므로 개찰 후에도 최종 낙찰자가 결정되기까지 시간이 걸립니다.",
        "commonMistakes": [
            {
                "mistake": "mở hồ sơ",
                "correction": "mở thầu",
                "explanation": "'mở hồ sơ'는 일반적인 서류 개봉이고, 입찰서류 개봉은 'mở thầu'라는 공식 용어를 사용합니다."
            },
            {
                "mistake": "입찰 개봉",
                "correction": "개찰",
                "explanation": "입찰 개봉은 구어적 표현이고, 공식 용어는 '개찰'입니다."
            },
            {
                "mistake": "mở túi dự thầu",
                "correction": "mở thầu",
                "explanation": "'mở túi'는 물리적 개봉 행위이고, 절차 전체는 'mở thầu'로 표현합니다."
            }
        ],
        "examples": [
            {
                "ko": "개찰은 내일 오전 10시에 본사 회의실에서 진행됩니다.",
                "vi": "Mở thầu sẽ diễn ra lúc 10 giờ sáng mai tại phòng họp trụ sở chính.",
                "situation": "formal"
            },
            {
                "ko": "개찰 현장에 가봤더니 우리가 최저가였어요.",
                "vi": "Khi đến hiện trường mở thầu, chúng tôi thấy giá của mình là thấp nhất.",
                "situation": "onsite"
            },
            {
                "ko": "개찰 시 서류 미비로 두 개 업체가 탈락했습니다.",
                "vi": "Khi mở thầu, hai công ty bị loại do thiếu tài liệu.",
                "situation": "formal"
            }
        ],
        "relatedTerms": ["ho-so-du-thau", "xet-thau", "trung-thau"]
    },
    {
        "slug": "xet-thau",
        "korean": "심사",
        "vietnamese": "xét thầu",
        "hanja": "審査",
        "hanjaReading": "審(살필 심) + 査(조사할 사)",
        "pronunciation": "셋 타우",
        "meaningKo": "개찰 후 제출된 입찰서류를 기술적, 재무적, 법적 측면에서 종합 평가하여 낙찰자를 선정하는 절차로, 베트남어로는 'xét thầu' 또는 'đánh giá hồ sơ dự thầu'라고 합니다. 통역 시 주의할 점은 심사 기준과 배점이 입찰공고에 명시되어 있으며, 이를 정확히 이해해야 합니다. 한국에서는 적격심사(기술능력 평가)와 가격심사를 병행하지만, 베트남에서는 '기술점수 + 가격점수' 합산 방식이 일반적입니다. 심사 항목은 기술제안서, 시공계획, 품질관리계획, 안전관리계획, 재무상태, 실적 등이 포함되며, 심사 결과는 공개됩니다.",
        "meaningVi": "Xét thầu là quá trình đánh giá hồ sơ dự thầu sau khi mở thầu để chọn nhà thầu trúng thầu. Ban xét thầu sẽ đánh giá về mặt kỹ thuật (năng lực, phương án thi công, chất lượng, tiến độ, an toàn), tài chính (báo cáo tài chính, khả năng thanh toán) và giá cả. Mỗi tiêu chí có điểm số theo quy định trong hồ sơ mời thầu. Nhà thầu có tổng điểm cao nhất (hoặc đáp ứng yêu cầu và giá thấp nhất tùy phương thức) sẽ được đề xuất trúng thầu. Kết quả xét thầu phải được công khai và các nhà thầu có quyền khiếu nại nếu thấy không công bằng.",
        "context": "심사위원회 회의, 평가 점수 산정, 낙찰자 선정",
        "culturalNote": "한국에서는 공공공사의 경우 입찰심사기준이 법으로 정해져 있어 객관성이 높지만, 베트남에서는 프로젝트마다 심사 기준이 다를 수 있어 입찰 전 철저한 분석이 필요합니다. 베트남에서는 심사 과정에서 발주자의 재량이 상대적으로 크고, '협상(thương thảo)' 절차가 포함되는 경우도 많습니다. 또한 베트남에서는 심사 결과에 대한 이의제기가 한국보다 형식적인 경우가 많아 사전 검토가 중요합니다.",
        "commonMistakes": [
            {
                "mistake": "đánh giá đấu thầu",
                "correction": "xét thầu",
                "explanation": "'đánh giá đấu thầu'는 일반적인 평가이고, 공식적인 입찰 심사는 'xét thầu'입니다."
            },
            {
                "mistake": "입찰평가",
                "correction": "심사 또는 입찰심사",
                "explanation": "입찰평가는 구어적 표현이고, 공식 용어는 '심사' 또는 '입찰심사'입니다."
            },
            {
                "mistake": "chấm thầu",
                "correction": "xét thầu",
                "explanation": "'chấm thầu'는 구어적 표현이고, 공식 용어는 'xét thầu'입니다."
            }
        ],
        "examples": [
            {
                "ko": "심사 결과 기술 점수가 높아서 1순위로 선정되었습니다.",
                "vi": "Kết quả xét thầu cho thấy chúng tôi có điểm kỹ thuật cao nên được xếp hạng nhất.",
                "situation": "formal"
            },
            {
                "ko": "심사위원회에서 우리 시공계획을 높게 평가했대요.",
                "vi": "Ban xét thầu đã đánh giá cao phương án thi công của chúng tôi.",
                "situation": "onsite"
            },
            {
                "ko": "심사 기준에 따르면 기술 60점, 가격 40점 배점입니다.",
                "vi": "Theo tiêu chí xét thầu, kỹ thuật chiếm 60 điểm, giá cả chiếm 40 điểm.",
                "situation": "formal"
            }
        ],
        "relatedTerms": ["mo-thau", "trung-thau", "ho-so-du-thau"]
    },
    {
        "slug": "trung-thau",
        "korean": "낙찰",
        "vietnamese": "trúng thầu",
        "hanja": "落札",
        "hanjaReading": "落(떨어질 락) + 札(찰 찰)",
        "pronunciation": "쭝 타우",
        "meaningKo": "입찰 심사 결과 최종적으로 공사 계약자로 선정되는 것을 의미하며, 베트남어로는 'trúng thầu'라고 합니다. 통역 시 주의할 점은 낙찰과 계약 체결은 별개의 절차이며, 낙찰 후에도 협상이나 추가 서류 제출이 필요할 수 있다는 것입니다. 한국에서는 낙찰자 발표 후 일정 기간 이의신청 기간을 거쳐 계약을 체결하지만, 베트남에서는 '낙찰 통지(thông báo trúng thầu)' 후 협상 절차가 이어지는 경우가 많습니다. 낙찰 후 계약 체결을 거부하면 입찰보증금이 몰수되며, 향후 입찰 참가에 제한을 받을 수 있습니다.",
        "meaningVi": "Trúng thầu là kết quả cuối cùng của quá trình đấu thầu, khi một nhà thầu được chọn để ký hợp đồng thực hiện công trình. Sau khi trúng thầu, nhà thầu sẽ nhận thông báo trúng thầu (thư mời ký hợp đồng) và phải thực hiện các thủ tục ký kết hợp đồng trong thời gian quy định. Nếu nhà thầu trúng thầu từ chối ký hợp đồng, bảo lãnh dự thầu sẽ bị tịch thu và có thể bị cấm tham gia đấu thầu trong một thời gian. Trúng thầu không đồng nghĩa với việc đã có hợp đồng chính thức, mà chỉ là bước trung gian trước khi hoàn tất thủ tục pháp lý.",
        "context": "입찰 결과 발표, 계약 협상 준비, 낙찰자 공고 확인",
        "culturalNote": "한국에서는 낙찰 후 계약 체결이 비교적 신속하게 진행되지만, 베트남에서는 낙찰 통지 후 계약 체결까지 추가 협상이나 서류 보완 요구가 있을 수 있어 시간이 더 소요됩니다. 베트남에서는 '조건부 낙찰(trúng thầu có điều kiện)'이라는 개념이 있어 특정 조건을 충족해야 최종 계약이 체결되기도 합니다. 또한 베트남에서는 낙찰 후에도 가격 협상이 이루어지는 경우가 있어 최종 계약금액이 입찰가격과 다를 수 있습니다.",
        "commonMistakes": [
            {
                "mistake": "thắng thầu",
                "correction": "trúng thầu",
                "explanation": "'thắng thầu'는 구어적 표현이고, 공식 용어는 'trúng thầu'입니다."
            },
            {
                "mistake": "낙찰받다",
                "correction": "낙찰되다 또는 낙찰자로 선정되다",
                "explanation": "낙찰은 '받는' 것이 아니라 '되는' 것이므로 '낙찰되다'가 정확한 표현입니다."
            },
            {
                "mistake": "được chọn thầu",
                "correction": "trúng thầu",
                "explanation": "'được chọn thầu'는 일반적인 선택이고, 공식 낙찰은 'trúng thầu'입니다."
            }
        ],
        "examples": [
            {
                "ko": "축하합니다! 귀사가 이번 공사에 낙찰되었습니다.",
                "vi": "Xin chúc mừng! Công ty quý vị đã trúng thầu dự án này.",
                "situation": "formal"
            },
            {
                "ko": "낙찰 통지를 받았으니 다음 주에 계약 체결하러 갑시다.",
                "vi": "Chúng ta đã nhận thông báo trúng thầu rồi, tuần sau đi ký hợp đồng nhé.",
                "situation": "onsite"
            },
            {
                "ko": "낙찰은 됐는데 계약 조건 협상이 남았어요.",
                "vi": "Chúng tôi đã trúng thầu nhưng còn phải thương thảo điều kiện hợp đồng.",
                "situation": "informal"
            }
        ],
        "relatedTerms": ["xet-thau", "hop-dong-thi-cong", "bao-lanh-du-thau"]
    },
    {
        "slug": "hop-dong-thi-cong",
        "korean": "시공계약",
        "vietnamese": "hợp đồng thi công",
        "hanja": "施工契約",
        "hanjaReading": "施(베풀 시) + 工(장인 공) + 契(맺을 계) + 約(약속할 약)",
        "pronunciation": "헙 동 티 공",
        "meaningKo": "발주자와 시공사 간에 공사의 범위, 기간, 금액, 조건 등을 명시한 법적 문서로, 베트남어로는 'hợp đồng thi công'이라고 합니다. 통역 시 주의할 점은 한국과 베트남의 계약서 구조와 필수 조항이 다를 수 있으므로 양국의 계약 관습을 모두 이해해야 합니다. 시공계약서에는 공사 범위, 계약금액, 지급 조건, 공사 기간, 지체상금, 하자보수 책임, 분쟁 해결 방법 등이 포함됩니다. 베트남에서는 계약서가 베트남어와 외국어 두 가지 버전으로 작성되는 경우 베트남어 버전이 우선합니다. 계약 체결 전 법률 검토와 공증이 필요한 경우가 많습니다.",
        "meaningVi": "Hợp đồng thi công là văn bản pháp lý giữa chủ đầu tư và nhà thầu quy định về phạm vi công việc, thời gian, giá trị, điều kiện thanh toán và các nghĩa vụ trách nhiệm trong quá trình xây dựng. Hợp đồng bao gồm các điều khoản về giá trị hợp đồng, tiến độ, chất lượng, bảo hành, xử phạt chậm tiến độ, điều chỉnh giá, thanh lý hợp đồng và giải quyết tranh chấp. Hợp đồng phải tuân thủ Luật Xây dựng và Luật Đấu thầu của Việt Nam. Trước khi ký, hai bên cần thỏa thuận kỹ tất cả các điều khoản để tránh tranh chấp sau này.",
        "context": "계약 협상, 계약서 검토, 계약 체결 의식",
        "culturalNote": "한국에서는 표준계약서 양식이 보편화되어 있지만, 베트남에서는 프로젝트마다 계약서 형식이 다양하고 협상 여지가 큽니다. 베트남에서는 계약서에 '불가항력(bất khả kháng)' 조항이 중요하며, 베트남 법률에 따라 자연재해, 전쟁, 정부 명령 등이 포함됩니다. 또한 베트남에서는 계약서에 '가격 조정(điều chỉnh giá)' 조항을 반드시 포함해야 자재비 상승 시 분쟁을 예방할 수 있습니다. 계약 분쟁 시 베트남 중재기관이나 법원이 관할권을 갖는지도 계약서에 명시해야 합니다.",
        "commonMistakes": [
            {
                "mistake": "hợp đồng xây dựng",
                "correction": "hợp đồng thi công",
                "explanation": "'hợp đồng xây dựng'은 건설 계약 전반을 의미하고, 시공 계약은 'hợp đồng thi công'이 더 정확합니다."
            },
            {
                "mistake": "공사계약",
                "correction": "시공계약",
                "explanation": "공사계약은 공사 관련 모든 계약을 의미할 수 있고, 시공사와 발주자 간의 계약은 '시공계약'이 정확합니다."
            },
            {
                "mistake": "hợp đồng công trình",
                "correction": "hợp đồng thi công",
                "explanation": "'hợp đồng công trình'은 공사 전반에 대한 계약이고, 시공에 특화된 계약은 'hợp đồng thi công'입니다."
            }
        ],
        "examples": [
            {
                "ko": "다음 주 월요일에 시공계약을 체결할 예정입니다.",
                "vi": "Chúng tôi sẽ ký hợp đồng thi công vào thứ Hai tuần tới.",
                "situation": "formal"
            },
            {
                "ko": "시공계약서에 가격 조정 조항을 꼭 넣어야 해요.",
                "vi": "Phải đưa điều khoản điều chỉnh giá vào hợp đồng thi công nhé.",
                "situation": "onsite"
            },
            {
                "ko": "시공계약 위반으로 지체상금을 청구받았습니다.",
                "vi": "Chúng tôi bị yêu cầu chi trả phạt chậm tiến độ do vi phạm hợp đồng thi công.",
                "situation": "formal"
            }
        ],
        "relatedTerms": ["trung-thau", "bao-lanh-thuc-hien", "bao-lanh-tam-ung"]
    }
]

def main():
    # Define file path
    file_path = os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', 'data', 'terms', 'construction.json')

    # Read existing data
    with open(file_path, 'r', encoding='utf-8') as f:
        data = json.load(f)  # data is a LIST

    print(f"📖 Current number of terms: {len(data)}")

    # Get existing slugs
    existing_slugs = {term['slug'] for term in data}
    print(f"🔍 Existing slugs: {len(existing_slugs)}")

    # Filter out duplicates
    new_unique_terms = [term for term in new_terms if term['slug'] not in existing_slugs]

    print(f"✨ New unique terms to add: {len(new_unique_terms)}")

    if not new_unique_terms:
        print("⚠️  No new terms to add (all duplicates)")
        return

    # Add new terms
    data.extend(new_unique_terms)

    # Write back
    with open(file_path, 'w', encoding='utf-8') as f:
        json.dump(data, f, ensure_ascii=False, indent=2)

    print(f"✅ Successfully added {len(new_unique_terms)} terms")
    print(f"📊 Total terms now: {len(data)}")

    # Print added terms
    print("\n📝 Added terms:")
    for term in new_unique_terms:
        print(f"  - {term['slug']}: {term['korean']} ({term['vietnamese']})")

if __name__ == "__main__":
    main()
