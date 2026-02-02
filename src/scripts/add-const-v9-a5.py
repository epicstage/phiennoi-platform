import os
import json

# Tier S 기준: 특수시공법 10개
data = [
    {
        "slug": "kết-cấu-src",
        "korean": "SRC구조",
        "vietnamese": "Kết cấu SRC",
        "hanja": "SRC構造",
        "hanjaReading": "S(에스) + R(알) + C(씨) + 구(지을 구) + 조(얽을 조)",
        "pronunciation": "에스알씨 구조",
        "meaningKo": "SRC(Steel Reinforced Concrete)구조는 철골과 철근콘크리트를 복합적으로 사용한 구조로, H형강 등의 철골을 철근콘크리트로 피복하여 내화성과 강성을 동시에 확보한 공법입니다. 고층건물이나 대형 구조물에서 기둥이나 보에 주로 적용되며, 철골의 시공성과 콘크리트의 내화성을 결합한 하이브리드 구조입니다. 통역 시 'SRC'를 '에스알씨'로 발음하고, 베트남어로는 'Kết cấu SRC' 또는 'Kết cấu thép bọc bê tông cốt thép'으로 구분하여 표현해야 합니다. 현장에서는 '철골철근콘크리트구조' 전체를 말하기보다 'SRC'로 축약하는 경우가 많으므로, 약어 사용에 주의해야 합니다.",
        "meaningVi": "Kết cấu SRC (Steel Reinforced Concrete) là kết cấu kết hợp giữa thép hình và bê tông cốt thép, trong đó thép hình H được bọc bằng bê tông cốt thép để đảm bảo đồng thời tính chịu lửa và độ cứng. Công nghệ này thường được áp dụng cho cột và dầm trong các tòa nhà cao tầng hoặc công trình lớn, kết hợp khả năng thi công của kết cấu thép và tính chịu lửa của bê tông.",
        "context": "고층건물, 대형구조물, 복합건축, 특수구조",
        "culturalNote": "한국에서는 1990년대 이후 고층건물 건설 붐과 함께 SRC구조가 일반화되었으며, 철골구조(S구조)와 철근콘크리트구조(RC구조)의 장점을 결합한 방식으로 인식됩니다. 베트남에서는 최근 고층건물 건설이 증가하면서 SRC공법이 도입되고 있으나, 아직 일반 건축현장에서는 RC구조가 주류를 이루고 있습니다. 한국 현장에서는 'SRC기둥', 'SRC보' 등으로 부위를 명확히 구분하며, 베트남 현장에서는 'cột SRC', 'dầm SRC'로 표현합니다. 통역 시 구조 방식의 차이와 시공 순서(철골 선조립 → 거푸집 → 콘크리트 타설)를 명확히 설명해야 합니다.",
        "commonMistakes": [
            {
                "mistake": "SRC를 'Steel Concrete'로 축약",
                "correction": "'Steel Reinforced Concrete'로 전체 표현",
                "explanation": "RC(Reinforced Concrete)와 혼동될 수 있으므로 'Reinforced'를 생략하지 않아야 함"
            },
            {
                "mistake": "'Kết cấu thép bê tông'으로 단순 번역",
                "correction": "'Kết cấu thép bọc bê tông cốt thép' 또는 'Kết cấu SRC'",
                "explanation": "철골+철근콘크리트 복합구조임을 명확히 표현해야 함"
            },
            {
                "mistake": "CFT구조와 혼동하여 설명",
                "correction": "SRC는 철골을 콘크리트로 피복, CFT는 강관 내부에 콘크리트 충전",
                "explanation": "구조 원리가 완전히 다르므로 명확히 구분 필요"
            }
        ],
        "examples": [
            {
                "ko": "이 건물의 주요 기둥은 SRC구조로 시공합니다.",
                "vi": "Các cột chính của tòa nhà này được thi công bằng kết cấu SRC.",
                "situation": "formal"
            },
            {
                "ko": "SRC 철골 조립 후 철근 배근하고 거푸집 설치하세요.",
                "vi": "Sau khi lắp thép hình SRC, hãy bố trí cốt thép và lắp ván khuôn.",
                "situation": "onsite"
            },
            {
                "ko": "이번 프로젝트는 SRC구조와 RC구조를 혼합 적용합니다.",
                "vi": "Dự án này áp dụng kết hợp kết cấu SRC và kết cấu RC.",
                "situation": "formal"
            }
        ],
        "relatedTerms": ["CFT구조", "철골구조", "철근콘크리트", "복합구조", "내화피복"]
    },
    {
        "slug": "kết-cấu-cft",
        "korean": "CFT구조",
        "vietnamese": "Kết cấu CFT",
        "hanja": "CFT構造",
        "hanjaReading": "C(씨) + F(에프) + T(티) + 구(지을 구) + 조(얽을 조)",
        "pronunciation": "씨에프티 구조",
        "meaningKo": "CFT(Concrete Filled steel Tube)구조는 강관(원형 또는 각형) 내부에 콘크리트를 충전하여 강관과 콘크리트가 일체로 거동하도록 만든 합성구조입니다. 강관이 거푸집 역할을 하므로 별도의 거푸집이 불필요하고, 강관의 구속효과로 콘크리트의 압축강도가 증가하며, 내진성능이 우수합니다. 주로 고층건물 기둥, 교량 교각 등에 적용됩니다. 통역 시 'CFT'를 '씨에프티'로 발음하며, 베트남어로는 'Kết cấu CFT' 또는 'Kết cấu ống thép nhồi bê tông'으로 표현합니다. 현장에서는 '충전', '주입' 등의 용어와 함께 사용되므로 콘크리트 타설 방법을 정확히 전달해야 합니다.",
        "meaningVi": "Kết cấu CFT (Concrete Filled steel Tube) là kết cấu tổ hợp được tạo bằng cách nhồi bê tông vào bên trong ống thép (hình tròn hoặc vuông) để ống thép và bê tông hoạt động đồng nhất. Ống thép đóng vai trò là ván khuôn nên không cần ván khuôn riêng, đồng thời hiệu ứng ràng buộc của ống thép làm tăng cường độ nén của bê tông và khả năng chịu động đất. Công nghệ này chủ yếu được áp dụng cho cột trong các tòa nhà cao tầng và trụ cầu.",
        "context": "고층건물, 교량공사, 내진설계, 합성구조",
        "culturalNote": "한국에서는 2000년대 이후 내진설계 강화와 함께 CFT구조가 고층건물과 교량에서 적극 도입되었습니다. 특히 원형 CFT기둥은 미관과 구조성능을 동시에 만족시켜 건축물의 주요 기둥으로 선호됩니다. 베트남에서는 아직 일반적이지 않으나, 최근 고층건물과 대형 인프라 프로젝트에서 도입이 증가하고 있습니다. 한국 현장에서는 콘크리트 충전 시 '다짐(vibration)' 또는 '자기충전콘크리트(SCC)' 사용 여부가 중요한 이슈이며, 베트남 현장에서는 'đầm(다짐)' 또는 'bê tông tự đầm(자기충전콘크리트)'로 표현합니다. 통역 시 충전 방법과 품질관리 기준을 명확히 전달해야 합니다.",
        "commonMistakes": [
            {
                "mistake": "CFT를 'Steel Tube Concrete'로 순서 변경",
                "correction": "'Concrete Filled steel Tube' 순서 유지",
                "explanation": "콘크리트가 강관 내부에 '충전'되는 구조임을 강조하는 명칭"
            },
            {
                "mistake": "'Ống thép bê tông'으로 단순 번역",
                "correction": "'Ống thép nhồi bê tông' 또는 'Kết cấu CFT'",
                "explanation": "콘크리트가 강관 내부에 '충전(nhồi)'되는 방식임을 명확히 표현"
            },
            {
                "mistake": "SRC구조와 혼동",
                "correction": "CFT는 강관 내부 충전, SRC는 철골 외부 피복",
                "explanation": "콘크리트 위치가 정반대이므로 구분 필수"
            }
        ],
        "examples": [
            {
                "ko": "이 교량 교각은 원형 CFT구조로 설계되었습니다.",
                "vi": "Trụ cầu này được thiết kế bằng kết cấu CFT hình tròn.",
                "situation": "formal"
            },
            {
                "ko": "CFT 강관 조립 완료 후 콘크리트 충전 시작합니다.",
                "vi": "Sau khi lắp ráp ống thép CFT xong, bắt đầu nhồi bê tông.",
                "situation": "onsite"
            },
            {
                "ko": "이번 프로젝트는 각형 CFT기둥을 적용합니다.",
                "vi": "Dự án này áp dụng cột CFT hình vuông.",
                "situation": "formal"
            }
        ],
        "relatedTerms": ["SRC구조", "강관기둥", "충전콘크리트", "합성구조", "내진설계"]
    },
    {
        "slug": "công-nghệ-psc",
        "korean": "PSC공법",
        "vietnamese": "Công nghệ PSC",
        "hanja": "PSC工法",
        "hanjaReading": "P(피) + S(에스) + C(씨) + 공(일할 공) + 법(법 법)",
        "pronunciation": "피에스씨 공법",
        "meaningKo": "PSC(Prestressed Concrete)공법은 콘크리트에 미리 압축응력을 도입하여 인장응력에 취약한 콘크리트의 단점을 보완하는 공법입니다. 긴장재(PC강선, PS강연선)를 사용하여 콘크리트에 압축력을 가하며, 포스트텐션(Post-tension)과 프리텐션(Pre-tension) 방식으로 구분됩니다. 교량, 대형 보, 슬래브 등 장스팬 구조물에 주로 적용되며, 균열 제어와 처짐 최소화에 효과적입니다. 통역 시 'PSC'를 '피에스씨'로 발음하고, 베트nam어로는 'Công nghệ PSC' 또는 'Bê tông ứng suất trước'로 표현합니다. 현장에서는 '긴장', '정착', '그라우팅' 등 전문용어가 자주 사용되므로 정확한 번역이 필요합니다.",
        "meaningVi": "Công nghệ PSC (Prestressed Concrete) là công nghệ bê tông ứng suất trước, trong đó ứng suất nén được đưa vào bê tông trước để bù trừ nhược điểm kém chịu kéo của bê tông. Sử dụng cáp dự ứng lực (dây thép PC, tao thép PS) để tạo lực nén cho bê tông, được phân loại thành phương pháp Post-tension (căng sau) và Pre-tension (căng trước). Công nghệ này chủ yếu được áp dụng cho các công trình nhịp dài như cầu, dầm lớn, sàn, giúp kiểm soát vết nứt và giảm thiểu độ võng hiệu quả.",
        "context": "교량공사, 장스팬구조물, 특수구조, 프리캐스트",
        "culturalNote": "한국에서는 1970년대 고속도로 건설과 함께 PSC공법이 본격 도입되어 현재는 교량 건설의 표준공법으로 자리잡았습니다. 특히 PSC Beam, PSC Box Girder 등이 일반화되었습니다. 베트남에서도 교량 및 고가도로 건설에서 PSC공법이 활발히 적용되고 있으나, 긴장 및 정착 작업의 품질관리가 중요한 이슈입니다. 한국 현장에서는 '긴장력 관리', '정착구 점검', '그라우팅 충전' 등의 용어가 핵심이며, 베트남어로는 'quản lý lực căng', 'kiểm tra neo cố định', 'bơm vữa grouting'으로 표현합니다. 통역 시 긴장 작업 절차와 안전관리 사항을 명확히 전달해야 합니다.",
        "commonMistakes": [
            {
                "mistake": "PSC를 'Pre-Stressed Concrete'만으로 설명",
                "correction": "'Prestressed Concrete'로 통일 (Pre/Post 모두 포함)",
                "explanation": "PSC는 프리텐션과 포스트텐션 모두를 포괄하는 개념"
            },
            {
                "mistake": "'Bê tông căng trước'로 단순 번역",
                "correction": "'Bê tông ứng suất trước' 또는 'Công nghệ PSC'",
                "explanation": "'Pre-tension'만 의미하는 것이 아니므로 'ứng suất trước'가 정확"
            },
            {
                "mistake": "PC와 PSC를 혼동",
                "correction": "PC는 프리캐스트 콘크리트, PSC는 프리스트레스트 콘크리트",
                "explanation": "완전히 다른 개념이므로 명확히 구분 필요"
            }
        ],
        "examples": [
            {
                "ko": "이 교량은 PSC공법으로 시공합니다.",
                "vi": "Cầu này được thi công bằng công nghệ PSC.",
                "situation": "formal"
            },
            {
                "ko": "PSC 긴장 작업 시 긴장력 확인하고 기록하세요.",
                "vi": "Khi thực hiện công việc căng PSC, hãy kiểm tra và ghi lại lực căng.",
                "situation": "onsite"
            },
            {
                "ko": "PSC Box Girder 제작 후 현장으로 운반합니다.",
                "vi": "Sau khi chế tạo PSC Box Girder, vận chuyển đến công trường.",
                "situation": "formal"
            }
        ],
        "relatedTerms": ["포스트텐션", "프리텐션", "긴장재", "정착구", "그라우팅"]
    },
    {
        "slug": "post-tension",
        "korean": "포스트텐션",
        "vietnamese": "Post-tension",
        "hanja": None,
        "hanjaReading": None,
        "pronunciation": "포스트 텐션",
        "meaningKo": "포스트텐션(Post-tension)은 콘크리트 타설 및 양생 후 긴장재(PS강연선)를 긴장하여 콘크리트에 압축응력을 도입하는 PSC공법의 한 방식입니다. 쉬스관(sheath) 내부에 긴장재를 배치하고 콘크리트 타설 후 긴장→정착→그라우팅 순서로 시공합니다. 현장타설 구조물이나 대형 구조물에 적용되며, 프리텐션에 비해 시공 유연성이 높습니다. 통역 시 '포스트텐션'을 'Post-tension' 또는 'căng sau'로 표현하며, '긴장 후(後)' 방식임을 명확히 설명해야 합니다. 긴장력 관리, 정착구 설치, 그라우팅 충전 등 각 단계별 용어를 정확히 구분해야 합니다.",
        "meaningVi": "Post-tension (căng sau) là phương pháp căng cáp dự ứng lực (dây thép PS) sau khi đổ và bảo dưỡng bê tông để đưa ứng suất nén vào bê tông, là một phương thức của công nghệ PSC. Cáp dự ứng lực được bố trí bên trong ống bọc (sheath), sau khi đổ bê tông thực hiện theo thứ tự căng → neo cố định → bơm vữa grouting. Phương pháp này được áp dụng cho kết cấu đổ tại chỗ hoặc công trình lớn, có tính linh hoạt thi công cao hơn so với Pre-tension.",
        "context": "교량공사, 현장타설, 장스팬구조, PSC공법",
        "culturalNote": "한국에서는 현장타설 교량, 대형 건축물의 보 및 슬래브에 포스트텐션 공법이 널리 사용됩니다. 특히 아파트 장스팬 슬래브나 주차장 구조물에서 일반적입니다. 베트남에서도 최근 고층건물과 교량 공사에서 포스트텐션 적용이 증가하고 있으나, 긴장 장비와 숙련 인력 확보가 과제입니다. 한국 현장에서는 '긴장력 확인', '정착구 점검', '그라우팅 충전율 확인' 등이 품질관리의 핵심이며, 베트남어로는 'kiểm tra lực căng', 'kiểm tra neo cố định', 'kiểm tra tỷ lệ bơm vữa grouting'으로 표현합니다. 통역 시 각 단계의 안전 및 품질관리 기준을 명확히 전달해야 합니다.",
        "commonMistakes": [
            {
                "mistake": "'Post-tension'을 '이후 긴장'으로 직역",
                "correction": "'콘크리트 양생 후 긴장' 또는 'căng sau khi bê tông đông cứng'",
                "explanation": "단순 시간 순서가 아니라 콘크리트 양생 완료 후 긴장하는 공법임을 명확히"
            },
            {
                "mistake": "프리텐션과 혼동하여 설명",
                "correction": "포스트텐션은 콘크리트 타설 후 긴장, 프리텐션은 타설 전 긴장",
                "explanation": "긴장 시점이 정반대이므로 반드시 구분"
            },
            {
                "mistake": "'Căng trước'로 잘못 번역",
                "correction": "'Căng sau' 또는 'Post-tension'",
                "explanation": "'căng trước'는 Pre-tension이므로 완전히 반대 의미"
            }
        ],
        "examples": [
            {
                "ko": "이 슬래브는 포스트텐션 공법으로 시공합니다.",
                "vi": "Sàn này được thi công bằng phương pháp Post-tension.",
                "situation": "formal"
            },
            {
                "ko": "포스트텐션 긴장 후 그라우팅 충전하세요.",
                "vi": "Sau khi căng Post-tension, hãy bơm vữa grouting.",
                "situation": "onsite"
            },
            {
                "ko": "포스트텐션 정착구 위치 확인하고 마킹하세요.",
                "vi": "Hãy kiểm tra và đánh dấu vị trí neo cố định Post-tension.",
                "situation": "onsite"
            }
        ],
        "relatedTerms": ["프리텐션", "PSC공법", "긴장재", "정착구", "그라우팅"]
    },
    {
        "slug": "pre-tension",
        "korean": "프리텐션",
        "vietnamese": "Pre-tension",
        "hanja": None,
        "hanjaReading": None,
        "pronunciation": "프리 텐션",
        "meaningKo": "프리텐션(Pre-tension)은 콘크리트 타설 전에 긴장재(PS강연선)를 먼저 긴장하고, 콘크리트를 타설·양생한 후 긴장재를 절단하여 콘크리트에 압축응력을 도입하는 PSC공법의 한 방식입니다. 주로 공장에서 프리캐스트 부재(PC Beam, PC Slab 등)를 제작할 때 적용되며, 긴장대(Tension Bed)에서 대량생산이 가능합니다. 포스트텐션에 비해 정착구가 불필요하고 그라우팅 작업이 없어 시공이 단순하지만, 현장 적용에는 제약이 있습니다. 통역 시 '프리텐션'을 'Pre-tension' 또는 'căng trước'로 표현하며, '긴장 선(先)' 방식임을 명확히 설명해야 합니다.",
        "meaningVi": "Pre-tension (căng trước) là phương pháp căng cáp dự ứng lực (dây thép PS) trước khi đổ bê tông, sau khi đổ và bảo dưỡng bê tông thì cắt cáp để đưa ứng suất nén vào bê tông, là một phương thức của công nghệ PSC. Chủ yếu được áp dụng khi chế tạo cấu kiện precast (PC Beam, PC Slab, v.v.) tại nhà máy, có thể sản xuất hàng loạt trên giá căng (Tension Bed). So với Post-tension, không cần neo cố định và không có công việc bơm vữa grouting nên thi công đơn giản hơn, nhưng có hạn chế trong việc áp dụng tại hiện trường.",
        "context": "프리캐스트, 공장제작, PSC부재, 대량생산",
        "culturalNote": "한국에서는 프리캐스트 공장에서 프리텐션 방식으로 PC Beam, PC Slab 등을 대량 생산하여 현장에 공급하는 시스템이 확립되어 있습니다. 특히 주차장, 물류창고 등에서 표준화된 PC 부재를 사용하여 공기 단축을 도모합니다. 베트남에서도 프리캐스트 공장이 증가하고 있으나, 한국에 비해 규모와 자동화 수준이 낮은 편입니다. 한국 현장에서는 'PC Beam 설치', 'PC Slab 양중' 등의 표현이 일반적이며, 베트남어로는 'lắp dầm PC', 'cẩu lắp sàn PC'로 표현합니다. 통역 시 프리텐션 제작 과정과 현장 설치 방법을 구분하여 설명해야 합니다.",
        "commonMistakes": [
            {
                "mistake": "'Pre-tension'을 '사전 긴장'으로 직역",
                "correction": "'콘크리트 타설 전 긴장' 또는 'căng trước khi đổ bê tông'",
                "explanation": "타설 전 긴장하는 공법임을 명확히 표현"
            },
            {
                "mistake": "포스트텐션과 혼동",
                "correction": "프리텐션은 타설 전 긴장, 포스트텐션은 타설 후 긴장",
                "explanation": "긴장 시점이 정반대이므로 반드시 구분"
            },
            {
                "mistake": "'Căng sau'로 잘못 번역",
                "correction": "'Căng trước' 또는 'Pre-tension'",
                "explanation": "'căng sau'는 Post-tension이므로 완전히 반대 의미"
            }
        ],
        "examples": [
            {
                "ko": "이 PC Beam은 프리텐션 방식으로 제작되었습니다.",
                "vi": "Dầm PC này được chế tạo bằng phương pháp Pre-tension.",
                "situation": "formal"
            },
            {
                "ko": "프리텐션 긴장대에서 PS강연선 긴장 완료했습니다.",
                "vi": "Đã hoàn thành căng dây thép PS trên giá căng Pre-tension.",
                "situation": "onsite"
            },
            {
                "ko": "프리텐션 PC Slab 양중 시 파손 주의하세요.",
                "vi": "Khi cẩu lắp sàn PC Pre-tension, hãy chú ý tránh hư hỏng.",
                "situation": "onsite"
            }
        ],
        "relatedTerms": ["포스트텐션", "PSC공법", "프리캐스트", "PC Beam", "긴장대"]
    },
    {
        "slug": "phương-pháp-segment",
        "korean": "세그먼트공법",
        "vietnamese": "Phương pháp Segment",
        "hanja": None,
        "hanjaReading": None,
        "pronunciation": "세그먼트 공법",
        "meaningKo": "세그먼트공법(Segment Method)은 교량 상부구조를 여러 개의 세그먼트(분절)로 나누어 제작한 후, 현장에서 순차적으로 조립·접합하여 완성하는 공법입니다. 세그먼트는 공장 또는 현장 제작장에서 프리캐스트로 제작되며, 에폭시 접착제와 포스트텐션 긴장재로 접합합니다. MSS(Movable Scaffolding System), FCM(Free Cantilever Method), ILM(Incremental Launching Method) 등과 결합하여 사용되며, 장대교량 시공에 효과적입니다. 통역 시 '세그먼트'를 'Segment' 또는 'khúc đúc sẵn'으로 표현하며, 접합 방식과 조립 순서를 명확히 설명해야 합니다.",
        "meaningVi": "Phương pháp Segment là công nghệ chia kết cấu phần trên của cầu thành nhiều segment (khúc đúc sẵn), sau đó lắp ráp và nối tiếp tuần tự tại hiện trường để hoàn thành. Segment được chế tạo kiểu precast tại nhà máy hoặc khu vực chế tạo hiện trường, được nối bằng keo epoxy và cáp dự ứng lực Post-tension. Công nghệ này được sử dụng kết hợp với MSS (Movable Scaffolding System), FCM (Free Cantilever Method), ILM (Incremental Launching Method), v.v., hiệu quả cho thi công cầu dài.",
        "context": "교량공사, 장대교량, 프리캐스트, 특수공법",
        "culturalNote": "한국에서는 1990년대 이후 장대교량 건설에서 세그먼트공법이 본격 도입되었으며, 인천대교, 영종대교 등 대형 프로젝트에서 적용되었습니다. 세그먼트 제작의 정밀도와 접합 품질이 구조 안전성을 좌우하므로, 품질관리가 매우 엄격합니다. 베트남에서도 주요 교량 프로젝트에서 세그먼트공법이 적용되고 있으나, 세그먼트 제작 및 운반 장비의 확보가 과제입니다. 한국 현장에서는 '세그먼트 매칭(matching)', '에폭시 도포', '포스트텐션 긴장' 등의 용어가 핵심이며, 베트남어로는 'khớp nối segment', 'phủ epoxy', 'căng Post-tension'으로 표현합니다. 통역 시 세그먼트 제작 정밀도와 접합 절차를 명확히 전달해야 합니다.",
        "commonMistakes": [
            {
                "mistake": "'Segment'를 '구간'으로 단순 번역",
                "correction": "'세그먼트' 또는 'khúc đúc sẵn(프리캐스트 분절)'",
                "explanation": "교량 세그먼트는 단순 구간이 아니라 프리캐스트 부재를 의미"
            },
            {
                "mistake": "세그먼트공법과 FCM을 동일하게 설명",
                "correction": "세그먼트공법은 제작 방식, FCM은 조립 방식",
                "explanation": "세그먼트는 부재, FCM은 그것을 조립하는 방법 중 하나"
            },
            {
                "mistake": "'Phương pháp chia đoạn'으로 번역",
                "correction": "'Phương pháp Segment' 또는 'Công nghệ lắp ghép khúc đúc sẵn'",
                "explanation": "단순 분할이 아니라 프리캐스트 제작 후 조립하는 공법임을 명확히"
            }
        ],
        "examples": [
            {
                "ko": "이 교량은 세그먼트공법으로 시공합니다.",
                "vi": "Cầu này được thi công bằng phương pháp Segment.",
                "situation": "formal"
            },
            {
                "ko": "세그먼트 제작장에서 품질 검사 완료 후 현장 운반하세요.",
                "vi": "Sau khi hoàn thành kiểm tra chất lượng tại khu vực chế tạo segment, hãy vận chuyển đến công trường.",
                "situation": "onsite"
            },
            {
                "ko": "세그먼트 접합 시 에폭시 도포 두께 확인하세요.",
                "vi": "Khi nối segment, hãy kiểm tra độ dày lớp phủ epoxy.",
                "situation": "onsite"
            }
        ],
        "relatedTerms": ["FCM공법", "MSS공법", "ILM공법", "프리캐스트", "포스트텐션"]
    },
    {
        "slug": "cầu-giá-tạm",
        "korean": "가설교량",
        "vietnamese": "Cầu giá tạm",
        "hanja": "假設橋梁",
        "hanjaReading": "가(거짓 가) + 설(베풀 설) + 교(다리 교) + 량(들보 량)",
        "pronunciation": "가설교량",
        "meaningKo": "가설교량은 공사 기간 중 임시로 설치하는 교량으로, 공사용 장비·자재 운반, 작업자 통행, 또는 기존 교통 우회를 목적으로 설치됩니다. 강재(H-Beam, I-Beam 등) 또는 조립식 패널로 제작되며, 공사 완료 후 철거됩니다. 가설교량의 설계하중, 안전성, 유지관리가 중요하며, 특히 하천이나 계곡을 횡단하는 경우 홍수 시 유실 방지 대책이 필수입니다. 통역 시 '가설교량'을 'Cầu giá tạm' 또는 'Cầu tạm thời'로 표현하며, '임시(temporary)' 구조물임을 명확히 설명해야 합니다. '가설(架設)'과 혼동하지 않도록 주의가 필요합니다.",
        "meaningVi": "Cầu giá tạm là cầu được lắp đặt tạm thời trong thời gian thi công, nhằm mục đích vận chuyển thiết bị, vật tư công trình, lưu thông của công nhân, hoặc làm đường vòng cho giao thông hiện hữu. Được chế tạo bằng vật liệu thép (H-Beam, I-Beam, v.v.) hoặc tấm lắp ghép, sau khi hoàn thành công trình sẽ tháo dỡ. Tải trọng thiết kế, an toàn và bảo trì của cầu giá tạm rất quan trọng, đặc biệt khi vượt sông hoặc thung lũng cần có biện pháp phòng ngừa trôi mất khi lũ.",
        "context": "교량공사, 임시구조물, 가설공사, 현장안전",
        "culturalNote": "한국에서는 대형 교량 공사나 산간 도로 공사 시 가설교량을 설치하여 공사 기간 중 교통을 우회시키거나 장비를 운반하는 것이 일반적입니다. 특히 하천 횡단 시 홍수기 안전관리가 중요합니다. 베트남에서도 교량 공사 시 가설교량을 설치하나, 우기(mùa mưa)의 급류와 태풍 대비가 핵심 과제입니다. 한국 현장에서는 '가설교량 설치', '가설교량 철거' 등의 표현이 일반적이며, 베트남어로는 'lắp cầu giá tạm', 'tháo dỡ cầu giá tạm'으로 표현합니다. 통역 시 '가설(假設, 임시)'과 '가설(架設, 설치)'을 명확히 구분하여 설명해야 합니다.",
        "commonMistakes": [
            {
                "mistake": "'가설(架設)'과 '가설(假設)' 혼동",
                "correction": "가설교량(假設橋梁)은 임시교량, 가설(架設)은 설치 작업",
                "explanation": "한자가 다르고 의미가 완전히 다르므로 문맥에 따라 구분 필수"
            },
            {
                "mistake": "'Cầu thi công'으로 번역",
                "correction": "'Cầu giá tạm' 또는 'Cầu tạm thời'",
                "explanation": "'thi công'은 시공을 의미하므로 임시 구조물 의미 전달 불충분"
            },
            {
                "mistake": "영구교량과 동일한 안전기준 적용",
                "correction": "가설교량은 임시 구조물로 별도 안전기준 적용",
                "explanation": "사용 기간과 목적이 다르므로 설계·관리 기준 구분 필요"
            }
        ],
        "examples": [
            {
                "ko": "공사 기간 중 교통 우회를 위해 가설교량을 설치합니다.",
                "vi": "Trong thời gian thi công, lắp đặt cầu giá tạm để phân luồng giao thông.",
                "situation": "formal"
            },
            {
                "ko": "가설교량 하중 제한 표지판 설치하세요.",
                "vi": "Hãy lắp biển báo giới hạn tải trọng cho cầu giá tạm.",
                "situation": "onsite"
            },
            {
                "ko": "우기 전에 가설교량 안전점검 완료하세요.",
                "vi": "Hãy hoàn thành kiểm tra an toàn cầu giá tạm trước mùa mưa.",
                "situation": "onsite"
            }
        ],
        "relatedTerms": ["임시구조물", "가설공사", "강재교량", "하중제한", "안전점검"]
    },
    {
        "slug": "phương-pháp-launching",
        "korean": "런칭공법",
        "vietnamese": "Phương pháp Launching",
        "hanja": None,
        "hanjaReading": None,
        "pronunciation": "런칭 공법",
        "meaningKo": "런칭공법(Launching Method)은 교량 상부구조를 제작장에서 제작한 후, 레일이나 이동장치를 이용하여 제작한 구조물을 밀어내거나 당겨서 설치 위치로 이동시키는 공법입니다. ILM(Incremental Launching Method, 압출공법)이 대표적이며, 제작장에서 일정 길이의 세그먼트를 제작하고 순차적으로 밀어내며 조립합니다. 교각 간격이 일정하고 직선 또는 완만한 곡선 교량에 적합하며, 고소작업과 대형 크레인 사용을 최소화할 수 있습니다. 통역 시 '런칭'을 'Launching' 또는 'đẩy tiến(밀어내기)'로 표현하며, 이동 방향과 속도 관리가 중요함을 설명해야 합니다.",
        "meaningVi": "Phương pháp Launching là công nghệ chế tạo kết cấu phần trên của cầu tại khu vực chế tạo, sau đó sử dụng ray hoặc thiết bị di chuyển để đẩy hoặc kéo kết cấu đã chế tạo đến vị trí lắp đặt. ILM (Incremental Launching Method, phương pháp đẩy tiến từng đoạn) là phương pháp tiêu biểu, chế tạo segment có chiều dài nhất định tại khu vực chế tạo và đẩy tiến tuần tự để lắp ráp. Phù hợp với cầu có khoảng cách trụ đồng đều và đường thẳng hoặc đường cong thoải, giúp giảm thiểu tác nghiệp trên cao và sử dụng cần trục lớn.",
        "context": "교량공사, 장대교량, ILM공법, 특수공법",
        "culturalNote": "한국에서는 고속도로 교량이나 도심 고가도로 건설 시 주변 교통에 미치는 영향을 최소화하기 위해 런칭공법을 적극 활용합니다. 특히 교각이 일정 간격으로 배치된 고가도로에서 효과적입니다. 베트남에서도 도시 고가도로나 고속도로 건설에서 런칭공법이 도입되고 있으나, 대형 이동장치(Launching Girder) 확보와 숙련 인력 양성이 과제입니다. 한국 현장에서는 '런칭 속도', '편심 관리', '임시 지지대 설치' 등이 중요한 용어이며, 베트남어로는 'tốc độ đẩy tiến', 'quản lý độ lệch tâm', 'lắp giá đỡ tạm'으로 표현합니다. 통역 시 런칭 방향과 안전관리 사항을 명확히 전달해야 합니다.",
        "commonMistakes": [
            {
                "mistake": "'Launching'을 '발사'로 직역",
                "correction": "'밀어내기' 또는 'đẩy tiến(押進)'",
                "explanation": "교량 구조물을 점진적으로 밀어내는 공법이므로 '발사'는 부적절"
            },
            {
                "mistake": "런칭공법과 ILM을 별개로 설명",
                "correction": "ILM은 런칭공법의 대표적인 방식",
                "explanation": "런칭공법은 포괄 개념, ILM은 그 중 한 방식"
            },
            {
                "mistake": "'Phương pháp phóng'으로 번역",
                "correction": "'Phương pháp Launching' 또는 'Phương pháp đẩy tiến'",
                "explanation": "'phóng'은 발사를 의미하므로 부적절"
            }
        ],
        "examples": [
            {
                "ko": "이 고가도로는 런칭공법으로 시공합니다.",
                "vi": "Cầu vượt này được thi công bằng phương pháp Launching.",
                "situation": "formal"
            },
            {
                "ko": "런칭 작업 시 편심 발생 여부 확인하세요.",
                "vi": "Khi thực hiện công việc Launching, hãy kiểm tra xem có độ lệch tâm hay không.",
                "situation": "onsite"
            },
            {
                "ko": "런칭 속도는 시간당 5m로 제한합니다.",
                "vi": "Tốc độ Launching được giới hạn ở 5m/giờ.",
                "situation": "formal"
            }
        ],
        "relatedTerms": ["ILM공법", "세그먼트공법", "교량가설", "임시지지대", "편심관리"]
    },
    {
        "slug": "phương-pháp-ilm",
        "korean": "ILM공법",
        "vietnamese": "Phương pháp ILM",
        "hanja": "ILM工法",
        "hanjaReading": "I(아이) + L(엘) + M(엠) + 공(일할 공) + 법(법 법)",
        "pronunciation": "아이엘엠 공법",
        "meaningKo": "ILM(Incremental Launching Method)공법은 교량 상부구조를 제작장에서 일정 길이의 세그먼트로 제작한 후, 잭(Jack)을 이용하여 순차적으로 밀어내며 조립하는 런칭공법의 일종입니다. 제작장은 교대 후방에 위치하며, 제작→양생→런칭을 반복하여 전체 교량을 완성합니다. 교각 높이가 높거나 교통량이 많은 구간에서 효과적이며, 고소작업과 대형 크레인 사용을 최소화할 수 있습니다. 통역 시 'ILM'을 '아이엘엠'으로 발음하고, 베트남어로는 'Phương pháp ILM' 또는 'Phương pháp đẩy tiến từng đoạn'으로 표현합니다. '압출공법'이라고도 하며, 제작·런칭·정착의 3단계 순환을 명확히 설명해야 합니다.",
        "meaningVi": "Phương pháp ILM (Incremental Launching Method, phương pháp đẩy tiến từng đoạn) là một loại phương pháp Launching, trong đó kết cấu phần trên của cầu được chế tạo thành các segment có chiều dài nhất định tại khu vực chế tạo, sau đó sử dụng kích (Jack) để đẩy tiến tuần tự và lắp ráp. Khu vực chế tạo nằm phía sau trụ mố, lặp lại quy trình chế tạo → bảo dưỡng → đẩy tiến để hoàn thành toàn bộ cầu. Phương pháp này hiệu quả khi trụ cầu cao hoặc khu vực có lưu lượng giao thông lớn, giúp giảm thiểu tác nghiệp trên cao và sử dụng cần trục lớn.",
        "context": "교량공사, 고가도로, 장대교량, 특수공법",
        "culturalNote": "한국에서는 1980년대부터 고속도로 교량 건설에 ILM공법이 도입되어 현재는 도심 고가도로나 산간 지역 교량에서 널리 사용됩니다. 특히 교각이 높거나 하부 공간 확보가 어려운 구간에서 선호됩니다. 베트남에서도 최근 고가도로와 장대교량 프로젝트에서 ILM공법이 적용되고 있으나, 런칭 장비(Launching Jack)와 제작장 설치가 초기 비용 부담으로 작용합니다. 한국 현장에서는 '런칭 사이클', '임시 받침대', '선단부 보강' 등이 핵심 용어이며, 베트남어로는 'chu kỳ đẩy tiến', 'gối đỡ tạm', 'gia cường đầu mũi'로 표현합니다. 통역 시 제작 → 런칭 → 정착의 순환 과정을 명확히 설명해야 합니다.",
        "commonMistakes": [
            {
                "mistake": "ILM을 'Immediate Launching Method'로 오해",
                "correction": "'Incremental Launching Method'(점진적 압출공법)",
                "explanation": "'Incremental'은 단계적, 점진적을 의미"
            },
            {
                "mistake": "'Phương pháp phóng từng đoạn'으로 번역",
                "correction": "'Phương pháp đẩy tiến từng đoạn' 또는 'Phương pháp ILM'",
                "explanation": "'phóng'은 발사를 의미하므로 부적절, 'đẩy tiến'이 정확"
            },
            {
                "mistake": "FCM과 혼동",
                "correction": "ILM은 후방 제작장에서 밀어냄, FCM은 교각에서 양방향 조립",
                "explanation": "제작 위치와 조립 방향이 완전히 다름"
            }
        ],
        "examples": [
            {
                "ko": "이 교량은 ILM공법으로 시공하여 교통 통제를 최소화합니다.",
                "vi": "Cầu này được thi công bằng phương pháp ILM để giảm thiểu kiểm soát giao thông.",
                "situation": "formal"
            },
            {
                "ko": "ILM 런칭 작업 시 선단부 처짐 확인하세요.",
                "vi": "Khi thực hiện công việc đẩy tiến ILM, hãy kiểm tra độ võng đầu mũi.",
                "situation": "onsite"
            },
            {
                "ko": "ILM 제작장에서 다음 세그먼트 콘크리트 타설 시작합니다.",
                "vi": "Bắt đầu đổ bê tông segment tiếp theo tại khu vực chế tạo ILM.",
                "situation": "onsite"
            }
        ],
        "relatedTerms": ["런칭공법", "세그먼트공법", "압출공법", "임시받침대", "선단부보강"]
    },
    {
        "slug": "phương-pháp-fcm",
        "korean": "FCM공법",
        "vietnamese": "Phương pháp FCM",
        "hanja": "FCM工法",
        "hanjaReading": "F(에프) + C(씨) + M(엠) + 공(일할 공) + 법(법 법)",
        "pronunciation": "에프씨엠 공법",
        "meaningKo": "FCM(Free Cantilever Method)공법은 교량 상부구조를 교각 위에서 양방향으로 캔틸레버(Cantilever, 片持보) 방식으로 조립해 나가는 공법입니다. 세그먼트를 순차적으로 설치하며, 포스트텐션 긴장재로 일체화시킵니다. Form Traveller(이동식 거푸집)를 사용하여 현장타설하거나, 프리캐스트 세그먼트를 크레인으로 설치합니다. 교각이 높거나 하부 공간 확보가 어려운 계곡, 하천 등에서 효과적이며, 가설 비계 없이 시공할 수 있습니다. 통역 시 'FCM'을 '에프씨엠'으로 발음하고, 베트남어로는 'Phương pháp FCM' 또는 'Phương pháp lắp hẫng tự do'로 표현합니다. '캔틸레버(片持)'의 의미를 명확히 설명해야 합니다.",
        "meaningVi": "Phương pháp FCM (Free Cantilever Method) là công nghệ lắp ráp kết cấu phần trên của cầu theo phương pháp cantilever (dầm công xôn, 片持) hai chiều trên trụ cầu. Các segment được lắp đặt tuần tự và liên kết thành một khối bằng cáp dự ứng lực Post-tension. Sử dụng Form Traveller (ván khuôn di động) để đổ tại chỗ hoặc lắp segment precast bằng cần trục. Phương pháp này hiệu quả khi trụ cầu cao hoặc khó đảm bảo không gian phía dưới như thung lũng, sông, có thể thi công mà không cần giàn giáo tạm.",
        "context": "교량공사, 장대교량, 계곡교량, 특수공법",
        "culturalNote": "한국에서는 산간 지역 교량이나 해상교량 건설 시 FCM공법이 널리 사용됩니다. 특히 교각 높이가 50m 이상인 경우 가설 비계 설치가 비경제적이므로 FCM을 선호합니다. 베트남에서도 산악 지역과 메콩델타 지역의 장대교량 건설에서 FCM공법이 적용되고 있으나, Form Traveller 장비 확보와 숙련 인력 양성이 과제입니다. 한국 현장에서는 'Form Traveller 이동', '세그먼트 매칭', '캔틸레버 균형' 등이 핵심 용어이며, 베트남어로는 'di chuyển Form Traveller', 'khớp nối segment', 'cân bằng cantilever'로 표현합니다. 통역 시 양방향 조립과 균형 유지의 중요성을 명확히 설명해야 합니다.",
        "commonMistakes": [
            {
                "mistake": "FCM을 'Fast Construction Method'로 오해",
                "correction": "'Free Cantilever Method'(자유 캔틸레버 공법)",
                "explanation": "'Free'는 자유롭게 돌출된 상태를 의미"
            },
            {
                "mistake": "'Phương pháp công xôn nhanh'으로 번역",
                "correction": "'Phương pháp lắp hẫng tự do' 또는 'Phương pháp FCM'",
                "explanation": "'nhanh(빠른)'는 의미가 없으며, 'lắp hẫng tự do(자유롭게 돌출 조립)'가 정확"
            },
            {
                "mistake": "ILM과 혼동",
                "correction": "FCM은 교각에서 양방향 조립, ILM은 후방에서 밀어냄",
                "explanation": "조립 위치와 방향이 완전히 다름"
            }
        ],
        "examples": [
            {
                "ko": "이 계곡 교량은 FCM공법으로 시공하여 비계를 생략합니다.",
                "vi": "Cầu qua thung lũng này được thi công bằng phương pháp FCM, không cần giàn giáo.",
                "situation": "formal"
            },
            {
                "ko": "FCM 작업 시 양쪽 캔틸레버 중량 균형 확인하세요.",
                "vi": "Khi thực hiện công việc FCM, hãy kiểm tra cân bằng trọng lượng hai bên cantilever.",
                "situation": "onsite"
            },
            {
                "ko": "Form Traveller 이동 전 포스트텐션 긴장 완료하세요.",
                "vi": "Hãy hoàn thành căng Post-tension trước khi di chuyển Form Traveller.",
                "situation": "onsite"
            }
        ],
        "relatedTerms": ["캔틸레버", "세그먼트공법", "Form Traveller", "포스트텐션", "교량가설"]
    }
]

# 파일 저장
output_path = os.path.join(os.path.dirname(__file__), '..', 'data', 'terms', 'construction.json')
with open(output_path, 'r', encoding='utf-8') as f:
    existing_data = json.load(f)

existing_data.extend(data)

with open(output_path, 'w', encoding='utf-8') as f:
    json.dump(existing_data, f, ensure_ascii=False, indent=2)

print(f"✅ {len(data)}개 용어 추가 완료: {output_path}")
