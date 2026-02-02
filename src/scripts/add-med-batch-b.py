#!/usr/bin/env python3
import json, os
path = os.path.join(os.path.dirname(__file__), '../data/terms/medical.json')
with open(path, 'r', encoding='utf-8') as f: data = json.load(f)
existing = {t['slug'] for t in data}

def t(s,k,v,mk,mv,cx,cn,cm,ex,rt):
    return {"slug":s,"korean":k,"vietnamese":v,"hanja":None,"hanjaReading":None,"pronunciation":s,"meaningKo":mk,"meaningVi":mv,"context":cx,"culturalNote":cn,"commonMistakes":cm,"examples":ex,"relatedTerms":rt}

new = [
t("viem-mang-nao","뇌수막염","viêm màng não","뇌와 척수를 감싸는 막에 염증이 생기는 질환입니다. 두통, 고열, 목 경직이 특징입니다. 세균성은 응급, 바이러스성은 대부분 자연 회복됩니다. 통역 시 응급성 판단, 치료 방향을 설명해야 합니다.",
"Viêm màng bao quanh não và tủy sống gây đau đầu, sốt cao, cứng cổ","감염내과, 신경과","한국에서 세균성뇌수막염은 응급 상황입니다. 예방접종으로 일부 예방 가능합니다.",
[{"mistake":"모든 뇌수막염이 위험하다고만 설명","correction":"세균성은 응급, 바이러스성은 대부분 경증","explanation":"불필요한 공포를 줄입니다"},
{"mistake":"요추천자 검사 설명 부족","correction":"확진을 위해 뇌척수액 검사 필요함을 설명","explanation":"검사 협조를 얻습니다"},
{"mistake":"예방접종 미안내","correction":"수막구균, 폐렴구균 백신으로 예방 가능","explanation":"예방을 강조합니다"}],
[{"ko":"뇌수막염 확인을 위해 척추 천자가 필요합니다.","vi":"Cần chọc tủy sống để xác nhận viêm màng não.","situation":"formal"},
{"ko":"고열과 두통이 심하면 바로 오세요.","vi":"Sốt cao và đau đầu dữ dội thì đến ngay.","situation":"formal"},
{"ko":"이건 바이러스라 입원 안 해도 돼요.","vi":"Đây là virus nên không cần nhập viện.","situation":"informal"}],
["요추천자","항생제","예방접종"]),

t("viem-nao","뇌염","viêm não","뇌 자체에 염증이 생기는 질환입니다. 발열, 의식 변화, 경련이 나타납니다. 바이러스가 주요 원인입니다. 통역 시 응급성, 후유증 가능성을 설명해야 합니다.",
"Viêm não gây sốt, thay đổi ý thức, co giật","신경과, 감염내과","한국에서 일본뇌염 예방접종이 국가예방접종에 포함됩니다.",
[{"mistake":"뇌수막염과 뇌염 구분 안 함","correction":"뇌수막염은 막, 뇌염은 뇌 자체 염증","explanation":"정확한 진단을 이해시킵니다"},
{"mistake":"후유증 가능성 미설명","correction":"회복 후에도 인지, 운동 장애 남을 수 있음","explanation":"현실적 기대를 갖게 합니다"},
{"mistake":"일본뇌염 백신 미안내","correction":"예방접종으로 예방 가능","explanation":"예방의 중요성을 강조합니다"}],
[{"ko":"뇌염으로 집중 치료가 필요합니다.","vi":"Viêm não cần điều trị tích cực.","situation":"formal"},
{"ko":"의식이 명료해질 때까지 지켜봐야 합니다.","vi":"Cần theo dõi cho đến khi tỉnh táo.","situation":"formal"},
{"ko":"모기 물리지 않게 조심하세요.","vi":"Cẩn thận không để muỗi đốt.","situation":"informal"}],
["일본뇌염","항바이러스제","후유증"]),

t("co-giat-dong-kinh","간질","động kinh","뇌의 비정상적 전기 활동으로 반복적 발작이 일어나는 질환입니다. 항경련제로 조절합니다. 통역 시 발작 시 대처, 약물 복용 중요성, 일상생활 주의사항을 설명해야 합니다.",
"Bệnh gây co giật tái phát do hoạt động điện bất thường trong não","신경과","한국에서 간질은 적절한 치료로 70-80%가 발작 조절이 됩니다. 편견 해소가 중요합니다.",
[{"mistake":"간질을 정신질환으로 오해","correction":"뇌의 전기적 문제로 신경과 질환","explanation":"편견을 바로잡습니다"},
{"mistake":"발작 시 입에 뭔가 넣으라고 안내","correction":"입에 아무것도 넣지 말고 옆으로 눕히기","explanation":"올바른 응급 처치를 교육합니다"},
{"mistake":"운전, 수영 제한 미설명","correction":"발작 조절될 때까지 위험 활동 제한","explanation":"안전을 보장합니다"}],
[{"ko":"간질로 항경련제가 필요합니다.","vi":"Động kinh cần thuốc chống co giật.","situation":"formal"},
{"ko":"약을 규칙적으로 드셔야 발작이 안 와요.","vi":"Uống thuốc đều đặn thì không bị co giật.","situation":"formal"},
{"ko":"발작할 때 혀 깨무는 거 아니에요, 입에 아무것도 넣지 마세요.","vi":"Lúc co giật không cắn lưỡi đâu, đừng nhét gì vào miệng.","situation":"informal"}],
["항경련제","발작","뇌파검사"]),

t("benh-multiple-sclerosis","다발성경화증","bệnh xơ cứng rải rác","중추신경계의 수초가 손상되는 자가면역 질환입니다. 시력 저하, 마비, 감각 이상이 반복됩니다. 통역 시 재발-완화 패턴, 장기 관리, 최신 치료를 설명해야 합니다.",
"Bệnh tự miễn làm tổn thương vỏ myelin của hệ thần kinh trung ương","신경과","한국에서 다발성경화증은 드물지만 젊은 여성에게 많습니다. 최근 치료제 발전으로 예후가 개선되고 있습니다.",
[{"mistake":"휠체어가 필연적이라고 설명","correction":"조기 치료로 장애 진행 늦출 수 있음","explanation":"희망을 유지시킵니다"},
{"mistake":"모든 증상이 영구적이라고 설명","correction":"급성기 후 회복되는 증상도 많음","explanation":"재발-완화 패턴을 이해시킵니다"},
{"mistake":"최신 치료제 정보 부족","correction":"질환수정약물(DMT)로 재발 감소 가능","explanation":"치료 옵션을 알립니다"}],
[{"ko":"다발성경화증으로 약물 치료가 필요합니다.","vi":"Bệnh xơ cứng rải rác cần điều trị bằng thuốc.","situation":"formal"},
{"ko":"증상이 나타나면 빨리 치료해야 후유증이 적어요.","vi":"Khi có triệu chứng điều trị nhanh thì ít di chứng.","situation":"formal"},
{"ko":"요즘 좋은 약 많아서 잘 조절돼요.","vi":"Giờ có nhiều thuốc tốt nên kiểm soát được.","situation":"informal"}],
["MRI","질환수정약물","재활"]),

t("roi-loan-tien-dinh","어지럼증","rối loạn tiền đình","균형 감각 이상으로 어지러움을 느끼는 증상입니다. 말초성(내이), 중추성(뇌)으로 구분됩니다. 원인에 따라 치료가 다릅니다. 통역 시 원인 감별, 응급 신호, 재활을 설명해야 합니다.",
"Triệu chứng chóng mặt do rối loạn cảm giác thăng bằng","이비인후과, 신경과","한국에서 어지럼증은 흔한 증상입니다. 대부분 양성이지만 뇌졸중 감별이 중요합니다.",
[{"mistake":"모든 어지럼증이 빈혈이라고 설명","correction":"전정기관, 뇌 문제 등 다양한 원인 있음","explanation":"정확한 진단을 유도합니다"},
{"mistake":"뇌졸중 위험 신호 미설명","correction":"복시, 발음 장애, 마비 동반 시 응급","explanation":"응급 상황을 인지시킵니다"},
{"mistake":"전정재활 미안내","correction":"운동 치료로 호전 가능함을 설명","explanation":"적극적 재활을 독려합니다"}],
[{"ko":"어지럼증 원인을 찾기 위해 검사가 필요합니다.","vi":"Cần xét nghiệm để tìm nguyên nhân chóng mặt.","situation":"formal"},
{"ko":"말이 어눌해지거나 힘이 빠지면 바로 응급실 가세요.","vi":"Nếu nói ngọng hoặc yếu tay chân thì đi cấp cứu ngay.","situation":"formal"},
{"ko":"이 운동하면 어지럼증 많이 좋아져요.","vi":"Tập bài này thì hết chóng mặt nhiều.","situation":"informal"}],
["이석증","전정재활","MRI"]),

t("dau-dau-migraine","편두통","đau đầu migraine","반복적으로 발생하는 심한 두통입니다. 맥박처럼 뛰는 통증, 오심, 빛/소리 민감이 특징입니다. 예방약과 급성기 약으로 관리합니다. 통역 시 유발 요인, 약물 사용법, 생활관리를 설명해야 합니다.",
"Đau đầu dữ dội tái phát, đập theo nhịp, buồn nôn, nhạy cảm ánh sáng","신경과","한국에서 편두통은 여성에게 3배 많습니다. 올바른 약물 사용이 중요합니다.",
[{"mistake":"진통제 과다 복용 위험 미설명","correction":"월 10회 이상 진통제 사용 시 약물과용두통 위험","explanation":"약물 의존을 예방합니다"},
{"mistake":"예방 치료 미안내","correction":"잦은 편두통은 예방약으로 빈도 감소 가능","explanation":"삶의 질을 개선합니다"},
{"mistake":"유발 요인 교육 부족","correction":"스트레스, 수면 부족, 특정 음식 등 유발 요인 파악 권고","explanation":"자가관리를 돕습니다"}],
[{"ko":"편두통으로 예방약이 도움이 됩니다.","vi":"Đau đầu migraine cần thuốc phòng ngừa.","situation":"formal"},
{"ko":"진통제를 너무 자주 드시면 오히려 두통이 심해져요.","vi":"Uống thuốc giảm đau quá thường xuyên thì đau đầu nặng hơn.","situation":"formal"},
{"ko":"잠 부족하면 편두통 잘 와요.","vi":"Thiếu ngủ thì dễ bị migraine.","situation":"informal"}],
["진통제","예방약","트립탄"]),

t("roi-loan-giac-ngu","수면장애","rối loạn giấc ngủ","잠들기 어렵거나 수면 유지가 안 되는 상태입니다. 불면증, 수면무호흡, 하지불안증후군 등이 있습니다. 원인에 따라 치료합니다. 통역 시 수면위생, 수면제 주의사항, 수면검사를 설명해야 합니다.",
"Tình trạng khó ngủ hoặc không duy trì được giấc ngủ","정신건강의학과, 신경과","한국에서 수면장애는 매우 흔합니다. 수면제 의존보다 원인 치료가 중요합니다.",
[{"mistake":"수면제만 처방하면 된다고 설명","correction":"수면위생, 인지행동치료 등 비약물 치료 우선","explanation":"약물 의존을 예방합니다"},
{"mistake":"코골이를 대수롭지 않게 여김","correction":"수면무호흡 가능성 있어 검사 권고","explanation":"심혈관 합병증을 예방합니다"},
{"mistake":"카페인 영향 미설명","correction":"오후 카페인이 수면에 영향, 제한 권고","explanation":"수면위생을 교육합니다"}],
[{"ko":"수면장애 원인을 찾기 위해 검사가 필요합니다.","vi":"Cần xét nghiệm để tìm nguyên nhân rối loạn giấc ngủ.","situation":"formal"},
{"ko":"수면제는 단기간만 사용하세요.","vi":"Thuốc ngủ chỉ dùng ngắn hạn.","situation":"formal"},
{"ko":"커피 오후에 드시면 잠 안 와요.","vi":"Uống cà phê buổi chiều thì không ngủ được.","situation":"informal"}],
["수면다원검사","수면위생","수면무호흡"]),

t("ngung-tho-khi-ngu","수면무호흡증","ngưng thở khi ngủ","수면 중 호흡이 반복적으로 멈추는 질환입니다. 코골이, 주간 졸림이 특징입니다. 고혈압, 심장병 위험을 높입니다. 통역 시 검사, CPAP 치료, 체중 감량을 설명해야 합니다.",
"Bệnh ngưng thở nhiều lần khi ngủ gây ngáy và buồn ngủ ban ngày","이비인후과, 호흡기내과","한국에서 수면무호흡증은 비만 증가로 늘고 있습니다. 심혈관 합병증 예방이 중요합니다.",
[{"mistake":"코골이를 정상으로 여김","correction":"심한 코골이는 무호흡 동반 가능, 검사 권고","explanation":"위험성을 인지시킵니다"},
{"mistake":"CPAP 치료 거부감만 강조","correction":"적응 후 삶의 질 크게 개선됨을 설명","explanation":"치료 순응도를 높입니다"},
{"mistake":"체중 감량 중요성 미강조","correction":"비만이 주요 원인, 감량으로 호전 가능","explanation":"근본 치료를 권합니다"}],
[{"ko":"수면무호흡증 확인을 위해 수면검사가 필요합니다.","vi":"Cần xét nghiệm giấc ngủ để xác nhận ngưng thở khi ngủ.","situation":"formal"},
{"ko":"CPAP 기계를 쓰시면 피곤한 게 없어져요.","vi":"Dùng máy CPAP thì hết mệt.","situation":"formal"},
{"ko":"살 빠지면 코골이도 줄어요.","vi":"Giảm cân thì cũng bớt ngáy.","situation":"informal"}],
["수면다원검사","CPAP","비만"]),

t("roi-loan-hoang-loat","공황장애","rối loạn hoảng loạn","갑작스러운 심한 불안 발작이 반복되는 질환입니다. 심장 두근거림, 호흡곤란, 죽을 것 같은 공포가 특징입니다. 약물과 인지행동치료로 치료합니다. 통역 시 발작이 위험하지 않음, 치료 효과를 설명해야 합니다.",
"Bệnh với những cơn hoảng loạn đột ngột lặp đi lặp lại","정신건강의학과","한국에서 공황장애 환자가 증가하고 있습니다. 치료 효과가 좋으므로 적극 치료를 권합니다.",
[{"mistake":"공황발작을 심장마비로 오해","correction":"심장은 정상, 뇌의 불안 반응임을 설명","explanation":"불안을 줄입니다"},
{"mistake":"약물 의존성만 강조","correction":"적절한 치료로 완치 가능","explanation":"치료 순응도를 높입니다"},
{"mistake":"회피행동 조장","correction":"회피는 증상 악화, 인지행동치료로 극복","explanation":"적극적 치료를 독려합니다"}],
[{"ko":"공황장애로 약물과 상담 치료를 권합니다.","vi":"Rối loạn hoảng loạn cần thuốc và tư vấn.","situation":"formal"},
{"ko":"발작이 와도 죽지 않아요, 걱정 마세요.","vi":"Dù có cơn hoảng loạn cũng không chết, đừng lo.","situation":"formal"},
{"ko":"이 병은 치료하면 다 낫는 병이에요.","vi":"Bệnh này điều trị thì khỏi được.","situation":"informal"}],
["항불안제","인지행동치료","발작"]),

t("tam-than-phan-liet","조현병","tâm thần phân liệt","사고, 감정, 행동에 이상이 나타나는 정신질환입니다. 환청, 망상, 사회적 위축이 특징입니다. 항정신병약물로 치료합니다. 통역 시 편견 해소, 약물 복용 중요성, 가족 지지를 설명해야 합니다.",
"Bệnh tâm thần với rối loạn suy nghĩ, cảm xúc và hành vi","정신건강의학과","한국에서 조현병에 대한 편견이 줄어들고 있습니다. 조기 치료와 재활로 사회생활이 가능합니다.",
[{"mistake":"위험한 사람으로 낙인","correction":"대부분 폭력적이지 않음, 치료로 안정","explanation":"편견을 해소합니다"},
{"mistake":"평생 입원해야 한다고 설명","correction":"약물 복용하면 지역사회 생활 가능","explanation":"희망을 줍니다"},
{"mistake":"약물 부작용만 강조","correction":"부작용 조절 가능, 복용 중단 시 재발 위험","explanation":"약물 복용을 지지합니다"}],
[{"ko":"조현병으로 약물 치료가 필요합니다.","vi":"Tâm thần phân liệt cần điều trị bằng thuốc.","situation":"formal"},
{"ko":"약을 꾸준히 드시면 일상생활이 가능합니다.","vi":"Uống thuốc đều đặn thì có thể sống bình thường.","situation":"formal"},
{"ko":"약 먹으면 환청 안 들려요.","vi":"Uống thuốc thì không nghe tiếng ảo giác.","situation":"informal"}],
["항정신병약물","재활","가족지지"]),

t("roi-loan-luong-cuc","양극성장애","rối loạn lưỡng cực","조증과 우울증이 번갈아 나타나는 정신질환입니다. 기분안정제로 치료합니다. 통역 시 조증 증상, 장기 관리, 약물 복용 중요성을 설명해야 합니다.",
"Bệnh tâm thần với các giai đoạn hưng cảm và trầm cảm xen kẽ","정신건강의학과","한국에서 양극성장애는 조기 진단이 어려워 치료가 늦어지는 경우가 많습니다.",
[{"mistake":"단순 우울증으로 오진","correction":"조증 병력 확인이 진단에 중요","explanation":"정확한 진단을 유도합니다"},
{"mistake":"기분 좋을 때 약 중단해도 된다고 설명","correction":"조증 예방 위해 안정기에도 복용 필요","explanation":"재발을 예방합니다"},
{"mistake":"조증을 긍정적으로만 봄","correction":"조증 시 판단력 저하로 위험한 결정 가능","explanation":"위험성을 인지시킵니다"}],
[{"ko":"양극성장애로 기분안정제가 필요합니다.","vi":"Rối loạn lưỡng cực cần thuốc ổn định khí sắc.","situation":"formal"},
{"ko":"기분 좋을 때도 약을 드셔야 해요.","vi":"Dù khí sắc tốt cũng phải uống thuốc.","situation":"formal"},
{"ko":"기분이 너무 좋을 때가 오히려 위험해요.","vi":"Lúc quá vui mới là nguy hiểm.","situation":"informal"}],
["기분안정제","조증","우울증"]),

t("roi-loan-an-uong","섭식장애","rối loạn ăn uống","음식 섭취에 대한 비정상적 태도와 행동을 보이는 질환입니다. 신경성 식욕부진, 폭식증 등이 있습니다. 영양, 심리, 약물 치료가 필요합니다. 통역 시 신체 합병증, 심리 치료 필요성을 설명해야 합니다.",
"Bệnh với thái độ và hành vi bất thường về ăn uống","정신건강의학과, 내과","한국에서 섭식장애는 젊은 여성에게 많습니다. 신체와 정신 모두 치료가 필요합니다.",
[{"mistake":"의지로 고칠 수 있다고 설명","correction":"정신질환으로 전문 치료 필요","explanation":"적절한 치료를 유도합니다"},
{"mistake":"신체 합병증 미설명","correction":"전해질 이상, 골다공증 등 신체 위험","explanation":"신체 검사의 중요성을 강조합니다"},
{"mistake":"체중만 회복하면 된다고 설명","correction":"심리 치료 병행이 재발 방지에 필수","explanation":"종합 치료를 권합니다"}],
[{"ko":"섭식장애로 영양과 심리 치료가 필요합니다.","vi":"Rối loạn ăn uống cần điều trị dinh dưỡng và tâm lý.","situation":"formal"},
{"ko":"체중만 늘리는 게 아니라 마음도 치료해야 해요.","vi":"Không chỉ tăng cân mà còn phải điều trị tâm lý.","situation":"formal"},
{"ko":"이건 의지 문제가 아니라 병이에요.","vi":"Đây không phải vấn đề ý chí mà là bệnh.","situation":"informal"}],
["신경성식욕부진","폭식증","심리치료"]),
]

added = [n for n in new if n['slug'] not in existing]
data.extend(added)
print(f"B배치 추가: {len(added)}개, 총: {len(data)}개")
with open(path, 'w', encoding='utf-8') as f: json.dump(data, f, ensure_ascii=False, indent=2)
