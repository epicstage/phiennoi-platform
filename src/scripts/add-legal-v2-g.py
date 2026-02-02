#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
건설법/건축허가 용어 추가 스크립트
Theme: Construction Law/Building Permits
Target: 10 terms for legal.json
"""

import json
import os

def main():
    # CRITICAL: 절대 경로 구성
    file_path = os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', 'data', 'terms', 'legal.json')

    # 기존 데이터 로드 (LIST 형식)
    with open(file_path, 'r', encoding='utf-8') as f:
        data = json.load(f)

    # 기존 slug 추출 (중복 방지)
    existing_slugs = {t['slug'] for t in data}

    # 새 용어 정의 (Tier S 기준)
    new_terms = [
        {
            "slug": "giay-phep-xay-dung",
            "korean": "건축허가",
            "vietnamese": "giấy phép xây dựng",
            "hanja": "建築許可",
            "hanjaReading": "建(집 건) + 築(쌓을 축) + 許(허락할 허) + 可(옳을 가)",
            "pronunciation": "건축허가",
            "meaningKo": "건축물을 신축, 증축, 개축, 재축하거나 대수선하려는 경우 관할 행정기관으로부터 받아야 하는 법적 허가. 통역 시 주의할 점은 베트남의 건축허가 절차가 한국보다 복잡하고 시간이 오래 걸린다는 점을 명확히 설명해야 하며, '사전 허가제'와 '사후 신고제'의 차이를 구분하여 통역해야 합니다. 또한 베트남에서는 외국인이 직접 건축허가를 받기 어려우므로 현지 파트너를 통해야 한다는 실무적 조언도 함께 전달하는 것이 좋습니다.",
            "meaningVi": "Giấy phép do cơ quan hành chính có thẩm quyền cấp để được xây dựng mới, cải tạo, mở rộng, xây dựng lại hoặc sửa chữa lớn công trình. Thủ tục cấp giấy phép xây dựng tại Việt Nam thường phức tạp hơn và mất nhiều thời gian hơn so với Hàn Quốc. Người nước ngoài khó có thể tự làm thủ tục này mà cần thông qua đối tác địa phương.",
            "context": "건설 계약, 부동산 개발, 법률 자문 시",
            "culturalNote": "한국은 건축허가가 비교적 명확한 법적 기준에 따라 처리되지만, 베트남은 지방 정부의 재량권이 크고 관료주의적 절차가 많아 시간과 비용이 더 소요됩니다. 한국 기업이 베트남에서 건설 프로젝트를 진행할 때 이러한 차이를 이해하지 못해 일정 지연이 발생하는 경우가 많습니다. 또한 베트남은 뇌물 관행이 남아있어 '비공식 비용'이 발생할 수 있다는 점도 통역 시 은연중에 전달해야 할 문화적 맥락입니다.",
            "commonMistakes": [
                {
                    "mistake": "giấy chứng nhận xây dựng",
                    "correction": "giấy phép xây dựng",
                    "explanation": "'chứng nhận'은 증명서를 의미하므로, 허가를 뜻하는 'phép'을 사용해야 합니다."
                },
                {
                    "mistake": "cho phép xây dựng",
                    "correction": "giấy phép xây dựng",
                    "explanation": "동사 'cho phép'(허락하다)가 아닌 명사 'giấy phép'(허가서)를 사용해야 합니다."
                },
                {
                    "mistake": "허가증",
                    "correction": "건축허가",
                    "explanation": "한국어에서 '허가증'은 물리적 문서를 강조하지만, 법률 용어로는 '건축허가'가 정확합니다."
                }
            ],
            "examples": [
                {
                    "ko": "이 토지에 공장을 짓기 위해서는 먼저 건축허가를 받아야 합니다.",
                    "vi": "Để xây dựng nhà máy trên mảnh đất này, trước tiên phải xin giấy phép xây dựng.",
                    "situation": "formal"
                },
                {
                    "ko": "건축허가 없이 공사를 진행하면 법적 처벌을 받습니다.",
                    "vi": "Nếu thi công mà không có giấy phép xây dựng sẽ bị xử phạt theo pháp luật.",
                    "situation": "onsite"
                },
                {
                    "ko": "현지 파트너가 건축허가 절차를 대행해 주기로 했습니다.",
                    "vi": "Đối tác địa phương đã đồng ý đại diện làm thủ tục xin giấy phép xây dựng.",
                    "situation": "formal"
                }
            ],
            "relatedTerms": ["quy-hoach-xay-dung", "giam-sat-xay-dung", "nghiem-thu-cong-trinh", "vi-pham-xay-dung"]
        },
        {
            "slug": "quy-hoach-xay-dung",
            "korean": "건축계획",
            "vietnamese": "quy hoạch xây dựng",
            "hanja": "建築計劃",
            "hanjaReading": "建(집 건) + 築(쌓을 축) + 計(셀 계) + 劃(그을 획)",
            "pronunciation": "건축계획",
            "meaningKo": "건축물의 배치, 규모, 용도 등을 사전에 계획하는 것으로, 도시계획과 연계되어 진행됩니다. 통역 시 'quy hoạch'는 단순 계획이 아닌 '규제적 계획'의 의미가 강하므로, 베트남의 도시계획이 정부 주도의 강제성을 띤다는 점을 명확히 전달해야 합니다. 한국의 '건축계획'이 민간 주도의 유연한 계획이라면, 베트남의 'quy hoạch xây dựng'은 국가 계획에 종속되는 개념이므로 이 차이를 설명하는 것이 중요합니다.",
            "meaningVi": "Kế hoạch về bố trí, quy mô, công năng sử dụng của công trình xây dựng, được thực hiện dựa trên quy hoạch đô thị. Quy hoạch xây dựng tại Việt Nam mang tính bắt buộc do nhà nước quy định, khác với Hàn Quốc nơi doanh nghiệp tư nhân có nhiều quyền tự chủ hơn trong việc lập kế hoạch xây dựng.",
            "context": "도시 개발, 건설 프로젝트 기획 단계",
            "culturalNote": "베트남은 사회주의 체제로 토지가 국유이기 때문에 건축계획이 국가 계획에 종속됩니다. 한국 기업이 베트남에서 건설 프로젝트를 진행할 때 자국의 유연한 건축계획 방식을 기대하면 실패할 가능성이 높습니다. 베트남에서는 지방 정부의 5개년 계획, 10개년 계획 등 장기 도시계획에 맞춰야 하며, 이를 어기면 허가 자체가 불가능합니다. 통역사는 이러한 체제 차이를 명확히 인지하고 통역해야 합니다.",
            "commonMistakes": [
                {
                    "mistake": "kế hoạch xây dựng",
                    "correction": "quy hoạch xây dựng",
                    "explanation": "'kế hoạch'는 일반 계획이고, 'quy hoạch'는 법적 구속력이 있는 규제적 계획입니다."
                },
                {
                    "mistake": "thiết kế xây dựng",
                    "correction": "quy hoạch xây dựng",
                    "explanation": "'thiết kế'는 설계(design)를 의미하고, 'quy hoạch'는 계획(planning)을 의미합니다."
                },
                {
                    "mistake": "건축설계",
                    "correction": "건축계획",
                    "explanation": "설계는 구체적 도면 작성이고, 계획은 사전 기획 단계입니다."
                }
            ],
            "examples": [
                {
                    "ko": "이 지역의 건축계획은 정부의 도시계획에 따라야 합니다.",
                    "vi": "Quy hoạch xây dựng ở khu vực này phải tuân theo quy hoạch đô thị của chính phủ.",
                    "situation": "formal"
                },
                {
                    "ko": "건축계획 변경은 관할 당국의 승인이 필요합니다.",
                    "vi": "Thay đổi quy hoạch xây dựng cần có sự phê duyệt của cơ quan có thẩm quyền.",
                    "situation": "onsite"
                },
                {
                    "ko": "이 프로젝트는 장기 건축계획에 포함되어 있습니다.",
                    "vi": "Dự án này đã được đưa vào quy hoạch xây dựng dài hạn.",
                    "situation": "formal"
                }
            ],
            "relatedTerms": ["giay-phep-xay-dung", "giam-sat-xay-dung", "chat-luong-cong-trinh", "quy-hoach-do-thi"]
        },
        {
            "slug": "giam-sat-xay-dung",
            "korean": "건설감리",
            "vietnamese": "giám sát xây dựng",
            "hanja": "建設監理",
            "hanjaReading": "建(세울 건) + 設(베풀 설) + 監(볼 감) + 理(다스릴 리)",
            "pronunciation": "건설감리",
            "meaningKo": "건설공사가 설계도서대로 시공되는지, 관련 법규를 준수하는지를 감독하고 확인하는 업무. 통역 시 주의할 점은 한국의 '감리'가 독립적인 전문가 집단에 의해 수행되는 반면, 베트남의 'giám sát'은 건설사 내부 인력이나 정부 관료가 수행하는 경우가 많아 독립성이 약하다는 점을 명확히 전달해야 합니다. 또한 베트남 현장에서는 감리 기준이 한국만큼 엄격하지 않아 품질 문제가 발생할 수 있으므로, 한국 기업은 자체 감리단을 파견하는 것이 일반적입니다.",
            "meaningVi": "Công việc giám sát và kiểm tra xem công trình xây dựng có được thi công đúng theo bản vẽ thiết kế và tuân thủ các quy định pháp luật liên quan hay không. Tại Việt Nam, công tác giám sát thường do nhân viên nội bộ công ty xây dựng hoặc cán bộ chính phủ đảm nhận, nên tính độc lập không cao như Hàn Quốc nơi có đội ngũ chuyên gia giám sát độc lập.",
            "context": "건설 현장, 계약 관리, 품질 보증",
            "culturalNote": "한국은 건설기술진흥법에 따라 일정 규모 이상의 공사는 의무적으로 독립적인 감리업체를 선정해야 하지만, 베트남은 이러한 법적 의무가 약하고 감리의 전문성도 한국만큼 높지 않습니다. 베트남 현장에서는 감리자가 시공사와 유착되어 있거나 뇌물을 받고 불량 시공을 묵인하는 경우도 있어, 한국 기업들은 자체 감리팀을 파견하거나 제3의 국제 감리업체를 고용하는 경우가 많습니다. 통역사는 이러한 문화적 차이를 이해하고 한국 측에 베트남 현장의 실태를 정확히 전달해야 합니다.",
            "commonMistakes": [
                {
                    "mistake": "kiểm tra xây dựng",
                    "correction": "giám sát xây dựng",
                    "explanation": "'kiểm tra'는 단순 검사이고, 'giám sát'은 지속적인 감독을 의미합니다."
                },
                {
                    "mistake": "quản lý xây dựng",
                    "correction": "giám sát xây dựng",
                    "explanation": "'quản lý'는 관리(management)이고, 'giám sát'은 감리(supervision)입니다."
                },
                {
                    "mistake": "건설관리",
                    "correction": "건설감리",
                    "explanation": "관리는 시공사의 업무이고, 감리는 독립적인 감독 업무입니다."
                }
            ],
            "examples": [
                {
                    "ko": "이 프로젝트는 국제 표준에 따라 건설감리를 실시합니다.",
                    "vi": "Dự án này sẽ thực hiện giám sát xây dựng theo tiêu chuẩn quốc tế.",
                    "situation": "formal"
                },
                {
                    "ko": "건설감리 업체가 시공 품질에 문제를 제기했습니다.",
                    "vi": "Công ty giám sát xây dựng đã phát hiện vấn đề về chất lượng thi công.",
                    "situation": "onsite"
                },
                {
                    "ko": "현장 건설감리는 매일 진행 상황을 보고합니다.",
                    "vi": "Giám sát xây dựng tại hiện trường báo cáo tiến độ hàng ngày.",
                    "situation": "onsite"
                }
            ],
            "relatedTerms": ["giay-phep-xay-dung", "nghiem-thu-cong-trinh", "chat-luong-cong-trinh", "an-toan-xay-dung"]
        },
        {
            "slug": "nghiem-thu-cong-trinh",
            "korean": "건물검사",
            "vietnamese": "nghiệm thu công trình",
            "hanja": "建物檢査",
            "hanjaReading": "建(세울 건) + 物(물건 물) + 檢(조사할 검) + 査(조사할 사)",
            "pronunciation": "건물검사",
            "meaningKo": "건설공사가 완료된 후 설계도서와 관련 법규에 맞게 시공되었는지를 최종적으로 확인하는 절차로, 합격해야 사용승인을 받을 수 있습니다. 통역 시 주의할 점은 베트남의 'nghiệm thu'가 한국의 '준공검사'보다 더 포괄적인 개념으로, 단계별 검수(중간 검수, 최종 검수)를 모두 포함한다는 점입니다. 또한 베트남 현장에서는 검사 기준이 느슨하고 뇌물로 통과시키는 관행이 있어, 한국 기업은 자체 품질검사를 병행하는 것이 중요하다는 실무적 조언도 함께 전달해야 합니다.",
            "meaningVi": "Quy trình kiểm tra cuối cùng sau khi hoàn thành công trình xây dựng để xác nhận xem công trình có được thi công đúng theo bản vẽ thiết kế và tuân thủ các quy định pháp luật hay không. Chỉ khi nghiệm thu đạt yêu cầu mới được cấp giấy phép sử dụng. Tại Việt Nam, nghiệm thu bao gồm cả nghiệm thu từng giai đoạn và nghiệm thu tổng thể.",
            "context": "건설 준공, 사용승인 신청, 품질 확인",
            "culturalNote": "한국은 준공검사 기준이 엄격하고 제3자 검증 기관이 참여하지만, 베트남은 검사 기준이 상대적으로 느슨하고 부패 가능성이 높습니다. 베트남 현장에서는 검사 담당자에게 '차값'(tiền xe) 명목으로 비공식 비용을 지불하는 관행이 있으며, 이를 거부하면 검사가 지연되거나 불합격 처리되는 경우도 있습니다. 한국 기업은 이러한 문화적 차이를 이해하고, 자체 품질검사를 병행하여 실제 품질을 확보해야 합니다. 통역사는 이러한 민감한 상황을 완곡하게 전달하는 능력이 필요합니다.",
            "commonMistakes": [
                {
                    "mistake": "kiểm tra công trình",
                    "correction": "nghiệm thu công trình",
                    "explanation": "'kiểm tra'는 일반 검사이고, 'nghiệm thu'는 공식적인 인수검사입니다."
                },
                {
                    "mistake": "thanh tra công trình",
                    "correction": "nghiệm thu công trình",
                    "explanation": "'thanh tra'는 사찰/감사를 의미하고, 'nghiệm thu'는 완공 후 인수검사입니다."
                },
                {
                    "mistake": "준공검사",
                    "correction": "건물검사",
                    "explanation": "준공검사는 'nghiệm thu công trình'의 일부이며, 한국어로는 '건물검사'가 더 포괄적입니다."
                }
            ],
            "examples": [
                {
                    "ko": "건물검사를 통과해야 입주가 가능합니다.",
                    "vi": "Phải qua nghiệm thu công trình mới được phép đưa vào sử dụng.",
                    "situation": "formal"
                },
                {
                    "ko": "오늘 관계 당국이 현장 건물검사를 실시할 예정입니다.",
                    "vi": "Hôm nay cơ quan chức năng sẽ tiến hành nghiệm thu công trình tại hiện trường.",
                    "situation": "onsite"
                },
                {
                    "ko": "건물검사에서 안전 기준 미달로 불합격 판정을 받았습니다.",
                    "vi": "Công trình đã bị đánh giá không đạt yêu cầu nghiệm thu do không đảm bảo tiêu chuẩn an toàn.",
                    "situation": "formal"
                }
            ],
            "relatedTerms": ["giam-sat-xay-dung", "chat-luong-cong-trinh", "giay-phep-xay-dung", "an-toan-xay-dung"]
        },
        {
            "slug": "an-toan-xay-dung",
            "korean": "건설안전",
            "vietnamese": "an toàn xây dựng",
            "hanja": "建設安全",
            "hanjaReading": "建(세울 건) + 設(베풀 설) + 安(편안할 안) + 全(온전할 전)",
            "pronunciation": "건설안전",
            "meaningKo": "건설 현장에서 작업자의 생명과 신체를 보호하고 사고를 예방하기 위한 모든 조치와 규정. 통역 시 주의할 점은 한국의 산업안전보건법이 매우 엄격한 반면, 베트남의 안전 기준은 법적으로 존재하나 현장에서 제대로 지켜지지 않는 경우가 많다는 점을 명확히 전달해야 합니다. 특히 베트남 현장에서는 안전모, 안전벨트 등 기본 보호장구조차 착용하지 않는 경우가 흔하므로, 한국 기업이 베트남에서 시공할 때는 자체 안전관리 규정을 강화해야 한다는 실무적 조언이 필요합니다.",
            "meaningVi": "Mọi biện pháp và quy định nhằm bảo vệ tính mạng, sức khỏe của người lao động và phòng ngừa tai nạn tại công trường xây dựng. Tại Việt Nam, mặc dù có quy định về an toàn xây dựng nhưng trên thực tế nhiều công trường không tuân thủ nghiêm ngặt, khác với Hàn Quốc nơi luật an toàn lao động được thực thi chặt chẽ.",
            "context": "건설 현장, 안전 교육, 사고 예방",
            "culturalNote": "한국은 중대재해처벌법 등으로 건설 안전 관리가 매우 엄격하지만, 베트남은 법은 있으나 집행이 약합니다. 베트남 현장에서는 안전교육이 형식적이고, 작업자들이 안전수칙을 무시하는 경우가 많으며, 사고가 발생해도 은폐하거나 축소 보고하는 경우가 흔합니다. 한국 기업이 베트남에서 건설 프로젝트를 진행할 때는 현지 관행에 따르지 말고 한국 수준의 안전 기준을 적용해야 하며, 이를 위해 한국인 안전관리자를 파견하는 것이 일반적입니다. 통역사는 이러한 차이를 한국 측에 명확히 전달하여 안전사고를 예방하는 데 기여해야 합니다.",
            "commonMistakes": [
                {
                    "mistake": "bảo vệ xây dựng",
                    "correction": "an toàn xây dựng",
                    "explanation": "'bảo vệ'는 보안(security)이고, 'an toàn'은 안전(safety)입니다."
                },
                {
                    "mistake": "an ninh xây dựng",
                    "correction": "an toàn xây dựng",
                    "explanation": "'an ninh'는 치안/보안을 의미하고, 'an toàn'은 안전을 의미합니다."
                },
                {
                    "mistake": "건설보안",
                    "correction": "건설안전",
                    "explanation": "보안은 외부 침입 방지이고, 안전은 사고 예방입니다."
                }
            ],
            "examples": [
                {
                    "ko": "모든 작업자는 건설안전 교육을 이수해야 합니다.",
                    "vi": "Tất cả công nhân phải hoàn thành khóa đào tạo về an toàn xây dựng.",
                    "situation": "formal"
                },
                {
                    "ko": "건설안전 규정을 위반하면 작업이 즉시 중단됩니다.",
                    "vi": "Nếu vi phạm quy định an toàn xây dựng, công việc sẽ bị dừng ngay lập tức.",
                    "situation": "onsite"
                },
                {
                    "ko": "이번 달 건설안전 점검에서 여러 문제점이 발견되었습니다.",
                    "vi": "Trong đợt kiểm tra an toàn xây dựng tháng này đã phát hiện nhiều vấn đề.",
                    "situation": "formal"
                }
            ],
            "relatedTerms": ["giam-sat-xay-dung", "nghiem-thu-cong-trinh", "bao-hiem-xay-dung", "tai-nan-lao-dong"]
        },
        {
            "slug": "chat-luong-cong-trinh",
            "korean": "건물품질",
            "vietnamese": "chất lượng công trình",
            "hanja": "建物品質",
            "hanjaReading": "建(세울 건) + 物(물건 물) + 品(물건 품) + 質(바탕 질)",
            "pronunciation": "건물품질",
            "meaningKo": "건축물이 설계 의도와 관련 기준에 맞게 시공되었는지를 평가하는 기준으로, 구조 안전성, 기능성, 내구성 등을 포함합니다. 통역 시 주의할 점은 한국의 품질 기준(KS 인증 등)과 베트남의 품질 기준(TCVN 표준)이 다르며, 베트남 현장에서는 자재 품질이 낮거나 시공 기술이 부족하여 한국 기준을 충족하기 어려운 경우가 많다는 점을 명확히 전달해야 합니다. 한국 기업은 자재를 한국에서 수입하거나 베트남 현지에서 한국 기준에 맞는 자재를 별도로 선별해야 하는 경우가 많습니다.",
            "meaningVi": "Tiêu chí đánh giá xem công trình có được thi công đúng theo ý đồ thiết kế và các tiêu chuẩn liên quan hay không, bao gồm độ an toàn kết cấu, tính năng sử dụng, độ bền. Tiêu chuẩn chất lượng tại Việt Nam (TCVN) khác với Hàn Quốc (KS), và chất lượng vật liệu cũng như kỹ thuật thi công tại Việt Nam thường không đạt tiêu chuẩn Hàn Quốc.",
            "context": "건설 계약, 품질 검사, 하자 보수",
            "culturalNote": "한국은 품질 관리 시스템이 체계적이고, 불량 시공 시 법적 책임이 엄격하지만, 베트남은 품질 기준이 낮고 불량 시공에 대한 처벌도 약합니다. 베트남 현장에서는 저가 입찰로 인해 시공사가 원가 절감을 위해 저품질 자재를 사용하거나 부실 시공을 하는 경우가 많으며, 준공 후 몇 년 내에 하자가 발생하는 경우도 흔합니다. 한국 기업이 베트남에서 건설 프로젝트를 진행할 때는 품질 기준을 계약서에 명확히 명시하고, 자재 품질 검증 및 시공 과정 감리를 철저히 해야 합니다. 통역사는 한국 측의 품질 요구 수준을 베트남 시공사에 명확히 전달하는 것이 중요합니다.",
            "commonMistakes": [
                {
                    "mistake": "phẩm chất công trình",
                    "correction": "chất lượng công trình",
                    "explanation": "'phẩm chất'는 사람의 품성을 의미하고, 물건의 품질은 'chất lượng'입니다."
                },
                {
                    "mistake": "tiêu chuẩn công trình",
                    "correction": "chất lượng công trình",
                    "explanation": "'tiêu chuẩn'은 기준(standard)이고, 'chất lượng'은 품질(quality)입니다."
                },
                {
                    "mistake": "건물기준",
                    "correction": "건물품질",
                    "explanation": "기준은 평가 척도이고, 품질은 실제 상태입니다."
                }
            ],
            "examples": [
                {
                    "ko": "이 건물은 국제 표준에 맞는 건물품질을 자랑합니다.",
                    "vi": "Công trình này đảm bảo chất lượng công trình theo tiêu chuẩn quốc tế.",
                    "situation": "formal"
                },
                {
                    "ko": "건물품질 검사 결과 여러 하자가 발견되었습니다.",
                    "vi": "Kết quả kiểm tra chất lượng công trình đã phát hiện nhiều khuyết tật.",
                    "situation": "onsite"
                },
                {
                    "ko": "시공사는 건물품질 보증서를 제공해야 합니다.",
                    "vi": "Nhà thầu xây dựng phải cung cấp giấy bảo hành chất lượng công trình.",
                    "situation": "formal"
                }
            ],
            "relatedTerms": ["giam-sat-xay-dung", "nghiem-thu-cong-trinh", "bao-hanh-cong-trinh", "ha-ja-bao-su"]
        },
        {
            "slug": "vi-pham-xay-dung",
            "korean": "건축법위반",
            "vietnamese": "vi phạm xây dựng",
            "hanja": "建築法違反",
            "hanjaReading": "建(세울 건) + 築(쌓을 축) + 法(법 법) + 違(어긋날 위) + 反(돌이킬 반)",
            "pronunciation": "건축법위반",
            "meaningKo": "건축법 또는 관련 법규를 준수하지 않고 건축물을 건축, 사용, 유지하는 행위로, 법적 처벌 대상입니다. 통역 시 주의할 점은 한국은 건축법 위반에 대한 처벌이 엄격하고(이행강제금, 형사처벌 등), 적발 시스템도 체계적이지만, 베트남은 법은 있으나 단속이 느슨하고 벌금도 낮아 위반이 만연하다는 점을 명확히 전달해야 합니다. 베트남에서는 불법 건축물이 많고, 심지어 정부 관료도 뇌물을 받고 묵인하는 경우가 있어, 한국 기업이 법을 철저히 준수해도 현지 경쟁사에 비해 불리할 수 있습니다.",
            "meaningVi": "Hành vi xây dựng, sử dụng, duy trì công trình không tuân thủ Luật Xây dựng hoặc các quy định pháp luật liên quan, bị xử phạt theo pháp luật. Tại Việt Nam, mặc dù có quy định xử phạt vi phạm xây dựng nhưng việc kiểm soát lỏng lẻo và mức phạt thấp khiến tình trạng vi phạm rất phổ biến, khác với Hàn Quốc nơi xử phạt nghiêm khắc và hệ thống giám sát chặt chẽ.",
            "context": "건축 행정, 법률 자문, 분쟁 해결",
            "culturalNote": "한국은 건축법 위반 시 이행강제금, 철거명령, 형사처벌 등 엄격한 제재가 가해지지만, 베트남은 벌금이 낮고(수백만~수천만 동), 집행도 느슨하여 불법 건축이 만연합니다. 베트남 도시에는 허가 없이 증축한 건물, 용도를 불법 변경한 건물이 흔하며, 심지어 정부 건물 옆에 불법 건축물이 버젓이 존재하기도 합니다. 이는 관료들이 뇌물을 받고 단속을 하지 않기 때문입니다. 한국 기업이 베트남에서 법을 철저히 준수하면 비용과 시간이 더 들어 현지 기업에 비해 경쟁력이 떨어질 수 있으므로, 이러한 딜레마를 이해하고 통역해야 합니다.",
            "commonMistakes": [
                {
                    "mistake": "phạm luật xây dựng",
                    "correction": "vi phạm xây dựng",
                    "explanation": "'phạm luật'는 '법을 범하다'는 동사구이고, 'vi phạm'은 위반 행위를 나타내는 명사입니다."
                },
                {
                    "mistake": "sai phạm xây dựng",
                    "correction": "vi phạm xây dựng",
                    "explanation": "'sai phạm'는 잘못/과오를 의미하고, 'vi phạm'는 법적 위반입니다."
                },
                {
                    "mistake": "건축위반",
                    "correction": "건축법위반",
                    "explanation": "법률 용어로는 '건축법위반'이 정확합니다."
                }
            ],
            "examples": [
                {
                    "ko": "이 건물은 건축법위반으로 철거 명령을 받았습니다.",
                    "vi": "Công trình này đã bị ra lệnh phá dỡ do vi phạm xây dựng.",
                    "situation": "formal"
                },
                {
                    "ko": "건축법위반 건물은 사용승인을 받을 수 없습니다.",
                    "vi": "Công trình vi phạm xây dựng không thể được cấp giấy phép sử dụng.",
                    "situation": "onsite"
                },
                {
                    "ko": "관계 당국이 건축법위반 건물에 대한 단속을 강화하고 있습니다.",
                    "vi": "Cơ quan chức năng đang tăng cường kiểm soát các công trình vi phạm xây dựng.",
                    "situation": "formal"
                }
            ],
            "relatedTerms": ["cong-trinh-trai-phep", "pha-do-cong-trinh", "giay-phep-xay-dung", "xu-phat-hanh-chinh"]
        },
        {
            "slug": "cong-trinh-trai-phep",
            "korean": "불법건축물",
            "vietnamese": "công trình trái phép",
            "hanja": "不法建築物",
            "hanjaReading": "不(아니 불) + 法(법 법) + 建(세울 건) + 築(쌓을 축) + 物(물건 물)",
            "pronunciation": "불법건축물",
            "meaningKo": "건축허가를 받지 않고 건축하거나, 허가 내용과 다르게 건축한 건축물로, 법적으로 철거 대상이 됩니다. 통역 시 주의할 점은 베트남에서 'công trình trái phép'가 매우 흔하며, 심지어 도심 중심부에도 불법 건축물이 많아 한국인에게는 충격적일 수 있다는 점을 명확히 전달해야 합니다. 베트남에서는 불법 건축물을 사후에 합법화하는 절차(hợp thức hóa)가 있어, 한국처럼 무조건 철거되는 것은 아니라는 점도 설명이 필요합니다. 한국 기업이 베트남 부동산을 매입할 때는 불법 건축물 여부를 철저히 확인해야 합니다.",
            "meaningVi": "Công trình xây dựng không có giấy phép hoặc xây dựng không đúng theo nội dung giấy phép, theo pháp luật phải bị phá dỡ. Tại Việt Nam, công trình trái phép rất phổ biến, thậm chí ở trung tâm thành phố cũng có nhiều công trình trái phép. Khác với Hàn Quốc nơi công trình trái phép bị phá dỡ ngay, Việt Nam có thủ tục hợp thức hóa để biến công trình trái phép thành hợp pháp.",
            "context": "부동산 거래, 건축 행정, 법률 분쟁",
            "culturalNote": "한국은 불법 건축물에 대한 철거가 엄격하게 집행되지만, 베트남은 불법 건축물이 수십 년간 방치되거나, 심지어 정부가 사후에 합법화해주는 경우도 있습니다. 베트남에서는 토지가 국유이기 때문에 개인이 토지를 소유하지 못하고 사용권만 가지는데, 이로 인해 불법 건축에 대한 책임 소재가 모호합니다. 또한 지방 정부가 세수 확보를 위해 불법 건축물에 사후 허가를 내주고 벌금을 받는 경우도 있어, 한국의 상식으로는 이해하기 어려운 상황이 많습니다. 통역사는 이러한 문화적, 제도적 차이를 이해하고 한국 측에 정확히 설명해야 합니다.",
            "commonMistakes": [
                {
                    "mistake": "công trình bất hợp pháp",
                    "correction": "công trình trái phép",
                    "explanation": "'bất hợp pháp'는 일반적인 불법이고, 'trái phép'는 허가 없음을 강조합니다."
                },
                {
                    "mistake": "công trình vi phạm",
                    "correction": "công trình trái phép",
                    "explanation": "'vi phạm'는 위반 행위이고, 'trái phép'는 허가 없는 건축물 자체입니다."
                },
                {
                    "mistake": "무허가건물",
                    "correction": "불법건축물",
                    "explanation": "법률 용어로는 '불법건축물'이 정확합니다."
                }
            ],
            "examples": [
                {
                    "ko": "이 건물은 불법건축물로 판명되어 매매가 불가능합니다.",
                    "vi": "Công trình này đã được xác định là công trình trái phép nên không thể mua bán.",
                    "situation": "formal"
                },
                {
                    "ko": "불법건축물을 매입하면 법적 분쟁에 휘말릴 수 있습니다.",
                    "vi": "Nếu mua công trình trái phép có thể gặp tranh chấp pháp lý.",
                    "situation": "onsite"
                },
                {
                    "ko": "정부가 불법건축물 단속 캠페인을 시작했습니다.",
                    "vi": "Chính phủ đã bắt đầu chiến dịch kiểm soát các công trình trái phép.",
                    "situation": "formal"
                }
            ],
            "relatedTerms": ["vi-pham-xay-dung", "pha-do-cong-trinh", "giay-phep-xay-dung", "hop-thuc-hoa-cong-trinh"]
        },
        {
            "slug": "pha-do-cong-trinh",
            "korean": "건물철거",
            "vietnamese": "phá dỡ công trình",
            "hanja": "建物撤去",
            "hanjaReading": "建(세울 건) + 物(물건 물) + 撤(걷을 철) + 去(갈 거)",
            "pronunciation": "건물철거",
            "meaningKo": "안전상 위험하거나 불법으로 건축된 건축물을 물리적으로 해체하여 제거하는 행위. 통역 시 주의할 점은 한국은 철거 절차가 법적으로 엄격하고 보상 제도가 체계적이지만, 베트남은 철거 과정에서 주민과의 마찰이 많고, 보상이 불충분하여 강제 철거 시 폭력 사태가 발생하는 경우도 있다는 점을 명확히 전달해야 합니다. 특히 베트남에서는 토지 보상금이 시장 가격보다 훨씬 낮고, 이주 대책도 미흡하여 철거민들이 극렬 저항하는 경우가 많으며, 이로 인해 개발 프로젝트가 수년간 지연되기도 합니다.",
            "meaningVi": "Hành động tháo dỡ vật lý công trình xây dựng nguy hiểm hoặc xây dựng trái phép. Tại Việt Nam, quá trình phá dỡ thường gặp xung đột với cư dân do chế độ bồi thường không thỏa đáng, thậm chí có trường hợp xảy ra bạo lực khi cưỡng chế phá dỡ. Đền bù đất đai thường thấp hơn nhiều so với giá thị trường và chính sách tái định cư không đầy đủ khiến dân chúng phản kháng quyết liệt.",
            "context": "도시 재개발, 행정 대집행, 안전 조치",
            "culturalNote": "한국은 재개발 시 조합 설립, 동의율 확보, 보상 협의 등 법적 절차가 복잡하지만 대체로 준수되는 반면, 베트남은 토지가 국유이기 때문에 정부가 강제 수용할 수 있고, 보상금도 정부가 일방적으로 결정하여 주민들이 불만을 가지는 경우가 많습니다. 베트남에서는 철거 반대 시위가 유혈 사태로 번지거나, 철거민이 분신하는 극단적 상황도 발생합니다. 한국 기업이 베트남에서 재개발 사업에 참여할 때는 이러한 사회적 갈등을 고려하고, 현지 주민과의 소통에 신경 써야 합니다. 통역사는 이러한 민감한 사회 문제를 이해하고 양측의 입장을 균형 있게 전달해야 합니다.",
            "commonMistakes": [
                {
                    "mistake": "phá hủy công trình",
                    "correction": "phá dỡ công trình",
                    "explanation": "'phá hủy'는 파괴(destruction)이고, 'phá dỡ'는 철거(demolition)입니다."
                },
                {
                    "mistake": "tháo dỡ công trình",
                    "correction": "phá dỡ công trình",
                    "explanation": "'tháo dỡ'는 분해(disassembly)이고, 'phá dỡ'는 철거입니다."
                },
                {
                    "mistake": "건물파괴",
                    "correction": "건물철거",
                    "explanation": "파괴는 무분별한 행위이고, 철거는 법적 절차에 따른 행위입니다."
                }
            ],
            "examples": [
                {
                    "ko": "이 불법건축물은 다음 주에 건물철거될 예정입니다.",
                    "vi": "Công trình trái phép này sẽ bị phá dỡ vào tuần sau.",
                    "situation": "formal"
                },
                {
                    "ko": "안전상 위험한 건물에 대해 긴급 건물철거 명령이 내려졌습니다.",
                    "vi": "Đã có lệnh phá dỡ khẩn cấp đối với công trình nguy hiểm về mặt an toàn.",
                    "situation": "onsite"
                },
                {
                    "ko": "재개발 지역의 건물철거 작업이 주민 반대로 중단되었습니다.",
                    "vi": "Công việc phá dỡ công trình tại khu tái phát triển đã bị dừng do cư dân phản đối.",
                    "situation": "formal"
                }
            ],
            "relatedTerms": ["cong-trinh-trai-phep", "vi-pham-xay-dung", "tai-dinh-cu", "boi-thuong-giai-toa"]
        },
        {
            "slug": "bao-hiem-xay-dung",
            "korean": "건설보험",
            "vietnamese": "bảo hiểm xây dựng",
            "hanja": "建設保險",
            "hanjaReading": "建(세울 건) + 設(베풀 설) + 保(지킬 보) + 險(험할 험)",
            "pronunciation": "건설보험",
            "meaningKo": "건설공사 중 발생할 수 있는 각종 위험(화재, 붕괴, 사고 등)에 대비하여 가입하는 보험으로, 공사비, 제3자 배상책임 등을 보장합니다. 통역 시 주의할 점은 한국은 건설공사보험 가입이 의무화되어 있고 보험 시장이 발달했지만, 베트남은 보험 가입이 선택 사항인 경우가 많고, 보험 상품도 한정적이며, 보험금 지급이 지연되거나 거부되는 경우가 흔하다는 점을 명확히 전달해야 합니다. 한국 기업이 베트남에서 시공할 때는 한국의 보험사나 국제 보험사를 통해 보험에 가입하는 것이 안전합니다.",
            "meaningVi": "Bảo hiểm để phòng ngừa các rủi ro có thể xảy ra trong quá trình xây dựng (hỏa hoạn, sụp đổ, tai nạn...), bảo vệ chi phí công trình và trách nhiệm bồi thường cho bên thứ ba. Tại Việt Nam, việc mua bảo hiểm xây dựng thường là tùy chọn, thị trường bảo hiểm còn hạn chế và việc chi trả bảo hiểm thường bị chậm trễ hoặc từ chối.",
            "context": "건설 계약, 리스크 관리, 사고 보상",
            "culturalNote": "한국은 건설공사보험, 배상책임보험 등이 의무화되어 있고, 보험 상품이 다양하며, 보험금 지급도 비교적 신속하지만, 베트남은 보험 산업이 미발달하여 건설보험 가입률이 낮고, 보험 약관도 불명확하며, 사고 발생 시 보험사가 보험금 지급을 회피하려는 경향이 있습니다. 베트남 현지 보험사는 신뢰도가 낮고, 보험금 지급 과정에서 분쟁이 발생하는 경우가 많아, 한국 기업들은 한국 보험사의 해외 건설보험이나 AIG, Allianz 같은 글로벌 보험사를 선호합니다. 통역사는 한국 측에 베트남 보험 시장의 한계를 명확히 전달하여 리스크 관리에 도움을 줘야 합니다.",
            "commonMistakes": [
                {
                    "mistake": "bảo vệ xây dựng",
                    "correction": "bảo hiểm xây dựng",
                    "explanation": "'bảo vệ'는 보호(protection)이고, 'bảo hiểm'은 보험(insurance)입니다."
                },
                {
                    "mistake": "an toàn xây dựng",
                    "correction": "bảo hiểm xây dựng",
                    "explanation": "'an toàn'은 안전(safety)이고, 'bảo hiểm'은 보험입니다."
                },
                {
                    "mistake": "건설안전",
                    "correction": "건설보험",
                    "explanation": "안전은 사고 예방이고, 보험은 사고 발생 시 재정적 보호입니다."
                }
            ],
            "examples": [
                {
                    "ko": "이 프로젝트는 국제 보험사의 건설보험에 가입되어 있습니다.",
                    "vi": "Dự án này đã tham gia bảo hiểm xây dựng của công ty bảo hiểm quốc tế.",
                    "situation": "formal"
                },
                {
                    "ko": "건설보험 가입 증명서를 제출해야 공사를 시작할 수 있습니다.",
                    "vi": "Phải nộp giấy chứng nhận tham gia bảo hiểm xây dựng mới có thể bắt đầu thi công.",
                    "situation": "onsite"
                },
                {
                    "ko": "현장 사고로 인한 손실은 건설보험으로 보상받았습니다.",
                    "vi": "Thiệt hại do tai nạn tại công trường đã được bồi thường từ bảo hiểm xây dựng.",
                    "situation": "formal"
                }
            ],
            "relatedTerms": ["an-toan-xay-dung", "giam-sat-xay-dung", "boi-thuong-tai-nan", "hop-dong-xay-dung"]
        }
    ]

    # 중복 제거 후 추가
    unique_terms = [t for t in new_terms if t['slug'] not in existing_slugs]

    if not unique_terms:
        print("⚠️  모든 용어가 이미 존재합니다. 추가할 용어 없음.")
        return

    # 기존 데이터에 추가
    data.extend(unique_terms)

    # 파일 저장 (UTF-8, ensure_ascii=False, indent=2)
    with open(file_path, 'w', encoding='utf-8') as f:
        json.dump(data, f, ensure_ascii=False, indent=2)

    print(f"✅ {len(unique_terms)}개 용어 추가 완료!")
    print(f"📍 파일: {file_path}")
    print(f"📊 전체 용어 수: {len(data)}개")

    for term in unique_terms:
        print(f"   - {term['slug']}: {term['korean']} ({term['vietnamese']})")

if __name__ == "__main__":
    main()
