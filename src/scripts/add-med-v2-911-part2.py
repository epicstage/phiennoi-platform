#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Part 2: Remaining 38 medical terms (한방정형외과 ~ 물광주사)
"""

import json
import os

file_path = os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', 'data', 'terms', 'medical.json')

# PART 2: 38 MORE TERMS
additional_terms = [
    {
        "slug": "chinh-hinh-y-hoc-co-truyen",
        "korean": "한방정형외과",
        "vietnamese": "Chỉnh hình y học cổ truyền",
        "hanja": "韓方整形外科",
        "hanjaReading": "韓(나라 한) + 方(모 방) + 整(가지런할 정) + 形(모양 형) + 外(밖 외) + 科(과 과)",
        "pronunciation": "찐힌이혹꼬쯔엉",
        "meaningKo": "한의학에서 근골격계 질환과 외상을 다루는 분과로, 척추질환, 관절염, 골절, 염좌 등을 치료합니다. 한방정형외과는 추나요법, 침술, 부항, 한약 등을 복합적으로 사용합니다. 통역 시 주의할 점은 '정형외과'라는 명칭 때문에 양방 정형외과(수술)와 혼동될 수 있으므로, 한방정형외과는 비수술적 치료를 중심으로 한다는 점을 명확히 해야 합니다. 또한 디스크, 오십견, 무릎 관절염 같은 흔한 질환에 대한 한방 치료 접근법을 설명할 때는 치료 기간과 예상 경과를 구체적으로 전달하여 환자의 오해를 방지해야 합니다.",
        "meaningVi": "Chỉnh hình y học cổ truyền là chuyên khoa của y học Hàn Quốc điều trị bệnh lý cơ xương khớp và chấn thương như bệnh cột sống, viêm khớp, gãy xương, bong gân. Sử dụng Chu Na, châm cứu, giác hơi, hán dược tổng hợp. Chỉnh hình y học cổ truyền tập trung vào điều trị không phẫu thuật.",
        "context": "한의원, 재활센터, 척추클리닉, 관절센터",
        "culturalNote": "한국에서는 한방정형외과가 수술을 원하지 않는 환자들에게 인기가 높으며, 특히 디스크, 오십견, 퇴행성 관절염 치료에 많이 이용됩니다. 베트남에서는 수술이 부담스러운 환자들이 많으므로, 한방정형외과의 비수술적 접근이 좋은 대안이 될 수 있습니다. 한국에서는 한방정형외과 치료 후 통증 감소와 기능 회복 효과가 임상적으로 입증되어 있습니다. 베트남 환자에게는 한방정형외과가 부작용이 적고 재활 기간이 짧다는 장점을 강조하면 좋습니다.",
        "commonMistakes": [
            {
                "mistake": "Khoa chỉnh hình (양방 정형외과)",
                "correction": "Chỉnh hình y học cổ truyền (한방정형외과)",
                "explanation": "'Khoa chỉnh hình'은 수술을 하는 양방 정형외과입니다."
            },
            {
                "mistake": "수술 가능 여부를 묻는 환자에게 명확한 답변 없음",
                "correction": "'Chỉnh hình y học cổ truyền không phẫu thuật'",
                "explanation": "한방정형외과는 수술을 하지 않으므로 명확히 해야 합니다."
            },
            {
                "mistake": "치료 기간을 정확히 전달하지 않음",
                "correction": "질환별 예상 치료 기간 안내 (예: 디스크 3개월)",
                "explanation": "환자가 치료 기간을 알아야 계획을 세울 수 있습니다."
            }
        ],
        "examples": [
            {
                "ko": "허리디스크는 수술 없이 한방정형외과 치료로 호전될 수 있습니다.",
                "vi": "Thoát vị đĩa đệm có thể cải thiện bằng điều trị Chỉnh hình y học cổ truyền không phẫu thuật.",
                "situation": "formal"
            },
            {
                "ko": "추나요법과 침 치료를 병행하면 효과가 더 좋아요.",
                "vi": "Kết hợp Chu Na và châm cứu sẽ hiệu quả hơn.",
                "situation": "onsite"
            },
            {
                "ko": "한방정형외과는 재활 치료도 함께 진행합니다.",
                "vi": "Chỉnh hình y học cổ truyền cũng tiến hành phục hồi chức năng.",
                "situation": "formal"
            }
        ],
        "relatedTerms": ["추나요법", "디스크", "관절염", "재활치료"]
    },
    {
        "slug": "nhan-y-hoc-co-truyen",
        "korean": "한방안이비인후피부과",
        "vietnamese": "Nhãn - Tai Mũi Họng - Da liễu y học cổ truyền",
        "hanja": "韓方眼耳鼻咽喉皮膚科",
        "hanjaReading": "韓(나라 한) + 方(모 방) + 眼(눈 안) + 耳(귀 이) + 鼻(코 비) + 咽(목구멍 인) + 喉(목 후) + 皮(가죽 피) + 膚(살결 부) + 科(과 과)",
        "pronunciation": "년 - 따이무이혹 - 잘리에우이혹꼬쯔엉",
        "meaningKo": "한의학에서 눈, 귀, 코, 목, 피부 질환을 종합적으로 다루는 분과입니다. 알레르기 비염, 축농증, 중이염, 안구건조증, 아토피, 두드러기 등을 치료합니다. 통역 시 주의할 점은 이 과의 명칭이 매우 길어서 베트남어로 풀어 설명하기 어려우므로, 환자가 이해하기 쉽게 'Chuyên khoa tai mũi họng, mắt, da y học cổ truyền'으로 간단히 표현하는 것이 실수를 줄입니다. 또한 각 질환별로 한방 치료의 접근법(예: 비염은 체질 개선, 아토피는 독소 배출)을 설명할 때는 환자가 즉각적 효과를 기대하지 않도록 장기 치료 계획을 안내해야 합니다.",
        "meaningVi": "Nhãn - Tai Mũi Họng - Da liễu y học cổ truyền là chuyên khoa của y học Hàn Quốc điều trị tổng hợp bệnh lý về mắt, tai, mũi, họng, da như viêm mũi dị ứng, viêm xoang, viêm tai giữa, khô mắt, viêm da cơ địa, mề đay. Điều trị bằng hán dược và châm cứu nhằm cải thiện thể chất căn bản.",
        "context": "한의원, 이비인후과 클리닉, 피부과 클리닉, 알레르기 센터",
        "culturalNote": "한국에서는 한방안이비인후피부과가 만성 비염, 아토피 피부염, 건선 등 난치성 질환 치료에 많이 이용됩니다. 베트남에서도 알레르기와 피부 질환이 흔하므로, 한방 치료가 좋은 대안이 될 수 있습니다. 한국에서는 이 과에서 '비염 치료 한약', '아토피 연고' 등 특화된 처방을 제공합니다. 베트남 환자에게는 한방 치료가 스테로이드 없이 안전하게 피부 질환을 관리한다는 점을 강조하면 관심도가 높아집니다.",
        "commonMistakes": [
            {
                "mistake": "과 이름을 전부 직역하여 혼란 야기",
                "correction": "간단히 'Chuyên khoa tai mũi họng, mắt, da y học cổ truyền'",
                "explanation": "긴 명칭은 환자가 이해하기 어려우므로 간결하게 설명합니다."
            },
            {
                "mistake": "아토피를 'bệnh ngoài da(피부병)'로만 표현",
                "correction": "Viêm da cơ địa (아토피)",
                "explanation": "'Viêm da cơ địa'가 아토피의 정확한 베트남어입니다."
            },
            {
                "mistake": "즉각적 효과를 기대하게 함",
                "correction": "'Điều trị y học cổ truyền cần thời gian dài nhưng hiệu quả bền vững'",
                "explanation": "만성 질환은 장기 치료가 필요함을 명확히 해야 합니다."
            }
        ],
        "examples": [
            {
                "ko": "만성 비염은 한방안이비인후피부과에서 체질 개선 치료를 받으세요.",
                "vi": "Viêm mũi mãn tính hãy điều trị cải thiện thể chất ở chuyên khoa tai mũi họng y học cổ truyền.",
                "situation": "formal"
            },
            {
                "ko": "아토피는 한약 복용과 연고를 병행해요.",
                "vi": "Viêm da cơ địa uống hán dược kết hợp thoa thuốc mỡ.",
                "situation": "onsite"
            },
            {
                "ko": "안구건조증에는 간 기능을 보하는 한약이 효과적입니다.",
                "vi": "Khô mắt dùng hán dược bổ gan rất hiệu quả.",
                "situation": "formal"
            }
        ],
        "relatedTerms": ["비염", "아토피", "안구건조증", "축농증"]
    },
    {
        "slug": "visa-du-lich-y-te",
        "korean": "의료관광비자",
        "vietnamese": "Visa du lịch y tế",
        "hanja": None,
        "hanjaReading": None,
        "pronunciation": "비자주릭이떼",
        "meaningKo": "의료 목적으로 한국을 방문하는 외국인 환자가 받는 특별 비자입니다. 의료관광비자는 일반 관광비자보다 체류 기간이 길고, 동반자 비자도 함께 발급됩니다. 통역 시 주의할 점은 비자 신청 절차와 필요 서류를 정확히 전달해야 하는데, 특히 병원 진료 예약 확인서, 치료 계획서 등이 필수 서류임을 명확히 해야 합니다. 또한 의료관광비자의 체류 기간, 연장 가능 여부, 동반자 자격 등을 구체적으로 안내하여 환자가 미리 준비할 수 있도록 해야 합니다. 비자 발급 소요 기간도 정확히 전달하여 일정 계획에 차질이 없도록 하는 것이 중요합니다.",
        "meaningVi": "Visa du lịch y tế là loại visa đặc biệt dành cho bệnh nhân nước ngoài đến Hàn Quốc để điều trị y tế. Visa du lịch y tế có thời gian lưu trú dài hơn visa du lịch thông thường và cấp cả visa cho người đi kèm. Để xin visa cần có giấy xác nhận hẹn khám từ bệnh viện, kế hoạch điều trị và các giấy tờ liên quan.",
        "context": "의료관광, 병원 행정, 국제진료센터, 비자 상담",
        "culturalNote": "한국은 의료관광 강국으로, 매년 수십만 명의 외국인 환자가 치료를 받으러 옵니다. 베트남인도 성형, 건강검진, 암 치료 등을 위해 한국을 많이 방문합니다. 의료관광비자는 대한민국 영사관에서 발급하며, 병원의 초청장이 필요합니다. 통역사는 환자가 비자 신청 과정에서 어려움을 겪지 않도록 자세한 정보를 제공해야 합니다. 특히 베트남에서는 비자 발급 절차가 복잡할 수 있으므로, 병원에서 제공하는 서류의 정확성이 중요합니다.",
        "commonMistakes": [
            {
                "mistake": "Visa du lịch (일반 관광비자)",
                "correction": "Visa du lịch y tế (의료관광비자)",
                "explanation": "의료 목적이므로 'y tế(의료)'를 반드시 포함해야 합니다."
            },
            {
                "mistake": "필요 서류를 대략적으로만 설명",
                "correction": "진료 예약 확인서, 치료 계획서, 재정 증빙 등 구체적 목록 제공",
                "explanation": "서류 미비로 비자가 거부될 수 있으므로 정확한 목록이 필수입니다."
            },
            {
                "mistake": "동반자 비자 자격을 설명하지 않음",
                "correction": "'Người đi kèm phải là gia đình trực hệ(직계가족)'",
                "explanation": "동반자 자격이 제한적이므로 명확히 해야 합니다."
            }
        ],
        "examples": [
            {
                "ko": "의료관광비자를 신청하려면 병원의 진료 예약 확인서가 필요합니다.",
                "vi": "Để xin visa du lịch y tế cần có giấy xác nhận hẹn khám từ bệnh viện.",
                "situation": "formal"
            },
            {
                "ko": "의료관광비자는 최대 90일까지 체류할 수 있어요.",
                "vi": "Visa du lịch y tế có thể lưu trú tối đa 90 ngày.",
                "situation": "onsite"
            },
            {
                "ko": "환자 1명당 동반자 1명까지 비자를 받을 수 있습니다.",
                "vi": "Mỗi bệnh nhân được cấp visa cho 1 người đi kèm.",
                "situation": "formal"
            }
        ],
        "relatedTerms": ["의료관광", "진료예약", "국제진료", "비자연장"]
    },
    {
        "slug": "goi-kham-suc-khoe",
        "korean": "건강검진패키지",
        "vietnamese": "Gói khám sức khỏe",
        "hanja": "健康檢診package",
        "hanjaReading": "健(튼튼할 건) + 康(편안할 강) + 檢(조사할 검) + 診(진찰할 진)",
        "pronunciation": "고이캄슥코에",
        "meaningKo": "종합적인 건강 상태를 확인하기 위해 여러 검사를 묶어 제공하는 의료 서비스입니다. 한국의 건강검진패키지는 기본 검진부터 암 정밀검진, VIP 검진까지 다양합니다. 통역 시 주의할 점은 패키지에 포함된 검사 항목을 정확히 나열하고, 포함되지 않는 추가 검사와 비용을 명확히 구분해야 합니다. 또한 검진 소요 시간, 결과 수령 시기, 결과 설명 방법(대면/서면)을 구체적으로 전달하여 환자가 일정을 계획할 수 있도록 해야 합니다. 특히 베트남 환자에게는 한국 건강검진의 정밀도와 신속성을 강조하면 신뢰도가 높아집니다.",
        "meaningVi": "Gói khám sức khỏe là dịch vụ y tế tổng hợp nhiều xét nghiệm để kiểm tra toàn diện tình trạng sức khỏe. Gói khám sức khỏe ở Hàn Quốc rất đa dạng từ khám cơ bản đến khám ung thư chi tiết, khám VIP. Bao gồm xét nghiệm máu, nội soi, CT, MRI và tư vấn kết quả chi tiết. Thời gian khám từ vài giờ đến cả ngày tùy gói.",
        "context": "건강검진센터, 종합병원, 의료관광, 예방의학",
        "culturalNote": "한국의 건강검진은 세계적으로 유명하며, 특히 암 조기 발견율이 높습니다. 베트남인들이 한국에서 건강검진을 받으러 많이 오는 이유는 정밀한 검사와 빠른 결과 제공 때문입니다. 한국에서는 하루 안에 모든 검사를 마칠 수 있고, 결과도 며칠 내에 받을 수 있습니다. 베트남 환자에게는 검진 패키지의 가격 대비 가치와 한국 의료진의 전문성을 강조하면 좋습니다. 또한 통역 지원이 되는지 미리 안내해야 합니다.",
        "commonMistakes": [
            {
                "mistake": "Khám sức khỏe (일반 건강검진)",
                "correction": "Gói khám sức khỏe tổng quát (종합 건강검진 패키지)",
                "explanation": "'Gói(패키지)'를 명시해야 여러 검사가 포함됨을 알 수 있습니다."
            },
            {
                "mistake": "패키지 포함 항목을 모호하게 설명",
                "correction": "혈액검사, 영상검사, 내시경 등 구체적 항목 나열",
                "explanation": "환자가 어떤 검사를 받는지 정확히 알아야 합니다."
            },
            {
                "mistake": "추가 비용 발생 가능성을 미리 알리지 않음",
                "correction": "'Nếu phát hiện bất thường, xét nghiệm thêm có thể phát sinh chi phí'",
                "explanation": "추가 검사 비용 문제로 분쟁이 생길 수 있습니다."
            }
        ],
        "examples": [
            {
                "ko": "기본 건강검진 패키지는 혈액검사, 소변검사, 흉부 X-ray가 포함됩니다.",
                "vi": "Gói khám sức khỏe cơ bản bao gồm xét nghiệm máu, nước tiểu, X-quang ngực.",
                "situation": "formal"
            },
            {
                "ko": "검진 결과는 3일 후에 받으실 수 있어요.",
                "vi": "Kết quả khám sẽ nhận được sau 3 ngày.",
                "situation": "onsite"
            },
            {
                "ko": "VIP 패키지는 1:1 전담 코디네이터가 배정됩니다.",
                "vi": "Gói VIP được phân công điều phối viên riêng 1:1.",
                "situation": "formal"
            }
        ],
        "relatedTerms": ["종합검진", "암검진", "건강관리", "예방의학"]
    },
    {
        "slug": "du-lich-tham-my",
        "korean": "성형관광",
        "vietnamese": "Du lịch thẩm mỹ",
        "hanja": "成形觀光",
        "hanjaReading": "成(이룰 성) + 形(모양 형) + 觀(볼 관) + 光(빛 광)",
        "pronunciation": "주릭탐미",
        "meaningKo": "성형수술을 받기 위해 해외로 여행하는 의료관광의 한 형태입니다. 한국은 세계적인 성형관광 목적지로, 특히 얼굴 성형, 체형 관리에 강점이 있습니다. 통역 시 주의할 점은 수술 전후 주의사항, 회복 기간, 부작용 가능성을 정확하고 솔직하게 전달해야 하며, 환자의 기대치를 현실적으로 관리하는 것이 중요합니다. 또한 수술 후 한국에 머물러야 하는 기간, 사후 관리 방법, 귀국 후 문제 발생 시 대처 방법 등을 구체적으로 안내하여 환자가 충분히 준비할 수 있도록 해야 합니다. 성형 결과에 대한 과도한 기대를 줄이는 것도 통역사의 역할입니다.",
        "meaningVi": "Du lịch thẩm mỹ là hình thức du lịch y tế để thực hiện phẫu thuật thẩm mỹ ở nước ngoài. Hàn Quốc là điểm đến du lịch thẩm mỹ hàng đầu thế giới, đặc biệt nổi tiếng về phẫu thuật khuôn mặt và quản lý vóc dáng. Cần lưu ý thời gian hồi phục, chăm sóc sau phẫu thuật và nguy cơ biến chứng.",
        "context": "성형외과, 의료관광, 미용클리닉, 국제진료",
        "culturalNote": "한국은 '성형 천국'으로 불리며, 베트남을 포함한 많은 외국인이 한국에서 성형수술을 받습니다. 한국의 성형 기술은 세계 최고 수준이지만, 언어 소통 문제와 문화 차이로 인한 오해가 발생할 수 있습니다. 통역사는 의사와 환자 간의 정확한 의사소통을 돕고, 수술 동의서의 내용을 완전히 이해시켜야 합니다. 베트남 환자에게는 한국 성형의 자연스러움과 안전성을 강조하되, 부작용 가능성도 솔직히 전달해야 신뢰를 얻습니다.",
        "commonMistakes": [
            {
                "mistake": "Du lịch (일반 여행)",
                "correction": "Du lịch thẩm mỹ (성형관광)",
                "explanation": "'Thẩm mỹ(미용)'를 명시해야 의료 목적임을 알 수 있습니다."
            },
            {
                "mistake": "수술 결과를 과장하여 설명",
                "correction": "'Kết quả tùy thuộc vào điều kiện cá nhân'",
                "explanation": "과도한 기대는 불만으로 이어질 수 있습니다."
            },
            {
                "mistake": "회복 기간을 짧게 설명",
                "correction": "실제 회복 기간과 부기 지속 기간을 정확히 전달",
                "explanation": "환자가 일정을 잘못 계획할 수 있습니다."
            }
        ],
        "examples": [
            {
                "ko": "쌍꺼풀 수술 후 약 1주일은 부기가 있을 수 있습니다.",
                "vi": "Sau phẫu thuật mí mắt có thể sưng khoảng 1 tuần.",
                "situation": "formal"
            },
            {
                "ko": "수술 후 최소 3일은 한국에 머물러야 해요.",
                "vi": "Sau phẫu thuật phải ở lại Hàn Quốc ít nhất 3 ngày.",
                "situation": "onsite"
            },
            {
                "ko": "성형관광 패키지에는 공항 픽업과 숙박이 포함됩니다.",
                "vi": "Gói du lịch thẩm mỹ bao gồm đón sân bay và chỗ ở.",
                "situation": "formal"
            }
        ],
        "relatedTerms": ["성형수술", "미용", "회복기간", "사후관리"]
    },
    {
        "slug": "du-lich-nha-khoa",
        "korean": "치과관광",
        "vietnamese": "Du lịch nha khoa",
        "hanja": "齒科觀光",
        "hanjaReading": "齒(이 치) + 科(과 과) + 觀(볼 관) + 光(빛 광)",
        "pronunciation": "주릭냐코아",
        "meaningKo": "치과 치료를 받기 위해 해외로 여행하는 의료관광의 한 형태입니다. 한국은 임플란트, 심미 치료, 교정 등에서 높은 수준의 기술을 가지고 있습니다. 통역 시 주의할 점은 치료 과정이 여러 단계로 나뉘어질 수 있으므로, 각 단계별 소요 기간과 방문 횟수를 명확히 전달해야 합니다. 또한 임플란트 같은 경우 뼈 이식이 필요한지, 치료 기간이 얼마나 걸리는지 등을 구체적으로 설명하여 환자가 체류 기간을 계획할 수 있도록 해야 합니다. 치료 비용도 단계별로 나누어 설명하고, 귀국 후 문제 발생 시 원격 상담이 가능한지도 안내하는 것이 중요합니다.",
        "meaningVi": "Du lịch nha khoa là hình thức du lịch y tế để điều trị răng miệng ở nước ngoài. Hàn Quốc có công nghệ nha khoa tiên tiến về cấy ghép implant, điều trị thẩm mỹ, chỉnh nha. Cần lưu ý điều trị nha khoa thường chia nhiều giai đoạn, mỗi giai đoạn cần hẹn riêng và thời gian hồi phục.",
        "context": "치과, 임플란트센터, 심미치과, 의료관광",
        "culturalNote": "한국의 치과 기술은 세계적으로 인정받으며, 특히 임플란트와 라미네이트 치료에 강점이 있습니다. 베트남에서는 치과 치료 비용이 저렴하지만, 한국의 기술력과 위생 수준을 선호하는 환자들이 있습니다. 한국에서는 디지털 치과 장비를 사용하여 정밀한 진단과 치료가 가능합니다. 베트남 환자에게는 한국 치과의 첨단 장비와 무통 치료 기술을 강조하면 관심도가 높아집니다. 다만 치료 기간이 길 수 있으므로 현실적인 일정 안내가 필수입니다.",
        "commonMistakes": [
            {
                "mistake": "임플란트를 'răng giả(틀니)'로 오역",
                "correction": "Cấy ghép implant (임플란트)",
                "explanation": "임플란트와 틀니는 완전히 다른 치료법입니다."
            },
            {
                "mistake": "치료 기간을 한 번에 끝나는 것처럼 설명",
                "correction": "'Implant cần 2-3 lần hẹn, mỗi lần cách nhau vài tuần'",
                "explanation": "임플란트는 여러 단계를 거쳐야 함을 명확히 해야 합니다."
            },
            {
                "mistake": "귀국 후 문제 발생 시 대처 방법을 안내하지 않음",
                "correction": "'Nếu có vấn đề sau khi về nước, có thể tư vấn từ xa hoặc đến phòng khám liên kết'",
                "explanation": "사후 관리 방법을 모르면 환자가 불안해합니다."
            }
        ],
        "examples": [
            {
                "ko": "임플란트 치료는 총 3개월 정도 걸리며, 2-3회 방문이 필요합니다.",
                "vi": "Điều trị implant mất khoảng 3 tháng, cần đến 2-3 lần.",
                "situation": "formal"
            },
            {
                "ko": "라미네이트는 하루 만에 끝낼 수 있어요.",
                "vi": "Laminate có thể hoàn thành trong 1 ngày.",
                "situation": "onsite"
            },
            {
                "ko": "치아 교정은 최소 1년 이상 걸리므로 정기적으로 방문해야 합니다.",
                "vi": "Chỉnh nha mất ít nhất 1 năm, cần đến định kỳ.",
                "situation": "formal"
            }
        ],
        "relatedTerms": ["임플란트", "라미네이트", "치아교정", "심미치료"]
    },
    {
        "slug": "phong-hoi-tinh",
        "korean": "회복실",
        "vietnamese": "Phòng hồi tỉnh",
        "hanja": "回復室",
        "hanjaReading": "回(돌아올 회) + 復(회복할 복) + 室(방 실)",
        "pronunciation": "퐁허이띤",
        "meaningKo": "수술이나 마취 후 환자가 의식을 되찾고 안정을 취하는 병원 내 공간입니다. 회복실에서는 간호사가 환자의 활력징후를 모니터링하며, 합병증 발생 여부를 감시합니다. 통역 시 주의할 점은 환자가 회복실에서 얼마나 머물러야 하는지, 어떤 상태가 되면 병실로 이동할 수 있는지를 명확히 전달해야 합니다. 또한 회복실에서 느낄 수 있는 불편감(오심, 통증, 목마름)과 대처 방법을 미리 안내하여 환자가 당황하지 않도록 해야 합니다. 보호자가 회복실에 들어갈 수 있는지 여부도 사전에 확인하여 전달하는 것이 중요합니다.",
        "meaningVi": "Phòng hồi tỉnh là không gian trong bệnh viện để bệnh nhân tỉnh lại và ổn định sau phẫu thuật hoặc gây mê. Tại phòng hồi tỉnh, y tá theo dõi dấu hiệu sinh tồn và kiểm tra biến chứng. Thời gian lưu ở phòng hồi tỉnh tùy thuộc vào tình trạng bệnh nhân.",
        "context": "수술실, 마취과, 병원 입원, 응급실",
        "culturalNote": "한국 병원의 회복실은 철저한 감시 시스템을 갖추고 있으며, 환자 안전을 최우선으로 합니다. 베트남 환자들은 회복실이라는 개념이 낯설 수 있으므로, 수술 전에 회복실의 목적과 절차를 설명하는 것이 중요합니다. 한국에서는 회복실에서 완전히 깨어나고 활력징후가 안정될 때까지 보호자를 만날 수 없는 경우가 많으므로, 이를 사전에 안내해야 보호자가 걱정하지 않습니다.",
        "commonMistakes": [
            {
                "mistake": "Phòng nghỉ (휴게실)",
                "correction": "Phòng hồi tỉnh (회복실)",
                "explanation": "'Phòng nghỉ'는 일반 휴게실이고, 'Phòng hồi tỉnh'은 마취 후 회복실입니다."
            },
            {
                "mistake": "회복실 체류 시간을 정확히 안내하지 않음",
                "correction": "'Thường ở phòng hồi tỉnh 1-2 giờ tùy tình trạng'",
                "explanation": "환자와 보호자가 대기 시간을 알아야 합니다."
            },
            {
                "mistake": "회복실에서의 불편감을 미리 알리지 않음",
                "correction": "'Sau mê có thể buồn nôn, khát nước, đây là bình thường'",
                "explanation": "예상되는 증상을 미리 알려야 환자가 안심합니다."
            }
        ],
        "examples": [
            {
                "ko": "수술 후 회복실에서 1-2시간 정도 머물게 됩니다.",
                "vi": "Sau phẫu thuật sẽ ở phòng hồi tỉnh khoảng 1-2 giờ.",
                "situation": "formal"
            },
            {
                "ko": "회복실에서 완전히 깨어나면 병실로 옮겨져요.",
                "vi": "Khi tỉnh hẳn ở phòng hồi tỉnh sẽ chuyển lên phòng bệnh.",
                "situation": "onsite"
            },
            {
                "ko": "보호자는 환자가 병실로 이동한 후에 만날 수 있습니다.",
                "vi": "Người nhà có thể gặp sau khi bệnh nhân chuyển lên phòng bệnh.",
                "situation": "formal"
            }
        ],
        "relatedTerms": ["마취", "수술", "활력징후", "집중치료실"]
    },
    {
        "slug": "dieu-tri-ngoai-tru",
        "korean": "통원치료",
        "vietnamese": "Điều trị ngoại trú",
        "hanja": "通院治療",
        "hanjaReading": "通(통할 통) + 院(집 원) + 治(다스릴 치) + 療(고칠 료)",
        "pronunciation": "디에우찌응오아이쭈",
        "meaningKo": "입원하지 않고 병원에 정기적으로 방문하여 치료를 받는 형태입니다. 통원치료는 만성질환 관리, 재활 치료, 항암 치료 등에 사용됩니다. 통역 시 주의할 점은 통원 빈도(주 1회, 월 1회 등), 각 방문 시 소요 시간, 교통편 등을 구체적으로 안내하여 환자가 일정을 계획할 수 있도록 해야 합니다. 또한 통원치료와 입원치료의 비용 차이, 보험 적용 여부 등을 명확히 설명하여 환자가 치료 방식을 선택할 수 있도록 해야 합니다. 베트남 환자의 경우 거리가 멀면 통원이 어려울 수 있으므로 대안(집중 치료 후 귀국 등)도 제시하는 것이 좋습니다.",
        "meaningVi": "Điều trị ngoại trú là hình thức điều trị không nhập viện mà đến bệnh viện định kỳ. Điều trị ngoại trú được dùng cho quản lý bệnh mãn tính, phục hồi chức năng, hóa trị. Chi phí điều trị ngoại trú thấp hơn nội trú và bệnh nhân có thể sinh hoạt bình thường.",
        "context": "만성질환, 재활치료, 항암치료, 외래진료",
        "culturalNote": "한국의 의료 시스템은 통원치료와 입원치료를 명확히 구분하며, 가능하면 통원치료를 우선합니다. 베트남 환자들은 한국에서 통원치료를 받을 경우 숙박 문제와 교통 문제를 고려해야 하므로, 병원 근처 숙소 정보나 교통편을 함께 안내하는 것이 좋습니다. 한국의 통원치료는 효율적이고 체계적이므로, 입원보다 비용 부담이 적다는 장점을 설명하면 좋습니다.",
        "commonMistakes": [
            {
                "mistake": "Khám ngoại (외래 진찰)",
                "correction": "Điều trị ngoại trú (통원 치료)",
                "explanation": "'Khám(진찰)'과 'Điều trị(치료)'는 다릅니다."
            },
            {
                "mistake": "통원 빈도를 명확히 안내하지 않음",
                "correction": "'Cần đến 2 lần/tuần trong 1 tháng đầu'",
                "explanation": "환자가 통원 일정을 계획할 수 있어야 합니다."
            },
            {
                "mistake": "통원치료와 입원치료의 비용 차이를 설명하지 않음",
                "correction": "'Điều trị ngoại trú rẻ hơn nội trú khoảng 50%'",
                "explanation": "비용 정보는 환자의 의사결정에 중요합니다."
            }
        ],
        "examples": [
            {
                "ko": "당뇨병은 월 1회 통원치료로 관리할 수 있습니다.",
                "vi": "Tiểu đường có thể quản lý bằng điều trị ngoại trú 1 lần/tháng.",
                "situation": "formal"
            },
            {
                "ko": "항암 통원치료는 보통 3-4시간 정도 걸려요.",
                "vi": "Hóa trị ngoại trú thường mất khoảng 3-4 giờ.",
                "situation": "onsite"
            },
            {
                "ko": "통원치료가 가능하므로 입원할 필요는 없습니다.",
                "vi": "Có thể điều trị ngoại trú nên không cần nhập viện.",
                "situation": "formal"
            }
        ],
        "relatedTerms": ["외래진료", "입원치료", "만성질환", "재활"]
    },
    {
        "slug": "dieu-tri-noi-tru",
        "korean": "입원치료",
        "vietnamese": "Điều trị nội trú",
        "hanja": "入院治療",
        "hanjaReading": "入(들 입) + 院(집 원) + 治(다스릴 치) + 療(고칠 료)",
        "pronunciation": "디에우찌노이쭈",
        "meaningKo": "병원에 입원하여 집중적인 치료와 관리를 받는 형태입니다. 입원치료는 수술, 중증 질환, 집중 관찰이 필요한 경우에 시행됩니다. 통역 시 주의할 점은 입원 기간, 입원비, 병실 종류(일반실/2인실/1인실), 식사 제공 여부 등을 구체적으로 안내해야 합니다. 또한 입원 중 보호자의 동반 가능 여부, 면회 시간, 퇴원 기준 등을 명확히 전달하여 환자와 가족이 준비할 수 있도록 해야 합니다. 특히 베트남 환자의 경우 입원비가 부담될 수 있으므로, 보험 적용 여부와 일일 입원비를 사전에 정확히 안내하는 것이 중요합니다.",
        "meaningVi": "Điều trị nội trú là hình thức nhập viện để nhận điều trị và chăm sóc tập trung. Điều trị nội trú được áp dụng cho phẫu thuật, bệnh nặng, cần theo dõi sát. Thời gian nằm viện, chi phí, loại phòng bệnh (phòng thường/2 người/1 người) khác nhau.",
        "context": "병원 입원, 수술, 중환자실, 응급실",
        "culturalNote": "한국의 입원 시스템은 매우 체계적이며, 환자 안전과 편의를 우선합니다. 베트남과 달리 한국에서는 보호자가 24시간 병실에 머무르는 것이 제한될 수 있으므로, 이를 사전에 설명해야 합니다. 한국 병원은 입원 환자에게 식사를 제공하며, 병실 등급에 따라 편의시설이 다릅니다. 베트남 환자에게는 입원비 총액을 미리 견적으로 제공하고, 예상치 못한 추가 비용 발생 가능성도 안내해야 분쟁을 예방할 수 있습니다.",
        "commonMistakes": [
            {
                "mistake": "Nằm viện (단순히 병원에 누워있다)",
                "correction": "Điều trị nội trú / Nhập viện điều trị",
                "explanation": "'Điều trị(치료)'를 명시해야 적극적 치료임을 알 수 있습니다."
            },
            {
                "mistake": "입원 기간을 모호하게 안내",
                "correction": "'Dự kiến nằm viện 3-5 ngày'",
                "explanation": "환자가 일정과 비용을 계획할 수 있어야 합니다."
            },
            {
                "mistake": "보호자 동반 규정을 설명하지 않음",
                "correction": "'Người nhà có thể ở lại ban đêm với phòng 1 người'",
                "explanation": "보호자 동반 규정을 모르면 혼란이 생길 수 있습니다."
            }
        ],
        "examples": [
            {
                "ko": "수술 후 3-5일 정도 입원치료가 필요합니다.",
                "vi": "Sau phẫu thuật cần điều trị nội trú khoảng 3-5 ngày.",
                "situation": "formal"
            },
            {
                "ko": "1인실은 하루 입원비가 15만 원이에요.",
                "vi": "Phòng 1 người viện phí 1 ngày là 150 nghìn won.",
                "situation": "onsite"
            },
            {
                "ko": "입원 기간 동안 매일 회진을 통해 상태를 확인합니다.",
                "vi": "Trong thời gian nằm viện, mỗi ngày sẽ thăm khám để kiểm tra tình trạng.",
                "situation": "formal"
            }
        ],
        "relatedTerms": ["입원", "퇴원", "병실", "회진"]
    },
    {
        "slug": "kham-ngoai-tru",
        "korean": "외래진료",
        "vietnamese": "Khám ngoại trú",
        "hanja": "外來診療",
        "hanjaReading": "外(밖 외) + 來(올 래) + 診(진찰할 진) + 療(고칠 료)",
        "pronunciation": "캄응오아이쭈",
        "meaningKo": "입원하지 않고 병원을 방문하여 진찰과 간단한 치료를 받는 것입니다. 외래진료는 예약제로 운영되며, 진료과별로 요일과 시간이 정해져 있습니다. 통역 시 주의할 점은 예약 방법, 진료 대기 시간, 진료비, 처방전 수령 방법 등을 구체적으로 안내해야 합니다. 또한 초진과 재진의 차이, 건강보험 적용 여부 등을 명확히 설명하여 환자가 준비할 수 있도록 해야 합니다. 베트남 환자의 경우 예약 시스템이 익숙하지 않을 수 있으므로, 예약 절차와 예약 변경 방법을 자세히 설명하는 것이 중요합니다.",
        "meaningVi": "Khám ngoại trú là đến bệnh viện để khám bệnh và điều trị đơn giản không nhập viện. Khám ngoại trú hoạt động theo hệ thống hẹn trước, mỗi khoa có ngày giờ khám riêng. Cần đặt hẹn trước, mang theo giấy tờ cần thiết và thanh toán viện phí sau khám.",
        "context": "병원 외래, 예약진료, 만성질환 관리, 정기검진",
        "culturalNote": "한국의 외래진료는 예약 시스템이 잘 발달되어 있어 대기 시간이 짧습니다. 베트남에서는 예약 없이 병원에 가는 경우가 많지만, 한국에서는 예약이 필수입니다. 한국 병원의 외래진료는 효율적이며, 대부분 30분 이내에 진료가 끝납니다. 베트남 환자에게는 예약 시간을 엄수해야 한다는 점과 예약 없이 방문하면 당일 진료가 어려울 수 있다는 점을 강조해야 합니다.",
        "commonMistakes": [
            {
                "mistake": "Khám bệnh (일반적인 진찰)",
                "correction": "Khám ngoại trú (외래 진료)",
                "explanation": "'Ngoại trú(외래)'를 명시해야 입원과 구분됩니다."
            },
            {
                "mistake": "예약 없이 방문 가능하다고 안내",
                "correction": "'Cần đặt hẹn trước, không thể khám đột xuất'",
                "explanation": "한국은 예약제이므로 명확히 해야 합니다."
            },
            {
                "mistake": "진료비를 대략적으로만 안내",
                "correction": "초진 15,000원, 재진 10,000원 등 구체적 금액",
                "explanation": "환자가 비용을 미리 준비할 수 있어야 합니다."
            }
        ],
        "examples": [
            {
                "ko": "외래진료는 온라인이나 전화로 예약하실 수 있습니다.",
                "vi": "Khám ngoại trú có thể đặt hẹn online hoặc qua điện thoại.",
                "situation": "formal"
            },
            {
                "ko": "예약 시간 10분 전에 접수창구에 도착하세요.",
                "vi": "Hãy đến quầy tiếp nhận trước 10 phút giờ hẹn.",
                "situation": "onsite"
            },
            {
                "ko": "외래진료 후 약은 병원 약국에서 받으실 수 있습니다.",
                "vi": "Sau khám ngoại trú, nhận thuốc ở hiệu thuốc bệnh viện.",
                "situation": "formal"
            }
        ],
        "relatedTerms": ["예약진료", "초진", "재진", "진료비"]
    },
    {
        "slug": "kham-tu-xa",
        "korean": "원격진료",
        "vietnamese": "Khám từ xa",
        "hanja": "遠隔診療",
        "hanjaReading": "遠(멀 원) + 隔(사이 격) + 診(진찰할 진) + 療(고칠 료)",
        "pronunciation": "캄뜨싸",
        "meaningKo": "화상 통화나 전화를 통해 의사가 환자를 원격으로 진찰하고 상담하는 의료 서비스입니다. 코로나19 이후 한국에서도 제한적으로 허용되었습니다. 통역 시 주의할 점은 원격진료의 한계(정밀 검사 불가, 처방 제한)를 명확히 전달하고, 어떤 경우에 원격진료가 적합한지 설명해야 합니다. 또한 원격진료 플랫폼 사용 방법, 진료비 결제 방법, 처방전 수령 방법 등을 구체적으로 안내하여 환자가 원활하게 서비스를 이용할 수 있도록 해야 합니다. 베트남 환자의 경우 귀국 후 원격으로 사후 관리를 받을 수 있는지 여부도 중요한 정보입니다.",
        "meaningVi": "Khám từ xa là dịch vụ y tế mà bác sĩ khám và tư vấn bệnh nhân qua video call hoặc điện thoại. Sau Covid-19, Hàn Quốc cho phép khám từ xa có giới hạn. Khám từ xa không thể làm xét nghiệm chi tiết, kê đơn có hạn chế, phù hợp với tư vấn, tái khám, quản lý bệnh mãn tính.",
        "context": "의료관광 사후관리, 만성질환 관리, 재진, 상담",
        "culturalNote": "한국의 원격진료는 아직 제한적이지만, 의료관광 환자의 사후 관리에는 유용하게 사용됩니다. 베트남 환자가 귀국 후에도 한국 의사와 소통할 수 있다는 점은 큰 장점입니다. 다만 원격진료로는 약 처방이 제한적이고, 정밀 검사가 불가능하므로 긴급 상황에는 현지 병원을 방문해야 합니다. 베트남 환자에게는 원격진료가 가능한 시간대와 통역 지원 여부를 사전에 확인시켜야 합니다.",
        "commonMistakes": [
            {
                "mistake": "Khám online (온라인 진찰)",
                "correction": "Khám từ xa (원격 진료)",
                "explanation": "'Khám từ xa'가 정식 의료 용어입니다."
            },
            {
                "mistake": "원격진료로 모든 처방이 가능하다고 설명",
                "correction": "'Khám từ xa chỉ kê đơn thuốc đơn giản, thuốc mạnh không được'",
                "explanation": "원격진료의 처방 제한을 명확히 해야 합니다."
            },
            {
                "mistake": "플랫폼 사용 방법을 설명하지 않음",
                "correction": "앱 설치, 로그인, 예약 방법 단계별 안내",
                "explanation": "기술에 익숙하지 않은 환자를 위해 자세한 안내가 필요합니다."
            }
        ],
        "examples": [
            {
                "ko": "귀국 후에도 원격진료로 사후 관리를 받으실 수 있습니다.",
                "vi": "Sau khi về nước vẫn có thể nhận chăm sóc hậu phẫu qua khám từ xa.",
                "situation": "formal"
            },
            {
                "ko": "원격진료는 화상 통화로 진행되며 약 10-15분 정도 걸려요.",
                "vi": "Khám từ xa qua video call, mất khoảng 10-15 phút.",
                "situation": "onsite"
            },
            {
                "ko": "증상이 심해지면 원격진료 대신 직접 병원에 오셔야 합니다.",
                "vi": "Nếu triệu chứng nặng thì phải đến bệnh viện thay vì khám từ xa.",
                "situation": "formal"
            }
        ],
        "relatedTerms": ["화상진료", "전화상담", "사후관리", "처방전"]
    },
    {
        "slug": "y-kien-thu-hai",
        "korean": "세컨드오피니언",
        "vietnamese": "Ý kiến thứ hai",
        "hanja": None,
        "hanjaReading": None,
        "pronunciation": "이끼엔투하이",
        "meaningKo": "현재 받고 있는 진단이나 치료 계획에 대해 다른 의사의 의견을 듣는 것입니다. 세컨드오피니언은 환자의 권리이며, 중대한 수술이나 치료 결정 전에 권장됩니다. 통역 시 주의할 점은 세컨드오피니언이 기존 의사에 대한 불신이 아니라 신중한 의사결정을 위한 정당한 절차임을 강조해야 합니다. 또한 세컨드오피니언을 위해 필요한 서류(검사 결과, 영상 자료, 진료 기록)와 절차, 비용 등을 구체적으로 안내하여 환자가 준비할 수 있도록 해야 합니다. 베트남 환자의 경우 세컨드오피니언 문화가 낯설 수 있으므로, 이것이 환자의 당연한 권리라는 점을 설명하는 것이 중요합니다.",
        "meaningVi": "Ý kiến thứ hai là nghe ý kiến của bác sĩ khác về chẩn đoán hoặc kế hoạch điều trị hiện tại. Ý kiến thứ hai là quyền của bệnh nhân, được khuyến khích trước khi quyết định phẫu thuật hoặc điều trị lớn. Cần chuẩn bị kết quả xét nghiệm, hình ảnh y khoa, hồ sơ bệnh án.",
        "context": "암 진단, 수술 결정, 중증 질환, 환자 권리",
        "culturalNote": "한국에서는 세컨드오피니언이 환자의 권리로 인정되며, 특히 암이나 중대한 수술 전에 흔히 이용됩니다. 베트남에서는 세컨드오피니언 문화가 덜 발달되어 있을 수 있으므로, 이것이 의사에 대한 무례가 아니라 신중한 의사결정을 위한 것임을 설명해야 합니다. 한국의 대형 병원들은 세컨드오피니언 클리닉을 별도로 운영하며, 객관적이고 전문적인 의견을 제공합니다.",
        "commonMistakes": [
            {
                "mistake": "Hỏi ý kiến bác sĩ khác (단순히 다른 의사에게 물어보기)",
                "correction": "Tham khảo ý kiến thứ hai / Second opinion",
                "explanation": "'Second opinion'은 정식 의료 서비스입니다."
            },
            {
                "mistake": "세컨드오피니언을 의사에 대한 불신으로 표현",
                "correction": "'Đây là quyền của bệnh nhân để quyết định thận trọng'",
                "explanation": "세컨드오피니언은 환자의 정당한 권리임을 강조해야 합니다."
            },
            {
                "mistake": "필요한 서류를 안내하지 않음",
                "correction": "검사 결과, CT/MRI 필름, 진료 기록 등 목록 제공",
                "explanation": "서류가 없으면 세컨드오피니언이 불가능합니다."
            }
        ],
        "examples": [
            {
                "ko": "수술 전에 세컨드오피니언을 받아보시는 것을 권장합니다.",
                "vi": "Trước phẫu thuật, khuyến khích tham khảo ý kiến thứ hai.",
                "situation": "formal"
            },
            {
                "ko": "세컨드오피니언을 위해 기존 검사 결과를 가져오세요.",
                "vi": "Để được ý kiến thứ hai, hãy mang theo kết quả xét nghiệm cũ.",
                "situation": "onsite"
            },
            {
                "ko": "세컨드오피니언 진료 비용은 별도로 청구됩니다.",
                "vi": "Chi phí khám ý kiến thứ hai tính riêng.",
                "situation": "formal"
            }
        ],
        "relatedTerms": ["진단", "치료계획", "환자권리", "의료상담"]
    }
]

# Load existing, extend, save
with open(file_path, 'r', encoding='utf-8') as f:
    data = json.load(f)

data.extend(additional_terms)

with open(file_path, 'w', encoding='utf-8') as f:
    json.dump(data, f, ensure_ascii=False, indent=2)

print(f"✅ Part 2: Added {len(additional_terms)} more terms")
print(f"📊 Total: {len(data)} terms")
