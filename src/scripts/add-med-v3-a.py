#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
의료 전문용어 추가 스크립트 v3-a
20개 정형외과/재활의학 용어 추가
"""

import json
import os

# PATH CODE (MUST USE)
file_path = os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', 'data', 'terms', 'medical.json')
with open(file_path, 'r', encoding='utf-8') as f:
    data = json.load(f)  # data is a LIST, not dict

existing_slugs = {t['slug'] for t in data}

# 20개 신규 의료 용어 (정형외과/재활의학)
new_terms = [
    {
        "slug": "gay-xuong",
        "korean": "골절",
        "vietnamese": "Gãy xương",
        "hanja": "骨折",
        "hanjaReading": "骨(뼈 골) + 折(꺾을 절)",
        "pronunciation": "가이 쑤엉",
        "meaningKo": "뼈가 외부 충격으로 부러지거나 금이 간 상태. 통역 시 '단순골절'과 '복합골절'을 정확히 구분해야 하며, 환자가 '금 갔다'고 표현할 때 베트남어로는 'nứt xương'(금 간 뼈)과 'gãy xương'(완전 골절)을 명확히 구분해 전달해야 한다. 응급실에서 자주 쓰이므로 빠른 의사소통이 중요하다.",
        "meaningVi": "Tình trạng xương bị gãy hoặc nứt do va chạm mạnh từ bên ngoài. Trong y học, phân biệt rõ 'gãy xương đơn giản' (không thủng da) và 'gãy xương phức tạp' (xương chọc thủng da). Cần xử lý khẩn cấp để tránh biến chứng.",
        "context": "응급실, 정형외과, 사고 현장",
        "culturalNote": "한국에서는 '뼈에 금 갔다'는 표현을 일상적으로 쓰지만 베트남에서는 의료적으로 'nứt xương'과 'gãy xương'을 엄격히 구분한다. 한국 환자는 골절을 과소평가하는 경향이 있어 '괜찮다'고 말하는 경우가 많으므로, 통역사는 의료진에게 정확한 증상을 전달해야 한다.",
        "commonMistakes": [
            {
                "mistake": "골절을 'xương bị gãy'로만 번역",
                "correction": "'gãy xương' 또는 'chấn thương gãy xương'",
                "explanation": "'xương bị gãy'는 구어체이며 의료 기록에는 'gãy xương'을 써야 정확함"
            },
            {
                "mistake": "'금 갔다'를 'gãy xương'으로 통역",
                "correction": "'nứt xương' (미세골절) 또는 'vết nứt ở xương'",
                "explanation": "금 간 것은 완전 골절이 아니므로 구분 필수"
            },
            {
                "mistake": "'골절 부위'를 'chỗ gãy'로만 표현",
                "correction": "'vị trí gãy xương' 또는 'điểm gãy'",
                "explanation": "의료 용어로는 'vị trí'(위치)를 명시해야 전문적"
            }
        ],
        "examples": [
            {
                "ko": "왼쪽 팔뚝에 골절이 확인되었습니다.",
                "vi": "Phát hiện gãy xương ở cẳng tay trái.",
                "situation": "formal"
            },
            {
                "ko": "골절 부위를 고정하고 즉시 병원으로 이송하세요.",
                "vi": "Cố định vị trí gãy xương và chuyển ngay đến bệnh viện.",
                "situation": "onsite"
            },
            {
                "ko": "X-ray 결과 단순 골절로 수술 없이 깁스만 하면 됩니다.",
                "vi": "Kết quả X-quang cho thấy gãy xương đơn giản, chỉ cần bó bột không cần phẫu thuật.",
                "situation": "formal"
            }
        ],
        "relatedTerms": ["복합골절", "석고붕대", "정형외과", "X-ray", "부목"]
    },
    {
        "slug": "gay-xuong-phuc-tap",
        "korean": "복합골절",
        "vietnamese": "Gãy xương phức tạp",
        "hanja": "複合骨折",
        "hanjaReading": "複(복잡할 복) + 合(합할 합) + 骨(뼈 골) + 折(꺾을 절)",
        "pronunciation": "가이 쑤엉 푹 땁",
        "meaningKo": "골절된 뼈가 피부를 뚫고 나오거나 여러 조각으로 분쇄된 상태. 통역 시 반드시 'gãy xương hở'(개방성 골절)인지 'gãy xương kín'(폐쇄성 골절)인지 구분해 전달해야 하며, 감염 위험이 높아 응급 수술이 필요함을 환자에게 명확히 설명해야 한다. '위험하다'는 표현보다 구체적인 의료 조치를 전달하는 것이 중요하다.",
        "meaningVi": "Tình trạng xương gãy vỡ thành nhiều mảnh hoặc xương gãy chọc thủng da (gãy xương hở). Nguy cơ nhiễm trùng cao, cần phẫu thuật khẩn cấp. Phân loại thành gãy xương hở và gãy xương kín để có phương án điều trị phù hợp.",
        "context": "응급실, 정형외과 수술실, 중증외상센터",
        "culturalNote": "한국에서는 복합골절을 '심한 골절' 정도로 인식하지만, 베트nam 의료진은 즉각적인 수술 여부를 판단하므로 통역사가 '개방성/폐쇄성' 여부를 정확히 전달하지 않으면 치료 지연이 발생할 수 있다. 한국 환자 가족은 수술을 꺼리는 경향이 있어 설득 과정에서 통역사의 역할이 크다.",
        "commonMistakes": [
            {
                "mistake": "'복합골절'을 'gãy xương phức tạp'로만 번역",
                "correction": "'gãy xương hở' 또는 'gãy xương phức tạp có vết thương hở'",
                "explanation": "개방성 골절 여부를 명시해야 치료 방향이 결정됨"
            },
            {
                "mistake": "'뼈가 튀어나왔다'를 'xương nhô ra'로 직역",
                "correction": "'xương chọc thủng da' 또는 'gãy xương hở'",
                "explanation": "의료 용어로 정확히 표현해야 응급 처치가 빠름"
            },
            {
                "mistake": "'위험하다'를 'nguy hiểm'으로만 전달",
                "correction": "'cần phẫu thuật khẩn cấp để tránh nhiễm trùng'",
                "explanation": "구체적인 조치를 전달해야 환자가 심각성을 이해함"
            }
        ],
        "examples": [
            {
                "ko": "복합골절로 뼈가 피부 밖으로 노출되어 응급 수술이 필요합니다.",
                "vi": "Gãy xương hở với xương lộ ra ngoài da, cần phẫu thuật khẩn cấp.",
                "situation": "formal"
            },
            {
                "ko": "복합골절 환자는 감염 예방을 위해 항생제 투여가 필수입니다.",
                "vi": "Bệnh nhân gãy xương phức tạp bắt buộc phải dùng kháng sinh để phòng nhiễm trùng.",
                "situation": "formal"
            },
            {
                "ko": "사고 현장에서 복합골절 발견 시 절대 뼈를 만지지 마세요.",
                "vi": "Khi phát hiện gãy xương hở tại hiện trường, tuyệt đối không chạm vào xương.",
                "situation": "onsite"
            }
        ],
        "relatedTerms": ["골절", "개방성골절", "정형외과", "감염", "응급수술"]
    },
    {
        "slug": "trat-khop",
        "korean": "탈구",
        "vietnamese": "Trật khớp",
        "hanja": "脫臼",
        "hanjaReading": "脫(벗을 탈) + 臼(절구 구)",
        "pronunciation": "짯 컵",
        "meaningKo": "관절을 이루는 뼈가 정상 위치에서 어긋난 상태. 통역 시 환자가 '뼈가 빠졌다'고 표현하면 골절과 혼동하지 않도록 'trật khớp'으로 정확히 전달해야 하며, '도수정복'(chỉnh khớp bằng tay)이 가능한지 수술이 필요한지를 의료진과 확인해야 한다. 어깨, 턱관절 탈구가 가장 흔하다.",
        "meaningVi": "Tình trạng xương trong khớp bị lệch khỏi vị trí bình thường. Thường xảy ra ở khớp vai, khớp hàm. Cần chỉnh khớp bằng tay (nắn khớp) hoặc phẫu thuật tùy mức độ nghiêm trọng. Không tự chỉnh khớp để tránh tổn thương thêm.",
        "context": "응급실, 정형외과, 스포츠의학과",
        "culturalNote": "한국에서는 탈구를 '뼈가 빠졌다'고 표현하지만 베트남에서는 'trật khớp'과 'gãy xương'을 명확히 구분한다. 한국 환자는 턱관절 탈구(sai khớp hàm)를 대수롭지 않게 여기는 경향이 있으나, 베트남 의료진은 즉시 정복술을 권하므로 통역사가 환자 설득에 개입해야 하는 경우가 많다.",
        "commonMistakes": [
            {
                "mistake": "'뼈가 빠졌다'를 'xương bị rơi ra'로 직역",
                "correction": "'trật khớp' 또는 'khớp bị trật'",
                "explanation": "'뼈가 떨어졌다'는 의미가 아니라 관절 탈구를 의미함"
            },
            {
                "mistake": "'탈구'를 'gãy xương'(골절)로 혼동",
                "correction": "'trật khớp'으로 명확히 구분",
                "explanation": "골절과 탈구는 치료법이 완전히 다름"
            },
            {
                "mistake": "'도수정복'을 'chữa bằng tay'로만 번역",
                "correction": "'chỉnh khớp bằng tay' 또는 'nắn khớp'",
                "explanation": "'chữa'는 치료 일반이고 'chỉnh/nắn'이 정복술의 정확한 표현"
            }
        ],
        "examples": [
            {
                "ko": "어깨 탈구로 도수정복술을 시행했습니다.",
                "vi": "Đã thực hiện chỉnh khớp bằng tay cho trường hợp trật khớp vai.",
                "situation": "formal"
            },
            {
                "ko": "턱관절이 탈구되어 입을 다물 수 없습니다.",
                "vi": "Khớp hàm bị trật nên không thể khép miệng.",
                "situation": "onsite"
            },
            {
                "ko": "탈구 후 재발 방지를 위해 2주간 보조기를 착용하세요.",
                "vi": "Sau khi chỉnh khớp, đeo nẹp hỗ trợ trong 2 tuần để tránh tái phát.",
                "situation": "formal"
            }
        ],
        "relatedTerms": ["관절", "도수정복", "어깨탈구", "정형외과", "보조기"]
    },
    {
        "slug": "ton-thuong-day-chang",
        "korean": "인대손상",
        "vietnamese": "Tổn thương dây chằng",
        "hanja": "靭帶損傷",
        "hanjaReading": "靭(질긴 인) + 帶(띠 대) + 損(덜 손) + 傷(다칠 상)",
        "pronunciation": "톤 투엉 자이 짱",
        "meaningKo": "관절을 지지하는 인대가 늘어나거나 찢어진 상태. 통역 시 환자가 '삐었다'고 표현하면 단순 염좌인지 인대 파열인지 의료진이 판단하도록 정확히 전달해야 하며, MRI 검사 필요 여부를 확인해야 한다. 1도(경미), 2도(부분 파열), 3도(완전 파열)로 나뉘며 치료 방법이 다르므로 주의해야 한다.",
        "meaningVi": "Dây chằng giữ khớp bị giãn hoặc đứt. Phân loại mức độ 1 (nhẹ), mức độ 2 (đứt một phần), mức độ 3 (đứt hoàn toàn). Cần MRI để chẩn đoán chính xác. Điều trị từ nghỉ ngơi, vật lý trị liệu đến phẫu thuật tùy mức độ.",
        "context": "정형외과, 스포츠의학과, 재활의학과",
        "culturalNote": "한국에서는 '삐었다'는 표현으로 염좌와 인대손상을 구분 없이 쓰지만, 베트남 의료진은 'bong gân'(염좌)과 'đứt dây chằng'(인대 파열)을 명확히 구분한다. 한국 환자는 인대손상을 대수롭지 않게 여겨 방치하는 경우가 많으나, 베트남에서는 즉시 MRI를 촬영하므로 통역사가 검사 필요성을 설명해야 한다.",
        "commonMistakes": [
            {
                "mistake": "'삐었다'를 'bị vặn'으로만 번역",
                "correction": "'bong gân'(염좌) 또는 'tổn thương dây chằng'(인대손상)",
                "explanation": "의료 용어로 정확히 표현해야 치료 방향이 결정됨"
            },
            {
                "mistake": "'인대 파열'을 'dây chằng bị rách'로 번역",
                "correction": "'đứt dây chằng' 또는 'dây chằng bị đứt hoàn toàn'",
                "explanation": "'rách'는 찢어짐이고 'đứt'가 인대 파열의 정확한 표현"
            },
            {
                "mistake": "인대손상 정도를 전달하지 않음",
                "correction": "'mức độ 1/2/3' 또는 'nhẹ/trung bình/nặng'로 명시",
                "explanation": "치료법이 달라지므로 정도를 반드시 전달해야 함"
            }
        ],
        "examples": [
            {
                "ko": "무릎 인대손상 2도로 부분 파열이 확인되었습니다.",
                "vi": "Tổn thương dây chằng đầu gối mức độ 2, đứt một phần.",
                "situation": "formal"
            },
            {
                "ko": "발목을 삐어서 인대가 늘어났어요.",
                "vi": "Bong gân mắt cá chân, dây chằng bị giãn.",
                "situation": "informal"
            },
            {
                "ko": "인대 완전 파열로 재건 수술이 필요합니다.",
                "vi": "Dây chằng đứt hoàn toàn, cần phẫu thuật tái tạo dây chằng.",
                "situation": "formal"
            }
        ],
        "relatedTerms": ["전방십자인대", "염좌", "MRI", "재활치료", "관절경수술"]
    },
    {
        "slug": "day-chang-cheo-truoc",
        "korean": "전방십자인대",
        "vietnamese": "Dây chằng chéo trước",
        "hanja": "前方十字靭帶",
        "hanjaReading": "前(앞 전) + 方(모 방) + 十(열 십) + 字(글자 자) + 靭(질긴 인) + 帶(띠 대)",
        "pronunciation": "자이 짱 쩨오 쭈억",
        "meaningKo": "무릎 관절 내부에서 앞뒤 움직임을 제한하는 십자 모양 인대. 통역 시 축구, 농구 등 운동 중 파열이 흔하며, 환자가 '뚝' 소리를 들었다고 하면 파열 가능성이 높으므로 의료진에게 즉시 전달해야 한다. 수술 여부는 환자 나이, 활동량에 따라 결정되므로 상세한 문진이 중요하다.",
        "meaningVi": "Dây chằng hình chữ thập ở trong khớp gối, giữ ổn định chuyển động trước-sau. Thường bị đứt khi chơi thể thao (bóng đá, bóng rổ). Triệu chứng điển hình là nghe tiếng 'rắc', đầu gối sưng, không chịu lực. Cần phẫu thuật tái tạo dây chằng cho người trẻ hoặc vận động viên.",
        "context": "정형외과, 스포츠의학과, 재활의학과",
        "culturalNote": "한국에서는 'ACL 파열'이라는 영어 약어를 많이 쓰지만 베트남에서는 'đứt dây chằng chéo trước'으로 풀어서 말한다. 한국 환자는 수술을 미루려는 경향이 있으나 베트남 의료진은 젊은 환자에게 즉시 수술을 권하므로, 통역사가 수술 시기의 중요성을 설명해야 한다.",
        "commonMistakes": [
            {
                "mistake": "'ACL'을 그대로 사용",
                "correction": "'dây chằng chéo trước' 또는 'ACL (dây chằng chéo trước)'",
                "explanation": "베트남 환자는 영어 약어를 모를 수 있으므로 풀어서 설명"
            },
            {
                "mistake": "'십자인대'를 'dây chằng hình chữ thập'로만 번역",
                "correction": "'dây chằng chéo trước' (전방) 또는 'dây chằng chéo sau' (후방)",
                "explanation": "전방/후방을 명시해야 정확한 진단 가능"
            },
            {
                "mistake": "'뚝 소리'를 'tiếng kêu'로만 번역",
                "correction": "'tiếng rắc' 또는 'tiếng nổ tách'",
                "explanation": "인대 파열 시 특징적인 소리를 의료 용어로 표현"
            }
        ],
        "examples": [
            {
                "ko": "전방십자인대 파열로 관절경 재건술을 시행합니다.",
                "vi": "Đứt dây chằng chéo trước, thực hiện phẫu thuật tái tạo qua nội soi khớp.",
                "situation": "formal"
            },
            {
                "ko": "운동 중에 무릎에서 '뚝' 소리가 나고 주저앉았어요.",
                "vi": "Khi chơi thể thao, nghe tiếng rắc ở đầu gối và ngã ngồi.",
                "situation": "informal"
            },
            {
                "ko": "전방십자인대 수술 후 재활 기간은 6개월입니다.",
                "vi": "Sau phẫu thuật dây chằng chéo trước, thời gian phục hồi chức năng là 6 tháng.",
                "situation": "formal"
            }
        ],
        "relatedTerms": ["인대손상", "반월상연골", "관절경수술", "재활치료", "스포츠손상"]
    },
    {
        "slug": "sun-chem",
        "korean": "반월상연골",
        "vietnamese": "Sụn chêm",
        "hanja": "半月狀軟骨",
        "hanjaReading": "半(반 반) + 月(달 월) + 狀(모양 상) + 軟(부드러울 연) + 骨(뼈 골)",
        "pronunciation": "순 쩸",
        "meaningKo": "무릎 관절 사이에서 충격을 흡수하는 반달 모양의 연골. 통역 시 환자가 '무릎에서 소리가 난다', '걸릴 듯하다'고 표현하면 연골 파열을 의심하고 의료진에게 전달해야 한다. MRI 촬영이 필수이며, 파열 위치와 형태에 따라 봉합 또는 절제 수술을 결정한다.",
        "meaningVi": "Sụn hình bán nguyệt nằm giữa xương đùi và xương chày, có tác dụng đệm và giảm chấn động cho khớp gối. Khi sụn chêm bị rách, có triệu chứng khớp gối kêu, bị kẹt, đau. Cần chụp MRI để chẩn đoán. Điều trị bằng phẫu thuật nội soi khớp: khâu nối (nếu rách ít) hoặc cắt bỏ phần sụn rách.",
        "context": "정형외과, 스포츠의학과, 재활의학과",
        "culturalNote": "한국에서는 '연골 파열'이라는 표현을 많이 쓰지만 베트남에서는 'rách sụn chêm'으로 구체적으로 표현한다. 한국 환자는 연골 파열을 노화 현상으로 생각해 방치하는 경우가 많으나, 베트남 의료진은 젊은 환자에게도 즉시 수술을 권하므로 통역사가 수술 필요성을 설명해야 한다.",
        "commonMistakes": [
            {
                "mistake": "'연골'을 'sụn'으로만 번역",
                "correction": "'sụn chêm' 또는 'sụn bán nguyệt'",
                "explanation": "'sụn'은 연골 전체이고 'sụn chêm'이 반월상연골의 정확한 명칭"
            },
            {
                "mistake": "'연골 파열'을 'sụn bị vỡ'로 번역",
                "correction": "'rách sụn chêm' 또는 'sụn chêm bị rách'",
                "explanation": "'vỡ'는 부서짐이고 'rách'가 연골 파열의 정확한 표현"
            },
            {
                "mistake": "'무릎에서 소리 난다'를 'đầu gối kêu'로만 번역",
                "correction": "'đầu gối kêu cọt kẹt' 또는 'có tiếng kêu bất thường'",
                "explanation": "연골 파열의 특징적 증상을 구체적으로 전달해야 진단에 도움"
            }
        ],
        "examples": [
            {
                "ko": "MRI 결과 내측 반월상연골 파열이 확인되었습니다.",
                "vi": "Kết quả MRI cho thấy rách sụn chêm trong.",
                "situation": "formal"
            },
            {
                "ko": "무릎을 굽힐 때마다 걸리는 느낌이 들어요.",
                "vi": "Mỗi lần gập đầu gối có cảm giác bị kẹt.",
                "situation": "informal"
            },
            {
                "ko": "반월상연골 파열로 관절경 부분절제술을 시행했습니다.",
                "vi": "Đã thực hiện phẫu thuật cắt bỏ một phần sụn chêm qua nội soi khớp do rách sụn.",
                "situation": "formal"
            }
        ],
        "relatedTerms": ["전방십자인대", "관절경수술", "MRI", "무릎관절", "스포츠손상"]
    },
    {
        "slug": "chop-xoay",
        "korean": "회전근개",
        "vietnamese": "Chóp xoay",
        "hanja": "回轉筋蓋",
        "hanjaReading": "回(돌 회) + 轉(구를 전) + 筋(힘줄 근) + 蓋(덮을 개)",
        "pronunciation": "쪼프 쏘아이",
        "meaningKo": "어깨 관절을 덮고 있는 4개의 근육과 힘줄 집합체. 통역 시 환자가 '어깨가 아프다', '팔을 들 수 없다'고 하면 회전근개 파열을 의심하고 의료진에게 전달해야 한다. 나이가 들면 자연 파열되기 쉬우며, 부분 파열과 완전 파열에 따라 치료법이 다르므로 MRI 결과를 정확히 통역해야 한다.",
        "meaningVi": "Nhóm 4 cơ và gân bao quanh khớp vai, giúp xoay và nâng cánh tay. Khi bị rách (thường do tuổi tác hoặc chấn thương), có triệu chứng đau vai, không nâng tay lên được. Phân biệt rách một phần và rách hoàn toàn để quyết định điều trị vật lý trị liệu hay phẫu thuật.",
        "context": "정형외과, 재활의학과, 스포츠의학과",
        "culturalNote": "한국에서는 '오십견'과 '회전근개 파열'을 혼동하는 경우가 많지만, 베트남 의료진은 MRI로 명확히 구분한다. 한국 환자는 '나이 들면 어깨 아픈 거 당연하다'며 방치하지만, 베트남에서는 조기 치료를 강조하므로 통역사가 치료 시기를 설득해야 한다.",
        "commonMistakes": [
            {
                "mistake": "'회전근개'를 'cơ xoay'로만 번역",
                "correction": "'chóp xoay' 또는 'bộ phận cơ chóp xoay'",
                "explanation": "'chóp xoay'가 의료 용어로 정확한 표현"
            },
            {
                "mistake": "'오십견'과 '회전근개 파열'을 구분하지 않음",
                "correction": "오십견은 'đông cứng khớp vai', 회전근개는 'rách chóp xoay'",
                "explanation": "두 질환은 원인과 치료가 완전히 다름"
            },
            {
                "mistake": "'팔을 들 수 없다'를 'không nhấc tay lên được'로만 번역",
                "correction": "'không thể nâng tay lên do đau vai'로 증상 상세히 설명",
                "explanation": "통증 때문인지 근력 저하 때문인지 구분 필요"
            }
        ],
        "examples": [
            {
                "ko": "회전근개 완전 파열로 관절경 봉합술이 필요합니다.",
                "vi": "Rách hoàn toàn chóp xoay, cần phẫu thuật khâu nối qua nội soi khớp.",
                "situation": "formal"
            },
            {
                "ko": "밤에 어깨가 아파서 잠을 못 자겠어요.",
                "vi": "Ban đêm đau vai không ngủ được.",
                "situation": "informal"
            },
            {
                "ko": "회전근개 부분 파열은 물리치료로 회복 가능합니다.",
                "vi": "Rách một phần chóp xoay có thể hồi phục bằng vật lý trị liệu.",
                "situation": "formal"
            }
        ],
        "relatedTerms": ["오십견", "어깨통증", "관절경수술", "물리치료", "MRI"]
    },
    {
        "slug": "thoat-vi-dia-dem",
        "korean": "추간판탈출증",
        "vietnamese": "Thoát vị đĩa đệm",
        "hanja": "椎間板脫出症",
        "hanjaReading": "椎(등뼈 추) + 間(사이 간) + 板(널빤지 판) + 脫(벗을 탈) + 出(날 출) + 症(병 증)",
        "pronunciation": "토앗 비 지아 뎀",
        "meaningKo": "척추 뼈 사이 디스크가 튀어나와 신경을 압박하는 질환. 통역 시 환자가 '허리디스크', '목디스크'라고 표현하면 정확한 위치(요추/경추)를 확인하고, 다리/팔 저림 증상을 상세히 전달해야 한다. 수술 없이 보존적 치료로 회복 가능한 경우가 많으므로 환자에게 희망을 주는 것이 중요하다.",
        "meaningVi": "Đĩa đệm giữa các đốt sống bị lồi ra, chèn ép dây thần kinh gây đau và tê. Phân biệt thoát vị đĩa đệm thắt lưng (cột sống thắt lưng) và thoát vị đĩa đệm cổ (cột sống cổ). Điều trị bảo tồn (nghỉ ngơi, vật lý trị liệu, thuốc) hiệu quả trong nhiều trường hợp, chỉ phẫu thuật khi có chỉ định.",
        "context": "정형외과, 신경외과, 재활의학과, 통증의학과",
        "culturalNote": "한국에서는 '디스크'라는 영어 표현을 일상적으로 쓰지만 베트남에서는 'thoát vị đĩa đệm'이라는 정확한 의학 용어를 쓴다. 한국 환자는 '디스크=수술'이라고 생각하는 경우가 많아 공포를 느끼지만, 베트남 의료진은 보존적 치료를 먼저 시도하므로 통역사가 안심시켜야 한다.",
        "commonMistakes": [
            {
                "mistake": "'디스크'를 'đĩa'로만 번역",
                "correction": "'thoát vị đĩa đệm' 또는 'bệnh đĩa đệm'",
                "explanation": "'đĩa'는 원반이고 'thoát vị đĩa đệm'이 정확한 병명"
            },
            {
                "mistake": "'허리디스크'를 'đĩa thắt lưng'으로 번역",
                "correction": "'thoát vị đĩa đệm cột sống thắt lưng'",
                "explanation": "정확한 의학 용어로 표현해야 진료 기록에 적합"
            },
            {
                "mistake": "'다리 저림'을 'chân tê'로만 번역",
                "correction": "'tê buốt lan xuống chân' 또는 'tê bì ở chân'",
                "explanation": "저림의 양상과 범위를 상세히 전달해야 진단에 도움"
            }
        ],
        "examples": [
            {
                "ko": "요추 4-5번 추간판탈출증으로 신경 압박이 확인되었습니다.",
                "vi": "Thoát vị đĩa đệm L4-L5 có chèn ép dây thần kinh.",
                "situation": "formal"
            },
            {
                "ko": "허리 아프고 다리가 저려요.",
                "vi": "Đau lưng và tê buốt xuống chân.",
                "situation": "informal"
            },
            {
                "ko": "추간판탈출증 초기는 물리치료와 약물로 충분히 회복됩니다.",
                "vi": "Giai đoạn đầu thoát vị đĩa đệm có thể hồi phục hoàn toàn bằng vật lý trị liệu và thuốc.",
                "situation": "formal"
            }
        ],
        "relatedTerms": ["척추", "신경압박", "요통", "물리치료", "MRI"]
    },
    {
        "slug": "hep-ong-song",
        "korean": "척추관협착증",
        "vietnamese": "Hẹp ống sống",
        "hanja": "脊椎管狹窄症",
        "hanjaReading": "脊(등뼈 척) + 椎(등뼈 추) + 管(관 관) + 狹(좁을 협) + 窄(좁을 착) + 症(병 증)",
        "pronunciation": "헵 옹 송",
        "meaningKo": "척추관이 좁아져 신경을 압박하는 퇴행성 질환. 통역 시 환자가 '오래 걸으면 다리가 저려서 쉬었다 가야 한다'고 하면 전형적인 증상이므로 의료진에게 상세히 전달해야 한다. 고령 환자에게 흔하며 수술 여부는 보행 능력과 삶의 질을 고려해 신중히 결정한다.",
        "meaningVi": "Ống sống (kênh chứa tủy sống) bị hẹp lại, chèn ép tủy sống và rễ thần kinh. Bệnh thoái hóa hay gặp ở người cao tuổi. Triệu chứng điển hình: đi bộ một đoạn thì đau và tê chân, phải nghỉ một lúc mới đi tiếp được. Điều trị từ thuốc, vật lý trị liệu đến phẫu thuật giải áp tùy mức độ.",
        "context": "정형외과, 신경외과, 재활의학과",
        "culturalNote": "한국 환자는 '나이 들면 당연하다'며 방치하지만, 보행 장애가 심해지면 삶의 질이 급격히 떨어지므로 베트남 의료진은 적극적 치료를 권한다. 통역사는 '간헐적 파행'(đi một đoạn phải nghỉ) 증상을 정확히 전달해 혈관 질환과 구분하도록 해야 한다.",
        "commonMistakes": [
            {
                "mistake": "'협착증'을 'hẹp'으로만 번역",
                "correction": "'hẹp ống sống' 또는 'bệnh hẹp ống sống'",
                "explanation": "'hẹp'은 좁음이고 'hẹp ống sống'이 정확한 병명"
            },
            {
                "mistake": "'간헐적 파행'을 'đi khập khiễng'으로 번역",
                "correction": "'đi được một đoạn thì đau và tê, phải nghỉ mới đi tiếp'",
                "explanation": "'khập khiễng'은 절뚝거림이고, 협착증의 증상은 다름"
            },
            {
                "mistake": "'척추관'을 'cột sống'으로만 번역",
                "correction": "'ống sống' 또는 'kênh tủy sống'",
                "explanation": "'cột sống'은 척추 전체이고 'ống sống'이 척추관의 정확한 표현"
            }
        ],
        "examples": [
            {
                "ko": "요추 척추관협착증으로 100m 걷기도 힘듭니다.",
                "vi": "Hẹp ống sống thắt lưng, đi bộ 100m cũng khó khăn.",
                "situation": "formal"
            },
            {
                "ko": "조금 걷다가 쉬었다 가야 해요.",
                "vi": "Đi một chút phải nghỉ rồi mới đi tiếp.",
                "situation": "informal"
            },
            {
                "ko": "척추관협착증 수술로 신경 압박을 해소했습니다.",
                "vi": "Đã giải phóng chèn ép thần kinh bằng phẫu thuật hẹp ống sống.",
                "situation": "formal"
            }
        ],
        "relatedTerms": ["척추", "퇴행성질환", "신경압박", "간헐적파행", "척추수술"]
    },
    {
        "slug": "veo-cot-song",
        "korean": "측만증",
        "vietnamese": "Vẹo cột sống",
        "hanja": "側彎症",
        "hanjaReading": "側(곁 측) + 彎(구부릴 만) + 症(병 증)",
        "pronunciation": "베오 꼿 송",
        "meaningKo": "척추가 옆으로 휘어지는 변형 질환. 통역 시 청소년기 발견이 중요하며, 부모에게 '한쪽 어깨가 높다', '허리선이 비대칭'이라는 증상을 설명해야 한다. Cobb 각도 10도 이상이면 진단하며, 각도에 따라 관찰, 보조기, 수술을 결정한다.",
        "meaningVi": "Cột sống bị cong sang một bên, nhìn từ phía sau thấy lệch. Thường phát hiện ở thanh thiếu niên. Dấu hiệu: vai không bằng nhau, đường eo không đối xứng. Đo góc Cobb để đánh giá mức độ: < 20 độ theo dõi, 20-40 độ đeo nẹp chỉnh hình, > 40 độ phẫu thuật.",
        "context": "정형외과, 소아정형외과, 재활의학과",
        "culturalNote": "한국에서는 학교 건강검진에서 측만증을 발견하는 경우가 많지만, 베트남에서는 부모가 직접 발견하는 경우가 많다. 한국 부모는 '자세가 나쁘다'고 혼내지만, 측만증은 자세 문제가 아니라 질환이므로 통역사가 정확히 설명해야 한다.",
        "commonMistakes": [
            {
                "mistake": "'척추측만증'을 'cột sống cong'으로만 번역",
                "correction": "'vẹo cột sống' 또는 'bệnh vẹo cột sống'",
                "explanation": "'cong'은 구부러짐 일반이고 'vẹo'가 측만의 정확한 표현"
            },
            {
                "mistake": "'자세가 나빠서 생긴다'고 설명",
                "correction": "'đây là bệnh lý, không phải do tư thế xấu'",
                "explanation": "측만증은 자세 문제가 아니라 척추 변형 질환임을 명확히"
            },
            {
                "mistake": "Cobb 각도를 전달하지 않음",
                "correction": "'góc Cobb [X] độ'로 수치 명시",
                "explanation": "치료 방향이 각도에 따라 결정되므로 반드시 전달"
            }
        ],
        "examples": [
            {
                "ko": "Cobb 각 25도의 청소년기 특발성 측만증입니다.",
                "vi": "Vẹo cột sống tự phát ở thanh thiếu niên, góc Cobb 25 độ.",
                "situation": "formal"
            },
            {
                "ko": "한쪽 어깨가 다른 쪽보다 높아요.",
                "vi": "Một bên vai cao hơn bên kia.",
                "situation": "informal"
            },
            {
                "ko": "측만증 교정을 위해 보조기를 하루 18시간 착용해야 합니다.",
                "vi": "Để chỉnh vẹo cột sống, phải đeo nẹp 18 giờ mỗi ngày.",
                "situation": "formal"
            }
        ],
        "relatedTerms": ["척추", "보조기", "청소년", "자세", "정형외과"]
    },
    {
        "slug": "dau-than-kinh-toa",
        "korean": "좌골신경통",
        "vietnamese": "Đau thần kinh tọa",
        "hanja": "坐骨神經痛",
        "hanjaReading": "坐(앉을 좌) + 骨(뼈 골) + 神(귀신 신) + 經(지날 경) + 痛(아플 통)",
        "pronunciation": "다우 턴 낑 토아",
        "meaningKo": "좌골신경이 압박되어 엉덩이에서 다리로 통증이 퍼지는 증상. 통역 시 '다리가 찌릿하다', '전기 오는 것 같다'는 환자 표현을 'đau như điện giật'으로 정확히 전달해야 한다. 추간판탈출증, 척추관협착증 등이 원인이므로 원인 질환 치료가 중요함을 설명해야 한다.",
        "meaningVi": "Đau lan từ mông xuống chân do thần kinh tọa bị chèn ép. Triệu chứng: đau như điện giật, tê buốt, yếu cơ. Nguyên nhân thường do thoát vị đĩa đệm, hẹp ống sống. Điều trị tập trung vào nguyên nhân gốc, kết hợp thuốc giảm đau và vật lý trị liệu.",
        "context": "정형외과, 신경외과, 통증의학과, 재활의학과",
        "culturalNote": "한국 환자는 '다리 저리다'는 표현으로 모든 다리 증상을 말하지만, 베트남 의료진은 저림의 양상(tê, tê buốt, đau như điện giật)을 구분하므로 통역사가 상세히 묘사해야 한다. 좌골신경통은 증상이지 질환이 아니므로 원인 찾기가 중요함을 설명해야 한다.",
        "commonMistakes": [
            {
                "mistake": "'좌골신경통'을 질환으로 설명",
                "correction": "'triệu chứng đau do thần kinh tọa bị chèn ép'",
                "explanation": "좌골신경통은 증상이지 원인이 아님을 명확히"
            },
            {
                "mistake": "'찌릿하다'를 'tê'로만 번역",
                "correction": "'đau như điện giật' 또는 'tê buốt'",
                "explanation": "단순 저림(tê)과 전기 오는 통증(điện giật)은 다름"
            },
            {
                "mistake": "'엉덩이부터 다리까지'를 'từ mông đến chân'으로만 번역",
                "correction": "'đau lan từ mông qua đùi xuống bắp chân'",
                "explanation": "통증의 경로를 상세히 전달해야 진단에 도움"
            }
        ],
        "examples": [
            {
                "ko": "좌골신경통 증상으로 왼쪽 다리에 전기 오는 듯한 통증이 있습니다.",
                "vi": "Có triệu chứng đau thần kinh tọa, chân trái đau như điện giật.",
                "situation": "formal"
            },
            {
                "ko": "엉덩이부터 발끝까지 찌릿해요.",
                "vi": "Tê buốt từ mông xuống tận ngón chân.",
                "situation": "informal"
            },
            {
                "ko": "좌골신경통의 원인인 추간판탈출증을 먼저 치료해야 합니다.",
                "vi": "Cần điều trị thoát vị đĩa đệm - nguyên nhân gây đau thần kinh tọa.",
                "situation": "formal"
            }
        ],
        "relatedTerms": ["추간판탈출증", "척추관협착증", "신경압박", "방사통", "물리치료"]
    },
    {
        "slug": "viem-can-gan-chan",
        "korean": "족저근막염",
        "vietnamese": "Viêm cân gan chân",
        "hanja": "足底筋膜炎",
        "hanjaReading": "足(발 족) + 底(밑 저) + 筋(힘줄 근) + 膜(막 막) + 炎(불꽃 염)",
        "pronunciation": "비엠 껀 간 쩐",
        "meaningKo": "발바닥 근막에 염증이 생겨 발꿈치가 아픈 질환. 통역 시 환자가 '아침에 일어나 첫 발을 디딜 때 가장 아프다'고 하면 전형적인 증상이므로 의료진에게 전달해야 한다. 장시간 서 있는 직업, 비만, 평발이 위험 요인이며, 스트레칭과 깔창이 치료의 핵심임을 설명해야 한다.",
        "meaningVi": "Viêm cân mạc dưới lòng bàn chân gây đau gót chân. Triệu chứng đặc trưng: đau nhất khi vừa thức dậy bước chân đầu tiên. Nguyên nhân: đứng lâu, béo phì, bàn chân bẹt. Điều trị: nghỉ ngơi, kéo giãn cơ, đi giày có đệm lót, thuốc chống viêm.",
        "context": "정형외과, 재활의학과, 통증의학과",
        "culturalNote": "한국 환자는 '발뒤꿈치가 아프다'고만 표현하지만, 베트남 의료진은 통증의 시간(아침/저녁)과 양상(찌르는 듯/뻐근함)을 구분하므로 통역사가 상세히 물어봐야 한다. 한국에서는 '발바닥 테이핑'이 흔하지만 베트남에서는 깔창(miếng lót giày) 처방이 더 일반적이다.",
        "commonMistakes": [
            {
                "mistake": "'족저근막염'을 'viêm gân chân'으로 번역",
                "correction": "'viêm cân gan chân' 또는 'viêm cân mạc gan chân'",
                "explanation": "'gân'은 힘줄이고 'cân'이 근막의 정확한 표현"
            },
            {
                "mistake": "'발뒤꿉치 통증'을 'đau gót chân'으로만 번역",
                "correction": "'đau gót chân khi vừa thức dậy bước chân đầu tiên'",
                "explanation": "아침 첫 발 통증이 진단의 핵심 증상임"
            },
            {
                "mistake": "'깔창'을 'lót giày'로만 번역",
                "correction": "'miếng lót giày chỉnh hình' 또는 'đệm lót hỗ trợ vòm bàn chân'",
                "explanation": "일반 깔창이 아닌 교정용 깔창임을 명시"
            }
        ],
        "examples": [
            {
                "ko": "족저근막염으로 아침에 첫 발을 디딜 때 극심한 통증이 있습니다.",
                "vi": "Viêm cân gan chân, đau dữ dội khi vừa thức dậy bước chân đầu tiên.",
                "situation": "formal"
            },
            {
                "ko": "발뒤꿈치가 찌르는 것처럼 아파요.",
                "vi": "Gót chân đau như bị đâm.",
                "situation": "informal"
            },
            {
                "ko": "족저근막염 치료를 위해 매일 스트레칭과 교정 깔창 착용이 필요합니다.",
                "vi": "Để điều trị viêm cân gan chân, cần kéo giãn hàng ngày và đi giày có miếng lót chỉnh hình.",
                "situation": "formal"
            }
        ],
        "relatedTerms": ["발꿈치통증", "평발", "스트레칭", "깔창", "물리치료"]
    },
    {
        "slug": "dong-cung-khop-vai",
        "korean": "오십견",
        "vietnamese": "Đông cứng khớp vai",
        "hanja": "五十肩",
        "hanjaReading": "五(다섯 오) + 十(열 십) + 肩(어깨 견)",
        "pronunciation": "동 꿍 컵 바이",
        "meaningKo": "어깨 관절이 굳어 움직임이 제한되는 질환. 통역 시 환자가 '팔을 뒤로 돌릴 수 없다', '머리를 빗을 수 없다'고 하면 전형적인 증상이며, 회전근개 파열과 구분해야 한다. 50대에 흔하지만 당뇨 환자는 더 젊은 나이에도 발생하며, 자연 회복까지 1-2년 걸린다는 점을 환자에게 설명해야 한다.",
        "meaningVi": "Khớp vai bị cứng, hạn chế vận động (còn gọi là vai đông cứng). Thường gặp ở người 50 tuổi, người tiểu đường. Triệu chứng: không duỗi tay ra sau, không chải đầu được. Khác với rách chóp xoay. Điều trị: vật lý trị liệu, thuốc, tiêm khớp. Tự hồi phục sau 1-2 năm.",
        "context": "정형외과, 재활의학과",
        "culturalNote": "한국에서는 '오십견'이라는 이름 때문에 50대에만 생긴다고 오해하지만, 당뇨 환자는 40대에도 흔하다. 베트남에서는 'đông cứng khớp vai'(어깨 관절 동결)이라는 병리적 명칭을 쓴다. 한국 환자는 '낫는다'는 말에 치료를 소홀히 하지만, 재활 치료를 안 하면 회복이 더디므로 통역사가 강조해야 한다.",
        "commonMistakes": [
            {
                "mistake": "'오십견'을 'vai năm mươi tuổi'로 직역",
                "correction": "'đông cứng khớp vai' 또는 'vai đông cứng'",
                "explanation": "나이가 아닌 증상을 기준으로 한 의학 용어 사용"
            },
            {
                "mistake": "'회전근개 파열'과 구분 없이 통역",
                "correction": "오십견은 'đông cứng', 회전근개는 'rách chóp xoay'",
                "explanation": "두 질환은 치료가 완전히 다름"
            },
            {
                "mistake": "'저절로 낫는다'를 'tự khỏi'로만 전달",
                "correction": "'tự hồi phục sau 1-2 năm nếu tích cực vật lý trị liệu'",
                "explanation": "재활 치료 없이는 회복이 더디거나 불완전할 수 있음"
            }
        ],
        "examples": [
            {
                "ko": "오십견으로 팔을 옆으로 들거나 뒤로 돌릴 수 없습니다.",
                "vi": "Đông cứng khớp vai, không thể giơ tay ra ngang hoặc quay ra sau.",
                "situation": "formal"
            },
            {
                "ko": "머리를 빗거나 옷을 입기가 힘들어요.",
                "vi": "Khó chải đầu và mặc quần áo.",
                "situation": "informal"
            },
            {
                "ko": "오십견은 적극적인 물리치료로 회복 기간을 단축할 수 있습니다.",
                "vi": "Đông cứng khớp vai có thể rút ngắn thời gian hồi phục bằng vật lý trị liệu tích cực.",
                "situation": "formal"
            }
        ],
        "relatedTerms": ["회전근개", "어깨통증", "물리치료", "당뇨", "관절운동"]
    },
    {
        "slug": "phau-thuat-noi-soi-khop",
        "korean": "관절경수술",
        "vietnamese": "Phẫu thuật nội soi khớp",
        "hanja": "關節鏡手術",
        "hanjaReading": "關(관계 관) + 節(마디 절) + 鏡(거울 경) + 手(손 수) + 術(재주 술)",
        "pronunciation": "퍼우 투얏 노이 쏘이 컵",
        "meaningKo": "작은 카메라를 관절에 삽입해 최소 절개로 수술하는 방법. 통역 시 환자에게 '흉터가 작다', '회복이 빠르다'는 장점을 설명하고, 전신마취가 필요하며 입원 기간은 보통 1-2일임을 전달해야 한다. 반월상연골, 전방십자인대, 회전근개 수술에 주로 쓰인다.",
        "meaningVi": "Phẫu thuật sử dụng camera nhỏ đưa vào khớp, rạch da tối thiểu. Ưu điểm: sẹo nhỏ, hồi phục nhanh, ít đau. Cần gây mê toàn thân, nằm viện 1-2 ngày. Dùng cho phẫu thuật sụn chêm, dây chằng chéo trước, chóp xoay.",
        "context": "정형외과, 스포츠의학과",
        "culturalNote": "한국 환자는 '내시경'이라는 용어에 익숙하지만 베트남에서는 'nội soi'라고 한다. 한국에서는 관절경 수술을 '간단한 수술'로 인식하는 경향이 있으나, 베트남 의료진은 전신마취와 재활 기간의 중요성을 강조하므로 통역사가 환자 기대치를 조정해야 한다.",
        "commonMistakes": [
            {
                "mistake": "'관절경'을 'kính khớp'으로만 번역",
                "correction": "'nội soi khớp' 또는 'phẫu thuật nội soi khớp'",
                "explanation": "'nội soi'가 의료 용어로 정확한 표현"
            },
            {
                "mistake": "'간단한 수술'이라고 설명",
                "correction": "'phẫu thuật ít xâm lấn nhưng vẫn cần gây mê và hồi phục'",
                "explanation": "최소 침습이지만 여전히 수술이며 재활이 필요함"
            },
            {
                "mistake": "마취 방법을 전달하지 않음",
                "correction": "'gây mê toàn thân' (전신마취) 명시",
                "explanation": "환자가 마취에 대한 준비를 해야 함"
            }
        ],
        "examples": [
            {
                "ko": "반월상연골 파열로 관절경 부분절제술을 시행합니다.",
                "vi": "Rách sụn chêm, thực hiện phẫu thuật cắt bỏ một phần qua nội soi khớp.",
                "situation": "formal"
            },
            {
                "ko": "흉터가 작아서 미용상 좋아요.",
                "vi": "Sẹo nhỏ nên tốt về mặt thẩm mỹ.",
                "situation": "informal"
            },
            {
                "ko": "관절경수술 후 2주간 목발 사용이 필요합니다.",
                "vi": "Sau phẫu thuật nội soi khớp, cần dùng nạng 2 tuần.",
                "situation": "formal"
            }
        ],
        "relatedTerms": ["반월상연골", "전방십자인대", "최소침습수술", "재활치료", "정형외과"]
    },
    {
        "slug": "phau-thuat-thay-khop-nhan-tao",
        "korean": "인공관절치환술",
        "vietnamese": "Phẫu thuật thay khớp nhân tạo",
        "hanja": "人工關節置換術",
        "hanjaReading": "人(사람 인) + 工(장인 공) + 關(관계 관) + 節(마디 절) + 置(둘 치) + 換(바꿀 환) + 術(재주 술)",
        "pronunciation": "퍼우 투얏 타이 컵 년 따오",
        "meaningKo": "손상된 관절을 인공 관절로 교체하는 수술. 통역 시 환자에게 수술 후 통증이 사라지고 보행이 가능해진다는 점을 강조하되, 인공 관절 수명은 15-20년이며 재수술이 필요할 수 있음을 설명해야 한다. 무릎, 고관절 치환이 가장 흔하며, 재활 기간은 3-6개월이다.",
        "meaningVi": "Phẫu thuật thay khớp bị hư bằng khớp nhân tạo. Thường làm ở khớp gối, khớp háng. Sau phẫu thuật hết đau, đi lại được. Khớp nhân tạo dùng được 15-20 năm, có thể cần thay lại. Thời gian phục hồi chức năng 3-6 tháng.",
        "context": "정형외과, 재활의학과",
        "culturalNote": "한국 환자는 '인공 관절'이라는 말에 거부감을 느끼는 경우가 많으나, 베트남 의료진은 '삶의 질 향상'을 강조한다. 한국 환자는 수술을 최대한 미루려 하지만, 너무 늦으면 근육이 약해져 회복이 어려우므로 통역사가 적절한 수술 시기를 설명해야 한다.",
        "commonMistakes": [
            {
                "mistake": "'인공 관절'을 'khớp giả'로 번역",
                "correction": "'khớp nhân tạo'",
                "explanation": "'giả'는 가짜라는 부정적 뉘앙스, 'nhân tạo'가 정확"
            },
            {
                "mistake": "'평생 쓴다'고 설명",
                "correction": "'dùng được 15-20 năm, có thể cần thay lại'",
                "explanation": "인공 관절 수명을 정확히 전달해야 기대치 조정"
            },
            {
                "mistake": "'수술 후 바로 걸을 수 있다'고 설명",
                "correction": "'sau phẫu thuật cần tập phục hồi chức năng 3-6 tháng'",
                "explanation": "재활 기간을 명시하지 않으면 환자가 실망할 수 있음"
            }
        ],
        "examples": [
            {
                "ko": "퇴행성 관절염이 심해 무릎 인공관절치환술을 권합니다.",
                "vi": "Viêm khớp thoái hóa nặng, khuyên thay khớp gối nhân tạo.",
                "situation": "formal"
            },
            {
                "ko": "수술 후에는 통증 없이 걸을 수 있어요.",
                "vi": "Sau phẫu thuật có thể đi lại không đau.",
                "situation": "informal"
            },
            {
                "ko": "인공관절 수술 후 3개월간 집중 재활치료가 필요합니다.",
                "vi": "Sau phẫu thuật thay khớp nhân tạo, cần điều trị phục hồi chức năng tích cực trong 3 tháng.",
                "situation": "formal"
            }
        ],
        "relatedTerms": ["퇴행성관절염", "고관절", "무릎관절", "재활치료", "정형외과"]
    },
    {
        "slug": "tri-lieu-bang-tay",
        "korean": "도수치료",
        "vietnamese": "Trị liệu bằng tay",
        "hanja": "徒手治療",
        "hanjaReading": "徒(무리 도) + 手(손 수) + 治(다스릴 치) + 療(병 고칠 료)",
        "pronunciation": "찌 리에우 방 따이",
        "meaningKo": "치료사가 손으로 근육과 관절을 풀어주는 치료. 통역 시 한국에서는 비급여 항목이지만 베트남에서는 일반 물리치료에 포함되는 경우가 많아 비용 차이를 설명해야 한다. '마사지'와 다른 의료행위이며, 척추·관절 질환에 효과적이지만 급성 염증이나 골절에는 금기임을 전달해야 한다.",
        "meaningVi": "Điều trị bằng cách trị liệu viên dùng tay nắn, kéo giãn cơ và khớp. Khác với massage thông thường, đây là liệu pháp y tế. Hiệu quả với bệnh cột sống, khớp. Chống chỉ định khi viêm cấp tính, gãy xương.",
        "context": "재활의학과, 정형외과, 통증의학과",
        "culturalNote": "한국에서는 도수치료가 고가의 비급여 항목으로 인식되지만, 베트남에서는 'trị liệu bằng tay' 또는 'vật lý trị liệu thủ công'으로 불리며 일반 재활 치료의 일부로 간주된다. 한국 환자는 '마사지 받는다'고 표현하지만, 의료진에게는 정확히 '의료적 도수치료'임을 전달해야 보험 적용 여부를 판단할 수 있다.",
        "commonMistakes": [
            {
                "mistake": "'도수치료'를 'massage'로 번역",
                "correction": "'trị liệu bằng tay' 또는 'thủ pháp chỉnh cơ xương khớp'",
                "explanation": "massage는 일반 마사지이고 도수치료는 의료행위"
            },
            {
                "mistake": "'누구나 받을 수 있다'고 설명",
                "correction": "'có chống chỉ định: viêm cấp, gãy xương, u'",
                "explanation": "금기사항을 전달하지 않으면 위험할 수 있음"
            },
            {
                "mistake": "비용 차이를 설명하지 않음",
                "correction": "'ở Hàn Quốc là dịch vụ tự trả, ở Việt Nam có thể được bảo hiểm'",
                "explanation": "양국 의료 시스템 차이를 환자에게 알려야 함"
            }
        ],
        "examples": [
            {
                "ko": "추간판탈출증으로 주 2회 도수치료를 받고 있습니다.",
                "vi": "Đang điều trị thoát vị đĩa đệm bằng trị liệu bằng tay 2 lần/tuần.",
                "situation": "formal"
            },
            {
                "ko": "도수치료 받으니까 허리가 한결 나아졌어요.",
                "vi": "Sau khi trị liệu bằng tay, lưng đỡ hơn nhiều.",
                "situation": "informal"
            },
            {
                "ko": "급성 염증 시에는 도수치료가 금기입니다.",
                "vi": "Khi viêm cấp tính, chống chỉ định trị liệu bằng tay.",
                "situation": "formal"
            }
        ],
        "relatedTerms": ["물리치료", "재활치료", "척추", "관절", "근육"]
    },
    {
        "slug": "vat-ly-tri-lieu-van-dong",
        "korean": "운동치료",
        "vietnamese": "Vật lý trị liệu vận động",
        "hanja": "運動治療",
        "hanjaReading": "運(운전할 운) + 動(움직일 동) + 治(다스릴 치) + 療(병 고칠 료)",
        "pronunciation": "벗 리 찌 리에우 번 동",
        "meaningKo": "치료사 지도 하에 운동으로 기능을 회복하는 치료. 통역 시 '집에서 혼자 하는 운동'과 다르며 전문 치료사가 환자 상태에 맞춰 강도를 조절함을 설명해야 한다. 수술 후 재활, 뇌졸중 후 보행 훈련, 근력 강화 등에 필수적이며, 꾸준히 해야 효과가 있음을 강조해야 한다.",
        "meaningVi": "Điều trị phục hồi chức năng bằng các bài tập vận động dưới sự hướng dẫn của trị liệu viên. Khác với tập thể dục tự do, đây là liệu pháp y tế có điều chỉnh cường độ theo từng bệnh nhân. Cần thiết sau phẫu thuật, đột quỵ, chấn thương. Hiệu quả khi kiên trì.",
        "context": "재활의학과, 정형외과, 신경과",
        "culturalNote": "한국 환자는 '운동치료'를 '체육관 운동'과 혼동하는 경우가 많으나, 베트남에서는 'vật lý trị liệu vận động'으로 의료 행위임을 명확히 한다. 한국 환자는 '집에서 혼자 할게요'라며 병원 재활을 거부하지만, 전문 치료사의 지도가 회복 속도를 2배 이상 빠르게 하므로 통역사가 설득해야 한다.",
        "commonMistakes": [
            {
                "mistake": "'운동치료'를 'tập thể dục'으로 번역",
                "correction": "'vật lý trị liệu vận động' 또는 'điều trị phục hồi chức năng'",
                "explanation": "'tập thể dục'은 일반 운동이고 운동치료는 의료행위"
            },
            {
                "mistake": "'집에서 해도 된다'고 설명",
                "correction": "'cần hướng dẫn của trị liệu viên chuyên khoa'",
                "explanation": "잘못된 운동은 오히려 악화시킬 수 있음"
            },
            {
                "mistake": "운동 강도를 전달하지 않음",
                "correction": "'cường độ nhẹ/vừa/nặng' 명시",
                "explanation": "환자가 집에서 할 때 강도 조절 필요"
            }
        ],
        "examples": [
            {
                "ko": "무릎 인공관절 수술 후 운동치료가 필수입니다.",
                "vi": "Sau phẫu thuật thay khớp gối nhân tạo, vật lý trị liệu vận động là bắt buộc.",
                "situation": "formal"
            },
            {
                "ko": "선생님 지도 하에 운동하니까 확실히 빨리 나아요.",
                "vi": "Tập với sự hướng dẫn của thầy thì hồi phục nhanh hơn rõ ràng.",
                "situation": "informal"
            },
            {
                "ko": "운동치료는 주 3회, 회당 30분씩 진행합니다.",
                "vi": "Vật lý trị liệu vận động 3 lần/tuần, mỗi lần 30 phút.",
                "situation": "formal"
            }
        ],
        "relatedTerms": ["재활치료", "물리치료", "근력강화", "가동범위", "재활의학"]
    },
    {
        "slug": "thang-do-dau",
        "korean": "통증척도",
        "vietnamese": "Thang đo đau",
        "hanja": "痛症尺度",
        "hanjaReading": "痛(아플 통) + 症(병 증) + 尺(자 척) + 度(법도 도)",
        "pronunciation": "탕 도 다우",
        "meaningKo": "통증 정도를 0-10점으로 수치화하는 도구. 통역 시 환자에게 '0은 전혀 안 아픈 것, 10은 참을 수 없는 극심한 통증'이라고 설명해야 한다. 한국 환자는 통증을 참는 경향이 있어 낮게 말하는 경우가 많으므로, '진짜 통증 정도'를 정확히 전달하도록 유도해야 한다.",
        "meaningVi": "Thang đánh giá mức độ đau từ 0-10 điểm. 0 là không đau, 10 là đau không chịu được. Dùng để đánh giá hiệu quả điều trị và quyết định dùng thuốc giảm đau. Bệnh nhân cần trung thực khi báo cáo mức độ đau.",
        "context": "통증의학과, 응급실, 병동, 재활의학과",
        "culturalNote": "한국 환자는 '참을 만하다'며 통증을 과소평가하는 경향이 있으나, 베트남 의료진은 수치를 기준으로 진통제를 처방하므로 통역사가 정확한 점수를 전달해야 한다. 또한 한국에서는 '10점'을 잘 쓰지 않지만, 베트남에서는 '10 điểm'이 실제 응급 상황을 의미하므로 구분이 중요하다.",
        "commonMistakes": [
            {
                "mistake": "'통증척도'를 'đo độ đau'로만 번역",
                "correction": "'thang đo đau' 또는 'thang điểm đau VAS'",
                "explanation": "'thang đo'가 의료 용어로 정확한 표현"
            },
            {
                "mistake": "환자가 '참을 만하다'고 하면 낮은 점수로 전달",
                "correction": "실제 통증 정도를 재확인 후 전달",
                "explanation": "한국 환자의 인내심 때문에 과소평가될 수 있음"
            },
            {
                "mistake": "척도 기준을 설명하지 않음",
                "correction": "'0 = không đau, 10 = đau không chịu được' 설명",
                "explanation": "환자가 척도를 이해해야 정확한 점수 부여 가능"
            }
        ],
        "examples": [
            {
                "ko": "현재 통증 정도를 0부터 10까지 중 몇 점으로 표현하시겠습니까?",
                "vi": "Hiện tại, mức độ đau của bạn là bao nhiêu điểm từ 0 đến 10?",
                "situation": "formal"
            },
            {
                "ko": "7점 이상이면 진통제를 추가로 드릴게요.",
                "vi": "Nếu từ 7 điểm trở lên, sẽ cho thêm thuốc giảm đau.",
                "situation": "onsite"
            },
            {
                "ko": "어제 8점이었는데 오늘은 5점으로 줄었어요.",
                "vi": "Hôm qua 8 điểm, hôm nay giảm xuống còn 5 điểm.",
                "situation": "informal"
            }
        ],
        "relatedTerms": ["통증", "진통제", "통증관리", "VAS", "통증의학"]
    },
    {
        "slug": "giai-phong-can-mac",
        "korean": "근막이완술",
        "vietnamese": "Giải phóng cân mạc",
        "hanja": "筋膜弛緩術",
        "hanjaReading": "筋(힘줄 근) + 膜(막 막) + 弛(늦출 이) + 緩(느릴 완) + 術(재주 술)",
        "pronunciation": "자이 퐁 껀 막",
        "meaningKo": "뭉친 근막을 풀어 통증을 완화하는 치료. 통역 시 '근막'이라는 개념을 베트남어로 설명하기 어려우므로 'cân mạc bao bọc cơ'(근육을 감싸는 막)로 풀어서 말해야 한다. 도수치료의 한 기법이며, 만성 통증, 근육 경직에 효과적이지만 1회로 끝나는 것이 아니라 여러 회 치료가 필요함을 설명해야 한다.",
        "meaningVi": "Liệu pháp nới lỏng cân mạc (lớp màng bao bọc cơ) để giảm đau. Một kỹ thuật trong trị liệu bằng tay. Hiệu quả với đau mãn tính, cứng cơ. Cần nhiều lần điều trị, không phải một lần là khỏi.",
        "context": "재활의학과, 정형외과, 통증의학과",
        "culturalNote": "한국에서는 '근막이완'이라는 용어가 최근 유행하지만, 베트남 환자는 이 개념을 잘 모르므로 통역사가 '근육을 감싸는 막을 풀어준다'고 쉽게 설명해야 한다. 한국 환자는 1-2회로 완치를 기대하지만, 만성 통증은 장기 치료가 필요하므로 현실적인 기대치를 전달해야 한다.",
        "commonMistakes": [
            {
                "mistake": "'근막'을 'gân'(힘줄)으로 번역",
                "correction": "'cân mạc' 또는 'màng cơ'",
                "explanation": "'gân'은 힘줄이고 'cân mạc'이 근막의 정확한 표현"
            },
            {
                "mistake": "'1회로 완치된다'고 설명",
                "correction": "'cần nhiều lần điều trị, từ 6-12 lần'",
                "explanation": "만성 통증은 장기 치료가 필요함을 명시"
            },
            {
                "mistake": "근막 개념을 설명하지 않음",
                "correction": "'lớp màng bao bọc cơ, khi bị căng gây đau'",
                "explanation": "환자가 이해해야 치료 순응도가 높아짐"
            }
        ],
        "examples": [
            {
                "ko": "만성 요통으로 근막이완술을 받고 있습니다.",
                "vi": "Đau lưng mãn tính, đang điều trị giải phóng cân mạc.",
                "situation": "formal"
            },
            {
                "ko": "근막이 풀리니까 움직임이 훨씬 편해졌어요.",
                "vi": "Sau khi nới lỏng cân mạc, cử động dễ dàng hơn nhiều.",
                "situation": "informal"
            },
            {
                "ko": "근막이완술은 주 2회, 총 10회 과정을 권장합니다.",
                "vi": "Giải phóng cân mạc khuyên điều trị 2 lần/tuần, tổng 10 lần.",
                "situation": "formal"
            }
        ],
        "relatedTerms": ["도수치료", "만성통증", "근육경직", "물리치료", "재활"]
    },
    {
        "slug": "bo-bot",
        "korean": "석고붕대",
        "vietnamese": "Bó bột",
        "hanja": "石膏繃帶",
        "hanjaReading": "石(돌 석) + 膏(기름 고) + 繃(동일 붕) + 帶(띠 대)",
        "pronunciation": "보 봇",
        "meaningKo": "골절 부위를 고정하기 위해 석고로 만든 붕대. 통역 시 환자에게 '깁스'라는 표현이 더 익숙하므로 'bó bột (깁스)'로 설명하고, 착용 기간, 샤워 방법, 가려움 대처법 등을 상세히 전달해야 한다. 최근에는 가볍고 방수되는 합성수지 재질도 있어 선택지를 제시해야 한다.",
        "meaningVi": "Băng bột (bó bột) dùng để cố định vị trí gãy xương. Thời gian đeo tùy vị trí gãy: tay 4-6 tuần, chân 6-8 tuần. Không được ướt, không được tháo tự ý. Có loại bột thường và loại tổng hợp nhẹ, chống nước.",
        "context": "응급실, 정형외과",
        "culturalNote": "한국에서는 '깁스'라는 일본어 외래어를 쓰지만, 베트남에서는 'bó bột'이 표준이다. 한국 환자는 깁스를 '불편하다'며 일찍 제거하려 하지만, 베트남 의료진은 정해진 기간을 엄수해야 한다고 강조하므로 통역사가 합병증 위험을 설명해야 한다.",
        "commonMistakes": [
            {
                "mistake": "'깁스'를 'gips'로 음차",
                "correction": "'bó bột' 또는 'băng bột'",
                "explanation": "베트남 의료 용어는 'bó bột'이 표준"
            },
            {
                "mistake": "착용 기간을 전달하지 않음",
                "correction": "'đeo bột [X] tuần' 명시",
                "explanation": "환자가 언제까지 착용해야 하는지 알아야 함"
            },
            {
                "mistake": "'물에 닿으면 안 된다'를 'không được dính nước'로만 전달",
                "correction": "'khi tắm, bọc túi nilon cẩn thận' 등 구체적 방법 제시",
                "explanation": "실생활 대처법을 알려줘야 순응도가 높아짐"
            }
        ],
        "examples": [
            {
                "ko": "팔목 골절로 4주간 석고붕대를 착용해야 합니다.",
                "vi": "Gãy xương cổ tay, phải bó bột 4 tuần.",
                "situation": "formal"
            },
            {
                "ko": "깁스 안이 가려워도 긁으면 안 돼요.",
                "vi": "Dù bên trong bột ngứa cũng không được gãi.",
                "situation": "informal"
            },
            {
                "ko": "방수 깁스로 하면 샤워할 때 편합니다.",
                "vi": "Nếu dùng bột tổng hợp chống nước thì tắm tiện hơn.",
                "situation": "onsite"
            }
        ],
        "relatedTerms": ["골절", "부목", "정형외과", "고정", "깁스"]
    }
]

# 중복 제거 및 추가
new_slugs_set = {term['slug'] for term in new_terms}
filtered_new_terms = [term for term in new_terms if term['slug'] not in existing_slugs]

# 기존 데이터 확장
data.extend(filtered_new_terms)

# 저장
with open(file_path, 'w', encoding='utf-8') as f:
    json.dump(data, f, ensure_ascii=False, indent=2)

# 결과 출력
added_count = len(filtered_new_terms)
skipped_count = len(new_terms) - added_count
total_count = len(data)

print(f"\n{'='*60}")
print(f"✅ 의료 용어 추가 완료 (v3-a)")
print(f"{'='*60}")
print(f"신규 추가: {added_count}개")
print(f"중복 제외: {skipped_count}개")
print(f"전체 용어: {total_count}개")
print(f"파일 위치: {file_path}")
print(f"{'='*60}\n")

if added_count > 0:
    print("추가된 용어:")
    for i, term in enumerate(filtered_new_terms, 1):
        print(f"  {i:2d}. {term['korean']:12s} - {term['vietnamese']}")
