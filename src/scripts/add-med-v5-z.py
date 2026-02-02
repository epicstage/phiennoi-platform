#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
의료 용어 추가 스크립트 - 감염병/공중보건 (v5-z)
테마: Infectious Disease/Public Health
"""

import json
import os

# 파일 경로 설정
file_path = os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', 'data', 'terms', 'medical.json')

# 추가할 용어 목록 (Tier S 품질 기준 충족)
new_terms = [
    {
        "slug": "luat-phong-chong-benh-truyen-nhiem",
        "korean": "감염병예방법",
        "vietnamese": "Luật phòng chống bệnh truyền nhiễm",
        "hanja": "感染病豫防法",
        "hanjaReading": "感(느낄 감) + 染(물들 염) + 病(병 병) + 豫(미리 예) + 防(막을 방) + 法(법 법)",
        "pronunciation": "루얏 퐁 쫑 벵 쭈옌 니엠",
        "category": "medical",
        "subcategory": "publicHealth",
        "meaningKo": "감염병의 예방 및 관리에 관한 법률을 지칭하는 용어입니다. 한국의 「감염병의 예방 및 관리에 관한 법률」과 베트남의 감염병 관련 법령은 구조와 내용이 다르므로 통역 시 주의가 필요합니다. 한국은 1~4급 분류 체계를 사용하지만 베트남은 A, B, C 그룹으로 분류하므로, 단순 번역이 아닌 양국 법체계의 차이를 설명해야 합니다. 법령 명칭을 통역할 때는 'Luật'(법률)과 'Nghị định'(시행령)을 정확히 구분해야 하며, 실무에서는 약칭보다 정식 명칭을 사용하는 것이 오해를 방지합니다.",
        "meaningVi": "Luật quy định về phòng ngừa và quản lý các bệnh truyền nhiễm. Hệ thống pháp luật về bệnh truyền nhiễm ở Hàn Quốc và Việt Nam có sự khác biệt về cấu trúc và phân loại. Hàn Quốc phân loại theo cấp độ 1-4, trong khi Việt Nam phân loại theo nhóm A, B, C. Khi phiên dịch, cần giải thích rõ sự khác biệt này thay vì chỉ dịch thuật ngữ.",
        "context": "법률/행정 문서, 보건 당국 회의, 의료 법규 설명 시 사용",
        "culturalNote": "한국의 감염병예방법은 질병관리청 주관으로 매우 체계적이며, 위반 시 형사처벌까지 가능합니다. 베트남도 유사한 법체계가 있으나 집행 강도와 세부 규정에 차이가 있습니다. 특히 격리 조치, 신고 의무, 방역 수칙 위반에 대한 처벌 수위가 다르므로, 법률 통역 시 한국의 강제성이 더 높다는 점을 명확히 전달해야 합니다. 또한 한국은 디지털 방역 시스템이 발달했으나 베트남은 수기 신고가 많아 실무 절차에서도 차이가 있습니다.",
        "commonMistakes": [
            {
                "mistake": "Luật bệnh truyền nhiễm",
                "correction": "Luật phòng chống bệnh truyền nhiễm",
                "explanation": "'phòng chống'(예방 및 관리)를 생략하면 법률의 목적이 제대로 전달되지 않음"
            },
            {
                "mistake": "한국과 베트남의 감염병 분류가 같다고 가정",
                "correction": "1~4급 분류와 A/B/C 그룹 분류의 차이를 설명",
                "explanation": "법체계 차이를 모르고 직역하면 실무자에게 혼란을 줌"
            },
            {
                "mistake": "Quy định(규정)로 번역",
                "correction": "Luật(법률)로 번역",
                "explanation": "법률과 하위 규정의 법적 위계를 정확히 구분해야 함"
            }
        ],
        "examples": [
            {
                "ko": "감염병예방법 제11조에 따라 의사는 감염병 환자를 즉시 신고해야 합니다.",
                "vi": "Theo Điều 11 Luật phòng chống bệnh truyền nhiễm, bác sĩ phải báo cáo ngay lập tức khi phát hiện bệnh nhân nhiễm bệnh.",
                "situation": "formal"
            },
            {
                "ko": "이 시설은 감염병예방법 위반으로 과태료 처분을 받았습니다.",
                "vi": "Cơ sở này đã bị xử phạt vi phạm hành chính do vi phạm Luật phòng chống bệnh truyền nhiễm.",
                "situation": "formal"
            },
            {
                "ko": "현장에서는 감염병예방법상 격리 조치를 즉시 시행해야 해요.",
                "vi": "Tại hiện trường, chúng ta phải thực hiện biện pháp cách ly ngay theo quy định của Luật phòng chống bệnh truyền nhiễm.",
                "situation": "onsite"
            }
        ],
        "relatedTerms": ["격리조치", "신고의무", "방역수칙", "질병관리청"]
    },
    {
        "slug": "tu-cach-ly",
        "korean": "자가격리",
        "vietnamese": "Tự cách ly",
        "hanja": "自家隔離",
        "hanjaReading": "自(스스로 자) + 家(집 가) + 隔(사이뜰 격) + 離(떠날 리)",
        "pronunciation": "뜨 깍 리",
        "category": "medical",
        "subcategory": "publicHealth",
        "meaningKo": "감염병 확산 방지를 위해 자택에서 일정 기간 외부와의 접촉을 차단하는 조치입니다. 통역 시 중요한 점은 한국의 자가격리는 법적 강제성이 있어 위반 시 처벌을 받지만, 베트남에서는 집행 강도가 다를 수 있다는 점입니다. 또한 자가격리 기간, 생활수칙, 지원 제도가 양국 간 차이가 있으므로 단순 번역이 아닌 맥락 설명이 필요합니다. 실무에서는 '격리(cách ly)'와 '자가격리(tự cách ly)', '시설격리(cách ly tập trung)'를 명확히 구분해야 오해가 없습니다.",
        "meaningVi": "Biện pháp cách ly tại nhà để ngăn chặn sự lây lan của bệnh truyền nhiễm. Ở Hàn Quốc, tự cách ly có tính chất bắt buộc theo pháp luật và có thể bị xử phạt nếu vi phạm. Thời gian cách ly, quy tắc sinh hoạt và chế độ hỗ trợ có thể khác nhau giữa Hàn Quốc và Việt Nam.",
        "context": "보건소 안내, 입국 절차, 의료기관 지시사항 설명 시 사용",
        "culturalNote": "한국에서는 자가격리 중 GPS 추적, 자가진단앱 사용 등 디지털 감시가 엄격하며, 위반 시 최대 1년 이하 징역 또는 1천만 원 이하 벌금이 부과될 수 있습니다. 베트남도 자가격리 제도가 있으나 디지털 감시 수준과 처벌 강도에 차이가 있습니다. 또한 한국은 자가격리자에게 생활지원금을 지급하는 경우가 많지만, 베트남의 지원 제도는 다를 수 있어 통역 시 이러한 제도적 차이를 설명해야 합니다. 문화적으로도 한국은 집단 방역 준수 의식이 높은 편입니다.",
        "commonMistakes": [
            {
                "mistake": "Cách ly ở nhà",
                "correction": "Tự cách ly",
                "explanation": "'자가'의 '스스로'라는 의미를 'tự'로 정확히 표현해야 함"
            },
            {
                "mistake": "자가격리와 시설격리를 구분하지 않음",
                "correction": "Tự cách ly(자가) vs Cách ly tập trung(시설)",
                "explanation": "격리 장소에 따라 법적 의무와 절차가 완전히 다름"
            },
            {
                "mistake": "자가격리가 자율적 권고라고 설명",
                "correction": "법적 의무사항이며 위반 시 처벌된다고 설명",
                "explanation": "한국의 자가격리는 강제성이 있는 행정명령임"
            }
        ],
        "examples": [
            {
                "ko": "해외 입국자는 7일간 자가격리 의무가 있습니다.",
                "vi": "Người nhập cảnh từ nước ngoài có nghĩa vụ tự cách ly trong 7 ngày.",
                "situation": "formal"
            },
            {
                "ko": "자가격리 중에는 절대 외출하시면 안 됩니다.",
                "vi": "Trong thời gian tự cách ly, tuyệt đối không được ra ngoài.",
                "situation": "onsite"
            },
            {
                "ko": "자가격리 기간 동안 매일 자가진단앱으로 건강 상태를 보고해야 해요.",
                "vi": "Trong suốt thời gian tự cách ly, bạn phải báo cáo tình trạng sức khỏe hàng ngày qua ứng dụng tự kiểm tra.",
                "situation": "informal"
            }
        ],
        "relatedTerms": ["격리조치", "시설격리", "자가진단앱", "생활수칙"]
    },
    {
        "slug": "xet-nghiem-pcr",
        "korean": "PCR검사",
        "vietnamese": "Xét nghiệm PCR",
        "hanja": None,
        "hanjaReading": None,
        "pronunciation": "셋 응이엠 피씨알",
        "category": "medical",
        "subcategory": "diagnostics",
        "meaningKo": "Polymerase Chain Reaction(중합효소 연쇄반응)을 이용한 유전자 증폭 검사로, 감염병 진단의 표준 검사법입니다. 통역 시 주의할 점은 'PCR'은 한국과 베트남 모두 영어 약자를 그대로 사용하지만, '검사'를 'xét nghiệm'으로 번역해야 한다는 점입니다. 또한 신속항원검사(rapid antigen test)와의 차이, 검사 소요 시간, 정확도 차이를 설명할 수 있어야 합니다. 실무에서는 검사 비용, 검사 장소(보건소/병원/임시선별소), 결과 통보 방식 등이 양국 간 다를 수 있어 맥락 설명이 필요합니다.",
        "meaningVi": "Xét nghiệm sử dụng phương pháp Phản ứng chuỗi Polymerase (PCR) để nhân bản gen và chẩn đoán bệnh truyền nhiễm. Đây là phương pháp xét nghiệm chuẩn với độ chính xác cao nhất. Cần phân biệt với xét nghiệm kháng nguyên nhanh (rapid test) về thời gian, độ chính xác và chi phí.",
        "context": "검사 안내, 입국 절차, 진단검사 설명, 의료기관 예약 시 사용",
        "culturalNote": "한국에서는 PCR검사를 보건소에서 무료로 받을 수 있는 경우가 많았으나(정책에 따라 변동), 베트남에서는 검사 비용과 접근성이 다를 수 있습니다. 또한 한국은 검사 후 6시간 내 결과 통보가 일반적이지만, 베트남은 검사 인프라에 따라 소요 시간이 다를 수 있습니다. 통역 시 검사 비용 부담 주체(본인/정부/보험), 검사 결과의 법적 효력(입국서류, 격리해제 증명 등)을 명확히 설명해야 혼란을 방지할 수 있습니다. 문화적으로 한국은 검사 인프라가 매우 발달해 있어 접근성이 높습니다.",
        "commonMistakes": [
            {
                "mistake": "Test PCR",
                "correction": "Xét nghiệm PCR",
                "explanation": "베트남어에서는 'xét nghiệm'(검사)을 먼저 쓰는 어순"
            },
            {
                "mistake": "PCR검사와 신속검사를 같다고 설명",
                "correction": "PCR(정확도 높음, 시간 오래)과 신속검사(빠름, 정확도 낮음)를 구분",
                "explanation": "검사 방법과 목적이 완전히 다름"
            },
            {
                "mistake": "Kiểm tra PCR",
                "correction": "Xét nghiệm PCR",
                "explanation": "'kiểm tra'는 일반적 점검, 'xét nghiệm'은 의학적 검사"
            }
        ],
        "examples": [
            {
                "ko": "입국 시 72시간 이내 발급된 PCR검사 음성확인서가 필요합니다.",
                "vi": "Khi nhập cảnh, cần có giấy xác nhận kết quả xét nghiệm PCR âm tính trong vòng 72 giờ.",
                "situation": "formal"
            },
            {
                "ko": "PCR검사 결과는 내일 오후에 문자로 받으실 수 있습니다.",
                "vi": "Kết quả xét nghiệm PCR sẽ được gửi qua tin nhắn vào chiều mai.",
                "situation": "onsite"
            },
            {
                "ko": "신속검사는 빠르지만 PCR검사가 훨씬 정확해요.",
                "vi": "Xét nghiệm nhanh tuy nhanh nhưng xét nghiệm PCR chính xác hơn nhiều.",
                "situation": "informal"
            }
        ],
        "relatedTerms": ["신속항원검사", "음성확인서", "검체채취", "진단검사"]
    },
    {
        "slug": "dieu-tra-dich-te",
        "korean": "역학조사",
        "vietnamese": "Điều tra dịch tễ",
        "hanja": "疫學調査",
        "hanjaReading": "疫(전염병 역) + 學(배울 학) + 調(고를 조) + 査(조사할 사)",
        "pronunciation": "디에우 짜 직 떼",
        "category": "medical",
        "subcategory": "publicHealth",
        "meaningKo": "감염병 발생 시 감염 경로, 접촉자, 전파 범위 등을 조사하여 추가 확산을 방지하는 공중보건학적 조사 활동입니다. 통역 시 중요한 점은 역학조사가 단순 조사가 아니라 법적 근거에 기반한 강제 조사이며, 조사 거부 시 처벌받을 수 있다는 점을 명확히 전달해야 합니다. 또한 개인정보 수집 범위(동선, 카드사용내역, CCTV 등)가 광범위하므로 프라이버시 우려에 대한 설명도 필요합니다. 한국의 디지털 역학조사 시스템과 베트남의 조사 방식 차이를 이해하고 통역해야 합니다.",
        "meaningVi": "Hoạt động điều tra y tế công cộng để xác định đường lây nhiễm, người tiếp xúc và phạm vi lây lan khi có dịch bệnh xảy ra, nhằm ngăn chặn sự lây lan thêm. Đây là hoạt động điều tra bắt buộc có cơ sở pháp lý, từ chối điều tra có thể bị xử phạt. Thu thập thông tin cá nhân rộng rãi bao gồm lịch trình di chuyển, giao dịch thẻ, camera an ninh.",
        "context": "보건소 역학조사관 면담, 방역 당국 브리핑, 감염병 대응 회의 시 사용",
        "culturalNote": "한국의 역학조사는 매우 체계적이며, 질병관리청과 보건소의 역학조사관이 신속하게 동선을 파악하고 공개합니다. GPS, 카드사용내역, CCTV, 통신 기록까지 활용하여 매우 상세한 조사가 이루어지는데, 이는 개인정보보호보다 공중보건을 우선시하는 문화에서 비롯됩니다. 베트남도 역학조사를 실시하나 디지털 인프라와 조사 범위에 차이가 있을 수 있습니다. 통역 시 조사 협조 의무, 거짓 진술 시 처벌, 조사 결과의 공개 범위 등을 명확히 설명해야 합니다.",
        "commonMistakes": [
            {
                "mistake": "Khảo sát dịch bệnh",
                "correction": "Điều tra dịch tễ",
                "explanation": "'khảo sát'는 일반 설문조사, 'điều tra'는 공식 조사 활동"
            },
            {
                "mistake": "역학조사가 자율적 협조라고 설명",
                "correction": "법적 의무이며 거부 시 처벌된다고 설명",
                "explanation": "감염병예방법상 강제 조사이며 거부권이 제한됨"
            },
            {
                "mistake": "동선 공개가 선택사항이라고 설명",
                "correction": "공익을 위해 필요 범위 내에서 공개될 수 있다고 설명",
                "explanation": "개인정보보다 공중보건이 우선되는 경우가 있음"
            }
        ],
        "examples": [
            {
                "ko": "확진자 발생으로 역학조사를 실시하고 있으니 협조 부탁드립니다.",
                "vi": "Chúng tôi đang tiến hành điều tra dịch tễ do có ca nhiễm được xác nhận, mong quý vị hợp tác.",
                "situation": "formal"
            },
            {
                "ko": "역학조사관이 최근 14일간의 동선을 상세히 질문할 겁니다.",
                "vi": "Nhân viên điều tra dịch tễ sẽ hỏi chi tiết về lịch trình di chuyển 14 ngày qua.",
                "situation": "onsite"
            },
            {
                "ko": "역학조사 때 정확하게 답변하지 않으면 나중에 문제가 될 수 있어요.",
                "vi": "Nếu không trả lời chính xác trong điều tra dịch tễ, sau này có thể gặp vấn đề.",
                "situation": "informal"
            }
        ],
        "relatedTerms": ["접촉자추적", "동선공개", "감염경로", "역학조사관"]
    },
    {
        "slug": "lay-nhiem-tap-the",
        "korean": "집단감염",
        "vietnamese": "Lây nhiễm tập thể",
        "hanja": "集團感染",
        "hanjaReading": "集(모을 집) + 團(무리 단) + 感(느낄 감) + 染(물들 염)",
        "pronunciation": "러이 니엠 땁 테",
        "category": "medical",
        "subcategory": "publicHealth",
        "meaningKo": "특정 집단이나 장소에서 동일한 감염병이 다수에게 발생하는 현象입니다. 통역 시 주의할 점은 '집단감염'과 '유행(epidemic)', '대유행(pandemic)'을 명확히 구분해야 한다는 것입니다. 집단감염은 제한된 집단 내 발생이지만, 유행은 지역 단위, 대유행은 전 세계적 확산을 의미합니다. 또한 한국에서는 집단감염 발생 시 해당 시설의 즉각적인 폐쇄와 전수조사가 이루어지는데, 이러한 강력한 방역 조치가 베트남과 다를 수 있어 맥락 설명이 필요합니다.",
        "meaningVi": "Hiện tượng nhiều người trong một nhóm hoặc địa điểm cụ thể bị nhiễm cùng một bệnh truyền nhiễm. Cần phân biệt với 'dịch bệnh'(epidemic - quy mô khu vực) và 'đại dịch'(pandemic - quy mô toàn cầu). Khi xảy ra lây nhiễm tập thể, cơ sở liên quan thường bị đóng cửa ngay và tiến hành kiểm tra toàn bộ.",
        "context": "방역 브리핑, 언론 보도, 보건 당국 발표, 시설 관리자 교육 시 사용",
        "culturalNote": "한국에서는 집단감염 발생 시 매우 신속하고 강력한 대응이 이루어집니다. 해당 시설(교회, 요양원, 공장 등)은 즉시 폐쇄되고, 관련자 전원에 대한 전수검사와 격리 조치가 시행됩니다. 또한 언론을 통해 집단감염 발생 사실이 신속하게 공개되어 국민의 경각심을 높입니다. 베트남도 유사한 조치를 취하지만, 시설 폐쇄 기준, 검사 범위, 정보 공개 수준에 차이가 있을 수 있습니다. 통역 시 집단감염의 법적 정의(동일 장소/집단에서 일정 기간 내 일정 수 이상 발생)를 명확히 하고, 방역 조치의 강제성을 설명해야 합니다.",
        "commonMistakes": [
            {
                "mistake": "Nhiễm trùng tập thể",
                "correction": "Lây nhiễm tập thể",
                "explanation": "'nhiễm trùng'은 감염 상태, 'lây nhiễm'은 전파/감염 과정"
            },
            {
                "mistake": "집단감염과 유행병을 같다고 설명",
                "correction": "집단감염(제한된 집단)과 유행(지역 확산)을 구분",
                "explanation": "발생 규모와 범위가 완전히 다름"
            },
            {
                "mistake": "Bùng phát dịch",
                "correction": "Lây nhiễm tập thể 또는 Ổ dịch",
                "explanation": "'bùng phát'는 발발/폭발, 집단감염은 'lây nhiễm tập thể' 또는 'ổ dịch'"
            }
        ],
        "examples": [
            {
                "ko": "요양병원에서 집단감염이 발생하여 전원 검사를 실시합니다.",
                "vi": "Do xảy ra lây nhiễm tập thể tại bệnh viện điều양, chúng tôi sẽ tiến hành xét nghiệm toàn bộ.",
                "situation": "formal"
            },
            {
                "ko": "이 시설은 집단감염 발생으로 2주간 운영을 중단합니다.",
                "vi": "Cơ sở này tạm ngưng hoạt động trong 2 tuần do xảy ra lây nhiễm tập thể.",
                "situation": "onsite"
            },
            {
                "ko": "집단감염이 일어나면 관련된 사람들 전부 검사받아야 해요.",
                "vi": "Khi xảy ra lây nhiễm tập thể, tất cả những người liên quan đều phải xét nghiệm.",
                "situation": "informal"
            }
        ],
        "relatedTerms": ["감염병유행", "전수조사", "시설폐쇄", "방역조치"]
    },
    {
        "slug": "kiem-dich",
        "korean": "검역",
        "vietnamese": "Kiểm dịch",
        "hanja": "檢疫",
        "hanjaReading": "檢(검사할 검) + 疫(전염병 역)",
        "pronunciation": "끼엠 직",
        "category": "medical",
        "subcategory": "publicHealth",
        "meaningKo": "국경, 항만, 공항 등에서 감염병의 국내 유입을 막기 위해 사람, 동물, 식물, 화물 등을 검사하는 행정 조치입니다. 통역 시 주의할 점은 검역이 단순 검사가 아니라 법적 강제력이 있는 공식 절차이며, 검역 회피나 거짓 신고 시 처벌받을 수 있다는 점을 명확히 해야 합니다. 또한 '검역'(kiểm dịch), '검사'(xét nghiệm), '심사'(thẩm tra)를 정확히 구분해야 하며, 검역 대상(사람/동물/식물)에 따라 담당 기관과 절차가 다르다는 점도 설명해야 합니다.",
        "meaningVi": "Biện pháp hành chính kiểm tra người, động vật, thực vật và hàng hóa tại biên giới, cảng biển, sân bay để ngăn chặn dịch bệnh xâm nhập vào trong nước. Đây là thủ tục bắt buộc có hiệu lực pháp luật, trốn tránh hoặc khai báo gian dối có thể bị xử phạt. Cần phân biệt 'kiểm dịch'(quarantine), 'xét nghiệm'(test) và 'thẩm tra'(inspection).",
        "context": "공항 입국 절차, 수출입 화물 검사, 동식물 반입 설명 시 사용",
        "culturalNote": "한국의 검역 시스템은 매우 체계적이며, 특히 인천국제공항 등 주요 관문에서는 첨단 검역 장비와 전문 인력이 배치되어 있습니다. 입국자는 Q-CODE(검역정보 사전입력 시스템)를 통해 사전에 건강상태를 신고해야 하며, 발열 등 증상 발견 시 즉시 격리 조치됩니다. 베트남도 검역 시스템이 있으나 디지털화 수준과 검역 범위에 차이가 있을 수 있습니다. 통역 시 검역 대상 품목(금지품, 신고 대상), 검역증 발급 절차, 위반 시 처벌(과태료, 물품 폐기 등)을 구체적으로 설명해야 합니다.",
        "commonMistakes": [
            {
                "mistake": "Kiểm tra dịch bệnh",
                "correction": "Kiểm dịch",
                "explanation": "'검역'은 고유 행정 용어로 'kiểm dịch' 하나로 표현"
            },
            {
                "mistake": "검역과 세관 심사를 같다고 설명",
                "correction": "검역(보건)과 세관(관세)은 별도 절차라고 설명",
                "explanation": "담당 기관과 목적이 완전히 다름"
            },
            {
                "mistake": "검역이 선택사항이라고 설명",
                "correction": "법적 의무 절차이며 회피 시 처벌된다고 설명",
                "explanation": "검역법에 따른 강제 절차임"
            }
        ],
        "examples": [
            {
                "ko": "입국 시 모든 승객은 검역 절차를 거쳐야 합니다.",
                "vi": "Khi nhập cảnh, tất cả hành khách phải trải qua thủ tục kiểm dịch.",
                "situation": "formal"
            },
            {
                "ko": "이 식물은 검역증이 없어서 반입이 불가능합니다.",
                "vi": "Cây này không thể mang vào vì không có giấy chứng nhận kiểm dịch.",
                "situation": "onsite"
            },
            {
                "ko": "공항 검역대에서 발열 체크하고 건강 상태 신고해야 해요.",
                "vi": "Tại khu kiểm dịch sân bay, phải kiểm tra nhiệt độ và khai báo tình trạng sức khỏe.",
                "situation": "informal"
            }
        ],
        "relatedTerms": ["검역증", "입국심사", "Q-CODE", "방역조치"]
    },
    {
        "slug": "khang-khang-sinh",
        "korean": "항생제내성",
        "vietnamese": "Kháng kháng sinh",
        "hanja": "抗生劑耐性",
        "hanjaReading": "抗(막을 항) + 生(날 생) + 劑(약 제) + 耐(견딜 내) + 性(성품 성)",
        "pronunciation": "캉 캉 신",
        "category": "medical",
        "subcategory": "pharmacology",
        "meaningKo": "세균이 항생제에 저항성을 갖게 되어 항생제로 치료가 어려워지는 현상입니다. 통역 시 중요한 점은 이것이 단순한 의학 용어가 아니라 전 세계적인 공중보건 위기 사안이라는 점을 전달해야 합니다. 또한 항생제 오남용의 위험성, 내성균 발생 메커니즘, 예방 방법(처방대로 복용, 임의 중단 금지)을 설명할 수 있어야 합니다. 한국과 베트남 모두 항생제 처방 관리를 강화하고 있으나, 실제 처방 관행과 약국에서의 구입 가능성에 차이가 있을 수 있어 맥락 설명이 필요합니다.",
        "meaningVi": "Hiện tượng vi khuẩn phát triển khả năng kháng lại kháng sinh, khiến việc điều trị bằng kháng sinh trở nên khó khăn. Đây là vấn đề nghiêm trọng của y tế công cộng toàn cầu. Nguyên nhân chính là sử dụng kháng sinh sai cách và lạm dụng. Cần giải thích nguy cơ, cơ chế phát sinh kháng thuốc và cách phòng ngừa (uống đúng đơn, không tự ý ngừng).",
        "context": "약물 처방 설명, 환자 교육, 공중보건 캠페인, 의약품 안전 교육 시 사용",
        "culturalNote": "한국에서는 항생제 처방을 의사만 할 수 있으며, 약국에서 임의 구매가 불가능합니다(일부 예외 제외). 정부는 항생제 적정 사용 캠페인을 지속적으로 진행하고 있으며, 의료기관의 항생제 처방률을 모니터링합니다. 베트남에서도 항생제 관리가 강화되고 있으나, 과거 약국에서 처방전 없이 구입이 가능했던 관행이 남아있는 경우가 있어 실제 접근성에 차이가 있을 수 있습니다. 통역 시 항생제 내성의 심각성(슈퍼박테리아, 치료 불가능한 감염), 올바른 복용법(용량, 기간 준수), 예방 수칙을 강조해야 합니다.",
        "commonMistakes": [
            {
                "mistake": "Chống kháng sinh",
                "correction": "Kháng kháng sinh",
                "explanation": "'kháng'(저항)이 정확한 표현, 'chống'(대항)은 부적절"
            },
            {
                "mistake": "항생제내성이 사람에게 생긴다고 설명",
                "correction": "세균이 내성을 갖게 되는 것이라고 설명",
                "explanation": "내성은 사람이 아닌 세균에게 발생하는 현상"
            },
            {
                "mistake": "Kháng thuốc kháng sinh",
                "correction": "Kháng kháng sinh (또는 Đề kháng kháng sinh)",
                "explanation": "간결하고 정확한 표현 사용"
            }
        ],
        "examples": [
            {
                "ko": "항생제내성 발생을 막기 위해 처방된 기간만큼 정확히 복용해야 합니다.",
                "vi": "Để ngăn ngừa kháng kháng sinh, bạn phải uống đúng thời gian được kê đơn.",
                "situation": "formal"
            },
            {
                "ko": "이 환자는 항생제내성균에 감염되어 치료가 어렵습니다.",
                "vi": "Bệnh nhân này bị nhiễm vi khuẩn kháng kháng sinh nên khó điều trị.",
                "situation": "onsite"
            },
            {
                "ko": "증상이 나아져도 항생제를 임의로 끊으면 내성이 생길 수 있어요.",
                "vi": "Dù triệu chứng thuyên giảm, nếu tự ý ngừng kháng sinh có thể phát sinh kháng thuốc.",
                "situation": "informal"
            }
        ],
        "relatedTerms": ["슈퍼박테리아", "항생제처방", "약물내성", "적정사용"]
    },
    {
        "slug": "giay-chung-nhan-tiem-phong",
        "korean": "예방접종증명서",
        "vietnamese": "Giấy chứng nhận tiêm phòng",
        "hanja": "豫防接種證明書",
        "hanjaReading": "豫(미리 예) + 防(막을 방) + 接(이을 접) + 種(심을 종) + 證(증거 증) + 明(밝을 명) + 書(글 서)",
        "pronunciation": "저이 쯩 년 띠엠 퐁",
        "category": "medical",
        "subcategory": "publicHealth",
        "meaningKo": "예방접종을 받은 사실을 증명하는 공식 문서로, 주로 해외여행, 입국, 학교 입학 등에 필요합니다. 통역 시 주의할 점은 종이 증명서와 전자 증명서(COOV 등)의 차이, 국제 공인 여부, 유효기간, 발급 기관을 명확히 해야 한다는 것입니다. 또한 한국의 '예방접종 도우미' 시스템과 베트남의 접종 기록 관리 시스템이 다르므로, 국가 간 증명서 인정 여부와 추가 접종 필요 여부를 확인해야 합니다. 실무에서는 어떤 백신이 필수인지, 어디서 발급받는지, 영문 증명서 발급 가능 여부 등을 설명할 수 있어야 합니다.",
        "meaningVi": "Giấy tờ chính thức chứng nhận đã tiêm phòng, thường cần thiết cho du lịch nước ngoài, nhập cảnh, nhập học. Cần phân biệt giấy chứng nhận giấy và giấy chứng nhận điện tử (COOV v.v.), tính hợp lệ quốc tế, thời hạn hiệu lực, cơ quan cấp. Hệ thống quản lý hồ sơ tiêm chủng ở Hàn Quốc và Việt Nam khác nhau, cần xác nhận các nước có công nhận lẫn nhau hay không và có cần tiêm bổ sung hay không.",
        "context": "공항 입국 수속, 학교/직장 제출 서류, 비자 신청, 의료기관 확인 시 사용",
        "culturalNote": "한국에서는 예방접종 기록이 '예방접종 도우미' 시스템에 전자적으로 관리되며, 보건소나 병원에서 쉽게 영문 증명서를 발급받을 수 있습니다. 특히 코로나19 이후 COOV(전자예방접종증명서) 앱을 통해 QR코드로 접종 이력을 즉시 확인할 수 있게 되었습니다. 베트남도 전자 증명서 시스템을 도입하고 있으나, 국제 공인 범위와 디지털 인프라에 차이가 있을 수 있습니다. 통역 시 어떤 백신이 필수인지(황열, 콜레라 등 국가별 다름), 접종 후 유효기간, 부스터샷 필요 여부 등을 설명해야 합니다.",
        "commonMistakes": [
            {
                "mistake": "Giấy tiêm chủng",
                "correction": "Giấy chứng nhận tiêm phòng",
                "explanation": "공식 증명서는 'chứng nhận'을 포함해야 함"
            },
            {
                "mistake": "접종 기록과 증명서를 같다고 설명",
                "correction": "기록(hồ sơ)과 공식 증명서(giấy chứng nhận)를 구분",
                "explanation": "기록은 내부 문서, 증명서는 공식 발급 문서"
            },
            {
                "mistake": "모든 접종증명서가 국제적으로 인정된다고 설명",
                "correction": "국가별로 인정 범위가 다르며 확인이 필요하다고 설명",
                "explanation": "WHO 인증, 국가 간 협정 등에 따라 인정 여부가 다름"
            }
        ],
        "examples": [
            {
                "ko": "입국 시 코로나19 예방접종증명서를 제출해야 합니다.",
                "vi": "Khi nhập cảnh, bạn phải nộp giấy chứng nhận tiêm phòng COVID-19.",
                "situation": "formal"
            },
            {
                "ko": "보건소에서 영문 예방접종증명서를 발급받을 수 있습니다.",
                "vi": "Bạn có thể xin cấp giấy chứng nhận tiêm phòng bằng tiếng Anh tại trạm y tế.",
                "situation": "onsite"
            },
            {
                "ko": "COOV 앱에서 전자 접종증명서를 바로 확인할 수 있어요.",
                "vi": "Trên ứng dụng COOV, bạn có thể kiểm tra ngay giấy chứng nhận tiêm phòng điện tử.",
                "situation": "informal"
            }
        ],
        "relatedTerms": ["예방접종기록", "COOV", "국제공인백신", "부스터샷"]
    },
    {
        "slug": "khai-bao-benh-truyen-nhiem",
        "korean": "감염병신고",
        "vietnamese": "Khai báo bệnh truyền nhiễm",
        "hanja": "感染病申告",
        "hanjaReading": "感(느낄 감) + 染(물들 염) + 病(병 병) + 申(펼 신) + 告(알릴 고)",
        "pronunciation": "카이 바오 벵 쭈옌 니엠",
        "category": "medical",
        "subcategory": "publicHealth",
        "meaningKo": "의료기관이나 개인이 감염병 환자 발생을 보건 당국에 의무적으로 보고하는 법적 절차입니다. 통역 시 중요한 점은 이것이 선택사항이 아니라 법적 의무이며, 신고 지연이나 미신고 시 처벌받을 수 있다는 점을 명확히 해야 합니다. 또한 신고 대상 감염병의 종류(1~4급), 신고 시한(즉시/24시간 이내), 신고 방법(전산, 전화, 팩스)을 정확히 설명해야 합니다. 한국과 베트남의 신고 대상 질병, 신고 절차, 처벌 수위가 다를 수 있어 양국 제도의 차이를 이해하고 통역해야 합니다.",
        "meaningVi": "Thủ tục pháp lý bắt buộc mà cơ sở y tế hoặc cá nhân phải báo cáo cho cơ quan y tế khi phát hiện bệnh nhân nhiễm bệnh truyền nhiễm. Đây không phải là tùy chọn mà là nghĩa vụ pháp lý, chậm báo cáo hoặc không báo cáo có thể bị xử phạt. Cần giải thích rõ loại bệnh phải báo (cấp 1-4), thời hạn báo cáo (ngay lập tức/trong 24 giờ), phương thức báo cáo (điện tử, điện thoại, fax).",
        "context": "의료기관 의무 교육, 보건소 지침, 법률 설명, 의사 면허 교육 시 사용",
        "culturalNote": "한국에서는 감염병예방법에 따라 의사, 한의사, 간호사 등이 법정 감염병을 진단하거나 의심되는 경우 즉시(1급) 또는 24시간 이내(2~4급) 관할 보건소에 신고해야 합니다. 신고는 '질병보건통합관리시스템'을 통해 전산으로 이루어지며, 미신고 시 500만 원 이하의 과태료가 부과됩니다. 베트남도 유사한 신고 제도가 있으나 신고 대상 질병의 분류, 신고 시한, 처벌 수위에 차이가 있을 수 있습니다. 통역 시 신고 의무자(의사, 병원장 등), 신고 내용(환자 정보, 진단명 등), 정보 보호 의무를 명확히 설명해야 합니다.",
        "commonMistakes": [
            {
                "mistake": "Thông báo bệnh truyền nhiễm",
                "correction": "Khai báo bệnh truyền nhiễm",
                "explanation": "'khai báo'가 공식적인 신고/보고 용어"
            },
            {
                "mistake": "감염병신고가 권고사항이라고 설명",
                "correction": "법적 의무이며 위반 시 과태료가 부과된다고 설명",
                "explanation": "감염병예방법상 강제 의무 사항임"
            },
            {
                "mistake": "모든 감염병을 신고해야 한다고 설명",
                "correction": "법정 감염병(1~4급)만 신고 대상이라고 설명",
                "explanation": "신고 대상은 법으로 지정된 질병에 한정됨"
            }
        ],
        "examples": [
            {
                "ko": "결핵 환자를 진단한 의사는 24시간 이내에 감염병신고를 해야 합니다.",
                "vi": "Bác sĩ chẩn đoán bệnh nhân lao phải khai báo bệnh truyền nhiễm trong vòng 24 giờ.",
                "situation": "formal"
            },
            {
                "ko": "감염병신고를 하지 않으면 과태료 처분을 받을 수 있습니다.",
                "vi": "Nếu không khai báo bệnh truyền nhiễm, có thể bị xử phạt vi phạm hành chính.",
                "situation": "onsite"
            },
            {
                "ko": "의심 환자라도 일단 신고하고 나중에 확진 여부를 업데이트하면 돼요.",
                "vi": "Ngay cả ca nghi ngờ cũng nên báo cáo trước, sau đó cập nhật kết quả xác nhận.",
                "situation": "informal"
            }
        ],
        "relatedTerms": ["법정감염병", "신고의무", "질병관리청", "신고지연"]
    },
    {
        "slug": "quy-tac-phong-dich",
        "korean": "방역수칙",
        "vietnamese": "Quy tắc phòng dịch",
        "hanja": "防疫守則",
        "hanjaReading": "防(막을 방) + 疫(전염병 역) + 守(지킬 수) + 則(법칙 칙)",
        "pronunciation": "꾸이 딱 퐁 직",
        "category": "medical",
        "subcategory": "publicHealth",
        "meaningKo": "감염병 확산을 방지하기 위해 개인이나 집단이 지켜야 할 규칙과 지침입니다. 통역 시 주의할 점은 방역수칙이 단순 권고가 아니라 행정명령에 기반한 강제 사항일 수 있다는 점을 명확히 해야 합니다. 또한 구체적인 수칙 내용(마스크 착용, 거리두기, 손씻기, 환기 등)과 위반 시 처벌(과태료, 시설 운영 중단 등)을 정확히 전달해야 합니다. 한국의 사회적 거리두기 단계, 마스크 착용 의무화 등의 방역 조치가 시기와 상황에 따라 변동되므로, 최신 정보를 반영한 통역이 필요합니다.",
        "meaningVi": "Quy tắc và hướng dẫn mà cá nhân hoặc tập thể phải tuân thủ để ngăn chặn sự lây lan của dịch bệnh. Cần làm rõ rằng quy tắc phòng dịch có thể không chỉ là khuyến cáo mà là biện pháp bắt buộc dựa trên lệnh hành chính. Phải truyền đạt chính xác nội dung cụ thể (đeo khẩu trang, giãn cách, rửa tay, thông gió) và hình phạt khi vi phạm (phạt tiền, đình chỉ hoạt động cơ sở).",
        "context": "공공장소 안내문, 시설 이용 규칙, 방역 당국 발표, 직장/학교 지침 시 사용",
        "culturalNote": "한국에서는 방역수칙 준수가 매우 엄격하게 시행되며, 마스크 착용 의무화, 사회적 거리두기 단계별 조치, QR코드 출입 기록 등이 강력하게 시행되었습니다. 위반 시 개인은 10만 원, 시설은 300만 원의 과태료가 부과되며, 반복 위반 시 시설 운영 정지까지 가능합니다. 베트남도 유사한 방역 조치를 취하지만, 디지털 추적 시스템의 발달 정도, 시민의 준수 문화, 처벌 강도에 차이가 있을 수 있습니다. 통역 시 방역수칙의 법적 근거(감염병예방법, 재난안전법), 시행 기간, 단계별 차이를 명확히 설명해야 합니다.",
        "commonMistakes": [
            {
                "mistake": "Hướng dẫn phòng dịch",
                "correction": "Quy tắc phòng dịch",
                "explanation": "'hướng dẫn'은 가이드, 'quy tắc'은 준수해야 할 규칙"
            },
            {
                "mistake": "방역수칙이 선택적 권고라고 설명",
                "correction": "상황에 따라 법적 의무이며 위반 시 과태료가 부과된다고 설명",
                "explanation": "행정명령에 기반한 경우 강제성이 있음"
            },
            {
                "mistake": "Quy định phòng chống dịch",
                "correction": "Quy tắc phòng dịch",
                "explanation": "'quy tắc'이 더 일상적이고 명확한 표현"
            }
        ],
        "examples": [
            {
                "ko": "실내에서는 반드시 마스크를 착용하는 것이 방역수칙입니다.",
                "vi": "Quy tắc phòng dịch yêu cầu bắt buộc phải đeo khẩu trang trong nhà.",
                "situation": "formal"
            },
            {
                "ko": "이 시설은 방역수칙 위반으로 2주간 운영 정지 처분을 받았습니다.",
                "vi": "Cơ sở này đã bị đình chỉ hoạt động 2 tuần do vi phạm quy tắc phòng dịch.",
                "situation": "onsite"
            },
            {
                "ko": "방역수칙 잘 지키면 감염 위험을 크게 줄일 수 있어요.",
                "vi": "Nếu tuân thủ tốt quy tắc phòng dịch, có thể giảm đáng kể nguy cơ lây nhiễm.",
                "situation": "informal"
            }
        ],
        "relatedTerms": ["사회적거리두기", "마스크착용", "출입명부", "방역조치"]
    }
]

def main():
    print("=" * 60)
    print("의료 용어 추가 스크립트 (감염병/공중보건)")
    print("=" * 60)

    # 파일 읽기
    try:
        with open(file_path, 'r', encoding='utf-8') as f:
            data = json.load(f)
        print(f"✅ 파일 로드 성공: {len(data)}개 기존 용어")
    except FileNotFoundError:
        print(f"❌ 파일을 찾을 수 없습니다: {file_path}")
        return
    except json.JSONDecodeError as e:
        print(f"❌ JSON 파싱 오류: {e}")
        return

    # 중복 필터링
    existing_slugs = {term['slug'] for term in data}
    new_unique_terms = [term for term in new_terms if term['slug'] not in existing_slugs]

    duplicate_count = len(new_terms) - len(new_unique_terms)
    if duplicate_count > 0:
        print(f"⚠️  중복 제거: {duplicate_count}개 용어")

    if not new_unique_terms:
        print("❌ 추가할 새 용어가 없습니다 (모두 중복)")
        return

    # 용어 추가
    data.extend(new_unique_terms)
    print(f"✅ {len(new_unique_terms)}개 용어 추가 완료")

    # 파일 저장
    try:
        with open(file_path, 'w', encoding='utf-8') as f:
            json.dump(data, f, ensure_ascii=False, indent=2)
        print(f"✅ 파일 저장 완료: {len(data)}개 총 용어")
    except Exception as e:
        print(f"❌ 파일 저장 실패: {e}")
        return

    print("\n" + "=" * 60)
    print("추가된 용어 목록:")
    print("=" * 60)
    for i, term in enumerate(new_unique_terms, 1):
        print(f"{i:2d}. {term['korean']:12s} → {term['vietnamese']}")

    print("\n" + "=" * 60)
    print("품질 검증을 위해 다음 명령어를 실행하세요:")
    print("npm run validate:terms -- --domain=medical")
    print("=" * 60)

if __name__ == "__main__":
    main()
