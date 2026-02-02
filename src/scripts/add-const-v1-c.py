import json
import os

file_path = os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', 'data', 'terms', 'construction.json')

with open(file_path, 'r', encoding='utf-8') as f:
    data = json.load(f)

existing_slugs = {t['slug'] for t in data}

new_terms = [
    {
        "slug": "giay-dan-tuong",
        "korean": "도배",
        "vietnamese": "Giấy dán tường",
        "hanja": "塗褙",
        "hanjaReading": "塗(칠할 도) + 褙(배접할 배)",
        "pronunciation": "도배",
        "meaningKo": "벽면에 종이나 벽지를 바르는 작업을 말합니다. 한국에서는 전통적으로 한지를 사용했으나 현대에는 합성수지 벽지, 실크 벽지 등 다양한 소재를 사용합니다. 통역 시 '도배'와 '벽지'를 혼동하지 않도록 주의해야 하며, '도배하다(작업)'와 '벽지(자재)'를 명확히 구분해야 합니다. 베트남에서는 페인트 마감이 일반적이므로 한국의 벽지 문화에 대한 설명이 필요할 수 있습니다. 현장에서는 '합지', '실크', '천연벽지' 등 종류별 구분이 중요하며, 시공 전 벽면 퍼티 작업 여부도 확인해야 합니다.",
        "meaningVi": "Công việc dán giấy hoặc giấy dán tường lên bề mặt tường. Ở Hàn Quốc truyền thống sử dụng giấy hanji, nhưng hiện đại có nhiều loại như giấy dán tường nhựa tổng hợp, giấy lụa. Cần phân biệt rõ 'công việc dán tường (도배하다)' và 'vật liệu giấy dán tường (벽지)'.",
        "context": "마감공사",
        "culturalNote": "한국은 벽지 문화가 발달하여 대부분의 주거 공간에 벽지를 사용하지만, 베트남은 페인트 마감이 주류입니다. 한국의 '도배 문화'는 습도 조절, 단열 효과, 교체 용이성 등의 이유로 선호되며, 베트남 현장에서는 이러한 장점을 설명할 필요가 있습니다. 또한 한국에서는 입주 전 새 벽지로 도배하는 것이 관례이나 베트남에서는 일반적이지 않습니다.",
        "commonMistakes": [
            {
                "mistake": "도배를 'painting walls'로 번역",
                "correction": "giấy dán tường (wallpapering)",
                "explanation": "도배는 페인트가 아니라 벽지를 바르는 작업이므로 painting과 혼동하면 안 됩니다"
            },
            {
                "mistake": "벽지와 도배를 같은 의미로 사용",
                "correction": "벽지=giấy dán tường(자재), 도배=công việc dán tường(작업)",
                "explanation": "자재와 작업을 구분해야 정확한 의사소통이 가능합니다"
            },
            {
                "mistake": "'합지', '실크' 등 종류를 설명 없이 사용",
                "correction": "giấy dán tường tổng hợp, giấy dán tường lụa 등으로 구체화",
                "explanation": "한국 특유의 벽지 분류는 베트남에서 생소하므로 자세한 설명이 필요합니다"
            }
        ],
        "examples": [
            {
                "ko": "이번 주말에 거실 도배 공사가 예정되어 있습니다.",
                "vi": "Cuối tuần này dự kiến thi công dán giấy dán tường phòng khách.",
                "situation": "formal"
            },
            {
                "ko": "도배 전에 벽면 퍼티 작업 먼저 해주세요.",
                "vi": "Trước khi dán tường, hãy trét bột trét tường trước.",
                "situation": "onsite"
            },
            {
                "ko": "실크 벽지로 도배하면 고급스러워 보여요.",
                "vi": "Nếu dán giấy dán tường lụa thì trông sang trọng hơn.",
                "situation": "informal"
            }
        ],
        "relatedTerms": ["벽지", "퍼티", "천장마감"]
    },
    {
        "slug": "vet-mach",
        "korean": "줄눈",
        "vietnamese": "Vết mạch",
        "hanja": None,
        "hanjaReading": None,
        "pronunciation": "줄눈",
        "meaningKo": "타일, 벽돌, 석재 등을 시공할 때 재료와 재료 사이에 생기는 틈을 말합니다. 이 틈을 채우는 작업을 '줄눈 시공' 또는 '줄눈 처리'라고 합니다. 통역 시 줄눈의 폭(예: 2mm, 5mm)과 재료(시멘트, 에폭시, 실리콘 등)를 명확히 구분해야 하며, 방수 줄눈인지 일반 줄눈인지도 중요한 정보입니다. 한국에서는 욕실, 주방 등 습한 공간의 줄눈 곰팡이 문제가 흔하므로 방수·방곰팡이 처리에 대한 논의가 자주 발생합니다. '줄눈 시공'과 '줄눈 청소'를 혼동하지 않도록 주의해야 합니다.",
        "meaningVi": "Khe hở giữa các viên gạch, gạch ốp, đá khi thi công. Công việc lấp đầy khe hở này gọi là 'thi công vết mạch' hoặc 'xử lý vết mạch'. Cần phân biệt rõ độ rộng vết mạch (2mm, 5mm) và vật liệu (xi măng, epoxy, silicone).",
        "context": "마감공사",
        "culturalNote": "한국에서는 욕실과 주방의 줄눈 곰팡이가 큰 문제로 인식되어 줄눈 청소 전문 서비스까지 존재합니다. 베트남에서는 상대적으로 덜 민감하게 인식되는 경향이 있습니다. 또한 한국은 좁은 줄눈(2mm 이하)을 선호하여 세련된 마감을 추구하지만, 베트남은 시공 편의를 위해 더 넓은 줄눈을 사용하는 경우가 많습니다. 계약 시 줄눈 폭과 재료 규격을 명확히 해야 분쟁을 예방할 수 있습니다.",
        "commonMistakes": [
            {
                "mistake": "줄눈을 'tile gap'이나 'space'로만 표현",
                "correction": "vết mạch (grout joint)",
                "explanation": "전문 용어를 사용해야 정확한 시공 의도를 전달할 수 있습니다"
            },
            {
                "mistake": "줄눈 시공과 줄눈 청소를 혼동",
                "correction": "시공=thi công vết mạch, 청소=vệ sinh vết mạch",
                "explanation": "작업 단계가 다르므로 명확히 구분해야 합니다"
            },
            {
                "mistake": "줄눈 폭 수치를 언급 없이 '좁게', '넓게'로만 표현",
                "correction": "구체적 mm 단위로 명시 (예: vết mạch 2mm)",
                "explanation": "주관적 표현은 오해를 낳으므로 정확한 수치를 사용해야 합니다"
            }
        ],
        "examples": [
            {
                "ko": "욕실 타일 줄눈은 방수 실리콘으로 처리해 주세요.",
                "vi": "Vết mạch gạch nhà tắm xử lý bằng silicone chống thấm.",
                "situation": "formal"
            },
            {
                "ko": "줄눈 폭은 2mm로 맞춰서 시공하겠습니다.",
                "vi": "Độ rộng vết mạch sẽ thi công theo chuẩn 2mm.",
                "situation": "onsite"
            },
            {
                "ko": "줄눈에 곰팡이가 생겨서 다시 해야 할 것 같아요.",
                "vi": "Vết mạch bị mốc rồi, có lẽ phải làm lại.",
                "situation": "informal"
            }
        ],
        "relatedTerms": ["타일", "실리콘", "코킹"]
    },
    {
        "slug": "silicone",
        "korean": "실리콘",
        "vietnamese": "Silicone",
        "hanja": None,
        "hanjaReading": None,
        "pronunciation": "실리콘",
        "meaningKo": "규소를 주성분으로 하는 합성수지로, 건설 현장에서는 방수·접착·충진 용도로 사용됩니다. 욕실, 주방, 창호 틈새 등에 시공하며, 용도에 따라 중성 실리콘(유리·금속용), 산성 실리콘(일반용), 곰팡이 방지 실리콘 등으로 구분됩니다. 통역 시 '실리콘'과 '코킹'을 혼용하는 경우가 많은데, 실리콘은 재료명이고 코킹은 틈새 충진 작업을 의미하므로 정확히 구분해야 합니다. 또한 '실리콘 건(gun)'은 시공 도구를 의미하며, 현장에서는 'silicone bắn' 등의 표현이 사용됩니다. 시공 후 경화 시간과 사용 가능 시점을 명확히 전달하는 것이 중요합니다.",
        "meaningVi": "Nhựa tổng hợp có thành phần chính là silicon, dùng cho mục đích chống thấm, dán kết, lấp khe trong công trường. Thi công ở nhà tắm, nhà bếp, khe cửa sổ. Có nhiều loại: silicone trung tính (cho kính, kim loại), silicone acid (dùng chung), silicone chống nấm mốc.",
        "context": "마감공사",
        "culturalNote": "한국에서는 실리콘 시공 품질을 매우 중요하게 여기며, 특히 욕실의 경우 곰팡이 방지 실리콘을 필수로 사용합니다. 베트남에서는 저가 실리콘 사용이 흔하여 내구성 문제가 발생하는 경우가 많습니다. 한국 건축주는 실리콘 브랜드(예: KCC, 다우코닝)를 지정하는 경우도 많으므로 계약 시 명확히 해야 합니다. 또한 한국은 실리콘 시공 후 매끄러운 마감을 중시하는 반면, 베트남은 기능성에 더 중점을 둡니다.",
        "commonMistakes": [
            {
                "mistake": "실리콘과 코킹을 같은 의미로 사용",
                "correction": "실리콘=silicone(재료), 코킹=bắn keo/làm keo(작업)",
                "explanation": "재료명과 작업명은 구분되어야 합니다"
            },
            {
                "mistake": "실리콘 종류를 구분하지 않고 통칭",
                "correction": "용도별로 중성/산성/방곰팡이 실리콘 명시",
                "explanation": "용도에 맞지 않는 실리콘 사용 시 하자 발생 가능성이 높습니다"
            },
            {
                "mistake": "'실리콘 건'을 'silicon gun'으로 번역",
                "correction": "súng bắn silicone",
                "explanation": "베트남 현장에서 통용되는 표현을 사용해야 합니다"
            }
        ],
        "examples": [
            {
                "ko": "욕실 코너 부분은 곰팡이 방지 실리콘으로 마감해 주세요.",
                "vi": "Góc nhà tắm hoàn thiện bằng silicone chống nấm mốc.",
                "situation": "formal"
            },
            {
                "ko": "실리콘 건으로 깔끔하게 시공해야 해요.",
                "vi": "Phải dùng súng bắn silicone thi công gọn gàng.",
                "situation": "onsite"
            },
            {
                "ko": "실리콘이 다 마르려면 24시간 걸려요.",
                "vi": "Silicone khô hẳn mất 24 giờ.",
                "situation": "informal"
            }
        ],
        "relatedTerms": ["코킹", "줄눈", "방수"]
    },
    {
        "slug": "lam-keo",
        "korean": "코킹",
        "vietnamese": "Làm keo",
        "hanja": None,
        "hanjaReading": None,
        "pronunciation": "코킹",
        "meaningKo": "건축물의 틈새나 접합부에 실런트(sealant)를 충진하여 방수, 기밀, 차음 등의 목적을 달성하는 작업입니다. 영어 'caulking'에서 유래했으며, 한국 현장에서는 주로 '코킹' 또는 '실링(sealing)' 작업으로 불립니다. 통역 시 코킹 재료(실리콘, 우레탄, 아크릴 등)와 코킹 작업을 구분해야 하며, 1차 코킹(구조 단계)과 2차 코킹(마감 단계)의 차이도 이해해야 합니다. 창호, 외벽, 욕실, 주방 등 위치에 따라 요구되는 코킹 재료와 기법이 다르므로 현장 상황을 정확히 파악해야 합니다.",
        "meaningVi": "Công việc lấp đầy khe hở hoặc mối nối của công trình bằng chất trám kín (sealant) để đạt mục đích chống thấm, kín khí, cách âm. Gốc từ tiếng Anh 'caulking', tại Hàn Quốc gọi là 'coking' hoặc 'sealing'. Cần phân biệt vật liệu làm keo (silicone, urethane, acrylic) và công việc làm keo.",
        "context": "마감공사",
        "culturalNote": "한국에서는 코킹 작업의 미관을 매우 중시하여 마감선이 일직선이고 매끄러워야 합니다. 베트남에서는 기능성(방수)에 더 집중하는 경향이 있어 마감 품질 기대치에 차이가 있을 수 있습니다. 또한 한국은 코킹 작업 후 즉시 마스킹 테이프를 제거하여 깔끔한 라인을 만드는 기법을 표준으로 하지만, 베트남에서는 이러한 세밀한 작업이 일반적이지 않습니다. 계약 시 마감 품질 기준을 구체적으로 명시하는 것이 분쟁 예방에 도움이 됩니다.",
        "commonMistakes": [
            {
                "mistake": "코킹을 단순히 'keo'(풀)로 번역",
                "correction": "làm keo chống thấm 또는 bắn keo trám",
                "explanation": "일반 접착제와 건축용 실런트는 다른 재료입니다"
            },
            {
                "mistake": "1차 코킹과 2차 코킹을 구분하지 않음",
                "correction": "làm keo lần 1 (cấu trúc), làm keo lần 2 (hoàn thiện)",
                "explanation": "시공 단계별로 목적과 재료가 다릅니다"
            },
            {
                "mistake": "코킹과 실리콘을 같은 것으로 혼동",
                "correction": "코킹=작업(làm keo), 실리콘=재료(silicone)",
                "explanation": "작업명과 재료명을 명확히 구분해야 합니다"
            }
        ],
        "examples": [
            {
                "ko": "창호 주변 코킹 작업은 내일 진행하겠습니다.",
                "vi": "Công việc làm keo xung quanh cửa sổ sẽ tiến hành ngày mai.",
                "situation": "formal"
            },
            {
                "ko": "코킹할 때 마스킹 테이프 꼭 붙이고 하세요.",
                "vi": "Khi làm keo nhớ dán băng keo che trước.",
                "situation": "onsite"
            },
            {
                "ko": "욕실 코킹이 벗겨져서 물이 새요.",
                "vi": "Keo nhà tắm bong ra nên bị dột nước.",
                "situation": "informal"
            }
        ],
        "relatedTerms": ["실리콘", "실런트", "방수"]
    },
    {
        "slug": "bot-tret-tuong",
        "korean": "퍼티",
        "vietnamese": "Bột trét tường",
        "hanja": None,
        "hanjaReading": None,
        "pronunciation": "퍼티",
        "meaningKo": "벽면이나 천장의 요철, 균열, 타정 자국 등을 메우고 평활하게 만드는 충진재입니다. 영어 'putty'에서 유래했으며, 도배나 페인트 작업 전 필수 선행 작업입니다. 통역 시 퍼티 작업 횟수(1회, 2회, 3회)에 따라 마감 품질과 비용이 달라지므로 명확히 전달해야 합니다. 한국에서는 석고 퍼티가 일반적이며, 실내용과 외부용이 구분됩니다. 퍼티 작업 후 샌딩(연마) 작업이 필수이며, 이를 '퍼티 갈기' 또는 '퍼티 샌딩'이라고 합니다. 베트남에서는 'bột trét tường' 외에 'trét tường' 등으로 표현됩니다.",
        "meaningVi": "Vật liệu lấp đầy để san phẳng các chỗ lồi lõm, vết nứt, lỗ đinh trên tường hoặc trần nhà. Gốc từ tiếng Anh 'putty', là công việc bắt buộc trước khi dán tường hoặc sơn. Số lần trét bột (1 lần, 2 lần, 3 lần) quyết định chất lượng hoàn thiện và chi phí.",
        "context": "마감공사",
        "culturalNote": "한국에서는 퍼티 작업을 매우 섬세하게 진행하여 2~3회 반복 시공과 샌딩을 표준으로 하지만, 베트남에서는 1회 시공으로 마무리하는 경우가 많아 마감 품질에 차이가 발생합니다. 한국 건축주는 평활도를 중시하므로 벽면에 손을 대어 확인하는 경우가 흔하며, 이러한 품질 기준을 사전에 합의하지 않으면 분쟁 소지가 있습니다. 또한 한국은 석고 퍼티를 선호하지만 베트남은 시멘트계 퍼티를 주로 사용하여 재료 선택에 대한 논의가 필요합니다.",
        "commonMistakes": [
            {
                "mistake": "퍼티를 'cement'로 번역",
                "correction": "bột trét tường (putty)",
                "explanation": "시멘트와 퍼티는 용도와 성분이 다른 재료입니다"
            },
            {
                "mistake": "퍼티 작업 횟수를 명시하지 않음",
                "correction": "trét bột 1 lần/2 lần/3 lần",
                "explanation": "시공 횟수가 품질과 비용에 직접적인 영향을 미칩니다"
            },
            {
                "mistake": "'퍼티 갈기'를 설명 없이 사용",
                "correction": "chà nhám bột trét (sanding putty)",
                "explanation": "샌딩 작업은 베트남에서 생소할 수 있으므로 설명이 필요합니다"
            }
        ],
        "examples": [
            {
                "ko": "벽면 퍼티 2회 시공 후 샌딩 작업을 진행합니다.",
                "vi": "Sau khi trét bột tường 2 lần, tiến hành chà nhám.",
                "situation": "formal"
            },
            {
                "ko": "퍼티 작업 끝나면 하루 말려야 해요.",
                "vi": "Sau khi trét bột xong phải phơi khô một ngày.",
                "situation": "onsite"
            },
            {
                "ko": "퍼티 한 번만 해도 될까요?",
                "vi": "Trét bột một lần thôi có được không?",
                "situation": "informal"
            }
        ],
        "relatedTerms": ["도배", "샌딩", "석고보드"]
    },
    {
        "slug": "op-tuong",
        "korean": "몰딩",
        "vietnamese": "Ốp tường",
        "hanja": None,
        "hanjaReading": None,
        "pronunciation": "몰딩",
        "meaningKo": "벽면과 천장, 벽면과 바닥의 경계부, 문틀 주변 등에 장식과 마감을 위해 설치하는 부재를 말합니다. 영어 'molding'에서 유래했으며, 용도에 따라 천장 몰딩(crown molding), 걸레받이 몰딩(baseboard), 문틀 몰딩(casing) 등으로 구분됩니다. 통역 시 몰딩의 위치와 재질(우드, PVC, 석고, 우레탄 등)을 명확히 해야 하며, 한국에서는 주로 인테리어 미관 목적으로 사용되지만 틈새 마감 기능도 겸합니다. 유럽풍 클래식 인테리어에서 필수 요소로 여겨지며, 최근에는 간접조명을 위한 몰딩 시공도 증가하고 있습니다.",
        "meaningVi": "Cấu kiện lắp đặt ở ranh giới tường-trần, tường-sàn, xung quanh khung cửa để trang trí và hoàn thiện. Gốc từ tiếng Anh 'molding', phân loại theo mục đích: ốp trần (crown molding), ốp chân tường (baseboard), ốp khung cửa (casing). Cần nói rõ vị trí và chất liệu (gỗ, PVC, thạch cao, urethane).",
        "context": "마감공사",
        "culturalNote": "한국에서는 몰딩을 고급 인테리어의 상징으로 여기며, 특히 아파트 리모델링 시 천장 몰딩과 간접조명 결합을 선호합니다. 베트남에서는 몰딩 문화가 덜 발달하여 필요성에 대한 인식이 낮을 수 있으며, 시공 기술자도 부족한 편입니다. 한국 건축주가 몰딩을 요구할 경우, 베트남 현장에서는 숙련된 목수나 마감공을 별도로 섭외해야 할 수 있습니다. 또한 한국은 몰딩의 디테일(곡선, 패턴)을 중시하지만 베트남은 단순한 직선 형태를 선호합니다.",
        "commonMistakes": [
            {
                "mistake": "몰딩을 'decoration'으로만 번역",
                "correction": "ốp tường trang trí (molding)",
                "explanation": "장식이지만 구조적 마감 기능도 있으므로 전문 용어를 사용해야 합니다"
            },
            {
                "mistake": "몰딩 종류를 구분하지 않고 통칭",
                "correction": "천장 몰딩=ốp trần, 걸레받이=ốp chân tường",
                "explanation": "위치별로 시공 방법과 재료가 다릅니다"
            },
            {
                "mistake": "'간접조명 몰딩'을 설명 없이 사용",
                "correction": "ốp trần có rãnh đèn gián tiếp",
                "explanation": "한국 특유의 인테리어 기법이므로 상세 설명이 필요합니다"
            }
        ],
        "examples": [
            {
                "ko": "거실 천장에 간접조명용 몰딩을 설치해 주세요.",
                "vi": "Lắp ốp trần có rãnh đèn gián tiếp ở trần phòng khách.",
                "situation": "formal"
            },
            {
                "ko": "이 몰딩은 PVC라서 습기에 강해요.",
                "vi": "Ốp tường này bằng PVC nên chống ẩm tốt.",
                "situation": "onsite"
            },
            {
                "ko": "몰딩 색상이 벽지랑 안 맞는 것 같아요.",
                "vi": "Màu ốp tường hình như không hợp với giấy dán tường.",
                "situation": "informal"
            }
        ],
        "relatedTerms": ["걸레받이", "천장마감", "인테리어"]
    },
    {
        "slug": "op-chan-tuong",
        "korean": "걸레받이",
        "vietnamese": "Ốp chân tường",
        "hanja": None,
        "hanjaReading": None,
        "pronunciation": "걸레받이",
        "meaningKo": "벽면 하단부와 바닥이 만나는 경계에 설치하는 마감재로, 청소 시 걸레질로부터 벽면을 보호하는 역할을 합니다. 영어로는 'baseboard' 또는 'skirting board'라고 하며, 높이는 보통 5~15cm입니다. 통역 시 걸레받이의 높이, 재질(원목, MDF, PVC, 타일 등), 설치 방법(접착제, 못, 앵커)을 명확히 전달해야 합니다. 한국에서는 바닥재 시공 후 마지막 단계로 걸레받이를 설치하며, 바닥재와 같은 재질로 통일하는 것이 일반적입니다. 최근에는 디자인 측면에서 걸레받이를 생략하거나 벽면에 홈을 파는 '걸레받이 없는 시공'도 증가하고 있습니다.",
        "meaningVi": "Vật liệu hoàn thiện lắp đặt ở ranh giới giữa chân tường và sàn nhà, có vai trò bảo vệ tường khi lau dọn. Tiếng Anh là 'baseboard' hoặc 'skirting board', chiều cao thường 5~15cm. Cần nói rõ chiều cao, chất liệu (gỗ tự nhiên, MDF, PVC, gạch) và phương pháp lắp đặt (keo dán, đinh, neo).",
        "context": "마감공사",
        "culturalNote": "한국에서는 걸레받이를 필수 마감재로 인식하며, 바닥과 일체감 있는 디자인을 중시합니다. 베트남에서도 걸레받이를 사용하지만 높이가 더 높고(10~15cm) 타일 재질을 선호하는 경향이 있어 미관상 차이가 있습니다. 한국은 얇고 낮은 걸레받이(5~7cm)로 현대적 감각을 추구하지만, 베트남은 실용성과 내구성을 우선시합니다. 또한 한국의 '걸레받이 없는 시공'은 베트남에서 생소한 개념이므로 도입 시 상세한 설명이 필요합니다.",
        "commonMistakes": [
            {
                "mistake": "걸레받이를 'wall guard'로 번역",
                "correction": "ốp chân tường (baseboard/skirting)",
                "explanation": "전문 건축 용어를 사용해야 정확합니다"
            },
            {
                "mistake": "걸레받이 높이를 명시하지 않음",
                "correction": "ốp chân tường cao 7cm",
                "explanation": "높이에 따라 시공 방법과 비용이 달라집니다"
            },
            {
                "mistake": "'걸레받이 없는 시공'을 설명 없이 사용",
                "correction": "thi công không có ốp chân tường (rãnh âm tường)",
                "explanation": "한국의 최신 시공 기법이므로 추가 설명이 필요합니다"
            }
        ],
        "examples": [
            {
                "ko": "바닥재와 같은 색상의 걸레받이로 시공해 주세요.",
                "vi": "Thi công ốp chân tường cùng màu với sàn.",
                "situation": "formal"
            },
            {
                "ko": "걸레받이는 접착제로 붙이면 돼요.",
                "vi": "Ốp chân tường dán bằng keo là được.",
                "situation": "onsite"
            },
            {
                "ko": "걸레받이가 벗겨져서 다시 붙여야겠어요.",
                "vi": "Ốp chân tường bong ra rồi phải dán lại.",
                "situation": "informal"
            }
        ],
        "relatedTerms": ["몰딩", "바닥재", "마감"]
    },
    {
        "slug": "hoan-thien-tran",
        "korean": "천장마감",
        "vietnamese": "Hoàn thiện trần",
        "hanja": "天障",
        "hanjaReading": "天(하늘 천) + 障(막을 장)",
        "meaningKo": "실내 천장면의 마감 작업을 총칭하는 용어로, 석고보드, 천장 텍스, 시스템 천장, 몰딩, 도장 등 다양한 공법이 있습니다. 통역 시 천장 마감재의 종류(석고보드, 칼라강판, 우드, 텍스, 시스템 천장 등)와 마감 방법(도장, 도배, 노출 등)을 명확히 구분해야 합니다. 한국에서는 평천장(flat ceiling)이 일반적이지만, 간접조명을 위한 단차 천장이나 디자인 천장도 많이 시공됩니다. 천장 높이(층고)와 마감 후 실제 사용 가능한 높이를 정확히 전달하는 것이 중요하며, 소음, 단열, 방화 등의 기능도 고려해야 합니다.",
        "meaningVi": "Thuật ngữ chỉ công việc hoàn thiện mặt trần trong nhà, có nhiều công pháp như tấm thạch cao, sơn trần, trần hệ thống, ốp trần, sơn. Cần phân biệt rõ loại vật liệu hoàn thiện trần (tấm thạch cao, tôn màu, gỗ, sơn, trần hệ thống) và phương pháp hoàn thiện (sơn, dán, để lộ).",
        "context": "마감공사",
        "culturalNote": "한국에서는 천장 마감을 중시하여 평활하고 깨끗한 마감을 표준으로 하며, 간접조명 설치를 위한 단차 천장이 매우 보편화되어 있습니다. 베트남에서는 천장 마감이 상대적으로 단순하며, 고급 건물이 아니면 간접조명 천장이 흔하지 않습니다. 한국의 아파트는 대부분 석고보드 위에 도배 또는 도장으로 마감하지만, 베트Nam은 노출 콘크리트에 페인트만 하는 경우도 많습니다. 천장 높이에 대한 기대치도 달라서, 한국은 2.3m 이상을 선호하지만 베트남은 2.7m 이상이 일반적입니다.",
        "commonMistakes": [
            {
                "mistake": "천장마감을 'ceiling'으로만 번역",
                "correction": "hoàn thiện trần (ceiling finishing)",
                "explanation": "구조물(trần)과 마감 작업(hoàn thiện trần)을 구분해야 합니다"
            },
            {
                "mistake": "'단차 천장'을 설명 없이 사용",
                "correction": "trần nhiều cấp độ (stepped ceiling)",
                "explanation": "한국 특유의 천장 디자인이므로 추가 설명이 필요합니다"
            },
            {
                "mistake": "천장 높이와 층고를 혼동",
                "correction": "층고=chiều cao tầng, 천장 높이=chiều cao trần hoàn thiện",
                "explanation": "구조 높이와 마감 후 높이는 다릅니다"
            }
        ],
        "examples": [
            {
                "ko": "거실 천장은 간접조명을 위한 단차 천장으로 시공합니다.",
                "vi": "Trần phòng khách thi công trần nhiều cấp độ cho đèn gián tiếp.",
                "situation": "formal"
            },
            {
                "ko": "천장 석고보드 작업 끝나면 퍼티 치고 도장하면 돼요.",
                "vi": "Sau khi xong tấm thạch cao trần, trét bột rồi sơn là được.",
                "situation": "onsite"
            },
            {
                "ko": "천장이 너무 낮아서 답답해 보여요.",
                "vi": "Trần quá thấp nên trông bí bách.",
                "situation": "informal"
            }
        ],
        "relatedTerms": ["석고보드", "몰딩", "간접조명"]
    },
    {
        "slug": "vat-lieu-san",
        "korean": "바닥재",
        "vietnamese": "Vật liệu sàn",
        "hanja": None,
        "hanjaReading": None,
        "pronunciation": "바닥재",
        "meaningKo": "건축물 바닥면에 시공되는 마감재를 총칭하는 용어로, 종류가 매우 다양합니다. 주거용은 마루(원목, 강화마루, PVC 마루), 타일, 장판 등이 일반적이며, 상업용은 에폭시, 카펫, 데코타일 등을 사용합니다. 통역 시 바닥재의 종류, 두께, 시공 방법(접착제, 못, 클릭, 자가접착 등), 내구성 등을 명확히 전달해야 합니다. 한국에서는 강화마루가 가장 보편적이며, 바닥 난방(온돌) 시스템에 적합한 제품을 선택합니다. 베트남은 타일 바닥이 주류이므로 한국식 마루 바닥 문화에 대한 설명이 필요할 수 있습니다.",
        "meaningVi": "Thuật ngữ chỉ vật liệu hoàn thiện được thi công trên mặt sàn của công trình, có rất nhiều loại. Dùng cho nhà ở có sàn gỗ (gỗ tự nhiên, sàn gỗ tổng hợp, sàn PVC), gạch, lát vinyl. Thương mại dùng epoxy, thảm, gạch trang trí. Cần nói rõ loại, độ dày, phương pháp thi công (keo dán, đinh, click, tự dính) và độ bền.",
        "context": "마감공사",
        "culturalNote": "한국에서는 온돌(바닥난방) 문화로 인해 난방에 강한 강화마루를 선호하며, 보행감(폭신함)과 소음 저감을 중시합니다. 베트남은 타일 바닥이 일반적이며, 열대 기후 특성상 시원한 촉감과 청소 편의성을 우선시합니다. 한국 건축주가 베트남 현장에서 마루 시공을 요구할 경우, 습도 관리와 시공 기술자 숙련도가 중요한 이슈가 됩니다. 또한 한국은 바닥재 두께(8mm, 11mm)에 민감하지만 베트남은 상대적으로 덜 중요시합니다.",
        "commonMistakes": [
            {
                "mistake": "바닥재를 'floor'로만 번역",
                "correction": "vật liệu sàn (flooring material)",
                "explanation": "구조물(sàn)과 마감재(vật liệu sàn)를 구분해야 합니다"
            },
            {
                "mistake": "마루 종류를 구분하지 않고 통칭",
                "correction": "원목=gỗ tự nhiên, 강화마루=sàn gỗ công nghiệp",
                "explanation": "재질과 가격이 크게 다르므로 명확히 구분해야 합니다"
            },
            {
                "mistake": "'온돌용 바닥재'를 설명 없이 사용",
                "correction": "vật liệu sàn chịu nhiệt (for floor heating)",
                "explanation": "베트남에는 바닥난방 문화가 없으므로 설명이 필요합니다"
            }
        ],
        "examples": [
            {
                "ko": "거실과 방은 강화마루로, 욕실과 주방은 타일로 시공합니다.",
                "vi": "Phòng khách và phòng ngủ thi công sàn gỗ công nghiệp, nhà tắm và bếp dùng gạch.",
                "situation": "formal"
            },
            {
                "ko": "이 바닥재는 온돌용이라 열에 강해요.",
                "vi": "Vật liệu sàn này dùng cho sưởi sàn nên chịu nhiệt tốt.",
                "situation": "onsite"
            },
            {
                "ko": "바닥재 색상이 너무 어두운 것 같아요.",
                "vi": "Màu vật liệu sàn hình như quá tối.",
                "situation": "informal"
            }
        ],
        "relatedTerms": ["강화마루", "타일", "걸레받이"]
    },
    {
        "slug": "gach-trang-tri",
        "korean": "데코타일",
        "vietnamese": "Gạch trang trí",
        "hanja": None,
        "hanjaReading": None,
        "pronunciation": "데코타일",
        "meaningKo": "장식 목적으로 사용되는 타일로, 일반 바닥·벽 타일과 달리 디자인과 패턴이 강조된 제품입니다. '데코레이션(decoration) + 타일(tile)'의 합성어이며, 주로 포인트 벽, 주방 백스플래시, 욕실 악센트 등에 사용됩니다. 통역 시 데코타일과 일반 타일을 구분하고, 패턴 타일, 모자이크 타일, 아트 타일 등 세부 종류도 이해해야 합니다. 한국에서는 최근 셀프 인테리어 트렌드로 접착식 데코타일(스티커 타일)이 인기를 얻고 있으며, 이는 시공이 간편하지만 내구성은 일반 타일보다 낮습니다. 계약 시 데코타일의 용도(장식/실사용)와 시공 방법을 명확히 해야 합니다.",
        "meaningVi": "Gạch dùng cho mục đích trang trí, khác với gạch sàn-tường thông thường vì nhấn mạnh thiết kế và hoa văn. Là từ ghép của 'decoration + tile', chủ yếu dùng cho tường điểm nhấn, tường bếp backsplash, điểm nhấn nhà tắm. Cần phân biệt gạch trang trí và gạch thông thường, hiểu cả các loại chi tiết như gạch hoa văn, gạch mosaic, gạch nghệ thuật.",
        "context": "마감공사",
        "culturalNote": "한국에서는 데코타일을 인테리어 포인트로 중시하며, SNS에 공유할 만한 '인스타그래머블'한 공간 연출을 위해 적극 활용합니다. 베트남에서는 장식용 타일보다 실용적 타일을 선호하는 경향이 있어, 데코타일에 추가 비용을 지불하는 것에 거부감이 있을 수 있습니다. 한국의 접착식 데코타일은 베트남에서 생소한 제품이므로 내구성과 방수 기능에 대한 명확한 설명이 필요합니다. 또한 한국은 작은 면적에도 포인트 타일을 사용하지만, 베트남은 넓은 면적에 적용하는 경향이 있습니다.",
        "commonMistakes": [
            {
                "mistake": "데코타일을 단순히 'tile'로 번역",
                "correction": "gạch trang trí (decorative tile)",
                "explanation": "장식 목적을 명확히 해야 일반 타일과 구분됩니다"
            },
            {
                "mistake": "'스티커 타일'을 설명 없이 사용",
                "correction": "gạch dán tự dính (peel-and-stick tile)",
                "explanation": "한국의 셀프 인테리어 제품이므로 추가 설명이 필요합니다"
            },
            {
                "mistake": "데코타일 용도를 명시하지 않음",
                "correction": "장식용인지 실사용 가능한지 명확히 (trang trí/sử dụng thực tế)",
                "explanation": "용도에 따라 요구되는 내구성이 다릅니다"
            }
        ],
        "examples": [
            {
                "ko": "주방 싱크대 뒤쪽 벽에 데코타일을 붙이겠습니다.",
                "vi": "Sẽ dán gạch trang trí ở tường phía sau bồn rửa bếp.",
                "situation": "formal"
            },
            {
                "ko": "이 데코타일은 접착식이라 시공이 쉬워요.",
                "vi": "Gạch trang trí này dạng tự dính nên thi công dễ.",
                "situation": "onsite"
            },
            {
                "ko": "데코타일 패턴이 너무 화려한 것 같아요.",
                "vi": "Hoa văn gạch trang trí hình như quá rực rỡ.",
                "situation": "informal"
            }
        ],
        "relatedTerms": ["타일", "백스플래시", "포인트월"]
    }
]

filtered = [t for t in new_terms if t['slug'] not in existing_slugs]
data.extend(filtered)

with open(file_path, 'w', encoding='utf-8') as f:
    json.dump(data, f, ensure_ascii=False, indent=2)

print(f"Added {len(filtered)} terms. Total: {len(data)}")
