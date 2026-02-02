#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
건설(Construction) 용어 추가 스크립트 v4
테마: 전기/통신배선 (케이블트레이, 전선관, 차단기, 접지, 통신배관 등)
Tier S 품질 기준 준수 (90점 이상)
"""

import json
import os

# 추가할 용어 데이터 (10개)
new_terms = [
    {
        "slug": "cau-thang-cap",
        "korean": "케이블트레이",
        "vietnamese": "Cáu thang cáp",
        "hanja": None,
        "hanjaReading": None,
        "pronunciation": "까우 탕 깝",
        "meaningKo": "전선이나 케이블을 지지하고 보호하기 위한 사다리 모양의 금속 구조물입니다. 통역 시 '케이블 랙'과 혼동하지 않도록 주의해야 하며, 베트남 현장에서는 'máng cáp'이라는 용어도 함께 사용됩니다. 시공 시 하중 계산과 접지 여부를 반드시 확인해야 하며, 소방법상 난연성 케이블 사용 구간에서는 방화 구획 관통부 처리가 필수입니다.",
        "meaningVi": "Kết cấu kim loại hình thang đỡ và bảo vệ dây điện hoặc cáp. Trong công trường Việt Nam thường gọi là 'máng cáp'. Khi thi công cần kiểm tra tính toán tải trọng và tiếp địa bắt buộc.",
        "context": "전기 배선 공사, 통신 설비 공사, 플랜트 설비",
        "culturalNote": "한국에서는 KS 규격에 따라 하중 등급(경량/중량)을 엄격히 구분하지만, 베트남 현장에서는 'máng cáp kim loại'와 'máng cáp nhựa'로 재질 중심으로 분류하는 경우가 많습니다. 특히 베트남에서는 부식 방지를 위해 아연도금 처리를 한국보다 더 중요하게 여기며, 해안 지역 프로젝트에서는 스테인리스 재질 사용을 요구하기도 합니다.",
        "commonMistakes": [
            {
                "mistake": "케이블 랙이요 (Cable rack-iyô)",
                "correction": "케이블트레이입니다 (Cáu thang cáp)",
                "explanation": "영어 'cable tray'를 한국식으로 표기한 것이 '케이블트레이'이며, 베트남어로는 사다리를 의미하는 'cáu thang'을 사용합니다"
            },
            {
                "mistake": "Máng cáp điện (전기 케이블 덕트)",
                "correction": "Cáu thang cáp 또는 Máng cáp",
                "explanation": "덕트(ống gió)와 케이블트레이는 다른 설비이므로 구분 필요"
            },
            {
                "mistake": "하중 등급 미확인 통역",
                "correction": "Cấp tải trọng (loại nhẹ/loại nặng) 반드시 명시",
                "explanation": "하중 등급에 따라 자재 사양이 달라지므로 통역 시 누락 금지"
            }
        ],
        "examples": [
            {
                "ko": "이 구간은 케이블트레이를 천장에 매달아 시공합니다",
                "vi": "Đoạn này thi công cáu thang cáp treo trần",
                "situation": "onsite"
            },
            {
                "ko": "케이블트레이 접지 저항값이 기준치를 초과했습니다",
                "vi": "Giá trị điện trở tiếp địa của cáu thang cáp vượt quá tiêu chuẩn",
                "situation": "formal"
            },
            {
                "ko": "아연도금 케이블트레이로 자재 변경 부탁드립니다",
                "vi": "Nhờ thay đổi vật liệu sang cáu thang cáp mạ kẽm",
                "situation": "informal"
            }
        ],
        "relatedTerms": ["전선관", "배관", "접지", "케이블", "전기배선"]
    },
    {
        "slug": "ong-day-dien",
        "korean": "전선관",
        "vietnamese": "Ống dây điện",
        "hanja": "電線管",
        "hanjaReading": "전(번개 전) + 선(줄 선) + 관(대롱 관)",
        "pronunciation": "옹 제이 디엔",
        "meaningKo": "전선을 보호하고 배선 경로를 확보하기 위한 관(管) 형태의 자재입니다. 통역 시 PVC관, 금속관, 가요전선관 등 종류를 정확히 구분해야 하며, 베트남에서는 'ống luồn dây'라는 표현도 혼용됩니다. 노출 배관과 은폐 배관에 따라 시공 방법이 다르므로 도면 검토 시 주의가 필요하며, 특히 방폭 구역에서는 후강전선관(ống thép dày) 사용이 의무화됩니다.",
        "meaningVi": "Vật liệu dạng ống bảo vệ dây điện và tạo đường dẫn lắp đặt. Có nhiều loại như ống PVC, ống kim loại, ống ruột gà. Khu vực chống cháy nổ bắt buộc dùng ống thép dày.",
        "context": "전기 공사, 건축 설비, 배선 시공",
        "culturalNote": "한국에서는 KS C 8454 규격에 따라 전선관 두께와 내압 성능을 엄격히 관리하지만, 베트남에서는 TCVN 표준 외에도 현장별로 자체 기준을 적용하는 경우가 많습니다. 특히 베트남 남부 지역은 습도가 높아 PVC관 사용 비율이 높으며, 한국처럼 금속 가요전선관을 선호하지 않습니다. 또한 베트남에서는 콘크리트 매립 배관 시 진동 다짐을 한국보다 덜 엄격하게 하는 경향이 있어 품질 관리 주의가 필요합니다.",
        "commonMistakes": [
            {
                "mistake": "Ống nước (수도관)",
                "correction": "Ống dây điện 또는 Ống luồn dây",
                "explanation": "수도관(ống nước)과 전선관(ống dây điện)은 완전히 다른 설비"
            },
            {
                "mistake": "PVC관을 Ống nhựa라고만 표현",
                "correction": "Ống nhựa PVC 또는 Ống luồn dây PVC",
                "explanation": "'ống nhựa'는 모든 플라스틱 관을 의미하므로 전선관임을 명시 필요"
            },
            {
                "mistake": "노출 배관을 lộ thiên(야외 노출)으로 오역",
                "correction": "Lắp nổi (노출 배관) vs Lắp âm (은폐 배관)",
                "explanation": "'lộ thiên'은 실외를 의미하며, 실내 노출 배관은 'lắp nổi'"
            }
        ],
        "examples": [
            {
                "ko": "이 구간은 PVC 전선관으로 시공합니다",
                "vi": "Đoạn này thi công bằng ống dây điện PVC",
                "situation": "onsite"
            },
            {
                "ko": "전선관 굽힘 반경이 규정에 맞지 않습니다",
                "vi": "Bán kính uốn ống dây điện không đúng quy định",
                "situation": "formal"
            },
            {
                "ko": "가요전선관 연결부 실링 확인 부탁드립니다",
                "vi": "Nhờ kiểm tra phần đóng kín nối ống ruột gà",
                "situation": "informal"
            }
        ],
        "relatedTerms": ["케이블트레이", "배선", "접지", "PVC관", "금속관"]
    },
    {
        "slug": "cb-bao-ve-day-dien",
        "korean": "배선용차단기",
        "vietnamese": "CB bảo vệ dây điện",
        "hanja": "配線用遮斷器",
        "hanjaReading": "배(나눌 배) + 선(줄 선) + 용(쓸 용) + 차(가릴 차) + 단(끊을 단) + 기(그릇 기)",
        "pronunciation": "씨비 바오 베 제이 디엔",
        "meaningKo": "과전류나 단락 발생 시 자동으로 회로를 차단하여 배선을 보호하는 차단기입니다. 통역 시 MCCB(Molded Case Circuit Breaker)와 구분해야 하며, 정격 전류(dòng điện định mức)와 차단 용량(khả năng cắt)을 반드시 확인해야 합니다. 베트남에서는 흔히 'CB'라고 줄여 부르며, 분전반 내 설치 위치와 결선 방식(단상/삼상)에 따라 시공 방법이 달라집니다. 통역 실수 방지를 위해 누전차단기(ELCB)와 명확히 구분하는 것이 중요합니다.",
        "meaningVi": "Thiết bị tự động ngắt mạch khi có quá dòng hoặc đoản mạch để bảo vệ hệ thống dây điện. Thường gọi tắt là 'CB'. Cần phân biệt với MCCB và ELCB. Phải kiểm tra dòng điện định mức và khả năng cắt.",
        "context": "전기 설비, 분전반 시공, 안전 장치",
        "culturalNote": "한국에서는 주택용으로 주로 2P(2극) 배선용차단기를 사용하지만, 베트남에서는 1P+N(1극+중성선) 타입도 많이 사용합니다. 또한 한국은 KS C 8321 규격을 따르지만 베트남은 IEC 규격을 주로 참조하므로, 정격 표기 방식이 다를 수 있습니다. 베트남 현장에서는 중국산 저가 CB를 사용하는 경우가 많아, 한국 시공사는 품질 검증 절차를 강화해야 합니다. 특히 베트남에서는 'aptomat'이라는 프랑스어 유래 용어도 함께 사용됩니다.",
        "commonMistakes": [
            {
                "mistake": "CB와 ELCB를 혼동",
                "correction": "CB(배선용차단기)는 과전류, ELCB(누전차단기)는 누전 차단",
                "explanation": "용도와 동작 원리가 다르므로 반드시 구분"
            },
            {
                "mistake": "Cầu dao tự động (자동 스위치)로 통역",
                "correction": "CB bảo vệ dây điện 또는 Aptomat",
                "explanation": "'cầu dao'는 단순 개폐기이며 보호 기능 없음"
            },
            {
                "mistake": "정격 전류를 dòng điện tối đa(최대 전류)로 오역",
                "correction": "Dòng điện định mức (정격 전류)",
                "explanation": "정격과 최대는 다른 개념"
            }
        ],
        "examples": [
            {
                "ko": "이 분전반에는 63A 배선용차단기를 설치합니다",
                "vi": "Tủ điện này lắp CB bảo vệ dây điện 63A",
                "situation": "onsite"
            },
            {
                "ko": "배선용차단기 동작 시험 결과가 불합격입니다",
                "vi": "Kết quả thử nghiệm hoạt động CB bảo vệ dây điện không đạt",
                "situation": "formal"
            },
            {
                "ko": "CB 트립됐어요, 확인 좀 해주세요",
                "vi": "CB bị cắt rồi, nhờ kiểm tra giúp",
                "situation": "informal"
            }
        ],
        "relatedTerms": ["누전차단기", "분전반", "과전류", "단락", "전기안전"]
    },
    {
        "slug": "elcb-chong-ro-dien",
        "korean": "누전차단기",
        "vietnamese": "ELCB chống rò điện",
        "hanja": "漏電遮斷器",
        "hanjaReading": "누(샐 누) + 전(번개 전) + 차(가릴 차) + 단(끊을 단) + 기(그릇 기)",
        "pronunciation": "이엘씨비 총 조 디엔",
        "meaningKo": "누설 전류를 감지하여 감전 사고를 예방하는 안전 차단기입니다. 통역 시 배선용차단기(CB)와 구분이 중요하며, 동작 감도(độ nhạy)는 통상 30mA가 기준입니다. 베트남에서는 'aptomat chống giật'이라는 표현도 사용되며, 욕실이나 주방 등 습기가 많은 장소에는 필수로 설치해야 합니다. 월 1회 시험 버튼(nút thử) 작동 확인이 의무이며, 접지 시스템과 연동하여 안전성을 확보해야 합니다.",
        "meaningVi": "Thiết bị an toàn tự động ngắt điện khi phát hiện dòng rò để ngăn ngừa tai nạn điện giật. Thường gọi là 'aptomat chống giật'. Độ nhạy tiêu chuẩn 30mA. Bắt buộc lắp ở khu vực ẩm ướt như nhà tắm, bếp.",
        "context": "전기 안전, 주택 설비, 습기 지역 배선",
        "culturalNote": "한국에서는 전기사업법에 따라 주택용 콘센트 회로에 누전차단기 설치가 의무화되어 있지만, 베트남에서는 규정 적용이 상대적으로 느슨한 편입니다. 특히 베트남 구형 건물에서는 누전차단기가 없는 경우도 많아, 한국 시공사가 리모델링 시 안전 기준 강화를 제안해야 합니다. 베트남에서는 프랑스 식민지 시절 용어인 'disjoncteur différentiel'을 줄여 'aptomat chống giật'으로 부르며, 한국의 '인체감전보호용 누전차단기'에 해당합니다.",
        "commonMistakes": [
            {
                "mistake": "ELCB와 CB를 같은 것으로 통역",
                "correction": "ELCB(누전차단기)는 감전 방지, CB(배선용차단기)는 과전류 방지",
                "explanation": "보호 목적과 동작 원리가 완전히 다름"
            },
            {
                "mistake": "Aptomat (일반 차단기)로만 통역",
                "correction": "ELCB 또는 Aptomat chống giật (감전 방지 차단기)",
                "explanation": "'aptomat'은 모든 차단기를 의미하므로 누전 기능 명시 필요"
            },
            {
                "mistake": "시험 버튼을 nút bấm(일반 버튼)으로 통역",
                "correction": "Nút thử (시험 버튼) 또는 nút test",
                "explanation": "정기 점검용 전용 버튼이므로 용도 명시 필요"
            }
        ],
        "examples": [
            {
                "ko": "욕실에는 30mA 누전차단기를 설치해야 합니다",
                "vi": "Phòng tắm phải lắp ELCB 30mA",
                "situation": "formal"
            },
            {
                "ko": "누전차단기 시험 버튼 눌러서 작동 확인해주세요",
                "vi": "Nhờ nhấn nút thử ELCB để kiểm tra hoạt động",
                "situation": "onsite"
            },
            {
                "ko": "누전차단기가 자꾸 떨어져요",
                "vi": "ELCB cứ bị cắt liên tục",
                "situation": "informal"
            }
        ],
        "relatedTerms": ["배선용차단기", "접지", "감전", "분전반", "전기안전"]
    },
    {
        "slug": "tiep-dia",
        "korean": "접지",
        "vietnamese": "Tiếp địa",
        "hanja": "接地",
        "hanjaReading": "접(이을 접) + 지(땅 지)",
        "pronunciation": "띱 지아",
        "meaningKo": "전기 설비의 금속 외함을 대지에 연결하여 감전 사고를 예방하는 안전 조치입니다. 통역 시 접지 저항값(điện trở tiếp địa)과 접지 종류(1종/2종/3종 접지)를 명확히 구분해야 하며, 베트남에서는 'заземление'(러시아어 유래)를 줄여 'đấu đất'라고도 표현합니다. 시공 시 접지봉 매설 깊이와 토양 저항률을 반드시 측정해야 하며, 피뢰 설비와 연동하여 전체 접지 시스템을 설계해야 합니다.",
        "meaningVi": "Biện pháp an toàn kết nối vỏ kim loại thiết bị điện với đất để ngăn ngừa tai nạn điện giật. Thường gọi là 'đấu đất'. Cần đo điện trở tiếp địa và phân loại theo cấp (cấp 1/2/3). Phải kiểm tra độ sâu chôn que tiếp địa và điện trở suất đất.",
        "context": "전기 안전, 설비 시공, 피뢰 설비",
        "culturalNote": "한국에서는 KS C IEC 60364 기준에 따라 접지 저항 기준이 엄격하지만(1종 접지 10Ω 이하), 베트남에서는 TCVN 기준이 상대적으로 완화되어 있습니다(4Ω 이하도 허용). 특히 베트남 남부는 토양 저항률이 높아 접지 시공이 어려운 경우가 많아, 화학적 접지 공법이나 다수의 접지봉 병렬 연결을 사용합니다. 또한 베트남에서는 'nối đất'(대지 연결)와 'tiếp địa'를 혼용하지만, 기술 문서에서는 'tiếp địa'가 공식 용어입니다.",
        "commonMistakes": [
            {
                "mistake": "Đấu mass (배터리 음극 접지)로 오역",
                "correction": "Tiếp địa (대지 접지) 또는 Đấu đất",
                "explanation": "'mass'는 자동차 전기에서 쓰는 용어이며 건축 전기는 'tiếp địa'"
            },
            {
                "mistake": "접지 저항을 điện trở đất(토양 저항)로 통역",
                "correction": "Điện trở tiếp địa (접지 저항)",
                "explanation": "토양 저항률(điện trở suất đất)과 접지 저항은 다른 개념"
            },
            {
                "mistake": "1종 접지를 loại 1(1번째 타입)로 통역",
                "correction": "Tiếp địa cấp 1 (1종 접지)",
                "explanation": "'loại'는 일반 분류, 접지 등급은 'cấp'"
            }
        ],
        "examples": [
            {
                "ko": "접지 저항 측정값이 15Ω으로 기준 초과입니다",
                "vi": "Giá trị đo điện trở tiếp địa là 15Ω, vượt tiêu chuẩn",
                "situation": "formal"
            },
            {
                "ko": "접지봉 3개를 3m 간격으로 설치합니다",
                "vi": "Lắp 3 que tiếp địa cách nhau 3m",
                "situation": "onsite"
            },
            {
                "ko": "접지선 연결 확인 좀 해주세요",
                "vi": "Nhờ kiểm tra kết nối dây tiếp địa",
                "situation": "informal"
            }
        ],
        "relatedTerms": ["누전차단기", "피뢰침", "분전반", "전기안전", "접지봉"]
    },
    {
        "slug": "kim-thu-set",
        "korean": "피뢰침",
        "vietnamese": "Kim thu sét",
        "hanja": "避雷針",
        "hanjaReading": "피(피할 피) + 뢰(우레 뢰) + 침(바늘 침)",
        "pronunciation": "낌 투 셋",
        "meaningKo": "건축물을 낙뢰로부터 보호하기 위해 지붕이나 최상부에 설치하는 금속 침입니다. 통역 시 수뢰부(đầu thu sét), 인하도선(dây dẫn xuống), 접지극(cực tiếp địa)의 3요소를 명확히 구분해야 하며, 베트nam에서는 'cột thu sét'(피뢰 기둥)이라는 표현도 사용됩니다. 보호 범위는 침 높이의 2배 반경이 기본이며, 건물 높이가 20m를 초과하면 설치가 의무화됩니다. 통역 실수 방지를 위해 피뢰기(arrester)와 구분이 중요합니다.",
        "meaningVi": "Kim kim loại lắp trên mái hoặc đỉnh công trình để bảo vệ khỏi sét đánh. Gồm 3 bộ phận: đầu thu sét (đầu nhận), dây dẫn xuống, cực tiếp địa. Bán kính bảo vệ thường bằng 2 lần chiều cao kim. Công trình cao trên 20m bắt buộc lắp.",
        "context": "건축 전기, 안전 설비, 고층 건물",
        "culturalNote": "한국에서는 건축법 시행령에 따라 높이 20m 이상 건물은 피뢰침 설치가 의무이지만, 베트남에서는 지역별로 낙뢰 빈도가 높아 10m 이상 건물에도 권장됩니다. 특히 베트남 북부는 여름철 낙뢰가 빈번하여 피뢰 설비 중요도가 한국보다 높습니다. 베트남에서는 프랑스 식민지 시절 용어인 'paratonnerre'를 줄여 'kim thu sét'으로 번역했으며, 중국어 영향으로 '避雷針'이라는 한자어도 함께 사용됩니다. 시공 시 베트남은 접지 저항 기준이 한국보다 완화되어 있어 품질 관리 주의가 필요합니다.",
        "commonMistakes": [
            {
                "mistake": "피뢰기(arrester)와 피뢰침 혼동",
                "correction": "피뢰침(kim thu sét)은 건물용, 피뢰기(chống sét lan truyền)는 전력선용",
                "explanation": "용도와 설치 위치가 완전히 다름"
            },
            {
                "mistake": "Kim sét (낙뢰)로 통역",
                "correction": "Kim thu sét (피뢰침) 또는 Cột thu sét",
                "explanation": "'kim sét'은 번개를 의미하며 설비가 아님"
            },
            {
                "mistake": "인하도선을 dây điện(전선)으로 통역",
                "correction": "Dây dẫn xuống (인하도선)",
                "explanation": "피뢰침 전용 도선이므로 일반 전선과 구분 필요"
            }
        ],
        "examples": [
            {
                "ko": "건물 높이가 25m이므로 피뢰침 설치가 필요합니다",
                "vi": "Chiều cao công trình 25m nên cần lắp kim thu sét",
                "situation": "formal"
            },
            {
                "ko": "피뢰침 접지 저항값이 10Ω입니다",
                "vi": "Điện trở tiếp địa kim thu sét là 10Ω",
                "situation": "onsite"
            },
            {
                "ko": "피뢰침 인하도선 연결 상태 확인 부탁해요",
                "vi": "Nhờ kiểm tra kết nối dây dẫn xuống kim thu sét",
                "situation": "informal"
            }
        ],
        "relatedTerms": ["접지", "인하도선", "피뢰기", "낙뢰", "전기안전"]
    },
    {
        "slug": "ong-thong-tin",
        "korean": "통신배관",
        "vietnamese": "Ống thông tin",
        "hanja": "通信配管",
        "hanjaReading": "통(통할 통) + 신(믿을 신) + 배(나눌 배) + 관(대롱 관)",
        "pronunciation": "옹 통 띤",
        "meaningKo": "전화선, 인터넷 케이블, 방송 선로 등 통신 케이블을 보호하고 배선하기 위한 배관입니다. 통역 시 전력 배관(ống điện lực)과 구분이 중요하며, 베트남에서는 'ống viễn thông' 또는 'ống cáp mạng'이라는 표현도 사용됩니다. 시공 시 전력선과의 이격 거리(통상 30cm 이상)를 준수해야 하며, 광케이블용 배관은 곡률 반경을 더 크게 확보해야 합니다. 건물 인입부에서 통신사 MDF실까지의 경로 계획이 중요합니다.",
        "meaningVi": "Ống bảo vệ và lắp đặt cáp thông tin như dây điện thoại, cáp mạng internet, cáp truyền hình. Phải phân biệt với ống điện lực. Khoảng cách tối thiểu với đường điện lực thường 30cm. Ống cáp quang cần bán kính uốn lớn hơn.",
        "context": "통신 설비, 건축 전기, 네트워크 시공",
        "culturalNote": "한국에서는 정보통신공사업법에 따라 통신 배관과 전력 배관을 엄격히 분리하지만, 베트남 현장에서는 간혹 혼용하는 사례가 발생하여 주의가 필요합니다. 특히 베트남에서는 통신사(VNPT, Viettel 등)별로 자체 시공 기준이 있어 사전 협의가 필수입니다. 한국은 PVC 배관을 주로 사용하지만, 베트남에서는 HDPE 배관도 많이 사용하며, 지하 매설 시 경고 테이프 색상도 다릅니다(한국: 주황색, 베트남: 노란색).",
        "commonMistakes": [
            {
                "mistake": "Ống điện (전기 배관)으로 통역",
                "correction": "Ống thông tin (통신 배관) 또는 Ống viễn thông",
                "explanation": "통신과 전력 배관은 용도와 규격이 다름"
            },
            {
                "mistake": "Ống mạng (네트워크 관)으로만 통역",
                "correction": "Ống thông tin (전화/인터넷/방송 모두 포함)",
                "explanation": "'ống mạng'은 인터넷만 의미하므로 범위가 좁음"
            },
            {
                "mistake": "이격 거리를 khoảng cách xa(먼 거리)로 애매하게 통역",
                "correction": "Khoảng cách an toàn tối thiểu 30cm (최소 안전 이격 30cm)",
                "explanation": "규정 수치를 명확히 전달해야 시공 오류 방지"
            }
        ],
        "examples": [
            {
                "ko": "통신배관은 전력 배관과 30cm 이상 이격하여 설치합니다",
                "vi": "Ống thông tin lắp cách ống điện lực tối thiểu 30cm",
                "situation": "formal"
            },
            {
                "ko": "MDF실까지 통신배관 경로 확인 부탁드립니다",
                "vi": "Nhờ kiểm tra đường đi ống thông tin đến phòng MDF",
                "situation": "onsite"
            },
            {
                "ko": "광케이블용 배관은 곡률 반경 크게 해주세요",
                "vi": "Ống cáp quang nhờ làm bán kính uốn lớn",
                "situation": "informal"
            }
        ],
        "relatedTerms": ["전선관", "케이블", "LAN설비", "광케이블", "MDF실"]
    },
    {
        "slug": "thiet-bi-lan",
        "korean": "LAN설비",
        "vietnamese": "Thiết bị LAN",
        "hanja": None,
        "hanjaReading": None,
        "pronunciation": "티엣 비 란",
        "meaningKo": "근거리 통신망(Local Area Network) 구축을 위한 네트워크 장비 및 배선 시스템입니다. 통역 시 스위치, 라우터, 패치 패널, 정보통신 아웃렛(IO) 등 구성 요소를 명확히 구분해야 하며, 베트남에서는 'hệ thống mạng nội bộ'라는 표현도 사용됩니다. 시공 시 Cat.5e, Cat.6, Cat.6A 등 케이블 등급을 정확히 확인해야 하며, PoE(Power over Ethernet) 지원 여부에 따라 전원 공급 방식이 달라집니다. 통역 실수 방지를 위해 WAN과 구분이 중요합니다.",
        "meaningVi": "Hệ thống thiết bị và dây cáp xây dựng mạng LAN (mạng nội bộ). Bao gồm switch, router, patch panel, ổ cắm IO. Phải kiểm tra cấp cáp Cat.5e, Cat.6, Cat.6A. Cần xác định hỗ trợ PoE hay không để cấp nguồn.",
        "context": "네트워크 시공, 정보통신 설비, 건물 IT 인프라",
        "culturalNote": "한국에서는 TIA/EIA-568 국제 표준을 따르지만, 베트남에서는 간혹 구형 Cat.5 케이블을 사용하는 경우가 있어 시방서 검토가 필요합니다. 특히 베트남 현장에서는 중국산 저가 케이블 사용 비율이 높아 품질 인증(Fluke 테스트) 여부를 반드시 확인해야 합니다. 한국은 정보통신 아웃렛을 '정보통신 단자함'이라고도 하지만, 베트남에서는 'ổ cắm mạng' 또는 'IO'로 줄여 부르며, 시공 방식도 한국은 은폐형을 선호하는 반면 베트남은 노출형 몰딩 시공이 많습니다.",
        "commonMistakes": [
            {
                "mistake": "WAN과 LAN 혼동",
                "correction": "LAN(mạng nội bộ)은 건물 내부, WAN(mạng diện rộng)은 외부 연결",
                "explanation": "네트워크 범위와 장비 구성이 다름"
            },
            {
                "mistake": "Switch를 Công tắc(전기 스위치)로 오역",
                "correction": "Switch mạng (네트워크 스위치) 또는 Thiết bị chuyển mạch",
                "explanation": "전기 스위치와 네트워크 스위치는 완전히 다른 장비"
            },
            {
                "mistake": "Cat.6를 Mèo 6(고양이 6)으로 오역",
                "correction": "Cáp Cat.6 (Category 6 케이블)",
                "explanation": "'Cat'은 'Category'의 약자이며 케이블 등급 표시"
            }
        ],
        "examples": [
            {
                "ko": "이 건물은 Cat.6A 케이블로 LAN설비를 구축합니다",
                "vi": "Tòa nhà này xây dựng thiết bị LAN bằng cáp Cat.6A",
                "situation": "formal"
            },
            {
                "ko": "스위치에서 각 IO까지 케이블 길이가 90m를 초과하면 안 됩니다",
                "vi": "Chiều dài cáp từ switch đến mỗi IO không được vượt quá 90m",
                "situation": "onsite"
            },
            {
                "ko": "IO 위치 좀 확인해주세요",
                "vi": "Nhờ kiểm tra vị trí ổ cắm mạng",
                "situation": "informal"
            }
        ],
        "relatedTerms": ["통신배관", "스위치", "라우터", "케이블", "네트워크"]
    },
    {
        "slug": "ong-yeu-dien",
        "korean": "약전배관",
        "vietnamese": "Ống yếu điện",
        "hanja": "弱電配管",
        "hanjaReading": "약(약할 약) + 전(번개 전) + 배(나눌 배) + 관(대롱 관)",
        "pronunciation": "옹 이에우 디엔",
        "meaningKo": "전화, 인터넷, CCTV, 화재경보기 등 저전압(통상 DC 48V 이하) 신호 전송용 배관입니다. 통역 시 강전 배관(ống điện mạnh)과 구분이 필수이며, 베트남에서는 'ống hệ thống yếu'라는 표현도 사용됩니다. 시공 시 강전선과의 교차 부분에서는 직각으로 교차시켜야 하며, 병행 구간에서는 30cm 이상 이격해야 합니다. 통역 실수 방지를 위해 신호의 전압 레벨과 용도를 명확히 설명해야 합니다.",
        "meaningVi": "Ống lắp đặt cáp điện áp thấp (thường dưới DC 48V) dùng cho điện thoại, internet, CCTV, báo cháy. Phải phân biệt với ống điện mạnh. Khi giao với đường điện mạnh phải vuông góc, đoạn song song cách tối thiểu 30cm.",
        "context": "건축 전기, 약전 설비, 신호 전송 시스템",
        "culturalNote": "한국에서는 전기설비기술기준에 따라 약전과 강전을 명확히 구분하여 시공하지만, 베트남 현장에서는 간혹 혼용하는 경우가 있어 도면 검토 시 주의가 필요합니다. 특히 베트남에서는 CCTV나 인터폰 배관을 별도로 '약전'으로 분류하지 않고 '통신 배관'으로 통칭하는 경우가 많아, 시방서에서 명확히 구분해야 합니다. 한국은 PF관(플렉시블관)을 많이 사용하지만, 베트남에서는 경질 PVC관을 선호하는 경향이 있습니다.",
        "commonMistakes": [
            {
                "mistake": "Ống điện nhỏ (작은 전기 배관)로 통역",
                "correction": "Ống yếu điện (약전 배관) 또는 Ống hệ thống yếu",
                "explanation": "전압 레벨과 용도가 다르므로 크기가 아닌 전압으로 구분"
            },
            {
                "mistake": "강전과 약전을 điện cao/thấp(고압/저압)으로 오역",
                "correction": "Điện mạnh(강전) / Điện yếu(약전)",
                "explanation": "고압/저압은 다른 분류 체계"
            },
            {
                "mistake": "교차를 cắt ngang(가로지르기)으로 애매하게 통역",
                "correction": "Giao vuông góc (직각 교차)",
                "explanation": "시공 기준에 직각 교차가 명시되어 있음"
            }
        ],
        "examples": [
            {
                "ko": "CCTV 배선은 약전배관으로 시공합니다",
                "vi": "Dây CCTV thi công bằng ống yếu điện",
                "situation": "formal"
            },
            {
                "ko": "약전배관이 강전 배관과 너무 가까워요",
                "vi": "Ống yếu điện quá gần ống điện mạnh",
                "situation": "onsite"
            },
            {
                "ko": "화재경보기 선은 약전으로 처리하세요",
                "vi": "Dây báo cháy xử lý theo hệ thống yếu điện",
                "situation": "informal"
            }
        ],
        "relatedTerms": ["통신배관", "강전", "CCTV", "화재경보기", "전선관"]
    },
    {
        "slug": "den-chieu-sang",
        "korean": "조명기구",
        "vietnamese": "Đèn chiếu sáng",
        "hanja": "照明器具",
        "hanjaReading": "조(비출 조) + 명(밝을 명) + 기(그릇 기) + 구(갖출 구)",
        "pronunciation": "덴 찌에우 상",
        "meaningKo": "실내외 공간을 밝히기 위한 전기 조명 장치의 총칭입니다. 통역 시 LED, 형광등(đèn huỳnh quang), 백열등(đèn sợi đốt) 등 광원 종류와 매입형(âm trần), 노출형(nổi), 펜던트형(treo) 등 설치 방식을 구분해야 합니다. 베트남에서는 'đồ chiếu sáng'이라는 표현도 사용되며, 시공 시 조도 기준(lux)과 색온도(nhiệt độ màu)를 확인해야 합니다. 통역 실수 방지를 위해 비상조명(đèn sự cố)과 일반 조명을 명확히 구분하는 것이 중요합니다.",
        "meaningVi": "Thiết bị chiếu sáng điện dùng cho không gian trong nhà và ngoài trời. Phân loại theo nguồn sáng (LED, đèn huỳnh quang, đèn sợi đốt) và cách lắp (âm trần, nổi, treo). Cần kiểm tra tiêu chuẩn độ sáng (lux) và nhiệt độ màu.",
        "context": "전기 설비, 건축 조명, 인테리어",
        "culturalNote": "한국에서는 KS 조도 기준(사무실 500lux, 복도 150lux 등)을 엄격히 적용하지만, 베트남에서는 TCVN 기준이 상대적으로 낮아 한국 시공사는 조도 상향을 제안하는 경우가 많습니다. 특히 베트남에서는 전력 요금이 비싸 LED 조명 사용 비율이 한국보다 훨씬 높으며, 형광등은 거의 사용하지 않는 추세입니다. 베트남에서는 '등(đèn)' 단위로 부르며, 한국처럼 '등기구'라는 포괄 용어보다는 '조명(chiếu sáng)'이 더 일반적입니다.",
        "commonMistakes": [
            {
                "mistake": "Đèn điện (전기등)으로만 통역",
                "correction": "Đèn chiếu sáng (조명기구) 또는 Đồ chiếu sáng",
                "explanation": "'đèn điện'은 일상 용어이며 기술 문서에서는 부적합"
            },
            {
                "mistake": "매입등을 đèn chìm(잠긴 등)으로 오역",
                "correction": "Đèn âm trần (매입형 조명)",
                "explanation": "'chìm'은 물에 잠긴 것을 의미하므로 부적절"
            },
            {
                "mistake": "조도를 độ sáng(밝기)로 통역",
                "correction": "Cường độ chiếu sáng (조도, 단위 lux)",
                "explanation": "'độ sáng'은 일반 밝기이며 조도는 기술 용어"
            }
        ],
        "examples": [
            {
                "ko": "사무실 조명기구는 500lux 기준으로 설계합니다",
                "vi": "Đèn chiếu sáng văn phòng thiết kế theo tiêu chuẩn 500lux",
                "situation": "formal"
            },
            {
                "ko": "복도는 매입형 LED 조명으로 시공해주세요",
                "vi": "Hành lang nhờ thi công đèn LED âm trần",
                "situation": "onsite"
            },
            {
                "ko": "이 조명 색온도 좀 확인해봐요",
                "vi": "Kiểm tra nhiệt độ màu đèn này xem",
                "situation": "informal"
            }
        ],
        "relatedTerms": ["LED", "조도", "비상조명", "분전반", "전기배선"]
    }
]

# JSON 파일 경로
base_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
json_path = os.path.join(base_dir, "data", "terms", "construction.json")

# 기존 JSON 읽기
with open(json_path, "r", encoding="utf-8") as f:
    data = json.load(f)

# 새 용어 추가
data.extend(new_terms)

# JSON 저장 (한글 유지, 들여쓰기 2칸)
with open(json_path, "w", encoding="utf-8") as f:
    json.dump(data, f, ensure_ascii=False, indent=2)

print(f"✅ 전기/통신배선 테마 건설 용어 {len(new_terms)}개 추가 완료")
print(f"📂 파일: {json_path}")
print(f"📊 총 용어 수: {len(data)}개")
print("\n추가된 용어:")
for i, term in enumerate(new_terms, 1):
    print(f"{i}. {term['korean']} ({term['vietnamese']})")
