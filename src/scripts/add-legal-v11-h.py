#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
형사소송 심화 - 증거법/공판절차 용어 추가 스크립트
Criminal Procedure Advanced - Evidence/Trial Terms
"""

import json
import os

# 스크립트의 절대 경로 기준으로 legal.json 경로 설정
SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
PROJECT_ROOT = os.path.dirname(os.path.dirname(SCRIPT_DIR))
LEGAL_JSON_PATH = os.path.join(PROJECT_ROOT, "src", "data", "terms", "legal.json")

# 추가할 용어 데이터 (형사소송 심화 - 증거법/공판절차)
new_terms = [
    {
        "slug": "chung-geo-neung-ryeok",
        "korean": "증거능력",
        "vietnamese": "Năng lực chứng cứ",
        "hanja": "證據能力",
        "hanjaReading": "證(증거 증) 據(근거 거) 能(능할 능) 力(힘 력)",
        "pronunciation": "증거능력",
        "meaningKo": "증거로서 법정에 제출되어 사실인정의 자료로 사용될 수 있는 자격을 말합니다. 위법수집증거배제법칙, 전문법칙 등에 위배되면 증거능력이 부정됩니다. 통역 시 '증거로 쓸 수 있는 자격'이라는 개념을 명확히 전달해야 하며, 증명력(증거가치)과 혼동하지 않도록 주의해야 합니다. 베트남어로는 '법적으로 인정되는 증거의 자격'이라는 맥락을 강조하여 설명하는 것이 효과적입니다.",
        "meaningVi": "Là tư cách của chứng cứ được đệ trình lên tòa án và có thể được sử dụng làm tài liệu để xác định sự thật. Nếu vi phạm nguyên tắc loại trừ chứng cứ thu thập bất hợp pháp hoặc nguyên tắc truyền văn thì năng lực chứng cứ sẽ bị phủ định. Đây là khái niệm quan trọng trong tố tụng hình sự Hàn Quốc.",
        "context": "형사소송절차",
        "culturalNote": "한국 형사소송법은 증거능력과 증명력을 엄격히 구분합니다. 증거능력은 증거가 법정에 제출될 자격이고, 증명력은 그 증거가 사실인정에 얼마나 기여하는지의 정도입니다. 베트남 형사소송법에서는 이 구분이 한국만큼 명확하지 않을 수 있어, 통역 시 개념의 차이를 설명하는 것이 중요합니다. 특히 위법수집증거배제법칙은 한국에서 매우 엄격하게 적용됩니다.",
        "commonMistakes": [
            {
                "mistake": "증거능력을 'giá trị chứng cứ'로 번역",
                "correction": "'năng lực chứng cứ'로 번역",
                "explanation": "giá trị chứng cứ는 증명력(證明力)에 해당하며, 증거능력과는 다른 개념입니다"
            },
            {
                "mistake": "증거능력과 증명력을 혼동",
                "correction": "증거능력은 자격, 증명력은 가치로 구분",
                "explanation": "증거능력은 법정 제출 자격이고, 증명력은 사실인정의 설득력입니다"
            },
            {
                "mistake": "위법수집증거를 단순히 '불법 증거'로만 설명",
                "correction": "'법 위반 절차로 수집된 증거로서 증거능력이 배제되는 증거'로 설명",
                "explanation": "위법수집증거배제법칙의 법리를 정확히 전달해야 합니다"
            }
        ],
        "examples": [
            {
                "ko": "이 진술조서는 적법한 절차를 거치지 않아 증거능력이 없습니다",
                "vi": "Biên bản khai báo này không có năng lực chứng cứ vì không trải qua thủ tục hợp pháp",
                "situation": "formal"
            },
            {
                "ko": "증거능력이 인정되더라도 증명력은 법관이 자유롭게 판단합니다",
                "vi": "Ngay cả khi năng lực chứng cứ được thừa nhận, thẩm phán sẽ tự do đánh giá sức thuyết phục của chứng cứ",
                "situation": "formal"
            },
            {
                "ko": "전문증거는 원칙적으로 증거능력이 제한됩니다",
                "vi": "Chứng cứ truyền văn về nguyên tắc bị hạn chế năng lực chứng cứ",
                "situation": "formal"
            }
        ],
        "relatedTerms": ["증명력", "위법수집증거배제법칙", "전문법칙", "자백배제법칙"]
    },
    {
        "slug": "wi-beop-su-jip-jeung-geo-bae-je-beop-chik",
        "korean": "위법수집증거배제법칙",
        "vietnamese": "Nguyên tắc loại trừ chứng cứ thu thập bất hợp pháp",
        "hanja": "違法蒐集證據排除法則",
        "hanjaReading": "違(어긋날 위) 法(법 법) 蒐(모을 수) 集(모을 집) 證(증거 증) 據(근거 거) 排(물리칠 배) 除(덜 제) 法(법 법) 則(법칙 칙)",
        "pronunciation": "위법수집증거배제법칙",
        "meaningKo": "수사기관이 적법한 절차를 위반하여 수집한 증거는 증거능력이 부정된다는 법원칙입니다. 영장주의, 진술거부권 고지, 변호인 참여권 등을 위반한 경우 적용됩니다. 통역 시 단순히 '불법 증거는 안 된다'는 식의 설명이 아니라, 적법절차 원칙(due process)과 연결하여 설명해야 합니다. 베트남 통역사들이 특히 주의해야 할 점은, 한국에서는 이 법칙이 매우 엄격하게 적용되어 증거 채택이 무효화될 수 있다는 점입니다.",
        "meaningVi": "Là nguyên tắc pháp lý theo đó chứng cứ được thu thập bởi cơ quan điều tra vi phạm thủ tục hợp pháp sẽ bị phủ nhận năng lực chứng cứ. Áp dụng khi vi phạm nguyên tắc lệnh, thông báo quyền im lặng, quyền có luật sư tham gia, v.v. Đây là nguyên tắc rất quan trọng và được áp dụng nghiêm ngặt trong hệ thống tư pháp Hàn Quốc.",
        "context": "형사소송절차",
        "culturalNote": "한국 형사소송법은 2007년 개정 이후 위법수집증거배제법칙을 명문화하였습니다(형사소송법 제308조의2). 미국의 'exclusionary rule'을 계수한 것으로, 인권보호와 적법절차 준수를 강조합니다. 베트남에서도 유사한 원칙이 있지만 한국만큼 엄격하게 적용되지 않을 수 있습니다. 통역 시 이 법칙이 한국 형사재판에서 피고인의 중요한 방어 수단임을 명확히 전달해야 합니다.",
        "commonMistakes": [
            {
                "mistake": "'không hợp pháp'만으로 번역",
                "correction": "'thu thập bất hợp pháp'로 명확히 번역",
                "explanation": "증거 자체가 불법이 아니라 수집 과정이 위법하다는 의미를 분명히 해야 합니다"
            },
            {
                "mistake": "단순히 '증거 무효'로만 설명",
                "correction": "'증거능력 배제'라는 법률 용어로 정확히 전달",
                "explanation": "증거가 완전히 무효가 아니라 법정에서 사용할 수 없다는 의미입니다"
            },
            {
                "mistake": "모든 절차 위반에 적용되는 것으로 설명",
                "correction": "중대한 위법이나 적법절차 위반에 한정된다고 설명",
                "explanation": "경미한 절차 위반은 배제되지 않을 수 있습니다"
            }
        ],
        "examples": [
            {
                "ko": "영장 없이 압수한 증거는 위법수집증거배제법칙에 따라 증거능력이 없습니다",
                "vi": "Chứng cứ bị tịch thu không có lệnh sẽ không có năng lực chứng cứ theo nguyên tắc loại trừ chứng cứ thu thập bất hợp pháp",
                "situation": "formal"
            },
            {
                "ko": "변호인 참여 없이 진행된 조사로 얻은 진술은 배제되어야 합니다",
                "vi": "Lời khai thu được từ cuộc điều tra tiến hành không có sự tham gia của luật sư phải bị loại trừ",
                "situation": "formal"
            },
            {
                "ko": "이 법칙은 수사기관의 위법행위를 억제하는 기능도 합니다",
                "vi": "Nguyên tắc này cũng có chức năng ngăn chặn hành vi vi phạm pháp luật của cơ quan điều tra",
                "situation": "formal"
            }
        ],
        "relatedTerms": ["증거능력", "적법절차", "영장주의", "독수독과이론"]
    },
    {
        "slug": "jeon-mun-beop-chik",
        "korean": "전문법칙",
        "vietnamese": "Nguyên tắc truyền văn",
        "hanja": "傳聞法則",
        "hanjaReading": "傳(전할 전) 聞(들을 문) 法(법 법) 則(법칙 칙)",
        "pronunciation": "전문법칙",
        "meaningKo": "법정 외에서 행해진 진술을 그 내용의 진실성을 증명하기 위해 법정에서 증거로 사용하는 것을 원칙적으로 금지하는 법칙입니다. 전문증거는 원진술자를 반대신문할 수 없어 진술의 신빙성을 담보하기 어렵기 때문입니다. 통역 시 '전문(傳聞)'의 개념을 '직접 경험하지 않고 다른 사람에게서 들은 것'이라고 설명하고, 원진술자의 출석과 반대신문권 보장이 핵심임을 강조해야 합니다. 베트남어로는 '간접 증거의 제한'이라는 맥락으로 이해시키는 것이 효과적입니다.",
        "meaningVi": "Là nguyên tắc về nguyên tắc cấm sử dụng làm chứng cứ tại tòa án những lời khai được thực hiện ngoài tòa án để chứng minh tính chân thực của nội dung đó. Chứng cứ truyền văn không thể bảo đảm tính tin cậy của lời khai vì không thể phản đối thẩm vấn người khai ban đầu. Đây là nguyên tắc quan trọng để bảo vệ quyền phản biện của bị cáo.",
        "context": "형사소송절차",
        "culturalNote": "전문법칙은 영미법계의 'hearsay rule'을 계수한 것으로, 한국 형사소송법 제310조의2에 규정되어 있습니다. 피고인의 반대신문권을 보장하기 위한 제도입니다. 베트남 형사소송법에서는 서면 증거의 사용이 더 폭넓게 인정되는 경향이 있어, 한국의 엄격한 전문법칙이 생소할 수 있습니다. 통역 시 '원진술자의 법정 출석과 선서, 반대신문'이 핵심이라는 점을 명확히 전달해야 합니다.",
        "commonMistakes": [
            {
                "mistake": "전문증거를 '전문가의 증거'로 오해",
                "correction": "'전해 들은 증거(hearsay)'로 설명",
                "explanation": "전문(傳聞)은 '듣고 전함'이지 '전문성'이 아닙니다"
            },
            {
                "mistake": "모든 서면 증거를 전문증거로 분류",
                "correction": "원진술자가 법정에 나와 확인할 수 없는 것만 전문증거",
                "explanation": "법정에서 작성된 조서나 원진술자가 출석한 경우는 예외입니다"
            },
            {
                "mistake": "전문법칙 예외를 설명하지 않음",
                "correction": "특신상태, 동의 등 예외사유를 함께 설명",
                "explanation": "실무에서는 예외가 많이 적용되므로 이를 알려야 합니다"
            }
        ],
        "examples": [
            {
                "ko": "이 진술조서는 전문법칙에 따라 증거로 사용할 수 없습니다",
                "vi": "Biên bản khai báo này không thể được sử dụng làm chứng cứ theo nguyên tắc truyền văn",
                "situation": "formal"
            },
            {
                "ko": "원진술자가 출석하여 반대신문을 받으면 전문증거가 아닙니다",
                "vi": "Nếu người khai ban đầu có mặt và chịu phản đối thẩm vấn thì không phải là chứng cứ truyền văn",
                "situation": "formal"
            },
            {
                "ko": "피고인이 증거로 함에 동의하면 전문법칙의 예외로 인정됩니다",
                "vi": "Nếu bị cáo đồng ý sử dụng làm chứng cứ thì được thừa nhận như ngoại lệ của nguyên tắc truyền văn",
                "situation": "formal"
            }
        ],
        "relatedTerms": ["증거능력", "반대신문권", "특신상태", "진술조서"]
    },
    {
        "slug": "gong-pan-jung-sim-ju-ui",
        "korean": "공판중심주의",
        "vietnamese": "Chủ nghĩa tập trung vào phiên tòa công khai",
        "hanja": "公判中心主義",
        "hanjaReading": "公(공평할 공) 判(판단할 판) 中(가운데 중) 心(마음 심) 主(주인 주) 義(옳을 의)",
        "pronunciation": "공판중심주의",
        "meaningKo": "형사재판에서 사실인정은 공개된 법정에서의 심리를 중심으로 이루어져야 한다는 원칙입니다. 수사단계에서 작성된 조서보다 법정에서의 직접 진술을 우선시하며, 증거조사와 변론이 공판정에서 집중적으로 이루어져야 합니다. 통역 시 '조서재판에서 공판재판으로의 전환'이라는 역사적 맥락과, 피고인의 방어권 보장이 핵심임을 설명해야 합니다. 베트남 통역사는 한국이 2007년 이후 공판중심주의를 강화하고 있음을 인지해야 합니다.",
        "meaningVi": "Là nguyên tắc theo đó việc xác định sự thật trong xét xử hình sự phải được thực hiện tập trung vào phiên xét xử công khai tại tòa án. Ưu tiên lời khai trực tiếp tại tòa hơn biên bản được lập trong giai đoạn điều tra, và việc điều tra chứng cứ và tranh luận phải được tiến hành tập trung tại phiên tòa. Đây là nguyên tắc quan trọng để bảo vệ quyền bào chữa của bị cáo.",
        "context": "형사소송절차",
        "culturalNote": "한국은 전통적으로 '조서재판' 중심이었으나, 2007년 형사소송법 개정을 통해 공판중심주의를 강화했습니다. 이는 피고인의 방어권 보장과 실체적 진실 발견을 위한 것입니다. 베트남도 공개재판 원칙이 있지만, 한국처럼 법정에서의 직접심리를 강조하는 정도는 다를 수 있습니다. 통역 시 '피고인이 법정에서 직접 증인을 대면하고 질문할 권리'가 핵심임을 강조해야 합니다.",
        "commonMistakes": [
            {
                "mistake": "단순히 '공개재판'으로 번역",
                "correction": "'공판 중심의 심리'라는 의미로 전달",
                "explanation": "공개성뿐 아니라 법정 중심의 증거조사가 핵심입니다"
            },
            {
                "mistake": "조서의 증거능력을 완전히 부정하는 것으로 설명",
                "correction": "조서보다 법정진술을 우선한다고 설명",
                "explanation": "조서도 일정 요건 하에 증거능력이 인정됩니다"
            },
            {
                "mistake": "검사의 조서 낭독을 원칙으로 설명",
                "correction": "증인의 직접 출석과 신문이 원칙이라고 설명",
                "explanation": "공판중심주의의 핵심은 직접심리입니다"
            }
        ],
        "examples": [
            {
                "ko": "공판중심주의에 따라 증인을 직접 출석시켜 신문해야 합니다",
                "vi": "Theo chủ nghĩa tập trung vào phiên tòa công khai, phải triệu tập nhân chứng trực tiếp để thẩm vấn",
                "situation": "formal"
            },
            {
                "ko": "수사단계 조서는 보충적 증거로만 활용됩니다",
                "vi": "Biên bản giai đoạn điều tra chỉ được sử dụng như chứng cứ bổ sung",
                "situation": "formal"
            },
            {
                "ko": "피고인은 법정에서 증인과 대면하여 반대신문할 권리가 있습니다",
                "vi": "Bị cáo có quyền đối chất với nhân chứng tại tòa và tiến hành phản đối thẩm vấn",
                "situation": "formal"
            }
        ],
        "relatedTerms": ["직접심리주의", "반대신문권", "전문법칙", "구술심리주의"]
    },
    {
        "slug": "ban-dae-sin-mun-gwon",
        "korean": "반대신문권",
        "vietnamese": "Quyền phản đối thẩm vấn",
        "hanja": "反對訊問權",
        "hanjaReading": "反(돌이킬 반) 對(대할 대) 訊(물을 신) 問(물을 문) 權(권리 권)",
        "pronunciation": "반대신문권",
        "meaningKo": "형사재판에서 피고인이나 변호인이 상대방(주로 검사)이 신청한 증인에게 질문할 수 있는 권리입니다. 증인의 진술 신빙성을 탄핵하고 피고인에게 유리한 사실을 이끌어내기 위한 방어권의 핵심입니다. 통역 시 '주신문'과 '반대신문'의 차이를 명확히 설명하고, 반대신문이 단순한 질문이 아니라 헌법상 권리임을 강조해야 합니다. 베트남어로는 '상대방 증인을 심문할 권리'라는 직접적 표현이 이해하기 쉽습니다.",
        "meaningVi": "Là quyền của bị cáo hoặc luật sư bào chữa được đặt câu hỏi cho nhân chứng do phía đối phương (chủ yếu là công tố viên) đề nghị. Đây là cốt lõi của quyền bào chữa nhằm bác bỏ độ tin cậy của lời khai nhân chứng và khai thác sự thật có lợi cho bị cáo. Đây là quyền hiến định, không chỉ là một thủ tục tố tụng đơn thuần.",
        "context": "형사소송절차",
        "culturalNote": "반대신문권은 영미법계의 'right to cross-examination'을 계수한 것으로, 한국 헌법 제27조(재판받을 권리)와 형사소송법에서 보장합니다. 대륙법계인 베트남에서는 심문 절차가 한국과 다를 수 있으며, 판사 주도의 직권탐지주의가 강할 수 있습니다. 통역 시 한국에서는 당사자주의적 요소가 강화되어 변호인의 반대신문이 매우 중요한 역할을 한다는 점을 설명해야 합니다.",
        "commonMistakes": [
            {
                "mistake": "'chất vấn'(질의)로만 번역",
                "correction": "'phản đối thẩm vấn'으로 정확히 번역",
                "explanation": "일반 질문과 법적 권리인 반대신문을 구별해야 합니다"
            },
            {
                "mistake": "피고인만의 권리로 설명",
                "correction": "변호인도 행사할 수 있는 권리로 설명",
                "explanation": "실무에서는 주로 변호인이 반대신문을 수행합니다"
            },
            {
                "mistake": "주신문과 반대신문의 차이를 설명하지 않음",
                "correction": "주신문은 자기 측 증인, 반대신문은 상대 측 증인에 대한 것",
                "explanation": "신문의 종류와 목적을 구분해야 합니다"
            }
        ],
        "examples": [
            {
                "ko": "변호인은 검사 측 증인에게 반대신문권을 행사할 수 있습니다",
                "vi": "Luật sư bào chữa có thể thực hiện quyền phản đối thẩm vấn đối với nhân chứng bên công tố",
                "situation": "formal"
            },
            {
                "ko": "반대신문 기회를 박탈당하면 재판이 무효가 될 수 있습니다",
                "vi": "Nếu bị tước quyền phản đối thẩm vấn, phiên tòa có thể bị vô hiệu",
                "situation": "formal"
            },
            {
                "ko": "반대신문을 통해 증인 진술의 모순점을 드러낼 수 있습니다",
                "vi": "Thông qua phản đối thẩm vấn có thể phát hiện điểm mâu thuẫn trong lời khai của nhân chứng",
                "situation": "formal"
            }
        ],
        "relatedTerms": ["주신문", "재신문", "증인신문", "공판중심주의"]
    },
    {
        "slug": "ja-baek-bae-je-beop-chik",
        "korean": "자백배제법칙",
        "vietnamese": "Nguyên tắc loại trừ lời thú tội",
        "hanja": "自白排除法則",
        "hanjaReading": "自(스스로 자) 白(밝을 백) 排(물리칠 배) 除(덜 제) 法(법 법) 則(법칙 칙)",
        "pronunciation": "자백배제법칙",
        "meaningKo": "피고인의 자백이 강제, 고문, 폭행, 협박, 장기간 구속, 기망 등 임의성이 의심되는 방법으로 얻어진 경우 증거능력을 부인하는 법칙입니다. 헌법 제12조와 형사소송법 제309조에 규정되어 있습니다. 통역 시 '자백의 임의성'이 핵심이며, 임의성이 없으면 증거로 쓸 수 없다는 점을 명확히 해야 합니다. 베트남어로는 '강제로 얻은 자백은 무효'라는 맥락으로 설명하되, 법적 근거와 요건을 정확히 전달해야 합니다.",
        "meaningVi": "Là nguyên tắc phủ nhận năng lực chứng cứ đối với lời thú tội của bị cáo nếu thu được bằng phương pháp gây nghi ngờ về tính tự nguyện như cưỡng ép, tra tấn, bạo hành, đe dọa, giam giữ kéo dài, lừa dối. Được quy định tại Điều 12 Hiến pháp và Điều 309 Luật Tố tụng Hình sự Hàn Quốc. Đây là nguyên tắc quan trọng để bảo vệ nhân quyền của bị cáo.",
        "context": "형사소송절차",
        "culturalNote": "한국 헌법은 '불리한 진술을 강요당하지 않을 권리'를 명시하고 있으며, 자백배제법칙은 이를 구체화한 것입니다. 과거 고문에 의한 자백 강요의 역사적 반성에서 비롯된 제도입니다. 베트남에서도 강제 자백은 금지되지만, 임의성 판단 기준과 입증책임이 다를 수 있습니다. 통역 시 한국에서는 검사가 임의성을 입증해야 한다는 점을 강조해야 합니다.",
        "commonMistakes": [
            {
                "mistake": "단순히 '강제 자백 금지'로만 설명",
                "correction": "'임의성 없는 자백의 증거능력 배제'로 정확히 설명",
                "explanation": "법적 효과는 증거능력 배제이며, 임의성이 핵심 개념입니다"
            },
            {
                "mistake": "고문이나 폭행만 해당하는 것으로 설명",
                "correction": "기망, 회유, 장기간 구속 등도 포함된다고 설명",
                "explanation": "물리적 강제뿐 아니라 심리적 강제도 해당됩니다"
            },
            {
                "mistake": "자백배제법칙과 위법수집증거배제법칙을 혼동",
                "correction": "자백배제법칙은 자백에 한정, 위법수집증거배제법칙은 모든 증거",
                "explanation": "적용 대상과 요건이 다릅니다"
            }
        ],
        "examples": [
            {
                "ko": "변호인 없이 장시간 조사받은 자백은 임의성이 인정되지 않을 수 있습니다",
                "vi": "Lời thú tội sau khi bị điều tra trong thời gian dài không có luật sư có thể không được thừa nhận tính tự nguyện",
                "situation": "formal"
            },
            {
                "ko": "자백의 임의성은 검사가 입증해야 합니다",
                "vi": "Công tố viên phải chứng minh tính tự nguyện của lời thú tội",
                "situation": "formal"
            },
            {
                "ko": "강압에 의한 자백은 자백배제법칙에 따라 증거로 사용할 수 없습니다",
                "vi": "Lời thú tội do cưỡng ép không thể sử dụng làm chứng cứ theo nguyên tắc loại trừ lời thú tội",
                "situation": "formal"
            }
        ],
        "relatedTerms": ["자백의임의성", "진술거부권", "위법수집증거배제법칙", "보강증거법칙"]
    },
    {
        "slug": "bo-gang-jeung-geo-beop-chik",
        "korean": "보강증거법칙",
        "vietnamese": "Nguyên tắc chứng cứ bổ sung",
        "hanja": "補强證據法則",
        "hanjaReading": "補(도울 보) 强(강할 강) 證(증거 증) 據(근거 거) 法(법 법) 則(법칙 칙)",
        "pronunciation": "보강증거법칙",
        "meaningKo": "피고인의 자백만으로는 유죄를 인정할 수 없고, 자백을 뒷받침하는 다른 증거(보강증거)가 있어야 한다는 법칙입니다. 형사소송법 제310조에 규정되어 있으며, 허위자백에 의한 오판을 방지하기 위한 제도입니다. 통역 시 '자백만으로는 부족하다'는 점과, 보강증거는 범죄사실 전체가 아니라 자백의 신빙성을 뒷받침하면 된다는 점을 설명해야 합니다. 베트남 통역사는 이 법칙이 자백의 임의성과는 별개의 문제임을 이해해야 합니다.",
        "meaningVi": "Là nguyên tắc theo đó không thể kết tội chỉ dựa trên lời thú tội của bị cáo mà phải có chứng cứ khác (chứng cứ bổ sung) hỗ trợ lời thú tội. Được quy định tại Điều 310 Luật Tố tụng Hình sự, đây là chế độ nhằm ngăn ngừa phán quyết oan sai do lời thú tội giả. Chứng cứ bổ sung không cần chứng minh toàn bộ sự việc phạm tội mà chỉ cần hỗ trợ độ tin cậy của lời thú tội.",
        "context": "형사소송절차",
        "culturalNote": "보강증거법칙은 대륙법계의 전통적 제도로, 자백 편중주의를 방지하기 위한 것입니다. 한국은 과거 고문에 의한 허위자백 사건들을 겪으며 이 법칙의 중요성을 인식하게 되었습니다. 베트남에서도 유사한 원칙이 있을 수 있으나, 보강증거의 범위와 정도에 대한 해석이 다를 수 있습니다. 통역 시 보강증거는 범죄사실 전체를 입증할 필요는 없고, 자백의 진실성을 뒷받침하면 충분하다는 점을 명확히 해야 합니다.",
        "commonMistakes": [
            {
                "mistake": "보강증거가 범죄사실 전체를 입증해야 한다고 설명",
                "correction": "자백의 진실성을 뒷받침하면 충분하다고 설명",
                "explanation": "보강증거는 자백의 신빙성을 보완하는 것이지 독립적으로 범죄를 입증하는 것이 아닙니다"
            },
            {
                "mistake": "자백배제법칙과 혼동",
                "correction": "자백배제법칙은 임의성 문제, 보강증거법칙은 신빙성 문제",
                "explanation": "두 법칙은 적용 요건과 목적이 다릅니다"
            },
            {
                "mistake": "공범의 자백을 보강증거로 사용할 수 있다고 설명",
                "correction": "공범의 자백은 보강증거가 될 수 없다고 설명",
                "explanation": "판례는 공범의 자백을 보강증거로 인정하지 않습니다"
            }
        ],
        "examples": [
            {
                "ko": "피고인의 자백 외에 범행도구가 발견되어 보강증거법칙을 충족합니다",
                "vi": "Ngoài lời thú tội của bị cáo, công cụ phạm tội được phát hiện nên đáp ứng nguyên tắc chứng cứ bổ sung",
                "situation": "formal"
            },
            {
                "ko": "자백만으로는 유죄를 인정할 수 없으므로 추가 증거가 필요합니다",
                "vi": "Không thể kết tội chỉ dựa trên lời thú tội nên cần chứng cứ bổ sung",
                "situation": "formal"
            },
            {
                "ko": "보강증거는 범죄사실의 일부만 입증하면 됩니다",
                "vi": "Chứng cứ bổ sung chỉ cần chứng minh một phần sự việc phạm tội",
                "situation": "formal"
            }
        ],
        "relatedTerms": ["자백", "자백배제법칙", "증거능력", "증명력"]
    },
    {
        "slug": "jeung-geo-bo-jeon",
        "korean": "증거보전",
        "vietnamese": "Bảo toàn chứng cứ",
        "hanja": "證據保全",
        "hanjaReading": "證(증거 증) 據(근거 거) 保(지킬 보) 全(온전할 전)",
        "pronunciation": "증거보전",
        "meaningKo": "공판기일 전에 증거를 조사하여 그 결과를 보존하는 절차입니다. 증인이 병환 등으로 공판에 출석하기 어렵거나, 증거가 멸실될 우려가 있을 때 신청합니다. 형사소송법 제184조~제221조의2에 규정되어 있습니다. 통역 시 '긴급하게 증거를 확보하는 절차'라는 개념과, 법원의 허가가 필요하다는 점을 설명해야 합니다. 베트남어로는 '증거를 미리 보호하는 절차'로 이해시키는 것이 효과적입니다.",
        "meaningVi": "Là thủ tục điều tra chứng cứ trước ngày xét xử công khai và bảo quản kết quả đó. Được đề nghị khi nhân chứng khó có mặt tại phiên tòa do ốm đau v.v. hoặc khi có lo ngại chứng cứ bị mất mát. Quy định tại Điều 184~221-2 Luật Tố tụng Hình sự. Đây là thủ tục cần có sự cho phép của tòa án nhằm bảo đảm chứng cứ trong trường hợp khẩn cấp.",
        "context": "형사소송절차",
        "culturalNote": "증거보전은 공판중심주의의 예외적 제도로, 불가피한 경우에만 인정됩니다. 한국에서는 특히 성폭력 피해자나 아동 증인의 경우 증거보전이 자주 활용됩니다. 베트남에서도 유사한 제도가 있을 수 있으나, 절차와 요건이 다를 수 있습니다. 통역 시 증거보전은 법원의 허가를 받아 판사 앞에서 진행되며, 그 결과가 공판에서 증거로 사용된다는 점을 명확히 해야 합니다.",
        "commonMistakes": [
            {
                "mistake": "단순한 증거 수집으로 이해",
                "correction": "법원의 허가를 받아 진행하는 공식 절차로 설명",
                "explanation": "수사기관의 일반적 증거 수집과는 다릅니다"
            },
            {
                "mistake": "언제든 신청할 수 있다고 설명",
                "correction": "증거가 멸실될 우려 등 특별한 사유가 있어야 한다고 설명",
                "explanation": "긴급성과 필요성이 인정되어야 합니다"
            },
            {
                "mistake": "검사만 신청할 수 있다고 설명",
                "correction": "피고인이나 변호인도 신청할 수 있다고 설명",
                "explanation": "당사자 쌍방 모두 신청권이 있습니다"
            }
        ],
        "examples": [
            {
                "ko": "중요 증인이 해외로 출국할 예정이므로 증거보전을 신청합니다",
                "vi": "Vì nhân chứng quan trọng dự định xuất cảnh nên đề nghị bảo toàn chứng cứ",
                "situation": "formal"
            },
            {
                "ko": "증거보전 절차는 판사의 지휘 하에 진행됩니다",
                "vi": "Thủ tục bảo toàn chứng cứ được tiến hành dưới sự chỉ đạo của thẩm phán",
                "situation": "formal"
            },
            {
                "ko": "증거보전으로 확보한 증언은 공판에서 증거로 사용할 수 있습니다",
                "vi": "Lời khai được xác bảo thông qua bảo toàn chứng cứ có thể được sử dụng làm chứng cứ tại phiên tòa",
                "situation": "formal"
            }
        ],
        "relatedTerms": ["증거조사", "증인신문", "공판전정리절차", "영상녹화"]
    },
    {
        "slug": "ja-baek-ui-im-ui-seong",
        "korean": "자백의임의성",
        "vietnamese": "Tính tự nguyện của lời thú tội",
        "hanja": "自白의任意性",
        "hanjaReading": "自(스스로 자) 白(밝을 백) 의 任(맡길 임) 意(뜻 의) 性(성품 성)",
        "pronunciation": "자백의임의성",
        "meaningKo": "피고인의 자백이 외부의 강제, 고문, 폭행, 협박, 기망 등 없이 자유로운 의사에 기하여 이루어졌는지 여부를 의미합니다. 임의성이 없는 자백은 자백배제법칙에 따라 증거능력이 부정됩니다. 통역 시 '자유로운 의사'가 핵심이며, 물리적 강제뿐 아니라 심리적 압박도 임의성을 훼손할 수 있음을 설명해야 합니다. 베트nam어로는 '강제 없이 스스로 한 자백'이라는 개념으로 전달하되, 입증책임이 검사에게 있다는 점을 강조해야 합니다.",
        "meaningVi": "Ý chỉ việc lời thú tội của bị cáo có được thực hiện dựa trên ý chí tự do không có sự cưỡng ép, tra tấn, bạo hành, đe dọa, lừa dối từ bên ngoài hay không. Lời thú tội không có tính tự nguyện sẽ bị phủ nhận năng lực chứng cứ theo nguyên tắc loại trừ lời thú tội. Không chỉ cưỡng ép vật lý mà áp lực tâm lý cũng có thể làm tổn hại tính tự nguyện.",
        "context": "형사소송절차",
        "culturalNote": "한국 형사소송법은 자백의 임의성 입증책임을 검사에게 부과하고 있습니다. 이는 피고인 보호를 위한 것으로, 무죄추정의 원칙과 연결됩니다. 실무에서는 조사과정의 녹음·녹화 자료가 임의성 판단의 중요한 증거가 됩니다. 베트남에서는 입증책임의 배분이 다를 수 있으므로, 통역 시 한국에서는 검사가 임의성을 증명해야 한다는 점을 명확히 해야 합니다.",
        "commonMistakes": [
            {
                "mistake": "'자발성'으로 번역",
                "correction": "'임의성(任意性)'으로 정확히 번역",
                "explanation": "법률 용어로서 '임의성'은 자발성보다 넓은 개념입니다"
            },
            {
                "mistake": "피고인이 임의성을 입증해야 한다고 설명",
                "correction": "검사가 임의성을 입증해야 한다고 설명",
                "explanation": "입증책임은 검사에게 있습니다"
            },
            {
                "mistake": "물리적 강제만 해당한다고 설명",
                "correction": "심리적 압박, 기망, 회유 등도 임의성을 해칠 수 있다고 설명",
                "explanation": "임의성 판단은 종합적으로 이루어집니다"
            }
        ],
        "examples": [
            {
                "ko": "조사과정이 녹화되어 있어 자백의 임의성을 확인할 수 있습니다",
                "vi": "Quá trình điều tra được ghi hình nên có thể xác nhận tính tự nguyện của lời thú tội",
                "situation": "formal"
            },
            {
                "ko": "자백의 임의성이 의심되면 검사가 이를 입증해야 합니다",
                "vi": "Nếu tính tự nguyện của lời thú tội bị nghi ngờ, công tố viên phải chứng minh điều đó",
                "situation": "formal"
            },
            {
                "ko": "변호인 참여 없이 밤새 조사받은 자백은 임의성이 부정될 수 있습니다",
                "vi": "Lời thú tội sau khi bị điều tra suốt đêm không có luật sư có thể bị phủ nhận tính tự nguyện",
                "situation": "formal"
            }
        ],
        "relatedTerms": ["자백배제법칙", "진술거부권", "변호인참여권", "피의자신문조서"]
    },
    {
        "slug": "jik-jeop-sim-ri-ju-ui",
        "korean": "직접심리주의",
        "vietnamese": "Chủ nghĩa xét xử trực tiếp",
        "hanja": "直接審理主義",
        "hanjaReading": "直(곧을 직) 接(이을 접) 審(살필 심) 理(다스릴 리) 主(주인 주) 義(옳을 의)",
        "pronunciation": "직접심리주의",
        "meaningKo": "법관이 직접 증거를 조사하고 당사자를 심문하여 사실을 인정해야 한다는 원칙입니다. 서면이나 전문(傳聞)이 아니라 법정에서의 직접 경험을 토대로 판단해야 합니다. 공판중심주의와 밀접하게 연결된 원칙입니다. 통역 시 '법관이 직접 보고 듣고 판단한다'는 개념과, 이것이 실체적 진실 발견과 피고인 방어권 보장을 위한 것임을 설명해야 합니다. 베트남어로는 '법관의 직접 참여'라는 맥락으로 전달하는 것이 효과적입니다.",
        "meaningVi": "Là nguyên tắc theo đó thẩm phán phải trực tiếp điều tra chứng cứ và thẩm vấn các bên để xác định sự thật. Phải đưa ra phán đoán dựa trên kinh nghiệm trực tiếp tại tòa án chứ không phải dựa trên văn bản hoặc truyền văn. Đây là nguyên tắc liên kết chặt chẽ với chủ nghĩa tập trung vào phiên tòa công khai, nhằm phát hiện sự thật thực chất và bảo đảm quyền bào chữa của bị cáo.",
        "context": "형사소송절차",
        "culturalNote": "직접심리주의는 대륙법계와 영미법계 모두에서 인정되는 원칙으로, 법관의 심증 형성을 위한 기본 요건입니다. 한국에서는 이 원칙이 공판중심주의 강화와 함께 더욱 중요해졌습니다. 베트남도 유사한 원칙이 있을 수 있으나, 서면증거의 활용 범위가 다를 수 있습니다. 통역 시 직접심리주의가 전문법칙, 공판중심주의와 어떻게 연결되는지 설명하면 이해가 쉽습니다.",
        "commonMistakes": [
            {
                "mistake": "법관이 모든 증거를 직접 수집해야 한다고 설명",
                "correction": "법관이 법정에서 직접 증거조사를 해야 한다고 설명",
                "explanation": "증거 수집은 수사기관이 하고, 법관은 법정에서 조사합니다"
            },
            {
                "mistake": "공판중심주의와 동일한 개념으로 설명",
                "correction": "관련은 있지만 구별되는 원칙으로 설명",
                "explanation": "직접심리주의는 법관의 직접 조사, 공판중심주의는 법정 중심 심리입니다"
            },
            {
                "mistake": "서면 증거를 전혀 사용할 수 없다고 설명",
                "correction": "원칙적으로 직접 조사를 우선하지만 예외가 있다고 설명",
                "explanation": "일정한 요건 하에 서면 증거도 사용 가능합니다"
            }
        ],
        "examples": [
            {
                "ko": "직접심리주의에 따라 증인을 법정에 출석시켜 심문해야 합니다",
                "vi": "Theo chủ nghĩa xét xử trực tiếp, phải triệu tập nhân chứng đến tòa để thẩm vấn",
                "situation": "formal"
            },
            {
                "ko": "판결에 관여한 법관이 직접 증거조사를 하지 않으면 판결이 무효입니다",
                "vi": "Nếu thẩm phán tham gia phán quyết không trực tiếp điều tra chứng cứ thì phán quyết vô hiệu",
                "situation": "formal"
            },
            {
                "ko": "조서 낭독보다는 증인의 직접 진술이 우선됩니다",
                "vi": "Lời khai trực tiếp của nhân chứng được ưu tiên hơn việc đọc biên bản",
                "situation": "formal"
            }
        ],
        "relatedTerms": ["공판중심주의", "구술심리주의", "전문법칙", "증거조사"]
    }
]


def main():
    """메인 실행 함수"""
    print(f"📂 대상 파일: {LEGAL_JSON_PATH}")

    # 기존 legal.json 읽기
    try:
        with open(LEGAL_JSON_PATH, 'r', encoding='utf-8') as f:
            existing_data = json.load(f)
        print(f"✅ 기존 데이터 로드 완료: {len(existing_data)}개 용어")
    except FileNotFoundError:
        print("❌ legal.json 파일을 찾을 수 없습니다.")
        return
    except json.JSONDecodeError as e:
        print(f"❌ JSON 파싱 오류: {e}")
        return

    # 중복 확인
    existing_slugs = {term.get('slug') for term in existing_data}
    duplicates = [term['slug'] for term in new_terms if term['slug'] in existing_slugs]

    if duplicates:
        print(f"⚠️  중복된 slug 발견: {duplicates}")
        print("중복 제거 후 진행합니다.")
        new_terms_filtered = [term for term in new_terms if term['slug'] not in existing_slugs]
    else:
        new_terms_filtered = new_terms

    if not new_terms_filtered:
        print("⚠️  추가할 새 용어가 없습니다.")
        return

    # 데이터 병합
    merged_data = existing_data + new_terms_filtered
    print(f"📊 병합 후 총 용어 수: {len(merged_data)}개 (추가: {len(new_terms_filtered)}개)")

    # legal.json 덮어쓰기 (FLAT ARRAY 형식 유지)
    try:
        with open(LEGAL_JSON_PATH, 'w', encoding='utf-8') as f:
            json.dump(merged_data, f, ensure_ascii=False, indent=2)
        print(f"✅ {LEGAL_JSON_PATH} 업데이트 완료!")
        print(f"✨ 추가된 용어: {len(new_terms_filtered)}개")
        for term in new_terms_filtered:
            print(f"   - {term['korean']} ({term['slug']})")
    except Exception as e:
        print(f"❌ 파일 저장 오류: {e}")


if __name__ == "__main__":
    main()
