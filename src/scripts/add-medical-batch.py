#!/usr/bin/env python3
"""Medical 용어 배치 추가 - 질병/증상 카테고리"""
import json, os

path = os.path.join(os.path.dirname(__file__), '../data/terms/medical.json')
with open(path, 'r', encoding='utf-8') as f:
    data = json.load(f)

existing = {t['slug'] for t in data}

def t(slug, ko, vi, hanja, hr, pron, mko, mvi, ctx, cn, cm, ex, rt):
    return {"slug":slug,"korean":ko,"vietnamese":vi,"hanja":hanja,"hanjaReading":hr,
            "pronunciation":pron,"meaningKo":mko,"meaningVi":mvi,"context":ctx,
            "culturalNote":cn,"commonMistakes":cm,"examples":ex,"relatedTerms":rt}

new = [
    t("viem-gan-c","C형간염","viêm gan C","C型肝炎",None,"ssi-hyeong-gan-yeom",
      "C형 간염 바이러스(HCV)에 의한 간 감염 질환입니다. 혈액을 통해 전염되며 만성화되면 간경변, 간암으로 진행할 수 있습니다. 최근 직접작용항바이러스제(DAA)로 완치율이 95% 이상입니다. 통역 시 전염 경로, 치료 가능성, 정기 검진의 중요성을 강조해야 합니다.",
      "Bệnh nhiễm virus viêm gan C (HCV) qua đường máu, có thể chữa khỏi với thuốc kháng virus",
      "감염내과, 소화기내과",
      "한국에서 C형간염은 건강검진 시 선별검사가 권장됩니다. 베트남도 유병률이 높아 검사와 치료의 중요성을 설명해야 합니다.",
      [{"mistake":"B형간염과 C형간염 구분 안 함","correction":"B형은 백신 있고, C형은 백신 없지만 완치 가능","explanation":"두 질환의 예방과 치료가 다릅니다"},
       {"mistake":"치료 불가능하다고 설명","correction":"최신 약물로 95% 이상 완치됨을 안내","explanation":"환자에게 희망을 줄 수 있는 정보입니다"},
       {"mistake":"전염 경로 설명 부족","correction":"혈액 접촉(주사, 문신 등)으로 전염됨을 설명","explanation":"예방을 위한 교육이 필요합니다"}],
      [{"ko":"C형간염 검사 결과 양성입니다.","vi":"Kết quả xét nghiệm viêm gan C dương tính.","situation":"formal"},
       {"ko":"치료하면 완치될 수 있습니다.","vi":"Điều trị thì có thể chữa khỏi.","situation":"formal"},
       {"ko":"C형간염은 요즘 약으로 다 나아요.","vi":"Viêm gan C bây giờ uống thuốc là khỏi.","situation":"informal"}],
      ["간경변","간암","항바이러스제"]),

    t("benh-parkinson","파킨슨병","bệnh Parkinson","파킨슨病",None,"pa-kin-seun-byeong",
      "뇌의 도파민 신경세포가 소실되어 발생하는 신경퇴행성 질환입니다. 떨림, 경직, 서동증, 자세 불안정이 주요 증상입니다. 완치는 어렵지만 약물과 재활로 증상 조절이 가능합니다. 통역 시 진행성 질환임을 설명하되 관리로 삶의 질 유지가 가능함을 강조해야 합니다.",
      "Bệnh thoái hóa thần kinh do mất tế bào thần kinh dopamin, gây run, cứng cơ, chậm vận động",
      "신경과",
      "한국에서 파킨슨병 환자는 꾸준히 증가하고 있습니다. 장기 치료가 필요하므로 환자와 가족 모두의 이해와 협조가 중요합니다.",
      [{"mistake":"치매와 파킨슨병 혼동","correction":"파킨슨병은 운동장애, 치매는 인지장애가 주증상","explanation":"두 질환은 다르지만 파킨슨병 말기에 치매 동반 가능"},
       {"mistake":"완치 가능하다고 오해","correction":"완치는 어렵지만 증상 조절로 일상생활 가능","explanation":"현실적인 기대를 갖도록 설명합니다"},
       {"mistake":"약물 부작용 설명 누락","correction":"이상운동증 등 장기 복용 부작용 안내","explanation":"약물 조절의 중요성을 이해시킵니다"}],
      [{"ko":"파킨슨병 진단을 받으셨습니다.","vi":"Bạn được chẩn đoán mắc bệnh Parkinson.","situation":"formal"},
       {"ko":"약을 꾸준히 드시면 증상 조절이 됩니다.","vi":"Uống thuốc đều đặn sẽ kiểm soát được triệu chứng.","situation":"formal"},
       {"ko":"손이 떨리는 건 파킨슨 증상이에요.","vi":"Tay run là triệu chứng của Parkinson.","situation":"informal"}],
      ["떨림","도파민","뇌심부자극술"]),

    t("ung-thu-phoi","폐암","ung thư phổi","肺癌","폐(허파 폐) + 암(암 암)","pye-am",
      "폐에서 발생하는 악성 종양으로, 흡연이 가장 큰 위험요인입니다. 비소세포폐암과 소세포폐암으로 구분됩니다. 초기에는 증상이 없어 발견이 늦어지는 경우가 많습니다. 통역 시 병기, 치료 방법(수술, 항암, 방사선, 표적치료), 예후를 정확히 전달해야 합니다.",
      "Khối u ác tính ở phổi, hút thuốc là yếu tố nguy cơ lớn nhất",
      "호흡기내과, 흉부외과, 종양내과",
      "한국에서 폐암은 암 사망률 1위입니다. 저선량 CT로 조기 발견이 가능하며, 표적치료와 면역치료의 발전으로 생존율이 향상되고 있습니다.",
      [{"mistake":"폐암을 모두 같은 병으로 설명","correction":"비소세포폐암, 소세포폐암의 치료와 예후가 다름을 설명","explanation":"세포 유형에 따라 치료 방침이 다릅니다"},
       {"mistake":"흡연력만 강조","correction":"비흡연자도 폐암 발생 가능함을 안내","explanation":"대기오염, 유전 등 다른 요인도 있습니다"},
       {"mistake":"병기 설명 부족","correction":"1~4기의 의미와 치료 방향을 명확히 설명","explanation":"환자가 자신의 상태를 이해해야 합니다"}],
      [{"ko":"폐암 3기로 진단되었습니다.","vi":"Được chẩn đoán ung thư phổi giai đoạn 3.","situation":"formal"},
       {"ko":"표적치료제가 효과가 있습니다.","vi":"Thuốc nhắm trúng đích có hiệu quả.","situation":"formal"},
       {"ko":"담배 안 피워도 폐암 걸릴 수 있어요.","vi":"Không hút thuốc cũng có thể bị ung thư phổi.","situation":"informal"}],
      ["흉부CT","조직검사","표적치료"]),

    t("ung-thu-da-day","위암","ung thư dạ dày","胃癌","위(밥통 위) + 암(암 암)","wi-am",
      "위 점막에서 발생하는 악성 종양입니다. 한국인에게 흔한 암으로, 조기 발견 시 내시경 절제로 완치가 가능합니다. 헬리코박터균 감염, 짠 음식, 가족력 등이 위험요인입니다. 통역 시 조기위암과 진행성위암의 치료 차이, 수술 후 식이 관리 등을 설명해야 합니다.",
      "Khối u ác tính ở niêm mạc dạ dày, phổ biến ở người Hàn Quốc",
      "소화기내과, 외과, 종양내과",
      "한국은 위암 발생률이 높아 국가암검진에 포함됩니다. 40세 이상은 2년마다 위내시경을 권장하며, 조기 발견으로 생존율이 크게 향상됩니다.",
      [{"mistake":"위암 진단을 곧 사망으로 연결","correction":"조기위암은 90% 이상 완치됨을 강조","explanation":"환자에게 희망을 줄 수 있는 정보입니다"},
       {"mistake":"내시경 절제와 수술 구분 안 함","correction":"조기암은 내시경, 진행암은 수술이 필요함을 설명","explanation":"치료 방법이 다릅니다"},
       {"mistake":"수술 후 식이 설명 부족","correction":"소량씩 자주 먹기, 덤핑증후군 주의 등 안내","explanation":"위 절제 후 생활 적응이 필요합니다"}],
      [{"ko":"조기위암으로 내시경 절제가 가능합니다.","vi":"Ung thư dạ dày giai đoạn sớm có thể cắt bằng nội soi.","situation":"formal"},
       {"ko":"위 전절제술이 필요합니다.","vi":"Cần phẫu thuật cắt toàn bộ dạ dày.","situation":"formal"},
       {"ko":"일찍 발견해서 다행이에요.","vi":"May mà phát hiện sớm.","situation":"informal"}],
      ["위내시경","헬리코박터","항암치료"]),

    t("ung-thu-gan","간암","ung thư gan","肝癌","간(간 간) + 암(암 암)","gan-am",
      "간에서 발생하는 악성 종양으로, B형/C형 간염, 간경변, 음주가 주요 위험요인입니다. 초기 증상이 없어 간염/간경변 환자는 정기검진이 필수입니다. 치료는 수술, 고주파열치료, 색전술, 표적치료 등이 있습니다. 통역 시 기저 간질환 관리의 중요성을 강조해야 합니다.",
      "Khối u ác tính ở gan, liên quan đến viêm gan B/C, xơ gan, rượu",
      "소화기내과, 외과, 종양내과",
      "한국에서 간암은 B형간염과 밀접한 관련이 있습니다. 고위험군(간경변, 만성간염)은 6개월마다 초음파와 혈액검사(AFP)를 권장합니다.",
      [{"mistake":"간암을 간경변과 혼동","correction":"간경변은 간암의 위험요인, 간암은 악성종양","explanation":"두 질환의 관계를 명확히 설명합니다"},
       {"mistake":"치료 방법 설명 부족","correction":"수술, 색전술, 고주파치료, 표적치료 등 다양한 방법 안내","explanation":"환자 상태에 따라 치료법이 다릅니다"},
       {"mistake":"정기검진 중요성 미강조","correction":"간염/간경변 환자는 6개월마다 검사 필요","explanation":"조기 발견이 생존율을 높입니다"}],
      [{"ko":"간암 의심 소견이 있어 추가 검사가 필요합니다.","vi":"Có nghi ngờ ung thư gan nên cần xét nghiệm thêm.","situation":"formal"},
       {"ko":"고주파열치료로 종양을 태울 수 있습니다.","vi":"Có thể đốt khối u bằng sóng cao tần.","situation":"formal"},
       {"ko":"간경변 있으면 정기검사 꼭 받으세요.","vi":"Nếu bị xơ gan thì phải khám định kỳ.","situation":"informal"}],
      ["간경변","B형간염","AFP"]),

    t("ung-thu-dai-trang","대장암","ung thư đại tràng","大腸癌","대(큰 대) + 장(창자 장) + 암(암 암)","dae-jang-am",
      "대장(결장, 직장)에서 발생하는 악성 종양입니다. 대부분 용종에서 시작되어 암으로 진행됩니다. 50세 이상, 가족력, 염증성 장질환이 위험요인입니다. 통역 시 용종 제거로 예방 가능함, 수술 후 장루 가능성 등을 설명해야 합니다.",
      "Khối u ác tính ở đại tràng (ruột già), thường phát triển từ polyp",
      "소화기내과, 외과, 종양내과",
      "한국에서 대장암은 발생률이 높아 50세 이상 국가암검진 대상입니다. 대장내시경으로 용종을 제거하면 암 예방이 가능합니다.",
      [{"mistake":"대장암과 직장암 구분 안 함","correction":"직장암은 항문에 가까워 치료 방법이 다를 수 있음","explanation":"위치에 따라 수술 방법과 장루 여부가 달라집니다"},
       {"mistake":"장루(인공항문) 설명 회피","correction":"직장암 수술 시 장루가 필요할 수 있음을 미리 안내","explanation":"환자가 심리적으로 준비할 수 있게 합니다"},
       {"mistake":"용종과 암의 관계 미설명","correction":"용종 단계에서 제거하면 암 예방 가능","explanation":"예방 검진의 중요성을 강조합니다"}],
      [{"ko":"대장암 2기로 수술이 필요합니다.","vi":"Ung thư đại tràng giai đoạn 2 cần phẫu thuật.","situation":"formal"},
       {"ko":"수술 후 항암치료를 받으셔야 합니다.","vi":"Sau phẫu thuật cần hóa trị.","situation":"formal"},
       {"ko":"용종 있을 때 떼면 암 안 걸려요.","vi":"Cắt polyp sớm thì không bị ung thư.","situation":"informal"}],
      ["대장내시경","용종","장루"]),

    t("ung-thu-vu","유방암","ung thư vú","乳房癌","유(젖 유) + 방(방 방) + 암(암 암)","yu-bang-am",
      "유방 조직에서 발생하는 악성 종양으로, 여성 암 중 가장 흔합니다. 자가검진, 유방촬영, 초음파로 조기 발견이 가능합니다. 호르몬 수용체, HER2 상태에 따라 치료가 다릅니다. 통역 시 유방 보존술과 전절제술의 차이, 보조 치료의 중요성을 설명해야 합니다.",
      "Khối u ác tính ở mô vú, phổ biến nhất ở phụ nữ",
      "유방외과, 종양내과",
      "한국에서 유방암은 40세 이상 여성 국가암검진 대상입니다. 조기 발견 시 유방 보존술이 가능하고 생존율이 높습니다.",
      [{"mistake":"유방암 진단을 유방 전절제로만 연결","correction":"조기암은 유방 보존술로 치료 가능","explanation":"환자의 불안을 줄여줍니다"},
       {"mistake":"호르몬 치료 설명 부족","correction":"호르몬 수용체 양성이면 5-10년 호르몬 치료 필요","explanation":"장기 치료 계획을 설명합니다"},
       {"mistake":"유전성 유방암 설명 누락","correction":"BRCA 유전자 변이 시 가족 검사 권고","explanation":"가족 상담이 필요할 수 있습니다"}],
      [{"ko":"유방암 1기로 유방 보존술이 가능합니다.","vi":"Ung thư vú giai đoạn 1 có thể mổ bảo tồn vú.","situation":"formal"},
       {"ko":"호르몬 치료를 5년간 받으셔야 합니다.","vi":"Cần điều trị hormone trong 5 năm.","situation":"formal"},
       {"ko":"일찍 발견해서 가슴 안 떼도 돼요.","vi":"Phát hiện sớm nên không cần cắt ngực.","situation":"informal"}],
      ["유방촬영","BRCA","호르몬치료"]),

    t("ung-thu-tuyen-giap","갑상선암","ung thư tuyến giáp","甲狀腺癌","갑(갑옷 갑) + 상(모양 상) + 선(샘 선) + 암(암 암)","gap-sang-seon-am",
      "갑상선에서 발생하는 악성 종양으로, 한국에서 가장 많이 진단되는 암입니다. 대부분 유두암으로 예후가 좋습니다. 초음파 검사로 발견되며, 수술이 주 치료입니다. 통역 시 예후가 좋은 암임을 설명하되 평생 갑상선 호르몬제 복용이 필요함을 안내해야 합니다.",
      "Khối u ác tính ở tuyến giáp, phổ biến nhất ở Hàn Quốc, tiên lượng tốt",
      "내분비외과, 핵의학과",
      "한국에서 갑상선암은 가장 많이 발견되는 암이지만 생존율이 매우 높습니다. 과잉 진단 논란도 있어 관찰 가능한 경우도 있음을 설명합니다.",
      [{"mistake":"갑상선암을 다른 암처럼 심각하게 설명","correction":"대부분 예후가 좋고 완치율이 높음을 안내","explanation":"환자의 과도한 불안을 줄여줍니다"},
       {"mistake":"평생 약 복용 설명 누락","correction":"갑상선 제거 후 호르몬제 평생 복용 필요","explanation":"수술 후 관리에 대해 미리 안내합니다"},
       {"mistake":"방사성요오드 치료 설명 부족","correction":"재발 방지를 위해 필요할 수 있음을 설명","explanation":"추가 치료 가능성을 안내합니다"}],
      [{"ko":"갑상선 유두암으로 수술이 필요합니다.","vi":"Ung thư tuyến giáp thể nhú cần phẫu thuật.","situation":"formal"},
       {"ko":"수술 후 평생 호르몬제를 드셔야 합니다.","vi":"Sau mổ phải uống thuốc hormone suốt đời.","situation":"formal"},
       {"ko":"갑상선암은 착한 암이라 너무 걱정 마세요.","vi":"Ung thư tuyến giáp tiên lượng tốt, đừng lo quá.","situation":"informal"}],
      ["갑상선초음파","방사성요오드","갑상선호르몬"]),

    t("dot-quy","뇌졸중","đột quỵ","腦卒中","뇌(골 뇌) + 졸(갑자기 졸) + 중(가운데 중)","noe-jol-jung",
      "뇌혈관이 막히거나(허혈성) 터져서(출혈성) 뇌 손상이 발생하는 응급 질환입니다. 얼굴 처짐, 팔 힘 약화, 언어 장애가 주요 증상입니다. 골든타임(4.5시간) 내 치료가 중요합니다. 통역 시 증상 인지와 즉시 응급실 방문의 중요성을 강조해야 합니다.",
      "Bệnh cấp cứu do mạch máu não bị tắc hoặc vỡ, cần điều trị trong thời gian vàng",
      "신경과, 응급의학과",
      "한국에서 뇌졸중은 주요 사망원인이자 장애 원인입니다. 베트남어 'đột quỵ'는 뇌졸중을 정확히 표현하며, 증상 발생 시 즉시 119 호출이 중요합니다.",
      [{"mistake":"뇌졸중과 뇌출혈 구분 안 함","correction":"뇌졸중은 허혈성(뇌경색)과 출혈성(뇌출혈) 모두 포함","explanation":"치료 방법이 다르므로 구분이 필요합니다"},
       {"mistake":"골든타임 설명 누락","correction":"4.5시간 내 혈전용해제 투여 가능, 빠른 치료가 중요","explanation":"시간이 예후를 결정합니다"},
       {"mistake":"증상 설명 부족","correction":"FAST(얼굴, 팔, 언어, 시간) 증상 교육","explanation":"빠른 인지가 생명을 살립니다"}],
      [{"ko":"뇌졸중으로 응급 치료가 필요합니다.","vi":"Đột quỵ cần điều trị cấp cứu.","situation":"formal"},
       {"ko":"4시간 30분 내에 치료를 시작해야 합니다.","vi":"Phải bắt đầu điều trị trong vòng 4 tiếng 30 phút.","situation":"formal"},
       {"ko":"갑자기 말이 어눌해지면 바로 응급실 가세요.","vi":"Nếu đột nhiên nói ngọng thì đi cấp cứu ngay.","situation":"informal"}],
      ["뇌경색","뇌출혈","혈전용해제"]),

    t("nhoi-mau-co-tim","심근경색","nhồi máu cơ tim","心筋梗塞","심(마음 심) + 근(힘줄 근) + 경(막힐 경) + 색(막힐 색)","sim-geun-gyeong-saek",
      "관상동맥이 막혀 심장 근육에 혈액이 공급되지 않아 심장 근육이 괴사하는 응급 질환입니다. 흉통, 호흡곤란, 식은땀이 주요 증상입니다. 스텐트 시술이나 우회술로 치료합니다. 통역 시 가슴 통증 발생 시 즉시 응급실 방문, 니트로글리세린 사용법을 안내해야 합니다.",
      "Bệnh cấp cứu do động mạch vành bị tắc, cơ tim không được cung cấp máu",
      "심장내과, 응급의학과",
      "한국에서 심근경색은 돌연사의 주요 원인입니다. 흉통이 30분 이상 지속되면 즉시 119에 연락해야 합니다. 베트남어로는 'nhồi máu cơ tim' 또는 'đau tim'으로 표현합니다.",
      [{"mistake":"협심증과 심근경색 구분 안 함","correction":"협심증은 일시적 허혈, 심근경색은 괴사까지 진행","explanation":"심근경색이 더 위급합니다"},
       {"mistake":"증상 설명 부족","correction":"가슴을 쥐어짜는 통증, 턱이나 팔로 퍼지는 통증 설명","explanation":"비전형적 증상도 안내합니다"},
       {"mistake":"응급 대처법 미설명","correction":"아스피린 복용, 안정, 119 호출 안내","explanation":"첫 대처가 생존율에 영향을 미칩니다"}],
      [{"ko":"심근경색으로 응급 시술이 필요합니다.","vi":"Nhồi máu cơ tim cần can thiệp cấp cứu.","situation":"formal"},
       {"ko":"스텐트를 넣어 막힌 혈관을 뚫겠습니다.","vi":"Sẽ đặt stent để thông mạch máu bị tắc.","situation":"formal"},
       {"ko":"가슴이 아프고 식은땀 나면 바로 119 부르세요.","vi":"Nếu đau ngực và đổ mồ hôi lạnh thì gọi 119 ngay.","situation":"informal"}],
      ["협심증","스텐트","관상동맥"]),
]

# 중복 제거 후 추가
added = [n for n in new if n['slug'] not in existing]
data.extend(added)
print(f"추가: {len(added)}개, 총: {len(data)}개")

with open(path, 'w', encoding='utf-8') as f:
    json.dump(data, f, ensure_ascii=False, indent=2)
print("저장 완료")
