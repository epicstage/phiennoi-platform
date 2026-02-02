import json, os
file_path = os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', 'data', 'terms', 'medical.json')
with open(file_path, 'r', encoding='utf-8') as f:
    data = json.load(f)
existing_slugs = {t['slug'] for t in data}

new_terms = [
    {
        "slug": "quyet-dinh-keo-dai-su-song",
        "korean": "연명의료결정",
        "vietnamese": "Quyết định kéo dài sự sống",
        "hanja": "延命醫療決定",
        "hanjaReading": "延(늘일 연) + 命(목숨 명) + 醫(의원 의) + 療(치료할 료) + 決(결단할 결) + 定(정할 정)",
        "pronunciation": "연명의료결정",
        "meaningKo": "회복 가능성이 없는 환자에게 생명 연장을 위한 의료 행위를 계속할지 중단할지에 대한 결정을 의미합니다. 통역 시 주의할 점은 한국의 '연명의료결정법'과 베트남의 관련 법규가 다르므로, 단순 번역이 아닌 법적 맥락을 함께 설명해야 합니다. 환자 본인의 의사, 가족의 동의, 의료진의 판단이 모두 관련되므로 각 주체의 역할을 명확히 구분하여 통역해야 오해를 방지할 수 있습니다.",
        "meaningVi": "Quyết định về việc tiếp tục hay ngừng các biện pháp y tế nhằm kéo dài sự sống cho bệnh nhân không còn khả năng hồi phục. Quyết định này liên quan đến ý chí của bệnh nhân, sự đồng ý của gia đình và đánh giá của đội ngũ y tế.",
        "context": "의료윤리, 말기환자 치료, 법률 상담",
        "culturalNote": "한국은 '연명의료결정법'(2018년 시행)으로 환자의 자기결정권을 존중하지만, 베트남은 아직 명확한 법적 체계가 부족합니다. 한국에서는 사전연명의료의향서 작성이 일반화되어 있으나, 베트남에서는 가족 중심의 의사결정이 주를 이루므로 통역 시 이러한 문화적 차이를 고려해야 합니다.",
        "commonMistakes": [
            {
                "mistake": "Quyết định chết tự nhiên",
                "correction": "Quyết định kéo dài sự sống",
                "explanation": "연명의료결정은 '자연사 결정'이 아니라 생명 연장 의료에 대한 결정이므로 정확한 표현을 사용해야 합니다."
            },
            {
                "mistake": "Quyết định của bác sĩ",
                "correction": "Quyết định của bệnh nhân/gia đình với tư vấn y tế",
                "explanation": "의사만의 결정이 아니라 환자와 가족의 의사가 중심이 되므로 주체를 명확히 해야 합니다."
            },
            {
                "mistake": "Dừng điều trị",
                "correction": "Không thực hiện các biện pháp kéo dài sự sống",
                "explanation": "모든 치료를 중단하는 것이 아니라 연명치료만 보류하는 것이므로 범위를 정확히 전달해야 합니다."
            }
        ],
        "examples": [
            {
                "ko": "환자분의 연명의료결정에 대해 가족과 상담이 필요합니다.",
                "vi": "Cần tư vấn với gia đình về quyết định kéo dài sự sống của bệnh nhân.",
                "situation": "formal"
            },
            {
                "ko": "사전에 연명의료의향서를 작성하셨나요?",
                "vi": "Bệnh nhân đã từng lập giấy ý nguyện điều trị cuối đời chưa?",
                "situation": "onsite"
            },
            {
                "ko": "연명의료를 중단하기로 결정했습니다.",
                "vi": "Đã quyết định không tiếp tục các biện pháp kéo dài sự sống.",
                "situation": "formal"
            }
        ],
        "relatedTerms": ["사전연명의료의향서", "완화의료", "호스피스"]
    },
    {
        "slug": "giay-y-nguyen-dieu-tri-cuoi-doi",
        "korean": "사전연명의료의향서",
        "vietnamese": "Giấy ý nguyện điều trị cuối đời",
        "hanja": "事前延命醫療意向書",
        "hanjaReading": "事(일 사) + 前(앞 전) + 延(늘일 연) + 命(목숨 명) + 醫(의원 의) + 療(치료할 료) + 意(뜻 의) + 向(향할 향) + 書(글 서)",
        "pronunciation": "사전연명의료의향서",
        "meaningKo": "본인이 향후 의식이 없거나 의사표현을 할 수 없는 상태가 되었을 때 연명의료를 받지 않겠다는 의향을 미리 밝혀두는 문서입니다. 통역 시 주의할 점은 이 문서가 법적 효력을 가지며, 작성 시 등록기관에서 공식 절차를 거쳐야 한다는 점을 명확히 전달해야 합니다. 베트남에는 동일한 제도가 없으므로, 한국 의료 시스템 내에서의 역할과 중요성을 충분히 설명해야 합니다.",
        "meaningVi": "Văn bản ghi lại ý nguyện của bản thân về việc từ chối các biện pháp kéo dài sự sống khi không còn ý thức hoặc không thể bày tỏ ý kiến. Đây là văn bản có hiệu lực pháp lý tại Hàn Quốc.",
        "context": "의료 상담, 법률 문서, 환자 권리",
        "culturalNote": "한국에서는 2018년부터 사전연명의료의향서 작성이 법제화되어 국민건강보험공단 등록기관에서 공식적으로 관리됩니다. 베트남에는 이러한 제도가 없고, 가족이 환자를 대신해 결정하는 경우가 많아 개인의 자기결정권에 대한 인식 차이가 큽니다. 통역 시 이 문서의 법적 구속력을 강조해야 합니다.",
        "commonMistakes": [
            {
                "mistake": "Giấy từ chối điều trị",
                "correction": "Giấy ý nguyện điều trị cuối đời",
                "explanation": "모든 치료를 거부하는 것이 아니라 연명의료에 대한 의향서이므로 정확한 명칭을 사용해야 합니다."
            },
            {
                "mistake": "Di chúc y tế",
                "correction": "Giấy ý nguyện điều trị cuối đời",
                "explanation": "유언장과 혼동하지 않도록 의료 의향서임을 명확히 해야 합니다."
            },
            {
                "mistake": "Văn bản cá nhân",
                "correction": "Văn bản đăng ký chính thức tại cơ quan được ủy quyền",
                "explanation": "개인이 작성만 하는 것이 아니라 등록기관을 통해 공식 등록되어야 효력이 있음을 설명해야 합니다."
            }
        ],
        "examples": [
            {
                "ko": "사전연명의료의향서를 작성하시면 등록기관에 보관됩니다.",
                "vi": "Nếu lập giấy ý nguyện điều trị cuối đời, nó sẽ được lưu giữ tại cơ quan đăng ký.",
                "situation": "formal"
            },
            {
                "ko": "이 의향서는 언제든 철회할 수 있습니다.",
                "vi": "Ý nguyện này có thể được rút lại bất cứ lúc nào.",
                "situation": "onsite"
            },
            {
                "ko": "작성 시 본인 확인이 필요합니다.",
                "vi": "Khi lập cần xác minh danh tính bản thân.",
                "situation": "formal"
            }
        ],
        "relatedTerms": ["연명의료결정", "환자 자기결정권", "법정대리인"]
    },
    {
        "slug": "hien-tang",
        "korean": "장기기증",
        "vietnamese": "Hiến tặng nội tạng",
        "hanja": "臟器寄贈",
        "hanjaReading": "臟(오장 장) + 器(그릇 기) + 寄(부칠 기) + 贈(줄 증)",
        "pronunciation": "장기기증",
        "meaningKo": "자신의 장기를 타인에게 기증하여 생명을 구하는 행위로, 뇌사 또는 사후에 이루어집니다. 통역 시 주의할 점은 '기증'과 '이식'을 혼동하지 않도록 해야 하며, 한국은 장기기증 등록 시스템이 잘 갖춰져 있지만 베트남은 문화적·종교적 이유로 기증률이 낮다는 점을 인지해야 합니다. 기증 의사 확인 절차와 법적 요건을 정확히 전달하는 것이 중요합니다.",
        "meaningVi": "Hành động hiến tặng nội tạng của mình để cứu sống người khác, thường được thực hiện sau khi chết não hoặc tử vong. Tại Hàn Quốc, hệ thống đăng ký hiến tặng nội tạng được tổ chức tốt.",
        "context": "의료 상담, 윤리 논의, 법률 절차",
        "culturalNote": "한국은 장기기증 등록이 활성화되어 있고 국립장기조직혈액관리원(KONOS)에서 체계적으로 관리하지만, 베트남은 유교·불교 전통으로 인해 시신 온전함을 중시하여 기증률이 낮습니다. 통역 시 기증 절차와 가족 동의의 중요성을 강조하되, 문화적 민감성을 고려해야 합니다.",
        "commonMistakes": [
            {
                "mistake": "Cấy ghép nội tạng",
                "correction": "Hiến tặng nội tạng",
                "explanation": "'이식'(cấy ghép)과 '기증'(hiến tặng)은 반대 개념이므로 명확히 구분해야 합니다."
            },
            {
                "mistake": "Bán nội tạng",
                "correction": "Hiến tặng nội tạng",
                "explanation": "장기매매가 아닌 자발적 기증임을 명확히 해야 불법 행위로 오해받지 않습니다."
            },
            {
                "mistake": "Chỉ sau khi chết",
                "correction": "Có thể sau khi chết não hoặc tử vong, hoặc hiến tặng một phần khi còn sống (như thận)",
                "explanation": "생체 기증도 가능하므로 조건을 정확히 전달해야 합니다."
            }
        ],
        "examples": [
            {
                "ko": "장기기증 등록을 원하시면 온라인으로 신청 가능합니다.",
                "vi": "Nếu muốn đăng ký hiến tặng nội tạng, có thể đăng ký trực tuyến.",
                "situation": "formal"
            },
            {
                "ko": "뇌사 판정 후 장기기증이 진행됩니다.",
                "vi": "Sau khi xác định chết não, sẽ tiến hành hiến tặng nội tạng.",
                "situation": "onsite"
            },
            {
                "ko": "가족의 동의가 필요합니다.",
                "vi": "Cần có sự đồng ý của gia đình.",
                "situation": "formal"
            }
        ],
        "relatedTerms": ["뇌사판정", "장기이식", "각막기증"]
    },
    {
        "slug": "xac-dinh-chet-nao",
        "korean": "뇌사판정",
        "vietnamese": "Xác định chết não",
        "hanja": "腦死判定",
        "hanjaReading": "腦(뇌 뇌) + 死(죽을 사) + 判(판단할 판) + 定(정할 정)",
        "pronunciation": "뇌사판정",
        "meaningKo": "뇌의 모든 기능이 영구적으로 정지된 상태를 의학적으로 확인하고 판정하는 절차입니다. 통역 시 주의할 점은 '뇌사'와 '심정지'를 명확히 구분해야 하며, 한국의 뇌사판정 기준(두 차례 검사, 6시간 간격)을 정확히 설명해야 합니다. 뇌사 판정 후 장기기증이 가능하므로, 법적·윤리적 절차를 혼동 없이 전달하는 것이 중요합니다.",
        "meaningVi": "Quá trình xác định y khoa rằng tất cả chức năng của não đã ngừng hoạt động vĩnh viễn. Tại Hàn Quốc, cần tiến hành kiểm tra hai lần cách nhau 6 giờ để xác định chết não.",
        "context": "중환자실, 응급의료, 법률 상담",
        "culturalNote": "한국은 뇌사판정위원회를 통해 엄격한 의료·법적 절차를 거쳐 판정하며, 판정 후 장기기증 여부를 결정할 수 있습니다. 베트남에서는 뇌사 개념이 의료 현장에서는 인지되지만 법적 기준이 덜 명확하고, 문화적으로 '심장이 뛰는 상태'를 살아있는 것으로 보는 경향이 있어 통역 시 개념 설명이 필요합니다.",
        "commonMistakes": [
            {
                "mistake": "Ngừng tim",
                "correction": "Chết não (não ngừng hoạt động nhưng tim vẫn có thể đập)",
                "explanation": "뇌사는 심정지와 다르며, 뇌 기능 정지 상태임을 명확히 해야 합니다."
            },
            {
                "mistake": "Hôn mê sâu",
                "correction": "Chết não (không thể hồi phục)",
                "explanation": "혼수상태는 회복 가능성이 있지만 뇌사는 불가역적이므로 구분이 중요합니다."
            },
            {
                "mistake": "Bác sĩ quyết định",
                "correction": "Ủy ban xác định chết não quyết định sau kiểm tra kỹ lưỡng",
                "explanation": "개인 의사가 아닌 판정위원회가 결정하는 절차임을 전달해야 합니다."
            }
        ],
        "examples": [
            {
                "ko": "뇌사판정을 위해 두 차례 검사를 진행합니다.",
                "vi": "Để xác định chết não, sẽ tiến hành kiểm tra hai lần.",
                "situation": "formal"
            },
            {
                "ko": "뇌사 상태로 판정되었습니다.",
                "vi": "Đã được xác định ở trạng thái chết não.",
                "situation": "onsite"
            },
            {
                "ko": "뇌사판정 후 장기기증이 가능합니다.",
                "vi": "Sau khi xác định chết não, có thể hiến tặng nội tạng.",
                "situation": "formal"
            }
        ],
        "relatedTerms": ["장기기증", "심폐소생술", "연명의료"]
    },
    {
        "slug": "thu-nghiem-lam-sang",
        "korean": "임상시험",
        "vietnamese": "Thử nghiệm lâm sàng",
        "hanja": "臨床試驗",
        "hanjaReading": "臨(임할 임) + 床(평상 상) + 試(시험할 시) + 驗(시험할 험)",
        "pronunciation": "임상시험",
        "meaningKo": "신약이나 의료기기의 안전성과 유효성을 확인하기 위해 사람을 대상으로 실시하는 시험입니다. 통역 시 주의할 점은 임상시험 참여는 자발적이며 언제든 중단할 수 있다는 점, 그리고 IRB(임상시험심사위원회) 승인을 받은 합법적 절차임을 명확히 해야 합니다. 베트남 환자가 한국에서 임상시험에 참여할 경우 보상·보험·부작용 대응 절차를 상세히 설명해야 오해를 방지할 수 있습니다.",
        "meaningVi": "Thử nghiệm được thực hiện trên con người nhằm xác nhận tính an toàn và hiệu quả của thuốc mới hoặc thiết bị y tế. Việc tham gia là tự nguyện và có thể rút lui bất cứ lúc nào.",
        "context": "신약 개발, 의료 연구, 환자 동의",
        "culturalNote": "한국은 식품의약품안전처(MFDS)의 엄격한 규제 하에 임상시험이 진행되며, 참여자 보호를 위한 법적 장치가 잘 마련되어 있습니다. 베트nam에서는 임상시험에 대한 인식이 낮고 '실험 대상'으로 오해받을 수 있어, 통역 시 참여자 권리(보상, 보험, 중도 포기 가능)를 명확히 전달해야 합니다.",
        "commonMistakes": [
            {
                "mistake": "Thí nghiệm",
                "correction": "Thử nghiệm lâm sàng",
                "explanation": "단순 실험이 아닌 임상시험이라는 의료 전문 용어를 사용해야 합니다."
            },
            {
                "mistake": "Bắt buộc tham gia",
                "correction": "Tự nguyện tham gia và có thể rút lui",
                "explanation": "강제가 아닌 자발적 참여임을 반드시 명확히 해야 합니다."
            },
            {
                "mistake": "Không được bồi thường",
                "correction": "Có bảo hiểm và chế độ bồi thường nếu xảy ra tác dụng phụ",
                "explanation": "부작용 발생 시 보상 체계가 있음을 전달해야 불안을 줄일 수 있습니다."
            }
        ],
        "examples": [
            {
                "ko": "이 임상시험은 IRB 승인을 받았습니다.",
                "vi": "Thử nghiệm lâm sàng này đã được Hội đồng Đạo đức Y sinh phê duyệt.",
                "situation": "formal"
            },
            {
                "ko": "참여는 자발적이며 언제든 중단 가능합니다.",
                "vi": "Tham gia là tự nguyện và có thể dừng lại bất cứ lúc nào.",
                "situation": "onsite"
            },
            {
                "ko": "부작용 발생 시 즉시 보고해주세요.",
                "vi": "Nếu xảy ra tác dụng phụ, vui lòng báo cáo ngay lập tức.",
                "situation": "onsite"
            }
        ],
        "relatedTerms": ["IRB", "신약개발", "약물이상반응"]
    },
    {
        "slug": "phan-ung-co-hai-thuoc",
        "korean": "약물이상반응",
        "vietnamese": "Phản ứng có hại của thuốc",
        "hanja": "藥物異常反應",
        "hanjaReading": "藥(약 약) + 物(만물 물) + 異(다를 이) + 常(항상 상) + 反(돌이킬 반) + 應(응할 응)",
        "pronunciation": "약물이상반응",
        "meaningKo": "의약품을 정상적으로 사용했음에도 발생하는 예상치 못한 유해한 반응을 의미합니다. 통역 시 주의할 점은 '부작용'과 '이상반응'을 구분해야 하며, 경미한 증상부터 생명을 위협하는 중증까지 범위가 넓으므로 증상의 심각도를 정확히 전달해야 합니다. 환자가 증상을 느끼면 즉시 보고해야 함을 강조하고, 한국의 약물이상반응 보고 시스템(KAERS)을 안내해야 합니다.",
        "meaningVi": "Phản ứng có hại không mong đợi xảy ra khi sử dụng thuốc theo đúng cách. Mức độ nghiêm trọng có thể từ nhẹ đến đe dọa tính mạng, và cần báo cáo ngay lập tức khi có triệu chứng.",
        "context": "약물 처방, 부작용 관찰, 응급 상황",
        "culturalNote": "한국은 약물이상반응을 한국의약품안전관리원(KIDS)에 보고하는 체계가 확립되어 있으며, 환자·의료진 모두 보고 의무가 있습니다. 베트남에서는 이상반응 보고 문화가 덜 발달되어 있고, 환자가 증상을 참거나 자가 판단으로 복용 중단하는 경우가 많아 통역 시 보고의 중요성을 강조해야 합니다.",
        "commonMistakes": [
            {
                "mistake": "Tác dụng phụ bình thường",
                "correction": "Phản ứng có hại (không phải tác dụng phụ thông thường)",
                "explanation": "예상된 부작용과 예상치 못한 이상반응을 구분해야 합니다."
            },
            {
                "mistake": "Tự ngừng thuốc",
                "correction": "Báo cáo bác sĩ trước khi ngừng thuốc",
                "explanation": "임의 중단이 아닌 의료진 상담 후 조치해야 함을 명확히 해야 합니다."
            },
            {
                "mistake": "Chỉ báo cáo phản ứng nặng",
                "correction": "Báo cáo mọi phản ứng bất thường, dù nhẹ",
                "explanation": "경미한 증상도 보고 대상임을 전달해야 안전합니다."
            }
        ],
        "examples": [
            {
                "ko": "약물이상반응이 의심되면 즉시 알려주세요.",
                "vi": "Nếu nghi ngờ có phản ứng có hại của thuốc, vui lòng thông báo ngay.",
                "situation": "onsite"
            },
            {
                "ko": "이 증상은 약물이상반응으로 보고하겠습니다.",
                "vi": "Triệu chứng này sẽ được báo cáo như phản ứng có hại của thuốc.",
                "situation": "formal"
            },
            {
                "ko": "심한 두드러기는 중증 이상반응일 수 있습니다.",
                "vi": "Mề đay nghiêm trọng có thể là phản ứng có hại mức độ nặng.",
                "situation": "onsite"
            }
        ],
        "relatedTerms": ["부작용", "알레르기", "아나필락시스"]
    },
    {
        "slug": "su-co-y-te",
        "korean": "의료사고",
        "vietnamese": "Sự cố y tế",
        "hanja": "醫療事故",
        "hanjaReading": "醫(의원 의) + 療(치료할 료) + 事(일 사) + 故(일 고)",
        "pronunciation": "의료사고",
        "meaningKo": "의료 행위 중 발생한 환자의 사망, 상해 등 예기치 못한 나쁜 결과를 의미합니다. 통역 시 주의할 점은 '의료사고'와 '의료과실'을 구분해야 하며, 한국의 의료분쟁조정제도와 보상 절차를 정확히 안내해야 합니다. 환자·가족이 감정적으로 대응하기 쉬운 상황이므로, 법적 권리(한국의료분쟁조정중재원 신청 등)를 냉정하게 전달하는 것이 중요합니다.",
        "meaningVi": "Kết quả xấu không mong đợi như tử vong, thương tích xảy ra trong quá trình điều trị y tế. Tại Hàn Quốc, có cơ chế hòa giải tranh chấp y tế và chế độ bồi thường.",
        "context": "의료 분쟁, 법률 상담, 보험 청구",
        "culturalNote": "한국은 한국의료분쟁조정중재원을 통해 의료사고 조정·중재를 체계적으로 진행하며, 의료사고 피해구제 및 의료분쟁 조정법이 시행되고 있습니다. 베트남은 의료사고 처리 절차가 덜 명확하고 보상 기준이 일관되지 않아, 한국에서 사고를 겪은 베트남 환자는 법적 절차를 이해하기 어려울 수 있으므로 통역 시 상세한 안내가 필요합니다.",
        "commonMistakes": [
            {
                "mistake": "Lỗi của bác sĩ",
                "correction": "Sự cố y tế (có thể do nhiều nguyên nhân, không chỉ lỗi bác sĩ)",
                "explanation": "의료사고가 모두 의료진 과실은 아니므로 원인을 단정 짓지 않아야 합니다."
            },
            {
                "mistake": "Không được bồi thường",
                "correction": "Có thể yêu cầu hòa giải và bồi thường qua cơ quan điều chỉnh",
                "explanation": "보상 청구 절차가 있음을 안내해야 환자 권리를 보호할 수 있습니다."
            },
            {
                "mistake": "Chỉ kiện tụng",
                "correction": "Có thể hòa giải trước khi kiện tụng",
                "explanation": "소송 전 조정 절차가 있음을 알려 불필요한 법적 비용을 줄일 수 있습니다."
            }
        ],
        "examples": [
            {
                "ko": "의료사고 발생 시 한국의료분쟁조정중재원에 신청할 수 있습니다.",
                "vi": "Khi xảy ra sự cố y tế, có thể nộp đơn lên Cơ quan Hòa giải Tranh chấp Y tế Hàn Quốc.",
                "situation": "formal"
            },
            {
                "ko": "사고 경위를 상세히 기록해두세요.",
                "vi": "Vui lòng ghi chép chi tiết diễn biến sự cố.",
                "situation": "onsite"
            },
            {
                "ko": "의료사고 보험으로 보상받을 수 있습니다.",
                "vi": "Có thể được bồi thường qua bảo hiểm sự cố y tế.",
                "situation": "formal"
            }
        ],
        "relatedTerms": ["의료과실", "의료분쟁조정", "환자 권리"]
    },
    {
        "slug": "hang-muc-khong-bao-hiem",
        "korean": "비급여항목",
        "vietnamese": "Hạng mục không bảo hiểm",
        "hanja": "非給與項目",
        "hanjaReading": "非(아닐 비) + 給(줄 급) + 與(줄 여) + 項(항목 항) + 目(눈 목)",
        "pronunciation": "비급여항목",
        "meaningKo": "건강보험이 적용되지 않아 환자가 전액 본인 부담으로 지불해야 하는 의료 항목을 의미합니다. 통역 시 주의할 점은 비급여 항목은 병원마다 가격이 다를 수 있으므로 사전 확인이 필요하며, 외국인 환자는 급여 혜택을 받지 못하는 경우가 많아 비용 부담이 크다는 점을 명확히 안내해야 합니다. 특히 고가의 비급여 항목(특수 검사, 상급병실료 등)은 비용 고지를 반드시 선행해야 분쟁을 예방할 수 있습니다.",
        "meaningVi": "Các hạng mục y tế không được bảo hiểm y tế chi trả, bệnh nhân phải tự trả toàn bộ chi phí. Giá có thể khác nhau giữa các bệnh viện và cần xác nhận trước.",
        "context": "진료비 상담, 보험 청구, 외국인 환자",
        "culturalNote": "한국 국민건강보험은 많은 항목을 보장하지만, 미용 목적, 특수 재료, 선택진료비 등은 비급여로 분류됩니다. 베트남은 공공보험 적용 범위가 한국보다 좁아 비급여 개념이 생소할 수 있으며, 외국인은 한국 보험 혜택을 받지 못하는 경우가 많아 통역 시 비용 부담을 충분히 설명해야 합니다.",
        "commonMistakes": [
            {
                "mistake": "Bảo hiểm sẽ chi trả",
                "correction": "Bảo hiểm không chi trả, bệnh nhân phải tự trả",
                "explanation": "비급여는 보험 적용 대상이 아니므로 명확히 구분해야 합니다."
            },
            {
                "mistake": "Giá cố định",
                "correction": "Giá có thể khác nhau giữa các bệnh viện",
                "explanation": "비급여는 병원이 자율적으로 책정하므로 가격 차이가 있음을 알려야 합니다."
            },
            {
                "mistake": "Người nước ngoài cũng được hưởng",
                "correction": "Người nước ngoài thường không được hưởng bảo hiểm y tế Hàn Quốc",
                "explanation": "외국인은 대부분 급여 혜택을 받지 못하므로 비용 부담을 미리 안내해야 합니다."
            }
        ],
        "examples": [
            {
                "ko": "이 검사는 비급여항목이라 전액 본인 부담입니다.",
                "vi": "Xét nghiệm này là hạng mục không bảo hiểm nên bệnh nhân phải tự trả toàn bộ.",
                "situation": "onsite"
            },
            {
                "ko": "비급여 항목은 병원마다 가격이 다릅니다.",
                "vi": "Hạng mục không bảo hiểm có giá khác nhau tùy bệnh viện.",
                "situation": "formal"
            },
            {
                "ko": "상급병실료는 비급여입니다.",
                "vi": "Phí phòng hạng sang là hạng mục không bảo hiểm.",
                "situation": "onsite"
            }
        ],
        "relatedTerms": ["본인부담금", "선택진료비", "건강보험"]
    },
    {
        "slug": "dac-le-tinh-phi",
        "korean": "산정특례",
        "vietnamese": "Đặc lệ tính phí",
        "hanja": "算定特例",
        "hanjaReading": "算(셈 산) + 定(정할 정) + 特(특별할 특) + 例(예 례)",
        "pronunciation": "산정특례",
        "meaningKo": "암, 희귀난치질환 등 중증질환 환자에게 본인부담률을 대폭 경감해주는 건강보험 제도입니다. 통역 시 주의할 점은 산정특례 등록 시 본인부담률이 5~10%로 낮아지며, 등록 절차와 갱신 주기(5년)를 정확히 안내해야 합니다. 외국인 환자는 이 제도를 모르는 경우가 많아 적극적으로 안내하면 의료비 부담을 크게 줄일 수 있습니다.",
        "meaningVi": "Chế độ giảm tỷ lệ chi trả của bệnh nhân xuống 5-10% đối với các bệnh nghiêm trọng như ung thư, bệnh hiếm gặp. Cần đăng ký và gia hạn mỗi 5 năm.",
        "context": "보험 상담, 중증질환 치료, 진료비 청구",
        "culturalNote": "한국 건강보험의 산정특례는 암, 심장질환, 희귀질환 등에 적용되며, 환자의 경제적 부담을 크게 줄여주는 핵심 제도입니다. 베트남에는 이러한 중증질환 특례 제도가 체계화되지 않아, 통역 시 등록 방법과 혜택을 상세히 설명하면 환자가 적극 활용할 수 있도록 도울 수 있습니다.",
        "commonMistakes": [
            {
                "mistake": "Miễn phí hoàn toàn",
                "correction": "Giảm xuống 5-10%, không phải miễn phí",
                "explanation": "전액 면제가 아니므로 정확한 부담률을 전달해야 기대 착오를 방지합니다."
            },
            {
                "mistake": "Tự động áp dụng",
                "correction": "Cần đăng ký tại bệnh viện",
                "explanation": "자동 적용이 아닌 등록 절차가 필요함을 명확히 해야 합니다."
            },
            {
                "mistake": "Áp dụng vĩnh viễn",
                "correction": "Cần gia hạn mỗi 5 năm",
                "explanation": "갱신 주기가 있으므로 기한을 안내해야 혜택이 중단되지 않습니다."
            }
        ],
        "examples": [
            {
                "ko": "암 진단을 받으시면 산정특례 등록이 가능합니다.",
                "vi": "Nếu được chẩn đoán ung thư, có thể đăng ký đặc lệ tính phí.",
                "situation": "formal"
            },
            {
                "ko": "산정특례 등록 시 본인부담률이 5%로 줄어듭니다.",
                "vi": "Khi đăng ký đặc lệ tính phí, tỷ lệ tự trả giảm xuống 5%.",
                "situation": "onsite"
            },
            {
                "ko": "5년마다 갱신해야 합니다.",
                "vi": "Cần gia hạn mỗi 5 năm.",
                "situation": "formal"
            }
        ],
        "relatedTerms": ["본인부담금", "건강보험", "중증질환"]
    },
    {
        "slug": "phi-tu-tra",
        "korean": "본인부담금",
        "vietnamese": "Phí tự trả",
        "hanja": "本人負擔金",
        "hanjaReading": "本(근본 본) + 人(사람 인) + 負(질 부) + 擔(멜 담) + 金(쇠 금)",
        "pronunciation": "본인부담금",
        "meaningKo": "건강보험 적용 항목 중 환자가 직접 부담해야 하는 금액을 의미하며, 일반적으로 진료비의 일정 비율(외래 30~60%, 입원 20% 등)입니다. 통역 시 주의할 점은 급여 항목이라도 본인부담금이 발생하며, 비급여는 전액 본인 부담이라는 차이를 명확히 구분해야 합니다. 외국인 환자는 보험 미가입 시 전액 본인 부담이므로, 사전에 비용 규모를 안내하는 것이 중요합니다.",
        "meaningVi": "Số tiền bệnh nhân phải tự trả trong các hạng mục được bảo hiểm chi trả, thường là tỷ lệ phần trăm của chi phí (ngoại trú 30-60%, nội trú 20%). Nếu không có bảo hiểm, phải trả toàn bộ.",
        "context": "진료비 계산, 보험 청구, 수납 안내",
        "culturalNote": "한국 건강보험은 대부분 의료 항목을 보장하지만 본인부담금이 있으며, 상급종합병원은 부담률이 더 높습니다. 베트남은 공공보험 적용 범위가 좁고 본인부담 비율이 높아, 한국의 본인부담금 개념을 설명할 때 '보험이 있어도 일부는 내야 한다'는 점을 명확히 해야 혼란을 방지할 수 있습니다.",
        "commonMistakes": [
            {
                "mistake": "Bảo hiểm chi trả hết",
                "correction": "Bảo hiểm chi trả một phần, bệnh nhân phải tự trả phần còn lại",
                "explanation": "보험 적용 항목도 본인부담금이 있음을 명확히 해야 합니다."
            },
            {
                "mistake": "Không có bảo hiểm thì không phải trả",
                "correction": "Không có bảo hiểm thì phải trả toàn bộ chi phí",
                "explanation": "보험 미가입 시 전액 부담임을 강조해야 비용 충격을 줄일 수 있습니다."
            },
            {
                "mistake": "Mọi bệnh viện đều như nhau",
                "correction": "Bệnh viện cấp cao hơn có tỷ lệ tự trả cao hơn",
                "explanation": "병원 등급에 따라 본인부담률이 다름을 안내해야 합니다."
            }
        ],
        "examples": [
            {
                "ko": "본인부담금은 진료비의 30%입니다.",
                "vi": "Phí tự trả là 30% chi phí khám chữa bệnh.",
                "situation": "onsite"
            },
            {
                "ko": "보험이 없으시면 전액 본인 부담입니다.",
                "vi": "Nếu không có bảo hiểm, phải tự trả toàn bộ chi phí.",
                "situation": "formal"
            },
            {
                "ko": "상급종합병원은 본인부담률이 더 높습니다.",
                "vi": "Bệnh viện tuyến cao có tỷ lệ tự trả cao hơn.",
                "situation": "formal"
            }
        ],
        "relatedTerms": ["비급여항목", "건강보험", "산정특례"]
    }
]

new_terms = [t for t in new_terms if t['slug'] not in existing_slugs]
data.extend(new_terms)

with open(file_path, 'w', encoding='utf-8') as f:
    json.dump(data, f, ensure_ascii=False, indent=2)

print(f"Added {len(new_terms)} new medical terms. Total: {len(data)}")
