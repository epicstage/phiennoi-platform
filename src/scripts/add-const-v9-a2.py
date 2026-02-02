#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
건설 용어 추가 스크립트 - 건설보건/건강 테마
진폐증, 열사병, 동상, 근골격계질환, 유해물질, 석면조사, 납중독, 소음성난청, 건강검진, 응급처치
"""

import json
import os

# 건설보건/건강 테마 용어 10개 (Tier S 기준)
data = [
    {
        "slug": "benh-phoi-bui",
        "korean": "진폐증",
        "vietnamese": "bệnh phổi bụi",
        "hanja": "塵肺症",
        "hanjaReading": "진(티끌 진) + 폐(허파 폐) + 증(병 증)",
        "pronunciation": "벤 포이 부이",
        "meaningKo": "분진(석면, 규산, 석탄분 등)을 장기간 흡입하여 폐에 섬유화가 진행되는 직업성 호흡기 질환으로, 건설 현장에서 가장 치명적인 산업재해 중 하나입니다. 통역 시 '진폐증'은 'bệnh phổi bụi' 또는 'bệnh phổi do bụi nghề nghiệp'으로 표현하며, 단순한 '폐질환(bệnh phổi)'과 구분해야 합니다. 진폐증은 크게 석면폐증(asbestosis), 규폐증(silicosis), 탄광부 진폐증(coal worker's pneumoconiosis)으로 분류됩니다. 건설 현장에서는 절단·연마·파쇄·굴착 작업 시 발생하는 미세 분진을 흡입하여 발병하며, 잠복기가 10~20년으로 길어 초기 발견이 어렵습니다. 한국 「산업안전보건법」은 분진 작업장에 국소배기장치(LEV) 설치, 방진마스크 착용, 6개월마다 건강검진(흉부 X-ray)을 의무화하고 있습니다. 진폐증은 치료가 불가능하고 점진적으로 악화되므로 예방이 유일한 대책입니다. 분진 노출 기준은 호흡성 분진 1mg/m³ 이하(8시간 시간가중평균)이며, 초과 시 작업 중단 조치를 취해야 합니다.",
        "meaningVi": "Bệnh phổi bụi (bệnh phổi do bụi nghề nghiệp) là bệnh hô hấp nghề nghiệp do hít phải bụi (amiang, silic, than) trong thời gian dài gây xơ phổi, là tai nạn lao động chết người nhất ở công trường xây dựng. Có 3 loại: phổi amiang, phổi silic, phổi thợ mỏ. Thời gian ủ bệnh 10~20 năm. Không thể chữa khỏi, duy nhất là phòng ngừa. Chuẩn tiếp xúc bụi hô hấp ≤1mg/m³ (TWA 8h).",
        "context": "산업안전, 보건관리, 직업병",
        "culturalNote": "한국은 진폐증을 중대재해로 간주하며, 진폐 환자에게 국가가 의료비와 생활비를 지원하는 '진폐근로자보호법'을 운영합니다. 건설 현장은 분진 발생 작업(콘크리트 절단, 연마, 터널 굴착)에 습식 공법(물 분사), 국소배기장치, 방진마스크(KF94 이상)를 의무 적용하며, 감독기관이 분진 농도를 측정하여 기준 초과 시 작업 중지 명령을 내립니다. 베트남은 진폐증 예방 인식이 낮고, 분진 작업 시 마스크를 착용하지 않거나 일회용 마스크(KF80 이하)를 사용하는 경우가 많습니다. 국소배기장치 설치를 생략하고, 건강검진도 형식적으로 실시하여 진폐증 환자가 발생해도 직업병으로 인정받지 못하는 경우가 흔합니다. 한국 안전관리자가 방진마스크 착용을 강조하면 베트남 근로자는 '숨쉬기 불편하다', '더럽다'는 이유로 착용을 거부하는 경우가 있어, 통역 시 진폐증의 치명성(불치병, 호흡곤란, 사망)을 구체적으로 설명하여 예방 조치의 중요성을 전달해야 합니다.",
        "commonMistakes": [
            {
                "mistake": "'진폐증'을 'bệnh phổi'(일반 폐질환)로만 번역",
                "correction": "'bệnh phổi bụi' 또는 'bệnh phổi do bụi nghề nghiệp' 사용",
                "explanation": "진폐증은 분진에 의한 직업성 질환으로, 일반 폐질환과 구분 필수"
            },
            {
                "mistake": "'석면폐증', '규폐증'을 구분 없이 '진폐증'으로만 번역",
                "correction": "석면폐증='bệnh phổi amiang', 규폐증='bệnh phổi silic'로 구분",
                "explanation": "원인 물질(석면, 규산)에 따라 질병 유형이 다름"
            },
            {
                "mistake": "'방진마스크'를 'khẩu trang'(일반 마스크)로 번역",
                "correction": "'khẩu trang chống bụi' 또는 'mặt nạ chống bụi nghề nghiệp' 사용",
                "explanation": "방진마스크는 미세 분진을 차단하는 산업용 마스크로, 일반 마스크와 다름"
            }
        ],
        "examples": [
            {
                "ko": "콘크리트 절단 작업 시 반드시 방진마스크를 착용하여 진폐증을 예방하세요.",
                "vi": "Khi cắt bê tông nhất thiết đeo khẩu trang chống bụi để phòng bệnh phổi bụi.",
                "situation": "onsite"
            },
            {
                "ko": "진폐증은 잠복기가 길어 초기 발견이 어려우므로 정기 건강검진이 필수입니다.",
                "vi": "Bệnh phổi bụi có thời gian ủ bệnh dài khó phát hiện sớm nên khám sức khỏe định kỳ là bắt buộc.",
                "situation": "formal"
            },
            {
                "ko": "진폐증은 치료가 불가능하니까 분진 작업할 때 꼭 마스크 써야 해요.",
                "vi": "Bệnh phổi bụi không chữa được nên làm việc bụi nhất định phải đeo khẩu trang.",
                "situation": "informal"
            }
        ],
        "relatedTerms": [
            "석면폐증",
            "규폐증",
            "방진마스크",
            "국소배기장치",
            "분진농도"
        ]
    },
    {
        "slug": "say-nang",
        "korean": "열사병",
        "vietnamese": "say nắng",
        "hanja": "熱射病",
        "hanjaReading": "열(더울 열) + 사(쏠 사) + 병(병 병)",
        "pronunciation": "사이 낭",
        "meaningKo": "고온 환경에서 장시간 작업하여 체온 조절 기능이 마비되고 체온이 40°C 이상으로 상승하여 생명이 위험한 온열질환입니다. 통역 시 '열사병'은 'say nắng nặng' 또는 'sốc nhiệt'로 표현하며, 경미한 '열탈진(say nóng)'과 구분해야 합니다. 열탈진은 수분·염분 손실로 인한 피로·어지러움이고, 열사병은 체온 조절 실패로 인한 응급상황입니다. 열사병 증상은 의식 혼미, 경련, 피부 건조·뜨거움, 빠른 맥박이며, 방치 시 뇌손상·다장기부전으로 사망에 이릅니다. 한국 「산업안전보건법」은 폭염 시 옥외 작업에 그늘막 설치, 2시간마다 휴식, 염분 음료 제공, WBGT(습구흑구온도) 측정을 의무화하고 있습니다. WBGT 31°C 이상 시 작업 시간을 단축(25%↓)하거나 중지하며, 열사병 의심 시 즉시 119 신고, 그늘로 이동, 몸을 식히고 의식이 있으면 물을 마시게 합니다(의식 없으면 물 금지). 열사병은 골든타임이 30분 이내이므로 신속한 응급조치가 생명을 좌우합니다.",
        "meaningVi": "Say nắng nặng (sốc nhiệt) là bệnh nhiệt nghề nghiệp do làm việc lâu trong môi trường nóng, chức năng điều hòa thân nhiệt bị tê liệt, thân nhiệt tăng trên 40°C, nguy hiểm tính mạng. Khác với say nóng (mệt, chóng mặt), say nắng nặng là cấp cứu. Triệu chứng: mê sảng, co giật, da khô nóng, mạch nhanh. Bỏ mặc gây tổn thương não, suy đa cơ quan, tử vong. Thời gian vàng 30 phút.",
        "context": "산업안전, 보건관리, 응급처치",
        "culturalNote": "한국은 매년 7~8월 폭염 기간에 건설 현장 열사병 사고가 다발하며, 고용노동부가 '폭염 특별감독'을 실시하여 그늘막, 휴게시설, 염분 음료 비치 여부를 점검합니다. 현장에는 WBGT 측정기를 비치하고, 기준 초과 시 작업 시간을 단축하거나 중지하며, 열사병 의심 시 즉시 119 신고와 응급조치를 취합니다. 근로자에게 '아이스조끼(쿨링 베스트)', 쿨링 타올을 제공하고, 휴게실에 에어컨·선풍기를 설치합니다. 베트남은 연중 고온 환경이지만 열사병 예방 의식이 낮고, 그늘막 없이 직사광선 아래에서 작업하는 경우가 많습니다. 휴식 시간을 지키지 않고, 물 대신 커피·차를 마시는 경우도 흔합니다(카페인은 탈수 촉진). 열사병 발생 시 응급조치 없이 방치하거나 잘못된 조치(의식 없는 환자에게 물 먹이기)를 하는 경우가 있어, 통역 시 열사병의 치명성과 정확한 응급조치 방법(그늘 이동, 119 신고, 몸 식히기, 의식 확인 후 물 제공)을 구체적으로 전달해야 합니다.",
        "commonMistakes": [
            {
                "mistake": "'열사병'을 'say nắng'(가벼운 일사병)로만 번역",
                "correction": "'say nắng nặng' 또는 'sốc nhiệt' 사용",
                "explanation": "열사병은 생명이 위험한 응급상황으로, 경미한 일사병과 구분 필수"
            },
            {
                "mistake": "'열탈진'과 '열사병'을 구분 없이 번역",
                "correction": "열탈진='say nóng'(피로), 열사병='say nắng nặng'(응급)으로 구분",
                "explanation": "증상과 위험도가 다르므로 혼동 시 응급조치 지연"
            },
            {
                "mistake": "'WBGT'를 번역 없이 영문 약어만 사용",
                "correction": "'chỉ số nhiệt độ cầu ướt cầu đen' 또는 'WBGT (Wet Bulb Globe Temperature)' 병기",
                "explanation": "베트남 근로자는 WBGT 용어에 익숙하지 않음"
            }
        ],
        "examples": [
            {
                "ko": "WBGT가 31°C를 넘으면 작업 시간을 25% 단축하고, 2시간마다 휴식하세요.",
                "vi": "WBGT vượt 31°C thì giảm thời gian làm việc 25%, nghỉ mỗi 2 giờ.",
                "situation": "onsite"
            },
            {
                "ko": "열사병 의심 시 즉시 119에 신고하고, 그늘로 옮겨 몸을 식히세요.",
                "vi": "Nghi say nắng nặng lập tức gọi 119, chuyển đến bóng râm, làm mát cơ thể.",
                "situation": "formal"
            },
            {
                "ko": "열사병은 30분 안에 처치해야 살 수 있으니까 빨리 대응해야 해요.",
                "vi": "Say nắng nặng phải xử lý trong 30 phút mới cứu được nên phải phản ứng nhanh.",
                "situation": "informal"
            }
        ],
        "relatedTerms": [
            "열탈진",
            "WBGT",
            "폭염특보",
            "응급처치",
            "그늘막"
        ]
    },
    {
        "slug": "dong-thuong",
        "korean": "동상",
        "vietnamese": "đông thương",
        "hanja": "凍傷",
        "hanjaReading": "동(얼 동) + 상(상할 상)",
        "pronunciation": "동 투엉",
        "meaningKo": "추운 환경에서 장시간 노출되어 피부 조직이 동결되어 손상되는 저체온 질환으로, 주로 손가락·발가락·귀·코 등 말단 부위에 발생합니다. 통역 시 '동상'은 'đông thương' 또는 'tổn thương do lạnh'로 표현하며, 단순한 '추위(lạnh)'와 구분해야 합니다. 동상은 경증(1~2도)과 중증(3~4도)으로 구분되며, 경증은 피부 창백·저림·통증이고, 중증은 조직 괴사로 절단이 필요할 수 있습니다. 한국은 겨울철 옥외 작업 시 방한복, 방한장갑, 방한화, 귀마개, 마스크를 착용하고, 난방 시설이 있는 휴게실을 설치하며, 1시간마다 10분 이상 휴식을 취하도록 합니다. 동상 의심 시 즉시 따뜻한 물(37~40°C)에 담가 서서히 녹이며, 뜨거운 물(60°C 이상) 또는 불로 직접 가열하면 조직 손상이 악화됩니다. 동상 부위를 비비거나 마사지하는 것도 금지이며, 즉시 의료기관으로 이송해야 합니다. 동상 예방을 위해 땀에 젖은 옷은 즉시 갈아입고, 술을 마시지 않으며(혈관 수축), 충분한 칼로리를 섭취해야 합니다.",
        "meaningVi": "Đông thương (tổn thương do lạnh) là bệnh hạ thân nhiệt do tiếp xúc lâu với môi trường lạnh, mô da đông cứng bị tổn thương, chủ yếu ở ngón tay, ngón chân, tai, mũi. Chia độ nhẹ (1~2 độ: da nhợt, tê, đau) và độ nặng (3~4 độ: hoại tử mô, có thể cắt cụt). Xử lý: ngâm nước ấm (37~40°C) từ từ, cấm nước sôi hoặc lửa. Cấm chà xát, massage. Phải chuyển viện.",
        "context": "산업안전, 보건관리, 동절기 작업",
        "culturalNote": "한국은 겨울철(-10°C 이하) 옥외 작업이 많고, 동상 사고 예방을 위해 '한파 특별감독'을 실시합니다. 현장에는 온풍기, 난로, 온수기를 설치하고, 동절기 작업 시간을 단축(오전 10시~오후 3시)하며, 혹한 시(-20°C 이하) 작업을 중지합니다. 방한복·장갑은 보온성(CLO 값) 기준을 충족해야 하며, 젖은 장갑은 즉시 교체합니다. 베트남은 아열대 기후로 동상 개념이 생소하고, 겨울철에도 기온이 10~15°C로 따뜻하여 방한 장비를 착용하지 않는 경우가 많습니다. 베트남 근로자가 한국 겨울 현장에 투입되면 추위에 익숙하지 않아 동상 위험이 높으며, 동상 발생 시 응급조치 방법을 모르는 경우가 많습니다. 한국 안전관리자가 방한복 착용을 강조하면 베트남 근로자는 '불편하다', '움직이기 어렵다'는 이유로 거부하는 경우가 있어, 통역 시 동상의 위험성(조직 괴사, 절단)과 예방 조치(방한복, 휴식, 따뜻한 음료)를 구체적으로 전달해야 합니다.",
        "commonMistakes": [
            {
                "mistake": "'동상'을 'lạnh'(추위)로만 번역",
                "correction": "'đông thương' 또는 'tổn thương do lạnh' 사용",
                "explanation": "동상은 추위에 의한 조직 손상으로, 단순한 '춥다'와 구분 필수"
            },
            {
                "mistake": "동상 응급조치를 '뜨거운 물로 녹인다'로 번역",
                "correction": "'ngâm nước ấm (37~40°C) từ từ làm tan' 사용, 뜨거운 물 금지",
                "explanation": "뜨거운 물은 조직 손상을 악화시키므로 따뜻한 물(미온수)로 서서히 녹여야 함"
            },
            {
                "mistake": "'방한복'을 'áo ấm'(따뜻한 옷)로 일반화",
                "correction": "'quần áo chống rét' 또는 'đồ bảo hộ mùa đông' 사용",
                "explanation": "방한복은 보온 기준(CLO 값)을 충족하는 산업용 보호구"
            }
        ],
        "examples": [
            {
                "ko": "겨울철 옥외 작업 시 방한장갑과 방한화를 착용하여 동상을 예방하세요.",
                "vi": "Làm việc ngoài trời mùa đông đeo găng tay chống rét và giày chống rét để phòng đông thương.",
                "situation": "onsite"
            },
            {
                "ko": "동상 의심 시 따뜻한 물(37~40°C)에 담가 서서히 녹이고, 뜨거운 물은 금지입니다.",
                "vi": "Nghi đông thương ngâm nước ấm (37~40°C) từ từ làm tan, cấm dùng nước sôi.",
                "situation": "formal"
            },
            {
                "ko": "동상 걸리면 손가락 잘릴 수도 있으니까 꼭 방한복 입어야 해요.",
                "vi": "Đông thương có thể cắt mất ngón tay nên nhất định phải mặc quần áo chống rét.",
                "situation": "informal"
            }
        ],
        "relatedTerms": [
            "저체온증",
            "방한복",
            "방한장갑",
            "한파특보",
            "응급처치"
        ]
    },
    {
        "slug": "benh-co-xuong-khop",
        "korean": "근골격계질환",
        "vietnamese": "bệnh cơ xương khớp",
        "hanja": "筋骨格系疾患",
        "hanjaReading": "근(힘줄 근) + 골(뼈 골) + 격(격식 격) + 계(이을 계) + 질(병 질) + 환(근심 환)",
        "pronunciation": "벤 커 슈엉 콥",
        "meaningKo": "반복적인 동작, 무리한 힘, 부적절한 자세로 인해 근육·뼈·관절·인대·신경 등이 손상되는 직업성 질환의 총칭입니다. 통역 시 '근골격계질환'은 'bệnh cơ xương khớp' 또는 'rối loạn cơ xương' 으로 표현하며, '근골격계부담작업'과 함께 설명해야 합니다. 건설 현장에서는 중량물 취급(철근, 거푸집, 자재 운반), 반복 작업(타일 붙이기, 철근 결속), 부적절한 자세(쪼그려 앉기, 허리 굽히기)로 인해 요통, 경견완장애(목·어깨·팔 통증), 수근관증후군(손목 통증) 등이 다발합니다. 한국 「산업안전보건법」은 근골격계부담작업에 대해 3년마다 유해요인 조사를 실시하고, 위험 요인 발견 시 개선 조치(보조기구 도입, 작업 순환, 휴식 시간 확보)를 취하도록 의무화하고 있습니다. 근골격계질환 예방을 위해 작업 전 스트레칭, 중량물 운반 시 2인 1조, 보조기구(지게차, 리프트) 사용, 작업대 높이 조절, 방진장갑·무릎보호대 착용 등이 필요합니다. 근골격계질환은 초기 증상(피로, 통증)을 방치하면 만성화되어 업무 복귀가 어려워지므로, 조기 발견과 조치가 중요합니다.",
        "meaningVi": "Bệnh cơ xương khớp (rối loạn cơ xương) là tổng hợp bệnh nghề nghiệp do động tác lặp đi lặp lại, lực quá mức, tư thế không hợp lý gây tổn thương cơ, xương, khớp, dây chằng, thần kinh. Ở công trường: xử lý vật nặng, công việc lặp lại, tư thế sai gây đau lưng, vai gáy cánh tay, ống cổ tay. Phòng ngừa: giãn cơ trước làm, 2 người khiêng nặng, dùng xe nâng, điều chỉnh chiều cao bàn làm, đeo găng tay đầu gối.",
        "context": "산업안전, 보건관리, 인간공학",
        "culturalNote": "한국은 근골격계질환을 산재 승인 1위 질병(전체 산재의 60% 이상)으로 간주하며, 정부가 예방 프로그램(작업 개선, 보조기구 지원)에 막대한 예산을 투입하고 있습니다. 건설 현장은 근골격계부담작업이 많아 작업 전 5분 스트레칭을 의무화하고, 중량물 운반 시 기계 장비(지게차, 호이스트)를 사용하며, 인력 운반이 불가피할 때는 2인 1조로 작업합니다. 요통 예방을 위해 허리 보호대를 착용하고, 작업대 높이를 조절하여 허리 굽힘을 최소화합니다. 베트남은 근골격계질환 개념이 생소하고, '아프면 쉬면 된다'는 인식이 강해 예방 조치를 소홀히 합니다. 중량물을 혼자 들거나, 쪼그려 앉아 장시간 작업하는 경우가 많으며, 스트레칭이나 보조기구 사용을 '시간 낭비'로 여기는 경향이 있습니다. 한국 안전관리자가 스트레칭과 2인 1조 작업을 강조하면 베트남 근로자는 '번거롭다', '혼자 할 수 있다'는 이유로 거부하는 경우가 있어, 통역 시 근골격계질환의 장기적 피해(만성 통증, 업무 불능)와 예방 조치의 효과를 구체적으로 전달해야 합니다.",
        "commonMistakes": [
            {
                "mistake": "'근골격계질환'을 'đau cơ'(근육통)로만 번역",
                "correction": "'bệnh cơ xương khớp' 또는 'rối loạn cơ xương nghề nghiệp' 사용",
                "explanation": "근골격계질환은 근육·뼈·관절을 포함하는 직업병으로, 단순 근육통과 구분"
            },
            {
                "mistake": "'요통'을 'đau lưng'(일반 허리 통증)로만 번역",
                "correction": "'đau lưng nghề nghiệp' 또는 'tổn thương cột sống do công việc' 사용",
                "explanation": "직업성 요통은 작업으로 인한 척추 손상으로, 일반 요통과 구분 필요"
            },
            {
                "mistake": "'스트레칭'을 'vận động'(운동)으로 일반화",
                "correction": "'giãn cơ' 또는 'kéo giãn cơ bắp' 사용",
                "explanation": "스트레칭은 근육을 늘리는 특정 동작으로, 일반 운동과 다름"
            }
        ],
        "examples": [
            {
                "ko": "중량물 운반 시 2인 1조로 작업하여 근골격계질환을 예방하세요.",
                "vi": "Khiêng vật nặng làm theo nhóm 2 người để phòng bệnh cơ xương khớp.",
                "situation": "onsite"
            },
            {
                "ko": "작업 전 5분 스트레칭을 실시하여 요통과 경견완장애를 예방합니다.",
                "vi": "Giãn cơ 5 phút trước làm để phòng đau lưng và vai gáy cánh tay.",
                "situation": "formal"
            },
            {
                "ko": "근골격계질환은 초기에 방치하면 만성화돼서 일 못하게 돼요.",
                "vi": "Bệnh cơ xương khớp bỏ mặc ban đầu thành mạn tính không làm việc được.",
                "situation": "informal"
            }
        ],
        "relatedTerms": [
            "요통",
            "경견완장애",
            "수근관증후군",
            "인간공학",
            "스트레칭"
        ]
    },
    {
        "slug": "chat-doc-hai",
        "korean": "유해물질",
        "vietnamese": "chất độc hại",
        "hanja": "有害物質",
        "hanjaReading": "유(있을 유) + 해(해 해) + 물(물건 물) + 질(바탕 질)",
        "pronunciation": "쩟 독 하이",
        "meaningKo": "인체에 해로운 화학물질의 총칭으로, 건설 현장에서는 석면, 납, 유기용제, 중금속, 분진 등이 해당됩니다. 통역 시 '유해물질'은 'chất độc hại' 또는 'hóa chất nguy hiểm'로 표현하며, '위험물(chất nguy hiểm)'과 구분해야 합니다. 위험물은 폭발·화재 위험이 있는 물질(유류, 가스)이고, 유해물질은 건강에 해로운 물질입니다. 건설 현장 주요 유해물질은 석면(단열재, 슬레이트), 납(구조물 도료), 유기용제(페인트, 접착제), 규산(콘크리트 분진), 크롬·니켈(용접 흄) 등이며, 노출 시 암, 중독, 호흡기 질환을 유발합니다. 한국 「산업안전보건법」은 유해물질 취급 시 물질안전보건자료(MSDS) 비치, 보호구 착용, 환기·배기 장치 설치, 특수건강검진(6개월~1년마다)을 의무화하고 있습니다. 석면·납 등 특정 유해물질은 작업 전 사전조사(석면조사, 납 함량 측정)를 실시하고, 전문 업체가 제거·처리해야 하며, 무단 작업 시 형사처벌(3년 이하 징역 또는 3000만원 이하 벌금)을 받습니다.",
        "meaningVi": "Chất độc hại (hóa chất nguy hiểm) là tổng hợp hóa chất có hại cho cơ thể người, ở công trường gồm amiang, chì, dung môi hữu cơ, kim loại nặng, bụi. Khác với chất nguy hiểm (nổ cháy), chất độc hại gây hại sức khỏe. Chất chính: amiang, chì (sơn), dung môi (sơn keo), silic (bụi bê tông), crom niken (khói hàn). Tiếp xúc gây ung thư, nhiễm độc, bệnh hô hấp. Phải có MSDS, đeo bảo hộ, thông gió, khám đặc biệt 6 tháng~1 năm.",
        "context": "산업안전, 보건관리, 화학물질 관리",
        "culturalNote": "한국은 유해물질 관리를 엄격히 시행하며, 석면·납·중금속 사용을 법으로 규제하고 있습니다. 건설 현장은 유해물질 취급 전 MSDS를 근로자에게 교육하고, 보호구(방독마스크, 보호복, 장갑)를 착용하며, 작업 중 환기·배기 장치를 가동하고, 작업 후 세척 시설에서 샤워합니다. 석면·납 제거 작업은 전문 업체가 밀폐 공간에서 실시하고, 폐기물은 지정 장소에 특별 관리합니다. 베트남은 유해물질 개념이 약하고, MSDS를 비치하지 않거나 근로자가 읽지 못하는 경우가 많습니다. 석면·납이 포함된 자재를 사전조사 없이 철거하고, 보호구 없이 맨손으로 작업하는 경우가 흔하며, 유기용제를 밀폐 공간에서 환기 없이 사용하여 중독 사고가 발생합니다. 한국 안전관리자가 MSDS와 보호구 착용을 강조하면 베트남 근로자는 '귀찮다', '숨쉬기 불편하다'는 이유로 거부하는 경우가 있어, 통역 시 유해물질의 장기 피해(암, 중독, 불임)와 법적 의무(형사처벌)를 구체적으로 전달해야 합니다.",
        "commonMistakes": [
            {
                "mistake": "'유해물질'을 'chất nguy hiểm'(위험물)로만 번역",
                "correction": "'chất độc hại' 또는 'hóa chất độc hại sức khỏe' 사용",
                "explanation": "위험물은 폭발·화재 위험, 유해물질은 건강 위해로 구분 필요"
            },
            {
                "mistake": "'MSDS'를 번역 없이 영문 약어만 사용",
                "correction": "'phiếu an toàn hóa chất' 또는 'MSDS (Material Safety Data Sheet)' 병기",
                "explanation": "베트남 근로자는 MSDS 용어에 익숙하지 않음"
            },
            {
                "mistake": "'방독마스크'를 'khẩu trang'(일반 마스크)로 번역",
                "correction": "'mặt nạ phòng độc' 또는 'khẩu trang chống hóa chất' 사용",
                "explanation": "방독마스크는 유해가스·증기를 차단하는 산업용 마스크"
            }
        ],
        "examples": [
            {
                "ko": "유해물질 작업 전 MSDS를 확인하고, 방독마스크와 보호복을 착용하세요.",
                "vi": "Trước làm việc chất độc hại kiểm tra MSDS, đeo mặt nạ phòng độc và quần áo bảo hộ.",
                "situation": "onsite"
            },
            {
                "ko": "석면과 납은 특정 유해물질이므로 전문 업체가 제거해야 합니다.",
                "vi": "Amiang và chì là chất độc hại đặc biệt nên đơn vị chuyên môn phải tháo dỡ.",
                "situation": "formal"
            },
            {
                "ko": "유해물질은 암이나 중독을 일으킬 수 있으니까 꼭 보호구 써야 해요.",
                "vi": "Chất độc hại có thể gây ung thư hoặc nhiễm độc nên nhất định phải đeo bảo hộ.",
                "situation": "informal"
            }
        ],
        "relatedTerms": [
            "석면",
            "납",
            "MSDS",
            "방독마스크",
            "특수건강검진"
        ]
    },
    {
        "slug": "khao-sat-amiang",
        "korean": "석면조사",
        "vietnamese": "khảo sát amiang",
        "hanja": "石綿調査",
        "hanjaReading": "석(돌 석) + 면(솜 면) + 조(살필 조) + 사(조사할 사)",
        "pronunciation": "카오 삿 아미앙",
        "meaningKo": "건축물·시설물을 철거·해체하기 전에 석면 함유 여부와 종류·함량·위치를 조사하는 법정 의무 절차입니다. 통역 시 '석면조사'는 'khảo sát amiang' 또는 'điều tra amiang'으로 표현하며, '석면 제거(tháo dỡ amiang)'와 구분해야 합니다. 석면은 1급 발암물질로, 건축물 단열재·슬레이트·천장재·배관 보온재에 널리 사용되었으며, 흡입 시 석면폐증·폐암·중피종을 유발합니다. 한국은 「석면안전관리법」에 따라 철거·해체 전 석면조사를 의무화하고 있으며, 조사 기관은 환경부 지정 업체만 가능합니다. 조사는 (1) 설계도면 검토, (2) 육안 조사, (3) 시료 채취(벌크 샘플링), (4) 실험실 분석(편광현미경, 전자현미경)으로 진행되며, 조사 결과에 따라 석면 제거 계획을 수립합니다. 석면 함량이 1% 이상이면 '석면 함유 자재'로 간주하며, 전문 업체가 밀폐 공간에서 습식 제거 후 지정 폐기물로 처리합니다. 무단 철거 시 7년 이하 징역 또는 1억원 이하 벌금에 처해집니다.",
        "meaningVi": "Khảo sát amiang (điều tra amiang) là thủ tục bắt buộc theo pháp luật điều tra có hay không amiang, loại, hàm lượng, vị trí trước khi phá dỡ công trình. Amiang là chất gây ung thư hạng 1, dùng trong vật liệu cách nhiệt, tấm lợp, trần, ống. Hít vào gây bệnh phổi amiang, ung thư phổi, u trung biểu mô. Quy trình: (1) xem bản vẽ, (2) khảo sát mắt, (3) lấy mẫu, (4) phân tích phòng thí nghiệm. Hàm lượng ≥1% là vật liệu chứa amiang, đơn vị chuyên môn tháo dỡ ướt trong không gian kín, xử lý chất thải đặc biệt.",
        "context": "석면관리, 환경안전, 철거공사",
        "culturalNote": "한국은 석면을 '조용한 살인자(silent killer)'로 간주하며, 정부가 석면 관리에 엄격한 규제를 시행하고 있습니다. 1990년대까지 건축물에 석면이 광범위하게 사용되었고, 현재 노후 건축물 철거 시 석면조사가 필수입니다. 조사 비용은 건축물 규모에 따라 50만~200만원이며, 조사 기간은 1~2주입니다. 석면 제거 비용은 면적당 1만~3만원/m²로, 소규모 건물도 수백만원이 소요됩니다. 베트남은 석면 사용 규제가 약하고, 현재도 슬레이트·석면 시멘트 제품을 사용하는 경우가 많습니다. 철거 전 석면조사를 실시하지 않고, 석면 함유 자재를 일반 폐기물로 처리하는 경우가 흔합니다. 한국 발주처가 석면조사를 요구하면 베트남 시공사는 '비용이 많이 든다', '베트남에는 없다'는 이유로 거부하는 경우가 있어, 통역 시 석면의 치명성(불치병, 잠복기 20년)과 법적 의무(형사처벌)를 구체적으로 전달하여 조사의 필요성을 설득해야 합니다.",
        "commonMistakes": [
            {
                "mistake": "'석면조사'를 'kiểm tra amiang'(석면 점검)으로만 번역",
                "correction": "'khảo sát amiang' 또는 'điều tra amiang chuyên môn' 사용",
                "explanation": "석면조사는 법정 절차로, 시료 채취·분석을 포함하는 전문 조사"
            },
            {
                "mistake": "'석면 제거'와 '석면조사'를 동일한 것으로 설명",
                "correction": "석면조사='khảo sát amiang'(사전조사), 석면 제거='tháo dỡ amiang'(실제 작업)으로 구분",
                "explanation": "조사는 제거 전 필수 절차로, 순서와 목적이 다름"
            },
            {
                "mistake": "'석면폐증', '중피종'을 일반 '폐암'으로만 번역",
                "correction": "석면폐증='bệnh phổi amiang', 중피종='u trung biểu mô', 폐암='ung thư phổi'로 구분",
                "explanation": "석면으로 인한 질병은 종류가 다르며 모두 치명적"
            }
        ],
        "examples": [
            {
                "ko": "철거 전 석면조사를 실시하여 석면 함유 여부를 확인하세요.",
                "vi": "Trước phá dỡ tiến hành khảo sát amiang để xác nhận có chứa amiang không.",
                "situation": "formal"
            },
            {
                "ko": "석면 함량이 1% 이상이면 전문 업체가 밀폐 공간에서 제거해야 합니다.",
                "vi": "Hàm lượng amiang ≥1% thì đơn vị chuyên môn phải tháo dỡ trong không gian kín.",
                "situation": "formal"
            },
            {
                "ko": "석면 무단 철거하면 7년 징역받을 수 있으니까 조사 꼭 해야 해요.",
                "vi": "Tự ý phá dỡ amiang có thể bị 7 năm tù nên nhất định phải khảo sát.",
                "situation": "informal"
            }
        ],
        "relatedTerms": [
            "석면",
            "석면폐증",
            "중피종",
            "석면제거",
            "지정폐기물"
        ]
    },
    {
        "slug": "nhiem-doc-chi",
        "korean": "납중독",
        "vietnamese": "nhiễm độc chì",
        "hanja": "鉛中毒",
        "hanjaReading": "납(납 납) + 중(가운데 중) + 독(독 독)",
        "pronunciation": "니엠 독 치",
        "meaningKo": "납(Pb) 또는 납 화합물을 흡입·섭취하여 체내에 축적되어 발생하는 중독 질환으로, 신경계·혈액·신장에 치명적인 손상을 입힙니다. 통역 시 '납중독'은 'nhiễm độc chì' 또는 'ngộ độc chì'로 표현하며, '납 노출(tiếp xúc chì)'과 구분해야 합니다. 건설 현장에서는 구조물 도료(방청페인트), 납 배관, 납땜 작업, 구건물 철거 시 납 분진·흄(fume)에 노출되어 납중독이 발생합니다. 납중독 증상은 두통, 복통, 피로, 빈혈, 신경 마비이며, 만성 노출 시 뇌손상, 신부전, 불임을 유발합니다. 한국 「산업안전보건법」은 납 작업 시 혈중 납 농도 측정(6개월마다), 호흡용 보호구 착용, 작업장 환기, 세척 시설 설치를 의무화하고 있으며, 혈중 납 농도가 40μg/dL 이상이면 작업 전환, 60μg/dL 이상이면 작업 금지 조치를 취합니다. 납 작업 후에는 반드시 샤워하고 작업복을 세탁하며, 작업장에서 음식 섭취·흡연을 금지합니다(납 입으로 섭취 방지). 납 함유 도료는 무단 제거 금지이며, 전문 업체가 밀폐 공간에서 습식 제거해야 합니다.",
        "meaningVi": "Nhiễm độc chì (ngộ độc chì) là bệnh nhiễm độc do hít hoặc nuốt chì (Pb) hoặc hợp chất chì tích tụ trong cơ thể, gây tổn thương chết người cho thần kinh, máu, thận. Ở công trường: tiếp xúc bụi khói chì từ sơn chống gỉ, ống chì, hàn chì, phá dỡ công trình cũ. Triệu chứng: đau đầu, đau bụng, mệt, thiếu máu, liệt thần kinh. Tiếp xúc mạn tính gây tổn thương não, suy thận, vô sinh. Đo nồng độ chì trong máu 6 tháng/lần, ≥40μg/dL chuyển việc, ≥60μg/dL cấm làm.",
        "context": "산업안전, 보건관리, 중금속 관리",
        "culturalNote": "한국은 납중독을 중대 직업병으로 간주하며, 정부가 납 작업장을 특별 관리합니다. 납 작업 근로자는 6개월마다 혈중 납 농도를 측정하고, 기준 초과 시 즉시 작업 전환 조치를 취하며, 치료비를 산재보험에서 지원합니다. 납 함유 도료는 1990년대 이전 건축물에 광범위하게 사용되었고, 현재 철거 시 납 함량 측정을 의무화하고 있습니다. 납 작업장은 별도의 세척 시설과 탈의실을 설치하고, 작업복은 외부 반출 금지이며 현장에서 세탁합니다. 베트남은 납중독 개념이 약하고, 납 함유 도료를 사전조사 없이 철거하는 경우가 많습니다. 납 작업 후 손을 씻지 않고 식사하거나, 작업복을 집으로 가져가 세탁하는 경우가 흔하며(가족 2차 오염), 혈중 납 농도 측정을 하지 않아 만성 납중독 환자가 많습니다. 한국 안전관리자가 납 작업 시 보호구 착용과 샤워를 강조하면 베트남 근로자는 '귀찮다', '시간 걸린다'는 이유로 거부하는 경우가 있어, 통역 시 납중독의 장기 피해(뇌손상, 불임)와 가족 2차 오염 위험을 구체적으로 전달해야 합니다.",
        "commonMistakes": [
            {
                "mistake": "'납중독'을 'nhiễm độc'(일반 중독)로만 번역",
                "correction": "'nhiễm độc chì' 또는 'ngộ độc chì' 사용",
                "explanation": "납중독은 중금속 중독의 특정 유형으로, 일반 중독과 구분 필요"
            },
            {
                "mistake": "'혈중 납 농도'를 'lượng chì trong máu'로 직역",
                "correction": "'nồng độ chì trong máu' 사용",
                "explanation": "'nồng độ(농도)'가 의학 용어로 적합하며, 'lượng(양)'은 부정확"
            },
            {
                "mistake": "납 작업 후 세척 필요성을 설명 없이 번역",
                "correction": "납이 손·피부에 남아 입으로 섭취될 위험을 강조",
                "explanation": "베트남 근로자는 납이 손에 묻어도 위험하지 않다고 오해하는 경우 많음"
            }
        ],
        "examples": [
            {
                "ko": "납 도료 제거 작업 시 방독마스크를 착용하고, 작업 후 샤워하세요.",
                "vi": "Khi tháo dỡ sơn chì đeo mặt nạ phòng độc, sau làm việc tắm rửa.",
                "situation": "onsite"
            },
            {
                "ko": "혈중 납 농도가 40μg/dL 이상이면 작업 전환이 필요합니다.",
                "vi": "Nồng độ chì trong máu ≥40μg/dL thì cần chuyển công việc.",
                "situation": "formal"
            },
            {
                "ko": "납중독은 뇌손상과 불임을 일으킬 수 있으니까 꼭 보호구 써야 해요.",
                "vi": "Nhiễm độc chì có thể gây tổn thương não và vô sinh nên nhất định phải đeo bảo hộ.",
                "situation": "informal"
            }
        ],
        "relatedTerms": [
            "중금속",
            "혈중납농도",
            "방독마스크",
            "습식제거",
            "특수건강검진"
        ]
    },
    {
        "slug": "diec-tai-do-on",
        "korean": "소음성난청",
        "vietnamese": "điếc tai do ồn",
        "hanja": "騷音性難聽",
        "hanjaReading": "소(시끄러울 소) + 음(소리 음) + 성(성품 성) + 난(어려울 난) + 청(들을 청)",
        "pronunciation": "지엑 타이 조 온",
        "meaningKo": "85dB 이상의 소음에 장기간 노출되어 내이(內耳)의 청각세포가 손상되어 발생하는 비가역적 청력 손실입니다. 통역 시 '소음성난청'은 'điếc tai do ồn' 또는 'giảm thính lực do tiếng ồn'으로 표현하며, 일시적인 '청력 저하(giảm thính lực tạm thời)'와 구분해야 합니다. 건설 현장에서는 항타기, 파쇄기, 절단기, 압축기 등 고소음 장비 사용으로 소음성난청이 다발하며, 한번 손상된 청각세포는 재생되지 않아 영구적 난청이 됩니다. 한국 「산업안전보건법」은 85dB 이상 소음 작업장에 귀마개·귀덮개 착용, 6개월마다 청력 검사, 소음 저감 조치(방음벽, 소음기 부착)를 의무화하고 있습니다. 90dB 이상 작업장은 작업 시간을 제한(8시간→4시간)하고, 소음원에서 가능한 멀리 떨어져 작업합니다. 소음 수준은 소음계(sound level meter)로 측정하며, 85dB은 1m 거리에서 고함 수준, 90dB은 지하철 소음, 100dB은 착암기 소음, 120dB은 고통 수준입니다. 소음성난청은 초기 증상(이명, 고음역 청력 저하)을 자각하기 어려워 정기 검진이 중요하며, 예방이 유일한 대책입니다.",
        "meaningVi": "Điếc tai do ồn (giảm thính lực do tiếng ồn) là mất thính lực không hồi phục do tiếp xúc lâu với tiếng ồn ≥85dB, tế bào thính giác bị tổn thương. Ở công trường: máy đóng cọc, máy phá, máy cắt, máy nén gây điếc tai nhiều. Tế bào thính giác tổn thương không tái sinh, điếc vĩnh viễn. ≥85dB đeo nút tai/chụp tai, khám thính lực 6 tháng/lần. ≥90dB giảm thời gian làm (8h→4h). 85dB=la hét 1m, 90dB=tàu điện ngầm, 100dB=máy khoan đá, 120dB=đau.",
        "context": "산업안전, 보건관리, 소음 관리",
        "culturalNote": "한국은 소음성난청을 산재 승인 상위 질병(진폐증 다음)으로 간주하며, 정부가 소음 작업장을 특별 관리합니다. 건설 현장은 소음 측정을 정기적으로 실시하고, 기준 초과 시 방음벽·방음 덮개를 설치하거나 장비를 소음이 적은 모델로 교체합니다. 근로자에게 귀마개(삽입형, 폼 타입) 또는 귀덮개(헤드셋형)를 지급하고, 착용 교육을 실시합니다. 소음 작업 근로자는 6개월마다 순음청력검사(pure tone audiometry)를 받으며, 청력 저하 발견 시 작업 전환 조치를 취합니다. 베트남은 소음성난청 개념이 약하고, 귀마개를 지급하지 않거나 근로자가 착용을 거부하는 경우가 많습니다. '조금 시끄럽지만 견딜 만하다', '귀마개 끼면 대화가 안 들린다'는 이유로 미착용하며, 청력 검사도 형식적으로 실시하여 난청 환자가 발견되지 않습니다. 한국 안전관리자가 귀마개 착용을 강조하면 베트남 근로자는 '불편하다', '귀가 간지럽다'는 이유로 거부하는 경우가 있어, 통역 시 소음성난청의 비가역성(영구 난청, 치료 불가)과 일상생활 피해(대화 불가, 보청기 필요)를 구체적으로 전달해야 합니다.",
        "commonMistakes": [
            {
                "mistake": "'소음성난청'을 'điếc tai'(일반 난청)로만 번역",
                "correction": "'điếc tai do ồn' 또는 'giảm thính lực do tiếng ồn nghề nghiệp' 사용",
                "explanation": "소음성난청은 직업성 질환으로, 일반 난청과 구분 필요"
            },
            {
                "mistake": "'귀마개'와 '귀덮개'를 구분 없이 번역",
                "correction": "귀마개='nút tai' 또는 'bịt tai', 귀덮개='chụp tai' 또는 'bịt tai dạng vòng' 사용",
                "explanation": "귀마개는 삽입형, 귀덮개는 헤드셋형으로 형태와 착용법이 다름"
            },
            {
                "mistake": "소음 수준(dB)을 설명 없이 숫자만 제시",
                "correction": "85dB='la hét 1m', 90dB='tàu điện ngầm', 100dB='máy khoan' 등 비유 병기",
                "explanation": "베트남 근로자는 dB 단위에 익숙하지 않아 체감 비유 필요"
            }
        ],
        "examples": [
            {
                "ko": "85dB 이상 소음 작업 시 귀마개를 착용하여 소음성난청을 예방하세요.",
                "vi": "Làm việc tiếng ồn ≥85dB đeo nút tai để phòng điếc tai do ồn.",
                "situation": "onsite"
            },
            {
                "ko": "소음성난청은 한번 발생하면 치료가 불가능하므로 예방이 중요합니다.",
                "vi": "Điếc tai do ồn một khi xảy ra không chữa được nên phòng ngừa quan trọng.",
                "situation": "formal"
            },
            {
                "ko": "소음성난청 걸리면 평생 보청기 껴야 하니까 귀마개 꼭 써야 해요.",
                "vi": "Điếc tai do ồn suốt đời phải đeo máy trợ thính nên nhất định phải đeo nút tai.",
                "situation": "informal"
            }
        ],
        "relatedTerms": [
            "소음",
            "귀마개",
            "귀덮개",
            "청력검사",
            "이명"
        ]
    },
    {
        "slug": "kham-suc-khoe",
        "korean": "건강검진",
        "vietnamese": "khám sức khỏe",
        "hanja": "健康檢診",
        "hanjaReading": "건(건강할 건) + 강(강할 강) + 검(조사할 검) + 진(진찰할 진)",
        "pronunciation": "캄 슉 코에",
        "meaningKo": "근로자의 건강 상태를 주기적으로 검사하여 질병을 조기 발견하고 예방하는 법정 의무 제도입니다. 통역 시 '건강검진'은 'khám sức khỏe' 또는 'kiểm tra sức khỏe định kỳ'로 표현하며, '일반건강검진'과 '특수건강검진'을 구분해야 합니다. 일반건강검진은 모든 근로자를 대상으로 연 1회 실시하며(사무직은 2년 1회), 혈압·혈당·간기능·폐기능·흉부 X-ray 등을 검사합니다. 특수건강검진은 유해 작업(분진·소음·화학물질·중금속) 종사자를 대상으로 6개월~1년마다 실시하며, 유해 요인별 특화 검사(혈중 납 농도, 청력 검사, 폐기능 정밀 검사)를 추가합니다. 한국 「산업안전보건법」은 사업주에게 건강검진 실시 의무를 부과하고, 검진 비용은 사업주 부담이며, 검진 시간은 근무 시간으로 인정됩니다. 검진 결과 '직업병 의심' 또는 '요관찰' 판정을 받으면 작업 전환, 근무 시간 단축, 추가 검사 등 사후조치를 취해야 하며, 미이행 시 과태료(500만원)가 부과됩니다. 건강검진은 직업병을 조기 발견하는 유일한 방법이므로, 근로자는 검진을 성실히 받고 결과를 보관해야 합니다.",
        "meaningVi": "Khám sức khỏe (kiểm tra sức khỏe định kỳ) là chế độ bắt buộc theo pháp luật kiểm tra sức khỏe người lao động định kỳ để phát hiện sớm và phòng bệnh. Chia khám chung và khám đặc biệt. Khám chung: mọi người lao động 1 lần/năm (văn phòng 1 lần/2 năm), kiểm tra huyết áp, đường huyết, gan, phổi, X-quang ngực. Khám đặc biệt: người làm việc có hại (bụi, ồn, hóa chất, kim loại nặng) 6 tháng~1 năm/lần, thêm kiểm tra chuyên biệt (nồng độ chì, thính lực, phổi chi tiết). Chi phí chủ sử dụng lao động, thời gian khám tính giờ làm.",
        "context": "산업안전, 보건관리, 직업병 예방",
        "culturalNote": "한국은 건강검진을 직업병 예방의 핵심 제도로 간주하며, 정부가 검진 기관(지정 의료기관)을 지정하고 검진 내용을 표준화하고 있습니다. 건강검진은 국민건강보험공단과 연계되어 데이터베이스로 관리되며, 검진 결과는 온라인으로 조회 가능합니다. 사업주는 검진 결과를 근로자에게 통보하고, '요관찰' 이상 판정을 받은 근로자에게 사후조치(추가 검사, 작업 전환, 치료 지원)를 취해야 합니다. 베트남은 건강검진 제도가 있지만 형식적으로 운영되는 경우가 많고, 특수건강검진을 생략하거나 간이 검사(혈압·체중만)로 대체하는 경우가 흔합니다. 검진 결과를 근로자에게 통보하지 않고, '요관찰' 판정을 받아도 사후조치를 취하지 않습니다. 한국 발주처가 건강검진 실시를 요구하면 베트남 시공사는 '비용이 많이 든다', '작업 시간이 줄어든다'는 이유로 거부하는 경우가 있어, 통역 시 건강검진의 법적 의무와 직업병 조기 발견의 중요성(치료 가능 시기, 보상 청구 근거)을 구체적으로 전달해야 합니다.",
        "commonMistakes": [
            {
                "mistake": "'건강검진'을 'khám bệnh'(진료)로만 번역",
                "correction": "'khám sức khỏe' 또는 'kiểm tra sức khỏe định kỳ' 사용",
                "explanation": "건강검진은 정기 검사로, 일반 진료(khám bệnh)와 구분 필요"
            },
            {
                "mistake": "'일반건강검진'과 '특수건강검진'을 구분 없이 번역",
                "correction": "일반='khám sức khỏe chung', 특수='khám sức khỏe đặc biệt' 또는 'khám nghề nghiệp đặc thù' 사용",
                "explanation": "대상과 검사 항목이 다르므로 혼동 시 검진 누락"
            },
            {
                "mistake": "검진 결과 판정을 설명 없이 번역",
                "correction": "'bình thường(정상)', 'cần theo dõi(요관찰)', 'nghi bệnh nghề nghiệp(직업병 의심)' 등 판정 기준 설명",
                "explanation": "베트남 근로자는 판정 의미를 모르는 경우 많음"
            }
        ],
        "examples": [
            {
                "ko": "모든 근로자는 연 1회 일반건강검진을 받아야 하며, 비용은 회사가 부담합니다.",
                "vi": "Mọi người lao động phải khám sức khỏe chung 1 lần/năm, chi phí công ty chịu.",
                "situation": "formal"
            },
            {
                "ko": "분진 작업자는 6개월마다 특수건강검진을 받아 진폐증을 조기 발견해야 합니다.",
                "vi": "Người làm việc bụi phải khám sức khỏe đặc biệt mỗi 6 tháng để phát hiện sớm bệnh phổi bụi.",
                "situation": "formal"
            },
            {
                "ko": "검진 결과 '요관찰' 나오면 작업 바꾸거나 치료받아야 해요.",
                "vi": "Kết quả khám ra 'cần theo dõi' thì phải đổi việc hoặc điều trị.",
                "situation": "informal"
            }
        ],
        "relatedTerms": [
            "일반건강검진",
            "특수건강검진",
            "직업병",
            "요관찰",
            "작업전환"
        ]
    },
    {
        "slug": "cap-cuu",
        "korean": "응급처치",
        "vietnamese": "cấp cứu",
        "hanja": "應急處置",
        "hanjaReading": "응(응할 응) + 급(급할 급) + 처(처리할 처) + 치(다스릴 치)",
        "pronunciation": "껍 끄우",
        "meaningKo": "사고·질병으로 부상·의식불명 등 응급 상황이 발생했을 때 전문 의료기관 도착 전까지 실시하는 일시적 조치로, 생명을 구하고 상태 악화를 방지하는 것이 목적입니다. 통역 시 '응급처치'는 'cấp cứu' 또는 'sơ cứu'로 표현하며, '치료(điều trị)'와 구분해야 합니다. 건설 현장 주요 응급 상황은 추락·절단·감전·화상·열사병·심정지이며, 각 상황별 응급처치 방법이 다릅니다. 한국 「산업안전보건법」은 상시 근로자 50인 이상 사업장에 응급처치 요원(응급처치 교육 이수자) 배치, 응급처치 장비(들것, AED, 구급함) 비치, 응급 연락망(119, 인근 병원) 게시를 의무화하고 있습니다. 응급처치 기본 원칙은 (1) 안전 확인(2차 사고 방지), (2) 119 신고, (3) 의식·호흡·맥박 확인, (4) 심폐소생술(CPR) 또는 지혈·고정 등 응급조치, (5) 보온·안정입니다. 심정지 환자는 골든타임이 4분 이내이므로 즉시 심폐소생술과 AED(자동제세동기)를 실시해야 하며, 출혈 환자는 지혈대·압박 지혈, 골절 환자는 부목 고정, 화상 환자는 찬물 냉각(10분 이상)이 필요합니다. 응급처치는 전문 교육(4시간 이상)을 이수한 자가 실시하며, 응급처치 요원은 2년마다 재교육을 받아야 합니다.",
        "meaningVi": "Cấp cứu (sơ cứu) là biện pháp tạm thời trước khi đến bệnh viện khi xảy ra tình huống khẩn cấp do tai nạn hoặc bệnh (thương tích, mất ý thức), mục đích cứu mạng và ngăn tình trạng xấu đi. Khác với điều trị (chữa bệnh chuyên môn), cấp cứu là xử lý ban đầu. Ở công trường: rơi, cắt, điện giật, bỏng, say nắng, ngừng tim. Nguyên tắc: (1) kiểm tra an toàn, (2) gọi 119, (3) kiểm tra ý thức/hô hấp/mạch, (4) CPR hoặc cầm máu/cố định, (5) giữ ấm/yên. Ngừng tim: thời gian vàng 4 phút, CPR + AED. Chảy máu: dây cầm máu/ép. Gãy xương: nẹp cố định. Bỏng: nước lạnh 10 phút.",
        "context": "산업안전, 응급의료, 재해 대응",
        "culturalNote": "한국은 응급처치를 현장 안전의 최후 보루로 간주하며, 정부가 응급처치 교육(심폐소생술, 지혈법, 골절 처치)을 무료로 제공하고 있습니다. 건설 현장은 응급처치 요원을 지정하고, 요원은 형광 조끼에 '응급처치 요원' 표시를 하며, 사고 발생 시 즉시 출동합니다. 현장에는 AED(자동제세동기)를 비치하고, 전 근로자에게 AED 위치와 사용법을 교육합니다. 구급함에는 붕대, 소독약, 지혈대, 부목, 화상 연고, 냉각 팩이 구비되며, 6개월마다 내용물을 점검·보충합니다. 베트남은 응급처치 개념이 약하고, 응급처치 요원을 지정하지 않거나 교육을 형식적으로 실시하는 경우가 많습니다. 사고 발생 시 119 신고 없이 개인 차량으로 병원에 이송하거나, 잘못된 응급처치(골절 환자를 무리하게 옮김, 화상에 된장·치약 바름)를 하는 경우가 흔합니다. 한국 안전관리자가 응급처치 교육을 강조하면 베트남 근로자는 '어렵다', '쓸 일 없다'는 이유로 소홀히 하는 경우가 있어, 통역 시 응급처치의 생명 구조 효과(골든타임, 생존율 증가)와 법적 의무를 구체적으로 전달해야 합니다.",
        "commonMistakes": [
            {
                "mistake": "'응급처치'를 'điều trị'(치료)로만 번역",
                "correction": "'cấp cứu' 또는 'sơ cứu' 사용",
                "explanation": "응급처치는 전문 의료 전 임시 조치로, 치료(điều trị)와 구분 필요"
            },
            {
                "mistake": "'심폐소생술(CPR)'을 번역 없이 영문 약어만 사용",
                "correction": "'hồi sức tim phổi' 또는 'CPR (tim phổi)' 병기",
                "explanation": "베트남 근로자는 CPR 용어에 익숙하지 않음"
            },
            {
                "mistake": "응급처치 방법을 추상적으로 설명",
                "correction": "지혈='ép vết thương', 냉각='ngâm nước lạnh', 고정='cố định bằng nẹp' 등 구체적 동작 설명",
                "explanation": "베트남 근로자는 응급처치 교육 경험이 없어 구체적 설명 필요"
            }
        ],
        "examples": [
            {
                "ko": "출혈 환자는 깨끗한 천으로 상처를 강하게 눌러 지혈하고, 119에 신고하세요.",
                "vi": "Người chảy máu dùng vải sạch ép mạnh vết thương cầm máu, gọi 119.",
                "situation": "onsite"
            },
            {
                "ko": "심정지 환자는 즉시 심폐소생술(CPR)을 실시하고, AED를 사용하세요.",
                "vi": "Người ngừng tim lập tức hồi sức tim phổi (CPR), dùng AED.",
                "situation": "formal"
            },
            {
                "ko": "응급처치는 4분 안에 해야 살릴 수 있으니까 배워둬야 해요.",
                "vi": "Cấp cứu phải làm trong 4 phút mới cứu được nên phải học trước.",
                "situation": "informal"
            }
        ],
        "relatedTerms": [
            "심폐소생술",
            "AED",
            "지혈",
            "골절고정",
            "119신고"
        ]
    }
]

# 저장 경로
output_path = os.path.join(
    os.path.dirname(os.path.abspath(__file__)),
    "..",
    "data",
    "terms",
    "construction.json"
)

print(f"저장 경로: {output_path}")
print(f"추가할 용어 개수: {len(data)}개")
print("\n추가할 용어 목록:")
for i, term in enumerate(data, 1):
    print(f"{i}. {term['korean']} ({term['vietnamese']})")

# 실행 금지 - 스크립트만 생성
print("\n⚠️  이 스크립트는 실행하지 마세요. Write만 하고 종료합니다.")

# === Merge Logic ===
import json as _json
with open(output_path, 'r', encoding='utf-8') as _f:
    _existing = _json.load(_f)
_existing_slugs = {t['slug'] for t in _existing}
_filtered = [t for t in data if t['slug'] not in _existing_slugs]
_existing.extend(_filtered)
with open(output_path, 'w', encoding='utf-8') as _f:
    _json.dump(_existing, _f, ensure_ascii=False, indent=2)
print(f"Added {len(_filtered)} terms. Total: {len(_existing)}")
