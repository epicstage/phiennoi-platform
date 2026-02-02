#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
건축구성요소 용어 10개 추가 스크립트
테마: 처마, 차양, 캐노피, 발코니, 테라스, 필로티, 아트리움, 로비, 코어, 계단실
Tier S 기준 (90점 이상)
"""

import json
import os

# 추가할 용어 데이터
new_terms = [
    {
        "slug": "cheo-nha",
        "korean": "처마",
        "vietnamese": "Chéo nhà",
        "hanja": "處馬",
        "hanjaReading": "處(곳 처) + 馬(말 마)",
        "pronunciation": "처마",
        "meaningKo": "지붕이 외벽보다 돌출되어 비와 햇빛을 막아주는 부분. 베트남어로는 '지붕의 처마'라는 의미의 'chéo nhà'로 표현하며, 프랑스어 영향으로 'auvent'라고도 함. 통역 시 주의할 점은 베트남 전통 가옥의 처마(mái hiên)와 현대 건축의 처마(chéo nhà)를 구분해야 한다는 것. 한국의 처마는 미학적 요소가 강하지만 베트남에서는 실용성(우기 대비)이 더 중요하므로 설명 시 기능적 측면을 강조하는 것이 효과적. '처마 끝 처리'는 'xử lý đầu mái', '처마 높이'는 'độ cao mái hiên'으로 번역.",
        "meaningVi": "Phần mái nhà nhô ra ngoài tường để che mưa và nắng. Trong tiếng Hàn gọi là '처마', thường thấy trong kiến trúc truyền thống Hàn Quốc với tính thẩm mỹ cao. Cần phân biệt với 'mái hiên' - thuật ngữ truyền thống của Việt Nam. Trong bản vẽ kỹ thuật hay ghi là 'chéo nhà' hoặc 'phần nhô mái', chiều dài nhô ra thường từ 0.5-1.5m tùy thiết kế.",
        "context": "건축 설계, 전통 건축, 외장 시공",
        "culturalNote": "한국 전통 건축에서 처마는 건물의 품격을 나타내는 중요한 요소로, 처마 곡선(추녀)의 아름다움이 강조됨. 반면 베트남에서는 실용적 기능(우기 때 비 차단)이 우선시되어 단순한 형태가 많음. 한국의 '기와 처마'는 베트남 통역사에게 'mái ngói kiểu Hàn Quốc'으로 설명하면 이해가 빠름. 현대 건축에서는 양국 모두 차양(canopy) 개념과 혼용되어 사용되므로 맥락에 따라 정확한 용어 선택 필요.",
        "commonMistakes": [
            {
                "mistake": "처마를 'mái nhà'라고만 번역",
                "correction": "'chéo nhà' 또는 'mái hiên'으로 구체화",
                "explanation": "'mái nhà'는 지붕 전체를 의미하므로 처마의 돌출 부분을 표현하지 못함"
            },
            {
                "mistake": "차양(canopy)과 처마를 같은 용어로 번역",
                "correction": "차양은 'mái che', 처마는 'chéo nhà'로 구분",
                "explanation": "차양은 독립적 구조물, 처마는 지붕의 연장선이므로 개념 차이가 명확함"
            },
            {
                "mistake": "'처마 끝'을 'cuối mái'로 직역",
                "correction": "'đầu mái' 또는 'đuôi mái' 사용",
                "explanation": "베트남 건축 용어에서는 'đầu mái'(mái의 끝부분)가 관용적 표현"
            },
            {
                "mistake": "전통 건축 처마를 현대식 용어로 설명",
                "correction": "전통 처마는 'mái hiên truyền thống', 현대는 'chéo nhà hiện đại'",
                "explanation": "건축 양식에 따라 용어가 달라지므로 맥락 구분 필수"
            }
        ],
        "examples": [
            {
                "ko": "처마를 1미터 이상 돌출시켜 빗물이 외벽에 닿지 않도록 설계했습니다.",
                "vi": "Thiết kế chéo nhà nhô ra hơn 1 mét để nước mưa không chạm vào tường ngoài.",
                "situation": "formal"
            },
            {
                "ko": "한옥의 처마 곡선이 아름답게 표현되도록 목공 작업에 세심한 주의가 필요합니다.",
                "vi": "Cần chú ý cẩn thận trong công tác mộc để đường cong mái hiên hanok được thể hiện đẹp mắt.",
                "situation": "onsite"
            },
            {
                "ko": "처마 끝에 홈통을 설치해서 배수 처리를 해야 돼요.",
                "vi": "Phải lắp máng nước ở đầu mái để xử lý thoát nước.",
                "situation": "informal"
            }
        ],
        "relatedTerms": ["차양", "캐노피", "지붕", "홈통", "추녀"]
    },
    {
        "slug": "mai-che",
        "korean": "차양",
        "vietnamese": "Mái che",
        "hanja": "遮陽",
        "hanjaReading": "遮(가릴 차) + 陽(볕 양)",
        "pronunciation": "차양",
        "meaningKo": "햇빛을 가리기 위해 창문이나 출입구 위에 설치하는 덮개. 베트남어로는 'mái che' 또는 'tấm che nắng'으로 표현. 통역 시 주의점은 차양(awning)과 캐노피(canopy)의 구분으로, 차양은 주로 천이나 금속판으로 된 가벼운 구조물을 말하며 접고 펼 수 있는 경우가 많음. 반면 캐노피는 고정식 구조물. 베트남 현장에서는 '차양 프레임'을 'khung mái che', '차양막'을 'bạt che nắng'이라 함. 한국에서 흔한 '전동 차양'은 'mái che tự động'으로 번역하되, 베트남에서는 보급률이 낮아 설명이 필요할 수 있음.",
        "meaningVi": "Tấm che lắp đặt phía trên cửa sổ hoặc lối ra vào để chắn nắng. Trong tiếng Hàn gọi là '차양', thường dùng vật liệu nhẹ như vải bạt hoặc tấm kim loại, có thể gấp mở được. Khác với 'canopy' (mái che cố định lớn), '차양' thường nhỏ gọn và linh hoạt hơn. Phổ biến ở các cửa hàng, nhà hàng, hoặc cửa sổ tầng thấp.",
        "context": "외장 설계, 상업 건축, 주거 인테리어",
        "culturalNote": "한국에서는 카페나 상점에서 브랜드 로고가 새겨진 차양을 많이 사용하며 마케팅 요소로 활용. 베트남에서도 상업 공간에서 유사하게 사용되나, 열대 기후 특성상 더 두껍고 내구성 있는 재질 선호. 한국의 '스트라이프 차양'(sọc kẻ)은 유럽풍 감성으로 인식되며, 베트남에서는 단색 차양이 더 일반적. '접이식 차양'은 한국에서 흔하지만 베트남에서는 고정식이 주류.",
        "commonMistakes": [
            {
                "mistake": "차양과 캐노피를 모두 'mái che'로 번역",
                "correction": "차양은 'mái che' 또는 'tấm che nắng', 캐노피는 'mái đón'",
                "explanation": "캐노피는 규모가 크고 구조적으로 독립된 구조물을 의미함"
            },
            {
                "mistake": "'차양막'을 'màn che'로 번역",
                "correction": "'bạt che nắng' 또는 'vải bạt mái che' 사용",
                "explanation": "'màn'은 커튼을 의미하므로 차양의 천막 재질을 표현하지 못함"
            },
            {
                "mistake": "'전동 차양'을 그냥 'mái che điện'으로만 표현",
                "correction": "'mái che tự động điều khiển bằng điện' (전기로 조작되는 자동 차양)",
                "explanation": "베트남에서 생소한 개념이므로 작동 방식까지 설명 필요"
            },
            {
                "mistake": "차양 각도를 'góc mái che'로만 표현",
                "correction": "'góc độ nghiêng của mái che' (차양의 기울기 각도)",
                "explanation": "각도 조절 기능을 명확히 표현하기 위해 '기울기' 개념 포함"
            }
        ],
        "examples": [
            {
                "ko": "카페 입구에 빨간색 줄무늬 차양을 설치하여 브랜드 정체성을 강화했습니다.",
                "vi": "Lắp đặt mái che sọc đỏ ở lối vào quán cà phê để tăng cường nhận diện thương hiệu.",
                "situation": "formal"
            },
            {
                "ko": "차양 프레임이 녹슬었으니 교체 작업이 필요합니다.",
                "vi": "Khung mái che bị gỉ nên cần thay thế.",
                "situation": "onsite"
            },
            {
                "ko": "여름에는 차양 펼쳐놓고 겨울엔 접어두면 돼요.",
                "vi": "Mùa hè thì mở mái che ra, mùa đông thì gập lại là được.",
                "situation": "informal"
            }
        ],
        "relatedTerms": ["캐노피", "처마", "블라인드", "파라솔", "텐트"]
    },
    {
        "slug": "mai-don",
        "korean": "캐노피",
        "vietnamese": "Mái đón",
        "hanja": None,
        "hanjaReading": None,
        "pronunciation": "캐노피",
        "meaningKo": "출입구나 통로를 덮는 큰 규모의 고정식 지붕 구조물. 영어 'canopy'의 음차어로 베트남어로는 'mái đón'(맞이하는 지붕) 또는 'mái hiên lớn'으로 표현. 통역 시 주의할 점은 차양(awning)보다 구조가 크고 견고하며, 독립적인 기둥으로 지탱된다는 점을 강조해야 함. 한국에서는 호텔 입구, 공항 승하차 구역, 주유소 등에서 볼 수 있으며, 베트남에서도 유사한 용도로 사용. '유리 캐노피'는 'mái đón kính', '철골 캐노피'는 'mái đón thép'으로 번역. 설계 시 배수 처리(thoát nước)와 구조 안전성(an toàn kết cấu)을 반드시 언급해야 베트남 엔지니어와 소통이 원활함.",
        "meaningVi": "Cấu trúc mái lớn cố định che lối vào hoặc khu vực đón tiếp. Trong tiếng Hàn gọi là '캐노피' (canopy), thường thấy ở lối vào khách sạn, sân bay, trạm xăng. Khác với 'mái che' (차양) nhỏ gọn, canopy có quy mô lớn hơn, kết cấu vững chắc hơn và thường được đỡ bằng cột độc lập. Vật liệu phổ biến: kính cường lực, tấm polycarbonate, thép không gỉ.",
        "context": "건축 외장, 상업 시설, 교통 인프라",
        "culturalNote": "한국에서는 호텔이나 고급 건물 입구의 캐노피를 'VIP 진입로'의 상징으로 인식하며 미학적 가치 중시. 베트남에서도 유사하나 열대 우기 대비 기능이 더 강조됨. 한국의 '유리 캐노피'는 현대적 세련미를 주지만, 베트남 현장에서는 강렬한 햇빛으로 인한 온실 효과를 우려하여 차광 처리(lớp phủ chống nắng) 여부를 반드시 확인함. 공항 캐노피는 양국 모두 'mái đón sân bay'로 통용.",
        "commonMistakes": [
            {
                "mistake": "캐노피를 '차양(mái che)'으로 번역",
                "correction": "'mái đón' 또는 'mái hiên lớn' 사용",
                "explanation": "캐노피는 구조적으로 독립된 큰 규모의 구조물이므로 차양과 구분 필요"
            },
            {
                "mistake": "'유리 캐노피'를 'mái kính'으로만 표현",
                "correction": "'mái đón kính cường lực' (강화 유리 캐노피)",
                "explanation": "안전 기준상 일반 유리가 아닌 강화 유리를 사용하므로 재질 명시"
            },
            {
                "mistake": "캐노피 설치를 'lắp mái'로 직역",
                "correction": "'thi công mái đón' 또는 'lắp đặt hệ thống mái đón' 사용",
                "explanation": "단순 설치가 아닌 구조 시공의 개념이므로 'thi công' 사용"
            },
            {
                "mistake": "'캐노피 기둥'을 'cột mái'로만 표현",
                "correction": "'cột đỡ mái đón' (캐노피를 지지하는 기둥)",
                "explanation": "기능을 명확히 표현하여 구조적 역할 강조"
            }
        ],
        "examples": [
            {
                "ko": "호텔 정문에 10미터 길이의 유리 캐노피를 설치하여 고급스러운 이미지를 연출했습니다.",
                "vi": "Lắp đặt mái đón kính dài 10 mét ở cổng chính khách sạn để tạo hình ảnh sang trọng.",
                "situation": "formal"
            },
            {
                "ko": "캐노피 기둥이 차량 동선을 방해하지 않도록 위치 조정이 필요합니다.",
                "vi": "Cần điều chỉnh vị trí cột đỡ mái đón để không cản trở động선 xe.",
                "situation": "onsite"
            },
            {
                "ko": "비 올 때 캐노피 아래에서 택시 기다리면 돼요.",
                "vi": "Trời mưa thì đợi taxi dưới mái đón là được.",
                "situation": "informal"
            }
        ],
        "relatedTerms": ["차양", "처마", "포치", "현관", "주차캐노피"]
    },
    {
        "slug": "ban-cong",
        "korean": "발코니",
        "vietnamese": "Ban công",
        "hanja": None,
        "hanjaReading": None,
        "pronunciation": "발코니",
        "meaningKo": "건물 외벽에서 돌출되어 외부 공기와 접하는 공간. 영어 'balcony'의 음차어로 베트남어로는 'ban công'이라 함. 통역 시 주의점은 한국의 '확장 발코니'와 '비확장 발코니' 개념을 베트남어로 설명하기 어렵다는 것. '발코니 확장'은 'mở rộng ban công thành phòng'(발코니를 방으로 확장), '비확장'은 'giữ nguyên ban công'(발코니를 원래 상태로 유지)로 풀어서 설명. 베트남에서는 발코니를 빨래 건조 공간으로 주로 사용하므로, 한국식 확장 발코니 개념은 'không gian sinh hoạt mở rộng'(확장된 생활 공간)으로 설명하는 것이 효과적.",
        "meaningVi": "Không gian nhô ra ngoài tường bên ngoài tòa nhà, tiếp xúc với không khí bên ngoài. Trong tiếng Hàn gọi là '발코니' (balcony). Ở Hàn Quốc có khái niệm 'balcony mở rộng' (확장 발코니) - biến ban công thành một phần của phòng bằng cách lắp cửa kính và sưởi ấm, khác với ban công truyền thống để phơi đồ. Cần phân biệt với '테라스' (terrace) - không gian ngoài trời rộng hơn ở tầng thấp.",
        "context": "주거 건축, 아파트 설계, 인테리어",
        "culturalNote": "한국에서는 발코니 확장이 일반화되어 거실의 연장 공간으로 활용하며, 불법 확장 문제도 존재. 베트남에서는 발코니를 실용적 공간(빨래, 화분)으로 사용하며 확장 개념이 드물어 설명 필요. 한국의 '드레스룸으로 확장한 발코니'는 베트남 통역사에게 생소한 개념이므로 'ban công được cải tạo thành phòng thay đồ'로 구체적 설명 필요. 안전 난간 기준도 양국 차이 있음(한국 1.2m, 베트남 1.1m).",
        "commonMistakes": [
            {
                "mistake": "'발코니 확장'을 'mở rộng ban công'으로만 번역",
                "correction": "'mở rộng ban công thành không gian sinh hoạt' (생활 공간으로 발코니 확장)",
                "explanation": "단순 면적 확장이 아닌 실내 공간으로의 전환 개념을 명확히 해야 함"
            },
            {
                "mistake": "발코니와 테라스를 모두 'ban công'으로 번역",
                "correction": "발코니는 'ban công', 테라스는 'sân thượng' 또는 'không gian ngoài trời'",
                "explanation": "테라스는 지상층 또는 옥상의 넓은 외부 공간을 의미하므로 구분 필요"
            },
            {
                "mistake": "'발코니 난간'을 'lan can'으로만 표현",
                "correction": "'lan can ban công' (발코니 난간) 또는 'tay vịn an toàn'",
                "explanation": "'lan can'은 일반적 난간이므로 발코니 안전 난간임을 명시"
            },
            {
                "mistake": "'발코니 새시'를 'cửa ban công'으로 번역",
                "correction": "'hệ thống cửa kính ban công' (발코니 유리창 시스템)",
                "explanation": "'새시'는 창틀 시스템을 의미하므로 'hệ thống cửa kính' 사용"
            }
        ],
        "examples": [
            {
                "ko": "이 아파트는 거실 발코니를 확장하여 12평형보다 넓게 사용할 수 있습니다.",
                "vi": "Căn hộ này mở rộng ban công phòng khách nên có thể sử dụng rộng hơn diện tích 12 평.",
                "situation": "formal"
            },
            {
                "ko": "발코니 방수 작업이 제대로 안 되어서 누수가 발생했습니다.",
                "vi": "Công tác chống thấm ban công không đạt nên bị thấm nước.",
                "situation": "onsite"
            },
            {
                "ko": "발코니에서 빨래 널고 화분도 키워요.",
                "vi": "Phơi đồ và trồng cây ở ban công.",
                "situation": "informal"
            }
        ],
        "relatedTerms": ["테라스", "베란다", "난간", "새시", "확장"]
    },
    {
        "slug": "san-thuong",
        "korean": "테라스",
        "vietnamese": "Sân thượng",
        "hanja": None,
        "hanjaReading": None,
        "pronunciation": "테라스",
        "meaningKo": "건물의 지상층 또는 상층에 위치한 넓은 외부 공간. 영어 'terrace'의 음차어로 베트남어로는 'sân thượng'(옥상 마당) 또는 'không gian ngoài trời'로 표현. 통역 시 주의할 점은 한국의 '루프탑 테라스'와 '1층 테라스'를 구분하는 것. 옥상 테라스는 'sân thượng', 1층 테라스는 'sân ngoài tầng 1' 또는 'khoảng sân'으로 번역. 베트남에서는 테라스를 카페나 레스토랑의 야외 좌석 공간으로 많이 활용하며, 한국의 아파트 '테라스 하우스'는 'nhà có sân thượng riêng'으로 설명. 발코니보다 면적이 넓고 지붕이 없거나 부분적으로만 있다는 점을 강조.",
        "meaningVi": "Không gian ngoài trời rộng ở tầng trệt hoặc tầng cao của tòa nhà. Trong tiếng Hàn gọi là '테라스' (terrace), khác với 'ban công' (발코니) vì có diện tích lớn hơn và thường không có mái che hoặc chỉ che một phần. Phổ biến ở các quán cà phê, nhà hàng như khu vực ngồi ngoài trời. Trong căn hộ cao cấp, '테라스 하우스' là loại căn có sân thượng riêng biệt.",
        "context": "주거 건축, 상업 공간, 조경 설계",
        "culturalNote": "한국에서는 '루프탑 테라스'가 카페나 바의 인기 공간으로 자리잡았으며, 아파트에서도 프리미엄 옵션으로 인식됨. 베트남에서도 도심 카페의 옥상 테라스가 인기 있으나, 열대 기후 특성상 그늘막(mái che) 설치가 필수. 한국의 '1층 테라스 정원'은 베트남에서 'sân vườn tầng trệt'로 표현하며, 프랑스 식민지 영향으로 빌라 스타일에서 흔히 볼 수 있음. '테라스 가구'는 양국 모두 'nội thất ngoài trời'로 통용.",
        "commonMistakes": [
            {
                "mistake": "테라스와 발코니를 구분 없이 'ban công'으로 번역",
                "correction": "테라스는 'sân thượng' 또는 'không gian ngoài trời', 발코니는 'ban công'",
                "explanation": "테라스는 면적이 넓고 지붕이 없는 공간, 발코니는 돌출된 작은 공간"
            },
            {
                "mistake": "'루프탑 테라스'를 'mái nhà'로 번역",
                "correction": "'sân thượng' 또는 'khu vực tầng thượng' 사용",
                "explanation": "'mái nhà'는 지붕 자체를 의미하므로 활용 공간 개념과 다름"
            },
            {
                "mistake": "'테라스 하우스'를 그냥 'nhà có sân'으로 번역",
                "correction": "'căn hộ có sân thượng riêng' (전용 옥상이 있는 집)",
                "explanation": "아파트 내 특별한 유닛 형태를 구체적으로 설명 필요"
            },
            {
                "mistake": "테라스 조경을 'cảnh quan mái'으로 표현",
                "correction": "'cảnh quan sân thượng' 또는 'thiết kế cây xanh ngoài trời'",
                "explanation": "조경 공간의 기능을 명확히 표현"
            }
        ],
        "examples": [
            {
                "ko": "최상층 테라스에는 바비큐 시설과 야외 라운지가 구비되어 있습니다.",
                "vi": "Sân thượng tầng cao nhất được trang bị khu BBQ và khu nghỉ ngoài trời.",
                "situation": "formal"
            },
            {
                "ko": "테라스 바닥 방수 처리 후 목재 데크를 시공하겠습니다.",
                "vi": "Sau khi chống thấm sàn sân thượng, sẽ thi công sàn gỗ ngoài trời.",
                "situation": "onsite"
            },
            {
                "ko": "테라스에서 맥주 한잔하면서 야경 보는 게 최고예요.",
                "vi": "Ngồi uống bia ở sân thượng ngắm cảnh đêm là tuyệt nhất.",
                "situation": "informal"
            }
        ],
        "relatedTerms": ["발코니", "옥상", "루프탑", "데크", "파고라"]
    },
    {
        "slug": "khong-gian-tru",
        "korean": "필로티",
        "vietnamese": "Không gian trụ",
        "hanja": None,
        "hanjaReading": None,
        "pronunciation": "필로티",
        "meaningKo": "건물 1층을 기둥만으로 구성하여 개방된 공간으로 만드는 건축 기법. 프랑스어 'pilotis'에서 유래한 용어로 베트nam어로는 'không gian trụ'(기둥 공간), 'tầng trệt hở'(개방된 1층), 또는 'pilotis' 그대로 사용. 통역 시 주의점은 필로티의 용도를 명확히 설명하는 것 - 한국에서는 주차 공간, 커뮤니티 공간, 또는 침수 방지용으로 활용. 베트남에서는 열대 기후 특성상 통풍과 그늘 확보 목적이 강조됨. '필로티 주차장'은 'bãi đỗ xe tầng trệt hở', '필로티 구조'는 'kết cấu pilotis'로 번역하며, 구조 안전성 확보를 위해 기둥 간격과 내진 설계를 반드시 언급.",
        "meaningVi": "Kỹ thuật kiến trúc để tầng một của tòa nhà chỉ có cột, tạo thành không gian mở. Trong tiếng Hàn gọi là '필로티' (pilotis - từ tiếng Pháp). Ở Hàn Quốc thường dùng làm bãi đỗ xe hoặc không gian cộng đồng, đồng thời có tác dụng chống ngập lụt. Ở Việt Nam, kiểu thiết kế này phổ biến để tạo thông gió và bóng mát trong khí hậu nhiệt đới. Yêu cầu kỹ thuật cao về kết cấu cột và móng để đảm bảo an toàn.",
        "context": "건축 설계, 아파트 단지, 도시 계획",
        "culturalNote": "한국에서는 1990년대 이후 아파트 단지에서 필로티 구조가 확산되었으나, 일부 지역에서 범죄 우려와 구조 안전 문제로 논란. 베트남에서는 프랑스 식민지 시대 건축 유산으로 도심 구시가에서 흔히 볼 수 있으며, 오토바이 주차와 노점상 공간으로 활용. 한국의 '필로티 화재 위험'은 베트남 현장에서도 공유되는 우려사항이므로 방화 대책(biện pháp phòng cháy) 언급 필수. 필로티 높이는 한국 기준 2.3m 이상, 베트남은 2.5m 이상 권장.",
        "commonMistakes": [
            {
                "mistake": "필로티를 '1층 주차장(bãi đỗ xe tầng 1)'으로만 번역",
                "correction": "'không gian trụ' 또는 'tầng trệt hở' 사용",
                "explanation": "필로티는 주차장뿐 아니라 다목적 개방 공간을 의미하므로 용도 한정 금지"
            },
            {
                "mistake": "'필로티 기둥'을 'cột tầng 1'으로만 표현",
                "correction": "'cột pilotis' 또는 'cột đỡ tầng trệt hở'",
                "explanation": "구조적 기능을 명확히 표현하여 일반 기둥과 구분"
            },
            {
                "mistake": "필로티 공간을 'tầng trống'으로 번역",
                "correction": "'không gian mở tầng trệt' 또는 'tầng trệt thông thoáng'",
                "explanation": "'trống'(빈)은 부정적 뉘앙스, '개방성'을 강조하는 표현 필요"
            },
            {
                "mistake": "필로티 침수 방지 기능을 설명 없이 생략",
                "correction": "'pilotis giúp tránh ngập úng' (필로티는 침수 방지에 도움)",
                "explanation": "베트남 우기를 고려할 때 중요한 기능이므로 반드시 언급"
            }
        ],
        "examples": [
            {
                "ko": "이 아파트는 필로티 구조로 1층을 개방하여 주차 공간과 커뮤니티 시설을 배치했습니다.",
                "vi": "Chung cư này áp dụng kết cấu pilotis, để tầng trệt mở bố trí bãi đỗ xe và tiện ích cộng đồng.",
                "situation": "formal"
            },
            {
                "ko": "필로티 기둥 간격이 6미터인데, 구조 검토 결과 보강이 필요합니다.",
                "vi": "Khoảng cách giữa các cột pilotis là 6 mét, kết quả kiểm tra kết cấu cho thấy cần gia cố.",
                "situation": "onsite"
            },
            {
                "ko": "비 올 때 필로티 밑에 차 대면 안 젖어서 좋아요.",
                "vi": "Trời mưa đỗ xe dưới pilotis thì không bị ướt, rất tiện.",
                "situation": "informal"
            }
        ],
        "relatedTerms": ["기둥", "주차장", "커뮤니티시설", "내진설계", "개방공간"]
    },
    {
        "slug": "san-giua",
        "korean": "아트리움",
        "vietnamese": "Sân giữa",
        "hanja": None,
        "hanjaReading": None,
        "pronunciation": "아트리움",
        "meaningKo": "건물 내부에 위치한 개방된 중앙 공간으로, 여러 층을 관통하며 자연 채광을 받는 구조. 라틴어 'atrium'에서 유래한 용어로 베트남어로는 'sân giữa'(중간 마당), 'khoảng trống trung tâm'(중앙 공터), 또는 'atrium' 그대로 사용. 통역 시 주의점은 아트리움의 기능을 명확히 전달하는 것 - 자연 채광(ánh sáng tự nhiên), 환기(thông gió), 시각적 개방감(cảm giác mở)을 제공. 한국에서는 호텔 로비, 쇼핑몰, 오피스 빌딩에서 흔히 볼 수 있으며, 베트남에서도 고급 상업 시설에서 활용. '유리 천장 아트리움'은 'atrium mái kính', '아트리움 정원'은 'vườn trong atrium'으로 번역.",
        "meaningVi": "Không gian mở ở trung tâm tòa nhà, xuyên suốt nhiều tầng và có ánh sáng tự nhiên từ trên cao chiếu xuống. Trong tiếng Hàn gọi là '아트리움' (atrium - từ Latin). Phổ biến ở sảnh khách sạn, trung tâm thương mại, tòa nhà văn phòng cao cấp. Chức năng chính: tạo ánh sáng tự nhiên, thông gió, và cảm giác không gian rộng rãi. Thường có mái kính và có thể bố trí cây xanh, ghế ngồi.",
        "context": "상업 건축, 호텔 설계, 오피스 빌딩",
        "culturalNote": "한국에서는 대형 쇼핑몰과 호텔에서 아트리움을 고급스러움의 상징으로 활용하며, 이벤트 공간으로도 사용. 베트남에서는 프랑스 식민지 시대 건축물에서 중정(courtyard) 형태로 유사한 개념 존재. 한국의 '복층 아트리움'은 베트남어로 'atrium xuyên suốt nhiều tầng'로 설명하며, 에어컨 효율 저하 우려를 언급하면 베트남 엔지니어와 소통 원활. 아트리움 소음 문제도 양국 공통 관심사.",
        "commonMistakes": [
            {
                "mistake": "아트리움을 '중정(sân trong)'과 혼동하여 번역",
                "correction": "아트리움은 'atrium' 또는 'sân giữa có mái kính', 중정은 'sân trong'",
                "explanation": "아트리움은 실내 공간이며 유리 지붕이 특징, 중정은 완전 야외 공간"
            },
            {
                "mistake": "'아트리움 천장'을 'trần atrium'으로만 표현",
                "correction": "'mái kính atrium' 또는 'hệ thống mái kính trung tâm'",
                "explanation": "유리 지붕이 핵심 특징이므로 재질 명시 필요"
            },
            {
                "mistake": "아트리움을 '홀(hall)'로 번역",
                "correction": "'atrium' 또는 'không gian trung tâm xuyên tầng'",
                "explanation": "홀은 단층 공간, 아트리움은 다층을 관통하는 공간"
            },
            {
                "mistake": "아트리움 조명을 '실내 조명(đèn trong nhà)'로만 표현",
                "correction": "'ánh sáng tự nhiên từ atrium' (아트리움의 자연 채광)",
                "explanation": "자연 채광이 아트리움의 핵심 기능이므로 강조 필요"
            }
        ],
        "examples": [
            {
                "ko": "이 호텔은 20층 높이의 아트리움을 중심으로 객실이 배치되어 개방감이 뛰어납니다.",
                "vi": "Khách sạn này bố trí phòng xung quanh atrium cao 20 tầng, tạo cảm giác mở rất tốt.",
                "situation": "formal"
            },
            {
                "ko": "아트리움 유리 청소는 고소작업이므로 안전 장비가 필수입니다.",
                "vi": "Vệ sinh kính atrium là công việc trên cao nên thiết bị an toàn là bắt buộc.",
                "situation": "onsite"
            },
            {
                "ko": "아트리움에서 콘서트 하면 소리가 울려서 분위기 좋아요.",
                "vi": "Tổ chức hòa nhạc ở atrium thì âm thanh vang lên rất hay.",
                "situation": "informal"
            }
        ],
        "relatedTerms": ["로비", "중정", "천창", "보이드", "복층"]
    },
    {
        "slug": "sanh-chinh",
        "korean": "로비",
        "vietnamese": "Sảnh chính",
        "hanja": None,
        "hanjaReading": None,
        "pronunciation": "로비",
        "meaningKo": "건물 출입구 인근의 넓은 대기 공간. 영어 'lobby'의 음차어로 베트남어로는 'sảnh chính'(중앙 홀), 'khu vực đón tiếp'(접객 구역)으로 표현. 통역 시 주의점은 용도에 따라 용어가 달라진다는 것 - 호텔 로비는 'sảnh khách sạn', 오피스 로비는 'sảnh tòa nhà', 아파트 로비는 'sảnh chung cư'. 한국에서는 로비를 건물의 '얼굴'로 인식하여 인테리어에 많은 투자를 하며, 베트남에서도 유사. '로비 라운지'는 'khu vực nghỉ ở sảnh', '리셉션 데스크'는 'quầy lễ tân'으로 번역하며, 로비 층고(chiều cao sảnh)와 마감재(vật liệu hoàn thiện)는 고급스러움의 지표로 인식됨.",
        "meaningVi": "Không gian rộng gần lối vào tòa nhà, dùng để đón tiếp và chờ đợi. Trong tiếng Hàn gọi là '로비' (lobby), thường thấy ở khách sạn, tòa nhà văn phòng, chung cư cao cấp. Ở Hàn Quốc, lobby được coi là 'khuôn mặt' của tòa nhà nên đầu tư nội thất và hoàn thiện rất cao cấp. Thường có quầy lễ tân, khu vực ngồi đợi, và hệ thống điều hòa tập trung.",
        "context": "상업 건축, 호텔, 오피스, 주거 시설",
        "culturalNote": "한국에서는 아파트 로비가 주민 자긍심의 척도가 되며, 대리석 마감과 샹들리에가 흔함. 베트남에서도 고급 아파트에서 유사한 경향 있으나, 열대 기후 특성상 개방형 로비와 자연 환기를 선호하는 경우도 많음. 한국의 '무인 로비 시스템'(출입 보안)은 베트남어로 'hệ thống bảo vệ tự động ở sảnh'로 설명. 로비 가구 배치는 양국 모두 풍수(phong thủy) 고려.",
        "commonMistakes": [
            {
                "mistake": "로비를 '입구(lối vào)'로만 번역",
                "correction": "'sảnh chính' 또는 'khu vực đón tiếp' 사용",
                "explanation": "로비는 단순 입구가 아닌 대기/접객 기능이 있는 넓은 공간"
            },
            {
                "mistake": "'로비 층고'를 'chiều cao lối vào'로 번역",
                "correction": "'chiều cao sảnh' 또는 'độ cao trần sảnh chính'",
                "explanation": "로비의 공간적 특성인 층고를 명확히 표현"
            },
            {
                "mistake": "'로비 라운지'를 'phòng chờ'로만 번역",
                "correction": "'khu vực nghỉ ngơi ở sảnh' 또는 'không gian lounge'",
                "explanation": "'phòng chờ'는 별도의 방, 라운지는 로비 내 개방된 휴식 공간"
            },
            {
                "mistake": "모든 로비를 'sảnh'으로만 표현",
                "correction": "호텔 로비 'sảnh khách sạn', 오피스 로비 'sảnh tòa nhà'로 구분",
                "explanation": "건물 유형에 따라 로비 용어 세분화 필요"
            }
        ],
        "examples": [
            {
                "ko": "이 아파트 로비는 6미터 층고와 대리석 마감으로 고급스러움을 연출했습니다.",
                "vi": "Sảnh chung cư này có chiều cao 6 mét và hoàn thiện bằng đá marble, tạo cảm giác sang trọng.",
                "situation": "formal"
            },
            {
                "ko": "로비 바닥 타일 시공 시 평탄도를 정밀하게 맞춰야 합니다.",
                "vi": "Khi thi công gạch sàn sảnh cần đảm bảo độ phẳng chính xác.",
                "situation": "onsite"
            },
            {
                "ko": "로비에서 친구 기다릴게요, 소파 있어서 편해요.",
                "vi": "Tôi đợi bạn ở sảnh, có sofa nên thoải mái.",
                "situation": "informal"
            }
        ],
        "relatedTerms": ["현관", "리셉션", "아트리움", "엘리베이터홀", "출입구"]
    },
    {
        "slug": "loi-thang-may",
        "korean": "코어",
        "vietnamese": "Lõi thang máy",
        "hanja": None,
        "hanjaReading": None,
        "pronunciation": "코어",
        "meaningKo": "건물에서 엘리베이터, 계단, 설비 샤프트 등이 집중된 수직 동선 공간. 영어 'core'의 음차어로 베트남어로는 'lõi'(코어), 'lõi thang máy'(엘리베이터 코어), 'khối dịch vụ trung tâm'(중앙 서비스 블록)으로 표현. 통역 시 주의점은 코어의 위치에 따른 분류 - '중앙 코어'는 'lõi trung tâm', '측면 코어'는 'lõi bên hông', '양측 코어'는 'lõi hai bên'. 한국 오피스 빌딩에서는 임대 효율을 위해 중앙 코어를 선호하며, 베트남에서도 유사. '코어 면적'은 'diện tích lõi', '코어 벽'은 'tường lõi cứng'(내진벽)로 번역하며, 내진 설계(thiết kế chống động đất)와 연계 설명 필요.",
        "meaningVi": "Không gian tập trung các động선 thẳng đứng trong tòa nhà như thang máy, cầu thang, hệ thống kỹ thuật. Trong tiếng Hàn gọi là '코어' (core). Ở các tòa nhà văn phòng Hàn Quốc thường đặt core ở trung tâm để tối ưu diện tích cho thuê. Core thường có tường bê tông cốt thép dày, đóng vai trò quan trọng trong kết cấu chống động đất. Bao gồm: thang máy, cầu thang thoát hiểm, các shaft kỹ thuật (điện, nước, điều hòa).",
        "context": "건축 설계, 오피스 빌딩, 초고층 건물",
        "culturalNote": "한국 오피스 빌딩에서는 '코어 효율'이 임대료와 직결되어 설계 핵심 요소. 베트남에서도 A급 오피스에서 유사한 개념 적용되나, 지진 대비 기준 차이로 코어 벽 두께가 다를 수 있음. 한국의 '무주(無柱) 오피스'는 코어만으로 하중을 지탱하는 구조로 베트남어로 'văn phòng không cột'로 설명. 코어 공간은 피난 동선이므로 소방 규정(quy định PCCC) 준수 필수.",
        "commonMistakes": [
            {
                "mistake": "코어를 '엘리베이터(thang máy)'로만 번역",
                "correction": "'lõi thang máy' 또는 'khối dịch vụ trung tâm'",
                "explanation": "코어는 엘리베이터뿐 아니라 계단, 설비 샤프트를 포함하는 종합 개념"
            },
            {
                "mistake": "'코어 벽'을 'tường bê tông'으로만 표현",
                "correction": "'tường lõi cứng' 또는 'tường chịu lực trung tâm'",
                "explanation": "코어 벽은 구조적 역할(내진)을 하므로 기능 명시 필요"
            },
            {
                "mistake": "'코어 면적'을 '공용 면적(diện tích chung)'에 포함하지 않고 설명",
                "correction": "'diện tích lõi (thuộc diện tích chung)' (공용 면적에 속하는 코어 면적)",
                "explanation": "임대 면적 계산 시 코어 면적은 공용 부분으로 분류됨을 명확히"
            },
            {
                "mistake": "코어 계획을 '엘리베이터 배치(bố trí thang máy)'로만 설명",
                "correction": "'quy hoạch khối dịch vụ trung tâm' (중앙 서비스 블록 계획)",
                "explanation": "코어는 엘리베이터뿐 아니라 설비, 계단 등 종합 계획"
            }
        ],
        "examples": [
            {
                "ko": "이 빌딩은 중앙 코어 방식으로 설계되어 사무 공간의 조망권이 우수합니다.",
                "vi": "Tòa nhà này thiết kế theo kiểu lõi trung tâm nên không gian văn phòng có tầm nhìn tốt.",
                "situation": "formal"
            },
            {
                "ko": "코어 벽 철근 배근 작업 시 설계 도면대로 정확히 시공하세요.",
                "vi": "Khi bố trí cốt thép tường lõi, thi công chính xác theo bản vẽ thiết kế.",
                "situation": "onsite"
            },
            {
                "ko": "엘리베이터 고장 나면 코어 계단으로 내려가야 해요.",
                "vi": "Thang máy hỏng thì phải đi cầu thang ở lõi xuống.",
                "situation": "informal"
            }
        ],
        "relatedTerms": ["엘리베이터", "계단실", "샤프트", "피난동선", "내진벽"]
    },
    {
        "slug": "cau-thang",
        "korean": "계단실",
        "vietnamese": "Cầu thang",
        "hanja": "階段室",
        "hanjaReading": "階(층계 계) + 段(층계 단) + 室(집 실)",
        "pronunciation": "계단실",
        "meaningKo": "건물 내 계단이 설치된 독립적인 수직 공간. 베트남어로는 'cầu thang'(계단), 'khu vực cầu thang'(계단 구역), 'lồng cầu thang'(계단 샤프트)로 표현. 통역 시 주의점은 계단실의 유형 구분 - '비상 계단실'은 'cầu thang thoát hiểm', '일반 계단실'은 'cầu thang thường', '외부 계단실'은 'cầu thang ngoài'로 번역. 한국 건축법상 계단실은 방화 구획과 피난 시설로 중요하며, 베트남에서도 소방 규정(quy định PCCC) 준수 필수. '계단실 가압'은 'tăng áp buồng cầu thang'(연기 유입 방지), '계단 폭'은 'chiều rộng bậc thang'으로 번역하며, 양국 모두 최소 1.2m 기준.",
        "meaningVi": "Không gian độc lập chứa cầu thang trong tòa nhà. Trong tiếng Hàn gọi là '계단실', đóng vai trò quan trọng trong hệ thống thoát hiểm và phòng cháy chữa cháy. Theo quy định xây dựng Hàn Quốc, cầu thang phải là khu vực chống cháy độc lập. Có các loại: cầu thang thoát hiểm (비상 계단실), cầu thang thường (일반 계단실), cầu thang ngoài (외부 계단실). Chiều rộng tối thiểu thường 1.2m, có hệ thống tăng áp để ngăn khói.",
        "context": "건축 설계, 소방 안전, 피난 계획",
        "culturalNote": "한국에서는 아파트 계단실을 '옆집과의 경계'로 인식하며, 방음과 방화 성능 중시. 베트남에서는 계단실을 보조 동선으로만 보는 경향 있어, 한국 기준의 계단실 가압 시스템(hệ thống tăng áp) 설명 필요. 한국의 '피난 계단'은 외부로 직접 연결되어야 하며, 베트남 통역 시 'cầu thang thoát hiểm ra ngoài trực tiếp'로 강조. 계단 논슬립(non-slip) 처리는 양국 공통 안전 기준.",
        "commonMistakes": [
            {
                "mistake": "계단실을 '계단(cầu thang)'으로만 번역",
                "correction": "'khu vực cầu thang' 또는 'lồng cầu thang'",
                "explanation": "계단실은 계단이 있는 독립된 공간을 의미하므로 'khu vực' 포함 필요"
            },
            {
                "mistake": "'비상 계단실'을 'cầu thang khẩn cấp'으로 직역",
                "correction": "'cầu thang thoát hiểm' (피난 계단)",
                "explanation": "'thoát hiểm'이 베트남 소방 규정의 공식 용어"
            },
            {
                "mistake": "'계단실 가압'을 'áp lực cầu thang'으로 번역",
                "correction": "'hệ thống tăng áp buồng cầu thang' (계단실 가압 시스템)",
                "explanation": "연기 유입 방지를 위한 시스템이므로 'hệ thống' 포함하여 설명"
            },
            {
                "mistake": "계단 논슬립을 'chống trượt'로만 표현",
                "correction": "'vật liệu chống trượt bậc thang' 또는 'lớp phủ an toàn'",
                "explanation": "안전 자재임을 명확히 표현"
            }
        ],
        "examples": [
            {
                "ko": "이 건물은 양쪽 끝에 비상 계단실을 배치하여 피난 동선을 확보했습니다.",
                "vi": "Tòa nhà này bố trí cầu thang thoát hiểm ở hai đầu để đảm bảo động선 thoát nạn.",
                "situation": "formal"
            },
            {
                "ko": "계단실 가압 팬 설치 위치를 옥상으로 변경하겠습니다.",
                "vi": "Sẽ thay đổi vị trí lắp quạt tăng áp buồng cầu thang lên sân thượng.",
                "situation": "onsite"
            },
            {
                "ko": "엘리베이터 고장이면 계단실로 걸어 내려가야 해요.",
                "vi": "Thang máy hỏng thì phải đi bộ xuống cầu thang.",
                "situation": "informal"
            }
        ],
        "relatedTerms": ["비상계단", "피난동선", "방화문", "코어", "난간"]
    }
]

def main():
    # 기존 construction.json 경로
    json_path = os.path.join(
        os.path.dirname(__file__),
        "..",
        "data",
        "terms",
        "construction.json"
    )

    # 기존 데이터 읽기
    with open(json_path, "r", encoding="utf-8") as f:
        data = json.load(f)

    # 새 용어 추가
    data.extend(new_terms)

    # 저장
    with open(json_path, "w", encoding="utf-8") as f:
        json.dump(data, f, ensure_ascii=False, indent=2)

    print(f"✅ {len(new_terms)}개 용어 추가 완료")
    print(f"📁 파일: {json_path}")
    print(f"📊 총 용어 수: {len(data)}개")

if __name__ == "__main__":
    main()
