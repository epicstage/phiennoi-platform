import json
import os

# File path setup
file_path = os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', 'data', 'terms', 'medical.json')

# Load existing data
with open(file_path, 'r', encoding='utf-8') as f:
    data = json.load(f)

existing_slugs = {t['slug'] for t in data}

# New terms to add
new_terms = [
    {
        "slug": "goi-kham-suc-khoe",
        "korean": "건강검진패키지",
        "vietnamese": "Gói khám sức khỏe",
        "hanja": "健康檢診package",
        "hanjaReading": "健(건강할 건) 康(편안할 강) 檢(조사할 검) 診(진찰할 진)",
        "pronunciation": "건강검진패키지",
        "meaningKo": "여러 검사 항목을 묶어 제공하는 종합 건강검진 상품. 베트남에서는 'gói' 개념이 익숙하므로 통역 시 '패키지'를 그대로 사용하기보다 'gói khám tổng quát'로 풀어 설명하는 것이 효과적입니다. 한국의 건강검진센터는 기본/프리미엄/VIP 등 등급별로 나뉘므로, 베트남 환자에게 각 패키지에 포함된 검사 항목을 구체적으로 설명해야 오해를 막을 수 있습니다. 가격 차이가 크므로 사전 안내가 중요합니다.",
        "meaningVi": "Gói dịch vụ khám sức khỏe tổng quát bao gồm nhiều hạng mục xét nghiệm và kiểm tra được thiết kế sẵn theo từng mức độ. Tại Hàn Quốc, các trung tâm khám sức khỏe cung cấp nhiều loại gói từ cơ bản đến cao cấp, khác với hệ thống khám theo yêu cầu ở Việt Nam.",
        "context": "의료관광, 건강검진센터, 예방의학",
        "culturalNote": "한국은 건강검진이 매우 체계화되어 국가건강검진과 민간 프리미엄 검진이 구분되지만, 베트남은 아직 패키지 개념이 덜 발달했습니다. 한국의 '당일 종합검진' 시스템은 베트남 환자에게 매우 새로운 경험이므로, 검진 소요시간, 식사 제공 여부, 결과 상담 절차를 사전에 명확히 안내해야 합니다.",
        "commonMistakes": [
            {
                "mistake": "패키지를 'package'로 음차",
                "correction": "gói khám sức khỏe 또는 gói khám tổng quát",
                "explanation": "베트남어에서 'package'는 일상어가 아니므로 'gói'로 자연스럽게 번역"
            },
            {
                "mistake": "검진 항목을 일일이 나열하지 않음",
                "correction": "포함된 검사 항목을 구체적으로 설명",
                "explanation": "베트남 환자는 패키지 구성을 잘 모르므로 상세 설명 필요"
            },
            {
                "mistake": "기본/프리미엄 등급을 단순 번역",
                "correction": "각 등급별 차이점을 비교 설명",
                "explanation": "가격 차이가 크므로 등급별 혜택을 명확히 구분해야 함"
            }
        ],
        "examples": [
            {
                "ko": "기본 건강검진패키지는 50만원이며 혈액검사와 영상검사가 포함됩니다",
                "vi": "Gói khám sức khỏe cơ bản có giá 500,000 won, bao gồm xét nghiệm máu và chụp hình ảnh học",
                "situation": "formal"
            },
            {
                "ko": "프리미엄 패키지는 MRI와 내시경 검사까지 포함돼요",
                "vi": "Gói cao cấp bao gồm cả chụp MRI và nội soi",
                "situation": "onsite"
            },
            {
                "ko": "당일 검진 가능한 패키지로 예약하시겠어요?",
                "vi": "Anh/chị muốn đặt gói khám trong ngày không ạ?",
                "situation": "informal"
            }
        ],
        "relatedTerms": ["종합건강검진", "건강검진센터", "예방의학", "조기진단"]
    },
    {
        "slug": "kham-benh-tu-xa",
        "korean": "원격진료",
        "vietnamese": "Khám bệnh từ xa",
        "hanja": "遠隔診療",
        "hanjaReading": "遠(멀 원) 隔(사이뜰 격) 診(진찰할 진) 療(치료할 료)",
        "pronunciation": "원격진료",
        "meaningKo": "정보통신기술을 활용하여 의사가 환자를 직접 대면하지 않고 진료하는 방식. 통역 시 주의할 점은 한국은 원격진료가 법적으로 제한적이지만 코로나19 이후 한시적으로 허용되었다는 점입니다. 베트남 환자에게는 '화상 진료' 개념으로 설명하되, 한국에서는 초진은 반드시 대면이어야 하고 재진만 원격 가능하다는 점을 명확히 해야 합니다. 처방전 발급과 약 배송 절차도 함께 안내해야 합니다.",
        "meaningVi": "Hình thức khám chữa bệnh mà bác sĩ không trực tiếp gặp mặt bệnh nhân mà sử dụng công nghệ thông tin. Ở Hàn Quốc, khám bệnh từ xa có những hạn chế về mặt pháp lý và chỉ áp dụng cho tái khám, không áp dụng cho khám lần đầu.",
        "context": "디지털헬스케어, 비대면진료, 의료법",
        "culturalNote": "한국은 의사협회의 반대로 원격진료가 제한적이지만, 베트남은 지리적 특성상 원격진료가 더 활성화되어 있습니다. 한국 환자는 원격진료를 불완전한 진료로 인식하는 경향이 있으나, 베트남에서는 실용적 대안으로 받아들여집니다. 통역 시 한국 의료법상 제약사항을 정확히 전달해야 환자가 오해하지 않습니다.",
        "commonMistakes": [
            {
                "mistake": "초진도 원격 가능하다고 안내",
                "correction": "초진은 대면 필수, 재진만 원격 가능",
                "explanation": "한국 의료법상 원격진료는 재진에만 허용됨"
            },
            {
                "mistake": "telemedicine을 그대로 음차",
                "correction": "khám bệnh từ xa 또는 khám qua video",
                "explanation": "베트남어로 자연스럽게 풀어 설명"
            },
            {
                "mistake": "처방전 수령 방법을 설명하지 않음",
                "correction": "약 배송 또는 약국 방문 절차 안내",
                "explanation": "원격진료 후 처방전 처리 과정이 중요함"
            }
        ],
        "examples": [
            {
                "ko": "원격진료는 재진 환자만 가능하며 초진은 직접 방문하셔야 합니다",
                "vi": "Khám bệnh từ xa chỉ áp dụng cho bệnh nhân tái khám, lần khám đầu tiên phải đến trực tiếp",
                "situation": "formal"
            },
            {
                "ko": "화상으로 진료받으시고 처방전은 문자로 받으실 수 있어요",
                "vi": "Anh/chị khám qua video và nhận đơn thuốc qua tin nhắn",
                "situation": "onsite"
            },
            {
                "ko": "원격진료 예약은 앱에서 할 수 있습니다",
                "vi": "Có thể đặt lịch khám từ xa qua ứng dụng",
                "situation": "informal"
            }
        ],
        "relatedTerms": ["비대면진료", "화상진료", "디지털헬스케어", "전자처방전"]
    },
    {
        "slug": "y-kien-bac-si-thu-hai",
        "korean": "세컨드오피니언",
        "vietnamese": "Ý kiến bác sĩ thứ hai",
        "hanja": None,
        "hanjaReading": None,
        "pronunciation": "세컨드오피니언",
        "meaningKo": "환자가 첫 번째 의사의 진단이나 치료 방침에 대해 다른 의사의 의견을 구하는 것. 통역 시 핵심은 이것이 불신의 표현이 아니라 환자의 정당한 권리임을 강조하는 것입니다. 한국에서는 중증질환 시 세컨드오피니언이 일반화되어 있으나, 베트남 문화에서는 의사에 대한 예의 문제로 받아들여질 수 있습니다. '추가 전문의 상담'으로 부드럽게 표현하면 문화적 거부감을 줄일 수 있습니다.",
        "meaningVi": "Việc bệnh nhân tìm kiếm ý kiến của bác sĩ khác về chẩn đoán hoặc phương án điều trị của bác sĩ đầu tiên. Đây là quyền hợp pháp của bệnh nhân, đặc biệt quan trọng trong các trường hợp bệnh nặng hoặc phẫu thuật lớn.",
        "context": "환자권리, 중증질환, 수술 결정",
        "culturalNote": "한국에서는 암이나 중증질환 진단 시 세컨드오피니언을 구하는 것이 매우 일반적이고 의료진도 권장하지만, 베트남에서는 의사-환자 관계에서 위계가 강해 세컨드오피니언 요청이 무례하다고 여겨질 수 있습니다. 통역 시 '더 나은 치료를 위한 추가 상담'으로 프레이밍하면 양측 모두 편안하게 받아들입니다.",
        "commonMistakes": [
            {
                "mistake": "'두 번째 의견'으로 직역",
                "correction": "ý kiến bác sĩ thứ hai 또는 tham khảo thêm chuyên gia",
                "explanation": "전문 용어로 정확히 표현해야 함"
            },
            {
                "mistake": "환자가 의사를 불신한다고 오해받음",
                "correction": "환자 권리이자 신중한 결정 과정임을 설명",
                "explanation": "문화적 맥락에서 긍정적으로 프레이밍"
            },
            {
                "mistake": "보험 적용 여부를 확인하지 않음",
                "correction": "세컨드오피니언 비용 및 보험 처리 안내",
                "explanation": "추가 비용이 발생할 수 있으므로 사전 안내 필요"
            }
        ],
        "examples": [
            {
                "ko": "중증 질환이므로 다른 전문의의 세컨드오피니언을 받아보시는 것을 권장합니다",
                "vi": "Vì bệnh nặng, chúng tôi khuyến khích anh/chị tham khảo thêm ý kiến của bác sĩ chuyên khoa khác",
                "situation": "formal"
            },
            {
                "ko": "수술 결정 전에 다른 병원 의견도 들어보시겠어요?",
                "vi": "Trước khi quyết định phẫu thuật, anh/chị có muốn nghe ý kiến bệnh viện khác không?",
                "situation": "onsite"
            },
            {
                "ko": "세컨드오피니언은 환자의 권리입니다",
                "vi": "Xin ý kiến bác sĩ thứ hai là quyền của bệnh nhân",
                "situation": "informal"
            }
        ],
        "relatedTerms": ["진단", "환자권리", "치료방침", "전문의상담"]
    },
    {
        "slug": "visa-du-lich-y-te",
        "korean": "의료관광비자",
        "vietnamese": "Visa du lịch y tế",
        "hanja": "醫療觀光visa",
        "hanjaReading": "醫(의원 의) 療(치료할 료) 觀(볼 관) 光(빛 광)",
        "pronunciation": "의료관광비자",
        "meaningKo": "치료 목적으로 한국을 방문하는 외국인에게 발급되는 특별 비자. 통역 시 핵심은 일반 관광비자와의 차이점을 명확히 하는 것입니다. 의료관광비자는 체류기간이 더 길고(최대 90일), 동반자 비자 발급이 용이하며, 초청장 발급 병원이 명시되어야 합니다. 베트남 환자에게는 비자 신청 시 필요한 의료기관 확인서, 진료 예약 증명서, 치료 계획서 등을 미리 준비하도록 안내해야 합니다.",
        "meaningVi": "Visa đặc biệt được cấp cho người nước ngoài đến Hàn Quốc nhằm mục đích điều trị y tế. Visa này có thời hạn lưu trú dài hơn visa du lịch thông thường (tối đa 90 ngày) và thuận tiện cho việc xin visa cho người đi cùng.",
        "context": "출입국관리, 의료관광, 국제진료",
        "culturalNote": "한국은 의료관광 활성화를 위해 비자 발급을 간소화했으나, 베트남인의 경우 여전히 서류 심사가 까다롭습니다. 초청 병원의 신뢰도, 치료비 지불 능력 증명, 귀국 보증이 중요합니다. 통역 시 비자 거절 가능성도 솔직히 안내하여 환자가 대비할 수 있도록 해야 합니다.",
        "commonMistakes": [
            {
                "mistake": "일반 관광비자로 치료 가능하다고 안내",
                "correction": "장기 치료는 의료관광비자 필요",
                "explanation": "비자 유형에 따라 체류 기간과 활동 범위가 다름"
            },
            {
                "mistake": "비자 발급이 자동 승인된다고 오해",
                "correction": "서류 심사 후 승인되며 거절 가능성 있음",
                "explanation": "비자는 승인제이므로 불확실성을 사전 고지해야 함"
            },
            {
                "mistake": "동반자 비자 절차를 설명하지 않음",
                "correction": "환자 비자와 동시 신청 가능하며 별도 서류 필요",
                "explanation": "보호자 동반이 필요한 경우가 많으므로 안내 필수"
            }
        ],
        "examples": [
            {
                "ko": "의료관광비자는 병원 초청장과 치료 계획서가 필요합니다",
                "vi": "Visa du lịch y tế cần có thư mời từ bệnh viện và kế hoạch điều trị",
                "situation": "formal"
            },
            {
                "ko": "비자 신청 후 승인까지 2주 정도 걸려요",
                "vi": "Sau khi nộp hồ sơ xin visa, mất khoảng 2 tuần để được phê duyệt",
                "situation": "onsite"
            },
            {
                "ko": "보호자분도 같이 비자 신청 가능합니다",
                "vi": "Người đi cùng cũng có thể xin visa cùng lúc",
                "situation": "informal"
            }
        ],
        "relatedTerms": ["의료관광", "초청장", "체류기간", "동반자비자"]
    },
    {
        "slug": "phien-dich-vien-y-te",
        "korean": "의료통역사",
        "vietnamese": "Phiên dịch viên y tế",
        "hanja": "醫療通譯士",
        "hanjaReading": "醫(의원 의) 療(치료할 료) 通(통할 통) 譯(번역할 역) 士(선비 사)",
        "pronunciation": "의료통역사",
        "meaningKo": "의료 현장에서 환자와 의료진 간 언어 소통을 돕는 전문 통역사. 통역 시 강조할 점은 단순 언어 변환이 아니라 의학 용어 전문성, 의료 윤리, 환자 권리 옹호 역할을 모두 수행한다는 것입니다. 베트남 환자에게는 의료통역사가 진단을 내리거나 의학적 조언을 하지 않으며, 오직 정확한 의사소통만 담당한다는 점을 명확히 해야 합니다. 한국에서는 아직 의료통역사 국가자격이 없어 민간 자격증이나 병원 자체 교육으로 양성됩니다.",
        "meaningVi": "Người phiên dịch chuyên nghiệp hỗ trợ giao tiếp giữa bệnh nhân và nhân viên y tế tại các cơ sở y tế. Họ không chỉ phiên dịch ngôn ngữ mà còn cần am hiểu thuật ngữ y khoa, đạo đức y tế và quyền lợi của bệnh nhân.",
        "context": "국제진료, 의료관광, 환자안전",
        "culturalNote": "한국의 대형병원은 주요 언어별 의료통역사를 고용하지만, 중소병원은 외부 통역 서비스를 이용합니다. 베트남에서는 의료통역사 개념이 생소하여, 가족이나 지인이 통역하는 경우가 많습니다. 통역 시 전문 의료통역사 이용의 중요성(정확성, 비밀보장, 법적 보호)을 강조해야 합니다.",
        "commonMistakes": [
            {
                "mistake": "일반 통역사와 동일하게 취급",
                "correction": "의학 용어와 의료 윤리 교육을 받은 전문 통역사",
                "explanation": "의료통역은 전문성과 책임이 다름"
            },
            {
                "mistake": "통역사가 의학적 조언을 한다고 오해",
                "correction": "통역사는 중립적 전달자이며 조언하지 않음",
                "explanation": "역할 범위를 명확히 해야 환자 혼란 방지"
            },
            {
                "mistake": "비밀 보장 의무를 설명하지 않음",
                "correction": "의료통역사는 환자 정보 비밀 유지 의무가 있음",
                "explanation": "환자가 안심하고 솔직히 증상을 말할 수 있도록"
            }
        ],
        "examples": [
            {
                "ko": "의료통역사는 의학 용어를 정확히 전달하며 환자 정보를 철저히 보호합니다",
                "vi": "Phiên dịch viên y tế truyền đạt chính xác thuật ngữ y khoa và bảo mật thông tin bệnh nhân",
                "situation": "formal"
            },
            {
                "ko": "통역사는 진단하지 않고 의사 말씀만 전달해요",
                "vi": "Phiên dịch viên không chẩn đoán mà chỉ truyền đạt lời bác sĩ",
                "situation": "onsite"
            },
            {
                "ko": "병원에서 제공하는 통역사 서비스를 이용하시면 안전합니다",
                "vi": "Sử dụng dịch vụ phiên dịch của bệnh viện sẽ an toàn hơn",
                "situation": "informal"
            }
        ],
        "relatedTerms": ["국제진료", "의료관광", "환자안전", "언어장벽"]
    },
    {
        "slug": "hoa-giai-tranh-chap-y-te",
        "korean": "의료분쟁조정",
        "vietnamese": "Hòa giải tranh chấp y tế",
        "hanja": "醫療紛爭調停",
        "hanjaReading": "醫(의원 의) 療(치료할 료) 紛(어지러울 분) 爭(다툴 쟁) 調(고를 조) 停(머무를 정)",
        "pronunciation": "의료분쟁조정",
        "meaningKo": "의료사고 발생 시 환자와 의료기관 간 분쟁을 법정 소송 없이 조정 절차를 통해 해결하는 제도. 통역 시 중요한 점은 한국의료분쟁조정중재원이 공정한 제3자 기관이며, 무료로 이용 가능하고, 조정 결과는 법적 효력이 있다는 것입니다. 베트남 환자에게는 소송보다 빠르고 비용 부담이 적으며, 의료 전문가가 참여하여 공정한 판단을 받을 수 있다는 점을 강조해야 합니다. 조정 신청 기한과 필요 서류도 명확히 안내해야 합니다.",
        "meaningVi": "Chế độ giải quyết tranh chấp giữa bệnh nhân và cơ sở y tế thông qua trung gian hòa giải thay vì kiện tụng. Tại Hàn Quốc, Cơ quan Trung gian và Hòa giải Tranh chấp Y tế cung cấp dịch vụ miễn phí và kết quả hòa giải có hiệu lực pháp lý.",
        "context": "의료사고, 환자권리, 법률",
        "culturalNote": "한국은 의료분쟁조정제도가 법으로 제도화되어 있으나, 베트남은 아직 체계가 미흡합니다. 베트남 환자는 의료사고 시 직접 소송하거나 포기하는 경우가 많아, 조정 제도의 존재 자체를 모르는 경우가 많습니다. 통역 시 이 제도가 환자 보호를 위한 안전장치임을 강조하고, 신청 방법을 구체적으로 안내해야 합니다.",
        "commonMistakes": [
            {
                "mistake": "조정이 의료기관 편을 든다고 오해",
                "correction": "중립적 제3자 기관이 공정하게 판단",
                "explanation": "환자가 불신하지 않도록 공정성 강조"
            },
            {
                "mistake": "조정 결과가 권고사항이라고 설명",
                "correction": "조정 성립 시 법적 효력 있음",
                "explanation": "강제력이 있다는 점을 명확히 해야 함"
            },
            {
                "mistake": "신청 기한을 안내하지 않음",
                "correction": "사고 발생 후 10년 이내 신청 가능",
                "explanation": "시효가 있으므로 조기 신청 권장"
            }
        ],
        "examples": [
            {
                "ko": "의료사고 발생 시 한국의료분쟁조정중재원에 무료로 조정 신청할 수 있습니다",
                "vi": "Khi xảy ra sự cố y tế, có thể nộp đơn hòa giải miễn phí tại Cơ quan Trung gian Tranh chấp Y tế Hàn Quốc",
                "situation": "formal"
            },
            {
                "ko": "소송보다 빠르고 비용이 안 들어서 환자에게 유리해요",
                "vi": "Nhanh hơn kiện tụng và không tốn phí nên có lợi cho bệnh nhân",
                "situation": "onsite"
            },
            {
                "ko": "조정 결과에 양측이 동의하면 법적 효력이 생겨요",
                "vi": "Nếu hai bên đồng ý kết quả hòa giải thì có hiệu lực pháp lý",
                "situation": "informal"
            }
        ],
        "relatedTerms": ["의료사고", "환자권리", "손해배상", "한국의료분쟁조정중재원"]
    },
    {
        "slug": "su-co-an-toan-benh-nhan",
        "korean": "환자안전사고",
        "vietnamese": "Sự cố an toàn bệnh nhân",
        "hanja": "患者安全事故",
        "hanjaReading": "患(근심할 환) 者(놈 자) 安(편안할 안) 全(온전할 전) 事(일 사) 故(연고 고)",
        "pronunciation": "환자안전사고",
        "meaningKo": "의료기관에서 환자에게 발생한 사망, 신체적·정신적 손상 또는 질병의 이환 등 예상하지 못한 사건. 통역 시 핵심은 '의료사고'와 '환자안전사고'의 차이를 명확히 하는 것입니다. 환자안전사고는 의료진의 과실 여부와 관계없이 환자에게 발생한 모든 안전 위해 사건을 포함하며, 병원은 이를 보고하고 재발 방지 대책을 마련해야 합니다. 베트남 환자에게는 사고 발생 시 병원의 대응 절차, 보고 의무, 보상 가능성을 안내해야 합니다.",
        "meaningVi": "Sự kiện không mong muốn xảy ra với bệnh nhân tại cơ sở y tế, bao gồm tử vong, tổn thương thể chất/tinh thần hoặc mắc bệnh. Khác với tai nạn y tế, sự cố an toàn bệnh nhân bao gồm mọi sự kiện gây hại cho bệnh nhân, bất kể có lỗi của nhân viên y tế hay không.",
        "context": "환자안전, 병원 관리, 의료 질",
        "culturalNote": "한국은 '환자안전법'으로 사고 보고를 의무화하고 있으나, 베트남은 아직 체계가 미흡합니다. 한국 병원은 사고 발생 시 환자에게 즉시 고지하고 재발 방지 대책을 수립해야 하지만, 베트남에서는 사고 은폐나 축소 보고가 문제됩니다. 통역 시 한국의 투명한 사고 보고 문화를 설명하여 환자가 안심할 수 있도록 해야 합니다.",
        "commonMistakes": [
            {
                "mistake": "'의료사고'와 혼용",
                "correction": "환자안전사고는 과실 여부 무관, 의료사고는 과실 포함",
                "explanation": "법적 정의가 다르므로 정확히 구분해야 함"
            },
            {
                "mistake": "사고 발생을 환자에게 숨긴다고 오해",
                "correction": "한국은 환자안전법으로 즉시 고지 의무 있음",
                "explanation": "투명한 보고 문화를 강조하여 신뢰 구축"
            },
            {
                "mistake": "보상 절차를 안내하지 않음",
                "correction": "사고 조사 후 손해배상 또는 조정 절차 안내",
                "explanation": "환자가 권리를 알고 대응할 수 있도록"
            }
        ],
        "examples": [
            {
                "ko": "환자안전사고 발생 시 병원은 즉시 환자에게 고지하고 재발 방지 대책을 수립해야 합니다",
                "vi": "Khi xảy ra sự cố an toàn bệnh nhân, bệnh viện phải thông báo ngay cho bệnh nhân và lập kế hoạch phòng ngừa tái phát",
                "situation": "formal"
            },
            {
                "ko": "낙상 사고도 환자안전사고에 포함돼요",
                "vi": "Tai nạn ngã cũng được tính là sự cố an toàn bệnh nhân",
                "situation": "onsite"
            },
            {
                "ko": "사고 내용은 환자안전보고 시스템에 기록됩니다",
                "vi": "Nội dung sự cố được ghi vào hệ thống báo cáo an toàn bệnh nhân",
                "situation": "informal"
            }
        ],
        "relatedTerms": ["환자안전법", "의료사고", "재발방지", "안전보고시스템"]
    },
    {
        "slug": "kiem-soat-nhiem-khuan",
        "korean": "감염관리",
        "vietnamese": "Kiểm soát nhiễm khuẩn",
        "hanja": "感染管理",
        "hanjaReading": "感(느낄 감) 染(물들 염) 管(대롱 관) 理(다스릴 리)",
        "pronunciation": "감염관리",
        "meaningKo": "의료기관 내 감염병 발생과 전파를 예방하고 관리하는 체계적인 활동. 통역 시 강조할 점은 한국 병원의 철저한 감염관리 시스템입니다. 손위생, 개인보호구 착용, 환경 소독, 격리 지침 등을 엄격히 준수하며, 감염관리실과 전담 간호사가 있습니다. 베트남 환자에게는 면회 제한, 보호자 출입 통제 등이 감염관리의 일환임을 설명하여 협조를 구해야 합니다. 코로나19 이후 더욱 엄격해진 기준도 안내해야 합니다.",
        "meaningVi": "Hoạt động hệ thống nhằm phòng ngừa và quản lý sự phát sinh và lây lan bệnh nhiễm trùng trong cơ sở y tế. Bao gồm vệ sinh tay, sử dụng trang bị bảo hộ cá nhân, khử trùng môi trường và hướng dẫn cách ly.",
        "context": "병원 관리, 감염병 예방, 환자안전",
        "culturalNote": "한국 병원은 감염관리 기준이 매우 엄격하여 면회 시간 제한, 보호자 1인 원칙, 신발 갈아신기 등을 철저히 시행합니다. 베트남에서는 가족 여러 명이 병실에 머무르는 것이 일반적이어서, 한국의 엄격한 규정에 불편을 느낄 수 있습니다. 통역 시 이것이 환자 안전을 위한 것임을 강조하고, 규정 위반 시 퇴원 조치까지 있을 수 있음을 명확히 해야 합니다.",
        "commonMistakes": [
            {
                "mistake": "면회 제한을 불친절로 오해",
                "correction": "감염관리 규정이며 환자 보호가 목적",
                "explanation": "문화 차이를 설명하여 협조 유도"
            },
            {
                "mistake": "손위생을 형식적 절차로 여김",
                "correction": "감염 예방의 가장 중요한 수단",
                "explanation": "중요성을 강조하여 실천 유도"
            },
            {
                "mistake": "격리 환자 차별로 인식",
                "correction": "감염 전파 방지를 위한 의학적 조치",
                "explanation": "격리는 치료의 일부임을 설명"
            }
        ],
        "examples": [
            {
                "ko": "감염관리를 위해 면회는 하루 1회 30분으로 제한됩니다",
                "vi": "Để kiểm soát nhiễm khuẩn, thăm bệnh được giới hạn 1 lần/ngày trong 30 phút",
                "situation": "formal"
            },
            {
                "ko": "병실 들어가기 전에 손 소독제 꼭 사용하세요",
                "vi": "Nhớ dùng nước rửa tay khử trùng trước khi vào phòng bệnh",
                "situation": "onsite"
            },
            {
                "ko": "격리 환자는 보호자도 보호구 착용이 필수예요",
                "vi": "Bệnh nhân cách ly thì người thăm cũng phải mặc đồ bảo hộ",
                "situation": "informal"
            }
        ],
        "relatedTerms": ["손위생", "개인보호구", "격리", "원내감염"]
    },
    {
        "slug": "chat-thai-y-te",
        "korean": "의료폐기물",
        "vietnamese": "Chất thải y tế",
        "hanja": "醫療廢棄物",
        "hanjaReading": "醫(의원 의) 療(치료할 료) 廢(버릴 폐) 棄(버릴 기) 物(만물 물)",
        "pronunciation": "의료폐기물",
        "meaningKo": "의료기관에서 발생하는 감염 위험이 있는 폐기물. 주사기, 수술 도구, 혈액 오염 물질 등이 포함되며, 일반 쓰레기와 달리 특수한 처리 절차를 거쳐야 합니다. 통역 시 중요한 점은 한국의 의료폐기물 처리 시스템이 매우 엄격하다는 것입니다. 색깔별 전용 용기에 분리 배출하고, 전문 처리 업체가 소각하며, 위반 시 법적 처벌을 받습니다. 베트남 환자나 보호자가 병실에서 주사기를 일반 쓰레기통에 버리지 않도록 주의를 주어야 합니다.",
        "meaningVi": "Chất thải phát sinh từ cơ sở y tế có nguy cơ lây nhiễm. Bao gồm kim tiêm, dụng cụ phẫu thuật, vật liệu nhiễm máu, v.v. và phải được xử lý đặc biệt, khác với rác thải thông thường.",
        "context": "병원 관리, 환경보호, 감염예방",
        "culturalNote": "한국은 의료폐기물관리법으로 엄격히 규제하며, 색상별 전용 용기 사용, 처리 업체 등록 등이 의무화되어 있습니다. 베트남은 대도시 병원에서는 관리가 되지만 지방은 체계가 미흡합니다. 한국 병원에서는 환자나 보호자가 의료폐기물을 함부로 다루면 안 되며, 간호사에게 알려야 합니다. 통역 시 이를 명확히 안내해야 합니다.",
        "commonMistakes": [
            {
                "mistake": "주사기를 일반 쓰레기통에 버림",
                "correction": "노란색 전용 용기에 버려야 함",
                "explanation": "감염 위험과 법적 규정 위반"
            },
            {
                "mistake": "약병이나 링거백도 의료폐기물로 오해",
                "correction": "감염 위험 없는 것은 일반 쓰레기",
                "explanation": "불필요한 분리로 혼란 방지"
            },
            {
                "mistake": "환자가 직접 처리한다고 안내",
                "correction": "의료진이나 청소 담당자가 처리",
                "explanation": "안전을 위해 전문 인력이 처리"
            }
        ],
        "examples": [
            {
                "ko": "의료폐기물은 색상별 전용 용기에 분리 배출해야 하며 일반 쓰레기와 섞으면 안 됩니다",
                "vi": "Chất thải y tế phải được bỏ vào thùng chuyên dụng theo màu sắc và không được trộn với rác thông thường",
                "situation": "formal"
            },
            {
                "ko": "사용한 주사기는 노란색 통에 버려주세요",
                "vi": "Kim tiêm đã dùng bỏ vào thùng màu vàng nhé",
                "situation": "onsite"
            },
            {
                "ko": "의료폐기물은 간호사가 처리하니까 건드리지 마세요",
                "vi": "Chất thải y tế do y tá xử lý, đừng động vào",
                "situation": "informal"
            }
        ],
        "relatedTerms": ["감염성폐기물", "격리폐기물", "의료폐기물관리법", "전용용기"]
    },
    {
        "slug": "nhiem-trung-benh-vien",
        "korean": "원내감염",
        "vietnamese": "Nhiễm trùng bệnh viện",
        "hanja": "院內感染",
        "hanjaReading": "院(집 원) 內(안 내) 感(느낄 감) 染(물들 염)",
        "pronunciation": "원내감염",
        "meaningKo": "환자가 병원에 입원한 후 48시간 이후 발생하는 감염. 입원 당시에는 없었던 감염이 병원 환경이나 의료 행위 과정에서 발생한 것을 의미합니다. 통역 시 핵심은 원내감염이 불가피한 경우도 있지만, 병원의 감염관리 노력으로 예방 가능하다는 점입니다. 수술 부위 감염, 요로감염, 폐렴 등이 흔하며, 항생제 내성균 문제가 심각합니다. 베트남 환자에게는 예방을 위해 손위생, 카테터 조기 제거, 조기 보행 등을 적극 협조하도록 안내해야 합니다.",
        "meaningVi": "Nhiễm trùng xảy ra sau 48 giờ kể từ khi bệnh nhân nhập viện. Là nhiễm trùng không có sẵn khi nhập viện mà phát sinh từ môi trường bệnh viện hoặc trong quá trình thực hiện các thủ thuật y tế.",
        "context": "감염관리, 환자안전, 의료 질",
        "culturalNote": "한국은 원내감염률을 중요한 병원 평가 지표로 삼아 철저히 관리하지만, 베트남에서는 아직 통계조차 정확하지 않은 경우가 많습니다. 한국 환자들은 원내감염을 병원의 책임으로 여기는 경향이 있으나, 면역저하 환자에게는 불가피한 측면도 있습니다. 통역 시 예방 가능한 부분과 불가피한 부분을 구분하여 설명하고, 환자 협조 사항을 명확히 해야 합니다.",
        "commonMistakes": [
            {
                "mistake": "원내감염을 모두 병원 잘못으로 단정",
                "correction": "면역저하 환자는 감염 위험이 높으며 불가피한 경우 있음",
                "explanation": "의학적 사실을 정확히 전달해야 함"
            },
            {
                "mistake": "예방법을 안내하지 않음",
                "correction": "손위생, 카테터 조기 제거 등 환자 협조 사항 설명",
                "explanation": "환자가 적극 참여해야 예방 효과"
            },
            {
                "mistake": "항생제 내성균 위험을 경시",
                "correction": "MRSA 등 내성균 감염 시 치료 어려움 강조",
                "explanation": "예방의 중요성을 인식시키기 위해"
            }
        ],
        "examples": [
            {
                "ko": "원내감염 예방을 위해 손 위생을 철저히 하고 카테터는 가능한 빨리 제거합니다",
                "vi": "Để phòng ngừa nhiễm trùng bệnh viện, cần vệ sinh tay kỹ lưỡng và tháo ống thông sớm nhất có thể",
                "situation": "formal"
            },
            {
                "ko": "수술 후 빨리 걷는 게 폐렴 예방에 도움 돼요",
                "vi": "Đi lại sớm sau phẫu thuật giúp phòng ngừa viêm phổi",
                "situation": "onsite"
            },
            {
                "ko": "열이 나면 바로 알려주세요. 원내감염 가능성 확인해야 해요",
                "vi": "Nếu bị sốt thì báo ngay nhé. Phải kiểm tra khả năng nhiễm trùng bệnh viện",
                "situation": "informal"
            }
        ],
        "relatedTerms": ["의료관련감염", "항생제내성균", "감염관리", "환자안전"]
    }
]

# Filter out duplicates
new_terms = [t for t in new_terms if t['slug'] not in existing_slugs]

# Add new terms
data.extend(new_terms)

# Save
with open(file_path, 'w', encoding='utf-8') as f:
    json.dump(data, f, ensure_ascii=False, indent=2)

print(f"✅ Added {len(new_terms)} new medical terms")
print(f"📊 Total terms: {len(data)}")
