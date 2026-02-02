#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
공기업법/공공조달 용어 추가 스크립트 (Tier S 품질)
Theme: State Enterprise/Public Procurement
"""

import json
import os

def main():
    # 1. 파일 경로 설정
    file_path = os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', 'data', 'terms', 'legal.json')

    # 2. 기존 데이터 로드
    with open(file_path, 'r', encoding='utf-8') as f:
        data = json.load(f)  # data는 LIST

    # 3. 기존 slug 추출
    existing_slugs = {t['slug'] for t in data}

    # 4. 새 용어 정의 (10개)
    new_terms = [
        {
            "slug": "doanh-nghiep-nha-nuoc",
            "korean": "국영기업",
            "vietnamese": "doanh nghiệp nhà nước",
            "hanja": "國營企業",
            "hanjaReading": "國(나라 국) + 營(경영할 영) + 企(꾀할 기) + 業(업 업)",
            "pronunciation": "도안 응이엡 냐 느억",
            "meaningKo": "국가가 소유하고 경영하는 기업. 통역 시 베트남에서는 'DNNN'으로 약칭하는 경우가 많으니 문맥에 따라 풀어서 설명해야 한다. 한국의 공기업과 유사하지만 베트남은 정부의 직접 지분 소유 비율이 더 높고, 경영 자율성이 상대적으로 제한적인 점을 주의해서 통역할 것. 또한 베트남에서는 국영기업 개혁(개혁 doanh nghiệp nhà nước)이 주요 경제 정책 이슈이므로, 관련 논의에서 민영화, 구조조정 등의 용어와 함께 사용되는 경우가 많다.",
            "meaningVi": "Doanh nghiệp do Nhà nước làm chủ sở hữu và trực tiếp quản lý, điều hành. Đây là loại hình doanh nghiệp phổ biến ở Việt Nam, đặc biệt trong các ngành then chốt như năng lượng, viễn thông, ngân hàng. Thường được viết tắt là DNNN trong các văn bản chính thức.",
            "context": "공공경제, 국가재산, 공기업 개혁, 민영화 논의",
            "culturalNote": "한국에서는 공기업이라는 용어를 더 많이 사용하지만, 베트남에서는 '국영기업(DNNN)'이 공식 용어이다. 베트남의 국영기업은 한국보다 경제에서 차지하는 비중이 더 크며, 정부의 통제도 강하다. 한국의 공기업은 경영 자율성이 상대적으로 높고, 이사회 구성도 독립적인 반면, 베트남 국영기업은 당-정부의 인사권이 직접적으로 작용하는 경우가 많다. 통역 시 이러한 제도적 차이를 고려해 설명을 추가할 필요가 있다.",
            "commonMistakes": [
                {
                    "mistake": "'công ty công cộng'으로 번역",
                    "correction": "'doanh nghiệp nhà nước' 사용",
                    "explanation": "công ty công cộng은 상장기업(publicly traded company)을 의미하므로 오해의 소지가 있다."
                },
                {
                    "mistake": "'국영'을 'công'으로만 번역",
                    "correction": "'nhà nước' 명시 필수",
                    "explanation": "'công'만 쓰면 공공/공적의 의미로 모호하므로 '국가 소유'를 명확히 해야 한다."
                },
                {
                    "mistake": "한국 공기업과 완전히 동일한 개념으로 설명",
                    "correction": "제도적 차이점 언급 필수",
                    "explanation": "양국의 공기업 제도는 소유구조, 경영자율성, 감독체계 등에서 차이가 있다."
                }
            ],
            "examples": [
                {
                    "ko": "베트남의 국영기업 구조조정은 경제 개혁의 핵심 과제입니다.",
                    "vi": "Cơ cấu lại doanh nghiệp nhà nước là nhiệm vụ then chốt của cải cách kinh tế Việt Nam.",
                    "situation": "formal"
                },
                {
                    "ko": "이 국영기업은 전력 분야에서 독점적 지위를 갖고 있습니다.",
                    "vi": "Doanh nghiệp nhà nước này nắm giữ vị trí độc quyền trong lĩnh vực điện lực.",
                    "situation": "formal"
                },
                {
                    "ko": "국영기업의 민영화 계획이 발표되었습니다.",
                    "vi": "Kế hoạch cổ phần hóa doanh nghiệp nhà nước đã được công bố.",
                    "situation": "formal"
                }
            ],
            "relatedTerms": ["co-phan-hoa", "dau-thau-cong", "von-nha-nuoc", "cong-ty-co-phan", "cai-cach-kinh-te"]
        },
        {
            "slug": "co-phan-hoa",
            "korean": "민영화",
            "vietnamese": "cổ phần hóa",
            "hanja": "民營化",
            "hanjaReading": "民(백성 민) + 營(경영할 영) + 化(될 화)",
            "pronunciation": "꼬 판 호아",
            "meaningKo": "국영기업을 민간 소유로 전환하는 것. 통역 시 주의할 점은 베트남어 'cổ phần hóa'는 문자 그대로 '주식화'를 의미하지만, 실질적으로는 민영화를 뜻한다는 점이다. 베트남에서는 완전 매각보다는 일부 지분을 민간에 매각하는 부분 민영화가 일반적이므로, 통역 시 '부분 민영화(cổ phần hóa một phần)'와 '완전 민영화(tư nhân hóa hoàn toàn)'를 구분해야 한다. 또한 베트남의 민영화는 정치적으로 민감한 주제이므로, 공식 석상에서는 '개혁(cải cách)' 또는 '구조조정(cơ cấu lại)'이라는 완곡한 표현이 선호된다.",
            "meaningVi": "Quá trình chuyển đổi doanh nghiệp nhà nước thành công ty cổ phần, trong đó một phần hoặc toàn bộ vốn của Nhà nước được bán cho các nhà đầu tư tư nhân. Đây là một phần quan trọng của cải cách kinh tế Việt Nam, nhằm nâng cao hiệu quả hoạt động và huy động vốn từ xã hội.",
            "context": "경제개혁, 국영기업 구조조정, 자본시장, 소유권 이전",
            "culturalNote": "한국에서는 '민영화'라는 용어가 직설적으로 사용되지만, 베트남에서는 '주식화(cổ phần hóa)'라는 우회적 표현을 쓴다. 이는 사회주의 체제 내에서 민영화를 추진하는 정치적 민감성을 반영한 것이다. 한국의 민영화는 대부분 완전 매각이지만, 베트남은 정부가 일정 지분(보통 51% 이상)을 유지하는 경우가 많아 실질적으로는 '부분 민영화'에 가깝다. 통역 시 이러한 차이를 설명하지 않으면 한국 측이 완전 민영화로 오해할 수 있다.",
            "commonMistakes": [
                {
                    "mistake": "'tư nhân hóa'로 번역",
                    "correction": "'cổ phần hóa' 사용",
                    "explanation": "tư nhân hóa는 완전 민영화를 뜻하며 정치적으로 민감하므로, 공식적으로는 cổ phần hóa를 사용한다."
                },
                {
                    "mistake": "완전 매각으로 통역",
                    "correction": "부분 지분 매각 여부 확인 후 통역",
                    "explanation": "베트남의 cổ phần hóa는 대부분 부분 민영화를 의미하므로 맥락 확인이 필요하다."
                },
                {
                    "mistake": "'사유화'로 통역",
                    "correction": "'민영화' 또는 '주식화' 사용",
                    "explanation": "'사유화'는 부정적 뉘앙스가 강하므로 중립적인 용어를 사용해야 한다."
                }
            ],
            "examples": [
                {
                    "ko": "정부는 올해 10개 국영기업의 민영화를 추진할 계획입니다.",
                    "vi": "Chính phủ có kế hoạch thực hiện cổ phần hóa 10 doanh nghiệp nhà nước trong năm nay.",
                    "situation": "formal"
                },
                {
                    "ko": "민영화 후에도 정부가 51%의 지분을 유지합니다.",
                    "vi": "Sau cổ phần hóa, Chính phủ vẫn nắm giữ 51% cổ phần chi phối.",
                    "situation": "formal"
                },
                {
                    "ko": "이 기업은 내년 1분기에 민영화될 예정입니다.",
                    "vi": "Doanh nghiệp này dự kiến được cổ phần hóa trong quý 1 năm sau.",
                    "situation": "formal"
                }
            ],
            "relatedTerms": ["doanh-nghiep-nha-nuoc", "co-phan", "co-dong", "cai-cach-kinh-te", "co-cau-lai"]
        },
        {
            "slug": "dau-thau-cong",
            "korean": "공공입찰",
            "vietnamese": "đấu thầu công",
            "hanja": "公共入札",
            "hanjaReading": "公(공평할 공) + 共(함께 공) + 入(들 입) + 札(찰 찰)",
            "pronunciation": "더우 타우 꽁",
            "meaningKo": "공공기관이 재화나 서비스를 구매하기 위해 실시하는 경쟁적 입찰 절차. 통역 시 주의할 점은 베트남에서는 '공공입찰(đấu thầu công)'과 '공개입찰(đấu thầu rộng rãi)', '제한입찰(đấu thầu hạn chế)' 등을 명확히 구분한다는 점이다. 또한 베트남 입찰법(Luật Đấu thầu)에 따라 일정 금액 이상의 공공사업은 반드시 입찰을 거쳐야 하며, 입찰 절차 위반 시 형사처벌 대상이 될 수 있다. 한국의 '나라장터' 시스템과 유사한 베트남의 'Hệ thống mạng đấu thầu quốc gia' 시스템이 있으며, 통역 시 이를 언급하면 이해를 돕는다.",
            "meaningVi": "Quy trình lựa chọn nhà thầu, nhà cung cấp hàng hóa, dịch vụ cho các dự án, gói thầu được đầu tư bằng vốn nhà nước hoặc có sử dụng tài sản nhà nước thông qua hình thức đấu thầu công khai, minh bạch. Đây là biện pháp quan trọng nhằm đảm bảo hiệu quả, công bằng và chống tham nhũng trong mua sắm công.",
            "context": "공공조달, 정부 프로젝트, 건설공사, 용역계약",
            "culturalNote": "한국에서는 '입찰'이라는 용어가 일반적이지만, 베트남에서는 '경쟁(đấu thầu)'이라는 표현을 사용한다. 베트남의 공공입찰 제도는 부패 방지를 위해 매우 엄격하게 운영되며, 입찰 참가 자격, 평가 기준, 계약 이행 등 모든 과정이 법으로 세밀하게 규정되어 있다. 한국 기업이 베트남 공공입찰에 참여할 때는 현지 파트너와의 컨소시엄 구성이 유리하며, 입찰 담보금(bảo lãnh dự thầu) 및 계약 이행 보증(bảo lãnh thực hiện hợp đồng) 제도를 반드시 이해해야 한다.",
            "commonMistakes": [
                {
                    "mistake": "'đấu giá'로 번역",
                    "correction": "'đấu thầu' 사용",
                    "explanation": "đấu giá는 경매(auction)를 의미하므로, 공공입찰은 đấu thầu로 표현해야 한다."
                },
                {
                    "mistake": "'công khai'만으로 번역",
                    "correction": "'đấu thầu công' 또는 'đấu thầu công khai' 사용",
                    "explanation": "'công khai'는 공개를 의미할 뿐 입찰의 의미가 없으므로 부정확하다."
                },
                {
                    "mistake": "입찰 방식 구분 없이 통역",
                    "correction": "공개입찰/제한입찰/지명입찰 구분 필요",
                    "explanation": "베트남 입찰법은 입찰 방식을 명확히 구분하므로, 통역 시 정확한 방식을 확인해야 한다."
                }
            ],
            "examples": [
                {
                    "ko": "이 프로젝트는 공공입찰을 통해 시공사를 선정할 예정입니다.",
                    "vi": "Dự án này sẽ lựa chọn nhà thầu thi công thông qua đấu thầu công.",
                    "situation": "formal"
                },
                {
                    "ko": "공공입찰 참가 신청 기한은 다음 달 15일까지입니다.",
                    "vi": "Thời hạn nộp hồ sơ dự thầu công là đến ngày 15 tháng sau.",
                    "situation": "formal"
                },
                {
                    "ko": "공공입찰법 위반으로 계약이 취소되었습니다.",
                    "vi": "Hợp đồng bị hủy bỏ do vi phạm Luật Đấu thầu.",
                    "situation": "formal"
                }
            ],
            "relatedTerms": ["mua-sam-cong", "hop-dong-BOT", "nha-thau", "goi-thau", "bao-lanh-du-thau"]
        },
        {
            "slug": "mua-sam-cong",
            "korean": "공공조달",
            "vietnamese": "mua sắm công",
            "hanja": "公共調達",
            "hanjaReading": "公(공평할 공) + 共(함께 공) + 調(고를 조) + 達(이룰 달)",
            "pronunciation": "무아 삼 꽁",
            "meaningKo": "공공기관이 업무 수행을 위해 필요한 재화나 서비스를 구매하는 활동. 통역 시 주의할 점은 베트남에서는 '조달(mua sắm)'이라는 용어가 한국보다 광범위하게 사용되며, 입찰뿐만 아니라 직접 구매, 가격 견적 등 다양한 구매 방식을 포괄한다는 점이다. 한국의 '나라장터'에 해당하는 베트남의 '국가조달시스템(Hệ thống mạng đấu thầu quốc gia)'은 2019년부터 전면 전자화되었으며, 모든 공공조달은 이 시스템을 통해 공개된다. 통역 시 조달 금액에 따라 입찰 방식이 달라지는 규정을 설명하면 이해를 돕는다.",
            "meaningVi": "Hoạt động mua sắm hàng hóa, xây lắp, dịch vụ tư vấn và dịch vụ phi tư vấn của các cơ quan, tổ chức, đơn vị sử dụng vốn nhà nước hoặc có sử dụng tài sản nhà nước. Mua sắm công phải tuân thủ các quy định của pháp luật về đấu thầu, đảm bảo công khai, minh bạch, cạnh tranh, công bằng và hiệu quả kinh tế.",
            "context": "정부 구매, 예산 집행, 공공사업, 물품 및 서비스 계약",
            "culturalNote": "한국에서는 '조달'과 '구매'가 어느 정도 구분되지만, 베트남에서는 'mua sắm'이 통합적으로 사용된다. 베트남의 공공조달 시스템은 세계은행과 ADB의 지원으로 구축되어 국제 기준을 따르고 있으며, 전자조달 비율이 매우 높다. 한국 기업이 베트남 공공조달 시장에 진출할 때는 현지 법인 설립 또는 현지 대리인 지정이 필요한 경우가 많으며, 베트남산 제품 우대 정책(ưu đãi hàng nội địa)도 고려해야 한다. 통역 시 이러한 제도적 차이를 설명하지 않으면 한국 측이 시장 진입 장벽을 과소평가할 수 있다.",
            "commonMistakes": [
                {
                    "mistake": "'mua bán công'으로 번역",
                    "correction": "'mua sắm công' 사용",
                    "explanation": "mua bán은 매매를 의미하며, 공공조달은 구매(mua sắm)로 표현해야 한다."
                },
                {
                    "mistake": "'đấu thầu'와 혼용",
                    "correction": "mua sắm은 조달 전체, đấu thầu는 입찰 절차",
                    "explanation": "mua sắm công은 포괄적 개념이고, đấu thầu는 그 중 한 방식이다."
                },
                {
                    "mistake": "국가별 제도 차이 무시",
                    "correction": "베트남 특유의 규정과 절차 설명 추가",
                    "explanation": "양국의 조달 제도는 자격 요건, 우대 정책 등에서 차이가 크다."
                }
            ],
            "examples": [
                {
                    "ko": "공공조달 투명성 강화를 위해 전자시스템이 도입되었습니다.",
                    "vi": "Hệ thống điện tử đã được áp dụng để tăng cường minh bạch trong mua sắm công.",
                    "situation": "formal"
                },
                {
                    "ko": "이 장비는 공공조달 절차를 통해 구매됩니다.",
                    "vi": "Thiết bị này sẽ được mua thông qua quy trình mua sắm công.",
                    "situation": "formal"
                },
                {
                    "ko": "공공조달 시장 규모는 연간 약 100억 달러입니다.",
                    "vi": "Quy mô thị trường mua sắm công khoảng 100 tỷ USD mỗi năm.",
                    "situation": "formal"
                }
            ],
            "relatedTerms": ["dau-thau-cong", "hop-dong-cung-cap", "he-thong-dau-thau", "nha-cung-cap", "goi-thau"]
        },
        {
            "slug": "von-nha-nuoc",
            "korean": "국유자산",
            "vietnamese": "vốn nhà nước",
            "hanja": "國有資産",
            "hanjaReading": "國(나라 국) + 有(있을 유) + 資(재물 자) + 産(날 산)",
            "pronunciation": "번 냐 느억",
            "meaningKo": "국가가 소유하고 관리하는 자산. 통역 시 주의할 점은 베트남에서 'vốn nhà nước'는 국가 자본을 의미하지만, 실무에서는 국유재산 전반을 지칭하는 경우가 많다는 점이다. 베트남에서는 국유자산 관리법(Luật Quản lý, sử dụng tài sản công)에 따라 국유자산의 분류, 평가, 처분 등이 엄격히 규제되며, 국유자산 유용이나 횡령은 중대 범죄로 처벌된다. 통역 시 'vốn'(자본)과 'tài sản'(재산)의 구분을 명확히 하고, 문맥에 따라 적절한 용어를 선택해야 한다.",
            "meaningVi": "Toàn bộ tài sản, vốn do Nhà nước làm chủ sở hữu, bao gồm vốn đầu tư vào doanh nghiệp nhà nước, tài sản công, quỹ đất công, và các tài sản khác do Nhà nước quản lý. Vốn nhà nước phải được quản lý chặt chẽ, sử dụng hiệu quả và bảo toàn, tăng trưởng theo quy định của pháp luật.",
            "context": "국가재산 관리, 공기업 자본, 예산 편성, 민영화",
            "culturalNote": "한국에서는 '국유재산'이라는 용어가 명확하게 정의되어 있지만, 베트남에서는 'vốn nhà nước'(국가 자본)와 'tài sản công'(공공재산)이 혼용되는 경우가 많다. 법적으로는 구분되지만 실무에서는 포괄적으로 사용되므로 통역 시 맥락 파악이 중요하다. 베트남은 국유자산 유실을 방지하기 위해 재산 평가, 처분, 임대 등에 대한 규제가 매우 엄격하며, 특히 토지(đất công)는 국가 소유가 원칙이므로 토지 관련 통역 시 주의가 필요하다.",
            "commonMistakes": [
                {
                    "mistake": "'tài sản quốc gia'로 번역",
                    "correction": "'vốn nhà nước' 또는 'tài sản công' 사용",
                    "explanation": "tài sản quốc gia는 국가 재산을 의미하지만, 법률 용어로는 vốn nhà nước가 정확하다."
                },
                {
                    "mistake": "'vốn'과 'tài sản' 구분 없이 통역",
                    "correction": "자본은 vốn, 재산은 tài sản으로 구분",
                    "explanation": "vốn은 금전적 자본, tài sản은 물적 재산을 의미하므로 맥락에 따라 구분해야 한다."
                },
                {
                    "mistake": "토지 소유권을 한국식으로 설명",
                    "correction": "베트남은 토지 국유제 원칙 설명 필수",
                    "explanation": "베트남에서 토지는 국가 소유이므로, 사용권만 거래되는 점을 명확히 해야 한다."
                }
            ],
            "examples": [
                {
                    "ko": "국유자산의 효율적 관리가 경제 발전에 중요합니다.",
                    "vi": "Quản lý hiệu quả vốn nhà nước là quan trọng cho phát triển kinh tế.",
                    "situation": "formal"
                },
                {
                    "ko": "민영화 과정에서 국유자산 가치 평가가 진행됩니다.",
                    "vi": "Trong quá trình cổ phần hóa, việc định giá vốn nhà nước được thực hiện.",
                    "situation": "formal"
                },
                {
                    "ko": "국유자산 유용 혐의로 조사를 받고 있습니다.",
                    "vi": "Đang bị điều tra về hành vi tham ô vốn nhà nước.",
                    "situation": "formal"
                }
            ],
            "relatedTerms": ["doanh-nghiep-nha-nuoc", "tai-san-cong", "quan-ly-von", "dinh-gia-tai-san", "co-phan-hoa"]
        },
        {
            "slug": "kiem-toan-nha-nuoc",
            "korean": "감사원",
            "vietnamese": "kiểm toán nhà nước",
            "hanja": "監査院",
            "hanjaReading": "監(볼 감) + 査(살필 사) + 院(집 원)",
            "pronunciation": "끼엠 또안 냐 느억",
            "meaningKo": "국가의 재정 및 공공기관의 업무를 감사하는 최고 감사기구. 통역 시 주의할 점은 베트남어로는 '국가감사(kiểm toán nhà nước)'라고 하며, 기관명은 'Kiểm toán Nhà nước Việt Nam(베트남 국가감사원)'이라는 점이다. 한국의 감사원은 대통령 소속 독립기관이지만, 베트남 국가감사원은 국회에 직속되어 있어 제도적 위상이 다르다. 베트남 감사원은 재정 감사뿐만 아니라 국영기업, 공공프로젝트, 정부 지출 전반에 대해 매우 강력한 조사권을 가지며, 감사 결과는 국회에 보고되어 정치적 파장이 큰 경우가 많다.",
            "meaningVi": "Cơ quan cao nhất của Nhà nước thực hiện kiểm toán hoạt động quản lý, sử dụng tài chính, tài sản công. Kiểm toán Nhà nước hoạt động độc lập, chịu trách nhiệm trước Quốc hội. Nhiệm vụ chính là kiểm toán ngân sách nhà nước, doanh nghiệp nhà nước, dự án đầu tư công và các đơn vị sử dụng vốn, tài sản nhà nước.",
            "context": "재정감사, 부패방지, 국가예산, 공공사업 감독",
            "culturalNote": "한국의 감사원과 베트남의 Kiểm toán Nhà nước는 명칭은 유사하지만 소속과 권한이 다르다. 한국 감사원은 대통령 소속이지만, 베트남 감사원은 국회 소속으로 입법부의 재정 감시 기능을 수행한다. 베트남에서는 감사원의 감사 결과가 언론에 대대적으로 보도되며, 고위 공직자의 부패 적발로 이어지는 경우가 많아 정치적 영향력이 크다. 통역 시 양국 기관의 제도적 차이를 설명하지 않으면, 한국 측이 베트남 감사원의 권한과 독립성을 오해할 수 있다.",
            "commonMistakes": [
                {
                    "mistake": "'감사원'을 고유명사로만 통역",
                    "correction": "'kiểm toán nhà nước' 또는 기관명 'Kiểm toán Nhà nước' 구분",
                    "explanation": "기관명인지 기능인지에 따라 대문자 표기를 구분해야 한다."
                },
                {
                    "mistake": "'thanh tra'로 번역",
                    "correction": "'kiểm toán' 사용",
                    "explanation": "thanh tra는 일반적인 감독/조사를 의미하고, kiểm toán은 회계/재정 감사를 뜻한다."
                },
                {
                    "mistake": "한국 감사원과 동일한 위상으로 설명",
                    "correction": "소속과 권한의 차이 설명 필요",
                    "explanation": "한국은 대통령 소속, 베트남은 국회 소속으로 제도적 차이가 크다."
                }
            ],
            "examples": [
                {
                    "ko": "감사원이 해당 프로젝트에 대한 감사를 실시합니다.",
                    "vi": "Kiểm toán Nhà nước sẽ tiến hành kiểm toán dự án này.",
                    "situation": "formal"
                },
                {
                    "ko": "감사원 보고서에 따르면 예산 집행에 문제가 있었습니다.",
                    "vi": "Theo báo cáo của Kiểm toán Nhà nước, có vấn đề trong việc thực hiện ngân sách.",
                    "situation": "formal"
                },
                {
                    "ko": "감사원이 국영기업의 재무제표를 감사했습니다.",
                    "vi": "Kiểm toán Nhà nước đã kiểm toán báo cáo tài chính của doanh nghiệp nhà nước.",
                    "situation": "formal"
                }
            ],
            "relatedTerms": ["thanh-tra", "ngan-sach-nha-nuoc", "kiem-soat-tai-chinh", "bao-cao-kiem-toan", "phong-chong-tham-nhung"]
        },
        {
            "slug": "ngan-sach-nha-nuoc",
            "korean": "국가예산",
            "vietnamese": "ngân sách nhà nước",
            "hanja": "國家豫算",
            "hanjaReading": "國(나라 국) + 家(집 가) + 豫(미리 예) + 算(셈 산)",
            "pronunciation": "응안 삭 냐 느억",
            "meaningKo": "국가의 1년간 수입과 지출 계획. 통역 시 주의할 점은 베트남의 예산 편성과 승인 절차가 한국과 다르다는 점이다. 베트남은 매년 국회에서 예산안을 심의하고 승인하며, 중앙예산과 지방예산이 명확히 구분된다. 특히 베트남은 'dự toán ngân sách'(예산안)와 'quyết toán ngân sách'(결산)를 엄격히 구분하므로, 통역 시 '예산안'인지 '확정 예산'인지 명확히 해야 한다. 또한 베트남은 재정 적자 한도가 GDP의 4%로 법으로 정해져 있어, 예산 논의 시 자주 언급된다.",
            "meaningVi": "Dự toán các khoản thu, chi của Nhà nước trong một năm, được Quốc hội quyết định. Ngân sách nhà nước bao gồm ngân sách trung ương và ngân sách địa phương, phản ánh chính sách kinh tế - xã hội của Nhà nước. Việc lập, phân bổ, chấp hành và quyết toán ngân sách phải tuân thủ Luật Ngân sách Nhà nước.",
            "context": "재정정책, 예산 편성, 세금, 공공지출, 국회 심의",
            "culturalNote": "한국과 베트남 모두 예산은 국회에서 승인되지만, 예산 구조와 운영 방식에 차이가 있다. 베트남은 중앙정부와 지방정부 예산이 법적으로 분리되어 있으며, 지방예산의 자율성이 상대적으로 높다. 한국의 경우 특별회계, 기금 등이 복잡하게 운영되지만, 베트남은 예산 체계가 비교적 단순하다. 베트남에서는 예산 심의 과정에서 국회의원들이 매우 세부적인 항목까지 질의하고 수정을 요구하는 경우가 많으며, 예산 집행 과정도 감사원의 엄격한 감시를 받는다.",
            "commonMistakes": [
                {
                    "mistake": "'ngân hàng nhà nước'와 혼동",
                    "correction": "ngân sách는 예산, ngân hàng은 은행",
                    "explanation": "발음이 유사하지만 ngân sách(예산)와 ngân hàng(은행)은 완전히 다른 개념이다."
                },
                {
                    "mistake": "'dự toán'과 'quyết toán' 구분 없이 통역",
                    "correction": "dự toán은 예산안, quyết toán은 결산",
                    "explanation": "베트남에서는 예산안과 결산을 명확히 구분하므로, 통역 시 정확한 용어를 사용해야 한다."
                },
                {
                    "mistake": "중앙예산과 지방예산 구분 없이 통역",
                    "correction": "ngân sách trung ương/địa phương 명시",
                    "explanation": "베트남은 중앙과 지방 예산이 법적으로 분리되어 있으므로 구분이 중요하다."
                }
            ],
            "examples": [
                {
                    "ko": "국회가 내년도 국가예산안을 승인했습니다.",
                    "vi": "Quốc hội đã thông qua dự toán ngân sách nhà nước năm sau.",
                    "situation": "formal"
                },
                {
                    "ko": "국가예산 중 교육 부문 지출이 20%를 차지합니다.",
                    "vi": "Chi ngân sách nhà nước cho giáo dục chiếm 20%.",
                    "situation": "formal"
                },
                {
                    "ko": "재정 적자가 GDP의 3.5%로 예상됩니다.",
                    "vi": "Thủ ngân sách dự kiến ở mức 3,5% GDP.",
                    "situation": "formal"
                }
            ],
            "relatedTerms": ["du-toan-ngan-sach", "quyet-toan", "thue", "chi-tieu-cong", "tai-khoan-ngân-sach"]
        },
        {
            "slug": "ke-hoach-dau-tu-cong",
            "korean": "공공투자계획",
            "vietnamese": "kế hoạch đầu tư công",
            "hanja": "公共投資計劃",
            "hanjaReading": "公(공평할 공) + 共(함께 공) + 投(던질 투) + 資(재물 자) + 計(셀 계) + 劃(그을 획)",
            "pronunciation": "께 호악 더우 뜨 꽁",
            "meaningKo": "국가가 공공 인프라 및 사회 발전을 위해 수립하는 투자 계획. 통역 시 주의할 점은 베트남에서 공공투자는 5개년 계획과 연계되어 매우 체계적으로 관리된다는 점이다. 베트남은 2021년 공공투자법(Luật Đầu tư công)을 개정하여 투자 효율성과 투명성을 강화했으며, 모든 공공투자 프로젝트는 국회 또는 총리의 승인을 받아야 한다. 통역 시 'kế hoạch đầu tư trung hạn'(중기투자계획)과 'kế hoạch đầu tư hàng năm'(연간투자계획)을 구분하고, 투자 자금 출처(vốn ngân sách, vốn ODA, vốn PPP 등)도 명확히 해야 한다.",
            "meaningVi": "Kế hoạch phân bổ và sử dụng vốn đầu tư công trong một thời kỳ nhất định để xây dựng kết cấu hạ tầng kinh tế - xã hội, phục vụ phát triển đất nước. Kế hoạch đầu tư công được lập theo kỳ 5 năm và hàng năm, phải đảm bảo phù hợp với chiến lược, quy hoạch phát triển kinh tế - xã hội và khả năng cân đối nguồn vốn.",
            "context": "국가 인프라, 사회발전 프로젝트, 예산 배분, 5개년 계획",
            "culturalNote": "베트남은 사회주의 계획경제의 전통을 유지하여 5개년 단위의 국가발전계획을 수립하며, 공공투자 계획도 이에 따라 중기적으로 관리된다. 한국은 예산이 매년 편성되지만, 베트남은 5개년 계획을 먼저 수립한 후 연간 계획으로 세분화하는 방식이다. 공공투자는 국회의 엄격한 승인과 감독을 받으며, 특히 대형 프로젝트(그룹 A, B, C 분류)는 투자 규모에 따라 승인 권한이 다르다. 통역 시 이러한 절차적 복잡성을 설명하지 않으면, 한국 기업이 프로젝트 승인 과정을 과소평가할 수 있다.",
            "commonMistakes": [
                {
                    "mistake": "'kế hoạch kinh doanh'로 번역",
                    "correction": "'kế hoạch đầu tư công' 사용",
                    "explanation": "kế hoạch kinh doanh은 사업 계획을 의미하며, 공공투자 계획과는 다르다."
                },
                {
                    "mistake": "5개년 계획과 연간 계획 구분 없이 통역",
                    "correction": "trung hạn(중기)/hàng năm(연간) 명시",
                    "explanation": "베트남의 투자 계획은 중기와 연간으로 구분되므로 정확히 표현해야 한다."
                },
                {
                    "mistake": "승인 권한 설명 생략",
                    "correction": "프로젝트 규모별 승인 기관 안내 필요",
                    "explanation": "베트남은 투자 규모에 따라 국회/총리/장관 승인으로 구분되므로 중요한 정보다."
                }
            ],
            "examples": [
                {
                    "ko": "정부가 2026-2030년 공공투자계획을 발표했습니다.",
                    "vi": "Chính phủ đã công bố kế hoạch đầu tư công giai đoạn 2026-2030.",
                    "situation": "formal"
                },
                {
                    "ko": "이 프로젝트는 공공투자계획에 포함되어 있습니다.",
                    "vi": "Dự án này được đưa vào kế hoạch đầu tư công.",
                    "situation": "formal"
                },
                {
                    "ko": "공공투자계획의 집행률이 저조합니다.",
                    "vi": "Tỷ lệ giải ngân kế hoạch đầu tư công còn thấp.",
                    "situation": "formal"
                }
            ],
            "relatedTerms": ["dau-tu-cong", "von-ngan-sach", "du-an-dau-tu", "giai-ngan", "ke-hoach-5-nam"]
        },
        {
            "slug": "hop-dong-BOT",
            "korean": "BOT계약",
            "vietnamese": "hợp đồng BOT",
            "hanja": None,
            "hanjaReading": None,
            "pronunciation": "험 동 비 오 떼",
            "meaningKo": "민간이 공공 인프라를 건설(Build)하고 일정 기간 운영(Operate)한 후 정부에 이전(Transfer)하는 계약 방식. 통역 시 주의할 점은 베트남어로도 'BOT'라는 영문 약어를 그대로 사용하지만, 정식 명칭은 'Xây dựng - Kinh doanh - Chuyển giao'라는 점이다. 베트남에서는 고속도로, 발전소, 수도 시설 등 대형 인프라 프로젝트에 BOT 방식이 널리 활용되며, 유사한 방식으로 BT(Build-Transfer), BTO(Build-Transfer-Operate), BOO(Build-Own-Operate) 등도 사용된다. 통역 시 운영 기간(thời gian nhượng quyền), 수익률(tỷ suất lợi nhuận), 위험 분담(phân bổ rủi ro) 등 핵심 조건을 명확히 해야 한다.",
            "meaningVi": "Hình thức hợp đồng đầu tư xây dựng công trình kết cấu hạ tầng, trong đó nhà đầu tư tư nhân xây dựng (Build) công trình bằng vốn của mình, kinh doanh khai thác (Operate) trong thời gian nhượng quyền để thu hồi vốn và lợi nhuận, sau đó chuyển giao (Transfer) công trình cho Nhà nước mà không phải bồi hoàn. Đây là hình thức PPP phổ biến ở Việt Nam, đặc biệt trong lĩnh vực giao thông và năng lượng.",
            "context": "인프라 개발, 민간투자, PPP, 고속도로, 발전소",
            "culturalNote": "한국과 베트남 모두 BOT 계약을 활용하지만, 계약 구조와 리스크 배분 방식에 차이가 있다. 베트남에서는 BOT 프로젝트의 통행료나 요금이 정부 승인을 받아야 하므로, 수익성 예측이 불확실한 경우가 많다. 또한 베트남은 토지 사용권 문제, 환경 영향 평가, 주민 보상 등으로 인해 프로젝트 착공이 지연되는 사례가 빈번하다. 한국 기업이 베트남 BOT 프로젝트에 참여할 때는 정치적 리스크(chính trị), 환율 리스크(tỷ giá), 법률 변경 리스크(thay đổi pháp luật)를 반드시 고려해야 한다.",
            "commonMistakes": [
                {
                    "mistake": "'BOT'를 베트남어로 풀어서 설명만 함",
                    "correction": "'hợp đồng BOT' 또는 'BOT'로 표현",
                    "explanation": "실무에서는 'BOT'라는 약어가 표준으로 사용되므로, 이를 먼저 사용하는 것이 자연스럽다."
                },
                {
                    "mistake": "BT, BTO, BOO 등 다른 방식과 구분 없이 통역",
                    "correction": "계약 방식별 차이점 명확히 구분",
                    "explanation": "이전 시점과 소유권이 다르므로, 각 방식의 특징을 정확히 전달해야 한다."
                },
                {
                    "mistake": "운영 기간을 명시하지 않음",
                    "correction": "nhượng quyền [X]năm 등 기간 포함",
                    "explanation": "BOT의 핵심은 운영 기간이므로, 통역 시 반드시 언급해야 한다."
                }
            ],
            "examples": [
                {
                    "ko": "이 고속도로는 30년 BOT계약으로 건설됩니다.",
                    "vi": "Đường cao tốc này sẽ được xây dựng theo hợp đồng BOT với thời gian nhượng quyền 30 năm.",
                    "situation": "formal"
                },
                {
                    "ko": "BOT계약에 따라 회사는 25년간 시설을 운영할 수 있습니다.",
                    "vi": "Theo hợp đồng BOT, công ty được quyền khai thác công trình trong 25 năm.",
                    "situation": "formal"
                },
                {
                    "ko": "BOT 방식으로 발전소를 건설하는 제안이 승인되었습니다.",
                    "vi": "Đề xuất xây dựng nhà máy điện theo hình thức BOT đã được phê duyệt.",
                    "situation": "formal"
                }
            ],
            "relatedTerms": ["doi-tac-cong-tu", "dau-tu-tu-nhan", "nhuong-quyen", "ha-tang-co-so", "hop-dong-BT"]
        },
        {
            "slug": "doi-tac-cong-tu",
            "korean": "민관협력",
            "vietnamese": "đối tác công tư",
            "hanja": "民官協力",
            "hanjaReading": "民(백성 민) + 官(벼슬 관) + 協(협력할 협) + 力(힘 력)",
            "pronunciation": "도이 딱 꽁 뜨",
            "meaningKo": "공공부문과 민간부문이 협력하여 공공서비스나 인프라를 제공하는 방식. 통역 시 주의할 점은 베트남어로 PPP(Public-Private Partnership)를 'đối tác công tư'라고 번역하며, 이는 BOT, BT, BTO 등 다양한 계약 방식을 포괄하는 상위 개념이라는 점이다. 베트남은 2020년 PPP법(Luật Đầu tư theo phương thức đối tác công tư)을 제정하여 민관협력 사업의 법적 근거를 마련했으며, 교통, 보건, 교육, 환경 등 다양한 분야에서 활용되고 있다. 통역 시 'đối tác'(파트너십)라는 용어가 협력의 평등성을 강조한다는 점을 이해하고, 계약 당사자 간 권리와 의무를 명확히 전달해야 한다.",
            "meaningVi": "Hình thức hợp tác giữa cơ quan nhà nước và nhà đầu tư tư nhân để cung cấp sản phẩm, dịch vụ công trên cơ sở chia sẻ nguồn lực, rủi ro và lợi ích. PPP được áp dụng rộng rãi trong các dự án kết cấu hạ tầng, y tế, giáo dục, môi trường nhằm huy động nguồn lực xã hội và nâng cao hiệu quả đầu tư công. Luật PPP 2020 đã tạo khung pháp lý rõ ràng cho loại hình đầu tư này.",
            "context": "인프라 개발, 공공서비스, 민간투자, 정부 파트너십",
            "culturalNote": "한국에서는 '민관협력' 또는 'PPP'라는 용어가 일반적이지만, 베트남에서는 'đối tác công tư'(공공-민간 파트너십)라는 표현을 사용한다. 베트남의 PPP 제도는 세계은행과 ADB의 지원으로 개발되어 국제 기준에 부합하지만, 실무 운영에서는 여전히 정부의 통제가 강하고 민간의 경영 자율성이 제한적인 경우가 많다. 한국 기업이 베트남 PPP 프로젝트에 참여할 때는 정부 보증(bảo lãnh chính phủ), 환율 조정(điều chỉnh tỷ giá), 수요 보장(đảm bảo nhu cầu) 등 리스크 완화 조치를 반드시 협상해야 한다.",
            "commonMistakes": [
                {
                    "mistake": "'hợp tác công tư'로 번역",
                    "correction": "'đối tác công tư' 사용",
                    "explanation": "공식 법률 용어는 đối tác이며, hợp tác은 일반적인 협력을 의미한다."
                },
                {
                    "mistake": "PPP를 BOT와 동일한 개념으로 설명",
                    "correction": "PPP는 상위 개념, BOT는 하위 방식 중 하나",
                    "explanation": "PPP는 다양한 계약 방식을 포괄하는 개념이므로 구분이 필요하다."
                },
                {
                    "mistake": "리스크 분담 구조 설명 생략",
                    "correction": "chia sẻ rủi ro(리스크 분담) 강조 필요",
                    "explanation": "PPP의 핵심은 리스크와 수익의 분담이므로, 이를 명확히 전달해야 한다."
                }
            ],
            "examples": [
                {
                    "ko": "정부는 민관협력 방식으로 병원을 건설할 계획입니다.",
                    "vi": "Chính phủ có kế hoạch xây dựng bệnh viện theo phương thức đối tác công tư.",
                    "situation": "formal"
                },
                {
                    "ko": "민관협력 사업은 양측의 리스크 분담을 전제로 합니다.",
                    "vi": "Dự án đối tác công tư dựa trên nguyên tắc chia sẻ rủi ro giữa hai bên.",
                    "situation": "formal"
                },
                {
                    "ko": "새로운 민관협력법이 투자 환경을 개선할 것으로 기대됩니다.",
                    "vi": "Luật PPP mới được kỳ vọng sẽ cải thiện môi trường đầu tư.",
                    "situation": "formal"
                }
            ],
            "relatedTerms": ["hop-dong-BOT", "dau-tu-tu-nhan", "du-an-ha-tang", "chia-se-rui-ro", "hop-tac-dau-tu"]
        }
    ]

    # 5. 중복 제거
    new_terms_filtered = [t for t in new_terms if t['slug'] not in existing_slugs]

    print(f"기존 용어 수: {len(data)}")
    print(f"추가할 용어 수: {len(new_terms_filtered)}")

    if not new_terms_filtered:
        print("중복 제거 후 추가할 용어가 없습니다.")
        return

    # 6. 데이터 병합
    data.extend(new_terms_filtered)

    # 7. 파일 저장
    with open(file_path, 'w', encoding='utf-8') as f:
        json.dump(data, f, ensure_ascii=False, indent=2)

    print(f"✅ {len(new_terms_filtered)}개 용어 추가 완료!")
    print(f"총 용어 수: {len(data)}")

    # 추가된 용어 목록 출력
    print("\n추가된 용어:")
    for term in new_terms_filtered:
        print(f"  - {term['slug']} ({term['korean']} / {term['vietnamese']})")

if __name__ == '__main__':
    main()
