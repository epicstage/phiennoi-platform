#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""개인정보보호법 용어 추가 스크립트 (v7-i)"""

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
            "slug": "xu-ly-thong-tin-ca-nhan",
            "korean": "개인정보처리",
            "vietnamese": "Xử lý thông tin cá nhân",
            "hanja": "個人情報處理",
            "hanjaReading": "個(낱 개) 人(사람 인) 情(뜻 정) 報(알릴 보) 處(처리할 처) 理(다스릴 리)",
            "pronunciation": "개인정보처리",
            "meaningKo": "개인정보의 수집, 생성, 연계, 연동, 기록, 저장, 보유, 가공, 편집, 검색, 출력, 정정, 복구, 이용, 제공, 공개, 파기, 그 밖에 이와 유사한 행위를 말합니다. 통역 시 단순히 '처리'라고만 번역하지 말고 구체적으로 어떤 처리 행위(수집, 이용, 제공 등)인지 명확히 전달해야 합니다. 베트남어로는 포괄적인 'xử lý'와 구체적인 'thu thập(수집)', 'sử dụng(이용)', 'cung cấp(제공)' 등을 상황에 맞게 구분하여 사용하는 것이 중요합니다.",
            "meaningVi": "Xử lý thông tin cá nhân bao gồm việc thu thập, tạo lập, liên kết, ghi chép, lưu trữ, giữ gìn, gia công, biên tập, tra cứu, xuất ra, chỉnh sửa, phục hồi, sử dụng, cung cấp, công khai, hủy bỏ và các hành vi tương tự khác. Đây là khái niệm toàn diện về mọi hoạt động liên quan đến dữ liệu cá nhân.",
            "context": "개인정보보호법의 핵심 개념으로, 모든 개인정보 관련 활동을 포괄하는 용어입니다.",
            "culturalNote": "한국의 개인정보보호법은 EU GDPR과 유사하게 '처리'를 포괄적으로 정의하지만, 베트남 개인정보보호법(2023년 시행)은 상대적으로 최근 제정되어 구체적인 처리 행위를 열거하는 방식을 선호합니다. 통역 시 한국 법령의 포괄적 개념을 베트남 청중이 이해할 수 있도록 예시를 들어 설명하는 것이 효과적입니다.",
            "commonMistakes": [
                {
                    "mistake": "개인정보처리를 'xử lý dữ liệu'로만 번역",
                    "correction": "'xử lý thông tin cá nhân' 또는 'xử lý dữ liệu cá nhân'",
                    "explanation": "개인정보는 일반 데이터가 아닌 특별한 법적 보호를 받는 '개인의 정보'이므로 'thông tin cá nhân' 또는 'dữ liệu cá nhân'으로 명시해야 합니다."
                },
                {
                    "mistake": "처리를 단순히 'quản lý(관리)'로 번역",
                    "correction": "'xử lý'로 번역",
                    "explanation": "'quản lý'는 관리를 의미하며, 법적으로 정의된 '처리'의 포괄적 의미를 담지 못합니다."
                },
                {
                    "mistake": "수집과 처리를 동일한 개념으로 설명",
                    "correction": "수집(thu thập)은 처리(xử lý)의 한 유형임을 명확히",
                    "explanation": "처리는 수집을 포함한 상위 개념이므로, 통역 시 이 위계를 명확히 전달해야 합니다."
                }
            ],
            "examples": [
                {
                    "ko": "당사는 이용자의 개인정보를 수집, 이용, 제공하는 등 개인정보처리 활동을 수행합니다.",
                    "vi": "Công ty chúng tôi thực hiện các hoạt động xử lý thông tin cá nhân như thu thập, sử dụng, cung cấp thông tin cá nhân của người dùng.",
                    "situation": "formal"
                },
                {
                    "ko": "개인정보처리자는 개인정보를 처리하기 전에 정보주체의 동의를 받아야 합니다.",
                    "vi": "Người xử lý thông tin cá nhân phải được sự đồng ý của chủ thể thông tin trước khi xử lý thông tin cá nhân.",
                    "situation": "formal"
                },
                {
                    "ko": "이 시스템은 개인정보처리 전 과정을 자동으로 기록합니다.",
                    "vi": "Hệ thống này tự động ghi lại toàn bộ quá trình xử lý thông tin cá nhân.",
                    "situation": "onsite"
                }
            ],
            "relatedTerms": ["정보주체", "개인정보처리자", "동의", "개인정보보호책임자"]
        },
        {
            "slug": "chu-the-thong-tin",
            "korean": "정보주체",
            "vietnamese": "Chủ thể thông tin",
            "hanja": "情報主體",
            "hanjaReading": "情(뜻 정) 報(알릴 보) 主(주인 주) 體(몸 체)",
            "pronunciation": "정보주체",
            "meaningKo": "처리되는 정보에 의하여 알아볼 수 있는 사람으로서 그 정보의 주체가 되는 사람을 말합니다. 통역 시 '개인정보의 주인'이라는 개념을 명확히 전달해야 하며, 베트남어 'chủ thể'는 법적 권리의 주체를 의미하므로 정보주체가 가지는 열람권, 정정권, 삭제권 등의 권리와 연결하여 설명하면 이해가 쉽습니다. 단순히 '정보를 제공한 사람'이 아니라 '정보에 관한 권리를 가진 주체'임을 강조해야 합니다.",
            "meaningVi": "Chủ thể thông tin là người có thể được nhận diện qua thông tin đang được xử lý và là người chủ sở hữu thông tin đó. Chủ thể thông tin có các quyền như quyền được xem, sửa, xóa thông tin cá nhân của mình.",
            "context": "개인정보보호법에서 개인정보의 소유자이자 권리의 주체를 지칭하는 법률 용어입니다.",
            "culturalNote": "한국 법체계에서 '정보주체'는 GDPR의 'data subject'를 차용한 개념으로, 정보에 대한 적극적 권리 주체임을 강조합니다. 베트남에서는 전통적으로 개인정보를 '제공하는 사람(người cung cấp thông tin)'으로 표현했으나, 최근 개인정보보호법 제정으로 'chủ thể thông tin'이라는 권리 중심 용어가 도입되었습니다. 통역 시 이 용어가 단순한 정보 제공자가 아닌 법적 권리의 주체임을 설명하는 것이 중요합니다.",
            "commonMistakes": [
                {
                    "mistake": "'정보주체'를 'người cung cấp thông tin(정보 제공자)'로 번역",
                    "correction": "'chủ thể thông tin'으로 번역",
                    "explanation": "'정보 제공자'는 수동적 의미이지만, '정보주체'는 권리를 가진 능동적 법적 주체입니다."
                },
                {
                    "mistake": "'정보주체'를 'cá nhân(개인)'으로만 번역",
                    "correction": "'chủ thể thông tin'으로 정확히 번역",
                    "explanation": "법률 용어이므로 정확한 법적 개념을 전달해야 하며, 단순히 '개인'이라고 하면 법적 권리 주체의 의미가 약화됩니다."
                },
                {
                    "mistake": "'정보주체의 권리'를 설명 없이 번역",
                    "correction": "구체적 권리(열람, 정정, 삭제, 처리정지 등)를 예시로 제시",
                    "explanation": "정보주체 개념이 낯선 청중에게는 구체적 권리를 함께 설명해야 이해가 쉽습니다."
                }
            ],
            "examples": [
                {
                    "ko": "정보주체는 자신의 개인정보 처리에 대해 동의를 철회할 권리가 있습니다.",
                    "vi": "Chủ thể thông tin có quyền rút lại sự đồng ý về việc xử lý thông tin cá nhân của mình.",
                    "situation": "formal"
                },
                {
                    "ko": "정보주체의 동의 없이 개인정보를 제3자에게 제공할 수 없습니다.",
                    "vi": "Không được cung cấp thông tin cá nhân cho bên thứ ba mà không có sự đồng ý của chủ thể thông tin.",
                    "situation": "formal"
                },
                {
                    "ko": "정보주체가 열람을 요구하면 10일 이내에 응답해야 합니다.",
                    "vi": "Nếu chủ thể thông tin yêu cầu xem thông tin, phải trả lời trong vòng 10 ngày.",
                    "situation": "onsite"
                }
            ],
            "relatedTerms": ["개인정보처리자", "동의", "열람권", "정정권"]
        },
        {
            "slug": "rut-lai-dong-y",
            "korean": "동의철회",
            "vietnamese": "Rút lại đồng ý",
            "hanja": "同意撤回",
            "hanjaReading": "同(한가지 동) 意(뜻 의) 撤(걷을 철) 回(돌아올 회)",
            "pronunciation": "동의철회",
            "meaningKo": "정보주체가 개인정보의 수집, 이용, 제공 등에 대하여 한 번 동의한 후 그 동의를 취소하거나 철회하는 것을 말합니다. 통역 시 중요한 점은 동의철회가 단순한 마음의 변화가 아니라 법적으로 보장된 권리라는 점과, 철회 시점 이후의 개인정보 처리는 원칙적으로 중단되어야 한다는 점을 명확히 전달해야 합니다. 또한 동의철회와 회원탈퇴(계정 삭제)는 다른 개념임을 구분하는 것이 중요합니다.",
            "meaningVi": "Rút lại đồng ý là việc chủ thể thông tin hủy bỏ hoặc thu hồi sự đồng ý đã đưa ra trước đó về việc thu thập, sử dụng, cung cấp thông tin cá nhân. Đây là quyền được pháp luật bảo vệ và sau khi rút lại đồng ý, việc xử lý thông tin cá nhân về nguyên tắc phải dừng lại.",
            "context": "정보주체의 기본권으로, 언제든지 자유롭게 행사할 수 있는 권리입니다.",
            "culturalNote": "한국에서는 2011년 개인정보보호법 제정 이후 동의철회권이 명확히 인정되었으며, 동의를 받은 방법과 동일하거나 더 쉬운 방법으로 철회할 수 있도록 해야 합니다. 베트남에서는 2023년 개인정보보호 법령 시행 이후 이 개념이 도입되었으나, 실무에서는 아직 '회원탈퇴'와 '동의철회'를 혼동하는 경우가 많습니다. 통역 시 동의철회는 특정 개인정보 처리에 대한 동의만 취소하는 것이고, 회원탈퇴는 서비스 이용 계약 자체를 종료하는 것임을 구분하여 설명하면 좋습니다.",
            "commonMistakes": [
                {
                    "mistake": "'동의철회'를 'hủy đồng ý(동의 취소)'로만 번역",
                    "correction": "'rút lại đồng ý' 또는 'thu hồi đồng ý'로 번역",
                    "explanation": "'hủy'는 무효화의 의미가 강하지만, '동의철회'는 유효했던 동의를 이후에 철회하는 것이므로 'rút lại' 또는 'thu hồi'가 더 정확합니다."
                },
                {
                    "mistake": "동의철회와 회원탈퇴를 동일하게 설명",
                    "correction": "동의철회(rút lại đồng ý)는 특정 정보처리에 대한 동의 취소, 회원탈퇴(xóa tài khoản)는 계정 삭제로 구분",
                    "explanation": "두 개념은 법적으로 다른 의미와 절차를 가지므로 명확히 구분해야 합니다."
                },
                {
                    "mistake": "동의철회 시 '기존 처리된 정보는 유효'라고만 설명",
                    "correction": "철회 시점 이후 처리는 중단되어야 하며, 기존 정보는 별도 법적 근거가 있을 때만 보유 가능함을 명시",
                    "explanation": "동의철회의 법적 효과를 정확히 전달하지 않으면 오해가 생길 수 있습니다."
                }
            ],
            "examples": [
                {
                    "ko": "정보주체는 언제든지 개인정보 처리에 대한 동의를 철회할 수 있습니다.",
                    "vi": "Chủ thể thông tin có thể rút lại đồng ý về việc xử lý thông tin cá nhân bất cứ lúc nào.",
                    "situation": "formal"
                },
                {
                    "ko": "동의철회는 동의를 받은 방법보다 쉬운 방법으로 가능해야 합니다.",
                    "vi": "Việc rút lại đồng ý phải có thể thực hiện bằng cách dễ dàng hơn hoặc bằng cách đã nhận được sự đồng ý.",
                    "situation": "formal"
                },
                {
                    "ko": "고객이 마케팅 수신 동의를 철회했으니 더 이상 광고 메일을 보내면 안 됩니다.",
                    "vi": "Khách hàng đã rút lại đồng ý nhận thông tin marketing nên không được gửi email quảng cáo nữa.",
                    "situation": "onsite"
                }
            ],
            "relatedTerms": ["정보주체", "동의", "개인정보처리자", "처리정지권"]
        },
        {
            "slug": "ro-ri-thong-tin-ca-nhan",
            "korean": "개인정보유출",
            "vietnamese": "Rò rỉ thông tin cá nhân",
            "hanja": "個人情報流出",
            "hanjaReading": "個(낱 개) 人(사람 인) 情(뜻 정) 報(알릴 보) 流(흐를 류) 出(날 출)",
            "pronunciation": "개인정보유출",
            "meaningKo": "개인정보가 정당한 권한 없이 외부로 유출되거나, 분실, 도난, 유출, 위조, 변조 또는 훼손되는 것을 말합니다. 통역 시 단순한 실수로 인한 노출과 해킹 등 의도적 공격에 의한 유출을 구분하여 설명하고, 유출 발생 시 법적 신고 의무(개인정보보호위원회 및 정보주체에게 통지)가 있음을 함께 전달하는 것이 중요합니다. 베트남어로는 'rò rỉ(누출)', 'mất mát(분실)', 'đánh cắp(도난)' 등 유출 유형을 구체적으로 표현하면 이해가 쉽습니다.",
            "meaningVi": "Rò rỉ thông tin cá nhân là việc thông tin cá nhân bị lộ ra bên ngoài không có thẩm quyền hợp pháp, hoặc bị mất mát, đánh cắp, rò rỉ, làm giả, sửa đổi hoặc hủy hoại. Khi xảy ra rò rỉ, có nghĩa vụ pháp lý phải báo cáo cho cơ quan quản lý và thông báo cho chủ thể thông tin.",
            "context": "개인정보보호법상 가장 중요한 사고 유형으로, 발생 시 즉시 신고와 대응이 필요합니다.",
            "culturalNote": "한국에서는 2011년 이후 대형 개인정보유출 사고가 연이어 발생하면서 법적 처벌과 배상 기준이 강화되었습니다. 유출 시 개인정보보호위원회에 신고하고 정보주체에게도 통지해야 하며, 과태료와 민사 손해배상 책임이 발생할 수 있습니다. 베트남에서도 2023년 개인정보보호 법령 시행 이후 유사한 신고 의무가 도입되었으나, 실무상 신고 절차와 기준이 아직 정착 단계입니다. 통역 시 한국의 엄격한 신고 의무(원칙적으로 24시간 이내)를 설명할 때 베트남에서는 상대적으로 유연한 해석이 가능함을 언급하면 도움이 됩니다.",
            "commonMistakes": [
                {
                    "mistake": "'개인정보유출'을 'mất thông tin(정보 분실)'로만 번역",
                    "correction": "'rò rỉ thông tin cá nhân' 또는 'lộ lọt thông tin cá nhân'",
                    "explanation": "'유출'은 분실뿐 아니라 도난, 해킹, 부정 접근 등을 모두 포함하는 개념이므로 'rò rỉ(누출)' 또는 'lộ lọt(누설)'이 더 포괄적입니다."
                },
                {
                    "mistake": "유출 신고 의무를 '권고사항'으로 설명",
                    "correction": "법적 의무(nghĩa vụ pháp lý)임을 명확히",
                    "explanation": "한국법상 개인정보유출 신고는 의무사항이며 미신고 시 과태료가 부과됩니다."
                },
                {
                    "mistake": "유출과 침해를 동일한 개념으로 설명",
                    "correction": "침해(xâm phạm)는 유출을 포함한 더 넓은 개념으로 구분",
                    "explanation": "개인정보 침해는 유출, 오용, 남용 등을 모두 포함하는 상위 개념입니다."
                }
            ],
            "examples": [
                {
                    "ko": "해킹으로 인한 개인정보유출 사고가 발생하여 긴급 대응팀을 구성했습니다.",
                    "vi": "Đã xảy ra sự cố rò rỉ thông tin cá nhân do bị tấn công hack, nên đã thành lập đội ứng phó khẩn cấp.",
                    "situation": "formal"
                },
                {
                    "ko": "개인정보유출이 확인되면 24시간 이내에 개인정보보호위원회에 신고해야 합니다.",
                    "vi": "Khi xác nhận có rò rỉ thông tin cá nhân, phải báo cáo cho Ủy ban Bảo vệ Thông tin Cá nhân trong vòng 24 giờ.",
                    "situation": "formal"
                },
                {
                    "ko": "개인정보유출로 인해 피해를 입은 고객에게 보상을 제공할 예정입니다.",
                    "vi": "Sẽ cung cấp bồi thường cho khách hàng bị thiệt hại do rò rỉ thông tin cá nhân.",
                    "situation": "onsite"
                }
            ],
            "relatedTerms": ["개인정보침해", "개인정보보호책임자", "안전조치의무", "개인정보처리자"]
        },
        {
            "slug": "nguoi-chiu-trach-nhiem-bao-ve-thong-tin",
            "korean": "개인정보보호책임자",
            "vietnamese": "Người chịu trách nhiệm bảo vệ thông tin",
            "hanja": "個人情報保護責任者",
            "hanjaReading": "個(낱 개) 人(사람 인) 情(뜻 정) 報(알릴 보) 保(지킬 보) 護(도울 호) 責(꾸짖을 책) 任(맡길 임) 者(놈 자)",
            "pronunciation": "개인정보보호책임자",
            "meaningKo": "개인정보의 처리에 관한 업무를 총괄해서 책임지는 사람으로, 개인정보처리자의 지휘·감독을 받아 개인정보보호 업무를 수행하는 직책입니다. 통역 시 단순한 담당자가 아니라 법적 책임을 지는 임원급 이상의 책임자라는 점을 강조해야 합니다. 베트남어로는 'người chịu trách nhiệm(책임자)'로 번역되지만, 실무에서는 CPO(Chief Privacy Officer) 개념과 유사함을 설명하면 이해가 쉽습니다. 이 책임자는 개인정보 처리 방침 수립, 직원 교육, 민원 처리, 유출 사고 대응 등 전반적인 개인정보보호 업무를 총괄합니다.",
            "meaningVi": "Người chịu trách nhiệm bảo vệ thông tin cá nhân là người tổng quát và chịu trách nhiệm về công việc xử lý thông tin cá nhân, thực hiện nhiệm vụ bảo vệ thông tin cá nhân dưới sự chỉ đạo và giám sát của người xử lý thông tin cá nhân. Đây là vị trí cấp lãnh đạo có trách nhiệm pháp lý, tương tự như CPO (Chief Privacy Officer).",
            "context": "개인정보보호법에서 요구하는 필수 지정 직책으로, 일정 규모 이상 기업은 반드시 지정해야 합니다.",
            "culturalNote": "한국에서는 공공기관과 5명 이상 직원을 둔 개인정보처리자는 개인정보보호책임자를 의무적으로 지정해야 하며, 임원급 이상이 맡는 것이 원칙입니다. 책임자의 성명과 연락처는 개인정보 처리방침에 공개해야 하며, 유출 사고 시 법적 책임을 질 수 있습니다. 베트남에서는 2023년 이후 유사한 제도가 도입되었으나, 아직 중소기업에서는 실무 담당자가 겸직하는 경우가 많습니다. 통역 시 한국의 엄격한 지정 요건(임원급, 법적 책임)을 설명할 때 베트남 기업의 현실을 고려하여 단계적 도입 방안을 제시하면 좋습니다.",
            "commonMistakes": [
                {
                    "mistake": "'개인정보보호책임자'를 'nhân viên phụ trách(담당 직원)'로 번역",
                    "correction": "'người chịu trách nhiệm bảo vệ thông tin cá nhân' 또는 'trưởng phòng bảo vệ thông tin'",
                    "explanation": "책임자는 임원급 이상의 고위직이며 법적 책임을 지는 직책이므로, 단순 '담당 직원'으로 번역하면 직급과 책임 범위가 축소됩니다."
                },
                {
                    "mistake": "정보보호책임자(CISO)와 동일한 개념으로 설명",
                    "correction": "정보보호책임자는 기술적 보안, 개인정보보호책임자는 법적 준수 중심으로 구분",
                    "explanation": "두 직책은 업무 영역이 다르며, 큰 조직에서는 별도로 지정하는 경우가 많습니다."
                },
                {
                    "mistake": "책임자 지정을 '선택사항'으로 설명",
                    "correction": "법적 의무사항임을 명확히",
                    "explanation": "일정 규모 이상 기업은 반드시 지정해야 하며 미지정 시 과태료가 부과됩니다."
                }
            ],
            "examples": [
                {
                    "ko": "개인정보보호책임자는 매년 임직원 대상 개인정보보호 교육을 실시해야 합니다.",
                    "vi": "Người chịu trách nhiệm bảo vệ thông tin cá nhân phải thực hiện đào tạo bảo vệ thông tin cá nhân cho cán bộ nhân viên hàng năm.",
                    "situation": "formal"
                },
                {
                    "ko": "개인정보 관련 민원은 개인정보보호책임자에게 문의하시기 바랍니다.",
                    "vi": "Vui lòng liên hệ với Người chịu trách nhiệm bảo vệ thông tin cá nhân về khiếu nại liên quan đến thông tin cá nhân.",
                    "situation": "formal"
                },
                {
                    "ko": "새로 부임한 개인정보보호책임자가 전사 개인정보 처리 실태를 점검하고 있습니다.",
                    "vi": "Người chịu trách nhiệm bảo vệ thông tin mới nhận chức đang kiểm tra tình hình xử lý thông tin cá nhân toàn công ty.",
                    "situation": "onsite"
                }
            ],
            "relatedTerms": ["개인정보처리자", "개인정보보호법", "안전조치의무", "개인정보유출"]
        },
        {
            "slug": "danh-gia-tac-dong-thong-tin-ca-nhan",
            "korean": "개인정보영향평가",
            "vietnamese": "Đánh giá tác động thông tin cá nhân",
            "hanja": "個人情報影響評價",
            "hanjaReading": "個(낱 개) 人(사람 인) 情(뜻 정) 報(알릴 보) 影(그림자 영) 響(울릴 향) 評(평할 평) 價(값 가)",
            "pronunciation": "개인정보영향평가",
            "meaningKo": "개인정보를 활용하는 새로운 정보시스템을 도입하거나 기존 시스템을 중요하게 변경할 때, 해당 시스템이 개인정보 보호에 미치는 영향을 사전에 조사·예측·평가하고 적절한 보호조치를 마련하는 절차를 말합니다. 통역 시 단순한 보안 점검이 아니라 개인정보 라이프사이클 전체(수집-이용-제공-파기)에 대한 종합적 평가임을 강조하고, 평가 결과에 따라 시스템 설계를 변경해야 할 수도 있음을 전달해야 합니다. 베트남어로는 'đánh giá tác động(영향평가)'의 개념과 GDPR의 DPIA(Data Protection Impact Assessment)와 유사함을 설명하면 이해가 쉽습니다.",
            "meaningVi": "Đánh giá tác động thông tin cá nhân là quy trình điều tra, dự đoán, đánh giá trước về ảnh hưởng của hệ thống lên việc bảo vệ thông tin cá nhân khi triển khai hệ thống thông tin mới sử dụng thông tin cá nhân hoặc thay đổi quan trọng hệ thống hiện có, và chuẩn bị các biện pháp bảo vệ thích hợp. Đây là khái niệm tương tự DPIA trong GDPR.",
            "context": "공공기관과 대규모 개인정보를 처리하는 기관이 정보시스템 구축 시 의무적으로 수행해야 하는 사전 평가입니다.",
            "culturalNote": "한국에서는 2012년부터 개인정보영향평가가 제도화되었으며, 공공기관과 5만 명 이상 정보주체의 민감정보 또는 고유식별정보를 처리하는 기관은 의무적으로 평가를 받아야 합니다. 평가는 한국인터넷진흥원(KISA) 등 전문기관에 의뢰하며, 평가 결과는 공개됩니다. 베트남에서는 아직 영향평가 제도가 본격화되지 않았으나, EU와의 교역이 많은 기업을 중심으로 GDPR의 DPIA를 자발적으로 도입하는 사례가 늘고 있습니다. 통역 시 한국의 의무적 평가 제도와 베트남의 자율적 도입 단계의 차이를 설명하면 도움이 됩니다.",
            "commonMistakes": [
                {
                    "mistake": "'개인정보영향평가'를 'kiểm tra bảo mật(보안 점검)'로 번역",
                    "correction": "'đánh giá tác động thông tin cá nhân' 또는 'đánh giá tác động bảo vệ dữ liệu'",
                    "explanation": "영향평가는 기술적 보안 점검을 넘어 법적·관리적 측면을 포함한 종합 평가입니다."
                },
                {
                    "mistake": "평가를 '선택사항'으로 설명",
                    "correction": "일정 요건 충족 시 의무사항임을 명확히",
                    "explanation": "공공기관 등은 법적으로 평가를 받아야 하며 미이행 시 과태료가 부과됩니다."
                },
                {
                    "mistake": "영향평가와 취약점 진단을 동일하게 설명",
                    "correction": "영향평가는 사전 예방적 평가, 취약점 진단은 기술적 보안 점검으로 구분",
                    "explanation": "영향평가는 시스템 설계 단계의 법적 준수 평가이고, 취약점 진단은 운영 중인 시스템의 기술적 점검입니다."
                }
            ],
            "examples": [
                {
                    "ko": "새로운 회원관리 시스템 도입 전에 개인정보영향평가를 실시해야 합니다.",
                    "vi": "Phải thực hiện đánh giá tác động thông tin cá nhân trước khi triển khai hệ thống quản lý hội viên mới.",
                    "situation": "formal"
                },
                {
                    "ko": "개인정보영향평가 결과 일부 개인정보 수집 항목을 줄이기로 결정했습니다.",
                    "vi": "Theo kết quả đánh giá tác động thông tin cá nhân, đã quyết định giảm bớt một số mục thu thập thông tin cá nhân.",
                    "situation": "formal"
                },
                {
                    "ko": "한국인터넷진흥원에 개인정보영향평가를 의뢰했습니다.",
                    "vi": "Đã ủy thác đánh giá tác động thông tin cá nhân cho Cơ quan Xúc tiến Internet Hàn Quốc (KISA).",
                    "situation": "onsite"
                }
            ],
            "relatedTerms": ["개인정보보호법", "안전조치의무", "개인정보보호책임자", "정보시스템"]
        },
        {
            "slug": "xu-ly-gia-danh",
            "korean": "가명처리",
            "vietnamese": "Xử lý giả danh",
            "hanja": "假名處理",
            "hanjaReading": "假(거짓 가) 名(이름 명) 處(처리할 처) 理(다스릴 리)",
            "pronunciation": "가명처리",
            "meaningKo": "개인정보의 일부를 삭제하거나 대체하여 추가 정보 없이는 특정 개인을 알아볼 수 없도록 처리하는 것을 말합니다. 통역 시 중요한 점은 가명처리된 정보는 완전히 익명이 아니며, 원래의 개인정보로 복원할 수 있는 추가 정보가 별도로 관리된다는 점입니다. 익명처리와 달리 가명정보는 정보주체의 동의 없이 통계작성, 과학적 연구, 공익적 기록보존 등의 목적으로 활용할 수 있으나, 다른 정보와 결합하여 특정 개인을 식별할 가능성이 있으므로 엄격한 보호조치가 필요합니다.",
            "meaningVi": "Xử lý giả danh là việc xóa hoặc thay thế một phần thông tin cá nhân để không thể nhận diện cá nhân cụ thể nếu không có thông tin bổ sung. Khác với xử lý ẩn danh, thông tin giả danh vẫn có thể được phục hồi về thông tin cá nhân ban đầu thông qua thông tin bổ sung được quản lý riêng.",
            "context": "2020년 개인정보보호법 개정으로 도입된 개념으로, 데이터 활용과 개인정보 보호의 균형을 위한 제도입니다.",
            "culturalNote": "한국에서는 2020년 데이터3법 개정으로 가명정보 개념이 도입되어 빅데이터와 AI 산업 발전을 위한 법적 기반이 마련되었습니다. 가명정보는 통계, 연구, 공익 목적으로 정보주체 동의 없이 활용할 수 있지만, 특정 개인을 재식별하려는 시도는 금지됩니다. 베트남에서는 아직 가명처리에 대한 명확한 법적 개념이 정립되지 않았으며, 대부분 완전한 익명화 또는 동의 기반 개인정보 처리로 접근합니다. 통역 시 가명처리가 EU GDPR의 'pseudonymization'과 동일한 개념이며, 데이터 활용을 위한 중간 단계 보호조치임을 설명하면 이해가 쉽습니다.",
            "commonMistakes": [
                {
                    "mistake": "'가명처리'를 'ẩn danh(익명)'로 번역",
                    "correction": "'giả danh(pseudonymous)' 또는 'xử lý giả danh'로 번역",
                    "explanation": "가명과 익명은 법적으로 다른 개념이며, 가명은 재식별 가능성이 있지만 익명은 불가능합니다."
                },
                {
                    "mistake": "가명정보는 '개인정보가 아니다'라고 설명",
                    "correction": "가명정보는 여전히 개인정보이며, 특정 목적으로만 활용 가능하다고 설명",
                    "explanation": "가명정보는 개인정보보호법상 개인정보로 분류되어 일정한 보호조치가 필요합니다."
                },
                {
                    "mistake": "가명처리를 단순 암호화로 설명",
                    "correction": "암호화(mã hóa)는 복호화 키로 복원, 가명처리는 별도 관리되는 추가 정보로 복원 가능으로 구분",
                    "explanation": "암호화는 기술적 보안 조치이고, 가명처리는 데이터 활용을 위한 법적 개념입니다."
                }
            ],
            "examples": [
                {
                    "ko": "빅데이터 분석을 위해 고객 정보를 가명처리한 후 활용하고 있습니다.",
                    "vi": "Đang sử dụng thông tin khách hàng sau khi xử lý giả danh để phân tích dữ liệu lớn.",
                    "situation": "formal"
                },
                {
                    "ko": "가명정보는 통계 작성, 과학적 연구 등의 목적으로만 이용할 수 있습니다.",
                    "vi": "Thông tin giả danh chỉ có thể được sử dụng cho mục đích lập thống kê, nghiên cứu khoa học, v.v.",
                    "situation": "formal"
                },
                {
                    "ko": "개인정보를 가명처리할 때는 복원에 필요한 추가 정보를 별도로 안전하게 관리해야 합니다.",
                    "vi": "Khi xử lý giả danh thông tin cá nhân, phải quản lý riêng biệt và an toàn thông tin bổ sung cần thiết để phục hồi.",
                    "situation": "onsite"
                }
            ],
            "relatedTerms": ["익명처리", "개인정보", "비식별조치", "재식별"]
        },
        {
            "slug": "xu-ly-an-danh",
            "korean": "익명처리",
            "vietnamese": "Xử lý ẩn danh",
            "hanja": "匿名處理",
            "hanjaReading": "匿(숨을 익) 名(이름 명) 處(처리할 처) 理(다스릴 리)",
            "pronunciation": "익명처리",
            "meaningKo": "개인정보의 일부 또는 전부를 삭제하거나 대체함으로써 더 이상 특정 개인을 알아볼 수 없고 원래의 상태로 복원할 수 없도록 처리하는 것을 말합니다. 통역 시 가장 중요한 점은 익명처리된 정보는 개인정보가 아니므로 개인정보보호법의 적용을 받지 않으며, 어떤 목적으로든 자유롭게 활용할 수 있다는 점입니다. 하지만 진정한 익명화는 매우 어려우며, 다른 데이터와 결합하여 재식별될 가능성이 조금이라도 있다면 익명처리로 인정받기 어렵습니다. 베트남어로는 완전한 'ẩn danh(익명)' 개념을 강조해야 합니다.",
            "meaningVi": "Xử lý ẩn danh là việc xóa hoặc thay thế một phần hoặc toàn bộ thông tin cá nhân để không thể nhận diện cá nhân cụ thể và không thể phục hồi về trạng thái ban đầu. Thông tin đã được ẩn danh hoàn toàn không còn là thông tin cá nhân và không áp dụng Luật Bảo vệ Thông tin Cá nhân.",
            "context": "데이터 활용을 위해 개인정보보호 규제에서 자유로워지려면 완전한 익명처리가 필요합니다.",
            "culturalNote": "한국에서는 진정한 익명처리의 기준이 매우 엄격하며, 개인정보보호위원회와 전문기관이 '비식별 조치 가이드라인'을 통해 구체적 기준을 제시하고 있습니다. 단순히 이름과 주민등록번호를 삭제하는 것만으로는 익명처리로 인정받기 어려우며, 다른 공개 데이터와 결합하여 재식별될 가능성까지 고려해야 합니다. 베트남에서는 익명화 기준이 아직 명확하지 않으며, 실무에서는 개인정보 여부에 대한 판단이 사안별로 이루어집니다. 통역 시 한국의 엄격한 익명화 기준(재식별 가능성 거의 0)을 설명하고, 의심스러우면 가명처리로 접근하는 것이 안전하다고 조언하는 것이 좋습니다.",
            "commonMistakes": [
                {
                    "mistake": "이름만 삭제하면 익명처리라고 설명",
                    "correction": "다른 정보와 결합하여 재식별 가능성이 완전히 제거되어야 익명처리",
                    "explanation": "나이, 성별, 지역 등 간접식별자의 조합으로도 개인을 식별할 수 있으므로 단순 직접식별자 삭제만으로는 부족합니다."
                },
                {
                    "mistake": "익명처리와 가명처리를 구분하지 않고 설명",
                    "correction": "익명(ẩn danh)은 복원 불가능, 가명(giả danh)은 복원 가능으로 명확히 구분",
                    "explanation": "법적 효과가 완전히 다르므로(익명은 개인정보 아님, 가명은 개인정보) 반드시 구분해야 합니다."
                },
                {
                    "mistake": "통계 데이터는 자동으로 익명정보라고 설명",
                    "correction": "통계 데이터라도 소규모 집단이면 재식별 가능하므로 주의 필요",
                    "explanation": "예를 들어 '특정 회사의 40대 남성 임원'처럼 집단이 작으면 개인이 특정될 수 있습니다."
                }
            ],
            "examples": [
                {
                    "ko": "고객 데이터를 완전히 익명처리한 후 통계 분석에 활용했습니다.",
                    "vi": "Đã sử dụng dữ liệu khách hàng cho phân tích thống kê sau khi xử lý ẩn danh hoàn toàn.",
                    "situation": "formal"
                },
                {
                    "ko": "익명처리된 정보는 개인정보가 아니므로 정보주체의 동의 없이 활용할 수 있습니다.",
                    "vi": "Thông tin đã được ẩn danh không phải là thông tin cá nhân nên có thể sử dụng mà không cần sự đồng ý của chủ thể thông tin.",
                    "situation": "formal"
                },
                {
                    "ko": "이 데이터가 진정한 익명처리인지 전문기관의 검토를 받아야 합니다.",
                    "vi": "Cần được cơ quan chuyên môn xem xét xem dữ liệu này có phải là xử lý ẩn danh thực sự hay không.",
                    "situation": "onsite"
                }
            ],
            "relatedTerms": ["가명처리", "비식별조치", "재식별", "개인정보"]
        },
        {
            "slug": "chuyen-thong-tin-ra-nuoc-ngoai",
            "korean": "국외이전",
            "vietnamese": "Chuyển thông tin ra nước ngoài",
            "hanja": "國外移轉",
            "hanjaReading": "國(나라 국) 外(밖 외) 移(옮길 이) 轉(구를 전)",
            "pronunciation": "국외이전",
            "meaningKo": "개인정보를 국외의 제3자에게 제공하거나, 국외에 보관·관리하도록 하는 행위를 말합니다. 통역 시 중요한 점은 단순히 외국 서버에 저장하는 것뿐 아니라 클라우드 서비스 이용, 해외 지사와의 정보 공유, 외국 기업에 업무 위탁 등도 모두 국외이전에 해당한다는 점입니다. 국외이전 시에는 정보주체에게 이전되는 국가, 이전 일시 및 방법, 이전 항목, 이전받는 자의 정보보호 조치 등을 고지하고 별도 동의를 받아야 합니다. 베트남어로는 'chuyển ra nước ngoài(국외 이전)' 또는 'truyền tải quốc tế(국제 전송)'로 표현할 수 있습니다.",
            "meaningVi": "Chuyển thông tin ra nước ngoài là hành vi cung cấp thông tin cá nhân cho bên thứ ba ở nước ngoài hoặc lưu trữ, quản lý ở nước ngoài. Điều này bao gồm việc sử dụng dịch vụ đám mây, chia sẻ thông tin với chi nhánh nước ngoài, ủy thác công việc cho công ty nước ngoài, v.v. Khi chuyển ra nước ngoài, phải thông báo và nhận sự đồng ý riêng từ chủ thể thông tin.",
            "context": "글로벌 비즈니스 환경에서 빈번히 발생하지만 법적 규제가 엄격한 영역입니다.",
            "culturalNote": "한국에서는 개인정보의 국외이전에 대해 매우 엄격한 규제를 적용하며, 정보주체에게 이전국가, 이전 목적, 이전받는 자의 정보, 이전 항목, 보유기간, 안전조치 등을 상세히 고지하고 별도 동의를 받아야 합니다. 특히 EU GDPR의 영향으로 '적정성 평가'를 통과한 국가로의 이전이 선호됩니다. 베트남에서도 2023년 개인정보보호 법령 시행 이후 국외이전에 대한 규제가 강화되었으며, 특히 중국과 미국으로의 데이터 이전에 대해 민감하게 반응합니다. 통역 시 양국 모두 국외이전을 높은 위험으로 인식하며, AWS, Google Cloud 등 글로벌 클라우드 이용도 국외이전으로 간주될 수 있음을 설명하면 좋습니다.",
            "commonMistakes": [
                {
                    "mistake": "'국외이전'을 단순히 'xuất khẩu dữ liệu(데이터 수출)'로 번역",
                    "correction": "'chuyển thông tin cá nhân ra nước ngoài' 또는 'truyền tải dữ liệu cá nhân quốc tế'",
                    "explanation": "'수출'은 상업적 의미가 강하지만, '국외이전'은 법적 규제 대상 행위를 의미합니다."
                },
                {
                    "mistake": "클라우드 서비스 이용은 국외이전이 아니라고 설명",
                    "correction": "해외 서버에 저장되면 국외이전으로 간주될 수 있음을 명시",
                    "explanation": "AWS, Azure 등 해외 클라우드 이용도 데이터가 해외에 저장되면 국외이전에 해당합니다."
                },
                {
                    "mistake": "그룹사 간 정보 공유는 예외라고 설명",
                    "correction": "해외 자회사나 지사와의 공유도 국외이전으로 별도 동의 필요",
                    "explanation": "그룹사라도 국외에 있으면 국외이전 규제를 받습니다."
                }
            ],
            "examples": [
                {
                    "ko": "고객 데이터를 미국 본사 서버로 국외이전하려면 별도 동의를 받아야 합니다.",
                    "vi": "Để chuyển dữ liệu khách hàng sang máy chủ trụ sở chính ở Mỹ, phải nhận được sự đồng ý riêng.",
                    "situation": "formal"
                },
                {
                    "ko": "개인정보 국외이전 시 이전국가, 이전 항목, 안전조치 등을 고지해야 합니다.",
                    "vi": "Khi chuyển thông tin cá nhân ra nước ngoài, phải thông báo về quốc gia nhận chuyển, các mục chuyển, biện pháp an toàn, v.v.",
                    "situation": "formal"
                },
                {
                    "ko": "AWS 서울 리전을 사용하면 국외이전 이슈를 피할 수 있습니다.",
                    "vi": "Nếu sử dụng AWS khu vực Seoul có thể tránh được vấn đề chuyển thông tin ra nước ngoài.",
                    "situation": "onsite"
                }
            ],
            "relatedTerms": ["개인정보처리자", "제3자제공", "동의", "안전조치의무"]
        },
        {
            "slug": "quyen-bi-lang-quen",
            "korean": "잊힐권리",
            "vietnamese": "Quyền bị lãng quên",
            "hanja": "忘却權",
            "hanjaReading": "忘(잊을 망) 却(물리칠 각) 權(권세 권)",
            "pronunciation": "잊힐권리",
            "meaningKo": "정보주체가 자신에 관한 정보가 인터넷 등에 유통되는 것을 원하지 않을 때, 해당 정보의 삭제나 검색결과에서의 제외를 요구할 수 있는 권리를 말합니다. 통역 시 단순한 삭제권과 구분하여, 인터넷 검색엔진이나 포털사이트에 자신에 관한 정보의 검색결과 삭제를 요구하는 권리라는 점을 강조해야 합니다. EU GDPR의 'Right to be Forgotten'에서 유래한 개념이며, 한국에서는 명시적으로 법제화되지 않았지만 판례와 정보통신망법을 통해 일정 범위에서 인정됩니다. 베트남어로는 직역한 'quyền bị lãng quên' 외에 'quyền được xóa thông tin(정보 삭제권)'으로 보충 설명하면 이해가 쉽습니다.",
            "meaningVi": "Quyền bị lãng quên là quyền của chủ thể thông tin yêu cầu xóa hoặc loại bỏ khỏi kết quả tìm kiếm những thông tin về bản thân mà họ không muốn lưu hành trên internet. Đây là khái niệm xuất phát từ 'Right to be Forgotten' của GDPR của EU, cho phép yêu cầu công cụ tìm kiếm hoặc cổng thông tin xóa kết quả tìm kiếm về bản thân.",
            "context": "디지털 시대에 개인의 프라이버시를 보호하기 위한 새로운 권리 개념으로, 특히 과거 정보의 영구 보존 문제와 관련됩니다.",
            "culturalNote": "한국에서는 EU처럼 명시적인 '잊힐 권리' 법률은 없지만, 정보통신망법의 '개인정보 삭제·정정 요구권', '임시조치 요청권' 등을 통해 유사한 권리가 보호됩니다. 특히 포털사이트의 검색결과나 언론 기사에 대해 개인정보 삭제를 요구하는 사례가 증가하고 있으며, 법원은 개인의 프라이버시 보호와 표현의 자유·알권리 사이에서 균형을 잡는 판단을 내립니다. 베트남에서는 아직 잊힐 권리 개념이 법제화되지 않았으며, 인터넷 검열이 강한 환경 특성상 개인의 정보 삭제 요구보다는 정부의 콘텐츠 규제가 더 강력합니다. 통역 시 이 권리가 절대적이지 않으며 공익, 표현의 자유 등과 균형을 이루어야 한다는 점을 설명하는 것이 중요합니다.",
            "commonMistakes": [
                {
                    "mistake": "'잊힐 권리'를 단순 'quyền xóa(삭제권)'로만 번역",
                    "correction": "'quyền bị lãng quên' 또는 'quyền được xóa thông tin trên internet'",
                    "explanation": "잊힐 권리는 인터넷 검색결과 삭제 등 특수한 맥락의 권리이므로 개념을 정확히 전달해야 합니다."
                },
                {
                    "mistake": "잊힐 권리는 모든 정보를 무조건 삭제할 수 있는 권리라고 설명",
                    "correction": "공익, 표현의 자유, 알권리 등과 균형을 고려하여 제한적으로 인정됨을 명시",
                    "explanation": "절대적 권리가 아니며, 언론의 자유나 역사적 기록 보존 등과 충돌할 수 있습니다."
                },
                {
                    "mistake": "한국에 잊힐 권리 법이 있다고 설명",
                    "correction": "명시적 법률은 없지만 판례와 정보통신망법 등을 통해 유사한 권리가 보호됨",
                    "explanation": "EU와 달리 한국은 별도의 '잊힐 권리' 법제화가 이루어지지 않았습니다."
                }
            ],
            "examples": [
                {
                    "ko": "과거 범죄 기록이 계속 검색되어 잊힐 권리를 주장하며 삭제를 요구했습니다.",
                    "vi": "Đã yêu cầu xóa vì hồ sơ phạm tội trong quá khứ vẫn tiếp tục được tìm kiếm, với lý do quyền bị lãng quên.",
                    "situation": "formal"
                },
                {
                    "ko": "잊힐 권리와 언론의 자유 사이에서 법원이 균형잡힌 판단을 내렸습니다.",
                    "vi": "Tòa án đã đưa ra phán quyết cân bằng giữa quyền bị lãng quên và tự do ngôn luận.",
                    "situation": "formal"
                },
                {
                    "ko": "포털사이트에 과거 기사 검색결과 삭제를 요청하는 것도 잊힐 권리의 일종입니다.",
                    "vi": "Yêu cầu cổng thông tin xóa kết quả tìm kiếm bài báo cũ cũng là một dạng quyền bị lãng quên.",
                    "situation": "onsite"
                }
            ],
            "relatedTerms": ["정보주체", "삭제권", "개인정보자기결정권", "프라이버시"]
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
