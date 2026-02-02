#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Construction v9-a8: 콘크리트 하자/결함 테마 10개 용어 추가
테마: 백화, 들뜸, 박리, 박락, 철근노출, 공극, 콜드조인트, 수축균열, 구조균열, 한중콘크리트
품질: Tier S (90점 이상)
"""

import json
import os

# 추가할 10개 용어 (Tier S 기준)
new_terms = [
    {
        "slug": "bach-hoa-be-tong",
        "korean": "백화",
        "vietnamese": "Bạch hóa bê tông",
        "hanja": "白化",
        "hanjaReading": "흰 백(白) + 될 화(化)",
        "pronunciation": "박화",
        "meaningKo": "콘크리트 표면에 흰색의 탄산칼슘 결정이 석출되어 나타나는 현상. 미관상 문제이지만 구조 안전성과는 무관한 경우가 많습니다. 통역 시 '구조적 문제가 아니다'라는 점을 명확히 전달해야 베트남 발주자가 과도하게 우려하지 않습니다. 시공사와 발주자 간 하자 분쟁의 주요 원인 중 하나이므로, 백화 발생 원인(물, 시멘트 성분)과 보수 방법을 정확히 설명해야 합니다.",
        "meaningVi": "Hiện tượng kết tinh canxi cacbonat màu trắng xuất hiện trên bề mặt bê tông. Thường chỉ ảnh hưởng thẩm mỹ, không ảnh hưởng kết cấu. Cần giải thích rõ nguyên nhân (nước, xi măng) và phương pháp xử lý để tránh tranh chấp với chủ đầu tư.",
        "context": "품질 검사, 하자 협의, 보수 지시",
        "culturalNote": "한국에서는 백화를 '미관상 하자'로 보는 경향이 강하지만, 베트남 발주자는 '시공 불량의 증거'로 인식하는 경우가 많습니다. 한국 기술자는 '구조적으로 문제없다'고 넘어가려 하지만, 베트남 측은 보수 비용 보상을 요구하는 경우가 잦습니다. 통역사는 양측의 기대치 차이를 조율하는 역할을 해야 합니다. 백화 발생 시 '외관 복구 비용은 누가 부담하는가'를 계약서 기준으로 명확히 안내해야 분쟁을 줄일 수 있습니다.",
        "commonMistakes": [
            {
                "mistake": "'백화'를 'trắng xóa'(희게 지우다)로 오역",
                "correction": "'Bạch hóa bê tông' 또는 'hiện tượng phong hóa trắng'",
                "explanation": "'trắng xóa'는 '지우다'는 뜻이므로 콘크리트 현상과 무관"
            },
            {
                "mistake": "'구조적으로 문제없다'를 'không vấn đề gì'로 축약",
                "correction": "'không ảnh hưởng đến kết cấu chịu lực'(하중 구조에 영향 없음)로 구체화",
                "explanation": "베트남 발주자는 '문제없다'는 말을 신뢰하지 않으므로 구조 안전성을 명시"
            },
            {
                "mistake": "백화 원인을 '시공 불량'으로 단정",
                "correction": "'do nước thấm qua bê tông'(물이 콘크리트를 통과하면서 발생)로 중립적 표현",
                "explanation": "시공 책임 여부는 조사 후 판단해야 하므로 원인은 중립적으로 설명"
            }
        ],
        "examples": [
            {
                "ko": "벽면 백화는 미관상 하자이므로 세척 후 도장으로 마감하겠습니다.",
                "vi": "Bạch hóa trên tường chỉ là lỗi thẩm mỹ, sẽ xử lý bằng cách làm sạch và sơn lại bề mặt.",
                "situation": "formal"
            },
            {
                "ko": "백화 발생 원인은 콘크리트 내부 수분이 증발하면서 석회 성분이 표면으로 이동한 것입니다.",
                "vi": "Nguyên nhân bạch hóa là do nước bên trong bê tông bay hơi, kéo theo thành phần vôi ra bề mặt.",
                "situation": "formal"
            },
            {
                "ko": "백화 생겼네. 청소팀한테 닦으라고 해.",
                "vi": "Có bạch hóa rồi. Bảo đội vệ sinh lau đi.",
                "situation": "onsite"
            }
        ],
        "relatedTerms": ["균열", "들뜸", "박리", "표면마감", "하자보수"]
    },
    {
        "slug": "de-tum",
        "korean": "들뜸",
        "vietnamese": "Hiện tượng phồng rộp",
        "hanja": None,
        "hanjaReading": None,
        "pronunciation": "드름",
        "meaningKo": "마감재(타일, 미장재 등)가 콘크리트 기층에서 분리되어 부풀어 오르는 현상. 접착 불량, 양생 불량, 하중 등이 원인입니다. 통역 시 '들뜸'이라는 순우리말을 베트남어로 정확히 전달해야 합니다. 'phồng rộp'(부풀어 오름)이 가장 정확하며, 'bong tróc'(박리)와 구분해야 합니다. 타일 들뜸은 낙하 위험이 있어 즉시 보수가 필요하므로, 긴급성을 강조해야 합니다.",
        "meaningVi": "Hiện tượng lớp hoàn thiện (gạch, vữa) tách khỏi lớp bê tông nền và phồng lên. Nguyên nhân: kết dính kém, dưỡng hộ không đủ, hoặc chịu lực. Cần xử lý ngay nếu là gạch ốp tường để tránh rơi gây nguy hiểm.",
        "context": "마감 검사, 안전 점검, 하자 보고",
        "culturalNote": "한국 현장에서는 타일 들뜸을 '쳐보면 소리로 안다'는 식으로 현장 경험으로 판단하지만, 베트남 발주자는 '과학적 검측'(적외선, 타격음 측정)을 요구하는 경우가 많습니다. 한국 기술자가 '이 정도는 괜찮다'고 넘어가려 하면 베트남 측은 '전수 조사 후 재시공'을 요구할 수 있습니다. 통역사는 들뜸 범위(몇 %)가 허용 기준 내인지 계약서를 근거로 조율해야 합니다.",
        "commonMistakes": [
            {
                "mistake": "'들뜸'을 'nổi lên'(떠오르다)로 직역",
                "correction": "'phồng rộp'(부풀어 오름) 또는 'bong tách'(분리)",
                "explanation": "'nổi lên'은 물체가 떠오르는 것이므로 건축 용어로 부적합"
            },
            {
                "mistake": "들뜸과 박리를 구분 없이 'bong tróc'로 통칭",
                "correction": "들뜸='phồng rộp', 박리='bong tróc'로 구분",
                "explanation": "들뜸은 '부풀어 오름', 박리는 '떨어져 나감'으로 현상이 다름"
            },
            {
                "mistake": "'들뜸 소리 들어봐'를 'nghe tiếng nổi'로 오역",
                "correction": "'gõ nghe âm thanh rỗng'(쳐서 빈 소리 들어봐)로 의역",
                "explanation": "'들뜸 소리'는 타격음 검사를 의미하므로 구체적으로 설명"
            }
        ],
        "examples": [
            {
                "ko": "외벽 타일에서 들뜸이 발견되어 낙하 위험이 있으니 즉시 재시공하겠습니다.",
                "vi": "Phát hiện gạch tường ngoài bị phồng rộp, có nguy cơ rơi, sẽ thi công lại ngay.",
                "situation": "formal"
            },
            {
                "ko": "들뜸 부위를 망치로 타격하여 범위를 확인한 후 절개 보수하겠습니다.",
                "vi": "Sẽ dùng búa gõ kiểm tra phạm vi phồng rộp, sau đó cắt và sửa chữa.",
                "situation": "formal"
            },
            {
                "ko": "여기 소리 이상한데? 들뜬 것 같아.",
                "vi": "Chỗ này nghe âm thanh lạ ấy? Có vẻ bị phồng.",
                "situation": "onsite"
            }
        ],
        "relatedTerms": ["박리", "타일공사", "접착제", "타격음검사", "하자보수"]
    },
    {
        "slug": "boc-ly",
        "korean": "박리",
        "vietnamese": "Bong tróc",
        "hanja": "剝離",
        "hanjaReading": "벗길 박(剝) + 떠날 리(離)",
        "pronunciation": "방니",
        "meaningKo": "콘크리트 표면층이나 마감재가 기층에서 떨어져 나가는 현상. 들뜸보다 진행된 상태로, 표면 일부가 실제로 벗겨집니다. 통역 시 '박리'는 단순 마감 하자가 아니라 구조적 문제의 신호일 수 있음을 강조해야 합니다. 특히 철근 부식으로 인한 피복 콘크리트 박리는 안전 문제이므로 즉시 보수해야 합니다. 베트남 발주자에게 박리 원인(동결융해, 철근 부식 등)을 명확히 설명하지 않으면 '전체 재시공' 요구로 이어질 수 있습니다.",
        "meaningVi": "Hiện tượng lớp bề mặt bê tông hoặc lớp hoàn thiện tách và bong ra khỏi lớp nền. Nghiêm trọng hơn 'phồng rộp', có thể là dấu hiệu của vấn đề kết cấu (ví dụ: thép gỉ). Cần xử lý ngay nếu do gỉ thép để đảm bảo an toàn.",
        "context": "구조 안전 점검, 하자 보고, 보수 설계",
        "culturalNote": "한국에서는 박리를 '표면 보수'로 처리하는 경우가 많지만, 베트남에서는 박리 발생 시 '구조 안전 진단'을 요구하는 경우가 많습니다. 특히 외벽 박리는 낙하 사고로 이어질 수 있어 베트남 안전 규정이 엄격합니다. 한국 기술자가 '이 정도는 미장으로 메우면 된다'고 하면, 베트남 감리는 '구조 전문가 의견서' 제출을 요구할 수 있습니다. 통역사는 박리 원인이 '표면 문제'인지 '구조 문제'인지 구분하여 전달해야 불필요한 분쟁을 막을 수 있습니다.",
        "commonMistakes": [
            {
                "mistake": "'박리'를 'tách ra'(분리되다)로 일반화",
                "correction": "'bong tróc'(박리) - 건축 전문용어 사용",
                "explanation": "'tách ra'는 일상어이므로 기술 문서에서는 'bong tróc' 사용"
            },
            {
                "mistake": "박리 원인을 '시공 불량'으로만 설명",
                "correction": "'do thép gỉ / do đông băng tan băng'(철근 부식/동결융해) 등 구체적 원인 명시",
                "explanation": "원인에 따라 보수 방법이 다르므로 정확한 원인 전달 필수"
            },
            {
                "mistake": "'박리 보수'를 'sơn lại'(재도장)로 단순화",
                "correction": "'xử lý bong tróc + sửa chữa lớp bê tông'(박리 처리 + 콘크리트층 보수)",
                "explanation": "박리는 표면 도장만으로 해결 불가, 구조 보수 필요"
            }
        ],
        "examples": [
            {
                "ko": "기둥 하부에서 피복 콘크리트 박리가 발견되어 철근 부식 여부를 조사하겠습니다.",
                "vi": "Phát hiện bong tróc lớp bê tông bảo vệ ở chân cột, sẽ kiểm tra tình trạng gỉ thép.",
                "situation": "formal"
            },
            {
                "ko": "박리 부위를 완전히 제거한 후 폴리머 시멘트로 단면 복구하겠습니다.",
                "vi": "Sau khi loại bỏ hoàn toàn vùng bong tróc, sẽ phục hồi mặt cắt bằng xi măng polymer.",
                "situation": "formal"
            },
            {
                "ko": "여기 박리 심한데? 망치로 쳐서 다 떨어뜨려.",
                "vi": "Chỗ này bong tróc nặng ấy? Dùng búa gõ bỏ hết ra.",
                "situation": "onsite"
            }
        ],
        "relatedTerms": ["박락", "철근부식", "피복두께", "단면복구", "보수공법"]
    },
    {
        "slug": "bac-lac",
        "korean": "박락",
        "vietnamese": "Bong rộp nặng / Bong vảy",
        "hanja": "剝落",
        "hanjaReading": "벗길 박(剝) + 떨어질 락(落)",
        "pronunciation": "방낙",
        "meaningKo": "박리보다 진행된 상태로, 콘크리트 표면이 큰 면적으로 떨어져 나가거나 덩어리째 탈락하는 현상. 구조 안전에 직접적인 영향을 미칠 수 있어 긴급 보수가 필요합니다. 통역 시 박락은 단순 미관 문제가 아닌 '구조 결함'임을 명확히 전달해야 하며, 철근 노출, 하중 감소 등의 위험성을 강조해야 합니다. 베트남 발주자에게 박락 발생 시 '구조 안전 진단 → 보강 설계 → 보수 시공'의 3단계 프로세스를 설명해야 이해를 도울 수 있습니다.",
        "meaningVi": "Hiện tượng bê tông bong tróc diện tích lớn hoặc rơi từng khối. Nghiêm trọng hơn 'bong tróc', có thể ảnh hưởng trực tiếp đến an toàn kết cấu. Cần kiểm tra kết cấu khẩn cấp và sửa chữa ngay. Thường kèm theo lộ thép, giảm khả năng chịu lực.",
        "context": "구조 안전 진단, 긴급 보수, 사고 조사",
        "culturalNote": "한국에서는 박락 발생 시 '즉시 통행 차단 → 긴급 보수'로 빠르게 대응하지만, 베트남에서는 '안전 진단 보고서 제출 → 당국 승인 → 보수 시공'의 행정 절차가 필요한 경우가 많습니다. 한국 기술자가 '일단 빨리 고치고 보자'는 식으로 접근하면, 베트남 당국으로부터 '무허가 보수'로 제재받을 수 있습니다. 통역사는 긴급성과 절차 준수를 동시에 강조하며, '임시 안전 조치 → 정식 보고 → 본 보수'의 단계를 조율해야 합니다.",
        "commonMistakes": [
            {
                "mistake": "'박락'을 'rơi xuống'(떨어지다)로 일반화",
                "correction": "'bong rộp nặng'(심한 박리) 또는 'bong vảy'(비늘처럼 벗겨짐)",
                "explanation": "'rơi xuống'은 일상어이므로 기술 용어 사용 필요"
            },
            {
                "mistake": "박락과 박리를 구분 없이 'bong tróc'로 통칭",
                "correction": "박리='bong tróc' (표면), 박락='bong rộp nặng' (대면적/구조 위험)",
                "explanation": "박락은 구조 안전 문제이므로 심각도를 구분하여 표현"
            },
            {
                "mistake": "'박락 부위 보수'를 'sửa chữa chỗ bong'으로 단순화",
                "correction": "'kiểm tra kết cấu + gia cố + phục hồi bê tông'(구조 검사 + 보강 + 복구)",
                "explanation": "박락은 구조 보강이 필요한 경우가 많으므로 보수 범위를 명확히"
            }
        ],
        "examples": [
            {
                "ko": "보 하부에서 대면적 박락이 발생하여 철근이 노출되었으니 즉시 구조 안전 진단을 실시하겠습니다.",
                "vi": "Phát hiện bong rộp diện tích lớn ở dưới dầm, thép bị lộ ra, sẽ tiến hành kiểm tra an toàn kết cấu ngay.",
                "situation": "formal"
            },
            {
                "ko": "박락 부위를 망으로 보강한 후 숏크리트 공법으로 단면을 복구하겠습니다.",
                "vi": "Sau khi gia cố vùng bong rộp bằng lưới, sẽ phục hồi mặt cắt bằng công nghệ phun bê tông (shotcrete).",
                "situation": "formal"
            },
            {
                "ko": "천장 박락 위험하니까 여기 출입 금지 표시해.",
                "vi": "Trần bong rộp nguy hiểm, cấm vào khu vực này.",
                "situation": "onsite"
            }
        ],
        "relatedTerms": ["박리", "철근노출", "구조안전진단", "단면복구", "숏크리트"]
    },
    {
        "slug": "thep-lo",
        "korean": "철근 노출",
        "vietnamese": "Thép lộ ra",
        "hanja": "鐵筋露出",
        "hanjaReading": "쇠 철(鐵) + 힘줄 근(筋) + 이슬 로(露) + 날 출(出)",
        "pronunciation": "철근 노출",
        "meaningKo": "콘크리트 피복이 탈락하거나 손상되어 내부 철근이 외부로 드러나는 현상. 철근 부식의 주요 원인이 되며 구조 안전에 직접적인 위험 요소입니다. 통역 시 '철근 노출 = 구조 위험 신호'임을 명확히 전달해야 하며, 즉시 보수하지 않으면 부식 → 단면 감소 → 구조 내력 저하로 이어짐을 설명해야 합니다. 베트남 발주자에게 철근 노출은 '시공 불량의 명백한 증거'로 인식되므로, 원인(피복 부족, 박리, 충격 등)을 명확히 규명하고 책임 소재를 조율해야 합니다.",
        "meaningVi": "Hiện tượng lớp bê tông bảo vệ bong tróc hoặc hư hỏng khiến cốt thép bên trong lộ ra ngoài. Là nguyên nhân chính gây gỉ thép, ảnh hưởng trực tiếp đến an toàn kết cấu. Nếu không xử lý kịp thời, thép sẽ gỉ → giảm tiết diện → giảm khả năng chịu lực.",
        "context": "구조 안전 점검, 하자 협의, 보수 설계",
        "culturalNote": "한국 현장에서는 철근 노출을 발견하면 '일단 녹 방지제 바르고 콘크리트로 덮자'는 식으로 빠르게 처리하지만, 베트남 감리는 '철근 부식 정도 측정 → 구조 안전성 평가 → 보수 방법 승인'의 절차를 요구합니다. 한국 기술자가 '이 정도는 구조에 영향 없다'고 넘어가려 하면, 베트남 측은 '구조 전문가 의견서' 제출을 요구할 수 있습니다. 통역사는 철근 노출의 원인이 '시공 오류'인지 '외부 충격'인지 구분하여 책임 소재를 조율해야 합니다.",
        "commonMistakes": [
            {
                "mistake": "'철근 노출'을 'thép lộ'로만 축약",
                "correction": "'cốt thép lộ ra' 또는 'thép bị lộ ra ngoài'로 완전한 문장",
                "explanation": "'thép lộ'는 일상적 표현이므로 기술 문서에서는 완전한 형태 사용"
            },
            {
                "mistake": "'철근 녹슬었다'를 'thép cũ'(오래된 철근)로 오역",
                "correction": "'thép bị gỉ' (철근이 부식되었다)",
                "explanation": "'cũ'는 '오래됨'이므로 부식 상태를 나타내지 못함"
            },
            {
                "mistake": "'피복 두께 부족'을 'bê tông mỏng'(콘크리트 얇음)로 일반화",
                "correction": "'chiều dày lớp bê tông bảo vệ không đủ'(보호 콘크리트층 두께 부족)",
                "explanation": "피복 두께는 철근 보호를 위한 최소 두께이므로 '보호층'임을 명시"
            }
        ],
        "examples": [
            {
                "ko": "외벽에서 철근 노출이 확인되어 녹 제거 후 부식 방지제 도포 및 단면 복구를 시행하겠습니다.",
                "vi": "Phát hiện thép lộ ra ở tường ngoài, sẽ loại bỏ gỉ, bôi chất chống gỉ và phục hồi mặt cắt.",
                "situation": "formal"
            },
            {
                "ko": "철근 노출 부위의 부식 깊이를 측정하여 구조 안전성을 평가하겠습니다.",
                "vi": "Sẽ đo độ sâu gỉ tại vùng thép lộ ra để đánh giá an toàn kết cấu.",
                "situation": "formal"
            },
            {
                "ko": "여기 철근 다 드러났네. 빨리 덮어야겠다.",
                "vi": "Chỗ này thép lộ hết rồi. Phải đắp lại ngay.",
                "situation": "onsite"
            }
        ],
        "relatedTerms": ["피복두께", "철근부식", "녹방지제", "단면복구", "박락"]
    },
    {
        "slug": "long-trong",
        "korean": "공극",
        "vietnamese": "Lỗ rỗng (Honeycomb)",
        "hanja": "空隙",
        "hanjaReading": "빌 공(空) + 틈 극(隙)",
        "pronunciation": "공극",
        "meaningKo": "콘크리트 타설 시 골재 사이에 시멘트 페이스트가 충분히 채워지지 않아 생긴 공간(벌집 모양). 강도 저하, 철근 부식, 내구성 감소의 원인이 됩니다. 통역 시 '공극'은 'honeycomb'(벌집)이라는 영어 표현도 함께 사용하면 이해가 빠릅니다. 베트남어로는 'lỗ rỗng' 또는 'tổ ong'(벌집)으로 표현하며, 발생 원인(다짐 불량, 배합 불량, 거푸집 누수)을 명확히 설명해야 합니다. 공극 발견 시 '구조 내력 평가 → 보수 방법 결정'의 단계를 베트남 발주자에게 설명해야 불필요한 재시공 요구를 막을 수 있습니다.",
        "meaningVi": "Khoảng trống giữa cốt liệu do vữa xi măng không lấp đầy (hình tổ ong). Gây giảm cường độ, gỉ thép, giảm độ bền. Nguyên nhân: đầm không kỹ, phối liệu kém, ván khuôn rò rỉ. Cần đánh giá khả năng chịu lực trước khi quyết định phương pháp sửa chữa.",
        "context": "콘크리트 타설 검사, 하자 보고, 보수 계획",
        "culturalNote": "한국 현장에서는 공극을 발견하면 '면적이 작으면 에폭시 주입, 크면 재타설'로 빠르게 판단하지만, 베트남 감리는 '공극 크기 측정 → 강도 시험 → 구조 검토 → 보수 승인'의 단계를 요구합니다. 한국 기술자가 '이 정도는 보수 가능하다'고 단언하면, 베트남 측은 '구조 전문가 의견서'를 요구할 수 있습니다. 통역사는 공극의 크기, 위치, 깊이를 구체적으로 전달하고, '허용 기준'을 계약서 또는 설계 기준에서 찾아 조율해야 합니다.",
        "commonMistakes": [
            {
                "mistake": "'공극'을 'lỗ'(구멍)로만 축약",
                "correction": "'lỗ rỗng' 또는 'tổ ong' (벌집 모양 공극)",
                "explanation": "'lỗ'는 일반적인 구멍이므로 콘크리트 결함을 특정하지 못함"
            },
            {
                "mistake": "'다짐 불량'을 'đầm không tốt'(다짐 좋지 않음)로 모호하게 표현",
                "correction": "'đầm không kỹ / không đủ thời gian đầm'(다짐 불충분 / 다짐 시간 부족)",
                "explanation": "원인을 구체적으로 명시해야 재발 방지 가능"
            },
            {
                "mistake": "'공극 보수'를 'đắp lại'(메우기)로 단순화",
                "correction": "'kiểm tra cường độ + chọn phương pháp sửa chữa'(강도 검사 + 보수 방법 선택)",
                "explanation": "공극 보수는 강도 평가 후 방법을 결정해야 함"
            }
        ],
        "examples": [
            {
                "ko": "기둥 하부에서 공극이 발견되어 코어 채취 후 강도 시험을 실시하겠습니다.",
                "vi": "Phát hiện lỗ rỗng ở chân cột, sẽ lấy mẫu lõi và tiến hành thử cường độ.",
                "situation": "formal"
            },
            {
                "ko": "공극 부위를 정리한 후 무수축 모르타르로 충전하겠습니다.",
                "vi": "Sau khi làm sạch vùng lỗ rỗng, sẽ lấp đầy bằng vữa không усадки.",
                "situation": "formal"
            },
            {
                "ko": "여기 공극 심한데? 다짐 제대로 안 한 것 같아.",
                "vi": "Chỗ này lỗ rỗng nhiều quá? Có vẻ đầm không kỹ.",
                "situation": "onsite"
            }
        ],
        "relatedTerms": ["다짐", "배합", "거푸집", "강도시험", "무수축모르타르"]
    },
    {
        "slug": "cold-joint",
        "korean": "콜드조인트",
        "vietnamese": "Mối nối lạnh (Cold Joint)",
        "hanja": None,
        "hanjaReading": None,
        "pronunciation": "콜드조인트",
        "meaningKo": "먼저 타설한 콘크리트가 응결되기 시작한 후 새 콘크리트를 타설하여 두 층이 완전히 일체화되지 못하고 경계면이 생기는 현상. 구조적 약점이 되며, 누수 및 균열의 원인이 됩니다. 통역 시 '콜드조인트'는 영어 표현 그대로 사용하거나 'mối nối lạnh'(찬 이음부)로 번역하며, 발생 원인(타설 지연, 작업 중단)과 방지 대책(타설 속도 관리, 지연제 사용)을 설명해야 합니다. 베트남 발주자에게 콜드조인트는 '시공 계획 불량'의 증거로 보이므로, 불가피한 사유(기계 고장, 날씨 등)를 명확히 설명해야 책임 분쟁을 줄일 수 있습니다.",
        "meaningVi": "Mối nối giữa hai lớp bê tông do lớp trước đã bắt đầu đông cứng trước khi đổ lớp sau, khiến hai lớp không kết dính hoàn toàn. Là điểm yếu kết cấu, gây rò rỉ và nứt. Nguyên nhân: chậm trễ đổ bê tông, gián đoạn thi công. Phòng tránh: quản lý tốc độ đổ, dùng phụ gia chậm đông.",
        "context": "콘크리트 타설 계획, 하자 분석, 보수 설계",
        "culturalNote": "한국 현장에서는 콜드조인트 발생 시 '위치가 중요 부위가 아니면 그대로 두거나 표면 처리'로 넘어가는 경우가 있지만, 베트남 감리는 '구조 안전성 평가 → 보수 방법 승인'을 요구합니다. 한국 기술자가 '이 정도는 괜찮다'고 하면, 베트남 측은 '누수 시험 + 구조 검토'를 요구할 수 있습니다. 통역사는 콜드조인트의 위치(하중 부위인지 비구조 부위인지)를 명확히 전달하고, 허용 여부를 설계 기준과 비교하여 조율해야 합니다.",
        "commonMistakes": [
            {
                "mistake": "'콜드조인트'를 'chỗ nối lạnh'(찬 곳 이음)로 직역",
                "correction": "'mối nối lạnh' 또는 영어 그대로 'cold joint'",
                "explanation": "'chỗ nối lạnh'은 일상어이므로 기술 용어는 'mối nối lạnh'"
            },
            {
                "mistake": "'타설 지연'을 'chậm đổ'(늦게 타설)로만 표현",
                "correction": "'chậm trễ do [원인] → tạo cold joint'(~로 인한 지연 → 콜드조인트 발생)",
                "explanation": "지연 원인을 명시해야 책임 소재 조율 가능"
            },
            {
                "mistake": "'콜드조인트 보수'를 'sơn lại'(재도장)로 단순화",
                "correction": "'xử lý bề mặt + tiêm keo kết dính'(표면 처리 + 에폭시 주입)",
                "explanation": "콜드조인트는 도장만으로 해결 불가, 접합부 보강 필요"
            }
        ],
        "examples": [
            {
                "ko": "벽체에서 콜드조인트가 발견되어 누수 여부를 확인한 후 에폭시 주입으로 보수하겠습니다.",
                "vi": "Phát hiện mối nối lạnh ở tường, sẽ kiểm tra rò rỉ sau đó sửa chữa bằng tiêm epoxy.",
                "situation": "formal"
            },
            {
                "ko": "타설 중단 시간이 2시간을 초과하여 콜드조인트 발생 가능성이 있으니 타설 속도를 높이겠습니다.",
                "vi": "Thời gian gián đoạn đổ bê tông vượt 2 giờ, có khả năng tạo cold joint, sẽ tăng tốc độ đổ.",
                "situation": "formal"
            },
            {
                "ko": "여기 콜드조인트 생긴 것 같은데? 시간 너무 오래 걸렸나?",
                "vi": "Chỗ này có vẻ có cold joint ấy? Mất quá nhiều thời gian à?",
                "situation": "onsite"
            }
        ],
        "relatedTerms": ["타설계획", "작업이음", "응결시간", "지연제", "에폭시주입"]
    },
    {
        "slug": "nut-co",
        "korean": "수축 균열",
        "vietnamese": "Vết nứt усадки",
        "hanja": "收縮龜裂",
        "hanjaReading": "거둘 수(收) + 줄 축(縮) + 거북 균(龜) + 찢을 열(裂)",
        "pronunciation": "수축 균열",
        "meaningKo": "콘크리트가 경화하면서 수분이 증발하여 부피가 줄어들며 발생하는 균열. 대부분 비구조적이지만, 균열 폭이 크거나 관통 균열인 경우 방수 및 내구성 문제가 됩니다. 통역 시 '수축 균열'은 'vết nứt усадки'(수축 균열) 또는 'vết nứt do co ngót'(수축에 의한 균열)로 표현하며, 구조 균열과의 차이를 명확히 설명해야 합니다. 베트남 발주자에게 '수축 균열은 정상 범위 내에서 발생 가능'하다는 점을 설명하되, 허용 균열 폭(보통 0.3mm 이하)을 기준으로 안전성을 안내해야 불필요한 우려를 줄일 수 있습니다.",
        "meaningVi": "Vết nứt do bê tông mất nước khi đông cứng, làm thể tích giảm. Phần lớn không ảnh hưởng kết cấu, nhưng nếu nứt rộng hoặc xuyên suốt có thể gây vấn đề chống thấm và độ bền. Cần phân biệt với 'vết nứt kết cấu'.",
        "context": "콘크리트 양생 관리, 균열 조사, 보수 판단",
        "culturalNote": "한국 현장에서는 수축 균열을 '0.3mm 이하면 정상'으로 보고 방수 처리로 마무리하지만, 베트남 발주자는 '균열 = 하자'로 인식하는 경향이 강합니다. 한국 기술자가 '이 정도 균열은 구조에 영향 없다'고 설명해도, 베트남 측은 '전수 조사 + 보수'를 요구할 수 있습니다. 통역사는 균열 폭, 길이, 패턴을 구체적으로 전달하고, 설계 기준의 '허용 균열 폭'을 근거로 안전성을 설명해야 분쟁을 줄일 수 있습니다. 또한 '구조 균열'과 '수축 균열'의 차이를 명확히 구분하여 전달해야 과도한 우려를 방지할 수 있습니다.",
        "commonMistakes": [
            {
                "mistake": "'수축 균열'을 단순히 'nứt'(균열)로만 표현",
                "correction": "'vết nứt усадки' 또는 'vết nứt do co ngót'",
                "explanation": "원인(수축)을 명시해야 구조 균열과 구분 가능"
            },
            {
                "mistake": "'균열 폭'을 'độ rộng vết nứt'로만 표현",
                "correction": "'bề rộng vết nứt' (균열 폭) + 수치 단위(mm)",
                "explanation": "'độ rộng'는 추상적이므로 'bề rộng' + 단위 명시"
            },
            {
                "mistake": "'허용 균열'을 'nứt được phép'(허용된 균열)로 직역",
                "correction": "'vết nứt trong giới hạn cho phép'(허용 한도 내 균열)",
                "explanation": "'nứt được phép'은 어색하므로 '한도 내'로 의역"
            }
        ],
        "examples": [
            {
                "ko": "슬래브에서 0.2mm 폭의 수축 균열이 관찰되나 구조 안전에는 영향이 없으며, 에폭시 주입으로 방수 처리하겠습니다.",
                "vi": "Quan sát thấy vết nứt усадки rộng 0.2mm trên sàn, không ảnh hưởng an toàn kết cấu, sẽ xử lý chống thấm bằng tiêm epoxy.",
                "situation": "formal"
            },
            {
                "ko": "수축 균열 발생을 최소화하기 위해 양생 기간 중 습윤 양생을 철저히 하겠습니다.",
                "vi": "Để giảm thiểu vết nứt усадки, sẽ dưỡng hộ ẩm kỹ lưỡng trong thời gian dưỡng hộ.",
                "situation": "formal"
            },
            {
                "ko": "이 균열은 수축 균열이니까 걱정 안 해도 돼.",
                "vi": "Vết nứt này do co ngót thôi, không cần lo.",
                "situation": "onsite"
            }
        ],
        "relatedTerms": ["균열폭", "구조균열", "양생", "에폭시주입", "방수처리"]
    },
    {
        "slug": "nut-ket-cau",
        "korean": "구조 균열",
        "vietnamese": "Vết nứt kết cấu",
        "hanja": "構造龜裂",
        "hanjaReading": "얽을 구(構) + 지을 조(造) + 거북 균(龜) + 찢을 열(裂)",
        "pronunciation": "구조 균열",
        "meaningKo": "구조물에 과도한 하중, 침하, 지진 등의 원인으로 발생하는 균열로, 구조 안전에 직접적인 영향을 미칩니다. 수축 균열과 달리 폭이 넓고(보통 0.3mm 초과), 진행성이 있으며, 하중 방향과 관련이 있습니다. 통역 시 '구조 균열'은 'vết nứt kết cấu'로 표현하며, 즉시 구조 안전 진단이 필요함을 강조해야 합니다. 베트남 발주자에게 구조 균열은 '긴급 대응'이 필요한 사안이므로, 발견 즉시 '하중 제한 → 안전 진단 → 보강 설계 → 보수 시공'의 프로세스를 설명해야 합니다.",
        "meaningVi": "Vết nứt do tải trọng quá mức, lún, động đất, ảnh hưởng trực tiếp đến an toàn kết cấu. Khác với 'vết nứt усадки', thường rộng hơn (>0.3mm), có xu hướng phát triển, liên quan đến hướng chịu lực. Cần kiểm tra an toàn kết cấu ngay lập tức.",
        "context": "구조 안전 진단, 긴급 대응, 보강 설계",
        "culturalNote": "한국에서는 구조 균열 발견 시 '즉시 하중 제한 + 전문가 진단'으로 빠르게 대응하지만, 베트남에서는 '당국 보고 → 사용 금지 명령 → 안전 진단 → 보강 승인'의 행정 절차가 필요합니다. 한국 기술자가 '일단 보강하고 보고하자'는 식으로 접근하면, 베트남 당국으로부터 '무단 보강'으로 제재받을 수 있습니다. 통역사는 긴급성과 절차 준수를 동시에 강조하며, '즉시 안전 조치(하중 제한, 출입 통제) → 당국 보고 → 정식 진단 → 보강 시공'의 단계를 조율해야 합니다.",
        "commonMistakes": [
            {
                "mistake": "'구조 균열'을 단순히 'nứt lớn'(큰 균열)로 표현",
                "correction": "'vết nứt kết cấu' (구조 균열)",
                "explanation": "'nứt lớn'은 크기만 나타내므로 구조 영향을 명시하지 못함"
            },
            {
                "mistake": "구조 균열과 수축 균열을 'nứt'로 통칭",
                "correction": "'vết nứt kết cấu'(구조) vs 'vết nứt усадки'(수축)로 명확히 구분",
                "explanation": "원인과 심각도가 다르므로 반드시 구분하여 표현"
            },
            {
                "mistake": "'구조 보강'을 'sửa chữa'(보수)로 단순화",
                "correction": "'gia cố kết cấu'(구조 보강)",
                "explanation": "'sửa chữa'는 일반 보수이므로 구조 보강의 중요성을 전달하지 못함"
            }
        ],
        "examples": [
            {
                "ko": "보에서 0.5mm 폭의 사인장 균열이 발견되어 구조 균열로 판단되므로 즉시 구조 안전 진단을 실시하겠습니다.",
                "vi": "Phát hiện vết nứt chéo rộng 0.5mm trên dầm, đánh giá là vết nứt kết cấu, sẽ tiến hành kiểm tra an toàn kết cấu ngay.",
                "situation": "formal"
            },
            {
                "ko": "구조 균열 부위를 탄소 섬유 시트로 보강한 후 에폭시 주입으로 충전하겠습니다.",
                "vi": "Sẽ gia cố vùng vết nứt kết cấu bằng tấm sợi carbon, sau đó lấp đầy bằng epoxy.",
                "situation": "formal"
            },
            {
                "ko": "이 균열 구조 균열이야. 위험하니까 여기 출입 금지.",
                "vi": "Vết nứt này là vết nứt kết cấu. Nguy hiểm, cấm vào đây.",
                "situation": "onsite"
            }
        ],
        "relatedTerms": ["수축균열", "사인장균열", "구조안전진단", "탄소섬유보강", "하중제한"]
    },
    {
        "slug": "be-tong-mua-lanh",
        "korean": "한중 콘크리트",
        "vietnamese": "Bê tông mùa lạnh",
        "hanja": "寒中콘크리트",
        "hanjaReading": "찰 한(寒) + 가운데 중(中) + 콘크리트",
        "pronunciation": "한중 콘크리트",
        "meaningKo": "일평균 기온이 4℃ 이하인 동절기에 타설하는 콘크리트. 저온으로 인한 강도 발현 지연, 동해(凍害) 방지를 위해 보온 양생, 가열 조치 등이 필요합니다. 통역 시 '한중 콘크리트'는 'bê tông mùa lạnh'(추운 계절 콘크리트)로 표현하며, 베트남에서는 북부 지역(하노이 등) 일부를 제외하면 한중 콘크리트 경험이 적으므로, 한국의 동절기 시공 기준(보온, 가열, 조강 시멘트 사용 등)을 상세히 설명해야 합니다. 베트남 현장에서 한중 콘크리트 시공 시 '추가 비용'이 발생하므로, 사전에 계약서에 명시되어 있는지 확인하고 조율해야 합니다.",
        "meaningVi": "Bê tông thi công trong thời kỳ nhiệt độ trung bình ngày dưới 4℃. Cần bảo ôn dưỡng hộ, gia nhiệt để tránh chậm phát triển cường độ và hư hỏng do đóng băng. Ở Việt Nam, kinh nghiệm thi công bê tông mùa lạnh hạn chế (chỉ một số khu vực miền Bắc), cần giải thích chi tiết tiêu chuẩn và biện pháp.",
        "context": "동절기 시공 계획, 양생 관리, 비용 협의",
        "culturalNote": "한국에서는 동절기 시공이 일상적이지만, 베트남에서는 대부분 지역이 아열대 기후라 한중 콘크리트 개념이 생소합니다. 한국 기술자가 '한중 콘크리트라 보온 조치가 필요하다'고 하면, 베트남 발주자는 '추가 비용은 누가 부담하는가'를 먼저 묻습니다. 통역사는 한중 콘크리트 시공의 필요성(강도 확보, 동해 방지)을 설명하되, 추가 비용 발생 여부를 계약서 기준으로 조율해야 합니다. 또한 베트남 하노이 등 북부 지역에서도 겨울철(12-2월) 최저 기온이 10℃ 이하로 내려가는 경우가 있으므로, 해당 시기 시공 시 한중 콘크리트 기준 적용 여부를 사전에 협의해야 합니다.",
        "commonMistakes": [
            {
                "mistake": "'한중 콘크리트'를 'bê tông lạnh'(차가운 콘크리트)로 직역",
                "correction": "'bê tông mùa lạnh' 또는 'bê tông thi công mùa đông'",
                "explanation": "'bê tông lạnh'은 온도가 낮은 콘크리트 자체를 의미하므로 부적합"
            },
            {
                "mistake": "'보온 양생'을 'bảo dưỡng'(보양)로 일반화",
                "correction": "'dưỡng hộ bảo ôn'(보온 양생)",
                "explanation": "보온(bảo ôn)을 명시해야 일반 양생과 구분"
            },
            {
                "mistake": "'동해'를 'hại do đông'(동쪽 피해)로 오역",
                "correction": "'hư hỏng do đóng băng'(동결에 의한 손상)",
                "explanation": "'đông'(동쪽)과 'đóng băng'(동결)을 혼동하지 말 것"
            }
        ],
        "examples": [
            {
                "ko": "금주부터 일평균 기온이 4℃ 이하로 예상되어 한중 콘크리트 시공 기준을 적용하고 보온 양생을 실시하겠습니다.",
                "vi": "Từ tuần này dự báo nhiệt độ trung bình dưới 4℃, sẽ áp dụng tiêu chuẩn bê tông mùa lạnh và thực hiện dưỡng hộ bảo ôn.",
                "situation": "formal"
            },
            {
                "ko": "한중 콘크리트 시공을 위해 조강 시멘트를 사용하고 갈탄 보온덮개로 양생하겠습니다.",
                "vi": "Để thi công bê tông mùa lạnh, sẽ dùng xi măng đông cứng nhanh và dưỡng hộ bằng tấm bảo ôn.",
                "situation": "formal"
            },
            {
                "ko": "날씨 추우니까 한중 콘크리트로 해야 돼. 보온덮개 준비해.",
                "vi": "Trời lạnh rồi, phải làm bê tông mùa lạnh. Chuẩn bị tấm bảo ôn.",
                "situation": "onsite"
            }
        ],
        "relatedTerms": ["보온양생", "조강시멘트", "가열양생", "동해", "서중콘크리트"]
    }
]

# 기존 파일 읽기
file_path = os.path.join(os.path.dirname(__file__), '..', 'data', 'terms', 'construction.json')

with open(file_path, 'r', encoding='utf-8') as f:
    data = json.load(f)

# 새 용어 추가
data.extend(new_terms)

# 파일 저장
with open(file_path, 'w', encoding='utf-8') as f:
    json.dump(data, f, ensure_ascii=False, indent=2)

print(f"✅ {len(new_terms)}개 용어가 {file_path}에 추가되었습니다.")
print("📋 추가된 용어:", [term['korean'] for term in new_terms])
