import json
import os

file_path = os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', 'data', 'terms', 'construction.json')
with open(file_path, 'r', encoding='utf-8') as f:
    data = json.load(f)

existing_slugs = {t['slug'] for t in data}

new_terms = [
    {
        "slug": "tro-bay",
        "korean": "플라이애시",
        "vietnamese": "Tro bay",
        "hanja": None,
        "hanjaReading": None,
        "pronunciation": "플라이애시",
        "meaningKo": "석탄 화력발전소에서 미분탄 연소 시 발생하는 회분을 포집한 미세한 분말 형태의 산업부산물로, 콘크리트 혼화재로 사용됩니다. 통역 시 '포졸란 반응'과 '장기강도 증진' 효과를 함께 설명해야 하며, 베트남에서는 시멘트 대체재로 활발히 사용됩니다. 배합설계에서 일반적으로 시멘트 중량의 15-30%를 대체하며, 초기강도는 다소 낮으나 장기강도와 내구성이 우수합니다. 친환경 건설재료로 각광받고 있어 환경 인증 관련 통역에서 자주 등장합니다.",
        "meaningVi": "Tro bay là sản phẩm phụ dạng bột mịn thu được từ quá trình đốt than nghiền ở nhà máy nhiệt điện, được sử dụng làm phụ gia khoáng cho bê tông. Phản ứng pozzolan tạo ra sức bền dài hạn cao hơn và cải thiện độ bền của bê tông.",
        "context": "배합설계, 환경건설, 품질관리",
        "culturalNote": "한국에서는 '플라이애시'라는 영어 발음 그대로 사용하지만, 베트남에서는 'tro bay'(날아가는 재)라는 순수 베트남어로 표현합니다. 한국 건설 현장에서는 친환경성보다 경제성을 강조하는 경향이 있으나, 베트남에서는 최근 환경 규제 강화로 tro bay 사용이 의무화되는 프로젝트가 증가하고 있습니다. 통역 시 'phụ gia khoáng'(광물질 혼화재)라는 상위 개념도 함께 이해해야 합니다.",
        "commonMistakes": [
            {
                "mistake": "플라이애시를 '비산재'로만 번역",
                "correction": "tro bay 또는 phụ gia tro bay",
                "explanation": "'비산재'는 직역이지만 베트남 건설 현장에서는 tro bay가 표준 용어입니다"
            },
            {
                "mistake": "포졸란 반응을 '화산재 반응'으로 설명",
                "correction": "phản ứng pozzolan",
                "explanation": "포졸란은 화산재뿐 아니라 다양한 규산질 재료의 반응을 포함하는 기술 용어입니다"
            },
            {
                "mistake": "초기강도 저하를 단점으로만 설명",
                "correction": "초기강도는 낮으나 장기강도와 내구성이 우수함을 함께 설명",
                "explanation": "플라이애시의 특성을 균형있게 전달해야 발주처의 오해를 방지할 수 있습니다"
            }
        ],
        "examples": [
            {
                "ko": "이번 교량 공사에는 시멘트 중량의 20% 플라이애시를 혼입합니다.",
                "vi": "Công trình cầu này sẽ trộn tro bay tương đương 20% trọng lượng xi măng.",
                "situation": "formal"
            },
            {
                "ko": "플라이애시 사용으로 수화열을 낮춰 균열을 방지할 수 있습니다.",
                "vi": "Sử dụng tro bay giúp giảm nhiệt thủy hóa và ngăn ngừa nứt.",
                "situation": "onsite"
            },
            {
                "ko": "이 플라이애시는 KS L 5405 규격을 만족합니까?",
                "vi": "Tro bay này có đáp ứng tiêu chuẩn KS L 5405 không?",
                "situation": "formal"
            }
        ],
        "relatedTerms": ["혼화재", "포졸란", "고로슬래그미분말", "실리카퓸"]
    },
    {
        "slug": "silica-fume",
        "korean": "실리카퓸",
        "vietnamese": "Silica fume",
        "hanja": None,
        "hanjaReading": None,
        "pronunciation": "실리카퓸",
        "meaningKo": "규소(Si) 함유 합금 제조 시 발생하는 극미세 분말 형태의 부산물로, 콘크리트의 고강도화 및 치밀화에 사용되는 초미립자 혼화재입니다. 통역 시 '마이크로실리카'라는 별칭과 함께 입자크기가 시멘트의 1/100 수준임을 강조해야 합니다. 고성능 콘크리트, 초고강도 콘크리트, 해양구조물 등에 필수적이며, 일반적으로 시멘트 중량의 5-10% 범위로 사용됩니다. 가격이 비싸 경제성 검토가 필수이며, 작업성 저하를 보완하기 위해 고성능 감수제와 병행 사용합니다.",
        "meaningVi": "Silica fume là sản phẩm phụ dạng bột siêu mịn từ quá trình sản xuất hợp kim chứa silicon, được dùng làm phụ gia khoáng siêu mịn cho bê tông cường độ cao và bê tông đặc biệt. Kích thước hạt nhỏ hơn xi măng 100 lần, giúp bê tông đạt cường độ và độ chặt rất cao.",
        "context": "고성능콘크리트, 해양구조물, 초고층",
        "culturalNote": "한국에서는 '실리카퓸'과 '마이크로실리카'를 혼용하지만, 베트남에서는 'silica fume'이라는 영어 표현을 그대로 사용하거나 'phụ gia silica siêu mịn'으로 풀어 씁니다. 한국에서는 초고층 건물이나 해양구조물에 주로 사용되지만, 베트남에서는 최근 고속도로 포장에도 적용이 증가하고 있습니다. 가격이 플라이애시의 10배 이상이므로 경제성 논의 시 주의가 필요합니다.",
        "commonMistakes": [
            {
                "mistake": "마이크로실리카를 다른 물질로 오해",
                "correction": "silica fume과 microsilica는 동일 물질",
                "explanation": "두 용어는 같은 재료를 지칭하는 다른 표현입니다"
            },
            {
                "mistake": "사용량을 플라이애시와 동일하게 설명",
                "correction": "일반적으로 시멘트 중량의 5-10%로 훨씬 적게 사용",
                "explanation": "실리카퓸은 극소량으로도 효과가 크므로 과다 사용 시 경제성과 작업성 문제가 발생합니다"
            },
            {
                "mistake": "모든 콘크리트에 적용 가능하다고 설명",
                "correction": "고성능/초고강도 콘크리트 등 특수한 경우에 한정",
                "explanation": "일반 콘크리트에는 경제성이 맞지 않아 사용하지 않습니다"
            }
        ],
        "examples": [
            {
                "ko": "80MPa급 콘크리트를 위해 실리카퓸 8%를 혼입합니다.",
                "vi": "Để đạt bê tông cấp 80MPa, chúng tôi trộn 8% silica fume.",
                "situation": "formal"
            },
            {
                "ko": "실리카퓸 사용 시 고성능 감수제를 반드시 병행해야 합니다.",
                "vi": "Khi dùng silica fume phải kết hợp với phụ gia giảm nước cao cấp.",
                "situation": "onsite"
            },
            {
                "ko": "이 교각은 해수 접촉 구간이라 실리카퓸 적용이 필수입니다.",
                "vi": "Trụ cầu này tiếp xúc nước biển nên bắt buộc phải dùng silica fume.",
                "situation": "formal"
            }
        ],
        "relatedTerms": ["마이크로실리카", "고성능콘크리트", "초고강도콘크리트", "고성능감수제"]
    },
    {
        "slug": "phu-gia-ae",
        "korean": "AE제",
        "vietnamese": "Phụ gia AE",
        "hanja": None,
        "hanjaReading": None,
        "pronunciation": "에이이제",
        "meaningKo": "Air Entraining Agent의 약자로, 콘크리트 내부에 미세한 독립기포를 연행시켜 동결융해 저항성을 향상시키는 혼화제입니다. 통역 시 '공기연행제' 또는 '기포발생제'로도 불리며, 한랭지 시공이나 동결융해 반복 환경에서 필수적임을 강조해야 합니다. 일반적으로 공기량 4-6%를 목표로 하며, 과다 사용 시 강도 저하가 발생하므로 정밀한 품질관리가 요구됩니다. 워커빌리티 개선 효과도 있어 펌프 압송성 향상에도 기여합니다.",
        "meaningVi": "AE (Air Entraining) là phụ gia tạo bọt khí nhỏ độc lập trong bê tông, giúp tăng khả năng chống đông - tan băng. Thường tạo ra hàm lượng khí 4-6% trong bê tông, cải thiện độ bền trong môi trường lạnh giá và tăng tính thi công.",
        "context": "한랭지시공, 동결융해, 내구성",
        "culturalNote": "한국에서는 'AE제'라는 약어를 일상적으로 사용하지만, 베트남에서는 'phụ gia AE' 또는 'phụ gia tạo bọt khí'로 풀어서 설명해야 합니다. 한국은 겨울철 동결융해가 심해 AE제 사용이 일반화되어 있으나, 베트남 남부 열대 지역에서는 생소한 개념일 수 있습니다. 다만 베트남 북부 산악지대나 냉동창고 등에서는 필수이므로 지역별 기후 특성을 고려한 설명이 필요합니다.",
        "commonMistakes": [
            {
                "mistake": "AE제를 '방수제'로 오해",
                "correction": "동결융해 저항성 향상이 주 목적",
                "explanation": "방수 효과는 부수적이며, 주 기능은 동결융해 환경에서의 내구성 확보입니다"
            },
            {
                "mistake": "공기량이 많을수록 좋다고 설명",
                "correction": "적정 공기량(4-6%) 관리가 중요, 과다 시 강도 저하",
                "explanation": "공기량 1% 증가마다 압축강도가 약 5% 감소하므로 정밀 관리가 필수입니다"
            },
            {
                "mistake": "AE제와 AE감수제를 동일하게 취급",
                "correction": "AE제는 공기연행만, AE감수제는 공기연행+감수 기능 복합",
                "explanation": "두 제품은 기능과 용도가 다르므로 명확히 구분해야 합니다"
            }
        ],
        "examples": [
            {
                "ko": "이번 동절기 타설에는 AE제를 0.01% 혼입합니다.",
                "vi": "Đổ bê tông mùa đông này sẽ trộn 0.01% phụ gia AE.",
                "situation": "onsite"
            },
            {
                "ko": "공기량 측정 결과 5.2%로 기준 범위 내입니다.",
                "vi": "Kết quả đo hàm lượng khí là 5.2%, nằm trong phạm vi tiêu chuẩn.",
                "situation": "formal"
            },
            {
                "ko": "AE제 사용으로 펌프 압송이 훨씬 원활해졌습니다.",
                "vi": "Nhờ dùng phụ gia AE, bơm bê tông trơn tru hơn nhiều.",
                "situation": "informal"
            }
        ],
        "relatedTerms": ["공기연행제", "AE감수제", "동결융해", "워커빌리티"]
    },
    {
        "slug": "phu-gia-giam-nuoc",
        "korean": "감수제",
        "vietnamese": "Phụ gia giảm nước",
        "hanja": "減水劑",
        "hanjaReading": "減(덜 감) + 水(물 수) + 劑(약제 제)",
        "pronunciation": "감수제",
        "meaningKo": "콘크리트의 단위수량을 감소시켜 동일한 워커빌리티에서 물-시멘트비를 낮춤으로써 강도와 내구성을 향상시키는 혼화제입니다. 통역 시 '표준형', '고성능(高性能)', '고성능AE형'으로 구분되며, 감수율에 따라 효과와 적용 범위가 크게 달라짐을 설명해야 합니다. 표준형은 8-12% 감수, 고성능형은 15-30% 감수 효과를 나타내며, 최근에는 유동화제와 결합된 제품도 많습니다. 슬럼프 유지 시간과 응결 지연 정도를 파악하여 현장 조건에 맞게 선정해야 합니다.",
        "meaningVi": "Phụ gia giảm nước là chất làm giảm lượng nước đơn vị trong bê tông, từ đó giảm tỷ lệ nước/xi măng và tăng cường độ, độ bền. Có các loại tiêu chuẩn (giảm 8-12%), cao cấp (giảm 15-30%), kết hợp với AE hoặc chất hóa lỏng.",
        "context": "배합설계, 품질관리, 레미콘",
        "culturalNote": "한국에서는 '감수제'라는 한자어가 일반적이지만, 베트남에서는 'phụ gia giảm nước'(물 줄이는 혼화제)로 직역합니다. 한국 건설 현장에서는 감수제를 거의 표준으로 사용하지만, 베트남에서는 아직 일반 공사에서는 비용 문제로 선택적으로 사용합니다. '고성능 감수제'를 베트남어로는 'phụ gia giảm nước cao cấp' 또는 'superplasticizer'로 표현하며, 후자가 기술자들 사이에서 더 널리 통용됩니다.",
        "commonMistakes": [
            {
                "mistake": "감수제를 단순히 물 줄이는 재료로만 설명",
                "correction": "물-시멘트비 저감을 통한 강도/내구성 향상이 목적",
                "explanation": "감수제의 핵심은 물을 줄이는 것이 아니라 성능을 향상시키는 것입니다"
            },
            {
                "mistake": "모든 감수제가 동일한 효과를 낸다고 설명",
                "correction": "표준형/고성능형/유동화형 등 종류별 효과가 크게 다름",
                "explanation": "감수율과 슬럼프 유지 시간이 제품마다 달라 현장 조건에 맞는 선택이 필요합니다"
            },
            {
                "mistake": "감수제 과다 투입으로 슬럼프를 조정",
                "correction": "정해진 배합비 준수, 슬럼프 조정은 AE제나 증점제 활용",
                "explanation": "감수제 과다 사용은 응결 지연 및 재료분리를 유발할 수 있습니다"
            }
        ],
        "examples": [
            {
                "ko": "이번 배합에는 고성능 감수제를 1.5% 사용합니다.",
                "vi": "Cấp phối này sử dụng 1.5% phụ gia giảm nước cao cấp.",
                "situation": "formal"
            },
            {
                "ko": "감수제 덕분에 물시멘트비를 45%에서 38%로 낮췄습니다.",
                "vi": "Nhờ phụ gia giảm nước, đã giảm tỷ lệ N/X từ 45% xuống 38%.",
                "situation": "onsite"
            },
            {
                "ko": "이 감수제는 슬럼프 유지 시간이 90분 이상입니다.",
                "vi": "Phụ gia này duy trì độ sụt trên 90 phút.",
                "situation": "formal"
            }
        ],
        "relatedTerms": ["고성능감수제", "유동화제", "물시멘트비", "워커빌리티"]
    },
    {
        "slug": "be-tong-luu-dong-cao",
        "korean": "고유동콘크리트",
        "vietnamese": "Bê tông lưu động cao",
        "hanja": "高流動콘크리트",
        "hanjaReading": "高(높을 고) + 流(흐를 류) + 動(움직일 동)",
        "pronunciation": "고유동콘크리트",
        "meaningKo": "고성능 감수제를 사용하여 진동다짐 없이도 자중으로 충전이 가능한 고유동성 콘크리트로, SCC(Self-Compacting Concrete)라고도 합니다. 통역 시 '자기충전성', '재료분리 저항성', '충전성'의 3대 요구성능을 반드시 설명해야 하며, 슬럼프플로 550-650mm 범위를 목표로 합니다. 철근 밀집 구간, 복잡한 형상, 접근 곤란 부위 등에 효과적이며, 진동다짐 생략으로 소음 감소 및 공기 단축이 가능합니다. 다만 배합설계와 품질관리가 까다로워 숙련된 기술이 필요합니다.",
        "meaningVi": "Bê tông lưu động cao (SCC - Self-Compacting Concrete) là loại bê tông có khả năng tự chảy và tự đầm lèn bằng trọng lượng bản thân mà không cần rung. Có độ chảy xòe 550-650mm, khả năng tự chèn lấp, chống phân tầng tốt, thích hợp với khu vực cốt thép dày đặc hoặc khuôn phức tạp.",
        "context": "고성능콘크리트, 프리캐스트, 복잡단면",
        "culturalNote": "한국에서는 '고유동콘크리트'와 'SCC'를 혼용하지만, 베트남에서는 'bê tông tự đầm' (자기다짐 콘크리트) 또는 'bê tông lưu động cao'로 표현합니다. 한국에서는 프리캐스트 공장과 복잡한 형상의 현장타설에 주로 사용되지만, 베트남에서는 아직 고급 공사에 한정되어 사용됩니다. '자기충전 콘크리트'라는 표현도 있으나 'tự đầm'이 더 직관적이고 널리 쓰입니다.",
        "commonMistakes": [
            {
                "mistake": "고유동콘크리트를 단순히 '슬럼프가 높은 콘크리트'로 설명",
                "correction": "자기충전성, 재료분리 저항성, 충전성을 갖춘 특수 콘크리트",
                "explanation": "단순히 물을 많이 넣어 슬럼프를 높인 것과는 근본적으로 다릅니다"
            },
            {
                "mistake": "모든 부위에 사용 가능하다고 설명",
                "correction": "철근 밀집부, 복잡형상 등 특수 부위에 선택적 적용",
                "explanation": "일반 부위에는 경제성이 맞지 않으며, 배합 관리가 어려워 숙련 필요"
            },
            {
                "mistake": "진동다짐을 전혀 하지 않아도 된다고 강조",
                "correction": "자기충전성이 있으나 필요시 최소한의 다짐은 가능",
                "explanation": "재료분리나 기포 제거를 위해 경미한 진동을 추가할 수 있습니다"
            }
        ],
        "examples": [
            {
                "ko": "이 기둥은 철근이 밀집되어 있어 고유동콘크리트를 적용합니다.",
                "vi": "Cột này có cốt thép dày đặc nên áp dụng bê tông tự đầm.",
                "situation": "onsite"
            },
            {
                "ko": "슬럼프플로 시험 결과 620mm로 기준을 만족합니다.",
                "vi": "Kết quả thử độ chảy xòe là 620mm, đạt tiêu chuẩn.",
                "situation": "formal"
            },
            {
                "ko": "고유동콘크리트 사용으로 타설 시간이 30% 단축되었습니다.",
                "vi": "Nhờ dùng bê tông lưu động cao, thời gian đổ giảm 30%.",
                "situation": "informal"
            }
        ],
        "relatedTerms": ["SCC", "자기충전콘크리트", "슬럼프플로", "고성능감수제"]
    },
    {
        "slug": "be-tong-phun",
        "korean": "숏크리트",
        "vietnamese": "Bê tông phun",
        "hanja": None,
        "hanjaReading": None,
        "pronunciation": "숏크리트",
        "meaningKo": "시멘트, 골재, 물 등을 압축공기로 고속 분사하여 타설과 다짐을 동시에 수행하는 특수 콘크리트 공법으로, 터널, 비탈면, 보수보강 공사에 주로 사용됩니다. 통역 시 '건식(Dry Mix)'과 '습식(Wet Mix)' 방법의 차이를 명확히 구분해야 하며, 리바운드(반발재)가 10-30% 발생함을 설명해야 합니다. 조기강도 발현이 빠르고 시공성이 우수하나, 숙련된 노즐맨(Nozzleman)이 필수이며, 분진과 소음 문제를 관리해야 합니다. 철망이나 강섬유로 보강하여 균열 저항성을 높입니다.",
        "meaningVi": "Bê tông phun (Shotcrete) là phương pháp phun hỗn hợp xi măng, cốt liệu, nước bằng khí nén áp suất cao, đồng thời đổ và đầm lèn. Dùng trong hầm, taluy, gia cố. Có phương pháp khô (Dry Mix) và ướt (Wet Mix), tỷ lệ nảy hồi (rebound) 10-30%.",
        "context": "터널공사, 비탈면보강, 보수공사",
        "culturalNote": "한국에서는 '숏크리트'라는 영어 발음을 그대로 사용하지만, 베트남에서는 'bê tông phun'(분사 콘크리트)이라는 순수 베트남어를 주로 씁니다. 한국에서는 터널공사의 표준 공법이나, 베트남에서는 아직 대형 인프라 프로젝트에 한정되어 사용됩니다. '건식/습식'을 베트nam어로 'phun khô/phun ướt'로 표현하며, 노즐맨은 'thợ điều khiển vòi phun'으로 번역합니다.",
        "commonMistakes": [
            {
                "mistake": "숏크리트를 일반 콘크리트 타설과 동일하게 설명",
                "correction": "고속 분사로 타설과 다짐을 동시에 수행하는 특수 공법",
                "explanation": "분사 압력으로 골재가 박히면서 다져지므로 일반 타설과 완전히 다릅니다"
            },
            {
                "mistake": "건식과 습식의 차이를 모호하게 설명",
                "correction": "건식은 노즐에서 물 혼합, 습식은 미리 혼합 후 분사",
                "explanation": "두 방식은 장비, 리바운드율, 품질이 다르므로 명확히 구분해야 합니다"
            },
            {
                "mistake": "리바운드를 품질 불량으로 오해",
                "correction": "숏크리트 공법의 불가피한 특성, 관리 범위 내 허용",
                "explanation": "리바운드는 공법 특성상 발생하며, 10-30% 범위는 정상입니다"
            }
        ],
        "examples": [
            {
                "ko": "이번 터널 구간은 습식 숏크리트 공법을 적용합니다.",
                "vi": "Đoạn hầm này áp dụng phương pháp bê tông phun ướt.",
                "situation": "formal"
            },
            {
                "ko": "숏크리트 두께는 200mm, 철망 보강을 실시합니다.",
                "vi": "Độ dày bê tông phun là 200mm, gia cố bằng lưới thép.",
                "situation": "onsite"
            },
            {
                "ko": "노즐맨의 숙련도가 숏크리트 품질을 좌우합니다.",
                "vi": "Trình độ thợ điều khiển vòi phun quyết định chất lượng shotcrete.",
                "situation": "informal"
            }
        ],
        "relatedTerms": ["건식숏크리트", "습식숏크리트", "리바운드", "노즐맨"]
    },
    {
        "slug": "be-tong-duoi-nuoc",
        "korean": "수중콘크리트",
        "vietnamese": "Bê tông dưới nước",
        "hanja": "水中콘크리트",
        "hanjaReading": "水(물 수) + 中(가운데 중)",
        "pronunciation": "수중콘크리트",
        "meaningKo": "물속에서 타설하는 콘크리트로, 재료분리를 방지하고 소요 강도를 확보하기 위해 특수한 배합과 시공방법을 사용합니다. 통역 시 '트레미관 공법', '콘크리트 펌프 공법', '프리팩트 콘크리트 공법'을 구분하여 설명해야 하며, 재료분리 방지를 위해 수중불분리성 혼화제를 필수로 사용함을 강조해야 합니다. 일반 콘크리트보다 단위시멘트량을 10-15% 증가시키고, 슬럼프는 18-21cm로 높게 관리합니다. 타설 속도와 연속성이 중요하며, 중단 시 콜드조인트 발생 위험이 큽니다.",
        "meaningVi": "Bê tông dưới nước là bê tông đổ trong môi trường nước, sử dụng phụ gia chống phân tầng trong nước và phương pháp thi công đặc biệt như ống Tremie, bơm, hoặc preplaced aggregate. Hàm lượng xi măng tăng 10-15%, độ sụt 18-21cm.",
        "context": "교량기초, 항만공사, 해양구조물",
        "culturalNote": "한국에서는 '수중콘크리트'라는 한자어를 쓰지만, 베트남에서는 'bê tông dưới nước'(물 아래 콘크리트)로 직역합니다. 한국에서는 교량 교각 기초나 항만 공사에서 일상적이나, 베트남에서는 대형 인프라 프로젝트에 한정됩니다. '트레미관'은 베트남어로 'ống Tremie'로 음차하며, '수중불분리성 혼화제'는 'phụ gia chống phân tầng trong nước'로 길게 풀어 씁니다.",
        "commonMistakes": [
            {
                "mistake": "수중콘크리트를 일반 콘크리트로 타설해도 된다고 설명",
                "correction": "수중불분리성 혼화제와 특수 배합 필수",
                "explanation": "일반 콘크리트를 물속에 타설하면 재료분리로 강도를 확보할 수 없습니다"
            },
            {
                "mistake": "트레미관 끝을 콘크리트 표면 위로 노출시켜도 된다고 설명",
                "correction": "트레미관 끝은 항상 콘크리트 속에 1m 이상 매입 유지",
                "explanation": "관 끝이 노출되면 콘크리트가 물과 직접 접촉하여 재료분리가 발생합니다"
            },
            {
                "mistake": "타설 중 일시 중단해도 문제없다고 설명",
                "correction": "연속 타설 필수, 중단 시 콜드조인트 발생",
                "explanation": "수중콘크리트는 연속성이 매우 중요하며, 중단 시 구조적 결함이 발생합니다"
            }
        ],
        "examples": [
            {
                "ko": "이 교각 기초는 수심 15m에서 수중콘크리트로 타설합니다.",
                "vi": "Móng trụ cầu này đổ bê tông dưới nước ở độ sâu 15m.",
                "situation": "formal"
            },
            {
                "ko": "트레미관을 통해 콘크리트를 연속 타설 중입니다.",
                "vi": "Đang đổ bê tông liên tục qua ống Tremie.",
                "situation": "onsite"
            },
            {
                "ko": "수중불분리성 혼화제 덕분에 재료분리 없이 타설되었습니다.",
                "vi": "Nhờ phụ gia chống phân tầng, bê tông đổ không bị tách lớp.",
                "situation": "informal"
            }
        ],
        "relatedTerms": ["트레미관", "수중불분리성혼화제", "프리팩트콘크리트", "재료분리"]
    },
    {
        "slug": "be-tong-khoi-lon",
        "korean": "매스콘크리트",
        "vietnamese": "Bê tông khối lớn",
        "hanja": None,
        "hanjaReading": None,
        "pronunciation": "매스콘크리트",
        "meaningKo": "부재의 치수가 커서 시멘트 수화열에 의한 온도 상승을 고려하여 설계·시공해야 하는 콘크리트로, 일반적으로 최소 단면이 80cm 이상이거나 부재 내부 최고온도와 표면온도 차이가 25℃를 초과할 우려가 있는 경우를 말합니다. 통역 시 '온도균열', '수화열 제어', '온도응력 해석'을 핵심으로 설명해야 하며, 플라이애시나 고로슬래그를 사용한 저발열 시멘트 적용을 강조해야 합니다. 타설 후 보온양생과 함께 파이프 쿨링(Pipe Cooling) 등 온도 관리가 필수이며, 온도 측정을 실시간으로 수행합니다.",
        "meaningVi": "Bê tông khối lớn (Mass Concrete) là loại bê tông có kích thước lớn (thường trên 80cm) cần kiểm soát nhiệt thủy hóa để tránh nứt nhiệt. Sử dụng xi măng ít tỏa nhiệt (có tro bay, xỉ lò cao), thi công làm nguội bằng ống (pipe cooling), theo dõi nhiệt độ liên tục.",
        "context": "댐, 교량기초, 대형기초판",
        "culturalNote": "한국에서는 'Mass Concrete'를 '매스콘크리트'로 음차하지만, 베트남에서는 'bê tông khối lớn'(큰 덩어리 콘크리트)으로 의역합니다. 한국에서는 댐, 교량 기초, 초고층 건물 기초판 등에 널리 사용되나, 베트남에서는 주로 수력발전 댐 프로젝트에 한정됩니다. '파이프 쿨링'은 'làm nguội bằng ống' 또는 그대로 'pipe cooling'으로 표현하며, 후자가 기술자들 사이에서 더 통용됩니다.",
        "commonMistakes": [
            {
                "mistake": "매스콘크리트를 단순히 '양이 많은 콘크리트'로 설명",
                "correction": "수화열 관리가 필요한 대단면 콘크리트",
                "explanation": "핵심은 양이 아니라 부재 크기로 인한 온도 관리입니다"
            },
            {
                "mistake": "일반 콘크리트와 동일한 배합을 사용해도 된다고 설명",
                "correction": "저발열 시멘트, 플라이애시 등으로 수화열 저감 필수",
                "explanation": "일반 배합으로는 내부 온도가 과도하게 상승하여 온도균열이 발생합니다"
            },
            {
                "mistake": "타설 후 관리가 불필요하다고 설명",
                "correction": "온도 측정, 파이프 쿨링, 보온양생 등 지속 관리 필수",
                "explanation": "타설 후 수일~수주간 온도 관리가 품질을 결정합니다"
            }
        ],
        "examples": [
            {
                "ko": "이 교량 기초는 두께 2m의 매스콘크리트로 타설합니다.",
                "vi": "Móng cầu này đổ bê tông khối lớn dày 2m.",
                "situation": "formal"
            },
            {
                "ko": "파이프 쿨링 시스템을 가동하여 내부 온도를 낮추고 있습니다.",
                "vi": "Đang vận hành hệ thống pipe cooling để giảm nhiệt độ bên trong.",
                "situation": "onsite"
            },
            {
                "ko": "온도 센서 데이터를 보니 내외부 온도차가 20℃입니다.",
                "vi": "Theo dữ liệu cảm biến, chênh lệch nhiệt độ trong-ngoài là 20℃.",
                "situation": "informal"
            }
        ],
        "relatedTerms": ["수화열", "온도균열", "파이프쿨링", "저발열시멘트"]
    },
    {
        "slug": "be-tong-nhe",
        "korean": "경량콘크리트",
        "vietnamese": "Bê tông nhẹ",
        "hanja": "輕量콘크리트",
        "hanjaReading": "輕(가벼울 경) + 量(양 량)",
        "pronunciation": "경량콘크리트",
        "meaningKo": "일반 콘크리트보다 가벼운 콘크리트로, 기건 단위용적질량이 2.0t/m³ 미만인 것을 말하며, 경량골재나 기포를 사용하여 제조합니다. 통역 시 '경량골재 콘크리트'와 '기포 콘크리트'를 구분해야 하며, 자중 경감, 단열성 향상, 시공성 개선 등의 장점을 설명해야 합니다. 고층 건물의 상층부 벽체, 지붕, 충진재 등에 사용되며, 압축강도는 일반 콘크리트보다 낮으나 최근에는 구조용 경량콘크리트도 개발되어 사용됩니다. 흡수율이 높아 방수 및 양생 관리가 중요합니다.",
        "meaningVi": "Bê tông nhẹ là loại bê tông có khối lượng thể tích khô dưới 2.0 tấn/m³, sử dụng cốt liệu nhẹ hoặc bọt khí. Giảm trọng lượng bản thân, tăng cách nhiệt, dùng cho tường tầng cao, mái, vật liệu lấp đầy. Cường độ nén thấp hơn bê tông thường.",
        "context": "고층건물, 단열재, 충진재",
        "culturalNote": "한국에서는 '경량콘크리트'라는 한자어를 쓰지만, 베트남에서는 'bê tông nhẹ'(가벼운 콘크리트)로 직역합니다. 한국에서는 고층 건물의 자중 저감을 위해 활발히 사용되나, 베트남에서는 아직 일부 고급 건물에 한정됩니다. '경량골재'는 'cốt liệu nhẹ', '기포 콘크리트'는 'bê tông bọt khí'로 번역하며, 단열 성능을 강조할 때는 'cách nhiệt'이라는 단어를 추가합니다.",
        "commonMistakes": [
            {
                "mistake": "경량콘크리트가 강도가 약해 구조용으로 쓸 수 없다고 단정",
                "correction": "일반적으로 강도가 낮으나, 구조용 경량콘크리트도 개발됨",
                "explanation": "최근에는 20-30MPa급 구조용 경량콘크리트도 사용되고 있습니다"
            },
            {
                "mistake": "경량골재 콘크리트와 기포 콘크리트를 동일하게 취급",
                "correction": "제조 방법, 강도, 용도가 다른 별개 종류",
                "explanation": "경량골재 콘크리트는 구조용 가능하나, 기포 콘크리트는 주로 충진·단열용입니다"
            },
            {
                "mistake": "일반 콘크리트와 동일한 양생 관리로 충분하다고 설명",
                "correction": "흡수율이 높아 방수 및 양생 관리가 더 엄격히 필요",
                "explanation": "경량골재의 높은 흡수율로 인해 초기 양생과 방수 처리가 매우 중요합니다"
            }
        ],
        "examples": [
            {
                "ko": "이 건물 상층부는 자중 저감을 위해 경량콘크리트를 사용합니다.",
                "vi": "Tầng cao của tòa nhà dùng bê tông nhẹ để giảm trọng lượng.",
                "situation": "formal"
            },
            {
                "ko": "경량콘크리트 타설 후 즉시 양생 조치를 실시하세요.",
                "vi": "Sau khi đổ bê tông nhẹ, thực hiện bảo dưỡng ngay lập tức.",
                "situation": "onsite"
            },
            {
                "ko": "이 경량콘크리트는 단위중량 1.8t/m³, 강도 18MPa입니다.",
                "vi": "Bê tông nhẹ này có trọng lượng đơn vị 1.8 tấn/m³, cường độ 18MPa.",
                "situation": "formal"
            }
        ],
        "relatedTerms": ["경량골재", "기포콘크리트", "단열콘크리트", "충진재"]
    },
    {
        "slug": "be-tong-cot-soi",
        "korean": "섬유보강콘크리트",
        "vietnamese": "Bê tông cốt sợi",
        "hanja": "纖維補強콘크리트",
        "hanjaReading": "纖(가는실 섬) + 維(벌레 유) + 補(기울 보) + 強(강할 강)",
        "pronunciation": "섬유보강콘크리트",
        "meaningKo": "콘크리트 내부에 강섬유, 유리섬유, 합성섬유 등을 혼입하여 인장강도, 휨강도, 균열저항성, 인성을 향상시킨 콘크리트입니다. 통역 시 '강섬유(Steel Fiber)', '폴리프로필렌 섬유(PP Fiber)', '유리섬유(Glass Fiber)' 등 섬유 종류별 특성을 구분하여 설명해야 하며, 일반적으로 콘크리트 부피의 0.5-2.0% 범위로 혼입함을 명시해야 합니다. 터널 라이닝, 산업 바닥, 보수재 등에 사용되며, 철근 대체 또는 보조 효과가 있습니다. 섬유 분산성과 워커빌리티 관리가 중요합니다.",
        "meaningVi": "Bê tông cốt sợi là bê tông trộn sợi thép, sợi thủy tinh, sợi tổng hợp để tăng cường độ kéo, chống uốn, chống nứt, độ dẻo dai. Hàm lượng sợi 0.5-2.0% thể tích, dùng cho hầm, sàn công nghiệp, vật liệu sửa chữa. Sợi có thể thay thế hoặc hỗ trợ cốt thép.",
        "context": "터널, 산업바닥, 보수공사",
        "culturalNote": "한국에서는 '섬유보강콘크리트' 또는 'FRC(Fiber Reinforced Concrete)'를 쓰지만, 베트남에서는 'bê tông cốt sợi'(섬유 철근 콘크리트)로 표현합니다. 한국에서는 터널과 산업 바닥에 널리 사용되나, 베트남에서는 아직 고급 프로젝트에 한정됩니다. '강섬유'는 'sợi thép', '폴리프로필렌 섬유'는 'sợi PP' 또는 'sợi polypropylene', '유리섬유'는 'sợi thủy tinh'으로 번역합니다.",
        "commonMistakes": [
            {
                "mistake": "섬유보강콘크리트가 철근을 완전히 대체한다고 설명",
                "correction": "철근 보조 또는 일부 대체, 구조적 철근은 여전히 필요",
                "explanation": "섬유는 균열 제어와 인성 향상이 주목적이며, 주 구조철근을 대체하지는 못합니다"
            },
            {
                "mistake": "모든 섬유가 동일한 효과를 낸다고 설명",
                "correction": "강섬유/유리섬유/합성섬유 각각 특성과 용도가 다름",
                "explanation": "강섬유는 구조 보강, PP섬유는 균열 방지, 유리섬유는 내화성 등 차이가 있습니다"
            },
            {
                "mistake": "섬유를 많이 넣을수록 좋다고 설명",
                "correction": "과다 혼입 시 워커빌리티 저하 및 섬유 뭉침 발생",
                "explanation": "일반적으로 2% 이하로 사용하며, 과다 시 시공성이 크게 떨어집니다"
            }
        ],
        "examples": [
            {
                "ko": "이 터널 라이닝에는 강섬유 1.5%를 혼입한 콘크리트를 사용합니다.",
                "vi": "Vỏ hầm này dùng bê tông trộn 1.5% sợi thép.",
                "situation": "formal"
            },
            {
                "ko": "섬유보강콘크리트 덕분에 균열이 현저히 감소했습니다.",
                "vi": "Nhờ bê tông cốt sợi, vết nứt giảm đáng kể.",
                "situation": "informal"
            },
            {
                "ko": "PP섬유는 초기 양생 균열 방지에 효과적입니다.",
                "vi": "Sợi PP hiệu quả trong việc ngăn nứt giai đoạn đầu.",
                "situation": "onsite"
            }
        ],
        "relatedTerms": ["강섬유", "PP섬유", "유리섬유", "FRC"]
    }
]

filtered = [t for t in new_terms if t['slug'] not in existing_slugs]
data.extend(filtered)

with open(file_path, 'w', encoding='utf-8') as f:
    json.dump(data, f, ensure_ascii=False, indent=2)

print(f"Added {len(filtered)} terms. Total: {len(data)}")
