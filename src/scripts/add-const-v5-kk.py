import json, os
file_path = os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', 'data', 'terms', 'construction.json')
with open(file_path, 'r', encoding='utf-8') as f:
    data = json.load(f)
existing_slugs = {t['slug'] for t in data}
new_terms = [
    {
        "slug": "vach-ngan-partition",
        "korean": "파티션",
        "vietnamese": "Vách ngăn (Partition)",
        "hanja": None,
        "hanjaReading": None,
        "pronunciation": "파티션",
        "meaningKo": "사무실이나 실내 공간을 나누는 가동식 또는 고정식 칸막이. 베트남에서는 'vách ngăn' 또는 'partition'으로 통용되며, 통역 시 재질(알루미늄, 유리, 석고보드 등)과 설치 방식(고정형/이동형)을 명확히 구분해야 함. 베트남 현장에서는 영어 'partition'을 그대로 사용하는 경우가 많으니 주의. 한국에서는 '칸막이', '파티션'을 혼용하나 베트남에서는 공식 문서에 'vách ngăn' 표기가 일반적.",
        "meaningVi": "Tấm ngăn di động hoặc cố định để chia không gian văn phòng hoặc nội thất. Thường được gọi là 'partition' trong tiếng Anh và 'vách ngăn' trong tiếng Việt, cần phân biệt rõ chất liệu (nhôm, kính, thạch cao) và cách lắp đặt (cố định/di động).",
        "context": "사무실 인테리어, 공간 분할",
        "culturalNote": "한국 사무실에서는 개방형 파티션이 많지만, 베트남에서는 아직 완전 밀폐형 파티션을 선호하는 경우가 많음. 또한 베트남 현장에서는 'vách ngăn di động'(이동식)과 'vách ngăn cố định'(고정식)을 엄격히 구분하여 발주하므로 통역 시 반드시 확인 필요.",
        "commonMistakes": [
            {
                "mistake": "'파티션'을 'tường' (벽)으로 번역",
                "correction": "'vách ngăn' 또는 'partition' 사용",
                "explanation": "Tường는 영구적 벽체를 뜻하므로 가동식/임시 칸막이인 파티션과 개념이 다름"
            },
            {
                "mistake": "재질 구분 없이 일괄 번역",
                "correction": "vách ngăn kính (유리), vách ngăn nhôm kính (알루미늄), vách ngăn thạch cao (석고보드) 등 재질 명시",
                "explanation": "베트남 현장에서는 재질에 따라 단가와 시공법이 크게 다르므로 반드시 구분 필요"
            },
            {
                "mistake": "'이동식 파티션'을 'vách di chuyển'로 직역",
                "correction": "'vách ngăn di động' 사용",
                "explanation": "'Di chuyển'는 '이동하다'의 동사형이고, 'di động'이 '이동식'의 형용사형"
            }
        ],
        "examples": [
            {
                "ko": "사무실 파티션은 알루미늄 프레임에 유리로 시공합니다.",
                "vi": "Vách ngăn văn phòng được thi công bằng khung nhôm và kính.",
                "situation": "formal"
            },
            {
                "ko": "이 파티션 높이를 2.4미터로 맞춰주세요.",
                "vi": "Vui lòng điều chỉnh chiều cao vách ngăn này thành 2.4 mét.",
                "situation": "onsite"
            },
            {
                "ko": "회의실 파티션은 방음 성능이 중요합니다.",
                "vi": "Vách ngăn phòng họp cần có khả năng cách âm tốt.",
                "situation": "formal"
            }
        ],
        "relatedTerms": ["칸막이", "간이벽", "사무실 인테리어", "석고보드", "유리공사"]
    },
    {
        "slug": "tam-op-tran-luoi",
        "korean": "천장루버",
        "vietnamese": "Tấm ốp trần lưới (Louver ceiling)",
        "hanja": "天障",
        "hanjaReading": "天(하늘 천) + 障(막을 장)",
        "pronunciation": "천장루버",
        "meaningKo": "천장에 설치하는 격자형 또는 판형 마감재로, 환기와 조명을 동시에 고려한 구조. 베트남에서는 'tấm ốp trần lưới' 또는 'louver ceiling'으로 통용되며, 통역 시 재질(알루미늄, 스틸, 목재)과 간격(pitch), 색상을 명확히 전달해야 함. 한국에서는 주로 상업 공간에 사용되지만 베트남에서는 공장 및 산업시설에도 많이 적용됨.",
        "meaningVi": "Vật liệu hoàn thiện trần dạng lưới hoặc tấm, kết hợp giữa thông gió và chiếu sáng. Thường gọi là 'louver ceiling' hoặc 'tấm ốp trần lưới', cần làm rõ chất liệu (nhôm, thép, gỗ), khoảng cách (pitch) và màu sắc khi thông dịch.",
        "context": "상업시설, 사무실 천장, 공장",
        "culturalNote": "한국에서는 천장루버를 주로 디자인 요소로 사용하지만, 베트남에서는 열대기후 특성상 환기 기능을 더 중시함. 따라서 베트남 현장에서는 루버 간격과 통기성을 우선적으로 논의하는 경우가 많음. 또한 베트남에서는 백색 계열보다 목재 색상(vân gỗ)을 선호하는 경향이 있음.",
        "commonMistakes": [
            {
                "mistake": "'루버'를 'loa' (스피커)로 오인",
                "correction": "'louver' 또는 'lưới trần' 사용",
                "explanation": "발음이 유사하여 베트남인이 'loa'로 오해할 수 있으므로 영어 'louver' 병기 권장"
            },
            {
                "mistake": "'천장'을 'tầng' (층)으로 번역",
                "correction": "'trần' (천장) 사용",
                "explanation": "Tầng은 '층'을 의미하므로 천장을 뜻하는 'trần'과 명확히 구분"
            },
            {
                "mistake": "루버 간격을 'khoảng cách'로만 표현",
                "correction": "'pitch' 또는 'bước lưới' 사용",
                "explanation": "건축 용어로는 'pitch'가 정확하며, 베트남 현장에서도 영어 'pitch' 통용"
            }
        ],
        "examples": [
            {
                "ko": "천장루버는 100mm 간격으로 알루미늄 화이트로 시공합니다.",
                "vi": "Tấm ốp trần lưới được thi công bằng nhôm trắng với khoảng cách 100mm.",
                "situation": "formal"
            },
            {
                "ko": "루버 방향을 건물 길이 방향으로 맞춰주세요.",
                "vi": "Vui lòng điều chỉnh hướng lưới theo chiều dài tòa nhà.",
                "situation": "onsite"
            },
            {
                "ko": "이 공간은 목재 루버로 고급스럽게 마감할 예정입니다.",
                "vi": "Khu vực này sẽ được hoàn thiện cao cấp bằng lưới trần gỗ.",
                "situation": "formal"
            }
        ],
        "relatedTerms": ["천장재", "알루미늄 루버", "목재 루버", "환기 시스템", "천장 마감"]
    },
    {
        "slug": "tham-carpet",
        "korean": "카펫",
        "vietnamese": "Thảm (Carpet)",
        "hanja": None,
        "hanjaReading": None,
        "pronunciation": "카펫",
        "meaningKo": "바닥에 깔아 방음, 보온, 장식 등을 목적으로 사용하는 섬유 재질의 바닥재. 베트남에서는 'thảm' 또는 'carpet'으로 통용되며, 통역 시 카펫 타일(thảm tấm)과 롤 카펫(thảm cuộn)을 구분해야 함. 한국에서는 사무실에 카펫 타일을 많이 사용하지만, 베트남에서는 습도가 높아 관리가 어려워 고급 사무실 외에는 잘 사용하지 않음.",
        "meaningVi": "Vật liệu lót sàn làm từ sợi dệt, dùng để cách âm, giữ ấm và trang trí. Gọi là 'thảm' hoặc 'carpet', cần phân biệt giữa thảm tấm (carpet tile) và thảm cuộn (roll carpet). Tại Việt Nam, do độ ẩm cao nên ít sử dụng ngoài các văn phòng cao cấp.",
        "context": "사무실, 호텔, 고급 주거",
        "culturalNote": "한국에서는 카펫을 사무실 표준 바닥재로 많이 사용하지만, 베트남에서는 열대 기후로 인해 곰팡이와 습기 문제로 선호도가 낮음. 대신 고급 호텔이나 회의실 등 특정 공간에만 제한적으로 사용. 통역 시 관리 방법(청소, 방습)에 대한 질문이 많으므로 사전 숙지 필요.",
        "commonMistakes": [
            {
                "mistake": "'카펫'을 'chăn' (담요)로 번역",
                "correction": "'thảm' 사용",
                "explanation": "Chăn은 침구류를 뜻하므로 바닥재인 카펫과 완전히 다른 개념"
            },
            {
                "mistake": "'카펫 타일'을 'gạch thảm'로 번역",
                "correction": "'thảm tấm' 또는 'carpet tile' 사용",
                "explanation": "Gạch은 세라믹/석재 타일을 의미하므로 섬유 재질인 카펫 타일과 혼동"
            },
            {
                "mistake": "두께를 'dày'로만 표현",
                "correction": "'độ dày' + 단위(mm) 명시",
                "explanation": "'Dày'는 형용사이고, 수치 표현 시 'độ dày'(두께) 사용이 정확"
            }
        ],
        "examples": [
            {
                "ko": "사무실 바닥은 카펫 타일로 시공합니다.",
                "vi": "Sàn văn phòng được thi công bằng thảm tấm.",
                "situation": "formal"
            },
            {
                "ko": "이 카펫은 방염 인증을 받았나요?",
                "vi": "Thảm này có chứng nhận chống cháy không?",
                "situation": "formal"
            },
            {
                "ko": "회의실 카펫은 흡음성이 좋은 제품으로 선택했습니다.",
                "vi": "Thảm phòng họp được chọn loại có khả năng hấp thụ âm thanh tốt.",
                "situation": "formal"
            }
        ],
        "relatedTerms": ["바닥재", "카펫 타일", "롤 카펫", "방염 카펫", "타일 카펫"]
    },
    {
        "slug": "san-epoxy",
        "korean": "에폭시바닥",
        "vietnamese": "Sàn epoxy",
        "hanja": None,
        "hanjaReading": None,
        "pronunciation": "에폭시바닥",
        "meaningKo": "에폭시 수지를 이용해 마감한 바닥으로, 내구성과 내화학성이 뛰어나 공장, 주차장, 실험실 등에 사용. 베트nam에서는 'sàn epoxy'로 통용되며, 통역 시 두께(일반형 2~3mm, 자기수평형 5mm 이상)와 마감 타입(광택/무광)을 명확히 해야 함. 한국에서는 주로 산업 시설에 사용하지만, 베트남에서는 최근 상업 공간에도 디자인 요소로 많이 적용됨.",
        "meaningVi": "Sàn hoàn thiện bằng nhựa epoxy, có độ bền cao và khả năng chống hóa chất tốt, thường dùng trong nhà máy, bãi đỗ xe, phòng thí nghiệm. Tại Việt Nam gọi là 'sàn epoxy', cần làm rõ độ dày (thông thường 2-3mm, tự san phẳng từ 5mm) và kiểu hoàn thiện (bóng/mờ).",
        "context": "공장, 주차장, 실험실, 상업 공간",
        "culturalNote": "한국에서는 에폭시바닥을 주로 산업 용도로 보지만, 베트남에서는 카페, 쇼룸 등 상업 공간에 광택 있는 에폭시를 디자인 요소로 활용하는 추세. 따라서 베트남 클라이언트는 색상(màu sắc)과 광택도(độ bóng)에 대한 요구가 구체적임. 또한 베트남은 습도가 높아 시공 전 바닥 방습 처리가 필수.",
        "commonMistakes": [
            {
                "mistake": "'에폭시'를 'sơn' (페인트)로 번역",
                "correction": "'epoxy' 또는 'nhựa epoxy' 사용",
                "explanation": "Sơn은 일반 도료를 뜻하며, 에폭시는 수지 기반이므로 구분 필요"
            },
            {
                "mistake": "'자기수평 에폭시'를 직역",
                "correction": "'epoxy tự san phẳng' 사용",
                "explanation": "'Tự san phẳng'이 self-leveling의 정확한 베트남어 표현"
            },
            {
                "mistake": "시공 두께를 'chiều cao'로 표현",
                "correction": "'độ dày' 사용",
                "explanation": "Chiều cao는 '높이'이고, 바닥 두께는 'độ dày'"
            }
        ],
        "examples": [
            {
                "ko": "공장 바닥은 3mm 두께 에폭시로 시공합니다.",
                "vi": "Sàn nhà máy được thi công bằng epoxy dày 3mm.",
                "situation": "formal"
            },
            {
                "ko": "에폭시 색상은 그레이 계열로 선정했습니다.",
                "vi": "Màu sàn epoxy đã được chọn tông xám.",
                "situation": "formal"
            },
            {
                "ko": "에폭시 시공 전 바닥 수분 측정 좀 해주세요.",
                "vi": "Vui lòng kiểm tra độ ẩm sàn trước khi thi công epoxy.",
                "situation": "onsite"
            }
        ],
        "relatedTerms": ["바닥재", "자기수평 에폭시", "우레탄바닥", "공장 바닥", "주차장 바닥"]
    },
    {
        "slug": "san-urethane",
        "korean": "우레탄바닥",
        "vietnamese": "Sàn urethane",
        "hanja": None,
        "hanjaReading": None,
        "pronunciation": "우레탄바닥",
        "meaningKo": "우레탄 수지를 이용한 바닥 마감재로, 에폭시보다 탄성이 좋아 충격 흡수가 필요한 공간에 사용. 베트남에서는 'sàn urethane' 또는 'sàn PU' (폴리우레탄)로 통용되며, 통역 시 용도(스포츠 시설, 식품 공장 등)에 따라 두께와 탄성도를 명확히 해야 함. 한국에서는 체육관, 실내 운동 공간에 많이 사용되며, 베트남에서도 유사하게 적용.",
        "meaningVi": "Vật liệu hoàn thiện sàn bằng nhựa urethane (PU), có tính đàn hồi tốt hơn epoxy nên dùng cho không gian cần hấp thụ va đập. Tại Việt Nam gọi là 'sàn urethane' hoặc 'sàn PU', cần làm rõ mục đích sử dụng (sân thể thao, nhà máy thực phẩm) để xác định độ dày và độ đàn hồi.",
        "context": "체육관, 스포츠 시설, 식품 공장",
        "culturalNote": "한국과 베트남 모두 우레탄바닥을 실내 스포츠 시설과 식품 공장에 주로 사용. 다만 베트남에서는 열대 기후로 인해 내열성(khả năng chịu nhiệt)에 대한 요구가 높으며, 특히 식품 공장에서는 위생 인증(chứng nhận vệ sinh)을 요구하는 경우가 많음. 통역 시 관련 인증서 보유 여부를 확인해야 함.",
        "commonMistakes": [
            {
                "mistake": "'우레탄'을 'nhựa thường' (일반 플라스틱)으로 번역",
                "correction": "'urethane' 또는 'PU (polyurethane)' 사용",
                "explanation": "일반 플라스틱과 폴리우레탄은 성질이 다르므로 명확히 구분"
            },
            {
                "mistake": "'탄성'을 'mềm' (부드러움)으로만 표현",
                "correction": "'tính đàn hồi' 사용",
                "explanation": "Mềm은 단순히 '부드럽다'이고, 탄성은 'tính đàn hồi'가 정확"
            },
            {
                "mistake": "스포츠 시설 우레탄을 'sơn sàn'으로 번역",
                "correction": "'sàn urethane' 또는 'sàn thể thao' 사용",
                "explanation": "Sơn sàn은 단순 바닥 도료이고, 스포츠용 우레탄은 별도 시스템"
            }
        ],
        "examples": [
            {
                "ko": "체육관 바닥은 5mm 우레탄으로 시공합니다.",
                "vi": "Sàn nhà thi đấu được thi công bằng urethane dày 5mm.",
                "situation": "formal"
            },
            {
                "ko": "이 우레탄은 충격 흡수율이 몇 퍼센트인가요?",
                "vi": "Sàn urethane này có tỷ lệ hấp thụ va đập là bao nhiêu phần trăm?",
                "situation": "formal"
            },
            {
                "ko": "식품 공장용 우레탄은 위생 인증이 필요합니다.",
                "vi": "Sàn urethane cho nhà máy thực phẩm cần có chứng nhận vệ sinh.",
                "situation": "formal"
            }
        ],
        "relatedTerms": ["바닥재", "에폭시바닥", "스포츠 바닥", "탄성 바닥", "PU 바닥"]
    },
    {
        "slug": "gach-nhua-vinyl",
        "korean": "비닐타일",
        "vietnamese": "Gạch nhựa vinyl",
        "hanja": None,
        "hanjaReading": None,
        "pronunciation": "비닐타일",
        "meaningKo": "PVC 재질의 타일형 바닥재로, 시공이 간편하고 다양한 디자인이 있어 주거 및 상업 공간에 널리 사용. 베트남에서는 'gạch nhựa vinyl' 또는 'sàn nhựa'로 통용되며, 통역 시 접착 방식(풀칠형/접착형/클릭형)과 두께를 명확히 해야 함. 한국에서는 '장판'과 혼동되기도 하나, 베트남에서는 타일형(gạch)과 롤형(cuộn)을 엄격히 구분.",
        "meaningVi": "Vật liệu lót sàn dạng tấm làm từ PVC, dễ thi công và có nhiều mẫu mã, phổ biến trong nhà ở và không gian thương mại. Tại Việt Nam gọi là 'gạch nhựa vinyl' hoặc 'sàn nhựa', cần làm rõ phương thức lắp đặt (dán keo/tự dính/hèm khóa) và độ dày.",
        "context": "주거, 사무실, 상업 공간",
        "culturalNote": "한국에서는 비닐타일과 장판을 혼용하지만, 베트남에서는 'gạch nhựa'(타일형)와 'sàn nhựa cuộn'(롤형)을 명확히 구분하여 발주. 특히 베트남에서는 목재 무늬(vân gỗ) 비닐타일이 인기 있으며, 한국보다 저렴한 제품이 많아 가격 협상 시 품질 기준(wear layer 두께 등)을 명시해야 함.",
        "commonMistakes": [
            {
                "mistake": "'비닐타일'을 'gạch' (세라믹 타일)로만 번역",
                "correction": "'gạch nhựa vinyl' 사용",
                "explanation": "Gạch만 쓰면 세라믹/석재 타일로 오해되므로 'nhựa vinyl' 명시 필수"
            },
            {
                "mistake": "'장판'과 '비닐타일'을 같은 단어로 번역",
                "correction": "장판='sàn nhựa cuộn', 비닐타일='gạch nhựa vinyl'",
                "explanation": "형태와 시공법이 다르므로 엄격히 구분"
            },
            {
                "mistake": "두께를 'dày'로만 표현",
                "correction": "'độ dày' + wear layer 명시",
                "explanation": "비닐타일은 전체 두께와 wear layer 두께를 모두 명시해야 정확"
            }
        ],
        "examples": [
            {
                "ko": "거실 바닥은 3mm 두께 비닐타일로 시공합니다.",
                "vi": "Sàn phòng khách được thi công bằng gạch nhựa vinyl dày 3mm.",
                "situation": "formal"
            },
            {
                "ko": "이 비닐타일은 접착제가 필요한가요?",
                "vi": "Gạch nhựa vinyl này có cần keo dán không?",
                "situation": "onsite"
            },
            {
                "ko": "목재 무늬 비닐타일로 고급스럽게 연출했습니다.",
                "vi": "Đã sử dụng gạch nhựa vinyl vân gỗ để tạo vẻ cao cấp.",
                "situation": "formal"
            }
        ],
        "relatedTerms": ["바닥재", "장판", "PVC 타일", "목재 무늬 타일", "접착식 타일"]
    },
    {
        "slug": "vat-lieu-cach-am",
        "korean": "흡음재",
        "vietnamese": "Vật liệu cách âm",
        "hanja": "吸音材",
        "hanjaReading": "吸(빨아들일 흡) + 音(소리 음) + 材(재료 재)",
        "pronunciation": "흡음재",
        "meaningKo": "소리를 흡수하여 반향을 줄이는 재료로, 회의실, 스튜디오, 극장 등에 사용. 베트남에서는 'vật liệu cách âm' (차음재)과 'vật liệu hấp thụ âm' (흡음재)를 혼용하므로, 통역 시 용도를 명확히 해야 함. 한국에서는 '차음'과 '흡음'을 엄격히 구분하지만, 베트남 현장에서는 'cách âm'으로 통칭하는 경우가 많아 주의 필요.",
        "meaningVi": "Vật liệu hấp thụ âm thanh để giảm tiếng vang, dùng trong phòng họp, studio, rạp hát. Tại Việt Nam thường gọi chung là 'vật liệu cách âm' (cả cách âm và hấp thụ âm), khi thông dịch cần làm rõ mục đích sử dụng.",
        "context": "회의실, 스튜디오, 극장, 공장",
        "culturalNote": "한국에서는 '차음'(소리 차단)과 '흡음'(소리 흡수)을 기술적으로 구분하지만, 베트남 현장에서는 'cách âm'으로 통칭하는 경우가 많음. 특히 베트남에서는 소음 규제가 한국보다 느슨하여, 흡음재 적용이 필수가 아닌 선택 사항인 경우가 많음. 통역 시 흡음 성능(NRC 계수)을 수치로 제시하면 이해가 빠름.",
        "commonMistakes": [
            {
                "mistake": "'흡음'과 '차음'을 모두 'cách âm'으로 번역",
                "correction": "흡음='hấp thụ âm', 차음='cách âm'",
                "explanation": "흡음은 소리를 흡수, 차음은 소리를 차단하므로 개념이 다름"
            },
            {
                "mistake": "'흡음재'를 'xốp cách âm' (스펀지)로만 표현",
                "correction": "'vật liệu hấp thủ âm' 또는 구체적 재질 명시 (tấm gỗ, tấm bông khoáng)",
                "explanation": "흡음재는 스펀지 외에도 다양한 재질이 있으므로 재질 명시 필요"
            },
            {
                "mistake": "흡음 성능을 '좋다/나쁘다'로만 표현",
                "correction": "NRC (hệ số hấp thụ âm) 수치 명시",
                "explanation": "베트남 현장에서도 NRC 계수로 성능 평가하므로 수치 제시가 정확"
            }
        ],
        "examples": [
            {
                "ko": "회의실 벽면에 흡음재를 설치합니다.",
                "vi": "Thi công vật liệu hấp thụ âm trên tường phòng họp.",
                "situation": "formal"
            },
            {
                "ko": "이 흡음재의 NRC 계수는 0.8입니다.",
                "vi": "Vật liệu hấp thụ âm này có hệ số NRC là 0.8.",
                "situation": "formal"
            },
            {
                "ko": "천장에 흡음재 좀 더 추가해주세요.",
                "vi": "Vui lòng bổ sung thêm vật liệu hấp thụ âm ở trần.",
                "situation": "onsite"
            }
        ],
        "relatedTerms": ["차음재", "방음재", "음향 설계", "NRC 계수", "반향 제어"]
    },
    {
        "slug": "nep-trang-tri-molding",
        "korean": "몰딩",
        "vietnamese": "Nẹp trang trí (Molding)",
        "hanja": None,
        "hanjaReading": None,
        "pronunciation": "몰딩",
        "meaningKo": "벽과 천장, 바닥의 경계나 모서리를 마감하는 장식용 부자재. 베트남에서는 'nẹp trang trí' 또는 'molding'으로 통용되며, 통역 시 재질(목재, PU, 석고, 알루미늄)과 설치 위치(천장, 벽 하단, 모서리)를 명확히 해야 함. 한국에서는 주로 인테리어 마감재로 보지만, 베트남에서는 실용성(보호)과 장식성을 동시에 중시.",
        "meaningVi": "Phụ kiện trang trí dùng để hoàn thiện góc cạnh giữa tường và trần, tường và sàn. Tại Việt Nam gọi là 'nẹp trang trí' hoặc 'molding', cần làm rõ chất liệu (gỗ, PU, thạch cao, nhôm) và vị trí lắp đặt (trần, chân tường, góc).",
        "context": "실내 인테리어, 마감재",
        "culturalNote": "한국에서는 몰딩을 주로 고급 인테리어의 장식 요소로 보지만, 베트남에서는 실용성(벽 보호, 청소 편의)도 중시하여 일반 주거에서도 많이 사용. 특히 베트남에서는 PU 몰딩이 인기 있으며, 습기에 강하고 가격이 저렴하여 목재 몰딩보다 선호도가 높음. 통역 시 'nẹp chân tường'(걸레받이)와 'nẹp trần'(천장 몰딩)을 구분해야 함.",
        "commonMistakes": [
            {
                "mistake": "'몰딩'을 'khung' (액자)로 번역",
                "correction": "'nẹp trang trí' 또는 'molding' 사용",
                "explanation": "Khung은 액자나 프레임을 뜻하므로 건축 마감재인 몰딩과 다름"
            },
            {
                "mistake": "'걸레받이'와 '몰딩'을 같은 단어로 번역",
                "correction": "걸레받이='nẹp chân tường', 장식 몰딩='nẹp trang trí'",
                "explanation": "용도와 위치가 다르므로 구분 필요"
            },
            {
                "mistake": "재질 구분 없이 일괄 번역",
                "correction": "nẹp gỗ (목재), nẹp PU (폴리우레탄), nẹp thạch cao (석고) 등 재질 명시",
                "explanation": "재질에 따라 가격과 시공법이 다르므로 명확히 구분"
            }
        ],
        "examples": [
            {
                "ko": "천장 몰딩은 PU 재질로 화이트 컬러입니다.",
                "vi": "Nẹp trần làm bằng PU màu trắng.",
                "situation": "formal"
            },
            {
                "ko": "벽 하단에 걸레받이 몰딩 설치해주세요.",
                "vi": "Vui lòng lắp nẹp chân tường ở phía dưới tường.",
                "situation": "onsite"
            },
            {
                "ko": "이 공간은 석고 몰딩으로 고급스럽게 연출했습니다.",
                "vi": "Khu vực này được trang trí cao cấp bằng nẹp thạch cao.",
                "situation": "formal"
            }
        ],
        "relatedTerms": ["걸레받이", "천장 몰딩", "PU 몰딩", "석고 몰딩", "인테리어 마감"]
    },
    {
        "slug": "tu-am-tuong",
        "korean": "붙박이장",
        "vietnamese": "Tủ âm tường",
        "hanja": None,
        "hanjaReading": None,
        "pronunciation": "붙박이장",
        "meaningKo": "벽에 고정 설치하는 수납장으로, 이동이 불가능하고 공간 활용도가 높음. 베트남에서는 'tủ âm tường' 또는 'built-in closet'으로 통용되며, 통역 시 도어 타입(여닫이/미닫이/폴딩)과 내부 구성(선반, 행거, 서랍)을 명확히 해야 함. 한국에서는 주거 공간의 기본 가구로 보지만, 베트남에서는 맞춤 가구로 인식되어 별도 견적이 일반적.",
        "meaningVi": "Tủ cố định gắn vào tường, không thể di chuyển, tối ưu hóa không gian. Tại Việt Nam gọi là 'tủ âm tường' hoặc 'built-in closet', cần làm rõ loại cửa (mở/trượt/gấp) và cấu trúc bên trong (kệ, thanh treo, ngăn kéo).",
        "context": "주거, 침실, 드레스룸",
        "culturalNote": "한국에서는 아파트 기본 옵션으로 붙박이장이 제공되는 경우가 많지만, 베트남에서는 대부분 별도 시공이며 맞춤 제작(đóng theo yêu cầu)이 일반적. 특히 베트남에서는 습기 방지를 위해 통풍 기능(thông gió)을 요구하는 경우가 많으므로, 통역 시 내부 환기 시스템에 대한 질문이 나올 수 있음.",
        "commonMistakes": [
            {
                "mistake": "'붙박이장'을 'tủ quần áo' (일반 옷장)로 번역",
                "correction": "'tủ âm tường' 또는 'built-in closet' 사용",
                "explanation": "Tủ quần áo는 이동 가능한 일반 옷장이고, 붙박이장은 고정형"
            },
            {
                "mistake": "'미닫이 도어'를 'cửa trượt'로만 표현",
                "correction": "'cửa lùa' 또는 'cửa trượt' 사용 (둘 다 통용)",
                "explanation": "베트남에서는 'cửa lùa'와 'cửa trượt' 모두 사용되므로 혼동 방지 필요"
            },
            {
                "mistake": "내부 구성을 '선반/서랍'으로만 표현",
                "correction": "kệ (선반), ngăn kéo (서랍), thanh treo (행거) 등 구체적 명시",
                "explanation": "베트남 클라이언트는 내부 구성을 매우 세부적으로 요구하므로 정확한 용어 사용"
            }
        ],
        "examples": [
            {
                "ko": "침실에 3미터 폭 붙박이장을 설치합니다.",
                "vi": "Lắp đặt tủ âm tường rộng 3 mét trong phòng ngủ.",
                "situation": "formal"
            },
            {
                "ko": "붙박이장 도어는 미닫이로 해주세요.",
                "vi": "Vui lòng làm cửa tủ âm tường dạng trượt.",
                "situation": "onsite"
            },
            {
                "ko": "이 붙박이장은 내부에 LED 조명이 설치되어 있습니다.",
                "vi": "Tủ âm tường này được trang bị đèn LED bên trong.",
                "situation": "formal"
            }
        ],
        "relatedTerms": ["수납장", "드레스룸", "맞춤 가구", "미닫이장", "시스템 가구"]
    },
    {
        "slug": "thi-cong-noi-that",
        "korean": "가구공사",
        "vietnamese": "Thi công nội thất",
        "hanja": "家具工事",
        "hanjaReading": "家(집 가) + 具(갖출 구) + 工(장인 공) + 事(일 사)",
        "pronunciation": "가구공사",
        "meaningKo": "건축 공사 중 가구류 제작 및 설치를 포함한 공사로, 붙박이장, 주방가구, 신발장, 파티션 등을 현장 제작하거나 설치하는 작업. 베트남에서는 'thi công nội thất' 또는 'thi công đồ gỗ'로 통용되며, 통역 시 맞춤 제작(đóng mới)과 기성품 설치(lắp đặt sẵn)를 구분해야 함. 한국에서는 건축 공사의 세부 항목으로 보지만, 베트남에서는 별도 전문 업체가 담당하는 경우가 많음.",
        "meaningVi": "Hạng mục thi công bao gồm chế tạo và lắp đặt đồ nội thất như tủ âm tường, tủ bếp, tủ giày, vách ngăn trong công trình xây dựng. Tại Việt Nam gọi là 'thi công nội thất' hoặc 'thi công đồ gỗ', cần phân biệt giữa đóng mới (chế tạo theo yêu cầu) và lắp đặt sẵn (lắp đặt thành phẩm).",
        "context": "건축, 인테리어, 리모델링",
        "culturalNote": "한국에서는 가구공사를 건축 공사의 일부로 통합 발주하는 경우가 많지만, 베트남에서는 대부분 별도 계약(hợp đồng riêng)으로 진행. 특히 베트남에서는 맞춤 가구(đồ gỗ đóng theo yêu cầu)를 선호하며, 목재 종류(gỗ tự nhiên/gỗ công nghiệp)에 따라 가격 차이가 크므로 통역 시 재질 명시 필수.",
        "commonMistakes": [
            {
                "mistake": "'가구공사'를 'mua đồ nội thất' (가구 구매)로 번역",
                "correction": "'thi công nội thất' 또는 'thi công đồ gỗ' 사용",
                "explanation": "가구공사는 제작·설치를 포함한 공사이므로 단순 구매와 다름"
            },
            {
                "mistake": "'맞춤 제작'을 'tùy chỉnh'로 번역",
                "correction": "'đóng theo yêu cầu' 또는 'đóng mới' 사용",
                "explanation": "'Tùy chỉnh'는 IT 용어이고, 가구 맞춤 제작은 'đóng theo yêu cầu'"
            },
            {
                "mistake": "목재 종류를 '나무'로만 표현",
                "correction": "gỗ tự nhiên (원목), gỗ công nghiệp (합판/MDF) 등 구체적 명시",
                "explanation": "베트남에서는 목재 종류에 따라 가격이 크게 다르므로 정확한 구분 필요"
            }
        ],
        "examples": [
            {
                "ko": "가구공사는 원목으로 진행합니다.",
                "vi": "Thi công nội thất bằng gỗ tự nhiên.",
                "situation": "formal"
            },
            {
                "ko": "주방가구는 기성품 설치로 진행할까요?",
                "vi": "Tủ bếp có nên lắp đặt thành phẩm không?",
                "situation": "formal"
            },
            {
                "ko": "가구공사 견적서에 도장 포함되어 있나요?",
                "vi": "Báo giá thi công nội thất có bao gồm sơn không?",
                "situation": "formal"
            }
        ],
        "relatedTerms": ["목공사", "붙박이장", "주방가구", "맞춤 가구", "인테리어 공사"]
    }
]
filtered = [t for t in new_terms if t['slug'] not in existing_slugs]
data.extend(filtered)
with open(file_path, 'w', encoding='utf-8') as f:
    json.dump(data, f, ensure_ascii=False, indent=2)
print(f"Added {len(filtered)} terms. Total: {len(data)}")
