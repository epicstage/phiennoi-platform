#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
교육법 (Education Law) 전문용어 추가 스크립트
Tier S 품질 기준 (90점+) 준수
"""

import json
import os
from datetime import datetime

def add_education_law_terms():
    """교육법 관련 10개 용어를 legal.json에 추가"""

    # 파일 경로 설정
    file_path = os.path.join(
        os.path.dirname(os.path.abspath(__file__)),
        '..', 'data', 'terms', 'legal.json'
    )

    # 기존 데이터 로드
    with open(file_path, 'r', encoding='utf-8') as f:
        data = json.load(f)  # List 형식

    # 기존 slug 목록 (중복 방지)
    existing_slugs = {term['slug'] for term in data}

    # 새 용어 정의
    new_terms = [
        {
            "slug": "luat-giao-duc",
            "korean": "교육법",
            "vietnamese": "Luật Giáo dục",
            "hanja": "教育法",
            "hanjaReading": "教(가르칠 교) + 育(기를 육) + 法(법 법)",
            "pronunciation": "루엇 자오 쭉",
            "meaningKo": "교육 제도, 교육 기관의 설립 및 운영, 교육자와 학습자의 권리와 의무 등을 규정한 법률입니다. 한국의 교육기본법과 초중등교육법, 고등교육법 등이 이에 해당하며, 베트남에서는 Luật Giáo dục이 통합적으로 규율합니다. 통역 시 주의할 점은 한국은 교육 단계별로 법률이 분리되어 있지만, 베트남은 단일 교육법 체계라는 점을 명확히 설명해야 합니다. 또한 '교육과정'과 '교육법'을 혼동하지 않도록 chương trình giáo dục(교육과정)과 구분하여 통역해야 합니다.",
            "meaningVi": "Luật quy định về hệ thống giáo dục, thành lập và hoạt động của cơ sở giáo dục, quyền và nghĩa vụ của người dạy và người học. Ở Việt Nam, Luật Giáo dục là văn bản pháp luật tổng hợp, trong khi Hàn Quốc có nhiều đạo luật riêng biệt theo cấp học (giáo dục phổ thông, đại học).",
            "context": "법률 문서, 교육 정책 논의, 교육 기관 설립 인허가, 교육 개혁 회의에서 사용",
            "culturalNote": "한국의 교육법 체계는 교육기본법을 상위법으로 하여 초중등교육법, 고등교육법, 평생교육법 등이 단계별로 세분화되어 있습니다. 반면 베트남은 Luật Giáo dục 하나로 유치원부터 대학까지 통합 규율하며, 2019년 개정법이 현재 시행 중입니다. 통역 시 한국 측이 '초중등교육법'이라고 할 때 베트남에는 대응되는 별도 법률이 없으므로 'quy định về giáo dục phổ thông trong Luật Giáo dục'(교육법 내 보통교육 규정)으로 풀어서 설명해야 오해를 방지할 수 있습니다.",
            "commonMistakes": [
                {
                    "mistake": "교육법을 Luật giáo trình으로 번역",
                    "correction": "Luật Giáo dục",
                    "explanation": "giáo trình은 '교재'를 의미하므로 완전히 다른 뜻입니다. 법률명은 반드시 공식 명칭을 사용해야 합니다."
                },
                {
                    "mistake": "한국의 교육기본법을 Luật Giáo dục으로 직역",
                    "correction": "Luật Giáo dục cơ bản của Hàn Quốc 또는 설명 추가",
                    "explanation": "베트남 Luật Giáo dục과 혼동될 수 있으므로 '한국의'를 명시하거나 체계 차이를 설명해야 합니다."
                },
                {
                    "mistake": "교육법 개정을 sửa đổi giáo dục으로 표현",
                    "correction": "sửa đổi Luật Giáo dục",
                    "explanation": "법률 개정은 반드시 'Luật'를 포함해야 하며, 'giáo dục'만으로는 교육 전반의 수정으로 오해될 수 있습니다."
                }
            ],
            "examples": [
                {
                    "ko": "교육법 제15조에 따라 학교법인의 설립 인가를 신청합니다.",
                    "vi": "Theo Điều 15 Luật Giáo dục, chúng tôi nộp đơn xin cấp phép thành lập pháp nhân trường học.",
                    "situation": "formal"
                },
                {
                    "ko": "이번 교육법 개정안은 학생 인권 보호를 강화하는 내용을 담고 있습니다.",
                    "vi": "Dự thảo sửa đổi Luật Giáo dục lần này có nội dung tăng cường bảo vệ quyền con người học sinh.",
                    "situation": "formal"
                },
                {
                    "ko": "교육법상 의무교육 기간은 9년이지만, 실질적으로는 12년까지 확대 논의 중입니다.",
                    "vi": "Theo Luật Giáo dục, thời gian giáo dục bắt buộc là 9 năm, nhưng đang có thảo luận mở rộng thực tế lên 12 năm.",
                    "situation": "formal"
                }
            ],
            "relatedTerms": ["giao-duc-bat-buoc", "co-so-giao-duc", "quyen-hoc-tap"]
        },
        {
            "slug": "co-so-giao-duc",
            "korean": "교육기관",
            "vietnamese": "Cơ sở giáo dục",
            "hanja": "教育機關",
            "hanjaReading": "教(가르칠 교) + 育(기를 육) + 機(틀 기) + 關(관계할 관)",
            "pronunciation": "꺼 서 자오 쭉",
            "meaningKo": "교육 활동을 수행하는 기관으로, 유치원, 초·중·고등학교, 대학교, 직업훈련원 등을 포괄하는 법적 용어입니다. 베트남어로는 'cơ sở giáo dục'이며, 한국의 '학교'(trường học)보다 넓은 개념입니다. 통역 시 주의할 점은 한국에서 '교육기관'이라고 하면 학원이나 평생교육시설도 포함될 수 있지만, 베트남 법률상 cơ sở giáo dục은 정규 교육 시스템 내 기관만을 지칭하므로, 사설 학원은 'trung tâm đào tạo'(교육센터)로 구분하여 통역해야 합니다. 또한 '비인가 교육기관'은 cơ sở giáo dục không được phép이 아니라 'cơ sở đào tạo chưa được cấp phép'로 표현해야 법적으로 정확합니다.",
            "meaningVi": "Các tổ chức thực hiện hoạt động giáo dục, bao gồm nhà trẻ, mẫu giáo, trường phổ thông, đại học, trung tâm dạy nghề. Khái niệm pháp lý rộng hơn 'trường học', bao gồm cả các hình thức giáo dục không chính quy có giấy phép.",
            "context": "교육법, 인허가 서류, 교육 행정, 학교 설립 및 폐쇄 절차에서 사용",
            "culturalNote": "한국에서는 '교육기관'을 학교와 거의 동일하게 사용하지만, 베트남에서는 cơ sở giáo dục이 법적으로 명확히 정의된 용어입니다. 베트남 교육법에 따르면 cơ sở giáo dục은 ①mầm non(유아교육), ②phổ thông(보통교육), ③đại học(대학), ④dạy nghề(직업교육) 4가지로 분류됩니다. 한국의 학원, 교습소 등은 베트남에서 trung tâm ngoại ngữ(외국어센터), trung tâm kỹ năng(기술센터) 등으로 불리며 cơ sở giáo dục에 포함되지 않습니다. 통역 시 이 차이를 명확히 하지 않으면 법적 분쟁의 소지가 있습니다.",
            "commonMistakes": [
                {
                    "mistake": "교육기관을 trường học으로 통역",
                    "correction": "cơ sở giáo dục",
                    "explanation": "trường học은 '학교'를 의미하며 좁은 개념입니다. 법률 문서에서는 반드시 공식 용어를 사용해야 합니다."
                },
                {
                    "mistake": "학원을 cơ sở giáo dục으로 번역",
                    "correction": "trung tâm đào tạo 또는 trung tâm học thêm",
                    "explanation": "한국의 사설 학원은 베트남 법상 cơ sở giáo dục이 아니므로 구분해야 합니다."
                },
                {
                    "mistake": "교육기관 폐쇄를 đóng cửa cơ sở giáo dục으로 표현",
                    "correction": "đình chỉ hoạt động hoặc thu hồi giấy phép",
                    "explanation": "법적 폐쇄는 '문 닫기'가 아니라 '활동 정지' 또는 '허가 취소'로 표현해야 정확합니다."
                }
            ],
            "examples": [
                {
                    "ko": "이 교육기관은 교육부로부터 정식 인가를 받았습니다.",
                    "vi": "Cơ sở giáo dục này đã được Bộ Giáo dục chính thức cấp phép.",
                    "situation": "formal"
                },
                {
                    "ko": "교육기관의 설립 기준은 교육법 시행령에 명시되어 있습니다.",
                    "vi": "Tiêu chuẩn thành lập cơ sở giáo dục được quy định rõ trong Nghị định thi hành Luật Giáo dục.",
                    "situation": "formal"
                },
                {
                    "ko": "우리 지역에는 외국인 근로자 자녀를 위한 교육기관이 부족합니다.",
                    "vi": "Ở khu vực chúng tôi, thiếu cơ sở giáo dục dành cho con em lao động nước ngoài.",
                    "situation": "formal"
                }
            ],
            "relatedTerms": ["luat-giao-duc", "bang-cap", "tu-chu-dai-hoc"]
        },
        {
            "slug": "hoc-phi",
            "korean": "학비",
            "vietnamese": "Học phí",
            "hanja": "學費",
            "hanjaReading": "學(배울 학) + 費(쓸 비)",
            "pronunciation": "혹 피",
            "meaningKo": "학생이 교육 서비스를 받기 위해 교육기관에 납부하는 금전으로, 등록금, 수업료를 포괄하는 용어입니다. 베트남어로는 'học phí'이며, 한국의 '등록금'(lệ phí đăng ký)보다 넓은 개념입니다. 통역 시 주의할 점은 한국에서 학비는 대학 등록금, 학원비, 교재비 등을 모두 포함할 수 있지만, 베트남 법률상 học phí는 정규 교육과정의 수업료만을 지칭하며, 입학금(lệ phí nhập học), 시험비(lệ phí thi), 교재비(tiền sách)는 별도로 구분됩니다. 또한 '학비 면제'는 miễn học phí, '학비 감면'은 giảm học phí로 명확히 구분하여 통역해야 하며, '학비 지원'은 hỗ trợ học phí 또는 장학금(học bổng)으로 문맥에 따라 선택해야 합니다.",
            "meaningVi": "Khoản tiền học sinh phải nộp cho cơ sở giáo dục để được cung cấp dịch vụ giáo dục. Trong pháp luật Việt Nam, học phí chỉ bao gồm tiền học chính khóa, không bao gồm lệ phí nhập học, thi cử hay tiền sách.",
            "context": "교육 계약서, 학비 납부 안내, 장학금 신청, 학비 분쟁 조정에서 사용",
            "culturalNote": "한국에서는 대학 등록금이 학비의 대표적 개념이며, 학기당 납부가 일반적입니다. 베트남에서는 초중등 공립학교는 학비가 무료(miễn học phí)이며, 사립학교와 대학만 학비를 징수합니다. 베트남의 학비 체계는 한국보다 세분화되어 있어, 예를 들어 ①학비(học phí - 수업료), ②입학금(lệ phí nhập học - 일회성), ③시설비(tiền cơ sở vật chất - 학기마다), ④교재비(tiền sách - 별도) 등으로 나뉩니다. 한국 측이 '학비 전액'이라고 표현할 때, 베트남에서는 'toàn bộ các khoản phí'(모든 비용)로 통역해야 입학금 등이 포함되는지 명확해집니다. 또한 베트남에는 '학비 동결'(đóng băng học phí) 정책이 자주 논의되므로, 이 용어도 숙지해야 합니다.",
            "commonMistakes": [
                {
                    "mistake": "학비를 tiền học으로 번역",
                    "correction": "học phí",
                    "explanation": "tiền học은 구어체이며, 법률 및 공식 문서에서는 반드시 học phí를 사용해야 합니다."
                },
                {
                    "mistake": "등록금을 học phí로만 통역",
                    "correction": "học phí 또는 lệ phí đăng ký học (문맥에 따라)",
                    "explanation": "한국의 '등록금'은 입학금 포함 여부가 불명확하므로, 베트남에서는 학비만 지칭하는지 입학금 포함인지 확인 후 통역해야 합니다."
                },
                {
                    "mistake": "학비 지원을 hỗ trợ tiền học으로 표현",
                    "correction": "hỗ trợ học phí 또는 cấp học bổng",
                    "explanation": "정부나 기관의 공식 지원은 'hỗ trợ học phí', 장학금 형태는 'học bổng'으로 구분해야 합니다."
                }
            ],
            "examples": [
                {
                    "ko": "이 대학의 학비는 학기당 300만 원입니다.",
                    "vi": "Học phí của trường đại học này là 3 triệu won mỗi học kỳ.",
                    "situation": "formal"
                },
                {
                    "ko": "저소득층 학생에게는 학비 전액 면제 혜택이 제공됩니다.",
                    "vi": "Học sinh gia đình có thu nhập thấp được miễn toàn bộ học phí.",
                    "situation": "formal"
                },
                {
                    "ko": "학비 납부 기한은 매 학기 시작 2주 전까지입니다.",
                    "vi": "Hạn nộp học phí là trước 2 tuần khi học kỳ bắt đầu.",
                    "situation": "formal"
                }
            ],
            "relatedTerms": ["co-so-giao-duc", "quyen-hoc-tap", "bang-cap"]
        },
        {
            "slug": "bang-cap",
            "korean": "학위",
            "vietnamese": "Bằng cấp",
            "hanja": "學位",
            "hanjaReading": "學(배울 학) + 位(자리 위)",
            "pronunciation": "방 껍",
            "meaningKo": "일정한 교육과정을 이수하고 학업 성취를 인정받아 수여되는 공식 증서로, 학사, 석사, 박사 학위 등을 포괄합니다. 베트남어로는 'bằng cấp'이며, 졸업장(bằng tốt nghiệp)과 구분됩니다. 통역 시 주의할 점은 한국에서 '학위'는 주로 대학 이상의 학력을 지칭하지만, 베트Nam에서 bằng cấp은 고등학교 졸업장(bằng tốt nghiệp THPT)부터 박사 학위(bằng tiến sĩ)까지 모든 공식 학력 증명서를 포괄하는 넓은 개념입니다. '학위 인정'은 'công nhận bằng cấp', '학위 취소'는 'thu hồi bằng cấp'으로 표현하며, '명예 학위'는 'bằng danh dự'로 구분해야 합니다. 또한 한국의 '전문학사'는 베트남의 'cao đẳng'에 해당하지만 학위 체계가 다르므로 설명이 필요합니다.",
            "meaningVi": "Văn bằng chính thức được cấp sau khi hoàn thành chương trình giáo dục, bao gồm từ bằng tốt nghiệp phổ thông đến tiến sĩ. Trong pháp luật Việt Nam, bằng cấp bao gồm: bằng THPT, bằng trung cấp, bằng cao đẳng, bằng đại học, bằng thạc sĩ, bằng tiến sĩ.",
            "context": "학력 인증, 채용 서류, 학위 인정 신청, 교육 행정에서 사용",
            "culturalNote": "한국의 학위 체계는 전문학사(2~3년) - 학사(4년) - 석사(2년) - 박사(3년 이상)로 구성됩니다. 베트남은 trung cấp(중급, 2년) - cao đẳng(전문대, 2~3년) - đại học(대학, 4~6년) - thạc sĩ(석사, 2년) - tiến sĩ(박사, 3~4년)로 단계가 더 세분화되어 있습니다. 특히 베트Nam의 'trung cấp nghề'(중급직업)는 한국의 특성화고나 마이스터고와 유사하지만 학위로 인정되므로, 한국에서 '고졸'이라고 할 때 베트Nam 측이 bằng THPT인지 bằng trung cấp nghề인지 혼동할 수 있습니다. 또한 베트Nam에서는 외국 학위의 경우 '영사 확인'(xác nhận lãnh sự)과 '학위 동등성 인정'(công nhận tương đương) 절차가 별도로 필요하므로 통역 시 이를 안내해야 합니다.",
            "commonMistakes": [
                {
                    "mistake": "학위를 văn bằng으로 번역",
                    "correction": "bằng cấp",
                    "explanation": "văn bằng은 문서 전반을 지칭하며, 학위는 bằng cấp이 정확합니다. 다만 '학위 증서'는 văn bằng bằng cấp이 맞습니다."
                },
                {
                    "mistake": "졸업장과 학위를 구분 없이 bằng cấp으로 통역",
                    "correction": "졸업장은 bằng tốt nghiệp, 학위는 bằng cấp",
                    "explanation": "베트Nam에서는 졸업장(수료 증명)과 학위(학력 증명)가 구분되므로 문맥에 따라 정확히 사용해야 합니다."
                },
                {
                    "mistake": "한국 전문학사를 bằng trung cấp으로 번역",
                    "correction": "bằng cao đẳng (+ 설명 필요)",
                    "explanation": "trung cấp은 고등학교 수준이며, 한국 전문학사는 cao đẳng이 가장 가깝지만 연수가 다르므로 '2~3년제 전문대학 학위'로 부연 설명이 필요합니다."
                }
            ],
            "examples": [
                {
                    "ko": "이 직무에 지원하려면 학사 학위 이상이 필요합니다.",
                    "vi": "Để ứng tuyển vị trí này, cần có bằng cấp từ đại học trở lên.",
                    "situation": "formal"
                },
                {
                    "ko": "외국에서 취득한 학위는 교육부의 인정을 받아야 합니다.",
                    "vi": "Bằng cấp lấy ở nước ngoài phải được Bộ Giáo dục công nhận.",
                    "situation": "formal"
                },
                {
                    "ko": "그는 서울대학교에서 경제학 박사 학위를 받았습니다.",
                    "vi": "Anh ấy đã nhận bằng tiến sĩ Kinh tế tại Đại học Quốc gia Seoul.",
                    "situation": "formal"
                }
            ],
            "relatedTerms": ["cong-nhan-bang", "co-so-giao-duc", "dao-tao-nghe"]
        },
        {
            "slug": "cong-nhan-bang",
            "korean": "학위인정",
            "vietnamese": "Công nhận bằng",
            "hanja": "學位認定",
            "hanjaReading": "學(배울 학) + 位(자리 위) + 認(알 인) + 定(정할 정)",
            "pronunciation": "꽁 년 방",
            "meaningKo": "외국 또는 비인가 교육기관에서 취득한 학위를 공식적으로 인정하는 행정 절차입니다. 베트Nam어로는 'công nhận bằng' 또는 'công nhận bằng cấp'이며, 교육부 또는 지정 기관이 심사를 통해 학위의 효력을 부여합니다. 통역 시 주의할 점은 한국에서 '학력 인정'과 '학위 인정'을 혼용하지만, 베트Nam에서는 ①công nhận bằng cấp(학위 인정 - 외국 학위), ②công nhận tương đương(동등성 인정 - 학력 수준 비교), ③công nhận tốt nghiệp(졸업 인정 - 국내 비인가 과정) 세 가지로 명확히 구분됩니다. 또한 '사전 학위 인정'은 없으며 반드시 졸업 후 신청해야 하고, 인정 절차에는 '영사 확인'(xác nhận lãnh sự)과 '아포스티유'(Apostille) 중 하나가 필수임을 안내해야 합니다.",
            "meaningVi": "Thủ tục hành chính để cơ quan có thẩm quyền chính thức thừa nhận giá trị pháp lý của bằng cấp lấy ở nước ngoài hoặc cơ sở giáo dục chưa được công nhận. Ở Việt Nam, Bộ Giáo dục và Đào tạo hoặc cơ quan được ủy quyền thực hiện việc công nhận sau khi thẩm định hồ sơ.",
            "context": "외국인 채용, 유학생 관리, 학력 검증, 행정 소송에서 사용",
            "culturalNote": "한국에서는 외국 학위 인정이 비교적 간소하며, 대사관 확인이나 아포스티유 서류만 있으면 대부분 인정됩니다. 베트남에서는 공식적인 학위 인정 절차가 매우 엄격하며, 교육부에 ①학위증 원본, ②성적증명서, ③교육기관 인가 증명, ④영사 확인/아포스티유, ⑤번역 공증본을 제출해야 합니다. 또한 베트남은 '학위 동등성 인정'(công nhận tương đương)이라는 별도 제도가 있어, 예를 들어 한국의 3년제 전문학사를 베트Nam의 4년제 대학 학위와 동등하게 인정받으려면 추가 심사가 필요합니다. 통역 시 한국 측이 '학위만 있으면 되지 않느냐'고 오해하지 않도록, 베트Nam의 복잡한 인정 절차와 소요 기간(보통 3~6개월)을 사전에 안내해야 분쟁을 예방할 수 있습니다.",
            "commonMistakes": [
                {
                    "mistake": "학위 인정을 chấp nhận bằng으로 번역",
                    "correction": "công nhận bằng hoặc công nhận bằng cấp",
                    "explanation": "chấp nhận은 '수락하다'의 의미이며, 공식 행정 절차는 công nhận(인정)입니다."
                },
                {
                    "mistake": "학력 인정과 학위 인정을 구분 없이 công nhận bằng cấp으로 통역",
                    "correction": "학력 인정은 công nhận trình độ, 학위 인정은 công nhận bằng cấp",
                    "explanation": "학력(수준)과 학위(증서)는 베트남 법상 다른 개념이므로 명확히 구분해야 합니다."
                },
                {
                    "mistake": "학위 인정 신청을 nộp đơn xin bằng으로 표현",
                    "correction": "nộp hồ sơ xin công nhận bằng cấp",
                    "explanation": "'xin bằng'은 '학위 발급 신청'으로 오해되며, 인정 신청은 'xin công nhận'이 정확합니다."
                }
            ],
            "examples": [
                {
                    "ko": "귀하의 미국 학위는 한국 교육부의 학위 인정을 받아야 취업이 가능합니다.",
                    "vi": "Bằng cấp Mỹ của quý vị phải được Bộ Giáo dục Hàn Quốc công nhận mới có thể xin việc.",
                    "situation": "formal"
                },
                {
                    "ko": "학위 인정 절차는 통상 3개월에서 6개월이 소요됩니다.",
                    "vi": "Thủ tục công nhận bằng cấp thường mất từ 3 đến 6 tháng.",
                    "situation": "formal"
                },
                {
                    "ko": "온라인으로 취득한 학위도 인정 신청이 가능합니까?",
                    "vi": "Bằng cấp lấy qua hình thức trực tuyến có thể nộp hồ sơ xin công nhận không?",
                    "situation": "formal"
                }
            ],
            "relatedTerms": ["bang-cap", "co-so-giao-duc", "luat-giao-duc"]
        },
        {
            "slug": "tu-chu-dai-hoc",
            "korean": "대학자율",
            "vietnamese": "Tự chủ đại học",
            "hanja": "大學自律",
            "hanjaReading": "大(큰 대) + 學(배울 학) + 自(스스로 자) + 律(법칙 률)",
            "pronunciation": "뜨 쭈 다이 혹",
            "meaningKo": "대학이 정부의 간섭 없이 교육과정, 인사, 재정 등을 독립적으로 결정할 수 있는 권리를 의미합니다. 베트Nam어로는 'tự chủ đại học'이며, 한국의 '대학 자치'와 유사하지만 법적 범위가 다릅니다. 통역 시 주의할 점은 한국에서 대학자율은 주로 학사 운영과 교수 인사를 지칭하지만, 베트Nam에서는 tự chủ đại học이 ①tự chủ học thuật(학술 자율 - 교육과정), ②tự chủ tổ chức(조직 자율 - 인사), ③tự chủ tài chính(재정 자율 - 예산) 세 가지로 명확히 구분되며, 각각 다른 수준의 자율권을 가집니다. 또한 베트Nam은 2012년 고등교육법 개정으로 대학자율을 크게 확대했지만, 여전히 정부 승인이 필요한 사항이 많으므로, '완전 자율'이라는 표현은 오해의 소지가 있습니다.",
            "meaningVi": "Quyền của trường đại học được tự quyết định về chương trình đào tạo, nhân sự, tài chính mà không bị can thiệp của cơ quan nhà nước. Theo Luật Giáo dục đại học Việt Nam (2012, sửa đổi 2018), tự chủ đại học bao gồm ba lĩnh vực: học thuật, tổ chức, tài chính.",
            "context": "대학 정책, 교육 개혁, 대학 평가, 국제 협력 논의에서 사용",
            "culturalNote": "한국의 대학자율은 1990년대 이후 점진적으로 확대되어 현재는 교육과정 편성, 교수 채용, 등록금 책정 등에서 상당한 자율권을 갖고 있습니다. 베트남에서는 2012년 고등교육법으로 대학자율이 법제화되었지만, 실제 운영에서는 여전히 정부 승인과 감독이 많이 남아 있습니다. 예를 들어 베트Nam 대학은 신규 전공 개설 시 교육부 승인이 필요하고, 학비는 정부가 정한 상한선을 초과할 수 없습니다. 반면 한국은 대학이 자율적으로 학과를 신설하고 등록금을 책정할 수 있습니다(물론 등록금 인상률은 물가상승률 제한). 통역 시 한국 측이 '대학자율'을 베트남식으로 오해하지 않도록, 양국의 자율 범위 차이를 명확히 설명해야 합니다. 특히 '자율'(tự chủ)과 '자치'(tự trị)는 베트남어에서 다른 개념이므로 혼동하지 않아야 합니다.",
            "commonMistakes": [
                {
                    "mistake": "대학자율을 tự do đại học으로 번역",
                    "correction": "tự chủ đại học",
                    "explanation": "tự do는 '자유'를 의미하며, 법적 개념인 '자율'은 반드시 tự chủ를 사용해야 합니다."
                },
                {
                    "mistake": "대학 자치와 대학자율을 모두 tự chủ đại học으로 통역",
                    "correction": "대학 자치는 tự trị đại học, 대학자율은 tự chủ đại học",
                    "explanation": "자치(self-governance)와 자율(autonomy)은 베트남어에서 다른 용어로 구분됩니다."
                },
                {
                    "mistake": "완전 대학자율을 tự chủ đại học hoàn toàn으로 표현",
                    "correction": "mức độ tự chủ cao 또는 설명 추가",
                    "explanation": "베트남에서는 '완전 자율'이 존재하지 않으므로, '높은 수준의 자율'로 표현하거나 제한 사항을 설명해야 합니다."
                }
            ],
            "examples": [
                {
                    "ko": "이번 교육법 개정으로 대학자율이 한층 강화되었습니다.",
                    "vi": "Lần sửa đổi Luật Giáo dục này đã tăng cường tự chủ đại học hơn nữa.",
                    "situation": "formal"
                },
                {
                    "ko": "대학자율 확대를 위해 정부의 규제를 대폭 완화할 계획입니다.",
                    "vi": "Để mở rộng tự chủ đại học, chính phủ dự định nới lỏng đáng kể các quy định.",
                    "situation": "formal"
                },
                {
                    "ko": "우리 대학은 재정 자율권을 갖고 있어 독립적으로 예산을 운용합니다.",
                    "vi": "Trường đại học chúng tôi có quyền tự chủ tài chính nên vận hành ngân sách độc lập.",
                    "situation": "formal"
                }
            ],
            "relatedTerms": ["luat-giao-duc", "co-so-giao-duc", "kiem-dinh-chat-luong-giao-duc"]
        },
        {
            "slug": "quyen-hoc-tap",
            "korean": "학습권",
            "vietnamese": "Quyền học tập",
            "hanja": "學習權",
            "hanjaReading": "學(배울 학) + 習(익힐 습) + 權(권리 권)",
            "pronunciation": "꿴 혹 땁",
            "meaningKo": "모든 국민이 교육을 받을 수 있는 기본 권리로, 헌법과 교육법에 명시된 기본권입니다. 베트Nam어로는 'quyền học tập'이며, 한국의 '교육받을 권리'와 동일한 개념입니다. 통역 시 주의할 점은 한국에서 학습권은 '교육을 받을 권리'와 '학습을 방해받지 않을 권리' 두 가지 측면을 모두 포함하지만, 베트Nam에서는 quyền học tập(학습할 권리)과 quyền không bị gián đoạn học tập(학습 방해받지 않을 권리)으로 구분되므로 문맥에 따라 정확히 선택해야 합니다. 또한 '의무교육'은 학습권을 보장하기 위한 제도이므로 quyền học tập과 giáo dục bắt buộc을 함께 설명하는 것이 효과적입니다. '학습권 침해'는 vi phạm quyền học tập으로 번역하며, 법적 분쟁 시 매우 중요한 용어입니다.",
            "meaningVi": "Quyền cơ bản của mọi công dân được tiếp cận và thụ hưởng giáo dục, được ghi nhận trong Hiến pháp và Luật Giáo dục. Ở Việt Nam, quyền học tập bao gồm quyền được học chữ, học văn hóa, học nghề, và học suốt đời mà không bị phân biệt đối xử.",
            "context": "교육 정책, 인권 논의, 교육 차별 금지, 교육 소송에서 사용",
            "culturalNote": "한국 헌법 제31조는 '모든 국민은 능력에 따라 균등하게 교육을 받을 권리를 가진다'고 규정하며, 학습권은 사회권이자 자유권적 성격을 동시에 가집니다. 베트남 헌법 제39조도 '공민은 학습할 권리를 가진다'(Công dân có quyền học tập)고 명시하며, 교육법에서 이를 구체화합니다. 양국 모두 학습권을 기본권으로 인정하지만, 구체적 보장 방식에 차이가 있습니다. 한국은 초등학교부터 중학교까지 의무교육이며 무상(무료)이고, 고등학교도 2021년부터 무상교육이 단계적으로 시행되고 있습니다. 베트남은 초등학교(5년)만 의무교육이며, 중학교(4년)는 보편화 정책으로 사실상 의무화되었지만 법적 의무는 아닙니다. 통역 시 한국의 '의무교육 9년'과 베트남의 '의무교육 5년'을 혼동하지 않도록 주의해야 합니다.",
            "commonMistakes": [
                {
                    "mistake": "학습권을 quyền giáo dục으로 번역",
                    "correction": "quyền học tập",
                    "explanation": "quyền giáo dục은 '교육할 권리'(교사·부모 관점)이며, 학생 관점의 '학습권'은 quyền học tập입니다."
                },
                {
                    "mistake": "학습권 보장을 đảm bảo học tập으로 표현",
                    "correction": "đảm bảo quyền học tập",
                    "explanation": "'quyền'(권리)을 생략하면 '학습 보장'이 되어 의미가 달라집니다. 법률 용어는 완전한 형태를 사용해야 합니다."
                },
                {
                    "mistake": "학습권 침해를 làm hại quyền học tập으로 번역",
                    "correction": "vi phạm quyền học tập",
                    "explanation": "법적 침해는 vi phạm(위반)을 사용하며, làm hại는 '해치다'의 일반적 표현입니다."
                }
            ],
            "examples": [
                {
                    "ko": "모든 아동은 출신과 관계없이 학습권을 보장받습니다.",
                    "vi": "Mọi trẻ em đều được đảm bảo quyền học tập bất kể xuất thân.",
                    "situation": "formal"
                },
                {
                    "ko": "학교는 학생의 학습권을 침해하는 어떠한 행위도 해서는 안 됩니다.",
                    "vi": "Nhà trường không được thực hiện bất kỳ hành vi nào vi phạm quyền học tập của học sinh.",
                    "situation": "formal"
                },
                {
                    "ko": "이번 정책은 장애 학생의 학습권 보장을 목표로 합니다.",
                    "vi": "Chính sách lần này nhằm mục tiêu đảm bảo quyền học tập của học sinh khuyết tật.",
                    "situation": "formal"
                }
            ],
            "relatedTerms": ["giao-duc-bat-buoc", "luat-giao-duc", "hoc-phi"]
        },
        {
            "slug": "dao-tao-nghe",
            "korean": "직업훈련",
            "vietnamese": "Đào tạo nghề",
            "hanja": "職業訓鍊",
            "hanjaReading": "職(직업 직) + 業(업 업) + 訓(가르칠 훈) + 鍊(연마할 련)",
            "pronunciation": "다오 따오 응에",
            "meaningKo": "특정 직업에 필요한 기술과 지식을 습득하도록 하는 교육 과정으로, 한국의 폴리텍, 직업전문학교 등이 이에 해당합니다. 베트Nam어로는 'đào tạo nghề'이며, 정규 대학 교육(đào tạo đại học)과 구분되는 별도 교육 체계입니다. 통역 시 주의할 점은 한국에서 '직업훈련'은 고용노동부 소관의 직업능력개발훈련과 교육부 소관의 직업교육을 포괄하지만, 베트Nam에서는 đào tạo nghề(직업훈련)이 교육법 체계 내에서 명확히 정의되어 있으며, ①trung cấp nghề(중급 직업, 2년), ②cao đẳng nghề(전문 직업, 2~3년), ③dạy nghề ngắn hạn(단기 직업, 3개월~1년) 세 가지로 구분됩니다. '직업훈련원'은 trung tâm dạy nghề, '직업훈련생'은 học viên dạy nghề로 번역하며, '실습'은 thực tập으로 표현합니다.",
            "meaningVi": "Hình thức giáo dục nhằm trang bị kỹ năng, kiến thức chuyên môn cho nghề nghiệp cụ thể. Ở Việt Nam, đào tạo nghề bao gồm các cấp độ: trung cấp nghề (2-3 năm), cao đẳng nghề (2-3 năm), và dạy nghề ngắn hạn (dưới 1 năm). Thuộc hệ thống giáo dục nghề nghiệp riêng biệt với giáo dục đại học.",
            "context": "고용 정책, 노동 계약, 인력 양성, 산학 협력에서 사용",
            "culturalNote": "한국의 직업훈련은 '일학습병행제', '폴리텍', '직업전문학교' 등 다양한 형태가 있으며, 고용보험 지원으로 무료 또는 저렴하게 제공되는 경우가 많습니다. 베트남에서는 직업훈련이 정규 교육 체계의 한 축으로 자리 잡고 있으며, trung cấp nghề와 cao đẳng nghề는 학위로 인정됩니다(bằng cấp). 한국의 '국가기술자격증'은 베트남의 'chứng chỉ nghề quốc gia'(국가직업자격증)와 유사하지만, 베트남은 자격증 없이도 취업이 가능한 경우가 많아 한국보다 자격증의 중요도가 낮습니다. 통역 시 한국 기업이 베트Nam 근로자에게 '자격증 필수'를 요구할 때, 베트Nam에서는 학위(bằng cấp)는 있지만 자격증(chứng chỉ)은 없는 경우가 많으므로 이를 명확히 구분하여 안내해야 합니다. 또한 베트Nam의 '직업훈련 센터'(trung tâm dạy nghề)는 한국의 학원과 유사한 사설 기관도 포함되므로, 공인 여부를 확인하는 것이 중요합니다.",
            "commonMistakes": [
                {
                    "mistake": "직업훈련을 đào tạo việc làm으로 번역",
                    "correction": "đào tạo nghề",
                    "explanation": "việc làm은 '일자리'를 의미하며, 직업(nghề)과는 다릅니다. 공식 용어는 đào tạo nghề입니다."
                },
                {
                    "mistake": "직업학교를 trường nghề로만 통역",
                    "correction": "trường trung cấp nghề 또는 trường cao đẳng nghề (수준에 따라)",
                    "explanation": "베트남에서는 직업학교의 수준을 명확히 해야 하므로 trung cấp인지 cao đẳng인지 구분이 필요합니다."
                },
                {
                    "mistake": "직업훈련생을 sinh viên dạy nghề로 표현",
                    "correction": "học viên dạy nghề",
                    "explanation": "sinh viên은 대학생을 지칭하며, 직업훈련생은 học viên(수강생)을 사용해야 합니다."
                }
            ],
            "examples": [
                {
                    "ko": "이 회사는 신입사원에게 3개월간 직업훈련을 제공합니다.",
                    "vi": "Công ty này cung cấp đào tạo nghề 3 tháng cho nhân viên mới.",
                    "situation": "formal"
                },
                {
                    "ko": "직업훈련원에서 용접 기술을 배우고 자격증을 취득했습니다.",
                    "vi": "Tôi đã học kỹ thuật hàn tại trung tâm dạy nghề và lấy được chứng chỉ.",
                    "situation": "formal"
                },
                {
                    "ko": "정부는 청년 실업 해소를 위해 직업훈련 프로그램을 확대하고 있습니다.",
                    "vi": "Chính phủ đang mở rộng các chương trình đào tạo nghề để giải quyết thất nghiệp thanh niên.",
                    "situation": "formal"
                }
            ],
            "relatedTerms": ["bang-cap", "co-so-giao-duc", "quyen-hoc-tap"]
        },
        {
            "slug": "giao-duc-bat-buoc",
            "korean": "의무교육",
            "vietnamese": "Giáo dục bắt buộc",
            "hanja": "義務教育",
            "hanjaReading": "義(옳을 의) + 務(힘쓸 무) + 教(가르칠 교) + 育(기를 육)",
            "pronunciation": "자오 쭉 밧 붙",
            "meaningKo": "국가가 모든 국민에게 일정 기간 동안 의무적으로 교육을 받도록 하는 제도로, 한국은 초등학교 6년과 중학교 3년 총 9년이 의무교육입니다. 베트Nam어로는 'giáo dục bắt buộc'이며, 베트Nam은 초등학교 5년만 법적 의무교육입니다. 통역 시 주의할 점은 한국에서 의무교육은 '무상교육'(학비 무료)과 동일하지만, 베트Nam에서는 giáo dục bắt buộc(의무)과 giáo dục miễn phí(무상)이 별개 개념이므로 혼동하지 않아야 합니다. 또한 한국은 '의무교육 9년'이지만 베트Nam은 '의무교육 5년 + 보편교육 중학교 4년'이므로, 한국 측이 '중학교는 의무교육 아닌가요?'라고 물을 때 베트Nam에서는 법적으로는 의무가 아니지만 사실상 보편화되었다고 설명해야 정확합니다. '의무교육 대상'은 đối tượng giáo dục bắt buộc, '의무교육 위반'은 vi phạm quy định giáo dục bắt buộc으로 표현합니다.",
            "meaningVi": "Chế độ giáo dục mà nhà nước quy định bắt buộc mọi công dân phải thực hiện trong thời gian nhất định. Ở Việt Nam, theo Luật Giáo dục, giáo dục bắt buộc là cấp tiểu học (5 năm). Trung học cơ sở (4 năm) là phổ cập nhưng chưa phải bắt buộc theo pháp luật.",
            "context": "교육 정책, 아동 인권, 교육법 위반, 학교 출석 관리에서 사용",
            "culturalNote": "한국의 의무교육은 1950년 초등 6년으로 시작하여 2004년 중학교까지 확대되었으며, 현재 고등학교 무상교육도 단계적으로 시행 중입니다. 베트남은 1991년 초등 5년이 의무교육으로 법제화되었고, 중학교는 2000년대부터 '보편교육'(phổ cập giáo dục) 정책으로 사실상 의무화되었지만 법적 강제는 아닙니다. 즉, 베트Nam에서 중학교를 가지 않아도 법적 처벌은 없지만, 정부가 보편화를 목표로 무료 교육을 제공합니다. 한국에서는 의무교육 대상 아동이 학교에 가지 않으면 부모가 과태료 처분을 받을 수 있지만, 베트Nam에서는 초등학교만 이러한 처벌 규정이 있습니다. 통역 시 한국 측이 '베트Nam도 중학교까지 의무 아닌가요?'라고 오해하는 경우가 많으므로, '법적 의무는 초등만, 중학은 사실상 보편교육'이라고 명확히 설명해야 합니다.",
            "commonMistakes": [
                {
                    "mistake": "의무교육을 giáo dục bắt buộc phải học으로 중복 표현",
                    "correction": "giáo dục bắt buộc",
                    "explanation": "bắt buộc 자체가 '의무'를 의미하므로 'phải học'(배워야 한다)은 중복입니다."
                },
                {
                    "mistake": "무상교육과 의무교육을 모두 giáo dục bắt buộc으로 통역",
                    "correction": "의무교육은 giáo dục bắt buộc, 무상교육은 giáo dục miễn phí",
                    "explanation": "의무(강제)와 무상(무료)은 다른 개념이며, 베트남에서는 명확히 구분됩니다."
                },
                {
                    "mistake": "의무교육 연한을 thời gian học bắt buộc으로 표현",
                    "correction": "thời gian giáo dục bắt buộc 또는 niên học bắt buộc",
                    "explanation": "thời gian học은 '공부 시간'으로 오해될 수 있으며, 교육 기간은 thời gian giáo dục이 정확합니다."
                }
            ],
            "examples": [
                {
                    "ko": "한국은 초등학교와 중학교 9년이 의무교육입니다.",
                    "vi": "Ở Hàn Quốc, 9 năm tiểu học và trung học cơ sở là giáo dục bắt buộc.",
                    "situation": "formal"
                },
                {
                    "ko": "의무교육 대상 아동은 반드시 학교에 등록해야 합니다.",
                    "vi": "Trẻ em thuộc đối tượng giáo dục bắt buộc phải đăng ký vào trường học.",
                    "situation": "formal"
                },
                {
                    "ko": "의무교육 기간 동안은 학비가 전액 면제됩니다.",
                    "vi": "Trong thời gian giáo dục bắt buộc, học phí được miễn toàn bộ.",
                    "situation": "formal"
                }
            ],
            "relatedTerms": ["quyen-hoc-tap", "luat-giao-duc", "hoc-phi"]
        },
        {
            "slug": "kiem-dinh-chat-luong-giao-duc",
            "korean": "교육품질인증",
            "vietnamese": "Kiểm định chất lượng giáo dục",
            "hanja": "教育品質認證",
            "hanjaReading": "教(가르칠 교) + 育(기를 육) + 品(물건 품) + 質(바탕 질) + 認(알 인) + 證(증거 증)",
            "pronunciation": "끼엠 딘 쩟 르엉 자오 쭉",
            "meaningKo": "교육기관의 교육 프로그램, 시설, 교수진 등이 일정 기준을 충족하는지 평가하고 인증하는 제도입니다. 한국에서는 대학평가인증, 학교평가 등이 이에 해당하며, 베트Nam어로는 'kiểm định chất lượng giáo dục'입니다. 통역 시 주의할 점은 한국에서 '인증'과 '평가'를 혼용하지만, 베트Nam에서는 ①kiểm định(인증 - 기준 충족 여부), ②đánh giá(평가 - 등급 부여), ③xếp hạng(순위 - 대학 랭킹) 세 가지로 명확히 구분됩니다. 또한 한국은 대학인증이 자율이지만, 베트Nam에서는 고등교육법상 모든 대학이 5년마다 의무적으로 kiểm định을 받아야 하므로, '선택'이 아닌 '의무'임을 강조해야 합니다. '인증 기관'은 tổ chức kiểm định, '인증 기준'은 tiêu chuẩn kiểm định, '인증서'는 giấy chứng nhận kiểm định으로 표현합니다.",
            "meaningVi": "Hệ thống đánh giá và xác nhận rằng chương trình giáo dục, cơ sở vật chất, đội ngũ giảng viên của cơ sở giáo dục đáp ứng các tiêu chuẩn chất lượng quy định. Ở Việt Nam, theo Luật Giáo dục đại học, các trường đại học phải thực hiện kiểm định chất lượng định kỳ 5 năm một lần.",
            "context": "대학 평가, 국제 협력, 학위 인정, 교육 행정에서 사용",
            "culturalNote": "한국의 교육품질인증은 대학교육협의회(대교협)와 한국대학평가원이 주관하며, 인증 결과가 정부 재정지원과 연계되지만 법적 강제는 아닙니다. 베트남에서는 교육품질관리국(Cục Quản lý chất lượng)이 주관하며, 법적으로 모든 대학이 의무적으로 받아야 합니다. 인증을 받지 못하면 신입생 모집 중단 등의 제재가 있습니다. 한국은 인증 기준이 상대적으로 유연하지만, 베트Nam은 ①교육 프로그램, ②교수진, ③학생, ④시설, ⑤연구 활동 등 5개 영역 25개 기준을 엄격히 적용합니다. 또한 베트Nam은 국제 인증(kiểm định quốc tế)을 받은 대학이 많지 않아, 한국과의 학위 인정 협상 시 'ABET, ACBSP 등 국제 인증 여부'가 중요한 이슈가 됩니다. 통역 시 한국 측이 '인증만 받으면 되는 거 아닌가요?'라고 단순화하지 않도록, 베트Nam의 복잡한 인증 체계와 주기, 기준을 상세히 안내해야 합니다.",
            "commonMistakes": [
                {
                    "mistake": "교육품질인증을 chứng nhận chất lượng giáo dục으로 번역",
                    "correction": "kiểm định chất lượng giáo dục",
                    "explanation": "chứng nhận은 단순 '증명'이며, 평가 과정을 포함하는 '인증'은 kiểm định입니다."
                },
                {
                    "mistake": "평가와 인증을 모두 kiểm định으로 통역",
                    "correction": "평가는 đánh giá, 인증은 kiểm định",
                    "explanation": "베트남에서는 đánh giá(성과 평가)와 kiểm định(기준 충족 인증)이 다른 개념입니다."
                },
                {
                    "mistake": "인증서를 bằng kiểm định으로 표현",
                    "correction": "giấy chứng nhận kiểm định",
                    "explanation": "bằng은 '학위'를 의미하며, 인증서는 giấy chứng nhận입니다."
                }
            ],
            "examples": [
                {
                    "ko": "이 대학은 교육품질인증을 통과하여 국제적으로 인정받고 있습니다.",
                    "vi": "Trường đại học này đã vượt qua kiểm định chất lượng giáo dục và được quốc tế công nhận.",
                    "situation": "formal"
                },
                {
                    "ko": "교육품질인증 기준을 충족하지 못하면 신입생 모집이 제한될 수 있습니다.",
                    "vi": "Nếu không đáp ứng tiêu chuẩn kiểm định chất lượng giáo dục, việc tuyển sinh có thể bị hạn chế.",
                    "situation": "formal"
                },
                {
                    "ko": "우리 기관은 내년에 교육품질인증을 받을 예정입니다.",
                    "vi": "Cơ quan chúng tôi dự kiến thực hiện kiểm định chất lượng giáo dục vào năm sau.",
                    "situation": "formal"
                }
            ],
            "relatedTerms": ["tu-chu-dai-hoc", "luat-giao-duc", "cong-nhan-bang"]
        }
    ]

    # 중복 체크 및 추가
    added_count = 0
    skipped = []

    for term in new_terms:
        if term['slug'] in existing_slugs:
            skipped.append(term['slug'])
            print(f"⚠️  중복 건너뜀: {term['slug']}")
        else:
            data.append(term)
            existing_slugs.add(term['slug'])
            added_count += 1
            print(f"✅ 추가됨: {term['slug']} - {term['korean']}")

    # 파일 저장
    with open(file_path, 'w', encoding='utf-8') as f:
        json.dump(data, f, ensure_ascii=False, indent=2)

    # 결과 출력
    print(f"\n{'='*50}")
    print(f"✨ 교육법 용어 추가 완료")
    print(f"{'='*50}")
    print(f"📊 추가된 용어: {added_count}개")
    print(f"⏭️  중복 건너뜀: {len(skipped)}개")
    if skipped:
        print(f"   건너뛴 slug: {', '.join(skipped)}")
    print(f"📁 파일: {file_path}")
    print(f"📈 전체 용어 수: {len(data)}개")
    print(f"\n🎯 품질 기준: Tier S (90점+)")
    print(f"   - meaningKo: 200자+ (통역 팁 포함)")
    print(f"   - meaningVi: 100자+ (성조 포함)")
    print(f"   - culturalNote: 100자+ (한베 문화 차이)")
    print(f"   - commonMistakes: 3개+ (객체 형식)")
    print(f"   - examples: 3개+ (situation 포함)")
    print(f"   - relatedTerms: 3개+")
    print(f"\n다음 단계:")
    print(f"  npm run validate:terms -- --domain=legal")
    print(f"{'='*50}\n")

if __name__ == '__main__':
    add_education_law_terms()
