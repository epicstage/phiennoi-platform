#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
건설 도메인 용어 추가 스크립트 - 기상/현장조건 테마 (10개)
Tier S 품질 기준 (90점 이상) 준수
"""

import json
import os

# 파일 경로 설정 (CRITICAL RULE 1)
file_path = os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', 'data', 'terms', 'construction.json')

# 기존 데이터 로드
with open(file_path, 'r', encoding='utf-8') as f:
    data = json.load(f)  # data is a LIST, not dict! (CRITICAL RULE 2)

# 기존 slug 수집 (CRITICAL RULE 4)
existing_slugs = {t['slug'] for t in data}

# 추가할 신규 용어 리스트
new_terms = [
    {
        "slug": "thoi-tiet-thi-cong",
        "korean": "시공기상",
        "vietnamese": "thời tiết thi công",
        "hanja": "施工氣象",
        "hanjaReading": "施(베풀 시) + 工(장인 공) + 氣(기운 기) + 象(형상 상)",
        "pronunciation": "티어이 띠엣 티 꽁",
        "meaningKo": "건설 공사가 진행되는 동안의 날씨 조건을 의미합니다. 통역 시 주의할 점은 베트남 남부와 북부의 기상 패턴 차이를 반드시 확인해야 한다는 것입니다. 호치민은 5~10월이 우기, 하노이는 5~9월이 우기로 시공 일정에 큰 영향을 미칩니다. 현장에서는 '날씨 때문에 못한다'는 변명이 잦으므로, 계약서에 우천 시 작업 중단 기준(강우량 mm/시간)을 명확히 규정해야 합니다. 한국은 '장마철'이라는 명확한 기간이 있지만, 베트남은 지역별로 우기가 달라 혼동이 잦습니다.",
        "meaningVi": "Điều kiện thời tiết trong suốt quá trình thi công xây dựng. Ở miền Nam, mùa mưa kéo dài từ tháng 5 đến tháng 10, còn miền Bắc từ tháng 5 đến tháng 9. Cần quy định rõ trong hợp đồng tiêu chuẩn dừng thi công khi mưa lớn (ví dụ: trên 10mm/giờ). Thời tiết ảnh hưởng trực tiếp đến tiến độ, chất lượng đổ bê tông, và an toàn lao động trên cao.",
        "context": "공정 계획, 안전 관리, 품질 관리",
        "culturalNote": "한국은 기상청 예보를 신뢰하고 주간 단위로 공정을 조정하지만, 베트남 현장에서는 '아침에 맑으면 그날 작업'하는 식의 단기 판단이 많습니다. 또한 한국은 영하 기온에서 콘크리트 양생 문제가 중요하지만, 베트남은 고온다습 환경에서의 급속 건조와 균열 방지가 더 중요합니다. 우기 시즌에는 현장 접근로가 침수되어 장비 투입이 불가능한 경우가 빈번하므로, 한국식 '비 와도 일단 출근'은 통하지 않습니다.",
        "commonMistakes": [
            {
                "mistake": "thời tiết xấu (날씨가 나쁘다)",
                "correction": "thời tiết không thuận lợi cho thi công (시공에 불리한 날씨)",
                "explanation": "건설 현장에서는 주관적인 '나쁜 날씨'가 아니라 '시공에 부적합한 조건'으로 구체적으로 표현해야 합니다."
            },
            {
                "mistake": "trời mưa nên nghỉ (비 와서 쉰다)",
                "correction": "tạm dừng thi công do mưa vượt tiêu chuẩn cho phép (허용 기준 초과 강우로 시공 중단)",
                "explanation": "계약서상 명시된 기준(예: 시간당 강우량 10mm 이상)을 언급해야 분쟁을 예방할 수 있습니다."
            },
            {
                "mistake": "thời tiết Hàn Quốc và Việt Nam giống nhau (한국과 베트남 날씨가 비슷하다)",
                "correction": "Hàn Quốc có 4 mùa rõ rệt, Việt Nam chỉ có mùa mưa và mùa khô (한국은 4계절, 베트남은 우기/건기)",
                "explanation": "기후 차이를 무시하면 공정 계획이 완전히 틀어집니다. 베트남은 '봄, 여름, 가을, 겨울' 개념이 약합니다."
            }
        ],
        "examples": [
            {
                "ko": "우기 시즌에는 콘크리트 타설 일정을 조정해야 합니다.",
                "vi": "Trong mùa mưa, cần điều chỉnh lịch đổ bê tông.",
                "situation": "formal"
            },
            {
                "ko": "오늘 강우량이 시간당 15mm 예상되니 고소작업 중단하세요.",
                "vi": "Hôm nay dự báo mưa 15mm/giờ, phải dừng tác nghiệp trên cao.",
                "situation": "onsite"
            },
            {
                "ko": "하노이는 5월부터 우기라 기초공사 그 전에 끝내야 해요.",
                "vi": "Hà Nội vào mùa mưa từ tháng 5, phải hoàn thành móng trước đó.",
                "situation": "informal"
            }
        ],
        "relatedTerms": ["mua-mua", "gio-manh", "nhiet-do-cao", "an-toan-lao-dong"]
    },
    {
        "slug": "mua-mua",
        "korean": "우기",
        "vietnamese": "mùa mưa",
        "hanja": "雨期",
        "hanjaReading": "雨(비 우) + 期(기약할 기)",
        "pronunciation": "무어 므어",
        "meaningKo": "1년 중 비가 집중적으로 내리는 시기로, 베트남에서는 지역별로 시기가 다릅니다. 통역 시 반드시 확인해야 할 것은 '남부는 5~10월, 북부는 5~9월'이라는 차이입니다. 한국인 발주자는 한국 장마철(6~7월) 기준으로 생각하기 쉬우나, 베트남 우기는 훨씬 길고 강우량도 많습니다. 현장에서는 '우기 전에 지붕 마감'과 같은 공정 마일스톤을 명확히 통역해야 하며, 계약서에 '우기 시 공기 연장 조건'을 구체적으로 명시하지 않으면 분쟁이 발생합니다. 특히 토공사, 기초공사는 우기 진입 전 완료가 필수입니다.",
        "meaningVi": "Thời kỳ mưa nhiều trong năm, ở miền Nam kéo dài từ tháng 5 đến tháng 10, miền Bắc từ tháng 5 đến tháng 9. Mùa mưa ảnh hưởng lớn đến tiến độ thi công, đặc biệt là công tác đào đất, đổ móng, và hoàn thiện mái. Hợp đồng cần quy định rõ điều kiện gia hạn tiến độ khi mưa kéo dài. Lượng mưa ở Việt Nam cao hơn nhiều so với mùa mưa ở Hàn Quốc.",
        "context": "공정 계획, 계약 조건, 현장 관리",
        "culturalNote": "한국인은 '장마철 = 6~7월 2개월'로 인식하지만, 베트남 우기는 5~6개월 지속되어 공사 기간의 절반 가까이를 차지합니다. 한국은 장마 후 무더위가 오지만, 베트남은 우기 중에도 햇볕이 강렬하게 나오는 날이 있어 '비 안 오는 날만 작업'하려는 경향이 있습니다. 또한 한국은 빗물 배수 시스템이 잘 되어 있지만, 베트남 현장은 배수 불량으로 장비가 수렁에 빠지는 사고가 빈번합니다. 우기 대비 배수로 확보는 필수입니다.",
        "commonMistakes": [
            {
                "mistake": "mùa mưa Hàn Quốc (한국 우기)",
                "correction": "mùa jangma ở Hàn Quốc (한국 장마철)",
                "explanation": "한국의 '장마'는 고유 명사처럼 쓰이므로 'jangma'로 음차하고, 베트남 우기와는 기간/강도가 다르다고 설명해야 합니다."
            },
            {
                "mistake": "mùa mưa toàn quốc từ tháng 5 (전국 우기 5월부터)",
                "correction": "mùa mưa miền Nam 5~10, miền Bắc 5~9 (남부 5~10월, 북부 5~9월)",
                "explanation": "베트남은 남북 길이가 길어 지역별 우기가 달라 '전국 일괄'로 말하면 안 됩니다."
            },
            {
                "mistake": "mưa thì không làm được gì (비 오면 아무것도 못한다)",
                "correction": "công tác ngoài trời bị hạn chế, trong nhà vẫn tiếp tục (외부작업 제한, 내부작업 계속)",
                "explanation": "우기에도 실내 마감, 설비 작업 등은 가능하므로 '전면 중단'으로 오해되지 않도록 해야 합니다."
            }
        ],
        "examples": [
            {
                "ko": "우기 전에 기초공사를 완료해야 합니다.",
                "vi": "Phải hoàn thành công tác móng trước mùa mưa.",
                "situation": "formal"
            },
            {
                "ko": "우기라 현장 진입로가 진흙탕이에요.",
                "vi": "Mùa mưa nên đường vào công trường lầy lội.",
                "situation": "onsite"
            },
            {
                "ko": "하노이 우기는 5월부터니까 지금 서두르세요.",
                "vi": "Mùa mưa Hà Nội từ tháng 5, phải khẩn trương ngay.",
                "situation": "informal"
            }
        ],
        "relatedTerms": ["mua-kho", "thoi-tiet-thi-cong", "thoat-nuoc", "tien-do-thi-cong"]
    },
    {
        "slug": "mua-kho",
        "korean": "건기",
        "vietnamese": "mùa khô",
        "hanja": "乾期",
        "hanjaReading": "乾(마를 건) + 期(기약할 기)",
        "pronunciation": "무어 커",
        "meaningKo": "비가 적게 오는 건조한 시기로, 베트남 남부는 11~4월, 북부는 10~4월입니다. 통역 시 중요한 점은 건기가 '시공 최적기'라는 것입니다. 한국인 발주자는 '건기 = 작업하기 좋은 날씨'로만 이해하지만, 베트남 건기는 건조해서 콘크리트 양생 시 급속 건조로 균열이 생기기 쉬우므로 살수 양생이 필수입니다. 또한 건기에는 먼지가 심해 마감공사 품질 관리에 주의가 필요합니다. 현장에서는 '건기에 외부공사 집중, 우기에 내부공사'라는 공정 전략을 명확히 전달해야 하며, 건기 중에도 가뭄으로 공사용수 확보가 어려울 수 있다는 점을 사전에 협의해야 합니다.",
        "meaningVi": "Thời kỳ khô ráo, mưa ít trong năm. Miền Nam từ tháng 11 đến tháng 4, miền Bắc từ tháng 10 đến tháng 4. Đây là thời điểm thuận lợi nhất cho thi công ngoài trời, nhưng cần lưu ý tưới nước dưỡng hộ bê tông thường xuyên vì không khí khô gây nứt nẻ. Bụi bặm nhiều nên cần che chắn khi thi công hoàn thiện. Mùa khô cũng có thể thiếu nước thi công nếu không chuẩn bị trước.",
        "context": "공정 계획, 품질 관리, 자원 관리",
        "culturalNote": "한국은 사계절이 뚜렷해 '건기'라는 개념이 약하지만, 베트남에서는 건기/우기가 공사 계획의 핵심입니다. 한국인은 '날씨 좋으면 작업 빠르다'고 생각하지만, 베트남 건기는 낮 기온이 35~40도까지 올라가 오전/오후 작업 시간을 조정해야 합니다. 또한 한국은 겨울에도 난방으로 실내작업이 가능하지만, 베트남 북부는 난방이 없어 건기(10~4월) 중 12~2월은 밤낮 기온차가 커서 아침 작업 시작이 늦어집니다. 건기에는 외국인 노동자 수요가 급증해 인력 확보가 어려워집니다.",
        "commonMistakes": [
            {
                "mistake": "mùa khô thì dễ làm (건기면 쉽다)",
                "correction": "mùa khô thuận lợi nhưng cần chú ý dưỡng hộ bê tông và bụi (건기는 유리하나 양생과 먼지 주의)",
                "explanation": "건기에도 고온 건조로 인한 균열, 먼지로 인한 품질 저하 등 관리 포인트가 있습니다."
            },
            {
                "mistake": "mùa khô không có vấn đề gì (건기는 문제없다)",
                "correction": "mùa khô có thể thiếu nước và quá nóng (건기는 물 부족과 고온 문제)",
                "explanation": "건기라고 해서 모든 게 순조로운 것이 아니라, 가뭄과 폭염이라는 다른 리스크가 있습니다."
            },
            {
                "mistake": "mùa khô cả nước giống nhau (전국 건기 동일)",
                "correction": "mùa khô miền Nam 11~4, miền Bắc 10~4, Tây Nguyên khác biệt (남부 11~4월, 북부 10~4월, 중부고원 다름)",
                "explanation": "베트남은 지역별 기후가 달라 건기 시작/종료 시점이 다릅니다."
            }
        ],
        "examples": [
            {
                "ko": "건기에 외장 마감공사를 집중 추진하겠습니다.",
                "vi": "Sẽ tập trung thi công hoàn thiện ngoại thất trong mùa khô.",
                "situation": "formal"
            },
            {
                "ko": "건기인데 먼지가 너무 많아 물 뿌려가며 작업하세요.",
                "vi": "Mùa khô bụi nhiều, phải tưới nước khi làm việc.",
                "situation": "onsite"
            },
            {
                "ko": "건기라 콘크리트 양생에 물 계속 줘야 해요.",
                "vi": "Mùa khô phải tưới nước liên tục để dưỡng hộ bê tông.",
                "situation": "informal"
            }
        ],
        "relatedTerms": ["mua-mua", "duong-ho-be-tong", "nhiet-do-cao", "bui-thi-cong"]
    },
    {
        "slug": "nhiet-do-cao",
        "korean": "고온",
        "vietnamese": "nhiệt độ cao",
        "hanja": "高溫",
        "hanjaReading": "高(높을 고) + 溫(따뜻할 온)",
        "pronunciation": "니엣 도 까오",
        "meaningKo": "기온이 높은 상태로, 베트남에서는 건기 한낮에 35~42도까지 올라갑니다. 통역 시 주의할 점은 한국의 '폭염(35도 이상)'과 베트남의 일상적 고온은 체감이 다르다는 것입니다. 베트남 현장에서는 고온 시 작업자 휴식 시간 확보, 음료 제공, 오전/저녁 집중 작업 등 안전 조치가 필수입니다. 또한 콘크리트 타설 시 급속 건조로 인한 균열 방지를 위해 타설 직후부터 살수 양생을 해야 하며, 아스팔트 작업은 고온에서 연화되므로 시공 품질에 주의해야 합니다. 한국인 관리자는 '더우면 쉬면 되지'라고 생각하지만, 베트남 노동법상 고온 작업 시 의무 휴식 시간이 있으므로 이를 공정에 반영해야 합니다.",
        "meaningVi": "Nhiệt độ không khí cao, thường 35~42°C vào mùa khô. Cần có biện pháp bảo vệ người lao động như nghỉ giải lao, cung cấp nước uống, điều chỉnh giờ làm việc sang buổi sáng sớm và chiều tối. Đổ bê tông trong thời tiết nóng cần tưới nước ngay sau khi đổ để tránh nứt nẻ. Luật lao động Việt Nam quy định giờ nghỉ bắt buộc khi nhiệt độ vượt ngưỡng an toàn.",
        "context": "안전 관리, 품질 관리, 노무 관리",
        "culturalNote": "한국은 여름 폭염이 7~8월 2개월 정도지만, 베트남은 3~5월 건기 말부터 9월까지 장기간 고온이 지속됩니다. 한국 현장에서는 '더워도 일한다'는 문화가 강하지만, 베트남에서는 고온 시 작업 효율이 급격히 떨어지고 안전사고가 증가합니다. 특히 한국인은 에어컨이 있는 사무실 기준으로 생각하지만, 베트남 현장 노동자는 직사광선 아래에서 일하므로 체감 온도가 훨씬 높습니다. 또한 베트남 북부는 한국처럼 여름만 덥지만, 남부는 연중 고온이므로 지역별 대응이 달라야 합니다.",
        "commonMistakes": [
            {
                "mistake": "trời nóng thì nghỉ (더우면 쉰다)",
                "correction": "nhiệt độ vượt 37°C phải nghỉ giải lao 15 phút/2 giờ theo quy định (37도 초과 시 2시간마다 15분 의무 휴식)",
                "explanation": "노동법상 구체적 기준을 명시해야 '임의 휴식'이 아닌 '법정 휴식'으로 이해됩니다."
            },
            {
                "mistake": "nóng như Hàn Quốc mùa hè (한국 여름처럼 덥다)",
                "correction": "Việt Nam nóng lâu hơn và ẩm hơn Hàn Quốc (베트남이 한국보다 더 오래, 더 습하게 덥다)",
                "explanation": "한국 폭염은 2개월, 베트남은 6개월 이상이며 습도도 높아 체감 온도가 다릅니다."
            },
            {
                "mistake": "đổ bê tông ban ngày cũng được (낮에 콘크리트 타설해도 된다)",
                "correction": "nhiệt độ cao nên ưu tiên đổ bê tông sáng sớm hoặc chiều tối (고온이므로 이른 아침이나 저녁 타설 우선)",
                "explanation": "한낮 고온에서는 콘크리트 급속 건조로 품질이 떨어지므로 시간대 조정이 필수입니다."
            }
        ],
        "examples": [
            {
                "ko": "오늘 기온이 38도 예상되므로 고소작업 시간을 조정하십시오.",
                "vi": "Hôm nay nhiệt độ dự kiến 38°C, phải điều chỉnh giờ tác nghiệp trên cao.",
                "situation": "formal"
            },
            {
                "ko": "너무 더워서 오전 7시부터 작업 시작하세요.",
                "vi": "Nóng quá, bắt đầu làm từ 7 giờ sáng.",
                "situation": "onsite"
            },
            {
                "ko": "고온 시 콘크리트 양생 물 자주 줘야 해요.",
                "vi": "Nhiệt độ cao phải tưới nước dưỡng hộ bê tông thường xuyên.",
                "situation": "informal"
            }
        ],
        "relatedTerms": ["mua-kho", "duong-ho-be-tong", "an-toan-lao-dong", "gio-lam-viec"]
    },
    {
        "slug": "gio-manh",
        "korean": "강풍",
        "vietnamese": "gió mạnh",
        "hanja": "強風",
        "hanjaReading": "強(강할 강) + 風(바람 풍)",
        "pronunciation": "조 만",
        "meaningKo": "바람이 세게 부는 기상 조건으로, 베트남에서는 태풍 시즌(8~11월)과 계절풍 전환기에 자주 발생합니다. 통역 시 중요한 것은 '풍속 기준'을 구체적으로 전달하는 것입니다. 한국 건설현장에서는 순간풍속 10m/s 이상 시 타워크레인 작업 중단이 일반적이지만, 베트남 현장에서는 이 기준이 명확하지 않아 사고가 빈번합니다. 특히 고층 건물 외부 마감 작업, 크레인 작업, 비계 작업 시 강풍은 치명적 위험 요소이므로 풍속계 설치와 실시간 모니터링이 필수입니다. 한국인 관리자는 '조금 바람 부는 정도'로 생각하지만, 베트남 해안 지역은 돌풍이 심하고 예측이 어려워 안전 기준을 엄격히 적용해야 합니다.",
        "meaningVi": "Điều kiện gió thổi mạnh, thường xảy ra trong mùa bão (tháng 8~11) và khi gió mùa chuyển hướng. Tiêu chuẩn an toàn phổ biến là dừng tác nghiệp cần cẩu khi gió vượt 10m/s. Công tác trên cao, lắp dựng giàn giáo, hoàn thiện ngoại thất đều phải theo dõi tốc độ gió liên tục. Vùng ven biển Việt Nam thường có gió giật mạnh khó dự báo, cần đặc biệt cẩn trọng.",
        "context": "안전 관리, 크레인 작업, 고소작업",
        "culturalNote": "한국은 태풍이 1년에 2~3개 상륙하는 정도지만, 베트남은 연간 10개 이상의 태풍이 영향을 미칩니다. 한국 현장에서는 태풍 예보 시 1~2일 전 사전 대비를 하지만, 베트남에서는 태풍 진로 변경이 잦아 '갑자기 작업 중단' 상황이 자주 발생합니다. 또한 한국은 크레인 풍속계가 의무이지만, 베트남 일부 현장에는 없어 관리자의 '감'으로 판단하는 경우가 있습니다. 한국인은 '바람 좀 부는데 왜 일 안 해?'라고 불만을 갖기 쉬우나, 실제 고소작업에서 강풍은 추락 사고로 직결되므로 안전 기준을 타협하면 안 됩니다.",
        "commonMistakes": [
            {
                "mistake": "gió hơi mạnh (바람이 좀 세다)",
                "correction": "tốc độ gió 12m/s, vượt mức cho phép (풍속 12m/s, 허용치 초과)",
                "explanation": "주관적 표현이 아니라 측정값으로 명확히 전달해야 안전 조치가 즉각 취해집니다."
            },
            {
                "mistake": "bão đến thì dừng (태풍 오면 중단)",
                "correction": "theo dõi dự báo, chuẩn bị trước 24 giờ (예보 모니터링, 24시간 전 대비)",
                "explanation": "태풍이 '오고 나서' 대응하면 늦으므로, 사전 대비 시점을 명확히 해야 합니다."
            },
            {
                "mistake": "cần cẩu không sợ gió (크레인은 바람 문제없다)",
                "correction": "cần cẩu phải dừng khi gió >10m/s theo tiêu chuẩn (크레인은 풍속 10m/s 초과 시 중단)",
                "explanation": "크레인 전도 사고는 대형 참사이므로, 절대 안전 기준을 무시하면 안 됩니다."
            }
        ],
        "examples": [
            {
                "ko": "현재 풍속 13m/s이므로 모든 크레인 작업을 즉시 중단하십시오.",
                "vi": "Tốc độ gió hiện tại 13m/s, lập tức dừng toàn bộ tác nghiệp cần cẩu.",
                "situation": "formal"
            },
            {
                "ko": "바람 너무 세니까 비계 작업 내일로 미루세요.",
                "vi": "Gió quá mạnh, hoãn tác nghiệp giàn giáo sang ngày mai.",
                "situation": "onsite"
            },
            {
                "ko": "태풍 예보 나왔어요. 자재 고정부터 확인하세요.",
                "vi": "Có dự báo bão, kiểm tra chằng buộc vật liệu trước.",
                "situation": "informal"
            }
        ],
        "relatedTerms": ["an-toan-lao-dong", "can-cau-thap", "tac-nghiep-tren-cao", "bao"]
    },
    {
        "slug": "muc-nuoc-ngam",
        "korean": "지하수위",
        "vietnamese": "mực nước ngầm",
        "hanja": "地下水位",
        "hanjaReading": "地(땅 지) + 下(아래 하) + 水(물 수) + 位(자리 위)",
        "pronunciation": "믹 느억 응암",
        "meaningKo": "지표면 아래 지하수가 위치한 깊이를 의미하며, 건설 현장에서는 기초 굴착과 지하 구조물 시공에 결정적 영향을 미칩니다. 통역 시 주의할 점은 베트남 남부(특히 메콩델타, 호치민)는 지하수위가 매우 높아(지표 1~2m) 기초 굴착 시 즉시 용수가 발생한다는 것입니다. 한국인 기술자는 서울 등 대도시 기준으로 '지하 5~10m' 수준을 예상하지만, 베트남 현장에서는 1~2m만 파도 물이 차오르므로 디워터링(배수) 장비가 필수입니다. 현장에서 '지하수위 조사 결과' 보고 시 지역별 차이(북부는 낮고, 남부는 높음)를 명확히 전달하고, 우기/건기에 따른 변동폭도 고려해야 합니다. 또한 지하수위가 높으면 흙막이 공사와 방수공사 비용이 크게 증가하므로 설계 변경이 필요할 수 있습니다.",
        "meaningVi": "Độ sâu mực nước dưới mặt đất, ảnh hưởng trực tiếp đến công tác đào móng và thi công công trình ngầm. Ở miền Nam (TP.HCM, đồng bằng sông Cửu Long) mực nước ngầm rất cao, chỉ 1~2m dưới mặt đất, nên cần hệ thống hút nước khi đào móng. Mực nước ngầm thay đổi theo mùa mưa/khô, cần khảo sát kỹ trước khi thiết kế móng và tầng hầm. Chi phí chống thấm và tường chắn đất tăng nhiều khi mực nước ngầm cao.",
        "context": "지질조사, 기초공사, 지하 구조물",
        "culturalNote": "한국은 도심 지역 대부분 지하수위가 깊어(지하 5~15m) 일반 건물 기초 굴착 시 배수 문제가 적지만, 베트남 남부는 거의 모든 현장에서 배수 펌프가 24시간 가동됩니다. 한국인 기술자는 '지하수위 보고서'를 형식적으로 보는 경우가 있으나, 베트남에서는 이 데이터가 공사비와 공기에 직접 영향을 미치므로 설계 단계부터 정밀 조사가 필수입니다. 또한 한국은 계절별 지하수위 변동이 적지만, 베트남은 우기 시 지하수위가 1~2m 상승하므로 건기 때 조사한 데이터만으로는 불충분합니다. 지하수위 대응 실패는 공사 중단으로 이어질 수 있습니다.",
        "commonMistakes": [
            {
                "mistake": "nước ngầm (지하수)",
                "correction": "mực nước ngầm (지하수위, 지하수면 높이)",
                "explanation": "'물' 자체가 아니라 '수위(높이)'를 말하는 것이므로 'mực'을 꼭 붙여야 합니다."
            },
            {
                "mistake": "Việt Nam và Hàn Quốc giống nhau (베트남과 한국 비슷하다)",
                "correction": "miền Nam Việt Nam mực nước ngầm cao hơn nhiều so với Hàn Quốc (베트남 남부는 한국보다 훨씬 높다)",
                "explanation": "지역별 차이를 무시하면 설계와 시공 계획이 완전히 틀어집니다."
            },
            {
                "mistake": "đào sâu là xong (깊이 파면 된다)",
                "correction": "đào sâu cần hút nước liên tục và gia cố thành hố đào (깊이 팔 때 지속 배수와 흙막이 보강 필수)",
                "explanation": "지하수위가 높은 곳에서는 단순 굴착이 아니라 배수+흙막이가 동시에 진행되어야 합니다."
            }
        ],
        "examples": [
            {
                "ko": "지하수위 조사 결과 지표 1.5m 지점이므로 디워터링 계획을 수립하십시오.",
                "vi": "Kết quả khảo sát mực nước ngầm ở độ sâu 1.5m, cần lập kế hoạch hút nước.",
                "situation": "formal"
            },
            {
                "ko": "여기 지하수위 높아서 조금만 파도 물 차요.",
                "vi": "Chỗ này mực nước ngầm cao, đào chút là ngập nước.",
                "situation": "onsite"
            },
            {
                "ko": "우기 때 지하수위 올라가니까 배수 펌프 추가하세요.",
                "vi": "Mùa mưa mực nước ngầm dâng, phải thêm máy bơm nước.",
                "situation": "informal"
            }
        ],
        "relatedTerms": ["tham-do-dia-chat", "dao-mong", "chong-tham", "dewateo-ring"]
    },
    {
        "slug": "dat-yeu",
        "korean": "연약지반",
        "vietnamese": "đất yếu",
        "hanja": "軟弱地盤",
        "hanjaReading": "軟(부드러울 연) + 弱(약할 약) + 地(땅 지) + 盤(소반 반)",
        "pronunciation": "닷 이에우",
        "meaningKo": "지지력이 약하고 압축성이 큰 지반으로, 점토, 실트, 이탄 등으로 구성되어 건물 하중을 지탱하기 어려운 토질을 의미합니다. 통역 시 주의할 점은 베트남 남부 메콩델타 지역과 호치민 일부 지역은 연약지반이 매우 광범위하여 지반 개량 없이는 건축이 불가능하다는 것입니다. 한국인 기술자는 서울 등 암반 지역 경험이 많아 '연약지반'을 특수 상황으로 보지만, 베트남 남부에서는 '기본 조건'입니다. 현장에서는 지반조사 결과 중 'N값(표준관입시험)'이 10 이하면 연약지반으로 판단하며, 말뚝 기초, 치환 공법, 다짐 등 지반 개량이 필수입니다. 또한 연약지반 위 시공 시 침하(가라앉음)가 장기간 발생하므로, 준공 후에도 모니터링이 필요하다는 점을 명확히 전달해야 합니다.",
        "meaningVi": "Nền đất có sức chịu tải thấp và độ nén cao, thường là sét, bùn, than bùn, không đủ khả năng chịu tải trọng công trình. Vùng đồng bằng sông Cửu Long và một số khu vực TP.HCM có đất yếu diện rộng, bắt buộc phải cải tạo nền hoặc dùng móng cọc. Tiêu chuẩn phổ biến: N-value <10 là đất yếu. Đất yếu gây lún công trình lâu dài, cần giám sát sau khi hoàn thành. Chi phí xử lý đất yếu chiếm tỷ trọng lớn trong tổng dự toán.",
        "context": "지질조사, 기초설계, 지반개량",
        "culturalNote": "한국은 산지가 많아 암반 또는 풍화토 지반이 일반적이지만, 베트남 남부는 충적토 평야로 연약지반이 기본입니다. 한국인 발주자는 '지반이 안 좋으면 말뚝 박으면 되지'라고 생각하지만, 베트남 연약지반은 깊이 20~30m까지 계속 무른 경우가 많아 말뚝 길이가 길어지고 비용이 급증합니다. 또한 한국은 지반조사를 1~2개 지점만 하는 경우가 있으나, 베트남 연약지반 지역은 수 미터 차이로 토질이 달라 밀도 높은 조사가 필요합니다. 지반 개량 공기를 과소평가하면 전체 공정이 지연되므로 초기 계획 시 충분한 기간을 배정해야 합니다.",
        "commonMistakes": [
            {
                "mistake": "đất xấu (나쁜 흙)",
                "correction": "đất yếu (연약지반, 지지력 부족 토질)",
                "explanation": "'나쁜'이라는 주관적 표현이 아니라 공학적 용어인 '연약지반'을 써야 합니다."
            },
            {
                "mistake": "đóng cọc là xong (말뚝 박으면 끝)",
                "correction": "phải khảo sát sâu để xác định chiều dài cọc phù hợp (심도 조사로 적정 말뚝 길이 결정 필요)",
                "explanation": "연약지반 깊이를 모르고 말뚝을 박으면 지지층에 도달하지 못해 침하가 발생합니다."
            },
            {
                "mistake": "đất yếu chỉ ở miền Nam (연약지반은 남부만)",
                "correction": "đất yếu chủ yếu ở đồng bằng sông Cửu Long, TP.HCM, một số vùng ven sông miền Bắc (주로 메콩델타, 호치민, 북부 일부 하천변)",
                "explanation": "베트남 전역이 아니라 특정 지역에 집중되어 있으므로 지역별 지질 데이터를 확인해야 합니다."
            }
        ],
        "examples": [
            {
                "ko": "지반조사 결과 N값 5 이하로 연약지반이므로 지반개량 공법을 검토하십시오.",
                "vi": "Kết quả khảo sát N-value dưới 5, là đất yếu, cần xem xét phương án cải tạo nền.",
                "situation": "formal"
            },
            {
                "ko": "이 지역 땅이 무르니까 중장비 함부로 진입하지 마세요.",
                "vi": "Khu này đất yếu, không được cho máy móc nặng vào lung tung.",
                "situation": "onsite"
            },
            {
                "ko": "호치민은 연약지반 많아서 기초공사비가 비싸요.",
                "vi": "TP.HCM có nhiều đất yếu nên chi phí móng cao.",
                "situation": "informal"
            }
        ],
        "relatedTerms": ["tham-do-dia-chat", "mong-coc", "cai-tao-nen", "N-value"]
    },
    {
        "slug": "dat-da",
        "korean": "암반",
        "vietnamese": "đất đá",
        "hanja": "岩盤",
        "hanjaReading": "岩(바위 암) + 盤(소반 반)",
        "pronunciation": "닷 다",
        "meaningKo": "단단한 암석으로 이루어진 지반으로, 건물의 지지력이 매우 우수한 이상적인 기초 조건입니다. 통역 시 주의할 점은 베트남어로 '암반'에 해당하는 정확한 단어가 없어 'đất đá(흙과 돌)'로 표현하거나 'đá gốc(기반암)', 'nền đá(암반층)'로 구분해야 한다는 것입니다. 한국인 기술자는 '암반=최고의 지반'으로 생각하지만, 베트남 현장에서는 암반 굴착이 어려워 오히려 공사비와 공기가 증가할 수 있습니다. 특히 베트남 북부 산지 지역은 암반이 많지만, 남부 평야는 거의 없어 지역별 차이가 큽니다. 현장에서 '암반 출현'을 보고할 때는 기초 설계에는 유리하나 굴착 장비(브레이커, 천공기)와 화약 발파 허가가 필요할 수 있음을 함께 전달해야 합니다.",
        "meaningVi": "Nền đá cứng, có sức chịu tải rất cao, là điều kiện lý tưởng cho móng công trình. Tuy nhiên, việc đào đá khó khăn hơn đất thường, cần máy đục (breaker), khoan phá (nếu được phép). Ở miền Bắc Việt Nam có nhiều vùng núi đá, miền Nam ít gặp. Khi gặp đá nền, thiết kế móng thuận lợi nhưng chi phí và thời gian đào đất tăng. Cần phân biệt 'đá gốc' (nền đá nguyên sinh) và 'đá lẫn' (đất có lẫn đá).",
        "context": "지질조사, 기초설계, 굴착공사",
        "culturalNote": "한국은 국토의 70%가 산지로 암반이 흔하고, 서울 등 대도시도 지하 얕은 곳에 화강암반이 나타나는 경우가 많습니다. 한국인 기술자는 '암반 나오면 좋다'는 인식이 강하지만, 베트남 남부 충적층 지역 기술자는 '암반=굴착 어려움'으로 인식합니다. 또한 한국은 발파 허가가 비교적 쉽지만, 베트남 도심에서는 소음/진동 규제로 발파가 금지되는 경우가 많아 기계식 파쇄만 가능합니다. 암반 조사 시 한국에서는 '암질 등급(RMR, RQD)'을 정밀 조사하지만, 베트남 일부 현장에서는 '돌 나왔다' 수준의 간략한 보고만 하는 경우가 있어 주의가 필요합니다.",
        "commonMistakes": [
            {
                "mistake": "đá (돌)",
                "correction": "đá gốc/nền đá (기반암, 암반층)",
                "explanation": "일반 '돌'과 '암반'을 구분해야 지반 조건을 정확히 전달할 수 있습니다."
            },
            {
                "mistake": "có đá là tốt (돌 나오면 좋다)",
                "correction": "nền đá chịu tải tốt nhưng khó đào (암반은 지지력 좋으나 굴착 어려움)",
                "explanation": "장단점을 함께 전달하지 않으면 일정과 예산에 문제가 생깁니다."
            },
            {
                "mistake": "nổ mìn là xong (발파하면 끝)",
                "correction": "khu đô thị thường cấm nổ mìn, chỉ dùng máy đục (도심은 발파 금지, 브레이커만 사용)",
                "explanation": "베트남 도심 규제를 모르고 발파 계획을 세우면 공법 변경으로 공기 지연이 발생합니다."
            }
        ],
        "examples": [
            {
                "ko": "지하 5m에서 암반이 출현하여 기초 설계를 직접기초로 변경하겠습니다.",
                "vi": "Gặp nền đá ở độ sâu 5m, sẽ thay đổi thiết kế móng sang móng trực tiếp.",
                "situation": "formal"
            },
            {
                "ko": "여기 암반이라 브레이커로 깨야 해요.",
                "vi": "Chỗ này đá nền phải dùng máy đục.",
                "situation": "onsite"
            },
            {
                "ko": "북부 산지는 암반 많아서 굴착비 많이 들어요.",
                "vi": "Miền Bắc vùng núi nhiều đá nền nên chi phí đào cao.",
                "situation": "informal"
            }
        ],
        "relatedTerms": ["tham-do-dia-chat", "dao-mong", "pha-da", "mong-truc-tiep"]
    },
    {
        "slug": "dia-chat",
        "korean": "지질",
        "vietnamese": "địa chất",
        "hanja": "地質",
        "hanjaReading": "地(땅 지) + 質(바탕 질)",
        "pronunciation": "디아 짯",
        "meaningKo": "땅을 구성하는 암석, 토양, 지층의 성질과 구조를 총칭하는 용어로, 건설 현장에서는 지반의 공학적 특성을 파악하는 핵심 정보입니다. 통역 시 중요한 점은 '지질조사'가 단순히 땅 파보는 것이 아니라 시추, 토질시험, N값 측정 등 체계적 절차임을 명확히 해야 한다는 것입니다. 한국인 기술자는 '지질보고서'를 설계 기초 자료로 중시하지만, 베트남 일부 현장에서는 간략한 조사만 하고 시공 중 문제가 발생하는 경우가 있습니다. 현장에서 '지질이 예상과 다르다'는 보고를 받으면 설계 변경과 추가 비용이 발생할 수 있으므로, 초기 조사를 충분히 해야 하며, 베트남 남부는 충적층, 북부는 풍화암/암반이 주를 이룬다는 지역별 특성을 공유해야 합니다.",
        "meaningVi": "Tính chất và cấu trúc của đất đá, lớp đất tạo nên nền móng. Khảo sát địa chất bao gồm khoan thăm dò, thí nghiệm đất, đo N-value để xác định sức chịu tải. Báo cáo địa chất là cơ sở thiết kế móng. Miền Nam Việt Nam chủ yếu là đất phù sa (충적토), miền Bắc có nhiều đá phong hóa và nền đá. Khảo sát không kỹ dẫn đến phát sinh thiết kế và chi phí trong thi công.",
        "context": "지질조사, 설계, 기초공사",
        "culturalNote": "한국은 지질조사를 설계 전 필수 단계로 보며, 대형 프로젝트는 수십 개 시추공으로 정밀 조사합니다. 베트남에서도 법적으로 지질조사가 의무이지만, 중소형 프로젝트에서는 비용 절감을 위해 최소한만 하는 경우가 있어 시공 중 '지질이 다르다'는 클레임이 빈번합니다. 한국인은 '지질보고서 = 신뢰할 수 있는 데이터'로 보지만, 베트남에서는 시추 위치가 대표성을 갖지 못할 수 있으므로 여유 있는 안전율 적용이 필요합니다. 또한 한국은 겨울 동결심도를 고려하지만, 베트남은 동결이 없어 기초 깊이 기준이 다릅니다.",
        "commonMistakes": [
            {
                "mistake": "đất (흙)",
                "correction": "địa chất (지질, 지반 구성 전체)",
                "explanation": "'흙'은 표층 토양만 지칭하고, '지질'은 심부 지층 구조까지 포함하는 넓은 개념입니다."
            },
            {
                "mistake": "xem đất là biết (땅 보면 안다)",
                "correction": "phải khảo sát khoan, thí nghiệm mới biết chính xác (시추, 시험해야 정확히 안다)",
                "explanation": "육안이나 경험만으로는 지하 지질을 알 수 없으므로 과학적 조사가 필수입니다."
            },
            {
                "mistake": "địa chất Việt Nam đồng nhất (베트남 지질 동일)",
                "correction": "miền Nam phù sa, miền Bắc núi đá, Tây Nguyên bazan (남부 충적토, 북부 산악암석, 중부고원 현무암)",
                "explanation": "베트남은 남북 1,600km로 지역별 지질이 완전히 다릅니다."
            }
        ],
        "examples": [
            {
                "ko": "지질조사 결과를 바탕으로 기초 형식을 결정하겠습니다.",
                "vi": "Dựa trên kết quả khảo sát địa chất sẽ quyết định loại móng.",
                "situation": "formal"
            },
            {
                "ko": "여기 지질이 예상과 달라서 설계 변경 필요해요.",
                "vi": "Địa chất chỗ này khác dự kiến, cần thay đổi thiết kế.",
                "situation": "onsite"
            },
            {
                "ko": "지질 보고서 보니까 지하수위 높네요.",
                "vi": "Xem báo cáo địa chất thấy mực nước ngầm cao.",
                "situation": "informal"
            }
        ],
        "relatedTerms": ["tham-do-dia-chat", "dat-yeu", "dat-da", "muc-nuoc-ngam"]
    },
    {
        "slug": "tham-do-dia-chat",
        "korean": "지질조사",
        "vietnamese": "thăm dò địa chất",
        "hanja": "地質調査",
        "hanjaReading": "地(땅 지) + 質(바탕 질) + 調(고를 조) + 査(조사할 사)",
        "pronunciation": "탐 도 디아 짯",
        "meaningKo": "건설 예정 부지의 지반 특성을 파악하기 위해 시추, 토질시험, 지하수위 측정 등을 수행하는 조사 작업입니다. 통역 시 주의할 점은 '지질조사'가 단순히 땅을 파보는 것이 아니라, 보링(시추), 표준관입시험(SPT, N값 측정), 실내 토질시험(압밀, 전단, 입도분석 등) 등 다단계 과학적 절차임을 명확히 해야 합니다. 한국에서는 지질조사가 설계 전 필수 단계로 자리 잡았지만, 베트남 일부 중소형 프로젝트에서는 비용 절감을 위해 최소한의 조사만 하거나 건너뛰는 경우가 있어 시공 중 지반 문제로 분쟁이 발생합니다. 현장에서는 조사 깊이(보통 지하 20~30m 또는 암반층까지), 시추공 개수(부지 면적당), 시험 항목을 구체적으로 협의하고, 베트남 남부는 연약지반+고지하수위, 북부는 풍화암/암반 중심으로 조사 초점이 다르다는 점을 공유해야 합니다.",
        "meaningVi": "Công tác khảo sát đặc tính nền đất bằng khoan thăm dò, thí nghiệm SPT (đo N-value), thí nghiệm trong phòng (nén cố kết, cắt, phân tích hạt). Là bước bắt buộc trước khi thiết kế móng. Ở Việt Nam, một số dự án nhỏ bỏ qua hoặc khảo sát sơ sài dẫn đến phát sinh trong thi công. Miền Nam cần tập trung khảo sát đất yếu và mực nước ngầm, miền Bắc cần xác định độ sâu và cấp độ đá ph풍화. Độ sâu khoan thường 20~30m hoặc đến khi gặp nền đá.",
        "context": "설계 준비, 기초 계획, 리스크 관리",
        "culturalNote": "한국에서는 '지질조사 = 설계 기본 자료'로 인식하며, 대형 프로젝트는 수천만 원 이상 조사비를 투입합니다. 베트남에서도 법적으로 의무이지만, 실제로는 '조사 안 하고 시작했다가 문제 생긴다'는 사례가 적지 않습니다. 한국인 발주자는 '보고서만 있으면 된다'고 생각하지만, 베트남에서는 보고서 품질 편차가 크므로 신뢰할 수 있는 조사기관 선정이 중요합니다. 또한 한국은 조사 후 즉시 설계에 반영하지만, 베트남은 조사→설계 사이 시간이 길어지면 우기/건기로 지하수위가 변동할 수 있으므로 재조사가 필요할 수 있습니다.",
        "commonMistakes": [
            {
                "mistake": "khảo sát đất (땅 조사)",
                "correction": "thăm dò địa chất (지질조사, 시추+시험)",
                "explanation": "'땅 조사'는 표층 확인만 연상시키고, '지질조사'는 심부 시추와 정밀 시험을 포함합니다."
            },
            {
                "mistake": "khoan 1 lỗ là đủ (시추공 1개면 충분)",
                "correction": "cần nhiều lỗ khoan tùy diện tích (부지 면적에 따라 다수 시추공 필요)",
                "explanation": "부지가 넓거나 지질이 불균일하면 1개 시추공으로는 대표성이 없습니다."
            },
            {
                "mistake": "có báo cáo cũ dùng lại (예전 보고서 재사용)",
                "correction": "mỗi dự án phải khảo sát riêng, vị trí khác thì địa chất khác (프로젝트마다 별도 조사, 위치 다르면 지질 다름)",
                "explanation": "인접 부지라도 지하 지층은 다를 수 있으므로 반드시 해당 부지 조사가 필요합니다."
            }
        ],
        "examples": [
            {
                "ko": "설계 전에 지질조사를 완료하여 기초 형식을 확정하겠습니다.",
                "vi": "Sẽ hoàn thành thăm dò địa chất trước khi thiết kế để xác định loại móng.",
                "situation": "formal"
            },
            {
                "ko": "시추 결과 지하 15m까지 연약지반이래요.",
                "vi": "Kết quả khoan thấy đất yếu đến độ sâu 15m.",
                "situation": "onsite"
            },
            {
                "ko": "지질조사비 아끼려다 나중에 더 들어요.",
                "vi": "Tiết kiệm chi phí thăm dò địa chất rồi sau tốn hơn.",
                "situation": "informal"
            }
        ],
        "relatedTerms": ["dia-chat", "dat-yeu", "dat-da", "muc-nuoc-ngam", "N-value"]
    }
]

# 중복 필터링 (CRITICAL RULE 5)
filtered_terms = [term for term in new_terms if term['slug'] not in existing_slugs]

# 기존 데이터에 추가
data.extend(filtered_terms)

# 저장 (use None, NOT null - CRITICAL RULE 3)
with open(file_path, 'w', encoding='utf-8') as f:
    json.dump(data, f, ensure_ascii=False, indent=2)

print(f"✅ {len(filtered_terms)}개 용어 추가 완료 (중복 {len(new_terms) - len(filtered_terms)}개 제외)")
print(f"📁 파일: {file_path}")
print(f"📊 전체 용어 수: {len(data)}개")
