#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Add remaining 30 medical terms to medical.json (Part 2)
Focus: Medical interpreting, Medical documents, Medical ethics
"""

import json
import os

# Use relative path from script location
file_path = os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', 'data', 'terms', 'medical.json')

new_terms_part2 = [
    {
        "slug": "thong-dich-dong-thoi",
        "korean": "동시통역",
        "vietnamese": "thông dịch đồng thời",
        "hanja": "同時通譯",
        "hanjaReading": "동(같을 동) + 시(때 시) + 통(통할 통) + 역(번역할 역)",
        "pronunciation": "dongsi-tongnyeok",
        "meaningKo": "화자가 말하는 동시에 실시간으로 통역하는 방식으로, 국제회의나 긴급 의료 상황에서 사용됩니다. 의료 현장에서는 주로 수술 중 의료진 간 소통, 원격 의료 상담, 다국적 컨퍼런스 등에서 활용됩니다. 통역 시 주의할 점은 동시통역은 순차통역보다 난이도가 높고 집중력이 요구되며, 의학 용어를 즉각 변환해야 하므로 사전 준비가 필수입니다. 일반 진료에서는 순차통역이 더 정확하고 안전하므로, 상황에 맞는 통역 방식을 선택하는 것이 중요합니다.",
        "meaningVi": "Phương thức thông dịch theo thời gian thực khi người nói đang phát biểu, được sử dụng trong hội nghị quốc tế hoặc tình huống y tế khẩn cấp. Trong y tế chủ yếu dùng cho giao tiếp giữa nhân viên y tế trong phẫu thuật, tư vấn y tế từ xa, hội nghị đa quốc gia.",
        "context": "의료 통역, 국제 진료, 원격 의료",
        "culturalNote": "한국의 대형 병원에서는 국제 진료센터에 동시통역 장비가 구비된 경우도 있지만, 일반 외래에서는 순차통역이 표준입니다. 베트남에서는 의료 동시통역이 거의 없어 환자들이 낯설어할 수 있습니다. 의료통역사는 자신의 역량을 고려하여 적절한 통역 방식을 제안해야 합니다.",
        "commonMistakes": [
            {
                "mistake": "동시통역과 순차통역을 구분하지 않고 사용",
                "correction": "동시통역은 'thông dịch đồng thời', 순차통역은 'thông dịch tuần tự' - 방식의 차이 명확히",
                "explanation": "두 방식의 난이도와 적용 상황이 다르므로 정확한 구분 필요"
            },
            {
                "mistake": "의료 현장에서 준비 없이 동시통역 시도",
                "correction": "사전에 의학 용어 학습과 시뮬레이션 훈련 필수",
                "explanation": "동시통역 실수는 환자 안전에 직결되므로 충분한 준비 없이는 시도하지 말아야"
            },
            {
                "mistake": "모든 상황에서 동시통역이 더 좋다고 설명",
                "correction": "일반 진료는 순차통역이 더 정확하고 안전 - 상황별로 적절한 방식 선택",
                "explanation": "의료 통역에서는 정확성이 속도보다 우선이므로 순차통역이 기본"
            }
        ],
        "examples": [
            {
                "ko": "국제 컨퍼런스에서는 동시통역 장비를 사용합니다.",
                "vi": "Trong hội nghị quốc tế, sử dụng thiết bị thông dịch đồng thời.",
                "situation": "formal"
            },
            {
                "ko": "수술 중에는 동시통역이 필요할 수 있습니다.",
                "vi": "Trong quá trình phẫu thuật có thể cần thông dịch đồng thời.",
                "situation": "onsite"
            },
            {
                "ko": "일반 진료는 순차통역이 더 안전해요.",
                "vi": "Khám bệnh thông thường, thông dịch tuần tự an toàn hơn.",
                "situation": "informal"
            }
        ],
        "relatedTerms": ["순차통역", "의료통역", "의료통역윤리"]
    },
    {
        "slug": "thong-dich-tuan-tu",
        "korean": "순차통역",
        "vietnamese": "thông dịch tuần tự",
        "hanja": "順次通譯",
        "hanjaReading": "순(순할 순) + 차(차례 차) + 통(통할 통) + 역(번역할 역)",
        "pronunciation": "suncha-tongnyeok",
        "meaningKo": "화자가 한 문장 또는 의미 단위로 말을 끊으면 통역사가 순차적으로 통역하는 방식으로, 의료 현장에서 가장 일반적으로 사용됩니다. 정확성과 완성도가 높아 진단, 치료 계획 설명, 동의서 작성 등 중요한 의료 정보 전달에 적합합니다. 통역 시 주의할 점은 의사와 환자 모두 통역사가 끼어들 수 있도록 적절한 간격을 두고 말해야 하며, 통역사는 메모를 활용하여 정확히 전달해야 합니다. 베트남어-한국어 의료통역에서는 순차통역이 표준 방식입니다.",
        "meaningVi": "Phương thức thông dịch khi người nói dừng lại sau mỗi câu hoặc đơn vị ý nghĩa để thông dịch viên chuyển tải tuần tự, là cách phổ biến nhất trong y tế. Có độ chính xác và hoàn thiện cao, phù hợp cho chẩn đoán, giải thích kế hoạch điều trị, ký giấy đồng ý, v.v.",
        "context": "의료 통역, 외래 진료, 환자 상담",
        "culturalNote": "한국 병원의 외래 진료에서는 순차통역이 기본이며, 의사들도 이 방식에 익숙합니다. 베트남에서는 비공식 통역이 많아 체계적인 순차통역 훈련을 받지 않은 경우가 많으므로, 전문 의료통역사는 메모 기법, 청킹(chunking), 정확한 용어 사용 등의 기술을 익혀야 합니다.",
        "commonMistakes": [
            {
                "mistake": "너무 긴 문장을 한 번에 통역하려다 내용 누락",
                "correction": "의사에게 문장을 짧게 끊어 말해달라고 요청하거나 메모 활용",
                "explanation": "정확성을 위해 적절한 길이로 청킹하는 것이 중요"
            },
            {
                "mistake": "환자의 질문을 요약하여 통역",
                "correction": "환자의 말을 가감 없이 그대로 통역",
                "explanation": "통역사의 주관적 판단으로 내용을 바꾸면 안 됨"
            },
            {
                "mistake": "의사의 전문 용어를 이해하지 못했는데 추측하여 통역",
                "correction": "모르는 용어는 즉시 확인하고 정확히 통역",
                "explanation": "의료통역에서 추측은 금물, 정확성이 최우선"
            }
        ],
        "examples": [
            {
                "ko": "순차통역으로 진행하겠습니다. 문장을 짧게 끊어 말씀해 주세요.",
                "vi": "Chúng tôi sẽ tiến hành thông dịch tuần tự. Vui lòng nói ngắn gọn từng câu.",
                "situation": "formal"
            },
            {
                "ko": "환자분이 말씀하시면 제가 통역하겠습니다.",
                "vi": "Khi bệnh nhân nói xong, tôi sẽ thông dịch.",
                "situation": "onsite"
            },
            {
                "ko": "순차통역이 시간은 걸리지만 더 정확해요.",
                "vi": "Thông dịch tuần tự mất thời gian nhưng chính xác hơn.",
                "situation": "informal"
            }
        ],
        "relatedTerms": ["동시통역", "의료통역", "메모테이킹"]
    },
    {
        "slug": "dao-duc-thong-dich-y-te",
        "korean": "의료통역윤리",
        "vietnamese": "đạo đức thông dịch y tế",
        "hanja": "醫療通譯倫理",
        "hanjaReading": "의(의원 의) + 료(고칠 료) + 통(통할 통) + 역(번역할 역) + 륜(인륜 륜) + 리(다스릴 리)",
        "pronunciation": "uiryo-tongnyeok-yulli",
        "meaningKo": "의료통역사가 지켜야 할 직업 윤리로, 정확성, 중립성, 비밀유지, 문화적 민감성, 전문성 유지 등이 포함됩니다. 의료통역사는 환자의 사생활을 보호하고, 어느 한쪽 편을 들지 않으며, 의료 정보를 정확히 전달해야 합니다. 통역 시 주의할 점은 개인적 의견을 개입시키거나, 환자를 대신하여 결정하거나, 의료 자문을 제공해서는 안 된다는 것입니다. 또한 통역 중 알게 된 환자의 개인 정보는 절대 외부에 누설하지 말아야 하며, 이는 법적 책임과도 연결됩니다.",
        "meaningVi": "Đạo đức nghề nghiệp mà thông dịch viên y tế phải tuân thủ, bao gồm tính chính xác, trung lập, bảo mật, nhạy cảm văn hóa, duy trì tính chuyên nghiệp. Thông dịch viên y tế phải bảo vệ quyền riêng tư của bệnh nhân, không thiên vị, truyền tải thông tin y tế chính xác.",
        "context": "의료 윤리, 통역 전문성, 환자 권리",
        "culturalNote": "한국은 의료통역사 윤리 강령이 체계화되어 있지만, 베트남에서는 비공식 통역이 많아 윤리 의식이 상대적으로 약할 수 있습니다. 특히 가족이나 친구가 통역할 경우 중립성과 비밀유지가 지켜지지 않는 경우가 많아, 전문 의료통역사의 윤리적 역할이 더욱 중요합니다.",
        "commonMistakes": [
            {
                "mistake": "환자에게 개인적 조언 제공",
                "correction": "통역사는 조언자가 아닌 전달자 - 의사의 말만 정확히 통역",
                "explanation": "통역사의 개인 의견은 의료 결정에 영향을 주어서는 안 됨"
            },
            {
                "mistake": "통역 중 알게 된 환자 정보를 다른 사람에게 이야기",
                "correction": "비밀유지 의무 - 어떤 경우에도 환자 정보 누설 금지",
                "explanation": "비밀유지 위반은 법적 책임과 직결되며 환자 신뢰를 무너뜨림"
            },
            {
                "mistake": "의사 편을 들며 환자를 설득",
                "correction": "중립 유지 - 양측의 말을 편견 없이 정확히 전달",
                "explanation": "통역사는 중재자가 아닌 전달자이므로 어느 한쪽 편을 들면 안 됨"
            }
        ],
        "examples": [
            {
                "ko": "의료통역윤리에 따라 환자분의 개인정보는 철저히 보호됩니다.",
                "vi": "Theo đạo đức thông dịch y tế, thông tin cá nhân của bệnh nhân được bảo vệ tuyệt đối.",
                "situation": "formal"
            },
            {
                "ko": "저는 중립적으로 통역하며, 어느 쪽 편도 들지 않습니다.",
                "vi": "Tôi thông dịch trung lập, không thiên vị bất kỳ bên nào.",
                "situation": "onsite"
            },
            {
                "ko": "통역사는 조언할 수 없어요. 의사 선생님께 직접 여쭤보세요.",
                "vi": "Thông dịch viên không thể tư vấn. Hãy hỏi bác sĩ trực tiếp.",
                "situation": "informal"
            }
        ],
        "relatedTerms": ["비밀유지의무", "의료통역", "환자권리"]
    },
    {
        "slug": "nghia-vu-bao-mat",
        "korean": "비밀유지의무",
        "vietnamese": "nghĩa vụ bảo mật",
        "hanja": "秘密維持義務",
        "hanjaReading": "비(숨길 비) + 밀(빽빽할 밀) + 유(오직 유) + 지(가질 지) + 의(마땅 의) + 무(힘쓸 무)",
        "pronunciation": "bimilyuji-uimu",
        "meaningKo": "의료인과 의료통역사가 업무 중 알게 된 환자의 개인정보와 의료정보를 외부에 누설하지 않을 법적, 윤리적 의무입니다. 환자의 진단명, 치료 내용, 개인 사생활 등 모든 정보가 포함되며, 이를 위반하면 법적 처벌을 받을 수 있습니다. 통역 시 주의할 점은 가족이라도 환자 본인의 동의 없이는 의료 정보를 공유할 수 없으며, 통역사는 통역 중 알게 된 정보를 절대 다른 사람에게 이야기해서는 안 됩니다. 외국인 환자의 경우 문화적으로 가족에게 모든 것을 공유하는 경향이 있으나, 한국 의료법은 엄격하므로 환자 본인 동의가 필수입니다.",
        "meaningVi": "Nghĩa vụ pháp lý và đạo đức của nhân viên y tế và thông dịch viên y tế không được tiết lộ thông tin cá nhân và y tế của bệnh nhân mà họ biết được trong quá trình làm việc. Bao gồm tất cả thông tin như chẩn đoán, điều trị, đời tư. Vi phạm có thể bị xử phạt theo pháp luật.",
        "context": "환자 권리, 의료 윤리, 개인정보 보호",
        "culturalNote": "한국은 개인정보보호법이 엄격하여 가족에게도 환자 동의 없이 정보를 주지 않지만, 베트남은 가족 중심 문화로 환자 정보를 가족과 공유하는 것이 자연스럽습니다. 이 문화적 차이로 인해 외국인 환자와 가족이 불편해할 수 있으므로, 법적 근거를 설명하며 이해를 구해야 합니다.",
        "commonMistakes": [
            {
                "mistake": "가족이라면 환자 동의 없이 정보 공유 가능하다고 설명",
                "correction": "가족이어도 환자 본인 동의 필수 - 법적 요건 명확히 안내",
                "explanation": "한국 의료법은 환자 본인 동의를 엄격히 요구함"
            },
            {
                "mistake": "통역사가 통역 후 환자 상황을 다른 사람에게 이야기",
                "correction": "통역 중 알게 된 정보는 절대 비밀 - 누구에게도 말하지 않기",
                "explanation": "비밀유지 의무 위반은 법적 책임과 직결됨"
            },
            {
                "mistake": "SNS에 환자 사례를 익명으로 올리면 괜찮다고 생각",
                "correction": "익명이어도 특정 가능한 정보는 유출 금지",
                "explanation": "간접적으로라도 환자 식별 가능하면 비밀유지 위반"
            }
        ],
        "examples": [
            {
                "ko": "비밀유지의무에 따라 환자분의 동의 없이는 가족에게도 정보를 드릴 수 없습니다.",
                "vi": "Theo nghĩa vụ bảo mật, không thể cung cấp thông tin cho gia đình nếu không có sự đồng ý của bệnh nhân.",
                "situation": "formal"
            },
            {
                "ko": "통역 중 알게 된 정보는 절대 외부에 공개하지 않습니다.",
                "vi": "Thông tin biết được trong quá trình thông dịch tuyệt đối không được tiết lộ ra bên ngoài.",
                "situation": "onsite"
            },
            {
                "ko": "환자 정보는 법으로 보호받아요. 아무에게도 말하면 안 돼요.",
                "vi": "Thông tin bệnh nhân được bảo vệ bởi pháp luật. Không được nói với ai cả.",
                "situation": "informal"
            }
        ],
        "relatedTerms": ["의료통역윤리", "환자권리장전", "개인정보보호"]
    },
    {
        "slug": "dong-y-truoc",
        "korean": "사전동의",
        "vietnamese": "đồng ý trước",
        "hanja": "事前同意",
        "hanjaReading": "사(일 사) + 전(앞 전) + 동(같을 동) + 의(뜻 의)",
        "pronunciation": "sajeon-dongui",
        "meaningKo": "의료행위를 시행하기 전에 환자에게 치료의 목적, 방법, 위험성, 부작용, 대안 등을 충분히 설명하고 환자의 자발적 동의를 얻는 과정입니다. 한국 의료법에서 필수적으로 요구하는 절차이며, 특히 수술, 마취, 침습적 검사, 연구 참여 등에서 반드시 서면 동의를 받아야 합니다. 통역 시 주의할 점은 환자가 내용을 정확히 이해하고 자발적으로 동의했는지 확인해야 하며, 이해하지 못한 상태에서 서명하지 않도록 해야 합니다. 외국인 환자는 언어 장벽으로 내용을 제대로 이해하지 못할 수 있으므로, 통역사의 명확하고 상세한 설명이 매우 중요합니다.",
        "meaningVi": "Quy trình giải thích đầy đủ cho bệnh nhân về mục đích, phương pháp, rủi ro, tác dụng phụ, phương án thay thế của điều trị và nhận được sự đồng ý tự nguyện của bệnh nhân trước khi thực hiện hành vi y tế. Là thủ tục bắt buộc theo Luật Y tế Hàn Quốc, đặc biệt cần có đồng ý bằng văn bản cho phẫu thuật, gây mê, xét nghiệm xâm lấn, tham gia nghiên cứu.",
        "context": "환자 권리, 의료 윤리, 법적 절차",
        "culturalNote": "한국은 사전동의 절차가 매우 엄격하지만, 베트남에서는 의사가 결정하고 환자가 따르는 경향이 강합니다. 외국인 환자는 사전동의서의 법적 중요성을 인식하지 못하고 형식적으로 서명하는 경우가 많아, 통역사가 이 문서의 중요성과 내용을 충분히 설명해야 합니다.",
        "commonMistakes": [
            {
                "mistake": "사전동의를 단순히 '서명'으로만 설명",
                "correction": "'đồng ý sau khi được giải thích đầy đủ' - 설명과 이해의 과정 강조",
                "explanation": "사전동의는 서명이 아니라 충분한 정보 제공 후 자발적 결정"
            },
            {
                "mistake": "환자가 이해하지 못해도 빨리 서명하도록 유도",
                "correction": "환자가 완전히 이해할 때까지 설명하고 질문 기회 제공",
                "explanation": "형식적 동의는 법적 효력이 없으며 환자 보호 실패"
            },
            {
                "mistake": "의학 용어를 그대로 통역하여 환자가 이해하지 못함",
                "correction": "의학 용어를 환자가 이해할 수 있는 쉬운 말로 풀어서 설명",
                "explanation": "환자의 진정한 이해가 사전동의의 핵심"
            }
        ],
        "examples": [
            {
                "ko": "수술 전 사전동의서를 작성하셔야 합니다. 모든 내용을 이해하셨나요?",
                "vi": "Trước phẫu thuật cần ký giấy đồng ý. Bạn đã hiểu hết nội dung chưa?",
                "situation": "formal"
            },
            {
                "ko": "사전동의는 환자의 권리를 보호하는 중요한 절차입니다.",
                "vi": "Đồng ý trước là thủ tục quan trọng bảo vệ quyền lợi của bệnh nhân.",
                "situation": "onsite"
            },
            {
                "ko": "이해되지 않는 부분이 있으면 서명하기 전에 꼭 물어보세요.",
                "vi": "Nếu có phần nào không hiểu, nhất định hỏi trước khi ký.",
                "situation": "informal"
            }
        ],
        "relatedTerms": ["충분한설명의무", "수술동의서", "환자권리장전"]
    },
    {
        "slug": "nghia-vu-giai-thich-day-du",
        "korean": "충분한설명의무",
        "vietnamese": "nghĩa vụ giải thích đầy đủ",
        "hanja": "充分한說明義務",
        "hanjaReading": "충(가득할 충) + 분(나눌 분) + 설(말씀 설) + 명(밝을 명) + 의(마땅 의) + 무(힘쓸 무)",
        "pronunciation": "chungbunhan-seolmyeong-uimu",
        "meaningKo": "의료인이 환자에게 질병의 상태, 치료 방법, 예상되는 결과, 부작용, 위험성, 대안적 치료법 등을 환자가 이해할 수 있도록 충분히 설명해야 할 법적 의무입니다. 단순히 의학 용어를 나열하는 것이 아니라, 환자의 교육 수준과 이해도에 맞춰 쉽게 설명해야 합니다. 통역 시 주의할 점은 의사의 설명을 정확히 통역하되, 환자가 이해하지 못한 부분이 있으면 의사에게 더 쉽게 설명해달라고 요청하는 것도 통역사의 역할입니다. 외국인 환자는 언어와 의료 시스템의 차이로 이해가 어려우므로, 통역사가 가교 역할을 충실히 해야 합니다.",
        "meaningVi": "Nghĩa vụ pháp lý của nhân viên y tế phải giải thích đầy đủ cho bệnh nhân về tình trạng bệnh, phương pháp điều trị, kết quả dự kiến, tác dụng phụ, rủi ro, phương pháp điều trị thay thế sao cho bệnh nhân có thể hiểu được. Không chỉ liệt kê thuật ngữ y học mà phải giải thích dễ hiểu phù hợp với trình độ và khả năng hiểu của bệnh nhân.",
        "context": "환자 권리, 의료 윤리, 법적 의무",
        "culturalNote": "한국은 의료 소송이 증가하면서 의사의 설명 의무가 강화되었지만, 베트남은 상대적으로 의사 권위가 강해 환자가 질문하기 어려운 문화입니다. 통역사는 환자가 이해하지 못해도 묻지 않는 경우가 많으므로, 능동적으로 이해 여부를 확인하고 필요시 추가 설명을 요청해야 합니다.",
        "commonMistakes": [
            {
                "mistake": "의사의 전문 용어를 그대로 베트남어 의학 용어로만 번역",
                "correction": "전문 용어 + 쉬운 말 설명 병행 - 환자가 실제로 이해할 수 있도록",
                "explanation": "의학 용어의 정확한 번역보다 환자의 이해가 우선"
            },
            {
                "mistake": "환자가 이해하지 못해도 의사에게 알리지 않음",
                "correction": "환자의 이해도를 확인하고 필요시 추가 설명 요청",
                "explanation": "통역사는 원활한 의사소통의 촉진자 역할 수행"
            },
            {
                "mistake": "설명 의무를 단순히 '의사가 말하는 것'으로만 이해",
                "correction": "환자가 이해하고 결정할 수 있을 때까지 설명하는 것",
                "explanation": "형식적 설명이 아닌 실질적 이해가 설명 의무의 핵심"
            }
        ],
        "examples": [
            {
                "ko": "의사는 충분한 설명 의무가 있으므로 이해될 때까지 설명드릴 것입니다.",
                "vi": "Bác sĩ có nghĩa vụ giải thích đầy đủ nên sẽ giải thích cho đến khi bạn hiểu.",
                "situation": "formal"
            },
            {
                "ko": "이해가 안 되는 부분이 있으면 편하게 질문하세요.",
                "vi": "Nếu có phần nào không hiểu, thoải mái hỏi nhé.",
                "situation": "onsite"
            },
            {
                "ko": "환자분이 이해하셨는지 확인이 필요합니다. 다시 한번 설명해 주시겠어요?",
                "vi": "Cần xác nhận xem bệnh nhân đã hiểu chưa. Có thể giải thích lại một lần nữa không?",
                "situation": "informal"
            }
        ],
        "relatedTerms": ["사전동의", "환자권리장전", "의료통역"]
    },
    {
        "slug": "hien-chuong-quyen-benh-nhan",
        "korean": "환자권리장전",
        "vietnamese": "hiến chương quyền bệnh nhân",
        "hanja": "患者權利章典",
        "hanjaReading": "환(근심 환) + 자(사람 자) + 권(권세 권) + 리(다스릴 리) + 장(글 장) + 전(법 전)",
        "pronunciation": "hwanja-gwolli-jangjeon",
        "meaningKo": "환자가 의료 과정에서 누려야 할 기본적 권리를 명시한 선언문으로, 진료받을 권리, 알 권리, 자기결정권, 비밀보장권, 상담 및 조력을 받을 권리 등이 포함됩니다. 한국 의료기관은 환자권리장전을 게시하고 환자에게 고지할 의무가 있습니다. 통역 시 주의할 점은 외국인 환자도 동등한 환자 권리를 가지며, 언어 장벽으로 권리를 행사하지 못하는 일이 없도록 통역사가 환자 권리를 안내하고 보호해야 합니다. 환자가 부당한 대우를 받거나 권리를 침해당했다고 느낄 때 적절한 구제 절차를 안내하는 것도 중요합니다.",
        "meaningVi": "Tuyên ngôn quy định các quyền cơ bản mà bệnh nhân phải được hưởng trong quá trình khám chữa bệnh, bao gồm quyền được khám chữa, quyền được biết, quyền tự quyết định, quyền bảo mật, quyền được tư vấn và hỗ trợ. Cơ sở y tế Hàn Quốc có nghĩa vụ niêm yết và thông báo Hiến chương Quyền Bệnh nhân.",
        "context": "환자 권리, 의료 윤리, 법적 보호",
        "culturalNote": "한국은 환자 권리가 법으로 보장되고 체계적이지만, 베트남은 여전히 의사 권위가 강하고 환자는 수동적인 경향이 있습니다. 외국인 환자는 자신의 권리를 모르고 부당한 대우를 참는 경우가 많으므로, 통역사가 환자 권리를 알려주고 필요시 권리 행사를 도와야 합니다.",
        "commonMistakes": [
            {
                "mistake": "환자권리장전을 형식적 문서로만 여김",
                "correction": "실제로 환자가 권리를 행사할 수 있도록 구체적 내용 안내",
                "explanation": "환자 권리는 실제 의료 현장에서 보장되어야 함"
            },
            {
                "mistake": "외국인은 권리가 제한적이라고 설명",
                "correction": "외국인도 동등한 환자 권리 보장 - 차별 없음 강조",
                "explanation": "국적과 관계없이 모든 환자는 동등한 권리 보유"
            },
            {
                "mistake": "환자가 권리를 주장하면 병원과 갈등을 우려하여 말림",
                "correction": "정당한 권리 행사를 지지하고 적절한 절차 안내",
                "explanation": "통역사는 환자의 권리 옹호자 역할도 수행"
            }
        ],
        "examples": [
            {
                "ko": "환자권리장전에 따라 치료에 대한 충분한 설명을 들으실 권리가 있습니다.",
                "vi": "Theo Hiến chương Quyền Bệnh nhân, bạn có quyền được giải thích đầy đủ về điều trị.",
                "situation": "formal"
            },
            {
                "ko": "외국인 환자님도 동일한 권리를 가지십니다.",
                "vi": "Bệnh nhân nước ngoài cũng có quyền như nhau.",
                "situation": "onsite"
            },
            {
                "ko": "불편한 점이 있으면 환자 권리를 주장할 수 있어요.",
                "vi": "Nếu có điều gì không thoải mái, bạn có thể đòi quyền của mình.",
                "situation": "informal"
            }
        ],
        "relatedTerms": ["사전동의", "비밀유지의무", "환자안전"]
    },
    {
        "slug": "quyet-dinh-duy-tri-su-song",
        "korean": "연명의료결정",
        "vietnamese": "quyết định duy trì sự sống",
        "hanja": "延命醫療決定",
        "hanjaReading": "연(늘일 연) + 명(목숨 명) + 의(의원 의) + 료(고칠 료) + 결(맺을 결) + 정(정할 정)",
        "pronunciation": "yeonmyeong-uiryo-gyeoljeong",
        "meaningKo": "회생 가능성이 없는 임종 과정의 환자에게 연명의료(심폐소생술, 인공호흡기, 혈액투석 등)를 시행할지 여부를 결정하는 것입니다. 한국은 '호스피스·완화의료 및 임종과정에 있는 환자의 연명의료결정에 관한 법률'에 따라 환자 본인의 의사를 최우선으로 하며, 사전연명의료의향서 작성이 가능합니다. 통역 시 주의할 점은 매우 민감하고 윤리적인 주제이므로, 환자와 가족의 감정을 배려하며 정확하고 신중하게 통역해야 합니다. 문화적으로 베트남은 가족이 결정하는 경향이 강하지만, 한국은 환자 본인의 의사가 우선이므로 이 차이를 이해시켜야 합니다.",
        "meaningVi": "Quyết định có thực hiện các biện pháp duy trì sự sống (hồi sức tim phổi, máy thở, lọc máu) cho bệnh nhân giai đoạn cuối không còn khả năng hồi phục hay không. Theo luật Hàn Quốc, ý chí của bệnh nhân được ưu tiên hàng đầu và có thể lập Giấy nguyện vọng về biện pháp duy trì sự sống trước.",
        "context": "임종 관리, 완화의료, 의료 윤리",
        "culturalNote": "한국은 환자 본인의 자기결정권을 존중하지만, 베트남을 포함한 많은 아시아 문화권에서는 가족이 집단으로 결정하는 것이 일반적입니다. 이 문화적 차이로 인해 외국인 환자와 가족이 혼란스러워하거나 갈등을 겪을 수 있으므로, 통역사는 한국 법의 취지와 문화적 차이를 모두 이해하고 중재 역할을 해야 합니다.",
        "commonMistakes": [
            {
                "mistake": "연명의료를 '안락사'로 오해하도록 통역",
                "correction": "연명의료 중단은 안락사가 아님 - 자연스러운 죽음을 받아들이는 것",
                "explanation": "안락사와 연명의료 중단은 완전히 다른 개념이므로 정확한 구분 필요"
            },
            {
                "mistake": "가족이 결정하면 된다고 설명",
                "correction": "환자 본인의 의사가 최우선 - 가족은 환자 의사를 확인하는 역할",
                "explanation": "한국 법은 환자 자기결정권을 강조하므로 문화적 차이 설명 필요"
            },
            {
                "mistake": "감정적으로 편향된 표현 사용",
                "correction": "중립적이고 존중하는 언어로 정확히 통역",
                "explanation": "민감한 주제이므로 통역사의 개인 가치관이나 감정을 배제"
            }
        ],
        "examples": [
            {
                "ko": "연명의료 결정은 환자 본인의 의사가 가장 중요합니다.",
                "vi": "Trong quyết định duy trì sự sống, ý chí của bệnh nhân quan trọng nhất.",
                "situation": "formal"
            },
            {
                "ko": "사전연명의료의향서를 작성하시면 본인의 뜻을 미리 밝힐 수 있습니다.",
                "vi": "Nếu lập Giấy nguyện vọng trước, có thể bày tỏ ý định của mình trước.",
                "situation": "onsite"
            },
            {
                "ko": "연명의료 중단은 안락사가 아니라 자연스러운 죽음을 받아들이는 거예요.",
                "vi": "Dừng duy trì sự sống không phải là an tử mà là chấp nhận cái chết tự nhiên.",
                "situation": "informal"
            }
        ],
        "relatedTerms": ["사전연명의료의향서", "호스피스", "완화의료"]
    },
    {
        "slug": "giay-nguyen-vong-duy-tri-su-song",
        "korean": "사전연명의료의향서",
        "vietnamese": "giấy nguyện vọng duy trì sự sống",
        "hanja": "事前延命醫療意向書",
        "hanjaReading": "사(일 사) + 전(앞 전) + 연(늘일 연) + 명(목숨 명) + 의(의원 의) + 료(고칠 료) + 의(뜻 의) + 향(향할 향) + 서(글 서)",
        "pronunciation": "sajeon-yeonmyeong-uiryo-uihyangseo",
        "meaningKo": "건강한 사람이 미리 작성하여 자신이 임종 과정에 있을 때 연명의료(심폐소생술, 인공호흡기 등)를 받을 것인지 거부할 것인지에 대한 의사를 밝히는 문서입니다. 만 19세 이상이면 작성할 수 있으며, 국가에 등록되어 법적 효력을 가집니다. 통역 시 주의할 점은 이 문서는 철회나 변경이 가능하며, 환자가 의사를 바꾸면 언제든 수정할 수 있다는 점을 안내해야 합니다. 외국인도 작성 가능하지만 절차와 의미를 정확히 이해하도록 도와야 합니다. 이는 생명과 관련된 매우 중요한 결정이므로 신중히 통역해야 합니다.",
        "meaningVi": "Văn bản do người khỏe mạnh lập trước để bày tỏ ý chí về việc có nhận các biện pháp duy trì sự sống (hồi sức tim phổi, máy thở) hay từ chối khi ở giai đoạn cuối. Người từ 19 tuổi trở lên có thể lập, được đăng ký quốc gia và có hiệu lực pháp lý.",
        "context": "사전 의료 계획, 자기결정권, 임종 준비",
        "culturalNote": "한국은 2018년부터 사전연명의료의향서 제도가 시행되어 많은 사람이 작성하지만, 베트남을 포함한 많은 국가에서는 이러한 제도가 생소합니다. 죽음에 대해 미리 계획하는 것을 불길하게 여기는 문화도 있으므로, 통역사는 이것이 자율성과 존엄성을 지키기 위한 권리임을 설명해야 합니다.",
        "commonMistakes": [
            {
                "mistake": "사전연명의료의향서를 '유언장'으로 오해하도록 통역",
                "correction": "유언장이 아니라 의료 결정에 관한 문서 - 재산과 무관",
                "explanation": "의료 의사 결정 문서와 재산 상속 문서는 완전히 다름"
            },
            {
                "mistake": "한번 작성하면 변경 불가하다고 설명",
                "correction": "언제든지 철회하거나 변경 가능 - 환자의 자율성 보장",
                "explanation": "의사가 바뀌면 수정할 수 있음을 알려 부담 줄이기"
            },
            {
                "mistake": "외국인은 작성할 수 없다고 안내",
                "correction": "외국인도 작성 가능 - 절차와 의미 정확히 설명",
                "explanation": "거주 외국인도 동등한 권리 보유"
            }
        ],
        "examples": [
            {
                "ko": "사전연명의료의향서는 본인의 의사를 미리 밝혀두는 문서입니다.",
                "vi": "Giấy nguyện vọng duy trì sự sống là văn bản bày tỏ ý chí của mình trước.",
                "situation": "formal"
            },
            {
                "ko": "외국인도 작성하실 수 있으며, 언제든 변경 가능합니다.",
                "vi": "Người nước ngoài cũng có thể lập và có thể thay đổi bất cứ lúc nào.",
                "situation": "onsite"
            },
            {
                "ko": "미리 작성해두면 본인의 뜻대로 의료를 받을 수 있어요.",
                "vi": "Nếu lập trước, có thể nhận điều trị theo ý muốn của mình.",
                "situation": "informal"
            }
        ],
        "relatedTerms": ["연명의료결정", "자기결정권", "호스피스"]
    },
    {
        "slug": "hien-tang-co-quan",
        "korean": "장기기증",
        "vietnamese": "hiến tặng cơ quan",
        "hanja": "臟器寄贈",
        "hanjaReading": "장(오장 장) + 기(그릇 기) + 기(부칠 기) + 증(줄 증)",
        "pronunciation": "janggi-gijeung",
        "meaningKo": "사망 후 또는 생존 시 자신의 장기(신장, 간, 심장, 폐, 각막 등)를 필요한 환자에게 기증하는 것입니다. 한국은 장기이식법에 따라 본인의 생전 동의가 원칙이며, 뇌사 기증과 사후 기증, 살아있는 기증자의 기증이 있습니다. 통역 시 주의할 점은 장기기증은 순수한 자발적 의사에 따라야 하며, 어떤 강요나 금전적 거래도 금지됩니다. 외국인도 기증 등록이 가능하지만, 문화적·종교적 신념에 따라 거부감이 있을 수 있으므로 존중하며 설명해야 합니다. 장기기증은 생명을 살리는 숭고한 행위이지만, 개인의 결정을 존중하는 것이 최우선입니다.",
        "meaningVi": "Hiến tặng cơ quan của mình (thận, gan, tim, phổi, giác mạc) cho bệnh nhân cần thiết sau khi chết hoặc khi còn sống. Theo luật ghép cơ quan Hàn Quốc, nguyên tắc là phải có sự đồng ý trước của bản thân, bao gồm hiến tặng chết não, hiến tặng sau khi chết, hiến tặng của người sống.",
        "context": "장기이식, 의료 윤리, 기증 문화",
        "culturalNote": "한국은 장기기증 문화가 점차 확산되고 있지만, 베트남을 포함한 많은 아시아 국가에서는 시신을 온전히 보존해야 한다는 전통적 신념이 강합니다. 또한 종교적 이유로 장기기증을 꺼리는 경우도 있으므로, 통역사는 환자의 문화적 배경을 이해하고 강요하지 않는 자세가 필요합니다.",
        "commonMistakes": [
            {
                "mistake": "장기기증을 단순히 '죽어서 장기 주는 것'으로만 설명",
                "correction": "뇌사 기증, 사후 기증, 살아있는 기증 구분하여 설명",
                "explanation": "기증 유형이 다양하며 각각 절차와 의미가 다름"
            },
            {
                "mistake": "장기기증을 권유하거나 설득하려는 태도",
                "correction": "정보만 제공하고, 결정은 전적으로 본인의 자유 - 중립 유지",
                "explanation": "통역사는 개인 신념을 강요해서는 안 되며 환자 자율성 존중"
            },
            {
                "mistake": "문화적·종교적 이유로 거부하는 것을 부정적으로 평가",
                "correction": "모든 결정을 존중 - 기증 거부도 정당한 선택",
                "explanation": "장기기증은 강요될 수 없으며 개인의 가치관 존중 필수"
            }
        ],
        "examples": [
            {
                "ko": "장기기증은 자발적 의사에 따라 결정하실 수 있습니다.",
                "vi": "Hiến tặng cơ quan có thể quyết định theo ý chí tự nguyện.",
                "situation": "formal"
            },
            {
                "ko": "외국인도 장기기증 등록이 가능하지만, 강제는 아닙니다.",
                "vi": "Người nước ngoài cũng có thể đăng ký hiến tặng cơ quan nhưng không bắt buộc.",
                "situation": "onsite"
            },
            {
                "ko": "종교적 이유로 거부하셔도 전혀 문제없어요.",
                "vi": "Nếu từ chối vì lý do tôn giáo, hoàn toàn không sao.",
                "situation": "informal"
            }
        ],
        "relatedTerms": ["뇌사판정", "장기이식", "사전동의"]
    },
    {
        "slug": "chan-doan-chet-nao",
        "korean": "뇌사판정",
        "vietnamese": "chẩn đoán chết não",
        "hanja": "腦死判定",
        "hanjaReading": "뇌(골 뇌) + 사(죽을 사) + 판(판단할 판) + 정(정할 정)",
        "pronunciation": "noesa-panjeong",
        "meaningKo": "뇌의 모든 기능이 비가역적으로 정지하여 회복 불가능한 상태를 의학적으로 판정하는 것입니다. 한국은 엄격한 뇌사 판정 기준이 있으며, 2명 이상의 전문의가 독립적으로 검사하여 판정합니다. 뇌사와 심장사는 다르며, 뇌사 판정 후에도 인공호흡기로 심장 박동을 유지할 수 있습니다. 통역 시 주의할 점은 뇌사 판정은 장기기증과 연결될 수 있지만, 뇌사 판정 자체가 장기기증을 강제하지 않으며, 가족의 동의가 필요합니다. 외국인 환자 가족은 뇌사 개념을 이해하기 어려워하므로, 신중하고 명확한 설명이 필요합니다.",
        "meaningVi": "Chẩn đoán y khoa xác định tình trạng tất cả chức năng não ngừng hoạt động không thể phục hồi. Hàn Quốc có tiêu chuẩn chẩn đoán chết não nghiêm ngặt, cần 2 bác sĩ chuyên khoa trở lên kiểm tra độc lập. Chết não khác với ngừng tim, sau khi chẩn đoán chết não vẫn có thể duy trì tim đập bằng máy thở.",
        "context": "중환자 관리, 장기기증, 임종 관리",
        "culturalNote": "베트남을 포함한 많은 국가에서 뇌사와 심장사를 명확히 구분하지 않거나, 뇌사를 죽음으로 받아들이기 어려워하는 경우가 많습니다. 심장이 뛰는데 죽었다고 하는 것에 대해 가족이 혼란스러워하거나 거부감을 가질 수 있으므로, 통역사는 감정을 배려하며 천천히 설명해야 합니다.",
        "commonMistakes": [
            {
                "mistake": "뇌사를 단순히 '혼수상태'로 번역",
                "correction": "뇌사는 'chết não' (비가역적 죽음), 혼수상태는 'hôn mê' (회복 가능) - 명확히 구분",
                "explanation": "뇌사와 혼수상태는 완전히 다른 개념이므로 정확한 구분 필수"
            },
            {
                "mistake": "뇌사 판정이 곧 장기기증을 의미한다고 설명",
                "correction": "뇌사 판정과 장기기증은 별개 - 기증은 가족의 자유 의사",
                "explanation": "뇌사 판정이 기증을 강제하지 않음을 명확히"
            },
            {
                "mistake": "의학적 설명만 하고 가족의 감정을 고려하지 않음",
                "correction": "의학적 정보 + 감정적 지지 - 가족의 슬픔과 혼란 이해",
                "explanation": "극도로 민감한 상황이므로 공감과 배려 필수"
            }
        ],
        "examples": [
            {
                "ko": "뇌사는 뇌의 모든 기능이 멈춘 상태로, 회복이 불가능합니다.",
                "vi": "Chết não là trạng thái tất cả chức năng não ngừng hoạt động, không thể phục hồi.",
                "situation": "formal"
            },
            {
                "ko": "뇌사 판정 후 장기기증은 가족의 결정에 달려 있습니다.",
                "vi": "Sau chẩn đoán chết não, hiến tặng cơ quan tùy thuộc quyết định của gia đình.",
                "situation": "onsite"
            },
            {
                "ko": "뇌사는 심장이 뛰어도 이미 돌아가신 상태예요. 이해하기 어려우시겠지만...",
                "vi": "Chết não nghĩa là đã mất dù tim còn đập. Có thể khó hiểu nhưng...",
                "situation": "informal"
            }
        ],
        "relatedTerms": ["장기기증", "연명의료결정", "인공호흡기"]
    },
    {
        "slug": "giay-dong-y-nghien-cuu-lam-sang",
        "korean": "임상시험동의서",
        "vietnamese": "giấy đồng ý nghiên cứu lâm sàng",
        "hanja": "臨床試驗同意書",
        "hanjaReading": "임(임할 임) + 상(자리 상) + 시(시험할 시) + 험(시험할 험) + 동(같을 동) + 의(뜻 의) + 서(글 서)",
        "pronunciation": "imsang-siheom-donguiseo",
        "meaningKo": "신약이나 의료기기의 안전성과 효과를 검증하기 위한 임상시험에 참여하기 전에 환자가 시험의 목적, 절차, 위험성, 이익, 권리 등을 충분히 이해하고 자발적으로 동의했음을 확인하는 문서입니다. 일반 치료와 달리 임상시험은 아직 검증되지 않은 치료법이므로, 더욱 엄격한 설명과 동의 과정이 필요합니다. 통역 시 주의할 점은 환자가 임상시험의 실험적 성격, 예상되는 위험, 언제든 철회할 수 있는 권리 등을 정확히 이해하도록 해야 하며, 무료 치료라는 이유만으로 충분한 이해 없이 동의하지 않도록 주의해야 합니다.",
        "meaningVi": "Văn bản xác nhận bệnh nhân đã hiểu đầy đủ về mục đích, quy trình, rủi ro, lợi ích, quyền lợi của thử nghiệm lâm sàng để kiểm chứng tính an toàn và hiệu quả của thuốc mới hoặc thiết bị y tế, và đồng ý tự nguyện tham gia. Khác với điều trị thông thường, thử nghiệm lâm sàng là phương pháp chưa được kiểm chứng nên cần quy trình giải thích và đồng ý nghiêm ngặt hơn.",
        "context": "임상연구, 신약 개발, 환자 보호",
        "culturalNote": "한국은 임상시험에 대한 규제가 엄격하지만, 일부 국가에서는 느슨할 수 있어 외국인 환자가 임상시험의 위험성을 과소평가할 수 있습니다. 특히 경제적으로 어려운 환자는 무료 치료에 혹해 충분한 이해 없이 동의하는 경우가 있으므로, 통역사는 환자 보호를 위해 더욱 신중히 설명해야 합니다.",
        "commonMistakes": [
            {
                "mistake": "임상시험을 일반 치료와 같은 것으로 설명",
                "correction": "실험적 치료이며 효과와 안전성이 아직 완전히 검증되지 않았음을 강조",
                "explanation": "환자가 임상시험의 실험적 성격을 정확히 인식해야 함"
            },
            {
                "mistake": "무료 치료만 강조하고 위험성은 축소",
                "correction": "이익과 위험을 균형 있게 설명 - 환자의 정보에 기반한 결정 지원",
                "explanation": "편향된 정보 제공은 환자의 자율적 결정을 방해함"
            },
            {
                "mistake": "한번 동의하면 중도 철회가 어렵다고 설명",
                "correction": "언제든지 불이익 없이 철회 가능 - 환자의 권리 명확히 안내",
                "explanation": "철회권은 환자 보호의 핵심 장치"
            }
        ],
        "examples": [
            {
                "ko": "이 치료는 임상시험으로, 아직 효과가 완전히 검증되지 않았습니다.",
                "vi": "Điều trị này là thử nghiệm lâm sàng, hiệu quả chưa được kiểm chứng hoàn toàn.",
                "situation": "formal"
            },
            {
                "ko": "임상시험은 언제든지 중단하실 수 있으며, 불이익은 없습니다.",
                "vi": "Thử nghiệm lâm sàng có thể dừng bất cứ lúc nào, không có bất lợi gì.",
                "situation": "onsite"
            },
            {
                "ko": "무료라고 해서 서둘러 결정하지 마시고, 충분히 생각해보세요.",
                "vi": "Dù miễn phí, đừng vội quyết định, hãy suy nghĩ kỹ.",
                "situation": "informal"
            }
        ],
        "relatedTerms": ["사전동의", "충분한설명의무", "환자권리"]
    },
    {
        "slug": "ho-so-benh-an-dien-tu",
        "korean": "전자의무기록",
        "vietnamese": "hồ sơ bệnh án điện tử",
        "hanja": "電子醫務記錄",
        "hanjaReading": "전(번개 전) + 자(글자 자) + 의(의원 의) + 무(일 무) + 기(기록할 기) + 록(기록할 록)",
        "pronunciation": "jeonja-uimu-girok",
        "meaningKo": "환자의 진료 정보를 전자적으로 기록하고 관리하는 시스템(EMR: Electronic Medical Record)으로, 진단, 검사 결과, 처방, 수술 기록 등 모든 의료 정보가 디지털로 저장됩니다. 한국 대부분의 병원이 전자의무기록을 사용하며, 병원 간 정보 공유, 의료의 질 향상, 환자 안전 증진에 기여합니다. 통역 시 주의할 점은 전자의무기록도 개인정보보호 대상이며, 환자 본인만 열람 권한이 있고, 환자는 자신의 의무기록 사본을 요청할 권리가 있다는 점을 안내해야 합니다. 외국인 환자가 의무기록 사본이 필요한 경우 신청 절차를 안내해야 합니다.",
        "meaningVi": "Hệ thống ghi chép và quản lý thông tin khám chữa bệnh của bệnh nhân bằng điện tử (EMR), lưu trữ tất cả thông tin y tế như chẩn đoán, kết quả xét nghiệm, đơn thuốc, hồ sơ phẫu thuật dưới dạng kỹ thuật số. Hầu hết bệnh viện Hàn Quốc sử dụng hồ sơ bệnh án điện tử, góp phần chia sẻ thông tin giữa các bệnh viện, nâng cao chất lượng y tế, tăng cường an toàn bệnh nhân.",
        "context": "의료 정보화, 환자 기록, 병원 시스템",
        "culturalNote": "한국은 의료 정보화가 매우 발달하여 전자의무기록이 표준이지만, 베트남을 포함한 많은 국가에서는 여전히 종이 기록을 사용하는 경우가 많습니다. 외국인 환자는 자신의 의무기록을 본국으로 가져가고 싶어하는 경우가 많으므로, 사본 발급 절차를 안내하는 것이 도움이 됩니다.",
        "commonMistakes": [
            {
                "mistake": "전자의무기록을 단순히 '컴퓨터에 저장하는 것'으로만 설명",
                "correction": "법적 효력이 있는 공식 의료 기록 - 종이 기록과 동일한 법적 지위",
                "explanation": "전자의무기록의 법적 중요성 인식 필요"
            },
            {
                "mistake": "누구나 환자 기록을 볼 수 있다고 설명",
                "correction": "환자 본인과 치료 담당 의료진만 열람 가능 - 개인정보보호",
                "explanation": "의무기록은 엄격히 보호되는 개인정보"
            },
            {
                "mistake": "의무기록 사본 발급이 어렵거나 불가능하다고 안내",
                "correction": "환자 본인은 사본 발급 권리 있음 - 신청 절차 안내",
                "explanation": "환자의 정보 접근 권리 보장"
            }
        ],
        "examples": [
            {
                "ko": "전자의무기록으로 어느 병원에서나 과거 진료 기록을 확인할 수 있습니다.",
                "vi": "Với hồ sơ bệnh án điện tử, có thể xem hồ sơ khám chữa bệnh trước ở bất kỳ bệnh viện nào.",
                "situation": "formal"
            },
            {
                "ko": "본인의 의무기록 사본이 필요하시면 원무과에 신청하시면 됩니다.",
                "vi": "Nếu cần bản sao hồ sơ bệnh án của mình, có thể nộp đơn tại phòng hành chính.",
                "situation": "onsite"
            },
            {
                "ko": "의무기록은 개인정보라서 본인만 볼 수 있어요.",
                "vi": "Hồ sơ bệnh án là thông tin cá nhân nên chỉ bản thân mới xem được.",
                "situation": "informal"
            }
        ],
        "relatedTerms": ["의무기록사본발급", "개인정보보호", "비밀유지의무"]
    },
    {
        "slug": "giay-gioi-thieu-kham-benh",
        "korean": "진료의뢰서",
        "vietnamese": "giấy giới thiệu khám bệnh",
        "hanja": "診療依賴書",
        "hanjaReading": "진(살필 진) + 료(고칠 료) + 의(의지할 의) + 뢰(믿을 뢰) + 서(글 서)",
        "pronunciation": "jillyo-uiroeseo",
        "meaningKo": "1차 의료기관(의원)에서 진료 후 더 전문적인 치료가 필요하다고 판단될 때, 상급 병원으로 환자를 보내며 작성하는 공식 문서입니다. 환자의 현재 상태, 진단명, 검사 결과, 의뢰 목적 등이 기재되며, 이를 통해 상급 병원 의사가 환자 상태를 빠르게 파악할 수 있습니다. 통역 시 주의할 점은 진료의뢰서가 있으면 상급 병원 진료 시 본인부담금이 경감되고, 없으면 가산금이 부과되므로 환자에게 반드시 챙기도록 안내해야 합니다. 외국인 환자는 이 제도를 모르는 경우가 많아 불필요한 비용을 부담하게 될 수 있습니다.",
        "meaningVi": "Văn bản chính thức do cơ sở y tế tuyến 1 (phòng khám) lập khi sau khi khám bệnh, đánh giá cần điều trị chuyên sâu hơn, giới thiệu bệnh nhân đến bệnh viện tuyến cao hơn. Ghi chép tình trạng hiện tại, chẩn đoán, kết quả xét nghiệm, mục đích giới thiệu, giúp bác sĩ bệnh viện tuyến cao nắm bắt nhanh tình trạng bệnh nhân.",
        "context": "의료 의뢰, 병원 이용, 진료비 절감",
        "culturalNote": "한국은 의료 전달 체계가 확립되어 1차→2차→3차 병원으로 단계적으로 진료받는 것이 원칙이지만, 베트남은 환자가 처음부터 큰 병원에 가는 경우가 많습니다. 외국인 환자는 진료의뢰서 없이 직접 대형 병원에 가면 비용이 더 들고 대기 시간도 길어질 수 있으므로, 제도를 설명하고 의뢰서를 받도록 안내하는 것이 중요합니다.",
        "commonMistakes": [
            {
                "mistake": "진료의뢰서를 단순히 '소개서'로만 번역",
                "correction": "'giấy giới thiệu khám bệnh' + 본인부담금 경감 효과 설명",
                "explanation": "경제적 이익을 명확히 알려야 환자가 챙김"
            },
            {
                "mistake": "의뢰서 없이도 문제없다고 안내",
                "correction": "의뢰서 없으면 가산금 부과 - 반드시 챙기도록 강조",
                "explanation": "환자의 불필요한 비용 부담 예방"
            },
            {
                "mistake": "의뢰서의 의학 정보를 환자에게 상세히 설명",
                "correction": "의뢰서는 의사 간 문서 - 환자에게는 간략히 설명하고 상급 병원 의사가 자세히 설명할 것임을 안내",
                "explanation": "통역사가 의학적 해석을 과도하게 하면 안 됨"
            }
        ],
        "examples": [
            {
                "ko": "진료의뢰서를 가지고 가시면 진료비가 줄어듭니다.",
                "vi": "Nếu mang giấy giới thiệu khám bệnh, chi phí khám sẽ giảm.",
                "situation": "formal"
            },
            {
                "ko": "의뢰서 없이 대형 병원에 가면 비용이 더 들어요.",
                "vi": "Nếu đến bệnh viện lớn không có giấy giới thiệu, chi phí cao hơn.",
                "situation": "onsite"
            },
            {
                "ko": "의뢰서 꼭 챙기세요. 돈 아낄 수 있어요.",
                "vi": "Nhớ mang giấy giới thiệu. Tiết kiệm được tiền.",
                "situation": "informal"
            }
        ],
        "relatedTerms": ["본인부담금", "상급종합병원", "진료비"]
    },
    {
        "slug": "giay-kham-benh",
        "korean": "소견서",
        "vietnamese": "giấy khám bệnh",
        "hanja": "所見書",
        "hanjaReading": "소(바 소) + 견(볼 견) + 서(글 서)",
        "pronunciation": "sogyeonseo",
        "meaningKo": "의사가 환자를 진찰한 결과를 기록한 문서로, 현재 건강 상태, 진단, 향후 치료 계획 등이 간략히 기재됩니다. 진단서보다 간단하며 법적 효력은 약하지만, 회사 제출용, 학교 제출용, 보험 청구용 등 다양한 용도로 사용됩니다. 통역 시 주의할 점은 소견서와 진단서의 차이를 명확히 알고, 환자가 어떤 목적으로 필요한지 확인하여 적절한 문서를 안내해야 합니다. 소견서는 진단서보다 저렴하므로, 법적 용도가 아니라면 소견서로 충분한 경우가 많습니다. 외국인 환자는 이 차이를 몰라 불필요하게 비싼 진단서를 발급받는 경우가 있습니다.",
        "meaningVi": "Văn bản ghi chép kết quả khám bệnh của bác sĩ, ghi chép ngắn gọn tình trạng sức khỏe hiện tại, chẩn đoán, kế hoạch điều trị sau này. Đơn giản hơn giấy chẩn đoán và hiệu lực pháp lý yếu hơn, nhưng được sử dụng cho nhiều mục đích như nộp công ty, trường học, yêu cầu bảo hiểm.",
        "context": "의료 문서, 회사 제출, 보험 청구",
        "culturalNote": "한국은 의료 문서가 세분화되어 있어 소견서와 진단서가 구분되지만, 베트남에서는 이러한 구분이 덜 명확할 수 있습니다. 외국인 환자는 모든 경우에 진단서를 요청하여 불필요한 비용을 지불하는 경우가 있으므로, 통역사가 용도를 확인하고 적절한 문서를 안내하는 것이 경제적으로 도움이 됩니다.",
        "commonMistakes": [
            {
                "mistake": "소견서와 진단서를 같은 것으로 설명",
                "correction": "소견서는 'giấy khám bệnh' (간단, 저렴), 진단서는 'giấy chẩn đoán' (법적 효력, 비쌈) - 차이 명확히",
                "explanation": "용도와 비용이 다르므로 환자가 적절한 선택 필요"
            },
            {
                "mistake": "무조건 진단서를 발급받으라고 안내",
                "correction": "용도 확인 후 소견서로 충분한지 판단 - 비용 절감 도움",
                "explanation": "불필요한 비용 부담 방지"
            },
            {
                "mistake": "소견서의 의학 내용을 환자에게 자의적으로 해석",
                "correction": "있는 그대로 통역하고, 추가 설명은 의사에게 요청",
                "explanation": "통역사는 의료 자문 제공 금지"
            }
        ],
        "examples": [
            {
                "ko": "회사 제출용이시라면 진단서보다 소견서가 경제적입니다.",
                "vi": "Nếu nộp cho công ty, giấy khám bệnh tiết kiệm hơn giấy chẩn đoán.",
                "situation": "formal"
            },
            {
                "ko": "소견서는 오늘 바로 발급 가능하고, 진단서는 며칠 걸립니다.",
                "vi": "Giấy khám bệnh có thể cấp ngay hôm nay, giấy chẩn đoán mất vài ngày.",
                "situation": "onsite"
            },
            {
                "ko": "법원 제출용이 아니면 소견서면 충분해요.",
                "vi": "Nếu không nộp tòa, giấy khám bệnh là đủ.",
                "situation": "informal"
            }
        ],
        "relatedTerms": ["진단서", "의무기록사본발급", "증명서"]
    },
    {
        "slug": "giay-chan-doan",
        "korean": "진단서",
        "vietnamese": "giấy chẩn đoán",
        "hanja": "診斷書",
        "hanjaReading": "진(살필 진) + 단(끊을 단) + 서(글 서)",
        "pronunciation": "jindanseo",
        "meaningKo": "의사가 환자의 질병 상태를 진단하고 그 결과를 공식적으로 증명하는 법적 효력이 있는 의료 문서입니다. 진단명, 발병 일자, 치료 내용, 향후 치료 계획 등이 상세히 기재되며, 법원 제출용, 보험 청구용, 장애 판정용 등 법적 용도로 주로 사용됩니다. 통역 시 주의할 점은 진단서는 소견서보다 발급 비용이 높고, 의사의 신중한 판단이 필요하므로 발급까지 시간이 걸릴 수 있으며, 한 번 발급된 진단서는 의사가 임의로 수정할 수 없다는 점입니다. 외국인 환자는 진단서가 법적 문서임을 인식하고 정확한 정보를 의사에게 제공해야 합니다.",
        "meaningVi": "Văn bản y tế có hiệu lực pháp lý do bác sĩ chẩn đoán tình trạng bệnh của bệnh nhân và chứng nhận chính thức. Ghi chép chi tiết tên bệnh, ngày mắc bệnh, nội dung điều trị, kế hoạch điều trị sau này, chủ yếu dùng cho mục đích pháp lý như nộp tòa án, yêu cầu bảo hiểm, giám định khuyết tật.",
        "context": "법적 문서, 보험 청구, 장애 판정",
        "culturalNote": "한국은 진단서의 법적 중요성이 매우 높아 의사가 신중하게 작성하지만, 일부 국가에서는 진단서 발급이 상대적으로 쉬울 수 있습니다. 외국인 환자가 진단서를 가볍게 여기거나, 반대로 거짓 정보를 제공하여 유리한 내용을 받으려 할 수 있으나, 이는 법적 문제를 일으킬 수 있으므로 정직하게 진술해야 함을 안내해야 합니다.",
        "commonMistakes": [
            {
                "mistake": "진단서를 단순히 '병원 서류'로만 설명",
                "correction": "'giấy chẩn đoán có hiệu lực pháp lý' - 법적 문서임을 강조",
                "explanation": "진단서의 법적 중요성 인식 필요"
            },
            {
                "mistake": "환자가 원하는 내용으로 진단서를 써달라고 의사에게 요청하도록 통역",
                "correction": "진단서는 객관적 사실만 기재 가능 - 환자 요구대로 작성 불가 설명",
                "explanation": "허위 진단서는 의사와 환자 모두 법적 처벌 대상"
            },
            {
                "mistake": "진단서 발급이 즉시 가능하다고 안내",
                "correction": "진단서는 발급까지 시간 소요 가능 - 의사의 신중한 판단 필요",
                "explanation": "법적 문서이므로 충분한 검토 시간 필요"
            }
        ],
        "examples": [
            {
                "ko": "진단서는 법적 효력이 있으므로 정확한 정보를 말씀해주셔야 합니다.",
                "vi": "Giấy chẩn đoán có hiệu lực pháp lý nên phải cung cấp thông tin chính xác.",
                "situation": "formal"
            },
            {
                "ko": "진단서는 발급까지 며칠 걸릴 수 있습니다.",
                "vi": "Giấy chẩn đoán có thể mất vài ngày để cấp.",
                "situation": "onsite"
            },
            {
                "ko": "진단서는 의사가 사실만 쓸 수 있어서, 원하는 내용으로 못 써요.",
                "vi": "Giấy chẩn đoán bác sĩ chỉ ghi sự thật, không thể viết theo ý muốn.",
                "situation": "informal"
            }
        ],
        "relatedTerms": ["소견서", "의무기록사본발급", "법적증명"]
    },
    {
        "slug": "don-thuoc-ke",
        "korean": "처방전",
        "vietnamese": "đơn thuốc kê",
        "hanja": "處方箋",
        "hanjaReading": "처(처리할 처) + 방(방법 방) + 전(종이 전)",
        "pronunciation": "cheobangjeon",
        "meaningKo": "의사가 환자의 질병 치료를 위해 필요한 약물의 종류, 용량, 복용 방법 등을 기재하여 약사에게 조제를 지시하는 공식 문서입니다. 한국은 의약분업이 시행되어 처방전이 있어야 약국에서 전문 의약품을 구입할 수 있습니다. 통역 시 주의할 점은 처방전의 유효 기간(보통 발행일로부터 3일)이 있으며, 환자가 약물 알레르기나 복용 중인 다른 약이 있으면 반드시 의사에게 알려야 한다는 점입니다. 외국인 환자는 베트남에서 쉽게 구할 수 있던 약이 한국에서는 처방전이 필요한 경우가 많아 불편해할 수 있으므로, 의약분업 제도를 설명해야 합니다.",
        "meaningVi": "Văn bản chính thức do bác sĩ ghi chép loại thuốc, liều lượng, cách dùng cần thiết để điều trị bệnh của bệnh nhân và chỉ thị cho dược sĩ pha chế. Hàn Quốc thực hiện phân công y dược, phải có đơn thuốc kê mới mua được thuốc chuyên môn ở nhà thuốc.",
        "context": "약물 치료, 약국 이용, 의약분업",
        "culturalNote": "베트남에서는 많은 약을 처방전 없이 구입할 수 있지만, 한국은 의약분업이 엄격하여 항생제, 진통제 등 대부분의 전문 의약품은 처방전이 필수입니다. 외국인 환자는 이 차이로 불편을 느끼거나, 불법으로 약을 구하려는 시도를 할 수 있으므로, 환자 안전을 위한 제도임을 설명하고 정당한 절차를 안내해야 합니다.",
        "commonMistakes": [
            {
                "mistake": "처방전 없이도 약국에서 약을 살 수 있다고 안내",
                "correction": "한국은 의약분업 - 처방약은 반드시 처방전 필요",
                "explanation": "잘못된 정보는 환자가 약을 구하지 못하거나 불법 경로를 시도하게 할 수 있음"
            },
            {
                "mistake": "약물 알레르기나 복용 중인 약을 의사에게 알리지 않아도 된다고 설명",
                "correction": "약물 상호작용 위험 - 반드시 모든 약물 정보 제공 필요",
                "explanation": "약물 상호작용은 생명과 직결될 수 있음"
            },
            {
                "mistake": "처방전 유효 기간을 안내하지 않음",
                "correction": "처방전은 발행 후 3일 내 사용 - 기간 지나면 재진료 필요",
                "explanation": "유효 기간 경과 시 약 조제 불가"
            }
        ],
        "examples": [
            {
                "ko": "처방전은 발행일로부터 3일 이내에 약국에 가져가셔야 합니다.",
                "vi": "Đơn thuốc kê phải mang đến nhà thuốc trong vòng 3 ngày kể từ ngày cấp.",
                "situation": "formal"
            },
            {
                "ko": "알레르기가 있는 약이나 복용 중인 약이 있으면 꼭 말씀하세요.",
                "vi": "Nếu có thuốc dị ứng hoặc đang uống thuốc nào, nhất định phải nói.",
                "situation": "onsite"
            },
            {
                "ko": "한국은 처방전 없이 항생제를 못 사요. 의사한테 받아야 해요.",
                "vi": "Ở Hàn Quốc không mua được kháng sinh không có đơn. Phải nhận từ bác sĩ.",
                "situation": "informal"
            }
        ],
        "relatedTerms": ["약국", "의약분업", "복약지도"]
    },
    {
        "slug": "tom-tat-xuat-vien",
        "korean": "퇴원요약",
        "vietnamese": "tóm tắt xuất viện",
        "hanja": "退院要約",
        "hanjaReading": "퇴(물러날 퇴) + 원(집 원) + 요(요긴할 요) + 약(간략할 약)",
        "pronunciation": "toewon-yoyak",
        "meaningKo": "환자가 입원 치료를 마치고 퇴원할 때 의사가 작성하는 요약 문서로, 입원 사유, 진단명, 치료 경과, 수술 내용, 퇴원 시 상태, 퇴원 후 주의사항 및 치료 계획 등이 기재됩니다. 환자의 입원 기간 동안의 의료 정보가 체계적으로 정리되어 있어, 다른 병원으로 전원하거나 외래 진료를 받을 때 중요한 참고 자료가 됩니다. 통역 시 주의할 점은 퇴원요약서에는 중요한 주의사항(약물 복용, 식이 조절, 활동 제한, 재진 일정 등)이 포함되어 있으므로, 환자가 정확히 이해하도록 상세히 설명해야 합니다. 외국인 환자는 언어 장벽으로 퇴원 후 관리를 제대로 못 하는 경우가 많아 합병증 위험이 높으므로, 통역사의 명확한 설명이 매우 중요합니다.",
        "meaningVi": "Văn bản tóm tắt do bác sĩ lập khi bệnh nhân hoàn thành điều trị nội trú và xuất viện, ghi chép lý do nhập viện, chẩn đoán, diễn biến điều trị, nội dung phẫu thuật, tình trạng khi xuất viện, lưu ý sau xuất viện và kế hoạch điều trị. Thông tin y tế trong thời gian nằm viện được tổng hợp có hệ thống, là tài liệu tham khảo quan trọng khi chuyển viện hoặc khám ngoại trú.",
        "context": "퇴원 관리, 치료 연속성, 환자 교육",
        "culturalNote": "한국은 퇴원 시 체계적인 퇴원 교육을 제공하지만, 베트남에서는 상대적으로 간략할 수 있습니다. 외국인 환자는 퇴원 후 관리의 중요성을 과소평가하거나, 퇴원요약서를 단순한 서류로 여겨 잘 보관하지 않는 경우가 있으므로, 이 문서의 중요성과 활용 방법을 강조해야 합니다.",
        "commonMistakes": [
            {
                "mistake": "퇴원요약서를 형식적으로만 통역하고 내용을 확인하지 않음",
                "correction": "환자가 퇴원 후 주의사항을 이해했는지 확인하고, 질문 기회 제공",
                "explanation": "퇴원 후 관리 실패는 재입원으로 이어질 수 있음"
            },
            {
                "mistake": "의학 용어를 그대로 번역하여 환자가 이해하지 못함",
                "correction": "전문 용어를 쉬운 말로 풀어서 설명하고, 구체적 예시 제공",
                "explanation": "환자의 실제 이해와 실천이 목적"
            },
            {
                "mistake": "퇴원요약서를 보관하지 않아도 된다고 안내",
                "correction": "재진 시 또는 다른 병원 방문 시 필요 - 잘 보관하도록 강조",
                "explanation": "퇴원요약서는 중요한 의료 기록"
            }
        ],
        "examples": [
            {
                "ko": "퇴원요약서에 퇴원 후 주의사항이 자세히 나와 있으니 잘 읽어보세요.",
                "vi": "Tóm tắt xuất viện có ghi chi tiết lưu ý sau xuất viện, hãy đọc kỹ.",
                "situation": "formal"
            },
            {
                "ko": "재진은 2주 후이고, 그 전에 이상 증상이 있으면 즉시 응급실로 오세요.",
                "vi": "Tái khám sau 2 tuần, nếu có triệu chứng bất thường trước đó, hãy đến phòng cấp cứu ngay.",
                "situation": "onsite"
            },
            {
                "ko": "퇴원요약서 잘 보관하세요. 다른 병원 갈 때 꼭 필요해요.",
                "vi": "Giữ tóm tắt xuất viện cẩn thận. Đến bệnh viện khác nhất định cần.",
                "situation": "informal"
            }
        ],
        "relatedTerms": ["퇴원", "재진", "입원"]
    }
]

# Read existing data
with open(file_path, 'r', encoding='utf-8') as f:
    data = json.load(f)

# Add new terms from part 2
data.extend(new_terms_part2)

# Write back
with open(file_path, 'w', encoding='utf-8') as f:
    json.dump(data, f, ensure_ascii=False, indent=2)

print(f"✅ Successfully added {len(new_terms_part2)} more medical terms (Part 2)")
print(f"📊 Total terms now: {len(data)}")
