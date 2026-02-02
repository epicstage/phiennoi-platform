#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""환경분쟁법 용어 추가 스크립트 (v7-j)"""

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
            "slug": "danh-gia-tac-dong-moi-truong",
            "korean": "환경영향평가",
            "vietnamese": "Đánh giá tác động môi trường",
            "hanja": "環境影響評價",
            "hanjaReading": "環(둘러쌀 환) + 境(지경 경) + 影(그림자 영) + 響(울릴 향) + 評(평할 평) + 價(값 가)",
            "pronunciation": "환경영향평가",
            "meaningKo": "개발사업이 환경에 미치는 영향을 사전에 조사·예측·평가하여 환경보전방안을 마련하는 제도입니다. 통역 시 한국의 '전략환경영향평가'와 '환경영향평가'를 베트남의 'Đánh giá môi trường chiến lược'와 'Đánh giá tác động môi trường'으로 정확히 구분해야 합니다. 베트남에서는 환경부(Bộ Tài nguyên và Môi trường) 승인이 필수이며, 한국의 환경부 승인 절차와 유사하지만 평가 항목과 기준이 다릅니다.",
            "meaningVi": "Là chế độ điều tra, dự báo, đánh giá trước các tác động của dự án phát triển đến môi trường và xây dựng phương án bảo vệ môi trường. Ở Việt Nam, đây là thủ tục bắt buộc theo Luật Bảo vệ môi trường 2020, yêu cầu phê duyệt của Bộ Tài nguyên và Môi trường trước khi triển khai dự án.",
            "context": "환경법, 건설법, 개발사업",
            "culturalNote": "한국은 전략환경영향평가(정책·계획 단계)와 환경영향평가(사업 단계)로 이원화되어 있고, 소규모 사업은 '환경영향평가 약식절차'를 적용합니다. 베트남은 2020년 환경보호법 개정으로 평가 대상 사업 범위가 확대되었으며, 한국보다 주민 의견수렴 절차가 간소한 편입니다. 양국 모두 미이행 시 사업 중단·과태료 부과가 가능하지만, 베트남은 형사처벌 가능성이 더 높습니다.",
            "commonMistakes": [
                {
                    "mistake": "환경평가",
                    "correction": "환경영향평가",
                    "explanation": "정식 법률 용어는 '환경영향평가'이며, 줄여서 '환경평가'라고 하면 다른 환경 관련 평가(환경성 검토, 사전환경성 검토 등)와 혼동될 수 있습니다."
                },
                {
                    "mistake": "Đánh giá môi trường",
                    "correction": "Đánh giá tác động môi trường (ĐTM)",
                    "explanation": "'Đánh giá môi trường'는 일반적 환경평가를 의미하므로, 법률상 정식 용어인 'Đánh giá tác động môi trường' 또는 약어 'ĐTM'을 사용해야 합니다."
                },
                {
                    "mistake": "전략평가와 영향평가를 같은 의미로 통역",
                    "correction": "전략환경영향평가(SEA)와 환경영향평가(EIA)는 별개 제도",
                    "explanation": "한국은 정책·계획 단계의 '전략환경영향평가'와 사업 단계의 '환경영향평가'를 법적으로 구분하므로, 통역 시 명확히 구별해야 합니다."
                }
            ],
            "examples": [
                {
                    "ko": "이 건설 프로젝트는 환경영향평가 협의를 완료해야 착공할 수 있습니다.",
                    "vi": "Dự án xây dựng này phải hoàn thành thủ tục tham vấn đánh giá tác động môi trường mới được khởi công.",
                    "situation": "formal"
                },
                {
                    "ko": "환경영향평가서 초안에 대한 주민 설명회를 개최해야 합니다.",
                    "vi": "Cần tổ chức buổi thuyết minh cho người dân về bản dự thảo báo cáo đánh giá tác động môi trường.",
                    "situation": "onsite"
                },
                {
                    "ko": "환경부가 환경영향평가 보완 요청을 했어요.",
                    "vi": "Bộ Tài nguyên và Môi trường đã yêu cầu bổ sung báo cáo ĐTM.",
                    "situation": "informal"
                }
            ],
            "relatedTerms": ["전략환경영향평가", "환경보전방안", "사후환경관리"]
        },
        {
            "slug": "xa-thai-o-nhiem",
            "korean": "오염배출",
            "vietnamese": "Xả thải ô nhiễm",
            "hanja": "汚染排出",
            "hanjaReading": "汚(더러울 오) + 染(물들일 염) + 排(물리칠 배) + 出(날 출)",
            "pronunciation": "오염배출",
            "meaningKo": "사업장이나 시설에서 대기, 수질, 토양 등을 오염시키는 물질을 외부로 내보내는 행위입니다. 통역 시 한국의 '배출허용기준'과 베트남의 'Tiêu chuẩn xả thải'을 혼동하지 않도록 주의해야 하며, 한국은 배출시설 허가제, 베트남은 환경허가제(Giấy phép môi trường)로 운영됩니다. 불법 배출 시 양국 모두 형사처벌이 가능하지만, 베트남은 더 엄격한 처벌 규정을 두고 있습니다.",
            "meaningVi": "Là hành vi thải ra ngoài các chất gây ô nhiễm không khí, nước, đất từ cơ sở sản xuất hoặc cơ sở dịch vụ. Theo quy định của Việt Nam, mọi hoạt động xả thải phải có Giấy phép môi trường và tuân thủ các tiêu chuẩn xả thải quy định trong QCVN (Quy chuẩn kỹ thuật quốc gia).",
            "context": "환경법, 형사법, 산업법",
            "culturalNote": "한국은 '대기환경보전법', '물환경보전법', '토양환경보전법'으로 매체별 관리가 분리되어 있고, 배출시설 설치 전 허가나 신고가 필요합니다. 베트남은 2020년 환경보호법으로 통합 관리하며, 환경허가증(Giấy phép môi trường) 하나로 모든 배출을 규제합니다. 한국은 배출부과금 제도가 발달했지만, 베트남은 행정처분과 형사처벌 중심입니다.",
            "commonMistakes": [
                {
                    "mistake": "배출",
                    "correction": "오염배출",
                    "explanation": "단순히 '배출'이라고 하면 정상적인 배출과 오염배출을 구분할 수 없으므로, 환경법적 맥락에서는 '오염배출'로 명확히 해야 합니다."
                },
                {
                    "mistake": "Thải ô nhiễm",
                    "correction": "Xả thải ô nhiễm",
                    "explanation": "'Thải'만 쓰면 일반적인 배출을 의미하므로, 환경오염 맥락에서는 'Xả thải'(방출하다)를 함께 사용해야 합니다."
                },
                {
                    "mistake": "배출허가를 환경허가로 통역",
                    "correction": "한국의 배출시설 허가와 베트남의 환경허가는 범위가 다름",
                    "explanation": "한국의 배출시설 허가는 매체별(대기, 수질 등)이지만, 베트남의 Giấy phép môi trường은 통합 환경허가이므로 맥락에 맞게 구분해야 합니다."
                }
            ],
            "examples": [
                {
                    "ko": "이 공장은 배출허용기준을 초과하여 오염배출한 혐의로 고발되었습니다.",
                    "vi": "Nhà máy này đã bị tố cáo về việc xả thải ô nhiễm vượt quá tiêu chuẩn cho phép.",
                    "situation": "formal"
                },
                {
                    "ko": "오염배출 시설을 가동하려면 먼저 허가를 받아야 해요.",
                    "vi": "Muốn vận hành cơ sở xả thải ô nhiễm thì phải xin giấy phép trước.",
                    "situation": "informal"
                },
                {
                    "ko": "현장에서 오염배출 농도를 측정하겠습니다.",
                    "vi": "Chúng tôi sẽ đo nồng độ xả thải ô nhiễm tại hiện trường.",
                    "situation": "onsite"
                }
            ],
            "relatedTerms": ["배출허용기준", "환경오염", "배출시설"]
        },
        {
            "slug": "xu-ly-chat-thai",
            "korean": "폐기물처리",
            "vietnamese": "Xử lý chất thải",
            "hanja": "廢棄物處理",
            "hanjaReading": "廢(폐할 폐) + 棄(버릴 기) + 物(물건 물) + 處(곳 처) + 理(다스릴 리)",
            "pronunciation": "폐기물처리",
            "meaningKo": "사업장이나 일상생활에서 발생한 쓰레기를 수집, 운반, 재활용, 소각, 매립 등의 방법으로 처분하는 행위입니다. 통역 시 한국의 '생활폐기물'과 '사업장폐기물', '지정폐기물'을 베트남의 'Chất thải sinh hoạt', 'Chất thải công nghiệp', 'Chất thải nguy hại'로 정확히 구분해야 합니다. 한국은 폐기물관리법으로 상세히 규정하며, 베트남은 환경보호법 내에서 규율합니다.",
            "meaningVi": "Là hoạt động thu gom, vận chuyển, tái chế, đốt, chôn lấp các loại rác thải phát sinh từ sản xuất hoặc sinh hoạt hàng ngày. Việt Nam phân loại chất thải thành chất thải sinh hoạt, chất thải công nghiệp thông thường và chất thải nguy hại, mỗi loại có quy định xử lý riêng theo Luật Bảo vệ môi trường 2020.",
            "context": "환경법, 행정법, 산업법",
            "culturalNote": "한국은 폐기물을 생활·사업장·건설·지정폐기물로 4분류하고, 배출자 책임 원칙(EPR)이 강하며, 종량제 봉투와 분리배출이 일상화되어 있습니다. 베트남은 생활·공업·의료·유해폐기물로 구분하며, 분리배출 문화가 아직 정착 단계입니다. 한국은 민간 폐기물처리업체가 발달했지만, 베트남은 국영 기업 중심입니다. 불법 투기 시 양국 모두 처벌하지만, 베트남은 벌금액이 상대적으로 낮습니다.",
            "commonMistakes": [
                {
                    "mistake": "쓰레기 처리",
                    "correction": "폐기물처리",
                    "explanation": "법률 용어는 '폐기물'이며, '쓰레기'는 일상 구어체입니다. 법률 문서나 공식 통역에서는 '폐기물'을 사용해야 합니다."
                },
                {
                    "mistake": "Xử lý rác",
                    "correction": "Xử lý chất thải",
                    "explanation": "'Rác'는 일반적인 쓰레기를 뜻하므로, 법률 및 환경 분야에서는 'Chất thải'(폐기물)라는 정식 용어를 사용해야 합니다."
                },
                {
                    "mistake": "지정폐기물을 유해폐기물로 통역",
                    "correction": "한국의 지정폐기물은 베트남의 Chất thải nguy hại와 유사하지만 범위가 다름",
                    "explanation": "한국의 지정폐기물은 의료, 유해 등을 포함하지만, 베트남의 Chất thải nguy hại는 더 넓은 범위를 포함할 수 있으므로 맥락 확인이 필요합니다."
                }
            ],
            "examples": [
                {
                    "ko": "사업장에서 발생한 폐기물은 허가받은 처리업체에 위탁해야 합니다.",
                    "vi": "Chất thải phát sinh từ cơ sở sản xuất phải ủy thác cho đơn vị xử lý có giấy phép.",
                    "situation": "formal"
                },
                {
                    "ko": "이 폐기물처리 시설은 환경기준을 충족하나요?",
                    "vi": "Cơ sở xử lý chất thải này có đáp ứng tiêu chuẩn môi trường không?",
                    "situation": "onsite"
                },
                {
                    "ko": "폐기물처리 비용이 너무 비싸요.",
                    "vi": "Chi phí xử lý chất thải đắt quá.",
                    "situation": "informal"
                }
            ],
            "relatedTerms": ["지정폐기물", "재활용", "소각"]
        },
        {
            "slug": "tieng-on-va-rung-dong",
            "korean": "소음진동",
            "vietnamese": "Tiếng ồn và rung động",
            "hanja": "騷音振動",
            "hanjaReading": "騷(시끄러울 소) + 音(소리 음) + 振(떨칠 진) + 動(움직일 동)",
            "pronunciation": "소음진동",
            "meaningKo": "사람의 건강과 환경에 해를 끼칠 수 있는 시끄러운 소리와 물리적 진동을 의미하며, 공사장, 공장, 도로, 항공기 등에서 주로 발생합니다. 통역 시 한국의 '소음·진동관리법'과 베트남의 소음 규제(QCVN 26:2010 - Tiếng ồn)를 구분하고, 한국은 소음과 진동을 함께 규제하지만 베트남은 주로 소음 중심으로 규제한다는 점을 유의해야 합니다. 민원이 많은 분야로, 측정·평가 기준이 양국 간 차이가 있습니다.",
            "meaningVi": "Là âm thanh lớn và dao động vật lý có thể gây hại cho sức khỏe con người và môi trường, chủ yếu phát sinh từ công trường xây dựng, nhà máy, đường giao thông, máy bay. Việt Nam quy định tiêu chuẩn tiếng ồn qua QCVN 26:2010, tập trung vào quản lý tiếng ồn nhiều hơn rung động.",
            "context": "환경법, 건설법, 민원",
            "culturalNote": "한국은 '소음·진동관리법'으로 소음과 진동을 동시에 규제하며, 생활소음(이웃 간 층간소음 포함)과 공장·건설·교통소음을 구분합니다. 베트남은 소음(tiếng ồn) 규제가 주를 이루고, 진동(rung động)은 별도 규정이 약한 편입니다. 한국은 소음측정망이 전국적으로 구축되어 있고, 베트남은 도시 중심으로 측정이 이루어집니다. 한국은 층간소음 이웃분쟁이 많지만, 베트남은 공사장·교통소음 민원이 더 많습니다.",
            "commonMistakes": [
                {
                    "mistake": "소음",
                    "correction": "소음진동",
                    "explanation": "법률상으로는 '소음진동'이 정식 용어이며, 소음만 언급하면 진동 규제가 누락될 수 있습니다."
                },
                {
                    "mistake": "Tiếng ồn",
                    "correction": "Tiếng ồn và rung động",
                    "explanation": "한국어 '소음진동'은 소음과 진동 모두를 포함하므로, 베트남어로도 'và rung động'을 함께 표기해야 정확합니다."
                },
                {
                    "mistake": "dB(A)를 dB로 통역",
                    "correction": "소음 단위는 dB(A), 진동은 dB(V)",
                    "explanation": "소음은 A-가중치 데시벨 dB(A), 진동은 진동가속도레벨 dB(V)로 단위가 다르므로 혼동하지 않아야 합니다."
                }
            ],
            "examples": [
                {
                    "ko": "이 건설 현장은 소음진동 규제기준을 초과하여 공사 중지 명령을 받았습니다.",
                    "vi": "Công trường xây dựng này đã nhận lệnh đình chỉ thi công do vượt quá tiêu chuẩn quy định về tiếng ồn và rung động.",
                    "situation": "formal"
                },
                {
                    "ko": "밤에 공사하면 소음진동 민원이 들어올 수 있어요.",
                    "vi": "Nếu thi công ban đêm có thể bị khiếu nại về tiếng ồn và rung động.",
                    "situation": "informal"
                },
                {
                    "ko": "소음진동 측정 장비를 현장에 설치하겠습니다.",
                    "vi": "Chúng tôi sẽ lắp đặt thiết bị đo tiếng ồn và rung động tại hiện trường.",
                    "situation": "onsite"
                }
            ],
            "relatedTerms": ["생활소음", "공사소음", "교통소음"]
        },
        {
            "slug": "o-nhiem-dat",
            "korean": "토양오염",
            "vietnamese": "Ô nhiễm đất",
            "hanja": "土壤汚染",
            "hanjaReading": "土(흙 토) + 壤(흙 양) + 汚(더러울 오) + 染(물들일 염)",
            "pronunciation": "토양오염",
            "meaningKo": "토양에 유해물질이 침투하여 인간이나 동식물에 해를 끼치는 상태로, 주로 공장 폐수, 농약, 중금속, 유류 유출 등으로 발생합니다. 통역 시 한국의 '토양환경보전법'과 '토양오염 우려기준·대책기준'을 베트남의 'QCVN 03:2015 (Chất lượng đất)'과 구분하고, 한국은 오염 토양 정화 의무가 강하지만 베트남은 제도가 아직 발전 중임을 인지해야 합니다. 오염 원인자 책임 원칙이 양국 모두 적용됩니다.",
            "meaningVi": "Là tình trạng đất bị xâm nhập các chất độc hại gây hại cho con người và động thực vật, chủ yếu do nước thải công nghiệp, thuốc trừ sâu, kim loại nặng, tràn dầu. Việt Nam quy định chất lượng đất qua QCVN 03:2015, nhưng chế độ xử lý và phục hồi đất ô nhiễm còn đang trong giai đoạn phát triển.",
            "context": "환경법, 농업법, 산업법",
            "culturalNote": "한국은 '토양환경보전법'으로 토양오염 관리 지역을 지정하고, 오염 원인자에게 정화 의무를 부과하며, 정화 비용이 매우 높습니다. 전국 토양측정망을 운영하고, 특정토양오염관리대상시설(주유소, 세탁소 등)을 지정 관리합니다. 베트남은 농업용 토양과 산업용 토양을 구분하며, 토양오염 정화 기술과 제도가 한국보다 덜 발달했습니다. 한국은 부동산 거래 시 토양오염 조사가 일반화되었지만, 베트남은 아직 선택적입니다.",
            "commonMistakes": [
                {
                    "mistake": "땅 오염",
                    "correction": "토양오염",
                    "explanation": "법률 용어는 '토양'이며, '땅'은 일상 구어체입니다. 환경법 맥락에서는 반드시 '토양'을 사용해야 합니다."
                },
                {
                    "mistake": "Ô nhiễm đất đai",
                    "correction": "Ô nhiễm đất",
                    "explanation": "'Đất đai'는 토지(재산) 개념이고, 환경 분야에서는 'Đất'(토양)만 사용합니다."
                },
                {
                    "mistake": "우려기준과 대책기준을 같은 의미로 통역",
                    "correction": "우려기준은 조사 기준, 대책기준은 정화 기준",
                    "explanation": "한국 토양환경보전법상 '우려기준' 초과 시 정밀조사, '대책기준' 초과 시 즉시 정화 명령이므로 명확히 구분해야 합니다."
                }
            ],
            "examples": [
                {
                    "ko": "이 부지는 토양오염 대책기준을 초과하여 정화 명령을 받았습니다.",
                    "vi": "Khu đất này đã nhận lệnh xử lý do vượt quá tiêu chu�n đối sách về ô nhiễm đất.",
                    "situation": "formal"
                },
                {
                    "ko": "공장 부지에서 토양오염이 발견되면 정화 비용이 엄청나요.",
                    "vi": "Nếu phát hiện ô nhiễm đất tại khu nhà máy thì chi phí xử lý rất lớn.",
                    "situation": "informal"
                },
                {
                    "ko": "토양오염 조사를 위해 시료를 채취하겠습니다.",
                    "vi": "Chúng tôi sẽ lấy mẫu để điều tra ô nhiễm đất.",
                    "situation": "onsite"
                }
            ],
            "relatedTerms": ["중금속오염", "유류오염", "토양정화"]
        },
        {
            "slug": "o-nhiem-nuoc",
            "korean": "수질오염",
            "vietnamese": "Ô nhiễm nước",
            "hanja": "水質汚染",
            "hanjaReading": "水(물 수) + 質(바탕 질) + 汚(더러울 오) + 染(물들일 염)",
            "pronunciation": "수질오염",
            "meaningKo": "하천, 호소, 바다 등의 물에 유해물질이 유입되어 물의 질이 저하되는 현상으로, 공장 폐수, 생활하수, 농업용수, 기름 유출 등이 원인입니다. 통역 시 한국의 '물환경보전법'과 '수질 및 수생태계 보전에 관한 법률'을 베트남의 'Luật Tài nguyên nước'와 구분하고, 한국은 4대강 물환경 관리, 베트남은 메콩강·홍강 중심 관리를 이해해야 합니다. BOD, COD 등 수질 지표를 정확히 통역해야 합니다.",
            "meaningVi": "Là hiện tượng chất lượng nước bị giảm sút do các chất độc hại xâm nhập vào sông, hồ, biển, nguyên nhân chủ yếu từ nước thải công nghiệp, nước thải sinh hoạt, nước nông nghiệp, tràn dầu. Việt Nam quản lý chất lượng nước qua Luật Tài nguyên nước và các QCVN về nước mặt, nước ngầm.",
            "context": "환경법, 수자원법, 산업법",
            "culturalNote": "한국은 '물환경보전법'으로 하천·호소·해역을 통합 관리하며, 총량관리제(오염총량제)를 시행합니다. 4대강(한강, 금강, 낙동강, 영산강) 물환경 관리가 체계적이며, 상수원보호구역 지정이 엄격합니다. 베트남은 메콩강 삼각주와 홍강 유역을 중심으로 관리하며, 산업단지 폐수와 생활하수 처리 인프라가 아직 부족합니다. 한국은 폐수 배출 사업장에 대한 처벌이 강하지만, 베트남은 단속이 상대적으로 느슨한 편입니다.",
            "commonMistakes": [
                {
                    "mistake": "물 오염",
                    "correction": "수질오염",
                    "explanation": "법률 용어는 '수질'이며, '물'은 일반 표현입니다. 환경법에서는 '수질오염'을 사용해야 합니다."
                },
                {
                    "mistake": "BOD를 수치 없이 통역",
                    "correction": "BOD(생물화학적 산소요구량) mg/L",
                    "explanation": "BOD는 수질오염 지표로, 단위(mg/L)와 함께 표기해야 하며, 처음 언급 시 풀네임을 함께 통역하는 것이 좋습니다."
                },
                {
                    "mistake": "Ô nhiễm nước uống",
                    "correction": "Ô nhiễm nước (일반) / Ô nhiễm nguồn nước (수원)",
                    "explanation": "'Nước uống'은 식수를 의미하므로, 일반적인 수질오염은 'Ô nhiễm nước' 또는 'Ô nhiễm nguồn nước'로 표현해야 합니다."
                }
            ],
            "examples": [
                {
                    "ko": "이 공장은 수질오염 배출허용기준을 위반하여 과태료를 부과받았습니다.",
                    "vi": "Nhà máy này đã bị phạt tiền do vi phạm tiêu chuẩn cho phép xả thải gây ô nhiễm nước.",
                    "situation": "formal"
                },
                {
                    "ko": "강에 수질오염 물질이 유입되면 생태계가 파괴돼요.",
                    "vi": "Nếu chất gây ô nhiễm nước chảy vào sông thì hệ sinh thái sẽ bị phá hủy.",
                    "situation": "informal"
                },
                {
                    "ko": "수질오염도를 측정하기 위해 샘플을 채취합니다.",
                    "vi": "Chúng tôi lấy mẫu để đo mức độ ô nhiễm nước.",
                    "situation": "onsite"
                }
            ],
            "relatedTerms": ["폐수처리", "BOD", "COD"]
        },
        {
            "slug": "o-nhiem-khong-khi",
            "korean": "대기오염",
            "vietnamese": "Ô nhiễm không khí",
            "hanja": "大氣汚染",
            "hanjaReading": "大(큰 대) + 氣(기운 기) + 汚(더러울 오) + 染(물들일 염)",
            "pronunciation": "대기오염",
            "meaningKo": "공기 중에 먼지, 가스, 매연 등 유해물질이 과도하게 존재하여 인간과 환경에 해를 끼치는 상태로, 자동차 배기가스, 공장 굴뚝, 미세먼지, 황사 등이 원인입니다. 통역 시 한국의 '대기환경보전법'과 '미세먼지 저감 및 관리에 관한 특별법'을 베트남의 대기질 규정(QCVN 05:2013)과 구분하고, PM2.5, PM10 등 입자상 물질 단위를 정확히 전달해야 합니다. 한국은 미세먼지 문제가 사회적 이슈이고, 베트남은 하노이·호치민 등 대도시 중심으로 심각합니다.",
            "meaningVi": "Là tình trạng không khí chứa quá nhiều bụi, khí, khói độc hại gây hại cho con người và môi trường, nguyên nhân chủ yếu từ khí thải xe cộ, ống khói nhà máy, bụi mịn PM2.5, bụi vàng. Việt Nam quy định chất lượng không khí qua QCVN 05:2013, các thành phố lớn như Hà Nội và Hồ Chí Minh đang đối mặt với vấn đề ô nhiễm không khí nghiêm trọng.",
            "context": "환경법, 산업법, 교통법",
            "culturalNote": "한국은 '대기환경보전법'으로 배출시설을 관리하고, 미세먼지 특별법으로 계절관리제(12월~3월 고농도 시즌)를 운영합니다. 실시간 대기질 정보(에어코리아)를 제공하며, 비상저감조치로 차량 2부제, 공사장 운영 제한 등을 시행합니다. 베트남은 하노이와 호치민에서 오토바이 배기가스와 건설 먼지가 주요 원인이며, 대기질 측정망이 확대 중입니다. 한국은 중국발 미세먼지 이슈가 있고, 베트남은 건기(11월~4월)에 대기오염이 심합니다.",
            "commonMistakes": [
                {
                    "mistake": "공기 오염",
                    "correction": "대기오염",
                    "explanation": "환경법상 정식 용어는 '대기'이며, '공기'는 일상 표현입니다."
                },
                {
                    "mistake": "PM2.5를 '미세먼지 2.5'로 통역",
                    "correction": "PM2.5(초미세먼지) 또는 미세먼지 PM10",
                    "explanation": "PM2.5는 초미세먼지(입자 지름 2.5μm 이하), PM10은 미세먼지(10μm 이하)이므로 정확히 구분해야 합니다."
                },
                {
                    "mistake": "Ô nhiễm không khí를 Ô nhiễm khí quyển으로 통역",
                    "correction": "Ô nhiễm không khí가 일반적 표현",
                    "explanation": "'Khí quyển'은 대기권(지구 전체)을 의미하므로, 환경오염 맥락에서는 'Không khí'를 사용합니다."
                }
            ],
            "examples": [
                {
                    "ko": "오늘 대기오염도가 '매우 나쁨' 단계로, 외출 자제가 권고됩니다.",
                    "vi": "Hôm nay mức độ ô nhiễm không khí ở mức 'rất xấu', khuyến cáo hạn chế ra ngoài.",
                    "situation": "formal"
                },
                {
                    "ko": "요즘 대기오염이 심해서 마스크 꼭 써야 해요.",
                    "vi": "Dạo này ô nhiễm không khí nặng nên phải đeo khẩu trang.",
                    "situation": "informal"
                },
                {
                    "ko": "대기오염 측정소를 설치하여 실시간 모니터링하겠습니다.",
                    "vi": "Chúng tôi sẽ lắp đặt trạm đo ô nhiễm không khí để giám sát thời gian thực.",
                    "situation": "onsite"
                }
            ],
            "relatedTerms": ["미세먼지", "배기가스", "황사"]
        },
        {
            "slug": "toi-pham-moi-truong",
            "korean": "환경범죄",
            "vietnamese": "Tội phạm môi trường",
            "hanja": "環境犯罪",
            "hanjaReading": "環(고리 환) + 境(지경 경) + 犯(범할 범) + 罪(허물 죄)",
            "pronunciation": "환경범죄",
            "meaningKo": "환경을 오염시키거나 파괴하는 행위로서 형법이나 환경법에 의해 처벌받는 범죄를 의미하며, 불법 폐기물 투기, 무허가 배출, 환경영향평가 미이행, 환경오염 은폐 등이 포함됩니다. 통역 시 한국의 '환경범죄 등의 단속 및 가중처벌에 관한 법률'과 베트남 형법 제15장(환경 관련 범죄)을 구분하고, 양국 모두 징역형과 벌금형을 병과할 수 있으며, 법인도 처벌 대상임을 인지해야 합니다.",
            "meaningVi": "Là hành vi gây ô nhiễm hoặc phá hoại môi trường bị trừng phạt theo Luật Hình sự hoặc Luật Bảo vệ môi trường, bao gồm đổ rác thải trái phép, xả thải không phép, không thực hiện đánh giá tác động môi trường, che giấu ô nhiễm môi trường. Luật Hình sự Việt Nam 2015 quy định các tội phạm môi trường tại Chương XV, có thể bị phạt tù và phạt tiền đồng thời.",
            "context": "환경법, 형사법, 행정법",
            "culturalNote": "한국은 '환경범죄 단속법'으로 상습·조직적 환경범죄를 가중처벌하며, 환경부 특별사법경찰이 직접 수사합니다. 환경범죄 신고포상금 제도가 있고, 법인 양벌규정으로 대표자와 법인 모두 처벌됩니다. 베트남은 형법 제15장에서 환경범죄를 규정하며, 심각한 경우 최대 15년 징역과 사업장 폐쇄 명령이 가능합니다. 한국은 환경단체의 감시가 강하지만, 베트남은 정부 주도 단속이 주를 이룹니다.",
            "commonMistakes": [
                {
                    "mistake": "환경 위반",
                    "correction": "환경범죄",
                    "explanation": "단순 행정 위반은 '환경 위반', 형사처벌 대상은 '환경범죄'로 구분해야 합니다."
                },
                {
                    "mistake": "Vi phạm môi trường",
                    "correction": "Tội phạm môi trường",
                    "explanation": "'Vi phạm'은 위반(행정), 'Tội phạm'은 범죄(형사)이므로, 형사처벌 맥락에서는 'Tội phạm'을 사용해야 합니다."
                },
                {
                    "mistake": "환경범죄 양벌규정을 개인 처벌로만 통역",
                    "correction": "양벌규정은 법인과 대표자 모두 처벌",
                    "explanation": "한국과 베트남 모두 환경범죄 시 법인과 행위자를 동시에 처벌할 수 있으므로, 양벌규정 개념을 정확히 전달해야 합니다."
                }
            ],
            "examples": [
                {
                    "ko": "이 회사는 폐수를 무단 방류한 환경범죄로 대표이사와 법인이 모두 기소되었습니다.",
                    "vi": "Công ty này đã bị khởi tố cả giám đốc và pháp nhân về tội phạm môi trường do xả nước thải trái phép.",
                    "situation": "formal"
                },
                {
                    "ko": "환경범죄는 벌금만이 아니라 징역형도 받을 수 있어요.",
                    "vi": "Tội phạm môi trường có thể bị phạt tù chứ không chỉ phạt tiền.",
                    "situation": "informal"
                },
                {
                    "ko": "환경범죄 혐의로 현장 조사를 진행하겠습니다.",
                    "vi": "Chúng tôi sẽ tiến hành điều tra hiện trường về tội phạm môi trường.",
                    "situation": "onsite"
                }
            ],
            "relatedTerms": ["양벌규정", "환경사범", "불법투기"]
        },
        {
            "slug": "dieu-chinh-tranh-chap-moi-truong",
            "korean": "환경분쟁조정",
            "vietnamese": "Điều chỉnh tranh chấp môi trường",
            "hanja": "環境紛爭調停",
            "hanjaReading": "環(고리 환) + 境(지경 경) + 紛(어지러울 분) + 爭(다툴 쟁) + 調(고를 조) + 停(그칠 정)",
            "pronunciation": "환경분쟁조정",
            "meaningKo": "환경오염이나 환경훼손으로 인해 발생한 분쟁을 법원 소송이 아닌 조정·중재·재정 절차로 해결하는 제도로, 한국은 환경분쟁조정위원회(중앙·지방)가 담당합니다. 통역 시 한국의 '환경분쟁 조정법'과 베트남의 분쟁 해결 절차를 구분하고, 한국은 전문 조정위원회가 있지만 베트남은 법원 중심 해결이 일반적임을 이해해야 합니다. 조정·중재·재정의 차이를 명확히 설명할 수 있어야 합니다.",
            "meaningVi": "Là chế độ giải quyết tranh chấp phát sinh từ ô nhiễm hoặc hủy hoại môi trường thông qua thủ tục hòa giải, trọng tài, tài quyết thay vì kiện tụng tại tòa án. Ở Hàn Quốc có Ủy ban Điều chỉnh Tranh chấp Môi trường (trung ương và địa phương), trong khi Việt Nam chủ yếu giải quyết qua tòa án hoặc hòa giải cơ sở.",
            "context": "환경법, 민사법, 행정법",
            "culturalNote": "한국은 '환경분쟁 조정법'에 따라 중앙환경분쟁조정위원회(환경부 산하)와 지방환경분쟁조정위원회(시·도)가 설치되어 있으며, 조정(합의), 재정(준사법적 결정), 중재(사적 합의) 세 가지 방식이 있습니다. 비용이 저렴하고 신속하며, 전문가(환경공학, 의학, 법학)가 참여합니다. 베트남은 환경 분쟁을 주로 민사소송이나 행정소송으로 해결하며, 마을 단위 hòa giải(화해·조정) 제도가 있지만 전문 환경분쟁조정 기구는 없습니다.",
            "commonMistakes": [
                {
                    "mistake": "조정과 중재를 같은 의미로 통역",
                    "correction": "조정(hòa giải)은 합의 유도, 중재(trọng tài)는 제3자 결정",
                    "explanation": "조정은 당사자 간 합의를 돕는 것이고, 중재는 중재인이 결정하여 양측이 따르는 것이므로 명확히 구분해야 합니다."
                },
                {
                    "mistake": "Điều chỉnh",
                    "correction": "Điều chỉnh tranh chấp (분쟁조정) / Điều chỉnh (조정)",
                    "explanation": "'Điều chỉnh'만 쓰면 '조정하다', '수정하다' 등 다양한 의미이므로, 환경분쟁 맥락에서는 'Điều chỉnh tranh chấp môi trường'으로 완전히 표기해야 합니다."
                },
                {
                    "mistake": "재정을 판결로 통역",
                    "correction": "재정(tài quyết)은 준사법적 결정, 판결(phán quyết)은 법원 판결",
                    "explanation": "환경분쟁조정위원회의 재정은 법원 판결과 유사한 효력이 있지만 법원 판결은 아니므로, 'tài quyết'(재정)로 구분해야 합니다."
                }
            ],
            "examples": [
                {
                    "ko": "공장 소음으로 인한 피해는 환경분쟁조정위원회에 신청하여 조정받을 수 있습니다.",
                    "vi": "Thiệt hại do tiếng ồn từ nhà máy có thể được hòa giải thông qua Ủy ban Điều chỉnh Tranh chấp Môi trường.",
                    "situation": "formal"
                },
                {
                    "ko": "법원 가기 전에 환경분쟁조정을 먼저 시도해보세요.",
                    "vi": "Trước khi ra tòa, hãy thử điều chỉnh tranh chấp môi trường trước.",
                    "situation": "informal"
                },
                {
                    "ko": "환경분쟁조정 신청서를 작성하여 제출하겠습니다.",
                    "vi": "Chúng tôi sẽ lập và nộp đơn xin điều chỉnh tranh chấp môi trường.",
                    "situation": "onsite"
                }
            ],
            "relatedTerms": ["조정", "중재", "재정"]
        },
        {
            "slug": "quyen-phat-thai-carbon",
            "korean": "탄소배출권",
            "vietnamese": "Quyền phát thải carbon",
            "hanja": "炭素排出權",
            "hanjaReading": "炭(숯 탄) + 素(본바탕 소) + 排(물리칠 배) + 出(날 출) + 權(권할 권)",
            "pronunciation": "탄소배출권",
            "meaningKo": "온실가스를 일정량 배출할 수 있는 권리로, 배출권거래제(ETS)를 통해 사고팔 수 있는 시장 상품입니다. 기업이 할당량보다 적게 배출하면 남은 배출권을 판매하고, 초과하면 구매해야 합니다. 통역 시 한국의 '온실가스 배출권의 할당 및 거래에 관한 법률'과 베트남의 탄소배출권 시범사업을 구분하고, 한국은 2015년부터 본격 시행 중이며 베트남은 아직 초기 단계임을 인지해야 합니다. tCO2-eq(이산화탄소 환산톤) 단위를 정확히 전달해야 합니다.",
            "meaningVi": "Là quyền được phát thải một lượng khí nhà kính nhất định, có thể mua bán thông qua chế độ giao dịch quyền phát thải (ETS). Doanh nghiệp phát thải ít hơn hạn mức được bán quyền thừa, phát thải vượt mức phải mua thêm. Việt Nam đang trong giai đoạn thí điểm chế độ này, trong khi Hàn Quốc đã vận hành chính thức từ 2015.",
            "context": "환경법, 기후법, 경제법",
            "culturalNote": "한국은 2015년부터 배출권거래제(K-ETS)를 시행하며, 발전·철강·석유화학·시멘트 등 대규모 배출 사업장 약 700개가 대상입니다. 배출권은 거래소에서 매매되며, 벌금보다 시장 메커니즘을 활용합니다. 베트남은 2025년 탄소세 도입 예정이며, 배출권거래제는 시범 단계로, 한국과 EU의 제도를 참고 중입니다. 한국은 탄소중립 2050을 선언했고, 베트남은 2050 넷제로를 목표로 합니다.",
            "commonMistakes": [
                {
                    "mistake": "탄소권",
                    "correction": "탄소배출권",
                    "explanation": "정식 용어는 '탄소배출권' 또는 '온실가스 배출권'이며, '탄소권'은 약칭이지만 공식 문서에서는 완전한 표현을 사용해야 합니다."
                },
                {
                    "mistake": "Quyền carbon",
                    "correction": "Quyền phát thải carbon",
                    "explanation": "'Quyền carbon'은 축약형이므로, 법률 및 공식 문서에서는 'Quyền phát thải carbon' 또는 'Quyền phát thải khí nhà kính'으로 표기해야 합니다."
                },
                {
                    "mistake": "tCO2를 '탄소 톤'으로 통역",
                    "correction": "tCO2-eq(이산화탄소 환산톤)",
                    "explanation": "배출권 단위는 tCO2-eq(이산화탄소 환산톤)이며, 메탄·아산화질소 등도 CO2로 환산한 값이므로 정확한 단위 표기가 필요합니다."
                }
            ],
            "examples": [
                {
                    "ko": "이 기업은 배출권 할당량을 초과하여 탄소배출권을 시장에서 구매해야 합니다.",
                    "vi": "Doanh nghiệp này đã vượt hạn mức phát thải và phải mua quyền phát thải carbon trên thị trường.",
                    "situation": "formal"
                },
                {
                    "ko": "탄소배출권 가격이 올라서 배출 감축 압박이 커지고 있어요.",
                    "vi": "Giá quyền phát thải carbon tăng nên áp lực giảm phát thải đang tăng.",
                    "situation": "informal"
                },
                {
                    "ko": "탄소배출권 거래 내역을 확인하겠습니다.",
                    "vi": "Chúng tôi sẽ xác nhận nội dung giao dịch quyền phát thải carbon.",
                    "situation": "onsite"
                }
            ],
            "relatedTerms": ["온실가스", "배출권거래제", "탄소중립"]
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
    print(f"Added {len(filtered)} terms. Total: {len(data)}")

if __name__ == '__main__':
    main()
