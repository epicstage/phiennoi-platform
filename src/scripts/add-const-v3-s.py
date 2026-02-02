import json
import os

# 파일 경로 설정
file_path = os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', 'data', 'terms', 'construction.json')

# 기존 데이터 로드
with open(file_path, 'r', encoding='utf-8') as f:
    data = json.load(f)

# 기존 slug 목록 추출
existing_slugs = {t['slug'] for t in data}

# 새 용어 추가 (지반개량/토질 - Ground Improvement)
new_terms = [
    {
        "slug": "chi-hoan-cong-phap",
        "korean": "치환공법",
        "vietnamese": "Phương pháp thay thế đất",
        "hanja": "置換工法",
        "hanjaReading": "置(둘 치) 換(바꿀 환) 工(장인 공) 法(법 법)",
        "pronunciation": "치환꽁뻡",
        "category": "construction",
        "difficulty": "intermediate",
        "frequency": "common",
        "meaningKo": "연약한 지반의 흙을 양질의 흙이나 자갈로 파내어 교체하는 지반개량공법입니다. 통역 시 '치환공법'과 '성토공법'을 혼동하지 않도록 주의해야 하며, 베트남 현장에서는 'đào đắp'(파고 채우기)라는 구어적 표현도 자주 사용됩니다. 시공 깊이, 치환재 종류, 다짐도 기준 등 구체적 시방을 정확히 전달하는 것이 중요합니다. 특히 '완전치환'과 '부분치환'을 구분하여 통역해야 합니다.",
        "meaningVi": "Phương pháp cải tạo nền đất yếu bằng cách đào bỏ đất xấu và thay thế bằng đất tốt hoặc đá dăm. Được sử dụng phổ biến trong xây dựng đường, sân bay và nền móng công trình. Yêu cầu kiểm soát chặt chẽ độ sâu đào, chất lượng vật liệu thay thế và độ đầm nén.",
        "context": "지반개량 시공계획 수립, 연약지반 대책공법 선정 시",
        "culturalNote": "한국은 산지가 많아 성토 후 침하 문제가 중요하지만, 베트남 델타 지역은 연약지반이 광범위하여 치환공법이 더 보편적으로 사용됩니다. 베트남 현장에서는 치환재로 현지 암석(đá dăm địa phương)을 선호하며, 환경 규제로 인해 준설토 활용이 제한적입니다. 한국식 '완전치환'과 베트남식 '부분치환+표층처리' 공법의 차이를 명확히 설명해야 합니다.",
        "commonMistakes": [
            {
                "mistake": "성토공법으로 번역",
                "correction": "치환공법(phương pháp thay thế đất)과 성토공법(phương pháp đắp đất)은 다른 공법",
                "explanation": "성토는 흙을 쌓는 것이고, 치환은 나쁜 흙을 파내고 좋은 흙으로 교체하는 것"
            },
            {
                "mistake": "'thay đất' (흙 바꾸기)로 단순 표현",
                "correction": "'phương pháp thay thế đất' 또는 'thay thế nền đất yếu'로 정확히 표현",
                "explanation": "공법의 전문성을 나타내기 위해 'phương pháp'을 명시해야 함"
            },
            {
                "mistake": "완전치환과 부분치환을 구분하지 않고 통역",
                "correction": "hoàn toàn thay thế(완전치환), một phần thay thế(부분치환)로 구분",
                "explanation": "시공 범위와 비용이 크게 차이나므로 정확한 구분 필수"
            }
        ],
        "examples": [
            {
                "ko": "연약지반 구간 500m에 대해 깊이 3m까지 치환공법을 적용합니다.",
                "vi": "Áp dụng phương pháp thay thế đất cho đoạn nền đất yếu 500m với độ sâu 3m.",
                "situation": "formal"
            },
            {
                "ko": "치환재로 쇄석 40-60mm를 사용하고, 다짐도 95% 이상 확보하세요.",
                "vi": "Sử dụng đá dăm 40-60mm làm vật liệu thay thế và đảm bảo độ đầm nén trên 95%.",
                "situation": "onsite"
            },
            {
                "ko": "이 구간은 부분치환으로 변경 가능한지 검토해주세요.",
                "vi": "Xin xem xét khả năng thay đổi sang phương pháp thay thế một phần cho đoạn này.",
                "situation": "formal"
            }
        ],
        "relatedTerms": ["성토공법", "지반개량", "연약지반", "다짐", "치환재"]
    },
    {
        "slug": "dam-nem-cat",
        "korean": "모래다짐말뚝",
        "vietnamese": "Cọc cát đầm chặt (Sand Compaction Pile)",
        "hanja": None,
        "hanjaReading": None,
        "pronunciation": "모래다짐말뚝",
        "category": "construction",
        "difficulty": "advanced",
        "frequency": "medium",
        "meaningKo": "연약지반에 모래를 투입하고 진동 또는 충격으로 다져서 형성하는 복합지반 개량공법입니다. 통역 시 'Sand Compaction Pile'의 약자인 'SCP공법'으로도 불리며, 베트남에서는 'cọc cát' 또는 'cọc cát đầm'으로 통용됩니다. 시공 시 진동기 종류(바이브로플롯, 바이브로해머), 모래 입도, 타설 간격, 치환율 등 기술 용어를 정확히 전달해야 합니다. '모래말뚝'과 '모래다짐말뚝'을 구분하는 것이 중요합니다.",
        "meaningVi": "Phương pháp cải tạo nền đất yếu bằng cách tạo các cọc cát trong lòng đất bằng rung hoặc đầm. Cọc cát kết hợp với đất xung quanh tạo thành nền tổng hợp có sức chịu tải cao hơn. Phương pháp này hiệu quả với đất sét yếu, giúp tăng cường khả năng thoát nước và giảm độ lún.",
        "context": "대규모 매립지, 항만시설, 공항 활주로 등 연약지반 개량 시",
        "culturalNote": "한국은 서해안 매립지에서 SCP공법을 많이 사용하지만, 베트남은 메콩델타 지역에서 주로 적용하며 시공장비 수급이 어려운 경우가 많습니다. 베트남 현장에서는 일본식 바이브로플롯 공법을 선호하지만, 장비 렌탈 비용이 높아 경제성 검토가 필수적입니다. 한국에서는 '치환율 70%'가 일반적이나, 베트남에서는 50-60%로 낮게 설계하는 경우가 많습니다.",
        "commonMistakes": [
            {
                "mistake": "'cọc cát'(모래말뚝)로만 표현",
                "correction": "'cọc cát đầm chặt' 또는 'Sand Compaction Pile'로 정확히 표현",
                "explanation": "다짐(đầm chặt)이 핵심 공정이므로 반드시 명시해야 함"
            },
            {
                "mistake": "바이브로플롯을 'máy rung'(진동기)로 단순 통역",
                "correction": "'máy rung baibro' 또는 'Vibroflot'로 음차 표기",
                "explanation": "특정 장비명은 음차로 표기하는 것이 현장에서 통용됨"
            },
            {
                "mistake": "치환율(tỷ lệ thay thế)과 개량율(tỷ lệ cải tạo)을 혼동",
                "correction": "치환율은 'tỷ lệ thay thế', 개량율은 'tỷ lệ cải tạo'로 구분",
                "explanation": "설계 파라미터가 다르므로 정확한 구분 필요"
            }
        ],
        "examples": [
            {
                "ko": "모래다짐말뚝 직경 700mm, 길이 15m, 타설 간격 1.8m로 시공합니다.",
                "vi": "Thi công cọc cát đầm chặt đường kính 700mm, chiều dài 15m, khoảng cách đóng cọc 1.8m.",
                "situation": "formal"
            },
            {
                "ko": "바이브로플롯으로 진동 다짐하면서 모래를 연속 투입하세요.",
                "vi": "Đầm rung bằng Vibroflot đồng thời đổ cát liên tục.",
                "situation": "onsite"
            },
            {
                "ko": "치환율 60% 설계안으로 진행해도 지내력 기준을 만족합니다.",
                "vi": "Thiết kế với tỷ lệ thay thế 60% vẫn đáp ứng tiêu chuẩn sức chịu tải.",
                "situation": "formal"
            }
        ],
        "relatedTerms": ["치환공법", "바이브로플롯", "연약지반", "치환율", "지반개량"]
    },
    {
        "slug": "yak-aek-chu-ip",
        "korean": "약액주입",
        "vietnamese": "Phun vữa hóa chất (Chemical Grouting)",
        "hanja": "藥液注入",
        "hanjaReading": "藥(약 약) 液(액체 액) 注(부을 주) 入(들 입)",
        "pronunciation": "야갱주입",
        "category": "construction",
        "difficulty": "advanced",
        "frequency": "medium",
        "meaningKo": "지반의 간극에 시멘트, 약액 등의 주입재를 압력으로 주입하여 지반을 강화하거나 차수하는 공법입니다. 통역 시 '그라우팅(grouting)'과 혼용되며, 베트남에서는 'phun vữa' 또는 'bơm hóa chất'로 표현합니다. 주입재 종류(시멘트계, 규산소다계, 우레탄계), 주입압력, 주입량, 겔타임 등 화학적 특성을 정확히 전달해야 합니다. 특히 지하수 차수 목적인지 지반 강화 목적인지를 명확히 구분하여 통역하는 것이 중요합니다.",
        "meaningVi": "Phương pháp gia cố hoặc chống thấm nền đất bằng cách bơm xi măng, hóa chất vào khe rỗng của đất dưới áp lực cao. Vữa được bơm vào sẽ lấp đầy khe rỗng và đông cứng lại, tạo thành khối đất có cường độ cao hoặc không thấm nước. Thường dùng trong xây dựng hầm, tàu điện ngầm, và xử lý thấm móng.",
        "context": "터널 공사, 지하철 건설, 댐 차수, 지반 보강 시",
        "culturalNote": "한국은 터널과 지하철 공사가 많아 약액주입 기술이 고도화되었으나, 베트남은 아직 초기 단계로 일본/한국 기술에 의존합니다. 베트남에서는 환경 규제로 화학약품 사용이 제한적이며, 시멘트 그라우팅을 선호합니다. 한국 현장에서는 '겔타임 조절'이 중요하지만, 베트남 고온 환경에서는 겔타임이 빨라지므로 배합 조정이 필수입니다.",
        "commonMistakes": [
            {
                "mistake": "'bơm xi măng'(시멘트 주입)로만 표현",
                "correction": "주입재에 따라 'phun vữa xi măng', 'phun hóa chất' 등으로 구분",
                "explanation": "시멘트계, 약액계에 따라 공법과 효과가 다름"
            },
            {
                "mistake": "그라우팅과 약액주입을 동일하게 통역",
                "correction": "그라우팅(grouting)은 넓은 개념, 약액주입(chemical grouting)은 구체적 공법",
                "explanation": "그라우팅에는 시멘트, 약액, 콘크리트 주입 등이 모두 포함됨"
            },
            {
                "mistake": "겔타임을 'thời gian đông cứng'(응결시간)으로 번역",
                "correction": "'thời gian gel hóa' 또는 'gel time'으로 음차",
                "explanation": "겔타임은 주입재가 겔 상태로 변하는 특정 시간으로, 응결시간과 다름"
            }
        ],
        "examples": [
            {
                "ko": "터널 막장 전방에 규산소다계 약액을 주입하여 차수합니다.",
                "vi": "Phun hóa chất gốc silicate vào phía trước mặt hầm để chống thấm.",
                "situation": "formal"
            },
            {
                "ko": "주입압력 5bar, 겔타임 30초로 시험주입 해보세요.",
                "vi": "Thử bơm với áp lực 5bar, thời gian gel hóa 30 giây.",
                "situation": "onsite"
            },
            {
                "ko": "약액주입 후 코어 채취로 침투 깊이를 확인합니다.",
                "vi": "Sau khi phun hóa chất, lấy lõi khoan để kiểm tra độ thấm sâu.",
                "situation": "formal"
            }
        ],
        "relatedTerms": ["그라우팅", "차수공사", "지반보강", "주입재", "겔타임"]
    },
    {
        "slug": "yeon-yak-ji-ban",
        "korean": "연약지반",
        "vietnamese": "Nền đất yếu",
        "hanja": "軟弱地盤",
        "hanjaReading": "軟(부드러울 연) 弱(약할 약) 地(땅 지) 盤(받침 반)",
        "pronunciation": "여냑찌반",
        "category": "construction",
        "difficulty": "intermediate",
        "frequency": "very_common",
        "meaningKo": "하중을 지지할 수 있는 힘이 약하고 압축성이 큰 지반으로, 주로 점토, 실트, 이탄 등으로 구성됩니다. 통역 시 '연약층', '약층'과 구분하며, 베트남에서는 'đất yếu' 또는 'nền đất yếu'로 표현합니다. 지내력, 압밀침하, 측방유동 등의 문제를 명확히 설명해야 하며, 특히 '연약지반 판정 기준'(N값, 일축압축강도)을 수치와 함께 통역하는 것이 중요합니다. 베트남 델타 지역에서는 거의 모든 현장이 연약지반입니다.",
        "meaningVi": "Nền đất có sức chịu tải kém và độ nén cao, thường gồm đất sét, bùn, than bùn. Đất yếu gây ra các vấn đề như lún, trượt nền, cần có biện pháp cải tạo trước khi xây dựng. Ở Việt Nam, đặc biệt vùng đồng bằng sông Cửu Long, nền đất yếu rất phổ biến và đòi hỏi xử lý đặc biệt.",
        "context": "지반조사 보고서, 기초 설계, 지반개량 공법 선정 시",
        "culturalNote": "한국은 서해안 매립지 위주로 연약지반이 분포하지만, 베트남은 메콩델타 전역이 연약지반으로 지반개량이 필수입니다. 베트남에서는 N값 4 이하를 연약지반으로 판정하며, 일축압축강도 50kPa 이하 기준을 사용합니다. 한국 기술자들은 '압밀침하 계산'을 중시하지만, 베트남 현장에서는 '단기 지내력 확보'에 더 집중하는 경향이 있습니다.",
        "commonMistakes": [
            {
                "mistake": "'đất mềm'(부드러운 흙)으로 번역",
                "correction": "'đất yếu' 또는 'nền đất yếu'로 표현",
                "explanation": "'mềm'은 물리적 촉감, 'yếu'는 공학적 지지력 부족을 의미"
            },
            {
                "mistake": "연약층(tầng đất yếu)과 연약지반(nền đất yếu)을 혼동",
                "correction": "연약층은 특정 층, 연약지반은 전체 지반 상태",
                "explanation": "층(tầng)은 지질학적 구분, 지반(nền)은 공학적 대상"
            },
            {
                "mistake": "N값을 'giá trị N'으로만 표현",
                "correction": "'chỉ số SPT' 또는 'giá trị N (SPT)'로 설명",
                "explanation": "SPT(Standard Penetration Test)를 명시해야 이해가 쉬움"
            }
        ],
        "examples": [
            {
                "ko": "이 현장은 N값 3 이하의 연약지반이 10m 깊이까지 분포합니다.",
                "vi": "Công trường này có nền đất yếu với chỉ số SPT dưới 3, phân bố đến độ sâu 10m.",
                "situation": "formal"
            },
            {
                "ko": "연약지반 구간은 치환공법으로 처리하기로 했습니다.",
                "vi": "Quyết định xử lý đoạn nền đất yếu bằng phương pháp thay thế đất.",
                "situation": "formal"
            },
            {
                "ko": "연약지반이라 성토 속도를 천천히 올려야 합니다.",
                "vi": "Do là nền đất yếu, cần tăng tốc độ đắp đất từ từ.",
                "situation": "onsite"
            }
        ],
        "relatedTerms": ["지내력", "압밀침하", "지반개량", "치환공법", "N값"]
    },
    {
        "slug": "to-jil-si-heom",
        "korean": "토질시험",
        "vietnamese": "Thí nghiệm cơ lý đất",
        "hanja": "土質試驗",
        "hanjaReading": "土(흙 토) 質(바탕 질) 試(시험할 시) 驗(시험할 험)",
        "pronunciation": "토질시험",
        "category": "construction",
        "difficulty": "intermediate",
        "frequency": "very_common",
        "meaningKo": "흙의 물리적·역학적 특성을 파악하기 위해 실시하는 각종 시험을 총칭합니다. 통역 시 '토질시험', '흙 시험', '지반조사'를 구분해야 하며, 베트남에서는 'thí nghiệm cơ lý đất' 또는 'thí nghiệm địa kỹ thuật'으로 표현합니다. 주요 시험 항목으로 입도분석, 함수비, 액성한계, 소성한계, 비중, 다짐시험, 투수시험, 압밀시험, 전단시험 등이 있으며, 각 시험명을 정확히 통역하는 것이 중요합니다. 특히 시험 결과 수치와 단위를 명확히 전달해야 합니다.",
        "meaningVi": "Tổng hợp các thí nghiệm để xác định tính chất vật lý và cơ học của đất. Bao gồm thí nghiệm phân tích hạt, độ ẩm, giới hạn Atterberg, tỷ trọng, đầm nén, thấm, nén lún, cắt. Kết quả thí nghiệm là cơ sở để thiết kế móng, đánh giá sức chịu tải và lựa chọn phương pháp xử lý nền.",
        "context": "지반조사 단계, 설계 검토, 시공 품질관리 시",
        "culturalNote": "한국은 토질시험 표준(KS F)이 체계적이고 시험소가 많지만, 베트남은 TCVN 기준을 따르며 시험소 수가 제한적입니다. 베트남에서는 '함수비 시험'을 가장 기본으로 하며, 한국처럼 '다짐시험'을 필수로 하지 않는 경우가 많습니다. 한국 기술자들은 '일축압축시험' 결과를 중시하지만, 베트남에서는 'SPT N값'에 더 의존하는 경향이 있습니다.",
        "commonMistakes": [
            {
                "mistake": "'thí nghiệm đất'(흙 시험)로 단순 표현",
                "correction": "'thí nghiệm cơ lý đất' 또는 'thí nghiệm địa kỹ thuật'으로 정확히 표현",
                "explanation": "공학적 시험임을 명확히 하기 위해 'cơ lý'(역학) 또는 'địa kỹ thuật'(지반공학) 명시"
            },
            {
                "mistake": "액성한계, 소성한계를 단순 번역",
                "correction": "'giới hạn Atterberg' 또는 'LL, PL'로 표준 용어 사용",
                "explanation": "국제적으로 통용되는 Atterberg 한계로 표현하는 것이 명확함"
            },
            {
                "mistake": "시험 결과 단위를 생략하고 통역",
                "correction": "함수비 %, 단위중량 kN/m³, 압축강도 kPa 등 단위 반드시 포함",
                "explanation": "단위가 없으면 수치의 의미가 달라질 수 있음"
            }
        ],
        "examples": [
            {
                "ko": "함수비 시험 결과 35%, 액성한계 48%로 고소성 점토입니다.",
                "vi": "Kết quả thí nghiệm độ ẩm 35%, giới hạn chảy 48%, là đất sét dẻo cao.",
                "situation": "formal"
            },
            {
                "ko": "다짐시험으로 최적 함수비와 최대건조단위중량을 구하세요.",
                "vi": "Xác định độ ẩm tối ưu và dung trọng khô lớn nhất qua thí nghiệm đầm nén.",
                "situation": "formal"
            },
            {
                "ko": "일축압축시험 3개 샘플 평균값으로 보고하세요.",
                "vi": "Báo cáo giá trị trung bình của 3 mẫu thí nghiệm nén một trục.",
                "situation": "onsite"
            }
        ],
        "relatedTerms": ["지반조사", "함수비", "액성한계", "다짐시험", "압밀시험"]
    },
    {
        "slug": "ji-nae-ryeok",
        "korean": "지내력",
        "vietnamese": "Sức chịu tải của nền (Bearing Capacity)",
        "hanja": "地耐力",
        "hanjaReading": "地(땅 지) 耐(견딜 내) 力(힘 력)",
        "pronunciation": "지내력",
        "category": "construction",
        "difficulty": "intermediate",
        "frequency": "very_common",
        "meaningKo": "지반이 상부 하중을 지탱할 수 있는 능력을 나타내는 공학적 지표입니다. 통역 시 '허용지내력', '극한지내력', '장기지내력', '단기지내력'을 명확히 구분해야 하며, 베트남에서는 'sức chịu tải' 또는 'khả năng chịu tải'으로 표현합니다. 단위는 kN/m², kPa, tf/m² 등이 사용되며, 설계 시 안전율을 고려한 허용지내력을 적용합니다. 특히 지내력 부족으로 인한 침하, 전단파괴 등의 문제를 설명할 때는 구체적 수치와 함께 통역하는 것이 중요합니다.",
        "meaningVi": "Khả năng chịu tải của nền đất đối với tải trọng từ công trình phía trên. Được tính toán dựa trên tính chất cơ lý của đất và hình dạng móng. Có sức chịu tải giới hạn (cực đại) và sức chịu tải cho phép (có hệ số an toàn). Đơn vị thường dùng: kN/m², kPa hoặc tf/m².",
        "context": "기초 설계, 지반조사 검토, 구조 계산 시",
        "culturalNote": "한국은 허용지내력 기준이 엄격하고 안전율 3.0을 일반적으로 적용하지만, 베트남은 안전율 2.0~2.5를 사용하는 경우가 많습니다. 베트남 델타 지역은 지내력이 매우 낮아(50kPa 이하) 말뚝기초가 필수적이며, 한국처럼 직접기초를 사용하기 어렵습니다. 한국 기술자들은 '장기허용지내력'을 중시하지만, 베트남에서는 '즉시 지내력 확보'에 초점을 맞춥니다.",
        "commonMistakes": [
            {
                "mistake": "'sức chịu tải'로만 표현하고 종류를 구분하지 않음",
                "correction": "허용지내력(sức chịu tải cho phép), 극한지내력(sức chịu tải giới hạn) 구분",
                "explanation": "설계에 사용되는 값과 이론적 최대값은 다름"
            },
            {
                "mistake": "지내력과 지지력을 혼용",
                "correction": "지내력(sức chịu tải nền)은 지반, 지지력(sức chịu tải móng)은 기초",
                "explanation": "지내력은 흙의 능력, 지지력은 기초 구조물의 능력"
            },
            {
                "mistake": "단위를 kgf/cm²로 통역",
                "correction": "국제 단위인 kPa 또는 kN/m²로 통역",
                "explanation": "베트남 기준(TCVN)도 SI 단위 사용"
            }
        ],
        "examples": [
            {
                "ko": "허용지내력 150kPa로 직접기초 설계 가능합니다.",
                "vi": "Có thể thiết kế móng trực tiếp với sức chịu tải cho phép 150kPa.",
                "situation": "formal"
            },
            {
                "ko": "지내력이 부족해서 말뚝기초로 변경합니다.",
                "vi": "Sức chịu tải nền không đủ nên chuyển sang móng cọc.",
                "situation": "formal"
            },
            {
                "ko": "평판재하시험으로 지내력을 확인하세요.",
                "vi": "Kiểm tra sức chịu tải bằng thí nghiệm nén tĩnh tấm.",
                "situation": "onsite"
            }
        ],
        "relatedTerms": ["허용지내력", "극한지내력", "기초설계", "지반조사", "평판재하시험"]
    },
    {
        "slug": "ham-su-bi",
        "korean": "함수비",
        "vietnamese": "Độ ẩm (Water Content)",
        "hanja": "含水比",
        "hanjaReading": "含(머금을 함) 水(물 수) 比(비교할 비)",
        "pronunciation": "함수비",
        "category": "construction",
        "difficulty": "basic",
        "frequency": "very_common",
        "meaningKo": "흙 속에 포함된 물의 무게를 흙 입자의 무게로 나눈 백분율로, 흙의 상태를 나타내는 가장 기본적인 지표입니다. 통역 시 '함수율', '수분함량'과 혼용되며, 베트남에서는 'độ ẩm' 또는 'hàm lượng nước'로 표현합니다. 자연함수비, 최적함수비, 포화함수비 등을 구분해야 하며, 특히 '최적함수비'는 다짐 시공 품질관리에 매우 중요합니다. 단위는 %로 표기하며, 소수점 첫째 자리까지 표현합니다.",
        "meaningVi": "Tỷ lệ phần trăm giữa khối lượng nước và khối lượng hạt đất khô. Là chỉ số cơ bản nhất để đánh giá trạng thái của đất. Độ ẩm tự nhiên (hiện trường), độ ẩm tối ưu (đầm nén), độ ẩm bão hòa (đầy nước) là các khái niệm quan trọng trong thi công và kiểm soát chất lượng.",
        "context": "토질시험, 다짐 품질관리, 지반조사 보고서 작성 시",
        "culturalNote": "한국은 함수비 측정을 매우 엄격하게 하며, 다짐 시공 시 최적함수비 ±2% 이내 관리를 요구합니다. 베트남은 건기/우기 함수비 변화가 크고, 우기에는 함수비 관리가 매우 어렵습니다. 한국 기술자들은 '노건조법'으로 정확히 측정하지만, 베트남 현장에서는 간이 측정기(휴대용 함수비 측정기)를 많이 사용합니다.",
        "commonMistakes": [
            {
                "mistake": "'độ nước' 또는 'lượng nước'로 번역",
                "correction": "'độ ẩm' 또는 'hàm lượng nước'로 표준 용어 사용",
                "explanation": "'độ ẩm'이 공학적으로 정확한 표현"
            },
            {
                "mistake": "함수비와 함수율을 다르게 통역",
                "correction": "함수비와 함수율은 같은 의미로 'độ ẩm' 사용",
                "explanation": "한국에서도 두 용어를 혼용하므로 베트남어는 통일"
            },
            {
                "mistake": "자연함수비와 최적함수비를 구분하지 않음",
                "correction": "독 ẩm tự nhiên(자연), độ ẩm tối ưu(최적)로 명확히 구분",
                "explanation": "자연 상태와 다짐 최적 상태는 다른 개념"
            }
        ],
        "examples": [
            {
                "ko": "자연함수비 28.5%로 포화에 가까운 상태입니다.",
                "vi": "Độ ẩm tự nhiên 28.5%, gần trạng thái bão hòa.",
                "situation": "formal"
            },
            {
                "ko": "최적함수비 15%에서 다짐해야 다짐도가 나옵니다.",
                "vi": "Cần đầm ở độ ẩm tối ưu 15% thì mới đạt độ đầm nén.",
                "situation": "onsite"
            },
            {
                "ko": "함수비가 너무 높으니 건조 후 다시 다짐하세요.",
                "vi": "Độ ẩm quá cao, cần phơi khô rồi đầm lại.",
                "situation": "onsite"
            }
        ],
        "relatedTerms": ["토질시험", "최적함수비", "다짐", "다짐도", "포화도"]
    },
    {
        "slug": "geu-ra-u-ting",
        "korean": "그라우팅",
        "vietnamese": "Phun vữa (Grouting)",
        "hanja": None,
        "hanjaReading": None,
        "pronunciation": "그라우팅",
        "category": "construction",
        "difficulty": "intermediate",
        "frequency": "common",
        "meaningKo": "콘크리트, 암반, 지반의 균열이나 공극에 시멘트, 약액 등을 압력으로 주입하여 충전·보강·차수하는 공법의 총칭입니다. 통역 시 '그라우팅', '주입공법', '몰탈주입'을 구분해야 하며, 베트남에서는 'phun vữa' 또는 'bơm vữa'로 표현합니다. 시멘트 그라우팅, 약액 그라우팅, 콘크리트 그라우팅으로 세분화되며, 목적(차수, 보강, 공극 충전)에 따라 주입재와 공법이 달라집니다. 특히 터널, 댐, PSC 긴장재 등 적용 부위를 명확히 설명해야 합니다.",
        "meaningVi": "Tổng hợp các phương pháp bơm xi măng, vữa, hóa chất vào khe nứt, lỗ rỗng của bê tông, đá hoặc đất để lấp đầy, gia cố hoặc chống thấm. Có grouting xi măng (phun vữa xi măng), grouting hóa chất (phun hóa chất), grouting bê tông. Thường dùng trong xây dựng hầm, đập, cầu dự ứng lực.",
        "context": "터널 공사, 댐 건설, PSC 공사, 지반 보강 시",
        "culturalNote": "한국은 PSC 교량 공사에서 그라우팅 품질관리가 매우 엄격하며, 긴장재 그라우팅은 필수입니다. 베트남은 아직 그라우팅 기술 수준이 낮아 외국 기술에 의존하며, 특히 댐 그라우팅은 일본/한국 기술자가 감독합니다. 한국에서는 '압력 그라우팅'과 '중력 그라우팅'을 명확히 구분하지만, 베트남 현장에서는 주로 압력 방식만 사용합니다.",
        "commonMistakes": [
            {
                "mistake": "'bơm xi măng'(시멘트 펌핑)로 단순 표현",
                "correction": "'phun vữa' 또는 'grouting'로 음차 표기",
                "explanation": "그라우팅은 단순 펌핑이 아니라 압력 주입 공법"
            },
            {
                "mistake": "콘크리트 타설(đổ bê tông)과 그라우팅을 혼동",
                "correction": "타설은 거푸집 내부 충전, 그라우팅은 공극/균열 주입",
                "explanation": "대상과 목적이 완전히 다름"
            },
            {
                "mistake": "PSC 그라우팅을 '케이블 주입'으로 번역",
                "correction": "'grouting cáp dự ứng lực' 또는 'phun vữa bảo vệ cáp'",
                "explanation": "긴장재를 보호하기 위한 특수 그라우팅임을 명시"
            }
        ],
        "examples": [
            {
                "ko": "터널 막장 그라우팅으로 지하수를 차단합니다.",
                "vi": "Chống thấm nước ngầm bằng phun vữa tại mặt hầm.",
                "situation": "formal"
            },
            {
                "ko": "PSC 긴장재 그라우팅은 긴장 후 48시간 이내에 완료하세요.",
                "vi": "Hoàn thành grouting cáp dự ứng lực trong vòng 48 giờ sau khi căng.",
                "situation": "onsite"
            },
            {
                "ko": "암반 그라우팅 주입압력 20bar로 시공합니다.",
                "vi": "Thi công phun vữa đá với áp lực bơm 20bar.",
                "situation": "formal"
            }
        ],
        "relatedTerms": ["약액주입", "차수공사", "PSC", "주입재", "주입압력"]
    },
    {
        "slug": "ji-ha-su-wi",
        "korean": "지하수위",
        "vietnamese": "Mực nước ngầm (Groundwater Level)",
        "hanja": "地下水位",
        "hanjaReading": "地(땅 지) 下(아래 하) 水(물 수) 位(자리 위)",
        "pronunciation": "지하수위",
        "category": "construction",
        "difficulty": "basic",
        "frequency": "very_common",
        "meaningKo": "지표면 아래 땅속에 존재하는 지하수의 수면 높이로, 지반공학과 기초 설계에서 매우 중요한 요소입니다. 통역 시 '지하수면', '지하수 수위'와 혼용되며, 베트남에서는 'mực nước ngầm' 또는 'cao độ nước ngầm'으로 표현합니다. 지하수위는 계절, 강우량, 조수에 따라 변동하므로, 설계 시 최고 지하수위(H.W.L)와 최저 지하수위(L.W.L)를 모두 고려해야 합니다. 특히 굴착, 터널, 지하 구조물 시공 시 지하수 처리(배수, 차수)가 필수적입니다.",
        "meaningVi": "Độ cao mặt nước ngầm dưới mặt đất, là yếu tố quan trọng trong thiết kế móng và thi công hầm. Mực nước ngầm thay đổi theo mùa, lượng mưa và thủy triều. Cần xác định mực nước ngầm cao nhất (H.W.L) và thấp nhất (L.W.L) để thiết kế. Trong thi công đào móng sâu, cần hạ thấp mực nước ngầm hoặc chống thấm.",
        "context": "지반조사, 기초 설계, 굴착 계획, 지하 구조물 시공 시",
        "culturalNote": "한국은 사계절이 뚜렷하여 지하수위 변동이 크지만, 베트남은 건기/우기에 따라 변동폭이 더 큽니다. 베트남 델타 지역은 지하수위가 지표면 바로 아래(GL-1m 이내)에 있어 굴착이 매우 어렵습니다. 한국에서는 '웰포인트 공법'으로 지하수위를 낮추지만, 베트남에서는 차수벽(지수벽) 설치를 선호합니다. 베트남 해안 지역은 조수의 영향으로 하루 중에도 지하수위가 변동합니다.",
        "commonMistakes": [
            {
                "mistake": "'nước ngầm'(지하수)로만 표현",
                "correction": "'mực nước ngầm'(지하수위) 또는 'cao độ nước ngầm'으로 정확히 표현",
                "explanation": "'nước ngầm'은 물 자체, 'mực nước ngầm'은 수위(높이)"
            },
            {
                "mistake": "H.W.L과 L.W.L을 영어로만 통역",
                "correction": "'mực nước ngầm cao nhất (H.W.L)', 'mực nước ngầm thấp nhất (L.W.L)'로 설명",
                "explanation": "약어만으로는 이해하기 어려우므로 베트남어 설명 필수"
            },
            {
                "mistake": "지하수위와 지하수압을 혼동",
                "correction": "지하수위는 'mực nước ngầm', 지하수압은 'áp lực nước ngầm'",
                "explanation": "수위는 높이, 수압은 압력으로 다른 개념"
            }
        ],
        "examples": [
            {
                "ko": "지하수위가 GL-2m로 얕아서 배수 공법이 필요합니다.",
                "vi": "Mực nước ngầm ở độ sâu GL-2m, cần áp dụng công pháp thoát nước.",
                "situation": "formal"
            },
            {
                "ko": "우기에는 지하수위가 1m 이상 올라갑니다.",
                "vi": "Vào mùa mưa, mực nước ngầm dâng lên hơn 1m.",
                "situation": "formal"
            },
            {
                "ko": "웰포인트로 지하수위를 5m 낮추세요.",
                "vi": "Hạ thấp mực nước ngầm 5m bằng công pháp wellpoint.",
                "situation": "onsite"
            }
        ],
        "relatedTerms": ["지하수", "배수공법", "웰포인트", "차수공사", "굴착"]
    },
    {
        "slug": "tu-su-gye-su",
        "korean": "투수계수",
        "vietnamese": "Hệ số thấm (Permeability Coefficient)",
        "hanja": "透水係數",
        "hanjaReading": "透(뚫을 투) 水(물 수) 係(맬 계) 數(셀 수)",
        "pronunciation": "투수계수",
        "category": "construction",
        "difficulty": "advanced",
        "frequency": "medium",
        "meaningKo": "물이 흙을 통과하는 속도를 나타내는 계수로, 지반의 투수성을 정량적으로 표현하는 지표입니다. 통역 시 '투수성', '투수능력'과 구분하며, 베트남에서는 'hệ số thấm' 또는 'độ thấm'으로 표현합니다. 단위는 cm/s 또는 m/day이며, 값이 클수록 물이 잘 통과합니다. 투수계수는 배수 설계, 차수 설계, 압밀침하 계산에 필수적이며, 정수위 투수시험 또는 변수위 투수시험으로 측정합니다. 흙의 종류에 따라 투수계수가 크게 달라집니다.",
        "meaningVi": "Hệ số biểu thị tốc độ nước thấm qua đất, là chỉ tiêu định lượng độ thấm của nền đất. Đơn vị: cm/s hoặc m/ngày. Hệ số thấm càng lớn thì nước càng dễ thấm qua. Là yếu tố quan trọng trong thiết kế thoát nước, chống thấm, tính toán lún. Đo bằng thí nghiệm thấm mực nước cố định hoặc thay đổi.",
        "context": "배수 설계, 차수 설계, 압밀침하 계산, 토질시험 보고서 작성 시",
        "culturalNote": "한국은 투수계수 측정을 표준화하여 시행하지만, 베트남은 시험 장비가 부족하여 경험값에 의존하는 경우가 많습니다. 베트남 델타 지역 점토는 투수계수가 매우 낮아(10⁻⁷ cm/s 이하) 압밀 배수에 오랜 시간이 걸립니다. 한국 기술자들은 '투수계수'를 정확히 측정하여 설계하지만, 베트남에서는 '투수/불투수' 정도로만 판단하는 경향이 있습니다.",
        "commonMistakes": [
            {
                "mistake": "'độ thấm'(투수성)로만 표현",
                "correction": "'hệ số thấm'(투수계수)로 정확히 표현",
                "explanation": "'độ thấm'은 정성적, 'hệ số thấm'은 정량적 지표"
            },
            {
                "mistake": "단위를 생략하고 수치만 통역",
                "correction": "10⁻⁵ cm/s 또는 0.01 cm/s처럼 단위 반드시 포함",
                "explanation": "단위가 없으면 수치의 크기를 판단할 수 없음"
            },
            {
                "mistake": "투수계수와 투수능을 혼동",
                "correction": "투수계수는 'hệ số thấm', 투수능은 'khả năng thấm'",
                "explanation": "계수는 수치, 능은 능력으로 구분"
            }
        ],
        "examples": [
            {
                "ko": "이 점토층의 투수계수는 5×10⁻⁷ cm/s로 거의 불투수입니다.",
                "vi": "Hệ số thấm của tầng sét này là 5×10⁻⁷ cm/s, gần như không thấm.",
                "situation": "formal"
            },
            {
                "ko": "배수층으로 투수계수 10⁻³ cm/s 이상의 모래를 사용하세요.",
                "vi": "Sử dụng cát có hệ số thấm trên 10⁻³ cm/s cho lớp thoát nước.",
                "situation": "onsite"
            },
            {
                "ko": "투수시험으로 투수계수를 측정해서 배수 설계에 반영합니다.",
                "vi": "Đo hệ số thấm qua thí nghiệm thấm và áp dụng vào thiết kế thoát nước.",
                "situation": "formal"
            }
        ],
        "relatedTerms": ["투수성", "배수공법", "차수공사", "토질시험", "압밀침하"]
    }
]

# 중복 방지: 기존에 없는 slug만 추가
filtered = [t for t in new_terms if t['slug'] not in existing_slugs]

# 기존 데이터에 추가 (data는 배열이므로 extend 사용)
data.extend(filtered)

# 파일 저장
with open(file_path, 'w', encoding='utf-8') as f:
    json.dump(data, f, ensure_ascii=False, indent=2)

print(f"Added {len(filtered)} terms. Total: {len(data)}")
