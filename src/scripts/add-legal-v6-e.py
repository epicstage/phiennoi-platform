#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""의료분쟁 용어 추가 스크립트 (v6-e)"""

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
            "slug": "loi-y-khoa",
            "korean": "의료과실",
            "vietnamese": "Lỗi y khoa",
            "hanja": "醫療過失",
            "hanjaReading": "醫(의원 의) 療(치료 료) 過(지날 과) 失(잃을 실)",
            "pronunciation": "이료과실",
            "meaningKo": "의사나 의료인이 진료 과정에서 주의의무를 다하지 못하여 환자에게 손해를 입힌 과실을 말합니다. 통역 시 '실수'와 구분해야 하며, 법적 책임이 따르는 과실임을 명확히 해야 합니다. 베트남에서는 'sai sót'(실수)과 'lỗi'(과실)을 구분하므로 주의가 필요합니다. 의료사고 중에서도 의료인의 주의의무 위반이 인정되어야 과실로 인정되며, 단순한 의료사고와는 법적 의미가 다릅니다. 통역사는 이 차이를 명확히 전달해야 합니다.",
            "meaningVi": "Lỗi y khoa là hành vi của bác sĩ hoặc nhân viên y tế không thực hiện đầy đủ nghĩa vụ chăm sóc trong quá trình khám chữa bệnh, gây thiệt hại cho bệnh nhân. Đây là khái niệm pháp lý quan trọng trong tranh chấp y tế, khác với 'sai sót' đơn thuần vì có trách nhiệm pháp lý đi kèm.",
            "context": "의료소송, 손해배상 청구, 의료사고 조사에서 사용",
            "culturalNote": "한국은 의료과실 입증책임이 환자 측에 있어 소송이 어렵지만, 베트남은 의료기관의 설명책임이 더 강조됩니다. 한국의 경우 대한의사협회의 감정이 중요한 역할을 하지만, 베트남은 보건부 산하 감정기관의 의견이 결정적입니다. 통역 시 양국의 입증책임 차이를 설명해야 합니다.",
            "commonMistakes": [
                {
                    "mistake": "'sai lầm y khoa'로 번역",
                    "correction": "'lỗi y khoa' 사용",
                    "explanation": "'sai lầm'은 단순 실수를 의미하여 법적 책임의 무게감이 약함"
                },
                {
                    "mistake": "의료사고와 의료과실을 동일하게 번역",
                    "correction": "의료사고는 'tai nạn y khoa', 의료과실은 'lỗi y khoa'",
                    "explanation": "사고는 과실 없이도 발생 가능하지만, 과실은 주의의무 위반이 전제됨"
                },
                {
                    "mistake": "'과실'을 'sơ suất'로 번역",
                    "correction": "'lỗi'로 번역",
                    "explanation": "'sơ suất'은 부주의를 의미하고, 'lỗi'는 법적 책임이 있는 과실을 의미함"
                }
            ],
            "examples": [
                {
                    "ko": "환자 측은 의사의 의료과실로 인한 손해배상을 청구했습니다.",
                    "vi": "Phía bệnh nhân đã yêu cầu bồi thường thiệt hại do lỗi y khoa của bác sĩ.",
                    "situation": "formal"
                },
                {
                    "ko": "의료과실이 인정되려면 주의의무 위반이 입증되어야 합니다.",
                    "vi": "Để được công nhận là lỗi y khoa, cần phải chứng minh có sự vi phạm nghĩa vụ chăm sóc.",
                    "situation": "formal"
                },
                {
                    "ko": "수술 중 의료과실로 환자가 심각한 후유증을 겪게 되었습니다.",
                    "vi": "Do lỗi y khoa trong quá trình phẫu thuật, bệnh nhân đã bị di chứng nghiêm trọng.",
                    "situation": "onsite"
                }
            ],
            "relatedTerms": ["의료사고", "주의의무", "손해배상", "의료소송"]
        },
        {
            "slug": "kien-y-khoa",
            "korean": "의료소송",
            "vietnamese": "Kiện y khoa",
            "hanja": "醫療訴訟",
            "hanjaReading": "醫(의원 의) 療(치료 료) 訴(하소연 소) 訟(송사 송)",
            "pronunciation": "이료소송",
            "meaningKo": "의료행위와 관련하여 환자나 보호자가 의료기관 또는 의료인을 상대로 제기하는 민사 또는 형사소송을 말합니다. 통역 시 민사소송(손해배상)과 형사소송(업무상과실치상)을 명확히 구분해야 하며, 베트남어로 각각 'kiện dân sự'와 'kiện hình sự'로 표현합니다. 의료소송은 전문성이 높아 감정인의 의견이 중요하며, 통역사는 의학용어와 법률용어를 모두 정확히 전달해야 합니다. 한국은 의료분쟁조정중재원을 통한 조정이 활성화되어 있지만, 베트남은 직접 소송으로 가는 경우가 많습니다.",
            "meaningVi": "Kiện y khoa là vụ kiện dân sự hoặc hình sự mà bệnh nhân hoặc người nhà khởi kiện cơ sở y tế hoặc nhân viên y tế liên quan đến hành vi khám chữa bệnh. Đây là loại vụ kiện chuyên môn cao, đòi hỏi giám định y khoa và hiểu biết sâu về cả y học lẫn pháp luật.",
            "context": "법원 재판, 의료분쟁 상담, 소송 준비 단계에서 사용",
            "culturalNote": "한국은 의료소송 승소율이 20-30%로 낮고 입증책임이 환자에게 있어 소송이 어렵습니다. 베트남은 의료기관의 설명책임이 더 강하지만, 법원의 의료전문성이 부족하여 감정결과에 크게 의존합니다. 한국은 의료분쟁조정중재원 제도가 있어 소송 전 조정이 활성화되어 있으나, 베트남은 이런 제도가 미비합니다.",
            "commonMistakes": [
                {
                    "mistake": "'tranh chấp y khoa'로 번역",
                    "correction": "'kiện y khoa' 사용",
                    "explanation": "'tranh chấp'은 분쟁 일반을 의미하고, 'kiện'은 법원에 제소한 소송을 의미함"
                },
                {
                    "mistake": "민사소송과 형사소송을 구분 없이 'kiện'으로만 표현",
                    "correction": "'kiện dân sự'(민사)와 'kiện hình sự'(형사) 명확히 구분",
                    "explanation": "법적 절차와 결과가 완전히 다르므로 반드시 구분해야 함"
                },
                {
                    "mistake": "'khởi kiện'과 'kiện'을 혼용",
                    "correction": "제소 행위는 'khởi kiện', 진행 중인 소송은 'kiện'",
                    "explanation": "소송의 단계에 따라 용어가 다름"
                }
            ],
            "examples": [
                {
                    "ko": "유족은 의료과실을 이유로 병원을 상대로 의료소송을 제기했습니다.",
                    "vi": "Gia đình nạn nhân đã khởi kiện y khoa đối với bệnh viện với lý do lỗi y khoa.",
                    "situation": "formal"
                },
                {
                    "ko": "의료소송에서는 전문 감정인의 의견이 판결에 큰 영향을 미칩니다.",
                    "vi": "Trong kiện y khoa, ý kiến của chuyên gia giám định có ảnh hưởng lớn đến phán quyết.",
                    "situation": "formal"
                },
                {
                    "ko": "의료소송은 입증이 어려워 환자 측 승소율이 낮습니다.",
                    "vi": "Kiện y khoa rất khó chứng minh nên tỷ lệ thắng kiện của bệnh nhân thấp.",
                    "situation": "informal"
                }
            ],
            "relatedTerms": ["의료과실", "손해배상", "감정인", "의료분쟁조정"]
        },
        {
            "slug": "dong-y-thu",
            "korean": "동의서",
            "vietnamese": "Đồng ý thư",
            "hanja": "同意書",
            "hanjaReading": "同(한가지 동) 意(뜻 의) 書(글 서)",
            "pronunciation": "동의서",
            "meaningKo": "환자가 의료행위의 내용, 위험성, 대안 등에 대해 충분히 설명을 듣고 자발적으로 동의한다는 의사를 표시하는 문서입니다. 통역 시 '사전동의' 원칙이 중요하며, 베트남어로 'nguyên tắc đồng ý trước'로 표현합니다. 동의서는 단순한 형식적 서명이 아니라 충분한 설명(informed consent)을 전제로 하므로, 통역사는 의료진의 설명이 충분히 전달되었는지 확인해야 합니다. 수술, 마취, 특수검사 등에 필수이며, 미성년자나 의식불명 환자의 경우 법정대리인이나 보호자의 동의가 필요합니다.",
            "meaningVi": "Đồng ý thư là văn bản thể hiện ý chí tự nguyện của bệnh nhân đồng ý thực hiện hành vi y tế sau khi được giải thích đầy đủ về nội dung, rủi ro và phương án thay thế. Đây là nguyên tắc 'đồng ý có hiểu biết' (informed consent), không chỉ là chữ ký hình thức.",
            "context": "수술 전, 특수검사 전, 임상시험 참여 시 필수",
            "culturalNote": "한국은 의료법상 동의서 작성이 엄격하게 규정되어 있고, 설명의무 위반 시 의료진에게 책임이 있습니다. 베트남도 동의서 제도가 있지만 실무상 형식적인 경우가 많고, 가족 중심 문화로 인해 환자 본인보다 가족의 동의를 우선시하는 경향이 있습니다. 통역 시 환자 자기결정권과 가족 의사결정 문화의 차이를 이해해야 합니다.",
            "commonMistakes": [
                {
                    "mistake": "'giấy đồng ý'로 번역",
                    "correction": "'đồng ý thư' 또는 'phiếu đồng ý' 사용",
                    "explanation": "'giấy'는 너무 일반적이고, 의료 맥락에서는 'đồng ý thư'가 표준 용어"
                },
                {
                    "mistake": "informed consent를 단순히 'đồng ý'로만 번역",
                    "correction": "'đồng ý có hiểu biết' 또는 'đồng ý sau khi được giải thích đầy đủ'",
                    "explanation": "설명을 전제로 한 동의라는 개념을 명확히 해야 함"
                },
                {
                    "mistake": "동의서와 승낙서를 구분 없이 번역",
                    "correction": "의료행위는 'đồng ý thư', 일반 승낙은 'giấy chấp thuận'",
                    "explanation": "의료 맥락의 동의는 특별한 법적 의미가 있음"
                }
            ],
            "examples": [
                {
                    "ko": "수술 전에 환자와 보호자에게 동의서를 받아야 합니다.",
                    "vi": "Trước phẫu thuật cần xin đồng ý thư của bệnh nhân và người nhà.",
                    "situation": "onsite"
                },
                {
                    "ko": "의사는 동의서를 받기 전에 충분한 설명을 해야 합니다.",
                    "vi": "Bác sĩ phải giải thích đầy đủ trước khi xin đồng ý thư.",
                    "situation": "formal"
                },
                {
                    "ko": "환자가 동의서에 서명을 거부하여 수술이 연기되었습니다.",
                    "vi": "Bệnh nhân từ chối ký đồng ý thư nên phẫu thuật bị hoãn.",
                    "situation": "informal"
                }
            ],
            "relatedTerms": ["설명의무", "자기결정권", "법정대리인", "사전동의"]
        },
        {
            "slug": "ho-so-benh-an",
            "korean": "진료기록",
            "vietnamese": "Hồ sơ bệnh án",
            "hanja": "診療記錄",
            "hanjaReading": "診(진찰 진) 療(치료 료) 記(기록 기) 錄(기록 록)",
            "pronunciation": "진료기록",
            "meaningKo": "의사가 환자의 진찰, 검사, 치료 등 의료행위 전반을 기록한 문서로, 법적으로 중요한 증거자료입니다. 통역 시 '차트' 또는 '의무기록'으로도 불리며, 베트남어로는 'hồ sơ bệnh án' 또는 'bệnh án'으로 표현합니다. 진료기록은 의료법상 일정 기간 보관의무가 있고, 환자는 열람 및 사본 발급을 요청할 권리가 있습니다. 의료분쟁 시 가장 중요한 증거가 되므로 정확하고 상세한 기록이 필수이며, 사후 수정 시 날짜와 이유를 명시해야 합니다.",
            "meaningVi": "Hồ sơ bệnh án là tài liệu ghi chép toàn bộ quá trình khám, xét nghiệm, điều trị của bệnh nhân do bác sĩ thực hiện, là bằng chứng pháp lý quan trọng. Theo pháp luật, cơ sở y tế phải lưu trữ trong thời gian quy định và bệnh nhân có quyền xem và sao chụp hồ sơ.",
            "context": "의료분쟁, 보험 청구, 진료 연속성 확보 시 사용",
            "culturalNote": "한국은 전자의무기록(EMR) 시스템이 잘 구축되어 있고, 진료기록 보관 및 열람 제도가 체계적입니다. 베트남도 대형 병원은 전산화되어 있지만 소규모 의료기관은 종이 기록이 많고, 환자의 진료기록 접근권이 실무상 제한적인 경우가 있습니다. 통역 시 양국의 의무기록 관리 수준 차이를 이해해야 합니다.",
            "commonMistakes": [
                {
                    "mistake": "'lý lịch bệnh'으로 번역",
                    "correction": "'hồ sơ bệnh án' 사용",
                    "explanation": "'lý lịch bệnh'은 병력을 의미하고, 'hồ sơ bệnh án'은 공식 진료기록 문서를 의미"
                },
                {
                    "mistake": "차트를 'biểu đồ'로 번역",
                    "correction": "의료 맥락에서 차트는 'bệnh án' 또는 'hồ sơ y tế'",
                    "explanation": "'biểu đồ'는 그래프를 의미하여 의료기록과는 다름"
                },
                {
                    "mistake": "'기록'과 '기록부'를 구분 없이 번역",
                    "correction": "개별 기록은 'ghi chép', 전체 기록부는 'hồ sơ'",
                    "explanation": "단위와 전체를 구분해야 의미가 명확함"
                }
            ],
            "examples": [
                {
                    "ko": "의료분쟁 발생 시 진료기록이 가장 중요한 증거가 됩니다.",
                    "vi": "Khi xảy ra tranh chấp y tế, hồ sơ bệnh án là bằng chứng quan trọng nhất.",
                    "situation": "formal"
                },
                {
                    "ko": "환자는 본인의 진료기록 사본을 요청할 권리가 있습니다.",
                    "vi": "Bệnh nhân có quyền yêu cầu sao chụp hồ sơ bệnh án của mình.",
                    "situation": "formal"
                },
                {
                    "ko": "진료기록을 사후에 수정할 경우 반드시 날짜와 이유를 기재해야 합니다.",
                    "vi": "Khi sửa đổi hồ sơ bệnh án sau này, phải ghi rõ ngày và lý do.",
                    "situation": "onsite"
                }
            ],
            "relatedTerms": ["의무기록", "전자의무기록", "기록열람권", "증거보전"]
        },
        {
            "slug": "tai-nan-y-khoa",
            "korean": "의료사고",
            "vietnamese": "Tai nạn y khoa",
            "hanja": "醫療事故",
            "hanjaReading": "醫(의원 의) 療(치료 료) 事(일 사) 故(연고 고)",
            "pronunciation": "이료사고",
            "meaningKo": "의료행위 과정에서 환자에게 예상하지 못한 나쁜 결과가 발생한 것으로, 의료인의 과실 유무와 무관하게 발생한 모든 사고를 포함합니다. 통역 시 '의료과실'과 구분해야 하며, 의료사고는 과실이 없어도 발생할 수 있는 합병증이나 부작용을 포함합니다. 베트남어로 'tai nạn y khoa'는 사고 일반을, 'biến chứng'은 합병증을 의미하므로 맥락에 따라 구분해야 합니다. 의료사고가 발생하면 원인 조사, 환자 및 가족 설명, 재발 방지 대책 수립이 필요하며, 과실이 인정되면 의료과실로 법적 책임이 발생합니다.",
            "meaningVi": "Tai nạn y khoa là kết quả xấu không lường trước xảy ra trong quá trình khám chữa bệnh, bao gồm tất cả sự cố bất kể có lỗi của nhân viên y tế hay không. Khác với 'lỗi y khoa', tai nạn y khoa có thể bao gồm biến chứng hoặc tác dụng phụ không do lỗi gây ra.",
            "context": "병원 안전관리, 사고 보고, 환자 설명 시 사용",
            "culturalNote": "한국은 의료사고 발생 시 자체 보고 및 조사 시스템이 구축되어 있고, 의료분쟁조정중재원을 통한 분쟁 해결이 가능합니다. 베트남은 의료사고 보고 체계가 미흡하고, 사고 발생 시 병원과 환자 간 직접 협상이나 소송으로 가는 경우가 많습니다. 통역 시 사고와 과실의 차이를 명확히 하여 불필요한 오해를 방지해야 합니다.",
            "commonMistakes": [
                {
                    "mistake": "의료사고와 의료과실을 동일하게 'lỗi y khoa'로 번역",
                    "correction": "의료사고는 'tai nạn y khoa', 의료과실은 'lỗi y khoa'",
                    "explanation": "사고는 과실 없이도 발생 가능하지만, 과실은 주의의무 위반이 필요함"
                },
                {
                    "mistake": "합병증을 'tai nạn'으로 번역",
                    "correction": "합병증은 'biến chứng', 사고는 'tai nạn'",
                    "explanation": "합병증은 의학적으로 예측 가능한 결과이고, 사고는 예기치 않은 사건"
                },
                {
                    "mistake": "'sự cố y tế'와 'tai nạn y khoa'를 혼용",
                    "correction": "경미한 사건은 'sự cố', 중대한 사고는 'tai nạn'",
                    "explanation": "심각도에 따라 용어가 다름"
                }
            ],
            "examples": [
                {
                    "ko": "의료사고가 발생했지만 의사의 과실은 인정되지 않았습니다.",
                    "vi": "Tai nạn y khoa đã xảy ra nhưng không công nhận lỗi của bác sĩ.",
                    "situation": "formal"
                },
                {
                    "ko": "병원은 의료사고 예방을 위해 안전 시스템을 강화했습니다.",
                    "vi": "Bệnh viện đã tăng cường hệ thống an toàn để phòng ngừa tai nạn y khoa.",
                    "situation": "formal"
                },
                {
                    "ko": "이 환자는 의료사고로 인한 합병증으로 추가 치료가 필요합니다.",
                    "vi": "Bệnh nhân này cần điều trị thêm do biến chứng từ tai nạn y khoa.",
                    "situation": "onsite"
                }
            ],
            "relatedTerms": ["의료과실", "합병증", "부작용", "환자안전"]
        },
        {
            "slug": "boi-thuong-thiet-hai",
            "korean": "손해배상",
            "vietnamese": "Bồi thường thiệt hại",
            "hanja": "損害賠償",
            "hanjaReading": "損(덜 손) 害(해칠 해) 賠(갚을 배) 償(갚을 상)",
            "pronunciation": "손해배상",
            "meaningKo": "위법행위로 타인에게 손해를 입힌 자가 그 손해를 금전으로 보상하는 것을 말합니다. 통역 시 재산상 손해와 정신적 손해(위자료)를 구분해야 하며, 베트남어로 각각 'thiệt hại vật chất'과 'thiệt hại tinh thần'으로 표현합니다. 의료분쟁에서는 치료비, 간병비, 상실 수익 등 재산상 손해와 함께 정신적 고통에 대한 위자료가 청구됩니다. 손해배상액 산정은 복잡하며, 과실 비율, 손해 범위, 인과관계 등을 종합적으로 고려합니다. 통역사는 손해 항목별 용어를 정확히 전달해야 합니다.",
            "meaningVi": "Bồi thường thiệt hại là việc người gây ra thiệt hại cho người khác do hành vi vi phạm pháp luật phải bồi hoàn bằng tiền. Trong tranh chấp y tế, bao gồm thiệt hại vật chất (chi phí điều trị, tiền công chăm sóc, thu nhập bị mất) và thiệt hại tinh thần (đau khổ về tinh thần).",
            "context": "의료소송, 보험 청구, 합의 협상 시 사용",
            "culturalNote": "한국은 손해배상액이 실제 손해에 기반하여 비교적 보수적으로 산정되고, 위자료는 별도로 청구됩니다. 베트남도 유사하지만 전반적으로 배상액 수준이 한국보다 낮은 편입니다. 한국은 상실 수익 계산 시 호프만 방식을 사용하지만, 베트남은 단순 계산 방식을 주로 사용합니다. 통역 시 양국의 배상액 산정 방식 차이를 이해해야 합니다.",
            "commonMistakes": [
                {
                    "mistake": "'đền bù'로 번역",
                    "correction": "'bồi thường' 사용",
                    "explanation": "'đền bù'는 일반 보상을, 'bồi thường'는 법적 손해배상을 의미"
                },
                {
                    "mistake": "위자료와 손해배상을 구분 없이 번역",
                    "correction": "재산상 손해는 'bồi thường thiệt hại vật chất', 위자료는 'bồi thường thiệt hại tinh thần'",
                    "explanation": "손해의 종류에 따라 법적 처리가 다름"
                },
                {
                    "mistake": "'배상금'을 'tiền phạt'로 번역",
                    "correction": "'tiền bồi thường' 사용",
                    "explanation": "'tiền phạt'는 벌금이고, 'tiền bồi thường'는 배상금"
                }
            ],
            "examples": [
                {
                    "ko": "법원은 피고에게 1억 원의 손해배상을 명령했습니다.",
                    "vi": "Tòa án đã ra lệnh bị cáo bồi thường thiệt hại 100 triệu won.",
                    "situation": "formal"
                },
                {
                    "ko": "손해배상액에는 치료비와 위자료가 포함됩니다.",
                    "vi": "Tiền bồi thường thiệt hại bao gồm chi phí điều trị và bồi thường tinh thần.",
                    "situation": "formal"
                },
                {
                    "ko": "환자 측은 5천만 원의 손해배상을 요구하고 있습니다.",
                    "vi": "Phía bệnh nhân đang yêu cầu bồi thường thiệt hại 50 triệu won.",
                    "situation": "informal"
                }
            ],
            "relatedTerms": ["위자료", "재산상손해", "일실이익", "과실상계"]
        },
        {
            "slug": "giam-dinh-y-khoa",
            "korean": "감정의뢰",
            "vietnamese": "Giám định y khoa",
            "hanja": "鑑定依賴",
            "hanjaReading": "鑑(거울 감) 定(정할 정) 依(의지 의) 賴(의뢰 뢰)",
            "pronunciation": "감정의뢰",
            "meaningKo": "의료분쟁에서 전문적인 의학 지식이 필요한 사항에 대해 전문가에게 의견을 구하는 것을 말합니다. 통역 시 '감정'은 전문가의 판단을, '감정의뢰'는 판단을 요청하는 행위를 의미하며, 베트남어로 각각 'giám định'과 'yêu cầu giám định'으로 표현합니다. 법원 또는 조정기관이 의료과실 여부, 인과관계, 장해 정도 등을 판단하기 위해 의료 전문가에게 감정을 의뢰하며, 감정 결과는 판결에 결정적 영향을 미칩니다. 통역사는 감정 질문과 답변을 정확히 전달해야 하며, 의학적 전문성과 법적 의미를 모두 이해해야 합니다.",
            "meaningVi": "Giám định y khoa là việc yêu cầu chuyên gia đưa ra ý kiến về các vấn đề cần kiến thức y học chuyên môn trong tranh chấp y tế. Tòa án hoặc cơ quan hòa giải yêu cầu chuyên gia y tế giám định về lỗi y khoa, quan hệ nhân quả, mức độ thương tật, và kết quả giám định có ảnh hưởng quyết định đến phán quyết.",
            "context": "의료소송, 조정 절차, 손해배상 산정 시 사용",
            "culturalNote": "한국은 대한의사협회, 대한의학회 등 공신력 있는 기관의 감정이 중요하고, 법원이 감정인을 선정합니다. 베트남은 보건부 산하 감정기관이나 대학병원 전문의가 감정을 수행하며, 감정 절차가 한국보다 덜 체계화되어 있습니다. 통역 시 양국의 감정 시스템과 절차 차이를 이해하고, 감정서의 법적 중요성을 설명해야 합니다.",
            "commonMistakes": [
                {
                    "mistake": "'khám nghiệm'으로 번역",
                    "correction": "'giám định' 사용",
                    "explanation": "'khám nghiệm'은 검시를 의미하고, 'giám định'은 전문가 감정을 의미"
                },
                {
                    "mistake": "감정과 검사를 구분 없이 번역",
                    "correction": "의료검사는 'xét nghiệm', 전문가 감정은 'giám định'",
                    "explanation": "검사는 진단 목적, 감정은 법적 판단 목적"
                },
                {
                    "mistake": "'감정서'를 'báo cáo'로만 번역",
                    "correction": "'giám định thư' 또는 'kết quả giám định'",
                    "explanation": "법적 효력이 있는 공식 문서임을 명확히 해야 함"
                }
            ],
            "examples": [
                {
                    "ko": "법원은 의료과실 여부를 판단하기 위해 전문가에게 감정을 의뢰했습니다.",
                    "vi": "Tòa án đã yêu cầu chuyên gia giám định để xác định có lỗi y khoa hay không.",
                    "situation": "formal"
                },
                {
                    "ko": "감정 결과 의사의 처치에는 문제가 없었다고 결론이 났습니다.",
                    "vi": "Kết quả giám định kết luận rằng không có vấn đề với cách xử trí của bác sĩ.",
                    "situation": "formal"
                },
                {
                    "ko": "감정의뢰에는 보통 2~3개월이 소요됩니다.",
                    "vi": "Giám định y khoa thường mất khoảng 2-3 tháng.",
                    "situation": "informal"
                }
            ],
            "relatedTerms": ["감정인", "감정서", "전문가증언", "의학적소견"]
        },
        {
            "slug": "dao-duc-y-khoa",
            "korean": "의료윤리",
            "vietnamese": "Đạo đức y khoa",
            "hanja": "醫療倫理",
            "hanjaReading": "醫(의원 의) 療(치료 료) 倫(인륜 륜) 理(다스릴 리)",
            "pronunciation": "이료윤리",
            "meaningKo": "의료인이 환자를 진료하고 의료 행위를 할 때 지켜야 할 도덕적 원칙과 행동 규범을 말합니다. 통역 시 자율성 존중, 악행 금지, 선행, 정의의 4대 원칙이 중요하며, 베트남어로 각각 'tôn trọng quyền tự chủ', 'không gây hại', 'làm lợi', 'công bằng'으로 표현합니다. 의료윤리는 법적 의무는 아니지만 의료인의 전문직 윤리로서 위반 시 징계나 면허 취소 사유가 될 수 있습니다. 통역사는 생명윤리, 환자 권리, 비밀 보장 등 윤리적 쟁점을 정확히 전달해야 하며, 특히 문화적 차이로 인한 윤리적 갈등 상황을 중재할 수 있어야 합니다.",
            "meaningVi": "Đạo đức y khoa là nguyên tắc đạo đức và chuẩn mực hành vi mà nhân viên y tế phải tuân thủ khi khám chữa bệnh. Bốn nguyên tắc cơ bản bao gồm tôn trọng quyền tự chủ, không gây hại, làm lợi cho bệnh nhân, và công bằng. Đây không phải nghĩa vụ pháp lý nhưng là đạo đức nghề nghiệp, vi phạm có thể dẫn đến kỷ luật hoặc thu hồi giấy phép hành nghề.",
            "context": "의료 교육, 임상윤리위원회, 의료분쟁 조정 시 사용",
            "culturalNote": "한국은 생명윤리법, 의료윤리 강령 등이 체계화되어 있고, 대형 병원에는 임상윤리위원회가 설치되어 있습니다. 베트남도 의료윤리 규범이 있지만 실무 적용이 한국보다 덜 엄격하고, 가족 중심 문화로 인해 환자 자율성보다 가족 결정을 우선하는 경향이 있습니다. 통역 시 환자 중심 윤리와 가족 중심 문화의 차이를 이해하고, 문화적으로 민감한 윤리 문제를 신중히 다뤄야 합니다.",
            "commonMistakes": [
                {
                    "mistake": "'đạo đức nghề nghiệp'으로 번역",
                    "correction": "'đạo đức y khoa' 사용",
                    "explanation": "'nghề nghiệp'은 일반 직업윤리이고, 'y khoa'는 의료 전문 윤리"
                },
                {
                    "mistake": "법과 윤리를 구분 없이 'pháp luật'로 번역",
                    "correction": "법은 'pháp luật', 윤리는 'đạo đức'",
                    "explanation": "법적 의무와 윤리적 의무는 성격이 다름"
                },
                {
                    "mistake": "비밀 보장을 단순히 'bảo mật'로 번역",
                    "correction": "의료 맥락에서 'bảo mật thông tin bệnh nhân' 또는 'giữ bí mật y tế'",
                    "explanation": "환자 정보 보호라는 특수성을 명확히 해야 함"
                }
            ],
            "examples": [
                {
                    "ko": "의사는 의료윤리에 따라 환자의 비밀을 보장해야 합니다.",
                    "vi": "Bác sĩ phải bảo mật thông tin bệnh nhân theo đạo đức y khoa.",
                    "situation": "formal"
                },
                {
                    "ko": "이 사안은 의료윤리위원회에서 검토할 필요가 있습니다.",
                    "vi": "Vấn đề này cần xem xét tại hội đồng đạo đức y khoa.",
                    "situation": "formal"
                },
                {
                    "ko": "의료윤리는 법적 의무는 아니지만 의료인의 기본 책무입니다.",
                    "vi": "Đạo đức y khoa không phải nghĩa vụ pháp lý nhưng là trách nhiệm cơ bản của nhân viên y tế.",
                    "situation": "informal"
                }
            ],
            "relatedTerms": ["생명윤리", "환자권리", "비밀보장", "자기결정권"]
        },
        {
            "slug": "quyen-benh-nhan",
            "korean": "환자권리",
            "vietnamese": "Quyền bệnh nhân",
            "hanja": "患者權利",
            "hanjaReading": "患(근심 환) 者(사람 자) 權(권세 권) 利(이로울 리)",
            "pronunciation": "환자권리",
            "meaningKo": "환자가 의료서비스를 받는 과정에서 인간으로서 존엄과 가치를 인정받고 보호받을 수 있는 권리를 말합니다. 통역 시 알 권리, 자기결정권, 비밀보장권, 진료거부 금지 등이 핵심이며, 베트남어로 각각 'quyền được biết', 'quyền tự quyết định', 'quyền bảo mật', 'cấm từ chối khám chữa bệnh'으로 표현합니다. 환자권리는 의료법과 환자안전법에 명시되어 있으며, 의료기관은 환자권리장전을 게시하고 환자에게 고지해야 합니다. 통역사는 환자가 자신의 권리를 충분히 이해하고 행사할 수 있도록 정확한 정보를 전달해야 하며, 문화적 차이로 인한 권리 인식의 차이를 좁혀야 합니다.",
            "meaningVi": "Quyền bệnh nhân là quyền được công nhận và bảo vệ phẩm giá, giá trị con người trong quá trình tiếp nhận dịch vụ y tế. Các quyền cốt lõi bao gồm quyền được biết thông tin, quyền tự quyết định điều trị, quyền bảo mật thông tin cá nhân, và quyền không bị từ chối khám chữa bệnh. Quyền này được quy định trong luật y tế.",
            "context": "환자 상담, 의료분쟁, 동의서 설명 시 사용",
            "culturalNote": "한국은 환자권리장전이 법제화되어 있고 환자 중심 의료가 강조됩니다. 베트남도 환자 권리 규정이 있지만 실무상 의료진 중심 문화가 강하고, 환자가 적극적으로 권리를 주장하는 경우가 드뭅니다. 한국은 의료소비자로서 환자의 선택권이 강조되지만, 베트남은 의사의 권위를 존중하는 문화가 강합니다. 통역 시 양국의 의료 문화 차이를 이해하고, 환자가 권리를 인식하도록 도와야 합니다.",
            "commonMistakes": [
                {
                    "mistake": "'quyền lợi bệnh nhân'으로 번역",
                    "correction": "'quyền bệnh nhân' 사용",
                    "explanation": "'quyền lợi'는 이익을 의미하고, 'quyền'은 권리를 의미하여 법적 개념이 다름"
                },
                {
                    "mistake": "알 권리를 단순히 'quyền biết'로 번역",
                    "correction": "'quyền được biết thông tin' 또는 'quyền được cung cấp thông tin'",
                    "explanation": "정보 제공받을 권리라는 의미를 명확히 해야 함"
                },
                {
                    "mistake": "자기결정권을 'quyền tự do'로 번역",
                    "correction": "'quyền tự quyết định'",
                    "explanation": "'tự do'는 일반적 자유이고, 'tự quyết định'은 자기결정권"
                }
            ],
            "examples": [
                {
                    "ko": "환자는 자신의 병명과 치료 방법에 대해 알 권리가 있습니다.",
                    "vi": "Bệnh nhân có quyền được biết về chẩn đoán và phương pháp điều trị của mình.",
                    "situation": "formal"
                },
                {
                    "ko": "환자권리장전에는 치료 거부권도 포함되어 있습니다.",
                    "vi": "Tuyên ngôn quyền bệnh nhân cũng bao gồm quyền từ chối điều trị.",
                    "situation": "formal"
                },
                {
                    "ko": "환자권리 존중은 의료윤리의 기본입니다.",
                    "vi": "Tôn trọng quyền bệnh nhân là nền tảng của đạo đức y khoa.",
                    "situation": "informal"
                }
            ],
            "relatedTerms": ["알권리", "자기결정권", "비밀보장권", "진료거부금지"]
        },
        {
            "slug": "hoa-giai-tranh-chap-y-khoa",
            "korean": "의료중재",
            "vietnamese": "Hòa giải tranh chấp y khoa",
            "hanja": "醫療仲裁",
            "hanjaReading": "醫(의원 의) 療(치료 료) 仲(가운데 중) 裁(재단 재)",
            "pronunciation": "이료중재",
            "meaningKo": "의료분쟁을 법원 소송이 아닌 제3자의 중재를 통해 해결하는 절차를 말합니다. 통역 시 '조정'과 '중재'를 구분해야 하며, 조정은 합의 권유(hòa giải), 중재는 구속력 있는 판정(trọng tài)을 의미합니다. 한국은 의료분쟁조정중재원을 통해 조정과 중재가 가능하며, 소송보다 신속하고 비용이 적게 듭니다. 베트남은 유사한 전문 기관이 없어 법원 소송으로 가는 경우가 많습니다. 통역사는 조정 절차, 비용, 기간, 효력 등을 정확히 설명하여 당사자가 분쟁 해결 방법을 선택할 수 있도록 도와야 합니다.",
            "meaningVi": "Hòa giải tranh chấp y khoa là thủ tục giải quyết tranh chấp y tế thông qua sự can thiệp của bên thứ ba thay vì kiện tụng tại tòa án. Cần phân biệt 'hòa giải' (khuyến khích thỏa thuận) và 'trọng tài' (phán quyết có tính ràng buộc). Ở Hàn Quốc có Trung tâm Hòa giải và Trọng tài Tranh chấp Y tế, nhanh hơn và ít tốn kém hơn kiện tụng.",
            "context": "의료분쟁 발생 시, 소송 전 단계, 합의 협상 시 사용",
            "culturalNote": "한국은 2012년부터 의료분쟁조정중재원이 운영되어 소송 외 분쟁 해결이 활성화되었고, 조정 성립률이 약 70%에 달합니다. 베트남은 이런 전문 기관이 없어 병원과 환자 간 직접 협상이나 법원 소송에 의존하며, 협상 문화도 한국과 다릅니다. 통역 시 한국의 중재 제도를 설명하고, 베트남 환자가 이를 활용할 수 있도록 안내해야 합니다.",
            "commonMistakes": [
                {
                    "mistake": "'hòa giải'와 'trọng tài'를 구분 없이 사용",
                    "correction": "조정은 'hòa giải', 중재는 'trọng tài'",
                    "explanation": "조정은 합의 유도, 중재는 구속력 있는 판정으로 성격이 다름"
                },
                {
                    "mistake": "중재원을 단순히 'trung tâm'으로만 번역",
                    "correction": "'Trung tâm Hòa giải và Trọng tài Tranh chấp Y tế'",
                    "explanation": "공식 명칭을 정확히 사용해야 함"
                },
                {
                    "mistake": "협상을 'đàm phán'으로 번역",
                    "correction": "법적 맥락에서는 'thương lượng' 또는 'hòa giải'",
                    "explanation": "'đàm phán'은 일반 협상이고, 법적 분쟁은 'thương lượng' 또는 'hòa giải'"
                }
            ],
            "examples": [
                {
                    "ko": "의료분쟁조정중재원을 통해 조정을 신청할 수 있습니다.",
                    "vi": "Có thể nộp đơn hòa giải thông qua Trung tâm Hòa giải và Trọng tài Tranh chấp Y tế.",
                    "situation": "formal"
                },
                {
                    "ko": "의료중재는 소송보다 빠르고 비용이 적게 듭니다.",
                    "vi": "Hòa giải tranh chấp y khoa nhanh hơn và ít tốn kém hơn kiện tụng.",
                    "situation": "formal"
                },
                {
                    "ko": "양측이 조정안에 합의하면 재판상 화해와 같은 효력이 있습니다.",
                    "vi": "Nếu hai bên đồng ý với phương án hòa giải, có hiệu lực như hòa giải tại tòa.",
                    "situation": "informal"
                }
            ],
            "relatedTerms": ["의료분쟁조정", "조정신청", "중재판정", "합의권고"]
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
