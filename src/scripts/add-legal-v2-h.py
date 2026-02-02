#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Add Financial Law/Banking Law terms to legal.json
Theme: 금융법/은행법 관련 전문용어 10개
Tier S Quality: All fields required, 200+ chars meaningKo, 100+ chars meaningVi/culturalNote
"""

import json
import os

# Get absolute path to legal.json
file_path = os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', 'data', 'terms', 'legal.json')

# Load existing data
with open(file_path, 'r', encoding='utf-8') as f:
    data = json.load(f)  # data is a LIST

# Get existing slugs to prevent duplicates
existing_slugs = {t['slug'] for t in data}

# New terms - Financial Law/Banking Law theme
new_terms = [
    {
        "slug": "ngan-hang-nha-nuoc",
        "korean": "중앙은행",
        "vietnamese": "Ngân hàng Nhà nước",
        "hanja": "中央銀行",
        "hanjaReading": "中(가운데 중) + 央(가운데 앙) + 銀(은 은) + 行(다닐 행)",
        "pronunciation": "응안 항 냐 느억",
        "meaningKo": "한국의 한국은행과 같이 국가 통화정책을 담당하는 최상위 금융기관입니다. 베트남에서는 'Ngân hàng Nhà nước Việt Nam(베트남 국가은행)'이 공식 명칭이며, 통역 시 주의할 점은 베트남 중앙은행이 단순히 통화정책뿐 아니라 상업은행에 대한 직접적인 감독 권한도 가지고 있어 한국보다 더 강력한 권한을 행사한다는 점입니다. 금융 규제 관련 통역에서 양국 중앙은행의 권한 범위 차이를 명확히 설명해야 오해를 방지할 수 있습니다.",
        "meaningVi": "Ngân hàng Nhà nước là cơ quan quản lý tiền tệ cấp cao nhất của quốc gia, chịu trách nhiệm điều hành chính sách tiền tệ, giám sát hệ thống ngân hàng thương mại và duy trì ổn định tài chính. Ở Việt Nam, Ngân hàng Nhà nước có quyền hạn rộng hơn so với ngân hàng trung ương Hàn Quốc trong việc giám sát trực tiếp các ngân hàng thương mại.",
        "context": "금융법, 은행법, 통화정책, 금융감독 관련 회의나 계약서에서 사용",
        "culturalNote": "한국은 한국은행(금융통화위원회)과 금융감독원이 역할을 분담하지만, 베트남은 중앙은행이 통화정책과 금융감독을 모두 담당합니다. 따라서 통역 시 'Ngân hàng Nhà nước'를 단순히 '중앙은행'으로만 번역하면 그 권한 범위가 축소되어 이해될 수 있으므로, 맥락에 따라 '중앙은행 겸 금융감독기관'으로 설명해야 할 때가 있습니다. 또한 베트남에서는 국가 소유 은행의 비중이 여전히 높아 중앙은행의 정책적 영향력이 더 직접적입니다.",
        "commonMistakes": [
            {
                "mistake": "'중앙은행'과 '국가은행'을 혼동하여 번역",
                "correction": "베트남에서는 'Ngân hàng Nhà nước'가 공식 명칭이며, '국가은행'으로 직역하지 말고 '중앙은행'으로 통역",
                "explanation": "베트남어 'Nhà nước'는 '국가'를 의미하지만, 금융 맥락에서는 국제 관례에 따라 'central bank(중앙은행)'으로 번역하는 것이 정확합니다"
            },
            {
                "mistake": "한국 금융감독원의 역할을 중앙은행과 별개로 설명",
                "correction": "베트남에서는 중앙은행이 금융감독 기능도 수행한다고 명시",
                "explanation": "양국 금융 거버넌스 구조가 다르므로, 이를 명확히 하지 않으면 업무 협의 시 혼선이 발생할 수 있습니다"
            },
            {
                "mistake": "'Ngân hàng Trung ương'으로 번역",
                "correction": "'Ngân hàng Nhà nước'가 공식 법률 용어",
                "explanation": "'Trung ương'도 '중앙'을 의미하지만, 베트남 법령에서는 'Nhà nước'를 사용하므로 공식 문서 통역 시 정확한 용어를 써야 합니다"
            }
        ],
        "examples": [
            {
                "ko": "한국은행과 베트남 중앙은행 간 통화스왑 협정을 체결했습니다.",
                "vi": "Ngân hàng Trung ương Hàn Quốc và Ngân hàng Nhà nước Việt Nam đã ký kết thỏa thuận hoán đổi tiền tệ.",
                "situation": "formal"
            },
            {
                "ko": "이 사안은 중앙은행의 승인이 필요합니다.",
                "vi": "Vấn đề này cần sự phê duyệt của Ngân hàng Nhà nước.",
                "situation": "formal"
            },
            {
                "ko": "중앙은행이 기준금리를 0.5%p 인하했습니다.",
                "vi": "Ngân hàng Nhà nước đã giảm lãi suất cơ bản xuống 0,5 điểm phần trăm.",
                "situation": "formal"
            }
        ],
        "relatedTerms": ["ngan-hang-thuong-mai", "lai-suat", "chinh-sach-tien-te"]
    },
    {
        "slug": "ngan-hang-thuong-mai",
        "korean": "상업은행",
        "vietnamese": "ngân hàng thương mại",
        "hanja": "商業銀行",
        "hanjaReading": "商(장사 상) + 業(업 업) + 銀(은 은) + 行(다닐 행)",
        "pronunciation": "응안 항 투엉 마이",
        "meaningKo": "예금 수신과 대출 업무를 주된 영업으로 하는 일반 은행을 의미합니다. 베트남에서는 국영 상업은행(BIDV, Vietinbank, Vietcombank 등)과 민간 상업은행으로 구분되며, 통역 시 주의할 점은 베트남의 4대 국영 상업은행이 여전히 시장의 60% 이상을 점유하고 있어 한국의 민영화된 은행 시스템과 차이가 크다는 것입니다. 금융 투자나 인수합병 통역 시 소유 구조와 정부 영향력을 명확히 설명해야 실수를 방지할 수 있습니다.",
        "meaningVi": "Ngân hàng thương mại là loại hình ngân hàng chủ yếu thực hiện nghiệp vụ huy động vốn và cho vay. Ở Việt Nam, các ngân hàng thương mại nhà nước (như BIDV, Vietinbank, Vietcombank) vẫn chiếm tỷ trọng lớn trên thị trường và có ảnh hưởng chính sách mạnh mẽ, khác với hệ thống ngân hàng tư nhân hóa ở Hàn Quốc.",
        "context": "은행업, 금융 투자, M&A, 금융 규제 관련 계약 및 회의에서 사용",
        "culturalNote": "한국에서는 1990년대 말 금융위기 이후 대부분의 은행이 민영화되었지만, 베트남은 여전히 4대 국영 상업은행(Agribank, BIDV, Vietinbank, Vietcombank)이 시장을 주도하며, 이들은 정부 정책에 따라 정책금융 역할도 수행합니다. 통역 시 '상업은행'이라는 용어가 주는 '순수 민간 영리 은행'이라는 뉘앙스와 베트남 국영 상업은행의 실제 역할 사이에 괴리가 있음을 인지하고, 필요 시 '국영' 또는 '민간' 여부를 명시해야 합니다.",
        "commonMistakes": [
            {
                "mistake": "모든 상업은행을 민간 은행으로 오해",
                "correction": "베트남 상업은행 중 국영과 민간을 구분하여 통역",
                "explanation": "베트남에서는 '국영 상업은행'이 엄연히 존재하며, 이는 정부 정책금융 기능도 수행하므로 한국의 시중은행과 성격이 다릅니다"
            },
            {
                "mistake": "'commercial bank'를 '기업은행'으로 오역",
                "correction": "'상업은행'으로 번역하며, 기업은행은 고유명사 'Industrial Bank of Korea'",
                "explanation": "'commercial'은 '상업적'이라는 뜻이며, 특정 은행 이름이 아닙니다"
            },
            {
                "mistake": "'ngân hàng thương mại'를 '일반은행'으로 번역",
                "correction": "'상업은행'이 정확한 법률 용어",
                "explanation": "은행법상 공식 용어는 '상업은행'이며, '일반은행'은 비공식 표현입니다"
            }
        ],
        "examples": [
            {
                "ko": "이 상업은행은 국영은행입니까, 민간은행입니까?",
                "vi": "Ngân hàng thương mại này là ngân hàng nhà nước hay ngân hàng tư nhân?",
                "situation": "formal"
            },
            {
                "ko": "상업은행 인가를 받기 위한 최소 자본금은 얼마입니까?",
                "vi": "Vốn điều lệ tối thiểu để được cấp phép thành lập ngân hàng thương mại là bao nhiêu?",
                "situation": "formal"
            },
            {
                "ko": "베트남 4대 국영 상업은행이 시장을 장악하고 있습니다.",
                "vi": "Bốn ngân hàng thương mại nhà nước lớn đang chiếm lĩnh thị trường Việt Nam.",
                "situation": "onsite"
            }
        ],
        "relatedTerms": ["ngan-hang-nha-nuoc", "cho-vay", "tin-dung"]
    },
    {
        "slug": "lai-suat",
        "korean": "이자율",
        "vietnamese": "lãi suất",
        "hanja": "利子率",
        "hanjaReading": "利(이로울 리) + 子(자식 자) + 率(비율 률)",
        "pronunciation": "라이 쑤엇",
        "meaningKo": "예금이나 대출 등 금융거래에서 원금에 대한 이자의 비율을 의미합니다. 베트남에서는 'lãi suất cơ bản(기준금리)', 'lãi suất cho vay(대출금리)', 'lãi suất tiền gửi(예금금리)' 등으로 세분화되며, 통역 시 주의할 점은 베트남의 금리가 한국보다 높은 수준(연 5~7%)을 유지하고 있어 금융상품 비교 시 단순 수치 번역만으로는 체감 가치를 전달하기 어렵다는 것입니다. 금융 자문 통역에서는 양국의 금리 환경 차이를 맥락으로 제공해야 합니다.",
        "meaningVi": "Lãi suất là tỷ lệ phần trăm của khoản lãi so với số tiền gốc trong giao dịch tài chính như tiền gửi hoặc cho vay. Việt Nam duy trì mức lãi suất cao hơn Hàn Quốc (khoảng 5-7% mỗi năm) do đặc thù kinh tế và chính sách tiền tệ, nên khi so sánh sản phẩm tài chính giữa hai nước cần chú ý đến sự khác biệt này.",
        "context": "금융계약서, 대출 상담, 투자 자문, 중앙은행 정책 브리핑 등에서 사용",
        "culturalNote": "한국의 기준금리가 3~4%대로 낮은 반면, 베트남은 5~7%대로 상대적으로 높습니다. 이는 베트남이 여전히 고성장 신흥국이며 인플레이션 압력이 크기 때문입니다. 통역 시 단순히 숫자만 전달하면 한국인 투자자가 베트남 금융상품의 '고금리'를 과대평가하거나, 반대로 베트남인이 한국 금융상품의 '저금리'를 매력 없다고 오해할 수 있습니다. 따라서 금리 통역 시에는 '베트남 기준으로는 평균 수준', '한국 대비 약 2배 높은 수준' 같은 맥락 정보를 함께 제공하는 것이 실무적으로 중요합니다.",
        "commonMistakes": [
            {
                "mistake": "'lãi suất'를 '이익률'로 오역",
                "correction": "'이자율' 또는 '금리'로 번역",
                "explanation": "'lãi'는 '이자'와 '이익' 두 가지 뜻이 있지만, 'lãi suất'는 금융 용어로 '이자율'을 의미합니다"
            },
            {
                "mistake": "금리 수치만 통역하고 맥락 설명 생략",
                "correction": "양국 금리 환경 차이를 간단히 덧붙임",
                "explanation": "금리는 절대값보다 상대적 수준이 중요하므로, 투자 결정 시 오해를 방지하려면 맥락 설명이 필수입니다"
            },
            {
                "mistake": "'interest rate'를 '관심도'로 오역",
                "correction": "'이자율' 또는 '금리'",
                "explanation": "'interest'는 문맥에 따라 '관심'과 '이자' 두 가지 의미가 있으므로, 금융 맥락에서는 반드시 '이자'로 이해해야 합니다"
            }
        ],
        "examples": [
            {
                "ko": "현재 기준금리는 연 6.5%입니다.",
                "vi": "Lãi suất cơ bản hiện nay là 6,5% mỗi năm.",
                "situation": "formal"
            },
            {
                "ko": "대출 이자율이 너무 높아서 부담스럽습니다.",
                "vi": "Lãi suất cho vay quá cao nên gánh nặng tài chính lớn.",
                "situation": "informal"
            },
            {
                "ko": "중앙은행이 금리를 인하할 것으로 예상됩니다.",
                "vi": "Dự kiến Ngân hàng Nhà nước sẽ giảm lãi suất.",
                "situation": "formal"
            }
        ],
        "relatedTerms": ["ngan-hang-nha-nuoc", "cho-vay", "tien-gui"]
    },
    {
        "slug": "cho-vay",
        "korean": "대출",
        "vietnamese": "cho vay",
        "hanja": "貸出",
        "hanjaReading": "貸(빌려줄 대) + 出(날 출)",
        "pronunciation": "쩌 바이",
        "meaningKo": "금융기관이 개인이나 기업에게 일정 조건으로 자금을 빌려주는 행위를 의미합니다. 베트남에서는 'cho vay tiêu dùng(소비자 대출)', 'cho vay doanh nghiệp(기업대출)', 'cho vay thế chấp(담보대출)' 등으로 구분되며, 통역 시 주의할 점은 베트남의 대출 심사 기준이 한국보다 까다롭고 담보 비중이 높으며, 특히 외국인의 경우 대출이 제한적이라는 것입니다. 부동산이나 사업 투자 관련 통역에서 대출 가능성에 대한 과도한 기대를 방지하기 위해 현지 대출 제약을 명확히 전달해야 합니다.",
        "meaningVi": "Cho vay là hành vi tổ chức tín dụng cung cấp vốn cho cá nhân hoặc doanh nghiệp theo điều kiện nhất định và thu lãi suất. Ở Việt Nam, tiêu chuẩn xét duyệt cho vay khắt khe hơn Hàn Quốc, tỷ lệ cho vay so với tài sản đảm bảo thấp hơn, và người nước ngoài gặp nhiều hạn chế trong việc vay vốn ngân hàng.",
        "context": "은행 업무, 부동산 거래, 사업 투자, 금융 자문 상담 등에서 사용",
        "culturalNote": "한국에서는 신용대출 비중이 높고 외국인도 일정 소득 증빙 시 대출이 가능하지만, 베트남은 담보대출 중심이며 외국인 대출은 매우 제한적입니다(일부 은행은 외국인 대출 불가). 또한 베트남의 대출 금리가 한국보다 2~3배 높아(연 10~15%) 대출 부담이 훨씬 큽니다. 통역 시 한국인 투자자가 '한국처럼 쉽게 대출받을 수 있다'고 오해하지 않도록 현지 대출 제약과 높은 금리를 명확히 설명해야 하며, 베트남인에게는 한국의 낮은 금리와 신용대출 제도를 설명할 때 '담보 없이도 가능'하다는 점을 강조해야 이해가 빠릅니다.",
        "commonMistakes": [
            {
                "mistake": "'cho vay'를 '빌려주다'로만 번역하여 공식성 부족",
                "correction": "'대출' 또는 '여신'으로 번역하여 금융 전문 용어로 표현",
                "explanation": "'cho vay'는 일상 표현이지만, 금융 맥락에서는 '대출'이라는 공식 용어를 사용해야 합니다"
            },
            {
                "mistake": "한국식 대출 조건을 그대로 설명",
                "correction": "베트남 현지 대출 제약(외국인 제한, 높은 금리, 낮은 LTV)을 명시",
                "explanation": "양국 대출 환경이 크게 다르므로, 오해를 방지하려면 현지 특성을 반드시 전달해야 합니다"
            },
            {
                "mistake": "'loan'을 '차용'으로 오역",
                "correction": "'대출'로 번역",
                "explanation": "'차용'은 개인 간 돈을 빌리는 행위이고, 'loan'은 금융기관의 공식 대출을 의미합니다"
            }
        ],
        "examples": [
            {
                "ko": "이 은행은 외국인에게도 대출을 해줍니까?",
                "vi": "Ngân hàng này có cho người nước ngoài vay không?",
                "situation": "formal"
            },
            {
                "ko": "대출 승인까지 얼마나 걸립니까?",
                "vi": "Mất bao lâu để được phê duyệt cho vay?",
                "situation": "onsite"
            },
            {
                "ko": "담보대출 한도는 부동산 가치의 70%까지입니다.",
                "vi": "Hạn mức cho vay thế chấp lên đến 70% giá trị bất động sản.",
                "situation": "formal"
            }
        ],
        "relatedTerms": ["ngan-hang-thuong-mai", "lai-suat", "tin-dung"]
    },
    {
        "slug": "tin-dung",
        "korean": "신용",
        "vietnamese": "tín dụng",
        "hanja": "信用",
        "hanjaReading": "信(믿을 신) + 用(쓸 용)",
        "pronunciation": "틴 중",
        "meaningKo": "금융거래에서 상환 능력에 대한 믿음을 바탕으로 자금을 빌려주는 것 또는 그러한 신뢰 수준을 의미합니다. 베트남에서는 'tổ chức tín dụng(신용기관, 즉 은행)', 'hạn mức tín dụng(신용한도)', 'lịch sử tín dụng(신용이력)' 등으로 사용되며, 통역 시 주의할 점은 베트남의 신용평가 시스템이 한국만큼 정교하지 않고 개인신용정보 축적이 부족하여 신용대출이 활성화되지 않았다는 것입니다. 금융 투자나 협업 논의 시 양국의 신용평가 인프라 차이를 설명해야 현실적인 기대치를 조율할 수 있습니다.",
        "meaningVi": "Tín dụng là việc cho vay dựa trên niềm tin về khả năng hoàn trả của người đi vay, hoặc mức độ tin cậy tài chính của một cá nhân/doanh nghiệp. Ở Việt Nam, hệ thống đánh giá tín dụng cá nhân chưa phát triển mạnh như Hàn Quốc, nên cho vay tín chấp còn hạn chế và ngân hàng chủ yếu dựa vào tài sản đảm bảo.",
        "context": "은행 대출, 신용카드 발급, 금융상품 가입, 신용평가 관련 논의에서 사용",
        "culturalNote": "한국은 1980년대부터 신용정보 집중 시스템이 발달해 개인신용점수(FICO 스코어와 유사)가 대출 심사의 핵심 기준이 되었지만, 베트남은 2010년대 들어서야 신용정보센터(CIC, Credit Information Center)가 본격 운영되기 시작했고, 아직 신용점수보다는 소득 증빙과 담보가 더 중요합니다. 통역 시 한국인 클라이언트가 '신용만으로 대출 가능'하다고 기대하지 않도록 베트남의 신용평가 미성숙을 설명해야 하며, 베트남인에게는 한국의 발달된 신용사회(신용카드 보급률 90% 이상) 시스템을 설명할 때 '신용등급이 일상생활과 금융거래 전반에 영향을 준다'는 점을 강조해야 합니다.",
        "commonMistakes": [
            {
                "mistake": "'tín dụng'을 '신뢰'로만 번역",
                "correction": "금융 맥락에서는 '신용' 또는 '여신'으로 번역",
                "explanation": "'tín dụng'은 금융 전문용어로 '신용거래' 또는 '대출'을 의미하며, 추상적 '신뢰'와는 다릅니다"
            },
            {
                "mistake": "'tổ chức tín dụng'을 '신용기관'으로만 번역",
                "correction": "'금융기관' 또는 '은행 등 신용기관'으로 설명",
                "explanation": "베트남 법률상 'tổ chức tín dụng'은 은행, 협동조합, 리스사 등 모든 여신기관을 포괄하므로, 맥락에 따라 구체화해야 합니다"
            },
            {
                "mistake": "한국 신용점수 시스템을 그대로 설명",
                "correction": "베트남은 신용점수보다 담보/소득 증빙이 중요하다고 명시",
                "explanation": "양국의 신용평가 인프라 차이가 크므로, 잘못 설명하면 대출 가능성을 과대평가하게 됩니다"
            }
        ],
        "examples": [
            {
                "ko": "신용등급이 낮아서 대출이 거절되었습니다.",
                "vi": "Hạng tín dụng thấp nên khoản vay bị từ chối.",
                "situation": "informal"
            },
            {
                "ko": "이 회사는 신용기관으로 등록되어 있습니까?",
                "vi": "Công ty này có đăng ký là tổ chức tín dụng không?",
                "situation": "formal"
            },
            {
                "ko": "신용카드 한도를 늘리고 싶습니다.",
                "vi": "Tôi muốn tăng hạn mức tín dụng thẻ.",
                "situation": "onsite"
            }
        ],
        "relatedTerms": ["cho-vay", "the-tin-dung", "ngan-hang-thuong-mai"]
    },
    {
        "slug": "the-tin-dung",
        "korean": "신용카드",
        "vietnamese": "thẻ tín dụng",
        "hanja": "信用카드",
        "hanjaReading": "信(믿을 신) + 用(쓸 용) + [카드는 외래어]",
        "pronunciation": "테 틴 중",
        "meaningKo": "은행이 발급하는 후불결제 카드로, 일정 한도 내에서 신용으로 결제하고 나중에 상환하는 금융상품입니다. 베트남에서는 'thẻ ghi nợ(체크카드)'와 구분되며, 통역 시 주의할 점은 베트남의 신용카드 보급률이 한국보다 훨씬 낮고(10% 미만), 현금 문화가 여전히 강하며, 외국인이 베트남에서 신용카드를 발급받기가 매우 어렵다는 것입니다. 금융 서비스 마케팅이나 결제 시스템 논의 시 양국의 카드 문화 차이를 명확히 전달해야 합니다.",
        "meaningVi": "Thẻ tín dụng là thẻ thanh toán do ngân hàng phát hành, cho phép người dùng chi tiêu trong hạn mức tín dụng và trả nợ sau. Ở Việt Nam, tỷ lệ sử dụng thẻ tín dụng thấp hơn nhiều so với Hàn Quốc (dưới 10%), văn hóa thanh toán tiền mặt vẫn phổ biến, và người nước ngoài rất khó được phát hành thẻ tín dụng tại Việt Nam.",
        "context": "은행 상품 안내, 결제 시스템 논의, 핀테크 서비스, 소비자 금융 관련 미팅에서 사용",
        "culturalNote": "한국의 신용카드 보급률은 90% 이상으로 세계 최고 수준이며, 현금 없이 생활하는 것이 일상화되어 있지만, 베트남은 여전히 현금 중심 사회로 신용카드 보급률이 10% 미만입니다. 이는 신용평가 인프라 부족, 낮은 금융 포용성, 그리고 베트남인들이 '빚'에 대한 심리적 거부감이 크기 때문입니다. 통역 시 한국 핀테크 기업이 베트남 시장에 진출할 때 '신용카드 사용이 보편적'이라고 가정하면 시장 진입 전략이 잘못될 수 있으므로, 현지의 낮은 카드 보급률과 현금 선호 문화를 명확히 전달해야 합니다. 반대로 베트남인에게 한국의 카드 문화를 설명할 때는 '한국에서는 현금을 거의 쓰지 않는다'는 점을 강조해야 이해가 빠릅니다.",
        "commonMistakes": [
            {
                "mistake": "'thẻ tín dụng'과 'thẻ ghi nợ(체크카드)'를 혼동",
                "correction": "신용카드는 후불결제, 체크카드는 즉시 계좌 출금이라고 명확히 구분",
                "explanation": "베트남에서는 체크카드가 훨씬 보편적이므로, 신용카드와 체크카드를 구분하지 않으면 혼선이 생깁니다"
            },
            {
                "mistake": "한국처럼 외국인도 쉽게 신용카드를 발급받을 수 있다고 설명",
                "correction": "베트남에서는 외국인 신용카드 발급이 매우 제한적이라고 명시",
                "explanation": "외국인은 베트남 거주증과 소득 증빙이 있어도 대부분 은행에서 신용카드 발급을 거절당합니다"
            },
            {
                "mistake": "'credit card'를 '크레딧 카드'로 음차",
                "correction": "'신용카드'로 번역",
                "explanation": "한국어에서는 '신용카드'가 정식 용어이며, 영어 음차는 비전문적으로 들립니다"
            }
        ],
        "examples": [
            {
                "ko": "신용카드로 결제해도 됩니까?",
                "vi": "Tôi có thể thanh toán bằng thẻ tín dụng không?",
                "situation": "onsite"
            },
            {
                "ko": "외국인도 신용카드를 발급받을 수 있습니까?",
                "vi": "Người nước ngoài có thể làm thẻ tín dụng không?",
                "situation": "formal"
            },
            {
                "ko": "이번 달 신용카드 대금이 300만 동입니다.",
                "vi": "Nợ thẻ tín dụng tháng này là 3 triệu đồng.",
                "situation": "informal"
            }
        ],
        "relatedTerms": ["tin-dung", "ngan-hang-thuong-mai", "the-ghi-no"]
    },
    {
        "slug": "rua-tien",
        "korean": "자금세탁",
        "vietnamese": "rửa tiền",
        "hanja": "資金洗濯",
        "hanjaReading": "資(재물 자) + 金(쇠 금) + 洗(씻을 세) + 濯(씻을 탁)",
        "pronunciation": "르어 띠엔",
        "meaningKo": "불법적으로 취득한 자금의 출처를 숨기기 위해 합법적 거래를 가장하여 자금을 이동시키는 범죄 행위를 의미합니다. 베트남에서는 'chống rửa tiền(자금세탁방지, AML)'이 금융 규제의 핵심 영역이며, 통역 시 주의할 점은 베트남이 FATF(자금세탁방지 국제기구)의 모니터링을 받고 있어 외국 투자자의 자금 출처 심사가 매우 엄격하고, 특히 부동산과 카지노 관련 거래에서 AML 규제가 강화되고 있다는 것입니다. 투자 자문이나 법률 통역 시 자금세탁 리스크를 명확히 설명해야 법적 문제를 예방할 수 있습니다.",
        "meaningVi": "Rửa tiền là hành vi tội phạm nhằm che giấu nguồn gốc bất hợp pháp của tiền bạng bằng cách giả vờ các giao dịch hợp pháp. Việt Nam đang chịu giám sát của FATF (Tổ chức Chống rửa tiền quốc tế), nên các quy định chống rửa tiền (AML) rất nghiêm ngặt, đặc biệt trong lĩnh vực bất động sản và casino, với yêu cầu xác minh nguồn gốc vốn rất chặt chẽ đối với nhà đầu tư nước ngoài.",
        "context": "금융 규제, 은행 컴플라이언스, 외국인 투자 심사, 부동산 거래, 법률 자문에서 사용",
        "culturalNote": "한국은 1990년대 말부터 자금세탁방지(AML) 제도를 정비했고, 금융정보분석원(FIU)이 의심거래를 모니터링하지만, 베트남은 2000년대 후반에야 본격적인 AML 법제를 도입했으며 여전히 현금거래 비중이 높아 자금세탁 리스크가 큽니다. 특히 베트남은 FATF의 '회색 명단(grey list)' 대상국이었던 적이 있어(2021년 해제), 국제 금융거래 시 추가 심사를 받는 경우가 많습니다. 통역 시 외국 투자자가 '단순히 투자금만 송금하면 된다'고 오해하지 않도록, 베트남의 엄격한 자금 출처 증빙 요구(예: 5만 달러 이상 송금 시 세무 서류, 소득 증빙, 은행 거래 내역 등)를 명확히 전달해야 합니다. 또한 '현금 거래는 편리하다'는 인식이 오히려 AML 리스크를 높인다는 점도 설명해야 합니다.",
        "commonMistakes": [
            {
                "mistake": "'rửa tiền'을 '돈 씻기'로 직역",
                "correction": "'자금세탁'이 정확한 법률 용어",
                "explanation": "'money laundering'의 한국어 번역은 '자금세탁'이며, '돈 씻기'는 비전문적 표현입니다"
            },
            {
                "mistake": "AML 규제를 단순한 행정 절차로 설명",
                "correction": "위반 시 형사처벌 대상이며, 투자 승인 거부 사유라고 강조",
                "explanation": "자금세탁방지는 단순한 서류 작업이 아니라 범죄 예방 규제이므로, 경중을 명확히 해야 합니다"
            },
            {
                "mistake": "'chống rửa tiền'을 '반대하는 돈'으로 오역",
                "correction": "'자금세탁방지' 또는 'AML'로 번역",
                "explanation": "'chống'은 '대항하다, 방지하다'는 뜻이므로, 금융 맥락에서는 '방지'로 이해해야 합니다"
            }
        ],
        "examples": [
            {
                "ko": "이 거래는 자금세탁 위험이 있어 심사가 필요합니다.",
                "vi": "Giao dịch này có rủi ro rửa tiền nên cần được xem xét kỹ lưỡng.",
                "situation": "formal"
            },
            {
                "ko": "자금 출처를 증명하는 서류를 제출하십시오.",
                "vi": "Hãy nộp tài liệu chứng minh nguồn gốc tiền.",
                "situation": "formal"
            },
            {
                "ko": "베트남은 자금세탁방지 규제가 강화되고 있습니다.",
                "vi": "Việt Nam đang tăng cường các quy định chống rửa tiền.",
                "situation": "onsite"
            }
        ],
        "relatedTerms": ["ngan-hang-thuong-mai", "dau-tu-nuoc-ngoai", "kiem-soat-von"]
    },
    {
        "slug": "chung-khoan",
        "korean": "증권",
        "vietnamese": "chứng khoán",
        "hanja": "證券",
        "hanjaReading": "證(증거 증) + 券(문서 권)",
        "pronunciation": "충 코안",
        "meaningKo": "주식, 채권 등 재산적 가치를 나타내는 금융 문서를 총칭하는 용어입니다. 베트남에서는 'chứng khoán(증권 일반)', 'cổ phiếu(주식)', 'trái phiếu(채권)'로 구분되며, 통역 시 주의할 점은 베트남 증권시장이 한국보다 변동성이 크고 유동성이 낮으며, 외국인 투자 한도(49% 룰)와 송금 규제가 있어 한국처럼 자유롭게 투자하기 어렵다는 것입니다. 투자 자문이나 자본시장 논의 시 양국 증권시장의 성숙도와 규제 차이를 명확히 전달해야 투자 리스크를 정확히 이해시킬 수 있습니다.",
        "meaningVi": "Chứng khoán là thuật ngữ chung chỉ các loại giấy tờ có giá như cổ phiếu, trái phiếu. Thị trường chứng khoán Việt Nam có biến động cao hơn và thanh khoản thấp hơn so với Hàn Quốc, với giới hạn sở hữu nước ngoài (tối đa 49% tại nhiều công ty) và quy định chặt chẽ về chuyển tiền ra nước ngoài, nên nhà đầu tư nước ngoài gặp nhiều hạn chế hơn.",
        "context": "증권 투자, 자본시장 논의, IPO, M&A, 금융 자문 미팅에서 사용",
        "culturalNote": "한국 증권시장(KOSPI, KOSDAQ)은 1980년대부터 발달해 시가총액이 2,000조 원을 넘고 외국인 투자자 비중이 30~40%에 달하지만, 베트남 증권시장(HOSE, HNX)은 2000년에 개장해 역사가 짧고 시가총액도 한국의 10분의 1 수준이며, 개인 투자자 비중이 압도적으로 높아 변동성이 매우 큽니다. 또한 베트남은 주요 기업에 외국인 지분 한도(49%)가 있어, 한국 투자자가 '마음대로 사고팔 수 있다'고 오해하지 않도록 명확히 설명해야 합니다. 통역 시 베트남 증권을 '신흥시장(emerging market)'으로 표현하면서 높은 수익 가능성과 동시에 높은 리스크를 함께 전달하는 것이 중요합니다.",
        "commonMistakes": [
            {
                "mistake": "'chứng khoán'을 '주식'으로만 번역",
                "correction": "'증권'으로 번역하고, 주식은 'cổ phiếu'라고 구분",
                "explanation": "'chứng khoán'은 주식, 채권, 펀드 등을 포괄하는 상위 개념입니다"
            },
            {
                "mistake": "한국 증권시장 수준으로 베트남 시장을 설명",
                "correction": "베트남은 신흥시장으로 변동성이 크고 외국인 투자 한도가 있다고 명시",
                "explanation": "양국 증권시장의 성숙도와 규제가 크게 다르므로, 동일선상에서 비교하면 오해가 발생합니다"
            },
            {
                "mistake": "'securities'를 '보안'으로 오역",
                "correction": "'증권'으로 번역",
                "explanation": "'security'는 IT 맥락에서는 '보안'이지만, 금융 맥락에서는 '증권'입니다"
            }
        ],
        "examples": [
            {
                "ko": "베트남 증권시장에 투자하고 싶습니다.",
                "vi": "Tôi muốn đầu tư vào thị trường chứng khoán Việt Nam.",
                "situation": "formal"
            },
            {
                "ko": "외국인 투자 한도는 얼마입니까?",
                "vi": "Hạn mức đầu tư nước ngoài là bao nhiêu?",
                "situation": "formal"
            },
            {
                "ko": "이 회사의 주식은 유동성이 낮습니다.",
                "vi": "Cổ phiếu công ty này có thanh khoản thấp.",
                "situation": "onsite"
            }
        ],
        "relatedTerms": ["co-phieu", "trai-phieu", "thi-truong-von"]
    },
    {
        "slug": "ngan-hang-dau-tu",
        "korean": "투자은행",
        "vietnamese": "ngân hàng đầu tư",
        "hanja": "投資銀行",
        "hanjaReading": "投(던질 투) + 資(재물 자) + 銀(은 은) + 行(다닐 행)",
        "pronunciation": "응안 항 더우 뜨",
        "meaningKo": "기업의 자금 조달, M&A 자문, 증권 인수 등 자본시장 업무를 주로 하는 금융기관을 의미합니다. 베트남에서는 'công ty chứng khoán(증권회사)'가 유사한 역할을 하며, 통역 시 주의할 점은 베트남에는 미국식 대형 투자은행(Goldman Sachs, JP Morgan 같은)이 없고, 대부분 증권회사 수준의 소규모 기관이거나 상업은행의 투자금융 부서 형태라는 것입니다. M&A나 IPO 자문 관련 통역에서 '투자은행'이라는 용어가 주는 '대형 글로벌 금융기관'이라는 이미지와 베트남 현지 증권회사의 실제 규모/역량 사이의 괴리를 명확히 전달해야 합니다.",
        "meaningVi": "Ngân hàng đầu tư là tổ chức tài chính chuyên về huy động vốn cho doanh nghiệp, tư vấn M&A, bảo lãnh phát hành chứng khoán. Ở Việt Nam, vai trò này chủ yếu do các công ty chứng khoán đảm nhận, với quy mô và năng lực nhỏ hơn nhiều so với các ngân hàng đầu tư lớn ở Mỹ hoặc Hàn Quốc, thường là bộ phận tài chính đầu tư của ngân hàng thương mại.",
        "context": "M&A, IPO, 기업 공개, 자본시장 자문, 금융 구조조정 논의에서 사용",
        "culturalNote": "한국에는 미래에셋증권, NH투자증권 같은 대형 투자은행급 증권사가 있고, 삼성증권, KB증권 등도 투자은행 업무(IB)를 활발히 하지만, 베트남은 증권회사들이 대부분 소규모이고 투자은행 업무 경험이 부족합니다. 베트남의 대형 M&A나 IPO는 주로 외국계 투자은행(씨티, HSBC 등)이나 한국계 증권사 베트남 지사가 주관하며, 현지 증권사는 보조 역할에 그치는 경우가 많습니다. 통역 시 한국 기업이 '현지 투자은행에 자문을 맡기겠다'고 할 때, 베트남 증권사의 실제 IB 역량을 솔직히 평가해 전달하지 않으면 자문 품질에 대한 기대와 현실 사이에 큰 괴리가 발생할 수 있습니다.",
        "commonMistakes": [
            {
                "mistake": "'ngân hàng đầu tư'를 일반 은행으로 오해",
                "correction": "'투자은행'은 상업은행과 다르며, 주로 기업금융 자문을 한다고 설명",
                "explanation": "'ngân hàng'이라는 단어 때문에 예금/대출 은행으로 오해할 수 있으므로, IB의 특수성을 명확히 해야 합니다"
            },
            {
                "mistake": "베트남 증권사를 한국 수준의 IB로 소개",
                "correction": "베트남 증권사는 IB 경험이 제한적이며, 대형 딜은 외국계가 주도한다고 설명",
                "explanation": "투자은행 역량을 과대평가하면 자문 품질 기대치가 어긋나 실망을 초래합니다"
            },
            {
                "mistake": "'investment bank'를 '투자 은행'으로 띄어쓰기",
                "correction": "'투자은행'으로 붙여 쓰는 것이 금융 용어",
                "explanation": "한국 금융업계에서는 '투자은행'을 하나의 합성어로 취급합니다"
            }
        ],
        "examples": [
            {
                "ko": "이번 M&A 자문은 어느 투자은행이 맡았습니까?",
                "vi": "Ngân hàng đầu tư nào đảm nhận tư vấn M&A này?",
                "situation": "formal"
            },
            {
                "ko": "투자은행의 수수료가 너무 비쌉니다.",
                "vi": "Phí của ngân hàng đầu tư quá cao.",
                "situation": "informal"
            },
            {
                "ko": "현지 증권사와 외국계 투자은행 중 어느 쪽을 선택하시겠습니까?",
                "vi": "Quý vị chọn công ty chứng khoán địa phương hay ngân hàng đầu tư nước ngoài?",
                "situation": "formal"
            }
        ],
        "relatedTerms": ["chung-khoan", "M&A", "IPO"]
    },
    {
        "slug": "bao-hiem-tien-gui",
        "korean": "예금보험",
        "vietnamese": "bảo hiểm tiền gửi",
        "hanja": "預金保險",
        "hanjaReading": "預(맡길 예) + 金(쇠 금) + 保(지킬 보) + 險(험할 험)",
        "pronunciation": "바오 히엠 띠엔 귀",
        "meaningKo": "은행이 파산할 경우 예금자를 보호하기 위해 일정 한도까지 예금을 보장하는 국가 제도를 의미합니다. 베트남에서는 DIV(Deposit Insurance of Vietnam)가 운영하며 보장 한도는 1인당 7,500만 동(약 300만 원)으로 한국의 5,000만 원보다 낮습니다. 통역 시 주의할 점은 베트남의 예금보험 한도가 낮고, 국영 은행에 대한 암묵적 국가 보증이 더 강해서 베트남인들이 '국영 은행이 더 안전하다'고 믿는 경향이 있으며, 외화 예금은 보호 범위가 제한적이라는 것입니다. 금융 자문이나 예금 상담 통역 시 예금보험 한도와 적용 조건을 명확히 설명해야 예금자 보호에 대한 오해를 방지할 수 있습니다.",
        "meaningVi": "Bảo hiểm tiền gửi là chế độ quốc gia bảo vệ người gửi tiền khi ngân hàng phá sản, với hạn mức bảo hiểm tại Việt Nam là 75 triệu đồng/người (khoảng 3 triệu won Hàn Quốc), thấp hơn mức 50 triệu won ở Hàn Quốc. Tiền gửi ngoại tệ có phạm vi bảo vệ hạn chế, và người Việt thường tin tưởng ngân hàng nhà nước hơn do có sự bảo lãnh ngầm của chính phủ.",
        "context": "은행 예금 상담, 금융 안전성 논의, 파산 리스크 설명, 투자 자문에서 사용",
        "culturalNote": "한국은 1996년 예금자보호법을 제정해 예금보험공사가 1인당 5,000만 원까지 보호하며, 대부분의 은행이 민영화되어 예금보험이 실질적인 안전장치로 작동하지만, 베트남은 2000년대 들어서야 예금보험 제도를 도입했고, 보장 한도가 낮으며(7,500만 동, 약 300만 원), 무엇보다 국영 은행에 대한 '정부가 망하게 내버려두지 않을 것'이라는 암묵적 신뢰가 강해 민간 은행보다 국영 은행 예금을 선호합니다. 통역 시 한국 기업이나 개인이 베트남 은행에 예금할 때 '한국처럼 5,000만 원까지 보호된다'고 오해하지 않도록 낮은 보장 한도를 명확히 전달하고, 외화 예금은 보호 범위가 더 제한적이라는 점도 설명해야 합니다. 반대로 베트남인에게 한국의 높은 예금보험 한도를 설명할 때는 '국영/민영 관계없이 모두 동일하게 보호된다'는 점을 강조해야 합니다.",
        "commonMistakes": [
            {
                "mistake": "베트남 예금보험 한도를 한국 수준으로 설명",
                "correction": "베트남은 7,500만 동(약 300만 원)으로 한국의 10분의 1 이하라고 명시",
                "explanation": "예금보험 한도 차이를 정확히 전달하지 않으면 예금 안전성에 대한 오해가 발생합니다"
            },
            {
                "mistake": "'bảo hiểm'을 '보험'으로만 번역하여 일반 보험으로 오해",
                "correction": "'예금보험'이라고 명확히 번역하고, 국가 제도임을 설명",
                "explanation": "'bảo hiểm'은 일반 보험과 예금보험 모두를 의미하므로, 맥락을 명확히 해야 합니다"
            },
            {
                "mistake": "외화 예금도 동일하게 보호된다고 설명",
                "correction": "베트남은 외화 예금 보호가 제한적이며, 동화(VND) 예금이 우선이라고 명시",
                "explanation": "베트남 예금보험은 주로 동화 예금을 대상으로 하며, 외화 예금은 별도 조건이 있습니다"
            }
        ],
        "examples": [
            {
                "ko": "이 은행이 망하면 제 예금은 어떻게 됩니까?",
                "vi": "Nếu ngân hàng này phá sản thì tiền gửi của tôi sẽ ra sao?",
                "situation": "informal"
            },
            {
                "ko": "예금보험 한도가 얼마입니까?",
                "vi": "Hạn mức bảo hiểm tiền gửi là bao nhiêu?",
                "situation": "formal"
            },
            {
                "ko": "외화 예금도 예금보험으로 보호됩니까?",
                "vi": "Tiền gửi ngoại tệ có được bảo hiểm tiền gửi bảo vệ không?",
                "situation": "formal"
            }
        ],
        "relatedTerms": ["ngan-hang-thuong-mai", "tien-gui", "ngan-hang-nha-nuoc"]
    }
]

# Filter out duplicates
new_terms_filtered = [t for t in new_terms if t['slug'] not in existing_slugs]

print(f"Found {len(existing_slugs)} existing terms")
print(f"Adding {len(new_terms_filtered)} new terms (filtered {len(new_terms) - len(new_terms_filtered)} duplicates)")

# Extend data list
data.extend(new_terms_filtered)

# Write back to file
with open(file_path, 'w', encoding='utf-8') as f:
    json.dump(data, f, ensure_ascii=False, indent=2)

print(f"✅ Successfully added {len(new_terms_filtered)} financial law terms to legal.json")
print(f"Total terms now: {len(data)}")
