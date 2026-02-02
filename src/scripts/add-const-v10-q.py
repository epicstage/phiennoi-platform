#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import json
import os

# Path to construction.json
file_path = os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', 'data', 'terms', 'construction.json')

# Read existing data
with open(file_path, 'r', encoding='utf-8') as f:
    data = json.load(f)  # data is a LIST

# Get existing slugs to prevent duplicates
existing_slugs = {t['slug'] for t in data}

# New terms: 건설 기초 도구/공구 (Basic Construction Tools)
new_terms = [
    {
        "slug": "bua",
        "korean": "망치",
        "vietnamese": "búa",
        "hanja": "亡鎚",
        "hanjaReading": "亡(망할 망) + 鎚(망치 추)",
        "pronunciation": "부아",
        "meaningKo": "못을 박거나 물건을 두드리는 데 사용하는 기본 공구. 건설 현장에서 가장 많이 사용되는 도구 중 하나. 통역 시 주의할 점은 베트남어로 búa đóng đinh(못 박는 망치), búa tạ(해머), búa cao su(고무망치) 등 용도에 따라 세분화되므로 문맥을 정확히 파악해야 합니다. 한국에서는 '해머'라는 외래어도 혼용되지만 베트nam에서는 búa가 표준입니다. 안전교육 시 '망치 사용법'은 cách sử dụng búa an toàn으로 통역하며, 현장에서는 타격 방향과 보호장구 착용을 반드시 언급해야 합니다.",
        "meaningVi": "Dụng cụ cơ bản dùng để đóng đinh hoặc đập vật liệu. Búa là công cụ được sử dụng phổ biến nhất trong công trường xây dựng. Có nhiều loại búa như búa đóng đinh, búa tạ, búa cao su tùy theo mục đích sử dụng. Khi sử dụng búa cần đeo kính bảo hộ và găng tay để đảm bảo an toàn lao động.",
        "context": "안전교육, 공구 대여, 작업 지시",
        "culturalNote": "한국 건설 현장에서는 못박이용 망치와 해체용 해머를 구분하여 사용하며 안전관리가 엄격합니다. 베트남에서는 búa라는 단일 용어로 통칭하는 경우가 많아 통역 시 구체적인 용도를 명시해야 합니다. 한국에서는 공구 관리대장에 개별 등록하지만 베트남에서는 소모품으로 분류하는 경우도 있습니다. 또한 한국은 추락방지를 위해 공구에 안전줄을 의무화하지만 베트남 현장에서는 아직 보편화되지 않았습니다.",
        "commonMistakes": [
            {
                "mistake": "망치를 cái búa로 통역",
                "correction": "búa (단독 사용)",
                "explanation": "베트남어에서 búa는 이미 명사이므로 분류사 cái를 붙이지 않는 것이 자연스럽습니다. 공식 문서나 안전 매뉴얼에서는 búa만 사용합니다."
            },
            {
                "mistake": "'해머'를 búa tạ로만 통역",
                "correction": "문맥에 따라 búa đóng đinh 또는 búa tạ 구분",
                "explanation": "한국어 '해머'는 일반 망치부터 대형 해머까지 포괄하지만, 베트남어는 용도별로 명확히 구분합니다. 못박기용은 búa đóng đinh, 타격용은 búa tạ입니다."
            },
            {
                "mistake": "안전교육에서 '망치질 방법'을 cách đập búa로 통역",
                "correction": "cách sử dụng búa an toàn",
                "explanation": "단순히 '때리는 방법'이 아니라 안전한 사용법을 강조해야 하므로 an toàn(안전)을 반드시 포함해야 합니다."
            },
            {
                "mistake": "공구함을 hộp búa로 통역",
                "correction": "hộp đựng dụng cụ 또는 túi đựng công cụ",
                "explanation": "공구함은 여러 도구를 담는 것이므로 búa(망치)만 지칭하는 표현은 부적절합니다."
            }
        ],
        "examples": [
            {
                "ko": "안전모와 보안경을 착용하고 망치 작업을 시작하세요.",
                "vi": "Đeo mũ bảo hộ và kính bảo hộ trước khi bắt đầu công việc dùng búa.",
                "situation": "formal"
            },
            {
                "ko": "이 못은 큰 망치로 박아야 해요.",
                "vi": "Cái đinh này phải đóng bằng búa to.",
                "situation": "onsite"
            },
            {
                "ko": "망치 손잡이가 헐거워졌으니 교체가 필요합니다.",
                "vi": "Cán búa bị lỏng rồi, cần phải thay mới.",
                "situation": "onsite"
            }
        ],
        "relatedTerms": ["dinh", "oc-vit", "kim-bam", "dung-cu-cam-tay"]
    },
    {
        "slug": "cua",
        "korean": "톱",
        "vietnamese": "cưa",
        "hanja": None,
        "hanjaReading": None,
        "pronunciation": "끄어",
        "meaningKo": "나무나 금속 등을 자르는 데 사용하는 공구. 건설 현장에서는 목재 가공, 거푸집 제작, 마감재 절단 등에 필수적입니다. 통역 시 주의할 점은 베트남어로 cưa tay(수동톱), cưa máy(전동톱), cưa xích(체인톱) 등 동력 유무와 톱날 형태에 따라 명칭이 다르므로 정확히 구분해야 합니다. 한국에서는 '톱'과 '쏘'를 혼용하지만 베트남에서는 cưa가 표준입니다. 안전교육 시 톱날 방향, 보호장구, 분진 관리를 반드시 포함하여 통역해야 하며, 특히 전동공구 사용 시 전원 차단 절차를 명확히 전달해야 합니다.",
        "meaningVi": "Dụng cụ dùng để cắt gỗ, kim loại hoặc vật liệu khác. Cưa là công cụ thiết yếu trong công trường xây dựng để gia công gỗ, cắt ván khuôn, cắt vật liệu hoàn thiện. Có nhiều loại cưa như cưa tay (cưa thủ công), cưa máy (cưa điện), cưa xích (cưa dây chuyền) tùy theo nguồn động lực và hình dạng lưỡi cưa. Khi sử dụng cưa cần chú ý hướng lưỡi cưa, đeo bảo hộ lao động, và kiểm soát bụi gỗ.",
        "context": "목공 작업, 안전교육, 공구 관리",
        "culturalNote": "한국 건설 현장에서는 전동톱 사용 시 자격증(전기기능사 등)을 요구하며 안전교육이 의무화되어 있습니다. 베트남에서는 자격 요건이 상대적으로 덜 엄격하나 최근 안전 규정이 강화되고 있습니다. 한국에서는 톱날 교체 주기를 엄격히 관리하지만 베트남에서는 현장 판단에 맡기는 경우가 많습니다. 또한 한국은 작업 후 톱날 보호 커버를 필수로 장착하지만 베트남 현장에서는 이를 생략하는 사례가 있어 안전 지적 사항이 됩니다.",
        "commonMistakes": [
            {
                "mistake": "전동톱을 cưa điện으로만 통역",
                "correction": "cưa máy 또는 문맥에 따라 cưa đĩa, cưa xích 등 구체화",
                "explanation": "cưa điện은 '전기톱' 일반을 의미하지만, 원형톱(cưa đĩa), 체인톱(cưa xích), 직쏘(cưa lọng) 등 구체적인 톱 종류를 명시하는 것이 정확합니다."
            },
            {
                "mistake": "'톱질하다'를 cắt cưa로 통역",
                "correction": "cưa (동사로 사용)",
                "explanation": "베트남어에서 cưa는 명사이면서 동사로도 사용되므로 cắt(자르다)를 중복으로 붙일 필요가 없습니다."
            },
            {
                "mistake": "톱날을 lưỡi dao로 통역",
                "correction": "lưỡi cưa",
                "explanation": "lưỡi dao는 칼날을 의미하며, 톱날은 lưỡi cưa로 정확히 표현해야 합니다."
            },
            {
                "mistake": "'톱밥'을 bụi gỗ로만 통역",
                "correction": "mùn cưa",
                "explanation": "bụi gỗ는 '목재 분진' 일반을 의미하지만, 톱질로 인한 톱밥은 mùn cưa가 정확한 표현입니다."
            }
        ],
        "examples": [
            {
                "ko": "목재를 자를 때는 반드시 전동톱을 사용하세요.",
                "vi": "Khi cắt gỗ, nhất định phải sử dụng cưa máy.",
                "situation": "formal"
            },
            {
                "ko": "톱날이 무뎌졌으니 새걸로 갈아야겠어요.",
                "vi": "Lưỡi cưa đã cùn rồi, phải thay lưỡi mới.",
                "situation": "onsite"
            },
            {
                "ko": "톱질할 때 보안경 꼭 착용하세요.",
                "vi": "Khi cưa nhớ đeo kính bảo hộ nhé.",
                "situation": "onsite"
            }
        ],
        "relatedTerms": ["may-cat", "luoi-cua", "go", "van-khuon"]
    },
    {
        "slug": "khoan-cam-tay",
        "korean": "핸드드릴",
        "vietnamese": "khoan cầm tay",
        "hanja": None,
        "hanjaReading": None,
        "pronunciation": "콴 껌 따이",
        "meaningKo": "손으로 잡고 사용하는 전동 드릴 공구. 콘크리트, 금속, 목재 등에 구멍을 뚫는 데 사용됩니다. 건설 현장에서는 앵커 설치, 배관 작업, 전기 배선 등 다양한 용도로 활용됩니다. 통역 시 주의할 점은 드릴의 종류(충격드릴, 해머드릴, 일반드릴)에 따라 베트남어 표현이 달라진다는 것입니다. khoan búa(해머드릴), khoan động lực(충격드릴), khoan thường(일반드릴)으로 구분하며, 작업 대상 재료에 따라 적절한 드릴을 지정해야 합니다. 안전교육에서는 드릴 비트 교체 시 전원 차단, 장갑 착용 금지, 회전 방향 확인 등을 명확히 전달해야 합니다.",
        "meaningVi": "Máy khoan cầm tay là dụng cụ điện dùng để khoan lỗ trên bê tông, kim loại, gỗ. Trong công trường xây dựng, máy khoan được sử dụng cho nhiều mục đích như lắp đặt neo, công việc ống nước, lắp đặt đường dây điện. Có các loại khoan khác nhau như khoan búa (máy khoan búa), khoan động lực (máy khoan va đập), khoan thường (máy khoan thông thường) tùy theo vật liệu cần khoan. Khi sử dụng cần chú ý cắt nguồn điện khi thay mũi khoan, không đeo găng tay khi vận hành, và kiểm tra chiều quay.",
        "context": "전기 작업, 앵커 설치, 배관 작업",
        "culturalNote": "한국 건설 현장에서는 전동공구 사용 전 반드시 안전교육을 이수해야 하며, 드릴 비트 규격을 엄격히 관리합니다. 베트남에서는 현장 재량에 맡기는 경우가 많으나 최근 한국 업체 진출로 안전 기준이 높아지고 있습니다. 한국에서는 충전식 드릴(máy khoan pin)이 보편화되었지만 베트남에서는 아직 유선식이 주류입니다. 또한 한국은 드릴 작업 시 분진 마스크 착용을 의무화하지만 베트남 현장에서는 이를 소홀히 하는 경우가 많아 통역 시 반드시 강조해야 합니다.",
        "commonMistakes": [
            {
                "mistake": "'드릴'을 khoan으로만 통역하고 종류 구분 안 함",
                "correction": "khoan búa(해머드릴), khoan động lực(충격드릴), khoan thường(일반드릴) 등 구체화",
                "explanation": "한국어 '드릴'은 포괄적이지만 베트남 현장에서는 작업 대상에 따라 드릴 종류를 정확히 지정해야 안전사고를 예방할 수 있습니다."
            },
            {
                "mistake": "드릴 비트를 mũi khoan máy로 통역",
                "correction": "mũi khoan",
                "explanation": "mũi khoan이 표준 용어이며, máy(기계)를 붙이면 오히려 어색합니다."
            },
            {
                "mistake": "'구멍을 뚫다'를 làm lỗ로 통역",
                "correction": "khoan lỗ",
                "explanation": "làm lỗ는 일반적인 '구멍 내기'이지만, 드릴 작업은 khoan lỗ가 정확한 전문 용어입니다."
            },
            {
                "mistake": "충전식 드릴을 khoan sạc로 통역",
                "correction": "khoan dùng pin 또는 khoan pin",
                "explanation": "sạc는 '충전하다'는 동사이므로, pin(배터리)을 사용하는 것으로 표현하는 것이 자연스럽습니다."
            }
        ],
        "examples": [
            {
                "ko": "콘크리트 벽에 앵커를 설치하려면 해머드릴을 사용해야 합니다.",
                "vi": "Để lắp đặt neo vào tường bê tông, phải sử dụng khoan búa.",
                "situation": "formal"
            },
            {
                "ko": "드릴 비트 10mm짜리로 바꿔주세요.",
                "vi": "Thay mũi khoan 10mm cho tôi.",
                "situation": "onsite"
            },
            {
                "ko": "드릴 쓸 때 장갑 끼면 위험해요.",
                "vi": "Khi dùng khoan, đeo găng tay rất nguy hiểm.",
                "situation": "onsite"
            }
        ],
        "relatedTerms": ["mui-khoan", "khoan-bua", "oc-vit", "neo-dinh"]
    },
    {
        "slug": "may-mai",
        "korean": "그라인더",
        "vietnamese": "máy mài",
        "hanja": None,
        "hanjaReading": None,
        "pronunciation": "마이 마이",
        "meaningKo": "금속, 콘크리트, 석재 등을 연마하거나 절단하는 전동공구. 건설 현장에서는 철근 절단, 용접 부위 연마, 타일 커팅, 녹 제거 등 다양한 작업에 사용됩니다. 통역 시 주의할 점은 그라인더와 디스크 종류를 정확히 구분해야 한다는 것입니다. máy mài góc(앵글 그라인더)이 가장 일반적이며, đĩa cắt(절단 디스크), đĩa mài(연마 디스크), đĩa chà nhám(샌딩 디스크) 등 용도별 디스크 명칭을 숙지해야 합니다. 안전교육에서는 보호 커버 장착, 보안경·안면보호구 착용, 화재 예방, 작업 후 디스크 식힘 대기 등을 반드시 강조해야 하며, 특히 베트남 현장에서 자주 발생하는 보호 커버 제거 관행을 경고해야 합니다.",
        "meaningVi": "Máy mài là công cụ điện dùng để mài, cắt kim loại, bê tông, đá. Trong công trường xây dựng, máy mài được sử dụng cho nhiều công việc như cắt thép, mài mối hàn, cắt gạch, loại bỏ gỉ sét. Máy mài góc là loại phổ biến nhất. Có các loại đĩa khác nhau như đĩa cắt (dùng để cắt), đĩa mài (dùng để mài), đĩa chà nhám (dùng để chà nhám) tùy theo mục đích. Khi sử dụng cần lắp nắp bảo vệ, đeo kính và mặt nạ bảo hộ, phòng cháy, và đợi đĩa nguội sau khi làm việc.",
        "context": "용접 작업, 철근 가공, 타일 시공",
        "culturalNote": "한국 건설 현장에서는 그라인더 사용 전 화재감시자 배치를 의무화하며, 작업 후 1시간 이상 감시를 유지합니다. 베트남에서는 이러한 규정이 덜 엄격하여 화재 사고가 빈번합니다. 한국에서는 보호 커버 제거 시 즉시 작업 중지 조치를 하지만, 베트남 현장에서는 작업 편의를 위해 커버를 제거하는 경우가 많아 통역 시 안전 위험을 명확히 전달해야 합니다. 또한 한국은 디스크 수명을 엄격히 관리하지만 베트남에서는 마모된 디스크를 계속 사용하는 경우가 있어 파손 위험이 큽니다.",
        "commonMistakes": [
            {
                "mistake": "'그라인더'를 máy xay로 통역",
                "correction": "máy mài 또는 máy mài góc",
                "explanation": "máy xay는 '믹서기, 분쇄기'를 의미하며, 건설용 그라인더는 máy mài(연마기)가 정확한 표현입니다."
            },
            {
                "mistake": "'절단 디스크'를 đĩa cắt máy mài로 통역",
                "correction": "đĩa cắt",
                "explanation": "đĩa cắt만으로도 의미가 명확하므로 máy mài를 중복으로 붙일 필요가 없습니다."
            },
            {
                "mistake": "'연마하다'를 làm sạch로 통역",
                "correction": "mài",
                "explanation": "làm sạch는 '깨끗이 하다'는 일반적 표현이지만, 그라인더로 연마하는 작업은 mài가 정확한 전문 용어입니다."
            },
            {
                "mistake": "보호 커버를 vỏ bảo vệ로 통역",
                "correction": "nắp bảo vệ",
                "explanation": "그라인더의 보호 커버는 nắp bảo vệ가 표준 용어이며, vỏ는 '껍질, 외피'를 의미하여 부적절합니다."
            }
        ],
        "examples": [
            {
                "ko": "철근 절단 작업 시에는 반드시 절단 디스크를 사용하고 보안경을 착용하세요.",
                "vi": "Khi cắt thép, nhất định phải dùng đĩa cắt và đeo kính bảo hộ.",
                "situation": "formal"
            },
            {
                "ko": "용접 부위를 그라인더로 매끄럽게 갈아주세요.",
                "vi": "Dùng máy mài để mài nhẵn chỗ hàn.",
                "situation": "onsite"
            },
            {
                "ko": "그라인더 쓸 때 커버 빼면 안 돼요!",
                "vi": "Khi dùng máy mài không được tháo nắp bảo vệ!",
                "situation": "onsite"
            }
        ],
        "relatedTerms": ["dia-cat", "dia-mai", "han", "thep"]
    },
    {
        "slug": "bay-xay",
        "korean": "흙손",
        "vietnamese": "bay xây",
        "hanja": None,
        "hanjaReading": None,
        "pronunciation": "바이 싸이",
        "meaningKo": "모르타르나 시멘트를 바르고 평탄하게 마감하는 데 사용하는 공구. 미장, 타일 시공, 벽돌 쌓기 등에 필수적인 도구입니다. 통역 시 주의할 점은 흙손의 종류와 용도를 정확히 구분해야 한다는 것입니다. bay trét(미장흙손), bay xây gạch(벽돌흙손), bay làm phẳng(평탄흙손) 등으로 세분화되며, 날의 재질(thép không gỉ=스테인리스)과 크기도 명시해야 합니다. 한국에서는 '미장칼'이라고도 하지만 베트남에서는 bay가 표준입니다. 숙련도에 따라 흙손 사용법이 크게 달라지므로, 기술 교육 시 손목 각도, 힘 조절, 마감 타이밍 등을 구체적으로 통역해야 합니다.",
        "meaningVi": "Bay xây là dụng cụ dùng để phết và làm phẳng vữa xi măng hoặc vữa hồ. Đây là công cụ thiết yếu cho công việc trát tường, lát gạch, xây gạch. Có nhiều loại bay như bay trét (bay trát tường), bay xây gạch (bay xây), bay làm phẳng (bay làm phẳng bề mặt) tùy theo mục đích sử dụng. Chất liệu lưỡi bay (thường là thép không gỉ) và kích thước cũng rất quan trọng. Cách sử dụng bay phụ thuộc nhiều vào tay nghề thợ, cần chú ý góc cổ tay, kiểm soát lực, và thời điểm hoàn thiện.",
        "context": "미장 작업, 타일 시공, 벽돌 쌓기",
        "culturalNote": "한국 미장공들은 전통적으로 특정 흙손 브랜드를 선호하며 개인 도구로 소중히 관리합니다. 베트남에서도 숙련공은 자신의 bay를 평생 사용하는 문화가 있습니다. 한국에서는 흙손 날의 유연성(mềm dẻo)을 중시하지만 베트남에서는 단단한(cứng) 흙손을 선호하는 경향이 있어, 작업 방식 차이를 이해해야 합니다. 또한 한국은 마감 품질 기준이 엄격하여 여러 번 반복 작업하지만, 베트남에서는 1차 마감으로 완료하는 경우가 많아 품질 기대치를 조율해야 합니다.",
        "commonMistakes": [
            {
                "mistake": "'흙손'을 dao xây로 통역",
                "correction": "bay xây",
                "explanation": "dao는 '칼'을 의미하며, 흙손은 bay가 정확한 베트남어 표현입니다."
            },
            {
                "mistake": "'미장하다'를 sơn tường로 통역",
                "correction": "trét tường",
                "explanation": "sơn tường는 '벽을 칠하다(페인트)'이고, 미장 작업은 trét tường(회반죽 바르기)입니다."
            },
            {
                "mistake": "'모르타르를 바르다'를 đổ vữa로 통역",
                "correction": "phết vữa 또는 trét vữa",
                "explanation": "đổ는 '붓다'는 의미이고, 흙손으로 바르는 작업은 phết 또는 trét을 사용합니다."
            },
            {
                "mistake": "흙손 크기를 kích thước로만 표현",
                "correction": "구체적인 치수 명시 (ví dụ: bay 20cm, bay 30cm)",
                "explanation": "흙손은 길이에 따라 용도가 다르므로 센티미터 단위로 명확히 지정해야 합니다."
            }
        ],
        "examples": [
            {
                "ko": "벽면 미장 작업에는 30cm 흙손을 사용하세요.",
                "vi": "Để trét tường, hãy sử dụng bay 30cm.",
                "situation": "formal"
            },
            {
                "ko": "모르타르가 마르기 전에 흙손으로 평탄하게 고르세요.",
                "vi": "Trước khi vữa khô, dùng bay làm phẳng bề mặt.",
                "situation": "onsite"
            },
            {
                "ko": "흙손 날이 휘었으니 새걸로 바꿔야겠어요.",
                "vi": "Lưỡi bay bị cong rồi, phải thay bay mới.",
                "situation": "onsite"
            }
        ],
        "relatedTerms": ["vua-ho", "xi-mang", "tret-tuong", "lat-gach"]
    },
    {
        "slug": "thuoc-thuy",
        "korean": "수평기",
        "vietnamese": "thước thủy",
        "hanja": "水平器",
        "hanjaReading": "水(물 수) + 平(평평할 평) + 器(그릇 기)",
        "pronunciation": "툭 투이",
        "meaningKo": "수평 상태를 확인하는 측정 도구. 건설 현장에서 바닥, 벽, 기둥 등이 수평 또는 수직인지 확인하는 데 필수적입니다. 통역 시 주의할 점은 수평기의 종류를 명확히 구분해야 한다는 것입니다. thước thủy bọt khí(기포 수평기), thước thủy laser(레이저 수평기), thước thủy điện tử(전자 수평기) 등으로 세분화되며, 정밀도 요구사항에 따라 적절한 장비를 지정해야 합니다. 한국에서는 '레벨기'라는 외래어도 혼용되지만 베트남에서는 thước thủy가 표준입니다. 측정 시 기준점(điểm chuẩn), 오차 허용범위(dung sai), 보정 방법(cách hiệu chỉnh)을 정확히 전달해야 품질 문제를 예방할 수 있습니다.",
        "meaningVi": "Thước thủy là dụng cụ đo kiểm tra trạng thái thẳng đứng và ngang bằng. Trong công trường xây dựng, thước thủy là công cụ thiết yếu để kiểm tra sàn, tường, cột có thẳng đứng hay ngang bằng không. Có nhiều loại thước thủy như thước thủy bọt khí (thước thủy có bọt khí), thước thủy laser (thước thủy laser), thước thủy điện tử (thước thủy kỹ thuật số) tùy theo yêu cầu độ chính xác. Khi đo cần xác định điểm chuẩn, dung sai cho phép, và phương pháp hiệu chỉnh.",
        "context": "기초 작업, 벽돌 쌓기, 타일 시공",
        "culturalNote": "한국 건설 현장에서는 레이저 수평기가 보편화되어 정밀 시공이 가능하지만, 베트남에서는 아직 기포 수평기가 주류입니다. 한국에서는 수평 오차 허용범위를 mm 단위로 엄격히 관리하지만, 베트남에서는 육안 확인으로 판단하는 경우가 많아 품질 기준 차이가 큽니다. 또한 한국은 수평기 정기 교정(hiệu chuẩn định kỳ)을 의무화하지만 베트남 현장에서는 이를 생략하여 측정 오류가 누적되는 경우가 있습니다. 통역 시 품질 기준과 측정 빈도를 명확히 전달해야 합니다.",
        "commonMistakes": [
            {
                "mistake": "'수평'을 ngang으로만 통역",
                "correction": "thẳng đứng(수직) 또는 ngang bằng(수평) 구분",
                "explanation": "ngang은 '가로'를 의미하지만, 건설에서 수평은 ngang bằng, 수직은 thẳng đứng으로 명확히 구분해야 합니다."
            },
            {
                "mistake": "레이저 수평기를 thước thủy laze로 표기",
                "correction": "thước thủy laser",
                "explanation": "베트남어에서 '레이저'는 laser로 표기하며, laze는 오표기입니다."
            },
            {
                "mistake": "'수평을 맞추다'를 làm ngang로 통역",
                "correction": "căn chỉnh mức 또는 chỉnh thẳng",
                "explanation": "làm ngang은 단순히 '가로로 만들다'이고, 정밀한 수평 조정은 căn chỉnh mức이 적절합니다."
            },
            {
                "mistake": "기포를 bong bóng로 통역",
                "correction": "bọt khí",
                "explanation": "bong bóng은 '풍선'을 의미하며, 수평기의 기포는 bọt khí가 정확한 표현입니다."
            }
        ],
        "examples": [
            {
                "ko": "기초 작업 시 레이저 수평기로 정밀하게 측정하세요.",
                "vi": "Khi làm móng, hãy đo chính xác bằng thước thủy laser.",
                "situation": "formal"
            },
            {
                "ko": "이 벽이 수평이 안 맞네요, 다시 확인해주세요.",
                "vi": "Bức tường này không ngang bằng, kiểm tra lại đi.",
                "situation": "onsite"
            },
            {
                "ko": "수평기 기포가 중앙에 오도록 조정하세요.",
                "vi": "Điều chỉnh sao cho bọt khí thước thủy ở giữa.",
                "situation": "onsite"
            }
        ],
        "relatedTerms": ["thuoc-do", "may-thuy-binh", "kiem-tra-chat-luong", "chuan-xac"]
    },
    {
        "slug": "day-dop",
        "korean": "먹통",
        "vietnamese": "dây dọi",
        "hanja": None,
        "hanjaReading": None,
        "pronunciation": "저이 조이",
        "meaningKo": "수직선을 확인하거나 직선을 표시하는 데 사용하는 도구. 추(dọi)가 달린 줄(dây)을 늘어뜨려 수직을 확인하거나, 먹을 묻힌 줄을 튕겨 직선을 표시합니다. 건설 현장에서는 기둥의 수직 확인, 벽돌 쌓기 기준선, 타일 시공 기준선 등에 사용됩니다. 통역 시 주의할 점은 '먹통'과 '먹줄'의 용도 차이를 구분해야 한다는 것입니다. dây dọi는 주로 수직 확인용이고, dây mực(먹줄)는 직선 표시용입니다. 한국에서는 두 기능을 혼용하지만 베트남에서는 명확히 구분하는 경우가 많습니다. 사용법 설명 시 추의 무게(trọng lượng quả dọi), 줄의 팽창(căng dây), 먹 농도(độ đậm mực) 등을 구체적으로 전달해야 합니다.",
        "meaningVi": "Dây dọi là dụng cụ dùng để kiểm tra đường thẳng đứng hoặc đánh dấu đường thẳng. Sử dụng dây có quả nặng (dọi) treo xuống để kiểm tra độ thẳng đứng, hoặc dùng dây tẩm mực bật lên để đánh dấu đường thẳng. Trong công trường xây dựng, dây dọi được sử dụng để kiểm tra cột thẳng đứng, đường chuẩn xây gạch, đường chuẩn lát gạch. Dây dọi chủ yếu dùng kiểm tra thẳng đứng, còn dây mực dùng để đánh dấu đường thẳng. Khi sử dụng cần chú ý trọng lượng quả dọi, độ căng dây, và độ đậm mực.",
        "context": "기둥 시공, 벽돌 쌓기, 타일 시공",
        "culturalNote": "한국 전통 건축에서 먹통은 목수의 필수 도구로 여겨지며, 숙련된 장인은 먹통 줄을 튕기는 소리만으로 긴장도를 판단합니다. 베트남에서도 dây dọi는 전통 건축에서 중요한 도구이지만, 최근 레이저 장비 도입으로 사용 빈도가 줄고 있습니다. 한국에서는 먹통의 먹(mực)을 정기적으로 보충하고 관리하지만, 베트남 현장에서는 일회용 마커로 대체하는 경우가 증가하고 있습니다. 또한 한국은 수직 확인 시 여러 지점에서 교차 검증하지만 베트남에서는 단일 지점 측정으로 완료하는 경우가 많아 정밀도 차이가 있습니다.",
        "commonMistakes": [
            {
                "mistake": "'먹통'을 hộp mực로 통역",
                "correction": "dây dọi 또는 dây mực",
                "explanation": "hộp mực는 '먹통 케이스'를 의미할 수 있지만, 도구 자체는 dây dọi(수직 확인용) 또는 dây mực(직선 표시용)로 구분해야 합니다."
            },
            {
                "mistake": "'먹줄을 치다'를 đánh dây로 통역",
                "correction": "bật dây mực",
                "explanation": "먹줄을 튕겨서 직선을 표시하는 작업은 bật dây mực가 정확한 표현입니다."
            },
            {
                "mistake": "수직 확인을 kiểm tra thẳng로만 통역",
                "correction": "kiểm tra thẳng đứng",
                "explanation": "thẳng은 일반적인 '곧음'이고, 수직은 thẳng đứng으로 명확히 표현해야 합니다."
            },
            {
                "mistake": "추를 quả nặng로만 표현",
                "correction": "quả dọi",
                "explanation": "quả nặng은 '무거운 물체' 일반을 의미하지만, 먹통의 추는 quả dọi가 전문 용어입니다."
            }
        ],
        "examples": [
            {
                "ko": "기둥이 수직인지 먹통으로 확인하세요.",
                "vi": "Kiểm tra cột có thẳng đứng không bằng dây dọi.",
                "situation": "formal"
            },
            {
                "ko": "벽돌 쌓기 전에 먹줄 쳐주세요.",
                "vi": "Trước khi xây gạch, bật dây mực đánh dấu đi.",
                "situation": "onsite"
            },
            {
                "ko": "먹통 줄이 헐겁네, 다시 팽팽하게 당겨봐요.",
                "vi": "Dây dọi lỏng rồi, căng lại cho chặt.",
                "situation": "onsite"
            }
        ],
        "relatedTerms": ["thuoc-thuy", "may-thuy-binh", "kiem-tra-dung-thang", "chuan-xac"]
    },
    {
        "slug": "cuoc",
        "korean": "곡괭이",
        "vietnamese": "cuốc",
        "hanja": None,
        "hanjaReading": None,
        "pronunciation": "꿕",
        "meaningKo": "땅을 파거나 단단한 지반을 깨는 데 사용하는 수공구. 한쪽 끝은 뾰족하고(mũi nhọn) 다른 쪽은 넓적한(mũi rộng) 형태가 일반적입니다. 건설 현장에서는 토공 작업, 기초 굴착, 콘크리트 파쇄, 암반 작업 등에 사용됩니다. 통역 시 주의할 점은 곡괭이와 괭이(cuốc đất=호미)를 명확히 구분해야 한다는 것입니다. cuốc(곡괭이)는 무거운 타격 공구이고, cuốc đất는 농사용 호미입니다. 한국에서는 '픽(pick)'이라는 외래어도 사용하지만 베트남에서는 cuốc이 표준입니다. 안전교육 시 반동력(lực giật ngược), 파편 비산(văng mảnh vỡ), 발 보호(bảo vệ chân) 등을 반드시 강조해야 합니다.",
        "meaningVi": "Cuốc là dụng cụ thủ công dùng để đào đất hoặc phá nền cứng. Thường có một đầu nhọn (mũi nhọn) và một đầu rộng (mũi rộng). Trong công trường xây dựng, cuốc được sử dụng cho công việc đào đất, đào móng, phá bê tông, làm việc với đá. Cần phân biệt rõ cuốc (cuốc đào, công cụ đập nặng) và cuốc đất (cuốc làm vườn nhẹ). Khi huấn luyện an toàn cần nhấn mạnh lực giật ngược, mảnh vỡ văng ra, và bảo vệ chân.",
        "context": "토공 작업, 기초 굴착, 해체 작업",
        "culturalNote": "한국 건설 현장에서는 토공 작업 대부분이 기계화되어 곡괭이 사용이 줄었지만, 좁은 공간이나 정밀 작업에서는 여전히 필수입니다. 베트남에서는 인건비가 낮아 수작업 비중이 높아 곡괭이가 더 많이 사용됩니다. 한국에서는 곡괭이 자루(cán cuốc)의 길이와 재질을 규격화하지만 베트남에서는 현장 제작하는 경우가 많아 안전성이 떨어집니다. 또한 한국은 곡괭이 작업 시 안전화 착용을 의무화하지만, 베트남 현장에서는 맨발이나 샌들 착용 사례가 있어 부상 위험이 큽니다.",
        "commonMistakes": [
            {
                "mistake": "'곡괭이'를 cuốc đất로 통역",
                "correction": "cuốc (단독) 또는 cuốc đào",
                "explanation": "cuốc đất는 농사용 호미를 의미하며, 건설용 곡괭이는 cuốc 또는 cuốc đào로 구분해야 합니다."
            },
            {
                "mistake": "'땅을 파다'를 cắt đất로 통역",
                "correction": "đào đất",
                "explanation": "cắt는 '자르다'이고, 곡괭이로 땅을 파는 작업은 đào가 적절합니다."
            },
            {
                "mistake": "곡괭이 자루를 que cuốc로 통역",
                "correction": "cán cuốc",
                "explanation": "que는 '막대기'를 의미하며, 공구의 자루는 cán이 정확한 용어입니다."
            },
            {
                "mistake": "'콘크리트를 깨다'를 phá bê tông로만 통역",
                "correction": "đục bê tông 또는 đập bê tông",
                "explanation": "phá는 '파괴하다' 일반이고, 곡괭이로 깨는 작업은 đục(쪼다) 또는 đập(때리다)이 더 구체적입니다."
            }
        ],
        "examples": [
            {
                "ko": "단단한 지반은 곡괭이로 먼저 풀어주세요.",
                "vi": "Nền đất cứng thì dùng cuốc đục lỏng ra trước.",
                "situation": "formal"
            },
            {
                "ko": "곡괭이 쓸 때 발 조심해요!",
                "vi": "Khi dùng cuốc cẩn thận chân nhé!",
                "situation": "onsite"
            },
            {
                "ko": "곡괭이 자루가 부러졌으니 새걸로 교체하세요.",
                "vi": "Cán cuốc gãy rồi, thay cái mới đi.",
                "situation": "onsite"
            }
        ],
        "relatedTerms": ["xeng", "dao-dat", "xe-rua", "dung-cu-tho-cong"]
    },
    {
        "slug": "xeng",
        "korean": "삽",
        "vietnamese": "xẻng",
        "hanja": None,
        "hanjaReading": None,
        "pronunciation": "쌩",
        "meaningKo": "흙, 모래, 자갈 등을 뜨거나 옮기는 데 사용하는 공구. 건설 현장에서는 토공 작업, 콘크리트 타설, 자재 이동 등에 필수적입니다. 통역 시 주의할 점은 삽의 종류를 용도에 따라 구분해야 한다는 것입니다. xẻng xúc(퍼내는 삽), xẻng cuốc(파는 삽), xẻng vuông(각삽), xẻng tròn(둥근 삽) 등으로 세분화되며, 날의 형태와 재질을 명시해야 합니다. 한국에서는 '스콥(scoop)'이라는 외래어도 사용하지만 베트남에서는 xẻng이 표준입니다. 작업 자세 교육 시 허리 각도(góc lưng), 무게 중심(trọng tâm), 반복 동작 주의(cẩn thận động tác lặp lại) 등을 강조하여 근골격계 질환을 예방해야 합니다.",
        "meaningVi": "Xẻng là dụng cụ dùng để xúc hoặc chuyển đất, cát, sỏi. Trong công trường xây dựng, xẻng là công cụ thiết yếu cho công việc đào đất, đổ bê tông, di chuyển vật liệu. Có nhiều loại xẻng như xẻng xúc (xẻng xúc lên), xẻng cuốc (xẻng đào), xẻng vuông (xẻng vuông), xẻng tròn (xẻng tròn) tùy theo mục đích sử dụng. Khi huấn luyện tư thế làm việc cần nhấn mạnh góc lưng, trọng tâm, và cẩn thận động tác lặp lại để phòng ngừa bệnh cơ xương khớp.",
        "context": "토공 작업, 콘크리트 타설, 자재 이동",
        "culturalNote": "한국 건설 현장에서는 대부분의 토공 작업이 기계화되어 삽 사용이 줄었지만, 마감 작업과 좁은 공간에서는 여전히 필수입니다. 베트남에서는 인력 작업 비중이 높아 삽이 더 많이 사용됩니다. 한국에서는 인체공학적 삽(손잡이 각도 조절 등)을 도입하고 있지만 베트남에서는 전통적인 직선형 삽이 주류입니다. 또한 한국은 삽 작업 시 허리 보호대 착용을 권장하지만, 베트남 현장에서는 이를 소홀히 하여 요통 발생률이 높습니다. 통역 시 작업 자세와 안전 장비 착용을 명확히 전달해야 합니다.",
        "commonMistakes": [
            {
                "mistake": "'삽'을 cái xẻng로 통역",
                "correction": "xẻng (단독 사용)",
                "explanation": "베트남어에서 xẻng은 이미 명사이므로 분류사 cái를 붙이지 않는 것이 자연스럽습니다."
            },
            {
                "mistake": "'흙을 뜨다'를 lấy đất로 통역",
                "correction": "xúc đất",
                "explanation": "lấy는 '가져오다' 일반이고, 삽으로 흙을 뜨는 작업은 xúc가 정확한 동사입니다."
            },
            {
                "mistake": "각삽을 xẻng hình vuông로 통역",
                "correction": "xẻng vuông",
                "explanation": "hình vuông는 '사각형 모양'이고, 각삽은 xẻng vuông가 간결한 표현입니다."
            },
            {
                "mistake": "삽 자루를 tay cầm xẻng로 통역",
                "correction": "cán xẻng",
                "explanation": "tay cầm은 '손잡이' 일반이고, 공구 자루는 cán이 전문 용어입니다."
            }
        ],
        "examples": [
            {
                "ko": "콘크리트 타설 시 삽으로 골고루 펴주세요.",
                "vi": "Khi đổ bê tông, dùng xẻng trải đều.",
                "situation": "formal"
            },
            {
                "ko": "모래 한 삽 더 넣어주세요.",
                "vi": "Cho thêm một xẻng cát nữa.",
                "situation": "onsite"
            },
            {
                "ko": "삽질할 때 허리 조심하세요!",
                "vi": "Khi xúc đất cẩn thận lưng nhé!",
                "situation": "onsite"
            }
        ],
        "relatedTerms": ["cuoc", "dat", "cat", "be-tong"]
    },
    {
        "slug": "xe-rua",
        "korean": "손수레",
        "vietnamese": "xe rùa",
        "hanja": None,
        "hanjaReading": None,
        "pronunciation": "쎄 주어",
        "meaningKo": "흙, 자재, 잡석 등을 운반하는 한 바퀴 또는 두 바퀴 수레. 건설 현장에서 소량 자재 운반, 콘크리트 이동, 폐기물 처리 등에 사용됩니다. 통역 시 주의할 점은 손수레의 종류를 구분해야 한다는 것입니다. xe rùa một bánh(외바퀴 손수레), xe rùa hai bánh(쌍바퀴 손수레), xe đẩy(밀차) 등으로 세분화되며, 적재 용량(sức chứa)과 타이어 종류(bánh cao su=고무 바퀴)도 명시해야 합니다. 한국에서는 '외발 수레', '쌍발 수레'라고도 하지만 베트남에서는 xe rùa가 가장 보편적입니다. 안전교육 시 과적(quá tải) 금지, 경사로 작업 주의(cẩn thận khi đi dốc), 바퀴 정기 점검(kiểm tra bánh xe định kỳ)을 강조해야 합니다.",
        "meaningVi": "Xe rùa là xe đẩy một hoặc hai bánh dùng để chuyển đất, vật liệu, đá dăm. Trong công trường xây dựng, xe rùa được sử dụng để vận chuyển vật liệu số lượng nhỏ, di chuyển bê tông, xử lý chất thải. Có nhiều loại xe rùa như xe rùa một bánh (xe rùa một bánh), xe rùa hai bánh (xe rùa hai bánh), xe đẩy (xe đẩy). Cần chú ý sức chứa và loại bánh xe (bánh cao su). Khi huấn luyện an toàn cần nhấn mạnh cấm quá tải, cẩn thận khi đi dốc, và kiểm tra bánh xe định kỳ.",
        "context": "자재 운반, 토공 작업, 폐기물 처리",
        "culturalNote": "한국 건설 현장에서는 손수레 사용이 줄고 소형 운반차(xe vận chuyển nhỏ)로 대체되고 있지만, 좁은 통로나 계단 작업에서는 여전히 필수입니다. 베트남에서는 인건비 때문에 손수레가 더 많이 사용됩니다. 한국에서는 손수레 적재 용량을 엄격히 제한하지만 베트남에서는 과적 사례가 빈번하여 전복 사고가 발생합니다. 또한 한국은 손수레 바퀴를 정기적으로 교체하지만 베트남에서는 마모된 바퀴를 계속 사용하는 경우가 많아 조향 불능 위험이 있습니다. 통역 시 안전 적재량과 유지보수 필요성을 명확히 전달해야 합니다.",
        "commonMistakes": [
            {
                "mistake": "'손수레'를 xe đẩy tay로만 통역",
                "correction": "xe rùa (건설용) 또는 xe đẩy (일반용)",
                "explanation": "건설 현장에서는 xe rùa가 표준 용어이며, xe đẩy는 일반적인 밀차를 의미합니다."
            },
            {
                "mistake": "'외바퀴 수레'를 xe một bánh로 통역",
                "correction": "xe rùa một bánh",
                "explanation": "xe một bánh는 '한 바퀴 차량' 일반을 의미하며, 건설용 손수레는 xe rùa một bánh가 정확합니다."
            },
            {
                "mistake": "'수레를 밀다'를 đẩy xe로만 통역",
                "correction": "đẩy xe rùa",
                "explanation": "xe는 차량 일반이므로, 손수레를 명확히 지칭하려면 xe rùa를 사용해야 합니다."
            },
            {
                "mistake": "과적을 chở nhiều로 통역",
                "correction": "quá tải",
                "explanation": "chở nhiều는 '많이 싣다'는 중립적 표현이고, 안전 위반인 과적은 quá tải로 명확히 표현해야 합니다."
            }
        ],
        "examples": [
            {
                "ko": "손수레에 자재를 과적하지 말고 안전 용량을 지키세요.",
                "vi": "Không được chở quá tải trên xe rùa, phải tuân thủ sức chứa an toàn.",
                "situation": "formal"
            },
            {
                "ko": "경사로에서 손수레 조심해서 밀어요.",
                "vi": "Cẩn thận đẩy xe rùa ở đường dốc.",
                "situation": "onsite"
            },
            {
                "ko": "손수레 바퀴가 빠졌으니 수리가 필요해요.",
                "vi": "Bánh xe rùa bị tuột rồi, cần sửa chữa.",
                "situation": "onsite"
            }
        ],
        "relatedTerms": ["van-chuyen", "tai-lieu", "cuoc", "xeng"]
    }
]

# Filter out duplicates
new_terms_filtered = [t for t in new_terms if t['slug'] not in existing_slugs]

print(f"Found {len(existing_slugs)} existing terms")
print(f"Adding {len(new_terms_filtered)} new terms (filtered {len(new_terms) - len(new_terms_filtered)} duplicates)")

# Extend data with new terms
data.extend(new_terms_filtered)

# Write back to file
with open(file_path, 'w', encoding='utf-8') as f:
    json.dump(data, f, ensure_ascii=False, indent=2)

print(f"✅ Successfully added {len(new_terms_filtered)} construction tool terms")
print("New terms:", [t['slug'] for t in new_terms_filtered])
