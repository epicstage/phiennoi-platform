#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""군형법 용어 추가 스크립트 (v7-g)"""

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
            "slug": "toa-an-quan-su",
            "korean": "군사법원",
            "vietnamese": "Tòa án quân sự",
            "hanja": "軍事法院",
            "hanjaReading": "軍(군사 군) + 事(일 사) + 法(법 법) + 院(집 원)",
            "pronunciation": "똬안꾸언쓰",
            "meaningKo": "군사법원은 군인 및 군무원의 범죄를 심판하는 특별법원입니다. 통역 시 주의할 점은 베트남에서 군사법원(Tòa án quân sự)은 중앙군사법원(Tòa án quân sự trung ương)과 군단급 군사법원(Tòa án quân sự quân khu)으로 구분되며, 한국의 고등군사법원, 보통군사법원과 체계가 다릅니다. 한국에서는 평시 일반 군형법 사건은 보통군사법원에서, 항소심은 고등군사법원에서 다루지만, 베트남은 군단급 기준으로 관할이 나뉩니다. 통역 시 '군사재판소'라고 오역하지 않도록 주의하세요.",
            "meaningVi": "Tòa án quân sự là cơ quan tư pháp chuyên xét xử các tội phạm của quân nhân và nhân viên trong lực lượng vũ trang. Hệ thống tòa án quân sự Việt Nam gồm Tòa án quân sự trung ương và các Tòa án quân sự quân khu, khác với cấu trúc của Hàn Quốc.",
            "context": "군사법원 관할, 군형법 재판, 군사재판 절차 설명 시 사용",
            "culturalNote": "한국의 군사법원은 3심제(보통군사법원→고등군사법원→대법원)이지만 베트남은 중앙군사법원이 최고심입니다. 한국은 2022년부터 평시 군사법원 폐지 논의가 있었으나 유지 중이며, 베트남은 군사법원이 독립적으로 강력한 권한을 가집니다. 통역 시 양국 군사법원의 위상과 관할 범위 차이를 명확히 전달해야 합니다. 또한 한국은 군판사, 군검사가 법무관(법학전문대학원 출신)인 반면, 베트남은 정치 장교 출신이 많아 법률 전문성에 차이가 있을 수 있습니다.",
            "commonMistakes": [
                {
                    "mistake": "군사재판소 (Tòa xét xử quân sự)",
                    "correction": "군사법원 (Tòa án quân sự)",
                    "explanation": "'재판소'는 임시 기구를 의미하며 '법원'은 상설 기관입니다. 군사법원은 상설 특별법원이므로 'Tòa án'으로 표현해야 합니다."
                },
                {
                    "mistake": "군부대 법원 (Tòa án đơn vị quân đội)",
                    "correction": "군사법원 (Tòa án quân sự)",
                    "explanation": "부대 내부 징계위원회와 군사법원은 다릅니다. 군사법원은 독립된 사법기관입니다."
                },
                {
                    "mistake": "전시재판소 (Tòa án thời chiến)",
                    "correction": "군사법원 (Tòa án quân sự)",
                    "explanation": "군사법원은 평시와 전시 모두 운영되는 상설 기관입니다. 전시에만 운영되는 임시 재판소가 아닙니다."
                }
            ],
            "examples": [
                {
                    "ko": "피고인은 군사법원에서 항명죄로 기소되었습니다.",
                    "vi": "Bị cáo đã bị truy tố tội không tuân lệnh tại Tòa án quân sự.",
                    "situation": "formal"
                },
                {
                    "ko": "군사법원의 판결에 불복하여 고등군사법원에 항소했습니다.",
                    "vi": "Đã kháng cáo lên Tòa án quân sự cấp cao vì không đồng ý với phán quyết của Tòa án quân sự.",
                    "situation": "formal"
                },
                {
                    "ko": "군사법원 관할은 현역 군인에 한정됩니다.",
                    "vi": "Thẩm quyền của Tòa án quân sự chỉ giới hạn đối với quân nhân tại ngũ.",
                    "situation": "formal"
                }
            ],
            "relatedTerms": ["군검찰", "군형법", "군사재판", "항명죄"]
        },
        {
            "slug": "vien-kiem-sat-quan-su",
            "korean": "군검찰",
            "vietnamese": "Viện kiểm sát quân sự",
            "hanja": "軍檢察",
            "hanjaReading": "軍(군사 군) + 檢(조사할 검) + 察(살필 찰)",
            "pronunciation": "비엔끼엠삿꾸언쓰",
            "meaningKo": "군검찰은 군 관련 범죄를 수사하고 기소하는 군 특별검찰 기관입니다. 통역 시 주의할 점은 한국의 군검찰은 고등군검찰부와 보통군검찰부로 나뉘며, 법무관(군법무관)이 군검사로 임명됩니다. 베트남의 Viện kiểm sát quân sự는 중앙군검찰원과 군단급 군검찰원으로 구성되며, 군사법원에 대응하는 구조입니다. 통역 시 '군 수사기관'과 '군검찰'을 혼동하지 말아야 하며, 한국의 경우 군사경찰(헌병)이 수사하고 군검찰이 기소하는 분리 구조임을 베트남 측에 설명해야 합니다. 베트남은 검찰이 수사권과 기소권을 모두 가지므로 차이가 있습니다.",
            "meaningVi": "Viện kiểm sát quân sự là cơ quan công tố chuyên trách điều tra và truy tố các tội phạm liên quan đến quân đội. Hệ thống gồm Viện kiểm sát quân sự trung ương và các Viện kiểm sát quân sự quân khu, tương ứng với hệ thống tòa án quân sự.",
            "context": "군사범죄 수사, 기소, 재판 절차 설명 시 사용",
            "culturalNote": "한국의 군검찰은 일반 검찰청 소속이 아닌 국방부 소속으로, 군검사는 현역 법무관(장교)입니다. 반면 베트남의 군검찰은 최고인민검찰원 산하이지만 독립성이 강하며, 군검사는 군 정치 장교 출신이 많습니다. 한국은 2022년부터 평시 군검찰 권한 축소 논의가 있었으나 유지 중입니다. 통역 시 한국의 군검찰은 '군법무관 중 검사 임무를 맡은 자'라는 개념이며, 베트남의 군검찰은 '독립된 군 검찰 기관'이라는 차이를 명확히 전달해야 합니다. 또한 한국은 군검찰이 기소만 하고 수사는 헌병대가 하지만, 베트남은 군검찰이 직접 수사권을 행사할 수 있습니다.",
            "commonMistakes": [
                {
                    "mistake": "군 검사 (Công tố viên quân đội)",
                    "correction": "군검찰 (Viện kiểm sát quân sự)",
                    "explanation": "'군 검사'는 개인을 지칭하고 '군검찰'은 기관을 의미합니다. 기관명은 Viện kiểm sát quân sự로 표현합니다."
                },
                {
                    "mistake": "군 수사대 (Đội điều tra quân sự)",
                    "correction": "군검찰 (Viện kiểm sát quân sự)",
                    "explanation": "수사 기관(헌병대 등)과 기소 기관(군검찰)은 다릅니다. 군검찰은 기소를 담당하는 검찰 기관입니다."
                },
                {
                    "mistake": "군사검찰청 (Viện công tố quân sự)",
                    "correction": "군검찰 (Viện kiểm sát quân sự)",
                    "explanation": "베트남에서는 'Viện kiểm sát'이 공식 명칭입니다. 'Viện công tố'는 사용하지 않습니다."
                }
            ],
            "examples": [
                {
                    "ko": "군검찰은 탈영병에 대한 구속영장을 청구했습니다.",
                    "vi": "Viện kiểm sát quân sự đã đề nghị lệnh bắt giam binh lính đào ngũ.",
                    "situation": "formal"
                },
                {
                    "ko": "군검찰의 수사 결과 군사기밀 유출 혐의가 확인되었습니다.",
                    "vi": "Kết quả điều tra của Viện kiểm sát quân sự xác nhận nghi vấn tiết lộ bí mật quân sự.",
                    "situation": "formal"
                },
                {
                    "ko": "피의자는 군검찰 조사를 받고 있습니다.",
                    "vi": "Nghi phạm đang bị Viện kiểm sát quân sự điều tra.",
                    "situation": "formal"
                }
            ],
            "relatedTerms": ["군사법원", "군법무관", "헌병대", "군형법"]
        },
        {
            "slug": "toi-khong-tuan-lenh",
            "korean": "항명죄",
            "vietnamese": "Tội không tuân lệnh",
            "hanja": "抗命罪",
            "hanjaReading": "抗(거스를 항) + 命(목숨 명) + 罪(허물 죄)",
            "pronunciation": "또이콩뚜언렌",
            "meaningKo": "항명죄는 군인이 상관의 정당한 직무상 명령을 거부하거나 복종하지 않는 범죄입니다. 통역 시 주의할 점은 '항명(抗命)'과 '불복종(不服從)'의 차이를 명확히 해야 하며, 한국 군형법 제44조는 적전이 아닌 경우와 적전인 경우를 구분하여 처벌합니다. 베트남어 'Tội không tuân lệnh'는 명령 불복종을 의미하며, 전시(thời chiến)와 평시(thời bình)의 형량이 크게 다릅니다. 통역 시 '정당한 명령(mệnh lệnh chính đáng)'인지 여부가 핵심이며, 상관의 불법 명령을 거부하는 것은 항명죄가 아님을 설명해야 합니다. 또한 '명령 거부(từ chối mệnh lệnh)'와 '명령 불이행(không thực hiện mệnh lệnh)'의 차이도 통역 시 구분해야 합니다.",
            "meaningVi": "Tội không tuân lệnh là hành vi quân nhân từ chối hoặc không tuân theo mệnh lệnh chính đáng của cấp trên trong nhiệm vụ. Pháp luật quân sự phân biệt rõ giữa thời bình và thời chiến, với mức hình phạt khác nhau. Mệnh lệnh bất hợp pháp của cấp trên có thể được từ chối mà không bị coi là tội không tuân lệnh.",
            "context": "군 징계, 군사재판, 명령 체계 위반 사건 설명 시 사용",
            "culturalNote": "한국 군대는 계급과 명령 체계가 매우 엄격하며, 항명죄는 군기 해이의 상징으로 여겨집니다. 그러나 2000년대 이후 '정당한 명령'의 범위가 법적으로 명확해지면서, 불법 명령 거부는 항명죄가 아니라는 판례가 확립되었습니다. 베트남 군대도 유사하게 엄격한 명령 체계를 가지지만, 정치 교육과 당 조직의 역할이 강해 명령 불복종은 단순 군기 위반이 아닌 '혁명 정신 결여'로 해석될 수 있습니다. 통역 시 한국의 '정당한 명령' 개념과 베트남의 '혁명적 명령 준수' 개념의 뉘앙스 차이를 이해하고 전달해야 합니다. 또한 한국은 군인권센터 등 민간 감시 기구가 있어 항명죄 적용이 제한적이지만, 베트남은 군 내부 통제가 주를 이룹니다.",
            "commonMistakes": [
                {
                    "mistake": "명령 거부죄 (Tội từ chối mệnh lệnh)",
                    "correction": "항명죄 (Tội không tuân lệnh)",
                    "explanation": "'거부'는 명시적 반대를 의미하지만 '항명'은 복종하지 않는 행위 전반을 포함합니다. 법률 용어는 'Tội không tuân lệnh'가 정확합니다."
                },
                {
                    "mistake": "상관 모욕죄 (Tội xúc phạm cấp trên)",
                    "correction": "항명죄 (Tội không tuân lệnh)",
                    "explanation": "상관 모욕죄는 별도 죄목이며, 항명죄는 명령 불복종에 한정됩니다."
                },
                {
                    "mistake": "불복종 (Không phục t종)",
                    "correction": "항명죄 (Tội không tuân lệnh)",
                    "explanation": "'불복종'은 일반적 표현이고 '항명죄'는 법률 용어입니다. 공식 문서에서는 'Tội không tuân lệnh'를 사용해야 합니다."
                }
            ],
            "examples": [
                {
                    "ko": "상관의 명령을 세 차례 거부하여 항명죄로 기소되었습니다.",
                    "vi": "Đã bị truy tố tội không tuân lệnh vì từ chối mệnh lệnh của cấp trên ba lần.",
                    "situation": "formal"
                },
                {
                    "ko": "정당한 명령이 아니라면 항명죄가 성립하지 않습니다.",
                    "vi": "Nếu không phải là mệnh lệnh chính đáng thì không cấu thành tội không tuân lệnh.",
                    "situation": "formal"
                },
                {
                    "ko": "적전 항명은 사형에 처해질 수 있습니다.",
                    "vi": "Không tuân lệnh trước địch có thể bị xử tử hình.",
                    "situation": "formal"
                }
            ],
            "relatedTerms": ["상관모욕죄", "군기위반", "군사법원", "군형법"]
        },
        {
            "slug": "toi-dao-ngu",
            "korean": "탈영죄",
            "vietnamese": "Tội đào ngũ",
            "hanja": "脫營罪",
            "hanjaReading": "脫(벗을 탈) + 營(진영 영) + 罪(허물 죄)",
            "pronunciation": "또이다오응으",
            "meaningKo": "탈영죄는 군인이 허가 없이 부대를 이탈하여 복귀하지 않는 범죄입니다. 통역 시 주의할 점은 한국 군형법에서 '탈영'은 24시간 이상 무단 이탈을 의미하며, 24시간 미만은 '무단이탈(군무이탈)'로 구분됩니다. 베트남어 'Tội đào ngũ'는 부대 탈출, 도주를 뜻하며, 시간 기준보다는 '복귀 의사 없이 부대를 떠나는 행위'로 해석됩니다. 통역 시 '무단결근(vắng mặt không phép)'과 '탈영(đào ngũ)'의 차이, 그리고 '귀가 후 복귀하지 않음(không trở lại sau khi về nhà)'과 '부대 이탈 후 숨어 지냄(trốn sau khi rời đơn vị)'의 뉘앙스 차이를 명확히 전달해야 합니다. 또한 북한군 탈북자의 경우 한국에서는 '탈영'이 아닌 '귀순'으로 표현하는 점도 유의해야 합니다.",
            "meaningVi": "Tội đào ngũ là hành vi quân nhân rời khỏi đơn vị mà không có sự cho phép và không có ý định trở lại. Khác với vắng mặt ngắn hạn, đào ngũ thể hiện ý định từ bỏ nghĩa vụ quân sự một cách lâu dài hoặc vĩnh viễn.",
            "context": "군 징계, 군사재판, 병역 의무 위반 사건 설명 시 사용",
            "culturalNote": "한국에서 탈영은 매우 중대한 범죄로 간주되며, 특히 1990년대 이전에는 엄벌되었습니다. 그러나 최근에는 군 복무 환경 개선과 함께 탈영자에 대한 사회적 시각이 다소 유연해졌으며, 정신질환이나 군내 폭력이 원인인 경우 감형되기도 합니다. 베트남은 징병제 국가로 탈영을 '혁명 의무 포기'로 간주하여 매우 엄격하게 처벌하며, 가족에게도 사회적 불이익이 있을 수 있습니다. 통역 시 한국의 탈영은 '개인 문제'로 다루어지지만 베트남은 '사회주의 의무 위반'으로 해석될 수 있음을 이해해야 합니다. 또한 한국은 탈영자 복귀 시 자수 감경 제도가 있지만, 베트남은 이러한 제도가 제한적입니다.",
            "commonMistakes": [
                {
                    "mistake": "무단이탈 (Vắng mặt không phép)",
                    "correction": "탈영 (Đào ngũ)",
                    "explanation": "무단이탈은 24시간 미만, 탈영은 24시간 이상 부재를 의미합니다. 'Đào ngũ'는 장기 부재와 복귀 의사 없음을 전제합니다."
                },
                {
                    "mistake": "부대 이탈 (Rời khỏi đơn vị)",
                    "correction": "탈영 (Đào ngũ)",
                    "explanation": "'부대 이탈'은 일반적 표현이고 '탈영'은 범죄 구성 요건을 갖춘 법률 용어입니다."
                },
                {
                    "mistake": "도망 (Chạy trốn)",
                    "correction": "탈영 (Đào ngũ)",
                    "explanation": "'도망'은 비공식적 표현이며 법률 문서에서는 'Đào ngũ'를 사용해야 합니다."
                }
            ],
            "examples": [
                {
                    "ko": "탈영병은 3개월 만에 헌병대에 체포되었습니다.",
                    "vi": "Binh lính đào ngũ đã bị Hiến binh bắt giữ sau 3 tháng.",
                    "situation": "formal"
                },
                {
                    "ko": "가족 문제로 탈영한 경우 정상참작이 가능합니다.",
                    "vi": "Trường hợp đào ngũ vì vấn đề gia đình có thể được xem xét giảm nhẹ.",
                    "situation": "formal"
                },
                {
                    "ko": "탈영 기간이 6개월 이상이면 가중 처벌됩니다.",
                    "vi": "Nếu thời gian đào ngũ trên 6 tháng sẽ bị tăng hình phạt.",
                    "situation": "formal"
                }
            ],
            "relatedTerms": ["무단이탈", "군무이탈", "귀순", "군형법"]
        },
        {
            "slug": "roi-khoi-nhiem-vu",
            "korean": "군무이탈",
            "vietnamese": "Rời khỏi nhiệm vụ",
            "hanja": "軍務離脫",
            "hanjaReading": "軍(군사 군) + 務(힘쓸 무) + 離(떠날 리) + 脫(벗을 탈)",
            "pronunciation": "로이코이니엠붓",
            "meaningKo": "군무이탈은 군인이 정당한 사유 없이 부대나 직무를 이탈한 행위를 의미하며, 탈영죄보다 경미한 범죄입니다. 통역 시 주의할 점은 한국 군형법에서 '군무이탈'은 24시간 미만의 무단 이탈을 의미하며, 24시간 이상이면 '탈영'으로 처벌이 가중됩니다. 베트남어로는 'Rời khỏi nhiệm vụ' (직무 이탈) 또는 'Vắng mặt không phép' (무단 결근)로 표현하며, 시간 기준보다는 '복귀 의사'가 있는지 여부가 중요합니다. 통역 시 '잠깐 자리를 비움(vắng mặt tạm thời)'과 '의도적 이탈(cố ý rời khỏi)'의 차이, 그리고 '근무 중 이탈'과 '휴가 후 미복귀'의 구분을 명확히 해야 합니다. 또한 '보초 근무 중 이탈'은 더 중한 죄로 다뤄지므로 상황 설명이 필수입니다.",
            "meaningVi": "Rời khỏi nhiệm vụ là hành vi quân nhân rời khỏi đơn vị hoặc vị trí công tác mà không có lý do chính đáng, nhưng vẫn có ý định trở lại. Khác với đào ngũ (tội nặng hơn), hành vi này thường kéo dài dưới 24 giờ và không thể hiện ý định từ bỏ nghĩa vụ quân sự.",
            "context": "군 징계, 근무 태만, 군기 위반 사건 설명 시 사용",
            "culturalNote": "한국 군대에서 군무이탈은 비교적 흔한 군기 위반 사례로, 주로 외출·외박 시간 초과, 근무 중 무단 이탈 등이 해당됩니다. 과거에는 엄격히 처벌했으나, 최근에는 초범이거나 경미한 경우 징계로 마무리되는 경우가 많습니다. 베트남 군대는 규율이 매우 엄격하여 짧은 무단 이탈도 정치 교육 대상이 될 수 있으며, '당의 명령 불복종'으로 해석될 위험이 있습니다. 통역 시 한국의 군무이탈은 '실수나 개인 사정'으로 이해되지만, 베트남은 '규율 의식 부족'으로 간주될 수 있음을 유의해야 합니다. 또한 한국은 군무이탈 시 복귀하면 감경되지만, 베트남은 복귀 후에도 정치 교육이나 징계가 따릅니다.",
            "commonMistakes": [
                {
                    "mistake": "탈영 (Đào ngũ)",
                    "correction": "군무이탈 (Rời khỏi nhiệm vụ)",
                    "explanation": "군무이탈은 24시간 미만, 탈영은 24시간 이상 부재를 의미합니다. 'Rời khỏi nhiệm vụ'는 일시적 이탈을 뜻합니다."
                },
                {
                    "mistake": "직무 유기 (Bỏ nhiệm vụ)",
                    "correction": "군무이탈 (Rời khỏi nhiệm vụ)",
                    "explanation": "'직무 유기'는 의도적으로 업무를 방기하는 것이고 '군무이탈'은 물리적 이탈을 의미합니다."
                },
                {
                    "mistake": "무단결근 (Vắng mặt không phép)",
                    "correction": "군무이탈 (Rời khỏi nhiệm vụ)",
                    "explanation": "'무단결근'은 근무 시작 전 출근하지 않은 것이고 '군무이탈'은 근무 중 이탈한 것입니다."
                }
            ],
            "examples": [
                {
                    "ko": "외출 시간을 3시간 초과하여 군무이탈로 징계받았습니다.",
                    "vi": "Đã bị kỷ luật vì rời khỏi nhiệm vụ do quá giờ ra ngoài 3 tiếng.",
                    "situation": "formal"
                },
                {
                    "ko": "보초 근무 중 자리를 비운 것은 중대한 군무이탈입니다.",
                    "vi": "Rời khỏi vị trí trong khi làm nhiệm vụ canh gác là hành vi rời nhiệm vụ nghiêm trọng.",
                    "situation": "formal"
                },
                {
                    "ko": "군무이탈 시간이 24시간을 넘으면 탈영죄로 전환됩니다.",
                    "vi": "Nếu thời gian rời khỏi nhiệm vụ vượt quá 24 giờ sẽ chuyển thành tội đào ngũ.",
                    "situation": "formal"
                }
            ],
            "relatedTerms": ["탈영죄", "무단결근", "직무유기", "군형법"]
        },
        {
            "slug": "tan-cong-linh-gac",
            "korean": "초병폭행",
            "vietnamese": "Tấn công lính gác",
            "hanja": "哨兵暴行",
            "hanjaReading": "哨(파수 초) + 兵(군사 병) + 暴(사나울 폭) + 行(다닐 행)",
            "pronunciation": "떤꽁린각",
            "meaningKo": "초병폭행은 보초 근무 중인 군인을 폭행하는 범죄로, 군기 확립과 경계 임무 보호를 위해 가중 처벌됩니다. 통역 시 주의할 점은 '초병(哨兵)'은 보초 근무 중인 군인을 의미하며, 베트남어 'Lính gác'는 경비병, 보초를 뜻합니다. 한국 군형법에서는 초병 폭행을 일반 폭행보다 무겁게 처벌하며, 특히 적전이나 경계 근무 중인 초병을 폭행하면 최고 사형까지 가능합니다. 통역 시 '보초(lính gác)', '경비병(lính canh)', '헌병(hiến binh)'의 차이를 구분해야 하며, '폭행(tấn công, đánh đập)'과 '협박(đe dọa)'의 경중도 명확히 전달해야 합니다. 또한 '초병 살해(giết lính gác)'는 별도의 더 중한 죄목임을 설명해야 합니다.",
            "meaningVi": "Tấn công lính gác là hành vi hành hung quân nhân đang làm nhiệm vụ canh gác, bị xử phạt nặng hơn hành hung thông thường để bảo vệ kỷ luật quân đội và nhiệm vụ cảnh giới. Đặc biệt, nếu tấn công lính gác trong thời chiến hoặc khi đang làm nhiệm vụ cảnh giới, có thể bị xử tử hình.",
            "context": "군사재판, 군기 위반, 폭력 사건 설명 시 사용",
            "culturalNote": "한국 군대에서 초병은 부대 경계의 최전선에서 근무하는 군인으로, 초병 폭행은 부대 안전을 위협하는 중대 범죄로 간주됩니다. 과거 군부대 총기 난사 사건이나 탈영 시도 시 초병이 피해를 입는 경우가 있어, 초병 보호는 매우 중요한 군기 사항입니다. 베트남 군대도 유사하게 경계 근무를 중시하며, 특히 국경 지대나 중요 시설 경비 중인 'Lính gác'는 국가 안보 최전선으로 인식되어 폭행 시 엄벌됩니다. 통역 시 한국의 초병은 '부대 경계'를 주로 담당하지만 베트남의 'Lính gác'는 '국경 수비'나 '주요 시설 보호'까지 포함하는 넓은 개념임을 이해해야 합니다. 또한 한국은 초병 폭행 시 군사법원 처리가 원칙이지만, 베트남은 군검찰과 군사법원이 함께 신속히 처리합니다.",
            "commonMistakes": [
                {
                    "mistake": "경비병 폭행 (Tấn công lính canh)",
                    "correction": "초병 폭행 (Tấn công lính gác)",
                    "explanation": "'경비병'은 일반 경비 임무를 의미하고 '초병'은 경계 근무 중인 보초를 의미합니다. 법률 용어는 'Lính gác'입니다."
                },
                {
                    "mistake": "헌병 폭행 (Tấn công hiến binh)",
                    "correction": "초병 폭행 (Tấn công lính gác)",
                    "explanation": "헌병은 군사경찰로 다른 직무입니다. 초병은 보초 근무 중인 병사를 의미합니다."
                },
                {
                    "mistake": "보초 공격 (Tấn công lính bảo vệ)",
                    "correction": "초병 폭행 (Tấn công lính gác)",
                    "explanation": "'보초 공격'은 직역이고 법률 용어는 'Tấn công lính gác'입니다."
                }
            ],
            "examples": [
                {
                    "ko": "야간 근무 중인 초병을 폭행한 혐의로 기소되었습니다.",
                    "vi": "Đã bị truy tố tội tấn công lính gác đang làm nhiệm vụ ban đêm.",
                    "situation": "formal"
                },
                {
                    "ko": "초병 폭행은 일반 폭행보다 형량이 2배 이상 무겁습니다.",
                    "vi": "Hình phạt tấn công lính gác nặng hơn hành hung thông thường gấp 2 lần trở lên.",
                    "situation": "formal"
                },
                {
                    "ko": "적전에서 초병을 살해하면 사형에 처해질 수 있습니다.",
                    "vi": "Giết lính gác trước địch có thể bị xử tử hình.",
                    "situation": "formal"
                }
            ],
            "relatedTerms": ["항명죄", "군형법", "보초근무", "군사법원"]
        },
        {
            "slug": "xuc-pham-cap-tren",
            "korean": "상관모욕",
            "vietnamese": "Xúc phạm cấp trên",
            "hanja": "上官侮辱",
            "hanjaReading": "上(위 상) + 官(벼슬 관) + 侮(업신여길 모) + 辱(욕될 욕)",
            "pronunciation": "쑥팜껍쩐",
            "meaningKo": "상관모욕은 군인이 상관의 명예를 훼손하거나 모욕하는 범죄로, 군 계급 질서와 명령 체계를 보호하기 위한 죄목입니다. 통역 시 주의할 점은 한국 군형법 제64조는 '공연히 또는 여러 사람 앞에서 상관을 모욕'하는 경우를 처벌하며, 단순히 사적으로 욕설을 한 것은 해당하지 않습니다. 베트남어 'Xúc phạm cấp trên'은 상급자 모욕을 의미하며, '공개적(công khai)'인지 여부가 중요합니다. 통역 시 '모욕(xúc phạm)', '명예훼손(phỉ báng)', '폭언(lăng mạ)'의 차이를 구분해야 하며, '사실 적시(nêu sự thật)'와 '허위 사실 유포(lan truyền sự việc giả mạo)'의 법적 의미도 명확히 전달해야 합니다. 또한 '상관(cấp trên)'의 범위는 직속 상관뿐 아니라 계급이 높은 모든 상급자를 포함함을 설명해야 합니다.",
            "meaningVi": "Xúc phạm cấp trên là hành vi quân nhân xúc phạm danh dự hoặc nhân phẩm của cấp trên, nhằm bảo vệ trật tự cấp bậc và hệ thống mệnh lệnh trong quân đội. Pháp luật quân sự chỉ xử phạt khi hành vi được thực hiện công khai hoặc trước mặt nhiều người, không áp dụng cho lời nói riêng tư.",
            "context": "군사재판, 군 징계, 명예훼손 사건 설명 시 사용",
            "culturalNote": "한국 군대는 엄격한 계급 사회로, 상관 모욕은 군기 해이의 대표적 사례로 여겨집니다. 그러나 2000년대 이후 군인권 인식이 높아지면서 '정당한 비판'과 '모욕'의 경계가 법적으로 논의되고 있으며, 상관의 불법 행위를 지적하는 것은 모욕죄가 아니라는 판례가 나오고 있습니다. 베트남 군대는 정치 교육과 당 조직이 강하여 상관 모욕은 단순 군기 위반이 아닌 '혁명 정신 부족'으로 해석될 수 있으며, 정치 교육이나 당 징계가 병행됩니다. 통역 시 한국의 '상관 모욕'은 법률적 문제이지만, 베트남은 '정치·도덕적 문제'로도 다뤄질 수 있음을 이해해야 합니다. 또한 한국은 상관 모욕 시 군사법원 처리가 원칙이지만, 베트남은 당 위원회 징계가 선행되는 경우가 많습니다.",
            "commonMistakes": [
                {
                    "mistake": "상관 폭행 (Tấn công cấp trên)",
                    "correction": "상관 모욕 (Xúc phạm cấp trên)",
                    "explanation": "폭행은 물리적 공격이고 모욕은 언어적 공격입니다. 'Xúc phạm'는 명예 훼손을 의미합니다."
                },
                {
                    "mistake": "상급자 비방 (Phỉ báng cấp trên)",
                    "correction": "상관 모욕 (Xúc phạm cấp trên)",
                    "explanation": "'비방'은 허위 사실 유포이고 '모욕'은 경멸 표현입니다. 법률 용어는 'Xúc phạm'입니다."
                },
                {
                    "mistake": "상관 욕설 (Chửi bới cấp trên)",
                    "correction": "상관 모욕 (Xúc phạm cấp trên)",
                    "explanation": "'욕설'은 구어체이고 법률 문서에서는 'Xúc phạm cấp trên'을 사용합니다."
                }
            ],
            "examples": [
                {
                    "ko": "여러 병사 앞에서 중대장을 모욕하여 징계위원회에 회부되었습니다.",
                    "vi": "Đã bị đưa ra hội đồng kỷ luật vì xúc phạm trung đội trưởng trước mặt nhiều chiến sĩ.",
                    "situation": "formal"
                },
                {
                    "ko": "상관 모욕은 공연성이 인정되어야 성립합니다.",
                    "vi": "Xúc phạm cấp trên chỉ được xác lập khi có tính công khai.",
                    "situation": "formal"
                },
                {
                    "ko": "정당한 비판은 상관 모욕으로 처벌받지 않습니다.",
                    "vi": "Phê bình chính đáng không bị xử phạt như xúc phạm cấp trên.",
                    "situation": "formal"
                }
            ],
            "relatedTerms": ["항명죄", "명예훼손", "군기위반", "군형법"]
        },
        {
            "slug": "tiet-lo-bi-mat-quan-su",
            "korean": "군사기밀누설",
            "vietnamese": "Tiết lộ bí mật quân sự",
            "hanja": "軍事機密漏泄",
            "hanjaReading": "軍(군사 군) + 事(일 사) + 機(틀 기) + 密(빽빽할 밀) + 漏(샐 루) + 泄(샐 설)",
            "pronunciation": "띠엣로비맏꾸언쓰",
            "meaningKo": "군사기밀누설은 군사상 기밀 정보를 허가 없이 누설하는 범죄로, 국가 안보를 위협하는 중대 범죄입니다. 통역 시 주의할 점은 한국 군형법 제81조는 '군사기밀'을 '적국이나 외국에 누설'하는 경우와 '일반에 누설'하는 경우로 구분하며, 적국에 누설하면 사형까지 가능합니다. 베트남어 'Tiết lộ bí mật quân sự'는 군사 기밀 유출을 의미하며, '국가 기밀(bí mật quốc gia)'과 '군사 기밀(bí mật quân sự)'의 구분이 중요합니다. 통역 시 '기밀(bí mật)', '비밀(bí mật)', '대외비(nội bộ)' 등급의 차이를 명확히 전달해야 하며, '누설(tiết lộ)'과 '유출(rò rỉ)', '간첩 행위(gián điệp)'의 법적 의미도 구분해야 합니다. 또한 북한 관련 정보는 자동으로 '1급 기밀'로 분류되는 한국의 특수성도 설명해야 합니다.",
            "meaningVi": "Tiết lộ bí mật quân sự là hành vi tiết lộ thông tin mật quân sự mà không được phép, đe dọa an ninh quốc gia. Pháp luật phân biệt giữa tiết lộ cho nước ngoài hoặc kẻ thù (có thể bị tử hình) và tiết lộ cho công chúng (hình phạt nhẹ hơn).",
            "context": "군사재판, 보안 사고, 간첩 사건 설명 시 사용",
            "culturalNote": "한국은 분단 국가로 군사기밀 보호가 매우 엄격하며, 특히 북한 관련 정보는 최고 수준의 기밀로 관리됩니다. 군사기밀 누설은 간첩죄와 연결될 수 있어 국가보안법 적용 대상이 될 수 있습니다. 또한 최근에는 SNS를 통한 부대 위치 노출, 군사 훈련 사진 게시 등도 군사기밀 누설로 처벌받는 사례가 증가하고 있습니다. 베트남도 사회주의 국가로 군사기밀 보호가 엄격하며, 특히 국경 지대 정보, 군사 시설 위치 등은 절대 기밀로 관리됩니다. 통역 시 한국의 군사기밀은 '북한 관련'이 핵심이지만, 베트남은 '국경 수비'와 '중국 관련'이 민감함을 이해해야 합니다. 또한 한국은 군사기밀 등급이 법률로 명확하지만, 베트남은 당과 군의 내부 규정으로 관리됩니다.",
            "commonMistakes": [
                {
                    "mistake": "군사 정보 유출 (Rò rỉ thông tin quân sự)",
                    "correction": "군사기밀 누설 (Tiết lộ bí mật quân sự)",
                    "explanation": "'정보 유출'은 일반적 표현이고 '기밀 누설'은 법률 용어입니다. 'Bí mật'은 기밀 등급을 의미합니다."
                },
                {
                    "mistake": "간첩 행위 (Hoạt động gián điệp)",
                    "correction": "군사기밀 누설 (Tiết lộ bí mật quân sự)",
                    "explanation": "간첩 행위는 외국을 위해 활동하는 것이고 군사기밀 누설은 정보를 누설하는 행위입니다."
                },
                {
                    "mistake": "보안 위반 (Vi phạm an ninh)",
                    "correction": "군사기밀 누설 (Tiết lộ bí mật quân sự)",
                    "explanation": "'보안 위반'은 넓은 개념이고 '군사기밀 누설'은 구체적 범죄 행위입니다."
                }
            ],
            "examples": [
                {
                    "ko": "부대 배치도를 SNS에 게시하여 군사기밀 누설로 기소되었습니다.",
                    "vi": "Đã bị truy tố tội tiết lộ bí mật quân sự vì đăng sơ đồ bố trí đơn vị lên mạng xã hội.",
                    "situation": "formal"
                },
                {
                    "ko": "적국에 군사기밀을 누설하면 사형에 처해질 수 있습니다.",
                    "vi": "Tiết lộ bí mật quân sự cho kẻ thù có thể bị xử tử hình.",
                    "situation": "formal"
                },
                {
                    "ko": "1급 군사기밀은 대통령 승인 없이 열람할 수 없습니다.",
                    "vi": "Bí mật quân sự cấp 1 không thể được xem mà không có sự phê duyệt của Tổng thống.",
                    "situation": "formal"
                }
            ],
            "relatedTerms": ["간첩죄", "국가보안법", "보안사고", "군형법"]
        },
        {
            "slug": "cong-nghiep-quoc-phong",
            "korean": "방위산업",
            "vietnamese": "Công nghiệp quốc phòng",
            "hanja": "防衛産業",
            "hanjaReading": "防(막을 방) + 衛(지킬 위) + 産(낳을 산) + 業(업 업)",
            "pronunciation": "꽁응이엡꾸옥퐁",
            "meaningKo": "방위산업은 국방에 필요한 무기, 장비, 시스템을 개발·생산하는 산업으로, 국가 안보와 직결된 전략 산업입니다. 통역 시 주의할 점은 한국의 방위산업은 방위사업청이 총괄하며, K-9 자주포, KF-21 전투기 등 첨단 무기 수출국으로 성장했습니다. 베트남어 'Công nghiệp quốc phòng'은 국방 산업을 의미하며, 베트남은 자체 무기 생산보다는 러시아, 중국 등으로부터 수입에 의존하는 구조입니다. 통역 시 '방위산업(công nghiệp quốc phòng)', '군수산업(công nghiệp quân sự)', '무기 제조(sản xuất vũ khí)'의 뉘앙스 차이를 이해해야 하며, '방산 수출(xuất khẩu quốc phòng)'과 '무기 거래(mua bán vũ khí)'의 법적 의미도 구분해야 합니다. 또한 한국의 '방산 비리'는 방위산업 부정부패를 의미하며, 이는 국가 안보를 위협하는 중대 범죄로 간주됩니다.",
            "meaningVi": "Công nghiệp quốc phòng là ngành công nghiệp phát triển và sản xuất vũ khí, trang thiết bị, hệ thống cần thiết cho quốc phòng, là ngành chiến lược gắn trực tiếp với an ninh quốc gia. Hàn Quốc đã phát triển thành nước xuất khẩu vũ khí tiên tiến như pháo tự hành K-9, máy bay chiến đấu KF-21.",
            "context": "방산 계약, 무기 수출입, 국방 예산 설명 시 사용",
            "culturalNote": "한국의 방위산업은 1970년대 박정희 정부의 '자주국방' 정책으로 시작되어 현재는 세계 10위권 방산 수출국으로 성장했습니다. K-방산(K-9 자주포, K-2 전차, KF-21 전투기 등)은 한국의 대표 수출 상품이며, 특히 폴란드, 호주, UAE 등에 대규모 수출 계약을 체결했습니다. 반면 베트남은 자체 방위산업이 제한적이며, 주로 러시아와 중국에서 무기를 수입합니다. 최근 베트남은 방위산업 현대화를 추진 중이지만, 여전히 기술력과 자본이 부족한 상황입니다. 통역 시 한국의 방위산업은 '수출 중심'이고 베트남은 '수입 의존'이라는 차이를 이해해야 합니다. 또한 한국은 방산 비리(뇌물, 납품 비리)가 사회 문제이지만, 베트남은 국가 기밀로 다뤄져 외부에 잘 알려지지 않습니다.",
            "commonMistakes": [
                {
                    "mistake": "군수 산업 (Công nghiệp quân sự)",
                    "correction": "방위산업 (Công nghiệp quốc phòng)",
                    "explanation": "'군수 산업'은 군대 보급품 전반을 의미하고 '방위산업'은 무기 제조에 한정됩니다. 베트남에서는 'Công nghiệp quốc phòng'이 공식 용어입니다."
                },
                {
                    "mistake": "무기 제조업 (Sản xuất vũ khí)",
                    "correction": "방위산업 (Công nghiệp quốc phòng)",
                    "explanation": "'무기 제조업'은 일반적 표현이고 '방위산업'은 국가 전략 산업을 의미합니다."
                },
                {
                    "mistake": "국방 공업 (Công nghiệp quốc phòng)",
                    "correction": "방위산업 (Công nghiệp quốc phòng)",
                    "explanation": "'국방 공업'은 직역이지만 베트남에서는 'Công nghiệp quốc phòng'이 표준 용어입니다."
                }
            ],
            "examples": [
                {
                    "ko": "한국의 방위산업은 K-9 자주포 수출로 큰 성과를 거두었습니다.",
                    "vi": "Công nghiệp quốc phòng Hàn Quốc đã đạt được thành tựu lớn nhờ xuất khẩu pháo tự hành K-9.",
                    "situation": "formal"
                },
                {
                    "ko": "방위산업 비리는 국가 안보를 위협하는 중대 범죄입니다.",
                    "vi": "Tham nhũng trong công nghiệp quốc phòng là tội phạm nghiêm trọng đe dọa an ninh quốc gia.",
                    "situation": "formal"
                },
                {
                    "ko": "방위산업청은 무기 개발과 구매를 총괄합니다.",
                    "vi": "Cơ quan Công nghiệp Quốc phòng tổng quát phát triển và mua sắm vũ khí.",
                    "situation": "formal"
                }
            ],
            "relatedTerms": ["방위사업청", "무기수출", "군수품", "국방예산"]
        },
        {
            "slug": "tu-choi-nghia-vu-quan-su",
            "korean": "병역거부",
            "vietnamese": "Từ chối nghĩa vụ quân sự",
            "hanja": "兵役拒否",
            "hanjaReading": "兵(군사 병) + 役(부릴 역) + 拒(물리칠 거) + 否(아닐 부)",
            "pronunciation": "뜨쬐이응이아붓꾸언쓰",
            "meaningKo": "병역거부는 종교적·양심적 이유로 병역 의무를 거부하는 행위로, 한국에서는 2018년까지 범죄로 처벌되었으나 헌법재판소 결정 이후 대체복무제가 도입되었습니다. 통역 시 주의할 점은 한국의 병역거부는 주로 여호와의 증인 신자들의 종교적 신념에 기반하며, 2020년부터 '대체복무(복무 기간 36개월)'가 인정되어 처벌받지 않게 되었습니다. 베트남어 'Từ chối nghĩa vụ quân sự'는 병역 거부를 의미하지만, 베트남에서는 대체복무 제도가 없으며 병역 거부 시 형사 처벌 대상입니다. 통역 시 '양심적 병역거부(từ chối nghĩa vụ quân sự vì lương tâm)'와 '병역 기피(trốn tránh nghĩa vụ quân sự)'의 차이를 명확히 해야 하며, 한국의 대체복무제는 베트남에 없는 개념임을 설명해야 합니다. 또한 '대체복무(phục vụ thay thế)'는 교정시설 등에서 36개월 근무하는 제도로, 일반 병역보다 긴 기간임을 전달해야 합니다.",
            "meaningVi": "Từ chối nghĩa vụ quân sự là hành vi từ chối thực hiện nghĩa vụ quân sự vì lý do tôn giáo hoặc lương tâm. Tại Hàn Quốc, sau quyết định của Tòa án Hiến pháp năm 2018, chế độ phục vụ thay thế (36 tháng) đã được đưa vào và người từ chối nghĩa vụ quân sự không còn bị xử phạt hình sự. Tuy nhiên, Việt Nam không có chế độ phục vụ thay thế và từ chối nghĩa vụ quân sự vẫn là tội phạm.",
            "context": "병역법, 대체복무, 종교의 자유 논의 시 사용",
            "culturalNote": "한국은 분단 국가로 징병제를 유지하며, 병역 의무는 헌법상 의무입니다. 그러나 2018년 헌법재판소가 '양심적 병역거부'를 인정하면서 대체복무제가 도입되었고, 여호와의 증인 신자들이 주로 이 제도를 이용합니다. 대체복무는 교정시설, 소방서 등에서 36개월(일반 육군 18개월의 2배) 근무하는 형태입니다. 베트남은 사회주의 국가로 병역 의무를 '혁명 의무'로 간주하며, 병역 거부는 인정되지 않습니다. 종교의 자유가 제한적이어서 종교적 이유로 병역을 거부하는 사례 자체가 거의 없습니다. 통역 시 한국의 병역거부는 '인권과 양심의 자유' 차원에서 논의되지만, 베트남에서는 '국가 의무 위반'으로만 해석될 수 있음을 유의해야 합니다. 또한 한국의 대체복무제는 '처벌이 아닌 권리'이지만, 복무 기간이 2배라는 점에서 논란이 있습니다.",
            "commonMistakes": [
                {
                    "mistake": "병역 기피 (Trốn tránh nghĩa vụ quân sự)",
                    "correction": "병역 거부 (Từ chối nghĩa vụ quân sự)",
                    "explanation": "'병역 기피'는 도피나 회피를 의미하고 '병역 거부'는 양심적 거부를 의미합니다. 'Từ chối'는 명시적 거부입니다."
                },
                {
                    "mistake": "입대 거부 (Từ chối nhập ngũ)",
                    "correction": "병역 거부 (Từ chối nghĩa vụ quân sự)",
                    "explanation": "'입대 거부'는 입대만 거부하는 것이고 '병역 거부'는 병역 의무 전체를 거부하는 것입니다."
                },
                {
                    "mistake": "군 복무 거부 (Từ chối phục vụ quân đội)",
                    "correction": "병역 거부 (Từ chối nghĩa vụ quân sự)",
                    "explanation": "'군 복무 거부'는 일반적 표현이고 '병역 거부'는 법률 용어입니다."
                }
            ],
            "examples": [
                {
                    "ko": "종교적 신념을 이유로 병역을 거부하고 대체복무를 신청했습니다.",
                    "vi": "Đã từ chối nghĩa vụ quân sự vì tín ngưỡng tôn giáo và nộp đơn xin phục vụ thay thế.",
                    "situation": "formal"
                },
                {
                    "ko": "병역 거부자는 36개월간 교정시설에서 대체복무를 합니다.",
                    "vi": "Người từ chối nghĩa vụ quân sự thực hiện phục vụ thay thế tại cơ sở cải huấn trong 36 tháng.",
                    "situation": "formal"
                },
                {
                    "ko": "2018년 이전에는 병역 거부자가 징역형을 받았습니다.",
                    "vi": "Trước năm 2018, người từ chối nghĩa vụ quân sự bị kết án tù.",
                    "situation": "formal"
                }
            ],
            "relatedTerms": ["대체복무", "징병제", "병역법", "양심의자유"]
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
