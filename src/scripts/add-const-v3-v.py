#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Construction Terms - Building Code & Permits (건축법규/인허가)
Theme: 건축허가, 건폐율, 용적률, 일조권, 건축선, 인접대지, 방화구획, 피난계단, 장애인편의시설, 건축물대장
Tier S quality standard (90+ points)
"""

import json
import os

# 10 terms: Building Code & Permits
data = [
    {
        "slug": "giay-phep-xay-dung",
        "korean": "건축허가",
        "vietnamese": "Giấy phép xây dựng",
        "hanja": "建築許可",
        "hanjaReading": "建(집 건) + 築(쌓을 축) + 許(허락할 허) + 可(옳을 가)",
        "pronunciation": "건추커까",
        "meaningKo": "건축물을 신축·증축·개축·재축하거나 대수선하려는 자가 관할 관청으로부터 받는 법적 승인. 통역 시 주의사항: 한국은 건축허가 신청 후 평균 30~60일 소요되며, 베트남은 지역에 따라 더 긴 경우가 많습니다. '착공신고', '사용승인' 등 단계별 절차가 다르므로 정확히 구분해야 합니다. 베트남에서는 중앙정부 허가와 지방정부 허가가 혼재되어 있어 통역 시 어느 레벨의 허가인지 명확히 해야 합니다.",
        "meaningVi": "Giấy phép xây dựng là sự chấp thuận của cơ quan có thẩm quyền để xây mới, mở rộng, cải tạo hoặc đại tu công trình. Ở Hàn Quốc, thời gian xét duyệt trung bình 30-60 ngày, trong khi Việt Nam có thể kéo dài hơn tùy khu vực. Cần phân biệt các giai đoạn như 'báo cáo khởi công', 'nghiệm thu đưa vào sử dụng'.",
        "context": "formal",
        "culturalNote": "한국은 건축허가, 착공신고, 사용승인의 3단계가 명확히 구분되며 온라인 민원24로 진행 상황을 실시간 추적할 수 있습니다. 베트남은 지방정부 재량이 크고, 인허가 과정에서 면대면 협의가 중요하며, 중앙과 지방의 권한 분배가 한국과 다릅니다. 통역 시 'giấy phép xây dựng'와 '건축허가'의 법적 효력 범위 차이를 설명해야 합니다.",
        "commonMistakes": [
            {
                "mistake": "건축신고를 건축허가로 번역",
                "correction": "건축신고는 'Báo cáo xây dựng', 건축허가는 'Giấy phép xây dựng'",
                "explanation": "신고는 일정 규모 이하 건축물에 적용되며 허가보다 간소화된 절차입니다."
            },
            {
                "mistake": "'착공신고'를 허가의 일부로 설명",
                "correction": "착공신고는 허가 취득 후 별도 단계",
                "explanation": "한국은 허가→착공신고→사용승인 순서이며, 베트남은 절차가 다를 수 있습니다."
            },
            {
                "mistake": "온라인 허가 신청 가능 여부를 양국 동일하게 설명",
                "correction": "한국은 온라인 가능, 베트남은 지역별 다름",
                "explanation": "베트남은 온라인 시스템이 발전 중이나 아직 오프라인 병행이 많습니다."
            }
        ],
        "examples": [
            {
                "ko": "이 프로젝트는 건축허가를 받는 데 90일이 소요될 예정입니다.",
                "vi": "Dự án này dự kiến mất 90 ngày để được cấp giấy phép xây dựng.",
                "situation": "formal"
            },
            {
                "ko": "건축허가 없이 시공하면 이행강제금이 부과됩니다.",
                "vi": "Nếu thi công không có giấy phép xây dựng, sẽ bị phạt tiền cưỡng chế.",
                "situation": "onsite"
            },
            {
                "ko": "허가 도면과 실제 시공이 다르면 준공검사를 통과할 수 없습니다.",
                "vi": "Nếu bản vẽ được phê duyệt khác với thi công thực tế, không thể qua nghiệm thu hoàn công.",
                "situation": "formal"
            }
        ],
        "relatedTerms": ["착공신고", "사용승인", "건축신고", "변경허가"]
    },
    {
        "slug": "ty-le-xay-dung",
        "korean": "건폐율",
        "vietnamese": "Tỷ lệ xây dựng",
        "hanja": "建蔽率",
        "hanjaReading": "建(집 건) + 蔽(가릴 폐) + 率(비율 률)",
        "pronunciation": "건페율",
        "meaningKo": "대지면적에 대한 건축면적(건물이 땅을 덮는 면적)의 비율로, 법적 상한선이 정해져 있습니다. 통역 시 주의사항: 한국은 용도지역별로 건폐율이 명확히 규정되어 있으며(예: 주거지역 50~70%), 베트남은 'tỷ lệ xây dựng' 개념이 유사하나 계산 방식이 다를 수 있습니다. 건폐율 위반 시 인허가 불가 또는 철거 명령이 나올 수 있으므로 통역 시 법적 강제력을 강조해야 합니다.",
        "meaningVi": "Tỷ lệ xây dựng là tỷ lệ giữa diện tích xây dựng (diện tích công trình chiếm trên mặt đất) và diện tích khu đất. Ở Hàn Quốc, tỷ lệ này được quy định nghiêm ngặt theo khu chức năng (ví dụ: 50-70% tại khu dân cư). Vi phạm có thể dẫn đến từ chối cấp phép hoặc lệnh phá dỡ.",
        "context": "formal",
        "culturalNote": "한국은 국토계획법상 용도지역별 건폐율이 법으로 정해져 있으며, 위반 시 행정처분이 엄격합니다. 베트남은 지방정부 조례에 따라 건폐율 기준이 다를 수 있고, 한국보다 유연하게 적용되는 경우가 있습니다. 통역 시 'tỷ lệ xây dựng'와 '건폐율'의 법적 구속력 차이를 명확히 해야 합니다.",
        "commonMistakes": [
            {
                "mistake": "건폐율과 용적률을 혼동",
                "correction": "건폐율은 수평 면적, 용적률은 수직 면적(연면적)",
                "explanation": "건폐율은 땅을 얼마나 덮는지, 용적률은 얼마나 높게 짓는지를 의미합니다."
            },
            {
                "mistake": "'건축면적'을 '연면적'으로 번역",
                "correction": "건축면적은 'diện tích xây dựng', 연면적은 'diện tích sàn'",
                "explanation": "건폐율은 건축면적 기준, 용적률은 연면적 기준입니다."
            },
            {
                "mistake": "건폐율 위반 시 단순 과태료만 언급",
                "correction": "이행강제금 부과, 사용승인 불가, 철거 명령 가능",
                "explanation": "한국에서는 건폐율 위반이 중대한 법적 문제입니다."
            }
        ],
        "examples": [
            {
                "ko": "이 대지의 건폐율은 60%이므로 300평 중 180평까지만 건축할 수 있습니다.",
                "vi": "Tỷ lệ xây dựng của khu đất này là 60%, nên chỉ được xây 180 bình trong tổng số 300 bình.",
                "situation": "formal"
            },
            {
                "ko": "건폐율을 초과하면 건축허가가 나지 않습니다.",
                "vi": "Nếu vượt quá tỷ lệ xây dựng, sẽ không được cấp giấy phép xây dựng.",
                "situation": "onsite"
            },
            {
                "ko": "이 지역은 주거지역이라 건폐율이 50%로 제한됩니다.",
                "vi": "Khu vực này là khu dân cư nên tỷ lệ xây dựng giới hạn 50%.",
                "situation": "formal"
            }
        ],
        "relatedTerms": ["용적률", "대지면적", "건축면적", "용도지역"]
    },
    {
        "slug": "ty-le-dien-tich-san",
        "korean": "용적률",
        "vietnamese": "Tỷ lệ diện tích sàn",
        "hanja": "容積率",
        "hanjaReading": "容(담을 용) + 積(쌓을 적) + 率(비율 률)",
        "pronunciation": "용저뮬",
        "meaningKo": "대지면적에 대한 연면적(모든 층의 바닥면적 합계)의 비율로, 건물의 높이와 규모를 제한하는 지표입니다. 통역 시 주의사항: 한국은 용도지역별로 용적률 상한이 법으로 정해져 있으며(예: 일반주거지역 200~300%), 베트남은 'tỷ lệ diện tích sàn' 개념이 있으나 계산 방식과 법적 강제력이 다를 수 있습니다. 용적률은 개발 수익성과 직결되므로 부동산 개발 통역 시 매우 중요합니다.",
        "meaningVi": "Tỷ lệ diện tích sàn là tỷ lệ giữa tổng diện tích sàn các tầng và diện tích khu đất. Ở Hàn Quốc, tỷ lệ này được quy định chặt chẽ theo khu chức năng (ví dụ: 200-300% tại khu dân cư thông thường). Tỷ lệ này ảnh hưởng trực tiếp đến khả năng sinh lời của dự án phát triển.",
        "context": "formal",
        "culturalNote": "한국은 용적률이 도시 밀도 관리의 핵심 수단이며, 용도지역제와 결합되어 엄격히 적용됩니다. 베트남은 층수 제한으로 용적률을 간접 관리하는 경우가 많고, 한국처럼 용적률 자체를 직접 규제하지 않는 지역도 있습니다. 통역 시 양국의 규제 방식 차이를 설명해야 합니다.",
        "commonMistakes": [
            {
                "mistake": "용적률을 단순히 '층수'로 설명",
                "correction": "용적률은 연면적 기준, 층수는 그 결과물",
                "explanation": "같은 용적률이어도 저층 넓게 또는 고층 좁게 지을 수 있습니다."
            },
            {
                "mistake": "'연면적'을 'diện tích xây dựng'로 번역",
                "correction": "연면적은 'tổng diện tích sàn', 건축면적은 'diện tích xây dựng'",
                "explanation": "용적률은 모든 층의 바닥면적 합계가 기준입니다."
            },
            {
                "mistake": "용적률 인센티브 제도를 양국 동일하게 설명",
                "correction": "한국은 공개공지 제공 시 용적률 완화, 베트남은 다름",
                "explanation": "각국의 인센티브 제도가 다르므로 명확히 구분해야 합니다."
            }
        ],
        "examples": [
            {
                "ko": "이 부지는 용적률 250%로 1000㎡ 대지에 2500㎡까지 지을 수 있습니다.",
                "vi": "Khu đất này có tỷ lệ diện tích sàn 250%, nên có thể xây 2500㎡ trên mặt bằng 1000㎡.",
                "situation": "formal"
            },
            {
                "ko": "용적률을 초과하면 위법 건축물로 철거 대상이 됩니다.",
                "vi": "Nếu vượt quá tỷ lệ diện tích sàn, công trình vi phạm pháp luật và có thể bị phá dỡ.",
                "situation": "onsite"
            },
            {
                "ko": "이 지역은 준주거지역이라 용적률이 400%까지 가능합니다.",
                "vi": "Khu vực này là khu cận dân cư nên tỷ lệ diện tích sàn có thể lên đến 400%.",
                "situation": "formal"
            }
        ],
        "relatedTerms": ["건폐율", "연면적", "용도지역", "공개공지"]
    },
    {
        "slug": "quyen-giu-anh-nang",
        "korean": "일조권",
        "vietnamese": "Quyền giữ ánh nắng",
        "hanja": "日照權",
        "hanjaReading": "日(날 일) + 照(비출 조) + 權(권리 권)",
        "pronunciation": "일쪼꿘",
        "meaningKo": "건축물이 햇빛을 받을 수 있는 권리로, 인접 건물이 일조를 방해하지 않도록 법으로 보호됩니다. 통역 시 주의사항: 한국은 건축법과 주택법에서 일조권 기준(예: 동지 기준 9시~15시 사이 최소 2시간 일조 확보)을 명시하며, 위반 시 손해배상 소송 대상이 됩니다. 베트남에서는 'quyền giữ ánh nắng' 개념이 있으나 한국만큼 법적으로 구체화되지 않았으며, 통역 시 한국의 엄격한 기준을 강조해야 합니다.",
        "meaningVi": "Quyền giữ ánh nắng là quyền được tiếp nhận ánh sáng mặt trời của công trình, được pháp luật bảo vệ để công trình lân cận không cản trở. Ở Hàn Quốc, Luật Xây dựng và Luật Nhà ở quy định cụ thể (ví dụ: tối thiểu 2 giờ ánh nắng từ 9h-15h vào ngày đông chí). Vi phạm có thể bị kiện đòi bồi thường.",
        "context": "formal",
        "culturalNote": "한국은 일조권 분쟁이 매우 흔하며, 건축 설계 단계부터 일조권 검토가 의무입니다. 베트남은 일조권 개념이 있으나 법적 강제력이 약하고, 분쟁 시 민사소송보다는 협의로 해결하는 경향이 강합니다. 통역 시 한국의 일조권 기준(예: 인동간격, 높이 제한)을 베트남 측에 명확히 설명해야 합니다.",
        "commonMistakes": [
            {
                "mistake": "일조권을 단순히 '햇빛 받을 권리'로만 설명",
                "correction": "법적 기준(2시간 일조 등)과 손해배상 가능성 포함",
                "explanation": "한국에서는 일조권 침해가 금전적 배상 사유입니다."
            },
            {
                "mistake": "'조망권'과 일조권을 혼동",
                "correction": "일조권은 햇빛, 조망권은 경치/전망",
                "explanation": "조망권은 일조권보다 법적 보호가 약합니다."
            },
            {
                "mistake": "일조권 기준을 양국 동일하게 설명",
                "correction": "한국은 동지 기준 2시간 일조, 베트남은 기준 다름",
                "explanation": "한국의 구체적 기준을 베트남에 그대로 적용할 수 없습니다."
            }
        ],
        "examples": [
            {
                "ko": "이 건물은 일조권 침해로 설계를 변경해야 합니다.",
                "vi": "Công trình này vi phạm quyền giữ ánh nắng nên phải thay đổi thiết kế.",
                "situation": "formal"
            },
            {
                "ko": "일조권 분석 결과, 인동간격을 8m로 조정하겠습니다.",
                "vi": "Theo phân tích quyền giữ ánh nắng, chúng tôi sẽ điều chỉnh khoảng cách giữa các tòa thành 8m.",
                "situation": "onsite"
            },
            {
                "ko": "일조권 침해로 인한 손해배상 소송이 제기되었습니다.",
                "vi": "Đã có đơn kiện đòi bồi thường do vi phạm quyền giữ ánh nắng.",
                "situation": "formal"
            }
        ],
        "relatedTerms": ["조망권", "인동간격", "높이제한", "환경권"]
    },
    {
        "slug": "duong-gioi-xay-dung",
        "korean": "건축선",
        "vietnamese": "Đường giới xây dựng",
        "hanja": "建築線",
        "hanjaReading": "建(집 건) + 築(쌓을 축) + 線(줄 선)",
        "pronunciation": "건축썬",
        "meaningKo": "도로와 대지의 경계에서 건축물을 지을 수 있는 한계선으로, 도로에서 일정 거리 후퇴하여 설정됩니다. 통역 시 주의사항: 한국은 건축법상 건축선 후퇴 의무(예: 4m 미만 도로는 중심선에서 2m 후퇴)가 명확하며, 베트남은 'đường giới xây dựng' 또는 'lùi ranh giới đường' 개념으로 유사하나 지역별로 기준이 다릅니다. 건축선 위반 시 건축허가가 나지 않으므로 통역 시 법적 강제성을 강조해야 합니다.",
        "meaningVi": "Đường giới xây dựng là ranh giới giới hạn xây dựng công trình, được thiết lập bằng cách lùi một khoảng cách nhất định từ ranh giới đường. Ở Hàn Quốc, Luật Xây dựng quy định nghĩa vụ lùi ranh (ví dụ: lùi 2m từ tâm đường nếu đường dưới 4m). Vi phạm đường giới xây dựng sẽ không được cấp giấy phép.",
        "context": "formal",
        "culturalNote": "한국은 건축선 후퇴를 통해 도로 확보 및 보행 공간을 확보하며, 건축선 위반 시 행정처분이 엄격합니다. 베트남은 'lùi ranh giới đường' 규정이 있으나 집행이 느슨한 지역이 많고, 기존 건물들이 건축선을 침범한 사례가 흔합니다. 통역 시 한국의 엄격한 기준을 설명하되, 베트남 측의 현지 관행도 고려해야 합니다.",
        "commonMistakes": [
            {
                "mistake": "'대지경계선'과 건축선을 혼동",
                "correction": "대지경계선은 토지 경계, 건축선은 건축 가능 한계선",
                "explanation": "건축선은 대지경계선보다 안쪽에 위치합니다."
            },
            {
                "mistake": "건축선을 단순히 '후퇴선'으로만 번역",
                "correction": "건축선은 법적 개념, 후퇴는 그 방법 중 하나",
                "explanation": "건축선은 법으로 정해진 건축 한계입니다."
            },
            {
                "mistake": "건축선 후퇴 거리를 양국 동일하게 설명",
                "correction": "한국은 도로 폭에 따라 1~3m 후퇴, 베트남은 지역별 다름",
                "explanation": "각국의 기준이 다르므로 명확히 구분해야 합니다."
            }
        ],
        "examples": [
            {
                "ko": "이 대지는 건축선에서 2m 후퇴해야 건축이 가능합니다.",
                "vi": "Khu đất này phải lùi 2m từ đường giới xây dựng mới được xây.",
                "situation": "formal"
            },
            {
                "ko": "건축선을 침범하면 건축허가가 반려됩니다.",
                "vi": "Nếu xâm phạm đường giới xây dựng, giấy phép xây dựng sẽ bị từ chối.",
                "situation": "onsite"
            },
            {
                "ko": "이 도로는 폭이 6m이므로 건축선에서 1.5m 후퇴하면 됩니다.",
                "vi": "Đường này rộng 6m nên chỉ cần lùi 1.5m từ đường giới xây dựng.",
                "situation": "formal"
            }
        ],
        "relatedTerms": ["대지경계선", "도로", "후퇴거리", "공지"]
    },
    {
        "slug": "khu-dat-lien-ke",
        "korean": "인접대지",
        "vietnamese": "Khu đất liền kề",
        "hanja": "隣接垈地",
        "hanjaReading": "隣(이웃 린) + 接(잇댈 접) + 垈(터 대) + 地(땅 지)",
        "pronunciation": "인접대지",
        "meaningKo": "건축하려는 대지와 맞닿아 있는 이웃 토지를 의미하며, 건축 계획 시 인접대지 소유자의 권리(일조권, 사생활 보호 등)를 침해하지 않도록 주의해야 합니다. 통역 시 주의사항: 한국은 인접대지와의 경계 분쟁, 일조권 침해, 소음 문제 등이 빈번하며, 민법상 상린관계로 규율됩니다. 베트남에서는 'khu đất liền kề' 또는 'đất giáp ranh' 개념으로 유사하나, 분쟁 해결 방식이 다를 수 있습니다. 통역 시 한국의 상린관계 법리를 설명해야 합니다.",
        "meaningVi": "Khu đất liền kề là khu đất tiếp giáp với khu đất dự định xây dựng. Khi lập kế hoạch xây dựng, cần chú ý không xâm phạm quyền lợi của chủ sở hữu khu đất liền kề (quyền giữ ánh nắng, quyền riêng tư, v.v.). Ở Hàn Quốc, tranh chấp về ranh giới, vi phạm ánh nắng, tiếng ồn rất phổ biến và được điều chỉnh bởi quan hệ láng giềng theo Luật Dân sự.",
        "context": "formal",
        "culturalNote": "한국은 인접대지 소유자와의 분쟁이 많아, 건축 설계 전 사전 협의가 중요하며, 분쟁 시 법원 조정이나 소송으로 이어집니다. 베트남은 인접대지 문제가 발생하면 주로 지방정부나 인민위원회가 중재하며, 법적 소송보다는 협의 해결이 일반적입니다. 통역 시 양국의 분쟁 해결 메커니즘 차이를 명확히 해야 합니다.",
        "commonMistakes": [
            {
                "mistake": "'인접대지'를 단순히 '옆 땅'으로만 번역",
                "correction": "법적 권리 관계(상린관계)가 존재하는 이웃 토지",
                "explanation": "인접대지는 법적 의무와 권리가 발생하는 개념입니다."
            },
            {
                "mistake": "인접대지 경계 분쟁을 단순 민원으로 처리",
                "correction": "경계 분쟁은 측량, 등기부 확인, 법적 절차 필요",
                "explanation": "경계 분쟁은 토지 소유권 문제로 법적 절차가 중요합니다."
            },
            {
                "mistake": "인접대지 동의서를 형식적으로 처리",
                "correction": "일조권, 소음, 프라이버시 침해 가능성을 구체적으로 설명",
                "explanation": "사후 분쟁을 방지하려면 사전에 충분히 협의해야 합니다."
            }
        ],
        "examples": [
            {
                "ko": "인접대지 소유자의 동의서를 받아야 건축허가가 가능합니다.",
                "vi": "Cần có giấy đồng ý của chủ sở hữu khu đất liền kề mới được cấp giấy phép xây dựng.",
                "situation": "formal"
            },
            {
                "ko": "인접대지와의 경계 분쟁으로 시공이 지연되고 있습니다.",
                "vi": "Tranh chấp ranh giới với khu đất liền kề đang làm chậm tiến độ thi công.",
                "situation": "onsite"
            },
            {
                "ko": "인접대지에 대한 일조권 침해를 최소화하도록 설계했습니다.",
                "vi": "Thiết kế đã được điều chỉnh để giảm thiểu vi phạm quyền giữ ánh nắng đối với khu đất liền kề.",
                "situation": "formal"
            }
        ],
        "relatedTerms": ["상린관계", "경계", "일조권", "대지경계선"]
    },
    {
        "slug": "khu-phan-chong-chay",
        "korean": "방화구획",
        "vietnamese": "Khu phân chống cháy",
        "hanja": "防火區劃",
        "hanjaReading": "防(막을 방) + 火(불 화) + 區(구역 구) + 劃(그을 획)",
        "pronunciation": "방화구획",
        "meaningKo": "건축물 내부를 화재 확산 방지를 위해 내화구조로 구획한 단위로, 일정 면적마다 방화벽·방화문으로 분리해야 합니다. 통역 시 주의사항: 한국은 건축법 및 소방법에서 방화구획 설치 기준(예: 1,000㎡마다, 3개 층마다)을 명시하며, 위반 시 건축물 사용승인이 불가합니다. 베트남에서는 'khu phân chống cháy' 개념이 있으나 기준이 덜 구체적이고, 통역 시 한국의 엄격한 기준을 설명해야 합니다.",
        "meaningVi": "Khu phân chống cháy là đơn vị được ngăn cách bằng tường chịu lửa và cửa chống cháy để ngăn chặn sự lan rộng của hỏa hoạn trong công trình. Ở Hàn Quốc, Luật Xây dựng và Luật Phòng cháy chữa cháy quy định cụ thể tiêu chuẩn (ví dụ: cứ 1.000㎡ hoặc 3 tầng phải phân khu). Vi phạm sẽ không được nghiệm thu đưa vào sử dụng.",
        "context": "formal",
        "culturalNote": "한국은 방화구획이 소방검사의 핵심 항목이며, 준공 전 소방서 검사를 통과해야 사용승인을 받을 수 있습니다. 베트남은 방화구획 개념이 있으나 검사가 덜 엄격한 경우가 많고, 기존 건물에 사후 적용하는 경우도 흔합니다. 통역 시 한국의 방화구획 기준(면적, 층수, 내화성능)을 명확히 설명해야 합니다.",
        "commonMistakes": [
            {
                "mistake": "방화구획을 단순히 '불막이 벽'으로만 설명",
                "correction": "내화성능 기준(1~3시간)을 충족하는 법적 구획",
                "explanation": "방화구획은 내화구조, 방화문, 스프링클러 등이 포함된 시스템입니다."
            },
            {
                "mistake": "'방화벽'과 '내화벽'을 혼동",
                "correction": "방화벽은 화재 확산 방지, 내화벽은 구조 내화",
                "explanation": "방화벽은 소방법, 내화벽은 건축법 개념입니다."
            },
            {
                "mistake": "방화구획 면적 기준을 양국 동일하게 설명",
                "correction": "한국은 1,000㎡ 기준, 베트남은 다를 수 있음",
                "explanation": "각국의 소방 기준이 다르므로 명확히 구분해야 합니다."
            }
        ],
        "examples": [
            {
                "ko": "이 건물은 1,500㎡이므로 방화구획을 2개 이상 설치해야 합니다.",
                "vi": "Công trình này có 1.500㎡ nên phải lắp đặt ít nhất 2 khu phân chống cháy.",
                "situation": "formal"
            },
            {
                "ko": "방화구획 미설치로 소방검사에서 불합격 판정을 받았습니다.",
                "vi": "Bị đánh giá không đạt trong kiểm tra phòng cháy do chưa lắp đặt khu phân chống cháy.",
                "situation": "onsite"
            },
            {
                "ko": "방화문은 1시간 내화성능을 충족해야 방화구획으로 인정됩니다.",
                "vi": "Cửa chống cháy phải đáp ứng khả năng chịu lửa 1 giờ mới được công nhận là khu phân chống cháy.",
                "situation": "formal"
            }
        ],
        "relatedTerms": ["방화벽", "방화문", "내화구조", "소방시설"]
    },
    {
        "slug": "cau-thang-thoat-nan",
        "korean": "피난계단",
        "vietnamese": "Cầu thang thoát nạn",
        "hanja": "避難階段",
        "hanjaReading": "避(피할 피) + 難(어려울 난) + 階(층계 계) + 段(층계 단)",
        "pronunciation": "피난계단",
        "meaningKo": "화재 등 비상 시 건축물 밖으로 안전하게 대피할 수 있도록 설치된 계단으로, 내화구조와 방연 성능을 갖추어야 합니다. 통역 시 주의사항: 한국은 건축법상 일정 층수(3층 이상) 또는 용도(다중이용시설)에 피난계단 설치가 의무이며, 특별피난계단과 일반 피난계단으로 구분됩니다. 베트남에서는 'cầu thang thoát nạn' 또는 'cầu thang PCCC' 개념으로 유사하나, 기준이 덜 구체적일 수 있으며, 통역 시 한국의 엄격한 기준을 강조해야 합니다.",
        "meaningVi": "Cầu thang thoát nạn là cầu thang được thiết kế để người dân có thể sơ tán an toàn ra ngoài công trình khi xảy ra hỏa hoạn hoặc tình huống khẩn cấp, phải có kết cấu chịu lửa và khả năng chống khói. Ở Hàn Quốc, Luật Xây dựng quy định bắt buộc lắp đặt cầu thang thoát nạn từ tầng 3 trở lên hoặc công trình đông người, chia thành cầu thang thoát nạn đặc biệt và cầu thang thoát nạn thông thường.",
        "context": "formal",
        "culturalNote": "한국은 피난계단이 소방검사의 핵심 항목이며, 구조·위치·폭·방연설비 등이 엄격히 규정됩니다. 베트남은 피난계단 설치 의무가 있으나 검사가 느슨한 경우가 많고, 기존 건물에 사후 설치를 요구받는 사례도 흔합니다. 통역 시 한국의 특별피난계단 기준(제연설비, 부속실 등)을 명확히 설명해야 합니다.",
        "commonMistakes": [
            {
                "mistake": "'비상계단'과 피난계단을 혼동",
                "correction": "피난계단은 법적 개념, 비상계단은 일상 용어",
                "explanation": "피난계단은 건축법에 정의된 특정 구조입니다."
            },
            {
                "mistake": "특별피난계단과 일반 피난계단 구분 없이 설명",
                "correction": "특별피난계단은 제연설비, 부속실 필수",
                "explanation": "고층 건물은 특별피난계단 설치가 의무입니다."
            },
            {
                "mistake": "피난계단 폭 기준을 양국 동일하게 설명",
                "correction": "한국은 1.2m 이상, 베트남은 기준 다를 수 있음",
                "explanation": "각국의 기준이 다르므로 명확히 구분해야 합니다."
            }
        ],
        "examples": [
            {
                "ko": "이 건물은 5층이므로 특별피난계단을 설치해야 합니다.",
                "vi": "Công trình này có 5 tầng nên phải lắp đặt cầu thang thoát nạn đặc biệt.",
                "situation": "formal"
            },
            {
                "ko": "피난계단의 폭이 기준 미달로 시정 명령이 내려졌습니다.",
                "vi": "Đã có lệnh khắc phục do chiều rộng cầu thang thoát nạn không đạt tiêu chuẩn.",
                "situation": "onsite"
            },
            {
                "ko": "피난계단 부속실에 제연설비를 추가로 설치했습니다.",
                "vi": "Đã bổ sung lắp đặt thiết bị chống khói tại tiền thất của cầu thang thoát nạn.",
                "situation": "formal"
            }
        ],
        "relatedTerms": ["특별피난계단", "제연설비", "부속실", "비상구"]
    },
    {
        "slug": "co-so-vat-chat-cho-nguoi-khuyet-tat",
        "korean": "장애인편의시설",
        "vietnamese": "Cơ sở vật chất cho người khuyết tật",
        "hanja": "障礙人便宜施設",
        "hanjaReading": "障(막을 장) + 礙(막힐 애) + 人(사람 인) + 便(편할 편) + 宜(마땅할 의) + 施(베풀 시) + 設(베풀 설)",
        "pronunciation": "장애인편의시설",
        "meaningKo": "장애인·노인·임산부 등이 건축물을 안전하고 편리하게 이용할 수 있도록 설치하는 시설로, 경사로·승강기·화장실·주차장 등이 포함됩니다. 통역 시 주의사항: 한국은 '장애인·노인·임산부 등의 편의증진 보장에 관한 법률(장애인편의법)'로 설치 기준이 매우 구체적이며(예: 경사로 기울기 1/12 이하), 위반 시 과태료 및 시정 명령이 부과됩니다. 베트남에서는 'cơ sở vật chất cho người khuyết tật' 개념이 있으나 법적 강제력이 약하며, 통역 시 한국의 엄격한 기준을 설명해야 합니다.",
        "meaningVi": "Cơ sở vật chất cho người khuyết tật là các thiết bị được lắp đặt để người khuyết tật, người cao tuổi, phụ nữ mang thai có thể sử dụng công trình một cách an toàn và thuận tiện, bao gồm đường dốc, thang máy, nhà vệ sinh, bãi đỗ xe, v.v. Ở Hàn Quốc, Luật Tăng cường tiện nghi cho người khuyết tật quy định tiêu chuẩn rất chi tiết (ví dụ: độ dốc đường dốc ≤1/12). Vi phạm sẽ bị phạt tiền và lệnh khắc phục.",
        "context": "formal",
        "culturalNote": "한국은 장애인편의시설 설치가 건축허가 및 사용승인의 필수 조건이며, 설치 후에도 유지관리 의무가 있습니다. 베트남은 장애인편의시설 법규가 있으나 기존 건물에 적용이 느슨하고, 신축 건물에도 검사가 엄격하지 않은 경우가 많습니다. 통역 시 한국의 설치 기준(폭, 기울기, 재질 등)을 구체적으로 설명해야 합니다.",
        "commonMistakes": [
            {
                "mistake": "장애인편의시설을 '선택 사항'으로 설명",
                "correction": "한국에서는 법적 의무 시설",
                "explanation": "일정 규모 이상 건축물은 반드시 설치해야 합니다."
            },
            {
                "mistake": "경사로와 엘리베이터만 언급",
                "correction": "화장실, 주차장, 안내시설, 점자블록 등도 포함",
                "explanation": "장애인편의시설은 포괄적 개념입니다."
            },
            {
                "mistake": "경사로 기울기 기준을 양국 동일하게 설명",
                "correction": "한국은 1/12 이하, 베트남은 기준 다를 수 있음",
                "explanation": "각국의 기준이 다르므로 명확히 구분해야 합니다."
            }
        ],
        "examples": [
            {
                "ko": "이 건물은 장애인편의시설 미설치로 사용승인이 보류되었습니다.",
                "vi": "Công trình này bị trì hoãn nghiệm thu do chưa lắp đặt cơ sở vật chất cho người khuyết tật.",
                "situation": "formal"
            },
            {
                "ko": "장애인 화장실의 손잡이 높이가 기준에 맞지 않아 시정했습니다.",
                "vi": "Đã khắc phục do chiều cao tay vịn nhà vệ sinh cho người khuyết tật không đúng tiêu chuẩn.",
                "situation": "onsite"
            },
            {
                "ko": "장애인 주차장 2면 이상 확보가 의무입니다.",
                "vi": "Bắt buộc phải đảm bảo ít nhất 2 chỗ đỗ xe cho người khuyết tật.",
                "situation": "formal"
            }
        ],
        "relatedTerms": ["경사로", "승강기", "점자블록", "장애인화장실"]
    },
    {
        "slug": "so-dang-ky-cong-trinh",
        "korean": "건축물대장",
        "vietnamese": "Sổ đăng ký công trình",
        "hanja": "建築物臺帳",
        "hanjaReading": "建(집 건) + 築(쌓을 축) + 物(물건 물) + 臺(대 대) + 帳(장부 장)",
        "pronunciation": "건축물대장",
        "meaningKo": "건축물의 소재지·면적·구조·용도·소유자 등을 기록한 공적 장부로, 부동산 등기와 함께 건축물의 법적 현황을 증명합니다. 통역 시 주의사항: 한국은 건축물대장이 건축행정시스템(세움터)에 전산화되어 있으며, 사용승인 후 자동 생성됩니다. 베트남에서는 'sổ đăng ký công trình' 또는 'hồ sơ công trình' 개념으로 유사하나, 전산화 수준이 낮고 지방정부마다 관리 방식이 다를 수 있습니다. 통역 시 건축물대장의 법적 증명력과 등기부등본과의 차이를 명확히 해야 합니다.",
        "meaningVi": "Sổ đăng ký công trình là sổ sách công khai ghi chép vị trí, diện tích, kết cấu, mục đích sử dụng, chủ sở hữu của công trình, cùng với đăng ký bất động sản chứng minh tình trạng pháp lý của công trình. Ở Hàn Quốc, sổ đăng ký công trình được số hóa trong Hệ thống hành chính xây dựng (Sewoom-teo) và tự động tạo sau nghiệm thu đưa vào sử dụng.",
        "context": "formal",
        "culturalNote": "한국은 건축물대장이 부동산 거래, 담보 설정, 세금 부과의 기초 자료로 활용되며, 정부24에서 온라인 열람·발급이 가능합니다. 베트남은 건축물 등록 시스템이 발전 중이나 아직 지방정부 오프라인 기록에 의존하는 경우가 많고, 통역 시 한국의 전산화된 시스템을 설명하되 베트남의 현지 관행도 고려해야 합니다.",
        "commonMistakes": [
            {
                "mistake": "'등기부등본'과 건축물대장을 혼동",
                "correction": "등기부등본은 소유권, 건축물대장은 건축 현황",
                "explanation": "등기부등본은 법무부, 건축물대장은 국토부 소관입니다."
            },
            {
                "mistake": "건축물대장 미발급을 단순 행정 실수로 처리",
                "correction": "사용승인 없이는 건축물대장 발급 불가",
                "explanation": "사용승인이 건축물대장 생성의 전제 조건입니다."
            },
            {
                "mistake": "건축물대장 정정을 쉽게 가능한 것으로 설명",
                "correction": "정정은 증빙서류와 현장 확인 필요",
                "explanation": "면적·구조 변경은 법적 절차를 거쳐야 합니다."
            }
        ],
        "examples": [
            {
                "ko": "건축물대장에 기재된 면적과 실제 면적이 달라 정정 신청을 했습니다.",
                "vi": "Đã nộp đơn sửa chữa vì diện tích ghi trong sổ đăng ký công trình khác với diện tích thực tế.",
                "situation": "formal"
            },
            {
                "ko": "건축물대장은 정부24에서 즉시 발급받을 수 있습니다.",
                "vi": "Sổ đăng ký công trình có thể được cấp ngay trên Chính phủ24.",
                "situation": "onsite"
            },
            {
                "ko": "건축물대장상 용도를 주거에서 상업으로 변경하려면 용도변경 허가가 필요합니다.",
                "vi": "Để thay đổi mục đích sử dụng trong sổ đăng ký công trình từ nhà ở sang thương mại, cần có giấy phép thay đổi mục đích sử dụng.",
                "situation": "formal"
            }
        ],
        "relatedTerms": ["등기부등본", "사용승인", "용도변경", "면적"]
    }
]

def main():
    # File path
    file_path = os.path.join(
        os.path.dirname(__file__),
        "..",
        "data",
        "terms",
        "construction.json"
    )

    # Read existing data
    with open(file_path, "r", encoding="utf-8") as f:
        existing_data = json.load(f)

    print(f"기존 용어 수: {len(existing_data)}")

    # Add new terms
    existing_data.extend(data)

    print(f"추가된 용어 수: {len(data)}")
    print(f"총 용어 수: {len(existing_data)}")

    # Write back
    with open(file_path, "w", encoding="utf-8") as f:
        json.dump(existing_data, f, ensure_ascii=False, indent=2)

    print(f"\n✅ 저장 완료: {file_path}")
    print("\n추가된 용어 목록:")
    for i, term in enumerate(data, 1):
        print(f"{i}. {term['korean']} ({term['vietnamese']})")

if __name__ == "__main__":
    main()
