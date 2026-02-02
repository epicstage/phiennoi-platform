#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""파산/회생법 용어 추가 스크립트 (v7-b)"""

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
            "slug": "tuyen-bo-pha-san",
            "korean": "파산선고",
            "vietnamese": "Tuyên bố phá sản",
            "hanja": "破産宣告",
            "hanjaReading": "破(깨뜨릴 파) + 産(재산 산) + 宣(베풀 선) + 告(고할 고)",
            "pronunciation": "파산선고",
            "meaningKo": "법원이 채무자의 재산으로 채무를 완제할 수 없다고 인정하여 파산을 선고하는 재판. 통역 시 주의할 점은 베트남에서는 'phá sản'이 파산절차뿐 아니라 회생절차도 포함하는 개념으로 사용되므로, 한국의 파산선고는 'tuyên bố phá sản'으로 명확히 구분해야 합니다. 파산선고 후 채무자는 법적 제한을 받으며, 관재인이 재산을 관리하게 됩니다.",
            "meaningVi": "Quyết định của tòa án tuyên bố người mắc nợ không có khả năng thanh toán đầy đủ các khoản nợ bằng tài sản hiện có. Sau khi có tuyên bố phá sản, tài sản của con nợ sẽ được quản tài viên quản lý và thanh lý để trả nợ cho các chủ nợ theo thứ tự ưu tiên.",
            "context": "법원, 파산절차, 채무변제",
            "culturalNote": "한국의 파산선고는 베트남의 'tuyên bố phá sản'과 유사하나, 한국은 파산과 회생을 명확히 구분하는 반면 베트nam에서는 'phá sản'이 더 포괄적 의미로 사용됩니다. 한국의 파산선고는 청산형 절차인 반면, 회생절차는 기업 존속을 목적으로 합니다. 베트남 통역사는 이 차이를 명확히 인지하고 통역해야 합니다.",
            "commonMistakes": [
                {
                    "mistake": "파산선고를 'phá sản'으로만 번역",
                    "correction": "'tuyên bố phá sản' 또는 'tuyên bố phá sản thanh lý'로 명확히 표현",
                    "explanation": "'phá sản'만으로는 회생절차와 구분이 안 되므로 청산형 파산임을 명확히 해야 함"
                },
                {
                    "mistake": "파산선고와 회생절차 개시를 혼동",
                    "correction": "파산선고는 'tuyên bố phá sản', 회생절차 개시는 'mở thủ tục phục hồi doanh nghiệp'로 구분",
                    "explanation": "파산은 청산, 회생은 기업 존속이라는 근본적 차이가 있음"
                },
                {
                    "mistake": "파산선고 후 채무자를 'người phá sản'으로만 표현",
                    "correction": "'người bị tuyên bố phá sản' 또는 'con nợ phá sản'으로 표현",
                    "explanation": "법적 지위가 변경되었음을 명확히 해야 함"
                }
            ],
            "examples": [
                {
                    "ko": "법원은 채무자의 재산으로 채무를 변제할 수 없다고 인정하여 파산선고를 하였습니다.",
                    "vi": "Tòa án đã tuyên bố phá sản vì nhận định người mắc nợ không có khả năng thanh toán các khoản nợ bằng tài sản hiện có.",
                    "situation": "formal"
                },
                {
                    "ko": "파산선고가 나면 채무자는 관재인의 관리를 받게 됩니다.",
                    "vi": "Khi có tuyên bố phá sản, con nợ sẽ chịu sự quản lý của quản tài viên.",
                    "situation": "onsite"
                },
                {
                    "ko": "파산선고를 받으면 일정 기간 신용카드 발급이나 대출이 제한됩니다.",
                    "vi": "Sau khi bị tuyên bố phá sản, trong một thời gian nhất định sẽ bị hạn chế phát hành thẻ tín dụng hay vay vốn.",
                    "situation": "informal"
                }
            ],
            "relatedTerms": ["관재인", "회생절차", "채권자집회", "면책"]
        },
        {
            "slug": "thu-tuc-phuc-hoi",
            "korean": "회생절차",
            "vietnamese": "Thủ tục phục hồi",
            "hanja": "回生節次",
            "hanjaReading": "回(돌아올 회) + 生(날 생) + 節(마디 절) + 次(버금 차)",
            "pronunciation": "회생절차",
            "meaningKo": "재정적 어려움에 처한 채무자에 대하여 채권자·주주 등 이해관계인의 법률관계를 조정하여 채무자 또는 그 사업의 효율적인 회생을 도모하는 법적 절차. 통역 시 중요한 점은 베트남어로 'thủ tục phục hồi doanh nghiệp' 또는 'tái cơ cấu'로 표현되며, 파산(thanh lý)과 달리 기업의 존속과 재기를 목표로 한다는 점을 강조해야 합니다. 회생계획안 인가, 채권자 동의, M&A 등 복잡한 절차를 포함합니다.",
            "meaningVi": "Thủ tục pháp lý nhằm điều chỉnh quan hệ pháp luật giữa các bên liên quan như chủ nợ, cổ đông đối với con nợ gặp khó khăn tài chính, để hỗ trợ con nợ hoặc doanh nghiệp của họ phục hồi một cách hiệu quả. Khác với thanh lý phá sản, thủ tục phục hồi hướng tới việc duy trì hoạt động và tái thiết doanh nghiệp.",
            "context": "법원, 기업구조조정, 채무조정",
            "culturalNote": "한국의 회생절차는 베트남의 'thủ tục phục hồi doanh nghiệp'과 유사하나, 한국은 법원 주도의 엄격한 절차인 반면 베트남은 상대적으로 유연합니다. 한국은 회생절차 중에도 경영진이 업무를 계속할 수 있는 DIP(Debtor-In-Possession) 제도가 있으나, 베트남에서는 이러한 개념이 덜 발달했습니다. 통역 시 양국의 제도 차이를 명확히 설명해야 합니다.",
            "commonMistakes": [
                {
                    "mistake": "회생절차를 'phá sản'으로 번역",
                    "correction": "'thủ tục phục hồi doanh nghiệp' 또는 'tái cơ cấu doanh nghiệp'로 표현",
                    "explanation": "회생은 기업 존속이 목적이고 파산은 청산이 목적이므로 명확히 구분해야 함"
                },
                {
                    "mistake": "회생절차와 워크아웃을 혼동",
                    "correction": "회생절차는 'thủ tục phục hồi theo tòa án', 워크아웃은 'tái cơ cấu ngoài tòa án'으로 구분",
                    "explanation": "회생은 법원 절차, 워크아웃은 사적 채무조정이라는 차이가 있음"
                },
                {
                    "mistake": "회생계획안을 'kế hoạch phục hồi'로만 표현",
                    "correction": "'phương án phục hồi doanh nghiệp' 또는 'kế hoạch tái cơ cấu'로 표현",
                    "explanation": "법적 문서로서의 정확성을 위해 'phương án'을 사용하는 것이 적절함"
                }
            ],
            "examples": [
                {
                    "ko": "회사는 법원에 회생절차 개시를 신청하여 기업 정상화를 도모하고 있습니다.",
                    "vi": "Công ty đã nộp đơn yêu cầu tòa án mở thủ tục phục hồi doanh nghiệp để tái thiết hoạt động kinh doanh.",
                    "situation": "formal"
                },
                {
                    "ko": "회생절차에서는 채권자의 동의를 얻어 채무를 감면받을 수 있습니다.",
                    "vi": "Trong thủ tục phục hồi, có thể được giảm nợ sau khi có sự đồng ý của các chủ nợ.",
                    "situation": "onsite"
                },
                {
                    "ko": "회생절차 중에도 회사는 정상 영업을 계속할 수 있습니다.",
                    "vi": "Trong quá trình thủ tục phục hồi, công ty vẫn có thể tiếp tục hoạt động kinh doanh bình thường.",
                    "situation": "informal"
                }
            ],
            "relatedTerms": ["파산선고", "워크아웃", "관재인", "채권자집회"]
        },
        {
            "slug": "hoi-chu-no",
            "korean": "채권자집회",
            "vietnamese": "Hội chủ nợ",
            "hanja": "債權者集會",
            "hanjaReading": "債(빚 채) + 權(권세 권) + 者(놈 자) + 集(모을 집) + 會(모일 회)",
            "pronunciation": "채권자집회",
            "meaningKo": "파산절차나 회생절차에서 채권자들이 모여 중요 사항을 결정하는 회의. 통역 시 주의할 점은 채권자집회의 의결권은 채권액에 비례하여 행사되며, 회생계획안 가결을 위해서는 의결권 있는 채권자의 과반수 동의와 채권액 3/4 이상의 동의가 필요하다는 점을 정확히 전달해야 합니다. 베트남어로는 'hội nghị chủ nợ' 또는 'đại hội chủ nợ'로도 표현됩니다.",
            "meaningVi": "Cuộc họp của các chủ nợ trong thủ tục phá sản hoặc thủ tục phục hồi để quyết định các vấn đề quan trọng. Quyền biểu quyết được thực hiện theo tỷ lệ số tiền nợ, và để thông qua phương án phục hồi cần có sự đồng ý của đa số chủ nợ có quyền biểu quyết và trên 3/4 tổng số nợ.",
            "context": "파산절차, 회생절차, 채권자 의결",
            "culturalNote": "한국의 채권자집회는 베트남의 'hội chủ nợ'와 유사하나, 한국은 채권액 기준 의결이 더 엄격하게 적용됩니다. 한국에서는 회생계획안 가결을 위해 조별 의결(담보권자, 일반채권자 등)이 필요한 반면, 베트남은 상대적으로 단순합니다. 또한 한국에서는 소액채권자 보호를 위한 별도 규정이 있어, 통역 시 이러한 제도적 차이를 설명해야 합니다.",
            "commonMistakes": [
                {
                    "mistake": "채권자집회를 'cuộc họp chủ nợ'로만 번역",
                    "correction": "'hội chủ nợ' 또는 'đại hội chủ nợ'로 표현",
                    "explanation": "법적 절차상의 공식 회의체임을 명확히 해야 함"
                },
                {
                    "mistake": "의결권을 '투표권(quyền bỏ phiếu)'으로 표현",
                    "correction": "'quyền biểu quyết' 또는 'quyền quyết định'으로 표현",
                    "explanation": "법률 용어로서 'quyền biểu quyết'이 더 정확함"
                },
                {
                    "mistake": "채권자집회 결의를 'quyết định'으로만 표현",
                    "correction": "'nghị quyết của hội chủ nợ'로 표현",
                    "explanation": "집회의 공식 결정임을 명확히 해야 함"
                }
            ],
            "examples": [
                {
                    "ko": "채권자집회에서 회생계획안이 가결되어 법원에 인가를 신청할 예정입니다.",
                    "vi": "Phương án phục hồi đã được thông qua tại hội chủ nợ và sẽ nộp đơn xin tòa án phê chuẩn.",
                    "situation": "formal"
                },
                {
                    "ko": "채권자집회에서는 채권액에 비례하여 의결권을 행사합니다.",
                    "vi": "Tại hội chủ nợ, quyền biểu quyết được thực hiện theo tỷ lệ số tiền nợ.",
                    "situation": "onsite"
                },
                {
                    "ko": "다음 주 채권자집회에서 관재인 선임 건을 논의할 예정입니다.",
                    "vi": "Tuần sau tại hội chủ nợ sẽ thảo luận về việc bổ nhiệm quản tài viên.",
                    "situation": "informal"
                }
            ],
            "relatedTerms": ["관재인", "회생절차", "의결권", "회생계획안"]
        },
        {
            "slug": "quan-tai-vien",
            "korean": "관재인",
            "vietnamese": "Quản tài viên",
            "hanja": "管財人",
            "hanjaReading": "管(거느릴 관) + 財(재물 재) + 人(사람 인)",
            "pronunciation": "관재인",
            "meaningKo": "파산절차에서 법원이 선임하여 채무자의 재산을 관리하고 환가·배당하는 업무를 수행하는 자. 통역 시 주의할 점은 관재인은 법원의 감독을 받으며 채무자의 재산을 공정하게 관리·처분할 의무가 있다는 점을 명확히 해야 합니다. 베트남에서는 'quản tài viên' 또는 'người quản lý tài sản phá sản'으로 표현되며, 변호사나 회계사 등 전문가가 선임됩니다.",
            "meaningVi": "Người được tòa án chỉ định trong thủ tục phá sản để quản lý tài sản của con nợ, thanh lý và phân chia cho các chủ nợ. Quản tài viên chịu sự giám sát của tòa án và có nghĩa vụ quản lý, xử lý tài sản một cách công bằng. Thường là luật sư hoặc kế toán viên có chuyên môn.",
            "context": "파산절차, 재산관리, 채권자 보호",
            "culturalNote": "한국의 관재인 제도는 베트남의 'quản tài viên'과 유사하나, 한국은 파산관재인과 회생절차의 관리인을 구분하는 반면 베트남은 용어를 혼용하는 경우가 많습니다. 한국에서는 변호사, 회계사 등 전문자격자가 선임되며 법원의 엄격한 감독을 받습니다. 베트남에서도 유사하나 실무상 법원의 감독 강도가 다를 수 있어, 통역 시 이러한 차이를 설명해야 합니다.",
            "commonMistakes": [
                {
                    "mistake": "관재인을 'người quản lý'로만 번역",
                    "correction": "'quản tài viên' 또는 'người quản lý tài sản phá sản'으로 표현",
                    "explanation": "법적 지위와 역할을 명확히 하기 위해 공식 용어를 사용해야 함"
                },
                {
                    "mistake": "파산관재인과 회생절차 관리인을 구분 없이 번역",
                    "correction": "파산관재인은 'quản tài viên phá sản', 회생 관리인은 'quản lý viên phục hồi'로 구분",
                    "explanation": "절차와 역할이 다르므로 명확히 구분해야 함"
                },
                {
                    "mistake": "관재인의 업무를 '관리(quản lý)'로만 표현",
                    "correction": "'quản lý, thanh lý và phân phối tài sản'으로 구체적으로 표현",
                    "explanation": "관재인의 주요 업무인 환가와 배당을 명확히 해야 함"
                }
            ],
            "examples": [
                {
                    "ko": "법원은 파산선고와 동시에 관재인을 선임하였습니다.",
                    "vi": "Tòa án đã chỉ định quản tài viên đồng thời với việc tuyên bố phá sản.",
                    "situation": "formal"
                },
                {
                    "ko": "관재인은 채무자의 재산을 조사하고 환가하여 채권자에게 배당합니다.",
                    "vi": "Quản tài viên điều tra tài sản của con nợ, thanh lý và phân phối cho các chủ nợ.",
                    "situation": "onsite"
                },
                {
                    "ko": "관재인의 승인 없이는 재산을 처분할 수 없습니다.",
                    "vi": "Không thể xử lý tài sản nếu không có sự chấp thuận của quản tài viên.",
                    "situation": "informal"
                }
            ],
            "relatedTerms": ["파산선고", "채권자집회", "회생절차", "환가"]
        },
        {
            "slug": "mien-trai-nghiem",
            "korean": "면책",
            "vietnamese": "Miễn trách nhiệm",
            "hanja": "免責",
            "hanjaReading": "免(면할 면) + 責(꾸짖을 책)",
            "pronunciation": "면책",
            "meaningKo": "파산절차 종결 후 파산자가 파산채권에 대한 채무 전부를 면하는 것. 통역 시 중요한 점은 면책을 받으면 법적으로 채무 변제 의무가 소멸하지만, 조세채권, 고의·중과실 불법행위 채권 등 일부 채권은 면책되지 않는다는 점을 명확히 전달해야 합니다. 베트남어로는 'miễn trách nhiệm' 또는 'miễn nợ'로 표현되나, 법적 효과를 강조하려면 'miễn trách nhiệm trả nợ'가 더 정확합니다.",
            "meaningVi": "Sau khi kết thúc thủ tục phá sản, người phá sản được miễn toàn bộ nghĩa vụ trả nợ đối với các khoản nợ phá sản. Tuy nhiên, một số khoản nợ như nợ thuế, nợ do hành vi trái pháp luật cố ý hoặc sơ suất nghiêm trọng sẽ không được miễn.",
            "context": "파산절차, 채무 소멸, 개인파산",
            "culturalNote": "한국의 면책제도는 베트남의 'miễn trách nhiệm trả nợ'와 유사하나, 한국은 개인파산자의 경제적 재기를 적극 지원하는 반면 베트남은 상대적으로 엄격합니다. 한국에서는 성실한 파산자에게 면책이 원칙이나, 베트남에서는 면책 요건이 더 까다롭습니다. 또한 한국은 면책 후에도 신용정보에 기록이 남아 일정 기간 금융거래에 제약이 있으나, 법적 채무는 소멸한다는 점을 통역 시 명확히 해야 합니다.",
            "commonMistakes": [
                {
                    "mistake": "면책을 '免除(miễn trừ)'로 번역",
                    "correction": "'miễn trách nhiệm trả nợ' 또는 'miễn nợ phá sản'으로 표현",
                    "explanation": "법적 채무 소멸이라는 효과를 명확히 해야 함"
                },
                {
                    "mistake": "면책되지 않는 채권을 설명하지 않음",
                    "correction": "'một số khoản nợ không được miễn như nợ thuế, nợ do hành vi cố ý'로 명시",
                    "explanation": "면책의 예외를 명확히 전달해야 채권자가 오해하지 않음"
                },
                {
                    "mistake": "면책과 채무 감면을 혼동",
                    "correction": "면책은 'miễn trách nhiệm', 감면은 'giảm nợ'로 구분",
                    "explanation": "면책은 법적 소멸, 감면은 일부 줄이는 것으로 의미가 다름"
                }
            ],
            "examples": [
                {
                    "ko": "파산절차가 종결되어 면책 결정을 받았습니다.",
                    "vi": "Thủ tục phá sản đã kết thúc và nhận được quyết định miễn trách nhiệm trả nợ.",
                    "situation": "formal"
                },
                {
                    "ko": "면책을 받으면 파산채권에 대한 법적 책임이 사라집니다.",
                    "vi": "Khi được miễn trách nhiệm, nghĩa vụ pháp lý đối với các khoản nợ phá sản sẽ chấm dứt.",
                    "situation": "onsite"
                },
                {
                    "ko": "조세 채무는 면책 대상이 아니므로 여전히 납부해야 합니다.",
                    "vi": "Nợ thuế không thuộc đối tượng miễn trách nhiệm nên vẫn phải thanh toán.",
                    "situation": "informal"
                }
            ],
            "relatedTerms": ["파산선고", "개인회생", "채무 소멸", "비면책채권"]
        },
        {
            "slug": "quyen-phu-nhan",
            "korean": "부인권",
            "vietnamese": "Quyền phủ nhận",
            "hanja": "否認權",
            "hanjaReading": "否(아닐 부) + 認(알 인) + 權(권세 권)",
            "pronunciation": "부인권",
            "meaningKo": "파산절차나 회생절차에서 관재인이나 관리인이 채무자가 파산선고 전에 한 특정 법률행위의 효력을 부인하여 그 재산을 회복하는 권리. 통역 시 중요한 점은 부인권은 채권자의 공평한 만족을 위해 부당하게 재산이 유출되는 것을 막는 제도라는 점을 명확히 해야 합니다. 특히 편파행위(특정 채권자에게만 변제), 사해행위(재산 은닉) 등이 부인권 행사 대상이 됩니다.",
            "meaningVi": "Quyền của quản tài viên hoặc người quản lý trong thủ tục phá sản hoặc thủ tục phục hồi để phủ nhận hiệu lực của các hành vi pháp lý mà con nợ đã thực hiện trước khi tuyên bố phá sản và thu hồi tài sản. Chế độ này nhằm ngăn chặn việc tài sản bị chuyển đi bất hợp lý, đảm bảo sự công bằng cho các chủ nợ.",
            "context": "파산절차, 재산 회복, 채권자 보호",
            "culturalNote": "한국의 부인권 제도는 베트남의 'quyền phủ nhận giao dịch'과 유사하나, 한국은 부인 대상 기간과 요건이 더 구체적입니다. 한국에서는 파산선고 전 1년 이내 편파행위, 위기시기 이후 사해행위 등을 부인할 수 있으나, 베트남은 법률에 따라 다를 수 있습니다. 통역 시 부인권 행사 요건, 대상 기간, 법적 효과를 정확히 전달해야 분쟁을 예방할 수 있습니다.",
            "commonMistakes": [
                {
                    "mistake": "부인권을 '취소권(quyền hủy bỏ)'으로 번역",
                    "correction": "'quyền phủ nhận giao dịch' 또는 'quyền vô hiệu hóa giao dịch'로 표현",
                    "explanation": "파산법상 특별한 권리임을 명확히 해야 함"
                },
                {
                    "mistake": "편파행위를 'hành vi thiên vị'로 번역",
                    "correction": "'hành vi thiên vị chủ nợ' 또는 'thanh toán không bình đẳng cho chủ nợ'로 구체적으로 표현",
                    "explanation": "법적 의미를 정확히 전달해야 함"
                },
                {
                    "mistake": "부인 대상 기간을 명시하지 않음",
                    "correction": "'trước thời điểm tuyên bố phá sản trong vòng X tháng/năm'로 명시",
                    "explanation": "부인권 행사 가능 여부를 판단하려면 기간 정보가 필수"
                }
            ],
            "examples": [
                {
                    "ko": "관재인은 파산선고 전 특정 채권자에게만 변제한 행위에 대해 부인권을 행사하였습니다.",
                    "vi": "Quản tài viên đã thực hiện quyền phủ nhận đối với hành vi thanh toán chỉ cho một chủ nợ cụ thể trước khi tuyên bố phá sản.",
                    "situation": "formal"
                },
                {
                    "ko": "부인권이 인정되면 그 재산은 파산재단에 회복됩니다.",
                    "vi": "Nếu quyền phủ nhận được công nhận, tài sản đó sẽ được thu hồi vào khối tài sản phá sản.",
                    "situation": "onsite"
                },
                {
                    "ko": "파산 직전에 친인척에게 재산을 증여한 것은 부인권 대상이 될 수 있습니다.",
                    "vi": "Việc tặng cho tài sản cho người thân ngay trước khi phá sản có thể là đối tượng của quyền phủ nhận.",
                    "situation": "informal"
                }
            ],
            "relatedTerms": ["관재인", "편파행위", "사해행위", "파산재단"]
        },
        {
            "slug": "quyen-biet-che",
            "korean": "별제권",
            "vietnamese": "Quyền biệt chế",
            "hanja": "別除權",
            "hanjaReading": "別(다를 별) + 除(덜 제) + 權(권세 권)",
            "pronunciation": "별제권",
            "meaningKo": "파산절차에서 파산재단에 속하는 재산에 대하여 담보권을 가진 채권자가 파산절차에 의하지 않고 별도로 변제받을 수 있는 권리. 통역 시 주의할 점은 별제권자는 담보 목적물의 환가 대금에서 우선 변제받으며, 부족액에 대해서는 파산채권자로 참가할 수 있다는 점을 명확히 해야 합니다. 저당권, 질권, 유치권 등이 별제권으로 인정됩니다.",
            "meaningVi": "Quyền của chủ nợ có bảo đảm đối với tài sản thuộc khối tài sản phá sản được thanh toán riêng biệt không theo thủ tục phá sản. Chủ nợ có quyền biệt chế được ưu tiên thanh toán từ số tiền thanh lý tài sản bảo đảm, và nếu không đủ có thể tham gia với tư cách chủ nợ phá sản cho phần còn thiếu.",
            "context": "파산절차, 담보권, 우선변제",
            "culturalNote": "한국의 별제권 제도는 베트남의 'quyền ưu tiên thanh toán từ tài sản bảo đảm'와 유사하나, 한국은 별제권자의 지위가 더 강력합니다. 한국에서는 별제권자가 파산절차와 무관하게 담보권을 실행할 수 있으나, 베트남은 법원의 통제를 더 받는 경향이 있습니다. 통역 시 별제권의 범위, 실행 방법, 부족액 처리 등을 정확히 설명해야 채권자의 권리 행사에 문제가 없습니다.",
            "commonMistakes": [
                {
                    "mistake": "별제권을 '우선권(quyền ưu tiên)'으로만 번역",
                    "correction": "'quyền biệt chế' 또는 'quyền thanh toán riêng từ tài sản bảo đảm'로 표현",
                    "explanation": "파산법상 특별한 권리임을 명확히 해야 함"
                },
                {
                    "mistake": "별제권과 우선특권을 혼동",
                    "correction": "별제권은 'quyền biệt chế', 우선특권은 'đặc quyền ưu tiên'으로 구분",
                    "explanation": "담보권 유무, 법적 근거가 다르므로 명확히 구분해야 함"
                },
                {
                    "mistake": "부족액 처리를 설명하지 않음",
                    "correction": "'phần thiếu hụt có thể tham gia với tư cách chủ nợ phá sản'로 명시",
                    "explanation": "별제권자의 완전한 권리 행사를 위해 필요한 정보"
                }
            ],
            "examples": [
                {
                    "ko": "저당권자는 별제권을 행사하여 담보 부동산을 경매로 환가할 수 있습니다.",
                    "vi": "Chủ nợ có quyền thế chấp có thể thực hiện quyền biệt chế để thanh lý bất động sản bảo đảm qua đấu giá.",
                    "situation": "formal"
                },
                {
                    "ko": "별제권자는 파산절차와 무관하게 담보권을 실행할 수 있습니다.",
                    "vi": "Chủ nợ có quyền biệt chế có thể thực hiện quyền bảo đảm không phụ thuộc vào thủ tục phá sản.",
                    "situation": "onsite"
                },
                {
                    "ko": "담보 가치가 채권액에 미치지 못하면 나머지는 파산채권으로 신고해야 합니다.",
                    "vi": "Nếu giá trị bảo đảm không đủ để thanh toán toàn bộ nợ, phần còn lại phải được khai báo là khoản nợ phá sản.",
                    "situation": "informal"
                }
            ],
            "relatedTerms": ["담보권", "저당권", "우선특권", "파산채권"]
        },
        {
            "slug": "quyen-bu-tru",
            "korean": "상계권",
            "vietnamese": "Quyền bù trừ",
            "hanja": "相計權",
            "hanjaReading": "相(서로 상) + 計(셀 계) + 權(권세 권)",
            "pronunciation": "상계권",
            "meaningKo": "파산절차에서 파산채권자가 파산선고 당시 채무자에 대하여 채무를 부담하는 경우 파산절차에 의하지 않고 상계할 수 있는 권리. 통역 시 중요한 점은 상계는 채권과 채무가 서로 대등액에서 소멸하는 효과가 있으며, 이는 실질적으로 채권 전액을 변제받는 것과 같아 채권자에게 매우 유리하다는 점을 설명해야 합니다. 다만 부인권 대상이 되는 경우 상계가 제한될 수 있습니다.",
            "meaningVi": "Quyền của chủ nợ phá sản được bù trừ nợ một cách riêng biệt không theo thủ tục phá sản khi chủ nợ đồng thời là con nợ của người phá sản tại thời điểm tuyên bố phá sản. Bù trừ có hiệu lực làm nợ và quyền đòi nợ triệt tiêu lẫn nhau ở phần bằng nhau, tương đương với việc được thanh toán toàn bộ nợ.",
            "context": "파산절차, 채권·채무 상계, 채권자 보호",
            "culturalNote": "한국의 상계권 제도는 베트남의 'quyền bù trừ'와 유사하나, 한국은 파산절차에서 상계권 행사 요건이 더 명확합니다. 한국에서는 파산선고 당시 채권·채무가 모두 존재하면 상계할 수 있으나, 위기시기 이후 취득한 채권은 상계가 제한됩니다. 베트남도 유사한 제한이 있을 수 있으나, 실무상 적용이 다를 수 있어 통역 시 양국 법률의 차이를 확인하고 설명해야 합니다.",
            "commonMistakes": [
                {
                    "mistake": "상계를 '차감(trừ)'으로만 번역",
                    "correction": "'bù trừ' 또는 'khấu trừ nợ lẫn nhau'로 표현",
                    "explanation": "법적 효과인 채권·채무의 소멸을 명확히 해야 함"
                },
                {
                    "mistake": "상계권 행사 시기를 명시하지 않음",
                    "correction": "'tại thời điểm tuyên bố phá sản' 또는 '필요한 시기를 기준으로'를 명시",
                    "explanation": "상계 가능 여부 판단에 시기가 중요함"
                },
                {
                    "mistake": "상계 제한 사유를 설명하지 않음",
                    "correction": "'nợ phát sinh sau thời kỳ khủng hoảng không thể bù trừ' 등 제한 명시",
                    "explanation": "상계권 행사 가능 여부를 정확히 판단하려면 제한 사유 필요"
                }
            ],
            "examples": [
                {
                    "ko": "채권자는 파산채권 5천만 원과 채무 3천만 원을 상계하여 2천만 원만 파산채권으로 신고하였습니다.",
                    "vi": "Chủ nợ đã bù trừ khoản nợ phá sản 50 triệu won với khoản nợ 30 triệu won và chỉ khai báo 20 triệu won là khoản nợ phá sản.",
                    "situation": "formal"
                },
                {
                    "ko": "상계권을 행사하면 전액 변제받는 것과 같은 효과가 있습니다.",
                    "vi": "Việc thực hiện quyền bù trừ có hiệu lực tương đương với việc được thanh toán toàn bộ nợ.",
                    "situation": "onsite"
                },
                {
                    "ko": "파산선고 후 취득한 채권으로는 상계할 수 없습니다.",
                    "vi": "Không thể bù trừ bằng khoản nợ được phát sinh sau khi tuyên bố phá sản.",
                    "situation": "informal"
                }
            ],
            "relatedTerms": ["별제권", "파산채권", "부인권", "채권자 평등"]
        },
        {
            "slug": "phuc-hoi-ca-nhan",
            "korean": "개인회생",
            "vietnamese": "Phục hồi cá nhân",
            "hanja": "個人回生",
            "hanjaReading": "個(낱 개) + 人(사람 인) + 回(돌아올 회) + 生(날 생)",
            "pronunciation": "개인회생",
            "meaningKo": "경제적으로 파탄에 직면한 개인 채무자가 법원의 허가를 받은 변제계획에 따라 채무를 분할 변제하고 나머지 채무를 면책받는 제도. 통역 시 중요한 점은 개인회생은 일정한 소득이 있는 개인이 5년 내 분할 상환하고 나머지는 면책받는 제도로, 개인파산보다 신용 회복이 빠르고 재산을 일부 유지할 수 있다는 장점이 있다는 점을 설명해야 합니다.",
            "meaningVi": "Chế độ cho phép con nợ cá nhân gặp khó khăn tài chính được thanh toán nợ theo phương án trả góp được tòa án chấp thuận và được miễn nợ phần còn lại. Con nợ có thu nhập ổn định có thể trả góp trong vòng 5 năm và được miễn phần còn lại, giúp phục hồi tín dụng nhanh hơn so với phá sản cá nhân và có thể giữ lại một phần tài sản.",
            "context": "채무조정, 분할 상환, 신용 회복",
            "culturalNote": "한국의 개인회생 제도는 베트남에는 명확히 대응하는 제도가 없어 통역 시 설명이 필요합니다. 한국에서는 급여소득자, 영업소득자 등 일정 소득이 있는 개인이 신청할 수 있으며, 5년간 변제 후 나머지 채무를 면책받습니다. 베트남에서는 개인 파산 제도가 상대적으로 덜 발달했으므로, 통역 시 제도의 취지와 절차를 상세히 설명해야 이해를 도울 수 있습니다.",
            "commonMistakes": [
                {
                    "mistake": "개인회생을 'phá sản cá nhân'으로 번역",
                    "correction": "'thủ tục phục hồi cá nhân' 또는 'tái cơ cấu nợ cá nhân'으로 표현",
                    "explanation": "파산(청산)과 회생(재기)은 근본적으로 다른 제도임"
                },
                {
                    "mistake": "변제 기간을 명시하지 않음",
                    "correction": "'trả góp trong vòng 5 năm'으로 구체적으로 명시",
                    "explanation": "제도의 핵심 요소이므로 반드시 전달해야 함"
                },
                {
                    "mistake": "개인회생과 개인파산의 차이를 설명하지 않음",
                    "correction": "소득 유무, 변제 기간, 신용 회복 속도 등 차이를 명확히 설명",
                    "explanation": "채무자가 올바른 절차를 선택하려면 차이 이해가 필수"
                }
            ],
            "examples": [
                {
                    "ko": "일정한 소득이 있다면 개인파산보다 개인회생이 유리할 수 있습니다.",
                    "vi": "Nếu có thu nhập ổn định, thủ tục phục hồi cá nhân có thể có lợi hơn so với phá sản cá nhân.",
                    "situation": "formal"
                },
                {
                    "ko": "개인회생은 5년간 변제하고 나머지 채무를 면책받는 제도입니다.",
                    "vi": "Thủ tục phục hồi cá nhân là chế độ trả nợ trong 5 năm và được miễn phần nợ còn lại.",
                    "situation": "onsite"
                },
                {
                    "ko": "개인회생 신청 후에는 강제집행이 중지됩니다.",
                    "vi": "Sau khi nộp đơn xin thủ tục phục hồi cá nhân, việc cưỡng chế thi hành sẽ bị đình chỉ.",
                    "situation": "informal"
                }
            ],
            "relatedTerms": ["개인파산", "면책", "채무조정", "신용회복"]
        },
        {
            "slug": "workout",
            "korean": "워크아웃",
            "vietnamese": "Workout",
            "hanja": None,
            "hanjaReading": None,
            "pronunciation": "워크아웃",
            "meaningKo": "기업이 법원의 회생절차를 거치지 않고 채권자와의 협의를 통해 채무를 조정하는 사적 구조조정 절차. 통역 시 주의할 점은 워크아웃은 법정절차가 아니라 채권은행 주도의 자율적 구조조정이며, 법원의 관여 없이 채권단 협의로 진행된다는 점을 명확히 해야 합니다. 한국에서는 기업구조조정촉진법(기촉법)에 근거하며, 대상 기업의 정상화 가능성이 있어야 합니다.",
            "meaningVi": "Thủ tục tái cơ cấu tư nhân mà doanh nghiệp điều chỉnh nợ thông qua thỏa thuận với các chủ nợ mà không thông qua thủ tục phục hồi của tòa án. Đây không phải là thủ tục pháp lý mà là tái cơ cấu tự nguyện do nhóm ngân hàng chủ nợ chủ trì, tiến hành bằng thỏa thuận của đoàn chủ nợ mà không có sự can thiệp của tòa án.",
            "context": "기업구조조정, 채무 재조정, 채권은행",
            "culturalNote": "한국의 워크아웃 제도는 베트남에는 명확한 대응 제도가 없으며, 'tái cơ cấu nợ ngoài tòa án' 또는 'thương lượng nợ'로 설명해야 합니다. 한국에서는 주채권은행 주도로 기촉법에 따라 진행되며, 채권단의 75% 이상 동의가 필요합니다. 베트남에서는 채권자-채무자 간 협상이 더 비공식적으로 이루어지므로, 통역 시 한국의 워크아웃이 제도화된 절차임을 강조해야 합니다.",
            "commonMistakes": [
                {
                    "mistake": "워크아웃을 'phục hồi doanh nghiệp'로 번역",
                    "correction": "'tái cơ cấu nợ ngoài tòa án' 또는 'workout (giữ nguyên tiếng Anh)'로 표현",
                    "explanation": "법정 회생절차와 구분하기 위해 '법원 밖' 절차임을 명시해야 함"
                },
                {
                    "mistake": "워크아웃과 법정관리를 혼동",
                    "correction": "워크아웃은 '사적 절차', 회생절차는 '법원 절차'로 명확히 구분",
                    "explanation": "절차, 법적 효력, 채권자 보호 수준이 다름"
                },
                {
                    "mistake": "주채권은행의 역할을 설명하지 않음",
                    "correction": "'ngân hàng chủ nợ chính chủ trì' 역할을 명시",
                    "explanation": "워크아웃의 핵심 특징이므로 반드시 전달해야 함"
                }
            ],
            "examples": [
                {
                    "ko": "회사는 법원 회생절차 대신 채권단과 워크아웃 협상을 진행하고 있습니다.",
                    "vi": "Công ty đang tiến hành đàm phán workout với đoàn chủ nợ thay vì thủ tục phục hồi qua tòa án.",
                    "situation": "formal"
                },
                {
                    "ko": "워크아웃에 성공하면 법원 절차를 피하고 더 빠르게 정상화할 수 있습니다.",
                    "vi": "Nếu workout thành công, có thể tránh thủ tục tòa án và bình thường hóa nhanh hơn.",
                    "situation": "onsite"
                },
                {
                    "ko": "주채권은행의 동의 없이는 워크아웃을 진행할 수 없습니다.",
                    "vi": "Không thể tiến hành workout nếu không có sự đồng ý của ngân hàng chủ nợ chính.",
                    "situation": "informal"
                }
            ],
            "relatedTerms": ["회생절차", "채권단", "기업구조조정", "사적정리"]
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
