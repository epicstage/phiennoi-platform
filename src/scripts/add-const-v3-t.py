#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Construction Domain - Demolition & Remodeling Terms (해체/리모델링)
Add 10 terms: 철거, 석면제거, 폐기물처리, 구조보강, 탄소섬유보강, 에폭시주입, 리모델링, 증축, 용도변경, 내진보강
"""

import json
import os

# 추가할 용어 데이터 (Tier S 기준)
new_terms = [
    {
        "slug": "철거-phá-dỡ",
        "korean": "철거",
        "vietnamese": "Phá dỡ",
        "hanja": "撤去",
        "hanjaReading": "撤(철거할 철) + 去(갈 거)",
        "pronunciation": "퍼 저이",
        "meaningKo": "건축물이나 구조물을 해체하여 제거하는 작업. 통역 시 '철거'와 '해체'를 구분해야 함 - 철거는 완전 제거, 해체는 부분적 분리. 베트남 현장에서는 안전 절차(quy trình an toàn)와 분진 방지(chống bụi) 강조가 필수. '철거 허가(giấy phép phá dỡ)' 관련 행정 용어도 숙지 필요.",
        "meaningVi": "Công việc tháo dỡ và loại bỏ hoàn toàn công trình xây dựng hoặc kết cấu. Phá dỡ thường áp dụng cho toàn bộ công trình, trong khi tháo dỡ có thể chỉ một phần. Cần tuân thủ nghiêm ngặt các quy định về an toàn lao động và bảo vệ môi trường.",
        "context": "건설 현장, 리모델링 프로젝트, 재개발 사업",
        "culturalNote": "한국은 철거 전 석면 조사가 법적 의무이나, 베트남은 일부 지역에서 규제가 느슨한 편. 한국 통역사는 '안전 제일(an toàn là trên hết)' 원칙을 강조하여 현장 문화 차이를 메워야 함. 또한 한국의 철거 허가 절차가 베트남보다 복잡함을 설명 필요.",
        "commonMistakes": [
            {
                "mistake": "Phá dỡ를 '폭파'로 오역",
                "correction": "'철거'로 번역 (폭파는 Nổ mìn)",
                "explanation": "Phá dỡ는 일반 철거, 폭파는 별도 용어"
            },
            {
                "mistake": "'철거'를 Dỡ bỏ로만 표현",
                "correction": "공식 문서에서는 Phá dỡ 사용",
                "explanation": "Dỡ bỏ는 구어체, Phá dỡ가 법적 용어"
            },
            {
                "mistake": "철거 범위를 명확히 하지 않음",
                "correction": "'전체 철거(phá dỡ toàn bộ)' vs '부분 철거(phá dỡ một phần)' 구분",
                "explanation": "범위 불명확 시 현장 혼선 발생"
            }
        ],
        "examples": [
            {
                "ko": "석면 조사 후 철거 작업을 시작하겠습니다.",
                "vi": "Sau khi kiểm tra amiăng, chúng tôi sẽ bắt đầu công việc phá dỡ.",
                "situation": "formal"
            },
            {
                "ko": "이 건물은 부분 철거만 진행됩니다.",
                "vi": "Tòa nhà này chỉ tiến hành phá dỡ một phần.",
                "situation": "onsite"
            },
            {
                "ko": "철거 허가증을 먼저 받아야 합니다.",
                "vi": "Phải xin giấy phép phá dỡ trước đã.",
                "situation": "informal"
            }
        ],
        "relatedTerms": ["해체", "석면제거", "폐기물처리", "안전관리"]
    },
    {
        "slug": "석면제거-loại-bỏ-amiăng",
        "korean": "석면제거",
        "vietnamese": "Loại bỏ amiăng",
        "hanja": "石綿除去",
        "hanjaReading": "石(돌 석) + 綿(솜 면) + 除(덜 제) + 去(갈 거)",
        "pronunciation": "로아이 버 아미앙",
        "meaningKo": "건축물 내 석면 함유 자재를 안전하게 제거하는 작업. 통역 시 반드시 '작업자 보호구(thiết bị bảo hộ)' 착용 강조 필요 - 석면은 1급 발암물질. 베트남 현장에서는 '음압 설비(hệ thống áp suất âm)' 개념이 생소할 수 있어 설명 필수. '석면 해체 신고' 절차도 통역 빈출 항목.",
        "meaningVi": "Công việc tháo dỡ và loại bỏ an toàn các vật liệu có chứa amiăng trong công trình. Amiăng là chất gây ung thư nhóm 1, cần tuân thủ nghiêm ngặt quy trình an toàn bao gồm trang bị bảo hộ đầy đủ, hệ thống áp suất âm, và phương pháp xử lý chất thải đặc biệt.",
        "context": "리모델링 현장, 노후 건물 철거, 안전 교육",
        "culturalNote": "한국은 석면 관련 법규가 매우 엄격하나, 베트남은 최근에야 규제 강화 추세. 한국 통역사는 석면의 위험성(nguy hiểm của amiăng)을 문화적 맥락에서 설명해야 함. '건강 검진(khám sức khỏe)' 의무화도 한국 특유 제도임을 명시.",
        "commonMistakes": [
            {
                "mistake": "Amiăng를 '석면'이 아닌 '석탄'으로 오역",
                "correction": "Amiăng = 석면 (석탄은 Than đá)",
                "explanation": "발음 유사하나 완전히 다른 물질"
            },
            {
                "mistake": "'제거'를 단순히 Xóa로 표현",
                "correction": "Loại bỏ 또는 Tháo dỡ 사용",
                "explanation": "Xóa는 '지우다', 석면은 물리적 제거"
            },
            {
                "mistake": "보호구 착용 지시를 생략",
                "correction": "'Bắt buộc đeo đầy đủ thiết bị bảo hộ' 명확히 통역",
                "explanation": "생명과 직결된 안전 지시는 강조 필수"
            }
        ],
        "examples": [
            {
                "ko": "석면제거 작업 중에는 반드시 방진 마스크를 착용하세요.",
                "vi": "Trong quá trình loại bỏ amiăng, bắt buộc phải đeo khẩu trang chống bụi.",
                "situation": "formal"
            },
            {
                "ko": "음압 설비 설치 후 석면 해체를 시작합니다.",
                "vi": "Sau khi lắp đặt hệ thống áp suất âm, bắt đầu tháo dỡ amiăng.",
                "situation": "onsite"
            },
            {
                "ko": "석면 나오면 작업 바로 중단하고 신고해야 돼.",
                "vi": "Nếu phát hiện amiăng, phải dừng ngay và báo cáo.",
                "situation": "informal"
            }
        ],
        "relatedTerms": ["철거", "안전관리", "폐기물처리", "작업자보호"]
    },
    {
        "slug": "폐기물처리-xử-lý-chất-thải",
        "korean": "폐기물처리",
        "vietnamese": "Xử lý chất thải",
        "hanja": "廢棄物處理",
        "hanjaReading": "廢(버릴 폐) + 棄(버릴 기) + 物(물건 물) + 處(곳 처) + 理(다스릴 리)",
        "pronunciation": "쑤 리 쩟 타이",
        "meaningKo": "건설 현장에서 발생한 쓰레기와 부산물을 법적 기준에 따라 처리하는 과정. 통역 시 '일반 폐기물(chất thải thông thường)'과 '지정 폐기물(chất thải nguy hại)' 구분 필수. 베트남은 '폐기물 운반 허가(giấy phép vận chuyển chất thải)' 제도가 한국과 달라 설명 필요. 불법 투기 방지 교육도 통역 빈출.",
        "meaningVi": "Quá trình xử lý rác thải và phụ phẩm phát sinh tại công trường xây dựng theo quy định pháp luật. Bao gồm phân loại (phân loại), thu gom (thu gom), vận chuyển (vận chuyển) và xử lý cuối cùng (xử lý cuối cùng) tại cơ sở được cấp phép.",
        "context": "건설 현장, 환경 관리, 행정 절차",
        "culturalNote": "한국은 폐기물 분리배출 문화가 강하나, 베트남 일부 지역은 아직 혼합 배출이 일반적. 통역사는 '재활용(tái chế)' 개념을 강조하여 환경 의식 고취 필요. 또한 한국의 '처리 비용 선지급' 제도가 베트남 업체에 생소할 수 있음.",
        "commonMistakes": [
            {
                "mistake": "Chất thải를 '쓰레기(rác)'로만 번역",
                "correction": "공식 문서에서는 Chất thải 사용",
                "explanation": "Rác은 일반 쓰레기, Chất thải가 법적 용어"
            },
            {
                "mistake": "'처리'를 Xóa로 오역",
                "correction": "Xử lý 사용 (처리 = 관리 프로세스)",
                "explanation": "Xóa는 단순 삭제, Xử lý는 체계적 처리"
            },
            {
                "mistake": "폐기물 분류를 생략",
                "correction": "'일반/지정/건설 폐기물' 구분하여 통역",
                "explanation": "분류에 따라 처리 방법과 비용이 달라짐"
            }
        ],
        "examples": [
            {
                "ko": "건설 폐기물은 지정된 처리 업체로 운반해야 합니다.",
                "vi": "Chất thải xây dựng phải được vận chuyển đến đơn vị xử lý được chỉ định.",
                "situation": "formal"
            },
            {
                "ko": "콘크리트 파쇄물은 재활용 가능합니다.",
                "vi": "Mảnh vỡ bê tông có thể tái chế được.",
                "situation": "onsite"
            },
            {
                "ko": "폐기물 아무데나 버리면 안 돼요.",
                "vi": "Không được vứt chất thải bừa bãi đâu nhé.",
                "situation": "informal"
            }
        ],
        "relatedTerms": ["철거", "환경관리", "재활용", "안전관리"]
    },
    {
        "slug": "구조보강-gia-cố-kết-cấu",
        "korean": "구조보강",
        "vietnamese": "Gia cố kết cấu",
        "hanja": "構造補強",
        "hanjaReading": "構(얽을 구) + 造(지을 조) + 補(기울 보) + 強(강할 강)",
        "pronunciation": "자 꼬 껫 까우",
        "meaningKo": "기존 건축물의 구조적 안전성을 높이기 위해 추가 부재나 공법을 적용하는 작업. 통역 시 '내력벽(tường chịu lực)'과 '비내력벽(tường không chịu lực)' 구분 필수. 베트남 현장에서는 '탄소섬유 시트(tấm sợi carbon)' 공법이 생소할 수 있어 상세 설명 필요. '구조 안전 진단' 결과 기반 작업임을 강조.",
        "meaningVi": "Công việc áp dụng thêm cấu kiện hoặc phương pháp thi công để nâng cao độ an toàn kết cấu của công trình hiện có. Thường được thực hiện sau khi kiểm tra an toàn kết cấu (kiểm định kết cấu), bao gồm các phương pháp như gia cố bằng thép, sợi carbon, hoặc bê tông phun.",
        "context": "리모델링, 노후 건물 보수, 내진 보강",
        "culturalNote": "한국은 '30년 이상 건물 구조 진단' 법제화가 되어 있으나, 베트남은 상대적으로 느슨. 통역사는 한국의 '예방적 보강(gia cố phòng ngừa)' 문화를 설명하여 안전 인식 격차 메워야 함. 또한 한국의 내진 설계 기준이 베트남보다 엄격함을 명시.",
        "commonMistakes": [
            {
                "mistake": "Gia cố를 '수리(sửa chữa)'로 번역",
                "correction": "'구조보강'은 Gia cố kết cấu (수리는 일반 보수)",
                "explanation": "수리는 외관, 보강은 구조적 안전성"
            },
            {
                "mistake": "'보강'을 Tăng cường으로만 표현",
                "correction": "구조 맥락에서는 Gia cố 사용",
                "explanation": "Tăng cường은 일반 강화, Gia cố는 구조 전문 용어"
            },
            {
                "mistake": "보강 방법을 구체적으로 설명 안 함",
                "correction": "'탄소섬유/강판/콘크리트 증타' 등 공법 명시",
                "explanation": "공법에 따라 공기와 비용 차이 큼"
            }
        ],
        "examples": [
            {
                "ko": "기둥에 탄소섬유 시트를 감아 구조보강을 실시합니다.",
                "vi": "Quấn tấm sợi carbon vào cột để gia cố kết cấu.",
                "situation": "formal"
            },
            {
                "ko": "이 벽은 내력벽이라 함부로 철거하면 안 됩니다.",
                "vi": "Bức tường này là tường chịu lực nên không được phá dỡ tùy tiện.",
                "situation": "onsite"
            },
            {
                "ko": "구조 보강 안 하면 위험해요.",
                "vi": "Không gia cố kết cấu thì nguy hiểm lắm.",
                "situation": "informal"
            }
        ],
        "relatedTerms": ["내진보강", "탄소섬유보강", "에폭시주입", "구조안전진단"]
    },
    {
        "slug": "탄소섬유보강-gia-cố-sợi-carbon",
        "korean": "탄소섬유보강",
        "vietnamese": "Gia cố sợi carbon",
        "hanja": None,
        "hanjaReading": None,
        "pronunciation": "자 꼬 서이 까본",
        "meaningKo": "탄소섬유 시트나 판을 구조물 표면에 부착하여 강도를 높이는 보강 공법. 통역 시 'CFRP(Carbon Fiber Reinforced Polymer)' 약어 설명 필요. 베트남 현장에서는 '에폭시 수지(nhựa epoxy)' 접착 과정이 중요하므로 양생 시간 통역 주의. 무게 증가 없이 강도 향상이 장점임을 강조.",
        "meaningVi": "Phương pháp gia cố kết cấu bằng cách dán tấm hoặc cuộn sợi carbon lên bề mặt kết cấu để tăng cường độ. Ưu điểm lớn là không làm tăng trọng lượng kết cấu nhưng vẫn nâng cao khả năng chịu lực đáng kể. Quá trình thi công yêu cầu kỹ thuật cao, đặc biệt là khâu dán bằng nhựa epoxy.",
        "context": "구조보강, 교량 보수, 고층 건물 리모델링",
        "culturalNote": "한국은 탄소섬유 보강이 일반화되었으나, 베트남은 고가 공법으로 인식. 통역사는 '장기적 비용 효율(hiệu quả chi phí dài hạn)'을 강조하여 기술 수용도 높여야 함. 또한 한국의 '품질 인증서(giấy chứng nhận chất lượng)' 요구 사항도 설명 필요.",
        "commonMistakes": [
            {
                "mistake": "Carbon fiber를 '탄소 섬유' 대신 '탄소강'으로 오역",
                "correction": "Sợi carbon = 탄소섬유 (탄소강은 Thép carbon)",
                "explanation": "재질이 완전히 다른 물질"
            },
            {
                "mistake": "'보강'을 Tăng cường으로만 표현",
                "correction": "Gia cố sợi carbon이 정확한 용어",
                "explanation": "구조 전문 용어로 통일 필요"
            },
            {
                "mistake": "에폭시 양생 시간을 생략",
                "correction": "'24시간 양생 필수' 등 구체적 지시 통역",
                "explanation": "양생 미준수 시 접착 실패로 안전 문제"
            }
        ],
        "examples": [
            {
                "ko": "보 하부에 탄소섬유 시트를 3겹 적층합니다.",
                "vi": "Dán 3 lớp tấm sợi carbon ở dưới dầm.",
                "situation": "formal"
            },
            {
                "ko": "에폭시가 완전히 경화될 때까지 하중 금지입니다.",
                "vi": "Cấm chịu tải cho đến khi nhựa epoxy đóng rắn hoàn toàn.",
                "situation": "onsite"
            },
            {
                "ko": "탄소섬유 붙이면 기둥 두껍게 안 해도 돼요.",
                "vi": "Dán sợi carbon thì không cần làm cột dày đâu.",
                "situation": "informal"
            }
        ],
        "relatedTerms": ["구조보강", "에폭시주입", "내진보강", "CFRP"]
    },
    {
        "slug": "에폭시주입-bơm-nhựa-epoxy",
        "korean": "에폭시주입",
        "vietnamese": "Bơm nhựa epoxy",
        "hanja": None,
        "hanjaReading": None,
        "pronunciation": "범 느아 에복시",
        "meaningKo": "균열이나 공극에 에폭시 수지를 주입하여 구조물을 일체화하고 방수 성능을 회복하는 공법. 통역 시 '크랙 폭(độ rộng vết nứt)'에 따라 주입 압력 조절 필요함을 설명. 베트남 현장에서는 '주입기(máy bơm)'의 압력 단위 통일(MPa vs kg/cm²) 주의. 온도와 습도가 경화 시간에 영향을 미침을 강조.",
        "meaningVi": "Phương pháp bơm nhựa epoxy vào các vết nứt hoặc khe rỗng để liên kết lại kết cấu và khôi phục khả năng chống thấm. Kỹ thuật này yêu cầu kiểm soát chặt chẽ áp suất bơm theo độ rộng vết nứt, nhiệt độ và độ ẩm môi trường để đảm bảo nhựa epoxy thấm đều và đóng rắn hoàn toàn.",
        "context": "균열 보수, 누수 방지, 구조 복원",
        "culturalNote": "한국은 에폭시 주입 기술자 자격증 제도가 있으나, 베트남은 경험 위주. 통역사는 '시공 자격(chứng chỉ thi công)' 개념을 설명하여 품질 관리 인식 제고 필요. 또한 한국의 '주입 전 건조(làm khô trước khi bơm)' 원칙이 베트남에서 간과되기 쉬움.",
        "commonMistakes": [
            {
                "mistake": "Epoxy를 '접착제(keo dán)'로 단순화",
                "correction": "Nhựa epoxy가 정확한 전문 용어",
                "explanation": "일반 접착제와 구조용 에폭시는 성능 차이 큼"
            },
            {
                "mistake": "'주입'을 Đổ (붓다)로 오역",
                "correction": "Bơm (펌프로 주입)이 정확",
                "explanation": "압력 주입과 단순 붓기는 공법이 다름"
            },
            {
                "mistake": "주입 압력을 명시하지 않음",
                "correction": "'0.5MPa로 주입' 등 수치 포함 통역",
                "explanation": "압력 과다 시 2차 균열 발생 위험"
            }
        ],
        "examples": [
            {
                "ko": "균열 폭 0.3mm 이상은 에폭시 주입으로 보수합니다.",
                "vi": "Vết nứt rộng từ 0.3mm trở lên được sửa chữa bằng bơm nhựa epoxy.",
                "situation": "formal"
            },
            {
                "ko": "주입 전에 균열 부위를 완전히 건조시키세요.",
                "vi": "Làm khô hoàn toàn vị trí vết nứt trước khi bơm.",
                "situation": "onsite"
            },
            {
                "ko": "에폭시 다 굳으면 물 안 새요.",
                "vi": "Khi nhựa epoxy đóng rắn hết thì không thấm nước nữa.",
                "situation": "informal"
            }
        ],
        "relatedTerms": ["균열보수", "구조보강", "방수공사", "탄소섬유보강"]
    },
    {
        "slug": "리모델링-cải-tạo",
        "korean": "리모델링",
        "vietnamese": "Cải tạo",
        "hanja": None,
        "hanjaReading": None,
        "pronunciation": "까이 따오",
        "meaningKo": "기존 건축물의 기능과 성능을 개선하기 위해 내·외부를 전면 개조하는 작업. 통역 시 '대수선(sửa chữa lớn)'과 구분 - 리모델링은 기능 변경 포함. 베트남 현장에서는 '용도 변경 허가(giấy phép thay đổi công năng sử dụng)' 절차 설명 필수. '인테리어 리모델링'과 '구조 리모델링' 구분도 중요.",
        "meaningVi": "Công việc cải tạo toàn diện nội ngoại thất để cải thiện chức năng và hiệu suất của công trình hiện có. Có thể bao gồm thay đổi công năng sử dụng, nâng cấp hệ thống kỹ thuật (điện, nước, điều hòa), và cải tạo kết cấu. Khác với sửa chữa thông thường, cải tạo thường yêu cầu giấy phép xây dựng.",
        "context": "노후 건물 개선, 상업 공간 전환, 주거 환경 개선",
        "culturalNote": "한국은 '15년 이상 아파트 리모델링' 법적 기준이 명확하나, 베트남은 개별 판단. 통역사는 한국의 '세대별 동의율(tỷ lệ đồng ý của hộ dân)' 요구 사항을 설명하여 절차 이해 도와야 함. 또한 '수직 증축(tăng tầng theo chiều dọc)' 개념이 베트남에서 덜 일반적.",
        "commonMistakes": [
            {
                "mistake": "Remodeling을 '수리(sửa chữa)'로만 번역",
                "correction": "Cải tạo가 정확 (수리는 부분 보수)",
                "explanation": "리모델링은 전면 개조, 수리는 국부 보수"
            },
            {
                "mistake": "'리모델링'을 Tân trang으로 표현",
                "correction": "Tân trang은 외관 개선, Cải tạo는 기능 개선",
                "explanation": "범위와 목적이 다름"
            },
            {
                "mistake": "허가 절차를 생략",
                "correction": "'Cần giấy phép xây dựng' 반드시 통역",
                "explanation": "무허가 리모델링 시 법적 제재"
            }
        ],
        "examples": [
            {
                "ko": "이 오피스 건물을 주거용으로 리모델링할 계획입니다.",
                "vi": "Chúng tôi dự định cải tạo tòa nhà văn phòng này thành nhà ở.",
                "situation": "formal"
            },
            {
                "ko": "구조 보강 먼저 하고 리모델링 들어갑니다.",
                "vi": "Gia cố kết cấu trước, sau đó mới bắt đầu cải tạo.",
                "situation": "onsite"
            },
            {
                "ko": "리모델링하면 집 새것처럼 돼요.",
                "vi": "Cải tạo xong thì nhà như mới luôn.",
                "situation": "informal"
            }
        ],
        "relatedTerms": ["증축", "구조보강", "용도변경", "대수선"]
    },
    {
        "slug": "증축-tăng-diện-tích-xây-dựng",
        "korean": "증축",
        "vietnamese": "Tăng diện tích xây dựng",
        "hanja": "增築",
        "hanjaReading": "增(더할 증) + 築(쌓을 축)",
        "pronunciation": "땅 지엔 띡 싸이 증",
        "meaningKo": "기존 건축물에 바닥 면적이나 층수를 추가하는 행위. 통역 시 '수평 증축(mở rộng theo chiều ngang)'과 '수직 증축(tăng tầng)' 구분 필수. 베트남 현장에서는 '건폐율(tỷ lệ xây dựng)' 제한 설명 필요. 구조 안전 검토 없는 증축의 위험성을 강조해야 함.",
        "meaningVi": "Hành vi tăng thêm diện tích sàn hoặc số tầng cho công trình hiện có. Bao gồm mở rộng theo chiều ngang (tăng diện tích mặt bằng) hoặc tăng tầng theo chiều dọc. Mọi công trình tăng diện tích đều phải được kiểm định kết cấu và có giấy phép xây dựng.",
        "context": "주택 확장, 상업 시설 확대, 공간 부족 해결",
        "culturalNote": "한국은 증축 전 '구조 안전 진단' 필수이나, 베트남은 소규모 증축에 대해 관대한 편. 통역사는 '불법 증축(xây dựng không phép)' 리스크를 설명하여 법규 준수 유도 필요. 또한 한국의 '일조권(quyền ánh sáng mặt trời)' 개념이 베트남에서 생소함.",
        "commonMistakes": [
            {
                "mistake": "증축을 단순히 Xây thêm으로만 표현",
                "correction": "Tăng diện tích xây dựng이 법적 용어",
                "explanation": "행정 문서에서는 정확한 용어 사용 필수"
            },
            {
                "mistake": "'증축'과 '개축'을 혼동",
                "correction": "증축은 면적 증가, 개축(cải tạo lại)은 재건축",
                "explanation": "법적 정의가 다름"
            },
            {
                "mistake": "수평/수직 증축 구분 안 함",
                "correction": "'Mở rộng ngang' vs 'Tăng tầng dọc' 명시",
                "explanation": "공법과 비용이 크게 다름"
            }
        ],
        "examples": [
            {
                "ko": "기존 건물 옥상에 1개 층을 수직 증축합니다.",
                "vi": "Tăng 1 tầng theo chiều dọc trên mái nhà hiện có.",
                "situation": "formal"
            },
            {
                "ko": "증축 전에 구조 안전 진단부터 받으세요.",
                "vi": "Trước khi tăng diện tích, phải kiểm định an toàn kết cấu trước.",
                "situation": "onsite"
            },
            {
                "ko": "허가 없이 증축하면 나중에 문제 돼요.",
                "vi": "Tăng diện tích không phép thì sau này có vấn đề đó.",
                "situation": "informal"
            }
        ],
        "relatedTerms": ["리모델링", "구조보강", "건축허가", "용도변경"]
    },
    {
        "slug": "용도변경-thay-đổi-công-năng-sử-dụng",
        "korean": "용도변경",
        "vietnamese": "Thay đổi công năng sử dụng",
        "hanja": "用途變更",
        "hanjaReading": "用(쓸 용) + 途(길 도) + 變(변할 변) + 更(고칠 경)",
        "pronunciation": "타이 도이 꽁 낭 쓰 중",
        "meaningKo": "건축물의 사용 목적을 법적으로 변경하는 행위. 통역 시 '근린생활시설(cơ sở sinh hoạt cộng đồng)'과 '업무시설(cơ sở văn phòng)' 등 용도 분류 이해 필수. 베트남 현장에서는 '소방 설비 기준(tiêu chuẩn thiết bị phòng cháy)' 변경 사항 설명 필요. 허가 없는 용도 변경의 법적 결과 강조.",
        "meaningVi": "Hành vi thay đổi mục đích sử dụng của công trình theo quy định pháp luật. Ví dụ: nhà ở thành văn phòng, kho thành cửa hàng. Mỗi loại công năng sử dụng có yêu cầu riêng về kết cấu, phòng cháy chữa cháy, và đỗ xe. Thay đổi công năng mà không có giấy phép sẽ bị xử phạt hành chính.",
        "context": "리모델링, 상업 공간 전환, 부동산 개발",
        "culturalNote": "한국은 용도 변경 시 '주차 대수(số lượng chỗ đỗ xe)' 재계산 의무가 엄격하나, 베트남은 상대적으로 유연. 통역사는 한국의 '용도별 건축 기준(tiêu chuẩn xây dựng theo công năng)' 엄격성을 설명하여 인식 차이 메워야 함. 또한 '근린생활시설 1종·2종' 같은 세부 분류가 베트남에 없음.",
        "commonMistakes": [
            {
                "mistake": "용도를 단순히 Mục đích으로만 번역",
                "correction": "Công năng sử dụng이 법적 정확 용어",
                "explanation": "건축법에서는 Công năng sử dụng 사용"
            },
            {
                "mistake": "'변경'을 Đổi로만 표현",
                "correction": "Thay đổi가 공식 용어",
                "explanation": "행정 문서에서는 Thay đổi 사용"
            },
            {
                "mistake": "허가 절차를 강조하지 않음",
                "correction": "'Bắt buộc phải có giấy phép' 명확히 통역",
                "explanation": "무허가 변경 시 영업 중지 등 제재"
            }
        ],
        "examples": [
            {
                "ko": "주택을 사무실로 용도 변경하려면 소방 설비를 보강해야 합니다.",
                "vi": "Để thay đổi nhà ở thành văn phòng, phải tăng cường thiết bị phòng cháy.",
                "situation": "formal"
            },
            {
                "ko": "이 건물은 근린생활시설로 용도 변경 가능합니다.",
                "vi": "Tòa nhà này có thể thay đổi thành cơ sở sinh hoạt cộng đồng.",
                "situation": "onsite"
            },
            {
                "ko": "허가 없이 가게 차리면 나중에 단속 당해요.",
                "vi": "Mở cửa hàng không phép thì sau này bị kiểm tra đấy.",
                "situation": "informal"
            }
        ],
        "relatedTerms": ["리모델링", "건축허가", "증축", "소방설비"]
    },
    {
        "slug": "내진보강-gia-cố-chống-động-đất",
        "korean": "내진보강",
        "vietnamese": "Gia cố chống động đất",
        "hanja": "耐震補強",
        "hanjaReading": "耐(견딜 내) + 震(진동 진) + 補(기울 보) + 強(강할 강)",
        "pronunciation": "자 꼬 쫑 동 닷",
        "meaningKo": "지진에 대한 건축물의 저항 능력을 향상시키는 보강 작업. 통역 시 '내진 등급(cấp độ chống động đất)' 개념 설명 필수 - 한국은 내진설계 의무화. 베트남 현장에서는 '면진장치(thiết bị cách ly chấn động)' 공법이 생소할 수 있음. '기존 건물 내진 성능 평가' 절차도 통역 빈출.",
        "meaningVi": "Công việc tăng cường khả năng chống chịu động đất của công trình. Bao gồm các phương pháp như gia cố tường, cột, dầm bằng vật liệu composite hoặc thép, lắp đặt thiết bị cách ly chấn động (giảm chấn). Ở Việt Nam, yêu cầu chống động đất chủ yếu áp dụng cho công trình quan trọng và khu vực có nguy cơ cao.",
        "context": "노후 건물 보강, 학교·병원 안전 강화, 재난 대비",
        "culturalNote": "한국은 '포항 지진(2017)' 이후 내진 보강 의무화가 강화되었으나, 베트남은 지진 빈도가 낮아 인식 부족. 통역사는 '예방적 보강(gia cố phòng ngừa)'의 중요성을 문화적 맥락에서 설명 필요. 또한 한국의 '내진 1등급·2등급' 분류가 베트남에 없음.",
        "commonMistakes": [
            {
                "mistake": "내진을 단순히 Chống rung으로만 번역",
                "correction": "Chống động đất이 정확한 지진 대비 용어",
                "explanation": "Rung은 진동 일반, Động đất은 지진 특화"
            },
            {
                "mistake": "'보강'을 Tăng cường으로만 표현",
                "correction": "Gia cố chống động đất이 전문 용어",
                "explanation": "구조 보강 맥락에서는 Gia cố 사용"
            },
            {
                "mistake": "내진 등급을 설명 안 함",
                "correction": "'Cấp 1 (quan trọng), Cấp 2 (thông thường)' 구분",
                "explanation": "등급에 따라 보강 기준 다름"
            }
        ],
        "examples": [
            {
                "ko": "학교 건물은 내진 1등급으로 보강해야 합니다.",
                "vi": "Tòa nhà trường học phải gia cố theo cấp 1 chống động đất.",
                "situation": "formal"
            },
            {
                "ko": "기둥에 철판을 감아 내진 성능을 높입니다.",
                "vi": "Quấn thép tấm quanh cột để tăng khả năng chống động đất.",
                "situation": "onsite"
            },
            {
                "ko": "지진 나면 무너질 수 있어요. 보강해야 돼요.",
                "vi": "Động đất thì có thể sập đấy. Phải gia cố mới được.",
                "situation": "informal"
            }
        ],
        "relatedTerms": ["구조보강", "탄소섬유보강", "면진장치", "내진설계"]
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
    data = json.load(f)

# 기존 slug 목록 (중복 방지)
existing_slugs = {term["slug"] for term in data}

# 중복 제거하고 추가
added_count = 0
for term in new_terms:
    if term["slug"] not in existing_slugs:
        data.append(term)
        existing_slugs.add(term["slug"])
        added_count += 1
        print(f"✅ 추가: {term['korean']} ({term['slug']})")
    else:
        print(f"⚠️  중복: {term['korean']} ({term['slug']}) - 건너뜀")

# 저장
with open(file_path, "w", encoding="utf-8") as f:
    json.dump(data, f, ensure_ascii=False, indent=2)

print(f"\n{'='*60}")
print(f"✅ 완료: {added_count}개 용어 추가됨")
print(f"📊 총 용어 수: {len(data)}개")
print(f"📁 파일: {file_path}")
print(f"{'='*60}")
