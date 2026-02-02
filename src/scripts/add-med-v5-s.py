#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
정형외과/신경과 전문용어 추가 스크립트
Tier S 품질 기준 준수 (90점 이상)
"""

import json
import os

# 파일 경로 설정
file_path = os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', 'data', 'terms', 'medical.json')

# 추가할 용어 데이터
new_terms = [
    {
        "slug": "thoat-vi-dia-dem",
        "korean": "디스크(추간판탈출증)",
        "vietnamese": "Thoát vị đĩa đệm",
        "hanja": "椎間板脫出症",
        "hanjaReading": "椎(등뼈 추) 間(사이 간) 板(널빤지 판) 脫(벗을 탈) 出(날 출) 症(증세 증)",
        "pronunciation": "토앗 비 디아 뎀",
        "meaningKo": "척추뼈 사이의 디스크(추간판)가 튀어나와 신경을 압박하는 질환. 통역 시 주의할 점은 한국에서는 흔히 '디스크'라고 줄여 부르지만, 베트남어로는 정확히 'thoát vị đĩa đệm'으로 표현해야 한다. 환자들이 '허리디스크', '목디스크'라고 말할 때 각각 'thoát vị đĩa đệm thắt lưng', 'thoát vị đĩa đệm cổ'로 구분하여 통역해야 혼동을 피할 수 있다. 베트남 현장에서는 종종 'sai khớp đĩa đệm'이라는 비표준 표현을 쓰기도 하므로 정확한 의학용어 사용을 유도해야 한다.",
        "meaningVi": "Bệnh lý đĩa đệm nằm giữa các đốt sống bị thoát ra ngoài và chèn ép lên dây thần kinh, gây đau và tê. Đây là một trong những bệnh cột sống phổ biến nhất ở người lao động văn phòng và công nhân. Triệu chứng thường gặp là đau lưng, tê chân, yếu cơ. Cần phân biệt với thoái hóa cột sống (thoái hóa đốt sống).",
        "context": "병원 진료실, 물리치료실, 산재보험 청구",
        "culturalNote": "한국에서는 '디스크'라는 약칭이 매우 보편화되어 일반인도 흔히 사용하지만, 베트남에서는 정식 의학용어 'thoát vị đĩa đệm'을 주로 쓴다. 한국은 허리디스크 수술이 매우 흔하고 치료 인프라가 잘 갖춰져 있으나, 베트남은 보존적 치료(물리치료, 약물)를 우선하고 수술은 마지막 수단으로 고려하는 경향이 강하다. 통역 시 한국 의사가 수술을 권할 때 베트남 환자가 심리적 저항감을 보일 수 있으므로, 수술의 필요성과 장점을 충분히 설명하도록 유도해야 한다.",
        "commonMistakes": [
            {
                "mistake": "'đĩa đệm bị trượt'라고 표현",
                "correction": "'thoát vị đĩa đệm'이 정확한 의학용어",
                "explanation": "'trượt'은 '미끄러지다'라는 의미로 의학적으로 부정확하며, 'thoát vị'가 '탈출'의 정확한 표현"
            },
            {
                "mistake": "모든 허리 통증을 '디스크'로 통역",
                "correction": "진단명 확인 후 정확히 구분 (đau lưng 일반 요통 vs thoát vị đĩa đệm)",
                "explanation": "한국인 환자들이 허리만 아파도 '디스크인가요?'라고 묻는 경우가 많은데, 이를 그대로 통역하면 오진 위험"
            },
            {
                "mistake": "'sai khớp đĩa đệm'으로 통역",
                "correction": "'thoát vị đĩa đệm'이 표준 의학용어",
                "explanation": "'sai khớp'은 구어체 표현이며 의료 현장에서는 정확한 용어 사용 필요"
            }
        ],
        "examples": [
            {
                "ko": "MRI 검사 결과 요추 4-5번 사이 디스크 탈출이 확인되었습니다.",
                "vi": "Kết quả MRI cho thấy thoát vị đĩa đệm giữa đốt sống thắt lưng L4-L5.",
                "situation": "formal"
            },
            {
                "ko": "디스크가 심하면 수술이 필요할 수도 있어요.",
                "vi": "Nếu thoát vị đĩa đệm nghiêm trọng thì có thể cần phẫu thuật.",
                "situation": "onsite"
            },
            {
                "ko": "물건 들다가 허리디스크 재발했어요.",
                "vi": "Tôi bị tái phát thoát vị đĩa đệm thắt lưng khi nhấc đồ nặng.",
                "situation": "informal"
            }
        ],
        "relatedTerms": ["척추관협착증", "좌골신경통", "요추신경근병증", "물리치료", "MRI"]
    },
    {
        "slug": "viem-khop",
        "korean": "관절염",
        "vietnamese": "Viêm khớp",
        "hanja": "關節炎",
        "hanjaReading": "關(관계할 관) 節(마디 절) 炎(불꽃 염)",
        "pronunciation": "비엠 컵",
        "meaningKo": "관절에 염증이 생겨 통증, 부종, 운동 제한이 나타나는 질환. 통역 시 반드시 구분해야 할 것은 퇴행성 관절염(viêm khớp thoái hóa)과 류마티스 관절염(viêm khớp dạng thấp)이다. 한국 환자들이 단순히 '관절염'이라고 말할 때, 어떤 종류인지 의사에게 확인하여 정확히 통역해야 한다. 베트남 현장에서는 나이 든 근로자들이 무릎 통증을 호소하며 'đau khớp'라고 표현하는데, 이것이 단순 통증인지 염증성 질환인지 구분이 필요하다. 또한 한국은 관절염 치료에 인공관절 수술을 적극 권하지만, 베트남은 보존적 치료를 먼저 시도하는 문화적 차이가 있다.",
        "meaningVi": "Bệnh lý gây viêm tại khớp, dẫn đến đau, sưng và hạn chế vận động. Có nhiều loại viêm khớp, trong đó phổ biến nhất là viêm khớp thoái hóa (do tuổi tác) và viêm khớp dạng thấp (tự miễn). Bệnh thường gặp ở người lao động nặng, người lớn tuổi và phụ nữ sau mãn kinh. Cần điều trị lâu dài và phục hồi chức năng.",
        "context": "병원 정형외과, 산업재해 보험, 요양원",
        "culturalNote": "한국에서는 50대 이상 인구의 관절염 유병률이 매우 높아 인공관절 수술이 일상화되어 있고, 건강보험 적용으로 비용 부담이 적다. 반면 베트남은 인공관절 수술 비용이 매우 고가이며, 수술 후 재활 인프라도 부족하여 환자들이 수술을 꺼리는 경향이 강하다. 통역 시 한국 의사가 수술을 권할 때, 베트남 환자의 경제적 상황과 문화적 배경을 고려하여 충분한 설명이 이뤄지도록 도와야 한다. 또한 베트남에서는 전통 의학(đông y)에서 viêm khớp 치료에 침술, 부항을 많이 사용하는데, 한국 의사들이 이를 이해하지 못하는 경우가 있어 통역사가 문화적 맥락을 설명할 필요가 있다.",
        "commonMistakes": [
            {
                "mistake": "모든 관절 통증을 'viêm khớp'로 통역",
                "correction": "단순 통증(đau khớp)과 염증성 질환(viêm khớp) 구분 필요",
                "explanation": "'đau khớp'은 증상, 'viêm khớp'은 진단명으로 의학적으로 명확히 구분됨"
            },
            {
                "mistake": "'viêm xương khớp'로 잘못 표현",
                "correction": "'viêm khớp'이 표준 용어",
                "explanation": "'xương'(뼈)을 불필요하게 추가하면 의미가 달라질 수 있음"
            },
            {
                "mistake": "류마티스 관절염을 단순 'viêm khớp'로 통역",
                "correction": "'viêm khớp dạng thấp'로 정확히 구분",
                "explanation": "퇴행성과 류마티스는 원인과 치료법이 전혀 다르므로 반드시 구분"
            }
        ],
        "examples": [
            {
                "ko": "엑스레이 결과 퇴행성 관절염 소견이 보입니다.",
                "vi": "Kết quả X-quang cho thấy dấu hiệu viêm khớp thoái hóa.",
                "situation": "formal"
            },
            {
                "ko": "무릎 관절염 때문에 계단 오르기가 힘드세요?",
                "vi": "Anh bị viêm khớp gối nên khó đi cầu thang phải không?",
                "situation": "onsite"
            },
            {
                "ko": "날씨가 추우면 관절염이 더 아파요.",
                "vi": "Trời lạnh thì viêm khớp đau hơn.",
                "situation": "informal"
            }
        ],
        "relatedTerms": ["류마티스", "퇴행성관절염", "인공관절", "물리치료", "소염진통제"]
    },
    {
        "slug": "ton-thuong-day-chang",
        "korean": "인대손상",
        "vietnamese": "Tổn thương dây chằng",
        "hanja": "靭帶損傷",
        "hanjaReading": "靭(질긴 인) 帶(띠 대) 損(덜 손) 傷(다칠 상)",
        "pronunciation": "똔 투억 자이 쨍",
        "meaningKo": "뼈와 뼈를 연결하는 인대가 늘어나거나 찢어진 상태. 통역 시 주의할 점은 인대손상(dây chằng)과 힘줄손상(gân)을 명확히 구분해야 한다는 것이다. 한국 환자들은 둘을 혼동하여 표현하는 경우가 많다. 스포츠 손상이나 산업재해 현장에서 자주 발생하며, 특히 무릎 전방십자인대(ACL) 손상은 수술이 필요한 중대 손상으로 통역 시 정확한 진단명 전달이 매우 중요하다. 베트남 근로자들은 인대손상을 단순 염좌(bong gân)로 오인하고 방치하다가 만성 불안정성으로 악화되는 경우가 많으므로, 조기 진단과 치료의 중요성을 강조하는 통역이 필요하다.",
        "meaningVi": "Tình trạng dây chằng - sợi mô liên kết giữa các xương - bị giãn hoặc đứt. Thường xảy ra do chấn thương thể thao, tai nạn lao động hoặc ngã. Mức độ nghiêm trọng chia thành 3 cấp: cấp 1 (giãn nhẹ), cấp 2 (đứt một phần), cấp 3 (đứt hoàn toàn cần phẫu thuật). Dây chằng không có mạch máu tốt nên khó lành, cần thời gian phục hồi dài.",
        "context": "응급실, 스포츠의학과, 산업재해 현장",
        "culturalNote": "한국은 스포츠 의학이 발달하여 인대손상 진단과 수술 기술이 매우 앞서 있으며, 특히 프로 운동선수들의 전방십자인대 재건술이 일상화되어 있다. 베트남은 MRI 검사 비용이 비싸고 인대 재건 수술을 할 수 있는 병원이 제한적이어서, 많은 환자들이 보존적 치료에 의존한다. 통역 시 한국 의사가 수술을 권할 때, 베트남 환자의 경제적 상황과 현지 의료 인프라를 고려한 대안(보존적 치료, 재활 운동)도 함께 설명하도록 유도하는 것이 좋다. 또한 베트남 근로자들은 인대손상 후 충분한 회복 없이 일터로 복귀하는 경우가 많아, 재활 기간 준수의 중요성을 강조해야 한다.",
        "commonMistakes": [
            {
                "mistake": "인대(dây chằng)와 힘줄(gân)을 혼동",
                "correction": "인대는 뼈-뼈 연결(dây chằng), 힘줄은 근육-뼈 연결(gân)",
                "explanation": "해부학적으로 전혀 다른 구조물이며 치료법도 다름"
            },
            {
                "mistake": "'bong gân'(염좌)과 'tổn thương dây chằng'을 동일시",
                "correction": "염좌는 경증 손상, 인대손상은 부분/완전 파열 포함하는 넓은 개념",
                "explanation": "심각도 차이가 크므로 정확한 구분 필요"
            },
            {
                "mistake": "'dây thần kinh'(신경)으로 잘못 통역",
                "correction": "'dây chằng'이 인대의 정확한 표현",
                "explanation": "발음이 비슷하지만 완전히 다른 조직으로 의료 오류 유발 가능"
            }
        ],
        "examples": [
            {
                "ko": "MRI 검사 결과 전방십자인대 완전 파열이 확인되었습니다.",
                "vi": "Kết quả MRI xác nhận đứt hoàn toàn dây chằng chéo trước (ACL).",
                "situation": "formal"
            },
            {
                "ko": "발목을 삐끗해서 인대가 늘어났어요.",
                "vi": "Tôi trẹo cổ chân nên dây chằng bị giãn.",
                "situation": "onsite"
            },
            {
                "ko": "인대 수술 후 6개월은 재활 치료가 필요합니다.",
                "vi": "Sau phẫu thuật dây chằng cần phục hồi chức năng trong 6 tháng.",
                "situation": "formal"
            }
        ],
        "relatedTerms": ["전방십자인대", "측부인대", "염좌", "관절경수술", "재활치료"]
    },
    {
        "slug": "ton-thuong-sun-chem",
        "korean": "반월상연골손상",
        "vietnamese": "Tổn thương sụn chêm",
        "hanja": "半月狀軟骨損傷",
        "hanjaReading": "半(반 반) 月(달 월) 狀(모양 상) 軟(부드러울 연) 骨(뼈 골) 損(덜 손) 傷(다칠 상)",
        "pronunciation": "똔 투억 순 쩸",
        "meaningKo": "무릎 관절 내부에 있는 반달 모양의 연골이 찢어지거나 손상된 상태. 통역 시 매우 주의해야 할 점은 한국에서는 흔히 '연골'이라고 줄여 말하는데, 베트남어에서 연골에는 여러 종류(sụn khớp 관절연골, sụn chêm 반월상연골)가 있어 반드시 'sụn chêm'으로 정확히 지칭해야 한다. 한국 환자들이 '무릎 연골이 닳았다'고 표현할 때, 이것이 반월상연골 손상인지 관절연골 마모(thoái hóa sụn khớp)인지 의사에게 확인 후 통역해야 한다. 무릎 손상 중 가장 흔하며, 스포츠 활동이나 쪼그려 앉는 작업이 많은 베트남 근로자들에게 자주 발생한다. 심한 경우 관절경 수술이 필요하다.",
        "meaningVi": "Sụn chêm là miếng sụn hình bán nguyệt nằm giữa xương đùi và xương chày, có vai trò đệm và ổn định khớp gối. Khi bị tổn thương, người bệnh cảm thấy đau, khớp kêu lục cục, khó duỗi thẳng chân. Thường xảy ra khi xoay đùi đột ngột trong khi chân đang chịu lực, phổ biến ở vận động viên và công nhân. Nếu không điều trị, có thể dẫn đến viêm khớp sớm.",
        "context": "정형외과, 스포츠의학과, 산업재해 현장",
        "culturalNote": "한국은 무릎 관절경 수술 기술이 매우 발달하여 반월상연골 손상 시 적극적으로 수술을 권하며, 당일 퇴원도 가능할 정도로 간단한 시술로 여겨진다. 그러나 베트남은 관절경 수술을 할 수 있는 병원이 대도시에만 있고 비용도 상당하여, 많은 환자들이 진통제와 물리치료로 버티다가 증상이 악화되는 경우가 많다. 통역 시 한국 의사가 '간단한 수술'이라고 설명해도, 베트남 환자에게는 경제적·심리적 부담이 큰 결정임을 인지하고, 수술의 장점과 방치 시 위험성을 균형있게 전달해야 한다. 또한 베트남 근로자들은 쪼그려 앉아 일하는 경우가 많아 반월상연골 손상 위험이 높으므로, 예방 교육도 중요하다.",
        "commonMistakes": [
            {
                "mistake": "단순히 'sụn'(연골)이라고만 통역",
                "correction": "'sụn chêm'으로 정확히 명시",
                "explanation": "무릎에는 여러 종류 연골이 있어 구체적 명시 필요"
            },
            {
                "mistake": "'thoái hóa sụn khớp'(관절연골 마모)와 혼동",
                "correction": "반월상연골(sụn chêm)은 관절연골(sụn khớp)과 다른 구조",
                "explanation": "위치, 기능, 치료법이 완전히 다르므로 반드시 구분"
            },
            {
                "mistake": "'vỡ sụn'(연골 파괴)로 과장 표현",
                "correction": "'tổn thương sụn chêm'이 의학적으로 정확한 표현",
                "explanation": "'vỡ'는 너무 극단적 표현으로 환자에게 불필요한 공포 유발"
            }
        ],
        "examples": [
            {
                "ko": "관절경 검사에서 내측 반월상연골 파열이 확인되었습니다.",
                "vi": "Nội soi khớp xác nhận rách sụn chêm trong.",
                "situation": "formal"
            },
            {
                "ko": "무릎에서 소리가 나고 잘 안 펴져요.",
                "vi": "Đầu gối kêu lục cục và khó duỗi thẳng.",
                "situation": "onsite"
            },
            {
                "ko": "연골 수술 받으면 다음 날 퇴원할 수 있어요.",
                "vi": "Phẫu thuật sụn chêm xong có thể xuất viện ngày hôm sau.",
                "situation": "informal"
            }
        ],
        "relatedTerms": ["관절경수술", "무릎관절", "십자인대", "관절염", "물리치료"]
    },
    {
        "slug": "hep-ong-song",
        "korean": "척추관협착증",
        "vietnamese": "Hẹp ống sống",
        "hanja": "脊椎管狹窄症",
        "hanjaReading": "脊(등뼈 척) 椎(등뼈 추) 管(대롱 관) 狹(좁을 협) 窄(좁을 착) 症(증세 증)",
        "pronunciation": "헵 옹 송",
        "meaningKo": "척추 뼈 속의 신경이 지나가는 통로(척추관)가 좁아져 신경을 압박하는 질환. 통역 시 반드시 구분해야 할 것은 디스크(thoát vị đĩa đệm)와 협착증(hẹp ống sống)의 차이다. 환자들은 둘 다 '허리가 아프고 다리가 저리다'고 표현하지만, 원인과 치료법이 다르다. 협착증은 주로 노화로 인해 발생하며, 걸을 때 다리가 저려서 자주 쉬어야 하는 '간헐적 파행' 증상이 특징적이다. 베트남 고령 근로자들이 이 증상을 호소할 때, 단순 노화 현상으로 치부하지 말고 정확한 진단을 받도록 유도해야 한다. 한국에서는 감압술이나 유합술 같은 수술을 적극 권하지만, 베트남은 수술 비용과 회복 기간 부담으로 보존적 치료를 선호하는 문화적 차이가 있다.",
        "meaningVi": "Tình trạng ống sống - kênh chứa dây thần kinh tủy sống - bị hẹp lại, chèn ép dây thần kinh. Thường xảy ra ở người cao tuổi do thoái hóa cột sống, dây chằng dày lên, khớp phì đại. Triệu chứng điển hình là đau lưng, tê chân khi đi bộ và giảm khi nghỉ hoặc cúi người (gọi là 'khập khiễng từng đợt'). Nếu nặng, có thể gây yếu cơ, đại tiểu tiện khó khăn.",
        "context": "정형외과, 신경외과, 노인의학과",
        "culturalNote": "한국은 고령화 사회로 척추관협착증 환자가 매우 많으며, 척추 수술 기술이 세계적 수준이다. 건강보험 적용으로 수술 비용 부담도 상대적으로 낮다. 반면 베트남은 아직 고령화 초기 단계이며, 척추 수술은 매우 고가이고 전문 병원도 제한적이다. 통역 시 한국 의사가 수술을 권할 때, 베트남 환자의 경제적 상황과 가족 돌봄 체계(베트남은 노인을 자녀가 집에서 돌보는 문화)를 고려한 설명이 필요하다. 또한 베트남에서는 침술, 부항 등 전통 치료를 선호하는 경우가 많은데, 한국 의사들이 이를 비과학적으로 여기는 문화적 마찰이 발생할 수 있다. 통역사는 양측의 관점을 존중하면서 의학적으로 검증된 치료법을 선택하도록 중재하는 역할이 필요하다.",
        "commonMistakes": [
            {
                "mistake": "디스크(thoát vị đĩa đệm)와 혼동하여 통역",
                "correction": "협착증은 'hẹp ống sống', 디스크는 'thoát vị đĩa đệm'으로 명확히 구분",
                "explanation": "증상은 비슷하지만 원인(협착 vs 탈출)과 치료법이 다름"
            },
            {
                "mistake": "'hẹp kênh sống'으로 표현",
                "correction": "'hẹp ống sống'이 표준 의학용어",
                "explanation": "'ống'이 정확한 해부학적 표현"
            },
            {
                "mistake": "간헐적 파행을 단순 '다리 저림'으로 통역",
                "correction": "'khập khiễng từng đợt' 또는 'claudication'으로 정확히 표현",
                "explanation": "이 증상이 협착증의 특징적 증상이므로 정확한 전달 필수"
            }
        ],
        "examples": [
            {
                "ko": "MRI에서 요추 4-5번 부위 척추관 협착이 심하게 보입니다.",
                "vi": "MRI cho thấy hẹp ống sống nghiêm trọng ở vùng L4-L5.",
                "situation": "formal"
            },
            {
                "ko": "조금만 걸어도 다리가 저려서 자꾸 쉬어야 해요.",
                "vi": "Đi bộ một chút là chân tê phải nghỉ liên tục.",
                "situation": "onsite"
            },
            {
                "ko": "협착증 수술하면 허리 신경 압박이 풀려요.",
                "vi": "Phẫu thuật hẹp ống sống sẽ giảm chèn ép dây thần kinh.",
                "situation": "informal"
            }
        ],
        "relatedTerms": ["디스크", "간헐적파행", "척추유합술", "신경감압술", "물리치료"]
    },
    {
        "slug": "dot-quy-nao",
        "korean": "뇌졸중",
        "vietnamese": "Đột quỵ não",
        "hanja": "腦卒中",
        "hanjaReading": "腦(뇌 뇌) 卒(갑자기 졸) 中(맞을 중)",
        "pronunciation": "돋 뀌 나오",
        "meaningKo": "뇌혈관이 막히거나(뇌경색) 터져서(뇌출혈) 뇌 조직이 손상되는 응급 질환. 통역 시 생명과 직결된 응급 상황이므로 매우 정확하고 신속한 통역이 필요하다. 반드시 구분해야 할 것은 뇌경색(nhồi máu não)과 뇌출혈(xuất huyết não)이며, 치료법이 정반대(경색은 혈전용해제, 출혈은 지혈)이므로 절대 혼동해서는 안 된다. 골든타임(황금시간) 개념을 명확히 전달해야 하며, 한국은 3시간 이내 치료 시작을 목표로 하고 있다. 베트남 근로자나 환자 가족들이 전통 의학(침술, 사혈)을 먼저 시도하려는 경우가 있는데, 이는 치료 시기를 놓칠 수 있으므로 즉시 병원 이송의 중요성을 강력히 전달해야 한다.",
        "meaningVi": "Bệnh lý mạch máu não bị tắc nghẽn (nhồi máu não) hoặc vỡ (xuất huyết não), dẫn đến thiếu máu cục bộ và tổn thương não. Triệu chứng: yếu hoặc tê nửa người, méo miệng, nói khó, đau đầu dữ dội, chóng mặt. Đây là cấp cứu y khoa, cần đến bệnh viện ngay trong vòng 3 giờ để tăng cơ hội cứu sống và giảm di chứng. Nguyên nhân chính: huyết áp cao, đái tháo đường, hút thuốc.",
        "context": "응급실, 신경과, 재활의학과, 중환자실",
        "culturalNote": "한국은 뇌졸중 응급 치료 시스템(stroke unit)이 잘 갖춰져 있고, 119 구급대원들도 뇌졸중 증상을 빠르게 인지하여 전문 병원으로 이송한다. 반면 베트남은 농촌이나 중소도시에서는 뇌졸중 전문 치료가 가능한 병원이 부족하고, 구급차 시스템도 미비하다. 통역 시 베트남 환자나 가족이 '집에서 지켜보자' 또는 '전통 치료를 먼저 해보자'고 하면, 골든타임의 중요성과 후유증 위험을 강력히 설명해야 한다. 또한 베트남에서는 뇌졸중 후 재활 치료 인프라가 부족하여, 많은 환자들이 적절한 재활을 받지 못하고 장애를 안고 살아간다. 한국 의료진이 재활 계획을 설명할 때, 베트남 현지에서 실현 가능한 방법(가정 재활, 지역사회 자원 활용)도 함께 안내하도록 유도하는 것이 좋다.",
        "commonMistakes": [
            {
                "mistake": "뇌경색과 뇌출혈을 구분 없이 'đột quỵ'로만 통역",
                "correction": "반드시 'nhồi máu não'(경색) 또는 'xuất huyết não'(출혈)로 구분",
                "explanation": "치료법이 정반대이므로 구분 필수, 생명과 직결됨"
            },
            {
                "mistake": "'tai biến mạch máu não'를 다른 질환으로 오인",
                "correction": "이것도 뇌졸중의 베트남 의학용어 (đột quỵ = tai biến)",
                "explanation": "같은 질환의 다른 표현이므로 혼동 방지 필요"
            },
            {
                "mistake": "골든타임을 정확히 전달하지 않음",
                "correction": "'trong vòng 3 giờ'(3시간 이내) 명확히 강조",
                "explanation": "시간 지체 시 치료 효과 급감, 사망 또는 중증 장애 위험"
            }
        ],
        "examples": [
            {
                "ko": "CT 촬영 결과 뇌경색으로 확인되어 혈전용해제를 투여하겠습니다.",
                "vi": "Kết quả CT xác nhận nhồi máu não, chúng tôi sẽ tiêm thuốc tiêu huyết khối.",
                "situation": "formal"
            },
            {
                "ko": "한쪽 팔다리에 힘이 없고 말이 어눌하면 바로 119 부르세요.",
                "vi": "Nếu tay chân một bên yếu và nói khó thì gọi cấp cứu ngay.",
                "situation": "onsite"
            },
            {
                "ko": "뇌졸중은 3시간 내에 병원 가야 후유증이 적어요.",
                "vi": "Đột quỵ phải đến bệnh viện trong 3 giờ thì di chứng ít hơn.",
                "situation": "informal"
            }
        ],
        "relatedTerms": ["뇌경색", "뇌출혈", "골든타임", "재활치료", "고혈압"]
    },
    {
        "slug": "dong-kinh",
        "korean": "간질(뇌전증)",
        "vietnamese": "Động kinh",
        "hanja": "癎疾(腦電症)",
        "hanjaReading": "癎(간질 간) 疾(병 질) / 腦(뇌 뇌) 電(번개 전) 症(증세 증)",
        "pronunciation": "동 낑",
        "meaningKo": "뇌의 신경세포가 일시적으로 이상 흥분하여 발작을 일으키는 만성 신경 질환. 통역 시 매우 주의해야 할 점은 '간질'이라는 용어가 한국에서도 사회적 낙인이 있어 최근에는 '뇌전증'으로 순화하여 부르고 있다는 것이다. 베트남에서도 'động kinh'에 대한 사회적 편견이 심하여, 환자들이 병을 숨기거나 치료를 기피하는 경우가 많다. 통역 시 의료진의 설명을 정확히 전달하되, 환자와 가족의 심리적 부담을 고려한 공감적 태도가 필요하다. 또한 베트남에서는 간질을 귀신 들림이나 정신병으로 오해하는 전통적 인식이 남아있어, 이것이 뇌의 전기적 이상으로 인한 신경 질환임을 명확히 교육하는 것이 중요하다. 약물 복용의 중요성과 임의 중단의 위험성을 반드시 강조해야 한다.",
        "meaningVi": "Bệnh lý thần kinh mạn tính do các tế bào thần kinh trong não hoạt động bất thường, gây co giật. Có nhiều loại cơn động kinh: từ mất ý thức ngắn, động kinh cục bộ đến co giật toàn thân. Nguyên nhân có thể do di truyền, chấn thương đầu, nhiễm trùng não, u não. Cần uống thuốc thường xuyên để kiểm soát cơn động kinh, không được tự ý ngừng thuốc. Đây là bệnh thần kinh, không phải bệnh tâm thần.",
        "context": "신경과, 응급실, 소아청소년과",
        "culturalNote": "한국에서는 간질(뇌전증)에 대한 인식이 많이 개선되어 '뇌전증'이라는 중립적 용어를 사용하고, 환자 권리 보호와 사회적 차별 금지가 법제화되어 있다. 그러나 베트남은 아직도 'động kinh'을 정신병이나 저주로 여기는 미신이 강하게 남아있어, 환자들이 병을 숨기고 적절한 치료를 받지 못하는 경우가 많다. 통역 시 의사가 뇌전증 진단을 내릴 때, 환자와 가족이 받을 충격을 고려하여 이것이 치료 가능한 신경 질환임을 강조하고, 약물 복용으로 정상 생활이 가능함을 안심시켜야 한다. 또한 베트남에서는 항경련제 공급이 불안정한 지역도 있어, 약물 중단 시 위험성을 명확히 전달하고, 한국에서 처방받은 약을 베트남에서도 구할 수 있는지 확인하도록 도와야 한다.",
        "commonMistakes": [
            {
                "mistake": "'bệnh tâm thần'(정신병)으로 잘못 설명",
                "correction": "'bệnh thần kinh'(신경 질환)이 정확한 표현",
                "explanation": "정신병과 신경 질환은 완전히 다르며, 오해 시 환자에게 큰 상처"
            },
            {
                "mistake": "'co giật'(경련)과 'động kinh'을 동일시",
                "correction": "경련은 증상, 간질은 질환명으로 구분 필요",
                "explanation": "열성경련 등 다른 원인의 경련과 혼동 방지"
            },
            {
                "mistake": "사회적 편견 용어('bệnh ma', 귀신병)를 그대로 사용",
                "correction": "정식 의학용어 'động kinh' 사용 및 미신 교정",
                "explanation": "의료 통역사는 과학적 용어 사용으로 편견 해소에 기여해야 함"
            }
        ],
        "examples": [
            {
                "ko": "뇌파 검사 결과 뇌전증으로 진단되어 항경련제를 처방하겠습니다.",
                "vi": "Kết quả điện não đồ chẩn đoán động kinh, tôi sẽ kê thuốc chống co giật.",
                "situation": "formal"
            },
            {
                "ko": "발작할 때 억지로 입에 뭘 넣으면 안 돼요.",
                "vi": "Khi co giật không được nhét gì vào miệng.",
                "situation": "onsite"
            },
            {
                "ko": "약 먹으면 발작 안 일어나고 정상 생활 가능해요.",
                "vi": "Uống thuốc đều đặn thì không co giật và sống bình thường được.",
                "situation": "informal"
            }
        ],
        "relatedTerms": ["뇌파검사", "항경련제", "발작", "경련", "신경과"]
    },
    {
        "slug": "benh-parkinson",
        "korean": "파킨슨병",
        "vietnamese": "Bệnh Parkinson",
        "hanja": None,
        "hanjaReading": None,
        "pronunciation": "벵 파낀슨",
        "meaningKo": "뇌의 도파민 신경세포가 소실되어 운동 기능 장애가 나타나는 퇴행성 뇌질환. 통역 시 주의할 점은 파킨슨병(Parkinson's disease)과 파킨슨증후군(Parkinsonism)을 구분해야 한다는 것이다. 전자는 특발성 질환이고 후자는 다른 원인(약물, 뇌손상)으로 인한 증상이다. 주요 증상인 '떨림, 경직, 느린 움직임, 자세 불안정'을 정확히 전달해야 하며, 특히 '떨림'이 파킨슨병의 대표 증상으로 알려져 있지만 모든 환자에게 나타나는 것은 아니라는 점을 명확히 해야 한다. 베트남 고령 인구가 증가하면서 파킨슨병 환자도 늘고 있으나, 전문 치료를 받을 수 있는 병원이 제한적이다. 약물 치료의 중요성과 함께, 재활 운동과 일상생활 관리 방법을 자세히 통역하여 환자와 가족이 실천할 수 있도록 도와야 한다.",
        "meaningVi": "Bệnh thoái hóa thần kinh do thiếu dopamine trong não, gây rối loạn vận động. Triệu chứng chính: run tay chân (đặc biệt khi nghỉ), cứng cơ, chậm chạp trong cử động, mất thăng bằng. Thường khởi phát từ 60 tuổi trở lên. Chưa có thuốc chữa khỏi, nhưng có thể kiểm soát triệu chứng bằng thuốc (Levodopa), vật lý trị liệu và phẫu thuật kích thích não sâu (DBS) trong trường hợp nặng.",
        "context": "신경과, 재활의학과, 노인의학과",
        "culturalNote": "한국은 고령화 사회로 파킨슨병 환자가 많으며, 뇌심부자극술(DBS) 같은 첨단 치료도 건강보험 적용을 받는다. 파킨슨병 환자 지원 단체와 재활 프로그램도 잘 갖춰져 있다. 반면 베트남은 파킨슨병에 대한 인식이 낮아 단순 노화로 여기고 방치하는 경우가 많고, 레보도파 같은 기본 약물조차 구하기 어려운 지역이 있다. 통역 시 한국 의사가 약물 치료와 수술을 권할 때, 베트남에서의 약물 구입 가능성과 비용을 확인하도록 유도해야 한다. 또한 파킨슨병 환자는 낙상 위험이 높으므로, 가정 내 안전 관리(미끄럼 방지, 손잡이 설치)에 대한 구체적 조언을 통역하여 가족 돌봄자가 실천할 수 있도록 돕는 것이 중요하다.",
        "commonMistakes": [
            {
                "mistake": "노인성 떨림(run già)과 파킨슨병 떨림을 혼동",
                "correction": "파킨슨은 안정 시 떨림, 노인성 떨림은 동작 시 떨림",
                "explanation": "감별 진단이 중요하며 치료법도 다름"
            },
            {
                "mistake": "'bệnh lạc nội tiết tố'(호르몬 질환)로 오해",
                "correction": "'bệnh thoái hóa thần kinh'(퇴행성 신경 질환)이 정확",
                "explanation": "질환 분류를 명확히 해야 적절한 진료과 안내 가능"
            },
            {
                "mistake": "치매(sa sút trí tuệ)와 동일시",
                "correction": "파킨슨은 운동장애 질환이며, 말기에만 인지기능 저하 가능",
                "explanation": "초기에는 인지기능 정상이므로 혼동 방지 필요"
            }
        ],
        "examples": [
            {
                "ko": "파킨슨병 진단을 받으셨고, 레보도파 약물을 처방하겠습니다.",
                "vi": "Anh được chẩn đoán bệnh Parkinson và tôi sẽ kê thuốc Levodopa.",
                "situation": "formal"
            },
            {
                "ko": "손이 떨리고 걸음이 느려졌어요.",
                "vi": "Tay run và đi chậm hơn.",
                "situation": "onsite"
            },
            {
                "ko": "약 먹으면 증상이 좋아지지만 완치는 어려워요.",
                "vi": "Uống thuốc thì triệu chứng giảm nhưng khó chữa khỏi hoàn toàn.",
                "situation": "informal"
            }
        ],
        "relatedTerms": ["도파민", "레보도파", "뇌심부자극술", "떨림", "재활치료"]
    },
    {
        "slug": "benh-than-kinh-ngoai-bien",
        "korean": "말초신경병증",
        "vietnamese": "Bệnh thần kinh ngoại biên",
        "hanja": "末梢神經病症",
        "hanjaReading": "末(끝 말) 梢(끝 초) 神(귀신 신) 經(경서 경) 病(병 병) 症(증세 증)",
        "pronunciation": "벵 턴 낑 응와이 비엔",
        "meaningKo": "말초신경(뇌와 척수 밖의 신경)이 손상되어 손발 저림, 통증, 감각 이상, 근력 약화가 나타나는 질환. 통역 시 주의할 점은 원인이 매우 다양(당뇨, 알코올, 비타민 결핍, 약물 부작용, 독성 물질 노출 등)하므로, 환자의 직업력과 생활습관을 정확히 전달해야 원인 규명에 도움이 된다는 것이다. 특히 베트남 근로자들이 공장에서 유기용제나 중금속에 노출되는 경우가 많아 직업성 신경병증 가능성을 염두에 두어야 한다. '저림(tê)'과 '통증(đau)'을 명확히 구분하여 통역해야 하며, 증상의 분포(양측 대칭, 장갑-양말 모양 등)도 정확히 전달해야 한다. 당뇨병성 신경병증이 가장 흔하므로, 혈당 관리의 중요성을 반드시 강조해야 한다.",
        "meaningVi": "Tổn thương các dây thần kinh ngoại biên (ngoài não và tủy sống), gây tê, đau, yếu cơ ở tay chân. Nguyên nhân thường gặp: đái tháo đường (phổ biến nhất), thiếu vitamin B, rượu, thuốc hóa trị, tiếp xúc chất độc (chì, thủy ngân, dung môi hữu cơ). Triệu chứng thường bắt đầu từ đầu ngón tay/chân, lan dần lên, có cảm giác 'như đeo găng tay, mang tất'. Cần điều trị nguyên nhân gốc và kiểm soát triệu chứng.",
        "context": "신경과, 내분비내과, 직업환경의학과",
        "culturalNote": "한국은 당뇨병 유병률이 높아 당뇨병성 신경병증 환자가 매우 많으며, 신경전도검사 같은 진단 장비가 잘 갖춰져 있다. 반면 베트남은 당뇨병 인식이 낮아 혈당 조절이 안 되는 환자가 많고, 신경병증이 진행된 후에야 병원을 찾는 경우가 많다. 통역 시 당뇨병성 신경병증은 혈당 관리로 예방·진행 지연이 가능함을 강조하고, 베트남에서도 실천 가능한 혈당 관리 방법(식이요법, 운동, 약물)을 구체적으로 안내해야 한다. 또한 베트남 공장 근로자들이 화학물질 노출로 인한 직업성 신경병증을 앓는 경우가 많은데, 산재 보상 신청을 위해서는 직업 관련성을 입증하는 정확한 통역(노출 물질명, 노출 기간, 보호구 착용 여부 등)이 매우 중요하다.",
        "commonMistakes": [
            {
                "mistake": "모든 손발 저림을 '말초신경병증'으로 통역",
                "correction": "원인 확인 후 정확한 진단명 사용 (경추병증, 수근관증후군 등 구분)",
                "explanation": "손발 저림의 원인은 다양하므로 감별 진단 필요"
            },
            {
                "mistake": "'bệnh thần kinh trung ương'(중추신경)과 혼동",
                "correction": "'thần kinh ngoại biên'(말초)으로 명확히 구분",
                "explanation": "중추와 말초는 해부학적으로 완전히 다른 부위"
            },
            {
                "mistake": "'tê liệt'(마비)로 과장 표현",
                "correction": "'tê, đau, yếu cơ' 등 정확한 증상 표현",
                "explanation": "'liệt'은 완전 마비를 의미하여 환자에게 불필요한 공포 유발"
            }
        ],
        "examples": [
            {
                "ko": "신경전도검사에서 말초신경병증이 확인되었고, 당뇨 조절이 가장 중요합니다.",
                "vi": "Kiểm tra dẫn truyền thần kinh xác nhận bệnh thần kinh ngoại biên, quan trọng nhất là kiểm soát đường huyết.",
                "situation": "formal"
            },
            {
                "ko": "발끝이 저리고 감각이 둔해졌어요.",
                "vi": "Đầu ngón chân tê và cảm giác kém.",
                "situation": "onsite"
            },
            {
                "ko": "당뇨 잘 관리하면 신경병증 진행을 막을 수 있어요.",
                "vi": "Kiểm soát đái tháo đường tốt thì ngăn được bệnh thần kinh tiến triển.",
                "situation": "informal"
            }
        ],
        "relatedTerms": ["당뇨병", "신경전도검사", "비타민B", "수근관증후군", "직업병"]
    },
    {
        "slug": "dau-nua-dau",
        "korean": "두통(편두통)",
        "vietnamese": "Đau nửa đầu",
        "hanja": "頭痛(偏頭痛)",
        "hanjaReading": "頭(머리 두) 痛(아플 통) / 偏(치우칠 편) 頭(머리 두) 痛(아플 통)",
        "pronunciation": "다우 느어 더우",
        "pronunciation": "다우 느어 더우",
        "meaningKo": "머리의 한쪽에서 주로 나타나는 박동성 두통으로, 구역, 구토, 빛·소리 과민 등이 동반되는 신경 질환. 통역 시 반드시 구분해야 할 것은 일반 두통(đau đầu)과 편두통(đau nửa đầu 또는 migraine)이다. 편두통은 단순 두통이 아니라 뇌의 신경·혈관계 이상으로 인한 질환이므로, 전조 증상(시야 장애, 감각 이상), 통증 양상(박동성, 편측성), 동반 증상을 정확히 전달해야 한다. 베트남 근로자들이 두통을 호소할 때, 단순 피로나 스트레스로 치부하지 말고 편두통 가능성을 염두에 두어야 한다. 편두통은 약물로 예방과 치료가 가능하므로, 참지 말고 치료받아야 함을 강조해야 한다. 또한 한국은 트립탄 계열 약물이 흔히 처방되는데, 베트남에서는 구하기 어려울 수 있으므로 귀국 시 약물 처방에 대한 안내가 필요하다.",
        "meaningVi": "Đau đầu dữ dội, thường chỉ một bên đầu, có tính chất đập thình thịch, kèm buồn nôn, nôn, sợ ánh sáng và tiếng ồn. Có thể có triệu chứng báo trước (aura) như nhìn lóe sáng, tê tay. Cơn đau kéo dài 4-72 giờ nếu không điều trị. Thường do di truyền, stress, thiếu ngủ, thay đổi thời tiết, thực phẩm kích thích (chocolate, phô mai, rượu). Có thuốc đặc trị (triptan) và thuốc dự phòng.",
        "context": "신경과, 응급실, 가정의학과",
        "culturalNote": "한국에서는 편두통을 질환으로 인정하고 신경과에서 적극 치료하며, 트립탄 계열 약물이 건강보험 적용을 받는다. 그러나 베트남에서는 편두통을 단순 두통으로 여겨 진통제만 복용하고 참는 경우가 많고, 전문 치료를 받는 비율이 낮다. 통역 시 편두통이 만성화되면 삶의 질이 크게 떨어지므로, 예방 치료와 급성기 치료를 병행해야 함을 강조해야 한다. 또한 베트남 근로자들이 야근, 교대근무로 인한 수면 부족과 스트레스로 편두통이 악화될 수 있으므로, 생활습관 개선(규칙적 수면, 스트레스 관리, 유발 음식 회피)에 대한 구체적 조언을 통역하는 것이 중요하다. 베트남에서 트립탄 약물을 구하기 어렵다면, 대체 치료법(NSAIDs, 예방약)에 대한 정보도 제공해야 한다.",
        "commonMistakes": [
            {
                "mistake": "일반 두통(đau đầu)과 편두통을 구분 없이 통역",
                "correction": "편두통은 'đau nửa đầu' 또는 'migraine'으로 정확히 표현",
                "explanation": "편두통은 특정 치료가 필요한 질환이므로 구분 필수"
            },
            {
                "mistake": "'đau đầu do stress'(스트레스성 두통)로 단순화",
                "correction": "신경학적 질환임을 명확히 하고 전조증상, 동반증상 정확히 전달",
                "explanation": "단순 스트레스로 치부하면 적절한 치료를 받지 못함"
            },
            {
                "mistake": "전조 증상(aura)을 제대로 설명하지 않음",
                "correction": "'triệu chứng báo trước'로 표현하고 구체적 증상 나열",
                "explanation": "전조 증상은 편두통 진단의 중요한 단서"
            }
        ],
        "examples": [
            {
                "ko": "전조증상 동반 편두통으로 진단되어 트립탄 제제를 처방하겠습니다.",
                "vi": "Chẩn đoán đau nửa đầu có triệu chứng báo trước, tôi sẽ kê thuốc triptan.",
                "situation": "formal"
            },
            {
                "ko": "머리 한쪽이 쿵쿵거리며 아프고 토할 것 같아요.",
                "vi": "Một bên đầu đập thình thịch và muốn nôn.",
                "situation": "onsite"
            },
            {
                "ko": "편두통 약은 통증 시작하자마자 먹어야 효과가 좋아요.",
                "vi": "Thuốc đau nửa đầu uống ngay khi bắt đầu đau thì hiệu quả tốt.",
                "situation": "informal"
            }
        ],
        "relatedTerms": ["전조증상", "트립탄", "진통제", "예방약", "신경과"]
    }
]

def main():
    # 기존 파일 읽기
    with open(file_path, 'r', encoding='utf-8') as f:
        data = json.load(f)

    # 중복 확인
    existing_slugs = {term['slug'] for term in data}
    new_terms_filtered = [term for term in new_terms if term['slug'] not in existing_slugs]

    if not new_terms_filtered:
        print("⚠️  모든 용어가 이미 존재합니다.")
        return

    # 새 용어 추가
    data.extend(new_terms_filtered)

    # 파일 저장
    with open(file_path, 'w', encoding='utf-8') as f:
        json.dump(data, f, ensure_ascii=False, indent=2)

    print(f"✅ {len(new_terms_filtered)}개의 정형외과/신경과 용어가 추가되었습니다.")
    print(f"   파일: {file_path}")
    for term in new_terms_filtered:
        print(f"   - {term['korean']} ({term['vietnamese']})")

if __name__ == "__main__":
    main()
