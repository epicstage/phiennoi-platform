import json
import os

file_path = os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', 'data', 'terms', 'construction.json')

with open(file_path, 'r', encoding='utf-8') as f:
    data = json.load(f)

existing_slugs = {t['slug'] for t in data}

new_terms = [
    {
        "slug": "tuong-rem-kinh",
        "korean": "커튼월",
        "vietnamese": "Tường rèm kính",
        "hanja": "Curtain Wall",
        "hanjaReading": None,
        "pronunciation": "커튼월",
        "difficulty": "intermediate",
        "category": "materials",
        "subcategory": "windows-glass",
        "meaningKo": "건물 외벽을 비내력 유리와 알루미늄 프레임으로 구성한 외장 시스템입니다. 통역 시 주의할 점은 '유리벽'이 아닌 '커튼월'로 불러야 하며, 베트남에서는 고층 빌딩에 주로 사용되지만 시공 기술 차이로 누수 문제가 자주 발생합니다. 한국은 이중 실란트 시스템이 표준이지만 베트남은 단일 실란트를 사용하는 경우가 많아 품질 기준 설명이 중요합니다. '비내력벽'이라는 구조적 특성을 반드시 강조해야 합니다.",
        "meaningVi": "Hệ thống ốp ngoài tòa nhà được cấu tạo bằng khung nhôm và kính không chịu lực. Tường rèm kính thường được sử dụng cho các tòa nhà cao tầng hiện đại, tạo vẻ đẹp thẩm mỹ và cho phép ánh sáng tự nhiên. Khác với tường gạch, tường rèm không có chức năng chịu lực mà chỉ bảo vệ khỏi thời tiết.",
        "context": "외벽 시공, 건축 설계 회의, 고층 건물 공사",
        "culturalNote": "한국에서는 초고층 건물의 표준 외장재로 인식되며 에너지 효율 기준이 엄격합니다. 베트남은 열대기후 특성상 태양열 차단 성능(Low-E 코팅)이 더욱 중요하며, 태풍 대비 풍압 설계 기준이 다릅니다. 한국 시공사들이 베트남 프로젝트에서 현지 기후 조건을 간과하여 결로 문제가 발생하는 경우가 많습니다.",
        "commonMistakes": [
            {
                "mistake": "유리벽",
                "correction": "커튼월",
                "explanation": "기술 용어로는 '커튼월'이 정확하며, '유리벽'은 일반인 표현입니다"
            },
            {
                "mistake": "내력벽",
                "correction": "비내력 외장재",
                "explanation": "커튼월은 하중을 지지하지 않는 비내력 시스템입니다"
            },
            {
                "mistake": "Tường kính đơn thuần",
                "correction": "Hệ thống tường rèm kính",
                "explanation": "단순 유리벽이 아닌 프레임 시스템을 포함한 전체 구조를 의미합니다"
            }
        ],
        "examples": [
            {
                "ko": "이 프로젝트는 유닛 커튼월 방식으로 시공됩니다",
                "vi": "Dự án này sẽ thi công theo phương pháp tường rèm kính đơn nguyên",
                "situation": "formal"
            },
            {
                "ko": "커튼월 누수 테스트 일정 잡아주세요",
                "vi": "Hãy lên lịch kiểm tra chống thấm tường rèm kính",
                "situation": "onsite"
            },
            {
                "ko": "스팬드럴 부위 단열 보강이 필요합니다",
                "vi": "Cần tăng cường cách nhiệt ở vị trí spandrel",
                "situation": "formal"
            }
        ],
        "relatedTerms": ["알루미늄창호", "복층유리", "실란트", "열관류율"]
    },
    {
        "slug": "kinh-hai-lop",
        "korean": "복층유리",
        "vietnamese": "Kính hai lớp",
        "hanja": "複層유리",
        "hanjaReading": "복(겹 복) + 층(층 층)",
        "pronunciation": "복층유리",
        "difficulty": "basic",
        "category": "materials",
        "subcategory": "windows-glass",
        "meaningKo": "두 장의 유리 사이에 공기층이나 가스층을 두어 단열 및 차음 성능을 높인 유리입니다. 통역 시 주의할 점은 '이중유리'라는 일반 표현보다 '복층유리'가 기술 용어로 정확하며, 베트남에서는 'kính hộp'이라고도 부르지만 공식 명칭은 'kính hai lớp'입니다. 한국은 로이(Low-E) 코팅과 아르곤 가스 충진이 표준이지만 베트남은 비용 절감을 위해 일반 공기층만 사용하는 경우가 많아 단열 성능 차이를 설명해야 합니다.",
        "meaningVi": "Loại kính gồm hai lớp kính được ngăn cách bởi lớp không khí hoặc khí trơ (argon), giúp cách nhiệt và cách âm tốt hơn kính đơn. Kính hai lớp được sử dụng rộng rãi trong các công trình hiện đại để tiết kiệm năng lượng điều hòa.",
        "context": "창호 사양 결정, 에너지 절약 설계, 소음 차단",
        "culturalNote": "한국에서는 건축법상 일정 규모 이상 건물에 복층유리 사용이 의무화되어 있으며, 에너지 효율 등급 표시가 엄격합니다. 베트남은 열대기후로 인해 차음보다 단열(냉방 효율)이 더 중요하며, 고급 건물에서만 복층유리를 사용하는 경향이 있습니다. 습도가 높아 복층유리 내부 결로 문제가 자주 발생하므로 엣지 실링 품질이 중요합니다.",
        "commonMistakes": [
            {
                "mistake": "이중유리",
                "correction": "복층유리",
                "explanation": "일반인 표현은 '이중유리'지만 기술 용어는 '복층유리'입니다"
            },
            {
                "mistake": "Kính cường lực",
                "correction": "Kính hai lớp",
                "explanation": "강화유리(kính cường lực)와 복층유리는 다른 개념입니다"
            },
            {
                "mistake": "공기층 두께는 상관없다",
                "correction": "공기층 두께는 단열 성능에 직결됩니다",
                "explanation": "일반적으로 12mm가 최적이며, 너무 얇거나 두꺼우면 성능이 떨어집니다"
            }
        ],
        "examples": [
            {
                "ko": "12mm 로이복층유리로 사양 변경합니다",
                "vi": "Thay đổi quy cách sang kính hai lớp Low-E 12mm",
                "situation": "formal"
            },
            {
                "ko": "복층유리 내부에 습기 찼어요",
                "vi": "Có hơi nước bên trong kính hai lớp",
                "situation": "onsite"
            },
            {
                "ko": "아르곤 가스 충진 복층유리로 단열 성능을 높였습니다",
                "vi": "Đã nâng cao hiệu quả cách nhiệt bằng kính hai lớp bơm khí argon",
                "situation": "formal"
            }
        ],
        "relatedTerms": ["로이유리", "열관류율", "아르곤가스", "실란트"]
    },
    {
        "slug": "kinh-low-e",
        "korean": "로이유리",
        "vietnamese": "Kính Low-E",
        "hanja": None,
        "hanjaReading": None,
        "pronunciation": "로이유리",
        "difficulty": "intermediate",
        "category": "materials",
        "subcategory": "windows-glass",
        "meaningKo": "Low Emissivity의 약자로, 유리 표면에 특수 금속 산화물을 코팅하여 열 방사율을 낮춘 고단열 유리입니다. 통역 시 주의할 점은 베트남어로 그대로 'Low-E'라고 부르며 별도 번역어가 없다는 것입니다. 한국은 겨울 난방열 보존이 중요하지만 베트남은 여름 태양열 차단이 주목적이므로 코팅 위치(#2면 vs #3면)가 반대입니다. '저방사'라는 기술 용어보다 '단열 코팅 유리'로 설명하면 이해가 빠릅니다.",
        "meaningVi": "Kính được phủ lớp oxit kim loại mỏng đặc biệt để giảm tỉ lệ phát xạ nhiệt, giúp chặn bức xạ nhiệt từ mặt trời vào mùa hè và giữ nhiệt vào mùa đông. Kính Low-E là lựa chọn hàng đầu cho các công trình tiết kiệm năng lượng ở vùng khí hậu nóng.",
        "context": "에너지 절약 설계, 친환경 건축, 유리 사양 결정",
        "culturalNote": "한국에서는 난방비 절감을 위해 난방용 로이유리(Heat Mirror)가 주로 사용되지만, 베트남은 냉방비 절감을 위해 태양열 차단형(Solar Control)이 필수입니다. 한국 시공사들이 한국 사양을 그대로 적용하여 베트남에서 냉방 효율이 떨어지는 실수를 자주 합니다. 베트남은 투과율이 낮은 반사형을 선호하지만 한국은 채광을 중시하여 투과율이 높은 제품을 선호합니다.",
        "commonMistakes": [
            {
                "mistake": "저방사유리",
                "correction": "로이유리 또는 Low-E 유리",
                "explanation": "현장에서는 '로이유리'가 통용되며, '저방사'는 기술 문서에서만 사용합니다"
            },
            {
                "mistake": "Kính phản quang",
                "correction": "Kính Low-E",
                "explanation": "반사유리(kính phản quang)와 로이유리는 다른 기술입니다"
            },
            {
                "mistake": "한국 사양 그대로 적용",
                "correction": "베트남 기후에 맞는 태양열 차단형 선택",
                "explanation": "난방용과 냉방용 로이유리는 코팅 위치와 성능이 다릅니다"
            }
        ],
        "examples": [
            {
                "ko": "남측 외벽은 모두 로이유리로 적용해주세요",
                "vi": "Hãy áp dụng kính Low-E cho toàn bộ tường ngoài phía nam",
                "situation": "formal"
            },
            {
                "ko": "로이유리 코팅면이 안쪽으로 가야 합니다",
                "vi": "Mặt phủ Low-E phải hướng vào trong",
                "situation": "onsite"
            },
            {
                "ko": "SHGC 0.3 이하 로이유리로 변경합니다",
                "vi": "Thay đổi sang kính Low-E có SHGC dưới 0.3",
                "situation": "formal"
            }
        ],
        "relatedTerms": ["복층유리", "열관류율", "태양열취득률", "코팅"]
    },
    {
        "slug": "kinh-cuong-luc",
        "korean": "강화유리",
        "vietnamese": "Kính cường lực",
        "hanja": "強化유리",
        "hanjaReading": "강(강할 강) + 화(될 화)",
        "pronunciation": "강화유리",
        "difficulty": "basic",
        "category": "materials",
        "subcategory": "windows-glass",
        "meaningKo": "일반 유리를 고온으로 가열한 후 급속 냉각하여 표면에 압축응력을 형성시킨 안전유리입니다. 통역 시 주의할 점은 깨질 때 작은 입자로 부서져 '안전유리'라 불리지만, 일단 깨지면 전체가 파손되어 '파손 후 지지력 없음'을 반드시 설명해야 합니다. 베트남에서는 'kính an toàn'이라고도 하지만 공식 용어는 'kính cường lực'입니다. 한국은 두께 표기를 T로 하지만 베트남은 mm를 병기하는 경우가 많습니다.",
        "meaningVi": "Kính được gia nhiệt đến nhiệt độ cao rồi làm nguội đột ngột để tạo lớp ứng suất nén trên bề mặt, tăng độ bền gấp 5-7 lần kính thường. Khi vỡ, kính cường lực vỡ thành những mảnh nhỏ không sắc nhọn, giảm nguy cơ thương tích.",
        "context": "안전 기준, 샤워부스, 발코니 난간, 출입문",
        "culturalNote": "한국에서는 건축법상 일정 높이 이상 유리는 강화유리 또는 접합유리 사용이 의무이며, 안전 마크 표시가 엄격합니다. 베트남은 안전 기준이 느슨하여 일반 유리 사용이 많지만, 최근 고층 건물 사고로 인해 강화유리 의무화가 확대되고 있습니다. 베트남은 습도가 높아 강화유리 자연폭발(spontaneous breakage) 발생률이 한국보다 높으므로 Heat Soak Test 필요성을 강조해야 합니다.",
        "commonMistakes": [
            {
                "mistake": "안전유리 = 절대 안 깨진다",
                "correction": "안전유리 = 깨져도 덜 위험하다",
                "explanation": "강화유리도 충격을 받으면 깨지지만, 작은 입자로 부서져 부상 위험이 적습니다"
            },
            {
                "mistake": "Kính không vỡ",
                "correction": "Kính an toàn khi vỡ",
                "explanation": "깨지지 않는 유리가 아니라 깨져도 안전한 유리입니다"
            },
            {
                "mistake": "강화 후 절단 가능",
                "correction": "강화 전에 절단 완료 필수",
                "explanation": "강화유리는 강화 처리 후 절단/가공이 불가능합니다"
            }
        ],
        "examples": [
            {
                "ko": "난간 유리는 12T 강화유리로 해주세요",
                "vi": "Kính lan can làm bằng kính cường lực dày 12mm",
                "situation": "formal"
            },
            {
                "ko": "강화유리 모서리 깨졌어요",
                "vi": "Góc kính cường lực bị vỡ",
                "situation": "onsite"
            },
            {
                "ko": "HST 처리된 강화유리로 자연폭발 방지합니다",
                "vi": "Kính cường lực đã qua xử lý HST để ngăn vỡ tự nhiên",
                "situation": "formal"
            }
        ],
        "relatedTerms": ["접합유리", "안전유리", "열처리", "자연폭발"]
    },
    {
        "slug": "khung-nhom",
        "korean": "알루미늄창호",
        "vietnamese": "Khung nhôm",
        "hanja": "Aluminum 窗戶",
        "hanjaReading": None,
        "pronunciation": "알루미늄창호",
        "difficulty": "basic",
        "category": "materials",
        "subcategory": "windows-glass",
        "meaningKo": "알루미늄 합금으로 만든 창문 및 문틀 시스템으로, 가볍고 내구성이 우수하며 유지보수가 쉬운 창호재입니다. 통역 시 주의할 점은 한국에서는 '시스템창호'라고도 부르며, 단순 알루미늄 프레임과 구분하여 열교 차단(thermal break) 기능이 포함된 제품을 의미합니다. 베트남에서는 'cửa nhôm kính'이라고도 하지만 정확히는 'khung nhôm'이 프레임을 지칭합니다. 한국은 단열 성능을 중시하지만 베트nam은 부식 방지와 태풍 저항이 더 중요합니다.",
        "meaningVi": "Hệ thống khung cửa sổ và cửa đi làm từ hợp kim nhôm, có trọng lượng nhẹ, độ bền cao và dễ bảo trì. Khung nhôm được sử dụng phổ biến trong các công trình hiện đại nhờ tính thẩm mỹ và khả năng chống ăn mòn tốt trong điều kiện khí hậu nhiệt đới.",
        "context": "창호 공사, 외장재 선정, 건물 마감",
        "culturalNote": "한국에서는 아파트 표준 창호로 PVC와 경쟁하며, 고급 건물일수록 알루미늄창호 선호도가 높습니다. 베트남은 습도와 염분이 높아 양극산화 처리(anodizing)가 필수이며, 분체도장(powder coating)만으로는 부식이 빠르게 진행됩니다. 한국은 기밀성과 단열성을 중시하지만 베트남은 통풍과 방범을 더 중요하게 생각하여 설계 방향이 다릅니다. 태풍 지역은 풍압 설계 기준이 한국보다 엄격합니다.",
        "commonMistakes": [
            {
                "mistake": "알루미늄은 녹슬지 않는다",
                "correction": "알루미늄도 부식됩니다",
                "explanation": "알루미늄은 산화 피막으로 보호되지만, 염분과 습기가 많으면 부식됩니다"
            },
            {
                "mistake": "Cửa kính",
                "correction": "Khung nhôm kính",
                "explanation": "유리(kính)만이 아닌 프레임 시스템 전체를 지칭해야 합니다"
            },
            {
                "mistake": "열교차단 없이 시공",
                "correction": "단열 성능을 위해 열교차단재 필수",
                "explanation": "열대기후에서도 냉방 효율을 위해 열교차단이 중요합니다"
            }
        ],
        "examples": [
            {
                "ko": "70mm 시스템 알루미늄창호로 시공합니다",
                "vi": "Thi công bằng khung nhôm hệ thống 70mm",
                "situation": "formal"
            },
            {
                "ko": "창틀 모서리 실리콘 다시 쳐주세요",
                "vi": "Đánh silicon lại góc khung cửa",
                "situation": "onsite"
            },
            {
                "ko": "슬라이딩 방식에서 틸트 앤 턴으로 변경합니다",
                "vi": "Thay đổi từ kiểu trượt sang kiểu mở nghiêng và mở quay",
                "situation": "formal"
            }
        ],
        "relatedTerms": ["PVC창호", "열교차단", "양극산화", "분체도장"]
    },
    {
        "slug": "cua-nhua-pvc",
        "korean": "PVC창호",
        "vietnamese": "Cửa nhựa PVC",
        "hanja": None,
        "hanjaReading": None,
        "pronunciation": "피브이씨창호",
        "difficulty": "basic",
        "category": "materials",
        "subcategory": "windows-glass",
        "meaningKo": "폴리염화비닐(PVC) 수지로 만든 창문 프레임으로, 단열 성능이 우수하고 가격이 저렴하여 주거용 건물에 많이 사용되는 창호재입니다. 통역 시 주의할 점은 베트남에서는 'cửa nhựa'라고 하면 저가 플라스틱 창으로 오해할 수 있으므로 반드시 'PVC'를 명시해야 합니다. 한국은 내부 철심 보강(steel reinforcement)이 표준이지만 베트남은 생략하는 경우가 많아 강성 문제가 발생합니다. 열대기후에서는 자외선 열화가 빠르므로 UV 안정제 함유 여부를 확인해야 합니다.",
        "meaningVi": "Khung cửa làm từ nhựa PVC (polyvinyl chloride), có khả năng cách nhiệt tốt, giá thành hợp lý và được sử dụng phổ biến trong các công trình dân dụng. Cửa PVC có ưu điểm là không bị ăn mòn, cách âm tốt và không cần sơn bảo dưỡng.",
        "context": "주거용 건물, 창호 견적, 단열 공사",
        "culturalNote": "한국에서는 아파트 표준 창호로 PVC와 알루미늄이 경쟁하며, PVC는 단열 성능으로 북부 지역에서 선호됩니다. 베트남은 PVC창호를 저급 자재로 인식하여 고급 건물에서는 잘 사용하지 않으며, 알루미늄창호를 더 선호합니다. 한국 제품은 5챔버(chamber) 이상이 표준이지만 베트남은 3챔버 제품이 많아 단열 성능 차이가 큽니다. 열대기후에서는 PVC가 팽창/수축하여 기밀 성능이 저하되므로 시공 시 클리어런스 확보가 중요합니다.",
        "commonMistakes": [
            {
                "mistake": "PVC = 플라스틱 = 저급",
                "correction": "PVC는 고성능 엔지니어링 플라스틱",
                "explanation": "현대 PVC창호는 단열/차음 성능이 우수한 고급 자재입니다"
            },
            {
                "mistake": "Cửa nhựa thông thường",
                "correction": "Cửa nhựa PVC cao cấp",
                "explanation": "일반 플라스틱창과 구분하기 위해 '고급(cao cấp)'을 명시해야 합니다"
            },
            {
                "mistake": "철심 보강 생략",
                "correction": "대형 창호는 철심 보강 필수",
                "explanation": "철심 없이는 처짐과 변형이 발생합니다"
            }
        ],
        "examples": [
            {
                "ko": "5챔버 PVC창호로 단열 성능을 높였습니다",
                "vi": "Đã nâng cao hiệu quả cách nhiệt bằng cửa PVC 5 buồng",
                "situation": "formal"
            },
            {
                "ko": "PVC 프레임 색상 변색됐어요",
                "vi": "Khung PVC bị phai màu",
                "situation": "onsite"
            },
            {
                "ko": "독일 VEKA 프로파일 사용합니다",
                "vi": "Sử dụng profile VEKA của Đức",
                "situation": "formal"
            }
        ],
        "relatedTerms": ["알루미늄창호", "챔버", "철심보강", "프로파일"]
    },
    {
        "slug": "keo-silicone",
        "korean": "실란트",
        "vietnamese": "Keo silicone",
        "hanja": "Sealant",
        "hanjaReading": None,
        "pronunciation": "실란트",
        "difficulty": "basic",
        "category": "materials",
        "subcategory": "windows-glass",
        "meaningKo": "건축물의 접합부나 틈새를 메워 기밀·수밀·기능을 확보하는 충전재로, 주로 실리콘 계열이 사용됩니다. 통역 시 주의할 점은 한국에서는 '실리콘'과 '실란트'를 혼용하지만 엄밀히는 실란트가 상위 개념이며, 베트남에서는 'keo trám' 또는 'keo silicon'이라고 부릅니다. 구조용(structural)과 비구조용(non-structural)을 명확히 구분해야 하며, 커튼월 시공 시 양면 실란트 품질 관리가 누수 방지의 핵심입니다. 열대기후에서는 곰팡이 방지(anti-fungal) 기능이 필수입니다.",
        "meaningVi": "Vật liệu trám kín được sử dụng để lấp đầy khe hở và mối nối trong xây dựng, đảm bảo chống nước và chống thấm khí. Keo silicone là loại phổ biến nhất với độ đàn hồi cao và khả năng chịu thời tiết tốt, thường dùng cho cửa kính, tường rèm và các mối nối ngoài trời.",
        "context": "창호 시공, 방수 공사, 마감 작업",
        "culturalNote": "한국에서는 실란트 시공이 전문 직종(caulking specialist)으로 인정되며, 품질 기준이 엄격합니다. 베트남은 실란트를 단순 마감재로 인식하여 시공 품질이 떨어지는 경우가 많으며, 특히 프라이머 도포를 생략하여 접착 불량이 자주 발생합니다. 한국은 2성분형(two-component) 구조용 실란트가 표준이지만 베트남은 비용 절감을 위해 1성분형을 많이 사용합니다. 열대 우기 시즌에는 시공 후 경화 시간이 중요하므로 날씨 고려가 필수입니다.",
        "commonMistakes": [
            {
                "mistake": "실리콘 = 실란트",
                "correction": "실리콘은 실란트의 한 종류",
                "explanation": "실란트에는 실리콘, 폴리우레탄, 아크릴 등 다양한 종류가 있습니다"
            },
            {
                "mistake": "Keo dán kính",
                "correction": "Keo trám silicone",
                "explanation": "접착제(keo dán)가 아닌 충전재(keo trám)입니다"
            },
            {
                "mistake": "프라이머 생략",
                "correction": "접착면 프라이머 도포 필수",
                "explanation": "프라이머 없이는 실란트가 곧 탈락합니다"
            }
        ],
        "examples": [
            {
                "ko": "구조용 실란트로 유리 고정합니다",
                "vi": "Cố định kính bằng keo silicone kết cấu",
                "situation": "formal"
            },
            {
                "ko": "실란트 다 떨어졌어요, 다시 쳐야 됩니다",
                "vi": "Keo silicone bong hết rồi, phải đánh lại",
                "situation": "onsite"
            },
            {
                "ko": "중성 경화형 실란트 사용하세요",
                "vi": "Sử dụng keo silicone trung tính",
                "situation": "formal"
            }
        ],
        "relatedTerms": ["프라이머", "코킹", "실링", "방수"]
    },
    {
        "slug": "phu-kien-cua",
        "korean": "창호하드웨어",
        "vietnamese": "Phụ kiện cửa",
        "hanja": "窗戶 Hardware",
        "hanjaReading": None,
        "pronunciation": "창호하드웨어",
        "difficulty": "intermediate",
        "category": "materials",
        "subcategory": "windows-glass",
        "meaningKo": "창문과 문의 개폐, 잠금, 지지를 위한 금속 부속품 전체를 지칭하며, 경첩(hinge), 잠금장치(lock), 손잡이(handle) 등을 포함합니다. 통역 시 주의할 점은 한국에서는 '하드웨어'라는 영어를 그대로 사용하지만 베트남에서는 'phụ kiện'(부속품)이 더 자연스럽습니다. 독일/이탈리아 브랜드(Roto, Siegenia, Giesse)가 고급으로 인식되며, 중국산은 저가로 분류됩니다. 하드웨어 품질이 창호 수명을 결정하므로 'hardware는 싸게, 프레임은 비싸게'라는 접근은 위험합니다.",
        "meaningVi": "Tổng hợp các phụ kiện kim loại dùng để mở, đóng, khóa và đỡ cửa sổ/cửa đi, bao gồm bản lề, khóa, tay nắm, ray trượt, v.v. Chất lượng phụ kiện quyết định tuổi thọ và tính năng của toàn bộ hệ thống cửa, đặc biệt quan trọng với cửa lớn và cửa nặng.",
        "context": "창호 시공, 유지보수, 사양 결정",
        "culturalNote": "한국에서는 하드웨어를 창호 시스템의 일부로 통합 구매하는 경우가 많지만, 베트남은 프레임과 하드웨어를 별도 구매하여 호환성 문제가 자주 발생합니다. 한국은 다점잠금(multi-point locking)이 표준이지만 베트남은 단점잠금도 많이 사용합니다. 염분과 습도가 높아 스테인리스 스틸(SUS304 이상) 하드웨어가 필수이며, 도금 제품은 빠르게 부식됩니다. 태풍 지역은 강풍 시 창문이 떨어지지 않도록 안전 체인이나 제한기(restrictor) 설치가 중요합니다.",
        "commonMistakes": [
            {
                "mistake": "하드웨어는 나중에 교체하면 된다",
                "correction": "하드웨어는 프레임과 호환성이 중요합니다",
                "explanation": "나중에 교체하려면 프레임 가공이 필요할 수 있습니다"
            },
            {
                "mistake": "Linh kiện nhỏ không quan trọng",
                "correction": "Phụ kiện quyết định chất lượng cửa",
                "explanation": "작은 부품이지만 창호 전체 성능을 좌우합니다"
            },
            {
                "mistake": "도금 하드웨어 사용",
                "correction": "스테인리스 스틸 하드웨어 사용",
                "explanation": "열대 해안 지역에서는 도금이 빠르게 벗겨집니다"
            }
        ],
        "examples": [
            {
                "ko": "로토 틸트 앤 턴 하드웨어로 적용합니다",
                "vi": "Áp dụng phụ kiện Roto mở nghiêng và mở quay",
                "situation": "formal"
            },
            {
                "ko": "경첩 나사 풀렸어요, 조여주세요",
                "vi": "Vít bản lề lỏng rồi, vặn lại giúp tôi",
                "situation": "onsite"
            },
            {
                "ko": "SUS316 하드웨어로 부식 방지합니다",
                "vi": "Sử dụng phụ kiện SUS316 chống ăn mòn",
                "situation": "formal"
            }
        ],
        "relatedTerms": ["경첩", "잠금장치", "스테인리스", "다점잠금"]
    },
    {
        "slug": "luoi-chong-muoi",
        "korean": "방충망",
        "vietnamese": "Lưới chống muỗi",
        "hanja": "防蟲網",
        "hanjaReading": "방(막을 방) + 충(벌레 충) + 망(그물 망)",
        "pronunciation": "방충망",
        "difficulty": "basic",
        "category": "materials",
        "subcategory": "windows-glass",
        "meaningKo": "창문에 설치하여 벌레의 침입을 막으면서 통풍을 허용하는 그물망입니다. 통역 시 주의할 점은 베트남에서는 모기장(mosquito net)을 의미하는 'màn chống muỗi'와 구분하여 고정식 방충망은 'lưới chống muỗi'라고 부릅니다. 한국은 권취식(roll-up)이 주류이지만 베트남은 고정식과 여닫이식을 많이 사용하며, 열대지역 특성상 방충망이 선택이 아닌 필수입니다. 뎅기열, 말라리아 등 모기 매개 질병 예방을 위해 망목(mesh) 크기가 중요합니다.",
        "meaningVi": "Lưới lắp đặt trên cửa sổ để ngăn côn trùng xâm nhập đồng thời cho phép không khí lưu thông. Lưới chống muỗi đặc biệt quan trọng ở vùng nhiệt đới để phòng ngừa các bệnh do muỗi truyền như sốt xuất huyết, sốt rét. Có nhiều loại: lưới cố định, lưới cuốn, lưới xếp.",
        "context": "주거용 창호, 통풍 설계, 위생 관리",
        "culturalNote": "한국에서는 방충망이 미관을 해친다고 생각하여 최소화하는 경향이 있지만, 베트남은 건강과 직결되어 모든 창문에 필수로 설치합니다. 한국은 봄·여름만 사용하지만 베트남은 연중 설치가 기본입니다. 한국 방충망은 주로 회색/검정이지만 베트남은 흰색·은색을 선호하여 채광을 중시합니다. 도시 지역은 대기오염 때문에 방충망에 미세먼지가 쌓여 청소가 중요하며, 농촌은 말벌·전갈 침입 방지를 위해 더 촘촘한 망이 필요합니다.",
        "commonMistakes": [
            {
                "mistake": "방충망 = 모기장",
                "correction": "방충망은 창문 고정식, 모기장은 침대용",
                "explanation": "용도와 형태가 다릅니다"
            },
            {
                "mistake": "Màn tuyn",
                "correction": "Lưới chống muỗi",
                "explanation": "'màn tuyn'은 천으로 된 모기장이고, 'lưới'는 그물망입니다"
            },
            {
                "mistake": "망목 크기 무시",
                "correction": "모기 방지는 18×16 메시 이상 필요",
                "explanation": "망목이 크면 모기가 들어옵니다"
            }
        ],
        "examples": [
            {
                "ko": "권취식 방충망으로 설치합니다",
                "vi": "Lắp đặt lưới chống muỗi kiểu cuốn",
                "situation": "formal"
            },
            {
                "ko": "방충망 찢어졌어요, 교체해주세요",
                "vi": "Lưới chống muỗi bị rách, thay mới giúp tôi",
                "situation": "onsite"
            },
            {
                "ko": "스테인리스 방충망으로 내구성을 높였습니다",
                "vi": "Đã tăng độ bền bằng lưới inox chống muỗi",
                "situation": "formal"
            }
        ],
        "relatedTerms": ["창호", "통풍", "메시", "권취식"]
    },
    {
        "slug": "cua-tu-dong",
        "korean": "자동문",
        "vietnamese": "Cửa tự động",
        "hanja": "自動門",
        "hanjaReading": "자(스스로 자) + 동(움직일 동) + 문(문 문)",
        "pronunciation": "자동문",
        "difficulty": "intermediate",
        "category": "materials",
        "subcategory": "windows-glass",
        "meaningKo": "센서나 버튼을 통해 자동으로 개폐되는 출입문으로, 주로 상업시설이나 공공건물에 설치됩니다. 통역 시 주의할 점은 슬라이딩(sliding), 스윙(swing), 회전(revolving) 방식을 명확히 구분해야 하며, 베트남에서는 'cửa tự động trượt'(슬라이딩), 'cửa tự động quay'(회전) 등으로 세분화하여 부릅니다. 한국은 화재안전 기준(비상시 자동 개방)이 엄격하지만 베트남은 느슨하여 정전 시 수동 개방 방법 교육이 중요합니다. 접근성(accessibility) 기준이 강화되면서 장애인 편의를 위한 자동문 설치가 증가하고 있습니다.",
        "meaningVi": "Cửa ra vào tự động mở/đóng bằng cảm biến hoặc nút bấm, thường được lắp đặt tại các tòa nhà thương mại, khách sạn, bệnh viện. Cửa tự động giúp tiết kiệm năng lượng điều hòa, tăng tính thuận tiện và vệ sinh (không cần chạm tay), đồng thời hỗ trợ người khuyết tật và người mang vác.",
        "context": "상업시설, 빌딩 로비, 출입 통제",
        "culturalNote": "한국에서는 자동문이 고급 건물의 표준 설비로 인식되며, 에너지 절약과 방범 기능이 통합된 제품이 많습니다. 베트남은 정전이 잦아 UPS(무정전전원장치) 설치가 필수이며, 수동 개방 훈련이 중요합니다. 한국은 겨울철 냉기 차단을 위해 에어커튼과 함께 설치하지만, 베트남은 냉방 효율을 위해 빠른 개폐 속도를 선호합니다. 태풍 지역은 강풍 시 자동문 오작동이 자주 발생하므로 풍압 센서와 잠금 모드가 필요합니다.",
        "commonMistakes": [
            {
                "mistake": "자동문 = 무조건 안전",
                "correction": "센서 오작동 시 사고 위험",
                "explanation": "정기 점검과 안전장치 확인이 필수입니다"
            },
            {
                "mistake": "Cửa kính tự mở",
                "correction": "Cửa tự động",
                "explanation": "'자동으로 열리는 유리문'보다 '자동문'이 정확한 용어입니다"
            },
            {
                "mistake": "정전 대비 없음",
                "correction": "UPS 또는 수동 개방 장치 필수",
                "explanation": "정전 시 갇힐 수 있습니다"
            }
        ],
        "examples": [
            {
                "ko": "슬라이딩 자동문 센서 감도 조정해주세요",
                "vi": "Điều chỉnh độ nhạy cảm biến cửa tự động trượt",
                "situation": "formal"
            },
            {
                "ko": "자동문 안 닫혀요, 센서 확인 좀",
                "vi": "Cửa tự động không đóng, kiểm tra cảm biến giúp tôi",
                "situation": "onsite"
            },
            {
                "ko": "비상시 수동 개방 버튼은 우측에 있습니다",
                "vi": "Nút mở thủ công khẩn cấp ở bên phải",
                "situation": "formal"
            }
        ],
        "relatedTerms": ["센서", "슬라이딩", "UPS", "안전장치"]
    }
]

filtered = [t for t in new_terms if t['slug'] not in existing_slugs]
data.extend(filtered)

with open(file_path, 'w', encoding='utf-8') as f:
    json.dump(data, f, ensure_ascii=False, indent=2)

print(f"Added {len(filtered)} terms. Total: {len(data)}")
