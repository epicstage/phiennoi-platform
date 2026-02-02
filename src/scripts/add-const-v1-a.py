import json
import os

# 파일 경로 설정
file_path = os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', 'data', 'terms', 'construction.json')

# 기존 데이터 로드
with open(file_path, 'r', encoding='utf-8') as f:
    data = json.load(f)

# 기존 slug 목록
existing_slugs = {t['slug'] for t in data}

# 신규 용어 10개 (기초공사/토공사)
new_terms = [
    {
        "slug": "danh-coc",
        "korean": "말뚝항타",
        "vietnamese": "Đóng cọc",
        "hanja": "말뚝項打",
        "hanjaReading": "말(말 발) + 뚝(뚝 독) + 항(목 항) + 타(칠 타)",
        "pronunciation": "danh cọc",
        "meaningKo": "지반이 연약하거나 건축물의 하중이 클 때, 기초를 지지하기 위해 땅속 깊이 말뚝을 박아 넣는 공법입니다. 통역 시 '항타'와 '타입'을 혼동하지 않도록 주의해야 하며, 베트남에서는 'đóng cọc' 외에도 'ép cọc'(압입), 'khoan cọc'(천공) 등 공법에 따라 다른 용어를 사용합니다. 현장에서는 '말뚝박기'라는 구어체도 자주 사용되므로, 공식 문서에서는 '말뚝항타'로 정확히 번역하고, 작업 지시는 '말뚝박기'로 통역하는 유연성이 필요합니다. 항타 깊이, 지지력, N값 등 관련 수치도 함께 통역해야 합니다.",
        "meaningVi": "Công pháp đóng cọc là phương pháp thi công móng cọc bằng cách đóng cọc thẳng đứng xuống lòng đất để chịu tải trọng của công trình. Được sử dụng khi đất yếu hoặc tải trọng công trình lớn. Có nhiều phương pháp như đóng cọc, ép cọc, khoan cọc tùy theo điều kiện địa chất và yêu cầu kỹ thuật.",
        "context": "기초공사 설계 및 시공 단계에서 사용하며, 지질조사 결과에 따라 말뚝 종류와 항타 방법을 결정합니다.",
        "culturalNote": "한국은 지반이 비교적 단단하여 말뚝 길이가 짧은 편이지만, 베트남 남부(호치민 등)는 연약 지반이 많아 30m 이상의 깊은 말뚝을 사용하는 경우가 많습니다. 베트남에서는 소음 규제로 인해 주간에만 항타 작업이 가능하며, 도심지에서는 저소음 공법(압입식)을 선호합니다. 한국의 'PHC파일'을 베트nam에서는 'cọc ly tâm' 또는 'cọc bê tông ứng suất trước'라고 부르며, 공법별 베트nam어 용어를 정확히 구분해야 합니다.",
        "commonMistakes": [
            {
                "mistake": "항타를 '타입 공사'로 번역",
                "correction": "đóng cọc 또는 thi công cọc",
                "explanation": "'타입'은 pile의 외래어이므로 공법명인 '항타'는 đóng cọc으로 번역해야 합니다."
            },
            {
                "mistake": "'말뚝박기'를 공식 문서에 그대로 사용",
                "correction": "공식: 말뚝항타, 현장: 말뚝박기",
                "explanation": "구어체와 공식 용어를 상황에 맞게 구분해야 합니다."
            },
            {
                "mistake": "모든 말뚝을 'cọc'로만 통역",
                "correction": "PHC파일: cọc ly tâm, 강관말뚝: cọc thép ống",
                "explanation": "말뚝 종류에 따라 정확한 베트남어 용어를 사용해야 합니다."
            }
        ],
        "examples": [
            {
                "ko": "내일부터 말뚝항타 작업을 시작하니 소음 민원에 대비하세요.",
                "vi": "Từ ngày mai bắt đầu công tác đóng cọc, hãy chuẩn bị ứng phó khiếu nại về tiếng ồn.",
                "situation": "onsite"
            },
            {
                "ko": "지질조사 결과 N값이 낮아 말뚝 길이를 25m로 연장합니다.",
                "vi": "Kết quả khảo sát địa chất cho thấy chỉ số N thấp nên kéo dài chiều dài cọc lên 25m.",
                "situation": "formal"
            },
            {
                "ko": "말뚝항타 시 진동으로 인근 건물에 균열 발생 가능성이 있습니다.",
                "vi": "Khi đóng cọc có thể gây nứt công trình lân cận do rung động.",
                "situation": "formal"
            }
        ],
        "relatedTerms": ["ji-bung-gong-sa", "khao-sat", "mong-coc", "지내력", "진동측정"]
    },
    {
        "slug": "dat-chong",
        "korean": "흙막이",
        "vietnamese": "Đất chống",
        "hanja": None,
        "hanjaReading": None,
        "pronunciation": "dát chống",
        "meaningKo": "굴착 시 주변 지반의 붕괴를 방지하기 위해 설치하는 가설 구조물입니다. 통역 시 '흙막이벽', '토류벽', 'Earth retaining wall' 등 다양한 표현이 혼용되므로 맥락에 따라 정확히 구분해야 합니다. 베트남에서는 'đất chống', 'tường chắn đất', 'vây cừ tràm' 등 공법에 따라 용어가 달라집니다. 현장에서 '흙막이 치기', '버팀대 설치' 등의 작업 지시가 나올 때, 안전과 직결되므로 정확한 통역이 필수입니다. 공법(CIP, SCW, Sheet pile 등)별 베트남어 용어와 시공 순서를 숙지해야 합니다.",
        "meaningVi": "Kết cấu tạm thời được lắp đặt để ngăn đất sụt lở khi đào móng sâu. Có nhiều phương pháp như vây cừ tràm, tường chắn đất bê tông cốt thép, tường cọc khoan nhồi. Đây là công tác quan trọng đảm bảo an toàn thi công và công trình lân cận.",
        "context": "지하층 시공 시 굴착 깊이가 1.5m를 초과하는 경우 반드시 설치하며, 지하 주차장, 지하철 등 대규모 지하 공사에서 필수적입니다.",
        "culturalNote": "한국은 CIP(현장타설) 공법을 많이 사용하지만, 베트남은 공사 기간과 비용 문제로 Sheet pile(강널말뚝) 또는 전통적인 'vây cừ tràm'(나무 흙막이)을 선호합니다. 베트남 남부는 지하수위가 높아 흙막이 공사 시 배수 작업이 필수이며, 우기에는 공사가 지연되는 경우가 많습니다. 한국의 '어스앵커' 공법을 베트남에서는 'neo đất', '버팀대'는 'giằng chống'이라고 부르며, 안전 규정도 양국이 다르므로 주의해야 합니다.",
        "commonMistakes": [
            {
                "mistake": "흙막이를 단순히 'tường đất'로 번역",
                "correction": "đất chống 또는 tường chắn đất",
                "explanation": "'tường đất'는 흙벽을 의미하므로 가설 구조물인 흙막이와 다릅니다."
            },
            {
                "mistake": "모든 공법을 'đất chống'으로 통칭",
                "correction": "CIP: tường cọc khoan nhồi, Sheet pile: cừ tràm thép",
                "explanation": "공법에 따라 정확한 용어를 사용해야 합니다."
            },
            {
                "mistake": "'버팀대'를 '기둥'으로 오역",
                "correction": "giằng chống (버팀대), cột (기둥)",
                "explanation": "가설 지보재와 영구 구조물을 명확히 구분해야 합니다."
            }
        ],
        "examples": [
            {
                "ko": "흙막이 설치 후 굴착 작업을 진행하겠습니다.",
                "vi": "Sau khi lắp đặt đất chống sẽ tiến hành công tác đào đất.",
                "situation": "onsite"
            },
            {
                "ko": "이번 프로젝트는 CIP 공법으로 흙막이벽을 시공합니다.",
                "vi": "Dự án này thi công tường chắn đất bằng phương pháp cọc khoan nhồi tại chỗ (CIP).",
                "situation": "formal"
            },
            {
                "ko": "흙막이 변위 측정 결과 안전 기준치를 초과했습니다.",
                "vi": "Kết quả đo chuyển vị đất chống vượt quá tiêu chuẩn an toàn.",
                "situation": "formal"
            }
        ],
        "relatedTerms": ["dao-ho-mong", "an-toan-cong-truong", "mong-bang", "어스앵커", "버팀대"]
    },
    {
        "slug": "khao-sat-dia-chat",
        "korean": "지반조사",
        "vietnamese": "Khảo sát địa chất",
        "hanja": "地盤調査",
        "hanjaReading": "지(땅 지) + 반(쟁반 반) + 조(살필 조) + 사(살필 사)",
        "pronunciation": "카오삿 디아짓",
        "meaningKo": "건축물 시공 전 지반의 물리적·화학적 성질을 조사하여 기초 설계에 필요한 자료를 수집하는 작업입니다. 통역 시 '지질조사', '토질조사' 등과 혼용되므로 맥락을 정확히 파악해야 합니다. 베트남에서는 'khảo sát địa chất', 'khảo sát địa kỹ thuật' 등으로 불리며, 조사 항목(N값, 지내력, 지하수위 등)을 베트남어로 정확히 통역하는 것이 중요합니다. 보고서에는 'bản đồ địa chất'(지질도), 'mặt cắt địa tầng'(지층 단면도) 등 전문 용어가 포함되므로 사전 학습이 필요합니다.",
        "meaningVi": "Công tác khảo sát để xác định tính chất vật lý, cơ học của đất nền phục vụ thiết kế móng công trình. Bao gồm khoan khảo sát, lấy mẫu, thí nghiệm hiện trường (SPT) và phòng thí nghiệm để xác định sức chịu tải, độ lún, mực nước ngầm và các thông số địa chất khác.",
        "context": "모든 건설 프로젝트의 설계 전 단계에서 필수적으로 수행하며, 조사 결과에 따라 기초 형식(직접기초/말뚝기초)을 결정합니다.",
        "culturalNote": "한국은 지반조사 보고서가 매우 상세하며, 법적으로 의무화되어 있지만, 베트남은 중소 규모 공사에서는 간략한 조사만 하는 경우가 많습니다. 베트남 남부(메콩델타)는 연약 지반이 많아 N값이 5 이하인 경우가 흔하며, 이런 경우 '말뚝기초' 또는 '지반개량'이 필수입니다. 한국의 '표준관입시험(SPT)'을 베트남에서는 'thí nghiệm xuyên tiêu chuẩn' 또는 간단히 'SPT'라고 부르며, N값은 'chỉ số N'으로 통역합니다.",
        "commonMistakes": [
            {
                "mistake": "지반조사를 '땅 조사'로 직역",
                "correction": "khảo sát địa chất",
                "explanation": "전문 용어는 정확한 베트남어 표현을 사용해야 합니다."
            },
            {
                "mistake": "N값을 '엔 값'으로 음역",
                "correction": "chỉ số N",
                "explanation": "기술 용어는 베트남어로 풀어 설명해야 합니다."
            },
            {
                "mistake": "'지내력'과 '지지력'을 구분 없이 통역",
                "correction": "지내력: sức chịu tải của đất nền, 지지력: sức chịu tải của cọc",
                "explanation": "지반과 말뚝의 하중 지지 능력을 명확히 구분해야 합니다."
            }
        ],
        "examples": [
            {
                "ko": "지반조사 결과 N값이 평균 8로 나왔습니다.",
                "vi": "Kết quả khảo sát địa chất cho chỉ số N trung bình là 8.",
                "situation": "formal"
            },
            {
                "ko": "지하수위가 높아서 흙막이 공사 시 배수 작업이 필요합니다.",
                "vi": "Do mực nước ngầm cao nên cần công tác thoát nước khi thi công đất chống.",
                "situation": "onsite"
            },
            {
                "ko": "지반조사 보고서를 검토한 결과 말뚝기초로 변경해야 합니다.",
                "vi": "Sau khi xem xét báo cáo khảo sát địa chất cần thay đổi sang móng cọc.",
                "situation": "formal"
            }
        ],
        "relatedTerms": ["ji-bung-gong-sa", "mong-coc", "danh-coc", "N값", "지내력"]
    },
    {
        "slug": "suc-chiu-tai-dat-nen",
        "korean": "지내력",
        "vietnamese": "Sức chịu tải đất nền",
        "hanja": "地耐力",
        "hanjaReading": "지(땅 지) + 내(견딜 내) + 력(힘 력)",
        "pronunciation": "숙치우타이 닷넌",
        "meaningKo": "지반이 건축물의 하중을 견딜 수 있는 능력으로, 기초 설계의 핵심 지표입니다. 통역 시 '지지력'과 혼동하지 않도록 주의해야 하며, '지내력'은 지반 자체의 하중 지지 능력, '지지력'은 말뚝이 하중을 지지하는 능력을 의미합니다. 베트남어로는 'sức chịu tải đất nền'(지내력), 'sức chịu tải cọc'(지지력)로 명확히 구분됩니다. 설계 문서에서는 '허용지내력', '극한지내력' 등의 용어가 나오므로, 각각 'sức chịu tải cho phép', 'sức chịu tải cực hạn'으로 정확히 통역해야 합니다.",
        "meaningVi": "Khả năng chịu tải của đất nền dưới móng công trình. Là thông số quan trọng để thiết kế móng, xác định bằng khảo sát địa chất và thí nghiệm. Bao gồm sức chịu tải cho phép (áp dụng hệ số an toàn) và sức chịu tải cực hạn (trước khi đất bị phá hoại).",
        "context": "기초 설계 시 지반조사 보고서의 지내력 수치를 바탕으로 기초 형식과 크기를 결정하며, 지내력이 부족한 경우 지반개량 또는 말뚝기초를 적용합니다.",
        "culturalNote": "한국은 설계기준에서 허용지내력을 엄격히 적용하지만, 베트남은 중소형 프로젝트에서 안전율을 낮게 적용하는 경우가 있어 주의가 필요합니다. 베트남 남부는 연약 지반이 많아 지내력이 5~10 tf/m² 정도로 낮은 반면, 북부(하노이)는 상대적으로 단단한 지반이 많습니다. '토크'(tonf/m²)와 'kN/m²' 단위 변환도 통역 시 자주 필요하며, 1 tf/m² ≈ 10 kN/m²입니다.",
        "commonMistakes": [
            {
                "mistake": "지내력과 지지력을 구분 없이 'sức chịu tải'로만 통역",
                "correction": "지내력: sức chịu tải đất nền, 지지력: sức chịu tải cọc",
                "explanation": "지반과 말뚝의 하중 지지 능력을 명확히 구분해야 합니다."
            },
            {
                "mistake": "허용지내력을 '안전지내력'으로 오역",
                "correction": "sức chịu tải cho phép",
                "explanation": "'cho phép'은 허용을 의미하며, 안전은 'an toàn'입니다."
            },
            {
                "mistake": "단위 변환 없이 수치만 통역",
                "correction": "10 tf/m² = 100 kN/m²",
                "explanation": "양국이 사용하는 단위가 다를 수 있으므로 변환 여부를 확인해야 합니다."
            }
        ],
        "examples": [
            {
                "ko": "이 지역의 허용지내력은 8 tf/m²입니다.",
                "vi": "Sức chịu tải cho phép của đất nền khu vực này là 8 tf/m² (80 kN/m²).",
                "situation": "formal"
            },
            {
                "ko": "지내력이 부족해서 지반개량 공사가 필요합니다.",
                "vi": "Do sức chịu tải đất nền không đủ nên cần cải tạo nền đất.",
                "situation": "onsite"
            },
            {
                "ko": "극한지내력은 20 tf/m²이지만 안전율 3을 적용하여 허용지내력은 6.7 tf/m²입니다.",
                "vi": "Sức chịu tải cực hạn là 20 tf/m² nhưng áp dụng hệ số an toàn 3 thì sức chịu tải cho phép là 6.7 tf/m².",
                "situation": "formal"
            }
        ],
        "relatedTerms": ["khao-sat-dia-chat", "mong-bang", "mong-coc", "지반개량", "안전율"]
    },
    {
        "slug": "do-dat",
        "korean": "성토",
        "vietnamese": "Đổ đất",
        "hanja": "盛土",
        "hanjaReading": "성(성할 성) + 토(흙 토)",
        "pronunciation": "도닷",
        "meaningKo": "낮은 지반을 높이기 위해 흙을 쌓아 올리는 작업으로, 도로, 제방, 부지 조성 등에 사용됩니다. 통역 시 '성토'와 반대 개념인 '절토'(깎아내기)를 함께 숙지해야 하며, 베트남어로는 각각 'đổ đất', 'đào đất'로 구분됩니다. 현장에서는 '흙 쌓기', '흙 깎기' 등 구어체가 사용되므로 상황에 맞게 통역해야 합니다. 성토 작업 시 '다짐도', '함수비', '층별 다짐' 등의 품질 관리 용어도 자주 나오므로 'độ đầm chặt', 'hàm lượng nước', 'đầm lèn theo lớp' 등을 숙지해야 합니다.",
        "meaningVi": "Công tác đổ đắp đất để nâng cao mặt bằng hoặc tạo nền móng. Đất đổ phải được đầm chặt theo từng lớp (thường 20-30cm) để đạt độ chặt yêu cầu. Sử dụng trong xây dựng đường, đê, kè, san lấp mặt bằng. Đất đổ cần kiểm tra hàm lượng nước và độ đầm chặt.",
        "context": "부지 조성, 도로 건설, 제방 축조 등에서 필수 공정이며, 성토 후 일정 기간 침하를 기다려야 구조물 시공이 가능합니다.",
        "culturalNote": "한국은 성토 작업 시 품질 관리가 엄격하며, 층별 다짐 시험(다짐도 95% 이상)을 철저히 하지만, 베트남은 소규모 공사에서는 육안 점검으로 대체하는 경우가 많습니다. 베트남 남부는 우기에 성토 작업이 어려우며, 흙의 함수비가 높아 다짐이 잘 되지 않습니다. '다짐 장비'도 한국은 로드롤러가 일반적이지만, 베트남은 진동다짐기(đầm cóc)를 많이 사용합니다. 성토 후 '침하 대기 기간'을 한국은 수개월 두지만, 베트남은 공사 기간 단축을 위해 짧게 하는 경향이 있습니다.",
        "commonMistakes": [
            {
                "mistake": "성토를 '흙 붓기'로 직역",
                "correction": "đổ đất 또는 đắp đất",
                "explanation": "'đổ đất'은 성토, 'đắp đất'은 쌓기를 의미하며 문맥에 맞게 사용합니다."
            },
            {
                "mistake": "다짐도를 '압축도'로 오역",
                "correction": "độ đầm chặt",
                "explanation": "'độ đầm chặt'은 다짐의 정도를 나타내는 전문 용어입니다."
            },
            {
                "mistake": "절토와 성토를 혼동",
                "correction": "성토: đổ đất (쌓기), 절토: đào đất (깎기)",
                "explanation": "정반대 작업이므로 명확히 구분해야 합니다."
            }
        ],
        "examples": [
            {
                "ko": "성토 작업은 20cm씩 층별로 다짐하면서 진행합니다.",
                "vi": "Công tác đổ đất tiến hành đầm lèn theo từng lớp 20cm.",
                "situation": "onsite"
            },
            {
                "ko": "다짐도 시험 결과 95%를 충족했습니다.",
                "vi": "Kết quả thí nghiệm độ đầm chặt đạt 95%.",
                "situation": "formal"
            },
            {
                "ko": "성토 후 3개월간 침하 대기 기간을 두겠습니다.",
                "vi": "Sau khi đổ đất sẽ để thời gian chờ lún 3 tháng.",
                "situation": "formal"
            }
        ],
        "relatedTerms": ["dao-dat", "절토", "다짐도", "함수비", "침하"]
    },
    {
        "slug": "cat-dat",
        "korean": "절토",
        "vietnamese": "Cắt đất",
        "hanja": "切土",
        "hanjaReading": "절(끊을 절) + 토(흙 토)",
        "pronunciation": "깟닷",
        "meaningKo": "높은 지반을 깎아내어 평탄하게 만드는 작업으로, 도로 건설, 부지 조성 등에서 성토와 함께 사용됩니다. 통역 시 '절개', '굴착'과 구분해야 하며, '절토'는 자연 지반을 깎는 것, '굴착'은 기초나 지하층을 파는 것을 의미합니다. 베트남어로는 'cắt đất', 'đào đất', 'khai thác mặt bằng' 등으로 표현되며, 맥락에 따라 선택해야 합니다. 절토 작업 시 '법면 보호', '배수 처리', '토석 반출' 등의 용어가 자주 나오므로 사전 학습이 필요합니다.",
        "meaningVi": "Công tác đào bỏ đất để hạ thấp mặt bằng hoặc tạo mặt phẳng thi công. Thường kết hợp với công tác đổ đất (cân bằng đào đắp). Cần lưu ý bảo vệ mái taluy, thoát nước mặt và xử lý đất đào thải. Sử dụng máy xúc, máy ủi để thi công.",
        "context": "도로 건설에서 언덕을 깎거나, 부지 조성 시 평탄화 작업에 사용하며, 절토량과 성토량을 균형있게 계획하여 토사 반출 비용을 절감합니다.",
        "culturalNote": "한국은 절토 시 법면 보호(콘크리트 뿜칠, 식생)를 의무화하지만, 베트남은 소규모 공사에서는 생략하는 경우가 많아 우기에 토사 유실이 발생합니다. 베트남은 인건비가 저렴하여 소규모 절토는 인력으로 하는 경우도 있으나, 한국은 대부분 장비를 사용합니다. '토사 반출'을 한국은 '잔토 처리'라고 하며, 베트남어로는 'vận chuyển đất thải' 또는 'xử lý đất thừa'로 표현합니다. 절토 경사(법면 기울기)도 양국 기준이 다르므로 설계도 검토 시 주의해야 합니다.",
        "commonMistakes": [
            {
                "mistake": "절토를 '굴착'으로 통역",
                "correction": "절토: cắt đất (지반 깎기), 굴착: đào móng (기초 파기)",
                "explanation": "절토는 넓은 면적의 지반 깎기, 굴착은 특정 부위 파기입니다."
            },
            {
                "mistake": "법면을 '벽면'으로 오역",
                "correction": "mái taluy (법면), tường (벽)",
                "explanation": "자연 경사면과 구조물 벽을 구분해야 합니다."
            },
            {
                "mistake": "'잔토'를 '남은 흙'으로 직역",
                "correction": "đất thải 또는 đất thừa",
                "explanation": "'đất thải'는 폐기할 흙, 'đất thừa'는 여분의 흙을 의미합니다."
            }
        ],
        "examples": [
            {
                "ko": "절토 구간의 법면은 1:1.5 기울기로 시공합니다.",
                "vi": "Mái taluy đoạn cắt đất thi công với độ dốc 1:1.5.",
                "situation": "formal"
            },
            {
                "ko": "절토량이 성토량보다 많아서 잔토 처리 계획이 필요합니다.",
                "vi": "Khối lượng cắt đất nhiều hơn đổ đất nên cần kế hoạch xử lý đất thải.",
                "situation": "onsite"
            },
            {
                "ko": "비탈면 보호를 위해 콘크리트 뿜칠 작업을 실시합니다.",
                "vi": "Thực hiện phun bê tông để bảo vệ mái taluy.",
                "situation": "onsite"
            }
        ],
        "relatedTerms": ["do-dat", "dao-ho-mong", "법면", "잔토처리", "토공"]
    },
    {
        "slug": "lan-lai-dat",
        "korean": "되메우기",
        "vietnamese": "Lấp lại đất",
        "hanja": None,
        "hanjaReading": None,
        "pronunciation": "럽라이닷",
        "meaningKo": "기초 구조물 시공 후 여분의 공간에 흙을 다시 채워 넣는 작업입니다. 통역 시 '뒤채움', '되메우기' 등으로 불리며, 영어로는 'backfill'입니다. 베트남어로는 'lấp lại đất', 'đắp đất trở lại', 'hoàn thổ' 등으로 표현되며, 현장에서는 간단히 'lấp lại'라고도 합니다. 되메우기 작업 시 '다짐', '배수', '침하 방지' 등이 중요하며, 부실 시공 시 건물 침하나 균열의 원인이 됩니다. '양질의 토사', '사질토', '투수성' 등의 용어도 함께 숙지해야 합니다.",
        "meaningVi": "Công tác đắp đất trở lại sau khi hoàn thành móng hoặc công trình ngầm. Đất lấp lại cần đầm chặt cẩn thận để tránh lún, sử dụng đất tốt có tính thoát nước. Thường đắp theo lớp 20-30cm và kiểm tra độ đầm chặt. Đây là công đoạn quan trọng ảnh hưởng đến ổn định công trình.",
        "context": "기초 공사, 배관 매설, 지하 구조물 시공 후 필수 공정이며, 되메우기 품질이 나쁘면 지반 침하로 인한 구조물 손상이 발생합니다.",
        "culturalNote": "한국은 되메우기 시 '굵은 모래', '쇄석' 등 양질의 재료를 사용하고 층별 다짐을 철저히 하지만, 베트남은 비용 절감을 위해 파낸 흙을 그대로 사용하는 경우가 많습니다. 베트남 남부는 점토질 흙이 많아 배수가 잘 안 되므로, 되메우기 시 사질토 또는 쇄석을 사용하는 것이 좋습니다. '다짐 장비'도 한국은 진동롤러를 사용하지만, 베트남은 소형 현장에서 '다짐봉'(đầm đóng) 또는 '플레이트 다짐기'(đầm bàn)를 많이 사용합니다.",
        "commonMistakes": [
            {
                "mistake": "되메우기를 '다시 덮기'로 직역",
                "correction": "lấp lại đất 또는 hoàn thổ",
                "explanation": "'lấp lại'는 되메우기, 'hoàn thổ'는 복토를 의미합니다."
            },
            {
                "mistake": "'양질의 토사'를 '좋은 흙'으로 통역",
                "correction": "đất tốt có tính thoát nước (배수성 좋은 흙)",
                "explanation": "기술적 특성을 명확히 설명해야 합니다."
            },
            {
                "mistake": "다짐 없이 흙만 채우는 것으로 오해",
                "correction": "lấp lại phải đầm chặt từng lớp (층별 다짐 필수)",
                "explanation": "되메우기는 단순 채움이 아니라 다짐이 필수입니다."
            }
        ],
        "examples": [
            {
                "ko": "기초 타설 후 되메우기 작업을 시작하겠습니다.",
                "vi": "Sau khi đổ móng sẽ bắt đầu công tác lấp lại đất.",
                "situation": "onsite"
            },
            {
                "ko": "되메우기에는 양질의 사질토를 사용하고 20cm씩 다짐합니다.",
                "vi": "Công tác lấp lại sử dụng đất cát tốt và đầm chặt từng lớp 20cm.",
                "situation": "formal"
            },
            {
                "ko": "되메우기 불량으로 인해 바닥에 균열이 발생했습니다.",
                "vi": "Do lấp lại đất không đảm bảo chất lượng nên sàn bị nứt.",
                "situation": "onsite"
            }
        ],
        "relatedTerms": ["do-dat", "다짐", "침하", "배수", "양질토"]
    },
    {
        "slug": "xu-ly-dat-thua",
        "korean": "잔토처리",
        "vietnamese": "Xử lý đất thừa",
        "hanja": "殘土處理",
        "hanjaReading": "잔(남을 잔) + 토(흙 토) + 처(처리할 처) + 리(다스릴 리)",
        "pronunciation": "쑤리 닷투어",
        "meaningKo": "굴착이나 절토 작업 후 남은 흙을 처리하는 작업으로, 공사 현장에서 발생하는 토사를 반출하거나 재활용하는 과정입니다. 통역 시 '토사 반출', '여토 처리', '잔토 반출' 등으로 불리며, 베트남어로는 'xử lý đất thải', 'vận chuyển đất thừa', 'đổ đất thải' 등으로 표현됩니다. 현장에서는 '흙 버리기', '토사 운반' 등 구어체가 사용되므로 상황에 맞게 통역해야 합니다. 환경 규제로 인해 '합법 처리장', '토사 적치장' 등의 용어도 함께 숙지해야 합니다.",
        "meaningVi": "Công tác vận chuyển và xử lý đất thừa sau khi đào đất. Đất thải phải được vận chuyển đến bãi thải hợp pháp hoặc tái sử dụng cho công trình khác. Cần có giấy phép vận chuyển và xác nhận nơi đổ đất hợp quy định. Chi phí xử lý đất thải thường tính theo khối lượng (m³) và khoảng cách vận chuyển.",
        "context": "지하층 굴착, 절토 공사 등에서 발생한 토사를 처리하며, 환경 규제에 따라 지정된 장소에 반출해야 합니다.",
        "culturalNote": "한국은 잔토 처리 시 환경 규제가 엄격하여 합법 처리장 이용이 의무화되어 있고, 불법 투기 시 강력한 처벌이 있지만, 베트남은 규제가 느슨하여 불법 투기가 빈번합니다. 베트남 도심지에서는 잔토 반출 시간 제한(야간 금지)이 있으며, 차량 과적 단속도 엄격합니다. 잔토 처리 비용은 한국이 훨씬 비싸며(운반비 + 처리비), 베트남은 상대적으로 저렴하지만 합법 처리 시 비용이 증가하는 추세입니다. '토사 운반 차량'을 한국은 '덤프트럭'이라 하고, 베트남은 'xe ben'(벤차)이라고 부릅니다.",
        "commonMistakes": [
            {
                "mistake": "잔토를 '쓰레기'로 번역",
                "correction": "đất thải (폐토), rác thải (쓰레기)",
                "explanation": "건설 폐기물 중 토사는 'đất thải', 기타 쓰레기는 'rác thải'입니다."
            },
            {
                "mistake": "'처리장'을 '공장'으로 오역",
                "correction": "bãi thải hợp pháp (합법 처리장)",
                "explanation": "'bãi thải'는 토사 적치장, 'nhà máy'는 공장입니다."
            },
            {
                "mistake": "반출과 반입을 혼동",
                "correction": "반출: vận chuyển ra (내보내기), 반입: vận chuyển vào (들여오기)",
                "explanation": "토사의 이동 방향을 명확히 구분해야 합니다."
            }
        ],
        "examples": [
            {
                "ko": "잔토 처리는 00 처리장으로 반출하겠습니다.",
                "vi": "Đất thải sẽ được vận chuyển đến bãi thải 00.",
                "situation": "formal"
            },
            {
                "ko": "오늘 덤프트럭 10대로 잔토 200m³를 반출했습니다.",
                "vi": "Hôm nay đã vận chuyển 200m³ đất thải bằng 10 xe ben.",
                "situation": "onsite"
            },
            {
                "ko": "잔토 처리 비용이 예상보다 높아서 예산 조정이 필요합니다.",
                "vi": "Chi phí xử lý đất thải cao hơn dự kiến nên cần điều chỉnh ngân sách.",
                "situation": "formal"
            }
        ],
        "relatedTerms": ["dao-dat", "cat-dat", "xe-tai-ben", "토사", "반출"]
    },
    {
        "slug": "tuong-chan",
        "korean": "옹벽",
        "vietnamese": "Tường chắn",
        "hanja": "擁壁",
        "hanjaReading": "옹(안을 옹) + 벽(벽 벽)",
        "pronunciation": "뜨엉찬",
        "meaningKo": "절토나 성토로 인한 비탈면의 토압을 지지하기 위해 설치하는 구조물입니다. 통역 시 '흙막이벽'과 혼동하지 않도록 주의해야 하며, '옹벽'은 영구 구조물, '흙막이벽'은 가설 구조물입니다. 베트남어로는 'tường chắn đất', 'tường trọng lực' (중력식 옹벽), 'tường cánh tay đòn' (캔틸레버 옹벽) 등으로 세분화됩니다. 옹벽 설계 시 '토압', '배수', '기초 지내력', '전도', '활동' 등의 검토 항목이 있으므로 관련 용어를 숙지해야 합니다.",
        "meaningVi": "Kết cấu chắn đất vĩnh viễn để chống đỡ áp lực đất ở vị trí có chênh lệch cao độ. Có nhiều loại: tường trọng lực (dựa vào trọng lượng), tường cánh tay đòn, tường cọc chắn. Cần tính toán áp lực đất, khả năng chống lật, chống trượt và bố trí hệ thống thoát nước sau tường.",
        "context": "도로 건설, 부지 조성, 하천 제방 등에서 높낮이 차이가 있는 곳에 설치하며, 붕괴 방지를 위한 필수 구조물입니다.",
        "culturalNote": "한국은 옹벽 설계 기준이 엄격하여 구조 계산서 제출이 의무이지만, 베트남은 소규모 옹벽(3m 이하)은 표준 도면으로 시공하는 경우가 많습니다. 베트남 남부는 연약 지반이 많아 옹벽 기초를 말뚝으로 지지하는 경우가 많으며, 우기에는 배수 처리가 중요합니다. 한국의 '블록식 옹벽'을 베트남에서는 'tường khối lắp ghép', '석축'은 'tường đá xây'이라고 부릅니다. 옹벽 배수공(weep hole)을 'lỗ thoát nước'라고 하며, 막히면 토압 증가로 붕괴 위험이 있으므로 유지관리가 중요합니다.",
        "commonMistakes": [
            {
                "mistake": "옹벽과 흙막이벽을 구분 없이 통역",
                "correction": "옹벽: tường chắn (영구), 흙막이: đất chống (가설)",
                "explanation": "영구 구조물과 가설 구조물을 명확히 구분해야 합니다."
            },
            {
                "mistake": "'토압'을 '흙 압력'으로 직역",
                "correction": "áp lực đất",
                "explanation": "'áp lực đất'은 토압을 의미하는 전문 용어입니다."
            },
            {
                "mistake": "배수공을 '배수관'으로 오역",
                "correction": "lỗ thoát nước (배수공, weep hole)",
                "explanation": "옹벽의 작은 배수 구멍과 일반 배수관을 구분해야 합니다."
            }
        ],
        "examples": [
            {
                "ko": "절토 구간에 높이 5m의 캔틸레버 옹벽을 설치합니다.",
                "vi": "Lắp đặt tường chắn kiểu cánh tay đòn cao 5m tại đoạn cắt đất.",
                "situation": "formal"
            },
            {
                "ko": "옹벽 배수공이 막혀서 토압이 증가했습니다.",
                "vi": "Lỗ thoát nước tường chắn bị tắc nên áp lực đất tăng.",
                "situation": "onsite"
            },
            {
                "ko": "옹벽 기초는 지내력 부족으로 말뚝 지지를 적용합니다.",
                "vi": "Móng tường chắn do sức chịu tải không đủ nên áp dụng cọc chống.",
                "situation": "formal"
            }
        ],
        "relatedTerms": ["dat-chong", "cat-dat", "토압", "배수", "기초"]
    },
    {
        "slug": "phuong-phap-coc",
        "korean": "파일공법",
        "vietnamese": "Phương pháp cọc",
        "hanja": "pile工法",
        "hanjaReading": "파일(pile 영어) + 공(장인 공) + 법(법 법)",
        "pronunciation": "프엉팝 콕",
        "meaningKo": "연약 지반이나 건물 하중이 클 때 말뚝(파일)을 사용하여 기초를 지지하는 공법의 총칭입니다. 통역 시 '파일'과 '말뚝'을 혼용하여 사용하므로 맥락을 파악해야 하며, 베트남어로는 'phương pháp cọc', 'công pháp móng cọc' 등으로 표현됩니다. 파일 종류에 따라 'cọc đóng'(기성말뚝), 'cọc khoan nhồi'(현장타설말뚝), 'cọc ép'(압입말뚝) 등으로 구분되며, 각각의 시공 방법과 특성을 숙지해야 합니다. 베트남 현장에서는 'PHC파일'(cọc ly tâm), 'H-pile'(cọc thép chữ H) 등 제품명도 자주 사용됩니다.",
        "meaningVi": "Tổng hợp các công pháp thi công móng cọc để chuyển tải trọng công trình xuống lớp đất có sức chịu tải tốt ở sâu. Bao gồm cọc đóng (đóng sẵn), cọc khoan nhồi (đổ bê tông tại chỗ), cọc ép (ép thủy lực). Lựa chọn công pháp dựa vào địa chất, tải trọng, điều kiện thi công và chi phí.",
        "context": "연약 지반 또는 고층 건물의 기초 공사에서 필수적이며, 지질조사 결과에 따라 적합한 파일 공법을 선정합니다.",
        "culturalNote": "한국은 PHC파일(프리스트레스트 고강도 콘크리트 파일)을 가장 많이 사용하지만, 베트남은 비용 문제로 일반 콘크리트 파일이나 목재 파일도 사용합니다. 베트남 남부(호치민)는 연약 지반이 깊어 파일 길이가 30~50m에 달하며, 북부(하노이)는 상대적으로 짧습니다. 베트남에서는 소음 규제로 인해 도심지에서는 '압입 공법'(cọc ép)을 선호하며, '항타 공법'(cọc đóng)은 외곽 지역에서 주로 사용합니다. 한국의 '어스드릴 공법'을 베트남에서는 'khoan nhồi ướt', '올케이싱 공법'은 'khoan nhồi khô'라고 부릅니다.",
        "commonMistakes": [
            {
                "mistake": "모든 파일을 'cọc'로만 통역",
                "correction": "PHC파일: cọc ly tâm, H-pile: cọc thép chữ H",
                "explanation": "파일 종류에 따라 정확한 베트남어 명칭을 사용해야 합니다."
            },
            {
                "mistake": "공법과 제품명을 혼동",
                "correction": "공법: phương pháp cọc, 제품: loại cọc",
                "explanation": "시공 방법과 재료를 구분해야 합니다."
            },
            {
                "mistake": "'지지말뚝'과 '마찰말뚝'을 구분 없이 통역",
                "correction": "지지말뚝: cọc chống, 마찰말뚝: cọc ma sát",
                "explanation": "하중 전달 원리가 다르므로 구분해야 합니다."
            }
        ],
        "examples": [
            {
                "ko": "이 프로젝트는 PHC파일 공법으로 기초를 시공합니다.",
                "vi": "Dự án này thi công móng bằng phương pháp cọc ly tâm ứng suất trước (PHC).",
                "situation": "formal"
            },
            {
                "ko": "소음 문제로 항타 공법 대신 압입 공법을 사용하겠습니다.",
                "vi": "Do vấn đề tiếng ồn sẽ sử dụng phương pháp ép cọc thay vì đóng cọc.",
                "situation": "onsite"
            },
            {
                "ko": "말뚝 재하시험 결과 설계 하중을 만족했습니다.",
                "vi": "Kết quả thí nghiệm tải trọng cọc đạt yêu cầu thiết kế.",
                "situation": "formal"
            }
        ],
        "relatedTerms": ["danh-coc", "mong-coc", "khao-sat-dia-chat", "PHC파일", "재하시험"]
    }
]

# 기존 slug와 중복 제거
filtered_terms = [t for t in new_terms if t['slug'] not in existing_slugs]

# 데이터 추가
data.extend(filtered_terms)

# 저장
with open(file_path, 'w', encoding='utf-8') as f:
    json.dump(data, f, ensure_ascii=False, indent=2)

print(f"Added {len(filtered_terms)} terms. Total: {len(data)}")
