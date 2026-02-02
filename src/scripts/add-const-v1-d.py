import json
import os

# 파일 경로 설정
file_path = os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', 'data', 'terms', 'construction.json')

# 기존 데이터 로드
with open(file_path, 'r', encoding='utf-8') as f:
    data = json.load(f)

# 기존 slug 수집
existing_slugs = {t['slug'] for t in data}

# 신규 용어 10개 (설비공사/MEP)
new_terms = [
    {
        "slug": "tu-phan-phoi-dien",
        "korean": "분전반",
        "vietnamese": "Tủ phân phối điện",
        "hanja": "分電盤",
        "hanjaReading": "分(나눌 분) + 電(전기 전) + 盤(소반 반)",
        "pronunciation": "분전반",
        "meaningKo": "전기를 여러 회로로 나누어 배분하고 각 회로를 보호하는 차단기와 계측기를 수납한 함체. 통역 시 주의: 베트남에서는 브레이커함(tủ cầu dao)과 혼동되기 쉬우나, 분전반은 더 큰 개념으로 전체 전기 분배 시스템을 포함함. 현장에서는 '메인 패널'이라는 영어 표현도 자주 사용되므로 문맥에 따라 구분 필요. 베트남 현장에서는 크기와 용량을 구체적으로 명시해야 오해가 없음.",
        "meaningVi": "Tủ chứa các thiết bị phân chia và phân phối điện năng đến các mạch khác nhau, bao gồm cầu dao, CB và đồng hồ đo. Là trung tâm điều khiển hệ thống điện của công trình. Phân biệt với tủ cầu dao đơn thuần chỉ chứa CB.",
        "context": "전기설비 공사, MEP 설계, 안전관리",
        "culturalNote": "한국에서는 분전반을 아파트나 건물 각 층에 설치하는 것이 일반적이나, 베트남에서는 상대적으로 집중화된 배전 시스템을 선호하는 경향이 있음. 또한 베트남 전기 규정(TCVN)에 따른 접지 방식과 한국의 KEC 기준이 다르므로 통역 시 규격 차이를 명확히 해야 함. 베트남 현장에서는 중국산과 유럽산 분전반이 혼재되어 사용됨.",
        "commonMistakes": [
            {
                "mistake": "분전반을 'hộp điện'으로 번역",
                "correction": "Tủ phân phối điện",
                "explanation": "hộp điện은 단순 전기 박스를 의미하며, 분전반의 기능과 규모를 제대로 표현하지 못함"
            },
            {
                "mistake": "차단기함과 분전반을 동일하게 번역",
                "correction": "차단기함: Tủ cầu dao / 분전반: Tủ phân phối điện",
                "explanation": "분전반은 차단기함을 포함하는 더 넓은 개념"
            },
            {
                "mistake": "규격 설명 없이 분전반만 언급",
                "correction": "전압, 암페어, 회로 수 함께 명시",
                "explanation": "베트남 현장에서는 구체적 사양 없이는 자재 발주가 불가능"
            }
        ],
        "examples": [
            {
                "ko": "3층 복도에 분전반 설치 위치를 확인해 주세요.",
                "vi": "Vui lòng xác nhận vị trí lắp đặt tủ phân phối điện ở hành lang tầng 3.",
                "situation": "onsite"
            },
            {
                "ko": "분전반 내부 배선 작업이 완료되었습니다.",
                "vi": "Công tác đấu nối dây điện bên trong tủ phân phối đã hoàn thành.",
                "situation": "formal"
            },
            {
                "ko": "분전반에서 이상한 소리가 나는데 점검 좀 해주세요.",
                "vi": "Có tiếng lạ từ tủ phân phối điện, anh kiểm tra giúp em.",
                "situation": "informal"
            }
        ],
        "relatedTerms": ["차단기", "배선", "접지", "누전차단기"]
    },
    {
        "slug": "cau-dao-tu-dong",
        "korean": "차단기",
        "vietnamese": "Cầu dao tự động",
        "hanja": "遮斷器",
        "hanjaReading": "遮(가릴 차) + 斷(끊을 단) + 器(그릇 기)",
        "pronunciation": "차단기",
        "meaningKo": "전기 회로에 과전류나 단락이 발생했을 때 자동으로 전원을 차단하여 회로와 기기를 보호하는 장치. 통역 시 주의: 베트남에서는 CB(Circuit Breaker)라는 영어 약자를 그대로 사용하는 경우가 많으며, 용량에 따라 MCB(소형), MCCB(중형), ACB(대형)로 구분됨. 한국에서는 '누전차단기'와 '과전류차단기'를 구분하지만, 베트nam 현장에서는 이를 명확히 구분하지 않는 경우가 많아 통역 시 정확한 종류를 확인해야 함.",
        "meaningVi": "Thiết bị tự động ngắt mạch điện khi có quá tải hoặc ngắn mạch để bảo vệ hệ thống và thiết bị. Thường gọi tắt là CB. Phân loại theo dung lượng: MCB (nhỏ, dưới 100A), MCCB (trung bình, 100-1000A), ACB (lớn, trên 1000A).",
        "context": "전기설비, 안전장치, 보호설비",
        "culturalNote": "한국에서는 누전차단기 설치가 법적으로 강제되어 있으나, 베트남에서는 상대적으로 규제가 느슨하여 일반 차단기만 사용하는 경우가 많음. 베트남 현장에서 '안전'을 강조할 때는 한국 기준을 설명하며 누전차단기의 중요성을 강조해야 함. 또한 베트남에서는 중국산 저가 차단기 사용이 흔하므로 품질 문제가 자주 발생함.",
        "commonMistakes": [
            {
                "mistake": "차단기를 'công tắc điện'으로 번역",
                "correction": "Cầu dao tự động 또는 CB",
                "explanation": "công tắc điện은 일반 전등 스위치를 의미하며, 보호 기능이 없음"
            },
            {
                "mistake": "모든 차단기를 동일하게 번역",
                "correction": "누전차단기: ELCB/RCCB, 과전류차단기: MCB/MCCB",
                "explanation": "종류에 따라 베트남어 표현과 약자가 다름"
            },
            {
                "mistake": "암페어(A) 용량 언급 없이 차단기만 지칭",
                "correction": "반드시 정격전류 명시 (예: CB 63A)",
                "explanation": "베트남 현장에서는 용량 없이는 어떤 차단기인지 파악 불가"
            }
        ],
        "examples": [
            {
                "ko": "메인 차단기가 자꾸 내려가는데 원인을 찾아야 합니다.",
                "vi": "CB chính cứ bị nhảy, cần tìm nguyên nhân.",
                "situation": "onsite"
            },
            {
                "ko": "각 회로마다 20A 차단기를 설치하겠습니다.",
                "vi": "Mỗi mạch sẽ lắp CB 20A.",
                "situation": "formal"
            },
            {
                "ko": "차단기 올려도 돼? 작업 끝났어.",
                "vi": "Đóng CB lại được chưa? Làm xong rồi.",
                "situation": "informal"
            }
        ],
        "relatedTerms": ["분전반", "누전차단기", "과전류", "전기안전"]
    },
    {
        "slug": "ong-dan-nuoc",
        "korean": "배관",
        "vietnamese": "Ống dẫn nước",
        "hanja": "配管",
        "hanjaReading": "配(나눌 배) + 管(대롱 관)",
        "pronunciation": "배관",
        "meaningKo": "물이나 가스 등의 유체를 이동시키기 위해 설치하는 관(파이프) 시스템. 통역 시 주의: 베트남에서는 용도에 따라 ống nước(급수), ống thoát nước(배수), ống gas(가스), ống điều hòa(에어컨 냉매)로 명확히 구분하여 사용함. 한국에서 포괄적으로 '배관'이라고 하는 것과 달리, 베트남 현장에서는 구체적인 종류를 명시하지 않으면 의사소통에 혼란이 생김. 또한 재질(PVC, PPR, thép không gỉ)과 직경(phi)을 반드시 함께 언급해야 함.",
        "meaningVi": "Hệ thống ống dẫn để vận chuyển chất lỏng hoặc khí. Phân loại theo công dụng: cấp nước sạch, thoát nước thải, gas, điều hòa không khí. Vật liệu phổ biến: PVC, PPR, thép mạ kẽm, inox (thép không gỉ).",
        "context": "설비공사, 위생설비, MEP",
        "culturalNote": "한국에서는 동관(đồng)을 고급 배관재로 인식하지만, 베트남에서는 가격이 비싸 주로 PPR이나 PVC를 사용함. 베트남의 수압이 한국보다 낮은 경우가 많아 펌프 설치가 필수적이며, 배관 설계 시 이를 고려해야 함. 또한 베트남 남부는 염도가 높은 지하수가 많아 부식 방지를 위한 재질 선택이 중요함.",
        "commonMistakes": [
            {
                "mistake": "배관을 'ống'으로만 번역",
                "correction": "용도를 명시 (예: ống cấp nước)",
                "explanation": "ống은 너무 포괄적이며, 현장에서는 구체적 종류가 필요"
            },
            {
                "mistake": "배관 크기를 인치로만 언급",
                "correction": "phi(직경) 단위 병행 사용 (예: phi 27, phi 34)",
                "explanation": "베트남에서는 밀리미터 기준의 phi를 주로 사용"
            },
            {
                "mistake": "급수와 배수 배관을 구분하지 않음",
                "correction": "cấp nước(급수) / thoát nước(배수) 명확히 구분",
                "explanation": "설치 위치와 기울기, 재질이 완전히 다름"
            }
        ],
        "examples": [
            {
                "ko": "욕실 배관 작업은 언제 시작하나요?",
                "vi": "Khi nào bắt đầu thi công hệ thống ống nước phòng tắm?",
                "situation": "formal"
            },
            {
                "ko": "이 배관 phi 34 맞죠? 확인 좀 해주세요.",
                "vi": "Ống này phi 34 đúng không? Kiểm tra giúp anh.",
                "situation": "onsite"
            },
            {
                "ko": "배관 새는데 어디 터진 거야?",
                "vi": "Ống nước bị chảy, chỗ nào vỡ vậy?",
                "situation": "informal"
            }
        ],
        "relatedTerms": ["급수", "배수", "위생설비", "밸브"]
    },
    {
        "slug": "ong-gio",
        "korean": "덕트",
        "vietnamese": "Ống gió",
        "hanja": None,
        "hanjaReading": None,
        "pronunciation": "덕트",
        "meaningKo": "공조 시스템에서 공기를 운반하는 관. 주로 냉난방 공기를 각 공간으로 분배하거나 배기를 위해 사용됨. 통역 시 주의: 베트남에서는 'ống gió'라는 직관적인 표현을 사용하며, 한국처럼 '덕트'라는 외래어를 사용하지 않음. 재질에 따라 ống gió tôn(철판 덕트), ống gió mềm(연성 덕트)로 구분하며, 단열 여부에 따라 có cách nhiệt/không cách nhiệt로 구분함. 베트남 현장에서는 크기를 폭×높이(mm)로 표현하므로 도면 해석 시 주의 필요.",
        "meaningVi": "Hệ thống ống dẫn khí dùng trong hệ thống điều hòa không khí và thông gió. Phân loại: ống gió tôn (tấm kim loại), ống gió mềm (mềm dẻo), ống gió vải. Chức năng: dẫn khí lạnh, nóng hoặc hút khói, thông gió.",
        "context": "공조설비, 환기시스템, MEP",
        "culturalNote": "한국에서는 사각 덕트를 주로 사용하지만, 베트남에서는 시공 편의상 원형 플렉시블 덕트 사용 비율이 높음. 베트남의 고온다습한 기후로 인해 덕트 내부 결로 문제가 빈번하므로 단열재 시공이 필수적임. 또한 베트남 소방법에서 방화댐퍼(van chống cháy) 설치 기준이 까다로우므로 설계 시 반드시 확인해야 함.",
        "commonMistakes": [
            {
                "mistake": "덕트를 'ống'으로만 번역",
                "correction": "Ống gió (공조용임을 명시)",
                "explanation": "ống만 사용하면 배관과 혼동됨"
            },
            {
                "mistake": "사각덕트/원형덕트 구분 없이 통역",
                "correction": "ống gió vuông(사각) / ống gió tròn(원형)",
                "explanation": "시공 방법과 자재가 완전히 다름"
            },
            {
                "mistake": "단열 여부를 언급하지 않음",
                "correction": "có cách nhiệt(단열) 여부 명시",
                "explanation": "베트남 기후상 단열은 필수 사양"
            }
        ],
        "examples": [
            {
                "ko": "천장 안에 덕트 배관 작업 완료했습니다.",
                "vi": "Đã hoàn thành lắp đặt ống gió trong trần.",
                "situation": "formal"
            },
            {
                "ko": "이 덕트 단열 제대로 안 돼 있는데요?",
                "vi": "Ống gió này cách nhiệt không đúng kỹ thuật?",
                "situation": "onsite"
            },
            {
                "ko": "덕트 소리 너무 시끄러운데 뭐 문제 있나?",
                "vi": "Ống gió ồn quá, có vấn đề gì không?",
                "situation": "informal"
            }
        ],
        "relatedTerms": ["공조설비", "환기", "에어컨", "방화댐퍼"]
    },
    {
        "slug": "he-thong-phun-nuoc-chua-chay",
        "korean": "스프링클러",
        "vietnamese": "Hệ thống phun nước chữa cháy",
        "hanja": None,
        "hanjaReading": None,
        "pronunciation": "스프링클러",
        "meaningKo": "화재 발생 시 자동으로 물을 분사하여 진화하는 소화설비. 천장에 설치되며 일정 온도 이상이 되면 스프링클러 헤드가 열리면서 물이 분사됨. 통역 시 주의: 베트남에서는 'hệ thống phun nước'라는 정식 명칭과 함께 영어 'sprinkler'를 병행 사용함. 베트남 소방법(PCCC - Phòng Cháy Chữa Cháy)에 따라 건물 규모와 용도에 따라 설치 의무가 다르며, 한국의 소방법과 기준이 다르므로 설계 시 현지 규정을 반드시 확인해야 함. 수압과 유량 기준도 다름.",
        "meaningVi": "Hệ thống chữa cháy tự động bằng cách phun nước khi phát hiện nhiệt độ cao. Bao gồm: đầu phun (sprinkler head), ống dẫn, van, bơm nước. Theo quy định PCCC Việt Nam, bắt buộc với các công trình cao tầng, trung tâm thương mại, nhà máy.",
        "context": "소방설비, 안전시설, MEP",
        "culturalNote": "한국에서는 습식 스프링클러가 일반적이나, 베트남에서는 예산 절감을 위해 건식(dry) 시스템 선호도가 높음. 베트남의 수압이 불안정한 지역이 많아 별도의 소화펌프와 물탱크 설치가 필수적임. 또한 베트남 소방당국(Cảnh sát PCCC)의 검수가 까다로우므로 시공 중 수시로 소방서와 협의해야 함. 한국과 달리 베트남에서는 스프링클러 오작동 시 배상 책임 기준이 모호함.",
        "commonMistakes": [
            {
                "mistake": "스프링클러를 'vòi phun nước'로 번역",
                "correction": "Hệ thống phun nước chữa cháy 또는 sprinkler",
                "explanation": "vòi phun nước는 일반 호스를 의미하며, 자동 소화 시스템의 의미가 없음"
            },
            {
                "mistake": "헤드 개수만 언급하고 유량 미명시",
                "correction": "헤드 수 + 유량(l/min) + 수압(bar) 함께 전달",
                "explanation": "베트남 소방 검수 시 필수 확인 항목"
            },
            {
                "mistake": "소화전과 스프링클러를 혼동",
                "correction": "소화전: Họng lấy nước chữa cháy / 스프링클러: Sprinkler",
                "explanation": "용도와 작동 방식이 완전히 다른 별개의 소방설비"
            }
        ],
        "examples": [
            {
                "ko": "각 층에 스프링클러 헤드 40개씩 설치 예정입니다.",
                "vi": "Dự kiến lắp 40 đầu phun sprinkler mỗi tầng.",
                "situation": "formal"
            },
            {
                "ko": "스프링클러 시험 배관 압력 확인 부탁드립니다.",
                "vi": "Kiểm tra áp lực đường ống hệ thống sprinkler khi test.",
                "situation": "onsite"
            },
            {
                "ko": "이거 스프링클러 터지면 물 엄청 나오는 거지?",
                "vi": "Cái này sprinkler nổ ra thì nước xả ầm ầm phải không?",
                "situation": "informal"
            }
        ],
        "relatedTerms": ["소화전", "소방펌프", "화재감지기", "PCCC"]
    },
    {
        "slug": "trong-cuu-hoa",
        "korean": "소화전",
        "vietnamese": "Trọng cứu hỏa",
        "hanja": "消火栓",
        "hanjaReading": "消(사라질 소) + 火(불 화) + 栓(마개 전)",
        "pronunciation": "소화전",
        "meaningKo": "화재 발생 시 소방호스를 연결하여 수동으로 물을 뿌려 진화하는 소방설비. 실내소화전과 옥외소화전으로 구분됨. 통역 시 주의: 베트남에서는 공식 명칭이 'trọng cứu hỏa'이지만 현장에서는 'họng lấy nước chữa cháy' 또는 'tủ chữa cháy'(소화전함)라는 표현을 더 많이 사용함. 베트남 소방법에서는 계단실 또는 복도에 일정 간격마다 설치를 의무화하고 있으며, 한국과 달리 호스 길이 기준(통상 30m)이 다름. 수압 기준도 베트남이 낮은 편임.",
        "meaningVi": "Thiết bị chữa cháy thủ công bằng cách nối vòi và phun nước trực tiếp. Gồm: vòi nước, họng lấy nước, cuộn ống (vòi chữa cháy). Phân loại: trong nhà (indoor) và ngoài trời (outdoor hydrant). Theo quy định PCCC, đặt cách nhau 25-30m ở hành lang, cầu thang.",
        "context": "소방설비, 안전시설, 비상대응",
        "culturalNote": "한국에서는 소화전함 내부에 소화기를 함께 비치하는 경우가 많지만, 베트남에서는 분리 설치가 일반적임. 베트남 건설 현장에서는 소화전 호스의 품질이 낮아 누수나 파손이 빈번하므로 정기 점검이 중요함. 또한 베트남에서는 소화전 사용 훈련이 부족하여 실제 화재 시 제대로 활용되지 못하는 경우가 많아, 시공 후 사용법 교육을 권장해야 함.",
        "commonMistakes": [
            {
                "mistake": "소화전을 'bình chữa cháy'로 번역",
                "correction": "Trọng cứu hỏa 또는 họng lấy nước chữa cháy",
                "explanation": "bình chữa cháy는 소화기를 의미하며, 소화전과는 완전히 다른 장비"
            },
            {
                "mistake": "소화전함과 소화전을 구분하지 않음",
                "correction": "소화전: họng lấy nước / 소화전함: tủ chữa cháy",
                "explanation": "함은 소화전을 보관하는 외부 케이스"
            },
            {
                "mistake": "실내/옥외 구분 없이 통역",
                "correction": "실내: trong nhà / 옥외: ngoài trời (hydrant)",
                "explanation": "설치 위치와 규격, 수압 요구사항이 다름"
            }
        ],
        "examples": [
            {
                "ko": "각 층 계단실에 소화전함 설치 완료했습니다.",
                "vi": "Đã lắp đặt xong tủ chữa cháy ở cầu thang mỗi tầng.",
                "situation": "formal"
            },
            {
                "ko": "소화전 호스 길이가 규정에 맞는지 확인해 주세요.",
                "vi": "Kiểm tra chiều dài vòi chữa cháy có đúng quy định không.",
                "situation": "onsite"
            },
            {
                "ko": "화재 나면 저 빨간 박스 열고 호스 꺼내는 거야.",
                "vi": "Cháy thì mở hộp đỏ kia lấy vòi ra xài.",
                "situation": "informal"
            }
        ],
        "relatedTerms": ["스프링클러", "소화기", "소방펌프", "비상대응"]
    },
    {
        "slug": "he-thong-bao-chay",
        "korean": "자동화재탐지설비",
        "vietnamese": "Hệ thống báo cháy",
        "hanja": "自動火災探知設備",
        "hanjaReading": "自(스스로 자) + 動(움직일 동) + 火(불 화) + 災(재앙 재) + 探(찾을 탐) + 知(알 지) + 設(베풀 설) + 備(갖출 비)",
        "pronunciation": "자동화재탐지설비",
        "meaningKo": "화재 발생 시 연기, 열, 불꽃 등을 자동으로 감지하여 경보를 울리고 관계자에게 알리는 시스템. 감지기(detector), 수신기(control panel), 발신기(manual call point), 경종(bell)으로 구성됨. 통역 시 주의: 베트남에서는 'hệ thống báo cháy' 또는 'Fire Alarm System(FAS)'라는 영어 약자를 혼용함. 한국에서는 연기감지기를 주로 사용하지만, 베트남에서는 열감지기 사용 비율이 높음. 베트남 소방법상 중앙감시실(phòng giám sát trung tâm) 설치 의무가 있는 건물이 많으므로 확인 필요.",
        "meaningVi": "Hệ thống phát hiện và cảnh báo cháy tự động thông qua cảm biến khói, nhiệt, lửa. Bao gồm: đầu báo khói/nhiệt (detector), tủ trung tâm (control panel), nút bấm khẩn cấp (manual call point), chuông/còi báo (bell/siren). Kết nối với hệ thống giám sát trung tâm.",
        "context": "소방설비, 안전시스템, 빌딩자동화",
        "culturalNote": "한국에서는 아날로그 방식과 디지털 방식 화재탐지설비를 모두 사용하지만, 베트남에서는 예산 문제로 기존 아날로그 방식(conventional)이 여전히 주류임. 베트남 소방당국 검수 시 감지기 작동 테스트가 매우 엄격하므로 사전 점검이 필수적임. 또한 베트남에서는 오작동(báo giả)으로 인한 민원이 많아 감지기 위치 선정이 중요함.",
        "commonMistakes": [
            {
                "mistake": "자동화재탐지설비를 '화재경보기'로 축약 번역",
                "correction": "Hệ thống báo cháy tự động (전체 시스템 명시)",
                "explanation": "베트남에서는 시스템 전체를 의미하므로 축약 표현은 오해 발생"
            },
            {
                "mistake": "연기감지기와 열감지기를 구분하지 않음",
                "correction": "đầu báo khói(연기) / đầu báo nhiệt(열)",
                "explanation": "설치 위치와 용도가 다르므로 반드시 구분"
            },
            {
                "mistake": "수신기를 단순 'máy'로 번역",
                "correction": "Tủ trung tâm báo cháy 또는 control panel",
                "explanation": "소방시스템의 핵심 장비이므로 정확한 명칭 필요"
            }
        ],
        "examples": [
            {
                "ko": "전 층에 자동화재탐지설비 설치 및 연동 테스트 완료했습니다.",
                "vi": "Đã hoàn thành lắp đặt và test liên động hệ thống báo cháy toàn bộ tòa nhà.",
                "situation": "formal"
            },
            {
                "ko": "복도 천장에 연기감지기 10m 간격으로 달아주세요.",
                "vi": "Lắp đầu báo khói ở trần hành lang, cách nhau 10m.",
                "situation": "onsite"
            },
            {
                "ko": "화재경보 울리는데 어디서 난 거야?",
                "vi": "Chuông báo cháy reo, chỗ nào vậy?",
                "situation": "informal"
            }
        ],
        "relatedTerms": ["연기감지기", "열감지기", "소방설비", "PCCC"]
    },
    {
        "slug": "chuong-cua",
        "korean": "인터폰",
        "vietnamese": "Chuông cửa",
        "hanja": None,
        "hanjaReading": None,
        "pronunciation": "인터폰",
        "meaningKo": "건물이나 주택의 출입구에 설치하여 방문자와 내부 거주자가 음성 또는 영상으로 소통하고 원격으로 문을 열 수 있는 통신설비. 통역 시 주의: 베트남에서는 'chuông cửa'(초인종)라는 표현이 가장 일반적이며, 영상 인터폰은 'chuông hình' 또는 'video door phone'이라고 함. 한국처럼 '인터폰'이라는 외래어는 사용하지 않음. 베트남에서는 아파트 단지 차원의 통합 인터폰 시스템보다는 각 세대별 독립형 인터폰이 주류임. 최근 스마트홈과 연동되는 IP 인터폰 수요가 증가 중임.",
        "meaningVi": "Thiết bị liên lạc giữa cổng/cửa và bên trong nhà, cho phép nghe/nhìn khách và mở cửa từ xa. Phân loại: chuông cửa âm thanh (audio), chuông hình (video). Hiện nay phổ biến loại kết nối IP, có thể xem qua smartphone.",
        "context": "약전설비, 보안시스템, 스마트홈",
        "culturalNote": "한국에서는 아파트에 월패드(home automation panel)와 통합된 인터폰이 표준이지만, 베트남에서는 독립형 인터폰이 대부분이며 월패드 개념이 생소함. 베트남에서는 도난 방지를 위해 카메라 기능이 있는 인터폰 선호도가 매우 높음. 또한 베트남의 불안정한 인터넷 환경으로 인해 IP 인터폰 설치 시 네트워크 안정성 확보가 중요함.",
        "commonMistakes": [
            {
                "mistake": "인터폰을 'điện thoại cửa'로 번역",
                "correction": "Chuông cửa 또는 video door phone",
                "explanation": "điện thoại cửa는 부자연스러운 표현이며 현장에서 사용되지 않음"
            },
            {
                "mistake": "영상/음성 인터폰 구분 없이 통역",
                "correction": "chuông cửa âm thanh(음성) / chuông hình(영상)",
                "explanation": "가격과 기능이 다르므로 구분 필수"
            },
            {
                "mistake": "월패드와 인터폰을 동일하게 번역",
                "correction": "인터폰: chuông cửa / 월패드: bảng điều khiển nhà thông minh",
                "explanation": "베트남에서는 별개의 장비로 인식됨"
            }
        ],
        "examples": [
            {
                "ko": "각 세대 현관에 영상 인터폰 설치 예정입니다.",
                "vi": "Dự kiến lắp chuông hình ở cửa ra vào mỗi căn hộ.",
                "situation": "formal"
            },
            {
                "ko": "인터폰으로 문 열어주세요.",
                "vi": "Mở cửa qua chuông cửa giúp anh.",
                "situation": "onsite"
            },
            {
                "ko": "초인종 누르면 폰으로 보이는 거 맞죠?",
                "vi": "Bấm chuông cửa là hiện lên điện thoại đúng không?",
                "situation": "informal"
            }
        ],
        "relatedTerms": ["월패드", "보안시스템", "출입통제", "스마트홈"]
    },
    {
        "slug": "he-thong-dong-dien-yeu",
        "korean": "약전",
        "vietnamese": "Hệ thống dòng điện yếu",
        "hanja": "弱電",
        "hanjaReading": "弱(약할 약) + 電(전기 전)",
        "pronunciation": "약전",
        "meaningKo": "전압이 낮은 전기 시스템으로, 통신, 정보, 제어, 신호 전송 등에 사용되는 전기설비. 전화, 인터넷, CCTV, 화재경보, 출입통제, 방송설비 등이 포함됨. 통역 시 주의: 베트남에서는 'hệ thống dòng điện yếu' 또는 'hệ thống kỹ thuật'이라고 하며, 영어로는 ELV(Extra Low Voltage) 또는 LV(Low Voltage)라고 함. 한국에서 '약전'이라는 한자어를 사용하는 것과 달리, 베트남에서는 구체적으로 어떤 시스템인지(LAN, CCTV, BMS 등) 명시해야 의사소통이 원활함. 강전과의 배선 분리가 필수.",
        "meaningVi": "Hệ thống điện áp thấp dùng cho truyền thông, thông tin, điều khiển, tín hiệu. Bao gồm: mạng LAN, CCTV, hệ thống báo cháy, kiểm soát ra vào, âm thanh, BMS (Building Management System). Điện áp thường dưới 50V, phải tách riêng với hệ thống điện mạnh (dòng điện mạnh).",
        "context": "전기설비, 통신설비, 빌딩자동화",
        "culturalNote": "한국에서는 약전 배선을 별도의 전선관(PVC 또는 금속관)으로 시공하는 것이 원칙이지만, 베트남에서는 예산 절감을 위해 케이블 트레이(cable tray)를 많이 사용함. 베트남 현장에서는 강전 배선과 약전 배선을 충분히 분리하지 않아 노이즈 문제가 빈번하므로 시공 시 주의가 필요함. 또한 베트남에서는 약전 시스템을 전문적으로 다루는 업체가 따로 있어 분리 발주하는 경우가 많음.",
        "commonMistakes": [
            {
                "mistake": "약전을 'điện nhẹ'로 번역",
                "correction": "Hệ thống dòng điện yếu 또는 ELV",
                "explanation": "điện nhẹ는 비표준 표현이며 기술 문서에서 사용되지 않음"
            },
            {
                "mistake": "약전과 강전을 구분하지 않고 통역",
                "correction": "약전: điện yếu / 강전: điện mạnh",
                "explanation": "시공 방법과 안전 기준이 완전히 다름"
            },
            {
                "mistake": "약전 시스템을 구체적으로 명시하지 않음",
                "correction": "LAN, CCTV, 화재경보 등 구체적 항목 나열",
                "explanation": "베트남에서는 '약전'이라는 포괄 용어가 생소함"
            }
        ],
        "examples": [
            {
                "ko": "약전 배선은 천장 케이블 트레이로 시공하겠습니다.",
                "vi": "Hệ thống điện yếu sẽ thi công bằng cable tray trên trần.",
                "situation": "formal"
            },
            {
                "ko": "약전 라인이랑 강전 라인 섞이면 안 돼요.",
                "vi": "Đường dây điện yếu và điện mạnh không được lẫn vào nhau.",
                "situation": "onsite"
            },
            {
                "ko": "인터넷 선이랑 전화선은 약전이니까 따로 뽑아.",
                "vi": "Dây mạng với dây điện thoại là điện yếu nên kéo riêng.",
                "situation": "informal"
            }
        ],
        "relatedTerms": ["강전", "통신설비", "CCTV", "BMS"]
    },
    {
        "slug": "he-thong-dong-dien-manh",
        "korean": "강전",
        "vietnamese": "Hệ thống dòng điện mạnh",
        "hanja": "強電",
        "hanjaReading": "強(강할 강) + 電(전기 전)",
        "pronunciation": "강전",
        "meaningKo": "일반적인 전력 공급을 위한 높은 전압의 전기 시스템. 조명, 콘센트, 동력(모터), 냉난방 등에 사용되는 전기설비로, 일반적으로 220V 또는 380V 전압을 사용함. 통역 시 주의: 베트남에서는 'hệ thống dòng điện mạnh' 또는 'điện lực'이라고 하며, 영어로는 HV(High Voltage) 또는 Power System이라고 함. 베트남의 표준 전압은 220V/50Hz로 한국(220V/60Hz)과 전압은 같지만 주파수가 다름. 3상 전원은 380V를 사용하며, 배선 색상 코드(갈색-파랑-회색)도 한국과 다르므로 주의 필요.",
        "meaningVi": "Hệ thống điện áp cao dùng cấp nguồn cho thiết bị tiêu thụ điện năng: chiếu sáng, ổ cắm, động lực (motor), điều hòa. Điện áp thông dụng: 220V (1 pha) và 380V (3 pha). Tần số: 50Hz. Phải tách biệt hoàn toàn với hệ thống điện yếu.",
        "context": "전기설비, 동력설비, MEP",
        "culturalNote": "한국에서는 아파트 각 세대에 3상 전원을 공급하는 경우가 많지만, 베트남에서는 일반 주거용은 단상(220V)만 공급하는 것이 일반적임. 베트남의 전력 품질이 불안정하여 전압 변동과 순간 정전이 빈번하므로 중요 설비에는 UPS나 AVR 설치가 필수적임. 또한 베트남 전기요금 체계가 누진제가 아닌 단계별 요금제이므로 한국과 다른 전력 설계 접근이 필요함.",
        "commonMistakes": [
            {
                "mistake": "강전을 'điện cao áp'으로 번역",
                "correction": "Hệ thống dòng điện mạnh 또는 điện lực",
                "explanation": "điện cao áp은 고압송전(수만V)을 의미하며, 일반 강전과는 다름"
            },
            {
                "mistake": "한국과 베트남의 전기 주파수가 같다고 가정",
                "correction": "한국 60Hz, 베트남 50Hz 차이 명시",
                "explanation": "일부 전기기기는 주파수 차이로 오작동 가능"
            },
            {
                "mistake": "단상/3상 구분 없이 '전기'로만 통역",
                "correction": "1 pha(단상) / 3 pha(3상) 명확히 구분",
                "explanation": "베트남에서는 용도에 따라 엄격히 구분됨"
            }
        ],
        "examples": [
            {
                "ko": "지하 기계실에 380V 3상 전원 인입 완료했습니다.",
                "vi": "Đã hoàn thành đấu nối nguồn 3 pha 380V vào phòng máy tầng hầm.",
                "situation": "formal"
            },
            {
                "ko": "강전 메인 차단기 어디 있어요? 차단 좀 해야 되는데.",
                "vi": "CB chính điện mạnh ở đâu? Cần cắt điện.",
                "situation": "onsite"
            },
            {
                "ko": "이 콘센트 강전이니까 함부로 만지지 마.",
                "vi": "Ổ cắm này điện mạnh nên đừng có sờ lung tung.",
                "situation": "informal"
            }
        ],
        "relatedTerms": ["약전", "분전반", "차단기", "동력설비"]
    }
]

# 중복 체크 및 추가
filtered = [t for t in new_terms if t['slug'] not in existing_slugs]

if len(filtered) == 0:
    print("⚠️ All terms already exist. No new terms added.")
else:
    data.extend(filtered)

    # 저장
    with open(file_path, 'w', encoding='utf-8') as f:
        json.dump(data, f, ensure_ascii=False, indent=2)

    print(f"✅ Added {len(filtered)} new MEP terms to construction.json")
    print(f"📊 Total terms: {len(data)}")
    print("\n🆕 Added terms:")
    for term in filtered:
        print(f"  - {term['slug']}: {term['korean']} ({term['vietnamese']})")
