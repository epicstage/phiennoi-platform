#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Add 20 NEW medical terms (emergency & cardiopulmonary focus) - Tier S quality
"""

import json
import os

# PATH CODE (MUST USE)
file_path = os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', 'data', 'terms', 'medical.json')
with open(file_path, 'r', encoding='utf-8') as f:
    data = json.load(f)  # data is a LIST, not dict

existing_slugs = {t['slug'] for t in data}

# 20 NEW medical terms
new_terms = [
    {
        "slug": "hoi-sinh-tim-phoi",
        "korean": "심폐소생술",
        "vietnamese": "Hồi sinh tim phổi",
        "hanja": "心肺蘇生術",
        "hanjaReading": "심(마음 심) + 폐(허파 폐) + 소(살아날 소) + 생(날 생) + 술(재주 술)",
        "pronunciation": "호이 신 팀 포이",
        "meaningKo": "심장과 폐의 기능이 정지된 환자에게 가슴 압박과 인공호흡을 실시하여 혈액 순환과 호흡을 인위적으로 유지하는 응급처치술입니다. 통역 시 'CPR'이라는 약어를 사용할 때는 반드시 베트남어 풀네임을 먼저 설명해야 하며, 가슴 압박 속도(분당 100-120회)와 깊이(5-6cm) 등 구체적 수치는 양국이 동일하므로 혼동 없이 전달할 수 있습니다. 현장에서 '심폐소생술'과 '응급처치'를 혼동하지 않도록 주의해야 합니다.",
        "meaningVi": "Kỹ thuật cấp cứu được thực hiện khi tim và phổi ngừng hoạt động, bao gồm ép tim ngoài lồng ngực và thông khí nhân tạo để duy trì tuần hoàn máu và hô hấp. Viết tắt quốc tế là CPR (Cardiopulmonary Resuscitation).",
        "context": "emergency",
        "culturalNote": "한국에서는 일반인 대상 CPR 교육이 의무화되어 있어 많은 시민이 기본 술기를 알고 있으나, 베트남에서는 아직 보편화되지 않았습니다. 한국 병원에서는 'Code Blue'라는 용어를 사용하지만 베트남 병원에서는 'Cấp cứu tim phổi'라고 직접 표현합니다. 통역 시 한국의 자동심장충격기(AED) 보급률과 베트남의 차이를 설명해야 할 수 있습니다.",
        "commonMistakes": [
            {
                "mistake": "CPR을 'Phục hồi chức năng'(재활)으로 번역",
                "correction": "Hồi sinh tim phổi 또는 Cấp cứu tim phổi",
                "explanation": "재활(rehabilitation)과 소생술(resuscitation)은 완전히 다른 의료 행위입니다"
            },
            {
                "mistake": "'가슴 압박'을 'Massage tim'(심장 마사지)으로만 번역",
                "correction": "Ép tim ngoài lồng ngực",
                "explanation": "베트남 의료 표준 용어는 'ép tim'이며, 'massage'는 구어체입니다"
            },
            {
                "mistake": "응급처치(first aid)와 심폐소생술을 동일하게 번역",
                "correction": "응급처치는 Sơ cứu, 심폐소생술은 Hồi sinh tim phổi",
                "explanation": "CPR은 응급처치의 일부이지만 더 전문적이고 구체적인 술기입니다"
            }
        ],
        "examples": [
            {
                "ko": "환자의 의식이 없고 호흡이 정지되어 즉시 심폐소생술을 시작했습니다.",
                "vi": "Bệnh nhân mất ý thức và ngừng thở, chúng tôi đã bắt đầu hồi sinh tim phổi ngay lập tức.",
                "situation": "formal"
            },
            {
                "ko": "가슴 압박은 분당 100회에서 120회 속도로 실시해야 합니다.",
                "vi": "Ép tim phải thực hiện với tốc độ 100-120 lần mỗi phút.",
                "situation": "onsite"
            },
            {
                "ko": "CPR 중에는 2분마다 구조자를 교대하는 것이 좋습니다.",
                "vi": "Trong quá trình CPR, nên thay đổi người thực hiện sau mỗi 2 phút.",
                "situation": "informal"
            }
        ],
        "relatedTerms": ["자동심장충격기", "기관삽관", "응급의학", "심정지"]
    },
    {
        "slug": "may-khu-rung-tim-tu-dong",
        "korean": "자동심장충격기",
        "vietnamese": "Máy khử rung tim tự động",
        "hanja": "自動心臟衝擊機",
        "hanjaReading": "자(스스로 자) + 동(움직일 동) + 심(마음 심) + 장(오장육부 장) + 충(부딪칠 충) + 격(칠 격) + 기(기계 기)",
        "pronunciation": "마이 쿠 중 팀 뜨 동",
        "meaningKo": "심실세동이나 무맥성 심실빈맥 등 치명적인 부정맥을 자동으로 감지하고 전기충격을 가해 정상 심장 리듬을 회복시키는 의료기기입니다. 통역 시 'AED'라는 약어를 먼저 언급하되 베트남어 설명을 반드시 병기해야 하며, 한국에서는 공공장소 설치가 법적으로 의무화되어 있다는 점을 설명할 때 주의가 필요합니다. '제세동기'와 '자동심장충격기'를 구분하여 번역해야 합니다.",
        "meaningVi": "Thiết bị y tế tự động phát hiện rung thất hoặc nhịp nhanh thất không mạch và tự động phân tích nhịp tim, sau đó đưa ra điện giật để phục hồi nhịp tim bình thường. Viết tắt là AED (Automated External Defibrillator).",
        "context": "emergency",
        "culturalNote": "한국은 2012년부터 다중이용시설에 AED 설치를 의무화하여 전국 약 5만 대 이상이 보급되어 있으나, 베트남에서는 주로 대형 병원과 국제공항에만 설치되어 있습니다. 한국에서는 일반인도 사용법 교육을 받지만, 베트남에서는 의료인이 주로 사용합니다. 통역 시 'AED'를 베트남에서 'Máy sốc tim'이라고 줄여 말하는 경우가 많다는 점을 알아야 합니다.",
        "commonMistakes": [
            {
                "mistake": "AED를 'Máy điện giật'(전기충격기)로만 번역",
                "correction": "Máy khử rung tim tự động (AED)",
                "explanation": "일반 전기충격기와 자동제세동기는 기능과 용도가 다릅니다"
            },
            {
                "mistake": "'제세동기'와 'AED'를 동일하게 번역",
                "correction": "제세동기는 Máy khử rung tim (수동), AED는 Máy khử rung tim tự động",
                "explanation": "수동 제세동기는 의료진만 사용 가능하고, AED는 일반인도 사용 가능합니다"
            },
            {
                "mistake": "'심장충격기'를 'Máy sốc'로만 번역",
                "correction": "Máy khử rung tim tự động 또는 Máy sốc tim tự động",
                "explanation": "'sốc'만으로는 의미가 불명확하며, 'tim'(심장)을 반드시 포함해야 합니다"
            }
        ],
        "examples": [
            {
                "ko": "공항 대합실에 비치된 자동심장충격기를 사용하여 환자를 소생시켰습니다.",
                "vi": "Chúng tôi đã sử dụng máy khử rung tim tự động đặt tại phòng chờ sân bay để cứu sống bệnh nhân.",
                "situation": "formal"
            },
            {
                "ko": "AED는 음성 안내에 따라 일반인도 쉽게 사용할 수 있습니다.",
                "vi": "AED có thể dễ dàng sử dụng bởi người thường theo hướng dẫn bằng giọng nói.",
                "situation": "onsite"
            },
            {
                "ko": "패드를 가슴에 부착하면 기기가 자동으로 심전도를 분석합니다.",
                "vi": "Khi dán miếng dán lên ngực, thiết bị sẽ tự động phân tích điện tâm đồ.",
                "situation": "informal"
            }
        ],
        "relatedTerms": ["심폐소생술", "제세동", "심실세동", "부정맥"]
    },
    {
        "slug": "dat-noi-khi-quan",
        "korean": "기관삽관",
        "vietnamese": "Đặt nội khí quản",
        "hanja": "氣管揷管",
        "hanjaReading": "기(숨 기) + 관(대롱 관) + 삽(꽂을 삽) + 관(대롱 관)",
        "pronunciation": "닷 노이 키 꽌",
        "meaningKo": "의식이 없거나 스스로 호흡할 수 없는 환자의 기도를 확보하기 위해 입이나 코를 통해 기관 내로 특수 튜브를 삽입하는 의료 술기입니다. 통역 시 '삽관'과 '관 삽입'을 혼동하지 않도록 주의하며, 응급 상황에서 '튜브 넣기'라는 구어체 표현과 정확한 의학 용어를 구분하여 사용해야 합니다. 베트남어로는 '內氣管(nội khí quản)'이라는 한자어 기반 표현을 사용하므로 한국 통역사가 이해하기 쉽습니다.",
        "meaningVi": "Thủ thuật y tế đưa một ống nội khí quản đặc biệt qua miệng hoặc mũi vào khí quản để đảm bảo đường thở cho bệnh nhân không tự thở được hoặc mất ý thức. Đây là thủ thuật cấp cứu quan trọng trong hồi sức và gây mê.",
        "context": "emergency",
        "culturalNote": "한국과 베트남 모두 응급 상황에서 기관삽관은 의사만 시행할 수 있으나, 한국에서는 응급구조사(1급)도 특정 조건에서 시행 가능합니다. 베트남에서는 의사 외에 시행이 엄격히 제한됩니다. 통역 시 '기관절개술'과 혼동하지 않도록 주의해야 하며, 베트남 의료진은 때때로 'Đặt ống nội khí quản'이라고 더 구체적으로 표현합니다.",
        "commonMistakes": [
            {
                "mistake": "'기관삽관'을 'Đặt ống thở'(호흡관 삽입)로만 번역",
                "correction": "Đặt nội khí quản 또는 Đặt ống nội khí quản",
                "explanation": "'ống thở'는 일반적인 호흡관을 의미하며, 의학 용어로는 부정확합니다"
            },
            {
                "mistake": "'기관절개술'과 '기관삽관'을 같은 용어로 번역",
                "correction": "기관삽관은 Đặt nội khí quản, 기관절개술은 Mở khí quản",
                "explanation": "삽관은 튜브 삽입, 절개는 목을 절개하는 수술로 완전히 다른 시술입니다"
            },
            {
                "mistake": "'튜브 넣기'를 'Đưa ống vào'로 직역",
                "correction": "Đặt nội khí quản (정식 용어 사용)",
                "explanation": "의료 통역에서는 구어체보다 표준 의학 용어를 사용해야 합니다"
            }
        ],
        "examples": [
            {
                "ko": "전신마취 수술 전에 기관삽관을 시행하여 기도를 확보했습니다.",
                "vi": "Trước phẫu thuật gây mê toàn thân, chúng tôi đã thực hiện đặt nội khí quản để đảm bảo đường thở.",
                "situation": "formal"
            },
            {
                "ko": "삽관 튜브의 위치를 청진기로 확인해 주세요.",
                "vi": "Vui lòng kiểm tra vị trí ống nội khí quản bằng ống nghe.",
                "situation": "onsite"
            },
            {
                "ko": "환자 상태가 안정되면 발관을 고려할 예정입니다.",
                "vi": "Khi tình trạng bệnh nhân ổn định, chúng tôi sẽ xem xét rút ống nội khí quản.",
                "situation": "informal"
            }
        ],
        "relatedTerms": ["기관절개술", "인공호흡기", "기도확보", "전신마취"]
    },
    {
        "slug": "nhiem-trung-huyet",
        "korean": "패혈증",
        "vietnamese": "Nhiễm trùng huyết",
        "hanja": "敗血症",
        "hanjaReading": "패(망할 패) + 혈(피 혈) + 증(증세 증)",
        "pronunciation": "니엠 쭝 후옛",
        "meaningKo": "세균이나 바이러스 등의 감염으로 인해 전신에 염증 반응이 과도하게 일어나 장기 기능 장애가 발생하는 생명을 위협하는 응급 질환입니다. 통역 시 'Sepsis'라는 영어 용어를 함께 사용하면 양국 의료진이 명확히 이해하며, '패혈증'과 '혈액 감염'을 혼동하지 않도록 주의해야 합니다. 베트남에서는 '敗血症(nhiễm trùng huyết)'이라는 한자어를 그대로 사용하므로 의미 전달이 수월합니다.",
        "meaningVi": "Bệnh lý nguy hiểm đe dọa tính mạng do phản ứng viêm toàn thân quá mức trước nhiễm trùng (vi khuẩn, virus), gây ra rối loạn chức năng các cơ quan. Còn gọi là Sepsis theo thuật ngữ quốc tế.",
        "context": "emergency",
        "culturalNote": "한국과 베트남 모두 패혈증은 중환자실 치료가 필수적이나, 한국에서는 조기 패혈증 선별 도구(qSOFA)를 응급실에서 적극 사용하는 반면 베트남 일부 병원에서는 아직 보편화되지 않았습니다. 통역 시 '패혈증 쇼크'를 별도로 구분하여 설명해야 하며, 베트남 의료진은 'Nhiễm khuẩn huyết'(세균성 혈액 감염)과 혼용하는 경우가 있으므로 정확한 용어 확인이 필요합니다.",
        "commonMistakes": [
            {
                "mistake": "'패혈증'을 'Nhiễm khuẩn máu'(혈액 감염)로만 번역",
                "correction": "Nhiễm trùng huyết 또는 Nhiễm khuẩn huyết",
                "explanation": "'nhiễm trùng huyết'이 표준 의학 용어이며, 단순 혈액 감염보다 심각한 전신 반응을 의미합니다"
            },
            {
                "mistake": "'패혈증 쇼크'와 '패혈증'을 동일하게 번역",
                "correction": "패혈증은 Nhiễm trùng huyết, 패혈증 쇼크는 Sốc nhiễm trùng huyết",
                "explanation": "쇼크는 패혈증의 가장 심각한 단계로, 별도 용어가 필요합니다"
            },
            {
                "mistake": "'균혈증'과 '패혈증'을 혼동하여 번역",
                "correction": "균혈증은 Nhiễm khuẩn máu, 패혈증은 Nhiễm trùng huyết",
                "explanation": "균혈증은 혈액에 균이 있는 상태, 패혈증은 전신 염증 반응을 동반합니다"
            }
        ],
        "examples": [
            {
                "ko": "환자가 패혈증으로 중환자실에 입원하여 광범위 항생제 치료를 받고 있습니다.",
                "vi": "Bệnh nhân đang nhập viện tại ICU do nhiễm trùng huyết và đang được điều trị bằng kháng sinh phổ rộng.",
                "situation": "formal"
            },
            {
                "ko": "패혈증이 의심되면 1시간 이내에 항생제를 투여해야 합니다.",
                "vi": "Nếu nghi ngờ nhiễm trùng huyết, phải truyền kháng sinh trong vòng 1 giờ.",
                "situation": "onsite"
            },
            {
                "ko": "발열, 빈맥, 저혈압이 동반되면 패혈증을 의심해야 합니다.",
                "vi": "Nếu có sốt, nhịp tim nhanh và huyết áp thấp, cần nghi ngờ nhiễm trùng huyết.",
                "situation": "informal"
            }
        ],
        "relatedTerms": ["균혈증", "패혈증쇼크", "전신염증반응증후군", "다장기부전"]
    },
    {
        "slug": "soc-phan-ve",
        "korean": "아나필락시스",
        "vietnamese": "Sốc phản vệ",
        "hanja": None,
        "hanjaReading": None,
        "pronunciation": "쇽 판 베",
        "meaningKo": "특정 물질에 대한 심각한 알레르기 반응으로 수분 내에 호흡곤란, 혈압 저하, 의식 소실 등이 나타나는 생명을 위협하는 응급 상황입니다. 통역 시 'Anaphylaxis'라는 영어 의학 용어를 병기하는 것이 안전하며, '알레르기'와 '아나필락시스'의 심각도 차이를 명확히 구분하여 전달해야 합니다. 베트남에서는 '쇼크(sốc)'라는 표현을 사용하므로 긴급성을 강조할 수 있습니다.",
        "meaningVi": "Phản ứng dị ứng nghiêm trọng, đe dọa tính mạng xảy ra trong vòng vài phút sau khi tiếp xúc với chất gây dị ứng, biểu hiện bằng khó thở, hạ huyết áp, mất ý thức. Thuật ngữ quốc tế là Anaphylaxis.",
        "context": "emergency",
        "culturalNote": "한국에서는 식품 알레르기 표시제가 법적으로 의무화되어 있고, 에피네프린 자동주사기(에피펜)를 약국에서 구매할 수 있으나, 베트남에서는 에피펜 보급이 제한적이고 대형 병원에서만 사용 가능합니다. 통역 시 한국 환자가 '쇼크'라는 표현을 사용할 때 베트남어 'sốc'과 의미가 정확히 일치하므로 이해가 빠르지만, 일반 저혈압 쇼크와 구분이 필요합니다.",
        "commonMistakes": [
            {
                "mistake": "'아나필락시스'를 'Dị ứng nặng'(심한 알레르기)로만 번역",
                "correction": "Sốc phản vệ 또는 Phản vệ phản ứng",
                "explanation": "아나필락시스는 단순 심한 알레르기가 아니라 전신 쇼크 상태를 의미합니다"
            },
            {
                "mistake": "'과민반응'과 '아나필락시스'를 같은 용어로 번역",
                "correction": "과민반응은 Phản ứng quá mẫn, 아나필락시스는 Sốc phản vệ",
                "explanation": "과민반응은 넓은 개념이고, 아나필락시스는 가장 심각한 형태입니다"
            },
            {
                "mistake": "'쇼크'를 'Choáng'(어지러움)으로 번역",
                "correction": "Sốc (의학적 쇼크 상태)",
                "explanation": "'choáng'은 일시적 어지러움이고, 'sốc'은 생명을 위협하는 의학적 응급 상태입니다"
            }
        ],
        "examples": [
            {
                "ko": "환자가 땅콩 섭취 후 아나필락시스 쇼크가 발생하여 에피네프린을 즉시 투여했습니다.",
                "vi": "Bệnh nhân bị sốc phản vệ sau khi ăn đậu phộng, chúng tôi đã tiêm epinephrine ngay lập tức.",
                "situation": "formal"
            },
            {
                "ko": "벌에 쏘인 후 호흡곤란과 두드러기가 나타나면 아나필락시스를 의심해야 합니다.",
                "vi": "Nếu có khó thở và nổi mề đay sau khi bị ong đốt, cần nghi ngờ sốc phản vệ.",
                "situation": "onsite"
            },
            {
                "ko": "심한 알레르기 병력이 있는 환자는 에피펜을 항상 휴대해야 합니다.",
                "vi": "Bệnh nhân có tiền sử dị ứng nghiêm trọng phải luôn mang theo bút tiêm epinephrine tự động.",
                "situation": "informal"
            }
        ],
        "relatedTerms": ["알레르기", "에피네프린", "두드러기", "혈관부종"]
    },
    {
        "slug": "tran-khi-mang-phoi",
        "korean": "기흉",
        "vietnamese": "Tràn khí màng phổi",
        "hanja": "氣胸",
        "hanjaReading": "기(숨 기) + 흉(가슴 흉)",
        "pronunciation": "짠 키 망 포이",
        "meaningKo": "폐와 흉벽 사이의 늑막강에 공기가 차서 폐가 허탈되는 질환으로, 외상이나 자연 발생할 수 있습니다. 통역 시 '자연기흉'과 '외상성 기흉'을 명확히 구분하여 전달해야 하며, '긴장성 기흉'은 응급 수술이 필요한 중증 상태임을 강조해야 합니다. 베트남어로는 '막(màng, 膜)'과 '흉강(흉, lồng ngực)'이라는 해부학 용어를 정확히 사용해야 오해가 없습니다.",
        "meaningVi": "Bệnh lý có không khí tích tụ trong khoang màng phổi (giữa phổi và thành ngực), gây xẹp phổi. Có thể do chấn thương hoặc tự phát. Cần xử lý khẩn cấp nếu là tràn khí màng phổi áp lực cao.",
        "context": "emergency",
        "culturalNote": "한국에서는 키가 크고 마른 젊은 남성에게 자연기흉이 흔하다는 인식이 있으나, 베트남에서도 동일한 위험군이 존재합니다. 통역 시 '흉관 삽입술'을 설명할 때 한국에서는 '체스트 튜브'라는 영어 표현을 혼용하지만, 베트남에서는 'Đặt dẫn lưu màng phổi'라는 정식 용어를 사용합니다. 응급 상황에서 긴장성 기흉은 즉각적인 바늘 감압술이 필요함을 명확히 전달해야 합니다.",
        "commonMistakes": [
            {
                "mistake": "'기흉'을 'Khí trong phổi'(폐 속의 공기)로 번역",
                "correction": "Tràn khí màng phổi",
                "explanation": "기흉은 폐 '안'이 아니라 폐와 흉벽 '사이'에 공기가 차는 것입니다"
            },
            {
                "mistake": "'자연기흉'과 '외상성 기흉'을 구분하지 않고 번역",
                "correction": "자연기흉은 Tràn khí màng phổi tự phát, 외상성은 Tràn khí màng phổi do chấn thương",
                "explanation": "원인에 따라 치료와 예후가 다르므로 정확한 구분이 필요합니다"
            },
            {
                "mistake": "'긴장성 기흉'을 'Tràn khí căng'으로만 번역",
                "correction": "Tràn khí màng phổi áp lực cao 또는 Tràn khí màng phổi căng",
                "explanation": "'màng phổi'(늑막)를 명시해야 정확한 의학 용어입니다"
            }
        ],
        "examples": [
            {
                "ko": "흉부 X-ray에서 우측 기흉이 확인되어 흉관 삽입술을 시행했습니다.",
                "vi": "X-quang ngực cho thấy tràn khí màng phổi bên phải, chúng tôi đã thực hiện đặt dẫn lưu màng phổi.",
                "situation": "formal"
            },
            {
                "ko": "갑자기 가슴 통증과 호흡곤란이 생기면 기흉을 의심해야 합니다.",
                "vi": "Nếu đột ngột đau ngực và khó thở, cần nghi ngờ tràn khí màng phổi.",
                "situation": "onsite"
            },
            {
                "ko": "긴장성 기흉은 즉시 바늘 감압술이 필요한 응급 상황입니다.",
                "vi": "Tràn khí màng phổi áp lực cao là tình trạng cấp cứu cần giảm áp bằng kim ngay lập tức.",
                "situation": "informal"
            }
        ],
        "relatedTerms": ["흉관삽입술", "늑막강", "혈기흉", "종격동"]
    },
    {
        "slug": "thuyen-tac-phoi",
        "korean": "폐색전증",
        "vietnamese": "Thuyên tắc phổi",
        "hanja": "肺塞栓症",
        "hanjaReading": "폐(허파 폐) + 색(막힐 색) + 전(마개 전) + 증(증세 증)",
        "pronunciation": "투옌 턱 포이",
        "meaningKo": "혈전이나 이물질이 폐동맥을 막아서 폐로 가는 혈류가 차단되어 호흡곤란, 흉통, 쇼크 등이 발생하는 생명을 위협하는 응급 질환입니다. 통역 시 'PE(Pulmonary Embolism)'이라는 약어를 사용하면 양국 의료진이 빠르게 이해하며, '심부정맥혈전증'과의 연관성을 설명할 때 주의가 필요합니다. 베트남어로는 '栓(tắc, 막힘)'이라는 한자어를 사용하므로 의미 전달이 명확합니다.",
        "meaningVi": "Bệnh lý nguy hiểm do cục máu đông hoặc dị vật tắc động mạch phổi, ngăn chặn lưu lượng máu đến phổi, gây khó thở, đau ngực và sốc. Viết tắt quốc tế là PE (Pulmonary Embolism).",
        "context": "emergency",
        "culturalNote": "한국과 베트남 모두 장시간 비행이나 수술 후 폐색전증 위험이 높아지므로 예방적 항응고제 사용을 권장하지만, 베트남에서는 항응고제 모니터링 시스템이 한국만큼 체계적이지 않습니다. 통역 시 'D-dimer 검사'나 'CT 폐동맥조영술' 등의 진단 용어를 정확히 전달해야 하며, 베트남 의료진은 'Tắc mạch phổi'라는 줄임 표현을 사용하기도 합니다.",
        "commonMistakes": [
            {
                "mistake": "'폐색전증'을 'Tắc phổi'(폐 막힘)로만 번역",
                "correction": "Thuyên tắc phổi 또는 Tắc mạch phổi",
                "explanation": "'thuyên tắc'은 혈전에 의한 막힘을 의미하는 정확한 의학 용어입니다"
            },
            {
                "mistake": "'폐동맥색전증'과 '폐색전증'을 다르게 번역",
                "correction": "동일하게 Thuyên tắc phổi 또는 Thuyên tắc động mạch phổi",
                "explanation": "두 용어는 같은 질환을 의미하며, 후자가 더 정확한 표현입니다"
            },
            {
                "mistake": "'심부정맥혈전증'과 '폐색전증'을 혼동하여 번역",
                "correction": "심부정맥혈전증은 Huyết khối tĩnh mạch sâu, 폐색전증은 Thuyên tắc phổi",
                "explanation": "전자는 다리 정맥의 혈전, 후자는 폐동맥 막힘으로 연관되지만 다른 질환입니다"
            }
        ],
        "examples": [
            {
                "ko": "CT 폐동맥조영술에서 우측 폐동맥에 혈전이 발견되어 항응고제 치료를 시작했습니다.",
                "vi": "CT mạch máu phổi cho thấy huyết khối ở động mạch phổi bên phải, chúng tôi đã bắt đầu điều trị chống đông máu.",
                "situation": "formal"
            },
            {
                "ko": "장시간 비행 후 갑작스런 호흡곤란이 생기면 폐색전증을 의심해야 합니다.",
                "vi": "Nếu có khó thở đột ngột sau chuyến bay dài, cần nghi ngờ thuyên tắc phổi.",
                "situation": "onsite"
            },
            {
                "ko": "수술 후 조기 보행은 폐색전증 예방에 중요합니다.",
                "vi": "Đi lại sớm sau phẫu thuật rất quan trọng để phòng ngừa thuyên tắc phổi.",
                "situation": "informal"
            }
        ],
        "relatedTerms": ["심부정맥혈전증", "항응고제", "D-dimer", "폐동맥고혈압"]
    },
    {
        "slug": "nhoi-mau-co-tim",
        "korean": "심근경색",
        "vietnamese": "Nhồi máu cơ tim",
        "hanja": "心筋梗塞",
        "hanjaReading": "심(마음 심) + 근(힘줄 근) + 경(막힐 경) + 색(막힐 색)",
        "pronunciation": "노이 마우 꺼 팀",
        "meaningKo": "관상동맥이 막혀서 심장 근육으로 가는 혈류가 차단되어 심장 조직이 괴사하는 응급 질환으로, 흉통과 호흡곤란이 주요 증상입니다. 통역 시 'MI(Myocardial Infarction)' 또는 '심장마비'라는 표현과 구분하여 사용해야 하며, 'STEMI'와 'NSTEMI'를 정확히 구분하여 전달하는 것이 중요합니다. 베트nam어로는 '梗塞(nhồi máu, 혈액이 차서 막힘)'이라는 한자어를 사용합니다.",
        "meaningVi": "Bệnh cấp cứu do động mạch vành bị tắc, ngăn chặn lưu lượng máu đến cơ tim, gây hoại tử mô tim. Triệu chứng chính là đau ngực và khó thở. Viết tắt quốc tế là AMI (Acute Myocardial Infarction) hoặc MI.",
        "context": "emergency",
        "culturalNote": "한국에서는 '골든타임 90분' 개념이 널리 알려져 있어 환자들이 증상 발생 시 빠르게 병원을 찾지만, 베트남에서는 아직 인식이 부족한 편입니다. 통역 시 '심장마비'라는 일반인 용어와 '심근경색'이라는 의학 용어를 구분하여 사용해야 하며, 베트남 의료진은 'Nhồi máu cơ tim cấp'(급성 심근경색)이라고 더 구체적으로 표현합니다. 한국에서는 응급실 도착 즉시 심전도와 혈액검사를 시행하는 것이 표준 프로토콜입니다.",
        "commonMistakes": [
            {
                "mistake": "'심근경색'을 'Đột quỵ tim'(심장 뇌졸중)으로 번역",
                "correction": "Nhồi máu cơ tim",
                "explanation": "'đột quỵ'는 뇌졸중을 의미하며, 심장에는 'nhồi máu'를 사용합니다"
            },
            {
                "mistake": "'심장마비'와 '심근경색'을 동일하게 번역",
                "correction": "심장마비는 Ngừng tim, 심근경색은 Nhồi máu cơ tim",
                "explanation": "심장마비는 심장이 멈춘 상태, 심근경색은 혈류 차단으로 조직이 죽는 상태입니다"
            },
            {
                "mistake": "'협심증'과 '심근경색'을 혼동하여 번역",
                "correction": "협심증은 Đau thắt ngực, 심근경색은 Nhồi máu cơ tim",
                "explanation": "협심증은 일시적 허혈, 심근경색은 조직 괴사로 심각도가 다릅니다"
            }
        ],
        "examples": [
            {
                "ko": "환자가 급성 심근경색으로 응급실에 내원하여 즉시 관상동맥조영술을 시행했습니다.",
                "vi": "Bệnh nhân đến khoa cấp cứu do nhồi máu cơ tim cấp, chúng tôi đã thực hiện chụp mạch vành ngay lập tức.",
                "situation": "formal"
            },
            {
                "ko": "가슴 중앙에 짓누르는 듯한 통증이 20분 이상 지속되면 심근경색을 의심해야 합니다.",
                "vi": "Nếu đau ngực như bị đè nặng kéo dài trên 20 phút, cần nghi ngờ nhồi máu cơ tim.",
                "situation": "onsite"
            },
            {
                "ko": "트로포닌 수치가 상승하여 심근경색 진단이 확정되었습니다.",
                "vi": "Chỉ số troponin tăng cao, xác định chẩn đoán nhồi máu cơ tim.",
                "situation": "informal"
            }
        ],
        "relatedTerms": ["협심증", "관상동맥질환", "관상동맥조영술", "스텐트삽입술"]
    },
    {
        "slug": "loan-nhip-tim",
        "korean": "부정맥",
        "vietnamese": "Loạn nhịp tim",
        "hanja": "不整脈",
        "hanjaReading": "부(아닐 부) + 정(가지런할 정) + 맥(맥박 맥)",
        "pronunciation": "로안 닙 팀",
        "meaningKo": "심장의 전기적 신호 이상으로 인해 심박동이 불규칙하거나 지나치게 빠르거나 느려지는 질환의 총칭입니다. 통역 시 '빈맥', '서맥', '심방세동' 등 구체적 유형을 정확히 구분하여 전달해야 하며, 일부 부정맥은 생명을 위협하지만 일부는 양성임을 설명할 때 주의가 필요합니다. 베트남어로는 '亂(loạn, 어지러울 란)'이라는 한자어를 사용하여 의미가 명확합니다.",
        "meaningVi": "Nhóm bệnh lý do rối loạn tín hiệu điện của tim, khiến nhịp tim không đều, quá nhanh hoặc quá chậm. Bao gồm nhiều loại như rung nhĩ, nhịp nhanh thất, nhịp chậm xoang, v.v.",
        "context": "cardiology",
        "culturalNote": "한국에서는 심방세동 환자의 뇌졸중 예방을 위한 항응고제 치료가 적극적으로 시행되지만, 베트남에서는 항응고제 모니터링 인프라가 제한적입니다. 통역 시 '두근거림(palpitation)'이라는 증상과 '부정맥'이라는 진단명을 구분해야 하며, 베트남 환자들은 'Tim đập nhanh'(심장이 빨리 뛴다)라는 표현을 자주 사용합니다. 홀터 모니터링이나 전기생리학적 검사 등의 진단 방법도 정확히 전달해야 합니다.",
        "commonMistakes": [
            {
                "mistake": "'부정맥'을 'Tim đập không đều'(심장이 불규칙하게 뛴다)로만 번역",
                "correction": "Loạn nhịp tim",
                "explanation": "'loạn nhịp tim'이 표준 의학 용어이며, 구어체는 환자 설명 시에만 사용합니다"
            },
            {
                "mistake": "'빈맥'과 '서맥'을 'Loạn nhịp tim'으로 통칭하여 번역",
                "correction": "빈맥은 Nhịp nhanh, 서맥은 Nhịp chậm",
                "explanation": "부정맥의 세부 유형을 구분하여 번역해야 정확한 진단과 치료가 가능합니다"
            },
            {
                "mistake": "'심방세동'을 'Rung tim'(심장 떨림)으로만 번역",
                "correction": "Rung nhĩ (심방세동)",
                "explanation": "'rung tim'은 모호하며, 'rung nhĩ'가 심방세동의 정확한 용어입니다"
            }
        ],
        "examples": [
            {
                "ko": "심전도 검사에서 심방세동이 확인되어 항응고제 치료를 시작했습니다.",
                "vi": "Điện tâm đồ cho thấy rung nhĩ, chúng tôi đã bắt đầu điều trị chống đông máu.",
                "situation": "formal"
            },
            {
                "ko": "가슴이 두근거리고 어지러움이 있으면 부정맥을 의심하고 검사를 받아야 합니다.",
                "vi": "Nếu có hồi hộp và chóng mặt, cần nghi ngờ loạn nhịp tim và đi khám.",
                "situation": "onsite"
            },
            {
                "ko": "24시간 홀터 모니터링으로 간헐적 부정맥을 진단할 수 있습니다.",
                "vi": "Holter 24 giờ có thể chẩn đoán loạn nhịp tim từng đợt.",
                "situation": "informal"
            }
        ],
        "relatedTerms": ["심방세동", "심실빈맥", "동성서맥", "심전도"]
    },
    {
        "slug": "suy-tim",
        "korean": "심부전",
        "vietnamese": "Suy tim",
        "hanja": "心不全",
        "hanjaReading": "심(마음 심) + 부(아닐 부) + 전(온전할 전)",
        "pronunciation": "쑤이 팀",
        "meaningKo": "심장이 몸에 필요한 만큼의 혈액을 충분히 펌프질하지 못하는 상태로, 호흡곤란, 부종, 피로 등이 주요 증상입니다. 통역 시 '급성 심부전'과 '만성 심부전'을 구분하여 전달해야 하며, '좌심부전'과 '우심부전'의 증상 차이를 정확히 설명하는 것이 중요합니다. 베트남어로는 '衰(suy, 쇠할 쇠)'라는 한자어를 사용하여 심장 기능 저하를 명확히 표현합니다.",
        "meaningVi": "Tình trạng tim không bơm đủ lượng máu cần thiết cho cơ thể, gây khó thở, phù nề và mệt mỏi. Có thể cấp tính hoặc mạn tính, chia thành suy tim trái và suy tim phải theo vị trí tổn thương.",
        "context": "cardiology",
        "culturalNote": "한국에서는 심부전 환자에게 염분 제한(하루 5g 이하)을 엄격히 권고하지만, 베트남 음식 문화에서는 염분 조절이 어려워 환자 교육 시 문화적 차이를 고려해야 합니다. 통역 시 'NYHA 분류'(뉴욕심장협회 기능 분류)를 설명할 때 I-IV등급을 정확히 전달해야 하며, 베트남 의료진은 'Suy tim sung혈'(울혈성 심부전)이라는 표현을 자주 사용합니다.",
        "commonMistakes": [
            {
                "mistake": "'심부전'을 'Tim yếu'(약한 심장)로 번역",
                "correction": "Suy tim",
                "explanation": "'tim yếu'는 구어체이며, 의학 용어는 'suy tim'입니다"
            },
            {
                "mistake": "'울혈성 심부전'과 '심부전'을 다르게 번역",
                "correction": "둘 다 Suy tim 또는 Suy tim sung huyết (울혈성)",
                "explanation": "울혈성 심부전은 심부전의 가장 흔한 형태로, 'sung huyết'을 추가하면 더 정확합니다"
            },
            {
                "mistake": "'좌심부전'과 '우심부전'을 구분하지 않고 번역",
                "correction": "좌심부전은 Suy tim trái, 우심부전은 Suy tim phải",
                "explanation": "증상과 치료가 다르므로 좌우를 반드시 구분해야 합니다"
            }
        ],
        "examples": [
            {
                "ko": "환자는 NYHA III등급의 만성 심부전으로 이뇨제와 ACE 억제제로 치료 중입니다.",
                "vi": "Bệnh nhân bị suy tim mạn NYHA độ III, đang điều trị bằng thuốc lợi tiểu và thuốc ức chế ACE.",
                "situation": "formal"
            },
            {
                "ko": "누워 있을 때보다 앉아 있을 때 숨쉬기가 편하면 좌심부전을 의심해야 합니다.",
                "vi": "Nếu thở dễ hơn khi ngồi so với khi nằm, cần nghi ngờ suy tim trái.",
                "situation": "onsite"
            },
            {
                "ko": "다리 부종과 체중 증가는 우심부전의 흔한 증상입니다.",
                "vi": "Phù chân và tăng cân là triệu chứng phổ biến của suy tim phải.",
                "situation": "informal"
            }
        ],
        "relatedTerms": ["울혈성심부전", "박출률", "이뇨제", "NYHA분류"]
    },
    {
        "slug": "boc-tach-dong-mach-chu",
        "korean": "대동맥박리",
        "vietnamese": "Bóc tách động mạch chủ",
        "hanja": "大動脈剝離",
        "hanjaReading": "대(큰 대) + 동(움직일 동) + 맥(맥박 맥) + 박(벗길 박) + 리(떠날 리)",
        "pronunciation": "복 딱 동 맥 쭈",
        "meaningKo": "대동맥 내막이 찢어져서 혈관벽 사이로 혈액이 흘러 들어가 대동맥이 이중으로 갈라지는 응급 질환으로, 극심한 흉통과 함께 생명을 위협합니다. 통역 시 'Stanford A형'과 'B형'을 정확히 구분하여 전달해야 하며, 즉각적인 수술이 필요한 응급 상황임을 강조해야 합니다. 베트남어로는 '剝(bóc, 벗길 박)'과 '離(tách, 떨어질 리)'라는 한자어를 사용하여 혈관벽이 벗겨져 분리되는 상태를 명확히 표현합니다.",
        "meaningVi": "Bệnh cấp cứu do lớp trong của động mạch chủ bị rách, máu chảy vào giữa các lớp thành mạch khiến động mạch chủ bị tách thành hai lớp. Gây đau ngực dữ dội và đe dọa tính mạng, thường cần phẫu thuật khẩn cấp.",
        "context": "emergency",
        "culturalNote": "한국과 베트남 모두 대동맥박리는 매우 드물지만 치명적인 질환으로 인식되며, 한국에서는 고혈압 관리가 잘 되는 편이지만 베트남에서는 고혈압 인지율과 치료율이 낮아 위험이 더 높습니다. 통역 시 '찢어지는 듯한 흉통'이라는 특징적 증상을 정확히 전달해야 하며, Stanford 분류법(A형은 상행대동맥 침범, B형은 하행대동맥만 침범)을 설명할 때 주의가 필요합니다.",
        "commonMistakes": [
            {
                "mistake": "'대동맥박리'를 'Vỡ động mạch chủ'(대동맥 파열)로 번역",
                "correction": "Bóc tách động mạch chủ",
                "explanation": "박리는 혈관벽이 찢어져 분리되는 것이고, 파열은 완전히 터지는 것으로 다릅니다"
            },
            {
                "mistake": "'대동맥류'와 '대동맥박리'를 같은 용어로 번역",
                "correction": "대동맥류는 Phình động mạch chủ, 대동맥박리는 Bóc tách động mạch chủ",
                "explanation": "대동맥류는 혈관이 부풀어 오르는 것, 박리는 혈관벽이 찢어지는 것입니다"
            },
            {
                "mistake": "'Stanford A형'을 단순히 'Loại A'로만 번역",
                "correction": "Bóc tách động mạch chủ Stanford type A (침범 부위 설명 추가)",
                "explanation": "A형과 B형의 차이(상행 vs 하행)를 명확히 설명해야 합니다"
            }
        ],
        "examples": [
            {
                "ko": "환자가 갑작스런 찢어지는 듯한 흉통을 호소하여 CT 촬영 후 Stanford A형 대동맥박리가 확인되어 응급 수술을 시행했습니다.",
                "vi": "Bệnh nhân than đau ngực dữ dội như bị xé, sau chụp CT xác định bóc tách động mạch chủ Stanford type A, chúng tôi đã thực hiện phẫu thuật cấp cứu.",
                "situation": "formal"
            },
            {
                "ko": "등으로 퍼지는 극심한 가슴 통증이 있으면 대동맥박리를 의심해야 합니다.",
                "vi": "Nếu đau ngực dữ dội lan ra lưng, cần nghi ngờ bóc tách động mạch chủ.",
                "situation": "onsite"
            },
            {
                "ko": "고혈압 환자는 대동맥박리의 고위험군이므로 혈압 관리가 중요합니다.",
                "vi": "Bệnh nhân tăng huyết áp có nguy cơ cao bị bóc tách động mạch chủ, cần kiểm soát huyết áp tốt.",
                "situation": "informal"
            }
        ],
        "relatedTerms": ["대동맥류", "고혈압", "마르판증후군", "흉부CT"]
    },
    {
        "slug": "phau-thuat-bac-cau-mach-vanh",
        "korean": "관상동맥우회술",
        "vietnamese": "Phẫu thuật bắc cầu mạch vành",
        "hanja": "冠狀動脈迂回術",
        "hanjaReading": "관(갓 관) + 상(모양 상) + 동(움직일 동) + 맥(맥박 맥) + 우(멀 우) + 회(돌 회) + 술(재주 술)",
        "pronunciation": "퍼우 투엇 박 꺼우 맥 번",
        "meaningKo": "막히거나 좁아진 관상동맥을 우회하여 다른 혈관(주로 내흉동맥이나 복재정맥)을 이용해 심장 근육으로 가는 혈류를 회복시키는 개심 수술입니다. 통역 시 'CABG(Coronary Artery Bypass Grafting)'이라는 약어를 사용하면 양국 의료진이 빠르게 이해하며, '스텐트삽입술'과의 차이점을 명확히 설명해야 합니다. 베트남어로는 '架橋(bắc cầu, 다리 놓기)'라는 한자어를 사용하여 우회로를 만든다는 의미를 직관적으로 전달합니다.",
        "meaningVi": "Phẫu thuật tim hở sử dụng mạch máu khác (thường là động mạch ngực trong hoặc tĩnh mạch hiển) để tạo đường vòng qua đoạn động mạch vành bị tắc hoặc hẹp, khôi phục lưu lượng máu đến cơ tim. Viết tắt quốc tế là CABG.",
        "context": "surgery",
        "culturalNote": "한국에서는 CABG가 보험 적용되며 수술 후 재활 프로그램이 체계적이지만, 베트남에서는 수술 비용이 높고 재활 인프라가 제한적입니다. 통역 시 '인공심폐기 사용 여부(on-pump vs off-pump)'를 구분하여 설명해야 하며, 베트남 환자들은 개심 수술에 대한 두려움이 커서 스텐트 시술을 선호하는 경향이 있습니다. '다중혈관 질환'이 있을 때 CABG가 스텐트보다 우수하다는 점을 설명할 때 주의가 필요합니다.",
        "commonMistakes": [
            {
                "mistake": "'관상동맥우회술'을 'Phẫu thuật tim'(심장 수술)로만 번역",
                "correction": "Phẫu thuật bắc cầu mạch vành (CABG)",
                "explanation": "심장 수술은 광범위한 용어이고, CABG는 특정 수술법입니다"
            },
            {
                "mistake": "'스텐트삽입술'과 '관상동맥우회술'을 혼동하여 번역",
                "correction": "스텐트는 Đặt stent, 우회술은 Phẫu thuật bắc cầu mạch vành",
                "explanation": "스텐트는 비수술적 시술, 우회술은 개심 수술로 완전히 다릅니다"
            },
            {
                "mistake": "'이식 혈관'을 'Mạch ghép'으로만 번역",
                "correction": "Mạch máu ghép bắc cầu 또는 Mạch dùng làm cầu nối",
                "explanation": "'bắc cầu'(우회로 만들기)라는 목적을 명시해야 정확합니다"
            }
        ],
        "examples": [
            {
                "ko": "환자의 3개 관상동맥이 모두 심하게 좁아져 있어 삼중 관상동맥우회술을 시행했습니다.",
                "vi": "Ba động mạch vành của bệnh nhân đều hẹp nặng, chúng tôi đã thực hiện phẫu thuật bắc cầu mạch vành ba nhánh.",
                "situation": "formal"
            },
            {
                "ko": "내흉동맥을 이용한 우회술은 복재정맥보다 장기 개통률이 우수합니다.",
                "vi": "Phẫu thuật bắc cầu sử dụng động mạch ngực trong có tỷ lệ thông tốt dài hạn cao hơn tĩnh mạch hiển.",
                "situation": "onsite"
            },
            {
                "ko": "인공심폐기를 사용하지 않는 오프펌프 수술도 가능합니다.",
                "vi": "Có thể thực hiện phẫu thuật off-pump không sử dụng máy tuần hoàn ngoài cơ thể.",
                "situation": "informal"
            }
        ],
        "relatedTerms": ["관상동맥질환", "스텐트삽입술", "인공심폐기", "내흉동맥"]
    },
    {
        "slug": "dat-stent",
        "korean": "스텐트삽입술",
        "vietnamese": "Đặt stent",
        "hanja": None,
        "hanjaReading": None,
        "pronunciation": "닷 스텐트",
        "meaningKo": "좁아지거나 막힌 혈관 안에 그물망 형태의 금속 튜브(스텐트)를 삽입하여 혈관을 넓히고 혈류를 회복시키는 비수술적 시술입니다. 통역 시 '관상동맥 스텐트'와 '뇌혈관 스텐트' 등 부위를 명확히 구분하여 전달해야 하며, '약물방출 스텐트'와 '일반 금속 스텐트'의 차이를 설명할 때 주의가 필요합니다. 베트남어로는 'stent'를 외래어 그대로 사용하므로 이해가 쉽습니다.",
        "meaningVi": "Thủ thuật nội mạch (không phẫu thuật) đặt một ống lưới kim loại (stent) vào trong mạch máu bị hẹp hoặc tắc để nong rộng mạch máu và khôi phục lưu lượng máu. Thường áp dụng cho động mạch vành, mạch não, mạch thận, v.v.",
        "context": "intervention",
        "culturalNote": "한국에서는 약물방출 스텐트가 보험 적용되어 널리 사용되지만, 베트남에서는 비용 부담으로 일반 금속 스텐트를 사용하는 경우가 많습니다. 통역 시 스텐트 시술 후 항혈소판제(아스피린, 클로피도그렐) 복용이 필수적임을 강조해야 하며, 베트남 환자들은 'Nong mạch và đặt stent'(혈관 확장 및 스텐트 삽입)라고 표현하는 경우가 많습니다. 재협착률과 스텐트 혈전증 위험도 설명해야 합니다.",
        "commonMistakes": [
            {
                "mistake": "'스텐트'를 'Ống kim loại'(금속 튜브)로만 번역",
                "correction": "Stent (외래어 그대로) 또는 Giá đỡ mạch máu",
                "explanation": "'stent'는 국제 표준 용어이며, 베트남에서도 그대로 사용합니다"
            },
            {
                "mistake": "'풍선확장술'과 '스텐트삽입술'을 같은 용어로 번역",
                "correction": "풍선확장술은 Nong mạch bằng bóng, 스텐트는 Đặt stent",
                "explanation": "풍선확장만 하는 경우와 스텐트를 삽입하는 경우는 다릅니다"
            },
            {
                "mistake": "'약물방출 스텐트'를 'Stent có thuốc'로만 번역",
                "correction": "Stent phủ thuốc 또는 Stent bào thuốc (Drug-Eluting Stent, DES)",
                "explanation": "'phủ thuốc'(약물 코팅)이 더 정확한 의학 용어입니다"
            }
        ],
        "examples": [
            {
                "ko": "관상동맥조영술에서 좌전하행지 근위부에 90% 협착이 확인되어 약물방출 스텐트를 삽입했습니다.",
                "vi": "Chụp mạch vành cho thấy hẹp 90% đoạn gần nhánh liên thất trước, chúng tôi đã đặt stent phủ thuốc.",
                "situation": "formal"
            },
            {
                "ko": "스텐트 시술 후 최소 1년간은 항혈소판제 2제 병용요법이 필요합니다.",
                "vi": "Sau đặt stent, cần dùng kết hợp 2 thuốc chống kết tập tiểu cầu ít nhất 1 năm.",
                "situation": "onsite"
            },
            {
                "ko": "스텐트 내 재협착이 발생하면 풍선확장술이나 추가 스텐트 삽입을 고려합니다.",
                "vi": "Nếu tái hẹp trong stent, cần xem xét nong bóng hoặc đặt stent bổ sung.",
                "situation": "informal"
            }
        ],
        "relatedTerms": ["관상동맥조영술", "풍선혈관성형술", "항혈소판제", "재협착"]
    },
    {
        "slug": "benh-phoi-tac-nghen-man-tinh",
        "korean": "만성폐쇄성폐질환",
        "vietnamese": "Bệnh phổi tắc nghẽn mạn tính",
        "hanja": "慢性閉塞性肺疾患",
        "hanjaReading": "만(더딜 만) + 성(이룰 성) + 폐(닫을 폐) + 색(막힐 색) + 성(성품 성) + 폐(허파 폐) + 질(병 질) + 환(걱정 환)",
        "pronunciation": "벵 포이 턱 넹 만 틴",
        "meaningKo": "주로 흡연으로 인해 기도와 폐포가 손상되어 호흡곤란이 점차 악화되는 만성 질환으로, 만성 기관지염과 폐기종을 포함합니다. 통역 시 'COPD(Chronic Obstructive Pulmonary Disease)'라는 약어를 사용하면 양국 의료진이 빠르게 이해하며, '천식'과 구분하여 전달하는 것이 중요합니다. 베트남어로는 '阻塞(tắc nghẽn, 막힘)'이라는 한자어를 사용하여 기도 폐쇄를 명확히 표현합니다.",
        "meaningVi": "Bệnh phổi mạn tính do hút thuốc lá gây tổn thương đường thở và phế nang, khiến khó thở ngày càng nặng. Bao gồm viêm phế quản mạn và khí phế thũng. Viết tắt quốc tế là COPD.",
        "context": "pulmonology",
        "culturalNote": "한국에서는 COPD 조기 진단을 위해 폐기능 검사를 적극 권장하지만, 베트남에서는 검사 접근성이 제한적이고 흡연율이 높아(남성 45% 이상) 유병률이 높습니다. 통역 시 '급성 악화'를 설명할 때 항생제와 스테로이드 치료가 필요함을 강조해야 하며, 베트남 환자들은 'Bệnh phổi tắc nghẽn'을 줄여서 'COPD'라고 부르는 경우가 많습니다. 산소치료와 폐재활의 중요성도 전달해야 합니다.",
        "commonMistakes": [
            {
                "mistake": "'만성폐쇄성폐질환'을 'Bệnh phổi mạn'(만성 폐질환)으로만 번역",
                "correction": "Bệnh phổi tắc nghẽn mạn tính (COPD)",
                "explanation": "'tắc nghẽn'(폐쇄성)이 핵심 특징이므로 반드시 포함해야 합니다"
            },
            {
                "mistake": "'천식'과 'COPD'를 같은 용어로 번역",
                "correction": "천식은 Hen phế quản, COPD는 Bệnh phổi tắc nghẽn mạn tính",
                "explanation": "천식은 가역적이지만 COPD는 비가역적 기도 폐쇄입니다"
            },
            {
                "mistake": "'폐기종'과 'COPD'를 혼동하여 번역",
                "correction": "폐기종은 Khí phế thũng (COPD의 한 형태), COPD는 더 광범위한 개념",
                "explanation": "폐기종은 COPD에 포함되는 병리학적 소견입니다"
            }
        ],
        "examples": [
            {
                "ko": "환자는 40갑년의 흡연력이 있으며 폐기능 검사에서 COPD가 확진되었습니다.",
                "vi": "Bệnh nhân có tiền sử hút thuốc 40 gói-năm và được chẩn đoán xác định COPD qua xét nghiệm chức năng hô hấp.",
                "situation": "formal"
            },
            {
                "ko": "계단을 오를 때 숨이 차고 기침과 가래가 지속되면 COPD를 의심해야 합니다.",
                "vi": "Nếu khó thở khi lên cầu thang, ho và có đờm kéo dài, cần nghi ngờ COPD.",
                "situation": "onsite"
            },
            {
                "ko": "급성 악화 시 항생제와 스테로이드 치료가 필요합니다.",
                "vi": "Khi đợt cấp, cần điều trị bằng kháng sinh và steroid.",
                "situation": "informal"
            }
        ],
        "relatedTerms": ["폐기종", "만성기관지염", "천식", "폐기능검사"]
    },
    {
        "slug": "lao-phoi",
        "korean": "폐결핵",
        "vietnamese": "Lao phổi",
        "hanja": "肺結核",
        "hanjaReading": "폐(허파 폐) + 결(맺을 결) + 핵(씨 핵)",
        "pronunciation": "라오 포이",
        "meaningKo": "결핵균에 감염되어 주로 폐에 염증이 생기는 만성 전염병으로, 기침, 객혈, 체중 감소 등이 주요 증상입니다. 통역 시 '활동성 결핵'과 '잠복 결핵'을 명확히 구분하여 전달해야 하며, 다제내성 결핵(MDR-TB)의 경우 치료 기간이 길고 부작용이 많다는 점을 설명해야 합니다. 베트남어로는 '癆(lao, 결핵 로)'라는 한자어를 사용하여 오래된 질병임을 나타냅니다.",
        "meaningVi": "Bệnh truyền nhiễm mạn tính do vi khuẩn lao (Mycobacterium tuberculosis) gây viêm chủ yếu ở phổi. Triệu chứng chính là ho, ho ra máu, sụt cân. Cần điều trị dài hạn bằng kháng sinh kết hợp.",
        "context": "infectiousdisease",
        "culturalNote": "한국은 결핵 퇴치 사업으로 유병률이 크게 감소했지만, 베트남은 여전히 결핵 고부담 국가로 WHO에 분류되어 있습니다. 통역 시 한국의 무료 결핵 검진 및 치료 프로그램을 설명할 때 베트남과의 차이를 고려해야 하며, 베트남 환자들은 'Bệnh lao'라고 줄여 말하는 경우가 많습니다. 6개월 표준 치료 후에도 균 음전이 안 되면 MDR-TB를 의심해야 한다는 점을 강조해야 합니다.",
        "commonMistakes": [
            {
                "mistake": "'폐결핵'을 'Bệnh phổi'(폐질환)로만 번역",
                "correction": "Lao phổi 또는 Bệnh lao phổi",
                "explanation": "'lao'는 결핵을 의미하는 고유 용어이며 반드시 포함해야 합니다"
            },
            {
                "mistake": "'활동성 결핵'과 '잠복 결핵'을 구분하지 않고 번역",
                "correction": "활동성은 Lao hoạt động, 잠복은 Lao tiềm ẩn",
                "explanation": "활동성은 전염성이 있고 치료가 필요하지만, 잠복은 증상이 없습니다"
            },
            {
                "mistake": "'다제내성 결핵'을 'Lao khó chữa'(치료 어려운 결핵)로만 번역",
                "correction": "Lao kháng thuốc đa dược (MDR-TB)",
                "explanation": "'kháng thuốc đa dược'이 다제내성을 정확히 표현하는 의학 용어입니다"
            }
        ],
        "examples": [
            {
                "ko": "환자의 객담 도말 검사에서 항산균이 검출되어 활동성 폐결핵으로 진단하고 표준 4제 요법을 시작했습니다.",
                "vi": "Xét nghiệm đờm phát hiện vi khuẩn kháng acid, chẩn đoán lao phổi hoạt động và bắt đầu phác đồ 4 thuốc tiêu chuẩn.",
                "situation": "formal"
            },
            {
                "ko": "2주 이상 기침이 지속되고 미열과 야간 발한이 있으면 결핵을 의심해야 합니다.",
                "vi": "Nếu ho kéo dài trên 2 tuần kèm sốt nhẹ và đổ mồ hôi đêm, cần nghi ngờ bệnh lao.",
                "situation": "onsite"
            },
            {
                "ko": "결핵 치료는 최소 6개월 이상 꾸준히 약을 복용해야 완치됩니다.",
                "vi": "Điều trị lao cần uống thuốc đều đặn ít nhất 6 tháng mới khỏi hoàn toàn.",
                "situation": "informal"
            }
        ],
        "relatedTerms": ["결핵균", "항산균도말검사", "다제내성결핵", "잠복결핵"]
    },
    {
        "slug": "may-tho",
        "korean": "인공호흡기",
        "vietnamese": "Máy thở",
        "hanja": "人工呼吸器",
        "hanjaReading": "인(사람 인) + 공(장인 공) + 호(부를 호) + 흡(들이마실 흡) + 기(기계 기)",
        "pronunciation": "마이 터",
        "meaningKo": "스스로 호흡할 수 없거나 호흡이 불충분한 환자에게 기계적으로 공기를 폐에 주입하여 호흡을 보조하거나 대신하는 의료 기기입니다. 통역 시 '침습적 인공호흡(기관삽관 필요)'과 '비침습적 인공호흡(마스크 사용)'을 구분하여 전달해야 하며, 인공호흡기 이탈(weaning) 과정의 중요성을 설명할 때 주의가 필요합니다. 베트남어로는 간단히 'Máy thở'(호흡 기계)라고 표현하여 이해하기 쉽습니다.",
        "meaningVi": "Thiết bị y tế hỗ trợ hoặc thay thế hô hấp cho bệnh nhân không tự thở được hoặc hô hấp không đủ, bằng cách bơm khí vào phổi một cách cơ học. Có hai loại chính: thở máy xâm lấn (cần đặt nội khí quản) và thở máy không xâm lấn (dùng mặt nạ).",
        "context": "intensive-care",
        "culturalNote": "한국 중환자실에는 고급 인공호흡기가 충분히 보급되어 있으나, 베트남 일부 병원에서는 기기 부족으로 COVID-19 팬데믹 시 문제가 발생했습니다. 통역 시 '인공호흡기 관련 폐렴(VAP)' 예방의 중요성을 강조해야 하며, 베트남 의료진은 'Thở máy xâm lấn'(침습적)과 'BiPAP/CPAP'(비침습적)을 명확히 구분합니다. 인공호흡기 설정값(PEEP, FiO2 등)을 전달할 때는 수치를 정확히 확인해야 합니다.",
        "commonMistakes": [
            {
                "mistake": "'인공호흡기'를 'Máy hỗ trợ thở'(호흡 보조 기계)로만 번역",
                "correction": "Máy thở (표준 용어) 또는 Máy thở nhân tạo",
                "explanation": "'máy thở'가 베트남 의료계에서 보편적으로 사용하는 표준 용어입니다"
            },
            {
                "mistake": "'침습적'과 '비침습적' 인공호흡을 구분하지 않고 번역",
                "correction": "침습적은 Thở máy xâm lấn, 비침습적은 Thở máy không xâm lấn (NIV)",
                "explanation": "기관삽관 유무에 따라 합병증과 관리가 다르므로 구분이 필수입니다"
            },
            {
                "mistake": "'인공호흡기 이탈'을 'Tắt máy thở'(기계 끄기)로 번역",
                "correction": "Cai máy thở (단계적 이탈 과정)",
                "explanation": "'cai'는 점진적으로 떼어내는 과정을 의미하며, 갑자기 끄는 것이 아닙니다"
            }
        ],
        "examples": [
            {
                "ko": "환자의 산소포화도가 계속 낮아져 기관삽관 후 침습적 인공호흡을 시작했습니다.",
                "vi": "Độ bão hòa oxy của bệnh nhân liên tục thấp, chúng tôi đã đặt nội khí quản và bắt đầu thở máy xâm lấn.",
                "situation": "formal"
            },
            {
                "ko": "비침습적 인공호흡으로 먼저 시도하고, 효과가 없으면 기관삽관을 고려합니다.",
                "vi": "Thử thở máy không xâm lấn trước, nếu không hiệu quả thì xem xét đặt nội khí quản.",
                "situation": "onsite"
            },
            {
                "ko": "인공호흡기 이탈 시도 전에 자발호흡시험을 실시합니다.",
                "vi": "Trước khi thử cai máy thở, thực hiện thử nghiệm hô hấp tự nhiên.",
                "situation": "informal"
            }
        ],
        "relatedTerms": ["기관삽관", "PEEP", "산소포화도", "인공호흡기관련폐렴"]
    },
    {
        "slug": "ecmo",
        "korean": "체외막산소공급",
        "vietnamese": "ECMO",
        "hanja": "體外膜酸素供給",
        "hanjaReading": "체(몸 체) + 외(바깥 외) + 막(막 막) + 산(신 산) + 소(성글 소) + 공(이바지할 공) + 급(줄 급)",
        "pronunciation": "ECMO (엑모)",
        "meaningKo": "심장이나 폐의 기능이 심각하게 저하되었을 때 몸 밖에서 혈액을 빼내어 산소를 공급하고 이산화탄소를 제거한 후 다시 체내로 되돌려 보내는 고난도 생명 유지 장치입니다. 통역 시 'VV-ECMO(정맥-정맥, 폐 기능 대체)'와 'VA-ECMO(정맥-동맥, 심폐 기능 대체)'를 구분하여 전달해야 하며, 매우 제한적인 상황에서만 사용되는 최후의 치료 수단임을 강조해야 합니다. 베트남어로는 영문 약어 'ECMO'를 그대로 사용합니다.",
        "meaningVi": "Thiết bị hỗ trợ sự sống cao cấp dùng khi tim hoặc phổi suy giảm nghiêm trọng, lấy máu ra ngoài cơ thể để cung cấp oxy và loại bỏ CO2, sau đó trả lại vào cơ thể. Có hai loại: VV-ECMO (thay thế phổi) và VA-ECMO (thay thế tim phổi).",
        "context": "intensive-care",
        "culturalNote": "한국은 ECMO 기술이 매우 발달하여 COVID-19 팬데믹 시 사망률을 낮추는 데 기여했으나, 베트남에서는 대형 병원에서만 제한적으로 사용 가능합니다. 통역 시 ECMO는 '다리(bridge)' 치료로서 회복을 기다리거나 이식을 준비하는 동안 사용된다는 점을 설명해야 하며, 베트남 환자 가족들에게는 '인공심폐기'와의 차이(수술 중 vs 중환자실 장기 사용)를 명확히 전달해야 합니다.",
        "commonMistakes": [
            {
                "mistake": "'ECMO'를 'Máy tim phổi nhân tạo'(인공심폐기)로 번역",
                "correction": "ECMO (외래어 그대로) 또는 Oxy hóa qua màng ngoài cơ thể",
                "explanation": "인공심폐기는 수술 중 사용, ECMO는 중환자실 장기 사용으로 용도가 다릅니다"
            },
            {
                "mistake": "'VV-ECMO'와 'VA-ECMO'를 구분하지 않고 번역",
                "correction": "VV-ECMO (tĩnh mạch-tĩnh mạch, hỗ trợ phổi), VA-ECMO (tĩnh mạch-động mạch, hỗ trợ tim phổi)",
                "explanation": "두 방식은 적응증과 혈류 경로가 완전히 다릅니다"
            },
            {
                "mistake": "'체외순환'과 'ECMO'를 같은 용어로 번역",
                "correction": "체외순환은 Tuần hoàn ngoài cơ thể (수술용), ECMO는 생명 유지 장치",
                "explanation": "체외순환은 개심 수술 시 일시적 사용, ECMO는 수일~수주 장기 사용입니다"
            }
        ],
        "examples": [
            {
                "ko": "환자가 중증 급성 호흡곤란 증후군으로 인공호흡기로도 산소포화도가 유지되지 않아 VV-ECMO를 적용했습니다.",
                "vi": "Bệnh nhân bị hội chứng suy hô hấp cấp nặng, thở máy không duy trì được độ bão hòa oxy nên chúng tôi đã áp dụng VV-ECMO.",
                "situation": "formal"
            },
            {
                "ko": "ECMO는 심장이나 폐가 회복될 때까지 시간을 벌어주는 치료입니다.",
                "vi": "ECMO là liệu pháp giúp mua thời gian cho đến khi tim hoặc phổi hồi phục.",
                "situation": "onsite"
            },
            {
                "ko": "심인성 쇼크로 혈압이 유지되지 않아 VA-ECMO를 시작했습니다.",
                "vi": "Do sốc tim không duy trì được huyết áp, chúng tôi đã bắt đầu VA-ECMO.",
                "situation": "informal"
            }
        ],
        "relatedTerms": ["인공호흡기", "인공심폐기", "급성호흡곤란증후군", "심인성쇼크"]
    },
    {
        "slug": "truyen-mau",
        "korean": "수혈",
        "vietnamese": "Truyền máu",
        "hanja": "輸血",
        "hanjaReading": "수(보낼 수) + 혈(피 혈)",
        "pronunciation": "쭈옌 마우",
        "meaningKo": "출혈, 빈혈, 혈액 질환 등으로 혈액이 부족한 환자에게 타인의 혈액이나 혈액 제제를 정맥을 통해 주입하는 치료입니다. 통역 시 '전혈', '농축적혈구', '혈소판', '혈장' 등 혈액 제제의 종류를 정확히 구분하여 전달해야 하며, 수혈 전 교차시험과 수혈 부작용 모니터링의 중요성을 설명해야 합니다. 베트남어로는 '輸(truyền, 보낼 수)'라는 한자어를 사용하여 혈액을 전달한다는 의미를 명확히 표현합니다.",
        "meaningVi": "Liệu pháp truyền máu hoặc chế phẩm máu của người khác vào tĩnh mạch cho bệnh nhân thiếu máu do chảy máu, thiếu máu hoặc bệnh lý máu. Cần làm xét nghiệm chéo trước khi truyền và theo dõi phản ứng phụ.",
        "context": "transfusion",
        "culturalNote": "한국과 베트남 모두 혈액원 시스템이 있으나, 베트남에서는 혈액 부족 문제가 더 심각하고 유상 헌혈(가족이 대신 헌혈)이 흔합니다. 통역 시 ABO 혈액형과 Rh 인자를 정확히 전달해야 하며, 베트남에서는 'Nhóm máu'(혈액형) 표현 시 O형을 'Nhóm O'라고 발음('zero'가 아님)하므로 주의가 필요합니다. 수혈 반응(발열, 두드러기, 용혈) 발생 시 즉시 중단해야 한다는 점을 강조해야 합니다.",
        "commonMistakes": [
            {
                "mistake": "'수혈'을 'Tiêm máu'(혈액 주사)로 번역",
                "correction": "Truyền máu",
                "explanation": "'tiêm'은 근육/피하 주사이고, 'truyền'은 정맥 주입입니다"
            },
            {
                "mistake": "'농축적혈구'를 'Máu đỏ'(적혈구)로만 번역",
                "correction": "Hồng cầu cô đặc 또는 Khối hồng cầu (Packed RBC)",
                "explanation": "'cô đặc'(농축)이라는 표현이 혈액 제제의 특성을 정확히 나타냅니다"
            },
            {
                "mistake": "'교차시험'을 'Xét nghiệm máu'(혈액검사)로만 번역",
                "correction": "Xét nghiệm chéo 또는 Phản ứng chéo (Cross-matching)",
                "explanation": "수혈 전 공여자-수혈자 혈액 적합성을 확인하는 특수 검사입니다"
            }
        ],
        "examples": [
            {
                "ko": "환자의 혈색소가 7g/dL로 저하되어 농축적혈구 2단위를 수혈했습니다.",
                "vi": "Hemoglobin của bệnh nhân giảm xuống 7g/dL, chúng tôi đã truyền 2 đơn vị khối hồng cầu.",
                "situation": "formal"
            },
            {
                "ko": "수혈 시작 후 15분간은 이상 반응이 없는지 집중 관찰해야 합니다.",
                "vi": "Trong 15 phút đầu truyền máu, cần theo dõi chặt chẽ xem có phản ứng bất thường không.",
                "situation": "onsite"
            },
            {
                "ko": "혈소판 수치가 낮아서 혈소판 수혈이 필요합니다.",
                "vi": "Tiểu cầu thấp nên cần truyền tiểu cầu.",
                "situation": "informal"
            }
        ],
        "relatedTerms": ["혈액형", "교차시험", "농축적혈구", "수혈반응"]
    },
    {
        "slug": "chay-than-nhan-tao",
        "korean": "혈액투석",
        "vietnamese": "Chạy thận nhân tạo",
        "hanja": "血液透析",
        "hanjaReading": "혈(피 혈) + 액(진 액) + 투(통할 투) + 석(풀 석)",
        "pronunciation": "짜이 턴 년 따오",
        "meaningKo": "신장 기능이 심각하게 저하된 환자의 혈액을 체외로 빼내어 투석기(인공 신장)를 통해 노폐물과 과잉 수분을 제거한 후 다시 체내로 되돌려 보내는 신대체 요법입니다. 통역 시 '복막투석'과 구분하여 전달해야 하며, 주 3회 4시간씩 시행하는 것이 표준임을 설명할 때 주의가 필요합니다. 베트남어로는 구어적으로 'Chạy thận'(신장 돌리기)이라고 표현하여 환자들이 쉽게 이해합니다.",
        "meaningVi": "Phương pháp thay thế thận cho bệnh nhân suy thận nặng, lấy máu ra ngoài cơ thể, loại bỏ chất cặn bã và nước thừa qua máy lọc thận nhân tạo, rồi trả máu về cơ thể. Thường thực hiện 3 lần/tuần, mỗi lần 4 giờ.",
        "context": "nephrology",
        "culturalNote": "한국은 혈액투석 인프라가 잘 갖춰져 있고 건강보험 적용으로 비용 부담이 적지만, 베트남에서는 투석 비용이 높고 시설이 부족하여 환자들이 어려움을 겪습니다. 통역 시 '동정맥루(AVF)' 조성술의 중요성을 설명해야 하며, 베트남 환자들은 'Lọc máu'(혈액 여과)라는 표현도 사용합니다. 투석 전후 체중 측정과 건체중(dry weight) 개념도 정확히 전달해야 합니다.",
        "commonMistakes": [
            {
                "mistake": "'혈액투석'을 'Lọc máu'(혈액 여과)로만 번역",
                "correction": "Chạy thận nhân tạo 또는 Lọc máu bằng thận nhân tạo",
                "explanation": "'chạy thận'이 베트남에서 보편적으로 사용하는 표현입니다"
            },
            {
                "mistake": "'복막투석'과 '혈액투석'을 구분하지 않고 번역",
                "correction": "혈액투석은 Chạy thận nhân tạo, 복막투석은 Lọc màng bụng",
                "explanation": "투석 방식이 완전히 다르므로 명확한 구분이 필요합니다"
            },
            {
                "mistake": "'동정맥루'를 'Ống thông'(도관)으로 번역",
                "correction": "Cầu nối động-tĩnh mạch 또는 Shunt động-tĩnh mạch (AVF)",
                "explanation": "동정맥루는 수술로 만든 혈관 연결이고, 도관은 임시 카테터입니다"
            }
        ],
        "examples": [
            {
                "ko": "환자는 말기 신부전으로 주 3회 혈액투석을 받고 있으며, 좌측 전박부에 동정맥루가 조성되어 있습니다.",
                "vi": "Bệnh nhân bị suy thận giai đoạn cuối, đang chạy thận nhân tạo 3 lần/tuần, có cầu nối động-tĩnh mạch ở cẳng tay trái.",
                "situation": "formal"
            },
            {
                "ko": "투석 후 혈압이 떨어질 수 있으니 천천히 일어나세요.",
                "vi": "Sau khi chạy thận, huyết áp có thể giảm nên hãy đứng lên từ từ.",
                "situation": "onsite"
            },
            {
                "ko": "건체중을 유지하기 위해 투석 사이에 수분 섭취를 제한해야 합니다.",
                "vi": "Để duy trì cân nặng khô, cần hạn chế uống nước giữa các lần chạy thận.",
                "situation": "informal"
            }
        ],
        "relatedTerms": ["만성신부전", "복막투석", "동정맥루", "신이식"]
    },
    {
        "slug": "sang-icu",
        "korean": "중환자실섬망",
        "vietnamese": "Sảng ICU",
        "hanja": "重患者室譫妄",
        "hanjaReading": "중(무거울 중) + 환(걱정 환) + 자(사람 자) + 실(집 실) + 섬(헛소리할 섬) + 망(망령될 망)",
        "pronunciation": "상 ICU",
        "meaningKo": "중환자실에 입원한 환자가 급성으로 의식 혼란, 주의력 저하, 지남력 장애 등을 보이는 정신 상태 변화로, 인공호흡기 사용, 진정제, 수면 박탈 등이 주요 원인입니다. 통역 시 '과활동형 섬망'과 '저활동형 섬망'을 구분하여 전달해야 하며, 섬망 예방을 위한 비약물적 중재(조기 활동, 수면 촉진 등)의 중요성을 설명해야 합니다. 베트남어로는 '譫妄(sảng, 헛소리할 섬)'이라는 한자어를 사용합니다.",
        "meaningVi": "Rối loạn tâm thần cấp tính ở bệnh nhân nằm ICU, biểu hiện bằng lú lẫn, giảm tập trung, mất định hướng. Nguyên nhân chính là dùng máy thở, thuốc an thần, thiếu ngủ. Có hai dạng: sảng tăng động và sảng giảm động.",
        "context": "intensive-care",
        "culturalNote": "한국과 베트남 모두 중환자실 섬망이 흔하지만, 한국에서는 섬망 선별 도구(CAM-ICU)를 적극 사용하여 조기 발견하는 반면 베트남에서는 아직 체계적 평가가 부족합니다. 통역 시 '섬망'과 '치매'를 혼동하지 않도록 주의해야 하며(섬망은 급성이고 가역적, 치매는 만성이고 비가역적), 베트남 가족들에게는 섬망이 일시적이며 회복 가능하다는 점을 안심시켜야 합니다.",
        "commonMistakes": [
            {
                "mistake": "'섬망'을 'Mê sảng'(혼미)로만 번역",
                "correction": "Sảng (delirium) 또는 Rối loạn ý thức cấp",
                "explanation": "'mê sảng'은 의식 수준 저하를 의미하지만, 섬망은 의식 변동을 포함한 더 광범위한 개념입니다"
            },
            {
                "mistake": "'치매'와 '섬망'을 같은 용어로 번역",
                "correction": "치매는 Sa sút trí tuệ (만성), 섬망은 Sảng (급성)",
                "explanation": "치매는 만성 인지 저하, 섬망은 급성 의식 변화로 완전히 다릅니다"
            },
            {
                "mistake": "'과활동형 섬망'을 'Sảng mạnh'(강한 섬망)으로 번역",
                "correction": "Sảng tăng động (과활동형) vs Sảng giảm động (저활동형)",
                "explanation": "섬망의 활동 수준에 따른 정확한 분류가 필요합니다"
            }
        ],
        "examples": [
            {
                "ko": "환자가 중환자실 입원 3일째부터 초조, 환각, 지남력 장애를 보여 CAM-ICU로 섬망을 진단하고 비약물적 중재를 시작했습니다.",
                "vi": "Từ ngày thứ 3 nằm ICU, bệnh nhân có biểu hiện kích động, ảo giác, mất định hướng, chẩn đoán sảng bằng CAM-ICU và bắt đầu can thiệp không dùng thuốc.",
                "situation": "formal"
            },
            {
                "ko": "섬망 예방을 위해 낮에는 활동을 촉진하고 밤에는 조명을 줄여 수면을 돕습니다.",
                "vi": "Để phòng sảng, ban ngày khuyến khích hoạt động, ban đêm giảm đèn để giúp ngủ.",
                "situation": "onsite"
            },
            {
                "ko": "진정제를 줄이고 조기 보행을 시작하면 섬망 기간을 단축할 수 있습니다.",
                "vi": "Giảm thuốc an thần và bắt đầu đi lại sớm có thể rút ngắn thời gian sảng.",
                "situation": "informal"
            }
        ],
        "relatedTerms": ["중환자실", "인공호흡기", "진정제", "조기활동"]
    }
]

# Filter out any duplicates
new_slugs = {t['slug'] for t in new_terms}
duplicates = new_slugs & existing_slugs
if duplicates:
    print(f"⚠️  Skipping {len(duplicates)} duplicate slugs: {duplicates}")
    new_terms = [t for t in new_terms if t['slug'] not in existing_slugs]

# Add new terms
data.extend(new_terms)

# Save
with open(file_path, 'w', encoding='utf-8') as f:
    json.dump(data, f, ensure_ascii=False, indent=2)

print(f"✅ Added {len(new_terms)} new terms")
print(f"📊 Total terms now: {len(data)}")
