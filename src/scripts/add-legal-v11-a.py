#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""헌법재판/위헌심사 용어 추가 (v11-A)"""
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
            "slug": "toa-an-hien-phap",
            "korean": "헌법재판소",
            "vietnamese": "Tòa án Hiến pháp",
            "hanja": "憲法裁判所",
            "hanjaReading": "憲(법 헌) + 法(법 법) + 裁(재판할 재) + 判(판단할 판) + 所(곳 소)",
            "pronunciation": "헌법재판소",
            "meaningKo": "헌법재판소는 법률의 위헌 여부, 탄핵, 정당해산, 권한쟁의, 헌법소원 등을 심판하는 헌법기관입니다. 통역 시 주의할 점은 한국의 헌법재판소는 법원과 독립된 별도 기관이지만, 베트남에서는 국회 산하 기구로 운영된다는 차이가 있습니다. 한국에서는 9명의 재판관이 구성하며 6명 이상의 찬성으로 위헌 결정을 내리는 반면, 베트남은 국회의 결정에 자문하는 역할이 더 강합니다. 따라서 '독립성'과 '권한 범위'를 번역할 때 양국의 제도 차이를 명확히 전달해야 합니다.",
            "meaningVi": "Tòa án Hiến pháp là cơ quan tư pháp chuyên xem xét tính hợp hiến của luật pháp, đơn khiếu nại hiến pháp, luận tội, giải thể chính đảng và tranh chấp thẩm quyền. Ở Hàn Quốc, Tòa án Hiến pháp là cơ quan độc lập với hệ thống tòa án thông thường, trong khi ở Việt Nam thuộc Quốc hội.",
            "context": "헌법재판, 사법제도, 위헌심사",
            "culturalNote": "한국의 헌법재판소는 1988년 설립되어 강력한 위헌법률심사권을 가지고 있으며, 정치적 중립성과 독립성이 헌법으로 보장됩니다. 반면 베트남의 헌법재판 기능은 국회 산하 기구가 담당하며, 국회의 결정에 대한 자문 역할이 중심입니다. 통역 시 한국의 헌법재판소가 가진 '사법적 독립성'과 '최종 결정권'을 강조해야 합니다.",
            "commonMistakes": [
                {
                    "mistake": "Tòa án Tối cao (대법원)로 번역",
                    "correction": "Tòa án Hiến pháp",
                    "explanation": "대법원(Tòa án Tối cao)과 헌법재판소는 완전히 다른 기관입니다. 대법원은 일반 재판의 최고법원이고, 헌법재판소는 헌법 문제만 다룹니다."
                },
                {
                    "mistake": "Hội đồng Hiến pháp (헌법위원회)로 번역",
                    "correction": "Tòa án Hiến pháp (헌법재판소)",
                    "explanation": "베트남의 Hội đồng Hiến pháp은 자문기구이지만, 한국의 헌법재판소는 사법기관으로 법적 구속력 있는 결정을 내립니다."
                },
                {
                    "mistake": "권한을 '자문'으로 축소 번역",
                    "correction": "최종 심판권(quyền phán quyết cuối cùng)으로 강조",
                    "explanation": "한국 헌법재판소의 결정은 법적 구속력이 있으며 재심이 불가능한 최종 결정입니다."
                }
            ],
            "examples": [
                {
                    "ko": "헌법재판소가 해당 법률에 대해 위헌 결정을 내렸습니다.",
                    "vi": "Tòa án Hiến pháp đã ra quyết định vi hiến đối với luật đó.",
                    "situation": "formal"
                },
                {
                    "ko": "헌법재판소 재판관 9명 중 6명이 찬성했습니다.",
                    "vi": "6 trong số 9 thẩm phán Tòa án Hiến pháp đã tán thành.",
                    "situation": "formal"
                },
                {
                    "ko": "이 사건은 헌법재판소의 관할입니다.",
                    "vi": "Vụ việc này thuộc thẩm quyền của Tòa án Hiến pháp.",
                    "situation": "onsite"
                }
            ],
            "relatedTerms": ["위헌심사", "헌법소원", "위헌법률심판", "탄핵심판"]
        },
        {
            "slug": "xem-xet-tinh-hop-hien",
            "korean": "위헌심사",
            "vietnamese": "Xem xét tính hợp hiến",
            "hanja": "違憲審査",
            "hanjaReading": "違(어긋날 위) + 憲(법 헌) + 審(살필 심) + 査(조사할 사)",
            "pronunciation": "위헌심사",
            "meaningKo": "위헌심사는 법률, 명령, 규칙 등이 헌법에 위반되는지를 심사하는 절차입니다. 통역 시 주의할 점은 한국에서는 헌법재판소가 전담하는 반면, 베트남에서는 국회가 최종 결정권을 가진다는 차이입니다. 한국의 위헌심사는 '구체적 규범통제'와 '추상적 규범통제'로 나뉘며, 법원이 재판 중 위헌 의심이 들 때 헌법재판소에 제청할 수 있습니다. 베트남에서는 국회 상임위원회가 이 역할을 하므로, '사법적 심사'보다는 '입법적 통제'에 가깝습니다.",
            "meaningVi": "Xem xét tính hợp hiến là quá trình kiểm tra xem luật pháp, sắc lệnh, quy định có vi phạm Hiến pháp hay không. Ở Hàn Quốc, Tòa án Hiến pháp có quyền này, còn ở Việt Nam do Quốc hội quyết định.",
            "context": "헌법재판, 위헌법률심판, 사법심사",
            "culturalNote": "한국은 미국식 사법심사제도를 채택하여 헌법재판소가 법률의 위헌 여부를 독립적으로 판단합니다. 위헌 결정이 나면 해당 법률은 즉시 효력을 상실합니다. 반면 베트남은 국회 중심주의로 국회가 최고 권력기관이며, 법률의 위헌 여부도 국회가 최종 결정합니다. 통역 시 한국의 '사법 우위' 원칙을 명확히 전달해야 합니다.",
            "commonMistakes": [
                {
                    "mistake": "Kiểm tra hiến pháp (헌법 검사)로 번역",
                    "correction": "Xem xét tính hợp hiến (위헌심사)",
                    "explanation": "Kiểm tra는 단순 확인의 의미가 강하지만, Xem xét tính hợp hiến은 법적 판단과 결정을 포함하는 공식 용어입니다."
                },
                {
                    "mistake": "법원이 직접 위헌 결정을 내린다고 설명",
                    "correction": "법원은 위헌 제청만 하고 헌법재판소가 최종 결정",
                    "explanation": "한국에서는 법원이 위헌 의심이 들 때 헌법재판소에 제청하며, 최종 결정은 헌법재판소가 내립니다."
                },
                {
                    "mistake": "베트남도 같은 제도라고 가정",
                    "correction": "베트남은 국회 중심의 위헌심사 제도",
                    "explanation": "베트남에서는 사법부가 아닌 입법부(국회)가 위헌 여부를 최종 결정하는 구조적 차이가 있습니다."
                }
            ],
            "examples": [
                {
                    "ko": "법원은 이 법률에 대해 위헌심사를 제청했습니다.",
                    "vi": "Tòa án đã đề nghị xem xét tính hợp hiến của luật này.",
                    "situation": "formal"
                },
                {
                    "ko": "위헌심사 결과 해당 조항이 위헌으로 판단되었습니다.",
                    "vi": "Kết quả xem xét tính hợp hiến cho thấy điều khoản đó vi hiến.",
                    "situation": "formal"
                },
                {
                    "ko": "이 사안은 위헌심사 대상입니다.",
                    "vi": "Vấn đề này là đối tượng xem xét tính hợp hiến.",
                    "situation": "onsite"
                }
            ],
            "relatedTerms": ["헌법재판소", "위헌법률심판", "구체적 규범통제", "추상적 규범통제"]
        },
        {
            "slug": "vi-hien",
            "korean": "위헌",
            "vietnamese": "Vi hiến",
            "hanja": "違憲",
            "hanjaReading": "違(어긋날 위) + 憲(법 헌)",
            "pronunciation": "위헌",
            "meaningKo": "위헌은 법률, 명령, 처분 등이 헌법에 위배되는 것을 의미합니다. 통역 시 주의할 점은 '위헌'과 '위법'을 명확히 구분해야 한다는 것입니다. 위헌은 헌법 위반이고, 위법은 일반 법률 위반입니다. 한국에서 위헌 결정이 나면 해당 법률은 즉시 효력을 잃으며, 이미 그 법률로 처벌받은 사람도 재심을 청구할 수 있습니다. 베트남에서는 국회가 법률을 폐지하는 절차를 거쳐야 하므로, 효력 상실 시점과 구제 방법에 차이가 있습니다.",
            "meaningVi": "Vi hiến là tình trạng luật pháp, sắc lệnh, quyết định vi phạm Hiến pháp. Khi một luật bị tuyên bố vi hiến ở Hàn Quốc, luật đó mất hiệu lực ngay lập tức và có thể xét xử lại các vụ việc liên quan.",
            "context": "헌법재판, 위헌법률심판, 법률 효력",
            "culturalNote": "한국에서 위헌 결정의 효력은 절대적이며 소급 적용됩니다. 예를 들어 형벌 규정이 위헌으로 결정되면 과거에 그 법으로 처벌받은 사람도 재심을 청구할 수 있습니다. 베트남에서는 국회가 법률을 개정하거나 폐지하는 절차를 거쳐야 하므로, 위헌 판단의 실질적 효과가 다릅니다. 통역 시 위헌 결정의 '즉시 효력' 개념을 명확히 전달해야 합니다.",
            "commonMistakes": [
                {
                    "mistake": "Vi phạm pháp luật (위법)로 번역",
                    "correction": "Vi hiến (위헌)",
                    "explanation": "Vi phạm pháp luật은 일반 법률 위반이고, Vi hiến은 헌법 위반으로 훨씬 심각한 문제입니다."
                },
                {
                    "mistake": "위헌 결정 후에도 법률이 계속 유효하다고 설명",
                    "correction": "위헌 결정 즉시 해당 법률은 효력 상실",
                    "explanation": "한국에서 헌법재판소의 위헌 결정은 즉시 효력을 발생하며, 해당 법률은 더 이상 적용되지 않습니다."
                },
                {
                    "mistake": "Không hợp pháp (불법)으로 번역",
                    "correction": "Vi hiến (위헌)",
                    "explanation": "Không hợp pháp은 일반적 불법을 의미하지만, Vi hiến은 헌법 위반이라는 특정한 법적 개념입니다."
                }
            ],
            "examples": [
                {
                    "ko": "헌법재판소는 이 법률이 위헌이라고 결정했습니다.",
                    "vi": "Tòa án Hiến pháp đã quyết định luật này vi hiến.",
                    "situation": "formal"
                },
                {
                    "ko": "위헌 결정으로 인해 관련 규정이 모두 무효가 되었습니다.",
                    "vi": "Do quyết định vi hiến, tất cả các quy định liên quan đã vô hiệu.",
                    "situation": "formal"
                },
                {
                    "ko": "이 조항은 위헌 소지가 있습니다.",
                    "vi": "Điều khoản này có khả năng vi hiến.",
                    "situation": "onsite"
                }
            ],
            "relatedTerms": ["위헌심사", "합헌", "위헌법률심판", "헌법불합치"]
        },
        {
            "slug": "hop-hien",
            "korean": "합헌",
            "vietnamese": "Hợp hiến",
            "hanja": "合憲",
            "hanjaReading": "合(합할 합) + 憲(법 헌)",
            "pronunciation": "합헌",
            "meaningKo": "합헌은 법률이나 처분이 헌법에 합치한다는 헌법재판소의 결정을 의미합니다. 통역 시 주의할 점은 합헌 결정이 나면 같은 법률에 대해 다시 위헌심사를 청구할 수 없다는 점입니다(일사부재리 원칙). 다만 사회 상황이 크게 변화하여 '사정변경'이 인정되면 재심사가 가능합니다. 베트남에서는 국회가 법률의 최종 해석권을 가지므로, 한국의 합헌 결정과 같은 절대적 효력이 없습니다. 통역 시 합헌 결정의 '법적 안정성' 효과를 강조해야 합니다.",
            "meaningVi": "Hợp hiến là quyết định của Tòa án Hiến pháp cho rằng luật pháp hoặc quyết định phù hợp với Hiến pháp. Quyết định này có hiệu lực pháp lý ràng buộc và không thể khiếu nại lại về cùng nội dung.",
            "context": "헌법재판, 위헌심사, 법률 효력",
            "culturalNote": "한국에서 합헌 결정은 해당 법률의 헌법적 정당성을 확인하는 최종 판단으로, 국회와 정부에 법적 안정성을 제공합니다. 합헌 결정이 나면 같은 이유로 다시 위헌심사를 청구할 수 없습니다. 베트남에서는 국회가 언제든 법률을 개정할 수 있으므로, 합헌 판단의 지속성이 상대적으로 약합니다. 통역 시 합헌 결정의 '종국성'을 명확히 전달해야 합니다.",
            "commonMistakes": [
                {
                    "mistake": "Hợp pháp (합법)로 번역",
                    "correction": "Hợp hiến (합헌)",
                    "explanation": "Hợp pháp은 일반 법률에 맞다는 의미이고, Hợp hiến은 헌법에 맞다는 더 높은 수준의 개념입니다."
                },
                {
                    "mistake": "합헌 결정 후에도 재심사가 가능하다고 설명",
                    "correction": "원칙적으로 재심사 불가, 단 사정변경 시 예외",
                    "explanation": "합헌 결정은 종국적이며, 같은 이유로는 재심사를 청구할 수 없습니다."
                },
                {
                    "mistake": "Được phép (허용됨)로 번역",
                    "correction": "Hợp hiến (합헌)",
                    "explanation": "Được phép은 단순 허가의 의미이지만, Hợp hiến은 헌법재판소의 공식 법적 판단입니다."
                }
            ],
            "examples": [
                {
                    "ko": "헌법재판소는 이 법률이 합헌이라고 결정했습니다.",
                    "vi": "Tòa án Hiến pháp đã quyết định luật này hợp hiến.",
                    "situation": "formal"
                },
                {
                    "ko": "합헌 결정으로 법률의 효력이 유지됩니다.",
                    "vi": "Do quyết định hợp hiến, hiệu lực của luật được duy trì.",
                    "situation": "formal"
                },
                {
                    "ko": "이 조항은 합헌으로 판단되었습니다.",
                    "vi": "Điều khoản này đã được xác định là hợp hiến.",
                    "situation": "onsite"
                }
            ],
            "relatedTerms": ["위헌", "헌법불합치", "위헌심사", "일사부재리"]
        },
        {
            "slug": "khieu-nai-hien-phap",
            "korean": "헌법소원",
            "vietnamese": "Khiếu nại hiến pháp",
            "hanja": "憲法訴願",
            "hanjaReading": "憲(법 헌) + 法(법 법) + 訴(호소할 소) + 願(원할 원)",
            "pronunciation": "헌법소원",
            "meaningKo": "헌법소원은 공권력의 행사 또는 불행사로 인해 헌법상 보장된 기본권을 침해받은 경우 헌법재판소에 구제를 청구하는 제도입니다. 통역 시 주의할 점은 헌법소원에는 '권리구제형'과 '위헌심사형'이 있다는 것입니다. 권리구제형은 공권력 행위에 대한 직접 구제를 구하는 것이고, 위헌심사형은 법원의 위헌법률심판 제청 신청이 기각된 경우 제기합니다. 베트남에는 이러한 제도가 없으며, 국민이 직접 헌법 위반을 주장할 수 있는 법적 통로가 제한적입니다. 통역 시 헌법소원의 '국민의 직접 청구권' 성격을 강조해야 합니다.",
            "meaningVi": "Khiếu nại hiến pháp là chế độ cho phép công dân yêu cầu Tòa án Hiến pháp bảo vệ quyền cơ bản bị xâm phạm bởi hành vi hoặc không hành vi của cơ quan công quyền. Đây là quyền trực tiếp của người dân Hàn Quốc để bảo vệ quyền hiến định.",
            "context": "헌법재판, 기본권 구제, 공권력 통제",
            "culturalNote": "한국의 헌법소원 제도는 독일 모델을 따른 것으로, 국민이 직접 헌법재판소에 기본권 침해를 호소할 수 있는 강력한 권리 구제 수단입니다. 연간 수천 건의 헌법소원이 제기되며, 법률, 행정처분, 심지어 법원 판결도 대상이 될 수 있습니다. 베트남에는 유사한 제도가 없으며, 국민이 헌법 위반을 직접 주장할 수 있는 법적 통로가 매우 제한적입니다. 통역 시 헌법소원의 '직접성'과 '접근성'을 명확히 전달해야 합니다.",
            "commonMistakes": [
                {
                    "mistake": "Đơn kiện (소송)으로 번역",
                    "correction": "Khiếu nại hiến pháp (헌법소원)",
                    "explanation": "Đơn kiện은 일반 민사/형사 소송이고, Khiếu nại hiến pháp은 헌법재판소에 제기하는 특별한 헌법적 구제 절차입니다."
                },
                {
                    "mistake": "모든 불만을 헌법소원으로 제기할 수 있다고 설명",
                    "correction": "기본권 침해가 있어야 하고 다른 구제 수단이 없어야 함",
                    "explanation": "헌법소원은 보충성 원칙이 적용되어, 다른 법적 구제 수단을 모두 거친 후에만 제기할 수 있습니다."
                },
                {
                    "mistake": "Khiếu nại hành chính (행정소송)으로 혼동",
                    "correction": "Khiếu nại hiến pháp (헌법소원)",
                    "explanation": "행정소송은 일반 법원에 제기하지만, 헌법소원은 헌법재판소에만 제기하며 대상과 요건이 다릅니다."
                }
            ],
            "examples": [
                {
                    "ko": "시민들은 표현의 자유 침해를 이유로 헌법소원을 제기했습니다.",
                    "vi": "Công dân đã nộp khiếu nại hiến pháp với lý do xâm phạm quyền tự do ngôn luận.",
                    "situation": "formal"
                },
                {
                    "ko": "헌법소원은 침해 사실을 안 날로부터 90일 이내에 제기해야 합니다.",
                    "vi": "Khiếu nại hiến pháp phải được nộp trong vòng 90 ngày kể từ khi biết sự việc xâm phạm.",
                    "situation": "onsite"
                },
                {
                    "ko": "헌법재판소가 헌법소원을 인용하여 기본권 침해를 확인했습니다.",
                    "vi": "Tòa án Hiến pháp đã chấp nhận khiếu nại hiến pháp và xác nhận vi phạm quyền cơ bản.",
                    "situation": "formal"
                }
            ],
            "relatedTerms": ["기본권", "공권력", "권리구제", "보충성원칙"]
        },
        {
            "slug": "khong-phu-hop-hien-phap",
            "korean": "헌법불합치",
            "vietnamese": "Không phù hợp hiến pháp",
            "hanja": "憲法不合致",
            "hanjaReading": "憲(법 헌) + 法(법 법) + 不(아닐 불) + 合(합할 합) + 致(이를 치)",
            "pronunciation": "헌법불합치",
            "meaningKo": "헌법불합치는 법률이 헌법에 위반되지만, 즉시 효력을 상실시키면 법적 공백이나 혼란이 발생할 우려가 있어 일정 기간 효력을 유지하도록 하는 결정 형식입니다. 통역 시 주의할 점은 헌법불합치는 '위헌'과 '합헌'의 중간 형태가 아니라, 위헌이지만 개선 기회를 주는 결정이라는 점입니다. 국회에 법률 개정을 명령하며, 기한 내에 개정하지 않으면 해당 법률은 효력을 상실합니다. 베트남에는 이러한 단계적 무효화 개념이 없으며, 국회가 법률을 직접 개정하는 방식으로 처리합니다.",
            "meaningVi": "Không phù hợp hiến pháp là quyết định cho rằng luật vi phạm Hiến pháp nhưng vẫn duy trì hiệu lực tạm thời để tránh khoảng trống pháp lý, đồng thời yêu cầu Quốc hội sửa đổi trong thời hạn nhất định. Nếu không sửa đổi, luật sẽ mất hiệu lực.",
            "context": "헌법재판, 위헌심사, 법률 개정",
            "culturalNote": "한국의 헌법불합치 결정은 헌법재판소가 법적 안정성과 헌법 가치를 동시에 고려하는 유연한 제도입니다. 예를 들어 형벌 규정이 헌법불합치 결정을 받으면, 개정 시까지 기존 법률이 계속 적용되지만 국회는 반드시 개선해야 합니다. 이는 독일 헌법재판소의 영향을 받은 제도로, 베트남에는 유사 개념이 없습니다. 통역 시 헌법불합치의 '유예적 위헌' 성격을 명확히 전달해야 합니다.",
            "commonMistakes": [
                {
                    "mistake": "합헌도 위헌도 아닌 중립적 결정으로 설명",
                    "correction": "위헌이지만 즉시 효력 상실은 유예",
                    "explanation": "헌법불합치는 본질적으로 위헌 결정이며, 단지 법적 공백을 막기 위해 효력 상실 시점을 유예하는 것입니다."
                },
                {
                    "mistake": "Tạm thời hợp pháp (일시 합법)로 번역",
                    "correction": "Không phù hợp hiến pháp (헌법불합치)",
                    "explanation": "헌법불합치는 합법적 상태가 아니라, 위헌이지만 개선 기회를 주는 결정입니다."
                },
                {
                    "mistake": "국회가 개정하지 않아도 법률이 계속 유효하다고 설명",
                    "correction": "기한 내 미개정 시 법률 효력 상실",
                    "explanation": "헌법불합치 결정은 국회에 개정 의무를 부과하며, 기한 내 미개정 시 자동 실효됩니다."
                }
            ],
            "examples": [
                {
                    "ko": "헌법재판소는 이 법률에 대해 헌법불합치 결정을 내렸습니다.",
                    "vi": "Tòa án Hiến pháp đã ra quyết định không phù hợp hiến pháp đối với luật này.",
                    "situation": "formal"
                },
                {
                    "ko": "국회는 내년 말까지 법률을 개정해야 합니다.",
                    "vi": "Quốc hội phải sửa đổi luật trước cuối năm sau.",
                    "situation": "onsite"
                },
                {
                    "ko": "헌법불합치 결정 후에도 법률은 잠정적으로 계속 적용됩니다.",
                    "vi": "Sau quyết định không phù hợp hiến pháp, luật vẫn tạm thời tiếp tục áp dụng.",
                    "situation": "formal"
                }
            ],
            "relatedTerms": ["위헌", "합헌", "법적공백", "잠정적용"]
        },
        {
            "slug": "xet-xu-luan-toi",
            "korean": "탄핵심판",
            "vietnamese": "Xét xử luận tội",
            "hanja": "彈劾審判",
            "hanjaReading": "彈(탄핵할 탄) + 劾(다스릴 핵) + 審(살필 심) + 判(판단할 판)",
            "pronunciation": "탄핵심판",
            "meaningKo": "탄핵심판은 대통령, 국무총리, 국무위원, 법관 등 고위 공직자가 직무수행 중 헌법이나 법률을 위배한 경우 그 지위를 박탈하는 헌법재판소의 심판입니다. 통역 시 주의할 점은 탄핵소추는 국회가 하고, 탄핵심판은 헌법재판소가 한다는 점입니다. 국회는 소추 의결만 하며, 최종 파면 결정은 헌법재판소가 내립니다. 베트남에서는 국회가 탄핵 의결과 파면을 모두 담당하므로, 한국의 '이원적 구조'를 명확히 설명해야 합니다. 대통령 탄핵의 경우 재적 재판관 6명 이상의 찬성이 필요합니다.",
            "meaningVi": "Xét xử luận tội là phiên xét xử của Tòa án Hiến pháp để truất phế chức vụ của các quan chức cấp cao như Tổng thống, Thủ tướng, thẩm phán khi họ vi phạm Hiến pháp hoặc pháp luật trong khi làm nhiệm vụ. Quốc hội khởi tố, Tòa án Hiến pháp quyết định cuối cùng.",
            "context": "헌법재판, 공직자 문책, 권력 견제",
            "culturalNote": "한국의 탄핵 제도는 국회(입법부)와 헌법재판소(사법부)가 협력하여 대통령을 포함한 고위 공직자를 견제하는 민주적 장치입니다. 국회가 탄핵소추 의결을 하면 해당 공직자는 즉시 권한 행사가 정지되며, 헌법재판소의 최종 판단을 기다립니다. 베트남에서는 국회가 탄핵 결정까지 모두 담당하므로, 한국의 '견제와 균형' 원리를 통역 시 강조해야 합니다.",
            "commonMistakes": [
                {
                    "mistake": "Luận tội (탄핵소추)와 Xét xử luận tội (탄핵심판)를 같은 것으로 설명",
                    "correction": "Luận tội는 국회 소추, Xét xử luận tội는 헌법재판소 심판",
                    "explanation": "탄핵소추(국회)와 탄핵심판(헌법재판소)은 각각 다른 기관이 담당하는 별개 절차입니다."
                },
                {
                    "mistake": "국회가 탄핵 소추하면 자동으로 파면된다고 설명",
                    "correction": "헌법재판소가 최종 파면 여부 결정",
                    "explanation": "국회 소추는 심판 개시 요건일 뿐이며, 파면은 헌법재판소만 결정할 수 있습니다."
                },
                {
                    "mistake": "Phế truất (폐위)로 번역",
                    "correction": "Xét xử luận tội (탄핵심판)",
                    "explanation": "Phế truất은 군주제의 폐위를 의미하지만, Xét xử luận tội는 민주적 법적 절차입니다."
                }
            ],
            "examples": [
                {
                    "ko": "국회는 대통령에 대한 탄핵소추안을 가결했습니다.",
                    "vi": "Quốc hội đã thông qua nghị quyết luận tội Tổng thống.",
                    "situation": "formal"
                },
                {
                    "ko": "헌법재판소는 탄핵심판에서 파면 결정을 내렸습니다.",
                    "vi": "Tòa án Hiến pháp đã ra quyết định truất phế trong xét xử luận tội.",
                    "situation": "formal"
                },
                {
                    "ko": "탄핵소추 의결 후 대통령의 권한 행사가 정지됩니다.",
                    "vi": "Sau nghị quyết luận tội, quyền hành của Tổng thống bị đình chỉ.",
                    "situation": "onsite"
                }
            ],
            "relatedTerms": ["탄핵소추", "파면", "권한정지", "헌법재판소"]
        },
        {
            "slug": "quyen-co-ban",
            "korean": "기본권",
            "vietnamese": "Quyền cơ bản",
            "hanja": "基本權",
            "hanjaReading": "基(기초 기) + 本(근본 본) + 權(권리 권)",
            "pronunciation": "기본권",
            "meaningKo": "기본권은 헌법이 보장하는 인간의 기본적 권리로, 국가 권력도 침해할 수 없는 불가침의 권리입니다. 통역 시 주의할 점은 한국 헌법은 자유권, 평등권, 청구권, 참정권, 사회권 등을 기본권으로 규정하고 있으며, 헌법재판소를 통해 실질적으로 보호받을 수 있다는 점입니다. 베트남 헌법도 기본권을 규정하지만, 한국처럼 개인이 직접 헌법소원을 제기하는 제도가 없어 보호 수단이 제한적입니다. 통역 시 기본권의 '불가침성'과 '사법적 구제 가능성'을 강조해야 합니다.",
            "meaningVi": "Quyền cơ bản là các quyền căn bản của con người được bảo đảm bởi Hiến pháp, không thể bị xâm phạm ngay cả bởi quyền lực nhà nước. Ở Hàn Quốc, công dân có thể trực tiếp yêu cầu Tòa án Hiến pháp bảo vệ các quyền này.",
            "context": "헌법, 인권, 헌법재판",
            "culturalNote": "한국 헌법의 기본권 체계는 독일 기본법의 영향을 받아 매우 상세하고 포괄적입니다. 특히 헌법 제37조는 '국민의 모든 자유와 권리는 헌법에 열거되지 아니한 이유로 경시되지 아니한다'고 규정하여, 헌법에 명시되지 않은 권리도 보호합니다. 헌법재판소는 이를 근거로 성적 자기결정권, 일반적 인격권 등 새로운 기본권을 인정해왔습니다. 베트남도 헌법에 기본권을 규정하지만, 개인이 직접 헌법적 보호를 청구하는 제도가 없습니다.",
            "commonMistakes": [
                {
                    "mistake": "Quyền con người (인권)으로 번역",
                    "correction": "Quyền cơ bản (기본권)",
                    "explanation": "Quyền con người은 보편적 인권 개념이고, Quyền cơ bản은 헌법이 보장하는 구체적 권리입니다."
                },
                {
                    "mistake": "기본권은 법률로 제한할 수 없다고 설명",
                    "correction": "공공복리를 위해 법률로 제한 가능하나 본질적 내용은 침해 불가",
                    "explanation": "한국 헌법 제37조 제2항은 기본권 제한을 허용하지만, 본질적 내용을 침해할 수 없다고 규정합니다."
                },
                {
                    "mistake": "Quyền pháp lý (법적 권리)로 번역",
                    "correction": "Quyền cơ bản (기본권)",
                    "explanation": "Quyền pháp lý는 일반 법률상 권리이고, Quyền cơ bản은 헌법적 권리로 위상이 다릅니다."
                }
            ],
            "examples": [
                {
                    "ko": "표현의 자유는 헌법이 보장하는 기본권입니다.",
                    "vi": "Quyền tự do ngôn luận là quyền cơ bản được Hiến pháp bảo đảm.",
                    "situation": "formal"
                },
                {
                    "ko": "기본권 제한은 법률로만 가능하며 본질적 내용을 침해할 수 없습니다.",
                    "vi": "Hạn chế quyền cơ bản chỉ có thể bằng luật và không được xâm phạm nội dung bản chất.",
                    "situation": "formal"
                },
                {
                    "ko": "이 조치는 기본권을 과도하게 제한합니다.",
                    "vi": "Biện pháp này hạn chế quyền cơ bản quá mức.",
                    "situation": "onsite"
                }
            ],
            "relatedTerms": ["자유권", "평등권", "청구권", "사회권"]
        },
        {
            "slug": "tranh-chap-tham-quyen",
            "korean": "권한쟁의심판",
            "vietnamese": "Tranh chấp thẩm quyền",
            "hanja": "權限爭議審判",
            "hanjaReading": "權(권세 권) + 限(한정할 한) + 爭(다툴 쟁) + 議(의논할 의) + 審(살필 심) + 判(판단할 판)",
            "pronunciation": "권한쟁의심판",
            "meaningKo": "권한쟁의심판은 국가기관 상호간, 국가기관과 지방자치단체 간, 지방자치단체 상호간의 권한 다툼을 헌법재판소가 해결하는 절차입니다. 통역 시 주의할 점은 권한쟁의는 개인이 아닌 '기관 대 기관'의 다툼이며, 헌법이나 법률이 정한 권한의 존부 또는 범위에 관한 분쟁이라는 점입니다. 예를 들어 국회와 정부 간, 중앙정부와 지방자치단체 간 권한 다툼이 대상입니다. 베트남에는 이러한 제도가 없으며, 국회 상임위원회나 정부가 내부적으로 조정합니다. 통역 시 권한쟁의심판의 '사법적 해결' 성격을 강조해야 합니다.",
            "meaningVi": "Tranh chấp thẩm quyền là thủ tục do Tòa án Hiến pháp giải quyết tranh chấp về quyền hạn giữa các cơ quan nhà nước, giữa cơ quan nhà nước và chính quyền địa phương, hoặc giữa các chính quyền địa phương. Đây là tranh chấp 'cơ quan với cơ quan', không phải cá nhân.",
            "context": "헌법재판, 권력분립, 지방자치",
            "culturalNote": "한국의 권한쟁의심판 제도는 권력분립 원칙과 지방자치를 보장하기 위한 사법적 장치입니다. 예를 들어 국회가 정부의 전속 권한을 침해했다고 판단되면 정부가 헌법재판소에 권한쟁의심판을 청구할 수 있습니다. 실제로 국회와 정부, 중앙정부와 서울시 간 권한쟁의가 여러 차례 있었습니다. 베트남에는 이러한 사법적 해결 제도가 없으며, 주로 정치적 협상이나 상급기관의 조정으로 해결합니다. 통역 시 권한쟁의심판의 '독립적 사법 판단' 성격을 명확히 전달해야 합니다.",
            "commonMistakes": [
                {
                    "mistake": "개인도 권한쟁의심판을 청구할 수 있다고 설명",
                    "correction": "오직 국가기관이나 지방자치단체만 청구 가능",
                    "explanation": "권한쟁의심판은 기관 간 분쟁 해결 제도이며, 개인의 권리 구제는 헌법소원으로 해결합니다."
                },
                {
                    "mistake": "Tranh chấp hành chính (행정쟁송)으로 번역",
                    "correction": "Tranh chấp thẩm quyền (권한쟁의심판)",
                    "explanation": "행정쟁송은 개인 대 행정청의 분쟁이고, 권한쟁의심판은 기관 대 기관의 헌법적 분쟁입니다."
                },
                {
                    "mistake": "상급기관이 결정한다고 설명",
                    "correction": "헌법재판소가 독립적으로 판단",
                    "explanation": "권한쟁의심판은 상하 관계가 아닌, 독립된 헌법재판소의 사법적 판단입니다."
                }
            ],
            "examples": [
                {
                    "ko": "정부는 국회의 권한 침해를 이유로 권한쟁의심판을 청구했습니다.",
                    "vi": "Chính phủ đã yêu cầu xét xử tranh chấp thẩm quyền với lý do Quốc hội xâm phạm quyền hạn.",
                    "situation": "formal"
                },
                {
                    "ko": "서울시와 중앙정부 간 권한쟁의가 발생했습니다.",
                    "vi": "Đã phát sinh tranh chấp thẩm quyền giữa Thành phố Seoul và chính phủ trung ương.",
                    "situation": "onsite"
                },
                {
                    "ko": "헌법재판소는 권한쟁의심판에서 국회의 손을 들어주었습니다.",
                    "vi": "Tòa án Hiến pháp đã ủng hộ Quốc hội trong xét xử tranh chấp thẩm quyền.",
                    "situation": "formal"
                }
            ],
            "relatedTerms": ["권력분립", "지방자치", "헌법기관", "권한침해"]
        },
        {
            "slug": "giai-the-chinh-dang",
            "korean": "정당해산심판",
            "vietnamese": "Giải thể chính đảng",
            "hanja": "政黨解散審判",
            "hanjaReading": "政(정사 정) + 黨(무리 당) + 解(풀 해) + 散(흩을 산) + 審(살필 심) + 判(판단할 판)",
            "pronunciation": "정당해산심판",
            "meaningKo": "정당해산심판은 정당의 목적이나 활동이 민주적 기본질서에 위배될 때 헌법재판소가 그 정당을 강제로 해산시키는 제도입니다. 통역 시 주의할 점은 정당해산은 정부가 헌법재판소에 청구하며, 재적 재판관 6명 이상의 찬성이 필요한 매우 엄격한 절차라는 점입니다. 한국 헌정사에서 정당해산 결정은 2014년 통합진보당 사례가 유일합니다. 베트남은 일당제 국가로 정당해산 제도 자체가 존재하지 않습니다. 통역 시 정당해산심판의 '민주적 방어' 기능과 '예외적 성격'을 강조해야 합니다.",
            "meaningVi": "Giải thể chính đảng là chế độ cho phép Tòa án Hiến pháp buộc giải tán một chính đảng khi mục đích hoặc hoạt động của đảng đó vi phạm trật tự dân chủ cơ bản. Chính phủ yêu cầu và cần ít nhất 6/9 thẩm phán đồng ý. Đây là thủ tục rất nghiêm ngặt và hiếm khi xảy ra.",
            "context": "헌법재판, 정당제도, 민주주의 수호",
            "culturalNote": "한국의 정당해산심판 제도는 '방어적 민주주의' 개념에 기반하며, 독일 기본법의 영향을 받았습니다. 민주주의를 파괴하려는 정당으로부터 민주주의를 방어하는 최후 수단입니다. 2014년 통합진보당 해산 사례는 북한식 사회주의 추구와 폭력적 방법 동원을 이유로 결정되었습니다. 정당해산은 정치적 견해의 차이가 아닌 '민주적 기본질서 위배'가 명확해야 합니다. 베트nam은 일당제이므로 이러한 제도가 없으며, 통역 시 다당제 민주주의의 맥락을 충분히 설명해야 합니다.",
            "commonMistakes": [
                {
                    "mistake": "국회가 정당해산을 결정한다고 설명",
                    "correction": "정부가 청구하고 헌법재판소가 결정",
                    "explanation": "정당해산은 헌법재판소의 전속 권한이며, 국회나 정부가 임의로 해산시킬 수 없습니다."
                },
                {
                    "mistake": "Cấm hoạt động chính trị (정치활동 금지)로 번역",
                    "correction": "Giải thể chính đảng (정당해산심판)",
                    "explanation": "정당해산은 법적 실체 자체를 소멸시키는 것으로, 단순 활동 금지보다 훨씬 강력합니다."
                },
                {
                    "mistake": "정부가 마음대로 정당을 해산할 수 있다고 설명",
                    "correction": "헌법재판소의 엄격한 심사와 고도의 증명 필요",
                    "explanation": "정당해산은 민주주의의 예외적 조치로, 매우 엄격한 요건과 증거가 필요합니다."
                }
            ],
            "examples": [
                {
                    "ko": "정부는 해당 정당이 민주적 기본질서를 위배했다며 정당해산심판을 청구했습니다.",
                    "vi": "Chính phủ đã yêu cầu giải thể chính đảng với lý do đảng đó vi phạm trật tự dân chủ cơ bản.",
                    "situation": "formal"
                },
                {
                    "ko": "헌법재판소는 정당해산 결정을 내렸고 해당 정당은 즉시 해산되었습니다.",
                    "vi": "Tòa án Hiến pháp đã ra quyết định giải thể và chính đảng đó lập tức bị giải tán.",
                    "situation": "formal"
                },
                {
                    "ko": "정당해산심판은 민주주의를 지키는 최후의 수단입니다.",
                    "vi": "Giải thể chính đảng là phương án cuối cùng để bảo vệ dân chủ.",
                    "situation": "onsite"
                }
            ],
            "relatedTerms": ["민주적기본질서", "방어적민주주의", "정당제도", "위헌정당"]
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
    print(f"✅ Added {len(filtered)} terms (헌법재판/위헌심사). Total: {len(data)}")

if __name__ == '__main__':
    main()
