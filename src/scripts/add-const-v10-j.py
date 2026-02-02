#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
건설경영/관리 용어 10개 추가 스크립트 (Construction Management)
Tier S 품질 기준 준수
"""

import json
import os

# 파일 경로 설정
file_path = os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', 'data', 'terms', 'construction.json')

# 기존 데이터 로드
with open(file_path, 'r', encoding='utf-8') as f:
    data = json.load(f)  # data is a LIST

# 기존 slug 추출
existing_slugs = {t['slug'] for t in data}

# 신규 용어 10개 (건설경영/관리)
new_terms = [
    {
        "slug": "quan-ly-du-an",
        "korean": "프로젝트관리",
        "vietnamese": "quản lý dự án",
        "hanja": "項目管理",
        "hanjaReading": "項(항목 항) + 目(눈 목) + 管(대롱 관) + 理(다스릴 리)",
        "pronunciation": "꽌 리 즈 안",
        "meaningKo": "건설 프로젝트의 계획, 실행, 통제를 총괄하는 관리 활동. 통역 시 주의할 점은 베트남에서 'dự án'이 한국보다 넓은 범위를 포함하여 사업, 계획, 프로젝트를 모두 의미할 수 있다는 것입니다. 한국의 '프로젝트관리'는 PMI의 PMBOK 기준을 따르는 체계적 관리를 의미하지만, 베트남 현장에서는 상대적으로 덜 체계적인 경우가 많아 구체적인 관리 방법론을 명시해야 오해를 방지할 수 있습니다. 특히 일정관리(quản lý tiến độ), 품질관리(quản lý chất lượng), 원가관리(quản lý chi phí)를 구분하여 설명해야 합니다.",
        "meaningVi": "Hoạt động quản lý tổng thể việc lập kế hoạch, thực hiện và kiểm soát dự án xây dựng. Bao gồm quản lý tiến độ, chất lượng, chi phí và nguồn lực con người. Ở Việt Nam, quản lý dự án thường được hiểu theo phương pháp truyền thống, trong khi Hàn Quốc áp dụng các chuẩn mực quốc tế như PMBOK của PMI với quy trình chặt chẽ hơn.",
        "context": "건설 현장, 공사 계약, 프로젝트 회의",
        "culturalNote": "한국 건설사는 통합 프로젝트관리 시스템(PMIS)을 사용하며 체계적인 문서화를 중시하는 반면, 베트남 현장은 상대적으로 유연하고 구두 커뮤니케이션에 의존하는 경향이 있습니다. 한국 PM은 일정 준수를 최우선으로 하지만, 베트남에서는 관계 유지와 유연성을 더 중요하게 여기는 문화적 차이가 있어 통역 시 양측의 기대치를 조율하는 것이 중요합니다.",
        "commonMistakes": [
            {
                "mistake": "quản lý công trình",
                "correction": "quản lý dự án",
                "explanation": "공사 현장만 관리하는 것이 아니라 전체 프로젝트를 관리하는 개념"
            },
            {
                "mistake": "điều hành dự án",
                "correction": "quản lý dự án",
                "explanation": "điều hành은 운영/지휘의 의미로 관리의 통제 기능이 약함"
            },
            {
                "mistake": "giám sát dự án",
                "correction": "quản lý dự án",
                "explanation": "giám sát은 감독/감시의 의미로 프로젝트관리의 포괄적 의미와 다름"
            }
        ],
        "examples": [
            {
                "ko": "이 프로젝트는 통합 프로젝트관리 시스템으로 관리됩니다.",
                "vi": "Dự án này được quản lý bằng hệ thống quản lý dự án tích hợp.",
                "situation": "formal"
            },
            {
                "ko": "프로젝트관리자가 주간 회의를 주재합니다.",
                "vi": "Người quản lý dự án chủ trì cuộc họp hàng tuần.",
                "situation": "onsite"
            },
            {
                "ko": "효과적인 프로젝트관리로 공기를 단축했습니다.",
                "vi": "Quản lý dự án hiệu quả giúp rút ngắn thời gian thi công.",
                "situation": "formal"
            }
        ],
        "relatedTerms": ["quan-ly-tien-do", "quan-ly-chat-luong", "quan-ly-chi-phi", "chuyen-gia-pm"]
    },
    {
        "slug": "ke-hoach-ngan-sach",
        "korean": "예산계획",
        "vietnamese": "kế hoạch ngân sách",
        "hanja": "豫算計劃",
        "hanjaReading": "豫(미리 예) + 算(셈 산) + 計(셀 계) + 劃(그을 획)",
        "pronunciation": "께 호악 응안 싹",
        "meaningKo": "건설 프로젝트의 총 비용을 예측하고 배분하는 재무 계획. 통역 시 주의할 점은 한국의 예산계획은 상세 내역서(세부 공종별 단가)를 기반으로 하지만, 베트남에서는 총액 개념으로 접근하는 경우가 많다는 것입니다. 한국 발주처는 예비비(contingency) 5-10%를 별도 항목으로 관리하지만, 베트남에서는 총액에 포함시키는 경우가 많아 예산 구조를 명확히 설명해야 합니다. 또한 'dự toán'은 견적의 의미도 있어 문맥에 따라 구분이 필요합니다.",
        "meaningVi": "Kế hoạch tài chính dự đoán và phân bổ tổng chi phí của dự án xây dựng. Bao gồm chi phí nhân công, vật liệu, thiết bị, quản lý và dự phòng. Ở Hàn Quốc, kế hoạch ngân sách được lập rất chi tiết theo từng hạng mục công việc với đơn giá cụ thể, trong khi Việt Nam thường tiếp cận theo tổng mức đầu tư.",
        "context": "프로젝트 기획, 입찰, 계약 협상",
        "culturalNote": "한국 건설사는 예산을 엄격하게 통제하며 변경 시 공식 절차(설계변경, VE)를 거치지만, 베트남 현장에서는 상대적으로 유연하게 조정하는 경향이 있습니다. 한국은 예산 초과를 심각한 문제로 보지만, 베트남에서는 협상을 통한 추가 예산 확보를 당연하게 여기는 문화적 차이가 있어 예산 관리 방식에 대한 명확한 합의가 필요합니다.",
        "commonMistakes": [
            {
                "mistake": "dự toán ngân sách",
                "correction": "kế hoạch ngân sách",
                "explanation": "dự toán은 견적의 의미가 강하고, 계획은 kế hoạch이 적절"
            },
            {
                "mistake": "ngân sách chi tiêu",
                "correction": "kế hoạch ngân sách",
                "explanation": "chi tiêu는 소비/지출의 의미로 건설 예산의 계획적 성격을 표현하지 못함"
            },
            {
                "mistake": "phân bổ ngân sách",
                "correction": "kế hoạch ngân sách",
                "explanation": "phân bổ는 배분만을 의미하고 예산 수립의 전체 과정을 포함하지 않음"
            }
        ],
        "examples": [
            {
                "ko": "예산계획에 예비비 7%를 포함시켰습니다.",
                "vi": "Kế hoạch ngân sách đã bao gồm 7% chi phí dự phòng.",
                "situation": "formal"
            },
            {
                "ko": "분기별 예산계획을 검토하겠습니다.",
                "vi": "Chúng tôi sẽ xem xét kế hoạch ngân sách theo quý.",
                "situation": "onsite"
            },
            {
                "ko": "예산계획 대비 실제 집행액을 비교해 주세요.",
                "vi": "Hãy so sánh chi tiêu thực tế với kế hoạch ngân sách.",
                "situation": "formal"
            }
        ],
        "relatedTerms": ["du-toan", "chi-phi-du-an", "kiem-soat-ngan-sach", "du-phong"]
    },
    {
        "slug": "quan-ly-rui-ro",
        "korean": "리스크관리",
        "vietnamese": "quản lý rủi ro",
        "hanja": None,
        "hanjaReading": None,
        "pronunciation": "꽌 리 주이 조",
        "meaningKo": "프로젝트 수행 중 발생 가능한 위험요소를 식별하고 대응하는 관리 활동. 통역 시 주의할 점은 한국에서는 'risk'를 리스크로 외래어 그대로 사용하지만, 베트남어로는 'rủi ro'(위험)로 번역되어 부정적 뉘앙스가 더 강하다는 것입니다. 한국의 리스크관리는 기회(opportunity)와 위협(threat)을 모두 포함하는 체계적 접근이지만, 베트남에서는 주로 부정적 위험 회피에 초점을 맞추는 경향이 있습니다. 리스크 등록부(risk register), 정성적/정량적 분석 등 전문 용어를 설명할 때 구체적인 예시를 들어야 이해를 돕습니다.",
        "meaningVi": "Hoạt động quản lý nhằm xác định và đối phóng các yếu tố rủi ro có thể xảy ra trong quá trình thực hiện dự án. Bao gồm phân tích rủi ro, lập kế hoạch ứng phó và giám sát liên tục. Quản lý rủi ro giúp giảm thiểu tổn thất và tăng khả năng thành công của dự án xây dựng.",
        "context": "프로젝트 계획, 안전 회의, 계약 협상",
        "culturalNote": "한국 건설사는 공식적인 리스크 관리 프로세스(식별→분석→대응→모니터링)를 문서화하고 정기적으로 검토하지만, 베트남 현장에서는 비공식적이고 경험 기반의 위험 관리가 일반적입니다. 한국은 사전 예방을 중시하지만, 베트남에서는 문제 발생 후 대응하는 방식이 많아 리스크 관리의 중요성과 방법론을 설득력 있게 전달하는 것이 중요합니다.",
        "commonMistakes": [
            {
                "mistake": "kiểm soát rủi ro",
                "correction": "quản lý rủi ro",
                "explanation": "kiểm soát은 통제만을 의미하고 식별, 분석, 대응의 전체 과정을 포함하지 않음"
            },
            {
                "mistake": "phòng ngừa rủi ro",
                "correction": "quản lý rủi ro",
                "explanation": "phòng ngừa는 예방만을 의미하고 관리의 포괄적 개념과 다름"
            },
            {
                "mistake": "đánh giá rủi ro",
                "correction": "quản lý rủi ro",
                "explanation": "đánh giá는 평가/분석만을 의미하고 관리의 일부 단계일 뿐"
            }
        ],
        "examples": [
            {
                "ko": "리스크관리 계획을 수립하여 잠재적 문제를 사전에 파악했습니다.",
                "vi": "Chúng tôi đã lập kế hoạch quản lý rủi ro để xác định vấn đề tiềm ẩn trước.",
                "situation": "formal"
            },
            {
                "ko": "이 현장의 주요 리스크는 우기 공사 지연입니다.",
                "vi": "Rủi ro chính của công trường này là chậm trễ thi công do mùa mưa.",
                "situation": "onsite"
            },
            {
                "ko": "리스크관리 회의를 매월 개최합니다.",
                "vi": "Cuộc họp quản lý rủi ro được tổ chức hàng tháng.",
                "situation": "formal"
            }
        ],
        "relatedTerms": ["danh-sach-rui-ro", "phan-tich-rui-ro", "ung-pho-rui-ro", "bao-hiem-cong-trinh"]
    },
    {
        "slug": "bao-cao-tai-chinh",
        "korean": "재무보고",
        "vietnamese": "báo cáo tài chính",
        "hanja": "財務報告",
        "hanjaReading": "財(재물 재) + 務(힘쓸 무) + 報(알릴 보) + 告(고할 고)",
        "pronunciation": "바오 까오 따이 찡",
        "meaningKo": "건설 프로젝트의 재무 상태와 성과를 정기적으로 보고하는 문서. 통역 시 주의할 점은 한국의 재무보고는 K-IFRS 또는 일반기업회계기준을 따르는 공식 재무제표(재무상태표, 손익계산서, 현금흐름표)를 의미하지만, 베트남 현장에서는 간단한 수입/지출 내역서를 의미하는 경우가 많다는 것입니다. 한국 본사는 월별 재무보고를 요구하지만, 베트nam 현지법인은 분기별 보고가 일반적이어서 보고 주기와 양식에 대한 명확한 합의가 필요합니다.",
        "meaningVi": "Tài liệu báo cáo định kỳ về tình trạng tài chính và kết quả hoạt động của dự án xây dựng. Bao gồm báo cáo thu chi, báo cáo lợi nhuận và báo cáo lưu chuyển tiền tệ. Ở Việt Nam, báo cáo tài chính tuân theo chuẩn mực kế toán Việt Nam (VAS), trong khi Hàn Quốc áp dụng K-IFRS với yêu cầu công bố chi tiết hơn.",
        "context": "본사 보고, 감사, 투자자 미팅",
        "culturalNote": "한국 건설사는 재무 투명성을 중시하며 세부 항목별 분석을 요구하지만, 베트남에서는 재무 정보를 민감하게 여겨 공개를 꺼리는 경향이 있습니다. 한국은 재무보고의 정확성과 적시성을 엄격히 요구하지만, 베트남에서는 상대적으로 유연한 해석을 허용하는 문화적 차이가 있어 보고 기준에 대한 명확한 가이드라인이 필요합니다.",
        "commonMistakes": [
            {
                "mistake": "báo cáo thu chi",
                "correction": "báo cáo tài chính",
                "explanation": "thu chi는 수입/지출만을 의미하고 재무상태표 등 전체 재무보고를 포함하지 않음"
            },
            {
                "mistake": "sổ sách kế toán",
                "correction": "báo cáo tài chính",
                "explanation": "sổ sách은 장부/기록의 의미로 공식 보고서와 다름"
            },
            {
                "mistake": "bảng kê tài chính",
                "correction": "báo cáo tài chính",
                "explanation": "bảng kê는 명세서/목록의 의미로 종합 보고서의 성격과 다름"
            }
        ],
        "examples": [
            {
                "ko": "분기별 재무보고를 이사회에 제출합니다.",
                "vi": "Báo cáo tài chính quý được trình lên hội đồng quản trị.",
                "situation": "formal"
            },
            {
                "ko": "외부 감사를 위한 재무보고서를 준비 중입니다.",
                "vi": "Chúng tôi đang chuẩn bị báo cáo tài chính cho kiểm toán bên ngoài.",
                "situation": "formal"
            },
            {
                "ko": "이번 달 재무보고에서 수익성이 개선되었습니다.",
                "vi": "Báo cáo tài chính tháng này cho thấy khả năng sinh lời được cải thiện.",
                "situation": "onsite"
            }
        ],
        "relatedTerms": ["bang-can-doi-ke-toan", "bao-cao-luu-chuyen-tien-te", "bao-cao-ket-qua-kinh-doanh", "kiem-toan"]
    },
    {
        "slug": "quan-ly-chuoi-cung-ung",
        "korean": "공급망관리",
        "vietnamese": "quản lý chuỗi cung ứng",
        "hanja": "供給網管理",
        "hanjaReading": "供(이바지할 공) + 給(줄 급) + 網(그물 망) + 管(대롱 관) + 理(다스릴 리)",
        "pronunciation": "꽌 리 쭈어이 꿍 응",
        "meaningKo": "자재 조달부터 현장 배송까지의 전체 공급 과정을 관리하는 활동. 통역 시 주의할 점은 한국의 공급망관리는 JIT(적시공급), VMI(공급사 재고관리) 등 선진 기법을 포함하지만, 베트남 현장에서는 단순히 자재 구매와 배송 관리를 의미하는 경우가 많다는 것입니다. 한국 건설사는 통합 ERP 시스템으로 공급망을 관리하지만, 베트남 협력사들은 수작업이나 단순 엑셀을 사용하는 경우가 많아 시스템 통합의 어려움을 설명해야 합니다. 또한 'chuỗi cung ứng'은 제조업에서 자주 쓰이는 용어로 건설 분야에서는 생소할 수 있어 구체적인 예시가 필요합니다.",
        "meaningVi": "Hoạt động quản lý toàn bộ quá trình cung ứng từ việc mua sắm vật tư đến giao hàng tại công trường. Bao gồm lập kế hoạch mua sắm, chọn nhà cung cấp, quản lý kho bãi và vận chuyển. Quản lý chuỗi cung ứng hiệu quả giúp giảm chi phí, đảm bảo tiến độ và chất lượng công trình.",
        "context": "자재 조달, 물류 관리, 협력사 관리",
        "culturalNote": "한국 건설사는 장기 계약과 전략적 파트너십을 통해 안정적인 공급망을 구축하지만, 베트남에서는 단기 거래와 가격 경쟁을 중시하는 경향이 있습니다. 한국은 품질과 납기를 최우선으로 하지만, 베트남 공급사들은 가격과 유연성을 더 중요하게 여기는 문화적 차이가 있어 공급 계약 시 명확한 기준 설정이 필요합니다.",
        "commonMistakes": [
            {
                "mistake": "quản lý vật tư",
                "correction": "quản lý chuỗi cung ứng",
                "explanation": "vật tư는 자재만을 의미하고 공급망의 전체 흐름을 포함하지 않음"
            },
            {
                "mistake": "mua sắm và cung cấp",
                "correction": "quản lý chuỗi cung ứng",
                "explanation": "구매와 공급만을 의미하고 물류, 재고 관리 등 전체 과정을 포함하지 않음"
            },
            {
                "mistake": "quản lý nhà cung cấp",
                "correction": "quản lý chuỗi cung ứng",
                "explanation": "공급사 관리만을 의미하고 공급망의 포괄적 개념과 다름"
            }
        ],
        "examples": [
            {
                "ko": "효율적인 공급망관리로 자재비를 15% 절감했습니다.",
                "vi": "Quản lý chuỗi cung ứng hiệu quả giúp tiết kiệm 15% chi phí vật tư.",
                "situation": "formal"
            },
            {
                "ko": "공급망관리 시스템을 도입하여 재고를 실시간으로 파악합니다.",
                "vi": "Chúng tôi triển khai hệ thống quản lý chuỗi cung ứng để theo dõi tồn kho theo thời gian thực.",
                "situation": "onsite"
            },
            {
                "ko": "주요 협력사와 공급망관리 협약을 체결했습니다.",
                "vi": "Chúng tôi đã ký thỏa thuận quản lý chuỗi cung ứng với các nhà cung cấp chính.",
                "situation": "formal"
            }
        ],
        "relatedTerms": ["mua-sam", "quan-ly-kho", "van-chuyen", "nha-cung-cap"]
    },
    {
        "slug": "dau-gia",
        "korean": "경매",
        "vietnamese": "đấu giá",
        "hanja": "競賣",
        "hanjaReading": "競(다툴 경) + 賣(팔 매)",
        "pronunciation": "더우 지아",
        "meaningKo": "공사 계약이나 자재 구매를 위해 여러 업체가 가격을 경쟁하는 절차. 통역 시 주의할 점은 한국의 '경매'는 주로 부동산 처분을 의미하고 건설 분야에서는 '입찰'(đấu thầu)을 사용하지만, 베트남에서는 'đấu giá'가 공공 조달과 일반 경매를 모두 포함할 수 있다는 것입니다. 한국의 입찰 제도는 적격심사, 최저가낙찰제, 종합심사낙찰제 등 복잡한 방식이 있지만, 베트남에서는 상대적으로 단순한 최저가 방식이 많아 입찰 방식의 차이를 명확히 설명해야 합니다.",
        "meaningVi": "Thủ tục cạnh tranh giá giữa nhiều đơn vị để ký hợp đồng thi công hoặc mua sắm vật tư. Ở Việt Nam, đấu giá thường áp dụng cho tài sản công và hàng hóa, trong khi đấu thầu (tender) được sử dụng cho các dự án xây dựng. Quá trình đấu giá phải minh bạch, công bằng và tuân thủ quy định pháp luật.",
        "context": "공공 공사, 자재 조달, 부동산 거래",
        "culturalNote": "한국의 공공 입찰은 엄격한 절차와 투명성을 요구하며 전자입찰 시스템(G2B)이 발달했지만, 베트남에서는 개인적 관계가 입찰 결과에 영향을 미치는 경우가 있습니다. 한국은 최저가보다 기술력과 신뢰도를 중시하는 종합평가방식을 선호하지만, 베트남에서는 여전히 최저가 낙찰이 일반적이어서 평가 기준의 차이를 설명하는 것이 중요합니다.",
        "commonMistakes": [
            {
                "mistake": "đấu thầu",
                "correction": "đấu giá",
                "explanation": "문맥에 따라 구분 필요: 건설 공사는 đấu thầu, 부동산/자산 처분은 đấu giá"
            },
            {
                "mistake": "bán đấu giá",
                "correction": "đấu giá",
                "explanation": "bán은 판매의 의미로 중복 표현, đấu giá만으로 충분"
            },
            {
                "mistake": "thi đấu giá",
                "correction": "đấu giá",
                "explanation": "thi는 불필요한 접두사, đấu giá가 정확한 표현"
            }
        ],
        "examples": [
            {
                "ko": "이 토지는 공개경매를 통해 매각됩니다.",
                "vi": "Mảnh đất này sẽ được bán qua đấu giá công khai.",
                "situation": "formal"
            },
            {
                "ko": "중고 건설장비를 경매로 구입했습니다.",
                "vi": "Chúng tôi đã mua thiết bị xây dựng cũ qua đấu giá.",
                "situation": "onsite"
            },
            {
                "ko": "경매 참가 자격 요건을 확인해 주세요.",
                "vi": "Vui lòng kiểm tra điều kiện tham gia đấu giá.",
                "situation": "formal"
            }
        ],
        "relatedTerms": ["dau-thau", "chao-gia", "gia-khoi-diem", "trung-thau"]
    },
    {
        "slug": "hop-dong-phu",
        "korean": "하도급계약",
        "vietnamese": "hợp đồng phụ",
        "hanja": "下都給契約",
        "hanjaReading": "下(아래 하) + 都(도읍 도) + 給(줄 급) + 契(맺을 계) + 約(맺을 약)",
        "pronunciation": "홉 동 푸",
        "meaningKo": "원도급사가 공사의 일부를 하도급사에게 재위탁하는 계약. 통역 시 주의할 점은 한국의 '하도급'은 건설산업기본법의 엄격한 규제를 받아 불법 하도급, 공사대금 직접지급제 등 법적 이슈가 많지만, 베트남에서는 상대적으로 규제가 느슨하다는 것입니다. 한국은 하도급 비율 제한(전문공사 30% 등)이 있지만, 베트남에서는 이러한 제한이 없거나 약해 하도급 구조의 법적 차이를 명확히 설명해야 합니다. 또한 'hợp đồng phụ'는 부속 계약의 의미도 있어 문맥 파악이 중요합니다.",
        "meaningVi": "Hợp đồng mà nhà thầu chính ủy thác một phần công việc cho nhà thầu phụ. Ở Việt Nam, hợp đồng phụ được quy định trong Luật Xây dựng, yêu cầu nhà thầu chính chịu trách nhiệm toàn bộ trước chủ đầu tư. Nhà thầu phụ thường đảm nhận các công việc chuyên môn như điện, nước, hoàn thiện.",
        "context": "공사 발주, 계약 협상, 시공 관리",
        "culturalNote": "한국에서는 하도급 대금 지급 지연이나 부당 단가 후려치기가 사회적 문제이며 법적 보호 장치가 많지만, 베트남에서는 하도급사의 권리 보호가 상대적으로 약합니다. 한국 원도급사는 하도급사를 파트너로 인식하고 장기 관계를 중시하지만, 베트남에서는 프로젝트별로 하도급사를 바꾸는 경우가 많아 하도급 관리 방식의 차이를 이해하는 것이 중요합니다.",
        "commonMistakes": [
            {
                "mistake": "hợp đồng thầu phụ",
                "correction": "hợp đồng phụ",
                "explanation": "thầu phụ는 부적절한 조합, nhà thầu phụ는 맞지만 hợp đồng phụ가 정확"
            },
            {
                "mistake": "hợp đồng ủy thác",
                "correction": "hợp đồng phụ",
                "explanation": "ủy thác은 위임의 일반적 의미로 건설 하도급의 특수성을 표현하지 못함"
            },
            {
                "mistake": "hợp đồng nhỏ",
                "correction": "hợp đồng phụ",
                "explanation": "nhỏ는 작다는 의미로 하도급의 법적 관계를 나타내지 못함"
            }
        ],
        "examples": [
            {
                "ko": "전기 공사는 하도급계약으로 진행합니다.",
                "vi": "Công việc điện sẽ được thực hiện theo hợp đồng phụ.",
                "situation": "formal"
            },
            {
                "ko": "하도급계약서에 공사 범위를 명확히 명시하세요.",
                "vi": "Hãy ghi rõ phạm vi công việc trong hợp đồng phụ.",
                "situation": "onsite"
            },
            {
                "ko": "하도급업체 선정 절차를 시작하겠습니다.",
                "vi": "Chúng tôi sẽ bắt đầu quy trình lựa chọn nhà thầu phụ.",
                "situation": "formal"
            }
        ],
        "relatedTerms": ["nha-thau-phu", "hop-dong-chinh", "nha-thau-chinh", "phan-cap-thi-cong"]
    },
    {
        "slug": "thanh-toan-giai-doan",
        "korean": "기성금",
        "vietnamese": "thanh toán giai đoạn",
        "hanja": "旣成金",
        "hanjaReading": "旣(이미 기) + 成(이룰 성) + 金(쇠 금)",
        "pronunciation": "탄 또안 자이 도안",
        "meaningKo": "공사 진행 단계별로 완성된 부분에 대해 지급하는 공사대금. 통역 시 주의할 점은 한국의 '기성금'은 건설 분야 고유 용어이지만 베트남어로 직역하면 의미 전달이 어려워 'thanh toán giai đoạn'(단계별 지급) 또는 'thanh toán khối lượng'(물량별 지급)으로 풀어 설명해야 한다는 것입니다. 한국은 월별 기성 검사 후 익월 지급이 일반적이지만, 베트남에서는 분기별 또는 마일스톤별 지급이 많아 지급 주기의 차이를 명확히 해야 합니다. 또한 선급금(tiền tạm ứng), 기성금(thanh toán giai đoạn), 준공금(thanh toán cuối cùng)의 구분이 필요합니다.",
        "meaningVi": "Khoản tiền công trình được thanh toán theo từng giai đoạn hoàn thành công việc. Sau khi nghiệm thu khối lượng thi công, chủ đầu tư sẽ thanh toán cho nhà thầu theo tỷ lệ hoàn thành. Đây là phương thức thanh toán phổ biến trong xây dựng để đảm bảo dòng tiền cho nhà thầu.",
        "context": "공사 대금 청구, 검수, 회계 처리",
        "culturalNote": "한국 건설사는 정확한 기성 측량과 공정율 산정을 중시하며 디지털 측량 도구를 사용하지만, 베트남 현장에서는 육안 평가나 단순 추정이 많아 기성률 산정 방식에 이견이 발생할 수 있습니다. 한국은 기성금 지급 지연을 계약 위반으로 엄격히 다루지만, 베트남에서는 지급 지연이 비교적 흔하여 현금 흐름 관리의 중요성을 설명해야 합니다.",
        "commonMistakes": [
            {
                "mistake": "tiền tạm ứng",
                "correction": "thanh toán giai đoạn",
                "explanation": "tạm ứng은 선급금을 의미하고 기성금과 다름"
            },
            {
                "mistake": "thanh toán hàng tháng",
                "correction": "thanh toán giai đoạn",
                "explanation": "월별 지급만을 의미하고 기성(완성 부분)의 개념이 없음"
            },
            {
                "mistake": "trả công",
                "correction": "thanh toán giai đoạn",
                "explanation": "trả công은 임금 지급의 의미로 공사대금과 다름"
            }
        ],
        "examples": [
            {
                "ko": "이번 달 기성금은 전체 공사비의 25%입니다.",
                "vi": "Thanh toán giai đoạn tháng này chiếm 25% tổng giá trị hợp đồng.",
                "situation": "formal"
            },
            {
                "ko": "기성 검사 후 7일 이내에 기성금을 지급합니다.",
                "vi": "Thanh toán giai đoạn sẽ được thực hiện trong vòng 7 ngày sau nghiệm thu.",
                "situation": "onsite"
            },
            {
                "ko": "기성금 청구서를 제출해 주세요.",
                "vi": "Vui lòng nộp hóa đơn thanh toán giai đoạn.",
                "situation": "formal"
            }
        ],
        "relatedTerms": ["tien-tam-ung", "nghiem-thu-giai-doan", "thanh-toan-cuoi-cung", "ty-le-hoan-thanh"]
    },
    {
        "slug": "phat-vi-pham",
        "korean": "위약금/지체상금",
        "vietnamese": "phạt vi phạm",
        "hanja": "違約金/遲滯償金",
        "hanjaReading": "違(어긋날 위) + 約(맺을 약) + 金(쇠 금) / 遲(더딜 지) + 滯(막힐 체) + 償(갚을 상) + 金(쇠 금)",
        "pronunciation": "팟 비 팜",
        "meaningKo": "계약 조건을 위반하거나 공기를 지연했을 때 부과하는 벌금. 통역 시 주의할 점은 한국에서는 '위약금'(계약 위반 시)과 '지체상금'(공기 지연 시)을 명확히 구분하지만, 베트남어 'phạt vi phạm'은 모든 위반에 대한 벌금을 포괄하는 용어라는 것입니다. 한국의 지체상금은 통상 도급금액의 일정 비율(예: 지연 1일당 0.1%)로 자동 계산되지만, 베트남에서는 협상 여지가 있어 계약서에 명확한 산정 기준을 명시해야 합니다. 또한 'phạt chậm tiến độ'(공기 지연 벌금)로 구분하여 표현하는 것이 정확합니다.",
        "meaningVi": "Khoản tiền phạt áp dụng khi vi phạm các điều kiện hợp đồng hoặc chậm tiến độ thi công. Ở Việt Nam, mức phạt được quy định trong hợp đồng, thường tính theo tỷ lệ phần trăm giá trị hợp đồng hoặc theo số ngày chậm trễ. Phạt vi phạm nhằm đảm bảo các bên thực hiện đúng cam kết.",
        "context": "계약 협상, 공정 관리, 분쟁 해결",
        "culturalNote": "한국 건설사는 지체상금을 엄격히 적용하며 공기 준수를 최우선으로 하지만, 베트남에서는 불가항력 사유나 관계를 고려해 벌금을 면제하거나 감액하는 경우가 많습니다. 한국은 계약서대로 자동 공제하는 것이 일반적이지만, 베트남에서는 협상을 통해 조정하는 것을 당연시하여 벌금 집행 방식의 문화적 차이를 이해하는 것이 중요합니다.",
        "commonMistakes": [
            {
                "mistake": "tiền phạt",
                "correction": "phạt vi phạm",
                "explanation": "tiền phạt은 일반적인 벌금으로 계약 위반의 구체성이 부족"
            },
            {
                "mistake": "bồi thường",
                "correction": "phạt vi phạm",
                "explanation": "bồi thường은 손해배상의 의미로 계약상 벌금과 다름"
            },
            {
                "mistake": "phạt chậm",
                "correction": "phạt vi phạm (hoặc phạt chậm tiến độ)",
                "explanation": "phạt chậm만으로는 불완전, 구체적인 위반 내용을 명시해야 함"
            }
        ],
        "examples": [
            {
                "ko": "공기 지연 시 하루당 위약금 0.1%가 부과됩니다.",
                "vi": "Phạt vi phạm 0.1% mỗi ngày sẽ được áp dụng nếu chậm tiến độ.",
                "situation": "formal"
            },
            {
                "ko": "위약금 조항을 계약서에 명시해야 합니다.",
                "vi": "Điều khoản phạt vi phạm phải được ghi rõ trong hợp đồng.",
                "situation": "onsite"
            },
            {
                "ko": "불가항력 사유로 위약금을 면제받았습니다.",
                "vi": "Chúng tôi được miễn phạt vi phạm do lý do bất khả kháng.",
                "situation": "formal"
            }
        ],
        "relatedTerms": ["vi-pham-hop-dong", "boi-thuong", "bat-kha-khang", "dieu-khoan-phat"]
    },
    {
        "slug": "gia-han-hop-dong",
        "korean": "계약연장",
        "vietnamese": "gia hạn hợp đồng",
        "hanja": "契約延長",
        "hanjaReading": "契(맺을 계) + 約(맺을 약) + 延(늘일 연) + 長(길 장)",
        "pronunciation": "자 한 홉 동",
        "meaningKo": "기존 계약의 유효 기간을 연장하는 절차. 통역 시 주의할 점은 한국에서 '계약연장'은 동일한 조건으로 기간만 연장하는 것을 의미하지만, 베트남에서는 조건 재협상을 포함하는 경우가 많다는 것입니다. 한국의 공공 공사는 설계변경이나 불가항력 사유가 명확해야 공기를 연장할 수 있지만, 베트남에서는 상대적으로 유연하게 연장이 가능하여 연장 요건의 차이를 설명해야 합니다. 또한 'gia hạn'은 기간 연장 일반을 의미하고, 'ký lại'는 재계약(새로운 계약)을 의미하여 구분이 필요합니다.",
        "meaningVi": "Thủ tục kéo dài thời hạn hiệu lực của hợp đồng hiện tại. Gia hạn hợp đồng có thể giữ nguyên hoặc điều chỉnh các điều khoản tùy theo thỏa thuận giữa các bên. Ở Việt Nam, gia hạn hợp đồng xây dựng thường được áp dụng khi có phát sinh khối lượng hoặc lý do bất khả kháng gây chậm tiến độ.",
        "context": "계약 관리, 공기 조정, 협상",
        "culturalNote": "한국 건설사는 계약연장을 예외적인 상황으로 보고 공식적인 절차와 문서화를 요구하지만, 베트남에서는 계약연장이 비교적 흔하며 구두 합의로 진행되는 경우도 있습니다. 한국은 연장 사유를 명확히 증빙해야 하지만, 베트남에서는 상호 신뢰를 바탕으로 유연하게 처리하는 문화적 차이가 있어 연장 절차에 대한 명확한 합의가 필요합니다.",
        "commonMistakes": [
            {
                "mistake": "ký lại hợp đồng",
                "correction": "gia hạn hợp đồng",
                "explanation": "ký lại는 재계약(새 계약)을 의미하고 기간 연장과 다름"
            },
            {
                "mistake": "kéo dài hợp đồng",
                "correction": "gia hạn hợp đồng",
                "explanation": "kéo dài은 비공식적 표현으로 법적 절차를 나타내지 못함"
            },
            {
                "mistake": "tái ký hợp đồng",
                "correction": "gia hạn hợp đồng",
                "explanation": "tái ký는 다시 서명의 의미로 연장의 정확한 의미와 다름"
            }
        ],
        "examples": [
            {
                "ko": "우기로 인한 공사 지연으로 계약을 3개월 연장합니다.",
                "vi": "Chúng tôi gia hạn hợp đồng 3 tháng do chậm tiến độ vì mưa.",
                "situation": "formal"
            },
            {
                "ko": "계약연장을 위한 부속 합의서를 작성하겠습니다.",
                "vi": "Chúng tôi sẽ lập phụ lục thỏa thuận để gia hạn hợp đồng.",
                "situation": "onsite"
            },
            {
                "ko": "발주처가 계약연장을 승인했습니다.",
                "vi": "Chủ đầu tư đã phê duyệt gia hạn hợp đồng.",
                "situation": "formal"
            }
        ],
        "relatedTerms": ["phu-luc-hop-dong", "thay-doi-hop-dong", "ky-lai-hop-dong", "han-hop-dong"]
    }
]

# 중복 제거 필터링
new_terms_filtered = [term for term in new_terms if term['slug'] not in existing_slugs]

print(f"추가 대상: {len(new_terms_filtered)}개 (중복 제외: {len(new_terms) - len(new_terms_filtered)}개)")

# 데이터 확장
data.extend(new_terms_filtered)

# 파일 저장
with open(file_path, 'w', encoding='utf-8') as f:
    json.dump(data, f, ensure_ascii=False, indent=2)

print(f"✅ 건설경영/관리 용어 {len(new_terms_filtered)}개 추가 완료!")
print(f"📊 총 용어 수: {len(data)}개")
