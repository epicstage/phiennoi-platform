#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
준공/인수인계 (Completion/Handover) 전문용어 추가 스크립트
Tier S 품질 기준 준수 (90점 이상)
"""

import json
import os

# 파일 경로 설정
file_path = os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', 'data', 'terms', 'construction.json')

# 기존 데이터 로드
with open(file_path, 'r', encoding='utf-8') as f:
    data = json.load(f)  # data is a LIST

# 기존 slug 수집
existing_slugs = {t['slug'] for t in data}

# 새 용어 정의
new_terms = [
    {
        "slug": "nghiem-thu-hoan-cong",
        "korean": "준공검사",
        "vietnamese": "nghiệm thu hoàn công",
        "hanja": "竣工檢査",
        "hanjaReading": "竣(마칠 준) + 工(장인 공) + 檢(조사할 검) + 査(조사할 사)",
        "pronunciation": "응이엠 투 호안 꽁",
        "meaningKo": "건설공사가 완료된 후 설계도서 및 관련 법규에 적합하게 시공되었는지 확인하는 최종 검사 절차입니다. 통역 시 '검사(kiểm tra)'와 '검수(nghiệm thu)'를 명확히 구분해야 하며, 베트남에서는 공사 단계별로 여러 차례 nghiệm thu가 있지만 '준공검사'는 최종 단계의 nghiệm thu hoàn công을 의미합니다. 한국에서는 감리자, 발주자, 인허가 기관이 참여하는 반면 베트남에서는 Hội đồng nghiệm thu(검수위원회) 형태로 진행되는 차이가 있습니다. 불합격 시 'không đạt yêu cầu'로 표현하며 재검사(nghiệm thu lại)가 필요합니다.",
        "meaningVi": "Quy trình kiểm tra cuối cùng để xác nhận công trình xây dựng đã hoàn thành đúng theo thiết kế và quy định pháp luật. Ở Việt Nam, nghiệm thu hoàn công được thực hiện bởi Hội đồng nghiệm thu gồm đại diện chủ đầu tư, tư vấn giám sát, nhà thầu và cơ quan quản lý nhà nước. Kết quả nghiệm thu được lập thành biên bản và là cơ sở để cấp giấy phép sử dụng công trình.",
        "context": "준공 단계",
        "culturalNote": "한국은 감리자 중심의 준공검사 후 지자체 사용승인을 받지만, 베트남은 Hội đồng nghiệm thu(검수위원회)가 공식 검사를 진행하고 Sở Xây dựng(건설청)이 최종 승인합니다. 한국의 '사용승인서'는 베트남의 'Giấy phép sử dụng'에 해당하지만 발급 주체와 절차가 다릅니다. 베트남에서는 nghiệm thu 단계가 더 세분화되어 있으며(nghiệm thu giai đoạn, nghiệm thu từng phần), 각 단계마다 biên bản(조서)을 작성해야 합니다.",
        "commonMistakes": [
            {
                "mistake": "nghiệm thu = 검사(일반)",
                "correction": "nghiệm thu hoàn công = 준공검사(최종)",
                "explanation": "nghiệm thu는 공사 중 여러 단계에서 이루어지지만, 준공검사는 반드시 'hoàn công'을 붙여 최종 검사임을 명시해야 합니다."
            },
            {
                "mistake": "kiểm tra hoàn công",
                "correction": "nghiệm thu hoàn công",
                "explanation": "kiểm tra는 일반 점검이고, nghiệm thu는 공식적인 검수 절차입니다. 법적 문서에서는 반드시 nghiệm thu를 사용합니다."
            },
            {
                "mistake": "합격 = đạt / 불합격 = không đạt",
                "correction": "đạt yêu cầu / không đạt yêu cầu",
                "explanation": "베트남에서는 'yêu cầu(요구사항)'를 반드시 포함하여 기준 충족 여부를 명확히 표현합니다."
            }
        ],
        "examples": [
            {
                "ko": "다음 주 화요일에 준공검사가 예정되어 있습니다.",
                "vi": "Nghiệm thu hoàn công dự kiến vào thứ Ba tuần sau.",
                "situation": "formal"
            },
            {
                "ko": "준공검사에서 방수 공사 부분이 불합격 판정을 받았습니다.",
                "vi": "Phần công tác chống thấm không đạt yêu cầu trong nghiệm thu hoàn công.",
                "situation": "formal"
            },
            {
                "ko": "검수위원회가 현장에서 준공검사를 진행 중입니다.",
                "vi": "Hội đồng nghiệm thu đang tiến hành nghiệm thu hoàn công tại hiện trường.",
                "situation": "onsite"
            }
        ],
        "relatedTerms": ["ban-giao-cong-trinh", "ho-so-hoan-cong", "giay-phep-su-dung", "bien-ban-nghiem-thu"]
    },
    {
        "slug": "ban-giao-cong-trinh",
        "korean": "건물인수",
        "vietnamese": "bàn giao công trình",
        "hanja": "建物引受",
        "hanjaReading": "建(세울 건) + 物(물건 물) + 引(끌 인) + 受(받을 수)",
        "pronunciation": "반 자오 꽁 트린",
        "meaningKo": "시공사가 완공된 건물을 발주자에게 공식적으로 넘겨주는 절차로, 준공검사 합격 후 진행됩니다. 통역 시 '인계(giao)'와 '인수(nhận)'를 구분하여 'bàn giao'는 쌍방 행위임을 강조해야 합니다. 베트남에서는 biên bản bàn giao(인수인계 조서)를 작성하고 양측이 서명하며, 이때 열쇠(chìa khóa), 도면(bản vẽ), 사용설명서(sổ tay hướng dẫn)를 함께 전달합니다. 한국과 달리 베트남은 인수 후 bảo hành(하자보수) 기간이 명확히 구분되며 일반적으로 12-24개월입니다.",
        "meaningVi": "Thủ tục chính thức chuyển giao công trình đã hoàn thành từ nhà thầu thi công cho chủ đầu tư sau khi nghiệm thu đạt yêu cầu. Quá trình bàn giao phải lập biên bản ghi rõ hiện trạng công trình, các hạng mục đã hoàn thành, tài liệu kỹ thuật, và cam kết bảo hành. Nhà thầu phải bàn giao đầy đủ hồ sơ hoàn công, bản vẽ as-built, sổ tay vận hành và bảo dưỡng.",
        "context": "인수인계 단계",
        "culturalNote": "한국은 준공 후 즉시 입주/사용이 가능하지만, 베트남은 bàn giao 후에도 giấy phép sử dụng(사용승인증)을 별도로 받아야 합니다. 한국의 '하자보수책임기간'은 베트남의 'thời gian bảo hành'과 유사하지만, 베트남은 계약서에 명시된 기간만 인정되며 법정 최소 기간이 없습니다. 또한 베트남에서는 bàn giao 시 현장에서 모든 설비를 함께 가동해보며 확인하는 것이 관례입니다.",
        "commonMistakes": [
            {
                "mistake": "giao nhận công trình",
                "correction": "bàn giao công trình",
                "explanation": "'bàn giao'는 공식적인 인수인계를 의미하는 법률 용어로, 단순한 'giao nhận(주고받기)'과 다릅니다."
            },
            {
                "mistake": "인수 = nhận / 인계 = giao",
                "correction": "인수인계 = bàn giao (쌍방 행위)",
                "explanation": "한국어 '인수인계'는 베트남어에서 하나의 동사 'bàn giao'로 표현되며, 쌍방이 참여하는 행위임을 내포합니다."
            },
            {
                "mistake": "chuyển giao = bàn giao",
                "correction": "chuyển giao(이전) ≠ bàn giao(공식 인수인계)",
                "explanation": "chuyển giao는 일반적인 이전이고, bàn giao는 문서와 조서를 수반하는 공식 절차입니다."
            }
        ],
        "examples": [
            {
                "ko": "이번 주 금요일에 공사현장 건물인수가 예정되어 있습니다.",
                "vi": "Bàn giao công trình tại hiện trường dự kiến vào thứ Sáu tuần này.",
                "situation": "formal"
            },
            {
                "ko": "인수인계 시 모든 열쇠와 준공도면을 함께 전달해주세요.",
                "vi": "Khi bàn giao, vui lòng chuyển giao đầy đủ chìa khóa và bản vẽ hoàn công.",
                "situation": "onsite"
            },
            {
                "ko": "발주처에서 건물인수를 거부했습니다.",
                "vi": "Chủ đầu tư từ chối bàn giao công trình.",
                "situation": "formal"
            }
        ],
        "relatedTerms": ["nghiem-thu-hoan-cong", "bien-ban-nghiem-thu", "ho-so-hoan-cong", "bao-tri-dinh-ky"]
    },
    {
        "slug": "ho-so-hoan-cong",
        "korean": "준공서류",
        "vietnamese": "hồ sơ hoàn công",
        "hanja": "竣工書類",
        "hanjaReading": "竣(마칠 준) + 工(장인 공) + 書(글 서) + 類(무리 류)",
        "pronunciation": "호 서 호안 꽁",
        "meaningKo": "건설공사가 완료된 후 작성되는 모든 문서와 도면을 포괄하는 용어로, 준공검사 및 건물인수에 필수적인 자료입니다. 통역 시 '서류(giấy tờ)'보다 '문서철/서류철(hồ sơ)'이 공식적이며, 베트남에서는 hồ sơ hoàn công이 법적 요구사항으로 Sở Xây dựng(건설청)에 제출해야 합니다. 포함 내용은 bản vẽ hoàn công(준공도면), biên bản nghiệm thu(검수조서), 자재 시험성적서, 안전점검 결과, 사용설명서 등이며, 한국보다 베트남이 더 상세한 문서를 요구합니다.",
        "meaningVi": "Toàn bộ tài liệu và bản vẽ được lập sau khi hoàn thành công trình xây dựng, bao gồm bản vẽ hoàn công, biên bản nghiệm thu các giai đoạn, giấy chứng nhận chất lượng vật liệu, kết quả thí nghiệm, sổ tay vận hành thiết bị và các tài liệu kỹ thuật khác. Hồ sơ hoàn công phải được nộp cho cơ quan quản lý nhà nước để xin cấp giấy phép sử dụng.",
        "context": "준공 서류 단계",
        "culturalNote": "한국은 준공서류를 감리단에 제출하면 되지만, 베트남은 Sở Xây dựng(건설청)에 직접 제출하고 심사를 받아야 합니다. 베트남의 hồ sơ hoàn công은 3부(주관 부서, 건설청, 시공사 보관용)를 준비하며, 모든 페이지에 도장과 서명이 필요합니다. 한국은 전자문서도 인정되지만 베트남은 여전히 종이 원본(bản gốc)을 요구하는 경우가 많습니다. 또한 베트남은 공사 중 변경사항(biên bản thay đổi)도 모두 hồ sơ에 포함해야 합니다.",
        "commonMistakes": [
            {
                "mistake": "giấy tờ hoàn công",
                "correction": "hồ sơ hoàn công",
                "explanation": "giấy tờ는 일반 서류를 의미하고, hồ sơ는 공식 문서철을 의미하는 법률 용어입니다."
            },
            {
                "mistake": "tài liệu hoàn thành",
                "correction": "hồ sơ hoàn công",
                "explanation": "'hoàn thành'은 일반적인 완료이고, 건설 분야에서는 반드시 'hoàn công'을 사용합니다."
            },
            {
                "mistake": "준공도면 = bản vẽ hoàn thành",
                "correction": "bản vẽ hoàn công",
                "explanation": "건설 용어에서 '준공'은 항상 'hoàn công'으로 번역하며 'hoàn thành'을 쓰지 않습니다."
            }
        ],
        "examples": [
            {
                "ko": "준공서류를 3부 준비해서 건설청에 제출해야 합니다.",
                "vi": "Cần chuẩn bị hồ sơ hoàn công 3 bộ để nộp cho Sở Xây dựng.",
                "situation": "formal"
            },
            {
                "ko": "준공서류 중 자재 시험성적서가 누락되었습니다.",
                "vi": "Trong hồ sơ hoàn công thiếu giấy chứng nhận chất lượng vật liệu.",
                "situation": "onsite"
            },
            {
                "ko": "모든 준공서류에 법인 직인을 날인해주세요.",
                "vi": "Vui lòng đóng dấu pháp nhân lên tất cả hồ sơ hoàn công.",
                "situation": "formal"
            }
        ],
        "relatedTerms": ["ban-ve-hoan-cong", "bien-ban-nghiem-thu", "nghiem-thu-hoan-cong", "giay-phep-su-dung"]
    },
    {
        "slug": "ban-ve-hoan-cong",
        "korean": "준공도면",
        "vietnamese": "bản vẽ hoàn công",
        "hanja": "竣工圖面",
        "hanjaReading": "竣(마칠 준) + 工(장인 공) + 圖(그림 도) + 面(낯 면)",
        "pronunciation": "반 베 호안 꽁",
        "meaningKo": "실제 시공 내용을 반영하여 최종 수정된 설계도면으로, 영어로는 'as-built drawing'이라고 합니다. 통역 시 '설계도면(bản vẽ thiết kế)'과 명확히 구분해야 하며, 준공도면은 시공 중 발생한 모든 변경사항을 빨간색(màu đỏ) 또는 별도 표기로 나타냅니다. 베트남에서는 bản vẽ hoàn công이 없으면 giấy phép sử dụng를 받을 수 없으며, 구조 변경, 배관 경로 수정, 전기 배선 변경 등이 반드시 기록되어야 합니다. 준공도면은 향후 리모델링이나 유지보수 시 필수 참고자료가 됩니다.",
        "meaningVi": "Bản vẽ thiết kế được chỉnh sửa cuối cùng để phản ánh nội dung thi công thực tế (as-built drawing). Tất cả thay đổi so với bản vẽ thiết kế ban đầu phải được thể hiện rõ ràng bằng màu đỏ hoặc ký hiệu riêng. Bản vẽ hoàn công là tài liệu bắt buộc trong hồ sơ hoàn công và được sử dụng cho bảo trì, sửa chữa sau này.",
        "context": "준공 서류",
        "culturalNote": "한국은 CAD 전자도면을 주로 사용하고 PDF도 인정되지만, 베트남은 여전히 A1 용지에 출력된 종이 도면(bản vẽ giấy)을 공식 문서로 요구하는 경우가 많습니다. 베트남에서는 설계 변경 시마다 biên bản thay đổi thiết kế(설계변경 조서)를 작성하고, 이를 바탕으로 준공도면을 수정합니다. 한국은 BIM 모델도 준공도면으로 인정되는 추세지만 베트Nam은 아직 2D 도면이 표준입니다. 도면에는 반드시 책임기술자의 서명과 도장이 필요합니다.",
        "commonMistakes": [
            {
                "mistake": "bản vẽ thi công = 준공도면",
                "correction": "bản vẽ thi công(시공도면) ≠ bản vẽ hoàn công(준공도면)",
                "explanation": "시공도면은 공사 전 작성하고, 준공도면은 공사 후 실제 시공 내용을 반영한 최종 도면입니다."
            },
            {
                "mistake": "as-built = hoàn thành",
                "correction": "as-built = hoàn công",
                "explanation": "영어 'as-built'는 베트남어로 'hoàn công'이며, 일반적인 완료인 'hoàn thành'과 구분됩니다."
            },
            {
                "mistake": "bản vẽ cuối cùng",
                "correction": "bản vẽ hoàn công",
                "explanation": "'cuối cùng(마지막)'은 애매하며, 건설 분야에서는 정확히 'hoàn công'을 사용해야 합니다."
            }
        ],
        "examples": [
            {
                "ko": "준공도면에 변경된 배관 경로를 빨간색으로 표시해주세요.",
                "vi": "Vui lòng đánh dấu màu đỏ đường ống đã thay đổi trên bản vẽ hoàn công.",
                "situation": "onsite"
            },
            {
                "ko": "설계도면과 준공도면의 차이를 확인해주세요.",
                "vi": "Vui lòng kiểm tra sự khác biệt giữa bản vẽ thiết kế và bản vẽ hoàn công.",
                "situation": "formal"
            },
            {
                "ko": "준공도면을 CAD 파일과 PDF로 제출해야 합니다.",
                "vi": "Cần nộp bản vẽ hoàn công dưới dạng file CAD và PDF.",
                "situation": "formal"
            }
        ],
        "relatedTerms": ["ho-so-hoan-cong", "nghiem-thu-hoan-cong", "ban-giao-cong-trinh", "bien-ban-nghiem-thu"]
    },
    {
        "slug": "giay-phep-su-dung",
        "korean": "사용승인",
        "vietnamese": "giấy phép sử dụng",
        "hanja": "使用承認",
        "hanjaReading": "使(부릴 사) + 用(쓸 용) + 承(받들 승) + 認(알 인)",
        "pronunciation": "자이 펩 수 중",
        "meaningKo": "건축물이 관련 법규에 적합하게 완공되었음을 증명하고 사용을 허가하는 공식 문서입니다. 통역 시 한국의 '사용승인서'는 베트남의 'giấy phép sử dụng công trình' 또는 줄여서 'giấy phép sử dụng'에 해당하지만, 발급 절차가 다릅니다. 한국은 지자체가 준공검사 후 즉시 발급하지만, 베트남은 Sở Xây dựng(건설청)에 hồ sơ hoàn công을 제출하고 심사를 거쳐 발급받습니다. 이 서류 없이는 건물을 합법적으로 사용할 수 없으며, 위반 시 phạt vi phạm hành chính(행정 처벌)을 받습니다.",
        "meaningVi": "Giấy tờ chính thức do cơ quan quản lý nhà nước cấp để xác nhận công trình xây dựng đã hoàn thành đúng quy định và được phép đưa vào sử dụng. Để được cấp giấy phép sử dụng, chủ đầu tư phải nộp hồ sơ hoàn công đầy đủ cho Sở Xây dựng, bao gồm biên bản nghiệm thu, bản vẽ hoàn công và các tài liệu kỹ thuật. Không có giấy phép sử dụng là vi phạm pháp luật xây dựng.",
        "context": "준공 후 단계",
        "culturalNote": "한국은 사용승인 후 즉시 등기가 가능하지만, 베트남은 giấy phép sử dụng 외에 별도로 giấy chứng nhận quyền sử dụng đất(토지사용권 증명서)도 필요합니다. 한국은 준공 후 7일 이내 신청하지만 베트Nam은 hoàn công 후 30일 이내 신청해야 하며, 지연 시 벌금이 부과됩니다. 베트남에서는 임시사용승인(giấy phép sử dụng tạm thời)도 있어 일부 미완성 부분이 있어도 제한적으로 사용할 수 있습니다. 주택의 경우 '소유권 증명(sổ hồng)'과는 별개의 서류입니다.",
        "commonMistakes": [
            {
                "mistake": "giấy phép hoàn công",
                "correction": "giấy phép sử dụng (công trình)",
                "explanation": "'hoàn công'은 준공 상태를 의미하고, 사용을 허가하는 것은 'sử dụng'입니다."
            },
            {
                "mistake": "chứng nhận sử dụng",
                "correction": "giấy phép sử dụng",
                "explanation": "베트남 법률 용어로는 'giấy phép(허가증)'이 정확하며 'chứng nhận(증명서)'과 구분됩니다."
            },
            {
                "mistake": "허가 = cho phép / 승인 = chấp thuận",
                "correction": "사용승인 = giấy phép sử dụng (하나의 법률 용어)",
                "explanation": "한국어 '사용승인'은 베트남어에서 'giấy phép sử dụng'이라는 하나의 명사구로 고정되어 있습니다."
            }
        ],
        "examples": [
            {
                "ko": "사용승인을 받기 전에는 입주할 수 없습니다.",
                "vi": "Không được sử dụng công trình trước khi có giấy phép sử dụng.",
                "situation": "formal"
            },
            {
                "ko": "건설청에 사용승인 신청서를 제출했습니다.",
                "vi": "Đã nộp đơn xin cấp giấy phép sử dụng cho Sở Xây dựng.",
                "situation": "formal"
            },
            {
                "ko": "임시사용승인으로 일부 공간만 먼저 사용하겠습니다.",
                "vi": "Sẽ sử dụng một phần không gian trước với giấy phép sử dụng tạm thời.",
                "situation": "onsite"
            }
        ],
        "relatedTerms": ["nghiem-thu-hoan-cong", "ho-so-hoan-cong", "ban-giao-cong-trinh", "bien-ban-nghiem-thu"]
    },
    {
        "slug": "kiem-tra-chat-luong",
        "korean": "품질검사",
        "vietnamese": "kiểm tra chất lượng",
        "hanja": "品質檢査",
        "hanjaReading": "品(물건 품) + 質(바탕 질) + 檢(조사할 검) + 査(조사할 사)",
        "pronunciation": "끼엠 짜 쳇 르엉",
        "meaningKo": "건설 자재, 시공 품질, 완성된 건축물이 정해진 기준에 부합하는지 확인하는 검사 절차입니다. 통역 시 '품질검사(kiểm tra chất lượng)'와 '품질관리(quản lý chất lượng)', '품질보증(đảm bảo chất lượng)'을 명확히 구분해야 합니다. 베트남에서는 công tác kiểm tra chất lượng이 시공 전(vật liệu), 시공 중(quá trình thi công), 시공 후(nghiệm thu)로 나뉘며, 각 단계마다 biên bản kiểm tra(검사 조서)를 작성합니다. 불합격 자재는 즉시 현장 반출(đưa ra khỏi công trường) 처리해야 하며, 무단 사용 시 심각한 법적 책임이 따릅니다.",
        "meaningVi": "Quy trình kiểm tra để xác nhận vật liệu xây dựng, chất lượng thi công và công trình hoàn thành có đạt tiêu chuẩn quy định hay không. Kiểm tra chất lượng bao gồm kiểm tra nguyên vật liệu trước khi sử dụng, kiểm tra trong quá trình thi công, và kiểm tra khi hoàn thành. Mỗi lần kiểm tra phải lập biên bản và lưu vào hồ sơ công trình. Vật liệu không đạt chất lượng phải được loại bỏ khỏi công trường ngay lập tức.",
        "context": "품질 관리",
        "culturalNote": "한국은 KS 인증 자재를 주로 사용하고 자체 품질검사로도 인정되지만, 베트남은 TCVN(베트남 국가표준) 인증 외에도 tổ chức kiểm định độc lập(독립 검사기관)의 검사를 요구하는 경우가 많습니다. 베트남에서는 xi măng(시멘트), thép(철근), gạch(벽돌) 등 주요 자재는 반드시 giấy chứng nhận chất lượng(품질증명서)와 tem chống hàng giả(위조방지 스티커)를 확인합니다. 한국보다 베트남이 현장 샘플링 테스트를 더 자주 요구하며, 발주자가 직접 검사에 참여하는 비율이 높습니다.",
        "commonMistakes": [
            {
                "mistake": "kiểm tra = 품질검사",
                "correction": "kiểm tra chất lượng = 품질검사",
                "explanation": "kiểm tra는 일반 점검이므로 반드시 'chất lượng(품질)'을 명시해야 합니다."
            },
            {
                "mistake": "quản lý chất lượng = 품질검사",
                "correction": "kiểm tra(검사) ≠ quản lý(관리) ≠ đảm bảo(보증)",
                "explanation": "검사는 확인 행위, 관리는 전체 프로세스, 보증은 결과 책임으로 각각 다릅니다."
            },
            {
                "mistake": "자재검사 = kiểm tra vật liệu",
                "correction": "kiểm tra chất lượng vật liệu",
                "explanation": "단순히 vật liệu만 쓰면 수량 검사로 오해될 수 있어 'chất lượng'을 포함해야 합니다."
            }
        ],
        "examples": [
            {
                "ko": "모든 철근은 현장 반입 전에 품질검사를 받아야 합니다.",
                "vi": "Tất cả thép phải qua kiểm tra chất lượng trước khi đưa vào công trường.",
                "situation": "formal"
            },
            {
                "ko": "품질검사에서 콘크리트 강도가 기준 미달입니다.",
                "vi": "Cường độ bê tông không đạt tiêu chuẩn trong kiểm tra chất lượng.",
                "situation": "onsite"
            },
            {
                "ko": "독립 검사기관에 품질검사를 의뢰했습니다.",
                "vi": "Đã ủy thác kiểm tra chất lượng cho tổ chức kiểm định độc lập.",
                "situation": "formal"
            }
        ],
        "relatedTerms": ["nghiem-thu-hoan-cong", "bien-ban-nghiem-thu", "ho-so-hoan-cong", "ban-giao-cong-trinh"]
    },
    {
        "slug": "bien-ban-nghiem-thu",
        "korean": "검수조서",
        "vietnamese": "biên bản nghiệm thu",
        "hanja": "檢收調書",
        "hanjaReading": "檢(조사할 검) + 收(거둘 수) + 調(고를 조) + 書(글 서)",
        "pronunciation": "비엔 반 응이엠 투",
        "meaningKo": "공사의 각 단계나 완공 후 검수 결과를 공식적으로 기록한 문서입니다. 통역 시 '조서(biên bản)'는 공식 회의록 또는 공식 기록을 의미하며, 베트남 법률 문서에서 매우 중요한 증거 자료가 됩니다. biên bản nghiệm thu에는 참석자 명단, 검수 항목, 합격/불합격 판정, 지적사항, 조치사항, 서명 날인이 포함되며, 한국의 '회의록'보다 법적 효력이 강합니다. 베트남에서는 nghiệm thu giai đoạn(단계별 검수), nghiệm thu từng phần(부분 검수), nghiệm thu hoàn công(준공 검수) 등 각각 별도의 biên bản을 작성합니다.",
        "meaningVi": "Văn bản chính thức ghi nhận kết quả nghiệm thu các giai đoạn thi công hoặc công trình hoàn thành. Biên bản nghiệm thu phải có chữ ký của các bên liên quan (chủ đầu tư, tư vấn giám sát, nhà thầu thi công) và ghi rõ các hạng mục đạt yêu cầu, không đạt yêu cầu, cũng như biện pháp khắc phục. Đây là tài liệu pháp lý quan trọng trong hồ sơ hoàn công.",
        "context": "검수 단계",
        "culturalNote": "한국은 검수 결과를 간단한 보고서 형태로 작성하지만, 베트Nam의 biên bản은 공증에 준하는 공식 문서로 모든 페이지에 서명과 도장이 필요합니다. 베트남에서는 biên bản 작성 시 반드시 모든 이해관계자가 현장에 모여야 하며(họp tại hiện trường), 불참 시 별도의 uỷ quyền(위임장)이 필요합니다. 한국과 달리 베트남은 biên bản을 여러 부 작성하여 각 당사자가 원본을 보관하며, 추후 분쟁 시 결정적 증거가 됩니다. 또한 불합격 항목은 반드시 사진과 함께 기록해야 합니다.",
        "commonMistakes": [
            {
                "mistake": "báo cáo nghiệm thu",
                "correction": "biên bản nghiệm thu",
                "explanation": "báo cáo는 일반 보고서이고, biên bản은 공식 조서로 법적 효력이 다릅니다."
            },
            {
                "mistake": "văn bản nghiệm thu",
                "correction": "biên bản nghiệm thu",
                "explanation": "văn bản은 일반 문서이고, biên bản은 회의 결과를 기록한 공식 조서입니다."
            },
            {
                "mistake": "회의록 = biên bản",
                "correction": "회의록(일반) ≠ 검수조서(biên bản nghiệm thu, 법적 효력)",
                "explanation": "한국어 '회의록'은 일반적이지만, biên bản은 법적 구속력이 있는 공식 문서입니다."
            }
        ],
        "examples": [
            {
                "ko": "준공검수조서에 모든 참석자가 서명했습니다.",
                "vi": "Tất cả người tham gia đã ký vào biên bản nghiệm thu hoàn công.",
                "situation": "formal"
            },
            {
                "ko": "검수조서에 불합격 항목과 시정조치를 기록해주세요.",
                "vi": "Vui lòng ghi các hạng mục không đạt và biện pháp khắc phục vào biên bản nghiệm thu.",
                "situation": "onsite"
            },
            {
                "ko": "검수조서 원본을 각 당사자에게 1부씩 전달하겠습니다.",
                "vi": "Sẽ chuyển giao 1 bản gốc biên bản nghiệm thu cho mỗi bên.",
                "situation": "formal"
            }
        ],
        "relatedTerms": ["nghiem-thu-hoan-cong", "ban-giao-cong-trinh", "ho-so-hoan-cong", "kiem-tra-chat-luong"]
    },
    {
        "slug": "so-tay-van-hanh",
        "korean": "운영매뉴얼",
        "vietnamese": "sổ tay vận hành",
        "hanja": "運營manual",
        "hanjaReading": "運(옮길 운) + 營(경영할 영) + manual(외래어)",
        "pronunciation": "소 따이 번 한",
        "meaningKo": "건축물과 설비의 올바른 사용 방법, 유지보수 절차, 주의사항 등을 기록한 안내서입니다. 통역 시 '사용설명서(sách hướng dẫn sử dụng)'와 구분하여, 운영매뉴얼은 더 포괄적이고 전문적인 'sổ tay vận hành' 또는 'sổ tay hướng dẫn vận hành'으로 표현합니다. 베트남에서는 bàn giao 시 반드시 제공해야 하는 문서이며, 기계실, 전기실, 소방설비, HVAC 시스템 등 주요 설비별로 별도의 sổ tay를 작성합니다. 내용은 베트남어로 작성하거나 베트남어 번역본을 함께 제공해야 하며, 외국 장비의 경우 제조사 매뉴얼(tài liệu của nhà sản xuất)도 첨부합니다.",
        "meaningVi": "Tài liệu hướng dẫn cách sử dụng, vận hành và bảo dưỡng đúng cách các hệ thống và thiết bị trong công trình. Sổ tay vận hành phải được lập riêng cho từng hệ thống chính như điện, nước, HVAC, phòng cháy chữa cháy, và phải bao gồm sơ đồ hệ thống, quy trình vận hành, quy trình bảo dưỡng định kỳ, xử lý sự cố, và danh bạ liên hệ nhà cung cấp. Đây là tài liệu bắt buộc khi bàn giao công trình.",
        "context": "인수인계 서류",
        "culturalNote": "한국은 설비업체가 제공하는 영문/한글 매뉴얼을 그대로 사용하는 경우가 많지만, 베트남은 반드시 베트남어 버전(bản tiếng Việt)을 요구하며 전문 번역이 필요합니다. 베트남에서는 sổ tay vận hành에 vận hành viên(운영 담당자)의 자격 요건도 명시하며, 특히 고압전기, 보일러 등은 자격증 보유자만 운영할 수 있어 이를 매뉴얼에 기재해야 합니다. 한국보다 베트남이 비상 연락처(danh bạ khẩn cấp)와 응급조치(xử lý sự cố khẩn cấp) 부분을 더 상세히 요구합니다.",
        "commonMistakes": [
            {
                "mistake": "sách hướng dẫn = 운영매뉴얼",
                "correction": "sổ tay vận hành (더 전문적)",
                "explanation": "sách hướng dẫn은 일반 사용설명서이고, sổ tay vận hành은 건축/설비 전문 매뉴얼입니다."
            },
            {
                "mistake": "manual = 매뉴얼(외래어 그대로)",
                "correction": "sổ tay vận hành (베트남어 표현)",
                "explanation": "베트남에서는 외래어 'manual'보다 순수 베트남어 'sổ tay vận hành'을 사용합니다."
            },
            {
                "mistake": "hướng dẫn sử dụng = 운영매뉴얼",
                "correction": "hướng dẫn sử dụng(사용법) < sổ tay vận hành(운영매뉴얼)",
                "explanation": "hướng dẫn sử dụng은 간단한 사용법이고, sổ tay vận hành은 유지보수 포함 종합 매뉴얼입니다."
            }
        ],
        "examples": [
            {
                "ko": "모든 설비의 운영매뉴얼을 베트남어로 준비해주세요.",
                "vi": "Vui lòng chuẩn bị sổ tay vận hành tất cả thiết bị bằng tiếng Việt.",
                "situation": "formal"
            },
            {
                "ko": "소방설비 운영매뉴얼에 비상 연락처를 추가해야 합니다.",
                "vi": "Cần bổ sung danh bạ khẩn cấp vào sổ tay vận hành hệ thống phòng cháy chữa cháy.",
                "situation": "onsite"
            },
            {
                "ko": "인수인계 시 모든 설비의 운영매뉴얼을 함께 전달합니다.",
                "vi": "Khi bàn giao sẽ chuyển giao sổ tay vận hành của tất cả thiết bị.",
                "situation": "formal"
            }
        ],
        "relatedTerms": ["ban-giao-cong-trinh", "ho-so-hoan-cong", "bao-tri-dinh-ky", "nghiem-thu-hoan-cong"]
    },
    {
        "slug": "bao-tri-dinh-ky",
        "korean": "정기유지보수",
        "vietnamese": "bảo trì định kỳ",
        "hanja": "定期維持保守",
        "hanjaReading": "定(정할 정) + 期(기약할 기) + 維(매을 유) + 持(가질 지) + 保(지킬 보) + 守(지킬 수)",
        "pronunciation": "바오 찌 딘 끼",
        "meaningKo": "건축물과 설비를 정해진 주기에 따라 점검하고 관리하는 유지보수 활동입니다. 통역 시 '유지보수(bảo trì)', '수리(sửa chữa)', '보수(sửa chữa lớn)', '점검(kiểm tra)'을 명확히 구분해야 합니다. 베트남에서는 bảo trì định kỳ가 계약서에 명시되며, hàng ngày(일일), hàng tuần(주간), hàng tháng(월간), hàng quý(분기), hàng năm(연간) 등으로 주기가 세분화됩니다. 엘리베이터, 소방설비, 전기설비 등 안전 관련 설비는 법적으로 정기점검이 의무화되어 있으며, 점검 기록(sổ bảo trì)을 비치해야 합니다.",
        "meaningVi": "Hoạt động kiểm tra, bảo dưỡng công trình và thiết bị theo chu kỳ định trước để duy trì hoạt động ổn định và an toàn. Bảo trì định kỳ bao gồm kiểm tra, vệ sinh, bôi trơn, thay thế linh kiện hao mòn và điều chỉnh thiết bị. Đối với các thiết bị quan trọng như thang máy, hệ thống phòng cháy, điện cao thế, pháp luật quy định bắt buộc phải bảo trì định kỳ và lưu hồ sơ.",
        "context": "유지관리 단계",
        "culturalNote": "한국은 통합 시설관리 업체가 전체를 관리하는 경우가 많지만, 베트Nam은 각 설비별로 전문 업체와 개별 계약(hợp đồng riêng)을 맺는 것이 일반적입니다. 베트남에서는 bảo hành(하자보수 기간 중 무상)과 bảo trì(유상 유지보수)를 명확히 구분하며, 계약서에 chi phí bảo trì(유지보수 비용)를 상세히 명시합니다. 한국보다 베트남이 정기점검 주기를 더 짧게 요구하는 경향이 있으며, 특히 엘리베이터는 월 2회 점검이 일반적입니다. 점검 시마다 sổ bảo trì(보수대장)에 기록하고 서명해야 합니다.",
        "commonMistakes": [
            {
                "mistake": "bảo trì = 수리",
                "correction": "bảo trì(유지보수) ≠ sửa chữa(수리)",
                "explanation": "bảo trì는 예방적 관리이고, sửa chữa는 고장 후 수리입니다."
            },
            {
                "mistake": "bảo hành = bảo trì",
                "correction": "bảo hành(하자보수, 무상) ≠ bảo trì(유지보수, 유상)",
                "explanation": "bảo hành은 보증기간 내 무상이고, bảo trì는 보증기간 후 유상 관리입니다."
            },
            {
                "mistake": "kiểm tra định kỳ = 정기유지보수",
                "correction": "kiểm tra(점검만) < bảo trì(점검+보수+교체)",
                "explanation": "정기유지보수는 점검뿐 아니라 보수, 교체까지 포함하므로 bảo trì가 정확합니다."
            }
        ],
        "examples": [
            {
                "ko": "엘리베이터 정기유지보수 계약을 체결했습니다.",
                "vi": "Đã ký hợp đồng bảo trì định kỳ thang máy.",
                "situation": "formal"
            },
            {
                "ko": "소방설비는 매월 1회 정기유지보수를 실시합니다.",
                "vi": "Hệ thống phòng cháy chữa cháy thực hiện bảo trì định kỳ 1 lần/tháng.",
                "situation": "onsite"
            },
            {
                "ko": "정기유지보수 기록을 보수대장에 작성해주세요.",
                "vi": "Vui lòng ghi chép kết quả bảo trì định kỳ vào sổ bảo trì.",
                "situation": "formal"
            }
        ],
        "relatedTerms": ["ban-giao-cong-trinh", "so-tay-van-hanh", "nghiem-thu-hoan-cong", "ho-so-hoan-cong"]
    },
    {
        "slug": "quyet-toan-cong-trinh",
        "korean": "공사정산",
        "vietnamese": "quyết toán công trình",
        "hanja": "工事精算",
        "hanjaReading": "工(장인 공) + 事(일 사) + 精(정밀할 정) + 算(셈 산)",
        "pronunciation": "꾸옛 또안 꽁 트린",
        "meaningKo": "공사 완료 후 실제 공사비를 최종 확정하는 절차로, 계약금액과 실제 투입 비용을 비교하여 정산합니다. 통역 시 '공사비 정산'은 베트남어로 'quyết toán công trình' 또는 'quyết toán chi phí xây dựng'이며, 한국보다 베트남이 정산 절차가 더 복잡하고 시간이 오래 걸립니다. 베트남에서는 quyết toán 시 thiết kế thay đổi(설계변경), khối lượng tăng giảm(물량 증감), giá vật liệu điều chỉnh(자재 가격 조정) 등을 모두 반영하며, 감사기관(kiểm toán)의 검증을 받아야 하는 경우도 많습니다. 정산 완료 후 công trình mới được coi là hoàn toàn hoàn tất(공사가 완전히 종료된 것으로 간주)됩니다.",
        "meaningVi": "Thủ tục xác định chi phí xây dựng thực tế sau khi hoàn thành công trình, bao gồm đối chiếu giữa giá trị hợp đồng và khối lượng thi công thực tế, điều chỉnh giá vật liệu, thiết bị, nhân công theo quy định. Quyết toán công trình phải có hồ sơ đầy đủ (hợp đồng, biên bản nghiệm thu, biên bản thay đổi thiết kế, chứng từ thanh toán) và có thể cần kiểm toán độc lập đối với công trình sử dụng vốn nhà nước.",
        "context": "준공 후 정산",
        "culturalNote": "한국은 준공 후 1~2개월 내 정산이 완료되지만, 베트남은 공공 공사의 경우 6개월~1년이 걸리는 경우도 많습니다. 베트Nam 공공 공사는 kiểm toán nhà nước(국가감사원)의 감사를 받아야 하며, 정산액이 계약액의 일정 비율(통상 10%)을 초과하면 추가 승인이 필요합니다. 한국은 물가변동 조정이 자동 반영되지만 베트남은 계약서에 명시된 경우만 인정되며, chỉ số giá(물가지수) 증빙 자료를 제출해야 합니다. 베트남에서는 정산 지연 시 lãi suất chậm trả(지연이자)가 발생합니다.",
        "commonMistakes": [
            {
                "mistake": "thanh toán = 정산",
                "correction": "thanh toán(지급) ≠ quyết toán(정산)",
                "explanation": "thanh toán은 중간 대금 지급이고, quyết toán은 최종 확정 정산입니다."
            },
            {
                "mistake": "tính toán công trình",
                "correction": "quyết toán công trình",
                "explanation": "tính toán은 일반 계산이고, quyết toán은 공식 정산 절차를 의미하는 법률 용어입니다."
            },
            {
                "mistake": "정산 = quyết toán / 결산 = quyết toán",
                "correction": "정산(공사) = quyết toán công trình / 결산(회계) = quyết toán tài chính",
                "explanation": "같은 'quyết toán'이지만 công trình(공사)과 tài chính(회계)으로 구분해야 합니다."
            }
        ],
        "examples": [
            {
                "ko": "준공 후 3개월 내에 공사정산을 완료해야 합니다.",
                "vi": "Phải hoàn thành quyết toán công trình trong vòng 3 tháng sau khi hoàn công.",
                "situation": "formal"
            },
            {
                "ko": "설계변경으로 인한 추가 공사비를 공사정산에 반영했습니다.",
                "vi": "Đã phản ánh chi phí thi công bổ sung do thay đổi thiết kế vào quyết toán công trình.",
                "situation": "formal"
            },
            {
                "ko": "국가감사원의 감사를 받은 후 공사정산이 승인되었습니다.",
                "vi": "Quyết toán công trình đã được phê duyệt sau khi kiểm toán nhà nước.",
                "situation": "formal"
            }
        ],
        "relatedTerms": ["nghiem-thu-hoan-cong", "ban-giao-cong-trinh", "ho-so-hoan-cong", "bien-ban-nghiem-thu"]
    }
]

# 중복 제거
new_terms_filtered = [t for t in new_terms if t['slug'] not in existing_slugs]

# 기존 데이터에 추가
data.extend(new_terms_filtered)

# 파일 저장
with open(file_path, 'w', encoding='utf-8') as f:
    json.dump(data, f, ensure_ascii=False, indent=2)

print(f"✅ {len(new_terms_filtered)}개 용어 추가 완료")
print(f"📊 총 용어 수: {len(data)}개")
for term in new_terms_filtered:
    print(f"   - {term['slug']} ({term['korean']})")
