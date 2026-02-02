# -*- coding: utf-8 -*-
import json
import os

# 외벽마감/단열재 테마 용어 10개 (Tier S 기준)
data = [
    {
        "slug": "eifs-drivit",
        "korean": "EIFS(드라이비트)",
        "vietnamese": "EIFS (Drivit)",
        "hanja": None,
        "hanjaReading": None,
        "pronunciation": "이아이에프에스(드라이비트)",
        "meaningKo": "외단열 마감 시스템(External Insulation and Finish System)의 약자로, 단열재 위에 베이스코트, 메쉬, 마감재를 시공하는 습식 외벽 마감 공법입니다. 드라이비트는 대표적인 EIFS 브랜드명으로 통용됩니다. 통역 시 '습식 외단열 공법', '드라이비트 공법'으로 구분해 설명하고, 베트남에서는 주로 고급 빌라나 상업건물에 사용되므로 '마감 품질'과 '단열 성능'을 강조해야 합니다. 시공 단계(단열재→베이스코트→메쉬→마감코트)를 정확히 구분하지 않으면 하자 책임 소재가 불명확해질 수 있습니다.",
        "meaningVi": "Hệ thống cách nhiệt và hoàn thiện ngoại thất (External Insulation and Finish System), gồm lớp cách nhiệt, lớp base coat, lưới sợi thủy tinh và lớp hoàn thiện bề mặt. Drivit là thương hiệu EIFS phổ biến nhất. Thường dùng cho biệt thự cao cấp và công trình thương mại.",
        "context": "외벽 마감 공법 선정, 외단열 시스템 설계, 견적 협의",
        "culturalNote": "한국에서는 드라이비트가 일반화되어 있으나 베트남에서는 고급 공법으로 인식되며 시공 기술자가 부족합니다. 한국은 '마감 미관'을 중시하지만 베트남은 '내구성'과 '균열 방지'에 더 민감합니다. 통역 시 시공 품질 보증 조건과 하자보수 기간을 명확히 전달해야 합니다. 습식 공법 특성상 우기 시공 제한 사항을 반드시 설명해야 합니다.",
        "commonMistakes": [
            {
                "mistake": "EIFS를 '외벽 페인트'로 번역",
                "correction": "hệ thống cách nhiệt ngoại thất (외단열 시스템)",
                "explanation": "단순 도장이 아닌 복합 시스템임을 명확히 해야 함"
            },
            {
                "mistake": "드라이비트를 일반명사로 사용",
                "correction": "EIFS (thương hiệu Drivit)",
                "explanation": "브랜드명과 공법명을 구분해야 함"
            },
            {
                "mistake": "베이스코트를 '기초 코팅'으로 직역",
                "correction": "lớp base coat (lớp vữa nền)",
                "explanation": "전문 시공 용어로 정확히 전달해야 함"
            }
        ],
        "examples": [
            {
                "ko": "EIFS 공법으로 외벽을 시공하면 단열 성능과 미관을 동시에 확보할 수 있습니다.",
                "vi": "Thi công tường ngoài bằng công nghệ EIFS đảm bảo cả hiệu quả cách nhiệt và thẩm mỹ.",
                "situation": "formal"
            },
            {
                "ko": "드라이비트 시공 시 메쉬 겹침은 최소 10cm 이상 확보하세요.",
                "vi": "Khi thi công Drivit, đảm bảo lưới sợi thủy tinh chồng lên nhau tối thiểu 10cm.",
                "situation": "onsite"
            },
            {
                "ko": "베이스코트가 완전히 건조된 후 마감코트를 시공해야 균열이 생기지 않습니다.",
                "vi": "Phải chờ lớp base coat khô hoàn toàn trước khi thi công lớp hoàn thiện để tránh nứt.",
                "situation": "onsite"
            }
        ],
        "relatedTerms": ["단열재", "외단열공법", "습식공법", "베이스코트", "마감코트"]
    },
    {
        "slug": "ceramic-siding",
        "korean": "세라믹사이딩",
        "vietnamese": "Tấm ốp ceramic",
        "hanja": None,
        "hanjaReading": None,
        "pronunciation": "세라믹사이딩",
        "meaningKo": "세라믹 재질의 외벽 마감재로, 내구성과 내후성이 우수하며 다양한 디자인 구현이 가능합니다. 건식 공법으로 시공이 간편하고 유지보수가 용이합니다. 통역 시 '습식 타일'과 구분하여 '건식 세라믹 패널'임을 명확히 해야 하며, 베트남에서는 아직 생소한 자재이므로 '장기 내구성', '저유지보수', '다양한 질감 구현' 장점을 강조해야 합니다. 앵커 고정 방식과 조인트 처리 방법을 정확히 설명하지 않으면 시공 오류가 발생합니다.",
        "meaningVi": "Tấm ốp tường ngoài bằng gốm sứ, có độ bền cao, chống thời tiết tốt và cho phép thiết kế đa dạng. Thi công theo phương pháp khô, dễ lắp đặt và bảo trì đơn giản. Khác với gạch ốp truyền thống, đây là tấm panel ceramic.",
        "context": "외벽 마감재 선정, 건식 공법 설계, 장기 유지보수 계획",
        "culturalNote": "한국에서는 프리미엄 주택과 상업건물에 널리 사용되나 베트남에서는 생소한 자재입니다. 베트남은 전통적으로 타일 습식 시공을 선호하므로 건식 공법의 장점(공기 단축, 하자 최소화)을 충분히 설명해야 합니다. 한국은 '디자인 다양성'을 중시하지만 베트남은 '시공 신뢰성'을 우선시합니다. 앵커 고정 시스템과 지진 대응 성능을 명확히 전달해야 합니다.",
        "commonMistakes": [
            {
                "mistake": "세라믹사이딩을 '세라믹 타일'로 번역",
                "correction": "tấm ốp ceramic (không phải gạch ceramic truyền thống)",
                "explanation": "습식 타일과 건식 패널을 구분해야 함"
            },
            {
                "mistake": "사이딩을 '외벽재'로 일반화",
                "correction": "tấm ốp ceramic (hệ thống lắp khô)",
                "explanation": "건식 공법 특성을 명확히 해야 함"
            },
            {
                "mistake": "앵커를 '못'으로 직역",
                "correction": "neo cố định chuyên dụng",
                "explanation": "전문 고정 부자재임을 명확히 해야 함"
            }
        ],
        "examples": [
            {
                "ko": "세라믹사이딩은 타일과 달리 건식 공법으로 시공하므로 공기를 단축할 수 있습니다.",
                "vi": "Tấm ốp ceramic thi công theo phương pháp khô nên rút ngắn thời gian so với gạch ốp truyền thống.",
                "situation": "formal"
            },
            {
                "ko": "앵커 간격은 설계도에 따라 정확히 시공하세요.",
                "vi": "Khoảng cách neo cố định phải tuân thủ chính xác theo bản vẽ thiết kế.",
                "situation": "onsite"
            },
            {
                "ko": "조인트 처리가 부실하면 빗물이 침투할 수 있으니 주의하세요.",
                "vi": "Nếu xử lý mối nối không kỹ, nước mưa có thể thấm vào, cần chú ý.",
                "situation": "onsite"
            }
        ],
        "relatedTerms": ["건식공법", "외벽패널", "앵커", "조인트", "마감재"]
    },
    {
        "slug": "metal-panel",
        "korean": "금속패널",
        "vietnamese": "Tấm kim loại",
        "hanja": "金屬-",
        "hanjaReading": "金(쇠 금) + 屬(무리 속)",
        "pronunciation": "금속패널",
        "meaningKo": "알루미늄, 스틸 등의 금속 소재로 제작된 외벽 마감 패널로, 경량이면서도 내구성이 뛰어나며 시공이 간편합니다. 단열재가 내장된 샌드위치 패널과 단순 금속 단판으로 구분됩니다. 통역 시 '샌드위치 패널'과 '단판 패널'을 명확히 구분해야 하며, 베트남에서는 주로 공장, 창고에 사용되므로 '단열 성능'과 '차음 성능'이 중요한 사무동/주거용에는 추가 설명이 필요합니다. 열팽창 계수를 고려한 고정 방식을 설명하지 않으면 변형 하자가 발생합니다.",
        "meaningVi": "Tấm ốp tường ngoài bằng kim loại (nhôm, thép), trọng lượng nhẹ, độ bền cao, dễ thi công. Có hai loại: tấm sandwich (có lớp cách nhiệt) và tấm đơn. Thường dùng cho nhà xưởng, kho bãi, và công trình thương mại.",
        "context": "공장/창고 외벽 시공, 경량 마감재 선정, 단열 성능 협의",
        "culturalNote": "한국에서는 다양한 건물 유형에 사용되나 베트남에서는 주로 산업 시설에 한정됩니다. 베트남은 '저비용 고효율'을 중시하므로 금속패널의 경제성을 강조해야 하지만, 주거/사무 용도 시 '차음 성능 보완'과 '결로 방지' 조치를 명확히 설명해야 합니다. 한국은 디자인 다양성을 중시하지만 베트남은 내구성과 유지보수 비용을 우선시합니다.",
        "commonMistakes": [
            {
                "mistake": "금속패널을 '철판'으로 단순화",
                "correction": "tấm kim loại chuyên dụng (nhôm hoặc thép tráng)",
                "explanation": "전문 건축 자재임을 명확히 해야 함"
            },
            {
                "mistake": "샌드위치 패널을 '복층 패널'로 직역",
                "correction": "tấm sandwich (có lõi cách nhiệt)",
                "explanation": "구조와 기능을 정확히 전달해야 함"
            },
            {
                "mistake": "열팽창을 고려하지 않은 고정 방식 설명",
                "correction": "cố định có khe co giãn nhiệt",
                "explanation": "변형 방지 조치를 반드시 전달해야 함"
            }
        ],
        "examples": [
            {
                "ko": "샌드위치 패널은 단열재가 내장되어 있어 별도 단열 공사가 불필요합니다.",
                "vi": "Tấm sandwich có lõi cách nhiệt tích hợp nên không cần thi công cách nhiệt riêng.",
                "situation": "formal"
            },
            {
                "ko": "금속패널 고정 시 열팽창 여유를 반드시 확보하세요.",
                "vi": "Khi cố định tấm kim loại, phải đảm bảo khe co giãn nhiệt.",
                "situation": "onsite"
            },
            {
                "ko": "결로 방지를 위해 단열재와 금속패널 사이에 방습층을 설치합니다.",
                "vi": "Để chống ngưng tụ, lắp màng chống ẩm giữa lớp cách nhiệt và tấm kim loại.",
                "situation": "onsite"
            }
        ],
        "relatedTerms": ["샌드위치패널", "단열재", "열팽창", "결로", "경량마감"]
    },
    {
        "slug": "zinc-panel",
        "korean": "징크판넬",
        "vietnamese": "Tấm kẽm (zinc)",
        "hanja": None,
        "hanjaReading": None,
        "pronunciation": "징크판넬",
        "meaningKo": "아연-티타늄 합금으로 제작된 고급 금속 외벽재로, 자가 보호 피막을 형성해 장기 내구성이 뛰어나고 독특한 질감을 연출할 수 있습니다. 시간이 지나면서 자연스러운 파티나(patina)가 형성되어 색상이 변화합니다. 통역 시 '일반 아연도금강판'과 구분하여 '프리미엄 징크 합금'임을 명확히 해야 하며, 베트남에서는 생소한 자재이므로 '자가 치유 기능', '50년 이상 내구성', '유지보수 불필요'를 강조해야 합니다. 파티나 변화를 '하자'로 오해하지 않도록 사전 설명이 필수입니다.",
        "meaningVi": "Tấm kim loại hợp kim kẽm-titan cao cấp, tự tạo lớp bảo vệ, độ bền dài hạn, và có kết cấu độc đáo. Theo thời gian sẽ hình thành lớp patina tự nhiên, thay đổi màu sắc. Khác với tôn mạ kẽm thông thường, đây là vật liệu hạng sang.",
        "context": "프리미엄 외벽 마감, 디자인 건축물, 장기 내구성 요구 프로젝트",
        "culturalNote": "한국에서는 현대적 건축물의 고급 마감재로 인정받지만 베트남에서는 매우 생소하며 가격 저항이 큽니다. 베트남은 '초기 비용'에 민감하므로 '장기 유지보수 비용 절감'과 '프리미엄 이미지'를 강조해야 설득이 가능합니다. 파티나 형성을 '산화', '부식'으로 오해할 수 있으므로 '의도된 디자인 변화'임을 명확히 전달해야 합니다. 한국은 미적 가치를 중시하지만 베트남은 실용성을 우선시합니다.",
        "commonMistakes": [
            {
                "mistake": "징크를 '아연도금강판'으로 번역",
                "correction": "tấm hợp kim kẽm-titan cao cấp (zinc premium)",
                "explanation": "일반 도금 강판과 완전히 다른 프리미엄 자재임을 명확히 해야 함"
            },
            {
                "mistake": "파티나를 '부식'으로 번역",
                "correction": "lớp patina tự nhiên (không phải ăn mòn)",
                "explanation": "자연스러운 변화이지 하자가 아님을 설명해야 함"
            },
            {
                "mistake": "유지보수 불필요를 '관리 무시'로 오해",
                "correction": "không cần bảo trì định kỳ (nhờ lớp tự bảo vệ)",
                "explanation": "자가 보호 메커니즘을 정확히 전달해야 함"
            }
        ],
        "examples": [
            {
                "ko": "징크판넬은 초기 비용은 높지만 50년 이상 유지보수 없이 사용할 수 있습니다.",
                "vi": "Tấm kẽm có chi phí ban đầu cao nhưng có thể sử dụng trên 50 năm không cần bảo trì.",
                "situation": "formal"
            },
            {
                "ko": "파티나가 형성되면서 색상이 변하는 것은 정상이며 오히려 매력 포인트입니다.",
                "vi": "Màu sắc thay đổi do hình thành lớp patina là hiện tượng bình thường và là điểm nhấn thẩm mỹ.",
                "situation": "formal"
            },
            {
                "ko": "징크판넬 시공 시 구리 등 이종 금속과의 접촉을 피해야 합니다.",
                "vi": "Khi thi công tấm kẽm, tránh tiếp xúc với đồng và các kim loại khác để tránh ăn mòn điện hóa.",
                "situation": "onsite"
            }
        ],
        "relatedTerms": ["파티나", "아연티타늄합금", "프리미엄마감", "자가보호피막", "장기내구성"]
    },
    {
        "slug": "composite-panel",
        "korean": "복합판넬",
        "vietnamese": "Tấm composite",
        "hanja": "複合-",
        "hanjaReading": "複(겹 복) + 合(합할 합)",
        "pronunciation": "복합판넬",
        "meaningKo": "두 개 이상의 이질 재료를 결합한 패널로, 주로 알루미늄 외피와 내부 심재(PE, FR 등)로 구성됩니다. 경량이면서도 강성이 우수하며 다양한 색상과 질감 구현이 가능합니다. 통역 시 심재 종류(PE: 일반용, FR: 난연용)를 명확히 구분해야 하며, 베트남에서는 '가연성'에 대한 우려가 크므로 '난연 등급'을 반드시 확인하고 전달해야 합니다. 커튼월과 조합 시 풍압 계산과 고정 디테일을 정확히 설명하지 않으면 탈락 사고가 발생할 수 있습니다.",
        "meaningVi": "Tấm ốp kết hợp từ hai vật liệu trở lên, thường gồm vỏ nhôm và lõi bên trong (PE, FR). Trọng lượng nhẹ, độ cứng cao, đa dạng màu sắc. Cần phân biệt loại lõi: PE (thông thường) và FR (chống cháy).",
        "context": "고층 건물 외벽, 커튼월 시스템, 난연 성능 협의",
        "culturalNote": "한국에서는 고층 건물 외벽재로 일반화되어 있으나 베트남에서는 화재 안전 규정이 엄격하지 않아 PE 심재가 많이 사용됩니다. 한국은 난연 등급(FR)을 필수로 요구하지만 베트남은 비용 절감을 위해 일반 PE를 선호하므로 '화재 위험성'과 '보험 조건'을 명확히 설명해야 합니다. 커튼월 시공 시 풍압 계산과 고정 디테일 오류로 인한 사고가 빈번하므로 통역 시 기술 검토를 강조해야 합니다.",
        "commonMistakes": [
            {
                "mistake": "복합판넬을 '알루미늄판'으로 단순화",
                "correction": "tấm composite (vỏ nhôm + lõi PE/FR)",
                "explanation": "구조를 정확히 전달해야 함"
            },
            {
                "mistake": "PE와 FR 심재를 구분하지 않음",
                "correction": "lõi PE (thường) hoặc lõi FR (chống cháy)",
                "explanation": "난연 등급을 명확히 구분해야 함"
            },
            {
                "mistake": "풍압 계산을 '일반 고정'으로 단순화",
                "correction": "tính toán áp lực gió và hệ thống cố định chuyên dụng",
                "explanation": "구조 안전성을 반드시 전달해야 함"
            }
        ],
        "examples": [
            {
                "ko": "고층 건물에는 반드시 FR 등급 복합판넬을 사용해야 합니다.",
                "vi": "Tòa nhà cao tầng bắt buộc sử dụng tấm composite loại FR (chống cháy).",
                "situation": "formal"
            },
            {
                "ko": "풍압 계산서를 확인하고 고정 간격을 준수하세요.",
                "vi": "Kiểm tra bản tính áp lực gió và tuân thủ khoảng cách cố định.",
                "situation": "onsite"
            },
            {
                "ko": "PE 심재는 비용은 저렴하지만 화재 위험이 있으니 주의하세요.",
                "vi": "Lõi PE có chi phí thấp nhưng tiềm ẩn nguy cơ cháy, cần lưu ý.",
                "situation": "informal"
            }
        ],
        "relatedTerms": ["커튼월", "난연등급", "풍압계산", "알루미늄외피", "PE심재", "FR심재"]
    },
    {
        "slug": "pir-insulation",
        "korean": "PIR단열재",
        "vietnamese": "Tấm cách nhiệt PIR",
        "hanja": None,
        "hanjaReading": None,
        "pronunciation": "피아이알 단열재",
        "meaningKo": "폴리이소시아누레이트(Polyisocyanurate) 발포 단열재로, 높은 단열 성능과 난연성을 동시에 확보한 고성능 단열재입니다. 일반 우레탄폼(PU)보다 열전도율이 낮고 화재 시 유독가스 발생이 적습니다. 통역 시 '일반 스티로폼', '우레탄폼'과 명확히 구분하여 '고성능 단열재'임을 강조해야 하며, 베트남에서는 생소한 자재이므로 '장기 단열 성능 유지', '난연 등급', '친환경 인증'을 부각해야 합니다. 가격 대비 성능을 정량적으로 비교하지 않으면 일반 단열재로 대체될 위험이 있습니다.",
        "meaningVi": "Tấm cách nhiệt bọt Polyisocyanurate (PIR), hiệu suất cách nhiệt cao và chống cháy tốt. Hệ số dẫn nhiệt thấp hơn bọt polyurethane (PU) thông thường, ít phát sinh khí độc khi cháy. Vật liệu cách nhiệt hiệu năng cao.",
        "context": "고성능 단열 설계, 난연 등급 요구 프로젝트, 장기 성능 유지",
        "culturalNote": "한국에서는 건축물 에너지 절감 정책으로 인해 PIR 단열재 사용이 증가하고 있으나 베트남에서는 매우 생소하며 가격 저항이 큽니다. 베트남은 '초기 비용'을 최우선시하므로 '장기 에너지 절감 효과'를 구체적 수치(ROI 계산)로 제시해야 설득이 가능합니다. 한국은 친환경 인증을 중시하지만 베트남은 '즉각적 비용 절감'을 중시합니다. 난연 성능은 보험료 절감과 연계하여 설명하면 효과적입니다.",
        "commonMistakes": [
            {
                "mistake": "PIR을 '우레탄폼'으로 번역",
                "correction": "tấm cách nhiệt PIR (khác với PU thông thường)",
                "explanation": "성능 등급이 다른 자재임을 명확히 해야 함"
            },
            {
                "mistake": "열전도율을 단순히 '단열 성능'으로 설명",
                "correction": "hệ số dẫn nhiệt λ = 0.022 W/mK (thấp hơn PU)",
                "explanation": "정량적 수치로 성능을 전달해야 함"
            },
            {
                "mistake": "가격만 비교하고 장기 효과 누락",
                "correction": "chi phí ban đầu cao nhưng tiết kiệm năng lượng dài hạn",
                "explanation": "투자 대비 효과를 반드시 설명해야 함"
            }
        ],
        "examples": [
            {
                "ko": "PIR 단열재는 일반 단열재보다 30% 얇은 두께로 동등한 단열 성능을 확보합니다.",
                "vi": "Tấm cách nhiệt PIR đạt hiệu quả tương đương với độ dày mỏng hơn 30% so với vật liệu thông thường.",
                "situation": "formal"
            },
            {
                "ko": "난연 등급이 높아 화재 위험이 적고 보험료 절감 효과가 있습니다.",
                "vi": "Cấp chống cháy cao, giảm nguy cơ hỏa hoạn và tiết kiệm phí bảo hiểm.",
                "situation": "formal"
            },
            {
                "ko": "PIR 단열재는 습기에 강해 장기 성능 저하가 거의 없습니다.",
                "vi": "Tấm PIR chống ẩm tốt nên gần như không suy giảm hiệu suất theo thời gian.",
                "situation": "onsite"
            }
        ],
        "relatedTerms": ["열전도율", "난연등급", "폴리이소시아누레이트", "고성능단열", "에너지절감"]
    },
    {
        "slug": "pf-insulation",
        "korean": "PF단열재",
        "vietnamese": "Tấm cách nhiệt PF",
        "hanja": None,
        "hanjaReading": None,
        "pronunciation": "피에프 단열재",
        "meaningKo": "페놀폼(Phenolic Foam) 단열재로, 극히 낮은 열전도율과 최고 수준의 난연 성능을 가진 프리미엄 단열재입니다. PIR보다도 성능이 우수하며 화재 시 연기와 유독가스 발생이 극히 적습니다. 통역 시 '최고급 단열재', '초고성능 난연재'임을 강조해야 하며, 베트남에서는 거의 사용되지 않는 자재이므로 '법적 난연 기준 초과 달성', '초박형 시공 가능', '장기 성능 보증'을 명확히 전달해야 합니다. 가격이 매우 높으므로 특수 용도(데이터센터, 클린룸 등)가 아니면 채택이 어렵습니다.",
        "meaningVi": "Tấm cách nhiệt bọt phenolic (PF), hệ số dẫn nhiệt cực thấp và chống cháy ở mức cao nhất. Hiệu suất vượt trội hơn PIR, phát sinh khói và khí độc tối thiểu khi cháy. Vật liệu cách nhiệt cao cấp nhất.",
        "context": "초고층 건물, 데이터센터, 클린룸, 극한 난연 요구 프로젝트",
        "culturalNote": "한국에서도 특수 용도에만 제한적으로 사용되며 베트남에서는 거의 알려지지 않은 자재입니다. 가격이 PIR의 2배 이상이므로 일반 건축물에는 적용이 어렵고, 법적 난연 기준이 엄격한 특수 시설(소방법 특별 규정 적용 건물)에만 제안해야 합니다. 베트남은 규정 준수보다 비용 절감을 우선시하므로 '법적 강제 요건' 또는 '보험사 요구 조건'이 아니면 채택되지 않습니다.",
        "commonMistakes": [
            {
                "mistake": "PF를 PIR과 동급으로 설명",
                "correction": "tấm PF (hiệu suất cao hơn PIR, giá cao hơn)",
                "explanation": "성능과 가격 등급을 명확히 구분해야 함"
            },
            {
                "mistake": "일반 건축물에 PF 제안",
                "correction": "chỉ dùng cho công trình đặc biệt (data center, clean room)",
                "explanation": "용도를 제한하여 제안해야 함"
            },
            {
                "mistake": "가격 설명 없이 성능만 강조",
                "correction": "hiệu suất cao nhất nhưng chi phí gấp đôi PIR",
                "explanation": "비용 대비 효과를 반드시 전달해야 함"
            }
        ],
        "examples": [
            {
                "ko": "PF 단열재는 열전도율이 0.018 W/mK로 가장 낮아 초박형 시공이 가능합니다.",
                "vi": "Tấm PF có hệ số dẫn nhiệt 0.018 W/mK thấp nhất, cho phép thi công siêu mỏng.",
                "situation": "formal"
            },
            {
                "ko": "데이터센터처럼 화재 위험이 높은 시설에는 PF 단열재를 권장합니다.",
                "vi": "Đối với công trình nguy cơ cháy cao như data center, khuyến nghị dùng tấm PF.",
                "situation": "formal"
            },
            {
                "ko": "PF 단열재는 고가이지만 보험료와 유지보수 비용을 장기적으로 절감합니다.",
                "vi": "Tấm PF có giá cao nhưng tiết kiệm phí bảo hiểm và chi phí bảo trì lâu dài.",
                "situation": "informal"
            }
        ],
        "relatedTerms": ["페놀폼", "초고성능단열", "극난연", "열전도율", "데이터센터"]
    },
    {
        "slug": "eps-insulation",
        "korean": "EPS",
        "vietnamese": "Tấm EPS",
        "hanja": None,
        "hanjaReading": None,
        "pronunciation": "이피에스",
        "meaningKo": "발포폴리스티렌(Expanded Polystyrene) 단열재로, 가장 널리 사용되는 경제적인 단열재입니다. 흔히 '스티로폼'으로 불리며 가볍고 가공이 쉽지만 난연 성능이 낮고 장기 성능 저하가 있습니다. 통역 시 '비드법 보온판'과 '압출법 보온판(XPS)'을 명확히 구분해야 하며, 베트남에서는 '스티로폼'으로 통칭되므로 품질 등급(밀도, 난연 첨가 여부)을 반드시 확인하고 전달해야 합니다. 외단열 적용 시 난연 처리 여부를 설명하지 않으면 화재 위험이 있습니다.",
        "meaningVi": "Tấm cách nhiệt bọt polystyrene giãn nở (EPS), thường gọi là 'xốp trắng' hoặc 'styrofoam'. Nhẹ, dễ gia công, giá thấp nhưng chống cháy kém và hiệu suất giảm theo thời gian. Phổ biến nhất tại Việt Nam.",
        "context": "일반 건축물 단열, 경제적 단열 설계, 비용 최소화 프로젝트",
        "culturalNote": "한국과 베트남 모두에서 가장 일반적으로 사용되는 단열재이지만 품질 편차가 큽니다. 베트남은 저가 EPS를 무분별하게 사용하여 화재 사고가 빈번하므로 '난연 첨가 EPS' 사용을 반드시 명시해야 합니다. 한국은 밀도 등급(1호~4호)을 엄격히 구분하지만 베트남은 육안 확인만으로 시공하는 경우가 많아 품질 검사 절차를 강조해야 합니다. '값싼 단열재'가 아닌 '적정 품질 EPS'임을 명확히 해야 합니다.",
        "commonMistakes": [
            {
                "mistake": "EPS를 단순히 '스티로폼'으로 번역",
                "correction": "tấm EPS (xốp cách nhiệt tiêu chuẩn, không phải xốp bao bì)",
                "explanation": "건축용 자재임을 명확히 해야 함"
            },
            {
                "mistake": "밀도 등급을 설명하지 않음",
                "correction": "EPS mật độ [X] kg/m³ (cấp 1~4 tùy mục đích)",
                "explanation": "품질 기준을 명확히 전달해야 함"
            },
            {
                "mistake": "난연 처리 여부를 확인하지 않음",
                "correction": "EPS có phụ gia chống cháy hay không?",
                "explanation": "화재 안전성을 반드시 확인해야 함"
            }
        ],
        "examples": [
            {
                "ko": "EPS는 가격이 저렴하지만 외단열 적용 시 반드시 난연 등급을 확인하세요.",
                "vi": "EPS có giá thấp nhưng khi dùng cho ngoại thất phải kiểm tra cấp chống cháy.",
                "situation": "formal"
            },
            {
                "ko": "밀도가 낮은 EPS는 장기 성능이 떨어지니 3호 이상을 사용하세요.",
                "vi": "EPS mật độ thấp giảm hiệu suất lâu dài, nên dùng cấp 3 trở lên.",
                "situation": "onsite"
            },
            {
                "ko": "EPS 시공 시 틈새가 생기지 않도록 밀착해서 붙이세요.",
                "vi": "Khi thi công EPS, dán sát không để khe hở.",
                "situation": "onsite"
            }
        ],
        "relatedTerms": ["스티로폼", "비드법보온판", "밀도등급", "난연첨가", "발포폴리스티렌"]
    },
    {
        "slug": "bead-eps",
        "korean": "비드법보온판",
        "vietnamese": "Tấm EPS phương pháp hạt",
        "hanja": "-法保溫板",
        "hanjaReading": "法(법 법) + 保(지킬 보) + 溫(따뜻할 온) + 板(널빤지 판)",
        "pronunciation": "비드법 보온판",
        "meaningKo": "폴리스티렌 비드(작은 알갱이)를 발포시켜 제조한 단열재로, 일반적인 'EPS'를 의미합니다. 압출법(XPS)과 구분하기 위한 정식 명칭입니다. 표면에 작은 알갱이가 보이는 것이 특징이며 가격이 저렴하고 가공이 쉽습니다. 통역 시 '압출법'과의 차이(흡수율, 압축강도)를 명확히 설명해야 하며, 베트남에서는 두 종류를 구분하지 않고 사용하는 경우가 많아 용도에 맞는 선택을 강조해야 합니다. 지하 외벽처럼 습기가 많은 곳에는 부적합함을 명확히 전달해야 합니다.",
        "meaningVi": "Tấm cách nhiệt làm từ hạt polystyrene nở bọt, tức là EPS thông thường. Tên chính thức để phân biệt với XPS (phương pháp ép đùn). Bề mặt thấy các hạt nhỏ, giá thấp, dễ gia công.",
        "context": "내외벽 단열, 바닥 단열, 경량 단열 시공",
        "culturalNote": "한국에서는 '비드법'과 '압출법'을 명확히 구분하여 용도에 맞게 사용하지만 베트남에서는 모두 'xốp cách nhiệt'로 통칭되어 혼용됩니다. 베트남 시공 현장에서는 육안으로만 구분하므로 '표면 알갱이 확인', '흡수율 테스트' 등 간단한 검증 방법을 통역 시 함께 전달해야 합니다. 지하 방수와 조합 시 흡수율 문제를 설명하지 않으면 단열 성능 저하가 발생합니다.",
        "commonMistakes": [
            {
                "mistake": "비드법을 단순히 'EPS'로만 번역",
                "correction": "tấm EPS phương pháp hạt (bề mặt thấy hạt)",
                "explanation": "제조 방식을 명확히 해야 압출법과 구분됨"
            },
            {
                "mistake": "압출법과 혼용하여 설명",
                "correction": "EPS (hạt) khác XPS (ép đùn) - độ thấm nước khác nhau",
                "explanation": "용도 차이를 명확히 해야 함"
            },
            {
                "mistake": "흡수율을 설명하지 않음",
                "correction": "EPS hút nước cao hơn XPS, không dùng cho tầng hầm",
                "explanation": "적용 제한 사항을 반드시 전달해야 함"
            }
        ],
        "examples": [
            {
                "ko": "비드법 보온판은 내벽 단열에 적합하며 가격이 저렴합니다.",
                "vi": "Tấm EPS hạt phù hợp cho cách nhiệt tường trong và có giá thấp.",
                "situation": "formal"
            },
            {
                "ko": "표면에 알갱이가 보이면 비드법, 매끈하면 압출법입니다.",
                "vi": "Nếu bề mặt thấy hạt là EPS, nếu nhẵn là XPS.",
                "situation": "onsite"
            },
            {
                "ko": "지하 외벽에는 흡수율이 낮은 압출법을 사용하세요.",
                "vi": "Với tường ngoài tầng hầm, dùng XPS có độ hút nước thấp.",
                "situation": "onsite"
            }
        ],
        "relatedTerms": ["EPS", "압출법보온판", "폴리스티렌", "흡수율", "단열재"]
    },
    {
        "slug": "extruded-eps",
        "korean": "압출법보온판",
        "vietnamese": "Tấm XPS (ép đùn)",
        "hanja": "押出法保溫板",
        "hanjaReading": "押(누를 압) + 出(날 출) + 法(법 법) + 保(지킬 보) + 溫(따뜻할 온) + 板(널빤지 판)",
        "pronunciation": "압출법 보온판",
        "meaningKo": "폴리스티렌을 압출 성형하여 제조한 단열재로, 'XPS'로 불립니다. 비드법(EPS)보다 밀도가 높고 흡수율이 낮아 습기가 많은 곳에 적합합니다. 표면이 매끄럽고 균일하며 압축강도가 우수하여 지하 외벽, 바닥 단열에 주로 사용됩니다. 통역 시 '비드법'과의 차이(흡수율 1/10 수준, 압축강도 2배)를 정량적으로 설명해야 하며, 베트남에서는 가격 차이로 인해 부적절한 대체가 빈번하므로 '용도별 필수 사양'임을 강조해야 합니다. 지하 방수층과의 시공 순서를 명확히 전달해야 합니다.",
        "meaningVi": "Tấm cách nhiệt polystyrene ép đùn (XPS), mật độ cao hơn EPS, độ hút nước thấp, phù hợp cho nơi ẩm ướt. Bề mặt nhẵn đều, độ nén cao, thường dùng cho tầng hầm, sàn. Giá cao hơn EPS nhưng hiệu suất tốt hơn.",
        "context": "지하 외벽 단열, 바닥 단열, 습기 많은 환경",
        "culturalNote": "한국에서는 지하 외벽과 바닥 단열에 XPS를 필수로 사용하지만 베트남에서는 비용 절감을 위해 EPS로 대체하는 경우가 많습니다. 이로 인해 습기 흡수로 단열 성능이 급격히 저하되고 곰팡이 발생 문제가 빈번합니다. 통역 시 '장기 성능 유지', '곰팡이 방지', '구조체 보호' 관점에서 XPS의 필요성을 강조해야 하며, 초기 비용 대비 유지보수 비용 절감 효과를 정량적으로 제시해야 설득이 가능합니다.",
        "commonMistakes": [
            {
                "mistake": "압출법을 'EPS 고급형'으로 설명",
                "correction": "tấm XPS (khác với EPS, mật độ cao, chống thấm tốt)",
                "explanation": "제조 방식과 성능이 완전히 다름을 명확히 해야 함"
            },
            {
                "mistake": "가격만 비교하고 성능 차이 누락",
                "correction": "XPS đắt hơn nhưng hút nước thấp gấp 10 lần EPS",
                "explanation": "정량적 성능 비교를 반드시 해야 함"
            },
            {
                "mistake": "용도를 구분하지 않고 일괄 제안",
                "correction": "tầng hầm, sàn → XPS bắt buộc / tường trong → EPS được",
                "explanation": "용도별 필수 사양을 명확히 해야 함"
            }
        ],
        "examples": [
            {
                "ko": "지하 외벽 단열은 반드시 압출법 보온판을 사용해야 습기 문제가 없습니다.",
                "vi": "Cách nhiệt tường tầng hầm bắt buộc dùng tấm XPS để tránh thấm ẩm.",
                "situation": "formal"
            },
            {
                "ko": "XPS는 EPS보다 2배 비싸지만 흡수율이 1/10로 낮아 장기적으로 유리합니다.",
                "vi": "XPS đắt gấp đôi EPS nhưng hút nước thấp gấp 10 lần, có lợi lâu dài.",
                "situation": "formal"
            },
            {
                "ko": "바닥 단열재는 압축강도가 높은 XPS를 사용하세요.",
                "vi": "Vật liệu cách nhiệt sàn phải dùng XPS có độ nén cao.",
                "situation": "onsite"
            }
        ],
        "relatedTerms": ["XPS", "비드법보온판", "흡수율", "압축강도", "지하방수"]
    }
]

# 파일 경로
file_path = os.path.join(
    "/Users/mac/Documents/claude_code/projects/vn.epicstage.co.kr/src/data/terms",
    "construction.json"
)

# 기존 데이터 읽기
with open(file_path, "r", encoding="utf-8") as f:
    existing_data = json.load(f)

# 새 데이터 추가
existing_data.extend(data)

# 저장
with open(file_path, "w", encoding="utf-8") as f:
    json.dump(existing_data, f, ensure_ascii=False, indent=2)

print(f"✅ {len(data)}개 용어 추가 완료: {file_path}")
