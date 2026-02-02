#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Add final 10 medical terms to medical.json (Part 3)
Focus: Medical documents, Medical procedures
"""

import json
import os

# Use relative path from script location
file_path = os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', 'data', 'terms', 'medical.json')

new_terms_part3 = [
    {
        "slug": "giay-dong-y-phau-thuat",
        "korean": "수술동의서",
        "vietnamese": "giấy đồng ý phẫu thuật",
        "hanja": "手術同意書",
        "hanjaReading": "수(손 수) + 술(기술 술) + 동(같을 동) + 의(뜻 의) + 서(글 서)",
        "pronunciation": "susul-donguiseo",
        "meaningKo": "수술을 시행하기 전에 의사가 환자에게 수술의 목적, 방법, 예상되는 결과, 위험성, 합병증, 대안적 치료법 등을 충분히 설명하고 환자의 자발적 동의를 받는 법적 문서입니다. 수술은 침습적 치료로 위험이 수반되므로, 사전동의 중에서도 특히 중요하며 서면 동의가 법적으로 필수입니다. 통역 시 주의할 점은 환자가 수술의 위험성과 합병증을 정확히 이해하고, 질문할 기회를 충분히 가진 후 자발적으로 동의하도록 해야 합니다. 외국인 환자는 언어 장벽과 문화적 차이로 내용을 제대로 이해하지 못한 채 형식적으로 서명하는 경우가 많아, 통역사는 환자 보호를 위해 더욱 신중하고 상세하게 설명해야 합니다.",
        "meaningVi": "Văn bản pháp lý nhận được sự đồng ý tự nguyện của bệnh nhân sau khi bác sĩ giải thích đầy đủ về mục đích, phương pháp, kết quả dự kiến, rủi ro, biến chứng, phương pháp điều trị thay thế trước khi tiến hành phẫu thuật. Phẫu thuật là điều trị xâm lấn có rủi ro nên đặc biệt quan trọng trong đồng ý trước và đồng ý bằng văn bản là bắt buộc theo luật.",
        "context": "수술 준비, 환자 권리, 의료 안전",
        "culturalNote": "한국은 수술 동의 절차가 매우 엄격하지만, 베트남에서는 가족이 환자를 대신하여 결정하거나, 의사가 설명하면 환자가 거의 반대하지 않는 문화가 있습니다. 외국인 환자가 수술동의서를 단순한 절차로 여기지 않도록, 이것이 환자 보호를 위한 중요한 권리 행사임을 강조해야 합니다.",
        "commonMistakes": [
            {
                "mistake": "수술동의서를 빨리 서명하도록 재촉",
                "correction": "환자가 완전히 이해하고 질문할 시간 충분히 제공 - 서두르지 않기",
                "explanation": "수술동의는 환자의 자율적 결정이 핵심이므로 시간 압박 금지"
            },
            {
                "mistake": "수술 위험을 축소하거나 생략하고 통역",
                "correction": "위험과 합병증을 정확히 통역 - 환자의 알 권리 보장",
                "explanation": "위험 정보 누락은 환자의 자기결정권 침해"
            },
            {
                "mistake": "가족이 대신 서명해도 된다고 안내",
                "correction": "환자 본인 서명 원칙 - 환자가 의식 없는 경우만 예외",
                "explanation": "한국 의료법은 환자 본인의 동의를 우선시"
            }
        ],
        "examples": [
            {
                "ko": "수술동의서는 환자분께서 수술 내용을 충분히 이해하신 후 서명하셔야 합니다.",
                "vi": "Giấy đồng ý phẫu thuật phải ký sau khi bệnh nhân hiểu đầy đủ nội dung phẫu thuật.",
                "situation": "formal"
            },
            {
                "ko": "수술의 위험과 합병증에 대해 설명드렸습니다. 질문 있으신가요?",
                "vi": "Đã giải thích về rủi ro và biến chứng của phẫu thuật. Có câu hỏi gì không?",
                "situation": "onsite"
            },
            {
                "ko": "이해 안 되는 부분이 있으면 서명하기 전에 꼭 물어보세요.",
                "vi": "Nếu có phần nào không hiểu, nhất định hỏi trước khi ký.",
                "situation": "informal"
            }
        ],
        "relatedTerms": ["마취동의서", "사전동의", "수술"]
    },
    {
        "slug": "giay-dong-y-gay-me",
        "korean": "마취동의서",
        "vietnamese": "giấy đồng ý gây mê",
        "hanja": "麻醉同意書",
        "hanjaReading": "마(마비 마) + 취(취할 취) + 동(같을 동) + 의(뜻 의) + 서(글 서)",
        "pronunciation": "chwi-donguiseo",
        "meaningKo": "수술 시 마취를 시행하기 전에 마취과 의사가 환자에게 마취 방법(전신마취, 부위마취, 국소마취 등), 마취 중 관리, 마취 후 회복, 마취 관련 위험성 및 합병증 등을 설명하고 동의를 받는 법적 문서입니다. 마취는 수술과 별개로 독자적인 위험이 있으므로, 수술동의서와 별도로 마취동의서를 작성해야 합니다. 통역 시 주의할 점은 환자가 마취 전 금식, 복용 중인 약물 중단, 마취 후 회복 과정 등을 정확히 이해하도록 해야 하며, 특히 외국인 환자는 마취에 대한 막연한 두려움이 있을 수 있으므로 안심시키면서도 정확한 정보를 전달해야 합니다.",
        "meaningVi": "Văn bản pháp lý nhận được sự đồng ý sau khi bác sĩ gây mê giải thích cho bệnh nhân về phương pháp gây mê (gây mê toàn thân, gây tê vùng, gây tê tại chỗ), quản lý trong gây mê, hồi phục sau gây mê, rủi ro và biến chứng liên quan đến gây mê trước khi tiến hành gây mê cho phẫu thuật. Gây mê có rủi ro riêng độc lập với phẫu thuật nên phải lập giấy đồng ý riêng ngoài giấy đồng ý phẫu thuật.",
        "context": "마취 준비, 환자 안전, 수술 전 관리",
        "culturalNote": "베트남을 포함한 일부 국가에서는 마취를 수술의 일부로 여겨 별도 동의를 받지 않는 경우가 있지만, 한국은 마취를 독립적 의료 행위로 보아 별도 동의가 필수입니다. 외국인 환자가 이 차이를 이해하지 못해 번거롭게 여길 수 있으나, 환자 안전을 위한 것임을 설명해야 합니다.",
        "commonMistakes": [
            {
                "mistake": "마취동의서를 수술동의서의 일부로 설명",
                "correction": "마취와 수술은 별개의 의료 행위 - 각각 독립적 동의 필요",
                "explanation": "마취는 별도의 전문 영역이며 고유한 위험이 있음"
            },
            {
                "mistake": "마취 전 금식 지침을 형식적으로만 안내",
                "correction": "금식 시간과 이유를 구체적으로 설명 - 환자 안전과 직결",
                "explanation": "금식 미준수는 심각한 마취 합병증 유발 가능"
            },
            {
                "mistake": "환자의 마취에 대한 두려움을 무시",
                "correction": "두려움을 공감하고, 안전한 마취 관리 계획 설명하여 안심시킴",
                "explanation": "환자의 불안은 마취에 영향을 줄 수 있으므로 심리적 지지 중요"
            }
        ],
        "examples": [
            {
                "ko": "마취 전 8시간 금식이 필요합니다. 물도 마시면 안 됩니다.",
                "vi": "Cần nhịn ăn 8 tiếng trước gây mê. Không được uống nước.",
                "situation": "formal"
            },
            {
                "ko": "마취동의서는 수술동의서와 별개로 작성하셔야 합니다.",
                "vi": "Giấy đồng ý gây mê phải lập riêng ngoài giấy đồng ý phẫu thuật.",
                "situation": "onsite"
            },
            {
                "ko": "마취는 안전하게 관리되니 너무 걱정하지 마세요.",
                "vi": "Gây mê được quản lý an toàn nên đừng quá lo lắng.",
                "situation": "informal"
            }
        ],
        "relatedTerms": ["수술동의서", "전신마취", "마취과"]
    },
    {
        "slug": "thu-tuc-nhap-xuat-vien",
        "korean": "입퇴원수속",
        "vietnamese": "thủ tục nhập xuất viện",
        "hanja": "入退院手續",
        "hanjaReading": "입(들 입) + 퇴(물러날 퇴) + 원(집 원) + 수(손 수) + 속(이을 속)",
        "pronunciation": "iptoe won-susok",
        "meaningKo": "환자가 입원하거나 퇴원할 때 병원 원무과에서 진행하는 행정 절차로, 입원 시에는 신원 확인, 보험 확인, 입원 동의서 작성, 병실 배정 등이 이루어지고, 퇴원 시에는 진료비 정산, 퇴원 처방전 수령, 다음 진료 예약 등이 진행됩니다. 통역 시 주의할 점은 외국인 환자는 보험 종류(건강보험, 여행자보험, 자비 등)에 따라 절차와 필요 서류가 다르므로, 사전에 확인하고 준비하도록 안내해야 합니다. 또한 퇴원 시 미정산 진료비가 있으면 퇴원이 지연될 수 있으므로, 입원비 예치금과 추가 비용 가능성을 미리 안내하는 것이 분쟁 예방에 도움이 됩니다.",
        "meaningVi": "Thủ tục hành chính tiến hành tại phòng hành chính bệnh viện khi bệnh nhân nhập viện hoặc xuất viện. Khi nhập viện: xác minh danh tính, xác nhận bảo hiểm, viết giấy đồng ý nhập viện, phân phòng bệnh. Khi xuất viện: thanh toán viện phí, nhận đơn thuốc xuất viện, hẹn khám tiếp theo.",
        "context": "병원 이용, 행정 절차, 진료비 관리",
        "culturalNote": "한국 병원의 입퇴원 절차는 베트남보다 체계적이고 전산화되어 있지만, 외국인에게는 복잡하게 느껴질 수 있습니다. 특히 건강보험 적용 여부, 예치금 납부, 병실 등급 선택 등에서 혼란을 겪는 경우가 많으므로, 통역사가 절차를 단계별로 안내하는 것이 중요합니다.",
        "commonMistakes": [
            {
                "mistake": "입퇴원수속을 단순히 '등록'으로만 번역",
                "correction": "'thủ tục nhập xuất viện' + 필요 서류와 절차 구체적 안내",
                "explanation": "환자가 무엇을 준비해야 하는지 알 수 있도록 정보 제공 필요"
            },
            {
                "mistake": "예치금에 대해 사전 안내 없이 진행",
                "correction": "입원 시 예치금 필요성과 금액 미리 안내 - 환자가 준비할 수 있도록",
                "explanation": "갑작스러운 비용 요구는 환자에게 부담이 크고 분쟁 소지"
            },
            {
                "mistake": "외국인도 내국인과 동일한 절차라고만 설명",
                "correction": "외국인은 추가 서류(여권, 외국인등록증) 필요 - 사전 준비 안내",
                "explanation": "외국인 특유의 추가 요건을 안내하여 절차 지연 방지"
            }
        ],
        "examples": [
            {
                "ko": "입원 수속을 위해 건강보험증과 신분증을 준비해 주세요.",
                "vi": "Để làm thủ tục nhập viện, vui lòng chuẩn bị thẻ bảo hiểm y tế và giấy tờ tùy thân.",
                "situation": "formal"
            },
            {
                "ko": "입원 시 예치금 50만원이 필요합니다.",
                "vi": "Khi nhập viện cần đặt cọc 500,000 won.",
                "situation": "onsite"
            },
            {
                "ko": "퇴원 수속은 1층 원무과에서 하면 돼요.",
                "vi": "Thủ tục xuất viện làm ở phòng hành chính tầng 1.",
                "situation": "informal"
            }
        ],
        "relatedTerms": ["입원", "퇴원", "진료비영수증"]
    },
    {
        "slug": "hoa-don-vien-phi",
        "korean": "의료비영수증",
        "vietnamese": "hóa đơn viện phí",
        "hanja": "醫療費領收證",
        "hanjaReading": "의(의원 의) + 료(고칠 료) + 비(쓸 비) + 영(받을 영) + 수(받을 수) + 증(증거 증)",
        "pronunciation": "uiryobi-yeongsujeung",
        "meaningKo": "환자가 병원에서 진료를 받고 지불한 의료비의 내역과 금액을 증명하는 공식 문서로, 진료 날짜, 진료 항목, 금액, 본인부담금, 보험 적용 내역 등이 기재됩니다. 이 문서는 실손보험 청구, 의료비 세액공제, 회사 제출용 등 다양한 용도로 사용되므로 반드시 보관해야 합니다. 통역 시 주의할 점은 영수증과 진료비 세부산정내역서는 다른 문서이며, 실손보험 청구 시 두 문서가 모두 필요한 경우가 많다는 점입니다. 외국인 환자는 영수증의 중요성을 모르고 버리는 경우가 있으므로, 보관의 중요성을 강조해야 합니다.",
        "meaningVi": "Văn bản chính thức chứng minh nội dung và số tiền viện phí mà bệnh nhân đã thanh toán sau khi khám chữa bệnh tại bệnh viện, ghi chép ngày khám, hạng mục khám, số tiền, chi phí tự trả, nội dung áp dụng bảo hiểm. Văn bản này được sử dụng cho nhiều mục đích như yêu cầu bảo hiểm thực tế, giảm trừ thuế viện phí, nộp công ty nên phải bảo quản.",
        "context": "진료비 정산, 보험 청구, 세금 신고",
        "culturalNote": "한국은 의료비 관련 서류 관리가 엄격하여 영수증이 없으면 보험 청구나 세액공제를 받을 수 없지만, 베트남에서는 서류 관리가 상대적으로 느슨할 수 있습니다. 외국인 환자에게 영수증 보관의 중요성과 재발급의 어려움을 설명하여 분실을 예방해야 합니다.",
        "commonMistakes": [
            {
                "mistake": "영수증을 받았는지 확인하지 않음",
                "correction": "진료 후 반드시 영수증 수령 확인 - 환자에게 보관 안내",
                "explanation": "영수증 없으면 보험 청구나 증빙 불가"
            },
            {
                "mistake": "영수증과 세부산정내역서를 구분하지 않음",
                "correction": "영수증은 'hóa đơn', 세부산정내역서는 'bảng kê chi tiết' - 두 문서 모두 필요한 경우 있음",
                "explanation": "용도에 따라 필요한 서류가 다르므로 구분 필요"
            },
            {
                "mistake": "영수증 분실 시 쉽게 재발급 받을 수 있다고 안내",
                "correction": "재발급은 가능하나 절차가 번거롭고 시간 소요 - 원본 잘 보관하도록 강조",
                "explanation": "분실 예방이 최선"
            }
        ],
        "examples": [
            {
                "ko": "의료비 영수증은 실손보험 청구 시 필요하니 잘 보관하세요.",
                "vi": "Hóa đơn viện phí cần để yêu cầu bảo hiểm thực tế nên hãy giữ cẩn thận.",
                "situation": "formal"
            },
            {
                "ko": "영수증을 분실하시면 재발급에 시간이 걸립니다.",
                "vi": "Nếu mất hóa đơn, mất thời gian để cấp lại.",
                "situation": "onsite"
            },
            {
                "ko": "영수증 받으셨어요? 꼭 챙겨야 해요.",
                "vi": "Đã nhận hóa đơn chưa? Nhất định phải giữ.",
                "situation": "informal"
            }
        ],
        "relatedTerms": ["진료비세부산정내역", "실손보험", "본인부담금"]
    },
    {
        "slug": "yeu-cau-bao-hiem",
        "korean": "보험청구",
        "vietnamese": "yêu cầu bảo hiểm",
        "hanja": "保險請求",
        "hanjaReading": "보(지킬 보) + 험(험할 험) + 청(청할 청) + 구(구할 구)",
        "pronunciation": "boheom-cheonggu",
        "meaningKo": "환자가 의료비를 지불한 후, 가입한 보험(건강보험, 실손보험 등)에 필요한 서류를 제출하여 보험금을 받는 절차입니다. 건강보험은 병원에서 자동으로 청구하지만, 실손보험은 환자가 직접 보험사에 청구해야 합니다. 통역 시 주의할 점은 보험 청구에 필요한 서류(영수증, 진료비세부산정내역서, 진단서 등)와 청구 기한을 사전에 안내하여 환자가 보험금을 놓치지 않도록 해야 합니다. 외국인 환자는 한국 보험 시스템에 익숙하지 않아 청구를 놓치거나, 서류 미비로 보험금을 받지 못하는 경우가 많으므로, 통역사의 명확한 안내가 중요합니다.",
        "meaningVi": "Quy trình bệnh nhân nộp các giấy tờ cần thiết cho bảo hiểm đã tham gia (bảo hiểm y tế, bảo hiểm thực tế) để nhận tiền bảo hiểm sau khi thanh toán viện phí. Bảo hiểm y tế do bệnh viện tự động yêu cầu, còn bảo hiểm thực tế bệnh nhân phải tự yêu cầu đến công ty bảo hiểm.",
        "context": "의료비 환급, 보험 이용, 행정 절차",
        "culturalNote": "한국은 보험 청구 절차가 체계적이지만 복잡할 수 있어, 베트남 환자가 혼란스러워하는 경우가 많습니다. 특히 실손보험 청구는 보험사마다 요구 서류와 절차가 달라 통역사가 일일이 안내하기 어려우므로, 환자가 직접 보험사에 문의하도록 안내하는 것이 안전합니다.",
        "commonMistakes": [
            {
                "mistake": "건강보험과 실손보험 청구를 같은 것으로 설명",
                "correction": "건강보험은 병원이 자동 청구, 실손보험은 환자가 직접 청구 - 절차 구분",
                "explanation": "두 보험의 청구 주체와 방법이 다름"
            },
            {
                "mistake": "보험 청구 기한을 안내하지 않음",
                "correction": "보험마다 청구 기한이 다름 - 빨리 청구하도록 안내",
                "explanation": "기한 경과 시 보험금 청구 불가"
            },
            {
                "mistake": "통역사가 보험 청구를 대신 처리해줄 수 있다고 기대",
                "correction": "통역사는 정보 안내만 가능 - 청구는 환자 본인 또는 보험사와 직접 진행",
                "explanation": "통역사의 역할 범위 명확히 하여 오해 방지"
            }
        ],
        "examples": [
            {
                "ko": "실손보험 청구는 환자분께서 직접 보험사에 서류를 제출하셔야 합니다.",
                "vi": "Yêu cầu bảo hiểm thực tế, bệnh nhân phải tự nộp giấy tờ cho công ty bảo hiểm.",
                "situation": "formal"
            },
            {
                "ko": "보험 청구에 필요한 서류는 영수증과 진료비 세부내역서입니다.",
                "vi": "Giấy tờ cần để yêu cầu bảo hiểm là hóa đơn và bảng kê chi tiết viện phí.",
                "situation": "onsite"
            },
            {
                "ko": "보험사마다 청구 방법이 달라요. 직접 문의해보세요.",
                "vi": "Cách yêu cầu khác nhau tùy công ty bảo hiểm. Hãy liên hệ trực tiếp.",
                "situation": "informal"
            }
        ],
        "relatedTerms": ["실손보험", "의료비영수증", "진료비세부산정내역"]
    },
    {
        "slug": "bang-ke-chi-tiet-vien-phi",
        "korean": "진료비세부산정내역",
        "vietnamese": "bảng kê chi tiết viện phí",
        "hanja": "診療費細部算定內譯",
        "hanjaReading": "진(살필 진) + 료(고칠 료) + 비(쓸 비) + 세(가늘 세) + 부(부분 부) + 산(셈 산) + 정(정할 정) + 내(안 내) + 역(나눌 역)",
        "pronunciation": "jillyobi-sebu-sanjeong-naeyeok",
        "meaningKo": "환자가 받은 진료의 모든 항목(진찰료, 검사비, 약제비, 수술비, 입원료 등)과 각 항목의 세부 비용이 상세히 기재된 문서로, 진료비가 어떻게 산정되었는지 투명하게 확인할 수 있습니다. 건강보험 적용 내역과 비급여 내역이 구분되어 있어, 본인부담금의 근거를 알 수 있습니다. 통역 시 주의할 점은 이 문서는 실손보험 청구 시 거의 필수로 요구되며, 진료비 영수증과 함께 보관해야 한다는 점입니다. 외국인 환자는 복잡한 내역서를 이해하기 어려워하므로, 주요 항목과 비용을 쉽게 설명하는 것이 도움이 됩니다.",
        "meaningVi": "Văn bản ghi chép chi tiết tất cả các hạng mục khám chữa bệnh (phí khám, phí xét nghiệm, phí thuốc, phí phẫu thuật, phí nằm viện) và chi phí cụ thể của từng hạng mục mà bệnh nhân đã nhận, có thể xác minh minh bạch cách tính viện phí. Phân biệt nội dung áp dụng bảo hiểm y tế và nội dung không được bảo hiểm, biết căn cứ của chi phí tự trả.",
        "context": "진료비 투명성, 보험 청구, 환자 권리",
        "culturalNote": "한국은 의료비 산정이 투명하고 세부내역을 환자에게 제공하는 것이 의무이지만, 베트남에서는 이러한 상세한 내역서를 제공하지 않는 경우가 많습니다. 외국인 환자는 복잡한 내역서에 압도되거나, 반대로 세부내역을 요구하는 것을 당연한 권리로 인식하지 못할 수 있으므로, 통역사가 환자 권리를 안내해야 합니다.",
        "commonMistakes": [
            {
                "mistake": "세부산정내역서를 영수증과 같은 것으로 설명",
                "correction": "영수증은 총액, 세부산정내역서는 항목별 상세 내역 - 두 문서 모두 중요",
                "explanation": "용도가 다르므로 구분 필요"
            },
            {
                "mistake": "복잡한 의학 용어와 코드를 그대로 통역",
                "correction": "주요 항목(검사, 약, 수술 등)을 쉬운 말로 설명하고, 상세 내역은 필요시 확인",
                "explanation": "환자가 전체적인 비용 구조를 이해하도록 돕는 것이 목적"
            },
            {
                "mistake": "환자가 요청하지 않으면 세부내역서를 받지 않아도 된다고 안내",
                "correction": "실손보험 청구 시 필수 - 미리 받아두도록 안내",
                "explanation": "나중에 필요할 때 재발급 받으려면 번거로움"
            }
        ],
        "examples": [
            {
                "ko": "진료비 세부산정내역서는 실손보험 청구 시 필요하니 함께 받으세요.",
                "vi": "Bảng kê chi tiết viện phí cần khi yêu cầu bảo hiểm thực tế nên hãy nhận cùng.",
                "situation": "formal"
            },
            {
                "ko": "이 내역서에서 급여와 비급여 항목을 확인할 수 있습니다.",
                "vi": "Trong bảng kê này có thể xem các khoản được bảo hiểm và không được bảo hiểm.",
                "situation": "onsite"
            },
            {
                "ko": "내역서가 복잡해 보이지만, 주요 항목만 보면 이해하기 쉬워요.",
                "vi": "Bảng kê trông phức tạp nhưng nếu chỉ xem các mục chính thì dễ hiểu.",
                "situation": "informal"
            }
        ],
        "relatedTerms": ["의료비영수증", "실손보험", "본인부담금"]
    },
    {
        "slug": "cap-ban-sao-ho-so-benh-an",
        "korean": "의무기록사본발급",
        "vietnamese": "cấp bản sao hồ sơ bệnh án",
        "hanja": "醫務記錄寫本發給",
        "hanjaReading": "의(의원 의) + 무(일 무) + 기(기록할 기) + 록(기록할 록) + 사(베낄 사) + 본(근본 본) + 발(필 발) + 급(줄 급)",
        "pronunciation": "uimu-girok-sabon-balgeup",
        "meaningKo": "환자가 자신의 진료 기록 사본을 병원에 신청하여 발급받는 절차로, 환자는 본인의 의무기록을 열람하고 사본을 받을 법적 권리가 있습니다. 다른 병원 진료 시, 보험 청구, 법적 분쟁, 해외 이주 등 다양한 용도로 필요합니다. 통역 시 주의할 점은 의무기록 발급 시 환자 본인 확인이 엄격하며, 대리인이 신청할 경우 위임장과 신분증이 필요하다는 점입니다. 외국인 환자는 귀국 시 의무기록을 가져가고 싶어하는 경우가 많으므로, 발급 절차와 비용, 소요 시간을 미리 안내하는 것이 도움이 됩니다.",
        "meaningVi": "Quy trình bệnh nhân nộp đơn xin cấp bản sao hồ sơ khám chữa bệnh của mình tại bệnh viện. Bệnh nhân có quyền pháp lý được xem và nhận bản sao hồ sơ bệnh án của mình. Cần cho nhiều mục đích như khám bệnh viện khác, yêu cầu bảo hiểm, tranh chấp pháp lý, di cư nước ngoài.",
        "context": "환자 권리, 의료 정보, 행정 절차",
        "culturalNote": "한국은 환자의 의무기록 접근 권리가 법으로 보장되어 있지만, 베트남에서는 의무기록을 병원 소유로 여기는 경향이 있어 환자가 사본을 받기 어려운 경우가 있습니다. 외국인 환자에게 한국에서는 본인의 의무기록을 받을 권리가 있음을 알리고, 절차를 안내하는 것이 중요합니다.",
        "commonMistakes": [
            {
                "mistake": "의무기록을 누구나 쉽게 받을 수 있다고 안내",
                "correction": "본인 확인 엄격 - 신분증 필수, 대리인은 위임장 필요",
                "explanation": "개인정보 보호를 위한 엄격한 확인 절차"
            },
            {
                "mistake": "의무기록 발급이 무료라고 안내",
                "correction": "발급 비용 발생 - 페이지 수에 따라 비용 다름",
                "explanation": "예상치 못한 비용으로 환자 불만 방지"
            },
            {
                "mistake": "즉시 발급 가능하다고 안내",
                "correction": "발급까지 며칠 소요 가능 - 미리 신청하도록 안내",
                "explanation": "귀국 일정이 있는 외국인은 충분한 시간 확보 필요"
            }
        ],
        "examples": [
            {
                "ko": "의무기록 사본 발급은 원무과에 신청하시면 되고, 신분증이 필요합니다.",
                "vi": "Cấp bản sao hồ sơ bệnh án, nộp đơn tại phòng hành chính, cần giấy tờ tùy thân.",
                "situation": "formal"
            },
            {
                "ko": "의무기록 발급에는 며칠 걸릴 수 있으니 미리 신청하세요.",
                "vi": "Cấp hồ sơ bệnh án có thể mất vài ngày nên hãy nộp đơn trước.",
                "situation": "onsite"
            },
            {
                "ko": "귀국하실 거면 의무기록 미리 받아가세요.",
                "vi": "Nếu về nước, hãy nhận hồ sơ bệnh án trước.",
                "situation": "informal"
            }
        ],
        "relatedTerms": ["전자의무기록", "환자권리", "개인정보보호"]
    },
    {
        "slug": "dang-ky-benh-nhan-nuoc-ngoai",
        "korean": "외국인환자등록",
        "vietnamese": "đăng ký bệnh nhân nước ngoài",
        "hanja": "外國人患者登錄",
        "hanjaReading": "외(바깥 외) + 국(나라 국) + 인(사람 인) + 환(근심 환) + 자(사람 자) + 등(올릴 등) + 록(기록할 록)",
        "pronunciation": "oegugin-hwanja-deungnok",
        "meaningKo": "외국인이 한국 병원에서 진료를 받기 위해 최초 방문 시 진행하는 등록 절차로, 여권, 외국인등록증 또는 체류증, 보험 정보 등을 제출하여 환자로 등록됩니다. 일부 대형 병원은 외국인 전용 창구나 국제진료센터를 운영하며, 통역 서비스를 제공하기도 합니다. 통역 시 주의할 점은 외국인 환자는 건강보험 가입 여부에 따라 진료비가 크게 달라지므로, 보험 가입 상태를 정확히 확인하고 등록 시 관련 서류를 제출하도록 안내해야 합니다. 또한 외국인 환자는 한국 의료 시스템에 익숙하지 않아 등록 절차에서 혼란을 겪을 수 있으므로, 통역사가 친절하고 명확하게 안내하는 것이 중요합니다.",
        "meaningVi": "Quy trình đăng ký khi người nước ngoài đến khám chữa bệnh lần đầu tại bệnh viện Hàn Quốc, nộp hộ chiếu, thẻ đăng ký người nước ngoài hoặc thẻ cư trú, thông tin bảo hiểm để đăng ký làm bệnh nhân. Một số bệnh viện lớn có quầy chuyên dụng cho người nước ngoài hoặc Trung tâm Khám chữa bệnh Quốc tế, cung cấp dịch vụ thông dịch.",
        "context": "외국인 의료, 병원 등록, 국제 진료",
        "culturalNote": "한국은 외국인 환자 유치를 위해 국제진료센터를 운영하는 병원이 증가하고 있지만, 여전히 많은 병원에서 외국인 환자 대응이 미흡합니다. 베트남 근로자들은 대부분 중소 병원이나 의원을 이용하는데, 이곳에서는 통역 서비스가 없어 어려움을 겪는 경우가 많으므로, 전문 의료통역사의 역할이 중요합니다.",
        "commonMistakes": [
            {
                "mistake": "외국인 등록을 내국인과 동일한 절차로 안내",
                "correction": "외국인은 여권, 외국인등록증 등 추가 서류 필요 - 사전 안내",
                "explanation": "필요 서류 미비로 등록 지연 방지"
            },
            {
                "mistake": "건강보험 가입 여부를 확인하지 않음",
                "correction": "보험 가입 여부에 따라 진료비 차이 큼 - 반드시 확인하고 증빙 제출",
                "explanation": "보험 미적용 시 고액 진료비 부담 발생"
            },
            {
                "mistake": "모든 병원에 국제진료센터가 있다고 안내",
                "correction": "국제진료센터는 일부 대형 병원에만 있음 - 사전 확인 필요",
                "explanation": "잘못된 기대로 환자 불편 방지"
            }
        ],
        "examples": [
            {
                "ko": "외국인 환자 등록을 위해 여권과 외국인등록증을 준비해 주세요.",
                "vi": "Để đăng ký bệnh nhân nước ngoài, vui lòng chuẩn bị hộ chiếu và thẻ đăng ký người nước ngoài.",
                "situation": "formal"
            },
            {
                "ko": "건강보험 가입자이신가요? 보험증을 제출하시면 진료비가 줄어듭니다.",
                "vi": "Bạn có tham gia bảo hiểm y tế không? Nộp thẻ bảo hiểm sẽ giảm viện phí.",
                "situation": "onsite"
            },
            {
                "ko": "이 병원은 외국인 전용 창구가 있어서 편해요.",
                "vi": "Bệnh viện này có quầy chuyên cho người nước ngoài nên tiện.",
                "situation": "informal"
            }
        ],
        "relatedTerms": ["국민건강보험", "국제진료센터", "외국인등록증"]
    },
    {
        "slug": "giam-tru-vien-phi",
        "korean": "의료비감면",
        "vietnamese": "giảm trừ viện phí",
        "hanja": "醫療費減免",
        "hanjaReading": "의(의원 의) + 료(고칠 료) + 비(쓸 비) + 감(덜 감) + 면(면할 면)",
        "pronunciation": "uiryobi-gamyeon",
        "meaningKo": "경제적 어려움이 있는 환자에게 병원이 의료비의 일부 또는 전부를 면제해주는 제도로, 저소득층, 의료급여 수급자, 재난 피해자 등이 대상입니다. 각 병원마다 감면 기준과 비율이 다르며, 신청 시 소득 증빙 서류가 필요합니다. 통역 시 주의할 점은 외국인도 일정 요건을 충족하면 의료비 감면을 받을 수 있는 경우가 있으므로, 경제적 어려움이 있는 환자에게 제도를 안내하고 신청을 도와야 합니다. 다만 통역사가 감면 여부를 판단할 수 없으므로, 병원 사회복지사나 담당 부서에 연결하는 것이 적절합니다.",
        "meaningVi": "Chế độ bệnh viện miễn một phần hoặc toàn bộ viện phí cho bệnh nhân có hoàn cảnh kinh tế khó khăn. Đối tượng là người thu nhập thấp, người nhận trợ cấp y tế, người bị thiên tai. Tiêu chuẩn và tỷ lệ giảm trừ khác nhau tùy bệnh viện, cần giấy chứng minh thu nhập khi nộp đơn.",
        "context": "의료 복지, 경제적 지원, 환자 권리",
        "culturalNote": "한국은 의료비 감면 제도가 있지만, 외국인의 경우 적용 범위가 제한적이고 병원마다 정책이 다릅니다. 베트남 근로자들은 이런 제도를 모르는 경우가 많아 경제적 어려움에도 신청하지 못하는 경우가 있으므로, 통역사가 정보를 제공하는 것이 중요합니다.",
        "commonMistakes": [
            {
                "mistake": "모든 외국인이 의료비 감면을 받을 수 있다고 안내",
                "correction": "외국인 감면은 제한적 - 병원 정책 확인 필요",
                "explanation": "잘못된 기대로 인한 실망과 분쟁 방지"
            },
            {
                "mistake": "통역사가 감면 여부를 판단",
                "correction": "감면은 병원 사회복지사나 담당 부서에서 판단 - 연결만 도움",
                "explanation": "통역사는 정보 제공자이지 결정권자가 아님"
            },
            {
                "mistake": "감면 신청을 안내하지 않음",
                "correction": "경제적 어려움 있는 환자에게 감면 제도 존재 알림 - 신청 기회 제공",
                "explanation": "환자의 권리 보호 및 경제적 부담 경감 도움"
            }
        ],
        "examples": [
            {
                "ko": "경제적으로 어려우시면 의료비 감면을 신청하실 수 있습니다.",
                "vi": "Nếu khó khăn về kinh tế, có thể nộp đơn xin giảm trừ viện phí.",
                "situation": "formal"
            },
            {
                "ko": "감면 신청은 사회복지팀에 문의하세요.",
                "vi": "Đơn xin giảm trừ, hãy liên hệ đội phúc lợi xã hội.",
                "situation": "onsite"
            },
            {
                "ko": "외국인도 상황에 따라 감면받을 수 있어요. 물어보세요.",
                "vi": "Người nước ngoài tùy hoàn cảnh cũng có thể được giảm. Hãy hỏi.",
                "situation": "informal"
            }
        ],
        "relatedTerms": ["의료급여", "본인부담금", "사회복지"]
    },
    {
        "slug": "cam-tu-choi-cap-cuu",
        "korean": "응급의료거부금지",
        "vietnamese": "cấm từ chối cấp cứu",
        "hanja": "應急醫療拒否禁止",
        "hanjaReading": "응(응할 응) + 급(급할 급) + 의(의원 의) + 료(고칠 료) + 거(막을 거) + 부(아닐 부) + 금(금할 금) + 지(그칠 지)",
        "pronunciation": "eunggeum-uiryo-geobu-geumji",
        "meaningKo": "응급환자가 발생했을 때 병원이나 의료인이 경제적 이유, 병상 부족 등을 이유로 진료를 거부할 수 없도록 법으로 금지한 것입니다. 응급의료에 관한 법률에 따라 모든 의료기관은 응급환자를 우선 치료해야 하며, 이를 위반하면 처벌받습니다. 통역 시 주의할 점은 외국인 환자도 응급 상황에서는 보험 유무나 지불 능력과 관계없이 치료받을 권리가 있다는 점을 알려야 합니다. 응급 상황에서 환자나 가족이 돈이 없어 병원이 거부할까봐 두려워한다면, 이 법적 보호를 설명하여 안심시켜야 합니다.",
        "meaningVi": "Luật cấm bệnh viện hoặc nhân viên y tế từ chối khám chữa bệnh khi có bệnh nhân cấp cứu vì lý do kinh tế, thiếu giường bệnh. Theo Luật Y tế Cấp cứu, tất cả cơ sở y tế phải ưu tiên điều trị bệnh nhân cấp cứu, vi phạm sẽ bị xử phạt.",
        "context": "응급 의료, 환자 권리, 법적 보호",
        "culturalNote": "한국은 응급의료 체계가 잘 구축되어 있고 법적 보호가 강하지만, 베트남을 포함한 일부 국가에서는 돈이 없으면 응급실에서도 거부당하는 경우가 있습니다. 외국인 환자는 한국에서도 마찬가지일 것이라 두려워할 수 있으므로, 통역사가 법적 보호를 명확히 알려 안심시켜야 합니다.",
        "commonMistakes": [
            {
                "mistake": "돈이 없으면 응급실에서도 진료를 못 받는다고 생각하게 함",
                "correction": "응급 상황에서는 지불 능력 관계없이 치료 우선 - 법적 보호 강조",
                "explanation": "환자가 두려움 때문에 응급실 방문을 주저하지 않도록"
            },
            {
                "mistake": "외국인은 응급의료 거부금지 대상이 아니라고 설명",
                "correction": "외국인도 동등하게 법적 보호 받음 - 차별 없음",
                "explanation": "모든 사람의 생명권은 동등하게 보호됨"
            },
            {
                "mistake": "응급 상황을 환자가 판단하도록 함",
                "correction": "의심스러우면 119 또는 응급실로 - 전문가가 판단",
                "explanation": "환자의 자가 판단 오류로 인한 위험 방지"
            }
        ],
        "examples": [
            {
                "ko": "응급 상황에서는 돈이 없어도 병원이 거부할 수 없습니다. 법으로 금지되어 있어요.",
                "vi": "Tình huống cấp cứu, dù không có tiền, bệnh viện không thể từ chối. Luật cấm.",
                "situation": "formal"
            },
            {
                "ko": "외국인도 응급 시에는 동일하게 보호받습니다.",
                "vi": "Người nước ngoài cũng được bảo vệ như nhau khi cấp cứu.",
                "situation": "onsite"
            },
            {
                "ko": "응급이면 일단 병원 가세요. 걱정 말고요.",
                "vi": "Nếu cấp cứu, hãy đến bệnh viện trước. Đừng lo.",
                "situation": "informal"
            }
        ],
        "relatedTerms": ["응급실", "환자권리", "119"]
    },
    {
        "slug": "giay-phep-nhan-vien-y-te",
        "korean": "의료인면허",
        "vietnamese": "giấy phép nhân viên y tế",
        "hanja": "醫療人免許",
        "hanjaReading": "의(의원 의) + 료(고칠 료) + 인(사람 인) + 면(면할 면) + 허(허락할 허)",
        "pronunciation": "uiryoin-myeonheo",
        "meaningKo": "의사, 치과의사, 한의사, 간호사, 조산사 등 의료 행위를 할 수 있는 자격을 국가가 공식적으로 인정하여 발급하는 면허증입니다. 한국에서는 의료 면허 없이 의료 행위를 하면 불법이며 처벌받습니다. 통역 시 주의할 점은 외국 의료인 면허는 한국에서 자동으로 인정되지 않으며, 한국 면허 시험을 통과해야 한국에서 의료 행위를 할 수 있다는 점입니다. 베트남에서 의료인이었던 사람이 한국에서 같은 일을 하려면 한국 면허를 취득해야 하므로, 이 점을 명확히 안내해야 합니다. 또한 환자가 진료받는 의료인의 면허 여부를 확인할 권리가 있음을 알려줄 수 있습니다.",
        "meaningVi": "Giấy phép do nhà nước chính thức cấp công nhận tư cách có thể hành nghề y tế như bác sĩ, nha sĩ, bác sĩ y học cổ truyền, y tá, hộ sinh. Ở Hàn Quốc, hành nghề y không có giấy phép là bất hợp pháp và bị xử phạt.",
        "context": "의료 자격, 법적 규제, 환자 안전",
        "culturalNote": "한국은 의료 면허 제도가 엄격하여 무면허 의료 행위를 철저히 단속하지만, 일부 국가에서는 느슨할 수 있습니다. 베트남 커뮤니티 내에서 무면허로 의료 행위를 하는 경우가 있을 수 있으나, 이는 불법이며 환자에게 위험하므로, 통역사는 환자가 정식 면허를 가진 의료인에게 진료받도록 안내해야 합니다.",
        "commonMistakes": [
            {
                "mistake": "외국 의료인 면허가 한국에서도 유효하다고 설명",
                "correction": "외국 면허는 한국에서 인정 안 됨 - 한국 면허 시험 통과 필요",
                "explanation": "무면허 의료 행위는 불법이므로 정확한 정보 제공 필수"
            },
            {
                "mistake": "커뮤니티 내 무면허 의료 행위를 묵인하거나 소개",
                "correction": "무면허 의료 행위는 불법 - 정식 병원 방문 권장",
                "explanation": "환자 안전과 법적 보호를 위해 합법적 의료 이용 안내"
            },
            {
                "mistake": "의료인의 면허 여부를 확인할 필요 없다고 안내",
                "correction": "환자는 의료인 면허 확인 권리 있음 - 병원에 게시되어 있음",
                "explanation": "환자의 알 권리 보장"
            }
        ],
        "examples": [
            {
                "ko": "한국에서 의료 행위를 하려면 한국 의료인 면허가 필요합니다.",
                "vi": "Để hành nghề y ở Hàn Quốc, cần có giấy phép nhân viên y tế Hàn Quốc.",
                "situation": "formal"
            },
            {
                "ko": "의사 선생님의 면허증은 진료실에 게시되어 있습니다.",
                "vi": "Giấy phép của bác sĩ được niêm yết trong phòng khám.",
                "situation": "onsite"
            },
            {
                "ko": "무면허 의료는 불법이에요. 정식 병원에 가세요.",
                "vi": "Y tế không phép là bất hợp pháp. Hãy đến bệnh viện chính thức.",
                "situation": "informal"
            }
        ],
        "relatedTerms": ["의사", "간호사", "의료법"]
    }
]

# Read existing data
with open(file_path, 'r', encoding='utf-8') as f:
    data = json.load(f)

# Add final terms from part 3
data.extend(new_terms_part3)

# Write back
with open(file_path, 'w', encoding='utf-8') as f:
    json.dump(data, f, ensure_ascii=False, indent=2)

print(f"✅ Successfully added {len(new_terms_part3)} final medical terms (Part 3)")
print(f"📊 Total terms in medical.json now: {len(data)}")
print(f"\n🎉 ALL 40 TERMS COMPLETED!")
print(f"\nRun this to add all terms:")
print(f"cd /Users/mac/Documents/claude_code/projects/vn.epicstage.co.kr && python3 src/scripts/add-med-v2-961.py && python3 src/scripts/add-med-v2-961-part2.py && python3 src/scripts/add-med-v2-961-part3.py")
