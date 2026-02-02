#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
건설 용어 추가 스크립트 - 건설폐기물/자재관리 테마
테마: 잔재, 폐목재, 폐합성수지, 혼합폐기물, 자재검수, 자재반입, 자재야적, 자재관리대장, 재고관리, 발주
"""

import json
import os

# 추가할 용어 데이터 (10개)
data = [
    {
        "slug": "phe-thai-con-lai",
        "korean": "잔재",
        "vietnamese": "Phế thải còn lại",
        "hanja": "殘材",
        "hanjaReading": "殘(남을 잔) + 材(재목 재)",
        "pronunciation": "잔재",
        "meaningKo": "건설 현장에서 작업 후 남은 자재의 잔여물로, 철근 절단 후 짧은 조각, 목재 단부, 콘크리트 잔량 등을 의미합니다. 통역 시 '잔재'는 'phế thải còn lại' 또는 'vật liệu thừa'로 표현하며, 재사용 가능한 잔재는 'vật liệu tái sử dụng', 폐기 대상 잔재는 'phế liệu'로 구분해야 합니다. 한국 현장에서는 잔재를 철저히 분류하여 재활용률을 높이는 것이 의무이며, 특히 철근·철골 잔재는 스크랩으로 회수하여 수익을 창출합니다. 베트남에서는 잔재 관리가 느슨하여 현장에 방치되거나 무단 투기되는 경우가 많아 환경 문제와 안전사고를 유발합니다. 잔재 처리 비용은 공사비에 포함되므로 통역 시 잔재량 산정과 처리 방법을 명확히 전달해야 합니다.",
        "meaningVi": "Phế thải còn lại là vật liệu thừa sau thi công như mảnh thép thừa sau cắt, đầu gỗ, bê tông dư. Cần phân loại: vật liệu tái sử dụng (có thể dùng lại) và phế liệu (phải hủy bỏ). Quản lý phế thải đúng cách giúp giảm chi phí, bảo vệ môi trường và tránh tai nạn lao động.",
        "context": "폐기물 관리, 환경 안전, 공사비 절감",
        "culturalNote": "한국은 건설폐기물 관리법에 따라 잔재를 5대 분류(콘크리트, 아스팔트, 목재, 금속, 혼합)로 분리배출해야 하며, 재활용률 목표(95% 이상)가 법정화되어 있습니다. 잔재 처리 업체는 허가를 받은 전문 업체만 가능하고, 처리 증명서를 발급받아 관리해야 합니다. 베트남은 폐기물 분류 기준이 모호하고, 잔재를 단순 매립하거나 야적하는 경우가 많으며, 처리 업체 허가 제도가 미비합니다. 한국 현장에서는 잔재량을 일일 기록하고 주간 보고하지만, 베트남은 이를 형식적으로 하거나 기록하지 않는 경우가 많아 폐기물 처리 비용 관리가 어렵습니다.",
        "commonMistakes": [
            {
                "mistake": "'잔재'를 'rác thải'(쓰레기)로 번역",
                "correction": "'phế thải còn lại' 또는 'vật liệu thừa' 사용",
                "explanation": "잔재는 자재의 일부로 재활용 가능하지만, 쓰레기는 폐기 대상"
            },
            {
                "mistake": "철근 잔재를 '폐철'로만 표기",
                "correction": "'thép thừa' (짧은 조각 재사용 가능) vs 'phế liệu thép' (스크랩) 구분",
                "explanation": "길이에 따라 재사용 여부가 달라지므로 명확한 구분 필요"
            },
            {
                "mistake": "잔재 처리를 '버리기'로만 표현",
                "correction": "'phân loại → tái sử dụng / thu hồi / xử lý' 전체 프로세스 명시",
                "explanation": "한국 기준은 분류와 재활용이 우선이므로 단순 폐기로 오해 금지"
            }
        ],
        "examples": [
            {
                "ko": "오늘 발생한 철근 잔재는 1m 이상은 보관하고, 그 이하는 스크랩으로 회수하세요.",
                "vi": "Thép thừa hôm nay, nếu trên 1m thì cất giữ, dưới 1m thu hồi làm phế liệu.",
                "situation": "onsite"
            },
            {
                "ko": "잔재 야적장을 분류 구역별로 구획하여 재활용률을 높이겠습니다.",
                "vi": "Sẽ chia khu vực tập kết phế thải theo loại để tăng tỷ lệ tái chế.",
                "situation": "formal"
            },
            {
                "ko": "이번 주 잔재 발생량은 5톤인데, 목표치 3톤을 초과했으니 원인을 분석해 주세요.",
                "vi": "Lượng phế thải tuần này là 5 tấn, vượt mục tiêu 3 tấn, hãy phân tích nguyên nhân.",
                "situation": "formal"
            }
        ],
        "relatedTerms": ["건설폐기물", "재활용", "스크랩", "폐기물 분류", "야적장"]
    },
    {
        "slug": "go-phe-lieu",
        "korean": "폐목재",
        "vietnamese": "Gỗ phế liệu",
        "hanja": "廢木材",
        "hanjaReading": "廢(버릴 폐) + 木(나무 목) + 材(재목 재)",
        "pronunciation": "폐목재",
        "meaningKo": "건설 현장에서 사용 후 버려지는 목재 폐기물로, 거푸집 해체 후 합판, 각재, 비계 목재 등이 해당됩니다. 통역 시 '폐목재'는 'gỗ phế liệu', '재활용 목재'는 'gỗ tái chế'로 구분하며, 처리 방법에 따라 '파쇄(nghiền)'와 '소각(đốt)'으로 나뉩니다. 한국에서는 폐목재를 A등급(재사용 가능 청정 목재)과 B등급(폐기 대상 오염 목재)으로 분류하며, 오염되지 않은 폐목재는 톱밥, 펠릿, 파티클보드 원료로 재활용됩니다. 못, 철물이 박힌 폐목재는 재활용이 어려우므로 분리 배출 시 주의가 필요하며, 페인트·방부제 처리된 목재는 유해 폐기물로 분류되어 특별 관리됩니다.",
        "meaningVi": "Gỗ phế liệu là gỗ thải bỏ từ công trường như ván khuôn cũ, gỗ giáo, gỗ giàn giáo. Phân loại: gỗ sạch (có thể tái chế thành mùn cưa, pellet) và gỗ nhiễm bẩn (sơn, chống mối) phải xử lý riêng. Gỗ có đinh, sắt khó tái chế nên cần tách kim loại trước khi xử lý.",
        "context": "폐기물 관리, 거푸집 공사, 환경 관리",
        "culturalNote": "한국은 폐목재 재활용률이 90% 이상으로 매우 높으며, 현장에서 못 제거 후 깨끗이 분류하여 전문 재활용 업체에 위탁합니다. 폐목재 처리 비용은 톤당 5만~10만원이며, 재활용 가능 목재는 역으로 수익을 창출할 수 있습니다. 베트남은 폐목재를 단순 소각하거나 매립하는 경우가 많고, 못 제거 없이 혼합 배출하여 재활용률이 낮습니다. 한국 현장에서는 폐목재 야적 시 화재 위험 때문에 소화기 비치와 금연 구역 지정이 의무이지만, 베트남은 이를 소홀히 하여 화재 사고가 빈번합니다. 통역 시 폐목재 분류 기준과 처리 방법의 차이를 명확히 전달해야 합니다.",
        "commonMistakes": [
            {
                "mistake": "'폐목재'를 'gỗ cũ'(낡은 목재)로 번역",
                "correction": "'gỗ phế liệu' 사용",
                "explanation": "낡은 목재는 재사용 가능할 수 있지만, 폐목재는 폐기 대상"
            },
            {
                "mistake": "거푸집 합판을 '일반 목재'와 같은 방법으로 처리",
                "correction": "'ván khuôn phế liệu' 별도 분류 (접착제 포함으로 재활용 방법 다름)",
                "explanation": "합판은 접착제 함유로 일반 목재와 재활용 공정이 다름"
            },
            {
                "mistake": "폐목재 소각을 '태우기'로만 표현",
                "correction": "'xử lý nhiệt' (열처리) 또는 'đốt có kiểm soát' (통제 소각)",
                "explanation": "무단 소각은 불법이며, 환경 기준을 준수한 소각 시설 이용 필요"
            }
        ],
        "examples": [
            {
                "ko": "거푸집 해체 후 폐목재는 못을 제거하고 A/B등급으로 분류해 주세요.",
                "vi": "Sau tháo ván khuôn, gỗ phế liệu nhổ đinh và phân loại A/B.",
                "situation": "onsite"
            },
            {
                "ko": "이번 달 폐목재 발생량이 20톤인데, 재활용 업체와 계약하여 처리하겠습니다.",
                "vi": "Lượng gỗ phế liệu tháng này là 20 tấn, sẽ ký hợp đồng với đơn vị tái chế để xử lý.",
                "situation": "formal"
            },
            {
                "ko": "폐목재 야적장 근처에서 흡연과 화기 사용을 엄격히 금지합니다.",
                "vi": "Nghiêm cấm hút thuốc và dùng lửa gần khu tập kết gỗ phế liệu.",
                "situation": "onsite"
            }
        ],
        "relatedTerms": ["거푸집", "합판", "각재", "건설폐기물", "재활용"]
    },
    {
        "slug": "nhua-phe-lieu",
        "korean": "폐합성수지",
        "vietnamese": "Nhựa phế liệu",
        "hanja": "廢合成樹脂",
        "hanjaReading": "廢(버릴 폐) + 合(합할 합) + 成(이룰 성) + 樹(나무 수) + 脂(기름 지)",
        "pronunciation": "폐합성수지",
        "meaningKo": "건설 현장에서 발생하는 플라스틱 폐기물로, 단열재 스티로폼, 파이프 절단재, 포장재, 방수시트 등이 포함됩니다. 통역 시 '폐합성수지'는 'nhựa phế liệu', 'PE/PVC 파이프'는 'ống PE/PVC', '스티로폼'은 'xốp mềm' 또는 'EPS'로 표현합니다. 합성수지는 재질별(PE, PP, PVC, PS 등) 분리배출이 원칙이며, 혼합 배출 시 재활용이 불가능해 매립 또는 소각 처리됩니다. 스티로폼은 부피가 커서 운반 비용이 높으므로 현장에서 압축기(compactor)로 압축 후 배출하는 것이 효율적입니다. 방수시트, 접착제가 묻은 합성수지는 유해 폐기물로 분류되어 별도 처리가 필요합니다.",
        "meaningVi": "Nhựa phế liệu là rác thải nhựa từ công trường như xốp cách nhiệt, mảnh ống nhựa, vật liệu đóng gói, màng chống thấm. Phân loại theo loại nhựa (PE, PVC, PP, PS) để tái chế. Xốp EPS cần ép để giảm thể tích trước vận chuyển. Nhựa dính keo, chống thấm là chất thải nguy hại cần xử lý riêng.",
        "context": "폐기물 관리, 포장재, 단열 공사",
        "culturalNote": "한국은 폐합성수지 재활용률 목표가 70% 이상이며, 현장에서 재질별 분리배출을 철저히 합니다. 스티로폼은 압축 후 재활용 업체에 무상 또는 유상으로 인계하며, PE/PVC 파이프는 파쇄 후 재생 원료로 판매됩니다. 베트남은 폐합성수지 분류 기준이 모호하고, 대부분 혼합 배출하여 재활용률이 낮습니다. 스티로폼을 압축 없이 그대로 버려 운반 비용이 과다하게 발생하는 경우가 많습니다. 한국은 방수시트 폐기물을 유해 폐기물로 분류하지만, 베트남은 일반 폐기물로 취급하여 환경 오염 우려가 있습니다. 통역 시 재질 구분과 처리 방법의 중요성을 강조해야 합니다.",
        "commonMistakes": [
            {
                "mistake": "'합성수지'를 'nhựa'로만 번역하고 재질 구분 없음",
                "correction": "'nhựa PE', 'nhựa PVC', 'nhựa PP' 등 재질 명시",
                "explanation": "재질별로 재활용 방법이 다르므로 정확한 분류 필요"
            },
            {
                "mistake": "'스티로폼'을 'bọt nhựa'(거품 플라스틱)로 번역",
                "correction": "'xốp mềm EPS' 또는 'xốp cách nhiệt' 사용",
                "explanation": "베트남에서 'xốp mềm'은 스티로폼을 지칭하는 관용 표현"
            },
            {
                "mistake": "폐합성수지를 '소각 처리'로만 제안",
                "correction": "재질 분류 → 재활용 → 불가능한 것만 소각/매립 순서 준수",
                "explanation": "한국 기준은 재활용 우선이므로 소각은 최후 수단"
            }
        ],
        "examples": [
            {
                "ko": "스티로폼 폐기물은 압축기로 1/20 부피로 줄인 후 재활용 업체에 인계하세요.",
                "vi": "Rác xốp mềm dùng máy ép giảm 1/20 thể tích rồi giao cho đơn vị tái chế.",
                "situation": "onsite"
            },
            {
                "ko": "PVC 파이프 절단재는 별도 수거하여 재생 원료로 판매 가능합니다.",
                "vi": "Mảnh ống PVC thu riêng có thể bán làm nguyên liệu tái sinh.",
                "situation": "formal"
            },
            {
                "ko": "방수시트는 유해 폐기물이므로 일반 폐합성수지와 혼합하지 마세요.",
                "vi": "Màng chống thấm là chất thải nguy hại, không trộn với nhựa phế liệu thông thường.",
                "situation": "onsite"
            }
        ],
        "relatedTerms": ["스티로폼", "파이프", "방수시트", "건설폐기물", "재활용"]
    },
    {
        "slug": "phe-thai-hon-hop",
        "korean": "혼합폐기물",
        "vietnamese": "Phế thải hỗn hợp",
        "hanja": "混合廢棄物",
        "hanjaReading": "混(섞일 혼) + 合(합할 합) + 廢(버릴 폐) + 棄(버릴 기) + 物(물건 물)",
        "pronunciation": "혼합폐기물",
        "meaningKo": "건설 현장에서 여러 종류의 폐기물이 섞여서 분리가 어려운 상태의 폐기물을 의미합니다. 통역 시 '혼합폐기물'은 'phế thải hỗn hợp', '선별 불가'는 'không thể phân loại'로 표현합니다. 혼합폐기물은 재활용이 거의 불가능하여 처리 비용이 단일 폐기물 대비 2~3배 높으며, 소각·매립 처리가 원칙입니다. 한국 건설 현장에서는 혼합폐기물 발생을 최소화하기 위해 분리배출 교육을 철저히 하고, 폐기물 종류별 전용 수거함을 설치합니다. 혼합폐기물 발생률이 전체 폐기물의 10%를 초과하면 패널티가 부과되는 현장도 많습니다. 불법 투기 방지를 위해 혼합폐기물 배출 시 전자 태그(RFID)를 부착하여 추적 관리합니다.",
        "meaningVi": "Phế thải hỗn hợp là rác thải nhiều loại trộn lẫn, khó phân loại như gỗ lẫn nhựa lẫn kim loại. Rác hỗn hợp không thể tái chế, chi phí xử lý cao gấp 2-3 lần rác đơn thuần, phải đốt hoặc chôn lấp. Để giảm phế thải hỗn hợp, công trường phải đặt thùng riêng cho từng loại và đào tạo công nhân phân loại đúng.",
        "context": "폐기물 관리, 비용 절감, 환경 관리",
        "culturalNote": "한국은 혼합폐기물 처리 비용이 톤당 15~25만원으로 매우 비싸기 때문에 현장에서 분리배출을 극도로 강조합니다. 환경 관리 담당자가 매일 폐기물 분리 상태를 점검하고, 위반 시 작업자에게 재교육 또는 경고를 부과합니다. 베트남은 폐기물 분리 의식이 낮아 대부분 혼합 배출되며, 처리 비용도 상대적으로 저렴해 분리배출 동기가 약합니다. 한국 업체가 베트남 현장을 운영할 때 혼합폐기물 과다 발생으로 예상보다 폐기물 처리 비용이 2~3배 증가하는 사례가 많습니다. 통역사는 분리배출의 경제적 중요성을 강조하고, 한국식 분리 기준을 베트남 근로자에게 명확히 전달해야 합니다.",
        "commonMistakes": [
            {
                "mistake": "'혼합폐기물'을 'rác trộn lẫn'(섞인 쓰레기)로만 번역",
                "correction": "'phế thải hỗn hợp' (공식 환경 용어) 사용",
                "explanation": "법적·행정적 문서에서는 정식 용어 사용 필요"
            },
            {
                "mistake": "혼합폐기물을 '나중에 분류'한다고 표현",
                "correction": "'một khi trộn lẫn, không thể tái chế' (섞이면 재활용 불가) 명확히 전달",
                "explanation": "사후 분류는 비현실적이며, 사전 분리가 핵심"
            },
            {
                "mistake": "처리 비용을 '똑같다'고 설명",
                "correction": "'chi phí gấp 2-3 lần' (2~3배 비용) 명시",
                "explanation": "경제적 손실을 명확히 알려야 분리배출 동기 부여"
            }
        ],
        "examples": [
            {
                "ko": "혼합폐기물 발생을 줄이기 위해 폐기물 분리 교육을 주 1회 실시하겠습니다.",
                "vi": "Để giảm phế thải hỗn hợp, sẽ đào tạo phân loại rác mỗi tuần 1 lần.",
                "situation": "formal"
            },
            {
                "ko": "이번 주 혼합폐기물이 15%나 발생했는데, 분리배출 기준을 다시 교육해 주세요.",
                "vi": "Tuần này phế thải hỗn hợp chiếm tới 15%, hãy đào tạo lại tiêu chuẩn phân loại.",
                "situation": "onsite"
            },
            {
                "ko": "혼합폐기물 처리 비용이 톤당 20만원이니, 분리배출로 비용을 절감합시다.",
                "vi": "Chi phí xử lý phế thải hỗn hợp 200 nghìn won/tấn, hãy phân loại để tiết kiệm chi phí.",
                "situation": "formal"
            }
        ],
        "relatedTerms": ["분리배출", "폐기물 처리", "재활용", "환경 관리", "처리 비용"]
    },
    {
        "slug": "kiem-nhan-vat-lieu",
        "korean": "자재검수",
        "vietnamese": "Kiểm nhận vật liệu",
        "hanja": "資材檢收",
        "hanjaReading": "資(재물 자) + 材(재목 재) + 檢(검사할 검) + 收(거둘 수)",
        "pronunciation": "자재검수",
        "meaningKo": "건설 현장에 반입된 자재의 수량, 규격, 품질을 확인하고 인수하는 절차입니다. 통역 시 '검수'는 'kiểm nhận', '합격'은 'đạt', '불합격'은 'không đạt', '반품'은 'trả lại'로 표현합니다. 검수는 자재 도착 즉시 수행해야 하며, 수량(kiểm tra số lượng), 외관(kiểm tra ngoại quan), 치수(kiểm tra kích thước), 시험성적서(giấy chứng nhận thí nghiệm) 확인이 필수입니다. 한국 현장에서는 자재 검수 체크리스트를 사용하여 항목별로 확인 후 서명하며, 불합격 시 즉시 반품 조치합니다. 검수 누락으로 인한 하자 발생 시 검수 담당자에게 책임이 부과되므로 매우 중요한 절차입니다.",
        "meaningVi": "Kiểm nhận vật liệu là quy trình kiểm tra số lượng, quy cách, chất lượng vật liệu khi nhập về công trường và xác nhận tiếp nhận. Kiểm tra bao gồm: số lượng, ngoại quan, kích thước, giấy chứng nhận thí nghiệm. Nếu không đạt phải trả lại ngay. Người kiểm nhận chịu trách nhiệm nếu vật liệu lỗi gây hư hỏng sau này.",
        "context": "자재 관리, 품질 관리, 공사 진행",
        "culturalNote": "한국은 자재 검수를 매우 철저히 하며, 검수 담당자는 자재 반입 전 미리 도면과 주문서를 검토하고 검수 기준을 숙지합니다. 자재 도착 시 운전기사와 함께 하역 전 육안 검사를 하고, 수량 확인 후 샘플링으로 치수·품질을 확인합니다. 불합격 시 현장 반입을 거부하고 즉시 반품 처리하며, 이를 기록으로 남깁니다. 베트남은 검수 절차가 형식적인 경우가 많아 수량만 확인하고 품질·규격 검사를 생략하는 경우가 많습니다. 자재 하역 후 문제 발견 시 반품이 어려워 현장에서 그대로 사용하거나 추가 비용을 들여 보강하는 사례가 빈번합니다. 통역사는 검수 기준과 절차의 중요성을 강조하고, 불합격 기준을 명확히 전달해야 합니다.",
        "commonMistakes": [
            {
                "mistake": "'검수'를 'kiểm tra'(단순 검사)로만 번역",
                "correction": "'kiểm nhận' (검사 후 인수) 사용",
                "explanation": "검수는 검사와 인수의 복합 행위로, 책임이 수반됨"
            },
            {
                "mistake": "검수를 '보기만 하는 것'으로 설명",
                "correction": "'kiểm tra + ký nhận + chịu trách nhiệm' (검사+서명+책임) 명확히 전달",
                "explanation": "검수는 법적 책임이 있는 공식 절차"
            },
            {
                "mistake": "불합격 시 '나중에 반품'이라고 표현",
                "correction": "'trả lại ngay lập tức' (즉시 반품) 명시",
                "explanation": "하역 후 반품은 어려우므로 반입 전 검수가 핵심"
            }
        ],
        "examples": [
            {
                "ko": "철근 반입 시 밀시트와 수량을 대조하고, 규격은 샘플링으로 검수하세요.",
                "vi": "Khi nhận thép, đối chiếu mill sheet với số lượng và kiểm tra quy cách bằng lấy mẫu.",
                "situation": "onsite"
            },
            {
                "ko": "이 자재는 외관에 녹이 심해서 검수 불합격입니다. 즉시 반품 처리하세요.",
                "vi": "Vật liệu này bị gỉ nặng ở ngoại quan, không đạt kiểm nhận. Trả lại ngay.",
                "situation": "onsite"
            },
            {
                "ko": "검수 체크리스트에 서명 후 자재를 야적장으로 이동시키세요.",
                "vi": "Sau khi ký danh sách kiểm nhận, chuyển vật liệu đến khu tập kết.",
                "situation": "formal"
            }
        ],
        "relatedTerms": ["자재 반입", "품질 관리", "반품", "밀시트", "시험성적서"]
    },
    {
        "slug": "nhap-vat-lieu",
        "korean": "자재반입",
        "vietnamese": "Nhập vật liệu",
        "hanja": "資材搬入",
        "hanjaReading": "資(재물 자) + 材(재목 재) + 搬(옮길 반) + 入(들 입)",
        "pronunciation": "자재반입",
        "meaningKo": "건설 자재를 현장으로 운반하여 들여오는 행위로, 사전 계획과 조율이 필요한 중요한 물류 활동입니다. 통역 시 '반입'은 'nhập', '반입 계획'은 'kế hoạch nhập vật liệu', '반입 시간'은 'thời gian nhập'으로 표현합니다. 자재 반입 시에는 운반 경로, 크레인·지게차 동원 계획, 안전 조치, 교통 통제, 야적 공간 확보가 선행되어야 합니다. 대형 자재(H빔, PC부재 등) 반입 시에는 도로 점용 허가, 경찰 협조, 주변 주민 사전 고지가 필요하며, 한국에서는 이를 매우 엄격하게 관리합니다. 자재 반입은 공정 계획과 연동되어야 하므로 통역사는 반입 일정과 공정의 연관성을 명확히 전달해야 합니다.",
        "meaningVi": "Nhập vật liệu là việc vận chuyển vật liệu xây dựng vào công trường, cần lập kế hoạch và điều phối trước. Bao gồm: lộ trình vận chuyển, kế hoạch cần cẩu/xe nâng, biện pháp an toàn, kiểm soát giao thông, chuẩn bị khu tập kết. Vật liệu lớn (dầm H, cấu kiện PC) cần xin phép chiếm đường, phối hợp cảnh sát, thông báo dân cư.",
        "context": "자재 관리, 공정 관리, 물류 계획",
        "culturalNote": "한국은 자재 반입을 주간 단위로 계획하고, 반입 3일 전 관련 팀(구조, 설비, 안전)에 사전 공유하여 충돌을 방지합니다. 대형 자재는 야간 반입을 원칙으로 하며, 교통 통제 계획서를 작성하여 경찰서에 제출합니다. 크레인 동원 시 작업 반경 내 안전 펜스를 설치하고, 신호수를 배치합니다. 베트남은 자재 반입이 즉흥적인 경우가 많아 현장에 자재가 도착했는데 야적 공간이 없거나, 하역 장비가 준비되지 않아 대기 시간이 길어지는 사례가 빈번합니다. 한국 현장은 자재 반입 시 검수와 야적을 동시에 진행하지만, 베트남은 이를 분리하여 비효율이 발생합니다. 통역사는 반입 계획의 중요성과 사전 조율 절차를 강조해야 합니다.",
        "commonMistakes": [
            {
                "mistake": "'반입'을 'mang vào'(들고 들어가기)로 직역",
                "correction": "'nhập vật liệu' 또는 'đưa vật liệu vào công trường' 사용",
                "explanation": "자재 반입은 단순 운반이 아닌 계획적 물류 활동"
            },
            {
                "mistake": "반입 시간을 '아무 때나 가능'으로 설명",
                "correction": "'theo kế hoạch và thời gian quy định' (계획과 규정 시간에 따라) 명시",
                "explanation": "무계획 반입은 현장 혼란과 안전사고 유발"
            },
            {
                "mistake": "대형 자재 반입을 '그냥 들여오면 된다'고 표현",
                "correction": "'cần xin phép, phối hợp cảnh sát, thông báo trước' (허가·경찰 협조·사전 고지 필요)",
                "explanation": "대형 자재는 법적 절차와 안전 조치 필수"
            }
        ],
        "examples": [
            {
                "ko": "이번 주 철골 반입은 수요일 야간 11시로 계획되었으니, 크레인과 신호수를 준비하세요.",
                "vi": "Tuần này nhập thép kết cấu vào đêm thứ Tư 11h, chuẩn bị cần cẩu và người chỉ huy.",
                "situation": "formal"
            },
            {
                "ko": "콘크리트 반입 차량이 1시간 후 도착하니, 타설 팀은 대기해 주세요.",
                "vi": "Xe bê tông sẽ đến sau 1 giờ, đội đổ bê tông chuẩn bị sẵn sàng.",
                "situation": "onsite"
            },
            {
                "ko": "PC부재 반입 시 도로 점용 허가를 받았으니, 경찰 협조 하에 진행하세요.",
                "vi": "Đã được cấp phép chiếm đường khi nhập cấu kiện PC, tiến hành với sự phối hợp của cảnh sát.",
                "situation": "formal"
            }
        ],
        "relatedTerms": ["자재 검수", "야적", "크레인", "물류 계획", "공정 관리"]
    },
    {
        "slug": "tap-ket-vat-lieu",
        "korean": "자재야적",
        "vietnamese": "Tập kết vật liệu",
        "hanja": "資材野積",
        "hanjaReading": "資(재물 자) + 材(재목 재) + 野(들 야) + 積(쌓을 적)",
        "pronunciation": "자재야적",
        "meaningKo": "건설 자재를 현장 내 지정된 장소에 임시로 쌓아두는 행위로, 공간 계획과 안전 관리가 필수입니다. 통역 시 '야적'은 'tập kết', '야적장'은 'khu tập kết', '적재 높이'는 'chiều cao xếp'으로 표현합니다. 자재 야적 시에는 자재 종류별 구획(phân khu theo loại), 선입선출 원칙(nguyên tắc FIFO), 적재 높이 제한(giới hạn chiều cao), 통행로 확보(đảm bảo lối đi), 우천 대비 덮개(bạt che mưa)가 고려되어야 합니다. 중량 자재는 지반 침하를 고려하여 깔판(pallet) 위에 적재하고, 장척 자재(철근, 파이프)는 전도 방지를 위한 받침대를 설치합니다. 한국 현장에서는 야적장 배치도를 작성하여 자재별 위치를 시각화하고, 정기적으로 정리정돈 상태를 점검합니다.",
        "meaningVi": "Tập kết vật liệu là việc xếp vật liệu tạm thời tại khu vực quy định trong công trường, cần kế hoạch không gian và quản lý an toàn. Bao gồm: phân khu theo loại, nguyên tắc FIFO, giới hạn chiều cao xếp, đảm bảo lối đi, bạt che mưa. Vật liệu nặng đặt trên pallet, vật liệu dài (thép, ống) có giá đỡ chống đổ.",
        "context": "자재 관리, 공간 관리, 안전 관리",
        "culturalNote": "한국은 자재 야적을 체계적으로 관리하며, 야적장 바닥은 콘크리트 포장 또는 쇄석 다짐으로 정리하고, 배수로를 설치하여 우수가 고이지 않게 합니다. 자재별로 표지판을 설치하여 품명·규격·입고일·담당자를 표기하고, RFID 태그로 재고를 실시간 관리하는 현장도 많습니다. 야적 높이는 자재 종류별로 기준이 있으며(철근 1.5m, 합판 2m 등), 이를 초과하면 안전 점검에서 지적됩니다. 베트남은 야적장이 무질서한 경우가 많아 자재를 찾는 데 시간이 소요되고, 중장비 통행로가 확보되지 않아 작업 효율이 떨어집니다. 우기에 덮개 없이 야적하여 자재가 손상되는 사례도 빈번합니다. 통역사는 야적 기준과 관리 방법의 차이를 명확히 전달해야 합니다.",
        "commonMistakes": [
            {
                "mistake": "'야적'을 'để ngoài trời'(야외에 두기)로만 번역",
                "correction": "'tập kết' (계획적 적재) 사용",
                "explanation": "야적은 단순 방치가 아닌 관리된 임시 보관"
            },
            {
                "mistake": "야적 높이를 '높이 쌓을수록 좋다'고 설명",
                "correction": "'giới hạn chiều cao theo quy định an toàn' (안전 기준에 따라 높이 제한) 명시",
                "explanation": "과적은 붕괴 위험으로 안전사고 유발"
            },
            {
                "mistake": "자재 종류를 '섞어서 쌓아도 된다'고 표현",
                "correction": "'phân khu riêng theo loại vật liệu' (자재 종류별 구획) 강조",
                "explanation": "혼합 야적은 자재 찾기 어렵고 손상 위험 증가"
            }
        ],
        "examples": [
            {
                "ko": "철근 야적장은 우기에 대비해 배수로를 설치하고, 깔판 위에 적재하세요.",
                "vi": "Khu tập kết thép chuẩn bị mương thoát nước cho mùa mưa và xếp trên pallet.",
                "situation": "onsite"
            },
            {
                "ko": "이 자재는 선입선출 원칙에 따라 입고 순서대로 사용해야 하니, 앞쪽부터 배치하세요.",
                "vi": "Vật liệu này theo FIFO phải dùng theo thứ tự nhập, hãy xếp từ phía trước.",
                "situation": "formal"
            },
            {
                "ko": "야적장 통행로는 폭 3m 이상 확보하여 덤프트럭이 진입할 수 있게 하세요.",
                "vi": "Lối đi trong khu tập kết đảm bảo rộng trên 3m để xe ben có thể vào.",
                "situation": "onsite"
            }
        ],
        "relatedTerms": ["자재 반입", "재고 관리", "선입선출", "적재", "야적장"]
    },
    {
        "slug": "so-quan-ly-vat-lieu",
        "korean": "자재관리대장",
        "vietnamese": "Sổ quản lý vật liệu",
        "hanja": "資材管理臺帳",
        "hanjaReading": "資(재물 자) + 材(재목 재) + 管(대롱 관) + 理(다스릴 리) + 臺(별 대) + 帳(장부 장)",
        "pronunciation": "자재관리대장",
        "meaningKo": "건설 현장에서 자재의 입고·출고·재고를 기록하고 관리하는 장부로, 공사 원가 관리와 자재 손실 방지를 위한 핵심 문서입니다. 통역 시 '대장'은 'sổ', '입고'는 'nhập kho', '출고'는 'xuất kho', '재고'는 'tồn kho'로 표현합니다. 자재관리대장에는 자재명, 규격, 단위, 입고일시, 출고일시, 사용처, 잔량, 담당자가 기록되며, 일일 단위로 작성하는 것이 원칙입니다. 한국 현장에서는 엑셀 또는 ERP 시스템으로 전산 관리하고, 실물 재고와 장부 재고를 주간 단위로 대조하여 차이를 분석합니다. 재고 차이가 5% 이상 발생하면 원인 조사 및 개선 조치를 시행합니다.",
        "meaningVi": "Sổ quản lý vật liệu là sổ ghi chép nhập-xuất-tồn vật liệu tại công trường, là tài liệu quan trọng để quản lý chi phí và ngăn thất thoát. Ghi: tên vật liệu, quy cách, đơn vị, ngày giờ nhập/xuất, nơi sử dụng, số dư, người phụ trách. Lập hàng ngày, đối chiếu tồn kho thực tế và sổ sách mỗi tuần.",
        "context": "자재 관리, 원가 관리, 재고 통제",
        "culturalNote": "한국은 자재관리대장을 법적 의무 문서로 간주하며, 감사 시 필수 제출 서류입니다. 자재 입고 시 검수 담당자가 즉시 대장에 기록하고, 출고 시에는 사용처와 수량을 명확히 기재하여 추적 가능성을 확보합니다. 대형 현장에서는 바코드나 RFID 시스템을 도입하여 자재 이동을 자동 기록하며, 실시간 재고 현황을 대시보드로 확인할 수 있습니다. 베트남은 자재관리대장 작성이 형식적인 경우가 많아 입고는 기록하지만 출고는 기록하지 않거나, 며칠치를 모아서 한꺼번에 기록하는 등 정확성이 떨어집니다. 실물 재고와 장부 재고의 차이가 커도 원인 분석 없이 넘어가는 경우가 많아 자재 손실이 발생합니다. 통역사는 대장 작성의 법적·경제적 중요성을 강조해야 합니다.",
        "commonMistakes": [
            {
                "mistake": "'대장'을 'danh sách'(목록)로 번역",
                "correction": "'sổ quản lý' 또는 'sổ sách' (장부) 사용",
                "explanation": "대장은 단순 목록이 아닌 관리 문서로서의 성격"
            },
            {
                "mistake": "입고만 기록하고 출고는 안 해도 된다고 설명",
                "correction": "'nhập-xuất-tồn đều phải ghi' (입고-출고-재고 모두 기록 필수) 명확히 전달",
                "explanation": "출고 미기록 시 재고 파악 불가로 관리 의미 상실"
            },
            {
                "mistake": "주간 단위로 기록해도 된다고 표현",
                "correction": "'ghi hàng ngày, đối chiếu hàng tuần' (일일 기록, 주간 대조) 강조",
                "explanation": "지연 기록은 분실·도난 발생 시 추적 불가"
            }
        ],
        "examples": [
            {
                "ko": "자재관리대장에 오늘 입고된 시멘트 200포를 기록하고, 담당자 서명을 받으세요.",
                "vi": "Ghi 200 bao xi măng nhập hôm nay vào sổ quản lý vật liệu và lấy chữ ký người phụ trách.",
                "situation": "onsite"
            },
            {
                "ko": "이번 주 재고 실사 결과, 장부와 실물이 3% 차이 나는데 원인을 조사해 주세요.",
                "vi": "Kiểm kê tuần này, sổ sách và thực tế chênh 3%, hãy điều tra nguyên nhân.",
                "situation": "formal"
            },
            {
                "ko": "자재관리대장은 엑셀로 작성하고, 매일 오후 5시에 업데이트하세요.",
                "vi": "Sổ quản lý vật liệu làm bằng Excel, cập nhật hàng ngày lúc 5h chiều.",
                "situation": "formal"
            }
        ],
        "relatedTerms": ["입고", "출고", "재고", "재고 실사", "원가 관리"]
    },
    {
        "slug": "quan-ly-ton-kho",
        "korean": "재고관리",
        "vietnamese": "Quản lý tồn kho",
        "hanja": "在庫管理",
        "hanjaReading": "在(있을 재) + 庫(곳간 고) + 管(대롱 관) + 理(다스릴 리)",
        "pronunciation": "재고관리",
        "meaningKo": "건설 현장에서 보유한 자재의 수량, 상태, 위치를 파악하고 적정 수준을 유지하는 관리 활동입니다. 통역 시 '재고'는 'tồn kho', '적정 재고'는 'tồn kho hợp lý', '과잉 재고'는 'tồn kho dư thừa', '재고 부족'은 'thiếu hàng tồn kho'로 표현합니다. 재고관리의 목적은 공정 지연 방지(ngăn chậm tiến độ)와 자재비 절감(giảm chi phí vật liệu)이며, 과잉 재고는 보관 비용과 자금 압박을, 재고 부족은 공정 지연을 유발합니다. 한국 현장에서는 JIT(Just-In-Time) 방식을 선호하여 필요한 시점에 필요한 만큼만 반입하고, 안전 재고(safety stock)는 3~7일분만 유지합니다. 재고 회전율(inventory turnover)을 KPI로 관리하며, 월 4회 이상을 목표로 합니다.",
        "meaningVi": "Quản lý tồn kho là hoạt động nắm bắt số lượng, tình trạng, vị trí vật liệu và duy trì ở mức hợp lý. Mục đích: ngăn chậm tiến độ và giảm chi phí vật liệu. Tồn kho dư thừa gây chi phí bảo quản và áp lực vốn, thiếu hàng gây chậm tiến độ. Phương pháp JIT nhập đúng thời điểm cần, chỉ giữ kho an toàn 3-7 ngày.",
        "context": "자재 관리, 원가 절감, 공정 관리",
        "culturalNote": "한국은 재고관리를 매우 정교하게 하며, ERP 시스템과 연동하여 실시간 재고 현황을 파악하고, 안전 재고 수준 이하로 떨어지면 자동 발주 알림이 발생합니다. 월말에는 재고 실사(kiểm kê)를 필수로 시행하여 장부 재고와 실물 재고를 대조하고, 차이가 발생하면 원인 분석 보고서를 작성합니다. 과잉 재고는 자금 회전율을 악화시키므로 철저히 관리되며, 장기 체류 재고(slow-moving stock)는 타 현장으로 이동하거나 반품 처리합니다. 베트남은 재고관리 개념이 약해 자재를 대량 주문하여 현장에 쌓아두는 경향이 있으며, 재고 실사도 형식적으로 하거나 생략하는 경우가 많습니다. 한국 업체가 베트남 현장에서 과잉 재고로 인한 자금 압박을 겪는 사례가 많으므로, 통역사는 적정 재고 개념을 명확히 전달해야 합니다.",
        "commonMistakes": [
            {
                "mistake": "'재고'를 'kho'(창고)로만 번역",
                "correction": "'tồn kho' (보유 재고량) 사용",
                "explanation": "창고는 장소, 재고는 보유 물량의 개념"
            },
            {
                "mistake": "재고를 '많을수록 좋다'고 설명",
                "correction": "'tồn kho hợp lý' (적정 재고) 개념 전달, 과잉은 비용 증가",
                "explanation": "과잉 재고는 자금 압박과 보관 비용 증가"
            },
            {
                "mistake": "재고 실사를 '1년에 1번'으로 표현",
                "correction": "'kiểm kê hàng tháng' (월간 실사) 또는 '주간 확인' 명시",
                "explanation": "장기 미실시 시 손실 누적으로 원인 파악 불가"
            }
        ],
        "examples": [
            {
                "ko": "이 현장의 적정 재고는 3일분인데, 현재 10일분이 쌓여 있으니 발주를 중단하세요.",
                "vi": "Tồn kho hợp lý của công trường này là 3 ngày, hiện đang có 10 ngày, ngừng đặt hàng.",
                "situation": "formal"
            },
            {
                "ko": "재고 회전율이 낮아서 자재비가 과다하게 발생하고 있으니 개선 방안을 마련해 주세요.",
                "vi": "Tỷ lệ quay vòng tồn kho thấp nên chi phí vật liệu quá cao, hãy lập phương án cải thiện.",
                "situation": "formal"
            },
            {
                "ko": "이번 달 재고 실사 결과, 장부와 실물이 일치하니 재고관리가 잘 되고 있습니다.",
                "vi": "Kiểm kê tháng này, sổ sách và thực tế khớp nhau, quản lý tồn kho tốt.",
                "situation": "formal"
            }
        ],
        "relatedTerms": ["적정 재고", "과잉 재고", "재고 실사", "JIT", "자재 관리"]
    },
    {
        "slug": "dat-hang",
        "korean": "발주",
        "vietnamese": "Đặt hàng",
        "hanja": "發注",
        "hanjaReading": "發(필 발) + 注(부을 주)",
        "pronunciation": "발주",
        "meaningKo": "건설 자재나 장비를 공급업체에 주문하는 행위로, 공정 계획과 원가 관리의 핵심 업무입니다. 통역 시 '발주'는 'đặt hàng', '발주서'는 'đơn đặt hàng', '긴급 발주'는 'đặt hàng khẩn', '취소'는 'hủy đơn'으로 표현합니다. 발주 시에는 품명·규격·수량·납기·단가를 명확히 기재해야 하며, 한국에서는 3사 이상 견적 비교(so sánh báo giá 3 nhà)를 원칙으로 합니다. 발주는 공정 계획보다 리드타임(lead time, 조달 기간)을 고려하여 선행 발주해야 하며, 철근·레미콘 등 주요 자재는 주간 공정회의에서 다음 주 발주량을 확정합니다. 발주 지연은 공정 지연으로 직결되므로 통역 시 납기의 중요성을 강조해야 합니다.",
        "meaningVi": "Đặt hàng là việc đặt mua vật liệu, thiết bị từ nhà cung cấp, là công việc then chốt trong kế hoạch tiến độ và quản lý chi phí. Đơn đặt hàng ghi rõ: tên hàng, quy cách, số lượng, thời hạn giao, đơn giá. Nguyên tắc: so sánh báo giá từ 3 nhà. Đặt hàng trước thời gian cần dùng để tính lead time (thời gian cung ứng).",
        "context": "자재 관리, 공정 관리, 원가 관리",
        "culturalNote": "한국은 발주 프로세스가 매우 체계적이며, 발주 담당자는 자재 소요 계획(material requirement plan)을 공정표와 연동하여 작성하고, 구매팀 승인 후 발주합니다. 발주서는 법적 효력이 있는 계약 문서로 간주되어 발주 번호, 납기, 검수 기준이 명확히 기재됩니다. 납기 지연 시 위약금 조항이 포함되며, 발주 이력은 ERP에 자동 기록되어 추적 가능합니다. 베트남은 발주가 구두로 이루어지는 경우가 많고, 발주서 없이 전화나 문자로 주문하여 분쟁 발생 시 증거 자료가 부족합니다. 납기 개념이 약해 '빠른 시일 내'로만 표현하고 정확한 날짜를 명시하지 않아 공정 지연이 빈번합니다. 통역사는 발주서 작성의 법적 중요성과 납기 엄수의 필요성을 강조해야 합니다.",
        "commonMistakes": [
            {
                "mistake": "'발주'를 'mua'(사기)로만 번역",
                "correction": "'đặt hàng' (주문) 사용",
                "explanation": "발주는 계약 행위이며, 단순 구매와 법적 성격 다름"
            },
            {
                "mistake": "납기를 '빨리'로만 표현",
                "correction": "'ngày giao cụ thể' (구체적 납품일) 명시",
                "explanation": "모호한 납기는 공정 지연과 분쟁 유발"
            },
            {
                "mistake": "발주를 '말로 해도 된다'고 설명",
                "correction": "'đơn đặt hàng bằng văn bản' (서면 발주서) 필수 강조",
                "explanation": "구두 발주는 분쟁 시 입증 자료 없어 위험"
            }
        ],
        "examples": [
            {
                "ko": "다음 주 콘크리트 타설 물량이 200㎥이니, 오늘 중으로 레미콘을 발주하세요.",
                "vi": "Tuần sau đổ 200㎥ bê tông, hôm nay phải đặt hàng bê tông thương phẩm.",
                "situation": "onsite"
            },
            {
                "ko": "이 자재는 리드타임이 2주이니, 사용 예정일 기준 3주 전에 발주해야 합니다.",
                "vi": "Vật liệu này lead time 2 tuần, phải đặt hàng trước 3 tuần so với ngày dự kiến dùng.",
                "situation": "formal"
            },
            {
                "ko": "발주서에 검수 기준과 납기 위약금 조항을 명확히 기재해 주세요.",
                "vi": "Trong đơn đặt hàng ghi rõ tiêu chuẩn kiểm nhận và điều khoản phạt trễ hạn.",
                "situation": "formal"
            }
        ],
        "relatedTerms": ["발주서", "납기", "리드타임", "견적", "자재 소요 계획"]
    }
]

def main():
    # 파일 경로 설정
    file_path = os.path.join(
        os.path.dirname(os.path.abspath(__file__)),
        '..',
        'data',
        'terms',
        'construction.json'
    )

    # 기존 데이터 읽기
    with open(file_path, 'r', encoding='utf-8') as f:
        existing_data = json.load(f)

    print(f"기존 용어 수: {len(existing_data)}")

    # 새 용어 추가
    existing_data.extend(data)

    print(f"추가 후 용어 수: {len(existing_data)}")

    # 파일에 저장
    with open(file_path, 'w', encoding='utf-8') as f:
        json.dump(existing_data, f, ensure_ascii=False, indent=2)

    print(f"✅ {len(data)}개 용어가 추가되었습니다.")
    print("\n추가된 용어:")
    for term in data:
        print(f"  - {term['korean']} ({term['vietnamese']})")

if __name__ == "__main__":
    main()
