#!/usr/bin/env python3
"""
Medical 도메인 용어 확장 스크립트
현재 192개 → 1,000개로 확장
"""

import json
import os

# 현재 medical.json 로드
medical_path = os.path.join(os.path.dirname(__file__), '../data/terms/medical.json')
with open(medical_path, 'r', encoding='utf-8') as f:
    existing_terms = json.load(f)

existing_slugs = {t['slug'] for t in existing_terms}
print(f"기존 용어 수: {len(existing_terms)}")

# Tier S 품질 템플릿 함수
def create_term(slug, korean, vietnamese, hanja, hanjaReading, pronunciation,
                meaningKo, meaningVi, context, culturalNote,
                commonMistakes, examples, relatedTerms):
    return {
        "slug": slug,
        "korean": korean,
        "vietnamese": vietnamese,
        "hanja": hanja,
        "hanjaReading": hanjaReading,
        "pronunciation": pronunciation,
        "meaningKo": meaningKo,
        "meaningVi": meaningVi,
        "context": context,
        "culturalNote": culturalNote,
        "commonMistakes": commonMistakes,
        "examples": examples,
        "relatedTerms": relatedTerms
    }

# 새로운 의료 용어 데이터
new_terms = []

# ============ 1. 진단/검사 용어 (100개) ============

diagnostic_terms = [
    create_term(
        "sinh-thiet", "생검", "sinh thiết", "生檢", "생(살 생) + 검(검사할 검)", "saeng-geom",
        "살아있는 조직의 일부를 채취하여 현미경으로 검사하는 진단 방법입니다. 암 진단에 필수적인 검사로, 종양이 악성인지 양성인지 판별합니다. 통역 시 환자에게 검사의 필요성과 절차를 명확히 설명해야 하며, 마취 여부, 검사 후 주의사항 등을 정확히 전달해야 합니다.",
        "Phương pháp chẩn đoán bằng cách lấy một phần mô sống để kiểm tra dưới kính hiển vi",
        "종양학, 병리학",
        "한국에서 생검은 암 의심 시 거의 필수적으로 시행됩니다. 베트남 환자들은 조직을 떼어낸다는 표현에 두려움을 느낄 수 있으므로 검사의 안전성을 충분히 설명해야 합니다.",
        [
            {"mistake": "생검을 'phẫu thuật'로 번역", "correction": "'sinh thiết' 또는 'lấy mẫu mô'", "explanation": "생검은 수술이 아닌 검사 목적의 조직 채취입니다"},
            {"mistake": "조직검사와 생검 혼용", "correction": "생검(sinh thiết)은 채취, 조직검사(xét nghiệm mô)는 분석", "explanation": "두 용어는 연결되어 있지만 구분해서 사용합니다"},
            {"mistake": "결과 설명 시 전문용어만 사용", "correction": "악성(ác tính), 양성(lành tính)을 쉬운 말로 추가 설명", "explanation": "환자가 이해할 수 있도록 풀어서 설명해야 합니다"}
        ],
        [
            {"ko": "정확한 진단을 위해 생검이 필요합니다.", "vi": "Cần sinh thiết để chẩn đoán chính xác.", "situation": "formal"},
            {"ko": "생검 결과는 일주일 후에 나옵니다.", "vi": "Kết quả sinh thiết sẽ có sau một tuần.", "situation": "formal"},
            {"ko": "작은 조직만 떼어내는 거라 많이 아프지 않아요.", "vi": "Chỉ lấy một mẫu mô nhỏ thôi nên không đau lắm.", "situation": "informal"}
        ],
        ["조직검사", "병리검사", "세포진검사"]
    ),
    create_term(
        "xet-nghiem-mau-tong-quat", "종합혈액검사", "xét nghiệm máu tổng quát", "綜合血液檢査", "종(모을 종) + 합(합할 합) + 혈(피 혈) + 액(진액 액) + 검(검사할 검) + 사(살필 사)", "jong-hap-hyeo-raek-geom-sa",
        "혈액의 여러 성분을 종합적으로 분석하는 기본 검사입니다. 적혈구, 백혈구, 혈소판 수치와 간기능, 신장기능, 혈당, 콜레스테롤 등을 확인합니다. 통역 시 각 수치의 의미와 정상 범위를 설명하고, 이상 소견이 있을 때 추가 검사나 치료 방향을 정확히 전달해야 합니다.",
        "Xét nghiệm phân tích tổng hợp các thành phần trong máu bao gồm tế bào máu, chức năng gan thận, đường huyết",
        "내과, 건강검진",
        "한국의 건강검진에서 종합혈액검사는 기본 항목입니다. 공복 상태에서 채혈해야 정확한 결과를 얻을 수 있으며, 검사 전날 저녁 9시 이후 금식이 필요합니다.",
        [
            {"mistake": "CBC와 종합혈액검사를 동일시", "correction": "CBC는 혈구검사만, 종합혈액검사는 생화학검사 포함", "explanation": "종합혈액검사는 더 광범위한 항목을 포함합니다"},
            {"mistake": "금식 안내 누락", "correction": "검사 8-12시간 전 금식 필요함을 안내", "explanation": "공복 혈당, 지질 수치 등이 영향을 받습니다"},
            {"mistake": "수치만 전달하고 의미 설명 안 함", "correction": "정상 범위와 이상 시 의미를 함께 설명", "explanation": "환자가 자신의 건강 상태를 이해할 수 있어야 합니다"}
        ],
        [
            {"ko": "종합혈액검사를 위해 채혈하겠습니다.", "vi": "Tôi sẽ lấy máu để xét nghiệm máu tổng quát.", "situation": "formal"},
            {"ko": "간 수치가 약간 높게 나왔습니다.", "vi": "Chỉ số gan hơi cao một chút.", "situation": "formal"},
            {"ko": "피검사 결과 다 정상이에요.", "vi": "Kết quả xét nghiệm máu đều bình thường.", "situation": "informal"}
        ],
        ["CBC", "간기능검사", "신장기능검사"]
    ),
    create_term(
        "xet-nghiem-nuoc-tieu-tong-hop", "소변검사", "xét nghiệm nước tiểu", "小便檢査", "소(작을 소) + 변(변 변) + 검(검사할 검) + 사(살필 사)", "so-byeon-geom-sa",
        "소변을 분석하여 신장, 요로계 질환 및 당뇨, 감염 등을 진단하는 검사입니다. 요단백, 요당, 잠혈, 세균 등을 확인합니다. 통역 시 중간뇨(midstream urine) 채취 방법을 정확히 설명해야 하며, 생리 중인 여성은 검사가 부정확할 수 있음을 안내해야 합니다.",
        "Xét nghiệm phân tích nước tiểu để chẩn đoán bệnh thận, đường tiết niệu, tiểu đường và nhiễm trùng",
        "내과, 비뇨기과, 건강검진",
        "한국에서 소변검사는 건강검진의 기본 항목입니다. 깨끗한 검체를 얻기 위해 중간뇨를 받아야 하며, 이 방법을 베트남 환자에게 명확히 설명해야 합니다.",
        [
            {"mistake": "중간뇨 채취 방법 설명 생략", "correction": "처음 소변 버리고 중간 부분을 받으라고 안내", "explanation": "초반 소변에는 오염물질이 있어 결과가 부정확해질 수 있습니다"},
            {"mistake": "여성 환자의 생리 여부 확인 안 함", "correction": "생리 중이면 검사 연기 권고", "explanation": "혈액이 섞이면 잠혈 양성으로 나올 수 있습니다"},
            {"mistake": "결과 용어를 그대로 전달", "correction": "양성/음성의 의미를 쉽게 설명", "explanation": "요단백 양성이 무엇을 의미하는지 환자가 이해해야 합니다"}
        ],
        [
            {"ko": "소변검사를 위해 이 컵에 소변을 받아 주세요.", "vi": "Xin vui lòng lấy nước tiểu vào cốc này để xét nghiệm.", "situation": "formal"},
            {"ko": "중간 소변을 받아 주셔야 합니다.", "vi": "Bạn cần lấy phần nước tiểu giữa dòng.", "situation": "formal"},
            {"ko": "소변에 피가 좀 섞여 나왔어요.", "vi": "Có một chút máu trong nước tiểu.", "situation": "informal"}
        ],
        ["요검사", "신장검사", "방광염"]
    ),
    create_term(
        "dien-nao-do", "뇌파검사", "điện não đồ", "腦波檢査", "뇌(골 뇌) + 파(물결 파) + 검(검사할 검) + 사(살필 사)", "noe-pa-geom-sa",
        "두피에 전극을 붙여 뇌의 전기적 활동을 기록하는 검사입니다. 간질(뇌전증), 수면장애, 의식장애 등을 진단합니다. 검사 시간은 30분-1시간이며, 검사 전날 머리를 깨끗이 감고 오일이나 스프레이 사용을 피해야 합니다. 통역 시 검사 중 눈을 감거나 과호흡을 하는 지시사항을 정확히 전달해야 합니다.",
        "Phương pháp ghi lại hoạt động điện của não bằng cách gắn điện cực lên da đầu",
        "신경과, 수면의학",
        "한국에서 뇌파검사는 간질 진단의 기본 검사입니다. 검사가 아프지 않고 방사선이 없어 안전하다는 점을 환자에게 설명하면 불안감을 줄일 수 있습니다.",
        [
            {"mistake": "EEG를 설명 없이 사용", "correction": "'điện não đồ' 또는 '검사 뇌 bằng điện cực'로 설명", "explanation": "의학 약어는 풀어서 설명해야 환자가 이해합니다"},
            {"mistake": "검사 준비사항 누락", "correction": "머리 감기, 카페인 제한, 충분한 수면 등 안내", "explanation": "준비 상태가 검사 결과에 영향을 미칩니다"},
            {"mistake": "검사 중 지시사항 미전달", "correction": "눈 감기, 과호흡, 광자극 등의 지시를 미리 설명", "explanation": "환자가 검사 중 당황하지 않도록 미리 안내합니다"}
        ],
        [
            {"ko": "간질 진단을 위해 뇌파검사를 하겠습니다.", "vi": "Chúng tôi sẽ làm điện não đồ để chẩn đoán động kinh.", "situation": "formal"},
            {"ko": "검사 중에 눈을 감으라는 지시가 있을 거예요.", "vi": "Trong khi kiểm tra sẽ có hướng dẫn nhắm mắt.", "situation": "formal"},
            {"ko": "뇌파검사는 안 아파요, 걱정 마세요.", "vi": "Điện não đồ không đau, đừng lo.", "situation": "informal"}
        ],
        ["간질", "수면다원검사", "MRI"]
    ),
    create_term(
        "sieu-am-tim", "심장초음파", "siêu âm tim", "心臟超音波", "심(마음 심) + 장(창자 장) + 초(넘을 초) + 음(소리 음) + 파(물결 파)", "sim-jang-cho-eum-pa",
        "초음파를 이용하여 심장의 구조와 기능을 실시간으로 관찰하는 검사입니다. 심장 판막 이상, 심근 기능, 심방/심실 크기 등을 확인합니다. 비침습적이고 방사선이 없어 안전하며, 검사 시간은 20-30분입니다. 통역 시 옆으로 눕는 자세, 숨 참기 등의 지시사항을 전달해야 합니다.",
        "Phương pháp quan sát cấu trúc và chức năng tim bằng siêu âm",
        "심장내과, 건강검진",
        "한국에서 심장초음파는 심장 질환 진단의 기본 검사입니다. 금식이 필요 없고 통증이 없어 부담이 적은 검사임을 환자에게 설명합니다.",
        [
            {"mistake": "심초음파를 '심전도'와 혼동", "correction": "심초음파는 초음파로 구조를 보고, 심전도는 전기 신호를 봄", "explanation": "두 검사는 목적과 방법이 다릅니다"},
            {"mistake": "검사 자세 설명 누락", "correction": "왼쪽으로 눕고 왼팔을 머리 위로 올리라고 안내", "explanation": "올바른 자세가 검사 결과에 영향을 미칩니다"},
            {"mistake": "젤 도포 안내 없음", "correction": "차가운 젤을 가슴에 바른다고 미리 안내", "explanation": "환자가 당황하지 않도록 미리 알려줍니다"}
        ],
        [
            {"ko": "심장초음파로 판막 상태를 확인하겠습니다.", "vi": "Chúng tôi sẽ kiểm tra van tim bằng siêu âm tim.", "situation": "formal"},
            {"ko": "왼쪽으로 누워 주세요.", "vi": "Xin vui lòng nằm nghiêng bên trái.", "situation": "formal"},
            {"ko": "심장 기능이 좋아요, 걱정 마세요.", "vi": "Chức năng tim tốt, đừng lo.", "situation": "informal"}
        ],
        ["심전도", "관상동맥조영술", "심부전"]
    ),
    create_term(
        "do-mat-do-xuong", "골밀도검사", "đo mật độ xương", "骨密度檢査", "골(뼈 골) + 밀(빽빽할 밀) + 도(정도 도) + 검(검사할 검) + 사(살필 사)", "gol-mil-do-geom-sa",
        "X선을 이용하여 뼈의 밀도를 측정하는 검사입니다. 골다공증 진단과 골절 위험도 평가에 사용됩니다. 주로 허리뼈와 고관절을 측정하며 검사 시간은 10-15분입니다. 통역 시 T-score의 의미(-1 이상 정상, -2.5 이하 골다공증)를 환자가 이해할 수 있게 설명해야 합니다.",
        "Phương pháp đo mật độ xương bằng tia X để chẩn đoán loãng xương",
        "정형외과, 내분비내과, 건강검진",
        "한국에서 65세 이상 여성은 건강보험으로 골밀도검사를 받을 수 있습니다. 폐경 후 여성에게 중요한 검사이며, 베트남에서는 아직 검사가 보편화되지 않아 검사의 필요성을 설명해야 합니다.",
        [
            {"mistake": "T-score를 설명 없이 전달", "correction": "수치의 의미(정상, 골감소, 골다공증)를 설명", "explanation": "-2.5 이하면 골다공증, -1~-2.5는 골감소증입니다"},
            {"mistake": "DEXA와 골밀도검사 구분 안 함", "correction": "DEXA는 검사 방법, 골밀도검사는 목적", "explanation": "DEXA(이중에너지 X선)로 골밀도를 측정합니다"},
            {"mistake": "칼슘제 복용 시점 안내 누락", "correction": "검사 결과에 따른 칼슘/비타민D 섭취 방법 설명", "explanation": "치료와 예방 방법까지 함께 안내합니다"}
        ],
        [
            {"ko": "골다공증 여부를 확인하기 위해 골밀도검사를 하겠습니다.", "vi": "Chúng tôi sẽ đo mật độ xương để kiểm tra loãng xương.", "situation": "formal"},
            {"ko": "T-score가 -2.7이면 골다공증입니다.", "vi": "T-score -2.7 có nghĩa là loãng xương.", "situation": "formal"},
            {"ko": "뼈가 좀 약해졌어요, 칼슘제 드세요.", "vi": "Xương hơi yếu, nên uống canxi.", "situation": "informal"}
        ],
        ["골다공증", "칼슘", "골절"]
    ),
    create_term(
        "noi-soi-phe-quan", "기관지내시경", "nội soi phế quản", "氣管支內視鏡", "기(기운 기) + 관(대롱 관) + 지(가지 지) + 내(안 내) + 시(볼 시) + 경(거울 경)", "gi-gwan-ji-nae-si-gyeong",
        "가느다란 내시경을 코나 입을 통해 기관지까지 삽입하여 폐와 기관지를 관찰하는 검사입니다. 폐암 진단, 이물질 제거, 조직 검사 등에 사용됩니다. 검사 전 금식이 필요하고, 국소마취 후 시행합니다. 통역 시 기침 반사가 있을 수 있음을 미리 안내해야 합니다.",
        "Phương pháp quan sát phổi và phế quản bằng cách đưa ống nội soi qua mũi hoặc miệng",
        "호흡기내과, 흉부외과",
        "한국에서 기관지내시경은 폐 질환 진단에 중요한 검사입니다. 검사 중 불편감이 있을 수 있어 환자의 협조가 필요하며, 검사 후 2시간 정도 금식해야 합니다.",
        [
            {"mistake": "기관지내시경을 위내시경과 혼동", "correction": "기관지내시경은 폐를, 위내시경은 위를 검사", "explanation": "검사 부위와 목적이 다릅니다"},
            {"mistake": "검사 중 불편감 설명 누락", "correction": "기침, 이물감이 있을 수 있다고 미리 안내", "explanation": "환자가 심리적으로 준비할 수 있게 합니다"},
            {"mistake": "검사 후 주의사항 미전달", "correction": "2시간 금식, 목소리 변화 가능성 안내", "explanation": "마취 효과가 남아 있어 사레 들릴 위험이 있습니다"}
        ],
        [
            {"ko": "폐 상태를 확인하기 위해 기관지내시경을 하겠습니다.", "vi": "Chúng tôi sẽ nội soi phế quản để kiểm tra tình trạng phổi.", "situation": "formal"},
            {"ko": "검사 중 기침이 나올 수 있어요.", "vi": "Có thể ho trong khi kiểm tra.", "situation": "formal"},
            {"ko": "검사 끝나고 2시간은 아무것도 드시면 안 돼요.", "vi": "Sau khi kiểm tra xong không được ăn gì trong 2 tiếng.", "situation": "informal"}
        ],
        ["폐암", "흉부CT", "객담검사"]
    ),
    create_term(
        "do-chuc-nang-ho-hap", "폐기능검사", "đo chức năng hô hấp", "肺機能檢査", "폐(허파 폐) + 기(틀 기) + 능(능할 능) + 검(검사할 검) + 사(살필 사)", "pye-gi-neung-geom-sa",
        "폐활량과 호흡 기능을 측정하는 검사입니다. 천식, COPD, 간질성 폐질환 등을 진단하고 치료 효과를 평가합니다. 마우스피스를 물고 최대한 숨을 들이쉬고 내쉬는 동작을 반복합니다. 통역 시 검사 방법과 환자의 적극적인 협조가 필요함을 강조해야 합니다.",
        "Phương pháp đo dung tích phổi và chức năng hô hấp",
        "호흡기내과, 직업환경의학",
        "한국에서 폐기능검사는 호흡기 질환 진단과 산업재해 판정에 사용됩니다. 환자의 협조 정도에 따라 결과가 달라지므로 검사 방법을 충분히 설명해야 합니다.",
        [
            {"mistake": "검사 방법 설명 부족", "correction": "최대한 깊이 숨 쉬고 힘껏 내쉬라고 구체적으로 안내", "explanation": "환자가 방법을 모르면 정확한 결과를 얻을 수 없습니다"},
            {"mistake": "FEV1, FVC 등 용어를 그대로 전달", "correction": "1초간 내쉴 수 있는 양, 총 폐활량 등으로 풀어 설명", "explanation": "전문 용어는 이해하기 쉽게 풀어서 설명합니다"},
            {"mistake": "기관지확장제 반응검사 설명 누락", "correction": "약물 흡입 전후 검사를 비교할 수 있음을 안내", "explanation": "천식 진단에 중요한 검사입니다"}
        ],
        [
            {"ko": "천식 여부를 확인하기 위해 폐기능검사를 하겠습니다.", "vi": "Chúng tôi sẽ đo chức năng hô hấp để kiểm tra hen suyễn.", "situation": "formal"},
            {"ko": "숨을 최대한 깊이 들이쉬고 힘껏 내쉬세요.", "vi": "Hít thật sâu rồi thở ra mạnh hết sức.", "situation": "formal"},
            {"ko": "폐활량이 좀 떨어졌네요.", "vi": "Dung tích phổi giảm một chút.", "situation": "informal"}
        ],
        ["천식", "COPD", "기관지확장제"]
    ),
    create_term(
        "do-dien-co", "근전도검사", "đo điện cơ", "筋電圖檢査", "근(힘줄 근) + 전(번개 전) + 도(그림 도) + 검(검사할 검) + 사(살필 사)", "geun-jeon-do-geom-sa",
        "근육과 신경의 전기적 활동을 측정하는 검사입니다. 말초신경병증, 근육병증, 신경근 접합부 질환 등을 진단합니다. 바늘 전극을 근육에 삽입하여 검사하므로 약간의 통증이 있습니다. 통역 시 검사의 목적과 통증 정도를 솔직하게 설명해야 합니다.",
        "Phương pháp đo hoạt động điện của cơ và thần kinh",
        "신경과, 재활의학과",
        "한국에서 근전도검사는 손목터널증후군, 디스크 등의 진단에 흔히 사용됩니다. 바늘 검사에 대한 두려움이 있을 수 있어 검사의 필요성을 충분히 설명해야 합니다.",
        [
            {"mistake": "EMG를 설명 없이 사용", "correction": "'đo điện cơ' 또는 'xét nghiệm cơ và thần kinh'로 설명", "explanation": "의학 약어는 풀어서 설명해야 합니다"},
            {"mistake": "통증에 대해 언급 안 함", "correction": "바늘 삽입 시 따끔할 수 있다고 솔직히 안내", "explanation": "예상치 못한 통증은 환자의 불안을 키웁니다"},
            {"mistake": "신경전도검사와 근전도검사 구분 안 함", "correction": "신경전도검사(NCS)는 신경을, 근전도(EMG)는 근육을 검사", "explanation": "두 검사는 함께 시행되지만 목적이 다릅니다"}
        ],
        [
            {"ko": "손 저림 원인을 찾기 위해 근전도검사를 하겠습니다.", "vi": "Chúng tôi sẽ đo điện cơ để tìm nguyên nhân tê tay.", "situation": "formal"},
            {"ko": "바늘을 찌를 때 조금 따끔할 수 있어요.", "vi": "Khi châm kim có thể hơi đau một chút.", "situation": "formal"},
            {"ko": "신경이 눌린 부분이 있네요.", "vi": "Có vị trí thần kinh bị chèn ép.", "situation": "informal"}
        ],
        ["신경전도검사", "손목터널증후군", "디스크"]
    ),
    create_term(
        "chup-dong-mach-vanh", "관상동맥조영술", "chụp động mạch vành", "冠狀動脈造影術", "관(관 관) + 상(모양 상) + 동(움직일 동) + 맥(맥 맥) + 조(지을 조) + 영(그림자 영) + 술(기술 술)", "gwan-sang-dong-maek-jo-yeong-sul",
        "심장에 혈액을 공급하는 관상동맥에 조영제를 주입하여 혈관 상태를 확인하는 검사입니다. 협심증, 심근경색 진단과 스텐트 시술을 위해 시행합니다. 대퇴동맥이나 손목동맥을 통해 카테터를 삽입합니다. 통역 시 조영제 알레르기 여부 확인과 검사 후 안정 시간 안내가 중요합니다.",
        "Phương pháp chụp động mạch vành bằng cách tiêm thuốc cản quang để kiểm tra tình trạng mạch máu tim",
        "심장내과, 영상의학과",
        "한국에서 관상동맥조영술은 심장 질환 진단의 표준 검사입니다. 침습적 검사이므로 입원이 필요하고, 검사 후 출혈 예방을 위해 안정이 필요합니다.",
        [
            {"mistake": "관상동맥조영술과 심장초음파 혼동", "correction": "조영술은 카테터 삽입, 초음파는 비침습적 검사", "explanation": "검사 방법과 침습도가 다릅니다"},
            {"mistake": "조영제 알레르기 확인 누락", "correction": "조영제, 요오드, 해산물 알레르기 여부 반드시 확인", "explanation": "알레르기 반응이 생명을 위협할 수 있습니다"},
            {"mistake": "검사 후 주의사항 미전달", "correction": "삽입 부위 압박, 안정 시간, 수분 섭취 안내", "explanation": "출혈과 조영제 배출을 위한 주의가 필요합니다"}
        ],
        [
            {"ko": "협심증 진단을 위해 관상동맥조영술을 하겠습니다.", "vi": "Chúng tôi sẽ chụp động mạch vành để chẩn đoán đau thắt ngực.", "situation": "formal"},
            {"ko": "조영제 알레르기가 있으신가요?", "vi": "Bạn có dị ứng thuốc cản quang không?", "situation": "formal"},
            {"ko": "혈관이 70% 막혀 있어서 스텐트가 필요해요.", "vi": "Mạch máu bị tắc 70% nên cần đặt stent.", "situation": "informal"}
        ],
        ["스텐트", "협심증", "심근경색"]
    )
]

new_terms.extend(diagnostic_terms)

# 추가 진단검사 용어 (계속)
more_diagnostic = [
    create_term(
        "chup-mach-nao", "뇌혈관조영술", "chụp mạch não", "腦血管造影術", "뇌(골 뇌) + 혈(피 혈) + 관(대롱 관) + 조(지을 조) + 영(그림자 영) + 술(기술 술)", "noe-hyeol-gwan-jo-yeong-sul",
        "뇌혈관에 조영제를 주입하여 혈관 상태를 확인하는 검사입니다. 뇌동맥류, 뇌혈관 기형, 뇌졸중 원인 파악에 사용됩니다. 대퇴동맥을 통해 카테터를 뇌혈관까지 진입시킵니다. 통역 시 검사의 필요성과 합병증 가능성을 설명하고 동의서 내용을 정확히 전달해야 합니다.",
        "Phương pháp chụp mạch máu não bằng cách tiêm thuốc cản quang để kiểm tra tình trạng mạch máu",
        "신경과, 신경외과",
        "한국에서 뇌혈관조영술은 뇌혈관 질환 진단의 표준 검사입니다. 침습적 검사로 입원이 필요하며, 드물지만 뇌졸중 등의 합병증이 발생할 수 있어 동의서 설명이 중요합니다.",
        [
            {"mistake": "MRA와 혈관조영술 혼동", "correction": "MRA는 자기공명, 혈관조영술은 카테터 삽입 검사", "explanation": "MRA는 비침습적, 혈관조영술은 침습적입니다"},
            {"mistake": "합병증 설명 생략", "correction": "뇌졸중, 출혈 등 드문 합병증 가능성 안내", "explanation": "동의서 내용을 환자가 이해해야 합니다"},
            {"mistake": "검사 후 주의사항 누락", "correction": "6시간 이상 누워있기, 다리 움직이지 않기 안내", "explanation": "출혈 예방을 위한 안정이 필요합니다"}
        ],
        [
            {"ko": "뇌동맥류 확인을 위해 뇌혈관조영술이 필요합니다.", "vi": "Cần chụp mạch não để kiểm tra phình động mạch não.", "situation": "formal"},
            {"ko": "검사 후 6시간 동안 누워 계셔야 합니다.", "vi": "Sau kiểm tra phải nằm yên 6 tiếng.", "situation": "formal"},
            {"ko": "뇌혈관에 문제가 있어서 자세히 봐야 해요.", "vi": "Mạch máu não có vấn đề nên cần kiểm tra kỹ.", "situation": "informal"}
        ],
        ["뇌동맥류", "뇌졸중", "MRA"]
    ),
    create_term(
        "holter-24h", "홀터검사", "Holter 24h", None, None, "hol-teo-geom-sa",
        "24시간 동안 심전도를 연속으로 기록하는 검사입니다. 부정맥, 협심증 등 일상생활 중 발생하는 심장 이상을 포착합니다. 작은 기계를 몸에 부착하고 일상생활을 하면서 검사합니다. 통역 시 기계 부착 방법, 샤워 제한, 증상 일지 작성 방법을 안내해야 합니다.",
        "Phương pháp ghi điện tâm đồ liên tục trong 24 giờ để phát hiện rối loạn nhịp tim",
        "심장내과",
        "한국에서 홀터검사는 부정맥 진단의 표준 검사입니다. 일상생활을 하면서 검사하므로 환자의 협조가 중요하며, 증상이 있을 때 버튼을 누르고 일지를 작성해야 합니다.",
        [
            {"mistake": "Holter를 설명 없이 사용", "correction": "'theo dõi điện tim 24 giờ' 또는 '홀터 모니터링'으로 설명", "explanation": "환자가 검사 내용을 이해할 수 있어야 합니다"},
            {"mistake": "일상생활 주의사항 누락", "correction": "샤워, 운동, 수면 시 주의사항 안내", "explanation": "기계가 젖거나 떨어지면 검사가 무효화됩니다"},
            {"mistake": "증상 기록 방법 설명 안 함", "correction": "두근거림, 어지러움 등 증상 시 버튼 누르고 기록하라고 안내", "explanation": "증상과 심전도를 연관 지어 분석합니다"}
        ],
        [
            {"ko": "24시간 심전도 검사를 위해 기계를 부착하겠습니다.", "vi": "Tôi sẽ gắn máy để theo dõi điện tim 24 giờ.", "situation": "formal"},
            {"ko": "증상이 있으면 이 버튼을 누르세요.", "vi": "Nếu có triệu chứng hãy nhấn nút này.", "situation": "formal"},
            {"ko": "이거 달고 평소처럼 생활하시면 돼요.", "vi": "Đeo cái này rồi sinh hoạt bình thường.", "situation": "informal"}
        ],
        ["부정맥", "심전도", "심장초음파"]
    ),
    create_term(
        "xet-nghiem-di-ung", "알레르기검사", "xét nghiệm dị ứng", "알레르기檢査", None, "al-le-reu-gi-geom-sa",
        "특정 물질에 대한 알레르기 반응 여부를 확인하는 검사입니다. 피부반응검사와 혈액검사(특이 IgE)가 있습니다. 음식, 약물, 환경 물질 등에 대한 알레르기를 진단합니다. 통역 시 검사 전 항히스타민제 중단 기간, 검사 방법(피부에 살짝 찔러 반응 확인)을 안내해야 합니다.",
        "Phương pháp kiểm tra phản ứng dị ứng với các chất cụ thể",
        "알레르기내과, 피부과",
        "한국에서 알레르기검사는 아토피, 천식, 식품알레르기 등의 진단에 사용됩니다. 피부반응검사 전 항히스타민제를 일주일 정도 중단해야 정확한 결과를 얻을 수 있습니다.",
        [
            {"mistake": "알레르기검사 종류 설명 누락", "correction": "피부반응검사, 혈액검사의 차이점 설명", "explanation": "검사 방법에 따라 준비사항이 다릅니다"},
            {"mistake": "약물 중단 안내 없음", "correction": "항히스타민제, 스테로이드 중단 기간 안내", "explanation": "약물 복용 시 검사 결과가 부정확해집니다"},
            {"mistake": "양성 결과의 의미 오해", "correction": "검사 양성이 반드시 임상 알레르기를 의미하지 않음 설명", "explanation": "증상과 함께 해석해야 합니다"}
        ],
        [
            {"ko": "알레르기검사를 위해 팔 안쪽에 검사를 하겠습니다.", "vi": "Tôi sẽ làm xét nghiệm dị ứng ở mặt trong cánh tay.", "situation": "formal"},
            {"ko": "검사 일주일 전부터 알레르기약을 드시면 안 됩니다.", "vi": "Không được uống thuốc dị ứng từ 1 tuần trước khi xét nghiệm.", "situation": "formal"},
            {"ko": "집먼지진드기 알레르기가 있네요.", "vi": "Bạn bị dị ứng với mạt bụi nhà.", "situation": "informal"}
        ],
        ["아토피", "천식", "두드러기"]
    ),
    create_term(
        "test-gay-me", "마취전검사", "xét nghiệm tiền mê", "麻醉前檢査", "마(저릴 마) + 취(취할 취) + 전(앞 전) + 검(검사할 검) + 사(살필 사)", "ma-chwi-jeon-geom-sa",
        "수술 전 전신마취의 안전성을 평가하는 검사들입니다. 혈액검사, 심전도, 흉부X선, 폐기능검사 등이 포함됩니다. 마취과 의사와의 면담에서 과거 마취 경험, 알레르기, 복용 약물 등을 확인합니다. 통역 시 금식 시간, 복용 중단 약물, 마취 동의서 내용을 정확히 전달해야 합니다.",
        "Các xét nghiệm đánh giá an toàn trước khi gây mê cho phẫu thuật",
        "마취통증의학과",
        "한국에서 마취전검사는 수술 전 필수 과정입니다. 환자의 기저질환, 복용 약물에 따라 추가 검사가 필요할 수 있으며, 마취 방법 선택에도 영향을 미칩니다.",
        [
            {"mistake": "마취전검사 항목 설명 누락", "correction": "혈액검사, 심전도, 흉부X선 등 검사 항목 안내", "explanation": "환자가 어떤 검사를 받는지 알아야 합니다"},
            {"mistake": "금식 시간 부정확하게 전달", "correction": "수술 8시간 전부터 금식, 물도 금지", "explanation": "금식 위반 시 수술이 취소될 수 있습니다"},
            {"mistake": "복용 약물 정보 누락", "correction": "혈액응고제, 당뇨약 등 중단 여부 확인", "explanation": "일부 약물은 수술 전 중단해야 합니다"}
        ],
        [
            {"ko": "수술 전 마취검사를 받으셔야 합니다.", "vi": "Bạn cần xét nghiệm tiền mê trước khi phẫu thuật.", "situation": "formal"},
            {"ko": "마취과 선생님과 상담이 있을 예정입니다.", "vi": "Sẽ có buổi tư vấn với bác sĩ gây mê.", "situation": "formal"},
            {"ko": "전에 마취하고 이상 없으셨어요?", "vi": "Lần trước gây mê có vấn đề gì không?", "situation": "informal"}
        ],
        ["전신마취", "수술동의서", "금식"]
    ),
    create_term(
        "soi-ong-mat", "담도내시경", "nội soi đường mật", "膽道內視鏡", "담(쓸개 담) + 도(길 도) + 내(안 내) + 시(볼 시) + 경(거울 경)", "dam-do-nae-si-gyeong",
        "내시경을 이용하여 담관과 췌관을 검사하고 치료하는 시술입니다. ERCP(내시경역행담췌관조영술)라고도 합니다. 담석 제거, 담관암 진단, 스텐트 삽입 등에 사용됩니다. 통역 시 검사 목적, 합병증(췌장염, 출혈) 가능성, 금식 등을 설명해야 합니다.",
        "Phương pháp kiểm tra và điều trị đường mật và tụy bằng nội soi",
        "소화기내과",
        "한국에서 ERCP는 담도 질환 치료에 중요한 시술입니다. 진단과 치료를 동시에 할 수 있지만 합병증 위험이 있어 동의서 설명이 중요합니다.",
        [
            {"mistake": "ERCP를 설명 없이 사용", "correction": "'nội soi đường mật' 또는 풀어서 설명", "explanation": "의학 약어는 환자가 이해하기 어렵습니다"},
            {"mistake": "합병증 설명 생략", "correction": "췌장염, 출혈, 천공 등 합병증 가능성 안내", "explanation": "동의서에 포함된 내용을 정확히 전달해야 합니다"},
            {"mistake": "치료적 시술 가능성 미언급", "correction": "담석 제거, 스텐트 삽입 등이 가능함을 안내", "explanation": "검사와 치료가 동시에 진행될 수 있습니다"}
        ],
        [
            {"ko": "담석을 제거하기 위해 담도내시경을 하겠습니다.", "vi": "Chúng tôi sẽ nội soi đường mật để lấy sỏi.", "situation": "formal"},
            {"ko": "시술 후 췌장염이 생길 수 있습니다.", "vi": "Sau thủ thuật có thể bị viêm tụy.", "situation": "formal"},
            {"ko": "담석 빼는 건 내시경으로 가능해요.", "vi": "Có thể lấy sỏi mật bằng nội soi.", "situation": "informal"}
        ],
        ["담석", "황달", "췌장염"]
    )
]

new_terms.extend(more_diagnostic)

print(f"생성된 새 용어 수: {len(new_terms)}")

# 기존 데이터와 병합
all_terms = existing_terms + [t for t in new_terms if t['slug'] not in existing_slugs]
print(f"총 용어 수: {len(all_terms)}")

# 저장
with open(medical_path, 'w', encoding='utf-8') as f:
    json.dump(all_terms, f, ensure_ascii=False, indent=2)

print("medical.json 저장 완료")
