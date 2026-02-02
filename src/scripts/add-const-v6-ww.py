#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
건설 용어 추가 스크립트 v6
테마: 현장 속어/관용어 (일본어 유래 건설 현장 용어)
"""

import json
import os

# 추가할 용어 데이터
new_terms = [
    {
        "slug": "bae-dae",
        "korean": "빼대",
        "vietnamese": "Tháo dỡ cốt pha",
        "hanja": None,
        "hanjaReading": None,
        "pronunciation": "빼대",
        "meaningKo": "거푸집이나 동바리를 해체하여 떼어내는 작업을 의미하는 현장 속어입니다. 일본어 '抜く(ぬく, 빼다)'에서 유래했으며, 정식 용어는 '거푸집 해체' 또는 '탈형'입니다. 통역 시 주의할 점은 베트남 현장에서는 이 속어를 사용하지 않으므로 'tháo dỡ cốt pha' 또는 'tháo ván khuôn'으로 정확히 표현해야 합니다. 작업 안전과 직결되는 공정이므로 오해가 없도록 명확한 표현 사용이 필수입니다.",
        "meaningVi": "Công việc tháo dỡ ván khuôn hoặc giàn giáo sau khi bê tông đông cứng. Là từ lóng công trường có nguồn gốc từ tiếng Nhật '抜く' (nuku - rút ra, tháo ra). Thuật ngữ chính thức là 'tháo dỡ cốt pha' hoặc 'tháo ván khuôn'. Đây là công đoạn quan trọng liên quan trực tiếp đến an toàn nên cần dùng thuật ngữ chính xác khi phiên dịch.",
        "context": "현장 작업 지시, 공정 스케줄 회의",
        "culturalNote": "한국 건설 현장에서는 일본 강점기와 일본 기술 도입 과정에서 유래한 일본어 속어가 여전히 광범위하게 사용됩니다. '빼대'는 그 대표적 사례로, 젊은 세대도 자주 사용하는 용어입니다. 베트남 현장에서는 이런 일본어 유래 속어를 사용하지 않으므로, 통역사는 한국 감독이 '빼대'라고 말할 때 베트남어 정식 용어로 정확히 전달해야 합니다. 또한 한국 현장의 언어 관습을 베트남 직원들에게 설명해주는 것도 문화적 이해를 돕는 데 중요합니다.",
        "commonMistakes": [
            {
                "mistake": "빼대를 베트남어로 직역하려고 시도",
                "correction": "tháo dỡ cốt pha 또는 tháo ván khuôn 사용",
                "explanation": "속어는 직역이 불가능하므로 정식 기술 용어로 번역해야 합니다"
            },
            {
                "mistake": "'bae-dae'를 음차하여 사용",
                "correction": "베트남어 표준 용어로 번역",
                "explanation": "현장 안전을 위해 명확한 표준 용어 사용이 필수입니다"
            },
            {
                "mistake": "탈형 시기를 혼동하여 통역",
                "correction": "콘크리트 양생 기간 확인 후 정확한 시기 전달",
                "explanation": "조기 탈형은 구조 안전에 치명적이므로 정확한 시기 소통이 중요합니다"
            }
        ],
        "examples": [
            {
                "ko": "콘크리트 양생 끝나면 빼대 시작하세요",
                "vi": "Sau khi bê tông đông cứng đủ thời gian, bắt đầu tháo dỡ cốt pha",
                "situation": "onsite"
            },
            {
                "ko": "오늘은 2층 빼대 작업입니다",
                "vi": "Hôm nay là công việc tháo ván khuôn tầng 2",
                "situation": "formal"
            },
            {
                "ko": "빼대 순서 틀리면 위험하니까 조심하세요",
                "vi": "Nếu tháo sai thứ tự sẽ rất nguy hiểm, hãy cẩn thận",
                "situation": "onsite"
            }
        ],
        "relatedTerms": ["거푸집", "탈형", "동바리", "양생", "콘크리트"]
    },
    {
        "slug": "meok-mae-gim",
        "korean": "먹매김",
        "vietnamese": "Đánh dấu bằng먹줄(먹줄 - dây먹)",
        "hanja": None,
        "hanjaReading": None,
        "pronunciation": "먹매김",
        "meaningKo": "건설 현장에서 먹줄(묵줄)을 이용해 기준선을 표시하는 작업입니다. '먹'은 먹물을 뜻하며, '매김'은 표시하다는 의미입니다. 정식 용어는 '기준선 표시' 또는 '묵출(墨出, すみだし)'이지만 현장에서는 '먹매김' 또는 '먹줄치기'라고 부릅니다. 통역 시 주의점은 베트Nam에서 사용하는 기준선 표시 도구와 방법이 다를 수 있으므로, 작업 방법을 구체적으로 설명하면서 통역해야 합니다. 정확한 먹매김은 시공 품질의 기본이므로 오차 범위와 검측 방법도 명확히 전달해야 합니다.",
        "meaningVi": "Công việc đánh dấu đường chuẩn bằng dây먹(dây tẩm먹) trên công trường xây dựng. 먹là먹물(mực), 매김 có nghĩa là đánh dấu. Thuật ngữ chính thức là 'đánh dấu đường chuẩn' nhưng ở công trường Hàn Quốc thường gọi là '먹매김' hoặc '먹줄치기'. Khi phiên dịch cần chú ý rằng công cụ và phương pháp đánh dấu đường chuẩn ở Việt Nam có thể khác nên cần giải thích cụ thể phương pháp làm việc. Đây là cơ sở của chất lượng thi công nên phải truyền đạt rõ ràng về sai số cho phép và phương pháp kiểm tra.",
        "context": "현장 먹선 작업, 측량 후 시공 준비",
        "culturalNote": "먹매김은 동아시아 전통 건축에서 유래한 기술로, 한국·일본·중국에서 공통적으로 사용되던 방법입니다. 현대 건설에서도 레이저 측량 장비가 보편화되었지만, 현장에서는 여전히 먹줄을 사용한 수작업 먹매김이 병행됩니다. 베트남 현장에서는 'dây nước' (물실) 또는 레이저 장비를 더 많이 사용하는 경향이 있으므로, 한국 방식의 먹줄 사용을 처음 접하는 베트남 직원에게는 사용법을 시연하면서 설명하는 것이 효과적입니다.",
        "commonMistakes": [
            {
                "mistake": "먹매김을 단순히 '선 긋기'로 통역",
                "correction": "đánh dấu đường chuẩn bằng dây먹으로 정확히 표현",
                "explanation": "정밀한 기준선 표시 작업이므로 구체적 방법까지 전달해야 합니다"
            },
            {
                "mistake": "먹줄과 수평선(水平線)을 혼동",
                "correction": "먹줄은 수직/수평/경사 모두 가능한 기준선 표시 도구",
                "explanation": "먹줄은 다양한 각도의 기준선을 표시할 수 있습니다"
            },
            {
                "mistake": "허용 오차 범위를 전달하지 않음",
                "correction": "±5mm, ±10mm 등 구체적 허용치 포함하여 통역",
                "explanation": "시공 품질 기준이므로 정확한 수치 전달 필수입니다"
            }
        ],
        "examples": [
            {
                "ko": "벽체 시공 전에 먹매김부터 정확하게 하세요",
                "vi": "Trước khi thi công tường, hãy đánh dấu đường chuẩn bằng dây먹chính xác trước",
                "situation": "onsite"
            },
            {
                "ko": "먹매김 검측 결과 오차가 3mm입니다",
                "vi": "Kết quả kiểm tra đường chuẩn có sai số 3mm",
                "situation": "formal"
            },
            {
                "ko": "바닥 먹줄 다시 쳐야겠어요, 비에 지워졌어요",
                "vi": "Phải đánh lại dây먹trên sàn, đã bị mưa xóa mất rồi",
                "situation": "informal"
            }
        ],
        "relatedTerms": ["먹줄", "기준선", "측량", "묵출", "수평"]
    },
    {
        "slug": "yeon-gang",
        "korean": "연강",
        "vietnamese": "Thép mềm",
        "hanja": "軟鋼",
        "hanjaReading": "軟(부드러울 연) + 鋼(쇠 강)",
        "pronunciation": "연강",
        "meaningKo": "탄소 함유량이 0.25% 이하인 저탄소강으로, 가공이 쉽고 용접성이 우수한 철강재입니다. '연하다(부드럽다)'는 의미에서 유래했으며, 건설 현장에서는 구조재보다는 마감재, 난간, 덕트, 배관 지지대 등에 주로 사용됩니다. 통역 시 주의할 점은 '연강'과 '경강(硬鋼)'을 명확히 구분해야 하며, 구조용 강재와 비구조용 연강재의 용도 차이를 정확히 전달해야 합니다. 특히 안전 난간이나 가설재로 사용할 때는 하중 제한을 명확히 소통해야 합니다.",
        "meaningVi": "Thép carbon thấp với hàm lượng carbon dưới 0.25%, dễ gia công và có khả năng hàn tốt. Có nghĩa là 'thép mềm' (軟鋼). Trên công trường xây dựng chủ yếu sử dụng cho vật liệu hoàn thiện, lan can, ống gió, giá đỡ đường ống hơn là kết cấu chịu lực. Khi phiên dịch cần phân biệt rõ 'thép mềm' (軟鋼) và 'thép cứng' (硬鋼), đồng thời truyền đạt chính xác sự khác biệt trong mục đích sử dụng giữa thép kết cấu và thép mềm phi kết cấu. Đặc biệt khi dùng cho lan can an toàn hoặc giàn giáo tạm thời cần truyền đạt rõ giới hạn tải trọng.",
        "context": "자재 발주, 용접 작업 지시",
        "culturalNote": "한국 건설 현장에서는 '연강'이라는 한자어를 그대로 사용하지만, 젊은 세대 기술자들 중에는 '소프트 스틸(soft steel)' 또는 '마일드 스틸(mild steel)'이라는 영어 표현을 혼용하는 경우도 늘고 있습니다. 베트남에서는 'thép mềm' 또는 'thép carbon thấp'라고 부르며, 국제 규격으로는 SS400, ASTM A36 등이 자주 언급됩니다. 자재 사양서에서 연강을 지정할 때는 인장강도, 항복강도 등 구체적 물성치를 함께 제시하는 것이 오해를 방지합니다.",
        "commonMistakes": [
            {
                "mistake": "연강을 '부드러운 철'로 직역",
                "correction": "thép mềm 또는 thép carbon thấp 사용",
                "explanation": "재료 공학 용어이므로 정식 기술 용어로 번역해야 합니다"
            },
            {
                "mistake": "모든 철강재를 연강으로 통칭",
                "correction": "고장력강, 경강, 스테인리스 등 정확히 구분",
                "explanation": "강재 종류에 따라 용도와 물성이 다르므로 구체적으로 구분해야 합니다"
            },
            {
                "mistake": "연강의 하중 제한을 전달하지 않음",
                "correction": "허용 하중, 항복강도 등 구체적 수치 포함",
                "explanation": "안전과 직결되므로 물성치를 명확히 전달해야 합니다"
            }
        ],
        "examples": [
            {
                "ko": "이 난간은 연강 파이프로 제작합니다",
                "vi": "Lan can này được chế tạo bằng ống thép mềm",
                "situation": "formal"
            },
            {
                "ko": "연강이라서 용접하기 쉬워요",
                "vi": "Vì là thép mềm nên dễ hàn",
                "situation": "onsite"
            },
            {
                "ko": "구조재는 고장력강, 마감재는 연강 사용해주세요",
                "vi": "Vật liệu kết cấu dùng thép cường độ cao, vật liệu hoàn thiện dùng thép mềm",
                "situation": "formal"
            }
        ],
        "relatedTerms": ["경강", "고장력강", "철근", "강재", "용접"]
    },
    {
        "slug": "jap-cheol",
        "korean": "잡철",
        "vietnamese": "Thép phụ, kim loại linh tinh",
        "hanja": None,
        "hanjaReading": None,
        "pronunciation": "잡철",
        "meaningKo": "주요 구조재가 아닌 보조적인 철물이나 금속 부자재를 통칭하는 현장 용어입니다. '잡다한 철물'의 줄임말로, 앵커볼트, 조인트, 브래킷, 행거, 스페이서, 타이 등 다양한 소형 철물류를 포함합니다. 통역 시 주의할 점은 '잡철'이라는 표현이 단순히 '중요하지 않은 철물'이 아니라 '보조적이지만 시공에 필수적인 철물'이라는 의미임을 명확히 해야 합니다. 특히 자재 발주 시 '잡철 일체'라는 표현이 나오면 구체적으로 어떤 품목들이 포함되는지 확인하고 통역해야 합니다.",
        "meaningVi": "Thuật ngữ công trường chỉ các kim loại hoặc vật liệu phụ không phải vật liệu kết cấu chính. Viết tắt của 'kim loại linh tinh', bao gồm nhiều loại kim khí nhỏ như bu lông neo, khớp nối, giá đỡ, móc treo, miếng đệm, dây kẹp v.v. Khi phiên dịch cần chú ý rằng '잡철' không có nghĩa là 'kim loại không quan trọng' mà là 'kim loại phụ trợ nhưng cần thiết cho thi công'. Đặc biệt khi đặt hàng vật liệu có cụm từ '잡철 일체' (toàn bộ잡철) thì phải kiểm tra và phiên dịch cụ thể các mặt hàng nào được bao gồm.",
        "context": "자재 발주, 철골 공사",
        "culturalNote": "한국 건설 현장에서 '잡철'은 매우 광범위하게 사용되는 용어로, 도면에 상세히 표기되지 않은 각종 철물류를 포괄적으로 지칭할 때 자주 쓰입니다. 견적 단계에서 '잡철 일체'라고 표기하면 경험 많은 시공사는 필요한 품목을 알아서 포함시키지만, 경험이 적거나 외국 업체와 협업할 때는 구체적인 품목 리스트가 필요합니다. 베트남 현장에서는 이런 포괄적 용어보다 'phụ kiện kim loại' (금속 부속품) 등 좀 더 구체적인 표현을 선호하므로, 통역 시 주요 품목을 예시로 들어주는 것이 좋습니다.",
        "commonMistakes": [
            {
                "mistake": "'잡철'을 '쓸모없는 철'로 오해",
                "correction": "'보조 철물' 또는 'phụ kiện kim loại'로 정확히 표현",
                "explanation": "중요도가 낮은 것이 아니라 보조적 역할을 하는 필수 부자재입니다"
            },
            {
                "mistake": "'잡철 일체'를 구체적 품목 없이 통역",
                "correction": "포함되는 주요 품목(볼트, 브래킷 등) 예시와 함께 통역",
                "explanation": "포괄적 표현은 오해의 소지가 있으므로 구체적 예시가 필요합니다"
            },
            {
                "mistake": "잡철과 철근(철근콘크리트용)을 혼동",
                "correction": "철근은 '철근(thép cốt)', 잡철은 'kim loại phụ'로 명확히 구분",
                "explanation": "용도와 규격이 완전히 다른 자재이므로 혼동 방지 필수입니다"
            }
        ],
        "examples": [
            {
                "ko": "잡철은 현장에서 필요한 만큼 추가 발주하세요",
                "vi": "Kim loại phụ hãy đặt hàng bổ sung theo nhu cầu tại công trường",
                "situation": "formal"
            },
            {
                "ko": "오늘 잡철 설치 작업입니다",
                "vi": "Hôm nay là công việc lắp đặt các phụ kiện kim loại",
                "situation": "onsite"
            },
            {
                "ko": "잡철 수량 부족한 것 같은데 확인해보세요",
                "vi": "Có vẻ như số lượng kim loại phụ không đủ, hãy kiểm tra lại",
                "situation": "informal"
            }
        ],
        "relatedTerms": ["앵커볼트", "브래킷", "철골", "부속자재", "타이"]
    },
    {
        "slug": "hu-rae-sing",
        "korean": "후레싱",
        "vietnamese": "Lót chống thấm (flashing)",
        "hanja": None,
        "hanjaReading": None,
        "pronunciation": "후레싱",
        "meaningKo": "건축물의 지붕, 벽체 접합부, 창호 주변 등에 설치하여 빗물 침투를 방지하는 판금 또는 방수 부자재를 의미하는 현장 용어입니다. 영어 'flashing'을 일본식으로 발음한 것이 한국 현장에 정착된 경우로, 정식 용어는 '수장판', '방수판', '홈통' 등이지만 현장에서는 '후레싱'이 더 널리 사용됩니다. 통역 시 주의할 점은 베트Nam에서는 'lót chống thấm' 또는 'tấm kim loại chống thấm'으로 정확히 표현해야 하며, 설치 위치(지붕, 벽, 창호 등)에 따라 구체적으로 설명해야 합니다.",
        "meaningVi": "Thuật ngữ công trường chỉ tấm kim loại hoặc vật liệu chống thấm được lắp đặt tại mái nhà, mối nối tường, xung quanh cửa sổ để ngăn nước mưa thấm vào. Phát âm theo kiểu Nhật Bản của từ tiếng Anh 'flashing' đã ăn sâu vào công trường Hàn Quốc. Thuật ngữ chính thức là '수장판' (tấm chắn), '방수판' (tấm chống thấm), '홈통' (máng nước) nhưng ở công trường '후레싱' được dùng phổ biến hơn. Khi phiên dịch cần chú ý ở Việt Nam phải diễn đạt chính xác là 'lót chống thấm' hoặc 'tấm kim loại chống thấm', và giải thích cụ thể theo vị trí lắp đặt (mái, tường, cửa v.v.).",
        "context": "방수 공사, 지붕 공사, 창호 공사",
        "culturalNote": "후레싱은 일본 건축 용어가 한국 현장에 정착된 대표적 사례입니다. 정식 명칭보다 일본식 발음이 더 널리 쓰이는 이유는 일제강점기와 전후 일본 기술 도입 시기에 형성된 언어 관습 때문입니다. 현대에는 국제 건설 프로젝트가 늘면서 영어 'flashing'을 직접 사용하는 경우도 많아졌습니다. 베트남 현장에서는 이런 일본식 발음 용어를 사용하지 않으므로, 통역사는 'lót chống thấm' 또는 'tấm chắn nước'으로 정확히 번역해야 하며, 필요 시 실물이나 도면을 가리키며 설명하는 것이 효과적입니다.",
        "commonMistakes": [
            {
                "mistake": "'후레싱'을 음차하여 베트남어로 그대로 전달",
                "correction": "lót chống thấm 또는 tấm kim loại chống thấm 사용",
                "explanation": "일본식 외래어는 베트남에서 통하지 않으므로 정식 용어로 번역 필수입니다"
            },
            {
                "mistake": "후레싱과 코킹(caulking)을 혼동",
                "correction": "후레싱은 판금, 코킹은 실런트로 명확히 구분",
                "explanation": "둘 다 방수 목적이지만 재료와 시공법이 완전히 다릅니다"
            },
            {
                "mistake": "설치 위치를 구체적으로 설명하지 않음",
                "correction": "'mái nhà', 'cửa sổ', 'tường' 등 구체적 위치 명시",
                "explanation": "위치에 따라 후레싱 형태와 시공법이 다르므로 명확한 전달 필요합니다"
            }
        ],
        "examples": [
            {
                "ko": "창호 주변 후레싱 설치 확인하세요",
                "vi": "Hãy kiểm tra lắp đặt lót chống thấm xung quanh cửa sổ",
                "situation": "formal"
            },
            {
                "ko": "지붕 후레싱이 헐거워서 물 새요",
                "vi": "Tấm chắn nước mái nhà bị lỏng nên bị dột",
                "situation": "onsite"
            },
            {
                "ko": "후레싱 시공 전에 방수 처리 먼저 하세요",
                "vi": "Trước khi thi công lót chống thấm, hãy xử lý chống thấm trước",
                "situation": "formal"
            }
        ],
        "relatedTerms": ["방수", "판금", "수장판", "코킹", "실런트"]
    },
    {
        "slug": "sa-bo-ri",
        "korean": "사보리",
        "vietnamese": "Lỗ kiểm tra đường ống",
        "hanja": None,
        "hanjaReading": None,
        "pronunciation": "사보리",
        "meaningKo": "배관 시스템에서 막힘이나 누수를 점검하기 위해 설치하는 청소구(cleanout) 또는 점검구를 의미하는 현장 속어입니다. 일본어 'さぼり(태만, 빼먹기)'에서 유래했다는 설과 'sub-hole'의 일본식 발음이라는 설이 있습니다. 정식 용어는 '청소구', '소제구(掃除口)', '점검구'이지만 현장에서는 '사보리'가 압도적으로 많이 사용됩니다. 통역 시 주의할 점은 베트남어로 'lỗ kiểm tra' 또는 'cửa làm sạch đường ống'으로 정확히 표현하고, 점검 주기와 방법도 함께 전달해야 합니다.",
        "meaningVi": "Từ lóng công trường chỉ lỗ làm sạch (cleanout) hoặc lỗ kiểm tra được lắp đặt trong hệ thống đường ống để kiểm tra tắc nghẽn hoặc rò rỉ. Có thuyết cho rằng bắt nguồn từ tiếng Nhật 'さぼり' (sơ suất, bỏ qua) hoặc phát âm kiểu Nhật của 'sub-hole'. Thuật ngữ chính thức là '청소구' (cửa làm sạch), '소제구' (掃除口), '점검구' (cửa kiểm tra) nhưng ở công trường '사보리' được dùng áp đảo. Khi phiên dịch cần chú ý diễn đạt chính xác bằng tiếng Việt là 'lỗ kiểm tra' hoặc 'cửa làm sạch đường ống', đồng thời truyền đạt cả chu kỳ và phương pháp kiểm tra.",
        "context": "배관 공사, 설비 점검",
        "culturalNote": "한국 건설 현장에서 '사보리'는 나이 든 기술자뿐 아니라 젊은 세대도 자연스럽게 사용하는 용어로, 그 어원조차 정확히 모르고 쓰는 경우가 많습니다. 이는 일본 건축 용어가 한국 현장 문화에 얼마나 깊이 뿌리내렸는지를 보여주는 사례입니다. 베트남 현장에서는 이 용어를 전혀 사용하지 않으므로, 통역사는 반드시 'lỗ kiểm tra đường ống' 또는 'cửa làm sạch'으로 정확히 번역해야 하며, 처음 듣는 베트남 직원에게는 실물을 가리키며 설명하는 것이 가장 효과적입니다.",
        "commonMistakes": [
            {
                "mistake": "'사보리'를 음차하여 그대로 전달",
                "correction": "lỗ kiểm tra 또는 cửa làm sạch đường ống 사용",
                "explanation": "일본어 유래 속어는 베트남에서 통하지 않습니다"
            },
            {
                "mistake": "사보리와 배수구를 혼동",
                "correction": "사보리는 점검용, 배수구는 배출용으로 명확히 구분",
                "explanation": "용도가 다른 별개의 설비입니다"
            },
            {
                "mistake": "점검 위치와 방법을 설명하지 않음",
                "correction": "위치, 점검 주기, 청소 방법 구체적으로 전달",
                "explanation": "유지보수를 위해 구체적 정보 전달이 필수입니다"
            }
        ],
        "examples": [
            {
                "ko": "배수관 사보리 위치 확인하고 청소하세요",
                "vi": "Hãy xác인 vị trí lỗ kiểm tra đường thoát nước và làm sạch",
                "situation": "onsite"
            },
            {
                "ko": "사보리 뚜껑이 없어졌어요",
                "vi": "Nắp lỗ kiểm tra đường ống bị mất rồi",
                "situation": "informal"
            },
            {
                "ko": "사보리를 통해 배관 내부를 점검합니다",
                "vi": "Kiểm tra bên trong đường ống qua lỗ kiểm tra",
                "situation": "formal"
            }
        ],
        "relatedTerms": ["청소구", "점검구", "배관", "배수관", "설비"]
    },
    {
        "slug": "e-ppa",
        "korean": "에빠",
        "vietnamese": "Chống cái (공기압착기)",
        "hanja": None,
        "hanjaReading": None,
        "pronunciation": "에빠",
        "meaningKo": "공기압을 이용한 타격 공구인 에어 해머(air hammer)를 의미하는 현장 속어입니다. 일본어 'エア(air)'의 발음에서 유래한 것으로 추정되며, 콘크리트 파쇄, 타일 제거, 철거 작업 등에 사용됩니다. 정식 명칭은 '공기압 타격기', '에어 해머', '착암기' 등이지만 현장에서는 '에빠', '에어빠찌' 등으로 불립니다. 통역 시 주의할 점은 베트남어로 'máy đục khí nén' (공기압 착암기) 또는 'búa khí nén' (공기압 해머)로 정확히 표현하고, 소음 및 진동 안전 수칙도 함께 전달해야 합니다.",
        "meaningVi": "Từ lóng công trường chỉ máy đục khí nén (air hammer) sử dụng áp lực khí để đập phá. Được cho là bắt nguồn từ phát âm của từ tiếng Nhật 'エア' (air), dùng để phá bê tông, tháo gạch, công việc phá dỡ. Tên chính thức là '공기압 타격기' (máy đập khí nén), '에어 해머' (air hammer), '착암기' (máy khoan đá) nhưng ở công trường gọi là '에빠', '에어빠찌'. Khi phiên dịch cần chú ý diễn đạt chính xác bằng tiếng Việt là 'máy đục khí nén' hoặc 'búa khí nén', đồng thời truyền đạt cả quy tắc an toàn về tiếng ồn và rung động.",
        "context": "철거 작업, 콘크리트 파쇄",
        "culturalNote": "한국 건설 현장에서 '에빠'는 매우 보편적으로 사용되는 속어로, 일본 강점기에 유입된 일본식 발음이 현재까지 이어지고 있습니다. 젊은 기술자들도 정식 명칭보다 이 속어를 더 자주 사용하며, 심지어 장비 대여 업체에서도 '에빠 대여'라는 표현을 쓸 정도로 일상화되어 있습니다. 베트남 현장에서는 이 용어를 전혀 사용하지 않으므로, 통역사는 반드시 'máy đục khí nén'으로 정확히 번역해야 하며, 작업 시 소음과 분진 발생이 많으므로 보호구 착용 지시도 명확히 전달해야 합니다.",
        "commonMistakes": [
            {
                "mistake": "'에빠'를 음차하여 그대로 전달",
                "correction": "máy đục khí nén 또는 búa khí nén 사용",
                "explanation": "일본어 유래 속어는 베트Nam에서 통하지 않습니다"
            },
            {
                "mistake": "에빠와 전동 드릴을 혼동",
                "correction": "에빠는 타격식, 드릴은 회전식으로 명확히 구분",
                "explanation": "작동 원리와 용도가 다른 별개의 공구입니다"
            },
            {
                "mistake": "안전 수칙(소음, 진동, 분진)을 함께 전달하지 않음",
                "correction": "귀마개, 방진 마스크, 장갑 착용 지시 포함",
                "explanation": "고소음·고진동 장비이므로 보호구 착용이 필수입니다"
            }
        ],
        "examples": [
            {
                "ko": "에빠로 콘크리트 파쇄 작업 시작하세요",
                "vi": "Bắt đầu công việc phá bê tông bằng máy đục khí nén",
                "situation": "onsite"
            },
            {
                "ko": "에빠 쓸 때 꼭 귀마개 착용하세요",
                "vi": "Khi dùng búa khí nén nhất định phải đeo nút tai",
                "situation": "onsite"
            },
            {
                "ko": "에빠 대여비는 일당 5만 원입니다",
                "vi": "Phí thuê máy đục khí nén là 50,000 won/ngày",
                "situation": "formal"
            }
        ],
        "relatedTerms": ["착암기", "공기압축기", "콘크리트파쇄", "철거", "타격공구"]
    },
    {
        "slug": "at-sya-ri",
        "korean": "앗샤리",
        "vietnamese": "Nhanh gọn, sạch sẽ",
        "hanja": None,
        "hanjaReading": None,
        "pronunciation": "앗샤리",
        "meaningKo": "작업을 깔끔하고 신속하게 마무리하는 것을 의미하는 현장 속어입니다. 일본어 'あっさり(깔끔하게, 담백하게)'에서 유래했으며, '앗사리'라고도 발음됩니다. '앗샤리하게 끝냈다'는 표현은 작업이 예상보다 빠르고 깨끗하게 완료되었음을 뜻합니다. 통역 시 주의할 점은 이 표현이 '대충' 또는 '날림'이 아니라 '효율적이고 깔끔하게'라는 긍정적 의미임을 명확히 전달해야 합니다. 베트남어로는 'nhanh gọn', 'sạch sẽ', 'gọn gàng'으로 표현할 수 있습니다.",
        "meaningVi": "Từ lóng công trường có nghĩa là hoàn thành công việc một cách gọn gàng và nhanh chóng. Bắt nguồn từ tiếng Nhật 'あっさり' (gọn gàng, thanh đạm), cũng phát âm là '앗사리'. Cụm từ '앗샤리하게 끝냈다' (kết thúc một cách앗샤리) có nghĩa là công việc được hoàn thành nhanh hơn và sạch sẽ hơn dự kiến. Khi phiên dịch cần chú ý rằng cách diễn đạt này không có nghĩa là 'qua loa' hay 'cẩu thả' mà là 'hiệu quả và gọn gàng', là ý nghĩa tích cực. Có thể diễn đạt bằng tiếng Việt là 'nhanh gọn', 'sạch sẽ', 'gọn gàng'.",
        "context": "작업 완료 보고, 현장 평가",
        "culturalNote": "한국 건설 현장에서 '앗샤리'는 작업 품질과 효율성을 모두 칭찬하는 표현으로 자주 사용됩니다. 이 표현은 일본어 어감을 그대로 유지한 채 한국 현장 문화에 자연스럽게 녹아든 사례입니다. 다만 외국인 근로자나 젊은 세대 중에는 이 표현을 처음 듣는 경우도 있어, 문맥에 따라 '깔끔하게', '신속하게', '효율적으로' 등으로 풀어 설명하는 것이 좋습니다. 베트Nam 직원에게는 'nhanh và gọn gàng' (빠르고 깔끔하게)로 번역하되, 칭찬의 뉘앙스를 담아 'làm rất tốt' (아주 잘 했다)를 덧붙이면 의도가 더 명확히 전달됩니다.",
        "commonMistakes": [
            {
                "mistake": "'앗샤리'를 '대충', '빨리만'으로 오해",
                "correction": "'nhanh gọn và sạch sẽ' (빠르고 깔끔하게)로 정확히 표현",
                "explanation": "속도와 품질을 모두 충족한 긍정적 표현입니다"
            },
            {
                "mistake": "'앗샤리'를 음차하여 그대로 전달",
                "correction": "베트남어 'gọn gàng', 'nhanh chóng' 등으로 번역",
                "explanation": "일본어 유래 속어는 번역이 필요합니다"
            },
            {
                "mistake": "칭찬의 뉘앙스를 빼고 중립적으로 통역",
                "correction": "'làm tốt lắm' (잘했어요) 등 긍정적 어조 포함",
                "explanation": "현장 사기 진작을 위해 칭찬의 뉘앙스 전달이 중요합니다"
            }
        ],
        "examples": [
            {
                "ko": "오늘 작업 앗샤리하게 끝났네요",
                "vi": "Hôm nay công việc hoàn thành nhanh gọn và sạch sẽ nhé",
                "situation": "informal"
            },
            {
                "ko": "이 팀은 항상 앗샤리하게 일해요",
                "vi": "Đội này luôn làm việc nhanh gọn và hiệu quả",
                "situation": "formal"
            },
            {
                "ko": "생각보다 앗샤리하게 끝나서 다행이에요",
                "vi": "May mắn là hoàn thành nhanh hơn dự kiến và rất gọn gàng",
                "situation": "informal"
            }
        ],
        "relatedTerms": ["깔끔", "신속", "효율", "완료", "마무리"]
    },
    {
        "slug": "bang-nol-i",
        "korean": "방놀이",
        "vietnamese": "Hoàn thiện nội thất phòng",
        "hanja": None,
        "hanjaReading": None,
        "pronunciation": "방놀이",
        "meaningKo": "건축물 내부의 방(room) 단위로 마감 작업을 진행하는 것을 의미하는 현장 용어입니다. '방'(room)과 '놀이'(작업)의 합성어로, 일본어 '部屋仕事(へやしごと, room work)'의 영향을 받아 형성된 표현으로 추정됩니다. 도배, 장판, 몰딩, 도어 설치 등 실내 마감 공사 전반을 포괄적으로 지칭합니다. 통역 시 주의할 점은 '놀이'가 유희가 아니라 '작업'을 의미하는 현장 용어임을 명확히 하고, 베트Nam어로는 'hoàn thiện nội thất' (내부 마감) 또는 'công việc nội thất từng phòng' (방별 내부 작업)으로 표현해야 합니다.",
        "meaningVi": "Thuật ngữ công trường có nghĩa là tiến hành công việc hoàn thiện theo từng phòng (room) bên trong công trình. Là từ ghép của '방' (phòng) và '놀이' (công việc), được cho là chịu ảnh hưởng của tiếng Nhật '部屋仕事' (へやしごと, room work). Bao gồm toàn bộ công trình hoàn thiện nội thất như dán giấy tường, lát sàn, lắp nẹp, lắp cửa. Khi phiên dịch cần chú ý rằng '놀이' không có nghĩa là 'vui chơi' mà là 'công việc', là thuật ngữ công trường. Nên diễn đạt bằng tiếng Việt là 'hoàn thiện nội thất' hoặc 'công việc nội thất từng phòng'.",
        "context": "내장 공사, 마감 공정",
        "culturalNote": "한국 건설 현장에서 '방놀이'는 오랜 전통을 가진 표현으로, 주로 주거 시설의 내부 마감 단계를 지칭할 때 사용됩니다. '놀이'라는 표현이 들어가지만 실제로는 고도의 기술이 요구되는 전문 작업이며, 숙련된 방놀이 기능공들은 현장에서 높은 대우를 받습니다. 이 표현은 일본 건축 문화의 영향을 받았으며, 현대에도 여전히 통용되고 있습니다. 베트남 현장에서는 이런 포괄적 속어를 사용하지 않으므로, 통역 시에는 'công việc hoàn thiện nội thất'로 번역하되, 구체적으로 어떤 작업들(dán giấy, lát sàn, lắp cửa 등)이 포함되는지 예시를 들어주는 것이 좋습니다.",
        "commonMistakes": [
            {
                "mistake": "'방놀이'를 '방에서 노는 것'으로 오해",
                "correction": "'hoàn thiện nội thất' (내부 마감 작업)로 정확히 표현",
                "explanation": "'놀이'는 작업을 의미하는 현장 용어입니다"
            },
            {
                "mistake": "'방놀이'를 음차하여 그대로 전달",
                "correction": "구체적인 작업 항목(도배, 장판 등)과 함께 설명",
                "explanation": "포괄적 속어는 구체적 작업 내용으로 풀어야 합니다"
            },
            {
                "mistake": "방놀이와 조적 공사를 혼동",
                "correction": "방놀이는 마감 공사, 조적은 구조체 공사로 명확히 구분",
                "explanation": "공정 순서와 작업 내용이 완전히 다릅니다"
            }
        ],
        "examples": [
            {
                "ko": "다음 주부터 방놀이 시작합니다",
                "vi": "Từ tuần sau bắt đầu công việc hoàn thiện nội thất từng phòng",
                "situation": "formal"
            },
            {
                "ko": "방놀이 끝나면 입주 가능해요",
                "vi": "Sau khi hoàn thiện nội thất xong có thể vào ở",
                "situation": "informal"
            },
            {
                "ko": "101호실 방놀이 완료했습니다",
                "vi": "Đã hoàn thành hoàn thiện nội thất phòng 101",
                "situation": "formal"
            }
        ],
        "relatedTerms": ["내장공사", "도배", "장판", "마감", "인테리어"]
    },
    {
        "slug": "deot-but-i-gi",
        "korean": "덧붙이기",
        "vietnamese": "Hàn thêm, bổ sung hàn",
        "hanja": None,
        "hanjaReading": None,
        "pronunciation": "덧붙이기",
        "meaningKo": "용접 작업에서 기존 용접부에 추가로 용접을 하거나, 구조재에 부재를 추가 접합하는 작업을 의미합니다. '덧붙이다'는 순우리말로 '추가하다', '더하다'의 의미이며, 건설 현장에서는 주로 용접 보강, 철근 이음, 구조 보강 등의 맥락에서 사용됩니다. 통역 시 주의할 점은 단순히 '추가'가 아니라 '보강' 또는 '이음'의 의미를 명확히 전달해야 하며, 베트남어로는 'hàn thêm' (추가 용접), 'hàn bổ sung' (보충 용접), 또는 'nối thêm' (추가 접합)으로 표현할 수 있습니다. 구조 안전과 관련된 작업이므로 시공 기준과 검사 방법도 함께 전달해야 합니다.",
        "meaningVi": "Trong công việc hàn, là việc hàn bổ sung vào mối hàn hiện có hoặc nối thêm cấu kiện vào vật liệu kết cấu. '덧붙이다' là từ thuần Hàn có nghĩa là 'bổ sung', 'thêm vào'. Trên công trường xây dựng chủ yếu được dùng trong ngữ cảnh gia cố hàn, nối thép, gia cố kết cấu. Khi phiên dịch cần chú ý không chỉ là 'thêm' đơn thuần mà phải truyền đạt rõ ý nghĩa 'gia cố' hoặc 'nối'. Có thể diễn đạt bằng tiếng Việt là 'hàn thêm', 'hàn bổ sung', hoặc 'nối thêm'. Vì là công việc liên quan đến an toàn kết cấu nên phải truyền đạt cả tiêu chuẩn thi công và phương pháp kiểm tra.",
        "context": "용접 공사, 구조 보강, 철근 이음",
        "culturalNote": "한국 건설 현장에서 '덧붙이기'는 매우 광범위하게 사용되는 표현으로, 용접뿐 아니라 철근 겹이음, 보강재 추가, 마감재 보수 등 다양한 상황에 적용됩니다. 이 표현은 순우리말이므로 일본어 유래 속어들과 달리 한국인에게 매우 자연스럽지만, 외국인에게는 '무엇을 어떻게 덧붙이는지'가 모호할 수 있습니다. 베트남 현장에서는 'hàn thêm', 'nối thêm', 'gia cố' 등 더 구체적인 표현을 선호하므로, 통역 시에는 작업 대상(용접부, 철근, 구조재 등)과 방법(용접, 볼트, 겹이음 등)을 명확히 설명해야 합니다.",
        "commonMistakes": [
            {
                "mistake": "'덧붙이기'를 단순히 '추가'로만 통역",
                "correction": "'hàn bổ sung' (보강 용접) 또는 'nối gia cố' (보강 접합)로 표현",
                "explanation": "구조적 보강 의미가 포함되므로 구체적으로 표현해야 합니다"
            },
            {
                "mistake": "덧붙이기와 임시 용접(가용접)을 혼동",
                "correction": "가용접은 'hàn tạm', 덧붙이기는 'hàn bổ sung'으로 구분",
                "explanation": "임시와 보강은 목적과 품질 기준이 다릅니다"
            },
            {
                "mistake": "검사 기준을 함께 전달하지 않음",
                "correction": "비파괴검사(NDT), 육안검사 등 검사 방법 명시",
                "explanation": "구조 안전을 위해 검사 기준 전달이 필수입니다"
            }
        ],
        "examples": [
            {
                "ko": "용접부가 약해 보이니 덧붙이기 해주세요",
                "vi": "Mối hàn có vẻ yếu nên hãy hàn bổ sung",
                "situation": "onsite"
            },
            {
                "ko": "철근 이음부에 덧붙이기 작업이 필요합니다",
                "vi": "Cần công việc nối thêm tại chỗ nối thép",
                "situation": "formal"
            },
            {
                "ko": "덧붙이기 완료 후 비파괴검사 진행하겠습니다",
                "vi": "Sau khi hoàn thành hàn bổ sung sẽ tiến hành kiểm tra không phá hủy",
                "situation": "formal"
            }
        ],
        "relatedTerms": ["용접", "보강", "이음", "철근", "구조재"]
    }
]

def add_terms_to_construction():
    """construction.json에 신규 용어 추가"""
    file_path = os.path.join(
        os.path.dirname(os.path.dirname(__file__)),
        'data', 'terms', 'construction.json'
    )

    # 기존 데이터 읽기
    with open(file_path, 'r', encoding='utf-8') as f:
        data = json.load(f)

    # 현재 용어 수
    before_count = len(data)

    # 신규 용어 추가
    data.extend(new_terms)

    # 저장
    with open(file_path, 'w', encoding='utf-8') as f:
        json.dump(data, f, ensure_ascii=False, indent=2)

    after_count = len(data)
    print(f"✅ construction.json 업데이트 완료")
    print(f"   이전: {before_count}개 → 이후: {after_count}개 (추가: {after_count - before_count}개)")
    print(f"\n추가된 용어:")
    for term in new_terms:
        print(f"   - {term['korean']} ({term['slug']})")

if __name__ == "__main__":
    add_terms_to_construction()
