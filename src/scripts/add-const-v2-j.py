import json
import os

# construction.json 경로
file_path = os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', 'data', 'terms', 'construction.json')

# 기존 용어 로드 (data는 배열!)
with open(file_path, 'r', encoding='utf-8') as f:
    data = json.load(f)

existing_slugs = {term['slug'] for term in data}

# 새 용어 10개: 방수/단열/보온 (Waterproofing & Insulation)
new_terms = [
    {
        "slug": "phuong-phap-chong-tham-tam",
        "korean": "시트방수",
        "vietnamese": "Phương pháp chống thấm tấm",
        "hanja": "시트防水",
        "hanjaReading": "시(베풀 시) + 트(없음, 외래어) + 방(막을 방) + 수(물 수)",
        "pronunciation": "시트방수",
        "meaningKo": "시트 형태의 방수재를 바닥이나 벽면에 붙여서 물이 스며드는 것을 막는 공법입니다. 아스팔트 시트, 고무 아스팔트 시트, 합성고분자계 시트 등이 있으며, 시공이 비교적 간단하고 균일한 두께를 유지할 수 있어 옥상이나 화장실 방수에 많이 사용됩니다. 통역 시 베트남 현장에서는 'màng chống thấm'(방수막)이라는 표현을 더 자주 쓰므로, 시트 타입임을 명확히 전달하려면 'tấm' 또는 'cuộn'(롤)이라는 단어를 추가하는 것이 좋습니다. 특히 시공 방법(열풍 용접, 접착제 도포, 기계적 고정 등)을 설명할 때는 한국 시공법과 베트남 현지 관행의 차이를 확인해야 합니다.",
        "meaningVi": "Phương pháp chống thấm bằng cách dán các tấm vật liệu chống thấm lên bề mặt sàn hoặc tường để ngăn nước thấm qua. Có nhiều loại như tấm nhựa đường (asphalt), tấm cao su nhựa đường, tấm polymer tổng hợp. Phương pháp này dễ thi công, đảm bảo độ dày đồng đều, thường dùng cho mái nhà và nhà vệ sinh.",
        "context": "옥상방수, 지하실방수, 화장실방수 등 건축 방수공사 현장",
        "culturalNote": "한국에서는 시트방수가 표준화되어 있고 KS 규격(한국산업표준)에 따라 품질이 관리되지만, 베트남 건설 현장에서는 품질 편차가 큰 중국산 저가 시트가 많이 유통됩니다. 따라서 자재 스펙 확인 시 제조국과 품질 인증서를 반드시 요청해야 하며, 시공 후 접합부 검사가 특히 중요합니다. 베트남 현장에서는 'cuộn màng'(롤 형태 막)이라는 표현도 흔하게 사용됩니다.",
        "commonMistakes": [
            {
                "mistake": "màng chống thấm만 말하고 시트 타입임을 명시 안 함",
                "correction": "màng chống thấm dạng tấm 또는 tấm màng chống thấm",
                "explanation": "màng은 '막'이라는 의미로 액체 방수재(도막방수)도 포함할 수 있어서, 시트 타입임을 명확히 하려면 'tấm'(판) 또는 'cuộn'(롤)을 붙여야 함"
            },
            {
                "mistake": "시트방수를 'phương pháp chống thấm giấy'로 번역",
                "correction": "phương pháp chống thấm tấm 또는 màng chống thấm dạng tấm",
                "explanation": "'giấy'는 종이를 의미하므로 방수 시트를 종이로 오해할 수 있음. 'tấm'(판재) 또는 'màng'(막)이 정확함"
            },
            {
                "mistake": "접합부를 'chỗ nối'로만 표현",
                "correction": "mối nối (lap joint) 또는 đường nối tấm màng",
                "explanation": "'chỗ nối'는 구어적이고 모호함. 'mối nối'는 공식적인 접합부 용어이며, 도면이나 시공 지시서에서 사용"
            }
        ],
        "examples": [
            {
                "ko": "옥상 방수는 고무 아스팔트 시트방수로 시공하고, 접합부는 열풍 용접으로 처리하겠습니다.",
                "vi": "Chống thấm mái sẽ sử dụng tấm màng nhựa đường cao su, và mối nối sẽ được hàn bằng khí nóng.",
                "situation": "formal"
            },
            {
                "ko": "시트 겹침은 최소 10cm 이상 확보하고, 접합부 테스트는 육안 검사로 합니다.",
                "vi": "Phần chồng lấp tấm màng tối thiểu 10cm, và kiểm tra mối nối bằng mắt thường.",
                "situation": "onsite"
            },
            {
                "ko": "화장실 시트방수는 벽면까지 올려 붙이고, 코너 부분은 보강재를 덧대세요.",
                "vi": "Màng chống thấm nhà vệ sinh phải dán lên tường, và ở góc cần gia cố thêm lớp vật liệu.",
                "situation": "onsite"
            }
        ],
        "relatedTerms": ["도막방수", "우레탄방수", "아스팔트방수", "접합부", "열풍용접"]
    },
    {
        "slug": "phuong-phap-chong-tham-son-phu",
        "korean": "도막방수",
        "vietnamese": "Phương pháp chống thấm sơn phủ",
        "hanja": "塗膜防水",
        "hanjaReading": "도(칠할 도) + 막(막 막) + 방(막을 방) + 수(물 수)",
        "pronunciation": "도막방수",
        "meaningKo": "액체 상태의 방수재를 붓이나 롤러로 바르거나 분무하여 건조 후 막을 형성시켜 방수하는 공법입니다. 우레탄, 아크릴, 고무 아스팔트 등 다양한 재료가 있으며, 복잡한 형상이나 좁은 면적에 적합합니다. 통역 시 '도막'이라는 한자어가 생소할 수 있으므로 '액체를 발라서 막을 만든다'는 개념을 전달해야 하며, 베트남어 'sơn phủ'(도장)는 일반 페인트를 연상시킬 수 있어서 'màng chống thấm dạng lỏng'(액체형 방수막) 또는 'chống thấm bằng cách phủ lớp'처럼 풀어서 설명하는 것이 안전합니다. 시공 시 도포 횟수와 건조 시간을 명확히 전달해야 합니다.",
        "meaningVi": "Phương pháp chống thấm bằng cách phủ lớp vật liệu chống thấm dạng lỏng (urethane, acrylic, nhựa đường cao su...) lên bề mặt bằng cọ, con lăn hoặc phun. Sau khi khô, tạo thành lớp màng liền mạch. Thích hợp cho bề mặt phức tạp hoặc diện tích nhỏ.",
        "context": "옥상, 베란다, 화장실, 수조, 지하구조물 방수 시공 현장",
        "culturalNote": "한국에서는 우레탄 도막방수가 화장실과 베란다에 표준으로 사용되며, 시공 후 24~48시간 양생이 필수입니다. 베트남에서는 'sơn chống thấm'이라는 표현이 흔하지만, 일반 방수 페인트(품질 낮은 제품)와 혼동될 수 있으므로 전문 방수 도막재임을 강조해야 합니다. 베트남 현장에서는 건조 시간을 단축하려고 두껍게 한 번에 바르는 경우가 있는데, 균열 위험이 있으므로 여러 번 나눠 바르도록 지시해야 합니다.",
        "commonMistakes": [
            {
                "mistake": "도막방수를 'sơn chống thấm'으로만 번역",
                "correction": "màng chống thấm dạng lỏng 또는 lớp phủ chống thấm dạng màng",
                "explanation": "'sơn'은 일반 페인트를 연상시켜 전문 방수재가 아닌 것으로 오해받을 수 있음. 'màng'(막)을 명시해야 함"
            },
            {
                "mistake": "'도막'을 직역해서 'màng sơn'이라고 함",
                "correction": "lớp màng chống thấm (방수막 층) 또는 màng chống thấm dạng lỏng",
                "explanation": "'màng sơn'은 어색하고 베트남 현장에서 잘 안 쓰임. 'lớp màng' 또는 'dạng lỏng'(액체형)으로 설명하는 게 자연스러움"
            },
            {
                "mistake": "도포 횟수를 'lần sơn'으로 표현",
                "correction": "số lớp phủ 또는 số lần phủ màng",
                "explanation": "'lần sơn'은 일반 페인트 칠하는 느낌. 'số lớp phủ'가 전문 용어"
            }
        ],
        "examples": [
            {
                "ko": "화장실 바닥은 우레탄 도막방수 2회 도포하고, 각 층당 4시간 간격을 두세요.",
                "vi": "Sàn nhà vệ sinh phủ màng chống thấm urethane 2 lớp, mỗi lớp cách nhau 4 giờ.",
                "situation": "formal"
            },
            {
                "ko": "코너 부분은 보강포를 깔고 도막방수를 추가로 발라주세요.",
                "vi": "Ở góc, trải vải gia cố rồi phủ thêm lớp màng chống thấm.",
                "situation": "onsite"
            },
            {
                "ko": "건조 전에 비 오면 다시 해야 하니까 일기예보 확인 필수입니다.",
                "vi": "Nếu mưa trước khi khô thì phải làm lại, nên bắt buộc phải kiểm tra dự báo thời tiết.",
                "situation": "onsite"
            }
        ],
        "relatedTerms": ["우레탄방수", "시트방수", "방수층", "도포", "양생기간"]
    },
    {
        "slug": "chong-tham-urethane",
        "korean": "우레탄방수",
        "vietnamese": "Chống thấm urethane",
        "hanja": None,
        "hanjaReading": None,
        "pronunciation": "우레탄방수",
        "meaningKo": "우레탄 수지를 주성분으로 한 액체 방수재를 도포하여 막을 형성하는 방수 공법입니다. 신축성이 우수하고 균열 추종성이 좋아 화장실, 베란다, 옥상 등에 널리 사용됩니다. 1액형과 2액형이 있으며, 2액형은 주제와 경화제를 현장에서 혼합해야 합니다. 통역 시 '우레탄'은 외래어이므로 베트남어로도 'urethane' 또는 'polyurethane'으로 표기하며, 한국에서 화장실 방수의 사실상 표준임을 강조하면 이해가 빠릅니다. 베트남 현장에서는 저가 제품 사용이 많아 품질 편차가 크므로, 제조사와 혼합 비율, 도포 두께를 명확히 전달해야 합니다.",
        "meaningVi": "Phương pháp chống thấm bằng cách phủ lớp vật liệu urethane (polyurethane) dạng lỏng lên bề mặt. Có độ co giãn tốt, bám dính tốt, thường dùng cho nhà vệ sinh, ban công, mái nhà. Có dạng 1 thành phần (sẵn sàng dùng) và 2 thành phần (cần trộn chất chính và chất đóng rắn tại công trường).",
        "context": "화장실, 베란다, 욕실, 옥상 방수 시공",
        "culturalNote": "한국에서는 우레탄 방수가 화장실 방수의 90% 이상을 차지할 정도로 보편적이며, 시공 후 48시간 양생 후 방수 테스트를 실시합니다. 베트남에서는 'chống thấm PU' 또는 'chống thấm urethane'으로 불리지만, 중국산 저가 제품이 많아 품질 신뢰도가 낮은 경우가 많습니다. 한국산 또는 일본산 제품을 지정할 때는 제조사명과 제품 스펙을 명확히 전달하고, 현장 혼합 비율(2액형)과 도포 두께(보통 1.5~2mm)를 엄격히 관리해야 합니다.",
        "commonMistakes": [
            {
                "mistake": "우레탄을 'nhựa'로 번역",
                "correction": "urethane 또는 polyurethane (PU)",
                "explanation": "'nhựa'는 일반 플라스틱을 의미하므로 부정확. 'urethane'은 고유명사처럼 그대로 쓰는 게 정확"
            },
            {
                "mistake": "1액형/2액형을 '1 loại / 2 loại'로 번역",
                "correction": "1 thành phần / 2 thành phần 또는 dạng 1 bộ phận / 2 bộ phận",
                "explanation": "'loại'는 '종류'라는 뜻으로 부정확. 'thành phần'(성분) 또는 'bộ phận'(부분)이 맞음"
            },
            {
                "mistake": "경화제를 'chất làm cứng'로 표현",
                "correction": "chất đóng rắn 또는 chất xúc tác đóng rắn",
                "explanation": "'làm cứng'은 구어적. 'đóng rắn'(경화)이 전문 용어"
            }
        ],
        "examples": [
            {
                "ko": "화장실 우레탄방수는 2액형으로 하고, 주제와 경화제 혼합 비율 10:1 지켜주세요.",
                "vi": "Chống thấm urethane nhà vệ sinh dùng loại 2 thành phần, tỷ lệ trộn chất chính và chất đóng rắn là 10:1.",
                "situation": "formal"
            },
            {
                "ko": "벽면은 바닥에서 최소 30cm 올려서 발라야 물튀김 막을 수 있습니다.",
                "vi": "Tường phải phủ lên tối thiểu 30cm từ sàn để chống nước bắn.",
                "situation": "onsite"
            },
            {
                "ko": "우레탄 경화 중에는 절대 물 닿으면 안 돼요. 양생 끝날 때까지 출입 금지하세요.",
                "vi": "Khi urethane đang đóng rắn tuyệt đối không được để nước chạm vào. Cấm vào cho đến khi hoàn thành bảo dưỡng.",
                "situation": "onsite"
            }
        ],
        "relatedTerms": ["도막방수", "방수층", "경화제", "양생", "방수테스트"]
    },
    {
        "slug": "tam-cach-nhiet-xps",
        "korean": "XPS단열재",
        "vietnamese": "Tấm cách nhiệt XPS",
        "hanja": "XPS斷熱材",
        "hanjaReading": "X-P-S(외래어) + 단(끊을 단) + 열(더울 열) + 재(재료 재)",
        "pronunciation": "엑스피에스단열재",
        "meaningKo": "압출법 발포 폴리스티렌(Extruded Polystyrene)을 사용한 단열재로, 독립된 미세 기포 구조로 인해 단열 성능과 압축 강도가 우수하며 흡수율이 매우 낮습니다. 주로 건물 외단열, 지붕 단열, 바닥 단열, 냉동창고 등에 사용됩니다. 통역 시 'XPS'는 약어이므로 베트nam어로도 그대로 'XPS'로 표기하거나 'polystyrene ép đùn'(압출 폴리스티렌)으로 풀어 설명할 수 있습니다. 한국에서는 EPS(비드법)보다 XPS(압출법)를 고급 단열재로 인식하며, 가격도 약 1.5~2배 비쌉니다. 베트남 현장에서는 두께와 밀도를 명확히 지정해야 저품질 제품 납품을 방지할 수 있습니다.",
        "meaningVi": "Vật liệu cách nhiệt làm từ polystyrene ép đùn (Extruded Polystyrene), có cấu trúc bọt khí kín, hiệu suất cách nhiệt cao, độ bền nén tốt, hấp thụ nước rất thấp. Dùng cho cách nhiệt ngoài tòa nhà, mái, sàn, kho lạnh. XPS được đánh giá cao hơn EPS (polystyrene dạng hạt) về chất lượng và giá thành.",
        "context": "외단열 시공, 옥상 단열, 냉동창고, 지하 외벽 단열 현장",
        "culturalNote": "한국 건축에서는 에너지 절약 설계 기준이 강화되면서 XPS 단열재 사용이 의무화된 경우가 많으며, 두께는 보통 50mm~100mm입니다. 베트남은 열대 기후라 난방 단열보다는 냉방 단열(열 차단)이 중요하지만, 최근 고급 건물에서는 XPS 사용이 증가하고 있습니다. 베트남에서는 'tấm xốp cách nhiệt' 또는 'tấm EPS/XPS'로 통칭되는 경우가 많아, 압출법(XPS)과 비드법(EPS)의 차이를 명확히 설명해야 품질 오해를 막을 수 있습니다.",
        "commonMistakes": [
            {
                "mistake": "XPS를 'tấm xốp'로만 표현",
                "correction": "tấm cách nhiệt XPS 또는 tấm polystyrene ép đùn",
                "explanation": "'tấm xốp'(발포판)은 일반 스티로폼도 포함하므로 XPS의 고급 특성이 전달 안 됨. 'XPS' 또는 'ép đùn'(압출)을 명시해야 함"
            },
            {
                "mistake": "EPS와 XPS를 구분 없이 'xốp cách nhiệt'로 통칭",
                "correction": "XPS는 'polystyrene ép đùn', EPS는 'polystyrene dạng hạt'",
                "explanation": "두 재료는 제조법과 성능이 다르므로 혼동하면 자재 발주 오류 발생. 압출법과 비드법을 구분해야 함"
            },
            {
                "mistake": "밀도를 'độ dày'로 번역",
                "correction": "밀도는 'khối lượng riêng' 또는 'mật độ', 두께는 'độ dày'",
                "explanation": "밀도(kg/m³)와 두께(mm)는 다른 개념. 혼동하면 자재 스펙 전달 실패"
            }
        ],
        "examples": [
            {
                "ko": "외벽 단열은 XPS 75mm, 밀도 30kg/m³ 이상 제품으로 시공하세요.",
                "vi": "Cách nhiệt tường ngoài dùng tấm XPS dày 75mm, mật độ tối thiểu 30kg/m³.",
                "situation": "formal"
            },
            {
                "ko": "XPS는 물 안 먹으니까 지하 외벽에 쓰기 좋아요. EPS는 물 먹어서 안 돼요.",
                "vi": "XPS không hút nước nên tốt cho tường ngoài tầng hầm. EPS hút nước nên không được dùng.",
                "situation": "onsite"
            },
            {
                "ko": "단열재 이음부는 테이프로 밀실하게 붙여서 열교 방지하세요.",
                "vi": "Chỗ nối tấm cách nhiệt dán kín bằng băng keo để ngăn cầu nhiệt.",
                "situation": "onsite"
            }
        ],
        "relatedTerms": ["EPS단열재", "외단열", "열교차단", "압축강도", "흡수율"]
    },
    {
        "slug": "bat-cach-nhiet-thuy-tinh",
        "korean": "글라스울",
        "vietnamese": "Bông cách nhiệt thủy tinh",
        "hanja": None,
        "hanjaReading": None,
        "pronunciation": "글라스울",
        "meaningKo": "유리 섬유를 원료로 만든 솜 형태의 단열재로, 가볍고 시공이 쉬우며 불연성이라 화재 안전성이 높습니다. 주로 벽체 충진, 천장 단열, 덕트 보온에 사용되며, 롤 타입과 보드 타입이 있습니다. 통역 시 '글라스울'은 영어 'glass wool'에서 온 외래어이므로, 베트남어로는 'bông thủy tinh'(유리솜) 또는 'bông khoáng thủy tinh'(유리 광물 솜)이 정확합니다. 한국에서는 방음 효과도 있어 층간소음 방지용으로도 쓰이지만, 시공 시 보호 장비(마스크, 장갑) 착용이 필수이며 피부에 닿으면 가려움증이 생길 수 있습니다. 베트남 현장에서는 석면과 혼동하는 경우가 있으므로, 석면(amiăng)이 아닌 유리 섬유임을 명확히 해야 합니다.",
        "meaningVi": "Vật liệu cách nhiệt dạng bông làm từ sợi thủy tinh, nhẹ, dễ thi công, không cháy nên an toàn cháy cao. Dùng chủ yếu cho cách nhiệt tường, trần, ống gió. Có dạng cuộn (roll) và dạng tấm (board). Còn có tác dụng cách âm. Khi thi công phải đeo khẩu trang và găng tay vì sợi thủy tinh gây ngứa da.",
        "context": "벽체 단열, 천장 단열, 덕트 보온, 층간소음 방지 현장",
        "culturalNote": "한국에서는 글라스울이 저렴하고 시공이 쉬워서 주택과 상업 건물에 널리 사용되며, 두께는 보통 50mm~100mm입니다. 베트남에서는 'bông thủy tinh'로 불리지만, 'bông khoáng' (mineral wool, 암면)과 혼동되기 쉬우므로 '유리 섬유'임을 강조해야 합니다. 또한 베트남 일부 구형 건물에서는 석면(amiăng)을 사용한 적이 있어, 건강 우려로 인해 글라스울도 석면으로 오해받는 경우가 있으니 '석면 아님, 유리 섬유'라는 점을 분명히 전달해야 합니다. 시공 시 피부 보호 교육이 필수입니다.",
        "commonMistakes": [
            {
                "mistake": "글라스울을 'bông amiăng'(석면)으로 번역",
                "correction": "bông thủy tinh 또는 bông sợi thủy tinh (절대 amiăng 사용 금지)",
                "explanation": "석면(amiăng)은 발암물질로 사용 금지. 글라스울은 유리 섬유이므로 'thủy tinh'(유리)를 명시해야 함"
            },
            {
                "mistake": "글라스울과 암면(rockwool)을 'bông cách nhiệt'으로 통칭",
                "correction": "글라스울은 'bông thủy tinh', 암면은 'bông đá' 또는 'bông khoáng đá'",
                "explanation": "재료가 다름. 유리 섬유와 암석 섬유를 구분해야 자재 발주 오류 방지"
            },
            {
                "mistake": "롤 타입을 'dạng cuốn'으로 표현",
                "correction": "dạng cuộn (roll)",
                "explanation": "'cuốn'은 책 등을 세는 단위. 'cuộn'이 롤 형태를 나타내는 정확한 단어"
            }
        ],
        "examples": [
            {
                "ko": "벽체 단열은 글라스울 75mm 롤 타입으로 충진하고, 틈새 없이 밀실하게 시공하세요.",
                "vi": "Cách nhiệt tường dùng bông thủy tinh dạng cuộn dày 75mm, thi công kín không để khe hở.",
                "situation": "formal"
            },
            {
                "ko": "글라스울 만질 때 꼭 장갑 끼세요. 손에 닿으면 엄청 가려워요.",
                "vi": "Khi chạm bông thủy tinh nhất định phải đeo găng tay. Nếu chạm tay sẽ rất ngứa.",
                "situation": "onsite"
            },
            {
                "ko": "층간소음 줄이려면 천장에 글라스울 50mm 깔고 석고보드로 마감하면 됩니다.",
                "vi": "Để giảm tiếng ồn giữa các tầng, trải bông thủy tinh 50mm trên trần rồi ốp tấm thạch cao.",
                "situation": "onsite"
            }
        ],
        "relatedTerms": ["암면", "단열재", "방음재", "불연재료", "유리섬유"]
    },
    {
        "slug": "phong-chong-ngung-tuyen",
        "korean": "결로방지",
        "vietnamese": "Phòng chống ngưng tụ",
        "hanja": "結露防止",
        "hanjaReading": "결(맺을 결) + 로(이슬 로) + 방(막을 방) + 지(그칠 지)",
        "pronunciation": "결로방지",
        "meaningKo": "실내외 온도 차이로 인해 공기 중 수증기가 차가운 표면에 물방울로 맺히는 현상(결로)을 막는 것입니다. 단열 성능 강화, 환기, 방습층 설치, 실내 습도 조절 등의 방법을 사용합니다. 결로가 발생하면 곰팡이, 벽지 탈락, 구조체 부식 등의 문제가 생깁니다. 통역 시 '결로'라는 한자어가 생소할 수 있으므로 '공기 중 습기가 차가운 벽에 물방울로 맺히는 현象'처럼 풀어서 설명하고, 베트남어 'ngưng tụ'(응결)는 과학 용어이므로 현장에서는 'đọng nước'(물이 맺힘)라고 쉽게 표현하는 것도 좋습니다. 베트남 열대 기후에서는 냉방 시 내부 결로가 많이 발생하므로, 한국과 반대로 내단열보다 외단열이 유리합니다.",
        "meaningVi": "Ngăn ngừa hiện tượng hơi nước trong không khí ngưng tụ thành giọt nước trên bề mặt lạnh do chênh lệch nhiệt độ trong và ngoài. Nguyên nhân gây ra nấm mốc, bong tróc giấy dán tường, ăn mòn kết cấu. Giải pháp: tăng cường cách nhiệt, thông gió, lắp lớp chống ẩm, điều chỉnh độ ẩm trong phòng.",
        "context": "단열 설계, 결로 문제 해결, 곰팡이 방지, 환기 시스템 계획 시",
        "culturalNote": "한국에서는 겨울철 난방으로 인한 표면 결로(외벽 안쪽)와 내부 결로(단열재 내부)가 큰 문제이며, 이를 방지하기 위해 단열재 실내 측에 방습층(비닐 시트)을 설치합니다. 베트남은 고온 다습하여 냉방 시 외부 공기가 실내 차가운 벽에 닿아 결로가 발생하므로, 한국과 반대로 외단열이 더 효과적입니다. 베트남 현장에서는 'đọng nước'(물 맺힘)라는 표현이 더 직관적이며, 'nấm mốc'(곰팡이)와 연결 지어 설명하면 이해가 빠릅니다.",
        "commonMistakes": [
            {
                "mistake": "결로를 'nước đọng'으로 표현",
                "correction": "hiện tượng ngưng tụ 또는 ngưng tụ hơi nước (공식), đọng nước (구어)",
                "explanation": "'nước đọng'은 고인 물 전반을 의미. '결로'라는 특정 현상은 'ngưng tụ'(응결)가 정확"
            },
            {
                "mistake": "결로방지를 'chống nước đọng'로 번역",
                "correction": "phòng chống ngưng tụ 또는 ngăn ngừa ngưng tụ",
                "explanation": "'chống nước đọng'은 물이 고이는 것 방지. 결로 현상 방지는 'phòng chống ngưng tụ'가 맞음"
            },
            {
                "mistake": "방습층을 'lớp chống nước'로 번역",
                "correction": "lớp chống ẩm 또는 màng ngăn hơi (vapor barrier)",
                "explanation": "'chống nước'(방수)는 액체 물 차단. 방습은 수증기 차단이므로 'chống ẩm' 또는 'ngăn hơi'가 정확"
            }
        ],
        "examples": [
            {
                "ko": "외벽 단열재 실내 측에 방습 비닐을 깔아서 내부 결로를 방지하세요.",
                "vi": "Phía trong của tấm cách nhiệt tường ngoài trải màng nhựa chống ẩm để ngăn ngừa ngưng tụ bên trong.",
                "situation": "formal"
            },
            {
                "ko": "창틀 주변에 물방울 맺히면 그게 결로예요. 단열 보강 필요합니다.",
                "vi": "Nếu thấy giọt nước đọng quanh khung cửa sổ, đó là hiện tượng ngưng tụ. Cần gia cố cách nhiệt.",
                "situation": "onsite"
            },
            {
                "ko": "환기 자주 안 하면 습기 차서 곰팡이 생겨요. 하루 2번 이상 환기하세요.",
                "vi": "Nếu không thông gió thường xuyên sẽ ẩm và nấm mốc mọc. Phải thông gió ít nhất 2 lần mỗi ngày.",
                "situation": "onsite"
            }
        ],
        "relatedTerms": ["단열", "방습층", "환기", "곰팡이", "내부결로"]
    },
    {
        "slug": "ngan-cau-nhiet",
        "korean": "열교차단",
        "vietnamese": "Ngăn cầu nhiệt",
        "hanja": "熱橋遮斷",
        "hanjaReading": "열(더울 열) + 교(다리 교) + 차(가릴 차) + 단(끊을 단)",
        "pronunciation": "열교차단",
        "meaningKo": "열전도율이 높은 구조 부재(철근, 앵커 등)가 단열층을 관통하여 열이 빠져나가는 현상(열교)을 차단하는 것입니다. 열교가 발생하면 해당 부위의 단열 성능이 떨어지고 결로가 발생하기 쉽습니다. 단열재 연속 시공, 열교 차단재(플라스틱 앵커, 단열 브래킷) 사용, 구조 설계 단계에서 열교 최소화 등의 방법을 사용합니다. 통역 시 '열교'는 생소한 용어이므로 '열이 다리처럼 연결되어 빠져나간다'는 의미를 전달하고, 베트남어 'cầu nhiệt'(열 다리)는 직역이지만 현장에서 잘 통하므로, '열이 새는 부분'이라는 개념을 추가로 설명하면 이해가 빠릅니다.",
        "meaningVi": "Ngăn chặn hiện tượng nhiệt thoát ra qua các bộ phần kết cấu có độ dẫn nhiệt cao (cốt thép, neo, khung kim loại...) xuyên qua lớp cách nhiệt, tạo thành 'cầu nhiệt'. Nếu có cầu nhiệt, hiệu suất cách nhiệt giảm và dễ xảy ra ngưng tụ. Giải pháp: thi công liên tục lớp cách nhiệt, dùng neo nhựa, khung cách nhiệt, thiết kế kết cấu tối thiểu hóa cầu nhiệt.",
        "context": "외단열 시공, 창호 설치, 발코니 단열, 고단열 건물 설계 시",
        "culturalNote": "한국에서는 에너지 절약 설계 기준 강화로 열교 차단이 필수 항목이 되었으며, 특히 발코니 확장 시 난간 부위의 열교 차단이 중요합니다. 베트남은 냉방 중심 기후라 난방만큼 열교 문제가 심각하지 않지만, 고급 건물이나 냉동창고에서는 열교로 인한 에너지 손실과 결로 문제가 발생합니다. 베트남 현장에서는 'cầu nhiệt'라는 용어가 생소할 수 있으므로, '철근이나 금속이 단열재를 뚫고 지나가서 열이 새는 현상'이라고 쉽게 풀어 설명하는 것이 좋습니다.",
        "commonMistakes": [
            {
                "mistake": "열교를 'cầu nhiệt'로만 번역하고 설명 없이 사용",
                "correction": "cầu nhiệt (nhiệt thoát qua kết cấu kim loại) - 괄호로 설명 추가",
                "explanation": "'cầu nhiệt'는 직역이라 현장에서 생소함. '열이 새는 부분'이라는 설명을 덧붙여야 이해됨"
            },
            {
                "mistake": "열교차단을 'chống cầu nhiệt'로 번역",
                "correction": "ngăn cầu nhiệt 또는 ngăn chặn cầu nhiệt",
                "explanation": "'chống'(대항하다)보다 'ngăn'(막다, 차단하다)이 더 정확한 표현"
            },
            {
                "mistake": "열교 부위를 'chỗ rò nhiệt'로 표현",
                "correction": "vị trí cầu nhiệt 또는 điểm cầu nhiệt",
                "explanation": "'rò nhiệt'는 일반적인 열 손실. 구조 부재를 통한 특정 경로는 'cầu nhiệt'로 구분해야 함"
            }
        ],
        "examples": [
            {
                "ko": "외단열 시공 시 앵커는 플라스틱 제품 사용해서 열교 차단하세요.",
                "vi": "Khi thi công cách nhiệt ngoài, dùng neo nhựa để ngăn cầu nhiệt.",
                "situation": "formal"
            },
            {
                "ko": "발코니 난간 콘크리트가 열교 부위예요. 단열재로 연속 처리해야 합니다.",
                "vi": "Bê tông lan can ban công là điểm cầu nhiệt. Phải xử lý liên tục bằng vật liệu cách nhiệt.",
                "situation": "onsite"
            },
            {
                "ko": "창틀 주변 결로는 대부분 열교 때문입니다. 창틀 단열 보강 필요해요.",
                "vi": "Ngưng tụ quanh khung cửa sổ chủ yếu do cầu nhiệt. Cần gia cố cách nhiệt khung cửa.",
                "situation": "onsite"
            }
        ],
        "relatedTerms": ["외단열", "결로방지", "단열브래킷", "플라스틱앵커", "발코니난간"]
    },
    {
        "slug": "mang-ngan-hoi",
        "korean": "증기차단막",
        "vietnamese": "Màng ngăn hơi",
        "hanja": "蒸氣遮斷膜",
        "hanjaReading": "증(찔 증) + 기(기운 기) + 차(가릴 차) + 단(끊을 단) + 막(막 막)",
        "pronunciation": "증기차단막",
        "meaningKo": "수증기가 벽체나 지붕 단열층으로 침투하여 내부 결로를 일으키는 것을 막기 위해 설치하는 방습 필름입니다. 주로 폴리에틸렌(PE) 필름을 사용하며, 단열재의 실내 측(따뜻한 쪽)에 설치합니다. 겨울철 난방으로 실내 습도가 높을 때 수증기가 단열재 내부로 이동하여 차가운 외벽 쪽에서 결로되는 것을 방지합니다. 통역 시 '증기차단막'은 한자어가 많아 생소하므로 '수증기를 막는 비닐'처럼 쉽게 풀어 설명하고, 베트남어 'màng ngăn hơi'(증기 차단 막) 또는 'màng chống ẩm'(방습막)으로 표현합니다. 한국 기후에서는 필수이지만, 베트남 열대 기후에서는 사용 여부를 신중히 결정해야 합니다.",
        "meaningVi": "Màng nhựa (thường là polyethylene - PE) ngăn hơi nước xâm nhập vào lớp cách nhiệt tường hoặc mái, tránh ngưng tụ bên trong. Thường lắp ở phía trong (phía ấm) của lớp cách nhiệt. Trong mùa đông, khi độ ẩm trong phòng cao, hơi nước di chuyển vào lớp cách nhiệt và ngưng tụ ở phía lạnh (tường ngoài), gây hư hỏng. Màng ngăn hơi ngăn chặn điều này.",
        "context": "단열 시공, 목조주택, 철골 건물, 지붕 단열 현장",
        "culturalNote": "한국에서는 겨울 난방으로 인해 실내 습도가 높아 증기차단막 설치가 필수이며, 단열재 실내 측에 시공합니다. 반면 베트남은 고온 다습한 열대 기후로 냉방 중심이므로, 증기차단막을 외부 측에 설치하거나 아예 설치하지 않는 경우도 많습니다. 잘못 설치하면 오히려 습기를 가둬서 곰팡이를 유발할 수 있으므로, 기후 조건에 맞는 설계가 중요합니다. 베트남 현장에서는 'màng PE'(PE 필름) 또는 'màng chống ẩm'으로 표현하는 것이 일반적입니다.",
        "commonMistakes": [
            {
                "mistake": "증기차단막을 'màng chống nước'로 번역",
                "correction": "màng ngăn hơi 또는 màng chống ẩm (vapor barrier)",
                "explanation": "'chống nước'는 액체 방수. 수증기 차단은 'ngăn hơi' 또는 'chống ẩm'이 정확"
            },
            {
                "mistake": "증기차단막과 방수층을 혼동",
                "correction": "증기차단막은 'màng ngăn hơi' (수증기), 방수층은 'lớp chống thấm' (액체)",
                "explanation": "수증기와 물은 다름. 증기차단막은 방습, 방수층은 방수"
            },
            {
                "mistake": "증기차단막 위치를 '외부 측'이라고 잘못 안내",
                "correction": "한국 기후는 '실내 측', 베트남 냉방 시는 '외부 측' 또는 '설치 안 함'",
                "explanation": "기후에 따라 위치가 다름. 한국 난방 기후와 베트남 냉방 기후는 정반대"
            }
        ],
        "examples": [
            {
                "ko": "벽 단열재 안쪽에 PE 필름 증기차단막 설치하고, 이음부는 테이프로 밀실하게 붙이세요.",
                "vi": "Lắp màng ngăn hơi PE phía trong lớp cách nhiệt tường, chỗ nối dán kín bằng băng keo.",
                "situation": "formal"
            },
            {
                "ko": "증기차단막 찢어지면 습기 들어가서 단열재 못 쓰게 돼요. 조심히 다루세요.",
                "vi": "Nếu màng ngăn hơi bị rách thì ẩm sẽ vào và làm hỏng lớp cách nhiệt. Phải xử lý cẩn thận.",
                "situation": "onsite"
            },
            {
                "ko": "베트남은 냉방 기후라 증기차단막을 외부에 달거나 안 쓸 수도 있어요.",
                "vi": "Việt Nam là khí hậu điều hòa lạnh nên màng ngăn hơi có thể lắp phía ngoài hoặc không dùng.",
                "situation": "onsite"
            }
        ],
        "relatedTerms": ["결로방지", "단열재", "방습", "PE필름", "내부결로"]
    },
    {
        "slug": "cach-nhiet-ben-ngoai",
        "korean": "외단열",
        "vietnamese": "Cách nhiệt bên ngoài",
        "hanja": "外斷熱",
        "hanjaReading": "외(바깥 외) + 단(끊을 단) + 열(더울 열)",
        "pronunciation": "외단열",
        "meaningKo": "건물 외벽의 바깥쪽에 단열재를 설치하는 공법으로, 구조체(콘크리트, 벽돌)를 실내 온도와 같게 유지하여 축열 효과가 크고 열교 발생을 최소화할 수 있습니다. 결로 방지에도 유리하며, 건물 전체를 단열재로 감싸므로 에너지 효율이 높습니다. 반면 시공비가 비싸고 외관 마감이 제한적입니다. 통역 시 '외단열'은 문자 그대로 '외부 단열'이므로 베트남어 'cách nhiệt bên ngoài'가 직관적이지만, 현장에서는 'cách nhiệt mặt ngoài tường'(외벽 외부 단열)처럼 구체적으로 표현하는 것이 오해를 줄입니다. 내단열과의 차이를 명확히 설명해야 합니다.",
        "meaningVi": "Phương pháp lắp đặt vật liệu cách nhiệt ở phía ngoài tường bên ngoài của tòa nhà. Kết cấu (bê tông, gạch) giữ nhiệt độ gần với trong nhà, có hiệu ứng tích nhiệt lớn, giảm thiểu cầu nhiệt, ngăn ngừa ngưng tụ tốt. Hiệu suất năng lượng cao vì bao bọc toàn bộ tòa nhà. Nhược điểm: chi phí thi công cao, hạn chế về hoàn thiện mặt ngoài.",
        "context": "고단열 건물, 리모델링, 에너지 절약 설계, 공동주택 외벽 개보수",
        "culturalNote": "한국에서는 에너지 절약 설계 기준 강화로 외단열이 표준화되고 있으며, 특히 공동주택 리모델링 시 외단열 시공이 의무화되는 경우가 많습니다. 베트남은 열대 기후라 난방보다 냉방이 중요하므로, 외단열은 태양열 차단과 실내 냉기 유지에 효과적입니다. 베트남 현장에서는 'cách nhiệt ngoài' 또는 'EIFS' (External Insulation Finishing System)라는 약어를 쓰기도 하며, 외벽 마감재(스터코, 타일)와의 호환성을 고려해야 합니다.",
        "commonMistakes": [
            {
                "mistake": "외단열을 'cách nhiệt ngoài trời'로 번역",
                "correction": "cách nhiệt bên ngoài 또는 cách nhiệt mặt ngoài",
                "explanation": "'ngoài trời'는 '야외'라는 뜻. 외단열은 '외벽 바깥쪽'이므로 'bên ngoài' 또는 'mặt ngoài'"
            },
            {
                "mistake": "외단열과 내단열을 혼동",
                "correction": "외단열은 'bên ngoài tường', 내단열은 'bên trong tường'",
                "explanation": "위치가 정반대. 외단열은 구조체 바깥, 내단열은 구조체 안쪽"
            },
            {
                "mistake": "외단열 시스템을 '단열재만' 지칭",
                "correction": "외단열은 '단열재 + 마감재 + 고정재'를 포함하는 시스템",
                "explanation": "외단열은 재료가 아닌 시스템. 단열재, 접착제, 앵커, 마감재가 모두 포함"
            }
        ],
        "examples": [
            {
                "ko": "이 건물은 외단열 시스템으로 XPS 100mm 시공하고, 스터코 마감 예정입니다.",
                "vi": "Tòa nhà này sẽ thi công hệ thống cách nhiệt bên ngoài bằng XPS 100mm, hoàn thiện stucco.",
                "situation": "formal"
            },
            {
                "ko": "외단열은 건물 전체를 감싸서 열교가 거의 없고, 결로도 안 생깁니다.",
                "vi": "Cách nhiệt bên ngoài bao bọc toàn bộ tòa nhà nên hầu như không có cầu nhiệt và không bị ngưng tụ.",
                "situation": "onsite"
            },
            {
                "ko": "외단열이 내단열보다 비싸지만, 장기적으로 에너지 절약 효과가 훨씬 큽니다.",
                "vi": "Cách nhiệt bên ngoài đắt hơn cách nhiệt bên trong, nhưng hiệu quả tiết kiệm năng lượng lâu dài lớn hơn nhiều.",
                "situation": "formal"
            }
        ],
        "relatedTerms": ["내단열", "XPS단열재", "열교차단", "결로방지", "EIFS"]
    },
    {
        "slug": "cach-nhiet-ben-trong",
        "korean": "내단열",
        "vietnamese": "Cách nhiệt bên trong",
        "hanja": "內斷熱",
        "hanjaReading": "내(안 내) + 단(끊을 단) + 열(더울 열)",
        "pronunciation": "내단열",
        "meaningKo": "건물 내벽의 안쪽(실내 측)에 단열재를 설치하는 공법으로, 시공이 간단하고 비용이 저렴하지만, 구조체가 외기 온도에 노출되어 열교 발생이 쉽고 결로 위험이 높습니다. 또한 실내 공간이 줄어들고 축열 효과가 없어 에너지 효율이 낮습니다. 주로 기존 건물 리모델링이나 저예산 공사에서 사용됩니다. 통역 시 '내단열'은 '내부 단열'이므로 베트남어 'cách nhiệt bên trong'으로 표현하며, 외단열과의 장단점 비교를 명확히 전달해야 합니다. 베트남에서는 시공 편의성과 비용 때문에 내단열이 많이 사용되지만, 결로 문제가 발생할 수 있습니다.",
        "meaningVi": "Phương pháp lắp đặt vật liệu cách nhiệt ở phía trong (phía phòng) của tường bên trong. Thi công đơn giản, chi phí thấp, nhưng kết cấu tiếp xúc với nhiệt độ bên ngoài nên dễ xảy ra cầu nhiệt và ngưng tụ. Diện tích phòng giảm, không có hiệu ứng tích nhiệt, hiệu suất năng lượng thấp. Thường dùng cho cải tạo tòa nhà cũ hoặc công trình ngân sách thấp.",
        "context": "리모델링, 저비용 단열 공사, 부분 단열 보강 현장",
        "culturalNote": "한국에서는 내단열이 과거에 많이 사용되었지만, 현재는 에너지 효율과 결로 문제로 외단열로 전환되는 추세입니다. 베트남에서는 시공 편의성과 저비용으로 내단열이 여전히 많이 사용되며, 'cách nhiệt trong' 또는 'cách nhiệt phía trong'으로 불립니다. 내단열 시공 시 증기차단막 설치가 중요하지만, 베트남 열대 기후에서는 오히려 습기를 가둘 수 있으므로 전문가와 상담이 필요합니다. 베트남 현장에서는 내단열 후 곰팡이 발생 사례가 많으므로, 환기 계획을 함께 전달해야 합니다.",
        "commonMistakes": [
            {
                "mistake": "내단열을 'cách nhiệt trong nhà'로 번역",
                "correction": "cách nhiệt bên trong 또는 cách nhiệt mặt trong tường",
                "explanation": "'trong nhà'는 '집 안'이라는 뜻. 내단열은 '벽 안쪽'이므로 'bên trong' 또는 'mặt trong'"
            },
            {
                "mistake": "내단열이 외단열보다 좋다고 설명",
                "correction": "내단열은 시공 쉽지만 결로 위험, 외단열은 비싸지만 에너지 효율 높음",
                "explanation": "각각 장단점이 있음. 내단열이 무조건 좋거나 나쁜 게 아님"
            },
            {
                "mistake": "내단열 시공 시 방습층 생략",
                "correction": "내단열은 결로 위험 높으므로 방습층 필수 (단, 베트남 기후는 예외)",
                "explanation": "내단열은 구조체가 차가워 결로 위험. 방습층 없으면 곰팡이 발생"
            }
        ],
        "examples": [
            {
                "ko": "예산 부족해서 내단열로 하되, 결로 방지용 증기차단막은 꼭 설치하세요.",
                "vi": "Do thiếu ngân sách nên dùng cách nhiệt bên trong, nhưng bắt buộc phải lắp màng ngăn hơi chống ngưng tụ.",
                "situation": "formal"
            },
            {
                "ko": "내단열은 벽 안쪽에 붙여서 시공 쉬운데, 방 크기가 좀 줄어듭니다.",
                "vi": "Cách nhiệt bên trong dán phía trong tường nên thi công dễ, nhưng diện tích phòng giảm một chút.",
                "situation": "onsite"
            },
            {
                "ko": "내단열 시공 후 환기 안 하면 곰팡이 생기기 쉬우니 환기 자주 하세요.",
                "vi": "Sau khi thi công cách nhiệt bên trong, nếu không thông gió dễ mọc nấm mốc nên phải thông gió thường xuyên.",
                "situation": "onsite"
            }
        ],
        "relatedTerms": ["외단열", "결로방지", "증기차단막", "글라스울", "곰팡이"]
    }
]

# 중복 제거 및 추가
filtered = [term for term in new_terms if term['slug'] not in existing_slugs]
data.extend(filtered)

# 저장
with open(file_path, 'w', encoding='utf-8') as f:
    json.dump(data, f, ensure_ascii=False, indent=2)

print(f"Added {len(filtered)} terms. Total: {len(data)}")
