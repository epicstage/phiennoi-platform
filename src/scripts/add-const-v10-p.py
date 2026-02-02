#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
건설자재시험/품질시험 (Construction Material Testing) 용어 추가 스크립트
Tier S 품질 기준 준수
"""

import json
import os

# CRITICAL: 상대 경로로 construction.json 찾기
file_path = os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', 'data', 'terms', 'construction.json')

# 기존 데이터 로드
with open(file_path, 'r', encoding='utf-8') as f:
    data = json.load(f)  # data is a LIST

# 기존 slug 수집 (중복 방지)
existing_slugs = {t['slug'] for t in data}

# 새 용어 10개 (건설자재시험/품질시험)
new_terms = [
    {
        "slug": "thi-nghiem-nen",
        "korean": "압축시험",
        "vietnamese": "thí nghiệm nén",
        "hanja": "壓縮試驗",
        "hanjaReading": "壓(누를 압) + 縮(줄일 축) + 試(시험할 시) + 驗(시험할 험)",
        "pronunciation": "압축시험 [áp súc tí nggiẹm]",
        "meaningKo": "콘크리트나 석재 등의 건설 자재가 압축력(누르는 힘)을 받았을 때 얼마나 견디는지 측정하는 시험입니다. 통역 시 '압축강도'와 혼동하지 않도록 주의해야 하며, 시험 결과는 MPa(메가파스칼) 단위로 표현됩니다. 베트남 현장에서는 공시체 양생 기간(7일, 28일)을 명확히 구분하여 통역해야 하며, '시험'과 '강도'를 각각 'thí nghiệm'과 'cường độ'로 정확히 구분하여 사용해야 합니다.",
        "meaningVi": "Thí nghiệm xác định khả năng chịu lực nén của vật liệu xây dựng như bê tông, đá. Kết quả đo bằng đơn vị MPa. Cần phân biệt rõ 'thí nghiệm nén' (compression test) với 'cường độ nén' (compressive strength). Trong thực tế công trường, phải chú ý đến thời gian bảo dưỡng mẫu thử (7 ngày, 28 ngày) khi báo cáo kết quả.",
        "context": "건설 현장에서 콘크리트 품질 검사 시 사용",
        "culturalNote": "한국은 KS F 2405 규격을 따르지만 베트남은 TCVN 3118 규격을 따릅니다. 한국 현장에서는 '28일 강도'를 기준으로 하지만 베트남은 경우에 따라 7일 강도도 중요하게 취급합니다. 또한 한국은 100mm 원주형 공시체를 주로 사용하지만 베트남은 150mm 정육면체 공시체도 혼용하므로, 통역 시 공시체 규격을 반드시 확인해야 합니다.",
        "commonMistakes": [
            {
                "mistake": "압축강도와 압축시험을 같은 의미로 사용",
                "correction": "압축시험(thí nghiệm nén)은 '과정', 압축강도(cường độ nén)는 '결과'",
                "explanation": "시험은 행위이고 강도는 측정값이므로 명확히 구분해야 합니다"
            },
            {
                "mistake": "'thí nghiệm ép'으로 번역",
                "correction": "'thí nghiệm nén'이 표준 용어",
                "explanation": "'ép'은 일반적인 누르기, 'nén'은 기술적 압축을 의미합니다"
            },
            {
                "mistake": "단위를 kg/cm²로만 표현",
                "correction": "국제 표준 MPa를 병기하거나 우선 사용",
                "explanation": "베트남도 SI 단위계로 전환 중이므로 MPa 사용이 권장됩니다"
            }
        ],
        "examples": [
            {
                "ko": "28일 압축시험 결과가 설계강도에 미달합니다",
                "vi": "Kết quả thí nghiệm nén 28 ngày không đạt cường độ thiết kế",
                "situation": "formal"
            },
            {
                "ko": "공시체 3개를 채취해서 압축시험 돌려주세요",
                "vi": "Lấy 3 mẫu thử để tiến hành thí nghiệm nén",
                "situation": "onsite"
            },
            {
                "ko": "압축시험기 교정 날짜 확인해봐야겠어요",
                "vi": "Cần kiểm tra ngày hiệu chuẩn máy thí nghiệm nén",
                "situation": "informal"
            }
        ],
        "relatedTerms": ["cường độ nén (압축강도)", "mẫu thử (공시체)", "phòng thí nghiệm (시험실)", "cường độ thiết kế (설계강도)"]
    },
    {
        "slug": "thi-nghiem-keo",
        "korean": "인장시험",
        "vietnamese": "thí nghiệm kéo",
        "hanja": "引張試驗",
        "hanjaReading": "引(끌 인) + 張(베풀 장) + 試(시험할 시) + 驗(시험할 험)",
        "pronunciation": "인장시험 [tí nggiẹm kéo]",
        "meaningKo": "철근, 강재, 용접부 등이 당기는 힘(인장력)에 얼마나 견디는지 측정하는 시험입니다. 통역 시 '항복강도(độ bền chảy)'와 '인장강도(độ bền kéo)'를 명확히 구분해야 하며, 연신율(tỷ lệ dãn dài)도 함께 측정됩니다. 베트남 현장에서는 철근 규격(D10, D13 등)에 따라 시험 방법이 달라지므로 규격을 정확히 통역해야 하며, 시험 결과는 N/mm² 또는 MPa 단위로 표현됩니다.",
        "meaningVi": "Thí nghiệm xác định khả năng chịu lực kéo của vật liệu như thép, cốt thép, mối hàn. Kết quả bao gồm độ bền chảy (yield strength), độ bền kéo (tensile strength) và tỷ lệ dãn dài (elongation). Đơn vị đo là N/mm² hoặc MPa. Phương pháp thí nghiệm khác nhau tùy theo quy cách thép (D10, D13, v.v.).",
        "context": "철근 콘크리트 구조물 시공 시 철근 품질 검사",
        "culturalNote": "한국은 KS D 3504(철근 규격)를 따르고 베트남은 TCVN 1651을 따릅니다. 한국에서는 SD400(항복강도 400MPa)이 표준이지만 베트nam에서는 CB300-V, CB400-V 등의 표기를 사용합니다. 또한 한국은 철근 인장시험 시 표점거리를 명확히 하지만 베트남 현장에서는 이를 생략하는 경우가 있어 통역 시 확인이 필요합니다.",
        "commonMistakes": [
            {
                "mistake": "'thí nghiệm kéo dài'로 표현",
                "correction": "'thí nghiệm kéo'가 정확한 기술 용어",
                "explanation": "'kéo dài'는 '늘이다'는 뜻이고 'kéo'만으로 인장을 의미합니다"
            },
            {
                "mistake": "항복강도와 인장강도를 혼동하여 통역",
                "correction": "항복강도(độ bền chảy), 인장강도(độ bền kéo)는 다른 값",
                "explanation": "항복강도는 소성변형 시작점, 인장강도는 최대 하중점입니다"
            },
            {
                "mistake": "연신율을 '늘어난 길이'로만 표현",
                "correction": "'tỷ lệ dãn dài (%)'로 백분율 표시",
                "explanation": "연신율은 원래 길이 대비 늘어난 비율입니다"
            }
        ],
        "examples": [
            {
                "ko": "이 철근은 인장시험 결과 항복강도가 420MPa입니다",
                "vi": "Thép này có độ bền chảy 420MPa theo kết quả thí nghiệm kéo",
                "situation": "formal"
            },
            {
                "ko": "용접부 인장시험 샘플 3개 준비해주세요",
                "vi": "Chuẩn bị 3 mẫu thí nghiệm kéo mối hàn",
                "situation": "onsite"
            },
            {
                "ko": "인장시험 했더니 연신율이 기준 미달이네요",
                "vi": "Sau thí nghiệm kéo thì tỷ lệ dãn dài không đạt tiêu chuẩn",
                "situation": "informal"
            }
        ],
        "relatedTerms": ["độ bền kéo (인장강도)", "độ bền chảy (항복강도)", "tỷ lệ dãn dài (연신율)", "cốt thép (철근)"]
    },
    {
        "slug": "thi-nghiem-uon",
        "korean": "휨시험",
        "vietnamese": "thí nghiệm uốn",
        "hanja": "휨試驗",
        "hanjaReading": "휨(고유어, 한자 없음) + 試(시험할 시) + 驗(시험할 험)",
        "pronunciation": "휨시험 [tí nggiẹm uốn]",
        "meaningKo": "콘크리트 슬래브, 보, 아스팔트 등의 휨에 대한 저항력을 측정하는 시험입니다. 통역 시 '휨강도(cường độ uốn)'와 구분해야 하며, 3점 재하 방식과 4점 재하 방식을 명확히 구분하여 통역해야 합니다. 도로 포장 콘크리트의 경우 휨강도가 압축강도보다 중요한 설계 기준이 되므로, 베트남 현장에서는 이를 강조하여 통역해야 합니다. 시험 결과는 MPa 단위로 표현되며 일반적으로 압축강도의 1/10 수준입니다.",
        "meaningVi": "Thí nghiệm xác định khả năng chống uốn của vật liệu như bê tông sàn, dầm, nhựa đường. Có hai phương pháp: tải trọng 3 điểm và 4 điểm. Đối với bê tông mặt đường, cường độ uốn quan trọng hơn cường độ nén trong thiết kế. Kết quả đo bằng MPa, thường bằng 1/10 cường độ nén.",
        "context": "도로 포장 콘크리트, 슬래브 품질 검사",
        "culturalNote": "한국은 KS F 2408(콘크리트 휨강도 시험)을 따르고 베트남은 TCVN 3119를 따릅니다. 한국 도로 현장에서는 휨강도 4.5MPa를 기준으로 하는 경우가 많지만 베트남은 4.0MPa를 기준으로 하는 경우가 많습니다. 또한 한국은 150×150×550mm 공시체를 주로 사용하지만 베트남은 100×100×400mm도 사용하므로 통역 시 규격을 명확히 해야 합니다.",
        "commonMistakes": [
            {
                "mistake": "'thí nghiệm gấp'으로 번역",
                "correction": "'thí nghiệm uốn'이 표준 기술 용어",
                "explanation": "'gấp'은 종이 접기 같은 행위, 'uốn'은 힘에 의한 휨을 의미합니다"
            },
            {
                "mistake": "3점 재하와 4점 재하를 구분하지 않음",
                "correction": "'tải trọng 3 điểm', 'tải trọng 4 điểm'으로 명확히 구분",
                "explanation": "재하 방식에 따라 응력 분포가 다르므로 구분 필수입니다"
            },
            {
                "mistake": "휨강도를 압축강도와 동일 수준으로 이해",
                "correction": "휨강도는 압축강도의 약 1/10 수준임을 설명",
                "explanation": "수치 차이가 크므로 혼동 방지가 중요합니다"
            }
        ],
        "examples": [
            {
                "ko": "도로 포장 콘크리트 휨시험 결과가 4.2MPa로 합격입니다",
                "vi": "Kết quả thí nghiệm uốn bê tông mặt đường đạt 4.2MPa, đạt yêu cầu",
                "situation": "formal"
            },
            {
                "ko": "휨시험용 공시체 제작 좀 서둘러주세요",
                "vi": "Hãy nhanh chóng chế tạo mẫu thử cho thí nghiệm uốn",
                "situation": "onsite"
            },
            {
                "ko": "이번 배치는 휨강도가 좀 낮게 나왔네요",
                "vi": "Mẻ này có cường độ uốn hơi thấp",
                "situation": "informal"
            }
        ],
        "relatedTerms": ["cường độ uốn (휨강도)", "bê tông mặt đường (도로 포장 콘크리트)", "tải trọng (재하)", "mẫu thử (공시체)"]
    },
    {
        "slug": "do-sut",
        "korean": "슬럼프시험",
        "vietnamese": "độ sụt",
        "hanja": None,
        "hanjaReading": None,
        "pronunciation": "슬럼프시험 [độ sụt]",
        "meaningKo": "아직 굳지 않은 콘크리트의 반죽 질기(연경도)를 측정하는 시험으로, 슬럼프 콘(원뿔형 틀)에 콘크리트를 채운 후 빼내어 주저앉은 정도를 mm 단위로 측정합니다. 통역 시 '워커빌리티(tính thi công)', '배합(phối trộn)', '물-시멘트비(tỷ lệ nước/xi măng)'와 함께 자주 사용되므로 이들 용어를 숙지해야 합니다. 베트남 현장에서는 일반 콘크리트 슬럼프 기준이 80~180mm이며, 펌프카 타설 시에는 150mm 이상을 요구하는 경우가 많습니다.",
        "meaningVi": "Thí nghiệm đo độ sụt của bê tông tươi để xác định độ dẻo (workability). Sử dụng phễu hình nón (slump cone), đổ đầy bê tông rồi nhấc lên để đo độ sụt xuống tính bằng mm. Tiêu chuẩn độ sụt thông thường là 80~180mm, khi đổ bằng máy bơm thì yêu cầu ≥150mm. Độ sụt liên quan đến tỷ lệ nước/xi măng và tính thi công.",
        "context": "콘크리트 타설 전 현장 품질 관리",
        "culturalNote": "한국은 KS F 2402(콘크리트 슬럼프 시험)를 따르고 베트남은 TCVN 3106을 따릅니다. 한국 현장에서는 슬럼프 값을 엄격히 관리하지만 베트남 현장에서는 날씨(특히 더위)로 인해 현장에서 물을 추가하는 경우가 종종 있어 품질 관리에 주의가 필요합니다. 또한 한국은 '슬럼프'라는 외래어를 그대로 사용하지만 베트남은 'độ sụt'라는 베트남어 표현을 주로 사용합니다.",
        "commonMistakes": [
            {
                "mistake": "'thí nghiệm slump'라고 영어를 그대로 사용",
                "correction": "'độ sụt' 또는 'thí nghiệm độ sụt'",
                "explanation": "베트남 현장에서는 베트남어 용어를 선호합니다"
            },
            {
                "mistake": "슬럼프가 높으면 '강도가 높다'고 오해",
                "correction": "슬럼프는 '시공성'이지 '강도'가 아님",
                "explanation": "오히려 슬럼프가 너무 높으면 강도가 낮아질 수 있습니다"
            },
            {
                "mistake": "현장 물 추가를 그냥 허용하도록 통역",
                "correction": "물 추가는 강도 저하 원인임을 명확히 전달",
                "explanation": "무분별한 물 추가는 품질 저하의 주요 원인입니다"
            }
        ],
        "examples": [
            {
                "ko": "이 레미콘은 슬럼프가 150mm로 기준에 적합합니다",
                "vi": "Bê tông thương phẩm này có độ sụt 150mm, đạt tiêu chuẩn",
                "situation": "formal"
            },
            {
                "ko": "슬럼프 너무 낮은데 물 좀 더 넣어도 될까요?",
                "vi": "Độ sụt quá thấp, có được thêm nước không?",
                "situation": "onsite"
            },
            {
                "ko": "더워서 슬럼프가 금방 떨어지네요",
                "vi": "Nóng quá nên độ sụt giảm nhanh",
                "situation": "informal"
            }
        ],
        "relatedTerms": ["bê tông tươi (생콘크리트)", "tính thi công (워커빌리티)", "tỷ lệ nước/xi măng (물-시멘트비)", "máy bơm bê tông (콘크리트 펌프카)"]
    },
    {
        "slug": "mau-thu",
        "korean": "시험편/공시체",
        "vietnamese": "mẫu thử",
        "hanja": "試驗片/供試體",
        "hanjaReading": "試(시험할 시) + 驗(시험할 험) + 片(조각 편) / 供(이바지할 공) + 試(시험할 시) + 體(몸 체)",
        "pronunciation": "시험편/공시체 [머우 tử]",
        "meaningKo": "콘크리트, 철근, 토양 등의 재료 시험을 위해 규격에 맞게 제작하거나 채취한 샘플입니다. 통역 시 '공시체'는 주로 콘크리트에 사용하고 '시험편'은 철근이나 금속에 사용하는 경향이 있으나, 베트남에서는 'mẫu thử'로 통일하여 사용합니다. 공시체 제작 시 다짐(đầm), 양생(bảo dưỡng), 표면 처리(xử lý bề mặt) 등의 절차가 중요하며, 통역 시 이를 정확히 전달해야 합니다. 시험 결과의 신뢰도는 공시체 제작 품질에 크게 좌우됩니다.",
        "meaningVi": "Mẫu vật liệu như bê tông, thép, đất được chế tạo hoặc lấy theo quy cách để thí nghiệm. Phải tuân thủ quy trình đầm, bảo dưỡng, xử lý bề mặt. Chất lượng chế tạo mẫu thử quyết định độ tin cậy của kết quả thí nghiệm. Đối với bê tông thường dùng hình trụ Ø100×200mm hoặc khối 150×150×150mm.",
        "context": "모든 건설 재료 품질 시험",
        "culturalNote": "한국은 원주형 공시체(Ø100×200mm)를 표준으로 하지만 베트남은 정육면체(150×150×150mm)도 많이 사용합니다. 양생 조건도 한국은 수중 양생(20±2℃)을 엄격히 하지만 베트남 현장에서는 습윤 양생이나 자연 양생을 하는 경우가 많아 시험 결과에 영향을 줄 수 있습니다. 통역 시 공시체 규격과 양생 조건을 반드시 확인해야 합니다.",
        "commonMistakes": [
            {
                "mistake": "'mẫu'만 단독으로 사용",
                "correction": "'mẫu thử'로 정확히 표현",
                "explanation": "'mẫu'는 일반적인 샘플, 'mẫu thử'는 시험용 샘플입니다"
            },
            {
                "mistake": "공시체와 시험편을 다르게 번역하려고 시도",
                "correction": "베트남어에서는 둘 다 'mẫu thử'로 통일",
                "explanation": "한국어의 구분이 베트남어에는 없으므로 맥락으로 구분합니다"
            },
            {
                "mistake": "양생 조건을 생략하고 통역",
                "correction": "양생 방법(수중/습윤/자연)과 기간을 명시",
                "explanation": "양생 조건이 다르면 시험 결과도 달라집니다"
            }
        ],
        "examples": [
            {
                "ko": "28일 압축시험용 공시체 9개를 제작해주세요",
                "vi": "Chế tạo 9 mẫu thử cho thí nghiệm nén 28 ngày",
                "situation": "formal"
            },
            {
                "ko": "공시체 표면이 매끄럽지 않은데 괜찮나요?",
                "vi": "Bề mặt mẫu thử không nhẵn, có được không?",
                "situation": "onsite"
            },
            {
                "ko": "이 공시체들은 수중 양생 중입니다",
                "vi": "Các mẫu thử này đang được bảo dưỡng trong nước",
                "situation": "informal"
            }
        ],
        "relatedTerms": ["bảo dưỡng (양생)", "thí nghiệm (시험)", "quy cách (규격)", "đầm (다짐)"]
    },
    {
        "slug": "ket-qua-thi-nghiem",
        "korean": "시험결과",
        "vietnamese": "kết quả thí nghiệm",
        "hanja": "試驗結果",
        "hanjaReading": "試(시험할 시) + 驗(시험할 험) + 結(맺을 결) + 果(열매 과)",
        "pronunciation": "시험결과 [껫 꽈 tí nggiẹm]",
        "meaningKo": "재료 시험을 수행한 후 얻어진 측정값과 분석 결과를 의미하며, 일반적으로 시험 성적서(giấy chứng nhận thí nghiệm) 형태로 문서화됩니다. 통역 시 합격/불합격(đạt/không đạt), 설계 기준(tiêu chuẩn thiết kế), 평균값(giá trị trung bình), 표준편차(độ lệch chuẩn) 등의 용어와 함께 사용됩니다. 베트남 현장에서는 시험 결과를 감리(giám sát)와 발주처(chủ đầu tư)에게 동시에 제출해야 하므로, 통역 시 보고 경로를 명확히 해야 합니다.",
        "meaningVi": "Giá trị đo và phân tích thu được sau khi thực hiện thí nghiệm vật liệu, thường được lập thành giấy chứng nhận thí nghiệm. Bao gồm các thuật ngữ như đạt/không đạt yêu cầu, tiêu chuẩn thiết kế, giá trị trung bình, độ lệch chuẩn. Kết quả phải được nộp cho giám sát và chủ đầu tư.",
        "context": "품질 관리 보고서, 감리 보고",
        "culturalNote": "한국은 시험 결과를 시험실에서 즉시 전산 입력하여 관계자가 실시간으로 확인할 수 있지만, 베트남은 여전히 종이 문서로 제출하는 경우가 많습니다. 또한 한국은 부적합 발생 시 즉시 재시험을 하지만 베트남은 감리나 발주처의 승인을 받아야 하는 경우가 있어 절차가 다릅니다. 통역 시 이러한 절차 차이를 이해하고 설명해야 합니다.",
        "commonMistakes": [
            {
                "mistake": "'kết quả test'로 영어 혼용",
                "correction": "'kết quả thí nghiệm'으로 정확히",
                "explanation": "공식 문서에서는 베트남어 표준 용어를 사용해야 합니다"
            },
            {
                "mistake": "합격/불합격을 'OK/NG'로 표현",
                "correction": "'đạt yêu cầu/không đạt yêu cầu'로 명확히",
                "explanation": "공식 보고서에서는 정식 용어를 사용해야 합니다"
            },
            {
                "mistake": "시험 결과만 통역하고 조치 사항은 생략",
                "correction": "부적합 시 재시험이나 보강 조치도 함께 통역",
                "explanation": "결과와 후속 조치는 항상 함께 논의됩니다"
            }
        ],
        "examples": [
            {
                "ko": "압축시험 결과가 모두 설계강도를 상회합니다",
                "vi": "Kết quả thí nghiệm nén đều vượt cường độ thiết kế",
                "situation": "formal"
            },
            {
                "ko": "시험 결과 나오는 대로 바로 보내주세요",
                "vi": "Có kết quả thí nghiệm thì gửi ngay cho tôi",
                "situation": "onsite"
            },
            {
                "ko": "이번 결과는 좀 애매한데 재시험 해야 할 것 같아요",
                "vi": "Kết quả lần này hơi애매하다, có lẽ phải thí nghiệm lại",
                "situation": "informal"
            }
        ],
        "relatedTerms": ["giấy chứng nhận thí nghiệm (시험 성적서)", "đạt yêu cầu (합격)", "không đạt (불합격)", "tiêu chuẩn thiết kế (설계 기준)"]
    },
    {
        "slug": "phong-thi-nghiem",
        "korean": "시험실",
        "vietnamese": "phòng thí nghiệm",
        "hanja": "試驗室",
        "hanjaReading": "試(시험할 시) + 驗(시험할 험) + 室(집 실)",
        "pronunciation": "시험실 [퐁 tí nggiẹm]",
        "meaningKo": "건설 재료의 품질 시험을 수행하는 시설로, 압축시험기, 인장시험기, 항온항습실 등의 장비를 갖추고 있습니다. 통역 시 '공인시험실(phòng thí nghiệm được công nhận)', '현장시험실(phòng thí nghiệm công trường)', '외부 의뢰(ủy thác bên ngoài)' 등을 구분해야 합니다. 베트남 현장에서는 시험실 인증(VILAS 또는 국제 인증)을 중요하게 여기므로, 통역 시 시험실의 공신력을 강조해야 하는 경우가 많습니다.",
        "meaningVi": "Cơ sở thực hiện thí nghiệm chất lượng vật liệu xây dựng, trang bị máy thí nghiệm nén, máy kéo, phòng bảo dưỡng nhiệt độ-độ ẩm. Phân biệt phòng thí nghiệm được công nhận (VILAS hoặc quốc tế), phòng thí nghiệm công trường, và ủy thác bên ngoài. Uy tín phòng thí nghiệm rất quan trọng trong nghiệm thu.",
        "context": "품질 관리 계획, 시험 의뢰",
        "culturalNote": "한국은 KS 인증 시험실이나 국가공인시험기관을 선호하지만, 베트남은 VILAS(Vietnam Laboratory Accreditation Scheme) 인증을 요구합니다. 또한 한국은 대형 프로젝트에서 현장 시험실을 운영하는 경우가 많지만 베트남은 외부 시험실에 의뢰하는 것이 일반적입니다. 통역 시 시험 결과의 공신력과 관련하여 시험실 인증 여부를 명확히 해야 합니다.",
        "commonMistakes": [
            {
                "mistake": "'lab'이라고 영어로만 표현",
                "correction": "'phòng thí nghiệm'으로 정확히",
                "explanation": "공식 문서와 회의에서는 베트남어를 사용해야 합니다"
            },
            {
                "mistake": "현장시험실과 공인시험실을 구분하지 않음",
                "correction": "공인 여부를 명확히 표현",
                "explanation": "시험 결과의 법적 효력이 다릅니다"
            },
            {
                "mistake": "시험실 인증을 단순히 '자격증'으로 번역",
                "correction": "'công nhận' 또는 'chứng nhận ISO/VILAS'",
                "explanation": "인증 종류에 따라 공신력이 다릅니다"
            }
        ],
        "examples": [
            {
                "ko": "이 시험실은 VILAS 인증을 받은 공인시험실입니다",
                "vi": "Phòng thí nghiệm này được công nhận VILAS",
                "situation": "formal"
            },
            {
                "ko": "현장 시험실에서 슬럼프 측정하고 공인시험실로 공시체 보내세요",
                "vi": "Đo độ sụt ở phòng thí nghiệm công trường rồi gửi mẫu thử đến phòng thí nghiệm được công nhận",
                "situation": "onsite"
            },
            {
                "ko": "시험실 장비 교정 언제 했어요?",
                "vi": "Thiết bị phòng thí nghiệm hiệu chuẩn lần cuối khi nào?",
                "situation": "informal"
            }
        ],
        "relatedTerms": ["được công nhận (인증받은)", "thiết bị thí nghiệm (시험 장비)", "hiệu chuẩn (교정)", "VILAS (베트남 시험실 인증 제도)"]
    },
    {
        "slug": "chung-chi-chat-luong",
        "korean": "품질인증서",
        "vietnamese": "chứng chỉ chất lượng",
        "hanja": "品質認證書",
        "hanjaReading": "品(물건 품) + 質(바탕 질) + 認(알 인) + 證(증거 증) + 書(글 서)",
        "pronunciation": "품질인증서 [청 chỉ 챳 르엉]",
        "meaningKo": "건설 자재나 완성된 구조물이 규정된 품질 기준을 충족함을 증명하는 공식 문서입니다. 통역 시 '밀시트(mill sheet, giấy chứng nhận nhà máy)', '시험성적서(giấy chứng nhận thí nghiệm)', 'KS 인증(chứng nhận KS)' 등과 구분해야 합니다. 베트남 현장에서는 수입 자재의 경우 원산지 증명(giấy chứng nhận xuất xứ)과 품질인증서를 함께 요구하며, 감리 승인 없이는 자재를 반입할 수 없으므로 통역 시 서류 제출 절차를 명확히 해야 합니다.",
        "meaningVi": "Văn bản chính thức chứng minh vật liệu xây dựng hoặc công trình đạt tiêu chuẩn chất lượng quy định. Cần phân biệt với giấy chứng nhận nhà máy (mill sheet), giấy chứng nhận thí nghiệm, chứng nhận KS. Đối với vật liệu nhập khẩu cần có cả giấy chứng nhận xuất xứ. Không được đưa vật liệu vào công trường nếu chưa được giám sát phê duyệt.",
        "context": "자재 반입, 준공 서류",
        "culturalNote": "한국은 KS 마크나 단체표준 인증을 중요시하지만 베트남은 TCVN(베트남 국가 표준) 인증이나 제조사 자체 품질보증서를 주로 사용합니다. 또한 한국은 전자 문서를 많이 사용하지만 베트남은 여전히 원본 서류에 직인(con dấu)을 찍은 것을 요구하는 경우가 많습니다. 통역 시 문서의 법적 효력과 제출 형식을 명확히 해야 합니다.",
        "commonMistakes": [
            {
                "mistake": "'certificate'를 영어 그대로 사용",
                "correction": "'chứng chỉ' 또는 'giấy chứng nhận'",
                "explanation": "공식 문서명은 베트남어를 사용해야 합니다"
            },
            {
                "mistake": "밀시트와 품질인증서를 혼동",
                "correction": "밀시트는 제조사 발행, 품질인증서는 제3자 인증",
                "explanation": "발행 주체와 법적 효력이 다릅니다"
            },
            {
                "mistake": "전자 문서로 제출 가능하다고 오해",
                "correction": "원본 서류(직인 날인) 필요 여부 확인",
                "explanation": "베트남은 원본 서류를 요구하는 경우가 많습니다"
            }
        ],
        "examples": [
            {
                "ko": "이 철근은 KS 인증 품질인증서가 있습니까?",
                "vi": "Thép này có chứng chỉ chất lượng KS không?",
                "situation": "formal"
            },
            {
                "ko": "품질인증서 없으면 자재 반입 안 됩니다",
                "vi": "Không có chứng chỉ chất lượng thì không được đưa vật liệu vào",
                "situation": "onsite"
            },
            {
                "ko": "품질인증서 사본이라도 먼저 보내주세요",
                "vi": "Gửi bản sao chứng chỉ chất lượng trước cũng được",
                "situation": "informal"
            }
        ],
        "relatedTerms": ["giấy chứng nhận nhà máy (밀시트)", "chứng nhận KS (KS 인증)", "giấy chứng nhận xuất xứ (원산지 증명)", "con dấu (직인)"]
    },
    {
        "slug": "kiem-dinh-vat-lieu",
        "korean": "자재검정",
        "vietnamese": "kiểm định vật liệu",
        "hanja": "資材檢定",
        "hanjaReading": "資(재물 자) + 材(재목 재) + 檢(검사할 검) + 定(정할 정)",
        "pronunciation": "자재검정 [끼엠 띤 밧 리에우]",
        "meaningKo": "건설 현장에 반입되는 자재가 설계 도서와 시방서에 명시된 품질 기준을 충족하는지 검사하고 승인하는 절차입니다. 통역 시 '사전승인(phê duyệt trước)', '샘플 승인(duyệt mẫu)', '현장 검수(nghiệm thu tại công trường)' 등의 단계를 구분해야 합니다. 베트남 현장에서는 감리(giám sát)의 자재검정 승인 없이는 시공을 진행할 수 없으며, 특히 주요 구조 자재(철근, 시멘트, 레미콘)는 반드시 검정을 거쳐야 하므로 통역 시 이를 강조해야 합니다.",
        "meaningVi": "Quy trình kiểm tra và phê duyệt vật liệu đưa vào công trường có đạt tiêu chuẩn chất lượng trong hồ sơ thiết kế và thuyết minh kỹ thuật hay không. Phân biệt các bước: phê duyệt trước, duyệt mẫu, nghiệm thu tại công trường. Không được thi công nếu chưa có phê duyệt kiểm định vật liệu của giám sát, đặc biệt với vật liệu kết cấu chính (cốt thép, xi măng, bê tông).",
        "context": "시공 전 자재 관리",
        "culturalNote": "한국은 자재검정을 감리가 주도하지만 베트남은 감리와 발주처(chủ đầu tư)가 공동으로 승인하는 경우가 많습니다. 또한 한국은 자재검정 서류를 전산으로 관리하지만 베트남은 종이 문서로 제출하고 직인을 받는 방식이 일반적입니다. 통역 시 승인 권한과 절차를 명확히 하지 않으면 시공이 지연될 수 있으므로 주의가 필요합니다.",
        "commonMistakes": [
            {
                "mistake": "'test vật liệu'로 영어 혼용",
                "correction": "'kiểm định vật liệu'가 정확한 용어",
                "explanation": "검정은 단순 시험이 아닌 승인 절차까지 포함합니다"
            },
            {
                "mistake": "자재검정과 자재시험을 같은 것으로 이해",
                "correction": "검정은 승인 절차, 시험은 측정 행위",
                "explanation": "시험 결과를 바탕으로 검정(승인)이 이루어집니다"
            },
            {
                "mistake": "구두 승인으로 충분하다고 오해",
                "correction": "반드시 문서(직인 포함)로 승인받아야 함",
                "explanation": "베트남은 문서 증빙을 매우 중요시합니다"
            }
        ],
        "examples": [
            {
                "ko": "철근 자재검정 서류를 감리에게 제출해주십시오",
                "vi": "Vui lòng nộp hồ sơ kiểm định vật liệu thép cho giám sát",
                "situation": "formal"
            },
            {
                "ko": "이 시멘트는 아직 자재검정 안 받았으니 사용하지 마세요",
                "vi": "Xi măng này chưa được kiểm định nên không được sử dụng",
                "situation": "onsite"
            },
            {
                "ko": "자재검정 빨리 받아야 공정이 안 밀리는데요",
                "vi": "Phải kiểm định vật liệu nhanh thì mới không trễ tiến độ",
                "situation": "informal"
            }
        ],
        "relatedTerms": ["phê duyệt (승인)", "giám sát (감리)", "hồ sơ thiết kế (설계 도서)", "thuyết minh kỹ thuật (시방서)"]
    },
    {
        "slug": "do-ben",
        "korean": "내구성",
        "vietnamese": "độ bền",
        "hanja": "耐久性",
        "hanjaReading": "耐(견딜 내) + 久(오랠 구) + 性(성품 성)",
        "pronunciation": "내구성 [độ 번]",
        "meaningKo": "건설 재료나 구조물이 시간이 지나도 물리적, 화학적 성능을 유지하는 능력으로, 수명(tuổi thọ)과 직결됩니다. 통역 시 '동결융해(đóng băng-tan băng)', '탄산화(cacbonat hóa)', '염해(ăn mòn do muối)', '중성화(trung hòa)' 등의 열화 요인과 함께 설명해야 합니다. 베트남은 열대 기후로 고온다습, 염해가 주요 내구성 저하 요인이므로, 한국과 다른 환경 조건을 고려하여 통역해야 합니다. 특히 해안 지역 프로젝트에서는 염해 대책(피복 두께, 방청 처리)을 반드시 확인해야 합니다.",
        "meaningVi": "Khả năng duy trì tính năng vật lý, hóa học của vật liệu xây dựng hoặc công trình theo thời gian, liên quan trực tiếp đến tuổi thọ. Các yếu tố làm giảm độ bền: đóng băng-tan băng (ít gặp ở VN), cacbonat hóa, ăn mòn do muối, trung hòa. Việt Nam có khí hậu nhiệt đới ẩm nóng nên ăn mòn do muối là vấn đề chính, đặc biệt ở vùng ven biển. Cần chú ý lớp bảo vệ cốt thép và xử lý chống rỉ.",
        "context": "설계, 유지보수 계획",
        "culturalNote": "한국은 동결융해와 탄산화를 주요 내구성 저하 요인으로 다루지만, 베트남은 동결이 없고 대신 고온다습과 염해가 주요 문제입니다. 설계 기준 수명도 한국은 일반 건축물 50년, 특수 구조물 100년을 기준으로 하지만 베트남은 명확한 기준이 없는 경우가 많아 통역 시 명시적으로 확인해야 합니다. 또한 유지보수 개념이 한국보다 약해 내구성 설계의 중요성을 강조하는 것이 필요합니다.",
        "commonMistakes": [
            {
                "mistake": "'độ bền'을 단순히 '강도'로 이해",
                "correction": "강도(cường độ)는 즉시 성능, 내구성(độ bền)은 장기 성능",
                "explanation": "강도와 내구성은 다른 개념입니다"
            },
            {
                "mistake": "한국의 동결융해 기준을 베트남에 그대로 적용",
                "correction": "베트남은 동결이 없으므로 염해와 고온다습 대책 중심",
                "explanation": "기후 조건이 완전히 다릅니다"
            },
            {
                "mistake": "내구성을 단순히 'chất lượng tốt'으로 표현",
                "correction": "'độ bền' 또는 'khả năng chống lão hóa'",
                "explanation": "'좋은 품질'과 '내구성'은 다른 개념입니다"
            }
        ],
        "examples": [
            {
                "ko": "해안 지역이므로 염해에 대한 내구성 확보가 중요합니다",
                "vi": "Đây là khu vực ven biển nên việc đảm bảo độ bền chống ăn mòn muối rất quan trọng",
                "situation": "formal"
            },
            {
                "ko": "이 콘크리트는 내구성이 떨어져서 보수가 자주 필요해요",
                "vi": "Bê tông này độ bền kém nên phải sửa chữa thường xuyên",
                "situation": "onsite"
            },
            {
                "ko": "피복 두께를 늘려서 내구성을 높이는 게 어때요?",
                "vi": "Tăng độ dày lớp bảo vệ để nâng cao độ bền thì sao?",
                "situation": "informal"
            }
        ],
        "relatedTerms": ["tuổi thọ (수명)", "ăn mòn (부식)", "lớp bảo vệ cốt thép (피복)", "cacbonat hóa (탄산화)"]
    }
]

# 중복 제거
new_terms_filtered = [t for t in new_terms if t['slug'] not in existing_slugs]

# 데이터 추가
data.extend(new_terms_filtered)

# 저장
with open(file_path, 'w', encoding='utf-8') as f:
    json.dump(data, f, ensure_ascii=False, indent=2)

print(f"✅ {len(new_terms_filtered)}개 용어 추가 완료 (중복 제외)")
print(f"📁 파일: {file_path}")
print(f"📊 전체 용어 수: {len(data)}개")
