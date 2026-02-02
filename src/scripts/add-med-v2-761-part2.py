#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Medical Terms Addition Script - v2-761 Part 2
Terms 11-50: Cardiology and Pulmonology focus
"""

import json
import os

file_path = os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', 'data', 'terms', 'medical.json')

# Terms 11-50
additional_terms = [
    {
        "slug": "khi-hung",
        "korean": "기흉",
        "vietnamese": "Tràn khí màng phổi",
        "hanja": "氣胸",
        "hanjaReading": "氣(기운 기) + 胸(가슴 흉)",
        "pronunciation": "기흉",
        "meaningKo": "폐와 흉벽 사이의 공간(흉막강)에 공기가 차서 폐가 압박받는 상태. 통역 시 주의할 점은 한국에서는 '기흉'이라는 짧은 용어를 사용하지만 베트남에서는 'tràn khí màng phổi'(흉막에 공기가 찬다)로 길게 설명해야 이해가 쉽습니다. 특히 긴장성 기흉(khí màng phổi áp lực)은 즉시 응급 감압이 필요한 치명적 상태임을 강조해야 합니다.",
        "meaningVi": "Tình trạng có không khí trong khoảng màng phổi (giữa phổi và thành ngực), làm phổi bị xẹp. Có thể do chấn thương, bệnh phổi, hoặc tự nhiên xảy ra ở người gầy cao. Triệu chứng gồm đau ngực đột ngột, khó thở, cần dẫn lưu màng phổi để điều trị.",
        "context": "응급의학, 흉부외과, 호흡기내과",
        "culturalNote": "한국에서는 키가 크고 마른 청소년의 자연기흉이 흔하며, 흉관 삽입술이 응급실에서 즉시 시행됩니다. 베트남에서도 비슷한 패턴이지만, 결핵 후유증으로 인한 이차성 기흉이 상대적으로 많습니다. 또한 한국에서는 재발성 기흉에 대해 흉강경 수술이 보편화되어 있으나 베트남에서는 개흉술을 하는 경우가 많습니다.",
        "commonMistakes": [
            {
                "mistake": "기흉을 '폐에 구멍'으로 설명",
                "correction": "폐 바깥 공간에 공기가 찬 것 (không khí trong khoảng màng phổi)",
                "explanation": "폐 자체의 손상이 아닌 흉막강 내 공기 축적이 핵심"
            },
            {
                "mistake": "긴장성 기흉과 일반 기흉을 구분하지 않음",
                "correction": "일반 기흉은 tràn khí màng phổi, 긴장성은 khí màng phổi áp lực",
                "explanation": "긴장성은 생명을 위협하는 응급상황이므로 반드시 구분"
            },
            {
                "mistake": "'흉관 삽입'을 '튜브 넣기'로 단순화",
                "correction": "đặt dẫn lưu màng phổi (흉관 삽입)",
                "explanation": "정확한 의학 용어 사용 필요"
            }
        ],
        "examples": [
            {
                "ko": "갑자기 숨이 차고 가슴이 아프다면 기흉을 의심해야 합니다.",
                "vi": "Nếu đột ngột khó thở và đau ngực, cần nghi ngờ tràn khí màng phổi.",
                "situation": "formal"
            },
            {
                "ko": "X-ray에서 왼쪽 기흉이 보입니다. 흉관을 삽입하겠습니다.",
                "vi": "X-quang thấy tràn khí màng phổi bên trái. Chúng tôi sẽ đặt dẫn lưu.",
                "situation": "onsite"
            },
            {
                "ko": "기흉은 키 크고 마른 젊은 남성에게 흔합니다.",
                "vi": "Tràn khí màng phổi thường gặp ở nam giới trẻ cao gầy.",
                "situation": "informal"
            }
        ],
        "relatedTerms": ["흉관삽입", "흉부외상", "호흡곤란", "긴장성기흉"]
    },
    {
        "slug": "tran-mau-khung-hung",
        "korean": "혈흉",
        "vietnamese": "Tràn máu khoang hung",
        "hanja": "血胸",
        "hanjaReading": "血(피 혈) + 胸(가슴 흉)",
        "pronunciation": "혈흉",
        "meaningKo": "흉막강에 피가 고이는 상태로 주로 흉부 외상이나 수술 후 발생. 통역 시 주의할 점은 대량 혈흉은 쇼크와 호흡곤란을 유발하여 응급 흉관 삽입이나 개흉술이 필요한 응급상황이라는 점을 명확히 전달해야 합니다. 한국에서는 외상센터에서 즉시 처치가 가능하나, 베트남에서는 대형 병원으로의 신속한 이송이 생명을 좌우할 수 있습니다.",
        "meaningVi": "Tình trạng máu tích tụ trong khoang màng phổi, thường do chấn thương ngực hoặc sau phẫu thuật. Nếu lượng máu nhiều, có thể gây sốc mất máu và khó thở nghiêm trọng, cần dẫn lưu màng phổi hoặc phẫu thuật cấp cứu để lấy máu ra và cầm máu.",
        "context": "응급의학, 흉부외과, 외상외과",
        "culturalNote": "한국의 외상센터는 초음파를 이용한 신속한 혈흉 진단(FAST)과 즉각적인 흉관 삽입 체계가 갖춰져 있습니다. 베트남에서는 X-ray 촬영 후 진단하는 경우가 많아 시간이 더 걸릴 수 있으며, 흉관 삽입 후 지속적인 출혈 시 수술 결정이 늦어질 수 있어 예후에 영향을 줄 수 있습니다.",
        "commonMistakes": [
            {
                "mistake": "혈흉을 '폐출혈'로 오역",
                "correction": "tràn máu khoang hung (흉막강 내 혈액)",
                "explanation": "폐출혈(xuất huyết phổi)은 기도로 피가 나오는 것이고, 혈흉은 흉막강에 피가 고이는 것"
            },
            {
                "mistake": "소량 혈흉과 대량 혈흉을 구분하지 않음",
                "correction": "소량은 tràn máu ít, 대량은 tràn máu nhiều hoặc tràn máu lớn",
                "explanation": "치료 방침이 완전히 다르므로 구분 필요"
            },
            {
                "mistake": "'배액'을 '피 빼기'로 구어체로만 표현",
                "correction": "dẫn lưu (배액) 또는 hút dịch (흡인)",
                "explanation": "의학 용어의 정확성 유지"
            }
        ],
        "examples": [
            {
                "ko": "교통사고 후 대량 혈흉이 발생하여 즉시 흉관을 삽입했습니다.",
                "vi": "Sau tai nạn giao thông, có tràn máu khoang hung nhiều, đã đặt dẫn lưu ngay lập tức.",
                "situation": "formal"
            },
            {
                "ko": "흉관으로 1시간에 200mL 이상 출혈이 계속되면 수술이 필요합니다.",
                "vi": "Nếu chảy máu qua dẫn lưu trên 200mL mỗi giờ, cần phẫu thuật.",
                "situation": "onsite"
            },
            {
                "ko": "혈흉은 방치하면 감염이나 섬유화가 생길 수 있습니다.",
                "vi": "Tràn máu khoang hung nếu không điều trị có thể gây nhiễm trùng hoặc xơ hóa.",
                "situation": "informal"
            }
        ],
        "relatedTerms": ["기흉", "흉부외상", "흉관삽입", "외상센터"]
    },
    {
        "slug": "chat-ep-tui-tim",
        "korean": "심낭압전",
        "vietnamese": "Chèn ép túi tim",
        "hanja": "心囊壓塡",
        "hanjaReading": "心(마음 심) + 囊(주머니 낭) + 壓(누를 압) + 塡(메울 전)",
        "pronunciation": "심낭압전",
        "meaningKo": "심장을 둘러싼 심낭에 액체(혈액, 삼출액)가 급격히 차서 심장이 압박받아 펌프 기능을 하지 못하는 응급상황. 통역 시 매우 주의할 점은 이것이 '심장압전증'이라고도 불리며, Beck's triad(낮은 혈압, 높은 정맥압, 작은 심음)가 특징적이지만 즉시 심낭천자를 하지 않으면 사망에 이를 수 있는 치명적 상태라는 것입니다.",
        "meaningVi": "Tình trạng dịch tích tụ trong túi màng ngoài tim (màng tim) làm chèn ép tim, cản trở tim bơm máu. Đây là cấp cứu nguy kịch, triệu chứng gồm huyết áp thấp, tĩnh mạch cổ nổi, tim đập yếu. Cần chọc hút dịch màng tim (chọc dò màng tim) ngay lập tức để cứu sống bệnh nhân.",
        "context": "응급의학, 심장내과, 흉부외과",
        "culturalNote": "한국에서는 응급실에서 초음파 유도하 심낭천자를 즉시 시행할 수 있으나, 베트남에서는 초음파 장비나 숙련된 의사 부족으로 시술이 지연될 수 있습니다. 또한 한국에서는 외상성 심낭압전 시 응급개흉술도 고려되지만, 베트남에서는 시설 제약으로 심낭천자에 의존하는 경우가 많습니다.",
        "commonMistakes": [
            {
                "mistake": "심낭압전을 '심장에 물 찬 것'으로 단순화",
                "correction": "chèn ép túi tim (심낭압전) - 생명을 위협하는 압박 상태 강조",
                "explanation": "단순 삼출과 압전은 응급성이 다르므로 구분 필요"
            },
            {
                "mistake": "'심낭천자'를 '심장 찌르기'로 직역",
                "correction": "chọc dò màng tim (심낭천자)",
                "explanation": "정확한 의학 용어 사용"
            },
            {
                "mistake": "심낭삼출(pericardial effusion)과 혼동",
                "correction": "삼출은 tràn dịch màng tim, 압전은 chèn ép túi tim",
                "explanation": "삼출은 서서히 차는 것, 압전은 급성 압박 상태"
            }
        ],
        "examples": [
            {
                "ko": "흉부 자상 후 심낭압전이 발생하여 즉시 심낭천자를 시행했습니다.",
                "vi": "Sau vết thương ngực, có chèn ép túi tim, đã thực hiện chọc dò màng tim ngay.",
                "situation": "formal"
            },
            {
                "ko": "혈압이 70/40이고 경정맥이 팽창되어 있어 심낭압전을 의심합니다.",
                "vi": "Huyết áp 70/40 và tĩnh mạch cổ nổi, nghi ngờ chèn ép túi tim.",
                "situation": "onsite"
            },
            {
                "ko": "심낭압전은 몇 분 안에 심정지로 진행할 수 있습니다.",
                "vi": "Chèn ép túi tim có thể dẫn đến ngừng tim trong vài phút.",
                "situation": "informal"
            }
        ],
        "relatedTerms": ["심낭천자", "외상", "Beck's triad", "초음파"]
    },
    {
        "slug": "thuan-tac-phoi",
        "korean": "폐색전증",
        "vietnamese": "Thuyên tắc phổi",
        "hanja": "肺塞栓症",
        "hanjaReading": "肺(허파 폐) + 塞(막을 색) + 栓(마개 전) + 症(병 증)",
        "pronunciation": "폐색전증",
        "meaningKo": "다리나 골반의 정맥에서 생긴 혈전이 떨어져 나와 폐동맥을 막아 호흡곤란과 흉통을 일으키는 질환. 통역 시 주의할 점은 한국에서는 장거리 비행 후 '이코노미 증후군'으로 알려져 있으나 베트남에서는 이 개념이 덜 알려져 있다는 것입니다. 또한 대량 폐색전증은 심정지를 일으킬 수 있어 즉각적인 혈전용해제 투여나 색전제거술이 필요함을 강조해야 합니다.",
        "meaningVi": "Cục máu đông từ tĩnh mạch chân hoặc khung chậu di chuyển lên tắc động mạch phổi, gây khó thở và đau ngực. Nguy cơ cao ở người nằm lâu, sau phẫu thuật, hoặc sau chuyến bay dài. Nếu tắc lớn có thể gây ngừng tim, cần thuốc tiêu sợi huyết hoặc lấy cục tắc khẩn cấp.",
        "context": "응급의학, 호흡기내과, 심장내과",
        "culturalNote": "한국에서는 수술 후 모든 환자에게 폐색전증 예방(압박스타킹, 항응고제)을 시행하며, CT pulmonary angiography가 응급실에서 즉시 가능합니다. 베트남에서는 CT 검사 대기 시간이 길고, D-dimer 검사가 모든 병원에서 가능하지 않아 진단이 지연될 수 있습니다. 또한 혈전용해제(tPA) 사용 경험이 한국보다 적습니다.",
        "commonMistakes": [
            {
                "mistake": "'색전'을 '혈전'으로 혼용",
                "correction": "혈전은 huyết khối (피떡), 색전은 thuyên tắc (막힌 것)",
                "explanation": "혈전은 생성물, 색전은 막힌 상태를 의미"
            },
            {
                "mistake": "폐색전증을 '폐에 피떡'으로 단순화",
                "correction": "thuyên tắc phổi (폐동맥이 막힌 질환)",
                "explanation": "정확한 병명 사용 필요"
            },
            {
                "mistake": "DVT(심부정맥혈전증)와 폐색전증을 구분하지 않음",
                "correction": "DVT는 huyết khối tĩnh mạch sâu, 폐색전증은 thuyên tắc phổi",
                "explanation": "DVT가 원인, 폐색전증이 결과이므로 구분 필요"
            }
        ],
        "examples": [
            {
                "ko": "장거리 비행 후 갑자기 숨이 차고 가슴이 아프면 폐색전증을 의심하세요.",
                "vi": "Sau chuyến bay dài, nếu đột ngột khó thở và đau ngực, nghi ngờ thuyên tắc phổi.",
                "situation": "formal"
            },
            {
                "ko": "CT에서 우측 폐동맥에 큰 색전이 보입니다. 혈전용해제를 투여하겠습니다.",
                "vi": "CT thấy cục tắc lớn ở động mạch phổi phải. Sẽ truyền thuốc tiêu sợi huyết.",
                "situation": "onsite"
            },
            {
                "ko": "수술 후 압박스타킹을 착용하면 폐색전증을 예방할 수 있습니다.",
                "vi": "Đi tất y tế sau phẫu thuật có thể phòng ngừa thuyên tắc phổi.",
                "situation": "informal"
            }
        ],
        "relatedTerms": ["심부정맥혈전증", "항응고제", "혈전용해제", "이코노미증후군"]
    },
    {
        "slug": "hoi-chung-dong-mach-vanh-cap",
        "korean": "급성관상동맥증후군",
        "vietnamese": "Hội chứng động mạch vành cấp",
        "hanja": "急性冠狀動脈症候群",
        "hanjaReading": "急(급할 급) + 性(성품 성) + 冠(갓 관) + 狀(모양 상) + 動(움직일 동) + 脈(맥 맥) + 症(병 증) + 候(기후 후) + 群(무리 군)",
        "pronunciation": "급성관상동맥증후군",
        "meaningKo": "심장에 혈액을 공급하는 관상동맥이 급격히 막히거나 좁아져 발생하는 응급 심장 질환의 총칭으로, 불안정형 협심증과 급성 심근경색을 포함. 통역 시 주의할 점은 한국에서는 ACS라는 약어를 의료진이 자주 사용하지만, 환자 가족에게는 '심장마비' 또는 '심근경색'으로 쉽게 설명하는 것이 좋습니다. 골든타임(90분 이내 관상동맥 재개통)을 강조해야 합니다.",
        "meaningVi": "Nhóm bệnh lý tim cấp tính do động mạch vành bị tắc hoặc hẹp đột ngột, bao gồm đau thắt ngực không ổn định và nhồi máu cơ tim cấp. Đây là cấp cứu tim mạch, triệu chứng gồm đau ngực dữ dội, khó thở, vã mồ hôi. Cần can thiệp mạch vành hoặc tiêu huyết khối trong 90 phút để cứu cơ tim.",
        "context": "심장내과, 응급의학",
        "culturalNote": "한국은 24시간 심혈관중재시술 가능한 병원이 전국적으로 분포되어 있어 'door-to-balloon time' 90분 이내를 목표로 합니다. 베트남은 대도시의 대형 병원에만 중재시술 시설이 있어 지방에서는 혈전용해제에 의존하거나 이송 시간이 길어져 예후가 나쁠 수 있습니다. 또한 한국의 구급차에는 12유도 심전도 장비가 있어 이송 중 진단이 가능하나 베트남은 제한적입니다.",
        "commonMistakes": [
            {
                "mistake": "ACS를 '심장마비'로만 번역",
                "correction": "hội chứng động mạch vành cấp (ACS) - 심장마비보다 넓은 개념",
                "explanation": "심정지(cardiac arrest)와 ACS는 다르므로 정확한 용어 사용"
            },
            {
                "mistake": "협심증과 심근경색을 구분하지 않음",
                "correction": "협심증은 đau thắt ngực, 심근경색은 nhồi máu cơ tim",
                "explanation": "치료 강도와 예후가 다르므로 명확히 구분 필요"
            },
            {
                "mistake": "'관상동맥'을 '심장 혈관'으로만 표현",
                "correction": "động mạch vành (관상동맥)",
                "explanation": "정확한 해부학적 용어 사용"
            }
        ],
        "examples": [
            {
                "ko": "급성관상동맥증후군으로 즉시 심혈관조영술을 시행하겠습니다.",
                "vi": "Do hội chứng động mạch vành cấp, sẽ thực hiện chụp mạch vành ngay.",
                "situation": "formal"
            },
            {
                "ko": "증상 발생 후 90분 이내에 막힌 혈관을 뚫어야 심장 손상을 최소화할 수 있습니다.",
                "vi": "Phải thông mạch trong vòng 90 phút kể từ khi có triệu chứng để giảm tổn thương tim.",
                "situation": "onsite"
            },
            {
                "ko": "가슴을 쥐어짜는 듯한 통증이 20분 이상 지속되면 급성관상동맥증후군을 의심하세요.",
                "vi": "Nếu đau ngực như bị siết chặt kéo dài trên 20 phút, nghi ngờ hội chứng động mạch vành cấp.",
                "situation": "informal"
            }
        ],
        "relatedTerms": ["심근경색", "협심증", "관상동맥중재술", "스텐트"]
    },
    {
        "slug": "nhoi-mau-co-tim",
        "korean": "심근경색",
        "vietnamese": "Nhồi máu cơ tim",
        "hanja": "心筋梗塞",
        "hanjaReading": "心(마음 심) + 筋(힘줄 근) + 梗(막힐 경) + 塞(막을 색)",
        "pronunciation": "심근경색",
        "meaningKo": "관상동맥이 완전히 막혀 심장 근육에 혈액 공급이 중단되어 심근 세포가 죽는 응급 상황. 통역 시 주의할 점은 일반인들이 '심장마비'라고 부르지만 의학적으로는 심근경색(MI)이 정확한 용어이며, STEMI(ST분절상승 심근경색)와 NSTEMI(비ST분절상승 심근경색)로 구분되어 치료법이 다르다는 것입니다. 골든타임 내 재관류가 생존과 직결됨을 강조해야 합니다.",
        "meaningVi": "Tình trạng động mạch vành bị tắc hoàn toàn khiến máu không đến nuôi cơ tim, gây tế bào cơ tim chết. Triệu chứng gồm đau ngực dữ dội lan ra vai trái, hàm, khó thở, vã mồ hôi lạnh. Cần can thiệp mạch vành (đặt stent) hoặc thuốc tiêu huyết khối khẩn cấp trong 90 phút để cứu tim.",
        "context": "심장내과, 응급의학, 중환자의학",
        "culturalNote": "한국은 심근경색 환자 이송 시 119 구급대에서 12유도 심전도를 찍어 병원에 미리 전송하여 중재시술실을 준비하는 'pre-hospital STEMI protocol'이 있습니다. 베트남은 이런 시스템이 없어 병원 도착 후 진단하므로 시간이 더 걸립니다. 또한 한국은 심근경색 등록체계가 있어 의료 질 관리가 철저하나 베트남은 통계조차 정확하지 않습니다.",
        "commonMistakes": [
            {
                "mistake": "'심근경색'을 '심장발작'으로 번역",
                "correction": "nhồi máu cơ tim (심근경색) - heart attack보다 정확한 의학 용어",
                "explanation": "정확한 진단명 사용이 중요"
            },
            {
                "mistake": "심정지(cardiac arrest)와 혼동",
                "correction": "심근경색은 nhồi máu cơ tim, 심정지는 ngừng tim",
                "explanation": "심근경색은 혈관 문제, 심정지는 심장 멈춤"
            },
            {
                "mistake": "STEMI와 NSTEMI를 구분하지 않음",
                "correction": "STEMI는 nhồi máu cơ tim có ST chênh lên, NSTEMI는 không có ST chênh",
                "explanation": "치료 긴급도가 다르므로 구분 필요"
            }
        ],
        "examples": [
            {
                "ko": "심전도에서 ST분절 상승이 보여 급성 심근경색으로 진단했습니다.",
                "vi": "Điện tâm đồ có ST chênh lên, chẩn đoán nhồi máu cơ tim cấp.",
                "situation": "formal"
            },
            {
                "ko": "지금 즉시 심장혈관조영실로 가서 막힌 혈관을 뚫겠습니다.",
                "vi": "Bây giờ sẽ vào phòng can thiệp mạch để thông mạch bị tắc ngay.",
                "situation": "onsite"
            },
            {
                "ko": "아버지께서 심근경색으로 스텐트 시술을 받으셨어요.",
                "vi": "Bố tôi bị nhồi máu cơ tim và đã được đặt stent.",
                "situation": "informal"
            }
        ],
        "relatedTerms": ["급성관상동맥증후군", "관상동맥중재술", "혈전용해제", "스텐트"]
    },
    {
        "slug": "dau-that-nguc",
        "korean": "협심증",
        "vietnamese": "Đau thắt ngực",
        "hanja": "狹心症",
        "hanjaReading": "狹(좁을 협) + 心(마음 심) + 症(병 증)",
        "pronunciation": "협심증",
        "meaningKo": "관상동맥이 좁아져 심장 근육에 충분한 혈액이 공급되지 않아 가슴 통증이 발생하는 질환. 통역 시 주의할 점은 안정형 협심증(운동 시만 증상)과 불안정형 협심증(휴식 시에도 증상)을 구분해야 하며, 후자는 심근경색으로 진행할 위험이 높아 입원 치료가 필요하다는 것입니다. 한국에서는 니트로글리세린 설하정을 처방하지만 베트남에서는 구하기 어려울 수 있습니다.",
        "meaningVi": "Bệnh lý do động mạch vành bị hẹp, cơ tim không nhận đủ máu nuôi dưỡng, gây đau ngực. Có thể là đau thắt ngực ổn định (chỉ đau khi gắng sức) hoặc không ổn định (đau cả khi nghỉ ngơi). Loại không ổn định nguy hiểm, có thể tiến triển thành nhồi máu cơ tim, cần nhập viện điều trị.",
        "context": "심장내과, 가정의학과",
        "culturalNote": "한국에서는 협심증 환자에게 운동부하검사, 심장초음파, 관상동맥CT 등으로 정밀 평가를 하고, 필요 시 스텐트 삽입을 적극적으로 권합니다. 베트남에서는 이런 검사가 비싸고 접근성이 낮아 약물 치료에 의존하는 경우가 많으며, 스텐트 시술도 제한적입니다. 니트로글리세린 설하정이 한국에서는 흔하지만 베트남에서는 구하기 어려워 대안 약물을 안내해야 할 수 있습니다.",
        "commonMistakes": [
            {
                "mistake": "'협심증'을 '가슴 통증'으로만 번역",
                "correction": "đau thắt ngực (협심증) - 특정 심장 질환명",
                "explanation": "일반적인 흉통과 협심증은 원인이 다름"
            },
            {
                "mistake": "안정형과 불안정형을 구분하지 않음",
                "correction": "안정형은 ổn định, 불안정형은 không ổn định",
                "explanation": "불안정형은 응급 입원이 필요하므로 반드시 구분"
            },
            {
                "mistake": "'니트로글리세린'을 음차만 사용",
                "correction": "nitroglycerin 또는 thuốc giãn mạch vành",
                "explanation": "베트남에서 통용되는 약물명 확인 필요"
            }
        ],
        "examples": [
            {
                "ko": "계단을 오를 때마다 가슴이 조이는 듯한 통증이 있으시면 협심증을 의심해야 합니다.",
                "vi": "Nếu mỗi lần lên cầu thang có cảm giác thắt ngực, cần nghi ngờ đau thắt ngực.",
                "situation": "formal"
            },
            {
                "ko": "협심증 증상이 나타나면 즉시 활동을 멈추고 니트로글리세린을 혀 밑에 넣으세요.",
                "vi": "Khi có triệu chứng đau thắt ngực, hãy dừng hoạt động và đặt nitroglycerin dưới lưỡi ngay.",
                "situation": "onsite"
            },
            {
                "ko": "불안정형 협심증은 심근경색의 전조 증상일 수 있어 위험합니다.",
                "vi": "Đau thắt ngực không ổn định nguy hiểm vì có thể là dấu hiệu sắp nhồi máu cơ tim.",
                "situation": "informal"
            }
        ],
        "relatedTerms": ["관상동맥질환", "심근경색", "니트로글리세린", "운동부하검사"]
    },
    {
        "slug": "roi-loan-nhip-tim",
        "korean": "부정맥",
        "vietnamese": "Rối loạn nhịp tim",
        "hanja": "不整脈",
        "hanjaReading": "不(아니 불) + 整(가지런할 정) + 脈(맥 맥)",
        "pronunciation": "부정맥",
        "meaningKo": "심장 박동이 정상적인 리듬을 벗어나 너무 빠르거나 느리거나 불규칙하게 뛰는 상태의 총칭. 통역 시 주의할 점은 부정맥의 종류가 매우 다양하여(심방세동, 심실빈맥 등) 각각 위험도와 치료법이 다르다는 것입니다. 한국에서는 24시간 홀터 모니터링과 전기생리학 검사가 보편화되어 있으나, 베트남에서는 접근성이 낮아 진단이 늦어질 수 있습니다.",
        "meaningVi": "Tình trạng tim đập không đều, có thể quá nhanh (nhịp nhanh), quá chậm (nhịp chậm), hoặc không đều (loạn nhịp). Nguyên nhân đa dạng từ bệnh tim, rối loạn điện giải, thuốc, đến stress. Một số loại vô hại, nhưng một số có thể gây đột quỵ hoặc tử vong đột ngột, cần điều trị tích cực.",
        "context": "심장내과, 응급의학",
        "culturalNote": "한국에서는 심방세동 환자에게 적극적으로 항응고제를 처방하여 뇌졸중을 예방하며, 전극도자절제술(catheter ablation)도 활발히 시행됩니다. 베트남에서는 항응고제 모니터링(INR 검사)이 어려워 와파린 사용을 꺼리고, 절제술도 대형 병원에서만 가능합니다. 또한 한국에서는 삽입형 제세동기(ICD)가 보험 적용되나 베트남에서는 매우 비싸 접근성이 낮습니다.",
        "commonMistakes": [
            {
                "mistake": "'부정맥'을 '심장 빨리 뜀'으로만 설명",
                "correction": "rối loạn nhịp tim (부정맥) - 빠름/느림/불규칙 모두 포함",
                "explanation": "부정맥은 빠른 것만이 아님"
            },
            {
                "mistake": "모든 부정맥을 위험한 것으로 설명",
                "correction": "양성 부정맥(lành tính)과 악성 부정맥(ác tính) 구분",
                "explanation": "과도한 불안을 주지 않도록 위험도 구분 필요"
            },
            {
                "mistake": "'제세동'과 '제세동기'를 구분하지 않음",
                "correction": "제세동은 sốc điện, 제세동기는 máy sốc điện",
                "explanation": "시술과 기기 구분"
            }
        ],
        "examples": [
            {
                "ko": "24시간 심전도 검사 결과 심방세동이 확인되었습니다.",
                "vi": "Kết quả điện tâm đồ 24 giờ xác nhận rung nhĩ (fibrillation nhĩ).",
                "situation": "formal"
            },
            {
                "ko": "부정맥이 있으면 가슴 두근거림, 어지러움, 실신 등이 나타날 수 있습니다.",
                "vi": "Nếu có rối loạn nhịp tim, có thể xuất hiện hồi hộp, chóng mặt, ngất.",
                "situation": "onsite"
            },
            {
                "ko": "부정맥 종류에 따라 약물 치료, 시술, 또는 경과 관찰을 합니다.",
                "vi": "Tùy loại rối loạn nhịp tim mà điều trị bằng thuốc, thủ thuật, hoặc theo dõi.",
                "situation": "informal"
            }
        ],
        "relatedTerms": ["심방세동", "심실빈맥", "홀터검사", "항응고제"]
    },
    {
        "slug": "rung-nhi",
        "korean": "심방세동",
        "vietnamese": "Rung nhĩ",
        "hanja": "心房細動",
        "hanjaReading": "心(마음 심) + 房(방 방) + 細(가늘 세) + 動(움직일 동)",
        "pronunciation": "심방세동",
        "meaningKo": "심장의 위쪽 방인 심방이 무질서하게 떨리면서 불규칙한 맥박을 만드는 가장 흔한 부정맥. 통역 시 주의할 점은 심방세동 자체는 즉시 생명을 위협하지 않지만, 심방 내에 혈전이 생겨 뇌졸중을 일으킬 위험이 5배 높아진다는 것입니다. 따라서 항응고제 복용의 중요성을 강조해야 하며, 한국에서는 NOAC(새로운 경구 항응고제)를 많이 사용하나 베트남에서는 비싸서 와파린을 주로 사용합니다.",
        "meaningVi": "Loại rối loạn nhịp tim phổ biến nhất, tâm nhĩ co bóp lộn xộn làm nhịp tim không đều. Tuy không nguy hiểm ngay lập tức, nhưng dễ hình thành cục máu đông trong nhĩ, gây đột quỵ não với nguy cơ cao gấp 5 lần. Cần uống thuốc chống đông máu lâu dài để phòng ngừa đột quỵ.",
        "context": "심장내과, 뇌졸중센터",
        "culturalNote": "한국에서는 CHA2DS2-VASc 점수를 계산하여 항응고제 처방을 결정하며, 심방세동 환자를 뇌졸중 고위험군으로 적극 관리합니다. 베트남에서는 INR 검사(와파린 모니터링)가 불편하고 비싸 환자 순응도가 낮으며, NOAC은 더 비싸 사용이 제한적입니다. 또한 한국에서는 전극도자절제술로 완치를 시도하지만 베트남에서는 약물 치료에 주로 의존합니다.",
        "commonMistakes": [
            {
                "mistake": "'심방세동'을 '심장 떨림'으로 단순화",
                "correction": "rung nhĩ (심방세동) - 특정 부정맥 진단명",
                "explanation": "정확한 의학 용어 사용"
            },
            {
                "mistake": "심방세동과 심실세동을 혼동",
                "correction": "심방세동은 rung nhĩ, 심실세동은 rung thất",
                "explanation": "심실세동은 즉각적 사망 위험이 있어 완전히 다름"
            },
            {
                "mistake": "'항응고제'를 '혈액을 묽게 하는 약'으로만 설명",
                "correction": "thuốc chống đông máu (항응고제)",
                "explanation": "정확한 약물 분류명 사용"
            }
        ],
        "examples": [
            {
                "ko": "심방세동이 확인되어 뇌졸중 예방을 위해 항응고제를 처방합니다.",
                "vi": "Xác nhận rung nhĩ, kê thuốc chống đông máu để phòng ngừa đột quỵ.",
                "situation": "formal"
            },
            {
                "ko": "맥박이 불규칙하고 가슴이 두근거린다면 심방세동일 수 있습니다.",
                "vi": "Nếu mạch đập không đều và hồi hộp, có thể là rung nhĩ.",
                "situation": "onsite"
            },
            {
                "ko": "심방세동 환자는 평생 항응고제를 복용해야 할 수 있습니다.",
                "vi": "Bệnh nhân rung nhĩ có thể phải uống thuốc chống đông máu suốt đời.",
                "situation": "informal"
            }
        ],
        "relatedTerms": ["부정맥", "뇌졸중", "항응고제", "전극도자절제술"]
    },
    {
        "slug": "nhip-nhanh-that",
        "korean": "심실빈맥",
        "vietnamese": "Nhịp nhanh thất",
        "hanja": "心室頻脈",
        "hanjaReading": "心(마음 심) + 室(집 실) + 頻(자주 빈) + 脈(맥 맥)",
        "pronunciation": "심실빈맥",
        "meaningKo": "심장의 아래쪽 방인 심실에서 비정상적으로 빠른 전기 신호가 발생하여 분당 100회 이상 빠르게 뛰는 치명적인 부정맥. 통역 시 매우 주의해야 할 점은 심실빈맥이 심실세동으로 진행하면 즉시 심정지가 되어 사망하므로, 즉각적인 전기적 제세동이나 항부정맥제 투여가 필요한 응급상황이라는 것입니다.",
        "meaningVi": "Loại rối loạn nhịp tim nguy hiểm, tâm thất đập rất nhanh (trên 100 lần/phút) do tín hiệu điện bất thường. Có thể gây choáng, ngất, hoặc tiến triển thành rung thất (ngừng tim). Đây là cấp cứu, cần sốc điện hoặc thuốc chống loạn nhịp ngay lập tức. Bệnh nhân nguy cơ cao cần đặt máy sốc điện cấy (ICD).",
        "context": "심장내과, 응급의학, 중환자의학",
        "culturalNote": "한국에서는 심실빈맥 고위험 환자(심근경색 후유증, 심부전 등)에게 삽입형 제세동기(ICD)를 적극 권장하며 보험 적용도 됩니다. 베트남에서는 ICD가 매우 비싸고 시술 가능한 병원이 제한적이어서 약물 치료에 의존하는 경우가 많습니다. 또한 한국에서는 전기생리학검사와 전극도자절제술로 근본 치료를 시도하지만 베트남에서는 흔하지 않습니다.",
        "commonMistakes": [
            {
                "mistake": "심실빈맥과 심방빈맥을 구분하지 않음",
                "correction": "심실빈맥은 nhịp nhanh thất, 심방빈맥은 nhịp nhanh nhĩ",
                "explanation": "심실빈맥이 훨씬 위험하므로 반드시 구분"
            },
            {
                "mistake": "'빈맥'을 단순히 '맥박 빠름'으로만 표현",
                "correction": "nhịp nhanh (빈맥) - 의학적 진단명",
                "explanation": "일시적 빈맥과 병적 빈맥 구분 필요"
            },
            {
                "mistake": "심실빈맥과 심실세동을 동일하게 표현",
                "correction": "심실빈맥은 nhịp nhanh thất, 심실세동은 rung thất",
                "explanation": "빈맥은 아직 조직적 박동, 세동은 무질서한 떨림"
            }
        ],
        "examples": [
            {
                "ko": "심전도에서 넓은 QRS파를 보이는 심실빈맥이 확인되었습니다.",
                "vi": "Điện tâm đồ thấy nhịp nhanh thất với sóng QRS rộng.",
                "situation": "formal"
            },
            {
                "ko": "심실빈맥이 지속되면 즉시 전기 제세동을 시행해야 합니다.",
                "vi": "Nếu nhịp nhanh thất kéo dài, phải sốc điện ngay lập tức.",
                "situation": "onsite"
            },
            {
                "ko": "심실빈맥 재발 방지를 위해 제세동기 삽입을 권장합니다.",
                "vi": "Để phòng tái phát nhịp nhanh thất, khuyến cáo đặt máy sốc điện cấy.",
                "situation": "informal"
            }
        ],
        "relatedTerms": ["심실세동", "부정맥", "제세동기", "항부정맥제"]
    },
    {
        "slug": "suy-tim",
        "korean": "심부전",
        "vietnamese": "Suy tim",
        "hanja": "心不全",
        "hanjaReading": "心(마음 심) + 不(아니 불) + 全(온전할 전)",
        "pronunciation": "심부전",
        "meaningKo": "심장이 몸에 필요한 만큼의 혈액을 펌프질하지 못하는 상태로, 호흡곤란, 부종, 피로가 주 증상. 통역 시 주의할 점은 심부전이 만성 질환으로 완치가 어렵고 지속적인 약물 치료와 생활 습관 관리가 필요하다는 것입니다. 한국에서는 좌심실 박출률(EF)에 따라 치료 방침이 달라지며, EF가 낮으면 ICD나 심장재동기화 치료(CRT)를 고려합니다.",
        "meaningVi": "Tình trạng tim không bơm đủ máu nuôi cơ thể, gây khó thở, phù chân, mệt mỏi. Là bệnh mãn tính, cần uống thuốc và kiểm soát chế độ ăn (hạn chế muối, nước) suốt đời. Nếu nặng, có thể cần đặt máy tạo nhịp đặc biệt (CRT) hoặc ghép tim.",
        "context": "심장내과, 가정의학과",
        "culturalNote": "한국에서는 심부전 환자를 심부전 클리닉에서 다학제 팀(의사, 간호사, 약사, 영양사)이 관리하며, BNP 검사로 중증도를 평가합니다. 베트남에서는 이런 체계적 관리가 부족하고, 환자들이 염분 제한과 수분 제한의 중요성을 잘 이해하지 못해 재입원율이 높습니다. 또한 한국에서는 심부전 치료제(ARNi, SGLT2i)가 최신 가이드라인대로 사용되나 베트남에서는 접근성이 낮습니다.",
        "commonMistakes": [
            {
                "mistake": "'심부전'을 '심장 약함'으로 직역",
                "correction": "suy tim (심부전) - 의학 진단명",
                "explanation": "단순 약한 것이 아닌 기능 부전 상태"
            },
            {
                "mistake": "급성 심부전과 만성 심부전을 구분하지 않음",
                "correction": "급성은 suy tim cấp, 만성은 suy tim mãn",
                "explanation": "치료 강도와 장소(입원 vs 외래)가 다름"
            },
            {
                "mistake": "'박출률'을 번역 없이 EF로만 사용",
                "correction": "phân suất tống máu (EF) 또는 EF (tỷ lệ máu bơm ra)",
                "explanation": "베트남 환자도 이해할 수 있도록 설명 추가"
            }
        ],
        "examples": [
            {
                "ko": "심초음파 검사 결과 좌심실 박출률이 30%로 중증 심부전입니다.",
                "vi": "Kết quả siêu âm tim cho thấy EF thất trái 30%, suy tim nặng.",
                "situation": "formal"
            },
            {
                "ko": "심부전 환자는 하루 염분 섭취를 5g 이하로 제한해야 합니다.",
                "vi": "Bệnh nhân suy tim phải hạn chế muối dưới 5g mỗi ngày.",
                "situation": "onsite"
            },
            {
                "ko": "계단만 오르면 숨이 차고 다리가 붓는다면 심부전을 의심하세요.",
                "vi": "Nếu chỉ lên cầu thang cũng khó thở và chân phù, nghi ngờ suy tim.",
                "situation": "informal"
            }
        ],
        "relatedTerms": ["심근경색", "고혈압", "박출률", "이뇨제"]
    },
    {
        "slug": "benh-van-tim",
        "korean": "판막질환",
        "vietnamese": "Bệnh van tim",
        "hanja": "瓣膜疾患",
        "hanjaReading": "瓣(꽃부리 판) + 膜(막 막) + 疾(병 질) + 患(근심 환)",
        "pronunciation": "판막질환",
        "meaningKo": "심장의 네 개 판막(승모판, 대동맥판, 삼첨판, 폐동맥판) 중 하나 이상이 좁아지거나(협착) 제대로 닫히지 않아(역류) 발생하는 질환. 통역 시 주의할 점은 한국에서는 판막 질환을 조기에 발견하여 적절한 시기에 수술(판막 성형술 또는 판막 치환술)을 하지만, 베트남에서는 류마티스열 후유증으로 인한 판막 질환이 많고 발견이 늦어 중증으로 진행된 경우가 많다는 것입니다.",
        "meaningVi": "Bệnh lý một hoặc nhiều van tim (van hai lá, van động mạch chủ, van ba lá, van động mạch phổi) bị hẹp hoặc hở, làm tim hoạt động kém hiệu quả. Triệu chứng gồm khó thở, mệt, đau ngực. Nếu nặng cần phẫu thuật sửa van hoặc thay van tim.",
        "context": "심장내과, 심장외과",
        "culturalNote": "한국에서는 퇴행성 판막 질환(노화로 인한)이 주를 이루며, 경피적 판막 시술(TAVI 등)이 발전하여 고령 환자도 수술 없이 치료 가능합니다. 베트남에서는 아직 류마티스성 판막 질환이 많고, TAVI 같은 최신 시술은 극소수 병원에서만 가능하여 대부분 개심술로 판막을 치환합니다. 또한 기계판막 사용 시 평생 항응고제를 복용해야 하는데, 베트남에서는 모니터링이 어려워 합병증이 많습니다.",
        "commonMistakes": [
            {
                "mistake": "'판막'을 '밸브'로 음차",
                "correction": "van tim (판막)",
                "explanation": "정확한 의학 용어 사용"
            },
            {
                "mistake": "판막 협착과 판막 역류를 구분하지 않음",
                "correction": "협착은 hẹp van, 역류는 hở van",
                "explanation": "병태생리와 치료가 다르므로 구분 필요"
            },
            {
                "mistake": "'기계판막'과 '생체판막'을 설명 없이 사용",
                "correction": "기계판막 van cơ học, 생체판막 van sinh học + 각각 장단점 설명",
                "explanation": "환자가 선택해야 하므로 차이점 명확히 전달"
            }
        ],
        "examples": [
            {
                "ko": "심초음파에서 중등도의 승모판 역류가 보입니다.",
                "vi": "Siêu âm tim thấy hở van hai lá mức độ trung bình.",
                "situation": "formal"
            },
            {
                "ko": "대동맥판 협착이 심하여 판막 치환술이 필요합니다.",
                "vi": "Hẹp van động mạch chủ nặng, cần phẫu thuật thay van.",
                "situation": "onsite"
            },
            {
                "ko": "기계판막을 선택하면 평생 항응고제를 먹어야 하지만 내구성이 좋습니다.",
                "vi": "Nếu chọn van cơ học, phải uống thuốc chống đông suốt đời nhưng độ bền cao.",
                "situation": "informal"
            }
        ],
        "relatedTerms": ["승모판협착증", "대동맥판역류", "판막치환술", "심초음파"]
    }
]

def main():
    print("=" * 80)
    print("Medical Terms Addition Script - v2-761 Part 2")
    print("Adding terms 11-50 (Cardiology, Pulmonology)")
    print("=" * 80)

    try:
        with open(file_path, 'r', encoding='utf-8') as f:
            data = json.load(f)
        print(f"✓ Successfully loaded existing data: {len(data)} terms")
    except Exception as e:
        print(f"✗ Error loading file: {e}")
        return

    existing_slugs = {term['slug'] for term in data}
    new_slugs = {term['slug'] for term in additional_terms}
    duplicates = existing_slugs & new_slugs

    if duplicates:
        print(f"\n⚠ Warning: Found {len(duplicates)} duplicate slugs:")
        for slug in duplicates:
            print(f"  - {slug}")
        terms_to_add = [t for t in additional_terms if t['slug'] not in duplicates]
    else:
        terms_to_add = additional_terms

    data.extend(terms_to_add)

    try:
        with open(file_path, 'w', encoding='utf-8') as f:
            json.dump(data, f, ensure_ascii=False, indent=2)
        print(f"\n✓ Successfully added {len(terms_to_add)} new terms")
        print(f"✓ Total terms in medical.json: {len(data)}")
    except Exception as e:
        print(f"\n✗ Error saving file: {e}")
        return

    print("\n" + "=" * 80)
    print(f"Part 2 completed: {len(terms_to_add)} terms added")
    print("=" * 80)

if __name__ == "__main__":
    main()
