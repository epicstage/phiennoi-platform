#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
건설(Construction) 용어 추가 스크립트
테마: 원가/견적 (Cost & Estimation)
Tier S 품질 기준 (90점 이상)
"""

import json
import os

# 추가할 용어 데이터 (10개)
data = [
    {
        "slug": "thuc-hanh-ngan-sach",
        "korean": "실행예산",
        "vietnamese": "Thực hành ngân sách",
        "hanja": "實行豫算",
        "hanjaReading": "實(열매 실) + 行(다닐 행) + 豫(미리 예) + 算(셈 산)",
        "pronunciation": "시행예산 (일반적으로 실행예산으로 발음)",
        "meaningKo": "공사 계약 후 실제 시공을 위해 세부적으로 편성하는 예산. 계약금액을 기준으로 공종별, 공정별로 구체적인 비용을 배분하여 원가관리의 기준이 되는 예산을 말합니다. 통역 시 '견적'과 혼동하지 않도록 주의해야 하며, 베트남 현장에서는 '실행'보다 '실제 집행 예산'으로 풀어 설명하는 것이 이해가 빠릅니다. 한국 건설사는 실행예산 대비 원가절감을 중요 KPI로 관리하므로, 회의에서 자주 언급되는 용어입니다.",
        "meaningVi": "Ngân sách được lập chi tiết sau khi ký hợp đồng để triển khai thi công thực tế. Đây là ngân sách cụ thể được phân bổ theo từng hạng mục công việc và tiến độ thi công, dựa trên số tiền hợp đồng, và trở thành cơ sở quản lý chi phí. Trong thực tế, đây là công cụ quản lý chi phí quan trọng nhất của nhà thầu Hàn Quốc.",
        "context": "원가관리, 예산편성, 공사관리, 회계",
        "culturalNote": "한국 건설사는 계약 직후 실행예산을 상세히 수립하고 매월 집행률을 점검하는 체계적인 원가관리 문화가 있습니다. 베트남 현장에서는 이러한 세밀한 예산관리 개념이 생소할 수 있으므로, '예산 대비 실제 지출 관리 계획'으로 풀어 설명하면 효과적입니다. 한국 본사는 실행예산 대비 실제 원가를 매월 보고받아 수익성을 관리합니다.",
        "commonMistakes": [
            {
                "mistake": "dự toán (견적)",
                "correction": "thực hành ngân sách 또는 ngân sách thi công thực tế",
                "explanation": "dự toán은 입찰 전 견적을 의미하고, 실행예산은 계약 후 실제 시공을 위한 세부 예산이므로 구분 필요"
            },
            {
                "mistake": "ngân sách dự án (프로젝트 예산)",
                "correction": "ngân sách thi công chi tiết (세부 시공 예산)",
                "explanation": "프로젝트 전체 예산이 아닌, 시공단계의 구체적 집행 예산임을 명확히 해야 함"
            },
            {
                "mistake": "kế hoạch chi phí (비용 계획)",
                "correction": "ngân sách quản lý chi phí thi công (시공원가 관리 예산)",
                "explanation": "단순 계획이 아닌 원가관리 목적의 상세 예산임을 강조해야 정확함"
            }
        ],
        "examples": [
            {
                "ko": "실행예산을 기준으로 매월 원가 집행률을 점검하겠습니다.",
                "vi": "Chúng tôi sẽ kiểm tra tỷ lệ chi tiêu chi phí hàng tháng dựa trên ngân sách thi công thực tế.",
                "situation": "formal"
            },
            {
                "ko": "자재비가 실행예산을 10% 초과했으니 절감 방안을 마련해 주세요.",
                "vi": "Chi phí vật liệu đã vượt ngân sách thi công 10%, vui lòng đưa ra phương án tiết giảm.",
                "situation": "onsite"
            },
            {
                "ko": "실행예산 대비 실제 원가 차이를 분석하는 게 중요해요.",
                "vi": "Việc phân tích chênh lệch giữa chi phí thực tế và ngân sách thi công rất quan trọng.",
                "situation": "informal"
            }
        ],
        "relatedTerms": ["공사원가", "견적", "원가관리", "예산편성", "집행률"]
    },
    {
        "slug": "chi-phi-thi-cong",
        "korean": "공사원가",
        "vietnamese": "Chi phí thi công",
        "hanja": "工事原價",
        "hanjaReading": "工(장인 공) + 事(일 사) + 原(근본 원) + 價(값 가)",
        "pronunciation": "공사원까",
        "meaningKo": "공사를 수행하는 데 소요되는 모든 비용의 총합. 재료비, 노무비, 경비로 구성되며, 여기에 일반관리비와 이윤을 더하면 공사금액이 됩니다. 통역 시 '공사비'와 구분해야 하는데, 공사원가는 이윤을 제외한 순수 원가를 의미하므로 주의가 필요합니다. 베트nam 현장에서는 '실제 들어간 비용'으로 설명하면 이해가 빠르며, 한국 건설사는 원가절감을 통한 이윤 극대화를 중요하게 여깁니다.",
        "meaningVi": "Tổng hợp tất cả chi phí cần thiết để thực hiện công trình. Bao gồm chi phí vật liệu, nhân công, và chi phí chung. Khi cộng thêm chi phí quản lý chung và lợi nhuận sẽ trở thành giá công trình. Đây là chi phí thuần túy chưa bao gồm lợi nhuận, khác với giá công trình (công사비).",
        "context": "원가관리, 예산, 회계, 손익분석",
        "culturalNote": "한국 건설사는 공사원가 분석을 매우 체계적으로 수행하며, 원가절감률이 성과평가의 핵심 지표입니다. 베트남 현장에서는 원가 개념을 '실제 지출'로 단순하게 인식하는 경향이 있어, '이윤 제외 전 순수 비용'임을 명확히 해야 오해가 없습니다. 한국은 원가를 재료비/노무비/경비로 세분화하여 관리하는 문화가 강합니다.",
        "commonMistakes": [
            {
                "mistake": "giá công trình (공사비)",
                "correction": "chi phí thi công (원가) hoặc nguyên giá thi công",
                "explanation": "공사비는 이윤 포함 총액이고, 원가는 이윤 제외 순수 비용이므로 구분 필수"
            },
            {
                "mistake": "chi phí xây dựng (건설비용)",
                "correction": "nguyên giá công trình (공사 원가)",
                "explanation": "일반적 건설비용이 아닌 회계적 의미의 원가 개념임을 명확히 해야 함"
            },
            {
                "mistake": "tổng chi phí (총비용)",
                "correction": "chi phí trực tiếp thi công (직접 시공 원가)",
                "explanation": "일반관리비, 이윤을 제외한 직접원가를 의미하므로 '총비용'보다 구체적 표현 필요"
            }
        ],
        "examples": [
            {
                "ko": "이번 공사의 공사원가는 계약금액의 82% 수준입니다.",
                "vi": "Chi phí thi công của công trình này ở mức 82% so với giá hợp đồng.",
                "situation": "formal"
            },
            {
                "ko": "공사원가를 줄이려면 자재 단가 협상이 중요합니다.",
                "vi": "Để giảm chi phí thi công, việc đàm phán đơn giá vật liệu rất quan trọng.",
                "situation": "onsite"
            },
            {
                "ko": "공사원가 분석해보니 노무비 비중이 너무 높아요.",
                "vi": "Phân tích chi phí thi công thì thấy tỷ trọng nhân công quá cao.",
                "situation": "informal"
            }
        ],
        "relatedTerms": ["실행예산", "재료비", "노무비", "경비", "이윤"]
    },
    {
        "slug": "don-gia-hang-muc",
        "korean": "일위대가",
        "vietnamese": "Đơn giá hạng mục",
        "hanja": "一位代價",
        "hanjaReading": "一(한 일) + 位(자리 위) + 代(대신 대) + 價(값 가)",
        "pronunciation": "일위대까",
        "meaningKo": "공사의 최소 단위 작업(공종)에 대한 단위당 가격. 예를 들어 '콘크리트 1㎥당 가격' 또는 '철근 1톤당 가격'처럼 작업 단위별로 재료비, 노무비, 경비를 합산하여 산정합니다. 통역 시 베트남 현장에서는 '단가표'로 오해할 수 있으나, 일위대가는 재료+인건비+장비비가 모두 포함된 종합단가임을 강조해야 합니다. 한국 건설에서 견적의 기초가 되는 매우 중요한 개념입니다.",
        "meaningVi": "Đơn giá cho một đơn vị công việc nhỏ nhất (hạng mục công tác). Ví dụ như 'giá mỗi m³ bê tông' hoặc 'giá mỗi tấn cốt thép', được tính bằng cách cộng chi phí vật liệu, nhân công và máy móc cho từng đơn vị công việc. Đây là đơn giá tổng hợp bao gồm vật tư + nhân công + thiết bị, khác với đơn giá vật liệu đơn thuần.",
        "context": "견적, 예산, 입찰, 원가산정",
        "culturalNote": "한국 건설에서는 표준품셈에 기반한 일위대가 작성이 필수이며, 공공공사는 표준일위대가 적용이 의무입니다. 베트남 현장에서는 이러한 표준화된 단가 체계가 덜 발달되어 있어, 일위대가 개념 자체를 설명하는 데 시간이 걸릴 수 있습니다. 한국 건설사는 일위대가를 DB화하여 재사용하는 문화가 강합니다.",
        "commonMistakes": [
            {
                "mistake": "đơn giá vật liệu (자재 단가)",
                "correction": "đơn giá tổng hợp hạng mục công tác (공종 종합단가)",
                "explanation": "자재만이 아닌 인건비, 장비비를 모두 포함한 종합단가임을 명확히 해야 함"
            },
            {
                "mistake": "bảng giá (가격표)",
                "correction": "đơn giá từng hạng mục công việc (개별 작업 단가)",
                "explanation": "단순 가격표가 아닌 공종별로 산출된 단가 체계임을 강조 필요"
            },
            {
                "mistake": "chi phí đơn vị (단위 비용)",
                "correction": "đơn giá cấu thành cho mỗi hạng mục (각 공종별 구성 단가)",
                "explanation": "재료+인건+장비의 구성 내역이 포함된 개념임을 전달해야 정확함"
            }
        ],
        "examples": [
            {
                "ko": "일위대가를 기준으로 전체 공사비를 산출하겠습니다.",
                "vi": "Chúng tôi sẽ tính toán tổng chi phí công trình dựa trên đơn giá từng hạng mục.",
                "situation": "formal"
            },
            {
                "ko": "철근 배근 일위대가에 현장 할증을 반영해야 합니다.",
                "vi": "Cần phản ánh phụ phí hiện trường vào đơn giá thi công cốt thép.",
                "situation": "onsite"
            },
            {
                "ko": "일위대가 분석해보니 노무비가 표준보다 높네요.",
                "vi": "Phân tích đơn giá thì thấy chi phí nhân công cao hơn tiêu chuẩn.",
                "situation": "informal"
            }
        ],
        "relatedTerms": ["품셈", "단가", "공종", "견적", "내역서"]
    },
    {
        "slug": "dinh-muc-lao-dong",
        "korean": "품셈",
        "vietnamese": "Định mức lao động",
        "hanja": None,
        "hanjaReading": None,
        "pronunciation": "품셈",
        "meaningKo": "일정한 작업을 완성하는 데 필요한 표준 노무량, 자재량, 장비 사용량을 정한 기준. '품(노동력) + 셈(계산)'의 합성어로, 예를 들어 '철근 1톤 배근에 필요한 인력과 시간'을 표준화한 것입니다. 통역 시 베트남에서는 이러한 표준화된 품셈 개념이 생소할 수 있으므로 '작업 표준량'으로 풀어 설명하면 효과적입니다. 한국 건설에서는 국토부 고시 표준품셈을 기준으로 견적을 작성합니다.",
        "meaningVi": "Tiêu chuẩn quy định lượng lao động, vật liệu, thiết bị cần thiết để hoàn thành một công việc nhất định. Đây là chuẩn mức được tiêu chuẩn hóa, ví dụ 'nhân lực và thời gian cần thiết để lắp đặt 1 tấn cốt thép'. Tại Hàn Quốc, định mức tiêu chuẩn do Bộ Đất đai công bố được sử dụng làm cơ sở lập dự toán.",
        "context": "견적, 원가산정, 공정계획, 노무관리",
        "culturalNote": "한국 건설산업은 1962년부터 표준품셈 제도를 운영하며 체계적으로 관리해왔습니다. 공공공사는 표준품셈 적용이 의무이며, 민간공사도 이를 기준으로 합니다. 베트남 현장에서는 이러한 국가 표준 품셈이 없거나 활용도가 낮아, 한국 기준을 설명할 때 '정부 공인 작업량 기준'임을 강조해야 신뢰를 얻을 수 있습니다.",
        "commonMistakes": [
            {
                "mistake": "tiêu chuẩn kỹ thuật (기술 기준)",
                "correction": "định mức lao động và vật tư (노무 및 자재 정량 기준)",
                "explanation": "기술 기준이 아닌 작업량/자재량의 표준 수량 기준임을 명확히 해야 함"
            },
            {
                "mistake": "bảng tính giá (견적표)",
                "correction": "định mức tiêu hao (소요량 정량 기준)",
                "explanation": "가격표가 아닌 작업에 필요한 투입량 기준임을 구분해야 정확함"
            },
            {
                "mistake": "năng suất lao động (노동 생산성)",
                "correction": "tiêu chuẩn lượng công lao động (노동 공수 표준)",
                "explanation": "생산성은 결과 지표이고, 품셈은 투입 기준이므로 개념 차이 존재"
            }
        ],
        "examples": [
            {
                "ko": "표준품셈을 적용하여 노무비를 산출하겠습니다.",
                "vi": "Chúng tôi sẽ tính chi phí nhân công dựa trên định mức tiêu chuẩn.",
                "situation": "formal"
            },
            {
                "ko": "현장 여건상 품셈보다 20% 더 걸릴 것 같습니다.",
                "vi": "Do điều kiện hiện trường, có vẻ sẽ mất nhiều hơn 20% so với định mức.",
                "situation": "onsite"
            },
            {
                "ko": "품셈 기준으로 인력 계획 세우면 정확해요.",
                "vi": "Nếu lập kế hoạch nhân lực theo định mức thì sẽ chính xác.",
                "situation": "informal"
            }
        ],
        "relatedTerms": ["일위대가", "노무비", "공수", "표준단가", "견적"]
    },
    {
        "slug": "don-gia-vat-lieu",
        "korean": "자재단가",
        "vietnamese": "Đơn giá vật liệu",
        "hanja": "資材單價",
        "hanjaReading": "資(재물 자) + 材(재목 재) + 單(홑 단) + 價(값 가)",
        "pronunciation": "자재단까",
        "meaningKo": "공사에 사용되는 각종 자재의 개별 가격. 시멘트, 철근, 목재, 전선 등 모든 건설자재의 단위당 가격을 의미하며, 시장 상황에 따라 변동됩니다. 통역 시 주의할 점은 자재단가는 '순수 재료비'만 포함하고 운반비나 양중비는 별도라는 것입니다. 베트남 현장에서는 자재단가에 운반비가 포함되는 경우가 많아 혼선이 생길 수 있으므로, 계약 시 명확히 구분해야 합니다.",
        "meaningVi": "Giá cả riêng lẻ của từng loại vật liệu sử dụng trong công trình. Bao gồm giá đơn vị của xi măng, cốt thép, gỗ, dây điện và tất cả vật liệu xây dựng, giá cả thay đổi theo tình hình thị trường. Cần lưu ý đơn giá vật liệu chỉ bao gồm chi phí nguyên vật liệu thuần túy, chi phí vận chuyển và bốc xếp được tính riêng.",
        "context": "견적, 구매, 자재관리, 원가산정",
        "culturalNote": "한국 건설사는 자재단가를 정기적으로 DB화하여 관리하며, 물가정보지(한국물가정보 등)를 통해 시장가격을 확인합니다. 베트남에서는 자재단가에 운반비, 부대비용이 포함되는 경우가 많아, 한국 방식대로 순수 자재비만 구분하여 계약하면 나중에 추가 비용 논쟁이 발생할 수 있으므로 계약 시 명확한 정의가 필요합니다.",
        "commonMistakes": [
            {
                "mistake": "giá vật tư bao gồm vận chuyển (운반비 포함 자재가격)",
                "correction": "đơn giá vật liệu thuần túy (순수 자재 단가)",
                "explanation": "한국 건설에서는 자재단가와 운반비를 별도 항목으로 구분하므로 명확히 해야 함"
            },
            {
                "mistake": "chi phí nguyên vật liệu (원자재 비용)",
                "correction": "đơn giá từng loại vật liệu (개별 자재 단가)",
                "explanation": "총비용이 아닌 개별 자재의 단위 가격임을 구분해야 정확함"
            },
            {
                "mistake": "giá mua vật liệu (자재 구매가)",
                "correction": "đơn giá vật liệu tiêu chuẩn (표준 자재 단가)",
                "explanation": "실제 구매가가 아닌 견적/원가 산정용 표준 단가를 의미하는 경우가 많음"
            }
        ],
        "examples": [
            {
                "ko": "철근 자재단가가 지난달 대비 15% 상승했습니다.",
                "vi": "Đơn giá cốt thép đã tăng 15% so với tháng trước.",
                "situation": "formal"
            },
            {
                "ko": "자재단가 협상해서 5% 절감했어요.",
                "vi": "Đàm phán đơn giá vật liệu và tiết kiệm được 5%.",
                "situation": "onsite"
            },
            {
                "ko": "자재단가는 운반비 빼고 계산하는 거예요.",
                "vi": "Đơn giá vật liệu được tính không bao gồm phí vận chuyển.",
                "situation": "informal"
            }
        ],
        "relatedTerms": ["재료비", "구매", "물가", "일위대가", "견적"]
    },
    {
        "slug": "chi-phi-nhan-cong",
        "korean": "노무비",
        "vietnamese": "Chi phí nhân công",
        "hanja": "勞務費",
        "hanjaReading": "勞(힘쓸 로) + 務(힘쓸 무) + 費(쓸 비)",
        "pronunciation": "노무비",
        "meaningKo": "공사에 투입되는 인력에 대한 인건비. 직접 작업하는 기능공, 보조인력, 현장관리자 등의 임금을 모두 포함합니다. 통역 시 주의할 점은 한국에서는 노무비를 '공종별 표준 노무단가 × 투입 공수'로 계산하는 반면, 베트남에서는 실제 지급 임금 기준으로 접근하는 경우가 많아 계산 방식의 차이를 명확히 해야 합니다. 공사원가에서 보통 30~40%를 차지하는 중요한 항목입니다.",
        "meaningVi": "Chi phí nhân công cho lao động đầu tư vào công trình. Bao gồm lương của thợ kỹ thuật trực tiếp thi công, nhân công phụ và quản lý hiện trường. Thường chiếm 30-40% trong tổng chi phí thi công, là hạng mục chi phí quan trọng. Tại Hàn Quốc tính theo đơn giá nhân công tiêu chuẩn x công lao động đầu vào.",
        "context": "원가관리, 인력관리, 견적, 예산",
        "culturalNote": "한국 건설에서는 노무비를 직접노무비(현장 작업자)와 간접노무비(현장 관리자)로 구분하여 관리합니다. 베트남 현장에서는 일당 기준 실비 정산 방식이 일반적이지만, 한국 본사는 표준품셈 기반 노무비 예산을 요구하므로 양쪽 방식을 모두 이해하고 통역해야 합니다. 특히 공공공사는 노무비 비율이 법적으로 정해져 있어 더욱 엄격합니다.",
        "commonMistakes": [
            {
                "mistake": "lương công nhân (노동자 임금)",
                "correction": "chi phí lao động thi công (시공 노무비)",
                "explanation": "단순 임금이 아닌 공사 원가 항목으로서의 노무비 개념을 명확히 해야 함"
            },
            {
                "mistake": "tiền công (품삯)",
                "correction": "chi phí nhân công (인건비) 또는 노무비",
                "explanation": "일용직 품삯 개념이 아닌 원가 구성요소로서의 노무비임을 강조 필요"
            },
            {
                "mistake": "chi phí lao động trực tiếp (직접 인건비만)",
                "correction": "chi phí nhân công bao gồm trực tiếp và gián tiếp (직간접 노무비 포함)",
                "explanation": "노무비는 직접+간접 노무비를 모두 포함하므로 범위를 명확히 해야 함"
            }
        ],
        "examples": [
            {
                "ko": "노무비가 전체 공사비의 35%를 차지하고 있습니다.",
                "vi": "Chi phí nhân công chiếm 35% tổng giá công trình.",
                "situation": "formal"
            },
            {
                "ko": "숙련공 부족으로 노무비가 예상보다 높아졌어요.",
                "vi": "Do thiếu thợ lành nghề nên chi phí nhân công cao hơn dự kiến.",
                "situation": "onsite"
            },
            {
                "ko": "노무비 절감하려면 공정 효율을 높여야 해요.",
                "vi": "Để giảm chi phí nhân công cần nâng cao hiệu suất thi công.",
                "situation": "informal"
            }
        ],
        "relatedTerms": ["공수", "품셈", "인건비", "직접노무비", "간접노무비"]
    },
    {
        "slug": "chi-phi-chung",
        "korean": "경비",
        "vietnamese": "Chi phí chung",
        "hanja": "經費",
        "hanjaReading": "經(지날 경) + 費(쓸 비)",
        "pronunciation": "경비",
        "meaningKo": "공사 수행에 필요하지만 직접 공사원가(재료비, 노무비)에 포함되지 않는 각종 부대비용. 전력비, 수도광열비, 운반비, 품질관리비, 안전관리비, 가설재 사용료 등을 포함합니다. 통역 시 베트남 현장에서는 '기타 비용'으로 뭉뚱그려 이해하는 경우가 많으나, 한국 건설에서는 경비를 세부 항목별로 명확히 구분하여 관리하므로 이를 강조해야 합니다. 공사원가의 약 10~15%를 차지합니다.",
        "meaningVi": "Các chi phí phụ trợ cần thiết cho thi công nhưng không được tính vào chi phí trực tiếp (vật liệu, nhân công). Bao gồm chi phí điện, nước, vận chuyển, quản lý chất lượng, an toàn, cho thuê vật liệu tạm. Chiếm khoảng 10-15% chi phí thi công. Tại Hàn Quốc được quản lý chi tiết theo từng hạng mục.",
        "context": "원가관리, 예산, 공사관리, 회계",
        "culturalNote": "한국 건설에서는 경비를 '순수 경비'와 '일반관리비'로 엄격히 구분합니다. 순수 경비는 현장에서 직접 발생하는 비용이고, 일반관리비는 본사 관리 비용으로 별도 항목입니다. 베트남 현장에서는 이러한 구분이 명확하지 않은 경우가 많아, 본사 보고 시 경비 항목 분류에 주의가 필요합니다. 특히 안전관리비는 법정 의무 비율이 있습니다.",
        "commonMistakes": [
            {
                "mistake": "chi phí khác (기타 비용)",
                "correction": "chi phí gián tiếp thi công (시공 간접비)",
                "explanation": "기타 비용이 아닌 명확히 정의된 간접비 항목임을 강조해야 함"
            },
            {
                "mistake": "chi phí quản lý (관리비 전체)",
                "correction": "kinh phí hiện trường (현장 경비)",
                "explanation": "일반관리비와 구분되는 현장 발생 경비임을 명확히 해야 함"
            },
            {
                "mistake": "phí tổn phụ (부대비용 일반)",
                "correction": "chi phí phụ trợ thi công (시공 부대비)",
                "explanation": "시공과 직접 관련된 부대비임을 구체화해야 정확함"
            }
        ],
        "examples": [
            {
                "ko": "경비 항목 중 안전관리비가 법정 비율에 미달합니다.",
                "vi": "Trong hạng mục chi phí chung, chi phí quản lý an toàn chưa đạt tỷ lệ quy định.",
                "situation": "formal"
            },
            {
                "ko": "전력비가 너무 많이 나와서 경비 예산을 초과했어요.",
                "vi": "Chi phí điện quá cao nên đã vượt ngân sách chi phí chung.",
                "situation": "onsite"
            },
            {
                "ko": "경비를 줄이려면 운반비 관리가 중요해요.",
                "vi": "Để giảm chi phí chung, quản lý chi phí vận chuyển rất quan trọng.",
                "situation": "informal"
            }
        ],
        "relatedTerms": ["재료비", "노무비", "일반관리비", "직접비", "간접비"]
    },
    {
        "slug": "chi-phi-gian-tiep",
        "korean": "간접비",
        "vietnamese": "Chi phí gián tiếp",
        "hanja": "間接費",
        "hanjaReading": "間(사이 간) + 接(이을 접) + 費(쓸 비)",
        "pronunciation": "간접비",
        "meaningKo": "공사 수행에 필요하지만 특정 공종이나 작업에 직접 귀속시키기 어려운 비용. 현장 관리자 인건비, 현장 사무소 운영비, 품질관리비, 안전관리비 등을 포함합니다. 통역 시 '직접비(재료비, 노무비, 경비)'와 대비되는 개념으로, 한국 건설에서는 간접비를 직접비의 일정 비율로 계산하는 경우가 많습니다. 베트남 현장에서는 간접비 개념이 모호한 경우가 많아 명확한 설명이 필요합니다.",
        "meaningVi": "Chi phí cần thiết cho thi công nhưng khó phân bổ trực tiếp cho một hạng mục hoặc công việc cụ thể. Bao gồm lương quản lý hiện trường, chi phí vận hành văn phòng hiện trường, quản lý chất lượng, an toàn. Là khái niệm đối lập với chi phí trực tiếp (vật liệu, nhân công, kinh phí). Tại Hàn Quốc thường tính theo tỷ lệ % của chi phí trực tiếp.",
        "context": "원가관리, 회계, 예산, 원가분석",
        "culturalNote": "한국 건설회계에서는 간접비를 현장간접비와 본사일반관리비로 구분합니다. 현장간접비는 프로젝트별로 발생하고, 일반관리비는 회사 전체 운영비입니다. 베트남에서는 이러한 2단계 구분이 생소할 수 있으며, 특히 본사 일반관리비를 현장 원가에 배부하는 방식이 이해되지 않을 수 있으므로 회계 원칙을 설명해야 합니다.",
        "commonMistakes": [
            {
                "mistake": "chi phí phụ (부대비용)",
                "correction": "chi phí không trực tiếp phân bổ (직접 배분 불가 비용)",
                "explanation": "부대비가 아닌 특정 공종에 직접 귀속시킬 수 없는 비용임을 명확히 해야 함"
            },
            {
                "mistake": "chi phí quản lý chung (일반관리비 전체)",
                "correction": "chi phí gián tiếp hiện trường (현장 간접비)",
                "explanation": "본사 일반관리비와 현장 간접비를 구분해야 정확함"
            },
            {
                "mistake": "chi phí không phân loại (미분류 비용)",
                "correction": "chi phí phân bổ chung (공통 배부비)",
                "explanation": "미분류가 아니라 공통으로 배부하는 비용 항목임을 강조 필요"
            }
        ],
        "examples": [
            {
                "ko": "간접비는 직접비의 12%로 계상하였습니다.",
                "vi": "Chi phí gián tiếp được tính là 12% của chi phí trực tiếp.",
                "situation": "formal"
            },
            {
                "ko": "현장 사무소 운영비는 간접비로 처리해야 합니다.",
                "vi": "Chi phí vận hành văn phòng hiện trường phải xử lý là chi phí gián tiếp.",
                "situation": "onsite"
            },
            {
                "ko": "간접비 비율이 너무 높으면 수익성이 나빠져요.",
                "vi": "Nếu tỷ lệ chi phí gián tiếp quá cao thì lợi nhuận sẽ giảm.",
                "situation": "informal"
            }
        ],
        "relatedTerms": ["직접비", "일반관리비", "경비", "배부", "원가"]
    },
    {
        "slug": "loi-nhuan",
        "korean": "이윤",
        "vietnamese": "Lợi nhuận",
        "hanja": "利潤",
        "hanjaReading": "利(이로울 리) + 潤(윤택할 윤)",
        "pronunciation": "이윤",
        "meaningKo": "공사원가에 더하여 건설사가 얻는 순수익. 일반적으로 공사금액 = 공사원가(재료비+노무비+경비) + 일반관리비 + 이윤으로 구성됩니다. 통역 시 주의할 점은 한국 공공공사의 경우 이윤율이 법으로 정해져 있으며(보통 15% 내외), 민간공사는 협상에 따라 달라진다는 것입니다. 베트남 현장에서는 이윤을 '마진'으로 표현하는 경우가 많으나, 회계 용어로는 '이윤'이 정확합니다.",
        "meaningVi": "Lợi nhuận thuần túy mà công ty xây dựng thu được, được cộng thêm vào chi phí thi công. Thông thường giá công trình = chi phí thi công (vật liệu+nhân công+kinh phí) + chi phí quản lý chung + lợi nhuận. Trong công trình công cộng Hàn Quốc, tỷ lệ lợi nhuận được quy định bởi pháp luật (thường khoảng 15%), công trình tư nhân thì tùy thuộc đàm phán.",
        "context": "원가관리, 회계, 계약, 수익성 분석",
        "culturalNote": "한국 공공공사는 이윤율을 예정가격의 15% 이내로 법정 상한선이 있으며, 공사 종류와 난이도에 따라 차등 적용됩니다. 베트남에서는 이러한 법정 이윤율 개념이 없어, 한국 공공공사 계약 시 '왜 이윤이 15%로 고정되는가'에 대한 설명이 필요할 수 있습니다. 민간공사는 협상을 통해 결정되지만 보통 10~20% 범위입니다.",
        "commonMistakes": [
            {
                "mistake": "margin (마진)",
                "correction": "lợi nhuận (이윤)",
                "explanation": "영어 차용어 마진보다 회계 용어 lợi nhuận이 공식 문서에 적합함"
            },
            {
                "mistake": "tiền lãi (이자, 이익금)",
                "correction": "lợi nhuận thi công (공사 이윤)",
                "explanation": "이자나 일반 이익이 아닌 건설 공사의 이윤임을 명확히 해야 함"
            },
            {
                "mistake": "thu nhập (수입)",
                "correction": "lợi nhuận ròng (순이윤)",
                "explanation": "총수입이 아닌 비용 차감 후 순이익임을 강조해야 정확함"
            }
        ],
        "examples": [
            {
                "ko": "이 공사의 예상 이윤율은 12%입니다.",
                "vi": "Tỷ suất lợi nhuận dự kiến của công trình này là 12%.",
                "situation": "formal"
            },
            {
                "ko": "원가 절감해서 이윤을 3% 더 확보했어요.",
                "vi": "Nhờ giảm chi phí nên đã đảm bảo thêm 3% lợi nhuận.",
                "situation": "onsite"
            },
            {
                "ko": "이윤 남기려면 공사비 관리를 잘해야 해요.",
                "vi": "Để có lợi nhuận phải quản lý chi phí công trình tốt.",
                "situation": "informal"
            }
        ],
        "relatedTerms": ["공사원가", "일반관리비", "수익성", "이윤율", "공사금액"]
    },
    {
        "slug": "kinh-phi-du-phong",
        "korean": "예비비",
        "vietnamese": "Kinh phí dự phòng",
        "hanja": "豫備費",
        "hanjaReading": "豫(미리 예) + 備(갖출 비) + 費(쓸 비)",
        "pronunciation": "예비비",
        "meaningKo": "공사 중 예상치 못한 상황이나 설계 변경에 대비하여 미리 확보해 두는 비용. 일반적으로 공사비의 3~10%를 예비비로 책정하며, 발주자가 관리합니다. 통역 시 주의할 점은 예비비는 '확정된 공사 범위 외의 추가 비용'을 위한 것이므로, 시공사가 임의로 사용할 수 없고 발주자 승인이 필요하다는 것입니다. 베트남 현장에서는 예비비 개념이 명확하지 않아 분쟁의 소지가 있으므로 계약 시 사용 조건을 명확히 해야 합니다.",
        "meaningVi": "Kinh phí dự trữ sẵn để đối phó với tình huống không lường trước hoặc thay đổi thiết kế trong quá trình thi công. Thông thường dành 3-10% giá công trình làm kinh phí dự phòng, do chủ đầu tư quản lý. Đây là chi phí cho 'công việc ngoài phạm vi đã xác định', nhà thầu không thể tự ý sử dụng mà cần sự phê duyệt của chủ đầu tư.",
        "context": "계약, 예산, 설계변경, 클레임",
        "culturalNote": "한국 공공공사에서는 예비비 사용에 대한 엄격한 절차가 있으며, 설계변경 승인 후에만 집행 가능합니다. 베트남 현장에서는 예비비를 '여유 예산'으로 오해하여 시공사가 자유롭게 쓸 수 있다고 생각하는 경우가 있으나, 이는 발주자 소유이며 특정 조건에서만 사용 가능함을 명확히 해야 합니다. 예비비 집행은 추가 계약(변경 계약) 형태로 이루어집니다.",
        "commonMistakes": [
            {
                "mistake": "ngân sách dự trữ tự do (자유 예비 예산)",
                "correction": "kinh phí dự phòng có điều kiện (조건부 예비비)",
                "explanation": "자유롭게 쓸 수 있는 예산이 아닌 발주자 승인 필요 비용임을 명확히 해야 함"
            },
            {
                "mistake": "tiền thừa (여유 자금)",
                "correction": "kinh phí cho biến động thiết kế (설계 변동 대비 비용)",
                "explanation": "남는 돈이 아닌 특정 목적(설계변경 등)을 위한 예비 비용임을 강조 필요"
            },
            {
                "mistake": "chi phí bổ sung (추가 비용 일반)",
                "correction": "kinh phí dự phòng rủi ro (위험 대비 예비비)",
                "explanation": "일반 추가비가 아닌 불확실성 대비 목적임을 명확히 해야 정확함"
            }
        ],
        "examples": [
            {
                "ko": "예비비는 설계 변경 승인 후에만 사용할 수 있습니다.",
                "vi": "Kinh phí dự phòng chỉ có thể sử dụng sau khi được phê duyệt thay đổi thiết kế.",
                "situation": "formal"
            },
            {
                "ko": "지반 조건이 달라서 예비비로 처리해야 할 것 같아요.",
                "vi": "Do điều kiện địa chất khác nên có vẻ phải xử lý bằng kinh phí dự phòng.",
                "situation": "onsite"
            },
            {
                "ko": "예비비 남으면 발주자가 회수해 가요.",
                "vi": "Nếu kinh phí dự phòng còn thừa thì chủ đầu tư sẽ thu hồi.",
                "situation": "informal"
            }
        ],
        "relatedTerms": ["설계변경", "추가공사", "클레임", "계약금액", "변경계약"]
    }
]

# 저장 경로 설정
project_root = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
terms_file = os.path.join(project_root, "data", "terms", "construction.json")

def main():
    """기존 construction.json에 새 용어 추가"""

    # 기존 파일 읽기
    with open(terms_file, 'r', encoding='utf-8') as f:
        existing_data = json.load(f)

    print(f"기존 용어 수: {len(existing_data)}")

    # 새 용어 추가
    existing_data.extend(data)

    print(f"추가된 용어 수: {len(data)}")
    print(f"총 용어 수: {len(existing_data)}")

    # 저장
    with open(terms_file, 'w', encoding='utf-8') as f:
        json.dump(existing_data, f, ensure_ascii=False, indent=2)

    print(f"\n✅ 저장 완료: {terms_file}")
    print("\n추가된 용어 목록:")
    for i, term in enumerate(data, 1):
        print(f"{i}. {term['korean']} ({term['vietnamese']})")

if __name__ == "__main__":
    main()
