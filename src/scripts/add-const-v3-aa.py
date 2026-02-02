#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
스마트건설/디지털 건설 용어 추가 스크립트
테마: 드론측량, 3D프린팅, IoT센서, AI안전, 모듈러, PC공법, 자동화, 원격모니터링, 디지털트윈, VR교육
"""

import json
import os

# 추가할 용어 데이터 (Tier S 기준)
data = [
    {
        "slug": "do-drone-measurement",
        "korean": "드론 측량",
        "vietnamese": "Đo đạc bằng drone",
        "hanja": "測量",
        "hanjaReading": "測(잴 측) + 量(헤아릴 량)",
        "pronunciation": "도 득 방 드론",
        "meaningKo": "무인항공기(드론)를 활용하여 건설 현장의 지형, 구조물을 촬영하고 3D 모델링하는 측량 기법. 전통적인 지상 측량 대비 시간과 비용을 절감하며, 위험 지역 접근이 용이합니다. 통역 시 'máy bay không người lái'와 'drone'을 혼용하되, 측량 전문성을 강조할 때는 'đo đạc địa hình bằng công nghệ drone'으로 구체화하세요. 베트남 건설 현장에서도 최근 급속히 도입되고 있어 최신 트렌드 용어로 주목받습니다.",
        "meaningVi": "Phương pháp đo đạc sử dụng thiết bị bay không người lái (drone) để chụp ảnh địa hình và tạo mô hình 3D công trình. Tiết kiệm thời gian, chi phí và an toàn hơn so với đo đạc truyền thống.",
        "context": "건설 현장 측량, 진척도 관리, 안전 점검, 지형 분석",
        "culturalNote": "한국은 국토교통부 드론 활용 가이드라인이 체계화되어 있으나, 베트남은 비행 허가 절차가 복잡할 수 있습니다. 통역 시 양국의 드론 규제 차이를 설명하고, 베트남 현장에서는 '허가 절차(thủ tục cấp phép bay)'를 반드시 언급해야 오해를 방지할 수 있습니다. 또한 한국은 '드론'이라는 외래어를 그대로 사용하지만, 베트남은 공식 문서에서는 'máy bay không người lái'를 선호합니다.",
        "commonMistakes": [
            {
                "mistake": "máy bay đo đạc",
                "correction": "đo đạc bằng drone / máy bay không người lái",
                "explanation": "'máy bay đo đạc'는 '측량용 비행기'로 오해될 수 있어, drone 또는 UAV 명시 필요"
            },
            {
                "mistake": "drone 찍기",
                "correction": "드론 측량 / 드론 촬영 측량",
                "explanation": "단순 촬영이 아닌 측량 목적임을 명확히 해야 전문성 전달"
            },
            {
                "mistake": "chụp ảnh drone",
                "correction": "đo đạc địa hình bằng drone",
                "explanation": "사진 촬영이 아닌 측량 데이터 수집 목적 강조 필요"
            }
        ],
        "examples": [
            {
                "ko": "이번 현장은 지형이 복잡해서 드론 측량으로 진행하겠습니다.",
                "vi": "Công trường lần này địa hình phức tạp nên chúng tôi sẽ tiến hành đo đạc bằng drone.",
                "situation": "formal"
            },
            {
                "ko": "드론 측량 데이터를 BIM 모델에 통합해주세요.",
                "vi": "Hãy tích hợp dữ liệu đo đạc drone vào mô hình BIM.",
                "situation": "onsite"
            },
            {
                "ko": "드론으로 주 1회 진척도 측량합니다.",
                "vi": "Mỗi tuần chúng tôi đo tiến độ một lần bằng drone.",
                "situation": "informal"
            }
        ],
        "relatedTerms": ["BIM", "3D 모델링", "지형 측량", "UAV", "디지털트윈"]
    },
    {
        "slug": "in-3d-xay-dung",
        "korean": "3D프린팅 건설",
        "vietnamese": "In 3D xây dựng",
        "hanja": None,
        "hanjaReading": None,
        "pronunciation": "인 3디 싸이 증",
        "meaningKo": "3D 프린터를 활용해 건축 구조물을 층층이 쌓아 올려 제작하는 건설 공법. 인건비 절감, 공기 단축, 복잡한 형상 구현이 가능하며, 친환경 자재 활용도 높습니다. 통역 시 '적층 제조(additive manufacturing)' 개념을 설명하고, 베트남 현장에서는 'công nghệ in 3D'만으로도 통하지만 전문 회의에서는 'xây dựng bằng công nghệ in 3D / in kết cấu 3D'로 구체화하세요. 한국은 시범 프로젝트 단계, 베트nam도 관심이 높아지는 추세입니다.",
        "meaningVi": "Công nghệ sử dụng máy in 3D để xây dựng kết cấu công trình bằng cách xếp chồng từng lớp vật liệu. Tiết kiệm nhân công, rút ngắn thời gian thi công và thân thiện môi trường.",
        "context": "신기술 건설, 시범 프로젝트, 주택 건설, 복잡한 형상 구조물",
        "culturalNote": "한국은 국토교통부 주도로 3D프린팅 건설 로드맵을 추진 중이며, 베트남은 아직 초기 단계이나 스타트업과 대학 연구소 중심으로 실험 프로젝트가 진행 중입니다. 통역 시 양국의 기술 성숙도 차이를 언급하고, 베트남 측에는 '시범 프로젝트(dự án thí điểm)' 개념을 강조해 현실적인 기대치를 형성하세요. 한국은 '3D프린팅'이라는 외래어를 그대로 사용하나, 베트남은 'in 3D' 또는 'công nghệ in ba chiều'로 표현합니다.",
        "commonMistakes": [
            {
                "mistake": "máy in nhà 3D",
                "correction": "xây dựng bằng công nghệ in 3D",
                "explanation": "'집 인쇄 기계'로 직역하면 오해 발생, 건설 공법임을 명확히 해야"
            },
            {
                "mistake": "3D프린터로 집 만들기",
                "correction": "3D프린팅 건설 / 3D프린팅 공법",
                "explanation": "구어체가 아닌 전문 용어로 표현 필요"
            },
            {
                "mistake": "in kết cấu",
                "correction": "xây dựng bằng công nghệ in 3D / in 3D kết cấu công trình",
                "explanation": "'구조 인쇄'만으로는 3D 기술임이 불명확, 기술명 명시 필요"
            }
        ],
        "examples": [
            {
                "ko": "이 시범 주택은 3D프린팅 건설로 2주 만에 완공했습니다.",
                "vi": "Ngôi nhà thí điểm này được hoàn thành trong 2 tuần bằng công nghệ in 3D xây dựng.",
                "situation": "formal"
            },
            {
                "ko": "3D프린팅으로 복잡한 곡선 외벽을 구현할 수 있어요.",
                "vi": "Có thể tạo tường cong phức tạp bằng công nghệ in 3D.",
                "situation": "onsite"
            },
            {
                "ko": "내년에 3D프린팅 건설 파일럿 프로젝트 시작합니다.",
                "vi": "Năm sau bắt đầu dự án thí điểm xây dựng in 3D.",
                "situation": "informal"
            }
        ],
        "relatedTerms": ["적층 제조", "신기술 공법", "친환경 건설", "모듈러 건설", "자동화"]
    },
    {
        "slug": "cam-bien-iot",
        "korean": "IoT 센서",
        "vietnamese": "Cảm biến IoT",
        "hanja": None,
        "hanjaReading": None,
        "pronunciation": "캄 비엔 아이오티",
        "meaningKo": "사물인터넷(Internet of Things) 기술 기반으로 건설 현장의 온도, 습도, 진동, 균열, 안전 상태 등을 실시간 수집·전송하는 센서. 데이터 기반 의사결정과 예측 유지보수가 가능합니다. 통역 시 'cảm biến thông minh'와 혼용되나, IoT는 네트워크 연결성을 강조하므로 'cảm biến kết nối IoT'로 구체화하세요. 베트남 현장에서는 '센서'를 'thiết bị cảm biến' 또는 'sensor'로도 부르므로 맥락에 맞게 선택해야 합니다.",
        "meaningVi": "Cảm biến dựa trên công nghệ Internet vạn vật (IoT) để thu thập và truyền dữ liệu thời gian thực về nhiệt độ, độ ẩm, rung động, vết nứt, tình trạng an toàn tại công trường.",
        "context": "스마트 건설, 안전 관리, 구조 모니터링, 예측 유지보수",
        "culturalNote": "한국은 스마트 건설 기술 로드맵에 IoT 센서 의무화 추진 중이며, 베트남은 대형 건설사 중심으로 도입이 시작되고 있습니다. 통역 시 한국의 '안전관리 시스템 통합' 사례를 설명하면 베트남 측 이해도가 높아집니다. 베트남은 'cảm biến thông minh(스마트 센서)'라는 표현도 널리 쓰이나, IoT는 클라우드 연결을 전제하므로 'kết nối đám mây' 개념을 함께 설명하세요.",
        "commonMistakes": [
            {
                "mistake": "sensor thông minh",
                "correction": "cảm biến IoT / cảm biến kết nối IoT",
                "explanation": "스마트 센서는 넓은 개념, IoT는 네트워크 연결성 강조 필요"
            },
            {
                "mistake": "아이오티 기계",
                "correction": "IoT 센서 / IoT 디바이스",
                "explanation": "'기계'는 모호한 표현, 센서 또는 디바이스로 명확히 해야"
            },
            {
                "mistake": "thiết bị đo",
                "correction": "cảm biến IoT / thiết bị cảm biến kết nối IoT",
                "explanation": "단순 측정 장비가 아닌 네트워크 연결 센서임을 명시 필요"
            }
        ],
        "examples": [
            {
                "ko": "현장 전역에 IoT 센서를 설치해 실시간 모니터링합니다.",
                "vi": "Lắp đặt cảm biến IoT khắp công trường để giám sát thời gian thực.",
                "situation": "formal"
            },
            {
                "ko": "IoT 센서가 균열을 감지하면 자동으로 알림이 옵니다.",
                "vi": "Khi cảm biến IoT phát hiện vết nứt sẽ tự động gửi thông báo.",
                "situation": "onsite"
            },
            {
                "ko": "이 센서 배터리 교체 주기는 6개월입니다.",
                "vi": "Chu kỳ thay pin cảm biến này là 6 tháng.",
                "situation": "informal"
            }
        ],
        "relatedTerms": ["스마트 건설", "원격 모니터링", "빅데이터", "클라우드", "예측 유지보수"]
    },
    {
        "slug": "quan-ly-an-toan-ai",
        "korean": "AI 안전 관리",
        "vietnamese": "Quản lý an toàn AI",
        "hanja": "安全管理",
        "hanjaReading": "安(편안할 안) + 全(온전할 전) + 管(대롱 관) + 理(다스릴 리)",
        "pronunciation": "꽌 리 안 토안 AI",
        "meaningKo": "인공지능(AI)을 활용해 건설 현장의 CCTV 영상을 분석하여 안전모 미착용, 위험 구역 진입, 낙하 위험 등을 자동 감지하고 경보하는 시스템. 사고 예방과 안전 관리 효율성을 극대화합니다. 통역 시 'AI 비전(AI vision)' 기술 기반임을 설명하고, 베트남 현장에서는 'hệ thống an toàn thông minh AI'로 표현하면 이해가 쉽습니다. 한국은 중대재해처벌법 시행 이후 도입이 급증하고 있으며, 베트남도 안전 규제 강화 추세입니다.",
        "meaningVi": "Hệ thống sử dụng trí tuệ nhân tạo (AI) để phân tích camera công trường, tự động phát hiện vi phạm an toàn như không đội mũ, vào khu vực nguy hiểm, nguy cơ rơi rớt và cảnh báo.",
        "context": "건설 안전, 사고 예방, CCTV 분석, 스마트 건설",
        "culturalNote": "한국은 중대재해처벌법으로 안전 관리 책임이 강화되어 AI 안전 시스템 도입이 의무화 추세이나, 베트남은 아직 권고 수준입니다. 통역 시 한국의 '법적 책임(trách nhiệm pháp lý)' 강조를 베트남 측에 설명하면 도입 필요성을 이해시킬 수 있습니다. 베트남은 'an toàn lao động(노동 안전)'이라는 표현을 선호하므로, 'quản lý an toàn lao động bằng AI'로 표현하는 것도 효과적입니다.",
        "commonMistakes": [
            {
                "mistake": "AI 카메라",
                "correction": "AI 안전 관리 시스템 / AI 기반 안전 모니터링",
                "explanation": "카메라는 수단일 뿐, 안전 관리 목적을 명확히 해야"
            },
            {
                "mistake": "camera thông minh",
                "correction": "hệ thống quản lý an toàn AI / giám sát an toàn bằng AI",
                "explanation": "스마트 카메라는 기능 설명 부족, AI 안전 시스템임을 명시 필요"
            },
            {
                "mistake": "AI 감시",
                "correction": "AI 안전 관리 / AI 기반 안전 모니터링",
                "explanation": "'감시'는 부정적 뉘앙스, '안전 관리'로 긍정적 표현 필요"
            }
        ],
        "examples": [
            {
                "ko": "AI 안전 관리 시스템이 안전모 미착용자를 실시간으로 감지합니다.",
                "vi": "Hệ thống quản lý an toàn AI phát hiện người không đội mũ bảo hộ theo thời gian thực.",
                "situation": "formal"
            },
            {
                "ko": "이 시스템은 위험 구역 진입 시 자동 경보를 울립니다.",
                "vi": "Hệ thống này tự động báo động khi có người vào khu vực nguy hiểm.",
                "situation": "onsite"
            },
            {
                "ko": "AI가 분석한 안전 위반 데이터를 주간 보고서로 받아요.",
                "vi": "Nhận báo cáo tuần về dữ liệu vi phạm an toàn do AI phân tích.",
                "situation": "informal"
            }
        ],
        "relatedTerms": ["CCTV", "안전모", "중대재해처벌법", "스마트 건설", "사고 예방"]
    },
    {
        "slug": "xay-dung-module",
        "korean": "모듈러 건설",
        "vietnamese": "Xây dựng module",
        "hanja": None,
        "hanjaReading": None,
        "pronunciation": "싸이 증 모듈",
        "meaningKo": "공장에서 사전 제작한 모듈 유닛을 현장에서 조립하는 건설 공법. 공기 단축(30~50%), 품질 향상, 현장 안전성 증대 효과가 있으며, 호텔, 기숙사, 병원 등에 주로 적용됩니다. 통역 시 'prefabricated construction(프리패브)'과 구분하여, 모듈러는 '독립적 기능 단위(đơn vị chức năng độc lập)'임을 강조하세요. 베트남에서는 'xây dựng lắp ghép'으로도 불리나, 모듈러는 공장 생산의 완성도가 더 높습니다.",
        "meaningVi": "Phương pháp xây dựng bằng cách lắp ráp các đơn vị module được sản xuất sẵn tại nhà máy trên công trường. Rút ngắn thời gian thi công 30-50%, nâng cao chất lượng và an toàn.",
        "context": "공장 제작, 현장 조립, 호텔/기숙사 건설, 공기 단축",
        "culturalNote": "한국은 모듈러 건축물 인증제도가 체계화되어 있고, 정부 발주 공공주택에 활발히 적용 중이나, 베트남은 아직 시범 프로젝트 단계입니다. 통역 시 한국의 '공장 품질 관리(kiểm soát chất lượng tại nhà máy)' 시스템을 설명하면 베트남 측 신뢰를 높일 수 있습니다. 베트남은 '조립식(lắp ghép)'이라는 표현도 쓰이나, 모듈러는 '독립 기능성'이 핵심이므로 'module có chức năng hoàn chỉnh'으로 구분하세요.",
        "commonMistakes": [
            {
                "mistake": "조립 건설",
                "correction": "모듈러 건설 / 모듈러 공법",
                "explanation": "조립은 수단, 모듈러는 공법 개념이므로 전문 용어 사용 필요"
            },
            {
                "mistake": "xây dựng lắp ráp",
                "correction": "xây dựng module / xây dựng theo công nghệ module",
                "explanation": "단순 조립이 아닌 모듈 단위 공법임을 명확히 해야"
            },
            {
                "mistake": "프리패브",
                "correction": "모듈러 건설 (또는 프리패브와 구분 설명)",
                "explanation": "프리패브는 부재 수준, 모듈러는 기능 단위이므로 구분 필요"
            }
        ],
        "examples": [
            {
                "ko": "이 호텔은 모듈러 건설로 6개월 만에 완공했습니다.",
                "vi": "Khách sạn này hoàn thành trong 6 tháng bằng công nghệ xây dựng module.",
                "situation": "formal"
            },
            {
                "ko": "공장에서 만든 모듈을 크레인으로 올려서 조립합니다.",
                "vi": "Dùng cần cẩu nâng module từ nhà máy lên và lắp ráp.",
                "situation": "onsite"
            },
            {
                "ko": "모듈러는 날씨 영향을 덜 받아서 좋아요.",
                "vi": "Module ít bị ảnh hưởng thời tiết nên tốt.",
                "situation": "informal"
            }
        ],
        "relatedTerms": ["프리캐스트", "공장 제작", "현장 조립", "공기 단축", "프리패브"]
    },
    {
        "slug": "cau-kien-duc-san-pc",
        "korean": "PC 공법",
        "vietnamese": "Cấu kiện đúc sẵn PC",
        "hanja": None,
        "hanjaReading": None,
        "pronunciation": "꺼우 끼엔 득 선 피씨",
        "meaningKo": "Precast Concrete(프리캐스트 콘크리트)의 약자로, 공장에서 콘크리트 부재를 미리 제작하여 현장에서 조립하는 공법. 품질 균일성, 공기 단축, 현장 폐기물 감소 효과가 있으며, 기둥, 보, 슬래브 등에 적용됩니다. 통역 시 베트남에서는 'bê tông đúc sẵn'으로 주로 표현하나, 전문 회의에서는 'PC(피씨)'라는 약어도 통용됩니다. 한국은 아파트 벽체, 계단에 널리 사용되며, 베트남은 교량, 공장 건물에 주로 적용됩니다.",
        "meaningVi": "Phương pháp sử dụng cấu kiện bê tông đúc sẵn tại nhà máy (Precast Concrete - PC) và lắp ráp tại công trường. Đảm bảo chất lượng đồng đều, rút ngắn thời gian và giảm chất thải hiện trường.",
        "context": "공장 제작, 현장 조립, 기둥/보/슬래브, 품질 관리",
        "culturalNote": "한국은 PC 공법이 공동주택 건설에 표준화되어 있고, KS 인증 제도가 엄격하나, 베트남은 주로 인프라와 산업 건축에 사용되며 품질 기준이 상대적으로 덜 체계적입니다. 통역 시 한국의 '공장 양생(dưỡng hộ tại nhà máy)' 시스템을 설명하면 품질 우위를 강조할 수 있습니다. 베트남은 'bê tông đúc sẵn'이라는 표현이 일반적이나, 전문가들은 'PC' 약어를 선호하므로 맥락에 맞게 선택하세요.",
        "commonMistakes": [
            {
                "mistake": "미리 만든 콘크리트",
                "correction": "PC 공법 / 프리캐스트 콘크리트 공법",
                "explanation": "구어체가 아닌 전문 용어로 표현 필요"
            },
            {
                "mistake": "bê tông làm sẵn",
                "correction": "cấu kiện đúc sẵn PC / bê tông đúc sẵn",
                "explanation": "'만들어진 콘크리트'는 부정확, '사전 제작 부재'임을 명시 필요"
            },
            {
                "mistake": "조립식 콘크리트",
                "correction": "PC 공법 / 프리캐스트 공법",
                "explanation": "조립은 시공 방법, PC는 공법 개념이므로 구분 필요"
            }
        ],
        "examples": [
            {
                "ko": "이번 현장은 기둥과 보를 PC 공법으로 시공합니다.",
                "vi": "Công trường này thi công cột và dầm bằng cấu kiện đúc sẵn PC.",
                "situation": "formal"
            },
            {
                "ko": "PC 부재는 공장에서 28일 양생 후 출하합니다.",
                "vi": "Cấu kiện PC được dưỡng hộ 28 ngày tại nhà máy rồi xuất xưởng.",
                "situation": "onsite"
            },
            {
                "ko": "PC로 하면 현장 콘크리트 타설보다 빨라요.",
                "vi": "Dùng PC nhanh hơn đổ bê tông tại chỗ.",
                "situation": "informal"
            }
        ],
        "relatedTerms": ["프리캐스트", "모듈러", "공장 제작", "현장 조립", "양생"]
    },
    {
        "slug": "tu-dong-hoa-xay-dung",
        "korean": "건설 자동화",
        "vietnamese": "Tự động hóa xây dựng",
        "hanja": "建設自動化",
        "hanjaReading": "建(지을 건) + 設(베풀 설) + 自(스스로 자) + 動(움직일 동) + 化(될 화)",
        "pronunciation": "뜨 동 호아 싸이 증",
        "meaningKo": "로봇, AI, IoT 등 첨단 기술을 활용해 건설 공정을 자동화하는 기술. 철근 결속, 용접, 도장, 자재 운반 등에 로봇을 투입하여 인건비 절감과 생산성 향상을 도모합니다. 통역 시 '무인화(vô nhân hóa)'와 구분하여, 자동화는 '사람 보조(hỗ trợ con người)' 개념임을 강조하세요. 한국은 건설 로봇 실증 단지를 운영 중이며, 베트남은 아직 초기 단계이나 관심이 높아지고 있습니다.",
        "meaningVi": "Công nghệ áp dụng robot, AI, IoT để tự động hóa quy trình xây dựng như buộc cốt thép, hàn, sơn, vận chuyển vật liệu. Giảm chi phí nhân công và nâng cao năng suất.",
        "context": "스마트 건설, 로봇 활용, 생산성 향상, 인력 부족 대응",
        "culturalNote": "한국은 건설업 고령화와 인력 부족으로 자동화 도입이 정부 정책으로 추진되고 있으나, 베트남은 인건비가 낮아 자동화 경제성이 낮은 편입니다. 통역 시 한국의 '안전성(an toàn)' 및 '품질 균일성(chất lượng đồng đều)' 장점을 강조하면 베트남 측 관심을 유도할 수 있습니다. 베트남은 'tự động hóa'라는 표현이 일반적이나, 'robot hóa'라는 표현도 쓰이므로 맥락에 맞게 선택하세요.",
        "commonMistakes": [
            {
                "mistake": "무인 건설",
                "correction": "건설 자동화 / 자동화 공법",
                "explanation": "무인은 극단적 표현, 자동화는 사람 보조 개념"
            },
            {
                "mistake": "robot xây dựng",
                "correction": "tự động hóa xây dựng / công nghệ tự động hóa trong xây dựng",
                "explanation": "로봇은 수단, 자동화가 목적이므로 개념 구분 필요"
            },
            {
                "mistake": "기계화",
                "correction": "자동화 / 건설 자동화",
                "explanation": "기계화는 단순 장비 도입, 자동화는 지능형 시스템"
            }
        ],
        "examples": [
            {
                "ko": "이 현장은 철근 결속 로봇으로 건설 자동화를 시범 도입했습니다.",
                "vi": "Công trường này thí điểm tự động hóa xây dựng bằng robot buộc cốt thép.",
                "situation": "formal"
            },
            {
                "ko": "자동화 장비로 작업 속도가 2배 빨라졌어요.",
                "vi": "Thiết bị tự động hóa giúp tăng tốc độ làm việc gấp đôi.",
                "situation": "onsite"
            },
            {
                "ko": "내년부터 용접 자동화 로봇 투입합니다.",
                "vi": "Năm sau triển khai robot tự động hóa hàn.",
                "situation": "informal"
            }
        ],
        "relatedTerms": ["로봇", "스마트 건설", "AI", "생산성", "무인화"]
    },
    {
        "slug": "giam-sat-tu-xa",
        "korean": "원격 모니터링",
        "vietnamese": "Giám sát từ xa",
        "hanja": "遠隔",
        "hanjaReading": "遠(멀 원) + 隔(사이뜰 격)",
        "pronunciation": "잠 삿 뜨 싸",
        "meaningKo": "IoT 센서, CCTV, 드론 등을 활용해 건설 현장을 원격에서 실시간으로 감시·관리하는 시스템. 진척도 확인, 안전 관리, 장비 가동 상태 점검 등을 사무실이나 모바일에서 수행할 수 있습니다. 통역 시 '실시간(thời gian thực)' 개념을 강조하고, 베트남 현장에서는 '클라우드 기반(dựa trên đám mây)' 설명을 추가하면 이해도가 높아집니다. 한국은 코로나19 이후 원격 관리 수요가 급증했으며, 베트남도 동남아 다국적 프로젝트에서 활용도가 증가하고 있습니다.",
        "meaningVi": "Hệ thống sử dụng cảm biến IoT, camera, drone để giám sát và quản lý công trường từ xa theo thời gian thực. Có thể kiểm tra tiến độ, an toàn, trạng thái thiết bị từ văn phòng hoặc di động.",
        "context": "스마트 건설, 현장 관리, 안전 점검, 진척도 관리",
        "culturalNote": "한국은 대형 건설사 중심으로 원격 모니터링 시스템이 표준화되어 있고, 정부도 '스마트 안전 관리' 지침을 권고하고 있으나, 베트남은 아직 초기 단계로 인터넷 인프라와 비용 문제가 장애 요인입니다. 통역 시 한국의 '모바일 앱 통합(tích hợp ứng dụng di động)' 사례를 소개하면 베트남 측 관심을 유도할 수 있습니다. 베트남은 'giám sát'이라는 표현이 일반적이나, 'theo dõi từ xa'라는 표현도 쓰이므로 맥락에 맞게 선택하세요.",
        "commonMistakes": [
            {
                "mistake": "원격 감시",
                "correction": "원격 모니터링 / 원격 관리",
                "explanation": "'감시'는 부정적 뉘앙스, '모니터링'이 중립적 전문 용어"
            },
            {
                "mistake": "xem từ xa",
                "correction": "giám sát từ xa / theo dõi từ xa",
                "explanation": "'보기'는 단순 관찰, 모니터링은 관리 목적 강조 필요"
            },
            {
                "mistake": "CCTV 보기",
                "correction": "원격 모니터링 / 실시간 원격 관리",
                "explanation": "CCTV는 수단, 모니터링 시스템 전체를 지칭해야"
            }
        ],
        "examples": [
            {
                "ko": "원격 모니터링 시스템으로 5개 현장을 동시에 관리합니다.",
                "vi": "Quản lý đồng thời 5 công trường bằng hệ thống giám sát từ xa.",
                "situation": "formal"
            },
            {
                "ko": "모바일 앱으로 현장 CCTV를 실시간으로 볼 수 있어요.",
                "vi": "Có thể xem camera công trường theo thời gian thực qua app di động.",
                "situation": "onsite"
            },
            {
                "ko": "원격으로 크레인 가동 상태 체크합니다.",
                "vi": "Kiểm tra trạng thái cần cẩu từ xa.",
                "situation": "informal"
            }
        ],
        "relatedTerms": ["IoT 센서", "CCTV", "클라우드", "스마트 건설", "모바일 앱"]
    },
    {
        "slug": "song-sinh-so-digital-twin",
        "korean": "디지털 트윈",
        "vietnamese": "Song sinh số (Digital Twin)",
        "hanja": None,
        "hanjaReading": None,
        "pronunciation": "송 신 쏘 (디지털 트윈)",
        "pronunciation": "송 신 쏘",
        "meaningKo": "건설 현장과 구조물을 가상 공간에 동일하게 재현한 디지털 모델. 실시간 센서 데이터를 반영하여 시뮬레이션, 예측 유지보수, 최적화가 가능합니다. 통역 시 'mô hình số kỹ thuật số'라는 직역보다 'song sinh số(디지털 쌍둥이)'라는 베트남어 신조어가 전문가들 사이에 널리 쓰이므로 이를 사용하세요. 한국은 스마트시티, 인프라 관리에 활발히 도입 중이며, 베트남은 연구 단계이나 관심이 높아지고 있습니다.",
        "meaningVi": "Mô hình kỹ thuật số tái tạo giống hệt công trường và công trình trong không gian ảo. Phản ánh dữ liệu cảm biến thời gian thực để mô phỏng, bảo trì dự đoán và tối ưu hóa.",
        "context": "스마트 건설, BIM, 시뮬레이션, 예측 유지보수, 인프라 관리",
        "culturalNote": "한국은 국토교통부가 디지털트윈 국가 전략을 추진 중이며, 건설 분야에서는 BIM과 연계한 디지털트윈 구축이 대형 프로젝트에 의무화되고 있습니다. 베트남은 아직 개념 도입 단계이나, 스마트시티 프로젝트에서 관심이 높아지고 있습니다. 통역 시 'song sinh số'라는 베트남어 표현이 최근 전문가들 사이에 정착되고 있으나, 'mô hình số ảo' 또는 'Digital Twin'을 병기하면 이해도를 높일 수 있습니다.",
        "commonMistakes": [
            {
                "mistake": "디지털 모델",
                "correction": "디지털 트윈 / 디지털 쌍둥이",
                "explanation": "단순 모델이 아닌 실시간 동기화된 쌍둥이 개념"
            },
            {
                "mistake": "mô hình ảo",
                "correction": "song sinh số / Digital Twin",
                "explanation": "가상 모델은 정적, 디지털트윈은 실시간 연동이 핵심"
            },
            {
                "mistake": "3D 모델",
                "correction": "디지털 트윈 (또는 3D와 구분 설명)",
                "explanation": "3D는 형상만, 디지털트윈은 데이터 동기화까지 포함"
            }
        ],
        "examples": [
            {
                "ko": "이 프로젝트는 디지털 트윈으로 시공 전 시뮬레이션을 진행합니다.",
                "vi": "Dự án này tiến hành mô phỏng trước thi công bằng song sinh số.",
                "situation": "formal"
            },
            {
                "ko": "디지털 트윈에서 균열 발생 위치를 예측할 수 있어요.",
                "vi": "Có thể dự đoán vị trí nứt bằng song sinh số.",
                "situation": "onsite"
            },
            {
                "ko": "BIM 데이터를 디지털 트윈과 연동합니다.",
                "vi": "Liên kết dữ liệu BIM với song sinh số.",
                "situation": "informal"
            }
        ],
        "relatedTerms": ["BIM", "IoT 센서", "시뮬레이션", "스마트시티", "클라우드"]
    },
    {
        "slug": "dao-tao-an-toan-vr",
        "korean": "VR 안전 교육",
        "vietnamese": "Đào tạo an toàn VR",
        "hanja": "安全敎育",
        "hanjaReading": "安(편안할 안) + 全(온전할 전) + 敎(가르칠 교) + 育(기를 육)",
        "pronunciation": "다오 타오 안 토안 VR",
        "meaningKo": "가상현실(VR) 기술을 활용해 건설 현장의 위험 상황을 체험하며 안전 교육을 받는 시스템. 추락, 감전, 중장비 사고 등을 안전하게 시뮬레이션하여 교육 효과를 극대화합니다. 통역 시 '몰입형 교육(đào tạo nhập vai)'임을 강조하고, 베트남 현장에서는 '실감형(chân thực)'이라는 표현을 추가하면 이해가 쉽습니다. 한국은 중대재해처벌법 시행 이후 VR 안전 교육 의무화 추세이며, 베트남도 대형 건설사 중심으로 도입이 시작되고 있습니다.",
        "meaningVi": "Hệ thống đào tạo an toàn sử dụng công nghệ thực tế ảo (VR) để trải nghiệm tình huống nguy hiểm như rơi từ độ cao, điện giật, tai nạn máy móc một cách an toàn và nâng cao hiệu quả đào tạo.",
        "context": "안전 교육, 사고 예방, 몰입형 체험, 신입 교육",
        "culturalNote": "한국은 건설 현장 안전 교육 시 VR 체험을 의무화하는 추세이며, 정부 보조금 지원도 있습니다. 베트남은 아직 초기 단계로 비용 부담이 크나, 외국계 및 대형 건설사에서 시범 도입 중입니다. 통역 시 한국의 '체험 효과(hiệu quả trải nghiệm)' 및 '사고율 감소(giảm tỷ lệ tai nạn)' 데이터를 제시하면 베트남 측 설득력을 높일 수 있습니다. 베트남은 'thực tế ảo'라는 표현이 일반적이나, 'VR'이라는 약어도 널리 통용됩니다.",
        "commonMistakes": [
            {
                "mistake": "가상 훈련",
                "correction": "VR 안전 교육 / 가상현실 안전 교육",
                "explanation": "가상은 개념만, VR은 기술 명시 필요"
            },
            {
                "mistake": "huấn luyện ảo",
                "correction": "đào tạo an toàn VR / đào tạo bằng thực tế ảo",
                "explanation": "가상 훈련은 모호, VR 기술임을 명확히 해야"
            },
            {
                "mistake": "VR 게임",
                "correction": "VR 안전 교육 / VR 안전 체험",
                "explanation": "게임이 아닌 교육 목적 강조 필요"
            }
        ],
        "examples": [
            {
                "ko": "신입 직원은 입사 시 VR 안전 교육을 필수로 받습니다.",
                "vi": "Nhân viên mới bắt buộc tham gia đào tạo an toàn VR khi nhập công.",
                "situation": "formal"
            },
            {
                "ko": "VR로 추락 사고를 체험하니까 실감 나더라고요.",
                "vi": "Trải nghiệm tai nạn rơi từ độ cao bằng VR rất chân thực.",
                "situation": "onsite"
            },
            {
                "ko": "이번 주 목요일에 VR 안전 교육 있어요.",
                "vi": "Thứ Năm tuần này có đào tạo an toàn VR.",
                "situation": "informal"
            }
        ],
        "relatedTerms": ["안전 교육", "가상현실", "중대재해처벌법", "사고 예방", "몰입형"]
    }
]

# 파일 경로 (절대 경로)
file_path = os.path.join(
    os.path.expanduser("~"),
    "Documents",
    "claude_code",
    "projects",
    "vn.epicstage.co.kr",
    "src",
    "data",
    "terms",
    "construction.json"
)

def main():
    """메인 실행 함수"""
    # 기존 파일 읽기
    with open(file_path, "r", encoding="utf-8") as f:
        existing_data = json.load(f)

    print(f"기존 용어 수: {len(existing_data)}")

    # 새 용어 추가
    existing_data.extend(data)

    print(f"추가 후 용어 수: {len(existing_data)}")

    # 파일 저장 (들여쓰기 2칸, 유니코드 이스케이프 없이)
    with open(file_path, "w", encoding="utf-8") as f:
        json.dump(existing_data, f, ensure_ascii=False, indent=2)

    print(f"✅ {len(data)}개 용어 추가 완료: {file_path}")
    print("\n추가된 용어:")
    for term in data:
        print(f"  - {term['korean']} ({term['vietnamese']})")

if __name__ == "__main__":
    main()
