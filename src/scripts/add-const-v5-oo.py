#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
건설(Construction) 용어 추가 스크립트 v5
테마: 가설자재/소모품 (파이프서포트, 유로폼, 합판거푸집, 세파타이, 스페이서, 결속선, 전산볼트, 와이어, 턴버클, 클램프)
Tier S 품질 기준 (90점 이상)
"""

import json
import os

# 추가할 용어 데이터 (10개)
new_terms = [
    {
        "slug": "ong-chong-ong",
        "korean": "파이프서포트",
        "vietnamese": "Ống chống ống",
        "hanja": None,
        "hanjaReading": None,
        "pronunciation": "파이프서포트",
        "meaningKo": "슬래브나 보 하부를 지지하는 신축식 강관 지지대. 높이 조절이 가능하며 반복 사용이 가능한 가설자재입니다. 통역 시 '수직 지지대'와 혼동 주의 - 파이프서포트는 특히 신축 조절 기능을 강조해야 하며, 베트남 현장에서는 'ống chống'으로 통칭되지만 정확히는 'ống chống ống (강관 서포트)'로 구분해야 합니다. 설치 간격과 허용하중 전달 시 안전 규정 준수 여부를 반드시 확인해야 합니다.",
        "meaningVi": "Thanh chống ống thép có thể điều chỉnh chiều cao để đỡ phần dưới của sàn bê tông hoặc dầm. Là vật liệu tạm có thể sử dụng lại nhiều lần. Cần phân biệt với 'giá đỡ cố định' - pipe support nhấn mạnh khả năng điều chỉnh chiều cao. Khi thông dịch phải xác nhận khoảng cách lắp đặt và tải trọng cho phép.",
        "context": "거푸집 공사, 슬래브 타설 현장에서 사용",
        "culturalNote": "한국은 3.6m급 파이프서포트가 표준이며 안전율 3배 적용, 베트남은 2.5~3.0m급이 일반적이고 안전 기준이 상이할 수 있어 시공 전 기준 확인 필수. 한국 현장은 '서포트 간격도'를 별도 작성하지만 베트남은 구두 지시가 많아 통역사가 수치를 정확히 기록하고 전달해야 합니다. 또한 파이프서포트 해체 순서(콘크리트 양생 후)를 명확히 통역해야 조기 해체 사고를 예방할 수 있습니다.",
        "commonMistakes": [
            {
                "mistake": "Ống thép đỡ",
                "correction": "Ống chống ống (hoặc Pipe support)",
                "explanation": "'Ống thép đỡ'는 일반 강관 지지대를 의미하며, 신축 조절 기능이 있는 파이프서포트의 특성을 표현하지 못함"
            },
            {
                "mistake": "파이프서포트를 '기둥'으로 번역",
                "correction": "Ống chống (giá đỡ tạm thời)",
                "explanation": "'Cột (기둥)'은 영구 구조물을 의미하므로, 가설재인 파이프서포트와 혼동 금지"
            },
            {
                "mistake": "서포트 간격 1.2m → 'Khoảng cách 1.2m'만 전달",
                "correction": "Khoảng cách giữa các ống chống 1.2m theo chiều dọc và ngang",
                "explanation": "종횡 방향을 구분하지 않으면 시공 오류 발생 위험"
            }
        ],
        "examples": [
            {
                "ko": "슬래브 하부에 파이프서포트를 1m 간격으로 설치하세요.",
                "vi": "Lắp đặt ống chống ống ở dưới sàn với khoảng cách 1m.",
                "situation": "onsite"
            },
            {
                "ko": "파이프서포트의 허용하중은 2.5톤이며, 반드시 수직으로 설치해야 합니다.",
                "vi": "Tải trọng cho phép của ống chống ống là 2.5 tấn, bắt buộc phải lắp theo phương thẳng đứng.",
                "situation": "formal"
            },
            {
                "ko": "서포트 높이 좀 더 올려주세요. 레벨 안 맞아요.",
                "vi": "Nâng ống chống lên cao hơn một chút. Cao độ chưa đúng.",
                "situation": "informal"
            }
        ],
        "relatedTerms": ["거푸집", "슬래브", "동바리", "지보공"]
    },
    {
        "slug": "euroform",
        "korean": "유로폼",
        "vietnamese": "Euroform",
        "hanja": None,
        "hanjaReading": None,
        "pronunciation": "유로폼",
        "meaningKo": "알루미늄 또는 강재 프레임에 합판을 부착한 조립식 거푸집. 반복 사용이 가능하고 조립/해체가 간편하여 벽체, 기둥 거푸집으로 널리 사용됩니다. 통역 시 '시스템 거푸집'과 구분 필요 - 유로폼은 소규모 프로젝트에 적합한 범용 거푸집이며, 'gang form'은 대규모 반복 구조물용입니다. 베트남 현장에서는 'ván khuôn nhôm' 또는 'Euroform'으로 통용되나, 한국산과 중국산의 품질 차이가 있어 원산지 명시가 중요합니다.",
        "meaningVi": "Ván khuôn lắp ghép bằng khung nhôm hoặc thép gắn ván ép. Có thể tái sử dụng nhiều lần, dễ lắp ghép và tháo dỡ, thường dùng cho ván khuôn tường và cột. Phân biệt với 'ván khuôn hệ thống' - Euroform phù hợp dự án quy mô nhỏ. Khi thông dịch cần chú ý xuất xứ (Hàn Quốc hay Trung Quốc) vì chất lượng khác biệt.",
        "context": "거푸집 공사, 콘크리트 타설 현장",
        "culturalNote": "한국은 0.6m×1.2m, 0.6m×1.8m 규격이 표준이고 100회 이상 재사용이 일반적이나, 베트남은 0.6m×1.5m 등 비표준 규격도 많고 재사용 횟수가 50~70회로 짧습니다. 한국 현장은 유로폼 번호를 도면에 표기하지만 베트남은 현장 조합이 많아 조립 순서를 구두로 정확히 전달해야 합니다. 또한 유로폼 표면에 박리제(form oil) 도포 여부를 명확히 통역해야 콘크리트 표면 품질을 유지할 수 있습니다.",
        "commonMistakes": [
            {
                "mistake": "Ván khuôn nhôm",
                "correction": "Euroform (hoặc Ván khuôn nhôm lắp ghép)",
                "explanation": "'Ván khuôn nhôm'은 알루미늄 거푸집 일반을 지칭하므로, 조립식 특성을 명시해야 유로폼의 정확한 의미 전달"
            },
            {
                "mistake": "유로폼을 'Gang form'으로 번역",
                "correction": "Euroform (ván khuôn lắp ghép quy mô nhỏ)",
                "explanation": "Gang form은 대형 시스템 거푸집으로 유로폼과 용도가 다름"
            },
            {
                "mistake": "유로폼 100장 → 'Euroform 100 cái'",
                "correction": "Euroform 100 tấm (hoặc 100 panel)",
                "explanation": "베트남어로 'cái'는 일반 개수 단위이므로, 'tấm (장)' 또는 'panel'로 정확히 전달"
            }
        ],
        "examples": [
            {
                "ko": "이번 층 벽체는 유로폼 0.6×1.8 규격으로 시공합니다.",
                "vi": "Tường tầng này thi công bằng Euroform kích thước 0.6×1.8m.",
                "situation": "formal"
            },
            {
                "ko": "유로폼 표면에 박리제 바르고 조립 시작하세요.",
                "vi": "Phết dung dịch tách khuôn lên mặt Euroform rồi bắt đầu lắp ghép.",
                "situation": "onsite"
            },
            {
                "ko": "유로폼 모서리 찌그러진 거 교체 좀 해주세요.",
                "vi": "Thay những tấm Euroform bị móp góc giúp tôi.",
                "situation": "informal"
            }
        ],
        "relatedTerms": ["거푸집", "합판거푸집", "박리제", "타이바"]
    },
    {
        "slug": "van-khuon-van-ep",
        "korean": "합판거푸집",
        "vietnamese": "Ván khuôn ván ép",
        "hanja": "合板거푸집",
        "hanjaReading": "合(합할 합) + 板(널빤지 판)",
        "pronunciation": "합판거푸집",
        "meaningKo": "합판(plywood)을 사용한 전통적 거푸집 형태. 자유로운 형상 시공이 가능하나 재사용 횟수가 제한적입니다. 통역 시 '목재 거푸집'과 구분 - 합판거푸집은 여러 겹의 단판을 접착한 공학목재이며, 일반 목재보다 강도와 내수성이 우수합니다. 베트남 현장에서는 'ván khuôn gỗ'로 통칭되기도 하나, 정확히는 'ván ép (합판)'을 사용한 거푸집임을 명시해야 자재 조달에 혼선이 없습니다.",
        "meaningVi": "Loại ván khuôn sử dụng ván ép (plywood) truyền thống. Có thể thi công hình dạng tự do nhưng số lần tái sử dụng hạn chế. Phân biệt với 'ván khuôn gỗ tự nhiên' - ván ép là gỗ kỹ thuật ghép nhiều lớp, có độ bền và chống nước tốt hơn gỗ thường. Cần ghi rõ 'ván ép' để tránh nhầm lẫn khi đặt hàng vật liệu.",
        "context": "거푸집 공사, 비정형 구조물 시공",
        "culturalNote": "한국은 12mm, 15mm 두께 합판이 표준이고 방수 처리된 'Black Form'을 선호하나, 베트남은 12mm가 일반적이고 방수 처리 없는 일반 합판도 많습니다. 한국 현장은 합판 재사용 횟수(보통 5~7회)를 정확히 관리하지만, 베트남은 육안 점검에 의존하는 경우가 많아 통역 시 수치 기준을 명확히 전달해야 합니다. 또한 합판 절단 시 톱날 방향과 절단면 처리 방법을 구체적으로 통역해야 품질을 유지할 수 있습니다.",
        "commonMistakes": [
            {
                "mistake": "Ván khuôn gỗ",
                "correction": "Ván khuôn ván ép (plywood formwork)",
                "explanation": "'Ván gỗ'는 원목 거푸집을 의미하므로, 합판의 적층 구조를 표현하지 못함"
            },
            {
                "mistake": "합판거푸집을 'OSB 거푸집'으로 번역",
                "correction": "Ván khuôn ván ép (không phải OSB)",
                "explanation": "OSB(Oriented Strand Board)는 합판과 다른 재료이므로 혼동 금지"
            },
            {
                "mistake": "15mm 합판 → 'Ván ép 15'만 전달",
                "correction": "Ván ép dày 15mm (hoặc 15 ly)",
                "explanation": "두께 단위 'mm' 또는 베트남 단위 'ly (층)'를 명시해야 정확한 자재 발주 가능"
            }
        ],
        "examples": [
            {
                "ko": "곡면 부분은 합판거푸집으로 시공하고, 직선 구간은 유로폼을 사용하세요.",
                "vi": "Phần cong thi công bằng ván khuôn ván ép, đoạn thẳng dùng Euroform.",
                "situation": "formal"
            },
            {
                "ko": "합판거푸집 5회 사용했으니 교체 시기입니다.",
                "vi": "Ván khuôn ván ép đã dùng 5 lần, đến thời điểm cần thay mới.",
                "situation": "onsite"
            },
            {
                "ko": "합판 자르는 거 반대로 자르지 마세요. 결 방향 보고 자르세요.",
                "vi": "Đừng cắt ván ép ngược hướng. Cắt theo hướng vân gỗ.",
                "situation": "informal"
            }
        ],
        "relatedTerms": ["거푸집", "유로폼", "목재", "박리제"]
    },
    {
        "slug": "sepa-tai",
        "korean": "세파타이",
        "vietnamese": "Sepa Tie",
        "hanja": None,
        "hanjaReading": None,
        "pronunciation": "세파타이",
        "meaningKo": "거푸집 간격을 유지하고 콘크리트 타설 시 거푸집이 벌어지지 않도록 고정하는 분리형 철물. 타설 후 중앙부를 제거하고 외부 캡으로 마감합니다. 통역 시 '타이바(tie bar)'와 구분 필요 - 세파타이는 분리 가능한 구조로 콘크리트 표면에 흔적을 최소화하며, 일체형 타이바는 제거 후 구멍이 남습니다. 베트남 현장에서는 'thanh giằng tách rời' 또는 'Sepa'로 통용되나, 규격(M12, M16 등)과 길이를 정확히 전달해야 합니다.",
        "meaningVi": "Vật liệu kim loại tách rời dùng để giữ khoảng cách giữa các tấm ván khuôn và cố định để ván khuôn không bị tách ra khi đổ bê tông. Sau khi đổ xong, tháo bỏ phần giữa và hoàn thiện bằng nút bịt bên ngoài. Phân biệt với 'tie bar nguyên khối' - Sepa có cấu trúc tháo rời, để lại dấu vết tối thiểu trên bề mặt bê tông. Cần truyền đạt chính xác quy cách (M12, M16...) và chiều dài.",
        "context": "거푸집 공사, 벽체 콘크리트 타설",
        "culturalNote": "한국은 M12×1000mm, M16×1200mm 등 표준 규격을 사용하고 세파타이 간격을 설계도에 명시하나, 베트남은 비표준 길이도 많고 간격을 현장 재량으로 결정하는 경우가 있어 통역 시 명확한 수치 전달이 필수입니다. 한국 현장은 세파타이 제거 시기(콘크리트 강도 5MPa 이상)를 엄격히 관리하지만, 베트남은 경험에 의존하는 경우가 많아 양생 기간을 구체적으로 통역해야 품질 문제를 예방할 수 있습니다.",
        "commonMistakes": [
            {
                "mistake": "Thanh giằng",
                "correction": "Sepa Tie (thanh giằng tách rời)",
                "explanation": "'Thanh giằng'은 일반 타이바를 의미하므로, 분리형 구조인 세파타이의 특성을 표현하지 못함"
            },
            {
                "mistake": "세파타이를 '앵커볼트'로 번역",
                "correction": "Sepa Tie (không phải bulông neo)",
                "explanation": "앵커볼트는 구조물 고정용이므로, 거푸집 간격 유지용 세파타이와 용도가 다름"
            },
            {
                "mistake": "세파타이 600간격 → 'Khoảng cách 600'만 전달",
                "correction": "Khoảng cách Sepa Tie 600mm theo phương ngang và phương đứng",
                "explanation": "종횡 방향과 단위를 명시하지 않으면 시공 오류 위험"
            }
        ],
        "examples": [
            {
                "ko": "벽체 세파타이는 수평 600mm, 수직 500mm 간격으로 설치하세요.",
                "vi": "Lắp Sepa Tie tường với khoảng cách ngang 600mm, dọc 500mm.",
                "situation": "formal"
            },
            {
                "ko": "콘크리트 강도 5MPa 나온 후 세파타이 제거하고 마감하세요.",
                "vi": "Sau khi bê tông đạt cường độ 5MPa, tháo Sepa Tie và hoàn thiện.",
                "situation": "onsite"
            },
            {
                "ko": "세파 구멍 메울 때 모르타르 제대로 채워 넣으세요.",
                "vi": "Khi trám lỗ Sepa, phải lấp đầy vữa xi măng đúng cách.",
                "situation": "informal"
            }
        ],
        "relatedTerms": ["거푸집", "타이바", "유로폼", "콘크리트"]
    },
    {
        "slug": "spacer",
        "korean": "스페이서",
        "vietnamese": "Spacer",
        "hanja": None,
        "hanjaReading": None,
        "pronunciation": "스페이서",
        "meaningKo": "철근과 거푸집 사이의 피복두께(콘크리트 보호층)를 확보하기 위한 받침재. 플라스틱, 콘크리트, 모르타르 등 다양한 재질이 있습니다. 통역 시 '철근 받침대'와 혼동 주의 - 스페이서는 피복두께 유지가 목적이며, 철근 받침대(bar support)는 철근의 높이를 유지하는 것이 목적입니다. 베트남 현장에서는 'đệm bê tông' 또는 'spacer'로 통용되나, 규격(20mm, 30mm 등)을 정확히 전달해야 구조 안전을 확보할 수 있습니다.",
        "meaningVi": "Vật đệm để đảm bảo độ dày lớp bảo vệ (lớp bê tông phủ) giữa cốt thép và ván khuôn. Có nhiều chất liệu như nhựa, bê tông, vữa xi măng. Phân biệt với 'giá đỡ cốt thép' - spacer có mục đích duy trì độ dày lớp phủ, còn bar support duy trì độ cao cốt thép. Cần truyền đạt chính xác quy cách (20mm, 30mm...) để đảm bảo an toàn kết cấu.",
        "context": "철근 공사, 콘크리트 타설 준비",
        "culturalNote": "한국은 슬래브 20mm, 벽체 40mm, 기초 70mm 등 부위별 피복두께 기준이 엄격하고 플라스틱 스페이서를 선호하나, 베트남은 기준이 느슨하고 콘크리트 스페이서나 모르타르 블록을 많이 사용합니다. 한국 현장은 스페이서 설치 개수(철근 1m²당 4~5개)를 명시하지만, 베트남은 경험적으로 배치하는 경우가 많아 통역 시 구체적 수치를 전달해야 품질을 유지할 수 있습니다. 특히 해안가 구조물은 피복두께가 중요하므로 스페이서 규격을 반드시 확인해야 합니다.",
        "commonMistakes": [
            {
                "mistake": "Đệm bê tông",
                "correction": "Spacer (đệm lớp phủ bê tông)",
                "explanation": "'Đệm bê tông'은 콘크리트 받침 일반을 지칭하므로, 피복두께 확보 목적을 명시해야 정확한 의미 전달"
            },
            {
                "mistake": "스페이서를 'Bar support'로 번역",
                "correction": "Spacer (không phải bar support)",
                "explanation": "Bar support는 철근 높이 유지용이므로 용도가 다름"
            },
            {
                "mistake": "스페이서 30 → 'Spacer 30'만 전달",
                "correction": "Spacer 30mm (độ dày lớp phủ 30mm)",
                "explanation": "단위 'mm'와 '피복두께'를 명시해야 정확한 시공 가능"
            }
        ],
        "examples": [
            {
                "ko": "슬래브 하부 철근에 스페이서 30mm를 1m²당 5개씩 설치하세요.",
                "vi": "Lắp spacer 30mm cho cốt thép dưới sàn, 5 cái/m².",
                "situation": "formal"
            },
            {
                "ko": "스페이서 설치 후 철근 배근 검사 받으세요.",
                "vi": "Sau khi lắp spacer, kiểm tra bố trí cốt thép.",
                "situation": "onsite"
            },
            {
                "ko": "스페이서 너무 적게 넣었어요. 더 추가하세요.",
                "vi": "Spacer đặt quá ít. Thêm vào nữa.",
                "situation": "informal"
            }
        ],
        "relatedTerms": ["철근", "피복두께", "거푸집", "콘크리트"]
    },
    {
        "slug": "day-ket-thep",
        "korean": "결속선",
        "vietnamese": "Dây kết thép",
        "hanja": "結束線",
        "hanjaReading": "結(맺을 결) + 束(묶을 속) + 線(줄 선)",
        "pronunciation": "결속선",
        "meaningKo": "철근을 결합하거나 고정할 때 사용하는 철선(wire). 일반적으로 #8(2.6mm), #10(3.2mm) 규격을 사용하며, 아연도금 처리된 제품이 녹 방지에 유리합니다. 통역 시 '철근 고정용 와이어'와 동일 의미이나, 한국 현장에서는 '결속선'이라는 용어가 더 일반적입니다. 베트남 현장에서는 'dây thép buộc' 또는 'dây kết'으로 통용되며, 굵기 번호(#8, #10) 체계를 정확히 이해해야 자재 조달에 혼선이 없습니다.",
        "meaningVi": "Dây thép dùng để buộc và cố định cốt thép. Thường dùng quy cách #8 (2.6mm), #10 (3.2mm), sản phẩm mạ kẽm có lợi cho chống rỉ sét. 'Dây thép buộc cốt thép' có cùng ý nghĩa, nhưng thuật ngữ 'dây kết' phổ biến hơn tại công trường Hàn Quốc. Cần hiểu chính xác hệ thống số đường kính (#8, #10) để tránh nhầm lẫn khi đặt hàng.",
        "context": "철근 공사, 철근 배근 작업",
        "culturalNote": "한국은 #8 결속선이 표준이고 전동 결속기(rebar tier)를 많이 사용하나, 베트남은 #10을 선호하고 수동 결속이 일반적입니다. 한국 현장은 결속 간격(300~500mm)을 도면에 명시하지만, 베트남은 현장 판단에 맡기는 경우가 많아 통역 시 구체적 수치를 전달해야 품질을 유지할 수 있습니다. 또한 결속선 꼬임 방향(시계방향 2~3회)과 끝 처리 방법(안쪽으로 구부리기)을 정확히 통역해야 작업자 안전과 콘크리트 표면 품질을 확보할 수 있습니다.",
        "commonMistakes": [
            {
                "mistake": "Dây thép",
                "correction": "Dây kết thép (rebar tie wire)",
                "explanation": "'Dây thép'은 일반 철선을 의미하므로, 철근 결속 전용임을 명시해야 정확한 의미 전달"
            },
            {
                "mistake": "결속선을 'Wire rope'로 번역",
                "correction": "Rebar tie wire (không phải wire rope)",
                "explanation": "Wire rope는 강선 로프로 용도가 다름"
            },
            {
                "mistake": "#8 결속선 → 'Dây #8'만 전달",
                "correction": "Dây kết #8 (đường kính 2.6mm)",
                "explanation": "번호 체계가 익숙하지 않은 경우를 대비해 실제 직경도 함께 전달"
            }
        ],
        "examples": [
            {
                "ko": "철근 교차부는 결속선 #8로 300mm 간격마다 결속하세요.",
                "vi": "Buộc các điểm giao cốt thép bằng dây kết #8, khoảng cách 300mm.",
                "situation": "formal"
            },
            {
                "ko": "결속선 끝을 안쪽으로 구부려서 마감하세요.",
                "vi": "Uốn đầu dây kết vào phía trong để hoàn thiện.",
                "situation": "onsite"
            },
            {
                "ko": "결속선 부족해요. 한 묶음 더 가져오세요.",
                "vi": "Dây kết không đủ. Lấy thêm một cuộn nữa.",
                "situation": "informal"
            }
        ],
        "relatedTerms": ["철근", "철근 배근", "전동 결속기", "아연도금"]
    },
    {
        "slug": "bulong-dien-toan",
        "korean": "전산볼트",
        "vietnamese": "Bulông điện toán",
        "hanja": "電算볼트",
        "hanjaReading": "電(전기 전) + 算(셈 산)",
        "pronunciation": "전산볼트",
        "meaningKo": "철골 구조물 접합에 사용되는 고강도 볼트. 전단력과 인장력을 동시에 받을 수 있으며, 토크렌치로 정확한 체결력을 관리합니다. 통역 시 '고력볼트(high tension bolt)'와 동일 의미이나, 한국 현장에서는 '전산볼트'라는 용어가 더 일반적입니다. 베트남 현장에서는 'bulông cường độ cao' 또는 'tension bolt'로 통용되며, 등급(F8T, F10T)과 조임 토크 값을 정확히 전달해야 구조 안전을 확보할 수 있습니다.",
        "meaningVi": "Bulông cường độ cao dùng cho liên kết kết cấu thép. Có thể chịu đồng thời lực cắt và lực kéo, quản lý lực xiết chính xác bằng cờ lê lực. 'High tension bolt' có cùng nghĩa, nhưng thuật ngữ 'bulông điện toán' phổ biến hơn tại Hàn Quốc. Cần truyền đạt chính xác cấp độ (F8T, F10T) và giá trị mô-men xiết để đảm bảo an toàn kết cấu.",
        "context": "철골 공사, 강구조 접합부 시공",
        "culturalNote": "한국은 F10T(M20, M22) 규격이 표준이고 1차 조임(70%)-마킹-2차 조임(100%)-검사의 3단계 체결 절차를 엄격히 준수하나, 베트남은 F8T를 많이 사용하고 체결 절차가 간소한 경우가 있어 통역 시 단계별 작업 내용을 명확히 전달해야 합니다. 한국 현장은 토크렌치 교정 주기(월 1회)를 관리하지만, 베트남은 육안 점검에 의존하는 경우가 많아 정량적 관리 기준을 구체적으로 통역해야 품질을 유지할 수 있습니다.",
        "commonMistakes": [
            {
                "mistake": "Bulông thường",
                "correction": "Bulông điện toán (hoặc Bulông cường độ cao)",
                "explanation": "'Bulông thường'은 일반 볼트를 의미하므로, 고강도 특성을 명시해야 정확한 의미 전달"
            },
            {
                "mistake": "전산볼트를 'Anchor bolt'로 번역",
                "correction": "Bulông điện toán (không phải bulông neo)",
                "explanation": "Anchor bolt는 구조물 고정용이므로, 철골 접합용 전산볼트와 용도가 다름"
            },
            {
                "mistake": "F10T M22 → 'F10T M22'만 전달",
                "correction": "Bulông điện toán F10T, đường kính M22 (mô-men xiết 650N·m)",
                "explanation": "등급, 직경, 조임 토크를 모두 전달해야 정확한 시공 가능"
            }
        ],
        "examples": [
            {
                "ko": "기둥-보 접합부는 전산볼트 F10T M22로 체결하세요.",
                "vi": "Liên kết cột-dầm xiết bằng bulông điện toán F10T M22.",
                "situation": "formal"
            },
            {
                "ko": "1차 조임 70% 완료 후 마킹하고 2차 조임 100% 하세요.",
                "vi": "Sau khi xiết sơ bộ 70%, đánh dấu rồi xiết chặt 100%.",
                "situation": "onsite"
            },
            {
                "ko": "전산볼트 토크렌치로 다시 확인 좀 해주세요.",
                "vi": "Kiểm tra lại bulông điện toán bằng cờ lê lực giúp tôi.",
                "situation": "informal"
            }
        ],
        "relatedTerms": ["철골", "토크렌치", "고력볼트", "강구조"]
    },
    {
        "slug": "day-thep",
        "korean": "와이어",
        "vietnamese": "Dây thép",
        "hanja": None,
        "hanjaReading": None,
        "pronunciation": "와이어",
        "meaningKo": "철골 구조물의 임시 고정, 인양, 지지 등에 사용하는 강선(steel wire). 직경과 강도에 따라 다양한 용도로 사용되며, 와이어로프(wire rope)와 단선 와이어로 구분됩니다. 통역 시 '강선(steel wire)'과 동일 의미이나, 한국 건설 현장에서는 '와이어'라는 외래어가 더 일반적입니다. 베트남 현장에서는 'dây cáp thép' 또는 'wire'로 통용되며, 용도(인양용/지지용)와 허용하중을 정확히 전달해야 안전사고를 예방할 수 있습니다.",
        "meaningVi": "Cáp thép dùng để cố định tạm thời, nâng hạ, đỡ kết cấu thép. Sử dụng cho nhiều mục đích khác nhau tùy theo đường kính và cường độ, phân biệt giữa wire rope (dây cáp thép) và single wire (dây đơn). Thuật ngữ 'wire' phổ biến hơn 'cáp thép' tại công trường Hàn Quốc. Cần truyền đạt chính xác mục đích sử dụng (nâng hạ/đỡ) và tải trọng cho phép để phòng ngừa tai nạn.",
        "context": "철골 공사, 중량물 인양, 가설 구조물 지지",
        "culturalNote": "한국은 6×24 구조의 와이어로프가 표준이고 안전계수 6배 이상을 적용하나, 베트남은 6×19 구조도 많이 사용하고 안전계수가 4~5배로 낮은 경우가 있어 통역 시 안전 기준을 명확히 전달해야 합니다. 한국 현장은 와이어 교체 주기(사용 횟수, 소선 절단 개수)를 정량적으로 관리하지만, 베트남은 육안 점검에 의존하는 경우가 많아 구체적 교체 기준을 통역해야 안전을 확보할 수 있습니다. 특히 인양 작업 시 와이어 각도(60도 이하 권장)를 정확히 전달해야 과하중을 방지할 수 있습니다.",
        "commonMistakes": [
            {
                "mistake": "Dây cáp",
                "correction": "Dây cáp thép (steel wire rope)",
                "explanation": "'Dây cáp'은 케이블 일반을 지칭하므로, 강재임을 명시해야 정확한 의미 전달"
            },
            {
                "mistake": "와이어를 'Chain'으로 번역",
                "correction": "Dây cáp thép (không phải xích)",
                "explanation": "Chain은 체인으로 용도와 구조가 다름"
            },
            {
                "mistake": "와이어 12mm → 'Dây 12mm'만 전달",
                "correction": "Dây cáp thép 12mm (tải trọng cho phép 2 tấn)",
                "explanation": "직경뿐 아니라 허용하중을 함께 전달해야 안전 작업 가능"
            }
        ],
        "examples": [
            {
                "ko": "철골 부재 인양 시 와이어로프 12mm 이상 사용하고 안전계수 6배 확보하세요.",
                "vi": "Khi nâng cấu kiện thép, dùng dây cáp thép từ 12mm trở lên và đảm bảo hệ số an toàn gấp 6 lần.",
                "situation": "formal"
            },
            {
                "ko": "와이어 소선 10개 이상 끊어졌으면 교체하세요.",
                "vi": "Nếu dây cáp đứt trên 10 sợi nhỏ, thay mới.",
                "situation": "onsite"
            },
            {
                "ko": "와이어 각도 너무 좁아요. 슬링 길이 늘려주세요.",
                "vi": "Góc dây cáp quá nhỏ. Kéo dài sling ra.",
                "situation": "informal"
            }
        ],
        "relatedTerms": ["철골", "인양", "샤클", "슬링"]
    },
    {
        "slug": "turnbuckle",
        "korean": "턴버클",
        "vietnamese": "Turnbuckle",
        "hanja": None,
        "hanjaReading": None,
        "pronunciation": "턴버클",
        "meaningKo": "와이어나 로드의 장력을 조절하는 나사식 조임 철물. 양쪽 끝에 나사가 반대 방향으로 되어 있어 중앙 몸체를 돌리면 길이가 조절됩니다. 통역 시 '장력 조절기' 또는 '텐셔너(tensioner)'와 유사하나, 나사 방식의 수동 조절 장치를 지칭할 때는 '턴버클'이 정확합니다. 베트남 현장에서는 'bộ căng dây' 또는 'turnbuckle'로 통용되며, 규격(M12, M16 등)과 허용하중을 정확히 전달해야 구조 안정성을 확보할 수 있습니다.",
        "meaningVi": "Thiết bị kim loại kiểu vít dùng để điều chỉnh lực căng của dây cáp hoặc thanh thép. Có ren ngược chiều ở hai đầu, xoay thân giữa để điều chỉnh chiều dài. 'Bộ căng dây' hoặc 'tensioner' tương tự, nhưng turnbuckle chỉ thiết bị điều chỉnh bằng tay kiểu vít. Cần truyền đạt chính xác quy cách (M12, M16...) và tải trọng cho phép để đảm bảo ổn định kết cấu.",
        "context": "철골 공사, 가시설 지지, 와이어 장력 조절",
        "culturalNote": "한국은 M12, M16 규격이 표준이고 장력계(tension meter)로 정량적 관리를 하나, 베트남은 비표준 규격도 많고 육안 또는 경험으로 장력을 판단하는 경우가 있어 통역 시 수치 기준을 명확히 전달해야 품질을 유지할 수 있습니다. 한국 현장은 턴버클 체결 후 고정핀 또는 와이어로 역회전 방지 조치를 필수로 하나, 베트남은 이를 생략하는 경우가 있어 안전 절차를 구체적으로 통역해야 사고를 예방할 수 있습니다.",
        "commonMistakes": [
            {
                "mistake": "Bộ căng",
                "correction": "Turnbuckle (bộ căng dây kiểu vít)",
                "explanation": "'Bộ căng'은 장력 조절 장치 일반을 지칭하므로, 나사식 구조를 명시해야 정확한 의미 전달"
            },
            {
                "mistake": "턴버클을 'Tensioner'로 번역",
                "correction": "Turnbuckle (không phải tensioner tự động)",
                "explanation": "Tensioner는 자동 장력 조절 장치를 의미하므로, 수동 조절 방식인 턴버클과 구분 필요"
            },
            {
                "mistake": "턴버클 M16 → 'Turnbuckle M16'만 전달",
                "correction": "Turnbuckle M16 (tải trọng cho phép 3 tấn)",
                "explanation": "규격뿐 아니라 허용하중을 함께 전달해야 안전 작업 가능"
            }
        ],
        "examples": [
            {
                "ko": "철골 가시설 브레이싱에 턴버클 M16을 설치하고 장력 2톤으로 조정하세요.",
                "vi": "Lắp turnbuckle M16 vào thanh chống xiên giàn giáo thép và điều chỉnh lực căng 2 tấn.",
                "situation": "formal"
            },
            {
                "ko": "턴버클 조정 후 고정핀 끼워서 역회전 방지하세요.",
                "vi": "Sau khi điều chỉnh turnbuckle, lắp chốt cố định để chống xoay ngược.",
                "situation": "onsite"
            },
            {
                "ko": "턴버클 너무 빡빡하게 조이지 마세요. 와이어 끊어져요.",
                "vi": "Đừng vặn turnbuckle quá chặt. Dây cáp sẽ đứt.",
                "situation": "informal"
            }
        ],
        "relatedTerms": ["와이어", "철골", "브레이싱", "장력"]
    },
    {
        "slug": "clamp",
        "korean": "클램프",
        "vietnamese": "Clamp",
        "hanja": None,
        "hanjaReading": None,
        "pronunciation": "클램프",
        "meaningKo": "파이프, 철골, 목재 등을 임시 고정하거나 결속할 때 사용하는 조임 철물. 용도에 따라 파이프 클램프, C클램프, 빔 클램프 등 다양한 종류가 있습니다. 통역 시 '고정 집게' 또는 '죔쇠'로 의역 가능하나, 건설 현장에서는 '클램프'라는 용어가 보편적입니다. 베트남 현장에서는 'kẹp' 또는 'clamp'로 통용되며, 종류(pipe clamp, beam clamp)와 허용하중을 정확히 전달해야 안전사고를 예방할 수 있습니다.",
        "meaningVi": "Thiết bị kẹp kim loại dùng để cố định tạm thời hoặc buộc ống, kết cấu thép, gỗ. Có nhiều loại tùy mục đích như pipe clamp, C-clamp, beam clamp. Có thể dịch nghĩa là 'kẹp cố định', nhưng thuật ngữ 'clamp' phổ biến hơn tại công trường. Cần truyền đạt chính xác loại (pipe clamp, beam clamp) và tải trọng cho phép để phòng ngừa tai nạn.",
        "context": "가설 공사, 철골 공사, 임시 고정 작업",
        "culturalNote": "한국은 KS 규격 클램프를 사용하고 허용하중 표시를 의무화하나, 베트남은 비표준 제품이 많고 하중 표시가 없는 경우가 있어 통역 시 안전 기준을 명확히 전달해야 합니다. 한국 현장은 클램프 점검 주기(주 1회)를 관리하지만, 베트남은 설치 후 점검을 생략하는 경우가 많아 정기 점검 절차를 구체적으로 통역해야 안전을 확보할 수 있습니다. 특히 파이프 클램프는 조임 토크가 중요하므로 '손으로 조이기'가 아닌 '토크렌치 사용' 등 구체적 방법을 전달해야 합니다.",
        "commonMistakes": [
            {
                "mistake": "Kẹp",
                "correction": "Clamp (kẹp cố định kim loại)",
                "explanation": "'Kẹp'은 집게 일반을 지칭하므로, 건설용 금속 클램프임을 명시해야 정확한 의미 전달"
            },
            {
                "mistake": "클램프를 'Vise'로 번역",
                "correction": "Clamp (không phải vise)",
                "explanation": "Vise는 작업대용 고정 바이스이므로, 현장 임시 고정용 클램프와 용도가 다름"
            },
            {
                "mistake": "파이프 클램프 → 'Pipe clamp'만 전달",
                "correction": "Pipe clamp (đường kính ống 48.6mm, tải trọng 500kg)",
                "explanation": "적용 파이프 직경과 허용하중을 함께 전달해야 안전 작업 가능"
            }
        ],
        "examples": [
            {
                "ko": "비계 파이프 연결부에 파이프 클램프를 설치하고 토크렌치로 40N·m 조임하세요.",
                "vi": "Lắp pipe clamp tại điểm nối ống giàn giáo và xiết bằng cờ lê lực 40N·m.",
                "situation": "formal"
            },
            {
                "ko": "클램프 체결 후 흔들림 테스트 하세요.",
                "vi": "Sau khi xiết clamp, kiểm tra độ rung.",
                "situation": "onsite"
            },
            {
                "ko": "클램프 좀 더 조여주세요. 헐렁해요.",
                "vi": "Vặn chặt clamp hơn nữa. Bị lỏng.",
                "situation": "informal"
            }
        ],
        "relatedTerms": ["파이프", "비계", "철골", "볼트"]
    }
]

# 기존 JSON 파일 경로
json_file_path = os.path.join(
    os.path.dirname(os.path.dirname(__file__)),
    "data",
    "terms",
    "construction.json"
)

# 기존 데이터 읽기
try:
    with open(json_file_path, "r", encoding="utf-8") as f:
        existing_data = json.load(f)
    print(f"✅ 기존 데이터 로드 완료: {len(existing_data)}개 용어")
except FileNotFoundError:
    print(f"❌ 파일을 찾을 수 없습니다: {json_file_path}")
    exit(1)
except json.JSONDecodeError as e:
    print(f"❌ JSON 파싱 오류: {e}")
    exit(1)

# 신규 용어 추가
existing_data.extend(new_terms)
print(f"✅ 신규 용어 {len(new_terms)}개 추가")

# JSON 파일 저장 (한글 유지, 들여쓰기 2칸)
try:
    with open(json_file_path, "w", encoding="utf-8") as f:
        json.dump(existing_data, f, ensure_ascii=False, indent=2)
    print(f"✅ 저장 완료: {json_file_path}")
    print(f"📊 총 용어 개수: {len(existing_data)}개")
except Exception as e:
    print(f"❌ 저장 실패: {e}")
    exit(1)
