#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""소년법 용어 추가 스크립트 (v6-i)"""

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
            "slug": "thieu-nien-pham",
            "korean": "소년범",
            "vietnamese": "Thiếu niên phạm",
            "hanja": "少年犯",
            "hanjaReading": "少(적을 소) + 年(해 년) + 犯(범할 범)",
            "pronunciation": "티에우니엔팜",
            "meaningKo": "만 10세 이상 19세 미만의 범죄 행위를 한 청소년을 지칭하는 법률 용어입니다. 한국에서는 소년법에 의해 성인과 다른 특별한 처우를 받으며, 교정과 교화를 통한 재사회화에 중점을 둡니다. 통역 시 베트남에서는 만 16세 미만을 형사책임을 지지 않는 연령으로 보는 등 형사책임 연령 기준이 다르므로 주의가 필요합니다. 베트남은 '미성년자 범죄'(tội phạm vị thành niên)로 표현하기도 하며, 한국의 소년법과 베트남의 아동법(Luật Trẻ em) 간 처벌과 보호의 철학적 차이를 명확히 설명해야 합니다.",
            "meaningVi": "Thuật ngữ pháp lý chỉ thanh thiếu niên từ đủ 10 đến dưới 19 tuổi có hành vi phạm tội. Ở Hàn Quốc, được áp dụng Luật Thiếu niên với chế độ xử lý đặc biệt khác với người lớn, tập trung vào tái hòa nhập xã hội thông qua giáo dục và cải tạo. Cần lưu ý Việt Nam quy định người dưới 16 tuổi không chịu trách nhiệm hình sự, có sự khác biệt về độ tuổi chịu trách nhiệm pháp lý.",
            "context": "형사법, 소년법, 가정법원",
            "culturalNote": "한국은 촉법소년(만 10~14세 미만)과 범죄소년(만 14세 이상)을 구분하여 전자는 형사처벌 대신 보호처분을 받으며, 후자는 형사처벌이 가능하지만 성인보다 감경됩니다. 베트남은 만 16세 미만은 형사책임을 지지 않고 교육적 조치를 우선하며, 만 16세 이상은 형사책임을 지되 관대한 처벌을 받습니다. 한국의 소년원 송치와 베트nam의 교육기관 송치는 목적과 운영 방식에서 차이가 있어 통역 시 이를 명확히 구분해야 합니다.",
            "commonMistakes": [
                {
                    "mistake": "모든 소년범을 'tội phạm nhỏ tuổi'로 직역",
                    "correction": "thiếu niên phạm 또는 vị thành niên phạm tội",
                    "explanation": "tội phạm nhỏ tuổi는 '어린 범죄자'라는 일상적 표현으로 법률 용어로는 부적절함"
                },
                {
                    "mistake": "소년범의 연령 범위를 베트남 기준으로 설명",
                    "correction": "한국 소년법상 만 10세 이상 19세 미만임을 명시",
                    "explanation": "양국의 연령 기준이 다르므로 어느 국가의 법체계인지 명확히 해야 함"
                },
                {
                    "mistake": "'소년범'을 'trẻ em phạm tội'로 번역",
                    "correction": "'thiếu niên phạm' 또는 'vị thành niên vi phạm pháp luật'",
                    "explanation": "trẻ em은 주로 유아~초등학생을 지칭하여 청소년 범죄자에는 부적합"
                }
            ],
            "examples": [
                {
                    "ko": "피고인은 범행 당시 만 17세의 소년범으로서 소년법이 적용됩니다.",
                    "vi": "Bị cáo là thiếu niên phạm 17 tuổi tại thời điểm phạm tội nên được áp dụng Luật Thiếu niên.",
                    "situation": "formal"
                },
                {
                    "ko": "소년범에 대해서는 구금보다 교육과 선도를 우선합니다.",
                    "vi": "Đối với thiếu niên phạm, ưu tiên giáo dục và cải tạo hơn là giam giữ.",
                    "situation": "formal"
                },
                {
                    "ko": "해당 사건은 소년범 전담 재판부에서 심리됩니다.",
                    "vi": "Vụ án này được xét xử tại tòa chuyên trách về thiếu niên phạm.",
                    "situation": "formal"
                }
            ],
            "relatedTerms": ["촉법소년", "보호처분", "소년원", "소년심판"]
        },
        {
            "slug": "xuc-phap-thieu-nien",
            "korean": "촉법소년",
            "vietnamese": "Xúc pháp thiếu niên",
            "hanja": "觸法少年",
            "hanjaReading": "觸(닿을 촉) + 法(법 법) + 少(적을 소) + 年(해 년)",
            "pronunciation": "쑥팝티에우니엔",
            "meaningKo": "만 10세 이상 14세 미만으로 형벌 법령에 저촉되는 행위를 한 소년을 의미하는 한국 소년법상의 용어입니다. 이들은 형사처벌 대상이 아니며 가정법원의 보호처분(감호, 보호관찰, 소년원 송치 등)을 받습니다. 통역 시 베트남에는 이에 정확히 대응하는 개념이 없으므로 '형사책임 연령 미만의 범법 청소년'으로 풀어서 설명해야 합니다. 최근 한국에서는 촉법소년 연령 하향 논쟁이 있으며, 이는 베트남의 만 16세 형사책임 기준과는 다른 맥락임을 주의해야 합니다.",
            "meaningVi": "Thuật ngữ trong Luật Thiếu niên Hàn Quốc chỉ trẻ em từ đủ 10 đến dưới 14 tuổi có hành vi vi phạm pháp luật hình sự. Họ không bị xử phạt hình sự mà được Tòa án gia đình áp dụng các biện pháp bảo vệ như quản chế, quan sát bảo vệ hoặc đưa vào cơ sở giáo dục thiếu niên. Việt Nam không có khái niệm tương ứng chính xác, cần giải thích là 'thiếu niên vi phạm pháp luật dưới độ tuổi chịu trách nhiệm hình sự'.",
            "context": "소년법, 가정법원, 형사정책",
            "culturalNote": "한국의 촉법소년 제도는 만 10~14세 미만 아동의 범죄 행위에 대해 형사책임을 묻지 않고 보호와 교육으로 대응하는 것이 핵심입니다. 베트남은 만 16세 미만 전체가 형사책임을 지지 않아 한국보다 보호 연령대가 넓지만, 실제 보호처분 체계는 한국이 더 세분화되어 있습니다. 최근 한국에서 촉법소년 연령을 만 13세 미만으로 낮추자는 논의가 있으나, 이는 베트남의 만 16세 기준과는 별개의 사회적 논쟁입니다.",
            "commonMistakes": [
                {
                    "mistake": "'촉법소년'을 'trẻ em phạm pháp'로 직역",
                    "correction": "'xúc pháp thiếu niên' 또는 'thiếu niên vi phạm pháp luật dưới tuổi chịu trách nhiệm hình sự'",
                    "explanation": "법률 용어로서의 정확성을 위해 한자 음차 또는 설명적 번역 필요"
                },
                {
                    "mistake": "촉법소년도 '범죄자'로 지칭",
                    "correction": "형사책임을 지지 않는 '보호 대상'임을 명시",
                    "explanation": "촉법소년은 법적으로 범죄자가 아니며 보호처분 대상자"
                },
                {
                    "mistake": "베트남의 만 16세 미만과 동일 개념으로 설명",
                    "correction": "한국의 촉법소년은 만 10~14세 미만이며 별도의 보호처분 체계 존재",
                    "explanation": "연령 범위와 법적 처우가 달라 혼동 방지 필요"
                }
            ],
            "examples": [
                {
                    "ko": "만 13세 피의자는 촉법소년에 해당하여 형사입건되지 않습니다.",
                    "vi": "Nghi phạm 13 tuổi là xúc pháp thiếu niên nên không bị khởi tố hình sự.",
                    "situation": "formal"
                },
                {
                    "ko": "촉법소년에 대해서는 가정법원이 보호처분을 결정합니다.",
                    "vi": "Đối với xúc pháp thiếu niên, Tòa án gia đình quyết định các biện pháp bảo vệ.",
                    "situation": "formal"
                },
                {
                    "ko": "촉법소년 연령 기준 개정안이 국회에 계류 중입니다.",
                    "vi": "Dự thảo sửa đổi tiêu chuẩn độ tuổi xúc pháp thiếu niên đang được Quốc hội xem xét.",
                    "situation": "formal"
                }
            ],
            "relatedTerms": ["소년범", "보호처분", "형사미성년자", "가정법원"]
        },
        {
            "slug": "bien-phap-bao-ve",
            "korean": "보호처분",
            "vietnamese": "Biện pháp bảo vệ",
            "hanja": "保護處分",
            "hanjaReading": "保(지킬 보) + 護(지킬 호) + 處(처리할 처) + 分(나눌 분)",
            "pronunciation": "비엔팝바오베",
            "meaningKo": "소년법에 따라 가정법원이 비행 청소년에게 내리는 처분으로, 형사처벌이 아닌 교육과 선도를 목적으로 합니다. 1호부터 10호까지 있으며, 보호자 감호 위탁, 수강명령, 사회봉사, 보호관찰, 소년원 송치 등이 포함됩니다. 통역 시 베트남의 '교육적 조치'(biện pháp giáo dục)와 혼동하지 않도록 주의해야 하며, 한국의 보호처분은 법원의 공식 결정이라는 점을 강조해야 합니다. 보호처분은 전과 기록으로 남지 않지만 재범 시 엄중한 처분을 받을 수 있어 그 법적 의미를 정확히 전달하는 것이 중요합니다.",
            "meaningVi": "Quyết định của Tòa án gia đình đối với thiếu niên vi phạm theo Luật Thiếu niên, nhằm mục đích giáo dục và cải tạo chứ không phải hình phạt. Gồm 10 loại từ cấp 1 đến 10, bao gồm giao cho người giám hộ, lệnh học tập, lao động công ích, quan sát bảo vệ, đưa vào cơ sở giáo dục thiếu niên, v.v. Không để lại tiền án nhưng nếu tái phạm sẽ bị xử lý nghiêm khắc hơn.",
            "context": "소년법, 가정법원, 소년사건",
            "culturalNote": "한국의 보호처분은 1호(보호자 감호 위탁)부터 10호(장기 소년원 송치)까지 단계별로 구성되며, 법원이 비행의 경중과 재범 가능성을 고려해 결정합니다. 베트남도 유사한 교육적 조치가 있으나 한국처럼 체계화되지 않았으며, 베트남에서는 가족과 지역사회의 역할이 더 강조됩니다. 한국에서는 보호처분을 받아도 전과로 남지 않지만, 보호처분 이력은 별도로 관리되어 재범 시 가중 사유가 됩니다. 통역 시 '처벌'이 아닌 '보호'의 개념임을 명확히 해야 오해를 방지할 수 있습니다.",
            "commonMistakes": [
                {
                    "mistake": "보호처분을 'hình phạt'(형벌)로 번역",
                    "correction": "'biện pháp bảo vệ'(보호 조치)로 번역",
                    "explanation": "보호처분은 형벌이 아니라 교육·선도 목적의 조치"
                },
                {
                    "mistake": "모든 보호처분을 동일한 수준으로 설명",
                    "correction": "1호부터 10호까지 경중이 다름을 명시",
                    "explanation": "보호자 감호부터 장기 소년원 송치까지 단계적 차이 존재"
                },
                {
                    "mistake": "보호처분을 '무죄'로 오인",
                    "correction": "비행 사실은 인정되나 형벌 대신 보호조치를 받는 것",
                    "explanation": "법적 책임은 인정되며 이행하지 않으면 소년원 송치 가능"
                }
            ],
            "examples": [
                {
                    "ko": "법원은 피고인에게 6개월 보호관찰 처분을 내렸습니다.",
                    "vi": "Tòa án đã ra quyết định biện pháp bảo vệ là quan sát bảo vệ 6 tháng đối với bị cáo.",
                    "situation": "formal"
                },
                {
                    "ko": "1호 처분인 보호자 감호 위탁으로 결정되었습니다.",
                    "vi": "Đã quyết định biện pháp bảo vệ cấp 1 là giao cho người giám hộ trông nom.",
                    "situation": "formal"
                },
                {
                    "ko": "보호처분 불이행 시 소년원 송치로 변경될 수 있습니다.",
                    "vi": "Nếu không tuân thủ biện pháp bảo vệ, có thể bị chuyển sang đưa vào cơ sở giáo dục thiếu niên.",
                    "situation": "formal"
                }
            ],
            "relatedTerms": ["보호관찰", "소년원", "수강명령", "가정법원"]
        },
        {
            "slug": "co-so-giao-duc-thieu-nien",
            "korean": "소년원",
            "vietnamese": "Cơ sở giáo dục thiếu niên",
            "hanja": "少年院",
            "hanjaReading": "少(적을 소) + 年(해 년) + 院(집 원)",
            "pronunciation": "꺼쏘자오죽티에우니엔",
            "meaningKo": "가정법원의 보호처분을 받은 비행 청소년을 수용하여 교육과 직업훈련을 실시하는 법무부 산하 교정시설입니다. 교육원(6개월 미만), 단기(6개월~1년), 장기(2년 이하)로 구분되며, 일반 교도소와 달리 중·고등학교 교육과정과 직업훈련을 병행합니다. 통역 시 베트남의 'trường giáo dưỡng'(교양학교)와 유사하지만, 한국의 소년원은 정규 학력을 인정받을 수 있고 직업자격증 취득이 가능하다는 점에서 차이가 있습니다. 소년원 수용은 형벌이 아닌 보호처분의 일종이므로 전과로 남지 않지만, 엄격한 생활 규율이 적용됩니다.",
            "meaningVi": "Cơ sở giáo dục trực thuộc Bộ Pháp vụ, nơi giam giữ và giáo dục thiếu niên vi phạm đã nhận biện pháp bảo vệ của Tòa án gia đình, thực hiện giáo dục văn hóa và đào tạo nghề. Phân loại thành trường giáo dục (dưới 6 tháng), ngắn hạn (6 tháng~1 năm), dài hạn (dưới 2 năm). Khác với nhà tù thông thường, kết hợp chương trình trung học phổ thông và đào tạo nghề, có thể được công nhận học vấn chính quy.",
            "context": "소년법, 보호처분, 교정행정",
            "culturalNote": "한국의 소년원은 단순 구금이 아닌 '교육과 교화'를 최우선으로 하며, 정규 학교 교육과 동일한 학력을 취득할 수 있고, 제빵, 미용, 용접 등 다양한 직업훈련 프로그램이 운영됩니다. 베트남의 'trường giáo dưỡng'은 주로 문제 행동 청소년의 교정에 초점을 맞추며, 학력 인정이나 직업훈련 체계가 한국만큼 체계적이지 않습니다. 한국에서는 소년원 수용 후에도 퇴원 후 사회 복귀를 돕는 사후관리 시스템(갱생보호)이 발달해 있어, 이 점도 통역 시 설명하면 좋습니다.",
            "commonMistakes": [
                {
                    "mistake": "소년원을 'nhà tù thiếu niên'(소년 교도소)로 번역",
                    "correction": "'cơ sở giáo dục thiếu niên' 또는 'viện giáo dục thiếu niên'",
                    "explanation": "소년원은 교도소가 아니라 교육기관의 성격이 강함"
                },
                {
                    "mistake": "소년원 송치를 '징역형'으로 설명",
                    "correction": "보호처분의 일종이며 전과가 아님을 명시",
                    "explanation": "형벌이 아니라 교육적 보호조치"
                },
                {
                    "mistake": "베트남의 'trường giáo dưỡng'과 완전히 동일하게 취급",
                    "correction": "한국 소년원은 학력 인정과 직업훈련이 체계화되어 있음을 구분",
                    "explanation": "시설의 목적과 프로그램 수준에 차이가 있음"
                }
            ],
            "examples": [
                {
                    "ko": "법원은 피고인에게 1년 단기 소년원 송치 처분을 내렸습니다.",
                    "vi": "Tòa án đã ra quyết định đưa bị cáo vào cơ sở giáo dục thiếu niên ngắn hạn 1 năm.",
                    "situation": "formal"
                },
                {
                    "ko": "소년원에서 고등학교 과정과 제과제빵 자격증을 취득했습니다.",
                    "vi": "Đã hoàn thành chương trình trung học phổ thông và lấy được chứng chỉ làm bánh tại cơ sở giáo dục thiếu niên.",
                    "situation": "informal"
                },
                {
                    "ko": "소년원 퇴원 후 갱생보호 프로그램이 제공됩니다.",
                    "vi": "Sau khi xuất viện từ cơ sở giáo dục thiếu niên, được cung cấp chương trình bảo vệ tái hòa nhập.",
                    "situation": "formal"
                }
            ],
            "relatedTerms": ["보호처분", "갱생보호", "보호관찰", "소년분류심사원"]
        },
        {
            "slug": "quan-sat-bao-ve",
            "korean": "보호관찰",
            "vietnamese": "Quan sát bảo vệ",
            "hanja": "保護觀察",
            "hanjaReading": "保(지킬 보) + 護(지킬 호) + 觀(볼 관) + 察(살필 찰)",
            "pronunciation": "꽌삿바오베",
            "meaningKo": "법원의 보호처분 또는 형의 집행유예·가석방 조건으로 부과되는 제도로, 보호관찰관이 대상자의 생활을 지도·감독하며 재범을 방지하는 사회 내 처우 방식입니다. 통역 시 단순한 '감시'가 아니라 '지도와 원호'가 결합된 개념임을 설명해야 하며, 베트남의 'quản chế'(관제)와는 달리 복지적 지원과 상담이 포함된다는 점을 강조해야 합니다. 보호관찰 기간 중 준수사항 위반 시 경고, 시설 수용 등 불이익이 따르며, 정기 출석, 거주지 이전 신고, 야간 외출 제한 등이 부과됩니다.",
            "meaningVi": "Chế độ được áp dụng như một biện pháp bảo vệ của tòa án hoặc điều kiện đình chỉ thi hành án, tạm tha, trong đó viên quan sát bảo vệ hướng dẫn và giám sát cuộc sống của đối tượng, ngăn ngừa tái phạm trong xã hội. Không chỉ là 'giám sát' mà kết hợp hướng dẫn và hỗ trợ phúc lợi. Nếu vi phạm các quy định trong thời gian quan sát bảo vệ, sẽ bị cảnh cáo, đưa vào cơ sở giam giữ, v.v.",
            "context": "소년법, 형법, 보호처분",
            "culturalNote": "한국의 보호관찰은 '사회 내 처우'의 핵심으로, 시설 수용 없이 일상생활을 유지하면서 재범을 방지하는 선진적 제도입니다. 보호관찰관은 단순 감시자가 아니라 상담자·멘토 역할을 하며, 취업 지원, 심리상담, 가족 관계 개선 등을 돕습니다. 베트남의 'quản chế'는 주로 이동과 활동의 제한에 초점이 맞춰져 있어 복지적 측면이 약하며, 한국의 보호관찰처럼 대상자의 사회 복귀를 적극 지원하는 체계는 아닙니다. 통역 시 이 차이를 명확히 전달해야 제도의 본질을 이해시킬 수 있습니다.",
            "commonMistakes": [
                {
                    "mistake": "보호관찰을 'giám sát'(감시)로만 번역",
                    "correction": "'quan sát bảo vệ' 또는 'quan sát và hỗ trợ'",
                    "explanation": "감시뿐 아니라 지도·원호의 복지적 기능 포함"
                },
                {
                    "mistake": "보호관찰을 '집행유예'와 동일하게 설명",
                    "correction": "집행유예의 조건이거나 독립적 보호처분으로 부과됨을 구분",
                    "explanation": "집행유예는 형 선고 유예이고, 보호관찰은 그 조건 또는 별도 처분"
                },
                {
                    "mistake": "베트남의 'quản chế'와 동일 개념으로 번역",
                    "correction": "한국의 보호관찰은 복지 지원이 강화된 제도임을 명시",
                    "explanation": "quản chế는 주로 행동 제한, 보호관찰은 재사회화 지원"
                }
            ],
            "examples": [
                {
                    "ko": "피고인에게 징역 1년에 집행유예 2년, 보호관찰 2년을 선고합니다.",
                    "vi": "Tuyên phạt bị cáo 1 năm tù, đình chỉ thi hành án 2 năm, quan sát bảo vệ 2 năm.",
                    "situation": "formal"
                },
                {
                    "ko": "보호관찰 기간 중 매월 보호관찰관을 만나 상담을 받아야 합니다.",
                    "vi": "Trong thời gian quan sát bảo vệ, phải gặp viên quan sát bảo vệ hàng tháng để nhận tư vấn.",
                    "situation": "onsite"
                },
                {
                    "ko": "준수사항을 위반하면 보호관찰이 취소될 수 있습니다.",
                    "vi": "Nếu vi phạm các quy định cần tuân thủ, quan sát bảo vệ có thể bị hủy bỏ.",
                    "situation": "formal"
                }
            ],
            "relatedTerms": ["집행유예", "가석방", "보호처분", "사회봉사명령"]
        },
        {
            "slug": "thieu-nien-xet-xu",
            "korean": "소년심판",
            "vietnamese": "Thiếu niên xét xử",
            "hanja": "少年審判",
            "hanjaReading": "少(적을 소) + 年(해 년) + 審(살필 심) + 判(판단할 판)",
            "pronunciation": "티에우니엔쎗쑤",
            "meaningKo": "가정법원 소년부에서 비행 청소년을 대상으로 진행하는 사법 절차로, 일반 형사재판과 달리 비공개로 진행되며 교육과 보호를 최우선으로 합니다. 소년심판은 조사, 심리, 처분의 단계로 이루어지며, 형사처벌보다는 보호처분을 통한 재사회화를 목표로 합니다. 통역 시 베트남의 청소년 사건 처리 절차와 비교하여, 한국은 전담 법원(가정법원)과 전문 판사가 배치되어 있어 체계적이라는 점을 강조해야 합니다. 소년심판에서는 피의자가 아닌 '소년'으로 호칭하고, 판사는 교육적·상담적 태도로 심리를 진행합니다.",
            "meaningVi": "Thủ tục tư pháp được tiến hành tại phòng thiếu niên Tòa án gia đình đối với thiếu niên vi phạm, khác với xét xử hình sự thông thường, được tiến hành kín và ưu tiên giáo dục và bảo vệ. Quy trình gồm điều tra, xét xử, quyết định biện pháp xử lý, nhằm mục tiêu tái hòa nhập xã hội thông qua biện pháp bảo vệ hơn là hình phạt. Trong thiếu niên xét xử, không gọi là 'nghi phạm' mà gọi là 'thiếu niên', và thẩm phán tiến hành với thái độ giáo dục và tư vấn.",
            "context": "소년법, 가정법원, 비행청소년",
            "culturalNote": "한국의 소년심판은 일반 형사재판과 명확히 구분되며, 비공개 원칙, 소년 중심 심리, 전문가 의견 청취(심리학자, 사회복지사 등)가 특징입니다. 재판 과정에서 소년의 가정환경, 교우관계, 성장 배경 등을 종합적으로 고려하여 '가장 적합한 교육적 처분'을 내립니다. 베트남에도 청소년 범죄자에 대한 별도 절차가 있으나, 한국처럼 전담 법원과 전문 인력이 체계적으로 운영되는 것은 아니며, 통역 시 이러한 제도적 차이를 명확히 전달해야 합니다.",
            "commonMistakes": [
                {
                    "mistake": "소년심판을 'tòa án hình sự thiếu niên'(소년 형사재판)으로 번역",
                    "correction": "'thiếu niên xét xử' 또는 'thủ tục xét xử thiếu niên tại Tòa án gia đình'",
                    "explanation": "형사재판이 아니라 보호절차 중심의 특별 심판"
                },
                {
                    "mistake": "소년심판을 공개 재판으로 설명",
                    "correction": "비공개 원칙이 적용됨을 명시",
                    "explanation": "소년의 인격권과 재사회화를 위해 비공개가 원칙"
                },
                {
                    "mistake": "소년심판에서 피의자를 'bị cáo'(피고인)로 지칭",
                    "correction": "'thiếu niên'(소년) 또는 'đối tượng'(대상자)",
                    "explanation": "소년심판에서는 범죄자가 아닌 보호 대상으로 호칭"
                }
            ],
            "examples": [
                {
                    "ko": "이 사건은 가정법원 소년부에서 소년심판 절차로 진행됩니다.",
                    "vi": "Vụ án này được tiến hành theo thủ tục thiếu niên xét xử tại phòng thiếu niên Tòa án gia đình.",
                    "situation": "formal"
                },
                {
                    "ko": "소년심판은 비공개로 진행되며 언론 보도가 제한됩니다.",
                    "vi": "Thiếu niên xét xử được tiến hành kín và hạn chế đưa tin trên báo chí.",
                    "situation": "formal"
                },
                {
                    "ko": "판사는 소년의 교육 환경과 가정 상황을 고려하여 처분을 결정했습니다.",
                    "vi": "Thẩm phán đã quyết định biện pháp xử lý sau khi xem xét môi trường giáo dục và hoàn cảnh gia đình của thiếu niên.",
                    "situation": "formal"
                }
            ],
            "relatedTerms": ["가정법원", "보호처분", "소년조사관", "비공개심리"]
        },
        {
            "slug": "thieu-nien-phi-hanh",
            "korean": "비행청소년",
            "vietnamese": "Thiếu niên phi hành",
            "hanja": "非行靑少年",
            "hanjaReading": "非(아닐 비) + 行(다닐 행) + 靑(푸를 청) + 少(적을 소) + 年(해 년)",
            "pronunciation": "티에우니엔피한",
            "meaningKo": "법령 위반, 도덕적 일탈, 가출, 무단결석 등 반사회적 행동을 하는 청소년을 포괄적으로 지칭하는 용어로, 범죄를 저지른 '소년범'뿐만 아니라 범죄 전 단계의 문제 행동을 보이는 청소년도 포함합니다. 통역 시 '비행(非行)'이 '범죄'보다 넓은 개념이며, 예방과 조기 개입이 중요하다는 맥락을 전달해야 합니다. 베트남어로는 'thiếu niên có hành vi lệch chuẩn' 또는 'thanh thiếu niên vi phạm'으로 표현할 수 있으나, 한국의 비행청소년 개념은 법적 처벌보다 교육적 개입을 우선한다는 점을 강조해야 합니다.",
            "meaningVi": "Thuật ngữ chỉ chung thanh thiếu niên có hành vi chống đối xã hội như vi phạm pháp luật, lệch chuẩn đạo đức, bỏ nhà ra đi, bỏ học, v.v., bao gồm không chỉ 'thiếu niên phạm' đã phạm tội mà cả thanh thiếu niên có hành vi vấn đề trước khi phạm tội. 'Phi hành' là khái niệm rộng hơn 'tội phạm', nhấn mạnh tầm quan trọng của phòng ngừa và can thiệp sớm.",
            "context": "소년법, 청소년복지, 예방교육",
            "culturalNote": "한국에서는 비행청소년을 범죄 청소년과 '우범소년'(범죄를 저지를 우려가 있는 소년)으로 구분하며, 후자에 대해서도 가정법원이 보호처분을 내릴 수 있습니다. 가출, 술·담배, 유흥업소 출입 등도 비행으로 간주되어 조기 개입 대상입니다. 베트남에서도 청소년 문제 행동에 대한 사회적 관심이 높지만, 한국처럼 법적 개입과 복지 지원이 체계화되지는 않았습니다. 통역 시 '비행'이 단순한 '범죄'가 아니라 더 넓은 개념임을 설명하고, 조기 발견과 교육적 개입의 중요성을 강조해야 합니다.",
            "commonMistakes": [
                {
                    "mistake": "비행청소년을 'thiếu niên tội phạm'(청소년 범죄자)로만 번역",
                    "correction": "'thiếu niên phi hành' 또는 'thanh thiếu niên có hành vi lệch chuẩn'",
                    "explanation": "비행은 범죄뿐 아니라 일탈 행동 전반을 포함하는 넓은 개념"
                },
                {
                    "mistake": "비행청소년을 모두 범죄자로 취급",
                    "correction": "범죄 전 단계의 문제 행동 청소년도 포함됨을 명시",
                    "explanation": "우범소년(범죄 우려가 있는 소년)도 비행청소년에 해당"
                },
                {
                    "mistake": "비행을 '도주', 'chạy trốn'으로 오역",
                    "correction": "'phi hành'(非行, 반사회적 행동)",
                    "explanation": "'비행'의 한자 의미를 이해하지 못한 오역"
                }
            ],
            "examples": [
                {
                    "ko": "비행청소년에 대한 조기 발견과 상담이 중요합니다.",
                    "vi": "Việc phát hiện sớm và tư vấn cho thiếu niên phi hành rất quan trọng.",
                    "situation": "formal"
                },
                {
                    "ko": "이 프로그램은 비행청소년의 사회 복귀를 돕습니다.",
                    "vi": "Chương trình này giúp thiếu niên phi hành tái hòa nhập xã hội.",
                    "situation": "informal"
                },
                {
                    "ko": "학교와 가정이 협력하여 비행청소년을 조기에 지도해야 합니다.",
                    "vi": "Nhà trường và gia đình cần hợp tác để hướng dẫn sớm thiếu niên phi hành.",
                    "situation": "formal"
                }
            ],
            "relatedTerms": ["우범소년", "소년범", "가출청소년", "학교밖청소년"]
        },
        {
            "slug": "bao-ve-canh-sinh",
            "korean": "갱생보호",
            "vietnamese": "Bảo vệ cánh sinh",
            "hanja": "更生保護",
            "hanjaReading": "更(다시 경) + 生(날 생) + 保(지킬 보) + 護(지킬 호)",
            "pronunciation": "바오베깐신",
            "meaningKo": "소년원, 교도소 등에서 출소한 사람이 사회에 성공적으로 복귀할 수 있도록 주거, 취업, 생계를 지원하는 제도입니다. 한국에는 법무부 산하 갱생보호공단과 민간 갱생보호단체가 있어 숙식 제공, 직업훈련, 취업 알선, 창업 지원 등을 수행합니다. 통역 시 단순한 '사후관리'를 넘어 적극적인 사회 복귀 지원 시스템임을 강조해야 하며, 베트남에는 이에 상응하는 체계적 제도가 부족하다는 점을 설명하면 좋습니다. 갱생보호는 재범 방지의 핵심 정책으로, 출소자의 자립 기반을 마련하는 것이 목표입니다.",
            "meaningVi": "Chế độ hỗ trợ về nhà ở, việc làm, sinh kế để người xuất viện từ cơ sở giáo dục thiếu niên hoặc xuất ngục có thể tái hòa nhập xã hội thành công. Ở Hàn Quốc có Công đoàn bảo vệ cánh sinh trực thuộc Bộ Pháp vụ và các tổ chức bảo vệ cánh sinh tư nhân thực hiện cung cấp chỗ ở, đào tạo nghề, giới thiệu việc làm, hỗ trợ khởi nghiệp, v.v. Là chính sách cốt lõi ngăn ngừa tái phạm, nhằm mục tiêu tạo nền tảng tự lập cho người xuất ngục.",
            "context": "형사정책, 사회복지, 재범방지",
            "culturalNote": "한국의 갱생보호 제도는 '처벌 후 방치'가 아닌 '재사회화 지원'이라는 선진적 형사정책의 일환입니다. 갱생보호시설에서는 무료 또는 저렴한 숙식을 제공하고, 취업 알선뿐 아니라 심리상담, 가족 관계 회복 지원까지 포함합니다. 특히 소년원 퇴원자에 대해서는 학업 복귀 지원, 대안교육 연계 등이 이루어집니다. 베트남에서는 출소자 지원이 주로 가족과 지역사회에 의존하며, 국가 차원의 체계적 지원은 미흡한 편입니다. 통역 시 한국의 갱생보호가 단순 선의가 아닌 법적·제도적 시스템임을 강조해야 합니다.",
            "commonMistakes": [
                {
                    "mistake": "갱생보호를 'chăm sóc sau phóng thích'(석방 후 돌봄)로만 번역",
                    "correction": "'bảo vệ cánh sinh' 또는 'hỗ trợ tái hòa nhập xã hội'",
                    "explanation": "단순 돌봄이 아니라 체계적 사회 복귀 지원 제도"
                },
                {
                    "mistake": "갱생보호를 자선사업으로 설명",
                    "correction": "법무부 산하 공식 제도이며 법적 근거가 있음을 명시",
                    "explanation": "갱생보호법에 기반한 국가 정책"
                },
                {
                    "mistake": "'갱생'을 'phục hồi'(회복)로만 번역",
                    "correction": "'cánh sinh'(更生, 다시 태어남)의 의미 전달",
                    "explanation": "단순 회복이 아니라 인생의 재출발이라는 철학적 의미 내포"
                }
            ],
            "examples": [
                {
                    "ko": "소년원 퇴원 후 갱생보호시설에서 6개월간 지원받았습니다.",
                    "vi": "Sau khi xuất viện từ cơ sở giáo dục thiếu niên, đã nhận hỗ trợ 6 tháng tại cơ sở bảo vệ cánh sinh.",
                    "situation": "informal"
                },
                {
                    "ko": "갱생보호공단에서 취업 알선과 주거 지원을 제공합니다.",
                    "vi": "Công đoàn bảo vệ cánh sinh cung cấp giới thiệu việc làm và hỗ trợ nhà ở.",
                    "situation": "formal"
                },
                {
                    "ko": "갱생보호는 재범 방지를 위한 핵심 정책입니다.",
                    "vi": "Bảo vệ cánh sinh là chính sách cốt lõi để ngăn ngừa tái phạm.",
                    "situation": "formal"
                }
            ],
            "relatedTerms": ["보호관찰", "사회복귀", "재범방지", "취업지원"]
        },
        {
            "slug": "thieu-nien-phan-loai-tra-xet",
            "korean": "소년분류심사",
            "vietnamese": "Thiếu niên phân loại tra xét",
            "hanja": "少年分類審査",
            "hanjaReading": "少(적을 소) + 年(해 년) + 分(나눌 분) + 類(무리 류) + 審(살필 심) + 査(조사할 사)",
            "pronunciation": "티에우니엔펀로아이짜쎗",
            "meaningKo": "가정법원의 결정으로 소년분류심사원에 수용된 청소년의 성격, 환경, 지능, 심리 상태 등을 과학적으로 조사하여 적합한 보호처분을 결정하기 위한 자료를 제공하는 절차입니다. 통상 4주 이내로 진행되며, 심리검사, 면담, 교육 프로그램 등이 실시됩니다. 통역 시 이는 처벌이 아니라 '개별 맞춤형 처우'를 위한 사전 조사 과정임을 강조해야 하며, 베트남에는 이처럼 체계화된 사전 심사 제도가 없다는 점을 설명하면 좋습니다. 분류심사 결과는 법원의 최종 처분 결정에 중요한 참고자료가 됩니다.",
            "meaningVi": "Thủ tục điều tra khoa học về tính cách, môi trường, trí tuệ, tâm lý của thiếu niên được đưa vào viện phân loại tra xét thiếu niên theo quyết định của Tòa án gia đình, nhằm cung cấp tài liệu để quyết định biện pháp bảo vệ thích hợp. Thường diễn ra trong vòng 4 tuần, thực hiện kiểm tra tâm lý, phỏng vấn, chương trình giáo dục, v.v. Không phải là hình phạt mà là quy trình điều tra trước để áp dụng 'xử lý phù hợp cá nhân'. Kết quả phân loại tra xét là tài liệu tham khảo quan trọng cho quyết định xử lý cuối cùng của tòa án.",
            "context": "소년법, 가정법원, 보호처분",
            "culturalNote": "한국의 소년분류심사원은 전국 10곳에 있으며, 임상심리사, 사회복지사, 교사 등 전문 인력이 청소년을 다각도로 평가합니다. 이는 '획일적 처벌'이 아닌 '개별화된 처우'라는 현대 소년사법의 이념을 실현하는 핵심 제도입니다. 베트남에는 이와 유사한 사전 심사 기관이 없으며, 주로 경찰 조사와 법원 심리만으로 처분이 결정됩니다. 통역 시 분류심사가 청소년의 인권을 보호하고 재범을 방지하기 위한 과학적 절차임을 강조하면, 제도의 선진성과 목적을 잘 전달할 수 있습니다.",
            "commonMistakes": [
                {
                    "mistake": "분류심사를 'kiểm tra phân loại'(단순 분류 검사)로 번역",
                    "correction": "'phân loại tra xét' 또는 'thẩm tra phân loại thiếu niên'",
                    "explanation": "단순 검사가 아니라 종합적 조사와 평가 과정"
                },
                {
                    "mistake": "분류심사원을 '구치소'로 설명",
                    "correction": "교정시설이 아닌 조사·평가 전문 기관임을 명시",
                    "explanation": "처벌 목적이 아니라 적합한 처우 결정을 위한 심사 기관"
                },
                {
                    "mistake": "분류심사를 법원 심리와 동일하게 설명",
                    "correction": "법원 결정 전 과학적 자료 수집 단계임을 구분",
                    "explanation": "심리는 법적 판단, 분류심사는 심리·사회적 조사"
                }
            ],
            "examples": [
                {
                    "ko": "법원은 피고인을 4주간 소년분류심사에 위탁했습니다.",
                    "vi": "Tòa án đã ủy thác bị cáo vào phân loại tra xét thiếu niên trong 4 tuần.",
                    "situation": "formal"
                },
                {
                    "ko": "분류심사 결과 피고인은 가정 환경 개선이 필요한 것으로 나타났습니다.",
                    "vi": "Kết quả phân loại tra xét cho thấy bị cáo cần cải thiện môi trường gia đình.",
                    "situation": "formal"
                },
                {
                    "ko": "분류심사원에서 심리검사와 직업적성검사를 실시합니다.",
                    "vi": "Tại viện phân loại tra xét, tiến hành kiểm tra tâm lý và kiểm tra năng khiếu nghề nghiệp.",
                    "situation": "onsite"
                }
            ],
            "relatedTerms": ["소년원", "보호처분", "가정법원", "심리검사"]
        },
        {
            "slug": "bao-ve-quan-sat",
            "korean": "보호관찰관",
            "vietnamese": "Viên bảo vệ quan sát",
            "hanja": "保護觀察官",
            "hanjaReading": "保(지킬 보) + 護(지킬 호) + 觀(볼 관) + 察(살필 찰) + 官(벼슬 관)",
            "pronunciation": "비엔바오베꽌삿",
            "meaningKo": "법무부 산하 보호관찰소에 소속되어 보호관찰 대상자를 지도·감독하고, 재범 방지를 위해 상담과 원호 서비스를 제공하는 공무원입니다. 단순한 감시자가 아니라 사회복지사, 상담자, 멘토의 역할을 겸하며, 대상자의 취업, 교육, 가족 관계 개선을 적극 지원합니다. 통역 시 베트남의 경찰 관리와 달리 복지적 지원 기능이 강조된 전문직임을 설명해야 하며, 보호관찰관은 대상자의 사회 복귀를 돕는 '파트너'라는 인식을 전달하는 것이 중요합니다.",
            "meaningVi": "Công chức thuộc Văn phòng quan sát bảo vệ trực thuộc Bộ Pháp vụ, có nhiệm vụ hướng dẫn và giám sát đối tượng quan sát bảo vệ, cung cấp dịch vụ tư vấn và hỗ trợ để ngăn ngừa tái phạm. Không chỉ là người giám sát mà còn kiêm vai trò nhân viên xã hội, tư vấn viên, người cố vấn, tích cực hỗ trợ đối tượng về việc làm, giáo dục, cải thiện quan hệ gia đình. Là nghề chuyên môn nhấn mạnh chức năng hỗ trợ phúc lợi, khác với quản lý công an.",
            "context": "보호관찰제도, 사회복지, 재범방지",
            "culturalNote": "한국의 보호관찰관은 5급 또는 7급 국가공무원으로, 사회복지, 심리, 법학 등 전문 지식을 갖춘 인력이 선발됩니다. 이들은 대상자와 정기 면담을 통해 생활 지도를 하고, 취업 지원, 심리상담, 가족 상담 등을 연계하며, 위기 상황 시 긴급 지원도 제공합니다. 베트남에는 이와 유사한 전문 직군이 없으며, 주로 경찰이나 지역 공무원이 관리 기능을 수행합니다. 통역 시 보호관찰관이 '감시자'가 아니라 '조력자'임을 강조하면, 제도의 목적과 대상자의 협조 필요성을 잘 전달할 수 있습니다.",
            "commonMistakes": [
                {
                    "mistake": "보호관찰관을 'cảnh sát giám sát'(감시 경찰)로 번역",
                    "correction": "'viên bảo vệ quan sát' 또는 'nhân viên quan sát bảo vệ'",
                    "explanation": "경찰이 아니라 법무부 소속 전문 공무원"
                },
                {
                    "mistake": "보호관찰관을 단순 감시자로 설명",
                    "correction": "지도·상담·지원 기능을 포함하는 복합적 역할임을 명시",
                    "explanation": "복지적 지원과 재사회화 조력이 주요 임무"
                },
                {
                    "mistake": "보호관찰관과 사회복지사를 동일하게 취급",
                    "correction": "보호관찰관은 법적 권한을 가진 공무원이며 준수사항 이행 감독 권한 있음",
                    "explanation": "복지사와 달리 법적 강제력을 행사할 수 있는 공권력 기관"
                }
            ],
            "examples": [
                {
                    "ko": "보호관찰관이 매월 가정 방문하여 생활 지도를 합니다.",
                    "vi": "Viên bảo vệ quan sát thăm gia đình hàng tháng để hướng dẫn cuộc sống.",
                    "situation": "informal"
                },
                {
                    "ko": "보호관찰관을 통해 취업 교육 프로그램에 참여할 수 있습니다.",
                    "vi": "Có thể tham gia chương trình đào tạo việc làm thông qua viên bảo vệ quan sát.",
                    "situation": "onsite"
                },
                {
                    "ko": "보호관찰관은 대상자의 사회 복귀를 적극 지원합니다.",
                    "vi": "Viên bảo vệ quan sát tích cực hỗ trợ tái hòa nhập xã hội của đối tượng.",
                    "situation": "formal"
                }
            ],
            "relatedTerms": ["보호관찰", "보호관찰소", "사회복귀", "사회내처우"]
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
