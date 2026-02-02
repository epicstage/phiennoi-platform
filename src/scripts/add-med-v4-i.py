import json, os
file_path = os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', 'data', 'terms', 'medical.json')
with open(file_path, 'r', encoding='utf-8') as f:
    data = json.load(f)
existing_slugs = {t['slug'] for t in data}

new_terms = [
    {
        "slug": "giay-dong-y-phau-thuat",
        "korean": "수술동의서",
        "vietnamese": "Giấy đồng ý phẫu thuật",
        "hanja": "手術同意書",
        "hanjaReading": "手(손 수) + 術(재주 술) + 同(한가지 동) + 意(뜻 의) + 書(글 서)",
        "pronunciation": "쑤쑤아트 동이서",
        "meaningKo": "환자가 수술의 필요성, 방법, 위험성 등을 충분히 설명받은 후 자발적으로 동의한다는 내용을 담은 법적 문서입니다. 통역 시 주의할 점은 베트남어 'đồng ý'가 단순 동의가 아닌 법적 책임을 동반하는 동의임을 강조해야 하며, 환자가 서명 전 충분히 이해했는지 확인하는 것이 중요합니다. 베트남에서는 가족 동의도 함께 받는 경우가 많아 한국의 환자 중심 의사결정과 차이가 있음을 설명해야 합니다.",
        "meaningVi": "Giấy đồng ý phẫu thuật là văn bản pháp lý ghi nhận rằng bệnh nhân đã được giải thích đầy đủ về sự cần thiết, phương pháp và rủi ro của ca phẫu thuật, và tự nguyện đồng ý thực hiện.",
        "context": "병원 입원 수속, 수술 전 준비 과정에서 필수적으로 작성하는 문서",
        "culturalNote": "한국에서는 만 19세 이상 성인 환자 본인의 동의만으로 수술이 가능하지만, 베트남에서는 전통적으로 가족(특히 가장)의 의견이 중요하게 작용합니다. 통역 시 한국 의료 시스템에서는 환자 본인의 자기결정권이 최우선임을 설명하되, 가족과 상의하고 싶다는 환자의 요구도 존중해야 합니다. 또한 베트남에서는 수술 동의서가 간소화된 경우가 많아 한국의 상세한 동의서에 당황할 수 있습니다.",
        "commonMistakes": [
            {
                "mistake": "'Giấy cho phép phẫu thuật' (수술 허가서)로 번역",
                "correction": "'Giấy đồng ý phẫu thuật' (수술 동의서)",
                "explanation": "'cho phép'는 상급자가 하급자에게 허락하는 뉘앙스인 반면, 'đồng ý'는 동등한 입장에서의 합의를 의미합니다. 의료 윤리상 환자와 의료진은 동등한 관계입니다."
            },
            {
                "mistake": "환자가 서명만 하면 된다고 단순 안내",
                "correction": "내용을 충분히 이해한 후 서명해야 함을 강조",
                "explanation": "법적 분쟁 시 '충분한 설명을 듣지 못했다'는 주장을 예방하기 위해 통역사는 환자가 내용을 이해했는지 반드시 확인해야 합니다."
            },
            {
                "mistake": "'ký tên' (서명하다)만 사용",
                "correction": "'đồng ý và ký tên' (동의하고 서명하다)",
                "explanation": "서명은 동의의 표현이므로 두 동작을 함께 언급해야 법적 의미가 명확해집니다."
            }
        ],
        "examples": [
            {
                "ko": "수술 전에 수술동의서에 서명하셔야 합니다",
                "vi": "Trước khi phẫu thuật, anh/chị cần đồng ý và ký tên vào giấy đồng ý phẫu thuật",
                "situation": "formal"
            },
            {
                "ko": "동의서 내용 중 이해 안 되는 부분 있으시면 말씀해 주세요",
                "vi": "Nếu có phần nào trong giấy đồng ý anh/chị chưa hiểu rõ, xin vui lòng cho biết",
                "situation": "onsite"
            },
            {
                "ko": "가족분도 함께 보시고 서명하셔도 됩니다",
                "vi": "Gia đình cũng có thể xem và ký tên cùng",
                "situation": "informal"
            }
        ],
        "relatedTerms": ["마취동의서", "진료동의서", "입원동의서", "개인정보동의서"]
    },
    {
        "slug": "giay-dong-y-gay-me",
        "korean": "마취동의서",
        "vietnamese": "Giấy đồng ý gây mê",
        "hanja": "痲醉同意書",
        "hanjaReading": "痲(저릴 마) + 醉(취할 취) + 同(한가지 동) + 意(뜻 의) + 書(글 서)",
        "pronunciation": "마췌 동이서",
        "meaningKo": "전신마취 또는 부분마취를 실시하기 전, 마취의 종류와 방법, 합병증 위험 등을 환자에게 설명하고 동의를 받는 문서입니다. 통역 시 '전신마취(gây mê toàn thân)'와 '부분마취(gây tê cục bộ)'의 차이를 명확히 구분해야 하며, 마취 후 회복 과정과 금식 시간 등 실질적 정보 전달이 중요합니다. 베트남 환자들이 마취에 대한 막연한 두려움을 갖는 경우가 많으므로 안전성을 강조하는 것이 필요합니다.",
        "meaningVi": "Giấy đồng ý gây mê là văn bản xác nhận bệnh nhân đã được giải thích về loại hình gây mê, phương pháp thực hiện và nguy cơ biến chứng, đồng thời tự nguyện đồng ý thực hiện.",
        "context": "수술 전 마취과 의사의 설명 후 작성, 전신마취나 척추마취 등 침습적 마취 시 필수",
        "culturalNote": "베트남에서는 '마취하면 깨어나지 못할 수도 있다'는 두려움이 한국보다 강하게 남아있습니다. 이는 과거 의료 수준이 낮았던 시기의 경험 때문입니다. 통역 시 현대 마취의 안전성을 강조하되, 합병증 가능성도 정직하게 전달해야 합니다. 또한 베트nam에서는 마취 동의서가 수술 동의서에 포함되는 경우가 많아, 별도 문서로 받는 한국 시스템을 설명해야 합니다.",
        "commonMistakes": [
            {
                "mistake": "'gây mê'와 'gây tê'를 혼용",
                "correction": "전신마취는 'gây mê', 부분마취는 'gây tê'로 엄격히 구분",
                "explanation": "'gây mê'는 의식을 잃는 전신마취, 'gây tê'는 의식은 있으나 감각이 없는 부분마취로 완전히 다른 개념입니다."
            },
            {
                "mistake": "금식 시간을 'nhịn ăn' (먹지 않다)로만 설명",
                "correction": "'nhịn ăn và uống' (먹고 마시지 않다) + 구체적 시간 명시",
                "explanation": "물도 마시면 안 되는데 '먹다'만 언급하면 환자가 물은 마셔도 된다고 오해할 수 있습니다."
            },
            {
                "mistake": "마취 후 '잠든다(ngủ)'로 표현",
                "correction": "'bất tỉnh' (의식을 잃다) 또는 'mất ý thức' (의식 상실)",
                "explanation": "일반적인 수면과 마취를 구분해야 환자가 마취의 심각성을 이해할 수 있습니다."
            }
        ],
        "examples": [
            {
                "ko": "전신마취로 진행될 예정이니 마취동의서에 서명해 주세요",
                "vi": "Ca phẫu thuật sẽ tiến hành với gây mê toàn thân, xin anh/chị ký giấy đồng ý gây mê",
                "situation": "formal"
            },
            {
                "ko": "수술 8시간 전부터 물도 마시면 안 됩니다",
                "vi": "Từ 8 tiếng trước ca phẫu thuật, anh/chị không được ăn và uống gì cả, kể cả nước",
                "situation": "onsite"
            },
            {
                "ko": "마취에서 깨어나면 목이 아플 수 있어요",
                "vi": "Khi tỉnh lại sau gây mê, anh/chị có thể bị đau họng",
                "situation": "informal"
            }
        ],
        "relatedTerms": ["수술동의서", "전신마취", "척추마취", "회복실"]
    },
    {
        "slug": "giay-gioi-thieu-kham",
        "korean": "진료의뢰서",
        "vietnamese": "Giấy giới thiệu khám",
        "hanja": "診療依賴書",
        "hanjaReading": "診(진찰 진) + 療(치료 료) + 依(의지 의) + 賴(믿을 뢰) + 書(글 서)",
        "pronunciation": "진리오 이리에 서",
        "meaningKo": "1차 의료기관에서 2차 이상 상급병원으로 환자를 전원하거나 전문 진료를 의뢰할 때 작성하는 공식 문서입니다. 통역 시 주의할 점은 한국의 '의료전달체계'를 설명해야 한다는 것입니다. 베트남과 달리 한국은 의뢰서 없이 상급병원에 가면 진료비가 추가되므로, 이 문서가 비용 절감의 핵심임을 강조해야 합니다. 또한 '소견서'와 구분하여 의뢰서는 의사 간 공식 커뮤니케이션 문서임을 명확히 해야 합니다.",
        "meaningVi": "Giấy giới thiệu khám là văn bản chính thức do bác sĩ tuyến dưới viết để chuyển bệnh nhân lên bệnh viện tuyến trên hoặc chuyên khoa để được khám và điều trị chuyên sâu.",
        "context": "동네 병원에서 큰 병원으로 전원 시, 전문과 진료 필요 시",
        "culturalNote": "한국의 의료전달체계는 1차(의원) → 2차(병원) → 3차(상급종합병원) 순서로 진료를 받도록 유도하는 시스템입니다. 의뢰서 없이 대형병원에 직접 가면 '선택진료비'가 추가됩니다. 반면 베트남은 이런 체계가 덜 엄격하여 환자가 자유롭게 병원을 선택합니다. 통역 시 한국 시스템의 경제적 이점을 설명하되, 응급 상황에서는 의뢰서 없이도 직접 방문 가능함을 안내해야 합니다.",
        "commonMistakes": [
            {
                "mistake": "'giấy chuyển viện' (전원서)와 혼동",
                "correction": "'giấy giới thiệu khám'은 의뢰, 'giấy chuyển viện'은 완전 전원",
                "explanation": "의뢰서는 특정 검사나 진료 후 다시 원래 병원으로 돌아올 수 있지만, 전원서는 치료를 완전히 다른 병원으로 옮기는 것입니다."
            },
            {
                "mistake": "의뢰서가 없어도 큰 병원에 갈 수 있다고 설명",
                "correction": "갈 수는 있으나 진료비가 추가된다고 명확히 안내",
                "explanation": "환자가 비용 부담을 모르고 직접 방문했다가 당황하는 상황을 예방해야 합니다."
            },
            {
                "mistake": "'소개장'이라는 일상 용어 그대로 번역",
                "correction": "의료 맥락에서는 'giấy giới thiệu khám' (진료 의뢰서) 사용",
                "explanation": "일상적인 '소개'가 아닌 의료 전문 문서임을 명확히 해야 합니다."
            }
        ],
        "examples": [
            {
                "ko": "정밀 검사가 필요해서 대학병원 진료의뢰서를 써드렸습니다",
                "vi": "Anh/chị cần làm xét nghiệm chuyên sâu nên tôi đã viết giấy giới thiệu khám tại bệnh viện đại học",
                "situation": "formal"
            },
            {
                "ko": "이 의뢰서 가지고 가시면 진료비가 덜 나와요",
                "vi": "Nếu mang giấy giới thiệu này đi, chi phí khám sẽ thấp hơn",
                "situation": "onsite"
            },
            {
                "ko": "의뢰서 안 가져가면 5만 원 더 내셔야 해요",
                "vi": "Nếu không mang giấy giới thiệu, anh/chị phải trả thêm khoảng 50,000 won",
                "situation": "informal"
            }
        ],
        "relatedTerms": ["소견서", "진단서", "의료전달체계", "상급종합병원"]
    },
    {
        "slug": "giay-y-kien-bac-si",
        "korean": "소견서",
        "vietnamese": "Giấy ý kiến bác sĩ",
        "hanja": "所見書",
        "hanjaReading": "所(바 소) + 見(볼 견) + 書(글 서)",
        "pronunciation": "소지엔 서",
        "meaningKo": "의사가 환자의 현재 건강 상태, 진단명, 치료 경과 등을 종합적으로 기록한 의학적 의견서입니다. 통역 시 주의할 점은 '진단서'와 구분해야 한다는 것입니다. 진단서는 법적 효력이 있는 공식 문서인 반면, 소견서는 의사의 의학적 견해를 담은 참고 문서입니다. 베트남 환자들이 보험 청구나 회사 제출용으로 혼동하는 경우가 많으므로, 용도에 따라 어떤 문서가 필요한지 명확히 안내해야 합니다.",
        "meaningVi": "Giấy ý kiến bác sĩ là văn bản ghi lại ý kiến y khoa tổng hợp của bác sĩ về tình trạng sức khỏe hiện tại, chẩn đoán và quá trình điều trị của bệnh nhân.",
        "context": "회사 제출, 학교 제출, 개인 기록 보관용으로 발급",
        "culturalNote": "한국에서는 '진단서'와 '소견서'의 법적 효력과 발급 비용이 다릅니다. 진단서는 법적 분쟁이나 보험 청구에 사용되며 비용이 비싸지만(보통 10만 원 이상), 소견서는 단순 참고용으로 저렴합니다(1~3만 원). 베트남에서는 이런 구분이 덜 명확하여 환자들이 혼동합니다. 통역 시 환자의 사용 목적을 먼저 파악한 후 적절한 문서를 안내해야 경제적 손실을 예방할 수 있습니다.",
        "commonMistakes": [
            {
                "mistake": "'giấy chẩn đoán' (진단서)와 구분 없이 사용",
                "correction": "소견서는 'giấy ý kiến bác sĩ', 진단서는 'giấy chẩn đoán bệnh'",
                "explanation": "소견서는 의견서(참고용), 진단서는 공식 의료 증명서로 법적 효력과 비용이 다릅니다."
            },
            {
                "mistake": "소견서로 보험 청구가 가능하다고 안내",
                "correction": "보험 청구는 진단서가 필요하다고 명확히 설명",
                "explanation": "소견서는 법적 효력이 없어 보험사가 인정하지 않을 수 있습니다."
            },
            {
                "mistake": "'ý kiến'을 단순 의견으로 가볍게 표현",
                "correction": "'ý kiến y khoa chuyên môn' (전문 의학적 의견) 강조",
                "explanation": "환자가 소견서를 단순 메모로 오해하지 않도록 전문성을 부각해야 합니다."
            }
        ],
        "examples": [
            {
                "ko": "회사에 제출하실 거면 소견서면 충분합니다",
                "vi": "Nếu nộp cho công ty thì giấy ý kiến bác sĩ là đủ",
                "situation": "formal"
            },
            {
                "ko": "보험 청구하려면 소견서가 아니라 진단서가 필요해요",
                "vi": "Để yêu cầu bảo hiểm, anh/chị cần giấy chẩn đoán bệnh chứ không phải giấy ý kiến bác sĩ",
                "situation": "onsite"
            },
            {
                "ko": "소견서는 진단서보다 저렴해요",
                "vi": "Giấy ý kiến bác sĩ rẻ hơn giấy chẩn đoán bệnh",
                "situation": "informal"
            }
        ],
        "relatedTerms": ["진단서", "진료확인서", "소견", "의무기록사본"]
    },
    {
        "slug": "tom-tat-ra-vien",
        "korean": "퇴원요약",
        "vietnamese": "Tóm tắt ra viện",
        "hanja": "退院要約",
        "hanjaReading": "退(물러날 퇴) + 院(집 원) + 要(요긴 요) + 約(맺을 약)",
        "pronunciation": "톰 닷 자 비엔",
        "meaningKo": "입원 기간 동안의 진단, 치료 과정, 투약 내역, 향후 치료 계획 등을 요약한 의료 문서로, 퇴원 시 환자에게 제공됩니다. 통역 시 주의할 점은 이 문서가 단순 퇴원 증명이 아닌 향후 치료의 연속성을 보장하는 핵심 자료라는 점입니다. 베트남 환자들이 이 문서를 잃어버리면 다음 진료 시 처음부터 검사를 다시 해야 할 수 있으므로, 보관의 중요성을 반드시 강조해야 합니다. 또한 귀국 시 현지 병원에서 이어서 치료받을 수 있도록 번역본 제공을 안내하는 것이 좋습니다.",
        "meaningVi": "Tóm tắt ra viện là văn bản y tế tóm lược chẩn đoán, quá trình điều trị, đơn thuốc và kế hoạch điều trị tiếp theo trong thời gian nằm viện, được cung cấp cho bệnh nhân khi xuất viện.",
        "context": "퇴원 수속 시 발급, 외래 진료 시 지참, 타 병원 전원 시 필수",
        "culturalNote": "한국 의료 시스템에서 퇴원요약서는 환자의 '의료 여권' 같은 역할을 합니다. 다음 병원 방문 시 이 문서가 있으면 중복 검사를 피할 수 있어 시간과 비용을 절약할 수 있습니다. 베트남에서는 입원 기록이 병원에 보관되고 환자가 받는 문서가 간소한 경우가 많아, 한국의 상세한 퇴원요약서에 놀라는 경우가 있습니다. 통역 시 이 문서를 귀국 시 베트남 의사에게 보여주면 치료 연속성 확보에 도움이 된다고 안내하면 좋습니다.",
        "commonMistakes": [
            {
                "mistake": "'giấy ra viện' (퇴원증)으로 단순 번역",
                "correction": "'tóm tắt ra viện' (퇴원 요약) 또는 'bản tóm tắt bệnh án' (병력 요약)",
                "explanation": "단순 퇴원 증명이 아닌 상세한 의료 기록 요약임을 나타내야 합니다."
            },
            {
                "mistake": "환자에게 '버리지 마세요'만 강조",
                "correction": "다음 진료 시 반드시 가져와야 한다고 구체적으로 안내",
                "explanation": "보관 이유와 활용 방법을 명확히 해야 환자가 중요성을 이해합니다."
            },
            {
                "mistake": "의학 용어를 그대로 번역하여 환자가 이해 못 함",
                "correction": "핵심 내용(진단명, 복용법)을 쉬운 말로 부연 설명",
                "explanation": "퇴원요약서는 전문 용어가 많아 통역사가 환자 눈높이로 해석해줘야 합니다."
            }
        ],
        "examples": [
            {
                "ko": "퇴원요약서에 향후 3개월간 복용할 약이 적혀있으니 꼭 보관하세요",
                "vi": "Trong tóm tắt ra viện có ghi thuốc phải uống trong 3 tháng tới, xin anh/chị bảo quản cẩn thận",
                "situation": "formal"
            },
            {
                "ko": "다음에 외래 올 때 이 서류 꼭 가져오세요",
                "vi": "Lần khám ngoại trú tiếp theo, anh/chị nhớ mang theo tài liệu này",
                "situation": "onsite"
            },
            {
                "ko": "베트남 돌아가서 병원 가면 이 서류 보여주세요",
                "vi": "Khi về Việt Nam đi khám bệnh viện, hãy đưa tài liệu này cho bác sĩ xem",
                "situation": "informal"
            }
        ],
        "relatedTerms": ["퇴원계획서", "진료기록사본", "투약기록", "경과기록"]
    },
    {
        "slug": "hoa-don-vien-phi",
        "korean": "의료비영수증",
        "vietnamese": "Hóa đơn viện phí",
        "hanja": "醫療費領收證",
        "hanjaReading": "醫(의원 의) + 療(치료 료) + 費(쓸 비) + 領(거느릴 령) + 收(거둘 수) + 證(증거 증)",
        "pronunciation": "호아 돈 비엔 피",
        "meaningKo": "병원에서 받은 진료, 검사, 약제, 입원 등 모든 의료 서비스에 대한 비용을 항목별로 상세히 기재한 공식 영수증입니다. 통역 시 주의할 점은 한국의 의료비 영수증이 '간이 영수증'과 '상세 영수증' 두 종류가 있다는 것입니다. 보험 청구나 의료비 공제 시에는 반드시 상세 영수증이 필요하므로, 환자가 어떤 용도로 사용할지 먼저 확인해야 합니다. 베트남 환자가 귀국 후 보험 청구할 경우를 대비해 영문 번역본 발급도 안내하면 좋습니다.",
        "meaningVi": "Hóa đơn viện phí là biên lai chính thức ghi chi tiết các khoản phí y tế theo từng hạng mục như khám bệnh, xét nghiệm, thuốc, nằm viện mà bệnh nhân đã chi trả tại bệnh viện.",
        "context": "진료비 수납 후 발급, 보험 청구 시 필수 제출, 연말정산 의료비 공제",
        "culturalNote": "한국은 의료비 영수증 시스템이 매우 체계적이어서 국세청 연말정산 간소화 서비스에 자동 등록됩니다. 하지만 외국인은 이 시스템을 이용할 수 없어 수기로 보관해야 합니다. 베트남은 의료비 영수증이 간소한 경우가 많아, 한국의 상세한 항목별 명세서를 보고 놀라는 환자가 많습니다. 통역 시 환자가 베트남 보험사에 청구할 경우 영문 번역본이 필요할 수 있으니 미리 발급받도록 안내하는 것이 중요합니다.",
        "commonMistakes": [
            {
                "mistake": "'biên lai' (일반 영수증)로 번역",
                "correction": "'hóa đơn viện phí' (의료비 영수증) 또는 'hóa đơn chi tiết viện phí' (상세 의료비 영수증)",
                "explanation": "일반 영수증과 구분하여 의료비 전용 영수증임을 명확히 해야 법적 효력을 인정받습니다."
            },
            {
                "mistake": "간이 영수증과 상세 영수증을 구분하지 않음",
                "correction": "보험 청구 시 'hóa đơn chi tiết' (상세 영수증) 필요하다고 명시",
                "explanation": "간이 영수증으로는 보험 청구가 거부될 수 있습니다."
            },
            {
                "mistake": "영수증을 환자가 안 챙겨도 된다고 안내",
                "correction": "향후 보험 청구나 분쟁 시 증빙 자료가 되므로 반드시 보관하도록 강조",
                "explanation": "나중에 영수증 재발급이 어렵거나 수수료가 발생할 수 있습니다."
            }
        ],
        "examples": [
            {
                "ko": "의료비 영수증은 보험 청구할 때 필요하니 잘 보관하세요",
                "vi": "Hóa đơn viện phí cần thiết khi yêu cầu bảo hiểm, xin anh/chị bảo quản cẩn thận",
                "situation": "formal"
            },
            {
                "ko": "상세 영수증으로 출력해 드릴까요?",
                "vi": "Tôi in hóa đơn chi tiết cho anh/chị nhé?",
                "situation": "onsite"
            },
            {
                "ko": "영수증 잃어버리면 재발급 수수료 내셔야 해요",
                "vi": "Nếu mất hóa đơn, anh/chị phải trả phí cấp lại",
                "situation": "informal"
            }
        ],
        "relatedTerms": ["진료비계산서", "보험청구서", "본인부담금", "비급여항목"]
    },
    {
        "slug": "thu-tuc-nhap-xuat-vien",
        "korean": "입퇴원수속",
        "vietnamese": "Thủ tục nhập xuất viện",
        "hanja": "入退院手續",
        "hanjaReading": "入(들 입) + 退(물러날 퇴) + 院(집 원) + 手(손 수) + 續(이을 속)",
        "pronunciation": "투 뚝 년 쑤앗 비엔",
        "meaningKo": "병원에 입원하거나 퇴원할 때 필요한 서류 작성, 보증금 납부, 개인정보 등록 등의 행정 절차를 총칭하는 용어입니다. 통역 시 주의할 점은 한국의 입원 시스템이 베트남과 달리 사전 예약제이며, 응급실을 통한 입원이 아닌 경우 대기 시간이 길 수 있다는 점입니다. 또한 입원 보증금 제도와 외국인 환자의 경우 선납금이 더 높을 수 있음을 미리 안내해야 환자가 당황하지 않습니다. 퇴원 수속 시에는 최종 정산 금액이 보증금을 초과할 수 있음을 설명해야 합니다.",
        "meaningVi": "Thủ tục nhập xuất viện là các quy trình hành chính cần thiết khi nhập viện hoặc xuất viện, bao gồm kê khai giấy tờ, nộp tiền đặt cọc, đăng ký thông tin cá nhân.",
        "context": "입원 결정 후 원무과 방문, 퇴원 당일 정산 및 서류 수령",
        "culturalNote": "한국 병원은 입원 시 보증금(đặt cọc) 제도를 운영합니다. 일반적으로 입원비의 일부를 선납하고, 퇴원 시 실제 사용액과 정산합니다. 베트남도 유사한 제도가 있으나, 한국은 외국인 환자에게 보증금을 더 높게 요구하는 경우가 많습니다(신용 리스크 때문). 통역 시 이것이 차별이 아닌 제도적 안전장치임을 설명하되, 환자가 불쾌해하지 않도록 공감하는 태도가 필요합니다. 또한 퇴원 수속이 오전 중에 완료되어야 당일 퇴원이 가능하므로, 시간 엄수를 강조해야 합니다.",
        "commonMistakes": [
            {
                "mistake": "'nhập viện'과 'nằm viện'을 혼용",
                "correction": "'nhập viện'은 입원 수속, 'nằm viện'은 입원 상태",
                "explanation": "입원하는 행위와 입원해 있는 상태를 구분해야 환자가 지금 무엇을 해야 하는지 명확히 이해합니다."
            },
            {
                "mistake": "보증금을 'tiền ký quỹ' (예치금)로만 설명",
                "correction": "'tiền đặt cọc nhập viện' (입원 보증금)으로 명확히 설명",
                "explanation": "일반 예치금과 달리 입원 비용 선납의 성격임을 분명히 해야 합니다."
            },
            {
                "mistake": "퇴원 시간을 '아무 때나'로 안내",
                "correction": "오전 중 수속 완료해야 추가 입원비가 안 나온다고 명시",
                "explanation": "오후에 퇴원하면 하루 입원비가 추가 청구될 수 있어 경제적 손실이 발생합니다."
            }
        ],
        "examples": [
            {
                "ko": "입원 수속하실 때 신분증과 보증금 100만 원 준비해 오세요",
                "vi": "Khi làm thủ tục nhập viện, xin anh/chị mang theo giấy tờ tùy thân và tiền đặt cọc 1 triệu won",
                "situation": "formal"
            },
            {
                "ko": "퇴원 수속은 1층 원무과에서 하시면 됩니다",
                "vi": "Thủ tục xuất viện làm tại phòng hành chính tầng 1",
                "situation": "onsite"
            },
            {
                "ko": "내일 오전 10시까지 퇴원 수속 마쳐야 추가 비용 안 나와요",
                "vi": "Phải hoàn tất thủ tục xuất viện trước 10 giờ sáng mai thì mới không bị tính thêm phí",
                "situation": "informal"
            }
        ],
        "relatedTerms": ["입원보증금", "원무과", "진료비정산", "퇴원계획"]
    },
    {
        "slug": "yeu-cau-bao-hiem",
        "korean": "보험청구",
        "vietnamese": "Yêu cầu bảo hiểm",
        "hanja": "保險請求",
        "hanjaReading": "保(지킬 보) + 險(험할 험) + 請(청할 청) + 求(구할 구)",
        "pronunciation": "이에우 까우 바오 히엠",
        "meaningKo": "의료비를 지불한 후 가입한 보험회사에 해당 비용의 전부 또는 일부를 환급받기 위해 관련 서류를 제출하는 절차입니다. 통역 시 주의할 점은 한국 건강보험과 베트남 보험의 청구 절차가 다르다는 것입니다. 한국 국민건강보험은 병원에서 자동 청구되지만, 외국인이 가입한 민간보험이나 베트남 보험은 환자가 직접 청구해야 합니다. 필요한 서류(진단서, 상세 영수증, 처방전 사본 등)를 미리 안내하여 환자가 추가 방문하지 않도록 하는 것이 중요합니다.",
        "meaningVi": "Yêu cầu bảo hiểm là thủ tục nộp hồ sơ cho công ty bảo hiểm để được hoàn lại toàn bộ hoặc một phần chi phí y tế đã chi trả.",
        "context": "진료비 수납 후, 보험회사에 서류 제출, 해외 체류 외국인의 본국 보험 청구",
        "culturalNote": "한국에서 진료받은 베트남 환자가 베트남 보험사에 청구하려면 진단서(영문), 상세 영수증(영문), 처방전(영문)이 필요한 경우가 많습니다. 한국 병원은 영문 서류 발급에 추가 비용과 시간이 소요되므로, 통역 시 환자에게 귀국 전 미리 준비하도록 안내해야 합니다. 또한 베트남 보험사마다 요구 서류가 다를 수 있으니, 환자가 본인 보험사에 먼저 확인하도록 권유하는 것이 좋습니다. 한국의 실손보험과 베트남의 bảo hiểm y tế tự nguyện (임의 건강보험)의 보장 범위 차이도 설명해야 합니다.",
        "commonMistakes": [
            {
                "mistake": "'đòi bảo hiểm' (보험 요구하다)로 번역",
                "correction": "'yêu cầu bảo hiểm' (보험 청구하다) 또는 'khiếu nại bảo hiểm' (보험 클레임)",
                "explanation": "'đòi'는 공격적 뉘앙스가 있어 정중한 행정 절차에 부적합합니다."
            },
            {
                "mistake": "모든 의료비가 보험 처리된다고 안내",
                "correction": "비급여 항목은 보험 적용 안 될 수 있다고 명시",
                "explanation": "상급 병실료, 특진비 등 비급여 항목은 보험사가 거부할 수 있습니다."
            },
            {
                "mistake": "한국어 서류로도 청구 가능하다고 설명",
                "correction": "베트남 보험사는 보통 영문 서류를 요구한다고 안내",
                "explanation": "환자가 귀국 후 서류 미비로 청구 거부당하는 것을 예방해야 합니다."
            }
        ],
        "examples": [
            {
                "ko": "보험 청구하시려면 영문 진단서와 상세 영수증이 필요합니다",
                "vi": "Để yêu cầu bảo hiểm, anh/chị cần giấy chẩn đoán tiếng Anh và hóa đơn chi tiết",
                "situation": "formal"
            },
            {
                "ko": "베트남 보험사에 어떤 서류가 필요한지 먼저 확인해 보세요",
                "vi": "Xin anh/chị hỏi công ty bảo hiểm Việt Nam cần những giấy tờ gì trước",
                "situation": "onsite"
            },
            {
                "ko": "영문 서류 발급에 3~5일 걸려요",
                "vi": "Cấp giấy tờ tiếng Anh mất 3-5 ngày",
                "situation": "informal"
            }
        ],
        "relatedTerms": ["실손보험", "진단서", "의료비영수증", "비급여항목"]
    },
    {
        "slug": "dang-ky-benh-nhan-nuoc-ngoai",
        "korean": "외국인환자등록",
        "vietnamese": "Đăng ký bệnh nhân nước ngoài",
        "hanja": "外國人患者登錄",
        "hanjaReading": "外(밖 외) + 國(나라 국) + 人(사람 인) + 患(근심 환) + 者(놈 자) + 登(오를 등) + 錄(기록 록)",
        "pronunciation": "당 끼 벤 년 느억 응와이",
        "meaningKo": "외국 국적을 가진 환자가 한국 병원에서 처음 진료를 받을 때 신분 확인 및 연락처, 체류 정보 등을 등록하는 절차입니다. 통역 시 주의할 점은 외국인 환자는 내국인과 달리 여권, 외국인등록증, 비자 정보 등 추가 서류가 필요하다는 것입니다. 또한 미등록 체류자의 경우 신분 노출을 꺼려 병원 방문을 주저하는 경우가 있는데, 의료법상 병원은 환자 정보를 출입국 관리소에 통보할 의무가 없음을 안내하면 환자가 안심하고 진료받을 수 있습니다.",
        "meaningVi": "Đăng ký bệnh nhân nước ngoài là thủ tục xác minh danh tính và ghi nhận thông tin liên lạc, tình trạng lưu trú của bệnh nhân mang quốc적 nước ngoài khi khám chữa bệnh lần đầu tại bệnh viện Hàn Quốc.",
        "context": "병원 첫 방문 시 원무과에서 진행, 외국인등록번호 또는 여권번호로 환자 식별",
        "culturalNote": "한국은 외국인 환자 유치를 장려하면서도 의료비 미납 방지를 위해 신분 확인을 철저히 합니다. 베트남 환자들은 이를 '감시'로 오해할 수 있으므로, 통역 시 이것이 환자 안전과 정확한 의료 기록 관리를 위한 것임을 설명해야 합니다. 특히 불법 체류자는 병원이 출입국 사무소에 신고할까 두려워 응급 상황에서도 병원을 피하는 경우가 있는데, 의료법 제3조에 따라 병원은 환자 정보 보호 의무가 있음을 안내하면 도움이 됩니다. 다만 중대 범죄 연루 시에는 예외가 있을 수 있습니다.",
        "commonMistakes": [
            {
                "mistake": "'đăng ký' (등록)만 사용하여 일반 등록과 구분 안 됨",
                "correction": "'đăng ký bệnh nhân nước ngoài' (외국인 환자 등록) 전체 표현 사용",
                "explanation": "외국인 특화 절차임을 명확히 해야 필요 서류를 제대로 준비할 수 있습니다."
            },
            {
                "mistake": "여권만 있으면 된다고 안내",
                "correction": "외국인등록증이나 장기 체류 비자도 요구될 수 있다고 설명",
                "explanation": "병원마다 요구 서류가 다를 수 있어 사전 확인이 필요합니다."
            },
            {
                "mistake": "불법 체류자는 병원 못 간다고 잘못 안내",
                "correction": "불법 체류 여부와 관계없이 응급 치료는 받을 수 있다고 설명",
                "explanation": "응급의료법에 따라 응급 환자는 체류 자격과 무관하게 치료받을 권리가 있습니다."
            }
        ],
        "examples": [
            {
                "ko": "외국인 환자 등록하실 때 여권이랑 외국인등록증 둘 다 가져오세요",
                "vi": "Khi đăng ký bệnh nhân nước ngoài, xin mang theo cả hộ chiếu và thẻ ngoại kiều",
                "situation": "formal"
            },
            {
                "ko": "병원은 환자 정보를 출입국 사무소에 알리지 않으니 걱정 마세요",
                "vi": "Bệnh viện không báo cáo thông tin bệnh nhân cho cơ quan xuất nhập cảnh, xin đừng lo",
                "situation": "onsite"
            },
            {
                "ko": "등록할 때 한국 연락처 필요해요",
                "vi": "Khi đăng ký cần số điện thoại ở Hàn Quốc",
                "situation": "informal"
            }
        ],
        "relatedTerms": ["외국인등록증", "여권", "비자", "미등록체류자"]
    },
    {
        "slug": "van-chuyen-cap-cuu",
        "korean": "응급이송",
        "vietnamese": "Vận chuyển cấp cứu",
        "hanja": "應急移送",
        "hanjaReading": "應(응할 응) + 急(급할 급) + 移(옮길 이) + 送(보낼 송)",
        "pronunciation": "번 쭈옌 껍 꾸",
        "meaningKo": "생명이 위급하거나 중증 질환으로 신속한 의료 처치가 필요한 환자를 구급차나 헬기 등을 이용하여 병원으로 긴급 이송하는 것을 의미합니다. 통역 시 주의할 점은 한국의 119 구급차는 무료이지만, 민간 구급차나 병원 간 이송은 비용이 발생한다는 것입니다. 베트남 환자들이 모든 구급차가 무료인 줄 알고 있다가 나중에 수십만 원의 이송 비용을 청구받고 당황하는 경우가 있으므로, 이송 전 비용 안내가 필수입니다. 또한 응급 상황에서는 환자 동의 없이도 이송이 가능함을 설명해야 합니다.",
        "meaningVi": "Vận chuyển cấp cứu là việc di chuyển khẩn cấp bệnh nhân có tính mạng nguy kịch hoặc bệnh nặng cần xử trí y tế nhanh chóng đến bệnh viện bằng xe cứu thương hoặc trực thăng.",
        "context": "응급실 호출, 병원 간 전원, 중증 환자 이송",
        "culturalNote": "한국의 응급의료 시스템은 119(소방) 구급차와 민간 구급차로 이원화되어 있습니다. 119는 무료이지만 생명이 위급한 경우에만 이용해야 하며, 단순 이동 목적으로 사용하면 과태료가 부과될 수 있습니다. 반면 베트남은 응급 이송 인프라가 덜 발달하여 택시로 병원 가는 경우도 많습니다. 통역 시 한국에서는 응급 상황 시 반드시 119를 부르고, 비응급 이송은 민간 구급차(유료)를 이용해야 한다고 명확히 안내해야 합니다. 또한 119는 한국어만 가능하므로, 베트남 환자는 주변 한국인에게 도움을 요청하거나 다누리콜센터(1345)를 이용하도록 안내하는 것이 좋습니다.",
        "commonMistakes": [
            {
                "mistake": "'xe cứu thương' (구급차)로만 번역하여 긴급성 표현 부족",
                "correction": "'vận chuyển cấp cứu' (응급 이송) 또는 'xe cấp cứu' (응급차)",
                "explanation": "일반 이송과 응급 이송을 구분해야 우선순위와 비용이 명확해집니다."
            },
            {
                "mistake": "모든 구급차가 무료라고 안내",
                "correction": "119는 무료, 민간 구급차는 유료라고 구분 설명",
                "explanation": "환자가 비용 부담을 모르고 민간 구급차를 부르면 경제적 손실이 발생합니다."
            },
            {
                "mistake": "119에 베트남어 통역이 있다고 안내",
                "correction": "119는 한국어만 가능하니 한국인 도움 필요하다고 설명",
                "explanation": "언어 문제로 응급 상황이 악화되는 것을 예방해야 합니다."
            }
        ],
        "examples": [
            {
                "ko": "응급 상황이면 119에 전화해서 구급차를 부르세요",
                "vi": "Nếu tình trạng cấp cứu, hãy gọi 119 để gọi xe cấp cứu",
                "situation": "formal"
            },
            {
                "ko": "다른 병원으로 옮기려면 민간 구급차 불러야 하는데 비용 나와요",
                "vi": "Nếu chuyển sang bệnh viện khác, phải gọi xe cứu thương tư nhân và sẽ mất phí",
                "situation": "onsite"
            },
            {
                "ko": "119는 한국어만 되니까 옆에 한국 사람한테 부탁하세요",
                "vi": "119 chỉ nói tiếng Hàn nên nhờ người Hàn Quốc bên cạnh giúp",
                "situation": "informal"
            }
        ],
        "relatedTerms": ["119", "응급실", "구급차", "전원"]
    }
]

# Filter out duplicates
new_terms = [t for t in new_terms if t['slug'] not in existing_slugs]

# Add to data
data.extend(new_terms)

# Save
with open(file_path, 'w', encoding='utf-8') as f:
    json.dump(data, f, ensure_ascii=False, indent=2)

print(f"Added {len(new_terms)} new medical terms. Total: {len(data)}")
