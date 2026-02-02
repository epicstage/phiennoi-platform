#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
실내마감재 (Interior Finishing Materials) 용어 추가 스크립트
Tier S 품질 기준 준수
"""

import json
import os

# 파일 경로 설정 (CRITICAL RULE 1)
file_path = os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', 'data', 'terms', 'construction.json')

# 기존 데이터 로드
with open(file_path, 'r', encoding='utf-8') as f:
    data = json.load(f)  # data is a LIST, not dict! (CRITICAL RULE 2)

# 기존 slug 추출 (CRITICAL RULE 4)
existing_slugs = {t['slug'] for t in data}

# 새 용어 정의
new_terms = [
    {
        "slug": "giay-dan-tuong",
        "korean": "벽지",
        "vietnamese": "giấy dán tường",
        "hanja": "壁紙",
        "hanjaReading": "壁(벽 벽) + 紙(종이 지)",
        "pronunciation": "벽찌",
        "meaningKo": "벽면에 붙이는 장식용 종이나 합성수지 재료. 통역 시 '도배'와 혼동 주의 - 도배는 '시공 행위'(thi công dán giấy)이고 벽지는 '재료'(vật liệu). 베트남에서는 giấy dán tường(종이 벽지)과 decal dán tường(스티커형)을 엄격히 구분하므로, 재질을 명확히 해야 함. PVC 벽지는 giấy dán tường PVC, 실크 벽지는 giấy lụa로 표현. 현장에서 '평당 가격'을 물을 때 베트남은 제곱미터(m²) 기준이므로 환산 필수.",
        "meaningVi": "Vật liệu trang trí bề mặt tường bằng giấy hoặc vật liệu tổng hợp. Có nhiều loại: giấy dán tường PVC chống thấm, giấy lụa cao cấp, giấy dán tường 3D. Khác với decal dán tường (loại dán tạm thời), giấy dán tường được thi công bằng keo chuyên dụng và có độ bền lâu hơn. Giá tính theo m², cần tính lượng hao hụt khoảng 10-15% khi thi công.",
        "context": "벽면 마감 시공, 인테리어 디자인",
        "culturalNote": "한국은 합지(giấy ghép) 벽지가 주류이나 베트남은 PVC 코팅 벽지를 선호 - 습도가 높아 곰팡이 방지 때문. 한국에서 '평당 몇만원' 견적을 베트nam에서 설명할 때 m² 환산 필수 (1평 ≈ 3.3m²). 베트남 현장에서 giấy dán tường Hàn Quốc(한국 벽지)는 고급 이미지지만 가격 민감도가 높아 m² 단가를 명확히 제시해야 분쟁 예방. 시공 시 keo dán giấy(벽지풀) 품질이 내구성을 좌우하므로 재료 스펙 확인 필수.",
        "commonMistakes": [
            {
                "mistake": "도배 = giấy dán tường",
                "correction": "도배(시공) = thi công dán giấy, 벽지(재료) = giấy dán tường",
                "explanation": "도배는 '행위'이고 벽지는 '자재'이므로 구분 필수. 견적서에서 혼동 시 금액 오해 발생"
            },
            {
                "mistake": "decal dán tường으로 통칭",
                "correction": "스티커형은 decal, 풀 시공형은 giấy dán tường",
                "explanation": "베트남에서 decal은 저가 임시용, giấy dán tường은 영구 시공용으로 명확히 구분됨"
            },
            {
                "mistake": "평 단위 그대로 사용",
                "correction": "m² 환산 필수 (1평 = 3.3m²)",
                "explanation": "베트남은 평 개념이 없어 m² 기준 견적 제시 필수. 환산 누락 시 가격 분쟁"
            }
        ],
        "examples": [
            {
                "ko": "벽지 시공 단가는 제곱미터당 15,000동입니다.",
                "vi": "Đơn giá thi công giấy dán tường là 15,000 đồng/m².",
                "situation": "formal"
            },
            {
                "ko": "이 벽지는 PVC 코팅이라 습기에 강해요.",
                "vi": "Giấy dán tường này có phủ PVC nên chống ẩm tốt.",
                "situation": "onsite"
            },
            {
                "ko": "패턴 맞춤 때문에 10% 더 주문해야 합니다.",
                "vi": "Do phải ghép hoa văn nên cần đặt thêm 10% vật liệu.",
                "situation": "formal"
            }
        ],
        "relatedTerms": ["keo-dan-giay", "thi-cong-op-tuong", "decal-dan-tuong"]
    },
    {
        "slug": "san-go",
        "korean": "마루",
        "vietnamese": "sàn gỗ",
        "hanja": None,
        "hanjaReading": None,
        "pronunciation": "마루",
        "meaningKo": "원목이나 합판으로 만든 바닥재. 통역 시 '마루'와 '원목바닥'을 구분해야 함 - 원목은 gỗ tự nhiên, 강화마루는 sàn gỗ công nghiệp. 베트남에서 sàn gỗ는 고급 자재로 인식되나 습기에 약해 1층은 피하는 게 관행. 시공 방식도 중요: 접착식(dán keo)과 floating 방식(lắp nổi)을 명확히 구분. 한국에서 '평당 8만원'이라 해도 베트남은 m² 단가 + 시공비 별도 견적이 일반적. 나무 종류(gỗ sồi/참나무, gỗ tếch/티크)에 따라 가격 차이가 크므로 수종 명시 필수.",
        "meaningVi": "Vật liệu lát sàn làm từ gỗ tự nhiên hoặc gỗ công nghiệp. Có 2 loại chính: sàn gỗ tự nhiên (đắt, cần bảo dưỡng kỹ) và sàn gỗ công nghiệp (rẻ hơn, chống ẩm tốt hơn). Thi công có 2 phương pháp: dán keo trực tiếp xuống nền hoặc lắp nổi (floating) với lớp xốp PE làm đệm. Không nên dùng cho tầng 1 hoặc khu vực ẩm ướt vì dễ cong vênh. Giá phụ thuộc loại gỗ: gỗ sồi, gỗ tếch, gỗ óc chó có giá khác nhau.",
        "context": "바닥재 시공, 인테리어 마감",
        "culturalNote": "한국은 온돌 문화로 마루 선호도가 높으나, 베트남은 타일(gạch lát nền) 선호 - 열대 기후 때문. sàn gỗ는 고급 주택/상업 공간용으로 인식. 한국 현장에서 '평당 시공비'로 말하면 베트남 협력업체는 m² 환산 + 인건비(tiền công) 별도 청구하므로 총액 확인 필수. 베트남에서 gỗ tự nhiên(원목)은 세금이 높아 수입 시 HS Code 확인 필요. 습도 70% 이상 환경에서는 sàn gỗ công nghiệp(강화마루) 권장이 통역 팁.",
        "commonMistakes": [
            {
                "mistake": "마루 = gỗ (나무)",
                "correction": "마루 = sàn gỗ (목재 바닥재)",
                "explanation": "gỗ는 원자재, sàn gỗ는 완제품 바닥재. 견적서에서 gỗ로만 쓰면 자재인지 시공품인지 불명확"
            },
            {
                "mistake": "원목과 강화마루 구분 없이 sàn gỗ로 통칭",
                "correction": "원목 = sàn gỗ tự nhiên, 강화마루 = sàn gỗ công nghiệp",
                "explanation": "가격과 내구성이 완전히 다르므로 구분 필수. 베트남 시장에서 혼동 시 클레임 발생"
            },
            {
                "mistake": "평 단위로 면적 제시",
                "correction": "m² 환산 필수",
                "explanation": "베트남은 평 개념 없음. 1평 = 3.3m²로 환산하여 견적 작성"
            }
        ],
        "examples": [
            {
                "ko": "원목 마루는 습기에 약하니 1층은 피하세요.",
                "vi": "Sàn gỗ tự nhiên dễ bị ẩm nên không nên dùng ở tầng 1.",
                "situation": "onsite"
            },
            {
                "ko": "강화마루 시공비는 제곱미터당 12만동입니다.",
                "vi": "Chi phí thi công sàn gỗ công nghiệp là 120,000 đồng/m².",
                "situation": "formal"
            },
            {
                "ko": "이 마루는 플로팅 방식이라 해체가 쉽습니다.",
                "vi": "Sàn gỗ này lắp nổi nên dễ tháo dỡ.",
                "situation": "onsite"
            }
        ],
        "relatedTerms": ["san-nhua", "keo-dan-san", "gach-lat-nen"]
    },
    {
        "slug": "san-nhua",
        "korean": "PVC 바닥재",
        "vietnamese": "sàn nhựa",
        "hanja": None,
        "hanjaReading": None,
        "pronunciation": "피브이씨 바닥재",
        "meaningKo": "폴리염화비닐(PVC) 재질의 바닥 마감재. 통역 시 '장판'과 혼동 주의 - 한국 구어체 '장판'은 베트남에서 sàn nhựa cuộn(롤 타입)과 sàn nhựa hèm khóa(클릭 타입)로 구분. 베트남 시장에서 sàn nhựa는 저가 이미지였으나 최근 SPC(Stone Plastic Composite) 타입은 고급화. 두께(mm)와 wear layer(lớp chịu mài mòn)가 가격 결정 요소. 시공 시 바닥 평탄도(độ phẳng nền) 중요 - 요철 있으면 sàn nhựa가 들뜨므로 사전 레벨링 필수. m² 단가 외 시공비(tiền công) 별도가 일반적.",
        "meaningVi": "Vật liệu lát sàn làm từ PVC, có 2 dạng: sàn nhựa cuộn (giống simili Hàn Quốc) và sàn nhựa hèm khóa (lắp ghép dễ dàng). Loại cao cấp là SPC (kết hợp đá và nhựa), chống nước tốt, dùng được cho nhà bếp và nhà tắm. Độ dày từ 2-6mm, lớp chịu mài mòn (wear layer) từ 0.3-0.7mm quyết định độ bền. Ưu điểm: chống thấm, dễ vệ sinh, giá rẻ hơn sàn gỗ. Nhược điểm: kém sang, dễ trầy xước nếu dùng loại mỏng. Cần nền phẳng mới thi công tốt.",
        "context": "바닥재 시공, 주택/상업 공간 마감",
        "culturalNote": "한국에서 '장판'은 저가 이미지지만 베트남에서 sàn nhựa hèm khóa(클릭형)는 실용적 선택으로 인식. 한국 현장에서 '평당 3만원'이라 해도 베트남은 m² 단가 + 레벨링 비용(làm phẳng nền) 별도 청구가 일반적. SPC sàn nhựa는 베트남어로 sàn nhựa composite đá 또는 그냥 SPC로 통용. 두께 4mm 이상은 상업용, 2-3mm는 주거용이 관행. 베트남 건설 현장에서 sàn nhựa Hàn Quốc(한국산)은 품질 신뢰도가 높으나 중국산 대비 30-50% 비싸므로 가격 비교 필수.",
        "commonMistakes": [
            {
                "mistake": "장판 = sàn nhựa로 직역",
                "correction": "구어: tấm lót sàn, 정식: sàn nhựa (타입 명시 권장)",
                "explanation": "장판은 한국 구어체로, 베트남에서는 cuộn(롤형)인지 hèm khóa(클릭형)인지 명시 필수"
            },
            {
                "mistake": "SPC를 일반 PVC와 동일하게 설명",
                "correction": "SPC = sàn nhựa composite đá (고급형)",
                "explanation": "SPC는 내구성과 방수성이 월등히 높아 가격도 2배 이상. 구분 안 하면 견적 오류"
            },
            {
                "mistake": "시공비 포함하여 평당 가격 제시",
                "correction": "자재비(m²) + 시공비(tiền công) 별도 명시",
                "explanation": "베트남은 자재와 인건비 분리 견적이 관행. 통합 가격 제시 시 오해 발생"
            }
        ],
        "examples": [
            {
                "ko": "SPC 바닥재는 두께 4mm, 방수 등급 IP67입니다.",
                "vi": "Sàn nhựa SPC dày 4mm, chống nước chuẩn IP67.",
                "situation": "formal"
            },
            {
                "ko": "바닥이 울퉁불퉁하면 PVC 시공 전에 레벨링 해야 해요.",
                "vi": "Nếu nền gồ ghề thì phải làm phẳng trước khi lắp sàn nhựa.",
                "situation": "onsite"
            },
            {
                "ko": "이 제품은 클릭형이라 풀 없이 시공 가능합니다.",
                "vi": "Sản phẩm này dạng hèm khóa nên không cần keo.",
                "situation": "onsite"
            }
        ],
        "relatedTerms": ["san-go", "keo-dan-san", "lam-phang-nen"]
    },
    {
        "slug": "tham-trai-san",
        "korean": "카펫",
        "vietnamese": "thảm trải sàn",
        "hanja": None,
        "hanjaReading": None,
        "pronunciation": "카펫",
        "meaningKo": "바닥에 까는 직물 형태의 마감재. 통역 시 '카펫'과 '러그'를 구분해야 함 - 전체 바닥을 덮는 건 thảm trải sàn cố định, 부분용은 thảm lót. 베트남에서 카펫은 호텔/사무실 용도가 주류이며 주거용은 드물다 - 습도와 먼지 관리 때문. 재질(len/양모, sợi tổng hợp/합성섬유)과 pile 높이(độ dày lông thảm)가 가격과 용도 결정. 시공 시 keo dán chuyên dụng(전용 접착제) 사용이 중요하며, 벗겨짐 방지를 위해 nền phẳng(평탄한 바닥) 필수. m² 단가에 시공비 별도가 일반적.",
        "meaningVi": "Vật liệu phủ sàn dạng vải dệt, dùng nhiều cho khách sạn, văn phòng, hội trường. Có 2 loại: thảm trải cố định (dán keo toàn bộ sàn) và thảm lót (để tự do, dễ di chuyển). Chất liệu phổ biến: len (cao cấp, mềm), sợi nylon (bền, rẻ), sợi polypropylene (chống thấm). Độ dày lông thảm (pile height) quyết định cảm giác êm ái. Nhược điểm: dễ bám bụi, cần hút bụi thường xuyên, không phù hợp khí hậu ẩm Việt Nam nếu dùng ở nhà ở. Thi công cần keo chuyên dụng và nền phẳng.",
        "context": "호텔, 사무실, 전시장 바닥재",
        "culturalNote": "한국은 주거 공간에도 카펫 사용이 흔하나 베트남은 습도 때문에 주택에는 거의 안 씀 - 곰팡이와 집먼지 진드기 우려. thảm trải sàn은 주로 5성급 호텔 객실, 대기업 임원실에 국한. 한국 현장에서 '평당 카펫비'로 말하면 베트남 업체는 m² 단가 + 시공 keo dán(접착) 비용 + 운반비(vận chuyển) 별도 청구. 베트남에서 thảm len(양모 카펫)은 수입품이라 관세가 높고, thảm sợi tổng hợp(합성 카펫)이 주류. 청소 유지비(chi phí vệ sinh)가 높아 사전 안내 필수.",
        "commonMistakes": [
            {
                "mistake": "카펫 = thảm (러그까지 포함)",
                "correction": "전면 시공 = thảm trải sàn cố định, 부분용 = thảm lót",
                "explanation": "시공 방식과 범위가 다르므로 구분 필수. 견적서에서 혼동 시 수량 오류"
            },
            {
                "mistake": "재질 구분 없이 thảm으로 통칭",
                "correction": "양모 = thảm len, 합성 = thảm sợi tổng hợp (nylon, PP 등)",
                "explanation": "재질에 따라 가격이 5배 이상 차이. 명시 안 하면 클레임"
            },
            {
                "mistake": "평 단위 견적",
                "correction": "m² 환산 필수 (1평 = 3.3m²)",
                "explanation": "베트남은 m² 기준. 평 사용 시 의사소통 단절"
            }
        ],
        "examples": [
            {
                "ko": "이 카펫은 나일론 소재라 내구성이 좋습니다.",
                "vi": "Thảm này làm từ sợi nylon nên độ bền cao.",
                "situation": "formal"
            },
            {
                "ko": "전용 접착제로 붙여야 벗겨지지 않아요.",
                "vi": "Phải dùng keo chuyên dụng mới không bị bong.",
                "situation": "onsite"
            },
            {
                "ko": "호텔 객실용은 pile 높이 8mm 이상 추천합니다.",
                "vi": "Cho phòng khách sạn nên dùng thảm dày lông 8mm trở lên.",
                "situation": "formal"
            }
        ],
        "relatedTerms": ["keo-dan-tham", "hut-bui-tham", "san-go"]
    },
    {
        "slug": "op-tuong",
        "korean": "벽체 마감",
        "vietnamese": "ốp tường",
        "hanja": "壁體",
        "hanjaReading": "壁(벽 벽) + 體(몸 체)",
        "pronunciation": "벽체 마감",
        "meaningKo": "벽면에 타일, 대리석, 목재 등을 붙여 마감하는 작업. 통역 시 '도배'(giấy dán tường)와 구분 필수 - ốp tường은 단단한 판재 시공을 의미. 베트남에서는 ốp đá(석재), ốp gỗ(목재), ốp gạch(타일)로 재질별 구분이 명확. 시공 방법도 중요: dán ướt(습식 - 시멘트 몰탈), dán khô(건식 - 접착제), lắp khung(프레임 설치)을 구분. 한국에서 '평당 시공비'로 말하면 베트남은 m² 단가 + 자재비(vật liệu) + 인건비(tiền công) 분리 견적. 높이 3m 이상은 비계(giàn giáo) 비용 별도.",
        "meaningVi": "Công việc ốp lát vật liệu cứng lên bề mặt tường như gạch, đá, gỗ. Khác với dán giấy dán tường (mềm), ốp tường dùng vật liệu cứng và bền lâu hơn. Có 3 phương pháp chính: dán ướt (dùng xi măng, cần dưỡng 7 ngày), dán khô (dùng keo, nhanh hơn), lắp khung kẽm (cho tấm ốp nhẹ). Vật liệu phổ biến: gạch men, đá granite, đá marble, gỗ tự nhiên, tấm nhựa giả gỗ. Giá phụ thuộc vào: loại vật liệu, diện tích, chiều cao thi công.",
        "context": "벽면 마감 시공, 인테리어",
        "culturalNote": "한국은 도배(giấy dán tường) 문화가 강하나 베트남은 타일 ốp tường을 선호 - 습기와 내구성 때문. 한국 현장에서 '벽체 마감'이라 하면 베트남 협력업체는 ốp gạch(타일) 또는 ốp đá(석재)로 이해하므로 재질 명시 필수. 베트남에서 ốp đá tự nhiên(천연석)은 고급 마감이나 무게 때문에 dán ướt(습식) 필수 - 접착제만으로는 낙하 위험. 높이 2.4m 이상 시공은 giàn giáo(비계) 설치비 별도 청구가 관행. m² 단가 외 góc cắt(모서리 절단) 추가비 발생 가능.",
        "commonMistakes": [
            {
                "mistake": "도배와 벽체 마감을 ốp tường으로 통칭",
                "correction": "도배 = dán giấy dán tường, 벽체 마감 = ốp tường (재질 명시)",
                "explanation": "도배는 종이/비닐, ốp tường은 타일/석재/목재. 완전히 다른 공정"
            },
            {
                "mistake": "시공비 포함 평당 단가 제시",
                "correction": "자재비 + 시공비(tiền công) 분리, m² 환산",
                "explanation": "베트남은 자재와 인건비 분리 견적. 평 단위는 이해 못 함"
            },
            {
                "mistake": "습식/건식 구분 없이 ốp으로만 설명",
                "correction": "dán ướt(습식) / dán khô(건식) / lắp khung(프레임) 명시",
                "explanation": "시공 기간과 비용이 다르므로 공법 명시 필수"
            }
        ],
        "examples": [
            {
                "ko": "욕실 벽은 습식 공법으로 타일 시공합니다.",
                "vi": "Tường nhà tắm ốp gạch bằng phương pháp dán ướt.",
                "situation": "formal"
            },
            {
                "ko": "대리석 ốp은 무게 때문에 접착제만으로는 안 돼요.",
                "vi": "Ốp đá marble phải dùng xi măng vì nặng, keo không đủ.",
                "situation": "onsite"
            },
            {
                "ko": "3미터 이상 높이는 비계비가 추가됩니다.",
                "vi": "Chiều cao trên 3m phải tính thêm chi phí giàn giáo.",
                "situation": "formal"
            }
        ],
        "relatedTerms": ["gach-op-tuong", "keo-dan-gach", "gian-giao"]
    },
    {
        "slug": "tran-thach-cao",
        "korean": "석고 천장",
        "vietnamese": "trần thạch cao",
        "hanja": "石膏",
        "hanjaReading": "石(돌 석) + 膏(기름 고)",
        "pronunciation": "석고 천장",
        "meaningKo": "석고보드로 만든 천장 마감재. 통역 시 '천장틀'(khung trần)과 '석고보드'(tấm thạch cao)를 구분해야 함 - 한국에서는 통칭하나 베트남은 자재와 골조를 분리 견적. trần thạch cao는 평천장(trần phẳng)과 단차 천장(trần giật cấp)으로 나뉨. 시공 시 khung xương(프레임)은 보통 kẽm mạ kẽm(아연도금 철재)이고, tấm thạch cao는 두께 9.5mm(주거용), 12mm(상업용) 구분. 습기 있는 곳은 tấm chống ẩm(방습 보드) 필수. m² 단가에 sơn hoàn thiện(도장) 비용 별도.",
        "meaningVi": "Vật liệu làm trần nhà bằng tấm thạch cao gắn lên khung xương kẽm. Gồm 2 phần: khung kẽm (xương chính + xương phụ) và tấm thạch cao (dày 9.5mm hoặc 12mm). Có nhiều kiểu: trần phẳng (đơn giản, rẻ), trần giật cấp (nhiều tầng, trang trí), trần hộp (chứa đèn âm). Loại tấm: thạch cao thường (phòng khô), thạch cao chống ẩm (nhà bếp, WC), thạch cao chống cháy (hành lang thoát hiểm). Sau khi lắp cần bả matit, chà nhám, sơn hoàn thiện. Giá tính theo m² bao gồm: khung kẽm + tấm + thi công, sơn thường tính riêng.",
        "context": "천장 마감 시공, 인테리어",
        "culturalNote": "한국은 석고보드 천장이 표준이나 베트남은 타일 천장(trần nhựa, trần nhôm)도 흔함 - 습도와 유지 보수 때문. 한국 현장에서 '평당 석고보드 천장'이라 하면 베트남 업체는 khung kẽm(철재 프레임) + tấm thạch cao + bả matit(퍼티) + sơn(도장)을 모두 별도 항목으로 견적 내므로 총액 확인 필수. 베트남에서 trần thạch cao Hàn Quốc(한국산)은 품질 신뢰도 높으나 중국산 대비 20-30% 비쌈. 3m 이상 높이는 thang nhôm(사다리) 또는 giàn giáo(비계) 비용 추가. tấm chống ẩm(방습 보드)은 tấm thường(일반) 대비 1.5배 가격.",
        "commonMistakes": [
            {
                "mistake": "석고보드 = thạch cao (골조 제외)",
                "correction": "석고보드 천장 = trần thạch cao (khung kẽm + tấm 포함)",
                "explanation": "베트남은 골조와 보드를 분리 견적. 통합 설명 시 금액 오해"
            },
            {
                "mistake": "평 단위 견적",
                "correction": "m² 환산 필수 (1평 = 3.3m²)",
                "explanation": "베트남은 평 개념 없음"
            },
            {
                "mistake": "도장비 포함으로 설명",
                "correction": "trần thạch cao (골조+보드) + sơn hoàn thiện (도장) 분리",
                "explanation": "베트남은 도장을 별도 공정으로 청구하는 게 관행"
            }
        ],
        "examples": [
            {
                "ko": "거실은 단차 천장으로 간접조명 넣을게요.",
                "vi": "Phòng khách làm trần giật cấp để lắp đèn gián tiếp.",
                "situation": "onsite"
            },
            {
                "ko": "욕실은 방습 석고보드 써야 합니다.",
                "vi": "Nhà tắm phải dùng tấm thạch cao chống ẩm.",
                "situation": "formal"
            },
            {
                "ko": "석고보드 12mm, 프레임 60cm 간격으로 시공합니다.",
                "vi": "Dùng tấm thạch cao 12mm, khung kẽm cách nhau 60cm.",
                "situation": "formal"
            }
        ],
        "relatedTerms": ["khung-kem", "ba-matit", "son-nuoc"]
    },
    {
        "slug": "son-lot",
        "korean": "프라이머",
        "vietnamese": "sơn lót",
        "hanja": None,
        "hanjaReading": None,
        "pronunciation": "프라이머",
        "meaningKo": "페인트 칠 전에 바탕면에 바르는 1차 도료. 통역 시 '하도'와 혼용되나 베트남에서는 sơn lót이 정식 용어. 역할은 bám dính(접착력 강화), chống thấm(방수), che lỗ(구멍 메우기). 자재별로 sơn lót gỗ(목재용), sơn lót tường(벽체용), sơn lót sắt(철재용)이 다름 - 혼용 시 박리 발생. 도포량은 m²당 100-150ml가 표준이며, 건조 시간(thời gian khô) 4시간 이상 필수. 프라이머 생략 시 sơn phủ(상도) 수명이 50% 단축되므로 필수 공정임을 강조해야 함.",
        "meaningVi": "Lớp sơn đầu tiên bôi lên bề mặt trước khi sơn màu chính, giúp tăng độ bám dính, chống thấm, che khuyết điểm. Có nhiều loại: sơn lót gỗ (ngăn hút sơn), sơn lót tường (chống kiềm), sơn lót sắt (chống gỉ). Không được dùng nhầm loại vì mỗi loại có công thức riêng. Thông thường cần 1 lớp sơn lót, khô 4-6 tiếng mới sơn màu chính. Nếu bỏ qua bước sơn lót, sơn phủ dễ bong tróc, màu không đều, tốn sơn hơn. Lượng dùng khoảng 100-150ml/m².",
        "context": "도장 작업 사전 처리",
        "culturalNote": "한국 현장에서는 프라이머를 '하도제' 또는 '1차 도료'로 부르나 베트남에서는 sơn lót으로 통일. 한국 업체가 '하도 생략 가능'이라 해도 베트남 협력업체는 sơn lót 필수로 견적 냄 - 습도 때문에 생략 시 하자율 높음. 베트남에서 sơn lót gỗ(목재용)와 sơn lót tường(벽체용)을 혼용하면 bong tróc(박리) 클레임 발생. 건조 시간 단축하려고 quạt thổi(선풍기)로 강제 건조 시 균열 위험 - 자연 건조 권장이 통역 팁. m² 단가에 인건비(tiền công) 별도.",
        "commonMistakes": [
            {
                "mistake": "프라이머 = sơn (페인트로 통칭)",
                "correction": "프라이머 = sơn lót, 상도 = sơn phủ",
                "explanation": "sơn은 '도료' 총칭. lót(밑칠)과 phủ(마감) 구분 필수"
            },
            {
                "mistake": "하도제로 번역",
                "correction": "sơn lót (베트남 표준 용어)",
                "explanation": "'하도제'는 한국 구어체. 베트남에서는 sơn lót이 공식 용어"
            },
            {
                "mistake": "자재 구분 없이 sơn lót으로만 표기",
                "correction": "sơn lót gỗ / sơn lót tường / sơn lót sắt 명시",
                "explanation": "용도별 제품이 다름. 혼용 시 하자 발생"
            }
        ],
        "examples": [
            {
                "ko": "목재는 프라이머 2회 도포 후 상도 칠하세요.",
                "vi": "Gỗ phải sơn lót 2 lớp rồi mới sơn phủ.",
                "situation": "onsite"
            },
            {
                "ko": "프라이머 건조 4시간 후 다음 공정 진행합니다.",
                "vi": "Sau khi sơn lót khô 4 tiếng mới làm tiếp.",
                "situation": "formal"
            },
            {
                "ko": "이 벽은 알칼리가 강해서 전용 프라이머 필요해요.",
                "vi": "Tường này kiềm cao nên cần sơn lót chống kiềm chuyên dụng.",
                "situation": "onsite"
            }
        ],
        "relatedTerms": ["son-phu", "quet-son", "ba-matit"]
    },
    {
        "slug": "keo-dan",
        "korean": "접착제",
        "vietnamese": "keo dán",
        "hanja": "接着劑",
        "hanjaReading": "接(이을 접) + 着(붙을 착) + 劑(약제 제)",
        "pronunciation": "접착제",
        "meaningKo": "두 면을 붙이는 화학 약제. 통역 시 용도별 구분 필수 - keo dán gỗ(목공), keo dán gạch(타일), keo dán giấy(벽지), keo silicone(실란트)는 전부 다름. 베트남에서 keo는 저가 이미지가 있어 고급 제품은 keo chuyên dụng(전용), keo công nghiệp(산업용)으로 강조. 접착력(độ bám dính)과 경화 시간(thời gian đóng rắn)이 핵심 스펙. 시공 환경도 중요: 25-30°C, 습도 60% 이하가 최적. 베트남 습도 70-80%에서는 keo chống ẩm(방습형) 필수. kg당 또는 리터당 가격 제시.",
        "meaningVi": "Chất kết dính hóa học dùng để gắn các bề mặt lại với nhau. Có nhiều loại theo công dụng: keo dán gỗ (PVA, D3, D4), keo dán gạch (xi măng hoặc gốc epoxy), keo dán giấy dán tường, keo silicone (chống thấm mạch nối). Thông số quan trọng: độ bám dính (N/mm²), thời gian đóng rắn (từ 10 phút đến 24 giờ), khả năng chịu nhiệt và chống ẩm. Keo chất lượng cao thường ghi rõ tiêu chuẩn (ISO, EN). Không nên dùng keo giá rẻ cho công trình lớn vì dễ bong tróc. Bảo quản nơi khô ráo, tránh ánh nắng.",
        "context": "건축 자재 접합, 마감 시공",
        "culturalNote": "한국에서 '본드'라는 브랜드명이 일반명사화됐으나 베트남에서는 keo dán이 표준. 한국 현장에서 '접착제'라고만 하면 베트남 협력업체는 용도를 재확인함 - gỗ(목재)/gạch(타일)/giấy(종이) 구분 필수. 베트남 습도 환경에서 일반 keo는 곰팡이(nấm mốc) 발생 위험이 있어 keo chống ẩm(방습형) 권장. 한국산 keo는 품질 신뢰도가 높으나 중국산 대비 2-3배 비싸므로 시방서에 출처 명시 필요. 경화 시간(thời gian đóng rắn) 무시하고 조기 하중 가하면 bong tróc(박리) 발생.",
        "commonMistakes": [
            {
                "mistake": "본드 = keo (브랜드명 직역)",
                "correction": "접착제 = keo dán (용도 명시)",
                "explanation": "'본드'는 한국 브랜드명. 베트남에서는 통하지 않음"
            },
            {
                "mistake": "접착제로만 표기",
                "correction": "keo dán gỗ / keo dán gạch / keo silicone 등 용도 구분",
                "explanation": "용도별 제품이 다름. 명시 안 하면 잘못된 자재 구매"
            },
            {
                "mistake": "kg 단위만 사용",
                "correction": "keo는 kg 또는 lít (액체는 리터)",
                "explanation": "베트남은 액체 접착제를 lít로 거래하는 경우 많음"
            }
        ],
        "examples": [
            {
                "ko": "타일 전용 접착제 사용하세요. 일반 접착제는 안 돼요.",
                "vi": "Phải dùng keo dán gạch chuyên dụng, keo thường không được.",
                "situation": "onsite"
            },
            {
                "ko": "이 접착제는 경화 시간 24시간입니다.",
                "vi": "Keo này thời gian đóng rắn hoàn toàn là 24 giờ.",
                "situation": "formal"
            },
            {
                "ko": "습도 높으면 방습형 접착제 써야 곰팡이 안 생겨요.",
                "vi": "Độ ẩm cao thì phải dùng keo chống ẩm mới không bị nấm mốc.",
                "situation": "onsite"
            }
        ],
        "relatedTerms": ["keo-silicone", "keo-dan-gach", "ron-mach"]
    },
    {
        "slug": "ron-silicone",
        "korean": "실리콘 실란트",
        "vietnamese": "ron silicone",
        "hanja": None,
        "hanjaReading": None,
        "pronunciation": "실리콘 실란트",
        "meaningKo": "실리콘 수지 기반의 틈새 충진 및 방수재. 통역 시 '코킹'과 혼용되나 베트남에서는 ron 또는 keo silicone이 정식 용어. 용도별로 ron vệ sinh(욕실용 - 곰팡이 방지), ron kính(유리용 - 투명), ron xây dựng(건축용 - 내후성)으로 구분. 시공 시 bề mặt sạch khô(청결 건조한 표면) 필수. 경화는 공기 중 수분과 반응이므로 두께 3mm 이상은 내부 미경화 위험. 색상(màu sắc)은 trắng(흰색), trong suốt(투명), đen(검정), màu kem(아이보리) 등. 튜브당(tuýp) 가격 제시.",
        "meaningVi": "Chất trám khe làm từ nhựa silicone, dùng để lấp khe hở, chống thấm nước. Có 3 loại chính: ron vệ sinh (chống nấm mốc, dùng cho nhà tắm), ron kính (trong suốt, dán kính), ron xây dựng (chịu thời tiết, dùng ngoài trời). Bề mặt phải sạch và khô ráo trước khi bơm ron. Độ dày tối đa 5mm để đảm bảo khô đều (ron khô từ ngoài vào trong nhờ hơi ẩm không khí). Màu phổ biến: trắng, trong suốt, đen, kem. Bảo quản tuýp chưa mở ở nhiệt độ thường, sau khi mở dùng hết trong 2 tháng. Giá tính theo tuýp (300ml hoặc 600ml).",
        "context": "방수, 틈새 처리, 유리 시공",
        "culturalNote": "한국에서 '코킹건으로 실리콘 쏜다'는 표현이 흔하나 베트남에서는 bơm ron silicone(실란트를 주입한다)이 정식. 한국 현장에서 '실리콘'으로만 말하면 베트남 협력업체는 용도를 재확인 - vệ sinh(욕실)/kính(유리)/xây dựng(건축) 구분 필수. 베트남 습도 환경에서 일반 ron은 곰팡이(nấm mốc) 발생이 빨라 ron vệ sinh(방곰팡이형) 필수. 한국산 ron silicone은 품질 신뢰도가 높으나 태국산/중국산 대비 2배 비쌈. tuýp 300ml 기준 시공 길이는 폭 5mm 기준 약 12m.",
        "commonMistakes": [
            {
                "mistake": "코킹 = silicone",
                "correction": "코킹(시공 행위) = bơm ron, 실란트(재료) = ron silicone",
                "explanation": "코킹은 '작업'이고 실리콘은 '자재'. 베트남에서는 구분함"
            },
            {
                "mistake": "실리콘으로만 표기",
                "correction": "ron vệ sinh / ron kính / ron xây dựng (용도 명시)",
                "explanation": "용도별 성분이 다름. 욕실용을 유리에 쓰면 황변 발생"
            },
            {
                "mistake": "개 단위로 수량 표기",
                "correction": "tuýp (튜브) 단위 사용",
                "explanation": "베트남은 tuýp 300ml 또는 600ml로 거래"
            }
        ],
        "examples": [
            {
                "ko": "욕실은 곰팡이 방지 실란트 써야 합니다.",
                "vi": "Nhà tắm phải dùng ron vệ sinh chống nấm mốc.",
                "situation": "formal"
            },
            {
                "ko": "유리창 시공에는 투명 실리콘 쓰세요.",
                "vi": "Lắp kính dùng ron trong suốt.",
                "situation": "onsite"
            },
            {
                "ko": "실란트 경화 24시간 후에 물 닿게 하세요.",
                "vi": "Sau khi bơm ron 24 giờ mới cho dính nước.",
                "situation": "onsite"
            }
        ],
        "relatedTerms": ["keo-dan", "chong-tham", "sung-bom-ron"]
    },
    {
        "slug": "tam-op-nhua",
        "korean": "PVC 패널",
        "vietnamese": "tấm ốp nhựa",
        "hanja": None,
        "hanjaReading": None,
        "pronunciation": "피브이씨 패널",
        "meaningKo": "PVC 재질의 벽면/천장 마감용 판재. 통역 시 '플라스틱 패널'보다 tấm ốp nhựa PVC가 정확. 용도별로 tấm ốp tường(벽용), tấm ốp trần(천장용)으로 구분. 베트남에서는 욕실/주방 같은 습기 공간에 선호 - chống thấm(방수), dễ vệ sinh(청소 용이). 두께는 5mm(얇은형), 8mm(표준), 10mm(두꺼운형)로 나뉘며 두꺼울수록 내구성 높지만 무거움. 시공은 lắp khung(프레임 설치) 후 bắt vít(나사 고정) 또는 dán keo(접착). 색상과 무늬(vân gỗ/나무결, vân đá/석재 패턴) 다양. m² 단가 제시.",
        "meaningVi": "Tấm nhựa PVC dùng để ốp tường hoặc trần, phổ biến ở nhà tắm, nhà bếp, ban công. Ưu điểm: chống thấm 100%, nhẹ, lắp nhanh, giá rẻ, dễ vệ sinh. Nhược điểm: kém sang, dễ cháy, không cách âm tốt. Độ dày: 5mm (mỏng, rẻ), 8mm (tiêu chuẩn), 10mm (dày, bền). Kích thước phổ biến: 20cm x 300cm hoặc 25cm x 600cm. Lắp bằng cách: làm khung gỗ hoặc kẽm, rồi bắt vít hoặc dán keo. Có nhiều mẫu: trơn màu, vân gỗ, vân đá. Giá tính theo m², khoảng 50,000-150,000 đồng/m² tùy loại.",
        "context": "욕실, 주방, 천장 마감",
        "culturalNote": "한국은 욕실에 타일(gạch) 선호하나 베트남 저가 주택은 tấm ốp nhựa가 주류 - 시공 속도와 비용 때문. 한국 현장에서 'PVC 패널'로만 말하면 베트남 협력업체는 용도를 재확인 - tường(벽)/trần(천장) 구분 필수. 베트남에서 tấm ốp nhựa vân gỗ(나무 패턴)는 저가 인테리어로 인식되나, 고급 제품(Thái Lan/한국산)은 giả gỗ cao cấp(고급 모조목)으로 차별화. m² 단가 외 khung gỗ(목재 프레임) 또는 khung kẽm(철재 프레임) 비용 별도. 5년 이상 사용 시 vàng úa(황변) 발생 가능 - 자외선 차단 코팅 여부 확인.",
        "commonMistakes": [
            {
                "mistake": "플라스틱 패널 = tấm nhựa (용도 불명확)",
                "correction": "PVC 패널 = tấm ốp nhựa PVC (벽/천장 명시)",
                "explanation": "tấm nhựa는 모든 플라스틱 판을 의미. ốp(마감용) 명시 필수"
            },
            {
                "mistake": "벽과 천장용 구분 없이 판매",
                "correction": "tấm ốp tường / tấm ốp trần 구분",
                "explanation": "천장용은 더 가벼운 제품. 벽용을 천장에 쓰면 처짐 위험"
            },
            {
                "mistake": "장당(장) 단위 견적",
                "correction": "m² 단위 사용",
                "explanation": "베트남은 m² 기준 거래. 판 크기가 다양해 장 단위는 혼란"
            }
        ],
        "examples": [
            {
                "ko": "욕실 천장은 8mm PVC 패널 추천합니다.",
                "vi": "Trần nhà tắm nên dùng tấm ốp nhựa dày 8mm.",
                "situation": "formal"
            },
            {
                "ko": "이 패널은 나무 패턴이라 고급스러워 보여요.",
                "vi": "Tấm này vân gỗ nên trông sang hơn.",
                "situation": "onsite"
            },
            {
                "ko": "프레임 설치 후 나사로 고정하면 됩니다.",
                "vi": "Làm khung xong rồi bắt vít là được.",
                "situation": "onsite"
            }
        ],
        "relatedTerms": ["op-tuong", "tran-nhua", "khung-kem"]
    }
]

# 중복 필터링 (CRITICAL RULE 5)
filtered_terms = [term for term in new_terms if term['slug'] not in existing_slugs]

if not filtered_terms:
    print("⚠️  모든 용어가 이미 존재합니다. 추가할 항목이 없습니다.")
else:
    # 기존 데이터에 추가
    data.extend(filtered_terms)

    # 파일 저장
    with open(file_path, 'w', encoding='utf-8') as f:
        json.dump(data, f, ensure_ascii=False, indent=2)

    print(f"✅ {len(filtered_terms)}개 용어 추가 완료!")
    print(f"📊 총 용어 수: {len(data)}개")
    print("\n추가된 용어:")
    for term in filtered_terms:
        print(f"  - {term['slug']}: {term['korean']} ({term['vietnamese']})")
