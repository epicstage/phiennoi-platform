#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
세법/조세 전문용어 추가 스크립트 (Tax Law Terms)
Tier S 품질 기준 준수
"""

import json
import os

def main():
    # 1. 파일 경로 설정 (CRITICAL: relative path from script location)
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

    # 3. 기존 slug 수집 (중복 방지)
    existing_slugs = {t['slug'] for t in data}

    # 4. 새 용어 정의 (Tier S 기준)
    new_terms = [
        {
            "slug": "thue-thu-nhap-doanh-nghiep",
            "korean": "법인세",
            "vietnamese": "thuế thu nhập doanh nghiệp",
            "hanja": "法人稅",
            "hanjaReading": "法(법 법) + 人(사람 인) + 稅(세금 세)",
            "pronunciation": "터에 투 늅 도안 응이업",
            "meaningKo": "법인(회사)의 소득에 부과되는 세금입니다. 통역 시 주의할 점은 베트남의 법인세율(20%)과 한국의 법인세율(10~25% 누진세)이 다르므로, 단순히 세율만 통역하면 오해가 생길 수 있습니다. 베트남은 단일세율, 한국은 과세표준 구간별 차등세율이 적용되므로 '누진세 방식'임을 명확히 설명해야 합니다. 또한 베트남에서는 'thuế TNDN'으로 줄여 부르는 경우가 많으니 약어에도 익숙해야 합니다.",
            "meaningVi": "Là loại thuế đánh vào thu nhập của doanh nghiệp (công ty). Thuế suất thuế thu nhập doanh nghiệp ở Việt Nam là 20% (thuế suất đơn), trong khi Hàn Quốc áp dụng thuế suất lũy tiến từ 10% đến 25% tùy theo mức thu nhập. Thông dịch viên cần làm rõ sự khác biệt này để tránh hiểu lầm.",
            "context": "법인 재무제표, 세무 신고, 투자 계약서",
            "culturalNote": "한국은 법인세 신고를 연 1회(사업연도 종료 후 3개월 이내) 하지만 베트남은 분기별 잠정 신고와 연말 확정 신고로 나뉩니다. 또한 베트남은 외국인 투자기업에 대해 법인세 감면 혜택(예: 최초 2년 면제, 이후 4년 50% 감면)을 제공하는 경우가 많아 한국 투자자들이 자주 문의합니다. 통역 시 'ưu đãi thuế'(세제혜택) 개념을 함께 설명할 수 있어야 합니다.",
            "commonMistakes": [
                {
                    "mistake": "법인세를 'thuế công ty'로 번역",
                    "correction": "'thuế thu nhập doanh nghiệp' 또는 'thuế TNDN'",
                    "explanation": "'thuế công ty'는 비공식 표현이며 법률 문서에서는 정식 명칭을 사용해야 합니다."
                },
                {
                    "mistake": "세율 차이를 설명하지 않고 숫자만 통역",
                    "correction": "누진세 방식인지 단일세율인지 명시",
                    "explanation": "양국의 과세 체계가 다르므로 세율만 말하면 오해 발생 가능성이 높습니다."
                },
                {
                    "mistake": "법인세 신고 주기를 동일하게 가정",
                    "correction": "한국은 연 1회, 베트남은 분기별+연말 확정",
                    "explanation": "신고 일정이 다르므로 계약서나 일정 조율 시 반드시 구분해야 합니다."
                }
            ],
            "examples": [
                {
                    "ko": "우리 회사의 올해 법인세 납부액은 5억원입니다.",
                    "vi": "Số tiền thuế thu nhập doanh nghiệp công ty chúng tôi phải nộp năm nay là 500 triệu won.",
                    "situation": "formal"
                },
                {
                    "ko": "베트남 법인세율이 20%로 단일 적용된다고 들었는데 맞나요?",
                    "vi": "Tôi nghe nói thuế suất thuế TNDN ở Việt Nam là 20% áp dụng đơn, đúng không?",
                    "situation": "informal"
                },
                {
                    "ko": "법인세 감면 혜택을 받으려면 어떤 조건을 충족해야 하나요?",
                    "vi": "Để được hưởng ưu đãi giảm thuế TNDN, cần đáp ứng những điều kiện gì?",
                    "situation": "onsite"
                }
            ],
            "relatedTerms": ["uu-dai-thue", "to-khai-thue", "thue-thu-nhap-ca-nhan"]
        },
        {
            "slug": "thue-thu-nhap-ca-nhan",
            "korean": "소득세",
            "vietnamese": "thuế thu nhập cá nhân",
            "hanja": "所得稅",
            "hanjaReading": "所(바 소) + 得(얻을 득) + 稅(세금 세)",
            "pronunciation": "터에 투 늅 까 년",
            "meaningKo": "개인의 소득에 부과되는 세금으로, 근로소득, 사업소득, 이자소득 등 다양한 소득 유형에 적용됩니다. 통역 시 주의할 점은 베트남의 개인소득세는 최고세율 35%(누진세 7단계)이고 한국은 최고세율 45%(누진세 8단계)라는 차이가 있습니다. 또한 베트남은 외국인 근로자에게도 183일 이상 체류 시 거주자로 간주해 과세하므로, 한국 기업의 베트남 파견 직원 관련 상담에서 자주 다뤄지는 주제입니다. '과세 대상 소득'을 정확히 구분해 통역해야 합니다.",
            "meaningVi": "Là loại thuế đánh vào thu nhập của cá nhân, bao gồm thu nhập từ tiền lương, thu nhập từ kinh doanh, lãi tiền gửi, v.v. Việt Nam áp dụng thuế suất lũy tiến 7 bậc (tối đa 35%), Hàn Quốc áp dụng 8 bậc (tối đa 45%). Người nước ngoài làm việc tại Việt Nam trên 183 ngày sẽ bị coi là cư trú và phải nộp thuế như người Việt Nam.",
            "context": "급여 명세서, 근로 계약서, 세무 상담",
            "culturalNote": "한국은 연말정산 제도가 보편적이지만 베트남은 월별 원천징수 후 연말 확정신고를 하는 방식이 일반적입니다. 또한 베트남은 가족 공제(부양가족 1인당 월 440만동, 2025년 기준) 개념이 있어 한국의 인적공제와 유사하지만 금액 산정 방식이 다릅니다. 통역 시 '공제(khấu trừ)'와 '감면(giảm trừ)'을 혼동하지 않도록 주의해야 합니다.",
            "commonMistakes": [
                {
                    "mistake": "소득세를 'thuế lương'(급여세)로 번역",
                    "correction": "'thuế thu nhập cá nhân' 또는 'thuế TNCN'",
                    "explanation": "'thuế lương'은 근로소득만 의미하므로 사업소득, 이자소득 등을 포괄하지 못합니다."
                },
                {
                    "mistake": "183일 규정을 설명 없이 통역",
                    "correction": "183일 이상 체류 시 거주자로 간주되어 전체 소득에 과세된다고 명시",
                    "explanation": "베트남 세법의 핵심 규정이므로 한국 파견자들에게 반드시 설명해야 합니다."
                },
                {
                    "mistake": "연말정산과 확정신고를 동일하게 표현",
                    "correction": "한국은 '연말정산(quyết toán thuế cuối năm)', 베트남은 '확정신고(kê khai quyết toán)'",
                    "explanation": "절차와 책임 주체가 다르므로 구분 필요합니다."
                }
            ],
            "examples": [
                {
                    "ko": "이번 달 급여에서 소득세 50만원이 원천징수되었습니다.",
                    "vi": "Tháng này, 500,000 won thuế thu nhập cá nhân đã được khấu trừ từ lương.",
                    "situation": "formal"
                },
                {
                    "ko": "베트남에서 6개월 넘게 일하면 소득세를 내야 한다고 들었어요.",
                    "vi": "Tôi nghe nói nếu làm việc ở Việt Nam hơn 6 tháng thì phải nộp thuế TNCN.",
                    "situation": "informal"
                },
                {
                    "ko": "부양가족 공제는 어떻게 신청하나요?",
                    "vi": "Làm thế nào để đăng ký giảm trừ gia cảnh?",
                    "situation": "onsite"
                }
            ],
            "relatedTerms": ["to-khai-thue", "thue-thu-nhap-doanh-nghiep", "uu-dai-thue"]
        },
        {
            "slug": "thue-gia-tri-gia-tang",
            "korean": "부가가치세",
            "vietnamese": "thuế giá trị gia tăng",
            "hanja": "附加價値稅",
            "hanjaReading": "附(붙을 부) + 加(더할 가) + 價(값 가) + 値(값 치) + 稅(세금 세)",
            "pronunciation": "터에 자 찌 자 땅",
            "meaningKo": "상품이나 서비스의 거래 과정에서 발생하는 부가가치에 부과되는 간접세입니다. 통역 시 핵심은 한국의 부가세율 10%와 베트남의 기본세율 10%(일부 품목 5%, 0%)가 같다는 점을 명확히 하되, 면세 품목 범위가 다르다는 점을 강조해야 합니다. 특히 베트남에서는 'VAT'라는 영어 약어를 공식 문서에서도 자주 사용하므로 'thuế GTGT' 또는 'VAT' 모두에 익숙해야 합니다. 또한 베트남은 전자세금계산서(hóa đơn điện tử) 의무화가 한국보다 빠르게 진행되고 있어 관련 용어도 함께 알아야 합니다.",
            "meaningVi": "Là loại thuế gián thu đánh vào giá trị gia tăng phát sinh trong quá trình giao dịch hàng hóa hoặc dịch vụ. Thuế suất VAT cơ bản ở cả Việt Nam và Hàn Quốc đều là 10%, nhưng danh mục hàng hóa miễn thuế khác nhau. Việt Nam đã bắt buộc sử dụng hóa đơn điện tử (e-invoice) từ năm 2022, trong khi Hàn Quốc cũng đang mở rộng hệ thống này.",
            "context": "세금계산서 발행, 수출입 통관, 회계 처리",
            "culturalNote": "한국은 부가세 신고를 분기별(개인사업자)과 월별(법인)로 나누지만, 베트남은 모든 사업자가 월별 신고 원칙입니다. 또한 베트남은 세금계산서를 'hóa đơn đỏ'(붉은 계산서)라고 구어로 부르는 경우가 많은데, 이는 과거 종이 계산서가 붉은색이었던 데서 유래한 표현입니다. 한국 기업이 베트남에 진출할 때 VAT 환급(hoàn thuế GTGT) 절차가 복잡하고 시일이 오래 걸린다는 점을 자주 불만으로 제기하므로, 통역 시 이 부분을 미리 안내하는 것이 좋습니다.",
            "commonMistakes": [
                {
                    "mistake": "부가가치세를 'thuế thêm'(추가세)로 번역",
                    "correction": "'thuế giá trị gia tăng' 또는 'thuế GTGT' 또는 'VAT'",
                    "explanation": "'thuế thêm'은 비공식 표현이며 세법상 정식 명칭이 아닙니다."
                },
                {
                    "mistake": "세금계산서를 'hóa đơn'으로만 표현",
                    "correction": "'hóa đơn GTGT' 또는 'hóa đơn đỏ'(구어)",
                    "explanation": "일반 영수증과 구분하기 위해 'GTGT'를 명시해야 합니다."
                },
                {
                    "mistake": "VAT 환급을 'hoàn tiền'(환불)로 표현",
                    "correction": "'hoàn thuế GTGT'(부가세 환급)",
                    "explanation": "'hoàn tiền'은 일반 환불이고, 세금 환급은 'hoàn thuế'라는 법률 용어를 써야 합니다."
                }
            ],
            "examples": [
                {
                    "ko": "이 제품 가격에는 부가가치세 10%가 포함되어 있습니다.",
                    "vi": "Giá sản phẩm này đã bao gồm thuế GTGT 10%.",
                    "situation": "formal"
                },
                {
                    "ko": "세금계산서 좀 끊어주세요.",
                    "vi": "Cho tôi xin hóa đơn đỏ.",
                    "situation": "informal"
                },
                {
                    "ko": "수출 시 부가세 영세율이 적용되나요?",
                    "vi": "Khi xuất khẩu có được áp dụng thuế suất 0% không?",
                    "situation": "onsite"
                }
            ],
            "relatedTerms": ["hoa-don-thue", "thue-xuat-nhap-khau", "uu-dai-thue"]
        },
        {
            "slug": "thue-xuat-nhap-khau",
            "korean": "관세",
            "vietnamese": "thuế xuất nhập khẩu",
            "hanja": "關稅",
            "hanjaReading": "關(관문 관) + 稅(세금 세)",
            "pronunciation": "터에 쑤엇 늅 커우",
            "meaningKo": "물품을 수출하거나 수입할 때 세관에서 부과하는 세금입니다. 통역 시 핵심은 '수입관세(thuế nhập khẩu)'와 '수출관세(thuế xuất khẩu)'를 명확히 구분하는 것입니다. 한국은 대부분의 수출품에 관세를 부과하지 않지만, 베트남은 일부 원자재(예: 광물, 목재)에 수출관세를 매기므로 이 차이를 설명해야 합니다. 또한 FTA(자유무역협정) 적용 시 관세 감면 혜택이 있으므로 'ưu đãi thuế quan theo FTA'(FTA에 따른 관세 혜택)라는 표현도 함께 알아야 합니다. HS Code(세번) 분류가 관세율 결정에 핵심이므로 'mã HS'라는 용어도 숙지해야 합니다.",
            "meaningVi": "Là loại thuế đánh vào hàng hóa khi xuất khẩu hoặc nhập khẩu qua cửa khẩu. Việt Nam áp dụng thuế xuất khẩu cho một số nguyên liệu thô (khoáng sản, gỗ), trong khi Hàn Quốc hầu như không đánh thuế xuất khẩu. Khi có FTA, hàng hóa được hưởng ưu đãi giảm hoặc miễn thuế nhập khẩu. Mã HS (mã số hàng hóa) là yếu tố quyết định thuế suất.",
            "context": "수출입 통관, 무역 계약서, 관세청 신고",
            "culturalNote": "한국은 관세청 시스템(UNI-PASS)이 전산화되어 있고 통관이 빠른 편이지만, 베트남은 서류 심사가 엄격하고 통관 시간이 오래 걸리는 경우가 많습니다. 특히 베트남은 '붉은선(red lane)' 검사와 '녹색선(green lane)' 검사로 나뉘는데, 붉은선에 걸리면 전수조사를 받으므로 시간이 대폭 지연됩니다. 한국 수출업체들이 이 점을 자주 불만으로 제기하므로 통역 시 '통관 소요 기간'을 미리 안내하는 것이 좋습니다. 또한 베트남은 수입품에 대해 'C/O(원산지증명서, Certificate of Origin)'를 엄격히 요구하므로 이 용어도 함께 알아야 합니다.",
            "commonMistakes": [
                {
                    "mistake": "관세를 'thuế hải quan'으로만 표현",
                    "correction": "수입 시 'thuế nhập khẩu', 수출 시 'thuế xuất khẩu'로 구분",
                    "explanation": "'thuế hải quan'은 세관세(관세청 업무 수수료)를 의미할 수 있어 혼동 가능성이 있습니다."
                },
                {
                    "mistake": "HS Code를 '상품코드'로 번역",
                    "correction": "'mã HS' 또는 'mã số hàng hóa'",
                    "explanation": "HS Code는 국제 표준이므로 'mã HS'로 그대로 쓰는 것이 일반적입니다."
                },
                {
                    "mistake": "FTA 관세 혜택을 '무관세(không thuế)'로만 표현",
                    "correction": "'ưu đãi thuế quan theo FTA'(FTA에 따른 관세 혜택)",
                    "explanation": "FTA에 따라 감면율이 다르므로 '혜택(ưu đãi)'이라는 포괄적 표현이 정확합니다."
                }
            ],
            "examples": [
                {
                    "ko": "이 제품의 수입관세율은 몇 퍼센트인가요?",
                    "vi": "Thuế suất thuế nhập khẩu của sản phẩm này là bao nhiêu phần trăm?",
                    "situation": "formal"
                },
                {
                    "ko": "FTA 적용하면 관세 안 내도 되나요?",
                    "vi": "Nếu áp dụng FTA thì có được miễn thuế nhập khẩu không?",
                    "situation": "informal"
                },
                {
                    "ko": "HS Code 8471.30에 해당하는 제품입니다.",
                    "vi": "Sản phẩm thuộc mã HS 8471.30.",
                    "situation": "onsite"
                }
            ],
            "relatedTerms": ["thue-gia-tri-gia-tang", "to-khai-thue", "uu-dai-thue"]
        },
        {
            "slug": "to-khai-thue",
            "korean": "세금신고서",
            "vietnamese": "tờ khai thuế",
            "hanja": "稅金申告書",
            "hanjaReading": "稅(세금 세) + 金(쇠 금) + 申(펼 신) + 告(알릴 고) + 書(글 서)",
            "pronunciation": "또 카이 터에",
            "meaningKo": "납세자가 세무당국에 제출하는 세금 신고 서류입니다. 통역 시 주의할 점은 베트남에서는 'tờ khai'라는 단어가 '신고서' 일반을 의미하므로 세금 종류를 명시해야 한다는 것입니다. 예를 들어 법인세 신고서는 'tờ khai thuế TNDN', 부가세 신고서는 'tờ khai thuế GTGT'처럼 구체적으로 표현해야 합니다. 또한 한국은 전자신고(홈택스)가 보편화되어 있지만 베트남도 'khai thuế điện tử'(전자세금신고) 시스템이 확대되고 있으므로 이 용어도 함께 알아야 합니다. 신고 기한(hạn nộp)을 놓치면 가산세(tiền phạt chậm nộp)가 부과되므로 이 점도 강조해야 합니다.",
            "meaningVi": "Là văn bản do người nộp thuế nộp cho cơ quan thuế để kê khai nghĩa vụ thuế. Tờ khai thuế cần ghi rõ loại thuế (thuế TNDN, thuế GTGT, v.v.). Hiện nay, Việt Nam đang mở rộng hệ thống khai thuế điện tử, tương tự như HomeTax của Hàn Quốc. Nếu nộp chậm quá hạn sẽ bị phạt tiền chậm nộp.",
            "context": "세무 신고, 회계 감사, 세무 상담",
            "culturalNote": "한국은 세금신고서를 '신고서' 또는 '과세표준신고서'라고 부르지만, 베트남은 'tờ khai'라는 단순한 명칭을 씁니다. 또한 한국은 세무대리인(세무사)이 신고를 대행하는 경우가 많지만, 베트남은 기업 내부 회계팀이 직접 작성하는 경우가 더 흔합니다. 통역 시 '대리 신고(khai thuế ủy quyền)'와 '직접 신고(tự khai thuế)'를 구분할 수 있어야 합니다. 또한 베트남 세무당국은 신고서 오류에 대해 한국보다 엄격하게 제재하므로, 수정신고(khai bổ sung) 절차도 함께 안내하는 것이 좋습니다.",
            "commonMistakes": [
                {
                    "mistake": "세금신고서를 'giấy khai thuế'로 표현",
                    "correction": "'tờ khai thuế'",
                    "explanation": "'giấy khai'는 비공식 표현이고, 'tờ khai'가 법률상 정식 용어입니다."
                },
                {
                    "mistake": "신고 기한을 'ngày cuối'(마지막 날)로만 표현",
                    "correction": "'hạn nộp tờ khai'(신고서 제출 기한)",
                    "explanation": "'hạn nộp'이 법률 용어로 더 정확합니다."
                },
                {
                    "mistake": "전자신고를 'khai thuế online'으로 표현",
                    "correction": "'khai thuế điện tử'",
                    "explanation": "공식 문서에서는 'điện tử'(전자)라는 용어를 씁니다."
                }
            ],
            "examples": [
                {
                    "ko": "이번 분기 세금신고서를 내일까지 제출해야 합니다.",
                    "vi": "Chúng ta phải nộp tờ khai thuế quý này trước ngày mai.",
                    "situation": "formal"
                },
                {
                    "ko": "세금신고서 작성 좀 도와주세요.",
                    "vi": "Giúp tôi điền tờ khai thuế với.",
                    "situation": "informal"
                },
                {
                    "ko": "신고 내용에 오류가 있으면 수정신고를 해야 하나요?",
                    "vi": "Nếu có sai sót trong nội dung khai thuế thì phải khai bổ sung không?",
                    "situation": "onsite"
                }
            ],
            "relatedTerms": ["thue-thu-nhap-doanh-nghiep", "thue-gia-tri-gia-tang", "kiem-tra-thue"]
        },
        {
            "slug": "hoa-don-thue",
            "korean": "세금계산서",
            "vietnamese": "hóa đơn thuế",
            "hanja": "稅金計算書",
            "hanjaReading": "稅(세금 세) + 金(쇠 금) + 計(셀 계) + 算(셈 산) + 書(글 서)",
            "pronunciation": "호아 돈 터에",
            "meaningKo": "부가가치세가 포함된 거래 증빙 서류로, 사업자 간 거래 시 발행하는 세금 영수증입니다. 통역 시 핵심은 베트남에서는 'hóa đơn GTGT'(부가세 계산서) 또는 구어로 'hóa đơn đỏ'(붉은 계산서)라고 부른다는 점을 알아야 합니다. 한국은 전자세금계산서가 의무화되어 있고, 베트남도 2022년부터 전자계산서(hóa đơn điện tử) 의무화가 시행되었으므로 이 부분을 명확히 설명해야 합니다. 특히 베트남은 세금계산서 발행 후 세무당국에 실시간 전송되므로, 허위 발행이나 지연 발행 시 즉시 적발될 수 있다는 점을 강조해야 합니다.",
            "meaningVi": "Là chứng từ giao dịch có kèm thuế GTGT, do người bán phát hành cho người mua trong giao dịch B2B. Ở Việt Nam gọi là 'hóa đơn GTGT' hoặc 'hóa đơn đỏ' (cách nói thông dụng). Từ năm 2022, Việt Nam bắt buộc sử dụng hóa đơn điện tử (hóa đơn điện tử) và dữ liệu được gửi trực tiếp đến cơ quan thuế, giống như hệ thống hóa đơn điện tử của Hàn Quốc.",
            "context": "매입·매출 관리, 부가세 신고, 세무 조사",
            "culturalNote": "한국은 세금계산서를 국세청 홈택스 시스템을 통해 발행하고, 매입자가 승인해야 효력이 발생합니다. 반면 베트남은 판매자가 발행하면 즉시 효력이 생기며, 매입자의 별도 승인 절차가 없습니다. 이 차이 때문에 한국 기업들이 베트남에서 세금계산서를 받았을 때 '승인'을 어디서 하냐고 문의하는 경우가 많으므로, 통역 시 이 점을 미리 설명하는 것이 좋습니다. 또한 베트남은 세금계산서에 QR코드가 인쇄되어 있어 진위 여부를 즉시 확인할 수 있습니다.",
            "commonMistakes": [
                {
                    "mistake": "세금계산서를 'hóa đơn'으로만 표현",
                    "correction": "'hóa đơn GTGT' 또는 'hóa đơn thuế'",
                    "explanation": "일반 영수증(hóa đơn bán lẻ)과 구분하기 위해 'GTGT' 또는 'thuế'를 붙여야 합니다."
                },
                {
                    "mistake": "전자세금계산서를 'e-invoice'로만 표현",
                    "correction": "'hóa đơn điện tử'",
                    "explanation": "베트남 공식 문서에서는 베트남어 'hóa đơn điện tử'를 씁니다."
                },
                {
                    "mistake": "발행을 'gửi'(보내다)로 표현",
                    "correction": "'phát hành'(발행) 또는 'xuất hóa đơn'",
                    "explanation": "'gửi'는 단순 전송이고, 'phát hành'이 법률상 정식 용어입니다."
                }
            ],
            "examples": [
                {
                    "ko": "세금계산서를 발행해주시면 다음 달에 대금을 입금하겠습니다.",
                    "vi": "Nếu anh xuất hóa đơn GTGT cho tôi thì tháng sau tôi sẽ chuyển tiền.",
                    "situation": "formal"
                },
                {
                    "ko": "계산서 좀 끊어주세요.",
                    "vi": "Cho tôi xin hóa đơn đỏ.",
                    "situation": "informal"
                },
                {
                    "ko": "이 세금계산서가 진짜인지 QR코드로 확인할 수 있나요?",
                    "vi": "Có thể kiểm tra hóa đơn này có thật không bằng mã QR không?",
                    "situation": "onsite"
                }
            ],
            "relatedTerms": ["thue-gia-tri-gia-tang", "to-khai-thue", "kiem-tra-thue"]
        },
        {
            "slug": "tron-thue",
            "korean": "탈세",
            "vietnamese": "trốn thuế",
            "hanja": "脫稅",
            "hanjaReading": "脫(벗을 탈) + 稅(세금 세)",
            "pronunciation": "쫀 터에",
            "meaningKo": "고의로 세금을 내지 않거나 축소 신고하는 불법 행위입니다. 통역 시 주의할 점은 '탈세(trốn thuế)'와 '절세(tiết kiệm thuế 또는 tối ưu hóa thuế)', '조세회피(tránh thuế)'를 명확히 구분해야 한다는 것입니다. 탈세는 형사처벌 대상이지만, 절세는 합법적인 세금 절감 방법이고, 조세회피는 법의 허점을 이용한 그레이존 행위입니다. 베트남은 탈세 적발 시 미납세액의 최대 3배까지 벌금을 부과하고, 심한 경우 영업정지나 형사처벌도 가능하므로 이 점을 강조해야 합니다. 또한 베트남 세무당국은 최근 AI 기반 빅데이터 분석으로 탈세를 적발하고 있어, 한국 기업들도 주의가 필요합니다.",
            "meaningVi": "Là hành vi cố tình không nộp thuế hoặc khai giảm thuế một cách bất hợp pháp. Cần phân biệt rõ 'trốn thuế' (bất hợp pháp, bị phạt tù), 'tiết kiệm thuế' (hợp pháp, tối ưu hóa thuế), và 'tránh thuế' (lợi dụng kẽ hở pháp luật, vùng xám). Ở Việt Nam, nếu bị phát hiện trốn thuế, có thể bị phạt tiền lên đến 3 lần số tiền thuế thiếu, thậm chí bị đình chỉ kinh doanh hoặc truy cứu hình sự.",
            "context": "세무 조사, 법률 자문, 언론 보도",
            "culturalNote": "한국은 '탈세'라는 단어에 강한 부정적 이미지가 있어 공개적으로 거론하기 꺼리지만, 베트남은 언론에서 탈세 사건을 자주 보도하고 기업명을 공개하는 경우가 많습니다. 또한 한국은 국세청이 탈세 제보 포상금 제도를 운영하는데, 베트남도 유사한 'tố giác trốn thuế'(탈세 신고) 제도가 있어 일반 시민이 탈세를 신고하면 포상금을 받을 수 있습니다. 통역 시 이 점을 알려주면 한국 기업들이 베트남에서 세무 관리에 더 신중해집니다.",
            "commonMistakes": [
                {
                    "mistake": "탈세를 'không nộp thuế'(세금 안 냄)로만 표현",
                    "correction": "'trốn thuế'",
                    "explanation": "'không nộp thuế'는 단순히 안 내는 것이고, 'trốn thuế'는 고의적 불법 행위를 의미합니다."
                },
                {
                    "mistake": "절세와 탈세를 구분하지 않고 통역",
                    "correction": "절세는 'tiết kiệm thuế' 또는 'tối ưu hóa thuế', 탈세는 'trốn thuế'",
                    "explanation": "법적 성격이 완전히 다르므로 반드시 구분해야 합니다."
                },
                {
                    "mistake": "조세회피를 탈세와 동일하게 표현",
                    "correction": "조세회피는 'tránh thuế', 탈세는 'trốn thuế'",
                    "explanation": "조세회피는 법의 허점 이용(그레이존), 탈세는 명백한 불법입니다."
                }
            ],
            "examples": [
                {
                    "ko": "그 회사는 매출을 축소 신고해서 탈세 혐의로 조사받고 있습니다.",
                    "vi": "Công ty đó đang bị điều tra với cáo buộc trốn thuế do khai giảm doanh thu.",
                    "situation": "formal"
                },
                {
                    "ko": "탈세하다 걸리면 큰일 나요.",
                    "vi": "Bị bắt quả tang trốn thuế là chết.",
                    "situation": "informal"
                },
                {
                    "ko": "합법적인 절세 방법을 찾고 있는데 조언 부탁드립니다.",
                    "vi": "Tôi đang tìm cách tiết kiệm thuế hợp pháp, xin tư vấn giúp.",
                    "situation": "onsite"
                }
            ],
            "relatedTerms": ["kiem-tra-thue", "no-thue", "to-khai-thue"]
        },
        {
            "slug": "uu-dai-thue",
            "korean": "세제혜택",
            "vietnamese": "ưu đãi thuế",
            "hanja": "稅制惠澤",
            "hanjaReading": "稅(세금 세) + 制(만들 제) + 惠(은혜 혜) + 澤(못 택)",
            "pronunciation": "으으 다이 터에",
            "meaningKo": "정부가 특정 산업이나 지역, 기업에 제공하는 세금 감면 또는 면제 혜택입니다. 통역 시 주의할 점은 베트남이 외국인 투자기업(FDI)에 대해 매우 다양한 세제혜택을 제공하므로, 구체적인 혜택 종류를 정확히 설명해야 한다는 것입니다. 예를 들어 '법인세 면제 2년 + 50% 감면 4년(miễn 2 năm, giảm 50% trong 4 năm)', '10% 우대세율(thuế suất ưu đãi 10%)', '투자 지역에 따른 혜택(ưu đãi theo địa bàn đầu tư)' 등 구체적으로 나뉩니다. 한국 투자자들이 베트남 진출 시 가장 관심 있는 부분이므로 관련 용어를 정확히 숙지해야 합니다.",
            "meaningVi": "Là các chính sách giảm hoặc miễn thuế mà chính phủ cung cấp cho một số ngành, khu vực hoặc doanh nghiệp cụ thể. Việt Nam có nhiều ưu đãi thuế dành cho doanh nghiệp FDI (vốn đầu tư nước ngoài), ví dụ: miễn thuế TNDN 2 năm và giảm 50% trong 4 năm tiếp theo, thuế suất ưu đãi 10%, ưu đãi theo địa bàn đầu tư (khu kinh tế, khu công nghiệp). Đây là vấn đề nhà đầu tư Hàn Quốc quan tâm nhất khi vào Việt Nam.",
            "context": "투자 유치, 법인 설립, 세무 상담",
            "culturalNote": "한국은 '조세특례제한법'에 따라 특정 산업(예: 연구개발, 창업)에 세제혜택을 주지만, 베트nam은 '투자법(Luật Đầu tư)'과 '세법(Luật Thuế)'에서 지역과 산업 모두를 고려해 혜택을 부여합니다. 특히 베트남은 '경제특구(khu kinh tế)', '공단(khu công nghiệp)', '하이테크파크(khu công nghệ cao)' 등 지역에 따라 혜택이 크게 다르므로, 통역 시 입지 선정의 중요성을 강조해야 합니다. 또한 베트남은 혜택 신청 절차가 복잡하고 서류가 많아 한국 기업들이 어려워하므로, '신청 절차(thủ tục xin ưu đãi)'도 함께 안내하는 것이 좋습니다.",
            "commonMistakes": [
                {
                    "mistake": "세제혜택을 'giảm thuế'(세금 감면)로만 표현",
                    "correction": "'ưu đãi thuế'(세제혜택 포괄) 또는 구체적으로 'miễn thuế'(면제), 'giảm thuế'(감면)",
                    "explanation": "'ưu đãi thuế'가 면제, 감면, 우대세율 등을 모두 포함하는 포괄적 용어입니다."
                },
                {
                    "mistake": "FDI 기업을 '외국 회사(công ty nước ngoài)'로만 표현",
                    "correction": "'doanh nghiệp FDI' 또는 'doanh nghiệp có vốn đầu tư nước ngoài'",
                    "explanation": "법률 용어로는 'doanh nghiệp FDI'를 써야 정확합니다."
                },
                {
                    "mistake": "우대세율을 '낮은 세율(thuế suất thấp)'로 표현",
                    "correction": "'thuế suất ưu đãi'(우대세율)",
                    "explanation": "'thuế suất ưu đãi'는 법률상 특별히 낮게 적용되는 세율을 의미합니다."
                }
            ],
            "examples": [
                {
                    "ko": "우리 회사는 하이테크파크에 입주해서 법인세 우대세율 10%를 적용받고 있습니다.",
                    "vi": "Công ty chúng tôi đặt tại Khu công nghệ cao nên được hưởng thuế suất ưu đãi 10% thuế TNDN.",
                    "situation": "formal"
                },
                {
                    "ko": "어느 지역에 공장 지으면 세제혜택이 제일 좋아요?",
                    "vi": "Xây nhà máy ở khu vực nào thì được ưu đãi thuế tốt nhất?",
                    "situation": "informal"
                },
                {
                    "ko": "세제혜택 신청하려면 어떤 서류가 필요하나요?",
                    "vi": "Để xin ưu đãi thuế cần những giấy tờ gì?",
                    "situation": "onsite"
                }
            ],
            "relatedTerms": ["thue-thu-nhap-doanh-nghiep", "kiem-tra-thue", "to-khai-thue"]
        },
        {
            "slug": "kiem-tra-thue",
            "korean": "세무조사",
            "vietnamese": "kiểm tra thuế",
            "hanja": "稅務調査",
            "hanjaReading": "稅(세금 세) + 務(일 무) + 調(고를 조) + 査(살필 사)",
            "pronunciation": "끼엠 짜 터에",
            "meaningKo": "세무당국이 납세자의 세금 신고 내역을 검증하기 위해 실시하는 조사입니다. 통역 시 주의할 점은 베트남의 세무조사가 '정기조사(kiểm tra định kỳ)'와 '특별조사(kiểm tra đột xuất)'로 나뉜다는 점을 명확히 해야 합니다. 정기조사는 사전 통보 후 실시되지만, 특별조사는 탈세 혐의가 있을 때 예고 없이 진행되므로 기업들이 매우 긴장합니다. 또한 베트남 세무조사는 한국보다 서류 요구 범위가 넓고 현장 조사 기간이 길어 한국 기업들이 부담스러워하므로, 통역 시 '조사 대비(chuẩn bị kiểm tra thuế)' 방법도 함께 안내하는 것이 좋습니다. 조사 결과 문제가 발견되면 '추징(truy thu thuế)'과 '가산세(tiền phạt chậm nộp)'가 부과됩니다.",
            "meaningVi": "Là hoạt động của cơ quan thuế nhằm kiểm tra tính chính xác của tờ khai thuế và nghĩa vụ nộp thuế của người nộp thuế. Có hai loại: kiểm tra định kỳ (có thông báo trước) và kiểm tra đột xuất (không báo trước, khi có nghi ngờ trốn thuế). Nếu phát hiện sai phạm, doanh nghiệp sẽ bị truy thu thuế (thuế thiếu) và phạt tiền chậm nộp (phạt).",
            "context": "세무 감사, 법률 자문, 회계 관리",
            "culturalNote": "한국은 국세청이 세무조사 사전통지를 하고 조사 범위를 명확히 하지만, 베트남은 특별조사 시 매우 광범위한 자료를 요구하고 조사 기간도 불확실한 경우가 많습니다. 또한 한국은 조사 과정에서 세무대리인(세무사)이 동석할 수 있지만, 베트남은 세무대리인 제도가 덜 발달해 있어 기업 담당자가 직접 대응해야 하는 경우가 많습니다. 통역 시 '세무대리인(đại diện thuế)' 역할을 설명하고, 필요하면 외부 회계법인(công ty kiểm toán) 지원을 받을 것을 제안하는 것이 좋습니다. 베트남 세무조사는 '친절하지 않다'는 인식이 있어 한국 기업들이 매우 스트레스를 받으므로, 통역사는 심리적 완충 역할도 해야 합니다.",
            "commonMistakes": [
                {
                    "mistake": "세무조사를 'điều tra thuế'로 표현",
                    "correction": "'kiểm tra thuế'",
                    "explanation": "'điều tra'는 형사 수사를 의미하고, 'kiểm tra'는 행정 조사(세무조사)를 의미합니다."
                },
                {
                    "mistake": "추징세를 'thuế thêm'(추가 세금)로 표현",
                    "correction": "'truy thu thuế'(추징)",
                    "explanation": "'truy thu'는 과거 납부하지 않은 세금을 소급 징수하는 법률 용어입니다."
                },
                {
                    "mistake": "가산세를 'thuế phạt'로 표현",
                    "correction": "'tiền phạt chậm nộp'(가산세) 또는 'tiền phạt vi phạm'(과태료)",
                    "explanation": "'thuế phạt'는 존재하지 않는 단어이고, 'tiền phạt'(벌금)가 정확합니다."
                }
            ],
            "examples": [
                {
                    "ko": "다음 주에 세무조사가 예정되어 있으니 서류를 미리 준비해주세요.",
                    "vi": "Tuần sau có kiểm tra thuế, xin anh chuẩn bị hồ sơ trước.",
                    "situation": "formal"
                },
                {
                    "ko": "갑자기 세무조사 나왔는데 어떡하죠?",
                    "vi": "Bất ngờ có kiểm tra thuế đột xuất, làm sao đây?",
                    "situation": "informal"
                },
                {
                    "ko": "조사 결과 추징세가 얼마나 나올까요?",
                    "vi": "Kết quả kiểm tra sẽ bị truy thu thuế bao nhiêu?",
                    "situation": "onsite"
                }
            ],
            "relatedTerms": ["tron-thue", "no-thue", "to-khai-thue"]
        },
        {
            "slug": "no-thue",
            "korean": "체납세",
            "vietnamese": "nợ thuế",
            "hanja": "滯納稅",
            "hanjaReading": "滯(막힐 체) + 納(들일 납) + 稅(세금 세)",
            "pronunciation": "너 터에",
            "meaningKo": "납부 기한이 지났는데도 내지 않은 세금입니다. 통역 시 주의할 점은 '체납(nợ thuế)'과 '연체(chậm nộp)'를 구분해야 한다는 것입니다. 연체는 단순히 납부일이 조금 지난 상태이고, 체납은 장기간 미납으로 법적 조치 대상이 됩니다. 베트남은 체납세에 대해 일 0.05%(연 18.25%)의 연체이자(lãi chậm nộp)를 부과하며, 장기 체납 시 은행 계좌 압류(phong tỏa tài khoản), 재산 압류(tạm giữ tài sản), 출국 금지(cấm xuất cảnh) 등의 강력한 조치를 취합니다. 한국 주재원들이 베트남에서 체납세가 있으면 출국이 불가능할 수 있으므로, 통역 시 이 점을 강조해야 합니다.",
            "meaningVi": "Là số thuế đã quá hạn nộp nhưng chưa được nộp. Cần phân biệt 'nợ thuế' (tiền thuế chưa nộp, có thể bị cưỡng chế) và 'chậm nộp' (nộp trễ hạn một chút). Ở Việt Nam, nợ thuế bị tính lãi chậm nộp 0,05%/ngày (tương đương 18,25%/năm). Nếu nợ thuế lâu ngày, có thể bị phong tỏa tài khoản ngân hàng, tạm giữ tài sản, thậm chí cấm xuất cảnh.",
            "context": "세무 상담, 채권 회수, 법적 조치",
            "culturalNote": "한국은 체납세가 있으면 국세청이 '독촉장' 발송 → '압류 예고' → '재산 압류' 순으로 진행하지만, 베트남은 통지 없이 바로 계좌 압류를 하는 경우도 있어 한국 기업들이 당황하는 경우가 많습니다. 또한 베트남은 법인의 체납세가 있으면 대표자 개인도 출국 금지될 수 있으므로, 한국 주재원들은 회사 폐업 또는 귀국 전에 반드시 체납세 여부를 확인해야 합니다. 통역 시 '세금 완납 증명서(giấy xác nhận hoàn thành nghĩa vụ thuế)'를 받아야 출국이 가능하다는 점을 강조해야 합니다.",
            "commonMistakes": [
                {
                    "mistake": "체납세를 'thuế chưa trả'(아직 안 낸 세금)로만 표현",
                    "correction": "'nợ thuế'",
                    "explanation": "'nợ thuế'는 법률 용어로 장기 미납을 의미하고, 'thuế chưa trả'는 단순히 안 낸 것입니다."
                },
                {
                    "mistake": "연체이자를 'lãi suất'(금리)로 표현",
                    "correction": "'lãi chậm nộp'(연체이자)",
                    "explanation": "'lãi suất'는 은행 금리이고, 'lãi chậm nộp'은 세금 연체에 대한 이자입니다."
                },
                {
                    "mistake": "출국 금지를 'không cho đi'로 표현",
                    "correction": "'cấm xuất cảnh'",
                    "explanation": "'cấm xuất cảnh'은 법률 용어로 출입국관리법상 출국 금지 조치입니다."
                }
            ],
            "examples": [
                {
                    "ko": "회사에 체납세가 100만 달러나 쌓여 있습니다.",
                    "vi": "Công ty đang nợ thuế lên đến 1 triệu USD.",
                    "situation": "formal"
                },
                {
                    "ko": "세금 안 내면 출국 못 한다던데 진짜예요?",
                    "vi": "Nghe nói không nộp thuế thì bị cấm xuất cảnh, có thật không?",
                    "situation": "informal"
                },
                {
                    "ko": "체납세를 분할 납부할 수 있나요?",
                    "vi": "Có thể nộp nợ thuế theo từng đợt được không?",
                    "situation": "onsite"
                }
            ],
            "relatedTerms": ["kiem-tra-thue", "tron-thue", "to-khai-thue"]
        }
    ]

    # 5. 중복 필터링
    new_terms_filtered = [t for t in new_terms if t['slug'] not in existing_slugs]

    if not new_terms_filtered:
        print("⚠️  모든 용어가 이미 존재합니다. 추가할 항목이 없습니다.")
        return

    # 6. 데이터 병합
    data.extend(new_terms_filtered)

    # 7. 파일 저장
    with open(file_path, 'w', encoding='utf-8') as f:
        json.dump(data, f, ensure_ascii=False, indent=2)

    print(f"✅ {len(new_terms_filtered)}개 세법/조세 용어 추가 완료!")
    print(f"📂 파일 위치: {file_path}")
    print(f"📊 전체 용어 수: {len(data)}개")

    # 8. 추가된 용어 목록 출력
    print("\n추가된 용어:")
    for i, term in enumerate(new_terms_filtered, 1):
        print(f"{i}. {term['slug']} ({term['korean']} - {term['vietnamese']})")

if __name__ == "__main__":
    main()
