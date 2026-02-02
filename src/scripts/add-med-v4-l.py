import json, os
file_path = os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', 'data', 'terms', 'medical.json')
with open(file_path, 'r', encoding='utf-8') as f:
    data = json.load(f)
existing_slugs = {t['slug'] for t in data}

new_terms = [
    {
        "slug": "cham-cuu",
        "korean": "침술",
        "vietnamese": "Châm cứu",
        "hanja": "鍼術",
        "hanjaReading": "鍼(바늘 침) + 術(재주 술)",
        "pronunciation": "참꾸",
        "meaningKo": "한의학의 대표적인 치료법으로 경혈에 침을 놓아 기혈 순환을 조절하고 질병을 치료하는 방법입니다. 통역 시 '침을 놓다'는 'châm kim'이지만 의료 행위로서는 'châm cứu'를 사용해야 하며, 베트남에서도 전통의학으로 인정받고 보험 적용이 되는 경우가 있으므로 'điều trị châm cứu có được bảo hiểm không?'과 같은 질문에 대비해야 합니다.",
        "meaningVi": "Phương pháp điều trị đặc trưng của y học cổ truyền Hàn Quốc bằng cách đâm kim vào các huyệt đạo để điều hòa khí huyết và chữa bệnh. Tại Việt Nam cũng được công nhận và có thể được bảo hiểm y tế chi trả.",
        "context": "한의원 진료, 재활치료, 통증 관리",
        "culturalNote": "한국에서는 침술이 의료보험 적용 대상이며 병원 내 한방과에서도 시술됩니다. 베트남에서도 'Y học cổ truyền'의 일부로 인정받지만 보험 적용 범위가 다를 수 있습니다. 한국 환자가 베트남에서 침술 치료를 받을 때 보험 적용 여부를 반드시 확인해야 합니다.",
        "commonMistakes": [
            {
                "mistake": "châm kim",
                "correction": "châm cứu",
                "explanation": "châm kim은 단순히 '침을 놓다'는 행위이고, châm cứu는 의료 행위로서의 침술 치료를 의미합니다."
            },
            {
                "mistake": "y học Trung Quốc",
                "correction": "y học cổ truyền Hàn Quốc / Hàn y học",
                "explanation": "한국 한의학은 중국 전통의학과 구분되는 독자적인 체계를 가지고 있으므로 반드시 구분해야 합니다."
            },
            {
                "mistake": "đâm kim",
                "correction": "châm cứu",
                "explanation": "đâm은 '찌르다'는 의미로 의료 행위를 표현하기에 부적절하며, 전문 용어인 châm cứu를 사용해야 합니다."
            }
        ],
        "examples": [
            {
                "ko": "허리 통증에 침술 치료를 받고 싶은데 보험 적용이 되나요?",
                "vi": "Tôi muốn điều trị châm cứu cho chứng đau lưng, có được bảo hiểm chi trả không?",
                "situation": "formal"
            },
            {
                "ko": "이 한의원에서는 침술과 뜸치료를 같이 받을 수 있습니다.",
                "vi": "Tại phòng khám Đông y này, bạn có thể điều trị kết hợp châm cứu và cứu ngải.",
                "situation": "formal"
            },
            {
                "ko": "침 맞고 나서 몸이 한결 가벼워졌어요.",
                "vi": "Sau khi châm cứu, cơ thể tôi đã nhẹ nhõm hơn rất nhiều.",
                "situation": "informal"
            }
        ],
        "relatedTerms": ["cuu-ngai", "kinh-lac", "huyet-dao", "phong-kham-dong-y"]
    },
    {
        "slug": "cuu-ngai",
        "korean": "뜸치료",
        "vietnamese": "Cứu ngải",
        "hanja": None,
        "hanjaReading": None,
        "pronunciation": "꾸응아이",
        "meaningKo": "쑥을 태워 경혈을 따뜻하게 하여 기혈 순환을 촉진하고 질병을 치료하는 한의학적 치료법입니다. 통역 시 '뜸뜨다'를 직역하지 말고 'cứu ngải' 또는 'giác hơi'과 혼동하지 않도록 주의해야 합니다. 베트남에서는 쑥을 사용하는 전통 요법이 있으나 한국의 뜸치료와는 방식이 다를 수 있으므로 'phương pháp cứu ngải Hàn Quốc'으로 명확히 해야 합니다.",
        "meaningVi": "Phương pháp điều trị bằng cách đốt ngải cứu để sưởi ấm huyệt đạo, thúc đẩy tuần hoàn khí huyết và chữa bệnh trong y học cổ truyền. Khác với giác hơi, cứu ngải sử dụng nhiệt từ ngải cứu đốt.",
        "context": "한방 물리치료, 냉증 치료, 면역력 강화",
        "culturalNote": "한국에서는 뜸치료가 침술과 함께 한의원의 기본 치료법입니다. 베트남에도 유사한 전통 요법이 있지만 'giác hơi'(부항)와 혼동되기 쉽습니다. 뜸은 열을 이용하고 giác hơi는 음압을 이용한다는 차이를 명확히 설명해야 합니다.",
        "commonMistakes": [
            {
                "mistake": "giác hơi",
                "correction": "cứu ngải",
                "explanation": "giác hơi는 부항(컵을 이용한 음압 치료)이고, cứu ngải는 쑥을 태워 열을 이용하는 뜸치료입니다."
            },
            {
                "mistake": "đốt ngải",
                "correction": "cứu ngải / điều trị cứu ngải",
                "explanation": "đốt ngải는 단순히 '쑥을 태우다'는 의미이고, 의료 행위로는 cứu ngải라는 전문 용어를 사용해야 합니다."
            },
            {
                "mistake": "xông hơi ngải cứu",
                "correction": "cứu ngải",
                "explanation": "xông hơi는 증기 치료를 의미하며, 뜸치료는 직접 열을 가하는 방식이므로 구분해야 합니다."
            }
        ],
        "examples": [
            {
                "ko": "수족냉증이 있어서 뜸치료를 받고 있습니다.",
                "vi": "Tôi bị lạnh tay chân nên đang điều trị bằng cứu ngải.",
                "situation": "formal"
            },
            {
                "ko": "침과 뜸을 같이 받으면 효과가 더 좋습니다.",
                "vi": "Kết hợp châm cứu và cứu ngải sẽ cho hiệu quả tốt hơn.",
                "situation": "formal"
            },
            {
                "ko": "뜸 뜨고 나니까 배가 따뜻해졌어요.",
                "vi": "Sau khi cứu ngải, bụng tôi ấm hơn nhiều.",
                "situation": "informal"
            }
        ],
        "relatedTerms": ["cham-cuu", "kinh-lac", "phong-kham-dong-y", "nan-chinh-cot-song"]
    },
    {
        "slug": "ke-don-thuoc-dong-y",
        "korean": "한약처방",
        "vietnamese": "Kê đơn thuốc Đông y",
        "hanja": "韓藥處方",
        "hanjaReading": "韓(나라 한) + 藥(약 약) + 處(곳 처) + 方(모 방)",
        "pronunciation": "께던툭동이",
        "meaningKo": "한의사가 환자의 체질과 증상에 맞춰 약재를 배합하여 처방하는 것입니다. 통역 시 '처방전'은 'đơn thuốc'이고, '처방하다'는 'kê đơn'입니다. 베트남에서도 전통의학 처방이 있으나 한국 한약은 제조 과정과 품질 기준이 다르므로 'thuốc Đông y Hàn Quốc'으로 명확히 구분해야 하며, 한국에서 처방받은 한약을 베트남으로 반입할 때 세관 신고가 필요할 수 있습니다.",
        "meaningVi": "Bác sĩ Đông y kê đơn phối hợp các vị thuốc phù hợp với thể chất và triệu chứng của bệnh nhân. Thuốc Đông y Hàn Quốc có quy trình sản xuất và tiêu chuẩn chất lượng khác với thuốc Bắc truyền thống.",
        "context": "한의원 진료, 만성질환 관리, 체질 개선",
        "culturalNote": "한국 한약은 GMP 인증 시설에서 생산되며 건강보험 적용이 가능합니다. 베트남의 'thuốc Bắc'과 유사하지만 약재 배합 비율과 제조법이 다릅니다. 한국 환자가 베트남에서 한약 처방을 받을 때는 약재의 출처와 품질을 확인하도록 안내해야 합니다.",
        "commonMistakes": [
            {
                "mistake": "đơn thuốc Trung Quốc",
                "correction": "đơn thuốc Đông y Hàn Quốc",
                "explanation": "한국 한약은 중국 약재와 처방 체계가 다르므로 반드시 '한국 한약'임을 명시해야 합니다."
            },
            {
                "mistake": "thuốc Nam",
                "correction": "thuốc Đông y Hàn Quốc",
                "explanation": "thuốc Nam은 베트남 남부 전통약을 의미하며, 한국 한약과는 전혀 다른 체계입니다."
            },
            {
                "mistake": "viết đơn thuốc",
                "correction": "kê đơn thuốc Đông y",
                "explanation": "의료 용어로는 viết보다 kê đơn이 더 전문적이고 정확한 표현입니다."
            }
        ],
        "examples": [
            {
                "ko": "한의사 선생님이 제 체질에 맞는 한약을 처방해 주셨습니다.",
                "vi": "Bác sĩ Đông y đã kê đơn thuốc phù hợp với thể chất của tôi.",
                "situation": "formal"
            },
            {
                "ko": "이 한약 처방전을 약국에 가져가면 약을 지어줍니다.",
                "vi": "Mang đơn thuốc Đông y này đến nhà thuốc thì họ sẽ thang thuốc cho bạn.",
                "situation": "formal"
            },
            {
                "ko": "한약 먹고 나서 소화가 잘 되기 시작했어요.",
                "vi": "Sau khi uống thuốc Đông y, tôi bắt đầu tiêu hóa tốt hơn.",
                "situation": "informal"
            }
        ],
        "relatedTerms": ["noi-khoa-dong-y", "tu-tuong-the-chat", "phong-kham-dong-y", "cham-cuu"]
    },
    {
        "slug": "nan-chinh-cot-song",
        "korean": "추나요법",
        "vietnamese": "Nắn chỉnh cột sống",
        "hanja": None,
        "hanjaReading": None,
        "pronunciation": "넌찡꼿송",
        "meaningKo": "한의학에서 손이나 신체 일부를 이용하여 척추와 관절을 교정하는 수기 치료법입니다. 통역 시 '추나'는 고유명사이므로 'Chuna' 또는 설명적으로 'nắn chỉnh cột sống theo phương pháp Đông y'로 표현하며, 단순 마사지나 카이로프랙틱과 구분해야 합니다. 2019년부터 한국에서 건강보험이 적용되므로 베트남 환자가 한국에서 치료받을 때 보험 혜택을 받을 수 있습니다.",
        "meaningVi": "Phương pháp điều trị bằng tay trong y học cổ truyền Hàn Quốc, sử dụng tay hoặc một phần cơ thể để chỉnh sửa cột sống và khớp xương. Khác với mát-xa thông thường hay chiropractic, đây là kỹ thuật đặc trưng của Hàn y học.",
        "context": "척추질환, 디스크 치료, 자세 교정",
        "culturalNote": "한국에서 추나요법은 한의사만 시술할 수 있으며 2019년부터 건강보험 적용 대상입니다. 베트남의 'bấm huyệt' 또는 일반 마사지와는 다른 의료 행위이므로 명확히 구분해야 합니다. 치료 전 X-ray 촬영이 필요할 수 있습니다.",
        "commonMistakes": [
            {
                "mistake": "mát-xa Hàn Quốc",
                "correction": "nắn chỉnh cột sống Chuna",
                "explanation": "추나요법은 단순 마사지가 아니라 척추 교정을 위한 의료 행위입니다."
            },
            {
                "mistake": "chiropractic",
                "correction": "Chuna (phương pháp nắn chỉnh cột sống Hàn Quốc)",
                "explanation": "카이로프랙틱과 추나는 원리와 기법이 다른 별개의 치료법입니다."
            },
            {
                "mistake": "bấm huyệt",
                "correction": "nắn chỉnh cột sống Chuna",
                "explanation": "bấm huyệt은 경혈을 누르는 지압이고, 추나는 척추와 관절을 교정하는 수기 치료입니다."
            }
        ],
        "examples": [
            {
                "ko": "허리디스크가 있어서 추나요법 치료를 받고 있습니다.",
                "vi": "Tôi bị thoát vị đĩa đệm nên đang điều trị bằng phương pháp Chuna.",
                "situation": "formal"
            },
            {
                "ko": "추나요법은 건강보험이 적용되니까 부담이 적습니다.",
                "vi": "Phương pháp Chuna được bảo hiểm y tế chi trả nên chi phí không cao.",
                "situation": "formal"
            },
            {
                "ko": "추나 받고 나니까 목이 훨씬 편해졌어요.",
                "vi": "Sau khi nắn chỉnh cột sống, cổ tôi đã thoải mái hơn rất nhiều.",
                "situation": "informal"
            }
        ],
        "relatedTerms": ["cham-cuu", "cuu-ngai", "noi-khoa-dong-y", "phong-kham-dong-y"]
    },
    {
        "slug": "tu-tuong-the-chat",
        "korean": "사상체질",
        "vietnamese": "Tứ tượng thể chất",
        "hanja": "四象體質",
        "hanjaReading": "四(넉 사) + 象(모양 상) + 體(몸 체) + 質(바탕 질)",
        "pronunciation": "뜨뜨엉테쨋",
        "meaningKo": "이제마가 창시한 한국 고유의 체질 분류법으로 태양인, 태음인, 소양인, 소음인 4가지로 나눕니다. 통역 시 각 체질명은 'Thái Dương nhân(태양인), Thái Âm nhân(태음인), Thiểu Dương nhân(소양인), Thiểu Âm nhân(소음인)'으로 표기하며, 중국 전통의학의 체질론과는 다른 한국 독자적인 이론임을 강조해야 합니다. 체질에 따라 처방과 식이요법이 달라지므로 정확한 번역이 매우 중요합니다.",
        "meaningVi": "Lý thuyết phân loại thể chất độc đáo của Hàn Quốc do Y sĩ Lee Je-ma sáng lập, chia làm 4 loại: Thái Dương nhân, Thái Âm nhân, Thiểu Dương nhân, Thiểu Âm nhân. Đây là lý thuyết riêng của y học Hàn Quốc, khác với các học thuyết y học cổ truyền Trung Quốc.",
        "context": "한방 진단, 체질별 처방, 건강관리",
        "culturalNote": "사상체질은 한국에서만 발전한 독특한 의학 이론으로 베트남이나 중국 전통의학에는 없는 개념입니다. 체질 진단 후 그에 맞는 음식, 약재, 생활습관을 권장하므로 체질명 번역이 정확해야 합니다. 베트nam 환자에게는 이 개념 자체를 설명하는 시간이 필요할 수 있습니다.",
        "commonMistakes": [
            {
                "mistake": "cơ địa",
                "correction": "Tứ tượng thể chất / thể chất Tứ tượng",
                "explanation": "cơ địa는 일반적인 '체질'을 의미하고, 사상체질은 특정한 4가지 분류 체계를 가진 전문 용어입니다."
            },
            {
                "mistake": "âm dương ngũ hành",
                "correction": "Tứ tượng thể chất",
                "explanation": "음양오행은 중국 전통의학의 기본 이론이고, 사상체질은 한국 고유의 체질 분류법입니다."
            },
            {
                "mistake": "4 loại cơ địa",
                "correction": "Tứ tượng thể chất (Thái Dương, Thái Âm, Thiểu Dương, Thiểu Âm)",
                "explanation": "단순히 '4가지 체질'이 아니라 고유명사로서 '사상체질'임을 명확히 해야 합니다."
            }
        ],
        "examples": [
            {
                "ko": "사상체질 진단을 받고 나서 내 체질에 맞는 한약을 처방받았습니다.",
                "vi": "Sau khi được chẩn đoán Tứ tượng thể chất, tôi được kê đơn thuốc Đông y phù hợp với thể chất của mình.",
                "situation": "formal"
            },
            {
                "ko": "저는 소음인 체질이라서 찬 음식을 피하는 게 좋대요.",
                "vi": "Tôi thuộc thể chất Thiểu Âm nhân nên nên tránh đồ ăn lạnh.",
                "situation": "informal"
            },
            {
                "ko": "체질에 맞는 음식을 먹으니까 건강이 많이 좋아졌어요.",
                "vi": "Ăn đúng thức ăn phù hợp với thể chất nên sức khỏe tôi đã tốt hơn nhiều.",
                "situation": "informal"
            }
        ],
        "relatedTerms": ["ke-don-thuoc-dong-y", "noi-khoa-dong-y", "phong-kham-dong-y", "cham-cuu"]
    },
    {
        "slug": "kinh-lac",
        "korean": "경락",
        "vietnamese": "Kinh lạc",
        "hanja": "經絡",
        "hanjaReading": "經(지날 경) + 絡(이을 락)",
        "pronunciation": "낑락",
        "meaningKo": "한의학에서 인체의 기혈이 흐르는 통로를 의미하며, 12개의 정경과 기경팔맥으로 구성됩니다. 통역 시 '경락'은 'kinh lạc', '경혈'은 'huyệt đạo'로 구분하며, 침술과 뜸치료의 이론적 기반이 됩니다. 베트남 전통의학에서도 동일한 개념을 사용하지만 명칭과 위치가 약간 다를 수 있으므로 한국 한의학 기준임을 명시해야 합니다.",
        "meaningVi": "Trong y học cổ truyền, kinh lạc là đường dẫn khí huyết trong cơ thể, bao gồm 12 kinh chính và bát mạch kỳ kinh. Đây là nền tảng lý thuyết cho châm cứu và cứu ngải.",
        "context": "침술 이론, 한의학 진단, 경혈 설명",
        "culturalNote": "경락 이론은 한국, 중국, 베트남 전통의학에 공통적으로 존재하지만 경혈의 위치와 명칭에 약간의 차이가 있을 수 있습니다. 통역 시 '12정경'은 '12 kinh chính', '기경팔맥'은 'Bát mạch kỳ kinh'으로 표현하며, 환자에게 설명할 때는 시각 자료를 활용하는 것이 효과적입니다.",
        "commonMistakes": [
            {
                "mistake": "huyệt đạo",
                "correction": "kinh lạc",
                "explanation": "huyệt đạo는 경혈(특정 점)이고, kinh lạc은 경락(기혈이 흐르는 길)입니다."
            },
            {
                "mistake": "đường dẫn máu",
                "correction": "kinh lạc (đường dẫn khí huyết)",
                "explanation": "경락은 단순히 혈관이 아니라 '기'와 '혈'이 함께 흐르는 통로입니다."
            },
            {
                "mistake": "mạch máu",
                "correction": "kinh lạc",
                "explanation": "mạch máu는 현대의학의 혈관이고, kinh lạc은 한의학의 경락으로 개념이 다릅니다."
            }
        ],
        "examples": [
            {
                "ko": "경락의 흐름이 막혀서 통증이 생긴 것 같습니다.",
                "vi": "Có vẻ như kinh lạc bị tắc nghẽn nên gây ra đau đớn.",
                "situation": "formal"
            },
            {
                "ko": "침술은 경락을 소통시켜 기혈 순환을 원활하게 합니다.",
                "vi": "Châm cứu giúp thông kinh lạc, làm cho khí huyết lưu thông.",
                "situation": "formal"
            },
            {
                "ko": "경락 마사지 받고 나니까 몸이 가벼워졌어요.",
                "vi": "Sau khi massage kinh lạc, cơ thể tôi nhẹ nhõm hơn nhiều.",
                "situation": "informal"
            }
        ],
        "relatedTerms": ["huyet-dao", "cham-cuu", "cuu-ngai", "noi-khoa-dong-y"]
    },
    {
        "slug": "huyet-dao",
        "korean": "경혈",
        "vietnamese": "Huyệt đạo",
        "hanja": "經穴",
        "hanjaReading": "經(지날 경) + 穴(구멍 혈)",
        "pronunciation": "휴엣다오",
        "meaningKo": "경락 위에 위치한 특정 지점으로 침이나 뜸을 놓는 자리입니다. 통역 시 '경혈'은 'huyệt đạo', '혈자리'는 'vị trí huyệt'로 표현하며, 환자에게 위치를 설명할 때는 '합곡혈(Hợp Cốc huyệt)', '족삼리혈(Túc Tam Lý huyệt)' 등 구체적인 혈명을 사용해야 합니다. 경혈의 위치는 정확해야 하므로 통역사는 주요 경혈의 베트남어 명칭을 숙지하는 것이 좋습니다.",
        "meaningVi": "Các điểm đặc biệt trên kinh lạc, nơi đặt kim châm hoặc cứu ngải. Vị trí của huyệt đạo phải chính xác để điều trị hiệu quả.",
        "context": "침술 시술, 경혈 설명, 자가 지압",
        "culturalNote": "경혈은 한국과 베트남 전통의학에서 공통적으로 사용되지만 명칭이 한자음으로 약간 다를 수 있습니다. 예를 들어 '합곡혈'은 베트nam어로 'Hợp Cốc huyệt', '족삼리'는 'Túc Tam Lý'입니다. 통역 시 한국 발음과 베트남 발음을 모두 알려주면 환자 이해에 도움이 됩니다.",
        "commonMistakes": [
            {
                "mistake": "kinh lạc",
                "correction": "huyệt đạo",
                "explanation": "kinh lạc은 경락(길)이고, huyệt đạo는 경혈(점)입니다."
            },
            {
                "mistake": "điểm châm",
                "correction": "huyệt đạo",
                "explanation": "điểm châm은 '침을 놓는 점'이라는 일반적 표현이고, huyệt đạo는 정확한 의학 용어입니다."
            },
            {
                "mistake": "chỗ châm kim",
                "correction": "huyệt đạo",
                "explanation": "구어체보다는 전문 용어인 huyệt đạo를 사용해야 의료 현장에서 정확합니다."
            }
        ],
        "examples": [
            {
                "ko": "합곡혈을 누르면 두통에 효과가 있습니다.",
                "vi": "Ấn vào huyệt Hợp Cốc có hiệu quả với chứng đau đầu.",
                "situation": "formal"
            },
            {
                "ko": "이 경혈에 침을 놓으면 소화가 잘 됩니다.",
                "vi": "Châm vào huyệt đạo này sẽ giúp tiêu hóa tốt hơn.",
                "situation": "formal"
            },
            {
                "ko": "잠들기 전에 족삼리 혈자리를 눌러주세요.",
                "vi": "Trước khi ngủ, hãy ấn vào huyệt Túc Tam Lý nhé.",
                "situation": "informal"
            }
        ],
        "relatedTerms": ["kinh-lac", "cham-cuu", "cuu-ngai", "noi-khoa-dong-y"]
    },
    {
        "slug": "noi-khoa-dong-y",
        "korean": "한방내과",
        "vietnamese": "Nội khoa Đông y",
        "hanja": "韓方內科",
        "hanjaReading": "韓(나라 한) + 方(모 방) + 內(안 내) + 科(과목 과)",
        "pronunciation": "노이콰동이",
        "meaningKo": "한의학에서 약물 치료를 주로 하는 진료과로 소화기, 호흡기, 순환기 질환 등을 다룹니다. 통역 시 '내과'는 'nội khoa'이지만 반드시 'Đông y'를 붙여 현대의학 내과(nội khoa Tây y)와 구분해야 합니다. 한방내과에서는 한약 처방이 주 치료법이며, 침술, 뜸, 부항 등을 병행할 수 있습니다.",
        "meaningVi": "Khoa điều trị bằng thuốc trong y học cổ truyền Hàn Quốc, chuyên về các bệnh tiêu hóa, hô hấp, tuần hoàn. Điều trị chủ yếu bằng thuốc Đông y, kết hợp châm cứu, cứu ngải, giác hơi.",
        "context": "한의원 진료, 만성질환 관리, 체질 치료",
        "culturalNote": "한국 한방내과는 현대의학 내과와 협진하는 경우가 많으며, 건강보험이 적용됩니다. 베트남에서는 'Khoa Y học cổ truyền'이 있지만 한국의 한방내과와 진료 범위나 보험 적용 기준이 다를 수 있습니다. 한국 환자가 베트남에서 진료받을 때는 진료 범위를 미리 확인해야 합니다.",
        "commonMistakes": [
            {
                "mistake": "nội khoa",
                "correction": "nội khoa Đông y",
                "explanation": "nội khoa만 쓰면 현대의학 내과로 오해될 수 있으므로 반드시 Đông y를 붙여야 합니다."
            },
            {
                "mistake": "khoa Y học cổ truyền",
                "correction": "nội khoa Đông y Hàn Quốc",
                "explanation": "일반적인 전통의학과와 한국 한방내과를 구분하려면 '한국'을 명시해야 합니다."
            },
            {
                "mistake": "bác sĩ đa khoa Đông y",
                "correction": "bác sĩ nội khoa Đông y",
                "explanation": "한방내과는 특정 전문과이므로 '다과'가 아닌 '내과'로 표현해야 합니다."
            }
        ],
        "examples": [
            {
                "ko": "만성 소화불량이 있어서 한방내과에서 진료를 받고 있습니다.",
                "vi": "Tôi bị khó tiêu mãn tính nên đang điều trị tại khoa nội Đông y.",
                "situation": "formal"
            },
            {
                "ko": "한방내과에서는 한약과 침을 같이 처방합니다.",
                "vi": "Khoa nội Đông y kê đơn kết hợp thuốc Đông y và châm cứu.",
                "situation": "formal"
            },
            {
                "ko": "한방내과 진료 보험 적용 되나요?",
                "vi": "Khám tại nội khoa Đông y có được bảo hiểm chi trả không?",
                "situation": "formal"
            }
        ],
        "relatedTerms": ["ke-don-thuoc-dong-y", "tu-tuong-the-chat", "cham-cuu", "phong-kham-dong-y"]
    },
    {
        "slug": "tiem-thuoc-dong-y",
        "korean": "약침",
        "vietnamese": "Tiêm thuốc Đông y",
        "hanja": "藥鍼",
        "hanjaReading": "藥(약 약) + 鍼(바늘 침)",
        "pronunciation": "띠엠툭동이",
        "meaningKo": "한약 성분을 정제하여 경혈에 주입하는 한의학 치료법으로, 침술의 효과와 약물의 효과를 동시에 얻을 수 있습니다. 통역 시 단순히 '주사'(tiêm)가 아니라 'tiêm thuốc Đông y vào huyệt đạo'로 설명해야 하며, 현대의학의 주사 치료와는 다른 개념임을 강조해야 합니다. 약침은 한국에서 개발된 독특한 치료법으로 베트남 전통의학에는 없는 개념입니다.",
        "meaningVi": "Phương pháp điều trị tiêm tinh chất thuốc Đông y vào huyệt đạo, kết hợp hiệu quả của châm cứu và thuốc. Đây là kỹ thuật độc đáo do Hàn Quốc phát triển, không có trong y học cổ truyền Việt Nam.",
        "context": "통증 치료, 염증 완화, 면역 강화",
        "culturalNote": "약침은 한국에서 1960년대에 개발된 고유 치료법으로 중국이나 베트남 전통의학에는 없습니다. 멸균 처리된 한약 추출물을 사용하며, 건강보험 적용 대상입니다. 베트남 환자에게는 이 치료법 자체를 처음부터 설명해야 하며, 일반 주사와의 차이점을 명확히 해야 합니다.",
        "commonMistakes": [
            {
                "mistake": "tiêm thuốc Tây",
                "correction": "tiêm thuốc Đông y vào huyệt đạo",
                "explanation": "약침은 현대의학의 주사(tiêm thuốc Tây)가 아니라 경혈에 한약 추출물을 주입하는 한의학 치료입니다."
            },
            {
                "mistake": "châm cứu với thuốc",
                "correction": "tiêm thuốc Đông y (dược châm)",
                "explanation": "침술과 약침은 다른 치료법으로, 약침은 약물을 주입하는 것입니다."
            },
            {
                "mistake": "tiêm vào tĩnh mạch",
                "correction": "tiêm vào huyệt đạo",
                "explanation": "약침은 정맥이 아니라 경혈에 주입합니다."
            }
        ],
        "examples": [
            {
                "ko": "무릎 관절염에 봉약침 치료를 받았습니다.",
                "vi": "Tôi đã được điều trị bằng tiêm thuốc Đông y từ nọc ong cho bệnh viêm khớp gối.",
                "situation": "formal"
            },
            {
                "ko": "약침은 경혈에 직접 약물을 주입하여 효과가 빠릅니다.",
                "vi": "Tiêm thuốc Đông y vào huyệt đạo nên có hiệu quả nhanh chóng.",
                "situation": "formal"
            },
            {
                "ko": "약침 맞고 나서 어깨 통증이 많이 줄었어요.",
                "vi": "Sau khi tiêm thuốc Đông y, đau vai của tôi đã giảm đáng kể.",
                "situation": "informal"
            }
        ],
        "relatedTerms": ["cham-cuu", "huyet-dao", "ke-don-thuoc-dong-y", "noi-khoa-dong-y"]
    },
    {
        "slug": "phong-kham-dong-y",
        "korean": "한의원",
        "vietnamese": "Phòng khám Đông y",
        "hanja": "韓醫院",
        "hanjaReading": "韓(나라 한) + 醫(의원 의) + 院(집 원)",
        "pronunciation": "퐁캄동이",
        "meaningKo": "한의사가 진료하는 의료기관으로 침술, 뜸, 한약 처방, 추나 등의 치료를 제공합니다. 통역 시 '한의원'은 'phòng khám Đông y' 또는 'phòng khám Y học cổ truyền Hàn Quốc'으로 표현하며, 일반 병원(bệnh viện Tây y)과 구분해야 합니다. 한국의 한의원은 건강보험이 적용되며, X-ray 등 현대 진단 장비를 갖춘 곳도 많습니다.",
        "meaningVi": "Cơ sở y tế nơi bác sĩ Đông y khám chữa bệnh, cung cấp các liệu pháp như châm cứu, cứu ngải, kê đơn thuốc Đông y, nắn chỉnh cột sống. Tại Hàn Quốc, nhiều phòng khám Đông y được trang bị thiết bị chẩn đoán hiện đại như X-quang.",
        "context": "의료기관 안내, 진료 예약, 치료 상담",
        "culturalNote": "한국의 한의원은 1차 의료기관으로 자유롭게 방문할 수 있으며, 건강보험 적용이 가능합니다. 베트남의 'phòng khám Y học cổ truyền'과 유사하지만 진료 범위와 시설 수준이 다를 수 있습니다. 베트남 환자가 한국 한의원을 처음 방문할 때는 진료 절차와 비용을 미리 안내하는 것이 좋습니다.",
        "commonMistakes": [
            {
                "mistake": "bệnh viện Đông y",
                "correction": "phòng khám Đông y",
                "explanation": "한의원은 일반적으로 '의원' 규모이므로 bệnh viện(병원)보다 phòng khám이 더 적절합니다."
            },
            {
                "mistake": "phòng khám Y học cổ truyền Trung Quốc",
                "correction": "phòng khám Đông y Hàn Quốc",
                "explanation": "한국 한의학은 중국 전통의학과 구분되므로 '한국'을 명시해야 합니다."
            },
            {
                "mistake": "nhà thuốc Đông y",
                "correction": "phòng khám Đông y",
                "explanation": "nhà thuốc는 약국이고, phòng khám은 의원(진료소)입니다."
            }
        ],
        "examples": [
            {
                "ko": "근처에 평판 좋은 한의원이 어디 있나요?",
                "vi": "Gần đây có phòng khám Đông y uy tín nào không?",
                "situation": "formal"
            },
            {
                "ko": "이 한의원은 토요일에도 진료를 합니다.",
                "vi": "Phòng khám Đông y này cũng khám vào thứ Bảy.",
                "situation": "formal"
            },
            {
                "ko": "한의원에서 침 맞고 약도 지어왔어요.",
                "vi": "Tôi đã châm cứu và lấy thuốc Đông y ở phòng khám.",
                "situation": "informal"
            }
        ],
        "relatedTerms": ["cham-cuu", "ke-don-thuoc-dong-y", "noi-khoa-dong-y", "nan-chinh-cot-song"]
    }
]

# Filter out duplicates
new_terms = [t for t in new_terms if t['slug'] not in existing_slugs]

# Add to data
data.extend(new_terms)

# Save
with open(file_path, 'w', encoding='utf-8') as f:
    json.dump(data, f, ensure_ascii=False, indent=2)

print(f"Added {len(new_terms)} new medical terms. Total: {len(data)} terms.")
