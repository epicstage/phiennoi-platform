#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
법률 도메인 용어 추가 스크립트 v8-i
테마: 노동조합법 (노조설립, 단체협약, 쟁의조정, 필수유지업무, 복수노조, 교섭창구단일화, 유니언샵, 부당노동행위, 조합비, 전임자)
"""

import json
import os
from pathlib import Path

# 프로젝트 루트 찾기
script_dir = Path(__file__).parent
project_root = script_dir.parent.parent
terms_file = project_root / "src" / "data" / "terms" / "legal.json"

# 새로운 용어 10개 (노동조합법)
new_terms = [
    {
        "slug": "thanh-lap-cong-doan",
        "korean": "노동조합 설립",
        "vietnamese": "Thành lập công đoàn",
        "hanja": "勞動組合設立",
        "hanjaReading": "勞(일할 로) 動(움직일 동) 組(짤 조) 合(합할 합) 設(베풀 설) 立(설 립)",
        "pronunciation": "노동조합 설립",
        "meaningKo": "근로자들이 자주적으로 단결하여 근로조건의 유지·개선과 근로자의 경제적·사회적 지위 향상을 도모하기 위한 조직을 만드는 행위. 통역 시 한국은 자유설립주의(신고제)를 채택하고 있어 행정관청의 '허가'가 아닌 '신고'로 설립되는 점을 강조해야 하며, 베트남은 상급 공회 승인이 필요한 점과 대비하여 설명할 필요가 있음. 특히 '자유설립주의'는 베트남어로 'chủ nghĩa tự do thành lập'으로 직역보다는 '신고만으로 설립 가능'이라는 의미로 풀어 설명하는 것이 효과적. 설립 요건(근로자 2인 이상)과 규약 필수 기재사항을 언급할 때는 양국 차이를 명확히 구분.",
        "meaningVi": "Hành vi thành lập tổ chức do người lao động tự nguyện đoàn kết để duy trì, cải thiện điều kiện lao động và nâng cao vị thế kinh tế-xã hội. Hàn Quốc áp dụng chế độ tự do thành lập (chỉ cần đăng ký), khác với Việt Nam yêu cầu phê duyệt từ công đoàn cấp trên. Điều kiện: tối thiểu 2 người lao động, phải có điều lệ quy định các nội dung bắt buộc.",
        "context": "노동법, 단체교섭, 노사관계",
        "culturalNote": "한국은 헌법에서 보장하는 노동3권(단결권·단체교섭권·단체행동권)에 따라 자유설립주의를 채택하여 근로자 2인 이상이면 노동조합을 설립할 수 있으며, 행정관청에 신고만 하면 됨. 반면 베트남은 Luật Công đoàn(공회법)에 따라 상급 공회의 승인을 받아야 하며, 모든 노동조합은 베트남총공회(Tổng Liên đoàn Lao động Việt Nam) 산하로 통합되어 있어 복수노조가 사실상 불가능. 통역 시 '자유설립'과 '승인제'의 차이를 명확히 하고, 한국의 복수노조 허용 정책과 대비하여 설명해야 함.",
        "commonMistakes": [
            {
                "mistake": "노동조합을 'Liên đoàn lao động'로 번역",
                "correction": "'Công đoàn' 사용",
                "explanation": "'Liên đoàn'은 연합회를 의미하며, 개별 노동조합은 'Công đoàn'이 정확함"
            },
            {
                "mistake": "'설립 허가'를 'cho phép thành lập'로 표현",
                "correction": "'đăng ký thành lập'(설립 신고) 사용",
                "explanation": "한국은 허가제가 아닌 신고제이므로 '허가'가 아닌 '신고'로 표현해야 함"
            },
            {
                "mistake": "설립 요건을 '근로자 5인 이상'으로 안내",
                "correction": "근로자 2인 이상",
                "explanation": "노동조합법 제2조에 따라 2인 이상이면 설립 가능"
            },
            {
                "mistake": "베트남도 자유설립주의라고 설명",
                "correction": "베트남은 총공회 승인제",
                "explanation": "양국 제도 차이를 명확히 구분해야 함"
            }
        ],
        "examples": [
            {
                "ko": "우리 회사 직원 10명이 모여 노동조합 설립을 추진하고 있습니다.",
                "vi": "10 nhân viên trong công ty chúng tôi đang chuẩn bị thành lập công đoàn.",
                "situation": "informal"
            },
            {
                "ko": "노동조합 설립신고서를 관할 행정관청에 제출하였습니다.",
                "vi": "Đã nộp đơn đăng ký thành lập công đoàn cho cơ quan hành chính có thẩm quyền.",
                "situation": "formal"
            },
            {
                "ko": "한국은 2인 이상이면 자유롭게 노동조합을 설립할 수 있습니다.",
                "vi": "Ở Hàn Quốc, có thể tự do thành lập công đoàn với từ 2 người trở lên.",
                "situation": "onsite"
            }
        ],
        "relatedTerms": ["단체협약", "노동3권", "복수노조", "부당노동행위"]
    },
    {
        "slug": "thoa-uoc-tap-the",
        "korean": "단체협약",
        "vietnamese": "Thỏa ước tập thể",
        "hanja": "團體協約",
        "hanjaReading": "團(모일 단) 體(몸 체) 協(화할 협) 約(맺을 약)",
        "pronunciation": "단체협약",
        "meaningKo": "노동조합과 사용자 또는 사용자단체 간에 근로조건 기타 노사관계에 관한 사항을 정한 협정. 통역 시 단체협약의 법적 효력(규범적 효력, 채무적 효력)과 유효기간(2년 한도)을 정확히 전달해야 하며, 특히 '규범적 효력'은 개별 근로계약에 우선 적용되는 강력한 효력을 의미함을 강조. 베트남어 'Thỏa ước tập thể'는 단체협약과 노사협의를 포괄하는 개념이므로, 한국법상 '단체협약'(노조와 사용자 간)과 '노사협의'(노사협의회)를 명확히 구분하여 통역할 필요. 유효기간 만료 시 자동 연장 여부, 유리한 조건 우선 원칙 등 실무적 쟁점도 숙지.",
        "meaningVi": "Thỏa thuận giữa công đoàn và người sử dụng lao động (hoặc hiệp hội người sử dụng lao động) về điều kiện lao động và quan hệ lao động. Có hiệu lực pháp lý mạnh mẽ (hiệu lực quy phạm), ưu tiên áp dụng hơn hợp đồng lao động cá nhân. Thời hạn hiệu lực tối đa 2 năm tại Hàn Quốc. Cần phân biệt với 'thỏa thuận lao động' (thoả thuận trong hội đồng lao động) ở Hàn Quốc.",
        "context": "단체교섭, 노사관계, 근로조건",
        "culturalNote": "한국에서 단체협약은 노동조합법에 따라 노동조합과 사용자가 대등한 입장에서 체결하며, 규범적 효력으로 인해 개별 근로계약보다 우선 적용됨. 유효기간은 2년을 초과할 수 없으며, 기간 만료 후에도 새로운 협약이 체결될 때까지 효력 유지(자동 연장). 베트남은 Thỏa ước lao động tập thể(집체노동협약)가 유사 개념이나, 노동조합이 없는 기업도 근로자 대표와 협약을 체결할 수 있어 한국보다 범위가 넓음. 통역 시 한국의 단체협약은 '노동조합'이 당사자인 점을 명확히 하고, 베트남의 'đại diện người lao động'(근로자 대표)와 구별해야 함.",
        "commonMistakes": [
            {
                "mistake": "단체협약을 'Hợp đồng lao động tập thể'로 번역",
                "correction": "'Thỏa ước tập thể' 사용",
                "explanation": "'Hợp đồng'은 계약, 'Thỏa ước'은 협약으로 법적 성격이 다름"
            },
            {
                "mistake": "유효기간을 3년으로 안내",
                "correction": "2년 한도",
                "explanation": "노동조합법 제32조에 따라 2년 초과 불가"
            },
            {
                "mistake": "규범적 효력을 'hiệu lực bắt buộc'로만 설명",
                "correction": "'hiệu lực quy phạm, ưu tiên áp dụng hơn hợp đồng cá nhân'",
                "explanation": "개별 계약에 우선한다는 점까지 명확히 전달해야 함"
            },
            {
                "mistake": "노사협의회 합의를 단체협약이라고 설명",
                "correction": "노사협의는 단체협약과 별개",
                "explanation": "단체협약은 노조-사용자 간, 노사협의는 노사협의회 차원"
            }
        ],
        "examples": [
            {
                "ko": "올해 임금 인상률 3%를 담은 단체협약을 체결했습니다.",
                "vi": "Đã ký kết thỏa ước tập thể với mức tăng lương 3% trong năm nay.",
                "situation": "formal"
            },
            {
                "ko": "단체협약에 명시된 조건은 모든 근로자에게 적용됩니다.",
                "vi": "Các điều kiện ghi trong thỏa ước tập thể áp dụng cho tất cả người lao động.",
                "situation": "onsite"
            },
            {
                "ko": "단체협약 유효기간이 만료되어 재협상을 진행 중입니다.",
                "vi": "Thời hạn thỏa ước tập thể đã hết, đang tiến hành đàm phán lại.",
                "situation": "formal"
            }
        ],
        "relatedTerms": ["단체교섭", "규범적 효력", "노사협의", "근로조건"]
    },
    {
        "slug": "dieu-chinh-tranh-chap-lao-dong",
        "korean": "쟁의조정",
        "vietnamese": "Điều chỉnh tranh chấp lao động",
        "hanja": "爭議調整",
        "hanjaReading": "爭(다툴 쟁) 議(의논할 의) 調(고를 조) 整(가지런할 정)",
        "pronunciation": "쟁의조정",
        "meaningKo": "노동쟁의가 발생했을 때 당사자 간 자주적 해결이 어려운 경우 제3자가 개입하여 분쟁을 해결하는 절차로, 알선·조정·중재의 3단계로 구성됨. 통역 시 각 단계의 법적 효력과 절차를 명확히 구분해야 하며, 특히 '조정'은 권고적 효력만 있지만 '중재'는 재판상 화해와 동일한 강제력을 가짐을 강조. 공익사업의 경우 쟁의행위 전 필수적으로 조정을 거쳐야 하는 '조정전치주의'를 설명할 때는 베트남어로 'nguyên tắc hòa giải bắt buộc trước khi đình công'으로 풀어 설명하는 것이 효과적. 조정 기간(10~15일)과 냉각기간(10~15일) 준수 여부가 쟁의행위의 정당성 판단 기준임을 숙지.",
        "meaningVi": "Quy trình giải quyết tranh chấp lao động bằng sự can thiệp của bên thứ ba khi các bên không tự giải quyết được, gồm 3 giai đoạn: hòa giải (alson), điều đình (jojung), trọng tài (jungjae). 'Điều đình' chỉ có hiệu lực khuyến nghị, nhưng 'trọng tài' có hiệu lực bắt buộc như hòa giải tại tòa. Đối với ngành công ích, phải trải qua điều đình trước khi đình công (nguyên tắc điều đình tiên quyết). Thời gian điều đình 10-15 ngày, thời gian làm mát 10-15 ngày.",
        "context": "노동쟁의, 파업, 직장폐쇄",
        "culturalNote": "한국 노동조합법에서 쟁의조정은 알선(노동위원회 위원장이 중재자 지정) → 조정(조정위원회 구성, 10일 내 조정안 제시) → 중재(중재위원회 결정, 재판상 화해 효력)로 진행되며, 공익사업은 조정을 필수적으로 거쳐야 함(조정전치주의). 베트남은 '화해→노동조정→파업'의 3단계를 거쳐야 하며, 특히 불법 파업 시 형사처벌 가능성이 있어 한국보다 엄격. 통역 시 한국의 '중재'는 양 당사자가 합의해야 신청 가능하나, 필수공익사업은 일방 신청도 가능함을 설명하고, 베트남의 'trọng tài' 개념과 혼동하지 않도록 주의.",
        "commonMistakes": [
            {
                "mistake": "조정과 중재를 같은 의미로 사용",
                "correction": "조정(điều đình)은 권고, 중재(trọng tài)는 강제",
                "explanation": "법적 효력이 완전히 다름"
            },
            {
                "mistake": "알선을 'hòa giải'로 번역",
                "correction": "'dàn xếp' 또는 'thương lượng với sự hỗ trợ'",
                "explanation": "'hòa giải'는 정식 조정 절차를 의미하므로 구분 필요"
            },
            {
                "mistake": "모든 사업장이 조정전치주의 적용된다고 설명",
                "correction": "공익사업만 해당",
                "explanation": "일반 사업은 조정 없이 쟁의행위 가능"
            },
            {
                "mistake": "조정안 거부 시 불법이라고 안내",
                "correction": "조정안은 권고사항",
                "explanation": "중재와 달리 조정은 강제력 없음"
            }
        ],
        "examples": [
            {
                "ko": "노사 양측이 합의에 이르지 못해 노동위원회에 조정 신청을 했습니다.",
                "vi": "Do hai bên không đạt được thỏa thuận, đã nộp đơn xin điều đình lên Ủy ban Lao động.",
                "situation": "formal"
            },
            {
                "ko": "공익사업이므로 쟁의행위 전에 반드시 조정을 거쳐야 합니다.",
                "vi": "Vì là ngành công ích nên phải trải qua điều đình trước khi đình công.",
                "situation": "onsite"
            },
            {
                "ko": "중재 결정이 나왔으므로 양 당사자는 이를 따라야 합니다.",
                "vi": "Đã có quyết định trọng tài nên cả hai bên phải tuân theo.",
                "situation": "formal"
            }
        ],
        "relatedTerms": ["노동쟁의", "조정전치주의", "필수유지업무", "냉각기간"]
    },
    {
        "slug": "nghiep-vu-uy-tri-bat-buoc",
        "korean": "필수유지업무",
        "vietnamese": "Nghiệp vụ duy trì bắt buộc",
        "hanja": "必須維持業務",
        "hanjaReading": "必(반드시 필) 須(모름지기 수) 維(맬 유) 持(가질 지) 業(업 업) 務(일 무)",
        "pronunciation": "필수유지업무",
        "meaningKo": "쟁의행위 기간 중에도 국민의 생명·건강·신체의 안전 또는 일상생활을 현저히 위태롭게 하는 업무로서 정상적으로 유지·운영해야 하는 업무. 통역 시 필수유지업무는 파업 중에도 '반드시 수행해야 하는' 업무이며, 이를 위반하면 쟁의행위의 정당성을 상실하여 손해배상 및 형사처벌 대상이 될 수 있음을 명확히 전달. 베트남어로는 'nghiệp vụ bắt buộc duy trì ngay cả khi đình công'으로 풀어 설명하는 것이 효과적. 필수유지업무 대상(철도·도시철도·항공·수도·전기·가스·석유·병원·혈액공급 등)과 협정 체결 절차, 불이행 시 제재를 구체적으로 안내.",
        "meaningVi": "Công việc phải duy trì hoạt động bình thường ngay cả trong thời gian đình công để bảo vệ sinh mạng, sức khỏe, an toàn thân thể hoặc đời sống hàng ngày của người dân. Nếu vi phạm, đình công mất tính chính đáng và có thể bị bồi thường thiệt hại, xử phạt hình sự. Áp dụng cho đường sắt, tàu điện ngầm, hàng không, nước, điện, gas, dầu, bệnh viện, cung cấp máu, v.v. Phải ký thỏa thuận duy trì nghiệp vụ bắt buộc trước khi đình công.",
        "context": "공익사업, 파업, 쟁의행위",
        "culturalNote": "한국 노동조합법 제42조의2~42조의6에 따라 필수공익사업(철도·항공·수도·전기·가스 등)은 쟁의행위 시에도 최소한의 업무를 유지해야 하며, 노사가 사전에 '필수유지업무 협정'을 체결해야 함. 협정 불이행 시 노동위원회가 결정하며, 이를 위반하면 쟁의행위가 불법이 됨. 베트남은 공공서비스 파업 시 사전 통지와 최소 서비스 유지 의무가 있으나, 한국만큼 상세한 협정 절차는 없음. 통역 시 '필수유지업무 협정'(thỏa thuận duy trì nghiệp vụ bắt buộc)과 '필수유지업무 결정'(quyết định duy trì nghiệp vụ bắt buộc)을 구분하고, 위반 시 '정당성 상실'(mất tính chính đáng)을 명확히 전달.",
        "commonMistakes": [
            {
                "mistake": "모든 공익사업이 필수유지업무 대상이라고 설명",
                "correction": "필수공익사업 중 법정 지정 업종만 해당",
                "explanation": "철도·항공·수도·전기·가스·석유·병원·혈액 등 한정"
            },
            {
                "mistake": "필수유지업무 협정을 '선택사항'으로 안내",
                "correction": "쟁의행위 전 필수 체결",
                "explanation": "협정 없으면 노동위원회가 결정"
            },
            {
                "mistake": "'필수유지업무'를 'nghiệp vụ cần thiết'로 번역",
                "correction": "'nghiệp vụ duy trì bắt buộc' 또는 'nghiệp vụ thiết yếu duy trì'",
                "explanation": "'bắt buộc'(강제성)를 명확히 표현해야 함"
            },
            {
                "mistake": "위반 시 '경고'만 받는다고 설명",
                "correction": "손해배상·형사처벌 가능",
                "explanation": "쟁의행위 정당성 상실로 민·형사 책임 발생"
            }
        ],
        "examples": [
            {
                "ko": "지하철 파업 시에도 출퇴근 시간대 최소 운행은 필수유지업무입니다.",
                "vi": "Ngay cả khi đình công tàu điện ngầm, vẫn phải duy trì tối thiểu chuyến đi giờ cao điểm, đây là nghiệp vụ duy trì bắt buộc.",
                "situation": "onsite"
            },
            {
                "ko": "필수유지업무 협정을 체결하지 않아 노동위원회가 결정을 내렸습니다.",
                "vi": "Do không ký thỏa thuận duy trì nghiệp vụ bắt buộc, Ủy ban Lao động đã ra quyết định.",
                "situation": "formal"
            },
            {
                "ko": "병원 응급실은 파업 중에도 정상 운영해야 하는 필수유지업무입니다.",
                "vi": "Phòng cấp cứu bệnh viện là nghiệp vụ duy trì bắt buộc, phải hoạt động bình thường ngay cả khi đình công.",
                "situation": "formal"
            }
        ],
        "relatedTerms": ["공익사업", "쟁의행위", "조정전치주의", "필수공익사업"]
    },
    {
        "slug": "da-cong-doan",
        "korean": "복수노조",
        "vietnamese": "Đa công đoàn",
        "hanja": "複數勞組",
        "hanjaReading": "複(겹 복) 數(셀 수) 勞(일할 로) 組(짤 조)",
        "pronunciation": "복수노조",
        "meaningKo": "하나의 사업 또는 사업장에 2개 이상의 노동조합이 설립·존재하는 것. 통역 시 한국은 2011년부터 복수노조를 법적으로 허용하고 있으며, 이전에는 '1사 1노조' 원칙이 적용되었던 역사를 설명할 필요가 있음. 복수노조 허용으로 인해 '교섭창구 단일화' 제도가 도입되었으며, 이는 사용자가 여러 노조와 개별 교섭하는 부담을 줄이기 위한 것임을 명확히 전달. 베트남은 사실상 단일 노조(베트남총공회 산하)만 인정되므로, 'đa công đoàn'은 한국의 특수한 제도임을 강조하고, '교섭권 분산'과 '노노갈등' 가능성 등 실무적 쟁점도 언급.",
        "meaningVi": "Sự tồn tại của từ 2 công đoàn trở lên trong một doanh nghiệp hoặc nơi làm việc. Hàn Quốc cho phép đa công đoàn từ năm 2011 (trước đó áp dụng nguyên tắc '1 công ty 1 công đoàn'). Do cho phép đa công đoàn, đã áp dụng chế độ 'thống nhất cửa đàm phán' (joseupchanggu dan-ilhwa) để tránh gánh nặng đàm phán với nhiều công đoàn. Việt Nam chỉ công nhận công đoàn duy nhất (trực thuộc Tổng Liên đoàn Lao động Việt Nam), nên 'đa công đoàn' là chế độ đặc thù của Hàn Quốc.",
        "context": "노사관계, 단체교섭, 교섭창구단일화",
        "culturalNote": "한국은 2011년 노동조합법 개정으로 복수노조를 허용하면서 동시에 교섭창구 단일화 제도를 도입함. 이는 하나의 사업장에 여러 노조가 있을 때 교섭 대표를 단일화하여 사용자의 교섭 부담을 줄이기 위한 것. 교섭 대표 노조는 조합원 과반수 지지를 받거나, 과반 노조가 없을 경우 교섭대표단을 구성함. 베트남은 모든 노조가 베트남총공회 산하로 통합되어 있어 복수노조 개념이 없으며, 기업 내 '지부'(chi bộ) 형태로만 존재. 통역 시 한국의 복수노조는 '경쟁적 노조 체제'(hệ thống công đoàn cạnh tranh)로 설명할 수 있으며, 노노갈등·조합원 쟁탈전 등 부작용도 함께 언급하는 것이 맥락 이해에 도움.",
        "commonMistakes": [
            {
                "mistake": "복수노조를 'nhiều công đoàn'으로만 번역",
                "correction": "'đa công đoàn' 또는 'chế độ đa công đoàn'",
                "explanation": "법률 용어로 정착된 표현 사용"
            },
            {
                "mistake": "복수노조가 항상 허용되었다고 설명",
                "correction": "2011년부터 허용",
                "explanation": "이전에는 1사 1노조 원칙 적용"
            },
            {
                "mistake": "모든 노조가 개별 교섭 가능하다고 안내",
                "correction": "교섭창구 단일화 필수",
                "explanation": "교섭 대표 노조를 정해야 함"
            },
            {
                "mistake": "베트남도 복수노조가 가능하다고 설명",
                "correction": "베트남은 단일 노조 체제",
                "explanation": "총공회 산하로만 조직 가능"
            }
        ],
        "examples": [
            {
                "ko": "우리 회사에는 3개의 노동조합이 있어 복수노조 체제입니다.",
                "vi": "Công ty chúng tôi có 3 công đoàn, áp dụng chế độ đa công đoàn.",
                "situation": "informal"
            },
            {
                "ko": "복수노조 허용으로 노조 간 경쟁이 심화되었습니다.",
                "vi": "Việc cho phép đa công đoàn đã làm gia tăng cạnh tranh giữa các công đoàn.",
                "situation": "formal"
            },
            {
                "ko": "복수노조 시대에는 교섭창구 단일화가 필수입니다.",
                "vi": "Trong thời đại đa công đoàn, việc thống nhất cửa đàm phán là bắt buộc.",
                "situation": "onsite"
            }
        ],
        "relatedTerms": ["교섭창구단일화", "단체교섭", "노동조합", "1사1노조"]
    },
    {
        "slug": "thong-nhat-cua-dam-phan",
        "korean": "교섭창구 단일화",
        "vietnamese": "Thống nhất cửa đàm phán",
        "hanja": "交涉窓口單一化",
        "hanjaReading": "交(사귈 교) 涉(건널 섭) 窓(창 창) 口(입 구) 單(홑 단) 一(한 일) 化(될 화)",
        "pronunciation": "교섭창구 단일화",
        "meaningKo": "하나의 사업 또는 사업장에 복수의 노동조합이 있을 때 교섭 대표를 단일화하여 사용자와 교섭하는 제도. 통역 시 교섭창구 단일화는 '사용자의 교섭 부담 경감'과 '노조 간 공정한 경쟁'을 목적으로 하며, 교섭 대표 노조 결정 방식(과반수 노조 또는 교섭대표단 구성)을 정확히 설명해야 함. 특히 '조합원 수 과반'과 '조합원 과반 지지'를 혼동하지 않도록 주의하며, 교섭창구 단일화 절차는 '자율 단일화(30일) → 공동교섭대표단 구성'으로 진행됨을 명시. 베트남에는 복수노조가 없어 이 제도가 존재하지 않으므로, 한국의 특수 제도임을 강조하고 '단일화 실패 시 노동위원회 결정' 등 예외 사항도 안내.",
        "meaningVi": "Chế độ thống nhất đại diện đàm phán khi có nhiều công đoàn trong một doanh nghiệp, để đàm phán với người sử dụng lao động. Mục đích: giảm gánh nặng đàm phán cho người sử dụng lao động và đảm bảo cạnh tranh công bằng giữa các công đoàn. Cách quyết định đại diện đàm phán: công đoàn có hơn 50% tổng số hội viên, hoặc thành lập đoàn đại diện đàm phán chung. Quy trình: tự nguyện thống nhất (30 ngày) → thành lập đoàn đại diện chung. Chế độ đặc thù của Hàn Quốc (Việt Nam không có do không có đa công đoàn).",
        "context": "복수노조, 단체교섭, 노사관계",
        "culturalNote": "한국 노동조합법 제29조의2에 따라 복수노조 사업장은 교섭창구를 단일화해야 하며, 이는 사용자가 여러 노조와 개별 교섭하는 혼란을 방지하기 위함. 교섭 대표 결정은 ①조합원 과반수 노조 자동 대표, ②과반 노조 없을 시 자율적 교섭대표단 구성(30일 내), ③자율 실패 시 공동교섭대표단 구성(조합원 10% 이상 노조 참여)으로 진행. 교섭 대표가 된 노조는 소수 노조 의견도 수렴해야 하는 '공정대표의무'를 부담함. 베트남은 단일 노조 체제라 이런 제도가 없으며, 통역 시 '창구 단일화'를 직역하지 말고 'thống nhất đại diện đàm phán'(대표 단일화)로 설명하는 것이 이해하기 쉬움.",
        "commonMistakes": [
            {
                "mistake": "'교섭창구'를 'cửa đàm phán'으로만 번역",
                "correction": "'cửa đàm phán' 또는 '채널 đàm phán'",
                "explanation": "'창구'는 접점·채널의 의미이므로 'kênh' 추가 가능"
            },
            {
                "mistake": "교섭 대표를 조합원 수가 가장 많은 노조로만 설명",
                "correction": "과반 노조 또는 교섭대표단",
                "explanation": "과반이 없으면 연합 구성"
            },
            {
                "mistake": "소수 노조는 교섭에 참여 못 한다고 안내",
                "correction": "교섭대표단 구성 시 10% 이상 노조는 참여 가능",
                "explanation": "공동교섭대표단에 포함될 수 있음"
            },
            {
                "mistake": "자율 단일화 기간을 '제한 없음'으로 설명",
                "correction": "30일 기한",
                "explanation": "기간 내 합의 못 하면 공동대표단 구성"
            }
        ],
        "examples": [
            {
                "ko": "3개 노조 중 조합원 수가 가장 많은 A노조가 교섭 대표가 되었습니다.",
                "vi": "Trong 3 công đoàn, công đoàn A có số hội viên nhiều nhất đã trở thành đại diện đàm phán.",
                "situation": "formal"
            },
            {
                "ko": "교섭창구 단일화 절차를 거쳐 공동교섭대표단을 구성했습니다.",
                "vi": "Đã thành lập đoàn đại diện đàm phán chung sau quy trình thống nhất cửa đàm phán.",
                "situation": "formal"
            },
            {
                "ko": "소수 노조도 교섭대표단에 참여할 수 있는 권리가 있습니다.",
                "vi": "Công đoàn thiểu số cũng có quyền tham gia đoàn đại diện đàm phán.",
                "situation": "onsite"
            }
        ],
        "relatedTerms": ["복수노조", "공정대표의무", "단체교섭", "교섭대표"]
    },
    {
        "slug": "union-shop",
        "korean": "유니언샵",
        "vietnamese": "Union shop",
        "hanja": None,
        "hanjaReading": None,
        "pronunciation": "유니언샵",
        "meaningKo": "근로자가 입사 후 일정 기간 내에 노동조합에 가입하지 않으면 사용자가 해고할 수 있도록 하는 단체협약상의 조항. 통역 시 유니언샵은 '조합 가입 강제' 조항이며, 한국에서는 합법이나 헌법재판소가 '조합 탈퇴 및 재가입 자유'를 보장하라는 조건부 합헌 결정을 내린 점을 명확히 전달. 특히 '조합 탈퇴 후 해고'는 위헌이므로, 실무에서는 유니언샵 조항이 있어도 탈퇴 근로자를 해고할 수 없음을 강조. 베트남어로는 'điều khoản bắt buộc gia nhập công đoàn'(조합 가입 강제 조항)으로 풀어 설명하거나, 영어 그대로 'Union shop'을 사용하되 주석 추가. 클로즈드샵(closed shop, 입사 전 조합 가입 필수)과 구분하여 설명.",
        "meaningVi": "Điều khoản trong thỏa ước tập thể cho phép người sử dụng lao động sa thải người lao động nếu họ không gia nhập công đoàn trong thời hạn nhất định sau khi vào làm. Hợp pháp tại Hàn Quốc nhưng Tòa Hiến pháp quy định phải bảo đảm quyền rút khỏi công đoàn và tái gia nhập (quyết định hợp hiến có điều kiện). Thực tế, không thể sa thải người lao động rút khỏi công đoàn. Khác với 'Closed shop' (bắt buộc gia nhập công đoàn trước khi vào làm).",
        "context": "단체협약, 조합 가입, 고용 조건",
        "culturalNote": "한국에서 유니언샵 조항은 노동조합의 조직력 강화를 위해 단체협약에 명시되며, 신규 입사자는 일정 기간(보통 3개월) 내 조합 가입을 해야 함. 2005년 헌법재판소는 유니언샵 자체는 합헌이나 '조합 탈퇴의 자유'를 제한하면 위헌이라고 판단(조건부 합헌). 따라서 탈퇴 후 해고는 불가하며, 실무에서는 유니언샵 조항이 있어도 탈퇴자를 해고하면 부당해고가 됨. 베트남은 노조 가입이 자유이며 유니언샵 개념이 없음. 통역 시 'Union shop'을 그대로 사용하거나 'chế độ bắt buộc gia nhập công đoàn sau khi tuyển dụng'로 설명하고, 클로즈드샵(입사 전 가입)과 차이를 명확히 하며, 현재는 탈퇴 자유 보장으로 실효성이 약화된 점도 언급.",
        "commonMistakes": [
            {
                "mistake": "유니언샵을 'cửa hàng công đoàn'으로 직역",
                "correction": "'Union shop' 또는 'điều khoản bắt buộc gia nhập công đoàn'",
                "explanation": "직역하면 의미 불명, 개념 설명 필요"
            },
            {
                "mistake": "조합 탈퇴 시 자동 해고된다고 설명",
                "correction": "탈퇴 후 해고는 위헌",
                "explanation": "헌재 결정으로 탈퇴 자유 보장"
            },
            {
                "mistake": "클로즈드샵과 유니언샵을 같은 의미로 사용",
                "correction": "클로즈드샵은 입사 전 가입, 유니언샵은 입사 후 가입",
                "explanation": "시점 차이가 핵심"
            },
            {
                "mistake": "유니언샵이 모든 사업장에 적용된다고 안내",
                "correction": "단체협약에 명시된 경우만 해당",
                "explanation": "법적 의무 아닌 협약 사항"
            }
        ],
        "examples": [
            {
                "ko": "우리 회사는 유니언샵 조항이 있어 입사 3개월 내 조합 가입이 필요합니다.",
                "vi": "Công ty chúng tôi có điều khoản Union shop nên phải gia nhập công đoàn trong 3 tháng sau khi vào làm.",
                "situation": "informal"
            },
            {
                "ko": "유니언샵 조항이 있어도 조합 탈퇴 후 해고는 불법입니다.",
                "vi": "Ngay cả khi có điều khoản Union shop, sa thải sau khi rút khỏi công đoàn là bất hợp pháp.",
                "situation": "formal"
            },
            {
                "ko": "헌법재판소 결정으로 유니언샵의 강제력이 약화되었습니다.",
                "vi": "Quyết định của Tòa Hiến pháp đã làm giảm tính bắt buộc của Union shop.",
                "situation": "onsite"
            }
        ],
        "relatedTerms": ["단체협약", "조합 가입", "클로즈드샵", "조합 탈퇴"]
    },
    {
        "slug": "hanh-vi-lao-dong-bat-cong",
        "korean": "부당노동행위",
        "vietnamese": "Hành vi lao động bất công",
        "hanja": "不當勞動行爲",
        "hanjaReading": "不(아닐 부) 當(마땅 당) 勞(일할 로) 動(움직일 동) 行(다닐 행) 爲(할 위)",
        "pronunciation": "부당노동행위",
        "meaningKo": "사용자가 근로자의 노동3권(단결권·단체교섭권·단체행동권)을 침해하는 행위로, 노동조합법에서 금지하고 있는 5가지 유형(불이익 취급, 지배·개입, 단체교섭 거부, 경비 원조, 보복적 불이익)을 의미함. 통역 시 부당노동행위는 '사용자만' 위반 주체가 될 수 있으며, 노동위원회에 구제 신청 가능하고, 위반 시 2년 이하 징역 또는 2천만 원 이하 벌금이라는 형사처벌까지 받을 수 있음을 명확히 전달. 베트남어로는 'hành vi vi phạm quyền lao động'(노동권 침해 행위)보다 'hành vi lao động bất công'(불공정 노동행위)이 더 정확하며, 5가지 유형을 구체적으로 열거하여 설명하는 것이 효과적. 특히 '지배·개입'(can thiệp, chi phối)은 노조 운영 방해·어용노조 지원 등을 포함함을 강조.",
        "meaningVi": "Hành vi của người sử dụng lao động xâm phạm quyền lao động 3 quyền (quyền đoàn kết, quyền đàm phán tập thể, quyền hành động tập thể), bị cấm theo Luật Công đoàn Hàn Quốc. 5 loại: ①đối xử bất lợi, ②chi phối/can thiệp, ③từ chối đàm phán tập thể, ④hỗ trợ kinh phí, ⑤bất lợi trả đũa. Chỉ người sử dụng lao động có thể vi phạm. Có thể đơn cứu tế lên Ủy ban Lao động, vi phạm bị phạt tù đến 2 năm hoặc phạt tiền đến 20 triệu won.",
        "context": "노동3권, 노사관계, 노동위원회",
        "culturalNote": "한국 노동조합법 제81조는 부당노동행위를 ①불리한 처우(조합 활동 이유로 해고·징계), ②지배·개입(노조 운영 간섭·어용노조 지원), ③단체교섭 거부(정당한 이유 없이 교섭 거부), ④경비 원조(노조 운영비 지원, 단 근무시간 중 급여 지급·최소 사무실 제공은 예외), ⑤보복적 불이익(노동위원회 신고 등을 이유로 불이익)으로 구분함. 근로자는 노동위원회에 구제 신청 가능하며, 구제명령 불이행 시 이행강제금 부과. 베트남은 '차별 금지'(cấm phân biệt đối xử) 조항은 있으나 부당노동행위만큼 상세한 규정은 없음. 통역 시 5가지 유형을 명확히 구분하고, 특히 '경비 원조'는 원칙적 금지이나 예외(급여·사무실)가 있음을 설명.",
        "commonMistakes": [
            {
                "mistake": "부당노동행위를 'hành vi lao động bất hợp pháp'로 번역",
                "correction": "'hành vi lao động bất công' 또는 'hành vi chống công đoàn'",
                "explanation": "'bất hợp pháp'은 불법, 'bất công'은 불공정·부당"
            },
            {
                "mistake": "근로자도 부당노동행위 주체가 될 수 있다고 설명",
                "correction": "사용자만 해당",
                "explanation": "노조법상 사용자의 위반 행위만 부당노동행위"
            },
            {
                "mistake": "노조에 경비 지원은 모두 금지라고 안내",
                "correction": "급여 지급·최소 사무실 제공은 예외",
                "explanation": "원칙 금지, 예외 인정"
            },
            {
                "mistake": "부당노동행위 구제는 법원에만 신청 가능하다고 설명",
                "correction": "노동위원회에 먼저 신청",
                "explanation": "행정 구제 우선, 불복 시 법원"
            }
        ],
        "examples": [
            {
                "ko": "조합 활동을 이유로 근로자를 해고하는 것은 부당노동행위입니다.",
                "vi": "Sa thải người lao động vì hoạt động công đoàn là hành vi lao động bất công.",
                "situation": "formal"
            },
            {
                "ko": "사용자가 노조 선거에 개입하는 것은 부당노동행위에 해당합니다.",
                "vi": "Người sử dụng lao động can thiệp vào bầu cử công đoàn là hành vi lao động bất công.",
                "situation": "onsite"
            },
            {
                "ko": "부당노동행위 구제 신청을 노동위원회에 제출했습니다.",
                "vi": "Đã nộp đơn cứu tế hành vi lao động bất công lên Ủy ban Lao động.",
                "situation": "formal"
            }
        ],
        "relatedTerms": ["노동3권", "노동위원회", "구제명령", "이행강제금"]
    },
    {
        "slug": "phi-cong-doan",
        "korean": "조합비",
        "vietnamese": "Phí công đoàn",
        "hanja": "組合費",
        "hanjaReading": "組(짤 조) 合(합할 합) 費(쓸 비)",
        "pronunciation": "조합비",
        "meaningKo": "노동조합 조합원이 조합 운영을 위해 정기적으로 납부하는 회비. 통역 시 조합비는 조합원의 '의무'이며, 통상 월 급여의 1~1.5% 수준이고, 체크오프(check-off, 사용자가 급여에서 공제하여 노조에 일괄 송금하는 제도)를 통해 징수되는 경우가 많음을 설명. 체크오프는 단체협약에 명시되어야 하며, 개별 조합원의 동의가 필요함을 명확히 전달. 베트남어로는 'phí công đoàn' 또는 'hội phí công đoàn'이 적절하며, 체크오프는 'khấu trừ lương để nộp phí công đoàn'(급여 공제로 조합비 납부)으로 풀어 설명. 조합비 미납 시 조합원 자격 상실 가능성, 사용자의 체크오프 거부가 부당노동행위가 될 수 있는 점도 언급.",
        "meaningVi": "Khoản phí mà hội viên công đoàn phải đóng định kỳ để vận hành công đoàn. Là nghĩa vụ của hội viên, thường là 1-1.5% lương tháng. Thường được thu qua chế độ 'check-off' (người sử dụng lao động khấu trừ từ lương và chuyển khoản hàng loạt cho công đoàn). Check-off phải ghi trong thỏa ước tập thể và có sự đồng ý của từng hội viên. Nếu không nộp phí, có thể mất tư cách hội viên. Người sử dụng lao động từ chối check-off có thể là hành vi lao động bất công.",
        "context": "노동조합, 조합 운영, 체크오프",
        "culturalNote": "한국에서 조합비는 노동조합 규약에 납부 의무와 금액(또는 비율)이 명시되며, 대부분 월 급여의 1~1.5%를 징수함. 체크오프 제도는 사용자가 급여에서 조합비를 일괄 공제하여 노조에 송금하는 방식으로, 조합원의 편의와 노조의 안정적 재정 확보를 위해 단체협약에 규정됨. 체크오프는 개별 조합원의 동의가 필요하며, 동의 철회 시 직접 납부로 전환됨. 베트남은 공회비(phí công đoàn)를 급여의 1%로 법정하여 사용자가 2%, 근로자가 1%를 부담하며, 한국과 달리 법으로 강제됨. 통역 시 한국의 조합비는 '조합 자율'로 결정되고 베트남은 '법정 1%'인 점을 대비하여 설명하며, 체크오프는 'khấu trừ tự động'(자동 공제)로 간단히 표현 가능.",
        "commonMistakes": [
            {
                "mistake": "조합비를 'lệ phí công đoàn'로 번역",
                "correction": "'phí công đoàn' 또는 'hội phí'",
                "explanation": "'lệ phí'는 행정 수수료, 'phí/hội phí'가 회비"
            },
            {
                "mistake": "조합비를 법으로 정한다고 설명",
                "correction": "조합 규약으로 자율 결정",
                "explanation": "법정 금액 없음, 조합마다 다름"
            },
            {
                "mistake": "체크오프는 조합원 동의 없이 가능하다고 안내",
                "correction": "개별 동의 필수",
                "explanation": "동의 없는 공제는 위법"
            },
            {
                "mistake": "조합비 미납 시 자동 해고된다고 설명",
                "correction": "조합원 자격 상실 가능",
                "explanation": "고용 관계와 무관, 조합원 지위만 영향"
            }
        ],
        "examples": [
            {
                "ko": "매월 급여의 1.2%를 조합비로 납부하고 있습니다.",
                "vi": "Hàng tháng tôi đóng 1.2% lương làm phí công đoàn.",
                "situation": "informal"
            },
            {
                "ko": "체크오프 제도로 조합비가 자동 공제됩니다.",
                "vi": "Phí công đoàn được khấu trừ tự động qua chế độ check-off.",
                "situation": "onsite"
            },
            {
                "ko": "조합비 납부는 조합원의 의무이므로 반드시 납부해야 합니다.",
                "vi": "Nộp phí công đoàn là nghĩa vụ của hội viên nên phải đóng.",
                "situation": "formal"
            }
        ],
        "relatedTerms": ["체크오프", "노동조합", "조합원", "단체협약"]
    },
    {
        "slug": "can-bo-chuyen-trach",
        "korean": "전임자",
        "vietnamese": "Cán bộ chuyên trách",
        "hanja": "專任者",
        "hanjaReading": "專(오로지 전) 任(맡길 임) 者(놈 자)",
        "pronunciation": "전임자",
        "meaningKo": "근로 제공 의무를 면제받고 노동조합 업무에만 전념하는 조합 간부. 통역 시 전임자는 '근로 제공 면제'를 받아 회사 업무를 하지 않고 조합 활동만 하며, 급여는 원칙적으로 노동조합이 지급하지만 단체협약으로 사용자가 지급하기로 정할 수 있음을 명확히 전달. 전임자 수와 급여 지급은 '타임오프(time-off)' 제도로 규제되며, 법정 한도를 초과하면 위법임을 강조. 베트남어로는 'cán bộ chuyên trách công đoàn'(조합 전임 간부) 또는 'người được miễn làm việc để hoạt động công đoàn'(조합 활동을 위해 근로 면제받은 사람)으로 풀어 설명. 타임오프는 'thời gian miễn làm việc cho hoạt động công đoàn'으로 표현하며, 한도 초과 시 부당노동행위(경비 원조) 해당 가능성도 언급.",
        "meaningVi": "Cán bộ công đoàn được miễn nghĩa vụ cung cấp lao động và chỉ tập trung vào công việc công đoàn. Được miễn làm việc công ty, chỉ hoạt động công đoàn. Nguyên tắc công đoàn trả lương, nhưng có thể thỏa thuận để người sử dụng lao động trả qua thỏa ước tập thể. Số lượng và lương cán bộ chuyên trách được quy định bởi chế độ 'time-off' (giới hạn pháp luật), vượt quá là vi phạm. Vượt giới hạn có thể bị coi là hành vi lao động bất công (hỗ trợ kinh phí).",
        "context": "노동조합, 조합 활동, 타임오프",
        "culturalNote": "한국 노동조합법 제24조는 근로시간 면제(타임오프) 한도를 정하여, 사용자는 단체협약으로 정한 범위 내에서 조합 전임자에게 급여를 지급할 수 있으나 법정 한도를 초과하면 부당노동행위(경비 원조)가 됨. 타임오프 한도는 조합원 수에 따라 산정되며(예: 100~299인 사업장은 연간 2,000시간), 초과 시 임금 지급 불가. 전임자는 회사 업무를 하지 않으므로 인사고과·승진에서 불이익을 받을 수 있으나, 전임 기간도 근속으로 인정됨. 베트남은 공회 간부가 일정 시간 공회 활동을 할 수 있으나 전임 개념은 약하며, 급여는 회사가 계속 지급함. 통역 시 한국의 '전임'은 '완전 면제'(hoàn toàn miễn làm việc)를 의미하고, 베트남의 '겸임'(겸직, kiêm nhiệm)과 구분하여 설명해야 함.",
        "commonMistakes": [
            {
                "mistake": "전임자를 'người làm việc toàn thời gian'로 번역",
                "correction": "'cán bộ chuyên trách công đoàn' 또는 'người miễn làm việc'",
                "explanation": "'toàn thời gian'은 풀타임 근로자, 전임자는 근로 면제"
            },
            {
                "mistake": "전임자는 회사가 무조건 급여 지급한다고 설명",
                "correction": "원칙은 노조 지급, 단체협약으로 회사 지급 가능",
                "explanation": "타임오프 한도 내에서만 회사 지급 가능"
            },
            {
                "mistake": "타임오프 한도를 '제한 없음'으로 안내",
                "correction": "조합원 수 기준 법정 한도 존재",
                "explanation": "한도 초과 시 위법"
            },
            {
                "mistake": "전임 기간은 근속에 포함 안 된다고 설명",
                "correction": "근속 기간 인정",
                "explanation": "근로 관계는 유지됨"
            }
        ],
        "examples": [
            {
                "ko": "김 대리는 노동조합 전임자로 근로 제공이 면제되었습니다.",
                "vi": "Anh Kim là cán bộ chuyên trách công đoàn, được miễn cung cấp lao động.",
                "situation": "formal"
            },
            {
                "ko": "타임오프 한도를 초과하여 전임자 급여를 지급하면 부당노동행위입니다.",
                "vi": "Nếu trả lương cán bộ chuyên trách vượt giới hạn time-off thì là hành vi lao động bất công.",
                "situation": "onsite"
            },
            {
                "ko": "전임자는 조합 업무만 전담하고 회사 업무는 하지 않습니다.",
                "vi": "Cán bộ chuyên trách chỉ lo công việc công đoàn, không làm công việc công ty.",
                "situation": "informal"
            }
        ],
        "relatedTerms": ["타임오프", "근로시간 면제", "부당노동행위", "조합 간부"]
    }
]

def main():
    # 기존 파일 읽기
    with open(terms_file, 'r', encoding='utf-8') as f:
        data = json.load(f)

    print(f"📖 기존 용어 수: {len(data)}개")

    # 중복 체크
    existing_slugs = {term['slug'] for term in data}
    new_slugs = {term['slug'] for term in new_terms}
    duplicates = existing_slugs & new_slugs

    if duplicates:
        print(f"⚠️  중복된 slug 발견: {duplicates}")
        print("중복된 용어는 추가하지 않습니다.")
        new_terms_filtered = [term for term in new_terms if term['slug'] not in duplicates]
    else:
        new_terms_filtered = new_terms

    # 새 용어 추가
    data.extend(new_terms_filtered)

    print(f"➕ 추가할 용어 수: {len(new_terms_filtered)}개")
    print(f"📊 최종 용어 수: {len(data)}개")

    # 파일 저장
    with open(terms_file, 'w', encoding='utf-8') as f:
        json.dump(data, f, ensure_ascii=False, indent=2)

    print(f"✅ 저장 완료: {terms_file}")

    # 추가된 용어 목록 출력
    print("\n📋 추가된 용어:")
    for term in new_terms_filtered:
        print(f"  - {term['korean']} ({term['slug']})")

if __name__ == "__main__":
    main()
