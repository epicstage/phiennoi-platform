#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""행정소송법 용어 추가 스크립트 (v7-f)"""

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
            "slug": "hanh-chanh-xu-phan-thu-tieu",
            "korean": "행정처분취소",
            "vietnamese": "Thu hồi quyết định hành chính",
            "hanja": "行政處分取消",
            "hanjaReading": "行(다닐 행) 政(정사 정) 處(곳 처) 分(나눌 분) 取(취할 취) 消(사라질 소)",
            "pronunciation": "행정처분취소",
            "meaningKo": "행정청의 위법하거나 부당한 처분을 법원이 무효화하는 행정소송의 가장 기본적인 유형입니다. 통역 시 주의할 점은 '취소'와 '무효'를 명확히 구분해야 하며, 베트남에서는 행정결정 취소가 한국보다 절차가 복잡하고 시간이 오래 걸린다는 점을 설명해야 합니다. 한국의 행정처분 취소소송은 처분이 있음을 안 날로부터 90일, 처분이 있은 날로부터 1년 이내에 제기해야 하는 제소기간 제한이 있습니다.",
            "meaningVi": "Thu hồi quyết định hành chính là loại vụ kiện hành chính cơ bản nhất, trong đó tòa án hủy bỏ quyết định trái pháp luật hoặc không hợp lý của cơ quan hành chính. Ở Việt Nam, thủ tục thu hồi quyết định hành chính phức tạp hơn và mất nhiều thời gian hơn so với Hàn Quốc.",
            "context": "행정소송에서 위법한 행정처분에 대한 구제를 구하는 경우에 사용",
            "culturalNote": "한국은 행정처분 취소소송이 매우 활발하고 국민의 권리구제 수단으로 널리 활용되는 반면, 베트남은 행정소송 제도가 상대적으로 덜 발달되어 있으며 행정청의 결정에 대한 사법심사가 제한적입니다. 한국에서는 처분의 취소와 무효를 명확히 구분하지만, 베트남 법체계에서는 이러한 구분이 덜 엄격합니다.",
            "commonMistakes": [
                {
                    "mistake": "취소와 무효를 구분하지 않고 통역",
                    "correction": "취소(thu hồi)는 소급효가 없고, 무효(vô hiệu)는 처음부터 효력이 없음을 명확히 구분",
                    "explanation": "법적 효과가 완전히 다르므로 정확한 구분 필수"
                },
                {
                    "mistake": "'행정처분'을 'xử phạt hành chính'(행정처벌)로 잘못 번역",
                    "correction": "'quyết định hành chính'(행정결정)으로 정확히 번역",
                    "explanation": "처분은 처벌보다 넓은 개념으로 인허가, 등록 등 포함"
                },
                {
                    "mistake": "제소기간을 설명 없이 통역",
                    "correction": "90일/1년 제한과 베트남의 다른 기간을 함께 설명",
                    "explanation": "양국의 제소기간이 다르므로 오해 방지 필요"
                }
            ],
            "examples": [
                {
                    "ko": "영업허가 취소처분에 불복하여 행정처분 취소소송을 제기하였습니다.",
                    "vi": "Tôi đã khởi kiện yêu cầu thu hồi quyết định thu hồi giấy phép kinh doanh.",
                    "situation": "formal"
                },
                {
                    "ko": "법원은 해당 행정처분이 위법하다고 판단하여 취소 판결을 내렸습니다.",
                    "vi": "Tòa án đã ra phán quyết hủy bỏ quyết định hành chính đó vì vi phạm pháp luật.",
                    "situation": "formal"
                },
                {
                    "ko": "행정처분 취소소송은 처분이 있음을 안 날부터 90일 이내에 제기해야 합니다.",
                    "vi": "Vụ kiện thu hồi quyết định hành chính phải được khởi kiện trong vòng 90 ngày kể từ ngày biết có quyết định.",
                    "situation": "formal"
                }
            ],
            "relatedTerms": ["행정소송", "제소기간", "원고적격", "집행정지"]
        },
        {
            "slug": "nghia-vu-y-hanh-to-tung",
            "korean": "의무이행소송",
            "vietnamese": "Vụ kiện buộc thực hiện nghĩa vụ",
            "hanja": "義務履行訴訟",
            "hanjaReading": "義(옳을 의) 務(힘쓸 무) 履(밟을 리) 行(다닐 행) 訴(호소할 소) 訟(송사 송)",
            "pronunciation": "의무이행소송",
            "meaningKo": "행정청이 법령상 당연히 해야 할 의무를 이행하지 않을 때, 법원에 그 의무의 이행을 명하는 판결을 구하는 소송입니다. 통역 시 '부작위 위법확인소송'과의 차이를 명확히 설명해야 하며, 한국에서는 2020년 행정소송법 개정으로 의무이행소송이 본격적으로 도입되었다는 점을 안내해야 합니다. 이는 국민의 권리구제를 강화하는 중요한 제도로, 행정청의 거부처분 뿐 아니라 아무런 처분도 하지 않는 부작위에 대해서도 소송을 제기할 수 있습니다.",
            "meaningVi": "Vụ kiện buộc thực hiện nghĩa vụ là loại vụ kiện yêu cầu tòa án ra phán quyết bắt buộc cơ quan hành chính thực hiện nghĩa vụ theo quy định pháp luật khi họ không thực hiện. Đây là chế độ được tăng cường ở Hàn Quốc từ năm 2020 nhằm bảo vệ quyền lợi của công dân tốt hơn.",
            "context": "행정청이 신청을 거부하거나 응답하지 않을 때 사용",
            "culturalNote": "한국은 2020년 행정소송법 개정을 통해 의무이행소송을 정식으로 도입하여 국민의 권리구제를 대폭 강화했습니다. 이전에는 부작위 위법확인소송만 가능했으나, 이제는 직접 의무이행을 구할 수 있습니다. 베트남에서는 이러한 소송 유형이 명확히 구분되지 않으며, 행정청의 부작위에 대한 사법구제가 제한적입니다.",
            "commonMistakes": [
                {
                    "mistake": "'부작위 위법확인소송'과 혼동하여 통역",
                    "correction": "부작위 위법확인은 위법만 확인, 의무이행소송은 직접 이행 명령",
                    "explanation": "법적 효과가 완전히 다른 별개의 소송 유형"
                },
                {
                    "mistake": "'의무'를 'trách nhiệm'(책임)으로 잘못 번역",
                    "correction": "'nghĩa vụ'(의무)로 정확히 번역",
                    "explanation": "법적 의무와 일반적 책임은 다른 개념"
                },
                {
                    "mistake": "2020년 개정 내용을 설명하지 않음",
                    "correction": "의무이행소송이 새로 도입된 제도임을 명확히 설명",
                    "explanation": "제도의 취지와 의의를 이해해야 정확한 통역 가능"
                }
            ],
            "examples": [
                {
                    "ko": "건축허가 신청에 대한 행정청의 거부처분에 대해 의무이행소송을 제기했습니다.",
                    "vi": "Tôi đã khởi kiện buộc thực hiện nghĩa vụ đối với quyết định từ chối cấp giấy phép xây dựng của cơ quan hành chính.",
                    "situation": "formal"
                },
                {
                    "ko": "의무이행소송은 행정청에게 직접 처분을 하도록 명령하는 판결을 구하는 것입니다.",
                    "vi": "Vụ kiện buộc thực hiện nghĩa vụ là yêu cầu tòa án ra phán quyết bắt buộc cơ quan hành chính phải ra quyết định trực tiếp.",
                    "situation": "formal"
                },
                {
                    "ko": "의무이행소송은 부작위 위법확인소송보다 실효성이 높습니다.",
                    "vi": "Vụ kiện buộc thực hiện nghĩa vụ có hiệu lực cao hơn vụ kiện xác nhận hành vi không hành động là trái pháp luật.",
                    "situation": "formal"
                }
            ],
            "relatedTerms": ["행정처분취소", "부작위", "행정소송", "원고적격"]
        },
        {
            "slug": "hanh-chanh-tam-phan",
            "korean": "행정심판",
            "vietnamese": "Tái thẩm hành chính",
            "hanja": "行政審判",
            "hanjaReading": "行(다닐 행) 政(정사 정) 審(살필 심) 判(판단할 판)",
            "pronunciation": "행정심판",
            "meaningKo": "행정청의 위법·부당한 처분이나 부작위에 대하여 행정기관이 스스로 시정하도록 하는 행정쟁송 절차로, 법원에 가기 전 행정 내부에서 먼저 다투는 제도입니다. 통역 시 행정소송과의 차이를 명확히 해야 하며, 한국에서는 행정심판을 거치지 않고 바로 행정소송을 제기할 수 있다는 '임의적 전심절차'임을 설명해야 합니다. 행정심판은 소송보다 빠르고 비용이 적게 들며, 전문성이 요구되는 사안에서 유리할 수 있으나, 법원의 판결과 같은 강제력은 없습니다.",
            "meaningVi": "Tái thẩm hành chính là thủ tục tranh chấp hành chính trong đó cơ quan hành chính tự điều chỉnh các quyết định trái pháp luật hoặc không hợp lý, là giai đoạn trước khi đi kiện tòa. Ở Hàn Quốc, đây là thủ tục tùy chọn, có thể bỏ qua và khởi kiện trực tiếp.",
            "context": "행정처분에 불복할 때 법원 제소 전에 고려하는 절차",
            "culturalNote": "한국에서는 행정심판이 임의적 전심절차여서 거치지 않고 바로 행정소송을 제기할 수 있지만, 베트남에서는 많은 경우 행정심판을 필수적으로 거쳐야 법원에 제소할 수 있습니다. 또한 한국의 행정심판위원회는 상당한 독립성을 가지고 있으나, 베트남에서는 행정기관의 영향력이 더 큽니다. 한국에서는 행정심판이 활발하게 이용되며, 인용률도 비교적 높은 편입니다.",
            "commonMistakes": [
                {
                    "mistake": "행정심판과 행정소송을 같은 것으로 혼동",
                    "correction": "행정심판은 행정기관 내부, 행정소송은 법원에서 진행됨을 명확히 구분",
                    "explanation": "절차와 효력이 완전히 다름"
                },
                {
                    "mistake": "필수적 전심절차로 잘못 설명",
                    "correction": "한국에서는 임의적 전심절차로 선택 가능함을 설명",
                    "explanation": "베트남과 달리 한국은 선택적"
                },
                {
                    "mistake": "'심판'을 'phán quyết'(판결)로 번역",
                    "correction": "'tái thẩm'(재심사) 또는 'phúc thẩm hành chính'으로 번역",
                    "explanation": "법원 판결이 아닌 행정 내부 심사 절차"
                }
            ],
            "examples": [
                {
                    "ko": "행정소송을 제기하기 전에 행정심판을 먼저 청구하는 것이 유리할 수 있습니다.",
                    "vi": "Có thể có lợi khi yêu cầu tái thẩm hành chính trước khi khởi kiện hành chính.",
                    "situation": "formal"
                },
                {
                    "ko": "행정심판위원회는 60일 이내에 재결을 해야 합니다.",
                    "vi": "Ủy ban tái thẩm hành chính phải ra quyết định tái thẩm trong vòng 60 ngày.",
                    "situation": "formal"
                },
                {
                    "ko": "행정심판은 행정소송보다 빠르고 비용이 적게 듭니다.",
                    "vi": "Tái thẩm hành chính nhanh hơn và tốn ít chi phí hơn so với vụ kiện hành chính.",
                    "situation": "onsite"
                }
            ],
            "relatedTerms": ["행정소송", "행정처분취소", "재결", "전심절차"]
        },
        {
            "slug": "chip-hanh-chanh-chi",
            "korean": "집행정지",
            "vietnamese": "Đình chỉ thi hành",
            "hanja": "執行停止",
            "hanjaReading": "執(잡을 집) 行(다닐 행) 停(머무를 정) 止(그칠 지)",
            "pronunciation": "집행정지",
            "meaningKo": "행정처분의 효력이나 집행을 임시로 정지시키는 제도로, 행정소송이나 행정심판 중에 처분의 집행으로 인해 회복하기 어려운 손해가 발생하는 것을 막기 위한 긴급구제 수단입니다. 통역 시 '집행부정지 원칙'이 원칙이지만 예외적으로 인정된다는 점을 설명해야 하며, 집행정지 결정을 받기 위해서는 '회복하기 어려운 손해', '긴급한 필요', '본안 승소 가능성' 등을 입증해야 합니다. 특히 건축 철거나 영업정지 같은 경우 집행정지가 매우 중요합니다.",
            "meaningVi": "Đình chỉ thi hành là chế độ tạm dừng hiệu lực hoặc thi hành quyết định hành chính, là biện pháp cứu trợ khẩn cấp nhằm ngăn chặn thiệt hại khó khắc phục xảy ra do việc thi hành quyết định trong quá trình xét xử vụ kiện hành chính hoặc tái thẩm hành chính.",
            "context": "행정소송이나 행정심판 제기 시 처분 집행으로 인한 피해를 막기 위해 신청",
            "culturalNote": "한국에서는 '집행부정지 원칙'이 적용되어 소송이나 심판을 제기해도 처분의 집행은 계속되는 것이 원칙이지만, 회복하기 어려운 손해를 막기 위해 예외적으로 집행정지가 인정됩니다. 베트남에서도 유사한 제도가 있으나, 집행정지 인용률이 한국보다 낮고 요건이 더 엄격합니다. 한국에서는 건축 철거, 영업정지, 자격정지 등의 경우 집행정지 신청이 활발합니다.",
            "commonMistakes": [
                {
                    "mistake": "집행정지가 자동으로 인정된다고 설명",
                    "correction": "예외적 제도로 엄격한 요건 충족 필요함을 명확히",
                    "explanation": "집행부정지가 원칙임을 이해해야 함"
                },
                {
                    "mistake": "'정지'를 'tạm ngừng'(일시중지)로만 번역",
                    "correction": "'đình chỉ thi hành'(집행정지)이라는 법률 용어 사용",
                    "explanation": "법적 절차의 정식 명칭 사용 필요"
                },
                {
                    "mistake": "집행정지와 처분 취소를 혼동",
                    "correction": "집행정지는 임시조치, 취소는 본안 판결임을 구분",
                    "explanation": "집행정지는 나중에 취소될 수도 있는 임시적 조치"
                }
            ],
            "examples": [
                {
                    "ko": "건물 철거 명령의 집행정지를 신청하여 인용되었습니다.",
                    "vi": "Tôi đã nộp đơn xin đình chỉ thi hành lệnh phá dỡ công trình và được chấp thuận.",
                    "situation": "formal"
                },
                {
                    "ko": "집행정지 결정을 받으려면 회복하기 어려운 손해가 있음을 소명해야 합니다.",
                    "vi": "Để được quyết định đình chỉ thi hành, cần chứng minh có thiệt hại khó khắc phục.",
                    "situation": "formal"
                },
                {
                    "ko": "영업정지 처분에 대해 집행정지를 신청하지 않으면 영업을 중단해야 합니다.",
                    "vi": "Nếu không nộp đơn đình chỉ thi hành quyết định đình chỉ kinh doanh, phải ngừng kinh doanh.",
                    "situation": "onsite"
                }
            ],
            "relatedTerms": ["행정처분취소", "행정소송", "집행부정지원칙", "가처분"]
        },
        {
            "slug": "xu-phan-i-do-chu-ga",
            "korean": "처분사유추가",
            "vietnamese": "Bổ sung lý do quyết định",
            "hanja": "處分事由追加",
            "hanjaReading": "處(곳 처) 分(나눌 분) 事(일 사) 由(말미암을 유) 追(쫓을 추) 加(더할 가)",
            "pronunciation": "처분사유추가",
            "meaningKo": "행정청이 당초 처분을 할 때 제시한 사유와 기본적 사실관계가 동일한 범위에서 소송 과정 중에 새로운 사유를 추가하거나 변경할 수 있는 제도입니다. 통역 시 '기본적 사실관계의 동일성' 범위 내에서만 가능하며, 완전히 새로운 사유는 추가할 수 없다는 점을 명확히 해야 합니다. 이는 행정청의 방어권을 보장하면서도 국민의 절차적 권리를 침해하지 않도록 균형을 맞추는 제도로, 실무에서 자주 문제되는 쟁점입니다.",
            "meaningVi": "Bổ sung lý do quyết định là chế độ cho phép cơ quan hành chính bổ sung hoặc thay đổi lý do mới trong quá trình kiện tụng trong phạm vi quan hệ sự thật cơ bản giống với lý do đưa ra ban đầu khi ra quyết định. Đây là vấn đề tranh cãi thường xuyên trong thực tiễn.",
            "context": "행정소송에서 행정청이 처분의 정당성을 입증하기 위해 새로운 근거를 제시할 때",
            "culturalNote": "한국 판례는 처분사유 추가를 엄격하게 제한하여 '기본적 사실관계의 동일성' 범위 내에서만 허용합니다. 이는 국민의 방어권과 예측가능성을 보호하기 위한 것입니다. 베트남에서는 이러한 제한이 상대적으로 느슨하여 행정청이 소송 중에 사유를 변경하는 것이 더 용이합니다. 한국에서는 처분사유 추가가 인정되는지 여부가 소송의 승패를 좌우하는 중요한 쟁점이 됩니다.",
            "commonMistakes": [
                {
                    "mistake": "아무 사유나 추가할 수 있다고 설명",
                    "correction": "'기본적 사실관계의 동일성' 범위 내로 엄격히 제한됨을 명확히",
                    "explanation": "무제한 추가는 국민의 방어권 침해"
                },
                {
                    "mistake": "'추가'를 단순히 'thêm'(더하다)로만 번역",
                    "correction": "'bổ sung lý do'(사유 보충)이라는 법적 맥락 포함",
                    "explanation": "법적 절차의 의미를 담아야 함"
                },
                {
                    "mistake": "처분사유 추가와 처분 변경을 혼동",
                    "correction": "사유 추가는 같은 처분 내에서, 처분 변경은 다른 처분으로 바꾸는 것",
                    "explanation": "법적 성질이 다름"
                }
            ],
            "examples": [
                {
                    "ko": "행정청이 소송 중 처분사유를 추가했으나, 기본적 사실관계가 다르다고 판단되어 인정되지 않았습니다.",
                    "vi": "Cơ quan hành chính đã bổ sung lý do quyết định trong quá trình kiện tụng nhưng không được chấp nhận vì quan hệ sự thật cơ bản khác nhau.",
                    "situation": "formal"
                },
                {
                    "ko": "처분사유의 추가는 원칙적으로 허용되지 않지만, 기본적 사실관계가 동일하면 예외적으로 인정됩니다.",
                    "vi": "Về nguyên tắc không cho phép bổ sung lý do quyết định, nhưng có thể được chấp nhận nếu quan hệ sự thật cơ bản giống nhau.",
                    "situation": "formal"
                },
                {
                    "ko": "당초 처분 이유와 완전히 다른 사유는 처분사유 추가로 인정되지 않습니다.",
                    "vi": "Lý do hoàn toàn khác với lý do quyết định ban đầu không được chấp nhận là bổ sung lý do quyết định.",
                    "situation": "formal"
                }
            ],
            "relatedTerms": ["행정처분취소", "행정소송", "처분의 동일성", "기본적 사실관계"]
        },
        {
            "slug": "nguyen-cao-chok-kyok",
            "korean": "원고적격",
            "vietnamese": "Tư cách nguyên đơn",
            "hanja": "原告適格",
            "hanjaReading": "原(근원 원) 告(고할 고) 適(맞을 적) 格(격식 격)",
            "pronunciation": "원고적격",
            "meaningKo": "행정소송을 제기할 수 있는 법률상 자격으로, '법률상 이익'이 있는 자만 원고가 될 수 있습니다. 통역 시 단순한 사실상·경제상 이익이 아닌 '법률상 보호되는 이익'이어야 한다는 점을 명확히 해야 하며, 최근 판례는 원고적격을 넓게 인정하는 추세라는 점도 설명해야 합니다. 제3자가 타인에 대한 처분의 취소를 구하는 경우 특히 원고적격이 문제되며, 환경소송이나 도시계획 소송에서 자주 쟁점이 됩니다.",
            "meaningVi": "Tư cách nguyên đơn là tư cách pháp lý để khởi kiện hành chính, chỉ người có 'lợi ích theo pháp luật' mới có thể làm nguyên đơn. Gần đây, án lệ có xu hướng công nhận tư cách nguyên đơn rộng hơn, đặc biệt trong các vụ kiện môi trường và quy hoạch đô thị.",
            "context": "행정소송 제기 시 원고가 될 수 있는 자격이 있는지 판단할 때",
            "culturalNote": "한국에서는 '법률상 이익'이 있어야 원고적격이 인정되며, 단순히 사실상 불이익을 받는 것만으로는 부족합니다. 최근 대법원 판례는 환경권이나 경쟁업자의 이익 등을 넓게 인정하는 추세입니다. 베트남에서도 유사하게 법적 이익이 있어야 하나, 제3자의 소송 제기가 한국보다 제한적입니다. 한국에서는 원고적격 인정 범위가 소송의 입구를 결정하는 중요한 요소입니다.",
            "commonMistakes": [
                {
                    "mistake": "사실상 불이익만 있어도 원고가 될 수 있다고 설명",
                    "correction": "'법률상 이익'이 있어야 함을 명확히",
                    "explanation": "법률상 보호받는 이익과 단순 불이익은 다름"
                },
                {
                    "mistake": "'적격'을 'đủ điều kiện'(조건 충족)로만 번역",
                    "correction": "'tư cách'(자격)이라는 법적 지위 개념 포함",
                    "explanation": "법적 자격의 의미를 담아야 함"
                },
                {
                    "mistake": "모든 이해관계인이 원고가 될 수 있다고 설명",
                    "correction": "법률상 보호되는 이익이 있는 자로 제한됨을 설명",
                    "explanation": "원고적격은 제한적 개념"
                }
            ],
            "examples": [
                {
                    "ko": "경쟁업체가 타사에 대한 인허가 처분의 취소를 구하려면 원고적격이 인정되어야 합니다.",
                    "vi": "Để công ty cạnh tranh yêu cầu hủy bỏ quyết định cấp phép cho công ty khác, cần được công nhận tư cách nguyên đơn.",
                    "situation": "formal"
                },
                {
                    "ko": "단순히 경제적 손해를 입었다는 것만으로는 원고적격이 인정되지 않습니다.",
                    "vi": "Chỉ bị thiệt hại kinh tế đơn thuần không đủ để được công nhận tư cách nguyên đơn.",
                    "situation": "formal"
                },
                {
                    "ko": "환경 소송에서는 인근 주민의 원고적격이 넓게 인정되는 추세입니다.",
                    "vi": "Trong các vụ kiện môi trường, có xu hướng công nhận rộng rãi tư cách nguyên đơn của cư dân lân cận.",
                    "situation": "onsite"
                }
            ],
            "relatedTerms": ["행정소송", "법률상 이익", "제3자 소송", "당사자적격"]
        },
        {
            "slug": "che-so-ki-gan",
            "korean": "제소기간",
            "vietnamese": "Thời hạn khởi kiện",
            "hanja": "提訴期間",
            "hanjaReading": "提(끌어올릴 제) 訴(호소할 소) 期(기약할 기) 間(사이 간)",
            "pronunciation": "제소기간",
            "meaningKo": "행정소송을 제기할 수 있는 법정 기간으로, 처분이 있음을 안 날로부터 90일, 처분이 있은 날로부터 1년 이내에 제기해야 합니다. 통역 시 이 기간을 넘기면 적법한 처분도 다툴 수 없게 된다는 점을 강조해야 하며, '안 날'의 기산점 계산이 중요하다는 점을 설명해야 합니다. 행정심판을 제기한 경우 재결서를 받은 날부터 90일이 기산되며, 정당한 사유가 있으면 예외적으로 기간이 연장될 수 있지만 매우 제한적입니다.",
            "meaningVi": "Thời hạn khởi kiện là thời hạn pháp định để khởi kiện hành chính, phải khởi kiện trong vòng 90 ngày kể từ ngày biết có quyết định và trong vòng 1 năm kể từ ngày có quyết định. Nếu quá thời hạn này, không thể tranh chấp ngay cả quyết định trái pháp luật.",
            "context": "행정소송 제기 시 기간 준수 여부를 판단할 때",
            "culturalNote": "한국의 제소기간은 90일/1년으로 상당히 짧은 편이며, 이는 법적 안정성을 위한 것입니다. 베트남의 제소기간과 비교하여 설명할 필요가 있으며, 베트남은 제소기간이 더 길거나 유연한 경우가 많습니다. 한국에서는 제소기간 도과로 각하되는 사례가 많아 기간 관리가 매우 중요하며, '안 날'의 입증이 분쟁이 되기도 합니다.",
            "commonMistakes": [
                {
                    "mistake": "처분이 있은 날부터만 계산",
                    "correction": "'안 날'과 '있은 날' 두 가지 기준 모두 설명",
                    "explanation": "두 기간 중 하나라도 지키면 적법"
                },
                {
                    "mistake": "제소기간을 '시효'로 설명",
                    "correction": "소송 제기 기간이지 권리 소멸 시효가 아님을 구분",
                    "explanation": "법적 성질이 다름"
                },
                {
                    "mistake": "기간 연장이 쉽게 인정된다고 설명",
                    "correction": "정당한 사유가 있는 예외적 경우에만 가능함을 명확히",
                    "explanation": "원칙적으로 불변기간"
                }
            ],
            "examples": [
                {
                    "ko": "처분 통지를 받은 날로부터 90일 이내에 소송을 제기해야 합니다.",
                    "vi": "Phải khởi kiện trong vòng 90 ngày kể từ ngày nhận được thông báo quyết định.",
                    "situation": "formal"
                },
                {
                    "ko": "제소기간이 지나면 소송이 각하되어 본안 판단을 받을 수 없습니다.",
                    "vi": "Nếu quá thời hạn khởi kiện, vụ kiện sẽ bị bác và không được xem xét nội dung.",
                    "situation": "formal"
                },
                {
                    "ko": "행정심판 재결을 받은 후에는 그 날부터 다시 90일의 제소기간이 진행됩니다.",
                    "vi": "Sau khi nhận được quyết định tái thẩm hành chính, thời hạn khởi kiện 90 ngày bắt đầu lại từ ngày đó.",
                    "situation": "onsite"
                }
            ],
            "relatedTerms": ["행정소송", "행정심판", "불변기간", "각하"]
        },
        {
            "slug": "kuk-ka-be-sang",
            "korean": "국가배상",
            "vietnamese": "Bồi thường của nhà nước",
            "hanja": "國家賠償",
            "hanjaReading": "國(나라 국) 家(집 가) 賠(갚을 배) 償(갚을 상)",
            "pronunciation": "국가배상",
            "meaningKo": "공무원의 직무상 불법행위나 영조물의 설치·관리 하자로 국민이 손해를 입었을 때 국가나 지방자치단체가 그 손해를 배상하는 제도입니다. 통역 시 '고의 또는 과실', '위법성', '손해', '인과관계'의 네 가지 요건을 모두 충족해야 한다는 점을 명확히 해야 하며, 공무원 개인이 아닌 국가가 배상 책임을 진다는 점을 설명해야 합니다. 민법상 불법행위와 달리 국가배상법이 특별법으로 적용되며, 배상액 산정 기준도 다릅니다.",
            "meaningVi": "Bồi thường của nhà nước là chế độ trong đó nhà nước hoặc chính quyền địa phương bồi thường thiệt hại khi công dân bị thiệt hại do hành vi trái pháp luật của công chức trong khi thi hành công vụ hoặc do lỗi trong việc lắp đặt, quản lý công trình công cộng.",
            "context": "공무원의 불법행위나 공공시설의 하자로 피해를 입은 경우",
            "culturalNote": "한국의 국가배상제도는 헌법과 국가배상법에 근거하여 국민의 권리구제를 두텁게 보장합니다. 공무원 개인은 고의나 중과실이 없는 한 책임을 지지 않고 국가가 책임을 부담하며, 나중에 국가가 공무원에게 구상권을 행사합니다. 베트남도 유사한 제도가 있으나, 실제 배상 인정률과 배상액이 한국보다 낮은 편입니다. 한국에서는 국가배상 청구가 활발하며, 군대 사고, 경찰 과잉진압, 도로 하자 등 다양한 사례가 있습니다.",
            "commonMistakes": [
                {
                    "mistake": "공무원 개인에게 배상을 청구할 수 있다고 설명",
                    "correction": "원칙적으로 국가가 배상하고, 국가가 공무원에게 구상권 행사",
                    "explanation": "국가배상법의 기본 원리"
                },
                {
                    "mistake": "민법상 불법행위와 동일하게 설명",
                    "correction": "국가배상법이 특별법으로 우선 적용됨을 명확히",
                    "explanation": "법 적용 순서가 다름"
                },
                {
                    "mistake": "'배상'을 'bồi hoàn'(보전)으로 잘못 번역",
                    "correction": "'bồi thường'(배상)으로 정확히 번역",
                    "explanation": "법적 용어의 정확성"
                }
            ],
            "examples": [
                {
                    "ko": "경찰의 과잉진압으로 다친 경우 국가배상을 청구할 수 있습니다.",
                    "vi": "Có thể yêu cầu bồi thường của nhà nước nếu bị thương do cảnh sát đàn áp quá mức.",
                    "situation": "formal"
                },
                {
                    "ko": "도로의 관리 하자로 사고가 발생한 경우 영조물 배상책임이 인정됩니다.",
                    "vi": "Nếu xảy ra tai nạn do lỗi quản lý đường, trách nhiệm bồi thường công trình công cộng được công nhận.",
                    "situation": "formal"
                },
                {
                    "ko": "국가배상 청구는 손해가 발생한 날로부터 5년 이내에 해야 합니다.",
                    "vi": "Yêu cầu bồi thường của nhà nước phải được nộp trong vòng 5 năm kể từ ngày xảy ra thiệt hại.",
                    "situation": "onsite"
                }
            ],
            "relatedTerms": ["손실보상", "불법행위", "영조물", "공무원"]
        },
        {
            "slug": "son-sil-bo-sang",
            "korean": "손실보상",
            "vietnamese": "Bồi thường tổn thất",
            "hanja": "損失補償",
            "hanjaReading": "損(덜 손) 失(잃을 실) 補(기울 보) 償(갚을 상)",
            "pronunciation": "손실보상",
            "meaningKo": "국가나 지방자치단체의 적법한 공권력 행사로 인해 특정인이 재산상 특별한 희생을 한 경우, 공평 부담의 원칙에 따라 국가 등이 그 손실을 보상하는 제도입니다. 통역 시 국가배상과 달리 '적법한' 행위로 인한 손실을 보상한다는 점을 명확히 구분해야 하며, 토지수용이나 개발제한구역 지정 등이 대표적 사례임을 설명해야 합니다. 손실보상은 재산권 보장의 중요한 수단이며, '정당한 보상'이 헌법상 보장되어 있습니다.",
            "meaningVi": "Bồi thường tổn thất là chế độ trong đó nhà nước hoặc chính quyền địa phương bồi thường thiệt hại khi người cụ thể phải hy sinh tài sản đặc biệt do việc thực thi quyền lực công hợp pháp, theo nguyên tắc gánh chịu công bằng.",
            "context": "토지수용, 개발제한, 영업제한 등 적법한 공권력으로 재산상 손실을 입은 경우",
            "culturalNote": "한국에서는 손실보상과 국가배상을 명확히 구분합니다. 손실보상은 적법한 행위로 인한 것이고, 국가배상은 위법한 행위로 인한 것입니다. 헌법 제23조 제3항은 '정당한 보상'을 보장하며, 이는 원칙적으로 시가(時價)를 의미합니다. 베트남에서도 토지수용 시 보상이 이루어지나, 보상 수준이나 절차가 한국과 다릅니다. 한국에서는 토지보상법 등 상세한 법령이 보상 기준을 규정하고 있습니다.",
            "commonMistakes": [
                {
                    "mistake": "국가배상과 손실보상을 구분하지 않고 사용",
                    "correction": "적법한 행위는 손실보상, 위법한 행위는 국가배상임을 명확히",
                    "explanation": "법적 근거와 요건이 완전히 다름"
                },
                {
                    "mistake": "'보상'을 'bồi thường'(배상)으로만 번역",
                    "correction": "손실보상은 'bồi thường tổn thất', 국가배상은 'bồi thường của nhà nước'로 구분",
                    "explanation": "법적 개념이 다름"
                },
                {
                    "mistake": "보상액이 시가보다 낮아도 된다고 설명",
                    "correction": "헌법상 '정당한 보상'은 원칙적으로 완전보상(시가)임을 명확히",
                    "explanation": "헌법적 보장 수준"
                }
            ],
            "examples": [
                {
                    "ko": "도로 건설을 위한 토지수용에 대해 손실보상을 받을 수 있습니다.",
                    "vi": "Có thể nhận bồi thường tổn thất do thu hồi đất để xây dựng đường.",
                    "situation": "formal"
                },
                {
                    "ko": "개발제한구역 지정으로 재산권 행사가 제한되면 손실보상을 청구할 수 있습니다.",
                    "vi": "Nếu việc chỉ định khu vực hạn chế phát triển hạn chế quyền tài sản, có thể yêu cầu bồi thường tổn thất.",
                    "situation": "formal"
                },
                {
                    "ko": "손실보상액에 불복하는 경우 토지수용위원회의 재결에 이의를 제기할 수 있습니다.",
                    "vi": "Nếu không đồng ý với số tiền bồi thường tổn thất, có thể phản đối quyết định của Ủy ban thu hồi đất.",
                    "situation": "onsite"
                }
            ],
            "relatedTerms": ["국가배상", "토지수용", "정당한보상", "재산권"]
        },
        {
            "slug": "hanh-chanh-cho-sa",
            "korean": "행정조사",
            "vietnamese": "Điều tra hành chính",
            "hanja": "行政調査",
            "hanjaReading": "行(다닐 행) 政(정사 정) 調(고를 조) 査(살필 사)",
            "pronunciation": "행정조사",
            "meaningKo": "행정기관이 정책을 결정하거나 직무를 수행하기 위해 필요한 정보나 자료를 수집하기 위하여 현장조사·문서열람·시료채취 등을 하거나 조사대상자에게 보고요구·자료제출요구 및 출석·진술요구를 하는 활동입니다. 통역 시 '행정조사기본법'에 따라 절차적 권리가 보장된다는 점을 명확히 해야 하며, 조사거부권이나 영장주의 예외 등 중요한 쟁점을 설명해야 합니다. 세무조사, 환경조사, 식품위생조사 등 다양한 유형이 있으며, 조사와 처분은 구별됩니다.",
            "meaningVi": "Điều tra hành chính là hoạt động của cơ quan hành chính thu thập thông tin hoặc tài liệu cần thiết để quyết định chính sách hoặc thực hiện nhiệm vụ thông qua điều tra hiện trường, xem xét tài liệu, lấy mẫu, hoặc yêu cầu đối tượng điều tra báo cáo, nộp tài liệu, có mặt và trình bày.",
            "context": "세무조사, 환경조사, 식품위생조사 등 행정기관의 조사를 받을 때",
            "culturalNote": "한국은 2007년 '행정조사기본법'을 제정하여 행정조사의 절차와 조사대상자의 권리를 명확히 규정했습니다. 조사 시 신분증 제시, 조사목적 고지, 조사범위 제한 등의 절차적 보장이 있으며, 야간조사나 영업시간 중 조사는 원칙적으로 제한됩니다. 베트남에서도 행정조사가 이루어지나, 절차적 보장 수준이 한국과 다를 수 있습니다. 한국에서는 부당한 행정조사에 대해 이의제기나 소송이 가능합니다.",
            "commonMistakes": [
                {
                    "mistake": "행정조사와 행정처분을 혼동",
                    "correction": "조사는 정보수집, 처분은 권리의무 변동임을 명확히 구분",
                    "explanation": "법적 성질이 다름"
                },
                {
                    "mistake": "조사에 무조건 응해야 한다고 설명",
                    "correction": "조사거부권이나 변호사 조력권 등 권리가 있음을 설명",
                    "explanation": "절차적 권리 보장"
                },
                {
                    "mistake": "'조사'를 'khám xét'(수색)로 잘못 번역",
                    "correction": "'điều tra hành chính'(행정조사)으로 정확히 번역",
                    "explanation": "수색은 형사절차로 성질이 다름"
                }
            ],
            "examples": [
                {
                    "ko": "세무서에서 행정조사를 실시한다는 통지를 받았습니다.",
                    "vi": "Tôi đã nhận được thông báo rằng cơ quan thuế sẽ tiến hành điều tra hành chính.",
                    "situation": "formal"
                },
                {
                    "ko": "행정조사를 받을 때는 조사 목적과 범위를 확인할 권리가 있습니다.",
                    "vi": "Khi bị điều tra hành chính, có quyền xác nhận mục đích và phạm vi điều tra.",
                    "situation": "formal"
                },
                {
                    "ko": "야간 행정조사는 원칙적으로 금지되며, 예외적인 경우에만 가능합니다.",
                    "vi": "Điều tra hành chính ban đêm về nguyên tắc bị cấm, chỉ có thể trong trường hợp ngoại lệ.",
                    "situation": "onsite"
                }
            ],
            "relatedTerms": ["행정처분", "세무조사", "조사거부권", "행정절차"]
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
