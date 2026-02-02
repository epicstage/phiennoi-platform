#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
건설교육/자격증 (Construction Education/Certification) 용어 추가 스크립트
Tier S 품질 기준 준수 (90점 이상)
"""

import json
import os

# 파일 경로 설정
file_path = os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', 'data', 'terms', 'construction.json')

# 새로운 용어 데이터 (10개)
new_terms = [
    {
        "slug": "chung-chi-hanh-nghe",
        "korean": "자격증",
        "vietnamese": "chứng chỉ hành nghề",
        "hanja": "資格證",
        "hanjaReading": "資(재물 자) + 格(격식 격) + 證(증거 증)",
        "pronunciation": "충 찌 한 응에",
        "meaningKo": "특정 직업이나 업무를 수행할 수 있는 자격을 공식적으로 인정받은 증서. 건설 현장에서 통역 시 주의할 점은 한국의 '기사 자격증'과 베트남의 'chứng chỉ hành nghề'가 발급 기관과 효력 범위에서 차이가 있다는 것입니다. 한국은 국가기술자격법에 따라 국가가 발급하지만, 베트남은 업종별 협회나 교육기관에서도 발급할 수 있어 통역 시 발급 주체를 명확히 구분해야 합니다. 또한 한국의 자격증은 등급(기능사/기사/기술사)이 있지만 베트남은 등급 구분이 덜 명확한 경우가 많아 실수를 주의해야 합니다.",
        "meaningVi": "Văn bằng chứng nhận năng lực và quyền hành nghề trong lĩnh vực chuyên môn. Tại Việt Nam, chứng chỉ hành nghề xây dựng được cấp bởi Bộ Xây dựng hoặc các hiệp hội ngành nghề. Cần phân biệt với bằng cấp học vấn (bằng tốt nghiệp) và giấy phép hành nghề (giấy phép hành nghề xây dựng). Chứng chỉ này là bắt buộc đối với các vị trí kỹ sư, giám sát tại công trường.",
        "context": "행정·인사 업무, 채용 면접, 자격 검증 시 사용",
        "culturalNote": "한국은 국가기술자격 체계가 매우 체계적이며 기능사-기사-기술사 3단계로 명확히 구분됩니다. 반면 베트남은 chứng chỉ hành nghề 외에도 giấy phép hành nghề(면허), bằng cấp(학위) 등이 혼재되어 사용되며, 발급 기관도 다양합니다. 통역 시 한국 측이 요구하는 자격증의 정확한 등급과 베트남 측이 보유한 자격의 법적 효력을 양측에 명확히 설명해야 오해를 방지할 수 있습니다.",
        "commonMistakes": [
            {
                "mistake": "자격증을 giấy phép로 번역",
                "correction": "chứng chỉ hành nghề 또는 văn bằng chuyên môn",
                "explanation": "giấy phép은 '면허'를 의미하며 정부 허가의 성격이 강함. 자격증은 능력 인증의 의미이므로 chứng chỉ가 적절함"
            },
            {
                "mistake": "기사 자격증을 bằng kỹ sư로 번역",
                "correction": "chứng chỉ kỹ sư xây dựng 또는 chứng chỉ hành nghề kỹ sư",
                "explanation": "bằng은 학위증을 의미하므로 자격증과 혼동될 수 있음. 명확히 chứng chỉ를 사용해야 함"
            },
            {
                "mistake": "자격증 등급을 베트남어로 구분 없이 사용",
                "correction": "기능사=chứng chỉ thợ, 기사=chứng chỉ kỹ sư, 기술사=chứng chỉ kỹ sư cao cấp",
                "explanation": "베트남은 한국만큼 등급 구분이 명확하지 않으므로 통역 시 등급을 설명 추가 필요"
            }
        ],
        "examples": [
            {
                "ko": "건설기사 자격증을 소지한 분만 지원 가능합니다.",
                "vi": "Chỉ ứng viên có chứng chỉ kỹ sư xây dựng mới được ứng tuyển.",
                "situation": "formal"
            },
            {
                "ko": "자격증 사본 제출 부탁드립니다.",
                "vi": "Vui lòng nộp bản sao chứng chỉ hành nghề.",
                "situation": "formal"
            },
            {
                "ko": "현장에서 자격증 확인 좀 해주세요.",
                "vi": "Anh kiểm tra chứng chỉ giúp tôi ở công trường nhé.",
                "situation": "onsite"
            }
        ],
        "relatedTerms": ["ky-su-xay-dung", "dao-tao-an-toan", "kiem-dinh-vien"]
    },
    {
        "slug": "dao-tao-an-toan",
        "korean": "안전교육",
        "vietnamese": "đào tạo an toàn",
        "hanja": "安全敎育",
        "hanjaReading": "安(편안 안) + 全(온전 전) + 敎(가르칠 교) + 育(기를 육)",
        "pronunciation": "다오 타오 안 토안",
        "meaningKo": "건설 현장에서 작업자의 안전을 위해 실시하는 필수 교육 프로그램. 통역 시 주의할 점은 한국의 산업안전보건법에 따른 의무 교육 시간(일일 안전교육 10분, 채용 시 8시간 등)과 베트남의 안전교육 규정이 다르다는 것입니다. 한국은 매일 작업 전 안전교육이 법적으로 강제되지만, 베트남은 프로젝트 착수 시와 분기별 교육이 일반적이어서 통역 시 양국의 교육 주기와 내용을 명확히 구분해야 합니다. 또한 '안전교육 이수증'과 '안전보건교육'을 혼동하지 않도록 주의가 필요합니다.",
        "meaningVi": "Chương trình đào tạo bắt buộc về an toàn lao động tại công trường xây dựng. Theo quy định của Việt Nam, công nhân phải được đào tạo an toàn trước khi vào làm việc và định kỳ hàng quý. Nội dung bao gồm: sử dụng thiết bị bảo hộ, quy trình làm việc an toàn, xử lý tình huống khẩn cấp, và phòng ngừa tai nạn lao động. Khác với Hàn Quốc, Việt Nam chưa có quy định đào tạo an toàn hàng ngày trước ca làm việc.",
        "context": "현장 안전 관리, 작업 착수 전, 정기 안전회의에서 사용",
        "culturalNote": "한국 건설현장은 '아침조회'에서 매일 10분 이상의 안전교육(TBM: Tool Box Meeting)이 법적으로 의무화되어 있으며, 미이행 시 과태료가 부과됩니다. 반면 베트남 현장은 프로젝트 시작 시 집중 교육 후 분기별 또는 월별 교육이 일반적입니다. 한국 시공사가 베트남 현장에 진출할 때 이 차이로 인한 갈등이 자주 발생하므로, 통역사는 양국의 법적 요구사항과 현장 관행을 모두 이해하고 있어야 합니다.",
        "commonMistakes": [
            {
                "mistake": "안전교육을 học an toàn로 번역",
                "correction": "đào tạo an toàn",
                "explanation": "học은 '배우다'는 학습자 입장이고, đào tạo는 '교육하다'는 제공자 입장으로 공식 용어임"
            },
            {
                "mistake": "일일 안전교육을 đào tạo an toàn hàng ngày로만 번역",
                "correction": "họp an toàn đầu ca 또는 TBM (Tool Box Meeting)",
                "explanation": "베트남 현장에서는 đào tạo보다 họp(회의) 개념으로 이해되는 경우가 많아 설명 추가 필요"
            },
            {
                "mistake": "안전교육 이수증을 bằng đào tạo로 번역",
                "correction": "giấy chứng nhận hoàn thành đào tạo an toàn",
                "explanation": "bằng은 학위를 의미하므로 부적절. giấy chứng nhận이 정확함"
            }
        ],
        "examples": [
            {
                "ko": "오늘 작업 전 안전교육 10분 진행하겠습니다.",
                "vi": "Hôm nay chúng ta sẽ họp an toàn 10 phút trước khi làm việc.",
                "situation": "onsite"
            },
            {
                "ko": "신규 작업자는 8시간 안전교육 필수입니다.",
                "vi": "Công nhân mới phải tham gia đào tạo an toàn 8 tiếng.",
                "situation": "formal"
            },
            {
                "ko": "안전교육 자료 준비해주세요.",
                "vi": "Anh chuẩn bị tài liệu đào tạo an toàn giúp tôi.",
                "situation": "onsite"
            }
        ],
        "relatedTerms": ["chung-chi-hanh-nghe", "huan-luyen-vien", "giam-sat-truong"]
    },
    {
        "slug": "ky-su-xay-dung",
        "korean": "건설기사",
        "vietnamese": "kỹ sư xây dựng",
        "hanja": "建設技士",
        "hanjaReading": "建(세울 건) + 設(베풀 설) + 技(재주 기) + 士(선비 사)",
        "pronunciation": "끼 쓰 싸이 증",
        "meaningKo": "건설 분야의 국가기술자격 중 하나로, 토목·건축 등의 설계·시공·감리 업무를 수행할 수 있는 중급 기술 자격. 통역 시 주의할 점은 한국의 '건설기사'는 국가기술자격법상 명확한 등급(기능사<기사<기술사)이지만, 베트남의 'kỹ sư xây dựng'은 일반적으로 4년제 건축/토목 대학 졸업자를 지칭하며 별도의 국가시험이 없는 경우가 많다는 것입니다. 따라서 한국 기업이 베트남 인력을 채용할 때 '건설기사 자격 보유자'를 요구하면 베트남 측에서는 학위증을 제출하는 경우가 많아 혼란이 발생합니다. 통역사는 이 차이를 명확히 설명해야 합니다.",
        "meaningVi": "Kỹ sư chuyên ngành xây dựng, có bằng đại học chuyên ngành xây dựng, kiến trúc hoặc kỹ thuật hạ tầng. Tại Việt Nam, kỹ sư xây dựng được công nhận dựa trên bằng cấp đại học, không cần thi quốc gia riêng như Hàn Quốc. Tuy nhiên, để hành nghề, cần có chứng chỉ hành nghề do Bộ Xây dựng cấp. Kỹ sư xây dựng có thể làm việc ở các vị trí: thiết kế, thi công, giám sát, quản lý dự án.",
        "context": "채용 공고, 자격 검증, 업무 배치 시 사용",
        "culturalNote": "한국의 건설기사는 필기시험+실기시험을 통과해야 하는 국가자격이며, 등급이 명확합니다(기능사→기사→기술사). 그러나 베트남은 대학 졸업만으로 'kỹ sư' 칭호를 받으며, 추가 국가시험 없이 경력과 학위만으로 kỹ sư로 인정받습니다. 한국 기업이 베트남에서 '건설기사 자격 소지자'를 구할 때, 베트남 측은 학위증을 제시하는 경우가 많아 통역사는 양국의 자격 체계 차이를 중재해야 합니다. 실무에서는 '한국 건설기사 = 베트남 대졸 kỹ sư + 실무 3년 이상'으로 환산하는 것이 일반적입니다.",
        "commonMistakes": [
            {
                "mistake": "건설기사를 kỹ sư xây dựng cấp 2로 번역",
                "correction": "kỹ sư xây dựng (có chứng chỉ hành nghề)",
                "explanation": "베트남에는 kỹ sư에 '급'(cấp) 구분이 공식적으로 없으므로 오해 발생 가능"
            },
            {
                "mistake": "기술사를 kỹ sư cao cấp으로만 번역",
                "correction": "kỹ sư chuyên gia (có trình độ chuyên gia)",
                "explanation": "베트남에 기술사에 대응하는 공식 자격이 없으므로 설명 추가 필요"
            },
            {
                "mistake": "건설기사 자격증을 bằng kỹ sư xây dựng으로 번역",
                "correction": "chứng chỉ kỹ sư xây dựng (자격증) vs bằng kỹ sư (학위증)",
                "explanation": "bằng은 학위, chứng chỉ는 자격증으로 명확히 구분해야 함"
            }
        ],
        "examples": [
            {
                "ko": "건설기사 자격 소지자 우대합니다.",
                "vi": "Ưu tiên ứng viên có chứng chỉ kỹ sư xây dựng (hoặc bằng đại học xây dựng + 3 năm kinh nghiệm).",
                "situation": "formal"
            },
            {
                "ko": "토목 건설기사 자격증 있으신가요?",
                "vi": "Anh có bằng kỹ sư xây dựng chuyên ngành công trình không?",
                "situation": "formal"
            },
            {
                "ko": "현장에 건설기사 몇 명 배치됐어?",
                "vi": "Công trường có bao nhiêu kỹ sư xây dựng?",
                "situation": "onsite"
            }
        ],
        "relatedTerms": ["chung-chi-hanh-nghe", "ky-su-ket-cau", "giam-sat-truong"]
    },
    {
        "slug": "giam-sat-truong",
        "korean": "감리단장",
        "vietnamese": "giám sát trưởng",
        "hanja": "監理團長",
        "hanjaReading": "監(볼 감) + 理(다스릴 리) + 團(둥글 단) + 長(긴 장)",
        "pronunciation": "잠 샛 쯩",
        "meaningKo": "건설공사 감리업무를 총괄하는 책임자로, 설계도서 대로 시공이 이루어지는지 감독하고 공사의 품질과 안전을 관리하는 최고 책임자. 통역 시 주의할 점은 한국의 '감리'와 베트남의 'giám sát'이 법적 책임 범위가 다르다는 것입니다. 한국은 감리가 독립적인 제3자로서 발주자와 시공자 사이에서 중립적 입장을 취하지만, 베트남은 giám sát이 종종 발주자 측 인력으로 간주되어 시공사와 대립 구도가 더 명확합니다. 또한 한국의 감리단장은 건축사 또는 기술사 자격 필수이지만, 베트남은 kỹ sư 학위와 경력으로 충분한 경우가 많아 자격 요건 차이를 설명해야 합니다.",
        "meaningVi": "Trưởng nhóm giám sát công trình, chịu tr책nhiệm tổng thể về kiểm soát chất lượng, tiến độ và an toàn tại công trường. Tại Việt Nam, giám sát trưởng thường là kỹ sư có ít nhất 5-7 năm kinh nghiệm, được bổ nhiệm bởi đơn vị tư vấn giám sát. Nhiệm vụ chính: kiểm tra bản vẽ thi công, giám sát quy trình thi công, nghiệm thu công trình, và báo cáo cho chủ đầu tư. Khác với Hàn Quốc, vai trò giám sát tại Việt Nam có xu hướng thiên về phía chủ đầu tư hơn là trung lập giữa các bên.",
        "context": "계약 체결, 현장 조직도 작성, 책임 소재 논의 시 사용",
        "culturalNote": "한국의 감리제도는 '건축사법'과 '건설기술진흥법'에 근거하여 엄격히 규제되며, 감리단장은 건축사 또는 건설기술사 자격이 필수입니다. 감리는 발주자도 시공자도 아닌 독립적 제3자로서 공정성을 유지해야 합니다. 반면 베트남의 giám sát(감리)는 발주자가 고용한 '감독관' 성격이 강하며, 시공사와의 관계가 한국보다 더 대립적입니다. 한국 감리사가 베트남 현장에서 일할 때 이 권한과 책임 범위의 차이로 인한 갈등이 빈번하므로, 통역사는 양국의 감리 역할과 법적 지위를 명확히 이해하고 설명해야 합니다.",
        "commonMistakes": [
            {
                "mistake": "감리단장을 người quản lý로 번역",
                "correction": "giám sát trưởng 또는 trưởng ban giám sát",
                "explanation": "quản lý는 '관리자' 일반을 의미하며, 감리의 법적 지위를 표현하지 못함"
            },
            {
                "mistake": "감리를 kiểm tra로 번역",
                "correction": "giám sát (감리) vs kiểm tra (검사)",
                "explanation": "kiểm tra는 일회성 검사, giám sát은 지속적 감독이므로 감리는 giám sát이 적절"
            },
            {
                "mistake": "감리단을 nhóm giám sát로만 번역",
                "correction": "ban giám sát 또는 đơn vị tư vấn giám sát",
                "explanation": "공식 문서에서는 nhóm보다 ban(단) 또는 đơn vị(단위)가 격식 있는 표현"
            }
        ],
        "examples": [
            {
                "ko": "감리단장 승인 없이는 공사 진행 불가합니다.",
                "vi": "Không được thi công nếu chưa có chữ ký giám sát trưởng.",
                "situation": "formal"
            },
            {
                "ko": "감리단장이 현장 점검 나오신다고 하니 정리 좀 해.",
                "vi": "Giám sát trưởng sẽ đến kiểm tra, anh dọn dẹp một chút.",
                "situation": "onsite"
            },
            {
                "ko": "감리단장 의견서 받으셨나요?",
                "vi": "Anh đã nhận ý kiến của giám sát trưởng chưa?",
                "situation": "formal"
            }
        ],
        "relatedTerms": ["ky-su-xay-dung", "kiem-dinh-vien", "dao-tao-an-toan"]
    },
    {
        "slug": "ky-su-ket-cau",
        "korean": "구조기술사",
        "vietnamese": "kỹ sư kết cấu",
        "hanja": "構造技術士",
        "hanjaReading": "構(얽을 구) + 造(지을 조) + 技(재주 기) + 術(재주 술) + 士(선비 사)",
        "pronunciation": "끼 쓰 껫 까우",
        "meaningKo": "건축물이나 구조물의 구조 설계 및 구조 안전성을 담당하는 최고급 기술 자격자. 한국에서는 국가기술자격 중 최고 등급인 '기술사' 자격으로, 고층 건물이나 대형 구조물의 구조 설계는 반드시 구조기술사의 검토를 받아야 합니다. 통역 시 주의할 점은 한국의 '기술사'는 매우 까다로운 국가시험(합격률 5% 이하)을 통과한 최상위 자격인 반면, 베트남에는 이에 대응하는 공식 자격이 없다는 것입니다. 베트남에서는 'kỹ sư kết cấu cao cấp' 또는 'chuyên gia kết cấu'로 표현하지만 이는 경력과 실적에 기반한 호칭이지 국가자격이 아닙니다. 통역 시 한국 기술사의 권위와 법적 책임을 베트남 측에 충분히 설명해야 합니다.",
        "meaningVi": "Kỹ sư chuyên về thiết kế kết cấu công trình, chịu trách nhiệm tính toán và đảm bảo an toàn kết cấu của tòa nhà, cầu, đường hầm và các công trình lớn. Tại Việt Nam, kỹ sư kết cấu là người có bằng đại học chuyên ngành kết cấu công trình và kinh nghiệm thiết kế thực tế. Khác với Hàn Quốc, Việt Nam chưa có hệ thống chứng chỉ quốc gia tương đương 'kỹ thuật sư' (기술사), do đó kỹ sư kết cấu được đánh giá chủ yếu dựa trên kinh nghiệm và danh tiếng cá nhân.",
        "context": "구조 설계 검토, 안전진단, 대형 프로젝트 계약 시 사용",
        "culturalNote": "한국의 기술사 제도는 1963년부터 시작된 최고급 국가기술자격으로, 특히 구조기술사는 건축구조기술사와 토목구조기술사로 세분화되어 있으며 대형 건축물(16층 이상)이나 특수구조물은 반드시 기술사의 구조 검토를 받아야 법적으로 인정됩니다. 반면 베트남에는 기술사에 해당하는 공식 자격이 없으며, 'chuyên gia' (전문가) 또는 'kỹ sư cao cấp' (고급 기술자)라는 비공식 호칭만 존재합니다. 한국 기업이 베트남에서 대형 프로젝트 수주 시 구조기술사를 투입하면 베트남 측은 그 권위를 이해하지 못하는 경우가 많으므로, 통역사는 '한국 최고 등급 자격, 합격률 5%, 평균 15년 경력'이라는 구체적 설명을 추가해야 합니다.",
        "commonMistakes": [
            {
                "mistake": "기술사를 kỹ sư cao cấp으로만 번역",
                "correction": "chuyên gia kỹ thuật (kỹ sư cấp cao nhất của Hàn Quốc)",
                "explanation": "베트남에 대응 자격이 없으므로 설명을 추가해야 권위가 전달됨"
            },
            {
                "mistake": "구조기술사를 kỹ sư kết cấu로만 번역",
                "correction": "kỹ sư kết cấu cấp chuyên gia (기술사급) 또는 chuyên gia kết cấu",
                "explanation": "일반 kỹ sư kết cấu와 구분하기 위해 '전문가급'임을 명시해야 함"
            },
            {
                "mistake": "기사와 기술사를 구분 없이 kỹ sư로 통일",
                "correction": "기사=kỹ sư, 기술사=chuyên gia kỹ thuật",
                "explanation": "한국의 3단계 자격(기능사/기사/기술사)을 베트남어로 구분해야 함"
            }
        ],
        "examples": [
            {
                "ko": "이 건물은 구조기술사 검토가 필요합니다.",
                "vi": "Tòa nhà này cần được chuyên gia kết cấu (kỹ thuật sư Hàn Quốc) kiểm tra.",
                "situation": "formal"
            },
            {
                "ko": "구조기술사 의견서를 첨부해주세요.",
                "vi": "Vui lòng đính kèm báo cáo của chuyên gia kết cấu.",
                "situation": "formal"
            },
            {
                "ko": "구조기술사가 이 설계 승인했어?",
                "vi": "Chuyên gia kết cấu đã duyệt bản thiết kế này chưa?",
                "situation": "onsite"
            }
        ],
        "relatedTerms": ["ky-su-xay-dung", "giam-sat-truong", "kiem-dinh-vien"]
    },
    {
        "slug": "ky-su-dien",
        "korean": "전기기사",
        "vietnamese": "kỹ sư điện",
        "hanja": "電氣技士",
        "hanjaReading": "電(번개 전) + 氣(기운 기) + 技(재주 기) + 士(선비 사)",
        "pronunciation": "끼 쓰 디엔",
        "meaningKo": "전기 설비의 설계, 시공, 유지보수 및 안전관리 업무를 수행할 수 있는 국가기술자격. 건설 현장에서는 전기 배선, 조명, 동력 설비 등의 설치와 점검을 담당합니다. 통역 시 주의할 점은 한국의 전기기사는 '전기공사법'에 따라 일정 규모 이상의 전기공사는 반드시 전기기사 이상의 자격자가 감리해야 하지만, 베트남은 이러한 법적 강제성이 약하다는 것입니다. 또한 한국은 전기기사와 전기공사기사가 별도 자격이지만, 베트남은 'kỹ sư điện'으로 통칭되므로 세부 전공(전력/제어/통신)을 명확히 구분해야 하는 경우가 많습니다.",
        "meaningVi": "Kỹ sư chuyên ngành điện, chịu trách nhiệm thiết kế, lắp đặt và vận hành hệ thống điện trong công trình. Tại Việt Nam, kỹ sư điện cần có bằng đại học chuyên ngành điện hoặc điện tử và chứng chỉ hành nghề điện do Bộ Công Thương cấp. Công việc bao gồm: thiết kế hệ thống cấp điện, lắp đặt đường dây và thiết bị điện, kiểm tra an toàn điện, và bảo trì hệ thống. Cần chú ý phân biệt kỹ sư điện (thiết kế/giám sát) và thợ điện (thi công).",
        "context": "전기 공사 계약, 안전 점검, 전기 설비 검수 시 사용",
        "culturalNote": "한국은 전기공사법과 전기사업법에 따라 전기 관련 업무가 엄격히 규제되며, 일정 용량 이상의 전기설비는 반드시 전기기사 이상 자격자의 감리를 받아야 합니다. 또한 전기안전공사의 검사를 의무적으로 받아야 준공이 가능합니다. 베트남도 유사한 제도가 있으나 집행이 덜 엄격하며, 소규모 공사에서는 경력 있는 thợ điện(전기공)이 kỹ sư 없이 작업하는 경우도 많습니다. 한국 현장에서 베트남 인력 투입 시 자격증 확인이 필수이며, 통역사는 '전기기사 = kỹ sư điện + chứng chỉ hành nghề'임을 명확히 해야 합니다.",
        "commonMistakes": [
            {
                "mistake": "전기기사를 thợ điện으로 번역",
                "correction": "kỹ sư điện (전기기사) vs thợ điện (전기공)",
                "explanation": "thợ điện은 기능공(기능사급)을 의미하므로 기사와는 등급이 다름"
            },
            {
                "mistake": "전기공사기사를 kỹ sư xây dựng điện으로 번역",
                "correction": "kỹ sư thi công điện 또는 kỹ sư điện (chuyên thi công)",
                "explanation": "베트남에는 한국처럼 전기기사/전기공사기사 구분이 없으므로 설명 추가 필요"
            },
            {
                "mistake": "전기 안전 점검을 kiểm tra điện로만 번역",
                "correction": "kiểm tra an toàn điện 또는 nghiệm thu hệ thống điện",
                "explanation": "단순 kiểm tra는 일반 점검, an toàn을 추가해야 법적 의무 점검임을 명확히 함"
            }
        ],
        "examples": [
            {
                "ko": "전기기사 자격증 있는 분이 현장에 상주해야 합니다.",
                "vi": "Cần có kỹ sư điện (có chứng chỉ) thường trú tại công trường.",
                "situation": "formal"
            },
            {
                "ko": "전기 안전 점검 끝났어?",
                "vi": "Kiểm tra an toàn điện xong chưa?",
                "situation": "onsite"
            },
            {
                "ko": "전기기사 승인 받아야 다음 공정 진행됩니다.",
                "vi": "Phải có chữ ký kỹ sư điện mới được tiếp tục công đoạn tiếp theo.",
                "situation": "formal"
            }
        ],
        "relatedTerms": ["ky-su-co-khi", "ky-su-xay-dung", "chung-chi-hanh-nghe"]
    },
    {
        "slug": "ky-su-co-khi",
        "korean": "기계기사",
        "vietnamese": "kỹ sư cơ khí",
        "hanja": "機械技士",
        "hanjaReading": "機(틀 기) + 械(기계 계) + 技(재주 기) + 士(선비 사)",
        "pronunciation": "끼 쓰 꺼 키",
        "meaningKo": "기계 설비의 설계, 제작, 설치, 유지보수를 담당하는 국가기술자격. 건설 현장에서는 냉난방 설비(HVAC), 승강기, 배관, 소방 설비 등 기계적 시스템의 설치와 관리를 책임집니다. 통역 시 주의할 점은 한국의 '기계기사'가 매우 광범위한 분야(일반기계, 건설기계, 공조냉동기계 등)를 포괄하지만, 건설 현장에서는 주로 '공조냉동기계기사' 또는 '건설기계기사'를 의미한다는 것입니다. 베트남에서는 'kỹ sư cơ khí'가 제조업 기계기사를 연상시키므로, 건설 현장 맥락에서는 'kỹ sư cơ điện (M&E)' 또는 'kỹ sư hệ thống'으로 구체화해야 오해가 없습니다.",
        "meaningVi": "Kỹ sư chuyên ngành cơ khí, chịu trách nhiệm thiết kế, lắp đặt và vận hành các hệ thống cơ khí trong công trình như: hệ thống điều hòa không khí (HVAC), thang máy, hệ thống cấp thoát nước, và thiết bị phòng cháy chữa cháy. Tại Việt Nam, kỹ sư cơ khí xây dựng (M&E Engineer) thường được gọi là 'kỹ sư hệ thống' hoặc 'kỹ sư cơ điện', khác với kỹ sư cơ khí chế tạo (manufacturing). Cần có bằng đại học chuyên ngành cơ khí và chứng chỉ hành nghề.",
        "context": "설비 공사 계약, 기계 설비 검수, HVAC 시스템 논의 시 사용",
        "culturalNote": "한국에서 '기계기사'는 분야별로 세분화되어 있습니다: 일반기계기사, 공조냉동기계기사, 건설기계기사, 설비기사 등. 건설 현장에서는 주로 공조냉동기계기사가 냉난방 시스템을, 설비기사가 배관을 담당합니다. 베트남에서는 이러한 세부 구분이 덜 명확하며, 'kỹ sư cơ khí'라고 하면 자동차나 제조업 기계를 연상하는 경우가 많습니다. 따라서 건설 현장에서는 'kỹ sư M&E' (Mechanical & Electrical Engineer) 또는 'kỹ sư hệ thống kỹ thuật'이라는 표현이 더 명확합니다. 통역 시 구체적인 담당 시스템(HVAC, 배관, 승강기 등)을 명시하는 것이 좋습니다.",
        "commonMistakes": [
            {
                "mistake": "기계기사를 kỹ sư chế tạo로 번역",
                "correction": "kỹ sư cơ khí (건설) 또는 kỹ sư M&E",
                "explanation": "chế tạo는 제조업을 의미하므로 건설 현장 맥락과 맞지 않음"
            },
            {
                "mistake": "공조냉동기계기사를 kỹ sư điều hòa로만 번역",
                "correction": "kỹ sư hệ thống điều hòa thông gió (HVAC)",
                "explanation": "điều hòa만 쓰면 에어컨 기사로 오해될 수 있으므로 HVAC 명시 필요"
            },
            {
                "mistake": "설비기사를 kỹ sư thiết bị로 번역",
                "correction": "kỹ sư hệ thống ống nước (배관) 또는 kỹ sư cơ điện",
                "explanation": "thiết bị는 장비 일반을 의미하므로 구체적 시스템명 필요"
            }
        ],
        "examples": [
            {
                "ko": "기계기사 자격증 소지자가 HVAC 시스템을 검수합니다.",
                "vi": "Kỹ sư cơ khí (có chứng chỉ) sẽ nghiệm thu hệ thống HVAC.",
                "situation": "formal"
            },
            {
                "ko": "냉난방 설비 점검 기계기사 불렀어?",
                "vi": "Anh đã gọi kỹ sư hệ thống điều hòa đến kiểm tra chưa?",
                "situation": "onsite"
            },
            {
                "ko": "승강기 설치는 기계기사 승인 필요합니다.",
                "vi": "Lắp đặt thang máy cần có chữ ký kỹ sư cơ khí.",
                "situation": "formal"
            }
        ],
        "relatedTerms": ["ky-su-dien", "ky-su-xay-dung", "tho-lanh-nghe"]
    },
    {
        "slug": "tho-lanh-nghe",
        "korean": "기능공",
        "vietnamese": "thợ lành nghề",
        "hanja": "技能工",
        "hanjaReading": "技(재주 기) + 能(능할 능) + 工(장인 공)",
        "pronunciation": "토 라잉 응에",
        "meaningKo": "특정 기술 분야에서 숙련된 실무 능력을 갖춘 작업자. 한국에서는 국가기술자격의 최하위 등급인 '기능사' 자격을 보유하거나, 공인된 직업훈련을 이수한 숙련공을 의미합니다. 건설 현장에서는 목공, 철근공, 용접공, 미장공, 전기공 등 다양한 분야의 기능공이 활동합니다. 통역 시 주의할 점은 한국의 '기능공'과 베트남의 'thợ'가 사회적 인식에서 차이가 있다는 것입니다. 한국은 기능공에 대한 국가 자격 체계(기능사)와 숙련도 인정 제도가 잘 갖춰져 있어 기능공의 지위가 상대적으로 높지만, 베트남은 'thợ'가 단순 육체노동자로 인식되는 경우가 많습니다. 따라서 'thợ lành nghề' (숙련공)임을 강조해야 존중의 의미가 전달됩니다.",
        "meaningVi": "Công nhân có tay nghề cao, được đào tạo chuyên môn trong lĩnh vực cụ thể như thợ mộc, thợ hàn, thợ điện, thợ sơn, v.v. Tại Việt Nam, thợ lành nghề thường qua đào tạo nghề (trung cấp nghề hoặc cao đẳng nghề) và có ít nhất 2-3 năm kinh nghiệm thực tế. Khác với công nhân phổ thông, thợ lành nghề có kỹ năng chuyên môn được công nhận và được trả lương cao hơn. Một số ngành nghề yêu cầu chứng chỉ hành nghề (ví dụ: thợ hàn, thợ điện).",
        "context": "채용 공고, 임금 협상, 작업 배치, 기술 교육 논의 시 사용",
        "culturalNote": "한국의 기능공 제도는 국가기술자격법에 따라 기능사 자격증을 통해 공식 인정되며, 숙련도에 따라 초급기능사→기능사→산업기사→기사로 승급할 수 있는 체계가 마련되어 있습니다. 또한 '명장' 제도를 통해 최고 수준의 기능공을 예우합니다. 반면 베트남은 'thợ'에 대한 공식 자격 체계가 덜 발달했으며, 대부분 도제식 훈련이나 직업학교 졸업으로 기능을 습득합니다. 'thợ'는 종종 육체노동자로 간주되어 사회적 지위가 낮게 평가되므로, 통역 시 'thợ lành nghề' (숙련공) 또는 'thợ có chứng chỉ' (자격증 보유 기능공)으로 표현해 존중을 표해야 합니다.",
        "commonMistakes": [
            {
                "mistake": "기능공을 công nhân로만 번역",
                "correction": "thợ lành nghề 또는 công nhân có tay nghề",
                "explanation": "công nhân은 일반 노동자를 의미하므로 숙련도가 표현되지 않음"
            },
            {
                "mistake": "기능사를 thợ로만 번역",
                "correction": "thợ có chứng chỉ nghề (기능사 자격증 보유)",
                "explanation": "한국의 기능사는 국가자격이므로 '자격증 보유'를 명시해야 함"
            },
            {
                "mistake": "숙련공을 thợ cũ로 번역",
                "correction": "thợ lành nghề (숙련공) vs thợ mới (신입)",
                "explanation": "cũ는 '오래된'의 의미로 부정적 뉘앙스, lành nghề가 '숙련된'의 긍정적 표현"
            }
        ],
        "examples": [
            {
                "ko": "용접 기능공 5명 채용합니다.",
                "vi": "Tuyển 5 thợ hàn lành nghề.",
                "situation": "formal"
            },
            {
                "ko": "이 작업은 숙련된 기능공이 해야 해.",
                "vi": "Công việc này phải có thợ lành nghề mới làm được.",
                "situation": "onsite"
            },
            {
                "ko": "기능사 자격증 있으신 분 우대합니다.",
                "vi": "Ưu tiên ứng viên có chứng chỉ nghề (기능사급).",
                "situation": "formal"
            }
        ],
        "relatedTerms": ["chung-chi-hanh-nghe", "dao-tao-an-toan", "huan-luyen-vien"]
    },
    {
        "slug": "huan-luyen-vien",
        "korean": "훈련교관",
        "vietnamese": "huấn luyện viên",
        "hanja": "訓鍊敎官",
        "hanjaReading": "訓(가르칠 훈) + 鍊(다듬을 련) + 敎(가르칠 교) + 官(벼슬 관)",
        "pronunciation": "후언 루옌 비엔",
        "meaningKo": "직업 기술이나 안전 교육을 전문적으로 가르치는 교육 담당자. 건설 현장에서는 주로 안전교육, 기술 훈련, 신규 작업자 교육을 담당합니다. 통역 시 주의할 점은 한국의 '훈련교관'이 법적으로 일정 자격(산업안전보건교육기관의 강사 자격 등)을 요구하는 공식 직책인 반면, 베트남의 'huấn luyện viên'은 교육 담당자 일반을 의미하여 법적 강제성이 약하다는 것입니다. 한국 현장에서는 교육 이수 시간과 교관 자격이 법적으로 기록되어야 하지만, 베트남은 상대적으로 유연하므로 통역 시 한국의 법적 요구사항을 명확히 전달해야 합니다. 또한 'giảng viên' (강사)와 'huấn luyện viên' (훈련사)을 구분하여, 실기 중심 교육은 huấn luyện viên이 적합함을 설명해야 합니다.",
        "meaningVi": "Người chịu trách nhiệm đào tạo và hướng dẫn kỹ năng nghề hoặc an toàn lao động cho công nhân. Tại công trường xây dựng, huấn luyện viên thường đảm nhận các khóa đào tạo: an toàn lao động, sử dụng thiết bị chuyên dụng, quy trình thi công chuẩn, và xử lý tình huống khẩn cấp. Khác với giảng viên (người dạy lý thuyết), huấn luyện viên tập trung vào thực hành và rèn luyện kỹ năng thực tế. Tại Việt Nam, huấn luyện viên cần có chứng chỉ sư phạm nghề hoặc kinh nghiệm thực tế dày dạn.",
        "context": "안전교육 계획, 신규 작업자 훈련, 기술 교육 프로그램 논의 시 사용",
        "culturalNote": "한국의 산업안전보건법은 일정 규모 이상의 사업장에서 안전보건교육을 의무화하며, 교육을 담당하는 훈련교관은 산업안전보건교육기관의 강사 자격을 갖춰야 합니다. 교육 시간과 내용, 교관 자격이 법적으로 기록되며 미이행 시 과태료가 부과됩니다. 베트남도 유사한 제도가 있으나 집행이 덜 엄격하며, 현장 경력자가 비공식적으로 교육을 담당하는 경우가 많습니다. 한국 기업이 베트남 현장에 진출할 때 안전교육의 법적 요구사항과 교관 자격 기준을 명확히 전달하지 않으면 교육이 형식적으로 진행되는 경우가 많으므로, 통역사는 '법적 의무' 임을 강조해야 합니다.",
        "commonMistakes": [
            {
                "mistake": "훈련교관을 giáo viên으로 번역",
                "correction": "huấn luyện viên (훈련사) vs giáo viên (학교 교사)",
                "explanation": "giáo viên은 학교 교사를 의미하므로 직업 훈련 맥락에서 부적절"
            },
            {
                "mistake": "안전교육 담당자를 người phụ trách an toàn로 번역",
                "correction": "huấn luyện viên an toàn 또는 giảng viên an toàn lao động",
                "explanation": "người phụ trách는 '관리자'이지 '교육자'가 아니므로 역할 혼동 가능"
            },
            {
                "mistake": "강사와 교관을 구분 없이 huấn luyện viên으로 통일",
                "correction": "강사(이론)=giảng viên, 교관(실기)=huấn luyện viên",
                "explanation": "이론 강의는 giảng viên, 실기 훈련은 huấn luyện viên이 적절"
            }
        ],
        "examples": [
            {
                "ko": "안전교육은 자격을 갖춘 훈련교관이 진행해야 합니다.",
                "vi": "Đào tạo an toàn phải do huấn luyện viên có chứng chỉ thực hiện.",
                "situation": "formal"
            },
            {
                "ko": "신규 작업자 훈련 교관 배치 부탁드립니다.",
                "vi": "Vui lòng bố trí huấn luyện viên cho công nhân mới.",
                "situation": "formal"
            },
            {
                "ko": "교관이 실습 지도해줄 거야.",
                "vi": "Huấn luyện viên sẽ hướng dẫn thực hành cho anh em.",
                "situation": "onsite"
            }
        ],
        "relatedTerms": ["dao-tao-an-toan", "tho-lanh-nghe", "chung-chi-hanh-nghe"]
    },
    {
        "slug": "kiem-dinh-vien",
        "korean": "검정원",
        "vietnamese": "kiểm định viên",
        "hanja": "檢定員",
        "hanjaReading": "檢(검사 검) + 定(정할 정) + 員(인원 원)",
        "pronunciation": "끼엠 딩 비엔",
        "meaningKo": "건설 자재, 구조물, 설비 등의 품질과 안전성을 검사하고 인증하는 전문 인력. 한국에서는 한국건설기술연구원, 한국산업안전보건공단 등 공인 기관의 자격을 갖춘 검정원이 법적으로 요구되는 검사를 수행합니다. 통역 시 주의할 점은 한국의 '검정원'이 공인된 제3자 기관 소속으로 법적 권한과 책임이 명확한 반면, 베트남의 'kiểm định viên'은 때로 발주자나 시공사 내부 인력이 담당하는 경우가 있어 독립성과 공정성에서 차이가 있다는 것입니다. 특히 한국은 용접, 비파괴검사, 승강기, 건설기계 등 분야별로 전문 검정원 자격이 세분화되어 있으므로, 통역 시 어떤 분야의 검정원인지 명확히 해야 합니다.",
        "meaningVi": "Chuyên viên kiểm tra và chứng nhận chất lượng, an toàn của vật liệu xây dựng, kết cấu công trình, và thiết bị. Tại Việt Nam, kiểm định viên thường thuộc các tổ chức kiểm định độc lập (như tổ chức chứng nhận ISO, kiểm định chất lượng công trình) hoặc cơ quan nhà nước (Cục Đăng kiểm). Công việc bao gồm: kiểm tra bê tông, thép, hàn, thang máy, cẩu tháp, và các thiết bị an toàn. Kiểm định viên phải có chứng chỉ chuyên môn và độc lập với nhà thầu thi công để đảm bảo công tâm.",
        "context": "품질 검사, 자재 검수, 안전 인증, 준공 검사 시 사용",
        "culturalNote": "한국의 검정 제도는 매우 체계적이며, 건설기술진흥법, 산업안전보건법 등에 따라 특정 항목(용접, 콘크리트 강도, 승강기 안전 등)은 반드시 공인 검정원의 검사를 받아야 준공이 가능합니다. 검정원은 한국산업인력공단, 한국건설기술연구원 등 공인 기관에서 자격을 부여하며, 검사 결과는 법적 효력을 갖습니다. 베트남도 kiểm định 제도가 있으나, 소규모 프로젝트에서는 자체 검사로 대체되는 경우가 많고, 검정 기관의 독립성이 한국만큼 엄격히 보장되지 않습니다. 한국 기업이 베트남에서 공사 시 한국 수준의 검정을 요구하면 베트남 측이 과도하다고 느끼는 경우가 많으므로, 통역사는 검정의 법적 필요성과 책임 소재를 명확히 설명해야 합니다.",
        "commonMistakes": [
            {
                "mistake": "검정원을 người kiểm tra로 번역",
                "correction": "kiểm định viên (공인 검정원) vs người kiểm tra (일반 검사자)",
                "explanation": "kiểm tra는 일반 검사, kiểm định은 공인 기관의 법적 검정을 의미"
            },
            {
                "mistake": "품질검사원을 kiểm định viên으로 통일",
                "correction": "품질검사원=nhân viên kiểm tra chất lượng, 검정원=kiểm định viên",
                "explanation": "품질검사원은 사내 인력, 검정원은 제3자 공인 인력으로 구분 필요"
            },
            {
                "mistake": "용접 검정을 kiểm tra hàn으로 번역",
                "correction": "kiểm định hàn (UT/RT 등 공인 검정)",
                "explanation": "용접은 법적으로 공인 검정(kiểm định)이 필수이므로 kiểm tra로는 부족"
            }
        ],
        "examples": [
            {
                "ko": "용접 검정원이 비파괴검사 진행합니다.",
                "vi": "Kiểm định viên hàn sẽ thực hiện kiểm tra không phá hủy (UT/RT).",
                "situation": "formal"
            },
            {
                "ko": "콘크리트 강도 검정 결과 나왔어?",
                "vi": "Kết quả kiểm định cường độ bê tông ra chưa?",
                "situation": "onsite"
            },
            {
                "ko": "공인 검정원 없이는 준공 불가능합니다.",
                "vi": "Không thể nghiệm thu nếu không có kiểm định viên được chứng nhận.",
                "situation": "formal"
            }
        ],
        "relatedTerms": ["giam-sat-truong", "ky-su-ket-cau", "dao-tao-an-toan"]
    }
]

def main():
    # 기존 파일 읽기
    with open(file_path, 'r', encoding='utf-8') as f:
        data = json.load(f)  # data는 리스트임

    # 중복 체크
    existing_slugs = {term['slug'] for term in data}

    # 중복 제거
    filtered_new_terms = [term for term in new_terms if term['slug'] not in existing_slugs]

    if not filtered_new_terms:
        print("⚠️  모든 용어가 이미 존재합니다. 추가할 용어가 없습니다.")
        return

    # 새 용어 추가
    data.extend(filtered_new_terms)

    # 파일 저장 (들여쓰기 2칸, 한글 유니코드 보존)
    with open(file_path, 'w', encoding='utf-8') as f:
        json.dump(data, f, ensure_ascii=False, indent=2)

    print(f"✅ {len(filtered_new_terms)}개 용어 추가 완료!")
    print(f"📂 파일 위치: {file_path}")
    print(f"📊 총 용어 수: {len(data)}개")

    # 추가된 용어 목록 출력
    print("\n추가된 용어:")
    for term in filtered_new_terms:
        print(f"  - {term['slug']} ({term['korean']} / {term['vietnamese']})")

if __name__ == "__main__":
    main()
