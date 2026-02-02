#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Construction 용어 추가 스크립트 v7 - 골재/모래/잡석 테마
테마: 굵은골재, 잔골재, 세골재, 쇄석, 모래, 왕모래, 잡석, 채움재, 필터재, 버림콘크리트
대상: construction.json에 10개 용어 추가
품질: Tier S (90점 이상) 필수
"""

import json
import os

# 추가할 용어 데이터 (10개)
new_terms = [
    {
        "slug": "cot-lon",
        "korean": "굵은골재",
        "vietnamese": "Cốt lớn",
        "hanja": "굵은骨材",
        "hanjaReading": "굵(굵을 굵) + 骨(뼈 골) + 材(재목 재)",
        "pronunciation": "꼴런",
        "meaningKo": "콘크리트나 아스팔트 포장에 사용되는 입자 크기 5mm 이상의 골재를 의미합니다. 주로 자갈, 쇄석 등이 사용되며 콘크리트의 뼈대 역할을 합니다. 통역 시 '자갈'로 오해하지 않도록 주의하세요. 베트남어로는 'Cốt lớn' 또는 'Đá dăm lớn'으로 표현하며, 한국 규격(KS)과 베트남 규격(TCVN)의 입도 기준이 다를 수 있어 수치 확인이 필수입니다. 현장에서는 '굵골', '큰 돌'로 불리기도 합니다.",
        "meaningVi": "Cốt liệu có kích thước hạt từ 5mm trở lên, thường là đá dăm hoặc sỏi, được dùng trong bê tông và asphalt để tạo khung xương cho kết cấu. Tiêu chuẩn cấp phối hạt có thể khác nhau giữa KS (Hàn Quốc) và TCVN (Việt Nam), cần kiểm tra số liệu cụ thể khi thông dịch.",
        "context": "formal",
        "culturalNote": "한국에서는 KS F 2526 기준에 따라 입도 관리가 엄격하며, 5mm~40mm 범위로 세분화합니다. 베트남은 TCVN 기준을 따르지만 현장에서 중국산 또는 한국산 자재를 혼용하는 경우가 많아, 통역사는 양국 규격 차이를 숙지해야 합니다. 특히 공사 감리 단계에서 입도 시험 결과를 설명할 때 혼란을 막기 위해 단위(mm)와 체 번호를 명확히 구분하세요.",
        "commonMistakes": [
            {
                "mistake": "Cốt lớn을 '큰 뼈'로 직역",
                "correction": "굵은골재 = Cốt lớn (cốt liệu lớn)",
                "explanation": "골재는 뼈(骨) + 재료(材)의 합성어이지만, 베트남어에서는 '뼈'를 따로 해석하지 않고 'cốt liệu'라는 전문용어로 통칭합니다."
            },
            {
                "mistake": "'자갈'로 통역",
                "correction": "굵은골재는 자갈뿐 아니라 쇄석도 포함하므로 'Cốt lớn' 또는 'Đá dăm lớn'",
                "explanation": "자갈(sỏi)은 자연산, 쇄석(đá dăm)은 인공 파쇄된 것으로 구분되므로 포괄 개념인 'Cốt lớn'을 사용해야 정확합니다."
            },
            {
                "mistake": "5mm 기준을 '5센티'로 오역",
                "correction": "5mm = 5 milimét (5밀리미터)",
                "explanation": "현장에서 센티(cm)와 밀리(mm)를 혼동하면 발주 오류로 이어질 수 있습니다."
            }
        ],
        "examples": [
            {
                "ko": "이번 현장은 굵은골재 최대 입경 25mm로 지정되어 있습니다.",
                "vi": "Công trường này quy định cốt lớn có kích thước hạt tối đa 25mm.",
                "situation": "formal"
            },
            {
                "ko": "굵은골재 입도 시험 결과 KS 기준에 적합합니다.",
                "vi": "Kết quả thí nghiệm cấp phối cốt lớn phù hợp với tiêu chuẩn KS.",
                "situation": "formal"
            },
            {
                "ko": "굵골은 어디서 반입하나요?",
                "vi": "Cốt lớn được nhập từ đâu vậy?",
                "situation": "onsite"
            }
        ],
        "relatedTerms": ["잔골재", "쇄석", "입도", "골재"],
        "difficulty": "intermediate",
        "frequency": "high"
    },
    {
        "slug": "cat-mịn",
        "korean": "잔골재",
        "vietnamese": "Cát mịn",
        "hanja": "殘骨材",
        "hanjaReading": "殘(남을 잔) + 骨(뼈 골) + 材(재목 재)",
        "pronunciation": "깟민",
        "meaningKo": "입자 크기 5mm 미만의 모래, 부순 모래 등을 포괄하는 골재입니다. 콘크리트의 공극을 채우고 워커빌리티를 높이는 역할을 하며, 한국에서는 '잔골재'로, 베트남에서는 주로 'Cát mịn' 또는 'Cốt nhỏ'로 표현합니다. 통역 시 '모래'와 혼용되지만 '잔골재'는 규격화된 전문용어이므로 공사 계약서나 품질 보고서에서는 엄밀히 구분해야 합니다. 현장에서는 '잔골'로 줄여 부르기도 합니다.",
        "meaningVi": "Cốt liệu có kích thước hạt dưới 5mm, bao gồm cát tự nhiên và cát nghiền, dùng để lấp đầy khe rỗng trong bê tông và cải thiện tính thi công. Tiêu chuẩn cấp phối cát tại Hàn Quốc (KS) và Việt Nam (TCVN) có thể khác nhau, cần xác minh trước khi thông dịch.",
        "context": "formal",
        "culturalNote": "한국에서는 강모래, 바닷모래, 쇄사를 구분하여 사용하며, KS F 2526에서 세부 기준을 정합니다. 베트남은 강모래(cát sông)를 주로 쓰지만 최근 환경 규제로 쇄사(cát nghiền)가 증가하는 추세입니다. 통역사는 발주처가 요구하는 잔골재 종류를 명확히 파악하고, 한국 기술진이 베트남산 모래의 염분 함량을 우려할 경우 관련 시험 성적서를 요청하도록 안내하세요.",
        "commonMistakes": [
            {
                "mistake": "'모래'로만 통역",
                "correction": "잔골재 = Cát mịn / Cốt nhỏ (규격 전문용어)",
                "explanation": "모래(cát)는 일상어이고, 잔골재는 공학적 정의가 담긴 용어이므로 공식 문서에서는 'Cát mịn'이나 'Cốt nhỏ'를 사용해야 합니다."
            },
            {
                "mistake": "'세골재'와 혼동",
                "correction": "잔골재(5mm 미만 전체), 세골재(더 미세한 입자)",
                "explanation": "세골재는 잔골재 중에서도 더 작은 입도를 의미하므로 구분이 필요합니다."
            },
            {
                "mistake": "염분 함량 언급 없이 바닷모래를 '모래'로 통역",
                "correction": "바닷모래 = Cát biển (염분 시험 필요)",
                "explanation": "베트남 현장에서 바닷모래를 쓸 경우 염분이 철근 부식을 일으킬 수 있으므로 반드시 시험 성적서를 확인하도록 안내하세요."
            }
        ],
        "examples": [
            {
                "ko": "잔골재는 입도 조정을 통해 워커빌리티를 개선할 수 있습니다.",
                "vi": "Có thể cải thiện độ thi công bằng cách điều chỉnh cấp phối của cát mịn.",
                "situation": "formal"
            },
            {
                "ko": "이번 배치는 잔골재 함수율이 높으니 물 추가를 줄이세요.",
                "vi": "Lô này hàm lượng nước trong cát cao, nên giảm lượng nước thêm vào.",
                "situation": "onsite"
            },
            {
                "ko": "잔골 입도 시험 결과 어떻게 나왔어요?",
                "vi": "Kết quả thí nghiệm cấp phối cát ra sao?",
                "situation": "informal"
            }
        ],
        "relatedTerms": ["굵은골재", "모래", "입도", "워커빌리티"],
        "difficulty": "intermediate",
        "frequency": "high"
    },
    {
        "slug": "cat-min",
        "korean": "세골재",
        "vietnamese": "Cát mịn",
        "hanja": "細骨材",
        "hanjaReading": "細(가늘 세) + 骨(뼈 골) + 材(재목 재)",
        "pronunciation": "깟민",
        "meaningKo": "잔골재 중에서도 특히 미세한 입자(보통 0.15mm~5mm)를 지칭하는 용어입니다. 콘크리트의 빈틈을 채우고 표면 마감을 매끄럽게 하는 역할을 하며, 한국에서는 '세골재'로, 베트남에서는 'Cát mịn' 또는 'Cát nhỏ'로 표현합니다. 통역 시 '잔골재'와 구분이 모호할 수 있으므로, 입도 범위를 함께 설명하거나 'cát rất mịn(매우 미세한 모래)'로 보충 설명하는 것이 좋습니다. 현장에서는 '고운 모래', '미세 모래'로 불리기도 합니다.",
        "meaningVi": "Cát có hạt rất mịn (thường 0.15mm~5mm), thuộc nhóm cốt nhỏ, dùng để lấp đầy khe rỗng trong bê tông và tạo bề mặt nhẵn mịn. Tại Hàn Quốc, 'Se-goljae(세골재)' là thuật ngữ kỹ thuật chính thức, tại Việt Nam thường gọi là 'Cát mịn' hoặc 'Cát nhỏ'.",
        "context": "formal",
        "culturalNote": "한국에서는 KS F 2526에서 세골재를 잔골재의 하위 분류로 정의하지만, 베트남에서는 'Cát mịn'이 일상어와 전문용어를 겸하므로 혼란이 생길 수 있습니다. 통역사는 발주처의 요구 사항에 따라 입도 범위를 명시하고, 필요시 체 분석(sieve analysis) 결과를 함께 제시하도록 안내하세요. 특히 미장 작업이나 초벌 콘크리트에서 세골재 비율이 높으면 수축 균열이 발생할 수 있으므로 주의가 필요합니다.",
        "commonMistakes": [
            {
                "mistake": "'잔골재'와 동일하게 통역",
                "correction": "세골재는 잔골재 중 더 미세한 입자 (0.15mm~5mm 범위 강조)",
                "explanation": "잔골재는 5mm 미만 전체, 세골재는 그중 미세한 부분이므로 구분이 필요합니다."
            },
            {
                "mistake": "'Cát mịn'만 말하고 입도 범위 생략",
                "correction": "Cát mịn (0.15mm~5mm) 또는 Cát rất mịn으로 보충",
                "explanation": "베트남 현장에서 'Cát mịn'은 일반 모래로 오해될 수 있으므로 입도를 명시하세요."
            },
            {
                "mistake": "고운 모래를 '파우더'로 직역",
                "correction": "세골재 = Cát mịn (không phải bột, mà là cát hạt nhỏ)",
                "explanation": "파우더(bột)는 시멘트나 석분을 의미하므로, 모래 입자인 세골재와는 다릅니다."
            }
        ],
        "examples": [
            {
                "ko": "세골재 함량이 과다하면 수축 균열 위험이 있습니다.",
                "vi": "Nếu hàm lượng cát mịn quá cao, có nguy cơ nứt co ngót.",
                "situation": "formal"
            },
            {
                "ko": "이번 미장은 세골재 비율을 높여 마감을 부드럽게 합시다.",
                "vi": "Lần trát này tăng tỷ lệ cát mịn để bề mặt nhẵn hơn.",
                "situation": "onsite"
            },
            {
                "ko": "세골 입도 분석 결과 좀 보여주세요.",
                "vi": "Cho xem kết quả phân tích cấp phối cát mịn.",
                "situation": "informal"
            }
        ],
        "relatedTerms": ["잔골재", "굵은골재", "입도", "모래"],
        "difficulty": "advanced",
        "frequency": "medium"
    },
    {
        "slug": "da-dam",
        "korean": "쇄석",
        "vietnamese": "Đá dăm",
        "hanja": "碎石",
        "hanjaReading": "碎(부술 쇄) + 石(돌 석)",
        "pronunciation": "다짬",
        "meaningKo": "암석을 인공적으로 파쇄하여 만든 골재로, 자연산 자갈보다 모서리가 각지고 부착력이 강해 콘크리트나 도로 기층에 주로 사용됩니다. 베트남어로는 'Đá dăm'이며, 한국 현장에서는 '쇄석', '깬돌', '부순돌'로 불립니다. 통역 시 자갈(sỏi)과 혼동하지 않도록 주의하세요. 쇄석은 입도, 강도, 편평도 등의 기준이 엄격하며, KS와 TCVN 규격 차이를 확인해야 합니다. 특히 도로 공사에서는 '보조기층용 쇄석', '상층용 쇄석'으로 구분되므로 용도를 명확히 하세요.",
        "meaningVi": "Đá thiên nhiên được nghiền nhỏ bằng máy, có góc cạnh sắc và độ bám dính cao, thường dùng trong bê tông và lớp móng đường. Khác với sỏi tự nhiên (đá cuội), đá dăm có hình dạng góc cạnh rõ ràng, phù hợp với các công trình yêu cầu độ chịu lực cao.",
        "context": "formal",
        "culturalNote": "한국에서는 화강암, 현무암, 석회암 등 암종별로 쇄석을 구분하며, KS F 2527에서 품질 기준을 정합니다. 베트남은 현무암(đá bazan) 쇄석이 흔하지만 한국 기술진은 화강암(đá granite) 쇄석을 선호하는 경우가 많습니다. 통역사는 발주처가 요구하는 암종과 강도를 확인하고, 현지 공급 가능 여부를 사전에 파악하도록 안내하세요. 또한 쇄석의 편평도(độ dẹt)가 기준을 초과하면 공극률이 높아져 콘크리트 품질이 저하될 수 있으므로 주의가 필요합니다.",
        "commonMistakes": [
            {
                "mistake": "'자갈'로 통역",
                "correction": "쇄석 = Đá dăm (인공 파쇄), 자갈 = Sỏi (자연산)",
                "explanation": "자갈은 둥글고 쇄석은 각진 형태이므로 구분이 필수입니다."
            },
            {
                "mistake": "'Đá'로만 말하고 'dăm' 생략",
                "correction": "쇄석 = Đá dăm (đá nghiền)",
                "explanation": "'Đá'는 일반 돌을 의미하므로, 'dăm(부순)'을 추가해야 쇄석임을 명확히 할 수 있습니다."
            },
            {
                "mistake": "암종 구분 없이 '쇄석'으로만 통역",
                "correction": "화강암 쇄석 = Đá dăm granite, 현무암 쇄석 = Đá dăm bazan",
                "explanation": "암종에 따라 강도와 내구성이 다르므로 발주처 요구를 정확히 전달해야 합니다."
            }
        ],
        "examples": [
            {
                "ko": "이번 기층은 쇄석 40mm를 사용합니다.",
                "vi": "Lớp móng này sử dụng đá dăm 40mm.",
                "situation": "formal"
            },
            {
                "ko": "쇄석 편평도 시험 결과 기준치 이내입니다.",
                "vi": "Kết quả thí nghiệm độ dẹt của đá dăm nằm trong tiêu chuẩn.",
                "situation": "formal"
            },
            {
                "ko": "쇄석 반입 확인 좀 해주세요.",
                "vi": "Kiểm tra nhập kho đá dăm giúp tôi.",
                "situation": "onsite"
            }
        ],
        "relatedTerms": ["굵은골재", "자갈", "입도", "암종"],
        "difficulty": "intermediate",
        "frequency": "high"
    },
    {
        "slug": "cat",
        "korean": "모래",
        "vietnamese": "Cát",
        "hanja": None,
        "hanjaReading": None,
        "pronunciation": "깟",
        "meaningKo": "자연적으로 형성된 암석 입자로, 입경이 주로 0.06mm~2mm 범위인 자연 골재입니다. 콘크리트, 모르타르, 미장재 등에 널리 사용되며, 강모래, 바닷모래, 산모래로 구분됩니다. 베트남어로는 'Cát'이며, 통역 시 '잔골재'와 혼용되기도 하지만 '모래'는 일상어, '잔골재'는 규격 전문용어임을 구분하세요. 한국에서는 KS F 2526에서 입도와 불순물 기준을 정하며, 베트남은 TCVN 기준을 따르지만 현장에서는 중국산이나 태국산 모래도 혼용됩니다. 통역사는 발주처가 요구하는 모래 종류(강/바다/산)와 염분 함량을 확인하도록 안내하세요.",
        "meaningVi": "Cát tự nhiên có kích thước hạt từ 0.06mm đến 2mm, được hình thành từ phong hóa đá, dùng trong bê tông, vữa xây, vữa trát. Phân loại: cát sông, cát biển, cát núi. Tiêu chuẩn hàm lượng muối và cấp phối hạt khác nhau giữa KS (Hàn Quốc) và TCVN (Việt Nam).",
        "context": "formal",
        "culturalNote": "한국에서는 환경 규제로 강모래 채취가 제한되어 쇄사(부순 모래) 사용이 증가하는 추세입니다. 베트남은 강모래(cát sông)가 풍부하지만, 최근 환경 보호법으로 일부 지역에서 채취가 금지되어 가격이 상승했습니다. 통역사는 한국 기술진이 바닷모래(cát biển) 사용을 우려할 경우 염분 제거(rửa muối) 공정과 시험 성적서를 요청하도록 안내하세요. 또한 산모래(cát núi)는 입도가 고르지 않아 콘크리트 품질이 떨어질 수 있으므로 주의가 필요합니다.",
        "commonMistakes": [
            {
                "mistake": "'모래'와 '잔골재'를 동일하게 통역",
                "correction": "모래 = Cát (일상어), 잔골재 = Cát mịn/Cốt nhỏ (규격 전문용어)",
                "explanation": "공식 문서나 품질 보고서에서는 '잔골재'를 사용하고, 일상 대화에서는 '모래'를 씁니다."
            },
            {
                "mistake": "바닷모래를 '모래'로만 통역",
                "correction": "바닷모래 = Cát biển (염분 시험 필요)",
                "explanation": "바닷모래는 염분 함량이 높아 철근 부식을 일으킬 수 있으므로 반드시 시험을 거쳐야 합니다."
            },
            {
                "mistake": "쇄사를 '부순 모래'로 직역",
                "correction": "쇄사 = Cát nghiền (인공 모래)",
                "explanation": "'Cát nghiền'이 베트남 현장에서 통용되는 전문용어입니다."
            }
        ],
        "examples": [
            {
                "ko": "이번 현장은 강모래를 사용하며, 염분 시험은 생략합니다.",
                "vi": "Công trường này dùng cát sông, bỏ qua thí nghiệm muối.",
                "situation": "formal"
            },
            {
                "ko": "모래 입도가 고르지 않으니 체질 후 사용하세요.",
                "vi": "Cấp phối cát không đều, hãy sàng lọc trước khi dùng.",
                "situation": "onsite"
            },
            {
                "ko": "모래 얼마나 남았어요?",
                "vi": "Cát còn bao nhiêu?",
                "situation": "informal"
            }
        ],
        "relatedTerms": ["잔골재", "쇄사", "강모래", "바닷모래"],
        "difficulty": "beginner",
        "frequency": "high"
    },
    {
        "slug": "cat-song-to",
        "korean": "왕모래",
        "vietnamese": "Cát sông to",
        "hanja": None,
        "hanjaReading": None,
        "pronunciation": "깟숑또",
        "meaningKo": "입자가 굵은 강모래로, 일반 모래보다 입경이 크고(보통 2mm~5mm) 배수성이 우수하여 필터층, 배수층, 뒷채움재 등에 사용됩니다. 베트남어로는 'Cát sông to' 또는 'Cát hạt lớn'이며, 한국 현장에서는 '왕모래', '굵은 모래'로 불립니다. 통역 시 '자갈'이나 '쇄석'과 혼동하지 않도록 주의하세요. 왕모래는 콘크리트용보다는 배수 및 충진 용도로 많이 쓰이며, 입도 분포가 중요합니다. 통역사는 발주처가 요구하는 입도 범위와 사용 목적을 명확히 확인하세요.",
        "meaningVi": "Cát sông có hạt lớn (2mm~5mm), thoát nước tốt, dùng làm lớp lọc, lớp thoát nước, vật liệu lấp. Tại Hàn Quốc gọi là 'Wang-morae(왕모래)', tại Việt Nam thường gọi 'Cát sông to' hoặc 'Cát hạt lớn'. Không dùng làm bê tông mà chủ yếu cho mục đích thoát nước và san lấp.",
        "context": "formal",
        "culturalNote": "한국에서는 왕모래를 주로 배수층이나 필터재로 사용하며, KS 기준에서는 입도 범위를 2mm~5mm로 정합니다. 베트남은 강모래(cát sông)가 풍부하여 왕모래 조달이 비교적 용이하지만, 한국 기술진은 입도 분포를 엄격히 확인하는 경우가 많습니다. 통역사는 발주처가 왕모래를 요구할 때 '자갈(sỏi)'이나 '쇄석(đá dăm)'과 혼동하지 않도록 입경 범위를 명시하고, 필요시 체 분석 결과를 제시하도록 안내하세요. 특히 배수 공사에서 왕모래 입도가 적절하지 않으면 배수 효율이 떨어질 수 있습니다.",
        "commonMistakes": [
            {
                "mistake": "'자갈'로 통역",
                "correction": "왕모래 = Cát sông to (2mm~5mm), 자갈 = Sỏi (5mm 이상)",
                "explanation": "왕모래는 모래의 일종이고, 자갈은 더 큰 입자이므로 구분이 필요합니다."
            },
            {
                "mistake": "'굵은골재'로 통역",
                "correction": "왕모래 = Cát sông to (2mm~5mm), 굵은골재 = Cốt lớn (5mm 이상)",
                "explanation": "왕모래는 5mm 미만이므로 굵은골재에 해당하지 않습니다."
            },
            {
                "mistake": "'Cát to'로만 말하고 'sông' 생략",
                "correction": "왕모래 = Cát sông to (강모래 중 입자가 큰 것)",
                "explanation": "'sông(강)'을 명시해야 출처가 명확해집니다."
            }
        ],
        "examples": [
            {
                "ko": "배수층은 왕모래 150mm 두께로 시공합니다.",
                "vi": "Lớp thoát nước thi công bằng cát sông to dày 150mm.",
                "situation": "formal"
            },
            {
                "ko": "왕모래 입도 시험 결과 2mm~5mm 범위 내입니다.",
                "vi": "Kết quả thí nghiệm cấp phối cát sông to trong khoảng 2mm~5mm.",
                "situation": "formal"
            },
            {
                "ko": "왕모래 좀 더 가져와.",
                "vi": "Mang thêm cát sông to.",
                "situation": "onsite"
            }
        ],
        "relatedTerms": ["모래", "자갈", "배수층", "필터재"],
        "difficulty": "intermediate",
        "frequency": "medium"
    },
    {
        "slug": "da-vo",
        "korean": "잡석",
        "vietnamese": "Đá vỡ",
        "hanja": "雜石",
        "hanjaReading": "雜(섞일 잡) + 石(돌 석)",
        "pronunciation": "다버",
        "meaningKo": "입경이 일정하지 않고 모양이 불규칙한 돌로, 주로 되메우기, 성토, 기초 지반 조성 등에 사용됩니다. 베트남어로는 'Đá vỡ' 또는 'Đá hộc'이며, 한국 현장에서는 '잡석', '잡돌', '허름돌'로 불립니다. 통역 시 '쇄석'이나 '자갈'과 혼동하지 않도록 주의하세요. 잡석은 품질 기준이 느슨하여 구조물에 직접 사용하기보다는 뒷채움이나 기초 충진 용도로 쓰입니다. 통역사는 발주처가 요구하는 용도와 입경 범위를 확인하고, 강도나 내구성이 중요한 부위에는 잡석 대신 쇄석을 권장하도록 안내하세요.",
        "meaningVi": "Đá có kích thước và hình dạng không đồng đều, dùng để san lấp, đắp nền, tạo móng. Tại Hàn Quốc gọi là 'Jap-seok(잡석)', tại Việt Nam thường gọi 'Đá vỡ' hoặc 'Đá hộc'. Không dùng cho kết cấu chịu lực mà chủ yếu cho mục đích lấp đầy và tạo nền.",
        "context": "formal",
        "culturalNote": "한국에서는 잡석을 주로 성토나 뒷채움에 사용하며, KS 기준에서는 잡석의 품질을 명확히 정의하지 않아 현장 재량으로 사용합니다. 베트남은 산지가 많아 잡석 조달이 용이하지만, 한국 기술진은 잡석의 강도와 입도 분포를 확인하는 경우가 많습니다. 통역사는 발주처가 잡석을 요구할 때 용도(되메우기/성토/기초)를 명확히 하고, 구조물에 직접 사용할 경우 쇄석으로 대체하도록 권장하세요. 특히 연약 지반에서는 잡석 다짐이 불균등하면 침하가 발생할 수 있으므로 주의가 필요합니다.",
        "commonMistakes": [
            {
                "mistake": "'쇄석'으로 통역",
                "correction": "잡석 = Đá vỡ (불규칙), 쇄석 = Đá dăm (규격)",
                "explanation": "쇄석은 규격화된 골재이고, 잡석은 품질 기준이 느슨한 충진재입니다."
            },
            {
                "mistake": "'자갈'로 통역",
                "correction": "잡석 = Đá vỡ (입경 불규칙), 자갈 = Sỏi (둥근 자연산)",
                "explanation": "자갈은 자연적으로 둥글게 형성된 것이고, 잡석은 모양이 불규칙합니다."
            },
            {
                "mistake": "'Đá'로만 말하고 'vỡ' 생략",
                "correction": "잡석 = Đá vỡ (đá không đều)",
                "explanation": "'vỡ(깨진)'를 추가해야 잡석임을 명확히 할 수 있습니다."
            }
        ],
        "examples": [
            {
                "ko": "기초 뒷채움은 잡석으로 시공하고 다짐은 3회 실시합니다.",
                "vi": "Lấp đầy móng bằng đá vỡ và đầm 3 lần.",
                "situation": "formal"
            },
            {
                "ko": "잡석 입경이 너무 커서 다짐이 어렵습니다.",
                "vi": "Kích thước đá vỡ quá lớn nên khó đầm nén.",
                "situation": "onsite"
            },
            {
                "ko": "잡석 좀 더 부어.",
                "vi": "Đổ thêm đá vỡ.",
                "situation": "informal"
            }
        ],
        "relatedTerms": ["쇄석", "자갈", "뒷채움", "성토"],
        "difficulty": "intermediate",
        "frequency": "medium"
    },
    {
        "slug": "vat-lieu-lap",
        "korean": "채움재",
        "vietnamese": "Vật liệu lấp",
        "hanja": "채움材",
        "hanjaReading": "채(채울 채) + 材(재목 재)",
        "pronunciation": "벗리에우럽",
        "meaningKo": "공극이나 빈 공간을 채우는 재료로, 주로 되메우기, 성토, 기초 조성 등에 사용됩니다. 모래, 자갈, 쇄석, 잡석, 순환골재 등 다양한 재료가 포함되며, 베트남어로는 'Vật liệu lấp' 또는 'Vật liệu đắp'입니다. 통역 시 '뒷채움재', '성토재', '충진재'와 혼용되므로 용도를 명확히 구분하세요. 한국에서는 KS 기준에서 채움재의 입도, 다짐도, 함수율 등을 정하며, 베트남은 TCVN 기준을 따르지만 현장에서는 순환골재(골재 재활용)를 선호하는 경우가 많습니다. 통역사는 발주처가 요구하는 채움재 종류와 품질 기준을 확인하고, 다짐 시방서를 함께 검토하도록 안내하세요.",
        "meaningVi": "Vật liệu dùng để lấp đầy khe rỗng hoặc không gian trống, bao gồm cát, sỏi, đá dăm, đá vỡ, cốt liệu tái chế. Tại Hàn Quốc gọi là 'Chaeum-jae(채움재)', tại Việt Nam thường gọi 'Vật liệu lấp' hoặc 'Vật liệu đắp'. Tiêu chuẩn cấp phối, độ đầm chặt, hàm lượng nước khác nhau giữa KS và TCVN.",
        "context": "formal",
        "culturalNote": "한국에서는 채움재를 용도별로 세분화하여 관리하며, 구조물 뒤채움에는 쇄석이나 모래, 도로 성토에는 양질토나 순환골재를 사용합니다. 베트남은 순환골재(cốt liệu tái chế) 사용이 증가하는 추세이지만, 한국 기술진은 품질 우려로 천연 골재를 선호하는 경우가 많습니다. 통역사는 발주처가 순환골재 사용을 승인했는지 확인하고, 다짐도(độ đầm chặt) 기준을 명확히 전달하세요. 특히 지하 구조물 뒤채움에서 다짐이 불충분하면 침하가 발생할 수 있으므로 주의가 필요합니다.",
        "commonMistakes": [
            {
                "mistake": "'뒷채움재'로만 통역",
                "correction": "채움재 = Vật liệu lấp (포괄 개념), 뒷채움재 = Vật liệu lấp phía sau (특정 부위)",
                "explanation": "채움재는 모든 충진 용도를 포괄하고, 뒷채움재는 구조물 뒤에 사용하는 것입니다."
            },
            {
                "mistake": "'충진재'와 동일하게 통역",
                "correction": "채움재(건축/토목), 충진재(기계/설비)",
                "explanation": "채움재는 토목/건축 용어이고, 충진재는 기계나 설비 틈새를 메우는 재료입니다."
            },
            {
                "mistake": "순환골재를 '재활용 쓰레기'로 오역",
                "correction": "순환골재 = Cốt liệu tái chế (품질 인증된 재활용 골재)",
                "explanation": "순환골재는 품질 검사를 거친 재활용 골재이므로 '쓰레기'와 다릅니다."
            }
        ],
        "examples": [
            {
                "ko": "기초 채움재는 쇄석 40mm를 사용하고 다짐도 95% 이상 확보하세요.",
                "vi": "Vật liệu lấp móng dùng đá dăm 40mm và đạt độ đầm chặt trên 95%.",
                "situation": "formal"
            },
            {
                "ko": "채움재 함수율이 높으니 건조 후 사용합시다.",
                "vi": "Hàm lượng nước trong vật liệu lấp cao, hãy phơi khô trước khi dùng.",
                "situation": "onsite"
            },
            {
                "ko": "채움재 얼마나 남았어?",
                "vi": "Vật liệu lấp còn bao nhiêu?",
                "situation": "informal"
            }
        ],
        "relatedTerms": ["뒷채움", "성토", "다짐", "순환골재"],
        "difficulty": "intermediate",
        "frequency": "high"
    },
    {
        "slug": "vat-lieu-loc",
        "korean": "필터재",
        "vietnamese": "Vật liệu lọc",
        "hanja": "필터材",
        "hanjaReading": "필터(filter 음차) + 材(재목 재)",
        "pronunciation": "벗리에우록",
        "meaningKo": "배수 시스템에서 물은 통과시키되 토사나 미세 입자는 걸러내는 역할을 하는 재료로, 주로 왕모래, 쇄석, 필터층 전용 골재 등이 사용됩니다. 베트남어로는 'Vật liệu lọc' 또는 'Vật liệu lọc nước'이며, 한국 현장에서는 '필터재', '여과재'로 불립니다. 통역 시 '배수재'와 혼동하지 않도록 주의하세요. 필터재는 입도 분포가 매우 중요하며, 입자가 너무 크면 토사가 빠져나가고, 너무 작으면 배수가 막힙니다. 통역사는 발주처가 요구하는 입도 범위와 투수 계수를 확인하고, 필요시 체 분석 및 투수 시험 결과를 제시하도록 안내하세요.",
        "meaningVi": "Vật liệu trong hệ thống thoát nước, cho phép nước đi qua nhưng giữ lại đất và hạt mịn, thường dùng cát sông to, đá dăm, hoặc cốt liệu chuyên dụng. Tại Hàn Quốc gọi là 'Filter-jae(필터재)', tại Việt Nam thường gọi 'Vật liệu lọc' hoặc 'Vật liệu lọc nước'. Cấp phối hạt rất quan trọng: hạt quá lớn thì đất thoát ra, hạt quá nhỏ thì nước bị tắc.",
        "context": "formal",
        "culturalNote": "한국에서는 KS 기준에서 필터재의 입도 분포, 투수 계수, 균등 계수 등을 엄격히 정하며, 배수 공사에서 필터재 선정은 설계 단계에서 결정됩니다. 베트남은 왕모래(cát sông to)나 자갈(sỏi)을 필터재로 많이 사용하지만, 한국 기술진은 입도 분포를 정밀하게 확인하는 경우가 많습니다. 통역사는 발주처가 필터재 사양을 요구할 때 입도 범위, 투수 계수, 균등 계수를 명시하고, 필요시 시험 성적서를 제출하도록 안내하세요. 특히 옹벽 뒤나 터널 배수층에서 필터재가 부적합하면 배수 불량으로 구조물 안전에 문제가 생길 수 있습니다.",
        "commonMistakes": [
            {
                "mistake": "'배수재'로 통역",
                "correction": "필터재 = Vật liệu lọc (물은 통과, 토사는 차단), 배수재 = Vật liệu thoát nước (물만 배출)",
                "explanation": "배수재는 물을 배출하는 재료이고, 필터재는 토사를 걸러내는 재료입니다."
            },
            {
                "mistake": "'Vật liệu lọc'만 말하고 입도 범위 생략",
                "correction": "필터재 = Vật liệu lọc (입도 X~Ymm, 투수 계수 Z)",
                "explanation": "입도와 투수 계수를 명시해야 적합한 필터재를 조달할 수 있습니다."
            },
            {
                "mistake": "왕모래를 '모래'로만 통역",
                "correction": "필터재용 왕모래 = Cát sông to dùng làm vật liệu lọc",
                "explanation": "왕모래의 입도(2mm~5mm)를 명시해야 필터재로 적합한지 판단할 수 있습니다."
            }
        ],
        "examples": [
            {
                "ko": "옹벽 뒤 배수층은 필터재 100mm, 배수관 위에 시공합니다.",
                "vi": "Lớp thoát nước sau tường chắn thi công vật liệu lọc dày 100mm, trên ống thoát nước.",
                "situation": "formal"
            },
            {
                "ko": "필터재 입도 시험 결과 2mm~5mm 범위 내입니다.",
                "vi": "Kết quả thí nghiệm cấp phối vật liệu lọc trong khoảng 2mm~5mm.",
                "situation": "formal"
            },
            {
                "ko": "필터재 좀 더 가져와.",
                "vi": "Mang thêm vật liệu lọc.",
                "situation": "onsite"
            }
        ],
        "relatedTerms": ["왕모래", "배수재", "입도", "투수 계수"],
        "difficulty": "advanced",
        "frequency": "medium"
    },
    {
        "slug": "be-tong-lot",
        "korean": "버림콘크리트",
        "vietnamese": "Bê tông lót",
        "hanja": "버림콘크리트",
        "hanjaReading": None,
        "pronunciation": "베똥롯",
        "meaningKo": "기초 바닥이나 슬래브 하부에 얇게 타설하여 평탄한 작업면을 만들고 습기를 차단하는 콘크리트입니다. 구조적 강도보다는 평탄성과 방습 기능이 중요하며, 주로 5~10cm 두께로 시공됩니다. 베트남어로는 'Bê tông lót' 또는 'Bê tông đệm'이며, 한국 현장에서는 '버림콘크리트', '깔콘', '레벨콘크리트'로 불립니다. 통역 시 '기초 콘크리트'와 혼동하지 않도록 주의하세요. 버림콘크리트는 강도 기준이 낮아(보통 18MPa) 구조물에 직접 사용하지 않으며, 철근 배근 전 바닥을 정리하는 용도입니다. 통역사는 발주처가 요구하는 두께와 강도를 확인하고, 양생 기간을 명시하도록 안내하세요.",
        "meaningVi": "Bê tông được đổ mỏng (5~10cm) dưới đáy móng hoặc sàn để tạo mặt phẳng thi công và ngăn ẩm. Tại Hàn Quốc gọi là 'Beorim-concrete(버림콘크리트)', tại Việt Nam thường gọi 'Bê tông lót' hoặc 'Bê tông đệm'. Không dùng làm kết cấu chịu lực mà chủ yếu để san phẳng và chống thấm.",
        "context": "formal",
        "culturalNote": "한국에서는 버림콘크리트를 기초 공사의 첫 단계로 시공하며, KS 기준에서는 강도 18MPa 이상, 두께 5cm 이상을 권장합니다. 베트남은 'Bê tông lót'을 비슷하게 시공하지만, 두께나 강도 기준이 느슨한 경우가 많아 한국 기술진이 재시공을 요구하는 사례가 있습니다. 통역사는 발주처가 버림콘크리트 사양을 요구할 때 두께, 강도, 양생 기간을 명시하고, 필요시 평탄도 기준(±5mm)을 함께 제시하도록 안내하세요. 특히 지하 구조물에서 버림콘크리트가 부실하면 방수층 시공이 어렵고, 이후 누수 문제로 이어질 수 있습니다.",
        "commonMistakes": [
            {
                "mistake": "'기초 콘크리트'로 통역",
                "correction": "버림콘크리트 = Bê tông lót (작업면용), 기초 콘크리트 = Bê tông móng (구조용)",
                "explanation": "버림콘크리트는 구조물이 아니고, 기초 콘크리트는 하중을 지탱하는 구조물입니다."
            },
            {
                "mistake": "'Bê tông'으로만 말하고 'lót' 생략",
                "correction": "버림콘크리트 = Bê tông lót (깔아주는 콘크리트)",
                "explanation": "'lót(깔다)'를 추가해야 버림콘크리트임을 명확히 할 수 있습니다."
            },
            {
                "mistake": "두께를 '5센티'로 오역",
                "correction": "두께 5cm = Dày 5cm (5 centimet)",
                "explanation": "cm(센티미터)를 정확히 표기해야 시공 오류를 막을 수 있습니다."
            }
        ],
        "examples": [
            {
                "ko": "기초 바닥에 버림콘크리트 5cm 타설 후 양생 3일 실시합니다.",
                "vi": "Đổ bê tông lót dày 5cm tại đáy móng, bảo dưỡng 3 ngày.",
                "situation": "formal"
            },
            {
                "ko": "버림콘크리트 평탄도 확인 후 철근 배근 시작하세요.",
                "vi": "Kiểm tra độ phẳng bê tông lót rồi bắt đầu lắp cốt thép.",
                "situation": "onsite"
            },
            {
                "ko": "깔콘 타설 완료.",
                "vi": "Hoàn thành đổ bê tông lót.",
                "situation": "informal"
            }
        ],
        "relatedTerms": ["기초", "평탄도", "양생", "방습"],
        "difficulty": "intermediate",
        "frequency": "high"
    }
]

# JSON 파일 경로
json_path = os.path.join(
    os.path.dirname(os.path.abspath(__file__)),
    "..",
    "data",
    "terms",
    "construction.json"
)

# 기존 데이터 읽기
with open(json_path, "r", encoding="utf-8") as f:
    data = json.load(f)

# 새 용어 추가
data.extend(new_terms)

# 파일 저장
with open(json_path, "w", encoding="utf-8") as f:
    json.dump(data, f, ensure_ascii=False, indent=2)

print(f"✅ {len(new_terms)}개 용어가 {json_path}에 추가되었습니다.")
print("⚠️ 이 스크립트는 실행하지 마세요. Write로 저장만 하세요.")
