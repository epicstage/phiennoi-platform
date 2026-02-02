#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
건설 보험/분쟁 관련 용어 추가 스크립트 (10개)
테마: 건설공사보험, 제3자배상책임보험, 산재보험, 분쟁조정, 중재, 감정평가, 하자담보책임, 손해배상, 공사중단, 계약해지
Tier S 품질 기준 준수
"""

import json
import os

# 추가할 용어 데이터 (Tier S 기준)
data = [
    {
        "slug": "bao-hiem-cong-trinh-xay-dung",
        "korean": "건설공사보험",
        "vietnamese": "Bảo hiểm công trình xây dựng",
        "hanja": "建設工事保險",
        "hanjaReading": "建(지을 건) + 設(베풀 설) + 工(장인 공) + 事(일 사) + 保(지킬 보) + 險(험할 험)",
        "pronunciation": "껀썰꽁사보헴",
        "meaningKo": "건설공사 중 발생할 수 있는 재해나 사고로 인한 손해를 보상하는 보험. 공사 기간 중 화재, 폭발, 붕괴, 홍수 등의 위험으로부터 공사 목적물과 자재를 보호합니다. 통역 시 베트남의 건설보험 의무가입 대상(대형 공사 위주)과 한국의 보험 가입 기준(건설공사비 100억 원 이상 등)의 차이를 명확히 설명해야 합니다. 보험료율, 보상 범위, 면책사항 등 구체적 조건도 함께 통역하는 것이 분쟁 예방에 중요합니다.",
        "meaningVi": "Bảo hiểm bồi thường các thiệt hại do tai nạn hoặc thảm họa xảy ra trong quá trình thi công xây dựng. Bảo vệ công trình và vật liệu khỏi các rủi ro như hỏa hoạn, nổ, sập đổ, lũ lụt. Ở Việt Nam, bảo hiểm công trình chủ yếu bắt buộc với các dự án lớn, trong khi Hàn Quốc có quy định cụ thể theo giá trị công trình (từ 10 tỷ won trở lên).",
        "context": "건설 보험, 계약 관리",
        "culturalNote": "한국에서는 건설공사보험이 일정 규모 이상(건설공사비 100억 원 이상 또는 연면적 5천㎡ 이상)의 공사에 의무화되어 있으며, 보험 가입 증명서를 발주처에 제출해야 합니다. 베트남도 대형 프로젝트에는 보험 가입이 요구되지만, 중소형 공사는 선택적인 경우가 많아 계약 단계에서 보험 조건을 명확히 협의하는 것이 중요합니다. 한국 기업이 베트남에서 시공할 때 한국 보험사의 보험 적용 범위와 베트남 현지 보험 요구사항의 차이로 인한 분쟁이 발생할 수 있으므로 주의가 필요합니다.",
        "commonMistakes": [
            {
                "mistake": "공사보험을 '산재보험'으로 혼동",
                "correction": "건설공사보험(공사 목적물 보호) ≠ 산재보험(근로자 보호)",
                "explanation": "건설공사보험은 공사 중 건물/자재의 손해를 보상하고, 산재보험은 근로자의 재해를 보상하는 별개의 보험입니다."
            },
            {
                "mistake": "Bảo hiểm tai nạn lao động으로 잘못 번역",
                "correction": "Bảo hiểm công trình xây dựng (공사보험) vs Bảo hiểm tai nạn lao động (산재보험)",
                "explanation": "베트남어에서도 공사보험과 산재보험은 명확히 구분되는 용어이므로 정확한 용어를 사용해야 합니다."
            },
            {
                "mistake": "보험료를 '보험금'으로 혼용",
                "correction": "보험료(phí bảo hiểm, 납부금) ≠ 보험금(tiền bảo hiểm, 보상금)",
                "explanation": "보험료는 가입자가 내는 돈, 보험금은 사고 시 받는 돈으로 완전히 반대 개념입니다."
            }
        ],
        "examples": [
            {
                "ko": "본 공사는 건설공사보험 의무 가입 대상이므로, 착공 전 보험 가입 증명서를 제출하시기 바랍니다.",
                "vi": "Công trình này thuộc đối tượng bắt buộc phải mua bảo hiểm công trình xây dựng, vui lòng nộp giấy chứng nhận bảo hiểm trước khi khởi công.",
                "situation": "formal"
            },
            {
                "ko": "태풍으로 인한 공사 목적물 손해는 건설공사보험으로 보상받을 수 있습니다.",
                "vi": "Thiệt hại đối với công trình do bão có thể được bồi thường qua bảo hiểm công trình xây dựng.",
                "situation": "formal"
            },
            {
                "ko": "보험료는 공사비의 약 0.3~0.5% 수준으로 책정됩니다.",
                "vi": "Phí bảo hiểm được ấn định ở mức khoảng 0.3~0.5% giá trị công trình.",
                "situation": "onsite"
            }
        ],
        "relatedTerms": ["산재보험", "제3자배상책임보험", "하자담보책임", "공사중단"]
    },
    {
        "slug": "bao-hiem-trach-nhiem-dan-su-doi-voi-ben-thu-ba",
        "korean": "제3자배상책임보험",
        "vietnamese": "Bảo hiểm trách nhiệm dân sự đối với bên thứ ba",
        "hanja": "第三者賠償責任保險",
        "hanjaReading": "第(차례 제) + 三(석 삼) + 者(놈 자) + 賠(갚을 배) + 償(갚을 상) + 責(꾸짖을 책) + 任(맡을 임) + 保(지킬 보) + 險(험할 험)",
        "pronunciation": "쩨썬쟈빼쌍짝넴보헴",
        "meaningKo": "건설공사 중 발생한 사고로 제3자(공사 당사자가 아닌 일반인, 인근 건물 등)에게 입힌 손해를 배상하는 보험. 공사 중 낙하물로 인한 부상, 진동으로 인한 인근 건물 균열, 소음으로 인한 피해 등을 보상합니다. 통역 시 '제3자'의 범위(공사 관계자 제외, 인근 주민/건물 포함)를 명확히 하고, 한국과 베트남의 배상책임 기준 차이(과실 비율, 배상 한도 등)를 설명해야 합니다. 특히 국제 공사에서는 보험 적용 지역과 법적 관할권 문제도 통역해야 합니다.",
        "meaningVi": "Bảo hiểm bồi thường thiệt hại gây ra cho bên thứ ba (người dân, tài sản lân cận không liên quan trực tiếp đến công trình) do tai nạn xảy ra trong quá trình thi công. Bao gồm các trường hợp như vật rơi gây thương tích, rung động làm nứt nhà lân cận, tiếng ồn gây ảnh hưởng. 'Bên thứ ba' không bao gồm nhân viên công trường mà chỉ người dân và tài sản xung quanh.",
        "context": "건설 보험, 안전 관리",
        "culturalNote": "한국에서는 제3자배상책임보험이 건설공사보험과 함께 일정 규모 이상 공사에 의무화되어 있으며, 보상 한도가 명확히 규정됩니다(대인 1인당 1억 5천만 원, 1사고당 15억 원 등). 베트남에서도 유사한 보험 제도가 있으나, 배상 기준과 한도가 다를 수 있어 국제 공사 시 양국 법규를 모두 검토해야 합니다. 특히 베트남 현지에서 한국 시공사가 베트남 주민에게 피해를 입힐 경우, 보상 기준과 절차가 복잡하므로 계약 단계에서 명확한 보험 조건 합의가 필수입니다.",
        "commonMistakes": [
            {
                "mistake": "제3자를 '공사 관계자 전체'로 오해",
                "correction": "제3자 = 공사 당사자가 아닌 외부인(인근 주민, 행인 등)",
                "explanation": "공사 관계자(발주자, 시공사, 근로자)는 제3자가 아니며, 제3자배상책임보험은 외부 피해자 보호를 위한 것입니다."
            },
            {
                "mistake": "Bảo hiểm tai nạn lao động으로 번역",
                "correction": "Bảo hiểm trách nhiệm dân sự đối với bên thứ ba (제3자배상책임) ≠ Bảo hiểm tai nạn lao động (산재보험)",
                "explanation": "산재보험은 근로자 보호, 제3자배상책임보험은 외부인 보호 목적으로 완전히 다릅니다."
            },
            {
                "mistake": "배상책임을 '책임보험'으로 축약",
                "correction": "제3자배상책임보험 (full term) 사용",
                "explanation": "베트남어에서도 'Bảo hiểm trách nhiệm dân sự đối với bên thứ ba'로 풀네임을 사용해야 오해가 없습니다."
            }
        ],
        "examples": [
            {
                "ko": "공사 중 낙하물로 인근 주민이 부상을 입을 경우, 제3자배상책임보험으로 치료비를 보상합니다.",
                "vi": "Trong trường hợp người dân lân cận bị thương do vật rơi từ công trường, chi phí điều trị sẽ được bồi thường qua bảo hiểm trách nhiệm dân sự đối với bên thứ ba.",
                "situation": "formal"
            },
            {
                "ko": "이 보험은 공사로 인한 진동, 소음 피해도 보상 대상에 포함됩니다.",
                "vi": "Bảo hiểm này cũng bao gồm bồi thường thiệt hại do rung động và tiếng ồn từ công trình.",
                "situation": "formal"
            },
            {
                "ko": "제3자배상책임보험의 보상 한도는 1사고당 15억 원입니다.",
                "vi": "Giới hạn bồi thường của bảo hiểm trách nhiệm dân sự đối với bên thứ ba là 1.5 tỷ won mỗi vụ tai nạn.",
                "situation": "onsite"
            }
        ],
        "relatedTerms": ["건설공사보험", "산재보험", "손해배상", "안전관리"]
    },
    {
        "slug": "bao-hiem-tai-nan-lao-dong",
        "korean": "산재보험",
        "vietnamese": "Bảo hiểm tai nạn lao động",
        "hanja": "産災保險",
        "hanjaReading": "産(낳을 산) + 災(재앙 재) + 保(지킬 보) + 險(험할 험)",
        "pronunciation": "바오힘따이난라오동",
        "meaningKo": "건설 현장에서 근로자가 업무 중 부상, 질병, 사망 등의 재해를 당했을 때 치료비, 휴업급여, 장해급여, 유족급여 등을 지급하는 사회보험. 한국에서는 근로자 1인 이상 사업장 의무 가입이며, 건설업은 공사금액 기준으로 보험료를 산정합니다. 통역 시 베트남의 산재보험(BHTN) 제도와 한국의 산재보험 제도의 차이(보험료율, 급여 수준, 인정 기준 등)를 명확히 설명해야 하며, 특히 국제 공사에서 한국인 근로자와 베트nam 근로자의 적용 보험이 다를 수 있음을 주의해야 합니다.",
        "meaningVi": "Bảo hiểm xã hội bắt buộc chi trả chi phí điều trị, trợ cấp nghỉ việc, trợ cấp thương tật, trợ cấp người thân khi người lao động bị tai nạn, bệnh nghề nghiệp, hoặc tử vong trong quá trình làm việc tại công trường xây dựng. Ở Việt Nam, BHTN (Bảo hiểm tai nạn lao động, bệnh nghề nghiệp) là một trong các loại bảo hiểm xã hội bắt buộc. Ở Hàn Quốc, mọi doanh nghiệp có từ 1 lao động trở lên đều phải tham gia bảo hiểm tai nạn lao động.",
        "context": "근로자 보호, 건설 안전",
        "culturalNote": "한국의 산재보험은 근로복지공단이 운영하며, 건설업은 공사금액의 일정 비율(약 1~3%, 업종별 차등)을 보험료로 납부합니다. 산재 인정 기준이 비교적 넓어 통근 재해, 출장 중 사고도 포함될 수 있습니다. 베트남의 산재보험(BHTN)은 사회보험(BHXH) 체계 안에 포함되어 있으며, 보험료율과 급여 수준이 한국과 다릅니다. 한국 기업이 베트남에서 현지 근로자를 고용할 때는 베트남 법에 따라 BHTN에 가입해야 하며, 한국인 주재원은 한국 산재보험 적용 여부를 별도로 확인해야 합니다.",
        "commonMistakes": [
            {
                "mistake": "산재보험을 '건설공사보험'으로 혼동",
                "correction": "산재보험(근로자 보호) ≠ 건설공사보험(공사 목적물 보호)",
                "explanation": "산재보험은 사람(근로자) 보호, 건설공사보험은 물건(공사 목적물) 보호 목적으로 별개입니다."
            },
            {
                "mistake": "Bảo hiểm xã hội로 축약",
                "correction": "Bảo hiểm tai nạn lao động (산재보험) ≠ Bảo hiểm xã hội (사회보험 전체)",
                "explanation": "베트남의 사회보험은 여러 종류가 있으므로, 산재보험은 'Bảo hiểm tai nạn lao động' 또는 'BHTN'으로 정확히 표현해야 합니다."
            },
            {
                "mistake": "산재 적용 범위를 '현장 내 사고'로만 제한",
                "correction": "산재는 출퇴근, 출장, 회식 중 사고도 포함 가능",
                "explanation": "한국 산재보험은 업무 관련성이 인정되면 현장 밖 사고도 보상 대상이므로, 통역 시 적용 범위를 넓게 설명해야 합니다."
            }
        ],
        "examples": [
            {
                "ko": "건설 현장 근로자는 전원 산재보험에 가입되어 있으며, 업무 중 부상 시 치료비가 전액 지원됩니다.",
                "vi": "Tất cả công nhân tại công trường đều được tham gia bảo hiểm tai nạn lao động, chi phí điều trị khi bị thương trong công việc được hỗ trợ toàn bộ.",
                "situation": "formal"
            },
            {
                "ko": "산재보험료는 공사금액의 약 2%로 산정되며, 시공사가 부담합니다.",
                "vi": "Phí bảo hiểm tai nạn lao động được tính khoảng 2% giá trị công trình và do nhà thầu thi công chi trả.",
                "situation": "formal"
            },
            {
                "ko": "출퇴근 중 사고도 산재로 인정받을 수 있으니, 사고 발생 시 즉시 신고하세요.",
                "vi": "Tai nạn trên đường đi làm, về nhà cũng có thể được công nhận là tai nạn lao động, hãy báo ngay khi xảy ra sự cố.",
                "situation": "onsite"
            }
        ],
        "relatedTerms": ["건설공사보험", "제3자배상책임보험", "안전관리", "근로자보호"]
    },
    {
        "slug": "dieu-chinh-tranh-chap",
        "korean": "분쟁조정",
        "vietnamese": "Điều chỉnh tranh chấp",
        "hanja": "紛爭調停",
        "hanjaReading": "紛(어지러울 분) + 爭(다툴 쟁) + 調(고를 조) + 停(머물 정)",
        "pronunciation": "디에우찐짱짭",
        "meaningKo": "건설공사 계약 당사자 간 발생한 분쟁을 법원 소송이 아닌 제3의 조정기관(건설분쟁조정위원회 등)을 통해 합의로 해결하는 절차. 소송보다 빠르고 비용이 적게 들며, 전문가의 중재로 기술적 분쟁도 효과적으로 해결할 수 있습니다. 통역 시 한국의 건설분쟁조정위원회와 베트남의 분쟁 조정 기관(중재센터 등)의 차이, 조정 결정의 법적 구속력 유무, 조정 절차와 기간을 명확히 설명해야 합니다. 특히 국제 공사에서는 조정 준거법과 관할권 문제가 중요하므로 계약서상 조정 조항을 정확히 통역해야 합니다.",
        "meaningVi": "Quy trình giải quyết tranh chấp giữa các bên trong hợp đồng xây dựng thông qua cơ quan điều chỉnh thứ ba (như Ủy ban Điều chỉnh Tranh chấp Xây dựng) bằng thỏa thuận, thay vì kiện tụng tại tòa án. Nhanh hơn, ít tốn kém hơn so với tố tụng, và có thể giải quyết hiệu quả các tranh chấp kỹ thuật nhờ chuyên gia trung gian. Quyết định điều chỉnh có thể có hoặc không có hiệu lực pháp lý ràng buộc tùy theo quy định của từng quốc gia.",
        "context": "계약 관리, 분쟁 해결",
        "culturalNote": "한국에서는 건설산업기본법에 따라 건설분쟁조정위원회가 설치되어 있으며, 공사비 10억 원 이상 분쟁은 의무적으로 조정을 거쳐야 소송을 제기할 수 있습니다. 조정 결정에 양측이 동의하면 재판상 화해와 동일한 효력을 가집니다. 베트남에서도 건설 분쟁 조정 절차가 있으나, 법적 구속력과 절차가 다를 수 있어 국제 계약 시 조정 조항을 명확히 규정해야 합니다. 한국 기업이 베트남에서 분쟁 발생 시, 양국 법체계의 차이로 인해 조정 결과의 집행력이 달라질 수 있으므로 사전 법률 검토가 필수입니다.",
        "commonMistakes": [
            {
                "mistake": "조정을 '중재'와 혼동",
                "correction": "조정(điều chỉnh, 합의 유도) ≠ 중재(trọng tài, 결정 강제)",
                "explanation": "조정은 제3자가 합의를 도와주는 과정이고, 중재는 제3자가 결정을 내려 양측을 구속하는 과정입니다."
            },
            {
                "mistake": "Hòa giải로 번역",
                "correction": "Điều chỉnh tranh chấp (공식 조정) ≠ Hòa giải (일반 화해)",
                "explanation": "Điều chỉnh tranh chấp은 법적 절차를 거친 공식 조정이고, Hòa giải는 비공식 화해를 의미합니다."
            },
            {
                "mistake": "조정 결정의 법적 효력을 '판결'로 설명",
                "correction": "조정 결정은 양측 동의 시에만 법적 효력 발생",
                "explanation": "조정은 합의가 전제이므로, 한쪽이 거부하면 효력이 없으며 이후 소송이 가능합니다."
            }
        ],
        "examples": [
            {
                "ko": "공사비 분쟁이 발생하여 건설분쟁조정위원회에 조정을 신청했습니다.",
                "vi": "Do phát sinh tranh chấp về chi phí công trình, chúng tôi đã nộp đơn xin điều chỉnh tranh chấp tại Ủy ban Điều chỉnh Tranh chấp Xây dựng.",
                "situation": "formal"
            },
            {
                "ko": "조정 결정에 양측이 동의하면, 재판상 화해와 동일한 효력을 갖습니다.",
                "vi": "Nếu cả hai bên đồng ý với quyết định điều chỉnh, nó sẽ có hiệu lực tương đương với hòa giải tại tòa.",
                "situation": "formal"
            },
            {
                "ko": "조정 절차는 약 3개월 소요되며, 소송보다 훨씬 빠릅니다.",
                "vi": "Quy trình điều chỉnh mất khoảng 3 tháng, nhanh hơn nhiều so với tố tụng.",
                "situation": "onsite"
            }
        ],
        "relatedTerms": ["중재", "소송", "감정평가", "계약해지"]
    },
    {
        "slug": "trong-tai",
        "korean": "중재",
        "vietnamese": "Trọng tài",
        "hanja": "仲裁",
        "hanjaReading": "仲(가운데 중) + 裁(마를 재)",
        "pronunciation": "쫑따이",
        "meaningKo": "건설공사 계약 당사자 간 분쟁을 법원이 아닌 독립적인 중재인 또는 중재기관이 판정하여 해결하는 절차. 중재 판정은 법원 판결과 동일한 효력을 가지며, 불복 시 항소가 원칙적으로 불가능합니다. 소송보다 신속하고 비공개로 진행되며, 기술적 전문성이 필요한 건설 분쟁에 효과적입니다. 통역 시 한국의 대한상사중재원과 베트남의 중재기관(VIAC 등)의 차이, 중재 판정의 집행력, 국제 중재(ICC 등) 적용 여부를 명확히 설명해야 합니다. 특히 중재 조항이 계약서에 명시되지 않으면 중재를 강제할 수 없으므로, 계약 단계에서 중재 합의를 정확히 통역하는 것이 중요합니다.",
        "meaningVi": "Quy trình giải quyết tranh chấp trong hợp đồng xây dựng thông qua trọng tài viên hoặc tổ chức trọng tài độc lập, không phải qua tòa án. Phán quyết trọng tài có hiệu lực tương đương bản án của tòa, và nguyên tắc không thể kháng cáo. Trọng tài nhanh hơn, bảo mật hơn tố tụng và hiệu quả với các tranh chấp xây dựng cần chuyên môn kỹ thuật. Ở Việt Nam, VIAC (Trung tâm Trọng tài Quốc tế Việt Nam) là tổ chức trọng tài chính. Phán quyết trọng tài chỉ có thể thực thi khi hợp đồng có điều khoản trọng tài rõ ràng.",
        "context": "계약 관리, 분쟁 해결",
        "culturalNote": "한국에서는 대한상사중재원이 건설 분쟁 중재를 주로 담당하며, 중재 판정은 법원 판결과 동일한 집행력을 가집니다. 중재는 1심으로 종결되어 항소가 불가능하므로 신중한 선택이 필요합니다. 베트남에서도 VIAC(베트남 국제중재센터) 등이 중재를 담당하며, 한국과 베트남 간 국제 공사에서는 ICC(국제상업회의소) 중재나 싱가포르 중재(SIAC) 등을 이용하기도 합니다. 중재 판정의 국제적 집행력을 위해서는 뉴욕협약 가입국 여부를 확인해야 하며, 계약서에 중재 조항(중재지, 준거법, 중재기관 등)을 명확히 규정하는 것이 분쟁 예방의 핵심입니다.",
        "commonMistakes": [
            {
                "mistake": "중재를 '조정'과 혼동",
                "correction": "중재(trọng tài, 결정 강제) ≠ 조정(điều chỉnh, 합의 유도)",
                "explanation": "중재는 중재인이 판정을 내려 강제하는 것이고, 조정은 제3자가 합의를 도와주는 것입니다."
            },
            {
                "mistake": "중재 판정을 '권고'로 오해",
                "correction": "중재 판정은 법원 판결과 동일한 강제력",
                "explanation": "중재 판정은 법적 구속력이 있으며, 이행하지 않으면 강제집행이 가능합니다."
            },
            {
                "mistake": "Hòa giải로 번역",
                "correction": "Trọng tài (중재) ≠ Hòa giải (화해)",
                "explanation": "베트남어에서 Trọng tài는 법적 구속력이 있는 중재, Hòa giải는 비공식 화해를 의미합니다."
            }
        ],
        "examples": [
            {
                "ko": "계약서 제20조에 따라 분쟁은 대한상사중재원의 중재로 해결합니다.",
                "vi": "Theo điều 20 của hợp đồng, tranh chấp sẽ được giải quyết bằng trọng tài tại Trung tâm Trọng tài Thương mại Hàn Quốc.",
                "situation": "formal"
            },
            {
                "ko": "중재 판정은 최종 결정으로, 항소가 불가능합니다.",
                "vi": "Phán quyết trọng tài là quyết định cuối cùng, không thể kháng cáo.",
                "situation": "formal"
            },
            {
                "ko": "국제 공사이므로 ICC 중재를 적용하기로 합의했습니다.",
                "vi": "Do là công trình quốc tế, chúng tôi đã thỏa thuận áp dụng trọng tài ICC.",
                "situation": "onsite"
            }
        ],
        "relatedTerms": ["분쟁조정", "소송", "계약해지", "손해배상"]
    },
    {
        "slug": "danh-gia-cam-dinh",
        "korean": "감정평가",
        "vietnamese": "Đánh giá cảm định",
        "hanja": "鑑定評價",
        "hanjaReading": "鑑(거울 감) + 定(정할 정) + 評(평할 평) + 價(값 가)",
        "pronunciation": "단자껌딘",
        "meaningKo": "건설공사에서 분쟁 또는 손해 산정을 위해 전문가(감정평가사, 기술사 등)가 공사 하자, 손해액, 공사비 등을 객관적으로 조사하고 평가하는 절차. 법원 소송이나 중재 시 증거 자료로 활용되며, 하자 발생 원인, 보수 비용, 공사 지연 손해액 등을 산정합니다. 통역 시 감정평가 대상(하자, 공사비, 토지 등), 감정 방법(현장 조사, 시험, 계산 등), 감정평가서의 법적 효력을 명확히 설명해야 합니다. 한국과 베트남의 감정평가 자격 제도와 평가 기준의 차이도 통역 시 유의해야 합니다.",
        "meaningVi": "Quy trình chuyên gia (thẩm định giá, kỹ sư) điều tra và đánh giá khách quan về lỗi thi công, giá trị thiệt hại, chi phí công trình trong các tranh chấp hoặc tính toán bồi thường xây dựng. Được sử dụng làm tài liệu chứng cứ trong tố tụng hoặc trọng tài, bao gồm xác định nguyên nhân lỗi, chi phí sửa chữa, thiệt hại do chậm tiến độ. Ở Việt Nam, cảm định giá được thực hiện bởi tổ chức thẩm định giá có chứng chỉ hành nghề, tương tự như hệ thống thẩm định giá Hàn Quốc.",
        "context": "분쟁 해결, 하자 관리",
        "culturalNote": "한국에서는 감정평가사법에 따라 자격을 가진 감정평가사만 공식 감정평가를 수행할 수 있으며, 법원 감정인으로 지정되기도 합니다. 건설 기술 분쟁의 경우 건축사, 기술사 등이 감정인으로 참여합니다. 베트남에서도 유사하게 공인된 감정평가 기관이 있으며, 법적 분쟁 시 법원이 인정하는 감정 기관의 평가서만 증거로 채택됩니다. 한국 기업이 베트남에서 공사 분쟁 시, 베트남 현지 감정평가 기준과 한국 기준이 다를 수 있어 양측이 합의한 감정 기관을 사전에 계약서에 명시하는 것이 분쟁 해결에 유리합니다.",
        "commonMistakes": [
            {
                "mistake": "감정평가를 '가격 조사'로 축소",
                "correction": "감정평가는 전문가의 공식 평가 절차",
                "explanation": "감정평가는 법적 효력이 있는 공식 절차이며, 단순 시장조사나 견적과는 다릅니다."
            },
            {
                "mistake": "Đánh giá로 축약",
                "correction": "Đánh giá cảm định (감정평가) ≠ Đánh giá (일반 평가)",
                "explanation": "베트남어에서 '감정평가'는 'Đánh giá cảm định' 또는 'Thẩm định giá'로 정확히 표현해야 공식 절차임을 나타냅니다."
            },
            {
                "mistake": "감정평가서를 '의견서'로 번역",
                "correction": "감정평가서는 법적 증거 능력이 있는 공식 문서",
                "explanation": "감정평가서는 전문가의 단순 의견이 아니라 법적 효력이 있는 공식 문서입니다."
            }
        ],
        "examples": [
            {
                "ko": "하자 보수 비용 산정을 위해 건축사에게 감정평가를 의뢰했습니다.",
                "vi": "Chúng tôi đã yêu cầu kiến trúc sư thực hiện đánh giá cảm định để tính toán chi phí sửa chữa lỗi thi công.",
                "situation": "formal"
            },
            {
                "ko": "법원은 공인 감정평가 기관의 평가서를 증거로 채택했습니다.",
                "vi": "Tòa án đã chấp nhận báo cáo đánh giá của tổ chức thẩm định giá được công nhận làm bằng chứng.",
                "situation": "formal"
            },
            {
                "ko": "감정평가 결과, 하자 보수비는 3억 원으로 산정되었습니다.",
                "vi": "Kết quả đánh giá cảm định, chi phí sửa chữa lỗi được tính là 300 triệu won.",
                "situation": "onsite"
            }
        ],
        "relatedTerms": ["하자담보책임", "손해배상", "분쟁조정", "중재"]
    },
    {
        "slug": "trach-nhiem-bao-hanh-loi",
        "korean": "하자담보책임",
        "vietnamese": "Trách nhiệm bảo hành lỗi",
        "hanja": "瑕疵擔保責任",
        "hanjaReading": "瑕(허물 하) + 疵(흠 자) + 擔(멜 담) + 保(지킬 보) + 責(꾸짖을 책) + 任(맡을 임)",
        "pronunciation": "짝넴바오한로이",
        "meaningKo": "건설공사 완공 후 일정 기간 내에 발견된 하자(결함, 불량)에 대해 시공사가 무상으로 보수할 책임. 민법과 건설산업기본법에 따라 하자담보책임 기간이 정해지며, 구조 안전과 관련된 중요 부분은 10년, 일반 부분은 2~3년입니다. 통역 시 하자의 종류(중대 하자, 경미 하자), 하자담보책임 기간, 하자보수 절차, 하자보증금 제도를 명확히 설명해야 합니다. 한국과 베트남의 하자담보책임 기간과 보수 범위의 차이도 국제 계약 시 주요 이슈이므로 정확한 통역이 필수입니다.",
        "meaningVi": "Trách nhiệm của nhà thầu thi công phải sửa chữa miễn phí các lỗi (khuyết tật, hỏng hóc) được phát hiện trong một khoảng thời gian nhất định sau khi hoàn thành công trình. Theo Luật Dân sự và Luật Xây dựng Hàn Quốc, thời hạn bảo hành lỗi được quy định: 10 năm cho các phần quan trọng liên quan đến an toàn kết cấu, 2~3 năm cho các phần thông thường. Ở Việt Nam, thời hạn bảo hành công trình xây dựng cũng được quy định trong hợp đồng và pháp luật, nhưng có thể khác với Hàn Quốc.",
        "context": "계약 관리, 하자 관리",
        "culturalNote": "한국에서는 건설산업기본법에 따라 하자담보책임 기간이 법정되어 있으며, 발주자는 하자보증금(통상 공사비의 3~5%)을 보관하다가 하자담보책임 기간 종료 후 반환합니다. 하자 발견 시 시공사에게 하자보수 청구를 하고, 시공사가 불응하면 보증금으로 직접 보수할 수 있습니다. 베트남에서도 유사한 하자담보 제도가 있으나, 법정 기간과 보증금 비율이 다를 수 있어 계약서에 명확히 규정해야 합니다. 한국 시공사가 베트남에서 공사할 때 한국법과 베트남법의 하자담보 기간 차이로 인한 분쟁을 예방하려면, 계약 단계에서 적용 법규와 책임 범위를 명확히 합의해야 합니다.",
        "commonMistakes": [
            {
                "mistake": "하자를 '파손'으로만 이해",
                "correction": "하자는 설계·시공 불량으로 인한 모든 결함",
                "explanation": "하자는 균열, 누수, 결함뿐 아니라 설계 미달, 성능 부족 등도 포함하는 넓은 개념입니다."
            },
            {
                "mistake": "Bảo hành으로만 번역",
                "correction": "Trách nhiệm bảo hành lỗi (하자담보책임) ≠ Bảo hành (일반 보증)",
                "explanation": "하자담보책임은 법적 책임이며, 단순 제품 보증과는 다른 건설법 개념입니다."
            },
            {
                "mistake": "하자담보책임 기간을 '보증기간'으로 혼용",
                "correction": "하자담보책임 기간은 법정 기간, 보증기간은 계약상 기간",
                "explanation": "하자담보책임 기간은 법으로 정해진 최소 기간이며, 계약으로 더 연장할 수는 있지만 단축은 불가능합니다."
            }
        ],
        "examples": [
            {
                "ko": "본 공사는 완공 후 구조 부분에 대해 10년간 하자담보책임을 집니다.",
                "vi": "Công trình này có trách nhiệm bảo hành lỗi cho phần kết cấu trong 10 năm sau khi hoàn thành.",
                "situation": "formal"
            },
            {
                "ko": "하자보증금은 공사비의 3%로, 하자담보책임 기간 종료 후 반환됩니다.",
                "vi": "Tiền bảo đảm bảo hành lỗi là 3% giá trị công trình, sẽ được hoàn trả sau khi kết thúc thời hạn bảo hành.",
                "situation": "formal"
            },
            {
                "ko": "외벽 균열은 하자에 해당하므로, 시공사가 무상으로 보수해야 합니다.",
                "vi": "Vết nứt trên tường ngoài là lỗi thi công, nhà thầu phải sửa chữa miễn phí.",
                "situation": "onsite"
            }
        ],
        "relatedTerms": ["하자보수", "감정평가", "손해배상", "분쟁조정"]
    },
    {
        "slug": "boi-thuong-thiet-hai",
        "korean": "손해배상",
        "vietnamese": "Bồi thường thiệt hại",
        "hanja": "損害賠償",
        "hanjaReading": "損(덜 손) + 害(해칠 해) + 賠(갚을 배) + 償(갚을 상)",
        "pronunciation": "보이투엉티엣하이",
        "meaningKo": "건설공사 계약 위반, 불법행위, 하자 등으로 인해 발생한 손해를 금전으로 보상하는 법적 책임. 공사 지연, 하자, 안전사고 등 다양한 원인으로 손해배상 청구가 발생하며, 배상 범위는 직접 손해(공사비, 보수비 등)와 간접 손해(영업 손실, 지연 손해 등)로 구분됩니다. 통역 시 손해배상의 원인(계약 위반, 불법행위 등), 배상 범위(직접/간접 손해), 배상액 산정 방법, 책임 제한 조항 등을 명확히 설명해야 합니다. 한국과 베트남의 손해배상 법리와 배상 기준의 차이도 국제 계약 시 중요한 통역 포인트입니다.",
        "meaningVi": "Trách nhiệm pháp lý phải bồi thường bằng tiền cho thiệt hại phát sinh do vi phạm hợp đồng, hành vi trái pháp luật, lỗi thi công trong xây dựng. Yêu cầu bồi thường thiệt hại có thể phát sinh từ nhiều nguyên nhân như chậm tiến độ, lỗi thi công, tai nạn an toàn, v.v. Phạm vi bồi thường bao gồm thiệt hại trực tiếp (chi phí công trình, chi phí sửa chữa) và thiệt hại gián tiếp (mất doanh thu, thiệt hại do chậm trễ). Tiêu chuẩn bồi thường ở Hàn Quốc và Việt Nam có thể khác nhau.",
        "context": "계약 관리, 분쟁 해결",
        "culturalNote": "한국에서는 민법에 따라 손해배상 책임이 인정되며, 계약 위반의 경우 손해배상 예정액을 계약서에 명시하기도 합니다(예: 공사 지연 시 1일당 공사비의 0.1% 등). 입증 책임은 피해자에게 있으나, 건설공사의 경우 과실 추정 원칙이 적용되어 시공사가 무과실을 입증해야 하는 경우도 많습니다. 베트남에서도 유사한 손해배상 제도가 있으나, 배상액 산정 기준과 입증 책임의 법리가 다를 수 있어 국제 계약 시 준거법과 배상 한도를 명확히 규정해야 합니다. 특히 간접 손해(영업 손실 등)의 인정 범위가 양국 간 다를 수 있으므로 계약서에 구체적으로 명시하는 것이 분쟁 예방에 중요합니다.",
        "commonMistakes": [
            {
                "mistake": "손해배상을 '벌금'으로 오해",
                "correction": "손해배상(민사책임) ≠ 벌금(형사처벌)",
                "explanation": "손해배상은 피해자에게 금전을 지급하는 민사 책임이고, 벌금은 국가에 납부하는 형사 처벌입니다."
            },
            {
                "mistake": "Tiền phạt로 번역",
                "correction": "Bồi thường thiệt hại (손해배상) ≠ Tiền phạt (벌금)",
                "explanation": "Bồi thường thiệt hại는 민사적 배상, Tiền phạt는 행정/형사 처벌이므로 명확히 구분해야 합니다."
            },
            {
                "mistake": "간접 손해를 배상 범위에서 제외",
                "correction": "계약서에 명시하지 않으면 간접 손해도 배상 대상",
                "explanation": "한국 법원은 예견 가능한 간접 손해도 배상 범위에 포함시킬 수 있으므로, 배상 범위 제한을 원하면 계약서에 명시해야 합니다."
            }
        ],
        "examples": [
            {
                "ko": "공사 지연으로 인한 손해배상액은 1일당 공사비의 0.1%로 산정합니다.",
                "vi": "Số tiền bồi thường thiệt hại do chậm tiến độ được tính là 0.1% giá trị công trình mỗi ngày.",
                "situation": "formal"
            },
            {
                "ko": "하자로 인한 보수비 외에도 영업 손실에 대한 손해배상을 청구할 수 있습니다.",
                "vi": "Ngoài chi phí sửa chữa lỗi, có thể yêu cầu bồi thường thiệt hại do mất doanh thu.",
                "situation": "formal"
            },
            {
                "ko": "손해배상 책임은 계약금액의 10%로 제한됩니다.",
                "vi": "Trách nhiệm bồi thường thiệt hại được giới hạn ở mức 10% giá trị hợp đồng.",
                "situation": "onsite"
            }
        ],
        "relatedTerms": ["하자담보책임", "계약해지", "감정평가", "분쟁조정"]
    },
    {
        "slug": "ngung-thi-cong",
        "korean": "공사중단",
        "vietnamese": "Ngừng thi công",
        "hanja": "工事中斷",
        "hanjaReading": "工(장인 공) + 事(일 사) + 中(가운데 중) + 斷(끊을 단)",
        "pronunciation": "응엉티꽁",
        "meaningKo": "건설공사를 일시적 또는 영구적으로 중지하는 것. 발주자의 지시, 설계 변경, 자금 부족, 안전사고, 민원, 날씨 등 다양한 원인으로 발생합니다. 공사중단 시 시공사는 중단 기간에 대한 보상을 청구할 수 있으며, 중단이 장기화되면 계약 해지 사유가 될 수 있습니다. 통역 시 공사중단의 원인(귀책사유), 중단 기간, 재개 조건, 중단 기간 중 비용(현장 유지비, 장비 대기료 등) 처리 방법을 명확히 설명해야 합니다. 한국과 베트남의 공사중단 보상 기준과 절차의 차이도 국제 계약 시 분쟁 원인이 되므로 정확한 통역이 필수입니다.",
        "meaningVi": "Tạm dừng hoặc ngừng vĩnh viễn thi công xây dựng. Có thể xảy ra do nhiều nguyên nhân như chỉ thị của chủ đầu tư, thay đổi thiết kế, thiếu vốn, tai nạn an toàn, khiếu nại dân sự, thời tiết, v.v. Khi ngừng thi công, nhà thầu có thể yêu cầu bồi thường cho thời gian ngừng, và nếu kéo dài có thể trở thành lý do chấm dứt hợp đồng. Cần làm rõ nguyên nhân ngừng công (trách nhiệm bên nào), thời gian ngừng, điều kiện tái khởi công, cách xử lý chi phí trong thời gian ngừng (phí duy trì hiện trường, phí chờ thiết bị).",
        "context": "공정 관리, 계약 관리",
        "culturalNote": "한국에서는 공사중단 사유가 발주자에게 있을 경우(설계 변경, 예산 부족 등) 시공사는 중단 기간에 대한 보상(현장 관리비, 장비 대기료 등)을 청구할 수 있으며, 중단이 3개월 이상 지속되면 계약 해지권을 행사할 수 있습니다. 베트남에서도 유사한 제도가 있으나, 보상 기준과 계약 해지 요건이 다를 수 있어 계약서에 공사중단 조항을 명확히 규정해야 합니다. 한국 시공사가 베트남에서 공사 중단 시, 현지 법규에 따른 신고 의무와 재개 절차를 준수해야 하며, 중단 기간 중 현장 안전 관리 책임도 명확히 해야 분쟁을 예방할 수 있습니다.",
        "commonMistakes": [
            {
                "mistake": "공사중단을 '공사완료'로 오해",
                "correction": "공사중단(ngừng thi công) ≠ 공사완료(hoàn thành)",
                "explanation": "공사중단은 일시적/영구적 정지를 의미하며, 완료와는 완전히 다른 개념입니다."
            },
            {
                "mistake": "Tạm dừng와 Ngừng을 혼용",
                "correction": "Tạm dừng(일시 중단) ≠ Ngừng vĩnh viễn(영구 중단)",
                "explanation": "베트남어에서 Tạm dừng는 재개 예정인 일시 중단, Ngừng는 영구 중단을 의미하므로 상황에 맞게 사용해야 합니다."
            },
            {
                "mistake": "중단 기간 비용을 '손해배상'으로만 처리",
                "correction": "중단 기간 비용은 '보상'(bồi hoàn) 개념",
                "explanation": "공사중단으로 인한 현장 유지비 등은 손해배상이 아니라 실비 보상의 성격이므로 정확한 용어 구분이 필요합니다."
            }
        ],
        "examples": [
            {
                "ko": "설계 변경으로 인해 공사를 3개월간 중단합니다.",
                "vi": "Do thay đổi thiết kế, chúng tôi sẽ ngừng thi công trong 3 tháng.",
                "situation": "formal"
            },
            {
                "ko": "공사중단 기간 중 현장 관리비는 발주자가 부담합니다.",
                "vi": "Chi phí quản lý hiện trường trong thời gian ngừng thi công do chủ đầu tư chịu.",
                "situation": "formal"
            },
            {
                "ko": "중단이 6개월 이상 지속되면 계약 해지를 요청할 수 있습니다.",
                "vi": "Nếu ngừng công kéo dài trên 6 tháng, có thể yêu cầu chấm dứt hợp đồng.",
                "situation": "onsite"
            }
        ],
        "relatedTerms": ["계약해지", "손해배상", "공정관리", "설계변경"]
    },
    {
        "slug": "cham-dut-hop-dong",
        "korean": "계약해지",
        "vietnamese": "Chấm dứt hợp đồng",
        "hanja": "契約解止",
        "hanjaReading": "契(맺을 계) + 約(맺을 약) + 解(풀 해) + 止(그칠 지)",
        "pronunciation": "짬즛홉동",
        "meaningKo": "건설공사 계약을 법적으로 종료시키는 것. 계약 위반, 공사중단, 불가항력 등의 사유로 발주자 또는 시공사가 계약을 해지할 수 있으며, 해지 시 기성부분 정산, 손해배상, 하자담보 등 후속 처리가 필요합니다. 통역 시 계약해지 사유(정당 해지, 약정 해지, 합의 해지), 해지 절차(통보, 이행 기간 부여 등), 해지 후 처리(기성 정산, 현장 인계, 하자담보 책임 등)를 명확히 설명해야 합니다. 한국과 베트남의 계약해지 요건과 법적 효과의 차이도 국제 계약 시 중요한 통역 포인트이며, 특히 부당 해지 시 손해배상 책임이 크므로 신중한 통역이 필요합니다.",
        "meaningVi": "Chấm dứt hợp đồng xây dựng theo pháp luật. Chủ đầu tư hoặc nhà thầu có thể chấm dứt hợp đồng do vi phạm hợp đồng, ngừng thi công, bất khả kháng, v.v. Khi chấm dứt, cần xử lý thanh toán phần đã hoàn thành, bồi thường thiệt hại, trách nhiệm bảo hành. Cần làm rõ lý do chấm dứt (chấm dứt chính đáng, chấm dứt theo thỏa thuận, chấm dứt hợp ý), quy trình chấm dứt (thông báo, thời gian thực hiện), xử lý sau chấm dứt (thanh toán, bàn giao hiện trường, trách nhiệm bảo hành). Nếu chấm dứt không chính đáng, trách nhiệm bồi thường có thể rất lớn.",
        "context": "계약 관리, 분쟁 해결",
        "culturalNote": "한국에서는 민법과 건설산업기본법에 따라 계약해지 사유와 절차가 규정되어 있으며, 정당한 사유 없이 해지할 경우 손해배상 책임이 발생합니다. 발주자가 해지할 경우 시공사에게 기성부분 대금을 지급하고, 시공사가 해지할 경우 발주자는 미완성 부분에 대한 손해를 청구할 수 있습니다. 베트남에서도 유사한 제도가 있으나, 해지 통보 기간, 기성 정산 방법, 손해배상 범위 등이 다를 수 있어 계약서에 해지 조항을 명확히 규정해야 합니다. 한국 기업이 베트남에서 계약 해지 시, 현지 법규에 따른 절차(통보 기간, 서면 요건 등)를 준수하지 않으면 부당 해지로 간주되어 큰 손해배상을 부담할 수 있으므로 주의가 필요합니다.",
        "commonMistakes": [
            {
                "mistake": "계약해지를 '계약파기'로 혼용",
                "correction": "계약해지(정당 절차) ≠ 계약파기(일방적 파기)",
                "explanation": "계약해지는 법적 절차에 따른 종료이고, 계약파기는 일방적 위반으로 부당 해지에 해당합니다."
            },
            {
                "mistake": "Hủy hợp đồng으로 번역",
                "correction": "Chấm dứt hợp đồng (계약해지) ≠ Hủy hợp đồng (계약 취소/무효)",
                "explanation": "Chấm dứt hợp đồng은 정당한 사유로 종료하는 것이고, Hủy hợp đồng은 계약 자체를 무효화하는 것으로 의미가 다릅니다."
            },
            {
                "mistake": "해지 후 하자담보책임이 소멸된다고 오해",
                "correction": "계약 해지 후에도 기성부분에 대한 하자담보책임은 유지",
                "explanation": "계약이 해지되어도 이미 완성된 부분에 대한 하자담보책임은 법정 기간 동안 유지됩니다."
            }
        ],
        "examples": [
            {
                "ko": "시공사의 중대한 계약 위반으로 인해 계약을 해지합니다.",
                "vi": "Do nhà thầu vi phạm nghiêm trọng hợp đồng, chúng tôi sẽ chấm dứt hợp đồng.",
                "situation": "formal"
            },
            {
                "ko": "계약해지 후 기성부분에 대한 대금을 30일 내에 지급하겠습니다.",
                "vi": "Sau khi chấm dứt hợp đồng, chúng tôi sẽ thanh toán tiền cho phần đã hoàn thành trong vòng 30 ngày.",
                "situation": "formal"
            },
            {
                "ko": "합의 해지 시에는 쌍방이 손해배상을 청구하지 않습니다.",
                "vi": "Trong trường hợp chấm dứt hợp đồng theo thỏa thuận, hai bên không yêu cầu bồi thường thiệt hại.",
                "situation": "onsite"
            }
        ],
        "relatedTerms": ["공사중단", "손해배상", "분쟁조정", "중재"]
    }
]

# 파일 경로
script_dir = os.path.dirname(os.path.abspath(__file__))
project_root = os.path.dirname(os.path.dirname(script_dir))
file_path = os.path.join(project_root, "src", "data", "terms", "construction.json")

# 기존 데이터 로드
with open(file_path, "r", encoding="utf-8") as f:
    existing_data = json.load(f)

# 새 용어 추가
existing_data.extend(data)

# 저장
with open(file_path, "w", encoding="utf-8") as f:
    json.dump(existing_data, f, ensure_ascii=False, indent=2)

print(f"✅ {len(data)}개 용어가 {file_path}에 추가되었습니다.")
print("추가된 용어:")
for term in data:
    print(f"  - {term['korean']} ({term['vietnamese']})")
