import json
import os

file_path = os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', 'data', 'terms', 'construction.json')

with open(file_path, 'r', encoding='utf-8') as f:
    data = json.load(f)

existing_slugs = {t['slug'] for t in data}

new_terms = [
    {
        "slug": "bai-gan",
        "korean": "배근",
        "vietnamese": "bài gan",
        "hanja": "配筋",
        "hanjaReading": "配(나눌 배) + 筋(힘줄 근)",
        "pronunciation": "바이 간",
        "meaningKo": "철근콘크리트 구조물에서 철근을 설계도에 따라 정확한 위치에 배치하는 작업입니다. 통역 시 '배근도'와 '배치도'를 혼동하지 않도록 주의해야 합니다. 베트남 현장에서는 'sơ đồ bài gan'(배근도)라는 용어를 자주 사용하며, 한국식 배근 간격과 베트남 기준이 다를 수 있어 도면 검토 시 반드시 확인이 필요합니다. 철근의 종류, 직경, 간격, 겹이음 길이 등 세부 사항을 정확히 전달하는 것이 안전과 직결됩니다.",
        "meaningVi": "Công việc bố trí cốt thép trong kết cấu bê tông cốt thép theo đúng vị trí, khoảng cách và chi tiết thiết kế. Bao gồm việc xác định số lượng, đường kính, chiều dài neo, chiều dài nối và khoảng cách giữa các thanh thép.",
        "context": "철근 배치 작업, 구조 시공",
        "culturalNote": "한국은 배근 시 철근 간격을 mm 단위로 매우 정밀하게 관리하며, 배근검사를 엄격히 실시합니다. 베트남 현장에서는 숙련공의 경험에 의존하는 경우가 많아 한국 감리가 배근 검수를 철저히 해야 합니다. 특히 내진 설계가 적용된 구조물의 경우 한국 기준이 더 엄격하므로 배근 상세를 명확히 전달해야 합니다.",
        "commonMistakes": [
            {
                "mistake": "bài gan을 bố trí cốt thép로만 번역",
                "correction": "bài gan 또는 sắp đặt cốt thép",
                "explanation": "베트남 현장에서는 'bài gan'이 더 일반적이며, 'bố trí'만 쓰면 단순 배치로 오해될 수 있습니다."
            },
            {
                "mistake": "배근도를 'bản vẽ bố trí'로 번역",
                "correction": "sơ đồ bài gan 또는 bản vẽ cốt thép",
                "explanation": "배근도는 철근 배치 전용 도면이므로 'sơ đồ bài gan'이 정확합니다."
            },
            {
                "mistake": "철근 간격을 'khoảng'으로만 표현",
                "correction": "khoảng cách giữa các thanh thép",
                "explanation": "'khoảng'만으로는 간격인지 구간인지 모호하므로 전체 표현을 사용해야 합니다."
            }
        ],
        "examples": [
            {
                "ko": "이 기둥은 D19 철근을 200mm 간격으로 배근합니다.",
                "vi": "Cột này bài gan cốt thép D19 với khoảng cách 200mm.",
                "situation": "formal"
            },
            {
                "ko": "배근 검사 후에 콘크리트를 타설하세요.",
                "vi": "Hãy đổ bê tông sau khi kiểm tra bài gan.",
                "situation": "onsite"
            },
            {
                "ko": "배근도에 표시된 위치와 다르게 시공되었습니다.",
                "vi": "Thi công sai so với vị trí trên sơ đồ bài gan.",
                "situation": "formal"
            }
        ],
        "relatedTerms": ["cot-thep", "be-tong", "ban-ve-thi-cong", "do-be-tong"]
    },
    {
        "slug": "do-day-lop-phu",
        "korean": "피복두께",
        "vietnamese": "độ dày lớp phủ",
        "hanja": "被覆厚",
        "hanjaReading": "被(입을 피) + 覆(덮을 복) + 厚(두터울 후)",
        "pronunciation": "도 자이 럽 푸",
        "meaningKo": "철근콘크리트에서 철근 표면부터 콘크리트 외부 표면까지의 최소 거리를 말합니다. 통역 시 '피복'과 '피복두께'를 구분해야 하며, 베트남어로는 'lớp bảo vệ' 또는 'độ dày lớp phủ'로 표현합니다. 철근 부식 방지와 내화성능 확보를 위해 매우 중요한 수치이며, 한국 기준(KDS)과 베트남 기준(TCVN)이 다를 수 있어 설계 단계에서 명확히 확인해야 합니다. 현장에서 피복두께 부족은 구조물 내구성에 치명적 영향을 미칩니다.",
        "meaningVi": "Khoảng cách tối thiểu từ bề mặt cốt thép đến bề mặt ngoài của bê tông, nhằm bảo vệ cốt thép khỏi ăn mòn và đảm bảo khả năng chịu lửa. Là yếu tố quan trọng ảnh hưởng trực tiếp đến độ bền của kết cấu bê tông cốt thép.",
        "context": "철근 시공, 품질 관리",
        "culturalNote": "한국에서는 피복두께를 스페이서로 정밀하게 유지하며, 검측 시 필수 확인 항목입니다. 베트남 현장에서는 피복두께 관리가 상대적으로 느슨한 경우가 많아 한국 감리의 철저한 검수가 필요합니다. 특히 해안가나 습한 환경에서는 피복두께가 부족하면 철근 부식이 빠르게 진행되므로 주의해야 합니다.",
        "commonMistakes": [
            {
                "mistake": "피복두께를 'độ phủ'로만 번역",
                "correction": "độ dày lớp phủ 또는 lớp bảo vệ bê tông",
                "explanation": "'độ phủ'는 커버리지를 의미하므로 두께를 명시해야 합니다."
            },
            {
                "mistake": "40mm를 'bốn mươi mm'로 읽기",
                "correction": "bốn mươi mi-li-mét",
                "explanation": "베트남에서는 단위를 풀어서 읽는 것이 더 명확합니다."
            },
            {
                "mistake": "피복 부족을 'thiếu lớp phủ'로만 표현",
                "correction": "độ dày lớp phủ không đủ",
                "explanation": "두께가 부족함을 명확히 전달해야 합니다."
            }
        ],
        "examples": [
            {
                "ko": "기둥의 피복두께는 최소 40mm 이상 확보해야 합니다.",
                "vi": "Độ dày lớp phủ của cột phải đảm bảo tối thiểu 40mm.",
                "situation": "formal"
            },
            {
                "ko": "스페이서로 피복두께를 유지하세요.",
                "vi": "Dùng đệm định vị để giữ độ dày lớp phủ.",
                "situation": "onsite"
            },
            {
                "ko": "피복두께가 부족하면 철근이 부식됩니다.",
                "vi": "Nếu độ dày lớp phủ không đủ, cốt thép sẽ bị ăn mòn.",
                "situation": "formal"
            }
        ],
        "relatedTerms": ["cot-thep", "be-tong", "e-seu-keol-lei-teo", "bai-gan"]
    },
    {
        "slug": "noi-cot-thep",
        "korean": "이음",
        "vietnamese": "nối cốt thép",
        "hanja": "繼音",
        "hanjaReading": "繼(이을 계) + 音(소리 음)",
        "pronunciation": "노이 꼿 텝",
        "meaningKo": "철근의 길이가 부족할 때 두 개 이상의 철근을 연결하여 연속성을 확보하는 작업입니다. 통역 시 '겹이음', '용접이음', '기계적이음'을 정확히 구분해야 합니다. 한국에서는 겹이음 길이를 철근 직경의 40~50배로 규정하지만 베트남 기준은 다를 수 있으므로 설계 기준을 명확히 전달해야 합니다. 이음 위치가 집중되면 구조적 취약점이 되므로 천장 또는 보 중앙부를 피하고 응력이 적은 구간에 배치하는 것이 원칙입니다.",
        "meaningVi": "Công việc liên kết hai hay nhiều thanh cốt thép với nhau để tạo sự liên tục khi chiều dài cốt thép không đủ. Có các phương pháp nối: nối chồng (nối ghép), nối hàn và nối cơ học. Vị trí và chiều dài nối phải tuân thủ tiêu chuẩn thiết kế.",
        "context": "철근 시공, 구조 설계",
        "culturalNote": "한국 현장에서는 이음 위치와 길이를 매우 엄격하게 관리하며, 겹이음 시 철선으로 단단히 묶는 것을 원칙으로 합니다. 베트남에서는 용접이음을 선호하는 경향이 있으나, 용접 품질 관리가 어려워 한국 감리는 겹이음을 권장하는 경우가 많습니다. 이음 위치가 한 단면에 집중되지 않도록 엇갈리게 배치하는 것이 중요합니다.",
        "commonMistakes": [
            {
                "mistake": "이음을 'kết nối'로만 번역",
                "correction": "nối cốt thép 또는 mối nối",
                "explanation": "'kết nối'는 일반적인 연결이므로 철근 이음 전문 용어를 사용해야 합니다."
            },
            {
                "mistake": "겹이음을 'nối chồng lên'으로 표현",
                "correction": "nối chồng 또는 nối ghép",
                "explanation": "베트남 건설 현장에서는 'nối chồng'이 표준 용어입니다."
            },
            {
                "mistake": "이음 길이를 'chiều dài nối'로만 번역",
                "correction": "chiều dài đoạn nối chồng",
                "explanation": "겹이음의 경우 '중첩 구간 길이'를 명확히 표현해야 합니다."
            }
        ],
        "examples": [
            {
                "ko": "D25 철근은 겹이음 길이를 1,000mm 이상 확보하세요.",
                "vi": "Cốt thép D25 phải đảm bảo chiều dài nối chồng tối thiểu 1.000mm.",
                "situation": "formal"
            },
            {
                "ko": "이음 위치를 서로 엇갈리게 배치하세요.",
                "vi": "Hãy bố trí vị trí nối xen kẽ nhau.",
                "situation": "onsite"
            },
            {
                "ko": "기둥 하단부에는 이음을 하지 마세요.",
                "vi": "Không nối cốt thép ở phần đáy cột.",
                "situation": "onsite"
            }
        ],
        "relatedTerms": ["cot-thep", "bai-gan", "han-diep", "do-day-lop-phu"]
    },
    {
        "slug": "neo-cot-thep",
        "korean": "정착",
        "vietnamese": "neo cốt thép",
        "hanja": "定着",
        "hanjaReading": "定(정할 정) + 着(붙을 착)",
        "pronunciation": "네오 꼿 텝",
        "meaningKo": "철근의 끝부분을 콘크리트 속에 일정 길이만큼 묻어서 철근과 콘크리트가 함께 힘을 받도록 하는 구조적 처리 방법입니다. 통역 시 '정착길이'와 '갈고리 정착'을 구분해야 하며, 베트남어로는 'neo' 또는 'cố định'으로 표현합니다. 정착 길이가 부족하면 철근이 콘크리트에서 빠져나와(인발) 구조물이 붕괴될 수 있으므로 매우 중요합니다. 한국 기준으로는 일반적으로 철근 직경의 30~40배 이상을 정착길이로 확보해야 합니다.",
        "meaningVi": "Phương pháp xử lý kết cấu bằng cách chôn đầu cốt thép vào trong bê tông một chiều dài nhất định để cốt thép và bê tông cùng chịu lực. Chiều dài neo phải đủ để ngăn cốt thép bị rút ra khỏi bê tông. Có thể sử dụng móc neo để tăng khả năng cố định.",
        "context": "철근 시공, 구조 안전",
        "culturalNote": "한국에서는 정착 길이와 갈고리 각도를 설계도에 명확히 표시하며, 시공 시 반드시 준수하도록 감독합니다. 베트남 현장에서는 정착 개념이 상대적으로 약해 철근이 짧게 잘리는 경우가 있으므로 통역사는 '정착 길이 부족은 구조 붕괴로 이어진다'는 점을 강조해야 합니다. 특히 벽체와 슬래브 접합부의 정착은 안전에 매우 중요합니다.",
        "commonMistakes": [
            {
                "mistake": "정착을 'cố định'으로만 번역",
                "correction": "neo cốt thép 또는 liên kết neo",
                "explanation": "'cố định'은 일반적인 고정이므로 철근 정착 전문 용어를 사용해야 합니다."
            },
            {
                "mistake": "정착길이를 'chiều dài cố định'으로 표현",
                "correction": "chiều dài neo",
                "explanation": "베트남 건설 기준에서는 'chiều dài neo'가 표준입니다."
            },
            {
                "mistake": "갈고리 정착을 'neo có móc'로만 표현",
                "correction": "neo bằng móc hoặc móc neo",
                "explanation": "갈고리 정착의 구조적 의미를 명확히 전달해야 합니다."
            }
        ],
        "examples": [
            {
                "ko": "이 보의 주철근은 기둥 안으로 600mm 정착해야 합니다.",
                "vi": "Cốt thép chính của dầm này phải neo vào cột 600mm.",
                "situation": "formal"
            },
            {
                "ko": "스터럽은 135도 갈고리로 정착하세요.",
                "vi": "Đai thép phải neo bằng móc 135 độ.",
                "situation": "onsite"
            },
            {
                "ko": "정착 길이가 부족하면 인발 파괴가 발생합니다.",
                "vi": "Nếu chiều dài neo không đủ, sẽ xảy ra phá hoại do rút cốt thép.",
                "situation": "formal"
            }
        ],
        "relatedTerms": ["cot-thep", "bai-gan", "noi-cot-thep", "be-tong"]
    },
    {
        "slug": "dem-dinh-vi",
        "korean": "스페이서",
        "vietnamese": "đệm định vị",
        "hanja": None,
        "hanjaReading": None,
        "pronunciation": "뎀 딘 비",
        "meaningKo": "철근과 거푸집 사이의 간격을 일정하게 유지하여 피복두께를 확보하기 위한 보조 자재입니다. 통역 시 '스페이서'를 베트남어로 'đệm định vị' 또는 'đệm chống'으로 표현하며, 플라스틱, 콘크리트, 철재 등 다양한 재질이 있습니다. 한국 현장에서는 피복두께 확보를 위해 스페이서 설치를 필수로 하지만, 베트nam 현장에서는 생략되는 경우가 많아 품질 저하의 원인이 됩니다. 스페이서 간격은 보통 1m 내외로 배치하며, 슬래브는 1㎡당 4~5개 정도 설치합니다.",
        "meaningVi": "Vật liệu phụ trợ được đặt giữa cốt thép và ván khuôn để duy trì khoảng cách đều, đảm bảo độ dày lớp phủ bê tông. Có nhiều loại: đệm nhựa, đệm bê tông, đệm thép. Việc sử dụng đệm định vị giúp bảo vệ cốt thép khỏi ăn mòn và đảm bảo chất lượng kết cấu.",
        "context": "철근 시공, 품질 관리",
        "culturalNote": "한국에서는 스페이서를 표준화된 제품으로 사용하며 간격과 개수를 엄격히 관리합니다. 베트남 현장에서는 스페이서 대신 벽돌 조각이나 나무 조각을 사용하는 경우가 있는데, 이는 피복두께 불균일과 품질 저하를 유발하므로 반드시 정식 스페이서를 사용하도록 지도해야 합니다. 특히 바닥 슬래브의 경우 스페이서가 콘크리트 타설 중 이탈하지 않도록 고정이 중요합니다.",
        "commonMistakes": [
            {
                "mistake": "스페이서를 'khoảng cách'로 번역",
                "correction": "đệm định vị 또는 đệm chống",
                "explanation": "'khoảng cách'는 간격이지 스페이서 부품을 의미하지 않습니다."
            },
            {
                "mistake": "피복 유지 장치를 'thiết bị giữ lớp phủ'로 표현",
                "correction": "đệm định vị",
                "explanation": "베트남 현장에서는 'đệm định vị'가 표준 용어입니다."
            },
            {
                "mistake": "스페이서 설치를 'lắp đệm'으로만 표현",
                "correction": "bố trí đệm định vị 또는 đặt đệm chống",
                "explanation": "설치 목적과 위치를 명확히 전달해야 합니다."
            }
        ],
        "examples": [
            {
                "ko": "슬래브 하부 철근에 스페이서를 1m 간격으로 설치하세요.",
                "vi": "Đặt đệm định vị cho cốt thép đáy sàn với khoảng cách 1m.",
                "situation": "onsite"
            },
            {
                "ko": "플라스틱 스페이서를 사용해서 피복두께 40mm를 확보하세요.",
                "vi": "Dùng đệm định vị nhựa để đảm bảo độ dày lớp phủ 40mm.",
                "situation": "formal"
            },
            {
                "ko": "콘크리트 타설 전에 스페이서가 이탈하지 않았는지 확인하세요.",
                "vi": "Kiểm tra đệm định vị không bị rơi trước khi đổ bê tông.",
                "situation": "onsite"
            }
        ],
        "relatedTerms": ["do-day-lop-phu", "cot-thep", "van-khuon", "do-be-tong"]
    },
    {
        "slug": "be-tong-thuong-pham",
        "korean": "레미콘",
        "vietnamese": "bê tông thương phẩm",
        "hanja": None,
        "hanjaReading": None,
        "pronunciation": "베 통 투엉 팜",
        "meaningKo": "공장에서 미리 배합하여 레미콘 차량으로 현장에 공급하는 레디믹스트 콘크리트(Ready Mixed Concrete)를 말합니다. 통역 시 '레미콘'은 일본식 콩글리시이므로 베트남어로는 'bê tông thương phẩm' 또는 'bê tông trộn sẵn'으로 표현합니다. 한국에서는 품질이 균일하고 시공이 빠른 레미콘을 주로 사용하지만, 베트남 일부 지역에서는 현장 비빔 콘크리트를 사용하는 경우도 있습니다. 레미콘 주문 시 설계기준강도, 슬럼프, 굵은 골재 최대치수, 배합 시간 등을 명확히 전달해야 합니다.",
        "meaningVi": "Bê tông được trộn sẵn tại nhà máy theo tỷ lệ chuẩn và vận chuyển đến công trường bằng xe bồn trộn (xe trộn bê tông). Đảm bảo chất lượng đồng đều, tiết kiệm thời gian thi công. Khi đặt hàng cần chỉ rõ cường độ thiết kế, độ sụt, cỡ hạt cốt liệu lớn nhất.",
        "context": "콘크리트 타설, 자재 발주",
        "culturalNote": "한국에서는 거의 모든 현장이 레미콘을 사용하며, 배합 신고제로 품질을 관리합니다. 베트남에서는 대도시는 레미콘을 사용하지만 지방은 현장 비빔을 하는 경우가 많아 품질 편차가 큽니다. 레미콘 도착 후 90분 이내 타설 원칙, 슬럼프 테스트 등 한국의 품질 관리 절차를 베트남 현장에도 적용하도록 통역해야 합니다.",
        "commonMistakes": [
            {
                "mistake": "레미콘을 'remicon'으로 그대로 사용",
                "correction": "bê tông thương phẩm 또는 bê tông trộn sẵn",
                "explanation": "'remicon'은 베트남에서 통용되지 않는 일본식 외래어입니다."
            },
            {
                "mistake": "레미콘 차를 'xe bê tông'으로만 표현",
                "correction": "xe bồn trộn bê tông 또는 xe trộn",
                "explanation": "'xe bê tông'은 모호하므로 믹서 트럭임을 명확히 해야 합니다."
            },
            {
                "mistake": "레미콘 공장을 'nhà máy bê tông'으로만 번역",
                "correction": "trạm trộn bê tông 또는 nhà máy sản xuất bê tông thương phẩm",
                "explanation": "레미콘 전용 공장임을 명시해야 합니다."
            }
        ],
        "examples": [
            {
                "ko": "내일 오전 8시에 25MPa 레미콘 50m³를 주문하세요.",
                "vi": "Hãy đặt 50m³ bê tông thương phẩm 25MPa cho 8 giờ sáng mai.",
                "situation": "formal"
            },
            {
                "ko": "레미콘이 도착하면 슬럼프 테스트를 먼저 하세요.",
                "vi": "Khi xe bê tông thương phẩm đến, hãy làm test độ sụt trước.",
                "situation": "onsite"
            },
            {
                "ko": "레미콘 공장에서 배합 시간이 90분 넘었어요.",
                "vi": "Thời gian trộn từ trạm bê tông đã vượt quá 90 phút.",
                "situation": "informal"
            }
        ],
        "relatedTerms": ["be-tong", "tron-be-tong", "do-be-tong", "slump-test"]
    },
    {
        "slug": "slump-test",
        "korean": "슬럼프",
        "vietnamese": "độ sụt",
        "hanja": None,
        "hanjaReading": None,
        "pronunciation": "도 숫",
        "meaningKo": "굳지 않은 콘크리트의 반죽질기를 측정하는 시험으로, 콘크리트의 유동성과 작업성을 나타내는 지표입니다. 통역 시 '슬럼프'는 영어 'slump'에서 온 용어이며 베트남어로는 'độ sụt'로 표현합니다. 슬럼프 값이 크면 유동성이 좋아 타설이 쉽지만 재료 분리 위험이 있고, 작으면 다짐이 어렵습니다. 한국 기준으로 일반 구조물은 80~150mm, 슬래브는 120~180mm 정도의 슬럼프를 사용합니다. 슬럼프 테스트는 레미콘 도착 시 현장에서 반드시 실시해야 하는 품질 관리 필수 항목입니다.",
        "meaningVi": "Thí nghiệm đo độ dẻo, độ chảy của bê tông chưa đông cứng, phản ánh tính lưu động và tính thi công của bê tông. Giá trị độ sụt càng lớn thì bê tông càng lỏng, dễ đổ nhưng có nguy cơ phân tầng vật liệu. Độ sụt tiêu chuẩn cho kết cấu thông thường là 80-150mm, sàn 120-180mm. Phải kiểm tra độ sụt khi xe bê tông đến công trường.",
        "context": "콘크리트 품질 관리",
        "culturalNote": "한국 현장에서는 슬럼프 테스트를 레미콘 도착 시마다 실시하며, 허용 범위를 벗어나면 반품합니다. 베트남에서는 슬럼프 테스트를 생략하거나 형식적으로 하는 경우가 많아, 한국 감리는 반드시 테스트 실시를 요구하고 결과를 기록해야 합니다. 특히 여름철 고온에서는 슬럼프가 빠르게 감소하므로 주의가 필요합니다.",
        "commonMistakes": [
            {
                "mistake": "슬럼프를 'slump'로 그대로 사용",
                "correction": "độ sụt",
                "explanation": "베트남 건설 기준에서는 'độ sụt'이 표준 용어입니다."
            },
            {
                "mistake": "슬럼프 시험을 'thí nghiệm slump'로 표현",
                "correction": "thí nghiệm độ sụt 또는 test độ sụt",
                "explanation": "베트남어 용어를 사용해야 현장에서 정확히 이해합니다."
            },
            {
                "mistake": "슬럼프 값을 'giá trị slump'로 표현",
                "correction": "giá trị độ sụt",
                "explanation": "전문 용어의 일관성을 유지해야 합니다."
            }
        ],
        "examples": [
            {
                "ko": "이 슬래브는 슬럼프 150mm로 주문하세요.",
                "vi": "Sàn này đặt bê tông với độ sụt 150mm.",
                "situation": "formal"
            },
            {
                "ko": "슬럼프가 180mm 넘으면 타설하지 마세요.",
                "vi": "Nếu độ sụt vượt quá 180mm thì không đổ.",
                "situation": "onsite"
            },
            {
                "ko": "지금 슬럼프 테스트 결과가 200mm 나왔습니다.",
                "vi": "Kết quả test độ sụt hiện tại là 200mm.",
                "situation": "informal"
            }
        ],
        "relatedTerms": ["be-tong-thuong-pham", "do-be-tong", "be-tong", "bao-duong-be-tong"]
    },
    {
        "slug": "bao-duong-be-tong",
        "korean": "양생",
        "vietnamese": "bảo dưỡng bê tông",
        "hanja": "養生",
        "hanjaReading": "養(기를 양) + 生(날 생)",
        "pronunciation": "바오 지엉 베 통",
        "meaningKo": "콘크리트 타설 후 일정 기간 동안 적절한 온도와 습도를 유지하여 강도가 충분히 발현되도록 관리하는 작업입니다. 통역 시 '양생'은 베트남어로 'bảo dưỡng'으로 표현하며, 물양생, 막양생, 증기양생 등 방법을 구분해야 합니다. 양생 기간은 보통 7일 이상이며, 초기 24시간이 가장 중요합니다. 양생 불량 시 표면 균열, 강도 저하, 내구성 감소 등 심각한 품질 문제가 발생합니다. 한국 기준으로는 평균기온 5도 이상에서 최소 5일 이상 습윤 양생을 실시해야 합니다.",
        "meaningVi": "Công việc duy trì nhiệt độ và độ ẩm thích hợp trong một thời gian nhất định sau khi đổ bê tông để cường độ phát triển đầy đủ. Có các phương pháp: bảo dưỡng bằng nước, bảo dưỡng bằng màng phủ, bảo dưỡng hơi nước. Thời gian bảo dưỡng tối thiểu 7 ngày, trong đó 24 giờ đầu là quan trọng nhất.",
        "context": "콘크리트 타설 후 관리",
        "culturalNote": "한국에서는 양생을 매우 중요하게 여겨 양생 담당자를 지정하고 일일 점검을 합니다. 베트남 현장에서는 양생을 소홀히 하여 표면 균열이 자주 발생하므로, 통역사는 '양생은 콘크리트 품질의 50%를 결정한다'는 점을 강조해야 합니다. 특히 건기에는 물양생을 하루 3~4회 실시하고, 우기에는 빗물이 콘크리트 표면을 씻어내지 않도록 보호해야 합니다.",
        "commonMistakes": [
            {
                "mistake": "양생을 'nuôi dưỡng'으로 번역",
                "correction": "bảo dưỡng bê tông",
                "explanation": "'nuôi dưỡng'은 생물 양육이므로 콘크리트 양생에는 'bảo dưỡng'을 씁니다."
            },
            {
                "mistake": "물양생을 'tưới nước'로만 표현",
                "correction": "bảo dưỡng bằng nước 또는 tưới nước bảo dưỡng",
                "explanation": "'tưới nước'만으로는 단순 물주기로 오해될 수 있습니다."
            },
            {
                "mistake": "양생 기간을 'thời gian nuôi'로 표현",
                "correction": "thời gian bảo dưỡng",
                "explanation": "콘크리트 전문 용어를 일관되게 사용해야 합니다."
            }
        ],
        "examples": [
            {
                "ko": "콘크리트 타설 후 7일간 물양생을 실시하세요.",
                "vi": "Thực hiện bảo dưỡng bằng nước trong 7 ngày sau khi đổ bê tông.",
                "situation": "formal"
            },
            {
                "ko": "오늘 날씨가 더우니까 양생 물을 자주 뿌려주세요.",
                "vi": "Hôm nay nóng nên hãy tưới nước bảo dưỡng thường xuyên.",
                "situation": "onsite"
            },
            {
                "ko": "양생 불량으로 표면에 균열이 생겼습니다.",
                "vi": "Do bảo dưỡng kém nên bề mặt bị nứt.",
                "situation": "formal"
            }
        ],
        "relatedTerms": ["do-be-tong", "be-tong", "nut-be-tong", "be-tong-thuong-pham"]
    },
    {
        "slug": "laitance",
        "korean": "레이탄스",
        "vietnamese": "màng xi măng nổi",
        "hanja": None,
        "hanjaReading": None,
        "pronunciation": "망 시 망 노이",
        "meaningKo": "콘크리트 타설 후 표면에 떠오르는 시멘트, 미세 골재, 물이 섞인 약한 피막층을 말합니다. 통역 시 '레이탄스'는 프랑스어 'laitance'에서 온 용어이며, 베트남어로는 'màng xi măng nổi' 또는 'váng bê tông'으로 표현합니다. 레이탄스는 강도가 매우 약하고 접착력이 없어, 다음 타설 전에 완전히 제거하지 않으면 층간 분리(콜드조인트)가 발생합니다. 제거 방법은 와이어 브러시, 샌드블라스팅, 치핑 등이 있으며, 젖은 상태에서 제거하는 것이 효과적입니다.",
        "meaningVi": "Lớp màng yếu gồm xi măng, cốt liệu mịn và nước nổi lên trên bề mặt bê tông sau khi đổ. Lớp này có cường độ rất thấp và không có khả năng dính kết, phải loại bỏ hoàn toàn trước khi đổ lớp bê tông tiếp theo để tránh hiện tượng tách lớp. Phương pháp loại bỏ: chổi thép, phun cát, đục bỏ.",
        "context": "콘크리트 타설, 이음 처리",
        "culturalNote": "한국 현장에서는 레이탄스 제거를 필수 공정으로 관리하며, 제거 여부를 검측합니다. 베트남에서는 레이탄스 제거를 생략하는 경우가 많아 층간 접합력이 약해지는 원인이 됩니다. 통역사는 '레이탄스 제거는 구조 일체성 확보의 핵심'임을 강조하고, 다음 타설 전 반드시 제거하도록 지시해야 합니다.",
        "commonMistakes": [
            {
                "mistake": "레이탄스를 'laitance'로 그대로 사용",
                "correction": "màng xi măng nổi 또는 váng bê tông",
                "explanation": "베트남 현장에서는 자국어 표현을 사용해야 이해가 빠릅니다."
            },
            {
                "mistake": "레이탄스 제거를 'làm sạch bề mặt'로만 표현",
                "correction": "loại bỏ màng xi măng nổi",
                "explanation": "단순 청소가 아닌 레이탄스 제거임을 명확히 해야 합니다."
            },
            {
                "mistake": "레이탄스층을 'lớp bê tông yếu'로 표현",
                "correction": "màng xi măng nổi 또는 lớp laitance",
                "explanation": "레이탄스는 콘크리트층이 아닌 피막이므로 구분해야 합니다."
            }
        ],
        "examples": [
            {
                "ko": "다음 층 타설 전에 레이탄스를 완전히 제거하세요.",
                "vi": "Loại bỏ hoàn toàn màng xi măng nổi trước khi đổ lớp tiếp theo.",
                "situation": "formal"
            },
            {
                "ko": "와이어 브러시로 레이탄스를 긁어내세요.",
                "vi": "Dùng chổi thép cạo bỏ màng xi măng nổi.",
                "situation": "onsite"
            },
            {
                "ko": "레이탄스를 제거하지 않으면 접합력이 약해집니다.",
                "vi": "Nếu không loại bỏ màng xi măng nổi thì lực dính kết sẽ yếu.",
                "situation": "formal"
            }
        ],
        "relatedTerms": ["do-be-tong", "be-tong", "noi-be-tong", "mat-bang-thi-cong"]
    },
    {
        "slug": "nut-be-tong",
        "korean": "균열",
        "vietnamese": "nứt bê tông",
        "hanja": "龜裂",
        "hanjaReading": "龜(거북 귀) + 裂(찢을 열)",
        "pronunciation": "눗 베 통",
        "meaningKo": "콘크리트 표면이나 내부에 발생하는 갈라짐 현상으로, 구조적 안전과 내구성에 영향을 미칩니다. 통역 시 '균열'은 베트남어로 'nứt' 또는 'vết nứt'으로 표현하며, 구조 균열과 비구조 균열을 구분해야 합니다. 균열 원인은 건조수축, 온도변화, 과하중, 철근 부식, 침하 등 다양하며, 폭 0.3mm 이상의 균열은 보수가 필요합니다. 균열 발생 시 위치, 방향, 폭, 길이를 기록하고 구조 검토를 실시해야 합니다. 예방을 위해서는 적절한 양생, 신축줄눈 설치, 배근 보강 등이 중요합니다.",
        "meaningVi": "Hiện tượng nứt, rạn trên bề mặt hoặc bên trong bê tông, ảnh hưởng đến an toàn kết cấu và độ bền. Phân biệt vết nứt kết cấu và vết nứt phi kết cấu. Nguyên nhân: co ngót khô, thay đổi nhiệt độ, quá tải, ăn mòn cốt thép, lún. Vết nứt rộng trên 0.3mm cần sửa chữa. Phải ghi nhận vị trí, hướng, độ rộng, chiều dài khi phát hiện vết nứt.",
        "context": "콘크리트 품질 관리, 보수",
        "culturalNote": "한국에서는 균열 발생 시 즉시 보고하고 원인 분석 및 보수 계획을 수립합니다. 베트남에서는 균열을 단순 미관 문제로 치부하는 경향이 있어, 통역사는 '균열은 구조 안전의 경고 신호'임을 강조해야 합니다. 특히 관통 균열이나 사선 균열은 구조적 문제를 시사하므로 즉각 조치가 필요합니다.",
        "commonMistakes": [
            {
                "mistake": "균열을 'khe hở'로 번역",
                "correction": "nứt 또는 vết nứt",
                "explanation": "'khe hở'는 의도된 틈이고, 균열은 'nứt'입니다."
            },
            {
                "mistake": "균열 폭을 'chiều rộng khe nứt'로만 표현",
                "correction": "độ rộng vết nứt",
                "explanation": "'độ rộng vết nứt'이 표준 표현입니다."
            },
            {
                "mistake": "구조 균열을 'nứt kết cấu'로만 표현",
                "correction": "vết nứt kết cấu 또는 nứt nguy hiểm",
                "explanation": "구조적 위험성을 명확히 전달해야 합니다."
            }
        ],
        "examples": [
            {
                "ko": "이 보에 폭 0.5mm의 사선 균열이 발생했습니다.",
                "vi": "Dầm này xuất hiện vết nứt chéo rộng 0.5mm.",
                "situation": "formal"
            },
            {
                "ko": "양생 불량으로 바닥에 균열이 많이 생겼어요.",
                "vi": "Do bảo dưỡng kém nên sàn bị nứt nhiều.",
                "situation": "informal"
            },
            {
                "ko": "균열 폭이 0.3mm를 넘으면 에폭시 주입으로 보수하세요.",
                "vi": "Nếu độ rộng vết nứt vượt quá 0.3mm thì sửa bằng cách bơm epoxy.",
                "situation": "formal"
            }
        ],
        "relatedTerms": ["be-tong", "bao-duong-be-tong", "sua-chua", "kiem-dinh"]
    }
]

existing_slugs = {t['slug'] for t in data}
filtered = [t for t in new_terms if t['slug'] not in existing_slugs]

data.extend(filtered)

with open(file_path, 'w', encoding='utf-8') as f:
    json.dump(data, f, ensure_ascii=False, indent=2)

print(f"Added {len(filtered)} terms. Total: {len(data)}")
