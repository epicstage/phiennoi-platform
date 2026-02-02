#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
해상법/보험법 용어 추가 스크립트
Maritime Law/Insurance Law Terms Addition Script

Tier S 품질 기준:
- meaningKo: 200자 이상, 통역 팁 포함
- meaningVi: 100자 이상, 성조 포함
- culturalNote: 100자 이상
- commonMistakes: 3개 이상 (객체 형식)
- examples: 3개 이상 (situation 포함)
- relatedTerms: 3개 이상
"""

import json
import os


def main():
    # 1. 파일 경로 설정
    file_path = os.path.join(
        os.path.dirname(os.path.abspath(__file__)),
        '..',
        'data',
        'terms',
        'legal.json'
    )

    # 2. 기존 데이터 로드
    with open(file_path, 'r', encoding='utf-8') as f:
        data = json.load(f)  # data is a LIST

    # 3. 기존 slug 추출
    existing_slugs = {t['slug'] for t in data}

    # 4. 신규 용어 정의 (해상법/보험법 테마)
    new_terms = [
        {
            "slug": "bao-hiem-hang-hai",
            "korean": "해상보험",
            "vietnamese": "Bảo hiểm hàng hải",
            "hanja": "海上保險",
            "hanjaReading": "海(바다 해) + 上(위 상) + 保(지킬 보) + 險(험할 험)",
            "pronunciation": "바오 히엠 항 하이",
            "meaningKo": "해상운송 중 발생하는 선박, 화물, 운임 등의 손해를 보상하는 보험계약입니다. 통역 시 '해상보험'과 '화물보험'을 명확히 구분해야 하며, 베트남에서는 'bảo hiểm hàng hải'가 선박보험을 의미하고 'bảo hiểm hàng hóa'가 화물보험을 의미하므로 주의가 필요합니다. 해상보험은 영국 해상보험법(MIA 1906)의 영향을 받아 국제적으로 표준화되어 있으나, 베트남은 Civil Code 2015와 Commercial Law 2005를 따르므로 양국의 법체계 차이를 숙지해야 합니다. 특히 'All Risks', 'FPA', 'WA' 등 영문 약어를 베트남어로 통역할 때는 베트남 보험업계에서 통용되는 표현을 사용해야 오해를 방지할 수 있습니다.",
            "meaningVi": "Bảo hiểm hàng hải là hợp đồng bảo hiểm bồi thường thiệt hại về tàu thuyền, hàng hóa, cước phí phát sinh trong quá trình vận chuyển đường biển. Theo Luật Thương mại Việt Nam 2005 và Bộ luật Dân sự 2015, bảo hiểm hàng hải bao gồm bảo hiểm thân tàu, bảo hiểm hàng hóa và bảo hiểm trách nhiệm. Cần phân biệt với 'bảo hiểm hàng hóa' (chỉ bảo hiểm cho hàng hóa) và 'bảo hiểm vận tải' (phạm vi rộng hơn bao gồm cả đường bộ, đường sắt).",
            "context": "해상 무역, 물류, 보험, 국제 운송 계약 협상 시 사용",
            "culturalNote": "한국은 해운 강국으로 해상보험 시장이 발달되어 있으며, 국제 해상보험 표준(영국 MIA 기준)을 따릅니다. 베트남은 최근 해운 산업이 성장하면서 해상보험 수요가 증가하고 있으나, 여전히 국영 보험사(Bảo Việt, PVI) 중심이며, 베트남 상법과 민법에 기반한 독자적 보험 체계를 유지합니다. 한국 통역사는 베트남 기업이 국제 해상보험 용어(영문 약어)에 익숙하지 않을 수 있음을 고려해야 합니다.",
            "commonMistakes": [
                {
                    "mistake": "'해상보험'을 'bảo hiểm biển'로 직역",
                    "correction": "'bảo hiểm hàng hải'가 정확한 법률 용어",
                    "explanation": "'bảo hiểm biển'은 비표준 표현이며, 베트남 상법에서는 'bảo hiểm hàng hải'를 공식 용어로 사용합니다."
                },
                {
                    "mistake": "'화물보험'과 '해상보험'을 혼동하여 모두 'bảo hiểm hàng hải'로 번역",
                    "correction": "화물보험은 'bảo hiểm hàng hóa', 선박보험은 'bảo hiểm tàu thuyền'으로 구분",
                    "explanation": "'bảo hiểm hàng hải'는 포괄 개념이며, 세부 보험 유형을 명확히 구분해야 합니다."
                },
                {
                    "mistake": "영문 약어 'FPA', 'WA'를 그대로 사용",
                    "correction": "'bảo hiểm bộ phận' (FPA), 'bảo hiểm toàn bộ rủi ro' (All Risks)로 설명",
                    "explanation": "베트남 고객은 영문 약어에 익숙하지 않을 수 있으므로 베트남어로 풀어서 설명해야 합니다."
                }
            ],
            "examples": [
                {
                    "ko": "해상보험 계약 시 보험가액과 보험금액을 명확히 구분해야 합니다.",
                    "vi": "Khi ký hợp đồng bảo hiểm hàng hải cần phân biệt rõ giá trị bảo hiểm và số tiền bảo hiểm.",
                    "situation": "formal"
                },
                {
                    "ko": "이 선박은 선체보험과 책임보험 모두 가입되어 있습니다.",
                    "vi": "Tàu này đã tham gia cả bảo hiểm thân tàu và bảo hiểm trách nhiệm.",
                    "situation": "onsite"
                },
                {
                    "ko": "해상보험 청구 시 선하증권과 보험증권을 함께 제출해야 합니다.",
                    "vi": "Khi yêu cầu bồi thường bảo hiểm hàng hải cần nộp cả vận đơn và chứng nhận bảo hiểm.",
                    "situation": "formal"
                }
            ],
            "relatedTerms": ["van-don", "van-tai-bien", "bao-hiem-hang-hoa", "trach-nhiem-van-chuyen"]
        },
        {
            "slug": "van-don",
            "korean": "선하증권",
            "vietnamese": "Vận đơn",
            "hanja": "船荷證券",
            "hanjaReading": "船(배 선) + 荷(짐 하) + 證(증거 증) + 券(문서 권)",
            "pronunciation": "번 던",
            "meaningKo": "선박회사가 화물을 수령하고 운송을 약정한 사실을 증명하는 유가증권으로, 물권적 효력을 가진 해상운송 필수 서류입니다. 통역 시 'Bill of Lading(B/L)'의 약어와 베트남어 'vận đơn'을 혼용하므로 문맥을 정확히 파악해야 합니다. 베트남에서는 'vận đơn gốc'(원본 선하증권)와 'bản sao vận đơn'(사본)의 법적 효력 차이가 크므로, 통역 시 'gốc'(원본) 여부를 명확히 전달해야 합니다. 선하증권은 화물인도청구권, 화물소유권 증명, 운송계약 증거의 3대 기능을 하며, 'Surrendered B/L', 'Telex Release' 등 전자 방식도 증가하고 있으므로 최신 용어를 숙지해야 합니다.",
            "meaningVi": "Vận đơn (Bill of Lading - B/L) là chứng từ có giá do hãng tàu phát hành, xác nhận đã nhận hàng và cam kết vận chuyển. Theo Bộ luật Hàng hải Việt Nam 2015, vận đơn có ba chức năng: chứng nhận nhận hàng, chứng cứ hợp đồng vận chuyển, và chứng từ để nhận hàng. Vận đơn gốc (vận đơn chính thức) có giá trị pháp lý, trong khi bản sao chỉ mang tính tham khảo. Hiện nay có xu hướng sử dụng vận đơn điện tử (Telex Release, Sea Waybill) để tăng tốc độ giao nhận hàng.",
            "context": "해상 무역, 수출입 통관, 화물 인도, 신용장 거래 시 사용",
            "culturalNote": "한국은 컨테이너 해운 강국으로 선하증권 실무가 매우 정교하며, 전자 선하증권(e-B/L) 도입이 활발합니다. 베트남은 종이 선하증권이 여전히 주류이며, 원본 선하증권 없이 화물을 인도하는 관행이 있어 분쟁이 자주 발생합니다. 베트남 해사법(Bộ luật Hàng hải 2015)은 선하증권의 법적 효력을 명확히 규정하고 있으나, 실무에서는 'Telex Release'나 'Surrendered B/L' 방식이 혼용되므로 통역 시 정확한 용어 사용이 중요합니다.",
            "commonMistakes": [
                {
                    "mistake": "'선하증권'을 'giấy chứng nhận hàng hóa'로 직역",
                    "correction": "'vận đơn' 또는 'bill of lading (B/L)'이 표준 용어",
                    "explanation": "'giấy chứng nhận hàng hóa'는 일반 증명서를 의미하며, 법적 효력이 있는 유가증권인 선하증권의 개념을 담지 못합니다."
                },
                {
                    "mistake": "'원본 선하증권'을 'vận đơn chính thức'로만 번역",
                    "correction": "'vận đơn gốc' 또는 'bản chính vận đơn'이 정확",
                    "explanation": "'vận đơn gốc'이 베트남 해사법에서 사용하는 공식 용어이며, 'chính thức'는 공식성을 의미하지만 원본성을 명확히 나타내지 못합니다."
                },
                {
                    "mistake": "'Surrendered B/L'을 '포기된 선하증권'으로 직역",
                    "correction": "'vận đơn đã đầu hàng' 또는 'vận đơn đã bỏ quyền'으로 설명",
                    "explanation": "'포기'는 부정적 의미가 있으므로, 베트남어로는 '권리를 양도한' 의미로 설명해야 합니다."
                }
            ],
            "examples": [
                {
                    "ko": "선하증권 원본 3통 중 1통만 제시하면 화물을 인도받을 수 있습니다.",
                    "vi": "Chỉ cần xuất trình 1 trong 3 bản gốc vận đơn là có thể nhận hàng.",
                    "situation": "formal"
                },
                {
                    "ko": "이번 선적은 Telex Release로 진행하니 원본 선하증권 없이 화물 인도 가능합니다.",
                    "vi": "Lô hàng này sử dụng Telex Release nên có thể nhận hàng mà không cần vận đơn gốc.",
                    "situation": "onsite"
                },
                {
                    "ko": "선하증권에 기재된 화물 상태와 실제가 다를 경우 클레임을 제기할 수 있습니다.",
                    "vi": "Nếu tình trạng hàng hóa ghi trên vận đơn khác với thực tế, có thể khiếu nại.",
                    "situation": "formal"
                }
            ],
            "relatedTerms": ["bao-hiem-hang-hai", "van-tai-bien", "hop-dong-van-chuyen", "hai-quan"]
        },
        {
            "slug": "van-tai-bien",
            "korean": "해상운송",
            "vietnamese": "Vận tải biển",
            "hanja": "海上運送",
            "hanjaReading": "海(바다 해) + 上(위 상) + 運(옮길 운) + 送(보낼 송)",
            "pronunciation": "번 타이 비엔",
            "meaningKo": "선박을 이용하여 화물이나 여객을 해상으로 운송하는 행위로, 국제 무역에서 가장 중요한 운송 수단입니다. 통역 시 '해상운송'과 '해상운송계약'을 구분해야 하며, 베트남어로는 각각 'vận tải biển'과 'hợp đồng vận tải biển'으로 명확히 구분됩니다. 해상운송은 정기선(Liner)과 부정기선(Tramper)으로 나뉘며, 컨테이너 운송(Container)과 벌크 운송(Bulk)의 차이도 통역 시 정확히 전달해야 합니다. 베트남은 Incoterms 2020을 적용하므로 FOB, CIF, CFR 등 무역조건 약어를 베트남어로 설명할 수 있어야 하며, 특히 '운송인 책임'과 '화주 책임'의 경계를 명확히 해야 분쟁을 예방할 수 있습니다.",
            "meaningVi": "Vận tải biển là hoạt động vận chuyển hàng hóa hoặc hành khách bằng tàu thủy qua đường biển, là phương thức vận tải chủ yếu trong thương mại quốc tế. Theo Bộ luật Hàng hải Việt Nam 2015, vận tải biển bao gồm vận tải đường biển quốc tế và nội địa. Các loại hình phổ biến: vận tải container (hàng hóa đóng trong container), vận tải rời (bulk cargo như than, gạo), vận tải tàu chở dầu. Vận tải biển có ưu điểm về chi phí thấp, khối lượng lớn nhưng thời gian vận chuyển lâu hơn so với đường hàng không.",
            "context": "수출입 무역, 물류 계약, 운임 협상, 해사법 소송 시 사용",
            "culturalNote": "한국은 세계 5위 해운국으로 HMM, 현대상선 등 글로벌 선사를 보유하고 있으며, 부산항과 인천항은 세계 주요 항구입니다. 베트남은 하노이항, 호치민항(Saigon Port)을 중심으로 해상운송이 발달하고 있으나, 항만 인프라가 한국에 비해 낙후되어 있어 체선료(Demurrage), 체화료(Detention)가 자주 발생합니다. 베트남 기업은 해상운송 용어를 영문 약어(FCL, LCL, THC 등)로 사용하는 경우가 많으므로 통역사는 영문 약어와 베트남어 정식 명칭을 모두 숙지해야 합니다.",
            "commonMistakes": [
                {
                    "mistake": "'해상운송'을 'vận chuyển biển'로 번역",
                    "correction": "'vận tải biển'이 표준 법률 용어",
                    "explanation": "'vận chuyển'은 일반적인 운송을 의미하지만, 'vận tải'는 상업적/공식적 운송을 의미하므로 법률 문서에서는 'vận tải'를 사용해야 합니다."
                },
                {
                    "mistake": "'컨테이너 운송'을 'vận chuyển container'로 직역",
                    "correction": "'vận tải container' 또는 'vận tải hàng hóa đóng container'",
                    "explanation": "베트남 해사법에서는 'vận tải container'가 정식 용어입니다."
                },
                {
                    "mistake": "FOB, CIF 등 약어를 설명 없이 사용",
                    "correction": "'FOB (giao hàng trên tàu)', 'CIF (giá bao gồm bảo hiểm và cước phí)'로 설명",
                    "explanation": "베트남 중소기업은 Incoterms 약어에 익숙하지 않을 수 있으므로 베트남어로 풀어서 설명해야 합니다."
                }
            ],
            "examples": [
                {
                    "ko": "해상운송 계약 시 운임, 체선료, 체화료를 명확히 규정해야 합니다.",
                    "vi": "Khi ký hợp đồng vận tải biển cần quy định rõ cước phí, phí phạt chậm trễ tại cảng và phí giữ container quá hạn.",
                    "situation": "formal"
                },
                {
                    "ko": "이번 선적은 FCL로 진행하며, 부산항에서 하이퐁항까지 약 7일 소요됩니다.",
                    "vi": "Lô hàng này vận chuyển theo hình thức FCL (nguyên container), từ cảng Busan đến cảng Hải Phòng mất khoảng 7 ngày.",
                    "situation": "onsite"
                },
                {
                    "ko": "악천후로 선박이 지연되어 해상운송 일정이 변경되었습니다.",
                    "vi": "Do thời tiết xấu, tàu bị trì hoãn nên lịch trình vận tải biển đã thay đổi.",
                    "situation": "informal"
                }
            ],
            "relatedTerms": ["van-don", "bao-hiem-hang-hai", "cang-bien", "hop-dong-van-chuyen"]
        },
        {
            "slug": "cuu-ho-hang-hai",
            "korean": "해난구조",
            "vietnamese": "Cứu hộ hàng hải",
            "hanja": "海難救助",
            "hanjaReading": "海(바다 해) + 難(어려울 난) + 救(구할 구) + 助(도울 조)",
            "pronunciation": "끄우 호 항 하이",
            "meaningKo": "해상에서 조난당한 선박, 화물, 인명을 구조하는 행위로, 국제해사법과 각국 해사법에서 규정하는 법적 행위입니다. 통역 시 '해난구조'와 '예인(曳引, towing)'을 명확히 구분해야 하며, 해난구조는 위험 상황에서의 구조를 의미하고 예인은 단순 견인을 의미합니다. 베트남 해사법은 'No Cure, No Pay' 원칙을 따르므로, 구조가 성공한 경우에만 구조료를 지급하며, 구조료 산정은 구조된 선박과 화물의 가액, 구조의 난이도 등을 고려합니다. 통역 시 'salvage award'(구조료), 'salvor'(구조자), 'salvaged property'(구조된 재산)를 베트남어로 정확히 표현해야 하며, 국제해사기구(IMO)의 국제해난구조협약(1989)과 베트남 국내법의 차이를 이해해야 합니다.",
            "meaningVi": "Cứu hộ hàng hải là hoạt động cứu giúp tàu thuyền, hàng hóa hoặc người gặp nạn trên biển. Theo Bộ luật Hàng hải Việt Nam 2015, cứu hộ hàng hải tuân thủ nguyên tắc 'Không cứu được, không trả tiền' (No Cure, No Pay), nghĩa là chỉ trả thù lao cứu hộ khi cứu hộ thành công. Thù lao cứu hộ được tính dựa trên giá trị tài sản cứu được, mức độ nguy hiểm, nỗ lực và thời gian của người cứu hộ. Cần phân biệt 'cứu hộ hàng hải' (salvage) với 'lai dắt' (towing - chỉ đơn thuần kéo tàu không có yếu tố nguy hiểm).",
            "context": "해사법 소송, 보험 청구, 해난 사고 협상, 해사 중재 시 사용",
            "culturalNote": "한국은 해양수산부 산하 해양경찰청과 민간 구조업체(예: 해양구조협회)가 협력하여 해난구조를 수행하며, 국제해난구조협약(1989)을 비준했습니다. 베트남도 동 협약을 비준했으나, 실무에서는 국영 구조업체(Vietnam Salvage Corporation)가 주도하며, 민간 참여가 제한적입니다. 베트남 해역에서 한국 선박이 조난당할 경우, 구조료 협상 시 양국 법체계 차이로 분쟁이 발생할 수 있으므로 통역사는 양국 해사법 규정을 숙지해야 합니다. 특히 베트남은 구조료 산정 시 베트남 법원의 판단을 우선하므로, 한국 기업은 이를 사전에 인지해야 합니다.",
            "commonMistakes": [
                {
                    "mistake": "'해난구조'를 'cứu nạn trên biển'로 직역",
                    "correction": "'cứu hộ hàng hải'가 법률 용어",
                    "explanation": "'cứu nạn'은 일반적인 구조를 의미하지만, 'cứu hộ hàng hải'는 법적 효력이 있는 해난구조 행위를 의미합니다."
                },
                {
                    "mistake": "'구조료'를 'tiền cứu hộ'로만 번역",
                    "correction": "'thù lao cứu hộ' 또는 'tiền thưởng cứu hộ'가 정확",
                    "explanation": "'tiền cứu hộ'는 일반적인 구조 비용을 의미하지만, 'thù lao cứu hộ'는 법적 보상 개념을 포함합니다."
                },
                {
                    "mistake": "'예인'과 '해난구조'를 모두 'cứu hộ'로 번역",
                    "correction": "예인은 'lai dắt', 해난구조는 'cứu hộ hàng hải'",
                    "explanation": "예인은 위험이 없는 단순 견인이므로 법적 성격이 다릅니다."
                }
            ],
            "examples": [
                {
                    "ko": "태풍으로 조난당한 선박을 구조하여 구조료 100만 달러를 청구했습니다.",
                    "vi": "Đã cứu hộ tàu gặp nạn do bão và yêu cầu thù lao cứu hộ 1 triệu USD.",
                    "situation": "formal"
                },
                {
                    "ko": "해난구조 계약은 'No Cure, No Pay' 원칙에 따라 성공 시에만 비용을 지급합니다.",
                    "vi": "Hợp đồng cứu hộ hàng hải theo nguyên tắc 'Không cứu được, không trả tiền', chỉ thanh toán khi cứu hộ thành công.",
                    "situation": "formal"
                },
                {
                    "ko": "구조된 화물의 가액에 따라 구조료가 산정됩니다.",
                    "vi": "Thù lao cứu hộ được tính dựa trên giá trị hàng hóa đã cứu được.",
                    "situation": "onsite"
                }
            ],
            "relatedTerms": ["bao-hiem-hang-hai", "ton-that-chung", "tai-nan-hang-hai", "trach-nhiem-chu-tau"]
        },
        {
            "slug": "ton-that-chung",
            "korean": "공동해손",
            "vietnamese": "Tổn thất chung",
            "hanja": "共同海損",
            "hanjaReading": "共(함께 공) + 同(한가지 동) + 海(바다 해) + 損(덜 손)",
            "pronunciation": "똔 탓 쭝",
            "meaningKo": "해상 위험 발생 시 선박과 화물의 공동 안전을 위해 선장이 고의적이고 합리적으로 취한 특별한 희생이나 비용으로, 이해관계자 전원이 비례적으로 분담하는 제도입니다. 통역 시 '공동해손'과 '단독해손'을 명확히 구분해야 하며, 공동해손은 전원이 분담하고 단독해손은 해당 당사자만 부담합니다. 베트남 해사법은 York-Antwerp Rules(국제 공동해손 규칙)를 준용하지만, 공동해손 정산은 복잡하고 시간이 오래 걸리므로 통역 시 '정산인(Average Adjuster)', '공동해손 담보(General Average Guarantee)' 등의 용어를 정확히 전달해야 합니다. 특히 한국 화주가 베트남 선박에 화물을 적재한 경우, 공동해손 선언 시 화주도 분담 의무가 있음을 명확히 설명해야 분쟁을 예방할 수 있습니다.",
            "meaningVi": "Tổn thất chung (General Average) là thiệt hại hoặc chi phí đặc biệt phát sinh do thuyền trưởng cố ý và hợp lý thực hiện để bảo vệ an toàn chung cho tàu và hàng hóa trong tình huống nguy hiểm trên biển, và được tất cả bên liên quan chia sẻ theo tỷ lệ giá trị tài sản. Theo Bộ luật Hàng hải Việt Nam 2015 và quy tắc York-Antwerp Rules, các trường hợp điển hình của tổn thất chung: vứt hàng xuống biển để giảm trọng lượng tàu, chi phí lánh nạn tại cảng trú ẩn, chi phí cứu hỏa trên tàu. Cần phân biệt với 'tổn thất riêng' (particular average) chỉ do một bên chịu.",
            "context": "해상 사고 보험 청구, 해운 분쟁 조정, 공동해손 정산 협상 시 사용",
            "culturalNote": "한국은 해운 산업이 발달하여 공동해손 정산 실무가 정교하며, 국제 정산인(Average Adjuster)을 통해 정산합니다. 베트남은 공동해손 사례가 상대적으로 적고, 국내 정산 전문가가 부족하여 대부분 싱가포르나 홍콩의 정산인에게 의뢰합니다. 베트남 화주는 공동해손 개념에 익숙하지 않아 '왜 내 화물이 무사한데 비용을 분담해야 하는가'라는 오해가 자주 발생하므로, 통역사는 공동해손의 법리를 쉽게 설명해야 합니다. 특히 공동해손 담보(GA Guarantee)를 제공하지 않으면 화물 인도가 지연될 수 있음을 명확히 전달해야 합니다.",
            "commonMistakes": [
                {
                    "mistake": "'공동해손'을 'thiệt hại chung'으로 직역",
                    "correction": "'tổn thất chung'이 법률 용어",
                    "explanation": "'thiệt hại'는 일반적인 손해를 의미하지만, 'tổn thất'은 법률적 손실 개념을 포함합니다."
                },
                {
                    "mistake": "'단독해손'과 '공동해손'을 구분하지 않고 모두 'tổn thất'로만 번역",
                    "correction": "단독해손은 'tổn thất riêng', 공동해손은 'tổn thất chung'",
                    "explanation": "양자의 법적 성격과 분담 주체가 완전히 다르므로 명확히 구분해야 합니다."
                },
                {
                    "mistake": "'공동해손 정산인'을 'người tính toán tổn thất chung'으로 직역",
                    "correction": "'chuyên gia điều chỉnh tổn thất chung' 또는 'Average Adjuster'",
                    "explanation": "'điều chỉnh'는 정산 전문가의 역할을 정확히 표현하며, 실무에서는 영문 'Average Adjuster'를 병기합니다."
                }
            ],
            "examples": [
                {
                    "ko": "선박 화재 진압을 위해 발생한 비용은 공동해손으로 인정되어 화주들이 분담합니다.",
                    "vi": "Chi phí dập cháy trên tàu được công nhận là tổn thất chung và được các chủ hàng chia sẻ.",
                    "situation": "formal"
                },
                {
                    "ko": "공동해손이 선언되면 화물 인도 전에 공동해손 담보를 제공해야 합니다.",
                    "vi": "Khi tổn thất chung được công bố, phải cung cấp bảo lãnh tổn thất chung trước khi nhận hàng.",
                    "situation": "formal"
                },
                {
                    "ko": "이번 사고는 공동해손에 해당하므로 정산인이 배정되었습니다.",
                    "vi": "Vụ tai nạn này thuộc trường hợp tổn thất chung nên chuyên gia điều chỉnh đã được chỉ định.",
                    "situation": "onsite"
                }
            ],
            "relatedTerms": ["bao-hiem-hang-hai", "cuu-ho-hang-hai", "ton-that-rieng", "chinh-san-ton-that"]
        },
        {
            "slug": "trach-nhiem-van-chuyen",
            "korean": "운송인책임",
            "vietnamese": "Trách nhiệm vận chuyển",
            "hanja": "運送人責任",
            "hanjaReading": "運(옮길 운) + 送(보낼 송) + 人(사람 인) + 責(꾸짖을 책) + 任(맡길 임)",
            "pronunciation": "짝 니엠 번 쭈엔",
            "meaningKo": "운송인이 화물의 수령부터 인도까지 화물의 멸실, 손상, 연착에 대해 지는 법적 책임으로, 해상운송에서는 선박회사가, 육상운송에서는 운송업체가 책임 주체입니다. 통역 시 '운송인 책임'과 '화주 책임'을 명확히 구분해야 하며, Incoterms(FOB, CIF 등)에 따라 책임 이전 시점이 달라지므로 정확한 용어 사용이 중요합니다. 베트남 상법은 '입증책임의 전환'을 규정하여, 운송인이 화물 손상 시 자신의 무과실을 입증해야 책임을 면할 수 있습니다. 통역 시 '면책사유(면책 약관)', '책임한도액', '손해배상청구권 소멸시효' 등을 베트남어로 정확히 전달해야 하며, 특히 베트남은 '불가항력(force majeure)'의 범위가 넓어 한국 기업이 예상하지 못한 면책 주장이 나올 수 있음을 주의해야 합니다.",
            "meaningVi": "Trách nhiệm vận chuyển là trách nhiệm pháp lý mà người vận chuyển (carrier) phải chịu đối với việc mất mát, hư hỏng hoặc chậm trễ hàng hóa từ lúc nhận hàng đến lúc giao hàng. Theo Luật Thương mại Việt Nam 2005 và Bộ luật Hàng hải 2015, người vận chuyển phải bồi thường thiệt hại trừ khi chứng minh được thiệt hại do bất khả kháng, khuyết tật riêng của hàng hóa, hoặc lỗi của người gửi hàng. Trách nhiệm được giới hạn theo quy định pháp luật (ví dụ: 666,67 SDR/kiện theo công ước quốc tế), trừ khi người vận chuyển cố ý hoặc vô ý thực hiện hành vi gây thiệt hại.",
            "context": "운송 계약 협상, 화물 사고 배상 청구, 보험 청구, 물류 분쟁 조정 시 사용",
            "culturalNote": "한국은 상법과 해상물품운송법에서 운송인 책임을 명확히 규정하고 있으며, 국제 협약(Hague-Visby Rules, Hamburg Rules)을 따릅니다. 베트남은 Hague-Visby Rules를 부분적으로 수용하되, 베트남 상법과 해사법이 우선 적용됩니다. 베트남 운송업체는 '불가항력' 항변을 자주 사용하므로, 한국 화주는 계약서에 면책 사유를 구체적으로 명시해야 합니다. 또한 베트남은 책임한도액이 한국보다 낮은 경우가 많아, 고가 화물은 별도 부보가 필요합니다. 통역사는 '책임한도액'과 '실제 손해액'의 차이를 명확히 설명해야 화주의 오해를 방지할 수 있습니다.",
            "commonMistakes": [
                {
                    "mistake": "'운송인 책임'을 'trách nhiệm của người vận chuyển'로만 번역",
                    "correction": "'trách nhiệm vận chuyển'이 간결한 법률 용어",
                    "explanation": "베트남 상법에서는 'trách nhiệm vận chuyển'을 표준 용어로 사용합니다."
                },
                {
                    "mistake": "'책임한도액'을 'số tiền trách nhiệm'으로 직역",
                    "correction": "'giới hạn trách nhiệm' 또는 'mức bồi thường tối đa'",
                    "explanation": "'giới hạn trách nhiệm'이 법률적 한도 개념을 정확히 표현합니다."
                },
                {
                    "mistake": "'불가항력'을 'không thể kiểm soát'로 직역",
                    "correction": "'bất khả kháng'이 법률 용어",
                    "explanation": "'bất khả kháng'은 베트남 민법과 상법에서 사용하는 공식 용어입니다."
                }
            ],
            "examples": [
                {
                    "ko": "운송 중 화물이 손상되었으나 운송인이 불가항력을 입증하여 책임을 면했습니다.",
                    "vi": "Hàng hóa bị hư hỏng trong vận chuyển nhưng người vận chuyển đã chứng minh bất khả kháng nên được miễn trách nhiệm.",
                    "situation": "formal"
                },
                {
                    "ko": "운송인 책임은 화물 가액의 일정 비율로 제한되므로 고가 화물은 별도 보험이 필요합니다.",
                    "vi": "Trách nhiệm vận chuyển được giới hạn theo tỷ lệ nhất định của giá trị hàng hóa, nên hàng hóa giá trị cao cần mua bảo hiểm riêng.",
                    "situation": "formal"
                },
                {
                    "ko": "운송인이 과실로 화물을 분실한 경우 책임한도를 초과하여 배상해야 합니다.",
                    "vi": "Nếu người vận chuyển làm mất hàng do lỗi cố ý, phải bồi thường vượt giới hạn trách nhiệm.",
                    "situation": "onsite"
                }
            ],
            "relatedTerms": ["van-don", "van-tai-bien", "bao-hiem-hang-hai", "hop-dong-van-chuyen"]
        },
        {
            "slug": "bao-hiem-nhan-tho",
            "korean": "생명보험",
            "vietnamese": "Bảo hiểm nhân thọ",
            "hanja": "生命保險",
            "hanjaReading": "生(날 생) + 命(목숨 명) + 保(지킬 보) + 險(험할 험)",
            "pronunciation": "바오 히엠 년 토",
            "meaningKo": "사람의 생존 또는 사망을 보험사고로 하여 보험금을 지급하는 인보험으로, 사망보험, 생존보험, 생사혼합보험으로 구분됩니다. 통역 시 '생명보험'과 '손해보험'을 명확히 구분해야 하며, 생명보험은 정액 보상, 손해보험은 실손 보상이 원칙입니다. 베트남어로는 'bảo hiểm nhân thọ'(생명보험)와 'bảo hiểm phi nhân thọ'(손해보험)로 구분되며, 베트남 보험법(2022년 개정)은 보험계약자, 피보험자, 수익자의 권리와 의무를 명확히 규정하고 있습니다. 통역 시 '보험료(phí bảo hiểm)', '보험금(tiền bảo hiểm)', '해약환급금(tiền hoàn lại khi hủy hợp đồng)'을 정확히 구분해야 하며, 베트남은 생명보험 가입률이 낮아 보험 용어에 익숙하지 않은 고객이 많으므로 쉬운 설명이 필요합니다.",
            "meaningVi": "Bảo hiểm nhân thọ là loại hình bảo hiểm dựa trên sự sống hoặc chết của người được bảo hiểm, chi trả tiền bảo hiểm khi xảy ra sự kiện bảo hiểm. Theo Luật Kinh doanh Bảo hiểm Việt Nam 2022, bảo hiểm nhân thọ bao gồm: bảo hiểm tử kỳ (chi trả khi người được bảo hiểm chết), bảo hiểm sinh kỳ (chi trả khi người được bảo hiểm sống đến thời hạn), bảo hiểm hỗn hợp (kết hợp cả hai). Bảo hiểm nhân thọ chi trả theo số tiền đã thỏa thuận, không phụ thuộc vào thiệt hại thực tế. Cần phân biệt với 'bảo hiểm phi nhân thọ' (bảo hiểm tài sản, trách nhiệm).",
            "context": "보험 상품 설명, 보험 계약 체결, 보험금 청구, 금융 상담 시 사용",
            "culturalNote": "한국은 생명보험 가입률이 높고 다양한 상품이 발달되어 있으며, 변액보험, 유니버셜보험 등 투자형 보험도 활성화되어 있습니다. 베트남은 생명보험 시장이 성장 중이나 가입률은 여전히 낮으며(인구의 약 15%), 국영 보험사(Bảo Việt, Bảo Minh)와 외국계 보험사(Prudential, Manulife)가 시장을 양분하고 있습니다. 베트남 고객은 보험을 저축 수단으로 인식하는 경우가 많아, '보장'과 '저축'의 차이를 명확히 설명해야 합니다. 또한 베트남은 보험금 청구 절차가 복잡하고 분쟁이 자주 발생하므로, 통역 시 청구 요건을 정확히 전달해야 합니다.",
            "commonMistakes": [
                {
                    "mistake": "'생명보험'을 'bảo hiểm sinh mạng'으로 직역",
                    "correction": "'bảo hiểm nhân thọ'가 표준 법률 용어",
                    "explanation": "'sinh mạng'은 일상어이지만, 'nhân thọ'는 보험법에서 사용하는 공식 용어입니다."
                },
                {
                    "mistake": "'보험금'과 '보험료'를 모두 'tiền bảo hiểm'으로 번역",
                    "correction": "보험료는 'phí bảo hiểm', 보험금은 'tiền bảo hiểm' 또는 'số tiền chi trả'",
                    "explanation": "보험료는 납부하는 금액, 보험금은 수령하는 금액이므로 명확히 구분해야 합니다."
                },
                {
                    "mistake": "'피보험자'를 'người mua bảo hiểm'으로 번역",
                    "correction": "'người được bảo hiểm'이 정확",
                    "explanation": "'người mua bảo hiểm'은 보험계약자(보험료 납부자)를 의미하며, 피보험자는 보험 대상자입니다."
                }
            ],
            "examples": [
                {
                    "ko": "생명보험 계약 시 피보험자의 건강 상태를 정확히 고지해야 합니다.",
                    "vi": "Khi ký hợp đồng bảo hiểm nhân thọ phải khai báo chính xác tình trạng sức khỏe của người được bảo hiểm.",
                    "situation": "formal"
                },
                {
                    "ko": "이 상품은 사망 시 1억 동을 지급하는 정기 생명보험입니다.",
                    "vi": "Sản phẩm này là bảo hiểm nhân thọ định kỳ, chi trả 100 triệu đồng khi người được bảo hiểm tử vong.",
                    "situation": "onsite"
                },
                {
                    "ko": "생명보험 수익자를 변경하려면 보험사에 서면으로 통보해야 합니다.",
                    "vi": "Để thay đổi người thụ hưởng bảo hiểm nhân thọ cần thông báo bằng văn bản cho công ty bảo hiểm.",
                    "situation": "formal"
                }
            ],
            "relatedTerms": ["bao-hiem-tai-san", "hop-dong-bao-hiem", "doi-boi-thuong", "phi-bao-hiem"]
        },
        {
            "slug": "bao-hiem-tai-san",
            "korean": "재산보험",
            "vietnamese": "Bảo hiểm tài sản",
            "hanja": "財產保險",
            "hanjaReading": "財(재물 재) + 產(낳을 산) + 保(지킬 보) + 險(험할 험)",
            "pronunciation": "바오 히엠 따이 산",
            "meaningKo": "화재, 도난, 자연재해 등으로 인한 재산상의 손해를 보상하는 손해보험의 일종으로, 실손 보상 원칙을 따릅니다. 통역 시 '재산보험'과 '배상책임보험'을 구분해야 하며, 재산보험은 자신의 재산 손해를 보상하고 배상책임보험은 타인에게 끼친 손해를 보상합니다. 베트남어로는 'bảo hiểm tài sản'이며, 베트남 보험법은 보험가액(giá trị bảo hiểm)과 보험금액(số tiền bảo hiểm)을 구분하여, 보험금액이 보험가액을 초과할 수 없도록 규정합니다(초과보험 금지). 통역 시 '일부보험(bảo hiểm không đầy đủ)', '비례보상(bồi thường theo tỷ lệ)', '면책금액(mức miễn thường)' 등을 정확히 전달해야 하며, 베트남은 자연재해가 잦아 풍수해 보험의 중요성이 크므로 관련 용어를 숙지해야 합니다.",
            "meaningVi": "Bảo hiểm tài sản là loại hình bảo hiểm bồi thường thiệt hại về tài sản do hỏa hoạn, trộm cắp, thiên tai hoặc các rủi ro khác. Theo Luật Kinh doanh Bảo hiểm Việt Nam 2022, bảo hiểm tài sản tuân thủ nguyên tắc bồi thường thực tế, nghĩa là chỉ bồi thường đúng mức thiệt hại thực tế (không vượt quá giá trị tài sản). Các loại bảo hiểm tài sản phổ biến: bảo hiểm nhà cửa, bảo hiểm xe cộ, bảo hiểm hàng hóa, bảo hiểm thiết bị. Cần phân biệt với 'bảo hiểm trách nhiệm' (bồi thường thiệt hại gây ra cho bên thứ ba).",
            "context": "부동산 계약, 차량 구매, 공장 설립, 보험 청구, 재난 대응 시 사용",
            "culturalNote": "한국은 주택화재보험, 자동차보험 등 재산보험 가입률이 높으며, 의무보험(자동차 책임보험 등)이 발달되어 있습니다. 베트남은 재산보험 가입률이 낮고(기업의 약 30%, 개인은 더 낮음), 자연재해(태풍, 홍수) 발생 시 보험 청구가 급증합니다. 베트남은 보험금 지급이 지연되거나 분쟁이 자주 발생하므로, 통역 시 청구 절차와 필요 서류를 명확히 전달해야 합니다. 특히 베트남은 '감가상각'을 적용하여 보험금을 산정하므로, 한국 고객이 예상보다 적은 보험금을 받을 수 있음을 사전에 설명해야 합니다.",
            "commonMistakes": [
                {
                    "mistake": "'재산보험'을 'bảo hiểm của cải'로 직역",
                    "correction": "'bảo hiểm tài sản'이 법률 용어",
                    "explanation": "'của cải'는 일상어이지만, 'tài sản'은 법률적 재산 개념을 포함합니다."
                },
                {
                    "mistake": "'보험가액'과 '보험금액'을 모두 'số tiền bảo hiểm'으로 번역",
                    "correction": "보험가액은 'giá trị bảo hiểm', 보험금액은 'số tiền bảo hiểm'",
                    "explanation": "보험가액은 재산의 실제 가치, 보험금액은 보험 계약 금액이므로 구분이 필요합니다."
                },
                {
                    "mistake": "'일부보험'을 'bảo hiểm một phần'으로만 번역",
                    "correction": "'bảo hiểm không đầy đủ' 또는 'bảo hiểm thiếu'가 정확",
                    "explanation": "'bảo hiểm không đầy đủ'가 베트남 보험법에서 사용하는 공식 용어입니다."
                }
            ],
            "examples": [
                {
                    "ko": "공장 화재로 발생한 손해는 재산보험으로 보상받을 수 있습니다.",
                    "vi": "Thiệt hại do hỏa hoạn nhà máy có thể được bồi thường qua bảo hiểm tài sản.",
                    "situation": "formal"
                },
                {
                    "ko": "보험금액이 재산 가치의 80%에 불과하므로 비례보상이 적용됩니다.",
                    "vi": "Số tiền bảo hiểm chỉ bằng 80% giá trị tài sản nên áp dụng bồi thường theo tỷ lệ.",
                    "situation": "formal"
                },
                {
                    "ko": "자동차 재산보험에는 자차 손해와 도난이 포함됩니다.",
                    "vi": "Bảo hiểm tài sản ô tô bao gồm thiệt hại xe và trộm cắp.",
                    "situation": "onsite"
                }
            ],
            "relatedTerms": ["bao-hiem-nhan-tho", "bao-hiem-trach-nhiem", "bao-hiem-chay-no", "bao-hiem-xe-co"]
        },
        {
            "slug": "hop-dong-bao-hiem",
            "korean": "보험계약",
            "vietnamese": "Hợp đồng bảo hiểm",
            "hanja": "保險契約",
            "hanjaReading": "保(지킬 보) + 險(험할 험) + 契(맺을 계) + 約(맺을 약)",
            "pronunciation": "헙 동 바오 히엠",
            "meaningKo": "보험계약자가 보험료를 지급하고 보험자가 보험사고 발생 시 보험금을 지급하기로 약정하는 계약으로, 상법상 불요식 계약이지만 보험증권으로 증명됩니다. 통역 시 '보험계약자(보험료 납부자)', '피보험자(보험 대상자)', '보험수익자(보험금 수령자)'를 명확히 구분해야 하며, 베트남어로는 각각 'bên mua bảo hiểm', 'người được bảo hiểm', 'người thụ hưởng'입니다. 보험계약은 최대선의의 원칙(utmost good faith)을 따르므로, 고지의무 위반 시 계약이 무효가 될 수 있습니다. 통역 시 '고지의무(nghĩa vụ khai báo)', '계약 전 알릴 의무(nghĩa vụ thông báo trước khi ký hợp đồng)', '면책조항(điều khoản miễn trách nhiệm)'을 정확히 전달해야 하며, 베트남은 보험 약관이 복잡하고 분쟁이 자주 발생하므로 계약서 해석에 주의가 필요합니다.",
            "meaningVi": "Hợp đồng bảo hiểm là thỏa thuận giữa bên mua bảo hiểm (người mua) và công ty bảo hiểm (người bán), trong đó bên mua đóng phí bảo hiểm và công ty bảo hiểm cam kết chi trả tiền bảo hiểm khi xảy ra sự kiện bảo hiểm. Theo Luật Kinh doanh Bảo hiểm Việt Nam 2022, hợp đồng bảo hiểm phải có các yếu tố: bên mua bảo hiểm, người được bảo hiểm, người thụ hưởng, phí bảo hiểm, số tiền bảo hiểm, thời hạn bảo hiểm, sự kiện bảo hiểm. Hợp đồng bảo hiểm tuân thủ nguyên tắc thiện chí tối đa (utmost good faith), nghĩa là bên mua phải khai báo đầy đủ thông tin.",
            "context": "보험 상품 판매, 계약 체결, 계약 해석, 보험 분쟁 조정 시 사용",
            "culturalNote": "한국은 보험 계약법이 상법에 명시되어 있으며, 표준 약관이 발달되어 있고, 금융감독원이 보험 계약 분쟁을 조정합니다. 베트남은 보험법(2022)과 민법(2015)에 보험 계약 규정이 있으며, 보험 약관이 복잡하고 베트남어 번역이 부정확한 경우가 많아 분쟁이 자주 발생합니다. 베트남 고객은 보험 약관을 자세히 읽지 않는 경향이 있어, 통역 시 주요 조항(특히 면책조항)을 강조해야 합니다. 또한 베트남은 보험 계약 해지 시 환급금이 적거나 없는 경우가 많아, 이를 사전에 명확히 설명해야 분쟁을 예방할 수 있습니다.",
            "commonMistakes": [
                {
                    "mistake": "'보험계약자'와 '피보험자'를 모두 'người mua bảo hiểm'으로 번역",
                    "correction": "보험계약자는 'bên mua bảo hiểm', 피보험자는 'người được bảo hiểm'",
                    "explanation": "보험계약자는 보험료를 내는 사람, 피보험자는 보험 대상자로 역할이 다릅니다."
                },
                {
                    "mistake": "'고지의무'를 'nghĩa vụ báo cáo'로 직역",
                    "correction": "'nghĩa vụ khai báo' 또는 'nghĩa vụ thông báo trung thực'",
                    "explanation": "'khai báo'는 법률적 고지 의무를 정확히 표현하며, 'báo cáo'는 일반 보고를 의미합니다."
                },
                {
                    "mistake": "'보험증권'을 'chứng chỉ bảo hiểm'으로만 번역",
                    "correction": "'giấy chứng nhận bảo hiểm' 또는 'đơn bảo hiểm'",
                    "explanation": "'giấy chứng nhận bảo hiểm'이 베트남 보험법에서 사용하는 공식 용어입니다."
                }
            ],
            "examples": [
                {
                    "ko": "보험계약 체결 시 기존 질병을 고지하지 않으면 계약이 무효가 될 수 있습니다.",
                    "vi": "Khi ký hợp đồng bảo hiểm, nếu không khai báo bệnh lý hiện có, hợp đồng có thể bị vô hiệu.",
                    "situation": "formal"
                },
                {
                    "ko": "이 보험계약은 피보험자가 사망하면 배우자에게 보험금이 지급됩니다.",
                    "vi": "Theo hợp đồng bảo hiểm này, khi người được bảo hiểm tử vong, tiền bảo hiểm sẽ được chi trả cho vợ/chồng.",
                    "situation": "formal"
                },
                {
                    "ko": "보험계약서의 면책조항을 주의 깊게 확인해야 합니다.",
                    "vi": "Cần kiểm tra kỹ các điều khoản miễn trách nhiệm trong hợp đồng bảo hiểm.",
                    "situation": "onsite"
                }
            ],
            "relatedTerms": ["bao-hiem-nhan-tho", "bao-hiem-tai-san", "doi-boi-thuong", "phi-bao-hiem"]
        },
        {
            "slug": "doi-boi-thuong",
            "korean": "보험금청구",
            "vietnamese": "Đòi bồi thường",
            "hanja": "保險金請求",
            "hanjaReading": "保(지킬 보) + 險(험할 험) + 金(쇠 금) + 請(청할 청) + 求(구할 구)",
            "pronunciation": "도이 보이 투엉",
            "meaningKo": "보험사고 발생 시 보험계약자 또는 수익자가 보험회사에 보험금 지급을 요구하는 행위로, 청구 절차와 필요 서류가 법령과 약관에 규정되어 있습니다. 통역 시 '보험금 청구'와 '손해배상 청구'를 구분해야 하며, 보험금 청구는 보험 계약에 따른 것이고 손해배상 청구는 불법행위에 따른 것입니다. 베트남어로는 'đòi bồi thường'(보상 청구) 또는 'yêu cầu chi trả bảo hiểm'(보험금 지급 요청)이며, 베트남 보험법은 청구 서류(giấy tờ yêu cầu bồi thường)와 청구 기한(thời hạn yêu cầu bồi thường)을 명시하고 있습니다. 통역 시 '사고 증명서(giấy chứng nhận tai nạn)', '의료 기록(hồ sơ y tế)', '손해 감정서(giấy định giá thiệt hại)' 등 필요 서류를 정확히 전달해야 하며, 베트남은 서류 심사가 까다롭고 청구 처리가 지연되는 경우가 많으므로 인내심을 가지고 설명해야 합니다.",
            "meaningVi": "Đòi bồi thường (hay yêu cầu chi trả bảo hiểm) là hành vi của bên mua bảo hiểm hoặc người thụ hưởng yêu cầu công ty bảo hiểm chi trả tiền bảo hiểm khi xảy ra sự kiện bảo hiểm. Theo Luật Kinh doanh Bảo hiểm Việt Nam 2022, người yêu cầu bồi thường phải cung cấp đầy đủ giấy tờ chứng minh (giấy chứng nhận tai nạn, hồ sơ y tế, hóa đơn chi phí, v.v.) trong thời hạn quy định. Công ty bảo hiểm phải xem xét và chi trả trong 15 ngày (bảo hiểm phi nhân thọ) hoặc 30 ngày (bảo hiểm nhân thọ) kể từ khi nhận đủ hồ sơ hợp lệ.",
            "context": "보험 사고 발생 후, 병원 치료 후, 재산 손해 발생 시 사용",
            "culturalNote": "한국은 보험금 청구 절차가 간소화되어 있으며, 온라인/모바일로 신속하게 청구할 수 있고, 금융감독원이 보험금 지급 지연을 감독합니다. 베트남은 보험금 청구 절차가 복잡하고 서류 요구가 많으며, 청구 처리가 지연되는 경우가 많아 고객 불만이 자주 발생합니다. 베트남 보험사는 청구를 거부하거나 감액하는 경우가 많으므로, 통역 시 청구 거부 사유를 명확히 설명하고, 필요 시 이의 제기(khiếu nại) 절차를 안내해야 합니다. 특히 의료 보험금 청구 시 베트남은 공립병원 영수증만 인정하는 경우가 있어, 사전에 인정 병원 목록을 확인하도록 안내해야 합니다.",
            "commonMistakes": [
                {
                    "mistake": "'보험금 청구'를 'yêu cầu tiền bảo hiểm'으로만 번역",
                    "correction": "'đòi bồi thường' 또는 'yêu cầu chi trả bảo hiểm'이 정확",
                    "explanation": "'đòi bồi thường'이 베트남 보험업계에서 통용되는 표준 용어입니다."
                },
                {
                    "mistake": "'청구 서류'를 'giấy tờ yêu cầu'로만 번역",
                    "correction": "'hồ sơ yêu cầu bồi thường' 또는 'giấy tờ chứng minh'",
                    "explanation": "'hồ sơ'는 서류 세트를 의미하며, 보험 청구 시 여러 서류가 필요하므로 'hồ sơ'가 적합합니다."
                },
                {
                    "mistake": "'청구 거부'를 'từ chối yêu cầu'로만 번역",
                    "correction": "'từ chối bồi thường' 또는 'không chấp nhận yêu cầu chi trả'",
                    "explanation": "'từ chối bồi thường'이 보험금 지급 거부를 명확히 표현합니다."
                }
            ],
            "examples": [
                {
                    "ko": "교통사고 후 30일 이내에 보험금을 청구해야 합니다.",
                    "vi": "Sau tai nạn giao thông phải yêu cầu chi trả bảo hiểm trong vòng 30 ngày.",
                    "situation": "formal"
                },
                {
                    "ko": "보험금 청구 시 사고 경위서와 진단서를 함께 제출해야 합니다.",
                    "vi": "Khi đòi bồi thường cần nộp cả biên bản tai nạn và giấy chẩn đoán.",
                    "situation": "onsite"
                },
                {
                    "ko": "청구가 거부되면 이의 제기를 할 수 있습니다.",
                    "vi": "Nếu yêu cầu bồi thường bị từ chối, có thể khiếu nại.",
                    "situation": "formal"
                }
            ],
            "relatedTerms": ["hop-dong-bao-hiem", "bao-hiem-nhan-tho", "bao-hiem-tai-san", "tranh-chap-bao-hiem"]
        }
    ]

    # 5. 중복 제거
    new_terms_filtered = [t for t in new_terms if t['slug'] not in existing_slugs]

    if not new_terms_filtered:
        print("⚠️  모든 용어가 이미 존재합니다. 추가할 항목이 없습니다.")
        return

    # 6. 데이터 병합
    data.extend(new_terms_filtered)

    # 7. 저장
    with open(file_path, 'w', encoding='utf-8') as f:
        json.dump(data, f, ensure_ascii=False, indent=2)

    print(f"✅ {len(new_terms_filtered)}개 용어 추가 완료!")
    print(f"📂 파일: {file_path}")
    print("\n추가된 용어:")
    for term in new_terms_filtered:
        print(f"  - {term['slug']} ({term['korean']} / {term['vietnamese']})")


if __name__ == "__main__":
    main()
