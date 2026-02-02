#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
의료기기/의료기술 용어 추가 스크립트
Medical Devices/Technology Terms Addition Script
"""

import json
import os

# 파일 경로 설정
file_path = os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', 'data', 'terms', 'medical.json')

# 추가할 용어 데이터
new_terms = [
    {
        "slug": "phau-thuat-robot-y-te",
        "korean": "의료로봇수술",
        "vietnamese": "Phẫu thuật robot y tế",
        "hanja": "醫療robot手術",
        "hanjaReading": "醫(의원 의) + 療(고칠 료) + robot(외래어) + 手(손 수) + 術(재주 술)",
        "pronunciation": "의료로봇수술",
        "meaningKo": "로봇 시스템을 이용하여 집도의가 콘솔에서 조작하면서 수행하는 최소침습 수술 방식입니다. 통역 시 주의할 점은 베트남에서는 아직 도입 초기 단계이므로 '다빈치 수술'이라는 특정 브랜드명으로 오해받을 수 있습니다. 일반적인 로봇 수술 개념임을 명확히 하고, 베트남 환자들에게는 비용과 접근성 문제를 함께 설명해야 합니다. 수술의 정밀성과 회복 기간 단축 등 장점을 강조할 때는 양국의 의료 인프라 차이를 고려해야 합니다.",
        "meaningVi": "Phương pháp phẫu thuật xâm lấn tối thiểu được thực hiện bởi bác sĩ điều khiển hệ thống robot từ bàn điều khiển. Công nghệ này giúp tăng độ chính xác, giảm chấn thương mô và rút ngắn thời gian hồi phục sau phẫu thuật. Tại Việt Nam, công nghệ này đang trong giai đoạn đầu triển khai tại một số bệnh viện lớn.",
        "context": "현대 의료기술, 최소침습 수술, 첨단 의료기기 관련 통역 상황",
        "culturalNote": "한국은 로봇 수술이 상대적으로 보편화되어 있고 건강보험 적용 범위가 넓은 반면, 베트남은 아직 하노이, 호치민 등 대도시 일부 병원에서만 가능하며 비용이 매우 높습니다. 한국 환자들은 로봇 수술을 일반적인 선택지로 생각하지만, 베트남 환자들에게는 최신 기술이자 고비용 옵션으로 인식됩니다. 통역 시 이러한 접근성과 인식 차이를 고려해야 합니다.",
        "commonMistakes": [
            {
                "mistake": "'Da Vinci surgery'로만 번역",
                "correction": "'Phẫu thuật robot y tế' 사용",
                "explanation": "다빈치는 특정 브랜드명이므로 일반적인 로봇 수술 개념과 구분 필요"
            },
            {
                "mistake": "'Robot tự động phẫu thuật' (로봇이 자동으로 수술)",
                "correction": "'Phẫu thuật robot y tế do bác sĩ điều khiển'",
                "explanation": "로봇이 자동으로 수술하는 것이 아니라 의사가 조작하는 도구임을 명확히 해야 함"
            },
            {
                "mistake": "비용 설명 생략",
                "correction": "양국의 비용 및 보험 적용 차이 설명 포함",
                "explanation": "베트남에서는 고비용이므로 환자의 기대치 관리가 중요함"
            }
        ],
        "examples": [
            {
                "ko": "로봇 수술은 기존 복강경 수술보다 정밀도가 높고 회복이 빠릅니다",
                "vi": "Phẫu thuật robot có độ chính xác cao hơn phẫu thuật nội soi thông thường và thời gian hồi phục nhanh hơn",
                "situation": "formal"
            },
            {
                "ko": "의료로봇수술 비용은 일반 수술보다 2-3배 높지만 건강보험 적용이 가능합니다",
                "vi": "Chi phí phẫu thuật robot cao gấp 2-3 lần so với phẫu thuật thông thường nhưng có thể được bảo hiểm y tế hỗ trợ",
                "situation": "formal"
            },
            {
                "ko": "저희 병원은 최신 의료로봇 시스템을 도입했습니다",
                "vi": "Bệnh viện chúng tôi đã đầu tư hệ thống robot y tế hiện đại nhất",
                "situation": "formal"
            }
        ],
        "relatedTerms": ["최소침습수술", "복강경수술", "내시경수술", "원격수술"]
    },
    {
        "slug": "vat-lieu-cay-ghep-in-3d",
        "korean": "3D프린팅보형물",
        "vietnamese": "Vật liệu cấy ghép in 3D",
        "hanja": None,
        "hanjaReading": None,
        "pronunciation": "쓰리디 프린팅 보형물",
        "meaningKo": "3D 프린팅 기술을 이용하여 환자 맞춤형으로 제작한 인공 삽입물 또는 보철물입니다. 통역 시 주의할 점은 '보형물'이라는 용어가 한국에서는 의료용 임플란트 전반을 가리키지만, 베트남어로는 미용 목적과 의료 목적을 명확히 구분해야 합니다. 또한 3D 프린팅 기술의 정밀도와 생체적합성에 대한 설명이 필요하며, 베트남에서는 아직 연구 단계이거나 제한적으로만 사용되므로 가용성에 대한 현실적인 기대치를 제시해야 합니다.",
        "meaningVi": "Vật liệu cấy ghép hoặc bộ phận nhân tạo được sản xuất theo kích thước và hình dạng riêng của từng bệnh nhân bằng công nghệ in 3D. Công nghệ này cho phép tạo ra các sản phẩm y tế chính xác cao, tương thích sinh học tốt và phù hợp hoàn hảo với cơ thể người nhận.",
        "context": "정형외과, 성형외과, 치과, 재건 수술 관련 통역 상황",
        "culturalNote": "한국은 3D 프린팅 의료기기 연구개발이 활발하고 일부 제품은 임상에서 사용되고 있지만, 베트남은 아직 대부분 연구 단계이거나 외국에서 수입해야 합니다. 한국 환자들은 맞춤형 의료기기에 대한 인식이 높지만, 베트남에서는 비용과 접근성 문제로 일반적인 선택지가 아닙니다. 통역 시 기술의 가능성과 함께 현실적인 제약사항도 함께 전달해야 합니다.",
        "commonMistakes": [
            {
                "mistake": "'Chất làm đầy in 3D' (3D 프린팅 충전재)",
                "correction": "'Vật liệu cấy ghép in 3D'",
                "explanation": "보형물은 단순 충전재가 아니라 구조적 지지 기능을 하는 임플란트임"
            },
            {
                "mistake": "미용 목적 보형물과 구분 없이 번역",
                "correction": "'Vật liệu cấy ghép y tế' 명시",
                "explanation": "의료 목적임을 명확히 하여 미용 성형과 혼동 방지"
            },
            {
                "mistake": "'In 3D' 용어만 강조하고 맞춤형 특성 생략",
                "correction": "'In 3D theo kích thước riêng của bệnh nhân'",
                "explanation": "환자 맞춤형이라는 핵심 장점을 반드시 포함해야 함"
            }
        ],
        "examples": [
            {
                "ko": "3D프린팅 기술로 환자의 두개골 형태에 맞춘 보형물을 제작했습니다",
                "vi": "Chúng tôi đã chế tạo vật liệu cấy ghép phù hợp với hình dạng hộp sọ của bệnh nhân bằng công nghệ in 3D",
                "situation": "formal"
            },
            {
                "ko": "3D프린팅보형물은 기존 제품보다 생체적합성이 우수합니다",
                "vi": "Vật liệu cấy ghép in 3D có tính tương thích sinh học tốt hơn so với sản phẩm truyền thống",
                "situation": "formal"
            },
            {
                "ko": "환자 맞춤형 3D 보형물 제작에는 약 2주가 소요됩니다",
                "vi": "Quá trình sản xuất vật liệu cấy ghép 3D theo yêu cầu riêng của bệnh nhân mất khoảng 2 tuần",
                "situation": "onsite"
            }
        ],
        "relatedTerms": ["인공관절", "생체재료", "맞춤형의료", "재건수술"]
    },
    {
        "slug": "thiet-bi-y-te-deo-duoc",
        "korean": "웨어러블의료기기",
        "vietnamese": "Thiết bị y tế đeo được",
        "hanja": None,
        "hanjaReading": None,
        "pronunciation": "웨어러블 의료기기",
        "meaningKo": "신체에 착용하여 건강 상태를 지속적으로 모니터링하거나 치료를 보조하는 휴대형 의료기기입니다. 통역 시 주의할 점은 단순 건강관리 기기(fitness tracker)와 의료기기로 인증받은 제품을 명확히 구분해야 한다는 것입니다. 한국에서는 식약처 인증을 받은 의료기기와 일반 웰니스 기기의 차이가 분명하지만, 베트남에서는 이러한 구분이 덜 엄격할 수 있습니다. 통역 시 의료적 목적과 데이터의 신뢰성, 개인정보 보호 문제도 함께 설명해야 합니다.",
        "meaningVi": "Thiết bị y tế di động được đeo trên cơ thể để theo dõi liên tục tình trạng sức khỏe hoặc hỗ trợ điều trị. Bao gồm đồng hồ thông minh y tế, máy đo đường huyết liên tục, thiết bị theo dõi nhịp tim và các sản phẩm được cấp phép y tế chính thức, khác biệt với các thiết bị theo dõi sức khỏe thông thường.",
        "context": "디지털헬스케어, 만성질환 관리, 원격의료 관련 통역 상황",
        "culturalNote": "한국은 웨어러블 의료기기 시장이 빠르게 성장하고 있으며 건강보험 적용도 확대되는 추세입니다. 반면 베트남은 아직 일반 스마트워치나 피트니스 트래커가 주를 이루며, 의료기기로 인증받은 제품의 보급률이 낮습니다. 한국 환자들은 데이터 기반 건강관리에 익숙하지만, 베트남에서는 개인정보 보호와 데이터 정확성에 대한 우려가 더 클 수 있습니다.",
        "commonMistakes": [
            {
                "mistake": "'Đồng hồ thông minh' (스마트워치)로만 번역",
                "correction": "'Thiết bị y tế đeo được được cấp phép'",
                "explanation": "일반 스마트워치와 의료기기 인증 제품을 구분해야 함"
            },
            {
                "mistake": "'Máy theo dõi sức khỏe' (건강 추적기)",
                "correction": "'Thiết bị y tế đeo được' 또는 'Thiết bị y tế mang trên người'",
                "explanation": "의료 목적의 전문 기기임을 명확히 해야 함"
            },
            {
                "mistake": "의료기기 인증 여부 설명 생략",
                "correction": "'Được Bộ Y tế/FDA phê duyệt' 등 인증 정보 포함",
                "explanation": "의료 목적 사용을 위해서는 정식 인증이 필수임을 강조해야 함"
            }
        ],
        "examples": [
            {
                "ko": "웨어러블 심전도 측정기로 24시간 부정맥을 모니터링할 수 있습니다",
                "vi": "Có thể theo dõi rối loạn nhịp tim 24 giờ bằng máy đo điện tim đeo được",
                "situation": "formal"
            },
            {
                "ko": "당뇨 환자를 위한 웨어러블 혈당 측정기가 건강보험 적용 대상입니다",
                "vi": "Thiết bị đo đường huyết đeo được dành cho bệnh nhân tiểu đường đã được bảo hiểm y tế chi trả",
                "situation": "formal"
            },
            {
                "ko": "이 웨어러블기기는 식약처 인증을 받은 의료기기입니다",
                "vi": "Thiết bị đeo này là thiết bị y tế được Cục Quản lý Thực phẩm và Dược phẩm phê duyệt",
                "situation": "onsite"
            }
        ],
        "relatedTerms": ["원격모니터링", "디지털헬스케어", "만성질환관리", "모바일헬스"]
    },
    {
        "slug": "benh-an-dien-tu",
        "korean": "전자의무기록",
        "vietnamese": "Bệnh án điện tử",
        "hanja": "電子醫務記錄",
        "hanjaReading": "電(번개 전) + 子(아들 자) + 醫(의원 의) + 務(힘쓸 무) + 記(기록할 기) + 錄(기록할 록)",
        "pronunciation": "전자의무기록",
        "meaningKo": "환자의 진료 정보를 전산 시스템에 기록하고 관리하는 디지털 의료기록 시스템입니다. 통역 시 주의할 점은 EMR(Electronic Medical Record)과 EHR(Electronic Health Record)의 차이를 구분해야 한다는 것입니다. 한국에서는 병원 간 정보 공유가 제한적이지만 점차 확대되는 추세이며, 베트남은 아직 표준화가 덜 되어 있습니다. 개인정보 보호법과 의료정보 보안 규정이 양국에서 다르므로, 정보 접근 권한과 보안 문제를 명확히 설명해야 합니다.",
        "meaningVi": "Hệ thống quản lý hồ sơ bệnh án bằng phương thức điện tử, lưu trữ thông tin khám chữa bệnh của người bệnh trên máy tính. Hệ thống này giúp tra cứu nhanh, chia sẻ thông tin giữa các bác sĩ và giảm sai sót so với hồ sơ giấy. Tại Việt Nam, việc triển khai bệnh án điện tử đang được đẩy mạnh tại các bệnh viện công lập và tư nhân.",
        "context": "병원 행정, 의료정보시스템, 디지털 헬스케어 관련 통역 상황",
        "culturalNote": "한국은 대부분의 병원이 전자의무기록을 사용하고 있으며, 정부 차원에서 의료정보 표준화를 추진 중입니다. 베트남도 전자의무기록 도입이 확대되고 있지만, 병원 간 시스템 호환성이 낮고 종이 기록을 병행하는 경우가 많습니다. 한국 환자들은 병원 간 기록 공유를 기대하지만, 베트남에서는 환자가 직접 기록을 옮기는 경우가 일반적입니다. 또한 개인정보 보호에 대한 인식 차이도 존재합니다.",
        "commonMistakes": [
            {
                "mistake": "'Hồ sơ y tế điện tử'와 'Bệnh án điện tử' 혼용",
                "correction": "병원 내 기록은 'Bệnh án điện tử', 통합 건강기록은 'Hồ sơ sức khỏe điện tử'",
                "explanation": "EMR(의무기록)과 EHR(건강기록)은 범위가 다름"
            },
            {
                "mistake": "'Sổ khám bệnh điện tử' (전자 진료수첩)",
                "correction": "'Bệnh án điện tử' 또는 'Hệ thống quản lý bệnh án điện tử'",
                "explanation": "단순 수첩이 아니라 통합 관리 시스템임을 명확히 해야 함"
            },
            {
                "mistake": "보안 및 개인정보 보호 규정 설명 생략",
                "correction": "접근 권한, 암호화, 법적 보호 조치 설명 포함",
                "explanation": "의료정보는 민감 정보이므로 보안 정책을 반드시 설명해야 함"
            }
        ],
        "examples": [
            {
                "ko": "전자의무기록 시스템 덕분에 과거 진료 이력을 즉시 확인할 수 있습니다",
                "vi": "Nhờ hệ thống bệnh án điện tử, chúng tôi có thể tra cứu ngay lịch sử khám chữa bệnh trước đây",
                "situation": "formal"
            },
            {
                "ko": "타 병원 전자의무기록은 환자 동의 후 열람 가능합니다",
                "vi": "Bệnh án điện tử từ bệnh viện khác chỉ có thể xem được sau khi bệnh nhân đồng ý",
                "situation": "formal"
            },
            {
                "ko": "전자의무기록은 암호화되어 안전하게 보관됩니다",
                "vi": "Bệnh án điện tử được mã hóa và lưu trữ an toàn",
                "situation": "onsite"
            }
        ],
        "relatedTerms": ["의료정보시스템", "개인건강기록", "원격진료", "디지털헬스"]
    },
    {
        "slug": "giam-sat-tu-xa",
        "korean": "원격모니터링",
        "vietnamese": "Giám sát từ xa",
        "hanja": "遠隔monitoring",
        "hanjaReading": "遠(멀 원) + 隔(사이 격) + monitoring(외래어)",
        "pronunciation": "원격모니터링",
        "meaningKo": "환자가 병원 밖에 있을 때도 의료진이 환자의 건강 상태를 실시간으로 확인하고 관리하는 의료 서비스입니다. 통역 시 주의할 점은 원격진료(telemedicine)와 원격모니터링의 차이를 명확히 구분해야 한다는 것입니다. 원격모니터링은 진단이나 처방보다는 지속적인 건강 상태 추적에 초점을 둡니다. 한국에서는 만성질환자 관리 목적으로 점차 확대되고 있으나 법적 제약이 있으며, 베트남은 인프라 한계로 대도시 중심으로만 가능합니다. 통역 시 서비스 범위와 한계를 분명히 해야 합니다.",
        "meaningVi": "Dịch vụ y tế cho phép đội ngũ y tế theo dõi tình trạng sức khỏe của bệnh nhân theo thời gian thực ngay cả khi bệnh nhân ở ngoài bệnh viện. Thường sử dụng các thiết bị đeo hoặc ứng dụng di động để thu thập dữ liệu sinh hiệu như nhịp tim, huyết áp, đường huyết và gửi về trung tâm y tế để bác sĩ phân tích.",
        "context": "만성질환 관리, 원격의료, 재택치료 관련 통역 상황",
        "culturalNote": "한국은 COVID-19 이후 원격모니터링이 확대되었으나 여전히 의료법상 제약이 많습니다. 건강보험 적용도 일부 만성질환에 한정됩니다. 베트남은 원격의료 인프라가 부족하고 대부분 민간 서비스로 제공되며, 농촌 지역은 인터넷 접속 문제로 이용이 어렵습니다. 한국 환자들은 정기적인 데이터 전송에 익숙하지만, 베트남 환자들은 직접 병원 방문을 선호하는 경향이 있습니다.",
        "commonMistakes": [
            {
                "mistake": "'Khám bệnh từ xa' (원격진료)",
                "correction": "'Giám sát từ xa' 또는 'Theo dõi sức khỏe từ xa'",
                "explanation": "원격진료(진단·처방)와 원격모니터링(관찰·추적)은 다른 개념"
            },
            {
                "mistake": "'Chăm sóc từ xa' (원격 돌봄)",
                "correction": "'Giám sát tình trạng sức khỏe từ xa'",
                "explanation": "단순 돌봄이 아니라 의료 데이터 기반 모니터링임"
            },
            {
                "mistake": "실시간 데이터 전송 방식 설명 생략",
                "correction": "'Truyền dữ liệu theo thời gian thực' 명시",
                "explanation": "실시간성이 핵심 특징이므로 반드시 강조해야 함"
            }
        ],
        "examples": [
            {
                "ko": "심부전 환자의 체중과 혈압을 원격모니터링으로 매일 확인합니다",
                "vi": "Chúng tôi theo dõi cân nặng và huyết áp của bệnh nhân suy tim hàng ngày qua hệ thống giám sát từ xa",
                "situation": "formal"
            },
            {
                "ko": "원격모니터링 덕분에 응급 상황을 조기에 발견할 수 있었습니다",
                "vi": "Nhờ hệ thống giám sát từ xa, chúng tôi đã phát hiện sớm tình trạng cấp cứu",
                "situation": "formal"
            },
            {
                "ko": "웨어러블 기기로 측정한 데이터가 자동으로 병원에 전송됩니다",
                "vi": "Dữ liệu đo từ thiết bị đeo được tự động gửi về bệnh viện",
                "situation": "onsite"
            }
        ],
        "relatedTerms": ["원격진료", "웨어러블의료기기", "만성질환관리", "디지털헬스케어"]
    },
    {
        "slug": "khop-nhan-tao",
        "korean": "인공관절",
        "vietnamese": "Khớp nhân tạo",
        "hanja": "人工關節",
        "hanjaReading": "人(사람 인) + 工(장인 공) + 關(관계할 관) + 節(마디 절)",
        "pronunciation": "인공관절",
        "meaningKo": "손상되거나 퇴행성 변화로 기능을 상실한 관절을 대체하기 위해 금속, 세라믹, 플라스틱 등으로 만든 인공 관절입니다. 통역 시 주의할 점은 부위별로 용어가 다르다는 것입니다(고관절, 슬관절, 견관절 등). 한국에서는 인공관절 수술이 매우 일반화되어 있고 건강보험 적용으로 비용 부담이 크지 않지만, 베트남에서는 여전히 고비용 수술로 인식되며 수술 후 재활 인프라도 차이가 있습니다. 통역 시 수술 후 관리와 재활 계획도 함께 설명해야 합니다.",
        "meaningVi": "Khớp nhân tạo được làm từ kim loại, gốm sứ hoặc nhựa y tế để thay thế khớp tự nhiên bị tổn thương hoặc thoái hóa. Phẫu thuật thay khớp nhân tạo phổ biến nhất là khớp háng (hông), khớp gối, khớp vai. Sau phẫu thuật, bệnh nhân cần tuân thủ chương trình phục hồi chức năng để đạt kết quả tốt nhất.",
        "context": "정형외과, 재활의학, 노인 의료 관련 통역 상황",
        "culturalNote": "한국은 고령화로 인공관절 수술이 매우 흔하며, 70대 이상 환자에게도 적극 권장됩니다. 건강보험 적용으로 본인 부담금이 낮고, 재활 프로그램도 체계적입니다. 베트남은 아직 인공관절 수술이 상대적으로 덜 보편화되어 있고 비용이 높으며, 수술 후 물리치료 접근성도 떨어집니다. 한국 의료진은 적극적으로 수술을 권하지만, 베트남 환자들은 경제적 부담과 수술 부담감으로 보수적인 경우가 많습니다.",
        "commonMistakes": [
            {
                "mistake": "'Khớp giả' (가짜 관절)",
                "correction": "'Khớp nhân tạo' 또는 'Khớp thay thế'",
                "explanation": "'giả'는 부정적 뉘앙스가 있으므로 'nhân tạo' 사용 권장"
            },
            {
                "mistake": "부위 구분 없이 일반적으로만 설명",
                "correction": "'Khớp gối nhân tạo', 'Khớp háng nhân tạo' 등 부위 명시",
                "explanation": "관절 부위에 따라 수술법과 예후가 다르므로 구분 필수"
            },
            {
                "mistake": "재료(금속, 세라믹, 플라스틱) 설명 생략",
                "correction": "사용 재료와 내구성 정보 포함",
                "explanation": "환자들이 재료와 수명에 대해 궁금해하므로 설명 필요"
            }
        ],
        "examples": [
            {
                "ko": "인공관절 수술 후 정상적인 보행이 가능해집니다",
                "vi": "Sau phẫu thuật thay khớp nhân tạo, bệnh nhân có thể đi lại bình thường",
                "situation": "formal"
            },
            {
                "ko": "인공관절의 수명은 평균 15-20년입니다",
                "vi": "Tuổi thọ trung bình của khớp nhân tạo là 15-20 năm",
                "situation": "formal"
            },
            {
                "ko": "무릎 인공관절 수술은 건강보험 적용이 됩니다",
                "vi": "Phẫu thuật thay khớp gối nhân tạo được bảo hiểm y tế chi trả",
                "situation": "onsite"
            }
        ],
        "relatedTerms": ["관절염", "퇴행성관절염", "관절치환술", "재활치료"]
    },
    {
        "slug": "may-tao-nhip-tim",
        "korean": "심장박동기",
        "vietnamese": "Máy tạo nhịp tim",
        "hanja": "心臟搏動器",
        "hanjaReading": "心(마음 심) + 臟(장기 장) + 搏(칠 박) + 動(움직일 동) + 器(그릇 기)",
        "pronunciation": "심장박동기",
        "meaningKo": "심장의 전기 신호에 이상이 생겨 박동이 불규칙하거나 느려질 때, 정상적인 심장 박동을 유지하도록 전기 자극을 주는 이식형 의료기기입니다. 통역 시 주의할 점은 '페이스메이커(pacemaker)'라는 외래어가 일반적으로 사용되지만, 환자 이해도를 위해 '심장박동기'라는 한국어 용어를 함께 사용해야 한다는 것입니다. 시술 후 MRI 촬영 제한, 전자기기 간섭 등 주의사항이 많으므로 통역 시 이러한 제약조건을 빠짐없이 전달해야 합니다.",
        "meaningVi": "Thiết bị y tế cấy ghép vào cơ thể để phát ra xung điện nhằm duy trì nhịp đập tim đều đặn khi tim có vấn đề về nhịp. Thường được chỉ định cho bệnh nhân nhịp tim chậm (nhịp tim chậm), block tim hoặc các rối loạn dẫn truyền điện tim khác. Sau khi cấy máy, bệnh nhân cần tuân thủ các hướng dẫn về tránh từ trường mạnh và kiểm tra định kỳ.",
        "context": "심장내과, 심장수술, 부정맥 관련 통역 상황",
        "culturalNote": "한국에서는 심장박동기 시술이 일반적이며 건강보험 적용으로 비용 부담이 적습니다. 시술 후 정기 점검 시스템도 잘 갖추어져 있습니다. 베트남에서도 대도시 병원에서는 가능하지만 비용이 높고, 시술 후 관리와 배터리 교체 등 장기 관리에 대한 인프라가 부족할 수 있습니다. 한국 환자들은 시술에 대한 두려움이 적지만, 베트nam 환자들은 '심장에 기계를 넣는다'는 것에 대한 심리적 부담이 클 수 있습니다.",
        "commonMistakes": [
            {
                "mistake": "'Máy hỗ trợ tim' (심장 보조 장치)",
                "correction": "'Máy tạo nhịp tim'",
                "explanation": "단순 보조가 아니라 박동을 직접 조절하는 기기임"
            },
            {
                "mistake": "'Pacemaker' 외래어만 사용",
                "correction": "'Máy tạo nhịp tim (pacemaker)' 병기",
                "explanation": "환자 이해를 위해 베트남어 설명과 외래어 병기 필요"
            },
            {
                "mistake": "MRI, 전자기기 간섭 주의사항 생략",
                "correction": "시술 후 제약사항 상세히 설명",
                "explanation": "환자 안전을 위해 생활 속 주의사항 반드시 전달해야 함"
            }
        ],
        "examples": [
            {
                "ko": "심장박동기를 이식하면 실신 증상이 개선됩니다",
                "vi": "Sau khi cấy máy tạo nhịp tim, triệu chứng ngất sẽ được cải thiện",
                "situation": "formal"
            },
            {
                "ko": "심장박동기 배터리는 보통 7-10년마다 교체가 필요합니다",
                "vi": "Pin của máy tạo nhịp tim thường cần thay sau mỗi 7-10 năm",
                "situation": "formal"
            },
            {
                "ko": "심장박동기를 한 환자는 MRI 촬영 전 반드시 의사와 상담해야 합니다",
                "vi": "Bệnh nhân có máy tạo nhịp tim phải tham khảo ý kiến bác sĩ trước khi chụp MRI",
                "situation": "onsite"
            }
        ],
        "relatedTerms": ["부정맥", "서맥", "제세동기", "심전도"]
    },
    {
        "slug": "dat-stent",
        "korean": "스텐트삽입",
        "vietnamese": "Đặt stent",
        "hanja": "stent揷入",
        "hanjaReading": "stent(외래어) + 揷(꽂을 삽) + 入(들 입)",
        "pronunciation": "스텐트 삽입",
        "meaningKo": "좁아지거나 막힌 혈관을 넓히고 유지하기 위해 그물망 형태의 금속 관을 삽입하는 시술입니다. 통역 시 주의할 점은 스텐트 종류(일반 금속 스텐트, 약물방출 스텐트)와 삽입 부위(관상동맥, 뇌혈관, 대동맥 등)에 따라 설명이 달라진다는 것입니다. 한국에서는 관상동맥 스텐트 시술이 매우 일반적이지만, 베트남에서는 시술 가능 병원이 제한적이고 비용도 높습니다. 시술 후 항혈소판제 복용 등 평생 관리가 필요하므로 이를 명확히 전달해야 합니다.",
        "meaningVi": "Thủ thuật đặt một ống lưới kim loại nhỏ vào động mạch bị hẹp hoặc tắc nghẽn để giữ cho lòng mạch luôn thông thoáng. Phổ biến nhất là đặt stent động mạch vành cho bệnh nhân nhồi máu cơ tim hoặc thiếu máu cơ tim. Sau thủ thuật, bệnh nhân cần uống thuốc chống đông máu suốt đời và tái khám định kỳ.",
        "context": "심장내과, 신경외과, 혈관외과 관련 통역 상황",
        "culturalNote": "한국은 스텐트 시술이 매우 보편화되어 있고 응급 상황에서 신속하게 시행됩니다. 건강보험 적용으로 비용 부담도 적습니다. 베트남에서도 대도시 병원에서는 가능하지만, 약물방출 스텐트는 비용이 높고 수입에 의존합니다. 한국 환자들은 스텐트 시술을 비교적 가벼운 시술로 여기지만, 베트남 환자들에게는 여전히 부담스러운 시술로 인식될 수 있습니다. 또한 시술 후 약물 복용 순응도도 문화적 차이가 있습니다.",
        "commonMistakes": [
            {
                "mistake": "'Lắp ống thông' (카테터 삽입)",
                "correction": "'Đặt stent' 또는 'Nong mạch và đặt stent'",
                "explanation": "카테터(ống thông)는 시술 도구이고 스텐트는 남아있는 장치임"
            },
            {
                "mistake": "일반 스텐트와 약물방출 스텐트 구분 없이 설명",
                "correction": "'Stent thường' vs 'Stent phủ thuốc' 구분",
                "explanation": "약물방출 스텐트는 비용이 더 높지만 재협착률이 낮음을 설명해야 함"
            },
            {
                "mistake": "시술 후 항혈소판제 복용 설명 생략",
                "correction": "'Uống thuốc chống đông suốt đời' 명시",
                "explanation": "약물 복용 중단 시 생명 위험이 있으므로 반드시 강조해야 함"
            }
        ],
        "examples": [
            {
                "ko": "관상동맥에 스텐트를 삽입하여 혈류를 회복시켰습니다",
                "vi": "Chúng tôi đã đặt stent vào động mạch vành để khôi phục lưu lượng máu",
                "situation": "formal"
            },
            {
                "ko": "약물방출 스텐트는 재협착 위험이 낮습니다",
                "vi": "Stent phủ thuốc có nguy cơ tái hẹp thấp hơn",
                "situation": "formal"
            },
            {
                "ko": "스텐트 삽입 후 최소 1년간 이중 항혈소판제를 복용해야 합니다",
                "vi": "Sau khi đặt stent, bệnh nhân phải uống thuốc chống kết tập tiểu cầu kép ít nhất 1 năm",
                "situation": "onsite"
            }
        ],
        "relatedTerms": ["관상동맥조영술", "혈관성형술", "심근경색", "항혈소판제"]
    },
    {
        "slug": "phau-thuat-noi-soi",
        "korean": "내시경수술",
        "vietnamese": "Phẫu thuật nội soi",
        "hanja": "內視鏡手術",
        "hanjaReading": "內(안 내) + 視(볼 시) + 鏡(거울 경) + 手(손 수) + 術(재주 술)",
        "pronunciation": "내시경수술",
        "meaningKo": "복부나 관절 등에 작은 구멍을 내고 카메라와 수술 기구를 삽입하여 수행하는 최소침습 수술 방법입니다. 통역 시 주의할 점은 진단 목적의 내시경 검사와 치료 목적의 내시경 수술을 명확히 구분해야 한다는 것입니다. 또한 복강경 수술(laparoscopy), 관절경 수술(arthroscopy) 등 부위에 따라 용어가 다릅니다. 한국에서는 맹장, 담낭, 자궁 수술 등에서 매우 일반적이지만, 베트남에서는 대도시 병원 중심으로만 가능하고 비용도 더 높습니다.",
        "meaningVi": "Phương pháp phẫu thuật xâm lấn tối thiểu bằng cách đưa camera và dụng cụ phẫu thuật qua các lỗ rạch nhỏ trên cơ thể. So với phẫu thuật mở truyền thống, phẫu thuật nội soi giúp giảm đau, ít sẹo, giảm nguy cơ nhiễm trùng và thời gian hồi phục nhanh hơn. Phổ biến trong phẫu thuật ổ bụng (nội soi ổ bụng), khớp (nội soi khớp) và các phẫu thuật phụ khoa.",
        "context": "외과, 부인과, 정형외과 관련 통역 상황",
        "culturalNote": "한국은 내시경 수술이 표준 치료법으로 자리 잡았으며, 환자들도 회복이 빠르고 흉터가 작다는 장점을 잘 알고 있습니다. 대부분의 병원에서 시행 가능하고 건강보험 적용도 됩니다. 베트남에서도 대도시 병원에서는 가능하지만, 외과의사의 숙련도에 따라 수술 결과가 달라질 수 있고, 일부 지방에서는 여전히 개복 수술이 일반적입니다. 환자들의 최소침습 수술에 대한 이해도도 차이가 있습니다.",
        "commonMistakes": [
            {
                "mistake": "'Nội soi' (내시경 검사)로만 번역",
                "correction": "'Phẫu thuật nội soi' 또는 'Phẫu thuật qua nội soi'",
                "explanation": "진단 목적 내시경과 수술을 명확히 구분해야 함"
            },
            {
                "mistake": "복강경, 관절경 등 부위별 구분 없이 일반화",
                "correction": "'Nội soi ổ bụng' (복강경), 'Nội soi khớp' (관절경) 등 명시",
                "explanation": "부위에 따라 수술법과 적응증이 다르므로 구분 필수"
            },
            {
                "mistake": "최소침습(xâm lấn tối thiểu) 특성 설명 생략",
                "correction": "작은 절개, 빠른 회복 등 장점 강조",
                "explanation": "환자들이 가장 궁금해하는 부분이므로 반드시 설명해야 함"
            }
        ],
        "examples": [
            {
                "ko": "내시경 수술로 맹장을 제거하여 흉터가 거의 남지 않았습니다",
                "vi": "Chúng tôi đã cắt ruột thừa bằng phẫu thuật nội soi nên hầu như không để lại sẹo",
                "situation": "formal"
            },
            {
                "ko": "내시경 수술 후 2-3일이면 퇴원이 가능합니다",
                "vi": "Sau phẫu thuật nội soi, bệnh nhân có thể xuất viện sau 2-3 ngày",
                "situation": "formal"
            },
            {
                "ko": "관절경으로 무릎 연골 손상을 치료했습니다",
                "vi": "Chúng tôi đã điều trị tổn thương sụn khớp gối bằng nội soi khớp",
                "situation": "onsite"
            }
        ],
        "relatedTerms": ["복강경수술", "관절경수술", "최소침습수술", "로봇수술"]
    },
    {
        "slug": "phau-thuat-laser",
        "korean": "레이저수술",
        "vietnamese": "Phẫu thuật laser",
        "hanja": "laser手術",
        "hanjaReading": "laser(외래어) + 手(손 수) + 術(재주 술)",
        "pronunciation": "레이저 수술",
        "meaningKo": "고에너지 광선(레이저)을 이용하여 조직을 절개하거나 응고, 제거하는 수술 방법입니다. 통역 시 주의할 점은 레이저 수술이 안과(시력교정), 피부과(점 제거, 제모), 비뇨기과(전립선), 산부인과 등 다양한 분야에서 사용되므로 적용 분야를 명확히 해야 한다는 것입니다. 특히 '라식/라섹' 같은 시력교정술은 미용 목적으로 오해받을 수 있으나 의료 시술임을 분명히 해야 합니다. 한국에서는 레이저 수술이 매우 보편화되어 있지만, 베트남에서는 장비 보유 병원이 제한적입니다.",
        "meaningVi": "Phương pháp phẫu thuật sử dụng chùm tia laser năng lượng cao để cắt, đông hoặc loại bỏ mô. Laser được ứng dụng rộng rãi trong nhiều lĩnh vực như nhãn khoa (phẫu thuật khúc xạ), da liễu (trị nám, tàn nhang, triệt lông), tiết niệu (điều trị u tuyến tiền liệt), phụ khoa và các chuyên khoa khác. Ưu điểm là ít chảy máu, độ chính xác cao và thời gian hồi phục nhanh.",
        "context": "안과, 피부과, 비뇨기과, 산부인과 관련 통역 상황",
        "culturalNote": "한국은 레이저 수술, 특히 시력교정술(라식/라섹)이 매우 대중화되어 있으며 젊은 층의 수술 비율이 높습니다. 피부과 레이저 시술도 일상적입니다. 베트남에서도 대도시 중심으로 확산되고 있지만, 장비 비용이 높아 수술 비용이 비싸고 의사의 숙련도에 따라 결과가 달라질 수 있습니다. 한국 환자들은 레이저 수술을 간단한 시술로 여기지만, 베트남 환자들은 여전히 신중하게 결정하는 경향이 있습니다.",
        "commonMistakes": [
            {
                "mistake": "'Phẫu thuật bằng ánh sáng' (빛을 이용한 수술)",
                "correction": "'Phẫu thuật laser'",
                "explanation": "일반 빛이 아니라 의료용 레이저임을 명확히 해야 함"
            },
            {
                "mistake": "시력교정술과 일반 레이저 수술 혼동",
                "correction": "'Phẫu thuật khúc xạ laser' (시력교정), 'Phẫu thuật laser da' (피부) 등 구분",
                "explanation": "레이저 종류와 목적이 다양하므로 분야별 구분 필수"
            },
            {
                "mistake": "레이저 종류(CO2, 엔디야그 등) 설명 생략",
                "correction": "사용되는 레이저 유형과 특성 설명 포함",
                "explanation": "레이저 종류에 따라 적응증과 효과가 다르므로 설명 필요"
            }
        ],
        "examples": [
            {
                "ko": "레이저 시력교정 수술로 안경 없이 생활할 수 있게 되었습니다",
                "vi": "Sau phẫu thuật khúc xạ laser, bệnh nhân có thể sinh hoạt mà không cần kính",
                "situation": "formal"
            },
            {
                "ko": "피부 점 제거를 위한 레이저 수술은 10분 정도 소요됩니다",
                "vi": "Phẫu thuật laser để loại bỏ nốt ruồi trên da mất khoảng 10 phút",
                "situation": "formal"
            },
            {
                "ko": "레이저로 전립선 비대증을 치료할 수 있습니다",
                "vi": "Có thể điều trị phì đại tuyến tiền liệt bằng laser",
                "situation": "onsite"
            }
        ],
        "relatedTerms": ["라식", "라섹", "시력교정술", "최소침습수술"]
    }
]

def main():
    # JSON 파일 읽기
    try:
        with open(file_path, 'r', encoding='utf-8') as f:
            data = json.load(f)
    except FileNotFoundError:
        print(f"❌ 파일을 찾을 수 없습니다: {file_path}")
        return
    except json.JSONDecodeError as e:
        print(f"❌ JSON 파싱 오류: {e}")
        return

    # data가 리스트인지 확인
    if not isinstance(data, list):
        print(f"❌ medical.json은 리스트 형식이어야 합니다. 현재 타입: {type(data)}")
        return

    # 기존 slug 목록 (중복 방지)
    existing_slugs = {term.get('slug') for term in data if isinstance(term, dict)}

    # 중복되지 않은 용어만 필터링
    terms_to_add = []
    duplicates = []

    for term in new_terms:
        if term['slug'] in existing_slugs:
            duplicates.append(term['slug'])
        else:
            terms_to_add.append(term)
            existing_slugs.add(term['slug'])

    if duplicates:
        print(f"⚠️  중복된 slug 발견 (추가 안 함): {', '.join(duplicates)}")

    if not terms_to_add:
        print("⚠️  추가할 새로운 용어가 없습니다 (모두 중복)")
        return

    # 용어 추가
    data.extend(terms_to_add)

    # JSON 파일 저장
    try:
        with open(file_path, 'w', encoding='utf-8') as f:
            json.dump(data, f, ensure_ascii=False, indent=2)

        print(f"✅ {len(terms_to_add)}개 용어가 medical.json에 추가되었습니다!")
        print(f"📊 총 용어 수: {len(data)}개")

        if duplicates:
            print(f"\n⚠️  중복으로 제외된 용어: {len(duplicates)}개")

        print("\n추가된 용어:")
        for term in terms_to_add:
            print(f"  - {term['korean']} ({term['vietnamese']})")

    except Exception as e:
        print(f"❌ 파일 저장 중 오류: {e}")

if __name__ == "__main__":
    main()
