#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""가정폭력/가사법 용어 추가 (v9-a)"""
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
            "slug": "bao-luc-gia-dinh",
            "korean": "가정폭력",
            "vietnamese": "Bạo lực gia đình",
            "hanja": "家庭暴力",
            "hanjaReading": "家(집 가) + 庭(뜰 정) + 暴(사나울 폭) + 力(힘 력)",
            "pronunciation": "까정포력",
            "meaningKo": "가족 구성원 사이의 신체적, 정신적 또는 재산상 피해를 수반하는 행위를 말합니다. 통역 시 베트남어 'bạo lực'은 물리적 폭력만을 연상시킬 수 있으나, 한국 가정폭력특례법은 정서적 학대, 경제적 통제도 포함하므로 반드시 'bạo lực thể chất và tinh thần'으로 명확히 전달해야 합니다. 피해자 보호와 가해자 처벌을 동시에 다루는 특수한 법 영역입니다.",
            "meaningVi": "Hành vi gây tổn hại về thể chất, tinh thần hoặc tài sản giữa các thành viên trong gia đình. Luật Hàn Quốc bao gồm cả bạo lực thể chất, lạm dụng cảm xúc và kiểm soát kinh tế.",
            "context": "가정폭력 피해 상담 및 법률 지원 상황에서 사용",
            "culturalNote": "한국은 2007년부터 가정폭력을 범죄로 엄격히 처벌하며 피해자 보호 시스템(쉼터, 상담소)이 발달했습니다. 베트남도 2007년 가정폭력방지법을 제정했으나, 전통적으로 가정 내 문제를 외부에 알리는 것을 꺼리는 문화가 강합니다. 통역 시 한국의 적극적 개입 시스템을 설명해야 합니다.",
            "commonMistakes": [
                {
                    "mistake": "bạo lực trong nhà",
                    "correction": "bạo lực gia đình",
                    "explanation": "'trong nhà'는 '집 안에서'라는 공간적 의미만 전달하며 법률 용어로 부적절합니다"
                },
                {
                    "mistake": "đánh đập vợ chồng",
                    "correction": "bạo lực gia đình (bao gồm cả bạo lực tinh thần)",
                    "explanation": "부부 간 구타만을 의미하여 자녀, 노인 학대 및 정서적 폭력을 누락시킵니다"
                },
                {
                    "mistake": "chuyện gia đình",
                    "correction": "bạo lực gia đình (vấn đề pháp lý)",
                    "explanation": "'가족 일'로 축소하여 범죄 행위의 심각성을 약화시킵니다"
                }
            ],
            "examples": [
                {
                    "ko": "가정폭력 피해자는 긴급전화 112로 즉시 신고할 수 있습니다",
                    "vi": "Nạn nhân bạo lực gia đình có thể gọi ngay đường dây nóng 112",
                    "situation": "formal"
                },
                {
                    "ko": "남편이 술 먹고 때려요. 가정폭력으로 신고하고 싶어요",
                    "vi": "Chồng tôi say rượu và đánh tôi. Tôi muốn báo cáo bạo lực gia đình",
                    "situation": "onsite"
                },
                {
                    "ko": "정서적 학대도 가정폭력에 해당합니다",
                    "vi": "Lạm dụng tinh thần cũng được coi là bạo lực gia đình",
                    "situation": "formal"
                }
            ],
            "relatedTerms": ["보호명령", "접근금지", "임시조치", "가정보호사건"]
        },
        {
            "slug": "li-hon",
            "korean": "이혼",
            "vietnamese": "Ly hôn",
            "hanja": "離婚",
            "hanjaReading": "離(떠날 리) + 婚(혼인 혼)",
            "pronunciation": "리혼",
            "meaningKo": "법률상 혼인 관계를 해소하는 절차입니다. 한국은 협의이혼과 재판상 이혼으로 구분되며, 통역 시 베트남과 달리 한국은 3개월 숙려기간이 의무화되어 있고, 재산분할과 위자료가 별도로 산정된다는 점을 명확히 전달해야 합니다. 양육권 협의가 선행되어야 이혼이 가능합니다.",
            "meaningVi": "Thủ tục chấm dứt quan hệ hôn nhân theo pháp luật. Ở Hàn Quốc chia thành ly hôn thỏa thuận và ly hôn qua tòa án, với thời gian suy nghĩ 3 tháng bắt buộc.",
            "context": "가정법원 이혼 소송 및 상담 상황에서 사용",
            "culturalNote": "한국은 2005년부터 협의이혼 시 3개월 숙려기간을 두며, 미성년 자녀가 있을 경우 양육권 합의가 필수입니다. 베트남은 숙려기간 없이 인민위원회나 법원에서 이혼이 가능하며, 절차가 비교적 간소합니다. 한국의 재산분할 제도는 기여도 중심으로 복잡하므로 통역 시 주의가 필요합니다.",
            "commonMistakes": [
                {
                    "mistake": "chia tay",
                    "correction": "ly hôn",
                    "explanation": "'헤어지다'는 일상적 표현으로 법률적 혼인 해소를 의미하지 않습니다"
                },
                {
                    "mistake": "ly dị",
                    "correction": "ly hôn",
                    "explanation": "'ly dị'는 북베트남 방언으로 공식 법률 문서에서는 'ly hôn'을 사용합니다"
                },
                {
                    "mistake": "đơn phương ly hôn",
                    "correction": "ly hôn đơn phương (재판상 이혼)",
                    "explanation": "일방적 이혼은 재판상 이혼의 개념이지만 협의이혼과 구분 없이 사용하면 혼란을 줍니다"
                }
            ],
            "examples": [
                {
                    "ko": "협의이혼은 법원의 이혼의사 확인 절차를 거쳐야 합니다",
                    "vi": "Ly hôn thỏa thuận phải trải qua thủ tục xác nhận ý định ly hôn tại tòa án",
                    "situation": "formal"
                },
                {
                    "ko": "이혼하면 애들은 누가 키워요? 재산은 어떻게 나눠요?",
                    "vi": "Nếu ly hôn, ai sẽ nuôi con? Tài sản chia thế nào?",
                    "situation": "onsite"
                },
                {
                    "ko": "재판상 이혼 사유는 민법 제840조에 규정되어 있습니다",
                    "vi": "Các lý do ly hôn qua tòa án được quy định trong Điều 840 Luật Dân sự",
                    "situation": "formal"
                }
            ],
            "relatedTerms": ["협의이혼", "재판상이혼", "재산분할", "위자료", "양육권"]
        },
        {
            "slug": "quyen-nuoi-con",
            "korean": "양육권",
            "vietnamese": "Quyền nuôi con",
            "hanja": "養育權",
            "hanjaReading": "養(기를 양) + 育(기를 육) + 權(권리 권)",
            "pronunciation": "양육꿘",
            "meaningKo": "부모가 이혼할 경우 미성년 자녀를 직접 양육할 권리와 의무를 말합니다. 통역 시 한국은 친권과 양육권이 분리 가능하며, 법원은 자녀의 복리를 최우선으로 판단한다는 점을 명확히 전달해야 합니다. 양육권자가 아닌 부모도 면접교섭권을 가지며, 양육비 지급 의무는 별도입니다.",
            "meaningVi": "Quyền và nghĩa vụ trực tiếp nuôi dưỡng con chưa thành niên khi cha mẹ ly hôn. Ở Hàn Quốc, quyền nuôi con có thể tách khỏi quyền thân quyền, và tòa án ưu tiên quyền lợi của trẻ.",
            "context": "가정법원 양육권 분쟁 및 조정 상황에서 사용",
            "culturalNote": "한국은 전통적으로 부계 중심 사회였으나 현대 법원은 성별과 무관하게 자녀 복리를 우선 판단하며, 어린 자녀의 경우 모친에게 양육권이 인정되는 경향이 있습니다. 베트남도 2014년 혼인가족법 개정으로 양성평등이 강화되었으나, 실무상 모친 우선 관행이 남아있습니다. 통역 시 양육권과 친권의 차이를 설명해야 합니다.",
            "commonMistakes": [
                {
                    "mistake": "quyền làm cha mẹ",
                    "correction": "quyền nuôi con (양육권) vs quyền thân quyền (친권)",
                    "explanation": "'부모 될 권리'는 친권과 양육권을 구분하지 못하는 모호한 표현입니다"
                },
                {
                    "mistake": "con thuộc về mẹ",
                    "correction": "quyền nuôi con được trao cho mẹ",
                    "explanation": "'자녀가 엄마 소유'라는 표현은 자녀의 주체성을 무시합니다"
                },
                {
                    "mistake": "quyền giám hộ",
                    "correction": "quyền nuôi con (양육권) hoặc quyền thân quyền (친권)",
                    "explanation": "'후견권'은 부모 이외의 제3자가 행사하는 권리로 의미가 다릅니다"
                }
            ],
            "examples": [
                {
                    "ko": "양육권은 부모의 합의나 법원의 판결로 결정됩니다",
                    "vi": "Quyền nuôi con được quyết định bởi thỏa thuận của cha mẹ hoặc phán quyết của tòa án",
                    "situation": "formal"
                },
                {
                    "ko": "제가 애를 키우고 싶어요. 양육권 어떻게 받나요?",
                    "vi": "Tôi muốn nuôi con. Làm thế nào để được quyền nuôi con?",
                    "situation": "onsite"
                },
                {
                    "ko": "양육권자는 자녀의 일상적인 모든 결정을 내릴 수 있습니다",
                    "vi": "Người có quyền nuôi con có thể đưa ra mọi quyết định hàng ngày liên quan đến con",
                    "situation": "formal"
                }
            ],
            "relatedTerms": ["친권", "면접교섭권", "양육비", "자녀복리"]
        },
        {
            "slug": "tien-boi-thuong-tinh-than",
            "korean": "위자료",
            "vietnamese": "Tiền bồi thường tinh thần",
            "hanja": "慰藉料",
            "hanjaReading": "慰(위로할 위) + 藉(빌 자) + 料(헤아릴 료)",
            "pronunciation": "위자료",
            "meaningKo": "이혼 시 배우자의 유책행위로 인한 정신적 고통에 대한 금전 배상을 말합니다. 통역 시 베트남어 'bồi thường tinh thần'은 일반적 손해배상과 혼동될 수 있으므로, 혼인 파탄의 책임이 있는 배우자가 상대방에게 지급하는 특수한 배상임을 명확히 해야 합니다. 재산분할과는 별개로 산정됩니다.",
            "meaningVi": "Khoản bồi thường bằng tiền cho tổn thất tinh thần do hành vi lỗi của vợ hoặc chồng khi ly hôn. Được tính riêng với việc phân chia tài sản.",
            "context": "이혼 소송에서 배상 청구 및 산정 상황에서 사용",
            "culturalNote": "한국은 위자료를 이혼 소송의 일반적 구제 수단으로 인정하며, 외도, 가정폭력 등 유책행위가 명확할 경우 수천만 원에서 억 단위까지 인정됩니다. 베트남은 2014년 혼인가족법에서 정신적 손해배상을 규정하지만 실무상 금액이 적고 인정 범위가 좁습니다. 통역 시 한국의 높은 배상 수준을 설명해야 합니다.",
            "commonMistakes": [
                {
                    "mistake": "tiền ly hôn",
                    "correction": "tiền bồi thường tinh thần (위자료)",
                    "explanation": "'이혼 비용'으로 오해되며 정신적 손해배상의 의미가 전달되지 않습니다"
                },
                {
                    "mistake": "tiền cấp dưỡng",
                    "correction": "tiền bồi thường tinh thần (위자료) vs tiền cấp dưỡng (양육비)",
                    "explanation": "'부양비'는 양육비를 의미하며 위자료와 법적 성격이 완전히 다릅니다"
                },
                {
                    "mistake": "tiền bồi thường",
                    "correction": "tiền bồi thường tinh thần (위자료)",
                    "explanation": "일반 손해배상과 구분하지 못하여 혼인 파탄 책임의 특수성이 누락됩니다"
                }
            ],
            "examples": [
                {
                    "ko": "배우자의 외도로 인해 위자료 5천만 원을 청구합니다",
                    "vi": "Tôi yêu cầu 50 triệu won tiền bồi thường tinh thần do ngoại tình của vợ/chồng",
                    "situation": "formal"
                },
                {
                    "ko": "위자료는 얼마나 받을 수 있나요?",
                    "vi": "Tôi có thể nhận được bao nhiêu tiền bồi thường tinh thần?",
                    "situation": "onsite"
                },
                {
                    "ko": "위자료는 유책배우자가 상대방에게 지급하는 것입니다",
                    "vi": "Tiền bồi thường tinh thần là khoản vợ/chồng có lỗi phải trả cho bên kia",
                    "situation": "formal"
                }
            ],
            "relatedTerms": ["재산분할", "유책배우자", "정신적손해", "이혼소송"]
        },
        {
            "slug": "phan-chia-tai-san",
            "korean": "재산분할",
            "vietnamese": "Phân chia tài sản",
            "hanja": "財產分割",
            "hanjaReading": "財(재물 재) + 產(낳을 산) + 分(나눌 분) + 割(나눌 할)",
            "pronunciation": "재산분할",
            "meaningKo": "혼인 중 부부가 공동으로 형성한 재산을 이혼 시 나누는 제도입니다. 통역 시 한국은 명의와 무관하게 기여도에 따라 분할하며, 가사노동도 재산 형성 기여로 인정된다는 점을 명확히 해야 합니다. 위자료, 양육비와는 별개로 산정되며, 혼인 전 재산과 상속재산은 원칙적으로 제외됩니다.",
            "meaningVi": "Chế độ chia tài sản mà vợ chồng cùng tạo dựng trong thời gian hôn nhân khi ly hôn. Ở Hàn Quốc, chia theo mức đóng góp bất kể tên trên giấy tờ, và công việc nội trợ cũng được coi là đóng góp.",
            "context": "이혼 재산분할 협의 및 소송 상황에서 사용",
            "culturalNote": "한국 판례는 전업주부의 가사노동을 재산 형성 기여로 인정하여 통상 30~50% 비율로 재산분할을 인정합니다. 베트남은 2014년 혼인가족법 개정으로 공동재산 원칙을 강화했으나, 실무상 명의자 중심 판단이 많아 통역 시 한국의 실질적 기여도 중심 접근을 설명해야 합니다. 부동산 분할은 감정평가가 필수입니다.",
            "commonMistakes": [
                {
                    "mistake": "chia đôi tài sản",
                    "correction": "phân chia tài sản theo mức đóng góp",
                    "explanation": "'절반 나누기'는 기여도 무시하고 무조건 50:50으로 오해시킵니다"
                },
                {
                    "mistake": "chia tài sản chung",
                    "correction": "phân chia tài sản chung vợ chồng (재산분할)",
                    "explanation": "'공동재산 나누기'는 맞지만 법률 용어로는 '재산분할'이 정확합니다"
                },
                {
                    "mistake": "tài sản của ai thì người đó giữ",
                    "correction": "phân chia tài sản theo đóng góp, không phụ thuộc tên trên giấy tờ",
                    "explanation": "명의 중심 사고는 한국 재산분할 제도의 핵심인 기여도 원칙을 왜곡합니다"
                }
            ],
            "examples": [
                {
                    "ko": "혼인 중 형성한 부동산은 명의와 관계없이 재산분할 대상입니다",
                    "vi": "Bất động sản tạo dựng trong hôn nhân là đối tượng phân chia tài sản bất kể tên trên giấy tờ",
                    "situation": "formal"
                },
                {
                    "ko": "집이 남편 명의인데 제 몫도 받을 수 있나요?",
                    "vi": "Nhà ghi tên chồng nhưng tôi có được chia không?",
                    "situation": "onsite"
                },
                {
                    "ko": "재산분할 비율은 각자의 기여도를 고려하여 결정됩니다",
                    "vi": "Tỷ lệ phân chia tài sản được quyết định dựa trên mức đóng góp của mỗi người",
                    "situation": "formal"
                }
            ],
            "relatedTerms": ["기여도", "공동재산", "특유재산", "위자료", "감정평가"]
        },
        {
            "slug": "lenh-cam-tiep-can",
            "korean": "접근금지",
            "vietnamese": "Lệnh cấm tiếp cận",
            "hanja": "接近禁止",
            "hanjaReading": "接(이을 접) + 近(가까울 근) + 禁(금할 금) + 止(그칠 지)",
            "pronunciation": "접근금지",
            "meaningKo": "가정폭력 피해자를 보호하기 위해 가해자가 피해자에게 일정 거리 이내로 접근하는 것을 금지하는 법원 명령입니다. 통역 시 한국은 100미터 반경을 기준으로 하며, 위반 시 형사처벌이 가능하다는 점을 명확히 전달해야 합니다. 전화, 문자 등 간접 접촉도 금지 대상입니다.",
            "meaningVi": "Lệnh của tòa án cấm kẻ gây hại tiếp cận nạn nhân trong một khoảng cách nhất định để bảo vệ nạn nhân bạo lực gia đình. Ở Hàn Quốc tiêu chuẩn là bán kính 100 mét, vi phạm sẽ bị xử lý hình sự.",
            "context": "가정폭력 피해자 보호 명령 신청 및 집행 상황에서 사용",
            "culturalNote": "한국은 가정폭력특례법에 따라 경찰이 긴급 접근금지를 조치할 수 있으며, 법원의 정식 보호명령으로 최대 2년까지 연장 가능합니다. 베트남은 2007년 가정폭력방지법에서 유사 제도를 두고 있으나, 집행 인프라가 약해 실효성이 낮습니다. 통역 시 한국의 전자발찌 등 기술적 집행 수단을 설명해야 합니다.",
            "commonMistakes": [
                {
                    "mistake": "cấm gặp mặt",
                    "correction": "lệnh cấm tiếp cận (trong phạm vi 100m)",
                    "explanation": "'만남 금지'는 물리적 거리 개념이 누락되어 법적 효력이 불명확합니다"
                },
                {
                    "mistake": "không được đến gần",
                    "correction": "lệnh cấm tiếp cận (명령의 법적 강제력 강조)",
                    "explanation": "일상적 표현으로 법원 명령의 강제성과 처벌 가능성이 전달되지 않습니다"
                },
                {
                    "mistake": "tránh xa",
                    "correction": "lệnh cấm tiếp cận của tòa án",
                    "explanation": "'멀리하다'는 자발적 행위를 연상시켜 법적 명령의 성격이 사라집니다"
                }
            ],
            "examples": [
                {
                    "ko": "법원은 가해자에게 피해자 주거지 100m 이내 접근금지 명령을 내렸습니다",
                    "vi": "Tòa án đã ra lệnh cấm kẻ gây hại tiếp cận trong vòng 100m nơi ở của nạn nhân",
                    "situation": "formal"
                },
                {
                    "ko": "남편이 계속 따라와요. 접근금지 신청하고 싶어요",
                    "vi": "Chồng cứ theo dõi tôi. Tôi muốn xin lệnh cấm tiếp cận",
                    "situation": "onsite"
                },
                {
                    "ko": "접근금지 명령을 위반하면 2년 이하 징역에 처해질 수 있습니다",
                    "vi": "Vi phạm lệnh cấm tiếp cận có thể bị phạt tù đến 2 năm",
                    "situation": "formal"
                }
            ],
            "relatedTerms": ["보호명령", "가정폭력", "긴급임시조치", "퇴거명령"]
        },
        {
            "slug": "lenh-bao-ve",
            "korean": "보호명령",
            "vietnamese": "Lệnh bảo vệ",
            "hanja": "保護命令",
            "hanjaReading": "保(지킬 보) + 護(도울 호) + 命(목숨 명) + 令(하여금 령)",
            "pronunciation": "보호명령",
            "meaningKo": "가정폭력 피해자를 보호하기 위해 법원이 가해자에게 내리는 각종 제재 명령의 총칭입니다. 통역 시 접근금지, 전기통신 금지, 친권행사 제한, 상담·치료 수강명령 등 6가지 유형이 있으며, 피해자 신청만으로 발령 가능하다는 점을 명확히 전달해야 합니다. 형사처벌과 별개로 진행됩니다.",
            "meaningVi": "Tổng hợp các lệnh trừng phạt mà tòa án ra cho kẻ gây hại để bảo vệ nạn nhân bạo lực gia đình. Có 6 loại bao gồm cấm tiếp cận, cấm liên lạc, hạn chế quyền thân quyền, lệnh tham gia tư vấn/điều trị.",
            "context": "가정보호사건 심리 및 보호명령 신청 절차에서 사용",
            "culturalNote": "한국은 1998년 가정폭력특례법 제정으로 형사처벌 외에 보호명령 제도를 도입했습니다. 법원은 피해자 안전을 우선하여 신속하게 명령을 발령하며, 위반 시 2년 이하 징역 또는 2천만 원 이하 벌금이 부과됩니다. 베트남은 유사 제도가 있으나 법원 접근성이 낮아 활용도가 낮습니다. 통역 시 한국의 신속한 피해자 보호 시스템을 강조해야 합니다.",
            "commonMistakes": [
                {
                    "mistake": "lệnh bảo vệ nạn nhân",
                    "correction": "lệnh bảo vệ (법원이 가해자에게 내리는 명령)",
                    "explanation": "'피해자 보호 명령'은 명령 대상이 피해자인 것처럼 오해시킵니다"
                },
                {
                    "mistake": "quyết định bảo vệ",
                    "correction": "lệnh bảo vệ (강제력 있는 명령)",
                    "explanation": "'결정'은 강제성이 약한 행정처분으로 오해될 수 있습니다"
                },
                {
                    "mistake": "bảo vệ tạm thời",
                    "correction": "lệnh bảo vệ (최대 2년, 연장 가능)",
                    "explanation": "'임시 보호'는 긴급임시조치와 혼동되며 기간을 축소 왜곡합니다"
                }
            ],
            "examples": [
                {
                    "ko": "법원은 가해자에게 6개월간 피해자 주거 퇴거, 접근금지, 친권행사 제한 보호명령을 내렸습니다",
                    "vi": "Tòa án đã ra lệnh bảo vệ 6 tháng buộc kẻ gây hại rời khỏi nhà, cấm tiếp cận và hạn chế quyền thân quyền",
                    "situation": "formal"
                },
                {
                    "ko": "보호명령 신청하면 며칠이나 걸려요?",
                    "vi": "Xin lệnh bảo vệ mất bao lâu?",
                    "situation": "onsite"
                },
                {
                    "ko": "보호명령은 최대 2년까지 연장할 수 있습니다",
                    "vi": "Lệnh bảo vệ có thể gia hạn tối đa 2 năm",
                    "situation": "formal"
                }
            ],
            "relatedTerms": ["접근금지", "퇴거명령", "전기통신금지", "친권행사제한"]
        },
        {
            "slug": "tien-nuoi-con",
            "korean": "아동양육비",
            "vietnamese": "Tiền nuôi con",
            "hanja": "兒童養育費",
            "hanjaReading": "兒(아이 아) + 童(아이 동) + 養(기를 양) + 育(기를 육) + 費(비용 비)",
            "pronunciation": "아동양육비",
            "meaningKo": "부모의 이혼 후 자녀를 직접 양육하지 않는 부모가 자녀 양육을 위해 지급하는 비용입니다. 통역 시 한국은 표준 양육비 산정표에 따라 부모 소득과 자녀 연령을 기준으로 산정하며, 미지급 시 이행명령·감치·재산조회·명단공개 등 강력한 집행 수단이 있음을 명확히 전달해야 합니다. 양육권과 무관하게 부모 모두의 의무입니다.",
            "meaningVi": "Chi phí mà cha hoặc mẹ không trực tiếp nuôi con phải trả để nuôi dưỡng con sau ly hôn. Ở Hàn Quốc tính theo bảng chuẩn dựa trên thu nhập cha mẹ và độ tuổi con, có biện pháp cưỡng chế mạnh nếu không trả.",
            "context": "양육비 산정 및 이행 강제 절차에서 사용",
            "culturalNote": "한국은 2015년 양육비이행법 제정으로 미지급 양육비에 대한 강제집행이 대폭 강화되었습니다. 양육비이행관리원이 체납자 재산을 조회하고 명단을 공개하며, 감치(구금)까지 가능합니다. 베트남은 양육비 개념은 있으나 집행 인프라가 약해 실제 수령률이 낮습니다. 통역 시 한국의 적극적 국가 개입을 설명해야 합니다.",
            "commonMistakes": [
                {
                    "mistake": "tiền cấp dưỡng con",
                    "correction": "tiền nuôi con (아동양육비)",
                    "explanation": "'cấp dưỡng'은 성인 부양도 포함하여 미성년 자녀 양육비의 특수성이 사라집니다"
                },
                {
                    "mistake": "tiền cho con",
                    "correction": "tiền nuôi con (법적 의무)",
                    "explanation": "'자녀에게 주는 돈'은 자발적 증여처럼 들려 법적 강제성이 약화됩니다"
                },
                {
                    "mistake": "chi phí sinh hoạt",
                    "correction": "tiền nuôi con (교육·의료 포함)",
                    "explanation": "'생활비'는 범위가 좁아 교육비, 의료비 등이 누락됩니다"
                }
            ],
            "examples": [
                {
                    "ko": "표준 양육비 산정표에 따르면 월 소득 300만 원 시 자녀 1인당 약 50만 원입니다",
                    "vi": "Theo bảng tính chuẩn, thu nhập 3 triệu won/tháng thì tiền nuôi 1 con khoảng 500,000 won",
                    "situation": "formal"
                },
                {
                    "ko": "전 남편이 양육비를 안 줘요. 어떻게 받나요?",
                    "vi": "Chồng cũ không trả tiền nuôi con. Làm sao để nhận được?",
                    "situation": "onsite"
                },
                {
                    "ko": "양육비 미지급 시 재산조회 및 감치가 가능합니다",
                    "vi": "Nếu không trả tiền nuôi con có thể tra cứu tài sản và tạm giam",
                    "situation": "formal"
                }
            ],
            "relatedTerms": ["양육비이행관리원", "양육비산정표", "감치", "이행명령"]
        },
        {
            "slug": "quyen-than-quyen",
            "korean": "친권",
            "vietnamese": "Quyền thân quyền",
            "hanja": "親權",
            "hanjaReading": "親(친할 친) + 權(권리 권)",
            "pronunciation": "친꿘",
            "meaningKo": "부모가 미성년 자녀를 보호하고 교양할 권리이자 의무로서, 자녀의 신분·재산에 관한 포괄적 결정권을 포함합니다. 통역 시 한국은 친권과 양육권이 분리 가능하며, 친권은 법률행위 대리, 재산관리 등 법적 권한을, 양육권은 일상 양육의 권리를 의미한다는 점을 명확히 구분해야 합니다. 친권 남용 시 법원이 제한·상실을 선고할 수 있습니다.",
            "meaningVi": "Quyền và nghĩa vụ của cha mẹ để bảo vệ và giáo dục con chưa thành niên, bao gồm quyền quyết định toàn diện về nhân thân và tài sản của con. Ở Hàn Quốc có thể tách rời quyền thân quyền và quyền nuôi con.",
            "context": "가정법원 친권 제한·상실 사건 및 친권자 지정 절차에서 사용",
            "culturalNote": "한국은 전통적으로 부권 중심이었으나 2014년 민법 개정으로 양성평등 원칙이 강화되었습니다. 현재는 이혼 후에도 공동친권이 원칙이며, 양육권자와 친권자가 다를 수 있습니다. 베트남도 2014년 혼인가족법에서 공동친권을 규정하지만, 실무상 양육권자에게 친권도 귀속되는 경향이 강합니다. 통역 시 두 개념의 차이를 반드시 설명해야 합니다.",
            "commonMistakes": [
                {
                    "mistake": "quyền làm cha mẹ",
                    "correction": "quyền thân quyền (친권) - quyền pháp lý đối với con",
                    "explanation": "'부모 될 권리'는 포괄적이며 친권의 법적 정의가 누락됩니다"
                },
                {
                    "mistake": "quyền nuôi con",
                    "correction": "quyền thân quyền (친권) vs quyền nuôi con (양육권)",
                    "explanation": "양육권과 친권을 혼동하여 법적 권한의 범위를 왜곡합니다"
                },
                {
                    "mistake": "quyền giám hộ",
                    "correction": "quyền thân quyền (친권, 부모의 권리) vs quyền giám hộ (후견, 제3자)",
                    "explanation": "후견권은 부모 아닌 제3자의 권리로 친권과 법적 성격이 다릅니다"
                }
            ],
            "examples": [
                {
                    "ko": "친권자는 자녀의 법률행위를 대리하고 재산을 관리합니다",
                    "vi": "Người có quyền thân quyền đại diện hành vi pháp lý của con và quản lý tài sản",
                    "situation": "formal"
                },
                {
                    "ko": "친권 없이도 애를 키울 수 있나요?",
                    "vi": "Không có quyền thân quyền vẫn nuôi con được không?",
                    "situation": "onsite"
                },
                {
                    "ko": "친권 남용 시 법원은 친권 상실을 선고할 수 있습니다",
                    "vi": "Nếu lạm dụng quyền thân quyền, tòa án có thể tuyên bố mất quyền thân quyền",
                    "situation": "formal"
                }
            ],
            "relatedTerms": ["양육권", "친권제한", "친권상실", "법정대리"]
        },
        {
            "slug": "toa-an-gia-dinh",
            "korean": "가정법원",
            "vietnamese": "Tòa án gia đình",
            "hanja": "家庭法院",
            "hanjaReading": "家(집 가) + 庭(뜰 정) + 法(법 법) + 院(집 원)",
            "pronunciation": "까정버붠",
            "meaningKo": "혼인, 이혼, 친권, 후견, 가정폭력 등 가정 관련 사건을 전문적으로 다루는 특별 법원입니다. 통역 시 한국은 가정법원에서 조정 전치주의를 채택하여 소송 전 반드시 조정 절차를 거쳐야 하며, 조정위원이 합의를 유도한다는 점을 명확히 전달해야 합니다. 절차가 비공개이며 가족 관계 회복을 우선합니다.",
            "meaningVi": "Tòa án chuyên biệt xử lý các vụ việc liên quan gia đình như hôn nhân, ly hôn, quyền thân quyền, giám hộ, bạo lực gia đình. Ở Hàn Quốc áp dụng nguyên tắc hòa giải trước khi kiện, với thủ tục kín và ưu tiên phục hồi quan hệ gia đình.",
            "context": "가정 사건 소송 및 조정 절차 안내 상황에서 사용",
            "culturalNote": "한국은 1963년 가정법원을 설치하여 전문성을 강화했으며, 서울가정법원 등 대도시에 독립 법원이 있고 지방에는 가정지원이 있습니다. 조정위원은 법관이 아닌 가족문제 전문가로 구성되어 심리적 지원을 병행합니다. 베트남은 독립된 가정법원이 없고 인민법원에서 처리하여 전문성이 낮습니다. 통역 시 한국의 조정 중심 접근을 강조해야 합니다.",
            "commonMistakes": [
                {
                    "mistake": "tòa án dân sự",
                    "correction": "tòa án gia đình (가정 전문)",
                    "explanation": "민사법원은 일반 민사사건을 다루며 가정 전문성이 없습니다"
                },
                {
                    "mistake": "tòa án hôn nhân",
                    "correction": "tòa án gia đình (혼인 외에도 친권·후견 등 포괄)",
                    "explanation": "'혼인 법원'은 관할 범위를 혼인으로만 축소하여 오해를 줍니다"
                },
                {
                    "mistake": "phòng xét xử gia đình",
                    "correction": "tòa án gia đình (독립 법원)",
                    "explanation": "'가정 재판부'는 일반법원 내 부서로 오해되며 독립성이 약화됩니다"
                }
            ],
            "examples": [
                {
                    "ko": "이혼 소송은 가정법원에 제기하며 조정 절차를 먼저 거쳐야 합니다",
                    "vi": "Vụ kiện ly hôn nộp lên tòa án gia đình và phải trải qua thủ tục hòa giải trước",
                    "situation": "formal"
                },
                {
                    "ko": "가정법원은 어디 가면 되나요?",
                    "vi": "Tòa án gia đình ở đâu ạ?",
                    "situation": "onsite"
                },
                {
                    "ko": "가정법원 조정은 비공개로 진행됩니다",
                    "vi": "Hòa giải tại tòa án gia đình diễn ra kín",
                    "situation": "formal"
                }
            ],
            "relatedTerms": ["조정전치주의", "조정위원", "이혼조정", "가정보호사건"]
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
    print(f"✅ Added {len(filtered)} terms (가정폭력/가사법). Total: {len(data)}")

if __name__ == '__main__':
    main()
