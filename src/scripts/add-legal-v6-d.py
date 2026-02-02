#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""해양법 용어 추가 스크립트 (v6-d)"""

import json
import os

def load_existing_terms():
    file_path = os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', 'data', 'terms', 'legal.json')
    with open(file_path, 'r', encoding='utf-8') as f:
        data = json.load(f)
    return data, file_path

def create_legal_terms():
    terms = [
        {
            "slug": "lanh-hai",
            "korean": "영해",
            "vietnamese": "Lãnh hải",
            "hanja": "領海",
            "hanjaReading": "領(거느릴 령) + 海(바다 해)",
            "pronunciation": "령해 (영해)",
            "meaningKo": "연안국이 주권을 행사하는 일정 범위의 바다 영역으로, 기선으로부터 12해리까지를 의미합니다. 통역 시 주의할 점은 베트남은 기선 설정 방식이 한국과 다를 수 있으며, 영해 내에서는 무해통항권을 제외하고는 연안국의 완전한 주권이 미친다는 점을 명확히 해야 합니다. 법률 문서에서는 '영해 및 접속수역법'과 같은 관련 법령을 함께 언급하는 것이 일반적입니다.",
            "meaningVi": "Vùng biển mà quốc gia ven biển thực hiện chủ quyền, kéo dài từ đường cơ sở đến 12 hải lý. Trong lãnh hải, quốc gia ven biển có chủ quyền hoàn toàn, ngoại trừ quyền đi qua không gây hại của tàu thuyền nước ngoài.",
            "context": "해양법협약, 영토분쟁, 국제해양법",
            "culturalNote": "한국과 베트남 모두 영해 범위를 12해리로 설정하고 있으나, 기선 설정 방식(직선기선, 통상기선)에서 차이가 있을 수 있습니다. 베트남은 남중국해 분쟁 지역에서 영해 주장이 복잡하게 얽혀 있으며, 통역 시 이러한 민감한 정치적 맥락을 이해하고 중립적 표현을 사용해야 합니다. 한국은 동해 명칭 문제와 연계하여 영해 개념을 설명하는 경우가 많습니다.",
            "commonMistakes": [
                {
                    "mistake": "영해를 '배타적경제수역'과 혼동하여 'Vùng đặc quyền kinh tế'로 번역",
                    "correction": "'Lãnh hải'로 정확히 구분",
                    "explanation": "영해는 주권이 완전히 미치는 12해리 이내, EEZ는 자원에 대한 주권적 권리가 미치는 200해리 이내로 법적 지위가 다름"
                },
                {
                    "mistake": "'Biển quốc gia' (국가의 바다)로 직역",
                    "correction": "법률 용어인 'Lãnh hải' 사용",
                    "explanation": "Lãnh hải는 국제해양법에서 공식적으로 정의된 법률 용어이며, 직역은 법적 정확성이 떨어짐"
                },
                {
                    "mistake": "무해통항권을 '자유통항'으로 과대 해석",
                    "correction": "'Quyền đi qua không gây hại' (무해통항권)로 제한적 개념 강조",
                    "explanation": "무해통항권은 연안국의 평화·질서·안전을 해치지 않는 범위 내에서만 인정되는 제한적 권리임"
                }
            ],
            "examples": [
                {
                    "ko": "우리나라 영해 내에서 불법 조업한 외국 선박은 나포될 수 있습니다.",
                    "vi": "Tàu nước ngoài đánh bắt bất hợp pháp trong lãnh hải của chúng ta có thể bị bắt giữ.",
                    "situation": "formal"
                },
                {
                    "ko": "영해기선은 간조 시 해안선을 기준으로 설정됩니다.",
                    "vi": "Đường cơ sở lãnh hải được xác định dựa trên đường bờ biển khi thủy triều thấp.",
                    "situation": "formal"
                },
                {
                    "ko": "영해 통과 시 연안국의 법령을 준수해야 합니다.",
                    "vi": "Khi đi qua lãnh hải phải tuân thủ pháp luật của quốc gia ven biển.",
                    "situation": "onsite"
                }
            ],
            "relatedTerms": ["batajeokkeongjeyeokwon", "jeopsogsuyeok", "gieon", "moohaetonghaengwon"]
        },
        {
            "slug": "vung-dac-quyen-kinh-te",
            "korean": "배타적경제수역",
            "vietnamese": "Vùng đặc quyền kinh tế",
            "hanja": "排他的經濟水域",
            "hanjaReading": "排(물리칠 배) + 他(다를 타) + 的(과녁 적) + 經(날 경) + 濟(건널 제) + 水(물 수) + 域(지경 역)",
            "pronunciation": "배타적경제수역",
            "meaningKo": "연안국이 기선으로부터 200해리까지 해양생물자원과 광물자원에 대한 주권적 권리를 행사하는 수역입니다. 통역 시 주의할 점은 이 수역에서 연안국은 영해와 달리 완전한 주권이 아닌 '자원에 대한 주권적 권리'만을 가지며, 타국의 항해·상공비행의 자유는 보장된다는 점을 명확히 구분해야 합니다. 어업협정, 해양자원 개발 계약 통역 시 자주 등장하는 핵심 개념입니다.",
            "meaningVi": "Khu vực biển mà quốc gia ven biển có quyền chủ quyền đối với tài nguyên sinh vật và khoáng sản, kéo dài đến 200 hải lý từ đường cơ sở. Các quốc gia khác vẫn có quyền tự do hàng hải và bay qua vùng trời.",
            "context": "어업협정, 해양자원 개발, 국제해양법",
            "culturalNote": "한국은 서해·남해·동해에서 중국·일본과 EEZ 경계획정 문제로 갈등을 겪고 있으며, 베트남은 남중국해에서 중국과 EEZ 중첩 분쟁이 심각합니다. 통역 시 이러한 양국의 민감한 해양분쟁 맥락을 이해하고, 특히 중국과의 관계에서 EEZ 개념을 설명할 때는 신중한 표현이 필요합니다. 베트남 어민들에게 EEZ는 생존권과 직결된 문제입니다.",
            "commonMistakes": [
                {
                    "mistake": "'Vùng kinh tế độc quyền'으로 번역하여 '독점'의 뉘앙스 전달",
                    "correction": "'Vùng đặc quyền kinh tế'로 '특별한 권리'의 의미 강조",
                    "explanation": "Độc quyền은 완전한 독점을 의미하지만, EEZ는 항해·상공비행의 자유가 보장되므로 đặc quyền(특권)이 더 정확함"
                },
                {
                    "mistake": "주권(chủ quyền)과 주권적 권리(quyền chủ quyền)를 혼동",
                    "correction": "EEZ에서는 '자원에 대한 quyền chủ quyền'만 존재",
                    "explanation": "영해는 chủ quyền(완전한 주권), EEZ는 quyền chủ quyền(자원에 한정된 주권적 권리)으로 법적 지위가 다름"
                },
                {
                    "mistake": "200해리를 '200km'로 오역",
                    "correction": "'200 hải lý' (약 370km)",
                    "explanation": "1해리는 1.852km이므로 단위 환산 오류는 법적 분쟁의 원인이 될 수 있음"
                }
            ],
            "examples": [
                {
                    "ko": "배타적경제수역 내에서 타국의 무단 어업은 불법입니다.",
                    "vi": "Đánh bắt cá trái phép của nước khác trong vùng đặc quyền kinh tế là bất hợp pháp.",
                    "situation": "formal"
                },
                {
                    "ko": "한-베트남 어업협정은 양국 배타적경제수역에서의 조업 조건을 규정합니다.",
                    "vi": "Hiệp định đánh cá Hàn-Việt quy định điều kiện đánh bắt trong vùng đặc quyền kinh tế của hai nước.",
                    "situation": "formal"
                },
                {
                    "ko": "이 해역은 우리 배타적경제수역이므로 해양자원 개발권은 우리에게 있습니다.",
                    "vi": "Vùng biển này là vùng đặc quyền kinh tế của chúng ta nên quyền khai thác tài nguyên biển thuộc về chúng ta.",
                    "situation": "onsite"
                }
            ],
            "relatedTerms": ["lanh-hai", "dai-luc-붕", "eobhyeobjeongeung", "haeyangjaewon"]
        },
        {
            "slug": "dai-luc-붕",
            "korean": "대륙붕",
            "vietnamese": "Thềm lục địa",
            "hanja": "大陸棚",
            "hanjaReading": "大(큰 대) + 陸(뭍 륙) + 棚(시렁 붕)",
            "pronunciation": "대륙붕",
            "meaningKo": "육지 영토의 자연연장으로 해안에서 대양 쪽으로 완만하게 경사진 해저지형을 의미하며, 연안국은 이 지역의 해저 및 하층토의 천연자원에 대해 주권적 권리를 행사합니다. 통역 시 주의할 점은 대륙붕의 범위가 지질학적 기준(대륙변계 외연)과 거리 기준(200해리 또는 최대 350해리) 중 유리한 것을 선택할 수 있다는 복잡한 법리를 정확히 전달해야 합니다. 해저자원 개발권 분쟁 시 핵심 쟁점입니다.",
            "meaningVi": "Vùng đáy biển và lòng đất dưới đáy biển kéo dài từ bờ biển ra phía đại dương với độ dốc thoải, là phần kéo dài tự nhiên của lãnh thổ đất liền. Quốc gia ven biển có quyền chủ quyền đối với tài nguyên thiên nhiên của vùng này.",
            "context": "해저자원 개발, 석유가스전, 해양광물",
            "culturalNote": "한국은 동중국해 대륙붕에서 중국·일본과 경계획정 분쟁을 겪고 있으며, 베트남은 남중국해에서 중국의 '구단선' 주장과 충돌하는 대륙붕 권리를 주장합니다. 통역 시 대륙붕 개념은 석유·가스전 개발권과 직결되어 경제적 이해관계가 크므로, 양국 모두 매우 민감하게 반응합니다. 특히 베트남은 남중국해 대륙붕에서 석유 시추권을 둘러싼 중국과의 충돌이 빈번합니다.",
            "commonMistakes": [
                {
                    "mistake": "'Bãi đá ngầm' (암초)로 오역",
                    "correction": "'Thềm lục địa'로 지질학적 개념 정확히 표현",
                    "explanation": "대륙붕은 해안에서 완만히 경사진 지형 전체를 의미하며, 암초는 수면 위 또는 직하에 있는 암석을 뜻함"
                },
                {
                    "mistake": "대륙붕을 EEZ와 동일시",
                    "correction": "대륙붕은 '해저 및 하층토 자원'에 대한 권리, EEZ는 '상부수역 포함 모든 자원'에 대한 권리",
                    "explanation": "대륙붕 권리는 해저에 한정되며 상부수역의 항해 자유는 보장되지만, EEZ는 수산자원도 포함"
                },
                {
                    "mistake": "200해리를 대륙붕의 최대 범위로 설명",
                    "correction": "지질학적 기준 충족 시 최대 350해리까지 연장 가능",
                    "explanation": "대륙변계 외연이 200해리를 초과하면 최대 350해리 또는 2500m 등심선에서 100해리까지 주장 가능"
                }
            ],
            "examples": [
                {
                    "ko": "대륙붕 경계획정은 형평의 원칙에 따라 이루어져야 합니다.",
                    "vi": "Phân định ranh giới thềm lục địa phải được thực hiện theo nguyên tắc công bằng.",
                    "situation": "formal"
                },
                {
                    "ko": "이 해저 유전은 우리나라 대륙붕에 위치합니다.",
                    "vi": "Mỏ dầu đáy biển này nằm trong thềm lục địa của chúng ta.",
                    "situation": "formal"
                },
                {
                    "ko": "대륙붕 자원 개발 계약서를 검토하겠습니다.",
                    "vi": "Tôi sẽ xem xét hợp đồng khai thác tài nguyên thềm lục địa.",
                    "situation": "onsite"
                }
            ],
            "relatedTerms": ["vung-dac-quyen-kinh-te", "haejeojaewon", "seongnyugajeon", "haeyanggyeonggye"]
        },
        {
            "slug": "cong-hai",
            "korean": "공해",
            "vietnamese": "Công hải",
            "hanja": "公海",
            "hanjaReading": "公(공평할 공) + 海(바다 해)",
            "pronunciation": "공해",
            "meaningKo": "어느 국가의 주권이나 관할권에도 속하지 않는 바다로, 모든 국가에 개방되어 있으며 항해·상공비행·해저전선 부설·어로의 자유가 보장됩니다. 통역 시 주의할 점은 공해자유 원칙이 절대적이지 않으며, 해적행위·마약밀매·노예매매 등에 대해서는 모든 국가가 단속할 수 있는 '보편적 관할권'이 인정된다는 점을 명확히 해야 합니다. 원양어업, 해운 계약 통역 시 자주 등장합니다.",
            "meaningVi": "Vùng biển không thuộc chủ quyền hay quyền tài phán của bất kỳ quốc gia nào, mở cửa cho tất cả các quốc gia với các quyền tự do hàng hải, bay qua, đặt cáp ngầm, và đánh cá.",
            "context": "원양어업, 국제해운, 해양환경보호",
            "culturalNote": "한국 원양어선들은 공해에서 조업하는 경우가 많으며, 베트남은 공해 조업 경험이 상대적으로 적어 개념 이해에 시간이 필요할 수 있습니다. 통역 시 '공해'를 '아무나 마음대로 쓸 수 있는 곳'으로 과도하게 단순화하지 말고, 국제해양법협약에 따른 규제(불법어업 금지, 환경보호 의무 등)가 존재함을 강조해야 합니다. 베트남어 '공해(ô nhiễm)'와 혼동하지 않도록 주의.",
            "commonMistakes": [
                {
                    "mistake": "베트남어 'Ô nhiễm' (오염)과 혼동",
                    "correction": "'Công hải' (公海)로 한자어 차용 표현 사용",
                    "explanation": "Ô nhiễm은 환경오염을 의미하며, 공해(바다)는 Công hải로 표기"
                },
                {
                    "mistake": "'Biển tự do' (자유로운 바다)로 직역하여 무제한적 자유 암시",
                    "correction": "'Công hải'로 법률 용어 사용하고, 국제법상 제약 설명 추가",
                    "explanation": "공해도 불법어업·환경파괴·해적행위 등은 금지되며, 기국주의 원칙에 따른 규제가 존재"
                },
                {
                    "mistake": "공해와 국제수역을 혼동",
                    "correction": "공해는 EEZ 밖의 바다, 국제수역은 영해 내 국제항행용 해협 포함",
                    "explanation": "국제항행용 해협은 영해이지만 통과통항권이 인정되므로 별도 개념"
                }
            ],
            "examples": [
                {
                    "ko": "공해에서의 어로활동은 국제협약을 준수해야 합니다.",
                    "vi": "Hoạt động đánh cá trên công hải phải tuân thủ các công ước quốc tế.",
                    "situation": "formal"
                },
                {
                    "ko": "이 선박은 공해상에서 해적의 공격을 받았습니다.",
                    "vi": "Con tàu này đã bị cướp biển tấn công trên công hải.",
                    "situation": "formal"
                },
                {
                    "ko": "공해 자유 원칙은 모든 국가에 동등하게 적용됩니다.",
                    "vi": "Nguyên tắc tự do công hải được áp dụng bình đẳng cho tất cả các quốc gia.",
                    "situation": "onsite"
                }
            ],
            "relatedTerms": ["wonyangeobeon", "haejok", "gigugjuui", "haeyangjayu"]
        },
        {
            "slug": "cuop-bien",
            "korean": "해적",
            "vietnamese": "Cướp biển",
            "hanja": "海賊",
            "hanjaReading": "海(바다 해) + 賊(도둑 적)",
            "pronunciation": "해적",
            "meaningKo": "공해 또는 국가 관할권 밖에서 사적 목적으로 다른 선박이나 항공기에 대해 불법적인 폭력·억류·약탈행위를 하는 것을 의미합니다. 통역 시 주의할 점은 해적행위는 '보편적 관할권' 대상이어서 어느 국가든 체포·처벌할 수 있으며, 영해 내 유사 행위는 '해적'이 아닌 '해상강도(armed robbery at sea)'로 구분된다는 점입니다. 해운보험, 선원 안전 교육에서 중요한 개념입니다.",
            "meaningVi": "Hành vi bạo lực, giam giữ hoặc cướp bóc bất hợp pháp được thực hiện vì mục đích cá nhân trên công hải hoặc ngoài phạm vi quyền tài phán của quốc gia, nhắm vào tàu thuyền hoặc máy bay khác.",
            "context": "해운보험, 선원안전, 국제형사법",
            "culturalNote": "한국 선박은 소말리아 해역, 말라카 해협 등에서 해적 피해를 입은 사례가 있으며, 베트남은 남중국해에서 어선이 공격당하는 사건이 발생합니다. 통역 시 해적과 테러리즘의 구분(테러는 정치적 목적, 해적은 사적 이익 추구), 해적행위 시 선원의 대응 매뉴얼(저항 금지, 안전 최우선) 등 실무적 내용을 정확히 전달해야 합니다. 베트남 어민들은 '해적'을 광범위하게 사용하므로 법적 정의를 명확히 할 필요가 있습니다.",
            "commonMistakes": [
                {
                    "mistake": "'Hải tặc' (고전적 해적)으로만 번역하여 현대적 해적 개념 누락",
                    "correction": "'Cướp biển'로 현대 국제법상 해적행위 표현",
                    "explanation": "Hải tặc은 고전적·낭만적 이미지가 강하고, Cướp biển은 현대 범죄 행위를 명확히 나타냄"
                },
                {
                    "mistake": "영해 내 강도행위를 '해적'으로 분류",
                    "correction": "공해상 행위만 '해적(cướp biển)', 영해 내는 '해상강도(cướp có vũ trang trên biển)'",
                    "explanation": "국제해양법협약 제101조는 해적행위를 공해 또는 국가 관할권 밖으로 한정"
                },
                {
                    "mistake": "'Khủng bố biển' (해상 테러)와 혼동",
                    "correction": "해적은 사적 이익, 테러는 정치적 목적으로 구분",
                    "explanation": "동기에 따라 적용 법률과 국제공조 방식이 다르므로 정확한 구분 필수"
                }
            ],
            "examples": [
                {
                    "ko": "소말리아 해역에서 해적 출몰이 보고되었습니다.",
                    "vi": "Đã có báo cáo về sự xuất hiện của cướp biển tại vùng biển Somalia.",
                    "situation": "formal"
                },
                {
                    "ko": "해적 공격 시 선원들은 안전구역으로 대피해야 합니다.",
                    "vi": "Khi bị cướp biển tấn công, thuyền viên phải sơ tán đến khu vực an toàn.",
                    "situation": "onsite"
                },
                {
                    "ko": "해적행위는 국제법상 중대범죄로 처벌됩니다.",
                    "vi": "Hành vi cướp biển bị trừng phạt như tội phạm nghiêm trọng theo luật quốc tế.",
                    "situation": "formal"
                }
            ],
            "relatedTerms": ["cong-hai", "haesanggangeodo", "bopyeonjeokgwanhalwon", "haeyunanbojeon"]
        },
        {
            "slug": "o-nhiem-bien",
            "korean": "해양오염",
            "vietnamese": "Ô nhiễm biển",
            "hanja": "海洋汚染",
            "hanjaReading": "海(바다 해) + 洋(큰바다 양) + 汚(더러울 오) + 染(물들 염)",
            "pronunciation": "해양오염",
            "meaningKo": "선박·해양시설·육상기인 활동 등으로 인해 바다에 유해물질이 유입되어 해양생물·인간 건강·어업·해양 이용에 피해를 주거나 해양환경의 질을 저하시키는 현상입니다. 통역 시 주의할 점은 오염원(기름유출, 폐기물투기, 육상배출수 등)을 명확히 구분하고, 국제협약(MARPOL, 런던협약 등)상 책임 소재와 배상 체계를 정확히 전달해야 합니다. 환경소송, 해양사고 보상 청구 시 핵심 개념입니다.",
            "meaningVi": "Hiện tượng các chất độc hại xâm nhập vào biển do tàu thuyền, công trình biển, hoạt động trên đất liền, gây thiệt hại cho sinh vật biển, sức khỏe con người, nghề cá, sử dụng biển hoặc làm giảm chất lượng môi trường biển.",
            "context": "환경법, 해양사고, 손해배상",
            "culturalNote": "한국은 삼성중공업 기름유출 사고(2014), 허베이 스피리트호 사고(2007) 등으로 해양오염 대응 체계가 발달했으며, 베트남은 2016년 Formosa 사태로 중부 해안이 대규모 오염되어 어민 생계에 큰 타격을 입었습니다. 통역 시 양국 모두 해양오염 문제에 민감하며, 특히 베트남은 Formosa 사태 이후 환경규제가 강화되었음을 인지해야 합니다. 어민 피해 보상 문제는 정치·사회적 쟁점이 됩니다.",
            "commonMistakes": [
                {
                    "mistake": "'Ô nhiễm môi trường' (환경오염)으로 포괄적 표현 사용",
                    "correction": "'Ô nhiễm biển'로 해양 특정 오염 명시",
                    "explanation": "해양오염은 해양환경관리법 등 특별법 적용 대상이므로 육상환경오염과 구분 필요"
                },
                {
                    "mistake": "기름유출(tràn dầu)만 해양오염으로 인식",
                    "correction": "폐기물 투기, 유독물질 배출, 플라스틱 오염 등 다양한 원인 포함",
                    "explanation": "해양오염 범위는 기름뿐 아니라 화학물질, 생활쓰레기, 방사능물질 등 광범위함"
                },
                {
                    "mistake": "오염원을 '선박'으로만 한정",
                    "correction": "육상기인(80%), 선박(10%), 해양투기(10%) 등 다양한 원인 설명",
                    "explanation": "실제로 육상에서 하천을 통해 유입되는 오염이 가장 큰 비중을 차지함"
                }
            ],
            "examples": [
                {
                    "ko": "원유 유출로 인한 해양오염 복구에는 수년이 걸립니다.",
                    "vi": "Phục hồi ô nhiễm biển do tràn dầu thô mất nhiều năm.",
                    "situation": "formal"
                },
                {
                    "ko": "해양오염 방지를 위해 선박은 MARPOL 협약을 준수해야 합니다.",
                    "vi": "Để phòng ngừa ô nhiễm biển, tàu thuyền phải tuân thủ Công ước MARPOL.",
                    "situation": "formal"
                },
                {
                    "ko": "이번 사고로 인한 해양오염 피해액을 산정 중입니다.",
                    "vi": "Đang tính toán thiệt hại do ô nhiễm biển từ vụ tai nạn này.",
                    "situation": "onsite"
                }
            ],
            "relatedTerms": ["gireumyuchul", "haeyanghakyeonbangji", "marpol", "sonhaebeasang"]
        },
        {
            "slug": "tai-nguyen-bien",
            "korean": "해양자원",
            "vietnamese": "Tài nguyên biển",
            "hanja": "海洋資源",
            "hanjaReading": "海(바다 해) + 洋(큰바다 양) + 資(재물 자) + 源(근원 원)",
            "pronunciation": "해양자원",
            "meaningKo": "바다에 존재하는 생물자원(어류, 해조류 등), 광물자원(석유, 가스, 망간단괴 등), 에너지자원(조력, 파력 등)을 총칭하는 개념입니다. 통역 시 주의할 점은 자원 유형에 따라 관할권(EEZ는 생물+비생물, 대륙붕은 해저·하층토만), 개발 허가권자, 환경영향평가 요건이 다르므로 계약서·협정문에서 어떤 자원을 다루는지 명확히 확인해야 합니다. 베트남은 해양자원 개발이 경제성장의 핵심 과제입니다.",
            "meaningVi": "Khái niệm tổng hợp các tài nguyên sinh vật (cá, rong biển...), tài nguyên khoáng sản (dầu, khí đốt, nốt mangan...), và tài nguyên năng lượng (thuỷ triều, sóng biển...) tồn tại trong biển.",
            "context": "자원개발 계약, 어업협정, 에너지정책",
            "culturalNote": "한국은 동해 가스하이드레이트, 서해 해상풍력 등 해양자원 개발에 주력하며, 베트남은 남중국해 석유·가스전이 국가재정의 중요한 부분을 차지합니다. 통역 시 해양자원은 단순한 경제적 이익을 넘어 영토주권·국가안보와 직결된 민감한 사안임을 인식해야 합니다. 특히 베트남은 중국의 석유 시추 방해로 인한 분쟁 경험이 있어 해양자원 개발권에 매우 민감합니다.",
            "commonMistakes": [
                {
                    "mistake": "'Tài nguyên thiên nhiên' (천연자원)으로 포괄적 표현",
                    "correction": "'Tài nguyên biển'로 해양 특정 자원 명시",
                    "explanation": "천연자원은 육상 자원도 포함하므로 법적 관할권이 다름"
                },
                {
                    "mistake": "어류만 해양자원으로 인식",
                    "correction": "생물(수산), 비생물(석유·가스·광물), 에너지(조력·파력) 모두 포함",
                    "explanation": "해양자원의 범위는 매우 광범위하며, 자원 유형에 따라 개발 규제와 관할권이 다름"
                },
                {
                    "mistake": "해양자원 개발을 '자유로운 활동'으로 오해",
                    "correction": "연안국 허가, 환경영향평가, 국제협약 준수 필수",
                    "explanation": "무단 개발은 주권 침해이며, 환경파괴 시 국제법상 책임 발생"
                }
            ],
            "examples": [
                {
                    "ko": "해양자원 공동개발 협정을 체결하겠습니다.",
                    "vi": "Chúng tôi sẽ ký kết hiệp định phát triển chung tài nguyên biển.",
                    "situation": "formal"
                },
                {
                    "ko": "이 해역의 해양자원 조사 결과를 보고드립니다.",
                    "vi": "Tôi báo cáo kết quả khảo sát tài nguyên biển tại vùng biển này.",
                    "situation": "formal"
                },
                {
                    "ko": "해양자원 개발에는 막대한 초기 투자가 필요합니다.",
                    "vi": "Phát triển tài nguyên biển cần đầu tư ban đầu rất lớn.",
                    "situation": "onsite"
                }
            ],
            "relatedTerms": ["vung-dac-quyen-kinh-te", "dai-luc-붕", "seongnyugajeon", "hwangyeongabpyounggah"]
        },
        {
            "slug": "hiep-dinh-nghep-ca",
            "korean": "어업협정",
            "vietnamese": "Hiệp định nghề cá",
            "hanja": "漁業協定",
            "hanjaReading": "漁(고기잡을 어) + 業(업 업) + 協(화합할 협) + 定(정할 정)",
            "pronunciation": "어업협정",
            "meaningKo": "두 개 이상의 국가가 각국 수역 또는 공해에서의 어업 활동에 관한 조업 조건, 어획량 할당, 단속·처벌 절차 등을 규정한 국제협정입니다. 통역 시 주의할 점은 협정 내용이 매우 기술적(어종별 쿼터, 그물 규격, 조업 구역 좌표 등)이므로 전문용어를 정확히 숙지하고, 위반 시 벌칙(나포, 벌금, 면허 취소 등)을 명확히 전달해야 합니다. 한-중, 한-일 어업협정이 대표적입니다.",
            "meaningVi": "Hiệp định quốc tế giữa hai hoặc nhiều quốc gia quy định về điều kiện đánh bắt, phân bổ sản lượng, thủ tục kiểm soát và xử phạt trong hoạt động nghề cá tại vùng biển của các nước hoặc trên công hải.",
            "context": "원양어업, 수산협력, 국제어업관리",
            "culturalNote": "한국은 중국·일본과 복잡한 어업협정을 맺고 있으며, 불법조업 단속이 외교 마찰의 원인이 되기도 합니다. 베트남은 남중국해에서 중국 어선의 불법조업 피해를 자주 입으며, 어민 보호가 정치적 이슈입니다. 통역 시 어업협정은 어민 생계와 직결되므로, 할당량·조업 구역 등 수치와 지리 정보를 정확히 전달하는 것이 매우 중요합니다. 베트남 어민은 협정 내용을 잘 모르는 경우가 많아 충분한 설명이 필요합니다.",
            "commonMistakes": [
                {
                    "mistake": "'Thỏa thuận đánh cá' (어업 합의)로 비공식적 표현 사용",
                    "correction": "'Hiệp định nghề cá'로 공식 조약 수준 표현",
                    "explanation": "Hiệp định은 국회 비준을 거친 정식 조약이며, Thỏa thuận은 행정협정 수준"
                },
                {
                    "mistake": "어획량 할당(phân bổ sản lượng)을 생략하고 '자유 조업' 암시",
                    "correction": "쿼터제·TAC(총허용어획량) 등 규제 내용 명확히 전달",
                    "explanation": "협정은 자원 보호를 위해 엄격한 어획 제한을 두므로 자유 조업이 아님"
                },
                {
                    "mistake": "위반 시 처벌을 '경고' 수준으로 축소",
                    "correction": "나포(bắt giữ), 벌금(phạt tiền), 면허 취소(thu hồi giấy phép) 등 구체적 제재 명시",
                    "explanation": "불법조업은 중대한 협정 위반으로 선박 나포 및 형사처벌 대상"
                }
            ],
            "examples": [
                {
                    "ko": "한-중 어업협정에 따라 조업 쿼터가 배정되었습니다.",
                    "vi": "Hạn ngạch đánh bắt đã được phân bổ theo Hiệp định nghề cá Hàn-Trung.",
                    "situation": "formal"
                },
                {
                    "ko": "협정 수역에서 조업하려면 사전 신고가 필요합니다.",
                    "vi": "Để đánh bắt trong vùng biển theo hiệp định cần báo trước.",
                    "situation": "onsite"
                },
                {
                    "ko": "어업협정 위반으로 선박이 나포되었습니다.",
                    "vi": "Tàu đã bị bắt giữ do vi phạm hiệp định nghề cá.",
                    "situation": "formal"
                }
            ],
            "relatedTerms": ["vung-dac-quyen-kinh-te", "bulleopjeobeob", "johapkwoeteo", "eohabhallarang"]
        },
        {
            "slug": "tranh-chap-bien",
            "korean": "해양분쟁",
            "vietnamese": "Tranh chấp biển",
            "hanja": "海洋紛爭",
            "hanjaReading": "海(바다 해) + 洋(큰바다 양) + 紛(어지러울 분) + 爭(다툴 쟁)",
            "pronunciation": "해양분쟁",
            "meaningKo": "국가 간 해양경계획정, 도서 영유권, 어업권, 해양자원 개발권 등을 둘러싼 법적·정치적 갈등을 의미합니다. 통역 시 주의할 점은 분쟁 해결 방식(양자협상, 중재재판, 국제해양법재판소 등)과 각 방식의 법적 구속력을 정확히 이해하고, 역사적 권원·지리적 형평성·해양법협약 등 복잡한 법리를 단순화하지 않고 전달해야 합니다. 영토주권과 연결되어 매우 민감한 사안입니다.",
            "meaningVi": "Xung đột pháp lý và chính trị giữa các quốc gia liên quan đến phân định ranh giới biển, chủ quyền đảo, quyền đánh cá, quyền khai thác tài nguyên biển.",
            "context": "국제중재, 영토분쟁, 외교협상",
            "culturalNote": "한국은 독도·이어도 문제로 일본·중국과 해양분쟁을 겪고 있으며, 베트남은 남중국해(Biển Đông)에서 중국·필리핀·말레이시아 등과 복잡한 다자분쟁 중입니다. 통역 시 해양분쟁은 국민감정이 격앙되는 주제이므로, 중립적 언어를 사용하고 법적 사실과 정치적 주장을 구분하여 전달해야 합니다. 특히 베트남에서 '남중국해'는 'Biển Đông'(동해)로 불리며, 'South China Sea'라는 표현을 싫어합니다.",
            "commonMistakes": [
                {
                    "mistake": "'Xung đột vũ trang' (무력충돌)로 과장",
                    "correction": "'Tranh chấp' (분쟁) 또는 'Bất đồng' (이견)로 외교적 표현 사용",
                    "explanation": "대부분의 해양분쟁은 외교·법적 수단으로 해결하며, 무력충돌은 극히 드물고 부정적 인상을 줌"
                },
                {
                    "mistake": "일방 국가의 주장만 전달하여 편향성 노출",
                    "correction": "양측 주장을 균형 있게 전달하고, '~라고 주장한다(cho rằng)'로 객관화",
                    "explanation": "통역사는 중립을 유지해야 하며, 어느 한쪽 입장을 지지하는 듯한 번역은 외교 마찰 야기"
                },
                {
                    "mistake": "'영토(lãnh thổ)'와 '도서(đảo)' 혼용",
                    "correction": "육지는 lãnh thổ, 섬은 đảo, 암초는 đá ngầm로 정확히 구분",
                    "explanation": "국제해양법에서 섬과 암초는 법적 지위가 다르며(섬은 EEZ 인정, 암초는 불인정), 용어 혼동 시 법리 왜곡"
                }
            ],
            "examples": [
                {
                    "ko": "해양분쟁은 국제해양법재판소에 회부할 수 있습니다.",
                    "vi": "Tranh chấp biển có thể được đưa ra Tòa án Luật biển Quốc tế.",
                    "situation": "formal"
                },
                {
                    "ko": "양국은 해양분쟁을 평화적으로 해결하기로 합의했습니다.",
                    "vi": "Hai nước đã đồng ý giải quyết tranh chấp biển một cách hòa bình.",
                    "situation": "formal"
                },
                {
                    "ko": "이 해역은 해양분쟁 대상 수역입니다.",
                    "vi": "Vùng biển này là khu vực có tranh chấp biển.",
                    "situation": "onsite"
                }
            ],
            "relatedTerms": ["lanh-hai", "vung-dac-quyen-kinh-te", "gungjejungjaejae", "dosueoyugwon"]
        },
        {
            "slug": "an-toan-hang-hai",
            "korean": "해양안전",
            "vietnamese": "An toàn hàng hải",
            "hanja": "海洋安全",
            "hanjaReading": "海(바다 해) + 洋(큰바다 양) + 安(편안할 안) + 全(온전할 전)",
            "pronunciation": "해양안전",
            "meaningKo": "선박의 항행 안전, 해상 인명 안전, 해양사고 예방, 수색·구조 체계 등 바다에서의 종합적 안전 확보를 의미합니다. 통역 시 주의할 점은 SOLAS(해상인명안전협약), STCW(선원훈련·자격증명·당직근무기준협약) 등 국제협약상의 구체적 안전 기준과, 선박검사·선원자격·항행장비·비상대응 절차 등 기술적 세부사항을 정확히 전달해야 합니다. 조선·해운업계, 해양경찰 업무에서 필수 개념입니다.",
            "meaningVi": "Đảm bảo an toàn tổng hợp trên biển bao gồm an toàn hàng hải tàu thuyền, an toàn tính mạng trên biển, phòng ngừa tai nạn biển, hệ thống tìm kiếm và cứu nạn.",
            "context": "조선업, 해운업, 해양경찰",
            "culturalNote": "한국은 세월호 참사(2014) 이후 해양안전 규제가 대폭 강화되었으며, 해양안전심판원·해양경찰 등 전문기관이 발달했습니다. 베트남은 어선 안전 관리가 상대적으로 취약하여 태풍·해난사고 시 인명 피해가 큽니다. 통역 시 한국의 해양안전 기준은 매우 엄격하므로, 베트남 선원·어민 대상 교육에서는 구체적 절차와 장비 사용법을 충분히 설명해야 하며, '안전은 선택이 아닌 의무'라는 인식을 강조해야 합니다.",
            "commonMistakes": [
                {
                    "mistake": "'An toàn giao thông đường thủy' (수상교통 안전)로 협소하게 번역",
                    "correction": "'An toàn hàng hải'로 해양 전반의 안전 포괄",
                    "explanation": "Giao thông đường thủy는 내륙 수로 교통을 연상시키며, 해양안전은 공해 항행, 해난 구조 등 광범위한 개념"
                },
                {
                    "mistake": "SOLAS, STCW 등 국제협약 약어를 설명 없이 사용",
                    "correction": "약어 + 베트남어 풀네임 병기 (예: SOLAS - Công ước An toàn Sinh mạng trên Biển)",
                    "explanation": "베트남 어민·선원은 국제협약 약어에 익숙하지 않아 혼란 초래"
                },
                {
                    "mistake": "'안전사고'를 '사고(tai nạn)'로만 번역하여 예방 측면 누락",
                    "correction": "'Phòng ngừa tai nạn' (사고 예방)으로 사전 대응 강조",
                    "explanation": "해양안전은 사후 처리보다 예방·점검·훈련이 핵심이므로 예방 개념 강조 필요"
                }
            ],
            "examples": [
                {
                    "ko": "모든 선원은 해양안전 교육을 이수해야 합니다.",
                    "vi": "Tất cả thuyền viên phải hoàn thành khóa đào tạo an toàn hàng hải.",
                    "situation": "formal"
                },
                {
                    "ko": "해양안전 점검 결과 구명조끼가 부족한 것으로 확인되었습니다.",
                    "vi": "Kết quả kiểm tra an toàn hàng hải xác nhận thiếu áo phao cứu sinh.",
                    "situation": "onsite"
                },
                {
                    "ko": "해양안전법 위반 시 운항 정지 처분을 받을 수 있습니다.",
                    "vi": "Vi phạm Luật An toàn Hàng hải có thể bị đình chỉ hoạt động.",
                    "situation": "formal"
                }
            ],
            "relatedTerms": ["seonbaggumsa", "seonwoenjaguk", "suseakgujo", "haeyungsago"]
        }
    ]
    return terms

def main():
    data, file_path = load_existing_terms()
    existing_slugs = {t['slug'] for t in data}
    new_terms = create_legal_terms()
    filtered = [t for t in new_terms if t['slug'] not in existing_slugs]
    data.extend(filtered)
    with open(file_path, 'w', encoding='utf-8') as f:
        json.dump(data, f, ensure_ascii=False, indent=2)
    print(f"Added {len(filtered)} terms. Total: {len(data)}")

if __name__ == '__main__':
    main()
