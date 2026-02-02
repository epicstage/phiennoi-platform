#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
건설(Construction) 용어 추가 스크립트 v4-ee
테마: 위생설비 (Sanitary Equipment)
대상: src/data/terms/construction.json
"""

import json
import os

# 추가할 용어 데이터 (Tier S 기준)
data = [
    {
        "slug": "lavabo",
        "korean": "세면기",
        "vietnamese": "Lavabo",
        "hanja": "洗面器",
        "hanjaReading": "洗(씻을 세) + 面(낯 면) + 器(그릇 기)",
        "pronunciation": "라바보",
        "meaningKo": "욕실이나 화장실에서 손과 얼굴을 씻는 데 사용하는 위생도기. 통역 시 '세면대', '세면기', '세수대' 등 다양한 표현이 혼용되나, 베트남 현장에서는 'lavabo'로 통일하는 것이 명확하다. 설치 높이(일반 800~850mm, 장애인용 750mm)와 배수 트랩 방식(P-트랩/S-트랩)을 구분하여 전달해야 한다. 벽걸이형(treo tường)과 받침대형(có chân đế)의 시공 방식 차이를 주의한다.",
        "meaningVi": "Thiết bị vệ sinh dùng để rửa tay và mặt trong phòng tắm hoặc nhà vệ sinh. Bao gồm các loại treo tường (wall-hung), có chân đế (pedestal), và âm bàn (under-counter). Chiều cao lắp đặt tiêu chuẩn là 800-850mm, riêng lavabo cho người khuyết tật là 750mm. Cần lưu ý phương thức thoát nước (P-trap hoặc S-trap) khi thi công.",
        "context": "위생설비 시공, 욕실 마감, 설비 자재 발주",
        "culturalNote": "한국에서는 '세면대'라는 용어가 일상적이나 베트남 현장에서는 프랑스어 기원의 'lavabo'가 공식 용어로 통용된다. 베트남은 습식 화장실 구조가 많아 배수 트랩 선택이 중요하며, 한국처럼 건식 구조를 전제로 한 시공 방식을 그대로 적용하면 물이 고이는 문제가 발생할 수 있다. 또한 베트남은 수압이 낮은 지역이 많아 세면기 수전(vòi lavabo)의 토출 압력 조정이 필수적이다.",
        "commonMistakes": [
            {
                "mistake": "세면대를 'bồn rửa mặt'로 번역",
                "correction": "lavabo",
                "explanation": "'bồn rửa mặt'는 직역이지만 현장에서 통용되지 않음. 'lavabo'가 표준 용어"
            },
            {
                "mistake": "설치 높이를 cm 단위로만 전달 (예: 80cm)",
                "correction": "800mm 또는 80cm (단위 병기)",
                "explanation": "베트남 도면은 mm 단위 사용. cm만 말하면 오해 발생"
            },
            {
                "mistake": "P-트랩과 S-트랩을 구분하지 않고 'bẫy thoát nước'로만 표현",
                "correction": "bẫy chữ P (P-trap), bẫy chữ S (S-trap)",
                "explanation": "트랩 형태에 따라 시공법이 다르므로 명확히 구분 필요"
            }
        ],
        "examples": [
            {
                "ko": "세면기는 벽걸이형으로 하고 P-트랩으로 배수 처리하세요.",
                "vi": "Lavabo lắp dạng treo tường và xử lý thoát nước bằng bẫy chữ P.",
                "situation": "onsite"
            },
            {
                "ko": "장애인용 세면기는 설치 높이를 750mm로 조정해야 합니다.",
                "vi": "Lavabo dành cho người khuyết tật cần điều chỉnh chiều cao lắp đặt xuống 750mm.",
                "situation": "formal"
            },
            {
                "ko": "이 세면기는 받침대가 있는 타입이라 배관이 보이지 않아요.",
                "vi": "Lavabo này có chân đế nên không nhìn thấy đường ống.",
                "situation": "informal"
            }
        ],
        "relatedTerms": ["급수전", "배수트랩", "위생도기", "욕실마감"]
    },
    {
        "slug": "bon-cau",
        "korean": "양변기",
        "vietnamese": "Bồn cầu",
        "hanja": "洋便器",
        "hanjaReading": "洋(서양 양) + 便(편할 편) + 器(그릇 기)",
        "pronunciation": "본꺼우",
        "meaningKo": "앉아서 용변을 보는 서양식 변기. 통역 시 '양변기', '좌변기', '변기' 등으로 불리나 베트남어 'bồn cầu'로 통일한다. 급수 방식에 따라 로탱크형(có bồn chứa nước)과 플러시밸브형(xả trực tiếp)으로 구분되며, 배수 방식도 벽배수(thoát nước qua tường)와 바닥배수(thoát nước qua sàn)로 나뉜다. 베트남 현장에서는 수압이 낮은 경우가 많아 로탱크형을 선호하므로, 플러시밸브형 지정 시 수압 확인이 필수다. 또한 비데 기능 일체형(kết hợp chức năng vòi xịt) 여부도 명확히 전달해야 한다.",
        "meaningVi": "Thiết bị vệ sinh dùng để đi vệ sinh theo kiểu ngồi. Phân loại theo phương thức cấp nước: có bồn chứa nước (cistern type) hoặc xả trực tiếp bằng van xả (flush valve). Phân loại theo phương thức thoát nước: thoát qua tường (wall-hung) hoặc thoát qua sàn (floor-mounted). Tại Việt Nam, do áp lực nước thường thấp, loại có bồn chứa được ưa chuộng hơn. Cần lưu ý khoảng cách từ tâm ống thoát nước đến tường (thường 300-400mm).",
        "context": "위생설비 시공, 화장실 마감, 설비 자재 선정",
        "culturalNote": "한국에서는 비데 일체형 양변기가 보편화되었으나, 베트남에서는 별도의 핸드 샤워(vòi xịt cầm tay)를 선호하는 경향이 강하다. 또한 베트남은 화장지를 변기에 버리지 않고 휴지통에 버리는 문화가 여전히 남아 있어, 배수관 막힘 문제를 예방하기 위해 하수 시스템 용량을 충분히 확보해야 한다. 한국식 '스마트 변기(bồn cầu thông minh)'를 도입할 때는 전기 콘센트 위치와 전압(220V) 호환성을 반드시 확인한다.",
        "commonMistakes": [
            {
                "mistake": "양변기를 'toilet'으로만 표현",
                "correction": "bồn cầu",
                "explanation": "'toilet'은 화장실 전체를 지칭. 변기 자체는 'bồn cầu'"
            },
            {
                "mistake": "로탱크형과 플러시밸브형을 구분하지 않고 'bồn cầu xả nước'로만 표현",
                "correction": "bồn cầu có bồn chứa nước / bồn cầu xả trực tiếp",
                "explanation": "급수 방식에 따라 시공법과 수압 요구사항이 다름"
            },
            {
                "mistake": "배수 거리를 구체적으로 전달하지 않음",
                "correction": "khoảng cách từ tâm ống thoát đến tường là 300mm",
                "explanation": "배수구 위치가 정확하지 않으면 변기 설치 불가"
            }
        ],
        "examples": [
            {
                "ko": "이 양변기는 벽배수 방식이고 배수 중심에서 벽까지 거리가 300mm입니다.",
                "vi": "Bồn cầu này là loại thoát nước qua tường, khoảng cách từ tâm ống thoát đến tường là 300mm.",
                "situation": "onsite"
            },
            {
                "ko": "로탱크형 양변기로 교체하되 비데 기능 일체형으로 선정하세요.",
                "vi": "Thay bằng bồn cầu có bồn chứa nước, chọn loại kết hợp chức năng vòi xịt.",
                "situation": "formal"
            },
            {
                "ko": "이 변기는 물이 약하게 내려가니까 로탱크 물 조절 좀 해주세요.",
                "vi": "Bồn cầu này xả nước yếu, vui lòng điều chỉnh mực nước trong bồn chứa.",
                "situation": "informal"
            }
        ],
        "relatedTerms": ["로탱크", "플러시밸브", "배수트랩", "위생도기"]
    },
    {
        "slug": "bon-tieu-nam",
        "korean": "소변기",
        "vietnamese": "Bồn tiểu nam",
        "hanja": "小便器",
        "hanjaReading": "小(작을 소) + 便(편할 편) + 器(그릇 기)",
        "pronunciation": "본띠에우남",
        "meaningKo": "남성이 서서 소변을 보는 위생도기. 통역 시 '소변기', '남자 소변기' 등으로 불리며 베트남어로는 'bồn tiểu nam'이다. 설치 방식에 따라 벽걸이형(treo tường)과 바닥형(đứng sàn)으로 구분되고, 급수 방식도 자동(cảm ứng tự động), 수동(bấm tay), 무수식(không dùng nước)으로 나뉜다. 베트남 현장에서는 물 절약을 위해 센서식 자동 급수(van cảm ứng)를 선호하나, 센서 고장 시 수동 플러시 버튼을 백업으로 설치하는 경우가 많다. 설치 높이는 일반 600mm, 어린이용 400mm가 표준이다.",
        "meaningVi": "Thiết bị vệ sinh dành cho nam giới đi tiểu đứng. Phân loại theo cách lắp đặt: treo tường (wall-hung) hoặc đứng sàn (floor-mounted). Phân loại theo phương thức cấp nước: tự động cảm ứng (sensor), bấm tay (manual flush), hoặc không dùng nước (waterless). Chiều cao lắp đặt tiêu chuẩn: 600mm cho người lớn, 400mm cho trẻ em. Để tiết kiệm nước, loại cảm ứng được ưa chuộng nhưng nên có nút bấm dự phòng khi cảm biến hỏng.",
        "context": "공공화장실 시공, 위생설비 설치, 남자 화장실 마감",
        "culturalNote": "한국에서는 무수식 소변기가 환경 친화적 선택으로 주목받지만, 베트남에서는 냄새 관리 문제로 인해 아직 대중화되지 않았다. 또한 베트남 공공화장실은 청소 빈도가 낮은 경우가 많아, 자동 급수 센서 방식이 위생 관리에 유리하다. 한국처럼 '세정력'보다는 '물 절약'과 '냄새 차단'이 더 중요한 선택 기준이므로, 통역 시 이를 강조하면 의사소통이 원활하다.",
        "commonMistakes": [
            {
                "mistake": "소변기를 'toilet nam'으로 번역",
                "correction": "bồn tiểu nam",
                "explanation": "'toilet'은 화장실 공간. 소변기 자체는 'bồn tiểu nam'"
            },
            {
                "mistake": "자동 급수를 'tự động xả nước'로만 표현",
                "correction": "van cảm ứng tự động (센서식 자동 급수)",
                "explanation": "'xả nước'는 물 내림 자체. 센서 방식임을 명확히 해야 함"
            },
            {
                "mistake": "설치 높이를 전달하지 않고 '벽에 걸어'라고만 지시",
                "correction": "treo tường ở độ cao 600mm",
                "explanation": "높이 지정이 없으면 시공자가 임의로 설치"
            }
        ],
        "examples": [
            {
                "ko": "소변기는 센서식 자동 급수로 하되, 수동 플러시 버튼도 함께 설치하세요.",
                "vi": "Bồn tiểu nam lắp van cảm ứng tự động, nhưng cũng cần lắp thêm nút bấm tay dự phòng.",
                "situation": "onsite"
            },
            {
                "ko": "어린이용 소변기는 설치 높이를 400mm로 낮춰야 합니다.",
                "vi": "Bồn tiểu cho trẻ em cần hạ độ cao lắp đặt xuống 400mm.",
                "situation": "formal"
            },
            {
                "ko": "이 소변기 센서가 안 되니까 수동 버튼으로 물 내려주세요.",
                "vi": "Cảm biến bồn tiểu này không hoạt động, vui lòng bấm nút tay để xả nước.",
                "situation": "informal"
            }
        ],
        "relatedTerms": ["자동급수밸브", "센서", "위생도기", "배수트랩"]
    },
    {
        "slug": "bon-tam",
        "korean": "욕조",
        "vietnamese": "Bồn tắm",
        "hanja": "浴槽",
        "hanjaReading": "浴(목욕할 욕) + 槽(구유 조)",
        "pronunciation": "본땀",
        "meaningKo": "물을 담아 몸을 담그고 목욕하는 위생 설비. 통역 시 '욕조', '욕탕', '배스텁(bathtub)' 등으로 불리며 베트남어로는 'bồn tắm'이다. 재질에 따라 아크릴(acrylic), 주철(gang đúc), FRP, 인조대리석(đá nhân tạo) 등으로 구분되고, 설치 방식도 빌트인형(âm sàn), 독립형(đặt riêng), 코너형(góc tường)으로 나뉜다. 베트남은 열대 기후로 인해 욕조 수요가 한국보다 낮으며, 주로 고급 주택이나 리조트에서 사용된다. 통역 시 배수 용량(dung tích thoát nước), 급탕 용량(khả năng cấp nước nóng), 방수 처리(chống thấm) 사항을 명확히 전달해야 한다.",
        "meaningVi": "Thiết bị vệ sinh dùng để chứa nước và ngâm mình t목욕. Phân loại theo vật liệu: acrylic, gang đúc (cast iron), FRP, đá nhân tạo. Phân loại theo cách lắp đặt: âm sàn (built-in), đặt riêng (freestanding), góc tường (corner type). Tại Việt Nam, do khí hậu nhiệt đới, nhu cầu bồn tắm thấp hơn và chủ yếu dùng trong nhà cao cấp hoặc resort. Cần chú ý dung tích nước (150-250 lít), khả năng cấp nước nóng, và xử lý chống thấm.",
        "context": "고급 욕실 시공, 리조트 설비, 위생설비 마감",
        "culturalNote": "한국에서는 욕조가 주거용 욕실의 표준 옵션이지만, 베트남에서는 샤워 부스(cabin tắm)가 더 보편적이다. 베트남 사람들은 더운 날씨로 인해 샤워를 선호하며, 욕조는 '사치품' 또는 '휴식 공간'으로 인식된다. 따라서 욕조 시공 시 급탕 용량을 충분히 확보하지 않으면 물이 차는 데 시간이 오래 걸려 불편하다. 또한 베트남은 습도가 높아 욕조 주변 방수 처리(chống thấm)와 환기(thông gió)가 매우 중요하다.",
        "commonMistakes": [
            {
                "mistake": "욕조를 'bathtub'으로만 표현",
                "correction": "bồn tắm",
                "explanation": "베트남 현장에서는 'bồn tắm'이 표준 용어"
            },
            {
                "mistake": "급탕 용량을 고려하지 않고 욕조 크기만 전달",
                "correction": "bồn tắm 200 lít, cần bình nóng lạnh 300 lít",
                "explanation": "급탕기 용량이 부족하면 물이 차는 시간이 너무 오래 걸림"
            },
            {
                "mistake": "방수 처리를 'chống nước'로만 표현",
                "correction": "chống thấm toàn bộ khu vực bồn tắm",
                "explanation": "'chống nước'는 물 튀김 방지. 방수는 'chống thấm'"
            }
        ],
        "examples": [
            {
                "ko": "이 욕조는 아크릴 재질이고 용량은 200리터입니다. 급탕기는 300리터로 선정하세요.",
                "vi": "Bồn tắm này bằng acrylic, dung tích 200 lít. Chọn bình nóng lạnh 300 lít.",
                "situation": "onsite"
            },
            {
                "ko": "욕조 설치 전에 바닥과 벽면 방수 처리를 완료해야 합니다.",
                "vi": "Trước khi lắp bồn tắm, cần hoàn thành xử lý chống thấm sàn và tường.",
                "situation": "formal"
            },
            {
                "ko": "이 욕조 물 빠지는 게 너무 느려요. 배수구 확인해주세요.",
                "vi": "Bồn tắm này thoát nước rất chậm. Vui lòng kiểm tra cống thoát nước.",
                "situation": "informal"
            }
        ],
        "relatedTerms": ["급탕기", "배수트랩", "방수처리", "위생도기"]
    },
    {
        "slug": "cabin-tam",
        "korean": "샤워부스",
        "vietnamese": "Cabin tắm",
        "hanja": None,
        "hanjaReading": None,
        "pronunciation": "까빈땀",
        "meaningKo": "샤워 공간을 유리나 패널로 구획한 독립형 샤워 시설. 통역 시 '샤워부스', '샤워박스', '샤워룸' 등으로 불리며 베트남어로는 'cabin tắm'이다. 재질에 따라 강화유리(kính cường lực), 아크릴 패널(tấm acrylic), 알루미늄 프레임(khung nhôm) 등으로 구분되고, 개폐 방식도 미닫이형(trượt), 여닫이형(mở quay), 접이형(gấp)으로 나뉜다. 베트남은 욕조보다 샤워를 선호하므로 샤워부스가 표준 욕실 옵션이다. 통역 시 배수 기울기(độ dốc thoát nước), 방수 높이(chiều cao chống thấm), 문 개폐 방향(hướng mở cửa)을 명확히 전달해야 한다.",
        "meaningVi": "Khu vực tắm đứng được ngăn bằng kính hoặc tấm panel. Phân loại theo vật liệu: kính cường lực (tempered glass), tấm acrylic, khung nhôm. Phân loại theo cách mở cửa: trượt (sliding), mở quay (swing), gấp (folding). Tại Việt Nam, cabin tắm là lựa chọn phổ biến hơn bồn tắm do khí hậu nóng ẩm. Cần lưu ý độ dốc sàn thoát nước (tối thiểu 1-2%), chiều cao chống thấm tường (tối thiểu 1800mm), và hướng mở cửa phù hợp với không gian.",
        "context": "욕실 마감, 위생설비 시공, 주거용 건축",
        "culturalNote": "한국에서는 욕실이 전체적으로 습식 구조인 경우가 많아 샤워부스가 선택 사항이지만, 베트남 중산층 이상 주택에서는 샤워부스가 필수로 간주된다. 베트남은 하루 2회 이상 샤워하는 문화가 보편적이므로, 배수 속도가 느리거나 물이 새는 문제가 발생하면 큰 불만으로 이어진다. 또한 베트남 욕실은 한국보다 좁은 경우가 많아, 문 개폐 방향과 동선을 고려한 설계가 중요하다.",
        "commonMistakes": [
            {
                "mistake": "샤워부스를 'phòng tắm'으로 번역",
                "correction": "cabin tắm",
                "explanation": "'phòng tắm'은 욕실 전체. 샤워부스는 'cabin tắm'"
            },
            {
                "mistake": "배수 기울기를 구체적으로 전달하지 않음",
                "correction": "độ dốc sàn tối thiểu 1-2%",
                "explanation": "기울기가 없으면 물이 고여 배수 불량 발생"
            },
            {
                "mistake": "문 개폐 방향을 '안쪽으로'라고만 지시",
                "correction": "cửa mở vào trong / cửa mở ra ngoài",
                "explanation": "공간 구조에 따라 문 방향이 달라야 함"
            }
        ],
        "examples": [
            {
                "ko": "샤워부스는 강화유리 8mm 두께로 하고, 문은 미닫이형으로 선정하세요.",
                "vi": "Cabin tắm dùng kính cường lực dày 8mm, cửa kiểu trượt.",
                "situation": "onsite"
            },
            {
                "ko": "샤워부스 바닥은 배수 기울기를 최소 1.5%로 확보해야 합니다.",
                "vi": "Sàn cabin tắm cần đảm bảo độ dốc thoát nước tối thiểu 1.5%.",
                "situation": "formal"
            },
            {
                "ko": "이 샤워부스 문이 안으로 열리니까 좁아서 불편해요.",
                "vi": "Cửa cabin tắm này mở vào trong nên chật, không tiện.",
                "situation": "informal"
            }
        ],
        "relatedTerms": ["강화유리", "배수트랩", "방수처리", "샤워헤드"]
    },
    {
        "slug": "binh-nong-lanh",
        "korean": "급탕기",
        "vietnamese": "Bình nóng lạnh",
        "hanja": "給湯器",
        "hanjaReading": "給(줄 급) + 湯(끓일 탕) + 器(그릇 기)",
        "pronunciation": "빈농라잉",
        "meaningKo": "물을 데워 온수를 공급하는 설비 장치. 통역 시 '급탕기', '온수기', '보일러' 등으로 불리나 베트남어로는 'bình nóng lạnh'가 표준이다. 가열 방식에 따라 전기식(điện), 가스식(gas), 태양열식(năng lượng mặt trời)으로 구분되고, 저장 방식도 저장형(có bồn chứa)과 순간가열형(trực tiếp, không bồn chứa)으로 나뉜다. 베트남은 전기 요금이 높고 가스 인프라가 제한적이므로, 소형 전기 저장형(15-30리터)이 가장 보편적이다. 통역 시 용량(dung tích), 전력 소비량(công suất tiêu thụ điện), 안전장치(thiết bị an toàn) 사항을 명확히 전달해야 한다.",
        "meaningVi": "Thiết bị gia nhiệt nước để cấp nước nóng. Phân loại theo nguồn năng lượng: điện (electric), gas, năng lượng mặt trời (solar). Phân loại theo cách lưu trữ: có bồn chứa (storage type), trực tiếp không bồn chứa (instant type). Tại Việt Nam, loại điện có bồn chứa 15-30 lít phổ biến nhất do giá điện cao và hạ tầng gas hạn chế. Cần lưu ý dung tích (phù hợp với số người dùng), công suất tiêu thụ điện (thường 1500-3000W), và các thiết bị an toàn (chống giật, chống cháy nổ).",
        "context": "위생설비 시공, 급탕 시스템 설계, 전기 설비 연동",
        "culturalNote": "한국에서는 중앙 보일러 시스템이 보편적이지만, 베트남에서는 각 욕실마다 독립적인 급탕기를 설치하는 방식이 일반적이다. 베트남은 전기 요금 누진제가 심하고 가스 배관이 갖춰지지 않은 지역이 많아, 용량이 작은 전기 저장형을 선호한다. 한국식 '보일러'를 그대로 도입하면 설치 비용과 유지비가 과도하게 증가할 수 있다. 또한 베트남은 정전이 잦은 지역이 있어, 급탕기 전용 차단기(cầu dao riêng) 설치가 필수다.",
        "commonMistakes": [
            {
                "mistake": "급탕기를 'boiler'로만 번역",
                "correction": "bình nóng lạnh",
                "explanation": "'boiler'는 중앙난방. 급탕기는 'bình nóng lạnh'"
            },
            {
                "mistake": "용량을 '큰 거'로만 요청",
                "correction": "dung tích 30 lít (cho 2-3 người)",
                "explanation": "용량을 숫자로 명확히 전달해야 적합한 제품 선정 가능"
            },
            {
                "mistake": "전력 용량을 확인하지 않고 설치 지시",
                "correction": "kiểm tra công suất tiêu thụ (2500W) và cầu dao phù hợp",
                "explanation": "전력 용량 초과 시 차단기가 내려가거나 화재 위험"
            }
        ],
        "examples": [
            {
                "ko": "이 욕실은 2인 사용 기준이니 30리터 전기 저장형 급탕기를 설치하세요.",
                "vi": "Phòng tắm này dùng cho 2 người, lắp bình nóng lạnh điện có bồn chứa 30 lít.",
                "situation": "onsite"
            },
            {
                "ko": "급탕기 전력 소비량이 2500W이므로 전용 차단기를 별도로 설치해야 합니다.",
                "vi": "Bình nóng lạnh tiêu thụ 2500W, cần lắp cầu dao riêng.",
                "situation": "formal"
            },
            {
                "ko": "이 온수기 물이 금방 식으니까 용량 더 큰 걸로 바꿔주세요.",
                "vi": "Bình nóng lạnh này nước nhanh nguội, vui lòng thay loại dung tích lớn hơn.",
                "situation": "informal"
            }
        ],
        "relatedTerms": ["전기설비", "차단기", "온수배관", "위생설비"]
    },
    {
        "slug": "bay-thoat-nuoc",
        "korean": "배수트랩",
        "vietnamese": "Bẫy thoát nước",
        "hanja": "排水Trap",
        "hanjaReading": "排(물리칠 배) + 水(물 수) + Trap(영어: 덫)",
        "pronunciation": "바이토아뜨느억",
        "meaningKo": "배수관에 물을 일정량 가두어 하수 악취와 해충이 역류하는 것을 막는 장치. 통역 시 '배수트랩', '트랩', 'S트랩', 'P트랩' 등으로 불리며 베트남어로는 'bẫy thoát nước'다. 형태에 따라 P형(chữ P), S형(chữ S), U형(chữ U), 병형(ống thẳng có van)으로 구분된다. 베트남은 습도가 높고 하수 시스템이 낙후된 지역이 많아, 트랩이 제대로 작동하지 않으면 악취와 모기 발생 문제가 심각하다. 통역 시 트랩 깊이(độ sâu bẫy), 청소 방법(cách vệ sinh), 물 증발 방지(chống bay hơi nước phong tỏa) 사항을 명확히 전달해야 한다.",
        "meaningVi": "Thiết bị giữ một lượng nước nhất định trong ống thoát nước để ngăn mùi hôi và côn trùng từ cống ngược lên. Phân loại theo hình dạng: chữ P (P-trap), chữ S (S-trap), chữ U (U-trap), ống thẳng có van (bottle trap). Tại Việt Nam, do độ ẩm cao và hệ thống thoát nước kém, bẫy thoát nước rất quan trọng để ngăn mùi và muỗi. Cần lưu ý độ sâu phong tỏa (thường 50-100mm), cách vệ sinh định kỳ, và chống bay hơi nước phong tỏa trong mùa khô.",
        "context": "위생설비 시공, 배관 설치, 악취 방지",
        "culturalNote": "한국에서는 배수트랩이 기본적으로 설치되지만, 베트남 저가 주택에서는 트랩 없이 직배수하는 경우가 많아 악취 문제가 빈번하다. 특히 건기(mùa khô)에는 트랩 내부의 물이 증발하여 악취 차단 기능이 상실되므로, 정기적으로 물을 부어주거나(đổ nước định kỳ) 증발 방지용 오일을 추가하는 관리가 필요하다. 한국식 '트랩'이라는 용어를 그대로 사용하면 베트남 시공자가 이해하지 못하므로 'bẫy thoát nước'로 명확히 표현해야 한다.",
        "commonMistakes": [
            {
                "mistake": "배수트랩을 'ống thoát nước'로만 표현",
                "correction": "bẫy thoát nước (trap)",
                "explanation": "'ống thoát nước'는 배수관 전체. 트랩은 'bẫy'"
            },
            {
                "mistake": "P트랩과 S트랩을 구분하지 않음",
                "correction": "bẫy chữ P / bẫy chữ S",
                "explanation": "설치 위치(벽배수/바닥배수)에 따라 트랩 형태가 달라짐"
            },
            {
                "mistake": "트랩 청소를 '파이프 청소'로만 표현",
                "correction": "vệ sinh bẫy thoát nước (tháo nắp đậy, rửa sạch)",
                "explanation": "트랩은 분해 청소가 가능한 구조"
            }
        ],
        "examples": [
            {
                "ko": "세면기 배수는 P트랩으로 처리하고, 바닥 배수는 S트랩을 사용하세요.",
                "vi": "Thoát nước lavabo dùng bẫy chữ P, thoát nước sàn dùng bẫy chữ S.",
                "situation": "onsite"
            },
            {
                "ko": "배수트랩 깊이는 최소 50mm 이상 확보하여 악취 차단 기능을 유지해야 합니다.",
                "vi": "Độ sâu bẫy thoát nước cần tối thiểu 50mm để duy trì chức năng ngăn mùi.",
                "situation": "formal"
            },
            {
                "ko": "화장실 냄새가 심하니까 배수트랩에 물 좀 부어주세요.",
                "vi": "Nhà vệ sinh mùi hôi, vui lòng đổ nước vào bẫy thoát nước.",
                "situation": "informal"
            }
        ],
        "relatedTerms": ["배수관", "악취방지", "위생설비", "통기관"]
    },
    {
        "slug": "ong-thong-gio",
        "korean": "통기관",
        "vietnamese": "Ống thông gió",
        "hanja": "通氣管",
        "hanjaReading": "通(통할 통) + 氣(기운 기) + 管(대롱 관)",
        "pronunciation": "옹통조",
        "meaningKo": "배수 시스템 내부의 압력을 조절하고 공기를 순환시켜 배수가 원활히 흐르도록 돕는 배관. 통역 시 '통기관', '벤트관', '에어벤트' 등으로 불리며 베트남어로는 'ống thông gió'다. 통기관이 없으면 배수 시 사이펀 현상(hiện tượng hút chân không)이 발생하여 트랩 내부의 물이 빨려 나가고, 악취가 역류하거나 배수 속도가 느려진다. 베트남 저가 주택에서는 통기관을 생략하는 경우가 많아, 고급 건축에서는 통기관 설계가 필수임을 강조해야 한다. 통역 시 통기관 위치(vị trí ống), 지름(đường kính), 옥상 배출 높이(chiều cao thoát khí)를 명확히 전달해야 한다.",
        "meaningVi": "Ống dẫn khí trong hệ thống thoát nước, giúp điều hòa áp suất và tuần hoàn không khí để nước thoát trơn tru. Nếu thiếu ống thông gió, hiện tượng hút chân không (siphon effect) sẽ xảy ra, làm nước phong tỏa trong bẫy bị hút ra, dẫn đến mùi hôi ngược lên và thoát nước chậm. Tại Việt Nam, nhà giá rẻ thường bỏ qua ống thông gió, nhưng trong xây dựng cao cấp thì đây là yếu tố thiết yếu. Cần lưu ý vị trí ống, đường kính (thường 50-75mm), và chiều cao thoát khí trên mái (tối thiểu 300mm trên mặt sàn mái).",
        "context": "배수 시스템 설계, 위생설비 시공, 건축 설비",
        "culturalNote": "한국에서는 고층 건물이나 대형 건축물에서 통기관이 필수적으로 설치되지만, 베트남 중소형 건축에서는 비용 절감을 위해 통기관을 생략하는 경우가 많다. 이로 인해 배수 불량, 악취, 소음 문제가 발생하므로, 고급 프로젝트에서는 통기관 설계를 반드시 포함해야 한다. 특히 베트남은 우기(mùa mưa)에 집중 호우가 잦아, 통기관이 없으면 배수 시스템이 막히거나 역류하는 사고가 발생할 수 있다.",
        "commonMistakes": [
            {
                "mistake": "통기관을 'ống thông khí'로 번역",
                "correction": "ống thông gió",
                "explanation": "'thông khí'는 환기. 배수 통기는 'thông gió'"
            },
            {
                "mistake": "통기관 위치를 '위쪽'으로만 지시",
                "correction": "ống thông gió nối từ đỉnh ống đứng, thoát khí trên mái",
                "explanation": "배수 수직관 최상단에서 연결하여 옥상으로 배출해야 함"
            },
            {
                "mistake": "통기관 지름을 지정하지 않음",
                "correction": "đường kính ống thông gió 50mm",
                "explanation": "지름이 작으면 통기 효과가 떨어짐"
            }
        ],
        "examples": [
            {
                "ko": "배수 수직관 최상단에서 통기관을 연결하고, 옥상으로 배출하세요.",
                "vi": "Nối ống thông gió từ đỉnh ống đứng thoát nước, thoát khí ra mái.",
                "situation": "onsite"
            },
            {
                "ko": "통기관 지름은 배수관과 같거나 그보다 크게 설계해야 합니다.",
                "vi": "Đường kính ống thông gió phải bằng hoặc lớn hơn ống thoát nước.",
                "situation": "formal"
            },
            {
                "ko": "화장실 물 내려갈 때 소리가 이상하니까 통기관 막힌 거 같아요.",
                "vi": "Khi xả nước nhà vệ sinh có tiếng lạ, có vẻ ống thông gió bị tắc.",
                "situation": "informal"
            }
        ],
        "relatedTerms": ["배수관", "배수트랩", "사이펀현상", "위생설비"]
    },
    {
        "slug": "ong-o-bau",
        "korean": "오배수관",
        "vietnamese": "Ống ô bậu",
        "hanja": "汚排水管",
        "hanjaReading": "汚(더러울 오) + 排(물리칠 배) + 水(물 수) + 管(대롱 관)",
        "pronunciation": "옹오바우",
        "meaningKo": "화장실, 세면기, 욕조 등에서 나오는 오수와 생활 잡배수를 함께 배출하는 배관. 통역 시 '오배수관', '하수관', '배수관' 등으로 불리며 베트남어로는 'ống ô bậu'다. 배수 방식에 따라 합류식(hệ thống thoát nước chung)과 분류식(hệ thống thoát nước riêng)으로 구분되며, 베트남은 합류식이 일반적이다. 오배수관은 경사(độ dốc), 지름(đường kính), 청소구(hố thông) 위치가 설계 핵심이다. 통역 시 최소 경사(1/50~1/100), 청소구 간격(15m 이내), 배관 재질(PVC/주철)을 명확히 전달해야 한다.",
        "meaningVi": "Ống dẫn nước thải từ nhà vệ sinh, lavabo, bồn tắm và nước sinh hoạt khác. Phân loại theo hệ thống: thoát nước chung (combined) hoặc thoát nước riêng (separate). Tại Việt Nam, hệ thống chung phổ biến hơn. Yếu tố thiết kế quan trọng: độ dốc (tối thiểu 1/50 đến 1/100), đường kính ống (tối thiểu 100mm cho toilet), vị trí hố thông (cách nhau tối đa 15m). Vật liệu thường dùng: PVC hoặc gang.",
        "context": "배관 설계, 위생설비 시공, 하수 시스템",
        "culturalNote": "한국에서는 오수와 잡배수를 분리하는 분류식 하수도가 확대되고 있지만, 베트남은 대부분 합류식이다. 베트남 하수 시스템은 한국보다 노후화되어 있고, 우기에 역류 사고가 잦으므로, 오배수관 경사와 청소구 설치가 매우 중요하다. 또한 베트남은 화장지를 변기에 버리지 않는 문화가 남아 있어 배관 막힘이 상대적으로 적지만, 음식물 찌꺼기나 기름이 배수구로 흘러가는 경우가 많아 그리스 트랩(bẫy mỡ) 설치가 권장된다.",
        "commonMistakes": [
            {
                "mistake": "오배수관을 'ống nước thải'로만 표현",
                "correction": "ống ô bậu (오배수관 전용 용어)",
                "explanation": "'nước thải'는 폐수 일반. 오배수는 'ô bậu'"
            },
            {
                "mistake": "경사를 '약간 기울여'라고만 지시",
                "correction": "độ dốc tối thiểu 1/50 (2%)",
                "explanation": "경사가 부족하면 배수 불량, 과도하면 고형물 침전"
            },
            {
                "mistake": "청소구 위치를 지정하지 않음",
                "correction": "lắp hố thông mỗi 15m và tại điểm uốn cong",
                "explanation": "청소구 없으면 막힘 발생 시 배관 해체 필요"
            }
        ],
        "examples": [
            {
                "ko": "오배수관은 최소 경사 1/50로 설계하고, 15미터마다 청소구를 설치하세요.",
                "vi": "Ống ô bậu thiết kế độ dốc tối thiểu 1/50, lắp hố thông mỗi 15m.",
                "situation": "onsite"
            },
            {
                "ko": "화장실 배수관은 지름 100mm 이상으로 해야 막힘이 없습니다.",
                "vi": "Ống thoát nước nhà vệ sinh cần đường kính tối thiểu 100mm để tránh tắc.",
                "situation": "formal"
            },
            {
                "ko": "이 배수관 자꾸 막히니까 청소구 열어서 확인해주세요.",
                "vi": "Ống thoát nước này hay bị tắc, vui lòng mở hố thông kiểm tra.",
                "situation": "informal"
            }
        ],
        "relatedTerms": ["배수트랩", "청소구", "통기관", "하수관"]
    },
    {
        "slug": "van-cap-nuoc",
        "korean": "급수밸브",
        "vietnamese": "Van cấp nước",
        "hanja": "給水Valve",
        "hanjaReading": "給(줄 급) + 水(물 수) + Valve(영어: 밸브)",
        "pronunciation": "반깝느억",
        "meaningKo": "급수관에서 물의 흐름을 제어하는 밸브. 통역 시 '급수밸브', '수전', '물 잠그는 밸브' 등으로 불리며 베트남어로는 'van cấp nước'다. 용도에 따라 각밸브(van góc), 글로브밸브(van cầu), 게이트밸브(van cửa), 체크밸브(van một chiều)로 구분된다. 베트남 위생설비에서는 각밸브(van góc)가 세면기, 양변기, 싱크대 등에 가장 많이 사용되며, 누수 방지와 유지보수를 위해 각 기구마다 독립적으로 설치하는 것이 원칙이다. 통역 시 밸브 위치(vị trí van), 크기(kích thước, 보통 1/2인치), 재질(đồng/nhựa)을 명확히 전달해야 한다.",
        "meaningVi": "Van điều khiển dòng chảy trong đường ống cấp nước. Phân loại theo công dụng: van góc (angle valve), van cầu (globe valve), van cửa (gate valve), van một chiều (check valve). Tại Việt Nam, van góc phổ biến nhất, dùng cho lavabo, bồn cầu, chậu rửa. Nguyên tắc: mỗi thiết bị cần có van riêng để dễ bảo trì và ngăn rò rỉ. Cần lưu ý vị trí van (thường đặt trước thiết bị, ở tường hoặc sàn), kích thước (thường 1/2 inch = DN15), và vật liệu (đồng hoặc nhựa PVC).",
        "context": "급수 배관, 위생설비 시공, 유지보수",
        "culturalNote": "한국에서는 급수밸브가 벽면에 매립되거나 미관을 고려해 숨겨지는 경우가 많지만, 베트남에서는 노출 배관이 일반적이라 밸브가 눈에 잘 띈다. 베트남은 수압 변동이 심하고 수질 문제로 인한 밸브 고장이 잦으므로, 유지보수가 쉬운 위치에 밸브를 설치하는 것이 중요하다. 또한 베트남 시공자들은 비용 절감을 위해 값싼 플라스틱 밸브를 사용하려는 경향이 있으나, 내구성을 위해 황동(đồng thau) 밸브 사용을 권장해야 한다.",
        "commonMistakes": [
            {
                "mistake": "급수밸브를 'vòi nước'로 표현",
                "correction": "van cấp nước",
                "explanation": "'vòi nước'는 수전(faucet). 밸브는 'van'"
            },
            {
                "mistake": "밸브 위치를 '적당한 곳'으로만 지시",
                "correction": "van cấp nước đặt trước thiết bị, chiều cao 150mm từ sàn",
                "explanation": "위치가 애매하면 유지보수 시 접근이 어려움"
            },
            {
                "mistake": "밸브 크기를 전달하지 않음",
                "correction": "van cấp nước 1/2 inch (DN15)",
                "explanation": "크기가 맞지 않으면 연결 불가"
            }
        ],
        "examples": [
            {
                "ko": "세면기 급수관 연결 전에 각밸브를 먼저 설치하세요.",
                "vi": "Trước khi nối ống cấp nước cho lavabo, lắp van góc trước.",
                "situation": "onsite"
            },
            {
                "ko": "각 위생기구마다 독립적인 급수밸브를 설치하여 유지보수를 용이하게 해야 합니다.",
                "vi": "Mỗi thiết bị vệ sinh cần có van cấp nước riêng để dễ bảo trì.",
                "situation": "formal"
            },
            {
                "ko": "이 세면기 물이 안 나오니까 밸브 잠긴 거 아닌지 확인해주세요.",
                "vi": "Lavabo này không có nước, vui lòng kiểm tra van có bị khóa không.",
                "situation": "informal"
            }
        ],
        "relatedTerms": ["급수관", "각밸브", "수전", "위생설비"]
    }
]

# 파일 경로
file_path = os.path.join(
    os.path.dirname(os.path.dirname(__file__)),
    "data",
    "terms",
    "construction.json"
)

def main():
    # 기존 파일 읽기
    try:
        with open(file_path, "r", encoding="utf-8") as f:
            existing_data = json.load(f)
        print(f"✅ 기존 파일 로드 완료: {len(existing_data)}개 용어")
    except FileNotFoundError:
        print("❌ 파일을 찾을 수 없습니다. 경로를 확인하세요.")
        return
    except json.JSONDecodeError:
        print("❌ JSON 파싱 오류. 파일 형식을 확인하세요.")
        return

    # 중복 확인
    existing_slugs = {term["slug"] for term in existing_data}
    new_terms = [term for term in data if term["slug"] not in existing_slugs]
    duplicates = [term["slug"] for term in data if term["slug"] in existing_slugs]

    if duplicates:
        print(f"⚠️  중복 slug 발견 (추가 안 함): {', '.join(duplicates)}")

    if not new_terms:
        print("ℹ️  추가할 새 용어가 없습니다.")
        return

    # 기존 데이터에 새 용어 추가
    existing_data.extend(new_terms)

    # 파일 저장
    with open(file_path, "w", encoding="utf-8") as f:
        json.dump(existing_data, f, ensure_ascii=False, indent=2)

    print(f"✅ {len(new_terms)}개 용어 추가 완료! (총 {len(existing_data)}개)")
    print(f"추가된 용어: {', '.join([t['slug'] for t in new_terms])}")

if __name__ == "__main__":
    main()
