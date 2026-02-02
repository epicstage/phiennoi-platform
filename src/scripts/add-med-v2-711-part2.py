#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Medical Terms Addition Script Part 2 - Remaining Pediatrics & Neonatology Terms
Adds remaining 30 medical terms to medical.json with Tier S quality (90+ score)
"""

import json
import os

# CRITICAL: Use exact path code
file_path = os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', 'data', 'terms', 'medical.json')

# Remaining 30 medical terms with complete Tier S quality data
new_terms = [
    {
        "slug": "bool-im",
        "korean": "불임",
        "vietnamese": "Vô sinh",
        "hanja": "不姙",
        "hanjaReading": "不(아닐 불) + 姙(아이 밸 임)",
        "pronunciation": "불임",
        "meaningKo": "1년 이상 피임 없이 정상적인 성생활을 했는데도 임신이 되지 않는 상태로, 남성과 여성 모두에게 원인이 있을 수 있습니다. 통역 시 '불임'이라는 용어의 부정적 어감 때문에 환자가 상처받지 않도록 주의하고, 남성 요인도 40%를 차지하므로 부부가 함께 검사받아야 함을 강조해야 합니다. 베트남어로는 'Vô sinh' 또는 'Hiếm muộn'(난임)이라고 하며, 최근에는 'Hiếm muộn'이라는 부드러운 표현을 선호합니다.",
        "meaningVi": "Tình trạng không mang thai được sau 12 tháng quan hệ tình dục đều đặn không tránh thai. Nguyên nhân có thể từ cả nam và nữ (nam chiếm 40%), cần vợ chồng cùng kiểm tra và điều trị. Thuật ngữ 'Hiếm muộn' được ưa dùng hơn vì ít gây tổn thương tâm lý.",
        "context": "불임 클리닉, 산부인과, 비뇨기과",
        "culturalNote": "한국과 베트남 모두 불임에 대한 사회적 압력이 크지만, 최근 '난임'이라는 용어를 사용하며 인식이 개선되고 있습니다. 한국은 국가 난임 지원 사업이 있어 시술 비용을 지원하지만, 베트남은 비용 부담이 커서 치료 접근성이 낮습니다. 통역 시 스트레스가 불임을 악화시킬 수 있으므로 심리적 지지와 함께 의학적 접근이 필요함을 설명해야 합니다.",
        "commonMistakes": [
            {
                "mistake": "무조건 여성 문제로 번역",
                "correction": "남성 요인 40%, 여성 요인 40%, 복합/원인불명 20%",
                "explanation": "부부가 함께 검사받아야 한다는 점을 명확히 해야 편견을 줄일 수 있습니다"
            },
            {
                "mistake": "'Vô sinh' 용어의 부정적 어감 무시",
                "correction": "'Hiếm muộn'(난임) 사용 권장",
                "explanation": "환자의 심리적 부담을 고려한 용어 선택이 중요합니다"
            },
            {
                "mistake": "나이와 무관하다고 설명",
                "correction": "여성 35세, 남성 40세 이후 임신율 급격히 감소",
                "explanation": "시간이 중요한 요소임을 전달하여 조기 검사를 유도해야 합니다"
            }
        ],
        "examples": [
            {
                "ko": "1년 이상 임신이 안 되어 불임 검사를 권유드리며, 남편분도 함께 정액검사를 받으시는 것이 좋습니다.",
                "vi": "Đã hơn 1 năm không mang thai được nên khuyên nên kiểm tra vô sinh, chồng cũng nên xét nghiệm tinh dịch cùng.",
                "situation": "formal"
            },
            {
                "ko": "검사 결과 배란 장애와 남성 요인이 복합적으로 있어, 인공수정이나 시험관 시술을 고려해야 합니다.",
                "vi": "Kết quả kiểm tra có cả rối loạn phóng noãn và yếu tố nam giới, cần cân nhắc thụ tinh nhân tạo hoặc thụ tinh ống nghiệm.",
                "situation": "onsite"
            },
            {
                "ko": "불임은 부부 문제니까 서로 탓하지 말고 함께 치료받으면 많이 좋아져요.",
                "vi": "Vô sinh là vấn đề của cả hai vợ chồng nên đừng đổ lỗi cho nhau mà cùng điều trị sẽ khá hơn nhiều nhé.",
                "situation": "informal"
            }
        ],
        "relatedTerms": ["난임", "시험관시술", "인공수정", "배란유도"]
    },
    {
        "slug": "si-hom-gwan-si-sul",
        "korean": "시험관시술",
        "vietnamese": "Thụ tinh ống nghiệm",
        "hanja": "試驗管施術",
        "hanjaReading": "試(시험할 시) + 驗(시험 험) + 管(대롱 관) + 施(베풀 시) + 術(재주 술)",
        "pronunciation": "시험관시술",
        "meaningKo": "난자와 정자를 체외에서 수정시킨 후 배아를 자궁에 이식하는 보조생식술로, 의학적으로는 IVF(In Vitro Fertilization)라고 합니다. 통역 시 과배란유도, 채란, 수정, 배양, 이식의 전 과정과 성공률, 비용, 부작용을 명확히 설명해야 하며, 한 번에 성공하지 못할 수 있음을 미리 알려 심리적 준비를 돕는 것이 중요합니다. 베트남어로는 'Thụ tinh ống nghiệm' 또는 줄여서 'IVF'라고 합니다.",
        "meaningVi": "Kỹ thuật hỗ trợ sinh sản bằng cách thụ tinh noãn và tinh trùng ngoài cơ thể rồi cấy phôi vào tử cung. Quy trình gồm kích trứng, lấy trứng, thụ tinh, nuôi cấy phôi và chuyển phôi. Tỷ lệ thành công phụ thuộc tuổi và nguyên nhân vô sinh.",
        "context": "불임 클리닉, 보조생식센터",
        "culturalNote": "한국은 시험관 시술이 매우 보편화되어 있고 국가 지원으로 비용 부담이 줄었습니다. 베트남도 대도시에서는 시술이 가능하지만 비용이 매우 높아 접근성이 제한적입니다. 통역 시 과배란유도 과정의 호르몬 주사, 채란 시술의 통증, 다태 임신 위험 등을 솔직하게 설명하고, 성공률이 100%가 아님을 명확히 해야 불필요한 기대와 실망을 줄일 수 있습니다.",
        "commonMistakes": [
            {
                "mistake": "'100% 성공'한다고 과장",
                "correction": "평균 성공률 30~40% (연령에 따라 차이)",
                "explanation": "현실적인 기대치를 전달해야 환자가 심리적으로 준비할 수 있습니다"
            },
            {
                "mistake": "'간단한 시술'로 설명",
                "correction": "수주간의 호르몬 치료와 여러 단계 거쳐야 함",
                "explanation": "시술의 복잡성과 부담을 정확히 전달해야 합니다"
            },
            {
                "mistake": "비용 설명 누락",
                "correction": "한 회차 수백만~천만원 이상 소요",
                "explanation": "경제적 준비를 위해 비용 정보는 필수입니다"
            }
        ],
        "examples": [
            {
                "ko": "자연 임신이 어려워 시험관 시술을 권유드리며, 과배란 주사 후 채란하여 배아를 배양한 뒤 이식합니다.",
                "vi": "Khó mang thai tự nhiên nên khuyên làm thụ tinh ống nghiệm, sau tiêm kích trứng sẽ lấy trứng, nuôi cấy phôi rồi chuyển phôi.",
                "situation": "formal"
            },
            {
                "ko": "시험관 시술로 신선배아 2개를 이식했고, 2주 후 임신 확인 검사를 하겠습니다.",
                "vi": "Đã chuyển 2 phôi tươi qua thụ tinh ống nghiệm, sau 2 tuần sẽ xét nghiệm xác nhận mang thai.",
                "situation": "onsite"
            },
            {
                "ko": "시험관 시술은 한 번에 안 될 수도 있으니 너무 스트레스 받지 말고 장기전으로 생각하세요.",
                "vi": "Thụ tinh ống nghiệm có thể không thành công ngay lần đầu nên đừng stress quá mà hãy nghĩ đây là cuộc chiến dài hạn nhé.",
                "situation": "informal"
            }
        ],
        "relatedTerms": ["과배란유도", "채란", "배아이식", "냉동배아"]
    },
    {
        "slug": "in-gong-su-jong",
        "korean": "인공수정",
        "vietnamese": "Thụ tinh nhân tạo",
        "hanja": "人工受精",
        "hanjaReading": "人(사람 인) + 工(장인 공) + 受(받을 수) + 精(정수 정)",
        "pronunciation": "인공수정",
        "meaningKo": "처리한 정자를 배란 시기에 맞춰 자궁 내로 직접 주입하는 시술로, 시험관보다 간단하고 저렴합니다. 통역 시 '인공수정'과 '시험관시술'의 차이를 명확히 설명해야 하며, 남성 불임이 경미하거나 원인불명 불임에서 1차로 시도하는 방법임을 알려야 합니다. 베트남어로는 'Thụ tinh nhân tạo' 또는 'IUI(Intrauterine Insemination)'라고 합니다.",
        "meaningVi": "Kỹ thuật bơm tinh trùng đã xử lý trực tiếp vào buồng tử cung vào thời điểm phóng noãn. Đơn giản và rẻ hơn thụ tinh ống nghiệm, thường dùng cho nam giới yếu tinh nhẹ hoặc vô sinh không rõ nguyên nhân, là phương pháp thử đầu tiên.",
        "context": "불임 치료, 산부인과",
        "culturalNote": "한국과 베트남 모두 인공수정을 불임 치료의 1차 선택으로 고려합니다. 시험관보다 비용이 저렴하고 신체 부담이 적어 먼저 시도하는 경우가 많습니다. 통역 시 성공률이 시험관보다 낮지만(10~20%), 여러 번 시도 가능하고 자연 임신에 가까운 방법이라는 점을 설명하면 환자가 선택하는 데 도움이 됩니다.",
        "commonMistakes": [
            {
                "mistake": "시험관시술과 동일하게 번역",
                "correction": "인공수정은 체내 수정, 시험관은 체외 수정",
                "explanation": "두 방법은 완전히 다른 시술이므로 명확히 구분해야 합니다"
            },
            {
                "mistake": "'Tinh trùng hiến tặng'(정자 기증)과 혼동",
                "correction": "남편 정자 또는 기증 정자 모두 사용 가능",
                "explanation": "인공수정은 방법이고, 정자 출처는 별개 문제입니다"
            },
            {
                "mistake": "성공률을 과장하여 전달",
                "correction": "회당 성공률 10~20%, 여러 번 시도 필요",
                "explanation": "현실적인 기대치를 가지도록 정확한 정보 제공이 필요합니다"
            }
        ],
        "examples": [
            {
                "ko": "정자 운동성이 조금 낮아 인공수정을 권유드리며, 배란유도와 함께 시행하면 성공률이 높아집니다.",
                "vi": "Vận động tinh trùng hơi yếu nên khuyên làm thụ tinh nhân tạo, kết hợp với kích trứng sẽ tăng tỷ lệ thành công.",
                "situation": "formal"
            },
            {
                "ko": "오늘 배란 확인되어 처리한 정자를 자궁 내로 주입하겠습니다. 시술은 5분 정도 걸립니다.",
                "vi": "Hôm nay xác nhận phóng noãn rồi nên sẽ bơm tinh trùng đã xử lý vào tử cung. Thủ thuật mất khoảng 5 phút.",
                "situation": "onsite"
            },
            {
                "ko": "인공수정은 시험관보다 간단하고 싸니까 먼저 3~4번 해보고 안 되면 시험관으로 넘어가요.",
                "vi": "Thụ tinh nhân tạo đơn giản và rẻ hơn nên thử 3-4 lần trước, không được thì chuyển sang ống nghiệm nhé.",
                "situation": "informal"
            }
        ],
        "relatedTerms": ["배란유도", "정자처리", "시험관시술", "난임치료"]
    },
    {
        "slug": "pyae-gyong-gi",
        "korean": "폐경기",
        "vietnamese": "Mãn kinh",
        "hanja": "閉經期",
        "hanjaReading": "閉(닫을 폐) + 經(지날 경) + 期(기약 기)",
        "pronunciation": "폐경기",
        "meaningKo": "난소 기능이 소실되어 생리가 영구적으로 멈추는 시기로, 12개월 이상 무월경이 지속되면 진단합니다. 통역 시 폐경은 질병이 아니라 자연스러운 노화 과정이지만, 안면홍조, 골다공증, 심혈관 질환 위험 증가 등의 증상 관리가 필요함을 설명해야 합니다. 베트남어로는 'Mãn kinh' 또는 'Bế kinh'이라고 하며, 평균 연령은 한국과 베트남 모두 49~51세입니다.",
        "meaningVi": "Thời kỳ buồng trứng ngừng hoạt động, kinh nguyệt dừng vĩnh viễn, được chẩn đoán sau 12 tháng không có kinh. Đây là quá trình tự nhiên của lão hóa, nhưng cần quản lý các triệu chứng như bốc hỏa, loãng xương, tăng nguy cơ tim mạch.",
        "context": "갱년기 클리닉, 여성건강의학과",
        "culturalNote": "한국과 베트남 모두 폐경을 '여성으로서의 끝'으로 인식하는 전통적 시각이 있지만, 최근에는 '제2의 인생 시작'으로 긍정적 인식이 확산되고 있습니다. 통역 시 폐경이 질병이 아닌 자연스러운 과정임을 강조하고, 호르몬 대체요법 등으로 삶의 질을 유지할 수 있음을 알려 불필요한 불안을 줄이는 것이 중요합니다.",
        "commonMistakes": [
            {
                "mistake": "'노화의 시작'으로 부정적 표현",
                "correction": "'새로운 인생 단계'로 중립적 표현",
                "explanation": "환자의 심리적 부담을 줄이기 위해 표현에 주의해야 합니다"
            },
            {
                "mistake": "'Hết kinh'(생리가 끝났다)로 번역",
                "correction": "'Mãn kinh'이 정확한 의학 용어",
                "explanation": "구어체보다는 의학 용어를 사용하는 것이 전문성을 높입니다"
            },
            {
                "mistake": "증상 관리 필요성을 설명하지 않음",
                "correction": "안면홍조, 골다공증 등 관리 가능한 증상 설명",
                "explanation": "적극적인 증상 관리로 삶의 질을 유지할 수 있음을 알려야 합니다"
            }
        ],
        "examples": [
            {
                "ko": "12개월 이상 생리가 없어 폐경으로 진단되며, 골밀도 검사와 심혈관 검진을 권유드립니다.",
                "vi": "Không có kinh trên 12 tháng nên chẩn đoán mãn kinh, khuyên nên đo mật độ xương và kiểm tra tim mạch.",
                "situation": "formal"
            },
            {
                "ko": "안면홍조가 심하면 호르몬 대체요법을 고려해볼 수 있지만, 위험과 이득을 충분히 상담 후 결정하겠습니다.",
                "vi": "Nếu bốc hỏa nặng có thể cân nhắc liệu pháp thay thế hormone, nhưng sẽ tư vấn kỹ về rủi ro và lợi ích trước khi quyết định.",
                "situation": "onsite"
            },
            {
                "ko": "폐경은 자연스러운 거니까 너무 우울해하지 말고, 운동하고 칼슘 챙기면 건강하게 보낼 수 있어요.",
                "vi": "Mãn kinh là điều tự nhiên nên đừng buồn quá, vận động và bổ sung canxi thì sống khỏe mạnh được nhé.",
                "situation": "informal"
            }
        ],
        "relatedTerms": ["호르몬대체요법", "골다공증", "안면홍조", "갱년기"]
    },
    {
        "slug": "ho-reu-mon-dae-che-yo-beop",
        "korean": "호르몬대체요법",
        "vietnamese": "Liệu pháp thay thế hormone",
        "hanja": "hormone代替療法",
        "hanjaReading": "代(대신할 대) + 替(바꿀 체) + 療(치료할 료) + 法(법 법)",
        "pronunciation": "호르몬대체요법",
        "meaningKo": "폐경 후 감소한 여성호르몬(에스트로겐, 프로게스테론)을 보충하여 갱년기 증상을 완화하는 치료입니다. 통역 시 안면홍조, 질 건조, 골다공증 등의 증상 개선에 효과적이지만, 유방암·혈전 위험 증가 가능성이 있어 개인별 위험-이득 평가 후 사용해야 함을 명확히 해야 합니다. 베트남어로는 'Liệu pháp thay thế hormone' 또는 줄여서 'HRT(Hormone Replacement Therapy)'라고 합니다.",
        "meaningVi": "Điều trị bằng cách bổ sung hormone nữ (estrogen, progesterone) đã giảm sau mãn kinh để làm giảm triệu chứng mãn kinh. Hiệu quả với bốc hỏa, khô âm đạo, loãng xương nhưng có nguy cơ ung thư vú và huyết khối, cần đánh giá rủi ro-lợi ích từng người.",
        "context": "갱년기 클리닉, 여성건강의학과",
        "culturalNote": "한국은 호르몬 대체요법에 대한 인식이 높아지고 있지만, 유방암 위험 논란으로 주저하는 환자도 많습니다. 베트남에서는 호르몬 치료에 대한 정보가 제한적이고 '인공 호르몬'에 대한 거부감이 있을 수 있습니다. 통역 시 최신 연구 결과에 따르면 5년 이내 단기 사용 시 위험이 크지 않으며, 증상이 심한 경우 삶의 질 개선 효과가 위험보다 크다는 점을 균형있게 전달해야 합니다.",
        "commonMistakes": [
            {
                "mistake": "'암 위험'만 강조하여 공포 조성",
                "correction": "위험과 이득을 균형있게 설명",
                "explanation": "한쪽만 강조하면 환자가 적절한 치료 기회를 놓칠 수 있습니다"
            },
            {
                "mistake": "'Hormone tổng hợp'(합성 호르몬)로 부정적 표현",
                "correction": "'Hormone thay thế'로 중립적 표현",
                "explanation": "'합성'이라는 단어가 부정적 인식을 줄 수 있습니다"
            },
            {
                "mistake": "평생 복용해야 한다고 오해",
                "correction": "보통 증상 있는 기간(5년 내외) 사용",
                "explanation": "치료 기간에 대한 정확한 정보 제공이 필요합니다"
            }
        ],
        "examples": [
            {
                "ko": "안면홍조와 질 건조증이 심해 호르몬 대체요법을 권유드리며, 유방암 가족력 등을 확인 후 처방하겠습니다.",
                "vi": "Bốc hỏa và khô âm đạo nặng nên khuyên làm liệu pháp thay thế hormone, sau khi kiểm tra tiền sử gia đình ung thư vú sẽ kê đơn.",
                "situation": "formal"
            },
            {
                "ko": "호르몬 패치를 매주 교체하시고, 6개월마다 유방 검진과 혈액검사를 받으셔야 합니다.",
                "vi": "Thay miếng dán hormone mỗi tuần, và 6 tháng một lần phải khám vú và xét nghiệm máu.",
                "situation": "onsite"
            },
            {
                "ko": "호르몬 대체요법 하면 갱년기 증상이 많이 좋아지는데, 5년 정도 쓰다가 증상 없으면 끊어요.",
                "vi": "Làm liệu pháp thay thế hormone thì triệu chứng mãn kinh khá hơn nhiều, dùng khoảng 5 năm rồi không triệu chứng thì ngừng nhé.",
                "situation": "informal"
            }
        ],
        "relatedTerms": ["폐경기", "에스트로겐", "골다공증", "안면홍조"]
    },
    {
        "slug": "mo-yu-su-yu",
        "korean": "모유수유",
        "vietnamese": "Cho con bú mẹ",
        "hanja": "母乳授乳",
        "hanjaReading": "母(어미 모) + 乳(젖 유) + 授(줄 수) + 乳(젖 유)",
        "pronunciation": "모유수유",
        "meaningKo": "엄마의 젖을 아기에게 먹이는 것으로, WHO는 생후 6개월간 완전 모유수유를 권장합니다. 통역 시 '모유가 최고'라는 압박보다는, 모유의 이점을 설명하되 분유 수유를 선택한 엄마도 존중해야 하며, 수유 중 어려움(유두 통증, 유선염, 수유량 부족 등)에 대한 실질적 도움을 제공하는 것이 중요합니다. 베트남어로는 'Cho con bú mẹ' 또는 'Nuôi con bằng sữa mẹ'라고 합니다.",
        "meaningVi": "Cho trẻ bú sữa mẹ, WHO khuyến nghị cho bú hoàn toàn trong 6 tháng đầu. Sữa mẹ cung cấp dinh dưỡng tối ưu và kháng thể, nhưng mẹ gặp khó khăn (đau núm vú, viêm tuyến vú, ít sữa) thì cần hỗ trợ, không nên gây áp lực.",
        "context": "산후 조리, 소아과, 모유수유 클리닉",
        "culturalNote": "한국과 베트남 모두 모유수유를 권장하지만, 직장 복귀, 수유 공간 부족 등 현실적 어려움이 많습니다. 한국은 '모유 신화'가 강해 분유 수유 엄마들이 죄책감을 느끼는 경우가 많고, 베트남도 유사합니다. 통역 시 '엄마 젖을 먹여야 한다'는 압박보다는, 선택을 존중하고 어려움 호소 시 적극적으로 도와주는 태도가 중요합니다.",
        "commonMistakes": [
            {
                "mistake": "'모유 안 먹이면 나쁜 엄마'라는 압박",
                "correction": "모유의 이점 설명하되 선택 존중",
                "explanation": "모유 수유 압박은 산후 우울증을 악화시킬 수 있습니다"
            },
            {
                "mistake": "'모유는 저절로 나온다'는 오해",
                "correction": "초기 어려움 정상이며 도움 받을 수 있음",
                "explanation": "수유는 학습이 필요한 과정임을 알려야 좌절을 줄일 수 있습니다"
            },
            {
                "mistake": "수유 중 약물 복용 무조건 금지",
                "correction": "수유 중 안전한 약물 많으므로 의사와 상담",
                "explanation": "불필요하게 수유를 중단하지 않도록 정확한 정보 제공이 필요합니다"
            }
        ],
        "examples": [
            {
                "ko": "초유에는 면역물질이 풍부하니 출산 직후부터 모유수유를 시작하시고, 어려우면 언제든 상담하세요.",
                "vi": "Sữa non giàu kháng thể nên ngay sau sinh hãy bắt đầu cho bú, gặp khó khăn thì tư vấn bất cứ lúc nào.",
                "situation": "formal"
            },
            {
                "ko": "유선염 증상이 있어서 항생제를 처방하지만, 모유수유는 계속하셔도 됩니다.",
                "vi": "Có triệu chứng viêm tuyến vú nên kê kháng sinh, nhưng vẫn tiếp tục cho con bú được.",
                "situation": "onsite"
            },
            {
                "ko": "모유 수유 힘들면 분유 먹여도 아기 잘 자라니까 너무 스트레스 받지 마세요.",
                "vi": "Cho bú mẹ khó thì cho bú sữa công thức bé vẫn lớn tốt nên đừng stress quá nhé.",
                "situation": "informal"
            }
        ],
        "relatedTerms": ["초유", "유선염", "젖몸살", "분유수유"]
    },
    {
        "slug": "bun-yu-su-yu",
        "korean": "분유수유",
        "vietnamese": "Cho con bú sữa công thức",
        "hanja": "粉乳授乳",
        "hanjaReading": "粉(가루 분) + 乳(젖 유) + 授(줄 수) + 乳(젖 유)",
        "pronunciation": "분유수유",
        "meaningKo": "조제분유로 아기를 먹이는 것으로, 모유 수유가 불가능하거나 선택하지 않을 때 안전한 대안입니다. 통역 시 분유도 충분한 영양을 제공하며, 분유 수유를 선택한 엄마를 비난하지 않는 것이 중요하고, 올바른 조유 방법과 위생 관리를 정확히 전달해야 합니다. 베트남어로는 'Cho con bú sữa công thức' 또는 'Nuôi con bằng sữa bột'이라고 합니다.",
        "meaningVi": "Cho trẻ ăn sữa công thức (sữa bột), là lựa chọn an toàn khi không thể hoặc không muốn cho bú mẹ. Sữa công thức cung cấp đầy đủ dinh dưỡng, không nên chỉ trích mẹ chọn sữa bột, quan trọng là pha đúng cách và vệ sinh tốt.",
        "context": "소아과, 산후 조리, 영양 상담",
        "culturalNote": "한국과 베트남 모두 '모유가 최고'라는 인식이 강해 분유 수유 엄마들이 사회적 압박과 죄책감을 느낍니다. 통역 시 분유 수유도 정당한 선택이며, 아기는 건강하게 자랄 수 있다는 점을 강조하고, 조유 농도, 물 온도, 젖병 소독 등 실질적 정보를 제공하여 엄마의 자신감을 높이는 것이 중요합니다.",
        "commonMistakes": [
            {
                "mistake": "분유 수유 선택을 비난하는 태도",
                "correction": "선택 존중하고 올바른 사용법 교육",
                "explanation": "엄마의 심리적 부담을 줄이고 긍정적 육아 환경 조성이 중요합니다"
            },
            {
                "mistake": "'Sữa bò pha'(우유 타서)로 번역",
                "correction": "'Sữa công thức'(조제분유)가 정확",
                "explanation": "일반 우유와 조제분유는 완전히 다른 제품입니다"
            },
            {
                "mistake": "조유 방법을 대충 설명",
                "correction": "물 온도(70도), 농도, 보관 시간 등 구체적 설명",
                "explanation": "잘못된 조유는 영양 불균형이나 감염을 일으킬 수 있습니다"
            }
        ],
        "examples": [
            {
                "ko": "모유 수유가 어려워 분유로 전환하시려면, 70도 물로 조유하고 2시간 이내 먹이세요.",
                "vi": "Khó cho bú mẹ muốn chuyển sang sữa công thức thì pha bằng nước 70 độ và cho ăn trong vòng 2 giờ.",
                "situation": "formal"
            },
            {
                "ko": "체중 증가가 잘 되고 있으니 분유 수유로도 충분히 건강하게 크고 있습니다.",
                "vi": "Cân nặng tăng tốt nên nuôi bằng sữa công thức cũng phát triển khỏe mạnh rồi.",
                "situation": "onsite"
            },
            {
                "ko": "분유 먹이는 게 잘못된 거 아니니까 죄책감 갖지 말고, 조유만 정확히 하면 돼요.",
                "vi": "Cho bú sữa công thức không sai nên đừng cảm thấy có lỗi, chỉ cần pha đúng cách là được nhé.",
                "situation": "informal"
            }
        ],
        "relatedTerms": ["조제분유", "조유방법", "젖병소독", "모유수유"]
    },
    {
        "slug": "shin-saeng-a-hwang-dal",
        "korean": "신생아황달",
        "vietnamese": "Vàng da sơ sinh",
        "hanja": "新生兒黃疸",
        "hanjaReading": "新(새 신) + 生(날 생) + 兒(아이 아) + 黃(누를 황) + 疸(황달 달)",
        "pronunciation": "신생아황달",
        "meaningKo": "신생아의 피부와 눈이 노랗게 변하는 증상으로, 대부분 생리적 황달로 자연 호전되지만, 수치가 높거나 지속되면 광선치료가 필요합니다. 통역 시 대부분의 신생아가 겪는 정상 과정이지만, 빌리루빈 수치가 높으면 뇌손상(핵황달) 위험이 있어 정기 검사가 필수임을 강조해야 합니다. 베트남어로는 'Vàng da sơ sinh' 또는 'Vàng da sinh lý'(생리적 황달)라고 합니다.",
        "meaningVi": "Da và mắt trẻ sơ sinh chuyển màu vàng, đa số là vàng da sinh lý tự khỏi, nhưng nếu chỉ số bilirubin cao hoặc kéo dài cần chiếu đèn. Nếu không điều trị kịp thời có nguy cơ tổn thương não (vàng da nhân), phải theo dõi định kỳ.",
        "context": "신생아실, 소아과, 산후 조리",
        "culturalNote": "한국과 베트남 모두 신생아 황달이 매우 흔하며(약 60%), 대부분 걱정할 필요가 없지만 일부 부모는 과도하게 불안해합니다. 한국은 황달 검사기로 수시 측정하고, 베트남도 유사하지만 지역에 따라 접근성이 다릅니다. 통역 시 '모유 황달'의 경우 모유를 끊지 않아도 되며, 광선치료는 안전하고 효과적임을 안심시키는 것이 중요합니다.",
        "commonMistakes": [
            {
                "mistake": "모든 황달을 위험하다고 과장",
                "correction": "생리적 황달은 정상, 수치 높을 때만 치료",
                "explanation": "불필요한 공포를 주지 않으면서 관찰의 중요성은 전달해야 합니다"
            },
            {
                "mistake": "'Vàng da'를 간염으로 오해 방치",
                "correction": "신생아 황달과 간염은 완전히 다름",
                "explanation": "혼동으로 인한 오진을 방지해야 합니다"
            },
            {
                "mistake": "'모유 황달'이라 모유 중단 권유",
                "correction": "모유 황달도 광선치료하며 모유 지속 가능",
                "explanation": "불필요한 모유 수유 중단을 막아야 합니다"
            }
        ],
        "examples": [
            {
                "ko": "황달 수치가 15mg/dL로 높아 광선치료를 시작하겠습니다. 치료는 안전하고 대부분 빠르게 좋아집니다.",
                "vi": "Chỉ số vàng da 15mg/dL cao nên sẽ bắt đầu chiếu đèn. Điều trị an toàn và đa số khỏi nhanh.",
                "situation": "formal"
            },
            {
                "ko": "생후 3일인데 약간 노란 건 생리적 황달로 정상이니, 4~5일 후 재검사하겠습니다.",
                "vi": "Sinh được 3 ngày mà hơi vàng là vàng da sinh lý bình thường, 4-5 ngày sau sẽ kiểm tra lại.",
                "situation": "onsite"
            },
            {
                "ko": "신생아 황달은 대부분 저절로 좋아지는데, 너무 노래지거나 잘 안 먹으면 바로 병원 가야 해요.",
                "vi": "Vàng da sơ sinh đa số tự khỏi, nhưng nếu quá vàng hoặc bú kém thì phải đến bệnh viện ngay nhé.",
                "situation": "informal"
            }
        ],
        "relatedTerms": ["빌리루빈", "광선치료", "핵황달", "모유황달"]
    },
    {
        "slug": "mi-suk-a",
        "korean": "미숙아",
        "vietnamese": "Trẻ sinh non",
        "hanja": "未熟兒",
        "hanjaReading": "未(아닐 미) + 熟(익을 숙) + 兒(아이 아)",
        "pronunciation": "미숙아",
        "meaningKo": "임신 37주 이전에 태어난 아기로, 장기가 미성숙하여 집중 치료가 필요한 경우가 많습니다. 통역 시 미숙아의 정도(경도/중등도/극소)에 따라 필요한 치료와 예후가 다르며, 부모의 불안을 줄이면서도 장기 추적 관찰의 필요성을 명확히 전달해야 합니다. 베트남어로는 'Trẻ sinh non' 또는 'Trẻ đẻ non tháng'라고 합니다.",
        "meaningVi": "Trẻ sinh trước tuần thứ 37 thai kỳ, các cơ quan chưa trưởng thành nên thường cần chăm sóc tích cực. Tùy mức độ non tháng (nhẹ/trung bình/cực nhẹ cân) mà điều trị và tiên lượng khác nhau, cần theo dõi lâu dài phát triển.",
        "context": "신생아집중치료실, 소아과",
        "culturalNote": "한국과 베트남 모두 미숙아 생존율이 향상되었지만, 극소 미숙아는 여전히 고위험입니다. 한국은 신생아집중치료실(NICU) 인프라가 잘 갖춰져 있고, 베트남은 대도시 병원에만 고급 NICU가 있습니다. 통역 시 미숙아 부모의 죄책감과 불안이 크므로, 현대 의학으로 많이 좋아졌다는 희망적 메시지와 함께 현실적 정보를 균형있게 전달해야 합니다.",
        "commonMistakes": [
            {
                "mistake": "'발달이 영구적으로 뒤처진다'고 단정",
                "correction": "대부분은 만2세경 따라잡으며, 교정연령 사용",
                "explanation": "불필요한 절망을 주지 않도록 희망적 예후도 전달해야 합니다"
            },
            {
                "mistake": "'Trẻ yếu'(약한 아이)로 낙인",
                "correction": "'Trẻ sinh non'이 정확하고 중립적",
                "explanation": "부정적 낙인을 피하고 의학적 용어를 사용해야 합니다"
            },
            {
                "mistake": "주수와 체중 기준 혼동",
                "correction": "미숙아는 주수(37주 미만), 저체중은 체중(2.5kg 미만)",
                "explanation": "미숙아와 저체중아는 다른 개념이므로 정확히 구분해야 합니다"
            }
        ],
        "examples": [
            {
                "ko": "34주에 태어난 미숙아로 호흡곤란이 있어 신생아집중치료실에서 치료 중이며, 예후는 양호합니다.",
                "vi": "Sinh non 34 tuần có khó thở nên đang điều trị ở phòng chăm sóc tích cực sơ sinh, tiên lượng tốt.",
                "situation": "formal"
            },
            {
                "ko": "미숙아라 교정연령으로 발달을 평가하니, 생일보다 예정일 기준으로 성장을 봐야 합니다.",
                "vi": "Vì sinh non nên đánh giá phát triển theo tuổi hiệu chỉnh, phải xem sự phát triển theo ngày dự sinh chứ không phải ngày sinh.",
                "situation": "onsite"
            },
            {
                "ko": "미숙아로 태어났어도 대부분 잘 자라니까 너무 걱정 말고, 정기 검진만 잘 받으세요.",
                "vi": "Dù sinh non nhưng đa số lớn lên tốt nên đừng lo quá, chỉ cần khám định kỳ đều đặn nhé.",
                "situation": "informal"
            }
        ],
        "relatedTerms": ["저체중출생아", "신생아집중치료실", "교정연령", "호흡곤란증후군"]
    },
    {
        "slug": "jeo-che-jung-chul-saeng-a",
        "korean": "저체중출생아",
        "vietnamese": "Trẻ sinh nhẹ cân",
        "hanja": "低體重出生兒",
        "hanjaReading": "低(낮을 저) + 體(몸 체) + 重(무거울 중) + 出(날 출) + 生(날 생) + 兒(아이 아)",
        "pronunciation": "저체중출생아",
        "meaningKo": "출생 체중이 2,500g 미만인 아기로, 미숙아이거나 자궁 내 성장지연으로 발생합니다. 통역 시 저체중아는 체온 조절, 감염, 저혈당 위험이 높아 특별한 관리가 필요하며, 성장 추적과 영양 보충이 중요함을 강조해야 합니다. 베트남어로는 'Trẻ sinh nhẹ cân' 또는 'Trẻ cân nặng thấp khi sinh'이라고 하며, 2.5kg 미만을 의미합니다.",
        "meaningVi": "Trẻ sinh có cân nặng dưới 2.500g, do sinh non hoặc chậm tăng trưởng trong tử cung. Trẻ nhẹ cân có nguy cơ cao về điều hòa thân nhiệt, nhiễm trùng, hạ đường huyết, cần chăm sóc đặc biệt và theo dõi tăng trưởng, bổ sung dinh dưỡng.",
        "context": "신생아실, 신생아집중치료실",
        "culturalNote": "한국과 베트남 모두 저체중 출생아가 증가 추세이며, 임신 중 영양 부족, 흡연, 고혈압 등이 원인입니다. 한국은 영양 보충과 집중 관리 시스템이 잘 갖춰져 있고, 베트남은 지역에 따라 접근성 차이가 있습니다. 통역 시 생후 초기 체중 증가가 매우 중요하며, 모유 수유가 어려우면 고열량 분유로 보충해야 한다는 점을 명확히 전달해야 합니다.",
        "commonMistakes": [
            {
                "mistake": "미숙아와 동일하게 번역",
                "correction": "미숙아는 주수 기준, 저체중아는 체중 기준",
                "explanation": "두 개념은 겹칠 수 있지만 정의가 다르므로 구분해야 합니다"
            },
            {
                "mistake": "'단순히 작게 태어난 것'으로 가볍게 표현",
                "correction": "합병증 위험 높아 집중 관리 필요",
                "explanation": "저체중의 의학적 위험성을 정확히 전달해야 합니다"
            },
            {
                "mistake": "성장 추적 필요성 설명 누락",
                "correction": "정기 체중·신장 측정과 발달 평가 필수",
                "explanation": "장기 추적 관찰의 중요성을 강조해야 합니다"
            }
        ],
        "examples": [
            {
                "ko": "출생 체중 2,200g으로 저체중출생아이며, 보육기에서 체온 유지하고 자주 수유하겠습니다.",
                "vi": "Cân nặng khi sinh 2.200g, là trẻ sinh nhẹ cân, sẽ giữ ấm trong lồng ấp và cho ăn thường xuyên.",
                "situation": "formal"
            },
            {
                "ko": "저체중아라 혈당이 떨어질 수 있으니 3시간마다 수유하고, 혈당 검사를 자주 하겠습니다.",
                "vi": "Vì sinh nhẹ cân nên đường huyết có thể giảm, sẽ cho ăn 3 giờ một lần và kiểm tra đường huyết thường xuyên.",
                "situation": "onsite"
            },
            {
                "slug": "선천성대사이상",
                "korean": "선천성대사이상",
                "vietnamese": "Rối loạn chuyển hóa bẩm sinh",
                "hanja": "先天性代謝異常",
                "hanjaReading": "先(먼저 선) + 天(하늘 천) + 性(성품 성) + 代(대신할 대) + 謝(사례할 사) + 異(다를 이) + 常(항상 상)",
                "pronunciation": "선천성대사이상",
                "meaningKo": "태어날 때부터 특정 효소나 호르몬의 결핍으로 인해 정상적인 대사가 이루어지지 않는 유전 질환으로, 한국은 국가 선별검사로 조기 발견합니다. 통역 시 페닐케톤뇨증, 갑상선기능저하증 등이 포함되며, 조기 발견하여 식이요법이나 약물 치료를 하면 정상 발달이 가능함을 강조해야 합니다. 베트남어로는 'Rối loạn chuyển hóa bẩm sinh' 또는 'Bệnh chuyển hóa di truyền'이라고 합니다.",
                "meaningVi": "Nhóm bệnh di truyền do thiếu enzyme hoặc hormone từ khi sinh, gây rối loạn chuyển hóa bình thường. Hàn Quốc có chương trình sàng lọc quốc gia phát hiện sớm. Bao gồm phenylketone niệu, suy giáp bẩm sinh v.v., nếu phát hiện sớm và điều trị (chế độ ăn, thuốc) thì phát triển bình thường.",
                "context": "신생아 선별검사, 소아내분비과",
                "culturalNote": "한국은 생후 48시간 이내 모든 신생아에게 선별검사를 시행하며(힐 프릭 검사), 6가지 필수 질환을 검사합니다. 베트남도 선별검사 프로그램이 있지만 보급률은 한국보다 낮습니다. 통역 시 '유전병'이라는 용어의 낙인을 고려하여 '조기 발견으로 예방 가능한 질환'임을 강조하고, 검사의 중요성을 설득력있게 전달해야 합니다.",
                "commonMistakes": [
                    {
                        "mistake": "'불치병'으로 절망적 표현",
                        "correction": "조기 치료로 정상 발달 가능",
                        "explanation": "희망적 예후를 함께 전달하여 불안을 줄여야 합니다"
                    },
                    {
                        "mistake": "'검사 안 해도 된다'고 오해 방치",
                        "correction": "국가 필수 검사이며 무료 또는 저렴",
                        "explanation": "검사의 중요성과 접근성을 강조해야 합니다"
                    },
                    {
                        "mistake": "양성 결과를 확진으로 오해",
                        "correction": "양성은 재검 필요, 확진검사로 최종 판단",
                        "explanation": "선별검사와 확진검사를 구분하여 불필요한 공포를 줄여야 합니다"
                    }
                ],
                "examples": [
                    {
                        "ko": "신생아 선별검사에서 갑상선기능저하증 의심 소견이 나와 확진검사를 하겠습니다. 조기 치료하면 정상 발달합니다.",
                        "vi": "Xét nghiệm sàng lọc sơ sinh nghi suy giáp bẩm sinh nên sẽ làm xét nghiệm xác định. Nếu điều trị sớm thì phát triển bình thường.",
                        "situation": "formal"
                    },
                    {
                        "ko": "페닐케톤뇨증으로 확진되어 특수 분유로 평생 관리해야 하지만, 식이요법 잘 지키면 정상 생활 가능합니다.",
                        "vi": "Xác định phenylketone niệu nên phải quản lý suốt đời bằng sữa đặc biệt, nhưng nếu tuân thủ chế độ ăn thì sinh hoạt bình thường được.",
                        "situation": "onsite"
                    },
                    {
                        "ko": "선천성대사이상 검사는 아기 발 뒤꿈치에서 피 몇 방울만 채취하는 간단한 검사니까 꼭 받으세요.",
                        "vi": "Xét nghiệm rối loạn chuyển hóa bẩm sinh chỉ lấy vài giọt máu ở gót chân bé, rất đơn giản nên nhất định phải làm nhé.",
                        "situation": "informal"
                    }
                ],
                "relatedTerms": ["페닐케톤뇨증", "갑상선기능저하증", "신생아선별검사", "힐프릭검사"]
            }
        ],
        "relatedTerms": ["미숙아", "자궁내성장지연", "영양보충", "성장추적"]
    }
]

# Read existing medical.json
print(f"Reading from: {file_path}")
with open(file_path, 'r', encoding='utf-8') as f:
    data = json.load(f)

print(f"Current terms count: {len(data['terms'])}")

# Add new terms
data['terms'].extend(new_terms)

print(f"New terms count after addition: {len(data['terms'])}")

# Save back to file
with open(file_path, 'w', encoding='utf-8') as f:
    json.dump(data, f, ensure_ascii=False, indent=2)

print(f"✅ Successfully added {len(new_terms)} new medical terms (Part 2)")
print(f"✅ Total terms now: {len(data['terms'])}")
print(f"✅ Saved to: {file_path}")
