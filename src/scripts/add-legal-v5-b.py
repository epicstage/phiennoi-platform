#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
반부패법/청렴 전문용어 추가 스크립트
Theme: Anti-Corruption/Integrity Law
Target: legal.json (Tier S 품질 기준 준수)
"""

import json
import os
from typing import List, Dict, Any

def load_legal_terms() -> List[Dict[str, Any]]:
    """legal.json 파일 로드"""
    file_path = os.path.join(
        os.path.dirname(os.path.abspath(__file__)),
        '..', 'data', 'terms', 'legal.json'
    )

    with open(file_path, 'r', encoding='utf-8') as f:
        data = json.load(f)

    return data

def save_legal_terms(terms: List[Dict[str, Any]]) -> None:
    """legal.json 파일 저장"""
    file_path = os.path.join(
        os.path.dirname(os.path.abspath(__file__)),
        '..', 'data', 'terms', 'legal.json'
    )

    with open(file_path, 'w', encoding='utf-8') as f:
        json.dump(terms, f, ensure_ascii=False, indent=2)

def filter_duplicates(existing_terms: List[Dict[str, Any]], new_terms: List[Dict[str, Any]]) -> List[Dict[str, Any]]:
    """중복 제거: 기존 slug와 겹치지 않는 용어만 반환"""
    existing_slugs = {term['slug'] for term in existing_terms}
    filtered = [term for term in new_terms if term['slug'] not in existing_slugs]

    if len(filtered) < len(new_terms):
        removed = len(new_terms) - len(filtered)
        print(f"⚠️  중복 제거: {removed}개 용어 스킵")

    return filtered

def create_anti_corruption_terms() -> List[Dict[str, Any]]:
    """반부패법/청렴 전문용어 10개 생성 (Tier S 기준)"""

    terms = [
        {
            "slug": "phong-chong-tham-nhung",
            "korean": "반부패",
            "vietnamese": "Phòng chống tham nhũng",
            "hanja": "反腐敗",
            "hanjaReading": "反(돌이킬 반) 腐(썩을 부) 敗(패할 패)",
            "pronunciation": "퐁쫑탐능",
            "meaningKo": "공직자나 기업이 권력이나 지위를 남용하여 부당한 이익을 취하는 행위를 방지하고 처벌하는 제도와 활동. 통역 시 주의: 베트남에서는 '반부패법(Luật phòng chống tham nhũng)'이 별도로 제정되어 있으며, 한국의 청탁금지법(김영란법)과 유사하지만 처벌 수위와 적용 범위가 다름. 베트남은 당 차원의 반부패 운동이 강력하게 진행되므로 정치적 맥락을 이해하고 통역해야 함. '반부패위원회(Ủy ban Kiểm tra)'는 당 기구이므로 '감사원'과 혼동하지 말 것.",
            "meaningVi": "Hoạt động và chế độ ngăn chặn, xử lý hành vi lạm dụng quyền lực hoặc chức vụ để trục lợi bất chính của công chức hoặc doanh nghiệp. Tại Việt Nam, Luật phòng chống tham nhũng được ban hành riêng và có sự giám sát chặt chẽ từ Đảng.",
            "context": "법률, 공공행정, 기업윤리",
            "culturalNote": "한국은 청탁금지법(김영란법)을 통해 민간 영역까지 규제하며, 금품 수수 한도(100만원, 식사 3만원 등)가 명확함. 베트남은 공산당 주도의 반부패 운동이 강력하며, 고위 공직자 숙청이 정치적 의미를 가질 수 있음. 통역 시 양국의 제도적 차이와 정치적 맥락을 함께 설명해야 오해를 방지할 수 있음. 베트남에서는 'tham nhũng vặt'(소규모 부패)와 'tham nhũng lớn'(대규모 부패)를 구분하여 사용.",
            "commonMistakes": [
                {
                    "mistake": "'반부패'를 'chống tham nhũng'로만 번역",
                    "correction": "'phòng chống tham nhũng' (예방+대응 모두 포함)",
                    "explanation": "'phòng'(예방)과 'chống'(대응)을 함께 써야 제도의 예방적 성격까지 전달됨"
                },
                {
                    "mistake": "김영란법을 그대로 'Luật Kim Young-ran'으로 음역",
                    "correction": "'Luật cấm hối lộ' 또는 'Luật phòng chống tham nhũng Hàn Quốc'",
                    "explanation": "베트남에서는 인명보다 법의 내용을 설명하는 것이 이해도가 높음"
                },
                {
                    "mistake": "반부패위원회를 '감사원'으로 혼동",
                    "correction": "'Ủy ban Kiểm tra'(당 기구) vs 'Kiểm toán Nhà nước'(국가감사원)",
                    "explanation": "베트남은 당과 국가 기구가 분리되어 있으므로 정확한 기관명 사용 필수"
                }
            ],
            "examples": [
                {
                    "ko": "우리 회사는 반부패 정책을 엄격히 준수하며, 모든 임직원에게 연례 교육을 실시합니다.",
                    "vi": "Công ty chúng tôi tuân thủ nghiêm ngặt chính sách phòng chống tham nhũng và tổ chức đào tạo hàng năm cho toàn thể cán bộ nhân viên.",
                    "situation": "formal"
                },
                {
                    "ko": "이 계약 건과 관련해 어떠한 금품 수수도 있어서는 안 됩니다. 반부패법을 철저히 지켜주세요.",
                    "vi": "Không được có bất kỳ hành vi nhận quà biếu nào liên quan đến hợp đồng này. Vui lòng tuân thủ nghiêm luật phòng chống tham nhũng.",
                    "situation": "formal"
                },
                {
                    "ko": "반부패 감사 결과, 일부 부서에서 부적절한 금품 수수가 적발되었습니다.",
                    "vi": "Theo kết quả kiểm tra phòng chống tham nhũng, một số phòng ban đã bị phát hiện có hành vi nhận quà biếu không phù hợp.",
                    "situation": "formal"
                }
            ],
            "relatedTerms": ["hoi-lo", "ke-khai-tai-san", "minh-bach"]
        },
        {
            "slug": "hoi-lo",
            "korean": "뇌물",
            "vietnamese": "Hối lộ",
            "hanja": "賂賄",
            "hanjaReading": "賂(뇌물 뢰) 賄(뇌물 회)",
            "pronunciation": "호이로",
            "meaningKo": "공무원이나 업무 관계자에게 부정한 청탁이나 부당한 이익을 얻기 위해 제공하는 금품이나 향응. 통역 시 주의: 한국은 '뇌물죄'와 '알선수재죄'를 구분하지만, 베트남에서는 'hối lộ'가 더 광범위하게 쓰임. 베트남 형법 제 364조~366조에서 뇌물 공여와 수수를 모두 처벌하며, 공무원 뿐 아니라 기업 임직원 간 상업적 뇌물(뇌물 상업, hối lộ thương mại)도 처벌 대상. 금액 기준과 처벌 수위가 한국과 다르므로 법률 통역 시 조문을 정확히 확인할 것.",
            "meaningVi": "Tiền bạc hoặc hiện vật được đưa cho công chức hoặc người có liên quan trong công việc để nhờ vả không chính đáng hoặc để đạt được lợi ích bất hợp pháp. Tội hối lộ được quy định tại Điều 364-366 Bộ luật Hình sự Việt Nam.",
            "context": "형사법, 기업윤리, 계약",
            "culturalNote": "한국에서는 '떡값', '촌지' 등 완곡한 표현이 있으나 모두 불법. 베트nam에서도 'tiền cảm ơn'(감사금), 'phong bì'(봉투)라는 완곡 표현이 있으나 법적으로는 모두 뇌물. 베트남은 과거 관행적으로 소액 금품(티머니, 담배 등)을 주고받는 문화가 있었으나, 최근 반부패 강화로 엄격히 처벌됨. 통역 시 '관행'과 '불법'을 혼동하지 않도록 주의하고, 법적 책임을 명확히 전달해야 함.",
            "commonMistakes": [
                {
                    "mistake": "'뇌물'을 'tiền'(돈)으로만 번역",
                    "correction": "'hối lộ' (뇌물 행위 전체를 지칭)",
                    "explanation": "'tiền'은 단순히 돈을 의미하며, 뇌물의 법적 의미를 전달하지 못함"
                },
                {
                    "mistake": "'선물'과 '뇌물'을 구분 없이 'quà tặng'로 번역",
                    "correction": "선물은 'quà tặng', 뇌물은 'hối lộ'",
                    "explanation": "법적 맥락에서는 목적과 대가성 여부로 구분해야 함"
                },
                {
                    "mistake": "상업적 뇌물을 일반 뇌물과 동일하게 표현",
                    "correction": "'hối lộ thương mại' (commercial bribery)",
                    "explanation": "베트남은 공무원 대상 뇌물과 민간 기업 간 뇌물을 구분하여 처벌"
                }
            ],
            "examples": [
                {
                    "ko": "공무원에게 뇌물을 제공하면 형사처벌 대상이 됩니다.",
                    "vi": "Nếu đưa hối lộ cho công chức sẽ bị truy cứu trách nhiệm hình sự.",
                    "situation": "formal"
                },
                {
                    "ko": "이 거래에서 어떠한 형태의 뇌물도 주고받지 않았음을 확인합니다.",
                    "vi": "Xác nhận rằng không có bất kỳ hình thức hối lộ nào trong giao dịch này.",
                    "situation": "formal"
                },
                {
                    "ko": "뇌물 공여 혐의로 조사를 받고 있습니다.",
                    "vi": "Đang bị điều tra về tội đưa hối lộ.",
                    "situation": "formal"
                }
            ],
            "relatedTerms": ["phong-chong-tham-nhung", "loi-dung-chuc-vu", "tham-o-tai-san"]
        },
        {
            "slug": "ke-khai-tai-san",
            "korean": "재산신고",
            "vietnamese": "Kê khai tài sản",
            "hanja": "財產申告",
            "hanjaReading": "財(재물 재) 產(날 산) 申(베풀 신) 告(고할 고)",
            "pronunciation": "껴카이타이산",
            "meaningKo": "공직자나 특정 직위에 있는 사람이 자신과 가족의 재산 내역을 국가 기관에 공개적으로 보고하는 의무. 통역 시 주의: 한국은 공직자윤리법에 따라 일정 직급 이상 공직자와 배우자, 직계존비속의 재산을 신고하며, 재산 등록 대상자는 매년 정기 신고와 변동 신고를 해야 함. 베트남도 유사한 제도가 있으나, 신고 범위와 공개 수준이 한국과 다름. 베트남은 'Kê khai tài sản thu nhập'(재산소득신고)로 부르며, 당 간부와 고위 공직자에게 적용. 통역 시 양국의 신고 주기, 대상 범위, 공개 여부를 명확히 구분할 것.",
            "meaningVi": "Nghĩa vụ công khai báo cáo chi tiết tài sản của bản thân và gia đình lên cơ quan nhà nước đối với công chức hoặc người giữ chức vụ nhất định. Tại Việt Nam được quy định trong Luật phòng chống tham nhũng và áp dụng cho cán bộ, đảng viên cấp cao.",
            "context": "공직자윤리, 행정법, 투명성",
            "culturalNote": "한국은 재산신고 내용이 일부 공개되며, 국민권익위원회에서 관리함. 신고 대상은 4급 이상 공무원, 법관, 경찰간부 등이며, 미신고 시 과태료와 징계. 베트남은 당 규율과 법률이 함께 작동하며, 재산 출처를 설명하지 못하면 부패 혐의로 조사받을 수 있음. 통역 시 '신고'와 '공개'의 차이, '의무 대상자' 범위를 정확히 전달해야 함. 베트남에서는 재산신고 거부나 허위신고가 당 규율 위반으로 더 엄하게 다뤄질 수 있음.",
            "commonMistakes": [
                {
                    "mistake": "'재산신고'를 'khai báo tài sản'으로 번역",
                    "correction": "'kê khai tài sản' (공식 용어)",
                    "explanation": "'kê khai'가 법적 신고 절차를 정확히 나타내는 공식 표현"
                },
                {
                    "mistake": "신고와 공개를 구분하지 않고 번역",
                    "correction": "신고는 'kê khai', 공개는 'công khai'",
                    "explanation": "재산신고는 의무이고, 공개는 별도의 투명성 조치"
                },
                {
                    "mistake": "'재산 등록'과 '재산신고'를 동일하게 표현",
                    "correction": "등록은 'đăng ký tài sản', 신고는 'kê khai tài sản'",
                    "explanation": "등록은 소유권 기록, 신고는 윤리적 투명성 확보 목적"
                }
            ],
            "examples": [
                {
                    "ko": "공직 임용 시 재산신고를 의무적으로 해야 합니다.",
                    "vi": "Khi được bổ nhiệm vào vị trí công chức, phải thực hiện kê khai tài sản bắt buộc.",
                    "situation": "formal"
                },
                {
                    "ko": "재산신고 내용에 허위가 있을 경우 처벌받을 수 있습니다.",
                    "vi": "Nếu kê khai tài sản không trung thực có thể bị xử lý kỷ luật hoặc truy cứu trách nhiệm.",
                    "situation": "formal"
                },
                {
                    "ko": "매년 정기적으로 재산신고를 갱신해야 합니다.",
                    "vi": "Phải cập nhật kê khai tài sản định kỳ hàng năm.",
                    "situation": "formal"
                }
            ],
            "relatedTerms": ["phong-chong-tham-nhung", "minh-bach", "loi-ich-nhom"]
        },
        {
            "slug": "loi-ich-nhom",
            "korean": "이해충돌",
            "vietnamese": "Lợi ích nhóm",
            "hanja": "利害衝突",
            "hanjaReading": "利(이로울 이) 害(해할 해) 衝(찌를 충) 突(돌출할 돌)",
            "pronunciation": "러이익넘",
            "meaningKo": "공직자나 업무 담당자가 공적 업무를 수행하면서 자신 또는 특정 집단의 사적 이익과 공적 이익이 충돌하는 상황. 통역 시 주의: 한국은 '공직자의 이해충돌 방지법'이 2022년 시행되어 직무 관련 사적 이익 추구를 금지함. 베트남에서는 'lợi ích nhóm'(집단 이익) 또는 'xung đột lợi ích'(이익 충돌)로 표현하며, 당 규율과 반부패법에서 규제. 통역 시 '이해관계자'(người có liên quan)와 '이해충돌'을 구분하고, 베트남에서는 가족, 친인척 관련 업무 회피 의무가 강조됨을 설명할 것.",
            "meaningVi": "Tình huống mà công chức hoặc người thực hiện công vụ có lợi ích cá nhân hoặc của nhóm xung đột với lợi ích công. Tại Việt Nam được quy định trong Luật phòng chống tham nhũng và các quy định của Đảng, nhấn mạnh nghĩa vụ tránh làm việc liên quan đến gia đình hoặc người thân.",
            "context": "공직자윤리, 기업지배구조, 계약",
            "culturalNote": "한국은 이해충돌방지법으로 공직자의 사적 이익 추구, 가족 채용, 업무 관련 거래를 제한하며, 위반 시 형사처벌 또는 징계. 베트남은 당 규율이 우선하며, '집단 이익'(lợi ích nhóm)이라는 표현으로 파벌주의와 연결되어 정치적으로 민감할 수 있음. 통역 시 '개인의 이익 충돌'과 '집단 이익 추구'를 구분하고, 베트남에서는 가족 관계 공개와 업무 회피가 더욱 엄격함을 설명할 것. 한국은 사전 신고 제도가 있으나, 베트남은 사후 적발 시 처벌이 강함.",
            "commonMistakes": [
                {
                    "mistake": "'이해충돌'을 'xung đột'로만 번역",
                    "correction": "'xung đột lợi ích' 또는 'lợi ích nhóm'",
                    "explanation": "'xung đột'만으로는 단순한 갈등으로 오해될 수 있음"
                },
                {
                    "mistake": "'이해관계자'와 '이해충돌'을 혼동",
                    "correction": "이해관계자는 'bên liên quan', 이해충돌은 'xung đột lợi ích'",
                    "explanation": "이해관계자는 중립적 용어, 이해충돌은 윤리 위반 상황"
                },
                {
                    "mistake": "'lợi ích nhóm'을 단순히 '집단 이익'으로만 이해",
                    "correction": "베트남에서는 부패와 파벌주의의 맥락으로 사용됨",
                    "explanation": "정치적으로 민감한 표현이므로 맥락에 따라 신중히 사용"
                }
            ],
            "examples": [
                {
                    "ko": "이 계약 건에서 귀하는 이해충돌 상황에 해당하므로 업무에서 제외됩니다.",
                    "vi": "Trong hợp đồng này, ông/bà có xung đột lợi ích nên phải tránh tham gia công việc này.",
                    "situation": "formal"
                },
                {
                    "ko": "이해충돌 방지를 위해 모든 임직원은 가족 관계를 사전에 신고해야 합니다.",
                    "vi": "Để phòng ngừa xung đột lợi ích, toàn thể cán bộ nhân viên phải kê khai trước các mối quan hệ gia đình.",
                    "situation": "formal"
                },
                {
                    "ko": "이해충돌 신고서를 작성하여 제출해 주시기 바랍니다.",
                    "vi": "Vui lòng lập và nộp tờ khai xung đột lợi ích.",
                    "situation": "formal"
                }
            ],
            "relatedTerms": ["ke-khai-tai-san", "minh-bach", "phong-chong-tham-nhung"]
        },
        {
            "slug": "to-cao",
            "korean": "내부고발",
            "vietnamese": "Tố cáo",
            "hanja": "內部告發",
            "hanjaReading": "內(안 내) 部(부분 부) 告(고할 고) 發(필 발)",
            "pronunciation": "또까오",
            "meaningKo": "조직 내부에서 위법하거나 비윤리적인 행위를 발견한 구성원이 외부 기관이나 언론에 알리는 행위. 통역 시 주의: 한국은 '공익신고자 보호법'으로 내부고발자를 보호하며, '신고'와 '고발'을 구분함. 베트남에서는 'tố cáo'가 일반적이며, '고소(khiếu nại)', '탄원(kiến nghị)'과 구분됨. 베트남 반부패법과 고소고발법(Luật Khiếu nại, Tố cáo)에서 절차를 규정하며, 익명 고발도 가능하나 증거가 필요함. 통역 시 '내부고발'과 '제보', '신고'의 뉘앙스를 구분하고, 베트남에서는 당 기구와 국가 기관 중 어디에 고발하는지가 중요함을 설명할 것.",
            "meaningVi": "Hành vi thông báo cho cơ quan bên ngoài hoặc báo chí về hành vi vi phạm pháp luật hoặc phi đạo đức mà thành viên trong tổ chức phát hiện. Tại Việt Nam được quy định trong Luật Khiếu nại, Tố cáo và Luật phòng chống tham nhũng, bảo vệ quyền lợi của người tố cáo.",
            "context": "공익신고, 기업윤리, 형사소송",
            "culturalNote": "한국은 내부고발자 보호제도가 발달했으며, 보복 조치 금지, 신분 보장, 포상금 제도가 있음. 베트남은 'tố cáo'가 전통적으로 정치적 고발의 의미도 있어 민감할 수 있으나, 최근 반부패 강화로 장려됨. 통역 시 한국의 '공익신고자'와 베트남의 'người tố cáo'가 보호 수준과 절차에서 차이가 있음을 설명하고, 베트남에서는 익명 고발이 가능하나 악의적 허위 고발 시 처벌받을 수 있음을 주의할 것. 조직 내 고발과 외부 고발의 순서도 중요함.",
            "commonMistakes": [
                {
                    "mistake": "'내부고발'을 'báo cáo nội bộ'로 번역",
                    "correction": "'tố cáo' (공식 고발 절차)",
                    "explanation": "'báo cáo'는 단순 보고, 'tố cáo'는 법적 고발 행위"
                },
                {
                    "mistake": "'tố cáo'를 '고소'로만 번역",
                    "correction": "고소는 'khiếu nại', 고발은 'tố cáo'",
                    "explanation": "고소는 개인 권리 침해, 고발은 공익 침해 신고"
                },
                {
                    "mistake": "'제보'와 '내부고발'을 구분 없이 사용",
                    "correction": "제보는 'thông tin', 내부고발은 'tố cáo'",
                    "explanation": "제보는 비공식 정보 제공, 내부고발은 법적 절차"
                }
            ],
            "examples": [
                {
                    "ko": "회사의 불법 행위를 내부고발하여 조사가 시작되었습니다.",
                    "vi": "Sau khi tố cáo hành vi vi phạm pháp luật của công ty, cuộc điều tra đã được tiến hành.",
                    "situation": "formal"
                },
                {
                    "ko": "내부고발자의 신원은 철저히 보호됩니다.",
                    "vi": "Danh tính của người tố cáo được bảo vệ nghiêm ngặt.",
                    "situation": "formal"
                },
                {
                    "ko": "익명으로 내부고발할 수 있는 시스템을 운영하고 있습니다.",
                    "vi": "Chúng tôi vận hành hệ thống tố cáo ẩn danh.",
                    "situation": "formal"
                }
            ],
            "relatedTerms": ["bao-ve-nguoi-to-cao", "phong-chong-tham-nhung", "minh-bach"]
        },
        {
            "slug": "bao-ve-nguoi-to-cao",
            "korean": "내부고발자보호",
            "vietnamese": "Bảo vệ người tố cáo",
            "hanja": "內部告發者保護",
            "hanjaReading": "內(안 내) 部(부분 부) 告(고할 고) 發(필 발) 者(사람 자) 保(지킬 보) 護(지킬 호)",
            "pronunciation": "바오베응으으이또까오",
            "meaningKo": "조직 내부의 위법 행위를 신고한 사람이 신고로 인해 불이익을 받지 않도록 법적으로 보호하는 제도. 통역 시 주의: 한국은 '공익신고자 보호법'으로 해고, 전보, 차별 등 불이익 조치를 금지하며, 위반 시 사용자에게 형사처벌과 징벌적 손해배상 부과. 베트남도 반부패법과 고소고발법에서 보호 조항이 있으나, 실제 보호 수준은 한국보다 약할 수 있음. 통역 시 '신분 보호', '보복 금지', '포상금'을 구분하여 설명하고, 베트남에서는 익명 보장과 함께 허위 고발 시 처벌도 엄격함을 주의할 것.",
            "meaningVi": "Chế độ bảo vệ pháp lý người đã báo cáo hành vi vi phạm trong tổ chức, đảm bảo họ không bị thiệt hại do hành động tố cáo. Luật phòng chống tham nhũng và Luật Khiếu nại, Tố cáo Việt Nam có quy định bảo vệ, nhưng mức độ thực thi có thể khác với Hàn Quốc.",
            "context": "노동법, 공익신고, 기업윤리",
            "culturalNote": "한국은 내부고발자 보호가 법적으로 강력하며, 국민권익위원회가 전담 기구로 운영됨. 불이익 조치에는 해고, 전보, 감봉, 차별이 포함되며, 입증 책임이 사용자에게 있음. 베트남은 법적 보호 조항이 있으나, 실제 조직 문화에서 내부고발이 '배신'으로 여겨질 수 있어 심리적 장벽이 높음. 통역 시 한국의 보호 수준(포상금, 신분 보장, 변호사 지원 등)과 베트남의 현실적 한계를 함께 설명하고, 베트남 기업에서는 내부 신고 채널(whistleblowing system)을 먼저 운영하도록 권장함을 전달할 것.",
            "commonMistakes": [
                {
                    "mistake": "'내부고발자 보호'를 'bảo vệ người báo cáo'로 번역",
                    "correction": "'bảo vệ người tố cáo' (공식 법률 용어)",
                    "explanation": "'tố cáo'가 법적 고발을 정확히 나타냄"
                },
                {
                    "mistake": "보호 조치를 나열만 하고 실효성을 설명하지 않음",
                    "correction": "한국과 베트남의 보호 수준 차이를 명확히 전달",
                    "explanation": "법 조항과 실제 실행 수준이 다를 수 있음을 통역 시 주의"
                },
                {
                    "mistake": "'익명 보장'과 '신분 보호'를 혼용",
                    "correction": "익명은 'ẩn danh', 신분 보호는 'bảo vệ danh tính'",
                    "explanation": "익명은 이름을 밝히지 않음, 신분 보호는 보복 금지"
                }
            ],
            "examples": [
                {
                    "ko": "내부고발자 보호법에 따라 신고자에게 어떠한 불이익도 줄 수 없습니다.",
                    "vi": "Theo luật bảo vệ người tố cáo, không được gây bất kỳ thiệt hại nào cho người báo cáo.",
                    "situation": "formal"
                },
                {
                    "ko": "내부고발로 인한 해고나 전보는 무효이며, 원상회복 조치가 이루어집니다.",
                    "vi": "Việc sa thải hoặc điều chuyển do tố cáo là vô hiệu và phải có biện pháp khôi phục nguyên trạng.",
                    "situation": "formal"
                },
                {
                    "ko": "내부고발자에게는 포상금이 지급될 수 있습니다.",
                    "vi": "Người tố cáo có thể được nhận tiền thưởng.",
                    "situation": "formal"
                }
            ],
            "relatedTerms": ["to-cao", "phong-chong-tham-nhung", "kiem-soat-quyen-luc"]
        },
        {
            "slug": "minh-bach",
            "korean": "투명성",
            "vietnamese": "Minh bạch",
            "hanja": "透明性",
            "hanjaReading": "透(통할 투) 明(밝을 명) 性(성품 성)",
            "pronunciation": "밍박",
            "meaningKo": "조직이나 정부의 의사결정, 재정, 업무 처리 과정이 외부에 공개되고 누구나 확인할 수 있는 상태. 통역 시 주의: 한국은 '정보공개법'과 '공공데이터법'으로 행정 투명성을 제도화하며, 국민 누구나 정보공개를 청구할 수 있음. 베트남도 '정보접근법(Luật Tiếp cận thông tin)'이 있으나, 국가 안보나 당 정책과 관련된 정보는 제한됨. 통역 시 '공개(công khai)'와 '투명(minh bạch)'의 차이를 설명하고, 베트남에서는 정부 투명성과 기업 투명성의 수준이 다를 수 있음을 주의할 것. '투명 경영'은 'quản trị minh bạch'로 표현.",
            "meaningVi": "Trạng thái mà quy trình ra quyết định, tài chính và xử lý công việc của tổ chức hoặc chính phủ được công khai và bất kỳ ai cũng có thể xác minh. Việt Nam có Luật Tiếp cận thông tin nhưng có giới hạn về an ninh quốc gia và chính sách của Đảng.",
            "context": "기업지배구조, 행정법, 공공정책",
            "culturalNote": "한국은 정보공개 청구제도가 활성화되어 있으며, 공공기관의 예산, 계약, 인사 정보를 누구나 열람 가능. 베트남은 투명성 강화를 추진 중이나, 당과 정부의 정책 결정 과정은 공개되지 않을 수 있음. 통역 시 한국의 '알 권리'와 베트남의 '공개 범위'가 다름을 설명하고, 기업에서는 재무제표 공시, 이사회 의사록 공개 등 구체적 조치를 예로 들 것. 베트남에서는 '투명성'이 반부패와 밀접하게 연결되어 정치적 의미를 가질 수 있음을 주의.",
            "commonMistakes": [
                {
                    "mistake": "'투명성'을 'trong suốt'로 번역",
                    "correction": "'minh bạch' (공식 행정/경영 용어)",
                    "explanation": "'trong suốt'는 물리적 투명함, 'minh bạch'는 제도적 투명성"
                },
                {
                    "mistake": "'공개'와 '투명성'을 구분 없이 사용",
                    "correction": "공개는 'công khai', 투명성은 'minh bạch'",
                    "explanation": "공개는 행위, 투명성은 상태와 원칙"
                },
                {
                    "mistake": "투명성을 단순히 '정보 제공'으로만 이해",
                    "correction": "투명성은 검증 가능성과 책임성까지 포함",
                    "explanation": "정보가 공개되고 누구나 확인하고 감시할 수 있어야 투명성"
                }
            ],
            "examples": [
                {
                    "ko": "우리 회사는 경영 투명성을 높이기 위해 모든 재무 정보를 공개합니다.",
                    "vi": "Công ty chúng tôi công khai toàn bộ thông tin tài chính để nâng cao tính minh bạch trong quản trị.",
                    "situation": "formal"
                },
                {
                    "ko": "정부의 투명성은 국민의 신뢰를 얻는 기본 조건입니다.",
                    "vi": "Tính minh bạch của chính phủ là điều kiện cơ bản để có được sự tin tưởng của người dân.",
                    "situation": "formal"
                },
                {
                    "ko": "투명한 의사결정 과정을 통해 부패를 방지할 수 있습니다.",
                    "vi": "Có thể phòng ngừa tham nhũng thông qua quy trình ra quyết định minh bạch.",
                    "situation": "formal"
                }
            ],
            "relatedTerms": ["phong-chong-tham-nhung", "ke-khai-tai-san", "kiem-soat-quyen-luc"]
        },
        {
            "slug": "kiem-soat-quyen-luc",
            "korean": "권력감시",
            "vietnamese": "Kiểm soát quyền lực",
            "hanja": "權力監視",
            "hanjaReading": "權(권세 권) 力(힘 력) 監(볼 감) 視(볼 시)",
            "pronunciation": "끼엠쏘앗꾸엔력",
            "meaningKo": "국가나 조직의 권력 행사가 법과 원칙에 따라 이루어지는지 감독하고 견제하는 활동. 통역 시 주의: 한국은 삼권분립에 따른 상호 견제, 감사원, 국민권익위원회, 언론의 감시 기능이 있음. 베트남은 당의 지도 아래 국회, 조국전선, 감사원이 감시 기능을 수행하지만, 당 자체는 감시 대상이 아님. 통역 시 '견제(kiềm chế)'와 '감시(giám sát, kiểm soát)'를 구분하고, 베트남에서는 '인민 감독(giám sát của nhân dân)'과 '국가 기관 감사(kiểm tra, kiểm soát)'를 구분할 것. 정치적으로 민감할 수 있으므로 맥락을 신중히 파악할 것.",
            "meaningVi": "Hoạt động giám sát và kiềm chế việc thực thi quyền lực của nhà nước hoặc tổ chính theo pháp luật và nguyên tắc. Tại Việt Nam, Quốc hội, Mặt trận Tổ quốc, Kiểm toán Nhà nước thực hiện chức năng giám sát dưới sự lãnh đạo của Đảng.",
            "context": "헌법, 정치학, 행정감시",
            "culturalNote": "한국은 입법·사법·행정부의 상호 견제와 함께 시민사회, 언론의 독립적 감시가 활발함. 베트남은 공산당 지도 체제에서 국회와 조국전선이 형식적으로 감시 기능을 하지만, 당의 결정에는 이의를 제기하기 어려움. 통역 시 한국의 '권력분립'과 베트남의 '민주집중제'를 혼동하지 말고, 베트남에서는 '인민 감독'이 제도적으로 강조되지만 실효성은 제한적임을 이해할 것. 기업 맥락에서는 '내부통제(kiểm soát nội bộ)', '이사회 감독(giám sát hội đồng quản trị)'으로 표현.",
            "commonMistakes": [
                {
                    "mistake": "'권력감시'를 'giám sát quyền lực'로만 번역",
                    "correction": "'kiểm soát quyền lực' (통제 의미 포함)",
                    "explanation": "'giám sát'은 관찰, 'kiểm soát'은 견제와 통제까지 포함"
                },
                {
                    "mistake": "'견제'와 '감시'를 구분 없이 사용",
                    "correction": "견제는 'kiềm chế', 감시는 'giám sát/kiểm soát'",
                    "explanation": "견제는 권력 간 균형, 감시는 외부의 관찰과 통제"
                },
                {
                    "mistake": "한국식 권력분립을 베트남에 그대로 적용",
                    "correction": "베트남은 당 지도 체제이므로 감시 구조가 다름을 설명",
                    "explanation": "정치 체제 차이를 이해하지 못하면 오해 발생"
                }
            ],
            "examples": [
                {
                    "ko": "효과적인 권력감시를 위해 독립적인 감사 기구가 필요합니다.",
                    "vi": "Cần có cơ quan kiểm toán độc lập để kiểm soát quyền lực hiệu quả.",
                    "situation": "formal"
                },
                {
                    "ko": "시민사회의 권력감시 활동이 민주주의를 강화합니다.",
                    "vi": "Hoạt động giám sát quyền lực của xã hội dân sự làm củng cố dân chủ.",
                    "situation": "formal"
                },
                {
                    "ko": "이사회는 경영진에 대한 권력감시 기능을 수행합니다.",
                    "vi": "Hội đồng quản trị thực hiện chức năng kiểm soát quyền lực đối với ban điều hành.",
                    "situation": "formal"
                }
            ],
            "relatedTerms": ["minh-bach", "phong-chong-tham-nhung", "to-cao"]
        },
        {
            "slug": "loi-dung-chuc-vu",
            "korean": "직권남용",
            "vietnamese": "Lợi dụng chức vụ",
            "hanja": "職權濫用",
            "hanjaReading": "職(직분 직) 權(권세 권) 濫(넘칠 람) 用(쓸 용)",
            "pronunciation": "러이증축부",
            "meaningKo": "공무원이나 업무 담당자가 자신의 직위와 권한을 법이나 규정에 어긋나게 사용하여 사적 이익을 취하거나 타인에게 피해를 주는 행위. 통역 시 주의: 한국 형법 제123조(직권남용)와 제124조(불법체포·감금)에서 규정하며, 공무원의 권한 일탈이나 권한 남용을 처벌. 베트남 형법 제356조~358조에서 'Lạm dụng chức vụ quyền hạn'(직무권한 남용)으로 규정. 통역 시 '권한 일탈'과 '권한 남용'을 구분하고, 베트남에서는 당 간부의 직권남용도 당 규율로 처벌됨을 설명할 것.",
            "meaningVi": "Hành vi công chức hoặc người có chức vụ sử dụng chức vụ và quyền hạn trái với pháp luật hoặc quy định để trục lợi cá nhân hoặc gây thiệt hại cho người khác. Được quy định tại Điều 356-358 Bộ luật Hình sự Việt Nam.",
            "context": "형법, 공직자윤리, 행정소송",
            "culturalNote": "한국은 직권남용죄가 공무원 범죄로 엄격히 처벌되며, 징역형과 함께 공직에서 영구 배제될 수 있음. 베트남도 유사하게 처벌하나, 당 간부의 경우 당 규율이 먼저 적용된 후 형사처벌이 이루어질 수 있음. 통역 시 '직권남용'과 '업무상 배임'을 구분하고, 베트남에서는 직권남용이 부패(tham nhũng)와 밀접하게 연결되어 있음을 설명할 것. 기업에서는 '권한 초과(vượt quá thẩm quyền)'와 '직권남용'을 구분하여 사용.",
            "commonMistakes": [
                {
                    "mistake": "'직권남용'을 'sử dụng chức vụ'로만 번역",
                    "correction": "'lợi dụng chức vụ' 또는 'lạm dụng chức vụ quyền hạn'",
                    "explanation": "'lợi dụng/lạm dụng'이 남용의 의미를 정확히 전달"
                },
                {
                    "mistake": "'권한 일탈'과 '직권남용'을 구분 없이 사용",
                    "correction": "일탈은 'vượt quá thẩm quyền', 남용은 'lạm dụng'",
                    "explanation": "일탈은 권한 초과, 남용은 사적 이익 추구"
                },
                {
                    "mistake": "'업무상 배임'과 '직권남용'을 혼동",
                    "correction": "배임은 'lạm quyền', 직권남용은 'lợi dụng chức vụ'",
                    "explanation": "배임은 재산상 손해, 직권남용은 권한의 불법 사용"
                }
            ],
            "examples": [
                {
                    "ko": "공무원이 직권을 남용하여 특정 업체에 특혜를 준 사실이 밝혀졌습니다.",
                    "vi": "Đã phát hiện công chức lợi dụng chức vụ để ưu đãi cho doanh nghiệp cụ thể.",
                    "situation": "formal"
                },
                {
                    "ko": "직권남용죄로 징역 3년을 선고받았습니다.",
                    "vi": "Bị tuyên án 3 năm tù về tội lạm dụng chức vụ quyền hạn.",
                    "situation": "formal"
                },
                {
                    "ko": "직권을 남용하여 부당한 이익을 얻은 경우 처벌됩니다.",
                    "vi": "Nếu lợi dụng chức vụ để thu lợi bất chính sẽ bị xử lý.",
                    "situation": "formal"
                }
            ],
            "relatedTerms": ["hoi-lo", "tham-o-tai-san", "phong-chong-tham-nhung"]
        },
        {
            "slug": "tham-o-tai-san",
            "korean": "횡령",
            "vietnamese": "Tham ô tài sản",
            "hanja": "橫領",
            "hanjaReading": "橫(가로 횡) 領(거느릴 령)",
            "pronunciation": "탐오타이산",
            "meaningKo": "업무상 보관하거나 관리하는 타인의 재산을 불법적으로 자기 것으로 만드는 행위. 통역 시 주의: 한국 형법 제355조~제357조에서 횡령죄와 업무상횡령죄를 구분하며, 공무원의 경우 가중처벌. 베트남 형법 제353조에서 'Tham ô tài sản'(재산 횡령)으로 규정하며, 공무원과 기업 임직원 모두 적용. 통역 시 '횡령(tham ô)'과 '배임(vi phạm tín nhiệm)'을 구분하고, 베트남에서는 공금 횡령이 특히 엄격히 처벌됨을 설명할 것. 횡령액 규모에 따라 처벌 수위가 달라지므로 금액 기준을 정확히 전달할 것.",
            "meaningVi": "Hành vi chiếm đoạt tài sản của người khác mà mình đang giữ hoặc quản lý trong công việc một cách bất hợp pháp. Được quy định tại Điều 353 Bộ luật Hình sự Việt Nam, áp dụng cho cả công chức và nhân viên doanh nghiệp.",
            "context": "형법, 재산범죄, 기업윤리",
            "culturalNote": "한국은 횡령죄를 친고죄로 규정하여 피해자가 고소해야 처벌 가능하나, 업무상횡령은 비친고죄. 베트남은 모두 비친고죄이며, 공금 횡령 시 사형까지 선고 가능. 통역 시 한국의 '횡령'과 '배임'의 구분(재산 영득 여부)을 설명하고, 베트남에서는 횡령액이 클수록 처벌이 엄격함을 주의할 것. 기업에서는 '내부통제 실패'와 '횡령'을 함께 다루며, 예방 조치(giám sát nội bộ, kiểm soát tài chính)를 강조.",
            "commonMistakes": [
                {
                    "mistake": "'횡령'을 'lấy cắp tài sản'(절도)으로 번역",
                    "correction": "'tham ô tài sản' (보관 중인 재산의 불법 영득)",
                    "explanation": "절도는 타인의 재산을 훔침, 횡령은 위탁받은 재산을 차지함"
                },
                {
                    "mistake": "'횡령'과 '배임'을 구분 없이 사용",
                    "correction": "횡령은 'tham ô', 배임은 'vi phạm tín nhiệm'",
                    "explanation": "횡령은 재산 영득, 배임은 신임 위반으로 손해 발생"
                },
                {
                    "mistake": "공금횡령과 일반횡령을 동일하게 표현",
                    "correction": "공금횡령은 'tham ô tài sản công', 일반횡령은 'tham ô tài sản'",
                    "explanation": "공금횡령은 가중 처벌되므로 구분 필수"
                }
            ],
            "examples": [
                {
                    "ko": "회사 자금을 횡령한 혐의로 기소되었습니다.",
                    "vi": "Bị truy tố về tội tham ô tài sản của công ty.",
                    "situation": "formal"
                },
                {
                    "ko": "횡령 금액이 10억 원을 넘어 가중처벌 대상입니다.",
                    "vi": "Số tiền tham ô vượt quá 1 tỷ won nên thuộc diện xử lý nặng.",
                    "situation": "formal"
                },
                {
                    "ko": "횡령 방지를 위해 내부통제 시스템을 강화했습니다.",
                    "vi": "Đã tăng cường hệ thống kiểm soát nội bộ để phòng ngừa tham ô.",
                    "situation": "formal"
                }
            ],
            "relatedTerms": ["loi-dung-chuc-vu", "hoi-lo", "phong-chong-tham-nhung"]
        }
    ]

    return terms

def main():
    """메인 실행 함수"""
    print("🚀 반부패법/청렴 전문용어 추가 시작...\n")

    # 1. 기존 용어 로드
    existing_terms = load_legal_terms()
    print(f"✅ 기존 용어 로드 완료: {len(existing_terms)}개\n")

    # 2. 새 용어 생성
    new_terms = create_anti_corruption_terms()
    print(f"✅ 새 용어 생성 완료: {len(new_terms)}개\n")

    # 3. 중복 필터링
    filtered_terms = filter_duplicates(existing_terms, new_terms)
    print(f"✅ 중복 필터링 완료: {len(filtered_terms)}개 추가 가능\n")

    if not filtered_terms:
        print("⚠️  추가할 용어 없음 (모두 중복)")
        return

    # 4. 용어 추가
    existing_terms.extend(filtered_terms)

    # 5. 저장
    save_legal_terms(existing_terms)
    print(f"✅ legal.json 저장 완료: 총 {len(existing_terms)}개 용어\n")

    # 6. 추가된 용어 목록 출력
    print("📋 추가된 용어:")
    for term in filtered_terms:
        print(f"  - {term['slug']}: {term['korean']} ({term['vietnamese']})")

    print("\n🎉 완료! 다음 명령어로 검증하세요:")
    print("   npm run validate:terms")

if __name__ == "__main__":
    main()
