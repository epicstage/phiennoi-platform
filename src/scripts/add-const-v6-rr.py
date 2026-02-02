#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
건설(Construction) 용어 추가 스크립트 v6
테마: 프리캐스트/PC공법
- PC기둥, PC보, 더블티, 할로우코어, 조인트, 그라우트충전, PC패널, 양중계획, PC야적장, 접합상세
"""

import json
import os

# 추가할 용어 데이터 (10개)
new_terms = [
    {
        "slug": "cot-pc",
        "korean": "PC기둥",
        "vietnamese": "Cột PC",
        "hanja": "基柱",
        "hanjaReading": "基(터 기) + 柱(기둥 주)",
        "pronunciation": "피씨 기둥",
        "meaningKo": "공장에서 미리 제작한 철근콘크리트 기둥. 현장 타설 대비 품질 균일, 공기 단축 가능. 통역 시 '기성 기둥', '조립식 기둥' 등으로 혼동 주의. 접합부 시공 품질이 구조 안전에 직결되므로 '접합', '조인트', '그라우트' 용어와 함께 사용 빈도 높음.",
        "meaningVi": "Cột bê tông cốt thép được đúc sẵn tại nhà máy. So với đổ bê tông tại chỗ, chất lượng đồng đều hơn và rút ngắn được thời gian thi công. Chất lượng thi công mối nối ảnh hưởng trực tiếp đến an toàn kết cấu.",
        "context": "구조 설계, 골조 공사, PC공법 현장",
        "culturalNote": "한국은 아파트/공장 골조에 PC부재 적극 활용. 베트남은 현장 타설 선호 문화가 강하나 최근 대형 프로젝트에서 PC 도입 증가. '공장 제작'이라는 개념이 품질 신뢰도로 연결되므로 'đúc sẵn tại nhà máy'를 명확히 강조해야 함.",
        "commonMistakes": [
            {
                "mistake": "Cột lắp ghép (조립식 기둥)",
                "correction": "Cột PC (PC기둥)",
                "explanation": "Lắp ghép은 금속/목재 조립을 연상시킴. PC는 공법 고유명사로 사용"
            },
            {
                "mistake": "Cột đúc trước",
                "correction": "Cột PC",
                "explanation": "Đúc trước는 일반 용어. 'PC'는 업계 표준 용어"
            },
            {
                "mistake": "'Mối nối'를 'điểm nối'로 번역",
                "correction": "'Mối nối'",
                "explanation": "Điểm은 점(point), mối는 이음부(joint) 의미"
            }
        ],
        "examples": [
            {
                "ko": "PC기둥 양중 시 수직도 ±5mm 이내 준수",
                "vi": "Khi cẩu lắp cột PC phải đảm bảo độ thẳng đứng trong phạm vi ±5mm",
                "situation": "onsite"
            },
            {
                "ko": "접합부 그라우트 충전 전 기둥 청소 완료 확인",
                "vi": "Xác nhận đã làm sạch cột trước khi đổ vữa grouting mối nối",
                "situation": "onsite"
            },
            {
                "ko": "PC기둥 제작 품질은 KCS 14 20 10 기준 적용",
                "vi": "Chất lượng chế tạo cột PC áp dụng theo tiêu chuẩn KCS 14 20 10",
                "situation": "formal"
            }
        ],
        "relatedTerms": ["PC보", "접합부", "그라우트", "양중계획"]
    },
    {
        "slug": "dam-pc",
        "korean": "PC보",
        "vietnamese": "Dầm PC",
        "hanja": "보",
        "hanjaReading": "보 보(梁)",
        "pronunciation": "피씨 보",
        "meaningKo": "공장 제작 철근콘크리트 보(beam). 기둥과 함께 골조를 구성. 통역 시 'dầm'(보) 앞에 반드시 'PC' 명시. 현장 타설 보(dầm đổ tại chỗ)와 혼동 방지 필요. 보-기둥 접합부 시공이 핵심이므로 '접합철물', '앵커볼트' 용어와 함께 자주 언급.",
        "meaningVi": "Dầm bê tông cốt thép được đúc sẵn tại nhà máy. Cùng với cột tạo thành kết cấu khung. Thi công mối nối giữa dầm và cột là điểm quan trọng, thường đề cập cùng với 'vật liệu nối', 'bulông neo'.",
        "context": "구조 설계, 골조 공사, PC공법 현장",
        "culturalNote": "한국은 보-기둥 프레임 공법 표준화. 베트남은 슬래브 일체식 선호 경향. PC보 도입 시 '접합부 품질'이 한국인 발주처의 핵심 관심사이므로 'mối nối'(접합부) 강조 필수.",
        "commonMistakes": [
            {
                "mistake": "Dầm lắp ghép",
                "correction": "Dầm PC",
                "explanation": "Lắp ghép은 금속 구조물 연상. PC는 콘크리트 공법 전문 용어"
            },
            {
                "mistake": "'Beam'을 'xà' 또는 'kèo'로 번역",
                "correction": "'Dầm'",
                "explanation": "Xà는 나무 보, kèo는 지붕 서까래. 콘크리트 보는 dầm"
            },
            {
                "mistake": "'보강철근'을 'thép tăng cường'로 번역",
                "correction": "'Cốt thép bổ sung'",
                "explanation": "Tăng cường는 일반 강화. 보강은 bổ sung(추가)"
            }
        ],
        "examples": [
            {
                "ko": "PC보 설치 후 기둥과의 접합부 용접 및 그라우트 시공",
                "vi": "Sau khi lắp dầm PC, thực hiện hàn mối nối với cột và thi công grouting",
                "situation": "onsite"
            },
            {
                "ko": "보의 처짐은 L/360 이내로 관리",
                "vi": "Độ võng của dầm quản lý trong phạm vi L/360",
                "situation": "formal"
            },
            {
                "ko": "PC보 야적 시 3단 이하, 받침목 위치 확인",
                "vi": "Khi xếp dầm PC tối đa 3 tầng, xác nhận vị trí gối đỡ",
                "situation": "onsite"
            }
        ],
        "relatedTerms": ["PC기둥", "접합부", "처짐", "양중"]
    },
    {
        "slug": "san-double-tee",
        "korean": "더블티",
        "vietnamese": "Sàn Double Tee",
        "hanja": None,
        "hanjaReading": None,
        "pronunciation": "더블 티",
        "meaningKo": "T자 단면 2개가 결합된 형태의 PC 슬래브. 장스팬(15~20m) 가능, 주차장/공장/체육관 등에 활용. 통역 시 'sàn Double Tee'로 음차 사용 일반적. 'hai chữ T'(T자 2개)로 설명 가능하나 고유명사로 인식시키는 것이 현장 소통에 유리.",
        "meaningVi": "Tấm sàn PC có mặt cắt hình hai chữ T liền nhau. Có thể thi công nhịp dài (15~20m), thường dùng cho bãi đỗ xe, nhà xưởng, nhà thi đấu. Thuật ngữ 'Double Tee' được dùng trực tiếp trong tiếng Việt.",
        "context": "구조 설계, 슬래브 공사, 대공간 건축",
        "culturalNote": "한국은 주차장/물류센터에서 더블티 슬래브 활발히 사용. 베트남은 플랫 슬래브 선호 문화가 강하나 외국계 프로젝트에서 도입 증가. 'Double Tee'를 베트남어로 완전히 의역하기보다 음차 + 설명 병기가 효과적.",
        "commonMistakes": [
            {
                "mistake": "Sàn chữ T kép",
                "correction": "Sàn Double Tee",
                "explanation": "Chữ T kép는 직역. Double Tee는 고유명사로 음차 사용"
            },
            {
                "mistake": "'장스팬'을 'khoảng cách dài'로 번역",
                "correction": "'Nhịp dài'",
                "explanation": "Khoảng cách는 일반 거리. 구조 용어는 nhịp(span)"
            },
            {
                "mistake": "'받침부'를 'chỗ đỡ'로 번역",
                "correction": "'Gối đỡ' 또는 'chỗ tựa'",
                "explanation": "Chỗ đỡ는 구어체. 전문 용어는 gối đỡ"
            }
        ],
        "examples": [
            {
                "ko": "더블티 슬래브 18m 스팬, 지지부는 네오프렌 받침 설치",
                "vi": "Sàn Double Tee nhịp 18m, tại vị trí tựa lắp đặt gối cao su neoprene",
                "situation": "formal"
            },
            {
                "ko": "더블티 양중 시 2점 걸이 전용 샤클 사용",
                "vi": "Khi cẩu Double Tee sử dụng shackle chuyên dụng móc 2 điểm",
                "situation": "onsite"
            },
            {
                "ko": "조인트부 콘크리트 후타설로 일체화",
                "vi": "Đổ bê tông phần mối nối sau để tạo tính toàn khối",
                "situation": "onsite"
            }
        ],
        "relatedTerms": ["PC슬래브", "장스팬", "네오프렌받침", "양중"]
    },
    {
        "slug": "san-hollow-core",
        "korean": "할로우코어",
        "vietnamese": "Sàn Hollow Core",
        "hanja": None,
        "hanjaReading": None,
        "pronunciation": "할로우 코어",
        "meaningKo": "속이 빈 원형 공동이 있는 PC 슬래브. 자중 경감, 배선/배관 공간 확보. 통역 시 'Hollow Core' 음차 후 'lõi rỗng'(빈 속)으로 설명 병행. 아파트 바닥판, 오피스텔 등에 활용. '중공(中空)'이라는 한자어보다 'Hollow Core'가 현장 표준 용어.",
        "meaningVi": "Tấm sàn PC có các lỗ tròn rỗng bên trong. Giảm trọng lượng bản thân, tạo không gian cho dây điện/đường ống. Thuật ngữ 'Hollow Core' được dùng trực tiếp, giải thích thêm 'lõi rỗng'. Thường dùng trong sàn chung cư, officetel.",
        "context": "구조 설계, 슬래브 공사, 공동주택",
        "culturalNote": "한국은 아파트 바닥 소음 저감 목적으로 할로우코어+완충재 조합 사용. 베트남은 RC 슬래브가 주류이나 고층 주거에서 할로우코어 도입 증가. '층간소음'이라는 개념이 한국 고유 관심사이므로 'giảm ồn' 강조 필요.",
        "commonMistakes": [
            {
                "mistake": "Sàn rỗng (빈 슬래브)",
                "correction": "Sàn Hollow Core",
                "explanation": "Sàn rỗng은 일반 설명. Hollow Core는 공법 고유명사"
            },
            {
                "mistake": "'중공 슬래브'를 'sàn không gian giữa'로 번역",
                "correction": "'Sàn Hollow Core' 또는 'sàn lõi rỗng'",
                "explanation": "Không gian giữa는 의미 왜곡. 전문 용어 사용 필수"
            },
            {
                "mistake": "'층간소음'을 'tiếng ồn giữa tầng'로 번역",
                "correction": "'Tiếng ồn xuyên sàn'",
                "explanation": "Giữa tầng은 공간 개념. 소음은 xuyên(관통) 사용"
            }
        ],
        "examples": [
            {
                "ko": "할로우코어 슬래브 두께 200mm, 공동 직경 150mm",
                "vi": "Sàn Hollow Core dày 200mm, đường kính lỗ rỗng 150mm",
                "situation": "formal"
            },
            {
                "ko": "공동부 막힘 없이 배선 관통 가능 확인",
                "vi": "Xác nhận có thể xuyên dây điện qua lỗ rỗng không bị tắc",
                "situation": "onsite"
            },
            {
                "ko": "층간소음 저감 위해 완충재 20mm 추가",
                "vi": "Bổ sung lớp đệm 20mm để giảm tiếng ồn xuyên sàn",
                "situation": "onsite"
            }
        ],
        "relatedTerms": ["PC슬래브", "층간소음", "배선", "경량화"]
    },
    {
        "slug": "moi-noi-pc",
        "korean": "PC조인트",
        "vietnamese": "Mối nối PC",
        "hanja": "接合",
        "hanjaReading": "接(이을 접) + 合(합할 합)",
        "pronunciation": "피씨 조인트",
        "meaningKo": "PC부재 간 또는 PC부재와 현장타설 부재의 접합부. 구조 안전의 핵심 부위. 통역 시 'mối nối'(접합) 앞에 'PC' 명시 필수. 용접, 볼트, 그라우트 등 접합 방식 다양. '이음부', '접속부'로도 불리나 'PC조인트'가 현장 표준 용어.",
        "meaningVi": "Vị trí nối giữa các cấu kiện PC hoặc giữa PC và bê tông đổ tại chỗ. Là điểm quan trọng quyết định an toàn kết cấu. Phương pháp nối đa dạng: hàn, bu lông, grouting. Thuật ngữ 'mối nối PC' là chuẩn hiện trường.",
        "context": "구조 시공, PC공법, 품질 관리",
        "culturalNote": "한국은 PC조인트 품질 관리 기준 엄격(KCS 14 20 52). 베트남은 조인트 시공 경험 부족으로 외국 기술자 의존 많음. '접합부 품질'이 안전과 직결되므로 'chất lượng mối nối' 강조, 세부 시공법 반복 설명 필요.",
        "commonMistakes": [
            {
                "mistake": "Điểm nối (연결점)",
                "correction": "Mối nối (접합부)",
                "explanation": "Điểm은 점(point). Mối는 이음부(joint) 의미로 구조 용어"
            },
            {
                "mistake": "'그라우트'를 'vữa xi măng'로 번역",
                "correction": "'Vữa grouting'",
                "explanation": "Vữa xi măng은 일반 모르타르. Grouting은 전문 용어"
            },
            {
                "mistake": "'용접'을 'hàn điện'으로만 번역",
                "correction": "'Hàn' 또는 구체적으로 'hàn hồ quang'",
                "explanation": "Hàn điện은 구어체. 공식 문서는 hàn hoặc hàn hồ quang"
            }
        ],
        "examples": [
            {
                "ko": "PC조인트 시공 전 철근 청소 및 녹 제거 완료",
                "vi": "Trước khi thi công mối nối PC, hoàn thành làm sạch và tẩy rỉ cốt thép",
                "situation": "onsite"
            },
            {
                "ko": "조인트부 그라우트 강도 40MPa 이상 확인",
                "vi": "Xác nhận cường độ vữa grouting tại mối nối đạt trên 40MPa",
                "situation": "formal"
            },
            {
                "ko": "용접 후 초음파 검사로 결함 여부 점검",
                "vi": "Sau khi hàn, kiểm tra khuyết tật bằng siêu âm",
                "situation": "formal"
            }
        ],
        "relatedTerms": ["그라우트", "용접", "앵커볼트", "접합철물"]
    },
    {
        "slug": "do-vua-grouting",
        "korean": "그라우트충전",
        "vietnamese": "Đổ vữa grouting",
        "hanja": "充塡",
        "hanjaReading": "充(채울 충) + 塡(메울 전)",
        "pronunciation": "그라우트 충전",
        "meaningKo": "PC부재 접합부의 빈 공간에 유동성 높은 시멘트 모르타르(그라우트)를 채워 일체화하는 공정. 통역 시 'grouting'을 음차 사용, '충전'은 'đổ'(붓다) 또는 'chèn'(채우다)로 표현. 강도, 유동성, 충전 높이 관리가 핵심. 'grouting 시공'으로 통칭.",
        "meaningVi": "Công đoạn đổ đầy vữa xi măng có tính chảy cao (grouting) vào khoảng trống tại mối nối PC để tạo tính toàn khối. Quản lý cường độ, độ chảy, chiều cao đổ là yếu tố then chốt. Thường gọi chung là 'thi công grouting'.",
        "context": "PC공법, 조인트 시공, 품질 관리",
        "culturalNote": "한국은 그라우트 배합비, 유동성(플로우), 블리딩 기준 명확. 베트남은 'vữa grouting'이라는 전문 용어 인식 낮아 '유동성 모르타르'로 설명 병행 필요. 'tính chảy'(유동성) 강조하면 이해도 높아짐.",
        "commonMistakes": [
            {
                "mistake": "Đổ vữa thường (일반 모르타르 타설)",
                "correction": "Đổ vữa grouting (그라우트 충전)",
                "explanation": "Vữa thường은 일반 모르타르. Grouting은 고유동성 전문 재료"
            },
            {
                "mistake": "'충전'을 'sạc'로 번역",
                "correction": "'Đổ' 또는 'chèn đầy'",
                "explanation": "Sạc은 배터리 충전. 시공 용어는 đổ(붓다)"
            },
            {
                "mistake": "'블리딩'을 'chảy ra'로 번역",
                "correction": "'Tiết nước' 또는 'bleeding'",
                "explanation": "Chảy ra는 일반 흐름. Bleeding은 콘크리트 전문 용어"
            }
        ],
        "examples": [
            {
                "ko": "그라우트 플로우 200±20mm 범위 내 관리",
                "vi": "Quản lý độ chảy vữa grouting trong phạm vi 200±20mm",
                "situation": "formal"
            },
            {
                "ko": "접합부 청소 후 그라우트 충전, 24시간 양생",
                "vi": "Sau khi làm sạch mối nối, đổ vữa grouting và bảo dưỡng 24 giờ",
                "situation": "onsite"
            },
            {
                "ko": "충전 높이 부족 시 재시공 필수",
                "vi": "Nếu chiều cao đổ không đủ phải thi công lại",
                "situation": "onsite"
            }
        ],
        "relatedTerms": ["PC조인트", "유동성", "블리딩", "양생"]
    },
    {
        "slug": "tam-op-pc",
        "korean": "PC패널",
        "vietnamese": "Tấm ốp PC",
        "hanja": "板",
        "hanjaReading": "판 판(板)",
        "pronunciation": "피씨 패널",
        "meaningKo": "건물 외벽에 설치하는 공장 제작 콘크리트 패널. 마감+단열+구조 일체화 가능. 통역 시 'tấm ốp'(덧판)은 비구조, 'tấm PC'는 구조재 의미 구분 필요. 커튼월(curtain wall) 개념과 혼동 주의. PC패널은 콘크리트, 커튼월은 유리/알루미늄.",
        "meaningVi": "Tấm bê tông được đúc sẵn lắp đặt trên tường ngoài. Có thể tích hợp hoàn thiện + cách nhiệt + kết cấu. Cần phân biệt: 'tấm ốp' (không chịu lực), 'tấm PC' (chịu lực). Chú ý không nhầm với curtain wall (kính/nhôm).",
        "context": "외벽 공사, PC공법, 건축 마감",
        "culturalNote": "한국은 공동주택 외벽에 PC패널 널리 사용(단열+마감+시공성). 베트남은 벽돌+미장 문화 강해 PC패널 생소. '단열+방수+마감 일체화'라는 개념을 'tích hợp'(통합)으로 강조하면 이해 빠름.",
        "commonMistakes": [
            {
                "mistake": "Tường bê tông lắp ghép (조립식 벽)",
                "correction": "Tấm ốp PC (PC패널)",
                "explanation": "Tường은 벽체 전체. Tấm ốp은 외벽 마감재"
            },
            {
                "mistake": "'커튼월'과 'PC패널' 혼동",
                "correction": "Curtain wall(유리), PC패널(콘크리트) 구분",
                "explanation": "재료와 용도가 완전히 다름"
            },
            {
                "mistake": "'패스너'를 'vít'로 번역",
                "correction": "'Liên kết kim loại' 또는 'fastener'",
                "explanation": "Vít은 나사못. 구조 연결재는 liên kết kim loại"
            }
        ],
        "examples": [
            {
                "ko": "PC패널 설치 후 패스너로 구조체와 연결",
                "vi": "Sau khi lắp tấm ốp PC, liên kết với kết cấu bằng fastener",
                "situation": "onsite"
            },
            {
                "ko": "패널 간 조인트 실링재로 방수 처리",
                "vi": "Xử lý chống thấm mối nối giữa các tấm bằng vật liệu trám kín",
                "situation": "onsite"
            },
            {
                "ko": "외벽 PC패널 단열성능 0.15 W/m²K 이하",
                "vi": "Hiệu suất cách nhiệt tấm ốp PC tường ngoài dưới 0.15 W/m²K",
                "situation": "formal"
            }
        ],
        "relatedTerms": ["외벽", "단열", "패스너", "조인트"]
    },
    {
        "slug": "ke-hoach-cau-lap",
        "korean": "양중계획",
        "vietnamese": "Kế hoạch cẩu lắp",
        "hanja": "揚重計劃",
        "hanjaReading": "揚(들 양) + 重(무거울 중) + 計(셀 계) + 劃(그을 획)",
        "pronunciation": "양중 계획",
        "meaningKo": "중량물(PC부재 등)을 크레인으로 들어 올려 설치하는 전체 계획. 장비 선정, 동선, 안전, 공정 포함. 통역 시 '양중'은 'cẩu lắp'(크레인 설치), '중량물'은 'cấu kiện nặng'. '리프팅 플랜'(Lifting Plan)으로도 불리나 한국 현장은 '양중계획'이 표준.",
        "meaningVi": "Kế hoạch toàn bộ quá trình sử dụng cần cẩu để nâng và lắp đặt vật nặng (như cấu kiện PC). Bao gồm lựa chọn thiết bị, động tuyến, an toàn, tiến độ. Còn gọi là 'Lifting Plan' nhưng thuật ngữ Hàn Quốc chuẩn là '양중계획'.",
        "context": "안전 관리, PC공법, 공정 관리",
        "culturalNote": "한국은 양중계획 수립 의무화(산업안전보건법), 크레인 용량, 작업반경, 지반 지지력 등 상세 검토. 베트남은 계획서 작성 문화 약하나 외국계 현장은 'Lifting Plan' 필수. '안전'을 'an toàn'으로 반복 강조해야 주의 환기 효과.",
        "commonMistakes": [
            {
                "mistake": "Kế hoạch nâng (들어올리기 계획)",
                "correction": "Kế hoạch cẩu lắp (양중계획)",
                "explanation": "Nâng은 일반 들기. Cẩu lắp은 크레인 전문 용어"
            },
            {
                "mistake": "'작업반경'을 'vùng làm việc'로 번역",
                "correction": "'Bán kính làm việc'",
                "explanation": "Vùng는 면적. 작업반경은 radius(bán kính)"
            },
            {
                "mistake": "'지반 지지력'을 'sức chịu đất'로 번역",
                "correction": "'Sức chịu tải của nền đất'",
                "explanation": "Sức chịu đất는 구어체. 공식 용어는 sức chịu tải"
            }
        ],
        "examples": [
            {
                "ko": "PC기둥 30톤, 150톤 크레인 사용 양중계획 수립",
                "vi": "Lập kế hoạch cẩu lắp cột PC 30 tấn bằng cần cẩu 150 tấn",
                "situation": "formal"
            },
            {
                "ko": "작업반경 내 장애물 제거 및 신호수 배치",
                "vi": "Loại bỏ vật cản trong bán kính làm việc và bố trí người báo hiệu",
                "situation": "onsite"
            },
            {
                "ko": "지반 지지력 부족 시 철판 깔기로 보강",
                "vi": "Nếu sức chịu tải nền đất không đủ, gia cố bằng tấm thép lót",
                "situation": "onsite"
            }
        ],
        "relatedTerms": ["크레인", "안전관리", "작업반경", "PC부재"]
    },
    {
        "slug": "bai-tap-ket-pc",
        "korean": "PC야적장",
        "vietnamese": "Bãi tập kết PC",
        "hanja": "野積場",
        "hanjaReading": "野(들 야) + 積(쌓을 적) + 場(마당 장)",
        "pronunciation": "피씨 야적장",
        "meaningKo": "PC부재를 현장 내 임시로 쌓아두는 장소. 지반 다짐, 배수, 적재 높이, 받침목 위치 관리 필수. 통역 시 'bãi tập kết'(집결장)이 적절. '야적'은 '야외 적재'의 의미. '스톡야드'(stock yard)로도 불리나 한국은 '야적장'이 현장 표준.",
        "meaningVi": "Nơi xếp tạm thời các cấu kiện PC trong khu vực công trường. Phải quản lý đầm nền, thoát nước, chiều cao xếp, vị trí gối đỡ. Thuật ngữ 'bãi tập kết' phù hợp. Ý nghĩa '야적': xếp ngoài trời. Còn gọi 'stock yard' nhưng Hàn Quốc dùng '야적장'.",
        "context": "현장 관리, PC공법, 물류 계획",
        "culturalNote": "한국은 야적장 위치, 동선, 적재 순서까지 상세 계획. 베트남은 현장 정리 문화 약해 외국계 감리의 지적 많음. '정리정돈'을 'trật tự'(질서)로 강조하면 베트남 근로자 이해도 높아짐.",
        "commonMistakes": [
            {
                "mistake": "Kho chứa PC (PC 창고)",
                "correction": "Bãi tập kết PC (PC야적장)",
                "explanation": "Kho는 실내 창고. Bãi는 야외 적재장"
            },
            {
                "mistake": "'받침목'을 'gỗ đỡ'로 번역",
                "correction": "'Gối đỡ' 또는 'thanh đệm'",
                "explanation": "Gỗ đỡ는 일반 나무. 전문 용어는 gối đỡ(받침)"
            },
            {
                "mistake": "'적재 순서'를 'thứ tự chất'로 번역",
                "correction": "'Thứ tự xếp'",
                "explanation": "Chất는 일반 싣기. Xếp은 정돈하며 쌓기"
            }
        ],
        "examples": [
            {
                "ko": "PC야적장 지반 다짐 후 자갈 150mm 부설",
                "vi": "Sau khi đầm nền bãi tập kết PC, rải sỏi dày 150mm",
                "situation": "onsite"
            },
            {
                "ko": "부재별 식별표 부착, 설치 순서대로 적재",
                "vi": "Dán nhãn phân loại theo cấu kiện, xếp theo trình tự lắp đặt",
                "situation": "onsite"
            },
            {
                "ko": "적재 높이 3단 이하, 받침목 간격 2m",
                "vi": "Chiều cao xếp tối đa 3 tầng, khoảng cách gối đỡ 2m",
                "situation": "formal"
            }
        ],
        "relatedTerms": ["PC부재", "적재", "받침목", "현장관리"]
    },
    {
        "slug": "chi-tiet-ket-noi",
        "korean": "접합상세",
        "vietnamese": "Chi tiết kết nối",
        "hanja": "接合詳細",
        "hanjaReading": "接(이을 접) + 合(합할 합) + 詳(자세할 상) + 細(가늘 세)",
        "pronunciation": "접합 상세",
        "meaningKo": "PC부재 간 또는 부재와 구조체의 접합 방법을 표현한 상세도. 철근 배근, 용접 위치, 볼트 규격, 그라우트 범위 등 포함. 통역 시 'chi tiết'(디테일)은 한베 공통 사용. '접합'은 'kết nối'(연결) 또는 'liên kết'(결합). 시공 품질 좌우하므로 정확한 전달 필수.",
        "meaningVi": "Bản vẽ chi tiết thể hiện phương pháp nối giữa các cấu kiện PC hoặc giữa cấu kiện và kết cấu. Bao gồm bố trí cốt thép, vị trí hàn, quy cách bulông, phạm vi grouting. Thuật ngữ 'chi tiết' dùng chung Hàn-Việt. 'Kết nối' hoặc 'liên kết' đều được. Quyết định chất lượng thi công nên phải truyền đạt chính xác.",
        "context": "구조 설계, 시공 도면, 품질 관리",
        "culturalNote": "한국은 접합상세도 작성 의무(구조기준), 시공 전 검토회의 필수. 베트남은 도면 해석 능력 편차 커서 3D 모델 또는 목업(mock-up) 병행 권장. '도면'을 'bản vẽ'로, '목업'을 'mô hình thực' 또는 'mock-up'으로 표현.",
        "commonMistakes": [
            {
                "mistake": "Chi tiết nối (연결 디테일)",
                "correction": "Chi tiết kết nối (접합상세)",
                "explanation": "Chi tiết nối는 약식. 공식 용어는 chi tiết kết nối"
            },
            {
                "mistake": "'배근'을 'sắp xếp thép'로 번역",
                "correction": "'Bố trí cốt thép'",
                "explanation": "Sắp xếp는 일반 배치. 배근은 bố trí cốt thép"
            },
            {
                "mistake": "'목업'을 'mô hình'으로만 번역",
                "correction": "'Mô hình thực' 또는 'mock-up'",
                "explanation": "Mô hình은 일반 모델. Mock-up은 실물 크기 시험체"
            }
        ],
        "examples": [
            {
                "ko": "접합상세도 검토 후 철근 가공 시작",
                "vi": "Sau khi xem xét chi tiết kết nối, bắt đầu gia công cốt thép",
                "situation": "formal"
            },
            {
                "ko": "용접 위치 표시 및 용접사 자격 확인",
                "vi": "Đánh dấu vị trí hàn và xác nhận tư cách thợ hàn",
                "situation": "onsite"
            },
            {
                "ko": "목업 제작으로 접합 시공성 사전 검증",
                "vi": "Làm mock-up để kiểm chứng khả thi thi công mối nối trước",
                "situation": "formal"
            }
        ],
        "relatedTerms": ["접합부", "배근", "용접", "그라우트"]
    }
]

def main():
    # 파일 경로 설정
    project_root = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    target_file = os.path.join(project_root, "data", "terms", "construction.json")

    # 기존 파일 읽기
    if not os.path.exists(target_file):
        print(f"❌ 파일을 찾을 수 없습니다: {target_file}")
        return

    with open(target_file, "r", encoding="utf-8") as f:
        data = json.load(f)

    print(f"📂 기존 용어 수: {len(data)}개")

    # 중복 체크 (slug 기준)
    existing_slugs = {term["slug"] for term in data}
    new_slugs = {term["slug"] for term in new_terms}
    duplicates = existing_slugs & new_slugs

    if duplicates:
        print(f"⚠️  중복된 slug 발견: {duplicates}")
        print("중복 제거 후 진행합니다.")
        new_terms_filtered = [t for t in new_terms if t["slug"] not in existing_slugs]
    else:
        new_terms_filtered = new_terms

    # 용어 추가
    data.extend(new_terms_filtered)

    # 파일 저장
    with open(target_file, "w", encoding="utf-8") as f:
        json.dump(data, f, ensure_ascii=False, indent=2)

    print(f"✅ {len(new_terms_filtered)}개 용어 추가 완료!")
    print(f"📊 최종 용어 수: {len(data)}개")
    print(f"💾 저장 위치: {target_file}")

    # 추가된 용어 목록 출력
    print("\n📋 추가된 용어:")
    for i, term in enumerate(new_terms_filtered, 1):
        print(f"{i}. {term['korean']} ({term['vietnamese']}) - {term['slug']}")

if __name__ == "__main__":
    main()
