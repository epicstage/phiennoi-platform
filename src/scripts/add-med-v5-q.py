#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
치과/안과/이비인후과 전문용어 10개 추가 스크립트
Tier S 품질 기준 (90점 이상) 준수
"""

import json
import os

# 파일 경로 설정
file_path = os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', 'data', 'terms', 'medical.json')

# 추가할 용어 데이터 (Tier S 기준)
new_terms = [
    {
        "slug": "dieu-tri-sau-rang",
        "korean": "충치치료",
        "vietnamese": "Điều trị sâu răng",
        "hanja": "蟲齒治療",
        "hanjaReading": "蟲(벌레 충) + 齒(이 치) + 治(다스릴 치) + 療(치료할 료)",
        "pronunciation": "디에우찌사우장",
        "meaningKo": "치아가 세균에 의해 썩은 부분을 제거하고 수복재로 메우는 치료. 통역 시 주의할 점은 베트남에서는 'Hàn răng(하언장, 이때우기)'라는 표현을 더 자주 쓰므로 환자가 이해하기 쉽게 병기해야 함. 베트남 환자들은 충치를 방치하는 경우가 많아 진행 단계(초기/중기/말기)를 명확히 설명하는 것이 중요. 한국의 레진 치료와 아말감 치료 차이를 베트남어로 구분해 설명할 수 있어야 하며, 보험 적용 여부도 실수 없이 전달해야 함.",
        "meaningVi": "Quy trình loại bỏ phần răng bị vi khuẩn phá hủy và trám lại bằng vật liệu phục hồi. Ở Việt Nam thường dùng thuật ngữ 'Hàn răng' (trám răng) cho cùng một khái niệm. Bệnh nhân Việt Nam thường đến khám muộn nên cần giải thích rõ mức độ sâu răng và phương pháp điều trị tương ứng.",
        "context": "치과 진료실, 치료 상담, 보험 청구",
        "culturalNote": "한국은 예방 중심의 정기 검진 문화가 발달했지만 베트남은 통증이 심해진 후에야 치과를 찾는 경우가 많음. 따라서 베트남 환자는 신경치료(Điều trị tủy răng)까지 필요한 경우가 빈번하므로 충치치료와 신경치료의 차이를 명확히 구분해 설명해야 함. 또한 한국의 레진 치료 비용이 베트남보다 높아 비용 설명 시 오해 방지가 필수.",
        "commonMistakes": [
            {
                "mistake": "충치치료를 'Chữa răng sâu'로만 번역",
                "correction": "'Điều trị sâu răng' 또는 'Hàn răng' 병기",
                "explanation": "베트남 환자들은 'Hàn răng'라는 표현에 더 익숙하므로 함께 설명해야 이해도가 높아짐"
            },
            {
                "mistake": "레진과 아말감을 구분 없이 'trám răng'로 통칭",
                "correction": "레진은 'Trám composite', 아말감은 'Trám amalgam'으로 구분",
                "explanation": "재료에 따라 비용과 심미성이 크게 달라 환자 선택권 보장을 위해 정확한 용어 사용 필요"
            },
            {
                "mistake": "충치 단계를 설명 없이 'sâu răng'로만 표현",
                "correction": "초기(Giai đoạn đầu), 중기(Giai đoạn giữa), 말기(Giai đoạn nặng) 구분",
                "explanation": "치료 방법과 비용이 단계별로 달라지므로 환자가 현재 상태를 정확히 이해할 수 있도록 해야 함"
            }
        ],
        "examples": [
            {
                "ko": "충치가 신경까지 진행되지 않아서 간단한 치료로 가능합니다.",
                "vi": "Răng sâu chưa tổn thương đến tủy nên có thể điều trị đơn giản bằng cách hàn răng.",
                "situation": "formal"
            },
            {
                "ko": "어금니 충치는 레진으로 때우는 게 좋을까요, 아말감으로 할까요?",
                "vi": "Răng hàm sâu nên trám bằng composite hay amalgam ạ?",
                "situation": "onsite"
            },
            {
                "ko": "충치 부위를 깎아내고 하얀 재료로 메웠어요.",
                "vi": "Đã đào bỏ phần sâu răng và trám lại bằng vật liệu màu trắng rồi ạ.",
                "situation": "informal"
            }
        ],
        "relatedTerms": ["신경치료", "치아우식증", "레진", "스케일링", "치아보존과"]
    },
    {
        "slug": "cao-voi-rang",
        "korean": "스케일링",
        "vietnamese": "Cạo vôi răng",
        "hanja": None,
        "hanjaReading": None,
        "pronunciation": "까오보이장",
        "meaningKo": "치아 표면과 잇몸 아래에 쌓인 치석을 초음파 기구로 제거하는 예방 치료. 통역 시 베트남어 'Lấy cao răng(라이까오장)'도 함께 설명하면 환자 이해도가 높아짐. 한국에서는 연 1회 보험 적용되지만 베트ناㅁ에서는 보험 적용이 제한적이라는 점을 사전에 안내해야 비용 관련 오해를 방지할 수 있음. 시술 후 일시적 시림 증상(ê buốt răng)에 대해서도 미리 설명하는 것이 중요.",
        "meaningVi": "Thủ thuật loại bỏ mảng bám và cao răng tích tụ trên bề mặt răng và dưới nướu bằng máy siêu âm. Là phương pháp dự phòng quan trọng để ngăn ngừa viêm nướu và bệnh nha chu. Ở Hàn Quốc được bảo hiểm y tế chi trả 1 lần/năm.",
        "context": "치과 정기검진, 예방치료 상담, 보험 적용 안내",
        "culturalNote": "한국은 스케일링을 연례 예방 관리 차원에서 받는 문화가 정착됐으나 베트남은 아직 치료 중심 사고가 강해 증상이 없으면 받지 않는 경우가 많음. 한국 건강보험 적용(연 1회)과 베트남 보험의 제한적 적용 차이를 설명해야 하며, 시술 후 며칠간 시린 증상이 정상임을 사전 안내하지 않으면 환자가 의료 사고로 오해할 수 있음.",
        "commonMistakes": [
            {
                "mistake": "'스케일링'을 'Làm sạch răng'로 번역",
                "correction": "'Cạo vôi răng' 또는 'Lấy cao răng' 사용",
                "explanation": "'Làm sạch răng'은 단순 치아 청소를 의미하여 전문 치석 제거 시술의 의미가 약해짐"
            },
            {
                "mistake": "시술 후 시림을 'tác dụng phụ(부작용)'로 표현",
                "correction": "'Hiện tượng bình thường(정상 현상)' 또는 'Tạm thời(일시적)'로 설명",
                "explanation": "부작용으로 표현하면 환자가 치료 실패로 오해할 수 있음"
            },
            {
                "mistake": "보험 적용을 확인 없이 '보험 된다'고 단정",
                "correction": "'Ở Hàn Quốc bảo hiểm chi trả 1 lần/năm' 명시",
                "explanation": "베트남 보험 체계와 다르므로 한국 보험 기준임을 명확히 해야 함"
            }
        ],
        "examples": [
            {
                "ko": "스케일링은 보험으로 1년에 한 번 받을 수 있습니다.",
                "vi": "Cạo vôi răng được bảo hiểm y tế chi trả 1 lần mỗi năm ở Hàn Quốc.",
                "situation": "formal"
            },
            {
                "ko": "스케일링 받고 나서 며칠 동안 이가 시릴 수 있어요.",
                "vi": "Sau khi cạo vôi răng có thể bị ê buốt răng vài ngày, đây là hiện tượng bình thường.",
                "situation": "onsite"
            },
            {
                "ko": "치석이 많이 쌓여서 스케일링 꼭 받으셔야 해요.",
                "vi": "Cao răng đã đóng nhiều nên bạn nhất định phải lấy cao răng nhé.",
                "situation": "informal"
            }
        ],
        "relatedTerms": ["치석", "치주질환", "잇몸염증", "예방치료", "치아미백"]
    },
    {
        "slug": "cay-ghep-rang",
        "korean": "임플란트",
        "vietnamese": "Cấy ghép răng",
        "hanja": None,
        "hanjaReading": None,
        "pronunciation": "까이겝장",
        "meaningKo": "상실된 치아를 대체하기 위해 인공 치근을 잇몸뼈에 심고 그 위에 보철물을 씌우는 치료. 통역 시 베트남어 'Implant răng(임쁠란트장)' 용어도 통용되므로 병기 설명 필요. 한국은 임플란트가 대중화됐으나 베트남에서는 고가 치료로 인식되어 브릿지(Cầu răng)나 틀니(Hàm giả)를 선호하는 경향이 있음을 이해해야 함. 수술 과정, 골이식 필요 여부, 치유 기간(3~6개월)을 단계별로 설명하는 것이 환자 신뢰 확보에 중요.",
        "meaningVi": "Phương pháp phục hồi răng mất bằng cách cấy trụ titan nhân tạo vào xương hàm và gắn răng sứ lên trên. Là giải pháp vĩnh viễn thay thế răng đã mất, giúp bảo vệ xương hàm không bị tiêu. Ở Việt Nam thuật ngữ 'Implant răng' cũng được sử dụng phổ biến.",
        "context": "치과 임플란트 상담, 치료 계획, 비용 안내",
        "culturalNote": "한국에서는 임플란트가 노년층 표준 치료로 자리잡았고 보험 적용(만 65세 이상 2개)도 되지만, 베트남에서는 여전히 고가 시술로 인식되어 경제적 여유가 있는 층만 선택함. 베트남 환자들은 브릿지(Cầu răng)나 틀니(Hàm giả)를 먼저 고려하므로 임플란트의 장기적 장점(뼈 보존, 인접 치아 보호)을 설명해야 선택에 도움이 됨. 또한 한국의 빠른 시술 시스템(당일 임플란트 등)이 베트남에서는 생소하므로 과정 설명이 필수.",
        "commonMistakes": [
            {
                "mistake": "임플란트를 'Răng giả(가짜 이)'로 번역",
                "correction": "'Cấy ghép răng' 또는 'Implant răng' 사용",
                "explanation": "'Răng giả'는 틀니를 연상시켜 임플란트의 영구적 특성이 전달되지 않음"
            },
            {
                "mistake": "골이식을 설명 없이 'ghép xương'로만 표현",
                "correction": "'Ghép xương hàm để đủ điều kiện cấy implant' 구체화",
                "explanation": "왜 골이식이 필요한지 맥락 설명이 없으면 환자가 추가 비용에 불만을 가질 수 있음"
            },
            {
                "mistake": "치유 기간을 '몇 달'로 애매하게 표현",
                "correction": "'3-6 tháng(3~6개월)' 구체적 기간 명시",
                "explanation": "정확한 기간 안내가 없으면 환자가 치료 일정 계획을 세우기 어려움"
            }
        ],
        "examples": [
            {
                "ko": "임플란트는 뼈에 인공치근이 붙는데 3개월 정도 걸립니다.",
                "vi": "Cấy ghép răng cần khoảng 3 tháng để trụ implant liền với xương hàm.",
                "situation": "formal"
            },
            {
                "ko": "뼈가 부족해서 먼저 뼈이식하고 임플란트 해야 할 것 같아요.",
                "vi": "Xương hàm không đủ nên phải ghép xương trước rồi mới cấy implant được ạ.",
                "situation": "onsite"
            },
            {
                "ko": "임플란트 하면 자기 치아처럼 쓸 수 있어요.",
                "vi": "Làm implant thì có thể dùng như răng thật của mình.",
                "situation": "informal"
            }
        ],
        "relatedTerms": ["골이식", "인공치근", "틀니", "브릿지", "보철치료"]
    },
    {
        "slug": "phau-thuat-duc-thuy-tinh-the",
        "korean": "백내장수술",
        "vietnamese": "Phẫu thuật đục thủy tinh thể",
        "hanja": "白內障手術",
        "hanjaReading": "白(흰 백) + 內(안 내) + 障(막을 장) + 手(손 수) + 術(재주 술)",
        "pronunciation": "퍼우투엇둑투이틴테",
        "meaningKo": "눈의 수정체가 혼탁해져 시력이 저하되는 백내장을 치료하기 위해 혼탁한 수정체를 제거하고 인공수정체를 삽입하는 수술. 통역 시 베트남 환자들이 'mổ mắt(모맛, 눈수술)'라는 일반 표현을 쓰는 경우가 많으므로 정확한 병명 'đục thủy tinh thể'를 함께 설명해야 함. 한국은 당일 퇴원이 일반적이나 베트남에서는 입원 수술로 인식하는 경우가 있어 시술 과정과 회복 기간을 명확히 안내하는 것이 중요. 다초점 인공수정체 옵션 설명 시 비용 차이도 투명하게 전달해야 함.",
        "meaningVi": "Phẫu thuật loại bỏ thủy tinh thể bị đục mờ và thay thế bằng thủy tinh thể nhân tạo để phục hồi thị lực. Là phẫu thuật phổ biến ở người cao tuổi khi thủy tinh thể mắt bị lão hóa. Ở Hàn Quốc thường thực hiện ngoại trú và bệnh nhân về nhà trong ngày.",
        "context": "안과 수술 상담, 노인성 질환 설명, 시력 회복 치료",
        "culturalNote": "한국에서는 백내장 수술이 매우 대중화되어 당일 수술 후 귀가가 일반적이지만, 베트남에서는 여전히 큰 수술로 인식되어 입원을 기대하는 환자가 많음. 따라서 수술 과정의 간편함과 안전성을 강조해야 불안감을 줄일 수 있음. 또한 한국의 다초점 인공수정체(Thủy tinh thể đa tiêu cự) 옵션이 베트남보다 다양하고 비용이 높을 수 있어, 단초점과 다초점의 차이를 비용과 함께 설명하는 것이 필수.",
        "commonMistakes": [
            {
                "mistake": "백내장을 'mờ mắt(눈 흐림)'로 설명",
                "correction": "'Đục thủy tinh thể(수정체 혼탁)' 정확한 병명 사용",
                "explanation": "'Mờ mắt'은 증상일 뿐 병명이 아니므로 환자가 질환을 정확히 이해하지 못함"
            },
            {
                "mistake": "인공수정체 종류를 구분 없이 'thủy tinh thể nhân tạo'로만 표현",
                "correction": "단초점(đơn tiêu cự), 다초점(đa tiêu cự) 구분 설명",
                "explanation": "종류에 따라 비용과 기능이 크게 달라 선택권 보장을 위해 정확한 구분 필요"
            },
            {
                "mistake": "회복 기간을 '금방 좋아진다'로 애매하게 표현",
                "correction": "'1-2 tuần phục hồi hoàn toàn(1~2주 완전 회복)' 구체화",
                "explanation": "구체적 기간 안내가 없으면 환자가 일상 복귀 시점을 판단하기 어려움"
            }
        ],
        "examples": [
            {
                "ko": "백내장 수술은 20분 정도 걸리고 당일 퇴원 가능합니다.",
                "vi": "Phẫu thuật đục thủy tinh thể mất khoảng 20 phút và có thể xuất viện trong ngày.",
                "situation": "formal"
            },
            {
                "ko": "다초점 렌즈로 하면 돋보기 없이도 잘 보여요.",
                "vi": "Nếu dùng thủy tinh thể đa tiêu cự thì không cần kính lão cũng nhìn rõ ạ.",
                "situation": "onsite"
            },
            {
                "ko": "수술 후 일주일은 눈에 물 들어가지 않게 조심하세요.",
                "vi": "Sau mổ 1 tuần thì cẩn thận đừng để nước vào mắt nhé.",
                "situation": "informal"
            }
        ],
        "relatedTerms": ["인공수정체", "수정체", "시력회복", "노인성질환", "안과수술"]
    },
    {
        "slug": "kiem-tra-thi-luc",
        "korean": "시력검사",
        "vietnamese": "Kiểm tra thị lực",
        "hanja": "視力檢査",
        "hanjaReading": "視(볼 시) + 力(힘 력) + 檢(조사할 검) + 査(조사할 사)",
        "pronunciation": "끼엠짜티륵",
        "meaningKo": "눈의 시력 상태를 측정하는 기본 검사. 통역 시 베트남어 'Khám mắt(캄맛, 눈검사)'와 구분하여 설명해야 함. 시력검사는 단순 시력 측정이지만 'Khám mắt'는 종합 안과 검진을 의미하므로 범위 차이를 명확히 해야 오해가 없음. 나안시력(Thị lực không kính)과 교정시력(Thị lực có kính) 개념도 함께 설명하는 것이 중요하며, 시력 표기법(1.0, 20/20 등)의 차이도 안내해야 함.",
        "meaningVi": "Xét nghiệm đo khả năng nhìn của mắt bằng bảng chữ E hoặc chữ C. Là bước kiểm tra cơ bản để xác định mức độ cận thị, viễn thị hay loạn thị. Kết quả thị lực được biểu thị bằng số như 1.0, 0.8 ở Hàn Quốc hoặc 20/20, 20/40 theo chuẩn quốc tế.",
        "context": "안과 검진, 안경 처방, 건강검진",
        "culturalNote": "한국은 시력검사가 무료 또는 저렴하게 제공되는 경우가 많지만 베트남에서는 유료인 경우가 일반적이라는 점을 안내하면 비용 관련 오해를 방지할 수 있음. 또한 한국의 정밀 굴절검사(Khúc xạ chính xác)와 단순 시력검사의 차이를 설명하지 않으면 환자가 검사 비용에 의문을 가질 수 있음. 시력 표기법도 국가별로 다르므로(한국 1.0 = 베트남 10/10) 환자가 이해할 수 있도록 변환 설명이 필요.",
        "commonMistakes": [
            {
                "mistake": "시력검사를 'Khám mắt'로 통칭",
                "correction": "'Kiểm tra thị lực' 또는 'Đo thị lực' 사용",
                "explanation": "'Khám mắt'는 종합 안과 검진을 의미하여 단순 시력 측정과 범위가 다름"
            },
            {
                "mistake": "시력 수치를 그대로 번역 (예: '1.0은 1.0')",
                "correction": "'Thị lực 1.0 tương đương 10/10 theo chuẩn Việt Nam' 설명",
                "explanation": "표기 방식이 다르므로 환자가 자국 기준으로 이해할 수 있도록 변환 필요"
            },
            {
                "mistake": "나안시력과 교정시력 구분 없이 '시력'으로만 표현",
                "correction": "나안(không kính), 교정(có kính) 명시",
                "explanation": "안경 착용 여부에 따라 시력이 크게 달라지므로 구분 표기 필수"
            }
        ],
        "examples": [
            {
                "ko": "시력검사 결과 나안시력 0.3, 교정시력 1.0입니다.",
                "vi": "Kết quả kiểm tra thị lực không kính là 0.3, có kính là 1.0 (tương đương 10/10).",
                "situation": "formal"
            },
            {
                "ko": "시력검사 먼저 하고 필요하면 정밀검사 할게요.",
                "vi": "Làm kiểm tra thị lực cơ bản trước, nếu cần sẽ làm thêm khúc xạ chính xác ạ.",
                "situation": "onsite"
            },
            {
                "ko": "시력이 많이 떨어져서 안경 도수 높여야 할 것 같아요.",
                "vi": "Thị lực giảm nhiều rồi, có lẽ phải tăng độ kính lên.",
                "situation": "informal"
            }
        ],
        "relatedTerms": ["나안시력", "교정시력", "굴절검사", "안경처방", "시력표"]
    },
    {
        "slug": "tang-nhan-ap",
        "korean": "녹내장",
        "vietnamese": "Tăng nhãn áp",
        "hanja": "綠內障",
        "hanjaReading": "綠(푸를 록) + 內(안 내) + 障(막을 장)",
        "pronunciation": "땅년압",
        "meaningKo": "안압이 높아져 시신경이 손상되어 시야가 좁아지는 만성 안과 질환. 통역 시 베트남어 'Glôcôm(글로콤)' 용어도 널리 쓰이므로 병기 설명 필요. 한국 환자들은 '녹내장'이라는 병명에 익숙하지만 베트남 환자들은 'Tăng nhãn áp(안압 상승)'이라는 증상명으로 이해하는 경우가 많아 시신경 손상과 실명 위험을 강조해 심각성을 전달해야 함. 정기 안압 검사의 중요성과 평생 약물 치료 필요성을 명확히 설명하는 것이 환자 순응도 향상에 중요.",
        "meaningVi": "Bệnh lý nhãn khoa mãn tính do tăng áp lực nội nhãn gây tổn thương dây thần kinh thị giác, dẫn đến thu hẹp thị trường và có thể mù lòa nếu không điều trị. Thuật ngữ 'Glôcôm' (Glaucoma) cũng được sử dụng phổ biến. Cần điều trị suốt đời bằng thuốc nhỏ mắt hoặc phẫu thuật.",
        "context": "안과 만성질환 관리, 안압 측정, 실명 예방",
        "culturalNote": "한국에서는 녹내장이 3대 실명 질환으로 잘 알려져 있고 정기 검진 인식이 높지만, 베트남에서는 증상이 나타난 후에야 진단받는 경우가 많아 이미 시신경 손상이 진행된 상태가 흔함. 따라서 무증상 초기에도 정기 안압 검사가 필수임을 강조해야 함. 또한 한국의 다양한 녹내장 약물(Thuốc nhỏ mắt điều trị glôcôm) 옵션과 레이저 치료(Điều trị laser) 선택지를 설명하면 환자 신뢰도가 높아짐.",
        "commonMistakes": [
            {
                "mistake": "녹내장을 'bệnh mắt(눈병)'로 애매하게 표현",
                "correction": "'Tăng nhãn áp' 또는 'Glôcôm' 정확한 병명 사용",
                "explanation": "병명이 명확하지 않으면 환자가 질환의 심각성을 인지하지 못함"
            },
            {
                "mistake": "안압을 '눈 압력'으로 직역",
                "correction": "'Nhãn áp(안압)' 의학 용어 사용",
                "explanation": "일반어로 표현하면 전문성이 떨어지고 환자가 검색 시 정보를 찾기 어려움"
            },
            {
                "mistake": "평생 치료를 '오래 치료'로 애매하게 표현",
                "correction": "'Điều trị suốt đời(평생 치료)' 명확히 표현",
                "explanation": "치료 기간이 불명확하면 환자가 임의로 약물 중단할 위험이 있음"
            }
        ],
        "examples": [
            {
                "ko": "녹내장은 초기에는 증상이 없어서 정기검진이 중요합니다.",
                "vi": "Tăng nhãn áp giai đoạn đầu không có triệu chứng nên kiểm tra định kỳ rất quan trọng.",
                "situation": "formal"
            },
            {
                "ko": "안압약은 매일 같은 시간에 넣어야 효과가 좋아요.",
                "vi": "Thuốc nhỏ mắt hạ nhãn áp phải nhỏ đúng giờ mỗi ngày thì mới hiệu quả ạ.",
                "situation": "onsite"
            },
            {
                "ko": "녹내장 있으면 시야가 점점 좁아지니까 꼭 치료받으세요.",
                "vi": "Có glôcôm thì thị trường sẽ dần thu hẹp, nhất định phải điều trị nhé.",
                "situation": "informal"
            }
        ],
        "relatedTerms": ["안압", "시신경", "시야검사", "안압하강제", "실명"]
    },
    {
        "slug": "phau-thuat-amidan",
        "korean": "편도선수술",
        "vietnamese": "Phẫu thuật amidan",
        "hanja": "扁桃腺手術",
        "hanjaReading": "扁(납작할 편) + 桃(복숭아 도) + 腺(샘 선) + 手(손 수) + 術(재주 술)",
        "pronunciation": "퍼우투엇아미단",
        "meaningKo": "반복적으로 염증이 생기거나 비대해진 편도선을 제거하는 수술. 통역 시 베트남 환자들이 'cắt amidan(깟아미단, 편도 자르기)'라는 일상 표현을 많이 쓰므로 병기하면 이해도가 높아짐. 한국에서는 소아 편도수술이 흔하지만 베트남에서는 항생제 치료를 먼저 시도하는 경향이 강해 수술 적응증(연 5회 이상 편도염, 수면무호흡 등)을 명확히 설명해야 함. 수술 후 통증 관리와 회복 기간(1~2주) 안내가 환자 만족도에 중요.",
        "meaningVi": "Phẫu thuật cắt bỏ amidan khi bị viêm tái đi tái lại hoặc phì đại gây khó thở. Thường thực hiện ở trẻ em bị viêm amidan mãn tính trên 5 lần/năm hoặc bị ngưng thở khi ngủ. Sau mổ cần nghỉ ngơi 1-2 tuần và kiêng đồ cay nóng.",
        "context": "이비인후과 수술, 소아 만성 편도염, 수면무호흡 치료",
        "culturalNote": "한국에서는 편도선 수술이 소아에게 흔한 시술로 당일 또는 1박 입원으로 진행되지만, 베트남에서는 수술보다 항생제 치료를 선호하는 경향이 강함. 따라서 수술 적응증(연 5회 이상 편도염, 수면무호흡, 학업 지장)을 구체적으로 설명해야 부모가 수술 결정을 내리는 데 도움이 됨. 수술 후 아이스크림 섭취가 도움이 된다는 점 등 회복 팁도 함께 안내하면 불안감을 줄일 수 있음.",
        "commonMistakes": [
            {
                "mistake": "편도선을 'tuyến hạnh nhân(아몬드샘)'으로 직역",
                "correction": "'Amidan' 베트남 의료계 통용 용어 사용",
                "explanation": "직역 표현은 베트남 의료계에서 쓰지 않아 환자가 생소하게 느낌"
            },
            {
                "mistake": "수술 적응증 없이 '수술하면 좋다'고 일반화",
                "correction": "연 5회 이상 편도염 또는 수면무호흡 등 구체적 기준 제시",
                "explanation": "적응증 설명 없이 수술 권유하면 과잉 진료로 오해받을 수 있음"
            },
            {
                "mistake": "회복 기간을 '며칠'로 애매하게 표현",
                "correction": "'1-2 tuần(1~2주)' 구체적 기간 명시",
                "explanation": "정확한 기간 안내가 없으면 보호자가 학교/직장 계획을 세우기 어려움"
            }
        ],
        "examples": [
            {
                "ko": "1년에 편도염이 다섯 번 이상 생기면 수술을 고려합니다.",
                "vi": "Nếu bị viêm amidan từ 5 lần trở lên trong 1 năm thì nên cân nhắc phẫu thuật.",
                "situation": "formal"
            },
            {
                "ko": "편도 수술 후 일주일은 딱딱한 음식 피하고 차가운 음식 드세요.",
                "vi": "Sau mổ amidan 1 tuần thì tránh đồ cứng, nên ăn đồ mát như kem ạ.",
                "situation": "onsite"
            },
            {
                "ko": "편도 크면 잠 잘 때 숨 막힐 수 있어요.",
                "vi": "Amidan to có thể bị tắc thở khi ngủ đấy.",
                "situation": "informal"
            }
        ],
        "relatedTerms": ["편도염", "아데노이드", "수면무호흡", "소아이비인후과", "전신마취"]
    },
    {
        "slug": "viem-tai-giua",
        "korean": "중이염",
        "vietnamese": "Viêm tai giữa",
        "hanja": "中耳炎",
        "hanjaReading": "中(가운데 중) + 耳(귀 이) + 炎(불꽃 염)",
        "pronunciation": "비엠따이쯔어",
        "meaningKo": "고막 안쪽 중이 공간에 염증이 생기는 질환으로 특히 소아에게 흔함. 통역 시 베트남어 'Viêm tai(비엠따이, 귀염증)'와 구분하여 정확히 '중이'임을 강조해야 함. 외이염(Viêm tai ngoài)과 혼동하지 않도록 위치를 명확히 설명하는 것이 중요하며, 항생제 치료 순응도와 고막 천공 위험성도 안내해야 함. 한국에서는 소아 중이염 예방접종(폐렴구균)이 일반화됐으나 베트남에서는 접종률이 낮아 관련 정보 제공이 도움됨.",
        "meaningVi": "Viêm nhiễm ở khoang tai giữa (phía trong màng nhĩ), hay gặp ở trẻ em do ống nhĩ ngắn và nằm ngang. Triệu chứng bao gồm đau tai, sốt, tiết dịch. Nếu không điều trị có thể dẫn đến thủng màng nhĩ hoặc giảm thính lực. Cần dùng kháng sinh theo chỉ định bác sĩ.",
        "context": "이비인후과 소아 진료, 급성 귀 통증, 항생제 처방",
        "culturalNote": "한국에서는 소아 중이염이 매우 흔하게 진단되고 항생제 처방이 적극적이지만, 베트남에서는 경증 중이염을 자연 치유로 관리하는 경우도 있어 항생제 사용 기준을 명확히 설명해야 함. 또한 한국의 폐렴구균 백신(Vắc-xin phế cầu khuẩn) 접종이 중이염 예방에 효과적이라는 정보를 제공하면 부모들의 예방 의식 향상에 도움이 됨. 고막 절개(Rạch màng nhĩ) 필요성 설명 시 공포심 완화를 위해 빠른 회복과 통증 경감 효과를 강조해야 함.",
        "commonMistakes": [
            {
                "mistake": "중이염을 'viêm tai(귀염)'로만 표현",
                "correction": "'Viêm tai giữa(중이염)' 정확한 위치 명시",
                "explanation": "'Viêm tai'는 외이염과 구분되지 않아 치료 방향이 달라질 수 있음"
            },
            {
                "mistake": "외이염(Viêm tai ngoài)과 혼동하여 설명",
                "correction": "중이(tai giữa)는 고막 안쪽, 외이(tai ngoài)는 귓바퀴~고막 사이 구분",
                "explanation": "위치가 다르면 치료법도 다르므로 정확한 구분 필수"
            },
            {
                "mistake": "항생제 복용 기간을 '좀 드세요'로 애매하게 표현",
                "correction": "'Uống kháng sinh đủ 7-10 ngày(7~10일 복용)' 구체화",
                "explanation": "기간이 불명확하면 환자가 증상 호전 시 임의로 중단하여 재발 위험"
            }
        ],
        "examples": [
            {
                "ko": "중이염은 고막 안쪽에 생긴 염증이라 귀 청소로는 낫지 않습니다.",
                "vi": "Viêm tai giữa là viêm bên trong màng nhĩ nên lấy ráy tai không giúp khỏi bệnh.",
                "situation": "formal"
            },
            {
                "ko": "항생제 7일 다 먹어야 재발 안 해요.",
                "vi": "Phải uống kháng sinh đủ 7 ngày thì mới không tái phát ạ.",
                "situation": "onsite"
            },
            {
                "ko": "중이염 자주 생기면 고막에 튜브 넣을 수도 있어요.",
                "vi": "Nếu hay bị viêm tai giữa thì có thể phải đặt ống thông khí màng nhĩ.",
                "situation": "informal"
            }
        ],
        "relatedTerms": ["외이염", "고막천공", "항생제", "이관", "소아이비인후과"]
    },
    {
        "slug": "phau-thuat-vach-ngan-mui",
        "korean": "비중격수술",
        "vietnamese": "Phẫu thuật vách ngăn mũi",
        "hanja": "鼻中膈手術",
        "hanjaReading": "鼻(코 비) + 中(가운데 중) + 膈(막을 격) + 手(손 수) + 術(재주 술)",
        "pronunciation": "퍼우투엇박응안무이",
        "meaningKo": "코 안 중앙을 나누는 비중격이 휘어져 코막힘, 비염 등을 유발할 때 이를 교정하는 수술. 통역 시 베트남어로 'mổ vẹo vách ngăn(모베오박응안, 비중격 휨 수술)'이라는 일상 표현도 함께 설명하면 이해도가 높아짐. 한국에서는 비중격만곡증이 흔하게 진단되고 수술도 활발하나 베트남에서는 약물 치료를 먼저 시도하는 경향이 있어 수술 적응증(만성 코막힘, 수면장애 등)을 명확히 설명해야 함. 보험 적용 여부와 회복 기간도 투명하게 안내 필요.",
        "meaningVi": "Phẫu thuật chỉnh sửa vách ngăn mũi bị lệch gây tắc nghẽn mũi, viêm mũi mãn tính hoặc rối loạn giấc ngủ. Đây là phẫu thuật phổ biến ở Hàn Quốc khi điều trị nội khoa không hiệu quả. Sau mổ cần đặt gạc cầm máu trong mũi 1-2 ngày và kiêng gắng sức.",
        "context": "이비인후과 수술, 만성 코막힘, 수면장애 치료",
        "culturalNote": "한국에서는 비중격만곡증 수술이 보험 적용되고 흔한 시술이지만, 베트남에서는 수술보다 약물이나 비강 스프레이로 관리하는 경향이 강함. 따라서 수술 적응증(양측 코막힘 지속, 수면무호흡, 만성 부비동염 동반)을 구체적으로 설명해야 환자가 수술 필요성을 이해할 수 있음. 또한 수술 후 코막힘 패킹(Đặt gạc mũi) 기간과 불편함을 사전 고지해야 만족도가 높아짐.",
        "commonMistakes": [
            {
                "mistake": "비중격을 'xương mũi(코뼈)'로 표현",
                "correction": "'Vách ngăn mũi(비중격)' 정확한 부위 명시",
                "explanation": "코뼈는 외비(뼈)이고 비중격은 내부 칸막이로 구조가 다름"
            },
            {
                "mistake": "수술 후 패킹을 '거즈'로만 표현",
                "correction": "'Gạc cầm máu trong mũi(코 안 지혈 거즈)' 위치와 목적 명시",
                "explanation": "위치와 목적이 불명확하면 환자가 불편함의 이유를 이해하지 못함"
            },
            {
                "mistake": "회복 기간을 '금방'으로 애매하게 표현",
                "correction": "'1-2 tuần hồi phục(1~2주 회복)' 구체적 기간 제시",
                "explanation": "정확한 기간 안내가 없으면 환자가 일상 복귀 계획을 세우기 어려움"
            }
        ],
        "examples": [
            {
                "ko": "비중격이 심하게 휘어서 수술로 교정하는 게 좋겠습니다.",
                "vi": "Vách ngăn mũi bị lệch nghiêm trọng nên phẫu thuật chỉnh sửa là tốt nhất.",
                "situation": "formal"
            },
            {
                "ko": "수술 후 이틀간 코에 거즈 있어서 입으로 숨 쉬셔야 해요.",
                "vi": "Sau mổ 2 ngày có gạc trong mũi nên phải thở bằng miệng ạ.",
                "situation": "onsite"
            },
            {
                "ko": "비중격 수술하면 코막힘 확 좋아져요.",
                "vi": "Mổ vách ngăn mũi thì hết tắc nghẽn luôn.",
                "situation": "informal"
            }
        ],
        "relatedTerms": ["비중격만곡증", "코막힘", "비염", "부비동염", "코성형"]
    },
    {
        "slug": "may-tro-thinh",
        "korean": "보청기",
        "vietnamese": "Máy trợ thính",
        "hanja": "補聽器",
        "hanjaReading": "補(도울 보) + 聽(들을 청) + 器(그릇 기)",
        "pronunciation": "마이쩌팅",
        "meaningKo": "청력이 저하된 사람이 소리를 잘 듣기 위해 착용하는 전자 기기. 통역 시 베트남 환자들이 오해하기 쉬운 부분은 보청기가 청력을 '치료'하는 게 아니라 '보조'하는 기기라는 점을 명확히 해야 함. 한국은 보청기 보급률이 높고 다양한 형태(귓속형, 귀걸이형, 충전식 등)가 있지만 베트남에서는 여전히 고가 장비로 인식되어 구매를 망설이는 경우가 많음. 보청기 착용의 장기적 이점(치매 예방, 의사소통 개선)을 설명하고 보험 지원 정보도 안내하는 것이 중요.",
        "meaningVi": "Thiết bị điện tử đeo vào tai giúp người suy giảm thính lực nghe rõ hơn. Máy trợ thính không chữa khỏi bệnh mà chỉ khuếch đại âm thanh. Ở Hàn Quốc có hỗ trợ bảo hiểm cho người cao tuổi và người khuyết tật. Có nhiều loại: đeo trong tai (in-the-ear), đeo sau tai (behind-the-ear), sạc điện hoặc dùng pin.",
        "context": "이비인후과 보청기 상담, 노인성 난청, 청력 보조",
        "culturalNote": "한국에서는 노인성 난청에 대한 인식이 높아 보청기 착용률이 증가하고 있으며, 건강보험 지원(최대 131만 원)도 받을 수 있음. 반면 베트남에서는 보청기가 여전히 사치품으로 인식되어 경제적 여유가 있는 층만 구매하는 경향이 있음. 따라서 보청기의 필요성(의사소통 개선, 치매 예방)과 한국의 보험 지원 제도를 설명하면 환자의 구매 결정에 도움이 됨. 또한 보청기 적응 기간(1~2개월)과 정기 조정의 필요성도 안내해야 환자 만족도가 높아짐.",
        "commonMistakes": [
            {
                "mistake": "보청기를 'máy chữa điếc(귀먹음 치료기)'로 표현",
                "correction": "'Máy trợ thính(청력 보조기)' 사용",
                "explanation": "보청기는 치료 기기가 아니라 보조 기기이므로 정확한 용어 사용 필요"
            },
            {
                "mistake": "보청기 종류를 구분 없이 'máy trợ thính'로만 표현",
                "correction": "귓속형(trong tai), 귀걸이형(sau tai) 등 구체적 형태 설명",
                "explanation": "형태에 따라 착용감과 비용이 달라 환자 선택권 보장을 위해 구분 필요"
            },
            {
                "mistake": "적응 기간 설명 없이 '바로 잘 들린다'고 표현",
                "correction": "'Cần 1-2 tháng để quen(1~2개월 적응 기간 필요)' 명시",
                "explanation": "적응 기간 안내 없이 기대치를 높이면 환자가 실망하여 착용 중단할 위험"
            }
        ],
        "examples": [
            {
                "ko": "보청기는 청력을 치료하는 게 아니라 소리를 크게 해주는 기기입니다.",
                "vi": "Máy trợ thính không chữa khỏi điếc mà chỉ khuếch đại âm thanh để nghe rõ hơn.",
                "situation": "formal"
            },
            {
                "ko": "보청기 착용 후 한두 달은 적응 기간이 필요해요.",
                "vi": "Sau khi đeo máy trợ thính cần 1-2 tháng để quen dần ạ.",
                "situation": "onsite"
            },
            {
                "ko": "보청기 쓰면 대화하기 훨씬 편해져요.",
                "vi": "Đeo máy trợ thính thì nói chuyện dễ hơn nhiều.",
                "situation": "informal"
            }
        ],
        "relatedTerms": ["난청", "청력검사", "인공와우", "노인성난청", "청각장애"]
    }
]

def main():
    # 기존 데이터 읽기
    with open(file_path, 'r', encoding='utf-8') as f:
        data = json.load(f)

    # data는 리스트이므로 직접 사용
    existing_slugs = {term['slug'] for term in data}

    # 중복 제거
    unique_new_terms = [term for term in new_terms if term['slug'] not in existing_slugs]

    # 새 용어 추가
    data.extend(unique_new_terms)

    # 파일 저장
    with open(file_path, 'w', encoding='utf-8') as f:
        json.dump(data, f, ensure_ascii=False, indent=2)

    print(f"✅ {len(unique_new_terms)}개 용어 추가 완료")
    print(f"📊 총 용어 수: {len(data)}개")

    if len(unique_new_terms) < len(new_terms):
        skipped = len(new_terms) - len(unique_new_terms)
        print(f"⚠️  {skipped}개 중복 용어 건너뜀")

if __name__ == "__main__":
    main()
