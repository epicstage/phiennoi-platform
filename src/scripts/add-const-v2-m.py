#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Construction Terms - Contract & Administration (계약/행정)
Tier S Quality: 10 terms
"""

import json
import sys
from pathlib import Path

# 프로젝트 루트 기준 경로 설정
project_root = Path(__file__).parent.parent
terms_file = project_root / "data" / "terms" / "construction.json"

# 추가할 용어 데이터 (배열 형식)
new_terms = [
    {
        "slug": "hop-dong-thau",
        "korean": "도급계약",
        "vietnamese": "Hợp đồng thầu",
        "hanja": "都給契約",
        "hanjaReading": "都(도읍 도) + 給(줄 급) + 契(맺을 계) + 約(맺을 약)",
        "pronunciation": "호프동 터우",
        "meaningKo": "건설공사에서 발주자(건축주)와 시공자(건설업체) 간에 체결하는 공사 계약을 의미합니다. 도급계약에는 공사 범위, 공사 금액, 공사 기간, 하자보수 책임, 지체상금 등 주요 조건이 명시됩니다. 통역 시 주의사항: 베트남에서는 '계약서(Hợp đồng)'라는 표현이 일반적이며, 한국의 '도급'이라는 개념이 계약 형태를 구분하는 법적 용어임을 이해해야 합니다. 한국에서는 종합도급, 분할도급, 일괄도급 등 다양한 형태가 있으므로 계약 유형을 정확히 구분해서 통역해야 합니다. 베트남 현장에서는 'Hợp đồng thi công'(시공계약)으로 표현하는 경우가 많으므로 상황에 맞게 선택하세요.",
        "meaningVi": "Hợp đồng xây dựng được ký kết giữa chủ đầu tư và nhà thầu thi công, quy định phạm vi công việc, giá trị hợp đồng, thời gian thi công, trách nhiệm bảo hành, phạt chậm tiến độ và các điều khoản quan trọng khác. Tại Việt Nam, thuật ngữ 'Hợp đồng thầu' thường được sử dụng trong các dự án lớn, trong khi 'Hợp đồng thi công' phổ biến hơn ở các công trình dân dụng.",
        "context": "계약 체결, 입찰, 공사 착수 전 필수 서류",
        "culturalNote": "한국의 건설업법에서는 '도급'이라는 용어를 법적으로 명확히 정의하고 있으며, 종합도급·분할도급·일괄도급 등 다양한 형태로 분류됩니다. 베트남에서는 'Hợp đồng thầu' 또는 'Hợp đồng thi công'이라는 표현을 주로 사용하며, 계약 형태보다는 계약 내용과 책임 범위에 중점을 둡니다. 한국 현장에서는 계약서 검토 시 법률 전문가 참여가 일반적이지만, 베트남에서는 기술자와 행정 담당자가 주로 검토합니다.",
        "commonMistakes": [
            {
                "mistake": "'계약서'를 그냥 'Hợp đồng'으로만 번역",
                "correction": "'도급계약'은 'Hợp đồng thầu' 또는 'Hợp đồng thi công'으로 구체화",
                "explanation": "'Hợp đồng'만으로는 일반 계약을 의미하므로 건설 분야임을 명확히 해야 합니다"
            },
            {
                "mistake": "'종합도급'을 'Thầu tổng hợp'로 직역",
                "correction": "'Thầu chính' 또는 'Nhà thầu tổng thầu'로 번역",
                "explanation": "베트남 건설 업계에서 통용되는 정확한 용어를 사용해야 혼란을 방지합니다"
            },
            {
                "mistake": "계약 금액 단위를 환산 없이 그대로 통역",
                "correction": "한국 '억 원' 단위를 베트남 'tỷ đồng' 또는 USD로 환산 설명",
                "explanation": "양국 통화 단위와 환율을 고려하지 않으면 금액 오해가 발생할 수 있습니다"
            }
        ],
        "examples": [
            {
                "ko": "도급계약서에 명시된 공사 기간은 12개월입니다.",
                "vi": "Thời gian thi công ghi trong hợp đồng thầu là 12 tháng.",
                "situation": "formal"
            },
            {
                "ko": "이번 프로젝트는 종합도급 방식으로 진행됩니다.",
                "vi": "Dự án này sẽ thực hiện theo hình thức thầu chính.",
                "situation": "formal"
            },
            {
                "ko": "계약 조건 검토 후 내일 서명 예정입니다.",
                "vi": "Sau khi xem xét điều kiện hợp đồng, dự kiến ký ngày mai.",
                "situation": "onsite"
            }
        ],
        "relatedTerms": ["하도급계약", "계약금", "준공정산", "설계변경"]
    },
    {
        "slug": "hop-dong-thau-phu",
        "korean": "하도급계약",
        "vietnamese": "Hợp đồng thầu phụ",
        "hanja": "下都給契約",
        "hanjaReading": "下(아래 하) + 都(도읍 도) + 給(줄 급) + 契(맺을 계) + 約(맺을 약)",
        "pronunciation": "호프동 터우 푸",
        "meaningKo": "원도급자(종합건설업체)가 공사의 일부를 다른 건설업체(하도급업체)에게 재계약하는 것을 의미합니다. 하도급계약에는 하도급 범위, 금액, 기간, 안전 책임, 대금 지급 조건 등이 포함됩니다. 통역 시 주의사항: 한국에서는 '불법 하도급' 문제가 민감하게 다뤄지므로, 하도급 허용 범위와 신고 의무를 정확히 전달해야 합니다. 베트남 현장에서는 하도급 개념이 덜 엄격하게 적용되는 경우가 많으므로, 한국 법규상 제약 사항을 명확히 설명해야 합니다. '하도급대금 직불제', '하도급 대금 지급 보증' 등 한국 특유의 제도도 함께 설명하세요.",
        "meaningVi": "Hợp đồng mà nhà thầu chính ký kết với nhà thầu phụ để giao một phần công việc trong dự án. Hợp đồng này quy định phạm vi công việc, giá trị, thời gian, trách nhiệm an toàn và điều kiện thanh toán. Tại Hàn Quốc, việc thầu phụ được quản lý chặt chẽ bởi luật pháp, với các quy định nghiêm ngặt về phạm vi được phép và nghĩa vụ báo cáo.",
        "context": "공사 분할, 전문 공종 위탁, 노무 관리",
        "culturalNote": "한국에서는 '건설산업기본법'에 따라 하도급이 엄격히 규제되며, 불법 하도급 적발 시 영업정지나 과징금 등 강력한 처벌을 받습니다. 특히 '일괄하도급 금지', '2차 하도급 제한' 등의 규정이 있어 통역 시 주의가 필요합니다. 반면 베트남에서는 하도급 규제가 상대적으로 느슨하며, 다단계 하도급도 흔하게 이뤄집니다. 한국 발주처와 베트남 현지 업체 간 협업 시 이러한 법적 차이를 명확히 설명해야 분쟁을 예방할 수 있습니다.",
        "commonMistakes": [
            {
                "mistake": "'하도급'을 'Thầu dưới'로 직역",
                "correction": "'Thầu phụ' 또는 'Nhà thầu phụ'로 번역",
                "explanation": "베트남 건설 업계에서 정식으로 사용되는 용어는 'Thầu phụ'입니다"
            },
            {
                "mistake": "'불법 하도급'을 그냥 'Thầu phụ bất hợp pháp'로만 표현",
                "correction": "한국 법상 금지된 하도급 유형임을 구체적으로 설명 추가",
                "explanation": "단순 번역만으로는 한국 법규의 특수성을 전달하기 어렵습니다"
            },
            {
                "mistake": "하도급 허용 범위를 모호하게 통역",
                "correction": "법적으로 허용된 공종과 금지된 공종을 명확히 구분",
                "explanation": "애매한 통역은 법적 문제를 초래할 수 있습니다"
            }
        ],
        "examples": [
            {
                "ko": "전기 공사는 전문 하도급업체에게 맡깁니다.",
                "vi": "Công việc điện sẽ được giao cho nhà thầu phụ chuyên ngành.",
                "situation": "formal"
            },
            {
                "ko": "하도급 계약 전에 발주처 승인이 필요합니다.",
                "vi": "Cần có sự chấp thuận của chủ đầu tư trước khi ký hợp đồng thầu phụ.",
                "situation": "formal"
            },
            {
                "ko": "불법 하도급 적발 시 과태료가 부과됩니다.",
                "vi": "Nếu phát hiện thầu phụ bất hợp pháp sẽ bị phạt tiền.",
                "situation": "onsite"
            }
        ],
        "relatedTerms": ["도급계약", "일괄하도급", "하도급대금", "전문건설업"]
    },
    {
        "slug": "tien-tam-ung",
        "korean": "선급금",
        "vietnamese": "Tiền tạm ứng",
        "hanja": "先給金",
        "hanjaReading": "先(먼저 선) + 給(줄 급) + 金(쇠 금)",
        "pronunciation": "띠엔 땀 응",
        "meaningKo": "공사 착수 전 또는 초기 단계에 발주자가 시공사에게 미리 지급하는 공사비의 일부를 의미합니다. 일반적으로 총 공사비의 10~30% 범위에서 지급되며, 자재 구매, 인력 동원, 장비 확보 등 초기 공사 준비 비용으로 사용됩니다. 통역 시 주의사항: 한국에서는 '선급금'과 '계약금'을 명확히 구분하며, 선급금은 공사 진행에 따라 기성금에서 공제됩니다. 베트남에서는 'Tiền tạm ứng'이 선급금을 의미하지만, 'Tiền ứng trước'라고도 표현합니다. 선급금 반환 보증서(Guarantee for Advance Payment) 제출 의무도 함께 설명하세요.",
        "meaningVi": "Khoản tiền mà chủ đầu tư chi trả trước cho nhà thầu trước khi khởi công hoặc trong giai đoạn đầu thi công, thường chiếm 10-30% tổng giá trị hợp đồng. Tiền tạm ứng được sử dụng để mua vật liệu, huy động nhân lực và thiết bị. Nhà thầu thường phải cung cấp bảo lãnh hoàn trả tiền tạm ứng (Guarantee for Advance Payment) khi nhận tiền.",
        "context": "공사 착수, 초기 자금 조달, 재무 계획",
        "culturalNote": "한국 공공 공사에서는 '선급금 지급 규정'에 따라 명확한 지급 시기와 비율이 정해져 있으며, 선급금 사용 내역을 투명하게 보고해야 합니다. 민간 공사에서는 협의에 따라 결정됩니다. 베트남에서도 선급금 제도가 일반적이지만, 지급 비율과 조건이 한국보다 유연하게 적용되는 경우가 많습니다. 한국 발주처는 선급금 보증서를 필수로 요구하지만, 베트남 일부 소규모 현장에서는 보증서 없이 진행되기도 하므로 계약 조건을 명확히 확인하세요.",
        "commonMistakes": [
            {
                "mistake": "'선급금'을 'Tiền trước'로만 번역",
                "correction": "'Tiền tạm ứng' 또는 'Tiền ứng trước'로 정확히 표현",
                "explanation": "'Tiền trước'는 일반적인 '사전 지급'을 의미하므로 건설 용어로는 부적합합니다"
            },
            {
                "mistake": "선급금 공제 방식을 설명 없이 통역",
                "correction": "기성금에서 어떻게 공제되는지 구체적으로 설명",
                "explanation": "선급금 정산 방식을 이해하지 못하면 대금 분쟁이 발생할 수 있습니다"
            },
            {
                "mistake": "선급금과 계약금을 혼동",
                "correction": "선급금(Tiền tạm ứng)과 계약금(Tiền đặt cọc)을 명확히 구분",
                "explanation": "두 용어는 법적 성격과 용도가 다르므로 정확히 구분해야 합니다"
            }
        ],
        "examples": [
            {
                "ko": "공사 착수 시 총 공사비의 20%를 선급금으로 지급합니다.",
                "vi": "Khi khởi công, sẽ chi trả 20% tổng giá trị hợp đồng làm tiền tạm ứng.",
                "situation": "formal"
            },
            {
                "ko": "선급금 수령 전에 은행 보증서를 제출하세요.",
                "vi": "Hãy nộp bảo lãnh ngân hàng trước khi nhận tiền tạm ứng.",
                "situation": "formal"
            },
            {
                "ko": "선급금은 매월 기성금에서 공제됩니다.",
                "vi": "Tiền tạm ứng sẽ được khấu trừ trong tiền thanh toán khối lượng hàng tháng.",
                "situation": "onsite"
            }
        ],
        "relatedTerms": ["기성금", "계약금", "준공금", "선급금보증서"]
    },
    {
        "slug": "tien-nghiem-thu-khoi-luong",
        "korean": "기성금",
        "vietnamese": "Tiền nghiệm thu khối lượng",
        "hanja": "旣成金",
        "hanjaReading": "旣(이미 기) + 成(이룰 성) + 金(쇠 금)",
        "pronunciation": "띠엔 응이엠 투 코이 르엉",
        "meaningKo": "공사 진행 과정에서 일정 기간 동안 완료된 공사 물량을 검수받고 지급받는 대금을 의미합니다. 보통 월 단위로 작성된 기성 내역서를 발주자가 검토·승인한 후 지급됩니다. 통역 시 주의사항: 한국에서는 '기성금', '기성대가', '기성 지급'이라는 표현을 모두 사용하며, 공사 진행률에 따라 정기적으로 지급됩니다. 베트남에서는 'Tiền nghiệm thu khối lượng' 또는 'Tiền thanh toán theo khối lượng hoàn thành'이라고 표현합니다. 기성 검수 절차, 승인 기간, 지급 지연 시 이자 등 세부 조건을 명확히 전달하세요.",
        "meaningVi": "Khoản tiền thanh toán cho khối lượng công việc đã hoàn thành trong một khoảng thời gian nhất định, thường theo tháng. Nhà thầu lập bảng nghiệm thu khối lượng và được chủ đầu tư xem xét, phê duyệt trước khi thanh toán. Đây là hình thức thanh toán chủ yếu trong quá trình thi công.",
        "context": "공사 대금 청구, 월간 정산, 공사 진행률 확인",
        "culturalNote": "한국 건설 현장에서는 매월 기성 검수를 통해 공사 진행 상황을 확인하고 대금을 지급하는 것이 일반적입니다. 기성 검수는 발주자, 감리단, 시공사가 함께 참여하며, 검수 결과에 따라 기성률(%)이 결정됩니다. 베트남에서도 유사한 절차가 있지만, 기성 검수가 덜 엄격하거나 지급이 지연되는 경우가 있어 현금 흐름 관리에 주의해야 합니다. 한국 공공 공사에서는 기성금 지급 지연 시 지연 이자를 지급하는 규정이 있으므로 이를 명확히 설명하세요.",
        "commonMistakes": [
            {
                "mistake": "'기성금'을 'Tiền hoàn thành'로 번역",
                "correction": "'Tiền nghiệm thu khối lượng' 또는 'Tiền thanh toán theo tiến độ'로 번역",
                "explanation": "'Tiền hoàn thành'는 준공금(최종 대금)을 의미하므로 기성금과는 다릅니다"
            },
            {
                "mistake": "기성률(%)과 금액을 혼동",
                "correction": "기성률은 공사 진행률(%), 기성금은 실제 지급 금액임을 구분",
                "explanation": "두 개념을 혼동하면 대금 정산에서 오해가 발생합니다"
            },
            {
                "mistake": "선급금 공제를 빠뜨리고 통역",
                "correction": "기성금 계산 시 선급금 공제 여부를 함께 설명",
                "explanation": "선급금 공제는 실제 지급액에 큰 영향을 미칩니다"
            }
        ],
        "examples": [
            {
                "ko": "이번 달 기성금은 5억 원입니다.",
                "vi": "Tiền nghiệm thu khối lượng tháng này là 5 tỷ won.",
                "situation": "formal"
            },
            {
                "ko": "기성 검수는 매월 25일에 진행됩니다.",
                "vi": "Nghiệm thu khối lượng sẽ được thực hiện vào ngày 25 hàng tháng.",
                "situation": "onsite"
            },
            {
                "ko": "기성금 지급은 승인 후 15일 이내입니다.",
                "vi": "Thanh toán tiền nghiệm thu sẽ được thực hiện trong vòng 15 ngày sau khi phê duyệt.",
                "situation": "formal"
            }
        ],
        "relatedTerms": ["선급금", "준공금", "기성검수", "공사대금"]
    },
    {
        "slug": "quyet-toan-hoan-thanh",
        "korean": "준공정산",
        "vietnamese": "Quyết toán hoàn thành",
        "hanja": "竣工精算",
        "hanjaReading": "竣(마칠 준) + 工(장인 공) + 精(정밀할 정) + 算(셈할 산)",
        "pronunciation": "꾸예뜨 또안 호안 탄",
        "meaningKo": "공사 완료 후 최종적으로 공사비를 정산하는 절차를 의미합니다. 준공정산에는 총 공사비 확정, 추가·감액 내역 확인, 기지급금 차감, 최종 지급액 산정이 포함됩니다. 설계변경, 물가 변동, 클레임 등이 반영되어 최종 공사비가 결정됩니다. 통역 시 주의사항: 한국에서는 '준공정산'과 '준공금'을 구분해야 하며, 준공정산은 '절차'이고 준공금은 '금액'입니다. 베트남에서는 'Quyết toán hoàn thành' 또는 'Thanh lý hợp đồng'이라고 표현하며, 정산 과정에서 발생하는 서류(준공도서, 하자보수보증서 등)와 절차를 명확히 설명하세요.",
        "meaningVi": "Quá trình quyết toán cuối cùng chi phí xây dựng sau khi hoàn thành công trình. Quyết toán bao gồm xác định tổng chi phí xây dựng, kiểm tra các khoản tăng giảm, trừ tiền đã thanh toán và xác định số tiền thanh toán cuối cùng. Trong quá trình này, các thay đổi thiết kế, biến động giá cả, khiếu nại sẽ được phản ánh để xác định chi phí cuối cùng.",
        "context": "공사 완료, 최종 대금 정산, 준공 검사 후",
        "culturalNote": "한국 건설 현장에서는 준공 검사 통과 후 준공정산 절차가 시작되며, 통상 2~3개월이 소요됩니다. 준공정산 시 발주자와 시공사 간 설계변경 내역, 물가 변동분, 클레임 등에 대한 합의가 필요하며, 이 과정에서 분쟁이 발생하기도 합니다. 베트남에서는 준공정산 절차가 상대적으로 간소하지만, 서류 미비로 인한 지연이 흔합니다. 한국 발주처는 준공도서, 하자보수보증서, 세금계산서 등 제출 서류를 엄격히 요구하므로 사전에 준비해야 합니다.",
        "commonMistakes": [
            {
                "mistake": "'준공정산'을 'Thanh toán hoàn thành'로만 번역",
                "correction": "'Quyết toán hoàn thành' 또는 'Thanh lý hợp đồng'으로 표현",
                "explanation": "'Thanh toán'은 단순 지급을 의미하므로 정산 절차를 포괄하지 못합니다"
            },
            {
                "mistake": "준공금과 준공정산을 혼동",
                "correction": "준공정산은 절차, 준공금은 최종 지급액임을 구분",
                "explanation": "두 용어의 차이를 이해하지 못하면 혼란이 발생합니다"
            },
            {
                "mistake": "정산 서류 목록을 누락하고 통역",
                "correction": "준공도서, 하자보수보증서, 세금계산서 등 필수 서류 명시",
                "explanation": "서류 미비는 정산 지연의 주요 원인입니다"
            }
        ],
        "examples": [
            {
                "ko": "준공정산은 준공 검사 통과 후 시작됩니다.",
                "vi": "Quyết toán hoàn thành sẽ bắt đầu sau khi nghiệm thu công trình đạt yêu cầu.",
                "situation": "formal"
            },
            {
                "ko": "정산 서류를 다음 주까지 제출해 주세요.",
                "vi": "Vui lòng nộp hồ sơ quyết toán trước tuần sau.",
                "situation": "onsite"
            },
            {
                "ko": "설계변경 비용은 준공정산 시 반영됩니다.",
                "vi": "Chi phí thay đổi thiết kế sẽ được tính vào quyết toán hoàn thành.",
                "situation": "formal"
            }
        ],
        "relatedTerms": ["준공검사", "준공금", "설계변경", "하자보수보증서"]
    },
    {
        "slug": "thay-doi-thiet-ke",
        "korean": "설계변경",
        "vietnamese": "Thay đổi thiết kế",
        "hanja": "設計變更",
        "hanjaReading": "設(베풀 설) + 計(셈 계) + 變(변할 변) + 更(고칠 갱)",
        "pronunciation": "타이 도이 티엣 께",
        "meaningKo": "공사 진행 중 당초 설계 내용을 변경하는 것을 의미합니다. 설계변경은 발주자 요구, 현장 여건 변화, 기술적 문제 등으로 발생하며, 공사비와 공사 기간에 영향을 미칩니다. 통역 시 주의사항: 한국에서는 '설계변경'이 공식적인 절차로 관리되며, 설계변경 승인 없이는 임의로 시공할 수 없습니다. 베트남에서는 'Thay đổi thiết kế' 또는 'Điều chỉnh thiết kế'라고 표현하며, 변경 사유와 승인 절차를 명확히 설명해야 합니다. 설계변경으로 인한 공사비 증감(Tăng/Giảm chi phí)과 공기 연장(Gia hạn tiến độ) 여부도 함께 전달하세요.",
        "meaningVi": "Việc thay đổi nội dung thiết kế ban đầu trong quá trình thi công. Thay đổi thiết kế xảy ra do yêu cầu của chủ đầu tư, thay đổi điều kiện hiện trường hoặc vấn đề kỹ thuật, ảnh hưởng đến chi phí và tiến độ thi công. Tại Hàn Quốc, thay đổi thiết kế phải được phê duyệt chính thức và không được tự ý thi công khi chưa có phê duyệt.",
        "context": "공사 진행 중, 현장 여건 변화, 발주자 요구 사항 반영",
        "culturalNote": "한국 건설 현장에서는 설계변경 절차가 매우 엄격하며, 발주자·감리·설계자가 모두 참여하여 검토합니다. 설계변경 승인 없이 시공 시 준공 검사 불합격이나 대금 미지급 사태가 발생할 수 있습니다. 베트남에서는 설계변경 절차가 상대적으로 유연하지만, 서면 승인 없이 진행하면 나중에 대금 청구가 어려울 수 있습니다. 한국 발주처는 설계변경 내역서, 변경 도면, 물량 산출서 등 상세 자료를 요구하므로 철저히 준비하세요.",
        "commonMistakes": [
            {
                "mistake": "'설계변경'을 'Thay đổi'로만 축약",
                "correction": "'Thay đổi thiết kế' 또는 'Điều chỉnh thiết kế'로 완전히 표현",
                "explanation": "'Thay đổi'만으로는 무엇을 변경하는지 불명확합니다"
            },
            {
                "mistake": "설계변경 사유를 생략하고 통역",
                "correction": "변경 사유(발주자 요구/현장 여건/기술적 문제)를 명시",
                "explanation": "사유가 없으면 승인 여부 판단이 어렵습니다"
            },
            {
                "mistake": "공사비 증감 없이 변경만 통역",
                "correction": "설계변경으로 인한 공사비·공기 변동 여부 함께 설명",
                "explanation": "비용과 일정 변화는 설계변경의 핵심 사항입니다"
            }
        ],
        "examples": [
            {
                "ko": "발주자 요청으로 외벽 마감재를 변경합니다.",
                "vi": "Thay đổi vật liệu hoàn thiện tường ngoài theo yêu cầu của chủ đầu tư.",
                "situation": "formal"
            },
            {
                "ko": "설계변경 승인 후 시공을 시작하겠습니다.",
                "vi": "Sẽ bắt đầu thi công sau khi thay đổi thiết kế được phê duyệt.",
                "situation": "onsite"
            },
            {
                "ko": "이번 설계변경으로 공사비가 10% 증가합니다.",
                "vi": "Thay đổi thiết kế lần này sẽ làm tăng chi phí thi công 10%.",
                "situation": "formal"
            }
        ],
        "relatedTerms": ["설계도", "변경승인", "준공정산", "클레임"]
    },
    {
        "slug": "khieu-nai",
        "korean": "클레임",
        "vietnamese": "Khiếu nại",
        "hanja": None,
        "hanjaReading": None,
        "pronunciation": "키에우 나이",
        "meaningKo": "공사 계약 조건과 다르게 발생한 사항에 대해 시공사가 발주자에게 추가 비용이나 공기 연장을 요구하는 것을 의미합니다. 설계 오류, 현장 여건 불일치, 발주자 지시 변경 등이 주요 클레임 사유입니다. 통역 시 주의사항: 한국 건설업계에서는 영어 'Claim'을 그대로 '클레임'이라고 사용하며, 베트남에서는 'Khiếu nại' 또는 'Yêu cầu bồi thường'이라고 표현합니다. 클레임은 단순 불만이 아니라 법적 근거를 바탕으로 한 정당한 요구이므로, 근거 자료(도면, 사진, 이메일 등)와 계약 조항을 명확히 제시해야 합니다. 클레임 처리 절차와 기한도 함께 설명하세요.",
        "meaningVi": "Yêu cầu của nhà thầu đối với chủ đầu tư về chi phí bổ sung hoặc gia hạn tiến độ do các vấn đề phát sinh khác với điều kiện hợp đồng ban đầu. Nguyên nhân chính bao gồm sai sót thiết kế, không khớp điều kiện hiện trường, thay đổi chỉ thị của chủ đầu tư. Khiếu nại không phải là phàn nàn đơn thuần mà là yêu cầu chính đáng dựa trên cơ sở pháp lý.",
        "context": "분쟁 해결, 대금 협상, 공기 조정",
        "culturalNote": "한국 건설업계에서는 클레임이 공사 중 자주 발생하며, 클레임 관리 전문가(Claim Manager)를 두는 대형 프로젝트도 많습니다. 클레임 제기 시 계약서상 통지 기한(보통 14~28일 이내)을 엄수해야 하며, 기한 경과 시 권리를 상실할 수 있습니다. 베트남에서는 'Khiếu nại'라는 표현이 부정적으로 들릴 수 있으므로, 'Yêu cầu điều chỉnh hợp đồng'(계약 조정 요구)처럼 완곡하게 표현하는 것이 협상에 유리할 수 있습니다. 한국 발주처는 클레임에 대해 명확한 근거를 요구하므로 서류를 철저히 준비하세요.",
        "commonMistakes": [
            {
                "mistake": "'클레임'을 'Phàn nàn'(불만)으로 번역",
                "correction": "'Khiếu nại' 또는 'Yêu cầu bồi thường'으로 번역",
                "explanation": "'Phàn nàn'은 단순 불만이므로 법적 요구인 클레임과는 성격이 다릅니다"
            },
            {
                "mistake": "클레임 사유를 구체적으로 설명하지 않음",
                "correction": "설계 오류, 현장 여건 불일치 등 구체적 사유 명시",
                "explanation": "애매한 클레임은 받아들여지지 않습니다"
            },
            {
                "mistake": "클레임 통지 기한을 언급하지 않음",
                "correction": "계약서상 클레임 통지 기한을 확인하고 전달",
                "explanation": "기한 경과 시 클레임 권리를 상실할 수 있습니다"
            }
        ],
        "examples": [
            {
                "ko": "설계 오류로 인한 추가 공사비 클레임을 제출합니다.",
                "vi": "Nộp khiếu nại về chi phí bổ sung do lỗi thiết kế.",
                "situation": "formal"
            },
            {
                "ko": "클레임 처리 기한은 접수 후 30일 이내입니다.",
                "vi": "Thời hạn xử lý khiếu nại là trong vòng 30 ngày sau khi tiếp nhận.",
                "situation": "formal"
            },
            {
                "ko": "현장 여건 불일치로 공기 연장 클레임을 요청합니다.",
                "vi": "Yêu cầu khiếu nại gia hạn tiến độ do điều kiện hiện trường không khớp.",
                "situation": "onsite"
            }
        ],
        "relatedTerms": ["설계변경", "분쟁조정", "추가공사비", "계약서"]
    },
    {
        "slug": "tien-ky-quy-hop-dong",
        "korean": "계약보증금",
        "vietnamese": "Tiền ký quỹ hợp đồng",
        "hanja": "契約保證金",
        "hanjaReading": "契(맺을 계) + 約(맺을 약) + 保(지킬 보) + 證(증거 증) + 金(쇠 금)",
        "pronunciation": "띠엔 끼 꾸이 호프동",
        "meaningKo": "시공사가 계약 이행을 보증하기 위해 발주자에게 제공하는 보증금을 의미합니다. 일반적으로 계약금액의 5~10% 정도이며, 현금 납부 또는 은행 보증서(이행보증보험증권) 형태로 제공됩니다. 시공사가 계약을 불이행하거나 중도 포기할 경우 발주자는 이 보증금을 귀속시킬 수 있습니다. 통역 시 주의사항: 한국에서는 '계약보증금', '이행보증금', '계약이행보증' 등 다양한 표현을 사용하며, 베트남에서는 'Tiền ký quỹ hợp đồng' 또는 'Bảo lãnh thực hiện hợp đồng'이라고 합니다. 보증서 발급 은행, 유효 기간, 반환 조건 등을 명확히 전달하세요.",
        "meaningVi": "Khoản tiền ký quỹ mà nhà thầu cung cấp cho chủ đầu tư để đảm bảo thực hiện hợp đồng, thường chiếm 5-10% giá trị hợp đồng. Có thể cung cấp bằng tiền mặt hoặc bảo lãnh ngân hàng (giấy chứng nhận bảo hiểm thực hiện). Nếu nhà thầu không thực hiện hoặc từ bỏ hợp đồng, chủ đầu tư có quyền tịch thu tiền ký quỹ này.",
        "context": "계약 체결, 공사 착수, 리스크 관리",
        "culturalNote": "한국에서는 공공 공사의 경우 '계약이행보증보험증권' 제출이 의무화되어 있으며, 민간 공사에서도 일반적으로 요구됩니다. 보증 기간은 계약 기간 + 하자보수 기간을 포함하며, 준공 후 하자보수보증금으로 전환되기도 합니다. 베트남에서도 유사한 제도가 있지만, 보증금 비율과 반환 조건이 계약마다 다르므로 세부 내용을 확인해야 합니다. 한국 발주처는 보증서 원본과 보험사 확인을 엄격히 요구하므로 서류 준비에 주의하세요.",
        "commonMistakes": [
            {
                "mistake": "'계약보증금'을 'Tiền đặt cọc'(계약금)으로 혼동",
                "correction": "'Tiền ký quỹ hợp đồng' 또는 'Bảo lãnh thực hiện hợp đồng'으로 구분",
                "explanation": "계약금(Deposit)과 보증금(Guarantee)은 법적 성격이 다릅니다"
            },
            {
                "mistake": "보증금 반환 조건을 설명하지 않음",
                "correction": "준공 후 또는 하자보수 기간 종료 후 반환됨을 명시",
                "explanation": "반환 시점을 모르면 자금 계획에 차질이 생깁니다"
            },
            {
                "mistake": "현금과 보증서를 동일하게 취급",
                "correction": "현금 납부와 은행 보증서의 차이점 설명",
                "explanation": "실무에서는 은행 보증서가 선호되므로 차이를 알아야 합니다"
            }
        ],
        "examples": [
            {
                "ko": "계약보증금은 계약금액의 10%입니다.",
                "vi": "Tiền ký quỹ hợp đồng là 10% giá trị hợp đồng.",
                "situation": "formal"
            },
            {
                "ko": "은행 보증서로 계약보증금을 제출하세요.",
                "vi": "Vui lòng nộp bảo lãnh ngân hàng làm tiền ký quỹ hợp đồng.",
                "situation": "formal"
            },
            {
                "ko": "준공 검사 합격 후 보증금이 반환됩니다.",
                "vi": "Tiền ký quỹ sẽ được hoàn trả sau khi nghiệm thu công trình đạt yêu cầu.",
                "situation": "onsite"
            }
        ],
        "relatedTerms": ["이행보증보험", "하자보수보증금", "선급금보증서", "계약이행"]
    },
    {
        "slug": "bao-lanh-bao-hanh-sua-chua-khiem-khuyet",
        "korean": "하자보수보증",
        "vietnamese": "Bảo lãnh bảo hành sửa chữa khiếm khuyết",
        "hanja": "瑕疵補修保證",
        "hanjaReading": "瑕(흠 하) + 疵(흠 자) + 補(기울 보) + 修(닦을 수) + 保(지킬 보) + 證(증거 증)",
        "pronunciation": "바오 란 바오 한 스어 쓰어 키엠 쿠엣",
        "meaningKo": "준공 후 일정 기간(보통 1~3년) 동안 발생하는 하자를 무상으로 보수하겠다는 보증을 의미합니다. 시공사는 하자보수보증금(공사비의 2~5%) 또는 하자보수보증서를 발주자에게 제출하며, 하자보수 기간 종료 후 반환받습니다. 통역 시 주의사항: 한국에서는 '하자보수', '하자보증', '하자담보책임' 등 다양한 표현을 사용하며, 베트남에서는 'Bảo hành' 또는 'Sửa chữa khiếm khuyết'이라고 합니다. 하자 범위(시공 하자/사용 하자), 하자보수 기간(공종별 차이), 보증금 반환 조건 등을 명확히 전달하세요.",
        "meaningVi": "Cam kết sửa chữa miễn phí các khiếm khuyết phát sinh trong một khoảng thời gian nhất định (thường 1-3 năm) sau khi hoàn thành công trình. Nhà thầu phải nộp tiền ký quỹ bảo hành (2-5% giá trị công trình) hoặc giấy bảo lãnh bảo hành cho chủ đầu tư, và sẽ được hoàn trả sau khi hết thời gian bảo hành.",
        "context": "준공 후, 하자 발생 시, 유지보수 관리",
        "culturalNote": "한국에서는 '건설산업기본법'에 따라 공종별로 하자보수 기간이 법적으로 정해져 있습니다(예: 철근콘크리트 3년, 방수 5년). 하자보수 의무를 이행하지 않으면 법적 책임을 지며, 보증보험사가 대신 보수할 수 있습니다. 베트남에서는 하자보수 기간이 계약에 따라 결정되며, 통상 1~2년입니다. 한국 발주처는 하자 발생 시 즉각 조치를 요구하므로, 하자 접수 절차와 대응 체계를 사전에 마련해야 합니다.",
        "commonMistakes": [
            {
                "mistake": "'하자보수'를 'Sửa chữa'로만 축약",
                "correction": "'Bảo hành' 또는 'Sửa chữa khiếm khuyết'로 완전히 표현",
                "explanation": "'Sửa chữa'는 일반 수리를 의미하므로 보증 개념이 빠집니다"
            },
            {
                "mistake": "하자보수 기간을 명시하지 않음",
                "correction": "공종별 하자보수 기간(1~5년)을 구체적으로 설명",
                "explanation": "기간이 명확하지 않으면 책임 범위 분쟁이 발생합니다"
            },
            {
                "mistake": "사용 하자와 시공 하자를 구분하지 않음",
                "correction": "시공 하자는 무상 보수, 사용 하자는 유상임을 명시",
                "explanation": "하자 원인에 따라 책임이 달라지므로 정확히 구분해야 합니다"
            }
        ],
        "examples": [
            {
                "ko": "하자보수 기간은 준공 후 3년입니다.",
                "vi": "Thời gian bảo hành là 3 năm sau khi hoàn thành công trình.",
                "situation": "formal"
            },
            {
                "ko": "하자 발견 시 즉시 연락 주시기 바랍니다.",
                "vi": "Vui lòng liên hệ ngay khi phát hiện khiếm khuyết.",
                "situation": "onsite"
            },
            {
                "ko": "하자보수보증금은 공사비의 3%입니다.",
                "vi": "Tiền ký quỹ bảo hành là 3% giá trị công trình.",
                "situation": "formal"
            }
        ],
        "relatedTerms": ["하자보수기간", "준공검사", "유지보수", "계약보증금"]
    },
    {
        "slug": "tien-phat-cham-tien-do",
        "korean": "지체상금",
        "vietnamese": "Tiền phạt chậm tiến độ",
        "hanja": "遲滯償金",
        "hanjaReading": "遲(더딜 지) + 滯(막힐 체) + 償(갚을 상) + 金(쇠 금)",
        "pronunciation": "띠엔 팟 참 띠엔 도",
        "meaningKo": "공사가 계약상 완공일을 넘어 지연될 경우 시공사가 발주자에게 지급하는 손해배상금을 의미합니다. 일반적으로 지연 일수당 총 공사비의 일정 비율(예: 0.1~0.5%/일)로 계산되며, 상한선(총 공사비의 10~20%)이 정해져 있습니다. 통역 시 주의사항: 한국에서는 '지체상금', '지체보상금', '연체료' 등으로 표현하며, 베트남에서는 'Tiền phạt chậm tiến độ' 또는 'Tiền phạt vi phạm hợp đồng'이라고 합니다. 지체상금 산정 기준(일수, 비율, 상한), 면책 조건(천재지변, 발주자 귀책 사유), 공제 방식(기성금 또는 준공금에서 차감) 등을 명확히 전달하세요.",
        "meaningVi": "Khoản tiền bồi thường mà nhà thầu phải trả cho chủ đầu tư khi công trình chậm so với thời gian hoàn thành trong hợp đồng. Thường được tính theo tỷ lệ phần trăm giá trị hợp đồng trên mỗi ngày chậm (ví dụ: 0.1-0.5%/ngày), với mức tối đa (10-20% tổng giá trị hợp đồng).",
        "context": "공사 지연, 준공 검사, 대금 정산",
        "culturalNote": "한국 건설업계에서는 지체상금 조항이 표준계약서에 포함되어 있으며, 공공 공사의 경우 법적으로 강제됩니다. 다만 천재지변, 발주자 귀책 사유, 설계변경 등 정당한 사유가 있으면 공기 연장을 신청하여 지체상금을 면할 수 있습니다. 베트남에서도 유사한 제도가 있지만, 지체상금 비율과 상한이 계약마다 다르며, 실제 적용이 느슨한 경우도 있습니다. 한국 발주처는 지체상금을 엄격히 적용하므로, 공기 관리와 연장 신청을 철저히 해야 합니다.",
        "commonMistakes": [
            {
                "mistake": "'지체상금'을 'Tiền phạt'로만 축약",
                "correction": "'Tiền phạt chậm tiến độ' 또는 'Tiền phạt vi phạm hợp đồng'으로 구체화",
                "explanation": "'Tiền phạt'만으로는 무엇에 대한 벌금인지 불명확합니다"
            },
            {
                "mistake": "지체상금 상한을 언급하지 않음",
                "correction": "총 공사비의 10~20% 등 상한을 명시",
                "explanation": "무제한 지체상금은 시공사에게 과도한 부담이 됩니다"
            },
            {
                "mistake": "면책 조건을 설명하지 않음",
                "correction": "천재지변, 발주자 귀책 등 면책 사유 설명",
                "explanation": "정당한 사유가 있으면 지체상금을 면할 수 있으므로 중요합니다"
            }
        ],
        "examples": [
            {
                "ko": "공사 지연 시 일당 총 공사비의 0.2%를 지체상금으로 부과합니다.",
                "vi": "Khi chậm tiến độ, sẽ phạt 0.2% tổng giá trị hợp đồng mỗi ngày.",
                "situation": "formal"
            },
            {
                "ko": "지체상금 상한은 총 공사비의 15%입니다.",
                "vi": "Mức tối đa tiền phạt chậm tiến độ là 15% tổng giá trị hợp đồng.",
                "situation": "formal"
            },
            {
                "ko": "천재지변으로 인한 지연은 지체상금 대상이 아닙니다.",
                "vi": "Chậm tiến độ do thiên tai không bị phạt.",
                "situation": "onsite"
            }
        ],
        "relatedTerms": ["공사기간", "공기연장", "준공일", "계약위반"]
    }
]

def load_existing_terms():
    """기존 용어 데이터 로드"""
    if not terms_file.exists():
        print(f"❌ 오류: {terms_file} 파일을 찾을 수 없습니다.")
        sys.exit(1)

    with open(terms_file, 'r', encoding='utf-8') as f:
        data = json.load(f)

    return data

def add_terms(data, new_terms):
    """새 용어 추가 (중복 체크)"""
    existing_slugs = {term['slug'] for term in data}
    added = 0
    skipped = 0

    for term in new_terms:
        if term['slug'] in existing_slugs:
            print(f"⚠️  건너뜀 (중복): {term['slug']}")
            skipped += 1
        else:
            data.append(term)
            print(f"✅ 추가: {term['slug']} - {term['korean']}")
            added += 1

    return data, added, skipped

def save_terms(data):
    """용어 데이터 저장"""
    with open(terms_file, 'w', encoding='utf-8') as f:
        json.dump(data, f, ensure_ascii=False, indent=2)

    print(f"\n💾 저장 완료: {terms_file}")

def main():
    print("🏗️  건설 용어 추가 - Contract & Administration (계약/행정)")
    print(f"📂 파일: {terms_file}\n")

    # 1. 기존 데이터 로드
    data = load_existing_terms()
    print(f"📊 기존 용어 수: {len(data)}개\n")

    # 2. 새 용어 추가
    data, added, skipped = add_terms(data, new_terms)

    # 3. 저장
    save_terms(data)

    # 4. 결과 출력
    print(f"\n📈 최종 용어 수: {len(data)}개")
    print(f"✅ 추가: {added}개")
    print(f"⚠️  건너뜀: {skipped}개")
    print("\n✨ 완료!")

if __name__ == "__main__":
    main()
