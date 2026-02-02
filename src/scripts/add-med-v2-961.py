#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Add 40 NEW medical terms to medical.json
Focus: Health insurance, Medical law/ethics, Medical interpreting, Medical documents
"""

import json
import os

# Use relative path from script location
file_path = os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', 'data', 'terms', 'medical.json')

new_terms = [
    {
        "slug": "bao-hiem-y-te-quoc-gia",
        "korean": "국민건강보험",
        "vietnamese": "bảo hiểm y tế quốc gia",
        "hanja": "國民健康保險",
        "hanjaReading": "국(나라 국) + 민(백성 민) + 건(건강할 건) + 강(강할 강) + 보(지킬 보) + 험(험할 험)",
        "pronunciation": "gungmin-geongang-boheom",
        "meaningKo": "대한민국의 전 국민이 의무적으로 가입하는 사회보험으로, 의료비 부담을 줄이고 국민 건강을 보장하기 위한 제도입니다. 통역 시 주의할 점은 외국인 근로자도 체류 6개월 이후 의무 가입 대상이며, 보험료는 소득에 따라 차등 적용됩니다. 베트남의 보험 시스템과 달리 본인부담금 비율이 정해져 있고, 비급여 항목은 전액 본인 부담입니다. 환자에게 설명할 때는 급여/비급여 구분을 명확히 해야 오해를 방지할 수 있습니다.",
        "meaningVi": "Chế độ bảo hiểm y tế bắt buộc cho toàn thể công dân Hàn Quốc, giúp giảm gánh nặng chi phí y tế và đảm bảo sức khỏe cho người dân. Người lao động nước ngoài cũng phải tham gia sau 6 tháng cư trú.",
        "context": "의료보험, 건강관리, 외국인 의료",
        "culturalNote": "한국의 건강보험은 보장성이 높지만 비급여 항목이 많아 실제 본인부담금이 클 수 있습니다. 베트남과 달리 모든 국민이 의무 가입하며, 직장가입자와 지역가입자로 구분됩니다. 외국인 근로자는 이 차이를 이해하지 못해 보험료 납부에 혼란을 겪는 경우가 많습니다.",
        "commonMistakes": [
            {
                "mistake": "건강보험을 단순히 'bảo hiểm sức khỏe'로 번역",
                "correction": "'bảo hiểm y tế quốc gia' 또는 'bảo hiểm y tế bắt buộc'로 번역",
                "explanation": "한국의 건강보험은 국가가 운영하는 의무보험이므로 일반 민간 건강보험과 구분해야 합니다"
            },
            {
                "mistake": "급여/비급여 구분 없이 '보험 적용'이라고만 설명",
                "correction": "급여는 'được bảo hiểm chi trả', 비급여는 'không được bảo hiểm chi trả'로 명확히 구분",
                "explanation": "환자가 본인부담금을 예상하지 못해 발생하는 의료분쟁을 예방하기 위해 반드시 구분 설명 필요"
            },
            {
                "mistake": "외국인도 자동으로 보험 혜택을 받는다고 설명",
                "correction": "6개월 체류 후 의무가입, 보험료 납부 필요 설명",
                "explanation": "외국인은 체류기간과 보험료 납부 여부에 따라 혜택이 달라집니다"
            }
        ],
        "examples": [
            {
                "ko": "국민건강보험증을 지참하셨나요?",
                "vi": "Bạn có mang theo thẻ bảo hiểm y tế quốc gia không?",
                "situation": "formal"
            },
            {
                "ko": "이 치료는 건강보험이 적용되지 않아 전액 본인부담입니다.",
                "vi": "Điều trị này không được bảo hiểm y tế chi trả nên bạn phải tự thanh toán toàn bộ.",
                "situation": "onsite"
            },
            {
                "ko": "외국인 근로자도 6개월 후부터 건강보험 의무가입 대상입니다.",
                "vi": "Lao động nước ngoài cũng phải tham gia bảo hiểm y tế bắt buộc sau 6 tháng.",
                "situation": "formal"
            }
        ],
        "relatedTerms": ["본인부담금", "비급여항목", "의료급여"]
    },
    {
        "slug": "tro-cap-y-te",
        "korean": "의료급여",
        "vietnamese": "trợ cấp y tế",
        "hanja": "醫療給與",
        "hanjaReading": "의(의원 의) + 료(고칠 료) + 급(줄 급) + 여(줄 여)",
        "pronunciation": "uiryo-geupyeo",
        "meaningKo": "생활이 어려운 저소득층을 대상으로 국가가 의료비를 지원하는 공공부조 제도입니다. 건강보험과는 달리 보험료를 내지 않고도 의료 혜택을 받을 수 있으며, 본인부담금도 매우 낮거나 없습니다. 통역 시 주의할 점은 의료급여 수급자는 건강보험 가입자와 진료 절차가 다르며, 특정 병원에서만 진료를 받아야 하는 제한이 있을 수 있습니다. 외국인 근로자는 기본적으로 대상이 아니지만, 난민 인정자나 특별한 경우 수급 가능성이 있으므로 정확한 안내가 필요합니다.",
        "meaningVi": "Chế độ hỗ trợ y tế của nhà nước dành cho người có hoàn cảnh khó khăn, giúp họ được khám chữa bệnh mà không phải đóng phí bảo hiểm. Chi phí khám chữa bệnh được nhà nước chi trả hầu hết hoặc toàn bộ.",
        "context": "의료복지, 공공의료, 저소득층 지원",
        "culturalNote": "한국의 의료급여는 베트nam의 'bảo hiểm y tế miễn phí cho người nghèo'와 유사하지만, 선정 기준과 절차가 더 엄격합니다. 수급자는 1종과 2종으로 구분되며 본인부담금이 다릅니다. 외국인은 대부분 대상이 아니므로 환자가 기대하지 않도록 명확히 안내해야 합니다.",
        "commonMistakes": [
            {
                "mistake": "의료급여를 건강보험의 일종으로 설명",
                "correction": "의료급여는 'chế độ trợ cấp y tế', 건강보험은 'bảo hiểm y tế' - 완전히 다른 제도임을 강조",
                "explanation": "의료급여는 공공부조이고 건강보험은 사회보험으로 재원과 대상이 다릅니다"
            },
            {
                "mistake": "외국인도 신청하면 받을 수 있다고 안내",
                "correction": "원칙적으로 외국인은 제외, 예외 사항 확인 필요",
                "explanation": "잘못된 기대를 주면 민원이 발생하므로 정확한 자격 요건 안내 필수"
            },
            {
                "mistake": "의료급여 1종과 2종의 차이를 설명하지 않음",
                "correction": "1종은 본인부담 거의 없음, 2종은 일부 부담 - 명확히 구분 설명",
                "explanation": "환자가 예상치 못한 본인부담금 발생 시 불만 제기 가능"
            }
        ],
        "examples": [
            {
                "ko": "의료급여 수급자이신가요?",
                "vi": "Bạn có phải là người nhận trợ cấp y tế không?",
                "situation": "formal"
            },
            {
                "ko": "의료급여증을 제시해 주세요.",
                "vi": "Vui lòng xuất trình thẻ trợ cấp y tế.",
                "situation": "onsite"
            },
            {
                "ko": "외국인은 의료급여 대상이 아니므로 건강보험에 가입하셔야 합니다.",
                "vi": "Người nước ngoài không thuộc đối tượng trợ cấp y tế nên phải tham gia bảo hiểm y tế.",
                "situation": "formal"
            }
        ],
        "relatedTerms": ["국민건강보험", "본인부담금", "공공의료"]
    },
    {
        "slug": "bao-hiem-thuc-te",
        "korean": "실손보험",
        "vietnamese": "bảo hiểm thực tế",
        "hanja": "實損保險",
        "hanjaReading": "실(열매 실) + 손(손해 손) + 보(지킬 보) + 험(험할 험)",
        "pronunciation": "silson-boheom",
        "meaningKo": "실제 발생한 의료비 손해를 보상하는 민간 의료보험으로, 건강보험에서 보장하지 않는 비급여 항목이나 본인부담금을 보전해 줍니다. 통역 시 주의할 점은 실손보험은 국민건강보험과 별개의 사보험이며, 가입은 선택사항입니다. 환자가 실손보험 청구를 원할 경우 진료비 영수증, 진료비 세부내역서, 진단서 등이 필요하므로 사전에 안내해야 합니다. 보험사마다 보장 범위와 청구 절차가 다르므로 환자가 직접 보험사에 확인하도록 안내하는 것이 안전합니다.",
        "meaningVi": "Bảo hiểm y tế tư nhân bồi thường chi phí y tế thực tế phát sinh, bao gồm các khoản không được bảo hiểm y tế quốc gia chi trả hoặc phần bệnh nhân tự trả. Đây là bảo hiểm tự nguyện, không bắt buộc.",
        "context": "민간보험, 의료비 청구, 보험금 수령",
        "culturalNote": "한국에서는 대부분의 국민이 실손보험에 추가 가입하여 의료비 부담을 줄입니다. 베트남에서는 민간 의료보험이 덜 보편화되어 있어 환자가 실손보험 청구 절차를 잘 모르는 경우가 많습니다. 보험사별로 요구 서류와 절차가 달라 통역사가 일일이 안내하기 어렵습니다.",
        "commonMistakes": [
            {
                "mistake": "실손보험을 건강보험의 일부로 설명",
                "correction": "실손보험은 'bảo hiểm tư nhân' (민간보험), 건강보험은 'bảo hiểm quốc gia' (국가보험) - 완전히 별개",
                "explanation": "두 보험의 성격과 운영 주체가 다르므로 혼동하면 안 됩니다"
            },
            {
                "mistake": "병원이 보험금을 직접 지급한다고 설명",
                "correction": "환자가 병원비를 먼저 내고, 서류를 보험사에 제출해 환급받는 구조 설명",
                "explanation": "실손보험은 후불 정산 방식이므로 환자가 선납 후 청구해야 합니다"
            },
            {
                "mistake": "모든 비급여 항목이 실손보험으로 보장된다고 안내",
                "correction": "보험 상품마다 보장 범위가 다르므로 환자가 직접 보험사에 확인하도록 안내",
                "explanation": "통역사가 보장 여부를 단정하면 분쟁 소지가 있습니다"
            }
        ],
        "examples": [
            {
                "ko": "실손보험 청구를 위해 진료비 영수증과 세부내역서가 필요합니다.",
                "vi": "Để yêu cầu bảo hiểm thực tế, bạn cần hóa đơn viện phí và bảng kê chi tiết.",
                "situation": "formal"
            },
            {
                "ko": "실손보험 가입 여부를 확인해 주세요.",
                "vi": "Vui lòng xác nhận xem bạn có tham gia bảo hiểm thực tế không.",
                "situation": "onsite"
            },
            {
                "ko": "실손보험 보장 범위는 보험사마다 다르니 직접 문의하세요.",
                "vi": "Phạm vi bảo hiểm thực tế khác nhau tùy công ty, vui lòng liên hệ trực tiếp.",
                "situation": "informal"
            }
        ],
        "relatedTerms": ["비급여항목", "본인부담금", "의료비영수증"]
    },
    {
        "slug": "chi-phi-tu-tra",
        "korean": "본인부담금",
        "vietnamese": "chi phí tự trả",
        "hanja": "本人負擔金",
        "hanjaReading": "본(근본 본) + 인(사람 인) + 부(짊어질 부) + 담(짐 담) + 금(쇠 금)",
        "pronunciation": "bonin-budamgeum",
        "meaningKo": "건강보험이 적용되더라도 환자가 직접 부담해야 하는 의료비를 말합니다. 한국의 건강보험은 진료비의 일정 비율만 보장하고, 나머지는 본인부담금으로 환자가 지불합니다. 통역 시 주의할 점은 외래는 보통 30~50%, 입원은 20% 정도가 본인부담금이며, 상급종합병원 이용 시 본인부담금이 더 높습니다. 환자가 '보험 적용'을 '무료'로 오해하지 않도록 명확히 설명해야 하며, 특히 외국인 환자는 본인부담금 개념을 이해하지 못해 분쟁이 발생하는 경우가 많습니다.",
        "meaningVi": "Khoản tiền bệnh nhân phải tự trả ngay cả khi có bảo hiểm y tế. Bảo hiểm y tế Hàn Quốc chỉ chi trả một phần chi phí, phần còn lại bệnh nhân phải tự trả theo tỷ lệ nhất định (ngoại trú khoảng 30-50%, nội trú khoảng 20%).",
        "context": "진료비 결제, 의료보험, 비용 안내",
        "culturalNote": "베트남에서는 보험 적용되면 무료 또는 매우 적은 금액만 내는 경우가 많지만, 한국은 본인부담금 비율이 상당히 높아 환자들이 예상보다 많은 비용을 내야 할 수 있습니다. 특히 비급여 항목은 전액 본인부담이므로 사전 설명이 필수입니다.",
        "commonMistakes": [
            {
                "mistake": "본인부담금을 단순히 'tiền bệnh nhân trả'로만 번역",
                "correction": "'chi phí tự trả' 또는 'tiền đồng chi trả'로 구체적으로 번역하고 비율 설명",
                "explanation": "환자가 금액 규모를 예상할 수 있도록 비율 정보 제공 필요"
            },
            {
                "mistake": "보험 적용 = 무료라고 오해하도록 통역",
                "correction": "보험 적용되어도 본인부담금이 있다는 점 명확히 강조",
                "explanation": "환자가 청구서를 받고 놀라지 않도록 사전 예방 필수"
            },
            {
                "mistake": "병원 규모에 따른 본인부담금 차이를 설명하지 않음",
                "correction": "의원 < 병원 < 상급종합병원 순으로 본인부담금 증가 설명",
                "explanation": "환자가 병원 선택 시 비용을 고려할 수 있도록 정보 제공"
            }
        ],
        "examples": [
            {
                "ko": "보험 적용 후 본인부담금은 약 3만원입니다.",
                "vi": "Sau khi áp dụng bảo hiểm, chi phí tự trả khoảng 30,000 won.",
                "situation": "formal"
            },
            {
                "ko": "이 치료는 비급여라서 본인부담금이 100% 입니다.",
                "vi": "Điều trị này không được bảo hiểm chi trả nên bạn phải tự trả 100%.",
                "situation": "onsite"
            },
            {
                "ko": "상급종합병원은 본인부담금 비율이 더 높아요.",
                "vi": "Bệnh viện tuyến cao có tỷ lệ chi phí tự trả cao hơn.",
                "situation": "informal"
            }
        ],
        "relatedTerms": ["국민건강보험", "비급여항목", "진료비"]
    },
    {
        "slug": "khoan-khong-duoc-bao-hiem",
        "korean": "비급여항목",
        "vietnamese": "khoản không được bảo hiểm",
        "hanja": "非給與項目",
        "hanjaReading": "비(아닐 비) + 급(줄 급) + 여(줄 여) + 항(항목 항) + 목(눈 목)",
        "pronunciation": "bigeupyeo-hangmok",
        "meaningKo": "건강보험에서 보장하지 않아 환자가 전액 부담해야 하는 진료 항목을 말합니다. 미용 목적의 성형수술, 치과 임플란트, 한방 진료, 특실 입원료, 간병비 등이 대표적입니다. 통역 시 가장 주의해야 할 부분은 환자가 비급여 항목을 모르고 진료받다가 고액의 의료비를 청구받아 분쟁이 발생하는 경우가 많다는 점입니다. 의사가 비급여 항목을 설명할 때는 반드시 '전액 본인부담'임을 강조하고, 대략적인 비용을 미리 안내하도록 통역해야 합니다.",
        "meaningVi": "Các hạng mục khám chữa bệnh không được bảo hiểm y tế chi trả, bệnh nhân phải tự thanh toán toàn bộ chi phí. Bao gồm phẫu thuật thẩm mỹ, cấy ghép răng implant, điều trị y học cổ truyền, phòng bệnh cao cấp, chi phí chăm sóc, v.v.",
        "context": "진료비 안내, 의료보험, 비용 분쟁 예방",
        "culturalNote": "한국의 비급여 항목은 베트남보다 범위가 넓고 비용이 매우 높습니다. 특히 외국인 환자는 비급여 개념을 잘 모르고, 의사가 권하는 치료는 모두 보험 적용으로 오해하는 경우가 많아 통역사의 명확한 설명이 필수입니다. 비급여 항목은 병원마다 가격이 다를 수 있습니다.",
        "commonMistakes": [
            {
                "mistake": "비급여를 단순히 'không có bảo hiểm'으로만 번역",
                "correction": "'khoản không được bảo hiểm chi trả - bệnh nhân phải tự trả 100%'로 명확히 설명",
                "explanation": "환자가 전액 부담임을 정확히 이해하도록 강조 필요"
            },
            {
                "mistake": "비급여 항목임을 언급하지 않고 그냥 치료 내용만 통역",
                "correction": "의사가 비급여 언급 안 해도 통역사가 확인 후 환자에게 알려야",
                "explanation": "의료분쟁 예방을 위해 통역사의 능동적 확인과 설명 필수"
            },
            {
                "mistake": "대략적인 비용 안내 없이 진행",
                "correction": "가능하면 비급여 항목의 예상 비용을 미리 안내하도록 의사에게 요청",
                "explanation": "환자가 치료 여부를 결정할 수 있도록 정보 제공 필요"
            }
        ],
        "examples": [
            {
                "ko": "이 치료는 비급여 항목이라 전액 본인부담입니다.",
                "vi": "Điều trị này là khoản không được bảo hiểm nên bạn phải tự trả toàn bộ.",
                "situation": "formal"
            },
            {
                "ko": "특실 입원료는 비급여라서 하루에 10만원 정도 추가됩니다.",
                "vi": "Phòng bệnh cao cấp không được bảo hiểm, thêm khoảng 100,000 won/ngày.",
                "situation": "onsite"
            },
            {
                "ko": "비급여 항목에 대해서는 사전에 동의서를 받아야 합니다.",
                "vi": "Đối với khoản không được bảo hiểm, phải có sự đồng ý trước của bệnh nhân.",
                "situation": "formal"
            }
        ],
        "relatedTerms": ["본인부담금", "실손보험", "진료비세부산정내역"]
    },
    {
        "slug": "che-do-dac-biet",
        "korean": "산정특례",
        "vietnamese": "chế độ đặc biệt",
        "hanja": "算定特例",
        "hanjaReading": "산(셈 산) + 정(정할 정) + 특(특별할 특) + 례(례 례)",
        "pronunciation": "sanjeong-teukrye",
        "meaningKo": "암, 희귀질환, 중증난치질환 등 고액의 치료비가 필요한 중증질환자의 본인부담금을 경감해주는 건강보험 제도입니다. 일반적으로 본인부담률이 5~10%로 대폭 낮아지며, 등록 후 일정 기간 혜택을 받을 수 있습니다. 통역 시 주의할 점은 산정특례는 자동으로 적용되지 않고 환자가 신청해야 하며, 의사의 진단서와 소견서가 필요합니다. 외국인 근로자도 건강보험 가입자라면 신청 가능하므로, 중증질환 진단 시 반드시 산정특례 제도를 안내하여 환자의 의료비 부담을 줄여야 합니다.",
        "meaningVi": "Chế độ giảm chi phí tự trả trong bảo hiểm y tế dành cho bệnh nhân mắc bệnh hiểm nghèo như ung thư, bệnh hiếm, bệnh nan y. Tỷ lệ tự trả giảm xuống 5-10%. Người lao động nước ngoài có bảo hiểm y tế cũng có thể đăng ký.",
        "context": "중증질환 치료, 의료비 감면, 건강보험",
        "culturalNote": "베트남에는 유사한 제도가 없거나 덜 체계화되어 있어 환자가 이 제도를 이해하기 어려울 수 있습니다. 한국에서는 암 환자의 경제적 부담을 크게 줄여주는 중요한 제도이므로, 통역사가 적극적으로 안내하여 환자가 혜택을 놓치지 않도록 해야 합니다.",
        "commonMistakes": [
            {
                "mistake": "산정특례를 단순히 'giảm giá'로 번역",
                "correction": "'chế độ giảm chi phí đặc biệt cho bệnh hiểm nghèo' - 제도의 성격과 대상 명확히 설명",
                "explanation": "단순 할인이 아닌 법적 제도이며 중증질환자만 해당됨을 알려야"
            },
            {
                "mistake": "자동 적용된다고 설명",
                "correction": "환자가 직접 신청해야 하며, 의사 진단서 필요 - 신청 절차 안내",
                "explanation": "환자가 혜택을 받으려면 능동적으로 신청해야 함"
            },
            {
                "mistake": "외국인은 대상이 아니라고 안내",
                "correction": "건강보험 가입 외국인도 신청 가능 - 자격 요건 정확히 안내",
                "explanation": "외국인도 건강보험 가입자라면 내국인과 동일한 혜택 받을 수 있음"
            }
        ],
        "examples": [
            {
                "ko": "암 진단을 받으셨으니 산정특례를 신청하시면 본인부담금이 5%로 줄어듭니다.",
                "vi": "Vì bạn được chẩn đoán ung thư, nếu đăng ký chế độ đặc biệt, chi phí tự trả giảm xuống 5%.",
                "situation": "formal"
            },
            {
                "ko": "산정특례 신청을 위해 의사 소견서가 필요합니다.",
                "vi": "Để đăng ký chế độ đặc biệt, cần có giấy chẩn đoán của bác sĩ.",
                "situation": "onsite"
            },
            {
                "ko": "산정특례 등록 후 5년간 혜택을 받을 수 있어요.",
                "vi": "Sau khi đăng ký chế độ đặc biệt, bạn được hưởng quyền lợi trong 5 năm.",
                "situation": "informal"
            }
        ],
        "relatedTerms": ["본인부담금", "국민건강보험", "중증질환"]
    },
    {
        "slug": "dieu-chinh-tranh-chap-y-te",
        "korean": "의료분쟁조정",
        "vietnamese": "điều chỉnh tranh chấp y tế",
        "hanja": "醫療紛爭調整",
        "hanjaReading": "의(의원 의) + 료(고칠 료) + 분(어지러울 분) + 쟁(다툴 쟁) + 조(고를 조) + 정(바를 정)",
        "pronunciation": "uiryo-bunjaeng-jojeong",
        "meaningKo": "의료사고나 의료과오로 인해 발생한 환자와 의료인 간의 분쟁을 법적 소송 없이 중재하여 해결하는 제도입니다. 한국의료분쟁조정중재원에서 담당하며, 무료로 신청할 수 있고 소송보다 빠르고 경제적입니다. 통역 시 주의할 점은 외국인 환자도 이용 가능하며, 통역사가 의료분쟁 조정 제도를 알고 있어야 환자가 억울한 상황에서 적절한 구제 방법을 안내할 수 있습니다. 다만 통역사는 법률 자문을 할 수 없으므로, 제도의 존재를 알려주고 전문 기관에 연결하는 역할에 그쳐야 합니다.",
        "meaningVi": "Chế độ hòa giải tranh chấp giữa bệnh nhân và nhân viên y tế do tai nạn hoặc sai sót y khoa, thông qua Trung tâm Hòa giải Tranh chấp Y tế Hàn Quốc mà không cần kiện tụng. Người nước ngoài cũng có thể sử dụng dịch vụ miễn phí này.",
        "context": "의료사고, 환자 권리, 법적 보호",
        "culturalNote": "베트남에서는 의료분쟁 시 개인적으로 해결하거나 법원에 가는 경우가 많지만, 한국은 전문 조정기관이 있어 환자 보호가 체계적입니다. 외국인 환자는 이 제도를 모르는 경우가 많아 억울한 상황에서도 포기하는 경우가 있으므로 통역사의 안내가 중요합니다.",
        "commonMistakes": [
            {
                "mistake": "의료분쟁을 단순히 'tranh chấp y tế'로만 번역",
                "correction": "'điều chỉnh/hòa giải tranh chấp y tế' - 조정/중재 개념 포함하여 번역",
                "explanation": "조정은 법적 소송과 다른 대안적 분쟁 해결 방식임을 명확히"
            },
            {
                "mistake": "통역사가 법률 자문을 제공",
                "correction": "제도 안내만 하고, 구체적 법률 상담은 전문가에게 연결",
                "explanation": "통역사는 법률 전문가가 아니므로 역할 범위 준수 필요"
            },
            {
                "mistake": "외국인은 이용할 수 없다고 안내",
                "correction": "외국인도 무료로 이용 가능 - 한국어 통역 지원도 받을 수 있음",
                "explanation": "환자의 권리를 보호하기 위해 정확한 정보 제공 필수"
            }
        ],
        "examples": [
            {
                "ko": "의료사고가 있었다면 의료분쟁조정중재원에 신청하실 수 있습니다.",
                "vi": "Nếu có tai nạn y tế, bạn có thể nộp đơn đến Trung tâm Hòa giải Tranh chấp Y tế.",
                "situation": "formal"
            },
            {
                "ko": "의료분쟁조정은 무료이고 소송보다 빠릅니다.",
                "vi": "Hòa giải tranh chấp y tế miễn phí và nhanh hơn kiện tụng.",
                "situation": "onsite"
            },
            {
                "ko": "외국인 환자도 통역 지원을 받으며 의료분쟁조정을 신청할 수 있어요.",
                "vi": "Bệnh nhân nước ngoài cũng có thể đăng ký hòa giải với hỗ trợ thông dịch.",
                "situation": "informal"
            }
        ],
        "relatedTerms": ["의료과오", "환자안전", "환자권리장전"]
    },
    {
        "slug": "sai-sot-y-khoa",
        "korean": "의료과오",
        "vietnamese": "sai sót y khoa",
        "hanja": "醫療過誤",
        "hanjaReading": "의(의원 의) + 료(고칠 료) + 과(지날 과) + 오(그릇 오)",
        "pronunciation": "uiryo-gwao",
        "meaningKo": "의료인이 의료 행위 중 주의 의무를 다하지 못해 환자에게 피해를 입힌 과실을 말합니다. 오진, 수술 실수, 약물 투여 오류, 감염 관리 소홀 등이 해당되며, 법적 책임을 물을 수 있습니다. 통역 시 주의할 점은 환자가 단순히 치료 결과가 좋지 않다고 모두 의료과오는 아니며, 의료인의 '과실'이 입증되어야 한다는 점입니다. 통역사는 환자의 불만을 경청하되, 의료과오 여부를 판단하거나 법적 조언을 해서는 안 되며, 전문 기관(의료분쟁조정중재원 등)을 안내하는 것이 적절합니다.",
        "meaningVi": "Sai sót của nhân viên y tế trong quá trình khám chữa bệnh do không thực hiện đầy đủ nghĩa vụ cẩn trọng, gây thiệt hại cho bệnh nhân. Bao gồm chẩn đoán sai, lỗi phẫu thuật, sai sót trong dùng thuốc, lơ là kiểm soát nhiễm khuẩn, v.v.",
        "context": "의료사고, 법적 책임, 환자 보호",
        "culturalNote": "한국은 의료과오에 대한 법적 기준과 환자 보호 제도가 베트남보다 엄격하고 체계적입니다. 환자가 의료과오를 주장할 경우 감정적으로 대응하기보다는 객관적 사실 확인과 전문 기관 연계가 중요합니다. 통역사는 중립을 유지하며 양측의 의사소통을 돕는 역할에 충실해야 합니다.",
        "commonMistakes": [
            {
                "mistake": "의료과오를 단순히 'lỗi bác sĩ'로 번역",
                "correction": "'sai sót y khoa' 또는 'lỗi nghiệp vụ y tế' - 전문 용어로 번역",
                "explanation": "법적 개념이므로 정확한 전문 용어 사용 필요"
            },
            {
                "mistake": "통역사가 의료과오 여부를 판단",
                "correction": "환자의 주장을 있는 그대로 통역하되, 판단은 의료인과 전문가에게",
                "explanation": "통역사는 판단이나 평가를 해서는 안 되며 중립 유지 필수"
            },
            {
                "mistake": "환자의 감정적 불만을 그대로 통역하여 갈등 증폭",
                "correction": "핵심 내용은 정확히 전달하되, 불필요한 감정적 표현은 순화",
                "explanation": "통역사는 갈등 완화와 원활한 의사소통을 돕는 역할"
            }
        ],
        "examples": [
            {
                "ko": "이것이 의료과오인지는 전문 기관의 판단이 필요합니다.",
                "vi": "Việc này có phải là sai sót y khoa hay không cần cơ quan chuyên môn xác định.",
                "situation": "formal"
            },
            {
                "ko": "의료과오가 의심되면 의료분쟁조정중재원에 신청할 수 있습니다.",
                "vi": "Nếu nghi ngờ có sai sót y khoa, có thể nộp đơn đến Trung tâm Hòa giải Tranh chấp Y tế.",
                "situation": "onsite"
            },
            {
                "ko": "치료 결과가 좋지 않다고 해서 모두 의료과오는 아니에요.",
                "vi": "Kết quả điều trị không tốt không có nghĩa là có sai sót y khoa.",
                "situation": "informal"
            }
        ],
        "relatedTerms": ["의료분쟁조정", "환자안전", "의료사고"]
    },
    {
        "slug": "an-toan-benh-nhan",
        "korean": "환자안전",
        "vietnamese": "an toàn bệnh nhân",
        "hanja": "患者安全",
        "hanjaReading": "환(근심 환) + 자(사람 자) + 안(편안할 안) + 전(온전할 전)",
        "pronunciation": "hwanja-anjeon",
        "meaningKo": "의료 과정에서 환자에게 발생할 수 있는 위해를 예방하고, 안전한 의료 환경을 조성하기 위한 모든 활동을 말합니다. 낙상 예방, 환자 확인, 투약 안전, 감염 관리, 수술 안전 등이 포함됩니다. 통역 시 주의할 점은 환자안전은 의료인만의 책임이 아니라 환자와 보호자의 협조도 필요하므로, 안전 수칙(낙상 주의, 정확한 약물 복용, 증상 변화 보고 등)을 명확히 전달해야 합니다. 외국인 환자는 언어 장벽으로 안전 지침을 이해하지 못해 사고 위험이 높으므로, 통역사의 정확하고 이해하기 쉬운 설명이 매우 중요합니다.",
        "meaningVi": "Tất cả hoạt động nhằm ngăn ngừa các nguy cơ có thể xảy ra với bệnh nhân trong quá trình khám chữa bệnh và tạo môi trường y tế an toàn. Bao gồm phòng ngừa té ngã, xác minh bệnh nhân, an toàn dùng thuốc, kiểm soát nhiễm khuẩn, an toàn phẫu thuật, v.v.",
        "context": "병원 안전 관리, 환자 교육, 의료 질 향상",
        "culturalNote": "한국 병원은 환자안전에 대한 체계가 베트남보다 엄격하여, 낙상 예방 밴드, 환자 확인 절차, 약물 바코드 스캔 등 다양한 안전 장치가 있습니다. 외국인 환자는 이러한 절차가 번거롭다고 느낄 수 있으나, 환자 보호를 위한 것임을 이해시켜야 합니다.",
        "commonMistakes": [
            {
                "mistake": "환자안전을 단순히 'an toàn'으로만 번역",
                "correction": "'an toàn bệnh nhân' - 환자 중심의 안전임을 명확히",
                "explanation": "일반적인 안전과 환자안전은 의료 맥락에서 구분 필요"
            },
            {
                "mistake": "안전 수칙을 형식적으로만 통역",
                "correction": "환자가 실제로 이해하고 실천할 수 있도록 구체적 예시 포함하여 설명",
                "explanation": "언어 장벽이 있는 환자에게는 더 명확하고 반복적인 설명 필요"
            },
            {
                "mistake": "낙상 위험 안내를 대수롭지 않게 통역",
                "correction": "낙상 사고의 심각성과 예방 방법을 강조하여 전달",
                "explanation": "외국인 환자는 낙상 위험을 과소평가하는 경향이 있어 강조 필요"
            }
        ],
        "examples": [
            {
                "ko": "환자안전을 위해 이름과 생년월일을 확인하겠습니다.",
                "vi": "Để đảm bảo an toàn bệnh nhân, chúng tôi sẽ xác nhận tên và ngày sinh.",
                "situation": "formal"
            },
            {
                "ko": "낙상 예방을 위해 침대 난간을 올려주세요.",
                "vi": "Để phòng ngừa té ngã, vui lòng kéo thanh chắn giường lên.",
                "situation": "onsite"
            },
            {
                "ko": "증상이 악화되면 즉시 간호사를 불러주세요. 환자안전이 최우선입니다.",
                "vi": "Nếu triệu chứng xấu đi, hãy gọi y tá ngay. An toàn bệnh nhân là ưu tiên hàng đầu.",
                "situation": "informal"
            }
        ],
        "relatedTerms": ["감염관리", "낙상예방", "투약안전"]
    },
    {
        "slug": "kiem-soat-nhiem-khuan",
        "korean": "감염관리",
        "vietnamese": "kiểm soát nhiễm khuẩn",
        "hanja": "感染管理",
        "hanjaReading": "감(느낄 감) + 염(물들 염) + 관(꿰뚫을 관) + 리(다스릴 리)",
        "pronunciation": "gamyeom-gwalli",
        "meaningKo": "병원 내에서 감염병이 전파되는 것을 예방하고 관리하는 모든 활동을 말합니다. 손 위생, 격리, 소독, 멸균, 개인보호구 착용, 환기 등이 포함되며, 특히 COVID-19 이후 더욱 강화되었습니다. 통역 시 주의할 점은 환자와 보호자도 감염 관리에 협조해야 하므로, 손 씻기, 마스크 착용, 면회 제한, 격리 수칙 등을 명확히 전달해야 합니다. 외국인 환자가 문화적 차이로 감염 관리 수칙을 이해하지 못하거나 불편해할 수 있으나, 모든 환자의 안전을 위해 필수임을 설명해야 합니다.",
        "meaningVi": "Tất cả hoạt động nhằm ngăn ngừa và quản lý sự lây lan bệnh truyền nhiễm trong bệnh viện. Bao gồm vệ sinh tay, cách ly, khử trùng, tiệt trùng, đeo đồ bảo hộ cá nhân, thông gió, v.v. Đặc biệt được tăng cường sau COVID-19.",
        "context": "병원 위생, 감염병 예방, 환자 보호",
        "culturalNote": "한국 병원의 감염 관리 수준은 베트남보다 엄격하며, 손 소독제 사용, 마스크 착용, 면회 제한 등이 철저합니다. 베트남에서는 가족이 환자 곁에서 상주하며 돌보는 것이 일반적이나, 한국은 감염 관리를 위해 면회를 제한하는 경우가 많아 환자와 가족이 불편해할 수 있으므로 이유를 설명해야 합니다.",
        "commonMistakes": [
            {
                "mistake": "감염관리를 단순히 'phòng ngừa bệnh'로 번역",
                "correction": "'kiểm soát nhiễm khuẩn' 또는 'quản lý nhiễm trùng' - 전문 용어로 번역",
                "explanation": "감염관리는 체계적 관리 시스템이므로 정확한 용어 사용 필요"
            },
            {
                "mistake": "손 위생 수칙을 형식적으로만 안내",
                "correction": "언제, 어떻게 손을 씻어야 하는지 구체적으로 설명하고 시범 보이기",
                "explanation": "문화적 차이로 손 위생 습관이 다를 수 있어 구체적 교육 필요"
            },
            {
                "mistake": "면회 제한을 병원의 불친절로 오해하도록 통역",
                "correction": "감염 예방을 위한 필수 조치임을 강조하고 이해 구하기",
                "explanation": "환자와 가족의 협조를 얻기 위해 이유 설명 중요"
            }
        ],
        "examples": [
            {
                "ko": "감염관리를 위해 병실 출입 전후에 손 소독을 해주세요.",
                "vi": "Để kiểm soát nhiễm khuẩn, vui lòng rửa tay trước và sau khi vào phòng bệnh.",
                "situation": "formal"
            },
            {
                "ko": "격리 환자이므로 면회가 제한됩니다. 감염 확산 방지를 위함입니다.",
                "vi": "Do bệnh nhân được cách ly nên hạn chế thăm nuôi. Đây là biện pháp ngăn lây lan nhiễm khuẩn.",
                "situation": "onsite"
            },
            {
                "ko": "병원 감염 예방을 위해 모든 직원과 방문객은 마스크를 착용해야 해요.",
                "vi": "Để phòng ngừa nhiễm khuẩn trong bệnh viện, tất cả nhân viên và khách phải đeo khẩu trang.",
                "situation": "informal"
            }
        ],
        "relatedTerms": ["환자안전", "손위생", "격리"]
    },
    {
        "slug": "thong-dich-y-te",
        "korean": "의료통역",
        "vietnamese": "thông dịch y tế",
        "hanja": "醫療通譯",
        "hanjaReading": "의(의원 의) + 료(고칠 료) + 통(통할 통) + 역(번역할 역)",
        "pronunciation": "uiryo-tongnyeok",
        "meaningKo": "의료 현장에서 서로 다른 언어를 사용하는 의료인과 환자 간의 의사소통을 돕는 전문 통역입니다. 단순한 언어 변환을 넘어 의학 용어에 대한 정확한 이해, 문화적 차이 고려, 의료 윤리 준수가 필요합니다. 통역 시 주의할 점은 의료통역사는 중립을 유지하고, 환자의 말을 있는 그대로 전달하되 의학 용어는 정확히 통역해야 합니다. 또한 비밀유지 의무가 있으며, 환자를 대신하여 결정을 내리거나 의료 자문을 제공해서는 안 됩니다. 의료통역사의 역할과 한계를 명확히 인식하는 것이 중요합니다.",
        "meaningVi": "Thông dịch chuyên môn giúp giao tiếp giữa nhân viên y tế và bệnh nhân sử dụng ngôn ngữ khác nhau tại cơ sở y tế. Không chỉ chuyển đổi ngôn ngữ mà cần hiểu chính xác thuật ngữ y học, xem xét sự khác biệt văn hóa và tuân thủ đạo đức y tế.",
        "context": "의료 현장, 외국인 환자 진료, 국제 진료",
        "culturalNote": "한국의 의료통역은 베트남보다 전문화되어 있으며, 의료통역사 자격증 제도가 있습니다. 베트남에서는 가족이나 친구가 비공식적으로 통역하는 경우가 많지만, 한국은 전문 의료통역사 활용이 증가하고 있습니다. 의료통역사는 단순 통역이 아닌 문화 중재자 역할도 하므로 높은 전문성이 요구됩니다.",
        "commonMistakes": [
            {
                "mistake": "의료통역을 단순히 'phiên dịch'로 번역",
                "correction": "'thông dịch y tế' 또는 'thông dịch viên y tế chuyên nghiệp' - 전문성 강조",
                "explanation": "의료통역은 일반 통역과 달리 의학 지식과 윤리가 필요한 전문 분야"
            },
            {
                "mistake": "통역사가 환자를 대신하여 의사결정",
                "correction": "환자의 말을 정확히 전달하되, 결정은 환자 본인이 하도록 안내",
                "explanation": "통역사는 중립적 전달자이며 의사결정 주체가 아님"
            },
            {
                "mistake": "의학 용어를 이해하지 못하면서 추측하여 통역",
                "correction": "모르는 용어는 솔직히 확인하고 정확히 통역",
                "explanation": "잘못된 의학 정보 전달은 환자 안전에 치명적일 수 있음"
            }
        ],
        "examples": [
            {
                "ko": "의료통역사가 동행하여 정확한 진료가 가능합니다.",
                "vi": "Với sự hỗ trợ của thông dịch viên y tế, có thể khám chữa bệnh chính xác.",
                "situation": "formal"
            },
            {
                "ko": "저는 의료통역사로서 비밀유지 의무가 있습니다.",
                "vi": "Tôi là thông dịch viên y tế và có nghĩa vụ bảo mật.",
                "situation": "onsite"
            },
            {
                "ko": "의료통역사는 환자의 말을 그대로 전달하며, 개인 의견은 말하지 않아요.",
                "vi": "Thông dịch viên y tế chuyển tải đúng lời bệnh nhân, không nêu ý kiến cá nhân.",
                "situation": "informal"
            }
        ],
        "relatedTerms": ["동시통역", "순차통역", "의료통역윤리"]
    }
]

# Read existing data
with open(file_path, 'r', encoding='utf-8') as f:
    data = json.load(f)

# Add new terms
data.extend(new_terms)

# Write back
with open(file_path, 'w', encoding='utf-8') as f:
    json.dump(data, f, ensure_ascii=False, indent=2)

print(f"✅ Successfully added {len(new_terms)} new medical terms to medical.json")
print(f"📊 Total terms now: {len(data)}")
