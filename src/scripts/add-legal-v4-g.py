#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
선거법/정당법 용어 추가 스크립트 (Election/Political Party Law Terms)
Tier S 품질 기준 준수 (90점 이상)
"""

import json
import os

# 파일 경로 설정
file_path = os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', 'data', 'terms', 'legal.json')

# 추가할 용어 데이터 (10개)
new_terms = [
    {
        "slug": "bau-cu",
        "korean": "선거",
        "vietnamese": "Bầu cử",
        "hanja": "選擧",
        "hanjaReading": "選(가릴 선) + 擧(들 거)",
        "pronunciation": "바우 꾸",
        "meaningKo": "국민이나 조직의 구성원이 대표자를 투표로 뽑는 제도입니다. 베트남의 국회의원 선거는 5년마다 실시되며, 한국은 대통령 5년, 국회의원 4년 임기로 선거를 진행합니다. 통역 시 주의할 점은 베트남의 선거 제도는 공산당의 주도 하에 조국전선(Mặt trận Tổ quốc)이 후보를 추천하는 구조이므로, 한국의 다당제 경쟁 선거와 근본적으로 다르다는 점을 인지해야 합니다. '자유선거', '경쟁선거' 등의 개념을 통역할 때는 맥락을 명확히 전달해야 오해를 방지할 수 있습니다.",
        "meaningVi": "Bầu cử là quá trình mà công dân hoặc thành viên của một tổ chức bỏ phiếu để lựa chọn người đại diện. Ở Việt Nam, bầu cử Quốc hội diễn ra 5 năm một lần, trong khi Hàn Quốc có nhiều loại bầu cử khác nhau (Tổng thống 5 năm, Quốc hội 4 năm). Hệ thống bầu cử Việt Nam có sự lãnh đạo của Đảng Cộng sản và Mặt trận Tổ quốc đề cử ứng cử viên.",
        "context": "법률, 정치, 행정",
        "culturalNote": "한국은 다당제 민주주의 국가로 대통령제와 국회의원 선거가 경쟁적으로 이루어지지만, 베트남은 공산당 일당 체제 하에서 조국전선이 후보를 추천하고 국회가 승인하는 구조입니다. 따라서 '자유선거', '보통선거', '직접선거' 등의 개념이 양국에서 다르게 이해될 수 있으므로 통역 시 정치 체제의 차이를 명확히 인지하고 전달해야 합니다.",
        "commonMistakes": [
            {
                "mistake": "'Bầu cử tự do'를 한국식 자유선거로만 이해",
                "correction": "베트남의 맥락에서는 조국전선 추천 후보 중 선택하는 구조임을 설명",
                "explanation": "베트남의 선거 제도는 공산당 주도 하에 이루어지므로 한국의 다당제 경쟁 선거와 구조가 다름"
            },
            {
                "mistake": "'선거'를 단순히 'bầu'로만 번역",
                "correction": "'bầu cử'로 정확히 표현",
                "explanation": "'bầu'는 '뽑다'는 동사이고, 'bầu cử'가 선거 제도 전체를 의미하는 명사"
            },
            {
                "mistake": "한국의 대통령 선거를 'bầu Tổng thống'으로만 번역",
                "correction": "'bầu cử Tổng thống' 또는 'cuộc bầu cử Tổng thống'으로 표현",
                "explanation": "명사구로 표현하는 것이 공식 문서나 뉴스에서 더 자연스러움"
            }
        ],
        "examples": [
            {
                "ko": "다음 달에 국회의원 선거가 실시됩니다.",
                "vi": "Tháng sau sẽ diễn ra cuộc bầu cử Quốc hội.",
                "situation": "formal"
            },
            {
                "ko": "이번 선거에서 투표율이 75%를 기록했습니다.",
                "vi": "Cuộc bầu cử này đạt tỷ lệ cử tri đi bỏ phiếu là 75%.",
                "situation": "formal"
            },
            {
                "ko": "선거 유세 기간에는 후보자들이 공약을 발표합니다.",
                "vi": "Trong thời gian vận động tranh cử, các ứng cử viên công bố cam kết của mình.",
                "situation": "onsite"
            }
        ],
        "relatedTerms": ["ung-cu-vien", "cu-tri", "phieu-bau", "kiem-phieu"]
    },
    {
        "slug": "ung-cu-vien",
        "korean": "후보자",
        "vietnamese": "Ứng cử viên",
        "hanja": "候補者",
        "hanjaReading": "候(기다릴 후) + 補(도울 보) + 者(사람 자)",
        "pronunciation": "응 꾸 비엔",
        "meaningKo": "선거에서 당선되기 위해 출마한 사람을 의미합니다. 한국에서는 정당 공천을 받거나 무소속으로 출마할 수 있으며, 베트남에서는 조국전선(Mặt trận Tổ quốc)의 추천을 받은 후보가 국회의원 선거에 출마합니다. 통역 시 주의할 점은 한국의 경우 여러 정당에서 다양한 후보가 경쟁하지만, 베트남은 조국전선이 추천한 후보 중에서 선택하는 구조이므로 '경쟁 후보', '야당 후보' 등의 표현이 베트남 맥락에서는 다르게 이해될 수 있습니다.",
        "meaningVi": "Ứng cử viên là người ra ứng cử trong một cuộc bầu cử để được bầu vào một chức vụ. Ở Hàn Quốc, ứng cử viên có thể được đề cử bởi các đảng chính trị hoặc tranh cử độc lập, trong khi ở Việt Nam, ứng cử viên Quốc hội được Mặt trận Tổ quốc đề cử sau khi được sự đồng ý của Đảng Cộng sản.",
        "context": "법률, 정치, 선거",
        "culturalNote": "한국에서는 후보자가 정당에 소속되거나 무소속으로 자유롭게 출마할 수 있으며, TV 토론, 유세 등을 통해 경쟁합니다. 반면 베트남에서는 조국전선이 후보를 추천하고, 국회가 승인하는 절차를 거치므로 후보자의 출마 과정이 한국과 크게 다릅니다. 통역 시 '야당 후보', '여당 후보', '독립 후보' 등의 개념이 베트남에서는 적용되지 않음을 유의해야 합니다.",
        "commonMistakes": [
            {
                "mistake": "'후보자'를 단순히 'người ứng cử'로만 번역",
                "correction": "'ứng cử viên'으로 정확히 표현",
                "explanation": "'ứng cử viên'이 공식적이고 법적인 용어로 더 적합함"
            },
            {
                "mistake": "한국의 '야당 후보'를 'ứng cử viên đối lập'으로 직역",
                "correction": "베트남 맥락에서는 조국전선 추천 후보만 존재하므로, 한국의 정치 구조 설명 필요",
                "explanation": "베트남에는 야당 개념이 없으므로 직역하면 오해 발생"
            },
            {
                "mistake": "'무소속 후보'를 'ứng cử viên độc lập'으로만 번역",
                "correction": "'ứng cử viên không thuộc đảng phái'로 설명 추가",
                "explanation": "베트남에서는 모든 후보가 조국전선 추천을 받으므로 '독립' 개념이 다름"
            }
        ],
        "examples": [
            {
                "ko": "이번 선거에는 총 5명의 후보자가 출마했습니다.",
                "vi": "Cuộc bầu cử này có tổng cộng 5 ứng cử viên ra tranh cử.",
                "situation": "formal"
            },
            {
                "ko": "후보자는 선거 유세에서 공약을 발표했습니다.",
                "vi": "Ứng cử viên đã công bố cam kết trong chiến dịch vận động tranh cử.",
                "situation": "onsite"
            },
            {
                "ko": "후보자 등록 마감일은 다음 주입니다.",
                "vi": "Hạn chót đăng ký ứng cử viên là tuần sau.",
                "situation": "formal"
            }
        ],
        "relatedTerms": ["bau-cu", "cu-tri", "don-vi-bau-cu", "phieu-bau"]
    },
    {
        "slug": "cu-tri",
        "korean": "유권자",
        "vietnamese": "Cử tri",
        "hanja": "有權者",
        "hanjaReading": "有(있을 유) + 權(권세 권) + 者(사람 자)",
        "pronunciation": "꾸 찌",
        "meaningKo": "선거에서 투표할 권리를 가진 사람을 의미합니다. 한국에서는 만 18세 이상의 국민이 유권자이며, 베트남도 만 18세 이상 국민에게 선거권이 부여됩니다. 통역 시 주의할 점은 양국 모두 연령 제한이 비슷하지만, 한국의 경우 재외국민도 투표할 수 있는 제도가 있으며, 베트남은 국내 거주자 중심으로 선거가 이루어진다는 점입니다. 또한 '유권자 명부', '선거인단' 등의 표현은 법적 맥락에서 정확히 구분해야 합니다.",
        "meaningVi": "Cử tri là người có quyền bỏ phiếu trong một cuộc bầu cử. Ở cả Hàn Quốc và Việt Nam, công dân từ 18 tuổi trở lên đều có quyền bầu cử. Hàn Quốc có hệ thống bỏ phiếu cho công dân ở nước ngoài, trong khi Việt Nam tập trung vào cử tri trong nước. Cử tri có trách nhiệm bỏ phiếu và tham gia vào quá trình dân chủ.",
        "context": "법률, 정치, 선거",
        "culturalNote": "한국에서는 재외국민 투표, 사전투표, 부재자투표 등 다양한 투표 방식이 있어 유권자의 투표 접근성이 높습니다. 베트남은 주로 거주지 기반 투표가 이루어지며, 조국전선이 추천한 후보 중에서 선택하는 구조입니다. 통역 시 '유권자 명부', '투표권', '선거인단' 등의 표현은 법적 정확성을 유지하며, 양국의 선거 제도 차이를 명확히 전달해야 합니다.",
        "commonMistakes": [
            {
                "mistake": "'유권자'를 'người có quyền bỏ phiếu'로 풀어서 번역",
                "correction": "'cử tri'로 간결하게 표현",
                "explanation": "'cử tri'가 법적으로 정확한 용어이며 공식 문서에서 사용됨"
            },
            {
                "mistake": "'유권자 명부'를 'danh sách cử tri'로만 번역",
                "correction": "'danh sách cử tri' 또는 'danh bộ cử tri'로 표현",
                "explanation": "공식 문서에서는 'danh bộ'가 사용되기도 함"
            },
            {
                "mistake": "'선거인단'과 '유권자'를 혼동하여 모두 'cử tri'로 번역",
                "correction": "'선거인단'은 'đoàn cử tri' 또는 'hội đồng bầu cử'로 구분",
                "explanation": "선거인단은 특정 역할을 가진 집단이므로 유권자와 구분 필요"
            }
        ],
        "examples": [
            {
                "ko": "이번 선거의 유권자는 약 4천만 명입니다.",
                "vi": "Cuộc bầu cử này có khoảng 40 triệu cử tri.",
                "situation": "formal"
            },
            {
                "ko": "유권자는 투표소에서 신분증을 제시해야 합니다.",
                "vi": "Cử tri phải xuất trình chứng minh nhân dân tại điểm bỏ phiếu.",
                "situation": "onsite"
            },
            {
                "ko": "유권자 등록은 온라인으로도 가능합니다.",
                "vi": "Đăng ký cử tri cũng có thể thực hiện trực tuyến.",
                "situation": "informal"
            }
        ],
        "relatedTerms": ["bau-cu", "phieu-bau", "don-vi-bau-cu", "ung-cu-vien"]
    },
    {
        "slug": "don-vi-bau-cu",
        "korean": "선거구",
        "vietnamese": "Đơn vị bầu cử",
        "hanja": "選擧區",
        "hanjaReading": "選(가릴 선) + 擧(들 거) + 區(구역 구)",
        "pronunciation": "던 비 바우 꾸",
        "meaningKo": "선거를 실시하는 지역적 단위를 의미합니다. 한국에서는 지역구와 비례대표로 나뉘며, 지역구는 국회의원 1명을 선출하는 '소선거구제'를 채택하고 있습니다. 베트남은 각 성(tỉnh)이나 중앙직할시(thành phố trực thuộc trung ương)가 선거구 단위가 되며, 인구에 따라 국회의원 정원이 배정됩니다. 통역 시 주의할 점은 '지역구'와 '선거구'의 차이를 명확히 하고, 베트남의 선거구는 행정구역 기반이므로 한국의 게리맨더링(선거구 조작) 같은 개념이 덜 적용된다는 점을 이해해야 합니다.",
        "meaningVi": "Đơn vị bầu cử là khu vực địa lý được xác định để tổ chức bầu cử và bầu ra đại diện. Ở Hàn Quốc, có hệ thống khu vực bầu cử địa phương và đại diện theo tỷ lệ, trong khi Việt Nam chia đơn vị bầu cử theo tỉnh, thành phố trực thuộc trung ương, và số lượng đại biểu Quốc hội được phân bổ dựa trên dân số.",
        "context": "법률, 정치, 선거, 행정",
        "culturalNote": "한국의 선거구는 인구 변화에 따라 재조정되며, '선거구 획정' 문제가 정치적 쟁점이 되기도 합니다. 베트남은 행정구역 기반으로 선거구가 고정되어 있어 한국처럼 선거구 조정 논란이 적습니다. 통역 시 '지역구', '선거구', '선거구 획정', '게리맨더링' 등의 표현은 한국의 정치 맥락을 정확히 전달해야 하며, 베트남 청중에게는 추가 설명이 필요할 수 있습니다.",
        "commonMistakes": [
            {
                "mistake": "'선거구'를 'khu vực bầu cử'로만 번역",
                "correction": "'đơn vị bầu cử'로 정확히 표현",
                "explanation": "'đơn vị bầu cử'가 법적으로 정확한 용어이며 공식 문서에서 사용됨"
            },
            {
                "mistake": "'지역구'와 '선거구'를 혼동하여 모두 'đơn vị bầu cử'로 번역",
                "correction": "'지역구'는 'khu vực địa phương' 또는 'khu vực đại diện'으로 구분",
                "explanation": "지역구는 비례대표와 대비되는 개념이므로 선거구보다 좁은 의미"
            },
            {
                "mistake": "'선거구 획정'을 'phân chia đơn vị bầu cử'로만 번역",
                "correction": "'phân định đơn vị bầu cử' 또는 'phân chia khu vực bầu cử'로 표현",
                "explanation": "'phân định'이 법적 경계 설정을 더 명확히 표현함"
            }
        ],
        "examples": [
            {
                "ko": "서울시는 49개의 국회의원 선거구로 나뉩니다.",
                "vi": "Thành phố Seoul được chia thành 49 đơn vị bầu cử đại biểu Quốc hội.",
                "situation": "formal"
            },
            {
                "ko": "선거구 획정 위원회가 인구 변화를 반영하여 선거구를 조정했습니다.",
                "vi": "Ủy ban phân định đơn vị bầu cử đã điều chỉnh đơn vị bầu cử để phản ánh sự thay đổi dân số.",
                "situation": "formal"
            },
            {
                "ko": "이 선거구에서는 3명의 후보자가 경쟁하고 있습니다.",
                "vi": "Ở đơn vị bầu cử này, có 3 ứng cử viên đang cạnh tranh.",
                "situation": "onsite"
            }
        ],
        "relatedTerms": ["bau-cu", "cu-tri", "ung-cu-vien", "dai-bieu-quoc-hoi"]
    },
    {
        "slug": "phieu-bau",
        "korean": "투표용지",
        "vietnamese": "Phiếu bầu",
        "hanja": "投票用紙",
        "hanjaReading": "投(던질 투) + 票(표 표) + 用(쓸 용) + 紙(종이 지)",
        "pronunciation": "피에우 바우",
        "meaningKo": "선거에서 유권자가 후보자나 정당을 선택하여 표시하는 종이를 의미합니다. 한국에서는 후보자 이름과 정당이 인쇄된 용지에 도장을 찍는 방식이 일반적이며, 베트남도 유사하게 후보자 목록이 인쇄된 용지에 표시합니다. 통역 시 주의할 점은 '투표용지'와 '투표함', '투표소' 등의 관련 용어를 명확히 구분해야 하며, 전자투표 등 디지털 방식과의 차이도 설명할 수 있어야 합니다. 또한 베트남에서는 조국전선이 추천한 후보 목록이 투표용지에 인쇄되므로, 한국처럼 다수의 정당 후보가 나열되는 것과는 다릅니다.",
        "meaningVi": "Phiếu bầu là tờ giấy mà cử tri sử dụng để đánh dấu lựa chọn ứng cử viên hoặc đảng trong cuộc bầu cử. Ở Hàn Quốc, phiếu bầu thường có tên ứng cử viên và đảng được in sẵn, và cử tri đóng dấu để chọn. Ở Việt Nam, phiếu bầu cũng có danh sách ứng cử viên do Mặt trận Tổ quốc đề cử.",
        "context": "법률, 정치, 선거",
        "culturalNote": "한국의 투표용지는 중앙선거관리위원회가 인쇄하며, 정당 기호와 후보자 이름이 명확히 표기됩니다. 베트남의 투표용지는 조국전선이 추천한 후보 목록이 인쇄되며, 한국처럼 여러 정당이 경쟁하는 구조가 아니므로 투표용지 디자인과 내용이 다릅니다. 통역 시 '무효표', '백지투표', '기권' 등의 개념도 정확히 전달해야 합니다.",
        "commonMistakes": [
            {
                "mistake": "'투표용지'를 'giấy bỏ phiếu'로 번역",
                "correction": "'phiếu bầu' 또는 'lá phiếu'로 표현",
                "explanation": "'phiếu bầu'가 공식적이고 간결한 표현임"
            },
            {
                "mistake": "'무효표'를 'phiếu không hợp lệ'로만 번역",
                "correction": "'phiếu không hợp lệ' 또는 'phiếu bị hủy'로 표현",
                "explanation": "무효표는 법적으로 인정되지 않는 투표이므로 'phiếu bị hủy'가 더 명확"
            },
            {
                "mistake": "'백지투표'를 'phiếu trắng'으로만 번역",
                "correction": "'phiếu trắng' 또는 'phiếu bỏ trống'으로 표현",
                "explanation": "'phiếu bỏ trống'이 의도적으로 빈 투표임을 명확히 함"
            }
        ],
        "examples": [
            {
                "ko": "투표용지는 투표소에서 배부됩니다.",
                "vi": "Phiếu bầu được phát tại điểm bỏ phiếu.",
                "situation": "onsite"
            },
            {
                "ko": "투표용지를 훼손하면 무효표가 됩니다.",
                "vi": "Nếu làm hỏng phiếu bầu, phiếu sẽ bị hủy và không hợp lệ.",
                "situation": "formal"
            },
            {
                "ko": "투표용지에는 후보자 이름과 정당이 인쇄되어 있습니다.",
                "vi": "Phiếu bầu có in sẵn tên ứng cử viên và đảng phái.",
                "situation": "informal"
            }
        ],
        "relatedTerms": ["bau-cu", "cu-tri", "ung-cu-vien", "kiem-phieu"]
    },
    {
        "slug": "kiem-phieu",
        "korean": "개표",
        "vietnamese": "Kiểm phiếu",
        "hanja": "開票",
        "hanjaReading": "開(열 개) + 票(표 표)",
        "pronunciation": "끼엠 피에우",
        "meaningKo": "선거 종료 후 투표함을 열어 투표용지를 세고 집계하는 과정을 의미합니다. 한국에서는 중앙선거관리위원회 주관으로 투표 종료 즉시 개표가 시작되며, 각 정당의 참관인이 투명성을 확보합니다. 베트남도 유사하게 개표 과정에 감시단이 참여하지만, 조국전선이 추천한 후보 중에서 선택하는 구조이므로 개표 과정의 투명성과 경쟁성이 한국과 다릅니다. 통역 시 주의할 점은 '개표', '검표', '집계', '확정' 등의 단계를 명확히 구분하고, 개표 방법(수개표, 전자개표)의 차이도 설명할 수 있어야 합니다.",
        "meaningVi": "Kiểm phiếu là quá trình mở hòm phiếu sau khi bầu cử kết thúc và đếm, tập hợp kết quả bỏ phiếu. Ở Hàn Quốc, Ủy ban Bầu cử Trung ương giám sát quá trình kiểm phiếu với sự tham gia của đại diện các đảng để đảm bảo tính minh bạch. Ở Việt Nam, quá trình kiểm phiếu cũng có sự giám sát của đoàn quan sát.",
        "context": "법률, 정치, 선거",
        "culturalNote": "한국의 개표 과정은 실시간으로 방송되며, 각 정당의 참관인과 시민단체가 투명성을 감시합니다. 베트남의 개표 과정은 조국전선과 선거관리위원회 주도로 이루어지며, 한국만큼 경쟁적인 감시 구조가 아닙니다. 통역 시 '참관인', '감시단', '집계', '확정' 등의 표현은 법적 정확성을 유지하며, 양국의 개표 절차 차이를 명확히 전달해야 합니다.",
        "commonMistakes": [
            {
                "mistake": "'개표'를 'mở phiếu'로 직역",
                "correction": "'kiểm phiếu'로 정확히 표현",
                "explanation": "'kiểm phiếu'가 개표 전체 과정을 의미하는 공식 용어임"
            },
            {
                "mistake": "'검표'와 '개표'를 혼동하여 모두 'kiểm phiếu'로 번역",
                "correction": "'검표'는 'kiểm tra phiếu'로 구분",
                "explanation": "검표는 투표용지의 유효성을 확인하는 과정이고, 개표는 집계 과정 전체"
            },
            {
                "mistake": "'개표 결과'를 'kết quả mở phiếu'로 번역",
                "correction": "'kết quả kiểm phiếu' 또는 'kết quả bầu cử'로 표현",
                "explanation": "'kết quả kiểm phiếu'가 더 공식적이고 정확함"
            }
        ],
        "examples": [
            {
                "ko": "개표 작업은 투표 종료 후 즉시 시작됩니다.",
                "vi": "Công việc kiểm phiếu bắt đầu ngay sau khi bỏ phiếu kết thúc.",
                "situation": "formal"
            },
            {
                "ko": "개표 과정은 모든 정당의 참관인이 지켜봅니다.",
                "vi": "Quá trình kiểm phiếu được giám sát bởi đại diện của tất cả các đảng.",
                "situation": "onsite"
            },
            {
                "ko": "개표 결과는 다음 날 오전에 발표됩니다.",
                "vi": "Kết quả kiểm phiếu sẽ được công bố vào sáng hôm sau.",
                "situation": "formal"
            }
        ],
        "relatedTerms": ["bau-cu", "phieu-bau", "cu-tri", "ung-cu-vien"]
    },
    {
        "slug": "mat-tran-to-quoc",
        "korean": "조국전선",
        "vietnamese": "Mặt trận Tổ quốc",
        "hanja": "祖國戰線",
        "hanjaReading": "祖(조상 조) + 國(나라 국) + 戰(싸울 전) + 線(줄 선)",
        "pronunciation": "맛 쯔언 또 꾸억",
        "meaningKo": "베트남 공산당이 주도하는 대중 조직으로, 각계각층의 인민을 결집하고 국회의원 후보를 추천하는 역할을 합니다. 베트남의 조국전선은 정치·사회 조직들을 포괄하며, 선거에서 후보 추천권을 가지고 있어 사실상 후보자 검증 기능을 수행합니다. 한국에는 이와 직접 대응되는 조직이 없으므로 통역 시 주의가 필요합니다. 통역 시 주의할 점은 조국전선을 단순히 '시민단체' 또는 '사회단체'로 번역하면 안 되며, 베트남 정치 체제에서의 고유한 역할을 설명해야 합니다.",
        "meaningVi": "Mặt trận Tổ quốc Việt Nam là tổ chức chính trị - xã hội của nhân dân Việt Nam, do Đảng Cộng sản Việt Nam lãnh đạo, tập hợp các tầng lớp nhân dân, các đảng phái chính trị, tổ chức chính trị - xã hội, tổ chức xã hội, các lực lượng vũ trang nhân dân và đồng bào các dân tộc trong cả nước. Mặt trận Tổ quốc có vai trò đề cử ứng cử viên trong bầu cử Quốc hội.",
        "context": "법률, 정치, 사회",
        "culturalNote": "베트남의 조국전선은 공산당이 주도하는 대중 조직으로, 한국의 어떤 조직과도 직접 비교하기 어렵습니다. 한국에서는 정당이나 시민단체가 후보를 추천하지만, 베트남에서는 조국전선이 공산당의 지도 하에 후보를 추천하고, 국회가 승인하는 구조입니다. 통역 시 '조국전선'을 단순히 'front' 또는 'alliance'로 번역하면 오해를 줄 수 있으므로, 베트남 정치 체제 내에서의 고유한 역할과 기능을 정확히 전달해야 합니다.",
        "commonMistakes": [
            {
                "mistake": "'조국전선'을 'liên minh tổ quốc'으로 번역",
                "correction": "'Mặt trận Tổ quốc'으로 정확히 표현 (고유명사)",
                "explanation": "'Mặt trận Tổ quốc'은 베트남의 공식 조직 명칭이므로 고유명사로 표기"
            },
            {
                "mistake": "조국전선을 '시민단체' 또는 'tổ chức dân sự'로 설명",
                "correction": "베트남 공산당이 주도하는 정치·사회 조직임을 명확히 설명",
                "explanation": "조국전선은 일반 시민단체가 아니라 정치 체제의 핵심 조직"
            },
            {
                "mistake": "'조국전선 추천 후보'를 'ứng cử viên được liên minh đề cử'로 번역",
                "correction": "'ứng cử viên do Mặt trận Tổ quốc đề cử'로 표현",
                "explanation": "조국전선의 공식 명칭과 역할을 정확히 표현"
            }
        ],
        "examples": [
            {
                "ko": "조국전선은 국회의원 후보를 추천합니다.",
                "vi": "Mặt trận Tổ quốc đề cử ứng cử viên đại biểu Quốc hội.",
                "situation": "formal"
            },
            {
                "ko": "조국전선은 베트남 공산당이 주도하는 대중 조직입니다.",
                "vi": "Mặt trận Tổ quốc là tổ chức quần chúng do Đảng Cộng sản Việt Nam lãnh đạo.",
                "situation": "formal"
            },
            {
                "ko": "조국전선은 각계각층의 의견을 수렴하는 역할을 합니다.",
                "vi": "Mặt trận Tổ quốc có vai trò tập hợp ý kiến của các tầng lớp nhân dân.",
                "situation": "onsite"
            }
        ],
        "relatedTerms": ["bau-cu", "ung-cu-vien", "dai-bieu-quoc-hoi", "cu-tri"]
    },
    {
        "slug": "dai-bieu-quoc-hoi",
        "korean": "국회의원",
        "vietnamese": "Đại biểu Quốc hội",
        "hanja": "國會議員",
        "hanjaReading": "國(나라 국) + 會(모일 회) + 議(의논할 의) + 員(인원 원)",
        "pronunciation": "다이 비에우 꾸억 호이",
        "meaningKo": "국회에서 국민을 대표하여 입법, 예산 심의, 정부 감시 등의 역할을 수행하는 사람을 의미합니다. 한국에서는 국회의원이 지역구와 비례대표로 선출되며, 임기는 4년입니다. 베트남에서는 국회의원(Đại biểu Quốc hội)이 조국전선의 추천을 받아 선출되며, 임기는 5년입니다. 통역 시 주의할 점은 한국의 국회의원은 정당 소속이 명확하고 여야 구분이 있지만, 베트남의 국회의원은 공산당 주도 하에 선출되므로 '여당 의원', '야당 의원' 같은 표현이 적용되지 않습니다.",
        "meaningVi": "Đại biểu Quốc hội là người đại diện cho nhân dân tại Quốc hội, thực hiện vai trò lập pháp, thẩm tra ngân sách, giám sát chính phủ. Ở Việt Nam, đại biểu Quốc hội được bầu thông qua đề cử của Mặt trận Tổ quốc và có nhiệm kỳ 5 năm. Ở Hàn Quốc, nghị sĩ Quốc hội được bầu từ khu vực địa phương và theo tỷ lệ, nhiệm kỳ 4 năm.",
        "context": "법률, 정치, 행정",
        "culturalNote": "한국의 국회의원은 정당 정치 체제 하에서 여당과 야당으로 나뉘며, 정치적 경쟁이 치열합니다. 베트남의 국회의원은 공산당의 지도 하에 조국전선이 추천한 후보 중에서 선출되므로, 한국처럼 여야 대립 구도가 없습니다. 통역 시 '국회의원', '의원', '대표', '대의원' 등의 표현을 구분하고, 양국의 정치 체제 차이를 정확히 전달해야 합니다.",
        "commonMistakes": [
            {
                "mistake": "'국회의원'을 'nghị sĩ'로만 번역",
                "correction": "'đại biểu Quốc hội'로 정확히 표현",
                "explanation": "베트남에서는 'đại biểu Quốc hội'가 공식 용어이며, 'nghị sĩ'는 일반적인 의원을 의미"
            },
            {
                "mistake": "'여당 의원'과 '야당 의원'을 'nghị sĩ đảng cầm quyền', 'nghị sĩ đối lập'으로 직역",
                "correction": "베트남에는 여야 구분이 없으므로, 한국의 정치 구조 설명 필요",
                "explanation": "베트남은 공산당 일당 체제이므로 여야 개념이 없음"
            },
            {
                "mistake": "'의원'을 'thành viên'으로 번역",
                "correction": "'đại biểu' 또는 'nghị sĩ'로 표현",
                "explanation": "'thành viên'은 일반 회원을 의미하고, 국회의원은 'đại biểu' 또는 'nghị sĩ'"
            }
        ],
        "examples": [
            {
                "ko": "국회의원은 4년 임기로 선출됩니다.",
                "vi": "Đại biểu Quốc hội được bầu với nhiệm kỳ 4 năm. (Hàn Quốc)",
                "situation": "formal"
            },
            {
                "ko": "국회의원은 국민을 대표하여 법을 만듭니다.",
                "vi": "Đại biểu Quốc hội đại diện cho nhân dân để làm luật.",
                "situation": "formal"
            },
            {
                "ko": "국회의원은 정부를 감시하는 역할을 합니다.",
                "vi": "Đại biểu Quốc hội có vai trò giám sát chính phủ.",
                "situation": "onsite"
            }
        ],
        "relatedTerms": ["bau-cu", "mat-tran-to-quoc", "nhiem-ky", "don-vi-bau-cu"]
    },
    {
        "slug": "nhiem-ky",
        "korean": "임기",
        "vietnamese": "Nhiệm kỳ",
        "hanja": "任期",
        "hanjaReading": "任(맡길 임) + 期(기약할 기)",
        "pronunciation": "니엠 끼",
        "meaningKo": "선출되거나 임명된 공직자가 그 직책을 수행하는 법정 기간을 의미합니다. 한국에서는 대통령 5년 단임제, 국회의원 4년, 지방자치단체장 4년 임기가 적용됩니다. 베트남에서는 국회의원과 국가주석, 총리 등이 5년 임기를 가지며, 재선이 가능합니다. 통역 시 주의할 점은 한국의 대통령은 단임제이므로 '재선'이 불가능하지만, 베트남의 주요 공직자는 재선이 가능하다는 차이를 명확히 해야 합니다. 또한 '임기 만료', '임기 중', '중임', '연임' 등의 표현도 정확히 구분해야 합니다.",
        "meaningVi": "Nhiệm kỳ là thời gian pháp định mà một công chức được bầu hoặc bổ nhiệm thực hiện chức vụ của mình. Ở Hàn Quốc, Tổng thống có nhiệm kỳ 5 năm và chỉ được phục vụ một nhiệm kỳ, trong khi đại biểu Quốc hội có nhiệm kỳ 4 năm. Ở Việt Nam, đại biểu Quốc hội, Chủ tịch nước, Thủ tướng có nhiệm kỳ 5 năm và có thể tái cử.",
        "context": "법률, 정치, 행정",
        "culturalNote": "한국의 대통령은 5년 단임제로 재선이 불가능하며, 이는 권력 집중을 방지하기 위한 제도입니다. 베트남의 주요 공직자는 재선이 가능하며, 공산당의 지도 하에 장기 집권이 가능한 구조입니다. 통역 시 '단임제', '중임', '연임', '재선' 등의 표현을 정확히 구분하고, 양국의 정치 체제 차이를 명확히 전달해야 합니다.",
        "commonMistakes": [
            {
                "mistake": "'임기'를 'thời hạn'으로 번역",
                "correction": "'nhiệm kỳ'로 정확히 표현",
                "explanation": "'nhiệm kỳ'가 공직자의 법정 기간을 의미하는 공식 용어"
            },
            {
                "mistake": "'중임'과 '연임'을 모두 'tái nhiệm'으로 번역",
                "correction": "'중임'은 'phục vụ nhiều nhiệm kỳ', '연임'은 'tái cử liên tiếp'으로 구분",
                "explanation": "중임은 임기를 여러 번 수행하는 것, 연임은 연속으로 재선되는 것"
            },
            {
                "mistake": "'임기 만료'를 'hết hạn nhiệm kỳ'로 번역",
                "correction": "'hết nhiệm kỳ' 또는 'mãn nhiệm'으로 표현",
                "explanation": "'mãn nhiệm'이 공식적이고 간결한 표현"
            }
        ],
        "examples": [
            {
                "ko": "대통령의 임기는 5년입니다.",
                "vi": "Nhiệm kỳ của Tổng thống là 5 năm.",
                "situation": "formal"
            },
            {
                "ko": "국회의원의 임기는 4년이며, 재선이 가능합니다.",
                "vi": "Nhiệm kỳ của đại biểu Quốc hội là 4 năm và có thể tái cử.",
                "situation": "formal"
            },
            {
                "ko": "그는 임기 중에 많은 개혁을 이루었습니다.",
                "vi": "Ông ấy đã thực hiện nhiều cải cách trong nhiệm kỳ của mình.",
                "situation": "onsite"
            }
        ],
        "relatedTerms": ["dai-bieu-quoc-hoi", "bau-cu", "bai-nhiem", "ung-cu-vien"]
    },
    {
        "slug": "bai-nhiem",
        "korean": "해임/탄핵",
        "vietnamese": "Bãi nhiệm",
        "hanja": "罷免/彈劾",
        "hanjaReading": "罷(그만둘 파) + 免(면할 면) / 彈(탄알 탄) + 劾(다스릴 핵)",
        "pronunciation": "바이 니엠",
        "meaningKo": "공직자가 임기 중에 직책에서 물러나게 하는 법적 절차를 의미합니다. 한국에서는 '해임'은 상급 기관이 하급 공직자를 면직시키는 것이고, '탄핵'은 국회가 대통령이나 고위 공직자를 파면하는 절차입니다. 베트남에서는 'bãi nhiệm'이 국회의 의결로 공직자를 면직시키는 것을 의미하며, 한국의 탄핵과 유사합니다. 통역 시 주의할 점은 '해임', '파면', '탄핵', '사임'을 명확히 구분해야 하며, 한국의 탄핵은 헌법재판소의 최종 결정이 필요하지만, 베트남의 'bãi nhiệm'은 국회 의결로 확정된다는 차이를 이해해야 합니다.",
        "meaningVi": "Bãi nhiệm là thủ tục pháp lý để cách chức một công chức trong thời gian đang tại nhiệm. Ở Việt Nam, bãi nhiệm được thực hiện thông qua nghị quyết của Quốc hội. Ở Hàn Quốc, 'haeime' (해임) là việc cấp trên cách chức cấp dưới, còn 'tanhaek' (탄핵) là thủ tục Quốc hội luận tội và cách chức Tổng thống hoặc quan chức cấp cao, cần có quyết định cuối cùng của Tòa án Hiến pháp.",
        "context": "법률, 정치, 행정",
        "culturalNote": "한국의 탄핵은 국회가 소추하고 헌법재판소가 최종 판단하는 2단계 절차이며, 대통령 탄핵은 국회 재적의원 2/3 이상 찬성이 필요합니다. 베트남의 'bãi nhiệm'은 국회 의결로 확정되며, 공산당의 지도 하에 이루어집니다. 통역 시 '해임', '파면', '탄핵', '사임', '면직' 등의 표현을 정확히 구분하고, 양국의 절차 차이를 명확히 전달해야 합니다.",
        "commonMistakes": [
            {
                "mistake": "'탄핵'을 'luận tội'로만 번역",
                "correction": "'bãi nhiệm' 또는 'luận tội và cách chức'로 표현",
                "explanation": "'luận tội'는 탄핵 절차의 일부이고, 'bãi nhiệm'이 최종 결과"
            },
            {
                "mistake": "'해임'과 '탄핵'을 모두 'bãi nhiệm'으로 번역",
                "correction": "'해임'은 'cách chức', '탄핵'은 'bãi nhiệm' 또는 'luận tội'로 구분",
                "explanation": "해임은 상급 기관의 조치이고, 탄핵은 국회의 절차"
            },
            {
                "mistake": "'사임'과 '해임'을 혼동하여 모두 'từ chức'로 번역",
                "correction": "'사임'은 'từ chức', '해임'은 'cách chức' 또는 'bãi nhiệm'으로 구분",
                "explanation": "사임은 자발적 퇴임, 해임은 강제 면직"
            }
        ],
        "examples": [
            {
                "ko": "국회는 대통령 탄핵안을 의결했습니다.",
                "vi": "Quốc hội đã thông qua nghị quyết luận tội Tổng thống.",
                "situation": "formal"
            },
            {
                "ko": "장관이 직무 유기로 해임되었습니다.",
                "vi": "Bộ trưởng bị cách chức vì bỏ bê nhiệm vụ.",
                "situation": "formal"
            },
            {
                "ko": "탄핵 절차는 헌법재판소의 최종 결정이 필요합니다.",
                "vi": "Thủ tục luận tội cần có quyết định cuối cùng của Tòa án Hiến pháp. (Hàn Quốc)",
                "situation": "onsite"
            }
        ],
        "relatedTerms": ["dai-bieu-quoc-hoi", "nhiem-ky", "bau-cu", "mat-tran-to-quoc"]
    }
]

def main():
    """메인 실행 함수"""

    # 1. 기존 파일 읽기
    print(f"📂 파일 읽기: {file_path}")
    with open(file_path, 'r', encoding='utf-8') as f:
        data = json.load(f)

    # data는 리스트여야 함
    if not isinstance(data, list):
        raise ValueError("legal.json의 데이터는 리스트 형식이어야 합니다.")

    print(f"✅ 기존 용어 수: {len(data)}개")

    # 2. 중복 제거 (slug 기준)
    existing_slugs = {term['slug'] for term in data}
    print(f"🔍 기존 slug 목록: {existing_slugs}")

    new_terms_filtered = [term for term in new_terms if term['slug'] not in existing_slugs]
    duplicates = [term['slug'] for term in new_terms if term['slug'] in existing_slugs]

    if duplicates:
        print(f"⚠️  중복 제거된 용어: {duplicates}")

    # 3. 새 용어 추가
    if new_terms_filtered:
        data.extend(new_terms_filtered)
        print(f"➕ 추가된 용어 수: {len(new_terms_filtered)}개")

        # 4. 파일 저장
        with open(file_path, 'w', encoding='utf-8') as f:
            json.dump(data, f, ensure_ascii=False, indent=2)

        print(f"💾 저장 완료: {file_path}")
        print(f"📊 최종 용어 수: {len(data)}개")

        # 추가된 용어 출력
        print("\n✨ 추가된 용어:")
        for term in new_terms_filtered:
            print(f"  - {term['korean']} ({term['slug']})")
    else:
        print("ℹ️  추가할 새 용어가 없습니다 (모두 중복).")

if __name__ == "__main__":
    main()
