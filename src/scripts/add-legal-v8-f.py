#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
법률 도메인 용어 추가 스크립트 v8-f: 해사법/선박법
테마: 선박등록, 선원법, 해양사고, 해난구조, 선하증권, 용선계약, 해상보험, 선박금융, 해양환경보호, 항만법
"""

import json
import os

# 추가할 10개 용어 (해사법/선박법)
new_terms = [
    {
        "slug": "dang-ky-tau-bien",
        "korean": "선박등록",
        "vietnamese": "Đăng ký tàu biển",
        "hanja": "船舶登錄",
        "hanjaReading": "船(배 선) + 舶(배 박) + 登(오를 등) + 錄(기록할 록)",
        "pronunciation": "썬밥뜽록",
        "meaningKo": "선박을 국가에 등록하여 소유권과 국적을 법적으로 인정받는 절차입니다. 통역 시 베트남의 'đăng ký quyền sở hữu tàu'(선박 소유권 등록)와 한국의 선박등록법 체계를 구분해야 합니다. 선박국적증서, 선박소유권등록, 저당권설정 등을 포함하며, 국제항해 선박은 반드시 등록해야 합니다. 베트남은 교통부 산하 해사국에서 관리하고, 한국은 해양수산부와 지방해양수산청에서 담당합니다.",
        "meaningVi": "Thủ tục đăng ký tàu biển với cơ quan nhà nước để được công nhận quyền sở hữu và quốc tịch hợp pháp. Bao gồm cấp Giấy chứng nhận quốc tịch tàu biển, đăng ký quyền sở hữu, quyền thế chấp. Tàu biển hoạt động quốc tế bắt buộc phải đăng ký.",
        "context": "선박 취득 시, 국제항해 준비, 선박 담보 대출",
        "culturalNote": "한국은 선박등록이 의무이며 위반 시 벌금과 운항 금지가 가능합니다. 베트남도 유사하지만 소형 어선은 등록 절차가 간소화되어 있습니다. 한국은 편의치적(flag of convenience) 방지를 위해 실질적 소유자를 엄격히 심사하며, 베트남은 외국인 소유 선박에 대한 제한이 더 엄격합니다. 통역 시 양국의 선박법 차이를 명확히 설명해야 합니다.",
        "commonMistakes": [
            {
                "mistake": "đăng ký tàu = 차량 등록처럼 번역",
                "correction": "선박등록 (법적 국적과 소유권 인정)",
                "explanation": "단순 행정등록이 아닌 국제법상 선박 국적 부여 절차"
            },
            {
                "mistake": "giấy phép tàu biển = 선박등록증",
                "correction": "선박면허 vs 선박국적증서 구분",
                "explanation": "면허는 운항허가, 국적증서는 등록 증명"
            },
            {
                "mistake": "베트남 'đăng ký sở hữu'만 설명",
                "correction": "등록 + 국적 취득 + 저당권 포함 설명",
                "explanation": "선박등록은 소유권뿐만 아니라 국적과 담보권도 포함"
            }
        ],
        "examples": [
            {
                "ko": "이 선박은 파나마에 등록되어 있습니다.",
                "vi": "Tàu này được đăng ký tại Panama.",
                "situation": "formal"
            },
            {
                "ko": "선박등록 시 저당권 설정이 필요합니다.",
                "vi": "Khi đăng ký tàu biển cần thiết lập quyền thế chấp.",
                "situation": "formal"
            },
            {
                "ko": "등록증 없으면 출항할 수 없어요.",
                "vi": "Không có giấy chứng nhận đăng ký thì không thể xuất cảng.",
                "situation": "onsite"
            }
        ],
        "relatedTerms": ["선박국적증서", "저당권", "편의치적", "선박소유권"]
    },
    {
        "slug": "luat-thuy-thu",
        "korean": "선원법",
        "vietnamese": "Luật thủy thủ",
        "hanja": "船員法",
        "hanjaReading": "船(배 선) + 員(인원 원) + 法(법 법)",
        "pronunciation": "써눤뻡",
        "meaningKo": "선박에서 근무하는 선원의 근로조건, 안전, 복지를 규정하는 법률입니다. 통역 시 베트남의 '선원 노동법'과 한국의 선원법이 적용 범위가 다름을 주의해야 합니다. 근로시간, 휴식, 임금, 사회보험, 승선 및 하선 절차, 해상 안전 교육을 포함합니다. 국제해사기구(IMO)의 국제협약도 반영되며, 선원의 권리 보호가 핵심입니다.",
        "meaningVi": "Luật quy định điều kiện lao động, an toàn và phúc lợi của thuyền viên làm việc trên tàu biển. Bao gồm giờ làm việc, nghỉ ngơi, lương, bảo hiểm xã hội, thủ tục lên xuống tàu, đào tạo an toàn hàng hải. Tuân thủ các công ước quốc tế của IMO.",
        "context": "선원 채용, 선박 운항 관리, 노동 분쟁",
        "culturalNote": "한국 선원법은 육상 근로기준법보다 근로시간이 길고(1일 최대 14시간), 연속 휴식 보장이 강조됩니다. 베트남도 유사하지만 영세 어선의 경우 법 적용이 느슨합니다. 한국은 선원 복지를 위해 선원공제회가 발달했으며, 베트남은 국영 해운사가 복지를 주로 담당합니다. 통역 시 '선원'과 '어부'를 구분해야 합니다.",
        "commonMistakes": [
            {
                "mistake": "thuyền viên = 모든 해상 근로자",
                "correction": "선원 (상선/어선 구분)",
                "explanation": "법적으로 상선 선원과 어선 선원은 적용 법령이 다름"
            },
            {
                "mistake": "luật lao động biển = 선원법으로만 번역",
                "correction": "선원법 + 어선원법 구분",
                "explanation": "한국은 상선과 어선의 법이 분리되어 있음"
            },
            {
                "mistake": "근로기준법과 동일하게 설명",
                "correction": "선원법은 특별법 (장시간 근로 허용)",
                "explanation": "육상 근로자와 선원은 법적 기준이 다름"
            }
        ],
        "examples": [
            {
                "ko": "선원법에 따라 휴식 시간을 보장해야 합니다.",
                "vi": "Theo Luật thủy thủ phải đảm bảo thời gian nghỉ ngơi.",
                "situation": "formal"
            },
            {
                "ko": "이 선원은 계약 위반으로 하선 조치됩니다.",
                "vi": "Thuyền viên này bị cho xuống tàu do vi phạm hợp đồng.",
                "situation": "formal"
            },
            {
                "ko": "선원 보험 가입은 의무예요.",
                "vi": "Bảo hiểm thuyền viên là bắt buộc.",
                "situation": "onsite"
            }
        ],
        "relatedTerms": ["선원근로계약", "승선", "하선", "선원공제회"]
    },
    {
        "slug": "tai-nan-hang-hai",
        "korean": "해양사고",
        "vietnamese": "Tai nạn hàng hải",
        "hanja": "海洋事故",
        "hanjaReading": "海(바다 해) + 洋(큰 바다 양) + 事(일 사) + 故(연고 고)",
        "pronunciation": "해양싸꼬",
        "meaningKo": "선박의 충돌, 좌초, 침몰, 화재 등 해상에서 발생한 안전 사고를 의미합니다. 통역 시 베트남의 '해상 재난'과 한국의 '해양사고'가 포함 범위가 다를 수 있음을 유의해야 합니다. 인명 피해, 재산 손실, 환경오염을 초래할 수 있으며, 사고 원인 조사와 책임 규명이 중요합니다. 해양안전심판원이 사고를 조사하며, 국제해사기구(IMO) 규정도 적용됩니다.",
        "meaningVi": "Sự cố an toàn xảy ra trên biển như va chạm tàu, mắc cạn, chìm tàu, hỏa hoạn. Có thể gây thiệt hại về người, tài sản, ô nhiễm môi trường. Cơ quan điều tra tai nạn hàng hải sẽ xác định nguyên nhân và trách nhiệm theo quy định IMO.",
        "context": "선박 운항, 보험 청구, 사고 조사",
        "culturalNote": "한국은 세월호 사고 이후 해양사고 조사와 책임 규명이 강화되었으며, 안전관리체계(ISM Code)가 엄격히 적용됩니다. 베트남도 해양사고 신고 의무가 있지만, 소형 어선 사고는 보고되지 않는 경우가 많습니다. 한국은 해양안전심판원이 독립적으로 조사하고, 베트남은 교통부 산하 해사국이 담당합니다. 통역 시 '사고'와 '사건'을 구분해야 합니다.",
        "commonMistakes": [
            {
                "mistake": "tai nạn = 모든 사고",
                "correction": "해양사고 (선박 관련 한정)",
                "explanation": "일반 교통사고와 구분되는 해상 특화 사고"
            },
            {
                "mistake": "thảm họa biển = 해양사고",
                "correction": "해양재난 vs 해양사고 구분",
                "explanation": "재난은 대규모, 사고는 개별 선박 중심"
            },
            {
                "mistake": "사고 원인을 즉시 단정",
                "correction": "조사 중 또는 추정 원인으로 표현",
                "explanation": "공식 조사 결과 전까지는 확정 표현 금지"
            }
        ],
        "examples": [
            {
                "ko": "선박 충돌 사고로 유류가 유출되었습니다.",
                "vi": "Do tai nạn va chạm tàu đã xảy ra tràn dầu.",
                "situation": "formal"
            },
            {
                "ko": "해양사고 조사 결과가 나올 때까지 기다려야 합니다.",
                "vi": "Phải chờ kết quả điều tra tai nạn hàng hải.",
                "situation": "formal"
            },
            {
                "ko": "좌초 사고로 선체가 파손됐어요.",
                "vi": "Mắc cạn làm hư hỏng thân tàu.",
                "situation": "onsite"
            }
        ],
        "relatedTerms": ["선박충돌", "좌초", "침몰", "해양안전심판원"]
    },
    {
        "slug": "cuu-nan-bien",
        "korean": "해난구조",
        "vietnamese": "Cứu nạn biển",
        "hanja": "海難救助",
        "hanjaReading": "海(바다 해) + 難(어려울 난) + 救(구할 구) + 助(도울 조)",
        "pronunciation": "해난꾸조",
        "meaningKo": "해상에서 조난당한 선박이나 인명을 구조하는 행위를 의미합니다. 통역 시 베트남의 '구조 활동'과 한국의 '해난구조'가 법적 의미와 보상 체계에서 차이가 있음을 주의해야 합니다. 구조료 청구권, 공동해손, 국제해상구조협약(Salvage Convention) 적용 등이 포함됩니다. 해양경찰, 해군, 민간 구조업체가 참여하며, 구조 성공 시 보상금을 받을 수 있습니다.",
        "meaningVi": "Hành vi cứu giúp tàu biển hoặc con người gặp nạn trên biển. Bao gồm quyền yêu cầu tiền cứu hộ, tổn thất chung, áp dụng Công ước cứu hộ hàng hải quốc tế. Cảnh sát biển, hải quân, công ty cứu hộ tư nhân tham gia và có thể nhận tiền thưởng nếu thành công.",
        "context": "선박 조난, 보험 청구, 구조 계약",
        "culturalNote": "한국은 해난구조법에 따라 구조료가 명확히 규정되며, 성공보수(no cure no pay) 원칙이 적용됩니다. 베트남도 유사하지만 구조료 산정 기준이 덜 명확합니다. 한국은 해양경찰이 공공 구조를 담당하고, 민간 구조업체는 상업적 구조를 수행합니다. 베트남은 국영 구조업체가 주도합니다. 통역 시 '구조'와 '구난'을 구분해야 합니다.",
        "commonMistakes": [
            {
                "mistake": "cứu hộ = 해난구조로만 번역",
                "correction": "해난구조 (법적 권리 포함)",
                "explanation": "단순 구조가 아닌 구조료 청구권이 있는 법적 행위"
            },
            {
                "mistake": "무료 구조로 설명",
                "correction": "성공보수 원칙 (구조료 청구 가능)",
                "explanation": "민간 구조는 성공 시 보상금이 발생"
            },
            {
                "mistake": "cứu nạn = 모든 구조 활동",
                "correction": "해난구조 vs 해상 수색 구분",
                "explanation": "구조는 선박/화물, 수색은 실종자 찾기"
            }
        ],
        "examples": [
            {
                "ko": "해난구조법에 따라 구조료를 청구합니다.",
                "vi": "Theo Luật cứu nạn biển yêu cầu tiền cứu hộ.",
                "situation": "formal"
            },
            {
                "ko": "민간 구조업체가 구조에 성공했습니다.",
                "vi": "Công ty cứu hộ tư nhân đã cứu thành công.",
                "situation": "formal"
            },
            {
                "ko": "구조료는 선박 가치의 20%예요.",
                "vi": "Tiền cứu hộ là 20% giá trị tàu.",
                "situation": "onsite"
            }
        ],
        "relatedTerms": ["구조료", "공동해손", "성공보수", "해양구조협약"]
    },
    {
        "slug": "van-don-hang-hai",
        "korean": "선하증권",
        "vietnamese": "Vận đơn hàng hải",
        "hanja": "船荷證券",
        "hanjaReading": "船(배 선) + 荷(짐 하) + 證(증거 증) + 券(문서 권)",
        "pronunciation": "썬하쯩꿘",
        "meaningKo": "선박으로 운송되는 화물의 수령과 인도를 증명하는 유가증권입니다. 통역 시 베트남의 'vận đơn'과 한국의 선하증권이 법적 효력과 양도성에서 차이가 있음을 명확히 해야 합니다. 화물의 권리증서로서 매매, 담보, 양도가 가능하며, 신용장 거래에서 필수 서류입니다. B/L(Bill of Lading)로 약칭하며, Original B/L 없이는 화물 인수가 불가능합니다.",
        "meaningVi": "Chứng từ có giá chứng minh việc nhận và giao hàng hóa vận chuyển bằng tàu biển. Là chứng thư quyền sở hữu hàng hóa, có thể mua bán, thế chấp, chuyển nhượng. Là chứng từ bắt buộc trong giao dịch thư tín dụng. Không có B/L gốc thì không thể nhận hàng.",
        "context": "해상 운송, 무역 거래, 은행 결제",
        "culturalNote": "한국은 선하증권이 엄격한 요식증권으로 취급되며, 위조 시 형사 처벌을 받습니다. 베트남도 유사하지만 '해상화물운송장(Sea Waybill)'과 혼용되는 경우가 있습니다. 한국은 전자선하증권(e-B/L) 도입이 진행 중이며, 베트남은 아직 종이 문서가 주류입니다. 통역 시 Original B/L과 Copy의 차이를 명확히 설명해야 합니다.",
        "commonMistakes": [
            {
                "mistake": "vận đơn = 모든 운송 서류",
                "correction": "선하증권 (유가증권, 양도 가능)",
                "explanation": "일반 운송장과 달리 권리증서로서 법적 효력이 다름"
            },
            {
                "mistake": "B/L copy = 원본과 동일",
                "correction": "Original B/L만 화물 인수 가능",
                "explanation": "사본은 참고용일 뿐 법적 효력 없음"
            },
            {
                "mistake": "항공화물운송장과 동일하게 설명",
                "correction": "선하증권은 유가증권, 항공은 아님",
                "explanation": "양도성과 담보 가치가 다름"
            }
        ],
        "examples": [
            {
                "ko": "선하증권 원본 3통을 발행해 주세요.",
                "vi": "Vui lòng phát hành 3 bản gốc vận đơn hàng hải.",
                "situation": "formal"
            },
            {
                "ko": "신용장에 선하증권이 첨부되어야 합니다.",
                "vi": "Vận đơn hàng hải phải đính kèm thư tín dụng.",
                "situation": "formal"
            },
            {
                "ko": "B/L 없으면 화물 못 찾아요.",
                "vi": "Không có B/L thì không lấy được hàng.",
                "situation": "onsite"
            }
        ],
        "relatedTerms": ["유가증권", "신용장", "화물인도지시서", "전자선하증권"]
    },
    {
        "slug": "hop-dong-thue-tau",
        "korean": "용선계약",
        "vietnamese": "Hợp đồng thuê tàu",
        "hanja": "傭船契約",
        "hanjaReading": "傭(품팔이 용) + 船(배 선) + 契(맺을 계) + 約(약속 약)",
        "pronunciation": "용썬꼐약",
        "meaningKo": "선박의 전부 또는 일부를 임대하는 계약을 의미합니다. 통역 시 베트남의 '선박 임대'와 한국의 '용선계약'이 책임과 비용 분담에서 차이가 있음을 주의해야 합니다. 항해용선(Voyage Charter), 기간용선(Time Charter), 나용선(Bareboat Charter)으로 구분되며, 각각 선주와 용선자의 의무가 다릅니다. 용선료, 체선료, 조출료 등의 비용 조항이 중요합니다.",
        "meaningVi": "Hợp đồng thuê toàn bộ hoặc một phần tàu biển. Phân loại thành thuê chuyến (Voyage Charter), thuê kỳ hạn (Time Charter), thuê tàu không thủy thủ (Bareboat Charter). Trách nhiệm và chi phí khác nhau giữa chủ tàu và người thuê. Chi phí thuê tàu, phí chậm tải, phí trả sớm là các điều khoản quan trọng.",
        "context": "해운 사업, 화물 운송, 선박 임대",
        "culturalNote": "한국은 용선계약서가 영문 표준 양식(GENCON, NYPE 등)을 많이 사용하며, 국제 중재 조항이 포함됩니다. 베트남도 유사하지만 국내 운송은 베트남어 계약서를 선호합니다. 한국은 용선료 지급 지연 시 선박 유치권이 인정되며, 베트남도 유사합니다. 통역 시 '용선'과 '임차'를 구분하고, 책임 범위를 명확히 설명해야 합니다.",
        "commonMistakes": [
            {
                "mistake": "thuê tàu = 모든 선박 임대",
                "correction": "항해용선/기간용선/나용선 구분",
                "explanation": "유형별로 책임과 비용 부담이 완전히 다름"
            },
            {
                "mistake": "용선료 = 고정 금액",
                "correction": "용선 유형에 따라 계산 방식 다름",
                "explanation": "항해용선은 항차당, 기간용선은 일/월 단위"
            },
            {
                "mistake": "chủ tàu = 항상 운항 책임",
                "correction": "나용선은 용선자가 운항 책임",
                "explanation": "용선 유형에 따라 책임 주체가 다름"
            }
        ],
        "examples": [
            {
                "ko": "기간용선 계약으로 6개월간 선박을 임대합니다.",
                "vi": "Thuê tàu theo hợp đồng kỳ hạn trong 6 tháng.",
                "situation": "formal"
            },
            {
                "ko": "용선료는 하루 $10,000입니다.",
                "vi": "Phí thuê tàu là $10,000 mỗi ngày.",
                "situation": "formal"
            },
            {
                "ko": "나용선이라 선원은 우리가 고용해요.",
                "vi": "Vì thuê tàu không thủy thủ nên chúng tôi tự thuê thuyền viên.",
                "situation": "onsite"
            }
        ],
        "relatedTerms": ["항해용선", "기간용선", "나용선", "체선료"]
    },
    {
        "slug": "bao-hiem-hang-hai",
        "korean": "해상보험",
        "vietnamese": "Bảo hiểm hàng hải",
        "hanja": "海上保險",
        "hanjaReading": "海(바다 해) + 上(위 상) + 保(지킬 보) + 險(험할 험)",
        "pronunciation": "해썽보힘",
        "meaningKo": "해상 운송 중 발생하는 위험을 보상하는 보험을 의미합니다. 통역 시 베트남의 '해상 보험'과 한국의 '해상보험'이 보상 범위와 약관에서 차이가 있음을 유의해야 합니다. 선박보험, 적하보험(화물보험), 운임보험으로 구분되며, ICC(Institute Cargo Clauses) A/B/C 조건이 국제적으로 사용됩니다. 공동해손, 단독해손, 분손, 전손 등의 손해 유형을 이해해야 합니다.",
        "meaningVi": "Bảo hiểm bù đắp rủi ro xảy ra trong vận chuyển hàng hải. Bao gồm bảo hiểm tàu biển, bảo hiểm hàng hóa, bảo hiểm cước phí. Sử dụng điều kiện ICC A/B/C theo chuẩn quốc tế. Cần hiểu các loại thiệt hại: tổn thất chung, tổn thất riêng, hư hỏng một phần, toàn bộ tổn thất.",
        "context": "무역 거래, 선박 운항, 보험 청구",
        "culturalNote": "한국은 해상보험법이 상법에 포함되어 있으며, 보험금 청구 시 손해사정사가 개입합니다. 베트남도 유사하지만 보상 한도와 면책 조항이 더 엄격합니다. 한국은 ICC(A) 조건(전위험 담보)이 일반적이고, 베트남은 ICC(C) 조건(기본 담보)이 많습니다. 통역 시 '전손'과 '분손', '공동해손'과 '단독해손'을 명확히 구분해야 합니다.",
        "commonMistakes": [
            {
                "mistake": "bảo hiểm biển = 선박만 보험",
                "correction": "해상보험 (선박 + 화물 + 운임)",
                "explanation": "선박보험뿐만 아니라 적하보험도 포함"
            },
            {
                "mistake": "ICC A/B/C를 설명 없이 사용",
                "correction": "A는 전위험, C는 기본 위험만 보상",
                "explanation": "약관 차이를 명확히 설명해야 오해 방지"
            },
            {
                "mistake": "toàn bộ tổn thất = 모든 손해",
                "correction": "전손 (선박/화물 완전 손실)",
                "explanation": "부분 손해(분손)와 구분 필요"
            }
        ],
        "examples": [
            {
                "ko": "ICC(A) 조건으로 적하보험에 가입했습니다.",
                "vi": "Đã mua bảo hiểm hàng hóa theo điều kiện ICC(A).",
                "situation": "formal"
            },
            {
                "ko": "공동해손이 선언되어 화주가 분담해야 합니다.",
                "vi": "Tổn thất chung được tuyên bố, chủ hàng phải đóng góp.",
                "situation": "formal"
            },
            {
                "ko": "화물 손상으로 보험금 청구할게요.",
                "vi": "Hàng bị hư hỏng nên sẽ yêu cầu bồi thường bảo hiểm.",
                "situation": "onsite"
            }
        ],
        "relatedTerms": ["적하보험", "공동해손", "전손", "ICC조건"]
    },
    {
        "slug": "tai-chinh-tau-bien",
        "korean": "선박금융",
        "vietnamese": "Tài chính tàu biển",
        "hanja": "船舶金融",
        "hanjaReading": "船(배 선) + 舶(배 박) + 金(쇠 금) + 融(녹을 융)",
        "pronunciation": "썬밥끔늉",
        "meaningKo": "선박 건조나 구매를 위한 자금 조달을 의미합니다. 통역 시 베트남의 '선박 대출'과 한국의 '선박금융'이 담보와 상환 방식에서 차이가 있음을 주의해야 합니다. 선박저당, 리스, 선박펀드 등 다양한 금융 방식이 있으며, 국제 금융기관(IMO, 수출입은행)이 참여합니다. 선박은 고가이므로 장기 대출이 일반적이며, 선박 자체가 담보가 됩니다.",
        "meaningVi": "Huy động vốn để đóng mới hoặc mua tàu biển. Bao gồm thế chấp tàu biển, thuê tài chính, quỹ đầu tư tàu biển. Các tổ chức tài chính quốc tế (IMO, ngân hàng xuất nhập khẩu) tham gia. Do tàu biển có giá trị cao nên thường vay dài hạn, dùng chính tàu làm tài sản thế chấp.",
        "context": "조선소 계약, 선박 구매, 해운 투자",
        "culturalNote": "한국은 수출입은행과 한국해양진흥공사가 선박금융을 지원하며, 건조 중인 선박도 담보 인정됩니다. 베트남은 국영 은행이 주로 담당하며, 완공 선박만 담보로 인정하는 경우가 많습니다. 한국은 선박펀드가 발달했고, 베트남은 국영 해운사가 직접 발주하는 경우가 많습니다. 통역 시 '저당'과 '질권'을 구분해야 합니다.",
        "commonMistakes": [
            {
                "mistake": "vay mua tàu = 일반 대출",
                "correction": "선박금융 (특수 금융, 장기 대출)",
                "explanation": "선박 특성상 담보 평가와 상환 기간이 특수함"
            },
            {
                "mistake": "thế chấp tàu = 부동산 담보와 동일",
                "correction": "선박저당 (동산이지만 등기 필요)",
                "explanation": "선박은 이동 재산이지만 등기제도 적용"
            },
            {
                "mistake": "건조 중인 선박은 담보 불가",
                "correction": "한국은 건조 중 선박도 담보 인정",
                "explanation": "국가별 금융 제도 차이 명확히 설명"
            }
        ],
        "examples": [
            {
                "ko": "수출입은행에서 선박금융을 승인받았습니다.",
                "vi": "Đã được ngân hàng xuất nhập khẩu phê duyệt tài chính tàu biển.",
                "situation": "formal"
            },
            {
                "ko": "선박 저당권이 설정되어 있습니다.",
                "vi": "Tàu biển đã được thế chấp.",
                "situation": "formal"
            },
            {
                "ko": "대출 상환 기간은 15년이에요.",
                "vi": "Thời hạn trả nợ là 15 năm.",
                "situation": "onsite"
            }
        ],
        "relatedTerms": ["선박저당", "선박펀드", "리스", "수출입은행"]
    },
    {
        "slug": "bao-ve-moi-truong-bien",
        "korean": "해양환경보호",
        "vietnamese": "Bảo vệ môi trường biển",
        "hanja": "海洋環境保護",
        "hanjaReading": "海(바다 해) + 洋(큰 바다 양) + 環(고리 환) + 境(지경 경) + 保(지킬 보) + 護(지킬 호)",
        "pronunciation": "해양환경보호",
        "meaningKo": "해양 오염을 방지하고 해양 생태계를 보호하는 활동을 의미합니다. 통역 시 베트남의 '해양 보호'와 한국의 '해양환경보호'가 규제 강도와 처벌 수준에서 차이가 있음을 유의해야 합니다. 유류 오염, 폐기물 투기, 밸러스트수 관리, 대기오염 규제를 포함합니다. MARPOL 협약, IMO 2020(저황유 규제) 등 국제 규정이 적용되며, 위반 시 선박 억류와 벌금이 부과됩니다.",
        "meaningVi": "Hoạt động ngăn chặn ô nhiễm biển và bảo vệ hệ sinh thái biển. Bao gồm ô nhiễm dầu, xả rác, quản lý nước dằn, kiểm soát khí thải. Áp dụng Công ước MARPOL, IMO 2020 (quy định nhiên liệu sulfur thấp). Vi phạm sẽ bị tạm giữ tàu và phạt tiền.",
        "context": "선박 운항, 환경 규제, 국제 협약",
        "culturalNote": "한국은 해양환경관리법이 엄격하며, 유류 유출 시 대규모 배상이 요구됩니다. 베트남도 환경 보호를 강조하지만 집행이 느슨한 경우가 있습니다. 한국은 IMO 2020을 엄격히 적용하여 저황유 사용을 의무화하고, 베트남도 주요 항구에서 단속이 강화되고 있습니다. 통역 시 '오염'과 '배출'을 구분하고, 법적 책임 범위를 명확히 설명해야 합니다.",
        "commonMistakes": [
            {
                "mistake": "bảo vệ môi trường = 일반 환경 보호",
                "correction": "해양환경보호 (선박 오염 중심)",
                "explanation": "육상 환경과 구분되는 해양 특화 규제"
            },
            {
                "mistake": "xả nước thải = 모든 폐수 배출",
                "correction": "밸러스트수 관리 vs 생활하수 구분",
                "explanation": "선박 폐수는 유형별로 규제가 다름"
            },
            {
                "mistake": "IMO 2020 = 2020년 시행된 규정 전부",
                "correction": "저황유 규제 (황 함량 0.5% 이하)",
                "explanation": "특정 연료 규제임을 명확히 설명"
            }
        ],
        "examples": [
            {
                "ko": "MARPOL 협약에 따라 폐유를 육상에서 처리해야 합니다.",
                "vi": "Theo Công ước MARPOL phải xử lý dầu thải trên bờ.",
                "situation": "formal"
            },
            {
                "ko": "저황유 사용으로 연료비가 증가했습니다.",
                "vi": "Chi phí nhiên liệu tăng do sử dụng nhiên liệu sulfur thấp.",
                "situation": "formal"
            },
            {
                "ko": "밸러스트수 처리 장치가 고장났어요.",
                "vi": "Thiết bị xử lý nước dằn bị hỏng.",
                "situation": "onsite"
            }
        ],
        "relatedTerms": ["MARPOL협약", "저황유", "밸러스트수", "유류오염배상"]
    },
    {
        "slug": "luat-cang-bien",
        "korean": "항만법",
        "vietnamese": "Luật cảng biển",
        "hanja": "港灣法",
        "hanjaReading": "港(항구 항) + 灣(물가 만) + 法(법 법)",
        "pronunciation": "항만뻡",
        "meaningKo": "항만의 건설, 관리, 운영에 관한 법률을 의미합니다. 통역 시 베트남의 '항구법'과 한국의 '항만법'이 공공성과 민간 참여 범위에서 차이가 있음을 주의해야 합니다. 항만 시설 사용료, 하역 작업, 선박 입출항 절차, 항만 안전 관리를 포함합니다. 국제 항만은 세관, 검역, 출입국 관리가 통합되며, 자유무역항 제도도 포함됩니다.",
        "meaningVi": "Luật về xây dựng, quản lý và vận hành cảng biển. Bao gồm phí sử dụng cảng, hoạt động bốc xếp, thủ tục tàu ra vào, quản lý an toàn cảng. Cảng quốc tế có hải quan, kiểm dịch, xuất nhập cảnh tích hợp. Cũng bao gồm chế độ cảng tự do.",
        "context": "항만 운영, 선박 입출항, 하역 작업",
        "culturalNote": "한국은 항만공사(PA: Port Authority) 체제로 부산항, 인천항 등이 독립 운영되며, 민간 터미널도 많습니다. 베트남은 국영 항만공사가 주도하고, 민간 참여는 제한적입니다. 한국은 자동화 항만이 발달했고, 베트남은 인력 중심 하역이 많습니다. 통역 시 '항만'과 '항구'를 구분하고, 시설 사용료 계산 방식을 명확히 설명해야 합니다.",
        "commonMistakes": [
            {
                "mistake": "cảng = 항만으로만 번역",
                "correction": "항만 (시설 전체) vs 항구 (정박지)",
                "explanation": "항만은 시설 포함, 항구는 물리적 장소"
            },
            {
                "mistake": "phí cảng = 단일 요금",
                "correction": "입항료, 접안료, 하역료 구분",
                "explanation": "항만 비용은 여러 항목으로 구성"
            },
            {
                "mistake": "모든 항만이 자유무역항",
                "correction": "자유무역항은 특별 지위 항만",
                "explanation": "관세 혜택이 있는 특수 항만만 해당"
            }
        ],
        "examples": [
            {
                "ko": "항만법에 따라 입항 신고를 해야 합니다.",
                "vi": "Theo Luật cảng biển phải khai báo tàu vào cảng.",
                "situation": "formal"
            },
            {
                "ko": "부산항은 자유무역항으로 지정되어 있습니다.",
                "vi": "Cảng Busan được chỉ định là cảng tự do.",
                "situation": "formal"
            },
            {
                "ko": "접안료가 예상보다 비싸요.",
                "vi": "Phí cập cảng đắt hơn dự kiến.",
                "situation": "onsite"
            }
        ],
        "relatedTerms": ["항만공사", "입항료", "접안료", "자유무역항"]
    }
]

def main():
    # legal.json 파일 경로
    file_path = os.path.join(
        os.path.dirname(os.path.dirname(__file__)),
        'data', 'terms', 'legal.json'
    )

    # 기존 파일 읽기
    with open(file_path, 'r', encoding='utf-8') as f:
        data = json.load(f)

    print(f"📂 기존 용어 수: {len(data)}개")

    # 중복 확인 (slug 기준)
    existing_slugs = {term['slug'] for term in data}
    new_slugs = {term['slug'] for term in new_terms}
    duplicates = existing_slugs & new_slugs

    if duplicates:
        print(f"⚠️  중복된 slug 발견: {duplicates}")
        print("중복 제거 후 진행합니다.")
        new_terms_filtered = [term for term in new_terms if term['slug'] not in existing_slugs]
    else:
        new_terms_filtered = new_terms

    # 새 용어 추가
    data.extend(new_terms_filtered)

    print(f"➕ 추가된 용어: {len(new_terms_filtered)}개")
    print(f"📊 총 용어 수: {len(data)}개")

    # 파일 저장 (들여쓰기 2칸, 유니코드 그대로, 줄바꿈 LF)
    with open(file_path, 'w', encoding='utf-8') as f:
        json.dump(data, f, ensure_ascii=False, indent=2)
        f.write('\n')  # 파일 끝 줄바꿈

    print(f"✅ 저장 완료: {file_path}")

    # 추가된 용어 목록 출력
    print("\n📋 추가된 용어:")
    for term in new_terms_filtered:
        print(f"  - {term['korean']} ({term['vietnamese']}) - {term['slug']}")

if __name__ == '__main__':
    main()
