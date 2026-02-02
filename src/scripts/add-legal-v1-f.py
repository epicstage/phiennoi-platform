#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
부동산법/토지법 전문용어 추가 스크립트
Real Estate Law/Land Law Terms Addition Script

Tier S 품질 기준:
- meaningKo: 200자 이상, 통역 팁 필수
- meaningVi: 100자 이상, 성조 포함
- culturalNote: 100자 이상, 한베 문화 차이
- commonMistakes: 3개 이상 (객체 형식)
- examples: 3개 이상 (situation 포함)
- relatedTerms: 3개 이상
"""

import json
import os

def add_real_estate_law_terms():
    # 1. 파일 경로 설정 (상대 경로)
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

    # 3. 기존 slug 세트 생성
    existing_slugs = {t['slug'] for t in data}

    # 4. 새 용어 정의 (10개)
    new_terms = [
        {
            "slug": "quyen-su-dung-dat",
            "korean": "토지사용권",
            "vietnamese": "quyền sử dụng đất",
            "hanja": "土地使用權",
            "hanjaReading": "土(흙 토) + 地(땅 지) + 使(부릴 사) + 用(쓸 용) + 權(권세 권)",
            "pronunciation": "꾸옌 쓰 중 닷",
            "meaningKo": "베트남에서 토지의 소유권은 국가에 있으며, 개인이나 법인은 토지를 사용할 수 있는 권리만 보유합니다. 통역 시 주의할 점은 한국의 '소유권'과 베트남의 '사용권'을 명확히 구분해야 한다는 것입니다. 한국 투자자들이 베트남 부동산 매매 시 '토지를 산다'고 표현하지만, 실제로는 '토지사용권을 양도받는 것'이므로 이를 정확히 통역해야 오해를 방지할 수 있습니다. 계약서 통역 시 특히 사용 기한(50년, 70년 등)과 갱신 조건을 명확히 전달해야 합니다.",
            "meaningVi": "Quyền sử dụng đất là quyền được Nhà nước giao hoặc cho thuê để sử dụng đất trong một thời hạn nhất định. Đất đai thuộc sở hữu toàn dân do Nhà nước đại diện chủ sở hữu. Người sử dụng đất có các quyền như chuyển nhượng, cho thuê, thừa kế, thế chấp quyền sử dụng đất theo quy định của pháp luật.",
            "context": "부동산 거래, 투자 계약, 토지 관련 법률 자문",
            "culturalNote": "한국에서는 토지 소유권(所有權)이 개인에게 완전히 귀속되지만, 베트남은 사회주의 국가로서 모든 토지는 국가 소유입니다. 베트남인들은 '토지를 산다(mua đất)'고 일상적으로 표현하지만, 법적으로는 '토지사용권을 양도받는 것(nhận chuyển nhượng quyền sử dụng đất)'입니다. 이러한 차이를 이해하지 못하면 한국 기업의 베트남 투자 시 큰 법적 리스크가 발생할 수 있습니다.",
            "commonMistakes": [
                {
                    "mistake": "토지 소유권",
                    "correction": "토지사용권",
                    "explanation": "베트남에서 개인은 토지를 소유할 수 없고 사용권만 가질 수 있음"
                },
                {
                    "mistake": "quyền sở hữu đất",
                    "correction": "quyền sử dụng đất",
                    "explanation": "소유권(sở hữu)은 국가에 있고, 개인은 사용권(sử dụng)만 보유"
                },
                {
                    "mistake": "영구 소유",
                    "correction": "50년/70년 사용권 (갱신 가능)",
                    "explanation": "베트남 토지사용권은 기한이 정해져 있으며 자동 연장되지 않음"
                }
            ],
            "examples": [
                {
                    "ko": "이 토지의 사용권은 2050년까지 유효합니다.",
                    "vi": "Quyền sử dụng đất này có hiệu lực đến năm 2050.",
                    "situation": "formal"
                },
                {
                    "ko": "토지사용권 양도 계약서를 작성하겠습니다.",
                    "vi": "Chúng tôi sẽ lập hợp đồng chuyển nhượng quyền sử dụng đất.",
                    "situation": "formal"
                },
                {
                    "ko": "외국인도 베트남에서 토지사용권을 취득할 수 있나요?",
                    "vi": "Người nước ngoài có thể nhận quyền sử dụng đất tại Việt Nam không?",
                    "situation": "informal"
                }
            ],
            "relatedTerms": ["so-do", "giay-chung-nhan-quyen-su-dung-dat", "chuyen-nhuong-dat"]
        },
        {
            "slug": "so-do",
            "korean": "레드북",
            "vietnamese": "sổ đỏ",
            "hanja": None,
            "hanjaReading": None,
            "pronunciation": "쏘 도",
            "meaningKo": "베트남의 토지사용권증명서를 일상적으로 부르는 통칭으로, 빨간색 표지 때문에 '레드북'이라 불립니다. 통역 시 주의할 점은 한국의 '등기부등본'과 유사하지만 베트남에서는 이 문서가 토지 거래의 핵심 증빙서류라는 점입니다. 한국인들이 '등기증'이라고 오해하는 경우가 많은데, 실제로는 토지사용권과 주택 소유권을 함께 증명하는 통합 문서입니다. 부동산 거래 통역 시 'sổ đỏ'를 '레드북' 또는 '토지사용권증명서'로 번역하며, 원본 확인이 필수임을 강조해야 합니다.",
            "meaningVi": "Sổ đỏ là tên gọi thông dụng của Giấy chứng nhận quyền sử dụng đất, quyền sở hữu nhà ở và tài sản khác gắn liền với đất. Đây là chứng thư pháp lý quan trọng nhất trong giao dịch bất động sản tại Việt Nam, được cấp bởi Sở Tài nguyên và Môi trường. Sổ đỏ có màu đỏ, ghi đầy đủ thông tin về diện tích, vị trí, mục đích sử dụng đất và chủ sử dụng.",
            "context": "부동산 매매, 담보 대출, 상속 절차",
            "culturalNote": "베트남에서 'sổ đỏ'는 부동산 거래의 신뢰도를 결정하는 가장 중요한 문서입니다. 한국의 등기부등본처럼 온라인으로 즉시 확인할 수 없고, 원본 실물을 직접 확인해야 합니다. 위조 레드북 사기가 빈번하므로, 베트남 부동산 투자 시 반드시 관할 토지자원환경국(Sở Tài nguyên và Môi trường)에서 진위를 확인해야 합니다. 레드북이 없는 부동산은 거래가 불가능하거나 법적 분쟁 위험이 큽니다.",
            "commonMistakes": [
                {
                    "mistake": "등기증",
                    "correction": "레드북 (토지사용권증명서)",
                    "explanation": "한국의 등기 개념과 다르며, 레드북은 실물 증서 형태"
                },
                {
                    "mistake": "giấy tờ nhà đất",
                    "correction": "sổ đỏ 또는 giấy chứng nhận",
                    "explanation": "공식 명칭을 사용해야 법적 효력을 명확히 함"
                },
                {
                    "mistake": "복사본도 괜찮다",
                    "correction": "원본 확인 필수",
                    "explanation": "베트남 부동산 거래는 반드시 원본 레드북으로 진행해야 함"
                }
            ],
            "examples": [
                {
                    "ko": "레드북 원본을 확인해야 합니다.",
                    "vi": "Cần kiểm tra sổ đỏ gốc.",
                    "situation": "formal"
                },
                {
                    "ko": "이 집은 레드북이 있나요?",
                    "vi": "Nhà này có sổ đỏ không?",
                    "situation": "informal"
                },
                {
                    "ko": "레드북 명의가 누구입니까?",
                    "vi": "Sổ đỏ đứng tên ai?",
                    "situation": "formal"
                }
            ],
            "relatedTerms": ["quyen-su-dung-dat", "giay-chung-nhan-quyen-su-dung-dat", "dang-ky-dat-dai"]
        },
        {
            "slug": "giay-chung-nhan-quyen-su-dung-dat",
            "korean": "토지사용권증명서",
            "vietnamese": "giấy chứng nhận quyền sử dụng đất",
            "hanja": "土地使用權證明書",
            "hanjaReading": "土(흙 토) + 地(땅 지) + 使(부릴 사) + 用(쓸 용) + 權(권세 권) + 證(증거 증) + 明(밝을 명) + 書(글 서)",
            "pronunciation": "저이 쯩 년 꾸옌 쓰 중 닷",
            "meaningKo": "'레드북(sổ đỏ)'의 정식 명칭으로, 베트남 정부가 발급하는 토지사용권과 주택 소유권을 증명하는 공식 문서입니다. 통역 시 주의할 점은 이 증명서가 한국의 '등기부등본' 역할을 하지만, 베트남에서는 실물 원본 확인이 필수라는 점입니다. 한국 투자자들에게 이 문서가 없으면 법적으로 토지 거래가 불가능하며, 은행 담보 대출도 받을 수 없다는 점을 명확히 설명해야 합니다. 계약서 통역 시 '증명서 원본 제시'와 '관할청 확인' 조항이 포함되어야 함을 강조해야 합니다.",
            "meaningVi": "Giấy chứng nhận quyền sử dụng đất, quyền sở hữu nhà ở và tài sản khác gắn liền với đất là văn bản pháp lý do cơ quan nhà nước có thẩm quyền cấp, xác nhận quyền hợp pháp của người sử dụng đất. Đây là căn cứ pháp lý để thực hiện các giao dịch như chuyển nhượng, cho thuê, thế chấp, thừa kế. Giấy chứng nhận phải ghi đầy đủ thông tin về diện tích, vị trí, mục đích sử dụng, thời hạn sử dụng và chủ sử dụng đất.",
            "context": "부동산 계약, 법률 자문, 투자 실사",
            "culturalNote": "베트남의 토지사용권증명서는 2015년 이후 토지와 건물을 통합한 '핑크북'으로 변경되었지만, 여전히 많은 사람들이 '레드북'이라는 통칭을 사용합니다. 한국과 달리 베트남은 증명서 발급 절차가 복잡하고 시간이 오래 걸리며(3~6개월), 지방에 따라 행정 처리 속도가 다릅니다. 외국인이 베트남에서 부동산을 구입할 경우, 이 증명서를 받을 수 있는지 사전에 확인해야 하며, 일부 지역은 외국인에게 발급을 제한합니다.",
            "commonMistakes": [
                {
                    "mistake": "토지등기증",
                    "correction": "토지사용권증명서",
                    "explanation": "한국의 '등기' 개념과 다르며, 베트남은 증명서 형태"
                },
                {
                    "mistake": "giấy tờ đất",
                    "correction": "giấy chứng nhận quyền sử dụng đất",
                    "explanation": "공식 법률 용어를 사용해야 계약서에서 혼란 방지"
                },
                {
                    "mistake": "온라인으로 확인 가능",
                    "correction": "관할청 방문 원본 확인 필수",
                    "explanation": "베트남은 아직 온라인 등기 시스템이 완전하지 않음"
                }
            ],
            "examples": [
                {
                    "ko": "토지사용권증명서는 언제 발급됩니까?",
                    "vi": "Giấy chứng nhận quyền sử dụng đất được cấp khi nào?",
                    "situation": "formal"
                },
                {
                    "ko": "증명서에 기재된 면적과 실제 면적이 다릅니다.",
                    "vi": "Diện tích ghi trong giấy chứng nhận khác với diện tích thực tế.",
                    "situation": "onsite"
                },
                {
                    "ko": "이 증명서는 진짜인지 관할청에서 확인하세요.",
                    "vi": "Hãy xác minh giấy chứng nhận này tại cơ quan có thẩm quyền.",
                    "situation": "formal"
                }
            ],
            "relatedTerms": ["so-do", "quyen-su-dung-dat", "dang-ky-dat-dai"]
        },
        {
            "slug": "chuyen-nhuong-dat",
            "korean": "토지양도",
            "vietnamese": "chuyển nhượng đất",
            "hanja": "土地讓渡",
            "hanjaReading": "土(흙 토) + 地(땅 지) + 讓(사양할 양) + 渡(건널 도)",
            "pronunciation": "쭈옌 냐잉 닷",
            "meaningKo": "토지사용권을 다른 사람에게 유상 또는 무상으로 이전하는 법률 행위입니다. 통역 시 주의할 점은 한국의 '토지 매매'와 개념이 다르다는 것입니다. 베트남에서는 소유권이 아닌 사용권을 양도하는 것이므로, 계약서 통역 시 '토지를 판다/산다'가 아닌 '토지사용권을 양도한다/양수한다'로 정확히 표현해야 합니다. 특히 외국인 투자자에게는 양도 가능 여부, 사용 기한, 갱신 조건을 명확히 설명해야 하며, 정부 승인이 필요한 경우가 많다는 점을 강조해야 합니다.",
            "meaningVi": "Chuyển nhượng đất là việc chuyển quyền sử dụng đất từ người này sang người khác thông qua giao dịch mua bán, tặng cho, hoặc các hình thức khác theo quy định của pháp luật. Người chuyển nhượng phải có giấy chứng nhận quyền sử dụng đất hợp pháp. Sau khi chuyển nhượng, bên nhận chuyển nhượng phải làm thủ tục sang tên và được cấp giấy chứng nhận mới. Một số trường hợp chuyển nhượng đất cần xin phép cơ quan nhà nước.",
            "context": "부동산 거래, 투자 계약, 상속 절차",
            "culturalNote": "베트남에서 토지 양도는 복잡한 행정 절차를 거쳐야 하며, 지방에 따라 규정이 다를 수 있습니다. 한국처럼 당일 등기가 불가능하고, 보통 1~3개월이 소요됩니다. 특히 외국인이나 외국 기업은 양도 가능 여부가 제한되며, 일부 지역이나 용도의 토지는 정부 승인이 필요합니다. 한국 투자자들이 베트남 부동산 매매 시 양도세(최대 2%)와 등록비를 고려해야 하며, 계약 후 명의 변경 기한을 엄수해야 합니다.",
            "commonMistakes": [
                {
                    "mistake": "토지 매매",
                    "correction": "토지사용권 양도",
                    "explanation": "베트남에서는 사용권을 거래하는 것이지 소유권을 매매하는 것이 아님"
                },
                {
                    "mistake": "mua bán đất",
                    "correction": "chuyển nhượng quyền sử dụng đất",
                    "explanation": "법률 문서에서는 정확한 용어 사용 필수"
                },
                {
                    "mistake": "즉시 명의 변경 가능",
                    "correction": "행정 절차 1~3개월 소요",
                    "explanation": "베트남은 한국처럼 당일 등기가 불가능"
                }
            ],
            "examples": [
                {
                    "ko": "토지사용권 양도 계약을 체결하겠습니다.",
                    "vi": "Chúng tôi sẽ ký hợp đồng chuyển nhượng quyền sử dụng đất.",
                    "situation": "formal"
                },
                {
                    "ko": "이 토지는 외국인에게 양도할 수 있습니까?",
                    "vi": "Mảnh đất này có thể chuyển nhượng cho người nước ngoài không?",
                    "situation": "formal"
                },
                {
                    "ko": "양도 절차는 얼마나 걸리나요?",
                    "vi": "Thủ tục chuyển nhượng mất bao lâu?",
                    "situation": "informal"
                }
            ],
            "relatedTerms": ["quyen-su-dung-dat", "so-do", "dang-ky-dat-dai"]
        },
        {
            "slug": "thu-hoi-dat",
            "korean": "토지수용",
            "vietnamese": "thu hồi đất",
            "hanja": "土地收用",
            "hanjaReading": "土(흙 토) + 地(땅 지) + 收(거둘 수) + 用(쓸 용)",
            "pronunciation": "투 호이 닷",
            "meaningKo": "국가가 공공 목적을 위해 개인이나 조직의 토지사용권을 강제로 회수하는 행정 행위입니다. 통역 시 주의할 점은 한국의 '토지수용'과 유사하지만, 베트님에서는 보상 기준과 절차가 다르다는 것입니다. 특히 한국 투자자들에게 베트남 정부가 공공 이익을 위해 언제든지 토지를 회수할 수 있으며, 보상이 시장 가격보다 낮을 수 있다는 점을 명확히 설명해야 합니다. 통역 시 '수용'이라는 표현보다 '회수'가 베트남 법 개념에 더 가깝다는 점을 인지하고, 보상금 산정 기준과 이의 제기 절차를 정확히 전달해야 합니다.",
            "meaningVi": "Thu hồi đất là việc Nhà nước lấy lại quyền sử dụng đất của tổ chức, cá nhân khi có nhu cầu sử dụng đất vì mục đích quốc phòng, an ninh, lợi ích quốc gia, lợi ích công cộng hoặc do thực hiện dự án phát triển kinh tế - xã hội. Khi thu hồi đất, Nhà nước phải có quyết định thu hồi, thông báo trước cho người sử dụng đất và thực hiện bồi thường, hỗ trợ, tái định cư theo quy định.",
            "context": "공공 사업, 인프라 개발, 투자 리스크 평가",
            "culturalNote": "베트남에서 토지수용은 빈번하게 발생하며, 특히 도시 개발과 인프라 프로젝트에서 자주 일어납니다. 한국과 달리 보상 기준이 시장 가격보다 낮은 경우가 많아 분쟁이 잦습니다. 외국 투자자가 베트남에서 부동산 투자 시 해당 지역의 토지이용계획(quy hoạch)을 사전에 확인해야 하며, 수용 위험을 계약서에 반영해야 합니다. 일부 지역에서는 주민들이 보상에 불만을 품고 집단 항의를 하는 경우도 있으므로, 투자 실사 시 이러한 사회적 리스크도 고려해야 합니다.",
            "commonMistakes": [
                {
                    "mistake": "토지 몰수",
                    "correction": "토지수용 (회수)",
                    "explanation": "'몰수'는 처벌 의미가 있으나, '수용'은 공공 목적의 보상 있는 회수"
                },
                {
                    "mistake": "tịch thu đất",
                    "correction": "thu hồi đất",
                    "explanation": "'tịch thu'는 몰수(무보상), 'thu hồi'는 보상 있는 회수"
                },
                {
                    "mistake": "시장 가격 보상",
                    "correction": "정부 산정 보상 기준",
                    "explanation": "베트남 토지수용 보상은 시장 가격보다 낮을 수 있음"
                }
            ],
            "examples": [
                {
                    "ko": "이 지역은 공항 건설을 위해 토지수용 예정입니다.",
                    "vi": "Khu vực này sẽ bị thu hồi đất để xây dựng sân bay.",
                    "situation": "formal"
                },
                {
                    "ko": "토지수용 보상금은 어떻게 산정됩니까?",
                    "vi": "Tiền bồi thường thu hồi đất được tính như thế nào?",
                    "situation": "formal"
                },
                {
                    "ko": "수용 결정에 이의가 있으면 어디에 제기하나요?",
                    "vi": "Nếu không đồng ý với quyết định thu hồi, khiếu nại ở đâu?",
                    "situation": "informal"
                }
            ],
            "relatedTerms": ["den-bu-giai-phong-mat-bang", "quy-hoach-su-dung-dat", "quyen-su-dung-dat"]
        },
        {
            "slug": "den-bu-giai-phong-mat-bang",
            "korean": "토지보상",
            "vietnamese": "đền bù giải phóng mặt bằng",
            "hanja": "土地補償",
            "hanjaReading": "土(흙 토) + 地(땅 지) + 補(기울 보) + 償(갚을 상)",
            "pronunciation": "덴 부 저이 퐁 맛 방",
            "meaningKo": "국가가 토지를 수용할 때 토지사용자에게 지급하는 보상금과 지원금을 의미합니다. 통역 시 주의할 점은 '보상(đền bù)'과 '지원(hỗ trợ)', '재정착(tái định cư)'이 각각 다른 항목이라는 것입니다. 한국 투자자들에게 베트남의 보상 기준은 한국보다 복잡하며, 토지 가격, 지상물(나무, 건물 등), 이주비, 생계 지원 등이 별도로 산정된다는 점을 명확히 설명해야 합니다. 계약 통역 시 보상 기준이 지방 정부마다 다를 수 있으며, 시장 가격과 괴리가 크다는 점을 반드시 전달해야 분쟁을 예방할 수 있습니다.",
            "meaningVi": "Đền bù giải phóng mặt bằng là việc Nhà nước chi trả tiền bồi thường, hỗ trợ cho người có đất bị thu hồi để thực hiện dự án. Bồi thường bao gồm giá trị quyền sử dụng đất, tài sản trên đất (nhà cửa, cây trồng, vật kiến trúc), chi phí di chuyển, ổn định đời sống và sản xuất. Giá đất bồi thường được tính theo bảng giá đất do Ủy ban nhân dân cấp tỉnh quy định, thường thấp hơn giá thị trường. Người dân có quyền khiếu nại nếu không đồng ý với mức bồi thường.",
            "context": "공공 프로젝트, 인프라 개발, 분쟁 조정",
            "culturalNote": "베트남에서 토지보상 분쟁은 매우 흔하며, 보상 기준이 시장 가격의 50~70% 수준인 경우가 많습니다. 한국 투자자가 베트남에서 공장 부지를 확보할 때, 정부가 토지를 수용하여 제공하는 경우 기존 주민들의 보상 문제가 프로젝트 지연의 주요 원인이 됩니다. 일부 지역에서는 주민들이 보상에 불만을 품고 공사를 방해하거나 소송을 제기하는 경우도 있으므로, 투자 계약 시 '보상 완료 후 부지 인도' 조건을 명시해야 합니다.",
            "commonMistakes": [
                {
                    "mistake": "보상금",
                    "correction": "보상금 + 지원금 + 이주비",
                    "explanation": "베트남은 보상 항목이 여러 개로 나뉘어 있음"
                },
                {
                    "mistake": "đền bù",
                    "correction": "đền bù giải phóng mặt bằng",
                    "explanation": "정확한 법률 용어 사용 필요"
                },
                {
                    "mistake": "시장 가격 보상",
                    "correction": "정부 고시 가격 기준",
                    "explanation": "실제 보상액은 시장 가격보다 낮음"
                }
            ],
            "examples": [
                {
                    "ko": "토지보상 협상이 완료되지 않아 프로젝트가 지연되고 있습니다.",
                    "vi": "Dự án đang bị trì hoãn vì chưa hoàn thành đàm phán đền bù giải phóng mặt bằng.",
                    "situation": "formal"
                },
                {
                    "ko": "보상 기준은 어떻게 되나요?",
                    "vi": "Mức đền bù được tính như thế nào?",
                    "situation": "informal"
                },
                {
                    "ko": "이주민들에게 재정착 지원금도 지급됩니까?",
                    "vi": "Người dân phải di dời có được hỗ trợ tái định cư không?",
                    "situation": "formal"
                }
            ],
            "relatedTerms": ["thu-hoi-dat", "quy-hoach-su-dung-dat", "quyen-su-dung-dat"]
        },
        {
            "slug": "quy-hoach-su-dung-dat",
            "korean": "토지이용계획",
            "vietnamese": "quy hoạch sử dụng đất",
            "hanja": "土地利用計劃",
            "hanjaReading": "土(흙 토) + 地(땅 지) + 利(이로울 리) + 用(쓸 용) + 計(셀 계) + 劃(그을 획)",
            "pronunciation": "꾸이 호악 쓰 중 닷",
            "meaningKo": "국가가 일정 기간 동안 토지의 용도와 이용 방향을 정한 계획으로, 한국의 '도시계획' 또는 '국토이용계획'과 유사합니다. 통역 시 주의할 점은 베트남의 토지이용계획은 중앙 정부와 지방 정부가 층위별로 수립하며, 계획이 변경되면 기존 토지사용권자에게 큰 영향을 미칠 수 있다는 것입니다. 한국 투자자에게 부동산 투자 전 반드시 해당 지역의 토지이용계획을 확인해야 하며, 계획 변경 시 토지수용이나 용도 제한이 발생할 수 있다는 리스크를 명확히 설명해야 합니다.",
            "meaningVi": "Quy hoạch sử dụng đất là việc phân bổ, sắp xếp các loại đất cho các mục đích sử dung khác nhau trong một khoảng thời gian nhất định (thường 10 năm) trên địa bàn cả nước, tỉnh, huyện. Quy hoạch xác định diện tích các loại đất như đất nông nghiệp, đất ở, đất công nghiệp, đất công cộng. Người dân và doanh nghiệp cần tuân thủ quy hoạch khi sử dụng đất, không được tự ý chuyển đổi mục đích sử dụng đất trái quy hoạch.",
            "context": "투자 실사, 부동산 개발, 공공 사업",
            "culturalNote": "베트남에서 토지이용계획은 투자 결정의 핵심 요소입니다. 한국과 달리 계획이 자주 변경되며, 변경 시 공개 절차가 미흡한 경우가 많아 투자자가 예상치 못한 손실을 입을 수 있습니다. 특히 농업용지를 공업용지나 주거용지로 전환하려면 계획 변경 승인이 필요하며, 이 과정에서 1~2년이 소요될 수 있습니다. 한국 기업이 베트남에서 공장 부지를 매입할 때, 토지이용계획상 공업용지인지 반드시 확인해야 하며, 계획 외 지역이면 개발이 불가능할 수 있습니다.",
            "commonMistakes": [
                {
                    "mistake": "도시계획",
                    "correction": "토지이용계획",
                    "explanation": "도시계획은 도시만 포함하지만, 토지이용계획은 전국 모든 토지 포함"
                },
                {
                    "mistake": "quy hoạch đô thị",
                    "correction": "quy hoạch sử dụng đất",
                    "explanation": "도시계획(quy hoạch đô thị)은 토지이용계획의 일부"
                },
                {
                    "mistake": "계획은 변경 불가",
                    "correction": "계획은 5~10년마다 재조정 가능",
                    "explanation": "베트남 토지이용계획은 정기적으로 변경됨"
                }
            ],
            "examples": [
                {
                    "ko": "이 지역은 토지이용계획상 공업용지로 지정되어 있습니까?",
                    "vi": "Khu vực này được quy hoạch là đất công nghiệp không?",
                    "situation": "formal"
                },
                {
                    "ko": "토지이용계획이 변경되면 우리 공장은 어떻게 됩니까?",
                    "vi": "Nếu quy hoạch sử dụng đất thay đổi, nhà máy của chúng tôi sẽ như thế nào?",
                    "situation": "formal"
                },
                {
                    "ko": "계획 변경은 어디서 확인하나요?",
                    "vi": "Thay đổi quy hoạch được tra cứu ở đâu?",
                    "situation": "informal"
                }
            ],
            "relatedTerms": ["muc-dich-su-dung-dat", "thu-hoi-dat", "quyen-su-dung-dat"]
        },
        {
            "slug": "muc-dich-su-dung-dat",
            "korean": "토지용도",
            "vietnamese": "mục đích sử dụng đất",
            "hanja": "土地用途",
            "hanjaReading": "土(흙 토) + 地(땅 지) + 用(쓸 용) + 途(길 도)",
            "pronunciation": "목 딕 쓰 중 닷",
            "meaningKo": "토지가 어떤 목적으로 사용될 수 있는지를 법적으로 정한 것으로, 농업용지, 주거용지, 공업용지, 상업용지 등으로 구분됩니다. 통역 시 주의할 점은 베트남에서는 토지용도 변경이 매우 까다롭고 정부 승인이 필요하다는 것입니다. 한국 투자자들이 베트남 부동산을 매입할 때 레드북에 기재된 토지용도를 반드시 확인해야 하며, 용도와 다르게 사용할 경우 법적 제재를 받을 수 있다는 점을 명확히 설명해야 합니다. 특히 농업용지를 공장 부지로 전환하려면 용도 변경 승인을 받아야 하며, 이 과정에서 수개월에서 수년이 걸릴 수 있습니다.",
            "meaningVi": "Mục đích sử dụng đất là việc xác định đất được sử dụng vào việc gì, theo nhóm đất nào như đất nông nghiệp (trồng cây hàng năm, lâu năm, nuôi trồng thủy sản), đất phi nông nghiệp (đất ở, đất sản xuất kinh doanh, đất công cộng). Mỗi thửa đất chỉ được sử dụng đúng mục đích ghi trong giấy chứng nhận. Nếu muốn thay đổi mục đích sử dụng đất phải xin phép cơ quan nhà nước có thẩm quyền và có thể phải nộp thêm tiền sử dụng đất.",
            "context": "부동산 거래, 투자 계약, 건축 허가",
            "culturalNote": "베트남에서 토지용도 위반은 심각한 법적 문제를 야기할 수 있습니다. 한국과 달리 베트남은 농업용지를 다른 용도로 전환하는 것이 매우 제한적이며, 특히 쌀 재배 농지(đất lúa)는 전환이 거의 불가능합니다. 외국 투자자가 베트남에서 공장을 건설하려면 토지용도가 '공업용지' 또는 '생산경영용지'인지 확인해야 하며, 농업용지를 매입한 후 용도 변경을 시도하면 승인이 거부되거나 장기간 지연될 수 있습니다.",
            "commonMistakes": [
                {
                    "mistake": "토지 구역",
                    "correction": "토지용도",
                    "explanation": "용도는 사용 목적, 구역은 지리적 구분"
                },
                {
                    "mistake": "loại đất",
                    "correction": "mục đích sử dụng đất",
                    "explanation": "'loại đất'는 토지 유형, 'mục đích sử dụng đất'는 사용 목적"
                },
                {
                    "mistake": "용도 변경은 쉽다",
                    "correction": "용도 변경은 정부 승인 필수, 장기간 소요",
                    "explanation": "베트남은 토지용도 변경이 매우 까다로움"
                }
            ],
            "examples": [
                {
                    "ko": "이 토지의 용도는 무엇입니까?",
                    "vi": "Mục đích sử dụng đất của thửa đất này là gì?",
                    "situation": "formal"
                },
                {
                    "ko": "농업용지를 공업용지로 변경할 수 있나요?",
                    "vi": "Có thể chuyển đổi đất nông nghiệp sang đất công nghiệp không?",
                    "situation": "formal"
                },
                {
                    "ko": "용도와 다르게 사용하면 어떤 처벌을 받나요?",
                    "vi": "Nếu sử dụng đất sai mục đích sẽ bị xử phạt như thế nào?",
                    "situation": "informal"
                }
            ],
            "relatedTerms": ["quy-hoach-su-dung-dat", "quyen-su-dung-dat", "so-do"]
        },
        {
            "slug": "hop-dong-thue-dat",
            "korean": "토지임대계약",
            "vietnamese": "hợp đồng thuê đất",
            "hanja": "土地賃貸契約",
            "hanjaReading": "土(흙 토) + 地(땅 지) + 賃(품팔 임) + 貸(빌릴 대) + 契(맺을 계) + 約(맺을 약)",
            "pronunciation": "헙 동 투에 닷",
            "meaningKo": "토지사용권자가 다른 사람에게 토지를 일정 기간 빌려주고 임대료를 받는 계약입니다. 통역 시 주의할 점은 베트남에서는 '국가로부터 토지를 임대'하는 경우와 '개인으로부터 토지사용권을 임대'하는 경우가 다르다는 것입니다. 한국 투자자들에게 베트남에서 공장 부지를 확보할 때 국가 임대와 민간 임대의 차이를 명확히 설명해야 하며, 특히 외국 기업은 장기 토지 임대(50년)가 가능하지만 갱신 조건을 반드시 계약서에 명시해야 한다는 점을 강조해야 합니다.",
            "meaningVi": "Hợp đồng thuê đất là thỏa thuận giữa bên cho thuê (có thể là Nhà nước hoặc cá nhân có quyền sử dụng đất hợp pháp) và bên thuê về việc sử dụng đất trong một thời gian nhất định với mức tiền thuê đất theo thỏa thuận hoặc theo quy định. Hợp đồng thuê đất với Nhà nước thường áp dụng cho dự án đầu tư, doanh nghiệp nước ngoài, với thời hạn thuê tối đa 50 năm (có thể gia hạn). Hợp đồng thuê đất với cá nhân thường ngắn hạn hơn.",
            "context": "외국인 투자, 공장 부지 확보, 상업 시설 임대",
            "culturalNote": "베트남에서 외국 기업은 토지를 직접 매입할 수 없고 국가로부터 장기 임대하는 방식으로 부지를 확보합니다. 한국과 달리 토지 임대료가 매년 조정될 수 있으며, 지방 정부마다 임대료 산정 기준이 다릅니다. 한국 기업이 베트남에서 공장을 건설할 때, 토지 임대 기간과 갱신 조건을 명확히 해야 하며, 계약 종료 시 지상물(건물) 처리 방법을 사전에 협의해야 합니다. 일부 지역은 외국인 토지 임대를 제한하므로, 투자 전 해당 지역 규정을 확인해야 합니다.",
            "commonMistakes": [
                {
                    "mistake": "토지 임차",
                    "correction": "토지임대계약",
                    "explanation": "'임차'는 빌리는 행위, '임대계약'은 계약 자체를 의미"
                },
                {
                    "mistake": "thuê đất",
                    "correction": "hợp đồng thuê đất",
                    "explanation": "계약서 번역 시 정확한 법률 용어 사용 필요"
                },
                {
                    "mistake": "영구 임대",
                    "correction": "최대 50년 임대 (갱신 가능)",
                    "explanation": "베트남 토지 임대는 기한이 정해져 있음"
                }
            ],
            "examples": [
                {
                    "ko": "국가와 50년 토지임대계약을 체결했습니다.",
                    "vi": "Chúng tôi đã ký hợp đồng thuê đất 50 năm với Nhà nước.",
                    "situation": "formal"
                },
                {
                    "ko": "임대 기간 종료 후 갱신할 수 있나요?",
                    "vi": "Sau khi hết hạn thuê, có thể gia hạn không?",
                    "situation": "formal"
                },
                {
                    "ko": "임대료는 매년 얼마나 오르나요?",
                    "vi": "Tiền thuê đất tăng bao nhiêu mỗi năm?",
                    "situation": "informal"
                }
            ],
            "relatedTerms": ["quyen-su-dung-dat", "chuyen-nhuong-dat", "so-do"]
        },
        {
            "slug": "dang-ky-dat-dai",
            "korean": "토지등기",
            "vietnamese": "đăng ký đất đai",
            "hanja": "土地登記",
            "hanjaReading": "土(흙 토) + 地(땅 지) + 登(오를 등) + 記(기록할 기)",
            "pronunciation": "당 끼 닷 다이",
            "meaningKo": "토지사용권을 법적으로 공식 등록하는 절차로, 한국의 '부동산 등기'와 유사합니다. 통역 시 주의할 점은 베트남에서는 등기가 완료되어야 비로소 토지사용권증명서(레드북)가 발급된다는 것입니다. 한국 투자자들에게 베트남 부동산 거래 시 등기 절차가 한국보다 복잡하고 시간이 오래 걸린다(3~6개월)는 점을 명확히 설명해야 하며, 등기가 완료되기 전까지는 법적으로 완전한 권리를 행사할 수 없다는 점을 강조해야 합니다. 계약서 통역 시 '등기 완료 기한'과 '등기 비용 부담' 조항이 반드시 포함되어야 합니다.",
            "meaningVi": "Đăng ký đất đai là việc cơ quan nhà nước có thẩm quyền ghi chép, lưu giữ thông tin về thửa đất, quyền sử dụng đất, quyền sở hữu nhà ở và tài sản khác gắn liền với đất vào hệ thống cơ sở dữ liệu quốc gia về đất đai, đồng thời cấp giấy chứng nhận quyền sử dụng đất cho chủ sử dụng đất. Đăng ký đất đai giúp bảo vệ quyền và lợi ích hợp pháp của người sử dụng đất, tạo cơ sở pháp lý cho các giao dịch đất đai.",
            "context": "부동산 거래, 명의 변경, 투자 절차",
            "culturalNote": "베트남의 토지등기 시스템은 한국보다 덜 발달되어 있으며, 온라인으로 즉시 확인할 수 없는 경우가 많습니다. 한국 투자자들이 베트남 부동산을 매입한 후 등기 절차에서 예상치 못한 문제(기존 채권 압류, 소유권 분쟁 등)가 발견되는 경우가 많으므로, 계약 전 철저한 실사(due diligence)가 필수입니다. 특히 지방 정부의 행정 처리 속도가 느리고, 서류 미비로 등기가 지연되는 경우가 흔하므로, 투자 일정에 여유를 두어야 합니다.",
            "commonMistakes": [
                {
                    "mistake": "등기부등본",
                    "correction": "토지등기 (등록)",
                    "explanation": "'등기부등본'은 등기 내용 증명서, '등기'는 등록 행위 자체"
                },
                {
                    "mistake": "sổ đỏ",
                    "correction": "đăng ký đất đai",
                    "explanation": "'sổ đỏ'는 결과물, 'đăng ký'는 등록 절차"
                },
                {
                    "mistake": "당일 등기 가능",
                    "correction": "등기 완료까지 3~6개월 소요",
                    "explanation": "베트남은 한국처럼 즉시 등기가 불가능"
                }
            ],
            "examples": [
                {
                    "ko": "토지등기를 완료하는 데 얼마나 걸립니까?",
                    "vi": "Đăng ký đất đai mất bao lâu để hoàn tất?",
                    "situation": "formal"
                },
                {
                    "ko": "등기 서류는 무엇이 필요한가요?",
                    "vi": "Cần những giấy tờ gì để đăng ký đất đai?",
                    "situation": "informal"
                },
                {
                    "ko": "등기 비용은 누가 부담합니까?",
                    "vi": "Chi phí đăng ký đất đai do bên nào chịu?",
                    "situation": "formal"
                }
            ],
            "relatedTerms": ["so-do", "giay-chung-nhan-quyen-su-dung-dat", "chuyen-nhuong-dat"]
        }
    ]

    # 5. 중복 필터링
    filtered_terms = [t for t in new_terms if t['slug'] not in existing_slugs]

    print(f"✅ 기존 용어: {len(existing_slugs)}개")
    print(f"✅ 신규 용어: {len(filtered_terms)}개")
    print(f"⚠️  중복 제외: {len(new_terms) - len(filtered_terms)}개")

    # 6. 데이터 추가
    data.extend(filtered_terms)

    # 7. 파일 저장
    with open(file_path, 'w', encoding='utf-8') as f:
        json.dump(data, f, ensure_ascii=False, indent=2)

    print(f"\n✅ 저장 완료: {file_path}")
    print(f"📊 총 용어 수: {len(data)}개")

    # 8. 추가된 용어 목록 출력
    if filtered_terms:
        print("\n📋 추가된 용어:")
        for term in filtered_terms:
            print(f"  - {term['slug']}: {term['korean']} ({term['vietnamese']})")

if __name__ == "__main__":
    add_real_estate_law_terms()
