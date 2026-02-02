#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
법률 용어 추가 스크립트 - 중재/대체적분쟁해결 (Arbitration/ADR)
Theme: 중재/대체적분쟁해결 관련 법률 용어 10개
"""

import json
import os

# 파일 경로 설정
file_path = os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', 'data', 'terms', 'legal.json')

# 기존 데이터 로드
with open(file_path, 'r', encoding='utf-8') as f:
    data = json.load(f)  # data is a LIST

# 기존 slug 목록 추출
existing_slugs = {t['slug'] for t in data}

# 새로운 용어 리스트
new_terms = [
    {
        "slug": "trong-tai-thuong-mai",
        "korean": "상사중재",
        "vietnamese": "trọng tài thương mại",
        "hanja": "商事仲裁",
        "hanjaReading": "商(장사 상) 事(일 사) 仲(가운데 중) 裁(재판할 재)",
        "pronunciation": "상사중재",
        "meaningKo": "상사중재는 기업 간 상사 분쟁을 법원이 아닌 사적 중재기관에서 해결하는 제도입니다. 한국에서는 대한상사중재원(KCAB)이 대표적이며, 베트남은 VIAC(베트남국제중재센터)가 주요 기관입니다. 통역 시 주의할 점은 한국의 '상사'는 상업적 거래 전반을 포괄하지만, 베트남어 'thương mại'는 무역·매매를 중심으로 연상되기 쉬우므로 '기업 간 분쟁 해결'이라는 넓은 의미임을 명확히 해야 합니다. 계약서에 중재조항이 있으면 소송 대신 중재로 가야 하므로 중요한 구분입니다.",
        "meaningVi": "Trọng tài thương mại là chế độ giải quyết tranh chấp thương mại giữa các doanh nghiệp thông qua tổ chức trọng tài tư nhân thay vì tòa án. Ở Hàn Quốc, KCAB (Hiệp hội Trọng tài Thương mại Hàn Quốc) là cơ quan đại diện, còn ở Việt Nam là VIAC (Trung tâm Trọng tài Quốc tế Việt Nam). Khi hợp đồng có điều khoản trọng tài, tranh chấp phải được giải quyết bằng trọng tài thay vì kiện tụng.",
        "context": "기업 간 계약서, 국제무역, M&A 계약",
        "culturalNote": "한국은 중재를 분쟁해결의 효율적 대안으로 선호하며 대기업들이 자주 활용하는 반면, 베트남은 중재 문화가 비교적 최근에 발전하여 여전히 법원 소송을 선호하는 경향이 있습니다. VIAC의 역사는 1993년부터로 KCAB(1966년)보다 짧으며, 절차나 집행력에 대한 신뢰도 차이가 있습니다. 통역 시 양국의 중재제도 성숙도 차이를 인지하고, 베트남 측에 중재의 장점(신속성, 비밀유지, 전문성)을 충분히 설명해야 오해가 없습니다.",
        "commonMistakes": [
            {
                "mistake": "'trọng tài thương mại'를 단순 '무역 중재'로만 이해",
                "correction": "기업 간 모든 상사 분쟁 포괄(계약, 투자, 지재권 등)",
                "explanation": "베트남어 'thương mại'가 무역을 연상시키지만, 실제로는 기업 간 거래 전반을 의미하므로 범위를 명확히 해야 함"
            },
            {
                "mistake": "'중재'를 '조정(hòa giải)'과 혼동",
                "correction": "중재는 구속력 있는 판정, 조정은 합의 유도",
                "explanation": "중재판정은 법원 판결과 동일한 집행력이 있으나, 조정은 당사자 합의가 필수이므로 법적 효과가 다름"
            },
            {
                "mistake": "'KCAB'를 'Korean Commercial Arbitration Board'로 풀어 설명",
                "correction": "정확한 명칭은 'Korea Commercial Arbitration Board'",
                "explanation": "고유명사는 정확한 영문명을 사용해야 국제적으로 통용됨"
            },
            {
                "mistake": "중재기관 선택을 당연시하며 설명 생략",
                "correction": "계약서에 명시된 중재기관(KCAB, VIAC, ICC 등) 확인 필수",
                "explanation": "중재기관에 따라 규칙, 비용, 언어가 다르므로 계약 체결 시 신중히 선택해야 함"
            }
        ],
        "examples": [
            {
                "ko": "계약서에 '본 계약과 관련한 분쟁은 대한상사중재원의 상사중재규칙에 따라 중재로 해결한다'는 조항이 있습니다.",
                "vi": "Trong hợp đồng có điều khoản 'Mọi tranh chấp liên quan đến hợp đồng này sẽ được giải quyết bằng trọng tài thương mại theo quy tắc của KCAB'.",
                "situation": "formal"
            },
            {
                "ko": "중재는 소송보다 빠르고 비밀이 보장되어 기업들이 선호합니다.",
                "vi": "Trọng tài nhanh hơn và bảo mật hơn kiện tụng nên các doanh nghiệp ưa chuộng.",
                "situation": "informal"
            },
            {
                "ko": "상사중재 절차는 당사자가 합의한 규칙에 따라 진행됩니다.",
                "vi": "Thủ tục trọng tài thương mại được tiến hành theo quy tắc do các bên thỏa thuận.",
                "situation": "formal"
            }
        ],
        "relatedTerms": ["thoa-thuan-trong-tai", "trong-tai-vien", "phan-quyet-trong-tai", "viac"]
    },
    {
        "slug": "thoa-thuan-trong-tai",
        "korean": "중재합의",
        "vietnamese": "thỏa thuận trọng tài",
        "hanja": "仲裁合意",
        "hanjaReading": "仲(가운데 중) 裁(재판할 재) 合(합할 합) 意(뜻 의)",
        "pronunciation": "중재합의",
        "meaningKo": "중재합의는 당사자들이 분쟁을 법원이 아닌 중재로 해결하기로 약속한 계약입니다. 계약 체결 시 포함되는 '중재조항'과 분쟁 발생 후 작성하는 '중재계약'이 있습니다. 통역 시 주의할 점은 이 합의가 있으면 법원 소송권이 배제되므로 법적 구속력이 매우 강하다는 점을 명확히 해야 합니다. 베트남에서는 중재합의의 유효성 요건(서면, 명확한 범위)이 엄격하므로 계약서 작성 시 구체적으로 표현해야 나중에 분쟁이 없습니다.",
        "meaningVi": "Thỏa thuận trọng tài là hợp đồng mà các bên cam kết giải quyết tranh chấp bằng trọng tài thay vì tòa án. Có hai loại: điều khoản trọng tài (trong hợp đồng ban đầu) và hợp đồng trọng tài (ký sau khi phát sinh tranh chấp). Khi có thỏa thuận này, quyền kiện tụng tại tòa án bị loại trừ, do đó có hiệu lực pháp lý rất mạnh.",
        "context": "계약서 작성, 분쟁해결 협의",
        "culturalNote": "한국에서는 중재합의를 계약서의 표준 조항으로 인식하며 대부분 사전에 포함시키지만, 베트남에서는 중재합의의 법적 의미를 충분히 이해하지 못하고 형식적으로 서명하는 경우가 있습니다. 특히 베트남 중소기업은 중재 비용이나 절차에 대한 정보가 부족해 나중에 '소송으로 바꾸고 싶다'고 요청하기도 하는데, 이는 법적으로 불가능합니다. 통역 시 중재합의의 구속력과 포기되는 소송권을 명확히 전달해야 합니다.",
        "commonMistakes": [
            {
                "mistake": "'thỏa thuận'을 단순 '협의'로만 이해하고 법적 구속력 간과",
                "correction": "중재합의는 소송권 포기를 의미하는 법적 계약",
                "explanation": "일반 협의와 달리 중재합의는 법원 소송을 못하게 하므로 법적 효과가 매우 강함"
            },
            {
                "mistake": "구두 합의도 유효하다고 설명",
                "correction": "중재합의는 반드시 서면으로 작성해야 유효",
                "explanation": "양국 법 모두 서면 요건을 요구하며, 구두 합의는 중재 신청 시 무효 처리됨"
            },
            {
                "mistake": "'중재조항'과 '중재계약'을 구분하지 않음",
                "correction": "중재조항은 사전 합의, 중재계약은 사후 합의",
                "explanation": "시점의 차이가 있으며 실무에서는 중재조항이 훨씬 일반적임"
            },
            {
                "mistake": "중재합의 후에도 소송 가능하다고 오해",
                "correction": "유효한 중재합의가 있으면 법원은 소송을 각하함",
                "explanation": "중재합의는 소송권을 배제하는 효과가 있어 법원이 관할권을 거부함"
            }
        ],
        "examples": [
            {
                "ko": "계약 체결 전에 중재합의의 내용과 효과를 충분히 검토해야 합니다.",
                "vi": "Trước khi ký hợp đồng, cần xem xét kỹ nội dung và hiệu lực của thỏa thuận trọng tài.",
                "situation": "formal"
            },
            {
                "ko": "중재합의가 있으면 나중에 법원에 소송을 제기할 수 없습니다.",
                "vi": "Nếu có thỏa thuận trọng tài, không thể khởi kiện tại tòa án sau này.",
                "situation": "onsite"
            },
            {
                "ko": "이 조항은 중재합의이므로 신중하게 결정하시기 바랍니다.",
                "vi": "Điều khoản này là thỏa thuận trọng tài, xin hãy quyết định thận trọng.",
                "situation": "formal"
            }
        ],
        "relatedTerms": ["trong-tai-thuong-mai", "dieu-khoan-trong-tai", "trong-tai-vien", "phan-quyet-trong-tai"]
    },
    {
        "slug": "trong-tai-vien",
        "korean": "중재인",
        "vietnamese": "trọng tài viên",
        "hanja": "仲裁人",
        "hanjaReading": "仲(가운데 중) 裁(재판할 재) 人(사람 인)",
        "pronunciation": "중재인",
        "meaningKo": "중재인은 당사자들의 합의 또는 중재기관의 지정으로 선임되어 중재사건을 심리하고 판정을 내리는 사람입니다. 보통 1인 또는 3인으로 구성되며, 법률 전문가나 해당 분야 전문가가 맡습니다. 통역 시 주의할 점은 중재인의 자격과 선정 절차가 중재 결과에 큰 영향을 미치므로 당사자들이 신중히 선택해야 한다는 점을 전달해야 합니다. 한국에서는 변호사나 교수가 주로 중재인이 되지만, 베트남에서는 경력 있는 법조인이나 전 판사가 선호됩니다.",
        "meaningVi": "Trọng tài viên là người được các bên chọn hoặc do tổ chức trọng tài chỉ định để xét xử vụ tranh chấp và đưa ra phán quyết. Thường có 1 hoặc 3 trọng tài viên, là chuyên gia pháp lý hoặc chuyên gia trong lĩnh vực liên quan. Tư cách và quy trình lựa chọn trọng tài viên ảnh hưởng lớn đến kết quả, nên các bên cần chọn lựa thận trọng.",
        "context": "중재절차, 중재인 선정",
        "culturalNote": "한국에서는 중재인의 전문성과 경력을 중시하며, 대형 로펌 출신이나 대학교수가 선호됩니다. 3인 중재부일 경우 각 당사자가 1인씩 선정하고 의장 중재인을 합의로 정하는 방식이 일반적입니다. 베트남에서는 전직 판사나 검사 출신을 신뢰하는 경향이 있으며, 정부 관련 경력이 중시됩니다. 통역 시 중재인의 공정성과 독립성이 핵심 가치임을 강조하고, 당사자가 지명한 중재인도 편파적이어서는 안 된다는 점을 명확히 해야 합니다.",
        "commonMistakes": [
            {
                "mistake": "'trọng tài viên'을 '심판'으로 오역",
                "correction": "심판은 'trọng tài' (스포츠), 법적 중재인은 'trọng tài viên'",
                "explanation": "베트남어에서 같은 단어지만 법률 맥락에서는 'viên'을 붙여 전문성을 표현해야 함"
            },
            {
                "mistake": "당사자가 선정한 중재인은 '자기편'이라고 설명",
                "correction": "중재인은 독립적이고 공정해야 함, 당사자 이익 대변 아님",
                "explanation": "중재인은 판사와 같은 지위로 편파적이면 기피 사유가 됨"
            },
            {
                "mistake": "중재인 수를 임의로 정할 수 있다고 오해",
                "correction": "합의 또는 중재규칙에 따라 1인 또는 3인(홀수)으로 정함",
                "explanation": "짝수는 결정이 분열될 수 있어 보통 홀수로 구성함"
            },
            {
                "mistake": "중재인 선정이 중재기관의 전권이라고 설명",
                "correction": "당사자 합의가 우선, 합의 없을 때 기관이 지정",
                "explanation": "당사자 자율성이 중재의 핵심 원칙이므로 선정권을 먼저 부여함"
            }
        ],
        "examples": [
            {
                "ko": "중재인은 3인으로 구성하며, 각 당사자가 1인씩 선정하고 의장 중재인은 합의로 정합니다.",
                "vi": "Hội đồng trọng tài gồm 3 trọng tài viên, mỗi bên chọn 1 người và trọng tài viên chủ tọa do các bên thỏa thuận.",
                "situation": "formal"
            },
            {
                "ko": "이 분야 전문가를 중재인으로 선정하면 판정의 전문성이 높아집니다.",
                "vi": "Nếu chọn chuyên gia trong lĩnh vực này làm trọng tài viên, phán quyết sẽ có tính chuyên môn cao.",
                "situation": "informal"
            },
            {
                "ko": "중재인에게 이해관계가 있으면 기피 신청을 할 수 있습니다.",
                "vi": "Nếu trọng tài viên có quan hệ lợi ích, có thể yêu cầu loại trừ.",
                "situation": "onsite"
            }
        ],
        "relatedTerms": ["thoa-thuan-trong-tai", "phan-quyet-trong-tai", "trong-tai-thuong-mai", "hoi-dong-trong-tai"]
    },
    {
        "slug": "phan-quyet-trong-tai",
        "korean": "중재판정",
        "vietnamese": "phán quyết trọng tài",
        "hanja": "仲裁判定",
        "hanjaReading": "仲(가운데 중) 裁(재판할 재) 判(판단할 판) 定(정할 정)",
        "pronunciation": "중재판정",
        "meaningKo": "중재판정은 중재인이 내린 최종 결정으로, 법원 판결과 동일한 법적 구속력을 가집니다. 일단 확정되면 당사자는 이를 이행해야 하며, 불복 시 법원에 취소소송을 제기할 수 있으나 인정 사유가 매우 제한적입니다. 통역 시 주의할 점은 중재판정은 '최종적(final)'이며 항소가 없다는 특징을 명확히 전달해야 합니다. 한국 중재법과 베트남 중재법 모두 중재판정 취소 사유를 엄격히 제한하므로, 당사자들이 중재절차 중에 충분히 방어권을 행사해야 합니다.",
        "meaningVi": "Phán quyết trọng tài là quyết định cuối cùng của trọng tài viên, có hiệu lực pháp lý tương đương bản án của tòa án. Khi đã có hiệu lực, các bên phải thi hành, và nếu không phục chỉ có thể khởi kiện hủy tại tòa án với các lý do rất hạn chế. Đặc điểm quan trọng là phán quyết trọng tài là cuối cùng (final) và không có kháng cáo.",
        "context": "중재절차 종료, 판정 집행",
        "culturalNote": "한국에서는 중재판정의 최종성과 집행력을 높이 평가하며 분쟁 해결의 효율적 수단으로 인식하지만, 베트남에서는 아직까지 법원 판결보다 신뢰도가 낮고 집행 과정에서 어려움을 겪는 경우가 있습니다. 뉴욕협약 가입국 간에는 중재판정의 국제적 집행이 보장되지만, 실제로 베트남 법원에서 외국 중재판정 승인·집행이 지연되는 사례가 있습니다. 통역 시 중재판정의 법적 구속력과 불복 제한을 강조하되, 베트남 측의 집행 우려에 대해서도 현실적으로 대응해야 합니다.",
        "commonMistakes": [
            {
                "mistake": "'phán quyết'을 단순 '결정'으로 약화해 번역",
                "correction": "판결과 동일한 법적 효력이 있는 '판정'임을 명확히",
                "explanation": "베트남어에서도 'phán quyết'는 법적 구속력이 강한 용어이므로 격을 낮추지 말아야 함"
            },
            {
                "mistake": "중재판정에 항소할 수 있다고 오해",
                "correction": "항소 불가, 취소소송만 가능하며 사유 제한적",
                "explanation": "중재는 1심으로 종결되며 법원 소송과 달리 상소 절차가 없음"
            },
            {
                "mistake": "판정 불만 시 다시 중재 신청 가능하다고 설명",
                "correction": "동일 사안에 대해 재중재 불가 (一事不再理 원칙)",
                "explanation": "중재판정은 확정판결과 같아서 같은 분쟁을 다시 다룰 수 없음"
            },
            {
                "mistake": "중재판정 취소 사유를 넓게 설명",
                "correction": "절차상 하자, 공서양속 위반 등 극히 제한적",
                "explanation": "실체적 판단 오류는 취소 사유가 아니며 절차적 정당성만 법원이 심사함"
            }
        ],
        "examples": [
            {
                "ko": "중재판정이 내려지면 법원 판결과 동일한 효력으로 집행할 수 있습니다.",
                "vi": "Khi có phán quyết trọng tài, có thể thi hành với hiệu lực tương đương bản án của tòa án.",
                "situation": "formal"
            },
            {
                "ko": "이 판정에 불복하시면 60일 이내에 법원에 취소소송을 제기하셔야 합니다.",
                "vi": "Nếu không đồng ý với phán quyết này, phải khởi kiện hủy tại tòa án trong vòng 60 ngày.",
                "situation": "onsite"
            },
            {
                "ko": "중재판정은 최종적이라 항소가 없어 신속하게 분쟁이 종결됩니다.",
                "vi": "Phán quyết trọng tài là cuối cùng, không có kháng cáo nên tranh chấp được giải quyết nhanh chóng.",
                "situation": "informal"
            }
        ],
        "relatedTerms": ["trong-tai-vien", "thoa-thuan-trong-tai", "cong-nhan-phan-quyet", "huy-phan-quyet"]
    },
    {
        "slug": "thuong-luong",
        "korean": "교섭",
        "vietnamese": "thương lượng",
        "hanja": "交涉",
        "hanjaReading": "交(사귈 교) 涉(건널 섭)",
        "pronunciation": "교섭",
        "meaningKo": "교섭은 당사자들이 직접 대화를 통해 합의를 도출하는 가장 기본적인 분쟁해결 방법입니다. 법적 절차 이전 단계로, 비용이 들지 않고 관계 유지가 가능하다는 장점이 있습니다. 통역 시 주의할 점은 '협상'과 혼용되지만 법률 맥락에서는 '교섭'이 더 정확하며, 노사관계에서는 '단체교섭'처럼 특별한 의미를 가진다는 점입니다. 베트남에서는 'thương lượng'이 일상 협상부터 공식 교섭까지 광범위하게 쓰이므로, 법적 절차로서의 교섭인지 일반 협상인지 맥락을 명확히 해야 합니다.",
        "meaningVi": "Thương lượng là phương pháp giải quyết tranh chấp cơ bản nhất khi các bên trực tiếp đối thoại để đạt được thỏa thuận. Là giai đoạn trước thủ tục pháp lý, có ưu điểm là không tốn chi phí và có thể duy trì quan hệ. Trong tiếng Việt, 'thương lượng' được dùng rộng rãi từ đàm phán hàng ngày đến thương lượng chính thức, nên cần làm rõ ngữ cảnh.",
        "context": "분쟁 초기 단계, 계약 전 협의",
        "culturalNote": "한국에서는 교섭이 실패하면 바로 법적 절차(조정, 중재, 소송)로 넘어가는 경향이 있지만, 베트남에서는 관계 중심 문화로 인해 교섭이 오랜 기간 반복되는 경우가 많습니다. 베트남 비즈니스 문화에서는 직접적인 거절이나 법적 위협을 피하고 우회적으로 의사를 표현하므로, 한국 측이 '합의 가능'으로 오해할 수 있습니다. 통역 시 양측의 교섭 스타일 차이를 인지하고, 베트남 측의 완곡한 표현 뒤의 진짜 의도를 파악해 전달해야 합니다.",
        "commonMistakes": [
            {
                "mistake": "'thương lượng'을 단순 '흥정'으로 격하",
                "correction": "법적 의미의 교섭은 공식적 분쟁해결 절차",
                "explanation": "일상 협상과 달리 법률 맥락의 교섭은 증거 수집, 합의서 작성 등 법적 효과가 따름"
            },
            {
                "mistake": "교섭과 조정(hòa giải)을 혼동",
                "correction": "교섭은 당사자만 참여, 조정은 제3자 개입",
                "explanation": "교섭은 직접 대화, 조정은 중립적 조정인의 도움을 받는 절차로 구별됨"
            },
            {
                "mistake": "구두 교섭 결과도 법적 효력이 있다고 단정",
                "correction": "합의서를 서면으로 작성해야 집행 가능",
                "explanation": "교섭 과정은 구두로 하지만 최종 합의는 서면화해야 법적 효력이 생김"
            },
            {
                "mistake": "교섭 실패 시 바로 소송 간다고 압박",
                "correction": "조정, 중재 등 중간 절차도 고려 가능",
                "explanation": "ADR(대체적분쟁해결) 단계를 건너뛰면 관계 악화 및 비용 증가 우려"
            }
        ],
        "examples": [
            {
                "ko": "먼저 교섭을 통해 합의를 시도하고, 실패하면 조정을 거쳐 중재로 넘어갑니다.",
                "vi": "Trước tiên thử thương lượng để đạt thỏa thuận, nếu thất bại thì qua hòa giải rồi chuyển sang trọng tài.",
                "situation": "formal"
            },
            {
                "ko": "교섭 과정에서 합의한 내용은 반드시 서면으로 남겨야 합니다.",
                "vi": "Nội dung thỏa thuận trong quá trình thương lượng phải được lưu lại bằng văn bản.",
                "situation": "onsite"
            },
            {
                "ko": "양측이 직접 만나 교섭하면 서로 이해가 깊어져 합의 가능성이 높아집니다.",
                "vi": "Nếu hai bên gặp trực tiếp để thương lượng, sẽ hiểu nhau sâu hơn và khả năng thỏa thuận cao hơn.",
                "situation": "informal"
            }
        ],
        "relatedTerms": ["trung-gian-hoa-giai", "thoa-thuan", "dam-phan", "giai-quyet-tranh-chap"]
    },
    {
        "slug": "trung-gian-hoa-giai",
        "korean": "조정",
        "vietnamese": "trung gian hòa giải",
        "hanja": "調停",
        "hanjaReading": "調(고를 조) 停(그칠 정)",
        "pronunciation": "조정",
        "meaningKo": "조정은 제3자인 조정인이 분쟁 당사자 사이에서 합의를 이끌어내도록 돕는 절차입니다. 중재와 달리 조정인은 판정을 내리지 않고 당사자들이 스스로 합의하도록 유도합니다. 법원 조정과 사설 조정이 있으며, 합의가 성립하면 법적 효력이 생깁니다. 통역 시 주의할 점은 조정은 강제력이 없고 당사자의 자발적 합의가 핵심이라는 점을 강조해야 합니다. 베트남에서는 'hòa giải'가 전통적으로 마을 공동체의 분쟁해결 방식이었으므로 친숙하지만, 법적 조정과 민간 화해를 구분해야 합니다.",
        "meaningVi": "Trung gian hòa giải là thủ tục mà một bên thứ ba (người hòa giải) giúp các bên tranh chấp đạt được thỏa thuận. Khác với trọng tài, người hòa giải không đưa ra phán quyết mà chỉ hướng dẫn các bên tự thỏa thuận. Có hòa giải tòa án và hòa giải tư nhân, nếu thỏa thuận thành công sẽ có hiệu lực pháp lý. Hòa giải không mang tính cưỡng chế, tự nguyện của các bên là cốt lõi.",
        "context": "분쟁 중간 단계, 소송 전 절차",
        "culturalNote": "한국에서는 조정이 법원 소송 전 필수 절차(예: 가사조정, 민사조정)로 제도화되어 있으며, 조정 성립 시 판결과 동일한 효력을 갖습니다. 베트남에서는 'hòa giải'가 전통적으로 마을 어르신이나 지역 리더가 중재하는 비공식 방식으로 발전해왔으며, 현대 법제도에서도 소송 전 필수 절차로 요구되는 경우가 있습니다. 통역 시 법원 조정과 민간 화해를 구분하고, 조정 성립 시 법적 효력이 있다는 점을 명확히 해야 당사자들이 진지하게 임합니다.",
        "commonMistakes": [
            {
                "mistake": "'hòa giải'를 단순 '중재'로 오역",
                "correction": "중재(trọng tài)는 판정, 조정(hòa giải)은 합의 유도",
                "explanation": "조정은 당사자 합의가 필수이고 조정인은 결정권이 없음"
            },
            {
                "mistake": "조정 불성립 시 자동으로 소송 간다고 설명",
                "correction": "당사자가 소송 제기 여부 결정, 자동 아님",
                "explanation": "조정 실패는 합의 불발일 뿐, 소송 제기는 별도 선택 사항"
            },
            {
                "mistake": "조정인이 판결처럼 결정을 내릴 수 있다고 오해",
                "correction": "조정인은 중립적 촉진자, 결정권 없음",
                "explanation": "조정인의 역할은 대화 유도와 해결책 제시이며 강제력 없음"
            },
            {
                "mistake": "법원 조정과 사설 조정의 효력이 같다고 단정",
                "correction": "법원 조정은 판결과 동일 효력, 사설은 계약 효력",
                "explanation": "법원 조정 조서는 집행권원이지만 사설 조정 합의서는 일반 계약"
            }
        ],
        "examples": [
            {
                "ko": "소송 전에 법원 조정을 거치면 시간과 비용을 절약할 수 있습니다.",
                "vi": "Nếu qua hòa giải tòa án trước khi kiện, có thể tiết kiệm thời gian và chi phí.",
                "situation": "formal"
            },
            {
                "ko": "조정인이 양측의 의견을 듣고 합의안을 제시했습니다.",
                "vi": "Người hòa giải đã lắng nghe ý kiến hai bên và đề xuất phương án thỏa thuận.",
                "situation": "onsite"
            },
            {
                "ko": "조정이 성립하면 더 이상 소송할 필요가 없어요.",
                "vi": "Nếu hòa giải thành công thì không cần kiện tụng nữa.",
                "situation": "informal"
            }
        ],
        "relatedTerms": ["thuong-luong", "trong-tai-thuong-mai", "giai-quyet-tranh-chap", "nguoi-hoa-giai"]
    },
    {
        "slug": "cong-nhan-phan-quyet",
        "korean": "판정승인",
        "vietnamese": "công nhận phán quyết",
        "hanja": "判定承認",
        "hanjaReading": "判(판단할 판) 定(정할 정) 承(받들 승) 認(알 인)",
        "pronunciation": "판정승인",
        "meaningKo": "판정승인은 외국 중재판정을 자국 법원이 인정하여 집행력을 부여하는 절차입니다. 뉴욕협약(1958) 가입국 간에는 상호 승인 의무가 있어 외국 중재판정을 자국 판결처럼 집행할 수 있습니다. 통역 시 주의할 점은 승인 거부 사유가 매우 제한적(절차 하자, 공서양속 위반 등)이며 실체 재심사는 하지 않는다는 점입니다. 한국과 베트남 모두 뉴욕협약 가입국이므로 양국 중재판정은 원칙적으로 상호 집행 가능하지만, 실무에서는 베트남 법원의 승인 절차가 지연되는 경우가 있어 사전 준비가 필요합니다.",
        "meaningVi": "Công nhận phán quyết là thủ tục tòa án trong nước công nhận phán quyết trọng tài nước ngoài và cấp hiệu lực thi hành. Theo Công ước New York (1958), các nước thành viên có nghĩa vụ công nhận lẫn nhau, nên phán quyết trọng tài nước ngoài có thể được thi hành như bản án trong nước. Lý do từ chối công nhận rất hạn chế (khiếm khuyết thủ tục, vi phạm trật tự công cộng) và không xem xét lại nội dung.",
        "context": "국제중재, 판정집행",
        "culturalNote": "한국 법원은 뉴욕협약에 따라 외국 중재판정을 신속히 승인하는 편이며, 승인 거부율이 낮습니다. 베트남 법원도 협약 가입국이지만 실무에서는 행정 절차가 복잡하고 법원의 재량 해석이 넓어 승인이 지연되거나 거부되는 사례가 있습니다. 특히 베트남 정부 관련 분쟁에서는 공공이익이나 국가 주권을 이유로 승인을 거부할 가능성이 높습니다. 통역 시 양국의 승인 실무 차이를 설명하고, 베트남에서 판정 집행 시 현지 법률자문을 받아야 한다고 조언하는 것이 중요합니다.",
        "commonMistakes": [
            {
                "mistake": "'công nhận'을 단순 '인정'으로 약화",
                "correction": "법원의 공식 승인 절차로 집행력 부여",
                "explanation": "일반적 인정이 아니라 법적 효력을 생성하는 공식 절차임"
            },
            {
                "mistake": "뉴욕협약 가입국이면 자동 승인된다고 설명",
                "correction": "원칙적 승인 의무지만 예외 사유로 거부 가능",
                "explanation": "절차 하자, 공서양속 위반 등 협약상 예외 사유가 있으면 거부됨"
            },
            {
                "mistake": "승인 거부 시 실체 재심리 가능하다고 오해",
                "correction": "승인 단계에서는 절차적 정당성만 심사",
                "explanation": "중재판정의 옳고 그름은 심사하지 않고 절차적 요건만 확인함"
            },
            {
                "mistake": "판정승인이 필요 없다고 단정",
                "correction": "집행을 위해서는 반드시 집행국 법원의 승인 필요",
                "explanation": "외국 판정은 자동 집행력이 없어 집행 전 승인 절차 필수"
            }
        ],
        "examples": [
            {
                "ko": "한국 중재판정을 베트남에서 집행하려면 베트남 법원의 판정승인을 받아야 합니다.",
                "vi": "Để thi hành phán quyết trọng tài Hàn Quốc tại Việt Nam, phải được tòa án Việt Nam công nhận phán quyết.",
                "situation": "formal"
            },
            {
                "ko": "뉴욕협약에 따라 외국 중재판정을 승인하는 것이 원칙입니다.",
                "vi": "Theo Công ước New York, việc công nhận phán quyết trọng tài nước ngoài là nguyên tắc.",
                "situation": "formal"
            },
            {
                "ko": "판정승인이 거부되면 집행할 수 없으니 절차를 신중히 준비해야 합니다.",
                "vi": "Nếu bị từ chối công nhận phán quyết thì không thể thi hành, nên phải chuẩn bị thủ tục cẩn thận.",
                "situation": "onsite"
            }
        ],
        "relatedTerms": ["phan-quyet-trong-tai", "thi-hanh-phan-quyet", "cong-uoc-new-york", "nuoc-ngoai"]
    },
    {
        "slug": "dieu-khoan-trong-tai",
        "korean": "중재조항",
        "vietnamese": "điều khoản trọng tài",
        "hanja": "仲裁條項",
        "hanjaReading": "仲(가운데 중) 裁(재판할 재) 條(가지 조) 項(항목 항)",
        "pronunciation": "중재조항",
        "meaningKo": "중재조항은 계약서에 미리 포함시키는 중재합의 조항으로, 향후 분쟁 발생 시 소송 대신 중재로 해결하기로 약속하는 내용입니다. 중재기관, 중재지, 준거법, 중재인 수 등을 명시하며, 이 조항이 있으면 법원 소송이 배제됩니다. 통역 시 주의할 점은 이 조항의 유효성과 구체성이 매우 중요하며, 모호하면 나중에 분쟁이 생긴다는 점을 강조해야 합니다. 특히 국제계약에서는 중재지와 준거법 선택이 판정 결과에 큰 영향을 미치므로 신중히 협상해야 합니다.",
        "meaningVi": "Điều khoản trọng tài là điều khoản thỏa thuận trọng tài được đưa vào hợp đồng từ trước, cam kết rằng nếu phát sinh tranh chấp sẽ giải quyết bằng trọng tài thay vì kiện tụng. Cần ghi rõ tổ chức trọng tài, địa điểm trọng tài, luật áp dụng, số lượng trọng tài viên. Khi có điều khoản này, không được kiện tại tòa án. Tính hiệu lực và tính cụ thể của điều khoản rất quan trọng, nếu mơ hồ sẽ gây tranh chấp sau này.",
        "context": "계약서 작성, 국제계약",
        "culturalNote": "한국 기업들은 국제계약 시 중재조항을 표준으로 포함하며, 대형 로펌의 검토를 거쳐 정교하게 작성하는 편입니다. 반면 베트남 중소기업은 중재조항의 중요성을 충분히 인지하지 못하고 상대방이 제시한 표준 조항을 그대로 수용하는 경우가 많습니다. 나중에 분쟁 발생 시 불리한 중재기관이나 준거법이 적용되어 곤란을 겪기도 합니다. 통역 시 중재조항이 단순 형식이 아니라 분쟁 발생 시 게임의 룰을 정하는 핵심 조항임을 강조하고, 양측이 대등하게 협상하도록 유도해야 합니다.",
        "commonMistakes": [
            {
                "mistake": "'điều khoản'을 단순 '조건'으로 격하",
                "correction": "법적 구속력 있는 '조항'",
                "explanation": "계약 조건이 아니라 분쟁해결 절차를 정하는 독립된 법적 조항임"
            },
            {
                "mistake": "중재조항을 나중에 수정할 수 있다고 설명",
                "correction": "양 당사자 합의 없으면 일방 수정 불가",
                "explanation": "중재조항은 계약의 일부로 양측 동의 없이 변경 불가능"
            },
            {
                "mistake": "중재조항 없이도 중재 신청 가능하다고 오해",
                "correction": "중재합의 없으면 중재 불가, 소송만 가능",
                "explanation": "중재는 합의 기반 절차로 조항이나 별도 합의 없으면 진행 못함"
            },
            {
                "mistake": "중재조항이 짧고 간단할수록 좋다고 설명",
                "correction": "구체적으로 작성해야 분쟁 여지 없음",
                "explanation": "모호한 조항은 관할, 준거법 등에서 다시 분쟁 야기할 수 있음"
            }
        ],
        "examples": [
            {
                "ko": "계약서에 '분쟁은 대한상사중재원 규칙에 따라 서울에서 중재로 해결한다'는 중재조항을 넣었습니다.",
                "vi": "Trong hợp đồng đã đưa điều khoản trọng tài 'Tranh chấp sẽ được giải quyết bằng trọng tài tại Seoul theo quy tắc của KCAB'.",
                "situation": "formal"
            },
            {
                "ko": "중재조항이 불명확하면 나중에 어느 기관에서 중재할지 다시 다툴 수 있습니다.",
                "vi": "Nếu điều khoản trọng tài không rõ ràng, sau này có thể tranh chấp lại về tổ chức trọng tài nào.",
                "situation": "onsite"
            },
            {
                "ko": "중재조항에 중재지와 준거법을 명확히 써야 분쟁이 없어요.",
                "vi": "Phải ghi rõ địa điểm trọng tài và luật áp dụng trong điều khoản trọng tài thì mới không có tranh chấp.",
                "situation": "informal"
            }
        ],
        "relatedTerms": ["thoa-thuan-trong-tai", "trong-tai-thuong-mai", "luat-ap-dung", "dia-diem-trong-tai"]
    },
    {
        "slug": "luat-ap-dung",
        "korean": "준거법",
        "vietnamese": "luật áp dụng",
        "hanja": "準據法",
        "hanjaReading": "準(준할 준) 據(근거 거) 法(법 법)",
        "pronunciation": "준거법",
        "meaningKo": "준거법은 국제계약이나 중재에서 분쟁 해결의 기준이 되는 법률을 말합니다. 당사자들이 계약서에서 어느 나라 법을 적용할지 합의하며, 이에 따라 권리와 의무가 달라집니다. 통역 시 주의할 점은 준거법은 계약의 실체적 내용(권리·의무)을 규율하는 법이고, 중재지법은 중재 절차를 규율하는 법으로 구분된다는 점입니다. 한국법과 베트남법은 계약 해석, 손해배상 범위, 불가항력 등에서 차이가 있으므로 어느 법을 선택하느냐가 분쟁 결과에 큰 영향을 미칩니다.",
        "meaningVi": "Luật áp dụng là pháp luật được sử dụng làm chuẩn để giải quyết tranh chấp trong hợp đồng quốc tế hoặc trọng tài. Các bên thỏa thuận trong hợp đồng sẽ áp dụng luật nước nào, và quyền lợi cũng như nghĩa vụ sẽ khác nhau tùy theo đó. Luật áp dụng điều chỉnh nội dung thực chất (quyền, nghĩa vụ) của hợp đồng, còn luật tại địa điểm trọng tài điều chỉnh thủ tục trọng tài, cần phân biệt rõ.",
        "context": "국제계약, 중재조항",
        "culturalNote": "한국 기업들은 국제계약 시 자국법(한국 민법)을 준거법으로 정하려는 경향이 있으며, 이는 법률 예측 가능성과 자문 비용 절감을 위함입니다. 베트남 기업도 마찬가지로 베트남 민법을 선호하며, 외국법 적용 시 현지 법률자문 비용이 증가합니다. 실무에서는 제3국 법(예: 싱가포르법, 영국법)을 중립적 준거법으로 합의하기도 합니다. 통역 시 준거법 선택이 단순한 형식이 아니라 분쟁 시 승패를 좌우할 수 있는 핵심 협상 사항임을 양측에 명확히 전달해야 합니다.",
        "commonMistakes": [
            {
                "mistake": "'luật áp dụng'와 '법원 관할'을 혼동",
                "correction": "준거법은 실체법, 관할은 절차적 권한",
                "explanation": "준거법은 어느 나라 법을 적용할지, 관할은 어느 법원/중재기관에서 다룰지를 정하는 것으로 별개 개념"
            },
            {
                "mistake": "중재지법이 자동으로 준거법이 된다고 설명",
                "correction": "중재지법은 절차법, 준거법은 별도 합의 필요",
                "explanation": "중재를 서울에서 해도 준거법은 베트남법일 수 있음"
            },
            {
                "mistake": "준거법 합의 없으면 중재 못 한다고 오해",
                "correction": "합의 없으면 중재인/법원이 관련 법률 선택",
                "explanation": "준거법 미합의 시 국제사법 원칙에 따라 결정되므로 중재 진행 가능"
            },
            {
                "mistake": "준거법이 모든 쟁점에 적용된다고 단정",
                "correction": "계약 조항별로 다른 준거법 적용 가능(분할 준거법)",
                "explanation": "예: 제조물 책임은 A국법, 지급 조건은 B국법 적용 가능"
            }
        ],
        "examples": [
            {
                "ko": "이 계약의 준거법은 대한민국 법률로 하며, 해석과 이행은 한국 민법에 따릅니다.",
                "vi": "Luật áp dụng cho hợp đồng này là pháp luật Hàn Quốc, việc giải thích và thi hành theo Dân luật Hàn Quốc.",
                "situation": "formal"
            },
            {
                "ko": "준거법을 베트남 법으로 정하면 베트남 변호사 자문이 필요합니다.",
                "vi": "Nếu chọn luật Việt Nam làm luật áp dụng, cần tư vấn luật sư Việt Nam.",
                "situation": "onsite"
            },
            {
                "ko": "준거법이 다르면 손해배상 범위나 계약 해제 요건이 달라질 수 있어요.",
                "vi": "Nếu luật áp dụng khác nhau, phạm vi bồi thường thiệt hại hay điều kiện hủy hợp đồng có thể khác.",
                "situation": "informal"
            }
        ],
        "relatedTerms": ["dieu-khoan-trong-tai", "dia-diem-trong-tai", "hop-dong-quoc-te", "tranh-chap"]
    },
    {
        "slug": "phan-quyet-chung-tham",
        "korean": "최종판정",
        "vietnamese": "phán quyết chung thẩm",
        "hanja": "最終判定",
        "hanjaReading": "最(가장 최) 終(마칠 종) 判(판단할 판) 定(정할 정)",
        "pronunciation": "최종판정",
        "meaningKo": "최종판정은 중재 절차에서 내려지는 마지막 결정으로, 이후 항소나 재심이 불가능한 종국적 판단입니다. 중재의 핵심 특징인 '일회성(one-shot)'을 상징하며, 당사자는 이 판정에 구속되어 이행해야 합니다. 통역 시 주의할 점은 '최종(final)'의 의미가 단순히 마지막이 아니라 '더 이상 다툴 수 없는 확정'이라는 법적 효과를 가진다는 점을 명확히 해야 합니다. 취소소송은 가능하지만 사유가 극히 제한적이므로 실질적으로 번복이 어렵습니다.",
        "meaningVi": "Phán quyết chung thẩm là quyết định cuối cùng trong thủ tục trọng tài, sau đó không thể kháng cáo hay xem xét lại. Đây là biểu tượng của đặc điểm cốt lõi của trọng tài là 'một lần giải quyết (one-shot)', các bên bị ràng buộc và phải thi hành. Ý nghĩa của 'chung thẩm (cuối cùng)' không đơn thuần là lần cuối mà có hiệu lực pháp lý là 'không thể tranh chấp thêm'.",
        "context": "중재절차 종료, 판정 확정",
        "culturalNote": "한국에서는 중재의 최종성을 신뢰하고 판정 후 신속히 이행하는 문화가 정착되어 있으나, 베트남에서는 패소 측이 판정 불복을 시도하며 집행을 지연시키는 경우가 종종 있습니다. 법원에 취소소송을 제기하거나 집행 단계에서 이의를 제기하는 등의 전략을 쓰는데, 이는 중재의 최종성 원칙에 어긋나지만 실무에서 발생합니다. 통역 시 최종판정의 구속력과 집행 필요성을 강조하고, 베트남 측의 불복 가능성에 대비해 집행 전략을 미리 준비하도록 조언해야 합니다.",
        "commonMistakes": [
            {
                "mistake": "'phán quyết chung thẩm'을 '최종심 판결'로 오역",
                "correction": "중재는 1심으로 끝, '최종판정'이 정확",
                "explanation": "법원의 상소심 개념이 아니라 중재의 일회성을 나타내는 표현"
            },
            {
                "mistake": "최종판정 후에도 재심 가능하다고 오해",
                "correction": "재심 제도 없음, 취소소송만 극히 제한적 가능",
                "explanation": "중재는 최종성이 원칙이며 실체 재심사는 불가능"
            },
            {
                "mistake": "중재인이 판정을 변경할 수 있다고 설명",
                "correction": "일단 선고된 최종판정은 중재인도 변경 불가",
                "explanation": "오기 정정은 가능하지만 판단 내용 변경은 불가능"
            },
            {
                "mistake": "최종판정과 잠정조치를 동일시",
                "correction": "잠정조치는 임시, 최종판정은 확정 종국 결정",
                "explanation": "잠정조치는 절차 중 임시 명령, 최종판정은 분쟁 해결의 마지막 판단"
            }
        ],
        "examples": [
            {
                "ko": "중재인이 최종판정을 선고하면 더 이상 항소할 수 없으며 당사자는 이를 이행해야 합니다.",
                "vi": "Khi trọng tài viên tuyên phán quyết chung thẩm, không thể kháng cáo nữa và các bên phải thi hành.",
                "situation": "formal"
            },
            {
                "ko": "최종판정이 나왔으니 이제 판정 내용에 따라 금액을 지급하셔야 합니다.",
                "vi": "Đã có phán quyết chung thẩm, bây giờ phải thanh toán số tiền theo nội dung phán quyết.",
                "situation": "onsite"
            },
            {
                "ko": "중재의 장점은 최종판정이 빨리 나와서 분쟁이 오래 끌지 않는다는 거예요.",
                "vi": "Ưu điểm của trọng tài là phán quyết chung thẩm ra nhanh nên tranh chấp không kéo dài.",
                "situation": "informal"
            }
        ],
        "relatedTerms": ["phan-quyet-trong-tai", "khang-cao", "huy-phan-quyet", "thi-hanh-phan-quyet"]
    }
]

# 중복 제거 (기존 slug와 비교)
new_terms_filtered = [t for t in new_terms if t['slug'] not in existing_slugs]

# 데이터에 추가
data.extend(new_terms_filtered)

# 파일에 저장
with open(file_path, 'w', encoding='utf-8') as f:
    json.dump(data, f, ensure_ascii=False, indent=2)

print(f"✅ {len(new_terms_filtered)}개 중재/ADR 법률 용어 추가 완료")
print(f"총 용어 수: {len(data)}개")
