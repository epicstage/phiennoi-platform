#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
헌법/행정법 용어 추가 스크립트 (Constitutional/Administrative Law Terms)
Tier S 품질 기준 준수
"""

import json
import os

# 파일 경로 설정
file_path = os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', 'data', 'terms', 'legal.json')

# 기존 데이터 로드
with open(file_path, 'r', encoding='utf-8') as f:
    data = json.load(f)  # data is a LIST

# 기존 slug 추출
existing_slugs = {t['slug'] for t in data}

# 새 용어 정의
new_terms = [
    {
        "slug": "hien-phap",
        "korean": "헌법",
        "vietnamese": "Hiến pháp",
        "hanja": "憲法",
        "hanjaReading": "憲(법 헌) + 法(법 법)",
        "pronunciation": "헌법 - Hi-ến pháp",
        "meaningKo": "국가의 통치 조직과 국민의 기본권을 규정한 최고 법규. 통역 시 주의: 한국은 성문헌법 국가로 헌법재판소가 위헌심사를 하지만, 베트남은 국회 상임위원회가 헌법 해석권을 가진다는 점을 구분해야 함. '헌법 개정'을 통역할 때 한국은 국회 재적의원 2/3 찬성 + 국민투표가 필요하지만, 베트남은 국회 재적의원 2/3만으로 가능하다는 차이를 알아야 실수를 방지할 수 있음. 법률 통역 시 '위헌'과 '위법'을 명확히 구분하지 않으면 법적 오해가 발생할 수 있으므로 반드시 정확한 용어 선택이 필요함.",
        "meaningVi": "Đạo luật tối cao quy định về tổ chức bộ máy nhà nước và các quyền cơ bản của công dân. Hiến pháp Việt Nam do Quốc hội thông qua và sửa đổi, trong khi Hàn Quốc có Tòa án Hiến pháp riêng để xem xét tính hợp hiến. Sự khác biệt về quyền giải thích và sửa đổi Hiến pháp giữa hai nước cần được phân biệt rõ trong quá trình phiên dịch.",
        "context": "formal",
        "culturalNote": "한국의 헌법재판소 제도는 베트남에 존재하지 않으며, 베트남은 국회 상임위원회가 헌법 해석 및 감독 권한을 가짐. 한국 헌법은 1987년 민주화 이후 개정되지 않았으나, 베트남 헌법은 2013년 전면 개정됨. 헌법 개정 절차의 차이(한국: 국민투표 필수, 베트남: 국회만으로 가능)는 통역 시 반드시 설명해야 할 핵심 사항임. 또한 한국은 위헌법률심판제도가 발달했으나 베트남은 사후적 위헌심사 제도가 제한적이라는 점도 중요한 문화적 차이임.",
        "commonMistakes": [
            {
                "mistake": "헌법을 'luật hiến pháp'으로 번역",
                "correction": "'Hiến pháp'만으로 충분",
                "explanation": "Hiến pháp 자체가 이미 '헌법'을 의미하므로 luật(법률)를 앞에 붙이면 중복 표현이 됨"
            },
            {
                "mistake": "'위헌'과 '위법'을 모두 'vi phạm pháp luật'으로 통역",
                "correction": "위헌은 'vi hiến', 위법은 'vi phạm pháp luật'",
                "explanation": "위헌은 헌법 위반(constitutional violation), 위법은 일반 법률 위반으로 법적 의미가 완전히 다름"
            },
            {
                "mistake": "'헌법재판소'를 'Tòa án Hiến pháp'으로만 번역하고 설명 없이 넘어감",
                "correction": "'Tòa án Hiến pháp (cơ quan tư pháp độc lập của Hàn Quốc)'",
                "explanation": "베트남에는 해당 기관이 없으므로 추가 설명 없이 번역하면 청자가 이해하기 어려움"
            }
        ],
        "examples": [
            {
                "ko": "이 법률은 헌법에 위배되어 위헌 판결을 받았습니다.",
                "vi": "Luật này đã bị tuyên bố vi hiến vì trái với Hiến pháp.",
                "situation": "formal"
            },
            {
                "ko": "헌법 개정을 위해서는 국민투표가 필수입니다.",
                "vi": "Để sửa đổi Hiến pháp, cần phải có trưng cầu dân ý.",
                "situation": "formal"
            },
            {
                "ko": "헌법재판소는 이 사안에 대해 합헌 결정을 내렸습니다.",
                "vi": "Tòa án Hiến pháp Hàn Quốc đã ra quyết định hợp hiến cho vấn đề này.",
                "situation": "formal"
            }
        ],
        "relatedTerms": ["quoc-hoi", "co-quan-nha-nuoc", "quyen-con-nguoi"]
    },
    {
        "slug": "quoc-hoi",
        "korean": "국회",
        "vietnamese": "Quốc hội",
        "hanja": "國會",
        "hanjaReading": "國(나라 국) + 會(모일 회)",
        "pronunciation": "국회 - Quốc hội",
        "meaningKo": "국민을 대표하여 입법권을 행사하는 최고 의사기관. 통역 시 주의: 한국 국회는 단원제(300명)이며 임기 4년이지만, 베트남 Quốc hội는 단원제(500명)로 임기 5년이라는 차이가 있음. '국회의원'을 통역할 때 한국은 지역구+비례대표 혼합이지만 베트남은 지역 대표 중심이라는 선출 방식 차이를 이해해야 정확한 통역이 가능함. 국회의 권한 범위도 다르므로 '국회 동의'나 '국회 승인' 표현 시 양국의 제도적 차이를 고려해 통역해야 오해를 방지할 수 있음.",
        "meaningVi": "Cơ quan quyền lực nhà nước cao nhất, đại diện cho nhân dân, thực hiện quyền lập pháp. Quốc hội Việt Nam có 500 đại biểu với nhiệm kỳ 5 năm, trong khi Quốc hội Hàn Quốc có 300 nghị sĩ với nhiệm kỳ 4 năm. Quyền hạn và cách thức hoạt động của Quốc hội hai nước có sự khác biệt đáng kể cần lưu ý khi phiên dịch.",
        "context": "formal",
        "culturalNote": "한국 국회는 대통령제 하에서 견제와 균형의 원리로 작동하지만, 베트남 Quốc hội는 최고 권력기관으로서 국가주석과 정부를 선출하는 권한을 가짐. 한국은 여야 대립 구도가 명확하지만 베트남은 공산당 주도 하에 합의제로 운영됨. 국회의원 선출 방식도 다르며(한국: 지역구+정당명부, 베트남: 지역 대표 중심), 국회의 입법 절차와 권한 범위에서도 상당한 차이가 있어 통역 시 맥락 설명이 필수적임.",
        "commonMistakes": [
            {
                "mistake": "'국회의원'을 'nghị sĩ Quốc hội'와 'đại biểu Quốc hội' 중 구분 없이 사용",
                "correction": "한국은 'nghị sĩ Quốc hội', 베트남은 'đại biểu Quốc hội'",
                "explanation": "양국의 공식 명칭이 다르며, 역할과 권한에도 차이가 있으므로 정확한 용어 사용 필요"
            },
            {
                "mistake": "'국회 의결'을 'quyết định của Quốc hội'로만 번역",
                "correction": "'nghị quyết của Quốc hội' 또는 'biểu quyết của Quốc hội'",
                "explanation": "'quyết định'은 행정 결정을 의미하며, 입법 기관의 의결은 'nghị quyết'이 정확함"
            },
            {
                "mistake": "'국회 동의'와 '국회 승인'을 동일하게 'chấp thuận của Quốc hội'로 통역",
                "correction": "동의는 'đồng ý', 승인은 'phê chuẩn'으로 구분",
                "explanation": "법적 효력과 절차가 다른 개념이므로 명확히 구분해야 함"
            }
        ],
        "examples": [
            {
                "ko": "국회는 예산안을 심의하고 의결합니다.",
                "vi": "Quốc hội thẩm tra và biểu quyết dự toán ngân sách.",
                "situation": "formal"
            },
            {
                "ko": "이 법안은 국회 본회의를 통과했습니다.",
                "vi": "Dự luật này đã được thông qua tại phiên họp toàn thể Quốc hội.",
                "situation": "formal"
            },
            {
                "ko": "국회의원들이 정부 정책에 대해 질의했습니다.",
                "vi": "Các nghị sĩ Quốc hội đã chất vấn về chính sách của chính phủ.",
                "situation": "formal"
            }
        ],
        "relatedTerms": ["hien-phap", "chinh-phu", "quyen-bau-cu"]
    },
    {
        "slug": "chinh-phu",
        "korean": "정부",
        "vietnamese": "Chính phủ",
        "hanja": "政府",
        "hanjaReading": "政(정사 정) + 府(마을 부)",
        "pronunciation": "정부 - Chính phủ",
        "meaningKo": "국가의 행정권을 담당하는 집행기관. 통역 시 주의: 한국에서 '정부'는 행정부만을 의미하지만, 베트남에서 Chính phủ는 총리가 이끄는 행정 내각을 지칭함. '정부 발표'를 통역할 때 한국은 대통령실/각 부처를 모두 포함할 수 있으나, 베트남은 주로 총리실 또는 각 부(bộ) 발표를 의미하므로 맥락 파악이 중요함. 또한 '정부 정책'은 한국에서 대통령 주도가 강하지만 베트남은 당-국가-정부의 3중 구조를 이해해야 정확한 통역이 가능함.",
        "meaningVi": "Cơ quan hành chính nhà nước do Thủ tướng đứng đầu, thực hiện quyền hành pháp. Chính phủ Việt Nam do Quốc hội bầu ra và chịu trách nhiệm trước Quốc hội, trong khi Hàn Quốc theo chế độ tổng thống, Tổng thống trực tiếp lãnh đạo hành chính. Sự khác biệt về cấu trúc và quyền lực giữa hai nước cần được phân biệt rõ ràng.",
        "context": "formal",
        "culturalNote": "한국은 대통령제로 대통령이 행정부 수반이지만, 베트남은 총리가 정부(Chính phủ) 수반임. 한국의 '정부'는 넓게는 입법·사법·행정을 포괄하지만 좁게는 행정부만 지칭하는 반면, 베트nam의 Chính phủ는 명확히 행정 내각만을 의미함. 또한 베트남은 공산당이 국가를 영도하는 체제이므로 '당-국가-정부'의 관계를 이해하지 못하면 정책 결정 과정을 잘못 통역할 수 있음. 정부 조직 구조와 의사결정 절차의 차이도 통역 시 중요한 고려사항임.",
        "commonMistakes": [
            {
                "mistake": "한국의 '정부'를 항상 'Chính phủ'로만 번역",
                "correction": "맥락에 따라 'nhà nước'(국가) 또는 'chính quyền'(정권) 구분 필요",
                "explanation": "한국어 '정부'는 문맥에 따라 행정부, 국가 전체, 정권 등 다양한 의미로 쓰이므로 정확한 구분 필요"
            },
            {
                "mistake": "'정부 부처'를 'bộ phận chính phủ'로 번역",
                "correction": "'các bộ của Chính phủ' 또는 'bộ, ngành'",
                "explanation": "'bộ phận'은 조직 내 부분을 의미하며, 정부 부처는 'bộ'(部)가 정확한 표현"
            },
            {
                "mistake": "'정부 정책'을 통역할 때 주체를 명확히 하지 않음",
                "correction": "한국은 대통령/정부, 베트남은 당/정부 구분 필요",
                "explanation": "정책 결정 주체와 구조가 다르므로 누가 주도하는 정책인지 명확히 해야 함"
            }
        ],
        "examples": [
            {
                "ko": "정부는 경제 활성화를 위한 정책을 발표했습니다.",
                "vi": "Chính phủ đã công bố chính sách nhằm kích cầu kinh tế.",
                "situation": "formal"
            },
            {
                "ko": "이번 정부 조직 개편으로 새로운 부처가 신설됩니다.",
                "vi": "Với việc cải tổ bộ máy chính phủ lần này, sẽ thành lập bộ mới.",
                "situation": "formal"
            },
            {
                "ko": "정부 관계자는 이 문제에 대해 신중히 검토 중이라고 밝혔습니다.",
                "vi": "Quan chức chính phủ cho biết đang xem xét thận trọng vấn đề này.",
                "situation": "formal"
            }
        ],
        "relatedTerms": ["quoc-hoi", "co-quan-nha-nuoc", "luat-hanh-chinh"]
    },
    {
        "slug": "quyen-con-nguoi",
        "korean": "인권",
        "vietnamese": "Quyền con người",
        "hanja": "人權",
        "hanjaReading": "人(사람 인) + 權(권리 권)",
        "pronunciation": "인권 - Quyền con người",
        "meaningKo": "인간으로서 당연히 가지는 기본적 권리. 통역 시 주의: '인권'과 '기본권'을 구분해야 하며, 인권은 보편적 권리(universal rights)를, 기본권은 헌법상 보장된 권리(constitutional rights)를 의미함. 국제인권조약 관련 통역 시 한국은 개인청원권을 인정하는 조약이 많지만 베트남은 일부 제한적이라는 점을 알아야 함. '인권 침해'를 통역할 때 한국은 사법부 구제가 발달했으나 베트남은 행정 절차가 우선이라는 구제 체계 차이를 이해해야 정확한 통역이 가능함.",
        "meaningVi": "Các quyền cơ bản mà con người sinh ra đã có. Quyền con người được bảo vệ bởi luật pháp quốc tế và hiến pháp các nước. Việt Nam và Hàn Quốc đều là thành viên của nhiều công ước quốc tế về nhân quyền, nhưng cách thức thực thi và cơ chế bảo vệ có sự khác biệt cần lưu ý khi phiên dịch.",
        "context": "formal",
        "culturalNote": "한국은 국가인권위원회(독립 기구)가 있으나 베트남은 국회 산하 인권위원회로 운영 방식이 다름. 인권 개념과 범위에 대한 사회적 인식도 차이가 있으며, 한국은 개인의 자유권 중심이 강한 반면 베트남은 집단주의적 접근이 강함. 국제인권조약 가입 현황도 다르고(예: 한국은 개인청원권 인정, 베트남은 일부 유보), 인권 침해 구제 절차와 사법 접근성에서도 차이가 있어 통역 시 이러한 맥락을 고려해야 함.",
        "commonMistakes": [
            {
                "mistake": "'인권'과 '기본권'을 모두 'quyền con người'로 통역",
                "correction": "인권은 'quyền con người', 기본권은 'quyền cơ bản'",
                "explanation": "인권은 보편적 권리, 기본권은 헌법상 권리로 법적 근거와 범위가 다름"
            },
            {
                "mistake": "'인권 침해'를 'vi phạm nhân quyền'으로만 번역하고 구제 방법 설명 생략",
                "correction": "침해 유형과 구제 절차까지 설명 필요",
                "explanation": "양국의 인권 침해 구제 시스템이 다르므로 단순 번역만으로는 불충분함"
            },
            {
                "mistake": "'국가인권위원회'를 'Ủy ban Nhân quyền Quốc gia'로만 번역",
                "correction": "'Ủy ban Nhân quyền Quốc gia Hàn Quốc (cơ quan độc lập)'",
                "explanation": "베트남의 인권위원회는 국회 산하이므로 독립성 차이를 명시해야 함"
            }
        ],
        "examples": [
            {
                "ko": "모든 사람은 인권을 존중받을 권리가 있습니다.",
                "vi": "Mọi người đều có quyền được tôn trọng quyền con người.",
                "situation": "formal"
            },
            {
                "ko": "이 사건은 명백한 인권 침해 사례입니다.",
                "vi": "Vụ việc này là trường hợp vi phạm nhân quyền rõ ràng.",
                "situation": "formal"
            },
            {
                "ko": "국가인권위원회에 진정을 제기할 수 있습니다.",
                "vi": "Có thể nộp đơn khiếu nại lên Ủy ban Nhân quyền Quốc gia.",
                "situation": "formal"
            }
        ],
        "relatedTerms": ["hien-phap", "tu-do-ngon-luan", "quyen-bau-cu"]
    },
    {
        "slug": "tu-do-ngon-luan",
        "korean": "언론의자유",
        "vietnamese": "Tự do ngôn luận",
        "hanja": "言論의自由",
        "hanjaReading": "言(말씀 언) + 論(논할 론) + 自(스스로 자) + 由(말미암을 유)",
        "pronunciation": "언론의자유 - Tự do ngôn luận",
        "meaningKo": "사상이나 의견을 외부에 자유롭게 표현할 수 있는 권리. 통역 시 주의: '언론의 자유'는 표현의 자유(freedom of expression)와 보도의 자유(freedom of press)를 모두 포함하므로 맥락에 따라 구분해야 함. 한국은 헌법 제21조로 보장되며 사전검열 금지가 명시되어 있으나, 베트남은 당과 국가의 이익에 반하지 않는 범위 내에서 보장된다는 제한이 있음을 알아야 정확한 통역이 가능함. '명예훼손'과 '모욕죄' 관련 통역 시 양국의 법적 기준과 처벌 수위가 다르다는 점도 주의해야 함.",
        "meaningVi": "Quyền tự do bày tỏ tư tưởng và ý kiến ra bên ngoài. Tự do ngôn luận được bảo vệ bởi Hiến pháp, bao gồm cả tự do báo chí và tự do biểu đạt. Tuy nhiên, phạm vi và giới hạn của quyền này có sự khác biệt giữa Việt Nam và Hàn Quốc, đặc biệt về kiểm duyệt và trách nhiệm pháp lý.",
        "context": "formal",
        "culturalNote": "한국은 사전검열 절대 금지 원칙이 있으나 베트남은 출판물과 미디어에 대한 사전 심의 제도가 존재함. 한국은 언론사의 독립성이 높고 정부 비판이 자유롭지만, 베트남은 언론이 당과 국가의 지도를 받는다는 헌법 규정이 있음. 인터넷 표현의 자유 범위도 다르며, 명예훼손의 형사처벌 여부(한국: 가능, 베트남: 민사 중심)와 같은 법적 차이도 통역 시 고려해야 할 중요한 문화적 차이임.",
        "commonMistakes": [
            {
                "mistake": "'언론의 자유'를 'tự do báo chí'로만 번역",
                "correction": "'tự do ngôn luận' 또는 맥락에 따라 'tự do báo chí'",
                "explanation": "언론의 자유는 보도의 자유보다 넓은 개념으로 모든 표현의 자유를 포함함"
            },
            {
                "mistake": "'사전검열'을 'kiểm duyệt trước'로만 번역하고 금지 여부 설명 생략",
                "correction": "한국은 절대 금지, 베트남은 일부 허용이라는 차이 명시",
                "explanation": "양국의 사전검열 제도가 근본적으로 다르므로 단순 번역만으로는 오해 발생"
            },
            {
                "mistake": "'명예훼손'을 'phỉ báng'으로만 번역",
                "correction": "민사는 'xâm phạm danh dự', 형사는 'tội phỉ báng'",
                "explanation": "한국은 형사처벌 가능하지만 베트남은 주로 민사 책임이므로 구분 필요"
            }
        ],
        "examples": [
            {
                "ko": "헌법은 언론의 자유를 보장하되 사전검열을 금지합니다.",
                "vi": "Hiến pháp bảo đảm tự do ngôn luận và cấm kiểm duyệt trước.",
                "situation": "formal"
            },
            {
                "ko": "언론의 자유도 타인의 명예를 훼손해서는 안 됩니다.",
                "vi": "Tự do ngôn luận cũng không được xâm phạm danh dự người khác.",
                "situation": "formal"
            },
            {
                "ko": "이 사건은 언론의 자유와 인격권의 충돌 문제입니다.",
                "vi": "Vụ việc này là vấn đề xung đột giữa tự do ngôn luận và quyền nhân cách.",
                "situation": "formal"
            }
        ],
        "relatedTerms": ["quyen-con-nguoi", "hien-phap", "quyen-bau-cu"]
    },
    {
        "slug": "quyen-bau-cu",
        "korean": "선거권",
        "vietnamese": "Quyền bầu cử",
        "hanja": "選擧權",
        "hanjaReading": "選(가릴 선) + 擧(들 거) + 權(권리 권)",
        "pronunciation": "선거권 - Quyền bầu cử",
        "meaningKo": "국민이 선거를 통해 공직자를 선출할 수 있는 권리. 통역 시 주의: '선거권'(투표할 권리)과 '피선거권'(선출될 권리)을 구분해야 하며, 한국은 만 18세부터 선거권, 25세부터 피선거권(대통령은 40세)이지만 베트남은 18세부터 선거권, 21세부터 피선거권(국가주석은 40세)이라는 차이가 있음. '보통선거'를 통역할 때 재산·신분·성별 등에 의한 제한이 없다는 의미를 명확히 해야 하며, 선거 제도(한국: 직접선거, 베트남: 직접선거+간접선거 병행)의 차이도 설명해야 정확한 통역이 가능함.",
        "meaningVi": "Quyền của công dân được bầu chọn người đại diện thông qua bầu cử. Quyền bầu cử bao gồm quyền bầu (quyền bỏ phiếu) và quyền ứng cử (quyền được bầu). Độ tuổi và điều kiện thực hiện quyền này có sự khác biệt giữa Việt Nam và Hàn Quốc cần lưu ý khi phiên dịch.",
        "context": "formal",
        "culturalNote": "한국은 완전한 직접선거제이지만 베트남은 국회의원은 직접선거, 국가주석과 총리는 국회에서 간접선거로 선출함. 선거 연령과 피선거권 연령의 차이도 있으며, 선거 운동 방식과 규제도 상이함(한국: 정당 중심, 베트남: 조국전선 주도). 또한 한국은 비례대표제가 발달했으나 베트남은 지역 대표 중심이라는 점, 선거 관리와 감시 체계의 차이도 통역 시 중요한 문화적 맥락임.",
        "commonMistakes": [
            {
                "mistake": "'선거권'과 '피선거권'을 모두 'quyền bầu cử'로 통역",
                "correction": "선거권은 'quyền bầu cử(투표권)', 피선거권은 'quyền ứng cử'",
                "explanation": "투표할 권리와 선출될 권리는 법적으로 다른 개념이므로 명확히 구분 필요"
            },
            {
                "mistake": "'보통선거'를 'bầu cử phổ thông'으로만 번역하고 의미 설명 생략",
                "correction": "재산·신분·성별 제한이 없다는 점 명시 필요",
                "explanation": "'보통선거' 원칙의 역사적 의미를 이해하지 못하면 단순 번역이 됨"
            },
            {
                "mistake": "'직접선거'와 '간접선거'를 양국 동일하게 적용",
                "correction": "한국은 완전 직접선거, 베트남은 혼합형이라는 차이 설명",
                "explanation": "국가주석, 총리 선출 방식이 다르므로 제도 차이를 명확히 해야 함"
            }
        ],
        "examples": [
            {
                "ko": "만 18세 이상의 국민은 선거권을 가집니다.",
                "vi": "Công dân từ đủ 18 tuổi trở lên có quyền bầu cử.",
                "situation": "formal"
            },
            {
                "ko": "대통령 선거에 출마하려면 피선거권 연령인 만 40세 이상이어야 합니다.",
                "vi": "Để ứng cử Tổng thống cần đủ 40 tuổi trở lên theo quy định về quyền ứng cử.",
                "situation": "formal"
            },
            {
                "ko": "보통선거 원칙에 따라 모든 성인 국민이 투표할 수 있습니다.",
                "vi": "Theo nguyên tắc bầu cử phổ thông, mọi công dân trưởng thành đều có quyền bỏ phiếu.",
                "situation": "formal"
            }
        ],
        "relatedTerms": ["quoc-hoi", "hien-phap", "quyen-con-nguoi"]
    },
    {
        "slug": "luat-hanh-chinh",
        "korean": "행정법",
        "vietnamese": "Luật hành chính",
        "hanja": "行政法",
        "hanjaReading": "行(다닐 행) + 政(정사 정) + 法(법 법)",
        "pronunciation": "행정법 - Luật hành chính",
        "meaningKo": "행정 주체의 조직, 작용 및 구제에 관한 법의 총칭. 통역 시 주의: 행정법은 단일 법전이 아니라 행정조직법, 행정작용법, 행정구제법 등을 포괄하는 개념이므로 맥락에 따라 구체적으로 설명해야 함. '행정처분'을 통역할 때 한국은 항고소송으로 다투지만 베트남은 행정재판소 제도가 다르다는 점을 알아야 함. 또한 '행정심판'과 '행정소송'의 차이(전자는 행정기관 내부, 후자는 법원)를 명확히 구분하지 않으면 법적 절차를 잘못 안내할 수 있음.",
        "meaningVi": "Tổng hợp các quy định pháp luật về tổ chức, hoạt động và cơ chế cứu chế hành chính. Luật hành chính không phải là một bộ luật duy nhất mà bao gồm nhiều luật về tổ chức hành chính, hoạt động hành chính và tố tụng hành chính. Cơ chế khiếu nại, tố cáo và xem xét hành chính có sự khác biệt giữa hai nước cần lưu ý.",
        "context": "formal",
        "culturalNote": "한국은 행정심판법과 행정소송법이 분리되어 있으나 베트남은 행정소송법(Luật Tố tụng hành chính)으로 통합 규정함. 행정처분에 대한 불복 절차도 다르며(한국: 행정심판→행정소송, 베트남: 행정 내부 해결→행정재판), 행정재판소의 역할과 권한에서도 차이가 있음. 또한 행정법의 일반원칙(신뢰보호, 비례원칙 등)에 대한 법리 발달 정도도 다르므로 통역 시 이러한 제도적 차이를 고려해야 함.",
        "commonMistakes": [
            {
                "mistake": "'행정법'을 단일 법률로 착각하고 'Luật hành chính'만 언급",
                "correction": "행정 관련 법률 전체를 의미한다고 설명 필요",
                "explanation": "행정법은 법 분야(legal field)이지 특정 법률명이 아님"
            },
            {
                "mistake": "'행정심판'과 '행정소송'을 모두 'khiếu nại hành chính'으로 통역",
                "correction": "행정심판은 'khiếu nại hành chính', 행정소송은 'tố tụng hành chính'",
                "explanation": "심판은 행정기관 내부, 소송은 법원이라는 결정적 차이가 있음"
            },
            {
                "mistake": "'행정처분'을 'xử lý hành chính'로 번역",
                "correction": "'quyết định hành chính' 또는 'xử phạt hành chính'",
                "explanation": "'xử lý'는 일반적인 처리를 의미하며, 법적 행위로서의 처분은 'quyết định' 사용"
            }
        ],
        "examples": [
            {
                "ko": "행정법은 행정 작용의 적법성을 보장하기 위한 법입니다.",
                "vi": "Luật hành chính là pháp luật nhằm đảm bảo tính hợp pháp của hoạt động hành chính.",
                "situation": "formal"
            },
            {
                "ko": "이 사건은 행정법의 일반원칙인 신뢰보호원칙을 위반했습니다.",
                "vi": "Vụ việc này đã vi phạm nguyên tắc bảo vệ lòng tin - nguyên tắc chung của luật hành chính.",
                "situation": "formal"
            },
            {
                "ko": "행정법 강의에서는 행정조직법과 행정작용법을 다룹니다.",
                "vi": "Trong bài giảng luật hành chính sẽ đề cập đến luật tổ chức hành chính và luật hoạt động hành chính.",
                "situation": "formal"
            }
        ],
        "relatedTerms": ["xu-phat-hanh-chinh", "khieu-nai-hanh-chinh", "chinh-phu"]
    },
    {
        "slug": "xu-phat-hanh-chinh",
        "korean": "행정처분",
        "vietnamese": "Xử phạt hành chính",
        "hanja": "行政處分",
        "hanjaReading": "行(다닐 행) + 政(정사 정) + 處(곳 처) + 分(나눌 분)",
        "pronunciation": "행정처분 - Xử phạt hành chính",
        "meaningKo": "행정청이 공권력을 행사하여 국민의 권리·의무에 직접 영향을 미치는 행위. 통역 시 주의: '행정처분'은 넓은 의미로는 모든 행정 행위를, 좁은 의미로는 제재적 처분(영업정지, 과태료 등)을 의미하므로 맥락 파악이 중요함. 한국에서는 '처분'이 중립적 용어이지만 베트남어 'xử phạt'은 처벌의 뉘앙스가 강하므로, 허가나 인가 같은 수익적 처분은 'quyết định hành chính'으로 번역해야 함. 처분에 대한 불복 절차(행정심판, 행정소송)를 설명할 때 양국의 제도 차이를 명확히 해야 정확한 통역이 가능함.",
        "meaningVi": "Hành vi của cơ quan hành chính nhà nước thực hiện quyền công quyền, tác động trực tiếp đến quyền và nghĩa vụ của người dân. Ở nghĩa hẹp, xử phạt hành chính là biện pháp chế tài (đình chỉ kinh doanh, phạt tiền...). Quyết định hành chính có thể là cấp phép (có lợi) hoặc xử phạt (bất lợi), cần phân biệt rõ khi phiên dịch.",
        "context": "formal",
        "culturalNote": "한국은 행정처분의 종류를 수익적 처분(허가, 인가)과 침익적 처분(제재, 거부)으로 구분하는 법리가 발달했으나, 베트남은 'xử phạt hành chính'이 주로 제재적 의미로 쓰임. 처분에 대한 불복 수단도 다르며(한국: 행정심판 선택적 전치주의, 베트남: 행정 내부 해결 우선), 처분의 취소와 무효 개념, 처분의 효력 정지 제도 등에서도 차이가 있어 통역 시 주의가 필요함.",
        "commonMistakes": [
            {
                "mistake": "모든 '행정처분'을 'xử phạt hành chính'으로 번역",
                "correction": "제재는 'xử phạt', 일반 처분은 'quyết định hành chính'",
                "explanation": "'xử phạt'은 처벌의 의미가 강하므로 허가·인가 등에는 부적절함"
            },
            {
                "mistake": "'처분 취소'와 '처분 무효'를 동일하게 번역",
                "correction": "취소는 'hủy bỏ', 무효는 'vô hiệu'로 구분",
                "explanation": "취소는 소급효 없음, 무효는 처음부터 효력 없음이라는 법적 차이가 있음"
            },
            {
                "mistake": "'행정처분 불복'을 'không chấp nhận'으로 번역",
                "correction": "'khiếu nại quyết định hành chính' 또는 'khởi kiện hành chính'",
                "explanation": "법적 절차로서의 불복은 정식 용어 사용이 필요함"
            }
        ],
        "examples": [
            {
                "ko": "영업정지 행정처분에 불복하여 행정심판을 청구했습니다.",
                "vi": "Đã nộp đơn khiếu nại hành chính vì không chấp nhận quyết định đình chỉ kinh doanh.",
                "situation": "formal"
            },
            {
                "ko": "이 행정처분은 위법하여 취소되어야 합니다.",
                "vi": "Quyết định hành chính này vi phạm pháp luật và cần được hủy bỏ.",
                "situation": "formal"
            },
            {
                "ko": "건축 허가는 수익적 행정처분에 해당합니다.",
                "vi": "Giấy phép xây dựng là quyết định hành chính có lợi.",
                "situation": "formal"
            }
        ],
        "relatedTerms": ["luat-hanh-chinh", "khieu-nai-hanh-chinh", "co-quan-nha-nuoc"]
    },
    {
        "slug": "khieu-nai-hanh-chinh",
        "korean": "행정심판",
        "vietnamese": "Khiếu nại hành chính",
        "hanja": "行政審判",
        "hanjaReading": "行(다닐 행) + 政(정사 정) + 審(살필 심) + 判(판단할 판)",
        "pronunciation": "행정심판 - Khiếu nại hành chính",
        "meaningKo": "행정청의 위법·부당한 처분이나 부작위에 대해 행정기관에 불복하여 구제를 청구하는 절차. 통역 시 주의: '행정심판'은 법원이 아닌 행정심판위원회에서 진행되는 행정 내부 절차이므로 '행정소송'(법원 절차)과 명확히 구분해야 함. 한국은 행정심판을 거치지 않고 바로 행정소송을 제기할 수 있는 선택적 전치주의이지만, 베트남은 원칙적으로 행정 내부 해결을 먼저 시도해야 한다는 차이가 있음. '재결'(행정심판 결정)과 '판결'(법원 결정)의 차이도 정확히 전달해야 오해를 방지할 수 있음.",
        "meaningVi": "Thủ tục yêu cầu cứu chế trước cơ quan hành chính khi có quyết định hoặc hành vi hành chính trái pháp luật hoặc không đúng. Ở Hàn Quốc, khiếu nại hành chính được thực hiện bởi Ủy ban Khiếu nại Hành chính (không phải tòa án), khác với tố tụng hành chính (tại tòa án). Việt Nam ưu tiên giải quyết khiếu nại trong nội bộ hành chính trước khi đưa ra tòa.",
        "context": "formal",
        "culturalNote": "한국은 행정심판위원회가 독립적 준사법기관으로 운영되며 행정심판법에 따라 체계화되어 있으나, 베트남은 상급 행정기관이 하급 기관의 결정을 재검토하는 방식이 주를 이룸. 한국은 행정심판을 거치지 않고도 행정소송 제기가 가능하지만(선택적 전치주의), 베트남은 일부 사안에서 행정 절차를 먼저 거쳐야 함. 또한 행정심판의 구속력과 효력, 재결의 기속력 등에서도 양국 간 차이가 있어 통역 시 주의가 필요함.",
        "commonMistakes": [
            {
                "mistake": "'행정심판'과 '행정소송'을 구분하지 않고 모두 'tố tụng hành chính'으로 번역",
                "correction": "행정심판은 'khiếu nại hành chính', 행정소송은 'tố tụng hành chính'",
                "explanation": "심판은 행정기관 내부, 소송은 법원이라는 결정적 차이를 반드시 구분해야 함"
            },
            {
                "mistake": "'재결'을 '판결(bản án)'로 번역",
                "correction": "'quyết định giải quyết khiếu nại' 또는 'quyết định tái thẩm'",
                "explanation": "재결은 행정기관의 결정이고 판결은 법원의 결정이므로 다름"
            },
            {
                "mistake": "'행정심판 전치주의'를 설명 없이 번역",
                "correction": "한국은 선택적, 베트남은 필수적이라는 차이 명시",
                "explanation": "소송 제기 전 행정심판 필수 여부가 다르므로 절차 안내 시 중요함"
            }
        ],
        "examples": [
            {
                "ko": "행정처분에 불복이 있으면 행정심판을 청구할 수 있습니다.",
                "vi": "Nếu không đồng ý với quyết định hành chính, có thể nộp đơn khiếu nại hành chính.",
                "situation": "formal"
            },
            {
                "ko": "행정심판위원회는 청구를 인용하는 재결을 내렸습니다.",
                "vi": "Ủy ban Khiếu nại Hành chính đã ra quyết định chấp nhận đơn khiếu nại.",
                "situation": "formal"
            },
            {
                "ko": "행정심판을 거치지 않고 바로 행정소송을 제기할 수도 있습니다.",
                "vi": "Có thể khởi kiện hành chính trực tiếp mà không cần qua thủ tục khiếu nại hành chính.",
                "situation": "formal"
            }
        ],
        "relatedTerms": ["xu-phat-hanh-chinh", "luat-hanh-chinh", "co-quan-nha-nuoc"]
    },
    {
        "slug": "co-quan-nha-nuoc",
        "korean": "국가기관",
        "vietnamese": "Cơ quan nhà nước",
        "hanja": "國家機關",
        "hanjaReading": "國(나라 국) + 家(집 가) + 機(틀 기) + 關(관계할 관)",
        "pronunciation": "국가기관 - Cơ quan nhà nước",
        "meaningKo": "국가의 의사를 결정하고 실현하는 권한을 가진 조직. 통역 시 주의: '국가기관'은 입법·행정·사법부를 모두 포함하는 넓은 개념이므로 맥락에 따라 구체적으로 어느 기관인지 명시해야 함. 한국의 삼권분립 구조와 베트남의 권력 구조가 다르므로(베트남은 국회가 최고 권력기관), '국가기관 간 견제와 균형'을 통역할 때 양국의 헌법적 차이를 이해해야 함. 또한 '공공기관'과 '국가기관'의 차이(전자는 공기업 포함, 후자는 권력 행사 기관만)도 정확히 구분해야 정확한 통역이 가능함.",
        "meaningVi": "Tổ chức có thẩm quyền quyết định và thực hiện ý chí của nhà nước. Cơ quan nhà nước bao gồm cơ quan lập pháp, hành pháp và tư pháp. Cấu trúc quyền lực nhà nước ở Việt Nam khác với Hàn Quốc: Việt Nam lấy Quốc hội làm cơ quan quyền lực cao nhất, trong khi Hàn Quốc theo nguyên tắc tam quyền phân lập.",
        "context": "formal",
        "culturalNote": "한국은 입법·행정·사법의 삼권분립이 명확하지만, 베트남은 국회가 최고 권력기관으로서 국가주석, 정부, 법원을 선출하고 감독하는 구조임. 국가기관의 독립성과 상호 견제 방식에서 큰 차이가 있으며, 한국은 헌법재판소와 같은 독립 기관이 있으나 베트남은 국회 산하 기구가 많음. 또한 '공공기관'(기업 포함)과 '국가기관'(권력 행사 조직)의 구분, 중앙정부와 지방자치단체의 관계 등에서도 양국 간 차이가 있어 통역 시 맥락 설명이 필요함.",
        "commonMistakes": [
            {
                "mistake": "'국가기관'과 '공공기관'을 모두 'cơ quan nhà nước'로 번역",
                "correction": "국가기관은 'cơ quan nhà nước', 공공기관은 'cơ quan công cộng'",
                "explanation": "공공기관은 공기업 등을 포함하는 넓은 개념이므로 구분 필요"
            },
            {
                "mistake": "'삼권분립'을 'phân chia ba quyền'으로만 번역하고 양국 차이 설명 생략",
                "correction": "한국은 완전한 삼권분립, 베트남은 국회 중심 구조라는 차이 명시",
                "explanation": "권력 구조의 근본적 차이를 설명하지 않으면 오해 발생"
            },
            {
                "mistake": "'중앙행정기관'과 '지방자치단체'의 관계를 양국 동일하게 설명",
                "correction": "한국은 지방자치, 베트남은 중앙집권적 구조라는 차이 필요",
                "explanation": "지방 정부의 독립성과 권한 범위가 크게 다름"
            }
        ],
        "examples": [
            {
                "ko": "국가기관은 법률에 따라 그 권한을 행사해야 합니다.",
                "vi": "Cơ quan nhà nước phải thực hiện thẩm quyền theo quy định của pháp luật.",
                "situation": "formal"
            },
            {
                "ko": "삼권분립 원칙에 따라 국가기관은 서로 견제합니다.",
                "vi": "Theo nguyên tắc tam quyền phân lập, các cơ quan nhà nước kiềm chế lẫn nhau.",
                "situation": "formal"
            },
            {
                "ko": "이 사안은 여러 국가기관이 협력하여 처리해야 합니다.",
                "vi": "Vấn đề này cần nhiều cơ quan nhà nước phối hợp xử lý.",
                "situation": "formal"
            }
        ],
        "relatedTerms": ["quoc-hoi", "chinh-phu", "hien-phap"]
    }
]

# 중복 필터링
new_terms_filtered = [t for t in new_terms if t['slug'] not in existing_slugs]

# 데이터 추가
data.extend(new_terms_filtered)

# 저장
with open(file_path, 'w', encoding='utf-8') as f:
    json.dump(data, f, ensure_ascii=False, indent=2)

print(f"✅ {len(new_terms_filtered)}개 헌법/행정법 용어 추가 완료")
print(f"📊 총 {len(data)}개 법률 용어")
print("\n추가된 용어:")
for term in new_terms_filtered:
    print(f"  - {term['slug']}: {term['korean']} ({term['vietnamese']})")
