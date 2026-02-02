#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
사회복지법/사회보장 용어 추가 스크립트
Theme: Social Welfare/Social Security Law
"""

import json
import os

# 파일 경로 설정
file_path = os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', 'data', 'terms', 'legal.json')

# 추가할 10개 용어
new_terms = [
    {
        "slug": "an-sinh-xa-hoi",
        "korean": "사회보장",
        "vietnamese": "An sinh xã hội",
        "hanja": "社會保障",
        "hanjaReading": "社(모일 사) + 會(모일 회) + 保(지킬 보) + 障(막을 장)",
        "pronunciation": "안신 싸호이",
        "meaningKo": "국가가 국민의 생활 안정과 복지 향상을 위해 시행하는 제도로, 질병·장애·노령·실업·사망 등의 사회적 위험으로부터 국민을 보호합니다. 통역 시 베트남의 'An sinh xã hội'는 한국의 '사회보장'보다 포괄적 범위가 좁을 수 있으므로, 구체적으로 어떤 제도를 의미하는지 확인이 필요합니다. 한국은 사회보험, 공공부조, 사회서비스로 체계가 세분화되어 있으나, 베트남은 아직 발전 단계에 있어 제도 간 차이를 명확히 설명해야 합니다.",
        "meaningVi": "Hệ thống các chính sách và biện pháp do nhà nước thực hiện nhằm bảo vệ người dân trước các rủi ro xã hội như bệnh tật, thất nghiệp, già yếu, tử vong. Bao gồm bảo hiểm xã hội, trợ cấp xã hội và dịch vụ phúc lợi công cộng.",
        "context": "사회보장기본법, 복지정책, 사회보험 제도",
        "culturalNote": "한국의 사회보장 제도는 4대 보험(국민연금, 건강보험, 고용보험, 산재보험)을 중심으로 발달했으며, 전국민 건강보험을 달성한 선진적 체계입니다. 베트남은 현재 사회보험 제도를 확대 중이나 적용 범위가 한국보다 제한적입니다. 통역 시 양국의 제도 성숙도 차이를 고려하여 설명해야 하며, 베트남 투자기업의 경우 한국과 다른 사회보험 납부 의무를 이행해야 함을 주의해야 합니다.",
        "commonMistakes": [
            {
                "mistake": "'사회보장'을 'Phúc lợi xã hội'로만 번역",
                "correction": "'An sinh xã hội' 사용",
                "explanation": "'Phúc lợi'는 복지 일반을 의미하나, 'An sinh'는 법적 보장 체계를 명확히 나타냄"
            },
            {
                "mistake": "사회보험과 사회보장을 동일 개념으로 통역",
                "correction": "사회보장은 사회보험을 포함하는 상위 개념임을 설명",
                "explanation": "사회보장 = 사회보험 + 공공부조 + 사회서비스"
            },
            {
                "mistake": "한국 4대 보험을 베트남 제도와 직접 대응시킴",
                "correction": "각 보험의 적용 범위와 내용을 구체적으로 설명",
                "explanation": "베트남 사회보험은 한국의 국민연금+건강보험+고용보험+산재보험을 통합한 형태로 운영"
            }
        ],
        "examples": [
            {
                "ko": "우리나라는 전 국민 사회보장 제도를 시행하고 있습니다.",
                "vi": "Hàn Quốc đang thực hiện chế độ an sinh xã hội toàn dân.",
                "situation": "formal"
            },
            {
                "ko": "사회보장 급여는 신청주의 원칙에 따라 지급됩니다.",
                "vi": "Trợ cấp an sinh xã hội được chi trả theo nguyên tắc đăng ký chủ động.",
                "situation": "formal"
            },
            {
                "ko": "사회보장정보시스템에서 본인의 가입 이력을 확인할 수 있습니다.",
                "vi": "Bạn có thể kiểm tra lịch sử tham gia trên Hệ thống thông tin an sinh xã hội.",
                "situation": "informal"
            }
        ],
        "relatedTerms": ["사회보험", "공공부조", "복지정책", "사회서비스"]
    },
    {
        "slug": "bao-hiem-that-nghiep",
        "korean": "고용보험",
        "vietnamese": "Bảo hiểm thất nghiệp",
        "hanja": "雇傭保險",
        "hanjaReading": "雇(품팔 고) + 傭(품팔 용) + 保(지킬 보) + 險(험할 험)",
        "pronunciation": "바오히엠 텃응이엡",
        "meaningKo": "근로자가 실직한 경우 생활 안정을 위한 급여를 지급하고 재취업을 지원하는 사회보험 제도입니다. 통역 시 한국의 고용보험은 실업급여뿐만 아니라 직업능력개발, 고용안정, 육아휴직 급여 등 다양한 사업을 포함하는 점을 설명해야 합니다. 베트남의 'Bảo hiểm thất nghiệp'는 주로 실업급여에 초점을 맞추고 있어, 한국 제도의 포괄성을 강조할 필요가 있습니다. 또한 가입 대상, 보험료율, 급여 수준이 양국 간 상이하므로 구체적 수치 확인이 중요합니다.",
        "meaningVi": "Chế độ bảo hiểm xã hội cung cấp trợ cấp thất nghiệp và hỗ trợ tái tìm việc cho người lao động bị mất việc làm. Ở Hàn Quốc, bảo hiểm thất nghiệp còn bao gồm phát triển năng lực nghề nghiệp, ổn định việc làm và trợ cấp nghỉ thai sản.",
        "context": "고용보험법, 실업급여, 재취업 지원",
        "culturalNote": "한국의 고용보험은 1995년 도입되어 전 사업장으로 확대 적용되며, 실업급여 외에도 출산전후휴가급여, 육아휴직급여 등 일·가정 양립 지원을 포함합니다. 베트남은 2009년 고용보험법을 시행했으나 적용 범위가 제한적이고, 주로 실업급여에 집중되어 있습니다. 통역 시 한국 기업이 베트남 현지법인에서 고용보험 납부 의무를 이행해야 하며, 한국과 보험료율(한국 1.8%, 베트남 1%)이 다름을 안내해야 합니다.",
        "commonMistakes": [
            {
                "mistake": "'실업급여'와 '고용보험'을 혼용",
                "correction": "고용보험은 제도, 실업급여는 급여 종류임을 구분",
                "explanation": "고용보험 제도 안에 실업급여, 육아휴직급여 등 여러 급여가 포함됨"
            },
            {
                "mistake": "'Trợ cấp thất nghiệp'로만 번역",
                "correction": "'Bảo hiểm thất nghiệp' 사용",
                "explanation": "'Trợ cấp'는 급여만 의미하나, 'Bảo hiểm'은 보험 제도 전체를 지칭"
            },
            {
                "mistake": "고용보험 가입 요건을 양국 동일하게 설명",
                "correction": "한국은 1개월 이상 근로자, 베트남은 3개월 이상 계약직 등 차이 명시",
                "explanation": "가입 기준이 국가별로 다름"
            }
        ],
        "examples": [
            {
                "ko": "고용보험 가입 이력이 있어야 실업급여를 받을 수 있습니다.",
                "vi": "Phải có lịch sử tham gia bảo hiểm thất nghiệp mới được nhận trợ cấp thất nghiệp.",
                "situation": "formal"
            },
            {
                "ko": "육아휴직 급여는 고용보험에서 지급됩니다.",
                "vi": "Trợ cấp nghỉ nuôi con nhỏ được chi trả từ bảo hiểm thất nghiệp.",
                "situation": "formal"
            },
            {
                "ko": "회사가 고용보험료를 안 냈으면 나중에 문제 생겨요.",
                "vi": "Nếu công ty không đóng bảo hiểm thất nghiệp thì sau này sẽ có vấn đề.",
                "situation": "informal"
            }
        ],
        "relatedTerms": ["실업급여", "육아휴직급여", "직업훈련", "재취업지원서비스"]
    },
    {
        "slug": "che-do-huu-tri",
        "korean": "연금제도",
        "vietnamese": "Chế độ hưu trí",
        "hanja": "年金制度",
        "hanjaReading": "年(해 연) + 金(쇠 금) + 制(제도 제) + 度(법도 도)",
        "pronunciation": "째도 허우찌",
        "meaningKo": "노령, 장애, 사망 등으로 소득 능력을 상실한 경우 본인이나 유족에게 정기적으로 급여를 지급하는 사회보험 제도입니다. 통역 시 한국의 국민연금은 전 국민 강제가입 방식이나, 베트남은 공무원·기업 근로자 중심으로 운영되어 적용 범위가 다릅니다. 연금 수급 개시 연령(한국 만 63세→65세 상향 중, 베트남 남성 60세·여성 55세)과 보험료율(한국 9%, 베트남 8%)도 차이가 있으므로 구체적 설명이 필요합니다. 또한 한국은 기초연금 등 다층 노후소득보장 체계를 갖추고 있음을 안내해야 합니다.",
        "meaningVi": "Chế độ bảo hiểm xã hội chi trả trợ cấp định kỳ cho người lao động hoặc gia đình khi mất khả năng lao động do tuổi già, tàn tật hoặc tử vong. Hàn Quốc có hệ thống đa tầng bao gồm lương hưu quốc dân và lương hưu cơ bản cho người cao tuổi.",
        "context": "국민연금법, 노후소득보장, 기초연금",
        "culturalNote": "한국의 국민연금은 1988년 도입되어 전 국민 대상으로 확대되었으며, 저소득 노인을 위한 기초연금이 별도 운영됩니다. 베트남의 연금제도는 강제사회보험과 자발적사회보험으로 구분되며, 농민·자영업자는 자발적 가입 대상입니다. 통역 시 한국 기업의 베트남 주재원은 한국 국민연금 계속 가입이 가능하나, 현지 채용 직원은 베트남 연금에 가입해야 함을 설명해야 합니다. 또한 베트남은 일시금 수령 선택이 가능하나 한국은 연금 방식이 원칙임을 주의해야 합니다.",
        "commonMistakes": [
            {
                "mistake": "'Lương hưu'와 'Chế độ hưu trí'를 혼동",
                "correction": "'Chế độ hưu trí'는 제도, 'Lương hưu'는 연금액을 의미",
                "explanation": "제도와 급여를 구분하여 번역해야 정확함"
            },
            {
                "mistake": "연금 수급 연령을 양국 동일하게 안내",
                "correction": "한국 만 63~65세, 베트남 남성 60세·여성 55세로 차이 명시",
                "explanation": "수급 개시 연령이 국가별로 다름"
            },
            {
                "mistake": "기초연금을 국민연금의 일부로 설명",
                "correction": "기초연금은 별도 제도임을 구분",
                "explanation": "국민연금(보험료 납부 기반)과 기초연금(세금 기반)은 재원과 대상이 다름"
            }
        ],
        "examples": [
            {
                "ko": "국민연금 가입 기간이 10년 이상이어야 노령연금을 받을 수 있습니다.",
                "vi": "Phải đóng bảo hiểm hưu trí quốc dân tối thiểu 10 năm mới được nhận lương hưu tuổi già.",
                "situation": "formal"
            },
            {
                "ko": "연금제도 개혁으로 수급 연령이 단계적으로 상향됩니다.",
                "vi": "Do cải cách chế độ hưu trí, tuổi nhận lương hưu sẽ được nâng dần.",
                "situation": "formal"
            },
            {
                "ko": "부모님 기초연금 신청하려면 어디 가야 해요?",
                "vi": "Muốn đăng ký lương hưu cơ bản cho bố mẹ thì phải đến đâu ạ?",
                "situation": "informal"
            }
        ],
        "relatedTerms": ["국민연금", "기초연금", "노령연금", "퇴직연금"]
    },
    {
        "slug": "tro-cap-xa-hoi",
        "korean": "사회수당",
        "vietnamese": "Trợ cấp xã hội",
        "hanja": "社會手當",
        "hanjaReading": "社(모일 사) + 會(모일 회) + 手(손 수) + 當(마땅 당)",
        "pronunciation": "쩌깝 싸호이",
        "meaningKo": "국가나 지방자치단체가 일정 요건을 충족하는 국민에게 정기적으로 지급하는 현금 급여로, 보험료 납부와 무관하게 지급됩니다. 통역 시 사회수당은 기여금 없이 국가 재정으로 지급되는 비기여형 급여임을 명확히 해야 합니다. 한국의 대표적 사회수당으로는 기초연금, 아동수당, 장애인연금 등이 있으며, 소득·재산 기준을 적용하거나(선별적) 전체 대상에게 지급(보편적)하는 방식으로 구분됩니다. 베트nam에서는 사회부조적 성격의 'Trợ cấp'이 주로 빈곤층·취약계층 대상이므로, 한국의 보편적 수당과 차이가 있음을 설명해야 합니다.",
        "meaningVi": "Khoản trợ cấp tiền mặt định kỳ do nhà nước hoặc chính quyền địa phương chi trả cho công dân đáp ứng điều kiện nhất định, không cần đóng phí bảo hiểm. Bao gồm lương hưu cơ bản, trợ cấp trẻ em, trợ cấp người khuyết tật.",
        "context": "사회보장기본법, 공공부조, 복지급여",
        "culturalNote": "한국은 2000년대 이후 사회수당을 확대하여 아동수당(2018년), 기초연금(2014년) 등을 도입했으며, 일부는 소득 기준 없이 보편적으로 지급됩니다. 베트남의 사회부조는 주로 빈곤층, 장애인, 고아 등 취약계층에 집중되며, 지급 수준이 한국보다 낮습니다. 통역 시 한국의 아동수당은 전체 아동 대상(소득 무관)이나 베트남은 빈곤 가정 아동에게만 지급되는 차이를 설명해야 합니다. 또한 한국 지자체별로 추가 수당(청년수당, 출산장려금 등)이 있어 지역마다 혜택이 다름을 안내할 필요가 있습니다.",
        "commonMistakes": [
            {
                "mistake": "사회수당과 사회보험급여를 혼동",
                "correction": "사회수당은 보험료 없이 지급, 사회보험급여는 보험료 납부 필요",
                "explanation": "재원(세금 vs 보험료)과 지급 조건이 다름"
            },
            {
                "mistake": "'Trợ cấp xã hội'를 공공부조 전체로 번역",
                "correction": "사회수당은 정기 현금급여, 공공부조는 더 넓은 개념",
                "explanation": "공공부조는 현금·현물·서비스를 모두 포함하나, 사회수당은 현금급여에 한정"
            },
            {
                "mistake": "한국 아동수당을 베트남 빈곤아동 수당과 동일시",
                "correction": "한국은 보편적, 베트남은 선별적 지급임을 명시",
                "explanation": "대상 범위와 지급 조건이 근본적으로 다름"
            }
        ],
        "examples": [
            {
                "ko": "기초연금은 65세 이상 소득 하위 70% 노인에게 지급되는 사회수당입니다.",
                "vi": "Lương hưu cơ bản là trợ cấp xã hội dành cho người cao tuổi từ 65 tuổi thuộc 70% thu nhập thấp nhất.",
                "situation": "formal"
            },
            {
                "ko": "아동수당은 매달 25일에 계좌로 입금됩니다.",
                "vi": "Trợ cấp trẻ em được chuyển vào tài khoản vào ngày 25 hàng tháng.",
                "situation": "formal"
            },
            {
                "ko": "장애인연금 받으려면 장애 등급이 어떻게 돼야 해요?",
                "vi": "Muốn nhận trợ cấp người khuyết tật thì mức độ khuyết tật phải như thế nào ạ?",
                "situation": "informal"
            }
        ],
        "relatedTerms": ["기초연금", "아동수당", "장애인연금", "공공부조"]
    },
    {
        "slug": "nguoi-khuyet-tat",
        "korean": "장애인",
        "vietnamese": "Người khuyết tật",
        "hanja": "障碍人",
        "hanjaReading": "障(막을 장) + 碍(거리낄 애) + 人(사람 인)",
        "pronunciation": "응어이 쿠엣닷",
        "meaningKo": "신체적·정신적 손상으로 일상생활이나 사회생활에 제약을 받는 사람을 법적으로 지칭하는 용어입니다. 통역 시 한국의 '장애인'은 법적 등록 절차를 거쳐 인정되며, 장애 정도에 따라 '심한 장애'와 '심하지 않은 장애'로 구분됩니다(2019년 개정). 베트남의 'Người khuyết tật'은 장애 정도를 경증·중증·특중증으로 분류하며, 평가 기준이 한국과 다릅니다. 장애인복지법에 따른 지원(활동지원서비스, 장애인연금, 세제 혜택 등)이 양국 간 차이가 크므로 구체적 설명이 필요합니다.",
        "meaningVi": "Người bị tổn thương về thể chất hoặc tinh thần dẫn đến hạn chế trong sinh hoạt hàng ngày và xã hội, được công nhận theo pháp luật. Ở Hàn Quốc, người khuyết tật được phân loại thành 'khuyết tật nặng' và 'khuyết tật không nặng' từ năm 2019.",
        "context": "장애인복지법, 장애인차별금지법, 인권",
        "culturalNote": "한국은 2007년 '장애인차별금지 및 권리구제 등에 관한 법률'을 제정하여 장애인 인권 보호를 강화했으며, 장애인 고용의무제(50인 이상 사업장 3.1%)를 시행합니다. 베트남은 2010년 장애인법을 제정했으나 사회적 인식과 인프라가 발전 중입니다. 통역 시 한국의 '장애인'이라는 용어는 과거 '장애자'로 불리던 것을 인권 존중 차원에서 변경한 것임을 설명하고, 베트남에서도 'Người tàn tật'(장애자) 대신 'Người khuyết tật'(결함 있는 사람)이라는 존중어를 사용함을 안내해야 합니다.",
        "commonMistakes": [
            {
                "mistake": "'Người tàn tật'으로 번역",
                "correction": "'Người khuyết tật' 사용",
                "explanation": "'Tàn tật'은 비하적 뉘앙스, 'Khuyết tật'이 공식적이고 존중하는 표현"
            },
            {
                "mistake": "장애 등급을 1~6급으로 설명",
                "correction": "2019년 이후 '심한 장애'/'심하지 않은 장애' 2단계 체계로 변경됨을 안내",
                "explanation": "구 장애등급제가 폐지되고 장애정도제로 전환됨"
            },
            {
                "mistake": "장애인복지 혜택을 양국 동일하게 안내",
                "correction": "한국의 활동지원서비스, 이동지원 등 구체적 제도를 설명",
                "explanation": "베트남은 아직 해당 서비스가 제한적이므로 한국 제도의 특수성을 명시해야 함"
            }
        ],
        "examples": [
            {
                "ko": "장애인등록증을 제출하시면 세금 감면 혜택을 받으실 수 있습니다.",
                "vi": "Nếu xuất trình thẻ đăng ký người khuyết tật, bạn có thể được miễn giảm thuế.",
                "situation": "formal"
            },
            {
                "ko": "장애인 편의시설 설치는 법적 의무사항입니다.",
                "vi": "Lắp đặt tiện ích cho người khuyết tật là nghĩa vụ pháp lý.",
                "situation": "formal"
            },
            {
                "ko": "장애인 주차구역에 일반 차량이 주차하면 과태료 나와요.",
                "vi": "Nếu xe thường đỗ ở chỗ dành cho người khuyết tật sẽ bị phạt.",
                "situation": "informal"
            }
        ],
        "relatedTerms": ["장애인복지법", "장애인차별금지법", "장애인연금", "활동지원서비스"]
    },
    {
        "slug": "quyen-tre-em",
        "korean": "아동권리",
        "vietnamese": "Quyền trẻ em",
        "hanja": "兒童權利",
        "hanjaReading": "兒(어린아이 아) + 童(아이 동) + 權(권세 권) + 利(이로울 리)",
        "pronunciation": "꾸엔 쩨엠",
        "meaningKo": "아동이 인간으로서 누려야 할 기본적 권리로, 생존권·보호권·발달권·참여권을 포함합니다. 통역 시 한국은 UN 아동권리협약을 비준(1991년)하고 아동복지법을 통해 아동학대 예방, 교육권, 건강권 등을 보장하고 있음을 설명해야 합니다. 베트남도 아동법(2016년)을 통해 아동 보호를 강화했으나, 아동노동 금지 연령(한국 15세, 베트남 13세 이상 일부 허용)과 체벌 금지 등 세부 기준이 다릅니다. 또한 한국은 아동학대범죄처벌특례법으로 학대 가해자를 엄벌하며, 아동보호전문기관을 운영하는 점을 강조해야 합니다.",
        "meaningVi": "Các quyền cơ bản mà trẻ em phải được hưởng, bao gồm quyền sống, quyền được bảo vệ, quyền phát triển và quyền tham gia. Hàn Quốc đã phê chuẩn Công ước về quyền trẻ em của LHQ năm 1991 và ban hành Luật phúc lợi trẻ em.",
        "context": "아동복지법, 아동학대처벌법, UN아동권리협약",
        "culturalNote": "한국은 2000년대 이후 아동학대 신고의무제를 강화하고, 교사·의료인 등 직업군에 신고의무를 부과했습니다. 2014년에는 아동학대범죄처벌특례법을 제정하여 친권자의 학대도 형사처벌 대상으로 명시했습니다. 베트남은 전통적으로 가정 내 훈육 문화가 강하나, 최근 아동보호법 강화로 체벌을 제한하고 있습니다. 통역 시 한국의 아동학대 신고전화(112), 아동보호전문기관 운영 등 구체적 제도를 안내하고, 베트남 부모가 한국에서 자녀를 양육할 때 체벌 금지 등 법적 차이를 명확히 설명해야 합니다.",
        "commonMistakes": [
            {
                "mistake": "'아동'과 '청소년'을 혼용",
                "correction": "아동은 만 18세 미만, 청소년은 만 9~24세로 법적 정의가 다름",
                "explanation": "아동복지법과 청소년기본법의 대상 연령이 상이함"
            },
            {
                "mistake": "'Quyền trẻ em'을 단순 복지로만 설명",
                "correction": "생존권·보호권·발달권·참여권 4대 권리를 명시",
                "explanation": "아동권리는 복지를 넘어 의견 표명권, 차별받지 않을 권리 등을 포함"
            },
            {
                "mistake": "아동학대 신고의무를 선택사항으로 안내",
                "correction": "교사·의료인 등 직업군은 신고의무자로 법적 의무임을 강조",
                "explanation": "신고의무 위반 시 과태료 부과"
            }
        ],
        "examples": [
            {
                "ko": "모든 아동은 학대와 방임으로부터 보호받을 권리가 있습니다.",
                "vi": "Mọi trẻ em đều có quyền được bảo vệ khỏi bạo hành và bỏ bê.",
                "situation": "formal"
            },
            {
                "ko": "아동의 의견을 존중하는 것은 아동권리협약의 핵심입니다.",
                "vi": "Tôn trọng ý kiến của trẻ em là cốt lõi của Công ước về quyền trẻ em.",
                "situation": "formal"
            },
            {
                "ko": "아이한테 체벌하면 신고당할 수 있어요.",
                "vi": "Nếu đánh con có thể bị t고 cáo.",
                "situation": "informal"
            }
        ],
        "relatedTerms": ["아동복지법", "아동학대", "친권", "아동보호전문기관"]
    },
    {
        "slug": "bao-tro-xa-hoi",
        "korean": "사회부조",
        "vietnamese": "Bảo trợ xã hội",
        "hanja": "社會扶助",
        "hanjaReading": "社(모일 사) + 會(모일 회) + 扶(도울 부) + 助(도울 조)",
        "pronunciation": "바오쩌 싸호이",
        "meaningKo": "생활 유지 능력이 없거나 생활이 어려운 국민에게 국가가 필요한 급여를 제공하여 최저생활을 보장하고 자활을 지원하는 제도입니다. 통역 시 사회부조는 사회보험과 달리 보험료 납부 없이 국가 재정으로 지원되며, 소득·재산 조사를 거쳐 선별적으로 제공됩니다. 한국의 대표적 사회부조는 국민기초생활보장제도로, 생계·의료·주거·교육급여를 지급합니다. 베트남의 'Bảo trợ xã hội'는 주로 극빈층, 무의탁 노인, 고아 등에게 시설 보호 또는 현금 지원을 하며, 한국보다 지원 수준이 낮고 대상이 제한적입니다.",
        "meaningVi": "Chế độ do nhà nước cung cấp trợ cấp cần thiết cho công dân không có khả năng duy trì cuộc sống hoặc gặp khó khăn, nhằm đảm bảo mức sống tối thiểu và hỗ trợ tự lập. Ở Hàn Quốc, chế độ bảo trợ xã hội chính là Chế độ đảm bảo sinh hoạt tối thiểu quốc dân.",
        "context": "국민기초생활보장법, 공공부조, 빈곤정책",
        "culturalNote": "한국은 2000년 국민기초생활보장법을 시행하여 과거 생활보호제도를 전면 개편했으며, 근로능력 유무와 관계없이 소득인정액이 기준 이하이면 지원합니다. 2015년부터는 맞춤형 급여로 개편하여 생계·의료·주거·교육급여를 각각 신청할 수 있게 했습니다. 베트남의 사회부조는 주로 빈곤 가구에 대한 현금 지원과 시설 보호 중심이며, 자활 지원 프로그램이 제한적입니다. 통역 시 한국의 자활사업(취업 지원, 창업 교육 등)이 베트남보다 체계적임을 설명하고, 베트남 이주민이 한국에서 국민기초생활보장 수급 요건(국적·체류자격)을 충족하기 어려움을 안내해야 합니다.",
        "commonMistakes": [
            {
                "mistake": "사회부조와 사회보험을 혼동",
                "correction": "사회보험은 보험료 기반, 사회부조는 조세 기반",
                "explanation": "재원과 대상 선정 방식이 근본적으로 다름"
            },
            {
                "mistake": "'Bảo trợ xã hội'를 시설 보호만으로 번역",
                "correction": "현금급여와 현물급여를 모두 포함함을 명시",
                "explanation": "베트남에서는 주로 시설 보호를 의미하나, 한국은 현금급여가 중심"
            },
            {
                "mistake": "외국인도 동일하게 수급 가능하다고 안내",
                "correction": "국민기초생활보장은 원칙적으로 한국 국적자 대상, 일부 예외 존재",
                "explanation": "외국인은 수급 요건이 매우 제한적 (난민, 결혼이민자 등 일부)"
            }
        ],
        "examples": [
            {
                "ko": "국민기초생활보장 수급자는 생계급여와 의료급여를 받을 수 있습니다.",
                "vi": "Người nhận trợ cấp đảm bảo sinh hoạt tối thiểu quốc dân có thể nhận trợ cấp sinh hoạt và trợ cấp y tế.",
                "situation": "formal"
            },
            {
                "ko": "사회부조는 빈곤층의 최저생활을 보장하는 최후의 사회안전망입니다.",
                "vi": "Bảo trợ xã hội là lưới an toàn xã hội cuối cùng đảm bảo mức sống tối thiểu cho người nghèo.",
                "situation": "formal"
            },
            {
                "ko": "기초생활수급자면 병원비 거의 안 내도 돼요.",
                "vi": "Nếu là người nhận trợ cấp tối thiểu thì hầu như không phải trả viện phí.",
                "situation": "informal"
            }
        ],
        "relatedTerms": ["국민기초생활보장제도", "생계급여", "의료급여", "자활사업"]
    },
    {
        "slug": "cham-soc-nguoi-cao-tuoi",
        "korean": "노인복지",
        "vietnamese": "Chăm sóc người cao tuổi",
        "hanja": "老人福祉",
        "hanjaReading": "老(늙을 로) + 人(사람 인) + 福(복 복) + 祉(복 지)",
        "pronunciation": "짬속 응어이까오뜨어이",
        "meaningKo": "노인의 심신 건강 유지와 생활 안정을 위해 국가와 지방자치단체가 제공하는 복지 서비스입니다. 통역 시 한국의 노인복지는 노인장기요양보험(2008년 도입)을 중심으로 재가·시설 돌봄 서비스를 제공하며, 기초연금·노인일자리사업·경로당 운영 등 다양한 지원이 이루어짐을 설명해야 합니다. 베트남의 'Chăm sóc người cao tuổi'는 가족 중심 돌봄 문화가 강하나, 최근 고령화로 노인법(2009년)을 제정하고 양로원 등 시설을 확충하고 있습니다. 한국은 만 65세 이상을 노인으로 정의하나, 베트남은 남성 60세·여성 55세 이상입니다.",
        "meaningVi": "Dịch vụ phúc lợi do nhà nước và chính quyền địa phương cung cấp để duy trì sức khỏe thể chất, tinh thần và ổn định cuộc sống cho người cao tuổi. Hàn Quốc có hệ thống bảo hiểm chăm sóc dài hạn cho người cao tuổi từ năm 2008.",
        "context": "노인복지법, 노인장기요양보험법, 고령화사회",
        "culturalNote": "한국은 2000년 고령화사회 진입 후 노인복지 정책을 대폭 확대하여, 노인장기요양보험으로 치매·중풍 등 일상생활이 어려운 노인에게 요양서비스를 제공합니다. 기초연금(월 최대 약 30만원)과 노인일자리사업도 병행합니다. 베트남은 유교 문화의 영향으로 자녀가 부모를 부양하는 전통이 강하나, 도시화로 핵가족화가 진행되며 노인 돌봄 서비스가 발전 중입니다. 통역 시 한국의 요양보호사 제도, 주야간보호센터, 노인복지관 등 구체적 서비스를 안내하고, 베트남 이주민 부모가 한국에서 장기요양서비스를 받으려면 건강보험 가입이 선행되어야 함을 설명해야 합니다.",
        "commonMistakes": [
            {
                "mistake": "'노인복지'를 연금 지급으로만 설명",
                "correction": "연금 외에 돌봄서비스, 일자리, 여가활동 등 포괄적 지원임을 명시",
                "explanation": "노인복지는 소득보장+서비스 제공의 통합 개념"
            },
            {
                "mistake": "'Người già'로 번역",
                "correction": "'Người cao tuổi' 사용",
                "explanation": "'Già'는 '늙은'이라는 부정적 뉘앙스, 'Cao tuổi'가 존중 표현"
            },
            {
                "mistake": "노인장기요양보험을 건강보험과 동일시",
                "correction": "별도 보험으로 65세 이상 또는 노인성 질환자 대상임을 구분",
                "explanation": "장기요양보험은 건강보험과 재원·대상·급여가 다름"
            }
        ],
        "examples": [
            {
                "ko": "노인장기요양보험 등급을 받으면 요양원이나 방문요양 서비스를 이용할 수 있습니다.",
                "vi": "Nếu được xếp hạng bảo hiểm chăm sóc dài hạn người cao tuổi, có thể sử dụng dịch vụ nhà dưỡng lão hoặc chăm sóc tại nhà.",
                "situation": "formal"
            },
            {
                "ko": "경로당에서 노인들이 여가 활동을 하실 수 있습니다.",
                "vi": "Người cao tuổi có thể tham gia hoạt động giải trí tại trung tâm người cao tuổi.",
                "situation": "formal"
            },
            {
                "ko": "우리 할머니 요양보호사 선생님이 매일 와서 도와주세요.",
                "vi": "Bà tôi có cô chăm sóc người cao tuổi đến giúp mỗi ngày.",
                "situation": "informal"
            }
        ],
        "relatedTerms": ["노인장기요양보험", "요양보호사", "경로당", "노인일자리사업"]
    },
    {
        "slug": "phong-chong-bao-luc-gia-dinh",
        "korean": "가정폭력방지",
        "vietnamese": "Phòng chống bạo lực gia đình",
        "hanja": "家庭暴力防止",
        "hanjaReading": "家(집 가) + 庭(뜰 정) + 暴(사나울 폭) + 力(힘 력) + 防(막을 방) + 止(그칠 지)",
        "pronunciation": "퐁쫑 바오릭 자딘",
        "meaningKo": "가정 구성원 사이의 신체적·정신적·성적 폭력을 예방하고 피해자를 보호하기 위한 법적·사회적 조치입니다. 통역 시 한국의 가정폭력방지법(1997년 제정, 2021년 전부개정)은 피해자 보호와 가해자 처벌을 강화하며, 가정폭력 신고 시 경찰의 즉시 출동 의무와 임시조치(접근금지, 퇴거 등)를 규정하고 있음을 설명해야 합니다. 베트남도 2007년 가정폭력방지법을 제정했으나, 전통적 가부장 문화로 신고율이 낮고 피해자 보호 시설이 부족합니다. 한국은 가정폭력상담소, 보호시설, 해바라기센터(성폭력·가정폭력 통합 지원) 등 지원 체계가 발달했음을 강조해야 합니다.",
        "meaningVi": "Các biện pháp pháp lý và xã hội nhằm ngăn chặn bạo lực thể chất, tinh thần, tình dục giữa các thành viên gia đình và bảo vệ nạn nhân. Hàn Quốc có Luật phòng chống bạo lực gia đình từ năm 1997 và được cải cách toàn diện năm 2021.",
        "context": "가정폭력방지법, 가정보호사건, 피해자보호",
        "culturalNote": "한국은 과거 가정 내 폭력을 사적 영역으로 간주했으나, 1997년 가정폭력방지법 제정 이후 국가 개입이 강화되었습니다. 2021년 개정법은 피해자 보호명령제를 도입하여 법원이 가해자에게 접근금지·퇴거·친권제한 등을 명령할 수 있게 했습니다. 베트남도 2007년 이후 가정폭력 예방 캠페인을 전개하나, 가족 내 문제를 외부에 드러내지 않는 문화적 특성으로 신고가 저조합니다. 통역 시 한국의 가정폭력 긴급전화(1366), 경찰의 즉시 출동 의무, 피해자 무료 법률 지원 등 구체적 제도를 안내하고, 베트남 이주여성이 한국에서 가정폭력 피해 시 체류자격과 무관하게 보호받을 수 있음을 명시해야 합니다.",
        "commonMistakes": [
            {
                "mistake": "'Bạo lực gia đình'과 'Bạo hành gia đình'을 혼용",
                "correction": "'Bạo lực gia đình' 사용",
                "explanation": "법률 용어로는 'Bạo lực'이 공식 표현"
            },
            {
                "mistake": "가정폭력을 형사 사건으로만 설명",
                "correction": "가정보호사건(치료·상담 중심)과 형사사건으로 구분됨을 명시",
                "explanation": "경미한 경우 가정보호사건으로 처리되어 상담·교육 명령"
            },
            {
                "mistake": "피해자가 한국 국적자여야만 보호받는다고 안내",
                "correction": "외국인 배우자도 동일하게 보호받으며 체류 지원 가능",
                "explanation": "이주여성은 가정폭력 피해 시 체류자격 특례 적용"
            }
        ],
        "examples": [
            {
                "ko": "가정폭력 신고 시 경찰은 즉시 현장에 출동하여 피해자를 보호합니다.",
                "vi": "Khi nhận tin báo bạo lực gia đình, cảnh sát phải có mặt ngay lập tức để bảo vệ nạn nhân.",
                "situation": "formal"
            },
            {
                "ko": "법원은 가해자에게 피해자 접근 금지 명령을 내릴 수 있습니다.",
                "vi": "Tòa án có thể ra lệnh cấm người gây bạo lực tiếp cận nạn nhân.",
                "situation": "formal"
            },
            {
                "ko": "맞으면 참지 말고 1366 전화하세요.",
                "vi": "Nếu bị đánh thì đừng chịu đựng, hãy gọi 1366.",
                "situation": "informal"
            }
        ],
        "relatedTerms": ["가정폭력방지법", "피해자보호명령", "가정폭력상담소", "긴급전화1366"]
    },
    {
        "slug": "binh-dang-gioi",
        "korean": "양성평등",
        "vietnamese": "Bình đẳng giới",
        "hanja": "兩性平等",
        "hanjaReading": "兩(두 량) + 性(성품 성) + 平(평평할 평) + 等(무리 등)",
        "pronunciation": "빈당 저이",
        "meaningKo": "성별에 따른 차별 없이 동등한 권리와 기회를 보장하며, 책임을 공평하게 분담하는 것을 의미합니다. 통역 시 한국은 양성평등기본법(2015년 제정)을 통해 정치·경제·사회·문화 모든 영역에서 성평등을 실현하고자 하며, 여성가족부가 정책을 총괄함을 설명해야 합니다. 성별영향평가제도, 공공기관 성별균형 목표제(임원 40% 이상) 등 구체적 제도가 시행되고 있습니다. 베트남은 'Bình đẳng giới'를 헌법에 명시하고 있으나, 전통적 성역할 인식이 여전히 강하며, 여성의 정치·경제 참여율이 한국보다 낮습니다.",
        "meaningVi": "Đảm bảo quyền lợi và cơ hội bình đẳng không phân biệt giới tính, đồng thời chia sẻ trách nhiệm công bằng. Hàn Quốc có Luật cơ bản về bình đẳng giới từ năm 2015 và thực hiện chế độ đánh giá tác động giới tính trong các chính sách công.",
        "context": "양성평등기본법, 성차별 금지, 여성정책",
        "culturalNote": "한국은 1995년 여성발전기본법 이후 2015년 양성평등기본법으로 전환하여, 여성뿐 아니라 남성의 성평등도 강조합니다. 직장 내 성희롱 예방교육 의무화, 적극적 고용개선조치(500인 이상 사업장) 등이 시행되며, 최근에는 성별임금격차 해소와 돌봄노동 분담이 주요 과제입니다. 베트남은 여성의 경제활동 참가율은 높으나 관리직·정치 대표성은 낮으며, 가사노동 분담이 여성에게 편중되어 있습니다. 통역 시 한국의 육아휴직 부모 분할 사용 제도, 배우자 출산휴가(10일) 등 일·가정 양립 정책을 설명하고, 베트남 기업이 한국 진출 시 양성평등 관련 법규 준수가 필수임을 안내해야 합니다.",
        "commonMistakes": [
            {
                "mistake": "'Bình đẳng nam nữ'로 번역",
                "correction": "'Bình đẳng giới' 사용",
                "explanation": "'Giới'는 성별 정체성을 포괄하는 현대적 용어"
            },
            {
                "mistake": "양성평등을 여성 우대 정책으로 설명",
                "correction": "남녀 모두의 평등을 추구하며, 성별 고정관념 해소가 목표임을 명시",
                "explanation": "양성평등은 여성만의 이슈가 아니라 사회 전체의 문제"
            },
            {
                "mistake": "성평등 교육을 선택사항으로 안내",
                "correction": "직장 내 성희롱 예방교육은 법적 의무사항",
                "explanation": "연 1회 이상 교육 실시 의무, 위반 시 과태료"
            }
        ],
        "examples": [
            {
                "ko": "양성평등 실현을 위해 공공기관 임원의 40% 이상을 여성으로 임명해야 합니다.",
                "vi": "Để thực hiện bình đẳng giới, các cơ quan công phải bổ nhiệm ít nhất 40% lãnh đạo là nữ giới.",
                "situation": "formal"
            },
            {
                "ko": "성별을 이유로 채용에서 차별하는 것은 불법입니다.",
                "vi": "Phân biệt đối xử trong tuyển dụng vì lý do giới tính là bất hợp pháp.",
                "situation": "formal"
            },
            {
                "ko": "우리 회사는 남자도 육아휴직 쓸 수 있어요.",
                "vi": "Công ty chúng tôi cho cả nam giới nghỉ nuôi con nhỏ.",
                "situation": "informal"
            }
        ],
        "relatedTerms": ["양성평등기본법", "성차별금지", "성별영향평가", "적극적고용개선조치"]
    }
]

def main():
    # JSON 파일 읽기
    with open(file_path, 'r', encoding='utf-8') as f:
        data = json.load(f)

    # 기존 slug 목록 (중복 방지)
    existing_slugs = {term['slug'] for term in data}

    # 중복되지 않은 용어만 추가
    added_count = 0
    for term in new_terms:
        if term['slug'] not in existing_slugs:
            data.append(term)
            existing_slugs.add(term['slug'])
            added_count += 1
            print(f"✅ 추가됨: {term['slug']} ({term['korean']})")
        else:
            print(f"⚠️  중복 스킵: {term['slug']} ({term['korean']})")

    # JSON 파일 저장 (들여쓰기 2칸, 유니코드 그대로, 마지막 줄바꿈)
    with open(file_path, 'w', encoding='utf-8') as f:
        json.dump(data, f, ensure_ascii=False, indent=2)
        f.write('\n')

    print(f"\n{'='*60}")
    print(f"✨ 작업 완료: {added_count}개 용어 추가됨")
    print(f"📊 전체 용어 수: {len(data)}개")
    print(f"📂 파일 위치: {file_path}")
    print(f"{'='*60}")

if __name__ == "__main__":
    main()
