#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
노인의학/노화 관련 전문용어 10개 추가
Tier S 품질 기준 (90+) 준수
"""

import json
import os

# 파일 경로 설정
file_path = os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', 'data', 'terms', 'medical.json')

# 추가할 용어들 (Tier S 품질 기준)
new_terms = [
    {
        "slug": "sa-sut-tri-tue-nguoi-gia",
        "korean": "노인성치매",
        "vietnamese": "Sa sút trí tuệ người già",
        "hanja": "老人性痴呆",
        "hanjaReading": "노(늙을 로) + 인(사람 인) + 성(성품 성) + 치(어리석을 치) + 매(어리석을 매)",
        "pronunciation": "싸 쑤엇 찌 뚜에 응으이 지아",
        "meaningKo": "고령자에게 발생하는 인지기능 저하 질환으로, 기억력, 판단력, 언어능력 등이 점진적으로 감퇴합니다. 한국에서는 '치매'라는 용어가 일반적이며, 알츠하이머병이 가장 흔한 원인입니다. 통역 시 주의할 점은 베트남에서는 'bệnh mất trí nhớ'(기억력 상실병)로도 표현하지만, 의료 현장에서는 'sa sút trí tuệ'가 더 정확한 전문 용어입니다. 치매 환자 가족 상담 시 문화적 낙인(stigma)에 대한 이해가 필요하며, 한국의 장기요양보험 제도 설명이 필요할 수 있습니다. 실수하기 쉬운 점은 단순 건망증과 치매를 혼동하는 것인데, 일상생활 지장 여부가 핵심 구분 기준입니다.",
        "meaningVi": "Bệnh suy giảm trí nhớ và các chức năng nhận thức ở người cao tuổi, bao gồm trí nhớ, khả năng phán đoán, ngôn ngữ và kỹ năng sinh hoạt hàng ngày. Bệnh Alzheimer là nguyên nhân phổ biến nhất gây sa sút trí tuệ. Tại Hàn Quốc, có hệ thống bảo hiểm chăm sóc dài hạn để hỗ trợ bệnh nhân và gia đình.",
        "context": "노인의학, 신경과, 정신건강의학과, 가족 상담",
        "culturalNote": "한국 사회에서는 치매를 가족이 돌봐야 할 책임으로 여기는 유교적 전통이 강했으나, 최근 국가 차원의 치매 관리 체계가 확립되고 있습니다. 치매안심센터, 주간보호센터 등 공공 서비스가 발달했으며, 2008년부터 장기요양보험이 시행되어 치매 환자 가족의 부담이 줄어들었습니다. 베트남 문화권에서도 가족 중심 돌봄이 일반적이지만, 한국의 제도적 지원 시스템을 설명할 필요가 있습니다. 또한 '치매'라는 용어에 대한 부정적 인식이 있어 '인지장애'로 순화해서 표현하는 경우도 많습니다.",
        "commonMistakes": [
            {
                "mistake": "'치매'를 'bệnh mất trí nhớ'로만 번역",
                "correction": "'sa sút trí tuệ' 또는 'bệnh sa sút trí tuệ'로 번역",
                "explanation": "'mất trí nhớ'는 단순 기억력 상실을 의미하지만, 치매는 포괄적인 인지기능 장애이므로 'sa sút trí tuệ'가 의학적으로 정확합니다"
            },
            {
                "mistake": "건망증과 치매를 같은 용어로 통역",
                "correction": "건망증은 'hay quên', 치매는 'sa sút trí tuệ'로 구분",
                "explanation": "건망증은 정상적인 노화 현상이지만 치매는 병리적 상태로, 일상생활 지장 여부가 다릅니다"
            },
            {
                "mistake": "'노인성 치매'와 '알츠하이머'를 동일하게 번역",
                "correction": "노인성 치매는 포괄 용어, 알츠하이머는 'bệnh Alzheimer'로 구체적 질환명",
                "explanation": "알츠하이머는 치매의 가장 흔한 원인이지만, 혈관성 치매 등 다른 원인도 있으므로 구분이 필요합니다"
            }
        ],
        "examples": [
            {
                "ko": "환자분은 경증 노인성치매로 진단되었습니다.",
                "vi": "Bệnh nhân được chẩn đoán sa sút trí tuệ mức độ nhẹ.",
                "situation": "formal"
            },
            {
                "ko": "치매 초기에는 최근 일을 자주 잊어버리는 증상이 나타납니다.",
                "vi": "Giai đoạn đầu của sa sút trí tuệ thường có triệu chứng quên những việc gần đây.",
                "situation": "onsite"
            },
            {
                "ko": "어머니 치매가 심해져서 요양병원에 모셔야 할 것 같아요.",
                "vi": "Tình trạng sa sút trí tuệ của mẹ tôi nặng hơn, có lẽ phải đưa vào bệnh viện dưỡng lão.",
                "situation": "informal"
            }
        ],
        "relatedTerms": [
            "알츠하이머병",
            "혈관성치매",
            "인지기능검사",
            "장기요양보험",
            "치매안심센터"
        ]
    },
    {
        "slug": "loang-xuong",
        "korean": "골다공증",
        "vietnamese": "Loãng xương",
        "hanja": "骨多孔症",
        "hanjaReading": "골(뼈 골) + 다(많을 다) + 공(구멍 공) + 증(병 증)",
        "pronunciation": "로앙 쑤엉",
        "meaningKo": "뼈의 밀도가 감소하고 미세구조가 약해져 골절 위험이 증가하는 질환으로, 특히 폐경 후 여성에게 흔합니다. 한국에서는 국가건강검진에 골밀도 검사가 포함되어 있으며, 예방과 조기 발견에 중점을 둡니다. 통역 시 주의할 점은 '골다공증'을 단순히 '뼈가 약해지는 것'으로 설명하면 환자가 심각성을 인지하지 못할 수 있다는 것입니다. 반드시 골절 위험성, 특히 고관절 골절이 노인 사망률을 높인다는 점을 강조해야 합니다. 또한 칼슘과 비타민D 보충, 운동요법 등 생활습관 개선이 중요하므로 이를 정확히 전달해야 합니다. 베트남어로 'xương xốp'라고도 하지만 의학 용어로는 'loãng xương'이 표준입니다.",
        "meaningVi": "Bệnh giảm mật độ xương và suy giảm cấu trúc vi mô của xương, làm tăng nguy cơ gãy xương. Phổ biến ở phụ nữ sau mãn kinh và người cao tuổi. Cần bổ sung canxi, vitamin D và tập thể dục đều đặn để phòng ngừa. Tại Hàn Quốc, xét nghiệm mật độ xương được bao gồm trong chương trình khám sức khỏe quốc gia.",
        "context": "정형외과, 내분비내과, 폐경기 건강관리",
        "culturalNote": "한국에서는 54세 이상 여성과 66세 이상 남성에게 국가건강검진으로 골밀도 검사를 무료 제공합니다. 또한 한국인의 유제품 섭취가 서구에 비해 적어 칼슘 부족이 흔하며, 이에 대한 영양 교육이 중요합니다. 베트남에서는 햇볕을 쬐는 시간이 많아 비타민D 부족이 덜하지만, 한국에서는 실내 생활이 많고 자외선 차단제 사용이 일반화되어 비타민D 부족이 흔합니다. 골다공증 치료제는 건강보험 적용이 되며, T-score -2.5 이하 또는 골절 병력이 있으면 처방받을 수 있습니다.",
        "commonMistakes": [
            {
                "mistake": "'골다공증'을 'xương xốp'로만 번역",
                "correction": "'loãng xương' 사용 (의학 표준 용어)",
                "explanation": "'xương xốp'는 구어체 표현이고, 'loãng xương'이 의료 현장에서 사용하는 정식 용어입니다"
            },
            {
                "mistake": "'골밀도'를 'độ cứng xương'으로 번역",
                "correction": "'mật độ xương' (밀도) 또는 'độ chắc xương' (치밀도)",
                "explanation": "'độ cứng'은 경도(hardness)를 의미하므로 부적절하며, 밀도(density)를 나타내는 'mật độ'가 정확합니다"
            },
            {
                "mistake": "골다공증과 골연화증을 같은 용어로 통역",
                "correction": "골다공증은 'loãng xương', 골연화증은 'mềm xương'",
                "explanation": "골다공증은 뼈의 양이 감소하는 것이고, 골연화증은 뼈의 무기질화가 부족한 질환으로 원인과 치료가 다릅니다"
            }
        ],
        "examples": [
            {
                "ko": "골밀도 검사 결과 골다공증으로 진단되셨습니다.",
                "vi": "Kết quả xét nghiệm mật độ xương cho thấy bạn bị loãng xương.",
                "situation": "formal"
            },
            {
                "ko": "골다공증 예방을 위해 칼슘과 비타민D를 꾸준히 복용하세요.",
                "vi": "Để phòng ngừa loãng xương, hãy uống canxi và vitamin D đều đặn.",
                "situation": "onsite"
            },
            {
                "ko": "어머니가 골다공증이라 넘어지면 큰일 나요.",
                "vi": "Mẹ tôi bị loãng xương nên nếu ngã sẽ rất nguy hiểm.",
                "situation": "informal"
            }
        ],
        "relatedTerms": [
            "골밀도검사",
            "척추압박골절",
            "고관절골절",
            "칼슘보충제",
            "폐경"
        ]
    },
    {
        "slug": "phong-ngua-nga",
        "korean": "낙상예방",
        "vietnamese": "Phòng ngừa ngã",
        "hanja": "落傷豫防",
        "hanjaReading": "낙(떨어질 락) + 상(다칠 상) + 예(미리 예) + 방(막을 방)",
        "pronunciation": "퐁 응으어 응아",
        "meaningKo": "노인이 넘어져 다치는 사고를 미리 막기 위한 모든 활동과 중재를 의미합니다. 한국 노인 사망 원인 중 사고사의 가장 큰 비중을 차지하는 것이 낙상이므로, 노인의학과 재활의학에서 매우 중요하게 다루는 주제입니다. 통역 시 주의할 점은 단순히 '넘어지지 않게 조심하라'는 추상적 조언이 아니라, 구체적인 환경 개선(미끄럼 방지 매트, 손잡이 설치, 조명 개선)과 신체 기능 강화(근력 운동, 균형 감각 훈련) 방법을 명확히 전달해야 한다는 것입니다. 또한 시력 저하, 약물 부작용, 어지럼증 등 낙상 위험 요인을 평가하고 관리하는 것이 핵심입니다. 베트남어로 'ngã'는 '넘어지다'를 의미하며, 'té ngã'도 같은 의미로 사용됩니다.",
        "meaningVi": "Tất cả các hoạt động và biện pháp can thiệp để ngăn ngừa người cao tuổi bị ngã và chấn thương. Bao gồm cải thiện môi trường sống (thảm chống trượt, tay vịn, chiếu sáng tốt) và tăng cường chức năng thể chất (tập luyện sức mạnh cơ, cân bằng). Ngã là nguyên nhân hàng đầu gây tử vong do tai nạn ở người cao tuổi Hàn Quốc, đặc biệt là gãy xương hông.",
        "context": "노인의학, 재활의학, 간호, 요양시설 관리",
        "culturalNote": "한국의 주거 환경은 좁은 욕실, 미끄러운 타일 바닥, 높은 문턱 등 낙상 위험 요인이 많습니다. 특히 온돌 문화로 인해 바닥 생활을 하는 경우가 많아 일어서고 앉는 동작에서 낙상이 자주 발생합니다. 베트남의 전통 가옥은 높은 턱이 있고 계단이 급한 경우가 많지만, 한국 아파트는 평탄하면서도 욕실이 위험 지역입니다. 한국에서는 지역 보건소에서 노인 낙상 예방 교육과 가정 환경 평가 서비스를 무료로 제공하며, 지팡이나 보행 보조기구 지원 사업도 있습니다. 또한 겨울철 빙판길 낙상이 매우 흔하므로, 계절에 따른 예방 수칙이 다릅니다.",
        "commonMistakes": [
            {
                "mistake": "'낙상'을 단순히 'ngã'로만 번역",
                "correction": "'ngã' 또는 'té ngã'로 번역하되, 맥락에 따라 'tai nạn ngã'(낙상 사고)로 명확히",
                "explanation": "'ngã'는 '넘어지다'는 동작을 의미하므로, 의료 사고로서의 낙상을 표현할 때는 'tai nạn ngã'가 더 적절합니다"
            },
            {
                "mistake": "'낙상 예방'을 'tránh ngã'로 번역",
                "correction": "'phòng ngừa ngã' 또는 'dự phòng té ngã'",
                "explanation": "'tránh'는 단순히 피한다는 의미지만, 'phòng ngừa'는 체계적인 예방 활동을 의미하는 전문 용어입니다"
            },
            {
                "mistake": "낙상과 추락을 구분하지 않음",
                "correction": "낙상(ngã ở độ cao thấp)은 같은 높이에서, 추락(rơi từ trên cao)은 높은 곳에서",
                "explanation": "낙상은 보행 중 넘어지는 것이고, 추락은 사다리나 계단 등에서 떨어지는 것으로 손상 정도가 다릅니다"
            }
        ],
        "examples": [
            {
                "ko": "낙상예방을 위해 욕실에 손잡이를 설치하시는 것이 좋습니다.",
                "vi": "Để phòng ngừa ngã, nên lắp tay vịn trong phòng tắm.",
                "situation": "formal"
            },
            {
                "ko": "할머니, 밤에 화장실 가실 때 불 켜고 천천히 가세요. 낙상 위험해요.",
                "vi": "Bà ơi, khi đi vệ sinh ban đêm hãy bật đèn và đi chậm. Nguy cơ ngã cao.",
                "situation": "onsite"
            },
            {
                "ko": "우리 아버지 지난달에 낙상해서 고관절 수술 받으셨어요.",
                "vi": "Bố tôi bị ngã tháng trước và phải phẫu thuật xương hông.",
                "situation": "informal"
            }
        ],
        "relatedTerms": [
            "고관절골절",
            "균형감각훈련",
            "보행보조기",
            "어지럼증",
            "시력저하"
        ]
    },
    {
        "slug": "bao-hiem-cham-soc-dai-han",
        "korean": "장기요양보험",
        "vietnamese": "Bảo hiểm chăm sóc dài hạn",
        "hanja": "長期療養保險",
        "hanjaReading": "장(길 장) + 기(기약할 기) + 요(병 고칠 료) + 양(기를 양) + 보(지킬 보) + 험(험할 험)",
        "pronunciation": "바오 히엠 짬 쏙 자이 한",
        "meaningKo": "고령이나 노인성 질병으로 일상생활을 혼자 수행하기 어려운 사람에게 신체활동 및 가사활동 지원 서비스를 제공하는 사회보험 제도입니다. 2008년 7월부터 시행된 한국의 5대 사회보험 중 하나로, 건강보험공단에서 운영합니다. 통역 시 주의할 점은 이 제도가 단순한 의료보험이 아니라 돌봄 서비스를 제공하는 사회적 돌봄 보험이라는 점을 명확히 해야 한다는 것입니다. 요양등급(1~5등급, 인지지원등급)에 따라 재가급여(방문요양, 주야간보호 등) 또는 시설급여(요양원 입소)를 선택할 수 있으며, 본인부담금은 15~20%입니다. 외국인 근로자도 건강보험 가입 기간이 있으면 신청 가능하므로, 이를 정확히 안내해야 합니다.",
        "meaningVi": "Chế độ bảo hiểm xã hội cung cấp dịch vụ hỗ trợ sinh hoạt và chăm sóc cho người cao tuổi hoặc người mắc bệnh lý tuổi già không thể tự chăm sóc bản thân. Là một trong 5 loại bảo hiểm xã hội của Hàn Quốc, bắt đầu từ năm 2008, do Bảo hiểm y tế quốc gia vận hành. Tùy theo cấp độ cần chăm sóc (cấp 1-5), có thể chọn dịch vụ tại nhà hoặc nhập viện dưỡng lão, với chi phí cá nhân chịu 15-20%.",
        "context": "사회복지, 노인의료, 요양서비스, 건강보험",
        "culturalNote": "한국의 장기요양보험은 급속한 고령화에 대응하기 위해 도입된 제도로, 전통적인 가족 중심 돌봄 문화에서 사회적 돌봄 시스템으로 전환하는 과정을 반영합니다. 베트남은 아직 이러한 제도가 없으며, 가족이 노인을 돌보는 것이 당연시되므로, 한국 제도를 설명할 때 문화적 맥락을 함께 전달해야 합니다. 신청은 만 65세 이상 또는 노인성 질병(치매, 뇌혈관질환, 파킨슨병 등)이 있는 만 65세 미만도 가능하며, 건강보험공단 직원이 가정 방문하여 인정조사를 실시합니다. 외국인의 경우 영주권자나 결혼이민자는 내국인과 동일하게 적용되며, 단순 근로자도 일정 조건 충족 시 혜택을 받을 수 있습니다.",
        "commonMistakes": [
            {
                "mistake": "'장기요양보험'을 'bảo hiểm y tế dài hạn'로 번역",
                "correction": "'bảo hiểm chăm sóc dài hạn' 또는 'bảo hiểm dưỡng lão'",
                "explanation": "'y tế'는 의료(medical)를 의미하지만, 장기요양보험은 의료보다는 돌봄(care)에 중점을 둔 제도입니다"
            },
            {
                "mistake": "'요양등급'을 'cấp độ điều trị'로 번역",
                "correction": "'cấp độ chăm sóc' 또는 'mức độ cần chăm sóc'",
                "explanation": "'điều trị'는 치료를 의미하지만, 요양등급은 돌봄의 필요도를 나타내는 것입니다"
            },
            {
                "mistake": "건강보험과 장기요양보험을 같은 제도로 설명",
                "correction": "건강보험(bảo hiểm y tế)은 의료비, 장기요양보험(bảo hiểm chăm sóc dài hạn)은 돌봄 서비스",
                "explanation": "두 제도는 별개이며, 장기요양보험료는 건강보험료에 부가하여 징수되지만 용도가 다릅니다"
            }
        ],
        "examples": [
            {
                "ko": "어머니께서 치매 진단을 받으셨다면 장기요양보험을 신청하실 수 있습니다.",
                "vi": "Nếu mẹ được chẩn đoán sa sút trí tuệ, có thể đăng ký bảo hiểm chăm sóc dài hạn.",
                "situation": "formal"
            },
            {
                "ko": "장기요양 3등급 판정받으시면 주간보호센터 이용이 가능합니다.",
                "vi": "Nếu được đánh giá cấp 3, có thể sử dụng trung tâm chăm sóc ban ngày.",
                "situation": "onsite"
            },
            {
                "ko": "아버지 요양원 비용 걱정했는데, 장기요양보험으로 많이 줄었어요.",
                "vi": "Tôi lo lắng về chi phí viện dưỡng lão cho bố, nhưng nhờ bảo hiểm chăm sóc dài hạn mà giảm nhiều.",
                "situation": "informal"
            }
        ],
        "relatedTerms": [
            "요양등급",
            "방문요양",
            "주야간보호센터",
            "요양원",
            "인정조사"
        ]
    },
    {
        "slug": "benh-vien-duong-lao",
        "korean": "요양병원",
        "vietnamese": "Bệnh viện dưỡng lão",
        "hanja": "療養病院",
        "hanjaReading": "요(병 고칠 료) + 양(기를 양) + 병(병 병) + 원(집 원)",
        "pronunciation": "번 비엔 즈엉 라오",
        "meaningKo": "주로 노인성 질환이나 만성질환을 앓고 있어 장기간 입원 치료가 필요한 환자를 대상으로 의료 서비스와 요양 서비스를 함께 제공하는 의료기관입니다. 일반 병원과 달리 급성기 치료보다는 회복과 재활, 일상생활 지원에 중점을 둡니다. 통역 시 주의할 점은 요양병원이 단순한 '쉬는 곳'이 아니라 의사, 간호사가 상주하며 의료 행위를 제공하는 정식 의료기관이라는 점을 명확히 해야 한다는 것입니다. 또한 요양원(양로원, nursing home)과 혼동하지 않도록 구분이 필요합니다. 요양병원은 건강보험 적용을 받으며, 본인부담금은 입원료의 20%이고, 장기요양보험 대상자는 추가 감면을 받을 수 있습니다. 입원 기간이 길어질수록 본인부담률이 증가하는 구조입니다.",
        "meaningVi": "Cơ sở y tế chuyên cung cấp dịch vụ chăm sóc y tế và dưỡng lão cho bệnh nhân cao tuổi hoặc mắc bệnh mạn tính cần nằm viện dài hạn. Khác với bệnh viện thông thường tập trung vào điều trị cấp tính, bệnh viện dưỡng lão chú trọng phục hồi chức năng, hồi sức và hỗ trợ sinh hoạt hàng ngày. Có bác sĩ và y tá thường trực, được bảo hiểm y tế chi trả 80%, bệnh nhân tự chi trả 20%.",
        "context": "노인의료, 재활치료, 만성질환 관리, 장기입원",
        "culturalNote": "한국의 요양병원은 1990년대 중반 이후 급속히 증가했으며, 현재 전국에 1,500개 이상이 운영되고 있습니다. 이는 고령화와 핵가족화로 인해 집에서 노인을 돌보기 어려워진 사회 변화를 반영합니다. 베트남에서는 아직 이런 시설이 드물며, 노인은 가족이 집에서 돌보는 것이 일반적이므로, 한국의 요양병원 개념을 설명할 때 문화적 차이를 고려해야 합니다. 요양병원 입원비는 하루 평균 5~10만원 수준이며, 건강보험과 장기요양보험을 함께 적용받으면 실제 본인부담은 월 100~200만원 정도입니다. 일부 고급 요양병원은 비보험 진료를 많이 포함하여 비용이 훨씬 높을 수 있습니다.",
        "commonMistakes": [
            {
                "mistake": "'요양병원'과 '요양원'을 같은 용어로 번역",
                "correction": "요양병원은 'bệnh viện dưỡng lão'(의료기관), 요양원은 'viện dưỡng lão'(복지시설)",
                "explanation": "요양병원은 의사가 상주하는 의료기관이고, 요양원은 의료진 없이 돌봄만 제공하는 복지시설입니다"
            },
            {
                "mistake": "'재활병원'과 '요양병원'을 혼동",
                "correction": "재활병원은 'bệnh viện phục hồi chức năng'(집중 재활치료), 요양병원은 'bệnh viện dưỡng lão'(장기요양)",
                "explanation": "재활병원은 단기간 집중 재활치료를 목표로 하지만, 요양병원은 장기 요양과 생활 지원이 목적입니다"
            },
            {
                "mistake": "'요양병원'을 'bệnh viện nghỉ dưỡng'로 번역",
                "correction": "'bệnh viện dưỡng lão' 또는 'bệnh viện chăm sóc dài hạn'",
                "explanation": "'nghỉ dưỡng'는 휴양을 의미하지만, 요양병원은 의료적 돌봄을 제공하는 시설입니다"
            }
        ],
        "examples": [
            {
                "ko": "환자분 상태로는 요양병원에서 장기 치료를 받으시는 것이 좋겠습니다.",
                "vi": "Với tình trạng của bệnh nhân, nên điều trị dài hạn tại bệnh viện dưỡng lão.",
                "situation": "formal"
            },
            {
                "ko": "요양병원에서는 물리치료와 작업치료를 매일 받을 수 있어요.",
                "vi": "Ở bệnh viện dưỡng lão, có thể nhận vật lý trị liệu và trị liệu nghề nghiệp hàng ngày.",
                "situation": "onsite"
            },
            {
                "ko": "할머니를 집에서 모시기 힘들어서 요양병원에 모셨어요.",
                "vi": "Khó chăm sóc bà ở nhà nên đã đưa bà vào bệnh viện dưỡng lão.",
                "situation": "informal"
            }
        ],
        "relatedTerms": [
            "요양원",
            "재활병원",
            "장기요양보험",
            "방문간호",
            "만성질환"
        ]
    },
    {
        "slug": "cham-soc-cuoi-doi",
        "korean": "호스피스",
        "vietnamese": "Chăm sóc cuối đời",
        "hanja": None,
        "hanjaReading": None,
        "pronunciation": "짬 쏙 꾸이 도이",
        "meaningKo": "치유가 불가능한 말기 환자와 그 가족에게 통증 완화, 심리적·영적 지원, 임종 준비 등을 제공하는 전인적 돌봄 서비스입니다. 영어 'hospice'에서 온 외래어로, 한국에서는 주로 암환자 대상으로 시행되며, 2015년부터 건강보험이 적용됩니다. 통역 시 주의할 점은 호스피스가 '죽음을 준비하는 곳'이라는 부정적 인식을 완화하고, 삶의 질을 높이고 존엄한 죽음을 돕는 적극적 의료라는 점을 강조해야 한다는 것입니다. 한국에서는 완화의료(緩和醫療)라는 용어와 혼용되며, 입원형, 자문형, 가정형 세 가지 유형이 있습니다. 환자와 가족의 문화적·종교적 배경에 따라 임종 과정에 대한 인식이 크게 다르므로, 민감하게 접근해야 합니다.",
        "meaningVi": "Dịch vụ chăm sóc toàn diện cho bệnh nhân giai đoạn cuối không thể chữa khỏi và gia đình họ, bao gồm giảm đau, hỗ trợ tâm lý, tinh thần và chuẩn bị lâm chung. Từ tiếng Anh 'hospice', tại Hàn Quốc chủ yếu dành cho bệnh nhân ung thư giai đoạn cuối, được bảo hiểm y tế chi trả từ năm 2015. Có 3 loại: nội trú, tư vấn và chăm sóc tại nhà.",
        "context": "종양학, 완화의료, 임종 돌봄, 의료 윤리",
        "culturalNote": "한국 문화에서 죽음은 여전히 금기시되는 주제이며, 가족들이 환자에게 암 말기나 임종이 가까웠다는 사실을 알리지 않으려는 경향이 있습니다. 이는 '효(孝)' 사상과 관련이 있으며, 환자에게 심리적 부담을 주지 않으려는 배려입니다. 그러나 최근에는 환자의 알 권리와 자기결정권이 강조되면서 변화하고 있습니다. 베트남에서도 비슷한 문화적 특성이 있으며, 가족 중심의 의사결정이 일반적입니다. 한국의 호스피스 병동은 1인실 또는 2인실로 가족이 함께 머물 수 있도록 설계되어 있으며, 종교 시설(기도실, 법당)을 갖춘 곳도 많습니다. 호스피스 이용률은 아직 낮지만(암 사망자의 약 25%), 정부가 확대를 추진하고 있습니다.",
        "commonMistakes": [
            {
                "mistake": "'호스피스'를 'bệnh viện người sắp chết'로 번역",
                "correction": "'chăm sóc cuối đời' 또는 'chăm sóc giảm nhẹ giai đoạn cuối'",
                "explanation": "'người sắp chết'(죽을 사람)는 매우 부정적이고 무례한 표현이며, 'cuối đời'(인생의 마지막)가 존중하는 표현입니다"
            },
            {
                "mistake": "'호스피스'와 '안락사'를 혼동",
                "correction": "호스피스는 자연스러운 죽음 지원, 안락사는 의도적 생명 종결",
                "explanation": "호스피스는 통증 관리와 돌봄이 목적이며, 안락사는 한국에서 불법입니다(단, 연명의료중단은 합법)"
            },
            {
                "mistake": "'말기 환자'를 'bệnh nhân giai đoạn cuối'로만 번역",
                "correction": "맥락에 따라 'bệnh nhân không thể chữa khỏi' 또는 'bệnh nhân giai đoạn cuối'",
                "explanation": "'giai đoạn cuối'는 시간적 의미가 강하지만, 'không thể chữa khỏi'는 치유 불가능성을 강조합니다"
            }
        ],
        "examples": [
            {
                "ko": "환자분의 상태를 고려할 때 호스피스 병동으로 전원을 권유드립니다.",
                "vi": "Xét tình trạng của bệnh nhân, chúng tôi khuyến nghị chuyển sang khoa chăm sóc cuối đời.",
                "situation": "formal"
            },
            {
                "ko": "호스피스에서는 통증 관리와 함께 심리 상담도 받으실 수 있습니다.",
                "vi": "Tại khoa chăm sóc cuối đời, ngoài quản lý đau còn có tư vấn tâm lý.",
                "situation": "onsite"
            },
            {
                "ko": "아버지가 호스피스 병동에서 편안하게 마지막을 보내셨어요.",
                "vi": "Bố tôi đã trải qua những ngày cuối cùng một cách bình an tại khoa chăm sóc cuối đời.",
                "situation": "informal"
            }
        ],
        "relatedTerms": [
            "완화의료",
            "통증관리",
            "연명의료중단",
            "사전연명의료의향서",
            "임종돌봄"
        ]
    },
    {
        "slug": "y-te-giam-nhe",
        "korean": "완화의료",
        "vietnamese": "Y tế giảm nhẹ",
        "hanja": "緩和醫療",
        "hanjaReading": "완(느릴 완) + 화(화할 화) + 의(의원 의) + 료(고칠 료)",
        "pronunciation": "이 떼 잠 녜",
        "meaningKo": "생명을 위협하는 질환을 가진 환자와 가족의 통증 및 신체적·심리사회적·영적 문제를 조기에 발견하고 완벽하게 평가 및 치료함으로써 고통을 예방하고 완화하여 삶의 질을 향상시키는 의료입니다. 호스피스와 유사하지만, 완화의료는 질병의 초기 단계부터 적용 가능하며, 치료와 병행할 수 있다는 점에서 차이가 있습니다. 통역 시 주의할 점은 '완화'가 '포기'를 의미하지 않으며, 오히려 적극적으로 증상을 관리하고 삶의 질을 높이는 전문 의료 분야라는 점을 강조해야 한다는 것입니다. 통증 관리, 호흡곤란 완화, 오심·구토 조절, 영양 지원 등이 포함되며, 완화의료 전문의가 주도합니다.",
        "meaningVi": "Dịch vụ y tế nhằm phát hiện sớm, đánh giá và điều trị toàn diện các vấn đề về đau đớn, thể chất, tâm lý xã hội và tinh thần của bệnh nhân mắc bệnh đe dọa tính mạng và gia đình họ, từ đó phòng ngừa và giảm nhẹ đau khổ, nâng cao chất lượng cuộc sống. Khác với chăm sóc cuối đời, y tế giảm nhẹ có thể áp dụng từ giai đoạn đầu của bệnh và song hành với điều trị tích cực.",
        "context": "종양학, 만성질환 관리, 통증의학, 노인의학",
        "culturalNote": "한국에서 완화의료는 2000년대 후반부터 체계화되기 시작했으며, 2018년 '호스피스·완화의료 및 임종과정에 있는 환자의 연명의료결정에 관한 법률'(연명의료결정법)이 시행되면서 제도적 기반을 갖추었습니다. 이 법에 따라 말기 암, 후천성면역결핍증(AIDS), 만성 폐쇄성 호흡기질환, 만성 간경화 환자가 완화의료 대상입니다. 건강보험 적용으로 본인부담금이 5%로 낮아져 접근성이 향상되었습니다. 베트남에는 아직 완화의료 개념이 생소하며, 제도적 지원도 부족한 상황이므로, 한국의 시스템을 설명할 때 차이를 인지해야 합니다. 한국 의료진은 환자에게 직접 병명과 예후를 고지하는 것을 선호하지만, 베트남 문화권에서는 가족에게 먼저 알리는 것이 일반적입니다.",
        "commonMistakes": [
            {
                "mistake": "'완화의료'를 'điều trị làm dịu'로 번역",
                "correction": "'y tế giảm nhẹ' 또는 'chăm sóc giảm nhẹ'",
                "explanation": "'làm dịu'는 단순히 진정시킨다는 의미지만, 'giảm nhẹ'는 체계적인 증상 관리를 의미하는 전문 용어입니다"
            },
            {
                "mistake": "호스피스와 완화의료를 완전히 같은 것으로 설명",
                "correction": "완화의료는 넓은 개념, 호스피스는 말기 환자 대상 완화의료의 한 형태",
                "explanation": "완화의료는 질병 초기부터 적용 가능하지만, 호스피스는 주로 말기 환자를 대상으로 합니다"
            },
            {
                "mistake": "'완화'를 '포기'로 오해하는 표현 사용",
                "correction": "'적극적 증상 관리', '삶의 질 향상'으로 긍정적 의미 강조",
                "explanation": "완화의료는 치료 포기가 아니라 환자 중심의 적극적 의료 접근입니다"
            }
        ],
        "examples": [
            {
                "ko": "항암치료와 함께 완화의료팀의 도움을 받으시면 부작용 관리가 더 잘 됩니다.",
                "vi": "Nếu nhận hỗ trợ từ đội y tế giảm nhẹ cùng với hóa trị, việc quản lý tác dụng phụ sẽ tốt hơn.",
                "situation": "formal"
            },
            {
                "ko": "완화의료 전문의가 통증을 효과적으로 조절해드릴 거예요.",
                "vi": "Bác sĩ chuyên khoa y tế giảm nhẹ sẽ kiểm soát cơn đau hiệu quả.",
                "situation": "onsite"
            },
            {
                "ko": "어머니가 완화의료 받으면서 편안해 보이세요.",
                "vi": "Mẹ tôi trông thoải mái hơn khi nhận y tế giảm nhẹ.",
                "situation": "informal"
            }
        ],
        "relatedTerms": [
            "호스피스",
            "통증관리",
            "모르핀",
            "삶의질",
            "증상완화"
        ]
    },
    {
        "slug": "loet-do-ti-de",
        "korean": "욕창",
        "vietnamese": "Loét do tì đè",
        "hanja": "褥瘡",
        "hanjaReading": "욕(자리 욕) + 창(부스럼 창)",
        "pronunciation": "로엣 조 띠 데",
        "meaningKo": "장시간 같은 자세로 누워있거나 앉아있을 때 압력을 받는 부위의 피부와 조직이 손상되어 생기는 궤양입니다. 주로 뼈가 돌출된 부위(엉치뼈, 발꿈치, 엉덩이, 어깨뼈 등)에 발생하며, 중증의 경우 근육과 뼈까지 손상될 수 있습니다. 통역 시 주의할 점은 욕창이 단순히 '눌려서 생긴 상처'가 아니라 심각한 합병증을 유발할 수 있는 의학적 문제라는 점을 강조해야 한다는 것입니다. 특히 당뇨, 영양실조, 혈액순환 장애가 있는 환자는 욕창 발생 위험이 높고 치유가 어렵습니다. 예방이 가장 중요하며, 2시간마다 체위 변경, 압력 분산 매트리스 사용, 피부 청결 유지, 영양 관리 등이 핵심입니다. 욕창은 환자와 가족에게 경제적·심리적 부담을 주므로, 예방 교육이 매우 중요합니다.",
        "meaningVi": "Tổn thương da và mô dưới da do bị ép lâu ở cùng một vị trí khi nằm hoặc ngồi, hình thành loét. Thường xảy ra ở vùng xương nhô (xương cùng, gót chân, mông, xương vai). Nếu nặng có thể tổn thương đến cơ và xương. Bệnh nhân tiểu đường, suy dinh dưỡng, rối loạn tuần hoàn máu có nguy cơ cao. Phòng ngừa quan trọng hơn điều trị: thay đổi tư thế 2 giờ/lần, đệm phân tán áp lực, giữ da sạch, dinh dưỡng tốt.",
        "context": "간호, 재활의학, 노인의학, 중환자실",
        "culturalNote": "한국의 요양병원과 재가 돌봄 현장에서 욕창은 가장 흔하고 심각한 문제 중 하나입니다. 욕창 발생은 간호의 질을 나타내는 지표로 간주되며, 요양병원 평가 항목에도 포함됩니다. 욕창이 발생하면 치료 기간이 길고 비용이 많이 들며, 패혈증 등 치명적 합병증으로 이어질 수 있어 매우 중요합니다. 베트남에서도 노인 돌봄 시 욕창은 큰 문제이지만, 전문적인 예방 교육과 압력 분산 장비가 부족한 경우가 많습니다. 한국에서는 욕창 예방용 에어 매트리스, 체위 변경 보조 쿠션 등 다양한 의료기기가 개발되어 있으며, 장기요양보험으로 일부 대여할 수 있습니다. 가정에서 환자를 돌보는 가족에게 욕창 예방 교육을 제공하는 것이 간호사의 중요한 역할입니다.",
        "commonMistakes": [
            {
                "mistake": "'욕창'을 단순히 'vết loét'로 번역",
                "correction": "'loét do tì đè' 또는 'loét do nằm lâu'로 원인을 포함하여 번역",
                "explanation": "'vết loét'는 일반적인 궤양이지만, 욕창은 압력으로 인한 특수한 형태의 궤양입니다"
            },
            {
                "mistake": "'욕창 예방'을 '상처 예방'으로 일반화",
                "correction": "'phòng ngừa loét do tì đè'로 구체적으로 표현",
                "explanation": "욕창은 압력으로 인한 특수한 상처이므로, 일반적인 상처 예방과는 접근 방법이 다릅니다"
            },
            {
                "mistake": "욕창 단계를 설명 없이 숫자로만 전달",
                "correction": "1단계(da đỏ), 2단계(loét nông), 3단계(loét sâu), 4단계(lộ xương)로 설명",
                "explanation": "환자와 가족이 욕창의 심각성을 이해하려면 단계별 설명이 필요합니다"
            }
        ],
        "examples": [
            {
                "ko": "환자분 엉치뼈 부위에 2단계 욕창이 발생했습니다. 즉시 치료가 필요합니다.",
                "vi": "Bệnh nhân bị loét do tì đè giai đoạn 2 ở vùng xương cùng. Cần điều trị ngay.",
                "situation": "formal"
            },
            {
                "ko": "욕창 예방을 위해 2시간마다 환자분 자세를 바꿔드려야 합니다.",
                "vi": "Để phòng loét do tì đè, cần thay đổi tư thế bệnh nhân mỗi 2 giờ.",
                "situation": "onsite"
            },
            {
                "ko": "아버지 욕창이 생겨서 병원 다니는데, 낫는 데 오래 걸린대요.",
                "vi": "Bố tôi bị loét do tì đè nên phải đi bệnh viện, nghe nói lâu mới lành.",
                "situation": "informal"
            }
        ],
        "relatedTerms": [
            "체위변경",
            "에어매트리스",
            "압박괴사",
            "피부간호",
            "영양불량"
        ]
    },
    {
        "slug": "roi-loan-nuot",
        "korean": "연하장애",
        "vietnamese": "Rối loạn nuốt",
        "hanja": "嚥下障碍",
        "hanjaReading": "연(삼킬 연) + 하(아래 하) + 장(막을 장) + 애(거리낄 애)",
        "pronunciation": "조이 로안 누엇",
        "meaningKo": "음식이나 액체를 삼키는 과정에 문제가 생겨 정상적으로 삼키지 못하는 상태를 말합니다. 뇌졸중, 파킨슨병, 치매 등 신경계 질환이나 노화로 인해 발생하며, 심한 경우 흡인성 폐렴(음식이 기도로 들어가 생기는 폐렴)을 유발하여 생명에 위협이 될 수 있습니다. 통역 시 주의할 점은 환자와 가족이 '나이 들면 당연한 것'으로 여기지 않도록, 이것이 치료와 관리가 필요한 의학적 문제임을 명확히 해야 한다는 것입니다. 연하장애 환자에게는 음식 농도 조절(죽, 갈아먹기), 자세 교정, 연하재활 치료가 필요하며, 심한 경우 비위관(코로 영양 공급) 또는 위루관(배에 구멍 뚫어 영양 공급) 삽입을 고려합니다. 식사 시 사레 들림, 기침, 체중 감소, 식사 거부 등이 연하장애의 신호입니다.",
        "meaningVi": "Tình trạng gặp khó khăn trong quá trình nuốt thức ăn hoặc chất lỏng do đột quỵ, bệnh Parkinson, sa sút trí tuệ hoặc lão hóa. Nếu nặng có thể gây viêm phổi hít (do thức ăn vào đường thở), đe dọa tính mạng. Cần điều chỉnh độ đặc thức ăn (cháo, xay nhuyễn), tư thế ăn uống, và trị liệu phục hồi chức năng nuốt. Trường hợp nặng cần đặt ống thông dạ dày qua mũi hoặc qua thành bụng.",
        "context": "재활의학, 신경과, 노인의학, 언어치료",
        "culturalNote": "한국에서는 고령화로 인해 연하장애 환자가 급증하고 있으며, 요양병원과 재가 돌봄 현장에서 가장 중요한 간호 문제 중 하나입니다. 흡인성 폐렴은 노인 사망의 주요 원인이므로, 연하장애 조기 발견과 관리가 매우 중요합니다. 한국 전통 식문화는 국물이 많고 쌀밥 중심이어서, 연하장애 환자에게 적절한 식사 제공이 어려울 수 있습니다. 이에 따라 '연하보조식품'(농도 조절 식품)이 개발되어 시판되고 있습니다. 베트남 음식도 국물(phở, bún)이 많지만, 한국의 뜨거운 국물은 연하장애 환자에게 더 위험할 수 있으므로, 적절한 온도와 농도로 조절하는 것이 중요합니다. 언어치료사가 연하 평가와 재활을 담당하며, 건강보험 적용을 받을 수 있습니다.",
        "commonMistakes": [
            {
                "mistake": "'연하장애'를 단순히 'khó nuốt'로만 번역",
                "correction": "'rối loạn nuốt' 또는 'rối loạn chức năng nuốt'로 의학적 상태임을 명확히",
                "explanation": "'khó nuốt'는 일시적 어려움을 의미하지만, '연하장애'는 병리적 상태를 나타내는 전문 용어입니다"
            },
            {
                "mistake": "'사레 들림'과 '연하장애'를 같은 것으로 설명",
                "correction": "사레 들림(bị sặc)은 증상, 연하장애(rối loạn nuốt)는 질환",
                "explanation": "사레 들림은 연하장애의 증상 중 하나이지만, 연하장애는 더 포괄적인 개념입니다"
            },
            {
                "mistake": "'흡인성 폐렴'을 'viêm phổi do hít'로만 번역",
                "correction": "'viêm phổi hít' 또는 'viêm phổi do hít phải thức ăn/nước bọt'로 구체화",
                "explanation": "흡인성 폐렴의 원인(음식, 침 등이 기도로 들어감)을 명확히 해야 예방의 중요성이 전달됩니다"
            }
        ],
        "examples": [
            {
                "ko": "뇌졸중 후 연하장애가 있어 유동식으로 식단을 조절해야 합니다.",
                "vi": "Sau đột quỵ bị rối loạn nuốt nên phải điều chỉnh chế độ ăn thành thức ăn lỏng.",
                "situation": "formal"
            },
            {
                "ko": "식사 중 자주 사레 들리면 연하장애 검사를 받아보세요.",
                "vi": "Nếu thường xuyên bị sặc khi ăn, hãy kiểm tra rối loạn nuốt.",
                "situation": "onsite"
            },
            {
                "ko": "할아버지가 음식 삼키기 힘들어하셔서 다 갈아드려요.",
                "vi": "Ông tôi khó nuốt nên tôi xay nhuyễn hết thức ăn.",
                "situation": "informal"
            }
        ],
        "relatedTerms": [
            "흡인성폐렴",
            "비위관",
            "연하재활",
            "언어치료",
            "뇌졸중"
        ]
    },
    {
        "slug": "suy-nhuoc-tuoi-gia",
        "korean": "노쇠",
        "vietnamese": "Suy nhược tuổi già",
        "hanja": "老衰",
        "hanjaReading": "노(늙을 로) + 쇠(쇠할 쇠)",
        "pronunciation": "쑤이 뉴억 뚜이 지아",
        "meaningKo": "단순한 노화를 넘어서 신체의 예비능력이 현저히 감소하여 외부 스트레스에 취약해진 상태를 말합니다. 영어로 'frailty'라 하며, 근육량 감소(근감소증), 체중 감소, 피로, 보행속도 저하, 신체활동 감소 등이 특징입니다. 통역 시 주의할 점은 노쇠가 '자연스러운 노화'가 아니라 개입과 관리가 가능한 의학적 증후군이라는 점을 강조해야 한다는 것입니다. 노쇠한 노인은 낙상, 입원, 장애, 사망 위험이 높으며, 수술이나 질병 후 회복이 어렵습니다. 조기 발견과 다면적 중재(운동, 영양, 사회적 지원)가 중요하며, 한국의 노인건강검진에서 노쇠 선별검사를 시행합니다. 베트남어로 'frailty'를 직역한 명확한 용어는 없지만, 'suy nhược'(쇠약), 'yếu đuối tuổi già'(노년 허약) 등으로 표현할 수 있습니다.",
        "meaningVi": "Trạng thái dự trữ chức năng cơ thể giảm mạnh, dễ tổn thương trước stress bên ngoài, vượt quá lão hóa bình thường. Tiếng Anh gọi là 'frailty', đặc trưng bởi giảm khối cơ, giảm cân, mệt mỏi, đi chậm, ít hoạt động thể chất. Người cao tuổi suy nhược có nguy cơ cao bị ngã, nhập viện, tàn tật và tử vong. Can thiệp sớm (tập luyện, dinh dưỡng, hỗ trợ xã hội) rất quan trọng.",
        "context": "노인의학, 노인건강검진, 예방의학",
        "culturalNote": "한국에서 '노쇠'는 비교적 최근에 의학계와 정부가 주목하기 시작한 개념으로, 2018년부터 노인건강검진에 노쇠 선별검사가 도입되었습니다. 전통적으로 한국 사회에서는 노인의 쇠약을 '늙으면 당연한 것'으로 받아들였지만, 이제는 예방과 관리가 가능한 건강 문제로 인식이 변화하고 있습니다. 노쇠 예방을 위해서는 단백질 섭취(하루 체중 1kg당 1.0~1.2g), 근력 운동, 사회활동 참여가 중요합니다. 베트남에서는 아직 '노쇠'라는 개념이 의료 현장에서 널리 사용되지 않으므로, 통역 시 개념 설명이 필요합니다. 한국의 지역 보건소에서는 노쇠 예방 운동 프로그램을 무료로 제공하며, 영양 상담과 사회활동 지원도 연계하고 있습니다.",
        "commonMistakes": [
            {
                "mistake": "'노쇠'를 단순히 'già yếu'(늙고 약함)로 번역",
                "correction": "'suy nhược tuổi già' 또는 'hội chứng suy giảm chức năng tuổi già'로 의학적 증후군임을 명확히",
                "explanation": "'già yếu'는 일반적 표현이지만, 노쇠는 특정 기준이 있는 의학적 상태입니다"
            },
            {
                "mistake": "'프레일티(frailty)'를 음차 없이 그냥 사용",
                "correction": "'suy nhược'으로 번역하고 필요 시 괄호 안에 'frailty' 병기",
                "explanation": "의학 용어는 베트남어로 번역해야 환자가 이해할 수 있습니다"
            },
            {
                "mistake": "'근감소증'과 '노쇠'를 같은 것으로 설명",
                "correction": "근감소증(giảm khối cơ)은 노쇠의 핵심 요소이지만, 노쇠는 더 포괄적 개념",
                "explanation": "노쇠는 근육뿐 아니라 체중, 피로, 활동력 등 다면적 쇠약 상태를 포함합니다"
            }
        ],
        "examples": [
            {
                "ko": "노인건강검진 결과 노쇠 전단계로 나왔으니 운동과 영양 관리가 필요합니다.",
                "vi": "Kết quả khám sức khỏe người cao tuổi cho thấy giai đoạn tiền suy nhược, cần tập luyện và quản lý dinh dưỡng.",
                "situation": "formal"
            },
            {
                "ko": "노쇠 예방을 위해 매일 단백질 음식을 충분히 드시고 걷기 운동을 하세요.",
                "vi": "Để phòng ngừa suy nhược, hãy ăn đủ thực phẩm giàu protein mỗi ngày và đi bộ.",
                "situation": "onsite"
            },
            {
                "ko": "할머니가 요즘 부쩍 약해지신 것 같아요. 노쇠가 온 것 같아요.",
                "vi": "Gần đây bà tôi yếu hẳn đi. Có lẽ bị suy nhược rồi.",
                "situation": "informal"
            }
        ],
        "relatedTerms": [
            "근감소증",
            "노인건강검진",
            "단백질섭취",
            "근력운동",
            "낙상위험"
        ]
    }
]

def main():
    # 파일 읽기
    with open(file_path, 'r', encoding='utf-8') as f:
        data = json.load(f)

    # 기존 slug 목록 (중복 방지)
    existing_slugs = {term['slug'] for term in data}

    # 중복되지 않은 용어만 필터링
    terms_to_add = [term for term in new_terms if term['slug'] not in existing_slugs]

    if not terms_to_add:
        print("⚠️  모든 용어가 이미 존재합니다. 추가할 항목이 없습니다.")
        return

    # 용어 추가
    data.extend(terms_to_add)

    # 파일 저장 (indent=2, ensure_ascii=False로 한글 보존)
    with open(file_path, 'w', encoding='utf-8') as f:
        json.dump(data, f, indent=2, ensure_ascii=False)

    print(f"✅ {len(terms_to_add)}개의 노인의학 용어가 medical.json에 추가되었습니다.")
    print("\n추가된 용어:")
    for i, term in enumerate(terms_to_add, 1):
        print(f"  {i}. {term['korean']} ({term['vietnamese']})")

if __name__ == "__main__":
    main()
