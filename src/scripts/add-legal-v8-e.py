#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
한-베 통역 용어 플랫폼 - 법률 도메인 용어 추가 스크립트
테마: 산업재해보상법 (Industrial Accident Compensation Insurance Act)
"""

import json
import os

# 프로젝트 루트 경로
SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
PROJECT_ROOT = os.path.dirname(os.path.dirname(SCRIPT_DIR))
TERMS_FILE = os.path.join(PROJECT_ROOT, "src", "data", "terms", "legal.json")

# 추가할 용어 데이터 (Tier S 기준)
NEW_TERMS = [
    {
        "slug": "tai-nan-lao-dong-do-cong-viec",
        "korean": "업무상재해",
        "vietnamese": "Tai nạn lao động do công việc",
        "hanja": "業務上災害",
        "hanjaReading": "業(업 업) + 務(힘쓸 무) + 上(위 상) + 災(재앙 재) + 害(해칠 해)",
        "pronunciation": "업무상재해",
        "meaningKo": "근로자가 업무상 사유로 부상·질병·장해 또는 사망하는 것을 말합니다. 통역 시 주의할 점은 '업무수행성'과 '업무기인성' 두 가지 요건을 모두 충족해야 산재로 인정된다는 점입니다. 베트남에서는 '노동재해(tai nạn lao động)'로 통칭하지만, 한국은 업무 관련성을 명확히 구분합니다. 출퇴근 재해, 직업병, 과로사 등도 포함될 수 있으므로 맥락에 따라 정확히 통역해야 합니다. 산재 신청 절차나 보상 범위를 설명할 때는 양국 제도의 차이를 명확히 전달하는 것이 중요합니다.",
        "meaningVi": "Là trường hợp người lao động bị thương tích, mắc bệnh, tàn tật hoặc tử vong do nguyên nhân liên quan đến công việc. Ở Hàn Quốc, phải đáp ứng hai điều kiện là 'tính chất thực hiện công việc' và 'tính nhân quả từ công việc' thì mới được công nhận là tai nạn lao động. Bao gồm cả tai nạn đi làm về, bệnh nghề nghiệp, tử vong do làm việc quá sức. Hệ thống bảo hiểm tai nạn lao động Hàn Quốc có phạm vi bồi thường rộng hơn so với Việt Nam.",
        "context": "산재보험, 근로복지공단, 보상청구 절차에서 사용",
        "culturalNote": "한국의 산재보상 범위는 베트남보다 넓습니다. 출퇴근 재해, 직장 내 괴롭힘으로 인한 정신질환, 과로사까지 인정될 수 있습니다. 베트남은 직접적인 작업 중 사고에 초점을 맞추는 경향이 있어, 한국의 넓은 인정 범위를 설명할 때 오해가 없도록 주의해야 합니다. 또한 한국은 산재 은폐 시 사업주가 처벌받을 수 있지만, 베트남은 이러한 처벌 규정이 상대적으로 약합니다.",
        "commonMistakes": [
            {
                "mistake": "tai nạn lao động",
                "correction": "tai nạn lao động do công việc",
                "explanation": "단순 '노동재해'가 아닌 '업무로 인한'이라는 인과관계를 명시해야 법적 의미가 정확해집니다"
            },
            {
                "mistake": "tai nạn trong khi làm việc",
                "correction": "tai nạn lao động do công việc (thương tích, bệnh tật, tàn tật hoặc tử vong)",
                "explanation": "부상뿐만 아니라 질병, 장해, 사망까지 포함하는 포괄적 개념입니다"
            },
            {
                "mistake": "재해 발생 시 즉시 산재 인정된다고 설명",
                "correction": "근로복지공단의 조사와 심사를 거쳐 업무관련성이 인정되어야 한다고 설명",
                "explanation": "산재 인정은 자동이 아니며 엄격한 심사 과정이 있음을 명확히 해야 합니다"
            }
        ],
        "examples": [
            {
                "ko": "작업 중 낙하사고로 부상을 입은 경우 업무상재해로 인정됩니다.",
                "vi": "Trường hợp bị thương do tai nạn rơi từ trên cao trong khi làm việc sẽ được công nhận là tai nạn lao động do công việc.",
                "situation": "formal"
            },
            {
                "ko": "출퇴근 중 교통사고도 일정 요건 충족 시 업무상재해로 인정받을 수 있습니다.",
                "vi": "Tai nạn giao thông trên đường đi làm về cũng có thể được công nhận là tai nạn lao động nếu đáp ứng các điều kiện nhất định.",
                "situation": "formal"
            },
            {
                "ko": "이 부상이 업무상재해인지 확인하려면 근로복지공단에 산재 신청을 해야 합니다.",
                "vi": "Để xác nhận chấn thương này có phải là tai nạn lao động do công việc hay không, cần nộp đơn xin công nhận tai nạn lao động tới Tổng công ty Phúc lợi Người lao động Hàn Quốc (KCOMWEL).",
                "situation": "onsite"
            }
        ],
        "relatedTerms": ["산재보험", "요양급여", "휴업급여", "장해급여", "근로복지공단"]
    },
    {
        "slug": "bao-hiem-tai-nan-lao-dong",
        "korean": "산재보험",
        "vietnamese": "Bảo hiểm tai nạn lao động",
        "hanja": "産災保險",
        "hanjaReading": "産(날 산) + 災(재앙 재) + 保(지킬 보) + 險(험할 험)",
        "pronunciation": "산재보험",
        "meaningKo": "근로자가 업무상 재해를 입었을 때 신속하고 공정한 보상을 제공하기 위한 사회보험제도입니다. 통역 시 중요한 점은 한국의 산재보험이 전액 사업주 부담이라는 점입니다. 베트남과 달리 근로자는 보험료를 내지 않습니다. 또한 5인 미만 사업장도 대부분 의무가입 대상이며, 외국인 근로자도 내국인과 동일하게 보호받습니다. 보험급여에는 요양급여, 휴업급여, 장해급여, 유족급여 등이 포함되며, 재활 및 직업훈련 지원까지 포괄합니다. 통역 시 양국 제도의 차이를 명확히 설명해야 오해를 방지할 수 있습니다.",
        "meaningVi": "Chế độ bảo hiểm xã hội nhằm cung cấp bồi thường nhanh chóng và công bằng khi người lao động gặp tai nạn lao động do công việc. Ở Hàn Quốc, bảo hiểm tai nạn lao động được người sử dụng lao động chi trả 100%, người lao động không phải đóng phí. Cơ sở có dưới 5 người lao động cũng phải tham gia bắt buộc. Người lao động nước ngoài được bảo vệ như người Hàn. Bao gồm trợ cấp điều trị, trợ cấp nghỉ việc, trợ cấp thương tật, trợ cấp người thân, và hỗ trợ phục hồi chức năng.",
        "context": "근로계약, 고용보험, 사회보험 설명 시 사용",
        "culturalNote": "한국의 산재보험은 1964년 도입되어 세계적으로도 선진적인 제도로 평가받습니다. 베트남의 산재보험은 사회보험법(2014)에 통합되어 있으며, 보험료를 사업주와 근로자가 분담하는 구조입니다. 한국은 사업주 전액 부담이므로 베트남 근로자들에게 이 차이를 명확히 설명해야 합니다. 또한 한국은 산재보험 적용 범위가 매우 넓어 특수고용직, 1인 자영업자도 임의가입이 가능하다는 점이 특징입니다.",
        "commonMistakes": [
            {
                "mistake": "bảo hiểm xã hội",
                "correction": "bảo hiểm tai nạn lao động (một phần của bảo hiểm xã hội)",
                "explanation": "사회보험(bảo hiểm xã hội)은 국민연금, 건강보험, 고용보험, 산재보험을 포괄하는 개념입니다"
            },
            {
                "mistake": "근로자도 보험료를 낸다고 통역",
                "correction": "사업주가 전액 부담한다고 정확히 통역",
                "explanation": "한국 산재보험은 100% 사업주 부담이므로 잘못 통역하면 혼란을 줍니다"
            },
            {
                "mistake": "산재보험은 큰 회사만 가입한다고 설명",
                "correction": "근로자를 사용하는 모든 사업장이 원칙적으로 의무가입 대상이라고 설명",
                "explanation": "일부 예외(가구내 고용, 농림어업 일부)를 제외하고는 사업장 규모와 무관하게 의무가입입니다"
            }
        ],
        "examples": [
            {
                "ko": "우리 회사는 산재보험에 가입되어 있어서 작업 중 다치면 치료비 걱정 없습니다.",
                "vi": "Công ty chúng tôi đã tham gia bảo hiểm tai nạn lao động, nên nếu bị thương trong khi làm việc sẽ không phải lo chi phí điều trị.",
                "situation": "onsite"
            },
            {
                "ko": "산재보험료는 사업주가 전액 부담하므로 근로자 급여에서 공제되지 않습니다.",
                "vi": "Phí bảo hiểm tai nạn lao động do người sử dụng lao động chi trả toàn bộ, không khấu trừ từ lương người lao động.",
                "situation": "formal"
            },
            {
                "ko": "외국인 근로자도 산재보험 혜택을 받을 수 있으니 안심하셔도 됩니다.",
                "vi": "Người lao động nước ngoài cũng được hưởng quyền lợi bảo hiểm tai nạn lao động, xin yên tâm.",
                "situation": "informal"
            }
        ],
        "relatedTerms": ["업무상재해", "근로복지공단", "요양급여", "휴업급여", "사회보험"]
    },
    {
        "slug": "tro-cap-dieu-tri",
        "korean": "요양급여",
        "vietnamese": "Trợ cấp điều trị",
        "hanja": "療養給與",
        "hanjaReading": "療(병 고칠 료) + 養(기를 양) + 給(줄 급) + 與(더불 여)",
        "pronunciation": "요양급여",
        "meaningKo": "업무상 재해를 입은 근로자의 부상이나 질병을 치료하기 위해 제공되는 급여입니다. 통역 시 강조할 점은 요양급여가 전액 무료라는 것입니다. 진찰, 검사, 약제, 처치, 수술, 입원 등 모든 의료비용을 근로복지공단이 직접 의료기관에 지급합니다. 베트남과 달리 본인부담금이 없으며, 비급여 항목도 일부 인정됩니다. 요양 기간 중에는 휴업급여도 별도로 지급되므로 생계 걱정 없이 치료에 전념할 수 있습니다. 통역 시 '무료 치료'라는 점을 명확히 전달하여 근로자들이 치료를 주저하지 않도록 해야 합니다.",
        "meaningVi": "Trợ cấp được cung cấp để điều trị chấn thương hoặc bệnh tật của người lao động gặp tai nạn lao động do công việc. Điểm quan trọng là trợ cấp điều trị hoàn toàn miễn phí. Khám bệnh, xét nghiệm, thuốc, xử trí, phẫu thuật, nhập viện - tất cả chi phí y tế được Tổng công ty Phúc lợi Người lao động Hàn Quốc (KCOMWEL) chi trả trực tiếp cho cơ sở y tế. Không có đồng chi trả. Trong thời gian điều trị còn được nhận trợ cấp nghỉ việc riêng, nên có thể yên tâm tập trung điều trị.",
        "context": "산재 신청, 의료기관 방문, 치료 절차 설명 시 사용",
        "culturalNote": "한국의 요양급여는 본인부담금이 전혀 없어 베트남 근로자들이 놀라는 경우가 많습니다. 베트남의 경우 사회보험 가입자도 의료비의 일부(20~40%)를 본인이 부담하는 것이 일반적이기 때문입니다. 또한 한국은 산재 전문 요양기관이 지정되어 있어 일반 병원과 별도로 운영됩니다. 통역 시 '완전 무료'라는 점을 강조하고, 요양급여 승인 전에도 응급 치료는 가능하다는 점을 안내해야 합니다.",
        "commonMistakes": [
            {
                "mistake": "chi phí y tế",
                "correction": "trợ cấp điều trị (hỗ trợ toàn bộ chi phí y tế)",
                "explanation": "단순 의료비가 아닌 산재보험에서 지급하는 법적 급여 개념입니다"
            },
            {
                "mistake": "일부 본인부담이 있다고 통역",
                "correction": "전액 무료이며 본인부담금이 없다고 정확히 통역",
                "explanation": "한국 산재보험의 요양급여는 100% 공단 부담이므로 잘못 통역하면 치료를 주저할 수 있습니다"
            },
            {
                "mistake": "치료비만 지원된다고 설명",
                "correction": "요양급여 외에 휴업급여, 장해급여 등 다른 급여도 별도로 지급된다고 설명",
                "explanation": "요양급여는 여러 산재급여 중 하나이며, 다른 급여와 중복 수급 가능합니다"
            }
        ],
        "examples": [
            {
                "ko": "산재 승인이 나면 요양급여로 모든 치료비가 무료로 처리됩니다.",
                "vi": "Khi được công nhận tai nạn lao động, tất cả chi phí điều trị sẽ được xử lý miễn phí thông qua trợ cấp điều trị.",
                "situation": "formal"
            },
            {
                "ko": "요양급여 기간 중에는 병원비 걱정 말고 치료에만 집중하세요.",
                "vi": "Trong thời gian nhận trợ cấp điều trị, hãy tập trung vào điều trị mà không phải lo chi phí bệnh viện.",
                "situation": "informal"
            },
            {
                "ko": "요양급여는 진찰부터 수술, 재활치료까지 포함됩니다.",
                "vi": "Trợ cấp điều trị bao gồm từ khám bệnh, phẫu thuật đến điều trị phục hồi chức năng.",
                "situation": "formal"
            }
        ],
        "relatedTerms": ["업무상재해", "산재보험", "휴업급여", "근로복지공단", "산재전문병원"]
    },
    {
        "slug": "tro-cap-nghi-viec",
        "korean": "휴업급여",
        "vietnamese": "Trợ cấp nghỉ việc",
        "hanja": "休業給與",
        "hanjaReading": "休(쉴 휴) + 業(업 업) + 給(줄 급) + 與(더불 여)",
        "pronunciation": "휴업급여",
        "meaningKo": "업무상 재해로 요양 중인 근로자가 일하지 못해 임금을 받지 못하는 기간 동안 지급되는 급여입니다. 통역 시 핵심은 평균임금의 70%가 지급되며, 치료 기간 내내 계속 받을 수 있다는 점입니다. 베트남의 병가수당(60%)보다 높고, 지급 기간에 제한이 없습니다. 휴업급여는 요양급여와 별도로 지급되므로 치료비 걱정 없이 생활비도 보장받을 수 있습니다. 또한 4일 이상 요양이 필요한 경우부터 지급되며, 최초 3일은 사업주가 평균임금을 지급해야 합니다. 통역 시 '치료 중에도 소득이 보장된다'는 점을 명확히 전달해야 합니다.",
        "meaningVi": "Trợ cấp được chi trả trong thời gian người lao động đang điều trị do tai nạn lao động và không thể làm việc nên không nhận được tiền lương. Điểm quan trọng là được chi trả 70% tiền lương trung bình, và tiếp tục nhận suốt thời gian điều trị mà không giới hạn thời hạn. Cao hơn trợ cấp ốm đau của Việt Nam (60%). Trợ cấp nghỉ việc được chi trả riêng ngoài trợ cấp điều trị, nên vừa không lo chi phí điều trị vừa được đảm bảo sinh hoạt phí. Được chi trả từ trường hợp cần điều trị từ 4 ngày trở lên, 3 ngày đầu do người sử dụng lao động chi trả tiền lương trung bình.",
        "context": "산재 휴직, 임금 보상, 생활비 지원 설명 시 사용",
        "culturalNote": "한국의 휴업급여는 베트남보다 관대합니다. 베트남은 사회보험법상 병가수당이 60%(5년 이상 가입 시 75%)이지만, 한국은 산재의 경우 일률적으로 70%입니다. 또한 베트남은 병가수당 지급 기간이 제한적이지만, 한국은 완치될 때까지 계속 지급됩니다. 베트남 근로자들은 산재로 오래 쉬면 해고될까 걱정하는 경우가 많은데, 한국은 산재 요양 기간 및 그 후 30일간 해고가 금지되므로 이 점을 명확히 안내해야 합니다.",
        "commonMistakes": [
            {
                "mistake": "tiền lương nghỉ việc",
                "correction": "trợ cấp nghỉ việc (70% tiền lương trung bình)",
                "explanation": "급여(급부) 개념이므로 '수당(trợ cấp)'으로 표현하고 비율을 명시해야 합니다"
            },
            {
                "mistake": "치료 끝나면 지급 중단된다고 통역",
                "correction": "요양이 필요한 기간 동안 계속 지급된다고 통역",
                "explanation": "완치 또는 증상 고정 시까지 지급되므로 기간 제한이 없습니다"
            },
            {
                "mistake": "첫날부터 휴업급여를 받는다고 설명",
                "correction": "4일째부터 휴업급여가 지급되며, 처음 3일은 사업주가 평균임금을 지급한다고 설명",
                "explanation": "대기기간 3일에 대한 정확한 설명이 필요합니다"
            }
        ],
        "examples": [
            {
                "ko": "산재로 한 달간 입원 치료를 받는 경우, 휴업급여로 평균임금의 70%를 받을 수 있습니다.",
                "vi": "Trường hợp nhập viện điều trị một tháng do tai nạn lao động, có thể nhận 70% tiền lương trung bình qua trợ cấp nghỉ việc.",
                "situation": "formal"
            },
            {
                "ko": "휴업급여는 요양급여와 별도로 지급되니 치료 중 생활비 걱정은 안 하셔도 됩니다.",
                "vi": "Trợ cấp nghỉ việc được chi trả riêng ngoài trợ cấp điều trị, nên không phải lo sinh hoạt phí trong khi điều trị.",
                "situation": "informal"
            },
            {
                "ko": "완치될 때까지 휴업급여를 계속 받을 수 있으니 충분히 쉬면서 치료받으세요.",
                "vi": "Có thể tiếp tục nhận trợ cấp nghỉ việc cho đến khi khỏi bệnh, nên hãy nghỉ ngơi đầy đủ và điều trị.",
                "situation": "onsite"
            }
        ],
        "relatedTerms": ["업무상재해", "요양급여", "평균임금", "산재보험", "근로복지공단"]
    },
    {
        "slug": "tro-cap-thuong-tat",
        "korean": "장해급여",
        "vietnamese": "Trợ cấp thương tật",
        "hanja": "障害給與",
        "hanjaReading": "障(막을 장) + 害(해칠 해) + 給(줄 급) + 與(더불 여)",
        "pronunciation": "장해급여",
        "meaningKo": "업무상 재해로 인해 완치 후에도 신체나 정신에 장해가 남은 경우 지급되는 급여입니다. 통역 시 중요한 점은 장해 정도에 따라 1급부터 14급까지 구분되며, 1~3급은 연금, 4~14급은 일시금으로 지급된다는 것입니다. 장해급여는 향후 근로능력 상실에 대한 보상이므로 금액이 상당히 큽니다. 예를 들어 1급 장해는 평균임금의 329일분을 매년 평생 받습니다. 베트남의 장해보상과 비교하면 한국이 훨씬 관대합니다. 통역 시 '완치 후에도 후유장해가 있으면 추가 보상을 받는다'는 점을 명확히 전달하여 근로자들이 자신의 권리를 제대로 주장할 수 있도록 해야 합니다.",
        "meaningVi": "Trợ cấp được chi trả khi sau khi khỏi bệnh do tai nạn lao động nhưng vẫn còn di chứng tàn tật về thể chất hoặc tinh thần. Điểm quan trọng là phân loại từ cấp 1 đến cấp 14 theo mức độ thương tật, cấp 1~3 nhận dạng lương hưu, cấp 4~14 nhận một lần. Trợ cấp thương tật là bồi thường cho sự mất khả năng lao động trong tương lai nên số tiền khá lớn. Ví dụ thương tật cấp 1 nhận 329 ngày tiền lương trung bình mỗi năm suốt đời. So với bồi thường thương tật của Việt Nam, Hàn Quốc hào phóng hơn nhiều. Cần giải thích rõ 'ngay cả sau khi khỏi bệnh, nếu còn di chứng thì được bồi thường thêm' để người lao động chủ động yêu cầu quyền lợi của mình.",
        "context": "산재 후유증, 장해 판정, 보상 청구 시 사용",
        "culturalNote": "한국의 장해급여는 국제적으로도 인정받는 선진적 제도입니다. 베트남은 장해 등급이 8등급으로 한국(14등급)보다 단순하며, 보상 수준도 낮습니다. 한국은 정신적 장해(PTSD 등)도 인정하지만, 베트남은 신체적 장해에 집중하는 경향이 있습니다. 베트남 근로자들은 '장해가 있어도 참고 일해야 한다'는 인식이 있어, 통역 시 '적극적으로 장해 판정을 받아 정당한 보상을 받을 권리가 있다'는 점을 강조해야 합니다. 또한 장해급여 외에 간병급여, 재활급여 등도 추가로 받을 수 있음을 안내해야 합니다.",
        "commonMistakes": [
            {
                "mistake": "bồi thường thương tật",
                "correction": "trợ cấp thương tật (급여)",
                "explanation": "민사상 손해배상이 아닌 사회보험 급여이므로 '보상(bồi thường)'보다 '급여(trợ cấp)'가 적절합니다"
            },
            {
                "mistake": "완치되면 더 이상 돈을 못 받는다고 통역",
                "correction": "완치 후에도 장해가 남으면 장해급여를 추가로 받는다고 통역",
                "explanation": "요양급여와 장해급여는 별개이며, 완치 후 장해 판정을 받아야 합니다"
            },
            {
                "mistake": "모든 장해급여가 일시금이라고 설명",
                "correction": "1~3급은 연금, 4~14급은 일시금이라고 정확히 설명",
                "explanation": "중증 장해는 평생 연금으로 받으므로 구분이 중요합니다"
            }
        ],
        "examples": [
            {
                "ko": "치료가 끝난 후 손가락 일부가 절단된 상태로 남아 장해급여 7급 판정을 받았습니다.",
                "vi": "Sau khi kết thúc điều trị, một phần ngón tay bị cắt cụt và được đánh giá trợ cấp thương tật cấp 7.",
                "situation": "formal"
            },
            {
                "ko": "1급 장해는 평생 연금으로 받을 수 있어 생활이 보장됩니다.",
                "vi": "Thương tật cấp 1 có thể nhận dưới dạng lương hưu suốt đời, nên cuộc sống được đảm bảo.",
                "situation": "formal"
            },
            {
                "ko": "장해가 남을 것 같으면 치료 종결 전에 반드시 장해 판정 신청을 해야 합니다.",
                "vi": "Nếu có khả năng để lại di chứng tàn tật, nhất định phải nộp đơn xin đánh giá thương tật trước khi kết thúc điều trị.",
                "situation": "onsite"
            }
        ],
        "relatedTerms": ["업무상재해", "요양급여", "근로능력상실", "장해등급", "장해연금"]
    },
    {
        "slug": "tro-cap-nguoi-than",
        "korean": "유족급여",
        "vietnamese": "Trợ cấp người thân",
        "hanja": "遺族給與",
        "hanjaReading": "遺(남길 유) + 族(겨레 족) + 給(줄 급) + 與(더불 여)",
        "pronunciation": "유족급여",
        "meaningKo": "업무상 재해로 근로자가 사망한 경우 그 유족에게 지급되는 급여입니다. 통역 시 핵심은 유족의 범위와 급여 형태입니다. 배우자, 자녀, 부모, 손자녀, 조부모, 형제자매 순으로 수급권이 있으며, 연금 또는 일시금 중 선택할 수 있습니다. 유족연금은 평균임금의 52~67%를 유족 수에 따라 매년 지급하며, 배우자가 사망할 때까지 또는 자녀가 성년이 될 때까지 지급됩니다. 베트남의 사망보상금(36개월분 급여)과 비교하면 한국이 훨씬 두텁습니다. 통역 시 '가족의 생계가 보장된다'는 점을 명확히 전달하여 유족들이 안심할 수 있도록 해야 합니다.",
        "meaningVi": "Trợ cấp được chi trả cho người thân khi người lao động tử vong do tai nạn lao động do công việc. Điểm quan trọng là phạm vi người thân và hình thức trợ cấp. Vợ/chồng, con cái, cha mẹ, cháu, ông bà, anh chị em có quyền nhận theo thứ tự, và có thể lựa chọn giữa lương hưu hoặc một lần. Lương hưu người thân chi trả 52~67% tiền lương trung bình mỗi năm tùy theo số người thân, và được chi trả cho đến khi vợ/chồng qua đời hoặc con cái thành niên. So với tiền bồi thường tử vong của Việt Nam (36 tháng lương), Hàn Quốc hậu hĩnh hơn nhiều. Cần giải thích rõ 'sinh kế của gia đình được đảm bảo' để người thân yên tâm.",
        "context": "산재 사망, 유족 보상, 장례비 지원 설명 시 사용",
        "culturalNote": "한국의 유족급여는 매우 포괄적입니다. 베트남은 사망보상금이 36개월분 급여로 일시금이지만, 한국은 평생 연금으로 받을 수 있어 유족의 생계가 장기적으로 보장됩니다. 또한 한국은 장의비(평균임금 120일분)도 별도로 지급됩니다. 베트남 근로자들의 경우 본국에 배우자와 자녀가 있는 경우가 많은데, 한국에서 산재 사망 시 본국 유족도 급여를 받을 수 있음을 명확히 안내해야 합니다. 유족급여 신청 시 가족관계증명서 등 서류 준비가 필요하므로 영사관 지원을 받을 수 있다는 점도 알려줘야 합니다.",
        "commonMistakes": [
            {
                "mistake": "tiền bồi thường tử vong",
                "correction": "trợ cấp người thân (lương hưu hoặc một lần)",
                "explanation": "민사 손해배상이 아닌 사회보험 급여이며, 연금 선택 가능"
            },
            {
                "mistake": "한국에 있는 가족만 받을 수 있다고 통역",
                "correction": "본국에 있는 배우자와 자녀도 유족급여를 받을 수 있다고 통역",
                "explanation": "유족의 거주지는 수급권에 영향을 주지 않습니다"
            },
            {
                "mistake": "일시금으로 한 번만 받는다고 설명",
                "correction": "연금 또는 일시금 중 선택할 수 있으며, 연금은 장기간 지급된다고 설명",
                "explanation": "유족연금은 조건 충족 시 평생 또는 장기간 지급됩니다"
            }
        ],
        "examples": [
            {
                "ko": "산재로 사망한 경우 배우자는 유족급여를 평생 받을 수 있습니다.",
                "vi": "Trường hợp tử vong do tai nạn lao động, vợ/chồng có thể nhận trợ cấp người thân suốt đời.",
                "situation": "formal"
            },
            {
                "ko": "유족급여는 장의비와 별도로 지급되니 장례 비용 걱정은 하지 않으셔도 됩니다.",
                "vi": "Trợ cấp người thân được chi trả riêng ngoài chi phí tang lễ, nên không phải lo chi phí tang lễ.",
                "situation": "informal"
            },
            {
                "ko": "베트남에 계신 가족분들도 유족급여를 받으실 수 있으니 서류를 준비해 주세요.",
                "vi": "Gia đình ở Việt Nam cũng có thể nhận trợ cấp người thân, xin chuẩn bị giấy tờ.",
                "situation": "onsite"
            }
        ],
        "relatedTerms": ["업무상재해", "산재보험", "장의비", "유족연금", "근로복지공단"]
    },
    {
        "slug": "benh-nghe-nghiep",
        "korean": "직업병",
        "vietnamese": "Bệnh nghề nghiệp",
        "hanja": "職業病",
        "hanjaReading": "職(직책 직) + 業(업 업) + 病(병 병)",
        "pronunciation": "직업병",
        "meaningKo": "업무상 유해·위험 요인에 장기간 노출되어 발생하는 질병을 말합니다. 통역 시 강조할 점은 직업병도 업무상재해로 인정되어 산재보험 혜택을 받을 수 있다는 것입니다. 한국은 법정 직업병(소음성 난청, 진폐증, 화학물질 중독 등)과 업무 관련성이 인정되는 질환(근골격계 질환, 뇌심혈관질환, 정신질환 등)을 모두 포괄합니다. 베트남보다 인정 범위가 넓으며, 특히 과로사(뇌출혈, 심근경색 등)와 직장 내 괴롭힘으로 인한 우울증도 업무상 질병으로 인정될 수 있습니다. 통역 시 '서서히 나타나는 질병도 산재로 인정받을 수 있다'는 점을 명확히 전달해야 합니다.",
        "meaningVi": "Bệnh phát sinh do tiếp xúc lâu dài với các yếu tố độc hại, nguy hiểm trong công việc. Điểm quan trọng là bệnh nghề nghiệp cũng được công nhận là tai nạn lao động do công việc và được hưởng quyền lợi bảo hiểm tai nạn lao động. Hàn Quốc bao gồm cả bệnh nghề nghiệp theo luật định (điếc do tiếng ồn, bệnh phổi bụi, ngộ độc hóa chất) và bệnh được công nhận có liên quan đến công việc (bệnh cơ xương khớp, bệnh tim mạch não, bệnh tâm thần). Phạm vi công nhận rộng hơn Việt Nam, đặc biệt tử vong do làm việc quá sức (xuất huyết não, nhồi máu cơ tim) và trầm cảm do bắt nạt nơi làm việc cũng có thể được công nhận là bệnh do công việc.",
        "context": "건강검진, 유해물질 취급, 만성질환 상담 시 사용",
        "culturalNote": "한국의 직업병 인정 범위는 점차 확대되고 있습니다. 2018년 김용균법 제정 후 중대재해처벌법까지 시행되면서 사업주의 안전·보건 의무가 강화되었습니다. 베트남도 2015년부터 직업병 목록을 확대했지만, 한국만큼 정신질환이나 과로사를 폭넓게 인정하지는 않습니다. 베트남 근로자들은 '아프면 참고 일해야 한다'는 인식이 있어, 통역 시 '몸이 안 좋으면 즉시 회사에 알리고 검사를 받아야 한다'는 점을 강조해야 합니다. 또한 직업병은 퇴직 후에도 발병하면 인정받을 수 있다는 점도 안내해야 합니다.",
        "commonMistakes": [
            {
                "mistake": "bệnh mãn tính",
                "correction": "bệnh nghề nghiệp (do công việc gây ra)",
                "explanation": "단순 만성병이 아닌 업무 기인성이 있는 질병입니다"
            },
            {
                "mistake": "사고로 다친 것만 산재라고 통역",
                "correction": "직업병도 업무상재해로 인정되어 산재보험 혜택을 받을 수 있다고 통역",
                "explanation": "급성 사고뿐만 아니라 만성적 질병도 산재에 포함됩니다"
            },
            {
                "mistake": "법에 명시된 질병만 인정된다고 설명",
                "correction": "법정 직업병 외에도 업무관련성이 인정되면 산재로 인정받을 수 있다고 설명",
                "explanation": "포괄주의 원칙으로 목록에 없어도 인정 가능합니다"
            }
        ],
        "examples": [
            {
                "ko": "소음이 심한 작업장에서 오래 일해서 청력이 나빠진 경우 직업병으로 인정받을 수 있습니다.",
                "vi": "Trường hợp thính lực kém đi do làm việc lâu ở nơi có tiếng ồn lớn có thể được công nhận là bệnh nghề nghiệp.",
                "situation": "formal"
            },
            {
                "ko": "허리 디스크도 반복적인 중량물 작업으로 생긴 것이면 직업병으로 신청할 수 있습니다.",
                "vi": "Thoát vị đĩa đệm cũng có thể nộp đơn xin công nhận bệnh nghề nghiệp nếu phát sinh do vận chuyển nặng lặp đi lặp lại.",
                "situation": "onsite"
            },
            {
                "ko": "화학공장에서 일하다 폐 질환이 생기면 직업병으로 산재 신청을 해야 합니다.",
                "vi": "Nếu mắc bệnh phổi do làm việc ở nhà máy hóa chất, cần nộp đơn xin công nhận tai nạn lao động với tư cách bệnh nghề nghiệp.",
                "situation": "formal"
            }
        ],
        "relatedTerms": ["업무상재해", "산재보험", "건강검진", "유해물질", "과로사"]
    },
    {
        "slug": "tai-nan-di-lam-ve",
        "korean": "출퇴근재해",
        "vietnamese": "Tai nạn đi làm về",
        "hanja": "出退勤災害",
        "hanjaReading": "出(날 출) + 退(물러날 퇴) + 勤(부지런할 근) + 災(재앙 재) + 害(해칠 해)",
        "pronunciation": "출퇴근재해",
        "meaningKo": "근로자가 출퇴근 중 발생한 사고로 부상·질병·장해 또는 사망한 경우를 말합니다. 통역 시 핵심은 2018년부터 출퇴근재해가 업무상재해로 인정된다는 점입니다. 주거지와 취업장소 사이의 합리적 경로와 방법으로 이동 중 발생한 사고는 산재로 보호받습니다. 다만 일탈·중단이 있으면 인정되지 않으며(일용품 구입 등 일상적 행위는 예외), 사업주가 제공한 교통수단 이용 중 사고는 더 넓게 인정됩니다. 베트남은 출퇴근 재해를 산재로 인정하지 않아 이 차이가 매우 중요합니다. 통역 시 '출퇴근 중 사고도 보호받는다'는 점을 명확히 전달하여 근로자들이 적극적으로 권리를 주장하도록 해야 합니다.",
        "meaningVi": "Trường hợp người lao động bị thương tích, mắc bệnh, tàn tật hoặc tử vong do tai nạn xảy ra trên đường đi làm về. Điểm quan trọng là từ năm 2018, tai nạn đi làm về được công nhận là tai nạn lao động do công việc. Tai nạn xảy ra trong quá trình di chuyển giữa nơi ở và nơi làm việc theo lộ trình và phương thức hợp lý được bảo vệ như tai nạn lao động. Tuy nhiên nếu có sự lệch hướng, gián đoạn thì không được công nhận (trừ hành vi thường ngày như mua hàng tiêu dùng), tai nạn khi sử dụng phương tiện do người sử dụng lao động cung cấp được công nhận rộng rãi hơn. Việt Nam không công nhận tai nạn đi làm về là tai nạn lao động nên sự khác biệt này rất quan trọng.",
        "context": "교통사고, 통근버스, 산재 신청 상담 시 사용",
        "culturalNote": "출퇴근재해 인정은 한국의 큰 진전입니다. 베트남은 2015년 노동법과 2014년 사회보험법에도 출퇴근 재해를 산재로 인정하지 않습니다. 베트남 근로자들은 '출근길 사고는 개인 문제'라고 생각하는 경우가 많아, 통역 시 '한국에서는 출퇴근 중 사고도 산재로 보호받는다'는 점을 강조해야 합니다. 다만 술에 취한 상태, 무면허 운전, 고의적 일탈 등은 제외되므로 합리적 경로와 방법의 중요성을 함께 설명해야 합니다. 특히 회사 통근버스 이용 중 사고는 거의 예외 없이 인정되므로 통근버스 이용을 권장해야 합니다.",
        "commonMistakes": [
            {
                "mistake": "tai nạn giao thông",
                "correction": "tai nạn đi làm về (tai nạn giao thông trên đường đi làm)",
                "explanation": "일반 교통사고가 아닌 출퇴근 맥락의 사고임을 명시해야 합니다"
            },
            {
                "mistake": "모든 출퇴근 중 사고가 다 인정된다고 통역",
                "correction": "합리적 경로와 방법으로 이동 중 발생한 사고만 인정된다고 통역",
                "explanation": "고의적 일탈이나 사적 용무 중 사고는 제외됩니다"
            },
            {
                "mistake": "출근길 사고는 개인이 알아서 처리해야 한다고 설명",
                "correction": "출퇴근재해도 산재로 신청하여 보호받을 수 있다고 설명",
                "explanation": "2018년부터 산재보험법에 명시적으로 포함되었습니다"
            }
        ],
        "examples": [
            {
                "ko": "출근길에 지하철 계단에서 넘어져 다친 경우 출퇴근재해로 산재 신청이 가능합니다.",
                "vi": "Trường hợp ngã trên cầu thang tàu điện ngầm và bị thương trên đường đi làm có thể nộp đơn xin công nhận tai nạn lao động với tư cách tai nạn đi làm về.",
                "situation": "formal"
            },
            {
                "ko": "회사 통근버스를 타고 가다 교통사고가 나면 출퇴근재해로 인정됩니다.",
                "vi": "Nếu xảy ra tai nạn giao thông khi đi xe buýt đưa đón của công ty, sẽ được công nhận là tai nạn đi làm về.",
                "situation": "onsite"
            },
            {
                "ko": "퇴근길에 마트에 잠깐 들렀다가 사고가 나면 출퇴근재해로 인정 안 될 수 있습니다.",
                "vi": "Nếu xảy ra tai nạn sau khi ghé qua siêu thị trên đường về, có thể không được công nhận là tai nạn đi làm về.",
                "situation": "informal"
            }
        ],
        "relatedTerms": ["업무상재해", "산재보험", "교통사고", "합리적경로", "통근버스"]
    },
    {
        "slug": "phong-ngua-tai-nan",
        "korean": "재해예방",
        "vietnamese": "Phòng ngừa tai nạn",
        "hanja": "災害豫防",
        "hanjaReading": "災(재앙 재) + 害(해칠 해) + 豫(미리 예) + 防(막을 방)",
        "pronunciation": "재해예방",
        "meaningKo": "산업재해가 발생하지 않도록 사전에 위험 요인을 제거하고 안전한 작업환경을 조성하는 활동을 말합니다. 통역 시 강조할 점은 재해예방이 사업주의 법적 의무라는 것입니다. 산업안전보건법에 따라 사업주는 위험성 평가, 안전교육, 보호구 지급, 안전설비 설치 등을 반드시 이행해야 하며, 이를 위반하면 처벌받습니다. 중대재해처벌법 시행 이후 경영책임자도 처벌 대상이 되었습니다. 베트남도 산업안전보건법(2015)이 있지만, 한국만큼 강력하게 집행되지 않습니다. 통역 시 '안전은 선택이 아닌 의무'라는 점을 명확히 전달하여 근로자들이 위험한 상황에서 작업을 거부할 권리가 있음을 인식하도록 해야 합니다.",
        "meaningVi": "Hoạt động loại bỏ các yếu tố nguy hiểm trước và tạo môi trường làm việc an toàn để tai nạn lao động không xảy ra. Điểm quan trọng là phòng ngừa tai nạn là nghĩa vụ pháp lý của người sử dụng lao động. Theo Luật An toàn và Sức khỏe Nghề nghiệp, người sử dụng lao động phải thực hiện đánh giá rủi ro, giáo dục an toàn, cấp phát đồ bảo hộ, lắp đặt thiết bị an toàn, và sẽ bị xử phạt nếu vi phạm. Sau khi Luật Xử phạt Tai nạn Nghiêm trọng có hiệu lực, người chịu trách nhiệm kinh doanh cũng là đối tượng bị xử phạt. Việt Nam cũng có Luật An toàn và Sức khỏe Nghề nghiệp (2015) nhưng không được thi hành mạnh mẽ như Hàn Quốc.",
        "context": "안전교육, 안전점검, 위험작업 지시 시 사용",
        "culturalNote": "한국은 중대재해처벌법(2022) 시행 이후 안전에 대한 인식이 크게 높아졌습니다. 사망사고 발생 시 대표이사가 처벌받을 수 있어 기업들이 안전투자를 확대하고 있습니다. 베트남은 아직 '생산성 우선, 안전은 나중'이라는 인식이 남아있어, 베트Nam 근로자들은 위험해도 참고 일하는 경향이 있습니다. 통역 시 '위험하면 작업을 중단하고 관리자에게 보고할 권리가 있다'는 점을 강조해야 합니다. 또한 안전교육 불참, 보호구 미착용은 근로자도 처벌받을 수 있으므로 양방향 의무를 명확히 전달해야 합니다.",
        "commonMistakes": [
            {
                "mistake": "an toàn lao động",
                "correction": "phòng ngừa tai nạn (hoạt động chủ động trước khi xảy ra)",
                "explanation": "'안전'은 상태이고, '예방'은 적극적 활동이므로 구분이 필요합니다"
            },
            {
                "mistake": "안전교육은 형식적이라고 통역",
                "correction": "안전교육은 법적 의무이며 불참 시 처벌받을 수 있다고 통역",
                "explanation": "안전교육을 경시하면 사고 발생 시 책임 문제가 생깁니다"
            },
            {
                "mistake": "위험해도 시키면 해야 한다고 설명",
                "correction": "명백히 위험한 작업은 거부할 권리가 있으며 이로 인해 불이익을 받으면 안 된다고 설명",
                "explanation": "산업안전보건법상 작업중지권이 보장되어 있습니다"
            }
        ],
        "examples": [
            {
                "ko": "재해예방을 위해 매달 안전교육을 실시하고 있으니 반드시 참석해 주세요.",
                "vi": "Để phòng ngừa tai nạn, chúng tôi thực hiện giáo dục an toàn hàng tháng, xin nhất định tham dự.",
                "situation": "formal"
            },
            {
                "ko": "안전모와 안전화는 재해예방을 위한 필수 보호구이니 작업 중 꼭 착용하세요.",
                "vi": "Mũ bảo hộ và giày bảo hộ là đồ bảo hộ cần thiết để phòng ngừa tai nạn, xin nhất định đeo trong khi làm việc.",
                "situation": "onsite"
            },
            {
                "ko": "위험한 상황이 보이면 즉시 작업을 멈추고 관리자에게 보고하는 것이 재해예방의 첫걸음입니다.",
                "vi": "Nếu thấy tình huống nguy hiểm, ngay lập tức dừng công việc và báo cáo cho quản lý là bước đầu tiên để phòng ngừa tai nạn.",
                "situation": "informal"
            }
        ],
        "relatedTerms": ["산업안전보건법", "안전교육", "보호구", "위험성평가", "중대재해처벌법"]
    },
    {
        "slug": "che-giau-tai-nan-lao-dong",
        "korean": "산재은폐",
        "vietnamese": "Che giấu tai nạn lao động",
        "hanja": "産災隱蔽",
        "hanjaReading": "産(날 산) + 災(재앙 재) + 隱(숨길 은) + 蔽(가릴 폐)",
        "pronunciation": "산재은폐",
        "meaningKo": "사업주가 산업재해 발생 사실을 고의로 숨기거나 축소 보고하는 불법 행위를 말합니다. 통역 시 핵심은 산재은폐가 범죄이며 사업주가 처벌받는다는 점입니다. 산업안전보건법 위반으로 7년 이하 징역 또는 1억원 이하 벌금에 처해질 수 있으며, 중대재해처벌법 적용 시 더 무거운 처벌을 받습니다. 사업주가 '병원비 내줄 테니 산재 신청하지 말라'고 회유하거나, '산재 신청하면 해고하겠다'고 협박하는 경우가 전형적인 산재은폐입니다. 베트남에서는 산재은폐가 흔한 관행이지만, 한국에서는 엄격히 처벌됩니다. 통역 시 '산재 신청은 근로자의 당연한 권리이며 이를 막는 것은 범죄'라는 점을 명확히 전달해야 합니다.",
        "meaningVi": "Hành vi bất hợp pháp của người sử dụng lao động cố ý che giấu hoặc báo cáo giảm nhẹ sự việc xảy ra tai nạn lao động. Điểm quan trọng là che giấu tai nạn lao động là tội phạm và người sử dụng lao động bị xử phạt. Vi phạm Luật An toàn và Sức khỏe Nghề nghiệp có thể bị phạt tù đến 7 năm hoặc phạt tiền đến 100 triệu won, và nếu áp dụng Luật Xử phạt Tai nạn Nghiêm trọng sẽ bị xử phạt nặng hơn. Trường hợp điển hình là người sử dụng lao động dỗ dành 'sẽ trả viện phí nên đừng nộp đơn xin công nhận tai nạn lao động', hoặc đe dọa 'nếu nộp đơn xin công nhận tai nạn lao động sẽ sa thải'. Ở Việt Nam, che giấu tai nạn lao động là thông lệ phổ biến, nhưng ở Hàn Quốc bị xử phạt nghiêm khắc.",
        "context": "노무관리, 산재 신청 거부, 권리 침해 상담 시 사용",
        "culturalNote": "산재은폐는 한국에서 심각한 사회문제로 인식되고 있습니다. 고용노동부는 산재은폐 신고 시 포상금을 지급하며, 익명 신고도 가능합니다. 베트남은 산재은폐에 대한 처벌이 약하고 근로감독이 느슨해 사업주들이 은폐를 시도하는 경우가 많습니다. 베트Nam 근로자들은 '사장님이 화내니까 참자', '돈 받으면 되지'라고 생각하기 쉬운데, 통역 시 '산재 신청을 막는 것은 범죄이며, 나중에 후유증이 생겨도 보상받을 수 없다'는 점을 강조해야 합니다. 또한 산재 신청을 이유로 한 해고는 무효이며, 부당해고 구제신청을 할 수 있음도 안내해야 합니다.",
        "commonMistakes": [
            {
                "mistake": "giấu tai nạn",
                "correction": "che giấu tai nạn lao động (hành vi vi phạm pháp luật)",
                "explanation": "단순히 숨기는 것이 아닌 법적 처벌 대상인 불법행위임을 명시해야 합니다"
            },
            {
                "mistake": "사장님이 주는 돈만 받고 끝내면 된다고 통역",
                "correction": "산재 신청을 막는 것은 불법이며, 나중에 후유증이 생겨도 보상받을 수 없다고 통역",
                "explanation": "즉각적 금전 수수는 장기적으로 근로자에게 불리합니다"
            },
            {
                "mistake": "산재 신청하면 회사에서 잘릴 거라고 설명",
                "correction": "산재 신청을 이유로 한 해고는 무효이며 부당해고로 구제받을 수 있다고 설명",
                "explanation": "산재 보복 조치는 법으로 금지되어 있습니다"
            }
        ],
        "examples": [
            {
                "ko": "회사에서 '산재 신청하지 말고 병원비만 받으라'고 하는 것은 산재은폐로 처벌받을 수 있습니다.",
                "vi": "Công ty nói 'đừng nộp đơn xin công nhận tai nạn lao động mà chỉ nhận viện phí' là che giấu tai nạn lao động và có thể bị xử phạt.",
                "situation": "formal"
            },
            {
                "ko": "산재은폐를 강요당하면 노동부나 근로복지공단에 신고할 수 있고, 신고자는 보호받습니다.",
                "vi": "Nếu bị ép buộc che giấu tai nạn lao động, có thể t고 발 cho Bộ Lao động hoặc Tổng công ty Phúc lợi Người lao động, và người tố cáo được bảo vệ.",
                "situation": "formal"
            },
            {
                "ko": "지금 돈 받고 넘어가면 나중에 후유증 생겨도 보상 못 받으니 꼭 산재 신청하세요.",
                "vi": "Nếu nhận tiền và qua mặt bây giờ, sau này có di chứng cũng không được bồi thường, nên nhất định nộp đơn xin công nhận tai nạn lao động.",
                "situation": "informal"
            }
        ],
        "relatedTerms": ["업무상재해", "산재보험", "부당해고", "고용노동부", "근로감독"]
    }
]


def load_existing_terms():
    """기존 용어 데이터 로드"""
    try:
        with open(TERMS_FILE, 'r', encoding='utf-8') as f:
            data = json.load(f)
            return data
    except FileNotFoundError:
        print(f"❌ 파일을 찾을 수 없습니다: {TERMS_FILE}")
        return None
    except json.JSONDecodeError as e:
        print(f"❌ JSON 파싱 오류: {e}")
        return None


def save_terms(terms):
    """용어 데이터 저장"""
    data = {"terms": terms}
    try:
        with open(TERMS_FILE, 'w', encoding='utf-8') as f:
            json.dump(data, f, ensure_ascii=False, indent=2)
        return True
    except Exception as e:
        print(f"❌ 저장 실패: {e}")
        return False


def main():
    print("=" * 60)
    print("한-베 통역 용어 플랫폼 - 법률 도메인 용어 추가")
    print("테마: 산업재해보상법")
    print("=" * 60)
    print()

    # 기존 용어 로드
    print("📂 기존 용어 데이터 로드 중...")
    existing_terms = load_existing_terms()

    if existing_terms is None:
        return

    print(f"✅ 기존 용어 수: {len(existing_terms)}개")
    print()

    # 중복 확인
    existing_slugs = {term['slug'] for term in existing_terms}
    new_slugs = {term['slug'] for term in NEW_TERMS}
    duplicates = existing_slugs & new_slugs

    if duplicates:
        print(f"⚠️  중복된 slug 발견: {duplicates}")
        print("❌ 작업 중단 (중복 제거 후 다시 실행)")
        return

    # 용어 추가
    print(f"➕ 신규 용어 {len(NEW_TERMS)}개 추가 중...")
    existing_terms.extend(NEW_TERMS)

    # 저장
    print("💾 파일 저장 중...")
    if save_terms(existing_terms):
        print()
        print("=" * 60)
        print("✅ 작업 완료!")
        print(f"📊 최종 용어 수: {len(existing_terms)}개")
        print(f"📁 저장 위치: {TERMS_FILE}")
        print()
        print("추가된 용어:")
        for i, term in enumerate(NEW_TERMS, 1):
            print(f"  {i}. {term['korean']} ({term['slug']})")
        print("=" * 60)
    else:
        print("❌ 저장 실패")


if __name__ == "__main__":
    main()
