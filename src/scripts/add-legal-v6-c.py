#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""국제인권법 용어 추가 스크립트 (v6-c)"""

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
            "slug": "tuyen-ngon-nhan-quyen",
            "korean": "인권선언",
            "vietnamese": "Tuyên ngôn nhân quyền",
            "hanja": "人權宣言",
            "hanjaReading": "人(사람 인) + 權(권세 권) + 宣(베풀 선) + 言(말씀 언)",
            "pronunciation": "인꿘선언",
            "meaningKo": "모든 인간의 기본적 권리와 자유를 천명한 국제적 선언문으로, 가장 대표적인 것은 1948년 UN 세계인권선언입니다. 통역 시 베트남어 'tuyên ngôn'은 '선언'이라는 공식적 의미가 강하므로, 단순 성명(tuyên bố)과 혼동하지 않도록 주의해야 합니다. 한국에서는 세계인권선언을 '인권선언'으로 줄여 말하는 경우가 많지만, 베트남에서는 정식 명칭을 선호하므로 통역 시 맥락에 따라 'Tuyên ngôn Quốc tế Nhân quyền' 또는 'Tuyên ngôn Nhân quyền Thế giới'로 완전히 표현하는 것이 안전합니다.",
            "meaningVi": "Văn kiện chính thức công bố các quyền cơ bản và tự do của con người, nổi tiếng nhất là Tuyên ngôn Quốc tế Nhân quyền năm 1948 của Liên Hợp Quốc. Đây là nền tảng pháp lý quốc tế bảo vệ nhân quyền toàn cầu.",
            "context": "국제법, 인권법, UN 문서, 조약 협상",
            "culturalNote": "한국은 1948년 세계인권선언 채택에 참여했으며, 헌법에 인권 보장이 명시되어 있습니다. 베트남은 1982년 UN 가입 이후 인권 관련 국제조약에 서명했으나, 사회주의 체제 특성상 집단권과 개인권의 균형을 강조하는 경향이 있습니다. 통역 시 양국의 인권 개념 차이(개인주의 vs 집단주의)를 이해하고, 민감한 정치적 표현은 중립적으로 전달해야 합니다.",
            "commonMistakes": [
                {
                    "mistake": "'선언'을 'tuyên bố'로 번역",
                    "correction": "'tuyên ngôn'으로 번역",
                    "explanation": "tuyên bố는 일반적인 성명이나 발표를 의미하고, tuyên ngôn은 공식적이고 역사적 의미가 있는 선언문을 뜻합니다. 인권선언처럼 중요한 문서는 반드시 tuyên ngôn을 사용해야 합니다."
                },
                {
                    "mistake": "'세계인권선언'을 단순히 'Nhân quyền thế giới'로 번역",
                    "correction": "'Tuyên ngôn Quốc tế Nhân quyền' 또는 'Tuyên ngôn Nhân quyền Thế giới'",
                    "explanation": "정식 문서명이므로 'tuyên ngôn'을 반드시 포함해야 하며, 베트남에서는 'Quốc tế'(국제)를 'Thế giới'(세계)보다 더 많이 사용합니다."
                },
                {
                    "mistake": "'인권'을 'quyền con người'로만 번역",
                    "correction": "문맥에 따라 'nhân quyền' 또는 'quyền con người'",
                    "explanation": "공식 문서나 법률 용어는 'nhân quyền'(한자어 기원), 일상 대화는 'quyền con người'(순수 베트남어)를 사용하는 것이 자연스럽습니다."
                }
            ],
            "examples": [
                {
                    "ko": "한국은 세계인권선언의 원칙을 헌법에 반영하고 있습니다.",
                    "vi": "Hàn Quốc đã phản ánh các nguyên tắc của Tuyên ngôn Quốc tế Nhân quyền vào Hiến pháp.",
                    "situation": "formal"
                },
                {
                    "ko": "이번 협약은 인권선언의 정신을 계승합니다.",
                    "vi": "Công ước này kế thừa tinh thần của Tuyên ngôn Nhân quyền.",
                    "situation": "formal"
                },
                {
                    "ko": "인권선언 제1조는 모든 인간의 존엄과 평등을 명시합니다.",
                    "vi": "Điều 1 của Tuyên ngôn Nhân quyền nêu rõ phẩm giá và bình đẳng của mọi con người.",
                    "situation": "formal"
                }
            ],
            "relatedTerms": ["인권협약", "기본권", "자유권", "사회권"]
        },
        {
            "slug": "cong-uoc-nan-dan",
            "korean": "난민협약",
            "vietnamese": "Công ước난dân",
            "hanja": "難民協約",
            "hanjaReading": "難(어려울 난) + 民(백성 민) + 協(화합할 협) + 約(약속할 약)",
            "pronunciation": "난민협약",
            "meaningKo": "전쟁, 박해, 재난 등으로 자국을 떠나 보호를 요청하는 난민의 지위와 권리를 규정한 1951년 UN 협약입니다. 통역 시 '난민'과 '이주민'을 구분해야 하며, 베트남어 'người tị nạn'(난민)과 'người di cư'(이주민)는 법적 지위가 전혀 다릅니다. 한국은 1992년 난민협약에 가입했고, 베트남은 아직 가입하지 않았으나 UNHCR과 협력하고 있습니다. 통역 시 양국의 난민 정책 차이를 이해하고, '난민 인정'과 '인도적 체류' 등 법적 용어를 정확히 구분해야 합니다.",
            "meaningVi": "Công ước của Liên Hợp Quốc năm 1951 quy định về địa vị và quyền lợi của người tị nạn, những người phải rời bỏ đất nước vì chiến tranh, bị bách hại hoặc thảm họa. Đây là văn kiện pháp lý quốc tế quan trọng bảo vệ người tị nạn.",
            "context": "이민법, 인도주의, 국제난민법, 인권 보호",
            "culturalNote": "한국은 2013년 난민법을 제정하여 아시아 최초로 독립된 난민법을 갖춘 국가가 되었으나, 실제 난민 인정률은 낮은 편입니다. 베트남은 과거 보트피플 사태로 난민을 대량 배출한 역사가 있어 난민 문제에 민감하며, 현재는 국제사회의 난민 수용 요청에 제한적으로 응하고 있습니다. 통역 시 베트남 전쟁 역사와 연결된 표현은 주의가 필요합니다.",
            "commonMistakes": [
                {
                    "mistake": "'난민'을 'người nhập cư'로 번역",
                    "correction": "'người tị nạn'으로 번역",
                    "explanation": "người nhập cư는 단순 이민자를 뜻하고, người tị nạn은 법적 보호를 받는 난민을 의미합니다. 법적 지위가 완전히 다르므로 혼동하면 안 됩니다."
                },
                {
                    "mistake": "'협약'을 'hiệp định'으로 번역",
                    "correction": "'công ước'으로 번역",
                    "explanation": "난민협약처럼 다자간 국제조약은 'công ước'을 사용하고, 양자 조약은 'hiệp định'을 사용합니다."
                },
                {
                    "mistake": "'난민 신청자'를 'người xin tị nạn'로만 번역",
                    "correction": "'người xin tị nạn' 또는 'người đăng ký tị nạn'",
                    "explanation": "공식 문서에서는 'đăng ký'(등록)가 더 정확하며, 'xin'(요청)은 구어체에 가깝습니다."
                }
            ],
            "examples": [
                {
                    "ko": "한국은 난민협약에 따라 난민 심사 절차를 운영하고 있습니다.",
                    "vi": "Hàn Quốc đang vận hành thủ tục thẩm định người tị nạn theo Công ước Nan dân.",
                    "situation": "formal"
                },
                {
                    "ko": "이 사건은 난민협약 제33조 강제송환금지 원칙에 위배됩니다.",
                    "vi": "Vụ việc này vi phạm nguyên tắc cấm trục xuất cưỡng bức theo Điều 33 Công ước Nan dân.",
                    "situation": "formal"
                },
                {
                    "ko": "난민 지위 인정 여부는 난민협약에 근거하여 판단합니다.",
                    "vi": "Việc công nhận địa vị người tị nạn được xét dựa trên Công ước Nan dân.",
                    "situation": "formal"
                }
            ],
            "relatedTerms": ["난민법", "인도적체류", "강제송환금지", "박해"]
        },
        {
            "slug": "cong-uoc-chong-tra-tan",
            "korean": "고문방지협약",
            "vietnamese": "Công ước chống tra tấn",
            "hanja": "拷問防止協約",
            "hanjaReading": "拷(칠 고) + 問(물을 문) + 防(막을 방) + 止(그칠 지) + 協(화합할 협) + 約(약속할 약)",
            "pronunciation": "고문방지협약",
            "meaningKo": "고문 및 그 밖의 잔혹하고 비인도적인 처우나 처벌을 금지하는 1984년 UN 협약입니다. 통역 시 '고문'(tra tấn)과 '가혹행위'(hành vi tàn bạo)를 명확히 구분해야 하며, 법적 정의가 다릅니다. 한국은 1995년 비준했으며, 베트남은 2015년 가입했습니다. 통역 시 '고문'이라는 용어가 정치적으로 민감할 수 있으므로, 공식 회의에서는 협약의 정식 명칭을 사용하고, 구체적 사례 통역 시에는 중립적 표현을 유지해야 합니다. 특히 군사, 경찰 관련 맥락에서는 더욱 주의가 필요합니다.",
            "meaningVi": "Công ước của Liên Hợp Quốc năm 1984 cấm tra tấn và các hình thức đối xử hoặc trừng phạt tàn bạo, vô nhân đạo khác. Đây là công cụ pháp lý quốc tế quan trọng bảo vệ phẩm giá con người.",
            "context": "형사법, 인권법, 구금시설, 수사 절차",
            "culturalNote": "한국은 민주화 이후 고문 관련 과거사 정리 작업을 진행했으며, 현재는 고문 금지가 엄격히 시행됩니다. 베트남은 형사소송법에 고문 금지 조항을 두고 있으나, 실제 수사 과정에서의 인권 보호 수준은 개선 중입니다. 통역 시 '고문'이라는 표현이 상대국 정부를 비판하는 것으로 오해받지 않도록, 협약의 보편적 원칙을 강조하는 방식으로 전달하는 것이 안전합니다.",
            "commonMistakes": [
                {
                    "mistake": "'고문'을 'tra hỏi'로 번역",
                    "correction": "'tra tấn'으로 번역",
                    "explanation": "tra hỏi는 단순 심문/조사를 의미하고, tra tấn은 신체적·정신적 고통을 가하는 고문을 뜻합니다. 법적 의미가 완전히 다릅니다."
                },
                {
                    "mistake": "'방지'를 'phòng ngừa'로만 번역",
                    "correction": "'chống' 또는 'phòng chống'",
                    "explanation": "고문방지협약의 공식 명칭은 'chống tra tấn'을 사용하며, 'phòng ngừa'는 예방의 의미가 강합니다. 'chống'은 적극적 대항의 뉘앙스입니다."
                },
                {
                    "mistake": "'가혹행위'를 'tra tấn'으로 번역",
                    "correction": "'hành vi tàn bạo' 또는 'đối xử tàn nhẫn'",
                    "explanation": "가혹행위는 고문보다 넓은 개념으로, 모든 가혹행위가 법적 고문은 아닙니다. 협약에서는 이 둘을 구분하므로 정확한 번역이 중요합니다."
                }
            ],
            "examples": [
                {
                    "ko": "수사 과정에서 고문방지협약의 원칙을 준수해야 합니다.",
                    "vi": "Trong quá trình điều tra phải tuân thủ các nguyên tắc của Công ước chống tra tấn.",
                    "situation": "formal"
                },
                {
                    "ko": "이 사건은 고문방지협약 제3조 강제송환금지 의무와 관련이 있습니다.",
                    "vi": "Vụ việc này liên quan đến nghĩa vụ cấm trục xuất cưỡng bức theo Điều 3 Công ước chống tra tấn.",
                    "situation": "formal"
                },
                {
                    "ko": "구금시설은 고문방지협약에 따라 정기적으로 감독받습니다.",
                    "vi": "Các cơ sở giam giữ được giám sát định kỳ theo Công ước chống tra tấn.",
                    "situation": "formal"
                }
            ],
            "relatedTerms": ["인권침해", "가혹행위", "강제자백", "구금"]
        },
        {
            "slug": "cong-uoc-xoa-bo-ky-thi-chung-toc",
            "korean": "인종차별철폐협약",
            "vietnamese": "Công ước xóa bỏ kỳ thị chủng tộc",
            "hanja": "人種差別撤廢協約",
            "hanjaReading": "人(사람 인) + 種(씨 종) + 差(다를 차) + 別(나눌 별) + 撤(걷을 철) + 廢(폐할 폐) + 協(화합할 협) + 約(약속할 약)",
            "pronunciation": "인종차별철폐협약",
            "meaningKo": "모든 형태의 인종차별을 없애기 위한 1965년 UN 협약으로, 피부색, 혈통, 민족 등에 따른 차별을 금지합니다. 통역 시 '인종'(chủng tộc)과 '민족'(dân tộc)을 구분해야 하며, 베트남어에서 'dân tộc'은 국내 소수민족을 주로 지칭하고 'chủng tộc'은 국제적 인종 개념에 가깝습니다. 한국은 단일민족 의식이 강했으나 다문화 사회로 전환 중이며, 베트남은 54개 민족으로 구성된 다민족 국가입니다. 통역 시 '차별'과 '구별'의 차이, '적극적 우대조치'(affirmative action) 등의 개념을 정확히 전달해야 합니다.",
            "meaningVi": "Công ước của Liên Hợp Quốc năm 1965 nhằm xóa bỏ mọi hình thức phân biệt chủng tộc, cấm phân biệt đối xử dựa trên màu da, dòng dõi, nguồn gốc dân tộc. Đây là công cụ pháp lý quan trọng chống phân biệt chủng tộc toàn cầu.",
            "context": "인권법, 사회정책, 다문화, 노동법",
            "culturalNote": "한국은 전통적으로 단일민족 정체성을 강조했으나, 최근 다문화가정 증가로 인종차별 금지법 제정이 논의되고 있습니다. 베트남은 다민족 국가로 소수민족 우대정책을 시행하지만, 킨족(다수민족) 중심 문화가 강합니다. 통역 시 한국의 '다문화'와 베트남의 '소수민족'이 다른 맥락임을 이해하고, 특히 '단일민족' 표현은 베트남에서 오해를 살 수 있으므로 주의해야 합니다.",
            "commonMistakes": [
                {
                    "mistake": "'인종'을 'dân tộc'으로 번역",
                    "correction": "'chủng tộc'으로 번역",
                    "explanation": "dân tộc은 주로 국내 민족(ethnic group)을 의미하고, chủng tộc은 국제적 인종(race) 개념입니다. 협약명은 반드시 chủng tộc을 사용해야 합니다."
                },
                {
                    "mistake": "'차별'을 'phân biệt'로만 번역",
                    "correction": "'kỳ thị' 또는 'phân biệt đối xử'",
                    "explanation": "phân biệt는 중립적인 '구별'의 의미도 있지만, 협약에서는 부정적 의미의 'kỳ thị'(차별)를 사용합니다. 'phân biệt đối xử'는 '차별 대우'를 명확히 표현합니다."
                },
                {
                    "mistake": "'철폐'를 'loại bỏ'로 번역",
                    "correction": "'xóa bỏ'로 번역",
                    "explanation": "공식 협약명에서는 'xóa bỏ'를 사용하며, 이는 완전히 없앤다는 강한 의미입니다. loại bỏ도 제거의 의미지만 공식 용어는 xóa bỏ입니다."
                }
            ],
            "examples": [
                {
                    "ko": "한국은 인종차별철폐협약에 따라 외국인 노동자 보호 정책을 강화하고 있습니다.",
                    "vi": "Hàn Quốc đang tăng cường chính sách bảo vệ lao động nước ngoài theo Công ước xóa bỏ kỳ thị chủng tộc.",
                    "situation": "formal"
                },
                {
                    "ko": "이 법안은 인종차별철폐협약의 정신을 반영합니다.",
                    "vi": "Dự luật này phản ánh tinh thần của Công ước xóa bỏ kỳ thị chủng tộc.",
                    "situation": "formal"
                },
                {
                    "ko": "고용 과정에서의 인종차별은 협약 위반입니다.",
                    "vi": "Kỳ thị chủng tộc trong quá trình tuyển dụng là vi phạm Công ước.",
                    "situation": "formal"
                }
            ],
            "relatedTerms": ["다문화", "소수민족", "차별금지", "평등권"]
        },
        {
            "slug": "cong-uoc-xoa-bo-ky-thi-phu-nu",
            "korean": "여성차별철폐협약",
            "vietnamese": "Công ước xóa bỏ kỳ thị phụ nữ",
            "hanja": "女性差別撤廢協約",
            "hanjaReading": "女(계집 여) + 性(성품 성) + 差(다를 차) + 別(나눌 별) + 撤(걷을 철) + 廢(폐할 폐) + 協(화합할 협) + 約(약속할 약)",
            "pronunciation": "여성차별철폐협약",
            "meaningKo": "정치, 경제, 사회, 문화 등 모든 분야에서 여성에 대한 차별을 철폐하기 위한 1979년 UN 협약으로, 여성의 평등권 보장을 목표로 합니다. 통역 시 '여성'(phụ nữ)과 '여자'(con gái)를 구분하고, 공식 문서에서는 phụ nữ를 사용해야 합니다. 한국은 1984년 비준했으며, 베트남은 1982년 가입했습니다. 통역 시 '성평등'(bình đẳng giới)과 '양성평등'(bình đẳng nam nữ)의 차이, '적극적 평등 실현 조치'와 같은 개념을 정확히 전달해야 하며, 특히 가정 내 역할, 재산권, 정치 참여 등의 맥락에서 양국의 문화적 차이를 고려해야 합니다.",
            "meaningVi": "Công ước của Liên Hợp Quốc năm 1979 nhằm xóa bỏ mọi hình thức phân biệt đối xử với phụ nữ trong các lĩnh vực chính trị, kinh tế, xã hội, văn hóa, đảm bảo quyền bình đẳng cho phụ nữ.",
            "context": "여성인권, 성평등, 노동법, 가족법",
            "culturalNote": "한국은 최근 성평등 정책을 강화하고 있으나 여전히 유교적 가부장 문화의 영향이 남아있으며, 경력단절, 임금격차 등의 문제가 있습니다. 베트남은 사회주의 체제 하에서 여성의 경제활동 참여율이 높고, 전통적으로 여성이 가정 경제를 관리하는 문화가 있으나, 정치 지도부의 여성 비율은 낮은 편입니다. 통역 시 양국의 여성 지위와 역할에 대한 인식 차이를 이해하고, '여성 할당제', '육아휴직' 등의 제도를 설명할 때 문화적 맥락을 고려해야 합니다.",
            "commonMistakes": [
                {
                    "mistake": "'여성'을 'con gái'로 번역",
                    "correction": "'phụ nữ'로 번역",
                    "explanation": "con gái는 어린 여자아이나 딸을 의미하고, phụ nữ는 성인 여성 일반을 뜻합니다. 공식 문서와 협약명에는 반드시 phụ nữ를 사용해야 합니다."
                },
                {
                    "mistake": "'성평등'을 'bình đẳng giới tính'으로 번역",
                    "correction": "'bình đẳng giới' 또는 'bình đẳng nam nữ'",
                    "explanation": "giới tính은 생물학적 성(sex)을 의미하고, giới는 사회적 성(gender) 개념입니다. 성평등은 사회적 개념이므로 'bình đẳng giới'가 정확합니다."
                },
                {
                    "mistake": "'여성 할당제'를 'hệ thống phân chia cho phụ nữ'로 번역",
                    "correction": "'chế độ hạn ngạch cho phụ nữ' 또는 'chính sách định mức cho phụ nữ'",
                    "explanation": "할당제는 일정 비율을 보장하는 제도이므로 'hạn ngạch'(할당량) 또는 'định mức'(정량)을 사용해야 하며, 단순 분배(phân chia)와는 다릅니다."
                }
            ],
            "examples": [
                {
                    "ko": "한국은 여성차별철폐협약에 따라 성평등 정책을 추진하고 있습니다.",
                    "vi": "Hàn Quốc đang thúc đẩy chính sách bình đẳng giới theo Công ước xóa bỏ kỳ thị phụ nữ.",
                    "situation": "formal"
                },
                {
                    "ko": "이 법은 여성차별철폐협약 제11조의 고용 평등 원칙을 반영합니다.",
                    "vi": "Luật này phản ánh nguyên tắc bình đẳng việc làm theo Điều 11 Công ước xóa bỏ kỳ thị phụ nữ.",
                    "situation": "formal"
                },
                {
                    "ko": "정치 참여에서의 여성 할당제는 협약의 정신에 부합합니다.",
                    "vi": "Chế độ hạn ngạch cho phụ nữ trong tham gia chính trị phù hợp với tinh thần Công ước.",
                    "situation": "formal"
                }
            ],
            "relatedTerms": ["성평등", "여성인권", "모성보호", "성별임금격차"]
        },
        {
            "slug": "cong-uoc-quyen-tre-em",
            "korean": "아동권리협약",
            "vietnamese": "Công ước Quyền trẻ em",
            "hanja": "兒童權利協約",
            "hanjaReading": "兒(아이 아) + 童(아이 동) + 權(권세 권) + 利(이로울 리) + 協(화합할 협) + 約(약속할 약)",
            "pronunciation": "아동권리협약",
            "meaningKo": "18세 미만 모든 아동의 생존권, 보호권, 발달권, 참여권을 보장하는 1989년 UN 협약으로, 세계에서 가장 많은 국가가 비준한 인권조약입니다. 통역 시 '아동'(trẻ em)과 '청소년'(thanh thiếu niên)을 구분해야 하며, 협약상 아동은 18세 미만 전체를 포함합니다. 한국은 1991년 비준했으며, 베트남도 1990년 초기 비준국 중 하나입니다. 통역 시 '아동학대', '체벌', '아동노동' 등의 민감한 용어는 양국의 문화적 차이를 고려하여 신중하게 전달해야 하며, 특히 '훈육'과 '학대'의 경계, '조기교육'과 '아동노동'의 구분 등을 명확히 해야 합니다.",
            "meaningVi": "Công ước của Liên Hợp Quốc năm 1989 đảm bảo quyền sống, quyền được bảo vệ, quyền phát triển và quyền tham gia của mọi trẻ em dưới 18 tuổi. Đây là hiệp ước nhân quyền được phê chuẩn rộng rãi nhất thế giới.",
            "context": "아동복지, 교육, 사법, 보건",
            "culturalNote": "한국은 교육열이 높아 아동의 학습권을 중시하지만, 과도한 사교육과 학업 스트레스가 문제되고 있습니다. 베트남도 교육을 중시하나, 농촌 지역에서는 아동노동이 여전히 존재하며, 도시와 농촌의 교육 격차가 큽니다. 통역 시 '체벌' 개념이 양국에서 다르게 인식될 수 있으며(한국은 학교 체벌 금지, 베트남은 제한적 허용), '아동 최선의 이익'이라는 추상적 원칙을 구체적 상황에 적용할 때 문화적 맥락을 고려해야 합니다.",
            "commonMistakes": [
                {
                    "mistake": "'아동'을 'trẻ con'으로 번역",
                    "correction": "'trẻ em'으로 번역",
                    "explanation": "trẻ con은 어린아이(유아)를 지칭하는 구어체이고, trẻ em은 18세 미만 전체를 포함하는 공식 용어입니다. 협약명에는 반드시 trẻ em을 사용합니다."
                },
                {
                    "mistake": "'권리'를 'quyền lợi'로만 번역",
                    "correction": "'quyền' 또는 'quyền lợi'",
                    "explanation": "협약명은 'Quyền trẻ em'으로 간결하게 표현하며, 구체적 권리를 나열할 때는 'quyền lợi'를 사용할 수 있습니다."
                },
                {
                    "mistake": "'아동학대'를 'lạm dụng trẻ em'으로만 번역",
                    "correction": "'bạo hành trẻ em' 또는 'ngược đãi trẻ em'",
                    "explanation": "lạm dụng는 주로 성적 학대를 의미하고, 신체적·정서적 학대는 'bạo hành' 또는 'ngược đãi'를 사용합니다. 맥락에 따라 구분해야 합니다."
                }
            ],
            "examples": [
                {
                    "ko": "한국은 아동권리협약에 따라 아동 최선의 이익을 우선 고려합니다.",
                    "vi": "Hàn Quốc ưu tiên xem xét lợi ích tốt nhất của trẻ em theo Công ước Quyền trẻ em.",
                    "situation": "formal"
                },
                {
                    "ko": "이 정책은 아동권리협약 제28조의 교육권 보장 원칙을 따릅니다.",
                    "vi": "Chính sách này tuân theo nguyên tắc đảm bảo quyền giáo dục theo Điều 28 Công ước Quyền trẻ em.",
                    "situation": "formal"
                },
                {
                    "ko": "아동의 의견 표명권은 협약에서 보장하는 기본권입니다.",
                    "vi": "Quyền bày tỏ ý kiến của trẻ em là quyền cơ bản được Công ước đảm bảo.",
                    "situation": "formal"
                }
            ],
            "relatedTerms": ["아동복지", "친권", "후견인", "아동학대"]
        },
        {
            "slug": "cong-uoc-quyen-nguoi-khuyet-tat",
            "korean": "장애인권리협약",
            "vietnamese": "Công ước Quyền người khuyết tật",
            "hanja": "障礙人權利協約",
            "hanjaReading": "障(막을 장) + 礙(거리낄 애) + 人(사람 인) + 權(권세 권) + 利(이로울 리) + 協(화합할 협) + 約(약속할 약)",
            "pronunciation": "장애인권리협약",
            "meaningKo": "모든 장애인의 인권과 기본적 자유를 보장하고, 사회 참여를 촉진하기 위한 2006년 UN 협약입니다. 통역 시 '장애인'을 지칭하는 용어가 시대에 따라 변화했으며(장애자→장애인→장애를 가진 사람), 베트남어도 'người tàn tật'(장애자)에서 'người khuyết tật'(결함이 있는 사람)으로 변경되어 공식 용어는 후자를 사용해야 합니다. 한국은 2008년 비준했으며, 베트남은 2015년 가입했습니다. 통역 시 '정당한 편의 제공', '합리적 조정', '접근성' 등의 개념을 정확히 전달해야 하며, 양국의 장애인 복지 수준과 인프라 차이를 고려해야 합니다.",
            "meaningVi": "Công ước của Liên Hợp Quốc năm 2006 đảm bảo nhân quyền và tự do cơ bản của mọi người khuyết tật, thúc đẩy sự tham gia xã hội của họ.",
            "context": "사회복지, 접근성, 교육, 고용",
            "culturalNote": "한국은 장애인 복지 제도가 발달했으나 여전히 접근성과 고용 차별이 문제되며, 최근 탈시설화 정책을 추진 중입니다. 베트남은 전쟁 후유증으로 장애인이 많으나 복지 인프라가 부족하며, 전통적으로 장애를 가족이 돌보는 문화가 강합니다. 통역 시 '장애'를 개인의 결함이 아닌 사회적 장벽으로 보는 '사회적 모델' 관점을 전달해야 하며, '장애인을 위한'보다 '장애인과 함께'라는 표현이 권장됩니다.",
            "commonMistakes": [
                {
                    "mistake": "'장애인'을 'người tàn tật'로 번역",
                    "correction": "'người khuyết tật'로 번역",
                    "explanation": "người tàn tật는 구식 표현으로 부정적 뉘앙스가 있으며, 현재 공식 용어는 người khuyết tật입니다. 협약명도 이를 사용합니다."
                },
                {
                    "mistake": "'정당한 편의'를 'tiện ích hợp lý'로 번역",
                    "correction": "'hỗ trợ hợp lý' 또는 'điều chỉnh hợp lý'",
                    "explanation": "tiện ích는 일반적인 편의시설을 의미하고, 협약의 'reasonable accommodation'은 개별적 조정을 의미하므로 'hỗ trợ' 또는 'điều chỉnh'이 적합합니다."
                },
                {
                    "mistake": "'접근성'을 'tiếp cận'으로만 번역",
                    "correction": "'khả năng tiếp cận' 또는 'tính tiếp cận'",
                    "explanation": "tiếp cận은 동사(접근하다)이고, 명사형 '접근성'은 'khả năng tiếp cận' 또는 'tính tiếp cận'으로 표현해야 합니다."
                }
            ],
            "examples": [
                {
                    "ko": "한국은 장애인권리협약에 따라 접근성 개선 사업을 추진하고 있습니다.",
                    "vi": "Hàn Quốc đang thúc đẩy các dự án cải thiện khả năng tiếp cận theo Công ước Quyền người khuyết tật.",
                    "situation": "formal"
                },
                {
                    "ko": "고용 시 장애인에게 정당한 편의를 제공해야 합니다.",
                    "vi": "Khi tuyển dụng phải cung cấp hỗ trợ hợp lý cho người khuyết tật.",
                    "situation": "formal"
                },
                {
                    "ko": "이 건물은 장애인권리협약의 접근성 기준을 충족합니다.",
                    "vi": "Tòa nhà này đáp ứng tiêu chuẩn khả năng tiếp cận của Công ước Quyền người khuyết tật.",
                    "situation": "formal"
                }
            ],
            "relatedTerms": ["접근성", "정당한편의", "장애등급", "재활"]
        },
        {
            "slug": "he-thong-tu-hinh",
            "korean": "사형제도",
            "vietnamese": "Hệ thống tử hình",
            "hanja": "死刑制度",
            "hanjaReading": "死(죽을 사) + 刑(형벌 형) + 制(만들 제) + 度(법도 도)",
            "pronunciation": "사형제도",
            "meaningKo": "범죄자의 생명을 박탈하는 극형으로, 국제인권법에서 가장 논쟁적인 주제 중 하나입니다. 통역 시 '사형'(tử hình)과 '무기징역'(tù chung thân)을 명확히 구분해야 하며, '사형 집행 유예'와 '사형 폐지' 등의 개념도 정확히 전달해야 합니다. 한국은 1997년 이후 사형을 집행하지 않아 사실상 폐지국으로 분류되며, 베트남은 여전히 사형을 집행하고 있으나 대상 범죄를 축소하는 추세입니다. 통역 시 사형제도는 정치적·종교적으로 민감한 주제이므로, 가치 판단 없이 객관적으로 전달하고, '생명권'과 '범죄 억제' 등 양측 논리를 균형 있게 통역해야 합니다.",
            "meaningVi": "Hình phạt tước đoạt sinh mạng của tội phạm, là chủ đề gây tranh cãi nhất trong luật nhân quyền quốc tế. Hàn Quốc thực tế đã bỏ tử hình (không thi hành từ 1997), còn Việt Nam vẫn duy trì nhưng đang giảm phạm vi áp dụng.",
            "context": "형법, 인권법, 형사정책, 국제인권",
            "culturalNote": "한국은 1997년 김대중 대통령 이후 사형을 집행하지 않고 있으나, 법적으로는 폐지하지 않았으며 여론은 찬반이 엇갈립니다. 베트남은 2011년 총기 사형에서 약물 주사 사형으로 전환했고, 사형 대상 범죄를 점진적으로 줄이고 있습니다. 통역 시 사형제도에 대한 양국의 입장 차이를 이해하고, 국제인권단체의 사형 폐지 요구와 각국의 주권적 형사정책 사이의 긴장을 중립적으로 전달해야 합니다.",
            "commonMistakes": [
                {
                    "mistake": "'사형'을 'hình phạt tử hình'로 번역",
                    "correction": "'tử hình' 또는 'án tử hình'",
                    "explanation": "tử hình 자체가 사형을 의미하므로, hình phạt(형벌)을 붙이면 중복입니다. 판결을 강조할 때는 'án tử hình'을 사용합니다."
                },
                {
                    "mistake": "'사형 집행'을 'thực thi tử hình'로 번역",
                    "correction": "'thi hành tử hình' 또는 'hành quyết'",
                    "explanation": "사형 집행의 공식 용어는 'thi hành tử hình'이며, 'hành quyết'은 실제 처형 행위를 의미합니다. thực thi는 정책 집행에 주로 쓰입니다."
                },
                {
                    "mistake": "'사형 폐지'를 'hủy bỏ tử hình'로 번역",
                    "correction": "'bãi bỏ tử hình' 또는 'xóa bỏ tử hình'",
                    "explanation": "제도의 폐지는 'bãi bỏ' 또는 'xóa bỏ'를 사용하며, 'hủy bỏ'는 개별 결정이나 계약의 취소에 주로 사용됩니다."
                }
            ],
            "examples": [
                {
                    "ko": "한국은 1997년 이후 사형을 집행하지 않아 사실상 사형폐지국입니다.",
                    "vi": "Hàn Quốc thực tế là quốc gia bãi bỏ tử hình vì không thi hành từ năm 1997.",
                    "situation": "formal"
                },
                {
                    "ko": "국제인권단체들은 사형제도 폐지를 촉구하고 있습니다.",
                    "vi": "Các tổ chức nhân quyền quốc tế đang kêu gọi bãi bỏ hệ thống tử hình.",
                    "situation": "formal"
                },
                {
                    "ko": "베트남은 사형 대상 범죄를 점진적으로 축소하고 있습니다.",
                    "vi": "Việt Nam đang dần thu hẹp các loại tội áp dụng án tử hình.",
                    "situation": "formal"
                }
            ],
            "relatedTerms": ["생명권", "무기징역", "극형", "형벌"]
        },
        {
            "slug": "tu-do-bieu-dat",
            "korean": "표현의자유",
            "vietnamese": "Tự do biểu đạt",
            "hanja": "表現의自由",
            "hanjaReading": "表(나타낼 표) + 現(나타날 현) + 自(스스로 자) + 由(말미암을 유)",
            "pronunciation": "표현의자유",
            "meaningKo": "개인이 자신의 생각과 의견을 말, 글, 예술 등으로 자유롭게 표현할 수 있는 권리로, 민주주의의 핵심 요소입니다. 통역 시 '표현의 자유'와 '언론의 자유'를 구분해야 하며, 베트남어 'tự do biểu đạt'는 넓은 의미의 표현, 'tự do ngôn luận'은 언론에 특화된 개념입니다. 한국은 헌법 제21조에서 보장하나 명예훼손, 허위사실 유포 등으로 제한되며, 베트남은 사회주의 체제 하에서 당과 국가에 대한 비판이 제한됩니다. 통역 시 '표현의 자유'와 '책임', '제한의 정당성' 등을 균형 있게 전달하고, 양국의 법적·정치적 차이를 고려하여 민감한 표현은 신중히 처리해야 합니다.",
            "meaningVi": "Quyền của cá nhân được tự do thể hiện suy nghĩ và ý kiến bằng lời nói, văn bản, nghệ thuật, là yếu tố cốt lõi của dân chủ. Hàn Quốc đảm bảo trong Hiến pháp nhưng có giới hạn, Việt Nam hạn chế phê bình Đảng và Nhà nước.",
            "context": "헌법, 언론, SNS, 예술, 집회",
            "culturalNote": "한국은 민주화 이후 표현의 자유가 크게 확대되었으나, 명예훼손죄가 형사처벌 대상이라는 점에서 국제적 논란이 있습니다. 베트남은 인터넷 표현에 대한 규제가 강하며, 정치적 비판은 '국가전복 선동' 등으로 처벌받을 수 있습니다. 통역 시 '비판'과 '비방', '풍자'와 '모욕' 등의 경계가 양국에서 다르게 인식될 수 있으며, 특히 정치인에 대한 표현, 역사적 사건에 대한 평가 등은 매우 민감하므로 중립적 표현을 유지해야 합니다.",
            "commonMistakes": [
                {
                    "mistake": "'표현의 자유'를 'tự do thể hiện'으로 번역",
                    "correction": "'tự do biểu đạt'로 번역",
                    "explanation": "thể hiện은 단순히 드러내다는 의미이고, biểu đạt은 의견·생각을 표명한다는 의미로 법적 용어에 적합합니다."
                },
                {
                    "mistake": "'언론의 자유'를 'tự do biểu đạt'로 번역",
                    "correction": "'tự do ngôn luận' 또는 'tự do báo chí'",
                    "explanation": "표현의 자유(biểu đạt)는 넓은 개념이고, 언론의 자유는 'tự do ngôn luận'(말의 자유), 'tự do báo chí'(출판의 자유)로 구분됩니다."
                },
                {
                    "mistake": "'명예훼손'을 'phỉ báng'으로만 번역",
                    "correction": "'phỉ báng danh dự' 또는 'tội vu khống'",
                    "explanation": "phỉ báng는 일반적 비방이고, 법적 명예훼손은 'phỉ báng danh dự'입니다. 허위사실인 경우 'vu khống'(무고)를 사용합니다."
                }
            ],
            "examples": [
                {
                    "ko": "헌법은 표현의 자유를 보장하지만, 타인의 명예를 훼손해서는 안 됩니다.",
                    "vi": "Hiến pháp đảm bảo tự do biểu đạt nhưng không được phỉ báng danh dự người khác.",
                    "situation": "formal"
                },
                {
                    "ko": "인터넷 표현의 자유와 허위정보 규제 사이의 균형이 필요합니다.",
                    "vi": "Cần cân bằng giữa tự do biểu đạt trên internet và kiểm soát thông tin sai lệch.",
                    "situation": "formal"
                },
                {
                    "ko": "예술가의 표현의 자유는 민주사회에서 존중되어야 합니다.",
                    "vi": "Tự do biểu đạt của nghệ sĩ cần được tôn trọng trong xã hội dân chủ.",
                    "situation": "formal"
                }
            ],
            "relatedTerms": ["언론의자유", "검열", "명예훼손", "집회의자유"]
        },
        {
            "slug": "tu-do-luong-tam",
            "korean": "양심의자유",
            "vietnamese": "Tự do lương tâm",
            "hanja": "良心의自由",
            "hanjaReading": "良(어질 량/양) + 心(마음 심) + 自(스스로 자) + 由(말미암을 유)",
            "pronunciation": "양심의자유",
            "meaningKo": "개인이 내면의 윤리적·도덕적 신념을 형성하고 이에 따라 행동할 수 있는 권리로, 흔히 종교의 자유와 함께 논의됩니다. 통역 시 '양심'(lương tâm)과 '신념'(niềm tin), '종교'(tôn giáo)를 구분해야 하며, 양심의 자유는 종교를 넘어 세속적 신념도 포함합니다. 한국 헌법 제19조와 제20조에서 보장하며, 특히 양심적 병역거부가 중요한 쟁점입니다. 베트남은 종교의 자유를 인정하나 국가 안보와 사회 질서를 우선시하며, 공산당 이념과 충돌하는 신념은 제한될 수 있습니다. 통역 시 '양심적 거부', '신앙 고백', '종교 의례' 등의 개념을 설명할 때 양국의 법적·종교적 차이를 고려해야 합니다.",
            "meaningVi": "Quyền của cá nhân được hình thành và thực hiện theo niềm tin đạo đức, luân lý nội tâm, thường được bàn cùng tự do tôn giáo. Hàn Quốc đảm bảo trong Hiến pháp, Việt Nam ưu tiên an ninh quốc gia và trật tự xã hội.",
            "context": "헌법, 종교, 병역, 윤리",
            "culturalNote": "한국은 2018년 헌법재판소가 양심적 병역거부를 인정하면서 대체복무제를 도입했으며, 종교의 자유가 폭넓게 보장됩니다. 베트남은 불교, 가톨릭 등 주요 종교는 인정하나, 정부 승인을 받지 않은 종교 활동은 제한되며, 종교가 정치화되는 것을 경계합니다. 통역 시 '양심적 병역거부'는 베트남에서 생소한 개념이므로 설명이 필요하며, '종교 탄압'과 '종교 관리'의 표현 차이를 신중히 다뤄야 합니다. 또한 한국의 개신교, 베트남의 불교·가톨릭 등 주류 종교의 사회적 영향력 차이도 고려해야 합니다.",
            "commonMistakes": [
                {
                    "mistake": "'양심'을 'tâm trạng'으로 번역",
                    "correction": "'lương tâm'으로 번역",
                    "explanation": "tâm trạng은 일시적 기분·심정을 의미하고, lương tâm은 도덕적 양심을 뜻합니다. 법적 개념으로는 반드시 lương tâm을 사용해야 합니다."
                },
                {
                    "mistake": "'양심적 병역거부'를 'từ chối nghĩa vụ quân sự'로만 번역",
                    "correction": "'từ chối nghĩa vụ quân sự vì lý do lương tâm'",
                    "explanation": "단순 병역 거부와 양심적 거부를 구분하기 위해 'vì lý do lương tâm'(양심적 이유로)를 반드시 명시해야 합니다."
                },
                {
                    "mistake": "'신앙'을 'niềm tin'으로만 번역",
                    "correction": "'đức tin' 또는 'tín ngưỡng'",
                    "explanation": "niềm tin은 일반적 믿음이고, 종교적 신앙은 'đức tin'(기독교) 또는 'tín ngưỡng'(일반 종교)을 사용합니다."
                }
            ],
            "examples": [
                {
                    "ko": "양심의 자유는 헌법이 보장하는 기본권입니다.",
                    "vi": "Tự do lương tâm là quyền cơ bản được Hiến pháp đảm bảo.",
                    "situation": "formal"
                },
                {
                    "ko": "한국은 양심적 병역거부자에게 대체복무를 허용합니다.",
                    "vi": "Hàn Quốc cho phép phục vụ thay thế đối với người từ chối nghĩa vụ quân sự vì lý do lương tâm.",
                    "situation": "formal"
                },
                {
                    "ko": "종교의 자유는 양심의 자유의 중요한 부분입니다.",
                    "vi": "Tự do tôn giáo là phần quan trọng của tự do lương tâm.",
                    "situation": "formal"
                }
            ],
            "relatedTerms": ["종교의자유", "신앙", "병역거부", "윤리"]
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
