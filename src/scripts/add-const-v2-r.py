#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Construction Terms - Drawing & BIM (도면/BIM/디지털)
평면도, 입면도, 단면도, 상세도, 구조도, BIM, LOD, 3D스캔, 물량산출, 내역서
"""

data = [
    {
        "slug": "ban-ve-mat-bang",
        "korean": "평면도",
        "vietnamese": "Bản vẽ mặt bằng",
        "hanja": "平面圖",
        "hanjaReading": "平(평평할 평) + 面(낯 면) + 圖(그림 도)",
        "pronunciation": "반베맛방",
        "meaningKo": "건물이나 층을 수평으로 절단하여 위에서 내려다본 모습을 표현한 도면. 통역 시 'sơ đồ mặt bằng'과 혼동 주의 - sơ đồ는 개념도, bản vẽ는 정식 도면. 베트남에서는 'mặt bằng tầng'(층평면도)으로 구체화하는 경우 많음. 실무에서 평면도 검토 시 베트남 현장은 축척 확인을 한국보다 더 엄격하게 요구하는 경향.",
        "meaningVi": "Bản vẽ thể hiện mặt cắt ngang của công trình khi nhìn từ trên xuống. Thường bao gồm bố trí phòng, kích thước, vị trí cửa, cầu thang. Là loại bản vẽ cơ bản nhất trong hồ sơ thiết kế. Trong tiếng Việt phân biệt rõ 'bản vẽ mặt bằng' (kỹ thuật) và 'sơ đồ mặt bằng' (ý tưởng).",
        "context": "도면 작성, 설계 검토, 시공 지시",
        "culturalNote": "한국에서는 평면도를 'floor plan'으로 영어 병기하는 경우 많지만, 베트남에서는 'bản vẽ mặt bằng' 표현이 더 공식적. 베트남 건축법상 평면도는 축척 1/50~1/100 기준이 일반적이며, 한국의 1/100~1/200보다 더 상세한 표현 요구. 베트남 현장에서는 평면도에 가구 배치까지 표기하는 경우가 많아 한국식 간략 평면도와 차이.",
        "commonMistakes": [
            {
                "mistake": "sơ đồ mặt bằng",
                "correction": "bản vẽ mặt bằng",
                "explanation": "sơ đồ는 개념도/배치도, bản vẽ는 정식 기술 도면"
            },
            {
                "mistake": "bản vẽ tầng",
                "correction": "bản vẽ mặt bằng (tầng)",
                "explanation": "층을 나타낼 때는 'mặt bằng tầng X' 형식 사용"
            },
            {
                "mistake": "'평면도 보내드릴게요'를 'Tôi sẽ gửi sơ đồ'로 통역",
                "correction": "'Tôi sẽ gửi bản vẽ mặt bằng'",
                "explanation": "정식 도면은 반드시 'bản vẽ' 사용"
            }
        ],
        "examples": [
            {
                "ko": "1층 평면도 먼저 검토해 주세요.",
                "vi": "Vui lòng xem xét bản vẽ mặt bằng tầng 1 trước.",
                "situation": "formal"
            },
            {
                "ko": "평면도 축척이 1/100 맞나요?",
                "vi": "Tỷ lệ bản vẽ mặt bằng là 1/100 phải không?",
                "situation": "onsite"
            },
            {
                "ko": "평면도 수정본 내일까지 보내드리겠습니다.",
                "vi": "Bản vẽ mặt bằng sửa đổi tôi sẽ gửi trước ngày mai.",
                "situation": "formal"
            }
        ],
        "relatedTerms": ["입면도", "단면도", "배치도", "평면계획"]
    },
    {
        "slug": "ban-ve-mat-dung",
        "korean": "입면도",
        "vietnamese": "Bản vẽ mặt đứng",
        "hanja": "立面圖",
        "hanjaReading": "立(설 립) + 面(낯 면) + 圖(그림 도)",
        "pronunciation": "반베맛중",
        "meaningKo": "건물의 외관을 정면, 측면, 후면 등 수직 방향에서 본 모습을 표현한 도면. 통역 시 주의할 점은 베트남어로 동·서·남·북 입면도를 'mặt đứng Đông/Tây/Nam/Bắc'로 표현하며, 한국의 '정면/배면' 개념과 다름. 실무에서 입면도는 외장재 선정과 직결되므로 재료 표기 오역 주의. 베트Nam 현장에서는 입면도에 색상 코드까지 명시하는 경우가 많음.",
        "meaningVi": "Bản vẽ thể hiện hình dáng bên ngoài của công trình khi nhìn từ các phía (Đông, Tây, Nam, Bắc). Thể hiện chiều cao, hình dáng mái, cửa sổ, vật liệu hoàn thiện. Là tài liệu quan trọng để kiểm soát mỹ quan và vật liệu ngoại thất.",
        "context": "외관 설계, 외장재 선정, 경관 심의",
        "culturalNote": "한국에서는 '정면도', '배면도' 표현이 일반적이지만, 베트남에서는 방위 기준 '동측입면도', '서측입면도' 표현이 공식적. 베트남 건축 심의에서는 입면도의 색상과 재질 표현을 한국보다 더 중시하며, 3D 렌더링과 입면도를 함께 제출하는 경우가 많음. 베트남 전통 건축의 경우 입면도에 장식 요소 표기가 매우 상세함.",
        "commonMistakes": [
            {
                "mistake": "mặt trước/mặt sau",
                "correction": "mặt đứng Đông/Tây/Nam/Bắc",
                "explanation": "방위 기준 명칭이 공식적"
            },
            {
                "mistake": "bản vẽ ngoại thất",
                "correction": "bản vẽ mặt đứng",
                "explanation": "ngoại thất은 외장 마감, mặt đứng은 입면 형태"
            },
            {
                "mistake": "'입면도 확인'을 'kiểm tra mặt ngoài'로 통역",
                "correction": "'kiểm tra bản vẽ mặt đứng'",
                "explanation": "mặt ngoài는 외부, 도면은 bản vẽ로 명확히"
            }
        ],
        "examples": [
            {
                "ko": "남측 입면도에 외장재 표기해 주세요.",
                "vi": "Vui lòng ghi rõ vật liệu ngoại thất trên bản vẽ mặt đứng Nam.",
                "situation": "formal"
            },
            {
                "ko": "입면도 색상 샘플 다시 보내주실 수 있나요?",
                "vi": "Bạn có thể gửi lại mẫu màu cho bản vẽ mặt đứng không?",
                "situation": "onsite"
            },
            {
                "ko": "입면도 심의 결과 창호 위치 수정 필요합니다.",
                "vi": "Kết quả thẩm định bản vẽ mặt đứng yêu cầu điều chỉnh vị trí cửa sổ.",
                "situation": "formal"
            }
        ],
        "relatedTerms": ["평면도", "단면도", "외관디자인", "외장재"]
    },
    {
        "slug": "ban-ve-mat-cat",
        "korean": "단면도",
        "vietnamese": "Bản vẽ mặt cắt",
        "hanja": "斷面圖",
        "hanjaReading": "斷(끊을 단) + 面(낯 면) + 圖(그림 도)",
        "pronunciation": "반베맛껏",
        "meaningKo": "건물을 수직으로 절단하여 내부 구조와 층고, 구조체를 표현한 도면. 통역 시 주의할 점은 베트남에서 'mặt cắt dọc'(종단면), 'mặt cắt ngang'(횡단면)을 명확히 구분하며, 한국의 '종단면도/횡단면도'와 대응. 실무에서 단면도는 층고, 천장고, 기초 깊이 등 수직 치수 확인의 핵심이므로 치수 단위(mm/cm) 혼동 절대 금지. 베트남 현장에서는 단면도에 구조 부재명까지 상세히 표기.",
        "meaningVi": "Bản vẽ thể hiện kết cấu bên trong khi cắt công trình theo phương thẳng đứng. Thể hiện chiều cao tầng, độ dày sàn, kết cấu móng, mái. Phân biệt 'mặt cắt dọc' (theo chiều dài) và 'mặt cắt ngang' (theo chiều rộng). Rất quan trọng để kiểm soát kết cấu và thi công.",
        "context": "구조 검토, 층고 확인, 기초 설계",
        "culturalNote": "한국에서는 단면도를 'A-A' 단면', 'B-B' 단면' 형식으로 표기하는데, 베트남에서도 동일하지만 'Mặt cắt A-A', 'Mặt cắt B-B'로 명시. 베트남 건축법상 단면도에는 지하층 깊이와 지하수위 표기가 필수이며, 한국보다 더 상세한 기초 정보 요구. 베트남 전통 건축의 경우 단면도에 지붕 구조가 매우 상세하게 표현됨.",
        "commonMistakes": [
            {
                "mistake": "bản vẽ cắt",
                "correction": "bản vẽ mặt cắt",
                "explanation": "'mặt cắt'이 정식 용어, 'cắt'만으로는 불완전"
            },
            {
                "mistake": "mặt cắt trên/dưới",
                "correction": "mặt cắt dọc/ngang",
                "explanation": "방향 구분은 dọc(종)/ngang(횡)"
            },
            {
                "mistake": "'단면도 층고'를 'chiều cao của mặt cắt'로 통역",
                "correction": "'chiều cao tầng trên bản vẽ mặt cắt'",
                "explanation": "층고는 chiều cao tầng, 단면도는 bản vẽ"
            }
        ],
        "examples": [
            {
                "ko": "A-A' 단면도에서 1층 층고 확인 부탁드립니다.",
                "vi": "Vui lòng kiểm tra chiều cao tầng 1 trên bản vẽ mặt cắt A-A'.",
                "situation": "formal"
            },
            {
                "ko": "단면도 보니까 기초 깊이가 너무 얕은 것 같아요.",
                "vi": "Xem bản vẽ mặt cắt thì độ sâu móng có vẻ quá nông.",
                "situation": "onsite"
            },
            {
                "ko": "횡단면도와 종단면도 둘 다 제출해야 합니다.",
                "vi": "Phải nộp cả bản vẽ mặt cắt ngang và mặt cắt dọc.",
                "situation": "formal"
            }
        ],
        "relatedTerms": ["평면도", "입면도", "구조도", "층고"]
    },
    {
        "slug": "ban-ve-chi-tiet",
        "korean": "상세도",
        "vietnamese": "Bản vẽ chi tiết",
        "hanja": "詳細圖",
        "hanjaReading": "詳(자세할 상) + 細(가늘 세) + 圖(그림 도)",
        "pronunciation": "반베찌띠엣",
        "meaningKo": "특정 부위나 접합부를 확대하여 시공 방법을 상세히 표현한 도면. 통역 시 'bản vẽ thi công chi tiết'(시공상세도)와 구분 주의 - 후자가 더 구체적. 실무에서 상세도는 창호, 방수, 단열 등 까다로운 부위의 시공 품질을 좌우하므로 축척과 치수 표기 오역 절대 금지. 베트남 현장에서는 상세도 없이 시공 불가능한 부위가 많아 한국보다 더 많은 상세도 요구.",
        "meaningVi": "Bản vẽ phóng to chi tiết một bộ phận cụ thể của công trình để chỉ dẫn thi công. Thường có tỷ lệ 1/5, 1/10, 1/20. Bao gồm chi tiết nút kết cấu, chi tiết cửa sổ, chi tiết chống thấm, v.v. Là tài liệu quan trọng để đảm bảo chất lượng thi công.",
        "context": "시공 지시, 품질 관리, 접합부 검토",
        "culturalNote": "한국에서는 상세도를 'detail drawing'으로 영어 병기하지만, 베트남에서는 'bản vẽ chi tiết' 표현이 더 공식적. 베트남 건축법상 상세도는 축척 1/5~1/20 기준이며, 한국보다 더 큰 축척(더 상세한) 도면 요구하는 경우 많음. 베트남 현장에서는 상세도에 시공 순서(bước thi công)까지 표기하는 경우가 많아 한국식 도면보다 설명이 많음.",
        "commonMistakes": [
            {
                "mistake": "bản vẽ nhỏ",
                "correction": "bản vẽ chi tiết",
                "explanation": "nhỏ는 작다는 뜻, chi tiết이 상세 표현"
            },
            {
                "mistake": "hình vẽ chi tiết",
                "correction": "bản vẽ chi tiết",
                "explanation": "정식 도면은 bản vẽ, hình vẽ는 그림"
            },
            {
                "mistake": "'창호 상세도'를 'chi tiết cửa sổ'만 통역",
                "correction": "'bản vẽ chi tiết cửa sổ'",
                "explanation": "도면임을 명확히 표현"
            }
        ],
        "examples": [
            {
                "ko": "발코니 방수 상세도 추가로 그려주세요.",
                "vi": "Vui lòng vẽ thêm bản vẽ chi tiết chống thấm ban công.",
                "situation": "formal"
            },
            {
                "ko": "이 접합부 상세도대로 시공했나요?",
                "vi": "Nút này thi công theo bản vẽ chi tiết chưa?",
                "situation": "onsite"
            },
            {
                "ko": "창호 상세도 축척이 1/10이 맞나요?",
                "vi": "Tỷ lệ bản vẽ chi tiết cửa sổ là 1/10 đúng không?",
                "situation": "formal"
            }
        ],
        "relatedTerms": ["평면도", "시공도", "접합부", "축척"]
    },
    {
        "slug": "ban-ve-ket-cau",
        "korean": "구조도",
        "vietnamese": "Bản vẽ kết cấu",
        "hanja": "構造圖",
        "hanjaReading": "構(얽을 구) + 造(지을 조) + 圖(그림 도)",
        "pronunciation": "반베껫꺼우",
        "meaningKo": "건물의 구조체(기둥, 보, 슬라브, 벽체 등)의 배치와 치수, 철근 배근을 표현한 도면. 통역 시 주의할 점은 베트남에서 'bản vẽ kết cấu'(구조도)와 'bản vẽ cốt thép'(배근도)를 구분하며, 후자가 더 구체적. 실무에서 구조도는 안전과 직결되므로 부재 치수, 철근 규격 등의 숫자 오역 절대 금지. 베트남 현장에서는 구조도에 구조 계산서 참조 번호까지 표기하는 경우가 많음.",
        "meaningVi": "Bản vẽ thể hiện hệ thống kết cấu chịu lực của công trình (cột, dầm, sàn, tường). Bao gồm vị trí, kích thước, cốt thép của các cấu kiện. Phân biệt 'bản vẽ kết cấu' (tổng thể) và 'bản vẽ cốt thép' (chi tiết thép). Là tài liệu quan trọng nhất về an toàn công trình.",
        "context": "구조 설계, 안전 검토, 철근 배근",
        "culturalNote": "한국에서는 구조도와 배근도를 묶어서 '구조도'로 부르는 경우 많지만, 베트남에서는 'bản vẽ kết cấu'(구조 배치)와 'bản vẽ cốt thép'(철근 상세)를 명확히 구분. 베트남 건축법상 구조도는 구조기술사 확인이 필수이며, 한국보다 더 엄격한 검토 절차. 베트남은 지진대가 아니므로 내진 설계보다 풍하중 검토가 더 중요.",
        "commonMistakes": [
            {
                "mistake": "bản vẽ xây dựng",
                "correction": "bản vẽ kết cấu",
                "explanation": "xây dựng은 건축 일반, kết cấu는 구조 특화"
            },
            {
                "mistake": "sơ đồ kết cấu",
                "correction": "bản vẽ kết cấu",
                "explanation": "sơ đồ는 개념도, bản vẽ는 정식 도면"
            },
            {
                "mistake": "'구조도 검토'를 'xem kết cấu'로 통역",
                "correction": "'kiểm tra bản vẽ kết cấu'",
                "explanation": "도면 검토는 kiểm tra bản vẽ로 명확히"
            }
        ],
        "examples": [
            {
                "ko": "구조도 구조기술사 확인 받으셨나요?",
                "vi": "Bản vẽ kết cấu đã được kỹ sư kết cấu xác nhận chưa?",
                "situation": "formal"
            },
            {
                "ko": "이 기둥 철근 배근이 구조도랑 다른데요?",
                "vi": "Cốt thép cột này khác với bản vẽ kết cấu nhỉ?",
                "situation": "onsite"
            },
            {
                "ko": "구조도 수정 후 재검토 요청드립니다.",
                "vi": "Sau khi sửa bản vẽ kết cấu, xin kiểm tra lại.",
                "situation": "formal"
            }
        ],
        "relatedTerms": ["배근도", "구조계산서", "기둥", "보"]
    },
    {
        "slug": "mo-hinh-thong-tin-cong-trinh-bim",
        "korean": "BIM",
        "vietnamese": "Mô hình thông tin công trình (BIM)",
        "hanja": None,
        "hanjaReading": None,
        "pronunciation": "모힌통띤꽁트잉",
        "meaningKo": "Building Information Modeling의 약자로, 건물의 3차원 형상에 속성 정보를 결합한 디지털 모델. 통역 시 주의할 점은 베트남에서 BIM을 '빔'이 아닌 'BIM'(비-아이-엠)으로 발음하며, 'mô hình thông tin công trình' 풀네임도 함께 사용. 실무에서 BIM은 설계·시공·유지관리 전 과정을 통합하는 개념이므로 단순 3D 모델링과 구분 필수. 베트남은 2020년부터 대형 공공공사에 BIM 의무화 추진 중.",
        "meaningVi": "Mô hình hóa thông tin công trình. Kết hợp hình dạng 3D với thông tin thuộc tính (vật liệu, chi phí, thời gian). Cho phép mô phỏng, phát hiện xung đột, quản lý tiến độ. Việt Nam đang dần áp dụng BIM cho các dự án lớn. Phân biệt BIM (tích hợp thông tin) với 3D đơn thuần (chỉ hình dạng).",
        "context": "설계 협업, 간섭 검토, 물량 산출",
        "culturalNote": "한국에서는 BIM을 '빔'으로 발음하지만, 베트남에서는 영어식 'B-I-M' 발음. 베트남 정부는 2020년 로드맵으로 대형 공공공사 BIM 의무화를 추진했으나, 실제 현장 적용률은 아직 낮은 편. 한국은 건축·토목 분야 BIM 활용이 높지만, 베트남은 건축 중심. 베트남 현장에서는 BIM 파일 포맷으로 IFC보다 Revit 네이티브 파일(.rvt) 선호하는 경향.",
        "commonMistakes": [
            {
                "mistake": "mô hình 3D",
                "correction": "mô hình BIM hoặc mô hình thông tin công trình",
                "explanation": "3D는 형상만, BIM은 정보 통합"
            },
            {
                "mistake": "'빔 모델'을 'mô hình BIM'만 통역",
                "correction": "'mô hình BIM (Building Information Modeling)'",
                "explanation": "처음 사용 시 풀네임 병기"
            },
            {
                "mistake": "bản vẽ BIM",
                "correction": "mô hình BIM",
                "explanation": "BIM은 모델(mô hình), 도면(bản vẽ)이 아님"
            }
        ],
        "examples": [
            {
                "ko": "이번 프로젝트는 BIM으로 진행합니다.",
                "vi": "Dự án này sẽ thực hiện bằng BIM (mô hình thông tin công trình).",
                "situation": "formal"
            },
            {
                "ko": "BIM 모델에서 설비 간섭 체크 부탁드려요.",
                "vi": "Vui lòng kiểm tra xung đột hệ thống M&E trên mô hình BIM.",
                "situation": "onsite"
            },
            {
                "ko": "BIM 파일 IFC 포맷으로 내보내기 해주세요.",
                "vi": "Vui lòng xuất file BIM sang định dạng IFC.",
                "situation": "formal"
            }
        ],
        "relatedTerms": ["3D모델링", "간섭검토", "LOD", "IFC"]
    },
    {
        "slug": "muc-do-chi-tiet-lod",
        "korean": "LOD",
        "vietnamese": "Mức độ chi tiết (LOD)",
        "hanja": None,
        "hanjaReading": None,
        "pronunciation": "뭉도찌띠엣",
        "meaningKo": "Level of Development 또는 Level of Detail의 약자로, BIM 모델의 상세 수준을 단계별로 정의한 기준. 통역 시 주의할 점은 베트Nam에서 LOD를 '엘오디'로 발음하며, 'mức độ chi tiết' 또는 'mức độ phát triển'으로 번역. 실무에서 LOD 100~500까지 단계가 있으며, 설계·시공 단계에 따라 요구 LOD 레벨이 다름. 베트남 BIM 가이드라인에서는 LOD 300을 시공도 기준으로 권장.",
        "meaningVi": "Mức độ chi tiết hoặc mức độ phát triển của mô hình BIM. Chia thành các cấp: LOD 100 (khái niệm), LOD 200 (sơ bộ), LOD 300 (thiết kế thi công), LOD 400 (gia công chế tạo), LOD 500 (竣工). Giúp xác định mức độ thông tin cần thiết ở từng giai đoạn dự án.",
        "context": "BIM 설계, 시공도 작성, 발주 요구사항",
        "culturalNote": "한국에서는 LOD를 '엘오디'로 발음하고, 베트남도 동일. 한국 BIM 기준은 LOD를 6단계(100/200/300/350/400/500)로 세분화하지만, 베트남은 5단계(100/200/300/400/500)가 일반적. 베트남 공공공사 발주 시 LOD 300 이상 요구하는 경우가 많으며, 한국보다 LOD 기준이 덜 세밀한 편. 베트남 현장에서는 'LOD bao nhiêu?'(LOD 몇?) 형태로 자주 질문.",
        "commonMistakes": [
            {
                "mistake": "mức độ 3D",
                "correction": "mức độ chi tiết (LOD)",
                "explanation": "3D는 차원, LOD는 상세 수준"
            },
            {
                "mistake": "'LOD 300'을 'mức 300'만 통역",
                "correction": "'LOD 300 (mức độ chi tiết 300)'",
                "explanation": "LOD 약어 유지하고 필요 시 풀네임 병기"
            },
            {
                "mistake": "độ chi tiết",
                "correction": "mức độ chi tiết",
                "explanation": "'mức độ'가 정식 표현"
            }
        ],
        "examples": [
            {
                "ko": "현재 BIM 모델이 LOD 몇 수준인가요?",
                "vi": "Mô hình BIM hiện tại ở mức LOD bao nhiêu?",
                "situation": "formal"
            },
            {
                "ko": "시공 단계에서는 LOD 300 이상 필요합니다.",
                "vi": "Giai đoạn thi công cần LOD 300 trở lên.",
                "situation": "onsite"
            },
            {
                "ko": "준공 BIM은 LOD 500으로 제출하세요.",
                "vi": "BIM竣工 nộp ở mức LOD 500.",
                "situation": "formal"
            }
        ],
        "relatedTerms": ["BIM", "3D모델링", "시공도", "준공도"]
    },
    {
        "slug": "quet-3d",
        "korean": "3D스캔",
        "vietnamese": "Quét 3D",
        "hanja": None,
        "hanjaReading": None,
        "pronunciation": "꿰뜨바데",
        "meaningKo": "레이저 스캐너나 포토그래메트리를 이용해 기존 건물이나 지형을 3차원 디지털 데이터로 변환하는 기술. 통역 시 주의할 점은 베트남에서 '3D 스캔'을 'quét 3D' 또는 'quét laser 3D'로 표현하며, 장비 종류에 따라 명칭이 달라짐. 실무에서 3D스캔은 리모델링, 준공도 작성, BIM 역설계에 활용되며, 정확도(mm 단위)와 스캔 밀도가 중요. 베트Nam에서는 드론 측량과 3D스캔을 함께 사용하는 추세.",
        "meaningVi": "Công nghệ chuyển đổi công trình hiện hữu hoặc địa hình thành dữ liệu 3D bằng máy quét laser hoặc photogrammetry. Kết quả là đám mây điểm (point cloud) có thể chuyển thành mô hình BIM. Ứng dụng trong cải tạo, lập竣工, kiểm tra thi công. Độ chính xác thường đạt ±5mm.",
        "context": "리모델링, 준공도, 현황 조사",
        "culturalNote": "한국에서는 '3D 스캐닝' 또는 '라이다 스캔'으로 부르는데, 베트남에서는 'quét 3D' 또는 'quét laser'가 더 일반적. 베트남 건설 현장에서는 3D스캔을 주로 대형 인프라 프로젝트나 문화재 보존에 사용하며, 일반 건축에서는 아직 보편화되지 않음. 베트남은 드론(UAV) 측량 규제가 엄격하여 3D스캔 작업 시 사전 허가 필요한 경우 많음.",
        "commonMistakes": [
            {
                "mistake": "chụp 3D",
                "correction": "quét 3D",
                "explanation": "chụp은 사진 촬영, quét은 스캔"
            },
            {
                "mistake": "'3D 스캔 데이터'를 'dữ liệu 3D'만 통역",
                "correction": "'dữ liệu quét 3D' 또는 'đám mây điểm'",
                "explanation": "스캔 결과는 point cloud(đám mây điểm)"
            },
            {
                "mistake": "scan 3D",
                "correction": "quét 3D",
                "explanation": "베트남어로 quét이 표준"
            }
        ],
        "examples": [
            {
                "ko": "기존 건물 3D스캔 후 BIM 모델 만들겠습니다.",
                "vi": "Sau khi quét 3D công trình hiện hữu, tôi sẽ tạo mô hình BIM.",
                "situation": "formal"
            },
            {
                "ko": "3D스캔 정확도가 ±5mm 이내인가요?",
                "vi": "Độ chính xác quét 3D trong ±5mm phải không?",
                "situation": "onsite"
            },
            {
                "ko": "드론으로 3D스캔 가능한가요?",
                "vi": "Có thể quét 3D bằng drone không?",
                "situation": "informal"
            }
        ],
        "relatedTerms": ["BIM", "포인트클라우드", "역설계", "드론측량"]
    },
    {
        "slug": "tinh-khoi-luong",
        "korean": "물량산출",
        "vietnamese": "Tính khối lượng",
        "hanja": "物量算出",
        "hanjaReading": "物(물건 물) + 量(헤아릴 량) + 算(셈 산) + 出(날 출)",
        "pronunciation": "띤코이르엉",
        "meaningKo": "설계도면을 기반으로 공사에 필요한 자재와 수량을 계산하는 작업. 통역 시 주의할 점은 베트남에서 'tính khối lượng'(물량계산)과 'lập dự toán'(견적 작성)을 구분하며, 전자는 순수 수량, 후자는 금액 포함. 실무에서 물량산출은 입찰, 발주, 원가 관리의 기초이므로 단위(m²/m³/개) 혼동 절대 금지. 베트남에서는 물량산출서를 'bảng tính khối lượng'으로 부르며, 한국의 '물량 내역서'와 대응.",
        "meaningVi": "Công việc tính toán số lượng vật liệu, khối lượng công việc dựa trên bản vẽ thiết kế. Bao gồm diện tích, thể tích, số lượng cấu kiện. Là cơ sở để lập dự toán, đấu thầu, quản lý nguyên vật liệu. Phân biệt 'tính khối lượng' (số lượng) và 'lập dự toán' (giá tiền).",
        "context": "입찰, 견적, 원가 관리",
        "culturalNote": "한국에서는 '물량산출'과 '내역 작성'을 구분하지만, 베트남에서는 'tính khối lượng'(물량 계산)과 'lập dự toán'(예산 수립)으로 명확히 분리. 베트남 건설 관행상 물량산출은 발주자 측에서 하는 경우가 많으며, 한국처럼 시공사가 자체 물량 산출하는 경우는 드물. 베트남은 물량 단위로 m², m³, tấn(톤)을 주로 사용하며, '식(式)' 개념은 없음.",
        "commonMistakes": [
            {
                "mistake": "tính toán vật liệu",
                "correction": "tính khối lượng",
                "explanation": "vật liệu는 자재, khối lượng이 물량"
            },
            {
                "mistake": "'물량 산출'을 'lập dự toán'로 통역",
                "correction": "'tính khối lượng'",
                "explanation": "dự toán은 견적(금액 포함), khối lượng은 수량만"
            },
            {
                "mistake": "đo lường",
                "correction": "tính khối lượng",
                "explanation": "đo lường은 측정, tính은 계산"
            }
        ],
        "examples": [
            {
                "ko": "콘크리트 물량산출 다시 확인해 주세요.",
                "vi": "Vui lòng kiểm tra lại tính khối lượng bê tông.",
                "situation": "formal"
            },
            {
                "ko": "BIM으로 물량산출하면 정확도가 높아요.",
                "vi": "Tính khối lượng bằng BIM thì độ chính xác cao hơn.",
                "situation": "onsite"
            },
            {
                "ko": "철근 물량산출서 내일까지 제출 바랍니다.",
                "vi": "Vui lòng nộp bảng tính khối lượng cốt thép trước ngày mai.",
                "situation": "formal"
            }
        ],
        "relatedTerms": ["내역서", "견적", "BIM", "원가관리"]
    },
    {
        "slug": "bang-du-toan",
        "korean": "내역서",
        "vietnamese": "Bảng dự toán",
        "hanja": "內譯書",
        "hanjaReading": "內(안 내) + 譯(풀 역) + 書(글 서)",
        "pronunciation": "방즈어또안",
        "meaningKo": "공사에 필요한 항목별 물량과 단가, 금액을 상세히 기재한 문서. 통역 시 주의할 점은 베트남에서 'bảng dự toán'(견적서/예산서)과 'bảng nội dung chi tiết'(상세내역)을 구분하며, 전자가 더 포괄적. 실무에서 내역서는 계약과 대금 지급의 근거이므로 품명, 단위, 수량, 단가 오역 절대 금지. 베트남 내역서는 한국과 달리 부가세(VAT 10%)를 별도 표기하며, 한국의 '일위대가표'에 해당하는 'đơn giá chi tiết' 개념도 있음.",
        "meaningVi": "Bảng chi tiết các hạng mục công việc, khối lượng, đơn giá, thành tiền của dự án. Là tài liệu pháp lý quan trọng trong hợp đồng xây dựng, làm cơ sở thanh toán, quyết toán. Phân biệt 'bảng dự toán tổng hợp' (tổng thể) và 'đơn giá chi tiết' (phân tích đơn giá).",
        "context": "입찰, 계약, 대금 지급",
        "culturalNote": "한국에서는 '내역서'를 '공사내역서', '품셈내역서'로 세분화하지만, 베트Nam에서는 'bảng dự toán'이 통칭. 베트남 건설 관행상 내역서에 VAT 10%를 별도 표기하며, 한국처럼 부가세 포함 금액으로 표기하지 않음. 베트남은 국가 정한 단가표(định mức)가 있어 공공공사는 이를 기준으로 하며, 한국의 '표준품셈'과 유사. 베트남 내역서는 Excel보다 전용 소프트웨어(Dự toán Xây dựng) 사용이 많음.",
        "commonMistakes": [
            {
                "mistake": "bảng giá",
                "correction": "bảng dự toán",
                "explanation": "bảng giá는 단순 가격표, dự toán은 견적 내역"
            },
            {
                "mistake": "'내역서 작성'을 'viết bảng'로 통역",
                "correction": "'lập bảng dự toán'",
                "explanation": "내역서 작성은 lập dự toán"
            },
            {
                "mistake": "chi tiết giá",
                "correction": "bảng dự toán chi tiết",
                "explanation": "정식 표현은 bảng dự toán"
            }
        ],
        "examples": [
            {
                "ko": "공사 내역서 검토 후 회신 부탁드립니다.",
                "vi": "Vui lòng xem xét bảng dự toán công trình và phản hồi.",
                "situation": "formal"
            },
            {
                "ko": "내역서에 부가세 포함인가요?",
                "vi": "Bảng dự toán đã bao gồm VAT chưa?",
                "situation": "onsite"
            },
            {
                "ko": "내역서 단가가 시장가보다 높은 것 같아요.",
                "vi": "Đơn giá trong bảng dự toán có vẻ cao hơn giá thị trường.",
                "situation": "informal"
            }
        ],
        "relatedTerms": ["물량산출", "견적서", "일위대가", "품셈"]
    }
]
