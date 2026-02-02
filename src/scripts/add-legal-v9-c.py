#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""식품안전법 용어 추가 (v9-c)"""
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
            "slug": "ve-sinh-thuc-pham",
            "korean": "식품위생",
            "vietnamese": "Vệ sinh thực phẩm",
            "hanja": "食品衛生",
            "hanjaReading": "食(밥 식) + 品(물건 품) + 衛(지킬 위) + 生(날 생)",
            "pronunciation": "식품위생",
            "meaningKo": "식품의 안전성을 확보하고 국민 건강을 보호하기 위한 위생 관리 체계를 말합니다. 통역 시 한국 식품위생법은 제조·가공·조리·저장·운반 전 과정을 규율하며, 위생등급제와 정기 점검을 통해 관리하고, 위반 시 영업정지·과징금·형사처벌이 가능하다는 점을 명확히 전달해야 합니다. 식품위생법은 식품안전의 기본법입니다.",
            "meaningVi": "Hệ thống quản lý vệ sinh để đảm bảo an toàn thực phẩm và bảo vệ sức khỏe người dân. Luật vệ sinh thực phẩm Hàn Quốc quy định toàn bộ quy trình sản xuất, chế biến, nấu nướng, bảo quản, vận chuyển, có chế độ phân hạng vệ sinh và kiểm tra định kỳ, vi phạm có thể bị đình chỉ kinh doanh, phạt tiền, xử lý hình sự.",
            "context": "식품 제조·유통업체 위생 점검 및 행정처분 상황에서 사용",
            "culturalNote": "한국은 1960년대부터 식품위생법을 시행하며 높은 수준의 위생 관리 체계를 구축했습니다. 식약처가 전국 식품 업소를 정기 점검하며, 위생등급제를 통해 소비자에게 정보를 공개합니다. 베트남도 식품위생법이 있으나 영세 업체가 많아 관리가 어렵습니다. 통역 시 한국의 체계적인 점검 시스템과 높은 처벌 수위를 설명해야 합니다.",
            "commonMistakes": [
                {
                    "mistake": "vệ sinh ăn uống",
                    "correction": "vệ sinh thực phẩm (식품 전반)",
                    "explanation": "'음식 위생'은 조리·제공만 의미하며 제조·유통이 누락됩니다"
                },
                {
                    "mistake": "an toàn thực phẩm",
                    "correction": "vệ sinh thực phẩm (위생 관리) vs an toàn thực phẩm (안전성)",
                    "explanation": "'식품안전'은 결과이며 '식품위생'은 과정·관리 체계로 구분됩니다"
                },
                {
                    "mistake": "sạch sẽ thức ăn",
                    "correction": "vệ sinh thực phẩm (법적 기준)",
                    "explanation": "'음식 청결'은 일상 표현이며 법적 위생 기준의 개념이 누락됩니다"
                }
            ],
            "examples": [
                {
                    "ko": "이 식당은 식품위생법 위반으로 영업정지 2개월 처분을 받았습니다",
                    "vi": "Nhà hàng này bị đình chỉ 2 tháng vì vi phạm Luật vệ sinh thực phẩm",
                    "situation": "formal"
                },
                {
                    "ko": "식품위생 교육은 언제 받아야 하나요?",
                    "vi": "Khi nào phải tham gia đào tạo vệ sinh thực phẩm?",
                    "situation": "onsite"
                },
                {
                    "ko": "식품 제조업체는 연 2회 위생 점검을 받습니다",
                    "vi": "Doanh nghiệp sản xuất thực phẩm phải chịu kiểm tra vệ sinh 2 lần/năm",
                    "situation": "formal"
                }
            ],
            "relatedTerms": ["식품안전", "HACCP", "식약처", "위생등급"]
        },
        {
            "slug": "haccp",
            "korean": "해썹",
            "vietnamese": "HACCP",
            "hanja": None,
            "hanjaReading": None,
            "pronunciation": "해썹",
            "meaningKo": "식품의 원료 생산부터 최종 소비까지 각 단계에서 위해요소를 분석하고 중요관리점을 정하여 관리하는 과학적 위생관리 체계입니다. 통역 시 Hazard Analysis Critical Control Point의 약자이며, 한국은 일정 규모 이상 식품 제조업체에 HACCP 인증을 의무화하고, 위반 시 인증 취소와 과징금이 부과된다는 점을 명확히 전달해야 합니다.",
            "meaningVi": "Hệ thống quản lý vệ sinh khoa học phân tích yếu tố nguy hại và xác định điểm kiểm soát quan trọng từ sản xuất nguyên liệu đến tiêu dùng cuối cùng. Viết tắt của Hazard Analysis Critical Control Point, Hàn Quốc bắt buộc doanh nghiệp sản xuất thực phẩm quy mô nhất định phải có chứng nhận HACCP, vi phạm sẽ bị thu hồi chứng nhận và phạt tiền.",
            "context": "식품 제조업체 HACCP 인증 및 관리 상황에서 사용",
            "culturalNote": "한국은 1995년 HACCP 제도를 도입하여 2014년부터 단계적 의무화를 시행했습니다. 현재 집단급식소·어육가공품·냉동식품 등은 필수 인증이며, 식약처가 매년 점검합니다. 베트남도 HACCP 개념은 있으나 의무 적용 범위가 좁습니다. 통역 시 HACCP는 고유명사이므로 번역하지 않고 원어로 사용하며, 약자의 의미를 설명해야 합니다.",
            "commonMistakes": [
                {
                    "mistake": "hệ thống kiểm soát vệ sinh",
                    "correction": "HACCP (국제 표준 용어)",
                    "explanation": "'위생 통제 시스템'은 번역이지만 HACCP는 고유명사로 원어 사용이 원칙입니다"
                },
                {
                    "mistake": "chứng nhận an toàn",
                    "correction": "chứng nhận HACCP",
                    "explanation": "'안전 인증'은 포괄적이며 HACCP의 구체적 의미가 누락됩니다"
                },
                {
                    "mistake": "quản lý chất lượng",
                    "correction": "HACCP (위해요소 중점 관리)",
                    "explanation": "'품질 관리'는 일반 품질을 의미하며 위해요소 중점 관리와 다릅니다"
                }
            ],
            "examples": [
                {
                    "ko": "이 업체는 HACCP 인증을 받아 위생 관리가 우수합니다",
                    "vi": "Doanh nghiệp này có chứng nhận HACCP nên quản lý vệ sinh xuất sắc",
                    "situation": "formal"
                },
                {
                    "ko": "HACCP 인증 받으려면 뭐가 필요한가요?",
                    "vi": "Muốn nhận chứng nhận HACCP cần gì?",
                    "situation": "onsite"
                },
                {
                    "ko": "집단급식소는 HACCP 의무 적용 대상입니다",
                    "vi": "Bếp ăn tập thể là đối tượng bắt buộc áp dụng HACCP",
                    "situation": "formal"
                }
            ],
            "relatedTerms": ["식품위생", "위해요소", "중요관리점", "식품안전"]
        },
        {
            "slug": "phu-gia-thuc-pham",
            "korean": "식품첨가물",
            "vietnamese": "Phụ gia thực phẩm",
            "hanja": "食品添加物",
            "hanjaReading": "食(밥 식) + 品(물건 품) + 添(더할 첨) + 加(더할 가) + 物(물건 물)",
            "pronunciation": "식품첨가물",
            "meaningKo": "식품의 제조·가공·보존 과정에서 품질 개선이나 저장성 향상을 위해 첨가하는 물질입니다. 통역 시 한국은 식약처가 안전성을 평가하여 허용 목록을 지정하고, 사용 기준(용도·대상 식품·사용량)을 엄격히 관리하며, 무허가 첨가물 사용 시 5년 이하 징역 또는 5천만 원 이하 벌금에 처해진다는 점을 명확히 전달해야 합니다.",
            "meaningVi": "Chất được thêm vào trong quá trình sản xuất, chế biến, bảo quản thực phẩm để cải thiện chất lượng hoặc tăng khả năng bảo quản. Ở Hàn Quốc Cục Quản lý Thực phẩm và Dược phẩm đánh giá an toàn và chỉ định danh sách cho phép, quản lý chặt chẽ tiêu chuẩn sử dụng (mục đích, thực phẩm đối tượng, liều lượng), sử dụng phụ gia không phép bị phạt tù 5 năm hoặc phạt tiền đến 50 triệu won.",
            "context": "식품 제조 시 첨가물 사용 기준 및 단속 상황에서 사용",
            "culturalNote": "한국은 600여 종의 식품첨가물을 허가하며 용도별(보존료·착색료·감미료 등)로 분류합니다. 천연 첨가물과 화학적 합성품을 구분하며, 식품에 반드시 표시해야 합니다. 베트남도 식품첨가물 관리 제도가 있으나 허가 목록이 한국보다 적습니다. 통역 시 한국의 엄격한 사용 기준과 표시 의무를 설명해야 합니다.",
            "commonMistakes": [
                {
                    "mistake": "chất phụ gia",
                    "correction": "phụ gia thực phẩm",
                    "explanation": "'첨가제'는 포괄적이며 식품용임을 명시해야 합니다"
                },
                {
                    "mistake": "hóa chất thực phẩm",
                    "correction": "phụ gia thực phẩm (허가된 물질)",
                    "explanation": "'식품 화학물질'은 부정적 뉘앙스이며 합법적 첨가물의 의미가 약화됩니다"
                },
                {
                    "mistake": "chất bảo quản",
                    "correction": "phụ gia thực phẩm (bảo quản là một loại)",
                    "explanation": "'보존료'는 첨가물의 한 종류이며 전체를 대표하지 못합니다"
                }
            ],
            "examples": [
                {
                    "ko": "이 제품은 식품첨가물 사용 기준을 초과하여 회수 조치되었습니다",
                    "vi": "Sản phẩm này bị thu hồi vì vượt tiêu chuẩn sử dụng phụ gia thực phẩm",
                    "situation": "formal"
                },
                {
                    "ko": "이 첨가물 써도 되나요? 허가된 건가요?",
                    "vi": "Dùng phụ gia này được không? Có được phép không?",
                    "situation": "onsite"
                },
                {
                    "ko": "식품첨가물은 제품에 반드시 표시해야 합니다",
                    "vi": "Phụ gia thực phẩm phải được ghi rõ trên sản phẩm",
                    "situation": "formal"
                }
            ],
            "relatedTerms": ["보존료", "착색료", "감미료", "식품표시"]
        },
        {
            "slug": "ghi-nhan-xuat-xu",
            "korean": "원산지표시",
            "vietnamese": "Ghi nhãn xuất xứ",
            "hanja": "原産地標示",
            "hanjaReading": "原(근본 원) + 産(낳을 산) + 地(땅 지) + 標(표 표) + 示(보일 시)",
            "pronunciation": "원산지표시",
            "meaningKo": "농수산물과 가공식품의 생산지를 소비자에게 알리기 위해 표시하는 제도입니다. 통역 시 한국은 원산지 표시법으로 음식점·유통업체·가공업체 모두에게 표시 의무를 부과하며, 거짓 표시 시 7년 이하 징역 또는 1억 원 이하 벌금에 처해지고, 소비자는 손해배상을 청구할 수 있다는 점을 명확히 전달해야 합니다.",
            "meaningVi": "Chế độ ghi nhãn nơi sản xuất nông thủy sản và thực phẩm chế biến để thông báo cho người tiêu dùng. Ở Hàn Quốc Luật ghi nhãn xuất xứ bắt buộc tất cả nhà hàng, doanh nghiệp phân phối, chế biến phải ghi, ghi sai bị phạt tù 7 năm hoặc phạt tiền đến 100 triệu won, người tiêu dùng có thể yêu cầu bồi thường thiệt hại.",
            "context": "식당·유통업체 원산지 표시 단속 및 위반 처분 상황에서 사용",
            "culturalNote": "한국은 2008년 미국산 쇠고기 파동 이후 원산지 표시를 대폭 강화했습니다. 쇠고기·돼지고기·닭고기·쌀·배추김치 등은 음식점에서도 필수 표시이며, 허위 표시 시 징역형까지 가능합니다. 베트남도 원산지 표시 제도가 있으나 음식점 적용은 제한적입니다. 통역 시 한국의 엄격한 표시 의무와 높은 처벌 수위를 설명해야 합니다.",
            "commonMistakes": [
                {
                    "mistake": "nhãn nguồn gốc",
                    "correction": "ghi nhãn xuất xứ (원산지표시)",
                    "explanation": "'출처 라벨'은 모호하며 법률 용어로 정확하지 않습니다"
                },
                {
                    "mistake": "nơi sản xuất",
                    "correction": "ghi nhãn xuất xứ (표시 의무)",
                    "explanation": "'생산지'는 정보이며 표시 의무의 법적 성격이 누락됩니다"
                },
                {
                    "mistake": "xuất xứ hàng hóa",
                    "correction": "ghi nhãn xuất xứ (thực phẩm 중심)",
                    "explanation": "'상품 원산지'는 일반 상품을 의미하며 식품의 특수성이 약화됩니다"
                }
            ],
            "examples": [
                {
                    "ko": "이 음식점은 쇠고기 원산지를 허위로 표시하여 형사 고발되었습니다",
                    "vi": "Nhà hàng này bị truy tố hình sự vì ghi sai xuất xứ thịt bò",
                    "situation": "formal"
                },
                {
                    "ko": "메뉴판에 원산지 어떻게 써야 하나요?",
                    "vi": "Trên thực đơn ghi xuất xứ thế nào?",
                    "situation": "onsite"
                },
                {
                    "ko": "원산지 표시 위반 시 최대 7년 징역이 가능합니다",
                    "vi": "Vi phạm ghi nhãn xuất xứ có thể bị tù đến 7 năm",
                    "situation": "formal"
                }
            ],
            "relatedTerms": ["허위표시", "식품표시", "소비자보호", "과징금"]
        },
        {
            "slug": "thuc-pham-bien-doi-gen",
            "korean": "유전자변형식품",
            "vietnamese": "Thực phẩm biến đổi gen",
            "hanja": "遺傳子變形食品",
            "hanjaReading": "遺(남길 유) + 傳(전할 전) + 子(아들 자) + 變(변할 변) + 形(모양 형) + 食(밥 식) + 品(물건 품)",
            "pronunciation": "유전자변형식품",
            "meaningKo": "인위적으로 유전자를 재조합하거나 유전자를 구성하는 핵산을 직접 주입하는 기술을 활용하여 재배·육성된 농·축·수산물과 이를 원료로 제조·가공한 식품을 말합니다. 통역 시 한국은 GMO 표시를 의무화하며, 비의도적 혼입 3% 초과 시 표시해야 하고, 미표시 시 3년 이하 징역 또는 3천만 원 이하 벌금에 처해진다는 점을 명확히 전달해야 합니다.",
            "meaningVi": "Nông, súc, thủy sản được trồng/nuôi bằng công nghệ tái tổ hợp gen nhân tạo hoặc tiêm trực tiếp axit nucleic cấu thành gen và thực phẩm sản xuất/chế biến từ đó. Ở Hàn Quốc bắt buộc ghi nhãn GMO, phải ghi nếu lẫn không chủ ý trên 3%, không ghi bị phạt tù 3 năm hoặc phạt tiền đến 30 triệu won.",
            "context": "GMO 식품 수입·유통 및 표시 의무 상황에서 사용",
            "culturalNote": "한국은 GMO 표시 제도를 운영하지만 간장·식용유 등 DNA가 남지 않는 가공식품은 표시 예외입니다. 소비자단체는 표시 강화를 요구하지만 업계는 부담을 호소합니다. 베트남은 GMO 표시 제도가 미비합니다. 통역 시 GMO는 Genetically Modified Organism의 약자로 원어 사용이 일반적이며, 한국의 3% 기준을 설명해야 합니다.",
            "commonMistakes": [
                {
                    "mistake": "thực phẩm GMO",
                    "correction": "thực phẩm biến đổi gen (또는 GMO)",
                    "explanation": "GMO도 맞지만 공식 용어는 '유전자변형식품'이며 통역 시 둘 다 사용 가능합니다"
                },
                {
                    "mistake": "thực phẩm chuyển gen",
                    "correction": "thực phẩm biến đổi gen",
                    "explanation": "'전이유전자 식품'은 중국 용어이며 한국은 '변형'을 사용합니다"
                },
                {
                    "mistake": "cây trồng biến đổi gen",
                    "correction": "thực phẩm biến đổi gen (원료 + 가공품)",
                    "explanation": "'변형작물'은 원료만 의미하며 가공식품이 누락됩니다"
                }
            ],
            "examples": [
                {
                    "ko": "이 콩은 유전자변형식품으로 GMO 표시가 되어 있습니다",
                    "vi": "Đậu nành này là thực phẩm biến đổi gen và có ghi nhãn GMO",
                    "situation": "formal"
                },
                {
                    "ko": "GMO 안 쓴 제품은 어떻게 알아요?",
                    "vi": "Sản phẩm không dùng GMO biết thế nào?",
                    "situation": "onsite"
                },
                {
                    "ko": "유전자변형식품 미표시 시 형사처벌을 받습니다",
                    "vi": "Không ghi nhãn thực phẩm biến đổi gen sẽ bị xử lý hình sự",
                    "situation": "formal"
                }
            ],
            "relatedTerms": ["GMO표시", "식품표시", "유전자재조합", "식품안전"]
        },
        {
            "slug": "ngo-doc-thuc-pham",
            "korean": "식중독",
            "vietnamese": "Ngộ độc thực phẩm",
            "hanja": "食中毒",
            "hanjaReading": "食(밥 식) + 中(가운데 중) + 毒(독 독)",
            "pronunciation": "식중독",
            "meaningKo": "식품의 섭취로 인하여 인체에 유해한 미생물 또는 유독물질에 의해 발생하는 질병을 말합니다. 통역 시 한국은 식중독 발생 시 관할 보건소에 즉시 신고 의무가 있으며, 집단 식중독(2인 이상) 발생 업소는 영업정지·과징금·손해배상 책임을 지고, 고의·중과실 시 형사처벌이 가능하다는 점을 명확히 전달해야 합니다.",
            "meaningVi": "Bệnh do vi sinh vật hoặc chất độc hại gây ra cho cơ thể người khi ăn thực phẩm. Ở Hàn Quốc khi xảy ra ngộ độc thực phẩm phải báo cáo ngay cho trạm y tế, cơ sở xảy ra ngộ độc tập thể (2 người trở lên) phải chịu đình chỉ kinh doanh, phạt tiền, trách nhiệm bồi thường thiệt hại, cố ý hoặc lỗi nghiêm trọng có thể bị xử lý hình sự.",
            "context": "식중독 발생 신고 및 행정처분 상황에서 사용",
            "culturalNote": "한국은 여름철 식중독 예방을 위해 집단급식소와 음식점을 집중 점검합니다. 식중독 발생 시 역학조사를 실시하며, 원인 규명과 확산 방지에 집중합니다. 베트남도 식중독이 빈번하나 신고·조사 체계가 약합니다. 통역 시 한국의 즉시 신고 의무와 집단 식중독의 엄격한 처벌을 설명해야 합니다.",
            "commonMistakes": [
                {
                    "mistake": "đau bụng do ăn",
                    "correction": "ngộ độc thực phẩm (의학적 진단)",
                    "explanation": "'먹고 배탈'은 일상 표현이며 법적·의학적 식중독의 개념이 누락됩니다"
                },
                {
                    "mistake": "nhiễm khuẩn thức ăn",
                    "correction": "ngộ độc thực phẩm (질병 결과)",
                    "explanation": "'음식 세균 감염'은 원인이며 식중독이라는 질병 개념이 약화됩니다"
                },
                {
                    "mistake": "bị độc",
                    "correction": "ngộ độc thực phẩm (식품 기인)",
                    "explanation": "'중독되다'는 일반 중독이며 식품으로 인한 중독임을 명시해야 합니다"
                }
            ],
            "examples": [
                {
                    "ko": "이 식당에서 집단 식중독이 발생하여 30명이 입원했습니다",
                    "vi": "Xảy ra ngộ độc thực phẩm tập thể tại nhà hàng này, 30 người nhập viện",
                    "situation": "formal"
                },
                {
                    "ko": "손님들이 구토한다는데 식중독인가요?",
                    "vi": "Khách nói bị nôn, có phải ngộ độc thực phẩm không?",
                    "situation": "onsite"
                },
                {
                    "ko": "식중독 발생 시 보건소에 즉시 신고해야 합니다",
                    "vi": "Khi xảy ra ngộ độc thực phẩm phải báo cáo ngay cho trạm y tế",
                    "situation": "formal"
                }
            ],
            "relatedTerms": ["집단급식소", "식품위생", "역학조사", "영업정지"]
        },
        {
            "slug": "tap-chat",
            "korean": "이물질",
            "vietnamese": "Tạp chất",
            "hanja": "異物質",
            "hanjaReading": "異(다를 이) + 物(물건 물) + 質(바탕 질)",
            "pronunciation": "이물질",
            "meaningKo": "식품에 혼입되어서는 안 되는 머리카락·곤충·금속·플라스틱 등 본래 포함되지 않아야 할 물질을 말합니다. 통역 시 한국은 이물질 혼입 식품을 회수·폐기하며, 고의 혼입 시 7년 이하 징역, 제조 과정의 과실 혼입도 과징금·영업정지 대상이며, 소비자는 손해배상을 청구할 수 있다는 점을 명확히 전달해야 합니다.",
            "meaningVi": "Vật chất không được phép lẫn vào thực phẩm như tóc, côn trùng, kim loại, nhựa. Ở Hàn Quốc thực phẩm có tạp chất phải thu hồi/tiêu hủy, cố ý lẫn bị phạt tù 7 năm, lẫn do sơ suất trong sản xuất cũng bị phạt tiền/đình chỉ kinh doanh, người tiêu dùng có thể yêu cầu bồi thường.",
            "context": "식품 이물질 신고 및 소비자 피해구제 상황에서 사용",
            "culturalNote": "한국은 이물질 신고 시 식약처와 소비자원이 조사하며, SNS 확산으로 기업 이미지 타격이 커서 기업들이 자체 품질관리를 강화하고 있습니다. 이물질 발견 시 신고하면 검사와 보상이 이루어집니다. 베트남도 이물질 문제가 있으나 신고·보상 체계가 약합니다. 통역 시 한국의 적극적 소비자 보호 제도를 설명해야 합니다.",
            "commonMistakes": [
                {
                    "mistake": "chất lạ",
                    "correction": "tạp chất (이물질)",
                    "explanation": "'낯선 물질'은 모호하며 식품 혼입물의 법적 개념이 약화됩니다"
                },
                {
                    "mistake": "vật thể lạ",
                    "correction": "tạp chất (trong thực phẩm)",
                    "explanation": "'이상한 물체'는 일상 표현이며 식품 안전의 법률 용어로 부적절합니다"
                },
                {
                    "mistake": "bẩn",
                    "correction": "tạp chất (구체적 혼입물)",
                    "explanation": "'더럽다'는 주관적 표현이며 객관적 이물질 개념이 누락됩니다"
                }
            ],
            "examples": [
                {
                    "ko": "라면에서 금속 이물질이 발견되어 전량 회수 조치되었습니다",
                    "vi": "Phát hiện tạp chất kim loại trong mì gói, toàn bộ bị thu hồi",
                    "situation": "formal"
                },
                {
                    "ko": "빵에서 머리카락 나왔는데 신고할 수 있나요?",
                    "vi": "Bánh có tóc, có thể báo cáo không?",
                    "situation": "onsite"
                },
                {
                    "ko": "이물질 혼입 제품은 소비자에게 배상해야 합니다",
                    "vi": "Sản phẩm có tạp chất phải bồi thường cho người tiêu dùng",
                    "situation": "formal"
                }
            ],
            "relatedTerms": ["제품회수", "소비자보호", "손해배상", "식품안전"]
        },
        {
            "slug": "thu-hoi-thuc-pham",
            "korean": "식품리콜",
            "vietnamese": "Thu hồi thực phẩm",
            "hanja": None,
            "hanjaReading": None,
            "pronunciation": "식품리콜",
            "meaningKo": "유통 중인 식품이 안전 기준에 부적합하거나 위해가 발생할 우려가 있을 때 제조·수입업체가 해당 제품을 회수하는 조치입니다. 통역 시 한국은 리콜을 자발적 회수와 행정명령 회수로 구분하며, 미이행 시 5년 이하 징역 또는 5천만 원 이하 벌금, 회수 비용은 업체 부담이며 소비자 환불이 의무화된다는 점을 명확히 전달해야 합니다.",
            "meaningVi": "Biện pháp nhà sản xuất/nhập khẩu thu hồi sản phẩm khi thực phẩm đang lưu thông không đạt tiêu chuẩn an toàn hoặc có nguy cơ gây hại. Ở Hàn Quốc chia thu hồi tự nguyện và thu hồi theo lệnh hành chính, không thực hiện bị phạt tù 5 năm hoặc phạt tiền đến 50 triệu won, chi phí thu hồi do doanh nghiệp chịu và bắt buộc hoàn tiền cho người tiêu dùng.",
            "context": "식품 리콜 명령 및 소비자 환불 절차에서 사용",
            "culturalNote": "한국은 식약처가 리콜 정보를 실시간 공개하며, 대형마트와 온라인몰이 협조하여 신속히 회수합니다. 리콜 등급(Class I~III)에 따라 시급성을 구분하며, Class I(생명 위협)은 즉시 회수됩니다. 베트남은 리콜 제도가 있으나 집행력이 약합니다. 통역 시 리콜은 영어 원어로 사용하며, 한국의 신속한 회수 시스템을 설명해야 합니다.",
            "commonMistakes": [
                {
                    "mistake": "thu hồi sản phẩm",
                    "correction": "thu hồi thực phẩm (식품 특화)",
                    "explanation": "'제품 회수'는 일반 상품이며 식품의 특수성이 누락됩니다"
                },
                {
                    "mistake": "gọi lại",
                    "correction": "thu hồi thực phẩm (recall)",
                    "explanation": "'다시 부르다'는 직역이며 리콜의 법적 의미가 약화됩니다"
                },
                {
                    "mistake": "rút sản phẩm",
                    "correction": "thu hồi thực phẩm (공식 절차)",
                    "explanation": "'제품 회수'는 자발적 철수처럼 들리며 법적 강제성이 누락됩니다"
                }
            ],
            "examples": [
                {
                    "ko": "이 제품은 대장균 검출로 전국 매장에서 식품리콜되었습니다",
                    "vi": "Sản phẩm này bị thu hồi thực phẩm tại tất cả cửa hàng toàn quốc do phát hiện E.coli",
                    "situation": "formal"
                },
                {
                    "ko": "리콜 제품 사봤는데 환불 받을 수 있나요?",
                    "vi": "Mua sản phẩm bị thu hồi rồi, có được hoàn tiền không?",
                    "situation": "onsite"
                },
                {
                    "ko": "식품리콜 정보는 식약처 홈페이지에서 확인할 수 있습니다",
                    "vi": "Thông tin thu hồi thực phẩm có thể kiểm tra trên trang web Cục Quản lý Thực phẩm và Dược phẩm",
                    "situation": "formal"
                }
            ],
            "relatedTerms": ["제품회수", "소비자환불", "식품안전", "식약처"]
        },
        {
            "slug": "nhan-dinh-duong",
            "korean": "영양표시",
            "vietnamese": "Nhãn dinh dưỡng",
            "hanja": "營養表示",
            "hanjaReading": "營(경영할 영) + 養(기를 양) + 表(겉 표) + 示(보일 시)",
            "pronunciation": "영양표시",
            "meaningKo": "식품의 영양성분과 함량을 제품 포장에 표시하여 소비자에게 영양 정보를 제공하는 제도입니다. 통역 시 한국은 가공식품에 열량·나트륨·탄수화물·당류·지방·단백질 등 9가지 의무 표시 항목이 있으며, 미표시 또는 허위 표시 시 3년 이하 징역 또는 3천만 원 이하 벌금에 처해진다는 점을 명확히 전달해야 합니다.",
            "meaningVi": "Chế độ ghi thành phần dinh dưỡng và hàm lượng trên bao bì sản phẩm để cung cấp thông tin dinh dưỡng cho người tiêu dùng. Ở Hàn Quốc thực phẩm chế biến có 9 mục bắt buộc ghi như năng lượng, natri, carbohydrate, đường, chất béo, protein, không ghi hoặc ghi sai bị phạt tù 3 năm hoặc phạt tiền đến 30 triệu won.",
            "context": "식품 제조업체 영양표시 점검 및 소비자 정보 제공 상황에서 사용",
            "culturalNote": "한국은 2007년부터 영양표시를 의무화했으며, 최근 당류·나트륨 저감 정책으로 표시가 더욱 강화되었습니다. 1회 제공량 기준과 100g/100mL 기준을 병기하며, %영양소기준치도 표시합니다. 베트남도 영양표시 제도가 있으나 의무 항목이 적습니다. 통역 시 한국의 상세한 표시 의무를 설명해야 합니다.",
            "commonMistakes": [
                {
                    "mistake": "thông tin dinh dưỡng",
                    "correction": "nhãn dinh dưỡng (표시 의무)",
                    "explanation": "'영양 정보'는 일반 정보이며 법적 표시 의무의 개념이 누락됩니다"
                },
                {
                    "mistake": "ghi chất dinh dưỡng",
                    "correction": "nhãn dinh dưỡng (영양표시)",
                    "explanation": "'영양소 기재'는 행위이며 제도로서의 영양표시 개념이 약화됩니다"
                },
                {
                    "mistake": "bảng thành phần",
                    "correction": "nhãn dinh dưỡng (영양 정보) vs bảng thành phần (원재료)",
                    "explanation": "'성분표'는 원재료 목록을 의미하며 영양표시와 구분됩니다"
                }
            ],
            "examples": [
                {
                    "ko": "이 제품은 나트륨 함량을 영양표시에서 누락하여 과징금이 부과되었습니다",
                    "vi": "Sản phẩm này bị phạt tiền vì thiếu hàm lượng natri trong nhãn dinh dưỡng",
                    "situation": "formal"
                },
                {
                    "ko": "영양표시 어떻게 만들어야 하나요?",
                    "vi": "Nhãn dinh dưỡng làm thế nào?",
                    "situation": "onsite"
                },
                {
                    "ko": "영양표시는 1회 제공량 기준으로 작성합니다",
                    "vi": "Nhãn dinh dưỡng được lập theo khẩu phần ăn 1 lần",
                    "situation": "formal"
                }
            ],
            "relatedTerms": ["식품표시", "나트륨", "열량", "1회제공량"]
        },
        {
            "slug": "thuc-pham-chuc-nang-suc-khoe",
            "korean": "건강기능식품",
            "vietnamese": "Thực phẩm chức năng sức khỏe",
            "hanja": "健康機能食品",
            "hanjaReading": "健(튼튼할 건) + 康(편안할 강) + 機(틀 기) + 能(능할 능) + 食(밥 식) + 品(물건 품)",
            "pronunciation": "건강기능식품",
            "meaningKo": "인체에 유용한 기능성을 가진 원료나 성분을 사용하여 제조·가공한 식품으로, 질병 치료가 아닌 건강 유지·개선을 목적으로 합니다. 통역 시 한국은 건강기능식품법으로 별도 규율하며, 식약처 인증을 받아야 하고, 기능성 표시는 인정받은 내용만 가능하며, 질병 치료 효과 표시 시 3년 이하 징역 또는 3천만 원 이하 벌금에 처해진다는 점을 명확히 전달해야 합니다.",
            "meaningVi": "Thực phẩm sản xuất, chế biến bằng nguyên liệu hoặc thành phần có chức năng hữu ích cho cơ thể người, mục đích duy trì/cải thiện sức khỏe chứ không phải chữa bệnh. Ở Hàn Quốc được quy định riêng bởi Luật thực phẩm chức năng sức khỏe, phải có chứng nhận của Cục Quản lý Thực phẩm và Dược phẩm, chỉ được ghi chức năng đã được công nhận, ghi hiệu quả chữa bệnh bị phạt tù 3 năm hoặc phạt tiền đến 30 triệu won.",
            "context": "건강기능식품 제조·수입 및 광고 규제 상황에서 사용",
            "culturalNote": "한국은 홍삼·프로바이오틱스·오메가3 등 건강기능식품 시장이 크며, 식약처가 기능성 원료를 고시하고 개별 인정합니다. 과대광고가 빈번하여 공정위와 식약처가 합동 단속하며, '질병 예방·치료' 표현은 엄격히 금지됩니다. 베트남도 건강보조식품 시장이 성장 중이나 규제가 약합니다. 통역 시 한국의 엄격한 기능성 표시 규제를 설명해야 합니다.",
            "commonMistakes": [
                {
                    "mistake": "thực phẩm bổ sung",
                    "correction": "thực phẩm chức năng sức khỏe (법적 용어)",
                    "explanation": "'보충식품'은 영어 supplement 번역이며 한국 법률 용어와 정확히 대응하지 않습니다"
                },
                {
                    "mistake": "thực phẩm tốt cho sức khỏe",
                    "correction": "thực phẩm chức năng sức khỏe (인증 제품)",
                    "explanation": "'건강에 좋은 식품'은 일반 표현이며 법적 인증의 개념이 누락됩니다"
                },
                {
                    "mistake": "vitamin và khoáng chất",
                    "correction": "thực phẩm chức năng sức khỏe (포괄적 개념)",
                    "explanation": "'비타민과 미네랄'은 건강기능식품의 일부이며 전체를 대표하지 못합니다"
                }
            ],
            "examples": [
                {
                    "ko": "이 제품은 건강기능식품 인증을 받지 않고 기능성을 표시하여 적발되었습니다",
                    "vi": "Sản phẩm này bị phát hiện vì ghi chức năng mà không có chứng nhận thực phẩm chức năng sức khỏe",
                    "situation": "formal"
                },
                {
                    "ko": "홍삼 제품 만들려는데 건강기능식품 인증 받아야 하나요?",
                    "vi": "Muốn sản xuất sản phẩm hồng sâm, có phải xin chứng nhận thực phẩm chức năng sức khỏe không?",
                    "situation": "onsite"
                },
                {
                    "ko": "건강기능식품은 질병 치료 효과를 표시할 수 없습니다",
                    "vi": "Thực phẩm chức năng sức khỏe không được ghi hiệu quả chữa bệnh",
                    "situation": "formal"
                }
            ],
            "relatedTerms": ["기능성표시", "식약처인증", "과대광고", "개별인정"]
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
    print(f"✅ Added {len(filtered)} terms (식품안전법). Total: {len(data)}")

if __name__ == '__main__':
    main()
