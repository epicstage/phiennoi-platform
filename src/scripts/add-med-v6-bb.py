#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
의료 용어 추가 스크립트 v6-bb: 진단검사/영상의학
테마: Diagnostic Tests/Radiology
"""

import json
import os

# 파일 경로 설정
file_path = os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', 'data', 'terms', 'medical.json')

# 새로운 용어 10개 (진단검사/영상의학)
new_terms = [
    {
        "slug": "chup-ct",
        "korean": "CT촬영",
        "vietnamese": "Chụp CT",
        "hanja": "CT撮影",
        "hanjaReading": "촬(찍을 촬) + 영(그림자 영)",
        "pronunciation": "씨티 촤령",
        "meaningKo": "X선을 이용하여 인체의 단면 영상을 촬영하는 검사 방법입니다. 컴퓨터 단층촬영(Computed Tomography)의 약자로, 뼈, 혈관, 연조직을 3차원으로 관찰할 수 있습니다. 통역 시 주의사항: '조영제 사용 여부'를 반드시 확인해야 하며, 베트남어로는 'Chụp CT có thuốc cản quang' 또는 'Chụp CT không thuốc'으로 구분합니다. 환자가 금식이 필요한지, 알레르기가 있는지 확인하는 것이 중요하며, '단순 CT'는 'CT thường', '조영 CT'는 'CT có thuốc'으로 번역합니다.",
        "meaningVi": "Phương pháp chụp hình cắt lớp cơ thể bằng tia X. CT (Computed Tomography) cho phép quan sát xương, mạch máu, mô mềm theo không gian 3 chiều. Có thể thực hiện với hoặc không có thuốc cản quang tùy mục đích chẩn đoán.",
        "context": "진단검사실, 영상의학과, 응급실",
        "culturalNote": "한국에서는 CT촬영이 비교적 빠르게 예약되고 시행되지만, 베트남에서는 대형 병원에서만 가능하고 비용이 높아 접근성이 제한적입니다. 한국은 건강보험 적용으로 본인부담이 적지만, 베트남은 전액 본인부담인 경우가 많습니다. 통역 시 '조영제 부작용'에 대한 설명이 중요하며, 베트남 환자들은 방사선 피폭에 대한 우려를 자주 표현하므로 안전성에 대한 설명도 필요합니다.",
        "commonMistakes": [
            {
                "mistake": "CT를 '씨티 검사'로만 번역",
                "correction": "'Chụp CT' 또는 'Chụp cắt lớp vi tính'",
                "explanation": "CT는 촬영(chụp)이므로 동사를 포함해야 자연스럽습니다."
            },
            {
                "mistake": "조영제를 '염료'로 번역",
                "correction": "'Thuốc cản quang' (조영제)",
                "explanation": "염료(thuốc nhuộm)와 조영제는 다른 개념입니다."
            },
            {
                "mistake": "'CT 찍는다'를 'Chụp ảnh CT'로 번역",
                "correction": "'Chụp CT' 또는 'Chụp phim CT'",
                "explanation": "ảnh는 일반 사진을 의미하므로 의료용어로 부적절합니다."
            }
        ],
        "examples": [
            {
                "ko": "복부 CT촬영을 하려면 6시간 금식이 필요합니다.",
                "vi": "Để chụp CT bụng cần nhịn ăn 6 tiếng.",
                "situation": "formal"
            },
            {
                "ko": "조영제 주사하고 CT 찍을게요. 알레르기 있으세요?",
                "vi": "Sẽ tiêm thuốc cản quang rồi chụp CT. Anh/chị có dị ứng không?",
                "situation": "onsite"
            },
            {
                "ko": "CT 결과 보니까 폐에 그림자가 보이네요.",
                "vi": "Xem kết quả CT thấy có bóng mờ ở phổi.",
                "situation": "informal"
            }
        ],
        "relatedTerms": ["MRI촬영", "조영제", "방사선검사", "영상의학과"]
    },
    {
        "slug": "chup-mri",
        "korean": "MRI촬영",
        "vietnamese": "Chụp MRI",
        "hanja": "MRI撮影",
        "hanjaReading": "촬(찍을 촬) + 영(그림자 영)",
        "pronunciation": "엠알아이 촤령",
        "meaningKo": "자기장과 전파를 이용하여 인체 내부의 단면 영상을 얻는 검사입니다. 자기공명영상(Magnetic Resonance Imaging)의 약자로, CT보다 연조직 대조도가 우수하여 뇌, 척추, 관절, 복부 장기 검사에 적합합니다. 통역 시 주의사항: 금속 삽입물(임플란트, 심박조율기 등)이 있는지 반드시 확인해야 하며, 베트nam어로는 'Kim loại trong cơ thể'로 설명합니다. 촬영 시간이 20-60분으로 길고, 폐쇄공포증이 있는 환자는 진정제가 필요할 수 있습니다. 'MRI 들어간다'는 'Vào chụp MRI'로 번역합니다.",
        "meaningVi": "Phương pháp chụp hình cắt lớp bằng từ trường và sóng radio. MRI (Magnetic Resonance Imaging) có độ tương phản mô mềm tốt hơn CT, thích hợp cho não, cột sống, khớp. Cần kiểm tra kim loại trong cơ thể trước khi chụp.",
        "context": "영상의학과, 신경외과, 정형외과",
        "culturalNote": "한국은 MRI 장비가 많아 예약이 비교적 쉽지만, 베트남은 대형 병원에서만 가능하고 비용이 매우 높습니다(500만-1000만 동). 베트남 환자들은 MRI의 '둥둥' 소리에 놀라는 경우가 많으므로, 사전에 '소음이 크다(ồn)'고 설명하는 것이 좋습니다. 한국은 귀마개를 제공하지만, 베트남은 시설에 따라 제공하지 않을 수도 있습니다. 폐쇄공포증(sợ không gian kín)이 있는 환자를 위한 개방형 MRI는 베트남에 거의 없습니다.",
        "commonMistakes": [
            {
                "mistake": "MRI를 'X-ray 촬영'의 일종으로 설명",
                "correction": "자기장 이용, 방사선 없음을 강조",
                "explanation": "MRI는 방사선을 사용하지 않으므로 X-ray와 구분해야 합니다."
            },
            {
                "mistake": "'금속 제거'를 'Tháo kim loại'로만 번역",
                "correction": "'Tháo đồ kim loại' (액세서리) vs 'Kim loại cấy trong người' (임플란트)",
                "explanation": "착용한 금속과 체내 금속을 구분해야 합니다."
            },
            {
                "mistake": "촬영 시간을 '잠깐'으로 설명",
                "correction": "20-60분 소요를 정확히 알려야 함",
                "explanation": "환자가 긴 촬영 시간을 예상하지 못하면 중간에 움직일 수 있습니다."
            }
        ],
        "examples": [
            {
                "ko": "뇌 MRI촬영 전에 금속 액세서리를 모두 빼주세요.",
                "vi": "Trước khi chụp MRI não, vui lòng tháo hết đồ kim loại.",
                "situation": "formal"
            },
            {
                "ko": "MRI 기계 안에서 소리가 크니까 귀마개 끼고 계세요.",
                "vi": "Trong máy MRI sẽ ồn nên đeo nút tai vào nhé.",
                "situation": "onsite"
            },
            {
                "ko": "심장 박동기 있으면 MRI 못 찍어요.",
                "vi": "Nếu có máy tạo nhịp tim thì không thể chụp MRI.",
                "situation": "informal"
            }
        ],
        "relatedTerms": ["CT촬영", "조영제", "자기공명영상", "방사선검사"]
    },
    {
        "slug": "sieu-am",
        "korean": "초음파검사",
        "vietnamese": "Siêu âm",
        "hanja": "超音波檢査",
        "hanjaReading": "초(넘을 초) + 음(소리 음) + 파(물결 파) + 검(검사할 검) + 사(살필 사)",
        "pronunciation": "초음파 검사",
        "meaningKo": "인체에 무해한 고주파 음파를 이용하여 내부 장기나 태아의 상태를 실시간으로 관찰하는 검사입니다. 방사선 피폭이 없어 임산부와 영유아에게 안전하며, 복부, 심장, 갑상선, 유방, 산부인과 검사에 널리 사용됩니다. 통역 시 주의사항: '젤을 바른다'는 'Bôi gel'로 표현하며, 검사 부위에 따라 '경복부(qua bụng)', '경질(qua âm đạo)' 등을 명확히 구분해야 합니다. 임신 초음파는 'Siêu âm thai', 심장 초음파는 'Siêu âm tim'으로 세부 용어를 사용합니다.",
        "meaningVi": "Phương pháp kiểm tra sử dụng sóng âm tần số cao để quan sát cơ quan nội tạng hoặc thai nhi theo thời gian thực. Không có phóng xạ nên an toàn cho bà bầu và trẻ em. Thường dùng cho bụng, tim, tuyến giáp, vú, sản phụ khoa.",
        "context": "산부인과, 내과, 소화기내과, 건강검진센터",
        "culturalNote": "한국에서는 초음파검사가 매우 보편적이며 건강검진에도 포함되지만, 베트남에서는 임신 확인과 복부 검사 위주로 활용되고 심장·갑상선 초음파는 덜 보편적입니다. 한국은 3D/4D 초음파가 일반화되어 태아 얼굴을 선명하게 볼 수 있지만, 베트남은 2D 초음파가 주류입니다. 베트남 여성들은 경질 초음파(siêu âm đầu dò âm đạo)에 대한 거부감이 있을 수 있으므로, 검사 목적과 필요성을 충분히 설명해야 합니다.",
        "commonMistakes": [
            {
                "mistake": "'초음파'를 'Âm thanh siêu cao'로 번역",
                "correction": "'Siêu âm' (의료 용어)",
                "explanation": "초음파는 의학 검사를 의미하는 고정된 용어입니다."
            },
            {
                "mistake": "모든 초음파를 'Siêu âm bụng'으로 통칭",
                "correction": "부위별로 'Siêu âm tim', 'Siêu âm tuyến giáp' 등 구분",
                "explanation": "검사 부위를 명확히 해야 환자가 이해합니다."
            },
            {
                "mistake": "젤을 '기름(dầu)'으로 번역",
                "correction": "'Gel siêu âm' 또는 'Gel'",
                "explanation": "초음파 젤은 수용성이므로 기름과 다릅니다."
            }
        ],
        "examples": [
            {
                "ko": "복부 초음파검사를 위해 물을 많이 마시고 소변을 참아주세요.",
                "vi": "Để siêu âm bụng, vui lòng uống nhiều nước và nhịn tiểu.",
                "situation": "formal"
            },
            {
                "ko": "배에 젤 바르고 초음파 볼게요. 차가울 수 있어요.",
                "vi": "Sẽ bôi gel lên bụng rồi siêu âm nhé. Có thể hơi lạnh đấy.",
                "situation": "onsite"
            },
            {
                "ko": "임신 12주차인데 초음파 보니까 아기 심장 뛰는 게 보여요.",
                "vi": "Thai 12 tuần rồi, siêu âm thấy tim bé đập rồi.",
                "situation": "informal"
            }
        ],
        "relatedTerms": ["산전검사", "태아", "복부검사", "심장초음파"]
    },
    {
        "slug": "chup-pet-ct",
        "korean": "PET-CT",
        "vietnamese": "Chụp PET-CT",
        "hanja": None,
        "hanjaReading": None,
        "pronunciation": "펫씨티",
        "meaningKo": "양전자방출단층촬영(PET)과 컴퓨터단층촬영(CT)을 결합한 첨단 영상검사로, 암의 진단, 병기 결정, 치료 효과 판정, 재발 감시에 사용됩니다. 방사성 동위원소(주로 FDG)를 주사한 후 암세포의 대사 활동을 영상화하여, 전신의 암 전이 여부를 한 번에 확인할 수 있습니다. 통역 시 주의사항: 검사 전 최소 6시간 금식이 필수이며, 당뇨병 환자는 혈당 조절 상태를 확인해야 합니다. '방사성 물질 주사'는 'Tiêm chất phóng xạ'로 번역하되, 환자의 불안을 최소화하도록 안전성을 강조해야 합니다. 검사 후 2-3시간은 임산부와 영유아 접촉을 피해야 한다는 점도 설명이 필요합니다.",
        "meaningVi": "Phương pháp chẩn đoán hình ảnh tiên tiến kết hợp PET (chụp cắt lớp phát xạ positron) và CT, dùng để chẩn đoán ung thư, xác định giai đoạn bệnh, đánh giá hiệu quả điều trị và theo dõi tái phát. Tiêm chất phóng xạ FDG rồi chụp hình hoạt động chuyển hóa của tế bào ung thư trên toàn cơ thể.",
        "context": "핵의학과, 종양내과, 암센터",
        "culturalNote": "한국은 PET-CT가 보편화되어 있고 일부 건강보험이 적용되지만, 베트남에서는 극소수 대형 병원에서만 가능하고 비용이 매우 고가(2000만-3000만 동)입니다. 베트남 환자들은 '방사성 물질 주사'에 대한 두려움이 크므로, 안전성과 필요성을 충분히 설명해야 합니다. 한국은 PET-CT 검사 당일 귀가가 가능하지만, 베트남에서는 시설에 따라 하루 입원이 필요할 수도 있습니다. 검사 후 수분 섭취를 많이 하라는 지침이 중요합니다.",
        "commonMistakes": [
            {
                "mistake": "PET-CT를 일반 CT로 설명",
                "correction": "암 전이 검사용 특수 검사임을 명확히",
                "explanation": "PET-CT는 대사 영상까지 포함하는 고급 검사입니다."
            },
            {
                "mistake": "'방사성 물질'을 '위험한 독'으로 오해하게 번역",
                "correction": "'Chất phóng xạ an toàn, liều thấp' 강조",
                "explanation": "환자의 불필요한 공포를 방지해야 합니다."
            },
            {
                "mistake": "금식 시간을 '아침 안 먹기'로 애매하게 설명",
                "correction": "'Nhịn ăn tối thiểu 6 tiếng' 정확히 명시",
                "explanation": "금식 시간이 부족하면 검사 결과가 부정확합니다."
            }
        ],
        "examples": [
            {
                "ko": "암 전이 여부 확인을 위해 PET-CT 검사가 필요합니다.",
                "vi": "Để kiểm tra di căn ung thư, cần chụp PET-CT.",
                "situation": "formal"
            },
            {
                "ko": "방사성 물질 주사하고 1시간 후에 촬영할게요. 조용히 누워 계세요.",
                "vi": "Sau khi tiêm chất phóng xạ 1 tiếng sẽ chụp. Anh/chị nằm yên nhé.",
                "situation": "onsite"
            },
            {
                "ko": "PET-CT 찍고 나서 오늘은 애기랑 떨어져 자야 돼요.",
                "vi": "Sau khi chụp PET-CT hôm nay phải ngủ xa bé.",
                "situation": "informal"
            }
        ],
        "relatedTerms": ["CT촬영", "암진단", "종양표지자", "핵의학검사"]
    },
    {
        "slug": "xet-nghiem-mau",
        "korean": "혈액검사",
        "vietnamese": "Xét nghiệm máu",
        "hanja": "血液檢査",
        "hanjaReading": "혈(피 혈) + 액(진 액) + 검(검사할 검) + 사(살필 사)",
        "pronunciation": "혀렉 검사",
        "meaningKo": "혈액을 채취하여 각종 질병의 진단, 건강 상태 평가, 치료 효과 모니터링을 위해 시행하는 기본적인 검사입니다. 일반혈액검사(CBC), 간기능검사(LFT), 신장기능검사, 혈당, 지질검사 등 다양한 항목이 포함됩니다. 통역 시 주의사항: '공복 채혈'은 'Lấy máu đói' 또는 'Lấy máu lúc đói bụng'으로 표현하며, 최소 8시간 금식이 필요함을 명확히 해야 합니다. 검사 항목별로 '간 수치(chỉ số gan)', '신장 수치(chỉ số thận)', '혈당(đường huyết)' 등 구체적인 용어를 사용하는 것이 중요합니다.",
        "meaningVi": "Xét nghiệm lấy máu để chẩn đoán bệnh, đánh giá sức khỏe, theo dõi hiệu quả điều trị. Bao gồm nhiều hạng mục như xét nghiệm máu toàn bộ (CBC), chức năng gan (LFT), chức năng thận, đường huyết, lipid máu.",
        "context": "건강검진센터, 내과, 응급실, 모든 진료과",
        "culturalNote": "한국은 혈액검사가 매우 보편적이고 빠르게 결과가 나오지만(당일-익일), 베트남에서는 기본 항목 외 특수 검사는 시간이 오래 걸릴 수 있습니다(2-7일). 한국은 자동화 장비로 대량 검사가 가능하지만, 베트남 중소 병원은 수작업 검사가 많아 정확도 편차가 있을 수 있습니다. 베트남 환자들은 '피를 많이 뽑으면 몸이 약해진다'는 인식이 있어, 여러 튜브를 채혈할 때 이유를 설명하는 것이 좋습니다. 공복 검사의 중요성에 대한 인식도 낮으므로 강조가 필요합니다.",
        "commonMistakes": [
            {
                "mistake": "'채혈'을 'Lấy huyết' (문어체)로만 번역",
                "correction": "'Lấy máu' (구어체, 일반적)",
                "explanation": "환자와 소통 시 일상 용어가 더 적합합니다."
            },
            {
                "mistake": "'공복'을 'Bụng rỗng'로 번역",
                "correction": "'Đói bụng' 또는 'Nhịn ăn'",
                "explanation": "Bụng rỗng은 비속어적 표현이므로 부적절합니다."
            },
            {
                "mistake": "검사 항목을 통칭으로만 설명",
                "correction": "간, 신장, 혈당 등 구체적 항목 명시",
                "explanation": "환자가 무엇을 검사하는지 알아야 협조가 잘 됩니다."
            }
        ],
        "examples": [
            {
                "ko": "내일 오전 8시에 공복 혈액검사 하러 오세요.",
                "vi": "Ngày mai 8 giờ sáng đến lấy máu lúc đói.",
                "situation": "formal"
            },
            {
                "ko": "팔 좀 펴고 주먹 쥐세요. 피 뽑을게요.",
                "vi": "Duỗi tay và nắm chặt tay lại. Sẽ lấy máu nhé.",
                "situation": "onsite"
            },
            {
                "ko": "간 수치가 높게 나왔네요. 술 좀 줄이셔야겠어요.",
                "vi": "Chỉ số gan cao đấy. Phải giảm rượu thôi.",
                "situation": "informal"
            }
        ],
        "relatedTerms": ["공복채혈", "간기능검사", "혈당", "건강검진"]
    },
    {
        "slug": "xet-nghiem-nuoc-tieu",
        "korean": "소변검사",
        "vietnamese": "Xét nghiệm nước tiểu",
        "hanja": "小便檢査",
        "hanjaReading": "소(작을 소) + 변(변할 변) + 검(검사할 검) + 사(살필 사)",
        "pronunciation": "소변 검사",
        "meaningKo": "소변을 채취하여 신장 질환, 요로 감염, 당뇨병, 임신 등을 진단하는 기본적인 검사입니다. 소변의 색깔, pH, 비중, 단백질, 당, 적혈구, 백혈구, 세균 등을 분석합니다. 통역 시 주의사항: '중간뇨'는 'Nước tiểu giữa dòng'으로 표현하며, 처음과 끝 소변을 버리고 중간 부분만 받는 방법을 설명해야 합니다. 여성 환자의 경우 생리 중에는 결과가 부정확할 수 있으므로 'Đang có kinh nguyệt'인지 확인이 필요합니다. 소변 용기는 'Hộp đựng nước tiểu' 또는 'Cốc xét nghiệm'으로 번역합니다.",
        "meaningVi": "Xét nghiệm lấy nước tiểu để chẩn đoán bệnh thận, nhiễm trùng đường tiết niệu, tiểu đường, thai nghén. Phân tích màu sắc, pH, tỷ trọng, protein, đường, hồng cầu, bạch cầu, vi khuẩn trong nước tiểu.",
        "context": "비뇨기과, 내과, 산부인과, 건강검진센터",
        "culturalNote": "한국은 소변검사가 건강검진의 기본 항목이며 자동화 분석 장비로 빠르게 결과가 나오지만, 베트남에서는 현미경 육안 검사가 많아 시간이 걸릴 수 있습니다. 한국은 1회용 소변 채취 용기를 제공하지만, 베트남 중소 병원은 환자가 깨끗한 용기를 준비해야 할 수도 있습니다. 베트남 문화상 소변 이야기를 공개적으로 하는 것에 거부감이 있을 수 있으므로, 은밀하게 설명하는 배려가 필요합니다. '중간뇨' 채취 방법에 대한 인식이 낮아 자세한 설명이 중요합니다.",
        "commonMistakes": [
            {
                "mistake": "'소변'을 'Nước tiểu' 대신 'Nước đái'로 번역",
                "correction": "'Nước tiểu' (의학 용어)",
                "explanation": "Nước đái는 구어체이지만 의료 현장에서는 부적절합니다."
            },
            {
                "mistake": "'중간뇨'를 '소변 중간'으로 애매하게 설명",
                "correction": "'Nước tiểu giữa dòng' + 채취 방법 상세 설명",
                "explanation": "환자가 정확한 방법을 모르면 검사가 무의미합니다."
            },
            {
                "mistake": "검사 용기를 '컵(cốc)'으로만 설명",
                "correction": "'Hộp xét nghiệm nước tiểu' 또는 '멸균 용기'",
                "explanation": "일반 컵 사용 시 오염 가능성이 있습니다."
            }
        ],
        "examples": [
            {
                "ko": "소변검사를 위해 중간뇨를 받아주세요.",
                "vi": "Để xét nghiệm, vui lòng lấy nước tiểu giữa dòng.",
                "situation": "formal"
            },
            {
                "ko": "처음 소변은 버리고, 중간 부분만 컵에 받으세요.",
                "vi": "Nước tiểu đầu tiên bỏ đi, chỉ lấy phần giữa vào cốc thôi.",
                "situation": "onsite"
            },
            {
                "ko": "소변에 단백질이 나왔어요. 신장 검사 더 해야 돼요.",
                "vi": "Nước tiểu có protein. Phải xét nghiệm thận thêm.",
                "situation": "informal"
            }
        ],
        "relatedTerms": ["요로감염", "단백뇨", "혈뇨", "신장검사"]
    },
    {
        "slug": "dien-tam-do",
        "korean": "심전도검사",
        "vietnamese": "Điện tâm đồ",
        "hanja": "心電圖檢査",
        "hanjaReading": "심(마음 심) + 전(번개 전) + 도(그림 도) + 검(검사할 검) + 사(살필 사)",
        "pronunciation": "심전도 검사",
        "meaningKo": "심장의 전기적 활동을 기록하여 심장 질환을 진단하는 검사입니다. 부정맥, 심근경색, 협심증, 심장비대 등을 감지할 수 있습니다. 가슴, 팔, 다리에 전극을 부착하여 심장 박동의 리듬과 속도, 전기 신호의 강도를 측정합니다. 통역 시 주의사항: '전극 부착'은 'Dán điện cực'로 표현하며, 피부와의 접촉을 위해 젤을 바르거나 털을 제거할 수 있음을 설명해야 합니다. 검사 중 움직이거나 말하면 결과가 부정확하므로 '가만히 누워 있어야 한다(nằm yên)'는 점을 강조합니다. 약어 ECG 또는 EKG로도 불립니다.",
        "meaningVi": "Xét nghiệm ghi nhận hoạt động điện của tim để chẩn đoán bệnh tim. Có thể phát hiện rối loạn nhịp tim, nhồi máu cơ tim, đau thắt ngực, phì đại tim. Dán điện cực lên ngực, tay, chân để đo nhịp tim, tốc độ và cường độ tín hiệu điện.",
        "context": "순환기내과, 응급실, 건강검진센터, 수술 전 검사",
        "culturalNote": "한국은 심전도검사가 건강검진 기본 항목이며 모든 병원에서 가능하지만, 베트남에서는 중급 이상 병원에서만 가능합니다. 한국은 자동 판독 시스템이 있지만, 베트남은 의사의 육안 판독에 의존하는 경우가 많습니다. 베트남 남성들은 가슴 털을 제거하는 것에 대한 거부감이 있을 수 있으므로, 전극 부착을 위해 필요하다는 설명이 중요합니다. 심전도 용지의 파형을 환자에게 보여주며 설명하면 이해도가 높아집니다.",
        "commonMistakes": [
            {
                "mistake": "'심전도'를 'Tim điện' 또는 'Đồ điện tim'으로 번역",
                "correction": "'Điện tâm đồ' (표준 의학 용어)",
                "explanation": "ECG/EKG의 공식 베트남어 명칭입니다."
            },
            {
                "mistake": "전극을 '전기 충격기'로 오해하게 설명",
                "correction": "'Điện cực chỉ đo, không gây đau' 강조",
                "explanation": "환자가 전기 충격을 두려워할 수 있습니다."
            },
            {
                "mistake": "검사 시간을 말하지 않고 진행",
                "correction": "'5-10분 소요' 사전 고지",
                "explanation": "환자가 시간을 알면 협조가 더 잘 됩니다."
            }
        ],
        "examples": [
            {
                "ko": "심전도검사를 위해 상의를 벗고 침대에 누워주세요.",
                "vi": "Để làm điện tâm đồ, vui lòng cởi áo và nằm lên giường.",
                "situation": "formal"
            },
            {
                "ko": "전극 붙이고 5분만 가만히 계세요. 아프지 않아요.",
                "vi": "Dán điện cực xong nằm yên 5 phút thôi. Không đau đâu.",
                "situation": "onsite"
            },
            {
                "ko": "심전도 보니까 부정맥이 있네요. 심장내과 가보세요.",
                "vi": "Điện tâm đồ thấy rối loạn nhịp tim. Nên đi khám tim mạch.",
                "situation": "informal"
            }
        ],
        "relatedTerms": ["부정맥", "심근경색", "심장내과", "응급검사"]
    },
    {
        "slug": "do-mat-do-xuong",
        "korean": "골밀도검사",
        "vietnamese": "Đo mật độ xương",
        "hanja": "骨密度檢査",
        "hanjaReading": "골(뼈 골) + 밀(빽빽할 밀) + 도(법도 도) + 검(검사할 검) + 사(살필 사)",
        "pronunciation": "골밀도 검사",
        "meaningKo": "뼈의 강도와 밀도를 측정하여 골다공증을 진단하고 골절 위험도를 평가하는 검사입니다. 주로 이중에너지 X선 흡수계측법(DEXA 또는 DXA)을 사용하며, 요추와 대퇴골을 측정합니다. T-score와 Z-score로 결과를 표현합니다. 통역 시 주의사항: '골다공증'은 'Loãng xương'으로 번역하며, 폐경 후 여성과 노인에게 중요한 검사임을 설명합니다. T-score -2.5 이하면 골다공증으로 진단되며, -1.0~-2.5는 '골감소증(giảm mật độ xương)'입니다. 칼슘 보충과 운동의 필요성도 함께 설명하는 것이 좋습니다.",
        "meaningVi": "Xét nghiệm đo độ chắc và mật độ của xương để chẩn đoán loãng xương và đánh giá nguy cơ gãy xương. Chủ yếu dùng phương pháp DEXA/DXA, đo cột sống thắt lưng và xương đùi. Kết quả biểu thị bằng T-score và Z-score.",
        "context": "정형외과, 내분비내과, 재활의학과, 갱년기클리닉",
        "culturalNote": "한국은 50세 이상 여성에게 골밀도검사가 권장되며 건강보험이 적용되지만, 베트남에서는 대형 병원에서만 가능하고 비용이 비쌉니다. 베트남 여성들은 골다공증에 대한 인식이 낮아, 폐경 후에도 검사를 받지 않는 경우가 많습니다. 한국은 칼슘 보충제와 골다공증 약물이 보편화되어 있지만, 베트남에서는 접근성이 낮습니다. 베트남 식단은 우유 섭취가 적어 칼슘 부족이 흔하므로, 영양 상담도 함께 제공하는 것이 중요합니다.",
        "commonMistakes": [
            {
                "mistake": "'골밀도'를 'Độ dày xương'(뼈 두께)로 번역",
                "correction": "'Mật độ xương' (뼈 밀도)",
                "explanation": "두께와 밀도는 다른 개념입니다."
            },
            {
                "mistake": "'골다공증'을 'Xương rỗng'으로 번역",
                "correction": "'Loãng xương' (의학 용어)",
                "explanation": "Xương rỗng은 구어체로 부정확합니다."
            },
            {
                "mistake": "T-score 수치만 말하고 의미 설명 생략",
                "correction": "정상/골감소/골다공증 단계 함께 설명",
                "explanation": "숫자만으로는 환자가 심각성을 이해하기 어렵습니다."
            }
        ],
        "examples": [
            {
                "ko": "폐경 후 골다공증 검사를 위해 골밀도검사를 권장합니다.",
                "vi": "Sau mãn kinh nên đo mật độ xương để kiểm tra loãng xương.",
                "situation": "formal"
            },
            {
                "ko": "허리하고 엉덩이뼈 찍을게요. 누워만 있으면 돼요.",
                "vi": "Sẽ chụp xương lưng và xương hông. Chỉ cần nằm yên thôi.",
                "situation": "onsite"
            },
            {
                "ko": "골밀도가 많이 낮아졌네요. 칼슘약 드셔야겠어요.",
                "vi": "Mật độ xương giảm nhiều rồi. Phải uống thuốc canxi đấy.",
                "situation": "informal"
            }
        ],
        "relatedTerms": ["골다공증", "골절", "칼슘보충제", "폐경"]
    },
    {
        "slug": "xet-nghiem-gen",
        "korean": "유전자검사",
        "vietnamese": "Xét nghiệm gen",
        "hanja": "遺傳子檢査",
        "hanjaReading": "유(남길 유) + 전(전할 전) + 자(아들 자) + 검(검사할 검) + 사(살필 사)",
        "pronunciation": "유전자 검사",
        "meaningKo": "DNA를 분석하여 유전 질환, 암 발생 위험도, 약물 반응성, 친자 확인 등을 알아내는 검사입니다. 혈액, 타액, 구강 점막 세포 등을 채취하여 분석하며, 결과가 나오기까지 수 주가 걸릴 수 있습니다. 통역 시 주의사항: 유전자검사는 개인의 프라이버시와 윤리적 문제가 관련되어 있으므로, 결과의 비밀 보장과 사용 목적을 명확히 설명해야 합니다. '유전자 변이(đột biến gen)', '가족력(tiền sử gia đình)' 등의 용어를 정확히 사용하고, 검사 결과가 '확률(xác suất)'이지 '확정(chắc chắn)'이 아님을 강조해야 합니다. 유전 상담의 중요성도 함께 설명합니다.",
        "meaningVi": "Xét nghiệm phân tích DNA để tìm hiểu bệnh di truyền, nguy cơ ung thư, phản ứng thuốc, xác định huyết thống. Lấy mẫu máu, nước bọt, tế bào niêm mạc miệng để phân tích, kết quả có thể mất vài tuần.",
        "context": "유전학과, 종양내과, 산부인과, 소아과",
        "culturalNote": "한국은 유전자검사가 빠르게 보편화되고 있으며, 암 유전자검사(BRCA 등)는 건강보험이 적용되지만, 베트남에서는 극소수 대형 병원에서만 가능하고 비용이 매우 고가입니다. 베트남에서는 유전자검사에 대한 인식이 낮고, '운명론적' 사고로 인해 결과를 받아들이기 어려워하는 경우가 있습니다. 한국은 유전 상담사 제도가 있지만, 베트남에는 없어 의사가 직접 설명해야 합니다. 가족에게 검사 결과를 공개할지 여부는 문화적으로 민감한 문제이므로 신중한 접근이 필요합니다.",
        "commonMistakes": [
            {
                "mistake": "'유전자'를 'Di truyền'으로만 번역",
                "correction": "'Gen' 또는 'Xét nghiệm gen'",
                "explanation": "Gen이 더 구체적이고 의학적인 용어입니다."
            },
            {
                "mistake": "검사 결과를 '100% 확실'로 설명",
                "correction": "'Xác suất' (확률) 개념 강조",
                "explanation": "유전자검사는 위험도를 알려주는 것이지 확정 진단이 아닙니다."
            },
            {
                "mistake": "가족력 조사를 생략하고 검사만 진행",
                "correction": "'Tiền sử gia đình' 상세히 확인",
                "explanation": "가족력이 검사 해석에 중요합니다."
            }
        ],
        "examples": [
            {
                "ko": "유방암 가족력이 있으면 BRCA 유전자검사를 고려해보세요.",
                "vi": "Nếu có tiền sử ung thư vú trong gia đình, nên cân nhắc xét nghiệm gen BRCA.",
                "situation": "formal"
            },
            {
                "ko": "입안쪽을 면봉으로 긁어서 세포 채취할게요.",
                "vi": "Sẽ dùng que bông lấy tế bào trong má nhé.",
                "situation": "onsite"
            },
            {
                "ko": "유전자검사 결과 나오려면 3주 걸려요.",
                "vi": "Kết quả xét nghiệm gen phải đợi 3 tuần.",
                "situation": "informal"
            }
        ],
        "relatedTerms": ["유전질환", "가족력", "암유전자", "유전상담"]
    },
    {
        "slug": "thuoc-can-quang",
        "korean": "조영제",
        "vietnamese": "Thuốc cản quang",
        "hanja": "造影劑",
        "hanjaReading": "조(만들 조) + 영(그림자 영) + 제(약제 제)",
        "pronunciation": "조영제",
        "meaningKo": "CT, MRI, 혈관조영술 등의 영상검사에서 특정 장기나 혈관을 더 선명하게 보이게 하기 위해 체내에 주입하는 약물입니다. 요오드 조영제(CT용)와 가돌리늄 조영제(MRI용)가 주로 사용됩니다. 통역 시 주의사항: 조영제 투여 전 반드시 알레르기 병력, 신장 기능, 천식, 갑상선 질환 여부를 확인해야 합니다. '조영제 부작용'은 'Tác dụng phụ của thuốc cản quang'으로 번역하며, 구토, 두드러기, 호흡곤란 등의 증상이 나타날 수 있음을 설명합니다. 검사 후 수분을 많이 섭취하여 조영제 배출을 돕도록 안내합니다.",
        "meaningVi": "Thuốc tiêm vào cơ thể để làm rõ các cơ quan hoặc mạch máu trong các xét nghiệm hình ảnh như CT, MRI, chụp mạch máu. Chủ yếu dùng thuốc cản quang iod (cho CT) và gadolinium (cho MRI).",
        "context": "영상의학과, 심혈관센터, 응급실",
        "culturalNote": "한국은 조영제 투여 전 알레르기 테스트와 동의서 작성이 철저하지만, 베트남에서는 절차가 간소화되어 있어 부작용 발생 시 대응이 늦을 수 있습니다. 베트남 환자들은 '약물 주사'에 대한 막연한 두려움이 있으므로, 안전성과 필요성을 충분히 설명해야 합니다. 한국은 조영제 부작용 발생 시 즉시 대응팀이 있지만, 베트남 중소 병원은 응급 장비가 부족할 수 있습니다. 신장 기능이 나쁜 환자는 조영제 배출이 어려우므로 사전 검사가 필수입니다.",
        "commonMistakes": [
            {
                "mistake": "'조영제'를 'Thuốc nhuộm'(염료)로 번역",
                "correction": "'Thuốc cản quang' (조영제)",
                "explanation": "염료와 조영제는 다른 물질입니다."
            },
            {
                "mistake": "알레르기 확인 없이 바로 주사",
                "correction": "'Có dị ứng thuốc không?' 반드시 확인",
                "explanation": "아나필락시스 쇼크로 생명이 위험할 수 있습니다."
            },
            {
                "mistake": "검사 후 수분 섭취 안내 생략",
                "correction": "'Uống nhiều nước sau khi chụp' 필수 안내",
                "explanation": "조영제 배출을 돕고 신장 부담을 줄입니다."
            }
        ],
        "examples": [
            {
                "ko": "조영제를 주사한 후 CT촬영을 시작하겠습니다. 알레르기가 있으신가요?",
                "vi": "Sau khi tiêm thuốc cản quang sẽ bắt đầu chụp CT. Anh/chị có dị ứng không?",
                "situation": "formal"
            },
            {
                "ko": "조영제 들어가면 몸이 뜨끈해지는 느낌 있을 수 있어요.",
                "vi": "Khi thuốc vào có thể cảm thấy nóng người đấy.",
                "situation": "onsite"
            },
            {
                "ko": "조영제 빼려면 물 많이 마셔야 돼요.",
                "vi": "Để thuốc cản quang thoát ra phải uống nhiều nước.",
                "situation": "informal"
            }
        ],
        "relatedTerms": ["CT촬영", "MRI촬영", "알레르기", "신장기능검사"]
    }
]

# 파일 읽기
with open(file_path, 'r', encoding='utf-8') as f:
    data = f.read()
    # 빈 파일이면 빈 리스트로 초기화
    if not data.strip():
        existing_terms = []
    else:
        existing_terms = json.loads(data)

# 중복 제거: 기존 slug와 비교
existing_slugs = {term['slug'] for term in existing_terms}
terms_to_add = [term for term in new_terms if term['slug'] not in existing_slugs]

# 새 용어 추가
existing_terms.extend(terms_to_add)

# 파일에 저장 (indent=2, ensure_ascii=False)
with open(file_path, 'w', encoding='utf-8') as f:
    json.dump(existing_terms, f, ensure_ascii=False, indent=2)

print(f"✅ {len(terms_to_add)}개의 새로운 용어 추가 완료!")
print(f"📊 총 용어 수: {len(existing_terms)}개")
print(f"🏥 추가된 용어: {', '.join([t['korean'] for t in terms_to_add])}")
