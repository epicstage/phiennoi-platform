#!/usr/bin/env python3
"""
Add 10 social security/welfare law terms (version 11-i) to legal.json
Theme: 사회보장법/복지법 (Social Security Law/Welfare Law)
"""

import json
import sys
from pathlib import Path

# Navigate to project root
project_root = Path(__file__).parent.parent.parent
legal_json_path = project_root / "src" / "data" / "terms" / "legal.json"

# 10 new terms - Social Security Law/Welfare Law theme
new_terms = [
    {
        "slug": "che-do-bao-hiem-xa-hoi",
        "korean": "사회보험제도",
        "vietnamese": "Chế độ bảo hiểm xã hội",
        "hanja": "社會保險制度",
        "hanjaReading": "社(모일 사) 會(모일 회) 保(지킬 보) 險(험할 험) 制(제도 제) 度(법도 도)",
        "pronunciation": "사회보험제도",
        "meaningKo": "국민의 생활 안정과 복지 향상을 위해 질병·노령·실업·산재 등 사회적 위험으로부터 보호하는 국가의 의무적 보험제도. 통역 시 한국의 4대 보험(국민연금, 건강보험, 고용보험, 산재보험)과 베트남의 BHXH(사회보험), BHYT(건강보험), BHTN(실업보험) 체계가 다르므로 각국의 보험 종류와 가입 대상, 보험료율을 명확히 구분하여 설명해야 함. 한국은 국민연금과 건강보험이 분리되어 있으나 베트남은 통합 운영되는 경우가 많아 혼동 주의.",
        "meaningVi": "Chế độ bảo hiểm do nhà nước tổ chức, bắt buộc người lao động và người sử dụng lao động tham gia nhằm bảo vệ người lao động trước các rủi ro xã hội như ốm đau, già yếu, thất nghiệp, tai nạn lao động. Bao gồm BHXH (bảo hiểm xã hội), BHYT (bảo hiểm y tế), BHTN (bảo hiểm thất nghiệp) tại Việt Nam, tương ứng với 4대 보험 (bốn loại bảo hiểm bắt buộc) tại Hàn Quốc.",
        "context": "노동법·사회복지 분야 계약서, 근로자 채용 관련 법률 자문, 인사담당자 교육",
        "culturalNote": "한국의 4대 보험은 국민연금, 건강보험, 고용보험, 산재보험으로 각각 별도 법률에 근거하며 관리기관도 다름(국민연금공단, 건강보험공단, 근로복지공단). 베트남은 BHXH(사회보험청)가 연금·건강·실업보험을 통합 관리하며 보험료율과 급여 기준이 한국과 상이함. 통역 시 양국 제도의 가입 범위, 보험료 부담률, 급여 종류를 혼동하지 않도록 사전에 정확히 파악 필요.",
        "commonMistakes": [
            {
                "mistake": "'사회보험'을 단순히 'Bảo hiểm xã hội'로만 번역",
                "correction": "'Chế độ bảo hiểm xã hội'로 '제도' 개념 포함",
                "explanation": "단순 번역 시 제도적 틀을 놓칠 수 있음"
            },
            {
                "mistake": "한국 4대 보험을 베트남 3종 보험(BHXH, BHYT, BHTN)과 1:1 대응 설명",
                "correction": "각국 보험 체계의 차이를 명시하고 구체적 내용 설명",
                "explanation": "보험 종류와 관리기관이 다르므로 혼동 방지 필요"
            },
            {
                "mistake": "'국민연금'을 'BHXH'로 직역",
                "correction": "'Chế độ hưu trí quốc gia'(국가연금제도) 또는 'Bảo hiểm hưu trí'(연금보험)로 구분",
                "explanation": "베트남 BHXH는 연금·건강·실업을 포괄하는 개념"
            }
        ],
        "examples": [
            {
                "ko": "모든 근로자는 사회보험제도에 의무적으로 가입해야 합니다.",
                "vi": "Tất cả người lao động phải tham gia bắt buộc chế độ bảo hiểm xã hội.",
                "situation": "formal"
            },
            {
                "ko": "귀사는 4대 보험 가입 의무를 이행하고 계십니까?",
                "vi": "Quý công ty có thực hiện nghĩa vụ tham gia bốn loại bảo hiểm bắt buộc không?",
                "situation": "formal"
            },
            {
                "ko": "사회보험제도는 국민의 생활 안정을 위한 최소한의 안전망입니다.",
                "vi": "Chế độ bảo hiểm xã hội là mạng lưới an sinh tối thiểu cho sự ổn định cuộc sống của người dân.",
                "situation": "formal"
            }
        ],
        "relatedTerms": ["국민연금", "건강보험", "고용보험", "산재보험", "사회보장"]
    },
    {
        "slug": "tro-cap-that-nghiep",
        "korean": "실업급여",
        "vietnamese": "Trợ cấp thất nghiệp",
        "hanja": "失業給與",
        "hanjaReading": "失(잃을 실) 業(업 업) 給(줄 급) 與(줄 여)",
        "pronunciation": "시럽급여",
        "meaningKo": "고용보험에 가입한 근로자가 비자발적 사유로 실직한 경우 일정 기간 동안 지급받는 생활 안정 지원금. 통역 시 한국의 실업급여는 구직급여·취업촉진수당·연장급여 등으로 세분화되며, 베트남의 'Trợ cấp thất nghiệp'는 최대 3개월 지급되는 등 지급 기간과 조건이 상이함을 명확히 구분해야 함. 수급 요건(가입 기간, 비자발적 이직 증명 등)도 양국이 다르므로 혼동 주의.",
        "meaningVi": "Khoản tiền hỗ trợ do quỹ bảo hiểm thất nghiệp chi trả cho người lao động đã tham gia BHTN trong thời gian quy định, bị mất việc làm không do lỗi của mình. Tại Việt Nam, thời gian hưởng tối đa là 3 tháng (có thể 12 tháng tùy thời gian đóng), mức hưởng 60% mức lương bình quân tháng đóng BHTN của 6 tháng liền kề trước khi thất nghiệp.",
        "context": "고용보험 신청, 노동 분쟁, 이직 상담, HR 업무",
        "culturalNote": "한국은 실업급여 지급 기간이 최소 120일에서 최대 270일(50세 이상·장애인은 최대 330일)로 길고, 구직활동 의무가 엄격함. 베트남은 기본 3개월(가입 기간에 따라 최대 12개월)이며 구직활동 증명 요건이 상대적으로 느슨함. 통역 시 양국의 지급 기간, 수급액 산정 방식, 재취업 지원 프로그램의 차이를 정확히 전달해야 함.",
        "commonMistakes": [
            {
                "mistake": "'실업급여'를 'Tiền trợ cấp thất nghiệp'로 번역",
                "correction": "'Trợ cấp thất nghiệp'(실업 수당) 또는 'Trợ cấp mất việc làm'",
                "explanation": "'Tiền'(돈)을 붙이면 구어적이고 격식이 떨어짐"
            },
            {
                "mistake": "한국 실업급여 지급 기간을 베트남과 동일하게 3개월로 설명",
                "correction": "한국은 최소 120일(약 4개월)~최대 270일 등 상세히 설명",
                "explanation": "지급 기간이 크게 다르므로 혼동 방지 필요"
            },
            {
                "mistake": "'구직급여'와 '실업급여'를 구분 없이 번역",
                "correction": "'구직급여'는 'Trợ cấp tìm kiếm việc làm'로 세분화",
                "explanation": "한국은 실업급여 내 구직급여·취업촉진수당 등으로 구분됨"
            }
        ],
        "examples": [
            {
                "ko": "실업급여 신청을 위해 고용센터에 방문하셔야 합니다.",
                "vi": "Để đăng ký trợ cấp thất nghiệp, anh/chị phải đến Trung tâm dịch vụ việc làm.",
                "situation": "formal"
            },
            {
                "ko": "실업급여 수급 기간은 가입 기간과 연령에 따라 다릅니다.",
                "vi": "Thời gian hưởng trợ cấp thất nghiệp tùy thuộc vào thời gian tham gia bảo hiểm và độ tuổi.",
                "situation": "formal"
            },
            {
                "ko": "비자발적 퇴사가 아니면 실업급여를 받을 수 없습니다.",
                "vi": "Nếu không phải nghỉ việc không tự nguyện thì không thể nhận trợ cấp thất nghiệp.",
                "situation": "onsite"
            }
        ],
        "relatedTerms": ["고용보험", "구직급여", "이직확인서", "재취업수당", "실업인정"]
    },
    {
        "slug": "che-do-trieu-huu",
        "korean": "정년퇴직제도",
        "vietnamese": "Chế độ nghỉ hưu theo tuổi",
        "hanja": "定年退職制度",
        "hanjaReading": "定(정할 정) 年(해 년) 退(물러날 퇴) 職(직분 직) 制(제도 제) 度(법도 도)",
        "pronunciation": "정년퇴직제도",
        "meaningKo": "일정 연령에 도달한 근로자가 의무적으로 퇴직하는 제도로, 한국은 만 60세 이상으로 법정 정년이 정해져 있음. 통역 시 베트남의 법정 퇴직연령(남성 60세, 여성 55세)과 한국의 정년(만 60세 이상) 차이를 명확히 하고, 한국에서는 정년 연장 논의가 활발하며 정년 이후 재고용 제도도 보편화되고 있음을 설명해야 함. '정년퇴직'과 '명예퇴직'을 혼동하지 않도록 주의.",
        "meaningVi": "Chế độ bắt buộc người lao động nghỉ việc khi đạt độ tuổi quy định. Tại Việt Nam, tuổi nghỉ hưu hiện nay là 60 tuổi đối với nam và 55 tuổi đối với nữ (đang dần nâng lên 60 tuổi cho nữ theo lộ trình). Tại Hàn Quốc, tuổi nghỉ hưu tối thiểu là 60 tuổi (만 60세), và nhiều doanh nghiệp có chính sách tái tuyển dụng sau nghỉ hưu.",
        "context": "인사관리, 노무 상담, 퇴직연금 설계, 근로계약",
        "culturalNote": "한국은 2013년 「고령자고용법」 개정으로 만 60세 정년이 의무화되었으며, 2016년부터 300인 이상 사업장에 단계적 적용됨. 베트남은 남녀 정년이 다르고(남 60세, 여 55세) 여성 정년을 점진적으로 상향 중. 한국은 정년 이후 재고용·임금피크제가 일반화되어 있으나 베트남은 정년 퇴직 후 연금 수급이 주 생계수단. 통역 시 정년 연령, 퇴직금, 연금 수급 시점의 차이를 정확히 전달해야 함.",
        "commonMistakes": [
            {
                "mistake": "'정년퇴직'을 단순히 'Nghỉ hưu'로만 번역",
                "correction": "'Nghỉ hưu theo tuổi'(법정 정년) 또는 'Chế độ nghỉ hưu theo quy định'",
                "explanation": "자발적 은퇴와 법정 정년을 구분해야 함"
            },
            {
                "mistake": "한국 정년을 60세로 단정",
                "correction": "'만 60세 이상'(tối thiểu 60 tuổi)으로 명시",
                "explanation": "법정 최저 정년은 60세이나 기업마다 다를 수 있음"
            },
            {
                "mistake": "'정년퇴직'과 '명예퇴직'을 동일하게 번역",
                "correction": "'명예퇴직'은 'Nghỉ việc tự nguyện sớm'(조기 자발적 퇴직)",
                "explanation": "정년퇴직은 의무, 명예퇴직은 자발적 조기퇴직"
            }
        ],
        "examples": [
            {
                "ko": "우리 회사는 정년퇴직제도를 만 60세로 운영하고 있습니다.",
                "vi": "Công ty chúng tôi áp dụng chế độ nghỉ hưu theo tuổi tại 60 tuổi.",
                "situation": "formal"
            },
            {
                "ko": "정년퇴직 후 재고용 여부는 개인 역량에 따라 결정됩니다.",
                "vi": "Việc tái tuyển dụng sau nghỉ hưu sẽ được quyết định dựa trên năng lực cá nhân.",
                "situation": "formal"
            },
            {
                "ko": "정년이 다가오면 퇴직연금 수령 계획을 세우세요.",
                "vi": "Khi sắp đến tuổi nghỉ hưu, hãy lập kế hoạch nhận lương hưu.",
                "situation": "onsite"
            }
        ],
        "relatedTerms": ["퇴직연금", "명예퇴직", "고령자고용법", "임금피크제", "국민연금"]
    },
    {
        "slug": "tro-cap-duong-suc",
        "korean": "요양급여",
        "vietnamese": "Trợ cấp dưỡng sức",
        "hanja": "療養給與",
        "hanjaReading": "療(병 고칠 료) 養(기를 양) 給(줄 급) 與(줄 여)",
        "pronunciation": "요양급여",
        "meaningKo": "건강보험 가입자가 질병이나 부상으로 치료가 필요할 때 받는 의료서비스 및 비용 지원. 통역 시 한국의 요양급여는 건강보험공단이 의료기관에 직접 지급하는 현물급여 중심이며, 베트남의 'Trợ cấp dưỡng sức'는 현금 지급도 포함될 수 있음을 구분해야 함. 요양급여 범위(진찰·검사·투약·수술·입원 등)와 본인부담금 비율도 양국이 다르므로 혼동 주의.",
        "meaningVi": "Chế độ hỗ trợ chi phí điều trị y tế cho người tham gia bảo hiểm y tế khi mắc bệnh hoặc bị thương. Tại Việt Nam, BHYT (bảo hiểm y tế) chi trả trực tiếp cho cơ sở y tế hoặc hoàn trả cho người bệnh. Tại Hàn Quốc, 요양급여 được quỹ bảo hiểm sức khỏe (건강보험공단) chi trả trực tiếp cho bệnh viện, người bệnh chỉ trả phần đồng chi trả (본인부담금).",
        "context": "건강보험 청구, 의료기관 진료, 보험 상담, 의료비 정산",
        "culturalNote": "한국은 건강보험 보장률이 약 65%로 본인부담금(20~60%)이 존재하며 비급여 항목도 많음. 베트남은 BHYT 가입 시 1차 의료기관(trạm y tế, phòng khám)에서 80~100% 보장, 상급 병원은 보장률이 낮아짐. 한국은 요양급여가 현물급여(의료서비스) 중심, 베트남은 현금 환급도 가능. 통역 시 본인부담금·비급여 항목·직접 청구 방식 등의 차이를 명확히 전달해야 함.",
        "commonMistakes": [
            {
                "mistake": "'요양급여'를 'Tiền điều trị'(치료비)로 번역",
                "correction": "'Trợ cấp dưỡng sức' 또는 'Chế độ khám chữa bệnh'(진료 제도)",
                "explanation": "급여는 단순 비용이 아니라 제도적 지원"
            },
            {
                "mistake": "본인부담금을 설명 없이 생략",
                "correction": "'본인부담금'은 'Đồng chi trả'로 반드시 명시",
                "explanation": "요양급여는 전액 지원이 아니므로 본인부담 존재"
            },
            {
                "mistake": "'요양급여'와 '요양병원'을 혼동",
                "correction": "'요양병원'은 'Bệnh viện điều d양'(장기 요양 병원)",
                "explanation": "요양급여는 급여 종류, 요양병원은 시설"
            }
        ],
        "examples": [
            {
                "ko": "요양급여 범위에는 진찰, 검사, 투약, 수술 등이 포함됩니다.",
                "vi": "Phạm vi trợ cấp dưỡng sức bao gồm khám, xét nghiệm, cấp thuốc, phẫu thuật, v.v.",
                "situation": "formal"
            },
            {
                "ko": "본인부담금을 제외한 나머지는 건강보험에서 요양급여로 지급됩니다.",
                "vi": "Sau khi trừ đồng chi trả, phần còn lại được bảo hiểm y tế chi trả dưới hình thức trợ cấp dưỡng sức.",
                "situation": "formal"
            },
            {
                "ko": "비급여 항목은 요양급여 대상이 아닙니다.",
                "vi": "Các hạng mục không thuộc bảo hiểm (비급여) không được hưởng trợ cấp dưỡng sức.",
                "situation": "onsite"
            }
        ],
        "relatedTerms": ["건강보험", "본인부담금", "비급여", "요양병원", "의료급여"]
    },
    {
        "slug": "che-do-bao-hiem-tai-nan-lao-dong",
        "korean": "산재보험",
        "vietnamese": "Chế độ bảo hiểm tai nạn lao động",
        "hanja": "産災保險",
        "hanjaReading": "産(낳을 산) 災(재앙 재) 保(지킬 보) 險(험할 험)",
        "pronunciation": "산재보험",
        "meaningKo": "업무상 재해(사고·질병)로 인한 근로자의 부상·질병·장해·사망 시 보상을 제공하는 사회보험제도. 통역 시 한국의 산재보험은 근로복지공단이 관리하며 업무상 재해 인정 요건과 보상 내역(요양급여, 휴업급여, 장해급여, 유족급여 등)을 명확히 설명해야 함. 베트남의 'Bảo hiểm tai nạn lao động'와 보상 범위·절차가 다르므로 혼동 주의.",
        "meaningVi": "Chế độ bảo hiểm bắt buộc do người sử dụng lao động đóng 100%, bồi thường cho người lao động bị tai nạn lao động hoặc mắc bệnh nghề nghiệp trong quá trình làm việc. Tại Việt Nam, BHTNLĐ-BNN (bảo hiểm tai nạn lao động, bệnh nghề nghiệp) được quản lý bởi BHXH Việt Nam, bao gồm chi phí điều trị, trợ cấp tạm ngừng việc, trợ cấp thương tật, tử tuất.",
        "context": "산업재해 신청, 근로계약, 안전보건 교육, 보상 청구",
        "culturalNote": "한국은 산재보험료를 사업주가 전액 부담하며, 업무상 재해 인정 요건이 명확함(출퇴근 재해도 2018년부터 포함). 베트남도 사용자 전액 부담이나 보상 수준과 절차가 다름. 한국은 근로복지공단이 보상을 결정하고, 베트남은 BHXH(사회보험청)가 관리. 통역 시 '업무상 재해' 인정 범위(출퇴근 재해, 과로사 등)와 보상 종류(요양급여, 휴업급여, 장해급여, 유족급여)를 정확히 전달해야 함.",
        "commonMistakes": [
            {
                "mistake": "'산재보험'을 'Bảo hiểm tai nạn'으로만 번역",
                "correction": "'Bảo hiểm tai nạn lao động'(산업재해 보험)으로 명시",
                "explanation": "일반 사고 보험과 구분 필요"
            },
            {
                "mistake": "산재 인정을 '사고 발생'과 동일시",
                "correction": "'업무상 재해 인정'은 'Công nhận tai nạn lao động'으로 구분",
                "explanation": "사고 발생과 산재 인정은 별개 절차"
            },
            {
                "mistake": "산재보험료를 근로자도 부담한다고 설명",
                "correction": "사업주 전액 부담(Người sử dụng lao động chịu 100%)",
                "explanation": "산재보험은 사용자 단독 부담"
            }
        ],
        "examples": [
            {
                "ko": "업무 중 다친 경우 산재보험 신청이 가능합니다.",
                "vi": "Nếu bị thương trong quá trình làm việc, có thể đăng ký bảo hiểm tai nạn lao động.",
                "situation": "onsite"
            },
            {
                "ko": "산재보험료는 사업주가 전액 부담합니다.",
                "vi": "Phí bảo hiểm tai nạn lao động do người sử dụng lao động chịu toàn bộ.",
                "situation": "formal"
            },
            {
                "ko": "출퇴근 중 사고도 산재로 인정받을 수 있습니다.",
                "vi": "Tai nạn xảy ra trong quá trình đi làm, về nhà cũng có thể được công nhận là tai nạn lao động.",
                "situation": "formal"
            }
        ],
        "relatedTerms": ["업무상재해", "근로복지공단", "휴업급여", "장해급여", "유족급여"]
    },
    {
        "slug": "che-do-phuc-loi-xa-hoi",
        "korean": "사회복지제도",
        "vietnamese": "Chế độ phúc lợi xã hội",
        "hanja": "社會福祉制度",
        "hanjaReading": "社(모일 사) 會(모일 회) 福(복 복) 祉(복 지) 制(제도 제) 度(법도 도)",
        "pronunciation": "사회복지제도",
        "meaningKo": "국민의 기본적 생활을 보장하고 삶의 질을 향상시키기 위한 국가·지방자치단체·민간의 제도적·조직적 활동. 통역 시 한국의 사회복지는 공공부조(국민기초생활보장, 의료급여 등), 사회보험(4대 보험), 사회서비스(노인·장애인·아동 돌봄) 등으로 세분화되며, 베트남의 'Phúc lợi xã hội'는 정책 대상과 범위가 다름을 명확히 해야 함. 특히 한국의 복지 수급 요건과 베트남의 정책 대상 차이 주의.",
        "meaningVi": "Hệ thống chính sách và hoạt động do nhà nước, chính quyền địa phương, tổ chức dân sự thực hiện nhằm bảo đảm đời sống cơ bản và nâng cao chất lượng cuộc sống cho người dân. Bao gồm trợ giúp xã hội (công tác xã hội), bảo trợ xã hội (trợ cấp cho người nghèo, người già, trẻ em...), dịch vụ xã hội (chăm sóc người cao tuổi, người khuyết tật...).",
        "context": "사회복지정책 논의, 복지사업 설명, NGO 활동, 정부 지원금 신청",
        "culturalNote": "한국은 1990년대 이후 사회복지제도가 급속히 확대되어 공공부조(국민기초생활보장제도), 사회보험(4대 보험), 사회서비스(노인장기요양보험, 장애인활동지원 등)로 체계화됨. 베트남은 정부 주도의 복지정책이 상대적으로 제한적이며 가족·공동체 중심의 전통적 부양 문화가 강함. 통역 시 복지 수급 대상, 급여 수준, 전달 체계의 차이를 정확히 전달해야 함.",
        "commonMistakes": [
            {
                "mistake": "'사회복지'를 'Phúc lợi'로만 번역",
                "correction": "'Phúc lợi xã hội'(사회복지) 또는 'Chế độ phúc lợi xã hội'(제도)",
                "explanation": "'Phúc lợi' 단독 사용 시 기업 복리후생과 혼동 가능"
            },
            {
                "mistake": "공공부조와 사회보험을 구분 없이 번역",
                "correction": "'공공부조'는 'Trợ giúp xã hội công cộng', '사회보험'은 'Bảo hiểm xã hội'",
                "explanation": "공공부조는 무상 지원, 사회보험은 보험료 기반"
            },
            {
                "mistake": "'복지 수급자'를 단순히 'Người nhận phúc lợi'로 번역",
                "correction": "'Người thụ hưởng chế độ phúc lợi xã hội'(복지 수혜자)",
                "explanation": "격식과 정확성 제고"
            }
        ],
        "examples": [
            {
                "ko": "사회복지제도는 취약계층의 생활 안정을 위한 핵심 정책입니다.",
                "vi": "Chế độ phúc lợi xã hội là chính sách then chốt để đảm bảo cuộc sống ổn định cho tầng lớp yếu thế.",
                "situation": "formal"
            },
            {
                "ko": "정부는 사회복지 예산을 확대하고 있습니다.",
                "vi": "Chính phủ đang mở rộng ngân sách cho phúc lợi xã hội.",
                "situation": "formal"
            },
            {
                "ko": "노인·장애인·아동은 사회복지서비스의 주요 대상입니다.",
                "vi": "Người cao tuổi, người khuyết tật, trẻ em là đối tượng chính của dịch vụ phúc lợi xã hội.",
                "situation": "formal"
            }
        ],
        "relatedTerms": ["공공부조", "사회보험", "국민기초생활보장", "노인장기요양보험", "사회서비스"]
    },
    {
        "slug": "tro-cap-nuoi-con",
        "korean": "육아휴직급여",
        "vietnamese": "Trợ cấp nghỉ nuôi con",
        "hanja": "育兒休職給與",
        "hanjaReading": "育(기를 육) 兒(아이 아) 休(쉴 휴) 職(직분 직) 給(줄 급) 與(줄 여)",
        "pronunciation": "유가휴직급여",
        "meaningKo": "만 8세 이하 또는 초등학교 2학년 이하 자녀를 양육하기 위해 휴직한 근로자에게 고용보험에서 지급하는 소득 대체 급여. 통역 시 한국의 육아휴직급여는 최대 1년간 지급되며 상한액·하한액이 정해져 있고(2025년 기준 월 최대 150만 원, 최초 3개월은 통상임금의 80%), 베트남의 'Chế độ thai sản'(출산 휴가 급여)과 지급 기간·대상이 다름을 명확히 해야 함. 아버지의 육아휴직 사용 시 보너스(3+3 부모 육아휴직제)도 설명 필요.",
        "meaningVi": "Khoản trợ cấp do quỹ bảo hiểm thất nghiệp chi trả cho người lao động nghỉ việc để chăm sóc con dưới 8 tuổi hoặc học lớp 2 trở xuống. Tại Hàn Quốc, thời gian tối đa là 1 năm, mức trợ cấp lên đến 80% lương (3 tháng đầu, tối đa 150 vạn won/tháng, năm 2025). Tại Việt Nam, chế độ nghỉ thai sản (nghỉ sinh) là 6 tháng với 100% lương, khác với 육아휴직 (nghỉ nuôi con).",
        "context": "육아휴직 신청, 인사·노무 상담, 고용보험 급여, 일·가정 양립 정책",
        "culturalNote": "한국은 육아휴직급여가 고용보험에서 지급되며 남녀 모두 사용 가능하고, 부모가 동시 또는 순차적으로 사용 시 인센티브 지급(3+3 부모 육아휴직제: 3개월씩 사용 시 급여 상향). 베트남은 'nghỉ thai sản'(출산휴가)이 6개월이며 사회보험에서 100% 급여 지급, 한국의 '육아휴직'과는 개념이 다름. 통역 시 출산휴가(산전후휴가)와 육아휴직의 차이, 남성 육아휴직 장려 정책 등을 정확히 전달해야 함.",
        "commonMistakes": [
            {
                "mistake": "'육아휴직'을 'Nghỉ thai sản'(출산휴가)으로 번역",
                "correction": "'Nghỉ nuôi con'(육아 휴직) 또는 'Nghỉ chăm sóc con nhỏ'",
                "explanation": "출산휴가는 산전후휴가(출산 전후), 육아휴직은 양육 목적"
            },
            {
                "mistake": "급여를 '임금'이라고 번역",
                "correction": "'급여'는 'Trợ cấp'(수당), '임금'은 'Lương'",
                "explanation": "육아휴직급여는 회사가 아닌 고용보험에서 지급"
            },
            {
                "mistake": "3+3 부모 육아휴직제를 설명 없이 생략",
                "correction": "'Chế độ nghỉ nuôi con 3+3 cho cha mẹ'로 구체적 설명",
                "explanation": "인센티브 제도는 한국 특유의 정책"
            }
        ],
        "examples": [
            {
                "ko": "육아휴직급여는 고용보험에서 최대 1년간 지급됩니다.",
                "vi": "Trợ cấp nghỉ nuôi con được chi trả từ quỹ bảo hiểm thất nghiệp tối đa 1 năm.",
                "situation": "formal"
            },
            {
                "ko": "부모가 함께 육아휴직을 사용하면 급여가 더 늘어납니다.",
                "vi": "Nếu cả cha và mẹ cùng nghỉ nuôi con, mức trợ cấp sẽ tăng thêm.",
                "situation": "formal"
            },
            {
                "ko": "육아휴직은 만 8세 이하 자녀가 있으면 신청할 수 있어요.",
                "vi": "Có thể đăng ký nghỉ nuôi con nếu có con dưới 8 tuổi.",
                "situation": "onsite"
            }
        ],
        "relatedTerms": ["출산휴가", "배우자출산휴가", "육아기근로시간단축", "고용보험", "일·가정양립"]
    },
    {
        "slug": "tro-cap-nguoi-cao-tuoi",
        "korean": "기초연금",
        "vietnamese": "Trợ cấp người cao tuổi",
        "hanja": "基礎年金",
        "hanjaReading": "基(터 기) 礎(주춧돌 초) 年(해 년) 金(쇠 금)",
        "pronunciation": "기초연금",
        "meaningKo": "만 65세 이상 소득 하위 70% 노인에게 지급되는 국가 복지급여로, 국민연금과는 별도로 지급되는 공공부조 성격의 연금. 통역 시 기초연금은 국민연금(사회보험)과 달리 보험료 납부 없이 소득·재산 기준으로 지급되며, 베트남의 'Trợ cấp người cao tuổi'(고령자 수당)는 80세 이상 대상으로 지급 조건과 금액이 다름을 명확히 해야 함. 기초연금과 국민연금의 차이를 혼동하지 않도록 주의.",
        "meaningVi": "Khoản trợ cấp do nhà nước chi trả cho người cao tuổi từ 65 tuổi trở lên thuộc 70% hộ gia đình có thu nhập thấp. Đây là chế độ phúc lợi xã hội (không cần đóng bảo hiểm), khác với 국민연금 (lương hưu bảo hiểm xã hội bắt buộc). Tại Việt Nam, trợ cấp tuất hàng tháng (trợ cấp người cao tuổi) dành cho người từ 80 tuổi trở lên, mức thấp hơn Hàn Quốc.",
        "context": "노인복지 상담, 기초연금 신청, 사회복지정책 설명",
        "culturalNote": "한국의 기초연금은 2014년 도입되어 만 65세 이상 소득 하위 70%에게 지급되며, 국민연금과 별개의 제도임(2025년 기준 월 최대 약 33만 원). 베트남은 80세 이상 노인에게 월 27만 동(약 1.4만 원) 수준의 'trợ cấp tuất hàng tháng'(월 수당)을 지급. 한국은 연령·소득 기준이 낮고 금액도 높아 노인 빈곤 완화 효과가 큼. 통역 시 기초연금과 국민연금의 차이, 지급 대상과 금액 차이를 정확히 전달해야 함.",
        "commonMistakes": [
            {
                "mistake": "'기초연금'을 'Lương hưu cơ bản'으로 번역",
                "correction": "'Trợ cấp người cao tuổi'(고령자 수당) 또는 'Phụ cấp lương hưu cơ bản'",
                "explanation": "'Lương hưu'는 연금(보험), '기초연금'은 복지 수당"
            },
            {
                "mistake": "국민연금과 기초연금을 혼동하여 설명",
                "correction": "국민연금(Bảo hiểm hưu trí)과 기초연금(Trợ cấp người cao tuổi) 명확히 구분",
                "explanation": "국민연금은 사회보험, 기초연금은 공공부조"
            },
            {
                "mistake": "지급 조건을 '만 65세 이상 전원'으로 설명",
                "correction": "'소득 하위 70%'(70% hộ gia đình có thu nhập thấp) 조건 명시",
                "explanation": "기초연금은 선별적 복지"
            }
        ],
        "examples": [
            {
                "ko": "기초연금은 소득 하위 70% 노인에게 지급됩니다.",
                "vi": "Trợ cấp người cao tuổi được chi trả cho 70% người già có thu nhập thấp.",
                "situation": "formal"
            },
            {
                "ko": "국민연금과 기초연금은 별도로 받을 수 있어요.",
                "vi": "Có thể nhận cả lương hưu bảo hiểm (국민연금) và trợ cấp người cao tuổi (기초연금).",
                "situation": "onsite"
            },
            {
                "ko": "만 65세가 되면 기초연금 신청이 가능합니다.",
                "vi": "Khi đủ 65 tuổi, có thể đăng ký trợ cấp người cao tuổi.",
                "situation": "formal"
            }
        ],
        "relatedTerms": ["국민연금", "노인복지", "소득인정액", "공공부조", "노령연금"]
    },
    {
        "slug": "che-do-bao-tro-xa-hoi",
        "korean": "국민기초생활보장제도",
        "vietnamese": "Chế độ bảo trợ xã hội tối thiểu",
        "hanja": "國民基礎生活保障制度",
        "hanjaReading": "國(나라 국) 民(백성 민) 基(터 기) 礎(주춧돌 초) 生(날 생) 活(살 활) 保(지킬 보) 障(막을 장) 制(제도 제) 度(법도 도)",
        "pronunciation": "국민기초생활보장제도",
        "meaningKo": "생활이 어려운 국민에게 최저생활을 보장하고 자활을 돕기 위해 생계·의료·주거·교육급여 등을 지원하는 공공부조제도. 통역 시 한국의 기초생활보장제도는 소득인정액이 기준 중위소득의 일정 비율 이하인 가구가 수급 대상이며, 베트남의 'Chính sách trợ giúp xã hội'(사회부조 정책)와 수급 기준·급여 종류가 다름을 명확히 해야 함. 생계급여·의료급여·주거급여·교육급여를 구분하여 설명 필요.",
        "meaningVi": "Chế độ hỗ trợ do nhà nước cung cấp cho các hộ gia đình có thu nhập thấp dưới mức chuẩn nghèo, bao gồm trợ cấp sinh hoạt, y tế, nhà ở, giáo dục nhằm đảm bảo mức sống tối thiểu và hỗ trợ tự lập. Tại Hàn Quốc, đối tượng nhận hỗ trợ được xác định theo 소득인정액 (thu nhập được công nhận) so với 기준 중위소득 (thu nhập trung vị chuẩn).",
        "context": "복지 상담, 수급 신청, 사회복지정책 논의, 빈곤층 지원",
        "culturalNote": "한국의 국민기초생활보장제도는 2000년 도입되어 생계급여(중위소득 32% 이하), 의료급여(40% 이하), 주거급여(48% 이하), 교육급여(50% 이하) 등 맞춤형 급여로 세분화됨. 베트남은 'hộ nghèo'(빈곤 가구) 기준으로 정부 지원이 제공되나 한국만큼 체계적이지 않음. 통역 시 소득인정액 산정 방식, 급여 종류별 수급 조건, 자활 프로그램 등을 정확히 전달해야 함.",
        "commonMistakes": [
            {
                "mistake": "'기초생활보장'을 단순히 'Bảo trợ xã hội'로만 번역",
                "correction": "'Chế độ bảo trợ xã hội tối thiểu' 또는 'Bảo đảm đời sống cơ bản quốc dân'",
                "explanation": "'제도'와 '국민' 개념 포함 필요"
            },
            {
                "mistake": "생계급여·의료급여 등을 구분 없이 설명",
                "correction": "각 급여를 명확히 구분(Trợ cấp sinh hoạt, Y tế, Nhà ở, Giáo dục)",
                "explanation": "급여 종류마다 수급 조건과 내용이 다름"
            },
            {
                "mistake": "'소득인정액'을 'Thu nhập'으로만 번역",
                "correction": "'Thu nhập được công nhận'(소득인정액)으로 정확히 번역",
                "explanation": "실제 소득 + 재산의 소득환산액"
            }
        ],
        "examples": [
            {
                "ko": "국민기초생활보장제도는 생계·의료·주거·교육급여로 나뉩니다.",
                "vi": "Chế độ bảo trợ xã hội tối thiểu chia thành trợ cấp sinh hoạt, y tế, nhà ở, giáo dục.",
                "situation": "formal"
            },
            {
                "ko": "소득인정액이 기준 중위소득의 32% 이하면 생계급여를 받을 수 있습니다.",
                "vi": "Nếu thu nhập được công nhận dưới 32% thu nhập trung vị chuẩn, có thể nhận trợ cấp sinh hoạt.",
                "situation": "formal"
            },
            {
                "ko": "기초생활수급자는 의료비를 거의 부담하지 않습니다.",
                "vi": "Người thụ hưởng chế độ bảo trợ xã hội tối thiểu hầu như không phải trả chi phí y tế.",
                "situation": "onsite"
            }
        ],
        "relatedTerms": ["생계급여", "의료급여", "주거급여", "교육급여", "소득인정액"]
    },
    {
        "slug": "che-do-bao-hiem-duong-lao",
        "korean": "노인장기요양보험",
        "vietnamese": "Chế độ bảo hiểm dưỡng lão dài hạn",
        "hanja": "老人長期療養保險",
        "hanjaReading": "老(늙을 로) 人(사람 인) 長(긴 장) 期(기약할 기) 療(병 고칠 료) 養(기를 양) 保(지킬 보) 險(험할 험)",
        "pronunciation": "노인장기요양보험",
        "meaningKo": "고령이나 노인성 질병으로 일상생활이 어려운 노인에게 신체활동·가사활동 지원 등을 제공하는 사회보험제도. 통역 시 한국의 장기요양보험은 65세 이상 또는 노인성 질병이 있는 64세 이하가 대상이며, 요양등급(1~5등급, 인지지원등급)에 따라 재가급여·시설급여·특별현금급여를 제공함. 베트남은 이러한 제도가 아직 체계화되지 않아 가족 돌봄 중심이므로 제도 차이를 명확히 설명해야 함.",
        "meaningVi": "Chế độ bảo hiểm xã hội cung cấp dịch vụ chăm sóc dài hạn cho người cao tuổi (từ 65 tuổi trở lên) hoặc người mắc bệnh lão khoa, gặp khó khăn trong sinh hoạt hàng ngày. Tại Hàn Quốc, chế độ này cung cấp chăm sóc tại nhà (재가급여), chăm sóc tại cơ sở (시설급여), hoặc trợ cấp đặc biệt bằng tiền mặt (특별현금급여) tùy theo cấp độ (1~5급, 인지지원등급).",
        "context": "노인복지, 장기요양 신청, 요양시설 상담, 간병인 채용",
        "culturalNote": "한국은 2008년 노인장기요양보험을 도입하여 국민건강보험공단이 운영하며, 요양등급 판정 후 재가서비스(방문요양·목욕·간호) 또는 시설입소(요양원) 서비스를 제공함. 본인부담금은 15~20%. 베트남은 아직 공식적인 장기요양보험 제도가 없고 가족이 직접 돌보는 경우가 대부분. 통역 시 요양등급 판정 절차, 급여 종류(재가·시설), 본인부담금 등을 정확히 전달해야 함.",
        "commonMistakes": [
            {
                "mistake": "'장기요양'을 단순히 'Điều dưỡng'(요양)으로만 번역",
                "correction": "'Dưỡng lão dài hạn'(장기 노인 돌봄) 또는 'Chăm sóc dài hạn'",
                "explanation": "일반 치료와 장기 돌봄을 구분해야 함"
            },
            {
                "mistake": "요양등급을 설명 없이 생략",
                "correction": "'Cấp độ chăm sóc'(1~5급, 인지지원급) 구체적 설명",
                "explanation": "등급에 따라 급여 내용이 달라짐"
            },
            {
                "mistake": "재가급여와 시설급여를 혼동",
                "correction": "재가급여(Chăm sóc tại nhà), 시설급여(Chăm sóc tại cơ sở) 명확히 구분",
                "explanation": "서비스 제공 방식이 다름"
            }
        ],
        "examples": [
            {
                "ko": "노인장기요양보험은 만 65세 이상 노인이 대상입니다.",
                "vi": "Chế độ bảo hiểm dưỡng lão dài hạn dành cho người cao tuổi từ 65 tuổi trở lên.",
                "situation": "formal"
            },
            {
                "ko": "요양등급을 받으면 재가서비스나 시설입소를 선택할 수 있습니다.",
                "vi": "Sau khi được phân loại cấp độ chăm sóc, có thể chọn dịch vụ tại nhà hoặc nhập viện dưỡng lão.",
                "situation": "formal"
            },
            {
                "ko": "장기요양 신청은 건강보험공단에 하시면 됩니다.",
                "vi": "Đăng ký chăm sóc dài hạn tại Quỹ bảo hiểm sức khỏe quốc dân.",
                "situation": "onsite"
            }
        ],
        "relatedTerms": ["요양등급", "재가급여", "시설급여", "요양보호사", "건강보험공단"]
    }
]

def main():
    print(f"📖 Reading {legal_json_path}")

    # Read existing data
    with open(legal_json_path, 'r', encoding='utf-8') as f:
        data = json.load(f)

    if not isinstance(data, list):
        print("❌ Error: JSON root must be a flat array [...], not {\"terms\": [...]}")
        sys.exit(1)

    initial_count = len(data)
    print(f"📊 Current term count: {initial_count}")

    # Check for duplicates
    existing_slugs = {term.get('slug') for term in data if 'slug' in term}
    new_slugs = {term['slug'] for term in new_terms}
    duplicates = existing_slugs & new_slugs

    if duplicates:
        print(f"⚠️  Warning: Found {len(duplicates)} duplicate slugs:")
        for slug in duplicates:
            print(f"  - {slug}")
        response = input("Continue anyway? (y/N): ")
        if response.lower() != 'y':
            print("❌ Aborted")
            sys.exit(1)

    # Append new terms
    data.extend(new_terms)

    # Write back
    with open(legal_json_path, 'w', encoding='utf-8') as f:
        json.dump(data, f, ensure_ascii=False, indent=2)

    final_count = len(data)
    print(f"✅ Successfully added {len(new_terms)} terms")
    print(f"📊 New total: {final_count} terms")
    print(f"📁 File: {legal_json_path}")

if __name__ == "__main__":
    main()
