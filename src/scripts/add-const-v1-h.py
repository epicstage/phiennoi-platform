#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
건설(Construction) 도메인 용어 추가 스크립트 v1-h
테마: 지하공사/터널 (Underground & Tunnel)
"""

import json
import os

# 프로젝트 루트 기준 경로
PROJECT_ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
file_path = os.path.join(PROJECT_ROOT, "data", "terms", "construction.json")

# 신규 용어 10개 (지하공사/터널)
new_terms = [
    {
        "slug": "tuong-chan-dat",
        "korean": "흙막이벽",
        "vietnamese": "Tường chắn đất",
        "hanja": "土막이壁",
        "hanjaReading": "土(흙 토) + 壁(벽 벽)",
        "pronunciation": "흐으막이벼",
        "meaningKo": "지하 굴착 시 주변 지반의 붕괴를 방지하기 위해 설치하는 가설구조물로, 한국에서는 CIP(현장타설말뚝), SCW(soil cement wall), Sheet Pile(강널말뚝) 등 다양한 공법이 사용됩니다. 통역 시 '가설구조물'임을 강조해야 영구구조물인 옹벽(tường chắn cố định)과 혼동을 방지할 수 있습니다. 베트남에서는 주로 강널말뚝(cọc tấm thép) 방식이 일반적이므로, 한국의 CIP나 SCW 공법 설명 시 '콘크리트 타설 방식'임을 명확히 전달해야 합니다. 안전관리 회의에서는 '지반침하 방지', '지하수 차단' 기능을 함께 언급하는 것이 중요합니다.",
        "meaningVi": "Cấu trúc tạm thời được lắp đặt để ngăn chặn sự sụp đổ của nền đất xung quanh trong quá trình đào móng. Ở Hàn Quốc sử dụng nhiều phương pháp như CIP (cọc đổ tại chỗ), SCW (tường xi măng đất), Sheet Pile (cọc tấm thép). Cần phân biệt rõ với tường chắn cố định (옹벽) vì đây là cấu trúc tạm thời.",
        "context": "지하공사, 굴착공사, 안전관리",
        "culturalNote": "한국은 도심지 지하공사가 많아 CIP, SCW 같은 고급 공법이 발달했으나, 베트남은 아직 강널말뚝 중심입니다. 한국 현장에서 'CIP 공법'이라고 하면 베트남 통역사가 낯설어할 수 있으므로 '콘크리트를 현장에서 바로 타설하는 말뚝'이라고 풀어 설명하는 것이 효과적입니다. 또한 한국은 지하수 처리(배수, 차수)를 매우 중요시하므로 흙막이벽 설명 시 방수 기능도 함께 언급해야 합니다.",
        "commonMistakes": [
            {
                "mistake": "Tường chắn (옹벽으로 오역)",
                "correction": "Tường chắn đất tạm thời / Kết cấu chống sụp lở",
                "explanation": "옹벽(retaining wall)은 영구구조물이고, 흙막이벽은 가설구조물입니다. '가설(tạm thời)'을 반드시 명시해야 합니다."
            },
            {
                "mistake": "CIP를 '씨아이피'로 음차",
                "correction": "Cọc đổ bê tông tại chỗ (CIP)",
                "explanation": "약어를 그대로 읽으면 베트남 현장 인력이 이해 못 합니다. 풀어서 설명 후 약어를 병기하세요."
            },
            {
                "mistake": "Sheet Pile을 '시트 파일'로만 표현",
                "correction": "Cọc tấm thép (Sheet Pile)",
                "explanation": "베트남에서는 'cọc tấm thép'이 일반적이므로 베트남어 명칭을 먼저 말하고 영어를 괄호로 병기하는 것이 효과적입니다."
            }
        ],
        "examples": [
            {
                "ko": "이번 지하 3층 굴착에는 CIP 공법으로 흙막이벽을 시공합니다.",
                "vi": "Công trình đào hầm 3 tầng này sẽ thi công tường chắn đất bằng phương pháp CIP (cọc đổ bê tông tại chỗ).",
                "situation": "formal"
            },
            {
                "ko": "흙막이벽 변위 측정 결과 안전 기준 이내입니다.",
                "vi": "Kết quả đo biến dạng tường chắn đất nằm trong giới hạn an toàn.",
                "situation": "onsite"
            },
            {
                "ko": "강널말뚝(Sheet Pile) 방식은 비용은 저렴하지만 차수 성능이 CIP보다 낮습니다.",
                "vi": "Phương pháp cọc tấm thép (Sheet Pile) chi phí thấp nhưng khả năng chống thấm kém hơn CIP.",
                "situation": "formal"
            }
        ],
        "relatedTerms": ["굴착", "지반침하", "옹벽", "어스앵커"]
    },
    {
        "slug": "coc-do-tai-cho-cip",
        "korean": "현장타설말뚝",
        "vietnamese": "Cọc đổ tại chỗ (CIP)",
        "hanja": "現場打設말뚝",
        "hanjaReading": "現(나타날 현) + 場(마당 장) + 打(칠 타) + 設(베풀 설)",
        "pronunciation": "현장타설말뚝",
        "meaningKo": "지반을 천공한 후 현장에서 직접 콘크리트를 타설하여 만드는 기초말뚝으로, 영어로는 CIP(Cast In Place Pile)라고 합니다. 한국 건설 현장에서는 흙막이벽, 기초공사에 널리 사용되며, 공장 제작 말뚝(PHC 파일)보다 지지력이 우수하고 소음·진동이 적어 도심지 공사에 적합합니다. 통역 시 '현장에서 타설한다(đổ tại chỗ)'는 점을 강조해야 기성말뚝(cọc ép thành phẩm)과 구분됩니다. 베트남에서는 상대적으로 덜 사용되므로 공법 자체를 설명해야 할 때가 많습니다. 시공 순서는 천공→철근망 삽입→콘크리트 타설→양생 순입니다.",
        "meaningVi": "Cọc móng được tạo ra bằng cách khoan lỗ vào nền đất và đổ bê tông trực tiếp tại hiện trường. Tiếng Anh gọi là CIP (Cast In Place Pile). Ở Hàn Quốc được sử dụng rộng rãi cho tường chắn đất và công trình móng, có khả năng chịu lực tốt hơn cọc nhà máy (PHC) và ít gây tiếng ồn, rung động nên phù hợp với khu vực đô thị.",
        "context": "기초공사, 지하공사, 흙막이벽",
        "culturalNote": "한국은 도심지 건설이 많아 CIP 공법이 매우 발달했고, 대형 건설사들은 자체 CIP 장비와 시공 노하우를 보유하고 있습니다. 반면 베트남은 PHC 파일(cọc ép thành phẩm) 중심이라 CIP 경험이 상대적으로 적습니다. 한국 현장에서 CIP 시공 시 '천공 깊이', '철근망 규격', '콘크리트 타설 속도' 등 세밀한 품질관리를 강조하는데, 이를 통역할 때 베트남 인력에게는 '왜 이렇게 복잡한가'라는 반응이 나올 수 있으므로 '지지력 확보를 위한 필수 절차'임을 설명해야 합니다.",
        "commonMistakes": [
            {
                "mistake": "Cọc khoan nhồi (순수 천공 말뚝으로 오역)",
                "correction": "Cọc đổ bê tông tại chỗ (CIP)",
                "explanation": "'khoan nhồi'는 천공 후 콘크리트를 채우는 일반적인 방식이지만, CIP는 특수 공법이므로 'đổ tại chỗ'를 명시해야 합니다."
            },
            {
                "mistake": "PHC 파일과 혼동",
                "correction": "CIP는 현장 타설, PHC는 공장 제작 후 박음",
                "explanation": "PHC는 cọc ép thành phẩm(기성 압입말뚝)으로 완전히 다른 공법입니다. 통역 시 반드시 구분하세요."
            },
            {
                "mistake": "'타설'을 '붓는다(đổ)'로만 번역",
                "correction": "Đổ và đầm chặt bê tông (타설 및 다짐)",
                "explanation": "콘크리트 타설은 단순히 붓는 것이 아니라 진동다짐(đầm chặt)까지 포함하므로 함께 표현해야 합니다."
            }
        ],
        "examples": [
            {
                "ko": "이번 프로젝트는 지지력 확보를 위해 CIP 공법을 적용합니다.",
                "vi": "Dự án này áp dụng phương pháp CIP (cọc đổ tại chỗ) để đảm bảo sức chịu tải.",
                "situation": "formal"
            },
            {
                "ko": "CIP 타설 시 콘크리트 슬럼프는 18±2cm를 유지해야 합니다.",
                "vi": "Khi đổ CIP, độ sụt bê tông (slump) phải duy trì 18±2cm.",
                "situation": "onsite"
            },
            {
                "ko": "PHC 파일은 소음이 크지만, CIP는 진동이 적어 도심지에 유리합니다.",
                "vi": "Cọc PHC gây tiếng ồn lớn, nhưng CIP ít rung động nên thuận lợi cho khu vực đô thị.",
                "situation": "formal"
            }
        ],
        "relatedTerms": ["PHC파일", "천공", "콘크리트타설", "기초공사"]
    },
    {
        "slug": "tuong-xi-mang-dat-scw",
        "korean": "소일시멘트월",
        "vietnamese": "Tường xi măng đất (SCW)",
        "hanja": None,
        "hanjaReading": None,
        "pronunciation": "소일시멘트월",
        "meaningKo": "지반에 시멘트를 주입하여 흙과 혼합해 만드는 지중연속벽으로, 영어로는 SCW(Soil Cement Wall)라고 합니다. 한국에서는 도심지 지하공사 시 흙막이벽으로 많이 사용되며, CIP보다 시공 속도가 빠르고 차수 성능이 우수합니다. 통역 시 '시멘트와 흙을 섞는다(trộn xi măng với đất)'는 원리를 설명해야 베트남 현장 인력이 이해하기 쉽습니다. 베트남에서는 상대적으로 생소한 공법이므로 '지하수 차단 기능이 뛰어나다'는 장점을 강조하면 효과적입니다. 시공 시 교반 깊이, 시멘트 배합비를 엄격히 관리해야 품질이 확보됩니다.",
        "meaningVi": "Tường liên tục ngầm được tạo ra bằng cách bơm xi măng vào nền đất và trộn đều. Tiếng Anh gọi là SCW (Soil Cement Wall). Ở Hàn Quốc được sử dụng rộng rãi làm tường chắn đất cho công trình ngầm ở khu vực đô thị, tốc độ thi công nhanh hơn CIP và khả năng chống thấm tốt.",
        "context": "흙막이벽, 지하공사, 차수",
        "culturalNote": "한국은 지하철, 지하상가 건설이 많아 SCW 공법이 일반화되었고, 전문 장비(Mixing Plant)와 숙련 인력이 풍부합니다. 베트남은 지하 개발이 상대적으로 적어 SCW 경험이 부족하므로, 한국 현장에 베트남 인력을 투입할 때는 '시멘트 주입량', '교반 시간', '강도 측정' 등 품질관리 절차를 사전 교육해야 합니다. 또한 한국은 지하수위가 높은 지역이 많아 차수(chống thấm) 성능을 매우 중요시하는데, 이 부분을 통역 시 강조하지 않으면 베트남 인력이 시공 중요성을 간과할 수 있습니다.",
        "commonMistakes": [
            {
                "mistake": "Tường bê tông (콘크리트 벽으로 오역)",
                "correction": "Tường xi măng đất (SCW)",
                "explanation": "SCW는 순수 콘크리트가 아니라 흙+시멘트 혼합물이므로 'xi măng đất'로 표현해야 정확합니다."
            },
            {
                "mistake": "'소일'을 '토양(토壤)'으로 번역",
                "correction": "Đất (Soil)",
                "explanation": "'토양'은 농업용어이고, 건설에서는 '지반(nền đất)' 또는 단순히 '흙(đất)'이 맞습니다."
            },
            {
                "mistake": "차수 기능을 언급 안 함",
                "correction": "Khả năng chống thấm nước ngầm (지하수 차단 기능) 강조",
                "explanation": "SCW의 핵심 장점은 차수 성능이므로 이를 빠뜨리면 공법의 의미가 반감됩니다."
            }
        ],
        "examples": [
            {
                "ko": "지하수위가 높은 이 현장은 SCW 공법으로 차수 효과를 극대화합니다.",
                "vi": "Công trường này có mực nước ngầm cao nên áp dụng SCW để tối đa hóa hiệu quả chống thấm.",
                "situation": "formal"
            },
            {
                "ko": "SCW 교반 시 시멘트 배합비는 1:3을 준수하세요.",
                "vi": "Khi trộn SCW, vui lòng tuân thủ tỷ lệ xi măng 1:3.",
                "situation": "onsite"
            },
            {
                "ko": "CIP는 지지력이 강하고, SCW는 차수 성능이 우수합니다.",
                "vi": "CIP có sức chịu tải cao, còn SCW có khả năng chống thấm tốt.",
                "situation": "formal"
            }
        ],
        "relatedTerms": ["흙막이벽", "차수", "지하수", "CIP"]
    },
    {
        "slug": "neo-dat-earth-anchor",
        "korean": "어스앵커",
        "vietnamese": "Neo đất (Earth Anchor)",
        "hanja": None,
        "hanjaReading": None,
        "pronunciation": "어스앵커",
        "meaningKo": "지반 깊숙이 강선(PC강선)을 삽입하고 그라우팅하여 흙막이벽을 지지하는 가설 구조물로, 영어로는 Earth Anchor 또는 Ground Anchor라고 합니다. 한국 지하공사에서는 흙막이벽의 변위를 억제하기 위해 필수적으로 사용되며, 앵커 각도(보통 15~30도 하향), 긴장력(텐션) 관리가 안전의 핵심입니다. 통역 시 '지반 속에 박힌 줄로 벽을 당긴다'는 이미지를 전달하면 이해가 빠릅니다. 베트남에서는 'neo đất' 또는 'neo chống'으로 부르며, 시공 경험이 적은 편이라 텐션 측정, PS 강선 규격 등 세부 사항을 상세히 설명해야 합니다. 인장력 시험(load test)을 반드시 실시해야 안전이 확보됩니다.",
        "meaningVi": "Cấu trúc tạm thời hỗ trợ tường chắn đất bằng cách cắm sợi cáp thép (PC strand) sâu vào nền đất và phun vữa (grouting). Tiếng Anh gọi là Earth Anchor hoặc Ground Anchor. Ở Hàn Quốc được sử dụng bắt buộc trong công trình ngầm để ngăn biến dạng tường chắn, quản lý góc neo (thường 15~30 độ xuống) và lực căng (tension) là chìa khóa an toàn.",
        "context": "흙막이벽, 지하공사, 안전관리",
        "culturalNote": "한국은 도심지 협소 부지 공사가 많아 어스앵커 시공 기술이 고도로 발달했고, 앵커 설계(간격, 각도, 길이)를 매우 정밀하게 합니다. 베트남은 상대적으로 넓은 부지 공사가 많아 앵커 사용 빈도가 낮고, 시공 경험도 부족합니다. 한국 현장에서 '긴장력 200kN 유지'라는 지시를 통역할 때, 베트남 인력은 'kN'이라는 단위나 긴장력 측정 장비(load cell) 사용법을 모를 수 있으므로 사전 교육이 필수입니다. 또한 앵커 시공 후 인장시험(load test)을 반드시 하는데, 이를 '품질검증'이 아니라 '안전확인'으로 강조하면 현장 협조도가 높아집니다.",
        "commonMistakes": [
            {
                "mistake": "Neo (일반 앵커로 오역)",
                "correction": "Neo đất / Neo chống tường (어스앵커 명시)",
                "explanation": "'neo'만 쓰면 배의 닻이나 일반 앵커볼트와 혼동됩니다. 'neo đất' 또는 'neo chống tường'으로 명확히 해야 합니다."
            },
            {
                "mistake": "긴장력(Tension)을 '장력'으로만 표현",
                "correction": "Lực căng / Lực kéo căng (긴장력)",
                "explanation": "'tension'은 단순 장력이 아니라 사전 인장을 가한 상태이므로 'lực căng' 또는 'lực kéo căng'으로 표현해야 정확합니다."
            },
            {
                "mistake": "인장시험(Load Test)을 생략",
                "correction": "Thử tải trọng / Kiểm tra lực kéo căng",
                "explanation": "어스앵커의 핵심은 인장시험으로 안전을 확인하는 것인데, 이를 통역에서 누락하면 안전사고로 이어질 수 있습니다."
            }
        ],
        "examples": [
            {
                "ko": "흙막이벽 3단에 어스앵커를 15도 각도로 시공합니다.",
                "vi": "Thi công neo đất tại tầng 3 tường chắn với góc 15 độ.",
                "situation": "onsite"
            },
            {
                "ko": "앵커 긴장력은 설계값 200kN을 유지해야 합니다.",
                "vi": "Lực căng neo phải duy trì giá trị thiết kế 200kN.",
                "situation": "formal"
            },
            {
                "ko": "어스앵커 인장시험 결과 모두 합격입니다.",
                "vi": "Kết quả thử tải trọng neo đất đều đạt yêu cầu.",
                "situation": "onsite"
            }
        ],
        "relatedTerms": ["흙막이벽", "긴장력", "그라우팅", "인장시험"]
    },
    {
        "slug": "bulong-neo-da-rock-bolt",
        "korean": "락볼트",
        "vietnamese": "Bu lông neo đá (Rock Bolt)",
        "hanja": None,
        "hanjaReading": None,
        "pronunciation": "락볼트",
        "meaningKo": "터널이나 암반 굴착 시 암반의 이완과 낙석을 방지하기 위해 암반에 박아 넣는 강봉으로, 영어로는 Rock Bolt라고 합니다. 한국의 터널 공사, 지하발전소, 광산에서 필수적으로 사용되며, 볼트 길이(보통 2~6m), 간격(1~2m), 정착 방식(그라우팅/수지앵커)이 설계의 핵심입니다. 통역 시 '암반에 박는 못'이라는 이미지를 주되, '낙석 방지'와 '암반 일체화' 두 가지 기능을 모두 설명해야 합니다. 베트남에서는 'bu lông neo đá' 또는 'bulong kẹp đá'로 부르며, 터널 경험이 적은 현장 인력에게는 시공 순서(천공→볼트 삽입→그라우팅→긴결)를 단계별로 설명해야 합니다. 숏크리트와 함께 사용되는 경우가 많습니다.",
        "meaningVi": "Thanh thép được cắm vào đá để ngăn chặn sự nới lỏng và rơi đá trong quá trình đào hầm hoặc khai thác mỏ. Tiếng Anh gọi là Rock Bolt. Ở Hàn Quốc được sử dụng bắt buộc trong công trình hầm, nhà máy điện ngầm, mỏ khoáng sản. Chiều dài bu lông (thường 2~6m), khoảng cách (1~2m), phương pháp cố định (grouting/resin anchor) là yếu tố thiết kế chính.",
        "context": "터널공사, 암반공사, 안전관리",
        "culturalNote": "한국은 산악 지형이 많아 터널 건설 기술이 매우 발달했고, 락볼트는 NATM 공법의 핵심 요소입니다. 베트남은 평야가 많아 터널 경험이 상대적으로 적고, 락볼트 시공 노하우도 부족합니다. 한국 터널 현장에 베트남 인력을 투입할 때는 '천공 깊이 확인', '그라우팅 충전 확인', '볼트 긴결 토크' 등 품질관리 포인트를 사전 교육해야 합니다. 또한 한국은 안전을 위해 락볼트 시공 직후 타음 검사(두드려서 소리로 판단)를 하는데, 베트남 인력은 이를 형식적 절차로 오해할 수 있으므로 '낙석 사고 예방'이라는 목적을 명확히 전달해야 합니다.",
        "commonMistakes": [
            {
                "mistake": "Bu lông (일반 볼트로 오역)",
                "correction": "Bu lông neo đá (Rock Bolt)",
                "explanation": "'bu lông'만 쓰면 일반 체결용 볼트와 혼동됩니다. 'neo đá'를 붙여 암반용임을 명시해야 합니다."
            },
            {
                "mistake": "앵커볼트와 혼동",
                "correction": "앵커볼트(Anchor Bolt)는 콘크리트용, 락볼트(Rock Bolt)는 암반용",
                "explanation": "용도가 완전히 다르므로 통역 시 'đá(암반)'를 강조해 구분해야 합니다."
            },
            {
                "mistake": "그라우팅을 '주입'으로만 표현",
                "correction": "Phun vữa đầy (그라우팅 충전)",
                "explanation": "그라우팅은 단순 주입이 아니라 공극을 완전히 채우는 작업이므로 'đầy(가득 채움)'를 명시해야 합니다."
            }
        ],
        "examples": [
            {
                "ko": "터널 막장에 락볼트를 1.5m 간격으로 시공하세요.",
                "vi": "Thi công bu lông neo đá tại mặt hầm với khoảng cách 1.5m.",
                "situation": "onsite"
            },
            {
                "ko": "락볼트 정착 후 반드시 타음 검사를 실시합니다.",
                "vi": "Sau khi cố định bu lông neo đá, bắt buộc phải kiểm tra bằng cách gõ (thử âm thanh).",
                "situation": "formal"
            },
            {
                "ko": "숏크리트와 락볼트를 조합하면 암반 안정성이 크게 향상됩니다.",
                "vi": "Kết hợp shotcrete và bu lông neo đá sẽ cải thiện đáng kể độ ổn định của đá.",
                "situation": "formal"
            }
        ],
        "relatedTerms": ["터널", "숏크리트", "NATM공법", "암반"]
    },
    {
        "slug": "shotcrete-phun-be-tong",
        "korean": "숏크리트",
        "vietnamese": "Shotcrete (Phun bê tông)",
        "hanja": None,
        "hanjaReading": None,
        "pronunciation": "숏크리트",
        "meaningKo": "압축공기를 이용해 콘크리트를 고속으로 분사하는 공법으로, 터널 내벽 보강, 비탈면 보호에 사용됩니다. 영어로는 Shotcrete, 베트남어로는 'phun bê tông'이라고 합니다. 한국 터널 공사에서는 NATM 공법의 핵심 요소로, 굴착 직후 즉시 숏크리트를 타설해 암반 이완을 방지합니다. 통역 시 '뿜어서 붙인다(phun dính)'는 원리를 설명하되, 일반 콘크리트 타설과는 다른 '고속 분사'임을 강조해야 합니다. 건식(Dry Mix)과 습식(Wet Mix) 두 방식이 있으며, 한국은 품질 균일성 때문에 습식을 선호합니다. 시공 시 반발률(rebound), 두께 관리가 품질의 핵심이고, 락볼트와 함께 사용되는 경우가 많습니다.",
        "meaningVi": "Phương pháp phun bê tông tốc độ cao bằng khí nén, được sử dụng để gia cố thành hầm và bảo vệ mái dốc. Tiếng Anh gọi là Shotcrete. Ở Hàn Quốc là yếu tố cốt lõi của công nghệ NATM, ngay sau khi đào phải phun shotcrete để ngăn đá bị nới lỏng. Có hai phương pháp: trộn khô (Dry Mix) và trộn ướt (Wet Mix), Hàn Quốc ưu tiên trộn ướt vì chất lượng đồng đều.",
        "context": "터널공사, NATM공법, 비탈면보호",
        "culturalNote": "한국은 터널 기술이 발달해 숏크리트 장비와 시공 인력이 풍부하며, 품질관리 기준(압축강도, 두께, 반발률)이 엄격합니다. 베트남은 터널 경험이 적어 숏크리트를 '그냥 뿜는 콘크리트'로 단순하게 이해하는 경우가 많습니다. 한국 현장에서 '습식 숏크리트로 두께 10cm 균일하게 타설'이라는 지시를 통역할 때, 베트남 인력은 습식/건식 차이나 두께 측정 방법을 모를 수 있으므로 시공 전 시연(demonstration)을 하는 것이 효과적입니다. 또한 숏크리트는 분진이 심하므로 '환기', '마스크 착용'을 안전 지시와 함께 전달해야 합니다.",
        "commonMistakes": [
            {
                "mistake": "Bê tông phun (일반 콘크리트 분사로 오역)",
                "correction": "Shotcrete (Phun bê tông áp lực cao)",
                "explanation": "'phun bê tông'만 쓰면 일반 분사와 구분 안 됩니다. 'áp lực cao(고압)' 또는 'Shotcrete' 원어를 병기하세요."
            },
            {
                "mistake": "건식/습식 구분 없이 통역",
                "correction": "Trộn khô (Dry Mix) / Trộn ướt (Wet Mix) 명시",
                "explanation": "두 방식은 장비, 품질, 시공법이 다르므로 반드시 구분해서 통역해야 합니다."
            },
            {
                "mistake": "반발률(Rebound)을 '튕김'으로만 표현",
                "correction": "Tỷ lệ bật ra / Hệ số phản hồi (반발률)",
                "explanation": "'반발률'은 품질 지표이므로 'tỷ lệ(비율)'를 명시해야 기술 용어로 인식됩니다."
            }
        ],
        "examples": [
            {
                "ko": "터널 굴착 후 즉시 숏크리트 10cm를 타설하세요.",
                "vi": "Ngay sau khi đào hầm, phun shotcrete dày 10cm.",
                "situation": "onsite"
            },
            {
                "ko": "습식 숏크리트가 건식보다 품질이 균일합니다.",
                "vi": "Shotcrete trộn ướt có chất lượng đồng đều hơn trộn khô.",
                "situation": "formal"
            },
            {
                "ko": "숏크리트 시공 시 환기를 철저히 하고 마스크를 착용하세요.",
                "vi": "Khi thi công shotcrete, phải thông gió kỹ và đeo khẩu trang.",
                "situation": "onsite"
            }
        ],
        "relatedTerms": ["터널", "락볼트", "NATM공법", "비탈면"]
    },
    {
        "slug": "may-dao-ham-tbm",
        "korean": "TBM장비",
        "vietnamese": "Máy đào hầm TBM",
        "hanja": None,
        "hanjaReading": None,
        "pronunciation": "티비엠장비",
        "meaningKo": "Tunnel Boring Machine의 약자로, 대형 회전 커터로 지반을 굴착하며 터널을 자동으로 뚫는 기계식 터널 굴착 장비입니다. 한국에서는 지하철, 고속도로 터널 등 대규모 장대 터널 시공에 사용되며, NATM 공법보다 안전하고 빠르지만 초기 투자비가 매우 큽니다. 통역 시 '거대한 굴삭기'라는 이미지를 주되, '동시에 터널 벽을 세그먼트로 조립한다'는 특징을 강조해야 합니다. 베트남에서는 'máy đào hầm TBM' 또는 'máy khoan hầm'으로 부르며, 실제 운용 경험이 있는 인력이 거의 없으므로 장비 구조(커터헤드, 세그먼트, 후방 지원 시스템)를 상세히 설명해야 합니다. 굴진 속도는 지반 조건에 따라 일 10~30m 수준입니다.",
        "meaningVi": "Viết tắt của Tunnel Boring Machine, là thiết bị đào hầm cơ khí sử dụng đầu cắt xoay lớn để khai quật nền đất và tạo hầm tự động. Ở Hàn Quốc được dùng cho hầm quy mô lớn như tàu điện ngầm, đường hầm cao tốc. An toàn và nhanh hơn NATM nhưng chi phí đầu tư ban đầu rất cao. Tốc độ đào khoảng 10~30m/ngày tùy điều kiện nền.",
        "context": "터널공사, 대형공사, 지하철",
        "culturalNote": "한국은 서울, 부산 등 대도시 지하철 건설 과정에서 TBM 운용 경험이 축적되었고, 대형 건설사들은 자체 TBM을 보유하거나 리스합니다. 베트남은 아직 TBM을 사용한 터널 프로젝트가 극히 드물어, 통역 시 장비 자체를 처음 보는 현장 인력이 많습니다. TBM은 '굴착-세그먼트 조립-추진'이 동시에 이루어지는데, 이를 통역할 때 '컨베이어 벨트처럼 계속 앞으로 나간다'는 비유를 쓰면 이해가 빠릅니다. 또한 TBM은 장비 유지보수가 매우 중요하므로 '일일 점검', '커터 교체' 같은 용어를 정확히 전달해야 합니다.",
        "commonMistakes": [
            {
                "mistake": "Máy khoan (일반 드릴로 오역)",
                "correction": "Máy đào hầm TBM / Máy khoan hầm tự động",
                "explanation": "'máy khoan'만 쓰면 소형 드릴로 오해됩니다. '터널(hầm)'과 'TBM'을 명시하세요."
            },
            {
                "mistake": "세그먼트(Segment)를 '부품'으로 번역",
                "correction": "Tấm lót hầm / Segment lắp ghép",
                "explanation": "세그먼트는 터널 내벽을 구성하는 조립식 패널이므로 'tấm lót(내벽재)' 또는 'segment lắp ghép'으로 표현해야 합니다."
            },
            {
                "mistake": "NATM과 비교 없이 설명",
                "correction": "TBM은 기계식, NATM은 발파식 공법임을 대비 설명",
                "explanation": "베트남 인력이 터널=발파로 이해하는 경우가 많으므로 TBM의 차별점(무발파, 자동화)을 강조해야 합니다."
            }
        ],
        "examples": [
            {
                "ko": "이번 지하철 터널은 TBM 장비로 시공하여 발파 소음이 없습니다.",
                "vi": "Hầm tàu điện ngầm này thi công bằng TBM nên không có tiếng ồn nổ mìn.",
                "situation": "formal"
            },
            {
                "ko": "TBM 굴진 속도는 오늘 20m였습니다.",
                "vi": "Tốc độ đào của TBM hôm nay là 20m.",
                "situation": "onsite"
            },
            {
                "ko": "TBM 커터 교체 작업에 3일이 소요됩니다.",
                "vi": "Công việc thay đầu cắt TBM mất 3 ngày.",
                "situation": "formal"
            }
        ],
        "relatedTerms": ["터널", "세그먼트", "NATM공법", "지하철"]
    },
    {
        "slug": "gieng-thong-gio-ham",
        "korean": "환기구",
        "vietnamese": "Giếng thông gió hầm",
        "hanja": "換氣口",
        "hanjaReading": "換(바꿀 환) + 氣(기운 기) + 口(입 구)",
        "pronunciation": "환기구",
        "meaningKo": "터널 내부의 오염된 공기를 외부로 배출하고 신선한 공기를 공급하기 위한 수직 또는 경사 통로로, 장대 터널에서는 필수 시설입니다. 한국의 고속도로 터널, 지하철에서는 일정 간격마다 환기구를 설치하며, 환기 방식(자연환기/기계환기)과 배연(화재 시 연기 배출) 기능이 설계의 핵심입니다. 통역 시 '공기 교환'뿐 아니라 '화재 대피로' 역할도 설명해야 안전의 중요성이 전달됩니다. 베트남에서는 'giếng thông gió' 또는 'ống thông gió'로 부르며, 짧은 터널이 많아 환기구 설계 경험이 부족합니다. 환기구는 터널 본체 굴착 후 별도로 시공되며, 환기팬, 덕트 등 기계설비가 함께 설치됩니다.",
        "meaningVi": "Đường hầm dọc hoặc nghiêng để thoát khí bẩn và cung cấp không khí sạch vào trong hầm, là cơ sở hạ tầng bắt buộc cho hầm dài. Ở Hàn Quốc, hầm đường cao tốc và tàu điện ngầm lắp đặt giếng thông gió theo khoảng cách nhất định, phương thức thông gió (tự nhiên/cơ khí) và chức năng xả khói (thoát khói khi cháy) là yếu tố thiết kế chính.",
        "context": "터널, 환기설비, 안전시설",
        "culturalNote": "한국은 장대 터널(1km 이상)이 많아 환기 시스템 설계 기술이 매우 발달했고, 화재 대비 배연 기능을 법적으로 의무화하고 있습니다. 베트남은 평야가 많아 장대 터널이 드물고, 환기구 설계 경험이 부족합니다. 한국 현장에서 '환기구 시공'이라고 하면 베트남 인력은 '단순히 구멍 뚫는 것'으로 오해할 수 있으므로 '환기팬 설치', '덕트 연결', '제어 시스템' 등 전체 시스템을 설명해야 합니다. 또한 환기구는 소음원이 되기도 하므로 주변 민원 대책(방음벽, 소음기)을 함께 고려해야 하는데, 이 부분도 통역 시 전달하면 현장 이해도가 높아집니다.",
        "commonMistakes": [
            {
                "mistake": "Ống thông gió (일반 환기관으로 오역)",
                "correction": "Giếng thông gió hầm (터널 환기구)",
                "explanation": "'ống'은 작은 파이프를 연상시킵니다. 터널 환기구는 사람이 들어갈 수 있는 큰 수직 통로이므로 'giếng(우물, 수직갱)'을 써야 정확합니다."
            },
            {
                "mistake": "배연(排煙) 기능 누락",
                "correction": "Thông gió + Thoát khói khi cháy (환기 + 화재 시 배연)",
                "explanation": "환기구의 핵심 기능은 화재 대비 연기 배출이므로 이를 빠뜨리면 안전 중요성이 반감됩니다."
            },
            {
                "mistake": "자연환기/기계환기 구분 없이 설명",
                "correction": "Thông gió tự nhiên / Thông gió cơ khí (기계환기) 명시",
                "explanation": "두 방식은 설비, 비용, 유지관리가 완전히 다르므로 반드시 구분해서 통역해야 합니다."
            }
        ],
        "examples": [
            {
                "ko": "이 터널은 2km마다 환기구를 설치합니다.",
                "vi": "Hầm này lắp đặt giếng thông gió cứ mỗi 2km.",
                "situation": "formal"
            },
            {
                "ko": "환기구에는 환기팬과 배연 댐퍼가 함께 설치됩니다.",
                "vi": "Giếng thông gió được lắp đặt cùng quạt thông gió và van xả khói.",
                "situation": "onsite"
            },
            {
                "ko": "화재 발생 시 환기구를 통해 연기를 신속히 배출합니다.",
                "vi": "Khi xảy ra hỏa hoạn, khói được thoát nhanh qua giếng thông gió.",
                "situation": "formal"
            }
        ],
        "relatedTerms": ["터널", "환기팬", "배연", "안전시설"]
    },
    {
        "slug": "tam-chong-tham-pvc",
        "korean": "방수시트",
        "vietnamese": "Tấm chống thấm PVC",
        "hanja": "防水sheet",
        "hanjaReading": "防(막을 방) + 水(물 수)",
        "pronunciation": "방수시트",
        "meaningKo": "지하구조물이나 터널에서 지하수 침투를 막기 위해 설치하는 합성수지 막으로, 주로 PVC(폴리염화비닐) 또는 EVA 재질을 사용합니다. 한국 지하공사에서는 방수시트를 흙막이벽 뒤, 터널 내벽, 지하주차장 벽체에 필수적으로 시공하며, 두께(보통 1.5~2.0mm), 겹침 폭(최소 10cm), 열융착 품질이 방수 성능의 핵심입니다. 통역 시 '비닐 같은 막'이라고 단순화하면 품질 중요성이 전달되지 않으므로 '지하수 차단', '내구성' 측면을 강조해야 합니다. 베트남에서는 'tấm chống thấm' 또는 'màng chống thấm'으로 부르며, 저가 제품 사용이 많아 한국의 고사양 방수시트(KS 인증) 시공 기준을 상세히 설명해야 합니다. 방수시트 손상 시 누수로 이어지므로 시공 중 찢어짐, 구멍 방지가 매우 중요합니다.",
        "meaningVi": "Màng nhựa tổng hợp được lắp đặt để ngăn thấm nước ngầm vào công trình ngầm hoặc hầm, chủ yếu sử dụng chất liệu PVC (polyvinyl chloride) hoặc EVA. Ở Hàn Quốc được thi công bắt buộc ở sau tường chắn đất, thành hầm, tường hầm xe. Độ dày (thường 1.5~2.0mm), độ chồng (tối thiểu 10cm), chất lượng hàn nhiệt là yếu tố chính.",
        "context": "방수공사, 지하공사, 터널",
        "culturalNote": "한국은 지하수위가 높은 지역이 많고 누수 민원이 빈번해 방수시트 품질 관리가 매우 엄격합니다. 베트남은 지하수 관리가 상대적으로 느슨하고, 방수시트도 저가 제품을 많이 씁니다. 한국 현장에서 'KS 인증 방수시트 사용'이라는 지시를 통역할 때, 베트남 인력은 'KS'가 무엇인지 모르므로 '한국 국가 품질 인증'이라고 설명해야 합니다. 또한 방수시트는 시공 후 육안 검사가 어려워 '열융착 검사', '공기주입 누수 시험' 같은 품질 확인 절차를 거치는데, 이를 '형식적 절차'가 아니라 '누수 방지 필수 작업'으로 강조해야 현장 협조도가 높아집니다.",
        "commonMistakes": [
            {
                "mistake": "Màng nilon (비닐 랩으로 오역)",
                "correction": "Tấm chống thấm PVC / Màng chống thấm chuyên dụng",
                "explanation": "'nilon'은 일회용 비닐을 연상시킵니다. 방수시트는 내구성 있는 전문 자재이므로 'chống thấm chuyên dụng'을 명시하세요."
            },
            {
                "mistake": "열융착(Heat Sealing)을 '접착'으로만 표현",
                "correction": "Hàn nhiệt / Dán hàn bằng nhiệt (열융착)",
                "explanation": "열융착은 단순 접착이 아니라 열로 녹여 붙이는 방식이므로 'hàn(용접)'을 써야 기술 용어로 인식됩니다."
            },
            {
                "mistake": "두께, 겹침 폭 기준 누락",
                "correction": "Dày 1.5~2.0mm, chồng tối thiểu 10cm",
                "explanation": "방수시트 시공의 핵심은 두께와 겹침 폭 준수이므로 이를 빠뜨리면 시공 불량으로 이어집니다."
            }
        ],
        "examples": [
            {
                "ko": "터널 내벽에 두께 2mm PVC 방수시트를 전면 시공하세요.",
                "vi": "Thi công toàn bộ thành hầm bằng tấm chống thấm PVC dày 2mm.",
                "situation": "onsite"
            },
            {
                "ko": "방수시트 겹침 부위는 열융착으로 접합하고 공기 시험을 실시합니다.",
                "vi": "Vị trí chồng của tấm chống thấm phải hàn nhiệt và thực hiện thử nghiệm khí.",
                "situation": "formal"
            },
            {
                "ko": "방수시트가 찢어지면 즉시 보수하고 기록하세요.",
                "vi": "Nếu tấm chống thấm bị rách, phải sửa ngay và ghi chép lại.",
                "situation": "onsite"
            }
        ],
        "relatedTerms": ["방수공사", "지하수", "차수", "PVC"]
    },
    {
        "slug": "tam-thoat-nuoc-drainage-board",
        "korean": "배수판",
        "vietnamese": "Tấm thoát nước (Drainage Board)",
        "hanja": "排水板",
        "hanjaReading": "排(물리칠 배) + 水(물 수) + 板(널빤지 판)",
        "pronunciation": "배수판",
        "meaningKo": "지하구조물 외벽에 설치하여 지하수를 모아 배수층으로 유도하는 판형 자재로, 한쪽 면에 돌기(dimple)가 있어 물이 흐를 수 있는 공간을 확보합니다. 한국 지하공사에서는 방수시트와 함께 필수적으로 시공되며, 배수판→방수시트→구조체 순으로 설치합니다. 통역 시 '물을 빼주는 판'이라는 기능을 설명하되, 방수시트와의 '역할 분담'(배수판=물 배출, 방수시트=물 차단)을 명확히 해야 혼동을 방지할 수 있습니다. 베트남에서는 'tấm thoát nước' 또는 'tấm dẫn nước'로 부르며, 사용 빈도가 낮아 '왜 필요한가'를 설명해야 할 때가 많습니다. 배수판은 지하수압을 줄여 구조물 안정성을 높이고, 방수시트 수명을 연장하는 효과가 있습니다.",
        "meaningVi": "Tấm hình có gờ (dimple) lắp đặt ở tường ngoài công trình ngầm để thu và dẫn nước ngầm đến lớp thoát nước. Ở Hàn Quốc được thi công bắt buộc cùng tấm chống thấm, thứ tự lắp đặt: tấm thoát nước → tấm chống thấm → kết cấu. Tấm thoát nước giảm áp lực nước ngầm, tăng độ ổn định công trình và kéo dài tuổi thọ tấm chống thấm.",
        "context": "방수공사, 지하공사, 배수",
        "culturalNote": "한국은 지하수 관리를 매우 중요시해 배수판-방수시트 이중 시스템을 표준으로 사용하지만, 베트남은 배수판 없이 방수시트만 시공하는 경우가 많습니다. 한국 현장에서 '배수판 시공'이라고 하면 베트남 인력은 '방수시트만으로 충분한데 왜?'라는 의문을 가질 수 있으므로 '지하수압 감소', '방수시트 보호' 두 가지 효과를 명확히 설명해야 합니다. 또한 배수판은 돌기(dimple) 방향이 중요한데(돌기가 구조체 쪽), 이를 통역 시 '돌기 방향 확인'이라고 강조하지 않으면 시공 오류가 발생할 수 있습니다. 배수판은 가볍고 시공이 간단하지만, 겹침 부위 처리(테이핑)를 정확히 해야 물이 빠집니다.",
        "commonMistakes": [
            {
                "mistake": "Tấm chống thấm (방수시트로 혼동)",
                "correction": "Tấm thoát nước (Drainage Board) - chức năng thoát nước, không phải chống thấm",
                "explanation": "배수판(물 배출)과 방수시트(물 차단)는 정반대 기능이므로 통역 시 반드시 구분해야 합니다."
            },
            {
                "mistake": "돌기(Dimple)를 '울퉁불퉁한 것'으로만 표현",
                "correction": "Gờ nhô (Dimple) - tạo khoảng trống cho nước chảy",
                "explanation": "'울퉁불퉁'은 모양만 설명한 것이고, '물이 흐를 공간을 만든다'는 기능을 함께 설명해야 합니다."
            },
            {
                "mistake": "시공 순서 혼동 (방수시트→배수판 역순)",
                "correction": "Tấm thoát nước (밖) → Tấm chống thấm (안) → Kết cấu (구조체)",
                "explanation": "시공 순서를 틀리면 물이 안 빠지므로 반드시 정확한 순서를 통역해야 합니다."
            }
        ],
        "examples": [
            {
                "ko": "지하 외벽에 배수판을 먼저 붙이고 그 위에 방수시트를 시공합니다.",
                "vi": "Dán tấm thoát nước lên tường ngoài hầm trước, sau đó thi công tấm chống thấm bên trên.",
                "situation": "onsite"
            },
            {
                "ko": "배수판 돌기가 구조체 쪽을 향하도록 설치하세요.",
                "vi": "Lắp đặt tấm thoát nước sao cho gờ nhô hướng về phía kết cấu.",
                "situation": "onsite"
            },
            {
                "ko": "배수판 덕분에 지하수압이 줄어 구조물이 안정됩니다.",
                "vi": "Nhờ tấm thoát nước, áp lực nước ngầm giảm và công trình ổn định hơn.",
                "situation": "formal"
            }
        ],
        "relatedTerms": ["방수시트", "지하수", "배수", "지하공사"]
    }
]

def main():
    """메인 실행 함수"""
    print(f"📂 파일 읽는 중: {file_path}")

    with open(file_path, "r", encoding="utf-8") as f:
        data = json.load(f)

    print(f"✅ 기존 용어 개수: {len(data)}개")

    # 중복 체크 (slug 기준)
    existing_slugs = {term["slug"] for term in data}
    duplicates = []
    added_count = 0

    for term in new_terms:
        if term["slug"] in existing_slugs:
            duplicates.append(term["slug"])
        else:
            data.append(term)
            existing_slugs.add(term["slug"])
            added_count += 1

    if duplicates:
        print(f"⚠️  중복된 slug (추가 안 됨): {', '.join(duplicates)}")

    print(f"➕ 신규 추가: {added_count}개")
    print(f"📊 최종 용어 개수: {len(data)}개")

    # 파일 저장
    with open(file_path, "w", encoding="utf-8") as f:
        json.dump(data, f, ensure_ascii=False, indent=2)

    print(f"💾 저장 완료: {file_path}")
    print("\n✅ 작업 완료!")
    print(f"추가된 용어: {added_count}개")
    print("다음 단계: npm run validate:terms 실행하여 Tier S 검증")

if __name__ == "__main__":
    main()
