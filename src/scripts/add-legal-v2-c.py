#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
투자법/외국인투자 분야 전문용어 추가 스크립트
Theme: Investment Law/Foreign Investment
"""

import json
import os

# CRITICAL: Construct path relative to script location
file_path = os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', 'data', 'terms', 'legal.json')

# Load existing data
with open(file_path, 'r', encoding='utf-8') as f:
    data = json.load(f)  # data is a LIST, not dict!

# Extract existing slugs to prevent duplicates
existing_slugs = {t['slug'] for t in data}

# New terms - Investment Law/Foreign Investment (10 terms)
new_terms = [
    {
        "slug": "giay-chung-nhan-dau-tu",
        "korean": "투자등록증",
        "vietnamese": "giấy chứng nhận đầu tư",
        "hanja": "投資登錄證",
        "hanjaReading": "投(던질 투) + 資(밑천 자) + 登(오를 등) + 錄(기록할 록) + 證(증거 증)",
        "pronunciation": "지엉쭝년다우뜨",
        "meaningKo": "베트남에서 외국인 투자자가 사업을 시작하기 위해 필수적으로 받아야 하는 정부 발행 증명서. 투자법에 따라 계획투자부(MPI) 또는 각 성·시 인민위원회가 발급하며, 투자 규모, 업종, 자본금, 사업 기간 등이 명시됨. 통역 시 주의할 점은 이 서류가 사업자등록증(giấy phép kinh doanh)과는 별개이며, 투자등록증을 먼저 받은 후 사업자등록을 해야 한다는 점을 명확히 구분해야 함. 한국의 외국인투자신고증명서와 유사하나 법적 효력과 절차가 다르므로 혼동하지 않도록 주의.",
        "meaningVi": "Giấy chứng nhận do cơ quan nhà nước có thẩm quyền cấp cho nhà đầu tư nước ngoài khi thực hiện dự án đầu tư tại Việt Nam. Văn bản này xác nhận quyền và nghĩa vụ của nhà đầu tư, nêu rõ các thông tin về ngành nghề, vốn đầu tư, địa điểm, thời gian thực hiện dự án. Giấy chứng nhận đầu tư là điều kiện bắt buộc để được cấp giấy phép kinh doanh và triển khai hoạt động đầu tư hợp pháp.",
        "context": "외국인직접투자(FDI) 절차, 투자 인허가 심사, 투자 프로젝트 승인 단계에서 사용",
        "culturalNote": "베트남은 투자등록증과 사업자등록증을 엄격히 분리하는 이원화 시스템을 운영하는 반면, 한국은 외국인투자신고 후 사업자등록을 통합적으로 처리하는 경향이 있음. 베트남에서는 투자등록증 없이 사업을 시작하면 불법으로 간주되어 강제 철수 및 벌금이 부과될 수 있으므로, 한국 기업들이 현지 진출 시 절차적 복잡성을 간과하지 않도록 통역사가 명확히 설명해야 함.",
        "commonMistakes": [
            {
                "mistake": "투자허가증으로 번역",
                "correction": "투자등록증으로 번역",
                "explanation": "'허가'는 giấy phép에 해당하며, giấy chứng nhận은 '증명서' 또는 '등록증'으로 번역하는 것이 정확함"
            },
            {
                "mistake": "사업자등록증과 혼동하여 같은 것으로 설명",
                "correction": "투자등록증(giấy chứng nhận đầu tư)과 사업자등록증(giấy phép kinh doanh)은 별개 서류임을 명시",
                "explanation": "베트남 법상 투자등록증을 먼저 받아야 사업자등록증 발급이 가능하므로 순서와 구분이 중요함"
            },
            {
                "mistake": "한국의 외국인투자신고증명서와 동일하다고 설명",
                "correction": "유사하나 법적 효력과 발급 절차가 다름을 강조",
                "explanation": "양국 제도의 차이를 이해하지 못하면 투자자가 잘못된 절차를 밟을 위험이 있음"
            }
        ],
        "examples": [
            {
                "ko": "투자등록증을 받는 데 보통 45일 정도 걸립니다.",
                "vi": "Thủ tục cấp giấy chứng nhận đầu tư thường mất khoảng 45 ngày.",
                "situation": "formal"
            },
            {
                "ko": "이 공장은 투자등록증 상 허가된 업종이 아니라서 문제가 생겼어요.",
                "vi": "Nhà máy này gặp vấn đề vì ngành nghề không được ghi trong giấy chứng nhận đầu tư.",
                "situation": "onsite"
            },
            {
                "ko": "투자등록증 내용을 변경하려면 추가 서류가 필요합니다.",
                "vi": "Để điều chỉnh nội dung giấy chứng nhận đầu tư cần bổ sung hồ sơ.",
                "situation": "formal"
            }
        ],
        "relatedTerms": ["giay-phep-kinh-doanh", "du-an-dau-tu", "nha-dau-tu-nuoc-ngoai"]
    },
    {
        "slug": "khu-cong-nghiep",
        "korean": "공업단지",
        "vietnamese": "khu công nghiệp",
        "hanja": "工業團地",
        "hanjaReading": "工(장인 공) + 業(업 업) + 團(둥글 단) + 地(땅 지)",
        "pronunciation": "쿠꽁응이엡",
        "meaningKo": "제조업 및 산업 활동을 집중적으로 유치하기 위해 정부가 지정한 특별 구역. 베트남에서는 외국인 투자 유치를 위해 인프라(도로, 전기, 용수, 폐수 처리)를 사전에 구축하고 세제 혜택을 제공함. 통역 시 주의할 점은 한국의 '산업단지'와 거의 동일한 개념이지만, 베트남에서는 공업단지 내 토지 임대료와 세금 혜택이 지역마다 크게 다르므로, 투자 상담 시 구체적인 단지명과 위치를 명확히 전달해야 함.",
        "meaningVi": "Khu vực được quy hoạch và đầu tư hạ tầng để thu hút các doanh nghiệp sản xuất, chế biến. Các khu công nghiệp thường có ưu đãi về thuế, đất đai và được nhà nước hỗ trợ về điện, nước, xử lý chất thải. Đây là mô hình quan trọng trong chiến lược công nghiệp hóa, thu hút đầu tư nước ngoài.",
        "context": "외국인투자 유치, 공장 설립 절차, 부동산 임대 계약 논의 시 사용",
        "culturalNote": "베트남의 공업단지는 북부(바박, 하노이), 남부(빈증, 동나이, 빈즈엉), 중부(다낭) 등 지역별로 산업 특성과 인센티브가 다름. 한국 기업들은 특히 북부의 삼성·LG 협력사 밀집 단지나 남부의 한국인 밀집 단지를 선호하는 경향이 있으며, 통역사는 각 단지의 특징(임대료, 노동력, 항구 접근성 등)을 숙지하여 투자 결정에 도움을 줄 수 있어야 함.",
        "commonMistakes": [
            {
                "mistake": "산업단지(khu công nghiệp)와 경제특구(khu kinh tế)를 혼동",
                "correction": "공업단지는 제조업 중심, 경제특구는 더 넓은 범위의 경제 활동 포함",
                "explanation": "경제특구는 무역, 서비스, 관광까지 포함하지만 공업단지는 제조업에 특화되어 있음"
            },
            {
                "mistake": "'공단'으로 축약하여 통역",
                "correction": "정식 명칭인 '공업단지'를 사용하거나 맥락에 따라 축약",
                "explanation": "공식 문서나 계약서에서는 정식 명칭을 사용해야 법적 명확성을 확보할 수 있음"
            },
            {
                "mistake": "모든 공업단지가 같은 혜택을 준다고 설명",
                "correction": "단지마다 세제 혜택, 임대료, 인프라 수준이 다름을 명시",
                "explanation": "투자자가 잘못된 기대를 갖지 않도록 구체적 정보 확인이 필요함"
            }
        ],
        "examples": [
            {
                "ko": "이 공업단지는 세금 감면 혜택이 15년간 적용됩니다.",
                "vi": "Khu công nghiệp này được miễn giảm thuế trong 15 năm.",
                "situation": "formal"
            },
            {
                "ko": "공업단지 안에 공장 부지를 임대할 계획입니다.",
                "vi": "Chúng tôi dự định thuê đất trong khu công nghiệp để xây nhà máy.",
                "situation": "formal"
            },
            {
                "ko": "이 공단은 항구에서 가까워서 물류비가 절감돼요.",
                "vi": "Khu công nghiệp này gần cảng nên tiết kiệm chi phí logistics.",
                "situation": "onsite"
            }
        ],
        "relatedTerms": ["khu-kinh-te-dac-biet", "giay-chung-nhan-dau-tu", "du-an-dau-tu"]
    },
    {
        "slug": "khu-kinh-te-dac-biet",
        "korean": "경제특구",
        "vietnamese": "khu kinh tế đặc biệt",
        "hanja": "經濟特區",
        "hanjaReading": "經(지날 경) + 濟(건널 제) + 特(특별할 특) + 區(구역 구)",
        "pronunciation": "쿠낀떼닥비엣",
        "meaningKo": "정부가 경제 발전을 가속화하기 위해 특별한 정책과 인센티브를 부여한 지리적 구역. 일반 공업단지보다 더 포괄적인 경제 활동(제조업, 무역, 서비스, 관광, 금융 등)이 가능하며, 세제 혜택, 행정 절차 간소화, 외환 규제 완화 등의 특례를 받음. 통역 시 주의할 점은 베트남의 경제특구는 한국의 경제자유구역과 유사하지만, 베트Nam에서는 중국과의 국경 지역이나 전략적 요충지에 주로 설치되어 정치적 민감성이 있을 수 있으므로, 투자 논의 시 지역적 특성을 고려해야 함.",
        "meaningVi": "Khu vực được nhà nước quy định có chính sách ưu đãi đặc biệt để thu hút đầu tư, phát triển kinh tế nhanh. Khu kinh tế có phạm vi rộng hơn khu công nghiệp, bao gồm sản xuất, thương mại, dịch vụ, du lịch, với các đặc quyền về thuế, thủ tục hành chính, ngoại hối.",
        "context": "외국인투자 정책 논의, 전략적 투자 유치, 대규모 프로젝트 협상 시 사용",
        "culturalNote": "베트남은 중국과의 경쟁에서 외국인 투자를 유치하기 위해 경제특구 제도를 적극 활용하고 있으며, 반짱(Vân Đồn), 박반(Bắc Vân Phong), 푸꾸옥(Phú Quốc) 등이 대표적 사례. 그러나 중국 자본 유입에 대한 국민적 우려로 인해 일부 경제특구 법안이 보류된 적도 있어, 투자 논의 시 정치적 배경을 이해하는 것이 중요함. 한국의 경제자유구역(인천, 부산 등)과 개념은 유사하나 운영 방식과 규제 수준에 차이가 있음.",
        "commonMistakes": [
            {
                "mistake": "공업단지와 경제특구를 같은 의미로 사용",
                "correction": "경제특구는 공업단지보다 범위가 넓고 더 많은 특혜를 받는 구역",
                "explanation": "경제특구는 제조업뿐 아니라 서비스업, 관광업 등 다양한 경제 활동이 가능함"
            },
            {
                "mistake": "'자유무역지대'로 번역",
                "correction": "'경제특구'가 정확한 번역",
                "explanation": "자유무역지대(khu mậu dịch tự do)는 무역에 특화된 개념이고, 경제특구는 더 포괄적임"
            },
            {
                "mistake": "모든 경제특구가 동일한 혜택을 제공한다고 설명",
                "correction": "각 경제특구마다 특화 산업과 혜택 수준이 다름",
                "explanation": "지역별 전략과 정부 정책에 따라 차이가 크므로 구체적 확인 필요"
            }
        ],
        "examples": [
            {
                "ko": "이 경제특구에서는 법인세가 10%로 감면됩니다.",
                "vi": "Tại khu kinh tế đặc biệt này, thuế thu nhập doanh nghiệp được giảm xuống 10%.",
                "situation": "formal"
            },
            {
                "ko": "푸꾸옥 경제특구는 관광과 리조트 개발에 유리해요.",
                "vi": "Khu kinh tế Phú Quốc có lợi thế trong phát triển du lịch và resort.",
                "situation": "onsite"
            },
            {
                "ko": "경제특구 투자는 행정 절차가 일반 지역보다 간소화되어 있습니다.",
                "vi": "Đầu tư vào khu kinh tế đặc biệt có thủ tục hành chính đơn giản hơn các khu vực thông thường.",
                "situation": "formal"
            }
        ],
        "relatedTerms": ["khu-cong-nghiep", "uu-dai-dau-tu", "giay-chung-nhan-dau-tu"]
    },
    {
        "slug": "von-dau-tu",
        "korean": "투자자본",
        "vietnamese": "vốn đầu tư",
        "hanja": "投資資本",
        "hanjaReading": "投(던질 투) + 資(밑천 자) + 資(밑천 자) + 本(근본 본)",
        "pronunciation": "번다우뜨",
        "meaningKo": "기업이나 개인이 사업을 시작하거나 확장하기 위해 투입하는 자금. 베트남 투자법상 외국인 투자자는 투자등록증에 명시된 자본금을 법정 기한 내에 실제로 입금해야 하며, 이를 이행하지 않으면 투자 허가가 취소될 수 있음. 통역 시 주의할 점은 '등록 자본(vốn điều lệ)'과 '실제 투입 자본(vốn thực góp)'을 명확히 구분해야 하며, 베트남에서는 자본금 변경 시 투자등록증 변경 절차가 필요하다는 점을 설명해야 함.",
        "meaningVi": "Số tiền mà nhà đầu tư cam kết bỏ ra để thực hiện dự án kinh doanh. Theo Luật Đầu tư, vốn đầu tư phải được đưa vào đúng thời hạn theo giấy chứng nhận đầu tư. Nếu không thực hiện đầy đủ, dự án có thể bị thu hồi giấy chứng nhận.",
        "context": "투자 계약 체결, 자본금 증액 논의, 재무 실사 과정에서 사용",
        "culturalNote": "베트남 투자법은 자본금 미이행에 대해 엄격한 처벌 규정을 두고 있어, 한국 기업들이 단계적 투자 계획을 세울 때 법적 리스크를 고려해야 함. 한국에서는 자본금 변경이 상대적으로 유연하지만, 베트남에서는 투자등록증 변경 절차를 거쳐야 하므로 시간과 비용이 추가로 발생함. 통역사는 이러한 절차적 차이를 명확히 전달하여 투자 일정에 차질이 없도록 해야 함.",
        "commonMistakes": [
            {
                "mistake": "'자본금'과 '투자자본'을 같은 의미로 사용",
                "correction": "'등록 자본(vốn điều lệ)'과 '투자자본(vốn đầu tư)'은 법적으로 구분됨",
                "explanation": "등록 자본은 정관에 기재된 금액, 투자자본은 실제 투입된 금액으로 맥락에 따라 다름"
            },
            {
                "mistake": "자본금 변경이 한국처럼 간단하다고 설명",
                "correction": "베트남에서는 투자등록증 변경 절차가 필요함을 명시",
                "explanation": "절차를 간과하면 투자 일정에 차질이 생기고 법적 문제가 발생할 수 있음"
            },
            {
                "mistake": "약속한 자본금을 기한 내 입금하지 않아도 괜찮다고 오해",
                "correction": "기한 내 미이행 시 투자 허가 취소 위험이 있음을 강조",
                "explanation": "베트남 당국은 자본금 이행을 엄격히 모니터링하며, 미이행 시 법적 제재가 가해짐"
            }
        ],
        "examples": [
            {
                "ko": "투자자본은 미화 500만 달러로 등록되어 있습니다.",
                "vi": "Vốn đầu tư được đăng ký là 5 triệu đô la Mỹ.",
                "situation": "formal"
            },
            {
                "ko": "자본금을 늘리려면 투자등록증 변경 절차를 밟아야 해요.",
                "vi": "Để tăng vốn đầu tư cần làm thủ tục điều chỉnh giấy chứng nhận đầu tư.",
                "situation": "onsite"
            },
            {
                "ko": "약속한 투자자본을 6개월 내에 입금하지 않으면 허가가 취소될 수 있습니다.",
                "vi": "Nếu không góp đủ vốn đầu tư trong 6 tháng, giấy chứng nhận có thể bị thu hồi.",
                "situation": "formal"
            }
        ],
        "relatedTerms": ["giay-chung-nhan-dau-tu", "nha-dau-tu-nuoc-ngoai", "du-an-dau-tu"]
    },
    {
        "slug": "loi-nhuan-chuyen-ra-nuoc-ngoai",
        "korean": "해외이익송금",
        "vietnamese": "lợi nhuận chuyển ra nước ngoài",
        "hanja": "海外利益送金",
        "hanjaReading": "海(바다 해) + 外(바깥 외) + 利(이로울 리) + 益(더할 익) + 送(보낼 송) + 金(쇠 금)",
        "pronunciation": "러이늬언추옌자느억응오아이",
        "meaningKo": "외국인 투자자가 베트남에서 벌어들인 이익을 본국이나 제3국으로 송금하는 것. 베트남 투자법은 외국인 투자자의 이익 송금권을 보장하지만, 세금 완납과 재무제표 제출 등의 조건을 충족해야 함. 통역 시 주의할 점은 '배당금 송금'과 '영업이익 송금'을 구분하고, 송금 시 법인세, 외국인계약자세(FCT), 원천징수세 등을 정확히 계산하여 실제 수령액을 명확히 전달해야 함. 한국 기업들이 자주 착오하는 부분이므로 세금 부담을 사전에 설명하는 것이 중요함.",
        "meaningVi": "Quyền chuyển lợi nhuận thu được tại Việt Nam về nước của nhà đầu tư nước ngoài. Luật Đầu tư bảo đảm quyền này nhưng yêu cầu hoàn thành nghĩa vụ thuế, nộp báo cáo tài chính đầy đủ. Việc chuyển lợi nhuận phải tuân thủ quy định về quản lý ngoại hối.",
        "context": "외환 송금 절차, 세무 자문, 투자 수익 정산 논의 시 사용",
        "culturalNote": "베트남은 외환 관리를 엄격히 하고 있어, 해외 송금 시 은행이 송금 목적과 관련 서류를 철저히 확인함. 한국은 외환 거래가 상대적으로 자유로운 반면, 베트남에서는 송금 한도, 증빙 서류, 세금 납부 확인 등 복잡한 절차를 거쳐야 함. 특히 대규모 송금 시 국세청과 외환 당국의 승인이 필요할 수 있으므로, 통역사는 이러한 절차적 복잡성을 사전에 설명하여 투자자가 송금 지연을 겪지 않도록 해야 함.",
        "commonMistakes": [
            {
                "mistake": "이익이 발생하면 즉시 송금 가능하다고 설명",
                "correction": "세금 완납과 재무제표 제출 등의 조건을 충족해야 송금 가능",
                "explanation": "조건 미충족 시 은행이 송금을 거부하거나 세무 당국의 조사를 받을 수 있음"
            },
            {
                "mistake": "'배당금'과 '영업이익 송금'을 구분하지 않음",
                "correction": "배당금(cổ tức)과 영업이익(lợi nhuận kinh doanh)은 세율과 송금 절차가 다름",
                "explanation": "배당금은 원천징수세가 적용되고, 영업이익 송금은 법인세 납부 후 가능"
            },
            {
                "mistake": "송금 시 세금 부담을 고려하지 않고 전액 송금 가능하다고 오해",
                "correction": "법인세, FCT, 원천징수세 등을 차감한 후 실제 수령액을 계산해야 함",
                "explanation": "세금을 고려하지 않으면 예상보다 적은 금액을 받게 되어 재무 계획에 차질이 생김"
            }
        ],
        "examples": [
            {
                "ko": "해외이익송금을 하려면 먼저 법인세를 완납해야 합니다.",
                "vi": "Để chuyển lợi nhuận ra nước ngoài, trước tiên phải hoàn thành nghĩa vụ thuế thu nhập doanh nghiệp.",
                "situation": "formal"
            },
            {
                "ko": "올해 이익 100억 동 중에서 70억 동만 실제로 송금할 수 있어요. 세금이 30%거든요.",
                "vi": "Trong 10 tỷ đồng lợi nhuận năm nay, chỉ chuyển được 7 tỷ đồng thôi vì thuế chiếm 30%.",
                "situation": "onsite"
            },
            {
                "ko": "이익 송금 신청 시 감사받은 재무제표를 제출해야 합니다.",
                "vi": "Khi đăng ký chuyển lợi nhuận cần nộp báo cáo tài chính đã kiểm toán.",
                "situation": "formal"
            }
        ],
        "relatedTerms": ["nha-dau-tu-nuoc-ngoai", "von-dau-tu", "giay-chung-nhan-dau-tu"]
    },
    {
        "slug": "nha-dau-tu-nuoc-ngoai",
        "korean": "외국인투자자",
        "vietnamese": "nhà đầu tư nước ngoài",
        "hanja": "外國人投資者",
        "hanjaReading": "外(바깥 외) + 國(나라 국) + 人(사람 인) + 投(던질 투) + 資(밑천 자) + 者(놈 자)",
        "pronunciation": "냐다우뜨느억응오아이",
        "meaningKo": "베트남 국적이 아닌 개인 또는 법인으로서 베트남에 자본을 투자하는 주체. 베트남 투자법은 외국인 투자자를 '외국 개인, 외국 법인, 베트남 거주 외국인, 외국 자본 51% 이상 기업' 등으로 정의함. 통역 시 주의할 점은 한국인이라도 베트남 영주권을 가지면 일부 조건에서 내국인 대우를 받을 수 있으므로, 투자자의 법적 지위를 정확히 파악하여 적용 가능한 혜택과 제한을 설명해야 함.",
        "meaningVi": "Cá nhân hoặc tổ chức không mang quốc tịch Việt Nam thực hiện đầu tư vào Việt Nam. Theo Luật Đầu tư, nhà đầu tư nước ngoài bao gồm cá nhân, doanh nghiệp nước ngoài, người Việt Nam định cư ở nước ngoài, và doanh nghiệp có vốn nước ngoài từ 51% trở lên.",
        "context": "투자 계약 협상, 법률 자문, 인허가 절차 논의 시 사용",
        "culturalNote": "베트남은 외국인 투자자에게 특정 업종(부동산, 미디어, 통신 등)에서 지분 제한을 두고 있으며, 업종별로 투자 조건이 상이함. 한국 투자자들은 제조업에서는 100% 외국인 지분이 가능하지만, 유통업이나 서비스업에서는 제한이 있을 수 있으므로 사전 확인이 필요함. 통역사는 투자자의 국적, 업종, 투자 규모에 따라 적용되는 법규가 다름을 이해하고, 필요 시 법률 자문을 권장해야 함.",
        "commonMistakes": [
            {
                "mistake": "모든 외국인이 동일한 투자 조건을 받는다고 설명",
                "correction": "업종, 지역, 투자 규모에 따라 조건이 다름",
                "explanation": "장려 업종과 제한 업종의 혜택과 규제가 크게 다르므로 구체적 확인 필요"
            },
            {
                "mistake": "베트남 영주권자도 무조건 외국인 투자자로 분류",
                "correction": "영주권자는 일부 조건에서 내국인 대우를 받을 수 있음",
                "explanation": "법적 지위에 따라 혜택과 제한이 달라지므로 정확한 분류가 중요함"
            },
            {
                "mistake": "'외국인투자기업'과 '외국인투자자'를 혼동",
                "correction": "'투자자'는 주체, '투자기업'은 설립된 법인",
                "explanation": "법적 책임과 권리가 다르므로 명확히 구분해야 함"
            }
        ],
        "examples": [
            {
                "ko": "외국인투자자는 제조업에서 100% 지분을 보유할 수 있습니다.",
                "vi": "Nhà đầu tư nước ngoài có thể nắm giữ 100% vốn trong lĩnh vực sản xuất.",
                "situation": "formal"
            },
            {
                "ko": "이 업종은 외국인투자자에게 지분 제한이 있어서 49%까지만 투자할 수 있어요.",
                "vi": "Ngành này có hạn chế về vốn, nhà đầu tư nước ngoài chỉ được đầu tư tối đa 49%.",
                "situation": "onsite"
            },
            {
                "ko": "외국인투자자는 투자등록증을 받아야 합법적으로 사업을 시작할 수 있습니다.",
                "vi": "Nhà đầu tư nước ngoài phải có giấy chứng nhận đầu tư mới được kinh doanh hợp pháp.",
                "situation": "formal"
            }
        ],
        "relatedTerms": ["giay-chung-nhan-dau-tu", "du-an-dau-tu", "von-dau-tu"]
    },
    {
        "slug": "giay-phep-kinh-doanh",
        "korean": "사업허가증",
        "vietnamese": "giấy phép kinh doanh",
        "hanja": "事業許可證",
        "hanjaReading": "事(일 사) + 業(업 업) + 許(허락할 허) + 可(옳을 가) + 證(증거 증)",
        "pronunciation": "지엉펩낀도안",
        "meaningKo": "베트남에서 기업이 합법적으로 사업 활동을 할 수 있도록 정부가 발급하는 허가 증명서. 외국인 투자자는 투자등록증을 먼저 받은 후 사업허가증을 발급받아야 하며, 사업허가증에는 사업자 정보, 업종, 사업장 주소 등이 명시됨. 통역 시 주의할 점은 한국의 '사업자등록증'과 유사하지만 법적 절차와 발급 기관이 다르며, 베트남에서는 업종 변경이나 사업장 이전 시 사업허가증을 변경해야 한다는 점을 명확히 설명해야 함.",
        "meaningVi": "Giấy tờ do cơ quan có thẩm quyền cấp cho doanh nghiệp để được phép hoạt động kinh doanh hợp pháp. Giấy phép kinh doanh ghi rõ thông tin doanh nghiệp, ngành nghề, địa chỉ trụ sở. Đối với doanh nghiệp có vốn nước ngoài, phải có giấy chứng nhận đầu tư trước khi được cấp giấy phép kinh doanh.",
        "context": "기업 설립 절차, 인허가 신청, 사업 등록 논의 시 사용",
        "culturalNote": "베트남의 사업허가증 발급 절차는 한국의 사업자등록보다 복잡하고 시간이 오래 걸림. 한국은 온라인으로 당일 발급이 가능한 경우가 많지만, 베트남은 서류 제출 후 심사 기간이 필요하고, 업종에 따라 추가 허가가 요구될 수 있음. 통역사는 한국 기업들이 베트남 진출 시 인허가 기간을 충분히 확보하도록 안내하고, 사업허가증 없이 영업하면 불법으로 간주되어 벌금이나 사업 중단 명령을 받을 수 있음을 강조해야 함.",
        "commonMistakes": [
            {
                "mistake": "한국의 사업자등록증과 완전히 동일하다고 설명",
                "correction": "유사하나 발급 절차, 기관, 법적 효력이 다름",
                "explanation": "베트남에서는 투자등록증이 선행되어야 하며, 업종별 추가 허가가 필요할 수 있음"
            },
            {
                "mistake": "사업허가증 없이 영업해도 괜찮다고 오해",
                "correction": "무허가 영업은 불법이며 강제 폐업과 벌금 대상",
                "explanation": "베트남 당국은 사업허가 여부를 엄격히 단속하므로 반드시 발급받아야 함"
            },
            {
                "mistake": "업종 변경이나 사업장 이전 시 변경 신고가 불필요하다고 생각",
                "correction": "사업허가증 내용 변경 시 반드시 변경 허가를 받아야 함",
                "explanation": "미신고 시 법적 문제가 발생하고 영업 정지 처분을 받을 수 있음"
            }
        ],
        "examples": [
            {
                "ko": "사업허가증을 받으려면 투자등록증이 먼저 필요합니다.",
                "vi": "Để được cấp giấy phép kinh doanh, trước tiên cần có giấy chứng nhận đầu tư.",
                "situation": "formal"
            },
            {
                "ko": "사업허가증 발급까지 보통 2주 정도 걸려요.",
                "vi": "Thủ tục cấp giấy phép kinh doanh thường mất khoảng 2 tuần.",
                "situation": "onsite"
            },
            {
                "ko": "업종을 추가하려면 사업허가증 변경 절차를 밟아야 합니다.",
                "vi": "Để bổ sung ngành nghề cần làm thủ tục điều chỉnh giấy phép kinh doanh.",
                "situation": "formal"
            }
        ],
        "relatedTerms": ["giay-chung-nhan-dau-tu", "dang-ky-kinh-doanh", "du-an-dau-tu"]
    },
    {
        "slug": "dang-ky-kinh-doanh",
        "korean": "사업자등록",
        "vietnamese": "đăng ký kinh doanh",
        "hanja": "事業者登錄",
        "hanjaReading": "事(일 사) + 業(업 업) + 者(놈 자) + 登(오를 등) + 錄(기록할 록)",
        "pronunciation": "당끼낀도안",
        "meaningKo": "기업이나 개인이 사업을 시작하기 위해 정부에 사업자 정보를 등록하는 절차. 베트남에서는 기획투자부 또는 각 성·시 인민위원회 산하 기업등록국에 신청하며, 등록 후 사업자등록증(giấy chứng nhận đăng ký kinh doanh)을 발급받음. 통역 시 주의할 점은 외국인 투자자의 경우 '투자등록'과 '사업자등록'이 별도의 절차이며, 투자등록증을 먼저 받은 후 사업자등록을 해야 한다는 점을 명확히 구분해야 함.",
        "meaningVi": "Thủ tục đăng ký thông tin doanh nghiệp hoặc cá nhân với cơ quan nhà nước có thẩm quyền để được phép kinh doanh hợp pháp. Sau khi đăng ký, doanh nghiệp được cấp giấy chứng nhận đăng ký kinh doanh. Đối với doanh nghiệp có vốn nước ngoài, đăng ký kinh doanh được thực hiện sau khi có giấy chứng nhận đầu tư.",
        "context": "기업 설립, 법인 등록, 창업 절차 논의 시 사용",
        "culturalNote": "베트남의 사업자등록 절차는 최근 몇 년간 간소화되었으나 여전히 한국보다 시간이 오래 걸림. 한국은 온라인 신청 후 즉시 발급이 가능한 경우가 많지만, 베트남은 서류 검토와 심사 절차가 필요함. 특히 외국인 투자자는 투자등록증 발급 후 사업자등록을 해야 하므로, 전체 프로세스를 이해하고 충분한 시간을 확보하는 것이 중요함. 통역사는 한국 기업들이 베트남 진출 시 인허가 일정을 과소평가하지 않도록 주의시켜야 함.",
        "commonMistakes": [
            {
                "mistake": "한국처럼 당일 발급이 가능하다고 설명",
                "correction": "베트남에서는 심사 기간이 필요하며 통상 1~2주 소요",
                "explanation": "한국과 달리 즉시 발급이 어려우므로 사업 일정을 여유 있게 잡아야 함"
            },
            {
                "mistake": "'사업자등록'과 '투자등록'을 같은 절차로 혼동",
                "correction": "외국인 투자자는 투자등록 후 사업자등록을 별도로 진행",
                "explanation": "두 절차를 혼동하면 인허가 일정이 지연되고 사업 개시가 늦어짐"
            },
            {
                "mistake": "사업자등록증만 있으면 모든 사업 활동이 가능하다고 오해",
                "correction": "업종에 따라 추가 허가나 면허가 필요할 수 있음",
                "explanation": "식품, 의료, 교육 등 특정 업종은 별도 허가가 요구됨"
            }
        ],
        "examples": [
            {
                "ko": "사업자등록을 마쳐야 정식으로 영업을 시작할 수 있습니다.",
                "vi": "Phải hoàn thành đăng ký kinh doanh mới được chính thức hoạt động.",
                "situation": "formal"
            },
            {
                "ko": "사업자등록 신청서에 대표자 서명이 필요해요.",
                "vi": "Hồ sơ đăng ký kinh doanh cần chữ ký của người đại diện pháp luật.",
                "situation": "onsite"
            },
            {
                "ko": "외국인투자기업은 투자등록증을 받은 후 사업자등록을 진행합니다.",
                "vi": "Doanh nghiệp có vốn nước ngoài làm đăng ký kinh doanh sau khi có giấy chứng nhận đầu tư.",
                "situation": "formal"
            }
        ],
        "relatedTerms": ["giay-chung-nhan-dau-tu", "giay-phep-kinh-doanh", "du-an-dau-tu"]
    },
    {
        "slug": "du-an-dau-tu",
        "korean": "투자프로젝트",
        "vietnamese": "dự án đầu tư",
        "hanja": "投資project",
        "hanjaReading": "投(던질 투) + 資(밑천 자) + project(외래어)",
        "pronunciation": "쥬언다우뜨",
        "meaningKo": "외국인 투자자가 베트남에서 사업을 추진하기 위해 계획한 구체적인 투자 계획. 투자 목적, 규모, 자본금, 사업 기간, 예상 수익 등이 포함되며, 투자등록증 발급의 기초 자료가 됨. 통역 시 주의할 점은 '프로젝트'라는 용어가 일회성 사업만을 의미하는 것이 아니라, 공장 설립, 합작투자, 지사 설치 등 다양한 형태의 투자 활동을 포괄한다는 점을 설명해야 함. 한국에서는 '투자 사업' 또는 '투자 계획'으로 번역되기도 함.",
        "meaningVi": "Kế hoạch cụ thể của nhà đầu tư để triển khai hoạt động kinh tế tại Việt Nam. Dự án đầu tư bao gồm thông tin về mục đích, quy mô, vốn, thời gian thực hiện, dự kiến lợi nhuận. Dự án là cơ sở để cấp giấy chứng nhận đầu tư và giám sát hoạt động đầu tư.",
        "context": "투자 협상, 사업 계획 수립, 인허가 신청 단계에서 사용",
        "culturalNote": "베트남에서는 투자프로젝트의 규모와 업종에 따라 승인 권한이 다름. 중앙 정부(계획투자부)가 승인하는 대형 프로젝트와 지방 정부(성·시 인민위원회)가 승인하는 중소형 프로젝트로 나뉘며, 승인 절차와 기간이 상이함. 한국 기업들은 투자프로젝트 제출 시 사업 타당성, 환경 영향, 고용 창출 효과 등을 구체적으로 제시해야 승인 가능성이 높아짐. 통역사는 프로젝트 규모에 따른 승인 절차의 차이를 이해하고, 필요한 서류와 일정을 안내해야 함.",
        "commonMistakes": [
            {
                "mistake": "'프로젝트'를 일회성 사업으로만 이해",
                "correction": "공장 설립, 합작투자 등 지속적인 사업도 포함",
                "explanation": "베트남 투자법상 '프로젝트'는 다양한 형태의 투자 활동을 포괄하는 개념"
            },
            {
                "mistake": "모든 투자프로젝트가 같은 절차로 승인된다고 설명",
                "correction": "규모와 업종에 따라 승인 기관과 절차가 다름",
                "explanation": "대형 프로젝트는 중앙 정부, 중소형은 지방 정부가 승인하므로 구분 필요"
            },
            {
                "mistake": "투자프로젝트 승인이 자동으로 사업 허가를 의미한다고 오해",
                "correction": "프로젝트 승인 후에도 사업자등록, 건설 허가 등 추가 절차 필요",
                "explanation": "프로젝트 승인은 첫 단계일 뿐, 실제 사업 개시까지 여러 허가가 요구됨"
            }
        ],
        "examples": [
            {
                "ko": "이 투자프로젝트는 총 1천만 달러 규모로 계획되었습니다.",
                "vi": "Dự án đầu tư này có quy mô tổng cộng 10 triệu đô la.",
                "situation": "formal"
            },
            {
                "ko": "투자프로젝트 승인을 받으려면 환경영향평가를 먼저 해야 해요.",
                "vi": "Để được phê duyệt dự án đầu tư cần làm đánh giá tác động môi trường trước.",
                "situation": "onsite"
            },
            {
                "ko": "이 프로젝트는 지방 정부 권한이라서 승인 절차가 빠릅니다.",
                "vi": "Dự án này thuộc thẩm quyền địa phương nên thủ tục phê duyệt nhanh.",
                "situation": "formal"
            }
        ],
        "relatedTerms": ["giay-chung-nhan-dau-tu", "von-dau-tu", "nha-dau-tu-nuoc-ngoai"]
    },
    {
        "slug": "uu-dai-dau-tu",
        "korean": "투자인센티브",
        "vietnamese": "ưu đãi đầu tư",
        "hanja": "投資incentive",
        "hanjaReading": "投(던질 투) + 資(밑천 자) + incentive(외래어)",
        "pronunciation": "으우다이다우뜨",
        "meaningKo": "정부가 외국인 투자를 유치하기 위해 제공하는 각종 혜택. 세금 감면(법인세 면제·감면, 수입 관세 면제), 토지 임대료 우대, 행정 절차 간소화, 고용 보조금 등이 포함됨. 통역 시 주의할 점은 인센티브는 업종(첨단기술, 환경, 교육, 의료 등 장려 업종), 지역(경제적으로 낙후된 지역, 산업단지 등), 투자 규모에 따라 차등 적용되므로, 구체적인 조건을 명확히 확인하고 전달해야 함.",
        "meaningVi": "Các chính sách ưu đãi mà nhà nước cung cấp để khuyến khích đầu tư. Bao gồm miễn giảm thuế thu nhập doanh nghiệp, thuế nhập khẩu, ưu đãi về thuê đất, hỗ trợ hành chính, trợ cấp tuyển dụng. Ưu đãi được áp dụng khác nhau tùy theo ngành nghề, địa phương, quy mô đầu tư.",
        "context": "투자 협상, 인센티브 신청, 세무 계획 수립 시 사용",
        "culturalNote": "베트남의 투자인센티브는 중국, 태국 등 주변국과의 투자 유치 경쟁 속에서 점점 확대되고 있으며, 특히 하이테크, 환경, 교육 분야에 대한 혜택이 큼. 한국 기업들은 첨단 제조업에서 최대 4년간 법인세 면제, 이후 9년간 50% 감면 등의 혜택을 받을 수 있으나, 조건 충족 여부를 사전에 철저히 검토해야 함. 통역사는 인센티브 신청 절차와 사후 관리(투자 이행 의무, 고용 창출 목표 등)를 명확히 설명하여, 투자자가 혜택을 제대로 활용하면서도 의무를 이행할 수 있도록 도와야 함.",
        "commonMistakes": [
            {
                "mistake": "모든 투자자가 동일한 인센티브를 받는다고 설명",
                "correction": "업종, 지역, 규모에 따라 인센티브가 다름",
                "explanation": "장려 업종과 낙후 지역에 투자할 때 혜택이 크므로 구체적 확인 필요"
            },
            {
                "mistake": "인센티브 신청 없이 자동으로 혜택을 받는다고 오해",
                "correction": "인센티브는 신청 절차를 거쳐야 하며, 조건 충족 증명이 필요",
                "explanation": "미신청 시 혜택을 받지 못하므로 투자등록 단계에서 반드시 신청해야 함"
            },
            {
                "mistake": "인센티브 혜택이 영구적이라고 설명",
                "correction": "대부분의 인센티브는 기간 제한이 있으며, 의무 이행 여부를 점검받음",
                "explanation": "의무 미이행 시 인센티브가 회수되고 추가 세금을 납부해야 할 수 있음"
            }
        ],
        "examples": [
            {
                "ko": "이 지역에 투자하면 법인세를 4년간 면제받을 수 있습니다.",
                "vi": "Nếu đầu tư vào khu vực này, được miễn thuế thu nhập doanh nghiệp trong 4 năm.",
                "situation": "formal"
            },
            {
                "ko": "첨단기술 업종이라서 투자인센티브를 최대로 받을 수 있어요.",
                "vi": "Vì là ngành công nghệ cao nên được hưởng ưu đãi đầu tư tối đa.",
                "situation": "onsite"
            },
            {
                "ko": "투자인센티브를 받으려면 고용 창출 목표를 달성해야 합니다.",
                "vi": "Để được hưởng ưu đãi đầu tư cần đạt mục tiêu tạo việc làm.",
                "situation": "formal"
            }
        ],
        "relatedTerms": ["khu-cong-nghiep", "khu-kinh-te-dac-biet", "giay-chung-nhan-dau-tu"]
    }
]

# Filter out duplicates
new_terms_filtered = [t for t in new_terms if t['slug'] not in existing_slugs]

# Extend data with new terms
data.extend(new_terms_filtered)

# Save back to file
with open(file_path, 'w', encoding='utf-8') as f:
    json.dump(data, f, ensure_ascii=False, indent=2)

print(f"✅ Successfully added {len(new_terms_filtered)} new terms to legal.json")
print(f"📊 Total terms in legal.json: {len(data)}")
print("\n🎯 Added terms:")
for term in new_terms_filtered:
    print(f"  - {term['slug']} ({term['korean']} / {term['vietnamese']})")
