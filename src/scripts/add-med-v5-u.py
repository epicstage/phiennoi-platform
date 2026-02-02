#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
의료 도메인 용어 추가 스크립트 v5-u
Theme: 심장/순환기/혈액 (Cardiology/Hematology)
Quality: Tier S (90+ score)
"""

import json
import os

# 파일 경로 설정
file_path = os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', 'data', 'terms', 'medical.json')

# 추가할 10개 용어 (Tier S 품질 기준 충족)
new_terms = [
    {
        "slug": "nhoi-mau-co-tim",
        "korean": "심근경색",
        "vietnamese": "Nhồi máu cơ tim",
        "hanja": "心筋梗塞",
        "hanjaReading": "心(마음 심) + 筋(힘줄 근) + 梗(막힐 경) + 塞(막힐 새)",
        "pronunciation": "녀이 머우 커 띰",
        "meaningKo": "심장 근육에 혈액 공급이 차단되어 심장 조직이 괴사하는 응급 질환입니다. 통역 시 '심장마비'라는 구어적 표현과 구분해야 하며, 베트남어로는 '급성 심근경색(Nhồi máu cơ tim cấp)'과 '만성(mạn tính)'을 명확히 구분해야 합니다. 한국에서는 119 골든타임을 강조하지만, 베트남에서는 115 응급전화 시스템이 다르므로 통역 시 주의가 필요합니다. 증상 설명 시 '가슴 통증(đau ngực)', '식은땀(đổ mồ hôi lạnh)', '호흡곤란(khó thở)' 등을 정확히 전달해야 환자 생명과 직결됩니다.",
        "meaningVi": "Tình trạng nghiêm trọng xảy ra khi dòng máu đến cơ tim bị tắc nghẽn, dẫn đến hoại tử mô tim. Đây là tình huống cấp cứu y tế đòi hỏi xử lý khẩn trương trong vòng vài giờ đầu tiên. Triệu chứng điển hình bao gồm đau ngực dữ dội, đổ mồ hôi lạnh, và khó thở. Tại Hàn Quốc, hệ thống cấp cứu 119 rất phát triển với thời gian vàng (golden time) được nhấn mạnh trong điều trị.",
        "context": "응급실, 심장내과, 중환자실에서 사용. 환자 및 보호자 상담 시 필수 용어",
        "culturalNote": "한국은 급성 심근경색 치료 시스템이 매우 발달해 있어 '골든타임 2시간' 개념이 보편화되어 있으나, 베트남은 응급의료 인프라 격차가 지역별로 크므로 통역 시 이를 고려해야 합니다. 한국 환자는 스텐트 시술(can thiệp mạch vành)을 당연시하지만 베트남에서는 비용 부담이 커서 보존적 치료를 선호하는 경우가 많습니다. 또한 한국은 심근경색 후 심장재활 프로그램이 체계적이나 베트남은 아직 초기 단계입니다.",
        "commonMistakes": [
            {
                "mistake": "심장마비로 번역",
                "correction": "심근경색(Nhồi máu cơ tim)과 심정지(Ngừng tim)를 구분",
                "explanation": "심장마비는 구어체이며 의학적으로는 심근경색과 심정지를 명확히 구분해야 합니다"
            },
            {
                "mistake": "Đau tim으로 단순 번역",
                "correction": "Nhồi máu cơ tim (정확한 의학 용어)",
                "explanation": "Đau tim은 단순 '심장 통증'이며 심근경색의 의학적 정의를 담지 못합니다"
            },
            {
                "mistake": "응급도를 과소평가하여 통역",
                "correction": "응급 상황(tình huống cấp cứu), 생명 위협(đe dọa tính mạng) 강조",
                "explanation": "심근경색의 치명성을 베트남 환자에게 충분히 전달하지 못하면 치료 지연으로 이어집니다"
            },
            {
                "mistake": "Cơn đau tim (심장 발작) 혼용",
                "correction": "Nhồi máu cơ tim (조직 괴사 강조)",
                "explanation": "Cơn đau tim은 일시적 증상으로 오해될 수 있어 조직 손상을 명확히 해야 합니다"
            }
        ],
        "examples": [
            {
                "ko": "환자분이 급성 심근경색으로 응급실에 내원하셨습니다.",
                "vi": "Bệnh nhân được chuyển đến phòng cấp cứu do nhồi máu cơ tim cấp.",
                "situation": "formal"
            },
            {
                "ko": "가슴 통증이 30분 이상 지속되면 심근경색을 의심해야 합니다.",
                "vi": "Nếu đau ngực kéo dài hơn 30 phút, cần nghi ngờ nhồi máu cơ tim.",
                "situation": "onsite"
            },
            {
                "ko": "스텐트 시술로 막힌 혈관을 뚫었습니다.",
                "vi": "Chúng tôi đã thông mạch bằng kỹ thuật đặt stent.",
                "situation": "formal"
            }
        ],
        "relatedTerms": ["협심증", "관상동맥질환", "심정지", "심전도", "스텐트 시술"]
    },
    {
        "slug": "roi-loan-nhip-tim",
        "korean": "부정맥",
        "vietnamese": "Rối loạn nhịp tim",
        "hanja": "不整脈",
        "hanjaReading": "不(아닐 부) + 整(가지런할 정) + 脈(맥 맥)",
        "pronunciation": "조이 로안 늡 띰",
        "meaningKo": "심장이 불규칙하게 뛰거나 너무 빠르거나 느리게 뛰는 상태를 말합니다. 통역 시 '심장이 두근거린다'는 환자 표현을 정확한 의학 용어로 전환해야 하며, 빈맥(nhanh tim)과 서맥(chậm tim)을 구분해야 합니다. 베트남 환자는 부정맥을 단순 스트레스로 오해하는 경우가 많아 정확한 진단 필요성을 강조해야 합니다. 한국에서는 웨어러블 기기로 일상 모니터링이 보편화되어 있으나 베트nam에서는 아직 홀터 검사(Holter) 접근성이 낮습니다.",
        "meaningVi": "Tình trạng tim đập không đều, quá nhanh hoặc quá chậm so với nhịp bình thường. Có thể gây chóng mặt, mệt mỏi, hoặc ngất xĩu. Tại Hàn Quốc, việc phát hiện sớm qua thiết bị đeo tay thông minh rất phổ biến, trong khi tại Việt Nam chủ yếu phát hiện qua điện tâm đồ (ECG) khi có triệu chứng rõ ràng. Điều trị có thể bao gồm thuốc, máy tạo nhịp tim, hoặc phẫu thuật đốt điện.",
        "context": "심장내과, 응급실, 건강검진 결과 상담 시 사용",
        "culturalNote": "한국에서는 애플워치 등으로 심방세동을 조기 발견하는 사례가 많으나, 베트남에서는 아직 웨어러블 헬스케어가 보편화되지 않았습니다. 한국 환자는 부정맥 약물 복용에 적극적이나 베트남 환자는 한약이나 민간요법을 병행하려는 경향이 있어 약물 상호작용 확인이 필요합니다. 또한 한국은 전극도자절제술(phẫu thuật đốt điện) 보험 적용이 확대되었으나 베트남은 고비용 치료로 분류됩니다.",
        "commonMistakes": [
            {
                "mistake": "Tim đập nhanh로만 번역",
                "correction": "Rối loạn nhịp tim (포괄적 개념) + 세부 유형 구분",
                "explanation": "부정맥은 빠른 박동뿐 아니라 느린 박동, 불규칙 박동을 모두 포함합니다"
            },
            {
                "mistake": "두근거림(hồi hộp)과 혼동",
                "correction": "Rối loạn nhịp tim (의학적 이상) vs hồi hộp (감정적 반응)",
                "explanation": "환자가 느끼는 주관적 증상과 의학적 진단을 구분해야 합니다"
            },
            {
                "mistake": "심방세동을 일반 부정맥으로 통역",
                "correction": "Rung nhĩ (심방세동) - 뇌졸중 위험 강조",
                "explanation": "심방세동은 뇌졸중 위험이 높아 항응고제 치료가 필수임을 전달해야 합니다"
            }
        ],
        "examples": [
            {
                "ko": "홀터 검사 결과 심방세동이 발견되었습니다.",
                "vi": "Kết quả Holter cho thấy bệnh nhân bị rung nhĩ.",
                "situation": "formal"
            },
            {
                "ko": "가슴이 두근거리고 숨이 차시나요?",
                "vi": "Anh/chị có cảm thấy tim đập nhanh và khó thở không?",
                "situation": "onsite"
            },
            {
                "ko": "부정맥 치료를 위해 전극도자절제술이 필요합니다.",
                "vi": "Cần phẫu thuật đốt điện để điều trị rối loạn nhịp tim.",
                "situation": "formal"
            }
        ],
        "relatedTerms": ["심방세동", "빈맥", "서맥", "심전도", "홀터검사"]
    },
    {
        "slug": "suy-tim",
        "korean": "심부전",
        "vietnamese": "Suy tim",
        "hanja": "心不全",
        "hanjaReading": "心(마음 심) + 不(아닐 부) + 全(온전할 전)",
        "pronunciation": "쑤이 띰",
        "meaningKo": "심장이 전신에 필요한 혈액을 충분히 공급하지 못하는 만성 질환입니다. 통역 시 급성과 만성을 구분하고, 좌심실 부전과 우심실 부전의 차이를 설명해야 합니다. 한국에서는 '심장이 약해졌다'는 표현을 의학적으로 정확히 전달해야 하며, 베트남 환자에게는 염분 제한(hạn chế muối)과 수분 조절의 중요성을 강조해야 합니다. 한국은 심부전 클리닉과 재활 프로그램이 체계적이나 베트남은 말기까지 방치되는 경우가 많아 조기 진단의 중요성을 각별히 통역해야 합니다.",
        "meaningVi": "Tình trạng tim không thể bơm đủ máu để đáp ứng nhu cầu của cơ thể. Có thể là cấp tính hoặc mạn tính. Triệu chứng bao gồm khó thở, mệt mỏi, sưng phù chân. Tại Hàn Quốc, bệnh nhân được theo dõi sát sao qua phòng khám suy tim chuyên khoa với chế độ ăn kiêng nghiêm ngặt (hạn chế muối dưới 5g/ngày), trong khi Việt Nam chưa có hệ thống quản lý bệnh mạn tính toàn diện.",
        "context": "심장내과, 노인병과, 만성질환 관리 상담에서 사용",
        "culturalNote": "한국은 심부전 환자를 위한 다학제 팀(의사, 간호사, 영양사, 물리치료사)이 체계적으로 관리하나 베트남은 의사 중심의 단편적 치료가 일반적입니다. 한국 환자는 매일 체중 측정과 부종 관찰을 교육받지만 베트남 환자는 이런 자가관리 개념이 낯설 수 있습니다. 또한 한국은 심장이식이 보험 적용되나 베트남은 극소수 병원에서만 가능하고 비용이 매우 높습니다.",
        "commonMistakes": [
            {
                "mistake": "Tim yếu로 단순 번역",
                "correction": "Suy tim (의학 진단명)",
                "explanation": "Tim yếu는 구어적 표현이며 정확한 의학 용어는 Suy tim입니다"
            },
            {
                "mistake": "급성과 만성 구분 없이 통역",
                "correction": "Suy tim cấp vs Suy tim mạn",
                "explanation": "치료 접근과 예후가 완전히 다르므로 반드시 구분해야 합니다"
            },
            {
                "mistake": "좌/우심실 부전을 구분하지 않음",
                "correction": "Suy tim trái (호흡곤란) vs Suy tim phải (부종)",
                "explanation": "증상과 치료가 다르므로 정확한 위치를 전달해야 합니다"
            }
        ],
        "examples": [
            {
                "ko": "심부전으로 인해 폐에 물이 찼습니다.",
                "vi": "Do suy tim, phổi bị tràn dịch.",
                "situation": "formal"
            },
            {
                "ko": "염분 섭취를 하루 5g 이하로 제한하세요.",
                "vi": "Hãy hạn chế lượng muối dưới 5g mỗi ngày.",
                "situation": "onsite"
            },
            {
                "ko": "발이 붓거나 체중이 갑자기 늘면 즉시 병원에 오세요.",
                "vi": "Nếu chân sưng hoặc cân nặng tăng đột ngột, hãy đến bệnh viện ngay.",
                "situation": "onsite"
            }
        ],
        "relatedTerms": ["좌심실부전", "우심실부전", "폐부종", "심장이식", "박출률"]
    },
    {
        "slug": "tang-huyet-ap",
        "korean": "고혈압",
        "vietnamese": "Tăng huyết áp",
        "hanja": "高血壓",
        "hanjaReading": "高(높을 고) + 血(피 혈) + 壓(누를 압)",
        "pronunciation": "땅 후옛 압",
        "meaningKo": "혈압이 정상 범위보다 지속적으로 높은 상태를 말하며, 수축기 140mmHg 이상 또는 이완기 90mmHg 이상일 때 진단합니다. 통역 시 '혈압이 높다'는 표현을 정확한 수치와 함께 전달해야 하며, 베트남 환자에게는 한국의 혈압 기준과 베트남 기준이 동일함을 안내해야 합니다. 한국에서는 가정혈압 측정이 보편화되어 있으나 베트남은 병원 측정에 의존하는 경우가 많아 백의고혈압(huyết áp áo blouse trắng) 가능성을 설명해야 합니다. 또한 한국은 약물 순응도가 높으나 베트남은 증상 없으면 복약 중단하는 경향이 있어 합병증 위험을 강조해야 합니다.",
        "meaningVi": "Tình trạng huyết áp cao liên tục trên mức bình thường (≥140/90 mmHg). Đây là yếu tố nguy cơ chính gây đột quỵ, nhồi máu cơ tim, và suy thận. Tại Hàn Quốc, bệnh nhân được khuyến khích đo huyết áp tại nhà mỗi ngày, trong khi Việt Nam chủ yếu đo tại bệnh viện. Điều trị bao gồm thay đổi lối sống (giảm muối, tập thể dục) và thuốc hạ huyết áp.",
        "context": "내과, 건강검진, 만성질환 관리, 약국 상담에서 사용",
        "culturalNote": "한국은 고혈압을 '침묵의 살인자'로 인식하고 적극 치료하나, 베트남은 증상이 없으면 심각하게 여기지 않는 경향이 있습니다. 한국 환자는 가정용 혈압계(máy đo huyết áp gia đình)를 흔히 사용하지만 베트남 환자는 병원 방문 시에만 측정하는 경우가 많습니다. 또한 한국은 저염 식단이 강조되나 베트남 음식은 느억맘(nước mắm) 등 염분이 높아 식단 조절이 어렵습니다. 한국은 복합제(thuốc phối hợp) 사용이 많으나 베트남은 개별 약물을 선호합니다.",
        "commonMistakes": [
            {
                "mistake": "Huyết áp cao (단순 높은 혈압)로만 번역",
                "correction": "Tăng huyết áp (진단명) + 단계(giai đoạn) 명시",
                "explanation": "의학적 진단명과 일시적 상승을 구분해야 합니다"
            },
            {
                "mistake": "수치 없이 '높다'로만 통역",
                "correction": "구체적 수치(140/90 mmHg) 제시",
                "explanation": "환자가 자신의 상태를 정확히 이해하려면 수치가 필수입니다"
            },
            {
                "mistake": "백의고혈압을 실제 고혈압으로 오인",
                "correction": "Huyết áp áo blouse trắng (병원에서만 높은 혈압) 설명",
                "explanation": "과잉 치료를 방지하기 위해 가정혈압 측정의 중요성을 강조해야 합니다"
            }
        ],
        "examples": [
            {
                "ko": "혈압이 160/100으로 측정되어 약 처방이 필요합니다.",
                "vi": "Huyết áp của anh/chị là 160/100, cần kê đơn thuốc hạ huyết áp.",
                "situation": "formal"
            },
            {
                "ko": "아침마다 혈압을 재서 기록해 오세요.",
                "vi": "Hãy đo huyết áp mỗi sáng và ghi lại kết quả.",
                "situation": "onsite"
            },
            {
                "ko": "짜게 드시면 혈압이 더 올라갑니다.",
                "vi": "Nếu ăn mặn, huyết áp sẽ tăng cao hơn.",
                "situation": "informal"
            }
        ],
        "relatedTerms": ["수축기혈압", "이완기혈압", "백의고혈압", "가면고혈압", "항고혈압제"]
    },
    {
        "slug": "xo-vua-dong-mach",
        "korean": "동맥경화",
        "vietnamese": "Xơ vữa động mạch",
        "hanja": "動脈硬化",
        "hanjaReading": "動(움직일 동) + 脈(맥 맥) + 硬(굳을 경) + 化(될 화)",
        "pronunciation": "서 브어 동 막",
        "meaningKo": "혈관 벽에 콜레스테롤과 지방이 쌓여 혈관이 좁아지고 딱딱해지는 질환입니다. 통역 시 '혈관이 막혔다'는 환자 표현을 의학적으로 정확히 전달해야 하며, 죽상경화증(xơ vữa)과 동맥경화(xơ cứng động mạch)를 구분해야 합니다. 한국에서는 건강검진 시 경동맥 초음파로 조기 발견이 흔하나 베트남은 증상 발생 후 진단되는 경우가 많습니다. 통역 시 LDL 콜레스테롤(cholesterol LDL) 수치와 치료 목표치를 명확히 전달하고, 베트남 환자에게는 스타틴 약물의 장기 복용 필요성을 설득력 있게 설명해야 합니다.",
        "meaningVi": "Tình trạng mảng xơ vữa tích tụ trong thành động mạch, làm hẹp lòng mạch và giảm lưu lượng máu. Đây là nguyên nhân chính gây nhồi máu cơ tim, đột quỵ, và bệnh động mạch ngoại biên. Yếu tố nguy cơ bao gồm cholesterol cao, hút thuốc, tiểu đường, và tăng huyết áp. Tại Hàn Quốc, việc sàng lọc sớm qua siêu âm động mạch cảnh rất phổ biến trong khám sức khỏe định kỳ.",
        "context": "순환기내과, 심장내과, 건강검진 상담에서 사용",
        "culturalNote": "한국은 40대부터 정기적으로 경동맥 초음파(siêu âm động mạch cảnh)를 권장하나 베트남은 이런 예방 검진 문화가 약합니다. 한국 환자는 스타틴(statin) 복용을 당연시하지만 베트남 환자는 부작용을 우려해 거부하는 경우가 많아 이익과 위험을 균형 있게 설명해야 합니다. 또한 한국은 저지방 식단을 강조하나 베트남 음식 문화에서는 돼지기름(mỡ lợn), 코코넛 밀크(nước cốt dừa) 사용이 흔해 식단 교육이 더 필요합니다.",
        "commonMistakes": [
            {
                "mistake": "Tắc mạch (혈전증)와 혼동",
                "correction": "Xơ vữa động mạch (만성 진행) vs Tắc mạch (급성 폐쇄)",
                "explanation": "동맥경화는 서서히 진행되는 과정이고 혈전증은 급성 사건입니다"
            },
            {
                "mistake": "Cholesterol cao로만 설명",
                "correction": "Xơ vữa động mạch (병리 과정) - 콜레스테롤은 원인 중 하나",
                "explanation": "고콜레스테롤은 위험인자일 뿐 동맥경화 자체는 복합적 병변입니다"
            },
            {
                "mistake": "경동맥과 관상동맥을 구분하지 않음",
                "correction": "Động mạch cảnh (뇌졸중) vs Động mạch vành (심근경색)",
                "explanation": "침범 부위에 따라 합병증이 달라 정확한 위치 전달이 중요합니다"
            }
        ],
        "examples": [
            {
                "ko": "경동맥 초음파에서 혈관 내벽이 두꺼워진 소견이 보입니다.",
                "vi": "Siêu âm động mạch cảnh cho thấy thành mạch dày lên.",
                "situation": "formal"
            },
            {
                "ko": "LDL 콜레스테롤을 100 이하로 낮춰야 합니다.",
                "vi": "Cần giảm cholesterol LDL xuống dưới 100.",
                "situation": "onsite"
            },
            {
                "ko": "스타틴 약은 평생 드셔야 합니다.",
                "vi": "Thuốc statin cần uống suốt đời.",
                "situation": "onsite"
            }
        ],
        "relatedTerms": ["죽상경화증", "콜레스테롤", "스타틴", "경동맥협착증", "관상동맥질환"]
    },
    {
        "slug": "benh-van-tim",
        "korean": "심장판막질환",
        "vietnamese": "Bệnh van tim",
        "hanja": "心臟瓣膜疾患",
        "hanjaReading": "心(마음 심) + 臟(장기 장) + 瓣(꽃잎 판) + 膜(막 막) + 疾(병 질) + 患(근심 환)",
        "pronunciation": "벵 반 띰",
        "meaningKo": "심장의 네 개 판막(승모판, 대동맥판, 삼첨판, 폐동맥판) 중 하나 이상에 협착이나 역류가 발생한 질환입니다. 통역 시 판막의 위치와 문제 유형(협착 hẹp vs 역류 hở)을 정확히 구분해야 하며, 베트남에서는 류마티스성 심장병(bệnh tim do thấp khớp) 유병률이 한국보다 높아 원인 감별이 중요합니다. 한국에서는 판막 수술(phẫu thuật van tim)과 인공판막 시술(thay van nhân tạo)이 보편화되었으나 베트남은 접근성이 제한적이어서 통역 시 치료 옵션의 현실적 가능성을 함께 고려해야 합니다. 심초음파 소견을 설명할 때는 역류 정도(nhẹ, vừa, nặng)와 압력 차이를 수치로 전달해야 합니다.",
        "meaningVi": "Bệnh lý liên quan đến các van tim (van hai lá, van động mạch chủ, van ba lá, van động mạch phổi) bị hẹp hoặc hở. Tại Việt Nam, bệnh tim do thấp khớp vẫn là nguyên nhân phổ biến, trong khi Hàn Quốc chủ yếu do thoái hóa van ở người cao tuổi. Triệu chứng bao gồm khó thở, mệt mỏi, đau ngực. Chẩn đoán qua siêu âm tim, điều trị có thể là thuốc hoặc phẫu thuật thay van.",
        "context": "심장내과, 심장외과, 류마티스내과 진료 시 사용",
        "culturalNote": "베트남은 류마티스열(sốt thấp khớp) 후유증으로 젊은 나이에 판막질환이 발생하는 반면, 한국은 주로 노화에 따른 퇴행성 변화입니다. 한국에서는 경피적 판막 시술(TAVI: thay van động mạch chủ qua da)이 보험 적용되나 베트남은 극소수 병원에서만 가능하고 비용이 매우 높습니다. 인공판막 선택 시 한국은 기계판막(van cơ học)과 조직판막(van sinh học)을 환자 연령과 선호도에 따라 선택하나 베트남은 비용 문제로 기계판막을 선호하는 경향이 있습니다.",
        "commonMistakes": [
            {
                "mistake": "Van tim hở로만 번역",
                "correction": "Hở van (역류) vs Hẹp van (협착) 구분",
                "explanation": "병리 기전과 치료가 완전히 다르므로 정확한 유형을 전달해야 합니다"
            },
            {
                "mistake": "판막 위치를 구분하지 않음",
                "correction": "Van hai lá (승모판), Van động mạch chủ (대동맥판) 등 명시",
                "explanation": "네 개 판막의 위치에 따라 증상과 치료가 다릅니다"
            },
            {
                "mistake": "역류 정도를 수치 없이 통역",
                "correction": "Hở van nhẹ/vừa/nặng + 압력차(mmHg) 제시",
                "explanation": "수술 시기 결정에 정량적 평가가 필수입니다"
            }
        ],
        "examples": [
            {
                "ko": "승모판 역류가 중등도로 관찰됩니다.",
                "vi": "Hở van hai lá ở mức độ vừa.",
                "situation": "formal"
            },
            {
                "ko": "대동맥판 협착으로 판막 치환술이 필요합니다.",
                "vi": "Do hẹp van động mạch chủ, cần phẫu thuật thay van.",
                "situation": "formal"
            },
            {
                "ko": "기계판막을 선택하면 평생 혈액희석제를 복용해야 합니다.",
                "vi": "Nếu chọn van cơ học, phải uống thuốc chống đông máu suốt đời.",
                "situation": "onsite"
            }
        ],
        "relatedTerms": ["승모판협착증", "대동맥판역류", "류마티스성심장병", "판막치환술", "심초음파"]
    },
    {
        "slug": "thieu-mau",
        "korean": "빈혈",
        "vietnamese": "Thiếu máu",
        "hanja": "貧血",
        "hanjaReading": "貧(가난할 빈) + 血(피 혈)",
        "pronunciation": "티에우 머우",
        "meaningKo": "혈액 내 적혈구 수나 헤모글로빈 농도가 정상보다 낮은 상태를 말합니다. 통역 시 철결핍성(thiếu sắt), 거대적아구성(hồng cầu to), 재생불량성(suy tủy) 등 원인별 분류를 명확히 해야 하며, 단순히 '피가 부족하다'는 구어적 표현을 의학 용어로 전환해야 합니다. 한국에서는 건강검진에서 빈혈을 조기 발견하나 베트남은 증상이 심해진 후 발견되는 경우가 많습니다. 베트남 여성은 월경과다(kinh nguyệt nhiều)로 인한 철결핍성 빈혈이 흔하므로 철분제 복용 지도 시 위장장애 대처법도 함께 통역해야 합니다. 헤모글로빈 수치를 전달할 때는 한국 기준(남 13g/dL, 여 12g/dL)을 명확히 안내해야 합니다.",
        "meaningVi": "Tình trạng lượng hồng cầu hoặc hemoglobin trong máu thấp hơn bình thường. Nguyên nhân phổ biến bao gồm thiếu sắt, thiếu vitamin B12, mất máu mạn tính. Triệu chứng gồm mệt mỏi, chóng mặt, da xanh xao, tim đập nhanh. Tại Việt Nam, thiếu máu do thiếu sắt rất phổ biến ở phụ nữ trong độ tuổi sinh đẻ, trong khi Hàn Quốc có tỷ lệ thấp hơn nhờ chế độ ăn giàu sắt và tầm soát sớm.",
        "context": "내과, 산부인과, 혈액내과, 건강검진 상담에서 사용",
        "culturalNote": "한국은 학교 및 직장 건강검진에서 빈혈을 조기 발견하나 베트남은 어지러움이 심해진 후에야 병원을 찾는 경우가 많습니다. 한국 여성은 철분제 복용에 익숙하나 베트남 여성은 속쓰림을 이유로 중단하는 경우가 많아 식후 복용법을 강조해야 합니다. 또한 한국은 비타민 B12 결핍 검사가 보편화되어 있으나 베트남은 철결핍성 빈혈로만 간주하고 다른 원인을 놓치는 경우가 있습니다. 베트남은 채식주의자(người ăn chay)가 많아 비타민 B12 결핍 위험을 설명해야 합니다.",
        "commonMistakes": [
            {
                "mistake": "Thiếu máu로만 번역하고 원인 구분 없음",
                "correction": "Thiếu máu thiếu sắt (철결핍성) 등 원인별 명시",
                "explanation": "치료법이 원인에 따라 완전히 다르므로 정확한 분류가 필수입니다"
            },
            {
                "mistake": "헤모글로빈 수치 없이 '빈혈'로만 통역",
                "correction": "Hemoglobin [수치] g/dL - mức bình thường [기준치]",
                "explanation": "환자가 심각도를 이해하려면 구체적 수치가 필요합니다"
            },
            {
                "mistake": "Huyết áp thấp (저혈압)와 혼동",
                "correction": "Thiếu máu (빈혈) vs Huyết áp thấp (저혈압)",
                "explanation": "완전히 다른 질환이지만 어지러움 증상이 유사해 환자가 혼동합니다"
            }
        ],
        "examples": [
            {
                "ko": "헤모글로빈이 9.5로 낮아 철분제 처방이 필요합니다.",
                "vi": "Hemoglobin là 9.5, thấp hơn bình thường, cần kê đơn thuốc bổ sung sắt.",
                "situation": "formal"
            },
            {
                "ko": "철분제는 식후에 드시고, 커피나 차는 피하세요.",
                "vi": "Uống thuốc sắt sau bữa ăn và tránh cà phê hoặc trà.",
                "situation": "onsite"
            },
            {
                "ko": "어지럽고 쉽게 피곤하시죠? 빈혈 때문입니다.",
                "vi": "Anh/chị hay chóng mặt và mệt mỏi phải không? Đó là do thiếu máu.",
                "situation": "informal"
            }
        ],
        "relatedTerms": ["철결핍성빈혈", "헤모글로빈", "적혈구", "철분제", "비타민B12"]
    },
    {
        "slug": "ung-thu-mau",
        "korean": "백혈병",
        "vietnamese": "Ung thư máu",
        "hanja": "白血病",
        "hanjaReading": "白(흰 백) + 血(피 혈) + 病(병 병)",
        "pronunciation": "웅 투 머우",
        "meaningKo": "골수에서 비정상적인 백혈구가 과다 생성되어 정상 혈액세포를 억제하는 혈액암입니다. 통역 시 급성과 만성, 골수성과 림프구성을 구분해야 하며(급성 골수성 백혈병 AML: Ung thư máu cấp dòng tủy), 베트남 환자와 보호자에게는 '혈액암'이라는 용어가 주는 충격을 고려해 단계적으로 설명해야 합니다. 한국은 조혈모세포 이식(ghép tế bào gốc tạo máu) 시스템이 발달했으나 베트남은 공여자 찾기가 어렵고 비용 부담이 매우 커서 현실적 치료 옵션을 신중히 통역해야 합니다. 항암치료 과정에서 감염 예방의 중요성을 강조하되, 베트남 가족들의 과도한 병문안 문화를 감안해 면회 제한 필요성을 설득력 있게 전달해야 합니다.",
        "meaningVi": "Ung thư máu phát sinh từ tủy xương, nơi sản xuất các tế bào máu. Bệnh có thể cấp tính hoặc mạn tính, dòng tủy hoặc dòng lympho. Triệu chứng bao gồm mệt mỏi, nhiễm trùng tái đi tái lại, chảy máu dễ dàng, sốt. Điều trị bao gồm hóa trị, xạ trị, và ghép tế bào gốc. Tại Hàn Quốc, tỷ lệ thành công ghép tủy cao nhờ ngân hàng tế bào gốc phát triển, nhưng tại Việt Nam việc tìm người hiến phù hợp còn rất khó khăn.",
        "context": "혈액종양내과, 소아청소년과(소아백혈병), 이식센터에서 사용",
        "culturalNote": "한국은 국가 골수은행(ngân hàng tủy xương quốc gia)이 체계적이어서 비혈연 이식도 활발하나 베트남은 가족 내 공여자에 의존하는 경우가 대부분입니다. 한국 환자는 무균실 격리(cách ly vô trùng)를 받아들이나 베트남 문화에서는 가족이 항상 곁에 있어야 한다는 인식이 강해 감염 위험 설명이 더욱 중요합니다. 한국은 백혈병 환아 지원 시스템이 발달했으나 베트남은 치료비 마련을 위한 모금이 흔하며 이로 인한 심리적 부담을 통역 시 고려해야 합니다. 한국은 표적치료제(thuốc điều trị đích)가 보험 적용되나 베트남은 거의 전액 본인 부담입니다.",
        "commonMistakes": [
            {
                "mistake": "Bệnh bạch cầu (백혈구 질환)로 번역",
                "correction": "Ung thư máu (혈액암) 또는 Bệnh bạch cầu ác tính",
                "explanation": "암의 심각성을 전달하려면 'ung thư'라는 용어를 사용해야 합니다"
            },
            {
                "mistake": "급성/만성 구분 없이 통역",
                "correction": "Cấp (급성 - 수주 내 치료) vs Mạn (만성 - 수년 관리)",
                "explanation": "예후와 치료 긴급성이 완전히 다르므로 반드시 구분해야 합니다"
            },
            {
                "mistake": "골수이식을 간단한 수술로 설명",
                "correction": "Ghép tế bào gốc - 위험성, 비용, 공여자 필요성 상세 설명",
                "explanation": "베트남 환자에게 현실적 어려움을 솔직히 전달해야 합니다"
            }
        ],
        "examples": [
            {
                "ko": "급성 골수성 백혈병 진단으로 즉시 항암치료를 시작해야 합니다.",
                "vi": "Chẩn đoán ung thư máu cấp dòng tủy, cần bắt đầu hóa trị ngay lập tức.",
                "situation": "formal"
            },
            {
                "ko": "조혈모세포 이식을 위해 형제자매 중 적합한 공여자를 찾아야 합니다.",
                "vi": "Cần tìm người hiến phù hợp trong anh chị em để ghép tế bào gốc tạo máu.",
                "situation": "formal"
            },
            {
                "ko": "면역력이 매우 낮아 감염 예방이 중요하므로 면회를 제한해야 합니다.",
                "vi": "Vì miễn dịch rất yếu và cần phòng ngừa nhiễm trùng, phải hạn chế thăm bệnh.",
                "situation": "onsite"
            }
        ],
        "relatedTerms": ["급성골수성백혈병", "만성림프구성백혈병", "조혈모세포이식", "골수검사", "항암화학요법"]
    },
    {
        "slug": "huyet-khoi",
        "korean": "혈전증",
        "vietnamese": "Huyết khối",
        "hanja": "血栓症",
        "hanjaReading": "血(피 혈) + 栓(마개 전) + 症(증세 증)",
        "pronunciation": "후옛 코이",
        "meaningKo": "혈관 내에 혈액이 응고되어 덩어리(혈전)를 형성하는 질환입니다. 통역 시 정맥혈전증(huyết khối tĩnh mạch)과 동맥혈전증을 구분하고, 심부정맥혈전증(DVT: huyết khối tĩnh mạch sâu)과 폐색전증(PE: thuyên tắc phổi)의 연관성을 설명해야 합니다. 한국에서는 장거리 비행 후 예방 교육이 보편화되어 있으나 베트남에서는 인식이 낮아 '다리 부종'을 단순 피로로 오해하는 경우가 많습니다. 항응고제(thuốc chống đông máu) 복용 시 출혈 위험과 음식 제한(특히 와파린 복용 시 비타민 K 함유 식품)을 상세히 통역해야 하며, 베트남 환자가 한약을 병행하려 할 때 상호작용 위험을 강조해야 합니다.",
        "meaningVi": "Tình trạng hình thành cục máu đông trong lòng mạch máu, có thể gây tắc nghẽn dòng chảy. Huyết khối tĩnh mạch sâu (DVT) ở chân có thể di chuyển đến phổi gây thuyên tắc phổi nguy hiểm. Yếu tố nguy cơ bao gồm ngồi lâu, phẫu thuật, ung thư, thuốc tránh thai. Điều trị bằng thuốc chống đông máu như warfarin hoặc thuốc thế hệ mới. Tại Hàn Quốc, người đi máy bay dài được khuyến cáo mang tất y khoa, nhưng tại Việt Nam nhận thức về phòng ngừa còn hạn chế.",
        "context": "순환기내과, 외과(수술 후), 응급실에서 사용",
        "culturalNote": "한국은 수술 후 조기 보행(đi lại sớm)과 압박스타킹(tất y khoa) 착용을 철저히 교육하나 베트남은 '많이 쉬어야 한다'는 인식이 강해 오히려 혈전 위험을 높입니다. 한국 환자는 항응고제 복용 중 정기적 혈액검사(xét nghiệm INR)를 잘 따르지만 베트남 환자는 비용 부담으로 검사를 미루는 경우가 많습니다. 와파린 복용 시 청경채(rau cải xanh), 낫토 등 비타민 K 함유 식품 제한이 필요한데 베트남 채소 요리 문화에서는 실천이 어려워 신세대 항응고제(NOAC) 사용을 고려해야 합니다.",
        "commonMistakes": [
            {
                "mistake": "Cục máu đông (혈전)와 Tắc mạch (색전증) 혼동",
                "correction": "Huyết khối (제자리 응고) vs Thuyên tắc (떠다니다 막음)",
                "explanation": "혈전이 떨어져 다른 곳을 막으면 색전증이 됩니다"
            },
            {
                "mistake": "다리 부종을 단순 피로로 통역",
                "correction": "Sưng chân - nguy cơ huyết khối tĩnh mạch sâu",
                "explanation": "DVT는 폐색전증으로 진행될 수 있어 즉시 검사가 필요합니다"
            },
            {
                "mistake": "항응고제와 항혈소판제 구분 없이 번역",
                "correction": "Thuốc chống đông (와파린) vs Thuốc chống kết tập tiểu cầu (아스피린)",
                "explanation": "작용 기전과 적응증이 다르므로 정확히 구분해야 합니다"
            }
        ],
        "examples": [
            {
                "ko": "왼쪽 다리 심부정맥혈전증으로 항응고제 치료를 시작합니다.",
                "vi": "Huyết khối tĩnh mạch sâu chân trái, bắt đầu điều trị bằng thuốc chống đông máu.",
                "situation": "formal"
            },
            {
                "ko": "장거리 비행 시 2시간마다 일어나서 걸으세요.",
                "vi": "Khi đi máy bay dài, hãy đứng dậy đi lại mỗi 2 giờ.",
                "situation": "onsite"
            },
            {
                "ko": "와파린 복용 중에는 청경채나 시금치를 많이 먹지 마세요.",
                "vi": "Khi uống warfarin, không nên ăn nhiều rau cải xanh hoặc rau chân vịt.",
                "situation": "onsite"
            }
        ],
        "relatedTerms": ["심부정맥혈전증", "폐색전증", "항응고제", "와파린", "디다이머검사"]
    },
    {
        "slug": "benh-mau-kho-dong",
        "korean": "혈우병",
        "vietnamese": "Bệnh máu khó đông",
        "hanja": "血友病",
        "hanjaReading": "血(피 혈) + 友(벗 우) + 病(병 병)",
        "pronunciation": "벵 머우 커 동",
        "meaningKo": "혈액응고인자 부족으로 출혈이 멈추지 않는 유전질환입니다. 통역 시 A형(제8인자 결핍)과 B형(제9인자 결핍)을 구분하고, 경증·중등증·중증 분류를 명확히 해야 합니다. 한국에서는 국가 희귀질환 등록으로 응고인자 제제(chế phẩm yếu tố đông máu) 지원이 체계적이나 베트남은 약품 수급이 불안정하고 비용 부담이 매우 커서 현실적 치료 계획을 통역해야 합니다. 관절 출혈(chảy máu khớp)로 인한 장애 예방이 중요하므로 조기 치료의 필요성을 강조하되, 베트남 가족들이 '상처 나지 않게 보호'에만 집중해 정상적 활동을 과도하게 제한하지 않도록 균형 잡힌 설명이 필요합니다. 유전 상담 시 보인자(người mang gen) 검사와 산전 진단의 가능성을 민감하게 통역해야 합니다.",
        "meaningVi": "Bệnh di truyền làm máu khó đông do thiếu các yếu tố đông máu, chủ yếu yếu tố VIII (Hemophilia A) hoặc yếu tố IX (Hemophilia B). Triệu chứng bao gồm chảy máu kéo dài sau chấn thương, chảy máu khớp, chảy máu não nguy hiểm. Điều trị bằng truyền chế phẩm yếu tố đông máu thiếu hụt. Tại Hàn Quốc, bệnh nhân được hỗ trợ thuốc qua chương trình bệnh hiếm, nhưng tại Việt Nam chi phí điều trị rất cao và thuốc không luôn sẵn có.",
        "context": "혈액내과, 소아청소년과, 유전상담실에서 사용",
        "culturalNote": "한국은 혈우병 환자 등록 시스템과 응급카드 발급이 체계적이나 베트남은 인프라가 부족해 응급 상황 대처가 어렵습니다. 한국 환자는 예방적 치료(điều trị dự phòng)로 정기적 응고인자 투여를 받지만 베트남은 출혈 발생 시에만 치료하는 경우가 많아 관절 손상이 누적됩니다. 한국 사회는 혈우병 환자의 사회 통합을 지향하나 베트남은 과잉 보호로 인한 사회적 고립이 문제가 됩니다. 유전 상담 시 한국은 개방적이나 베트남은 가족 내 '결함' 노출을 꺼리는 문화가 있어 신중한 접근이 필요합니다.",
        "commonMistakes": [
            {
                "mistake": "Máu loãng (혈액 묽음)으로 오역",
                "correction": "Bệnh máu khó đông (응고장애)",
                "explanation": "혈액이 묽은 것이 아니라 응고인자가 부족한 것입니다"
            },
            {
                "mistake": "A형과 B형 구분 없이 통역",
                "correction": "Hemophilia A (yếu tố VIII) vs B (yếu tố IX)",
                "explanation": "치료에 필요한 응고인자가 다르므로 정확한 분류가 필수입니다"
            },
            {
                "mistake": "경증 환자를 중증으로 과장",
                "correction": "경증(nhẹ: >5%), 중등증(vừa: 1-5%), 중증(nặng: <1%)",
                "explanation": "중증도에 따라 일상생활 제약과 치료 강도가 달라집니다"
            }
        ],
        "examples": [
            {
                "ko": "A형 혈우병으로 제8응고인자 투여가 필요합니다.",
                "vi": "Bệnh máu khó đông type A, cần truyền yếu tố đông máu VIII.",
                "situation": "formal"
            },
            {
                "ko": "관절이 붓거나 아프면 즉시 병원에 오셔야 합니다.",
                "vi": "Nếu khớp sưng hoặc đau, phải đến bệnh viện ngay lập tức.",
                "situation": "onsite"
            },
            {
                "ko": "아이가 혈우병이 있지만 적절한 치료를 받으면 정상적인 생활이 가능합니다.",
                "vi": "Con có bệnh máu khó đông nhưng với điều trị phù hợp có thể sống bình thường.",
                "situation": "informal"
            }
        ],
        "relatedTerms": ["응고인자", "관절출혈", "유전상담", "보인자", "예방적치료"]
    }
]

def main():
    """메인 실행 함수"""
    print("=" * 60)
    print("의료 도메인 용어 추가 스크립트 v5-u")
    print("Theme: 심장/순환기/혈액 (Cardiology/Hematology)")
    print("=" * 60)

    # 파일 존재 확인
    if not os.path.exists(file_path):
        print(f"❌ 오류: {file_path} 파일을 찾을 수 없습니다.")
        return

    # 기존 데이터 로드
    print(f"\n📂 파일 로드 중: {file_path}")
    with open(file_path, 'r', encoding='utf-8') as f:
        data = json.load(f)

    print(f"✅ 기존 용어 수: {len(data)}개")

    # 중복 체크
    existing_slugs = {term['slug'] for term in data}
    new_unique_terms = [term for term in new_terms if term['slug'] not in existing_slugs]
    duplicates = [term['slug'] for term in new_terms if term['slug'] in existing_slugs]

    if duplicates:
        print(f"\n⚠️  중복 감지 ({len(duplicates)}개): {', '.join(duplicates)}")
        print("   → 중복 용어는 제외하고 진행합니다.")

    if not new_unique_terms:
        print("\n❌ 추가할 새 용어가 없습니다 (모두 중복).")
        return

    # 용어 추가
    print(f"\n➕ 새 용어 {len(new_unique_terms)}개 추가 중...")
    data.extend(new_unique_terms)

    # 파일 저장 (UTF-8, 들여쓰기 2칸, 한글 보존)
    with open(file_path, 'w', encoding='utf-8') as f:
        json.dump(data, f, ensure_ascii=False, indent=2)

    print(f"✅ 완료! 총 {len(data)}개 용어 (기존 {len(data) - len(new_unique_terms)} + 신규 {len(new_unique_terms)})")
    print("\n📋 추가된 용어:")
    for i, term in enumerate(new_unique_terms, 1):
        print(f"   {i}. {term['korean']} ({term['vietnamese']}) - slug: {term['slug']}")

    print("\n" + "=" * 60)
    print("✨ 다음 단계: npm run validate:terms 실행하여 Tier S 품질 확인")
    print("=" * 60)

if __name__ == "__main__":
    main()
