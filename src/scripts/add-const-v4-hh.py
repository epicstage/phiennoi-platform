#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Construction Terms Batch Add Script v4 - 댐/수자원/하천
Theme: Dam, Water Resources, River Engineering
Target: 10 terms (Concrete Dam, Fill Dam, Spillway, Intake Tower, Reservoir, Revetment, Levee, Sluice Gate, Fish Ladder, River Bed Protection)
Quality: Tier S (90+ score) - All fields required
"""

import json
import os

# 10개 용어 데이터 (Tier S 기준)
data = [
    {
        "slug": "dap-be-tong",
        "korean": "콘크리트댐",
        "vietnamese": "Đập bê tông",
        "hanja": "concrete댐",
        "hanjaReading": None,
        "pronunciation": "ḍắp be tông",
        "meaningKo": "콘크리트를 주재료로 하여 축조한 댐. 중력식댐, 아치댐, 버트리스댐 등으로 구분되며 내구성과 수밀성이 우수함. 통역 시 '중력식(trọng lực)', '아치형(vòm cung)' 등 댐 형식을 함께 언급해야 하며, 베트남에서는 최근 수력발전용으로 많이 건설되므로 'thủy điện(수력발전)'과 연계하여 이해할 것. 시공 시 콘크리트 품질관리(kiểm soát chất lượng bê tông)가 핵심이며, 한국은 계절별 타설온도 관리를 강조하나 베트남은 고온다습 환경에서의 양생(bảo dưỡng)을 더 중시함.",
        "meaningVi": "Đập được xây dựng chủ yếu bằng bê tông, phân loại thành đập trọng lực, đập vòm cung, đập chống đỡ. Có độ bền và khả năng chống thấm cao. Khi phiên dịch cần nêu rõ loại đập (trọng lực, vòm cung...) và liên kết với mục đích thủy điện nếu có.",
        "context": "수자원개발, 수력발전, 댐 안전진단",
        "culturalNote": "한국은 산악지형이 많아 소규모 다목적댐이 많으며 안전관리법(댐안전법)이 엄격함. 베트남은 메콩강 유역 대형댐 건설이 증가하고 있으며, 환경영향평가(EIA) 및 하류 국가와의 협의가 중요함. 한국은 '댐'이라는 단어를 일반적으로 사용하나 베트남은 'hồ chứa(저수지)'와 'đập(댐)'을 혼용하므로 맥락에 따라 구분 필요.",
        "commonMistakes": [
            {
                "mistake": "đập xi măng",
                "correction": "đập bê tông",
                "explanation": "xi măng은 시멘트(cement)를 의미하며 đập bê tông(콘크리트댐)이 정확한 표현. 콘크리트는 시멘트+골재+물의 혼합물임."
            },
            {
                "mistake": "댐 형식 구분 없이 일괄 번역",
                "correction": "중력식댐(đập trọng lực), 아치댐(đập vòm), 버트리스댐(đập chống đỡ) 등으로 세분화",
                "explanation": "댐 형식에 따라 구조와 시공법이 다르므로 정확한 분류가 필수."
            },
            {
                "mistake": "hồ chứa nước",
                "correction": "đập (댐 구조물 자체) vs hồ chứa (저수지/저장공간)",
                "explanation": "댐은 구조물, 저수지는 댐에 의해 만들어진 수역. 통역 시 문맥 파악 필요."
            }
        ],
        "examples": [
            {
                "ko": "이 콘크리트댐은 중력식 댐으로 설계되어 자중으로 수압을 지지합니다.",
                "vi": "Đập bê tông này được thiết kế theo kiểu đập trọng lực, dựa vào trọng lượng bản thân để chống lại áp lực nước.",
                "situation": "formal"
            },
            {
                "ko": "콘크리트 타설 시 온도관리 철저히 해야 돼요.",
                "vi": "Khi đổ bê tông phải kiểm soát nhiệt độ cẩn thận.",
                "situation": "onsite"
            },
            {
                "ko": "이 댐의 설계수명은 100년입니다.",
                "vi": "Tuổi thọ thiết kế của đập này là 100 năm.",
                "situation": "formal"
            }
        ],
        "relatedTerms": ["필댐", "여수로", "취수탑", "댐 안전진단"]
    },
    {
        "slug": "dap-dat",
        "korean": "필댐",
        "vietnamese": "Đập đất",
        "hanja": "fill댐",
        "hanjaReading": None,
        "pronunciation": "ḍắp ḍất",
        "meaningKo": "흙, 모래, 자갈 등 토사재료를 쌓아 축조한 댐. 시공이 비교적 간편하고 재료 조달이 용이하나 누수 방지를 위한 차수벽(chống thấm) 설치가 필수. 통역 시 '균일형(đồng nhất)', '존형(phân vùng)' 등 필댐 형식을 구분해야 하며, 베트남은 농업용 소규모 저수지에 많이 사용됨. 한국은 제체 안정성 평가 시 사면안전율(hệ số an toàn mái dốc)을 중시하나, 베트nam은 우기 침식(xói mòn mùa mưa) 방지에 더 집중함.",
        "meaningVi": "Đập được xây dựng bằng vật liệu đất đá như đất, cát, sỏi. Thi công đơn giản và dễ cung cấp vật liệu, nhưng bắt buộc phải có màng chống thấm. Phổ biến cho hồ chứa nông nghiệp quy mô nhỏ tại Việt Nam.",
        "context": "농업용 저수지, 관개시설, 소규모 댐 건설",
        "culturalNote": "한국은 필댐을 주로 농업용수 확보용으로 건설하며, 저수지 관리는 한국농어촌공사가 담당. 베트남은 지방정부 주도로 소규모 필댐이 많으며, 유지관리 예산 부족으로 노후화된 댐이 많음. 한국은 '필댐'이라는 용어를 사용하나 베트남에서는 '흙댐(đập đất)' 또는 '석축댐(đập đá)'으로 세분화.",
        "commonMistakes": [
            {
                "mistake": "đập đất đá",
                "correction": "đập đất (필댐) vs đập đá (rockfill dam/석축댐)",
                "explanation": "필댐은 주로 흙을 사용하며, 석축댐은 돌을 주재료로 함. 혼용 주의."
            },
            {
                "mistake": "차수벽을 '방수벽'으로 번역",
                "correction": "màng chống thấm (차수막) 또는 lõi chống thấm (차수 코어)",
                "explanation": "필댐의 차수는 누수 방지가 핵심이므로 chống thấm이 정확함."
            },
            {
                "mistake": "제체를 'thân đập'으로만 표현",
                "correction": "제체 구성요소 세분화: lõi (코어), vỏ (쉘), bệ (베이스) 등",
                "explanation": "필댐은 존형 구조이므로 각 부분의 역할을 정확히 전달해야 함."
            }
        ],
        "examples": [
            {
                "ko": "이 필댐은 중심 차수벽형으로 설계되었습니다.",
                "vi": "Đập đất này được thiết kế với lõi chống thấm ở giữa.",
                "situation": "formal"
            },
            {
                "ko": "사면 안정성 검토 결과 추가 보강이 필요합니다.",
                "vi": "Kết quả kiểm tra độ ổn định mái dốc cho thấy cần gia cố thêm.",
                "situation": "formal"
            },
            {
                "ko": "제체에 균열 확인했으니까 긴급 보수해야 돼요.",
                "vi": "Phát hiện vết nứt trên thân đập, cần sửa chữa khẩn cấp.",
                "situation": "onsite"
            }
        ],
        "relatedTerms": ["콘크리트댐", "차수벽", "사면안정", "제체"]
    },
    {
        "slug": "cong-tran",
        "korean": "여수로",
        "vietnamese": "Cống tràn",
        "hanja": "餘水路",
        "hanjaReading": "남을 여(餘) + 물 수(水) + 길 로(路)",
        "pronunciation": "công trần",
        "meaningKo": "댐에서 계획홍수량을 초과하는 물을 안전하게 하류로 방류하기 위한 수공구조물. 댐 안전의 핵심시설로, 설계홍수량(lưu lượng thiết kế) 산정이 매우 중요함. 통역 시 '자유월류식(tràn tự do)', '제어식(cống kiểm soát)', '터널식(tràn hầm)' 등 형식을 구분하고, 베트남에서는 'cống tràn'과 'đập tràn'을 혼용하나 cống tràn이 더 일반적. 한국은 극한홍수(PMF) 대비를 강조하나 베트남은 설계빈도(tần suất thiết kế) 기준이 상이하므로 주의.",
        "meaningVi": "Công trình thủy công dùng để xả an toàn lượng nước vượt quá lưu lượng lũ thiết kế từ đập xuống hạ lưu. Là thiết bị then chốt cho an toàn đập.",
        "context": "댐 설계, 홍수조절, 수공구조물",
        "culturalNote": "한국은 여수로 용량 산정 시 기후변화를 반영한 확률강우량을 적용하며, 베트남은 과거 관측 데이터 기반 설계가 많음. 한국은 '여수로'라는 한자어를 사용하나 베트남은 'cống tràn(방류문)' 또는 'đập tràn(월류댐)'으로 구분. 베트남 메콩강 유역에서는 여수로 설계 시 하류 국가 영향까지 고려해야 함.",
        "commonMistakes": [
            {
                "mistake": "cửa xả",
                "correction": "cống tràn (여수로) vs cửa xả đáy (저수문/바닥 배출구)",
                "explanation": "여수로는 홍수 월류용, 저수문은 저층수 배출용으로 용도가 다름."
            },
            {
                "mistake": "설계홍수량을 'lưu lượng lũ'로만 표현",
                "correction": "lưu lượng lũ thiết kế (설계홍수량) vs lưu lượng lũ kiểm tra (점검홍수량)",
                "explanation": "설계와 점검 기준이 다르므로 명확히 구분 필요."
            },
            {
                "mistake": "자유월류식을 'tự do'로만 표현",
                "correction": "cống tràn tự do (자유월류식) vs cống tràn có cống kiểm soát (제어식)",
                "explanation": "수문 유무에 따라 운영 방식이 달라지므로 정확한 용어 사용 필수."
            }
        ],
        "examples": [
            {
                "ko": "여수로 설계홍수량은 200년 빈도를 적용했습니다.",
                "vi": "Lưu lượng lũ thiết kế của cống tràn áp dụng tần suất 200 năm.",
                "situation": "formal"
            },
            {
                "ko": "수문 개도 조절해서 방류량 줄여야 돼요.",
                "vi": "Cần điều chỉnh độ mở cống để giảm lưu lượng xả.",
                "situation": "onsite"
            },
            {
                "ko": "월류부 콘크리트 침식 확인되어 긴급 보수가 필요합니다.",
                "vi": "Phát hiện xói mòn bê tông vùng tràn, cần sửa chữa khẩn cấp.",
                "situation": "formal"
            }
        ],
        "relatedTerms": ["콘크리트댐", "수문", "설계홍수량", "홍수조절"]
    },
    {
        "slug": "thap-lay-nuoc",
        "korean": "취수탑",
        "vietnamese": "Tháp lấy nước",
        "hanja": "取水塔",
        "hanjaReading": "취할 취(取) + 물 수(水) + 탑 탑(塔)",
        "pronunciation": "táp lấy nước",
        "meaningKo": "저수지나 댐에서 필요한 수심의 물을 취수하기 위한 탑 형태의 구조물. 수질 상태에 따라 취수 높이를 조절할 수 있으며, 주로 용수공급(cấp nước) 및 발전용수 확보에 사용됨. 통역 시 '선택취수(lấy nước chọn lọc)' 기능 여부를 확인하고, 베트남에서는 'tháp lấy nước' 또는 'trạm bơm(펌프장)'과 혼동하지 않도록 주의. 한국은 수질관리 목적의 다단 취수를 강조하나 베트남은 단순 취수 기능이 많음.",
        "meaningVi": "Công trình dạng tháp dùng để lấy nước ở độ sâu cần thiết từ hồ chứa hoặc đập. Có thể điều chỉnh độ cao lấy nước theo chất lượng nước, chủ yếu dùng cho cấp nước sinh hoạt và phát điện.",
        "context": "상수도 시설, 수력발전, 댐 부대시설",
        "culturalNote": "한국은 취수탑을 상수원 수질보호 차원에서 다층 취수 시스템으로 설계하는 경우가 많으며, 베트남은 단순 취수 기능 위주. 한국은 '취수탑'이라는 용어를 사용하나 베트남에서는 'tháp lấy nước' 또는 'cửa lấy nước(취수구)'로 표현. 베트남 북부는 홍강 유역 취수탑이 많으며, 남부는 메콩강 델타 지역 펌프장(trạm bơm)이 주를 이룸.",
        "commonMistakes": [
            {
                "mistake": "trạm bơm",
                "correction": "tháp lấy nước (취수탑) vs trạm bơm (펌프장/양수장)",
                "explanation": "취수탑은 중력식 취수, 펌프장은 양수 기능이 있으므로 구분 필요."
            },
            {
                "mistake": "취수구(cửa lấy nước)와 혼용",
                "correction": "tháp lấy nước (탑 형태 구조물) vs cửa lấy nước (취수구/개구부)",
                "explanation": "취수탑은 구조물 전체, 취수구는 물 유입구를 의미."
            },
            {
                "mistake": "선택취수를 'lấy nước tùy chọn'으로 표현",
                "correction": "lấy nước chọn lọc (theo độ sâu) - 수심별 선택취수",
                "explanation": "수질 상태에 따라 취수 높이를 조절하는 기능을 명확히 전달해야 함."
            }
        ],
        "examples": [
            {
                "ko": "이 취수탑은 3단 선택취수 방식으로 설계되었습니다.",
                "vi": "Tháp lấy nước này được thiết kế với hệ thống lấy nước chọn lọc 3 tầng.",
                "situation": "formal"
            },
            {
                "ko": "수질 검사 결과 상층 취수로 전환하세요.",
                "vi": "Theo kết quả kiểm tra chất lượng nước, chuyển sang lấy nước tầng trên.",
                "situation": "onsite"
            },
            {
                "ko": "취수탑 유입구에 스크린 설치가 필요합니다.",
                "vi": "Cần lắp đặt lưới chắn tại cửa vào tháp lấy nước.",
                "situation": "formal"
            }
        ],
        "relatedTerms": ["저수지", "상수도", "수질관리", "펌프장"]
    },
    {
        "slug": "ho-chua",
        "korean": "저수지",
        "vietnamese": "Hồ chứa",
        "hanja": "貯水池",
        "hanjaReading": "저축할 저(貯) + 물 수(水) + 못 지(池)",
        "pronunciation": "hồ chứa",
        "meaningKo": "물을 가두어 저장하는 인공 또는 자연 수역. 댐에 의해 형성되는 경우가 많으며, 농업용수, 생활용수, 발전용수 등 다목적으로 활용됨. 통역 시 '유효저수량(dung tích hữu ích)', '사수위(mực nước chết)', '만수위(mực nước dâng bình thường)' 등 수위 용어를 정확히 전달해야 하며, 베트남에서는 'hồ chứa'와 'đập(댐)'을 혼용하므로 문맥 파악 필요. 한국은 저수율(tỷ lệ chứa nước) 관리를 중시하나 베트남은 우기/건기 편차가 커서 계절별 저수량 변동이 큼.",
        "meaningVi": "Vùng nước nhân tạo hoặc tự nhiên dùng để chứa nước. Thường được hình thành bởi đập, sử dụng đa mục đích như nông nghiệp, sinh hoạt, phát điện.",
        "context": "수자원 관리, 댐 운영, 관개시설",
        "culturalNote": "한국은 농업용 저수지를 '저수지'로, 대형 다목적댐의 저수공간을 '댐 호소'로 구분하나 베트남은 'hồ chứa'로 통칭. 한국농어촌공사가 전국 17,000여 개 저수지를 관리하며, 베트남은 지방정부 주도 관리로 시설 노후화가 심각. 한국은 가뭄 대비 저수율을 실시간 모니터링하나 베트남은 우기 홍수 조절에 더 집중.",
        "commonMistakes": [
            {
                "mistake": "hồ (호수)와 혼용",
                "correction": "hồ chứa (저수지/인공) vs hồ tự nhiên (자연호수)",
                "explanation": "저수지는 인공 수역이며 댐과 연계되므로 hồ chứa가 정확함."
            },
            {
                "mistake": "유효저수량을 'dung tích nước'로만 표현",
                "correction": "dung tích hữu ích (유효저수량) vs dung tích toàn bộ (총저수량)",
                "explanation": "유효저수량은 실제 이용 가능한 물의 양으로 사수위 이상을 의미함."
            },
            {
                "mistake": "만수위를 'mực nước cao nhất'로 표현",
                "correction": "mực nước dâng bình thường (만수위) vs mực nước lũ thiết kế (계획홍수위)",
                "explanation": "만수위는 정상 운영 시 최고 수위이며, 홍수위와는 다름."
            }
        ],
        "examples": [
            {
                "ko": "이 저수지의 유효저수량은 1,000만 톤입니다.",
                "vi": "Dung tích hữu ích của hồ chứa này là 10 triệu m³.",
                "situation": "formal"
            },
            {
                "ko": "저수율이 30% 이하로 떨어져서 급수 제한이 예상됩니다.",
                "vi": "Tỷ lệ chứa nước giảm xuống dưới 30%, dự kiến phải hạn chế cấp nước.",
                "situation": "formal"
            },
            {
                "ko": "만수위 넘으면 여수로로 자동 방류됩니다.",
                "vi": "Khi vượt mực nước dâng bình thường, nước sẽ tự động xả qua cống tràn.",
                "situation": "onsite"
            }
        ],
        "relatedTerms": ["댐", "여수로", "취수탑", "수위"]
    },
    {
        "slug": "ho-ngan",
        "korean": "호안공",
        "vietnamese": "Hộ ngạn",
        "hanja": "護岸工",
        "hanjaReading": "지킬 호(護) + 언덕 안(岸) + 장인 공(工)",
        "pronunciation": "hộ ngạn",
        "meaningKo": "하천이나 저수지 제방의 비탈면을 침식과 파랑으로부터 보호하기 위한 구조물. 콘크리트블록, 사석(đá xây), 식생매트 등 다양한 공법이 있으며, 통역 시 '사석호안(hộ ngạn bằng đá)', '콘크리트블록호안(hộ ngạn khối bê tông)', '생태호안(hộ ngạn sinh thái)' 등을 구분해야 함. 한국은 친환경 생태호안을 강조하나 베트남은 내구성 위주의 콘크리트/사석 호안이 많음. 하천정비사업에서 필수 공종.",
        "meaningVi": "Công trình bảo vệ mái dốc đê, bờ sông hoặc hồ chứa khỏi xói mòn và sóng. Có nhiều công pháp như đá xây, khối bê tông, thảm thực vật.",
        "context": "하천정비, 제방보강, 저수지 관리",
        "culturalNote": "한국은 4대강 사업 이후 생태호안(hộ ngạn sinh thái) 조성을 강조하며 식생 복원을 병행하나, 베트남은 우기 침식 방지를 위한 견고한 사석/콘크리트 호안이 주류. 한국은 '호안공'이라는 한자어를 사용하나 베트남에서는 'kè (제방)', 'hộ ngạn (호안)', 'gia cố bờ (사면보강)'을 혼용. 베트남 메콩강 유역은 연약지반이 많아 호안공 침하 문제가 빈번.",
        "commonMistakes": [
            {
                "mistake": "kè (제방)와 혼용",
                "correction": "hộ ngạn (호안공/사면 보호) vs kè (제방 전체 구조물)",
                "explanation": "호안공은 제방의 비탈면 보호 구조물이며, 제방은 전체 구조를 의미."
            },
            {
                "mistake": "사석호안을 'đá'로만 표현",
                "correction": "hộ ngạn bằng đá xây (사석호안) - 'đá xây'는 쌓은 돌을 의미",
                "explanation": "단순히 '돌'이 아니라 '쌓은 돌' 또는 '사석'으로 명확히 전달."
            },
            {
                "mistake": "생태호안을 'hộ ngạn tự nhiên'으로 표현",
                "correction": "hộ ngạn sinh thái (생태호안) - 식생과 공학적 기법 결합",
                "explanation": "자연호안과 생태호안은 다르며, 생태호안은 의도적으로 식생을 조성함."
            }
        ],
        "examples": [
            {
                "ko": "이 구간은 사석호안으로 보강할 계획입니다.",
                "vi": "Đoạn này dự kiến gia cố bằng hộ ngạn đá xây.",
                "situation": "formal"
            },
            {
                "ko": "호안 블록 유실 확인되어 긴급 복구 필요합니다.",
                "vi": "Phát hiện mất khối bê tông hộ ngạn, cần khôi phục khẩn cấp.",
                "situation": "onsite"
            },
            {
                "ko": "생태호안 조성으로 수생식물 서식지를 만들겠습니다.",
                "vi": "Sẽ tạo sinh cảnh thực vật thủy sinh bằng hộ ngạn sinh thái.",
                "situation": "formal"
            }
        ],
        "relatedTerms": ["제방", "하천정비", "사면보강", "침식방지"]
    },
    {
        "slug": "de-bao",
        "korean": "제방",
        "vietnamese": "Đê bao",
        "hanja": "堤防",
        "hanjaReading": "둑 제(堤) + 막을 방(防)",
        "pronunciation": "đê bao",
        "meaningKo": "하천의 범람을 막기 위해 강변을 따라 쌓은 둑. 홍수 방어의 1차 구조물로, 제체(thân đê), 제내지(vùng trong đê), 제외지(vùng ngoài đê) 등으로 구분됨. 통역 시 '계획홍수위(mực nước lũ thiết kế)', '여유고(độ dư mực nước)', '제방고(chiều cao đê)' 등 수위 관련 용어를 정확히 전달해야 하며, 베트남에서는 'đê (북부)' 또는 'bờ bao (남부)'로 지역별 용어 차이가 있음. 한국은 제방 안전점검을 주기적으로 실시하나 베트남은 우기 전 긴급 보강이 주.",
        "meaningVi": "Đê đắp dọc bờ sông để ngăn lũ. Là công trình phòng chống lũ lụt bậc nhất, phân chia thành thân đê, vùng trong đê, vùng ngoài đê.",
        "context": "하천관리, 홍수방어, 재해예방",
        "culturalNote": "한국은 하천법에 따라 국가하천과 지방하천의 제방 관리 주체가 구분되며, 정기 안전점검이 의무화됨. 베트남은 북부 홍강 델타와 남부 메콩강 델타에서 제방이 매우 중요하며, 우기 범람이 빈번해 제방 높이를 지속적으로 증축. 한국은 '제방'이라는 용어를 사용하나 베트남은 북부 'đê', 남부 'bờ bao'로 지역차가 있음.",
        "commonMistakes": [
            {
                "mistake": "đập (댐)과 혼용",
                "correction": "đê (제방/하천 둑) vs đập (댐/저수 구조물)",
                "explanation": "제방은 하천 범람 방지용, 댐은 저수 및 발전용으로 목적이 다름."
            },
            {
                "mistake": "여유고를 'chiều cao dự phòng'로 표현",
                "correction": "độ dư mực nước (여유고) - 계획홍수위와 제방 상단 사이 높이",
                "explanation": "여유고는 파랑 등을 고려한 안전 여유분으로 명확한 기술 용어 사용 필요."
            },
            {
                "mistake": "제내지/제외지를 'trong/ngoài'로만 표현",
                "correction": "vùng trong đê (제내지/보호구역) vs vùng ngoài đê (제외지/하천구역)",
                "explanation": "제내/제외는 홍수 방어 기준이므로 vùng을 함께 사용."
            }
        ],
        "examples": [
            {
                "ko": "이 제방의 계획홍수위는 해발 5m이며 여유고는 1.5m입니다.",
                "vi": "Mực nước lũ thiết kế của đê này là 5m so với mực nước biển, độ dư mực nước là 1,5m.",
                "situation": "formal"
            },
            {
                "ko": "제체에 누수 확인되어 토낭 쌓아야 돼요.",
                "vi": "Phát hiện thấm nước ở thân đê, cần chất bao cát.",
                "situation": "onsite"
            },
            {
                "ko": "제방 월류 위험으로 주민 대피령이 발령되었습니다.",
                "vi": "Do nguy cơ nước tràn qua đê, đã ban hành lệnh sơ tán dân.",
                "situation": "formal"
            }
        ],
        "relatedTerms": ["호안공", "하천정비", "홍수방어", "여수로"]
    },
    {
        "slug": "cua-van",
        "korean": "수문",
        "vietnamese": "Cửa van",
        "hanja": "水門",
        "hanjaReading": "물 수(水) + 문 문(門)",
        "pronunciation": "cửa van",
        "meaningKo": "댐, 보, 제방 등에 설치되어 수위 조절 및 유량 제어를 위한 개폐식 구조물. 형식에 따라 슬루스게이트(cửa van trượt), 롤러게이트(cửa van cuộn), 레이디얼게이트(cửa van hướng tâm) 등으로 구분됨. 통역 시 수문의 형식과 작동 방식(thủy lực/hydraulic, điện cơ/전동)을 명확히 전달해야 하며, 베트남에서는 'cửa van'과 'cống(수문+통로)'을 혼용하므로 주의. 한국은 자동화된 원격 조작 시스템이 많으나 베트남은 수동 조작 수문이 많음.",
        "meaningVi": "Công trình có thể đóng mở được, lắp đặt tại đập, đập tràn, đê để điều tiết mực nước và kiểm soát lưu lượng. Phân loại theo kiểu cửa van trượt, cuộn, hướng tâm...",
        "context": "댐 운영, 수위 조절, 홍수 조절",
        "culturalNote": "한국은 4대강 사업 이후 자동 수문 조작 시스템이 보편화되었으며 실시간 유량 모니터링을 실시. 베트남은 전력 인프라가 취약한 지역이 많아 수동 또는 반자동 수문이 많으며, 우기 급격한 수위 상승 시 수문 조작 지연이 문제. 한국은 '수문'이라는 용어를 사용하나 베트남은 'cửa van(수문)', 'cống(배수문)' 등 용도에 따라 세분화.",
        "commonMistakes": [
            {
                "mistake": "cống (배수로)와 혼용",
                "correction": "cửa van (수문/개폐문) vs cống (배수로/터널 포함 구조)",
                "explanation": "수문은 개폐 가능한 문, cống은 배수 통로 전체를 의미."
            },
            {
                "mistake": "게이트 형식 구분 없이 번역",
                "correction": "슬루스(van trượt), 롤러(van cuộn), 레이디얼(van hướng tâm) 등 세분화",
                "explanation": "수문 형식에 따라 작동 원리와 유지관리가 다르므로 정확한 용어 필요."
            },
            {
                "mistake": "개도를 'độ mở'로만 표현",
                "correction": "độ mở cửa van (개도) - 수문 열림 정도, % 또는 m 단위",
                "explanation": "개도는 유량 조절의 핵심 변수이므로 명확히 전달."
            }
        ],
        "examples": [
            {
                "ko": "수문 개도 50%로 조정하여 하류 유량을 조절하세요.",
                "vi": "Điều chỉnh độ mở cửa van về 50% để kiểm soát lưu lượng hạ lưu.",
                "situation": "formal"
            },
            {
                "ko": "수문 권양기 고장나서 수동으로 올려야 돼요.",
                "vi": "Máy kéo cửa van bị hỏng, phải nâng thủ công.",
                "situation": "onsite"
            },
            {
                "ko": "홍수 시 수문을 전면 개방하여 방류합니다.",
                "vi": "Khi lũ, mở toàn bộ cửa van để xả nước.",
                "situation": "formal"
            }
        ],
        "relatedTerms": ["여수로", "댐", "수위 조절", "홍수 조절"]
    },
    {
        "slug": "ca-dao",
        "korean": "어도",
        "vietnamese": "Cá đạo",
        "hanja": "魚道",
        "hanjaReading": "물고기 어(魚) + 길 도(道)",
        "pronunciation": "cá ḍạo",
        "meaningKo": "댐이나 보에 의해 차단된 하천에서 물고기가 상하류로 이동할 수 있도록 만든 통로. 생태계 보전의 핵심 시설로, 계단식(dạng bậc thang), 수로식(dạng kênh), 엘리베이터식(thang máy cá) 등 다양한 형식이 있음. 통역 시 어도의 형식과 목적어종(어종)을 명확히 전달해야 하며, 베트남에서는 'cá đạo' 또는 'đường di cư cá(어류 회유로)'로 표현. 한국은 4대강 사업 이후 어도 설치가 의무화되었으나 베트남은 댐 건설 시 어도 고려가 부족한 편.",
        "meaningVi": "Đường đi dành cho cá để di chuyển lên xuống khi sông bị chặn bởi đập hoặc đập tràn. Là thiết bị then chốt cho bảo tồn sinh thái, có nhiều dạng như bậc thang, kênh, thang máy cá.",
        "context": "생태복원, 댐 부대시설, 하천 환경",
        "culturalNote": "한국은 하천법 및 환경영향평가법에 따라 일정 규모 이상의 보와 댐에 어도 설치가 의무화되었으며, 4대강 사업 이후 어도 효율성 논란이 많음. 베트남은 메콩강 유역 댐 건설 증가로 어류 회유 경로 차단 문제가 심각하나 어도 설치 사례는 적음. 한국은 '어도'라는 한자어를 사용하나 베트남은 'cá đạo' 또는 'cầu thang cá(물고기 계단)'로 표현.",
        "commonMistakes": [
            {
                "mistake": "đường cá",
                "correction": "cá đạo (어도/어류 통로) - '길 도(道)'의 의미 포함",
                "explanation": "어도는 단순한 길이 아니라 어류 이동을 위한 설계된 구조물."
            },
            {
                "mistake": "계단식 어도를 'cầu thang'으로만 표현",
                "correction": "cá đạo dạng bậc thang (계단식 어도) - 어도임을 명확히",
                "explanation": "계단(cầu thang)만 표현하면 어도인지 불명확하므로 cá đạo 함께 사용."
            },
            {
                "mistake": "어도 효율을 'hiệu quả'로만 표현",
                "correction": "hiệu quả di cư (회유 효율) - 어류가 실제로 통과하는 비율",
                "explanation": "어도의 성능은 어류가 실제로 이동하는지 여부로 평가해야 함."
            }
        ],
        "examples": [
            {
                "ko": "이 보에는 계단식 어도가 설치되어 있어 연어 회유가 가능합니다.",
                "vi": "Đập tràn này có lắp đặt cá đạo dạng bậc thang, giúp cá hồi di cư.",
                "situation": "formal"
            },
            {
                "ko": "어도 유속 측정 결과 설계 기준을 초과했습니다.",
                "vi": "Kết quả đo vận tốc dòng chảy trong cá đạo vượt tiêu chuẩn thiết kế.",
                "situation": "formal"
            },
            {
                "ko": "어도 입구에 쓰레기 쌓여서 청소해야 돼요.",
                "vi": "Rác tích tụ ở cửa vào cá đạo, cần dọn dẹp.",
                "situation": "onsite"
            }
        ],
        "relatedTerms": ["댐", "보", "생태복원", "하천 환경"]
    },
    {
        "slug": "cong-duy-tri-ha-상",
        "korean": "하상유지공",
        "vietnamese": "Công duy trì hạ sàng",
        "hanja": "河床維持工",
        "hanjaReading": "물 하(河) + 평상 상(床) + 유지할 유(維) + 지킬 지(持) + 장인 공(工)",
        "pronunciation": "công zuy trì hạ sàng",
        "meaningKo": "하천 바닥(하상)의 과도한 저하를 방지하여 하천 구조물의 안전성을 확보하기 위한 공법. 보(đập tràn nhỏ), 낙차공(công giảm cao độ), 바닥보호공(công bảo vệ đáy) 등이 포함되며, 통역 시 하상세굴(xói sâu lòng sông)과의 관계를 명확히 해야 함. 한국은 하천정비사업에서 교량·보 하류 세굴 방지 목적으로 많이 설치하나 베트남은 준설(nạo vét) 후 하상 안정화에 주로 사용. 하상변동(biến động lòng sông) 예측이 설계의 핵심.",
        "meaningVi": "Công pháp ngăn chặn đáy sông (hạ sàng) bị hạ thấp quá mức, đảm bảo an toàn công trình sông. Bao gồm đập tràn nhỏ, công giảm cao độ, công bảo vệ đáy.",
        "context": "하천정비, 세굴방지, 교량 기초보호",
        "culturalNote": "한국은 4대강 사업 이후 보 설치로 인한 상류 퇴적, 하류 세굴 문제가 발생하여 하상유지공 중요성이 증가. 베트남은 메콩강 유역 모래 채취(khai thác cát)로 인한 하상 저하가 심각하여 하상유지공 필요성이 높으나 예산 부족으로 설치율 낮음. 한국은 '하상유지공'이라는 전문용어를 사용하나 베트남에서는 'công chống xói đáy(하상 침식 방지공)'로 더 많이 표현.",
        "commonMistakes": [
            {
                "mistake": "낙차공을 'thác nước'로 표현",
                "correction": "công giảm cao độ (낙차공) - 에너지 감세를 위한 구조물",
                "explanation": "낙차공은 인공 폭포가 아니라 하상 안정 및 에너지 감세 목적의 공법."
            },
            {
                "mistake": "하상세굴을 'xói mòn đáy'로만 표현",
                "correction": "xói sâu lòng sông (하상세굴) - 수직 방향 침식 강조",
                "explanation": "하상세굴은 하상이 깊어지는 현상으로 xói sâu(깊이 파임)가 정확."
            },
            {
                "mistake": "보와 하상유지공을 혼용",
                "correction": "đập tràn nhỏ (보/소규모 댐) vs công duy trì hạ sàng (하상유지공/전반 공법)",
                "explanation": "보는 하상유지공의 한 형식이며, 하상유지공은 더 넓은 개념."
            }
        ],
        "examples": [
            {
                "ko": "교량 하류 하상세굴 방지를 위해 하상유지공을 설치합니다.",
                "vi": "Lắp đặt công duy trì hạ sàng để ngăn xói sâu lòng sông ở hạ lưu cầu.",
                "situation": "formal"
            },
            {
                "ko": "낙차공 콘크리트 파손 확인되어 보수 필요합니다.",
                "vi": "Phát hiện hư hỏng bê tông công giảm cao độ, cần sửa chữa.",
                "situation": "formal"
            },
            {
                "ko": "하상 내려가서 보 기초 노출됐어요. 긴급 보강해야 돼요.",
                "vi": "Đáy sông hạ thấp làm lộ móng đập tràn, cần gia cố khẩn cấp.",
                "situation": "onsite"
            }
        ],
        "relatedTerms": ["보", "세굴", "하천정비", "낙차공"]
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

def add_terms():
    """기존 construction.json에 10개 용어 추가"""
    # 기존 파일 읽기
    with open(file_path, "r", encoding="utf-8") as f:
        existing_data = json.load(f)

    print(f"[INFO] 기존 용어 수: {len(existing_data)}개")

    # 신규 용어 추가
    existing_data.extend(data)

    print(f"[INFO] 추가 후 용어 수: {len(existing_data)}개")

    # 파일 저장 (들여쓰기 2칸, 유니코드 그대로, 후행 개행 포함)
    with open(file_path, "w", encoding="utf-8") as f:
        json.dump(existing_data, f, ensure_ascii=False, indent=2)
        f.write("\n")

    print(f"[SUCCESS] {file_path} 저장 완료")
    print("\n[추가된 용어]")
    for i, term in enumerate(data, 1):
        print(f"{i}. {term['korean']} ({term['vietnamese']})")

if __name__ == "__main__":
    add_terms()
