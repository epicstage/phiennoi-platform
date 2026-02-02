#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
출입국/비자/체류 법률용어 추가 스크립트 (Immigration/Visa/Residency)
Tier S 품질 기준 준수 (90점 이상)
"""

import json
import os

# 파일 경로 설정
file_path = os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', 'data', 'terms', 'legal.json')

# 기존 데이터 로드
with open(file_path, 'r', encoding='utf-8') as f:
    data = json.load(f)  # data is a LIST

# 기존 slug 중복 체크
existing_slugs = {t['slug'] for t in data}

# 새 용어 데이터
new_terms = [
    {
        "slug": "thi-thuc",
        "korean": "비자",
        "vietnamese": "thị thực",
        "hanja": "査證",
        "hanjaReading": "査(조사할 사) + 證(증거 증)",
        "pronunciation": "티 툭",
        "meaningKo": "외국인이 특정 국가에 입국하거나 체류하기 위해 발급받는 공식 허가 문서입니다. 통역 시 비자 종류(관광, 취업, 학생 등)를 명확히 구분해야 하며, 베트남에서는 'visa' 외래어와 'thị thực' 한자어를 혼용하므로 맥락에 따라 적절히 선택해야 합니다. 한국의 D-2(유학), E-9(비전문취업) 등 알파벳 코드는 베트남에도 설명이 필요하며, 베트남의 DT(관광), DN(비즈니스) 코드도 마찬가지입니다.",
        "meaningVi": "Giấy tờ cho phép chính thức để người nước ngoài nhập cảnh hoặc lưu trú tại một quốc gia cụ thể. Cần phân biệt các loại thị thực như du lịch (DL), công tác (DN), lao động (LD). Thị thực Hàn Quốc có mã chữ cái như D-2 (du học), E-9 (lao động phổ thông).",
        "context": "출입국관리법, 대사관 업무, 외국인 고용 절차에서 사용",
        "culturalNote": "한국은 전자비자(K-ETA) 시스템을 운영하며 무비자 입국 가능 국가가 많은 반면, 베트남은 대부분의 국가에 비자를 요구합니다. 한국의 비자 연장은 출입국관리사무소에서, 베트남은 공안부 출입국관리국에서 처리하는 차이가 있습니다. 통역 시 양국의 비자 정책 차이를 설명할 준비가 필요합니다.",
        "commonMistakes": [
            {
                "mistake": "visa를 '비자' 대신 '사증'으로 통역",
                "correction": "'비자' 사용",
                "explanation": "법률 문서에는 '사증'이 정식 용어지만 실무에서는 '비자'가 압도적으로 많이 쓰임"
            },
            {
                "mistake": "thị thực을 '티 쑤억'으로 발음",
                "correction": "'티 툭'으로 발음",
                "explanation": "남부 베트남 발음에서 thực은 '툭'에 가까움"
            },
            {
                "mistake": "모든 비자를 giấy phép으로 통역",
                "correction": "비자는 thị thực, 허가증은 giấy phép으로 구분",
                "explanation": "비자와 각종 허가증은 법적으로 다른 문서임"
            }
        ],
        "examples": [
            {
                "ko": "관광비자로는 90일 이상 체류할 수 없습니다.",
                "vi": "Với thị thực du lịch không thể lưu trú quá 90 ngày.",
                "situation": "formal"
            },
            {
                "ko": "비자 연장 신청은 만료 10일 전까지 해야 합니다.",
                "vi": "Phải nộp đơn gia hạn thị thực trước 10 ngày trước khi hết hạn.",
                "situation": "formal"
            },
            {
                "ko": "무비자로 입국해서 한 달 있다가 나갈 거예요.",
                "vi": "Tôi sẽ nhập cảnh miễn thị thực, ở một tháng rồi xuất cảnh.",
                "situation": "informal"
            }
        ],
        "relatedTerms": ["giay-phep-lao-dong", "the-tam-tru", "gia-han-visa", "nhap-canh"]
    },
    {
        "slug": "ho-chieu",
        "korean": "여권",
        "vietnamese": "hộ chiếu",
        "hanja": "護照",
        "hanjaReading": "護(지킬 호) + 照(비출 조)",
        "pronunciation": "호 찌에우",
        "meaningKo": "국적 보유자가 해외 여행 시 신분과 국적을 증명하는 공식 문서입니다. 통역 시 여권 종류(일반, 관용, 외교)와 유효기간을 명확히 전달해야 하며, 베트남어에서는 한자어 'hộ chiếu'와 외래어 'passport'를 혼용하지만 공식 문서에서는 'hộ chiếu'를 사용합니다. 여권 분실, 재발급, 만료 등의 상황에서 긴급 여행증명서(emergency travel document)와 구분이 필요합니다.",
        "meaningVi": "Giấy tờ chính thức chứng minh danh tính và quốc tịch của công dân khi đi nước ngoài. Có các loại hộ chiếu phổ thông, công vụ, ngoại giao. Cần chú ý thời hạn còn hiệu lực (thường yêu cầu còn ít nhất 6 tháng khi xin thị thực).",
        "context": "출입국 심사, 신분 확인, 비자 신청 절차에서 사용",
        "culturalNote": "한국 여권은 세계에서 가장 강력한 여권 중 하나로 190개국 이상 무비자 입국이 가능하지만, 베트남 여권은 약 80개국 정도입니다. 한국은 10년 유효 여권을 발급하지만 베트남은 일반적으로 10년이나 최근 5년짜리도 발급합니다. 여권 색상도 한국은 녹색, 베트남은 진녹색으로 약간 다릅니다.",
        "commonMistakes": [
            {
                "mistake": "passport를 '패스포트'로 음역",
                "correction": "'여권' 또는 'hộ chiếu' 사용",
                "explanation": "공식 통역에서는 외래어 음역보다 고유어 사용이 원칙"
            },
            {
                "mistake": "hộ chiếu을 '호치에우'로 발음",
                "correction": "'호 찌에우'로 발음",
                "explanation": "chiếu의 ch는 북부에서 'ㅊ', 남부에서 'ㅉ' 발음"
            },
            {
                "mistake": "여권 만료를 'hết hạn hộ chiếu'로만 표현",
                "correction": "'hộ chiếu hết hiệu lực' 또는 'hộ chiếu quá hạn'도 사용",
                "explanation": "문맥에 따라 다양한 표현 가능"
            }
        ],
        "examples": [
            {
                "ko": "여권 유효기간이 6개월 이상 남아있어야 비자 신청이 가능합니다.",
                "vi": "Hộ chiếu phải còn hiệu lực ít nhất 6 tháng mới có thể xin thị thực.",
                "situation": "formal"
            },
            {
                "ko": "여권을 분실하셨으면 즉시 대사관에 신고하세요.",
                "vi": "Nếu bị mất hộ chiếu, hãy báo ngay cho đại sứ quán.",
                "situation": "formal"
            },
            {
                "ko": "여권 가져오셨어요?",
                "vi": "Anh mang hộ chiếu chưa?",
                "situation": "informal"
            }
        ],
        "relatedTerms": ["thi-thuc", "nhap-canh", "xuat-canh", "the-tam-tru"]
    },
    {
        "slug": "giay-phep-lao-dong",
        "korean": "노동허가증",
        "vietnamese": "giấy phép lao động",
        "hanja": "勞動許可證",
        "hanjaReading": "勞(일할 로) + 動(움직일 동) + 許(허락할 허) + 可(옳을 가) + 證(증거 증)",
        "pronunciation": "자이 펩 라오 동",
        "meaningKo": "외국인이 특정 국가에서 합법적으로 취업 활동을 하기 위해 발급받는 허가 문서입니다. 통역 시 취업비자(work visa)와 노동허가증의 차이를 명확히 해야 하며, 한국에서는 일부 비자 유형(E-7, E-9 등)에서 통합 관리되지만 베트남은 별도 발급입니다. 고용주의 초청장, 학력/경력 증명, 건강검진 등 구비서류가 많으므로 서류 명칭을 정확히 통역해야 합니다.",
        "meaningVi": "Giấy phép cho phép người nước ngoài làm việc hợp pháp tại một quốc gia. Ở Hàn Quốc, một số loại visa (E-7, E-9) đã tích hợp chức năng này nhưng ở Việt Nam phải xin riêng. Cần có thư mời từ nhà tuyển dụng, bằng cấp, kinh nghiệm và giấy khám sức khỏe.",
        "context": "외국인 고용 절차, 노동부 업무, 취업비자 신청에서 사용",
        "culturalNote": "한국은 외국인 근로자를 위한 고용허가제(EPS)가 체계적으로 운영되며 E-9 비자가 대표적입니다. 베트남은 최근 외국인 고용이 증가하며 노동허가증 발급 절차가 간소화되었지만 여전히 복잡합니다. 한국은 체류자격과 노동허가가 통합된 반면 베트남은 분리되어 있어 통역 시 혼동 주의가 필요합니다.",
        "commonMistakes": [
            {
                "mistake": "노동허가증과 취업비자를 같은 것으로 설명",
                "correction": "비자는 입국/체류 허가, 노동허가증은 취업 활동 허가로 구분",
                "explanation": "법적으로 다른 개념이며 국가마다 통합 여부가 다름"
            },
            {
                "mistake": "giấy phép을 '자이 펩'으로만 발음",
                "correction": "'자이 펩' (남부) 또는 '자이 펩' (북부, phép의 p는 약하게)",
                "explanation": "지역별 발음 차이 인지 필요"
            },
            {
                "mistake": "모든 외국인 근로자를 '이주노동자'로 통역",
                "correction": "맥락에 따라 '외국인 근로자', '이주노동자', '외국인 인력' 구분",
                "explanation": "법률 용어와 일반 용어의 뉘앙스 차이"
            }
        ],
        "examples": [
            {
                "ko": "노동허가증 없이 취업하면 불법체류로 간주됩니다.",
                "vi": "Nếu làm việc không có giấy phép lao động sẽ bị coi là lưu trú bất hợp pháp.",
                "situation": "formal"
            },
            {
                "ko": "노동허가증 발급까지 약 4주 소요됩니다.",
                "vi": "Thời gian cấp giấy phép lao động mất khoảng 4 tuần.",
                "situation": "formal"
            },
            {
                "ko": "허가증 나왔어요? 이제 일 시작할 수 있어요?",
                "vi": "Giấy phép ra chưa? Bây giờ có thể bắt đầu làm việc không?",
                "situation": "informal"
            }
        ],
        "relatedTerms": ["thi-thuc", "the-tam-tru", "gia-han-visa", "tam-tru"]
    },
    {
        "slug": "the-tam-tru",
        "korean": "체류카드",
        "vietnamese": "thẻ tạm trú",
        "hanja": "滯留카드",
        "hanjaReading": "滯(머무를 체) + 留(머무를 류) + card(외래어)",
        "pronunciation": "테 땀 쭈",
        "meaningKo": "외국인이 장기 체류 시 발급받는 신분증 형태의 체류 증명 카드입니다. 통역 시 한국의 외국인등록증(Alien Registration Card)과 베트남의 임시거주카드(thẻ tạm trú)는 유사하지만 발급 조건과 절차가 다름을 인지해야 합니다. 한국은 90일 이상 체류 시 발급하며 지문 등록이 필요하고, 베트남도 유사한 절차를 거칩니다. 분실 시 재발급 절차와 벌금을 명확히 전달해야 합니다.",
        "meaningVi": "Thẻ chứng minh danh tính dạng thẻ cho người nước ngoài lưu trú dài hạn. Ở Hàn Quốc gọi là 외국인등록증 (thẻ đăng ký người nước ngoài), cấp khi lưu trú trên 90 ngày, cần đăng ký vân tay. Thẻ này có chức năng như thẻ căn cước, dùng được trong nhiều giao dịch.",
        "context": "출입국관리, 신분 확인, 은행 업무, 계약 체결 시 사용",
        "culturalNote": "한국의 외국인등록증은 주민등록번호와 유사한 외국인등록번호를 부여하며 IC칩이 내장되어 있어 많은 공공/민간 서비스에서 본인 인증이 가능합니다. 베트남의 thẻ tạm trú도 점차 전자화되고 있지만 아직 수기 정보가 많습니다. 한국은 체류카드를 항상 휴대해야 하며 미휴대 시 과태료가 부과되는데, 베트남도 유사한 규정이 있습니다.",
        "commonMistakes": [
            {
                "mistake": "외국인등록증을 '외국인증명서'로 통역",
                "correction": "'외국인등록증' 정확히 사용",
                "explanation": "법정 명칭이므로 정확한 용어 사용 필수"
            },
            {
                "mistake": "thẻ tạm trú을 '테 땀뜨루'로 발음",
                "correction": "'테 땀 쭈'로 발음 (trú는 짧게)",
                "explanation": "trú의 t는 성조와 함께 짧고 강하게 발음"
            },
            {
                "mistake": "체류카드와 거소증을 혼동",
                "correction": "체류카드는 외국인용, 거소증은 재외국민용으로 구분",
                "explanation": "대상과 법적 근거가 다른 문서"
            }
        ],
        "examples": [
            {
                "ko": "입국 후 90일 이내에 체류카드를 발급받아야 합니다.",
                "vi": "Phải làm thẻ tạm trú trong vòng 90 ngày sau khi nhập cảnh.",
                "situation": "formal"
            },
            {
                "ko": "체류카드를 항상 휴대하시고, 요청 시 제시하셔야 합니다.",
                "vi": "Luôn mang thẻ tạm trú bên mình và xuất trình khi được yêu cầu.",
                "situation": "formal"
            },
            {
                "ko": "등록증 집에 두고 나왔는데 괜찮을까요?",
                "vi": "Tôi để thẻ ở nhà, có sao không?",
                "situation": "informal"
            }
        ],
        "relatedTerms": ["thi-thuc", "tam-tru", "giay-phep-lao-dong", "nhap-canh"]
    },
    {
        "slug": "gia-han-visa",
        "korean": "비자연장",
        "vietnamese": "gia hạn visa",
        "hanja": "査證延長",
        "hanjaReading": "査(조사할 사) + 證(증거 증) + 延(늘일 연) + 長(길 장)",
        "pronunciation": "자 한 비자",
        "meaningKo": "기존 비자의 유효기간을 늘리는 행정 절차입니다. 통역 시 연장(extension)과 갱신(renewal)의 차이, 신청 기한(보통 만료 전 10~30일), 필요 서류(재직증명서, 재학증명서 등)를 정확히 전달해야 합니다. 한국은 출입국관리사무소에서, 베트Nam은 공안부 출입국관리국에서 처리하며, 온라인 신청 가능 여부도 국가마다 다릅니다. 연장 불가 시 출국 후 재입국 절차도 설명할 수 있어야 합니다.",
        "meaningVi": "Thủ tục hành chính kéo dài thời hạn hiệu lực của visa hiện tại. Cần phân biệt gia hạn (kéo dài visa cũ) và làm mới (visa mới). Thông thường phải nộp đơn trước 10-30 ngày trước khi hết hạn, cần giấy xác nhận công việc hoặc học tập. Ở Hàn Quốc xử lý tại văn phòng quản lý xuất nhập cảnh.",
        "context": "출입국관리, 비자 행정, 장기 체류 계획 시 사용",
        "culturalNote": "한국은 Hi Korea 시스템을 통해 온라인으로 비자 연장 신청이 가능하며, 일부 체류자격은 자동 갱신되기도 합니다. 베트남은 최근 온라인 시스템이 도입되었지만 여전히 방문 신청이 일반적입니다. 연장 수수료도 한국은 비자 종류에 따라 6만~12만원, 베트남은 약 50만~200만동으로 차이가 있습니다. 불법체류 위험을 강조하여 기한 내 신청을 독려하는 것이 중요합니다.",
        "commonMistakes": [
            {
                "mistake": "연장과 갱신을 같은 의미로 사용",
                "correction": "연장은 기존 비자 기간 늘림, 갱신은 새 비자 발급",
                "explanation": "법적으로 다른 절차이며 수수료도 다름"
            },
            {
                "mistake": "gia hạn을 '지아한'으로 발음",
                "correction": "'자 한'으로 발음",
                "explanation": "gia는 북부에서 '자', 남부에서 '야'로 발음"
            },
            {
                "mistake": "만료 당일에도 연장 신청 가능하다고 통역",
                "correction": "국가마다 다르지만 보통 만료 전 신청 필수라고 강조",
                "explanation": "만료 후 신청은 불법체류로 간주될 수 있음"
            }
        ],
        "examples": [
            {
                "ko": "비자 만료 2주 전까지 연장 신청을 완료해 주시기 바랍니다.",
                "vi": "Vui lòng hoàn tất đơn gia hạn visa trước 2 tuần trước khi hết hạn.",
                "situation": "formal"
            },
            {
                "ko": "연장이 불가능한 경우 출국 후 재입국해야 합니다.",
                "vi": "Nếu không thể gia hạn, phải xuất cảnh rồi nhập cảnh lại.",
                "situation": "formal"
            },
            {
                "ko": "비자 연장 얼마나 걸려요?",
                "vi": "Gia hạn visa mất bao lâu?",
                "situation": "informal"
            }
        ],
        "relatedTerms": ["thi-thuc", "the-tam-tru", "tam-tru", "xuat-canh"]
    },
    {
        "slug": "truc-xuat",
        "korean": "추방",
        "vietnamese": "trục xuất",
        "hanja": "逐出",
        "hanjaReading": "逐(쫓을 축) + 出(날 출)",
        "pronunciation": "쭉 쑤엇",
        "meaningKo": "외국인이 법령 위반으로 강제로 출국 조치되는 것을 의미합니다. 통역 시 추방(deportation)과 출국명령(departure order)의 차이를 명확히 해야 하며, 추방 사유(불법체류, 범죄 등), 재입국 금지 기간, 이의신청 절차 등을 정확히 전달해야 합니다. 매우 민감한 사안이므로 감정적 표현을 배제하고 법적 절차를 중립적으로 통역해야 합니다. 강제퇴거와 혼용되기도 하지만 법적으로는 다른 용어입니다.",
        "meaningVi": "Người nước ngoài bị buộc phải rời khỏi đất nước do vi phạm pháp luật. Cần phân biệt trục xuất (deportation - cưỡng chế) và lệnh xuất cảnh (departure order - tự nguyện trong thời hạn). Lý do trục xuất: lưu trú bất hợp pháp, phạm tội, vi phạm điều kiện visa. Có thể bị cấm tái nhập cảnh từ 1-10 năm.",
        "context": "출입국관리법 위반, 형사 절차, 법원 판결에서 사용",
        "culturalNote": "한국은 출입국관리법에 따라 강제퇴거 절차가 엄격하게 규정되어 있으며, 보호소(detention center) 수용 후 추방이 진행됩니다. 베트남도 유사한 절차가 있으며, 양국 모두 추방 전 이의신청 기회를 제공합니다. 한국은 최근 불법체류자 자진 신고 시 출국명령으로 전환하는 정책을 운영하기도 합니다. 통역 시 추방과 자진출국의 차이를 명확히 하여 당사자가 선택할 수 있도록 해야 합니다.",
        "commonMistakes": [
            {
                "mistake": "추방과 강제퇴거를 완전히 같은 의미로 통역",
                "correction": "법률 문서에서는 '강제퇴거'가 정식 용어, 일반 대화에서는 '추방'도 사용",
                "explanation": "법정 용어와 일상 용어의 구분 필요"
            },
            {
                "mistake": "trục xuất을 '뜨룩 쑤앗'으로 발음",
                "correction": "'쭉 쑤엇'으로 발음",
                "explanation": "tr은 'ㅉ' 또는 'ㅊ'에 가까운 소리"
            },
            {
                "mistake": "추방되면 영원히 재입국 불가라고 통역",
                "correction": "재입국 금지 기간은 사안에 따라 1~10년 또는 영구적",
                "explanation": "케이스별로 다르므로 일괄적으로 말하면 안 됨"
            }
        ],
        "examples": [
            {
                "ko": "불법체류 적발 시 추방 및 5년간 재입국 금지 조치될 수 있습니다.",
                "vi": "Nếu bị phát hiện lưu trú bất hợp pháp có thể bị trục xuất và cấm tái nhập cảnh 5 năm.",
                "situation": "formal"
            },
            {
                "ko": "추방 결정에 불복할 경우 30일 이내 이의신청 가능합니다.",
                "vi": "Nếu không đồng ý với quyết định trục xuất, có thể kháng cáo trong vòng 30 ngày.",
                "situation": "formal"
            },
            {
                "ko": "불법체류하다 걸리면 쫓겨날 수도 있어요.",
                "vi": "Nếu lưu trú bất hợp pháp bị bắt có thể bị trục xuất đấy.",
                "situation": "informal"
            }
        ],
        "relatedTerms": ["thi-thuc", "tam-tru", "xuat-canh", "nhap-canh"]
    },
    {
        "slug": "nhap-canh",
        "korean": "입국",
        "vietnamese": "nhập cảnh",
        "hanja": "入國",
        "hanjaReading": "入(들 입) + 國(나라 국)",
        "pronunciation": "녑 까인",
        "meaningKo": "외국인이나 자국민이 국경을 넘어 한 국가의 영토에 들어오는 행위를 의미합니다. 통역 시 입국 절차(입국심사, 세관검사), 입국 거부(denial of entry) 사유, 입국 금지 조치 등을 명확히 전달해야 하며, 공항/항만/육로 입국의 차이도 설명할 수 있어야 합니다. 한국은 자동출입국심사(Smart Entry Service)가 발달했고, 베트남도 e-Gate를 도입 중입니다. 입국 시 제출하는 입국카드(arrival card) 작성법도 통역 범위에 포함됩니다.",
        "meaningVi": "Hành động một người nước ngoài hoặc công dân vượt biên giới vào lãnh thổ một quốc gia. Quy trình bao gồm kiểm tra xuất nhập cảnh, kiểm tra hải quan. Có thể bị từ chối nhập cảnh nếu không đủ điều kiện (visa không hợp lệ, mục đích không rõ ràng, v.v.). Hàn Quốc có hệ thống tự động (Smart Entry Service).",
        "context": "공항 입국심사, 출입국관리법, 여행 안내에서 사용",
        "culturalNote": "한국은 인천공항을 비롯한 주요 공항에서 입국 절차가 자동화되어 있으며, K-ETA(전자여행허가) 사전 신청 시 더 빠른 입국이 가능합니다. 베트남은 아직 수기 절차가 많지만 점차 전자화되고 있습니다. 양국 모두 입국 시 생체정보(지문, 얼굴) 수집이 일반화되었으며, 이에 대한 설명도 통역에 포함될 수 있습니다. 입국 금지 사유는 양국이 유사하지만 세부 기준이 다를 수 있습니다.",
        "commonMistakes": [
            {
                "mistake": "입국을 'entry' 대신 'come in'으로 통역",
                "correction": "'입국'은 'entry', 'nhập cảnh'으로 공식 용어 사용",
                "explanation": "법률/행정 용어는 정확한 대응어 사용 필수"
            },
            {
                "mistake": "nhập cảnh을 '냅까인'으로 발음",
                "correction": "'녑 까인'으로 발음 (nhập의 nh는 'ㄴ' 소리)",
                "explanation": "성조와 자음 정확히 발음해야 의미 전달"
            },
            {
                "mistake": "입국심사와 세관검사를 같은 절차로 설명",
                "correction": "입국심사는 출입국관리, 세관검사는 관세청 소관으로 구분",
                "explanation": "담당 기관과 목적이 다른 별도 절차"
            }
        ],
        "examples": [
            {
                "ko": "입국 시 여권과 비자를 입국심사대에 제시하십시오.",
                "vi": "Khi nhập cảnh, vui lòng xuất trình hộ chiếu và thị thực tại quầy kiểm tra.",
                "situation": "formal"
            },
            {
                "ko": "입국 목적이 불분명하면 입국이 거부될 수 있습니다.",
                "vi": "Nếu mục đích nhập cảnh không rõ ràng có thể bị từ chối nhập cảnh.",
                "situation": "formal"
            },
            {
                "ko": "한국 들어올 때 짐 검사 안 받았어요.",
                "vi": "Lúc nhập cảnh Hàn Quốc tôi không bị kiểm tra hành lý.",
                "situation": "informal"
            }
        ],
        "relatedTerms": ["xuat-canh", "thi-thuc", "ho-chieu", "the-tam-tru"]
    },
    {
        "slug": "xuat-canh",
        "korean": "출국",
        "vietnamese": "xuất cảnh",
        "hanja": "出國",
        "hanjaReading": "出(날 출) + 國(나라 국)",
        "pronunciation": "쑤엇 까인",
        "meaningKo": "한 국가의 국민이나 체류 중인 외국인이 그 국가의 영토를 떠나는 행위를 의미합니다. 통역 시 출국 절차(출국심사, 보안검색), 출국 금지 조치(travel ban), 출국 확인서 등을 명확히 전달해야 하며, 미납 세금, 병역 미필, 소송 계류 등으로 출국이 제한될 수 있음을 설명할 수 있어야 합니다. 한국은 출국 시 자동출입국심사 이용률이 높고, 베트남도 유사한 시스템을 도입 중입니다.",
        "meaningVi": "Hành động công dân hoặc người nước ngoài đang lưu trú rời khỏi lãnh thổ một quốc gia. Quy trình bao gồm kiểm tra xuất cảnh, kiểm tra an ninh. Có thể bị cấm xuất cảnh do nợ thuế, chưa hoàn thành nghĩa vụ quân sự, có vụ kiện đang chờ xử lý. Hàn Quốc có tỷ lệ sử dụng hệ thống tự động cao.",
        "context": "공항 출국 절차, 출입국관리, 법적 제재에서 사용",
        "culturalNote": "한국은 출국 시 병역 미필자의 경우 25세 이상이면 국외여행허가를 받아야 하고, 금융채무 불이행자는 출국 금지될 수 있습니다. 베트남도 형사 사건 관련자나 채무 불이행자에게 출국 금지 조치를 취할 수 있습니다. 양국 모두 공항에서 출국심사 후 탑승권 확인까지 일련의 절차가 있으며, 면세점 이용 시간도 고려해야 합니다. 출국 확인은 입국 기록과 연동되어 불법체류 여부 판단에 사용됩니다.",
        "commonMistakes": [
            {
                "mistake": "출국을 'go out' 또는 'leave'로만 통역",
                "correction": "'departure', 'xuất cảnh'으로 공식 용어 사용",
                "explanation": "행정/법률 문서에서는 정확한 용어 필수"
            },
            {
                "mistake": "xuất cảnh을 '수앗까인'으로 발음",
                "correction": "'쑤엇 까인'으로 발음 (xuất의 x는 's' 소리)",
                "explanation": "성조와 함께 정확한 자음 발음 필요"
            },
            {
                "mistake": "출국 금지와 출국 불가를 혼용",
                "correction": "출국 금지는 법적 조치, 출국 불가는 물리적 사유로 구분",
                "explanation": "법적 용어는 정확히 구분해야 함"
            }
        ],
        "examples": [
            {
                "ko": "출국 2시간 전까지 공항에 도착하시기 바랍니다.",
                "vi": "Vui lòng đến sân bay trước 2 giờ trước khi xuất cảnh.",
                "situation": "formal"
            },
            {
                "ko": "출국 금지 조치로 인해 현재 출국이 불가능합니다.",
                "vi": "Do lệnh cấm xuất cảnh, hiện tại không thể xuất cảnh.",
                "situation": "formal"
            },
            {
                "ko": "내일 한국 떠나요.",
                "vi": "Mai tôi xuất cảnh Hàn Quốc.",
                "situation": "informal"
            }
        ],
        "relatedTerms": ["nhap-canh", "thi-thuc", "ho-chieu", "truc-xuat"]
    },
    {
        "slug": "tam-tru",
        "korean": "임시체류",
        "vietnamese": "tạm trú",
        "hanja": "暫住",
        "hanjaReading": "暫(잠깐 잠) + 住(살 주)",
        "pronunciation": "땀 쭈",
        "meaningKo": "외국인이 일정 기간 동안 특정 국가에 합법적으로 머무르는 것을 의미합니다. 통역 시 임시체류와 영주(permanent residence)의 차이, 체류 기간 제한, 체류지 신고 의무 등을 명확히 해야 하며, 베트남어 'tạm trú'는 임시거주를 뜻하므로 '임시체류'와 정확히 대응됩니다. 한국은 외국인등록증 발급 시 체류지를 등록하며 이사 시 14일 내 신고 의무가 있고, 베트남도 유사한 규정이 있습니다.",
        "meaningVi": "Người nước ngoài lưu trú hợp pháp tại một quốc gia trong thời gian nhất định. Cần phân biệt tạm trú (tạm thời) và thường trú (vĩnh viễn). Có thời hạn giới hạn, phải đăng ký chỗ ở. Ở Hàn Quốc, khi làm thẻ đăng ký người nước ngoài phải đăng ký địa chỉ lưu trú, khi chuyển nhà phải báo trong 14 ngày.",
        "context": "출입국관리, 주거지 신고, 비자 행정에서 사용",
        "culturalNote": "한국은 외국인이 90일 이상 체류 시 출입국관리사무소에 외국인등록과 함께 체류지를 신고해야 하며, 체류지 변경 시 14일 내 신고하지 않으면 과태료가 부과됩니다. 베트남도 외국인이 임시거주 시 공안에 신고해야 하며, 호텔 숙박 시 호텔이 대신 신고합니다. 통역 시 양국의 체류지 신고 의무를 명확히 전달하여 법규 위반을 예방해야 합니다.",
        "commonMistakes": [
            {
                "mistake": "임시체류와 단기체류를 같은 의미로 사용",
                "correction": "임시체류는 기간 불문, 단기체류는 보통 90일 이하",
                "explanation": "법적으로 구분되는 개념"
            },
            {
                "mistake": "tạm trú를 '땀뜨루'로 발음",
                "correction": "'땀 쭈'로 발음 (trú는 짧고 강하게)",
                "explanation": "성조와 발음 정확히 해야 의미 전달"
            },
            {
                "mistake": "체류지 변경 신고를 선택사항으로 통역",
                "correction": "법적 의무사항으로 명확히 전달",
                "explanation": "미신고 시 과태료 부과되므로 강조 필요"
            }
        ],
        "examples": [
            {
                "ko": "임시체류 기간 동안 체류지 변경 시 반드시 신고하셔야 합니다.",
                "vi": "Trong thời gian tạm trú, khi thay đổi địa chỉ phải báo cáo bắt buộc.",
                "situation": "formal"
            },
            {
                "ko": "임시체류 허가는 최대 3년까지 가능합니다.",
                "vi": "Giấy phép tạm trú tối đa có thể đến 3 năm.",
                "situation": "formal"
            },
            {
                "ko": "여기서 얼마나 있을 수 있어요?",
                "vi": "Ở đây có thể tạm trú bao lâu?",
                "situation": "informal"
            }
        ],
        "relatedTerms": ["the-tam-tru", "thuong-tru", "thi-thuc", "gia-han-visa"]
    },
    {
        "slug": "thuong-tru",
        "korean": "영주",
        "vietnamese": "thường trú",
        "hanja": "永住",
        "hanjaReading": "永(길 영) + 住(살 주)",
        "pronunciation": "트엉 쭈",
        "meaningKo": "외국인이 특정 국가에 기간 제한 없이 영구적으로 거주할 수 있는 법적 지위를 의미합니다. 통역 시 영주권(permanent residence)과 시민권(citizenship)의 차이, 영주 자격 요건(체류 기간, 소득 요건 등), 영주권 취소 사유 등을 명확히 해야 합니다. 한국의 F-5 비자가 영주 자격이며, 베트남도 유사한 'thường trú' 제도가 있습니다. 영주권자는 대부분의 국민과 동일한 권리를 가지지만 선거권은 없습니다.",
        "meaningVi": "Tư cách pháp lý cho phép người nước ngoài cư trú vĩnh viễn tại một quốc gia không giới hạn thời gian. Cần phân biệt thường trú (permanent residence) và quốc tịch (citizenship). Ở Hàn Quốc visa F-5 là tư cách thường trú, có hầu hết quyền như công dân nhưng không có quyền bầu cử. Có yêu cầu về thời gian lưu trú, thu nhập, v.v.",
        "context": "출입국관리법, 장기 체류 계획, 귀화 절차에서 사용",
        "culturalNote": "한국은 일반적으로 5년 이상 합법 체류, 일정 소득 이상, 한국어 능력 등을 갖추면 F-5 영주 자격을 신청할 수 있으며, 영주권자는 재입국허가 없이 출입국이 자유롭고 거의 모든 경제활동이 가능합니다. 베트남도 유사한 제도가 있지만 요건이 더 까다롭습니다. 영주권은 취소될 수 있으므로(장기 해외 체류, 중범죄 등) 이를 통역 시 명확히 전달해야 합니다.",
        "commonMistakes": [
            {
                "mistake": "영주권과 시민권을 같은 것으로 설명",
                "correction": "영주권은 거주 권리, 시민권은 국적으로 명확히 구분",
                "explanation": "법적 권리와 의무가 다름"
            },
            {
                "mistake": "thường trú를 '트엉뜨루'로 발음",
                "correction": "'트엉 쭈'로 발음",
                "explanation": "trú는 짧고 강하게 발음"
            },
            {
                "mistake": "영주권을 받으면 절대 취소 안 된다고 통역",
                "correction": "일정 조건(중범죄, 장기 해외 체류 등) 시 취소 가능",
                "explanation": "영주권은 조건부 권리임을 명확히 해야 함"
            }
        ],
        "examples": [
            {
                "ko": "5년 이상 체류하고 소득 요건을 충족하면 영주권을 신청할 수 있습니다.",
                "vi": "Nếu lưu trú trên 5 năm và đáp ứng yêu cầu thu nhập có thể xin thường trú.",
                "situation": "formal"
            },
            {
                "ko": "영주권자는 선거권을 제외한 대부분의 권리를 가집니다.",
                "vi": "Người có thường trú có hầu hết quyền trừ quyền bầu cử.",
                "situation": "formal"
            },
            {
                "ko": "영주권 받으면 계속 여기서 살 수 있어요?",
                "vi": "Có thường trú rồi thì có thể ở đây mãi không?",
                "situation": "informal"
            }
        ],
        "relatedTerms": ["tam-tru", "thi-thuc", "the-tam-tru", "nhap-canh"]
    }
]

# 중복 필터링
new_terms_filtered = [t for t in new_terms if t['slug'] not in existing_slugs]

# 데이터 추가
data.extend(new_terms_filtered)

# 저장
with open(file_path, 'w', encoding='utf-8') as f:
    json.dump(data, f, ensure_ascii=False, indent=2)

print(f"✅ {len(new_terms_filtered)}개 용어 추가 완료")
print(f"📊 전체 용어 수: {len(data)}개")
print(f"🎯 추가된 용어: {', '.join([t['slug'] for t in new_terms_filtered])}")
