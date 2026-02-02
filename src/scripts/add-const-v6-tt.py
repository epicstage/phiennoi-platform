#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
건설 용어 추가 스크립트 v6 - 건설노무/인력관리 테마
테마: 일용직, 기능공, 특수공종, 작업반장, 팀장, 소장, 공무, 관리비, 작업허가서, 안전교육
"""

import json
import os

# 추가할 용어 데이터 (Tier S 기준 충족)
data = [
    {
        "slug": "cong-nhan-nhat-cong",
        "korean": "일용직",
        "vietnamese": "Công nhân nhật công",
        "hanja": "日傭職",
        "hanjaReading": "날 일(日) + 품팔이 용(傭) + 직책 직(職)",
        "pronunciation": "이룡직",
        "meaningKo": "하루 단위로 고용되어 일당을 받고 일하는 노동자를 의미합니다. 건설 현장에서는 '일용근로자', '날품팔이'라고도 불립니다. 통역 시 주의할 점은 베트남에서는 '계약 없는 불안정 노동'의 의미가 강하지만, 한국에서는 공식적인 고용 형태 중 하나로 인식된다는 점입니다. 베트남 현장에서는 'công nhân hợp đồng ngắn hạn'(단기계약 노동자)와 구분해 사용해야 합니다. 일용직도 4대보험 가입 대상이며, 근로기준법 보호를 받는다는 점을 명확히 설명해야 오해를 방지할 수 있습니다.",
        "meaningVi": "Lao động được thuê theo ngày và nhận lương theo từng ngày làm việc. Trong công trường xây dựng Hàn Quốc, đây là một hình thức tuyển dụng chính thức, được bảo vệ bởi luật lao động và có thể tham gia bảo hiểm xã hội (4대보험). Cần phân biệt với 'công nhân hợp đồng ngắn hạn' ở Việt Nam. Dù làm theo ngày nhưng vẫn có quyền lợi pháp lý đầy đủ.",
        "context": "건설 현장 인력 관리, 고용 형태, 급여 체계",
        "culturalNote": "한국에서 일용직은 공식적인 고용 형태로 법적 보호를 받지만, 베트남에서는 비공식/불안정 노동의 이미지가 강합니다. 한국 일용직은 4대보험 가입 가능하고 근로기준법 적용 대상이라는 점을 강조해야 합니다. 베트남 통역사들은 '일용직 = 불법 노동'으로 오해할 수 있으므로, '공식 단기 계약직'으로 설명하는 것이 효과적입니다. 또한 한국에서는 일당이 높은 기능공 일용직도 많아 부정적 의미만 있는 것은 아닙니다.",
        "commonMistakes": [
            {
                "mistake": "Công nhân bất hợp pháp (불법 노동자)",
                "correction": "Công nhân nhật công (chính thức) - 일용직(공식)",
                "explanation": "일용직을 불법 노동으로 번역하면 법적 오해 발생. 한국 일용직은 합법적 고용 형태입니다."
            },
            {
                "mistake": "Lao động không có hợp đồng (계약 없는 노동)",
                "correction": "Lao động hợp đồng ngày (일 단위 계약 노동)",
                "explanation": "일용직도 일 단위 근로계약이 존재하며, 법적 보호를 받습니다."
            },
            {
                "mistake": "일용직은 4대보험 가입 불가",
                "correction": "일용직도 4대보험 가입 가능 (조건 충족 시)",
                "explanation": "일정 조건(월 8일 이상 근무 등)을 충족하면 일용직도 사회보험 가입 대상입니다."
            }
        ],
        "examples": [
            {
                "ko": "이번 현장은 일용직 30명, 정규직 10명으로 구성됩니다.",
                "vi": "Công trường này gồm 30 công nhân nhật công và 10 nhân viên chính thức.",
                "situation": "formal"
            },
            {
                "ko": "일용직도 4대보험 들어요. 월 8일 이상 나오면 됩니다.",
                "vi": "Công nhân nhật công cũng có thể tham gia 4대보험. Chỉ cần làm từ 8 ngày/tháng trở lên.",
                "situation": "onsite"
            },
            {
                "ko": "일당 15만원 받는 일용직 미장공 구합니다.",
                "vi": "Tuyển thợ trát công nhật công, lương 150,000원/ngày.",
                "situation": "informal"
            }
        ],
        "relatedTerms": ["상용직", "기능공", "근로계약서", "4대보험"]
    },
    {
        "slug": "tho-co-ky-nang",
        "korean": "기능공",
        "vietnamese": "Thợ có kỹ năng",
        "hanja": "技能工",
        "hanjaReading": "재주 기(技) + 능할 능(能) + 장인 공(工)",
        "pronunciation": "기능공",
        "meaningKo": "특정 분야의 전문 기술과 자격을 갖춘 숙련 노동자를 의미합니다. 건설 현장에서는 '기술자', '기술공'이라고도 불립니다. 통역 시 주의할 점은 단순 노동자(인부)와 명확히 구분해야 하며, 베트남어로 'công nhân phổ thông'(일반 노동자)이 아닌 'thợ có kỹ năng' 또는 'thợ lành nghề'로 번역해야 한다는 점입니다. 기능공은 자격증 보유 여부, 경력, 기술 수준에 따라 임금 차이가 크며, 현장에서 높은 대우를 받습니다. 베트남 통역사들은 기능공과 단순 인부를 혼동하지 않도록 주의해야 합니다.",
        "meaningVi": "Công nhân có tay nghề chuyên môn và trình độ kỹ thuật cao trong lĩnh vực cụ thể. Phân biệt rõ với 'công nhân phổ thông' (thợ thường). Người này thường có chứng chỉ nghề, kinh nghiệm lâu năm và được trả lương cao hơn nhiều so với công nhân thường. Trong công trường Hàn Quốc, 기능공 được tôn trọng và có vị trí quan trọng.",
        "context": "건설 현장 인력 등급, 임금 체계, 기술 자격",
        "culturalNote": "한국 건설 현장에서 기능공은 단순 노동자보다 2~3배 높은 일당을 받으며, 사회적으로도 존중받습니다. 베트남에서도 숙련공이 존재하지만, 한국만큼 명확한 등급 구분과 임금 차이가 없는 경우가 많습니다. 통역 시 '기능공'을 단순히 'công nhân'으로 번역하면 모욕으로 받아들여질 수 있으므로 'thợ lành nghề', 'thợ có tay nghề cao'로 번역해야 합니다. 자격증(산업기사, 기능사 등)을 보유한 경우 임금 협상 시 중요한 요소입니다.",
        "commonMistakes": [
            {
                "mistake": "Công nhân phổ thông (일반 노동자)",
                "correction": "Thợ có kỹ năng / Thợ lành nghề (숙련공/기능공)",
                "explanation": "기능공을 일반 노동자로 번역하면 자격과 기술을 무시하는 것으로 모욕이 될 수 있습니다."
            },
            {
                "mistake": "기능공 = 인부 (같은 의미)",
                "correction": "기능공 ≠ 인부 (기술 수준, 자격, 임금이 다름)",
                "explanation": "기능공은 자격증과 기술을 갖춘 전문가이며, 인부와는 명확히 구분됩니다."
            },
            {
                "mistake": "Thợ (단순 '기술자')",
                "correction": "Thợ lành nghề / Thợ có chứng chỉ (자격증 보유 숙련공)",
                "explanation": "'Thợ'만으로는 기능공의 전문성과 자격을 충분히 표현하지 못합니다."
            }
        ],
        "examples": [
            {
                "ko": "기능공 미장 전문가 일당 25만원입니다.",
                "vi": "Thợ trát có tay nghề cao, lương 250,000원/ngày.",
                "situation": "formal"
            },
            {
                "ko": "기능사 자격증 있으면 기능공으로 인정됩니다.",
                "vi": "Nếu có chứng chỉ 기능사, sẽ được công nhận là thợ có kỹ năng.",
                "situation": "onsite"
            },
            {
                "ko": "기능공이랑 인부는 일당이 두 배 차이 나요.",
                "vi": "Lương thợ lành nghề gấp đôi công nhân phổ thông.",
                "situation": "informal"
            }
        ],
        "relatedTerms": ["산업기사", "기능사", "일용직", "특수공종"]
    },
    {
        "slug": "cong-trinh-dac-biet",
        "korean": "특수공종",
        "vietnamese": "Công trình đặc biệt",
        "hanja": "特殊工種",
        "hanjaReading": "특별할 특(特) + 다를 수(殊) + 장인 공(工) + 씨 종(種)",
        "pronunciation": "특수공종",
        "meaningKo": "일반 건설 작업과 달리 고도의 전문 기술, 특수 장비, 별도 자격증이 필요한 건설 공종을 의미합니다. 비계공, 철근공, 용접공, 도장공, 방수공, 타일공 등이 이에 해당합니다. 통역 시 주의할 점은 베트남어로 'công việc đặc biệt'(특별한 작업)보다는 'công trình chuyên môn'(전문 공종) 또는 'nghề đặc thù'로 번역하는 것이 더 정확하다는 점입니다. 특수공종 기능공은 위험 수당, 기술 수당이 추가되며 일반 인부보다 2~4배 높은 임금을 받습니다. 안전교육과 자격증 보유가 필수입니다.",
        "meaningVi": "Các công việc xây dựng đòi hỏi kỹ năng chuyên môn cao, thiết bị đặc biệt và chứng chỉ riêng. Bao gồm: thợ giàn giáo, thợ hàn, thợ sơn, thợ chống thấm, thợ gạch ốp lát, v.v. Được trả lương cao hơn công nhân thường 2-4 lần do tính chuyên môn và rủi ro cao. Bắt buộc phải có đào tạo an toàn và chứng chỉ nghề.",
        "context": "건설 공종 분류, 기술 자격, 임금 체계, 안전 관리",
        "culturalNote": "한국에서 특수공종은 고임금 직종이며, 숙련공 부족으로 인력난이 심각합니다. 베트남에서도 전문 공종이 존재하지만, 한국만큼 체계적인 자격 시스템과 임금 차등이 없는 경우가 많습니다. 통역 시 '특수공종'을 단순히 'công việc khó'(어려운 작업)로 번역하면 전문성이 무시되므로 'nghề đặc thù có chứng chỉ'(자격증이 필요한 전문 직종)로 설명해야 합니다. 특수공종 기능공은 현장에서 대우가 좋으며, 한국 건설업에서 핵심 인력입니다.",
        "commonMistakes": [
            {
                "mistake": "Công việc khó (어려운 작업)",
                "correction": "Nghề đặc thù / Công trình chuyên môn (전문 공종)",
                "explanation": "특수공종은 난이도가 아니라 전문성과 자격이 핵심입니다."
            },
            {
                "mistake": "특수공종 = 위험 작업만 포함",
                "correction": "특수공종 = 전문 기술 + 자격증 필요 공종 (위험 여부 무관)",
                "explanation": "위험하지 않아도 전문 기술이 필요하면 특수공종입니다(예: 타일공)."
            },
            {
                "mistake": "Công nhân đặc biệt (특별한 노동자)",
                "correction": "Thợ chuyên nghành đặc thù (특수 전문 공종 기술자)",
                "explanation": "'특별한 사람'이 아니라 '전문 분야'를 강조해야 합니다."
            }
        ],
        "examples": [
            {
                "ko": "이 현장은 특수공종 비계공 10명이 필요합니다.",
                "vi": "Công trường này cần 10 thợ giàn giáo (nghề đặc thù).",
                "situation": "formal"
            },
            {
                "ko": "특수공종은 자격증 없으면 작업 못 해요.",
                "vi": "Nghề đặc thù không có chứng chỉ thì không được làm.",
                "situation": "onsite"
            },
            {
                "ko": "용접공은 특수공종이라 일당 30만원입니다.",
                "vi": "Thợ hàn là nghề đặc thù nên lương 300,000원/ngày.",
                "situation": "informal"
            }
        ],
        "relatedTerms": ["기능공", "비계공", "용접공", "안전자격증"]
    },
    {
        "slug": "truong-nhom-thi-cong",
        "korean": "작업반장",
        "vietnamese": "Trưởng nhóm thi công",
        "hanja": "作業班長",
        "hanjaReading": "지을 작(作) + 업 업(業) + 무리 반(班) + 어른 장(長)",
        "pronunciation": "자겁반장",
        "meaningKo": "건설 현장에서 5~15명 정도의 작업팀을 직접 지휘하고 관리하는 현장 리더를 의미합니다. '반장님', '조장'이라고도 불립니다. 통역 시 주의할 점은 작업반장은 단순 감독이 아니라 직접 현장 작업도 함께 수행하며, 팀원들의 작업 지시, 자재 배분, 일정 관리, 안전 책임까지 맡는다는 점입니다. 베트Nam어로 'giám sát viên'(감독관)보다는 'trưởng nhóm'(팀장) 또는 'trưởng tổ'가 더 정확합니다. 작업반장은 팀원보다 일당이 1.5~2배 높으며, 경험과 리더십이 중요한 직책입니다.",
        "meaningVi": "Người quản lý trực tiếp một nhóm 5-15 công nhân tại công trường. Không chỉ giám sát mà còn tham gia làm việc cùng đội, chịu trách nhiệm phân công, quản lý vật liệu, tiến độ và an toàn. Lương cao hơn thành viên nhóm 1.5-2 lần. Cần kinh nghiệm và kỹ năng lãnh đạo.",
        "context": "건설 현장 조직, 인력 관리, 안전 책임",
        "culturalNote": "한국 건설 현장에서 작업반장은 실무 경험이 풍부한 베테랑이 맡으며, 현장 분위기와 생산성을 좌우하는 핵심 인물입니다. 베트Nam에서도 팀장이 있지만, 한국만큼 권한과 책임이 명확하지 않은 경우가 많습니다. 통역 시 작업반장을 'giám sát'(감독)으로 번역하면 사무직 이미지로 오해될 수 있으므로 'trưởng nhóm thi công'(시공 팀장)으로 설명해야 합니다. 작업반장은 안전사고 발생 시 1차 책임자이며, 일일 작업 보고 의무가 있습니다.",
        "commonMistakes": [
            {
                "mistake": "Giám sát viên (감독관/관리자)",
                "correction": "Trưởng nhóm thi công (현장 작업 팀장)",
                "explanation": "작업반장은 사무직 감독이 아니라 현장에서 직접 일하는 실무 리더입니다."
            },
            {
                "mistake": "작업반장 = 관리직 (작업 안 함)",
                "correction": "작업반장 = 작업 + 팀 관리 병행",
                "explanation": "작업반장도 직접 현장 작업에 참여하며, 팀원과 함께 일합니다."
            },
            {
                "mistake": "Người chỉ huy (지휘자/사령관)",
                "correction": "Trưởng tổ thợ (기능공 조장)",
                "explanation": "'지휘자'는 군대식 표현이며, 건설 현장에서는 부적절합니다."
            }
        ],
        "examples": [
            {
                "ko": "이 현장 미장 작업반장은 20년 경력입니다.",
                "vi": "Trưởng nhóm trát tường công trường này có 20 năm kinh nghiệm.",
                "situation": "formal"
            },
            {
                "ko": "반장님, 오늘 작업 지시 부탁드립니다.",
                "vi": "Anh trưởng nhóm, nhờ anh phân công công việc hôm nay.",
                "situation": "onsite"
            },
            {
                "ko": "반장 일당은 20만원, 팀원은 15만원이에요.",
                "vi": "Trưởng nhóm 200,000원/ngày, thành viên 150,000원/ngày.",
                "situation": "informal"
            }
        ],
        "relatedTerms": ["팀장", "소장", "안전관리자", "현장대리인"]
    },
    {
        "slug": "giam-doc-nhom",
        "korean": "팀장",
        "vietnamese": "Giám đốc nhóm",
        "hanja": None,
        "hanjaReading": None,
        "pronunciation": "팀장",
        "meaningKo": "건설 현장에서 여러 작업반을 총괄하거나, 특정 공종 전체를 책임지는 중간 관리자를 의미합니다. '파트장', '공종 책임자'라고도 불립니다. 통역 시 주의할 점은 '팀장'이 작업반장(trưởng nhóm)보다 상위 직책이며, 직접 작업보다는 관리 업무 비중이 높다는 점입니다. 베트Nam어로 'trưởng phòng'(부서장)보다는 'giám đốc nhóm' 또는 'quản lý công trình'(공사 관리자)가 적절합니다. 팀장은 작업 계획, 인력 배치, 자재 관리, 품질 관리, 공정 관리까지 담당하며, 현장소장과 작업반장 사이에서 조율 역할을 합니다.",
        "meaningVi": "Quản lý cấp trung gian, chịu trách nhiệm nhiều nhóm thi công hoặc toàn bộ một công đoạn. Cao hơn trưởng nhóm (작업반장), tập trung vào quản lý hơn là thi công trực tiếp. Đảm nhận: lập kế hoạch, phân bổ nhân lực, quản lý vật liệu, chất lượng, tiến độ. Là cầu nối giữa 소장 (giám đốc công trường) và 작업반장 (trưởng nhóm).",
        "context": "건설 현장 조직도, 중간 관리, 공종 책임",
        "culturalNote": "한국 건설 현장의 팀장은 사무직과 현장직의 중간 위치로, 베트Nam의 'kỹ sư công trường'(현장 엔지니어)와 유사한 역할입니다. 다만 한국 팀장은 기술보다 관리 능력이 더 중요하며, 현장 경험이 풍부한 실무자가 승진하는 경우가 많습니다. 통역 시 '팀장'을 단순히 'trưởng nhóm'으로 번역하면 작업반장과 혼동되므로, 직급과 역할 범위를 명확히 구분해야 합니다. 팀장은 여러 반을 관리하며, 현장소장의 지시를 실행하는 핵심 인력입니다.",
        "commonMistakes": [
            {
                "mistake": "Trưởng nhóm (작업반장과 동일)",
                "correction": "Giám đốc nhóm / Quản lý công trình (여러 팀 총괄)",
                "explanation": "팀장은 작업반장보다 상위 직책이며, 여러 반을 관리합니다."
            },
            {
                "mistake": "팀장 = 현장소장 (같은 의미)",
                "correction": "팀장 < 현장소장 (팀장은 중간 관리자)",
                "explanation": "팀장은 현장소장 아래에서 특정 공종 또는 구역을 담당합니다."
            },
            {
                "mistake": "Kỹ sư trưởng (수석 엔지니어)",
                "correction": "Quản lý thi công (시공 관리자)",
                "explanation": "팀장은 엔지니어가 아니라 현장 관리자입니다."
            }
        ],
        "examples": [
            {
                "ko": "토목 팀장님이 전체 토공 작업을 관리합니다.",
                "vi": "Giám đốc nhóm thổ mộc quản lý toàn bộ công tác đào đắp.",
                "situation": "formal"
            },
            {
                "ko": "팀장님, 이번 주 작업 계획 검토 부탁드립니다.",
                "vi": "Anh quản lý, nhờ anh kiểm tra kế hoạch thi công tuần này.",
                "situation": "onsite"
            },
            {
                "ko": "팀장은 3개 반을 총괄하고 있어요.",
                "vi": "Giám đốc nhóm đang quản lý 3 nhóm thi công.",
                "situation": "informal"
            }
        ],
        "relatedTerms": ["작업반장", "소장", "현장대리인", "공종책임자"]
    },
    {
        "slug": "giam-doc-cong-truong",
        "korean": "소장",
        "vietnamese": "Giám đốc công trường",
        "hanja": "所長",
        "hanjaReading": "바 소(所) + 어른 장(長)",
        "pronunciation": "소장",
        "meaningKo": "건설 현장 전체를 책임지고 총괄하는 최고 책임자를 의미합니다. '현장소장', '공사소장'이라고도 불립니다. 통역 시 주의할 점은 소장이 단순 관리자가 아니라 현장의 모든 공사, 안전, 품질, 인력, 예산, 일정을 책임지는 최고 의사결정권자라는 점입니다. 베트Nam어로 'giám đốc công trường' 또는 'chủ nhiệm công trường'으로 번역합니다. 소장은 건설사 본사와 현장을 연결하는 핵심 인물이며, 발주처(건축주)와의 협의, 하도급업체 관리, 안전사고 책임까지 모두 담당합니다. 소장의 결정은 현장에서 절대적입니다.",
        "meaningVi": "Giám đốc điều hành toàn bộ công trường, người chịu trách nhiệm cao nhất về thi công, an toàn, chất lượng, nhân sự, ngân sách, tiến độ. Là cầu nối giữa công ty xây dựng và công trường, đàm phán với chủ đầu tư, quản lý các nhà thầu phụ. Quyết định của 소장 có tính tuyệt đối tại công trường.",
        "context": "건설 현장 최고 책임자, 조직도 정점, 의사결정권",
        "culturalNote": "한국 건설 현장에서 소장은 '왕'과 같은 존재로, 모든 현장 직원이 소장의 지시를 따릅니다. 베트Nam에서도 'giám đốc công trường'이 존재하지만, 한국만큼 절대적 권한과 책임을 갖는 경우는 드뭅니다. 통역 시 소장을 'quản lý'(관리자)로 번역하면 권한이 축소되므로 'giám đốc'(이사/사장급)로 표현해야 합니다. 소장은 안전사고 발생 시 형사 책임까지 질 수 있으며, 현장 운영의 모든 권한과 책임을 집니다. 소장과의 대화 시 존댓말 사용이 필수입니다.",
        "commonMistakes": [
            {
                "mistake": "Quản lý công trường (현장 관리자)",
                "correction": "Giám đốc công trường (현장 최고 책임자)",
                "explanation": "소장은 관리자가 아니라 최고 의사결정권자입니다."
            },
            {
                "mistake": "소장 = 팀장 (같은 의미)",
                "correction": "소장 >> 팀장 (소장은 전체 총괄, 팀장은 일부 담당)",
                "explanation": "소장은 현장 전체를 책임지며, 팀장은 소장 아래에서 특정 공종을 담당합니다."
            },
            {
                "mistake": "Trưởng công trình (공사 책임자)",
                "correction": "Giám đốc điều hành (운영 이사급)",
                "explanation": "소장은 단순 책임자가 아니라 이사급 권한을 가진 최고 경영자입니다."
            }
        ],
        "examples": [
            {
                "ko": "소장님께서 내일 안전 점검 실시하신다고 하셨습니다.",
                "vi": "Giám đốc công trường cho biết sẽ tiến hành kiểm tra an toàn ngày mai.",
                "situation": "formal"
            },
            {
                "ko": "소장님, 자재 납품이 지연되고 있습니다.",
                "vi": "Giám đốc, vật liệu đang bị chậm giao.",
                "situation": "onsite"
            },
            {
                "ko": "이 현장 소장은 30년 경력이야.",
                "vi": "Giám đốc công trường này có 30 năm kinh nghiệm.",
                "situation": "informal"
            }
        ],
        "relatedTerms": ["현장대리인", "팀장", "안전관리자", "건설사"]
    },
    {
        "slug": "quan-ly-cong-vu",
        "korean": "공무",
        "vietnamese": "Quản lý công vụ",
        "hanja": "工務",
        "hanjaReading": "장인 공(工) + 일 무(務)",
        "pronunciation": "공무",
        "meaningKo": "건설 현장에서 공사 진행 상황을 관리하고, 도면 검토, 자재 발주, 공정 관리, 협력업체 조율 등의 사무 및 기술 업무를 담당하는 직무를 의미합니다. '공무팀', '공무담당'이라고도 불립니다. 통역 시 주의할 점은 공무가 단순 사무직이 아니라 기술 지식과 현장 경험이 필요한 전문직이라는 점입니다. 베트Nam어로 'hành chính'(행정)이 아니라 'quản lý kỹ thuật công trình'(공사 기술 관리) 또는 'công vụ kỹ thuật'로 번역해야 합니다. 공무 담당자는 설계 변경, 시공 계획 수립, 품질 관리 기준 설정 등 현장의 두뇌 역할을 합니다.",
        "meaningVi": "Bộ phận quản lý kỹ thuật và hành chính công trường: rà soát bản vẽ, đặt hàng vật liệu, quản lý tiến độ, điều phối nhà thầu phụ. Không phải chỉ văn phòng mà cần kiến thức kỹ thuật và kinh nghiệm công trường. Đóng vai trò 'bộ não' của công trường: thay đổi thiết kế, lập kế hoạch thi công, thiết lập tiêu chuẩn chất lượng.",
        "context": "건설 현장 사무직, 기술 관리, 공정 관리",
        "culturalNote": "한국 건설 현장에서 공무팀은 소장 다음으로 중요한 의사결정 부서이며, 현장 엔지니어와 행정 역할을 동시에 수행합니다. 베트Nam에서는 기술부서(kỹ thuật)와 행정부서(hành chính)가 분리되는 경우가 많지만, 한국은 공무팀이 두 역할을 통합합니다. 통역 시 공무를 'hành chính'(행정)으로 번역하면 단순 사무직으로 오해되므로, 'quản lý kỹ thuật công trình'(공사 기술 관리)로 설명해야 합니다. 공무 담당자는 건축/토목 전공자가 많으며, 설계 변경과 시공 계획 수립 권한을 갖습니다.",
        "commonMistakes": [
            {
                "mistake": "Hành chính (행정/사무)",
                "correction": "Quản lý kỹ thuật công trình (기술 관리)",
                "explanation": "공무는 단순 행정이 아니라 기술과 관리를 통합한 전문 직무입니다."
            },
            {
                "mistake": "공무 = 공무원 (공무원과 혼동)",
                "correction": "공무 = 공사 관리 업무 (건설 직무)",
                "explanation": "공무원(công chức)이 아니라 건설 현장의 기술 관리 직무입니다."
            },
            {
                "mistake": "Văn phòng công trường (현장 사무실)",
                "correction": "Bộ phận quản lý kỹ thuật (기술 관리 부서)",
                "explanation": "공무는 장소가 아니라 직무/부서를 의미합니다."
            }
        ],
        "examples": [
            {
                "ko": "공무팀에서 설계 변경 검토 중입니다.",
                "vi": "Bộ phận công vụ đang xem xét thay đổi thiết kế.",
                "situation": "formal"
            },
            {
                "ko": "공무 담당자한테 자재 발주 확인 부탁하세요.",
                "vi": "Nhờ người phụ trách công vụ xác nhận đặt hàng vật liệu.",
                "situation": "onsite"
            },
            {
                "ko": "공무팀이 공정표 짜고 있어요.",
                "vi": "Đội công vụ đang lập biểu đồ tiến độ.",
                "situation": "informal"
            }
        ],
        "relatedTerms": ["공정관리", "설계변경", "현장대리인", "시공계획"]
    },
    {
        "slug": "chi-phi-quan-ly",
        "korean": "관리비",
        "vietnamese": "Chi phí quản lý",
        "hanja": "管理費",
        "hanjaReading": "대롱 관(管) + 다스릴 리(理) + 쓸 비(費)",
        "pronunciation": "관리비",
        "meaningKo": "건설 공사에서 직접 공사비 외에 현장 운영, 인건비, 사무실 유지, 안전 관리 등을 위해 필요한 간접 비용을 의미합니다. '일반관리비', '현장경비'라고도 불립니다. 통역 시 주의할 점은 관리비가 아파트 관리비(maintenance fee)와 완전히 다른 개념이며, 건설 원가의 일부라는 점입니다. 베트Nam어로 'phí quản lý chung cư'(아파트 관리비)가 아니라 'chi phí quản lý công trình'(공사 관리 비용)으로 번역해야 합니다. 관리비는 직접공사비의 5~15% 정도이며, 현장 소장 인건비, 안전관리자 급여, 현장 사무실 운영비, 안전시설 비용 등이 포함됩니다.",
        "meaningVi": "Chi phí gián tiếp ngoài chi phí thi công trực tiếp, dùng cho vận hành công trường, nhân sự, văn phòng, quản lý an toàn. Chiếm 5-15% tổng chi phí thi công trực tiếp. Bao gồm: lương giám đốc công trường, lương quản lý an toàn, văn phòng hiện trường, thiết bị an toàn. Khác hoàn toàn với 'phí quản lý chung cư'.",
        "context": "건설 원가 구성, 공사비 산정, 계약 조건",
        "culturalNote": "한국 건설업에서 관리비는 공사 원가의 필수 항목이며, 발주처와 계약 시 명확히 명시됩니다. 베트Nam에서도 관리비가 존재하지만, 한국만큼 세부 항목이 체계화되지 않은 경우가 많습니다. 통역 시 '관리비'를 아파트 관리비로 오해하는 경우가 많으므로, 'chi phí quản lý công trình'(공사 관리비) 또는 'chi phí gián tiếp'(간접비)로 명확히 구분해야 합니다. 관리비에는 현장 운영에 필요한 모든 간접비가 포함되며, 안전관리비도 관리비의 일부입니다.",
        "commonMistakes": [
            {
                "mistake": "Phí quản lý chung cư (아파트 관리비)",
                "correction": "Chi phí quản lý công trình (공사 관리비)",
                "explanation": "건설 공사비의 관리비와 아파트 입주 후 관리비는 완전히 다릅니다."
            },
            {
                "mistake": "관리비 = 소장 급여만 포함",
                "correction": "관리비 = 현장 운영 전체 간접비 (인건비, 사무실, 안전 등)",
                "explanation": "관리비는 소장 급여 외에도 모든 간접 운영비를 포함합니다."
            },
            {
                "mistake": "Chi phí bảo trì (유지보수 비용)",
                "correction": "Chi phí quản lý hiện trường (현장 관리 비용)",
                "explanation": "보수비가 아니라 공사 기간 중 현장 운영비입니다."
            }
        ],
        "examples": [
            {
                "ko": "이번 공사 관리비는 직접공사비의 10%입니다.",
                "vi": "Chi phí quản lý công trình này là 10% chi phí thi công trực tiếp.",
                "situation": "formal"
            },
            {
                "ko": "관리비에 안전관리자 인건비도 포함돼요.",
                "vi": "Chi phí quản lý bao gồm cả lương quản lý an toàn.",
                "situation": "onsite"
            },
            {
                "ko": "관리비 빼면 실제 공사비는 얼마야?",
                "vi": "Trừ chi phí quản lý thì chi phí thi công thực tế là bao nhiêu?",
                "situation": "informal"
            }
        ],
        "relatedTerms": ["직접공사비", "간접비", "안전관리비", "공사원가"]
    },
    {
        "slug": "giay-phep-lam-viec",
        "korean": "작업허가서",
        "vietnamese": "Giấy phép làm việc",
        "hanja": "作業許可書",
        "hanjaReading": "지을 작(作) + 업 업(業) + 허락할 허(許) + 옳을 가(可) + 글 서(書)",
        "pronunciation": "자겁허가서",
        "meaningKo": "건설 현장에서 위험 작업(고소 작업, 밀폐 공간, 화기 작업, 중장비 등)을 수행하기 전에 안전 검토와 승인을 받아 발급하는 공식 문서를 의미합니다. '작업지시서', 'Work Permit'라고도 불립니다. 통역 시 주의할 점은 작업허가서가 단순 서류가 아니라 안전사고 예방을 위한 법적 의무 문서이며, 허가 없이 위험 작업 시 작업 중단 및 처벌 대상이 된다는 점입니다. 베트Nam어로 'giấy phép' 또는 'giấy cho phép làm việc'로 번역하며, 작업 전 반드시 소장 또는 안전관리자의 승인이 필요합니다. 작업허가서에는 작업 내용, 위험 요소, 안전 대책, 책임자, 작업 시간 등이 명시됩니다.",
        "meaningVi": "Văn bản chính thức phải được phê duyệt trước khi thực hiện các công việc nguy hiểm (làm việc trên cao, không gian kín, dùng lửa, máy móc hạng nặng). Không phải chỉ là giấy tờ mà là nghĩa vụ pháp lý để phòng ngừa tai nạn. Làm việc nguy hiểm không có phép sẽ bị dừng công việc và xử phạt. Cần phê duyệt của 소장 hoặc quản lý an toàn. Ghi rõ: nội dung, yếu tố nguy hiểm, biện pháp an toàn, người chịu trách nhiệm, thời gian.",
        "context": "건설 안전 관리, 위험 작업, 법적 의무",
        "culturalNote": "한국 건설 현장에서 작업허가서는 중대재해처벌법 이후 더욱 엄격히 적용되며, 위반 시 현장 소장과 안전관리자가 형사 처벌을 받을 수 있습니다. 베트Nam에서도 안전 허가가 존재하지만, 한국만큼 엄격하게 시행되지 않는 경우가 많습니다. 통역 시 작업허가서를 단순히 'giấy cho phép'으로만 번역하면 중요성이 전달되지 않으므로, 'văn bản pháp lý bắt buộc'(법적 의무 문서)임을 강조해야 합니다. 작업허가서 없이 작업 시 즉시 중단되며, 재발 시 퇴출될 수 있습니다.",
        "commonMistakes": [
            {
                "mistake": "Giấy đăng ký (등록증)",
                "correction": "Giấy phép an toàn (안전 허가서)",
                "explanation": "작업허가서는 등록이 아니라 안전 승인 문서입니다."
            },
            {
                "mistake": "작업허가서 = 선택 사항",
                "correction": "작업허가서 = 법적 의무 (위반 시 처벌)",
                "explanation": "위험 작업 시 작업허가서는 법적 필수이며, 위반 시 형사 처벌 대상입니다."
            },
            {
                "mistake": "Hướng dẫn công việc (작업 안내서)",
                "correction": "Giấy phép làm việc (작업 허가서)",
                "explanation": "안내서가 아니라 공식 승인 문서입니다."
            }
        ],
        "examples": [
            {
                "ko": "고소 작업 전 작업허가서를 반드시 제출하십시오.",
                "vi": "Trước khi làm việc trên cao, bắt buộc phải nộp giấy phép làm việc.",
                "situation": "formal"
            },
            {
                "ko": "허가서 없으면 작업 못 시작해요.",
                "vi": "Không có giấy phép thì không được bắt đầu làm.",
                "situation": "onsite"
            },
            {
                "ko": "용접 작업 허가서 소장님한테 받았어?",
                "vi": "Giấy phép hàn đã xin giám đốc chưa?",
                "situation": "informal"
            }
        ],
        "relatedTerms": ["안전교육", "위험작업", "안전관리자", "중대재해처벌법"]
    },
    {
        "slug": "dao-tao-an-toan",
        "korean": "안전교육",
        "vietnamese": "Đào tạo an toàn",
        "hanja": "安全敎育",
        "hanjaReading": "편안할 안(安) + 온전할 전(全) + 가르칠 교(敎) + 기를 육(育)",
        "pronunciation": "안전교육",
        "meaningKo": "건설 현장에서 근로자들이 작업 전 반드시 받아야 하는 안전 사고 예방 교육을 의미합니다. '안전 교육', '안전 훈련'이라고도 불립니다. 통역 시 주의할 점은 안전교육이 법적 의무이며, 교육 미이수 시 현장 출입이 금지된다는 점입니다. 베트Nam어로 'đào tạo an toàn' 또는 'giáo dục an toàn'으로 번역하며, 신규 근로자는 최소 2시간, 기존 근로자는 월 2시간 이상 의무입니다. 안전교육에는 추락 방지, 화재 대응, 장비 안전, 개인보호구 착용, 응급처치 등이 포함되며, 교육 이수 확인서를 발급받아야 작업이 가능합니다.",
        "meaningVi": "Khóa đào tạo phòng ngừa tai nạn lao động bắt buộc trước khi làm việc tại công trường. Là nghĩa vụ pháp lý - không hoàn thành không được vào công trường. Công nhân mới: tối thiểu 2 giờ; công nhân hiện tại: tối thiểu 2 giờ/tháng. Nội dung: phòng ngừa rơi, ứng phó cháy nổ, an toàn thiết bị, đeo đồ bảo hộ, sơ cứu. Phải có giấy xác nhận hoàn thành mới được làm việc.",
        "context": "건설 안전 관리, 법적 의무, 현장 출입 자격",
        "culturalNote": "한국 건설 현장에서 안전교육은 중대재해처벌법 시행 이후 매우 엄격히 적용되며, 교육 미이수 시 현장 출입이 즉시 차단됩니다. 베트Nam에서도 안전교육이 있지만, 한국만큼 체계적이고 강제적이지 않은 경우가 많습니다. 통역 시 '안전교육'을 단순히 'hội thảo an toàn'(안전 세미나)으로 번역하면 중요성이 약화되므로, 'đào tạo bắt buộc'(의무 교육)임을 강조해야 합니다. 교육 시간을 근무 시간으로 인정하며, 교육비는 회사 부담입니다. 교육 불참 시 임금 삭감 및 퇴출 사유가 될 수 있습니다.",
        "commonMistakes": [
            {
                "mistake": "Hội thảo an toàn (안전 세미나)",
                "correction": "Đào tạo an toàn bắt buộc (의무 안전교육)",
                "explanation": "세미나가 아니라 법적 의무 교육이며, 불참 시 처벌됩니다."
            },
            {
                "mistake": "안전교육 = 선택 참여",
                "correction": "안전교육 = 필수 (불참 시 출입 금지)",
                "explanation": "안전교육은 법적 필수이며, 미이수 시 현장 출입이 차단됩니다."
            },
            {
                "mistake": "Thông báo an toàn (안전 안내)",
                "correction": "Đào tạo chính thức (공식 교육)",
                "explanation": "단순 안내가 아니라 공식 교육 프로그램입니다."
            }
        ],
        "examples": [
            {
                "ko": "신규 근로자는 2시간 안전교육 이수 필수입니다.",
                "vi": "Công nhân mới bắt buộc phải hoàn thành 2 giờ đào tạo an toàn.",
                "situation": "formal"
            },
            {
                "ko": "안전교육 안 들으면 현장 못 들어와요.",
                "vi": "Không nghe đào tạo an toàn thì không được vào công trường.",
                "situation": "onsite"
            },
            {
                "ko": "내일 오전 안전교육 있으니까 8시까지 오세요.",
                "vi": "Sáng mai có đào tạo an toàn, đến trước 8 giờ nhé.",
                "situation": "informal"
            }
        ],
        "relatedTerms": ["안전관리자", "개인보호구", "작업허가서", "중대재해처벌법"]
    }
]

# 파일 경로
file_path = os.path.join(
    os.path.dirname(__file__),
    "..",
    "data",
    "terms",
    "construction.json"
)

# 기존 데이터 읽기
with open(file_path, "r", encoding="utf-8") as f:
    existing_data = json.load(f)

# 새 데이터 추가
existing_data.extend(data)

# 파일 저장
with open(file_path, "w", encoding="utf-8") as f:
    json.dump(existing_data, f, ensure_ascii=False, indent=2)

print(f"✅ 건설 용어 {len(data)}개 추가 완료")
print(f"📂 파일: {file_path}")
print(f"📊 총 용어 수: {len(existing_data)}개")
