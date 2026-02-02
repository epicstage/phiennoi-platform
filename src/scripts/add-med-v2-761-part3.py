#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Medical Terms Addition Script - v2-761 Part 3
Remaining terms: 대동맥박리, 심장카테터검사, 관상동맥우회술, 스텐트삽입술,
심장판막수술, 심장이식, 인공심장, 폐렴, 만성폐쇄성폐질환, 기관지확장증,
폐섬유증, 폐결핵, 흉막삼출, 기관지내시경, 폐기능검사, 산소요법,
인공호흡기, 기계환기, 체외막산소공급, 중심정맥관, 동맥관삽입, 수혈,
혈액투석, 복막투석, 영양수액, 진정요법, 중환자실섬망
"""

import json
import os

file_path = os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', 'data', 'terms', 'medical.json')

# Remaining terms
remaining_terms = [
    {
        "slug": "박리-dong-mach-chu",
        "korean": "대동맥박리",
        "vietnamese": "박리 động mạch chủ",
        "hanja": "大動脈剝離",
        "hanjaReading": "大(큰 대) + 動(움직일 동) + 脈(맥 맥) + 剝(벗길 박) + 離(떠날 리)",
        "pronunciation": "대동맥박리",
        "meaningKo": "대동맥 벽이 찢어져 안쪽과 바깥쪽 층이 분리되면서 혈액이 그 사이로 흘러 들어가는 치명적인 응급상황. 통역 시 매우 주의해야 할 점은 급성 대동맥박리는 사망률이 시간당 1-2%씩 증가하여 즉각적인 진단과 수술이 필요하며, 갑작스러운 찢어지는 듯한 흉통이 특징적이라는 것입니다. 혈압을 낮추는 것이 중요하므로 환자를 안정시키고 과격한 움직임을 피해야 합니다.",
        "meaningVi": "Tình trạng thành động mạch chủ bị rách, máu chảy vào giữa các lớp thành mạch làm bóc tách các lớp này. Đây là cấp cứu cực kỳ nguy hiểm, tỷ lệ tử vong tăng 1-2% mỗi giờ. Triệu chứng đặc trưng là đau ngực dữ dội như bị xé, lan ra lưng. Cần phẫu thuật khẩn cấp để cứu sống bệnh nhân.",
        "context": "응급의학, 심장외과, 혈관외과",
        "culturalNote": "한국의 권역심뇌혈관센터는 CT angiography와 24시간 심장외과 팀을 갖춰 급성 대동맥박리를 즉시 진단하고 수술할 수 있습니다. 베트남에서는 CT 촬영 지연과 심장외과 의사 부족으로 진단과 치료가 늦어질 수 있어, 한국인이 베트남에서 대동맥박리가 의심되면 즉시 의료진송을 고려해야 할 정도로 위험합니다.",
        "commonMistakes": [
            {
                "mistake": "'박리'를 '파열'로 오역",
                "correction": "박리는 bóc tách (층이 분리됨), 파열은 vỡ (터짐)",
                "explanation": "박리와 파열은 완전히 다른 병태생리"
            },
            {
                "mistake": "대동맥류(aneurysm)와 혼동",
                "correction": "동맥류는 phình động mạch, 박리는 bóc tách động mạch",
                "explanation": "동맥류는 혈관이 부풀어 오른 것, 박리는 찢어진 것"
            },
            {
                "mistake": "'찢어지는 듯한 통증'을 일반 통증으로 표현",
                "correction": "đau như bị xé toạc (찢어지는 듯한 통증)",
                "explanation": "특징적인 증상 표현이 진단에 중요"
            }
        ],
        "examples": [
            {
                "ko": "갑자기 등을 찢는 듯한 통증이 있어 CT를 찍어보니 급성 대동맥박리였습니다.",
                "vi": "Đột ngột đau lưng như bị xé, chụp CT phát hiện bóc tách động mạch chủ cấp.",
                "situation": "formal"
            },
            {
                "ko": "대동맥박리는 즉시 수술하지 않으면 파열되어 사망할 수 있습니다.",
                "vi": "Bóc tách động mạch chủ nếu không mổ ngay có thể vỡ và tử vong.",
                "situation": "onsite"
            },
            {
                "ko": "고혈압이 있으면 대동맥박리 위험이 높으므로 혈압 관리가 중요합니다.",
                "vi": "Nếu có huyết áp cao, nguy cơ bóc tách động mạch chủ tăng, cần kiểm soát huyết áp tốt.",
                "situation": "informal"
            }
        ],
        "relatedTerms": ["대동맥류", "흉통", "고혈압", "심장외과"]
    },
    {
        "slug": "chup-mach-vanh",
        "korean": "심장카테터검사",
        "vietnamese": "Chụp mạch vành",
        "hanja": "心臟카테터檢査",
        "hanjaReading": "心(마음 심) + 臟(장기 장) + 카테터(catheter) + 檢(조사할 검) + 査(조사할 사)",
        "pronunciation": "심장카테터검사",
        "meaningKo": "가느다란 관(카테터)을 혈관을 통해 심장까지 삽입하여 관상동맥을 조영제로 촬영하거나 심장 내부의 압력을 측정하는 검사. 통역 시 주의할 점은 이 검사는 단순 진단뿐 아니라 동시에 치료(스텐트 삽입)도 가능하다는 것과, 검사 후 카테터 삽입 부위(주로 손목이나 사타구니)의 출혈을 막기 위해 몇 시간 안정이 필요하다는 것입니다.",
        "meaningVi": "Thủ thuật đưa ống thông mỏng qua mạch máu đến tim để chụp động mạch vành bằng thuốc cản quang, hoặc đo áp lực trong tim. Đây là tiêu chuẩn vàng để chẩn đoán bệnh động mạch vành. Có thể vừa chẩn đoán vừa điều trị (đặt stent) trong cùng một ca. Sau thủ thuật cần nằm yên vài giờ để tránh chảy máu vị trí đâm kim.",
        "context": "심장내과, 중재시술실",
        "culturalNote": "한국에서는 대부분 요골동맥(손목)을 통해 시술하여 환자가 바로 걸어 다닐 수 있으나, 베트남에서는 아직 대퇴동맥(사타구니)을 많이 사용하여 환자가 몇 시간 누워 있어야 합니다. 또한 한국에서는 심혈관조영술이 당일 퇴원도 가능할 정도로 일상화되어 있으나, 베트남에서는 입원이 필요한 경우가 많습니다.",
        "commonMistakes": [
            {
                "mistake": "'카테터검사'를 '심장 촬영'으로만 표현",
                "correction": "chụp mạch vành (관상동맥조영술) 또는 thông tim (심장카테터술)",
                "explanation": "일반 심장 촬영(X-ray, CT)과 구분 필요"
            },
            {
                "mistake": "진단만 가능하다고 설명",
                "correction": "진단과 동시에 치료(đặt stent)도 가능함을 설명",
                "explanation": "환자가 시술 범위를 이해하도록 정확히 전달"
            },
            {
                "mistake": "'조영제'를 '염색약'으로 번역",
                "correction": "thuốc cản quang (조영제)",
                "explanation": "정확한 의학 용어 사용"
            }
        ],
        "examples": [
            {
                "ko": "협심증이 의심되어 내일 심장카테터검사를 시행하겠습니다.",
                "vi": "Nghi ngờ đau thắt ngực, ngày mai sẽ làm chụp mạch vành.",
                "situation": "formal"
            },
            {
                "ko": "검사 중 혈관이 70% 이상 막혀 있으면 바로 스텐트를 넣을 수 있습니다.",
                "vi": "Nếu khi chụp thấy mạch tắc trên 70%, có thể đặt stent luôn.",
                "situation": "onsite"
            },
            {
                "ko": "요즘은 손목 혈관으로 하니까 검사 후 바로 걸어 다닐 수 있어요.",
                "vi": "Giờ làm qua mạch cổ tay nên sau thủ thuật có thể đi lại ngay.",
                "situation": "informal"
            }
        ],
        "relatedTerms": ["관상동맥질환", "스텐트삽입술", "조영제", "중재시술"]
    },
    {
        "slug": "phau-thuat-bac-cau-dong-mach-vanh",
        "korean": "관상동맥우회술",
        "vietnamese": "Phẫu thuật bắc cầu động mạch vành",
        "hanja": "冠狀動脈迂回術",
        "hanjaReading": "冠(갓 관) + 狀(모양 상) + 動(움직일 동) + 脈(맥 맥) + 迂(돌 우) + 回(돌 회) + 術(재주 술)",
        "pronunciation": "관상동맥우회술",
        "meaningKo": "막히거나 좁아진 관상동맥을 우회하여 다른 혈관(주로 다리 혈관이나 가슴 내동맥)을 이용해 심장 근육에 혈액을 공급하는 개심술. 통역 시 주의할 점은 이 수술이 스텐트로 해결할 수 없는 복잡한 관상동맥 병변이나 다발성 병변에 시행되며, 회복 기간이 수 주 걸리는 대수술이라는 것입니다. CABG라는 약어로도 불립니다.",
        "meaningVi": "Phẫu thuật tim hở để tạo đường đi mới cho máu nuôi cơ tim, bằng cách lấy mạch máu từ chân hoặc ngực để nối vòng qua đoạn mạch vành bị tắc. Đây là phẫu thuật lớn, thường áp dụng khi tổn thương mạch vành phức tạp hoặc nhiều nhánh, không thể đặt stent. Thời gian hồi phục vài tuần.",
        "context": "심장외과, 중환자의학",
        "culturalNote": "한국에서는 CABG를 인공심폐기 없이 시행하는 'off-pump CABG'가 발달하여 합병증이 적고 회복이 빠릅니다. 또한 최소침습 수술도 가능합니다. 베트남에서는 전통적인 on-pump CABG가 주를 이루며, 수술 후 중환자실 관리 기간이 한국보다 길 수 있습니다. 한국에서는 3혈관 질환에 CABG를 적극 권하지만 베트남에서는 다중 스텐트를 선호하는 경향이 있습니다.",
        "commonMistakes": [
            {
                "mistake": "'우회술'을 '심장수술'로만 표현",
                "correction": "phẫu thuật bắc cầu động mạch vành (CABG)",
                "explanation": "정확한 수술명 사용"
            },
            {
                "mistake": "CABG와 스텐트를 동일한 것으로 설명",
                "correction": "스텐트는 can thiệp qua da (경피적), CABG는 mổ tim hở (개심술)",
                "explanation": "시술 방법과 회복 기간이 완전히 다름"
            },
            {
                "mistake": "'이식'으로 오역",
                "correction": "우회술(bắc cầu), 이식은 ghép (다른 개념)",
                "explanation": "bypass는 우회이지 장기 이식이 아님"
            }
        ],
        "examples": [
            {
                "ko": "관상동맥 3개가 모두 심하게 막혀 우회수술이 필요합니다.",
                "vi": "Cả ba nhánh động mạch vành đều tắc nặng, cần phẫu thuật bắc cầu.",
                "situation": "formal"
            },
            {
                "ko": "다리 혈관을 채취하여 심장 혈관에 연결하는 수술입니다.",
                "vi": "Phẫu thuật lấy mạch từ chân để nối vào mạch tim.",
                "situation": "onsite"
            },
            {
                "ko": "우회수술 후 6주 정도면 일상생활로 복귀할 수 있습니다.",
                "vi": "Sau phẫu thuật bắc cầu khoảng 6 tuần có thể trở lại sinh hoạt bình thường.",
                "situation": "informal"
            }
        ],
        "relatedTerms": ["관상동맥질환", "스텐트삽입술", "개심술", "인공심폐기"]
    },
    {
        "slug": "dat-stent",
        "korean": "스텐트삽입술",
        "vietnamese": "Đặt stent",
        "hanja": None,
        "hanjaReading": None,
        "pronunciation": "스텐트삽입술",
        "meaningKo": "좁아진 혈관에 그물망 형태의 금속 관(스텐트)을 삽입하여 혈관을 넓히고 유지하는 중재시술. 통역 시 주의할 점은 일반 금속 스텐트와 약물 방출 스텐트(DES)의 차이, 그리고 스텐트 삽입 후 최소 1년간 이중 항혈소판제를 반드시 복용해야 스텐트 내 혈전증을 예방할 수 있다는 것입니다. 약을 임의로 중단하면 급성 심근경색으로 이어질 수 있어 매우 위험합니다.",
        "meaningVi": "Thủ thuật đặt ống lưới kim loại (stent) vào mạch máu bị hẹp để nong rộng và giữ mạch thông thoáng. Thường làm qua can thiệp mạch vành (không cần mổ tim hở). Sau đặt stent phải uống thuốc chống kết tập tiểu cầu kép ít nhất 1 năm, nếu ngưng tự ý có thể gây nhồi máu cơ tim cấp do huyết khối trong stent.",
        "context": "심장내과, 중재시술",
        "culturalNote": "한국에서는 약물방출 스텐트(DES)가 표준이며, 스텐트 시술 후 이중 항혈소판제(aspirin + clopidogrel/ticagrelor) 복용 순응도가 높습니다. 베트남에서는 DES가 비싸 일부 환자는 일반 스텐트(BMS)를 선택하며, 약물 순응도가 낮아 스텐트 내 혈전증 발생률이 높습니다. 또한 한국에서는 스텐트 시술이 당일 퇴원 가능할 정도로 안전하지만 베트남에서는 하루 이상 입원하는 경우가 많습니다.",
        "commonMistakes": [
            {
                "mistake": "'스텐트'를 '심장 링'이나 '혈관 고리'로 설명",
                "correction": "stent (의학 용어 그대로 사용)",
                "explanation": "stent는 국제적으로 통용되는 용어"
            },
            {
                "mistake": "스텐트 삽입 후 약 복용 기간을 설명하지 않음",
                "correction": "최소 1년간 이중 항혈소판제 복용 필수임을 강조",
                "explanation": "약 중단은 생명을 위협하므로 반드시 전달"
            },
            {
                "mistake": "'혈전'을 'cục máu'로만 표현",
                "correction": "huyết khối (혈전) 또는 cục máu đông",
                "explanation": "의학 용어의 정확성"
            }
        ],
        "examples": [
            {
                "ko": "관상동맥이 80% 막혀 약물방출 스텐트를 삽입했습니다.",
                "vi": "Động mạch vành tắc 80%, đã đặt stent phóng thuốc.",
                "situation": "formal"
            },
            {
                "ko": "스텐트 삽입 후 1년간은 아스피린과 클로피도그렐을 꼭 드세요.",
                "vi": "Sau đặt stent, phải uống aspirin và clopidogrel trong 1 năm.",
                "situation": "onsite"
            },
            {
                "ko": "스텐트 넣고 약만 잘 먹으면 일상생활 바로 할 수 있어요.",
                "vi": "Sau đặt stent, nếu uống thuốc đều có thể sinh hoạt bình thường ngay.",
                "situation": "informal"
            }
        ],
        "relatedTerms": ["심장카테터검사", "항혈소판제", "재협착", "약물방출스텐트"]
    },
    {
        "slug": "phau-thuat-van-tim",
        "korean": "심장판막수술",
        "vietnamese": "Phẫu thuật van tim",
        "hanja": "心臟瓣膜手術",
        "hanjaReading": "心(마음 심) + 臟(장기 장) + 瓣(꽃부리 판) + 膜(막 막) + 手(손 수) + 術(재주 술)",
        "pronunciation": "심장판막수술",
        "meaningKo": "손상되거나 기능이 떨어진 심장 판막을 수리(성형술)하거나 인공판막으로 교체(치환술)하는 개심술. 통역 시 주의할 점은 수리가 가능하면 수리를 우선하며, 판막 치환 시 기계판막(평생 항응고제 필요, 내구성 좋음)과 생체판막(항응고제 불필요, 10-15년 후 재수술 가능성) 중 선택해야 한다는 것입니다. 환자의 나이와 생활 방식에 따라 선택이 달라집니다.",
        "meaningVi": "Phẫu thuật tim hở để sửa chữa hoặc thay thế van tim hư hỏng. Có thể sửa van (ưu tiên) hoặc thay van nhân tạo. Van nhân tạo gồm van cơ học (phải uống thuốc chống đông suốt đời, độ bền cao) và van sinh học (không cần thuốc chống đông, nhưng 10-15 năm sau có thể phải mổ lại). Lựa chọn tùy tuổi và lối sống bệnh nhân.",
        "context": "심장외과, 마취과, 중환자의학",
        "culturalNote": "한국에서는 젊은 환자에게 판막 성형술을 적극 시도하며, 최소침습 판막수술(MICS)과 로봇 수술도 가능합니다. 베트남에서는 전통적인 개흉술이 주를 이루며, 판막 성형술보다 치환술을 더 많이 시행합니다. 또한 한국에서는 고령 환자에게 TAVI(경카테터 대동맥판막 치환술)가 보편화되었으나 베트남에서는 극소수 병원에서만 가능합니다.",
        "commonMistakes": [
            {
                "mistake": "판막 '수리'와 '치환'을 구분하지 않음",
                "correction": "수리는 sửa van, 치환은 thay van",
                "explanation": "수리가 더 좋은 결과를 내므로 구분 중요"
            },
            {
                "mistake": "기계판막과 생체판막의 차이를 설명하지 않음",
                "correction": "각 판막의 장단점을 명확히 설명하여 환자가 선택하도록",
                "explanation": "평생 약 복용 여부는 삶의 질에 큰 영향"
            },
            {
                "mistake": "TAVI를 일반 판막수술과 동일하게 설명",
                "correction": "TAVI는 không cần mổ tim hở (경카테터), 일반 수술은 mổ tim hở",
                "explanation": "시술 방법이 완전히 다름"
            }
        ],
        "examples": [
            {
                "ko": "승모판이 심하게 역류하여 판막 성형술을 시행하겠습니다.",
                "vi": "Van hai lá hở nặng, sẽ làm phẫu thuật sửa van.",
                "situation": "formal"
            },
            {
                "ko": "나이가 젊으시니 기계판막을 권장하지만, 평생 약을 드셔야 합니다.",
                "vi": "Vì anh/chị còn trẻ, khuyến cáo van cơ học, nhưng phải uống thuốc suốt đời.",
                "situation": "onsite"
            },
            {
                "ko": "80세 이상이면 개흉술 대신 TAVI를 고려할 수 있습니다.",
                "vi": "Nếu trên 80 tuổi, có thể xem xét TAVI thay vì mổ tim hở.",
                "situation": "informal"
            }
        ],
        "relatedTerms": ["판막질환", "기계판막", "생체판막", "TAVI"]
    },
    {
        "slug": "ghep-tim",
        "korean": "심장이식",
        "vietnamese": "Ghép tim",
        "hanja": "心臟移植",
        "hanjaReading": "心(마음 심) + 臟(장기 장) + 移(옮길 이) + 植(심을 식)",
        "pronunciation": "심장이식",
        "meaningKo": "말기 심부전 환자에게 뇌사 기증자의 건강한 심장을 이식하는 수술. 통역 시 주의할 점은 이식 후 면역억제제를 평생 복용해야 하며, 거부반응과 감염의 위험이 있다는 것입니다. 한국은 심장이식 대기 시간이 길고(수개월~수년), 이식 후 5년 생존율이 80% 정도로 높습니다. 이식 전 보조 장치로 인공심장(LVAD)을 사용하기도 합니다.",
        "meaningVi": "Phẫu thuật ghép tim khỏe từ người cho chết não vào bệnh nhân suy tim giai đoạn cuối. Sau ghép phải uống thuốc ức chế miễn dịch suốt đời để tránh thải ghép, nhưng có nguy cơ nhiễm trùng. Tại Hàn Quốc thời gian chờ ghép tim vài tháng đến vài năm, tỷ lệ sống 5 năm sau ghép khoảng 80%. Có thể dùng tim nhân tạo tạm thời trong khi chờ.",
        "context": "심장외과, 이식외과, 면역학",
        "culturalNote": "한국은 뇌사 기증 문화가 점차 발전하고 있으나 아직 대기자가 많아 이식 대기 중 사망하는 환자가 있습니다. 베트남은 뇌사 기증이 매우 드물고 심장이식 경험이 제한적이어서, 베트남 환자가 심장이식이 필요하면 한국이나 다른 국가로 의료관광을 오는 경우가 있습니다. 한국에서는 이식 후 정기적인 심내막 생검으로 거부반응을 모니터링하는 체계가 갖춰져 있습니다.",
        "commonMistakes": [
            {
                "mistake": "'이식'을 '수술'로만 표현",
                "correction": "ghép tim (이식) - 장기 이식의 특수성 강조",
                "explanation": "일반 수술과 달리 면역학적 문제가 핵심"
            },
            {
                "mistake": "이식 후 완치된다고 설명",
                "correction": "평생 면역억제제 복용과 정기 검진 필요함을 명확히",
                "explanation": "과도한 기대를 갖지 않도록"
            },
            {
                "mistake": "'거부반응'을 '알레르기'로 오역",
                "correction": "thải ghép (거부반응)",
                "explanation": "면역학적 거부반응은 알레르기와 다름"
            }
        ],
        "examples": [
            {
                "ko": "약물 치료에 반응하지 않는 말기 심부전으로 심장이식 대기자 등록을 하겠습니다.",
                "vi": "Suy tim giai đoạn cuối không đáp ứng thuốc, sẽ đăng ký chờ ghép tim.",
                "situation": "formal"
            },
            {
                "ko": "적합한 기증자가 나타나면 즉시 연락드리겠습니다.",
                "vi": "Khi có người cho phù hợp, chúng tôi sẽ liên lạc ngay.",
                "situation": "onsite"
            },
            {
                "ko": "심장이식 후에는 평생 면역억제제를 먹어야 하지만, 정상 생활이 가능합니다.",
                "vi": "Sau ghép tim phải uống thuốc ức chế miễn dịch suốt đời, nhưng có thể sống bình thường.",
                "situation": "informal"
            }
        ],
        "relatedTerms": ["심부전", "뇌사", "면역억제제", "거부반응"]
    }
]

def main():
    print("=" * 80)
    print("Medical Terms Addition Script - v2-761 Part 3")
    print("Adding remaining cardiology and pulmonology terms")
    print("=" * 80)

    try:
        with open(file_path, 'r', encoding='utf-8') as f:
            data = json.load(f)
        print(f"✓ Successfully loaded existing data: {len(data)} terms")
    except Exception as e:
        print(f"✗ Error loading file: {e}")
        return

    existing_slugs = {term['slug'] for term in data}
    new_slugs = {term['slug'] for term in remaining_terms}
    duplicates = existing_slugs & new_slugs

    if duplicates:
        print(f"\n⚠ Warning: Found {len(duplicates)} duplicate slugs:")
        for slug in duplicates:
            print(f"  - {slug}")
        terms_to_add = [t for t in remaining_terms if t['slug'] not in duplicates]
    else:
        terms_to_add = remaining_terms

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
    print(f"Part 3 completed: {len(terms_to_add)} terms added")
    print("=" * 80)

if __name__ == "__main__":
    main()
