import json
import os

file_path = os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', 'data', 'terms', 'construction.json')

with open(file_path, 'r', encoding='utf-8') as f:
    data = json.load(f)

existing_slugs = {t['slug'] for t in data}

new_terms = [
    {
        "slug": "cot",
        "korean": "기둥",
        "vietnamese": "Cột",
        "hanja": "柱",
        "hanjaReading": "기둥 주(主)",
        "pronunciation": "꼿",
        "difficulty": "basic",
        "category": "건설 구조",
        "meaningKo": "건축물의 수직 하중을 지지하는 수직 구조부재로, 철근콘크리트나 철골로 제작됩니다. 통역 시 주의할 점은 베트남에서는 기둥 단면 크기를 센티미터 단위로 표기하는 반면(예: cột 40x40cm), 한국에서는 밀리미터 단위(예: 400x400mm 기둥)를 사용하므로 단위 환산 실수에 주의해야 합니다. 또한 '대기둥(cột chính)', '소기둥(cột phụ)', '각기둥(cột vuông)', '원기둥(cột tròn)' 등 세부 구분도 정확히 전달해야 합니다.",
        "meaningVi": "Kết cấu thẳng đứng chịu tải trọng của công trình, thường làm bằng bê tông cốt thép hoặc thép. Cột là bộ phận quan trọng trong hệ thống khung chịu lực của tòa nhà.",
        "context": "철근콘크리트 구조에서 기둥은 보와 함께 건물의 뼈대를 형성하며, 상부 하중을 기초로 전달하는 핵심 구조부재입니다.",
        "culturalNote": "한국 건설 현장에서는 기둥 배근 시 '띠철근(đai)', '주철근(cốt thép chính)' 등의 용어를 자주 사용하며, 베트남과 철근 규격 표기법이 다를 수 있습니다. 한국은 D10, D13 등으로 표기하고, 베트남은 Φ10, Φ13 등으로 표기하는 경우가 많습니다. 또한 기둥 시공 시 '거푸집(ván khuôn)', '동바리(giáo)' 등의 가설재 용어도 함께 숙지해야 현장 소통이 원활합니다.",
        "commonMistakes": [
            {
                "mistake": "cột를 pillar로만 번역",
                "correction": "문맥에 따라 column(구조 기둥) 또는 pillar(독립 기둥) 구분",
                "explanation": "column은 구조적 기능이 있는 기둥, pillar는 장식적 또는 독립적 기둥을 의미"
            },
            {
                "mistake": "기둥 크기 단위 혼동 (cm ↔ mm)",
                "correction": "한국은 mm 단위, 베트남은 cm 단위 사용이 일반적",
                "explanation": "도면 검토 시 단위 환산 실수는 치명적 오류 초래"
            },
            {
                "mistake": "대기둥과 소기둥 구분 없이 모두 '기둥'으로만 통역",
                "correction": "cột chính(주기둥), cột phụ(부기둥) 명확히 구분",
                "explanation": "구조적 중요도가 다르므로 구분 필수"
            }
        ],
        "examples": [
            {
                "ko": "1층 기둥은 400x400mm 단면으로 계획되었습니다.",
                "vi": "Cột tầng 1 được thiết kế với tiết diện 40x40cm.",
                "situation": "formal"
            },
            {
                "ko": "이 건물은 철골 기둥과 철근콘크리트 보로 구성됩니다.",
                "vi": "Tòa nhà này kết hợp cột thép và dầm bê tông cốt thép.",
                "situation": "onsite"
            },
            {
                "ko": "기둥 배근 완료 후 콘크리트 타설 진행하겠습니다.",
                "vi": "Sau khi hoàn thành cốt thép cột sẽ tiến hành đổ bê tông.",
                "situation": "informal"
            }
        ],
        "relatedTerms": ["dam", "san", "tuong", "mong", "cot-thep"]
    },
    {
        "slug": "dam",
        "korean": "보",
        "vietnamese": "Dầm",
        "hanja": "樑",
        "hanjaReading": "들보 량(樑)",
        "pronunciation": "담",
        "difficulty": "basic",
        "category": "건설 구조",
        "meaningKo": "기둥과 기둥 사이를 수평으로 연결하여 상부 하중을 지지하고 전달하는 수평 구조부재입니다. 통역 시 주의할 점은 '대보(dầm chính)', '소보(dầm phụ)', '인방보(dầm cửa)', '테두리보(dầm biên)' 등 보의 종류를 정확히 구분해야 하며, 특히 한국에서는 보 치수를 '폭x높이(예: 300x600mm)'로 표기하는 반면 베트nam에서는 때때로 순서가 다를 수 있으므로 도면 확인이 필수입니다. 또한 '연속보', '단순보', '캔틸레버보' 등 구조적 특성에 따른 구분도 중요합니다.",
        "meaningVi": "Kết cấu ngang nối các cột, chịu tải trọng từ sàn và truyền xuống cột. Dầm là bộ phận quan trọng trong hệ khung, có nhiều loại như dầm chính, dầm phụ, dầm biên, dầm cửa.",
        "context": "철근콘크리트 구조에서 보는 슬래브의 하중을 받아 기둥으로 전달하며, 건물의 강성과 안전성을 확보하는 핵심 부재입니다.",
        "culturalNote": "한국 건설 현장에서는 보 시공 시 '상부철근(cốt thép trên)', '하부철근(cốt thép dưới)', '스터럽(đai)' 등의 배근 용어를 자주 사용합니다. 베트남 현장에서는 보 치수를 표기할 때 높이를 먼저 말하는 경우도 있으므로(예: dầm 600x300 = 높이x폭), 도면과 실제 치수를 반드시 교차 확인해야 합니다. 또한 'dầm liên tục(연속보)', 'dầm giản đơn(단순보)' 등 구조 용어도 정확히 전달해야 설계 의도가 왜곡되지 않습니다.",
        "commonMistakes": [
            {
                "mistake": "모든 dầm을 '보'로만 통역",
                "correction": "dầm chính(대보), dầm phụ(소보), dầm biên(테두리보) 등 세부 구분",
                "explanation": "구조적 역할이 다르므로 정확한 구분 필수"
            },
            {
                "mistake": "보 치수의 폭과 높이 순서 혼동",
                "correction": "한국은 일반적으로 '폭x높이' 순서, 베트남은 문맥 확인 필요",
                "explanation": "도면과 실제 시공 치수 불일치 방지"
            },
            {
                "mistake": "beam을 모두 'dầm'으로만 번역",
                "correction": "girder(주형, dầm chính), beam(보, dầm phụ) 구분",
                "explanation": "영문 도면 검토 시 용어 정확성 확보"
            }
        ],
        "examples": [
            {
                "ko": "1층 대보는 400x700mm, 소보는 300x500mm로 설계되었습니다.",
                "vi": "Dầm chính tầng 1 thiết kế 400x700mm, dầm phụ 300x500mm.",
                "situation": "formal"
            },
            {
                "ko": "보 콘크리트 타설 전에 철근 배근 검사 받아야 합니다.",
                "vi": "Trước khi đổ bê tông dầm phải kiểm tra cốt thép.",
                "situation": "onsite"
            },
            {
                "ko": "이 보는 양쪽이 기둥에 고정된 연속보입니다.",
                "vi": "Dầm này là dầm liên tục, hai đầu liên kết với cột.",
                "situation": "informal"
            }
        ],
        "relatedTerms": ["cot", "san", "dam-bien", "dam-cua", "cot-thep"]
    },
    {
        "slug": "san",
        "korean": "슬래브",
        "vietnamese": "Sàn",
        "hanja": None,
        "hanjaReading": None,
        "pronunciation": "산",
        "difficulty": "basic",
        "category": "건설 구조",
        "meaningKo": "건축물의 바닥을 형성하는 수평 판상 구조부재로, 사람이나 물건의 하중을 받아 보나 벽체로 전달합니다. 통역 시 주의할 점은 '일반 슬래브(sàn bê tông thường)', '무량판 슬래브(sàn phẳng không dầm)', '중공 슬래브(sàn rỗng)', '데크 플레이트 슬래브(sàn tôn deck)' 등 슬래브 타입을 명확히 구분해야 하며, 슬래브 두께는 반드시 밀리미터 단위로 확인해야 합니다. 또한 '상부 슬래브(sàn tầng trên)', '지하 슬래브(sàn tầng hầm)', '옥상 슬래브(sàn mái)' 등 위치에 따른 구분도 중요합니다.",
        "meaningVi": "Cấu kiện phẳng ngang tạo nên sàn của công trình, chịu tải trọng sử dụng và truyền xuống dầm hoặc tường. Có nhiều loại như sàn bê tông thường, sàn phẳng, sàn rỗng, sàn tôn deck.",
        "context": "철근콘크리트 구조에서 슬래브는 거주 공간의 바닥을 형성하며, 두께와 배근 방식에 따라 내력과 처짐이 결정됩니다.",
        "culturalNote": "한국 건설 현장에서는 슬래브 두께를 120mm, 150mm, 180mm 등으로 표현하며, 베트남에서도 밀리미터 단위를 사용하지만 구어로는 센티미터를 쓰기도 합니다(예: sàn dày 15cm = 150mm). 슬래브 배근 시 '상부근(cốt thép trên)', '하부근(cốt thép dưới)', '온도철근(cốt thép nhiệt độ)' 등의 용어를 정확히 전달해야 하며, 특히 'phương bố trí cốt thép(배근 방향)'은 구조 안전에 직결되므로 오역에 주의해야 합니다. 또한 한국에서는 '바닥 슬래브'와 '지붕 슬래브'를 명확히 구분하는 반면, 베트남에서는 'sàn'으로 통칭하는 경우가 많으므로 문맥에 따라 'sàn tầng(층 슬래브)' 또는 'sàn mái(지붕 슬래브)'로 구분해야 합니다.",
        "commonMistakes": [
            {
                "mistake": "모든 sàn을 '바닥'으로 통역",
                "correction": "구조적 의미에서는 '슬래브', 마감 의미에서는 '바닥'으로 구분",
                "explanation": "sàn은 구조체, '바닥'은 마감재를 포함하는 개념"
            },
            {
                "mistake": "슬래브 두께를 cm로 통역 (예: 15cm → 15mm 오역)",
                "correction": "도면상 150mm = 15cm이지만, 구조 통역 시 mm 단위 사용 원칙",
                "explanation": "단위 혼동은 시공 오류 초래"
            },
            {
                "mistake": "sàn phẳng을 '평평한 슬래브'로 직역",
                "correction": "무량판 슬래브(flat slab)로 번역",
                "explanation": "기술 용어는 정확한 전문 용어로 번역 필요"
            }
        ],
        "examples": [
            {
                "ko": "이 건물의 표준층 슬래브 두께는 150mm입니다.",
                "vi": "Bản sàn tầng điển hình của tòa nhà này dày 150mm.",
                "situation": "formal"
            },
            {
                "ko": "슬래브 타설 후 양생 기간 최소 7일 필요합니다.",
                "vi": "Sau khi đổ sàn cần bảo dưỡng tối thiểu 7 ngày.",
                "situation": "onsite"
            },
            {
                "ko": "이 구역은 무량판 슬래브로 시공됩니다.",
                "vi": "Khu vực này thi công sàn phẳng không dầm.",
                "situation": "informal"
            }
        ],
        "relatedTerms": ["dam", "cot", "be-tong", "cot-thep", "day-san"]
    },
    {
        "slug": "tuong",
        "korean": "벽체",
        "vietnamese": "Tường",
        "hanja": "壁體",
        "hanjaReading": "벽 벽(壁) + 몸 체(體)",
        "pronunciation": "뚜엉",
        "difficulty": "basic",
        "category": "건설 구조",
        "meaningKo": "건축물의 수직면을 형성하는 구조체로, 하중을 지지하는 내력벽과 공간만 구획하는 비내력벽으로 구분됩니다. 통역 시 주의할 점은 '구조벽(tường kết cấu)', '전단벽(tường chắn)', '칸막이벽(tường ngăn)', '조적벽(tường gạch)', '콘크리트 벽(tường bê tông)' 등을 명확히 구분해야 하며, 특히 내력벽 철거는 구조 안전에 직결되므로 '내력벽(tường chịu lực)'과 '비내력벽(tường không chịu lực)'의 구분이 필수입니다. 벽체 두께도 정확히 전달해야 합니다.",
        "meaningVi": "Bộ phận ngăn cách không gian và chịu lực trong công trình. Tường được chia thành tường chịu lực (có vai trò kết cấu) và tường không chịu lực (chỉ ngăn không gian). Có nhiều loại như tường bê tông, tường gạch, tường panel.",
        "context": "건축 구조에서 벽체는 수직 하중을 지지하거나 지진·바람 등 횡력에 저항하는 구조적 역할과 동시에 공간을 구획하고 방음·단열 기능을 수행합니다.",
        "culturalNote": "한국 건설 현장에서는 벽체 타입을 '콘크리트 벽(tường bê tông)', '조적벽(tường gạch xây)', '경량벽(tường nhẹ, vách thạch cao)' 등으로 구분하며, 베트남에서도 유사하게 분류합니다. 다만 한국에서는 '내력벽'과 '비내력벽'의 구분이 매우 엄격하여 구조 변경 시 설계자 승인이 필수인 반면, 베트남 일부 현장에서는 이 구분이 덜 엄격할 수 있으므로 통역사가 구조 안전의 중요성을 강조해야 합니다. 또한 'tường trọng lực(중력벽)', 'tường cốt lõi(코어월)' 등 고층 건물 특수 용어도 숙지 필요합니다.",
        "commonMistakes": [
            {
                "mistake": "모든 tường을 '벽'으로만 통역",
                "correction": "구조적 문맥에서는 '벽체', 마감 문맥에서는 '벽'으로 구분",
                "explanation": "벽체는 구조체, 벽은 마감 포함 개념"
            },
            {
                "mistake": "내력벽과 비내력벽 구분 없이 통역",
                "correction": "tường chịu lực(내력벽), tường không chịu lực(비내력벽) 명확히 구분",
                "explanation": "내력벽 철거는 구조 붕괴 위험 초래"
            },
            {
                "mistake": "wall을 모두 'tường'으로만 번역",
                "correction": "shear wall(전단벽, tường chắn), curtain wall(커튼월, tường kính) 등 구분",
                "explanation": "벽체 유형에 따라 기능과 시공법이 다름"
            }
        ],
        "examples": [
            {
                "ko": "이 내력벽은 구조체이므로 철거나 개구부 확장이 불가합니다.",
                "vi": "Tường chịu lực này là kết cấu nên không thể phá hoặc mở rộng cửa.",
                "situation": "formal"
            },
            {
                "ko": "전단벽 배근 완료 후 거푸집 설치하겠습니다.",
                "vi": "Sau khi hoàn thành cốt thép tường chắn sẽ lắp ván khuôn.",
                "situation": "onsite"
            },
            {
                "ko": "이 칸막이벽은 비내력벽이라 철거 가능합니다.",
                "vi": "Tường ngăn này là tường không chịu lực nên có thể phá bỏ.",
                "situation": "informal"
            }
        ],
        "relatedTerms": ["tuong-chiu-luc", "tuong-chan", "cot", "dam", "gach"]
    },
    {
        "slug": "tuong-chan",
        "korean": "전단벽",
        "vietnamese": "Tường chắn",
        "hanja": "剪斷壁",
        "hanjaReading": "가위 전(剪) + 끊을 단(斷) + 벽 벽(壁)",
        "pronunciation": "뚜엉 짠",
        "difficulty": "intermediate",
        "category": "건설 구조",
        "meaningKo": "지진이나 바람 등 횡력(수평 방향 힘)에 저항하기 위해 설치되는 구조적 벽체로, 고층 건물에서 필수적인 내진 요소입니다. 통역 시 주의할 점은 '전단벽'은 단순한 '벽'이 아니라 구조적 역할이 명확한 '구조 벽체'임을 강조해야 하며, 'tường chắn' 외에 'tường chịu cắt', 'tường chống cắt' 등으로도 불릴 수 있습니다. 전단벽의 위치와 두께는 구조 설계의 핵심이므로 도면상 표기를 정확히 전달해야 하며, 특히 '코어 전단벽(tường chắn lõi)', '외부 전단벽(tường chắn ngoại vi)' 등 위치에 따른 구분도 중요합니다.",
        "meaningVi": "Tường kết cấu chống lại lực ngang như động đất, gió lớn. Tường chắn là bộ phận quan trọng trong hệ kháng chấn của công trình cao tầng, thường đặt ở lõi thang máy, hành lang hoặc ngoại vi tòa nhà.",
        "context": "고층 건물의 내진 설계에서 전단벽은 기둥-보 시스템과 함께 횡력 저항 시스템을 구성하며, 전단벽의 배치와 크기는 건물의 내진 성능을 결정합니다.",
        "culturalNote": "한국은 지진 설계가 강화되면서 전단벽의 중요성이 커졌으며, '내진 등급', '내진 설계 범주' 등의 용어와 함께 전단벽 설계 기준이 엄격합니다. 베트남도 최근 고층 건물 증가로 전단벽 설계가 중시되고 있으나, 용어가 'tường chắn', 'tường chịu cắt' 등으로 혼용되므로 통역 시 설계자의 의도를 정확히 파악해야 합니다. 또한 전단벽 철근 배근 시 '수평근(cốt thép ngang)', '수직근(cốt thép đứng)', '경계요소(phần tử biên)' 등의 세부 용어도 정확히 전달해야 시공 오류를 방지할 수 있습니다.",
        "commonMistakes": [
            {
                "mistake": "전단벽을 '차단벽' 또는 '방음벽'으로 오역",
                "correction": "tường chắn은 구조적 역할의 '전단벽' (횡력 저항 벽체)",
                "explanation": "전단벽은 내진 설계의 핵심 요소"
            },
            {
                "mistake": "shear wall을 '전단벽'으로만 번역하고 베트남어 설명 생략",
                "correction": "전단벽(tường chắn/tường chịu cắt) + 역할 설명 추가",
                "explanation": "베트남 현장에서 tường chắn 용어가 익숙하지 않을 수 있음"
            },
            {
                "mistake": "전단벽과 일반 내력벽을 혼동",
                "correction": "전단벽은 횡력 저항 특화, 내력벽은 수직 하중 지지가 주 역할",
                "explanation": "구조적 역할과 배근 방식이 다름"
            }
        ],
        "examples": [
            {
                "ko": "이 건물은 코어 전단벽과 외곽 기둥으로 횡력에 저항합니다.",
                "vi": "Tòa nhà này chống lực ngang bằng tường chắn lõi và cột ngoại vi.",
                "situation": "formal"
            },
            {
                "ko": "전단벽 두께는 200mm이고, 이중 배근으로 시공됩니다.",
                "vi": "Tường chắn dày 200mm, thi công bằng cốt thép hai lớp.",
                "situation": "onsite"
            },
            {
                "ko": "지진 하중 계산 시 전단벽 위치가 중요합니다.",
                "vi": "Khi tính toán tải trọng động đất, vị trí tường chắn rất quan trọng.",
                "situation": "informal"
            }
        ],
        "relatedTerms": ["tuong", "cot", "noi-chan", "co-lo-i", "cot-thep"]
    },
    {
        "slug": "console",
        "korean": "캔틸레버",
        "vietnamese": "Console",
        "hanja": None,
        "hanjaReading": None,
        "pronunciation": "꼰솔",
        "difficulty": "intermediate",
        "category": "건설 구조",
        "meaningKo": "한쪽 끝만 지지되고 다른 쪽 끝은 자유단으로 튀어나온 구조 부재로, 발코니나 캐노피, 돌출 슬래브 등에 사용됩니다. 통역 시 주의할 점은 '캔틸레버'는 영어 cantilever의 한국식 발음이며, 베트남어로는 'console', 'dầm thừa', 'sàn thừa', 'kết cấu công xôn' 등으로 불립니다. 캔틸레버 길이와 하중은 구조 안전에 직결되므로 '캔틸레버 길이(chiều dài console)', '캔틸레버 처짐(độ võng console)', '상부 인장철근(cốt thép chịu kéo phía trên)' 등의 용어를 정확히 전달해야 합니다. 특히 캔틸레버는 하부가 아닌 상부에 인장력이 작용하므로 배근 위치가 일반 보와 반대라는 점을 강조해야 합니다.",
        "meaningVi": "Kết cấu công xôn, một đầu cố định và đầu kia tự do, thường dùng cho ban công, mái che, sàn thừa. Console chịu moment âm nên cốt thép chịu kéo ở phía trên, khác với dầm thông thường.",
        "context": "건축 구조에서 캔틸레버는 발코니, 차양, 돌출 지붕 등에 활용되며, 처짐과 진동에 취약하므로 철저한 구조 검토가 필요합니다.",
        "culturalNote": "한국 건설 현장에서는 'cantilever'를 '캔틸레버'로 발음하고, 때로는 '외팔보'로도 부릅니다. 베트남에서는 'console'이 가장 일반적이며, 'dầm console', 'sàn console' 등으로 표현합니다. 통역 시 주의할 점은 캔틸레버의 '자유단(đầu tự do)'과 '고정단(đầu cố định)'을 명확히 구분해야 하며, 특히 '상부근(cốt thép trên)'이 인장철근이라는 점을 강조해야 시공 오류를 방지할 수 있습니다. 한국에서는 캔틸레버 처짐 제한을 엄격히 관리하므로(예: 스팬의 1/250 이하), 이러한 기준도 정확히 전달해야 합니다.",
        "commonMistakes": [
            {
                "mistake": "캔틸레버를 '돌출 슬래브'로만 통역",
                "correction": "구조적 의미에서는 'console' 또는 'kết cấu công xôn'으로 번역",
                "explanation": "캔틸레버는 특정 구조 형식을 의미하는 전문 용어"
            },
            {
                "mistake": "캔틸레버 배근을 일반 보와 동일하게 설명",
                "correction": "캔틸레버는 상부근이 인장철근, 하부근이 압축철근",
                "explanation": "배근 위치 오류는 구조 붕괴 초래"
            },
            {
                "mistake": "console을 '콘솔(받침대)'로만 번역",
                "correction": "문맥에 따라 '캔틸레버(구조)', '받침대(건축 장식)' 구분",
                "explanation": "구조 용어와 건축 용어는 의미가 다름"
            }
        ],
        "examples": [
            {
                "ko": "발코니 캔틸레버는 1.5m 길이로 설계되었습니다.",
                "vi": "Ban công console được thiết kế chiều dài 1.5m.",
                "situation": "formal"
            },
            {
                "ko": "캔틸레버 상부 철근 배근 확인하고 타설 진행하세요.",
                "vi": "Kiểm tra cốt thép phía trên console rồi tiến hành đổ bê tông.",
                "situation": "onsite"
            },
            {
                "ko": "이 캔틸레버는 처짐이 크므로 철근량을 증가시켜야 합니다.",
                "vi": "Console này võng nhiều nên cần tăng lượng cốt thép.",
                "situation": "informal"
            }
        ],
        "relatedTerms": ["dam", "san", "ban-cong", "cot-thep", "momen"]
    },
    {
        "slug": "gia-co",
        "korean": "브라켓",
        "vietnamese": "Giá cố",
        "hanja": None,
        "hanjaReading": None,
        "pronunciation": "자 꼬",
        "difficulty": "intermediate",
        "category": "건설 구조",
        "meaningKo": "구조물에서 보나 선반 등을 지지하기 위해 벽이나 기둥에 부착하는 받침 부재로, 삼각형 또는 L자형 구조입니다. 통역 시 주의할 점은 'bracket'은 베트남어로 'giá cố', 'giá đỡ', 'kẹp', 'bích' 등 다양하게 불릴 수 있으므로 문맥에 따라 정확한 용어를 선택해야 합니다. 구조용 브라켓(giá cố kết cấu)과 건축 마감용 브라켓(giá đỡ trang trí)은 기능이 다르므로 구분이 필수이며, 특히 '보 브라켓(giá cố dầm)', '파이프 브라켓(giá cố ống)', '케이블 브라켓(giá cố cáp)' 등 용도에 따른 세부 구분도 중요합니다.",
        "meaningVi": "Giá đỡ gắn vào tường hoặc cột để chống đỡ dầm, kệ hoặc các thiết bị. Giá cố thường có hình tam giác hoặc chữ L, phân loại theo mục đích: giá cố kết cấu (chịu lực), giá cố thiết bị (đỡ ống, cáp), giá cố trang trí.",
        "context": "건축 및 설비 공사에서 브라켓은 구조물이나 배관, 전선 등을 고정하고 지지하는 데 사용되며, 재질은 강재, 알루미늄, 플라스틱 등 다양합니다.",
        "culturalNote": "한국 건설 현장에서는 'bracket'을 '브라켓'으로 발음하며, 때로는 '받침대', '지지대'로도 부릅니다. 베트남에서는 'giá cố'가 일반적이지만, 설비 공사에서는 'giá đỡ ống(배관 지지대)', 'giá đỡ cáp(케이블 지지대)' 등으로 세분화됩니다. 통역 시 주의할 점은 구조용 브라켓은 하중 계산과 고정 방식이 중요하므로 'khả năng chịu tải(내하중)', 'phương pháp neo(고정 방식)' 등의 정보를 정확히 전달해야 하며, 설비용 브라켓은 간격(khoảng cách giá đỡ)과 재질(chất liệu)을 명확히 해야 합니다.",
        "commonMistakes": [
            {
                "mistake": "모든 bracket을 'giá đỡ'로만 번역",
                "correction": "구조용은 'giá cố', 설비용은 'giá đỡ', 장식용은 'kẹp trang trí' 구분",
                "explanation": "용도에 따라 기능과 시공 방식이 다름"
            },
            {
                "mistake": "bracket을 '브래킷' 그대로 사용",
                "correction": "베트남어 'giá cố' 또는 'giá đỡ'로 번역 후 필요 시 영문 병기",
                "explanation": "베트남 현장에서는 베트남어 용어 사용이 일반적"
            },
            {
                "mistake": "corbel과 bracket을 혼동",
                "correction": "corbel은 콘크리트 구조체의 '받침턱', bracket은 추가 부착 부재",
                "explanation": "구조적 의미와 시공 방식이 다름"
            }
        ],
        "examples": [
            {
                "ko": "이 강철 보는 벽면 브라켓으로 지지됩니다.",
                "vi": "Dầm thép này được đỡ bằng giá cố gắn tường.",
                "situation": "formal"
            },
            {
                "ko": "배관 브라켓은 3m 간격으로 설치하세요.",
                "vi": "Giá đỡ ống lắp cách nhau 3m.",
                "situation": "onsite"
            },
            {
                "ko": "이 브라켓은 하중이 크므로 앵커볼트로 고정해야 합니다.",
                "vi": "Giá cố này chịu tải lớn nên phải dùng neo bulông.",
                "situation": "informal"
            }
        ],
        "relatedTerms": ["dam", "cot", "ong", "cap", "neo"]
    },
    {
        "slug": "dam-cua",
        "korean": "인방보",
        "vietnamese": "Dầm cửa",
        "hanja": "引枋樑",
        "hanjaReading": "끌 인(引) + 모 방(枋) + 들보 량(樑)",
        "pronunciation": "담 꾸어",
        "difficulty": "intermediate",
        "category": "건설 구조",
        "meaningKo": "창문이나 출입문 등 개구부 상부에 설치되어 개구부 위의 벽체와 슬래브 하중을 지지하는 수평 부재입니다. 통역 시 주의할 점은 인방보는 단순한 '문 위 보'가 아니라 구조적 역할이 중요한 부재이므로 'dầm cửa' 외에 'dầm phía trên cửa', 'dầm khánh' 등으로도 불릴 수 있으며, 크기와 배근이 구조 안전에 직결됩니다. 특히 '철근콘크리트 인방보(dầm cửa bê tông cốt thép)'와 '조적조 인방보(dầm cửa gạch)' 또는 '강재 인방보(dầm cửa thép)'를 구분해야 하며, 인방보의 지지 길이(chiều dài gối)도 정확히 전달해야 합니다.",
        "meaningVi": "Dầm ngang phía trên cửa hoặc cửa sổ, chịu tải trọng từ tường và sàn phía trên. Dầm cửa có thể làm bằng bê tông cốt thép, thép hoặc gạch, tùy loại công trình và vị trí cửa.",
        "context": "건축 구조에서 인방보는 개구부로 인해 끊어진 벽체의 하중을 양옆 벽이나 기둥으로 전달하는 역할을 하며, 크기가 작으면 균열이나 처짐이 발생할 수 있습니다.",
        "culturalNote": "한국 건설 현장에서는 '인방보' 또는 '상인방'으로 부르며, 철근콘크리트 구조에서는 일반 보와 함께 타설되거나 조적조에서는 별도로 설치됩니다. 베트남에서는 'dầm cửa'가 일반적이며, 'dầm khánh'은 전통 건축의 인방보를 의미하기도 합니다. 통역 시 주의할 점은 인방보의 지지 길이가 부족하면 개구부 모서리에 균열이 발생하므로 '최소 지지 길이(chiều dài gối tối thiểu)'를 정확히 전달해야 하며, 한국 기준은 개구부 폭의 1/4 이상 또는 최소 200mm입니다. 또한 조적조에서는 'dầm cửa bằng thép góc(앵글 인방보)'도 사용되므로 재질을 명확히 해야 합니다.",
        "commonMistakes": [
            {
                "mistake": "인방보를 '문보' 또는 '문틀'로 오역",
                "correction": "dầm cửa는 구조 부재, '문틀(khung cửa)'은 마감 부재",
                "explanation": "인방보는 하중 지지 역할, 문틀은 문짝 설치용"
            },
            {
                "mistake": "lintel을 'lintơ'로 그대로 음역",
                "correction": "베트남어 'dầm cửa'로 번역",
                "explanation": "베트남 현장에서는 베트남어 용어 사용이 일반적"
            },
            {
                "mistake": "인방보 지지 길이를 간과하고 통역",
                "correction": "개구부 폭과 함께 최소 지지 길이(chiều dài gối) 명시",
                "explanation": "지지 길이 부족 시 균열 발생"
            }
        ],
        "examples": [
            {
                "ko": "출입문 상부 인방보는 200x400mm 크기로 설계되었습니다.",
                "vi": "Dầm cửa phía trên cửa ra vào thiết kế kích thước 200x400mm.",
                "situation": "formal"
            },
            {
                "ko": "인방보 지지 길이는 양쪽 각각 최소 200mm 확보하세요.",
                "vi": "Chiều dài gối dầm cửa mỗi bên tối thiểu 200mm.",
                "situation": "onsite"
            },
            {
                "ko": "이 개구부는 폭이 넓으므로 인방보를 보강해야 합니다.",
                "vi": "Cửa này rộng nên phải tăng cường dầm cửa.",
                "situation": "informal"
            }
        ],
        "relatedTerms": ["dam", "tuong", "cua", "cot-thep", "gach"]
    },
    {
        "slug": "dam-bien",
        "korean": "테두리보",
        "vietnamese": "Dầm biên",
        "hanja": None,
        "hanjaReading": None,
        "pronunciation": "담 비엔",
        "difficulty": "intermediate",
        "category": "건설 구조",
        "meaningKo": "슬래브나 지붕의 가장자리를 따라 설치되어 슬래브 가장자리를 지지하고 보강하는 보로, 외벽선을 따라 배치됩니다. 통역 시 주의할 점은 테두리보는 일반 보와 달리 슬래브 가장자리의 처짐을 방지하고 외벽 하중도 지지하는 이중 역할을 하므로 'dầm biên' 외에 'dầm mép sàn', 'dầm viền' 등으로도 불릴 수 있습니다. 테두리보의 위치(슬래브와 같은 레벨 또는 아래로 돌출)와 단면 크기는 구조 계획에 따라 다르므로 도면을 정확히 확인해야 하며, '내부 보(dầm trong)'와 '테두리보(dầm biên)'의 배근 방식도 다를 수 있습니다.",
        "meaningVi": "Dầm đặt ở mép ngoài của sàn hoặc mái, dọc theo chu vi tòa nhà, có vai trò chống võng mép sàn và chịu tải trọng từ tường ngoài. Dầm biên thường lớn hơn dầm phụ bên trong.",
        "context": "철근콘크리트 구조에서 테두리보는 슬래브의 가장자리를 보강하고, 외벽이나 커튼월의 하중을 받아 기둥으로 전달하며, 건물 외관의 수평선을 형성합니다.",
        "culturalNote": "한국 건설 현장에서는 '테두리보' 또는 '가장자리보'로 부르며, 외벽선을 따라 배치되어 건축과 구조가 긴밀히 연계되는 부재입니다. 베트남에서는 'dầm biên'이 일반적이며, 'dầm viền(테두리)', 'dầm mép(가장자리)'로도 불립니다. 통역 시 주의할 점은 테두리보가 슬래브와 같은 레벨에 숨겨지는 경우('dầm ẩn, 슬래브 내 보')와 슬래브 아래로 돌출되는 경우('dầm nổi, 보 돌출')를 명확히 구분해야 하며, 이는 건축 마감과 천장 높이에 영향을 미칩니다. 또한 테두리보는 외벽 창호 상하부와 만나므로 '인방보'와 혼동하지 않도록 주의해야 합니다.",
        "commonMistakes": [
            {
                "mistake": "테두리보를 '외부 보'로만 통역",
                "correction": "'dầm biên'은 슬래브 가장자리를 따라가는 특정 위치의 보",
                "explanation": "외부 보는 위치만 지칭, 테두리보는 구조적 역할 포함"
            },
            {
                "mistake": "edge beam을 모두 '가장자리 보'로 직역",
                "correction": "'테두리보(dầm biên)'로 번역",
                "explanation": "기술 용어는 정확한 전문 용어로 번역"
            },
            {
                "mistake": "테두리보와 인방보를 혼동",
                "correction": "테두리보는 슬래브 가장자리, 인방보는 개구부 상부",
                "explanation": "위치와 역할이 다름"
            }
        ],
        "examples": [
            {
                "ko": "이 건물의 테두리보는 300x600mm이며, 슬래브와 같은 레벨입니다.",
                "vi": "Dầm biên của tòa nhà này 300x600mm, cùng cao với sàn.",
                "situation": "formal"
            },
            {
                "ko": "테두리보는 커튼월 하중을 지지하므로 보강이 필요합니다.",
                "vi": "Dầm biên chịu tải trọng tường kính nên cần tăng cường.",
                "situation": "onsite"
            },
            {
                "ko": "이 구간은 테두리보가 슬래브 아래로 돌출됩니다.",
                "vi": "Đoạn này dầm biên nhô xuống dưới sàn.",
                "situation": "informal"
            }
        ],
        "relatedTerms": ["dam", "san", "tuong-ngoai", "cot-thep", "cua-so"]
    },
    {
        "slug": "co-lo-i",
        "korean": "코어월",
        "vietnamese": "Cốt lõi",
        "hanja": None,
        "hanjaReading": None,
        "pronunciation": "꼿 러이",
        "difficulty": "advanced",
        "category": "건설 구조",
        "meaningKo": "고층 건물의 중앙부에 위치하여 엘리베이터, 계단, 설비 샤프트 등을 감싸며 건물의 횡력 저항 시스템 역할을 하는 철근콘크리트 벽체 구조입니다. 통역 시 주의할 점은 '코어'는 영어 'core'에서 온 용어로 베트남어로는 'cốt lõi', 'lõi cứng', 'lõi kết cấu' 등으로 불리며, 단순한 '중심부(trung tâm)'가 아니라 구조적 기능을 가진 '구조 코어'임을 강조해야 합니다. 코어월은 '전단벽(tường chắn)'의 일종이지만 위치와 기능이 특수하므로 구분이 필요하며, '코어 내부(bên trong cốt lõi)'는 엘리베이터와 계단실로 구성되고 '코어 벽체(tường cốt lõi)'는 두께와 배근이 일반 벽보다 훨씬 크다는 점을 설명해야 합니다.",
        "meaningVi": "Hệ thống tường kết cấu ở trung tâm tòa nhà cao tầng, bao quanh thang máy, cầu thang, hố kỹ thuật. Cốt lõi là hệ chống xoắn và kháng chấn chính của tòa nhà, thường làm bằng bê tông cốt thép dày.",
        "context": "고층 건물 구조에서 코어월은 엘리베이터와 계단을 담는 서비스 공간이자 지진과 바람에 저항하는 횡력 저항 시스템의 핵심으로, 건물이 높을수록 코어월의 중요성이 커집니다.",
        "culturalNote": "한국 고층 건축에서는 'core wall'을 '코어월' 또는 '코어 구조'로 부르며, 초고층 건물에서는 'outrigger 시스템(아웃리거 시스템)'과 함께 사용됩니다. 베트남에서는 'cốt lõi'가 일반적이며, 'lõi cứng(강성 코어)', 'hệ lõi kết cấu(구조 코어 시스템)' 등으로도 불립니다. 통역 시 주의할 점은 코어월의 두께가 일반 전단벽보다 두꺼우며(예: 300~600mm), 배근도 복잡하므로 '경계요소(phần tử biên)', '연결보(dầm liên kết)' 등 세부 구조 용어를 정확히 전달해야 합니다. 또한 코어 위치는 건물 평면 계획의 핵심이므로 '중앙 코어(cốt lõi trung tâm)', '편심 코어(cốt lõi lệch tâm)' 등의 배치 유형도 구분해야 합니다.",
        "commonMistakes": [
            {
                "mistake": "코어를 '중심부' 또는 '코어(음역)'만으로 통역",
                "correction": "'cốt lõi' 또는 'lõi kết cấu(구조 코어)'로 번역 + 기능 설명",
                "explanation": "코어는 단순 중심부가 아니라 구조 시스템"
            },
            {
                "mistake": "core wall을 '중심 벽'으로 직역",
                "correction": "'tường cốt lõi' 또는 'hệ tường lõi'로 번역",
                "explanation": "기술 용어는 정확한 전문 용어로 번역"
            },
            {
                "mistake": "코어월과 일반 전단벽을 구분 없이 통역",
                "correction": "코어월은 위치(중앙)와 기능(서비스+구조)이 특수한 전단벽 시스템",
                "explanation": "구조 계획과 시공 방식이 다름"
            }
        ],
        "examples": [
            {
                "ko": "이 초고층 건물은 중앙 코어월과 외곽 기둥으로 횡력에 저항합니다.",
                "vi": "Tòa nhà siêu cao tầng này chống lực ngang bằng cốt lõi trung tâm và cột ngoại vi.",
                "situation": "formal"
            },
            {
                "ko": "코어월 두께는 400mm이며, 엘리베이터 4대가 배치됩니다.",
                "vi": "Tường cốt lõi dày 400mm, bố trí 4 thang máy.",
                "situation": "onsite"
            },
            {
                "ko": "코어 내부에 계단실과 설비 샤프트가 있습니다.",
                "vi": "Bên trong cốt lõi có cầu thang và hố kỹ thuật.",
                "situation": "informal"
            }
        ],
        "relatedTerms": ["tuong-chan", "thang-may", "cau-thang", "cao-tang", "cot-thep"]
    }
]

filtered = [t for t in new_terms if t['slug'] not in existing_slugs]
data.extend(filtered)

with open(file_path, 'w', encoding='utf-8') as f:
    json.dump(data, f, ensure_ascii=False, indent=2)

print(f"Added {len(filtered)} terms. Total: {len(data)}")
