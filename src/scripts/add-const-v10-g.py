#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
토공/포장 (Earthwork/Paving) 전문용어 10개 추가 스크립트
Tier S 품질 기준 준수
"""

import json
import os

def main():
    # 1. 파일 경로 설정 (상대 경로)
    file_path = os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', 'data', 'terms', 'construction.json')

    # 2. 기존 데이터 로드 (LIST 형식)
    with open(file_path, 'r', encoding='utf-8') as f:
        data = json.load(f)

    # 3. 기존 slug 목록 추출
    existing_slugs = {t['slug'] for t in data}

    # 4. 신규 용어 정의 (10개)
    new_terms = [
        {
            "slug": "dao-dat",
            "korean": "절토",
            "vietnamese": "đào đất",
            "hanja": "切土",
            "hanjaReading": "切(끊을 절) + 土(흙 토)",
            "pronunciation": "절토 / đào đất [다오 닷]",
            "meaningKo": "도로나 건설 부지를 만들기 위해 지반을 파내어 흙을 제거하는 작업입니다. 통역 시 '깎기'라는 구어체 표현과 혼동하지 않도록 주의하세요. 베트남 현장에서는 'đào đất'와 'đào móng'(기초 굴착)을 명확히 구분해야 하며, 굴착 깊이와 경사도를 정확히 전달하는 것이 안전사고 예방에 중요합니다. 특히 우기에는 절토면 붕괴 위험이 높아 배수 계획을 함께 논의해야 합니다.",
            "meaningVi": "Công tác đào bỏ đất để tạo ra mặt bằng xây dựng hoặc tuyến đường. Trong thi công, cần phân biệt rõ 'đào đất' (cắt đất) với 'đào móng' (đào hố móng). Độ dốc mái đào và hệ thống thoát nước là yếu tố quan trọng để đảm bảo an toàn, đặc biệt trong mùa mưa khi nguy cơ sạt lở cao.",
            "context": "도로공사, 부지조성, 토목공사 현장에서 사용",
            "culturalNote": "한국은 산지가 많아 절토 작업이 빈번하고 기술이 발달했으나, 베트남은 평야 지역이 많아 상대적으로 절토 규모가 작습니다. 베트남 현장에서는 우기 시 절토면 붕괴 사고가 자주 발생하므로 한국보다 더 보수적인 경사도 기준을 적용하는 경우가 많습니다. 또한 베트남에서는 절토된 흙을 인근 성토 구간에 재활용하는 것을 선호하여 경제성을 중시합니다.",
            "commonMistakes": [
                {
                    "mistake": "'굴착'을 모두 'đào đất'로 번역",
                    "correction": "절토는 'đào đất', 기초 굴착은 'đào móng', 터파기는 'đào hố'",
                    "explanation": "굴착의 목적과 규모에 따라 베트남어 표현이 달라집니다"
                },
                {
                    "mistake": "'깎기'를 그대로 직역",
                    "correction": "구어체 '깎기'는 'đào đất' 또는 'cắt đất'로 번역",
                    "explanation": "현장 구어를 정확한 기술 용어로 변환해야 합니다"
                },
                {
                    "mistake": "경사도를 '몇 대 몇'으로만 말함",
                    "correction": "'tỷ lệ mái dốc 1:1.5'처럼 구체적 수치와 함께 전달",
                    "explanation": "베트남 현장에서는 비율 표기법이 명확해야 시공 오류를 방지합니다"
                }
            ],
            "examples": [
                {
                    "ko": "이 구간은 절토 깊이가 5미터이므로 계단식으로 시공하겠습니다.",
                    "vi": "Đoạn này độ sâu đào đất là 5 mét nên chúng ta sẽ thi công theo dạng bậc thang.",
                    "situation": "onsite"
                },
                {
                    "ko": "절토 사면의 경사는 1:1.5로 설계되었습니다.",
                    "vi": "Mái dốc đào đất được thiết kế với tỷ lệ 1:1.5.",
                    "situation": "formal"
                },
                {
                    "ko": "절토 작업 중 지하수가 나와서 배수 처리가 필요합니다.",
                    "vi": "Trong quá trình đào đất có nước ngầm nên cần xử lý thoát nước.",
                    "situation": "onsite"
                }
            ],
            "relatedTerms": ["dap-dat", "dam-nen", "lop-mong-duong"]
        },
        {
            "slug": "dap-dat",
            "korean": "성토",
            "vietnamese": "đắp đất",
            "hanja": "盛土",
            "hanjaReading": "盛(성할 성) + 土(흙 토)",
            "pronunciation": "성토 / đắp đất [답 닷]",
            "meaningKo": "도로나 구조물을 만들기 위해 흙을 쌓아 올리는 작업입니다. 통역 시 '쌓기', '흙쌓기'라는 구어체와 기술용어를 구분하고, 베트남 현장에서는 다짐(đầm nén) 작업과 항상 함께 언급되므로 두 용어를 세트로 숙지해야 합니다. 성토 높이가 3m를 초과하면 단계별 다짐과 중간 점검이 필수이며, 이를 정확히 전달하지 않으면 침하 사고로 이어질 수 있습니다. 베트남 점토질 흙은 함수비 관리가 특히 중요합니다.",
            "meaningVi": "Công tác đắp đất để nâng cao mặt bằng hoặc tạo nền đường. Luôn phải đi kèm với công tác đầm nén để đảm bảo độ chặt yêu cầu. Khi cao độ đắp đất vượt quá 3m, cần đắp và đầm theo từng lớp với kiểm tra chất lượng giữa các lớp. Đối với đất sét ở Việt Nam, việc kiểm soát độ ẩm là rất quan trọng để đạt độ chặt tốt.",
            "context": "도로공사, 제방축조, 부지조성에서 사용",
            "culturalNote": "한국은 성토 재료로 양질의 토사를 선호하지만, 베트남은 경제성을 중시하여 현장 발생토를 최대한 활용합니다. 베트남의 점토질 흙은 우기에 함수비가 높아져 다짐이 어려우므로 한국보다 더 긴 양생 기간이 필요합니다. 또한 베트남 현장에서는 성토 높이 1m당 하루 정도의 양생 기간을 두는 관습이 있어 공정 계획 시 이를 반영해야 합니다.",
            "commonMistakes": [
                {
                    "mistake": "'쌓기'를 'xây'로 번역",
                    "correction": "흙 쌓기는 'đắp đất', 블록 쌓기는 'xây gạch'",
                    "explanation": "재료에 따라 동사가 달라지므로 명확히 구분해야 합니다"
                },
                {
                    "mistake": "다짐 작업을 언급하지 않음",
                    "correction": "'đắp đất và đầm nén'처럼 항상 함께 언급",
                    "explanation": "성토는 다짐이 필수이므로 베트남 현장에서 두 작업을 세트로 인식합니다"
                },
                {
                    "mistake": "함수비를 '물 양'으로 직역",
                    "correction": "'độ ẩm'(함수비) 또는 'hàm lượng nước'",
                    "explanation": "기술 용어는 정확한 베트남어 표준 용어를 사용해야 합니다"
                }
            ],
            "examples": [
                {
                    "ko": "성토는 30cm씩 나눠서 다짐하면서 쌓아올리세요.",
                    "vi": "Đắp đất theo từng lớp 30cm và đầm nén sau mỗi lớp.",
                    "situation": "onsite"
                },
                {
                    "ko": "성토 재료의 함수비가 너무 높아서 다짐이 안 됩니다.",
                    "vi": "Độ ẩm của vật liệu đắp đất quá cao nên không đầm nén được.",
                    "situation": "onsite"
                },
                {
                    "ko": "성토 높이 5m 구간은 단계별 품질 검사를 실시합니다.",
                    "vi": "Đoạn đắp đất cao 5m sẽ thực hiện kiểm tra chất lượng theo từng giai đoạn.",
                    "situation": "formal"
                }
            ],
            "relatedTerms": ["dao-dat", "dam-nen", "lop-mong-duong"]
        },
        {
            "slug": "dam-nen",
            "korean": "다짐",
            "vietnamese": "đầm nén",
            "hanja": None,
            "hanjaReading": None,
            "pronunciation": "다짐 / đầm nén [덤 넨]",
            "meaningKo": "흙이나 포장 재료를 기계적 힘으로 압축하여 밀도를 높이고 공극을 줄이는 작업입니다. 통역 시 '다지기', '전압'이라는 구어체와 구분하고, 베트남 현장에서는 다짐 횟수(số lần đầm)와 다짐도(độ chặt)를 항상 함께 명시해야 합니다. 특히 노반 작업에서는 95% 이상의 다짐도 확보가 필수이며, 이를 정확히 전달하지 않으면 포장 파손의 원인이 됩니다. 베트남은 진동롤러(lu rung)를 주로 사용하므로 장비 종류도 숙지하세요.",
            "meaningVi": "Công tác nén chặt đất hoặc vật liệu lớp móng bằng lực cơ học để tăng mật độ và giảm lỗ rỗng. Trong thi công, luôn phải quy định rõ số lần đầm (thường 6-8 lần) và độ chặt đạt được (thường ≥95% độ chặt tiêu chuẩn). Đối với lớp móng đường, độ chặt không đủ sẽ gây hư hỏng mặt đường sau này. Thiết bị chủ yếu là lu rung với trọng lượng và tần số rung phù hợp.",
            "context": "토공, 포장공사, 기초공사 현장에서 필수 공정",
            "culturalNote": "한국은 다짐도 측정을 엄격하게 하고 품질 관리 시스템이 잘 갖춰져 있지만, 베트남 현장은 장비와 측정 기술이 상대적으로 부족하여 육안 판단에 의존하는 경우가 많습니다. 이로 인해 한국 감리자가 베트남 현장에서 다짐도 재측정을 요구하는 경우가 빈번하므로, 통역 시 품질 기준의 차이를 설명할 수 있어야 합니다. 베트남은 인건비가 저렴하여 다짐 횟수를 늘리는 방식을 선호합니다.",
            "commonMistakes": [
                {
                    "mistake": "'전압'을 'điện áp'(전기 전압)로 번역",
                    "correction": "다짐/전압은 'đầm nén' 또는 'lu lèn'",
                    "explanation": "건설용어 '전압'은 전기와 무관하며 흙을 다지는 작업을 의미합니다"
                },
                {
                    "mistake": "다짐도 퍼센트를 그냥 '%'로만 말함",
                    "correction": "'độ chặt 95%' 또는 '95% độ chặt tiêu chuẩn'으로 명확히",
                    "explanation": "기준(tiêu chuẩn)을 함께 언급해야 오해가 없습니다"
                },
                {
                    "mistake": "롤러를 'máy cán'(압연기)로 번역",
                    "correction": "다짐 롤러는 'lu' 또는 'lu rung'(진동롤러)",
                    "explanation": "'máy cán'은 철강 압연에 사용하는 용어로 건설과 다릅니다"
                }
            ],
            "examples": [
                {
                    "ko": "이 층은 8톤 진동롤러로 6회 다짐하세요.",
                    "vi": "Lớp này dùng lu rung 8 tấn đầm nén 6 lần.",
                    "situation": "onsite"
                },
                {
                    "ko": "다짐도 시험 결과 93%라서 재시공이 필요합니다.",
                    "vi": "Kết quả thí nghiệm độ chặt là 93% nên cần thi công lại.",
                    "situation": "formal"
                },
                {
                    "ko": "함수비가 적정해야 다짐이 잘 됩니다.",
                    "vi": "Độ ẩm phải phù hợp thì đầm nén mới hiệu quả.",
                    "situation": "onsite"
                }
            ],
            "relatedTerms": ["dap-dat", "lu-rung", "lop-mong-duong"]
        },
        {
            "slug": "lop-mong-duong",
            "korean": "노상/노반",
            "vietnamese": "lớp móng đường",
            "hanja": "路床/路盤",
            "hanjaReading": "路(길 로) + 床(평상 상) / 路(길 로) + 盤(소반 반)",
            "pronunciation": "노상/노반 / lớp móng đường [럽 몽 드엉]",
            "meaningKo": "도로 포장 아래 하중을 지지하는 기층 구조를 총칭합니다. 노상(路床)은 자연 지반을 다진 최하층, 노반(路盤)은 그 위에 쇄석 등을 깔아 만든 층입니다. 통역 시 베트남에서는 두 용어를 통합하여 'lớp móng đường'로 표현하므로 문맥에 따라 구분 설명이 필요합니다. 특히 품질 검사에서는 지지력(sức chịu tải) 수치를 명확히 전달해야 하며, CBR 값이 기준 미달 시 보강 공법을 논의해야 합니다.",
            "meaningVi": "Các lớp kết cấu nền móng phía dưới mặt đường, có nhiệm vụ chịu tải trọng và phân bố đều xuống nền đất tự nhiên. Bao gồm lớp nền đất đầm nén (tương đương 노상) và lớp cấp phối đá dăm phía trên (tương đương 노반). Chất lượng lớp móng đường quyết định tuổi thọ của toàn bộ kết cấu áo đường. Cần kiểm tra độ chặt và sức chịu tải (CBR) để đảm bảo tiêu chuẩn.",
            "context": "도로공사, 포장공사의 기초 단계에서 사용",
            "culturalNote": "한국은 노상과 노반을 엄격히 구분하여 각각 다른 품질 기준을 적용하지만, 베트남은 'lớp móng đường'라는 포괄적 용어를 사용하며 세부 구분이 덜 엄격합니다. 이로 인해 한국 기술자가 베트남 시공사에게 노상/노반 품질 기준을 설명할 때 혼란이 생기는 경우가 많습니다. 통역사는 각 층의 역할과 품질 기준을 명확히 전달해야 시공 오류를 방지할 수 있습니다.",
            "commonMistakes": [
                {
                    "mistake": "'노상'을 'bề mặt đường'(도로 표면)로 번역",
                    "correction": "노상은 'lớp nền đất' 또는 'lớp móng dưới'",
                    "explanation": "노상은 표면이 아닌 포장 아래 기초층입니다"
                },
                {
                    "mistake": "CBR을 설명 없이 그대로 사용",
                    "correction": "'chỉ số CBR' 또는 'sức chịu tải California'로 설명",
                    "explanation": "베트남 현장 인력이 CBR 약어를 모르는 경우가 많습니다"
                },
                {
                    "mistake": "'지지력'을 'sức mạnh'(힘)로 직역",
                    "correction": "'sức chịu tải' 또는 'khả năng chịu lực'",
                    "explanation": "기술 용어는 정확한 표준어를 사용해야 합니다"
                }
            ],
            "examples": [
                {
                    "ko": "노반의 CBR 값이 기준에 못 미쳐서 석회 안정 처리를 하겠습니다.",
                    "vi": "Chỉ số CBR của lớp móng đường không đạt tiêu chuẩn nên sẽ xử lý ổn định bằng vôi.",
                    "situation": "formal"
                },
                {
                    "ko": "노상 다짐이 제대로 안 돼서 포장이 침하했어요.",
                    "vi": "Lớp nền đất đầm nén không đạt nên mặt đường bị lún.",
                    "situation": "onsite"
                },
                {
                    "ko": "노반 위에 쇄석 기층을 20cm 두께로 깔겠습니다.",
                    "vi": "Trên lớp móng sẽ rải lớp cấp phối đá dày 20cm.",
                    "situation": "onsite"
                }
            ],
            "relatedTerms": ["dam-nen", "cap-phoi-da", "lop-lot"]
        },
        {
            "slug": "mat-duong-be-tong",
            "korean": "콘크리트포장",
            "vietnamese": "mặt đường bê tông",
            "hanja": None,
            "hanjaReading": None,
            "pronunciation": "콘크리트포장 / mặt đường bê tông [맛 드엉 베 통]",
            "meaningKo": "시멘트 콘크리트를 사용하여 도로 표면을 포장하는 공법으로, 강성포장(剛性鋪裝)이라고도 합니다. 통역 시 아스팔트포장(mặt đường nhựa)과 명확히 구분하고, 줄눈(khe co giãn) 시공과 양생 기간을 정확히 전달해야 합니다. 베트남 현장에서는 양생 중 교통 개방 시기를 두고 한국 기술자와 현장 간 의견 충돌이 잦으므로, 최소 양생 기간(통상 7일)을 강조해야 합니다. 특히 고온 다습한 베트남 기후에서는 균열 방지를 위한 양생 관리가 더욱 중요합니다.",
            "meaningVi": "Công nghệ rải mặt đường bằng bê tông xi măng, còn gọi là áo đường cứng. Ưu điểm là độ bền cao, tuổi thọ lâu dài nhưng chi phí đầu tư cao hơn mặt đường nhựa. Cần thi công khe co giãn đúng kỹ thuật và dưỡng hộ tối thiểu 7 ngày trước khi cho phương tiện lưu thông. Trong điều kiện khí hậu nóng ẩm ở Việt Nam, việc dưỡng hộ và phòng chống nứt là rất quan trọng.",
            "context": "고속도로, 산업단지 도로, 항만 야드 등 중하중 도로에 적용",
            "culturalNote": "한국은 콘크리트포장 기술이 발달하여 고속도로에 많이 적용되지만, 베트남은 아스팔트포장을 선호하여 콘크리트포장 비율이 낮습니다. 이는 초기 건설비용 부담과 보수 기술 부족 때문입니다. 한국 기술자가 베트남 프로젝트에서 콘크리트포장을 제안할 때는 장기적 경제성과 유지관리 편의성을 충분히 설명해야 하며, 현지 시공 경험이 부족할 수 있음을 감안해야 합니다.",
            "commonMistakes": [
                {
                    "mistake": "'양생'을 'nuôi dưỡng'(영양 공급)로 번역",
                    "correction": "콘크리트 양생은 'dưỡng hộ bê tông'",
                    "explanation": "'nuôi dưỡng'은 생물학적 의미이고, 건설에서는 'dưỡng hộ'를 씁니다"
                },
                {
                    "mistake": "'줄눈'을 'đường may'(봉제선)로 번역",
                    "correction": "콘크리트 줄눈은 'khe co giãn' 또는 'mạch ngăn'",
                    "explanation": "기술 용어는 정확한 베트남어 표준 용어를 사용해야 합니다"
                },
                {
                    "mistake": "개방 시기를 날짜만 말함",
                    "correction": "'양생 7일 후 개방' = 'mở cửa giao thông sau 7 ngày dưỡng hộ'",
                    "explanation": "양생 기간과 개방 시기를 함께 명시해야 오해가 없습니다"
                }
            ],
            "examples": [
                {
                    "ko": "콘크리트포장은 두께 25cm로 타설하고 줄눈은 5m 간격으로 시공합니다.",
                    "vi": "Mặt đường bê tông đổ dày 25cm và thi công khe co giãn cách nhau 5m.",
                    "situation": "formal"
                },
                {
                    "ko": "양생 기간이 끝나지 않았으니 차량 진입을 막아주세요.",
                    "vi": "Chưa hết thời gian dưỡng hộ nên hãy chặn không cho xe vào.",
                    "situation": "onsite"
                },
                {
                    "ko": "콘크리트포장은 초기 비용이 높지만 유지비가 적게 듭니다.",
                    "vi": "Mặt đường bê tông có chi phí ban đầu cao nhưng chi phí bảo trì thấp.",
                    "situation": "formal"
                }
            ],
            "relatedTerms": ["mat-duong-nhua", "lop-mong-duong", "may-rai"]
        },
        {
            "slug": "mat-duong-nhua",
            "korean": "아스팔트포장",
            "vietnamese": "mặt đường nhựa",
            "hanja": None,
            "hanjaReading": None,
            "pronunciation": "아스팔트포장 / mặt đường nhựa [맛 드엉 늬어]",
            "meaningKo": "아스팔트 혼합물을 사용하여 도로 표면을 포장하는 공법으로, 유연포장(柔軟鋪裝)이라고도 합니다. 통역 시 '아스콘', '아스팔트 콘크리트'라는 약어도 함께 숙지하고, 베트남에서는 'nhựa'(고무/플라스틱)라는 단어가 혼동을 줄 수 있으므로 'nhựa đường'(도로용 아스팔트)로 명확히 해야 합니다. 포설 온도(nhiệt độ rải)가 140~160°C로 높아 안전 교육이 필수이며, 우천 시 시공 금지를 강조해야 합니다. 베트남은 고온 기후로 인해 여름철 소성변형(lún vệt bánh xe)이 자주 발생하므로 바인더 등급 선정이 중요합니다.",
            "meaningVi": "Công nghệ rải mặt đường bằng hỗn hợp nhựa đường (asphalt), còn gọi là áo đường mềm. Chi phí đầu tư thấp hơn bê tông, thi công nhanh, nhưng tuổi thọ ngắn hơn và cần bảo trì thường xuyên. Nhiệt độ rải từ 140~160°C nên phải đảm bảo an toàn lao động. Cấm thi công khi trời mưa vì ẩm ướt làm giảm chất lượng. Do khí hậu nóng ở Việt Nam, cần chọn loại nhựa chống biến dạng ở nhiệt độ cao.",
            "context": "도시 도로, 일반 국도, 주차장 등 대부분의 도로 포장에 사용",
            "culturalNote": "베트남은 아스팔트포장을 압도적으로 선호하는데, 이는 초기 비용이 낮고 보수가 상대적으로 쉽기 때문입니다. 그러나 한국처럼 품질 관리가 엄격하지 않아 조기 파손이 빈번하며, 특히 우기와 고온기에 품질 저하가 심합니다. 한국 기술자가 베트남 현장에서 시공 온도와 다짐 시기를 엄격히 관리하려 할 때 현장 인력의 이해 부족으로 마찰이 생길 수 있으므로, 통역사는 품질 기준의 중요성을 설득력 있게 전달해야 합니다.",
            "commonMistakes": [
                {
                    "mistake": "'아스콘'을 그대로 'ascon'으로 발음",
                    "correction": "'asphalt concrete' 또는 베트남식으로 'bê tông nhựa'",
                    "explanation": "한국식 약어를 베트남 현장에서 그대로 쓰면 이해하지 못합니다"
                },
                {
                    "mistake": "'nhựa'만 말해서 플라스틱으로 오해",
                    "correction": "'nhựa đường'(아스팔트) 또는 'atphan'으로 명확히",
                    "explanation": "'nhựa'는 베트남어로 고무/플라스틱을 뜻하므로 '도로용'임을 명시해야 합니다"
                },
                {
                    "mistake": "포설 온도를 '뜨겁다'로만 표현",
                    "correction": "'nhiệt độ rải 150°C'처럼 구체적 수치로",
                    "explanation": "안전 관리를 위해서는 정확한 온도를 전달해야 합니다"
                }
            ],
            "examples": [
                {
                    "ko": "아스팔트는 150도 이상에서 포설해야 다짐이 잘 됩니다.",
                    "vi": "Nhựa đường phải rải ở nhiệt độ trên 150°C thì đầm nén mới hiệu quả.",
                    "situation": "onsite"
                },
                {
                    "ko": "비가 오면 아스팔트포장 작업을 중단하세요.",
                    "vi": "Khi trời mưa thì dừng ngay công tác rải mặt đường nhựa.",
                    "situation": "onsite"
                },
                {
                    "ko": "이 도로는 교통량이 많아서 개질 아스팔트를 사용하겠습니다.",
                    "vi": "Tuyến đường này lưu lượng xe lớn nên sẽ dùng nhựa đường cải tiến.",
                    "situation": "formal"
                }
            ],
            "relatedTerms": ["mat-duong-be-tong", "may-rai", "lu-rung"]
        },
        {
            "slug": "lu-rung",
            "korean": "진동롤러",
            "vietnamese": "lu rung",
            "hanja": None,
            "hanjaReading": None,
            "pronunciation": "진동롤러 / lu rung [루 중]",
            "meaningKo": "진동 기능이 있는 다짐 장비로, 흙이나 아스팔트를 효과적으로 다지는 데 사용됩니다. 통역 시 '롤러', '로울러'라는 구어체 발음도 숙지하고, 베트남 현장에서는 톤수(tấn)와 진동 주파수(tần số rung)를 함께 명시해야 합니다. 일반 흙 다짐은 8~10톤, 아스팔트 다짐은 6~8톤급을 주로 사용하며, 다짐 속도가 너무 빠르면 효과가 없다는 점을 현장에 주지시켜야 합니다. 베트남 장비는 노후화된 경우가 많아 진동 기능 작동 여부를 시공 전 반드시 확인해야 합니다.",
            "meaningVi": "Thiết bị đầm nén có chức năng rung, dùng để đầm chặt đất hoặc nhựa đường hiệu quả. Trong thi công, cần quy định rõ trọng lượng (tấn) và tần số rung (Hz). Đối với đầm đất thường dùng lu 8~10 tấn, đầm nhựa dùng lu 6~8 tấn. Tốc độ lu quá nhanh sẽ không đạt hiệu quả đầm nén. Do thiết bị ở Việt Nam thường cũ nên cần kiểm tra chức năng rung trước khi thi công.",
            "context": "토공, 포장공사 현장의 필수 장비",
            "culturalNote": "한국은 최신 진동롤러를 보유하고 진동 주파수를 정밀 제어하지만, 베트남 현장은 노후 장비가 많고 진동 기능이 고장난 채 사용하는 경우도 있습니다. 한국 감리자가 장비 교체를 요구할 때 베트남 시공사가 경제적 부담으로 거부하는 경우가 있으므로, 통역사는 품질 기준과 비용 문제를 조율해야 합니다. 또한 베트남은 장비 임대 시장이 발달하여 단기 임대가 가능하므로 이를 대안으로 제시할 수 있습니다.",
            "commonMistakes": [
                {
                    "mistake": "'롤러'를 'roller'로 발음만 베트남식으로",
                    "correction": "베트남어는 'lu' (로울러는 통하지 않음)",
                    "explanation": "외래어가 아닌 베트남어 고유 용어를 사용해야 합니다"
                },
                {
                    "mistake": "톤수만 말하고 진동 여부를 언급 안 함",
                    "correction": "'lu rung 8 tấn'처럼 진동(rung)을 명시",
                    "explanation": "일반 롤러와 진동롤러는 다르므로 구분이 필요합니다"
                },
                {
                    "mistake": "다짐 속도를 '빨리'로만 표현",
                    "correction": "'tốc độ lu 3~5 km/h'처럼 구체적 속도로",
                    "explanation": "속도가 품질에 영향을 미치므로 수치로 전달해야 합니다"
                }
            ],
            "examples": [
                {
                    "ko": "10톤 진동롤러로 시속 4km 속도로 6회 다짐하세요.",
                    "vi": "Dùng lu rung 10 tấn, tốc độ 4 km/h, đầm nén 6 lần.",
                    "situation": "onsite"
                },
                {
                    "ko": "롤러 진동이 안 되면 다짐이 제대로 안 되니 확인해보세요.",
                    "vi": "Nếu lu không rung thì đầm nén không hiệu quả, hãy kiểm tra.",
                    "situation": "onsite"
                },
                {
                    "ko": "아스팔트 다짐은 6톤 롤러 2대로 동시 작업합니다.",
                    "vi": "Đầm nhựa đường dùng 2 xe lu 6 tấn làm đồng thời.",
                    "situation": "formal"
                }
            ],
            "relatedTerms": ["dam-nen", "mat-duong-nhua", "may-rai"]
        },
        {
            "slug": "may-rai",
            "korean": "포장기/피니셔",
            "vietnamese": "máy rải",
            "hanja": None,
            "hanjaReading": None,
            "pronunciation": "포장기/피니셔 / máy rải [마이 자이]",
            "meaningKo": "아스팔트 혼합물이나 콘크리트를 도로 표면에 균일하게 펼치는 기계 장비입니다. 통역 시 '피니셔'는 영어 'finisher'에서 온 외래어이므로 베트남에서는 'máy rải'로 표현해야 하며, 장비 폭(bề rộng rải)과 포설 속도(tốc độ rải)를 함께 명시해야 합니다. 베트남 현장에서는 장비 조작 미숙으로 포설 두께가 불균일한 경우가 많으므로, 자동 레벨링 시스템(hệ thống san bằng tự động) 사용을 권장하고 작업 전 교육을 강조해야 합니다. 특히 경사 구간에서는 재료 흘러내림 방지를 위한 주의가 필요합니다.",
            "meaningVi": "Thiết bị cơ giới dùng để rải đều hỗn hợp nhựa đường hoặc bê tông lên mặt đường. Cần quy định rõ chiều rộng rải (thường 3~6m) và tốc độ rải (thường 2~4m/phút). Máy hiện đại có hệ thống san bằng tự động để đảm bảo độ dày đồng đều. Kỹ năng điều khiển máy rất quan trọng, cần đào tạo trước khi thi công. Trên đoạn dốc phải chú ý chống trượt vật liệu.",
            "context": "아스팔트 및 콘크리트 포장공사 현장의 핵심 장비",
            "culturalNote": "한국은 최신 자동화 포장기를 사용하여 정밀 시공이 가능하지만, 베트남은 구형 장비가 많고 수동 조작에 의존하여 품질 편차가 큽니다. 한국 기술자가 베트남 현장에서 포장 두께 불균일을 지적할 때 장비 한계로 개선이 어려운 경우가 있으므로, 통역사는 장비 수준 차이를 이해하고 실현 가능한 대안(측량 빈도 증가, 수작업 보정 등)을 제안할 수 있어야 합니다.",
            "commonMistakes": [
                {
                    "mistake": "'피니셔'를 'finisher'로 영어 발음",
                    "correction": "베트남어로 'máy rải' 또는 'máy rải nhựa'",
                    "explanation": "외래어가 아닌 베트남어 용어를 사용해야 현장에서 통합니다"
                },
                {
                    "mistake": "'펼치기'를 'mở ra'(열다)로 번역",
                    "correction": "포설/펼치기는 'rải' 또는 'trải'",
                    "explanation": "'mở'는 문을 여는 것이고, 도로 재료는 'rải'를 씁니다"
                },
                {
                    "mistake": "포설 두께를 대략적으로만 말함",
                    "correction": "'độ dày rải 5cm'처럼 정확한 수치로",
                    "explanation": "포장 품질은 두께 정확도에 크게 좌우되므로 수치가 필수입니다"
                }
            ],
            "examples": [
                {
                    "ko": "피니셔로 5cm 두께로 포설하고 즉시 롤러로 다지세요.",
                    "vi": "Dùng máy rải phủ dày 5cm rồi dùng lu đầm ngay.",
                    "situation": "onsite"
                },
                {
                    "ko": "포장기 속도를 너무 빠르게 하면 두께가 불균일합니다.",
                    "vi": "Nếu tốc độ máy rải quá nhanh thì độ dày không đều.",
                    "situation": "onsite"
                },
                {
                    "ko": "이 장비는 6m 폭으로 한 번에 포설할 수 있습니다.",
                    "vi": "Thiết bị này có thể rải một lần rộng 6m.",
                    "situation": "formal"
                }
            ],
            "relatedTerms": ["mat-duong-nhua", "lu-rung", "mat-duong-be-tong"]
        },
        {
            "slug": "cap-phoi-da",
            "korean": "쇄석기층",
            "vietnamese": "cấp phối đá",
            "hanja": "碎石基層",
            "hanjaReading": "碎(부술 쇄) + 石(돌 석) + 基(터 기) + 層(층 층)",
            "pronunciation": "쇄석기층 / cấp phối đá [깝 퍼이 다]",
            "meaningKo": "다양한 크기의 쇄석(부순 돌)을 적절히 배합하여 노반 위에 깔아 만드는 하부 포장층입니다. 통역 시 '골재 기층', '보조기층'과 혼동하지 않도록 주의하고, 베트남 현장에서는 입도(cấp phối hạt) 시험 결과를 정확히 전달해야 합니다. 특히 과립분(hạt mịn quá cỡ)이 많으면 배수가 안 되고, 조립분(hạt thô)이 많으면 다짐이 어려워 품질 문제가 발생하므로, 입도 분포 그래프를 현장과 공유하며 설명해야 합니다. 베트남 채석장마다 석질 차이가 커서 공급원 변경 시 재검증이 필수입니다.",
            "meaningVi": "Lớp kết cấu phía dưới bằng đá dăm được phối trộn với các cỡ hạt khác nhau, rải trên lớp móng đường. Tỷ lệ cấp phối hạt phải đạt tiêu chuẩn: quá nhiều hạt mịn sẽ kém thoát nước, quá nhiều hạt thô sẽ khó đầm nén. Cần kiểm tra cấp phối bằng phân tích sàng và so sánh với đường cong cấp phối tiêu chuẩn. Chất lượng đá từ các mỏ khác nhau ở Việt Nam có thể khác biệt lớn nên cần kiểm tra lại khi đổi nguồn cung.",
            "context": "도로 포장 공사의 기층 시공 단계에서 사용",
            "culturalNote": "한국은 쇄석 품질 관리가 엄격하고 표준화되어 있지만, 베트남은 채석장 관리 수준이 제각각이어서 같은 지역 내에서도 품질 편차가 큽니다. 한국 감리자가 입도 시험을 요구할 때 베트남 시공사가 '이전에도 이렇게 했다'며 반발하는 경우가 있으므로, 통역사는 품질 기준의 중요성과 시험의 필요성을 설득력 있게 전달해야 합니다. 또한 베트남은 석산 허가가 엄격하여 공급 불안정이 발생할 수 있으므로 대체 공급원을 미리 확보하도록 조언해야 합니다.",
            "commonMistakes": [
                {
                    "mistake": "'쇄석'을 'đá vỡ'(깨진 돌)로 직역",
                    "correction": "'đá dăm'(쇄석) 또는 'cấp phối đá'(쇄석 혼합물)",
                    "explanation": "'đá vỡ'는 일반적 깨진 돌이고, 건설에서는 'đá dăm'을 씁니다"
                },
                {
                    "mistake": "'입도'를 '알갱이 크기'로 풀어서만 설명",
                    "correction": "'cấp phối hạt' 또는 'phân bố cỡ hạt'",
                    "explanation": "기술 용어는 표준 베트남어를 사용해야 시험 보고서와 일치합니다"
                },
                {
                    "mistake": "기층/보조기층을 구분 없이 'lớp móng'로 통칭",
                    "correction": "기층은 'lớp móng trên', 보조기층은 'lớp móng dưới'",
                    "explanation": "각 층의 역할이 다르므로 명확히 구분해야 합니다"
                }
            ],
            "examples": [
                {
                    "ko": "쇄석 기층은 20cm 두께로 2층에 나눠 다짐하세요.",
                    "vi": "Lớp cấp phối đá dày 20cm, chia làm 2 lớp để đầm nén.",
                    "situation": "onsite"
                },
                {
                    "ko": "입도 시험 결과 과립분이 많아서 석분을 줄이겠습니다.",
                    "vi": "Kết quả phân tích sàng cho thấy quá nhiều hạt mịn nên sẽ giảm bột đá.",
                    "situation": "formal"
                },
                {
                    "ko": "이 채석장 자재는 품질이 좋아서 계속 사용하겠습니다.",
                    "vi": "Vật liệu từ mỏ đá này chất lượng tốt nên sẽ tiếp tục dùng.",
                    "situation": "onsite"
                }
            ],
            "relatedTerms": ["lop-mong-duong", "lop-lot", "dam-nen"]
        },
        {
            "slug": "lop-lot",
            "korean": "보조기층",
            "vietnamese": "lớp lót",
            "hanja": "補助基層",
            "hanjaReading": "補(도울 보) + 助(도울 조) + 基(터 기) + 層(층 층)",
            "pronunciation": "보조기층 / lớp lót [럽 롯]",
            "meaningKo": "노상과 쇄석기층 사이에 시공하는 중간 기초층으로, 상부 하중을 분산시키고 모세관 현상을 차단하는 역할을 합니다. 통역 시 '차단층', '동상방지층'이라고도 하며, 베트남 현장에서는 지하수위(mực nước ngầm)가 높은 구간에서 필수임을 강조해야 합니다. 재료는 주로 양질의 모래나 선별 쇄석을 사용하며, 다짐도 기준이 상부 기층보다 낮지만(90% 이상) 배수 기능이 중요하므로 재료 선정 시 투수성(tính thấm nước)을 확인해야 합니다. 베트남 남부 메콩델타 지역은 지하수위가 특히 높아 보조기층 시공이 필수입니다.",
            "meaningVi": "Lớp kết cấu nằm giữa lớp nền đất và lớp cấp phối đá, có nhiệm vụ phân bố tải trọng và ngăn nước ngầm dâng lên. Còn gọi là lớp chống thấm hoặc lớp chống đóng băng. Vật liệu thường dùng là cát sạch hoặc đá dăm sàng, độ chặt yêu cầu ≥90%. Ở vùng đồng bằng sông Cửu Long nước ngầm cao nên lớp này rất quan trọng để chống hư hỏng mặt đường do nước.",
            "context": "도로공사에서 노상 상태가 불량하거나 지하수위가 높은 구간에 적용",
            "culturalNote": "한국은 계절별 온도 변화가 커서 동상방지를 위한 보조기층이 중요하지만, 베트남은 동결이 없어 주로 지하수 차단 목적으로 사용됩니다. 베트남 남부는 우기에 지하수위가 급상승하여 보조기층 없이 시공한 도로가 침하하는 사례가 많으므로, 한국 기술자가 설계 단계에서 보조기층 추가를 제안할 때 베트남 측이 비용 문제로 반대하는 경우가 있습니다. 통역사는 장기적 유지비 절감 효과를 설명하여 설득해야 합니다.",
            "commonMistakes": [
                {
                    "mistake": "'보조기층'을 'lớp phụ'(부수적 층)로 번역",
                    "correction": "'lớp lót' 또는 'lớp móng dưới'",
                    "explanation": "'lớp phụ'는 중요도가 낮다는 오해를 줄 수 있습니다"
                },
                {
                    "mistake": "'모세관 현상'을 설명 없이 직역",
                    "correction": "'hiện tượng mao dẫn'으로 번역 후 '지하수가 위로 올라오는 현상'으로 부연",
                    "explanation": "베트남 현장 인력이 기술 용어를 모르는 경우가 많아 부연 설명이 필요합니다"
                },
                {
                    "mistake": "지하수위를 '물 높이'로 직역",
                    "correction": "'mực nước ngầm' 또는 'cao độ nước ngầm'",
                    "explanation": "기술 용어는 정확한 표준어를 사용해야 합니다"
                }
            ],
            "examples": [
                {
                    "ko": "이 구간은 지하수위가 높아서 보조기층 15cm를 추가하겠습니다.",
                    "vi": "Đoạn này mực nước ngầm cao nên sẽ bổ sung lớp lót dày 15cm.",
                    "situation": "formal"
                },
                {
                    "ko": "보조기층 재료는 투수성이 좋은 모래를 사용하세요.",
                    "vi": "Vật liệu lớp lót dùng cát có tính thấm nước tốt.",
                    "situation": "onsite"
                },
                {
                    "ko": "보조기층이 없어서 포장 아래로 물이 차올라 침하가 발생했습니다.",
                    "vi": "Không có lớp lót nên nước dâng lên dưới mặt đường gây lún.",
                    "situation": "formal"
                }
            ],
            "relatedTerms": ["lop-mong-duong", "cap-phoi-da", "dam-nen"]
        }
    ]

    # 5. 중복 제거 필터링
    filtered_terms = [term for term in new_terms if term['slug'] not in existing_slugs]

    if not filtered_terms:
        print("⚠️  모든 용어가 이미 존재합니다. 추가할 용어가 없습니다.")
        return

    # 6. 데이터 병합 및 저장
    data.extend(filtered_terms)

    with open(file_path, 'w', encoding='utf-8') as f:
        json.dump(data, f, ensure_ascii=False, indent=2)

    print(f"✅ {len(filtered_terms)}개 용어 추가 완료!")
    print(f"📂 파일: {file_path}")
    print(f"📊 총 용어 수: {len(data)}개")

    # 추가된 용어 목록 출력
    print("\n추가된 용어:")
    for term in filtered_terms:
        print(f"  - {term['slug']}: {term['korean']} / {term['vietnamese']}")

if __name__ == "__main__":
    main()
