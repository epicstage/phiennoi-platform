#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
의료 용어 추가 스크립트 v3-e
20개 신규 용어: 소화기/비뇨기 질환
"""

import json
import os

# PATH CODE (MUST USE)
file_path = os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', 'data', 'terms', 'medical.json')
with open(file_path, 'r', encoding='utf-8') as f:
    data = json.load(f)  # data is a LIST, not dict

existing_slugs = {t['slug'] for t in data}

# 20개 신규 용어 (Tier S 기준)
new_terms = [
    {
        "slug": "noi-soi-da-day",
        "korean": "위내시경",
        "vietnamese": "Nội soi dạ dày",
        "hanja": "胃內視鏡",
        "hanjaReading": "胃(위 위) + 內(안 내) + 視(볼 시) + 鏡(거울 경)",
        "pronunciation": "위네시경",
        "meaningKo": "위 내부를 관찰하기 위해 내시경을 삽입하는 검사. 통역 시 '위카메라'로 오해하는 환자가 많으므로 '내시경 검사'임을 명확히 해야 함. '금식'은 베트남어로 'nhịn ăn/nhịn đói'로 구분해 설명. 검사 전 진정제 사용 여부는 '진정 내시경(nội soi có gây mê)'으로 구분. 조직검사는 'sinh thiết'으로 별도 용어임을 주의.",
        "meaningVi": "Thủ thuật kiểm tra bên trong dạ dày bằng cách đưa ống nội soi qua miệng. Bệnh nhân cần nhịn ăn uống trước khi làm. Có thể thực hiện với hoặc không gây mê tùy theo tình trạng. Thường dùng để chẩn đoán viêm loét, polyp, ung thư dạ dày.",
        "context": "내시경 검사실, 소화기내과",
        "culturalNote": "한국은 건강검진 시 위내시경이 기본 항목이나 베트남은 증상 있을 때만 실시. 한국은 수면내시경(진정제) 선호하나 베트남은 비용 문제로 비진정 내시경이 일반적. 통역 시 진정제 비용과 회복 시간 차이를 설명해야 환자 선택에 도움.",
        "commonMistakes": [
            {
                "mistake": "위카메라",
                "correction": "위내시경 검사",
                "explanation": "카메라는 일부일 뿐, 내시경은 관찰+조직검사+치료도 가능한 의료기구"
            },
            {
                "mistake": "nội soi bụng",
                "correction": "nội soi dạ dày",
                "explanation": "복강경(nội soi ổ bụng)과 위내시경은 완전히 다른 시술"
            },
            {
                "mistake": "수면내시경 = nội soi ngủ",
                "correction": "nội soi có gây mê/an thần",
                "explanation": "'ngủ'는 비전문적 표현, 정확한 의학용어 사용 필요"
            }
        ],
        "examples": [
            {
                "ko": "내일 위내시경 검사 예정이시니 오늘 밤 9시부터 금식하셔야 합니다.",
                "vi": "Ngày mai anh/chị sẽ làm nội soi dạ dày nên từ 9 giờ tối nay phải nhịn ăn uống.",
                "situation": "formal"
            },
            {
                "ko": "진정 내시경 하시면 검사 후 30분 정도 회복실에서 쉬셔야 해요.",
                "vi": "Nếu làm nội soi có gây mê thì sau khi làm phải nghỉ khoảng 30 phút ở phòng hồi sức.",
                "situation": "onsite"
            },
            {
                "ko": "위내시경 결과 조직검사가 필요한 부위가 발견되었습니다.",
                "vi": "Kết quả nội soi dạ dày phát hiện vùng cần sinh thiết.",
                "situation": "formal"
            }
        ],
        "relatedTerms": ["대장내시경", "조직검사", "소화성궤양", "위암"]
    },
    {
        "slug": "noi-soi-dai-trang",
        "korean": "대장내시경",
        "vietnamese": "Nội soi đại tràng",
        "hanja": "大腸內視鏡",
        "hanjaReading": "大(큰 대) + 腸(창자 장) + 內(안 내) + 視(볼 시) + 鏡(거울 경)",
        "pronunciation": "대장네시경",
        "meaningKo": "대장 내부를 관찰하기 위해 항문을 통해 내시경을 삽입하는 검사. 통역 시 검사 전 장정결제 복용(uống thuốc tẩy)을 반드시 설명해야 함. '용종제거술'은 검사 중 동시 진행 가능하므로 별도 수술 아님을 안내. 베트남 환자는 '항문 검사'에 대한 거부감이 있어 검사 필요성을 충분히 설명.",
        "meaningVi": "Kiểm tra bên trong đại tràng bằng cách đưa ống nội soi qua hậu môn. Trước khi làm phải uống thuốc tẩy để làm sạch ruột hoàn toàn. Có thể phát hiện và cắt polyp ngay trong quá trình nội soi. Thường dùng để tầm soát ung thư đại tràng.",
        "context": "소화기내과, 건강검진센터",
        "culturalNote": "한국은 50세 이상 건강검진 시 대장내시경 권장하나 베트남은 증상 없으면 잘 안 함. 장정결제 복용 과정이 힘들어 한국인도 기피하는데 베트남 환자는 더 생소함. 통역 시 '하루 전부터 맑은 유동식만 섭취'하는 과정을 단계별로 설명 필요.",
        "commonMistakes": [
            {
                "mistake": "nội soi hậu môn",
                "correction": "nội soi đại tràng",
                "explanation": "항문경(soi hậu môn)은 짧게만 보는 것, 대장내시경은 대장 전체 관찰"
            },
            {
                "mistake": "장세척 = rửa ruột",
                "correction": "làm sạch ruột bằng thuốc tẩy",
                "explanation": "'rửa'는 관장을 연상시킴, 약물 복용으로 배변하는 것임을 명확히"
            },
            {
                "mistake": "용종제거 = phẫu thuật cắt polyp",
                "correction": "cắt polyp trong khi nội soi",
                "explanation": "별도 수술이 아니라 내시경 중 시행 가능한 시술"
            }
        ],
        "examples": [
            {
                "ko": "대장내시경 전날부터 장정결제를 복용하시고 검사 당일 아침까지 물만 드세요.",
                "vi": "Từ ngày trước khi nội soi đại tràng phải uống thuốc tẩy và đến sáng ngày làm chỉ được uống nước.",
                "situation": "formal"
            },
            {
                "ko": "검사 중에 용종 3개 발견해서 바로 제거했습니다.",
                "vi": "Trong khi nội soi phát hiện 3 polyp và đã cắt bỏ ngay.",
                "situation": "onsite"
            },
            {
                "ko": "대장내시경은 대장암 조기발견에 가장 효과적인 검사입니다.",
                "vi": "Nội soi đại tràng là xét nghiệm hiệu quả nhất để phát hiện sớm ung thư đại tràng.",
                "situation": "formal"
            }
        ],
        "relatedTerms": ["대장용종", "대장암", "장정결제", "용종제거술"]
    },
    {
        "slug": "trao-nguoc-da-day-thuc-quan",
        "korean": "위식도역류질환",
        "vietnamese": "Trào ngược dạ dày thực quản",
        "hanja": "胃食道逆流疾患",
        "hanjaReading": "胃(위 위) + 食(먹을 식) + 道(길 도) + 逆(거스를 역) + 流(흐를 류) + 疾(병 질) + 患(근심 환)",
        "pronunciation": "위식도역류질환",
        "meaningKo": "위산이 식도로 역류하여 발생하는 질환으로 영어로 GERD. 통역 시 '가슴쓰림'은 베트남어로 'ợ nóng, nóng rát ngực'로 구분 설명. '역류'를 단순히 'nôn'(구토)로 오해하지 않도록 주의. 생활습관 개선(식후 바로 눕지 않기 등)이 중요하므로 환자교육 시 상세히 통역.",
        "meaningVi": "Bệnh do axit dạ dày trào ngược lên thực quản gây triệu chứng ợ nóng, đau rát ngực. Thường xảy ra sau khi ăn no, nằm ngay sau ăn hoặc ăn đêm muộn. Cần thay đổi thói quen ăn uống và có thể dùng thuốc ức chế axit. Nếu không điều trị có thể dẫn đến viêm loét thực quản.",
        "context": "소화기내과, 일반내과",
        "culturalNote": "한국은 야식 문화와 스트레스로 GERD 환자 많으나 베트nam은 상대적으로 적음. 한국은 약물치료 적극적이나 베트남은 생활습관 개선 우선. 통역 시 '카페인, 초콜릿, 술, 기름진 음식 피하기' 등 구체적 식이조절 방법 설명 필요.",
        "commonMistakes": [
            {
                "mistake": "역류 = nôn",
                "correction": "trào ngược",
                "explanation": "구토와 달리 의지와 무관하게 위산이 올라오는 것"
            },
            {
                "mistake": "ợ chua",
                "correction": "ợ nóng/trào ngược axit",
                "explanation": "'ợ chua'는 단순 신트림, GERD는 병적 상태"
            },
            {
                "mistake": "식도염 = viêm dạ dày",
                "correction": "viêm thực quản",
                "explanation": "위염과 식도염은 다른 질환"
            }
        ],
        "examples": [
            {
                "ko": "위식도역류질환은 식후 2-3시간은 눕지 않는 것이 중요합니다.",
                "vi": "Với bệnh trào ngược dạ dày thực quản, điều quan trọng là không nằm xuống trong 2-3 giờ sau khi ăn.",
                "situation": "formal"
            },
            {
                "ko": "가슴이 타는 것처럼 쓰리고 신물이 올라와요.",
                "vi": "Ngực nóng rát như bị bỏng và có axit trào ngược lên.",
                "situation": "informal"
            },
            {
                "ko": "제산제와 함께 생활습관 교정이 필요합니다.",
                "vi": "Cần dùng thuốc kháng axit kết hợp với thay đổi thói quen sinh hoạt.",
                "situation": "formal"
            }
        ],
        "relatedTerms": ["식도염", "위염", "소화성궤양", "제산제"]
    },
    {
        "slug": "loet-da-day-ta-trang",
        "korean": "소화성궤양",
        "vietnamese": "Loét dạ dày tá tràng",
        "hanja": "消化性潰瘍",
        "hanjaReading": "消(사라질 소) + 化(될 화) + 性(성품 성) + 潰(무너질 궤) + 瘍(부스럼 양)",
        "pronunciation": "소화성궤양",
        "meaningKo": "위나 십이지장 점막이 헐어서 생기는 궤양으로 위궤양과 십이지장궤양 포함. 통역 시 'Helicobacter pylori'는 '헬리코박터균'으로 설명하되 베트남어 'vi khuẩn HP'도 병기. 공복 시 통증과 식후 통증으로 위궤양/십이지장궤양 구분 가능. 제균치료는 '항생제 3제요법'으로 정확히 설명.",
        "meaningVi": "Tổn thương lòng dạ dày hoặc tá tràng do viêm loét. Nguyên nhân chủ yếu là nhiễm vi khuẩn HP (Helicobacter pylori) hoặc dùng thuốc giảm đau NSAID lâu dài. Triệu chứng điển hình là đau bụng, đói bụng thường đau nhiều hơn. Điều trị bằng thuốc kháng axit và diệt vi khuẩn HP.",
        "context": "소화기내과",
        "culturalNote": "한국은 HP 제균치료 보험 적용되나 베트남은 자비 부담. 한국은 내시경으로 조직검사 후 제균 여부 결정하나 베트남은 증상 치료 위주. 통역 시 제균치료의 중요성(재발 방지)과 항생제 복용 기간(보통 1-2주) 정확히 전달.",
        "commonMistakes": [
            {
                "mistake": "loét dạ dày = viêm dạ dày",
                "correction": "loét (궤양) ≠ viêm (염증)",
                "explanation": "위염은 염증, 궤양은 점막 손상이 더 깊은 상태"
            },
            {
                "mistake": "HP균 = vi rút HP",
                "correction": "vi khuẩn HP",
                "explanation": "세균(vi khuẩn)과 바이러스(vi rút) 혼동 주의"
            },
            {
                "mistake": "십이지장 = ruột non",
                "correction": "tá tràng",
                "explanation": "소장(ruột non) 전체가 아닌 십이지장(tá tràng) 특정"
            }
        ],
        "examples": [
            {
                "ko": "헬리코박터균 양성이 나와서 제균치료를 시작하겠습니다.",
                "vi": "Xét nghiệm dương tính với vi khuẩn HP nên sẽ bắt đầu điều trị diệt khuẩn.",
                "situation": "formal"
            },
            {
                "ko": "공복에 속이 쓰리고 밥 먹으면 좀 나아지는 증상은 십이지장궤양의 특징입니다.",
                "vi": "Triệu chứng đói bụng thì đau, ăn xong đỡ hơn là đặc trưng của loét tá tràng.",
                "situation": "onsite"
            },
            {
                "ko": "궤양 치료제를 최소 4주는 복용하셔야 합니다.",
                "vi": "Phải uống thuốc điều trị loét ít nhất 4 tuần.",
                "situation": "formal"
            }
        ],
        "relatedTerms": ["위염", "헬리코박터", "위출혈", "천공"]
    },
    {
        "slug": "polyp-dai-trang",
        "korean": "대장용종",
        "vietnamese": "Polyp đại tràng",
        "hanja": "大腸茸腫",
        "hanjaReading": "大(큰 대) + 腸(창자 장) + 茸(버섯 용) + 腫(부을 종)",
        "pronunciation": "대장용종",
        "meaningKo": "대장 점막에 생기는 혹으로 일부는 암으로 진행 가능. 통역 시 '용종'을 베트남어 'polyp'으로 그대로 사용하되 '혹(u)'과 구분. 선종성 용종(polyp tuyến)은 암 위험 높아 제거 필수. 내시경 중 절제술은 별도 수술 아님을 설명. 재발 가능하므로 정기 추적검사 필요.",
        "meaningVi": "Khối u nhỏ mọc trên niêm mạc đại tràng, một số loại có thể chuyển thành ung thư. Thường không có triệu chứng và được phát hiện khi nội soi. Polyp tuyến có nguy cơ ung thư hóa cao nên phải cắt bỏ. Có thể cắt ngay trong quá trình nội soi.",
        "context": "소화기내과, 건강검진",
        "culturalNote": "한국은 대장내시경 보급으로 용종 조기 발견율 높으나 베트남은 증상 없으면 검사 안 함. 한국은 5mm 이상 용종은 대부분 제거하나 베트남은 비용 문제로 큰 것만. 통역 시 용종 크기와 조직학적 유형에 따른 암화 위험도 설명 필요.",
        "commonMistakes": [
            {
                "mistake": "polyp = u",
                "correction": "polyp (용종) ≠ u (종양 일반)",
                "explanation": "용종은 특정 형태의 혹, 모든 u가 polyp은 아님"
            },
            {
                "mistake": "cắt polyp = phẫu thuật",
                "correction": "cắt polyp bằng nội soi",
                "explanation": "대부분 내시경으로 제거 가능, 개복수술 아님"
            },
            {
                "mistake": "모든 polyp = ung thư",
                "correction": "một số polyp có nguy cơ ung thư",
                "explanation": "선종성만 위험, 증식성 용종은 양성"
            }
        ],
        "examples": [
            {
                "ko": "대장내시경에서 5mm 용종 2개 발견되어 제거했습니다.",
                "vi": "Nội soi đại tràng phát hiện 2 polyp 5mm và đã cắt bỏ.",
                "situation": "formal"
            },
            {
                "ko": "조직검사 결과 선종성 용종으로 나와서 1년 후 재검 필요합니다.",
                "vi": "Kết quả sinh thiết là polyp tuyến nên cần tái khám sau 1 năm.",
                "situation": "onsite"
            },
            {
                "ko": "용종 크기가 작아서 바로 제거 가능합니다.",
                "vi": "Polyp nhỏ nên có thể cắt bỏ ngay.",
                "situation": "informal"
            }
        ],
        "relatedTerms": ["대장내시경", "대장암", "용종절제술", "선종"]
    },
    {
        "slug": "benh-crohn",
        "korean": "크론병",
        "vietnamese": "Bệnh Crohn",
        "hanja": None,
        "hanjaReading": None,
        "pronunciation": "크론병",
        "meaningKo": "소화관 전체에 발생 가능한 만성 염증성 장질환으로 IBD의 일종. 통역 시 '궤양성대장염'과 구분 필요 - 크론병은 전층 침범, 구강부터 항문까지 모든 소화관. '관해(remission)'와 '재발(relapse)' 용어 정확히 구분. 면역억제제 치료 시 감염 위험 설명 필수. 난치병이므로 장기 관리 필요성 강조.",
        "meaningVi": "Bệnh viêm mạn tính có thể xảy ra ở bất kỳ đâu trong đường tiêu hóa từ miệng đến hậu môn. Là bệnh tự miễn, không lây nhiễm. Triệu chứng gồm tiêu chảy, đau bụng, sụt cân. Điều trị bằng thuốc ức chế miễn dịch và sinh học. Cần theo dõi suốt đời vì bệnh có thể tái phát.",
        "context": "소화기내과, 희귀질환센터",
        "culturalNote": "한국은 IBD 치료제 보험 적용되고 전문센터 있으나 베트남은 진단/치료 어려움. 한국은 생물학적제제 사용 증가하나 베트남은 접근성 낮음. 통역 시 질병의 만성적 특성과 평생 관리 필요성, 정기 내시경 검사 중요성 설명.",
        "commonMistakes": [
            {
                "mistake": "Crohn = viêm đại tràng",
                "correction": "bệnh Crohn (viêm toàn bộ đường tiêu hóa)",
                "explanation": "대장염과 달리 소화관 전체 침범 가능"
            },
            {
                "mistake": "관해 = khỏi bệnh",
                "correction": "thuyên giảm/lui bệnh",
                "explanation": "완치 아니라 증상 없는 상태, 재발 가능"
            },
            {
                "mistake": "bệnh lây nhiễm",
                "correction": "bệnh tự miễn, không lây",
                "explanation": "전염병이 아니라 자가면역질환"
            }
        ],
        "examples": [
            {
                "ko": "크론병은 완치는 어렵지만 약물로 증상을 조절하며 지낼 수 있습니다.",
                "vi": "Bệnh Crohn khó chữa khỏi hoàn toàn nhưng có thể kiểm soát triệu chứng bằng thuốc.",
                "situation": "formal"
            },
            {
                "ko": "면역억제제 복용 중에는 감염 위험이 높으니 발열 시 즉시 내원하세요.",
                "vi": "Khi dùng thuốc ức chế miễn dịch, nguy cơ nhiễm trùng cao nên nếu sốt phải đến viện ngay.",
                "situation": "onsite"
            },
            {
                "ko": "현재 관해 상태지만 6개월마다 추적검사가 필요합니다.",
                "vi": "Hiện tại bệnh đang thuyên giảm nhưng cần tái khám mỗi 6 tháng.",
                "situation": "formal"
            }
        ],
        "relatedTerms": ["궤양성대장염", "염증성장질환", "면역억제제", "생물학적제제"]
    },
    {
        "slug": "viem-loet-dai-trang",
        "korean": "궤양성대장염",
        "vietnamese": "Viêm loét đại tràng",
        "hanja": "潰瘍性大腸炎",
        "hanjaReading": "潰(무너질 궤) + 瘍(부스럼 양) + 性(성품 성) + 大(큰 대) + 腸(창자 장) + 炎(불꽃 염)",
        "pronunciation": "궤양성대장염",
        "meaningKo": "대장에만 국한되어 발생하는 만성 염증성 장질환. 통역 시 '크론병'과 차이점 명확히 - 궤양성대장염은 대장만, 점막층만 침범. '혈변'은 'đi cầu ra máu'로 설명. 메살라진 등 약물 복용 순응도 중요. 중증 시 대장절제술 가능하므로 조기 치료 중요성 강조.",
        "meaningVi": "Viêm loét mạn tính chỉ xảy ra ở đại tràng, từ trực tràng lan dần lên. Triệu chứng chính là tiêu chảy có máu, đau bụng, táo bón. Là bệnh tự miễn không lây nhiễm. Điều trị chủ yếu bằng mesalazine và corticoid. Trường hợp nặng có thể cần phẫu thuật cắt đại tràng.",
        "context": "소화기내과",
        "culturalNote": "한국은 IBD 환자 증가 추세이나 베트남은 드문 편. 한국은 5-ASA 제제 보험 적용되나 베트남은 약값 부담. 통역 시 식이조절(섬유질 제한 등)과 스트레스 관리의 중요성 설명. 대장암 위험 증가하므로 정기 대장내시경 필요.",
        "commonMistakes": [
            {
                "mistake": "viêm loét = loét dạ dày",
                "correction": "viêm loét đại tràng (대장)",
                "explanation": "위궤양과 완전히 다른 질환"
            },
            {
                "mistake": "khỏi sau vài tuần",
                "correction": "bệnh mạn tính cần điều trị lâu dài",
                "explanation": "단기 치료로 완치 불가, 평생 관리 필요"
            },
            {
                "mistake": "혈변 = xuất huyết tiêu hóa",
                "correction": "đại tiện có máu/phân lẫn máu",
                "explanation": "소화관출혈 일반보다 구체적 표현"
            }
        ],
        "examples": [
            {
                "ko": "궤양성대장염은 재발과 관해를 반복하는 질환입니다.",
                "vi": "Viêm loét đại tràng là bệnh có tái phát và thuyên giảm luân phiên.",
                "situation": "formal"
            },
            {
                "ko": "하루 10회 이상 설사에 피가 섞여 나오면 입원 치료가 필요합니다.",
                "vi": "Nếu tiêu chảy trên 10 lần/ngày có lẫn máu thì cần nhập viện điều trị.",
                "situation": "onsite"
            },
            {
                "ko": "메살라진은 평생 복용해야 재발을 막을 수 있습니다.",
                "vi": "Phải uống mesalazine suốt đời mới ngăn được tái phát.",
                "situation": "formal"
            }
        ],
        "relatedTerms": ["크론병", "염증성장질환", "혈변", "메살라진"]
    },
    {
        "slug": "xo-gan",
        "korean": "간경변",
        "vietnamese": "Xơ gan",
        "hanja": "肝硬變",
        "hanjaReading": "肝(간 간) + 硬(굳을 경) + 變(변할 변)",
        "pronunciation": "간경변",
        "meaningKo": "간 조직이 섬유화되어 굳어지는 만성 간질환의 말기 상태. 통역 시 '복수(cổ trướng)'와 '정맥류(giãn tĩnh mạch)'는 합병증임을 구분. 원인으로 B형간염, C형간염, 알코올을 명확히. Child-Pugh 등급은 'phân độ/giai đoạn'으로 설명. 간이식은 'ghép gan'이며 말기 치료법임을 안내.",
        "meaningVi": "Giai đoạn cuối của bệnh gan mạn tính khi mô gan bị xơ hóa và cứng lại. Nguyên nhân chủ yếu là viêm gan B, C mạn tính hoặc uống rượu lâu năm. Biến chứng nguy hiểm gồm cổ trướng, giãn tĩnh mạch thực quản, hôn mê gan. Điều trị chủ yếu là ngăn tiến triển và xử lý biến chứng.",
        "context": "소화기내과, 간센터",
        "culturalNote": "한국은 B형간염 백신 접종으로 간경변 감소 중이나 베트남은 여전히 많음. 한국은 간이식 활발하나 베트남은 기증자 부족. 통역 시 금주의 절대적 중요성과 정기적 간암 검진(초음파+AFP) 필요성 강조.",
        "commonMistakes": [
            {
                "mistake": "xơ gan = ung thư gan",
                "correction": "xơ gan (간경변) ≠ ung thư gan (간암)",
                "explanation": "간경변은 간암 위험 높이지만 다른 질환"
            },
            {
                "mistake": "복수 = béo bụng",
                "correction": "cổ trướng (dịch ổ bụng)",
                "explanation": "비만과 복수는 전혀 다름"
            },
            {
                "mistake": "có thể hồi phục hoàn toàn",
                "correction": "không thể đảo ngược, chỉ ngăn tiến triển",
                "explanation": "간경변은 비가역적, 진행 억제만 가능"
            }
        ],
        "examples": [
            {
                "ko": "간경변 진단받으셨으니 절대 금주하셔야 합니다.",
                "vi": "Đã được chẩn đoán xơ gan nên tuyệt đối phải cấm rượu.",
                "situation": "formal"
            },
            {
                "ko": "복수가 차서 이뇨제를 처방하고 염분 제한이 필요합니다.",
                "vi": "Có cổ trướng nên kê thuốc lợi tiểu và cần hạn chế muối.",
                "situation": "onsite"
            },
            {
                "ko": "간경변 환자는 6개월마다 간암 검진을 받아야 합니다.",
                "vi": "Người bệnh xơ gan phải tầm soát ung thư gan mỗi 6 tháng.",
                "situation": "formal"
            }
        ],
        "relatedTerms": ["B형간염", "간암", "복수", "간이식"]
    },
    {
        "slug": "gan-nhiem-mo",
        "korean": "지방간",
        "vietnamese": "Gan nhiễm mỡ",
        "hanja": "脂肪肝",
        "hanjaReading": "脂(기름 지) + 肪(기름 방) + 肝(간 간)",
        "pronunciation": "지방간",
        "meaningKo": "간세포에 지방이 과도하게 축적된 상태로 비알코올성과 알코올성으로 구분. 통역 시 'fatty liver'를 'gan nhiễm mỡ'로 설명. 비만, 당뇨, 고지혈증이 원인이므로 체중감량(giảm cân)과 운동(tập thể dục) 중요성 강조. AST/ALT 수치는 'men gan'으로 설명. 방치 시 간염→간경변 진행 가능.",
        "meaningVi": "Tình trạng tế bào gan tích lũy quá nhiều mỡ. Phân loại thành gan nhiễm mỡ do rượu và không do rượu (NAFLD). Nguyên nhân chủ yếu là béo phì, đái tháo đường, rối loạn lipid máu. Thường không có triệu chứng, phát hiện qua siêu âm. Điều trị chủ yếu bằng giảm cân và thay đổi lối sống.",
        "context": "소화기내과, 건강검진",
        "culturalNote": "한국은 건강검진 보급으로 지방간 조기 발견 많으나 베트남은 증상 있을 때만 검사. 한국은 비만 증가로 지방간 급증하나 베트남은 상대적 적음. 통역 시 '술 안 마셔도 생길 수 있다'는 점과 체중 5-10% 감량만으로도 개선 가능함을 설명.",
        "commonMistakes": [
            {
                "mistake": "gan nhiễm mỡ = viêm gan",
                "correction": "gan nhiễm mỡ (지방간) ≠ viêm gan (간염)",
                "explanation": "염증 없이 지방만 축적된 상태"
            },
            {
                "mistake": "chỉ do uống rượu",
                "correction": "có gan nhiễm mỡ không do rượu",
                "explanation": "비만, 당뇨로도 발생"
            },
            {
                "mistake": "không nguy hiểm",
                "correction": "có thể tiến triển thành xơ gan",
                "explanation": "방치 시 간경변까지 진행 가능"
            }
        ],
        "examples": [
            {
                "ko": "지방간은 체중을 5-10% 줄이면 개선될 수 있습니다.",
                "vi": "Gan nhiễm mỡ có thể cải thiện nếu giảm 5-10% cân nặng.",
                "situation": "formal"
            },
            {
                "ko": "술을 전혀 안 드셔도 비만 때문에 지방간이 생길 수 있어요.",
                "vi": "Dù hoàn toàn không uống rượu vẫn có thể bị gan nhiễm mỡ do béo phì.",
                "situation": "informal"
            },
            {
                "ko": "간 수치가 높게 나왔는데 초음파에서 지방간 소견 보입니다.",
                "vi": "Men gan cao và siêu âm thấy hình ảnh gan nhiễm mỡ.",
                "situation": "onsite"
            }
        ],
        "relatedTerms": ["간수치", "비만", "당뇨병", "간염"]
    },
    {
        "slug": "viem-gan-b",
        "korean": "B형간염",
        "vietnamese": "Viêm gan B",
        "hanja": None,
        "hanjaReading": None,
        "pronunciation": "비형간염",
        "meaningKo": "B형간염바이러스(HBV)에 의한 간 염증으로 만성화 시 간경변, 간암 위험. 통역 시 '보균자(người mang virus)'와 '환자(bệnh nhân)'를 구분. 항원(kháng nguyên)과 항체(kháng thể) 검사 결과 설명 중요. 항바이러스제는 'thuốc kháng virus'. 수직감염 차단을 위한 신생아 백신 접종 설명 필수.",
        "meaningVi": "Viêm gan do virus viêm gan B (HBV) gây ra, có thể chuyển mạn tính và dẫn đến xơ gan, ung thư gan. Lây qua đường máu, quan hệ tình dục, mẹ truyền sang con. Có vaccine phòng ngừa hiệu quả. Người bệnh mạn tính cần dùng thuốc kháng virus lâu dài và theo dõi định kỳ.",
        "context": "소화기내과, 간센터",
        "culturalNote": "한국은 1980년대부터 백신 접종으로 보균율 크게 감소했으나 베트남은 여전히 높음. 한국은 항바이러스제 보험 적용되나 베트남은 비용 부담. 통역 시 가족 내 전파 예방(식기 공유 가능, 성관계 시 주의)과 정기 검진(간암 조기발견) 중요성 설명.",
        "commonMistakes": [
            {
                "mistake": "viêm gan B = ung thư gan",
                "correction": "viêm gan B có thể dẫn đến ung thư gan",
                "explanation": "간염과 간암은 다름, 간염이 간암 위험 높임"
            },
            {
                "mistake": "lây qua ăn uống chung",
                "correction": "không lây qua ăn uống chung",
                "explanation": "식기 공유로는 전염 안 됨, 혈액/체액 접촉만"
            },
            {
                "mistake": "người mang virus = bệnh nhân",
                "correction": "người mang virus có thể không bệnh",
                "explanation": "보균자는 증상 없을 수 있음"
            }
        ],
        "examples": [
            {
                "ko": "B형간염 보균자는 6개월마다 간 초음파와 혈액검사가 필요합니다.",
                "vi": "Người mang virus viêm gan B cần siêu âm gan và xét nghiệm máu mỗi 6 tháng.",
                "situation": "formal"
            },
            {
                "ko": "HBsAg 양성이고 HBeAg도 양성이면 전염력이 높은 상태입니다.",
                "vi": "Nếu HBsAg dương tính và HBeAg cũng dương tính thì khả năng lây cao.",
                "situation": "onsite"
            },
            {
                "ko": "항바이러스제를 임의로 중단하면 급성 악화될 수 있습니다.",
                "vi": "Nếu tự ý ngừng thuốc kháng virus có thể bị viêm gan cấp nặng.",
                "situation": "formal"
            }
        ],
        "relatedTerms": ["간경변", "간암", "항바이러스제", "백신"]
    },
    {
        "slug": "soi-mat",
        "korean": "담석증",
        "vietnamese": "Sỏi mật",
        "hanja": "膽石症",
        "hanjaReading": "膽(쓸개 담) + 石(돌 석) + 症(증세 증)",
        "pronunciation": "담석증",
        "meaningKo": "담낭이나 담관에 돌이 생기는 질환. 통역 시 '담낭(túi mật)'과 '담관(ống mật)' 위치 구분 중요. 담석산통은 'cơn đau mật'로 설명. 복강경 담낭절제술은 'cắt túi mật nội soi'. 무증상 담석은 경과관찰 가능하나 증상 있으면 수술 권유. 수술 후 소화 변화(기름진 음식 주의) 안내.",
        "meaningVi": "Sỏi hình thành trong túi mật hoặc ống mật. Nguyên nhân liên quan đến béo phì, chế độ ăn nhiều mỡ, tuổi tác. Triệu chứng điển hình là đau quặn vùng hạ sườn phải sau khi ăn no. Điều trị chủ yếu bằng phẫu thuật cắt túi mật nội soi. Sau mổ có thể tiêu chảy khi ăn nhiều dầu mỡ.",
        "context": "외과, 소화기내과",
        "culturalNote": "한국은 복강경 수술 보편화되어 회복 빠르나 베트남은 개복 수술도 많음. 한국은 무증상 담석도 수술 권유하나 베트남은 증상 있을 때만. 통역 시 수술 방법(복강경 vs 개복)에 따른 회복 기간과 흉터 차이 설명.",
        "commonMistakes": [
            {
                "mistake": "sỏi mật = sỏi thận",
                "correction": "sỏi mật (담석) ≠ sỏi thận (신석)",
                "explanation": "담석과 신석은 위치와 성분 다름"
            },
            {
                "mistake": "cắt túi mật = mất chức năng tiêu hóa",
                "correction": "có thể sống bình thường không có túi mật",
                "explanation": "담낭 없어도 간에서 담즙 분비 지속"
            },
            {
                "mistake": "sỏi nhỏ thì uống thuốc tan",
                "correction": "thuốc tan sỏi hiệu quả thấp",
                "explanation": "약물 용해는 효과 낮고 재발 많음"
            }
        ],
        "examples": [
            {
                "ko": "기름진 음식 먹고 나면 오른쪽 윗배가 심하게 아픈 것은 담석 증상입니다.",
                "vi": "Đau dữ dội vùng bụng trên bên phải sau khi ăn đồ nhiều dầu mỡ là triệu chứng sỏi mật.",
                "situation": "informal"
            },
            {
                "ko": "담낭에 돌이 여러 개 있어서 복강경으로 담낭 제거하겠습니다.",
                "vi": "Có nhiều sỏi trong túi mật nên sẽ cắt túi mật bằng nội soi.",
                "situation": "formal"
            },
            {
                "ko": "수술 후에는 기름진 음식을 한 번에 많이 드시지 마세요.",
                "vi": "Sau mổ không nên ăn quá nhiều đồ dầu mỡ một lúc.",
                "situation": "onsite"
            }
        ],
        "relatedTerms": ["담낭염", "담관염", "복강경수술", "췌장염"]
    },
    {
        "slug": "viem-tuy-cap",
        "korean": "급성췌장염",
        "vietnamese": "Viêm tụy cấp",
        "hanja": "急性膵臟炎",
        "hanjaReading": "急(급할 급) + 性(성품 성) + 膵(이자 췌) + 臟(장부 장) + 炎(불꽃 염)",
        "pronunciation": "급성췌장염",
        "meaningKo": "췌장에 급성 염증이 생긴 상태로 응급질환. 통역 시 원인으로 '담석'과 '알코올' 강조. 아밀라제/리파제는 'men tiêu hóa/men tụy'로 설명. 절대 금식(nhịn ăn tuyệt đối)이 초기 치료의 핵심. 중증 시 괴사성 췌장염(viêm tụy hoại tử) 진행 가능. 통증이 매우 심하므로 진통제 필요성 설명.",
        "meaningVi": "Viêm cấp tính của tuyến tụy, là cấp cứu ngoại khoa. Nguyên nhân thường gặp là sỏi mật và uống rượu. Triệu chứng điển hình là đau dữ dội vùng thượng vị lan ra lưng. Điều trị ban đầu là nhịn ăn hoàn toàn, truyền dịch, giảm đau. Trường hợp nặng có thể hoại tử tụy và tử vong.",
        "context": "응급실, 외과",
        "culturalNote": "한국은 음주 관련 췌장염 많으나 베트남은 담석 원인 비중 높음. 한국은 중환자실 치료 접근성 좋으나 베트남은 제한적. 통역 시 금주의 절대적 필요성과 재발 방지 위한 원인 제거(담석 수술 등) 중요성 강조.",
        "commonMistakes": [
            {
                "mistake": "tụy = gan",
                "correction": "tụy (췌장) ≠ gan (간)",
                "explanation": "췌장과 간은 다른 장기"
            },
            {
                "mistake": "có thể ăn nhẹ",
                "correction": "phải nhịn ăn tuyệt đối ban đầu",
                "explanation": "급성기에는 완전 금식 필수"
            },
            {
                "mistake": "uống thuốc giảm đau là đủ",
                "correction": "cần nhập viện điều trị tích cực",
                "explanation": "응급 입원 치료 필요, 집에서 진통제만으로는 위험"
            }
        ],
        "examples": [
            {
                "ko": "급성췌장염은 최소 3일은 금식하면서 수액 치료를 받아야 합니다.",
                "vi": "Viêm tụy cấp phải nhịn ăn ít nhất 3 ngày và điều trị truyền dịch.",
                "situation": "formal"
            },
            {
                "ko": "배꼽 주변이 극심하게 아프고 등으로 뻗치는 통증이 특징입니다.",
                "vi": "Đặc trưng là đau dữ dội vùng rốn và lan ra lưng.",
                "situation": "onsite"
            },
            {
                "ko": "췌장염 재발 방지를 위해 반드시 금주하셔야 합니다.",
                "vi": "Để ngăn tái phát viêm tụy phải tuyệt đối cấm rượu.",
                "situation": "formal"
            }
        ],
        "relatedTerms": ["담석증", "만성췌장염", "당뇨병", "알코올중독"]
    },
    {
        "slug": "soi-duong-tiet-nieu",
        "korean": "요로결석",
        "vietnamese": "Sỏi đường tiết niệu",
        "hanja": "尿路結石",
        "hanjaReading": "尿(오줌 뇨) + 路(길 로) + 結(맺을 결) + 石(돌 석)",
        "pronunciation": "요로결석",
        "meaningKo": "신장, 요관, 방광에 돌이 생기는 질환. 통역 시 '옆구리 통증(đau sườn lưng)'이 특징적 증상. 수분 섭취 증가가 예방과 치료에 핵심. 체외충격파쇄석술은 'tán sỏi ngoài cơ thể'. 혈뇨는 'tiểu ra máu'. 돌 크기에 따라 자연 배출 가능 여부 결정. 재발률 높아 식이조절 중요.",
        "meaningVi": "Sỏi hình thành trong thận, niệu quản hoặc bàng quang. Triệu chứng điển hình là đau quặn dữ dội vùng sườn lưng, tiểu ra máu. Nguyên nhân do uống ít nước, chế độ ăn nhiều muối. Điều trị tùy theo kích thước sỏi: nhỏ thì uống nhiều nước để tự đào thải, lớn thì tán sỏi hoặc phẫu thuật.",
        "context": "비뇨기과, 응급실",
        "culturalNote": "한국은 여름철 탈수로 요로결석 증가하나 베트남은 연중 더워 더 흔함. 한국은 체외충격파 보편화되었으나 베트남은 장비 접근성 낮음. 통역 시 하루 2-3L 물 섭취 권장과 칼슘/수산 많은 음식 제한 설명.",
        "commonMistakes": [
            {
                "mistake": "sỏi thận = sỏi mật",
                "correction": "sỏi thận (신석) ≠ sỏi mật (담석)",
                "explanation": "위치와 성분 완전히 다름"
            },
            {
                "mistake": "uống ít nước để tránh sỏi to",
                "correction": "uống nhiều nước để ngăn sỏi",
                "explanation": "탈수가 결석 원인, 수분 섭취가 예방책"
            },
            {
                "mistake": "모든 sỏi phải mổ",
                "correction": "sỏi nhỏ có thể tự ra",
                "explanation": "5mm 이하는 자연 배출 가능"
            }
        ],
        "examples": [
            {
                "ko": "5mm 이하 결석은 물 많이 드시면 자연 배출될 수 있습니다.",
                "vi": "Sỏi dưới 5mm có thể tự ra nếu uống nhiều nước.",
                "situation": "formal"
            },
            {
                "ko": "옆구리가 너무 아프고 소변에 피가 섞여 나왔어요.",
                "vi": "Đau sườn lưng dữ lắm và tiểu có lẫn máu.",
                "situation": "informal"
            },
            {
                "ko": "체외충격파로 돌을 깨뜨리는 시술을 하겠습니다.",
                "vi": "Sẽ làm thủ thuật tán sỏi ngoài cơ thể.",
                "situation": "onsite"
            }
        ],
        "relatedTerms": ["신장결석", "혈뇨", "수신증", "체외충격파쇄석술"]
    },
    {
        "slug": "phi-dai-tuyen-tien-liet",
        "korean": "전립선비대증",
        "vietnamese": "Phì đại tuyến tiền liệt",
        "hanja": "前立腺肥大症",
        "hanjaReading": "前(앞 전) + 立(설 립) + 腺(샘 선) + 肥(살찔 비) + 大(큰 대) + 症(증세 증)",
        "pronunciation": "전립선비대증",
        "meaningKo": "전립선이 커져서 요도를 압박하는 양성 질환. 통역 시 '암 아님'을 명확히 - 'u lành, không phải ung thư'. 배뇨 증상은 '빈뇨(tiểu đêm nhiều lần)', '세뇨(tiểu yếu)', '잔뇨감(cảm giác không hết nước tiểu)'. 알파차단제는 약물명보다 효과(giãn cơ tuyến tiền liệt) 설명. 급성 요폐 시 도뇨관 필요.",
        "meaningVi": "Tuyến tiền liệt to lên ch压 ép niệu đạo gây khó tiểu. Là bệnh lành tính, không phải ung thư. Triệu chứng gồm tiểu đêm nhiều, tiểu yếu, nhỏ giọt sau tiểu, cảm giác không hết nước tiểu. Điều trị bằng thuốc giãn cơ tuyến tiền liệt hoặc phẫu thuật nếu nặng.",
        "context": "비뇨기과",
        "culturalNote": "한국은 50대 이상 남성 절반이 증상 있으나 베트남은 의료 접근성 낮아 진단율 낮음. 한국은 약물치료 먼저 시도하나 베트남은 바로 수술 권유도 많음. 통역 시 PSA 검사(전립선암 배제)와 증상 점수표(IPSS) 설명.",
        "commonMistakes": [
            {
                "mistake": "phì đại = ung thư",
                "correction": "phì đại là u lành",
                "explanation": "비대증은 양성, 암과 다름"
            },
            {
                "mistake": "젊은 남성도 걸림",
                "correction": "chủ yếu nam giới trên 50 tuổi",
                "explanation": "나이 들수록 발생률 증가"
            },
            {
                "mistake": "uống thuốc = khỏi hẳn",
                "correction": "thuốc kiểm soát triệu chứng, không chữa khỏi",
                "explanation": "약은 증상 완화, 완치 아님"
            }
        ],
        "examples": [
            {
                "ko": "전립선이 커져서 소변 보기 힘든 것이지 암은 아닙니다.",
                "vi": "Tuyến tiền liệt to lên nên khó tiểu, không phải ung thư.",
                "situation": "formal"
            },
            {
                "ko": "밤에 소변 보러 몇 번씩 일어나시나요?",
                "vi": "Ban đêm dậy đi tiểu mấy lần?",
                "situation": "informal"
            },
            {
                "ko": "알파차단제를 복용하면 소변 줄기가 나아질 것입니다.",
                "vi": "Uống thuốc giãn cơ tuyến tiền liệt sẽ cải thiện dòng tiểu.",
                "situation": "onsite"
            }
        ],
        "relatedTerms": ["전립선암", "배뇨장애", "요폐", "PSA검사"]
    },
    {
        "slug": "viem-bang-quang",
        "korean": "방광염",
        "vietnamese": "Viêm bàng quang",
        "hanja": "膀胱炎",
        "hanjaReading": "膀(방광 방) + 胱(방광 광) + 炎(불꽃 염)",
        "pronunciation": "방광염",
        "meaningKo": "방광에 세균 감염으로 염증이 생긴 질환으로 여성에게 흔함. 통역 시 '배뇨통(đau khi tiểu)', '빈뇨(tiểu nhiều lần)', '잔뇨감'을 구분 설명. 항생제는 'kháng sinh'. 수분 섭취와 배뇨 참지 않기가 예방책. 반복 시 신우신염(viêm thận bể thận) 진행 가능하므로 조기 치료 중요.",
        "meaningVi": "Nhiễm khuẩn gây viêm bàng quang, hay gặp ở phụ nữ. Triệu chứng điển hình là đau rát khi tiểu, tiểu gấp nhiều lần, tiểu ít mỗi lần. Điều trị bằng kháng sinh thường 3-5 ngày. Phòng ngừa bằng cách uống đủ nước, không nhịn tiểu, vệ sinh sạch sẽ. Nếu tái phát nhiều cần tìm nguyên nhân.",
        "context": "비뇨기과, 일반내과",
        "culturalNote": "한국은 여성 방광염 흔해서 약국에서 항생제 쉽게 구입했으나 최근 규제. 베트남도 항생제 접근 쉬워 내성균 문제. 통역 시 항생제 전 과정 복용 중요성과 재발 시 소변배양 검사 필요성 설명.",
        "commonMistakes": [
            {
                "mistake": "viêm bàng quang = viêm thận",
                "correction": "viêm bàng quang (방광) ≠ viêm thận (신장)",
                "explanation": "방광염과 신우신염은 다름"
            },
            {
                "mistake": "uống kháng sinh 1-2 ngày là đủ",
                "correction": "phải uống đủ liều trình",
                "explanation": "증상 없어도 처방대로 끝까지 복용"
            },
            {
                "mistake": "chỉ phụ nữ mới bị",
                "correction": "nam giới cũng có thể bị",
                "explanation": "남성도 걸리나 여성이 더 흔함"
            }
        ],
        "examples": [
            {
                "ko": "소변 볼 때 따끔거리고 자주 마려운 증상은 방광염입니다.",
                "vi": "Đau rát khi tiểu và hay buồn tiểu là triệu chứng viêm bàng quang.",
                "situation": "formal"
            },
            {
                "ko": "항생제를 3일 처방드렸으니 꼭 다 드세요.",
                "vi": "Kê kháng sinh 3 ngày, nhớ uống hết.",
                "situation": "informal"
            },
            {
                "ko": "물을 많이 드시고 소변 참지 마세요.",
                "vi": "Uống nhiều nước và không nhịn tiểu.",
                "situation": "onsite"
            }
        ],
        "relatedTerms": ["요로감염", "신우신염", "배뇨통", "항생제"]
    },
    {
        "slug": "suy-than-cap",
        "korean": "급성신부전",
        "vietnamese": "Suy thận cấp",
        "hanja": "急性腎不全",
        "hanjaReading": "急(급할 급) + 性(성품 성) + 腎(콩팥 신) + 不(아니 부) + 全(온전 전)",
        "pronunciation": "급성신부전",
        "meaningKo": "신장 기능이 급격히 저하되는 응급상태. 통역 시 '투석(lọc máu/thẩm tích)'은 일시적일 수 있음을 설명. 크레아티닌 수치는 'chỉ số creatinine'으로. 원인으로 탈수, 약물, 감염 구분. 가역적이므로 원인 교정 시 회복 가능. 소변량 감소(thiểu niệu)가 주요 증상.",
        "meaningVi": "Suy giảm chức năng thận đột ngột trong vài giờ hoặc vài ngày. Nguyên nhân gồm mất nước nặng, nhiễm trùng, thuốc độc thận. Triệu chứng là tiểu ít, phù nề, mệt mỏi. Điều trị bằng truyền dịch, xử lý nguyên nhân, có thể cần lọc máu tạm thời. Nếu điều trị kịp thời có thể hồi phục hoàn toàn.",
        "context": "신장내과, 중환자실",
        "culturalNote": "한국은 중환자실 투석 접근성 좋으나 베트남은 제한적. 한국은 조기 발견으로 회복율 높으나 베트남은 늦게 오는 경우 많음. 통역 시 탈수 예방과 신독성 약물(소염진통제 등) 주의 설명.",
        "commonMistakes": [
            {
                "mistake": "suy thận cấp = suy thận mạn",
                "correction": "cấp có thể hồi phục, mạn không",
                "explanation": "급성은 가역적, 만성은 비가역적"
            },
            {
                "mistake": "lọc máu = suốt đời",
                "correction": "lọc máu tạm thời trong suy thận cấp",
                "explanation": "급성신부전 투석은 일시적"
            },
            {
                "mistake": "不喝水以减少尿",
                "correction": "cần truyền dịch đủ",
                "explanation": "탈수 교정이 치료의 핵심"
            }
        ],
        "examples": [
            {
                "ko": "크레아티닌 수치가 급격히 올라가서 급성신부전으로 진단했습니다.",
                "vi": "Chỉ số creatinine tăng đột ngột nên chẩn đoán suy thận cấp.",
                "situation": "formal"
            },
            {
                "ko": "소변량이 줄고 몸이 붓는 것은 신장 기능 저하 때문입니다.",
                "vi": "Tiểu ít và phù nề là do chức năng thận giảm.",
                "situation": "onsite"
            },
            {
                "ko": "일시적으로 투석이 필요하지만 회복되면 중단할 수 있습니다.",
                "vi": "Cần lọc máu tạm thời nhưng khi hồi phục có thể ngừng.",
                "situation": "formal"
            }
        ],
        "relatedTerms": ["만성신부전", "투석", "크레아티닌", "탈수"]
    },
    {
        "slug": "suy-than-man",
        "korean": "만성신부전",
        "vietnamese": "Suy thận mạn",
        "hanja": "慢性腎不全",
        "hanjaReading": "慢(느릴 만) + 性(성품 성) + 腎(콩팥 신) + 不(아니 부) + 全(온전 전)",
        "pronunciation": "만성신부전",
        "meaningKo": "신장 기능이 서서히 저하되어 회복 불가능한 상태. 통역 시 '투석'과 '신장이식'이 최종 치료법임을 명확히. 당뇨와 고혈압이 주요 원인이므로 혈당/혈압 조절 중요성 강조. 단백뇨는 'protein niệu'. 5단계로 구분하며 4-5단계는 투석 준비. 식이조절(저단백, 저염)이 진행 억제에 핵심.",
        "meaningVi": "Suy giảm chức năng thận từ từ, không thể hồi phục. Nguyên nhân chủ yếu là đái tháo đường và tăng huyết áp. Phân 5 giai đoạn, giai đoạn cuối cần lọc máu hoặc ghép thận. Điều trị chủ yếu là kiểm soát nguyên nhân, chế độ ăn ít protein ít muối, theo dõi chức năng thận định kỳ.",
        "context": "신장내과",
        "culturalNote": "한국은 투석 환자 많고 의료비 지원되나 베트남은 투석 접근성 낮고 비용 부담. 한국은 신장이식 활발하나 베트남은 기증자 매우 부족. 통역 시 혈액투석(lọc máu) vs 복막투석(thẩm phân phúc mạc) 차이와 각각의 장단점 설명.",
        "commonMistakes": [
            {
                "mistake": "suy thận mạn = có thể khỏi",
                "correction": "không thể đảo ngược, chỉ làm chậm tiến triển",
                "explanation": "만성신부전은 비가역적"
            },
            {
                "mistake": "giai đoạn 1-2 = phải lọc máu",
                "correction": "giai đoạn 5 mới cần lọc máu",
                "explanation": "초기는 약물과 식이로 관리"
            },
            {
                "mistake": "ăn nhiều protein để bổ thận",
                "correction": "phải hạn chế protein",
                "explanation": "고단백은 신장 부담 증가"
            }
        ],
        "examples": [
            {
                "ko": "만성신부전 3기로 저단백 식사와 혈압 조절이 중요합니다.",
                "vi": "Suy thận mạn giai đoạn 3, quan trọng là chế độ ăn ít protein và kiểm soát huyết áp.",
                "situation": "formal"
            },
            {
                "ko": "당뇨 조절 안 하면 신부전으로 진행됩니다.",
                "vi": "Nếu không kiểm soát đái tháo đường sẽ tiến triển thành suy thận.",
                "situation": "onsite"
            },
            {
                "ko": "신기능이 더 나빠지면 투석을 준비해야 합니다.",
                "vi": "Nếu chức năng thận giảm thêm phải chuẩn bị lọc máu.",
                "situation": "formal"
            }
        ],
        "relatedTerms": ["당뇨병", "고혈압", "혈액투석", "신장이식"]
    },
    {
        "slug": "viem-cau-than",
        "korean": "사구체신염",
        "vietnamese": "Viêm cầu thận",
        "hanja": "絲球體腎炎",
        "hanjaReading": "絲(실 사) + 球(공 구) + 體(몸 체) + 腎(콩팥 신) + 炎(불꽃 염)",
        "pronunciation": "사구체신염",
        "meaningKo": "신장의 사구체에 염증이 생긴 질환. 통역 시 '혈뇨(tiểu ra máu)'와 '단백뇨(protein niệu)'가 주요 증상. 급성과 만성 구분 중요 - 급성은 회복 가능. 부종은 특히 얼굴에 먼저(phù mặt). 신생검(sinh thiết thận)으로 확진. 스테로이드 치료 시 부작용 설명 필수.",
        "meaningVi": "Viêm các cầu thận (bộ lọc của thận). Triệu chứng gồm tiểu ra máu, protein niệu, phù nề (đặc biệt mặt). Có thể cấp tính (sau nhiễm trùng) hoặc mạn tính. Chẩn đoán xác định bằng sinh thiết thận. Điều trị bằng corticoid và thuốc ức chế miễn dịch. Nếu không điều trị có thể dẫn đến suy thận mạn.",
        "context": "신장내과",
        "culturalNote": "한국은 신생검 접근성 좋아 정확한 진단 가능하나 베트남은 시행 어려움. 한국은 면역억제제 사용 적극적이나 베트남은 보수적. 통역 시 감염 후 발생 가능(특히 편도염 후)함을 설명하고 조기 치료 중요성 강조.",
        "commonMistakes": [
            {
                "mistake": "viêm cầu thận = viêm bể thận",
                "correction": "cầu thận (사구체) ≠ bể thận (신우)",
                "explanation": "신우신염과 다른 질환"
            },
            {
                "mistake": "máu trong nước tiểu = ung thư",
                "correction": "có nhiều nguyên nhân gây hematuria",
                "explanation": "혈뇨는 다양한 원인 가능"
            },
            {
                "mistake": "cấp = không nghiêm trọng",
                "correction": "cấp tính cũng cần điều trị tích cực",
                "explanation": "급성도 적극 치료 필요"
            }
        ],
        "examples": [
            {
                "ko": "소변에 피가 나오고 얼굴이 붓는 것은 사구체신염 의심됩니다.",
                "vi": "Tiểu ra máu và phù mặt nghi ngờ viêm cầu thận.",
                "situation": "formal"
            },
            {
                "ko": "편도염 앓고 나서 2주 후에 나타나는 경우가 많습니다.",
                "vi": "Thường xuất hiện 2 tuần sau khi bị viêm amidan.",
                "situation": "onsite"
            },
            {
                "ko": "신생검으로 정확한 유형을 알아야 적절한 치료를 할 수 있습니다.",
                "vi": "Phải sinh thiết thận để biết chính xác loại viêm mới điều trị đúng được.",
                "situation": "formal"
            }
        ],
        "relatedTerms": ["혈뇨", "단백뇨", "신증후군", "신생검"]
    },
    {
        "slug": "roi-loan-dien-giai",
        "korean": "전해질불균형",
        "vietnamese": "Rối loạn điện giải",
        "hanja": "電解質不均衡",
        "hanjaReading": "電(번개 전) + 解(풀 해) + 質(바탕 질) + 不(아니 부) + 均(고를 균) + 衡(저울 형)",
        "pronunciation": "전해질불균형",
        "meaningKo": "체내 나트륨, 칼륨, 칼슘 등의 전해질이 정상 범위를 벗어난 상태. 통역 시 각 전해질별 증상 구분 - 저나트륨(hạ natri): 의식변화, 고칼륨(tăng kali): 부정맥. 탈수, 구토, 설사가 흔한 원인. 수액 치료 시 천천히 교정 필요(급격한 교정은 위험). 약물 부작용으로도 발생 가능.",
        "meaningVi": "Mất cân bằng các chất điện giải như natri, kali, canxi trong máu. Nguyên nhân do mất nước, nôn mửa, tiêu chảy, thuốc lợi tiểu. Triệu chứng gồm mệt mỏi, co giật, rối loạn nhịp tim. Điều trị bằng truyền dịch điều chỉnh điện giải, cần làm từ từ để tránh biến chứng. Xét nghiệm máu để theo dõi.",
        "context": "응급실, 내과",
        "culturalNote": "한국은 응급실에서 전해질 검사 즉시 가능하나 베트남은 검사 시간 오래 걸림. 한국은 경구수액(ORS) 보급 잘 되어 있으나 베트남은 정맥 수액 선호. 통역 시 경구수액 가능한 경우와 정맥 수액 필수인 경우 구분 설명.",
        "commonMistakes": [
            {
                "mistake": "điện giải = glucose",
                "correction": "điện giải (전해질) ≠ đường huyết (혈당)",
                "explanation": "전해질과 혈당은 다른 검사"
            },
            {
                "mistake": "uống nhiều nước = đủ",
                "correction": "cần nước có điện giải (ORS)",
                "explanation": "순수한 물만으로는 전해질 보충 안 됨"
            },
            {
                "mistake": "điều chỉnh nhanh càng tốt",
                "correction": "phải điều chỉnh từ từ",
                "explanation": "급격한 교정은 뇌부종 등 위험"
            }
        ],
        "examples": [
            {
                "ko": "설사가 심해서 저나트륨혈증이 생겼습니다.",
                "vi": "Tiêu chảy nặng nên bị hạ natri máu.",
                "situation": "formal"
            },
            {
                "ko": "칼륨 수치가 너무 높아서 부정맥 위험이 있습니다.",
                "vi": "Kali quá cao nên có nguy cơ rối loạn nhịp tim.",
                "situation": "onsite"
            },
            {
                "ko": "전해질 수액을 천천히 투여하겠습니다.",
                "vi": "Sẽ truyền dịch điện giải từ từ.",
                "situation": "formal"
            }
        ],
        "relatedTerms": ["탈수", "저나트륨혈증", "고칼륨혈증", "수액치료"]
    },
    {
        "slug": "ghep-than",
        "korean": "신장이식",
        "vietnamese": "Ghép thận",
        "hanja": "腎臟移植",
        "hanjaReading": "腎(콩팥 신) + 臟(장부 장) + 移(옮길 이) + 植(심을 식)",
        "pronunciation": "신장이식",
        "meaningKo": "만성신부전 환자에게 건강한 신장을 이식하는 수술. 통역 시 '생체이식(ghép từ người sống)'과 '뇌사이식(ghép từ người chết não)' 구분. 면역억제제는 평생 복용 필수 - 'thuốc chống thải ghép'. 거부반응은 'phản ứng thải ghép'. 이식 후에도 정기 검진과 감염 주의 필수.",
        "meaningVi": "Phẫu thuật cấy thận khỏe mạnh cho người suy thận mạn giai đoạn cuối. Có thể ghép từ người thân còn sống hoặc người chết não. Sau ghép phải uống thuốc chống thải ghép suốt đời. Cần theo dõi chức năng thận ghép định kỳ và tránh nhiễm trùng. Thành công cao hơn lọc máu về chất lượng sống.",
        "context": "신장내과, 이식외과",
        "culturalNote": "한국은 이식 시스템 잘 구축되었으나 베트남은 뇌사 기증 문화 부족. 한국은 면역억제제 보험 적용되나 베트남은 약값 부담. 통역 시 생체 기증자의 위험성(한 개 신장으로 살기)과 장기 대기 시간 설명.",
        "commonMistakes": [
            {
                "mistake": "ghép thận = khỏi hẳn bệnh",
                "correction": "cần uống thuốc và theo dõi suốt đời",
                "explanation": "이식 후에도 평생 관리 필요"
            },
            {
                "mistake": "ngừng thuốc khi thấy khỏe",
                "correction": "tuyệt đối không được ngừng thuốc chống thải ghép",
                "explanation": "면역억제제 중단 시 급성 거부반응"
            },
            {
                "mistake": "ghép xong = không cần lọc máu nữa",
                "correction": "đúng, nếu thận ghép hoạt động tốt",
                "explanation": "이식 성공 시 투석 중단 가능"
            }
        ],
        "examples": [
            {
                "ko": "어머니가 신장을 기증하셔서 생체이식 수술을 하겠습니다.",
                "vi": "Mẹ hiến thận nên sẽ làm phẫu thuật ghép từ người sống.",
                "situation": "formal"
            },
            {
                "ko": "이식 후 면역억제제를 절대 임의로 중단하면 안 됩니다.",
                "vi": "Sau ghép tuyệt đối không được tự ý ngừng thuốc chống thải ghép.",
                "situation": "onsite"
            },
            {
                "ko": "이식 받으면 투석에서 벗어날 수 있습니다.",
                "vi": "Nếu ghép thận có thể thoát khỏi lọc máu.",
                "situation": "informal"
            }
        ],
        "relatedTerms": ["만성신부전", "면역억제제", "거부반응", "생체기증"]
    }
]

# 중복 제거 및 추가
print("기존 용어 수:", len(data))
print("기존 slug:", existing_slugs)

new_count = 0
for term in new_terms:
    if term['slug'] not in existing_slugs:
        data.append(term)
        existing_slugs.add(term['slug'])
        new_count += 1
        print(f"✅ 추가: {term['slug']} - {term['korean']}")
    else:
        print(f"⏭️  중복 스킵: {term['slug']}")

# 저장
with open(file_path, 'w', encoding='utf-8') as f:
    json.dump(data, f, ensure_ascii=False, indent=2)

print(f"\n{'='*60}")
print(f"✅ 완료: {new_count}개 용어 추가")
print(f"📊 총 용어 수: {len(data)}개")
print(f"📁 저장 위치: {file_path}")
print(f"{'='*60}")
