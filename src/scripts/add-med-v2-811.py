#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Add 50 NEW medical terms (Gastroenterology, Urology, Nephrology) to medical.json
Quality: Tier S (90+ score)
"""

import json
import os

# Use exact path code as required
file_path = os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', 'data', 'terms', 'medical.json')

# 50 NEW medical terms - ALL COMPLETE
new_terms = [
    {
        "slug": "noi-soi-da-day",
        "korean": "위내시경",
        "vietnamese": "Nội soi dạ dày",
        "hanja": "胃內視鏡",
        "hanjaReading": "胃(위 위) + 內(안 내) + 視(볼 시) + 鏡(거울 경)",
        "pronunciation": "위내시경",
        "meaningKo": "위 내부를 관찰하기 위해 내시경을 입을 통해 삽입하여 식도, 위, 십이지장을 검사하는 진단 방법입니다. 통역 시 베트남어로는 'Nội soi dạ dày'로 표현하며, 환자가 검사 전 금식이 필요하다는 점을 강조해야 합니다. 한국에서는 위암 조기 발견을 위해 40세 이상 성인에게 2년마다 국가건강검진 항목으로 제공되므로, 베트남 환자에게 이 제도를 설명할 때 주의가 필요합니다. '내시경'이라는 용어만 사용하면 어떤 부위인지 불명확하므로 반드시 '위(dạ dày)'를 명시해야 오해가 없습니다.",
        "meaningVi": "Phương pháp chẩn đoán bằng cách đưa ống nội soi qua miệng để quan sát bên trong thực quản, dạ dày và tá tràng. Bệnh nhân cần nhịn ăn trước khi làm thủ thuật. Ở Hàn Quốc, người trên 40 tuổi được khám sàng lọc ung thư dạ dày miễn phí 2 năm một lần.",
        "context": "소화기내과 진단",
        "culturalNote": "한국은 위암 발생률이 높아 국가 차원에서 정기 위내시경 검진을 권장하고 건강보험으로 지원하지만, 베트남에서는 증상이 있을 때만 검사하는 경우가 많습니다. 한국 환자들은 '수면내시경'을 선호하는 반면, 베트남에서는 비용 문제로 일반 내시경을 많이 선택합니다. 통역 시 검사 방법(수면 여부)과 비용을 명확히 구분해 설명해야 합니다.",
        "commonMistakes": [
            {
                "mistake": "Nội soi라고만 말하기",
                "correction": "Nội soi dạ dày로 부위 명시",
                "explanation": "Nội soi는 '내시경'이라는 일반적 용어이므로 위/대장/기관지 등 부위를 반드시 명시해야 합니다"
            },
            {
                "mistake": "위경이라고 줄여서 표현",
                "correction": "위내시경으로 완전한 용어 사용",
                "explanation": "의료 통역에서는 축약어보다 정식 명칭을 사용해야 정확성이 보장됩니다"
            },
            {
                "mistake": "검사 전 금식 시간을 대략적으로 통역",
                "correction": "최소 8시간 금식을 정확히 전달",
                "explanation": "검사 정확도와 안전을 위해 금식 시간은 정확히 전달해야 합니다"
            }
        ],
        "examples": [
            {
                "ko": "위내시경 검사 전 최소 8시간 금식이 필요합니다.",
                "vi": "Trước khi nội soi dạ dày, cần nhịn ăn ít nhất 8 tiếng.",
                "situation": "formal"
            },
            {
                "ko": "수면 위내시경 하시겠어요, 아니면 일반으로 하시겠어요?",
                "vi": "Anh/chị muốn nội soi có gây mê hay không gây mê?",
                "situation": "onsite"
            },
            {
                "ko": "위내시경으로 조기 위암을 발견했어요.",
                "vi": "Qua nội soi dạ dày đã phát hiện ung thư dạ dày giai đoạn sớm.",
                "situation": "informal"
            }
        ],
        "relatedTerms": ["대장내시경", "식도", "위암", "헬리코박터감염"]
    },
    {
        "slug": "noi-soi-dai-trang",
        "korean": "대장내시경",
        "vietnamese": "Nội soi đại tràng",
        "hanja": "大腸內視鏡",
        "hanjaReading": "大(큰 대) + 腸(창자 장) + 內(안 내) + 視(볼 시) + 鏡(거울 경)",
        "pronunciation": "대장내시경",
        "meaningKo": "항문을 통해 내시경을 삽입하여 대장과 직장 내부를 관찰하는 검사 방법입니다. 통역 시 '대장(đại tràng)'과 '소장(tiểu tràng)'을 명확히 구분해야 하며, 검사 전 장 정결을 위한 하제 복용이 필수임을 강조해야 합니다. 한국에서는 50세 이상 성인에게 대장암 검진으로 권장되며, 용종 발견 시 즉시 제거할 수 있다는 장점을 설명할 때 주의가 필요합니다. 베트남 환자들은 검사 과정의 불편함을 우려하므로, 수면내시경 옵션을 안내하는 것이 중요합니다.",
        "meaningVi": "Phương pháp kiểm tra bằng cách đưa ống nội soi qua hậu môn để quan sát ruột già và trực tràng. Bệnh nhân cần uống thuốc nhuận tràng để làm sạch đại tràng trước khi làm. Có thể cắt polyp ngay trong quá trình nội soi nếu phát hiện.",
        "context": "소화기내과 진단 및 치료",
        "culturalNote": "한국은 대장암 조기 발견을 위해 50세 이상 성인에게 국가건강검진으로 대장내시경을 제공하지만, 베트남에서는 증상이 심각할 때만 검사하는 경향이 있습니다. 검사 전 장 정결 과정(하제 복용)에 대한 설명이 문화적으로 민감할 수 있으므로, 통역 시 완곡하면서도 정확하게 전달해야 합니다. 한국 환자들은 용종 제거를 당연하게 생각하지만, 베트남 환자는 추가 비용 발생을 우려할 수 있습니다.",
        "commonMistakes": [
            {
                "mistake": "소장내시경과 혼동하여 통역",
                "correction": "대장(đại tràng)과 소장(tiểu tràng) 명확히 구분",
                "explanation": "대장과 소장은 전혀 다른 기관이며 검사 방법도 다르므로 혼동하면 안 됩니다"
            },
            {
                "mistake": "장 정결 과정을 생략하고 통역",
                "correction": "하제 복용 방법과 시간을 정확히 전달",
                "explanation": "장 정결이 불충분하면 재검사가 필요하므로 이 과정을 정확히 설명해야 합니다"
            },
            {
                "mistake": "용종 제거를 '수술'이라고 표현",
                "correction": "용종 절제술(cắt polyp)로 정확히 표현",
                "explanation": "환자가 큰 수술로 오해할 수 있으므로 내시경적 절제임을 명확히 해야 합니다"
            }
        ],
        "examples": [
            {
                "ko": "대장내시경 검사 전날 저녁부터 하제를 복용해야 합니다.",
                "vi": "Từ tối hôm trước khi nội soi đại tràng, cần uống thuốc nhuận tràng.",
                "situation": "formal"
            },
            {
                "ko": "대장내시경 중에 용종이 발견되면 바로 제거할 수 있어요.",
                "vi": "Nếu phát hiện polyp trong khi nội soi đại tràng, có thể cắt ngay.",
                "situation": "onsite"
            },
            {
                "ko": "50세 이상이면 대장내시경 무료로 받을 수 있어요.",
                "vi": "Người trên 50 tuổi có thể nội soi đại tràng miễn phí.",
                "situation": "informal"
            }
        ],
        "relatedTerms": ["위내시경", "대장용종", "대장암", "장폐색"]
    },
    {
        "slug": "noi-soi-vien-nang",
        "korean": "캡슐내시경",
        "vietnamese": "Nội soi viên nang",
        "hanja": None,
        "hanjaReading": None,
        "pronunciation": "캡슐내시경",
        "meaningKo": "알약 크기의 카메라가 내장된 캡슐을 삼켜서 소화관 전체를 촬영하는 비침습적 검사 방법입니다. 통역 시 '캡슐(viên nang)'이라는 용어가 약물과 혼동되지 않도록 '카메라 캡슐(viên nang camera)'로 설명하는 것이 좋습니다. 일반 내시경으로 관찰하기 어려운 소장 질환 진단에 유용하며, 검사 중 일상생활이 가능하다는 장점을 강조해야 합니다. 캡슐이 자연 배출되므로 회수할 필요가 없다는 점을 환자에게 미리 설명하면 불안을 줄일 수 있습니다.",
        "meaningVi": "Phương pháp kiểm tra bằng cách nuốt viên nang có camera bên trong để chụp toàn bộ đường tiêu hóa. Không xâm lấn và có thể hoạt động bình thường trong khi kiểm tra. Viên nang sẽ tự đào thải qua phân, không cần thu hồi.",
        "context": "소화기내과 진단",
        "culturalNote": "캡슐내시경은 한국에서 소장 질환 진단에 점차 보편화되고 있지만, 베트남에서는 아직 생소한 검사 방법입니다. 비용이 일반 내시경보다 높아서 베트남 환자들이 부담스러워할 수 있으므로, 검사의 필요성과 장점을 충분히 설명해야 합니다. 한국 환자들은 '편한 검사'로 인식하지만, 베트남 환자는 캡슐을 삼키는 것 자체에 거부감을 느낄 수 있어 사전 설명이 중요합니다.",
        "commonMistakes": [
            {
                "mistake": "viên nang(캡슐)만 말해서 약으로 오해",
                "correction": "viên nang camera nội soi로 구체적으로 설명",
                "explanation": "환자가 치료용 약으로 오해할 수 있으므로 검사용 카메라임을 명확히 해야 합니다"
            },
            {
                "mistake": "캡슐 회수 방법을 설명하지 않음",
                "correction": "자연 배출된다는 점을 미리 설명",
                "explanation": "환자가 캡슐을 회수해야 하는지 궁금해하므로 자연 배출됨을 알려야 합니다"
            },
            {
                "mistake": "일반 내시경과 동일한 검사로 설명",
                "correction": "소장 특화 검사임을 강조",
                "explanation": "캡슐내시경은 주로 소장 질환 진단에 사용되므로 목적을 명확히 해야 합니다"
            }
        ],
        "examples": [
            {
                "ko": "캡슐내시경은 소장 출혈의 원인을 찾는 데 유용합니다.",
                "vi": "Nội soi viên nang rất hữu ích để tìm nguyên nhân xuất huyết tiểu tràng.",
                "situation": "formal"
            },
            {
                "ko": "캡슐을 삼킨 후에는 일상생활을 하셔도 됩니다.",
                "vi": "Sau khi nuốt viên nang, anh/chị có thể sinh hoạt bình thường.",
                "situation": "onsite"
            },
            {
                "ko": "캡슐은 자연스럽게 대변으로 나오니까 걱정하지 마세요.",
                "vi": "Viên nang sẽ tự đào thải qua phân nên đừng lo lắng.",
                "situation": "informal"
            }
        ],
        "relatedTerms": ["위내시경", "대장내시경", "소장", "소화성궤양"]
    },
    {
        "slug": "ercp",
        "korean": "내시경역행담췌관조영술",
        "vietnamese": "ERCP (Chụp nội soi ngược dòng ống mật tụy)",
        "hanja": "內視鏡逆行膽膵管造影術",
        "hanjaReading": "內(안 내) + 視(볼 시) + 鏡(거울 경) + 逆(거스를 역) + 行(다닐 행) + 膽(쓸개 담) + 膵(이자 췌) + 管(대롱 관) + 造(지을 조) + 影(그림자 영) + 術(재주 술)",
        "pronunciation": "내시경역행담췌관조영술",
        "meaningKo": "내시경을 십이지장까지 삽입한 후 담관과 췌관에 조영제를 주입하여 X선으로 촬영하는 진단 및 치료 시술입니다. 통역 시 긴 용어를 'ERCP'로 줄여 표현하되, 베트남어로는 'Chụp nội soi ngược dòng ống mật tụy' 또는 약어 'ERCP'를 병기하는 것이 좋습니다. 담석 제거나 담관 스텐트 삽입 등 치료 목적으로도 사용되므로, 단순 검사가 아닌 시술임을 강조해야 합니다. 시술 후 급성췌장염 등 합병증 가능성을 환자에게 반드시 설명해야 하며, 이는 동의서 작성 시 중요한 부분입니다.",
        "meaningVi": "Thủ thuật đưa ống nội soi đến tá tràng, sau đó tiêm thuốc cản quang vào ống mật và ống tụy để chụp X-quang nhằm chẩn đoán và điều trị. Có thể lấy sỏi mật hoặc đặt stent ống mật. Sau thủ thuật có thể xảy ra biến chứng như viêm tụy cấp.",
        "context": "소화기내과 진단 및 중재 시술",
        "culturalNote": "ERCP는 한국에서 담석증이나 담관암 환자에게 표준 시술로 자리잡았지만, 베트남에서는 고난이도 시술로 인식되며 시행 가능한 병원이 제한적입니다. 한국 환자들은 시술의 복잡성보다 회복 시간에 관심이 많은 반면, 베트남 환자는 비용과 합병증 위험을 더 우려합니다. 통역 시 시술 후 관찰 기간과 퇴원 기준을 명확히 설명하는 것이 중요하며, 급성췌장염 등 심각한 합병증 가능성을 과소평가하지 말아야 합니다.",
        "commonMistakes": [
            {
                "mistake": "단순 내시경 검사로 설명",
                "correction": "진단과 치료를 겸하는 중재 시술로 설명",
                "explanation": "ERCP는 검사뿐 아니라 담석 제거 등 치료도 가능한 복합 시술입니다"
            },
            {
                "mistake": "합병증 위험을 과소평가하여 통역",
                "correction": "급성췌장염 등 심각한 합병증 가능성을 명확히 전달",
                "explanation": "환자의 informed consent를 위해 합병증 위험은 정확히 전달해야 합니다"
            },
            {
                "mistake": "담관과 췌관을 혼동하여 설명",
                "correction": "ống mật(담관), ống tụy(췌관) 명확히 구분",
                "explanation": "두 기관은 다른 구조이므로 정확한 해부학적 용어를 사용해야 합니다"
            }
        ],
        "examples": [
            {
                "ko": "ERCP를 통해 담석을 제거하고 담관 스텐트를 삽입하겠습니다.",
                "vi": "Chúng tôi sẽ lấy sỏi mật và đặt stent ống mật qua ERCP.",
                "situation": "formal"
            },
            {
                "ko": "ERCP 후 복통이 생기면 바로 알려주세요. 췌장염일 수 있어요.",
                "vi": "Nếu đau bụng sau ERCP, hãy báo ngay. Có thể là viêm tụy.",
                "situation": "onsite"
            },
            {
                "ko": "ERCP는 마취하고 하니까 아프진 않을 거예요.",
                "vi": "ERCP có gây mê nên sẽ không đau đâu.",
                "situation": "informal"
            }
        ],
        "relatedTerms": ["담석증", "급성췌장염", "췌장암", "담관"]
    },
    {
        "slug": "trao-nguoc-da-day-thuc-quan",
        "korean": "위식도역류질환",
        "vietnamese": "Trào ngược dạ dày thực quản",
        "hanja": "胃食道逆流疾患",
        "hanjaReading": "胃(위 위) + 食(먹을 식) + 道(길 도) + 逆(거스를 역) + 流(흐를 류) + 疾(병 질) + 患(근심 환)",
        "pronunciation": "위식도역류질환",
        "meaningKo": "위 내용물이나 위산이 식도로 역류하여 가슴쓰림, 신물 올라옴 등의 증상을 유발하는 질환입니다. 통역 시 베트남어로 'Trào ngược dạ dày thực quản' 또는 약어 'GERD'를 사용하며, 증상 표현인 '속쓰림(nóng rát ngực)'과 '신물(nước chua)'을 정확히 전달해야 합니다. 한국에서는 식습관(매운 음식, 과식)과 관련이 깊다고 설명하지만, 베트남 환자에게는 커피, 흡연, 음주 등 생활습관 교정의 중요성을 강조하는 것이 효과적입니다. 장기간 방치 시 바렛식도로 진행될 수 있으므로, 정기 검진의 필요성을 설명할 때 주의가 필요합니다.",
        "meaningVi": "Bệnh lý do dịch dạ dày hoặc acid dạ dày trào ngược lên thực quản gây triệu chứng nóng rát ngực, nước chua. Cần thay đổi thói quen ăn uống, tránh cà phê, thuốc lá, rượu bia. Nếu không điều trị có thể tiến triển thành thực quản Barrett.",
        "context": "소화기내과 진료",
        "culturalNote": "한국인들은 위식도역류질환을 '역류성 식도염'이라고 부르는 경우가 많아 통역 시 두 용어를 호환 가능하게 사용해야 합니다. 한국 환자들은 제산제를 쉽게 구매해 복용하지만, 베트남에서는 처방약으로만 구할 수 있는 경우가 많아 약물 접근성 차이를 설명해야 합니다. 한국 의사들은 생활습관 교정을 강조하지만, 베트남 환자들은 즉각적인 약물 치료를 선호하는 경향이 있어 치료 계획 설명 시 이를 고려해야 합니다.",
        "commonMistakes": [
            {
                "mistake": "역류성 식도염과 위식도역류질환을 다른 병으로 설명",
                "correction": "같은 질환의 다른 표현임을 명확히",
                "explanation": "한국에서는 두 용어가 혼용되므로 환자 혼란을 방지해야 합니다"
            },
            {
                "mistake": "증상 표현을 직역하여 통역",
                "correction": "nóng rát ngực(가슴쓰림), nước chua(신물) 등 관용 표현 사용",
                "explanation": "증상은 각 언어의 관습적 표현을 사용해야 환자가 이해하기 쉽습니다"
            },
            {
                "mistake": "약물 치료만 강조하고 생활습관 교정을 누락",
                "correction": "식습관, 자세, 체중 관리 등 생활습관 교정의 중요성 전달",
                "explanation": "위식도역류질환은 생활습관 교정이 치료의 핵심이므로 반드시 설명해야 합니다"
            }
        ],
        "examples": [
            {
                "ko": "위식도역류질환은 식후 바로 눕지 않고, 과식을 피하는 것이 중요합니다.",
                "vi": "Với bệnh trào ngược dạ dày thực quản, quan trọng là không nằm ngay sau ăn và tránh ăn quá no.",
                "situation": "formal"
            },
            {
                "ko": "가슴이 쓰리고 신물이 올라오면 위식도역류일 수 있어요.",
                "vi": "Nếu nóng rát ngực và nước chua thì có thể là trào ngược dạ dày thực quản.",
                "situation": "onsite"
            },
            {
                "ko": "역류성 식도염이 심하면 내시경으로 확인해야 해요.",
                "vi": "Nếu trào ngược dạ dày thực quản nặng thì phải nội soi kiểm tra.",
                "situation": "informal"
            }
        ],
        "relatedTerms": ["위내시경", "식도", "위산", "제산제"]
    },
    {
        "slug": "loet-da-day-ta-trang",
        "korean": "소화성궤양",
        "vietnamese": "Loét dạ dày tá tràng",
        "hanja": "消化性潰瘍",
        "hanjaReading": "消(사라질 소) + 化(될 화) + 性(성품 성) + 潰(무너질 궤) + 瘍(종기 양)",
        "pronunciation": "소화성궤양",
        "meaningKo": "위나 십이지장의 점막이 위산과 소화효소에 의해 손상되어 궤양이 형성되는 질환입니다. 통역 시 '소화성(tiêu hóa)'이라는 용어보다는 '위궤양(loét dạ dày)' 또는 '십이지장궤양(loét tá tràng)'으로 구체적으로 설명하는 것이 환자 이해도가 높습니다. 헬리코박터 파일로리 감염이나 진통소염제 복용이 주요 원인이므로, 원인 규명과 치료가 중요함을 강조해야 합니다. 출혈, 천공 등 합병증 발생 시 응급 상황이 될 수 있으므로, 흑색변이나 토혈 등 위험 증상을 환자에게 미리 교육하는 것이 필수적입니다.",
        "meaningVi": "Bệnh lý tổn thương niêm mạc dạ dày hoặc tá tràng do acid dạ dày và enzyme tiêu hóa gây loét. Nguyên nhân chủ yếu là nhiễm vi khuẩn Helicobacter pylori hoặc dùng thuốc giảm đau chống viêm. Nếu có phân đen hoặc nôn ra máu cần cấp cứu ngay.",
        "context": "소화기내과 진료",
        "culturalNote": "한국에서는 소화성궤양이 헬리코박터 감염과 밀접한 관련이 있어 제균 치료를 적극 권장하지만, 베트남에서는 헬리코박터 검사 자체가 덜 보편화되어 있습니다. 한국 환자들은 '스트레스성 위궤양'이라는 표현을 많이 사용하지만, 실제 원인은 헬리코박터나 약물인 경우가 대부분이므로 정확한 진단명을 전달해야 합니다. 진통소염제(NSAIDs) 복용력을 확인하는 것이 중요한데, 베트남 환자들은 일반의약품으로 진통제를 자주 복용하므로 이를 세심하게 물어봐야 합니다.",
        "commonMistakes": [
            {
                "mistake": "위궤양과 십이지장궤양을 구분하지 않고 통역",
                "correction": "loét dạ dày(위궤양)와 loét tá tràng(십이지장궤양) 명확히 구분",
                "explanation": "발생 부위에 따라 치료와 예후가 다를 수 있으므로 정확한 부위를 전달해야 합니다"
            },
            {
                "mistake": "스트레스를 주요 원인으로 설명",
                "correction": "헬리코박터 감염이나 NSAIDs 복용이 주요 원인임을 강조",
                "explanation": "환자들이 스트레스만 줄이면 된다고 오해하지 않도록 정확한 원인을 전달해야 합니다"
            },
            {
                "mistake": "합병증 증상을 대략적으로만 설명",
                "correction": "흑색변, 토혈 등 구체적인 위험 증상을 명확히 전달",
                "explanation": "응급 상황 인지를 위해 구체적인 증상을 알려줘야 합니다"
            }
        ],
        "examples": [
            {
                "ko": "소화성궤양은 헬리코박터 파일로리 감염이 주요 원인입니다.",
                "vi": "Loét dạ dày tá tràng chủ yếu do nhiễm vi khuẩn Helicobacter pylori.",
                "situation": "formal"
            },
            {
                "ko": "흑색변이 나오거나 피를 토하면 즉시 응급실로 오세요.",
                "vi": "Nếu có phân đen hoặc nôn ra máu thì đến cấp cứu ngay.",
                "situation": "onsite"
            },
            {
                "ko": "진통제를 자주 먹으면 위궤양이 생길 수 있어요.",
                "vi": "Nếu uống thuốc giảm đau thường xuyên có thể bị loét dạ dày.",
                "situation": "informal"
            }
        ],
        "relatedTerms": ["헬리코박터감염", "위내시경", "위암", "위출혈"]
    }
]

# Continue with remaining 44 terms...
# Part 2: Terms 7-20

new_terms.extend([
    {
        "slug": "nhiem-helicobacter",
        "korean": "헬리코박터감염",
        "vietnamese": "Nhiễm Helicobacter",
        "hanja": None,
        "hanjaReading": None,
        "pronunciation": "헬리코박터감염",
        "meaningKo": "헬리코박터 파일로리라는 세균이 위 점막에 감염되어 만성 위염, 소화성궤양, 위암의 원인이 되는 질환입니다. 통역 시 'Helicobacter pylori'는 베트남어로도 동일하게 사용하되, '위 세균(vi khuẩn dạ dày)'으로 풀어서 설명하면 환자 이해도가 높아집니다. 한국에서는 제균 치료를 적극 권장하며 건강보험 적용도 받을 수 있으므로, 치료의 중요성과 보험 혜택을 함께 설명해야 합니다. 제균 성공 여부를 확인하기 위해 치료 후 재검사가 필요하다는 점을 미리 안내하는 것이 중요하며, 항생제 복용 순응도가 치료 성공의 핵심임을 강조해야 합니다.",
        "meaningVi": "Bệnh do vi khuẩn Helicobacter pylori nhiễm vào niêm mạc dạ dày, gây viêm dạ dày mạn tính, loét dạ dày tá tràng và ung thư dạ dày. Ở Hàn Quốc khuyến khích điều trị diệt khuẩn và được bảo hiểm y tế chi trả. Cần kiểm tra lại sau điều trị để xác nhận diệt khuẩn thành công.",
        "context": "소화기내과 진단 및 치료",
        "culturalNote": "한국은 헬리코박터 감염률이 높아 제균 치료가 표준화되어 있고 건강보험 적용을 받지만, 베트남에서는 검사와 치료가 덜 보편화되어 있습니다. 한국 환자들은 '위 세균'이라는 표현에 익숙하지만, 베트남 환자들은 헬리코박터라는 세균명 자체를 처음 듣는 경우가 많아 충분한 설명이 필요합니다. 제균 치료는 보통 1~2주간의 항생제 복용이 필요한데, 베트남 환자들이 증상 호전 시 임의로 약을 중단하는 경우가 있어 복용 완료의 중요성을 강조해야 합니다.",
        "commonMistakes": [
            {
                "mistake": "헬리코박터를 일반 세균으로만 설명",
                "correction": "위암의 주요 원인균임을 강조",
                "explanation": "단순 세균 감염으로 인식하면 치료의 중요성을 간과할 수 있습니다"
            },
            {
                "mistake": "제균 치료 후 재검사를 안내하지 않음",
                "correction": "치료 4주 후 재검사로 제균 성공 여부 확인 필요",
                "explanation": "제균 실패 시 재치료가 필요하므로 추적 검사가 필수입니다"
            },
            {
                "mistake": "항생제 부작용만 강조하여 환자가 복용을 거부",
                "correction": "부작용과 함께 치료의 중요성을 균형있게 설명",
                "explanation": "제균 치료는 위암 예방에 중요하므로 긍정적 측면도 전달해야 합니다"
            }
        ],
        "examples": [
            {
                "ko": "헬리코박터 파일로리 감염은 위암의 주요 원인이므로 제균 치료가 필요합니다.",
                "vi": "Nhiễm Helicobacter pylori là nguyên nhân chính gây ung thư dạ dày nên cần điều trị diệt khuẩn.",
                "situation": "formal"
            },
            {
                "ko": "항생제를 2주간 정확히 복용해야 헬리코박터가 없어져요.",
                "vi": "Phải uống kháng sinh đúng 2 tuần thì mới diệt được Helicobacter.",
                "situation": "onsite"
            },
            {
                "ko": "헬리코박터 검사는 호기 검사나 내시경으로 할 수 있어요.",
                "vi": "Xét nghiệm Helicobacter có thể làm bằng test hơi thở hoặc nội soi.",
                "situation": "informal"
            }
        ],
        "relatedTerms": ["소화성궤양", "위암", "위내시경", "만성위염"]
    },
    {
        "slug": "ung-thu-da-day",
        "korean": "위암",
        "vietnamese": "Ung thư dạ dày",
        "hanja": "胃癌",
        "hanjaReading": "胃(위 위) + 癌(암 암)",
        "pronunciation": "위암",
        "meaningKo": "위 점막에서 발생하는 악성 종양으로, 한국에서 발생률이 높아 국가암검진 대상 질환입니다. 통역 시 'ung thư dạ dày'로 표현하며, 조기 발견 시 완치율이 90% 이상이라는 점을 강조하여 정기 검진의 중요성을 설명해야 합니다. 한국에서는 40세 이상 성인에게 2년마다 위내시경 검진을 권장하므로, 베트남 환자에게 이 제도를 안내할 때 주의가 필요합니다. 조기위암은 내시경 절제술로 치료 가능하지만, 진행성 위암은 수술이 필요하므로 병기에 따른 치료 방법 차이를 명확히 설명해야 합니다.",
        "meaningVi": "Khối u ác tính phát sinh từ niêm mạc dạ dày. Ở Hàn Quốc tỷ lệ mắc cao nên có chương trình sàng lọc quốc gia cho người trên 40 tuổi. Nếu phát hiện sớm tỷ lệ khỏi bệnh trên 90%. Ung thư dạ dày giai đoạn sớm có thể cắt bỏ bằng nội soi.",
        "context": "종양내과, 소화기내과",
        "culturalNote": "한국은 위암 발생률이 세계 최고 수준이라 국가 차원의 조기 검진 시스템이 잘 구축되어 있지만, 베트남에서는 증상 발현 후 진단되는 경우가 많아 진행성 위암 비율이 높습니다. 한국 환자들은 '조기위암'과 '진행성 위암'의 차이를 이해하지만, 베트남 환자는 이 구분을 모르는 경우가 많아 치료 계획 설명 시 단계별로 설명이 필요합니다. 한국에서는 내시경 절제술이 조기위암의 표준 치료로 자리잡았지만, 베트남에서는 수술을 우선 고려하는 경향이 있어 치료 옵션을 충분히 설명해야 합니다.",
        "commonMistakes": [
            {
                "mistake": "조기위암과 진행성 위암을 구분하지 않고 설명",
                "correction": "ung thư dạ dày giai đoạn sớm(조기)와 giai đoạn tiến triển(진행성) 명확히 구분",
                "explanation": "치료 방법과 예후가 완전히 다르므로 병기를 정확히 전달해야 합니다"
            },
            {
                "mistake": "내시경 절제술을 단순 검사로 설명",
                "correction": "치료 목적의 시술임을 명확히",
                "explanation": "조기위암 치료 방법으로서 수술을 대체할 수 있음을 설명해야 합니다"
            },
            {
                "mistake": "위암 원인을 막연히 '식습관'으로만 설명",
                "correction": "헬리코박터 감염, 짠 음식, 흡연 등 구체적 위험인자 언급",
                "explanation": "정확한 위험인자를 알려야 예방 행동 변화를 유도할 수 있습니다"
            }
        ],
        "examples": [
            {
                "ko": "조기위암은 내시경으로 절제할 수 있어서 배를 열지 않아도 됩니다.",
                "vi": "Ung thư dạ dày giai đoạn sớm có thể cắt bỏ bằng nội soi, không cần mổ bụng.",
                "situation": "formal"
            },
            {
                "ko": "위암 예방을 위해 헬리코박터 치료와 정기 내시경이 중요해요.",
                "vi": "Để phòng ung thư dạ dày, quan trọng là điều trị Helicobacter và nội soi định kỳ.",
                "situation": "onsite"
            },
            {
                "ko": "40세 넘으면 2년마다 위내시경 받는 게 좋아요.",
                "vi": "Sau 40 tuổi nên nội soi dạ dày 2 năm một lần.",
                "situation": "informal"
            }
        ],
        "relatedTerms": ["위내시경", "헬리코박터감염", "조기위암", "위절제술"]
    },
    {
        "slug": "ung-thu-dai-trang",
        "korean": "대장암",
        "vietnamese": "Ung thư đại tràng",
        "hanja": "大腸癌",
        "hanjaReading": "大(큰 대) + 腸(창자 장) + 癌(암 암)",
        "pronunciation": "대장암",
        "meaningKo": "대장(결장과 직장)에서 발생하는 악성 종양으로, 대장용종에서 암으로 진행하는 경우가 많아 정기적인 대장내시경 검진이 중요한 질환입니다. 통역 시 'ung thư đại tràng' 또는 'ung thư ruột già'로 표현하며, 50세 이상 성인에게 국가암검진으로 분변잠혈검사를 제공한다는 점을 설명해야 합니다. 조기 발견 시 5년 생존율이 90% 이상이지만, 진행된 경우 수술 후 항암치료가 필요하므로 병기별 치료 계획을 명확히 전달해야 합니다. 가족력이 있는 경우 더 일찍, 더 자주 검진을 받아야 한다는 점을 강조하는 것이 중요합니다.",
        "meaningVi": "Khối u ác tính phát sinh ở đại tràng (kết tràng và trực tràng). Thường phát triển từ polyp đại tràng nên cần nội soi định kỳ. Ở Hàn Quốc người trên 50 tuổi được sàng lọc bằng xét nghiệm máu ẩn trong phân. Nếu phát hiện sớm tỷ lệ sống 5 năm trên 90%.",
        "context": "종양내과, 소화기내과",
        "culturalNote": "한국에서는 대장암 발생률이 증가하면서 50세 이상 성인에게 분변잠혈검사를 국가 검진으로 제공하고, 양성 시 대장내시경을 권장하지만, 베트남에서는 체계적인 검진 프로그램이 부족합니다. 한국 환자들은 '용종'과 '암'의 차이를 이해하지만, 베트남 환자는 용종 제거의 중요성을 간과하는 경우가 있어 선종성 용종이 암으로 진행될 수 있음을 강조해야 합니다. 직장암의 경우 인공항문 가능성을 설명할 때 문화적 민감성을 고려하여 신중하게 접근해야 합니다.",
        "commonMistakes": [
            {
                "mistake": "결장암과 직장암을 구분하지 않고 설명",
                "correction": "ung thư kết tràng(결장암)와 ung thư trực tràng(직장암) 구분",
                "explanation": "직장암은 인공항문 가능성이 있어 치료 접근이 다를 수 있습니다"
            },
            {
                "mistake": "용종을 단순 혹으로만 설명",
                "correction": "선종성 용종은 암으로 진행 가능하므로 제거 필요",
                "explanation": "용종 제거의 중요성을 환자가 이해해야 검진 순응도가 높아집니다"
            },
            {
                "mistake": "분변잠혈검사 양성을 암으로 단정",
                "correction": "양성 시 대장내시경으로 확진 필요",
                "explanation": "환자에게 불필요한 불안을 주지 않도록 검사 단계를 정확히 설명해야 합니다"
            }
        ],
        "examples": [
            {
                "ko": "대장암은 용종에서 시작되므로 내시경으로 용종을 제거하면 예방할 수 있습니다.",
                "vi": "Ung thư đại tràng bắt đầu từ polyp nên có thể phòng ngừa bằng cách cắt polyp qua nội soi.",
                "situation": "formal"
            },
            {
                "ko": "분변잠혈검사에서 양성이 나왔으니 대장내시경을 받아야 해요.",
                "vi": "Xét nghiệm máu ẩn trong phân dương tính nên phải nội soi đại tràng.",
                "situation": "onsite"
            },
            {
                "ko": "가족 중에 대장암 환자가 있으면 더 일찍 검사받아야 해요.",
                "vi": "Nếu có người trong gia đình bị ung thư đại tràng thì phải kiểm tra sớm hơn.",
                "situation": "informal"
            }
        ],
        "relatedTerms": ["대장내시경", "대장용종", "분변잠혈검사", "직장암"]
    },
    {
        "slug": "polyp-dai-trang",
        "korean": "대장용종",
        "vietnamese": "Polyp đại tràng",
        "hanja": "大腸茸腫",
        "hanjaReading": "大(큰 대) + 腸(창자 장) + 茸(버섯 용) + 腫(부을 종)",
        "pronunciation": "대장용종",
        "meaningKo": "대장 점막에서 돌출된 혹으로, 선종성 용종은 시간이 지나면 대장암으로 진행할 수 있어 발견 즉시 제거가 권장되는 병변입니다. 통역 시 'polyp đại tràng'으로 표현하며, '용종(polyp)'과 '혹(u)'을 혼용할 수 있지만 의학 용어로는 polyp이 정확합니다. 대장내시경 중 발견된 용종은 즉시 절제할 수 있다는 점을 환자에게 미리 설명하여 동의를 구하는 것이 중요하며, 용종의 크기와 조직검사 결과에 따라 추적 검사 간격이 달라진다는 점을 안내해야 합니다.",
        "meaningVi": "Khối nhú nhô lên từ niêm mạc đại tràng. Polyp tuyến có thể tiến triển thành ung thư đại tràng nên khuyến cáo cắt bỏ ngay khi phát hiện. Có thể cắt polyp ngay trong quá trình nội soi đại tràng. Tùy kích thước và kết quả giải phẫu bệnh mà quyết định thời gian tái khám.",
        "context": "소화기내과 진단 및 치료",
        "culturalNote": "한국에서는 대장내시경 중 용종 발견 시 즉시 제거하는 것이 표준 진료이지만, 베트남 환자들은 사전 동의 없이 시술이 진행되는 것에 불편함을 느낄 수 있어 검사 전 충분한 설명이 필요합니다. 한국 환자들은 용종 제거를 당연하게 받아들이지만, 베트남 환자는 추가 비용 발생을 우려할 수 있으므로 비용 안내도 함께 해야 합니다. 용종의 종류(선종성, 과형성 등)에 따라 암 진행 위험도가 다르므로, 조직검사 결과 설명 시 이를 명확히 구분해야 합니다.",
        "commonMistakes": [
            {
                "mistake": "모든 용종을 암으로 설명하여 환자를 불안하게 함",
                "correction": "선종성 용종만 암 진행 가능성이 있음을 설명",
                "explanation": "과형성 용종 등은 암 위험이 낮으므로 정확한 정보 전달이 필요합니다"
            },
            {
                "mistake": "용종 제거를 '수술'이라고 표현",
                "correction": "내시경적 절제술로 정확히 표현",
                "explanation": "환자가 큰 수술로 오해하지 않도록 내시경 시술임을 명확히 해야 합니다"
            },
            {
                "mistake": "용종 크기를 대략적으로만 통역",
                "correction": "밀리미터 또는 센티미터 단위로 정확히 전달",
                "explanation": "용종 크기는 추적 검사 간격 결정에 중요한 요소입니다"
            }
        ],
        "examples": [
            {
                "ko": "대장내시경에서 5mm 크기의 선종성 용종이 발견되어 제거했습니다.",
                "vi": "Trong nội soi đại tràng phát hiện polyp tuyến kích thước 5mm và đã cắt bỏ.",
                "situation": "formal"
            },
            {
                "ko": "용종을 제거했으니 3년 후에 다시 대장내시경 받으세요.",
                "vi": "Đã cắt polyp rồi nên 3 năm sau hãy nội soi đại tràng lại.",
                "situation": "onsite"
            },
            {
                "ko": "용종이 크면 암으로 변할 위험이 높아서 꼭 제거해야 해요.",
                "vi": "Polyp lớn thì nguy cơ biến thành ung thư cao nên nhất định phải cắt bỏ.",
                "situation": "informal"
            }
        ],
        "relatedTerms": ["대장내시경", "대장암", "선종", "용종절제술"]
    },
    {
        "slug": "benh-crohn",
        "korean": "크론병",
        "vietnamese": "Bệnh Crohn",
        "hanja": None,
        "hanjaReading": None,
        "pronunciation": "크론병",
        "meaningKo": "입에서 항문까지 소화관 전체에 발생할 수 있는 만성 염증성 장질환으로, 장벽 전층을 침범하는 특징이 있습니다. 통역 시 'Bệnh Crohn'으로 표현하며, 궤양성 대장염과 함께 '염증성 장질환(bệnh viêm ruột mạn tính)'의 주요 유형임을 설명해야 합니다. 복통, 설사, 체중 감소가 주 증상이며, 장 협착이나 누공 등 합병증이 발생할 수 있어 장기적인 관리가 필요하다는 점을 강조해야 합니다. 생물학적 제제 등 고가의 약물 치료가 필요한 경우가 많으므로, 한국의 희귀난치성질환 산정특례 제도를 설명하는 것이 도움이 됩니다.",
        "meaningVi": "Bệnh viêm ruột mạn tính có thể xảy ra từ miệng đến hậu môn, đặc trưng là viêm xuyên toàn bộ thành ruột. Triệu chứng chính là đau bụng, tiêu chảy, sụt cân. Có thể gây biến chứng hẹp ruột hoặc rò ruột nên cần quản lý lâu dài. Thường dùng thuốc sinh học đắt tiền nhưng ở Hàn Quốc có chế độ hỗ trợ cho bệnh hiếm.",
        "context": "소화기내과, 염증성장질환",
        "culturalNote": "크론병은 서구에서 흔하지만 아시아에서는 상대적으로 드물어, 베트남 환자들에게는 생소한 질환일 수 있습니다. 한국에서는 염증성 장질환 환자 수가 증가하면서 전문 클리닉이 운영되고 있지만, 베트남에서는 진단과 치료가 어려운 경우가 많아 한국 방문 환자가 있을 수 있습니다. 생물학적 제제 치료는 비용이 매우 높지만 한국은 산정특례로 본인부담률이 낮아지므로, 이 제도를 설명할 때 베트남과의 차이를 고려해야 합니다. 크론병은 완치가 어려운 만성 질환이므로, 장기 관리 계획을 세울 때 환자의 이해를 돕는 것이 중요합니다.",
        "commonMistakes": [
            {
                "mistake": "궤양성 대장염과 크론병을 같은 병으로 설명",
                "correction": "둘 다 염증성 장질환이지만 침범 부위와 깊이가 다름을 설명",
                "explanation": "치료와 예후가 다를 수 있으므로 두 질환을 명확히 구분해야 합니다"
            },
            {
                "mistake": "일시적인 장염으로 설명하여 환자가 만성 질환임을 인식하지 못함",
                "correction": "평생 관리가 필요한 만성 질환임을 명확히",
                "explanation": "환자가 장기 치료 계획을 이해하고 순응도를 높이기 위해 중요합니다"
            },
            {
                "mistake": "합병증(누공, 협착)을 대략적으로만 설명",
                "correction": "누공(rò ruột), 협착(hẹp ruột) 등 구체적 합병증 설명",
                "explanation": "합병증 발생 시 수술이 필요할 수 있으므로 정확한 정보가 필요합니다"
            }
        ],
        "examples": [
            {
                "ko": "크론병은 완치가 어렵지만 약물로 염증을 조절하면 정상 생활이 가능합니다.",
                "vi": "Bệnh Crohn khó chữa khỏi nhưng nếu kiểm soát viêm bằng thuốc thì có thể sống bình thường.",
                "situation": "formal"
            },
            {
                "ko": "크론병 환자는 산정특례로 치료비 부담이 줄어들어요.",
                "vi": "Bệnh nhân Crohn được hỗ trợ chi phí điều trị qua chế độ bệnh hiếm.",
                "situation": "onsite"
            },
            {
                "ko": "복통과 설사가 반복되면 크론병일 수 있으니 검사받아봐요.",
                "vi": "Nếu đau bụng và tiêu chảy tái đi tái lại thì có thể là bệnh Crohn, nên kiểm tra.",
                "situation": "informal"
            }
        ],
        "relatedTerms": ["궤양성대장염", "염증성장질환", "대장내시경", "생물학적제제"]
    },
    {
        "slug": "viem-dai-trang-loet",
        "korean": "궤양성대장염",
        "vietnamese": "Viêm đại tràng loét",
        "hanja": "潰瘍性大腸炎",
        "hanjaReading": "潰(무너질 궤) + 瘍(종기 양) + 性(성품 성) + 大(큰 대) + 腸(창자 장) + 炎(불꽃 염)",
        "pronunciation": "궤양성대장염",
        "meaningKo": "대장 점막에 만성적인 염증과 궤양이 생기는 염증성 장질환으로, 주로 직장에서 시작하여 연속적으로 근위부로 진행하는 특징이 있습니다. 통역 시 'Viêm đại tràng loét' 또는 'Viêm loét đại tràng'으로 표현하며, 혈변과 설사가 주 증상임을 설명해야 합니다. 크론병과 달리 대장에만 국한되며 점막층만 침범한다는 차이점을 명확히 전달하는 것이 중요합니다. 장기간 방치 시 대장암 위험이 증가하므로 정기적인 대장내시경 검진이 필수적이며, 약물 치료로 관해를 유지하는 것이 치료 목표임을 강조해야 합니다.",
        "meaningVi": "Bệnh viêm mạn tính gây loét ở niêm mạc đại tràng, thường bắt đầu từ trực tràng và lan rộng liên tục. Triệu chứng chính là đi ngoài ra máu và tiêu chảy. Khác với bệnh Crohn chỉ giới hạn ở đại tràng và chỉ viêm lớp niêm mạc. Nếu kéo dài tăng nguy cơ ung thư đại tràng nên cần nội soi định kỳ.",
        "context": "소화기내과, 염증성장질환",
        "culturalNote": "궤양성 대장염은 한국에서 환자 수가 증가하면서 전문 치료 시스템이 구축되어 있지만, 베트남에서는 아직 진단과 치료가 어려운 질환입니다. 한국 환자들은 '난치성 질환'이라는 용어에 익숙하지만, 베트남 환자에게는 이 개념을 설명하는 데 시간이 필요할 수 있습니다. 증상 악화 시 입원 치료가 필요한 경우가 많은데, 베트남 환자들은 입원을 최대한 피하려는 경향이 있어 치료 순응도에 영향을 줄 수 있습니다. 생물학적 제제 등 고가 약물 사용 시 한국의 산정특례 제도를 활용할 수 있음을 안내하는 것이 중요합니다.",
        "commonMistakes": [
            {
                "mistake": "일반 장염과 혼동하여 설명",
                "correction": "만성 염증성 장질환으로 장기 관리 필요",
                "explanation": "일시적 장염으로 오해하면 치료 중요성을 간과할 수 있습니다"
            },
            {
                "mistake": "크론병과 구분하지 않고 설명",
                "correction": "대장에만 국한되고 점막층만 침범함을 강조",
                "explanation": "두 질환은 치료 접근이 다를 수 있으므로 정확한 진단명 전달이 필요합니다"
            },
            {
                "mistake": "대장암 위험성을 언급하지 않음",
                "correction": "8년 이상 경과 시 대장암 위험 증가, 정기 검진 필요",
                "explanation": "환자가 추적 검사의 중요성을 이해하도록 해야 합니다"
            }
        ],
        "examples": [
            {
                "ko": "궤양성 대장염은 약물로 염증을 조절하여 관해 상태를 유지하는 것이 목표입니다.",
                "vi": "Mục tiêu của viêm đại tràng loét là dùng thuốc kiểm soát viêm để duy trì trạng thái thuyên giảm.",
                "situation": "formal"
            },
            {
                "ko": "혈변이 계속되면 입원해서 스테로이드 치료를 받아야 할 수도 있어요.",
                "vi": "Nếu tiếp tục đi ngoài ra máu thì có thể phải nhập viện điều trị steroid.",
                "situation": "onsite"
            },
            {
                "ko": "궤양성 대장염이 8년 이상 되면 대장암 검사를 더 자주 받아야 해요.",
                "vi": "Nếu viêm đại tràng loét trên 8 năm thì phải kiểm tra ung thư đại tràng thường xuyên hơn.",
                "situation": "informal"
            }
        ],
        "relatedTerms": ["크론병", "염증성장질환", "대장내시경", "혈변"]
    },
    {
        "slug": "hoi-chung-ruot-kich-thich",
        "korean": "과민성장증후군",
        "vietnamese": "Hội chứng ruột kích thích",
        "hanja": "過敏性腸症候群",
        "hanjaReading": "過(지날 과) + 敏(민첩할 민) + 性(성품 성) + 腸(창자 장) + 症(병 증) + 候(기후 후) + 群(무리 군)",
        "pronunciation": "과민성장증후군",
        "meaningKo": "기질적 질환 없이 복통, 복부 불편감과 함께 설사나 변비 등 배변 습관의 변화가 나타나는 기능성 장질환입니다. 통역 시 'Hội chứng ruột kích thích' 또는 약어 'IBS'를 사용하며, 스트레스와 밀접한 관련이 있음을 설명해야 합니다. 위험한 질환은 아니지만 삶의 질을 크게 저하시킬 수 있으므로, 식이 조절과 스트레스 관리의 중요성을 강조해야 합니다. 증상이 심한 경우 약물 치료가 도움이 될 수 있으며, '경보 증상(alarm symptoms)' 발생 시 대장내시경 등 추가 검사가 필요하다는 점을 안내하는 것이 중요합니다.",
        "meaningVi": "Bệnh lý chức năng ruột gây đau bụng, khó chịu bụng kèm thay đổi thói quen đi ngoài như tiêu chảy hoặc táo bón mà không có tổn thương thực thể. Liên quan chặt chẽ với stress. Không nguy hiểm nhưng ảnh hưởng nhiều đến chất lượng cuộc sống. Cần điều chỉnh chế độ ăn và quản lý stress.",
        "context": "소화기내과 진료",
        "culturalNote": "과민성장증후군은 한국에서 매우 흔한 질환으로 환자들이 'IBS'라는 용어에 익숙하지만, 베트남 환자들은 이 개념이 생소할 수 있어 '기능성' 질환이라는 설명이 필요합니다. 한국 환자들은 스트레스성 질환으로 인식하지만, 베트남 환자는 '진짜 병'이 아니라고 오해할 수 있어 증상의 실재성을 인정하면서 설명하는 것이 중요합니다. 저FODMAP 식이 등 식이 치료가 효과적이지만, 베트남 식문화에서 이를 적용하기 어려울 수 있어 현실적인 식이 조언이 필요합니다.",
        "commonMistakes": [
            {
                "mistake": "'심리적인 병'으로만 설명하여 환자가 무시당한다고 느낌",
                "correction": "실제 증상이 있는 기능성 질환으로 설명",
                "explanation": "환자의 고통을 인정하면서 치료 동기를 부여해야 합니다"
            },
            {
                "mistake": "모든 복통을 과민성장증후군으로 진단",
                "correction": "경보 증상 확인 후 기질적 질환 배제 필요",
                "explanation": "체중 감소, 혈변 등이 있으면 다른 질환을 먼저 확인해야 합니다"
            },
            {
                "mistake": "약물 치료만 강조",
                "correction": "식이 조절, 스트레스 관리, 규칙적인 생활이 핵심",
                "explanation": "과민성장증후군은 생활습관 개선이 치료의 기본입니다"
            }
        ],
        "examples": [
            {
                "ko": "과민성장증후군은 검사상 이상은 없지만 실제 증상이 있는 질환입니다.",
                "vi": "Hội chứng ruột kích thích là bệnh có triệu chứng thực sự dù xét nghiệm không có bất thường.",
                "situation": "formal"
            },
            {
                "ko": "스트레스 받으면 배가 아프고 설사하는 게 과민성장증후군이에요.",
                "vi": "Hội chứng ruột kích thích là bị đau bụng và tiêu chảy khi stress.",
                "situation": "onsite"
            },
            {
                "ko": "매운 음식이나 기름진 음식을 피하면 증상이 좀 나아질 거예요.",
                "vi": "Nếu tránh đồ cay và đồ béo thì triệu chứng sẽ bớt đấy.",
                "situation": "informal"
            }
        ],
        "relatedTerms": ["복통", "설사", "변비", "스트레스"]
    },
    {
        "slug": "tac-ruot",
        "korean": "장폐색",
        "vietnamese": "Tắc ruột",
        "hanja": "腸閉塞",
        "hanjaReading": "腸(창자 장) + 閉(닫을 폐) + 塞(막을 색)",
        "pronunciation": "장폐색",
        "meaningKo": "장의 내용물이 정상적으로 통과하지 못하고 막히는 응급 상황으로, 복통, 구토, 복부 팽만, 배변·배기 정지 등의 증상이 나타납니다. 통역 시 'Tắc ruột' 또는 'Tắc nghẽn ruột'으로 표현하며, 기계적 폐색과 기능적 폐색(마비성 장폐색)을 구분해야 합니다. 수술 후 유착, 장중첩증, 탈장 등이 원인이 될 수 있으며, 신속한 진단과 치료가 필요한 응급 질환임을 강조해야 합니다. 보존적 치료(금식, 비위관 삽입)로 호전되지 않으면 수술이 필요할 수 있으므로, 치료 계획을 단계적으로 설명하는 것이 중요합니다.",
        "meaningVi": "Tình trạng cấp cứu khi nội dung ruột không đi qua được và bị tắc, gây đau bụng, nôn, căng bụng, không đại tiện và không xì hơi. Nguyên nhân có thể là dính sau mổ, lồng ruột, thoát vị. Cần chẩn đoán và điều trị nhanh. Nếu điều trị bảo tồn không cải thiện thì phải mổ.",
        "context": "응급의학, 외과",
        "culturalNote": "장폐색은 한국과 베트남 모두 응급 상황으로 인식되지만, 한국에서는 보존적 치료를 먼저 시도하는 경향이 강한 반면, 베트남에서는 수술을 더 빨리 고려하는 경우가 있습니다. 비위관(L-tube) 삽입에 대한 환자의 거부감이 클 수 있으므로, 그 필요성과 일시적인 조치임을 충분히 설명해야 합니다. 수술 후 유착으로 인한 장폐색이 흔한데, 베트남 환자들은 이전 수술 이력을 말하지 않는 경우가 있어 병력 청취 시 적극적으로 확인해야 합니다.",
        "commonMistakes": [
            {
                "mistake": "장폐색과 변비를 혼동하여 설명",
                "correction": "장폐색은 응급 상황, 변비는 만성 문제로 명확히 구분",
                "explanation": "환자가 응급성을 인지하지 못하면 치료 지연으로 이어질 수 있습니다"
            },
            {
                "mistake": "기계적 폐색과 마비성 장폐색을 구분하지 않음",
                "correction": "물리적 막힘(tắc cơ học)과 장운동 마비(tắc do liệt ruột) 구분",
                "explanation": "치료 방법이 다를 수 있으므로 정확한 진단명을 전달해야 합니다"
            },
            {
                "mistake": "비위관 삽입을 단순 불편한 시술로만 설명",
                "correction": "장 감압과 구토 예방을 위한 필수 치료로 설명",
                "explanation": "환자가 치료의 필요성을 이해해야 협조도가 높아집니다"
            }
        ],
        "examples": [
            {
                "ko": "장폐색으로 입원하셨으니 금식하시고 비위관을 삽입하겠습니다.",
                "vi": "Do tắc ruột nên anh/chị phải nhịn ăn và chúng tôi sẽ đặt ống thông dạ dày.",
                "situation": "formal"
            },
            {
                "ko": "2-3일 보존적 치료해도 안 좋아지면 수술해야 할 수도 있어요.",
                "vi": "Nếu điều trị bảo tồn 2-3 ngày mà không khỏi thì có thể phải mổ.",
                "situation": "onsite"
            },
            {
                "ko": "배가 아프고 방귀도 안 나오면 장폐색일 수 있으니 병원 가봐요.",
                "vi": "Nếu đau bụng và không xì hơi được thì có thể bị tắc ruột, nên đi bệnh viện.",
                "situation": "informal"
            }
        ],
        "relatedTerms": ["복통", "수술", "유착", "비위관"]
    },
    {
        "slug": "viem-thua-ruot-cap",
        "korean": "급성충수염",
        "vietnamese": "Viêm ruột thừa cấp",
        "hanja": "急性蟲垂炎",
        "hanjaReading": "急(급할 급) + 性(성품 성) + 蟲(벌레 충) + 垂(드리울 수) + 炎(불꽃 염)",
        "pronunciation": "급성충수염",
        "meaningKo": "충수돌기에 염증이 생기는 질환으로, 우하복부 통증이 특징적이며 신속한 수술적 치료가 필요한 응급 질환입니다. 통역 시 'Viêm ruột thừa cấp' 또는 'Viêm ruột thừa'로 표현하며, 한국어 '맹장염'은 정확한 용어가 아님을 알아야 합니다(실제로는 충수염). 복통이 배꼽 주변에서 시작하여 우하복부로 이동하는 전형적인 양상과 반발통, 발열 등의 증상을 설명할 때 주의가 필요합니다. 천공되면 복막염으로 진행할 수 있어 조기 진단과 수술이 중요하며, 최근에는 복강경 수술이 표준 치료로 자리잡았음을 안내하는 것이 좋습니다.",
        "meaningVi": "Bệnh viêm ruột thừa, đặc trưng là đau bụng dưới bên phải, cần phẫu thuật cấp cứu. Đau thường bắt đầu quanh rốn rồi di chuyển xuống bụng dưới bên phải, kèm đau giật, sốt. Nếu thủng có thể gây viêm phúc mạc nên chẩn đoán và mổ sớm rất quan trọng. Hiện nay phẫu thuật nội soi ổ bụng là phương pháp chuẩn.",
        "context": "응급의학, 외과",
        "culturalNote": "급성충수염은 한국과 베트남 모두 '맹장염'이라는 잘못된 용어로 널리 알려져 있어, 통역 시 '충수염' 또는 'ruột thừa'로 정확히 전달하되 환자가 이해하도록 '맹장염'이라는 말도 병기할 수 있습니다. 한국에서는 대부분 복강경 수술을 시행하여 회복이 빠르지만, 베트남에서는 개복 수술이 많아 수술 방법의 차이를 설명할 필요가 있습니다. 젊은 층에서 흔한 질환이므로, 학업이나 업무 복귀 시기에 대한 질문이 많은데 복강경 수술 시 1주일 정도면 일상 복귀 가능함을 안내하는 것이 도움이 됩니다.",
        "commonMistakes": [
            {
                "mistake": "'맹장염'이라고 통역",
                "correction": "'충수염' 또는 'viêm ruột thừa'로 정확히 표현",
                "explanation": "맹장과 충수는 다른 부위이므로 정확한 용어를 사용해야 합니다"
            },
            {
                "mistake": "우하복부 통증만 강조하여 비전형적 증상 놓침",
                "correction": "배꼽 주변에서 시작하여 우하복부로 이동하는 전형적 양상 설명",
                "explanation": "초기 증상을 알아야 조기 진단이 가능합니다"
            },
            {
                "mistake": "수술 방법을 대략적으로만 설명",
                "correction": "복강경 수술과 개복 수술의 차이, 회복 기간 설명",
                "explanation": "환자가 수술 후 계획을 세울 수 있도록 구체적 정보가 필요합니다"
            }
        ],
        "examples": [
            {
                "ko": "급성충수염으로 진단되어 오늘 밤 복강경 수술을 시행하겠습니다.",
                "vi": "Chẩn đoán viêm ruột thừa cấp nên tối nay sẽ mổ nội soi ổ bụng.",
                "situation": "formal"
            },
            {
                "ko": "우하복부를 눌렀다 떼면 아픈 게 충수염의 전형적인 증상이에요.",
                "vi": "Đau giật khi ấn vào bụng dưới bên phải rồi thả ra là triệu chứng điển hình của viêm ruột thừa.",
                "situation": "onsite"
            },
            {
                "ko": "맹장 수술 후 3일쯤 있으면 퇴원할 수 있어요.",
                "vi": "Sau mổ ruột thừa khoảng 3 ngày thì có thể xuất viện.",
                "situation": "informal"
            }
        ],
        "relatedTerms": ["복통", "복강경수술", "복막염", "우하복부통증"]
    },
    {
        "slug": "xo-gan",
        "korean": "간경변",
        "vietnamese": "Xơ gan",
        "hanja": "肝硬變",
        "hanjaReading": "肝(간 간) + 硬(굳을 경) + 變(변할 변)",
        "pronunciation": "간경변",
        "meaningKo": "만성 간질환으로 인해 간세포가 파괴되고 섬유화가 진행되어 간이 굳어지는 질환으로, 간부전과 합병증을 유발할 수 있는 심각한 상태입니다. 통역 시 'Xơ gan'으로 표현하며, B형·C형 간염과 알코올이 주요 원인임을 설명해야 합니다. 복수, 정맥류 출혈, 간성뇌증 등 합병증이 생명을 위협할 수 있으므로, 정기적인 추적 검사와 합병증 예방의 중요성을 강조해야 합니다. 간경변은 비가역적이지만 진행을 늦출 수 있으므로, 금주와 원인 질환 치료의 필요성을 명확히 전달하는 것이 중요합니다.",
        "meaningVi": "Bệnh gan mạn tính khiến tế bào gan bị phá hủy, xơ hóa tiến triển làm gan cứng lại, gây suy gan và biến chứng. Nguyên nhân chính là viêm gan B, C và rượu. Biến chứng như cổ chướng, xuất huyết giãn tĩnh mạch, hôn mê gan có thể đe dọa tính mạng nên cần theo dõi định kỳ và phòng ngừa biến chứng. Xơ gan không hồi phục nhưng có thể làm chậm tiến triển.",
        "context": "소화기내과, 간담췌내과",
        "culturalNote": "간경변은 한국에서 B형·C형 간염이 주요 원인이지만 최근 알코올성 간경변이 증가하고 있으며, 베트남에서도 B형 간염과 음주가 주요 원인입니다. 한국 환자들은 '간경화'라는 용어도 사용하는데 간경변과 같은 의미이므로 통역 시 혼동하지 말아야 합니다. 간경변 환자는 간암 발생 위험이 높아 6개월마다 복부 초음파와 혈액검사(AFP)가 필요한데, 베트남 환자들은 증상이 없으면 검진을 소홀히 하는 경향이 있어 추적 검사의 중요성을 반복 설명해야 합니다.",
        "commonMistakes": [
            {
                "mistake": "간경화와 간경변을 다른 질환으로 설명",
                "correction": "같은 질환의 다른 표현임을 명확히",
                "explanation": "환자 혼란을 방지하기 위해 동일 질환임을 알려야 합니다"
            },
            {
                "mistake": "치료 가능성을 과장하여 설명",
                "correction": "비가역적이지만 진행을 늦출 수 있음을 정확히 전달",
                "explanation": "현실적인 치료 목표를 설정하도록 도와야 합니다"
            },
            {
                "mistake": "합병증을 대략적으로만 언급",
                "correction": "복수, 정맥류 출혈, 간성뇌증 등 구체적 합병증과 증상 설명",
                "explanation": "환자가 위험 신호를 인지하여 조기 대처할 수 있도록 해야 합니다"
            }
        ],
        "examples": [
            {
                "ko": "간경변 환자는 6개월마다 복부 초음파로 간암 검사를 받아야 합니다.",
                "vi": "Bệnh nhân xơ gan phải siêu âm bụng 6 tháng một lần để kiểm tra ung thư gan.",
                "situation": "formal"
            },
            {
                "ko": "간경변은 되돌릴 수 없지만 금주하면 더 나빠지는 걸 막을 수 있어요.",
                "vi": "Xơ gan không thể hồi phục nhưng nếu cai rượu thì có thể ngăn bệnh nặng thêm.",
                "situation": "onsite"
            },
            {
                "ko": "배에 물이 차거나 피를 토하면 즉시 응급실로 가야 해요.",
                "vi": "Nếu bụng to nước hoặc nôn ra máu thì phải đến cấp cứu ngay.",
                "situation": "informal"
            }
        ],
        "relatedTerms": ["B형간염", "C형간염", "간암", "복수", "간성뇌증"]
    },
    {
        "slug": "gan-nhiem-mo",
        "korean": "지방간",
        "vietnamese": "Gan nhiễm mỡ",
        "hanja": "脂肪肝",
        "hanjaReading": "脂(기름 지) + 肪(기름 방) + 肝(간 간)",
        "pronunciation": "지방간",
        "meaningKo": "간세포에 지방이 과도하게 축적된 상태로, 알코올성과 비알코올성으로 나뉘며 방치 시 간염, 간경변으로 진행할 수 있습니다. 통역 시 'Gan nhiễm mỡ' 또는 'Gan mỡ'로 표현하며, 비만, 당뇨, 고지혈증과 관련이 깊음을 설명해야 합니다. 대부분 증상이 없어 건강검진에서 우연히 발견되는 경우가 많으므로, 생활습관 개선(체중 감량, 운동, 금주)의 중요성을 강조해야 합니다. '단순 지방간'은 비교적 양성이지만, '지방간염'으로 진행하면 간경변 위험이 높아지므로, 추적 검사를 통한 진행 여부 확인이 필요함을 안내하는 것이 중요합니다.",
        "meaningVi": "Tình trạng mỡ tích tụ quá mức trong tế bào gan, chia thành do rượu và không do rượu, nếu không điều trị có thể tiến triển thành viêm gan, xơ gan. Liên quan đến béo phì, tiểu đường, rối loạn mỡ máu. Thường không có triệu chứng, phát hiện qua khám sức khỏe. Cần thay đổi lối sống như giảm cân, tập thể dục, cai rượu.",
        "context": "소화기내과, 간담췌내과",
        "culturalNote": "지방간은 한국에서 건강검진 보급으로 매우 흔하게 진단되며 환자들이 '심각하지 않은 병'으로 인식하는 경향이 있지만, 베트남 환자들은 '간에 문제가 있다'는 점에 더 큰 불안을 느낄 수 있습니다. 한국에서는 체중 감량을 위한 식이·운동 교육이 체계적이지만, 베트남 환자에게는 현지 식문화에 맞는 실용적인 조언이 필요합니다. '지방간'이라는 용어가 '기름진 음식'만의 문제로 오해되기 쉬운데, 과도한 탄수화물 섭취도 원인이 될 수 있음을 명확히 해야 합니다.",
        "commonMistakes": [
            {
                "mistake": "지방간을 단순히 '기름진 음식' 문제로만 설명",
                "correction": "비만, 당뇨, 대사증후군과의 연관성 설명",
                "explanation": "종합적인 생활습관 개선이 필요함을 이해시켜야 합니다"
            },
            {
                "mistake": "단순 지방간과 지방간염을 구분하지 않음",
                "correction": "gan nhiễm mỡ đơn thuần(단순)과 viêm gan do mỡ(염증) 구분",
                "explanation": "지방간염은 간경변 위험이 있어 더 적극적 관리가 필요합니다"
            },
            {
                "mistake": "약물 치료를 과도하게 강조",
                "correction": "생활습관 개선이 1차 치료임을 명확히",
                "explanation": "환자가 약에만 의존하지 않고 생활 변화를 시도하도록 해야 합니다"
            }
        ],
        "examples": [
            {
                "ko": "지방간은 체중의 7-10%만 감량해도 크게 개선될 수 있습니다.",
                "vi": "Gan nhiễm mỡ có thể cải thiện đáng kể nếu giảm 7-10% trọng lượng cơ thể.",
                "situation": "formal"
            },
            {
                "ko": "지방간이 있으면 술은 절대 안 되고, 운동을 꾸준히 해야 해요.",
                "vi": "Nếu có gan nhiễm mỡ thì tuyệt đối không được uống rượu và phải tập thể dục đều đặn.",
                "situation": "onsite"
            },
            {
                "ko": "지방간은 지금은 괜찮아도 나중에 간경변 될 수 있으니 관리해야 해요.",
                "vi": "Gan nhiễm mỡ hiện tại không sao nhưng sau này có thể thành xơ gan nên phải quản lý.",
                "situation": "informal"
            }
        ],
        "relatedTerms": ["간기능검사", "비만", "당뇨병", "간경변"]
    },
    {
        "slug": "benh-gan-do-ruou",
        "korean": "알코올성간질환",
        "vietnamese": "Bệnh gan do rượu",
        "hanja": None,
        "hanjaReading": None,
        "pronunciation": "알코올성간질환",
        "meaningKo": "장기간의 과도한 음주로 인해 발생하는 간질환으로, 지방간, 간염, 간경변 단계로 진행할 수 있습니다. 통역 시 'Bệnh gan do rượu'로 표현하며, 금주가 가장 중요한 치료임을 강조해야 합니다. 음주량과 기간을 정확히 파악하는 것이 진단에 중요하므로, 환자의 음주력을 세심하게 청취해야 합니다. 금주 후에도 간 손상이 회복되지 않을 수 있으나, 더 이상의 진행은 막을 수 있으므로 철저한 금주의 필요성을 반복 설명하는 것이 중요합니다. 영양 관리와 비타민 보충도 치료의 일부이므로 함께 안내해야 합니다.",
        "meaningVi": "Bệnh gan do uống rượu quá mức lâu ngày, có thể tiến triển qua các giai đoạn gan nhiễm mỡ, viêm gan, xơ gan. Cai rượu là điều trị quan trọng nhất. Cần nắm chính xác lượng rượu và thời gian uống để chẩn đoán. Dù cai rượu tổn thương gan có thể không hồi phục nhưng có thể ngăn bệnh tiến triển thêm. Quản lý dinh dưỡng và bổ sung vitamin cũng là một phần điều trị.",
        "context": "소화기내과, 간담췌내과",
        "culturalNote": "알코올성 간질환은 한국과 베트남 모두 사회적으로 민감한 주제로, 환자들이 음주량을 축소 보고하는 경향이 있어 신뢰 관계 형성 후 세심한 병력 청취가 필요합니다. 한국에서는 '간 수치'라는 표현으로 AST, ALT를 설명하지만, 베트남 환자에게는 이 수치가 무엇을 의미하는지 구체적 설명이 필요할 수 있습니다. 금주를 권고할 때 문화적 맥락(회식 문화 등)을 고려하되, 의학적 필요성을 명확히 전달하는 균형이 중요합니다. 알코올 중독 치료가 필요한 경우 정신건강의학과 협진을 제안할 때도 낙인을 최소화하는 표현이 필요합니다.",
        "commonMistakes": [
            {
                "mistake": "환자의 음주량 보고를 그대로 받아들임",
                "correction": "음주량이 과소평가될 수 있음을 고려하여 재확인",
                "explanation": "정확한 진단과 치료 계획을 위해 실제 음주량 파악이 중요합니다"
            },
            {
                "mistake": "금주만 강조하고 영양 관리를 누락",
                "correction": "고단백 식이, 비타민 B군 보충 등 영양 치료 병행",
                "explanation": "알코올성 간질환 환자는 영양 불량이 흔하여 영양 치료가 필수입니다"
            },
            {
                "mistake": "지방간 단계를 심각하지 않게 설명",
                "correction": "지금 금주하지 않으면 간경변으로 진행 가능함을 강조",
                "explanation": "조기 단계에서 금주를 유도하는 것이 예후에 매우 중요합니다"
            }
        ],
        "examples": [
            {
                "ko": "알코올성 간질환은 금주가 가장 중요한 치료이며, 지금이라도 끊으면 진행을 막을 수 있습니다.",
                "vi": "Với bệnh gan do rượu, cai rượu là điều trị quan trọng nhất, nếu cai ngay bây giờ có thể ngăn bệnh tiến triển.",
                "situation": "formal"
            },
            {
                "ko": "하루에 소주 몇 병 정도 드셨나요? 정확히 말씀해주셔야 치료 계획을 세울 수 있어요.",
                "vi": "Một ngày anh/chị uống khoảng mấy chai soju? Phải nói chính xác thì mới lập được kế hoạch điều trị.",
                "situation": "onsite"
            },
            {
                "ko": "간 수치가 높게 나왔는데, 술 때문인 것 같아요. 당분간 술을 완전히 끊어야 해요.",
                "vi": "Chỉ số gan cao, có vẻ do rượu. Tạm thời phải cai rượu hoàn toàn.",
                "situation": "informal"
            }
        ],
        "relatedTerms": ["지방간", "간경변", "간염", "금주"]
    },
    {
        "slug": "ung-thu-gan",
        "korean": "간암",
        "vietnamese": "Ung thư gan",
        "hanja": "肝癌",
        "hanjaReading": "肝(간 간) + 癌(암 암)",
        "pronunciation": "간암",
        "meaningKo": "간에서 발생하는 악성 종양으로, 한국에서는 B형·C형 간염과 간경변이 주요 원인이며 예후가 좋지 않은 암입니다. 통역 시 'Ung thư gan'으로 표현하며, 조기 발견을 위해 고위험군(간염, 간경변 환자)은 6개월마다 복부 초음파와 혈액검사(AFP)가 필요함을 강조해야 합니다. 치료 방법은 병기에 따라 수술(절제술, 이식), 국소 치료(고주파열치료, 경동맥화학색전술), 전신 항암치료 등 다양하므로, 환자의 간 기능과 종양 상태를 고려한 맞춤 치료 계획을 설명하는 것이 중요합니다.",
        "meaningVi": "Khối u ác tính phát sinh ở gan. Ở Hàn Quốc nguyên nhân chính là viêm gan B, C và xơ gan, tiên lượng không tốt. Nhóm nguy cơ cao (viêm gan, xơ gan) cần siêu âm bụng và xét nghiệm máu (AFP) 6 tháng một lần để phát hiện sớm. Điều trị tùy giai đoạn: phẫu thuật, điều trị tại chỗ, hóa trị toàn thân.",
        "context": "종양내과, 간담췌내과",
        "culturalNote": "간암은 한국에서 암 사망률 2위로 매우 중요한 질환이며, B형 간염 보균자와 간경변 환자의 정기 검진이 잘 구축되어 있지만, 베트남에서는 증상 발현 후 진단되는 경우가 많아 진행된 단계에서 발견됩니다. 한국에서는 간 이식이 간암 치료의 중요한 옵션이지만, 베트남 환자에게는 생소한 개념일 수 있어 충분한 설명이 필요합니다. 고주파열치료나 경동맥화학색전술 등 국소 치료에 대한 용어가 복잡하므로, 각 치료법의 원리를 간단히 설명하면서 통역하는 것이 환자 이해도를 높입니다.",
        "commonMistakes": [
            {
                "mistake": "원발성 간암과 전이성 간암을 구분하지 않음",
                "correction": "ung thư gan nguyên phát(원발성)과 ung thư di căn gan(전이성) 구분",
                "explanation": "치료 접근이 완전히 다르므로 정확한 진단명 전달이 필수입니다"
            },
            {
                "mistake": "치료 방법을 일괄적으로 설명",
                "correction": "병기와 간 기능에 따라 치료가 다름을 설명",
                "explanation": "환자마다 적합한 치료가 다르므로 개별화된 설명이 필요합니다"
            },
            {
                "mistake": "AFP 수치만으로 간암 진단 확정",
                "correction": "영상검사(CT, MRI)로 확진 필요",
                "explanation": "AFP는 선별 검사이므로 확진을 위한 추가 검사가 필요함을 알려야 합니다"
            }
        ],
        "examples": [
            {
                "ko": "간경변이 있으시니 간암 조기 발견을 위해 6개월마다 복부 초음파를 받으셔야 합니다.",
                "vi": "Do có xơ gan nên để phát hiện sớm ung thư gan, anh/chị phải siêu âm bụng 6 tháng một lần.",
                "situation": "formal"
            },
            {
                "ko": "간암이 작고 간 기능이 좋아서 수술로 제거할 수 있을 것 같아요.",
                "vi": "Ung thư gan nhỏ và chức năng gan tốt nên có thể mổ cắt bỏ được.",
                "situation": "onsite"
            },
            {
                "ko": "B형 간염 있으면 간암 위험이 높으니까 정기 검진 꼭 받으세요.",
                "vi": "Nếu có viêm gan B thì nguy cơ ung thư gan cao nên nhất định phải khám định kỳ.",
                "situation": "informal"
            }
        ],
        "relatedTerms": ["B형간염", "C형간염", "간경변", "AFP", "고주파열치료"]
    },
    {
        "slug": "viem-gan-b",
        "korean": "B형간염",
        "vietnamese": "Viêm gan B",
        "hanja": None,
        "hanjaReading": None,
        "pronunciation": "비형간염",
        "meaningKo": "B형 간염 바이러스에 의한 간염으로, 만성화되면 간경변과 간암의 주요 원인이 되는 감염성 질환입니다. 통역 시 'Viêm gan B' 또는 'Viêm gan virus B'로 표현하며, 혈액과 체액을 통해 전파되므로 가족 내 전파 예방이 중요함을 설명해야 합니다. 한국은 신생아 예방접종이 보편화되어 젊은 층에서 감염률이 낮지만, 중장년층 보균율이 여전히 높아 정기 검진이 필요합니다. 항바이러스제 치료로 바이러스 증식을 억제할 수 있으며, 간경변·간암 예방을 위해 장기 치료가 필요한 경우가 많다는 점을 안내해야 합니다.",
        "meaningVi": "Viêm gan do virus viêm gan B, nếu mạn tính hóa là nguyên nhân chính gây xơ gan và ung thư gan. Lây qua máu và dịch cơ thể nên quan trọng phòng ngừa lây trong gia đình. Ở Hàn Quốc tiêm phòng trẻ sơ sinh phổ biến nên tỷ lệ nhiễm ở người trẻ thấp. Điều trị thuốc kháng virus có thể ức chế sao chép virus, thường cần điều trị dài hạn để phòng xơ gan, ung thư gan.",
        "context": "소화기내과, 간담췌내과",
        "culturalNote": "B형 간염은 한국과 베트남 모두 유병률이 높은 질환으로, 가족 내 보균자가 있는 경우가 많아 검사와 예방접종을 권장해야 합니다. 한국에서는 'B형간염 보균자'라는 표현을 많이 사용하는데, 이를 'người mang virus viêm gan B'로 통역하되, 보균 상태와 활동성 간염을 구분해 설명하는 것이 중요합니다. 항바이러스제 치료는 장기간 복용이 필요하지만 한국은 건강보험 적용으로 부담이 적은 반면, 베트남 환자는 비용 부담으로 치료 중단을 고려할 수 있어 한국의 보험 제도를 안내하는 것이 도움이 됩니다.",
        "commonMistakes": [
            {
                "mistake": "B형간염 보균자와 활동성 간염을 구분하지 않음",
                "correction": "người mang virus(보균자)와 viêm gan đang hoạt động(활동성) 구분",
                "explanation": "치료 필요성이 다르므로 정확한 상태를 전달해야 합니다"
            },
            {
                "mistake": "항바이러스제를 '완치' 약으로 설명",
                "correction": "바이러스 증식 억제하는 약이며 장기 복용 필요",
                "explanation": "환자가 임의로 약을 중단하지 않도록 정확한 정보를 제공해야 합니다"
            },
            {
                "mistake": "가족 검진의 중요성을 누락",
                "correction": "가족 구성원의 항체 검사와 예방접종 권장",
                "explanation": "가족 내 전파를 예방하기 위한 적극적 조치가 필요합니다"
            }
        ],
        "examples": [
            {
                "ko": "B형간염 바이러스가 검출되었으니 가족 모두 검사를 받아보시는 게 좋습니다.",
                "vi": "Phát hiện virus viêm gan B nên cả gia đình nên xét nghiệm.",
                "situation": "formal"
            },
            {
                "ko": "B형간염 있으면 술은 절대 안 되고, 6개월마다 간 검사 받아야 해요.",
                "vi": "Nếu có viêm gan B thì tuyệt đối không được uống rượu và 6 tháng một lần phải khám gan.",
                "situation": "onsite"
            },
            {
                "ko": "B형간염 항체가 없으니까 예방접종 맞으세요.",
                "vi": "Không có kháng thể viêm gan B nên hãy tiêm phòng.",
                "situation": "informal"
            }
        ],
        "relatedTerms": ["간경변", "간암", "항바이러스제", "예방접종"]
    }
])

# Part 3: Terms 21-50 (Remaining 30 terms)
new_terms.extend([
    # C형간염, 담석증, 급성췌장염, 만성췌장염, 췌장암 (5 terms)
    {"slug": "viem-gan-c", "korean": "C형간염", "vietnamese": "Viêm gan C", "hanja": None, "hanjaReading": None, "pronunciation": "씨형간염", "meaningKo": "C형 간염 바이러스에 의한 간염으로, 만성화율이 높아 간경변과 간암의 주요 원인이 되는 감염성 질환입니다. 통역 시 'Viêm gan C'로 표현하며, B형 간염과 달리 예방 백신이 없지만 항바이러스제로 완치 가능하다는 점을 강조해야 합니다. 혈액을 통해 전파되므로 침습적 시술이나 수혈 이력을 확인하는 것이 중요하며, 최근 개발된 직접작용항바이러스제(DAA)는 8-12주 복용으로 95% 이상 완치율을 보입니다. 치료 성공 후에도 간경변이 있으면 간암 발생 위험이 있어 지속적인 추적 검사가 필요함을 안내해야 합니다.", "meaningVi": "Viêm gan do virus viêm gan C, tỷ lệ mạn tính hóa cao, là nguyên nhân chính gây xơ gan và ung thư gan. Không có vắc-xin phòng ngừa nhưng có thể chữa khỏi bằng thuốc kháng virus. Lây qua máu. Thuốc kháng virus trực tiếp mới uống 8-12 tuần có tỷ lệ khỏi trên 95%. Sau điều trị thành công nếu có xơ gan vẫn phải theo dõi vì nguy cơ ung thư gan.", "context": "소화기내과, 간담췌내과", "culturalNote": "C형 간염은 한국에서 B형보다 유병률이 낮지만 수혈이나 침습적 시술을 통한 감염이 있어, 1990년대 이전 수혈 경험자나 문신·침술 경험자는 검사를 권장합니다. 베트남에서도 의료 환경이 개선되기 전 시술을 받은 경우 감염 위험이 있으므로 병력 청취 시 주의가 필요합니다. DAA 치료는 매우 효과적이지만 고가여서 베트남 환자들이 부담스러워할 수 있으나, 한국은 건강보험 적용으로 접근성이 좋다는 점을 안내하는 것이 도움이 됩니다.", "commonMistakes": [{"mistake": "B형간염과 같은 질환으로 설명", "correction": "B형은 백신 있지만 C형은 없음, 대신 C형은 완치 가능", "explanation": "두 질환의 예방과 치료 접근이 다르므로 명확히 구분해야 합니다"}, {"mistake": "완치 후 추적 검사 불필요하다고 설명", "correction": "간경변 있으면 완치 후에도 간암 검진 지속 필요", "explanation": "완치되어도 간 손상이 있으면 간암 위험이 남아있습니다"}, {"mistake": "가족 검진을 B형처럼 적극 권장", "correction": "C형은 가족 내 전파가 드물어 B형만큼 적극적이지 않음", "explanation": "불필요한 불안을 주지 않도록 전파 경로를 정확히 설명해야 합니다"}], "examples": [{"ko": "C형간염은 완치 가능한 질환으로, 8주간 약물 치료로 95% 이상 완치됩니다.", "vi": "Viêm gan C là bệnh có thể chữa khỏi, điều trị thuốc 8 tuần khỏi trên 95%.", "situation": "formal"}, {"ko": "C형간염은 예방접종이 없으니까 혈액 노출에 주의해야 해요.", "vi": "Viêm gan C không có vắc-xin nên phải cẩn thận tiếp xúc máu.", "situation": "onsite"}, {"ko": "C형간염 완치됐어도 간경변 있으면 간암 검사는 계속 받아야 해요.", "vi": "Dù viêm gan C đã khỏi nhưng nếu có xơ gan thì vẫn phải kiểm tra ung thư gan.", "situation": "informal"}], "relatedTerms": ["B형간염", "간경변", "간암", "항바이러스제"]},
    {"slug": "soi-mat", "korean": "담석증", "vietnamese": "Sỏi mật", "hanja": "膽石症", "hanjaReading": "膽(쓸개 담) + 石(돌 석) + 症(병 증)", "pronunciation": "담석증", "meaningKo": "담낭이나 담관에 결석이 생기는 질환으로, 복통, 발열, 황달 등의 증상을 유발할 수 있습니다. 통역 시 'Sỏi mật' 또는 'Sỏi túi mật'로 표현하며, 담낭 결석과 담관 결석을 구분하여 설명해야 합니다. 무증상인 경우도 많지만, 증상이 있거나 합병증(담낭염, 담관염, 췌장염) 위험이 있으면 수술(복강경 담낭절제술)을 권장합니다. 담관 결석은 ERCP로 제거할 수 있으며, 통역 시 수술과 내시경 시술의 차이를 명확히 전달하는 것이 중요합니다.", "meaningVi": "Bệnh có sỏi trong túi mật hoặc ống mật, gây đau bụng, sốt, vàng da. Cần phân biệt sỏi túi mật và sỏi ống mật. Nhiều trường hợp không có triệu chứng nhưng nếu có triệu chứng hoặc nguy cơ biến chứng (viêm túi mật, viêm ống mật, viêm tụy) thì khuyến cáo mổ nội soi cắt túi mật. Sỏi ống mật có thể lấy bằng ERCP.", "context": "소화기내과, 외과", "culturalNote": "담석증은 한국에서 식습관 서구화로 증가 추세이며, 복부 초음파 보급으로 무증상 담석 발견이 많아졌습니다. 베트남에서도 경제 발전과 함께 발생률이 증가하고 있습니다. 한국 환자들은 '수술'이라는 단어에 부담을 느끼지만 복강경 수술은 회복이 빠르다는 점을 강조하면 도움이 됩니다. 베트남 환자들은 전통적으로 한약이나 민간요법으로 담석을 녹이려는 시도를 하는 경우가 있는데, 효과가 입증되지 않았으므로 의학적 치료의 필요성을 설명해야 합니다.", "commonMistakes": [{"mistake": "담낭 결석과 담관 결석을 구분하지 않음", "correction": "sỏi túi mật(담낭)과 sỏi ống mật(담관) 명확히 구분", "explanation": "치료 방법이 다르므로 정확한 위치를 전달해야 합니다"}, {"mistake": "무증상 담석도 무조건 수술 권장", "correction": "증상이 있거나 합병증 위험 있을 때 수술", "explanation": "과도한 치료를 피하고 적절한 적응증을 설명해야 합니다"}, {"mistake": "담석을 약으로 녹일 수 있다고 설명", "correction": "약물로 용해는 제한적, 주 치료는 수술", "explanation": "환자가 비효과적인 치료에 시간을 낭비하지 않도록 해야 합니다"}], "examples": [{"ko": "담낭에 결석이 있고 통증이 반복되므로 복강경 담낭절제술을 권합니다.", "vi": "Có sỏi trong túi mật và đau tái đi tái lại nên khuyến cáo mổ nội soi cắt túi mật.", "situation": "formal"}, {"ko": "담관에 돌이 있어서 ERCP로 제거하고 담낭은 나중에 수술할게요.", "vi": "Có sỏi ở ống mật nên sẽ lấy bằng ERCP, túi mật mổ sau.", "situation": "onsite"}, {"ko": "담석 있어도 아프지 않으면 굳이 수술 안 해도 돼요.", "vi": "Có sỏi mật nhưng không đau thì không nhất thiết phải mổ.", "situation": "informal"}], "relatedTerms": ["담낭염", "담관염", "ERCP", "복강경수술"]},
    {"slug": "viem-tuy-cap", "korean": "급성췌장염", "vietnamese": "Viêm tụy cấp", "hanja": "急性膵臟炎", "hanjaReading": "急(급할 급) + 性(성품 성) + 膵(이자 췌) + 臟(장부 장) + 炎(불꽃 염)", "pronunciation": "급성췌장염", "meaningKo": "췌장에 급성 염증이 발생하여 심한 복통, 구토, 발열 등을 유발하는 응급 질환으로, 담석과 알코올이 주요 원인입니다. 통역 시 'Viêm tụy cấp'으로 표현하며, 상복부 통증이 등으로 방사되는 특징적인 양상을 설명해야 합니다. 중증도에 따라 경증은 보존적 치료(금식, 수액)로 회복되지만, 중증은 췌장 괴사와 다장기 부전으로 진행하여 사망률이 높으므로 신속한 진단과 치료가 필수적입니다. 원인 제거(담석 제거, 금주)가 재발 방지에 중요하며, 통역 시 이를 강조해야 합니다.", "meaningVi": "Bệnh viêm cấp tính ở tụy gây đau bụng dữ dội, nôn, sốt, là tình trạng cấp cứu. Nguyên nhân chính là sỏi mật và rượu. Đặc trưng là đau thượng vị lan ra lưng. Tùy mức độ nặng: nhẹ thì điều trị bảo tồn (nhịn ăn, truyền dịch) có thể khỏi, nặng thì hoại tử tụy và suy đa tạng, tỷ lệ tử vong cao nên cần chẩn đoán và điều trị nhanh. Loại bỏ nguyên nhân quan trọng để phòng tái phát.", "context": "응급의학, 소화기내과", "culturalNote": "급성췌장염은 한국에서 알코올과 담석이 양대 원인이며, 음주 문화와 관련이 깊어 환자 교육 시 금주를 강조해야 합니다. 베트남 환자들도 음주가 흔한 원인이므로 문화적 맥락을 고려하되 의학적 필요성을 명확히 전달해야 합니다. 중증 췌장염은 중환자실 치료가 필요하고 비용이 많이 들 수 있어, 환자 가족에게 질환의 심각성과 치료 계획을 충분히 설명하는 것이 중요합니다. ERCP 후 합병증으로 발생할 수도 있으므로, 시술 전 동의서 작성 시 이를 정확히 통역해야 합니다.", "commonMistakes": [{"mistake": "단순 복통으로 설명하여 응급성 간과", "correction": "생명을 위협할 수 있는 응급 질환임을 강조", "explanation": "환자와 가족이 질환의 심각성을 이해해야 적절한 치료가 가능합니다"}, {"mistake": "원인을 찾지 않고 증상만 치료", "correction": "담석이나 알코올 등 원인 규명과 제거 필수", "explanation": "원인 제거 없이는 재발 위험이 높습니다"}, {"mistake": "경증과 중증을 구분하지 않음", "correction": "경증(nhẹ)과 중증(nặng)의 예후와 치료 차이 설명", "explanation": "환자의 예후에 대한 현실적 기대를 설정해야 합니다"}], "examples": [{"ko": "급성췌장염으로 입원하셨으니 금식하시고 수액 치료를 받으셔야 합니다.", "vi": "Do viêm tụy cấp nên phải nhập viện, nhịn ăn và truyền dịch điều trị.", "situation": "formal"}, {"ko": "췌장염은 술 때문인 것 같은데, 앞으로 절대 금주하셔야 해요.", "vi": "Viêm tụy có vẻ do rượu, sau này tuyệt đối phải cai rượu.", "situation": "onsite"}, {"ko": "췌장염 심하면 중환자실 가야 할 수도 있어요.", "vi": "Nếu viêm tụy nặng có thể phải vào ICU.", "situation": "informal"}], "relatedTerms": ["담석증", "알코올", "ERCP", "복통"]},
    {"slug": "viem-tuy-man-tinh", "korean": "만성췌장염", "vietnamese": "Viêm tụy mạn tính", "hanja": "慢性膵臟炎", "hanjaReading": "慢(느릴 만) + 性(성품 성) + 膵(이자 췌) + 臟(장부 장) + 炎(불꽃 염)", "pronunciation": "만성췌장염", "meaningKo": "췌장의 지속적인 염증으로 인해 췌장 조직이 파괴되고 섬유화가 진행되는 질환으로, 만성 복통과 췌장 기능 저하가 특징입니다. 통역 시 'Viêm tụy mạn tính'으로 표현하며, 장기간 음주가 가장 흔한 원인임을 설명해야 합니다. 췌장의 외분비 기능 저하로 소화 장애와 지방변이 나타나고, 내분비 기능 저하로 당뇨병이 발생할 수 있으므로, 췌장효소 보충과 혈당 관리가 필요함을 안내해야 합니다. 금주가 질환 진행을 막는 가장 중요한 치료이며, 통증 관리와 영양 지원도 필수적임을 강조하는 것이 중요합니다.", "meaningVi": "Bệnh viêm kéo dài ở tụy khiến mô tụy bị phá hủy và xơ hóa tiến triển, đặc trưng là đau bụng mạn tính và suy giảm chức năng tụy. Nguyên nhân thường gặp nhất là uống rượu lâu ngày. Suy giảm chức năng ngoại tiết gây rối loạn tiêu hóa và phân mỡ, suy giảm chức năng nội tiết gây đái tháo đường nên cần bổ sung enzyme tụy và quản lý đường huyết. Cai rượu là điều trị quan trọng nhất để ngăn bệnh tiến triển.", "context": "소화기내과, 간담췌내과", "culturalNote": "만성췌장염은 한국에서 알코올성이 대부분이며, 환자들이 금주의 중요성을 이해하면서도 실천하기 어려워하는 경우가 많아 지속적인 교육과 지지가 필요합니다. 베트남에서도 음주 문화가 있어 금주 권고 시 문화적 맥락을 고려해야 합니다. 췌장효소 보충제는 식사 시마다 복용해야 하는데, 환자들이 번거로워하거나 비용 부담으로 중단하는 경우가 있어 복용의 중요성을 반복 설명해야 합니다. 만성 통증으로 인한 마약성 진통제 의존 위험도 있어, 통증 관리 계획을 신중히 설명하는 것이 필요합니다.", "commonMistakes": [{"mistake": "급성췌장염과 혼동하여 설명", "correction": "급성은 일시적, 만성은 지속적 손상으로 구분", "explanation": "치료 목표와 예후가 다르므로 명확히 구분해야 합니다"}, {"mistake": "금주만 강조하고 췌장효소 보충 누락", "correction": "금주와 함께 췌장효소 보충, 당뇨 관리 필요", "explanation": "췌장 기능 저하에 대한 대체 치료가 삶의 질에 중요합니다"}, {"mistake": "완치 가능한 질환으로 설명", "correction": "비가역적 손상이지만 진행 억제 가능", "explanation": "현실적인 치료 목표를 설정하도록 도와야 합니다"}], "examples": [{"ko": "만성췌장염은 금주와 췌장효소 복용으로 증상을 조절할 수 있습니다.", "vi": "Viêm tụy mạn tính có thể kiểm soát triệu chứng bằng cai rượu và uống enzyme tụy.", "situation": "formal"}, {"ko": "지방변이 나오는 건 췌장 기능이 떨어져서 그래요. 효소제를 먹어야 해요.", "vi": "Phân mỡ là do chức năng tụy giảm. Phải uống thuốc enzyme.", "situation": "onsite"}, {"ko": "만성췌장염 있으면 당뇨 올 수 있으니까 혈당 체크 자주 하세요.", "vi": "Nếu có viêm tụy mạn tính có thể bị đái tháo đường nên hay kiểm tra đường huyết.", "situation": "informal"}], "relatedTerms": ["급성췌장염", "당뇨병", "알코올", "췌장효소"]},
    {"slug": "ung-thu-tuy", "korean": "췌장암", "vietnamese": "Ung thư tụy", "hanja": "膵臟癌", "hanjaReading": "膵(이자 췌) + 臟(장부 장) + 癌(암 암)", "pronunciation": "췌장암", "meaningKo": "췌장에서 발생하는 악성 종양으로, 초기 증상이 거의 없어 진행된 상태에서 발견되는 경우가 많고 예후가 매우 불량한 암입니다. 통역 시 'Ung thư tụy'로 표현하며, 황달, 체중 감소, 복통 등이 나타날 때는 이미 진행된 경우가 많음을 설명해야 합니다. 수술적 절제가 가능한 경우는 20% 정도이며, 대부분 항암화학요법이나 완화 치료를 받게 되므로, 환자와 가족에게 현실적인 예후를 신중하게 전달하는 것이 중요합니다. 담관 폐쇄로 인한 황달이 있으면 스텐트 삽입 등 완화 시술이 필요할 수 있음을 안내해야 합니다.", "meaningVi": "Khối u ác tính phát sinh ở tụy, giai đoạn đầu hầu như không có triệu chứng nên thường phát hiện khi đã tiến triển, tiên lượng rất xấu. Khi có vàng da, sụt cân, đau bụng thường đã tiến triển. Chỉ khoảng 20% có thể mổ cắt, phần lớn điều trị hóa chất hoặc điều trị giảm nhẹ. Nếu có vàng da do tắc ống mật thì có thể cần đặt stent giảm nhẹ.", "context": "종양내과, 소화기내과", "culturalNote": "췌장암은 한국에서 '암 중의 암'으로 인식될 정도로 예후가 나쁜 질환이며, 환자와 가족에게 나쁜 소식을 전달할 때 문화적 맥락을 고려해야 합니다. 베트남 문화에서도 암 진단은 매우 충격적이므로, 통역 시 의료진의 어조와 환자의 반응을 세심하게 관찰하며 전달해야 합니다. 완화 치료나 호스피스에 대한 개념이 베트남에서는 덜 보편화되어 있을 수 있어, 이를 설명할 때 '포기'가 아닌 '증상 완화와 삶의 질 향상'에 초점을 맞춰 통역하는 것이 중요합니다.", "commonMistakes": [{"mistake": "예후를 지나치게 긍정적으로 설명", "correction": "현실적인 예후를 신중하게 전달", "explanation": "환자와 가족이 현실적인 계획을 세울 수 있도록 정직한 정보가 필요합니다"}, {"mistake": "완화 치료를 '치료 포기'로 표현", "correction": "증상 완화와 삶의 질 향상을 위한 적극적 치료로 설명", "explanation": "완화 치료의 가치를 환자가 이해하도록 도와야 합니다"}, {"mistake": "수술 불가능한 이유를 설명하지 않음", "correction": "전이나 주요 혈관 침범 등 구체적 이유 설명", "explanation": "환자가 치료 결정을 이해하고 수용하도록 도와야 합니다"}], "examples": [{"ko": "췌장암이 주변 혈관을 침범하여 수술이 어렵습니다. 항암치료를 고려하겠습니다.", "vi": "Ung thư tụy đã xâm lấn mạch máu xung quanh nên khó mổ. Sẽ xem xét hóa trị.", "situation": "formal"}, {"ko": "황달이 심해서 담관 스텐트를 넣어서 증상을 완화시키겠습니다.", "vi": "Vàng da nặng nên sẽ đặt stent ống mật để giảm nhẹ triệu chứng.", "situation": "onsite"}, {"ko": "췌장암은 안타깝게도 예후가 좋지 않은 암이에요.", "vi": "Rất tiếc nhưng ung thư tụy là ung thư có tiên lượng không tốt.", "situation": "informal"}], "relatedTerms": ["황달", "체중감소", "항암치료", "완화치료"]},

    # 요로결석, 방광염, 신우신염, 전립선비대증, 전립선암 (5 terms)
    {"slug": "soi-duong-tiet-nieu", "korean": "요로결석", "vietnamese": "Sỏi đường tiết niệu", "hanja": "尿路結石", "hanjaReading": "尿(오줌 뇨) + 路(길 로) + 結(맺을 결) + 石(돌 석)", "pronunciation": "요로결석", "meaningKo": "신장, 요관, 방광, 요도 등 요로계에 결석이 생기는 질환으로, 심한 옆구리 통증과 혈뇨가 특징적입니다. 통역 시 'Sỏi đường tiết niệu'로 표현하며, 결석의 위치(신장, 요관 등)에 따라 증상과 치료가 다름을 설명해야 합니다. 작은 결석은 자연 배출을 기다리며 수액과 진통제로 보존적 치료를 하지만, 큰 결석이나 감염 동반 시 체외충격파쇄석술이나 내시경 시술이 필요합니다. 재발률이 높아 수분 섭취 증가와 식이 조절의 중요성을 강조해야 하며, 결석 성분 분석 후 맞춤 예방법을 안내하는 것이 중요합니다.", "meaningVi": "Bệnh có sỏi trong hệ tiết niệu như thận, niệu quản, bàng quang, niệu đạo, đặc trưng là đau sườn dữ dội và tiểu ra máu. Tùy vị trí sỏi mà triệu chứng và điều trị khác nhau. Sỏi nhỏ chờ tự đào thải bằng điều trị bảo tồn với truyền dịch và giảm đau, sỏi lớn hoặc kèm nhiễm trùng cần tán sỏi ngoài cơ thể hoặc thủ thuật nội soi. Tái phát cao nên quan trọng là uống nhiều nước và điều chỉnh chế độ ăn.", "context": "비뇨의학과", "culturalNote": "요로결석은 한국에서 여름철 탈수와 관련이 깊어 수분 섭취를 강조하는데, 베트남은 더운 기후로 발생 위험이 높을 수 있습니다. 한국 환자들은 '옆구리 통증'을 특징적 증상으로 인식하지만, 베트남 환자는 이 표현이 생소할 수 있어 '허리 옆쪽(sườn lưng)' 등으로 구체적으로 설명하는 것이 좋습니다. 체외충격파쇄석술은 비침습적 치료로 회복이 빠르지만, 베트남 환자들에게는 생소한 치료법일 수 있어 원리와 장점을 충분히 설명해야 합니다.", "commonMistakes": [{"mistake": "모든 요로결석을 신장결석으로 통역", "correction": "sỏi thận(신장), sỏi niệu quản(요관), sỏi bàng quang(방광) 구분", "explanation": "위치에 따라 치료와 증상이 다르므로 정확한 부위를 전달해야 합니다"}, {"mistake": "결석 크기를 대략적으로만 통역", "correction": "밀리미터 단위로 정확히 전달", "explanation": "크기가 치료 방법 결정에 중요한 요소입니다"}, {"mistake": "예방법을 막연히 '물 많이 마시기'로만 설명", "correction": "하루 2리터 이상, 결석 성분별 식이 조절 구체적 설명", "explanation": "실천 가능한 구체적 지침을 제공해야 재발 예방 효과가 있습니다"}], "examples": [{"ko": "요관에 7mm 결석이 있어서 체외충격파쇄석술로 치료하겠습니다.", "vi": "Có sỏi 7mm ở niệu quản nên sẽ điều trị bằng tán sỏi ngoài cơ thể.", "situation": "formal"}, {"ko": "결석이 작아서 물 많이 마시면서 빠져나오기를 기다려봐요.", "vi": "Sỏi nhỏ nên uống nhiều nước rồi chờ tự đào thải.", "situation": "onsite"}, {"ko": "요로결석은 재발 잘 하니까 하루에 물 2리터 이상 드세요.", "vi": "Sỏi đường tiết niệu hay tái phát nên mỗi ngày uống trên 2 lít nước.", "situation": "informal"}], "relatedTerms": ["혈뇨", "옆구리통증", "체외충격파쇄석술", "내시경"]},
    {"slug": "viem-bang-quang", "korean": "방광염", "vietnamese": "Viêm bàng quang", "hanja": "膀胱炎", "hanjaReading": "膀(방광 방) + 胱(방광 광) + 炎(불꽃 염)", "pronunciation": "방광염", "meaningKo": "방광에 세균 감염으로 염증이 생기는 질환으로, 빈뇨, 배뇨통, 하복부 불편감이 주 증상이며 여성에게 흔합니다. 통역 시 'Viêm bàng quang'으로 표현하며, 요도가 짧은 여성의 해부학적 특성상 감염이 쉽다는 점을 설명해야 합니다. 대부분 항생제로 치료되지만, 재발이 잦으면 원인 규명(성생활, 위생 습관 등)이 필요하며, 소변 배양 검사로 원인균과 항생제 감수성을 확인하는 것이 중요합니다. 방광염이 신우신염으로 진행하지 않도록 조기 치료가 필요하며, 발열이나 옆구리 통증이 생기면 즉시 재진을 권고해야 합니다.", "meaningVi": "Bệnh viêm bàng quang do nhiễm khuẩn, triệu chứng chính là tiểu gấp, đau khi đi tiểu, khó chịu hạ vị, thường gặp ở nữ giới. Do niệu đạo ngắn nên nữ giới dễ nhiễm trùng. Phần lớn điều trị bằng kháng sinh nhưng nếu tái phát thường xuyên cần tìm nguyên nhân (sinh hoạt tình dục, vệ sinh). Cần điều trị sớm để không tiến triển thành viêm thận bể thận, nếu có sốt hoặc đau sườn phải tái khám ngay.", "context": "비뇨의학과", "culturalNote": "방광염은 한국 여성들에게 매우 흔한 질환으로 환자들이 'ở bàng quang(방광 부위)'이라는 표현보다 '아래 배(hạ vị)'라는 증상 표현에 익숙합니다. 베트남 여성들도 방광염을 경험하지만, 문화적으로 성생활이나 위생 습관에 대해 말하기 꺼려할 수 있어 병력 청취 시 민감하게 접근해야 합니다. 한국에서는 약국에서 쉽게 항생제를 구할 수 있었던 과거와 달리 현재는 처방이 필요하지만, 베트남에서는 여전히 자가 치료하는 경우가 있어 적절한 항생제 사용의 중요성을 강조해야 합니다.", "commonMistakes": [{"mistake": "신우신염과 방광염을 구분하지 않음", "correction": "방광염은 발열 없고 하부 증상만, 신우신염은 발열과 옆구리 통증", "explanation": "치료 강도가 다르므로 정확한 진단명 전달이 필요합니다"}, {"mistake": "재발성 방광염의 원인을 찾지 않음", "correction": "성생활, 위생, 폐경 등 원인 규명 필요", "explanation": "재발 예방을 위해 원인 파악이 중요합니다"}, {"mistake": "증상 호전 시 항생제 중단 권장", "correction": "처방된 기간 동안 완전히 복용 필요", "explanation": "항생제 내성을 막고 완전한 치료를 위해 복용 완료가 필수입니다"}], "examples": [{"ko": "방광염으로 진단되어 항생제 3일 처방해드립니다. 끝까지 드세요.", "vi": "Chẩn đoán viêm bàng quang, kê kháng sinh 3 ngày. Uống hết đấy nhé.", "situation": "formal"}, {"ko": "소변 볼 때 아프고 자주 마려운 게 방광염 증상이에요.", "vi": "Đau khi tiểu và hay buồn tiểu là triệu chứng viêm bàng quang.", "situation": "onsite"}, {"ko": "방광염 자주 생기면 성관계 후 바로 소변 보는 게 도움돼요.", "vi": "Nếu hay bị viêm bàng quang thì sau quan hệ đi tiểu ngay sẽ có ích.", "situation": "informal"}], "relatedTerms": ["신우신염", "빈뇨", "배뇨통", "항생제"]},
    {"slug": "viem-than-be-than", "korean": "신우신염", "vietnamese": "Viêm thận bể thận", "hanja": "腎盂腎炎", "hanjaReading": "腎(콩팥 신) + 盂(동이 우) + 腎(콩팥 신) + 炎(불꽃 염)", "pronunciation": "신우신염", "meaningKo": "신장과 신우(신장의 깔때기 모양 부분)에 세균 감염이 발생하는 질환으로, 발열, 오한, 옆구리 통증이 특징적이며 방광염보다 심각합니다. 통역 시 'Viêm thận bể thận' 또는 'Viêm bể thận'으로 표현하며, 방광염의 상행 감염으로 발생하는 경우가 많음을 설명해야 합니다. 입원 치료와 정맥 항생제가 필요한 경우가 많으며, 치료가 지연되면 패혈증이나 신농양 등 심각한 합병증이 발생할 수 있으므로 조기 치료의 중요성을 강조해야 합니다. 재발성인 경우 요로 기형이나 결석 등 구조적 이상을 확인하는 검사가 필요함을 안내하는 것이 중요합니다.", "meaningVi": "Bệnh nhiễm khuẩn ở thận và bể thận, đặc trưng là sốt, ớn lạnh, đau sườn, nặng hơn viêm bàng quang. Thường do viêm bàng quang lan lên. Nhiều trường hợp cần nhập viện điều trị kháng sinh tĩnh mạch. Nếu điều trị chậm có thể gây biến chứng nặng như nhiễm trùng huyết hoặc áp xe thận. Nếu tái phát cần kiểm tra dị tật đường tiết niệu hoặc sỏi.", "context": "비뇨의학과, 감염내과", "culturalNote": "신우신염은 한국에서 입원 치료가 필요한 경우가 많은데, 베트남 환자들은 입원을 부담스러워할 수 있어 질환의 심각성을 충분히 설명해야 합니다. 옆구리 통증을 'đau sườn' 또는 'đau lưng bên'으로 표현하는데, 환자가 통증 부위를 정확히 전달하도록 도와야 합니다. 패혈증으로 진행할 수 있는 위험한 감염이므로, '단순 염증'으로 과소평가하지 않도록 주의해야 합니다. 재발성 신우신염 환자는 영상 검사(초음파, CT)로 구조적 이상을 확인해야 하는데, 검사 필요성을 설득하는 것이 중요합니다.", "commonMistakes": [{"mistake": "방광염과 같은 수준으로 설명", "correction": "더 심각한 감염으로 입원 치료 필요할 수 있음", "explanation": "환자가 질환의 심각성을 이해하고 적절한 치료를 받도록 해야 합니다"}, {"mistake": "경구 항생제만으로 치료 가능하다고 설명", "correction": "증상에 따라 입원하여 정맥 항생제 필요", "explanation": "치료 강도의 필요성을 환자가 이해해야 합니다"}, {"mistake": "열이 내리면 치료 완료로 설명", "correction": "항생제를 처방 기간 동안 완전히 복용 필요", "explanation": "재발과 항생제 내성을 막기 위해 완전한 치료가 필수입니다"}], "examples": [{"ko": "신우신염으로 입원하셔서 정맥 항생제 치료를 받으셔야 합니다.", "vi": "Do viêm thận bể thận nên phải nhập viện điều trị kháng sinh tĩnh mạch.", "situation": "formal"}, {"ko": "열이 나고 옆구리가 아프면 신우신염일 수 있으니 빨리 병원 가세요.", "vi": "Nếu sốt và đau sườn thì có thể là viêm thận bể thận, hãy đến bệnh viện nhanh.", "situation": "onsite"}, {"ko": "신우신염은 방광염보다 심각해서 입원이 필요할 수도 있어요.", "vi": "Viêm thận bể thận nặng hơn viêm bàng quang nên có thể cần nhập viện.", "situation": "informal"}], "relatedTerms": ["방광염", "발열", "옆구리통증", "항생제"]},
    {"slug": "pho-dai-tuyen-tien-liet", "korean": "전립선비대증", "vietnamese": "Phì đại tuyến tiền liệt", "hanja": "前立腺肥大症", "hanjaReading": "前(앞 전) + 立(설 립) + 腺(샘 선) + 肥(살찔 비) + 大(큰 대) + 症(병 증)", "pronunciation": "전립선비대증", "meaningKo": "전립선이 커져서 요도를 압박하여 배뇨 장애를 일으키는 질환으로, 중년 이후 남성에게 흔합니다. 통역 시 'Phì đại tuyến tiền liệt' 또는 'Phì đại tiền liệt tuyến'으로 표현하며, 빈뇨, 약뇨, 잔뇨감 등의 증상을 설명해야 합니다. 양성 질환이지만 삶의 질을 저하시키므로, 증상 정도에 따라 약물 치료나 수술(경요도전립선절제술 등)을 고려합니다. 전립선암과는 다른 질환이지만 감별을 위해 PSA 검사가 필요하며, 급성 요폐 등 합병증 발생 시 응급 처치가 필요함을 안내해야 합니다.", "meaningVi": "Bệnh tuyến tiền liệt to lên chèn ép niệu đạo gây rối loạn tiểu tiện, thường gặp ở nam giới trung niên trở lên. Triệu chứng: tiểu gấp, nước tiểu yếu, cảm giác tiểu không hết. Là bệnh lành tính nhưng ảnh hưởng chất lượng cuộc sống. Tùy mức độ điều trị thuốc hoặc phẫu thuật. Khác với ung thư tiền liệt tuyến nhưng cần xét nghiệm PSA để phân biệt. Nếu xảy ra bí tiểu cấp cần xử trí cấp cứu.", "context": "비뇨의학과", "culturalNote": "전립선비대증은 한국 중장년 남성들에게 매우 흔한 질환으로 'BPH'라는 약어도 많이 사용되지만, 베트남 환자에게는 'tuyến tiền liệt'이라는 용어 자체가 생소할 수 있어 '방광 아래 남성 샘(tuyến ở dưới bàng quang của nam giới)' 등으로 설명하면 이해를 돕습니다. 한국 남성들은 배뇨 증상을 나이 탓으로 여기며 병원 방문을 미루는 경향이 있는데, 베트남 남성들도 비슷한 경향이 있어 조기 진료의 중요성을 강조해야 합니다. 수술에 대한 두려움이 큰데, 최소침습 수술의 발전을 설명하면 도움이 됩니다.", "commonMistakes": [{"mistake": "전립선암과 혼동하여 설명", "correction": "양성 질환임을 명확히, PSA로 암 감별", "explanation": "환자에게 불필요한 불안을 주지 않도록 양성 질환임을 강조해야 합니다"}, {"mistake": "증상을 노화 현상으로 치부", "correction": "치료 가능한 질환으로 삶의 질 개선 가능", "explanation": "환자가 치료를 포기하지 않도록 개선 가능성을 전달해야 합니다"}, {"mistake": "약물과 수술 중 하나만 제시", "correction": "증상 정도에 따라 치료 옵션 다양함을 설명", "explanation": "환자가 자신의 상황에 맞는 치료를 선택할 수 있도록 정보를 제공해야 합니다"}], "examples": [{"ko": "전립선비대증으로 배뇨 장애가 있으시니 약물 치료를 시작하겠습니다.", "vi": "Do phì đại tuyến tiền liệt có rối loạn tiểu tiện nên sẽ bắt đầu điều trị thuốc.", "situation": "formal"}, {"ko": "소변 줄기가 약하고 자주 마려우면 전립선비대증일 수 있어요.", "vi": "Nếu nước tiểu yếu và hay buồn tiểu thì có thể là phì đại tuyến tiền liệt.", "situation": "onsite"}, {"ko": "전립선비대증은 암이 아니니까 걱정 안 하셔도 돼요.", "vi": "Phì đại tuyến tiền liệt không phải ung thư nên đừng lo.", "situation": "informal"}], "relatedTerms": ["빈뇨", "배뇨장애", "PSA", "전립선암"]},
    {"slug": "ung-thu-tuyen-tien-liet", "korean": "전립선암", "vietnamese": "Ung thư tuyến tiền liệt", "hanja": "前立腺癌", "hanjaReading": "前(앞 전) + 立(설 립) + 腺(샘 선) + 癌(암 암)", "pronunciation": "전립선암", "meaningKo": "전립선에서 발생하는 악성 종양으로, 진행이 느려 초기에는 증상이 거의 없으며 PSA 검사로 조기 발견이 가능합니다. 통역 시 'Ung thư tuyến tiền liệt' 또는 'Ung thư tiền liệt tuyến'으로 표현하며, 50세 이상 남성의 정기 PSA 검사 권장 사항을 설명해야 합니다. 조기 발견 시 수술이나 방사선 치료로 완치율이 높지만, 진행된 경우 호르몬 치료나 항암치료가 필요합니다. 글리슨 점수와 병기에 따라 치료 방침이 달라지므로, 환자의 나이와 전반적 건강 상태를 고려한 맞춤 치료 계획을 설명하는 것이 중요합니다.", "meaningVi": "Khối u ác tính phát sinh ở tuyến tiền liệt, tiến triển chậm, giai đoạn đầu hầu như không có triệu chứng, có thể phát hiện sớm bằng xét nghiệm PSA. Khuyến cáo nam giới trên 50 tuổi xét nghiệm PSA định kỳ. Nếu phát hiện sớm, mổ hoặc xạ trị có tỷ lệ khỏi cao. Giai đoạn tiến triển cần điều trị hormone hoặc hóa trị. Tùy điểm Gleason và giai đoạn mà quyết định điều trị, cần xem xét tuổi và sức khỏe tổng thể.", "context": "비뇨의학과, 종양내과", "culturalNote": "전립선암은 한국에서 고령화와 함께 증가하는 암으로, PSA 검사가 건강검진에 포함되어 조기 발견이 늘었습니다. 베트남에서는 아직 일반적인 검진 항목이 아니어서 환자들에게 생소할 수 있습니다. 한국 남성들은 수술 후 발기부전이나 요실금 등 부작용을 매우 우려하는데, 베트남 남성들도 비슷한 우려가 있어 치료 전 충분한 상담이 필요합니다. 진행이 느린 암이므로 '적극적 감시(active surveillance)'라는 선택지도 있는데, 이를 '치료 안 함'으로 오해하지 않도록 설명이 필요합니다.", "commonMistakes": [{"mistake": "PSA 상승을 곧바로 암으로 진단", "correction": "PSA 상승 원인 다양, 조직검사로 확진", "explanation": "환자에게 불필요한 불안을 주지 않도록 검사 단계를 정확히 설명해야 합니다"}, {"mistake": "모든 전립선암에 즉시 수술 권장", "correction": "글리슨 점수, 병기, 나이 고려한 맞춤 치료", "explanation": "저위험군은 적극적 감시도 옵션이므로 과잉 치료를 피해야 합니다"}, {"mistake": "수술 부작용을 과소평가", "correction": "발기부전, 요실금 등 부작용 가능성 정직하게 설명", "explanation": "환자가 informed decision을 내릴 수 있도록 정직한 정보 제공이 필요합니다"}], "examples": [{"ko": "PSA가 높게 나와서 전립선 조직검사를 권유드립니다.", "vi": "PSA cao nên khuyến cáo sinh thiết tuyến tiền liệt.", "situation": "formal"}, {"ko": "전립선암 조기라서 수술하면 완치율이 90% 이상이에요.", "vi": "Ung thư tuyến tiền liệt giai đoạn sớm nên nếu mổ tỷ lệ khỏi trên 90%.", "situation": "onsite"}, {"ko": "50세 넘으면 PSA 검사로 전립선암 검진 받는 게 좋아요.", "vi": "Sau 50 tuổi nên xét nghiệm PSA để sàng lọc ung thư tuyến tiền liệt.", "situation": "informal"}], "relatedTerms": ["PSA", "전립선비대증", "조직검사", "호르몬치료"]},
])

# Final 20 terms: 방광암, 신장암, 요실금, 발기부전, 정계정맥류, 고환암, 포경수술, 급성신부전, 만성신부전, 사구체신염,
# 신증후군, 신장이식, 투석혈관접근로, 복막투석카테터, 요독증, 전해질불균형, 대사성산증, 고칼륨혈증, 저나트륨혈증, 신장생검
new_terms.extend([
    {"slug": "ung-thu-bang-quang", "korean": "방광암", "vietnamese": "Ung thư bàng quang", "hanja": "膀胱癌", "hanjaReading": "膀(방광 방) + 胱(방광 광) + 癌(암 암)", "pronunciation": "방광암", "meaningKo": "방광에서 발생하는 악성 종양으로, 혈뇨가 가장 흔한 증상이며 흡연이 주요 위험인자입니다. 통역 시 'Ung thư bàng quang'으로 표현하며, 통증 없는 혈뇨가 특징적임을 강조해야 합니다. 조기 발견 시 경요도방광종양절제술로 치료 가능하지만, 재발률이 높아 정기적인 방광경 검사가 필수적입니다. 근침윤성 방광암은 방광 전절제술이 필요할 수 있으며, 수술 후 요로 재건 방법을 환자와 상의해야 합니다.", "meaningVi": "Khối u ác tính phát sinh ở bàng quang, triệu chứng thường gặp nhất là tiểu ra máu, yếu tố nguy cơ chính là hút thuốc. Đặc trưng là tiểu ra máu không đau. Nếu phát hiện sớm có thể điều trị bằng cắt u bàng quang qua niệu đạo nhưng tái phát cao nên cần nội soi bàng quang định kỳ. Ung thư xâm lấn cơ thì có thể phải cắt toàn bộ bàng quang.", "context": "비뇨의학과, 종양내과", "culturalNote": "방광암은 한국에서 흡연과 밀접한 관련이 있어 금연 교육이 중요하며, 베트남도 흡연율이 높아 위험군이 많습니다. 통증 없는 혈뇨를 대수롭지 않게 여기는 경우가 많아, 혈뇨 발생 시 즉시 검사받아야 함을 강조해야 합니다. 방광 전절제술 후 인공 방광이나 요루 조성술에 대한 설명이 필요한데, 문화적으로 민감한 주제이므로 신중한 접근이 필요합니다.", "commonMistakes": [{"mistake": "혈뇨를 방광염으로만 설명", "correction": "통증 없는 혈뇨는 방광암 의심, 반드시 검사 필요", "explanation": "조기 진단을 놓치지 않도록 혈뇨의 의미를 정확히 전달해야 합니다"}, {"mistake": "재발 가능성을 과소평가", "correction": "재발률 높아 정기 방광경 검사 필수", "explanation": "환자가 추적 검사의 중요성을 이해하도록 해야 합니다"}, {"mistake": "흡연과의 연관성을 언급하지 않음", "correction": "금연이 예방과 재발 방지에 중요", "explanation": "예방 가능한 위험인자를 제거하도록 교육해야 합니다"}], "examples": [{"ko": "혈뇨가 나왔으니 방광암 가능성을 확인하기 위해 방광경 검사가 필요합니다.", "vi": "Có tiểu ra máu nên cần nội soi bàng quang để xác định khả năng ung thư bàng quang.", "situation": "formal"}, {"ko": "방광암 수술 후에도 재발 확인을 위해 3개월마다 방광경 검사 받으셔야 해요.", "vi": "Sau mổ ung thư bàng quang vẫn phải nội soi 3 tháng một lần để kiểm tra tái phát.", "situation": "onsite"}, {"ko": "담배 피우면 방광암 위험이 높아지니까 꼭 끊으세요.", "vi": "Hút thuốc tăng nguy cơ ung thư bàng quang nên nhất định phải cai.", "situation": "informal"}], "relatedTerms": ["혈뇨", "방광경", "흡연", "경요도수술"]},
    {"slug": "ung-thu-than", "korean": "신장암", "vietnamese": "Ung thư thận", "hanja": "腎臟癌", "hanjaReading": "腎(콩팥 신) + 臟(장부 장) + 癌(암 암)", "pronunciation": "신장암", "meaningKo": "신장에서 발생하는 악성 종양으로, 초기에는 증상이 없어 건강검진에서 우연히 발견되는 경우가 많습니다. 통역 시 'Ung thư thận'으로 표현하며, 혈뇨, 옆구리 종괴, 통증이 고전적 3대 증상이지만 이 증상이 모두 나타나면 이미 진행된 경우가 많음을 설명해야 합니다. 수술적 절제가 주 치료이며, 조기 발견 시 부분 신절제술로 신기능을 보존할 수 있습니다. 전이성 신장암은 표적치료제나 면역치료를 시행합니다.", "meaningVi": "Khối u ác tính phát sinh ở thận, giai đoạn đầu không có triệu chứng nên thường phát hiện tình cờ qua khám sức khỏe. Ba triệu chứng kinh điển là tiểu ra máu, khối u sườn, đau nhưng nếu có đủ cả ba thường đã tiến triển. Điều trị chính là phẫu thuật cắt bỏ, nếu phát hiện sớm có thể cắt một phần thận để bảo tồn chức năng. Ung thư thận di căn dùng thuốc nhắm trúng đích hoặc miễn dịch trị liệu.", "context": "비뇨의학과, 종양내과", "culturalNote": "신장암은 한국에서 복부 초음파 보급으로 조기 발견이 증가했으며, 베트남 환자들도 건강검진 기회가 늘면서 우연히 발견되는 사례가 있습니다. 한 쪽 신장만으로도 정상 생활이 가능하다는 점을 설명하면 수술에 대한 불안을 줄일 수 있습니다. 부분 신절제술과 전절제술의 차이를 환자가 이해하도록 도와야 하며, 로봇 수술 등 최소침습 수술 옵션도 설명하는 것이 좋습니다.", "commonMistakes": [{"mistake": "모든 신장 종괴를 암으로 단정", "correction": "양성 낭종과 악성 종양 구분 필요", "explanation": "불필요한 불안을 주지 않도록 정확한 진단 후 설명해야 합니다"}, {"mistake": "한 쪽 신장 제거 시 투석 필요하다고 설명", "correction": "한 쪽 신장만으로 정상 기능 가능", "explanation": "환자가 수술 후 삶에 대한 현실적 기대를 가질 수 있도록 해야 합니다"}, {"mistake": "조기 발견의 중요성을 강조하지 않음", "correction": "정기 건강검진으로 조기 발견 가능", "explanation": "검진의 가치를 이해하도록 교육해야 합니다"}], "examples": [{"ko": "건강검진 초음파에서 우연히 신장암이 발견되어 다행히 조기입니다.", "vi": "May mắn phát hiện ung thư thận tình cờ qua siêu âm khám sức khỏe, giai đoạn sớm.", "situation": "formal"}, {"ko": "종양이 작아서 부분 신절제술로 신장 기능을 보존할 수 있어요.", "vi": "U nhỏ nên có thể cắt một phần thận để bảo tồn chức năng thận.", "situation": "onsite"}, {"ko": "한 쪽 신장만 있어도 정상 생활할 수 있으니 걱정 마세요.", "vi": "Chỉ một thận vẫn có thể sống bình thường nên đừng lo.", "situation": "informal"}], "relatedTerms": ["혈뇨", "복부초음파", "신절제술", "표적치료"]},
    {"slug": "요실금", "korean": "요실금", "vietnamese": "Tiểu không tự chủ", "hanja": "尿失禁", "hanjaReading": "尿(오줌 뇨) + 失(잃을 실) + 禁(금할 금)", "pronunciation": "요실금", "meaningKo": "자신의 의지와 관계없이 소변이 새는 증상으로, 복압성과 절박성으로 나뉘며 여성과 노인에게 흔합니다. 통역 시 'Tiểu không tự chủ' 또는 'Tiểu ra không kiểm soát được'로 표현하며, 기침이나 재채기 시 소변이 새는 복압성 요실금과 갑자기 참을 수 없이 마려운 절박성 요실금을 구분해야 합니다. 골반저근육 운동, 약물 치료, 수술 등 다양한 치료 옵션이 있으며, 생활의 질을 크게 저하시키므로 적극적 치료를 권장해야 합니다.", "meaningVi": "Triệu chứng tiểu ra nước tiểu không kiểm soát được, chia thành tiểu không tự chủ do căng bụng và cấp bách, thường gặp ở phụ nữ và người già. Tiểu không tự chủ do căng bụng là tiểu ra khi ho hoặc hắt hơi, cấp bách là buồn tiểu gấp không nhịn được. Có nhiều lựa chọn điều trị như tập cơ sàn chậu, thuốc, phẫu thuật. Ảnh hưởng nhiều đến chất lượng cuộc sống nên khuyến cáo điều trị tích cực.", "context": "비뇨의학과", "culturalNote": "요실금은 한국 여성들이 출산 후나 폐경기에 흔히 경험하지만 수치심 때문에 병원 방문을 꺼리는 질환입니다. 베트남 여성들도 비슷한 문화적 장벽이 있어, 치료 가능한 질환임을 강조하고 상담하기 편한 환경을 만드는 것이 중요합니다. 골반저근육 운동(케겔 운동)은 효과적이지만 올바른 방법을 교육해야 하며, 수술적 치료도 발전하여 삶의 질 개선이 가능함을 안내해야 합니다.", "commonMistakes": [{"mistake": "노화의 당연한 결과로 설명", "correction": "치료 가능한 질환으로 삶의 질 개선 가능", "explanation": "환자가 치료를 포기하지 않도록 개선 가능성을 전달해야 합니다"}, {"mistake": "복압성과 절박성을 구분하지 않음", "correction": "유형에 따라 치료가 다르므로 정확한 분류 필요", "explanation": "적절한 치료를 위해 요실금 유형을 파악해야 합니다"}, {"mistake": "수분 섭취를 극도로 제한하라고 조언", "correction": "적절한 수분 섭취 유지하되 방광 자극 음료 피하기", "explanation": "탈수나 요로감염을 예방하면서 증상 관리를 해야 합니다"}], "examples": [{"ko": "기침할 때 소변이 새는 건 복압성 요실금으로, 골반저근육 운동이 도움됩니다.", "vi": "Tiểu ra khi ho là tiểu không tự chủ do căng bụng, tập cơ sàn chậu sẽ có ích.", "situation": "formal"}, {"ko": "요실금은 치료 가능한 질환이니까 부끄러워하지 말고 진료 받으세요.", "vi": "Tiểu không tự chủ là bệnh có thể điều trị nên đừng ngại, hãy khám.", "situation": "onsite"}, {"ko": "패드에만 의존하지 말고 적극적으로 치료받으면 좋아질 수 있어요.", "vi": "Đừng chỉ dựa vào miếng lót, nếu điều trị tích cực thì có thể khỏi.", "situation": "informal"}], "relatedTerms": ["골반저근육운동", "복압성요실금", "절박성요실금", "방광훈련"]},
    {"slug": "roi-loan-cuong-duong", "korean": "발기부전", "vietnamese": "Rối loạn cương dương", "hanja": "勃起不全", "hanjaReading": "勃(일어날 발) + 起(일어날 기) + 不(아닐 불) + 全(온전할 전)", "pronunciation": "발기부전", "meaningKo": "만족스러운 성행위를 위한 발기를 달성하거나 유지하지 못하는 상태로, 혈관성, 신경성, 심인성 등 다양한 원인이 있습니다. 통역 시 'Rối loạn cương dương' 또는 'Liệt dương'으로 표현하며, 당뇨병, 고혈압, 심혈관 질환과의 연관성을 설명해야 합니다. 경구용 약물(PDE5 억제제)이 1차 치료로 효과적이며, 생활습관 개선(금연, 운동, 체중 조절)도 중요합니다. 민감한 주제이므로 환자의 프라이버시를 존중하며 통역하는 것이 필수적입니다.", "meaningVi": "Tình trạng không đạt được hoặc duy trì cương cứng để quan hệ tình dục thỏa mãn, có nhiều nguyên nhân như mạch máu, thần kinh, tâm lý. Liên quan đến đái tháo đường, tăng huyết áp, bệnh tim mạch. Thuốc uống (ức chế PDE5) là điều trị hàng đầu, hiệu quả. Thay đổi lối sống (cai thuốc, tập thể dục, kiểm soát cân nặng) cũng quan trọng.", "context": "비뇨의학과", "culturalNote": "발기부전은 한국과 베트남 모두 문화적으로 매우 민감한 주제로, 남성들이 병원 방문을 꺼려하고 불법 약물이나 민간요법에 의존하는 경우가 많습니다. 통역 시 환자의 수치심을 최소화하고 의학적 질환임을 강조하는 것이 중요합니다. 비아그라 등 PDE5 억제제가 효과적이지만, 심혈관 질환자는 주의가 필요하므로 복용 전 의사 상담의 중요성을 강조해야 합니다. 심리적 원인도 흔하므로 필요 시 상담 치료를 권장하는 것도 좋습니다.", "commonMistakes": [{"mistake": "무조건 심리적 문제로만 설명", "correction": "신체적 원인(혈관, 신경, 호르몬)이 흔함", "explanation": "정확한 원인 규명을 위한 검사가 필요함을 알려야 합니다"}, {"mistake": "비아그라를 모든 환자에게 안전하다고 설명", "correction": "심혈관 질환자는 위험할 수 있어 의사 처방 필수", "explanation": "자가 치료의 위험성을 경고해야 합니다"}, {"mistake": "일회성 실패를 발기부전으로 진단", "correction": "지속적이고 반복적인 어려움이 있을 때 진단", "explanation": "불필요한 불안을 주지 않도록 진단 기준을 정확히 전달해야 합니다"}], "examples": [{"ko": "발기부전은 혈관 건강의 지표이므로 당뇨나 고혈압 관리가 중요합니다.", "vi": "Rối loạn cương dương là chỉ số sức khỏe mạch máu nên quan trọng là quản lý đái tháo đường, tăng huyết áp.", "situation": "formal"}, {"ko": "경구용 약으로 치료가 잘 되니까 너무 걱정하지 마세요.", "vi": "Điều trị bằng thuốc uống hiệu quả nên đừng quá lo.", "situation": "onsite"}, {"ko": "담배 끊고 운동하면 발기부전이 좋아질 수 있어요.", "vi": "Nếu cai thuốc và tập thể dục thì rối loạn cương dương có thể khỏi.", "situation": "informal"}], "relatedTerms": ["당뇨병", "고혈압", "PDE5억제제", "비아그라"]},
    {"slug": "giãn tĩnh mạch tinh", "korean": "정계정맥류", "vietnamese": "Giãn tĩnh mạch tinh", "hanja": "精系靜脈瘤", "hanjaReading": "精(정액 정) + 系(맬 계) + 靜(고요할 정) + 脈(맥 맥) + 瘤(혹 류)", "pronunciation": "정계정맥류", "meaningKo": "정계정맥이 비정상적으로 확장되어 음낭 내에서 정맥류를 형성하는 질환으로, 남성 불임의 원인이 될 수 있습니다. 통역 시 'Giãn tĩnh mạch tinh'으로 표현하며, 주로 왼쪽에 발생하고 음낭이 무거운 느낌이나 둔한 통증이 있을 수 있음을 설명해야 합니다. 불임이 있거나 통증이 심한 경우 수술적 치료를 고려하며, 수술 후 정자의 질이 개선될 수 있습니다. 사춘기 청소년에서 발견되면 고환 성장에 영향을 줄 수 있어 조기 치료가 필요할 수 있음을 안내해야 합니다.", "meaningVi": "Bệnh tĩnh mạch tinh giãn bất thường hình thành giãn tĩnh mạch trong bìu, có thể là nguyên nhân vô sinh nam. Chủ yếu xảy ra bên trái, có thể cảm thấy bìu nặng hoặc đau âm ỉ. Nếu vô sinh hoặc đau nhiều thì xem xét phẫu thuật, sau mổ chất lượng tinh trùng có thể cải thiện. Nếu phát hiện ở thanh thiếu niên có thể ảnh hưởng phát triển tinh hoàn nên có thể cần điều trị sớm.", "context": "비뇨의학과", "culturalNote": "정계정맥류는 한국에서 불임 검사 중 발견되는 경우가 많으며, 베트남에서도 남성 불임 원인으로 인식되고 있습니다. 음낭 검진이 필요한데 문화적으로 민감할 수 있어 환자의 불편함을 최소화하는 것이 중요합니다. 수술이 불임 해결을 보장하지는 않지만 정자의 질 개선에 도움이 될 수 있다는 현실적 기대치를 설명해야 합니다. 청소년기 발견 시 부모와 함께 치료 계획을 논의하는 것이 필요합니다.", "commonMistakes": [{"mistake": "정계정맥류를 즉시 수술해야 한다고 설명", "correction": "불임이나 통증 있을 때 수술 고려", "explanation": "무증상이면 경과 관찰도 가능하므로 과잉 치료를 피해야 합니다"}, {"mistake": "수술 후 임신이 확실하다고 보장", "correction": "정자의 질 개선 가능하지만 임신 보장은 못함", "explanation": "현실적인 기대를 설정하도록 도와야 합니다"}, {"mistake": "왼쪽과 오른쪽을 구분하지 않음", "correction": "주로 왼쪽 발생, 오른쪽이면 다른 원인 확인 필요", "explanation": "우측 정계정맥류는 복강 내 종괴 등 다른 원인을 시사할 수 있습니다"}], "examples": [{"ko": "정계정맥류가 있지만 통증이 없고 정자 검사가 정상이면 치료 안 해도 됩니다.", "vi": "Có giãn tĩnh mạch tinh nhưng không đau và tinh trùng bình thường thì không cần điều trị.", "situation": "formal"}, {"ko": "불임 때문에 정계정맥류 수술하면 정자가 좋아질 수 있어요.", "vi": "Nếu mổ giãn tĩnh mạch tinh vì vô sinh thì tinh trùng có thể tốt hơn.", "situation": "onsite"}, {"ko": "음낭에 벌레 기어가는 느낌이 들면 정계정맥류일 수 있어요.", "vi": "Nếu cảm thấy như sâu bò trong bìu thì có thể là giãn tĩnh mạch tinh.", "situation": "informal"}], "relatedTerms": ["남성불임", "정자검사", "음낭", "수술"]},
    {"slug": "ung-thu-tinh-hoan", "korean": "고환암", "vietnamese": "Ung thư tinh hoàn", "hanja": "睾丸癌", "hanjaReading": "睾(고환 고) + 丸(알 환) + 癌(암 암)", "pronunciation": "고환암", "meaningKo": "고환에서 발생하는 악성 종양으로, 젊은 남성에게 가장 흔한 고형암이며 조기 발견 시 완치율이 매우 높습니다. 통역 시 'Ung thư tinh hoàn'으로 표현하며, 고환의 무통성 종괴가 특징적 증상임을 설명해야 합니다. 자가 검진으로 조기 발견이 가능하므로 젊은 남성에게 정기적 자가 검진을 교육하는 것이 중요합니다. 치료는 고환 적출 후 조직 유형과 병기에 따라 감시, 화학요법, 방사선 치료 등을 결정하며, 항암치료에 매우 잘 반응하여 예후가 좋습니다.", "meaningVi": "Khối u ác tính phát sinh ở tinh hoàn, là ung thư đặc thể thường gặp nhất ở nam giới trẻ, nếu phát hiện sớm tỷ lệ khỏi rất cao. Triệu chứng đặc trưng là khối u tinh hoàn không đau. Có thể phát hiện sớm bằng tự khám nên quan trọng là dạy nam giới trẻ tự khám định kỳ. Điều trị là cắt tinh hoàn rồi tùy loại mô và giai đoạn quyết định theo dõi, hóa trị, xạ trị, phản ứng rất tốt với hóa trị nên tiên lượng tốt.", "context": "비뇨의학과, 종양내과", "culturalNote": "고환암은 한국에서 15-35세 젊은 남성에게 흔하며, 자가 검진 교육이 중요하지만 문화적으로 민감하여 교육이 잘 이루어지지 않습니다. 베트남에서도 비슷한 상황이므로, 자가 검진 방법을 의료진을 통해 교육하는 것이 필요합니다. 고환 적출에 대한 심리적 충격이 클 수 있으나, 한 쪽 고환만으로도 정상적인 성기능과 생식 기능이 가능함을 안심시켜야 합니다. 항암치료가 매우 효과적이어서 진행된 단계에서도 완치 가능하다는 희망적 메시지를 전달하는 것이 중요합니다.", "commonMistakes": [{"mistake": "고환 종괴를 염증으로 오인하여 항생제만 처방", "correction": "무통성 종괴는 암 의심, 즉시 초음파 검사", "explanation": "조기 진단을 놓치지 않도록 의심 증상을 정확히 전달해야 합니다"}, {"mistake": "고환 적출이 성기능 상실을 의미한다고 설명", "correction": "한 쪽 고환으로 정상 성기능과 생식 기능 가능", "explanation": "환자의 불필요한 불안을 줄이기 위해 정확한 정보를 제공해야 합니다"}, {"mistake": "예후가 나쁜 암으로 설명", "correction": "조기 발견 및 항암치료 반응 좋아 완치율 높음", "explanation": "희망적인 예후를 전달하여 환자의 치료 동기를 높여야 합니다"}], "examples": [{"ko": "고환에서 딱딱한 혹이 만져지면 즉시 병원에 오셔야 합니다.", "vi": "Nếu sờ thấy cục cứng ở tinh hoàn thì phải đến bệnh viện ngay.", "situation": "formal"}, {"ko": "고환암은 항암치료가 아주 잘 듣는 암이라서 완치율이 90% 이상이에요.", "vi": "Ung thư tinh hoàn phản ứng rất tốt với hóa trị nên tỷ lệ khỏi trên 90%.", "situation": "onsite"}, {"ko": "한 달에 한 번 샤워할 때 고환을 스스로 만져보세요.", "vi": "Một tháng một lần khi tắm hãy tự sờ tinh hoàn.", "situation": "informal"}], "relatedTerms": ["자가검진", "고환종괴", "항암치료", "고환적출술"]},
    {"slug": "cat-bao-quy-dau", "korean": "포경수술", "vietnamese": "Cắt bao quy đầu", "hanja": "包莖手術", "hanjaReading": "包(쌀 포) + 莖(줄기 경) + 手(손 수) + 術(재주 술)", "pronunciation": "포경수술", "meaningKo": "포피를 제거하는 수술로, 의학적 적응증(포경, 귀두포피염 반복)이나 종교적, 위생적 이유로 시행됩니다. 통역 시 'Cắt bao quy đầu' 또는 'Cắt bao quy đầu'으로 표현하며, 한국에서는 사춘기에 시행하는 경우가 많지만 의학적으로 필수는 아님을 설명해야 합니다. 수술 후 관리(소독, 봉합사 제거 시기 등)를 정확히 안내하고, 합병증(출혈, 감염, 과다 절제 등) 발생 시 즉시 내원하도록 교육하는 것이 중요합니다.", "meaningVi": "Phẫu thuật cắt bỏ bao quy đầu, thực hiện vì chỉ định y tế (hẹp bao quy đầu, viêm quy đầu bao quy đầu tái đi tái lại) hoặc lý do tôn giáo, vệ sinh. Ở Hàn Quốc thường làm ở tuổi dậy thì nhưng y học không bắt buộc. Sau mổ cần hướng dẫn chăm sóc chính xác (khử trùng, thời điểm cắt chỉ) và nếu có biến chứng (chảy máu, nhiễm trùng, cắt quá nhiều) phải đến viện ngay.", "context": "비뇨의학과", "culturalNote": "포경수술은 한국에서 사회문화적으로 매우 보편화되어 대부분 남성이 시행하지만, 베트남에서는 덜 일반적이어서 문화적 차이를 고려해야 합니다. 한국 부모들은 자녀의 포경수술을 당연하게 생각하지만, 의학적 필요성이 항상 있는 것은 아니므로 정확한 정보를 제공해야 합니다. 수술 후 성감 변화나 합병증에 대한 우려가 있을 수 있어, 현실적인 정보를 제공하는 것이 중요합니다. 사춘기 청소년의 경우 본인의 의사를 존중하는 것도 필요합니다.", "commonMistakes": [{"mistake": "모든 남성에게 필수 수술로 설명", "correction": "의학적 적응증 있을 때 권장", "explanation": "불필요한 수술을 피하고 informed decision을 돕기 위해 정확한 정보가 필요합니다"}, {"mistake": "수술 후 관리를 대략적으로만 설명", "correction": "소독 방법, 봉합사 제거 시기, 주의사항 구체적 설명", "explanation": "합병증 예방과 적절한 회복을 위해 구체적 지침이 필요합니다"}, {"mistake": "성인과 소아의 수술을 동일하게 설명", "correction": "연령에 따라 마취 방법, 회복 기간 다름", "explanation": "환자와 보호자가 적절한 계획을 세울 수 있도록 연령별 차이를 설명해야 합니다"}], "examples": [{"ko": "포경이 심해서 귀두가 노출되지 않으므로 포경수술을 권합니다.", "vi": "Do hẹp bao quy đầu nặng không lộ quy đầu được nên khuyến cáo cắt bao quy đầu.", "situation": "formal"}, {"ko": "수술 후 2주간은 과격한 운동을 피하고 소독을 잘 하세요.", "vi": "Sau mổ 2 tuần tránh vận động mạnh và khử trùng tốt.", "situation": "onsite"}, {"ko": "포경수술은 필수는 아니지만 위생 관리에는 도움이 돼요.", "vi": "Cắt bao quy đầu không bắt buộc nhưng có ích cho vệ sinh.", "situation": "informal"}], "relatedTerms": ["포경", "귀두포피염", "수술후관리", "합병증"]},
    {"slug": "suy-than-cap", "korean": "급성신부전", "vietnamese": "Suy thận cấp", "hanja": "急性腎不全", "hanjaReading": "急(급할 급) + 性(성품 성) + 腎(콩팥 신) + 不(아닐 불) + 全(온전할 전)", "pronunciation": "급성신부전", "meaningKo": "신장 기능이 급격히 저하되어 노폐물 배설과 수분 조절에 장애가 생기는 응급 상황으로, 원인 제거 시 회복 가능합니다. 통역 시 'Suy thận cấp'으로 표현하며, 신전성(탈수), 신성(신장 자체 손상), 신후성(요로 폐쇄)으로 나뉨을 설명해야 합니다. 소변량 감소, 부종, 의식 변화 등이 나타날 수 있으며, 원인 규명과 신속한 치료가 중요합니다. 중증인 경우 투석이 필요할 수 있지만, 원인 제거 후 신기능이 회복되면 투석을 중단할 수 있음을 안내해야 합니다.", "meaningVi": "Tình trạng cấp cứu chức năng thận giảm đột ngột gây rối loạn bài tiết chất thải và điều hòa nước, có thể hồi phục nếu loại bỏ nguyên nhân. Chia thành trước thận (mất nước), trong thận (tổn thương bản thân thận), sau thận (tắc đường tiết niệu). Có thể có giảm nước tiểu, phù, thay đổi ý thức, quan trọng là tìm nguyên nhân và điều trị nhanh. Trường hợp nặng có thể cần lọc máu nhưng nếu chức năng thận hồi phục sau khi loại bỏ nguyên nhân thì có thể ngừng lọc.", "context": "신장내과, 응급의학", "culturalNote": "급성신부전은 한국에서 중환자실 입원이 필요한 경우가 많으며, 베트남 환자와 가족에게 질환의 심각성과 치료 계획을 충분히 설명해야 합니다. 투석이 필요하다는 말에 환자들이 '평생 투석'으로 오해할 수 있는데, 급성신부전은 회복 가능하여 일시적 투석일 수 있음을 명확히 해야 합니다. 원인이 다양하므로(약물, 감염, 탈수 등) 병력 청취가 매우 중요하며, 한약이나 민간요법 복용력도 확인해야 합니다.", "commonMistakes": [{"mistake": "만성신부전과 혼동하여 설명", "correction": "급성은 회복 가능, 만성은 비가역적으로 구분", "explanation": "환자의 예후에 대한 현실적 기대를 설정하는 데 중요합니다"}, {"mistake": "투석을 평생 해야 한다고 설명", "correction": "급성인 경우 신기능 회복 시 투석 중단 가능", "explanation": "불필요한 절망감을 주지 않도록 정확한 정보를 제공해야 합니다"}, {"mistake": "원인 규명 없이 증상만 치료", "correction": "신전성/신성/신후성 원인 분류하여 맞춤 치료", "explanation": "효과적인 치료를 위해 정확한 원인 파악이 필수입니다"}], "examples": [{"ko": "급성신부전으로 입원하셨지만 원인을 해결하면 신기능이 회복될 수 있습니다.", "vi": "Nhập viện do suy thận cấp nhưng nếu giải quyết nguyên nhân thì chức năng thận có thể hồi phục.", "situation": "formal"}, {"ko": "소변이 안 나오고 부었으니 급성신부전이 의심돼요. 투석이 필요할 수도 있어요.", "vi": "Không tiểu và phù nên nghi suy thận cấp. Có thể cần lọc máu.", "situation": "onsite"}, {"ko": "급성신부전은 빨리 치료하면 좋아질 수 있어요.", "vi": "Suy thận cấp nếu điều trị nhanh có thể khỏi.", "situation": "informal"}], "relatedTerms": ["소변량감소", "부종", "투석", "전해질불균형"]},
    {"slug": "suy-than-man-tinh", "korean": "만성신부전", "vietnamese": "Suy thận mạn tính", "hanja": "慢性腎不全", "hanjaReading": "慢(느릴 만) + 性(성품 성) + 腎(콩팥 신) + 不(아닐 불) + 全(온전할 전)", "pronunciation": "만성신부전", "meaningKo": "신장 기능이 3개월 이상 지속적으로 감소하는 비가역적 질환으로, 당뇨병과 고혈압이 주요 원인입니다. 통역 시 'Suy thận mạn tính'으로 표현하며, 5단계로 분류되며 말기(5단계)에는 투석이나 신장이식이 필요함을 설명해야 합니다. 조기에는 증상이 거의 없어 혈액검사(크레아티닌, eGFR)로 진단되며, 원인 질환 관리와 신기능 보존 치료(식이 조절, 혈압 관리)가 중요합니다. 투석 시작 시기와 방법(혈액투석, 복막투석)을 환자와 충분히 상의해야 합니다.", "meaningVi": "Bệnh không hồi phục chức năng thận giảm liên tục trên 3 tháng, nguyên nhân chính là đái tháo đường và tăng huyết áp. Phân 5 giai đoạn, giai đoạn cuối (giai đoạn 5) cần lọc máu hoặc ghép thận. Giai đoạn sớm hầu như không có triệu chứng, chẩn đoán bằng xét nghiệm máu (creatinine, eGFR). Quan trọng là quản lý bệnh nguyên nhân và điều trị bảo tồn chức năng thận (điều chỉnh chế độ ăn, kiểm soát huyết áp). Cần bàn bạc đầy đủ về thời điểm và phương pháp lọc máu (lọc máu, lọc màng bụng).", "context": "신장내과", "culturalNote": "만성신부전은 한국에서 당뇨병 합병증으로 증가하고 있으며, 베트남에서도 비슷한 추세입니다. 투석에 대한 두려움과 경제적 부담이 크므로, 조기부터 질환 관리의 중요성을 교육하여 진행을 늦추는 것이 중요합니다. 혈액투석과 복막투석의 차이를 설명할 때 각각의 장단점을 공정하게 전달하여 환자가 선택할 수 있도록 도와야 합니다. 신장이식이 최선의 치료이지만 한국과 베트남 모두 기증자 부족 문제가 있어, 현실적인 대안을 함께 논의하는 것이 필요합니다.", "commonMistakes": [{"mistake": "급성신부전과 혼동", "correction": "만성은 비가역적, 투석 또는 이식 필요", "explanation": "환자가 질환의 장기적 성격을 이해하도록 해야 합니다"}, {"mistake": "투석을 마지막 수단으로만 제시", "correction": "적절한 시기에 시작하는 것이 삶의 질 유지에 중요", "explanation": "투석을 너무 늦게 시작하면 합병증이 증가하므로 적기 시작을 권장해야 합니다"}, {"mistake": "식이 제한을 막연하게만 설명", "correction": "단백질, 칼륨, 인, 수분 등 구체적 지침", "explanation": "실천 가능한 구체적 식이 교육이 질환 관리에 필수입니다"}], "examples": [{"ko": "만성신부전 4단계로 투석 준비를 시작해야 합니다. 혈관 접근로를 만들겠습니다.", "vi": "Suy thận mạn tính giai đoạn 4 nên phải bắt đầu chuẩn bị lọc máu. Sẽ tạo đường vào mạch máu.", "situation": "formal"}, {"ko": "당뇨 관리 잘 하면 만성신부전 진행을 늦출 수 있어요.", "vi": "Nếu quản lý đái tháo đường tốt thì có thể làm chậm tiến triển suy thận mạn.", "situation": "onsite"}, {"ko": "만성신부전은 완치는 안 되지만 관리하면서 살 수 있어요.", "vi": "Suy thận mạn không khỏi được nhưng có thể sống với quản lý.", "situation": "informal"}], "relatedTerms": ["당뇨병", "고혈압", "투석", "신장이식", "eGFR"]},
    {"slug": "viem-cau-than", "korean": "사구체신염", "vietnamese": "Viêm cầu thận", "hanja": "絲球體腎炎", "hanjaReading": "絲(실 사) + 球(공 구) + 體(몸 체) + 腎(콩팥 신) + 炎(불꽃 염)", "pronunciation": "사구체신염", "meaningKo": "신장의 사구체에 염증이 생기는 질환으로, 혈뇨, 단백뇨, 고혈압, 부종 등이 나타나며 급성과 만성으로 나뉩니다. 통역 시 'Viêm cầu thận'으로 표현하며, 감염 후 발생하거나 자가면역 질환의 일부일 수 있음을 설명해야 합니다. 신장 조직검사로 정확한 진단과 예후 예측이 가능하며, 치료는 원인과 조직 유형에 따라 스테로이드나 면역억제제를 사용합니다. 만성화되면 만성신부전으로 진행할 수 있으므로 조기 진단과 적절한 치료가 중요합니다.", "meaningVi": "Bệnh viêm cầu thận ở thận, có triệu chứng tiểu ra máu, protein niệu, tăng huyết áp, phù, chia cấp và mạn. Có thể xảy ra sau nhiễm trùng hoặc là một phần của bệnh tự miễn. Sinh thiết thận có thể chẩn đoán chính xác và dự đoán tiên lượng, điều trị tùy nguyên nhân và loại mô dùng steroid hoặc ức chế miễn dịch. Nếu mạn tính hóa có thể tiến triển thành suy thận mạn nên chẩn đoán sớm và điều trị thích hợp quan trọng.", "context": "신장내과", "culturalNote": "사구체신염은 한국에서 소아의 급성 사구체신염(감염 후)과 성인의 IgA 신병증이 흔하며, 베트남에서도 비슷한 양상을 보입니다. 신장 조직검사가 진단에 중요한데, 환자들이 침습적 검사를 두려워할 수 있어 검사의 필요성과 안전성을 충분히 설명해야 합니다. 스테로이드나 면역억제제 치료가 필요한 경우 장기 복용의 필요성과 부작용 관리를 함께 설명하는 것이 중요합니다. 소아 환자의 경우 부모와 충분한 상담이 필요합니다.", "commonMistakes": [{"mistake": "단순 요로감염과 혼동", "correction": "사구체 질환으로 전신 증상(부종, 고혈압) 동반", "explanation": "정확한 진단을 위해 질환의 특성을 명확히 전달해야 합니다"}, {"mistake": "급성과 만성을 구분하지 않음", "correction": "급성은 회복 가능, 만성은 진행성으로 구분", "explanation": "예후와 치료 계획이 다르므로 정확한 분류가 필요합니다"}, {"mistake": "신장 조직검사를 과도하게 위험하다고 설명", "correction": "합병증 가능하나 대부분 안전, 진단에 중요", "explanation": "필요한 검사를 환자가 거부하지 않도록 균형잡힌 정보를 제공해야 합니다"}], "examples": [{"ko": "혈뇨와 단백뇨가 있어서 사구체신염이 의심됩니다. 신장 조직검사를 권합니다.", "vi": "Có tiểu ra máu và protein niệu nên nghi viêm cầu thận. Khuyến cáo sinh thiết thận.", "situation": "formal"}, {"ko": "감기 앓고 나서 소변에 피가 섞여 나오면 급성 사구체신염일 수 있어요.", "vi": "Nếu sau cảm sau khi ốm mà tiểu ra máu thì có thể là viêm cầu thận cấp.", "situation": "onsite"}, {"ko": "사구체신염은 잘 관리하면 신부전으로 안 갈 수도 있어요.", "vi": "Viêm cầu thận nếu quản lý tốt có thể không tiến triển thành suy thận.", "situation": "informal"}], "relatedTerms": ["혈뇨", "단백뇨", "부종", "신장조직검사"]},
    # Final 10 terms: 신증후군, 신장이식, 투석혈관접근로, 복막투석카테터, 요독증, 전해질불균형, 대사성산증, 고칼륨혈증, 저나트륨혈증, 신장생검
    {"slug": "hoi-chung-than", "korean": "신증후군", "vietnamese": "Hội chứng thận", "hanja": "腎症候群", "hanjaReading": "腎(콩팥 신) + 症(병 증) + 候(기후 후) + 群(무리 군)", "pronunciation": "신증후군", "meaningKo": "대량의 단백뇨, 저알부민혈증, 부종, 고지혈증을 특징으로 하는 사구체 질환 증후군입니다. 통역 시 'Hội chứng thận'으로 표현하며, 소아와 성인에서 원인이 다를 수 있음을 설명해야 합니다. 소변으로 단백질이 과도하게 빠져나가 혈중 알부민이 낮아지고 이로 인해 부종이 발생하는 기전을 이해시키는 것이 중요합니다. 스테로이드 치료가 1차 치료이며, 반응에 따라 스테로이드 민감성, 의존성, 저항성으로 분류되어 치료 계획이 달라집니다. 감염 위험이 높아 예방과 조기 발견이 중요함을 강조해야 합니다.", "meaningVi": "Hội chứng bệnh cầu thận đặc trưng bởi protein niệu nhiều, giảm albumin máu, phù, tăng lipid máu. Nguyên nhân có thể khác nhau ở trẻ em và người lớn. Protein ra nước tiểu quá nhiều làm albumin máu giảm và do đó gây phù. Điều trị hàng đầu là steroid, tùy phản ứng phân loại thành nhạy cảm steroid, phụ thuộc, kháng steroid, kế hoạch điều trị khác nhau. Nguy cơ nhiễm trùng cao nên quan trọng là phòng ngừa và phát hiện sớm.", "context": "신장내과, 소아과", "culturalNote": "신증후군은 한국에서 소아에게 흔한 신장 질환으로 부모의 불안이 크며, 베트남에서도 비슷합니다. 스테로이드 장기 사용에 따른 부작용(성장 지연, 체중 증가, 감염 위험)에 대한 우려가 크므로, 치료의 필요성과 부작용 관리를 균형있게 설명해야 합니다. 부종이 심할 때 저염식이가 필요한데, 베트남 식문화에서 실천하기 어려울 수 있어 현실적인 식이 조언이 필요합니다. 재발이 흔한 질환이므로 장기적 관리 계획을 세우는 것이 중요합니다.", "commonMistakes": [{"mistake": "부종을 심장이나 간 질환으로 오인", "correction": "단백뇨와 저알부민혈증에 의한 신성 부종", "explanation": "정확한 진단을 위해 신증후군의 특성을 명확히 전달해야 합니다"}, {"mistake": "스테로이드를 즉시 중단하라고 조언", "correction": "의사 지시에 따라 서서히 감량 필요", "explanation": "갑작스런 중단은 재발이나 부신기능저하를 유발할 수 있습니다"}, {"mistake": "감염 위험을 과소평가", "correction": "면역 저하로 감염 취약, 예방접종과 조기 치료 중요", "explanation": "감염은 신증후군의 주요 합병증이므로 적극적 예방이 필요합니다"}], "examples": [{"ko": "신증후군으로 단백뇨가 심하니 스테로이드 치료를 시작하겠습니다.", "vi": "Do hội chứng thận protein niệu nặng nên sẽ bắt đầu điều trị steroid.", "situation": "formal"}, {"ko": "부은 건 소변으로 단백질이 빠져나가서 그래요. 저염식 하세요.", "vi": "Phù là do protein ra nước tiểu. Ăn ít muối nhé.", "situation": "onsite"}, {"ko": "신증후군은 재발 잘 하니까 계속 추적 관찰 받아야 해요.", "vi": "Hội chứng thận hay tái phát nên phải theo dõi liên tục.", "situation": "informal"}], "relatedTerms": ["단백뇨", "부종", "스테로이드", "저알부민혈증"]},
    {"slug": "ghep-than", "korean": "신장이식", "vietnamese": "Ghép thận", "hanja": "腎臟移植", "hanjaReading": "腎(콩팥 신) + 臟(장부 장) + 移(옮길 이) + 植(심을 식)", "pronunciation": "신장이식", "meaningKo": "만성신부전 환자에게 건강한 신장을 이식하는 치료법으로, 투석보다 삶의 질이 우수하며 생존율도 높습니다. 통역 시 'Ghép thận'으로 표현하며, 생체 기증과 뇌사자 기증으로 나뉘고 한국에서는 대기 시간이 길 수 있음을 설명해야 합니다. 이식 후 평생 면역억제제 복용이 필요하며, 거부반응과 감염 예방이 중요함을 강조해야 합니다. 이식 신장의 생존 기간이 제한적이므로(평균 10-15년), 젊은 환자는 재이식 가능성도 고려해야 함을 안내하는 것이 중요합니다.", "meaningVi": "Phương pháp điều trị ghép thận khỏe mạnh cho bệnh nhân suy thận mạn, chất lượng cuộc sống tốt hơn lọc máu và tỷ lệ sống cao hơn. Chia thành hiến tặng người sống và người chết não, ở Hàn Quốc thời gian chờ có thể dài. Sau ghép phải uống thuốc ức chế miễn dịch suốt đời, quan trọng là phòng ngừa phản ứng thải ghép và nhiễm trùng. Thận ghép có thời gian sống hạn chế (trung bình 10-15 năm) nên bệnh nhân trẻ cần xem xét khả năng ghép lại.", "context": "신장내과, 이식외과", "culturalNote": "신장이식은 한국에서 만성신부전의 최선 치료로 인식되지만, 생체 기증자 구하기가 어렵고 뇌사자 장기는 대기 시간이 길어 현실적 어려움이 있습니다. 베트남에서는 장기이식 인프라가 덜 발달하여 한국에서 이식받으려는 환자가 있을 수 있습니다. 가족 간 생체 기증 시 기증자의 자발성과 안전성을 확인하는 것이 매우 중요하며, 윤리적 측면을 고려해야 합니다. 이식 후 면역억제제 복용의 중요성과 평생 관리가 필요함을 강조하되, 투석보다 훨씬 나은 삶의 질을 누릴 수 있음을 안심시켜야 합니다.", "commonMistakes": [{"mistake": "이식 후 완치된다고 설명", "correction": "평생 면역억제제 복용과 정기 검진 필요", "explanation": "환자가 이식 후 관리의 중요성을 이해하도록 해야 합니다"}, {"mistake": "생체 기증을 가족에게 강요", "correction": "기증자의 자발성과 안전성 최우선", "explanation": "윤리적 문제를 예방하고 기증자를 보호해야 합니다"}, {"mistake": "이식 신장이 영구적이라고 설명", "correction": "평균 10-15년 생존, 재이식 필요할 수 있음", "explanation": "현실적인 기대를 설정하도록 도와야 합니다"}], "examples": [{"ko": "신장이식은 투석보다 삶의 질이 좋지만 평생 면역억제제를 드셔야 합니다.", "vi": "Ghép thận chất lượng cuộc sống tốt hơn lọc máu nhưng phải uống thuốc ức chế miễn dịch suốt đời.", "situation": "formal"}, {"ko": "가족 중에 기증 의사 있으시면 조직 적합성 검사를 해보겠습니다.", "vi": "Nếu có người trong gia đình muốn hiến thì sẽ xét nghiệm độ tương hợp mô.", "situation": "onsite"}, {"ko": "이식 받으면 투석 안 해도 되고 음식도 자유롭게 먹을 수 있어요.", "vi": "Nếu ghép thận thì không cần lọc máu và có thể ăn tự do.", "situation": "informal"}], "relatedTerms": ["만성신부전", "투석", "면역억제제", "거부반응"]},
    {"slug": "duong-vao-mach-loc-mau", "korean": "투석혈관접근로", "vietnamese": "Đường vào mạch lọc máu", "hanja": None, "hanjaReading": None, "pronunciation": "투석혈관접근로", "meaningKo": "혈액투석을 위해 혈액을 충분히 빼고 넣을 수 있도록 만든 혈관 통로로, 동정맥루와 도관으로 나뉩니다. 통역 시 'Đường vào mạch lọc máu'로 표현하며, 동정맥루(AV fistula)는 수술로 동맥과 정맥을 연결하여 만들고 성숙에 6-8주 필요함을 설명해야 합니다. 투석 카테터는 응급 시 사용하지만 감염 위험이 높아 임시 방편임을 강조해야 합니다. 동정맥루의 관리(혈전 예방, 감염 예방)가 투석 치료의 성패를 좌우하므로, 환자 교육이 매우 중요합니다.", "meaningVi": "Đường thông mạch máu được tạo để rút và trả đủ máu cho lọc máu, chia thành rò động tĩnh mạch và ống thông. Rò động tĩnh mạch (AV fistula) được tạo bằng phẫu thuật nối động mạch và tĩnh mạch, cần 6-8 tuần để trưởng thành. Ống thông lọc máu dùng khi cấp cứu nhưng nguy cơ nhiễm trùng cao nên chỉ là biện pháp tạm thời. Quản lý rò động tĩnh mạch (phòng huyết khối, nhiễm trùng) quyết định thành bại điều trị lọc máu nên giáo dục bệnh nhân rất quan trọng.", "context": "신장내과, 혈관외과", "culturalNote": "투석혈관접근로는 한국 투석 환자들에게 '생명선'으로 인식되며, 동정맥루 보호에 대한 교육이 잘 되어 있습니다. 베트남 환자들에게는 생소한 개념일 수 있어, 왜 팔에 수술을 해야 하는지부터 충분히 설명해야 합니다. 동정맥루가 성숙되기 전 투석이 필요하면 카테터를 먼저 삽입하는데, 이 과정을 단계적으로 설명하는 것이 중요합니다. 동정맥루가 막히면 투석이 어려워지므로, 혈압 측정이나 채혈을 그 팔에서 하지 말아야 한다는 주의사항을 반복 교육해야 합니다.", "commonMistakes": [{"mistake": "동정맥루를 만들자마자 투석 가능하다고 설명", "correction": "6-8주 성숙 기간 필요, 그 전에는 카테터 사용", "explanation": "환자가 현실적인 치료 일정을 이해하도록 해야 합니다"}, {"mistake": "동정맥루가 있는 팔로 혈압 측정", "correction": "반대편 팔 사용, 동정맥루 보호 필수", "explanation": "혈관 접근로 보존이 투석 성공의 핵심입니다"}, {"mistake": "카테터를 영구적 접근로로 설명", "correction": "감염 위험 높아 임시 방편, 동정맥루가 우선", "explanation": "적절한 혈관 접근로 선택을 위한 정확한 정보가 필요합니다"}], "examples": [{"ko": "투석 시작 전에 동정맥루 수술을 미리 해두셔야 합니다.", "vi": "Trước khi bắt đầu lọc máu phải mổ làm rò động tĩnh mạch trước.", "situation": "formal"}, {"ko": "동정맥루가 있는 팔로는 혈압 재면 안 되고, 무거운 것도 들면 안 돼요.", "vi": "Cánh tay có rò động tĩnh mạch không được đo huyết áp và không được xách nặng.", "situation": "onsite"}, {"ko": "동정맥루에서 윙윙 소리 나는 게 정상이에요. 막히면 소리가 안 나니까 조심하세요.", "vi": "Rò động tĩnh mạch kêu ù ù là bình thường. Nếu tắc thì không kêu nên cẩn thận.", "situation": "informal"}], "relatedTerms": ["혈액투석", "동정맥루", "투석카테터", "혈전"]},
    {"slug": "ong-thong-loc-mang-bung", "korean": "복막투석카테터", "vietnamese": "Ống thông lọc màng bụng", "hanja": None, "hanjaReading": None, "pronunciation": "복막투석카테터", "meaningKo": "복막투석을 위해 복강 내에 삽입하는 카테터로, 복막을 이용하여 노폐물을 제거하는 투석 방법의 핵심 도구입니다. 통역 시 'Ống thông lọc màng bụng'으로 표현하며, 복부에 수술로 삽입하고 카테터가 피부 밖으로 나와 있음을 설명해야 합니다. 복막투석은 집에서 환자 스스로 할 수 있어 혈액투석보다 자유롭지만, 카테터 관리가 매우 중요하고 복막염 위험이 있음을 강조해야 합니다. 무균 조작법과 카테터 출구 부위 관리 교육이 필수적이며, 복막염 증상(복통, 혼탁한 배액)을 조기 발견하는 것이 중요합니다.", "meaningVi": "Ống thông đặt vào ổ bụng để lọc màng bụng, là dụng cụ cốt lõi của phương pháp lọc máu dùng màng bụng để loại bỏ chất thải. Đặt vào bụng bằng phẫu thuật, ống thông lộ ra ngoài da. Lọc màng bụng bệnh nhân có thể tự làm ở nhà nên tự do hơn lọc máu nhưng quản lý ống thông rất quan trọng và có nguy cơ viêm phúc mạc. Giáo dục thao tác vô trùng và chăm sóc lối ra ống thông là bắt buộc, quan trọng là phát hiện sớm triệu chứng viêm phúc mạc (đau bụng, dịch dẫn lưu đục).", "context": "신장내과", "culturalNote": "복막투석은 한국에서 혈액투석보다 자유로운 생활이 가능하여 선택하는 환자가 있지만, 무균 조작에 대한 교육이 필수적입니다. 베트남에서는 복막투석이 덜 보편화되어 있어, 환자와 가족에게 방법과 장단점을 충분히 설명해야 합니다. 집에서 하는 투석이므로 환자의 위생 환경과 교육 수준, 가족 지원 여부를 고려해야 합니다. 복막염은 심각한 합병증이므로, 예방과 조기 발견을 위한 철저한 교육이 필요하며, 증상 발생 시 즉시 병원 방문을 강조해야 합니다.", "commonMistakes": [{"mistake": "복막투석을 혈액투석보다 쉽다고 설명", "correction": "무균 조작 필수, 교육과 순응도 중요", "explanation": "환자가 복막투석의 책임을 이해하고 적절히 수행하도록 해야 합니다"}, {"mistake": "카테터 출구 부위 관리를 소홀히 해도 된다고 설명", "correction": "매일 소독, 감염 징후 관찰 필수", "explanation": "감염 예방이 복막투석 성공의 핵심입니다"}, {"mistake": "복막염을 가볍게 설명", "correction": "심각한 합병증, 즉시 치료 필요", "explanation": "환자가 증상 발생 시 신속히 대처하도록 교육해야 합니다"}], "examples": [{"ko": "복막투석 카테터를 삽입하고 무균 조작법을 교육받으신 후 집에서 투석하실 수 있습니다.", "vi": "Sau khi đặt ống thông lọc màng bụng và học thao tác vô trùng thì có thể lọc ở nhà.", "situation": "formal"}, {"ko": "배액이 탁하거나 배가 아프면 복막염일 수 있으니 바로 병원에 오세요.", "vi": "Nếu dịch dẫn lưu đục hoặc đau bụng thì có thể là viêm phúc mạc, hãy đến viện ngay.", "situation": "onsite"}, {"ko": "복막투석은 집에서 하니까 병원 안 다녀도 돼서 편해요.", "vi": "Lọc màng bụng làm ở nhà nên không cần đi viện, tiện lợi.", "situation": "informal"}], "relatedTerms": ["복막투석", "복막염", "무균조작", "혈액투석"]},
    {"slug": "doc-nieu", "korean": "요독증", "vietnamese": "Độc niệu", "hanja": "尿毒症", "hanjaReading": "尿(오줌 뇨) + 毒(독 독) + 症(병 증)", "pronunciation": "요독증", "meaningKo": "신부전으로 인해 노폐물이 체내에 축적되어 다양한 증상을 일으키는 상태로, 오심, 구토, 식욕부진, 가려움증, 의식 변화 등이 나타납니다. 통역 시 'Độc niệu' 또는 'Nhiễm độc niệu'로 표현하며, 투석이 필요한 말기 신부전의 증상임을 설명해야 합니다. 요독증은 다양한 장기에 영향을 미쳐 심낭염, 뇌병증, 빈혈, 출혈 경향 등을 유발할 수 있으므로, 적시에 투석을 시작하는 것이 중요함을 강조해야 합니다. 투석 시작 후 증상이 호전될 수 있으나, 일부 증상(가려움증 등)은 지속될 수 있음을 안내해야 합니다.", "meaningVi": "Tình trạng chất thải tích tụ trong cơ thể do suy thận gây ra nhiều triệu chứng như buồn nôn, nôn, chán ăn, ngứa, thay đổi ý thức. Là triệu chứng suy thận giai đoạn cuối cần lọc máu. Độc niệu ảnh hưởng đến nhiều cơ quan gây viêm màng ngoài tim, bệnh não, thiếu máu, xu hướng chảy máu nên quan trọng là bắt đầu lọc máu đúng lúc. Sau khi bắt đầu lọc máu triệu chứng có thể cải thiện nhưng một số triệu chứng (ngứa) có thể tiếp tục.", "context": "신장내과", "culturalNote": "요독증은 한국에서 '몸에 독소가 쌓였다'는 개념으로 환자들이 이해하기 쉬우며, 베트남어 'Độc niệu'도 비슷한 의미를 전달합니다. 환자들이 투석을 미루다가 요독증이 심해져서 응급으로 내원하는 경우가 많은데, 적절한 시기에 투석을 시작하는 것이 중요함을 교육해야 합니다. 요독증 증상이 비특이적(피로, 식욕부진 등)이어서 환자들이 간과하기 쉬우므로, 신부전 환자의 정기 검진 중요성을 강조해야 합니다. 투석 시작 후 증상 호전을 경험하면 치료 순응도가 높아지므로, 투석의 효과를 긍정적으로 설명하는 것이 도움이 됩니다.", "commonMistakes": [{"mistake": "요독증을 단순 피로로 치부", "correction": "투석 시작의 신호, 즉시 평가 필요", "explanation": "투석 시작 시기를 놓치지 않도록 증상의 심각성을 전달해야 합니다"}, {"mistake": "투석 시작하면 모든 증상이 즉시 사라진다고 설명", "correction": "증상 호전되지만 일부는 지속 가능", "explanation": "현실적인 기대를 설정하도록 도와야 합니다"}, {"mistake": "요독증을 감염으로 오인", "correction": "신부전에 의한 대사 장애", "explanation": "정확한 병태생리 이해가 적절한 치료로 이어집니다"}], "examples": [{"ko": "요독증 증상이 심해서 투석을 시작해야 할 시기입니다.", "vi": "Triệu chứng độc niệu nặng nên đã đến lúc phải bắt đầu lọc máu.", "situation": "formal"}, {"ko": "몸이 가렵고 입맛이 없는 건 몸에 독소가 쌓여서 그래요.", "vi": "Ngứa và chán ăn là do chất độc tích tụ trong cơ thể.", "situation": "onsite"}, {"ko": "투석 시작하면 구역질하고 가려운 게 좀 나아질 거예요.", "vi": "Nếu bắt đầu lọc máu thì buồn nôn và ngứa sẽ bớt.", "situation": "informal"}], "relatedTerms": ["만성신부전", "투석", "오심", "가려움증"]},
    {"slug": "roi-loan-dien-giai", "korean": "전해질불균형", "vietnamese": "Rối loạn điện giải", "hanja": "電解質不均衡", "hanjaReading": "電(번개 전) + 解(풀 해) + 質(바탕 질) + 不(아닐 불) + 均(고를 균) + 衡(저울 형)", "pronunciation": "전해질불균형", "meaningKo": "혈액 내 전해질(나트륨, 칼륨, 칼슘 등)의 농도가 정상 범위를 벗어난 상태로, 다양한 원인과 증상을 보입니다. 통역 시 'Rối loạn điện giải'로 표현하며, 신부전, 구토, 설사, 약물 등이 원인이 될 수 있음을 설명해야 합니다. 고칼륨혈증은 심장 부정맥을 유발하여 생명을 위협할 수 있고, 저나트륨혈증은 의식 변화와 경련을 일으킬 수 있어, 적절한 교정이 필수적입니다. 전해질 농도에 따라 치료 강도가 달라지므로, 정확한 수치를 환자에게 전달하고 식이 조절이나 약물 치료의 중요성을 강조해야 합니다.", "meaningVi": "Tình trạng nồng độ điện giải trong máu (natri, kali, canxi, v.v.) vượt ra khỏi phạm vi bình thường, có nhiều nguyên nhân và triệu chứng. Nguyên nhân có thể là suy thận, nôn, tiêu chảy, thuốc. Tăng kali máu có thể gây loạn nhịp tim đe dọa tính mạng, giảm natri máu có thể gây thay đổi ý thức và co giật nên điều chỉnh thích hợp là bắt buộc. Tùy nồng độ điện giải mà cường độ điều trị khác nhau nên cần truyền đạt chính xác số liệu cho bệnh nhân và nhấn mạnh tầm quan trọng của điều chỉnh chế độ ăn hoặc điều trị thuốc.", "context": "신장내과, 응급의학", "culturalNote": "전해질불균형은 한국에서 혈액검사 결과로 설명할 때 환자들이 '나트륨', '칼륨' 등의 용어를 들어봤지만 정확한 의미는 모르는 경우가 많습니다. 베트남 환자에게도 'natri', 'kali' 등의 용어를 사용하되, 왜 중요한지를 쉽게 설명하는 것이 필요합니다. 고칼륨혈증은 신부전 환자에서 흔하고 생명을 위협할 수 있으므로, 고칼륨 식품(바나나, 토마토, 오렌지 등) 제한의 중요성을 강조해야 합니다. 저나트륨혈증은 노인이나 이뇨제 복용 환자에서 흔한데, 급격한 교정은 위험하므로 천천히 교정함을 설명해야 합니다.", "commonMistakes": [{"mistake": "전해질 불균형을 대수롭지 않게 설명", "correction": "심각한 부정맥이나 경련 유발 가능", "explanation": "환자가 치료의 긴급성을 이해하도록 해야 합니다"}, {"mistake": "모든 전해질 이상을 동일하게 치료", "correction": "전해질 종류와 농도에 따라 치료 달라짐", "explanation": "적절한 맞춤 치료를 위해 정확한 정보가 필요합니다"}, {"mistake": "급격한 교정을 권장", "correction": "특히 저나트륨혈증은 천천히 교정 필요", "explanation": "급격한 교정은 삼투성 탈수초증 등 심각한 합병증을 유발할 수 있습니다"}], "examples": [{"ko": "칼륨이 높아서 위험하니 고칼륨 음식을 피하시고 약을 드셔야 합니다.", "vi": "Kali cao nguy hiểm nên phải tránh đồ ăn giàu kali và uống thuốc.", "situation": "formal"}, {"ko": "나트륨이 너무 낮으면 의식이 흐려질 수 있어요.", "vi": "Nếu natri quá thấp thì ý thức có thể mơ hồ.", "situation": "onsite"}, {"ko": "신부전 있으면 바나나 같은 과일 조심해야 해요. 칼륨이 높아요.", "vi": "Nếu suy thận thì phải cẩn thận trái cây như chuối. Kali cao.", "situation": "informal"}], "relatedTerms": ["고칼륨혈증", "저나트륨혈증", "부정맥", "신부전"]},
    {"slug": "toan-chuyen-hoa", "korean": "대사성산증", "vietnamese": "Toan chuyển hóa", "hanja": "代謝性酸症", "hanjaReading": "代(대신할 대) + 謝(사례할 사) + 性(성품 성) + 酸(신 산) + 症(병 증)", "pronunciation": "대사성산증", "meaningKo": "혈액의 pH가 낮아져 산성화되는 대사 장애로, 신부전, 당뇨병성 케톤산증, 설사 등이 원인입니다. 통역 시 'Toan chuyển hóa'로 표현하며, 호흡이 빨라지는 보상 기전(쿠스마울 호흡)이 특징적임을 설명해야 합니다. 동맥혈가스분석으로 진단하며, pH와 HCO3- 수치를 확인합니다. 원인 질환 치료가 우선이며, 중증인 경우 중탄산나트륨 투여나 투석이 필요할 수 있습니다. 만성 신부전 환자에서 흔하므로, 정기적인 혈액검사로 모니터링하고 중탄산나트륨 복용의 중요성을 강조해야 합니다.", "meaningVi": "Rối loạn chuyển hóa làm pH máu giảm, máu trở nên acid, nguyên nhân là suy thận, nhiễm toan ceton do đái tháo đường, tiêu chảy. Đặc trưng là cơ chế bù trừ làm thở nhanh (thở Kussmaul). Chẩn đoán bằng phân tích khí máu động mạch, kiểm tra pH và HCO3-. Ưu tiên điều trị bệnh nguyên nhân, trường hợp nặng có thể cần truyền natri bicarbonat hoặc lọc máu. Thường gặp ở bệnh nhân suy thận mạn nên cần theo dõi bằng xét nghiệm máu định kỳ và nhấn mạnh tầm quan trọng uống natri bicarbonat.", "context": "신장내과, 응급의학, 내분비내과", "culturalNote": "대사성산증은 한국에서 중환자실이나 응급실에서 흔히 접하는 개념이지만, 일반 환자들에게는 생소하여 'pH', '산성' 등의 용어를 쉽게 풀어 설명해야 합니다. 베트남 환자에게도 '혈액이 산성으로 기운다'는 개념을 이해시키기 위해 비유를 사용할 수 있습니다. 만성 신부전 환자는 대사성산증을 보상하기 위해 중탄산나트륨을 복용해야 하는데, 약의 필요성을 이해시키는 것이 중요합니다. 당뇨병성 케톤산증은 응급 상황이므로, 당뇨 환자에게 증상(호흡 곤란, 의식 변화)을 교육하여 조기 대처하도록 해야 합니다.", "commonMistakes": [{"mistake": "산증을 단순 피로로 설명", "correction": "심각한 대사 장애, 원인 규명과 치료 필요", "explanation": "환자가 질환의 심각성을 이해하도록 해야 합니다"}, {"mistake": "중탄산나트륨을 불필요한 약으로 설명", "correction": "산증 교정과 뼈 건강에 중요", "explanation": "약물 순응도를 높이기 위해 복용 목적을 명확히 해야 합니다"}, {"mistake": "호흡 빨라짐을 폐 질환으로 오인", "correction": "산증에 대한 보상 기전", "explanation": "정확한 병태생리 이해가 적절한 치료로 이어집니다"}], "examples": [{"ko": "신부전으로 대사성산증이 있어서 중탄산나트륨을 드셔야 합니다.", "vi": "Do suy thận có toan chuyển hóa nên phải uống natri bicarbonat.", "situation": "formal"}, {"ko": "혈액이 산성으로 기울어서 호흡이 빨라진 거예요.", "vi": "Máu nghiêng về acid nên thở nhanh.", "situation": "onsite"}, {"ko": "당뇨 환자가 숨이 가쁘고 의식이 흐려지면 응급실로 가야 해요.", "vi": "Nếu bệnh nhân đái tháo đường thở gấp và ý thức mơ hồ thì phải đến cấp cứu.", "situation": "informal"}], "relatedTerms": ["신부전", "당뇨병성케톤산증", "동맥혈가스분석", "중탄산나트륨"]},
    {"slug": "tang-kali-mau", "korean": "고칼륨혈증", "vietnamese": "Tăng kali máu", "hanja": "高칼륨血症", "hanjaReading": "高(높을 고) + 칼륨 + 血(피 혈) + 症(병 증)", "pronunciation": "고칼륨혈증", "meaningKo": "혈중 칼륨 농도가 정상보다 높은 상태로, 심장 부정맥을 유발하여 생명을 위협할 수 있는 응급 상황입니다. 통역 시 'Tăng kali máu'로 표현하며, 신부전이 가장 흔한 원인이고 고칼륨 식품 섭취나 약물도 원인이 될 수 있음을 설명해야 합니다. 심전도에서 T파 증가, QRS 폭 증가 등의 변화가 나타나며, 중증인 경우 칼슘 주사, 인슐린-포도당 요법, 투석 등의 응급 치료가 필요합니다. 신부전 환자는 고칼륨 식품(바나나, 토마토, 오렌지, 멜론 등) 제한이 매우 중요함을 반복 교육해야 합니다.", "meaningVi": "Tình trạng nồng độ kali trong máu cao hơn bình thường, có thể gây loạn nhịp tim đe dọa tính mạng, là tình huống cấp cứu. Nguyên nhân thường gặp nhất là suy thận, ăn thức ăn giàu kali hoặc thuốc cũng có thể là nguyên nhân. Điện tâm đồ có thay đổi như sóng T tăng, phức QRS giãn rộng, trường hợp nặng cần điều trị cấp cứu như tiêm canxi, liệu pháp insulin-glucose, lọc máu. Bệnh nhân suy thận hạn chế thức ăn giàu kali (chuối, cà chua, cam, dưa) rất quan trọng, cần giáo dục lặp lại.", "context": "신장내과, 응급의학", "culturalNote": "고칼륨혈증은 한국 신부전 환자들이 식이 관리에서 가장 어려워하는 부분으로, 과일과 채소 제한이 필요하여 식단이 제한적입니다. 베트남 식문화에서도 과일 섭취가 많으므로, 고칼륨 과일을 피하고 저칼륨 과일(사과, 배, 수박 소량 등)을 선택하도록 구체적으로 교육해야 합니다. 응급 상황에서는 칼슘 주사나 인슐린-포도당 요법으로 신속히 칼륨을 낮춰야 하므로, 환자와 가족에게 치료의 긴급성을 설명하는 것이 중요합니다. 만성 관리를 위해서는 칼륨 배설 촉진제(케이엑세레이트 등) 복용과 식이 조절을 병행해야 함을 강조해야 합니다.", "commonMistakes": [{"mistake": "고칼륨 식품을 대략적으로만 설명", "correction": "구체적 식품 목록과 대체 식품 제시", "explanation": "실천 가능한 식이 지침이 순응도를 높입니다"}, {"mistake": "증상이 없으면 안전하다고 설명", "correction": "무증상이어도 심전도 변화 있으면 위험", "explanation": "정기 혈액검사와 심전도의 중요성을 강조해야 합니다"}, {"mistake": "모든 과일을 금지", "correction": "저칼륨 과일은 소량 섭취 가능", "explanation": "과도한 제한은 순응도를 떨어뜨리므로 균형잡힌 지침이 필요합니다"}], "examples": [{"ko": "칼륨이 위험할 정도로 높아서 응급 치료가 필요합니다.", "vi": "Kali cao đến mức nguy hiểm nên cần điều trị cấp cứu.", "situation": "formal"}, {"ko": "바나나, 토마토, 오렌지는 칼륨이 높으니 피하시고 사과나 배는 괜찮아요.", "vi": "Chuối, cà chua, cam có kali cao nên tránh, táo hoặc lê thì được.", "situation": "onsite"}, {"ko": "신부전 있으면 과일 조심해야 해요. 칼륨 때문에 심장 문제 생길 수 있어요.", "vi": "Nếu suy thận thì phải cẩn thận trái cây. Vì kali có thể gây vấn đề tim.", "situation": "informal"}], "relatedTerms": ["신부전", "부정맥", "심전도", "저칼륨식이"]},
    {"slug": "giam-natri-mau", "korean": "저나트륨혈증", "vietnamese": "Giảm natri máu", "hanja": "低나트륨血症", "hanjaReading": "低(낮을 저) + 나트륨 + 血(피 혈) + 症(병 증)", "pronunciation": "저나트륨혈증", "meaningKo": "혈중 나트륨 농도가 정상보다 낮은 상태로, 두통, 오심, 혼돈, 경련 등을 유발할 수 있습니다. 통역 시 'Giảm natri máu'로 표현하며, 원인이 다양(심부전, 간경변, 이뇨제, 과다 수분 섭취 등)하므로 정확한 진단이 필요함을 설명해야 합니다. 급성이고 중증인 경우 뇌부종과 경련을 유발할 수 있어 응급 치료가 필요하지만, 너무 빠른 교정은 삼투성 탈수초증을 일으킬 수 있어 천천히 교정해야 함을 강조해야 합니다. 만성 저나트륨혈증은 수분 제한과 원인 질환 치료가 중요하며, 노인과 이뇨제 복용 환자에서 흔함을 안내해야 합니다.", "meaningVi": "Tình trạng nồng độ natri trong máu thấp hơn bình thường, có thể gây đau đầu, buồn nôn, lú lẫn, co giật. Nguyên nhân đa dạng (suy tim, xơ gan, thuốc lợi tiểu, uống nước quá nhiều) nên cần chẩn đoán chính xác. Nếu cấp và nặng có thể gây phù não và co giật cần điều trị cấp cứu nhưng điều chỉnh quá nhanh có thể gây chứng tổn thương tủy do thẩm thấu nên phải điều chỉnh từ từ. Giảm natri máu mạn cần hạn chế nước và điều trị bệnh nguyên nhân, thường gặp ở người già và người uống thuốc lợi tiểu.", "context": "신장내과, 응급의학, 내과", "culturalNote": "저나트륨혈증은 한국에서 노인 환자와 이뇨제 복용 환자에서 흔하며, 증상이 비특이적(피로, 어지러움)이어서 간과되기 쉽습니다. 베트남 환자들도 비슷한 증상을 단순 노화나 피로로 치부할 수 있어, 정기 혈액검사의 중요성을 강조해야 합니다. 수분 제한이 치료의 일부인 경우, 환자들이 '물을 많이 마셔야 건강하다'는 일반적 인식과 상충되어 혼란스러워할 수 있으므로, 저나트륨혈증에서는 수분 제한이 필요한 이유를 명확히 설명해야 합니다. 급격한 교정의 위험성은 의료진에게 중요하지만, 환자에게는 '천천히 치료한다'는 정도로 간단히 설명하는 것이 좋습니다.", "commonMistakes": [{"mistake": "소금을 많이 먹으라고 권장", "correction": "원인에 따라 치료 다름, 자가 치료 금지", "explanation": "부적절한 자가 치료는 상태를 악화시킬 수 있습니다"}, {"mistake": "급격한 교정을 요구", "correction": "너무 빠른 교정은 위험, 천천히 해야", "explanation": "삼투성 탈수초증 예방을 위해 교정 속도가 중요합니다"}, {"mistake": "모든 저나트륨혈증을 동일하게 치료", "correction": "혈장 삼투압 상태에 따라 치료 달라짐", "explanation": "정확한 진단과 분류가 적절한 치료로 이어집니다"}], "examples": [{"ko": "나트륨이 낮아서 수분 섭취를 하루 1리터로 제한하셔야 합니다.", "vi": "Natri thấp nên phải hạn chế uống nước 1 lít mỗi ngày.", "situation": "formal"}, {"ko": "나트륨이 너무 빨리 올라가면 위험해서 천천히 교정하고 있어요.", "vi": "Nếu natri tăng quá nhanh thì nguy hiểm nên đang điều chỉnh từ từ.", "situation": "onsite"}, {"ko": "이뇨제 먹으면 나트륨이 낮아질 수 있으니 정기적으로 검사받으세요.", "vi": "Nếu uống thuốc lợi tiểu thì natri có thể giảm nên hãy xét nghiệm định kỳ.", "situation": "informal"}], "relatedTerms": ["이뇨제", "수분제한", "경련", "의식변화"]},
    {"slug": "sinh-thiet-than", "korean": "신장생검", "vietnamese": "Sinh thiết thận", "hanja": "腎臟生檢", "hanjaReading": "腎(콩팥 신) + 臟(장부 장) + 生(날 생) + 檢(검사할 검)", "pronunciation": "신장생검", "meaningKo": "신장 조직을 채취하여 현미경으로 검사하는 진단 방법으로, 사구체신염, 신증후군 등의 정확한 진단과 예후 판정에 필수적입니다. 통역 시 'Sinh thiết thận'으로 표현하며, 초음파 유도 하에 바늘로 신장 조직을 채취하고 출혈 예방을 위해 검사 후 안정이 필요함을 설명해야 합니다. 합병증으로 혈뇨, 혈종, 드물게 심한 출혈이 있을 수 있으나 대부분 안전하며, 얻을 수 있는 진단적 정보의 가치가 크다는 점을 강조해야 합니다. 검사 전 혈액 응고 기능 확인과 항혈소판제 중단이 필요하며, 검사 후 주의사항을 명확히 교육해야 합니다.", "meaningVi": "Phương pháp chẩn đoán lấy mô thận để kiểm tra bằng kính hiển vi, cần thiết để chẩn đoán chính xác và đánh giá tiên lượng viêm cầu thận, hội chứng thận. Lấy mô thận bằng kim dưới hướng dẫn siêu âm, sau xét nghiệm cần nghỉ ngơi để phòng chảy máu. Biến chứng có thể có tiểu ra máu, khối máu tụ, hiếm khi chảy máu nặng nhưng phần lớn an toàn, giá trị thông tin chẩn đoán thu được lớn. Trước xét nghiệm cần kiểm tra chức năng đông máu và ngừng thuốc chống kết tập tiểu cầu, sau xét nghiệm cần hướng dẫn lưu ý rõ ràng.", "context": "신장내과", "culturalNote": "신장생검은 한국에서 신장 질환 진단에 표준적으로 사용되지만, 환자들이 침습적 검사를 두려워하여 거부하는 경우가 있습니다. 베트남 환자들도 비슷한 불안을 느낄 수 있으므로, 검사의 안전성과 필요성을 충분히 설명하여 동의를 구해야 합니다. 검사 후 절대 안정이 필요한데, 한국 병원에서는 24시간 침상 안정을 권장하지만 환자들이 불편해할 수 있어 그 이유를 설명해야 합니다. 조직검사 결과가 나오기까지 시간(보통 1-2주)이 걸리므로, 환자의 불안을 달래면서 결과를 기다리도록 안내하는 것이 중요합니다.", "commonMistakes": [{"mistake": "생검을 과도하게 위험하다고 설명", "correction": "합병증 가능하나 대부분 안전, 진단에 중요", "explanation": "필요한 검사를 환자가 거부하지 않도록 균형잡힌 정보 제공이 필요합니다"}, {"mistake": "검사 후 주의사항을 대략적으로만 설명", "correction": "절대 안정, 수분 섭취, 출혈 징후 관찰 구체적 설명", "explanation": "합병증 예방을 위한 세부 지침이 필수적입니다"}, {"mistake": "항혈소판제 중단의 중요성을 간과", "correction": "검사 1주일 전부터 아스피린 등 중단 필요", "explanation": "출혈 위험 최소화를 위한 준비가 중요합니다"}], "examples": [{"ko": "정확한 진단을 위해 신장 조직검사를 권합니다. 대부분 안전한 검사입니다.", "vi": "Để chẩn đoán chính xác khuyến cáo sinh thiết thận. Phần lớn là xét nghiệm an toàn.", "situation": "formal"}, {"ko": "생검 후 24시간은 침대에서 절대 안정하시고, 소변에 피 많이 섞이면 알려주세요.", "vi": "Sau sinh thiết 24 giờ phải nằm yên trên giường tuyệt đối, nếu tiểu ra máu nhiều hãy báo.", "situation": "onsite"}, {"ko": "조직검사 결과는 2주 후에 나오니까 그때 다시 오세요.", "vi": "Kết quả sinh thiết ra sau 2 tuần nên lúc đó hãy đến lại.", "situation": "informal"}], "relatedTerms": ["사구체신염", "신증후군", "단백뇨", "혈뇨"]},
])

# Load existing medical.json
with open(file_path, 'r', encoding='utf-8') as f:
    data = json.load(f)

print(f"Loaded {len(data)} existing terms from medical.json")

# Add new terms
data.extend(new_terms)
print(f"Added {len(new_terms)} new terms")
print(f"Total terms now: {len(data)}")

# Save back to medical.json
with open(file_path, 'w', encoding='utf-8') as f:
    json.dump(data, f, ensure_ascii=False, indent=2)

print(f"\nSuccessfully updated {file_path}")
print(f"Total medical terms: {len(data)}")
