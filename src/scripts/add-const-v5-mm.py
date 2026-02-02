#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Construction Terms Addition Script - Welding/Joining Theme
용접/접합 관련 전문용어 10개 추가
Tier S 기준 준수 (90점 이상)
"""

import json
import os

# 용접/접합 테마 용어 데이터 (Tier S 기준)
data = [
    {
        "slug": "han-arc",
        "korean": "아크용접",
        "vietnamese": "Hàn hồ quang",
        "hanja": "arc鎔接",
        "hanjaReading": "arc(외래어) + 鎔(녹을 용) + 接(이을 접)",
        "pronunciation": "한 홀 꽝",
        "meaningKo": "전기 아크의 고열을 이용하여 금속을 용융시켜 접합하는 용접 방법입니다. 통역 시 '아크'는 베트남어로 'hồ quang'(호광)으로 표현되며, 단순히 '용접'만 말하면 용접 방법이 특정되지 않아 오해가 발생할 수 있습니다. 건설 현장에서 가장 보편적으로 사용되는 용접 방법으로, 안전 교육 시 '전기 감전 위험'을 반드시 강조해야 합니다. 베트남 현장에서는 '한 디엔'(hàn điện, 전기용접)이라는 구어체 표현도 자주 사용되므로 문맥에 따라 구분이 필요합니다.",
        "meaningVi": "Phương pháp hàn sử dụng nhiệt độ cao của hồ quang điện để nấu chảy kim loại và nối chúng lại. Là phương pháp hàn phổ biến nhất trong công trường xây dựng, yêu cầu trang bị bảo hộ đầy đủ và đào tạo an toàn về nguy cơ điện giật.",
        "context": "철골 구조물 용접, 배관 연결, 철근 이음",
        "culturalNote": "한국 건설 현장에서는 아크용접을 '전기용접'이라고 통칭하는 경우가 많으나, 베트남에서는 'hàn hồ quang'(정식 명칭)과 'hàn điện'(구어체)을 구분하여 사용합니다. 또한 한국은 용접사 자격증이 세분화되어 있지만(특수용접, 보통용접 등), 베트남은 'thợ hàn'(용접공)으로 통칭되는 경우가 많아 자격 요건 설명 시 주의가 필요합니다. 안전 규정도 양국 간 차이가 있어, 한국 기준의 '용접 화재 예방 조치'를 설명할 때는 베트남 현지 안전 기준과 비교 설명이 필수입니다.",
        "commonMistakes": [
            {
                "mistake": "아크용접을 'hàn điện'으로만 번역",
                "correction": "정식 명칭 'hàn hồ quang' 사용 또는 병기",
                "explanation": "'hàn điện'은 구어체이며 기술 문서나 계약서에서는 'hàn hồ quang'이 정확한 표현입니다."
            },
            {
                "mistake": "용접을 'nối'(접합)으로 통역",
                "correction": "'hàn'(용접) 사용",
                "explanation": "'nối'는 일반적인 연결/접합이고, 'hàn'은 열을 가해 금속을 융합하는 용접을 의미합니다."
            },
            {
                "mistake": "용접사를 'người hàn'으로 표현",
                "correction": "'thợ hàn' 또는 'công nhân hàn' 사용",
                "explanation": "베트남 현장에서는 'thợ hàn'이 표준 호칭이며, 'người hàn'은 부자연스러운 표현입니다."
            }
        ],
        "examples": [
            {
                "ko": "내일 오전 철골 기둥 아크용접 작업이 예정되어 있으니 용접사 3명 배치 부탁드립니다.",
                "vi": "Sáng mai có lịch hàn hồ quang cột thép, vui lòng bố trí 3 thợ hàn.",
                "situation": "onsite"
            },
            {
                "ko": "아크용접 시 보안경과 용접 장갑 착용은 필수입니다.",
                "vi": "Khi hàn hồ quang, bắt buộc phải đeo kính bảo hộ và găng tay hàn.",
                "situation": "formal"
            },
            {
                "ko": "이 부위는 아크용접으로 처리하면 됩니다. 가스용접은 필요 없어요.",
                "vi": "Vị trí này dùng hàn hồ quang là được. Không cần hàn khí.",
                "situation": "onsite"
            }
        ],
        "relatedTerms": ["가스용접", "용접봉", "용접결함", "비드"]
    },
    {
        "slug": "han-khi",
        "korean": "가스용접",
        "vietnamese": "Hàn khí",
        "hanja": "gas鎔接",
        "hanjaReading": "gas(외래어) + 鎔(녹을 용) + 接(이을 접)",
        "pronunciation": "한 키",
        "meaningKo": "산소와 아세틸렌 등의 가연성 가스를 혼합 연소시켜 발생하는 고온의 불꽃으로 금속을 용융시켜 접합하는 방법입니다. 통역 시 '가스'는 베트남어로 'khí'(키)이며, '산소 아세틸렌 용접'은 'hàn khí oxy-axetylen'으로 표현됩니다. 아크용접보다 열 집중도가 낮아 얇은 판재나 비철금속 용접에 적합하며, 현장에서는 절단 작업(cắt khí)과 혼동하지 않도록 주의해야 합니다. 한국 현장에서는 '가스 토치'라고 부르지만 베트nam에서는 'đèn hàn khí' 또는 'mỏ hàn'으로 표현합니다.",
        "meaningVi": "Phương pháp hàn sử dụng ngọn lửa nhiệt độ cao từ việc đốt cháy hỗn hợp khí oxy và khí axetylen để nấu chảy kim loại. Thích hợp cho tấm mỏng và kim loại màu, có nhiệt độ tập trung thấp hơn hàn hồ quang.",
        "context": "배관 용접, 알루미늄 판재 접합, 수리 용접",
        "culturalNote": "한국에서는 가스용접을 '가스 불'이라는 구어체로 부르는 경우가 많으나, 베트남에서는 'hàn khí'와 'cắt khí'(가스절단)를 엄격히 구분합니다. 또한 한국은 산업안전보건법상 가스용접 작업 시 '화기 작업 허가증'이 필수이지만, 베트남은 'giấy phép an toàn lao động'(노동안전허가증)로 별도 관리되므로 통역 시 행정 절차 차이를 명확히 설명해야 합니다. 가스통 색상 규정도 한국(산소-녹색, 아세틸렌-주황)과 베트남(산소-파랑, 아세틸렌-빨강)이 달라 안전 교육 시 혼란 방지가 필요합니다.",
        "commonMistakes": [
            {
                "mistake": "가스용접을 'hàn ga'로 표현",
                "correction": "'hàn khí' 사용",
                "explanation": "'ga'는 외래어 차용이며, 'khí'가 표준 베트남어 표현입니다."
            },
            {
                "mistake": "가스용접과 가스절단을 구분하지 않고 'hàn'으로만 통역",
                "correction": "용접은 'hàn khí', 절단은 'cắt khí'로 명확히 구분",
                "explanation": "작업 방법과 안전 조치가 다르므로 정확한 구분이 필수입니다."
            },
            {
                "mistake": "토치를 'đèn'으로만 번역",
                "correction": "'mỏ hàn' 또는 'đèn hàn khí' 사용",
                "explanation": "'đèn'만으로는 조명 기구로 오해될 수 있습니다."
            }
        ],
        "examples": [
            {
                "ko": "이 배관은 가스용접으로 연결하면 됩니다. 아크는 너무 강해요.",
                "vi": "Ống này dùng hàn khí nối là được. Hàn hồ quang quá mạnh.",
                "situation": "onsite"
            },
            {
                "ko": "가스용접 작업 전 화기 작업 허가증을 반드시 받아야 합니다.",
                "vi": "Trước khi hàn khí, bắt buộc phải có giấy phép làm việc có lửa.",
                "situation": "formal"
            },
            {
                "ko": "산소통과 아세틸렌통을 3미터 이상 떨어뜨려 보관하세요.",
                "vi": "Bảo quản bình oxy và bình axetylen cách nhau trên 3 mét.",
                "situation": "onsite"
            }
        ],
        "relatedTerms": ["아크용접", "용접봉", "절단", "토치"]
    },
    {
        "slug": "han-mat-dai",
        "korean": "맞대기용접",
        "vietnamese": "Hàn giáp mối",
        "hanja": None,
        "hanjaReading": None,
        "pronunciation": "한 잡 머이",
        "meaningKo": "두 부재를 같은 평면상에서 맞대어 접합하는 용접 방법으로, 구조적으로 가장 강한 이음 형태입니다. 통역 시 '맞대기'는 'giáp mối'(잡 머이)로 표현되며, '겹치기용접'(hàn chồng)과 명확히 구분해야 합니다. 건설 현장에서 철골 기둥, 보, 배관 등의 주요 구조 접합에 사용되며, 완전 용입(full penetration)이 요구되는 경우가 많아 통역 시 'hàn thấm hoàn toàn'(완전 용입 용접)으로 추가 설명이 필요합니다. 품질 검사에서 UT(초음파 탐상)나 RT(방사선 투과) 검사가 필수인 경우가 많습니다.",
        "meaningVi": "Phương pháp hàn nối hai chi tiết ở cùng mặt phẳng, tạo mối hàn mạnh nhất về mặt kết cấu. Thường yêu cầu hàn thấm hoàn toàn và kiểm tra UT hoặc RT để đảm bảo chất lượng.",
        "context": "철골 구조물 접합, 압력 배관 연결, 탱크 제작",
        "culturalNote": "한국 건설 현장에서는 맞대기용접을 '버트 용접'(Butt welding)이라는 영어 표현으로 부르는 경우도 많으나, 베트남에서는 'hàn giáp mối'가 표준이며 'hàn butt'는 거의 사용되지 않습니다. 또한 한국은 용접 검사 기준이 KS B 0845(용접부 검사 기준) 등으로 세분화되어 있지만, 베트남은 TCVN(베트남 국가 표준) 기준을 따르므로, 검사 합격 기준을 통역할 때 양국 기준의 차이를 명확히 설명해야 합니다. 특히 '용입 깊이' 요구사항이 도면에 표기되어 있을 경우, 베트남 용접사에게 'độ sâu thấm'으로 정확히 전달하지 않으면 재작업이 발생할 수 있습니다.",
        "commonMistakes": [
            {
                "mistake": "맞대기용접을 'hàn nối'로만 표현",
                "correction": "'hàn giáp mối' 사용",
                "explanation": "'hàn nối'는 일반적인 연결 용접이고, 'hàn giáp mối'는 특정 형태의 맞대기 이음을 의미합니다."
            },
            {
                "mistake": "완전 용입을 'hàn đầy'로 통역",
                "correction": "'hàn thấm hoàn toàn' 사용",
                "explanation": "'hàn đầy'는 '가득 채운 용접'으로 오해될 수 있으며, 용입(thấm) 개념이 빠져 있습니다."
            },
            {
                "mistake": "맞대기와 겹치기를 구분하지 않고 모두 'hàn nối'로 통역",
                "correction": "맞대기는 'giáp mối', 겹치기는 'chồng'으로 구분",
                "explanation": "구조적 강도와 용접 방법이 다르므로 명확한 구분이 필수입니다."
            }
        ],
        "examples": [
            {
                "ko": "이 철골 기둥은 맞대기용접으로 연결하고, UT 검사 100% 실시합니다.",
                "vi": "Cột thép này nối bằng hàn giáp mối và kiểm tra UT 100%.",
                "situation": "formal"
            },
            {
                "ko": "맞대기용접 부위는 완전 용입이 필요하니까 뒷면도 잘 처리해야 합니다.",
                "vi": "Vị trí hàn giáp mối cần hàn thấm hoàn toàn nên phải xử lý tốt cả mặt sau.",
                "situation": "onsite"
            },
            {
                "ko": "배관 맞대기용접 전에 개선 가공은 완료됐나요?",
                "vi": "Đã gia công vát mép ống trước khi hàn giáp mối chưa?",
                "situation": "onsite"
            }
        ],
        "relatedTerms": ["필렛용접", "용접결함", "UT검사", "용입"]
    },
    {
        "slug": "han-fillet",
        "korean": "필렛용접",
        "vietnamese": "Hàn góc",
        "hanja": "fillet鎔接",
        "hanjaReading": "fillet(외래어) + 鎔(녹을 용) + 接(이을 접)",
        "pronunciation": "한 곡",
        "meaningKo": "두 부재가 직각 또는 경사지게 교차하는 모서리 부분을 삼각형 단면으로 용접하는 방법입니다. 통역 시 'fillet'은 베트남어로 'góc'(모서리, 각도)으로 표현되며, 'hàn góc'이 표준 번역입니다. 맞대기용접보다 시공이 간단하고 개선 가공이 불필요하여 건설 현장에서 가장 많이 사용되는 용접 형태입니다. 용접 크기(다리 길이, chân hàn)는 도면에 숫자로 표기되며(예: 6mm 필렛 → hàn góc chân 6mm), 통역 시 이 수치를 정확히 전달하지 않으면 구조 안전성에 문제가 발생할 수 있습니다. 주의할 점은 한국에서 '각 용접'이라고 부르는 경우도 있으나, 베트남에서는 'hàn góc'만 사용됩니다.",
        "meaningVi": "Phương pháp hàn các chi tiết giao nhau vuông góc hoặc xiên góc, tạo mặt cắt hình tam giác. Dễ thi công hơn hàn giáp mối vì không cần gia công vát mép, là loại hàn phổ biến nhất trong công trường xây dựng.",
        "context": "브라켓 용접, T형 접합, 보-기둥 연결",
        "culturalNote": "한국 건설 도면에서는 필렛용접을 삼각형 기호로 표시하고 다리 길이를 mm 단위로 표기하는데, 베트남 도면도 동일한 방식을 따르지만 'chân hàn'(용접 다리)이라는 용어를 사용합니다. 한국 용접사는 '6파이 필렛'처럼 지름(Ø) 표현을 쓰기도 하나, 베트남에서는 'chân 6'(다리 6mm)으로 표현하는 것이 일반적입니다. 또한 한국은 KS 규격에서 필렛용접의 목 두께(throat thickness)를 강조하지만, 베트남 현장에서는 'chiều cao mối hàn'(용접 높이)로 표현되는 경우가 많아 도면 검토 시 용어 통일이 필요합니다. 품질 검사는 육안 검사(VT)가 주로 사용되며, 'kiểm tra ngoại quan'으로 통역됩니다.",
        "commonMistakes": [
            {
                "mistake": "필렛용접을 'hàn tam giác'(삼각형 용접)으로 표현",
                "correction": "'hàn góc' 사용",
                "explanation": "'hàn tam giác'은 베트남 현장에서 사용되지 않는 표현입니다."
            },
            {
                "mistake": "용접 다리 길이를 'chiều dài'로 통역",
                "correction": "'chân hàn' 또는 'chân mối hàn' 사용",
                "explanation": "'chân hàn'은 필렛용접의 표준 측정 용어입니다."
            },
            {
                "mistake": "각 용접과 필렛용접을 다른 것으로 설명",
                "correction": "같은 용접 방법임을 명확히 하고 'hàn góc' 사용",
                "explanation": "한국에서 '각 용접'과 '필렛용접'은 같은 의미이며, 베트남어로는 모두 'hàn góc'입니다."
            }
        ],
        "examples": [
            {
                "ko": "이 브라켓은 6mm 필렛용접으로 전둘레 용접해 주세요.",
                "vi": "Khung đỡ này hàn góc chân 6mm, hàn toàn bộ chu vi.",
                "situation": "onsite"
            },
            {
                "ko": "필렛용접은 개선 가공이 필요 없어서 작업이 빠릅니다.",
                "vi": "Hàn góc không cần gia công vát mép nên làm nhanh.",
                "situation": "informal"
            },
            {
                "ko": "필렛 크기가 도면에 8로 표기되어 있으니 8mm로 시공하세요.",
                "vi": "Kích thước hàn góc trên bản vẽ ghi 8, thi công chân 8mm.",
                "situation": "onsite"
            }
        ],
        "relatedTerms": ["맞대기용접", "비드", "용접결함", "목 두께"]
    },
    {
        "slug": "khuyet-tat-han",
        "korean": "용접결함",
        "vietnamese": "Khuyết tật hàn",
        "hanja": "鎔接缺陷",
        "hanjaReading": "鎔(녹을 용) + 接(이을 접) + 缺(이지러질 결) + 陷(빠질 함)",
        "pronunciation": "쿠엣 땃 한",
        "meaningKo": "용접부에 발생하는 균열, 기공, 슬래그 혼입, 용입 부족 등의 불량 현상을 총칭하는 용어입니다. 통역 시 '결함'은 베트남어로 'khuyết tật'(쿠엣 땃)이며, 구체적인 결함 유형별로 정확한 베트남어 표현을 사용해야 합니다. 대표적인 결함으로는 균열(vết nứt), 기공(lỗ khí), 슬래그 혼입(xỉ lẫn), 융합 부족(thiếu dung hợp), 용입 부족(thiếu thấm) 등이 있으며, 각 결함은 발생 원인과 보수 방법이 다르므로 통역 시 세부 구분이 필수입니다. 한국 현장에서는 '용접 불량'이라는 포괄적 표현을 쓰지만, 베트남에서는 결함 유형을 명확히 지적해야 재작업 지시가 정확히 전달됩니다.",
        "meaningVi": "Tổng hợp các hiện tượng lỗi như vết nứt, lỗ khí, xỉ lẫn, thiếu thấm xảy ra ở mối hàn. Mỗi loại khuyết tật có nguyên nhân và phương pháp sửa chữa khác nhau, cần phân loại rõ ràng.",
        "context": "품질 검사, 재작업 지시, 안전 진단",
        "culturalNote": "한국 건설 현장에서는 용접 결함을 발견하면 '재용접' 또는 '보수 용접'을 지시하는데, 베트남에서는 'hàn lại'(재용접)와 'hàn sửa chữa'(보수 용접)를 구분하여 사용합니다. 또한 한국은 용접 결함 판정 기준이 KS B 0845 등으로 명확히 규정되어 있지만, 베트남은 TCVN 기준이나 프로젝트별 시방서를 따르는 경우가 많아, 합격/불합격 기준을 통역할 때 적용 기준을 명확히 해야 혼란을 방지할 수 있습니다. 특히 '크랙'(균열)은 구조 안전에 치명적이므로, 발견 시 즉시 'vết nứt nghiêm trọng'(심각한 균열)로 강조하여 전달해야 합니다. 베트남 용접사 중 일부는 경미한 기공을 무시하는 경향이 있어, 한국 기준의 엄격함을 교육할 필요가 있습니다.",
        "commonMistakes": [
            {
                "mistake": "모든 결함을 'lỗi hàn'으로만 통역",
                "correction": "결함 유형에 따라 'vết nứt', 'lỗ khí', 'xỉ lẫn' 등으로 구분",
                "explanation": "결함 유형마다 원인과 보수 방법이 다르므로 정확한 구분이 필수입니다."
            },
            {
                "mistake": "기공을 'lỗ rỗng'으로 표현",
                "correction": "'lỗ khí' 사용",
                "explanation": "'lỗ rỗng'은 일반적인 공간이고, 'lỗ khí'는 가스 기공을 의미하는 전문 용어입니다."
            },
            {
                "mistake": "재용접과 보수 용접을 구분하지 않고 'hàn lại'로만 통역",
                "correction": "전체 재시공은 'hàn lại', 부분 보수는 'hàn sửa chữa'로 구분",
                "explanation": "작업 범위와 비용이 다르므로 명확한 구분이 필요합니다."
            }
        ],
        "examples": [
            {
                "ko": "UT 검사 결과 내부에 기공이 발견되어 재용접이 필요합니다.",
                "vi": "Kết quả kiểm tra UT phát hiện lỗ khí bên trong, cần hàn lại.",
                "situation": "formal"
            },
            {
                "ko": "이 용접부에 균열이 있어요. 즉시 보수해야 합니다.",
                "vi": "Mối hàn này có vết nứt. Phải sửa chữa ngay.",
                "situation": "onsite"
            },
            {
                "ko": "슬래그 제거가 불완전해서 슬래그 혼입 결함이 자주 발생하네요.",
                "vi": "Làm sạch xỉ chưa kỹ nên thường xảy ra khuyết tật xỉ lẫn.",
                "situation": "onsite"
            }
        ],
        "relatedTerms": ["UT검사", "비드", "재용접", "균열"]
    },
    {
        "slug": "duong-ran-han",
        "korean": "비드",
        "vietnamese": "Đường rãnh hàn",
        "hanja": "bead",
        "hanjaReading": "bead(외래어, 구슬)",
        "pronunciation": "드엉 잔 한",
        "meaningKo": "용접봉이나 와이어가 녹아서 모재 위에 쌓인 한 줄의 용착 금속을 의미하며, 용접의 가장 기본 단위입니다. 통역 시 '비드'는 베트남어로 'đường rãnh hàn'(드엉 잔 한, 용접 홈선) 또는 간단히 'mối hàn'(용접선)으로 표현됩니다. 한 번의 용접 패스(pass)로 형성되는 용착 금속 한 줄을 지칭하며, 두꺼운 부재는 여러 층(nhiều lớp)의 비드를 쌓아 올려야 합니다. 비드 외관(ngoại quan đường hàn)은 용접 품질의 1차 지표로, '고른 비드'(đường hàn đều)는 숙련된 용접사의 증거이며, 불규칙한 비드는 재작업 대상이 될 수 있습니다. 한국 현장에서는 '비드 폭', '비드 높이'로 표현하지만 베트남에서는 'bề rộng mối hàn', 'chiều cao mối hàn'으로 통역해야 합니다.",
        "meaningVi": "Kim loại hàn được nạp lên bề mặt kim loại cơ bản theo một đường, là đơn vị cơ bản của mối hàn. Với chi tiết dày, cần nhiều lớp đường hàn chồng lên nhau.",
        "context": "용접 품질 평가, 다층 용접 지시, 외관 검사",
        "culturalNote": "한국 건설 현장에서는 '비드'라는 영어 표현을 그대로 사용하는 경우가 많지만, 베트남에서는 'đường rãnh hàn' 또는 'mối hàn'으로 순화하여 사용합니다. 특히 '위빙 비드'(weaving bead, 지그재그로 용접봉을 움직여 만드는 넓은 비드)는 베트남어로 'đường hàn dệt' 또는 'hàn dao động'으로 표현되며, 직선 비드('đường hàn thẳng')와 구분됩니다. 한국 용접 교육에서는 비드 외관의 미관을 강조하는 반면, 베트남 일부 현장에서는 기능적 강도만 중시하는 경향이 있어, 한국 품질 기준을 통역할 때 외관 품질의 중요성을 함께 설명해야 합니다. 또한 '초층 비드'(lớp đầu tiên), '마무리 비드'(lớp hoàn thiện) 등 용접 순서별 용어도 정확히 구분하여 통역해야 합니다.",
        "commonMistakes": [
            {
                "mistake": "비드를 'hạt'(구슬)로 직역",
                "correction": "'đường rãnh hàn' 또는 'mối hàn' 사용",
                "explanation": "'hạt'는 용접 용어로 사용되지 않으며, 'đường rãnh hàn'이 표준 표현입니다."
            },
            {
                "mistake": "다층 용접을 'hàn nhiều lần'(여러 번 용접)으로 표현",
                "correction": "'hàn nhiều lớp' 사용",
                "explanation": "'nhiều lần'은 단순 횟수이고, 'nhiều lớp'은 층을 쌓는다는 기술적 의미를 포함합니다."
            },
            {
                "mistake": "비드 외관을 'hình dáng'(형태)로 통역",
                "correction": "'ngoại quan đường hàn' 또는 'bề mặt mối hàn' 사용",
                "explanation": "용접 검사의 전문 용어이므로 정확한 표현이 필요합니다."
            }
        ],
        "examples": [
            {
                "ko": "초층 비드를 깔끔하게 깔아야 다음 층 작업이 쉬워집니다.",
                "vi": "Lớp đường hàn đầu tiên phải gọn gàng thì lớp sau mới dễ làm.",
                "situation": "onsite"
            },
            {
                "ko": "이 부위는 3층 비드로 쌓아 올리세요. 한 번에 너무 두껍게 하지 마세요.",
                "vi": "Vị trí này hàn 3 lớp. Đừng làm một lần quá dày.",
                "situation": "onsite"
            },
            {
                "ko": "비드 외관이 불균일하니 슬래그 제거 후 다시 확인하겠습니다.",
                "vi": "Bề mặt mối hàn không đều, sau khi làm sạch xỉ sẽ kiểm tra lại.",
                "situation": "formal"
            }
        ],
        "relatedTerms": ["용접봉", "슬래그", "다층용접", "용접결함"]
    },
    {
        "slug": "xi-han",
        "korean": "슬래그",
        "vietnamese": "Xỉ hàn",
        "hanja": "slag",
        "hanjaReading": "slag(외래어, 광재)",
        "pronunciation": "씨 한",
        "meaningKo": "용접 중 용접봉의 피복제나 플럭스가 녹아 생성되는 비금속 불순물로, 용접 후 표면에 남는 찌꺼기입니다. 통역 시 '슬래그'는 베트남어로 'xỉ hàn'(씨 한, 용접 찌꺼기)으로 표현됩니다. 슬래그는 용접 중 용융 금속을 대기로부터 보호하는 역할을 하지만, 용접 완료 후에는 반드시 제거(làm sạch xỉ)해야 다음 층 용접이나 도장 작업이 가능합니다. 슬래그 제거가 불완전하면 '슬래그 혼입'(xỉ lẫn) 결함이 발생하여 용접 강도가 저하됩니다. 제거 도구로는 슬래그 해머(búa gõ xỉ) 또는 와이어 브러시(bàn chải thép)를 사용하며, 통역 시 안전 장비(kính bảo hộ, 보안경) 착용을 강조해야 합니다.",
        "meaningVi": "Tạp chất phi kim sinh ra từ lớp phủ que hàn hoặc thuốc hàn, tạo thành cặn trên bề mặt sau khi hàn. Cần loại bỏ hoàn toàn trước khi hàn lớp tiếp theo hoặc sơn.",
        "context": "용접 후처리, 품질 관리, 다층 용접",
        "culturalNote": "한국 건설 현장에서는 '슬래그 치기' 또는 '슬래그 따기'라는 구어체 표현을 사용하지만, 베트남에서는 'làm sạch xỉ'(슬래그 청소) 또는 'gõ xỉ'(슬래그 두드리기)로 표현됩니다. 한국 용접사는 슬래그 제거를 당연한 후속 작업으로 인식하지만, 베트남 일부 현장에서는 이를 생략하거나 대충 하는 경우가 있어, 다층 용접 시 '각 층마다 완전히 제거'(làm sạch hoàn toàn sau mỗi lớp)를 강조해야 합니다. 슬래그 제거 시 비산물이 눈에 들어갈 위험이 있어, 한국은 보안경 착용을 의무화하지만 베트남 현장에서는 이를 간과하는 경우가 많으므로 안전 교육 시 'bắt buộc đeo kính bảo hộ'를 반복 강조해야 합니다.",
        "commonMistakes": [
            {
                "mistake": "슬래그를 'cặn bẩn'(더러운 찌꺼기)으로 표현",
                "correction": "'xỉ hàn' 사용",
                "explanation": "'xỉ hàn'은 용접 전문 용어이며, 'cặn bẩn'은 일반적인 오염물을 의미합니다."
            },
            {
                "mistake": "슬래그 제거를 'làm vệ sinh'(청소)으로만 표현",
                "correction": "'làm sạch xỉ' 또는 'gõ xỉ' 사용",
                "explanation": "용접 후처리의 구체적인 작업 내용을 명확히 전달해야 합니다."
            },
            {
                "mistake": "슬래그 혼입을 단순히 'xỉ bị lẫn'으로 통역",
                "correction": "'khuyết tật xỉ lẫn' 또는 'lỗi xỉ lẫn vào mối hàn' 사용",
                "explanation": "용접 결함의 일종임을 명확히 하는 표현이 필요합니다."
            }
        ],
        "examples": [
            {
                "ko": "각 층 용접 후 슬래그를 완전히 제거하고 다음 층을 시공하세요.",
                "vi": "Sau mỗi lớp hàn, làm sạch hoàn toàn xỉ rồi mới hàn lớp tiếp.",
                "situation": "onsite"
            },
            {
                "ko": "슬래그 제거 시 보안경 착용은 필수입니다. 눈에 들어가면 위험해요.",
                "vi": "Khi làm sạch xỉ bắt buộc đeo kính bảo hộ. Văng vào mắt rất nguy hiểm.",
                "situation": "onsite"
            },
            {
                "ko": "슬래그 해머로 두드려서 제거한 후 와이어 브러시로 마무리하세요.",
                "vi": "Dùng búa gõ xỉ gõ sạch rồi dùng bàn chải thép hoàn thiện.",
                "situation": "onsite"
            }
        ],
        "relatedTerms": ["용접봉", "비드", "용접결함", "와이어브러시"]
    },
    {
        "slug": "que-han",
        "korean": "용접봉",
        "vietnamese": "Que hàn",
        "hanja": "鎔接棒",
        "hanjaReading": "鎔(녹을 용) + 接(이을 접) + 棒(막대기 봉)",
        "pronunciation": "꿰 한",
        "meaningKo": "아크용접에 사용되는 심선에 피복제를 입힌 소모성 전극으로, 용접의 핵심 재료입니다. 통역 시 '용접봉'은 베트남어로 'que hàn'(꿰 한)이며, 종류에 따라 'que hàn thường'(일반 용접봉), 'que hàn đặc biệt'(특수 용접봉)로 구분됩니다. 용접봉은 규격(지름)과 재질에 따라 분류되며, 한국에서 'E4316'처럼 표기되는 용접봉 규격은 베트남에서도 동일하게 사용되지만, 통역 시 'que hàn E4316'으로 정확히 전달해야 합니다. 용접봉 보관은 습기를 피해야 하며(tránh ẩm), 건조로(lò sấy que hàn)에 보관하는 것이 원칙입니다. 사용 전 건조 여부를 확인하지 않으면 기공 결함이 발생할 수 있어, 통역 시 'kiểm tra độ khô'(건조도 확인)를 강조해야 합니다.",
        "meaningVi": "Que điện cực tiêu hao có lớp phủ, sử dụng trong hàn hồ quang, là vật liệu chính của mối hàn. Cần bảo quản tránh ẩm và sấy khô trước khi sử dụng để tránh lỗi lỗ khí.",
        "context": "용접 재료 관리, 용접 작업 지시, 품질 관리",
        "culturalNote": "한국 건설 현장에서는 용접봉을 '봉'이라고 줄여 부르는 경우가 많지만, 베트남에서는 'que'(막대기)로 표현되며 'que hàn'이 정식 명칭입니다. 용접봉 규격은 한국과 베트남 모두 AWS(미국용접협회) 또는 JIS(일본공업규격) 기준을 따르므로 'E4316', 'E7016' 같은 표기는 동일하게 사용되지만, 통역 시 '이포삼일육'처럼 숫자를 읽지 말고 'E bốn ba một sáu'로 정확히 읽어야 합니다. 한국은 용접봉 보관을 엄격히 관리하여 건조로(80~150°C)에 보관하지만, 베트남 일부 현장에서는 상온 보관하는 경우가 있어, 습기 흡수로 인한 품질 저하를 방지하기 위해 'bảo quản que hàn trong lò sấy'를 강조해야 합니다.",
        "commonMistakes": [
            {
                "mistake": "용접봉을 'que sắt'(쇠막대)로 표현",
                "correction": "'que hàn' 사용",
                "explanation": "'que sắt'는 일반 철 막대이고, 'que hàn'은 용접 전용 전극입니다."
            },
            {
                "mistake": "용접봉 규격을 '이포삼일육'으로 읽고 베트남어로 숫자만 통역",
                "correction": "'E bốn ba một sáu' 또는 'que hàn E4316'으로 정확히 표기",
                "explanation": "규격 표기는 국제 표준이므로 알파벳과 숫자를 명확히 구분하여 전달해야 합니다."
            },
            {
                "mistake": "건조로를 'lò nướng'(오븐)으로 통역",
                "correction": "'lò sấy que hàn' 사용",
                "explanation": "'lò nướng'은 음식 조리용이고, 'lò sấy'는 산업용 건조 설비입니다."
            }
        ],
        "examples": [
            {
                "ko": "오늘 사용할 용접봉은 E4316, 지름 3.2mm로 준비해 주세요.",
                "vi": "Que hàn dùng hôm nay là E4316, đường kính 3.2mm, chuẩn bị giúp.",
                "situation": "onsite"
            },
            {
                "ko": "용접봉을 비에 맞으면 안 돼요. 건조로에 보관하세요.",
                "vi": "Que hàn không được để mưa. Bảo quản trong lò sấy.",
                "situation": "onsite"
            },
            {
                "ko": "이 용접봉은 습기를 먹어서 못 쓸 것 같습니다. 새 것으로 교체하세요.",
                "vi": "Que hàn này bị ẩm, không dùng được. Thay que mới.",
                "situation": "onsite"
            }
        ],
        "relatedTerms": ["아크용접", "슬래그", "비드", "건조로"]
    },
    {
        "slug": "un-nong-truoc",
        "korean": "예열",
        "vietnamese": "Ủn nóng trước",
        "hanja": "豫熱",
        "hanjaReading": "豫(미리 예) + 熱(더울 열)",
        "pronunciation": "운 농 쯔억",
        "meaningKo": "용접 전에 모재를 일정 온도까지 가열하여 급격한 온도 변화를 방지하고 용접 품질을 확보하는 전처리 작업입니다. 통역 시 '예열'은 베트남어로 'ủn nóng trước'(운 농 쯔억, 사전 가열) 또는 'làm nóng trước'로 표현됩니다. 예열은 특히 두꺼운 부재나 저온 환경에서 필수이며, 예열 온도(nhiệt độ ủn nóng)는 재질과 두께에 따라 달라집니다. 한국 시방서에서 '100~150°C로 예열'이라고 명시되면, 베트남어로 'ủn nóng đến 100~150°C'로 통역하고, 온도 측정은 적외선 온도계(súng đo nhiệt độ) 또는 온도 크레용(bút sáp đo nhiệt)을 사용합니다. 예열 미실시 시 균열(vết nứt) 발생 위험이 높아지므로, 통역 시 이 점을 강조해야 합니다.",
        "meaningVi": "Công việc làm nóng trước kim loại cơ bản đến nhiệt độ nhất định trước khi hàn, để tránh thay đổi nhiệt độ đột ngột và đảm bảo chất lượng hàn. Đặc biệt cần thiết với chi tiết dày hoặc môi trường nhiệt độ thấp.",
        "context": "두께 25mm 이상 부재 용접, 겨울철 용접, 고강도 강재",
        "culturalNote": "한국 건설 현장에서는 예열을 '프리히팅'(preheating)이라는 영어 표현으로 부르는 경우도 많지만, 베트남에서는 'ủn nóng trước'가 표준이며 영어 차용어는 거의 사용되지 않습니다. 한국은 KS 규격에서 강재 두께와 탄소 당량에 따라 예열 온도를 세분화하여 규정하지만, 베트남 현장에서는 이를 간과하고 예열 없이 용접하는 경우가 있어, 특히 겨울철이나 두꺼운 부재 작업 시 예열의 중요성을 반복 강조해야 합니다. 예열 방법으로는 가스 토치(đèn khí), 전기 히터(máy sưởi điện), 유도 가열(gia nhiệt cảm ứng) 등이 있으며, 통역 시 사용 장비를 명확히 지정해야 합니다. 예열 온도 유지 시간도 중요하므로, 'giữ nhiệt trong 5 phút'(5분간 온도 유지)처럼 구체적으로 전달해야 합니다.",
        "commonMistakes": [
            {
                "mistake": "예열을 'đun nóng'(끓이기)로 표현",
                "correction": "'ủn nóng trước' 또는 'làm nóng trước' 사용",
                "explanation": "'đun nóng'은 물을 끓이는 것이고, 'ủn nóng'은 금속 가열을 의미합니다."
            },
            {
                "mistake": "예열 온도를 'nhiệt độ nóng'으로만 표현",
                "correction": "'nhiệt độ ủn nóng' 또는 구체적 수치 포함",
                "explanation": "예열은 정확한 온도 관리가 필수이므로 수치를 함께 전달해야 합니다."
            },
            {
                "mistake": "예열을 선택 사항으로 통역",
                "correction": "시방서에 명시된 경우 '필수'(bắt buộc)임을 강조",
                "explanation": "예열은 구조 안전과 직결되므로 의무 사항임을 명확히 해야 합니다."
            }
        ],
        "examples": [
            {
                "ko": "이 부재는 두께가 30mm이니까 용접 전에 100도로 예열해야 합니다.",
                "vi": "Chi tiết này dày 30mm nên trước khi hàn phải ủn nóng đến 100 độ.",
                "situation": "formal"
            },
            {
                "ko": "날씨가 추우니 예열을 꼭 하고 용접 시작하세요.",
                "vi": "Trời lạnh nên nhất định phải ủn nóng trước rồi mới bắt đầu hàn.",
                "situation": "onsite"
            },
            {
                "ko": "예열 온도를 적외선 온도계로 확인한 후 용접하세요.",
                "vi": "Kiểm tra nhiệt độ ủn nóng bằng súng đo nhiệt rồi mới hàn.",
                "situation": "onsite"
            }
        ],
        "relatedTerms": ["용접결함", "균열", "후열처리", "온도측정"]
    },
    {
        "slug": "kiem-tra-ut",
        "korean": "UT검사",
        "vietnamese": "Kiểm tra UT",
        "hanja": "UT檢査",
        "hanjaReading": "UT(Ultrasonic Testing, 초음파 탐상) + 檢(조사할 검) + 査(조사할 사)",
        "pronunciation": "끼엠 짜 유 떼",
        "meaningKo": "초음파를 이용하여 용접부 내부의 결함(균열, 기공, 슬래그 혼입 등)을 비파괴적으로 검사하는 방법입니다. 통역 시 'UT검사'는 베트남어로 'kiểm tra UT' 또는 풀어서 'kiểm tra siêu âm'(끼엠 짜 시에우 암, 초음파 검사)으로 표현됩니다. UT검사는 맞대기용접의 내부 품질을 확인하는 가장 보편적인 비파괴 검사 방법으로, 검사 결과는 합격(đạt) 또는 불합격(không đạt)으로 판정되며, 불합격 시 재용접(hàn lại) 또는 보수(sửa chữa)가 필요합니다. 검사원은 자격증(chứng chỉ UT)을 보유해야 하며, 검사 보고서(báo cáo kiểm tra UT)는 공사 기록으로 보관됩니다. 한국 현장에서는 '유티 검사'라고 발음하지만, 베트남에서는 알파벳 그대로 'U-T'로 읽습니다.",
        "meaningVi": "Phương pháp kiểm tra không phá hủy sử dụng sóng siêu âm để phát hiện khuyết tật bên trong mối hàn như vết nứt, lỗ khí, xỉ lẫn. Là phương pháp kiểm tra phổ biến nhất cho hàn giáp mối.",
        "context": "철골 구조물 품질 검사, 압력 용기 검사, 배관 용접 검증",
        "culturalNote": "한국 건설 현장에서는 UT검사를 '초음파 검사'와 혼용하지만, 베트남에서는 'kiểm tra UT'(약어)가 더 보편적으로 사용되며, 공식 문서에서는 'kiểm tra siêu âm'(정식 명칭)을 병기합니다. 한국은 UT검사 비율을 도면에 '%'로 표기(예: UT 100%)하는데, 베트남도 동일하게 'kiểm tra UT 100%'로 표현되지만, 일부 베트남 현장에서는 샘플 검사로 오해하는 경우가 있어 '전수 검사'(kiểm tra toàn bộ)임을 명확히 해야 합니다. 검사 합격 기준도 한국(KS)과 베트남(TCVN) 규격이 다를 수 있으므로, 계약 시 적용 기준을 명시하고 통역해야 혼란을 방지할 수 있습니다. UT검사 장비는 고가이므로, 베트남 현장에서는 전문 검사 업체에 외주를 주는 경우가 많으며, 이를 'thuê kiểm tra UT'(UT검사 용역)이라고 표현합니다.",
        "commonMistakes": [
            {
                "mistake": "UT검사를 'kiểm tra âm thanh'(소리 검사)로 통역",
                "correction": "'kiểm tra UT' 또는 'kiểm tra siêu âm' 사용",
                "explanation": "'âm thanh'은 일반적인 소리이고, 'siêu âm'은 초음파를 의미하는 전문 용어입니다."
            },
            {
                "mistake": "UT 100%를 '100개 검사'로 오역",
                "correction": "'kiểm tra UT 100%' 또는 'kiểm tra toàn bộ mối hàn' 사용",
                "explanation": "100%는 전수 검사를 의미하며, 개수가 아닙니다."
            },
            {
                "mistake": "검사 불합격을 'lỗi'(에러)로만 표현",
                "correction": "'không đạt' 또는 'kết quả không đạt yêu cầu' 사용",
                "explanation": "공식 검사 결과는 '합격/불합격'으로 표현해야 합니다."
            }
        ],
        "examples": [
            {
                "ko": "이 철골 기둥 용접부는 UT검사 100% 실시 예정입니다.",
                "vi": "Mối hàn cột thép này sẽ kiểm tra UT 100%.",
                "situation": "formal"
            },
            {
                "ko": "UT검사 결과 3군데에서 내부 결함이 발견되어 재용접이 필요합니다.",
                "vi": "Kết quả kiểm tra UT phát hiện khuyết tật bên trong ở 3 vị trí, cần hàn lại.",
                "situation": "formal"
            },
            {
                "ko": "UT 검사원 자격증 좀 확인해 보세요.",
                "vi": "Kiểm tra chứng chỉ của người kiểm tra UT.",
                "situation": "onsite"
            }
        ],
        "relatedTerms": ["용접결함", "맞대기용접", "비파괴검사", "RT검사"]
    }
]

# 기존 construction.json 읽기
json_path = os.path.join(
    os.path.dirname(os.path.dirname(__file__)),
    "data",
    "terms",
    "construction.json"
)

with open(json_path, "r", encoding="utf-8") as f:
    existing_data = json.load(f)

# 새 용어 추가
existing_data.extend(data)

# 저장
with open(json_path, "w", encoding="utf-8") as f:
    json.dump(existing_data, f, ensure_ascii=False, indent=2)

print(f"✅ 용접/접합 테마 용어 {len(data)}개 추가 완료")
print(f"📊 총 용어 수: {len(existing_data)}개")
print("\n추가된 용어:")
for term in data:
    print(f"  - {term['korean']} ({term['vietnamese']})")
