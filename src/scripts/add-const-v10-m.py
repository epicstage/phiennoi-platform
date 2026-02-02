#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
건설장비부품 (Construction Equipment Parts) - 10 terms
Tier S quality standard
"""

import json
import os

# Get absolute path to construction.json
file_path = os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', 'data', 'terms', 'construction.json')

# Load existing data
with open(file_path, 'r', encoding='utf-8') as f:
    data = json.load(f)  # data is a LIST

# Get existing slugs to prevent duplicates
existing_slugs = {t['slug'] for t in data}

# New terms (10 construction equipment parts)
new_terms = [
    {
        "slug": "gau-xuc",
        "korean": "버킷",
        "vietnamese": "gàu xúc",
        "hanja": "bucket",
        "hanjaReading": None,
        "pronunciation": "까우 쑥",
        "meaningKo": "굴삭기나 로더 등 건설 중장비의 전면에 부착되어 흙이나 자갈을 퍼내는 삽 모양의 부품입니다. 통역 시 '버킷'과 '굴삭기삽'을 혼용하지 않도록 주의하세요. 베트남 현장에서는 'gàu xúc'이 표준이지만 작업자들이 'xẻng máy'라고 부르기도 하므로 문맥에 따라 정확히 구분해야 합니다. 특히 용량(dung tích)을 명시할 때는 m³ 단위를 함께 통역하고, 마모 상태 점검 시 '이빨(răng gàu)', '날(lưỡi gàu)' 등 세부 부품명을 정확히 전달해야 합니다.",
        "meaningVi": "Gàu xúc là bộ phận hình xẻng gắn phía trước máy xúc hoặc máy xúc lật, dùng để đào bới và xúc đất, đá, cát. Đây là phụ tùng quan trọng nhất của thiết bị đào bới, có nhiều loại dung tích khác nhau tùy theo công suất máy. Khi làm việc tại công trường Hàn Quốc, cần phân biệt rõ 'bucket tiêu chuẩn' và 'bucket răng cưa' để tránh nhầm lẫn trong quá trình thay thế hoặc bảo dưỡng.",
        "context": "건설장비 부품, 굴삭기 작업, 중장비 수리, 장비 점검 시",
        "culturalNote": "한국 건설현장에서는 '버킷'이라는 영어식 표현이 보편화되어 있지만, 베트남에서는 'gàu xúc'이라는 베트남어 용어가 더 자연스럽습니다. 한국에서는 버킷 용량을 '평(坪)' 단위로 환산해 말하는 경우가 있는데, 베트남에서는 항상 m³(mét khối)로 표기합니다. 또한 한국 현장에서는 버킷 교체를 '붐 작업'이라고 통칭하지만, 베트남에서는 'thay gàu'로 명확히 구분합니다.",
        "commonMistakes": [
            {
                "mistake": "xẻng máy로 통역",
                "correction": "gàu xúc",
                "explanation": "xẻng máy는 구어체이며 공식 문서나 안전교육에서는 gàu xúc을 사용해야 합니다"
            },
            {
                "mistake": "버킷을 'thùng đựng'으로 번역",
                "correction": "gàu xúc",
                "explanation": "thùng đựng은 일반 용기를 의미하며 건설장비 전문용어로는 부적합합니다"
            },
            {
                "mistake": "용량 단위를 리터(lít)로 통역",
                "correction": "mét khối (m³)",
                "explanation": "건설장비 버킷 용량은 국제적으로 m³ 단위를 사용합니다"
            }
        ],
        "examples": [
            {
                "ko": "이 굴삭기 버킷 용량이 0.8세제곱미터입니다.",
                "vi": "Dung tích gàu xúc của máy này là 0.8 mét khối.",
                "situation": "formal"
            },
            {
                "ko": "버킷 이빨이 마모되어 교체가 필요합니다.",
                "vi": "Răng gàu bị mòn cần phải thay thế.",
                "situation": "onsite"
            },
            {
                "ko": "암석 작업용 강화 버킷으로 바꿔주세요.",
                "vi": "Hãy thay sang gàu xúc cứng chuyên dụng cho đá.",
                "situation": "onsite"
            }
        ],
        "relatedTerms": ["굴삭기", "붐", "암", "유압실린더"]
    },
    {
        "slug": "xich-may",
        "korean": "캐터필러",
        "vietnamese": "xích máy",
        "hanja": "無限軌道",
        "hanjaReading": "무(없을 무) + 한(한 한) + 궤(길 궤) + 도(길 도)",
        "pronunciation": "씩 마이",
        "meaningKo": "무한궤도라고도 하며, 굴삭기·불도저 등 건설 중장비가 이동할 때 사용하는 띠 모양의 궤도입니다. 통역 시 '캐터필러'는 브랜드명에서 유래한 용어이므로 공식적으로는 '무한궤도' 또는 베트남어 'xích máy'로 전달해야 합니다. 한국 현장에서는 관습적으로 '캐터필러' 또는 '캐터'라고 줄여 부르지만, 베트남 근로자들은 'xích máy' 또는 'xích xe'로 이해합니다. 특히 마모 점검 시 '슈(giày xích)', '링크(mắt xích)', '핀(chốt xích)' 등 세부 구성요소를 정확히 구분해서 통역해야 안전사고를 예방할 수 있습니다.",
        "meaningVi": "Xích máy (hay còn gọi là xích đại, xích bánh xích) là hệ thống di chuyển dạng đai xích của các thiết bị công trình như máy xúc, máy ủi. Khác với bánh lốp, xích máy giúp thiết bị di chuyển ổn định trên địa hình khó như bùn lầy, dốc cao. Hệ thống xích bao gồm các bộ phận: giày xích, mắt xích, chốt xích, con lăn. Khi làm việc tại Hàn Quốc, cần lưu ý người Hàn thường gọi là 'caterpillar' theo thương hiệu, nhưng thuật ngữ chuẩn là '무한궤도' hoặc 'xích máy' trong tiếng Việt.",
        "context": "중장비 정비, 캐터필러 교체, 궤도식 장비 점검 시",
        "culturalNote": "한국에서는 '캐터필러'가 보편화되어 있어 대부분의 작업자가 이 용어를 사용하지만, 이는 미국 Caterpillar사의 브랜드명에서 유래한 것입니다. 베트남에서는 'xích máy'가 표준 용어이며, 일부 지역에서는 'xích đại'라고도 부릅니다. 한국 현장에서는 캐터필러 장력 조정을 '체인 조임'이라고 표현하는데, 베트남에서는 'căng xích'으로 명확히 구분됩니다. 또한 한국은 캐터필러 수명을 '운행시간'으로 관리하지만, 베트남은 '킬로미터'로 측정하는 경우가 많아 통역 시 단위 환산이 필요합니다.",
        "commonMistakes": [
            {
                "mistake": "caterpillar를 베트남어로 음차하여 'ca-tơ-pi-la'로 통역",
                "correction": "xích máy",
                "explanation": "브랜드명이 아닌 일반 무한궤도를 지칭할 때는 xích máy를 사용해야 합니다"
            },
            {
                "mistake": "xích xe(차량 체인)로 혼동",
                "correction": "xích máy(건설장비 무한궤도)",
                "explanation": "xích xe는 자전거나 오토바이 체인을 의미하므로 구분 필요합니다"
            },
            {
                "mistake": "캐터필러 장력을 'lực căng dây xích'로 통역",
                "correction": "lực căng xích máy",
                "explanation": "dây xích(체인)이 아닌 xích máy(무한궤도)로 정확히 표현해야 합니다"
            }
        ],
        "examples": [
            {
                "ko": "캐터필러 장력을 점검하고 조정하세요.",
                "vi": "Hãy kiểm tra và điều chỉnh lực căng xích máy.",
                "situation": "formal"
            },
            {
                "ko": "캐터 한쪽이 빠졌으니 작업 중지하고 수리하세요.",
                "vi": "Xích máy một bên bị tuột, dừng thi công và sửa chữa ngay.",
                "situation": "onsite"
            },
            {
                "ko": "이 장비는 습지 작업용 광폭 캐터필러가 장착되어 있습니다.",
                "vi": "Thiết bị này được lắp xích máy rộng chuyên dụng cho công trình đầm lầy.",
                "situation": "formal"
            }
        ],
        "relatedTerms": ["굴삭기", "불도저", "슈", "링크"]
    },
    {
        "slug": "can-cau",
        "korean": "크레인붐",
        "vietnamese": "cần cẩu",
        "hanja": "crane boom",
        "hanjaReading": None,
        "pronunciation": "껀 꺼우",
        "meaningKo": "크레인의 팔에 해당하는 긴 구조물로, 중량물을 들어올리는 역할을 합니다. 통역 시 '붐(boom)'과 '지브(jib)'를 명확히 구분해야 하며, 베트nam에서는 'cần cẩu'가 기본 용어이나 'cần trục'으로도 불립니다. 한국 현장에서는 단순히 '붐'이라고 하면 메인붐을 의미하지만, 베트남에서는 'cần chính'과 'cần phụ'로 구분합니다. 특히 안전교육 시 붐의 작업반경(bán kính làm việc), 최대하중(tải trọng tối đa), 각도(góc nghiêng) 등을 정확히 통역해야 사고를 예방할 수 있습니다.",
        "meaningVi": "Cần cẩu là bộ phận dạng cánh tay dài của cần trục (crane), có chức năng nâng và di chuyển vật nặng. Cần cẩu có thể là loại cố định hoặc loại tele (rút ra/thu vào). Hệ thống cần cẩu bao gồm: cần chính (main boom), cần phụ (jib), cáp cẩu, móc cẩu. Khi làm việc tại công trường Hàn Quốc, cần phân biệt rõ các thuật ngữ về chiều dài cần, góc nghiêng, bán kính làm việc để đảm bảo an toàn lao động.",
        "context": "크레인 작업, 양중 작업, 타워크레인 운영 시",
        "culturalNote": "한국에서는 '붐'이라는 영어 발음을 그대로 사용하지만, 베트남에서는 'cần cẩu' 또는 'cần trục'이 표준입니다. 한국 현장에서는 붐 길이를 '단(段)' 단위로 표현하는 경우가 있는데(예: 5단 붐), 베트남에서는 미터 단위로만 표기합니다. 또한 한국은 붐 각도를 작업자가 육안으로 판단하는 경우가 많지만, 베트남 안전기준은 각도계(đồng hồ đo góc) 사용을 의무화하는 추세입니다. 통역 시 이러한 안전기준 차이를 명확히 전달해야 합니다.",
        "commonMistakes": [
            {
                "mistake": "boom을 베트남어로 음차하여 'bum'으로 통역",
                "correction": "cần cẩu",
                "explanation": "공식 용어는 cần cẩu이며 bum은 비표준 표현입니다"
            },
            {
                "mistake": "지브(jib)도 cần cẩu로 통역",
                "correction": "cần phụ 또는 jib",
                "explanation": "메인붐은 cần chính, 지브는 cần phụ로 구분해야 합니다"
            },
            {
                "mistake": "붐 길이를 '단'으로 그대로 통역",
                "correction": "mét (m) 단위로 환산",
                "explanation": "베트남에서는 미터 단위만 사용하므로 환산 필요합니다"
            }
        ],
        "examples": [
            {
                "ko": "타워크레인 붐 길이가 50미터입니다.",
                "vi": "Chiều dài cần cẩu của cần trục tháp là 50 mét.",
                "situation": "formal"
            },
            {
                "ko": "붐 각도를 70도로 조정하세요.",
                "vi": "Hãy điều chỉnh góc cần cẩu về 70 độ.",
                "situation": "onsite"
            },
            {
                "ko": "이 크레인은 텔레스코픽 붐 방식입니다.",
                "vi": "Cần trục này sử dụng cần cẩu kiểu tele (rút ra thu vào).",
                "situation": "formal"
            }
        ],
        "relatedTerms": ["크레인", "지브", "와이어로프", "후크"]
    },
    {
        "slug": "moc-cau",
        "korean": "후크",
        "vietnamese": "móc cẩu",
        "hanja": "hook",
        "hanjaReading": None,
        "pronunciation": "목 꺼우",
        "meaningKo": "크레인이나 호이스트의 케이블 끝에 달려 중량물을 걸어 올리는 갈고리 모양의 부품입니다. 통역 시 단순히 '후크'라고만 하지 말고, 용도에 따라 '싱글후크(móc đơn)', '더블후크(móc đôi)', '회전후크(móc xoay)' 등을 구분해야 합니다. 한국 현장에서는 '샤클(shackle)'과 혼동하는 경우가 많은데, 샤클은 'tao móc'으로 별도 용어입니다. 특히 안전교육 시 후크의 안전하중(tải trọng an toàn), 개구부(miệng móc), 안전장치(chốt an toàn) 등을 정확히 통역해야 추락사고를 예방할 수 있습니다.",
        "meaningVi": "Móc cẩu là phụ kiện hình móc gắn ở đầu cáp cẩu của cần trục hoặc palăng, dùng để móc và nâng vật nặng. Có nhiều loại móc cẩu: móc đơn, móc đôi, móc xoay, móc tự động. Mỗi móc có ghi rõ tải trọng an toàn (SWL - Safe Working Load). Khi làm việc tại Hàn Quốc, cần kiểm tra móc cẩu thường xuyên để phát hiện vết nứt, biến dạng, mòn miệng móc - đây là nguyên nhân phổ biến gây tai nạn rơi vật.",
        "context": "양중 작업, 크레인 작업, 리프팅 작업, 안전점검 시",
        "culturalNote": "한국 건설현장에서는 '후크'라는 영어 발음을 그대로 사용하지만, 베트남에서는 'móc cẩu'가 표준이며 'móc treo'라고도 부릅니다. 한국은 후크 안전하중을 톤(ton) 단위로 표기하지만, 베트남에서는 킬로그램(kg)과 톤을 혼용하므로 통역 시 단위 확인이 필수입니다. 또한 한국 현장에서는 후크 점검을 월 1회 실시하지만, 베트남 안전규정은 주 1회 점검을 권장하는 경우가 많습니다. 통역 시 이러한 안전점검 주기 차이를 명확히 전달해야 합니다.",
        "commonMistakes": [
            {
                "mistake": "hook을 베트남어로 음차하여 'húc'으로 통역",
                "correction": "móc cẩu",
                "explanation": "húc은 베트남어로 '들이받다'는 동사이므로 혼동 주의"
            },
            {
                "mistake": "샤클(shackle)을 móc cẩu로 통역",
                "correction": "tao móc (샤클은 별도 부품)",
                "explanation": "후크와 샤클은 다른 부품이므로 구분 필요합니다"
            },
            {
                "mistake": "안전하중(SWL)을 '최대하중'으로 통역",
                "correction": "tải trọng an toàn (안전하중 ≠ 최대하중)",
                "explanation": "안전하중은 최대하중의 1/3~1/5 수준이므로 명확히 구분해야 합니다"
            }
        ],
        "examples": [
            {
                "ko": "이 후크의 안전하중은 5톤입니다.",
                "vi": "Tải trọng an toàn của móc cẩu này là 5 tấn.",
                "situation": "formal"
            },
            {
                "ko": "후크 안전장치가 작동하는지 확인하세요.",
                "vi": "Hãy kiểm tra chốt an toàn của móc cẩu có hoạt động không.",
                "situation": "onsite"
            },
            {
                "ko": "회전후크를 사용하면 작업이 더 안전합니다.",
                "vi": "Sử dụng móc cẩu xoay sẽ an toàn hơn trong thi công.",
                "situation": "onsite"
            }
        ],
        "relatedTerms": ["크레인", "와이어로프", "샤클", "슬링"]
    },
    {
        "slug": "cap-cau",
        "korean": "와이어로프",
        "vietnamese": "cáp cẩu",
        "hanja": "wire rope",
        "hanjaReading": None,
        "pronunciation": "깝 꺼우",
        "meaningKo": "강철 소선을 여러 가닥 꼬아서 만든 케이블로, 크레인이나 호이스트에서 중량물을 매달아 올리는 데 사용됩니다. 통역 시 '와이어로프', '와이어케이블', '강삭(鋼索)' 등 다양한 표현이 있지만 베트남어로는 'cáp cẩu' 또는 'dây cáp thép'로 통일해서 사용합니다. 한국 현장에서는 직경(đường kính)을 밀리미터로, 파단하중(lực kéo đứt)을 톤으로 표기하는데, 베트남도 동일하므로 단위 변환 부담이 적습니다. 다만 와이어로프의 꼬임 방향(chiều xoắn)이나 구성(cấu tạo)을 설명할 때는 전문 용어가 복잡하므로 도면이나 실물을 함께 보며 통역하는 것이 효과적입니다.",
        "meaningVi": "Cáp cẩu (hay dây cáp thép) là loại cáp được kết cấu từ nhiều sợi thép nhỏ xoắn lại với nhau, dùng để treo và nâng vật nặng trên cần trục, palăng. Cáp cẩu có nhiều loại cấu tạo: 6x19, 6x37, 8x19... tùy theo mục đích sử dụng. Khi làm việc tại công trường Hàn Quốc, cần kiểm tra cáp thường xuyên để phát hiện dấu hiệu đứt sợi, rỉ sét, biến dạng - đây là nguyên nhân chính gây đứt cáp và tai nạn nghiêm trọng.",
        "context": "크레인 작업, 양중 작업, 와이어 점검, 리프팅 작업 시",
        "culturalNote": "한국에서는 '와이어로프'라는 영어 혼용 표현이 보편적이지만, 베트남에서는 'cáp cẩu' 또는 'dây cáp thép'이 표준입니다. 한국 현장에서는 와이어로프 폐기 기준을 '소선 절단 개수'로 판단하는데(예: 한 피치 내 10개 이상 절단 시 폐기), 베트남에서도 유사한 기준을 적용하지만 일부 현장에서는 육안 점검에만 의존하는 경우가 있어 통역 시 안전기준을 명확히 전달해야 합니다. 또한 한국은 와이어로프에 윤활유를 정기적으로 도포하지만, 베트남 일부 현장에서는 이를 소홀히 하는 경우가 있어 주의가 필요합니다.",
        "commonMistakes": [
            {
                "mistake": "wire rope를 베트남어로 음차하여 'oai rốp'으로 통역",
                "correction": "cáp cẩu 또는 dây cáp thép",
                "explanation": "음차 표현은 비표준이며 공식 문서에서는 cáp cẩu를 사용해야 합니다"
            },
            {
                "mistake": "일반 케이블(cáp điện)과 혼동",
                "correction": "cáp cẩu (전기케이블과 구조 다름)",
                "explanation": "cáp điện은 전기 케이블이므로 명확히 구분 필요합니다"
            },
            {
                "mistake": "파단하중(lực kéo đứt)을 '작업하중'으로 통역",
                "correction": "파단하중과 안전하중을 구분",
                "explanation": "파단하중은 끊어질 때의 하중, 안전하중은 사용 가능 하중으로 개념이 다릅니다"
            }
        ],
        "examples": [
            {
                "ko": "이 와이어로프는 직경 16밀리미터, 파단하중 20톤입니다.",
                "vi": "Cáp cẩu này có đường kính 16mm, lực kéo đứt 20 tấn.",
                "situation": "formal"
            },
            {
                "ko": "와이어 한 피치 내에 끊어진 소선이 10개 이상이면 교체하세요.",
                "vi": "Nếu trong một pitch có từ 10 sợi thép bị đứt trở lên thì phải thay cáp.",
                "situation": "formal"
            },
            {
                "ko": "와이어에 윤활유 발라놨으니까 녹 안 슬 거야.",
                "vi": "Đã tra dầu mỡ cho cáp rồi nên không bị gỉ đâu.",
                "situation": "informal"
            }
        ],
        "relatedTerms": ["크레인", "후크", "호이스트", "슬링"]
    },
    {
        "slug": "dong-co-thuy-luc",
        "korean": "유압모터",
        "vietnamese": "động cơ thủy lực",
        "hanja": "油壓motor",
        "hanjaReading": "유(기름 유) + 압(누를 압) + motor",
        "pronunciation": "동 꺼 투이 륵",
        "meaningKo": "유압 에너지를 기계적 회전 에너지로 변환하는 장치로, 굴삭기·크레인 등 건설장비의 작동부에 사용됩니다. 통역 시 '유압모터'와 '전동모터(động cơ điện)'를 명확히 구분해야 하며, 베트남 현장에서는 'động cơ thủy lực' 또는 줄여서 'mô tơ dầu'라고도 부릅니다. 한국 현장에서는 유압모터의 용량을 '배기량(cc)'으로 표현하지만, 베트남에서는 '유량(lưu lượng - lít/phút)'으로 표기하는 경우가 많아 통역 시 단위 확인이 필요합니다. 특히 고장 진단 시 '소음(tiếng ồn)', '진동(rung động)', '누유(rò rỉ dầu)' 등 증상을 정확히 전달해야 정비가 원활합니다.",
        "meaningVi": "Động cơ thủy lực là thiết bị chuyển đổi năng lượng thủy lực thành năng lượng cơ học quay, được sử dụng trong các bộ phận chuyển động của máy xúc, cần trục và thiết bị công trình. Khác với động cơ điện, động cơ thủy lực hoạt động nhờ dầu thủy lực áp suất cao. Có hai loại chính: động cơ piston và động cơ bánh răng. Khi làm việc tại công trường Hàn Quốc, cần phân biệt rõ 'động cơ thủy lực' (hydraulic motor) và 'xi lanh thủy lực' (hydraulic cylinder) vì chúng có chức năng khác nhau.",
        "context": "건설장비 정비, 유압시스템 점검, 장비 고장 진단 시",
        "culturalNote": "한국에서는 '유압모터'가 공식 용어이지만, 작업 현장에서는 '하이드로모터' 또는 줄여서 '하모'라고 부르기도 합니다. 베트남에서는 'động cơ thủy lực'이 표준이며, 일부 작업자는 'mô tơ dầu'라고 부릅니다. 한국 정비 매뉴얼은 유압모터 사양을 회전수(rpm)와 토크(N·m)로 표기하는데, 베트남 매뉴얼은 압력(bar)과 유량(L/min)을 중심으로 기술하는 경우가 많아 통역 시 혼동하지 않도록 주의해야 합니다. 또한 한국은 유압모터 교체 시 브랜드 순정품을 선호하지만, 베트남 일부 현장에서는 호환품을 사용하는 경향이 있어 품질 기준 차이를 명확히 전달해야 합니다.",
        "commonMistakes": [
            {
                "mistake": "전동모터(động cơ điện)와 혼동",
                "correction": "động cơ thủy lực (유압모터)",
                "explanation": "전동모터는 전기로, 유압모터는 유압으로 작동하므로 구조가 완전히 다릅니다"
            },
            {
                "mistake": "xi lanh thủy lực(유압실린더)로 잘못 통역",
                "correction": "động cơ thủy lực (회전운동) vs xi lanh (직선운동)",
                "explanation": "유압모터는 회전운동, 유압실린더는 직선운동을 만듭니다"
            },
            {
                "mistake": "용량을 '마력(hp)'으로 통역",
                "correction": "배기량(cc) 또는 유량(L/min)",
                "explanation": "유압모터는 마력보다 배기량/유량으로 표기하는 것이 일반적입니다"
            }
        ],
        "examples": [
            {
                "ko": "이 굴삭기 선회 유압모터 배기량은 250cc입니다.",
                "vi": "Động cơ thủy lực xoay của máy xúc này có dung tích 250cc.",
                "situation": "formal"
            },
            {
                "ko": "유압모터에서 이상한 소음이 나면 즉시 점검하세요.",
                "vi": "Nếu động cơ thủy lực phát ra tiếng ồn lạ thì phải kiểm tra ngay.",
                "situation": "onsite"
            },
            {
                "ko": "하모가 고장나서 선회가 안 돼요.",
                "vi": "Động cơ thủy lực hỏng nên không xoay được.",
                "situation": "informal"
            }
        ],
        "relatedTerms": ["유압펌프", "유압실린더", "유압밸브", "작동유"]
    },
    {
        "slug": "xi-lanh-thuy-luc",
        "korean": "유압실린더",
        "vietnamese": "xi lanh thủy lực",
        "hanja": "油壓cylinder",
        "hanjaReading": "유(기름 유) + 압(누를 압) + cylinder",
        "pronunciation": "씨 라잉 투이 륵",
        "meaningKo": "유압 에너지를 직선 운동으로 변환하는 장치로, 굴삭기의 붐·암·버킷 작동, 불도저의 블레이드 승강 등에 사용됩니다. 통역 시 '실린더(cylinder)'를 베트남어 'xi lanh'로 발음하는데, 이는 프랑스어 'cylindre'에서 유래한 외래어입니다. 한국 현장에서는 '붐실린더', '암실린더', '버킷실린더'처럼 장착 위치로 구분하는데, 베트남어로는 'xi lanh cần', 'xi lanh tay', 'xi lanh gàu'로 대응됩니다. 특히 유압실린더 점검 시 '로드(대롱/막대)', '패킹(gioăng)', '오일씰(phớt dầu)' 등 세부 부품을 정확히 구분해서 통역해야 누유(rò rỉ) 문제를 정확히 진단할 수 있습니다.",
        "meaningVi": "Xi lanh thủy lực là thiết bị chuyển đổi năng lượng thủy lực thành chuyển động thẳng, được sử dụng để điều khiển các bộ phận như cần cẩu, tay máy xúc, gàu xúc, lưỡi ủi. Xi lanh bao gồm: thân xi lanh, piston, trục piston (cần đẩy), các loại phớt và gioăng. Khi làm việc tại công trường Hàn Quốc, cần chú ý kiểm tra xi lanh thường xuyên để phát hiện rò rỉ dầu, trầy xước trục piston - đây là nguyên nhân phổ biến làm giảm hiệu suất và gây hỏng hóc.",
        "context": "건설장비 정비, 유압시스템 점검, 붐/암 작동 불량 시",
        "culturalNote": "한국에서는 '유압실린더' 또는 줄여서 '실린더'라고 부르지만, 베트남에서는 'xi lanh thủy lực' 또는 간단히 'xi lanh dầu'라고 합니다. 'xi lanh'는 프랑스 식민지 시대의 영향으로 정착된 외래어입니다. 한국 현장에서는 실린더 행정(stroke)을 밀리미터로 표기하는데, 베트남에서도 동일하게 mm 단위를 사용합니다. 다만 한국은 실린더 내경을 '보어(bore)'라고 부르지만, 베트남에서는 '직경(đường kính)' 또는 '구경(kính)'이라고 표현하므로 통역 시 혼동하지 않도록 주의해야 합니다. 또한 한국 정비 기준은 실린더 누유 발생 시 즉시 교체를 권장하지만, 베트남 일부 현장에서는 패킹만 교체하는 경우가 있어 안전기준 차이를 명확히 전달해야 합니다.",
        "commonMistakes": [
            {
                "mistake": "bom thủy lực(유압펌프)와 혼동",
                "correction": "xi lanh thủy lực (실린더 ≠ 펌프)",
                "explanation": "펌프는 압력 생성, 실린더는 직선운동 실행으로 역할이 다릅니다"
            },
            {
                "mistake": "động cơ thủy lực(유압모터)로 잘못 통역",
                "correction": "xi lanh (직선운동) vs động cơ (회전운동)",
                "explanation": "실린더는 직선, 모터는 회전운동을 만듭니다"
            },
            {
                "mistake": "실린더 로드를 '막대(막대기)'로 통역",
                "correction": "cần đẩy 또는 trục piston",
                "explanation": "막대는 일반 명사이며 전문용어는 cần đẩy입니다"
            }
        ],
        "examples": [
            {
                "ko": "붐실린더에서 오일이 새고 있으니 즉시 수리하세요.",
                "vi": "Xi lanh cần đang bị rò rỉ dầu, hãy sửa chữa ngay.",
                "situation": "formal"
            },
            {
                "ko": "실린더 로드에 흠집이 있으면 패킹이 손상될 수 있습니다.",
                "vi": "Nếu cần đẩy xi lanh bị trầy xước thì có thể làm hỏng phớt.",
                "situation": "formal"
            },
            {
                "ko": "암실린더 압력이 약해서 작업이 느려.",
                "vi": "Áp lực xi lanh tay yếu nên thi công chậm.",
                "situation": "informal"
            }
        ],
        "relatedTerms": ["유압펌프", "유압모터", "붐", "암"]
    },
    {
        "slug": "bom-thuy-luc",
        "korean": "유압펌프",
        "vietnamese": "bơm thủy lực",
        "hanja": "油壓pump",
        "hanjaReading": "유(기름 유) + 압(누를 압) + pump",
        "pronunciation": "범 투이 륵",
        "meaningKo": "유압유를 흡입하여 고압으로 배출하는 장치로, 건설장비 유압시스템의 동력원 역할을 합니다. 통역 시 '펌프'를 베트남어로 'bơm'이라고 하는데, 이는 프랑스어 'pompe'에서 유래한 외래어입니다. 한국 현장에서는 펌프 종류를 '기어펌프(bơm bánh răng)', '피스톤펌프(bơm piston)', '베인펌프(bơm cánh)'로 구분하는데, 각 펌프의 특성을 정확히 설명해야 정비나 교체 시 혼동을 막을 수 있습니다. 특히 유압펌프 고장 진단 시 '토출압력(áp suất đẩy)', '유량(lưu lượng)', '소음(tiếng ồn)', '발열(nóng)' 등 증상을 구체적으로 통역해야 정확한 원인 파악이 가능합니다.",
        "meaningVi": "Bơm thủy lực là thiết bị hút dầu thủy lực từ bình chứa và đẩy ra dưới áp suất cao để cung cấp năng lượng cho toàn bộ hệ thống thủy lực của máy xúc, máy ủi và các thiết bị công trình khác. Có ba loại bơm thủy lực chính: bơm bánh răng (gear pump), bơm piston (piston pump), bơm cánh (vane pump). Bơm thủy lực là bộ phận quan trọng nhất của hệ thống, khi hỏng sẽ làm toàn bộ máy ngừng hoạt động. Khi làm việc tại Hàn Quốc, cần chú ý kiểm tra bơm định kỳ và thay dầu đúng hạn để tránh hư hỏng.",
        "context": "건설장비 정비, 유압시스템 고장 진단, 펌프 교체 시",
        "culturalNote": "한국에서는 '유압펌프' 또는 줄여서 '펌프'라고 부르지만, 베트남에서는 'bơm thủy lực' 또는 'bơm dầu'라고 합니다. 'bơm'은 프랑스어 'pompe'에서 유래한 외래어로 베트남어에 정착되었습니다. 한국 현장에서는 펌프 성능을 '토출량(리터/분)'과 '압력(kgf/cm²)'으로 표기하는데, 베트남에서는 '유량(L/min)'과 '압력(bar 또는 MPa)'을 주로 사용하므로 통역 시 단위 환산이 필요합니다. 또한 한국은 펌프 교체 시 순정품을 선호하지만, 베트남 일부 현장에서는 재생품(bơm tái chế)을 사용하는 경우가 있어 품질 기준을 명확히 전달해야 합니다.",
        "commonMistakes": [
            {
                "mistake": "xi lanh thủy lực(유압실린더)와 혼동",
                "correction": "bơm thủy lực (펌프는 압력 생성, 실린더는 작동)",
                "explanation": "펌프는 유압 발생, 실린더는 유압을 받아 동작하는 장치입니다"
            },
            {
                "mistake": "bơm nước(물펌프)로 잘못 통역",
                "correction": "bơm thủy lực (유압펌프 ≠ 물펌프)",
                "explanation": "물펌프는 냉각수 순환용이며 유압펌프와는 다릅니다"
            },
            {
                "mistake": "펌프 압력을 psi 단위로 그대로 통역",
                "correction": "bar 또는 MPa로 환산",
                "explanation": "베트남에서는 bar나 MPa를 주로 사용하므로 환산 필요"
            }
        ],
        "examples": [
            {
                "ko": "이 굴삭기 유압펌프는 피스톤 타입으로 토출량이 200리터/분입니다.",
                "vi": "Bơm thủy lực của máy xúc này là loại piston, lưu lượng 200 lít/phút.",
                "situation": "formal"
            },
            {
                "ko": "펌프에서 이상한 소음이 나면 오일 부족이나 필터 막힘을 의심하세요.",
                "vi": "Nếu bơm phát ra tiếng ồn lạ thì nghi ngờ thiếu dầu hoặc lọc bị tắc.",
                "situation": "formal"
            },
            {
                "ko": "펌프가 뜨거워지면 과부하 걸린 거니까 바로 멈춰야 해.",
                "vi": "Nếu bơm nóng lên là do quá tải, phải dừng ngay.",
                "situation": "informal"
            }
        ],
        "relatedTerms": ["유압모터", "유압실린더", "유압밸브", "작동유"]
    },
    {
        "slug": "lop-may-xay-dung",
        "korean": "건설장비타이어",
        "vietnamese": "lốp máy xây dựng",
        "hanja": "建設裝備tire",
        "hanjaReading": "건(세울 건) + 설(세울 설) + 장(꾸밀 장) + 비(갖출 비) + tire",
        "pronunciation": "럽 마이 싸이 증",
        "meaningKo": "로더, 덤프트럭, 그레이더 등 바퀴식 건설장비에 장착되는 대형 타이어입니다. 통역 시 궤도식 장비의 '캐터필러'와 명확히 구분해야 하며, 베트남어로는 'lốp máy xây dựng' 또는 'lốp xe công trình'이라고 합니다. 한국 현장에서는 타이어 규격을 '23.5-25' 같은 인치 방식으로 표기하는데, 베트남에서도 동일한 규격 체계를 사용합니다. 다만 타이어 공기압을 한국은 'kgf/cm²'로, 베트남은 'bar' 또는 'psi'로 표기하는 경우가 많아 통역 시 단위 확인이 필요합니다. 특히 타이어 점검 시 '트레드 깊이(độ sâu rãnh gai)', '편마모(mòn lệch)', '측면 손상(tổn thương thành bên)' 등을 정확히 전달해야 파열 사고를 예방할 수 있습니다.",
        "meaningVi": "Lốp máy xây dựng là loại lốp cỡ lớn được gắn trên các thiết bị công trình bánh lốp như máy xúc lật, xe tải hạng nặng, máy san. Khác với lốp xe ô tô thường, lốp máy xây dựng có kết cấu chắc chắn hơn, gai sâu hơn để chịu được tải trọng lớn và địa hình khó. Có hai loại chính: lốp không săm (tubeless) và lốp có săm (tube type). Khi làm việc tại công trường Hàn Quốc, cần kiểm tra áp suất lốp hàng ngày và thay lốp đúng quy cách để đảm bảo an toàn.",
        "context": "건설장비 정비, 로더/덤프트럭 점검, 타이어 교체 시",
        "culturalNote": "한국에서는 '타이어'라는 영어 발음을 그대로 사용하지만, 베트남에서는 'lốp'(프랑스어 'loppe'에서 유래)이 표준입니다. 한국 현장에서는 건설장비 타이어를 '중장비타이어' 또는 '건설기계타이어'라고 부르는데, 베트남에서는 'lốp máy xây dựng' 또는 'lốp xe công trình'으로 통일해서 사용합니다. 한국은 타이어 공기압 관리를 정기적으로 하지만, 베트남 일부 현장에서는 육안으로만 확인하는 경우가 있어 통역 시 공기압 측정 중요성을 강조해야 합니다. 또한 한국은 타이어 폐기 기준을 트레드 깊이(mm)로 명확히 정하지만, 베트남 일부 현장에서는 '겉으로 봐서 괜찮으면 사용'하는 관습이 있어 안전기준 차이를 명확히 전달해야 합니다.",
        "commonMistakes": [
            {
                "mistake": "lốp xe(자동차 타이어)로 통역",
                "correction": "lốp máy xây dựng (건설장비타이어)",
                "explanation": "일반 자동차 타이어와 건설장비 타이어는 규격과 구조가 다릅니다"
            },
            {
                "mistake": "xích máy(캐터필러)와 혼동",
                "correction": "lốp (타이어) vs xích (무한궤도)",
                "explanation": "바퀴식 장비는 lốp, 궤도식 장비는 xích을 사용합니다"
            },
            {
                "mistake": "타이어 규격 '23.5-25'를 베트남어로 읽기",
                "correction": "국제 규격 그대로 사용 (23.5-25)",
                "explanation": "타이어 규격은 국제 표준이므로 번역하지 않습니다"
            }
        ],
        "examples": [
            {
                "ko": "이 로더 타이어 규격은 23.5-25이고 공기압은 3.5바입니다.",
                "vi": "Lốp máy xúc lật này có quy cách 23.5-25, áp suất 3.5 bar.",
                "situation": "formal"
            },
            {
                "ko": "타이어 트레드 깊이가 10밀리 이하면 교체하세요.",
                "vi": "Nếu độ sâu rãnh gai lốp dưới 10mm thì phải thay.",
                "situation": "formal"
            },
            {
                "ko": "타이어 옆구리에 금 가서 터질 것 같아.",
                "vi": "Thành bên lốp bị nứt, có vẻ sắp nổ.",
                "situation": "informal"
            }
        ],
        "relatedTerms": ["로더", "덤프트럭", "그레이더", "공기압"]
    },
    {
        "slug": "cabin-may",
        "korean": "운전실",
        "vietnamese": "cabin máy",
        "hanja": "運轉室",
        "hanjaReading": "운(구를 운) + 전(구를 전) + 실(집 실)",
        "pronunciation": "까빈 마이",
        "meaningKo": "건설장비 운전자가 탑승하여 조작하는 밀폐된 공간으로, 조종석·조작 패널·좌석 등이 설치되어 있습니다. 통역 시 '캐빈(cabin)'과 '운전실'을 혼용하는데, 베트남어로는 'cabin máy' 또는 'buồng lái'라고 합니다. 한국 현장에서는 단순히 '캐빈'이라고 하지만, 베트남에서는 'cabin'이 프랑스어 외래어로 정착되어 있어 'cabin máy' 또는 'cabin xe'로 구체화해서 말하는 것이 명확합니다. 특히 안전교육 시 운전실의 '안전벨트(dây an toàn)', '소화기(bình cứu hỏa)', '비상탈출구(lối thoát hiểm)' 등을 정확히 전달해야 사고 시 대응이 원활합니다. 또한 여름철 운전실 내부 온도 관리를 위한 '에어컨(điều hòa)', '환기(thông gió)' 관련 용어도 자주 사용됩니다.",
        "meaningVi": "Cabin máy (hay buồng lái) là không gian kín dành cho người vận hành thiết bị công trình, bên trong có ghế ngồi, bảng điều khiển, cần điều khiển. Cabin máy hiện đại thường được trang bị điều hòa, hệ thống âm thanh, camera lùi. Khi làm việc tại công trường Hàn Quốc, cần kiểm tra cabin thường xuyên để đảm bảo hệ thống điều khiển, kính, gương chiếu hậu, đèn chiếu sáng đều hoạt động tốt - đây là yếu tố quan trọng đảm bảo an toàn lao động.",
        "context": "건설장비 운용, 안전교육, 장비 점검, 캐빈 청소·정비 시",
        "culturalNote": "한국에서는 '캐빈' 또는 '운전실'이라고 부르는데, 젊은 작업자는 '캐빈', 나이 든 작업자는 '운전실'을 선호하는 경향이 있습니다. 베트남에서는 'cabin máy'가 가장 보편적이며, 일부는 'buồng lái' 또는 'phòng điều khiển'이라고도 합니다. 'cabin'은 프랑스어 외래어로 베트남어에 정착되었습니다. 한국 현장에서는 운전실 내부 청결을 개인 책임으로 보지만, 베트남 일부 현장에서는 청소 담당자가 따로 있는 경우도 있어 관리 방식 차이를 명확히 전달해야 합니다. 또한 한국은 운전실 에어컨을 거의 모든 장비에 기본 장착하지만, 베트남 일부 오래된 장비는 에어컨이 없어 여름철 작업 시 힘들어하는 경우가 있으므로 통역 시 이를 고려해야 합니다.",
        "commonMistakes": [
            {
                "mistake": "buồng lái ô tô(자동차 운전석)로 통역",
                "correction": "cabin máy (건설장비 운전실)",
                "explanation": "자동차와 건설장비 운전실은 구조와 규모가 다르므로 cabin máy로 구분"
            },
            {
                "mistake": "phòng(방)로 통역",
                "correction": "cabin máy",
                "explanation": "phòng은 일반 건물 방을 의미하며 장비 운전실에는 부적합"
            },
            {
                "mistake": "cabin을 '개빈'으로 한글 발음하여 통역",
                "correction": "베트남어 발음 'cabin'(까빈)으로 전달",
                "explanation": "cabin은 베트남어 외래어이므로 베트남식 발음으로 말해야 합니다"
            }
        ],
        "examples": [
            {
                "ko": "작업 전 운전실 내부 안전벨트와 소화기를 확인하세요.",
                "vi": "Trước khi làm việc, hãy kiểm tra dây an toàn và bình cứu hỏa trong cabin máy.",
                "situation": "formal"
            },
            {
                "ko": "캐빈 에어컨이 고장나서 더워 죽겠어요.",
                "vi": "Điều hòa cabin máy bị hỏng nên nóng chết được.",
                "situation": "informal"
            },
            {
                "ko": "이 굴삭기 운전실에는 후방카메라가 설치되어 있습니다.",
                "vi": "Cabin máy xúc này có lắp camera lùi.",
                "situation": "formal"
            }
        ],
        "relatedTerms": ["조종석", "조작패널", "안전벨트", "에어컨"]
    }
]

# Filter out duplicates
new_terms_filtered = [t for t in new_terms if t['slug'] not in existing_slugs]

# Extend data
data.extend(new_terms_filtered)

# Save back to file
with open(file_path, 'w', encoding='utf-8') as f:
    json.dump(data, f, ensure_ascii=False, indent=2)

print(f"✅ Added {len(new_terms_filtered)} new terms to construction.json")
print(f"📊 Total terms now: {len(data)}")
