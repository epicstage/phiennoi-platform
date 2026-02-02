#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
건설 용어 추가 스크립트 - 목공사/석공사 (Carpentry & Masonry)
Tier S 기준 (90점 이상)
"""

import json
import os

# 추가할 용어 데이터 (10개)
data = [
    {
        "slug": "van-ep",
        "korean": "합판",
        "vietnamese": "Ván ép",
        "hanja": "合板",
        "hanjaReading": "合(합할 합) + 板(널빤지 판)",
        "pronunciation": "합판 / 밴 엡",
        "meaningKo": "여러 겹의 얇은 목재를 결을 교차시켜 접착제로 붙여 만든 판재입니다. 일반 목재보다 변형이 적고 강도가 우수하여 건축 내장재, 가구재, 거푸집 등에 광범위하게 사용됩니다. 통역 시 베트남에서는 '반 엡(Ván ép)' 외에 '반 꽁니엔(Ván công nghiệp, 공업용 판재)'이라는 포괄적 용어도 자주 쓰이므로 문맥을 정확히 파악해야 합니다. 특히 현장에서 합판의 두께(9mm, 12mm, 18mm 등)와 등급(구조용/일반용)을 명확히 구분하여 전달하는 것이 중요합니다.",
        "meaningVi": "Tấm gỗ được làm từ nhiều lớp gỗ mỏng xếp chồng và dán chặt bằng keo. Ván ép có độ bền cao, ít bị cong vênh so với gỗ thường, được dùng phổ biến trong nội thất, đồ gỗ và ván khuôn.",
        "context": "내장 공사, 거푸집 공사, 가구 제작 현장에서 사용",
        "culturalNote": "한국에서는 합판을 두께와 용도에 따라 '구조용 합판', '일반 합판', '코팅 합판' 등으로 세분화하여 부르지만, 베트남 현장에서는 'Ván ép'으로 통칭하고 두께를 숫자로 덧붙이는 경우가 많습니다(예: Ván ép 12mm). 또한 한국은 KS 규격이 엄격하게 적용되지만 베트남은 중국산 저가 합판이 많이 유통되어 품질 편차가 크므로, 통역 시 '등급'과 '원산지'를 명확히 전달해야 합니다.",
        "commonMistakes": [
            {
                "mistake": "Ván gỗ (목재판)",
                "correction": "Ván ép (합판)",
                "explanation": "Ván gỗ는 일반 원목 판재를 의미하여 합판의 적층 구조를 표현하지 못함"
            },
            {
                "mistake": "Gỗ dán (접착 목재)",
                "correction": "Ván ép (합판)",
                "explanation": "Gỗ dán은 집성재를 가리킬 수 있어 합판과 혼동될 수 있음"
            },
            {
                "mistake": "합판을 'MDF'로 혼용",
                "correction": "합판(Ván ép)과 MDF(Ván MDF)는 제조 방식이 다름",
                "explanation": "합판은 목재 단판을 겹친 것, MDF는 목재 섬유를 압축한 것으로 구조가 전혀 다름"
            }
        ],
        "examples": [
            {
                "ko": "거푸집용 합판 18mm 두께로 100장 준비해 주세요.",
                "vi": "Chuẩn bị 100 tấm ván ép 18mm dùng cho ván khuôn.",
                "situation": "onsite"
            },
            {
                "ko": "이 합판은 KS F 3101 구조용 합판 1등급입니다.",
                "vi": "Ván ép này đạt tiêu chuẩn KS F 3101 cấp 1 dùng cho kết cấu.",
                "situation": "formal"
            },
            {
                "ko": "코팅 합판으로 천장 마감할 거예요.",
                "vi": "Chúng tôi sẽ hoàn thiện trần bằng ván ép phủ melamine.",
                "situation": "onsite"
            }
        ],
        "relatedTerms": ["MDF", "석고보드", "거푸집", "목공사"]
    },
    {
        "slug": "van-mdf",
        "korean": "MDF",
        "vietnamese": "Ván MDF",
        "hanja": None,
        "hanjaReading": None,
        "pronunciation": "엠디에프 / 밴 엠디엡",
        "meaningKo": "Medium Density Fiberboard(중밀도 섬유판)의 약자로, 목재를 섬유 상태로 분쇄한 후 접착제와 함께 고온·고압으로 압축 성형한 판재입니다. 표면이 매끄럽고 균일하여 도장이나 라미네이팅에 적합하며, 가구 제작과 내장 마감재로 널리 쓰입니다. 통역 시 '엠디에프'라는 약어가 한국과 베트남 모두 통용되지만, 베트남 현장에서는 종종 '반 엡(합판)'과 혼동하는 경우가 있으므로 '섬유판'임을 강조해야 합니다. 특히 습기에 약한 특성 때문에 방수 MDF 여부를 확인하는 것이 중요합니다.",
        "meaningVi": "Ván sợi mật độ trung bình, làm từ sợi gỗ nghiền nhỏ được ép chặt với keo dưới nhiệt độ và áp suất cao. Bề mặt nhẵn, dễ sơn phủ và gia công, thường dùng trong nội thất và đồ gỗ.",
        "context": "가구 제작, 내장 마감, 도어 제작 현장에서 사용",
        "culturalNote": "한국에서는 MDF를 두께와 밀도에 따라 세분화하여 고밀도(HDF), 중밀도(MDF), 저밀도(LDF)로 구분하지만, 베트남 현장에서는 대부분 'Ván MDF'로 통칭합니다. 한국은 친환경 포름알데히드 방출 등급(E0, E1)을 중시하지만, 베트남은 저가 중국산 MDF가 많아 유해물질 기준이 느슨한 편입니다. 통역 시 건강 안전 기준을 명확히 전달하고, 방수 MDF(MDF chống ẩm) 여부를 확인해야 합니다.",
        "commonMistakes": [
            {
                "mistake": "Ván gỗ công nghiệp (공업용 목재판)",
                "correction": "Ván MDF (MDF 판재)",
                "explanation": "Ván gỗ công nghiệp은 합판, MDF, 파티클보드를 모두 포함하는 광의 개념"
            },
            {
                "mistake": "MDF를 '합판'으로 번역",
                "correction": "MDF는 섬유판, 합판은 단판 적층",
                "explanation": "제조 방식과 물성이 완전히 다르므로 명확히 구분 필요"
            },
            {
                "mistake": "Ván ép sợi (섬유 압착판)",
                "correction": "Ván MDF (엠디에프)",
                "explanation": "기술적으로는 맞지만 현장에서는 'Ván MDF'가 표준 용어"
            }
        ],
        "examples": [
            {
                "ko": "방수 MDF 18mm로 주방 수납장 제작해 주세요.",
                "vi": "Làm tủ bếp bằng ván MDF chống ẩm 18mm.",
                "situation": "onsite"
            },
            {
                "ko": "이 MDF는 E0 등급으로 포름알데히드 방출량이 극히 낮습니다.",
                "vi": "Ván MDF này đạt chuẩn E0, lượng phát thải formaldehyde cực thấp.",
                "situation": "formal"
            },
            {
                "ko": "MDF 표면에 멜라민 시트 붙여서 마감할게요.",
                "vi": "Chúng tôi sẽ dán tấm melamine lên bề mặt ván MDF để hoàn thiện.",
                "situation": "onsite"
            }
        ],
        "relatedTerms": ["합판", "파티클보드", "멜라민시트", "내장공사"]
    },
    {
        "slug": "tam-thach-cao",
        "korean": "석고보드",
        "vietnamese": "Tấm thạch cao",
        "hanja": "石膏보드",
        "hanjaReading": "石(돌 석) + 膏(기름 고)",
        "pronunciation": "석고보드 / 땀 탁까오",
        "meaningKo": "석고(황산칼슘)를 심재로 하고 양면을 종이로 피복한 건축 내장재로, 건식벽체 공법의 핵심 자재입니다. 시공이 빠르고 화재에 강하며 방음·단열 성능이 우수하여 천장, 벽체, 칸막이 등에 광범위하게 사용됩니다. 통역 시 베트남에서는 프랑스어 영향으로 'Placoplatre(플라코플라트르)'라는 브랜드명을 일반명사처럼 쓰는 경우가 많으므로 주의해야 합니다. 또한 일반형, 방수형, 방화형 등 종류를 명확히 구분하여 전달하는 것이 중요합니다.",
        "meaningVi": "Tấm xây dựng có lõi thạch cao được bọc hai mặt bằng giấy chuyên dụng. Được dùng phổ biến cho vách ngăn, trần nhà và tường bên trong nhờ khả năng chống cháy, cách âm và thi công nhanh.",
        "context": "건식벽체 공사, 천장 공사, 칸막이 공사 현장에서 사용",
        "culturalNote": "한국에서는 석고보드를 KS 규격에 따라 일반형(백색), 방수형(녹색), 방화형(분홍색) 등으로 색상 코드화하여 구분하지만, 베트남은 이러한 색상 구분이 덜 보편화되어 있어 '종류'를 명시적으로 설명해야 합니다. 또한 베트남에서는 프랑스 식민지 영향으로 'Placo'(프랑스 브랜드)를 석고보드의 대명사처럼 쓰므로, 현장에서 'Tấm thạch cao' 대신 'Placo'라고 하는 경우가 많습니다. 두께는 한국과 동일하게 9.5mm, 12.5mm가 표준입니다.",
        "commonMistakes": [
            {
                "mistake": "Tấm xi măng (시멘트 판)",
                "correction": "Tấm thạch cao (석고보드)",
                "explanation": "시멘트판은 무겁고 습식 공법에 쓰이며, 석고보드는 가볍고 건식 공법용"
            },
            {
                "mistake": "Placo (브랜드명)",
                "correction": "Tấm thạch cao (일반명사)",
                "explanation": "Placo는 프랑스 브랜드명이지만 베트남에서 일반화되어 주의 필요"
            },
            {
                "mistake": "석고보드를 '천장재'로만 한정",
                "correction": "벽체, 천장, 칸막이 모두 사용 가능",
                "explanation": "석고보드는 다목적 내장재이므로 용도를 명확히 구분"
            }
        ],
        "examples": [
            {
                "ko": "방수 석고보드 12.5mm로 화장실 벽체 시공합니다.",
                "vi": "Thi công tường nhà vệ sinh bằng tấm thạch cao chống ẩm 12.5mm.",
                "situation": "onsite"
            },
            {
                "ko": "이 석고보드는 KS F 3504 방화 1급 인증 제품입니다.",
                "vi": "Tấm thạch cao này đạt chứng nhận chống cháy cấp 1 theo KS F 3504.",
                "situation": "formal"
            },
            {
                "ko": "천장에 이중 석고보드 시공해서 방음 강화할게요.",
                "vi": "Chúng tôi sẽ lắp hai lớp tấm thạch cao ở trần để tăng cường cách âm.",
                "situation": "onsite"
            }
        ],
        "relatedTerms": ["경량칸막이", "건식벽체", "천장틀", "메탈스터드"]
    },
    {
        "slug": "vach-ngan-khung-thep-nhe",
        "korean": "경량칸막이",
        "vietnamese": "Vách ngăn khung thép nhẹ",
        "hanja": "輕量間막이",
        "hanjaReading": "輕(가벼울 경) + 量(헤아릴 량) + 間(사이 간)",
        "pronunciation": "경량칸막이 / 박 응안 쿵 텝 녜",
        "meaningKo": "경량 철골(메탈 스터드)로 골조를 세우고 양면에 석고보드를 부착하여 만드는 비내력 벽체 시스템입니다. 습식 공법에 비해 공기 단축, 경량화, 시공 용이성 등의 장점이 있어 사무실, 상업시설의 내부 칸막이로 널리 사용됩니다. 통역 시 '경량칸막이'는 한국 특유의 복합 용어이므로 베트남어로는 '가벼운 철골 틀 칸막이(Vách ngăn khung thép nhẹ)' 또는 '건식 칸막이(Vách ngăn khô)'로 풀어서 설명해야 합니다. 특히 방음 성능과 내화 성능을 명시하는 것이 중요합니다.",
        "meaningVi": "Hệ thống vách ngăn không chịu lực được làm từ khung thép mạ kẽm nhẹ (metal stud) kết hợp tấm thạch cao hai mặt. Thi công nhanh, nhẹ, không cần vữa xi măng, thường dùng cho văn phòng và công trình thương mại.",
        "context": "사무실 인테리어, 상업시설 내부 공사, 병원·학교 칸막이 공사에서 사용",
        "culturalNote": "한국에서는 '경량칸막이'라는 단어가 건설 현장에서 보편적으로 통용되지만, 베트남에서는 'Vách ngăn khung thép nhẹ'(가벼운 철골 칸막이) 또는 'Vách ngăn khô'(건식 칸막이)라는 긴 표현을 써야 정확히 전달됩니다. 한국은 방음 등급(50dB, 55dB 등)을 엄격히 구분하지만, 베트남은 아직 관련 기준이 느슨한 편입니다. 또한 한국은 내화 구조 인증(1시간, 2시간)을 중시하므로 통역 시 이를 명확히 전달해야 합니다.",
        "commonMistakes": [
            {
                "mistake": "Tường ngăn (일반 벽)",
                "correction": "Vách ngăn khung thép nhẹ (경량 철골 칸막이)",
                "explanation": "Tường ngăn은 습식 벽체를 포함하므로 건식 경량칸막이와 구분 필요"
            },
            {
                "mistake": "Vách thạch cao (석고 칸막이)",
                "correction": "Vách ngăn khung thép nhẹ (경량칸막이)",
                "explanation": "석고보드는 마감재일 뿐, 골조는 철골 프레임이므로 전체 시스템 명칭 사용"
            },
            {
                "mistake": "'경량칸막이'를 '이동식 파티션'으로 오역",
                "correction": "경량칸막이는 고정형, 이동식 파티션은 Vách ngăn di động",
                "explanation": "경량칸막이는 구조물에 고정되어 철거 전까지 유지되는 벽체"
            }
        ],
        "examples": [
            {
                "ko": "사무실 전체를 경량칸막이로 구획하고 방음재 충진하세요.",
                "vi": "Chia toàn bộ văn phòng bằng vách ngăn khung thép nhẹ và nhồi bông tiêu âm.",
                "situation": "onsite"
            },
            {
                "ko": "이 경량칸막이는 차음 성능 50dB, 내화 1시간 성능입니다.",
                "vi": "Vách ngăn này đạt khả năng cách âm 50dB và chống cháy 1 giờ.",
                "situation": "formal"
            },
            {
                "ko": "경량칸막이 골조는 75mm 메탈 스터드 사용합니다.",
                "vi": "Khung vách ngăn sử dụng thanh thép metal stud 75mm.",
                "situation": "onsite"
            }
        ],
        "relatedTerms": ["석고보드", "메탈스터드", "건식벽체", "차음재"]
    },
    {
        "slug": "nan-chan-nang",
        "korean": "루버",
        "vietnamese": "Nan chắn nắng",
        "hanja": None,
        "hanjaReading": None,
        "pronunciation": "루버 / 난 쩐 낭",
        "meaningKo": "일정 간격으로 평행하게 배열된 가늘고 긴 판재로, 빛과 바람은 통하되 직사광선과 시선은 차단하는 건축 요소입니다. 외부 파사드의 차양 장치나 실내 천장·벽면의 디자인 요소로 활용되며, 알루미늄, 목재, PVC 등 다양한 소재로 제작됩니다. 통역 시 베트남어 'Nan chắn nắng'은 '햇빛 가림 날개'라는 뜻으로, 주로 외부 차양 루버를 지칭하므로 실내 디자인 루버는 'Nan trang trí'(장식 날개)로 구분하여 설명하는 것이 좋습니다.",
        "meaningVi": "Hệ thống thanh nan song song được bố trí cách đều nhau, cho phép ánh sáng và gió lưu thông nhưng ngăn ánh nắng trực tiếp và tầm nhìn. Dùng làm che nắng mặt ngoài hoặc trang trí nội thất, có thể làm từ nhôm, gỗ, PVC.",
        "context": "외장 파사드 공사, 실내 천장 마감, 통풍구 설치 현장에서 사용",
        "culturalNote": "한국에서는 '루버'라는 외래어가 건축 현장에서 보편적으로 쓰이지만, 베트남에서는 'Nan chắn nắng'(햇빛 차단 날개)이라는 베트남어 고유 표현이 더 자연스럽습니다. 한국은 알루미늄 루버를 많이 쓰지만, 베트남은 열대 기후 때문에 목재 루버의 부식 문제로 PVC나 알루미늄을 선호합니다. 또한 한국은 고정형 루버가 많지만, 베트남은 각도 조절 가능한 가동형 루버를 선호하는 경향이 있어 'Nan điều chỉnh'(조절 가능 루버) 여부를 확인해야 합니다.",
        "commonMistakes": [
            {
                "mistake": "Rèm (커튼)",
                "correction": "Nan chắn nắng (루버)",
                "explanation": "Rèm은 천 소재 커튼, 루버는 단단한 판재로 만든 구조물"
            },
            {
                "mistake": "Mái che (지붕 차양)",
                "correction": "Nan chắn nắng (루버)",
                "explanation": "Mái che는 지붕형 차양, 루버는 날개형 차양 구조"
            },
            {
                "mistake": "루버를 '블라인드'로 혼용",
                "correction": "루버는 건축 구조물, 블라인드는 실내 창호 부속",
                "explanation": "루버는 고정 건축 요소, 블라인드는 가동식 실내 창문 가림"
            }
        ],
        "examples": [
            {
                "ko": "남측 외벽에 알루미늄 루버 설치해서 일사 차단하세요.",
                "vi": "Lắp nan chắn nắng bằng nhôm ở tường phía nam để chặn ánh nắng.",
                "situation": "onsite"
            },
            {
                "ko": "이 루버는 각도 조절 가능한 가동형입니다.",
                "vi": "Nan chắn nắng này là loại điều chỉnh được góc nghiêng.",
                "situation": "formal"
            },
            {
                "ko": "천장에 목재 루버 달아서 공간감 살릴게요.",
                "vi": "Chúng tôi sẽ lắp nan gỗ trên trần để tạo chiều sâu không gian.",
                "situation": "onsite"
            }
        ],
        "relatedTerms": ["파사드", "차양", "알루미늄패널", "커튼월"]
    },
    {
        "slug": "op-lat-da",
        "korean": "석재마감",
        "vietnamese": "Ốp lát đá",
        "hanja": "石材마감",
        "hanjaReading": "石(돌 석) + 材(재목 재)",
        "pronunciation": "석재마감 / 업 랏 다",
        "meaningKo": "화강석, 대리석, 석회석 등 천연석이나 인조석을 벽면 또는 바닥에 붙이거나 깔아서 마감하는 공법입니다. 고급스러운 외관과 내구성을 제공하며, 로비·현관·외벽 등에 주로 사용됩니다. 통역 시 '석재'는 종류(화강석/대리석)와 가공 방식(버너구이/물갈기/혹두기), 시공 방법(습식/건식)을 명확히 구분하여 전달해야 합니다. 베트남은 습식 공법이 주류이지만 한국은 건식 앵커 공법도 많이 쓰이므로 공법 차이를 주의해야 합니다.",
        "meaningVi": "Phương pháp hoàn thiện bề mặt tường hoặc sàn bằng cách ốp hoặc lát đá tự nhiên (granite, marble, limestone) hoặc đá nhân tạo. Tạo vẻ sang trọng, bền vững, thường dùng cho sảnh, lối vào và tường ngoài.",
        "context": "고급 건물 로비, 호텔·상업시설 외벽, 주택 현관 마감 공사에서 사용",
        "culturalNote": "한국에서는 석재를 '화강석(granite)', '대리석(marble)', '석회석(limestone)' 등으로 정확히 구분하여 부르지만, 베트남 현장에서는 모두 'Đá'(돌)로 통칭하고 색상이나 무늬로 구분하는 경우가 많아 혼동이 생길 수 있습니다. 한국은 건식 앵커 공법(thép neo)을 많이 쓰지만, 베트남은 습식 시멘트 공법이 주류입니다. 또한 한국은 버너구이(nung), 물갈기(đánh bóng) 등 표면 마감 방식을 중시하므로 이를 명확히 전달해야 합니다.",
        "commonMistakes": [
            {
                "mistake": "Gạch đá (석재 타일)",
                "correction": "Đá tự nhiên (천연 석재) 또는 Ốp lát đá (석재 마감)",
                "explanation": "Gạch đá는 세라믹 타일처럼 들릴 수 있어 천연석임을 강조 필요"
            },
            {
                "mistake": "화강석과 대리석을 모두 'Marble'로 번역",
                "correction": "화강석=Granite, 대리석=Marble",
                "explanation": "물성과 가격이 다르므로 정확한 구분 필수"
            },
            {
                "mistake": "습식/건식 공법 구분 없이 'Ốp đá'로만 표현",
                "correction": "습식=Ốp ướt, 건식=Ốp khô (thép neo)",
                "explanation": "공법에 따라 비용과 공기가 크게 달라지므로 명시 필요"
            }
        ],
        "examples": [
            {
                "ko": "로비 벽면에 이태리 대리석으로 석재마감 시공하세요.",
                "vi": "Ốp tường sảnh bằng đá marble Ý.",
                "situation": "onsite"
            },
            {
                "ko": "이 화강석은 버너구이 마감으로 미끄럼 방지 처리되어 있습니다.",
                "vi": "Đá granite này được xử lý mặt nung để chống trơn trượt.",
                "situation": "formal"
            },
            {
                "ko": "외벽 석재는 건식 앵커 공법으로 시공합니다.",
                "vi": "Đá ốp tường ngoài sẽ thi công bằng phương pháp neo thép khô.",
                "situation": "onsite"
            }
        ],
        "relatedTerms": ["화강석", "대리석", "타일공사", "앵커공법"]
    },
    {
        "slug": "da-granite",
        "korean": "화강석",
        "vietnamese": "Đá granite",
        "hanja": "花崗石",
        "hanjaReading": "花(꽃 화) + 崗(언덕 강) + 石(돌 석)",
        "pronunciation": "화강석 / 다 그라닛",
        "meaningKo": "화성암의 일종으로, 석영·장석·운모 등의 광물로 이루어진 단단하고 내구성이 뛰어난 천연석입니다. 회색, 분홍색, 검은색 등 다양한 색상이 있으며, 건물 외벽·바닥·계단 등에 광범위하게 사용됩니다. 대리석보다 단단하여 외부 마감재로 적합합니다. 통역 시 베트남에서는 '그라닛(Granite)'이라는 영어 표현이 보편적으로 통용되며, 원산지(중국산/인도산/한국산)에 따라 품질과 가격 차이가 크므로 출처를 명확히 해야 합니다.",
        "meaningVi": "Đá magma tự nhiên cứng và bền, gồm thạch anh, feldspar và mica. Có nhiều màu (xám, hồng, đen), thường dùng cho tường ngoài, sàn, cầu thang. Cứng hơn đá marble nên phù hợp cho ngoại thất.",
        "context": "건물 외벽, 바닥재, 계단 마감, 기념비·조형물 공사에서 사용",
        "culturalNote": "한국에서는 '화강석'이라는 한자어가 공식 명칭이지만, 베트남은 프랑스 식민지 영향으로 'Granite'이라는 영어-프랑스어 혼용 표현이 더 보편적입니다. 한국은 포천석, 거창석 등 산지별 브랜드가 발달했지만, 베트남은 중국산 저가 화강석이 대량 유통되어 품질 편차가 큽니다. 통역 시 원산지(한국/중국/인도)와 등급(A급/B급)을 명확히 전달하고, 표면 마감 방식(물갈기/버너구이/혹두기)을 구분해야 합니다.",
        "commonMistakes": [
            {
                "mistake": "Đá hoa (대리석)",
                "correction": "Đá granite (화강석)",
                "explanation": "Đá hoa는 대리석(marble)을 가리키며, 화강석과 완전히 다른 석재"
            },
            {
                "mistake": "Đá tự nhiên (천연석)",
                "correction": "Đá granite (화강석)",
                "explanation": "천연석은 화강석, 대리석, 석회석 등을 모두 포함하는 광의 개념"
            },
            {
                "mistake": "화강석을 'Marble'로 오역",
                "correction": "Granite ≠ Marble",
                "explanation": "화강석은 화성암, 대리석은 변성암으로 광물 구성과 물성이 다름"
            }
        ],
        "examples": [
            {
                "ko": "외벽에 거창 화강석 버너구이 마감으로 시공하세요.",
                "vi": "Ốp tường ngoài bằng đá granite Geochang xử lý mặt nung.",
                "situation": "onsite"
            },
            {
                "ko": "이 화강석은 한국산 A급 원석으로 색상이 균일합니다.",
                "vi": "Đá granite này là nguyên liệu cấp A từ Hàn Quốc, màu đồng đều.",
                "situation": "formal"
            },
            {
                "ko": "바닥재는 화강석 물갈기 마감, 600×600 규격입니다.",
                "vi": "Sàn lát đá granite đánh bóng, kích thước 600×600mm.",
                "situation": "onsite"
            }
        ],
        "relatedTerms": ["대리석", "석재마감", "버너구이", "물갈기"]
    },
    {
        "slug": "da-marble",
        "korean": "대리석",
        "vietnamese": "Đá marble",
        "hanja": "大理石",
        "hanjaReading": "大(큰 대) + 理(다스릴 리) + 石(돌 석)",
        "pronunciation": "대리석 / 다 마블",
        "meaningKo": "석회암이 변성작용을 받아 생성된 결정질 천연석으로, 아름다운 무늬와 광택이 특징입니다. 화강석보다 무르지만 고급스러운 외관 때문에 실내 벽면, 바닥, 조형물 등에 널리 사용됩니다. 이태리 카라라 대리석, 터키 트라버틴 등이 유명합니다. 통역 시 베트남에서는 'Đá hoa'(꽃 돌)라는 전통 명칭과 'Marble'이라는 외래어를 혼용하므로, 문맥에 따라 적절히 선택해야 합니다. 특히 산성에 약한 특성 때문에 외부 사용 시 주의사항을 전달해야 합니다.",
        "meaningVi": "Đá biến chất từ đá vôi, có vân đẹp và bóng tự nhiên. Mềm hơn granite nhưng sang trọng, thường dùng cho nội thất, tường, sàn và tác phẩm điêu khắc. Đá marble Ý (Carrara) và Thổ Nhĩ Kỳ (Travertine) rất nổi tiếng.",
        "context": "고급 건물 로비, 호텔 욕실, 주택 거실 바닥, 조각 작품에 사용",
        "culturalNote": "한국에서는 '대리석'이라는 한자어가 공식 명칭이지만, 베트남에서는 'Đá hoa'(꽃 무늬 돌)라는 전통 베트남어와 'Marble'이라는 외래어를 모두 씁니다. 특히 고급 프로젝트에서는 'Marble'을, 일반 현장에서는 'Đá hoa'를 더 많이 씁니다. 한국은 이태리·터키산 고급 대리석을 선호하지만, 베트남은 중국산 저가 대리석이 많아 품질 편차가 큽니다. 대리석은 산성에 약하므로 외부 사용 시 빗물 영향을 설명해야 합니다.",
        "commonMistakes": [
            {
                "mistake": "Đá granite (화강석)",
                "correction": "Đá marble (대리석)",
                "explanation": "화강석은 화성암, 대리석은 변성암으로 완전히 다른 석재"
            },
            {
                "mistake": "Đá cẩm thạch (옥석)",
                "correction": "Đá marble (대리석)",
                "explanation": "Đá cẩm thạch는 옥(jade)을 가리키므로 대리석과 혼동하지 말 것"
            },
            {
                "mistake": "대리석을 외부 바닥재로 추천",
                "correction": "대리석은 실내용, 외부는 화강석 권장",
                "explanation": "대리석은 산성비와 마모에 약해 외부 사용 부적합"
            }
        ],
        "examples": [
            {
                "ko": "로비 벽면에 이태리 카라라 대리석으로 마감하세요.",
                "vi": "Ốp tường sảnh bằng đá marble Carrara Ý.",
                "situation": "onsite"
            },
            {
                "ko": "이 대리석은 백색 바탕에 회색 자연 무늬가 있습니다.",
                "vi": "Đá marble này có nền trắng với vân tự nhiên màu xám.",
                "situation": "formal"
            },
            {
                "ko": "욕실 바닥은 대리석 물갈기 마감, 미끄럼 주의하세요.",
                "vi": "Sàn nhà tắm lát đá marble đánh bóng, cẩn thận trơn trượt.",
                "situation": "onsite"
            }
        ],
        "relatedTerms": ["화강석", "석재마감", "트라버틴", "물갈기"]
    },
    {
        "slug": "tuong-kho",
        "korean": "건식벽체",
        "vietnamese": "Tường khô",
        "hanja": "乾式壁體",
        "hanjaReading": "乾(마를 건) + 式(법 식) + 壁(벽 벽) + 體(몸 체)",
        "pronunciation": "건식벽체 / 뜨엉 커",
        "meaningKo": "시멘트 모르타르나 콘크리트 등 물을 사용하는 습식 공법 대신, 석고보드·합판 등 건조된 판재를 경량 철골 프레임에 고정하여 벽체를 구성하는 공법입니다. 공기 단축, 정밀 시공, 경량화 등의 장점이 있어 현대 건축에서 내부 칸막이와 마감재로 널리 사용됩니다. 통역 시 '건식(乾式)'이라는 한자어 개념이 베트남어로 직역하기 어렵지만, 'Tường khô'(마른 벽) 또는 'Tường không dùng vữa'(모르타르 안 쓰는 벽)로 설명할 수 있습니다.",
        "meaningVi": "Phương pháp xây tường không sử dụng vữa xi măng ướt, thay vào đó dùng tấm khô (thạch cao, ván ép) gắn vào khung thép nhẹ. Thi công nhanh, nhẹ, chính xác, thường dùng cho vách ngăn và hoàn thiện nội thất hiện đại.",
        "context": "사무실·주택 내부 칸막이, 천장 공사, 리모델링 공사에서 사용",
        "culturalNote": "한국에서는 '건식벽체'가 건축 표준 용어로 자리잡았지만, 베트남에서는 'Tường khô'(마른 벽)라는 직역어가 아직 생소하여 'Tường thạch cao'(석고보드 벽) 또는 'Vách ngăn khô'(건식 칸막이)라는 구체적 표현을 더 많이 씁니다. 한국은 내화·방음 성능 인증을 중시하지만, 베트남은 관련 규정이 느슨하여 저가 자재를 쓰는 경우가 많습니다. 통역 시 '습식 vs 건식' 개념을 명확히 설명하고, 공기 단축 효과를 강조하는 것이 효과적입니다.",
        "commonMistakes": [
            {
                "mistake": "Tường gạch (벽돌 벽)",
                "correction": "Tường khô (건식벽체)",
                "explanation": "벽돌 벽은 습식 공법, 건식벽체는 판재 조립 공법"
            },
            {
                "mistake": "Tường thạch cao (석고보드 벽)",
                "correction": "Tường khô / Tường vách khô (건식벽체)",
                "explanation": "석고보드는 마감재일 뿐, 건식 시스템 전체를 포괄하는 용어 필요"
            },
            {
                "mistake": "'건식'을 '마른 상태'로만 이해",
                "correction": "'습식 공법(물 사용) vs 건식 공법(판재 조립)'",
                "explanation": "건식은 시공 방식의 차이를 의미하는 기술 용어"
            }
        ],
        "examples": [
            {
                "ko": "이번 리모델링은 전체 건식벽체로 시공해서 공기 단축합니다.",
                "vi": "Dự án cải tạo này sẽ dùng toàn bộ tường khô để rút ngắn thời gian thi công.",
                "situation": "onsite"
            },
            {
                "ko": "건식벽체는 습식 벽돌 공법보다 시공 속도가 3배 빠릅니다.",
                "vi": "Tường khô thi công nhanh gấp 3 lần so với tường gạch ướt.",
                "situation": "formal"
            },
            {
                "ko": "경량칸막이는 대표적인 건식벽체 시스템입니다.",
                "vi": "Vách ngăn khung thép nhẹ là hệ thống tường khô điển hình.",
                "situation": "onsite"
            }
        ],
        "relatedTerms": ["경량칸막이", "석고보드", "메탈스터드", "습식벽체"]
    },
    {
        "slug": "khung-tran",
        "korean": "천장틀",
        "vietnamese": "Khung trần",
        "hanja": "天障틀",
        "hanjaReading": "天(하늘 천) + 障(막을 장)",
        "pronunciation": "천장틀 / 쿵 쩐",
        "meaningKo": "천장 마감재(석고보드, 텍스 등)를 지지하기 위해 설치하는 경량 철골 골조 시스템입니다. 메인 러너(main runner), 크로스 티(cross tee) 등으로 구성되며, 조명·환기구·배관 등을 숨기고 천장 높이를 조절할 수 있습니다. 통역 시 '천장틀'은 한국어 고유 표현이므로 베트남어로는 'Khung trần'(천장 프레임)으로 번역하며, 시스템 천장(trần chìm) 또는 노출 천장(trần nổi) 여부를 명시하는 것이 중요합니다.",
        "meaningVi": "Hệ thống khung thép nhẹ làm kết cấu chịu lực cho trần (thạch cao, trần nổi, v.v.). Gồm thanh chính (main runner) và thanh ngang (cross tee), giúp che đường ống, dây điện và điều chỉnh chiều cao trần.",
        "context": "사무실 천장, 상업시설 천장, 주택 거실 천장 공사에서 사용",
        "culturalNote": "한국에서는 '천장틀'이라는 단순한 명칭을 쓰지만, 베트남에서는 'Khung trần'(천장 프레임) 또는 'Hệ thống trần chìm'(시스템 천장)이라고 부릅니다. 한국은 석고보드 천장이 주류이지만, 베트남은 상업시설에서 노출 천장(trần nổi, T-bar ceiling)을 많이 씁니다. 통역 시 천장 마감재 종류(석고보드/텍스/알루미늄 패널)와 천장 속 설비(조명/배관/덕트)를 함께 설명하면 이해가 쉬워집니다.",
        "commonMistakes": [
            {
                "mistake": "Trần nhà (천장)",
                "correction": "Khung trần (천장틀)",
                "explanation": "Trần nhà는 천장 마감면, Khung trần은 골조 시스템"
            },
            {
                "mistake": "Trần thạch cao (석고보드 천장)",
                "correction": "Khung trần thạch cao (석고보드 천장틀)",
                "explanation": "석고보드는 마감재, 천장틀은 골조를 의미"
            },
            {
                "mistake": "'천장틀'을 '천장 마감'으로 오역",
                "correction": "천장틀=골조, 천장 마감=표면 처리",
                "explanation": "골조와 마감재는 별개의 공정"
            }
        ],
        "examples": [
            {
                "ko": "사무실 천장틀 설치 후 석고보드 부착하세요.",
                "vi": "Lắp khung trần văn phòng xong rồi gắn tấm thạch cao.",
                "situation": "onsite"
            },
            {
                "ko": "이 천장틀은 메인 러너 간격 900mm로 시공합니다.",
                "vi": "Khung trần này thi công với khoảng cách thanh chính 900mm.",
                "situation": "formal"
            },
            {
                "ko": "노출 천장틀 위에 LED 조명 매입할게요.",
                "vi": "Chúng tôi sẽ âm đèn LED vào khung trần nổi.",
                "situation": "onsite"
            }
        ],
        "relatedTerms": ["석고보드", "시스템천장", "메탈스터드", "텍스"]
    }
]

def main():
    """건설 용어 추가 메인 함수"""
    json_path = "/Users/mac/Documents/claude_code/projects/vn.epicstage.co.kr/src/data/terms/construction.json"

    # 기존 데이터 읽기
    with open(json_path, "r", encoding="utf-8") as f:
        existing_data = json.load(f)

    print(f"기존 용어 수: {len(existing_data)}")

    # 중복 체크 (slug 기준)
    existing_slugs = {term["slug"] for term in existing_data}
    new_terms = [term for term in data if term["slug"] not in existing_slugs]

    if not new_terms:
        print("⚠️  추가할 신규 용어 없음 (모두 중복)")
        return

    print(f"신규 용어 수: {len(new_terms)}")

    # 기존 데이터에 추가
    existing_data.extend(new_terms)

    # 저장
    with open(json_path, "w", encoding="utf-8") as f:
        json.dump(existing_data, f, ensure_ascii=False, indent=2)

    print(f"✅ 완료! 총 용어 수: {len(existing_data)}")
    print("\n추가된 용어:")
    for term in new_terms:
        print(f"  - {term['korean']} ({term['vietnamese']})")

if __name__ == "__main__":
    main()
