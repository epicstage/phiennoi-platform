import json
import os

def t(s, k, v, h, hr, p, mk, mv, cx, cn, cm, ex, rt):
    return {
        "slug": s, "korean": k, "vietnamese": v,
        "hanja": h, "hanjaReading": hr, "pronunciation": p,
        "meaningKo": mk, "meaningVi": mv, "context": cx,
        "culturalNote": cn, "commonMistakes": cm,
        "examples": ex, "relatedTerms": rt
    }

terms = [
    # 751-800: Emergency Medicine, Critical Care, Pain Management, Sleep Medicine, Clinical Trials, Bioethics, Telemedicine

    t("phan-loai-khan-cap", "중증도 분류", "phân loại khẩn cấp",
      "重症度分類", "무거울 중(重) + 병 증(症) + 정도 도(度) + 나눌 분(分) + 종류 류(類)",
      "중증도 분류",
      "응급실에서 환자의 상태를 긴급도와 중증도에 따라 분류하는 시스템으로, 통역 시 주의할 점은 한국은 KTAS(Korean Triage and Acuity Scale) 1~5단계를 사용하며 숫자가 낮을수록 위급함을 의미한다는 것입니다. 베트남 통역사는 'phân loại'를 단순히 '분류'로만 이해하지 말고, 생명과 직결된 우선순위 결정 과정임을 강조해야 합니다. 특히 보호자에게 '3단계라 괜찮다'는 오해를 주지 않도록 '응급 상황이지만 1~2단계보다 덜 위급하다'는 뉘앙스로 전달해야 합니다.",
      "Hệ thống phân loại tình trạng bệnh nhân tại phòng cấp cứu theo mức độ khẩn cấp và nghiêm trọng. Hàn Quốc sử dụng KTAS với 5 cấp độ, số càng thấp càng nguy kịch.",
      "emergency",
      "한국 응급실은 KTAS 5단계 체계를 사용하여 환자를 분류하는데, 1단계(소생)가 가장 위급하고 5단계(비응급)가 가장 낮습니다. 베트남은 3단계 체계(cấp cứu đỏ/vàng/xanh)를 주로 사용하므로, 통역 시 양국 체계의 차이를 명확히 설명해야 합니다. '3단계'라는 숫자만 들으면 보호자가 '중간 정도'로 오해할 수 있으므로 주의가 필요합니다.",
      [
        {"mistake": "Phân loại cấp 3", "correction": "Phân loại mức độ khẩn cấp cấp 3 (KTAS)", "explanation": "KTAS 체계임을 명시하지 않으면 베트nam 색상 체계와 혼동"},
        {"mistake": "Cấp 3 không nghiêm trọng", "correction": "Cấp 3 cần điều trị trong 30 phút, vẫn là tình trạng khẩn cấp", "explanation": "숫자가 크다고 안전하다는 오해 방지"},
        {"mistake": "Triaging", "correction": "Phân loại khẩn cấp (triage)", "explanation": "영어 발음보다 베트남어로 설명 후 영어 병기"}
      ],
      [
        {"ko": "환자분은 KTAS 3단계로 분류되어 30분 이내 진료를 받으실 예정입니다.", "vi": "Bệnh nhân được phân loại KTAS cấp 3, sẽ được khám trong vòng 30 phút.", "situation": "formal"},
        {"ko": "지금 1단계 환자가 들어와서 먼저 처치하고 있습니다.", "vi": "Hiện có bệnh nhân cấp 1 vừa đến nên đang được xử lý trước.", "situation": "onsite"},
        {"ko": "중증도 분류는 도착 순서가 아니라 위급도로 결정됩니다.", "vi": "Phân loại khẩn cấp được quyết định theo mức độ nguy kịch chứ không phải thứ tự đến.", "situation": "informal"}
      ],
      ["응급실", "KTAS", "우선순위"]),

    t("noi-khi-quan", "기관내삽관", "nội khí quản",
      "氣管內揷管", "기운 기(氣) + 대롱 관(管) + 안 내(內) + 꽂을 삽(揷) + 대롱 관(管)",
      "기관내삽관",
      "기도를 확보하기 위해 후두를 통해 기관 안으로 튜브를 삽입하는 응급처치로, 통역 시 주의할 점은 'intubation'을 '삽관'이라고만 하면 보호자가 이해하지 못하므로 '호흡을 돕기 위해 목 안에 튜브를 넣는 것'이라고 풀어서 설명해야 합니다. 베트남에서는 'đặt nội khí quản' 또는 'đặt ống nội khí quản'이라고 하는데, 한국에서는 '기관내삽관' 또는 줄여서 '인튜베이션'이라고 합니다. 응급 상황에서 보호자 동의를 구할 때는 신속하면서도 정확한 설명이 생명과 직결되므로 평소 연습이 필수입니다.",
      "Thủ thuật đặt ống qua thanh quản vào khí quản để đảm bảo đường thở. Thường dùng trong cấp cứu, gây mê, hoặc hỗ trợ hô hấp.",
      "emergency",
      "한국 응급실에서는 의식이 없거나 호흡곤란이 심한 환자에게 즉시 시행하며, 보호자 동의 없이도 응급처치로 진행할 수 있습니다. 베트남에서도 유사하지만, 가족의 입회를 중시하는 문화적 차이가 있어 통역 시 '응급 상황이라 즉시 시행했다'는 설명이 필요할 수 있습니다. 또한 '기관절개술(mở khí quản)'과 혼동하지 않도록 주의해야 합니다.",
      [
        {"mistake": "Đặt ống thở", "correction": "Đặt nội khí quản (intubation)", "explanation": "일반 산소호흡과 구분 필요"},
        {"mistake": "Mở khí quản", "correction": "Đặt nội khí quản qua miệng/mũi", "explanation": "기관절개술(tracheostomy)과 혼동"},
        {"mistake": "Đã cho ống vào", "correction": "Đã đặt nội khí quản để hỗ trợ hô hấp", "explanation": "목적과 상황 설명 없이 행위만 전달하면 보호자 불안 가중"}
      ],
      [
        {"ko": "환자분 상태가 위중하여 기관내삽관을 시행했습니다.", "vi": "Tình trạng bệnh nhân nguy kịch nên đã đặt nội khí quản.", "situation": "formal"},
        {"ko": "지금 인튜베이션 하고 있으니까 잠시만 밖에서 기다려 주세요.", "vi": "Hiện đang đặt ống nội khí quản, vui lòng đợi bên ngoài một chút.", "situation": "onsite"},
        {"ko": "삽관 후 인공호흡기를 연결할 겁니다.", "vi": "Sau khi đặt nội khí quản sẽ nối máy thở.", "situation": "informal"}
      ],
      ["인공호흡기", "기도확보", "응급처치"]),

    t("soc-tim-phoi", "심폐소생술", "sốc tim phổi",
      "心肺蘇生術", "마음 심(心) + 허파 폐(肺) + 깨어날 소(蘇) + 날 생(生) + 기술 술(術)",
      "심폐소생술",
      "심장과 호흡이 멈춘 환자에게 인공적으로 혈액순환과 호흡을 유지하는 응급처치로, 영어로는 CPR(Cardiopulmonary Resuscitation)이라고 합니다. 통역 시 주의할 점은 '소생술'이라는 단어가 '다시 살린다'는 의미여서 보호자가 100% 살아날 것으로 오해할 수 있다는 점입니다. 베트남어로는 'sốc tim phổi' 또는 'hồi sức tim phổi'라고 하는데, 의료진이 CPR 시행 동의를 구할 때는 '생존 가능성을 높이기 위한 시도'라는 뉘앙스로 전달해야 합니다. 또한 가족이 CPR 중단을 원하는 경우(DNR) 통역은 매우 민감하므로 정확하고 신중하게 해야 합니다.",
      "Kỹ thuật cấp cứu duy trì tuần hoàn máu và hô hấp khi tim ngừng đập. Bao gồm ép tim và thổi ngạt nhân tạo.",
      "emergency",
      "한국에서는 119 구급대원도 CPR 교육을 받으며, 병원 도착 전부터 시행하는 경우가 많습니다. 베트남에서도 점차 일반인 CPR 교육이 확대되고 있지만, 문화적으로 '시신을 건드리는 것'에 대한 거부감이 있을 수 있습니다. 통역 시 '생명을 구하기 위한 마지막 노력'임을 강조하되, 가족의 감정을 존중하는 태도가 중요합니다.",
      [
        {"mistake": "Đang ép tim", "correction": "Đang thực hiện hồi sức tim phổi (CPR)", "explanation": "가슴압박만 언급하면 전체 시술 이해 어려움"},
        {"mistake": "Sẽ cứu sống", "correction": "Đang nỗ lực hồi sức, tăng khả năng sống sót", "explanation": "100% 소생 보장으로 오해 방지"},
        {"mistake": "Bơm tim", "correction": "Ép tim trong CPR", "explanation": "'bơm'은 펌프 느낌, 'ép'이 의학 용어"}
      ],
      [
        {"ko": "심정지 발생하여 즉시 심폐소생술을 시행했습니다.", "vi": "Đã xảy ra ngừng tim, lập tức thực hiện CPR.", "situation": "formal"},
        {"ko": "지금 CPR 하고 있는데 가족분들 들어오시면 힘드실 거예요.", "vi": "Hiện đang làm CPR, gia đình vào có thể sẽ rất khó chịu.", "situation": "onsite"},
        {"ko": "소생술 30분 했는데 반응이 없으시네요.", "vi": "Đã hồi sức 30 phút nhưng không có phản ứng.", "situation": "informal"}
      ],
      ["심정지", "응급처치", "제세동기"]),

    t("soc-dien", "제세동", "sốc điện",
      "除細動", "덜 제(除) + 가늘 세(細) + 움직일 동(動)",
      "제세동",
      "심실세동 등 치명적 부정맥을 치료하기 위해 전기충격을 가하는 응급처치로, 영어로는 'defibrillation'이라고 합니다. 통역 시 주의할 점은 '전기 충격'이라는 말에 보호자가 공포를 느낄 수 있으므로 '심장 리듬을 정상으로 되돌리기 위한 치료'라고 설명해야 합니다. 베트남어로는 'sốc điện' 또는 'khử rung tim'이라고 하는데, 'sốc'이라는 단어가 '쇼크' 상태와 혼동될 수 있으니 'điện giật điều trị'(치료적 전기 충격)로 풀어 설명하는 것이 좋습니다. 자동제세동기(AED) 사용법도 함께 숙지해야 합니다.",
      "Kỹ thuật sử dụng xung điện để phục hồi nhịp tim bình thường khi có rối loạn nhịp nguy hiểm như rung thất.",
      "emergency",
      "한국은 공공장소에 자동제세동기(AED) 설치가 의무화되어 있고, 일반인도 사용할 수 있도록 안내되어 있습니다. 베트남은 아직 AED 보급이 제한적이므로, 베트남 환자 가족이 '전기 충격'에 대해 생소하거나 두려워할 수 있습니다. 통역 시 '안전하고 검증된 치료법'임을 강조하는 것이 중요합니다.",
      [
        {"mistake": "Giật điện", "correction": "Sốc điện điều trị (defibrillation)", "explanation": "'giật điện'은 감전사고 느낌"},
        {"mistake": "Sẽ đánh điện", "correction": "Sẽ thực hiện sốc điện để điều chỉnh nhịp tim", "explanation": "목적 설명 없이 행위만 언급하면 공포 유발"},
        {"mistake": "Máy sốc", "correction": "Máy khử rung tim (defibrillator)", "explanation": "'sốc'만으로는 기능 불명확"}
      ],
      [
        {"ko": "심실세동이 발생하여 즉시 제세동을 시행합니다.", "vi": "Có rung thất, lập tức thực hiện sốc điện.", "situation": "formal"},
        {"ko": "지금 패들 대고 쇼크 줄게요, 다들 떨어지세요!", "vi": "Bây giờ sẽ sốc, mọi người tránh ra!", "situation": "onsite"},
        {"ko": "AED 가져와서 바로 붙여!", "vi": "Lấy AED đến và gắn ngay!", "situation": "informal"}
      ],
      ["심실세동", "자동제세동기", "심폐소생술"]),

    t("chan-thuong-da-chan", "다발성 외상", "chấn thương đa chấn",
      "多發性外傷", "많을 다(多) + 필 발(發) + 성품 성(性) + 바깥 외(外) + 다칠 상(傷)",
      "다발성 외상",
      "교통사고나 추락 등으로 여러 신체 부위에 동시에 손상을 입은 상태로, 영어로는 'multiple trauma' 또는 'polytrauma'라고 합니다. 통역 시 주의할 점은 '다발성'을 단순히 '여러 곳'으로만 전달하면 심각성이 저평가될 수 있으므로, '생명을 위협하는 복합 손상'이라는 뉘앙스를 전달해야 합니다. 베트남어로는 'chấn thương đa chấn' 또는 'chấn thương phối hợp'이라고 하며, 외상센터(trauma center)에서 다학제 팀이 동시에 치료합니다. 손상 부위와 중증도를 정확히 전달하는 것이 초기 치료 방향 결정에 중요합니다.",
      "Tình trạng tổn thương đồng thời ở nhiều vị trí trên cơ thể do tai nạn, té ngã hoặc bạo lực. Cần điều trị khẩn cấp đa chuyên khoa.",
      "emergency",
      "한국의 권역외상센터는 24시간 다학제 팀(외과, 정형외과, 신경외과, 흉부외과 등)이 대기하며, 골든타임 내 수술이 가능합니다. 베트남도 대도시 중심으로 외상센터가 생기고 있지만, 지방에서는 여러 병원을 옮겨야 하는 경우가 많습니다. 통역 시 한국 외상센터의 통합 치료 시스템을 설명하면 가족의 불안을 줄일 수 있습니다.",
      [
        {"mistake": "Bị thương nhiều chỗ", "correction": "Chấn thương đa chấn (multiple trauma)", "explanation": "의학적 심각성 표현 부족"},
        {"mistake": "Gãy xương nhiều", "correction": "Chấn thương đa chấn bao gồm gãy xương, chấn thương nội tạng...", "explanation": "골절 외 내부 장기 손상도 포함됨을 명시"},
        {"mistake": "Tai nạn nặng", "correction": "Chấn thương đa chấn do tai nạn", "explanation": "사고 결과가 아닌 의학적 상태로 표현"}
      ],
      [
        {"ko": "교통사고로 다발성 외상을 입어 여러 과에서 동시 치료 중입니다.", "vi": "Do tai nạn giao thông bị chấn thương đa chấn, nhiều khoa đang điều trị đồng thời.", "situation": "formal"},
        {"ko": "골반골절, 간 파열, 두부외상 다 있어요.", "vi": "Có gãy xương chậu, vỡ gan, chấn thương sọ não.", "situation": "onsite"},
        {"ko": "폴리트라우마라 응급수술 들어갑니다.", "vi": "Do đa chấn thương nên sẽ phẫu thuật cấp cứu.", "situation": "informal"}
      ],
      ["외상센터", "골든타임", "다학제치료"]),

    t("co-giat", "경련", "co giật",
      "痙攣", "경련 경(痙) + 경련 련(攣)",
      "경련",
      "뇌의 비정상적 전기 활동으로 근육이 불수의적으로 수축하는 증상으로, 영어로는 'seizure' 또는 'convulsion'이라고 합니다. 통역 시 주의할 점은 '경련'과 '발작(cơn động kinh)'을 구분해야 하며, 일회성 경련인지 만성 뇌전증(epilepsy)의 증상인지 맥락을 파악해야 합니다. 베트남어로는 'co giật'이 일반적이며, 'cơn giật'은 발작 에피소드를 의미합니다. 응급실에서 경련 환자 발생 시 보호자에게 '언제, 얼마나 지속되었는지, 처음인지' 등을 신속히 묻고 의료진에게 전달하는 것이 중요합니다.",
      "Tình trạng co thắt cơ không tự chủ do hoạt động điện bất thường trong não. Có thể do sốt cao, động kinh, hoặc các nguyên nhân khác.",
      "emergency",
      "한국에서는 열성경련(co giật do sốt)이 소아에게 흔하며, 대부분 양성이지만 보호자가 극도로 불안해합니다. 베트남도 유사하나, '경련=귀신 들림'으로 오해하는 전통적 인식이 남아있을 수 있어, 통역 시 '뇌의 일시적 전기 이상'이라는 과학적 설명이 필요합니다. 또한 경련 중 혀를 깨물까봐 입에 물건을 넣는 잘못된 응급처치를 막아야 합니다.",
      [
        {"mistake": "Động kinh", "correction": "Co giật (có thể do nhiều nguyên nhân, không nhất thiết là động kinh)", "explanation": "일회성 경련을 뇌전증으로 단정 금지"},
        {"mistake": "Giật mình", "correction": "Co giật toàn thân", "explanation": "'giật mình'은 놀람 반응, 의학적 경련과 다름"},
        {"mistake": "Lên cơn", "correction": "Xuất hiện cơn co giật", "explanation": "'lên cơn'만으로는 어떤 증상인지 불명확"}
      ],
      [
        {"ko": "아이가 고열로 인한 열성 경련을 일으켰습니다.", "vi": "Trẻ bị co giật do sốt cao.", "situation": "formal"},
        {"ko": "지금 경련 하고 있으니 입에 아무것도 넣지 마세요!", "vi": "Hiện đang co giật, đừng cho gì vào miệng!", "situation": "onsite"},
        {"ko": "경련 멈추고 5분 지났는데 아직 의식이 안 돌아와요.", "vi": "Co giật đã ngừng 5 phút nhưng vẫn chưa tỉnh.", "situation": "informal"}
      ],
      ["열성경련", "뇌전증", "항경련제"]),

    t("soc-phan-ung", "아나필락시스", "sốc phản ứng",
      null, null,
      "아나필락시스",
      "알레르기 항원에 노출된 후 발생하는 급성 전신 과민반응으로, 기도 폐쇄와 혈압 저하로 생명을 위협할 수 있습니다. 영어로는 'anaphylaxis'이며, 통역 시 주의할 점은 단순 알레르기 반응과 구분하여 '생명을 위협하는 심각한 알레르기 쇼크'임을 강조해야 합니다. 베트남어로는 'sốc phản ứng' 또는 'phản vệ'라고 하며, 에피네프린(adrenaline) 자가주사기(EpiPen)를 즉시 투여해야 합니다. 음식, 약물, 벌침 등 원인 물질을 신속히 파악하고 전달하는 것이 재발 방지에 중요합니다.",
      "Phản ứng dị ứng nghiêm trọng toàn thân, có thể gây tắc đường thở và sốc. Cần tiêm adrenaline khẩn cấp.",
      "emergency",
      "한국에서는 땅콩, 갑각류 알레르기가 증가 추세이며, 학교에서 에피펜 사용 교육이 확대되고 있습니다. 베트남은 해산물 알레르기가 흔하나 아나필락시스 인지도가 낮아, 중증 반응을 '체한 것'으로 오인하는 경우가 있습니다. 통역 시 '알레르기가 아니라 쇼크'라는 점을 명확히 해야 합니다.",
      [
        {"mistake": "Dị ứng nặng", "correction": "Sốc phản ứng (anaphylaxis)", "explanation": "일반 알레르기와 생명 위협 쇼크는 다름"},
        {"mistake": "Bị ngộ độc", "correction": "Sốc phản ứng dị ứng", "explanation": "중독과 알레르기 반응 혼동"},
        {"mistake": "Tiêm thuốc dị ứng", "correction": "Tiêm adrenaline cấp cứu", "explanation": "항히스타민제가 아닌 에피네프린임을 명시"}
      ],
      [
        {"ko": "새우 먹고 아나필락시스 쇼크가 왔습니다.", "vi": "Ăn tôm bị sốc phản ứng.", "situation": "formal"},
        {"ko": "지금 목 붓고 숨 안 쉬어져요, 에피 놔!", "vi": "Hiện sưng cổ, khó thở, tiêm adrenaline!", "situation": "onsite"},
        {"ko": "앞으로 이 약은 절대 드시면 안 됩니다.", "vi": "Từ nay tuyệt đối không được dùng thuốc này.", "situation": "informal"}
      ],
      ["에피네프린", "알레르기", "쇼크"]),

    t("thong-khi-nhan-tao", "인공호흡기", "thông khí nhân tạo",
      "人工呼吸器", "사람 인(人) + 장인 공(工) + 부를 호(呼) + 마실 흡(吸) + 그릇 기(器)",
      "인공호흡기",
      "스스로 호흡이 불가능하거나 불충분한 환자에게 기계적으로 환기를 제공하는 의료기기로, 영어로는 'ventilator' 또는 'mechanical ventilator'라고 합니다. 통역 시 주의할 점은 '인공호흡기 적용'이 곧 '죽음'을 의미한다고 오해하는 보호자가 많으므로, '호흡을 돕는 장치'이며 회복 후 제거 가능함을 설명해야 합니다. 베트남어로는 'máy thở' 또는 'thở máy'라고 하며, '호흡기를 떼는 것(weaning, cai máy thở)'도 중요한 통역 포인트입니다. 설정값(PEEP, FiO2 등)은 전문 용어이므로 숫자와 단위를 정확히 전달해야 합니다.",
      "Thiết bị y tế hỗ trợ hoặc thay thế hô hấp tự nhiên cho bệnh nhân không thể tự thở đủ. Thường dùng trong ICU.",
      "critical care",
      "한국 중환자실에서는 진정제를 투여하면서 인공호흡기를 적용하는 경우가 많아, 환자가 의식이 없어 보여 보호자가 충격을 받습니다. 베트남도 유사하나, '기계에 의존한다'는 부정적 인식이 강할 수 있습니다. 통역 시 '폐를 쉬게 하여 회복을 돕는 치료'라는 긍정적 프레임을 사용하는 것이 좋습니다.",
      [
        {"mistake": "Máy oxy", "correction": "Máy thở (ventilator)", "explanation": "산소마스크와 인공호흡기는 다름"},
        {"mistake": "Thở ống", "correction": "Sử dụng máy thở/thở máy", "explanation": "'ống'만으로는 기능 불명확"},
        {"mistake": "Đã cắm máy", "correction": "Đã đặt nội khí quản và nối máy thở", "explanation": "'cắm'은 부정적 뉘앙스, 의학적 표현 사용"}
      ],
      [
        {"ko": "호흡 부전으로 인공호흡기 치료를 시작했습니다.", "vi": "Do suy hô hấp nên bắt đầu điều trị bằng máy thở.", "situation": "formal"},
        {"ko": "벤틸레이터 세팅 PEEP 5, FiO2 40%로 갑니다.", "vi": "Cài đặt máy thở PEEP 5, FiO2 40%.", "situation": "onsite"},
        {"ko": "이제 스스로 숨 쉴 수 있어서 호흡기 뺄 예정입니다.", "vi": "Giờ đã thở được tự nhiên nên sẽ rút máy thở.", "situation": "informal"}
      ],
      ["기관내삽관", "중환자실", "호흡부전"]),

    t("thuoc-an-than", "진정제", "thuốc an thần",
      "鎭靜劑", "누를 진(鎭) + 고요할 정(靜) + 약 제(劑)",
      "진정제",
      "중추신경계를 억제하여 불안을 감소시키고 진정 상태를 유도하는 약물로, 영어로는 'sedative'라고 합니다. 통역 시 주의할 점은 '수면제(sleeping pill)'와 구분해야 하며, 중환자실에서는 인공호흡기 적용 시 환자의 고통을 줄이기 위해 사용한다는 점을 설명해야 합니다. 베트남어로는 'thuốc an thần' 또는 'thuốc an định'이라고 하며, 진정 깊이(sedation level)는 의식 수준과 직결되므로 정확한 전달이 중요합니다. 또한 'midazolam', 'propofol' 등 약물명은 발음 그대로 전달하되, 용량과 투여 속도를 명확히 해야 합니다.",
      "Thuốc ức chế thần kinh trung ương để giảm lo âu, tạo trạng thái an thần. Thường dùng trong ICU khi thở máy.",
      "critical care",
      "한국 중환자실에서는 프로토콜에 따라 진정 깊이를 조절하며, RASS 점수(Richmond Agitation-Sedation Scale)로 평가합니다. 베트남도 유사하나, 가족이 '환자가 혼수상태'로 오해할 수 있으므로 통역 시 '치료를 위해 의도적으로 재우는 것'임을 강조해야 합니다. 또한 진정제 중단 시 섬망 가능성도 미리 안내하는 것이 좋습니다.",
      [
        {"mistake": "Thuốc ngủ", "correction": "Thuốc an thần (sedative)", "explanation": "수면제와 진정제는 목적과 강도가 다름"},
        {"mistake": "Cho hôn mê", "correction": "Sử dụng thuốc an thần sâu để hỗ trợ điều trị", "explanation": "'혼수'는 병적 상태, 치료적 진정과 구분"},
        {"mistake": "Tiêm thuốc mê", "correction": "Tiêm thuốc an thần (không phải gây mê phẫu thuật)", "explanation": "전신마취와 진정 구분"}
      ],
      [
        {"ko": "인공호흡기 사용 중이라 진정제를 지속 투여하고 있습니다.", "vi": "Do đang thở máy nên liên tục truyền thuốc an thần.", "situation": "formal"},
        {"ko": "프로포폴 줄이면서 깨워볼게요.", "vi": "Sẽ giảm propofol để đánh thức.", "situation": "onsite"},
        {"ko": "진정 끊으면 좀 흥분할 수 있어요.", "vi": "Khi ngừng an thần có thể kích động.", "situation": "informal"}
      ],
      ["인공호흡기", "섬망", "RASS"]),

    t("cham-soc-tich-cuc", "중환자 치료", "chăm sóc tích cực",
      "重患者治療", "무거울 중(重) + 근심 환(患) + 사람 자(者) + 다스릴 치(治) + 괴로울 료(療)",
      "중환자 치료",
      "생명을 위협하는 중증 질환이나 손상을 가진 환자를 집중적으로 모니터링하고 치료하는 것으로, 중환자실(ICU)에서 이루어집니다. 영어로는 'intensive care' 또는 'critical care'라고 합니다. 통역 시 주의할 점은 중환자실 입실 자체가 '곧 죽는다'는 의미가 아니라 '집중 관찰과 치료가 필요한 상태'임을 설명해야 합니다. 베트남어로는 'chăm sóc tích cực' 또는 줄여서 'hồi sức'이라고 하며, 면회 제한, 무균 관리 등 ICU 규칙도 함께 설명해야 합니다. 다장기부전(multi-organ failure) 등 복잡한 상태를 보호자가 이해할 수 있도록 풀어 설명하는 능력이 필요합니다.",
      "Điều trị và theo dõi tập trung cho bệnh nhân nguy kịch tại ICU. Bao gồm hỗ trợ đa cơ quan và theo dõi sát 24/7.",
      "critical care",
      "한국의 ICU는 간호사 1명당 환자 2~3명으로 집중 케어가 가능하며, 최신 모니터링 장비를 갖추고 있습니다. 베트남은 대도시 대형병원 외에는 ICU 시설이 제한적이고, 가족이 간병하는 문화가 강해 면회 제한에 불만이 있을 수 있습니다. 통역 시 감염 예방과 치료 집중을 위한 불가피한 조치임을 설명해야 합니다.",
      [
        {"mistake": "Phòng cấp cứu", "correction": "Phòng hồi sức tích cực (ICU)", "explanation": "응급실과 중환자실은 다른 공간"},
        {"mistake": "Điều trị đặc biệt", "correction": "Chăm sóc tích cực/Hồi sức", "explanation": "'특별 치료'는 모호함"},
        {"mistake": "Vào ICU là nguy hiểm lắm", "correction": "Vào ICU để được theo dõi và điều trị sát sao", "explanation": "부정적 뉘앙스 → 긍정적 프레임"}
      ],
      [
        {"ko": "상태가 불안정하여 중환자실로 입실했습니다.", "vi": "Tình trạng không ổn định nên chuyển vào ICU.", "situation": "formal"},
        {"ko": "ICU에서 24시간 모니터링하면서 치료할 겁니다.", "vi": "Tại ICU sẽ theo dõi 24 giờ và điều trị.", "situation": "onsite"},
        {"ko": "중환자실은 면회 시간이 정해져 있어요.", "vi": "ICU có giờ thăm bệnh cố định.", "situation": "informal"}
      ],
      ["중환자실", "다장기부전", "생체징후감시"]),

    t("chan-dau-than-kinh", "신경차단술", "chặn đau thần kinh",
      "神經遮斷術", "귀신 신(神) + 지날 경(經) + 가릴 차(遮) + 끊을 단(斷) + 기술 술(術)",
      "신경차단술",
      "통증을 전달하는 신경에 국소마취제나 약물을 주입하여 통증 신호를 차단하는 시술로, 영어로는 'nerve block'이라고 합니다. 통역 시 주의할 점은 '신경을 자르는 것'으로 오해하지 않도록 '일시적으로 통증 전달을 차단하는 것'임을 설명해야 합니다. 베트남어로는 'chặn thần kinh' 또는 'gây tê thần kinh'이라고 하며, 경막외차단(epidural block), 척추차단(spinal block) 등 종류가 다양하므로 정확한 명칭을 전달해야 합니다. 출산 시 무통분만(painless delivery)에 사용되는 경막외마취도 신경차단의 일종입니다.",
      "Kỹ thuật tiêm thuốc tê hoặc thuốc giảm đau vào vùng thần kinh để ngăn tín hiệu đau. Dùng trong phẫu thuật, đẻ không đau, hoặc điều trị đau mãn tính.",
      "pain management",
      "한국에서는 무통분만 선택률이 높아지고 있으며, 통증클리닉에서 만성 통증 치료로도 널리 사용됩니다. 베트남은 전통적으로 '자연분만=고통을 견뎌야 한다'는 인식이 있어 무통분만 선택률이 낮았으나, 최근 증가 추세입니다. 통역 시 '아기에게 영향 없다'는 점을 강조하면 선택에 도움이 됩니다.",
      [
        {"mistake": "Cắt thần kinh", "correction": "Chặn thần kinh (tạm thời)", "explanation": "신경 절단이 아닌 일시적 차단"},
        {"mistake": "Gây mê cột sống", "correction": "Gây tê vùng cột sống (spinal/epidural block)", "explanation": "전신마취와 구분"},
        {"mistake": "Tiêm thuốc giảm đau", "correction": "Tiêm chặn thần kinh để giảm đau", "explanation": "일반 진통제 주사와 구분"}
      ],
      [
        {"ko": "수술 후 통증 관리를 위해 신경차단술을 시행합니다.", "vi": "Để kiểm soát đau sau phẫu thuật sẽ thực hiện chặn thần kinh.", "situation": "formal"},
        {"ko": "무통주사 맞으실 건가요?", "vi": "Có muốn tiêm giảm đau (epidural) không?", "situation": "onsite"},
        {"ko": "블록 효과는 몇 시간 갑니다.", "vi": "Hiệu quả chặn thần kinh kéo dài vài giờ.", "situation": "informal"}
      ],
      ["무통분만", "경막외마취", "통증관리"]),

    t("thang-do-dau", "통증 척도", "thang đo đau",
      "痛症尺度", "아플 통(痛) + 병 증(症) + 자 척(尺) + 법도 도(度)",
      "통증 척도",
      "환자가 느끼는 통증의 강도를 객관적으로 평가하기 위한 도구로, 가장 흔한 것은 0~10점 숫자 척도(NRS, Numerical Rating Scale)입니다. 통역 시 주의할 점은 '10점 만점에 몇 점'이라고 물을 때 문화적 차이로 인해 과소평가하거나 과대평가할 수 있다는 것입니다. 베트남어로는 'thang đo đau' 또는 'mức độ đau'라고 하며, 0은 '전혀 안 아픔(không đau)', 10은 '상상할 수 있는 최악의 통증(đau không chịu nổi)'임을 명확히 설명해야 합니다. 얼굴 표정 척도(faces scale)는 소아나 언어 장벽이 있는 환자에게 유용합니다.",
      "Công cụ đánh giá mức độ đau của bệnh nhân, thường dùng thang 0-10 (0 = không đau, 10 = đau tột độ).",
      "pain management",
      "한국 의료진은 통증을 '5번째 활력징후'로 간주하여 자주 평가하는데, 베트남 환자는 '참는 것이 미덕'이라 생각하여 낮게 답하는 경향이 있습니다. 반대로 한국 환자는 적극적으로 통증을 호소합니다. 통역 시 '정확한 평가를 위해 솔직하게 답해야 한다'고 안내하는 것이 중요합니다.",
      [
        {"mistake": "Đau mấy phần trăm?", "correction": "Đau mức độ bao nhiêu từ 0 đến 10?", "explanation": "퍼센트가 아닌 0~10 척도"},
        {"mistake": "Có đau không?", "correction": "Mức độ đau từ 0-10 là bao nhiêu?", "explanation": "유무가 아닌 강도 측정"},
        {"mistake": "Đau nhiều hay ít?", "correction": "Đánh giá mức đau trên thang 0-10", "explanation": "주관적 표현보다 객관적 척도"}
      ],
      [
        {"ko": "지금 통증이 0에서 10점 중 몇 점이세요?", "vi": "Hiện tại mức độ đau của anh/chị từ 0 đến 10 là bao nhiêu?", "situation": "formal"},
        {"ko": "NRS 5점 이상이면 진통제 드릴게요.", "vi": "Nếu mức đau 5 trở lên sẽ cho thuốc giảm đau.", "situation": "onsite"},
        {"ko": "통증 점수 좀 매겨 보세요.", "vi": "Cho biết mức độ đau bao nhiêu điểm.", "situation": "informal"}
      ],
      ["통증관리", "진통제", "NRS"]),

    t("roi-loan-giay-ngu", "수면 장애", "rối loạn giấc ngủ",
      "睡眠障碍", "잘 수(睡) + 잘 면(眠) + 막힐 장(障) + 어그러질 애(碍)",
      "수면 장애",
      "정상적인 수면 패턴이 방해받아 충분한 수면을 취하지 못하는 상태로, 불면증, 수면무호흡증, 기면증 등 다양한 유형이 있습니다. 영어로는 'sleep disorder'라고 합니다. 통역 시 주의할 점은 단순히 '잠을 못 잔다'는 것과 의학적 수면장애를 구분해야 하며, 수면다원검사(polysomnography) 등 정밀 검사가 필요할 수 있음을 설명해야 합니다. 베트남어로는 'rối loạn giấc ngủ' 또는 'mất ngủ'(불면증)라고 하며, 수면위생(sleep hygiene) 교육도 중요한 치료의 일부입니다.",
      "Tình trạng giấc ngủ bị ảnh hưởng, không đủ giấc hoặc chất lượng kém. Bao gồm mất ngủ, ngưng thở khi ngủ, ngủ rũ...",
      "sleep medicine",
      "한국에서는 스트레스와 야간 근무로 인한 불면증이 증가하고 있으며, 수면클리닉과 수면다원검사 시설이 확대되고 있습니다. 베트남도 도시화로 수면장애가 증가 중이나, '정신과 문제'로 오해하여 치료를 꺼리는 경우가 있습니다. 통역 시 '뇌와 신체의 생리적 문제'임을 강조하는 것이 좋습니다.",
      [
        {"mistake": "Không ngủ được", "correction": "Rối loạn giấc ngủ (cần đánh giá y khoa)", "explanation": "일시적 불면과 의학적 장애 구분"},
        {"mistake": "Hay mơ", "correction": "Có thể là rối loạn giấc ngủ REM", "explanation": "악몽과 REM 수면행동장애 구분"},
        {"mistake": "Ngủ nhiều", "correction": "Ngủ quá nhiều (hypersomnia/rối loạn ngủ rũ)", "explanation": "과다수면도 수면장애의 일종"}
      ],
      [
        {"ko": "수면다원검사로 수면 패턴을 분석하겠습니다.", "vi": "Sẽ phân tích giấc ngủ bằng xét nghiệm đa ký giấc ngủ.", "situation": "formal"},
        {"ko": "코골이랑 무호흡이 심하시네요.", "vi": "Ngáy và ngưng thở khi ngủ khá nặng.", "situation": "onsite"},
        {"ko": "수면제는 단기만 드세요.", "vi": "Thuốc ngủ chỉ dùng ngắn hạn.", "situation": "informal"}
      ],
      ["불면증", "수면무호흡증", "수면다원검사"]),

    t("ngung-tho-khi-ngu", "수면무호흡증", "ngưng thở khi ngủ",
      "睡眠無呼吸症", "잘 수(睡) + 잘 면(眠) + 없을 무(無) + 부를 호(呼) + 마실 흡(吸) + 병 증(症)",
      "수면무호흡증",
      "수면 중 반복적으로 호흡이 멈추거나 얕아지는 질환으로, 폐쇄성(obstructive), 중추성(central), 혼합형으로 나뉩니다. 영어로는 'sleep apnea'라고 합니다. 통역 시 주의할 점은 단순 코골이(snoring)와 구분해야 하며, 치료하지 않으면 고혈압, 심혈관질환, 뇌졸중 위험이 증가한다는 점을 강조해야 합니다. 베트남어로는 'ngưng thở khi ngủ' 또는 'hội chứng ngưng thở khi ngủ'라고 하며, 지속기도양압(CPAP) 치료가 표준입니다. 체중 감량과 옆으로 자는 자세 교정도 중요합니다.",
      "Bệnh ngừng thở hoặc thở nông nhiều lần khi ngủ do đường thở bị tắc hoặc não không điều khiển hô hấp. Gây mệt mỏi, tăng huyết áp.",
      "sleep medicine",
      "한국에서는 비만과 고령화로 수면무호흡증 환자가 증가하고 있으며, CPAP 장비 건강보험 적용이 확대되고 있습니다. 베트남은 아직 인식과 진단률이 낮으며, '코골이는 잘 자는 것'이라는 오해가 있습니다. 통역 시 '코골이가 심하면 수면무호흡 가능성'을 설명하고 검사를 권유하는 것이 중요합니다.",
      [
        {"mistake": "Ngáy", "correction": "Ngưng thở khi ngủ (có thể kèm ngáy)", "explanation": "코골이는 증상, 무호흡은 질환"},
        {"mistake": "Thở không đều", "correction": "Ngưng thở nhiều lần khi ngủ", "explanation": "불규칙 호흡과 무호흡은 다름"},
        {"mistake": "Máy thở lúc ngủ", "correction": "Máy CPAP hỗ trợ thở khi ngủ", "explanation": "인공호흡기와 CPAP 구분"}
      ],
      [
        {"ko": "수면다원검사 결과 시간당 30회 무호흡이 관찰됩니다.", "vi": "Kết quả xét nghiệm cho thấy ngưng thở 30 lần/giờ.", "situation": "formal"},
        {"ko": "CPAP 기계 매일 밤 쓰셔야 해요.", "vi": "Phải dùng máy CPAP mỗi đêm.", "situation": "onsite"},
        {"ko": "살 빼시면 무호흡 좀 나아질 거예요.", "vi": "Giảm cân sẽ cải thiện tình trạng ngưng thở.", "situation": "informal"}
      ],
      ["CPAP", "코골이", "수면다원검사"]),

    t("nghi-ruou", "알코올 중독", "nghiện rượu",
      "alcoholism", null,
      "알코올 중독",
      "알코올에 대한 신체적, 정신적 의존이 형성되어 조절 능력을 상실한 상태로, 영어로는 'alcoholism' 또는 'alcohol use disorder'라고 합니다. 통역 시 주의할 점은 '중독'이라는 단어가 낙인을 찍을 수 있으므로 '알코올 사용 장애'로 순화하여 표현하고, 치료 가능한 질병임을 강조해야 합니다. 베트남어로는 'nghiện rượu' 또는 'lạm dụng rượu'라고 하며, 금단증상(withdrawal syndrome)과 섬망(delirium tremens)에 대한 설명도 필요합니다. 해독(detoxification) 과정과 재활 프로그램에 대한 정보 제공도 중요합니다.",
      "Tình trạng phụ thuộc thể chất và tinh thần vào rượu, mất khả năng kiểm soát. Là bệnh có thể điều trị được.",
      "addiction medicine",
      "한국은 음주 문화가 강하여 알코올 중독률이 높으며, 직장과 가정 문제로 이어지는 경우가 많습니다. 베트남도 남성 음주율이 높으나, '중독=의지 박약'으로 보는 시각이 강해 치료를 꺼립니다. 통역 시 '뇌의 질환'이며 전문적 치료가 필요함을 강조하는 것이 중요합니다.",
      [
        {"mistake": "Hay uống rượu", "correction": "Nghiện rượu/Rối loạn sử dụng rượu", "explanation": "사회적 음주와 중독 구분"},
        {"mistake": "Không cai được", "correction": "Cần điều trị cai nghiện chuyên khoa", "explanation": "의지 문제가 아닌 질병으로 접근"},
        {"mistake": "Say rượu", "correction": "Triệu chứng nghiện rượu/cai rượu", "explanation": "급성 취함과 만성 중독 구분"}
      ],
      [
        {"ko": "알코올 의존 진단으로 해독 치료가 필요합니다.", "vi": "Được chẩn đoán nghiện rượu, cần điều trị cai nghiện.", "situation": "formal"},
        {"ko": "술 끊으면 손 떨리고 환각 올 수 있어요.", "vi": "Khi cai rượu có thể run tay và ảo giác.", "situation": "onsite"},
        {"ko": "재활 프로그램 참여하셔야 합니다.", "vi": "Cần tham gia chương trình phục hồi.", "situation": "informal"}
      ],
      ["금단증상", "섬망", "재활치료"]),

    t("ngoi-doc", "중독", "ngộ độc",
      "中毒", "가운데 중(中) + 독 독(毒)",
      "중독",
      "유해 물질이 체내에 들어와 생리 기능을 방해하는 상태로, 급성 중독과 만성 중독으로 나뉩니다. 영어로는 'poisoning' 또는 'intoxication'이라고 합니다. 통역 시 주의할 점은 중독 물질(약물, 식품, 화학물질 등)을 신속히 파악하고 전달하는 것이 해독제(antidote) 투여와 치료 방향 결정에 중요하다는 것입니다. 베트남어로는 'ngộ độc'이 일반적이며, 'ngộ độc thực phẩm'(식중독), 'ngộ độc thuốc'(약물 중독) 등으로 세분화됩니다. 119에 신고 시 중독 물질명과 섭취 시간, 양을 정확히 전달해야 합니다.",
      "Tình trạng chất độc xâm nhập cơ thể gây rối loạn chức năng. Có thể do thuốc, thực phẩm, hóa chất...",
      "toxicology",
      "한국은 농약 중독(특히 파라콰트)과 약물 과다복용이 많으며, 응급실에 중독센터 핫라인이 연결되어 있습니다. 베트남은 식중독과 메탄올 중독이 흔합니다. 통역 시 중독 물질에 따라 대처법이 완전히 다르므로(구토 유발 금기 물질 등), 정확한 물질명 확인이 생명과 직결됩니다.",
      [
        {"mistake": "Bị nhiễm độc", "correction": "Ngộ độc cấp tính", "explanation": "'nhiễm'은 감염 느낌, 'ngộ'가 중독"},
        {"mistake": "Ăn nhầm", "correction": "Ngộ độc do ăn phải [물질명]", "explanation": "물질명 명시 필수"},
        {"mistake": "Nôn ra là khỏi", "correction": "Không tự gây nôn, cần đánh giá y tế", "explanation": "일부 중독은 구토 유발 금기"}
      ],
      [
        {"ko": "파라콰트 음독으로 응급 투석이 필요합니다.", "vi": "Uống nhầm paraquat, cần lọc máu khẩn cấp.", "situation": "formal"},
        {"ko": "뭘 먹었는지 정확히 말씀해 주세요!", "vi": "Vui lòng cho biết chính xác đã ăn/uống gì!", "situation": "onsite"},
        {"ko": "위세척 하고 활성탄 투여할게요.", "vi": "Sẽ rửa dạ dày và cho than hoạt tính.", "situation": "informal"}
      ],
      ["해독제", "위세척", "활성탄"]),

    t("thuoc-giai-doc", "해독제", "thuốc giải độc",
      "解毒劑", "풀 해(解) + 독 독(毒) + 약 제(劑)",
      "해독제",
      "특정 독성 물질의 작용을 중화하거나 제거하는 약물로, 영어로는 'antidote'라고 합니다. 통역 시 주의할 점은 해독제가 모든 중독에 존재하는 것이 아니며, 특정 물질에만 효과가 있다는 점을 설명해야 합니다. 베트남어로는 'thuốc giải độc' 또는 'thuốc kháng độc'이라고 하며, N-아세틸시스테인(acetaminophen 중독), 날록손(opioid 중독), 아트로핀(유기인계 중독) 등 대표적 해독제와 적응증을 숙지해야 합니다. 골든타임 내 투여가 중요하므로 신속한 통역이 필요합니다.",
      "Thuốc trung hòa hoặc loại bỏ tác dụng của chất độc cụ thể. Chỉ hiệu quả với một số chất độc nhất định.",
      "toxicology",
      "한국 응급실에는 주요 해독제가 비치되어 있으며, 중독센터에서 전문가 자문을 받을 수 있습니다. 베트남은 해독제 수급이 원활하지 않은 경우가 있어, 특수 해독제는 대형병원으로 이송해야 할 수 있습니다. 통역 시 해독제 유무와 이송 필요성을 명확히 전달해야 합니다.",
      [
        {"mistake": "Thuốc trị độc", "correction": "Thuốc giải độc (antidote)", "explanation": "'치료'가 아닌 '해독' 개념"},
        {"mistake": "Thuốc chữa hết độc", "correction": "Thuốc giải độc cho [특정 물질]", "explanation": "만능 해독제는 없음, 특정 물질용임을 명시"},
        {"mistake": "Uống thuốc giải", "correction": "Truyền thuốc giải độc tĩnh mạch", "explanation": "투여 경로 정확히 전달"}
      ],
      [
        {"ko": "타이레놀 과다복용이라 N-아세틸시스테인을 투여합니다.", "vi": "Do uống quá liều paracetamol nên truyền N-acetylcysteine.", "situation": "formal"},
        {"ko": "해독제 있는데 빨리 써야 해요.", "vi": "Có thuốc giải độc nhưng phải dùng ngay.", "situation": "onsite"},
        {"ko": "이 독은 해독제가 없어서 대증치료만 가능합니다.", "vi": "Chất độc này không có thuốc giải, chỉ điều trị triệu chứng.", "situation": "informal"}
      ],
      ["중독", "응급처치", "골든타임"]),

    t("bong", "화상", "bỏng",
      "火傷", "불 화(火) + 다칠 상(傷)",
      "화상",
      "열, 화학물질, 전기, 방사선 등에 의해 피부나 조직이 손상된 상태로, 깊이에 따라 1도, 2도, 3도로 분류됩니다. 영어로는 'burn'이라고 합니다. 통역 시 주의할 점은 화상 면적(체표면적의 몇 %)과 깊이를 정확히 전달해야 하며, '9의 법칙(rule of nines)'으로 면적을 계산한다는 점을 알아야 합니다. 베트남어로는 'bỏng'이며, 'bỏng độ 1/2/3'으로 깊이를 표현합니다. 화상 응급처치(찬물로 식히기, 물집 터뜨리지 않기)와 감염 예방, 수액 치료의 중요성도 함께 설명해야 합니다.",
      "Tổn thương da và mô do nhiệt, hóa chất, điện, hoặc bức xạ. Phân loại theo độ sâu (độ 1, 2, 3).",
      "wound care",
      "한국의 화상전문센터는 중증 화상 치료에 특화되어 있으며, 한랭요법, 피부이식 등 최신 치료를 제공합니다. 베트남은 화상 치료 시설이 제한적이며, 민간요법(치약, 간장 바르기 등)으로 인한 2차 감염이 문제입니다. 통역 시 잘못된 민간요법을 경고하는 것이 중요합니다.",
      [
        {"mistake": "Phỏng", "correction": "Bỏng (phỏng은 경미한 데임)", "explanation": "심각도 구분"},
        {"mistake": "Bỏng nặng", "correction": "Bỏng độ 3, diện tích X%", "explanation": "깊이와 면적 구체적 명시"},
        {"mistake": "Tra kem", "correction": "Rửa nước mát 10-20 phút, không tra gì", "explanation": "응급처치 시 이물질 금지"}
      ],
      [
        {"ko": "체표면적 30% 2도 화상으로 수액 치료가 필요합니다.", "vi": "Bỏng độ 2 diện tích 30% cơ thể, cần truyền dịch.", "situation": "formal"},
        {"ko": "물집 절대 터뜨리지 마세요!", "vi": "Tuyệt đối không được chọc vỡ mụn nước!", "situation": "onsite"},
        {"ko": "피부이식 수술 들어갈 거예요.", "vi": "Sẽ phẫu thuật ghép da.", "situation": "informal"}
      ],
      ["피부이식", "체표면적", "수액치료"]),

    t("cat-lot-mo-chet", "괴사조직제거술", "cắt lột mô chết",
      "壞死組織除去術", "무너질 괴(壞) + 죽을 사(死) + 짤 조(組) + 베 직(織) + 덜 제(除) + 갈 거(去) + 기술 술(術)",
      "괴사조직제거술",
      "상처나 화상 부위의 죽은 조직을 외과적으로 제거하여 치유를 촉진하는 시술로, 영어로는 'debridement'라고 합니다. 통역 시 주의할 점은 '살을 도려낸다'는 표현에 보호자가 공포를 느낄 수 있으므로, '죽은 조직을 제거하여 새 살이 돋도록 돕는 치료'라고 설명해야 합니다. 베트남어로는 'cắt lột mô hoại tử' 또는 'làm sạch vết thương'이라고 하며, 수술적(surgical), 기계적(mechanical), 화학적(chemical) 방법이 있습니다. 통증이 있을 수 있으므로 진통제나 마취 사용 여부도 함께 설명해야 합니다.",
      "Kỹ thuật loại bỏ mô hoại tử ở vết thương/bỏng để thúc đẩy lành vết thương. Có thể gây đau.",
      "wound care",
      "한국에서는 당뇨발(diabetic foot)이나 욕창(pressure ulcer) 치료 시 정기적으로 시행하며, 외래에서도 가능합니다. 베트남은 당뇨 합병증 관리가 미흡하여 괴사가 진행된 후 내원하는 경우가 많습니다. 통역 시 조기 치료의 중요성을 강조하는 것이 좋습니다.",
      [
        {"mistake": "Cắt thịt", "correction": "Cắt lột mô hoại tử (debridement)", "explanation": "'살 자르기'보다 의학 용어 사용"},
        {"mistake": "Mổ vết thương", "correction": "Làm sạch vết thương bằng cách cắt lột mô chết", "explanation": "'수술'보다 '상처 관리' 뉘앙스"},
        {"mistake": "Sẽ rất đau", "correction": "Có thể hơi đau, sẽ dùng thuốc giảm đau", "explanation": "공포 유발 방지, 대책 함께 설명"}
      ],
      [
        {"ko": "당뇨발 괴사 부위를 제거하는 디브리망이 필요합니다.", "vi": "Cần cắt lột mô hoại tử ở bàn chân do tiểu đường.", "situation": "formal"},
        {"ko": "오늘 드레싱하면서 죽은 살 좀 떼어낼게요.", "vi": "Hôm nay sẽ thay băng và lấy bớt mô chết.", "situation": "onsite"},
        {"ko": "이거 안 하면 감염 번져요.", "vi": "Không làm thì nhiễm trùng lan rộng.", "situation": "informal"}
      ],
      ["상처관리", "당뇨발", "욕창"]),

    t("ghep-da", "피부이식", "ghép da",
      "皮膚移植", "가죽 피(皮) + 살갗 부(膚) + 옮길 이(移) + 심을 식(植)",
      "피부이식",
      "넓은 화상이나 외상으로 손상된 부위에 자가 피부나 인공 피부를 이식하는 수술로, 영어로는 'skin graft'라고 합니다. 통역 시 주의할 점은 자가이식(autograft, 본인 피부), 동종이식(allograft, 타인 피부), 이종이식(xenograft, 돼지 피부 등)을 구분해야 하며, 공여부(donor site)와 수여부(recipient site)의 관리가 모두 중요함을 설명해야 합니다. 베트남어로는 'ghép da'이며, 'lấy da từ [부위]'로 공여부를 설명합니다. 부분층 이식(split-thickness)과 전층 이식(full-thickness)의 차이도 이해해야 합니다.",
      "Phẫu thuật lấy da từ vùng khỏe mạnh (hoặc da nhân tạo) để đắp lên vùng da bị tổn thương.",
      "wound care",
      "한국은 화상전문센터에서 광범위 화상에 배양피부(cultured skin)까지 사용 가능합니다. 베트남은 자가 피부이식이 주류이며, 인공피부는 비용 문제로 사용이 제한적입니다. 통역 시 이식 옵션과 비용, 회복 기간을 명확히 설명해야 합니다.",
      [
        {"mistake": "Dán da", "correction": "Ghép da (skin graft)", "explanation": "'붙이기'보다 '이식' 개념"},
        {"mistake": "Lấy da người khác", "correction": "Ghép da tự thân (lấy da chính mình)", "explanation": "자가이식이 기본임을 명시"},
        {"mistake": "Mổ da", "correction": "Phẫu thuật ghép da", "explanation": "명확한 수술명"}
      ],
      [
        {"ko": "허벅지에서 피부를 채취해 화상 부위에 이식할 예정입니다.", "vi": "Sẽ lấy da từ đùi để ghép lên vùng bỏng.", "situation": "formal"},
        {"ko": "스킨그라프트 수술 2시간 걸립니다.", "vi": "Phẫu thuật ghép da mất 2 giờ.", "situation": "onsite"},
        {"ko": "공여부도 상처니까 관리 잘 하셔야 해요.", "vi": "Vùng lấy da cũng là vết thương, phải chăm sóc cẩn thận.", "situation": "informal"}
      ],
      ["화상", "자가이식", "공여부"]),

    t("thu-nghiem-lam-sang", "임상시험", "thử nghiệm lâm sàng",
      "臨床試驗", "임할 임(臨) + 자리 상(床) + 시험할 시(試) + 시험할 험(驗)",
      "임상시험",
      "새로운 약물이나 치료법의 안전성과 유효성을 평가하기 위해 사람을 대상으로 수행하는 연구로, 1상, 2상, 3상, 4상으로 나뉩니다. 영어로는 'clinical trial'이라고 합니다. 통역 시 주의할 점은 임상시험 참여는 자발적이며 언제든 중단할 수 있다는 점, 위약(placebo) 그룹이 있을 수 있다는 점, 모든 위험과 이익을 충분히 설명받아야 한다는 점을 명확히 해야 합니다. 베트남어로는 'thử nghiệm lâm sàng'이며, 동의서(informed consent) 과정이 매우 중요합니다. '인체 실험'이라는 부정적 인식을 바로잡는 것도 통역사의 역할입니다.",
      "Nghiên cứu trên người để đánh giá an toàn và hiệu quả của thuốc/liệu pháp mới. Chia giai đoạn 1, 2, 3, 4.",
      "clinical trials",
      "한국은 임상시험 윤리 기준이 엄격하며, IRB(기관생명윤리위원회) 승인이 필수입니다. 베트남도 유사한 시스템이 있으나, '가난한 사람들 대상 실험'이라는 부정적 인식이 남아있습니다. 통역 시 윤리 기준과 참여자 보호 장치를 강조하는 것이 중요합니다.",
      [
        {"mistake": "Thí nghiệm trên người", "correction": "Thử nghiệm lâm sàng (clinical trial)", "explanation": "'실험'보다 '임상시험' 용어 사용"},
        {"mistake": "Làm chuột bạch", "correction": "Tham gia nghiên cứu lâm sàng", "explanation": "부정적 표현 금지"},
        {"mistake": "Chắc chắn có hiệu quả", "correction": "Đang nghiên cứu hiệu quả, chưa có kết luận", "explanation": "효과 보장 금지"}
      ],
      [
        {"ko": "이 항암제 3상 임상시험에 참여하시겠습니까?", "vi": "Anh/chị có muốn tham gia thử nghiệm lâm sàng giai đoạn 3 thuốc chống ung thư này không?", "situation": "formal"},
        {"ko": "위약 그룹에 배정될 수도 있습니다.", "vi": "Có thể được phân vào nhóm dùng giả dược.", "situation": "onsite"},
        {"ko": "언제든 중단하실 수 있어요.", "vi": "Có thể ngừng tham gia bất cứ lúc nào.", "situation": "informal"}
      ],
      ["임상시험동의서", "위약", "IRB"]),

    t("diem-cuoi-chinh", "1차 평가변수", "điểm cuối chính",
      "一次評價變數", "한 일(一) + 차례 차(次) + 평가할 평(評) + 값 가(價) + 변할 변(變) + 셈 수(數)",
      "일차 평가변수",
      "임상시험에서 치료 효과를 판정하기 위한 주요 결과 지표로, 영어로는 'primary endpoint'라고 합니다. 통역 시 주의할 점은 이것이 임상시험의 성패를 결정하는 핵심 지표이며, 2차 평가변수(secondary endpoint)와 구분된다는 점을 설명해야 합니다. 베트남어로는 'điểm cuối chính' 또는 'chỉ tiêu chính'이라고 하며, 생존율(survival rate), 재발률(recurrence rate), 증상 개선도 등 구체적 지표를 명확히 전달해야 합니다. 통계적 유의성(statistical significance)에 대한 기본 이해도 필요합니다.",
      "Chỉ tiêu kết quả chính để đánh giá hiệu quả điều trị trong thử nghiệm lâm sàng. Quyết định thành công của nghiên cứu.",
      "clinical trials",
      "한국은 글로벌 임상시험에 많이 참여하여 primary endpoint 개념이 익숙하지만, 베트남은 상대적으로 생소할 수 있습니다. 통역 시 '이 연구의 가장 중요한 목표'라고 풀어 설명하면 이해가 쉽습니다.",
      [
        {"mistake": "Kết quả chính", "correction": "Điểm cuối chính (primary endpoint)", "explanation": "임상시험 전문 용어 사용"},
        {"mistake": "Mục tiêu đầu tiên", "correction": "Chỉ tiêu đánh giá chính", "explanation": "'목표'가 아닌 '평가지표'"},
        {"mistake": "Điểm số", "correction": "Điểm cuối (endpoint)", "explanation": "'점수'가 아닌 '결과 시점'"}
      ],
      [
        {"ko": "이 연구의 1차 평가변수는 3년 무병생존율입니다.", "vi": "Điểm cuối chính của nghiên cứu này là tỷ lệ sống không bệnh 3 năm.", "situation": "formal"},
        {"ko": "Primary endpoint 달성하면 신약 승인 가능성 높아요.", "vi": "Nếu đạt được điểm cuối chính thì khả năng phê duyệt thuốc mới cao.", "situation": "onsite"},
        {"ko": "2차 평가변수는 부작용 발생률입니다.", "vi": "Điểm cuối thứ cấp là tỷ lệ tác dụng phụ.", "situation": "informal"}
      ],
      ["임상시험", "통계적유의성", "생존율"]),

    t("dong-y-sau-hieu", "사전동의", "đồng ý sau hiểu",
      "事前同意", "일 사(事) + 앞 전(前) + 한가지 동(同) + 뜻 의(意)",
      "사전동의",
      "의료 행위나 연구 참여 전에 충분한 정보를 제공받고 자발적으로 동의하는 것으로, 영어로는 'informed consent'라고 합니다. 통역 시 주의할 점은 단순히 서명하는 것이 아니라, 위험과 이익, 대안, 거부 권리를 모두 이해한 후 자유 의사로 결정하는 것임을 강조해야 합니다. 베트남어로는 'đồng ý sau khi được giải thích' 또는 'chấp thuận có hiểu biết'라고 하며, 동의 철회 권리도 함께 설명해야 합니다. 의료 통역에서 가장 윤리적으로 민감한 부분 중 하나로, 환자가 진정으로 이해했는지 확인하는 것이 중요합니다.",
      "Đồng ý tự nguyện sau khi được cung cấp đầy đủ thông tin về rủi ro, lợi ích, phương án thay thế. Là quyền cơ bản của bệnh nhân.",
      "bioethics",
      "한국은 의료법과 생명윤리법에서 사전동의를 엄격히 규정하고 있으며, 동의서 양식도 표준화되어 있습니다. 베트남도 법적으로 요구하지만, 실제로는 형식적인 서명에 그치는 경우가 많습니다. 통역 시 환자가 압박감 없이 질문하고 결정할 시간을 충분히 갖도록 도와야 합니다.",
      [
        {"mistake": "Ký đồng ý", "correction": "Đồng ý sau khi hiểu rõ (informed consent)", "explanation": "서명 행위가 아닌 이해 과정 강조"},
        {"mistake": "Bắt buộc phải đồng ý", "correction": "Có quyền từ chối, đồng ý là tự nguyện", "explanation": "자발성 강조"},
        {"mistake": "Đọc rồi ký", "correction": "Giải thích đầy đủ, hỏi đáp, sau đó quyết định", "explanation": "과정의 중요성"}
      ],
      [
        {"ko": "수술 전 충분한 설명을 드린 후 사전동의서를 받겠습니다.", "vi": "Trước phẫu thuật sẽ giải thích đầy đủ rồi nhận đồng ý có hiểu biết.", "situation": "formal"},
        {"ko": "이해 안 되시는 부분 있으면 언제든 물어보세요.", "vi": "Có gì không hiểu cứ hỏi bất cứ lúc nào.", "situation": "onsite"},
        {"ko": "동의 안 하셔도 불이익 없습니다.", "vi": "Không đồng ý cũng không bị bất lợi gì.", "situation": "informal"}
      ],
      ["의료윤리", "환자권리", "임상시험"]),

    t("khong-cap-cuu", "연명치료거부", "không cấp cứu",
      null, null,
      "연명치료거부",
      "회복 불가능한 말기 상태에서 심폐소생술 등 연명치료를 시행하지 않기로 미리 결정하는 것으로, 영어로는 'DNR(Do Not Resuscitate)' 또는 'AND(Allow Natural Death)'라고 합니다. 통역 시 주의할 점은 이것이 '치료 포기'가 아니라 '무의미한 연명 중단'이며, 환자의 존엄성을 존중하는 선택임을 강조해야 합니다. 베트남어로는 'không hồi sức' 또는 'cho phép tử vong tự nhiên'이라고 하며, 가족의 정서적 부담이 크므로 매우 신중하고 공감적인 통역이 필요합니다. 사전연명의료의향서(advance directive)와 연명의료계획서의 차이도 이해해야 합니다.",
      "Quyết định trước không thực hiện hồi sức tim phổi khi bệnh giai đoạn cuối không thể hồi phục. Tôn trọng phẩm giá người bệnh.",
      "bioethics",
      "한국은 '연명의료결정법'으로 제도화되어 있으며, 환자 본인의 의사가 최우선입니다. 베트남은 법적 제도가 미비하고, 가족 중심 의사결정 문화가 강해 환자 본인보다 가족이 결정하는 경우가 많습니다. 통역 시 한국 법의 취지(환자 자기결정권)를 설명하되, 문화적 차이를 존중하는 태도가 필요합니다.",
      [
        {"mistake": "Bỏ mặc cho chết", "correction": "Cho phép tử vong tự nhiên, không kéo dài vô ích", "explanation": "'방치'가 아닌 '존엄한 죽음' 개념"},
        {"mistake": "Không điều trị nữa", "correction": "Không hồi sức tim phổi, vẫn điều trị giảm đau", "explanation": "완화의료는 계속됨을 명시"},
        {"mistake": "Gia đình quyết định", "correction": "Tôn trọng ý nguyện của bệnh nhân", "explanation": "환자 의사 우선 강조"}
      ],
      [
        {"ko": "환자분이 사전에 DNR 의사를 밝히셨습니다.", "vi": "Bệnh nhân đã bày tỏ nguyện vọng không hồi sức trước đó.", "situation": "formal"},
        {"ko": "심정지 와도 CPR 안 하는 거 맞으시죠?", "vi": "Nếu ngừng tim thì không làm CPR, đúng không?", "situation": "onsite"},
        {"ko": "편안하게 보내드리는 게 맞다고 생각됩니다.", "vi": "Tôi nghĩ nên để người bệnh ra đi một cách an lành.", "situation": "informal"}
      ],
      ["연명의료", "사전연명의료의향서", "완화의료"]),

    t("chi-thi-truoc", "사전의료지시서", "chỉ thị trước",
      "事前醫療指示書", "일 사(事) + 앞 전(前) + 의원 의(醫) + 치료할 료(療) + 가리킬 지(指) + 보일 시(示) + 글 서(書)",
      "사전의료지시서",
      "의사결정능력이 있을 때 미리 작성하여 향후 의식 없을 때를 대비해 치료 방침을 지시하는 문서로, 영어로는 'advance directive' 또는 'living will'이라고 합니다. 통역 시 주의할 점은 이것이 법적 효력이 있는 문서이며, 건강할 때 미리 작성하는 것이 중요하다는 점을 설명해야 합니다. 베트남어로는 'chỉ thị y tế trước' 또는 'di chúc sinh tiền'이라고 하며, DNR뿐 아니라 장기기증, 의료대리인 지정 등도 포함될 수 있습니다. 문화적으로 '죽음을 준비한다'는 것에 대한 거부감이 있을 수 있으므로, '미래를 위한 현명한 준비'라는 긍정적 프레임을 사용하는 것이 좋습니다.",
      "Văn bản pháp lý ghi rõ nguyện vọng điều trị khi không còn khả năng quyết định. Bao gồm DNR, hiến tạng, đại diện y tế...",
      "bioethics",
      "한국은 연명의료결정법으로 사전연명의료의향서 등록 시스템이 있으며, 의료기관과 보건소에서 작성 가능합니다. 베트남은 이런 제도가 없어, 한국에서 치료받는 베트남 환자에게 생소한 개념입니다. 통역 시 제도의 취지와 작성 방법을 친절히 안내해야 합니다.",
      [
        {"mistake": "Di chúc", "correction": "Chỉ thị y tế trước (advance directive)", "explanation": "재산 유언과 의료 지시 구분"},
        {"mistake": "Giấy từ chối điều trị", "correction": "Văn bản nguyện vọng điều trị trước", "explanation": "'거부'가 아닌 '희망 치료' 명시"},
        {"mistake": "Chỉ người già mới viết", "correction": "Người trưởng thành nên chuẩn bị sớm", "explanation": "나이 제한 없음, 조기 준비 권장"}
      ],
      [
        {"ko": "건강하실 때 미리 사전의료지시서를 작성해 두시는 것을 권합니다.", "vi": "Khuyến khích viết chỉ thị y tế trước khi còn khỏe mạnh.", "situation": "formal"},
        {"ko": "리빙윌에 장기기증 의사도 포함할 수 있어요.", "vi": "Trong chỉ thị y tế có thể ghi nguyện vọng hiến tạng.", "situation": "onsite"},
        {"ko": "언제든 내용 변경 가능합니다.", "vi": "Có thể thay đổi nội dung bất cứ lúc nào.", "situation": "informal"}
      ],
      ["연명의료", "DNR", "의료대리인"]),

    t("kham-benh-tu-xa", "원격진료", "khám bệnh từ xa",
      "遠隔診療", "멀 원(遠) + 사이 격(隔) + 진찰할 진(診) + 치료할 료(療)",
      "원격진료",
      "정보통신기술을 이용하여 원격지에 있는 환자를 진찰하고 상담하는 의료 서비스로, 영어로는 'telemedicine' 또는 'telehealth'라고 합니다. 통역 시 주의할 점은 원격진료의 법적 허용 범위가 국가마다 다르며, 한국은 코로나19 이후 한시적으로 허용되었다가 논란 중이라는 점을 이해해야 합니다. 베트남어로는 'khám bệnh từ xa' 또는 'y tế từ xa'라고 하며, 화상진료, 원격모니터링, 원격처방 등 다양한 형태가 있습니다. 기술적 문제(인터넷 불안정, 화질 저하)로 인한 의사소통 장애도 통역 시 고려해야 합니다.",
      "Dịch vụ y tế từ xa qua công nghệ thông tin, bao gồm tư vấn video, theo dõi từ xa, kê đơn trực tuyến.",
      "telemedicine",
      "한국은 도서산간 지역과 만성질환 관리에 원격진료가 시범 운영 중이며, 기술 수준은 높으나 법적 제도가 미비합니다. 베트남은 지리적으로 원격진료 수요가 높으나 인프라가 부족합니다. 통역 시 기술적 한계(직접 진찰 불가능)와 법적 제약을 설명하는 것이 중요합니다.",
      [
        {"mistake": "Khám qua điện thoại", "correction": "Khám bệnh từ xa qua video (telemedicine)", "explanation": "음성 통화와 화상진료 구분"},
        {"mistake": "Khám online", "correction": "Tư vấn y tế từ xa (có giới hạn)", "explanation": "'온라인 쇼핑'과 혼동 방지, 한계 명시"},
        {"mistake": "Bác sĩ ở nước ngoài khám", "correction": "Tư vấn từ xa với bác sĩ tại [위치]", "explanation": "의사 면허 관할권 명시"}
      ],
      [
        {"ko": "만성질환 모니터링은 원격진료로 가능합니다.", "vi": "Theo dõi bệnh mãn tính có thể qua khám bệnh từ xa.", "situation": "formal"},
        {"ko": "화상으로 상담하고 처방전 보내드릴게요.", "vi": "Sẽ tư vấn qua video và gửi đơn thuốc.", "situation": "onsite"},
        {"ko": "직접 진찰이 필요하면 내원하셔야 해요.", "vi": "Nếu cần khám trực tiếp thì phải đến bệnh viện.", "situation": "informal"}
      ],
      ["화상진료", "원격처방", "디지털헬스"]),

    t("theo-doi-suc-khoe-tu-xa", "원격모니터링", "theo dõi sức khỏe từ xa",
      "遠隔監視", "멀 원(遠) + 사이 격(隔) + 볼 감(監) + 볼 시(視)",
      "원격모니터링",
      "착용형 기기나 센서를 통해 환자의 생체 데이터를 원격으로 수집하고 모니터링하는 시스템으로, 영어로는 'remote patient monitoring'이라고 합니다. 통역 시 주의할 점은 혈압, 혈당, 심전도 등 측정 데이터가 자동으로 의료진에게 전송되며, 이상 시 알람이 온다는 점을 설명해야 합니다. 베트남어로는 'theo dõi bệnh nhân từ xa' 또는 'giám sát sức khỏe từ xa'라고 하며, 웨어러블 기기, 스마트폰 앱 등 다양한 도구가 사용됩니다. 개인정보 보호와 데이터 보안에 대한 우려도 함께 설명해야 합니다.",
      "Hệ thống thu thập dữ liệu sinh học từ xa qua thiết bị đeo, gửi về bác sĩ. Dùng cho quản lý bệnh mãn tính.",
      "telemedicine",
      "한국은 만성질환자와 퇴원 후 환자 관리에 원격모니터링이 확대되고 있으며, 건강보험 수가 적용도 논의 중입니다. 베트남은 기기 보급이 제한적이며, 대도시 중심으로 시작 단계입니다. 통역 시 기기 사용법과 데이터 전송 방식을 쉽게 설명하는 것이 중요합니다.",
      [
        {"mistake": "Máy đo gửi kết quả", "correction": "Hệ thống theo dõi từ xa tự động gửi dữ liệu cho bác sĩ", "explanation": "시스템 전체 설명"},
        {"mistake": "Bác sĩ nhìn mình", "correction": "Bác sĩ nhận dữ liệu sức khỏe (không có camera)", "explanation": "영상 감시와 구분"},
        {"mistake": "App điện thoại", "correction": "Ứng dụng y tế kết nối thiết bị giám sát", "explanation": "의료 목적 명시"}
      ],
      [
        {"ko": "스마트 혈압계로 측정하면 자동으로 저희에게 전송됩니다.", "vi": "Đo bằng máy đo huyết áp thông minh sẽ tự động gửi cho chúng tôi.", "situation": "formal"},
        {"ko": "혈당 200 넘으면 앱에서 경고 뜰 거예요.", "vi": "Nếu đường huyết trên 200 thì app sẽ cảnh báo.", "situation": "onsite"},
        {"ko": "매일 측정하고 주 1회 확인해 드릴게요.", "vi": "Đo hàng ngày, tuần 1 lần chúng tôi kiểm tra.", "situation": "informal"}
      ],
      ["웨어러블", "디지털헬스", "만성질환관리"]),

    t("ung-dung-suc-khoe", "헬스케어 앱", "ứng dụng sức khỏe",
      null, null,
      "헬스케어 앱",
      "건강 관리, 질병 예방, 의료 정보 제공을 위한 스마트폰 애플리케이션으로, 영어로는 'health app' 또는 'mHealth app'이라고 합니다. 통역 시 주의할 점은 의료기기로 허가받은 앱과 일반 건강관리 앱을 구분해야 하며, 앱의 정보가 의사 진료를 대체할 수 없음을 명확히 해야 합니다. 베트남어로는 'ứng dụng chăm sóc sức khỏe' 또는 'app y tế'라고 하며, 복약 알림, 증상 체크, 건강 기록 등 다양한 기능이 있습니다. 개인정보 수집 동의와 보안에 대한 안내도 필요합니다.",
      "Ứng dụng di động quản lý sức khỏe, ghi nhận triệu chứng, nhắc uống thuốc. Không thay thế khám bác sĩ.",
      "digital health",
      "한국은 다양한 헬스케어 앱이 개발되어 있으며, 일부는 의료기기로 허가받아 보험 적용도 받습니다. 베트남은 앱 사용이 증가 중이나, '의사 대신 앱'으로 오해하는 경우가 있습니다. 통역 시 앱의 한계(진단 불가)를 명확히 하는 것이 중요합니다.",
      [
        {"mistake": "App thay bác sĩ", "correction": "App hỗ trợ, không thay thế bác sĩ", "explanation": "의사 진료 대체 불가 강조"},
        {"mistake": "Tự chẩn đoán qua app", "correction": "App ghi nhận triệu chứng, bác sĩ chẩn đoán", "explanation": "진단 권한은 의사에게만"},
        {"mistake": "App miễn phí", "correction": "Một số app miễn phí, một số có phí", "explanation": "비용 정보 정확히"}
      ],
      [
        {"ko": "이 앱으로 혈압, 혈당 기록하고 저희와 공유해 주세요.", "vi": "Ghi huyết áp, đường huyết vào app này và chia sẻ với chúng tôi.", "situation": "formal"},
        {"ko": "복약 알람 설정해 드릴게요.", "vi": "Sẽ cài đặt nhắc nhở uống thuốc.", "situation": "onsite"},
        {"ko": "증상 이상하면 앱만 보지 말고 바로 연락하세요.", "vi": "Nếu triệu chứng lạ đừng chỉ xem app, liên hệ ngay.", "situation": "informal"}
      ],
      ["디지털헬스", "원격진료", "모바일헬스"]),

    t("tri-tue-nhan-tao-y-te", "의료 인공지능", "trí tuệ nhân tạo y tế",
      "醫療人工知能", "의원 의(醫) + 치료할 료(療) + 사람 인(人) + 장인 공(工) + 알 지(知) + 능할 능(能)",
      "의료 인공지능",
      "인공지능 기술을 의료 진단, 치료 계획, 신약 개발 등에 적용하는 것으로, 영어로는 'medical AI' 또는 'AI in healthcare'라고 합니다. 통역 시 주의할 점은 AI가 의사를 대체하는 것이 아니라 보조 도구이며, 최종 판단은 의사가 한다는 점을 강조해야 합니다. 베트남어로는 'trí tuệ nhân tạo trong y tế' 또는 'AI y khoa'라고 하며, 영상 판독(image analysis), 질병 예측(disease prediction), 약물 추천(drug recommendation) 등 다양한 분야에 사용됩니다. AI의 한계와 오류 가능성도 함께 설명해야 합니다.",
      "Ứng dụng AI trong chẩn đoán hình ảnh, dự đoán bệnh, đề xuất thuốc. Hỗ trợ bác sĩ, không thay thế.",
      "digital health",
      "한국은 AI 기반 영상 판독 시스템이 상용화되어 있으며, 폐암, 유방암 검진에 활용됩니다. 베트남은 대형병원 중심으로 도입 시작 단계입니다. 통역 시 'AI가 분석했다'는 말에 환자가 불안해하거나 반대로 맹신하지 않도록 균형 잡힌 설명이 필요합니다.",
      [
        {"mistake": "Máy tính chẩn đoán", "correction": "AI hỗ trợ phân tích, bác sĩ chẩn đoán cuối cùng", "explanation": "AI 역할 명확화"},
        {"mistake": "AI không bao giờ sai", "correction": "AI rất chính xác nhưng vẫn cần bác sĩ kiểm tra", "explanation": "AI 한계 인식"},
        {"mistake": "Robot làm thay bác sĩ", "correction": "AI là công cụ hỗ trợ bác sĩ", "explanation": "대체가 아닌 보조"}
      ],
      [
        {"ko": "AI가 폐 CT를 분석한 결과 이상 소견이 있어 전문의가 정밀 판독합니다.", "vi": "AI phân tích CT phổi thấy bất thường, bác sĩ chuyên khoa sẽ đọc kỹ.", "situation": "formal"},
        {"ko": "인공지능이 암 위험도 70%로 예측했어요.", "vi": "AI dự đoán nguy cơ ung thư 70%.", "situation": "onsite"},
        {"ko": "AI 추천이지만 최종은 선생님이 결정하세요.", "vi": "AI đề xuất nhưng cuối cùng bác sĩ quyết định.", "situation": "informal"}
      ],
      ["영상판독", "질병예측", "디지털헬스"]),

    t("du-lieu-suc-khoe-ca-nhan", "개인 건강 데이터", "dữ liệu sức khỏe cá nhân",
      "個人健康data", "낱 개(個) + 사람 인(人) + 건강할 건(健) + 세울 강(康)",
      "개인 건강 데이터",
      "개인의 의료 기록, 생체 정보, 유전자 정보 등을 디지털 형태로 수집한 데이터로, 영어로는 'personal health data' 또는 'PHR(Personal Health Record)'이라고 합니다. 통역 시 주의할 점은 이 데이터가 민감한 개인정보이며, 보안과 프라이버시 보호가 매우 중요하다는 점을 강조해야 합니다. 베트남어로는 'dữ liệu sức khỏe cá nhân' 또는 'hồ sơ sức khỏe điện tử'라고 하며, 데이터 소유권, 활용 동의, 제3자 제공 범위 등을 명확히 설명해야 합니다. GDPR, 개인정보보호법 등 법적 보호 장치도 함께 안내하는 것이 좋습니다.",
      "Thông tin y tế cá nhân dạng số, bao gồm bệnh án, xét nghiệm, gen. Là dữ liệu nhạy cảm cần bảo mật.",
      "digital health",
      "한국은 마이헬스웨이 등 개인 건강기록 통합 플랫폼이 구축되어 있으며, 개인정보보호법으로 엄격히 보호됩니다. 베트남은 전자건강기록 시스템이 발전 중이나, 개인정보 인식이 낮아 유출 위험이 있습니다. 통역 시 데이터 보안의 중요성을 교육하는 것이 필요합니다.",
      [
        {"mistake": "Hồ sơ bệnh án", "correction": "Dữ liệu sức khỏe điện tử (bao gồm cả dữ liệu từ thiết bị)", "explanation": "종이 기록과 디지털 데이터 구분"},
        {"mistake": "Ai cũng xem được", "correction": "Chỉ người được ủy quyền mới truy cập", "explanation": "접근 권한 제한 명시"},
        {"mistake": "Dữ liệu của bệnh viện", "correction": "Dữ liệu của bạn, bạn có quyền sở hữu", "explanation": "개인 소유권 강조"}
      ],
      [
        {"ko": "개인 건강 데이터는 암호화되어 안전하게 보관됩니다.", "vi": "Dữ liệu sức khỏe cá nhân được mã hóa và bảo quản an toàn.", "situation": "formal"},
        {"ko": "연구 목적 데이터 활용은 별도 동의가 필요해요.", "vi": "Sử dụng dữ liệu cho nghiên cứu cần đồng ý riêng.", "situation": "onsite"},
        {"ko": "앱 삭제해도 데이터는 서버에 남아요.", "vi": "Xóa app nhưng dữ liệu vẫn ở server.", "situation": "informal"}
      ],
      ["개인정보보호", "전자건강기록", "데이터보안"]),

    t("y-hoc-chinh-xac", "정밀의료", "y học chính xác",
      "精密醫療", "정밀할 정(精) + 빽빽할 밀(密) + 의원 의(醫) + 치료할 료(療)",
      "정밀의료",
      "개인의 유전자, 환경, 생활습관을 분석하여 맞춤형 치료를 제공하는 의료 패러다임으로, 영어로는 'precision medicine' 또는 'personalized medicine'이라고 합니다. 통역 시 주의할 점은 '정밀'이 '세밀한 수술'을 의미하는 것이 아니라 '개인 맞춤형'을 의미한다는 점을 설명해야 합니다. 베트남어로는 'y học chính xác' 또는 'y học cá thể hóa'라고 하며, 유전자 검사(gene test), 표적치료(targeted therapy), 면역치료(immunotherapy) 등이 포함됩니다. 비용이 높을 수 있으므로 건강보험 적용 여부도 함께 안내해야 합니다.",
      "Y học dựa trên phân tích gen, môi trường, lối sống để điều trị cá nhân hóa. Bao gồm xét nghiệm gen, liệu pháp đích.",
      "digital health",
      "한국은 암 환자 대상 유전자 패널 검사가 건강보험 적용되며, 정밀의료 센터가 확대되고 있습니다. 베트남은 대형병원 중심으로 도입 시작 단계이며, 비용이 높아 접근성이 제한적입니다. 통역 시 정밀의료의 이점과 함께 비용 부담을 설명하는 것이 중요합니다.",
      [
        {"mistake": "Phẫu thuật chính xác", "correction": "Y học cá thể hóa (precision medicine)", "explanation": "수술 정밀도가 아닌 맞춤 치료"},
        {"mistake": "Xét nghiệm gen = chữa được", "correction": "Xét nghiệm gen giúp chọn thuốc phù hợp hơn", "explanation": "치료 보장 아닌 최적화"},
        {"mistake": "Chỉ người giàu mới được", "correction": "Một số xét nghiệm có bảo hiểm", "explanation": "보험 적용 가능성 안내"}
      ],
      [
        {"ko": "유전자 검사 결과에 따라 표적항암제를 선택합니다.", "vi": "Căn cứ kết quả xét nghiệm gen chọn thuốc ung thư đích.", "situation": "formal"},
        {"ko": "당신한테 맞는 약을 찾는 거예요.", "vi": "Tìm thuốc phù hợp với bạn.", "situation": "onsite"},
        {"ko": "정밀의료는 비용이 좀 높지만 효과가 더 좋을 수 있어요.", "vi": "Y học chính xác tốn kém hơn nhưng có thể hiệu quả hơn.", "situation": "informal"}
      ],
      ["유전자검사", "표적치료", "맞춤의료"])
]

file_path = os.path.join(os.path.dirname(__file__), '..', 'data', 'terms', 'medical.json')

# Read existing data
with open(file_path, 'r', encoding='utf-8') as f:
    data = json.load(f)

# Check for duplicates
existing_slugs = {term['slug'] for term in data}
new_terms = [term for term in terms if term['slug'] not in existing_slugs]

# Append new terms
data.extend(new_terms)

# Write back
with open(file_path, 'w', encoding='utf-8') as f:
    json.dump(data, f, ensure_ascii=False, indent=2)

print(f"Added {len(new_terms)} new terms (751-800). Total terms: {len(data)}")
if len(new_terms) < len(terms):
    print(f"Skipped {len(terms) - len(new_terms)} duplicate slugs.")
