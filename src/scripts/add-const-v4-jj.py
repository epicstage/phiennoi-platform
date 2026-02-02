#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Construction(건설) 용어 추가 스크립트 v4
테마: 환경/폐기물/건설재활용
대상: src/data/terms/construction.json
"""

import json
import os

# 추가할 10개 용어 (Tier S 기준 준수)
data = [
    {
        "slug": "phe-thai-xay-dung",
        "korean": "건설폐기물",
        "vietnamese": "Phế thải xây dựng",
        "hanja": "建設廢棄物",
        "hanjaReading": "建(세울 건) + 設(베풀 설) + 廢(버릴 폐) + 棄(버릴 기) + 物(물건 물)",
        "pronunciation": "건설페기물",
        "meaningKo": "건축물, 토목구조물 등의 건설공사로 인하여 발생하는 각종 폐자재와 폐기물. 통역 시 '건설쓰레기'가 아닌 '건설폐기물'로 정확히 번역해야 하며, 베트남에서는 재활용 의무가 한국보다 약한 편이므로 현장 관리자에게 한국 기준(분리배출, 재활용률)을 명확히 전달해야 합니다. 건설폐기물 처리계획서 통역 시 각 폐기물 종류별 처리 방법을 구체적으로 설명해야 합니다.",
        "meaningVi": "Các loại phế liệu và chất thải phát sinh từ các công trình xây dựng như nhà ở, công trình dân dụng. Bao gồm bê tông, gạch, thép, gỗ, nhựa và các vật liệu khác. Cần phân loại và tái chế theo quy định.",
        "context": "공사현장, 환경관리, 폐기물처리, 법규준수",
        "culturalNote": "한국은 건설폐기물 재활용률이 97% 이상으로 매우 높고 폐기물관리법이 엄격하지만, 베트남은 재활용 인프라가 부족하여 현장 관리자들이 한국 기준을 이해하지 못하는 경우가 많습니다. 통역사는 '재활용 의무', '분리배출', '처리비용 책임' 등을 강조하며 한국 본사와 현장 간 기준 차이를 명확히 전달해야 합니다.",
        "commonMistakes": [
            {
                "mistake": "건설쓰레기 = Rác xây dựng",
                "correction": "건설폐기물 = Phế thải xây dựng",
                "explanation": "공식 문서에서는 '쓰레기'보다 '폐기물'이 정확한 법적 용어입니다."
            },
            {
                "mistake": "폐기물 처리 = Xử lý rác",
                "correction": "폐기물 처리 = Xử lý phế thải",
                "explanation": "'Rác'은 일반 쓰레기, 'Phế thải'는 건설/산업 폐기물을 의미합니다."
            },
            {
                "mistake": "재활용 의무 없음으로 통역",
                "correction": "한국 기준 재활용 의무 97% 이상임을 명시",
                "explanation": "베트남 관리자가 한국 본사 기준을 오해하지 않도록 수치를 정확히 전달해야 합니다."
            }
        ],
        "examples": [
            {
                "ko": "건설폐기물 처리계획서를 제출해 주세요.",
                "vi": "Hãy nộp kế hoạch xử lý phế thải xây dựng.",
                "situation": "formal"
            },
            {
                "ko": "폐콘크리트는 순환골재로 재활용해야 합니다.",
                "vi": "Bê tông phế liệu phải được tái chế thành cốt liệu tuần hoàn.",
                "situation": "onsite"
            },
            {
                "ko": "건설폐기물 반출 시 반드시 분리배출해야 합니다.",
                "vi": "Khi vận chuyển phế thải xây dựng ra ngoài, bắt buộc phải phân loại.",
                "situation": "formal"
            }
        ],
        "relatedTerms": ["폐콘크리트", "순환골재", "분리배출", "폐기물관리법"]
    },
    {
        "slug": "phe-be-tong",
        "korean": "폐콘크리트",
        "vietnamese": "Phế bê tông",
        "hanja": "廢-",
        "hanjaReading": "廢(버릴 폐)",
        "pronunciation": "페콘크리트",
        "meaningKo": "건설공사 중 발생한 콘크리트 구조물의 해체물이나 잔재. 통역 시 '부숴진 콘크리트'보다 '폐콘크리트'가 정확하며, 베트남 현장에서는 재활용 개념이 약해 그냥 버리려는 경향이 있으므로 '순환골재로 재활용 가능'하다는 점을 강조해야 합니다. 폐콘크리트 파쇄 및 재활용 공정 설명 시 기술 용어를 정확히 전달해야 합니다.",
        "meaningVi": "Bê tông phế liệu từ công trình xây dựng bị phá dỡ hoặc còn thừa. Có thể tái chế thành cốt liệu tuần hoàn (cốt liệu tái chế) để sử dụng lại trong xây dựng, giảm lãng phí tài nguyên và chi phí.",
        "context": "폐기물처리, 재활용, 순환골재, 친환경공법",
        "culturalNote": "한국은 폐콘크리트를 파쇄하여 순환골재로 재활용하는 기술이 발달했지만, 베트남은 재활용 인프라가 부족해 대부분 매립 처리됩니다. 통역사는 한국 본사가 요구하는 '재활용률', '순환골재 사용 비율' 등을 현장에 정확히 전달하되, 현지 여건을 본사에 피드백해야 합니다.",
        "commonMistakes": [
            {
                "mistake": "부숴진 콘크리트 = Bê tông vỡ",
                "correction": "폐콘크리트 = Phế bê tông",
                "explanation": "'Vỡ'는 단순히 깨진 상태, 'Phế'는 폐기물로서의 법적 지위를 나타냅니다."
            },
            {
                "mistake": "재활용 불가능으로 통역",
                "correction": "순환골재로 재활용 가능함을 명시",
                "explanation": "베트남 관리자가 폐콘크리트를 버리려 할 때 재활용 가능성을 알려야 합니다."
            },
            {
                "mistake": "폐콘크리트 = Rác bê tông",
                "correction": "폐콘크리트 = Phế bê tông",
                "explanation": "'Rác'은 일반 쓰레기를 의미하므로 공식 용어로 부적절합니다."
            }
        ],
        "examples": [
            {
                "ko": "폐콘크리트는 파쇄기로 분쇄하여 순환골재로 만듭니다.",
                "vi": "Phế bê tông được nghiền bằng máy nghiền để tạo thành cốt liệu tuần hoàn.",
                "situation": "onsite"
            },
            {
                "ko": "이 현장에서 발생한 폐콘크리트는 전량 재활용 처리합니다.",
                "vi": "Toàn bộ phế bê tông phát sinh tại công trường này đều được tái chế.",
                "situation": "formal"
            },
            {
                "ko": "폐콘크리트를 아무 데나 버리면 안 됩니다.",
                "vi": "Không được vứt phế bê tông bừa bãi.",
                "situation": "onsite"
            }
        ],
        "relatedTerms": ["순환골재", "건설폐기물", "파쇄기", "재활용"]
    },
    {
        "slug": "cot-lieu-tuan-hoan",
        "korean": "순환골재",
        "vietnamese": "Cốt liệu tuần hoàn",
        "hanja": "循環骨材",
        "hanjaReading": "循(돌 순) + 環(고리 환) + 骨(뼈 골) + 材(재목 재)",
        "pronunciation": "순환골재",
        "meaningKo": "폐콘크리트를 파쇄·선별하여 다시 골재로 사용할 수 있도록 재활용한 것. 통역 시 '재활용 골재'보다 '순환골재'가 정확하며, 베트남에서는 생소한 개념이므로 '폐콘크리트를 다시 사용할 수 있게 만든 골재'로 풀어서 설명해야 합니다. 순환골재 품질 기준 설명 시 한국 KS 기준을 베트남 엔지니어가 이해할 수 있도록 구체적 수치를 제시해야 합니다.",
        "meaningVi": "Cốt liệu được tái chế từ phế bê tông sau khi nghiền và phân loại, có thể sử dụng lại trong sản xuất bê tông hoặc công trình đường. Giúp tiết kiệm tài nguyên thiên nhiên và giảm chi phí.",
        "context": "재활용, 친환경건설, 자원절약, 품질관리",
        "culturalNote": "한국은 순환골재 사용을 의무화(공공공사 일정 비율 이상 사용)하지만, 베트남은 순환골재 사용이 거의 없고 품질 기준도 명확하지 않습니다. 통역사는 한국 본사의 순환골재 사용 요구를 현장에 전달하되, '천연골재 대비 품질이 떨어지지 않는다'는 점을 강조하여 현장 엔지니어의 우려를 해소해야 합니다.",
        "commonMistakes": [
            {
                "mistake": "재활용 골재 = Cốt liệu tái chế",
                "correction": "순환골재 = Cốt liệu tuần hoàn",
                "explanation": "'Tuần hoàn'은 순환 개념을 포함한 공식 용어입니다."
            },
            {
                "mistake": "품질이 낮다고 통역",
                "correction": "한국 KS 기준 충족 시 천연골재와 동등함을 명시",
                "explanation": "베트남 엔지니어가 품질을 의심하지 않도록 기준을 명확히 전달해야 합니다."
            },
            {
                "mistake": "순환골재 = Đá tái chế",
                "correction": "순환골재 = Cốt liệu tuần hoàn",
                "explanation": "'Đá'는 돌, 'Cốt liệu'는 골재(콘크리트 재료)를 의미합니다."
            }
        ],
        "examples": [
            {
                "ko": "이 공사에는 순환골재를 30% 이상 사용해야 합니다.",
                "vi": "Công trình này phải sử dụng trên 30% cốt liệu tuần hoàn.",
                "situation": "formal"
            },
            {
                "ko": "순환골재 품질이 KS 기준을 충족하는지 확인해 주세요.",
                "vi": "Hãy kiểm tra xem chất lượng cốt liệu tuần hoàn có đạt tiêu chuẩn KS không.",
                "situation": "onsite"
            },
            {
                "ko": "순환골재는 천연골재보다 저렴하고 환경에도 좋습니다.",
                "vi": "Cốt liệu tuần hoàn rẻ hơn cốt liệu tự nhiên và cũng tốt cho môi trường.",
                "situation": "informal"
            }
        ],
        "relatedTerms": ["폐콘크리트", "골재", "친환경건설", "KS기준"]
    },
    {
        "slug": "bi-san-bui",
        "korean": "비산먼지",
        "vietnamese": "Bụi bay",
        "hanja": "飛散-",
        "hanjaReading": "飛(날 비) + 散(흩을 산)",
        "pronunciation": "비산먼지",
        "meaningKo": "공사장에서 바람에 날려 흩어지는 먼지. 통역 시 '날리는 먼지'보다 '비산먼지'가 정확하며, 베트남 현장에서는 비산먼지 관리를 소홀히 하는 경우가 많아 주민 민원이 발생하므로 '살수차 운영', '방진막 설치', '차량 세륜' 등 구체적 대책을 강조해야 합니다. 환경영향평가 통역 시 비산먼지 저감 대책을 명확히 전달해야 합니다.",
        "meaningVi": "Bụi phát sinh từ công trường xây dựng bị gió thổi bay ra xung quanh, gây ô nhiễm không khí và ảnh hưởng đến sức khỏe người dân. Cần có biện pháp kiểm soát như phun nước, lắp màn chắn bụi.",
        "context": "환경관리, 공해방지, 주민민원, 법규준수",
        "culturalNote": "한국은 비산먼지 관리 법규가 엄격하여 살수차 운영, 방진막 설치 등이 의무화되어 있지만, 베트남은 규제가 느슨해 현장에서 비용 절감을 위해 대책을 생략하는 경우가 많습니다. 통역사는 '주민 민원 발생 시 공사 중단 가능성'을 강조하며 현장 관리자가 예방 조치를 취하도록 유도해야 합니다.",
        "commonMistakes": [
            {
                "mistake": "날리는 먼지 = Bụi bay",
                "correction": "비산먼지 = Bụi bay (공식 용어로는 동일하나 맥락 강조)",
                "explanation": "공식 문서에서는 '비산먼지'라는 법적 용어를 사용해야 합니다."
            },
            {
                "mistake": "먼지 관리 필요 없다고 통역",
                "correction": "한국 기준 비산먼지 관리 의무 있음을 명시",
                "explanation": "베트남 관리자가 규제를 무시하지 않도록 법적 책임을 전달해야 합니다."
            },
            {
                "mistake": "비산먼지 = Bụi xây dựng",
                "correction": "비산먼지 = Bụi bay",
                "explanation": "'Bụi xây dựng'은 건설 먼지 전반, 'Bụi bay'는 날리는 먼지를 의미합니다."
            }
        ],
        "examples": [
            {
                "ko": "비산먼지 방지를 위해 하루 3회 이상 살수해야 합니다.",
                "vi": "Để ngăn bụi bay, phải phun nước ít nhất 3 lần mỗi ngày.",
                "situation": "onsite"
            },
            {
                "ko": "비산먼지로 인한 주민 민원이 발생하지 않도록 방진막을 설치하세요.",
                "vi": "Hãy lắp màn chắn bụi để không xảy ra khiếu nại của dân cư do bụi bay.",
                "situation": "formal"
            },
            {
                "ko": "오늘 바람이 강하니 비산먼지 관리 철저히 하세요.",
                "vi": "Hôm nay gió mạnh nên hãy quản lý bụi bay thật kỹ.",
                "situation": "informal"
            }
        ],
        "relatedTerms": ["살수차", "방진막", "환경관리", "주민민원"]
    },
    {
        "slug": "tuong-cach-am",
        "korean": "방음벽",
        "vietnamese": "Tường cách âm",
        "hanja": "防音壁",
        "hanjaReading": "防(막을 방) + 音(소리 음) + 壁(벽 벽)",
        "pronunciation": "방음벽",
        "meaningKo": "소음을 차단하기 위해 설치하는 벽. 통역 시 '소음 막는 벽'보다 '방음벽'이 정확하며, 베트남 현장에서는 방음벽 설치를 비용으로만 여겨 생략하려는 경향이 있으므로 '주민 민원 예방', '법적 의무' 측면을 강조해야 합니다. 방음벽 설치 기준 및 소음 측정 방법을 설명할 때 한국 환경부 기준을 명확히 전달해야 합니다.",
        "meaningVi": "Tường được xây hoặc lắp đặt để ngăn chặn tiếng ồn từ công trường truyền ra khu dân cư. Thường làm bằng tấm panel cách âm hoặc bê tông, cao từ 2-5m tùy mức độ ồn.",
        "context": "소음관리, 환경대책, 주민민원, 법규준수",
        "culturalNote": "한국은 주거지역 인근 공사 시 방음벽 설치가 의무화되어 있고 소음 기준(주간 70dB, 야간 60dB 이하)이 엄격하지만, 베트남은 규제가 느슨하여 현장에서 방음벽을 설치하지 않는 경우가 많습니다. 통역사는 한국 본사의 방음벽 설치 요구를 전달하되, 현지 규제 수준을 본사에 피드백하여 현실적 대안을 찾도록 도와야 합니다.",
        "commonMistakes": [
            {
                "mistake": "소음 막는 벽 = Tường chặn tiếng ồn",
                "correction": "방음벽 = Tường cách âm",
                "explanation": "'Cách âm'은 방음의 공식 용어입니다."
            },
            {
                "mistake": "방음벽 설치 필요 없다고 통역",
                "correction": "한국 기준 주거지역 인근 공사 시 방음벽 의무 설치임을 명시",
                "explanation": "베트남 관리자가 법적 책임을 인지하도록 해야 합니다."
            },
            {
                "mistake": "방음벽 = Tường chống ồn",
                "correction": "방음벽 = Tường cách âm",
                "explanation": "'Chống ồn'은 소음 대책 일반, 'Cách âm'은 방음벽 특정 용어입니다."
            }
        ],
        "examples": [
            {
                "ko": "주거지역과 가까우니 높이 3m 방음벽을 설치하세요.",
                "vi": "Gần khu dân cư nên hãy lắp tường cách âm cao 3m.",
                "situation": "onsite"
            },
            {
                "ko": "방음벽 설치 후 소음을 측정하여 기준치 이하인지 확인하세요.",
                "vi": "Sau khi lắp tường cách âm, hãy đo tiếng ồn để xác nhận dưới ngưỡng quy định.",
                "situation": "formal"
            },
            {
                "ko": "방음벽이 제대로 설치되지 않아 주민 민원이 들어왔습니다.",
                "vi": "Do tường cách âm không được lắp đúng cách nên có khiếu nại của dân cư.",
                "situation": "informal"
            }
        ],
        "relatedTerms": ["소음측정", "주민민원", "환경관리", "데시벨(dB)"]
    },
    {
        "slug": "man-chong-tham",
        "korean": "차수막",
        "vietnamese": "Màn chống thấm",
        "hanja": "遮水幕",
        "hanjaReading": "遮(가릴 차) + 水(물 수) + 幕(막 막)",
        "pronunciation": "차수막",
        "meaningKo": "지하수나 빗물이 공사 현장으로 들어오는 것을 막기 위해 설치하는 차단막. 통역 시 '물 막는 막'보다 '차수막'이 정확하며, 베트남 우기에는 차수막 설치가 필수적이므로 '지하수 유입 방지', '굴착면 붕괴 예방' 측면을 강조해야 합니다. 흙막이 공사와 함께 차수막 설치 방법을 설명할 때 기술 용어를 정확히 전달해야 합니다.",
        "meaningVi": "Màn hoặc tấm chống thấm được lắp đặt để ngăn nước ngầm hoặc nước mưa xâm nhập vào khu vực thi công, đặc biệt trong công trình đào móng sâu. Giúp bảo vệ kết cấu và an toàn công trình.",
        "context": "굴착공사, 지하공사, 우기대책, 안전관리",
        "culturalNote": "한국은 지하 굴착 공사 시 차수막 설치가 표준 공법이지만, 베트남은 우기(5~10월) 강수량이 많아 차수막 설치가 더욱 중요함에도 현장에서 비용 절감을 위해 생략하는 경우가 많습니다. 통역사는 '차수막 미설치 시 굴착면 붕괴 및 공사 지연 위험'을 강조하여 현장 관리자가 예방 조치를 취하도록 해야 합니다.",
        "commonMistakes": [
            {
                "mistake": "물 막는 막 = Màn chặn nước",
                "correction": "차수막 = Màn chống thấm",
                "explanation": "'Chống thấm'은 방수·차수의 공식 용어입니다."
            },
            {
                "mistake": "우기에만 필요하다고 통역",
                "correction": "지하수 유입 방지를 위해 굴착 공사 시 항상 필요함을 명시",
                "explanation": "건기에도 지하수가 있으므로 차수막 설치는 필수입니다."
            },
            {
                "mistake": "차수막 = Màn chắn nước",
                "correction": "차수막 = Màn chống thấm",
                "explanation": "'Chống thấm'이 차수·방수의 정확한 용어입니다."
            }
        ],
        "examples": [
            {
                "ko": "지하 3층까지 굴착하니 차수막을 반드시 설치하세요.",
                "vi": "Do đào sâu đến tầng hầm 3 nên nhất định phải lắp màn chống thấm.",
                "situation": "onsite"
            },
            {
                "ko": "우기가 시작되기 전에 차수막 설치를 완료해야 합니다.",
                "vi": "Phải hoàn thành lắp màn chống thấm trước khi mùa mưa bắt đầu.",
                "situation": "formal"
            },
            {
                "ko": "차수막이 제대로 안 되어서 지하수가 들어오고 있어요.",
                "vi": "Màn chống thấm không kín nên nước ngầm đang lọt vào.",
                "situation": "informal"
            }
        ],
        "relatedTerms": ["흙막이공사", "지하굴착", "방수공사", "우기대책"]
    },
    {
        "slug": "man-chong-duc",
        "korean": "오탁방지막",
        "vietnamese": "Màn chống đục",
        "hanja": "汚濁防止幕",
        "hanjaReading": "汚(더러울 오) + 濁(흐릴 탁) + 防(막을 방) + 止(그칠 지) + 幕(막 막)",
        "pronunciation": "오탁방지막",
        "meaningKo": "해상이나 하천 공사 시 흙탕물이 주변 수역으로 퍼지는 것을 막기 위해 설치하는 막. 통역 시 '탁수 막는 막'보다 '오탁방지막'이 정확하며, 베트남에서는 수질 오염 관리가 느슨하여 현장에서 생략하려는 경향이 있으므로 '어업 피해 방지', '환경 규제 준수' 측면을 강조해야 합니다. 해상 공사 환경영향평가 통역 시 오탁방지막 설치 범위 및 방법을 명확히 전달해야 합니다.",
        "meaningVi": "Màn hoặc rèm được lắp đặt trong nước để ngăn cản bùn đất, trầm tích lan tràn ra khu vực xung quanh khi thi công dưới nước hoặc ven sông biển. Bảo vệ môi trường nước và sinh vật thủy sinh.",
        "context": "해상공사, 하천공사, 수질관리, 환경보호",
        "culturalNote": "한국은 해상 및 하천 공사 시 오탁방지막 설치가 환경영향평가 조건으로 의무화되어 있고 수질 측정도 엄격하지만, 베트남은 규제가 느슨하여 현장에서 비용 절감을 위해 설치를 생략하는 경우가 많습니다. 통역사는 '어업 피해 보상 소송', '공사 중단 위험'을 강조하며 현장 관리자가 예방 조치를 취하도록 해야 합니다.",
        "commonMistakes": [
            {
                "mistake": "탁수 막는 막 = Màn chặn nước đục",
                "correction": "오탁방지막 = Màn chống đục",
                "explanation": "'Chống đục'이 오탁 방지의 공식 용어입니다."
            },
            {
                "mistake": "육상 공사에도 필요하다고 통역",
                "correction": "해상·하천 공사 시에만 필요함을 명시",
                "explanation": "오탁방지막은 수중·수변 공사에 특화된 장비입니다."
            },
            {
                "mistake": "오탁방지막 = Màn lọc nước",
                "correction": "오탁방지막 = Màn chống đục",
                "explanation": "'Lọc nước'는 정수, 'Chống đục'은 오탁 방지를 의미합니다."
            }
        ],
        "examples": [
            {
                "ko": "항만 준설 공사 시 오탁방지막을 설치하여 수질 오염을 막으세요.",
                "vi": "Khi nạo vét cảng, hãy lắp màn chống đục để ngăn ô nhiễm nước.",
                "situation": "formal"
            },
            {
                "ko": "오탁방지막 안쪽에서만 준설 작업을 진행하세요.",
                "vi": "Chỉ tiến hành nạo vét bên trong màn chống đục thôi.",
                "situation": "onsite"
            },
            {
                "ko": "강풍으로 오탁방지막이 떠내려갔습니다.",
                "vi": "Màn chống đục bị trôi mất do gió mạnh.",
                "situation": "informal"
            }
        ],
        "relatedTerms": ["준설공사", "수질관리", "해상공사", "환경영향평가"]
    },
    {
        "slug": "thiet-bi-rua-xe",
        "korean": "세륜세차시설",
        "vietnamese": "Thiết bị rửa xe",
        "hanja": "洗輪洗車施設",
        "hanjaReading": "洗(씻을 세) + 輪(바퀴 륜) + 洗(씻을 세) + 車(수레 차) + 施(베풀 시) + 設(베풀 설)",
        "pronunciation": "세륜세차시설",
        "meaningKo": "공사장을 출입하는 차량의 바퀴와 차체를 씻는 시설. 통역 시 '차 씻는 곳'보다 '세륜세차시설'이 정확하며, 베트남 현장에서는 비용 절감을 위해 생략하는 경우가 많아 공사 차량이 흙을 묻힌 채 도로로 나가 민원이 발생하므로 '도로 오염 방지', '법적 의무' 측면을 강조해야 합니다. 세륜세차시설 설치 기준 및 운영 방법을 설명할 때 구체적 절차를 전달해야 합니다.",
        "meaningVi": "Thiết bị rửa bánh xe và thân xe tại cổng ra vào công trường để loại bỏ bùn đất, tránh làm bẩn đường công cộng. Thường bao gồm bể nước, vòi phun áp lực và hệ thống thoát nước.",
        "context": "환경관리, 공사장출입관리, 도로청결, 법규준수",
        "culturalNote": "한국은 대형 공사장에 세륜세차시설 설치가 의무화되어 있고 미설치 시 과태료가 부과되지만, 베트남은 규제가 느슨하여 현장에서 간이 호스로만 씻거나 아예 씻지 않고 출입하는 경우가 많습니다. 통역사는 '도로 오염으로 인한 민원 발생 시 공사 중단 가능성'을 강조하며 현장 관리자가 예방 조치를 취하도록 해야 합니다.",
        "commonMistakes": [
            {
                "mistake": "차 씻는 곳 = Nơi rửa xe",
                "correction": "세륜세차시설 = Thiết bị rửa xe (공식 시설 개념)",
                "explanation": "'Thiết bị'는 장비·시설을 의미하는 공식 용어입니다."
            },
            {
                "mistake": "간이 호스로 충분하다고 통역",
                "correction": "세륜세차시설(자동 또는 고압 세척) 설치 의무 있음을 명시",
                "explanation": "베트남 관리자가 법적 기준을 오해하지 않도록 해야 합니다."
            },
            {
                "mistake": "세륜세차시설 = Máy rửa xe",
                "correction": "세륜세차시설 = Thiết bị rửa xe (시설 개념)",
                "explanation": "'Máy'는 기계, 'Thiết bị'는 시설·장비를 의미합니다."
            }
        ],
        "examples": [
            {
                "ko": "공사장 출구에 세륜세차시설을 설치하고 모든 차량이 씻고 나가도록 하세요.",
                "vi": "Hãy lắp thiết bị rửa xe tại cổng ra và yêu cầu mọi xe phải rửa trước khi ra ngoài.",
                "situation": "formal"
            },
            {
                "ko": "세륜세차시설에서 바퀴를 제대로 안 씻어서 도로가 더러워졌어요.",
                "vi": "Do không rửa bánh xe kỹ ở thiết bị rửa xe nên đường bị bẩn.",
                "situation": "informal"
            },
            {
                "ko": "우기에는 세륜세차시설을 더 자주 점검하세요.",
                "vi": "Trong mùa mưa, hãy kiểm tra thiết bị rửa xe thường xuyên hơn.",
                "situation": "onsite"
            }
        ],
        "relatedTerms": ["비산먼지", "도로청결", "공사장출입관리", "환경관리"]
    },
    {
        "slug": "tieng-on-xay-dung",
        "korean": "건설소음",
        "vietnamese": "Tiếng ồn xây dựng",
        "hanja": "建設騷音",
        "hanjaReading": "建(세울 건) + 設(베풀 설) + 騷(시끄러울 소) + 音(소리 음)",
        "pronunciation": "건설소음",
        "meaningKo": "건설공사 중 발생하는 소음. 통역 시 '공사 소리'보다 '건설소음'이 정확하며, 베트남 현장에서는 야간 공사 시에도 소음 관리를 소홀히 하여 주민 민원이 발생하므로 '소음 기준치(주간 70dB, 야간 60dB)', '방음벽 설치', '저소음 공법' 등을 강조해야 합니다. 환경영향평가 통역 시 소음 측정 위치 및 기준을 명확히 전달해야 합니다.",
        "meaningVi": "Tiếng ồn phát sinh từ hoạt động xây dựng như đào đất, đóng cọc, vận chuyển vật liệu. Cần kiểm soát để không vượt ngưỡng cho phép, đặc biệt ở khu dân cư và ban đêm.",
        "context": "환경관리, 소음규제, 주민민원, 법규준수",
        "culturalNote": "한국은 주거지역 인근 건설소음 기준이 엄격(주간 70dB, 야간 60dB 이하)하고 야간 공사 시 사전 신고 의무가 있지만, 베트남은 규제가 느슨하여 현장에서 야간에도 공사를 진행하다가 주민 민원이 발생하는 경우가 많습니다. 통역사는 한국 본사의 소음 관리 요구를 전달하되, '주민 민원 발생 시 공사 중단 및 배상 위험'을 강조하여 현장 관리자가 예방 조치를 취하도록 해야 합니다.",
        "commonMistakes": [
            {
                "mistake": "공사 소리 = Tiếng xây dựng",
                "correction": "건설소음 = Tiếng ồn xây dựng",
                "explanation": "'Tiếng ồn'은 소음(규제 대상), 'Tiếng'은 단순 소리를 의미합니다."
            },
            {
                "mistake": "야간 공사 가능하다고 통역",
                "correction": "야간 공사 시 소음 기준 더 엄격(60dB 이하) 및 사전 신고 필요함을 명시",
                "explanation": "베트남 관리자가 법적 제약을 인지하도록 해야 합니다."
            },
            {
                "mistake": "건설소음 = Ồn ào công trường",
                "correction": "건설소음 = Tiếng ồn xây dựng",
                "explanation": "'Ồn ào'는 시끄럽다는 형용사, 'Tiếng ồn'은 소음(명사)입니다."
            }
        ],
        "examples": [
            {
                "ko": "건설소음이 기준치를 초과하여 주민 민원이 들어왔습니다.",
                "vi": "Tiếng ồn xây dựng vượt ngưỡng quy định nên có khiếu nại của dân cư.",
                "situation": "formal"
            },
            {
                "ko": "야간 공사를 하려면 건설소음을 60dB 이하로 유지해야 합니다.",
                "vi": "Nếu thi công ban đêm, phải giữ tiếng ồn xây dựng dưới 60dB.",
                "situation": "onsite"
            },
            {
                "ko": "건설소음 때문에 주민들이 항의하러 왔어요.",
                "vi": "Dân cư đến phản đối vì tiếng ồn xây dựng.",
                "situation": "informal"
            }
        ],
        "relatedTerms": ["방음벽", "소음측정", "데시벨(dB)", "주민민원"]
    },
    {
        "slug": "do-rung-dong",
        "korean": "진동측정",
        "vietnamese": "Đo rung động",
        "hanja": "振動測定",
        "hanjaReading": "振(떨 진) + 動(움직일 동) + 測(헤아릴 측) + 定(정할 정)",
        "pronunciation": "진동측정",
        "meaningKo": "공사로 인한 지반 진동의 크기를 측정하는 것. 통역 시 '진동 재기'보다 '진동측정'이 정확하며, 베트남 현장에서는 진동 관리를 소홀히 하여 인근 건물 균열 등의 피해가 발생하므로 '발파 공사', '항타 공사' 시 진동 기준치(0.5cm/s 이하) 및 측정 의무를 강조해야 합니다. 환경영향평가 통역 시 진동 측정 위치 및 방법을 명확히 전달해야 합니다.",
        "meaningVi": "Việc đo lường độ rung động của nền đất do hoạt động xây dựng gây ra, như đóng cọc, nổ mìn. Cần kiểm soát để không gây hư hại cho công trình xung quanh.",
        "context": "안전관리, 환경관리, 건물보호, 법규준수",
        "culturalNote": "한국은 발파·항타 공사 시 진동측정이 의무화되어 있고 기준치(0.5cm/s 이하) 초과 시 공사 중단되지만, 베트남은 규제가 느슨하여 현장에서 진동 측정을 생략하다가 인근 건물 균열 등의 피해가 발생하는 경우가 많습니다. 통역사는 '진동 피해 보상 소송', '공사 중단 위험'을 강조하며 현장 관리자가 예방 조치를 취하도록 해야 합니다.",
        "commonMistakes": [
            {
                "mistake": "진동 재기 = Đo rung",
                "correction": "진동측정 = Đo rung động",
                "explanation": "'Rung động'은 진동의 공식 용어입니다."
            },
            {
                "mistake": "모든 공사에서 필요하다고 통역",
                "correction": "발파·항타 등 진동 발생 공사 시에만 필요함을 명시",
                "explanation": "일반 공사에서는 진동측정 의무가 없습니다."
            },
            {
                "mistake": "진동측정 = Đo độ rung",
                "correction": "진동측정 = Đo rung động",
                "explanation": "'Rung động'이 진동의 정확한 용어입니다."
            }
        ],
        "examples": [
            {
                "ko": "항타 공사 전에 인근 건물 3곳에 진동측정기를 설치하세요.",
                "vi": "Trước khi đóng cọc, hãy lắp máy đo rung động tại 3 công trình lân cận.",
                "situation": "onsite"
            },
            {
                "ko": "진동측정 결과가 기준치를 초과하여 공사를 중단해야 합니다.",
                "vi": "Kết quả đo rung động vượt ngưỡng quy định nên phải dừng thi công.",
                "situation": "formal"
            },
            {
                "ko": "진동이 너무 심해서 주민들이 항의하고 있어요.",
                "vi": "Rung động quá mạnh nên dân cư đang phản đối.",
                "situation": "informal"
            }
        ],
        "relatedTerms": ["항타공사", "발파공사", "건물균열", "안전관리"]
    }
]

# 파일 경로
project_root = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
json_path = os.path.join(project_root, "data", "terms", "construction.json")

# 기존 파일 읽기
try:
    with open(json_path, "r", encoding="utf-8") as f:
        existing_terms = json.load(f)
    print(f"✅ 기존 파일 로드 완료: {len(existing_terms)}개 용어")
except FileNotFoundError:
    print(f"❌ 파일을 찾을 수 없습니다: {json_path}")
    exit(1)

# 새 용어 추가
existing_terms.extend(data)
print(f"✅ 새 용어 {len(data)}개 추가됨 → 총 {len(existing_terms)}개")

# 저장
with open(json_path, "w", encoding="utf-8") as f:
    json.dump(existing_terms, f, ensure_ascii=False, indent=2)

print(f"✅ 저장 완료: {json_path}")
print(f"📊 최종 용어 수: {len(existing_terms)}개")
