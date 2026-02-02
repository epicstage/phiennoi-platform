#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
형사절차 심화 용어 추가 스크립트 (Advanced Criminal Procedure Terms)
Tier S 품질 기준 준수
"""

import json
import os

def main():
    # 1. 파일 경로 설정
    file_path = os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', 'data', 'terms', 'legal.json')

    # 2. 기존 데이터 로드
    with open(file_path, 'r', encoding='utf-8') as f:
        data = json.load(f)  # data is a LIST

    # 3. 기존 slug 추출
    existing_slugs = {t['slug'] for t in data}

    # 4. 새 용어 정의
    new_terms = [
        {
            "slug": "tam-giu",
            "korean": "구류",
            "vietnamese": "tạm giữ",
            "hanja": "拘留",
            "hanjaReading": "拘(가둘 구) + 留(머물 류)",
            "pronunciation": "따잠 쥬",
            "meaningKo": "형사절차에서 피의자를 일정 기간 동안 경찰서나 구치소에 임시로 억류하는 강제처분. 베트남에서는 최대 72시간까지 가능하며, 검찰의 승인이 필요함. 한국의 체포와 유사하지만 기간이 더 짧음. 통역 시 '구속'과 혼동하지 말 것 - tạm giữ는 단기간의 임시 억류이고, tạm giam(구속)은 장기간의 구금을 의미. 베트nam 법에서는 tạm giữ 기간을 엄격히 제한하므로 기간 관련 통역 시 특히 주의.",
            "meaningVi": "Biện pháp cưỡng chế trong tố tụng hình sự, tạm thời giam giữ người bị nghi ngờ phạm tội tại trụ sở công an hoặc nhà tạm giữ trong thời gian nhất định. Ở Việt Nam, thời gian tạm giữ tối đa là 72 giờ và cần sự phê duyệt của viện kiểm sát. Khác với tạm giam (giam giữ dài hạn), tạm giữ chỉ áp dụng trong thời gian ngắn để điều tra ban đầu.",
            "context": "형사절차, 경찰 조사, 피의자 권리",
            "culturalNote": "베트남의 tạm giữ(구류)는 한국의 체포에 해당하며 최대 72시간으로 제한됩니다. 한국은 48시간 이내 구속영장을 청구해야 하는 반면, 베트남은 검찰 승인 하에 연장 가능. 베트남에서는 tạm giữ와 tạm giam(구속)을 명확히 구분하며, 법적 효력과 기간이 다릅니다. 통역사는 두 용어를 절대 혼용해서는 안 되며, 의뢰인에게 차이점을 명확히 설명해야 합니다.",
            "commonMistakes": [
                {
                    "mistake": "tạm giữ를 '구속'으로 번역",
                    "correction": "tạm giữ는 '구류' 또는 '체포'",
                    "explanation": "tạm giam이 구속이고, tạm giữ는 단기 억류입니다"
                },
                {
                    "mistake": "thời gian tạm giữ를 '구속 기간'으로 통역",
                    "correction": "'구류 기간' 또는 '체포 기간'",
                    "explanation": "법적 의미가 완전히 달라 권리 행사에 영향을 줍니다"
                },
                {
                    "mistake": "72시간을 '3일'로 통역",
                    "correction": "'72시간' 또는 '최대 3일'로 정확히 통역",
                    "explanation": "법적 기간은 시간 단위로 계산되므로 정확성이 중요합니다"
                }
            ],
            "examples": [
                {
                    "ko": "피의자를 tạm giữ 조치했습니다.",
                    "vi": "Người bị nghi ngờ đã bị tạm giữ.",
                    "situation": "formal"
                },
                {
                    "ko": "구류 기간이 72시간을 초과할 수 없습니다.",
                    "vi": "Thời gian tạm giữ không được vượt quá 72 giờ.",
                    "situation": "formal"
                },
                {
                    "ko": "검찰 승인 없이 구류를 연장할 수 없어요.",
                    "vi": "Không thể gia hạn tạm giữ mà không có sự phê duyệt của viện kiểm sát.",
                    "situation": "onsite"
                }
            ],
            "relatedTerms": ["tạm giam (구속)", "bắt giữ (체포)", "lệnh bắt (체포영장)", "viện kiểm sát (검찰)"]
        },
        {
            "slug": "tai-ngoai",
            "korean": "보석",
            "vietnamese": "tại ngoại",
            "hanja": "在外",
            "hanjaReading": "在(있을 재) + 外(밖 외)",
            "pronunciation": "따이 응오아이",
            "meaningKo": "형사피고인이나 피의자를 구속하지 않고 석방하여 외부에서 재판을 받게 하는 제도. 베트남에서는 보석금 납부나 보증인 제공이 필요하며, 법원의 허가를 받아야 함. 한국의 보석제도와 유사하지만 절차가 다름. 통역 시 '석방'과 구분 필요 - tại ngoại는 조건부 석방이고 tha tự(석방)는 무조건 석방. 베트남에서는 중죄 사건의 경우 tại ngoại 허가가 매우 제한적이므로, 의뢰인의 기대치를 조정하는 설명이 중요.",
            "meaningVi": "Chế độ cho phép người bị cáo hoặc bị can không bị tạm giam mà được ở ngoài để chờ xét xử. Cần có sự cho phép của tòa án, có thể yêu cầu đặt tiền bảo lãnh hoặc có người bảo lãnh. Là biện pháp ngăn chặn, bảo đảm thay thế tạm giam, người được tại ngoại phải tuân thủ các quy định của pháp luật và có mặt khi được triệu tập.",
            "context": "형사재판, 구속 대체수단, 피고인 권리",
            "culturalNote": "베트남의 tại ngoại 제도는 한국의 보석제도와 유사하지만, 허가 기준이 더 엄격합니다. 특히 경제범죄나 부패 사건에서는 tại ngoại가 거의 허가되지 않습니다. 한국은 보석금액이 주요 요소지만, 베트남은 범죄의 성격과 도주 위험을 더 중시합니다. 통역 시 한국 의뢰인에게 베트남의 엄격한 기준을 사전에 설명해야 불필요한 기대를 방지할 수 있습니다.",
            "commonMistakes": [
                {
                    "mistake": "tại ngoại를 '석방'으로 통역",
                    "correction": "'보석' 또는 '조건부 석방'",
                    "explanation": "tha tự가 석방이고, tại ngoại는 조건이 있는 보석입니다"
                },
                {
                    "mistake": "tiền bảo lãnh을 '벌금'으로 번역",
                    "correction": "'보석금' 또는 '보증금'",
                    "explanation": "벌금은 tiền phạt이며, 법적 성격이 완전히 다릅니다"
                },
                {
                    "mistake": "보석 허가율을 한국 기준으로 설명",
                    "correction": "베트남의 엄격한 기준을 명시",
                    "explanation": "베트남은 중죄 사건에서 보석이 매우 제한적입니다"
                }
            ],
            "examples": [
                {
                    "ko": "피고인은 보석으로 석방되었습니다.",
                    "vi": "Bị cáo đã được cho tại ngoại.",
                    "situation": "formal"
                },
                {
                    "ko": "보석금 5억 동을 납부해야 합니다.",
                    "vi": "Cần nộp tiền bảo lãnh 500 triệu đồng.",
                    "situation": "formal"
                },
                {
                    "ko": "보석 조건으로 매주 경찰서에 출석해야 해요.",
                    "vi": "Điều kiện tại ngoại là phải có mặt tại trụ sở công an mỗi tuần.",
                    "situation": "onsite"
                }
            ],
            "relatedTerms": ["tạm giam (구속)", "tha tự (석방)", "tiền bảo lãnh (보석금)", "biện pháp ngăn chặn (강제처분)"]
        },
        {
            "slug": "truy-na",
            "korean": "수배",
            "vietnamese": "truy nã",
            "hanja": "追拿",
            "hanjaReading": "追(쫓을 추) + 拿(잡을 나)",
            "pronunciation": "쭈이 나",
            "meaningKo": "도주한 피의자나 피고인을 체포하기 위해 공개적으로 수색하고 검거하는 형사절차. 베트남에서는 경찰이나 검찰이 법원의 승인 하에 발령하며, 국내 수배와 국제 수배(INTERPOL)로 구분. 한국의 지명수배와 동일한 개념. 통역 시 truy nã toàn quốc(전국 수배)와 truy nã quốc tế(국제 수배)를 구분해야 하며, 수배 단계에 따라 법적 효력이 다름을 의뢰인에게 명확히 설명. 베트남에서는 경제범죄자에 대한 국제 수배가 활발히 이루어지고 있음.",
            "meaningVi": "Biện pháp tố tụng để truy tìm và bắt giữ người bị can, bị cáo đã bỏ trốn. Do cơ quan công an hoặc viện kiểm sát ra quyết định với sự phê chuẩn của tòa án. Có hai loại: truy nã trong nước và truy nã quốc tế (thông qua INTERPOL). Người bị truy nã phải chịu các hạn chế về quyền công dân và có thể bị bắt bất cứ lúc nào.",
            "context": "형사절차, 도주범 검거, 국제공조",
            "culturalNote": "베트남의 truy nã(수배) 제도는 한국과 유사하지만, 경제범죄나 부패 사건에서 더 적극적으로 활용됩니다. 특히 국제 수배의 경우 INTERPOL을 통해 신속하게 진행되며, 한국과 베트남 간 범죄인 인도 조약이 있어 효력이 큽니다. 베트남에서는 수배자의 재산 동결과 출국 금지가 동시에 이루어지므로, 가족들에게 미치는 영향도 설명해야 합니다. 수배 해제 절차도 복잡하므로 통역 시 주의 필요.",
            "commonMistakes": [
                {
                    "mistake": "truy nã를 '지명수배'로만 번역",
                    "correction": "'수배' 또는 '지명수배' (상황에 따라)",
                    "explanation": "truy nã는 지명수배를 포함하는 더 넓은 개념입니다"
                },
                {
                    "mistake": "truy nã quốc tế를 '국제 지명수배'로만 통역",
                    "correction": "'국제 수배' 또는 'INTERPOL 수배'로 명확히",
                    "explanation": "INTERPOL을 통한 공식 절차임을 명시해야 합니다"
                },
                {
                    "mistake": "수배 효력을 한국 기준으로 설명",
                    "correction": "베트남의 재산 동결, 출국 금지 등 부가 조치 설명",
                    "explanation": "베트남은 수배 시 재산에 대한 조치가 동시에 이루어집니다"
                }
            ],
            "examples": [
                {
                    "ko": "피의자는 현재 전국에 수배 중입니다.",
                    "vi": "Người bị nghi ngờ hiện đang bị truy nã toàn quốc.",
                    "situation": "formal"
                },
                {
                    "ko": "INTERPOL을 통해 국제 수배를 발령했습니다.",
                    "vi": "Đã ra quyết định truy nã quốc tế thông qua INTERPOL.",
                    "situation": "formal"
                },
                {
                    "ko": "수배자의 은행 계좌가 모두 동결됐어요.",
                    "vi": "Tất cả tài khoản ngân hàng của người bị truy nã đã bị phong tỏa.",
                    "situation": "onsite"
                }
            ],
            "relatedTerms": ["bắt giữ (체포)", "lệnh bắt (체포영장)", "bỏ trốn (도주)", "INTERPOL (인터폴)"]
        },
        {
            "slug": "lenh-bat",
            "korean": "체포영장",
            "vietnamese": "lệnh bắt",
            "hanja": "逮捕令狀",
            "hanjaReading": "逮(잡을 체) + 捕(잡을 포) + 令(영 령) + 狀(문서 장)",
            "pronunciation": "렝 밧",
            "meaningKo": "법원이나 검찰이 발부하는 피의자 또는 피고인을 체포할 수 있는 법적 권한을 증명하는 문서. 베트남에서는 viện kiểm sát(검찰)이 발부하며, 중죄의 경우 필수. 한국의 체포영장과 동일한 개념. 통역 시 lệnh bắt(체포영장)와 lệnh khám xét(압수수색영장)을 혼동하지 말 것. 베트남 법상 lệnh bắt 없이 체포하면 위법이며, 피의자는 영장을 열람할 권리가 있음을 의뢰인에게 설명해야 함. 긴급체포의 경우 사후에 영장을 받아야 함.",
            "meaningVi": "Văn bản do viện kiểm sát hoặc tòa án ban hành, cho phép bắt giữ người bị can hoặc bị cáo. Đối với các tội nghiêm trọng, lệnh bắt là bắt buộc. Người bị bắt có quyền được xem lệnh bắt và biết lý do bị bắt. Lệnh bắt phải ghi rõ họ tên, địa chỉ, tội danh và thời hạn hiệu lực. Bắt người mà không có lệnh bắt là vi phạm pháp luật.",
            "context": "형사절차, 강제수사, 피의자 권리",
            "culturalNote": "베트남의 lệnh bắt(체포영장) 제도는 한국과 매우 유사하지만, 발부 주체가 검찰이라는 점이 다릅니다. 한국은 법원이 발부하지만 베트남은 검찰이 주도적 역할을 합니다. 베트남에서는 경미한 범죄의 경우 영장 없이 체포 가능한 경우도 있으나, 중죄는 반드시 영장이 필요합니다. 통역 시 피의자의 영장 열람권을 반드시 설명하고, 영장 내용을 정확히 통역해야 합니다.",
            "commonMistakes": [
                {
                    "mistake": "lệnh bắt을 '구속영장'으로 번역",
                    "correction": "'체포영장' (구속은 lệnh tạm giam)",
                    "explanation": "체포와 구속은 법적으로 다른 절차입니다"
                },
                {
                    "mistake": "lệnh khám xét을 '체포영장'으로 통역",
                    "correction": "'압수수색영장'",
                    "explanation": "lệnh khám xét은 장소나 물건 수색 영장입니다"
                },
                {
                    "mistake": "영장 발부 주체를 '법원'으로 통역",
                    "correction": "'검찰' (viện kiểm sát)",
                    "explanation": "베트남은 검찰이 영장을 발부합니다"
                }
            ],
            "examples": [
                {
                    "ko": "검찰이 피의자에 대한 체포영장을 발부했습니다.",
                    "vi": "Viện kiểm sát đã ban hành lệnh bắt đối với người bị nghi ngờ.",
                    "situation": "formal"
                },
                {
                    "ko": "체포영장에 범죄 혐의가 명시되어 있습니다.",
                    "vi": "Lệnh bắt có ghi rõ tội danh bị cáo buộc.",
                    "situation": "formal"
                },
                {
                    "ko": "영장을 보여달라고 요구할 권리가 있어요.",
                    "vi": "Bạn có quyền yêu cầu xem lệnh bắt.",
                    "situation": "onsite"
                }
            ],
            "relatedTerms": ["bắt giữ (체포)", "lệnh khám xét (압수수색영장)", "viện kiểm sát (검찰)", "quyền của người bị bắt (피의자 권리)"]
        },
        {
            "slug": "dong-pham",
            "korean": "공범",
            "vietnamese": "đồng phạm",
            "hanja": "共犯",
            "hanjaReading": "共(함께 공) + 犯(범할 범)",
            "pronunciation": "동 팜",
            "meaningKo": "두 명 이상이 공동으로 범죄를 실행하거나 범죄 실행을 도운 사람들. 베트남 형법에서는 chủ mưu(주모자), thực hành(실행범), giúp sức(방조범), xúi giục(교사범)으로 구분. 한국의 공범 개념과 유사하지만 분류 방식이 다름. 통역 시 각 공범 유형에 따라 형량이 크게 달라지므로 정확한 구분이 중요. 베트남에서는 chủ mưu가 가장 무거운 처벌을 받으며, giúp sức은 상대적으로 가벼운 처벌. 경제범죄에서 đồng phạm 인정 범위가 넓어 주의 필요.",
            "meaningVi": "Hai người trở lên cùng thực hiện một tội phạm hoặc cố ý giúp đỡ người khác thực hiện tội phạm. Luật hình sự Việt Nam phân loại thành: chủ mưu (người tổ chức, chỉ huy), thực hành (người trực tiếp thực hiện), giúp sức (người tạo điều kiện) và xúi giục (người kích động). Mỗi loại đồng phạm có mức độ trách nhiệm hình sự khác nhau, chủ mưu thường bị phạt nặng nhất.",
            "context": "형사책임, 범죄 유형, 양형",
            "culturalNote": "베트남의 đồng phạm(공범) 분류는 한국보다 세분화되어 있습니다. 한국은 정범과 종범으로 크게 나누지만, 베트남은 4단계로 구분하며 각각 형량 차이가 큽니다. 특히 부패 사건이나 경제범죄에서 đồng phạm 인정 범위가 매우 넓어, 단순히 서류에 서명했거나 지시를 전달한 것만으로도 공범이 될 수 있습니다. 통역 시 의뢰인이 자신의 역할을 과소평가하지 않도록 경고해야 합니다.",
            "commonMistakes": [
                {
                    "mistake": "chủ mưu를 '주범'으로만 번역",
                    "correction": "'주모자' 또는 '공모 주도자'",
                    "explanation": "chủ mưu는 조직하고 지휘한 사람으로 한국의 주범보다 넓은 개념입니다"
                },
                {
                    "mistake": "giúp sức를 '종범'으로 통역",
                    "correction": "'방조범' 또는 '협조자'",
                    "explanation": "종범은 從犯으로 법적 개념이 다릅니다"
                },
                {
                    "mistake": "공범 범위를 한국 기준으로 설명",
                    "correction": "베트남의 넓은 공범 인정 범위를 명시",
                    "explanation": "베트남은 간접적 관여도 공범으로 인정하는 경우가 많습니다"
                }
            ],
            "examples": [
                {
                    "ko": "피고인은 이 사건의 주모자로 인정됩니다.",
                    "vi": "Bị cáo được xác định là chủ mưu trong vụ án này.",
                    "situation": "formal"
                },
                {
                    "ko": "방조범은 실행범보다 가벼운 처벌을 받습니다.",
                    "vi": "Người giúp sức bị phạt nhẹ hơn người thực hành.",
                    "situation": "formal"
                },
                {
                    "ko": "서류에 서명한 것만으로도 공범이 될 수 있어요.",
                    "vi": "Chỉ việc ký vào giấy tờ cũng có thể bị coi là đồng phạm.",
                    "situation": "onsite"
                }
            ],
            "relatedTerms": ["chủ mưu (주모자)", "thực hành (실행범)", "giúp sức (방조범)", "xúi giục (교사범)"]
        },
        {
            "slug": "xu-ly-hinh-su",
            "korean": "형사처분",
            "vietnamese": "xử lý hình sự",
            "hanja": "處理刑事",
            "hanjaReading": "處(처리할 처) + 理(다스릴 리) + 刑(형벌 형) + 事(일 사)",
            "pronunciation": "쑤 리 힌 쑤",
            "meaningKo": "범죄를 저지른 사람에 대해 형사법에 따라 법적 책임을 묻고 처벌하는 일련의 절차와 결정. 베트남에서는 khởi tố(기소), xét xử(재판), thi hành án(형 집행)의 단계로 진행. 한국의 형사처분과 개념이 동일하지만 절차가 다름. 통역 시 xử lý hành chính(행정처분)과 명확히 구분해야 하며, 형사처분은 전과 기록이 남고 더 무거운 법적 결과를 초래함을 의뢰인에게 설명. 베트남에서는 경제범죄에 대한 형사처분이 매우 엄격함.",
            "meaningVi": "Quá trình và quyết định xử lý trách nhiệm pháp lý đối với người phạm tội theo luật hình sự. Bao gồm các giai đoạn khởi tố, điều tra, truy tố, xét xử và thi hành án. Xử lý hình sự khác với xử lý hành chính ở chỗ nó để lại tiền án tiền sự và có hậu quả pháp lý nghiêm trọng hơn. Chỉ áp dụng khi hành vi vi phạm đã cấu thành tội phạm theo quy định của bộ luật hình sự.",
            "context": "형사절차, 법적 책임, 처벌",
            "culturalNote": "베트남의 xử lý hình sự(형사처분)는 한국과 절차가 유사하지만, 경제범죄나 부패 사건에서 훨씬 엄격하게 적용됩니다. 한국은 벌금형이나 집행유예가 많지만, 베트남은 실형을 선고하는 비율이 높습니다. 특히 외국인의 경우 형사처분 후 추방될 가능성이 크므로 통역 시 이를 명확히 설명해야 합니다. 또한 베트남에서는 형사처분 이력이 취업, 비자 발급 등에 큰 영향을 미칩니다.",
            "commonMistakes": [
                {
                    "mistake": "xử lý hành chính을 '형사처분'으로 통역",
                    "correction": "'행정처분' (형사처분은 xử lý hình sự)",
                    "explanation": "행정처분과 형사처분은 법적 효과가 완전히 다릅니다"
                },
                {
                    "mistake": "khởi tố를 '재판'으로 번역",
                    "correction": "'기소' 또는 '소추'",
                    "explanation": "khởi tố는 수사 시작 단계이고 xét xử가 재판입니다"
                },
                {
                    "mistake": "형사처분 결과를 한국 기준으로 설명",
                    "correction": "베트남의 엄격한 처벌 기준과 추방 가능성 명시",
                    "explanation": "베트남은 외국인에 대한 형사처분이 더 엄격합니다"
                }
            ],
            "examples": [
                {
                    "ko": "이 사건은 형사처분 대상입니다.",
                    "vi": "Vụ việc này thuộc diện xử lý hình sự.",
                    "situation": "formal"
                },
                {
                    "ko": "행정처분이 아닌 형사처분이 필요합니다.",
                    "vi": "Cần xử lý hình sự chứ không phải xử lý hành chính.",
                    "situation": "formal"
                },
                {
                    "ko": "형사처분 받으면 전과 기록이 남아요.",
                    "vi": "Nếu bị xử lý hình sự sẽ để lại tiền án tiền sự.",
                    "situation": "onsite"
                }
            ],
            "relatedTerms": ["khởi tố (기소)", "xét xử (재판)", "thi hành án (형 집행)", "xử lý hành chính (행정처분)"]
        },
        {
            "slug": "giam-an",
            "korean": "감형",
            "vietnamese": "giảm án",
            "hanja": "減刑",
            "hanjaReading": "減(덜 감) + 刑(형벌 형)",
            "pronunciation": "잠 안",
            "meaningKo": "선고된 형벌을 줄이는 법적 조치. 베트남에서는 복역 중 모범적 행동, 공로, 특별사면 등의 사유로 가능. 법원이나 국가주석의 권한으로 이루어짐. 한국의 감형제도와 유사하지만 절차가 다름. 통역 시 giảm án(감형)과 ân xá(사면)를 구분해야 하며, 감형은 형량을 줄이는 것이고 사면은 형 자체를 면제하는 것. 베트남에서는 명절(Tết)이나 국경일에 대규모 감형이 이루어지는 관례가 있음을 의뢰인에게 설명하면 도움이 됨.",
            "meaningVi": "Biện pháp giảm nhẹ hình phạt đã tuyên. Có thể được thực hiện do tòa án hoặc Chủ tịch nước quyết định dựa trên các lý do như cải tạo tốt, có thành tích, đặc xá. Giảm án khác với ân xá ở chỗ chỉ giảm mức độ hình phạt chứ không xóa tội. Thường được áp dụng vào các dịp lễ lớn như Tết, Quốc khánh hoặc khi phạm nhân có biểu hiện cải tạo tốt.",
            "context": "형 집행, 사면, 교정",
            "culturalNote": "베트남의 giảm án(감형) 제도는 한국보다 더 자주, 더 광범위하게 적용됩니다. 특히 Tết(설)이나 9월 2일(국경일) 같은 국가 기념일에 대통령령으로 대규모 감형이 이루어집니다. 한국은 개별 심사가 엄격하지만, 베트남은 일정 조건을 만족하면 자동으로 감형되는 경우가 많습니다. 통역 시 의뢰인에게 감형 가능 시기와 조건을 명확히 설명하면 수감 생활에 대한 계획을 세우는 데 도움이 됩니다.",
            "commonMistakes": [
                {
                    "mistake": "giảm án을 '사면'으로 번역",
                    "correction": "'감형' (사면은 ân xá)",
                    "explanation": "감형은 형량을 줄이는 것이고 사면은 형을 면제하는 것입니다"
                },
                {
                    "mistake": "đặc xá를 '특별감형'으로 통역",
                    "correction": "'특별사면' 또는 '특사'",
                    "explanation": "đặc xá는 국가주석이 선포하는 특별사면입니다"
                },
                {
                    "mistake": "감형 조건을 한국 기준으로 설명",
                    "correction": "베트남의 명절 감형 관례와 자동 감형 조건 명시",
                    "explanation": "베트남은 집단적 감형이 흔합니다"
                }
            ],
            "examples": [
                {
                    "ko": "모범수로 인정되어 1년 감형받았습니다.",
                    "vi": "Được công nhận là phạm nhân cải tạo tốt và được giảm án 1 năm.",
                    "situation": "formal"
                },
                {
                    "ko": "국경일 특사로 감형 대상이 될 수 있습니다.",
                    "vi": "Có thể được giảm án theo đặc xá nhân dịp Quốc khánh.",
                    "situation": "formal"
                },
                {
                    "ko": "설 명절에 감형 기회가 있어요.",
                    "vi": "Có cơ hội được giảm án vào dịp Tết.",
                    "situation": "onsite"
                }
            ],
            "relatedTerms": ["ân xá (사면)", "đặc xá (특별사면)", "cải tạo (교정)", "thi hành án (형 집행)"]
        },
        {
            "slug": "tha-tu",
            "korean": "석방",
            "vietnamese": "thả tự do",
            "hanja": "釋放",
            "hanjaReading": "釋(풀 석) + 放(놓을 방)",
            "pronunciation": "타 뜨 도",
            "meaningKo": "구금되어 있던 사람을 자유롭게 풀어주는 조치. 베트남에서는 형기 만료, 무죄 판결, 사면 등의 사유로 이루어짐. thả tự do(완전 석방)와 tại ngoại(조건부 석방/보석)를 명확히 구분해야 함. 통역 시 석방 후에도 일정 기간 감시를 받는 경우(quản chế)가 있음을 설명. 베트남에서는 외국인의 경우 석방 즉시 추방되는 경우가 많으므로 의뢰인에게 사전 안내 필요. 석방 증명서(giấy thả tự do)를 반드시 받아야 이후 법적 문제 방지 가능.",
            "meaningVi": "Hành động thả người đang bị giam giữ ra tự do. Có thể do hết thời hạn thi hành án, được tuyên vô tội, được ân xá hoặc các lý do hợp pháp khác. Khác với tại ngoại (thả có điều kiện), thả tự do là thả hoàn toàn không ràng buộc. Tuy nhiên, một số trường hợp sau khi thả vẫn phải chịu biện pháp quản chế (giám sát tại địa phương). Người được thả phải nhận giấy thả để làm thủ tục hành chính.",
            "context": "형 집행 종료, 무죄 판결, 인권",
            "culturalNote": "베트남의 thả tự do(석방) 절차는 한국과 유사하지만, 외국인에 대한 처리가 다릅니다. 한국은 석방 후 출국 절차를 밟지만, 베트남은 석방 즉시 출입국관리소로 이송되어 추방되는 경우가 많습니다. 또한 석방 후에도 quản chế(관제) 조치로 거주지 제한이나 정기 보고 의무가 부과될 수 있습니다. 통역 시 석방이 완전한 자유를 의미하지 않을 수 있음을 명확히 설명해야 합니다.",
            "commonMistakes": [
                {
                    "mistake": "tại ngoại를 '석방'으로 통역",
                    "correction": "'보석' 또는 '조건부 석방'",
                    "explanation": "thả tự do가 완전 석방이고 tại ngoại는 조건부입니다"
                },
                {
                    "mistake": "quản chế를 '보호관찰'로 번역",
                    "correction": "'관제' 또는 '거주지 감시'",
                    "explanation": "quản chế는 거주지 제한이 있는 행정 조치입니다"
                },
                {
                    "mistake": "석방 후 절차를 한국 기준으로 설명",
                    "correction": "외국인 즉시 추방 가능성과 관제 조치 명시",
                    "explanation": "베트남은 외국인 석방 시 추방이 일반적입니다"
                }
            ],
            "examples": [
                {
                    "ko": "형기가 만료되어 오늘 석방되었습니다.",
                    "vi": "Đã được thả tự do hôm nay do hết thời hạn thi hành án.",
                    "situation": "formal"
                },
                {
                    "ko": "무죄 판결로 즉시 석방 조치되었습니다.",
                    "vi": "Đã được thả tự do ngay lập tức do bản án tuyên vô tội.",
                    "situation": "formal"
                },
                {
                    "ko": "석방됐지만 3개월간 관제 조치를 받아요.",
                    "vi": "Được thả tự do nhưng phải chịu biện pháp quản chế trong 3 tháng.",
                    "situation": "onsite"
                }
            ],
            "relatedTerms": ["tại ngoại (보석)", "quản chế (관제)", "giấy thả tự do (석방증명서)", "hết hạn tù (형기 만료)"]
        },
        {
            "slug": "tu-hinh",
            "korean": "사형",
            "vietnamese": "tử hình",
            "hanja": "死刑",
            "hanjaReading": "死(죽을 사) + 刑(형벌 형)",
            "pronunciation": "뜨 힌",
            "meaningKo": "범죄자의 생명을 박탈하는 최고형. 베트남에서는 살인, 마약 밀매, 반역죄 등 중대 범죄에 적용. 집행 방법은 총살형이며, 베트남은 세계에서 사형 집행이 많은 국가 중 하나. 한국은 1997년 이후 사형 집행이 없지만 베트남은 여전히 활발히 집행 중. 통역 시 bản án tử hình(사형 선고)와 thi hành tử hình(사형 집행)을 구분하고, 상소 기회와 특사 가능성을 설명해야 함. 베트남에서는 마약 범죄에 대한 사형 선고율이 매우 높으므로 의뢰인에게 심각성을 충분히 전달해야 함.",
            "meaningVi": "Hình phạt tước đoạt sinh mạng của người phạm tội, là hình phạt nghiêm khắc nhất trong hệ thống hình phạt. Được áp dụng cho các tội đặc biệt nghiêm trọng như giết người, buôn bán ma túy số lượng lớn, phản bội tổ quốc. Việt Nam thi hành tử hình bằng hình thức tiêm thuốc độc hoặc bắn. Người bị kết án tử hình có quyền kháng cáo và xin đặc xá. Tuy nhiên, tỷ lệ tử hình được giảm xuống rất thấp.",
            "context": "형벌, 중대 범죄, 사법 제도",
            "culturalNote": "베트남의 tử hình(사형) 제도는 한국과 큰 차이가 있습니다. 한국은 사실상 사형 집행이 중단되었지만(사형 폐지국), 베트남은 여전히 활발히 집행하고 있습니다(사형 존치국). 특히 마약 범죄의 경우 100g 이상의 헤로인이나 코카인 소지만으로도 사형이 선고될 수 있습니다. 통역 시 한국 의뢰인에게 베트남의 엄격한 사형 기준을 명확히 설명하고, 마약 범죄에 대한 경각심을 높여야 합니다.",
            "commonMistakes": [
                {
                    "mistake": "bản án tử hình을 '사형 집행'으로 번역",
                    "correction": "'사형 선고' (집행은 thi hành tử hình)",
                    "explanation": "선고와 집행은 시점과 의미가 완전히 다릅니다"
                },
                {
                    "mistake": "총살형을 유일한 집행 방법으로 설명",
                    "correction": "현재는 주로 독극물 주사형 사용",
                    "explanation": "베트남은 2011년부터 독극물 주사형으로 전환했습니다"
                },
                {
                    "mistake": "사형 기준을 한국과 동일하게 설명",
                    "correction": "베트남의 마약 범죄 사형 기준이 매우 낮음을 명시",
                    "explanation": "마약 100g만으로도 사형이 가능합니다"
                }
            ],
            "examples": [
                {
                    "ko": "피고인에게 사형이 선고되었습니다.",
                    "vi": "Bị cáo đã bị tuyên án tử hình.",
                    "situation": "formal"
                },
                {
                    "ko": "마약 밀매죄로 사형을 받을 수 있습니다.",
                    "vi": "Có thể bị án tử hình vì tội buôn bán ma túy.",
                    "situation": "formal"
                },
                {
                    "ko": "100g 이상 마약 소지하면 사형 대상이에요.",
                    "vi": "Nếu tàng trữ trên 100g ma túy có thể bị tử hình.",
                    "situation": "onsite"
                }
            ],
            "relatedTerms": ["bản án tử hình (사형 선고)", "thi hành tử hình (사형 집행)", "kháng cáo (항소)", "đặc xá (특별사면)"]
        },
        {
            "slug": "toi-kinh-te",
            "korean": "경제범죄",
            "vietnamese": "tội kinh tế",
            "hanja": "經濟犯罪",
            "hanjaReading": "經(경영할 경) + 濟(구제할 제) + 犯(범할 범) + 罪(죄 죄)",
            "pronunciation": "또이 낀 떼",
            "meaningKo": "경제 활동과 관련하여 발생하는 범죄 행위의 총칭. 베트남에서는 횡령(tham ô), 뇌물(hối lộ), 사기(lừa đảo), 탈세(trốn thuế), 밀수(buôn lậu) 등을 포함. 베트남 정부가 강력히 단속하는 분야로 형량이 매우 무거움. 통역 시 tội kinh tế(경제범죄)와 vi phạm hành chính trong kinh doanh(사업상 행정위반)를 구분해야 하며, 경제범죄는 형사처벌 대상이고 전과가 남음. 베트남에서는 외국인 투자자도 경제범죄로 구속되는 사례가 많으므로 계약서나 회계 처리에 각별한 주의 필요함을 설명.",
            "meaningVi": "Tổng hợp các hành vi phạm tội liên quan đến hoạt động kinh tế. Bao gồm tham ô, hối lộ, lừa đảo, trốn thuế, buôn lậu và các tội khác xâm phạm trật tự quản lý kinh tế. Việt Nam đang tăng cường đấu tranh chống tội phạm kinh tế với các mức phạt rất nghiêm khắc. Tội kinh tế không chỉ ảnh hưởng đến cá nhân mà còn có thể liên đới đến doanh nghiệp và người liên quan.",
            "context": "경제 활동, 부패 방지, 기업 범죄",
            "culturalNote": "베트남의 tội kinh tế(경제범죄) 단속은 한국보다 훨씬 엄격합니다. 특히 부패 방지 캠페인의 일환으로 고위 공직자나 기업인에 대한 경제범죄 수사가 강화되고 있습니다. 한국에서는 벌금이나 집행유예로 끝나는 사안도 베트남에서는 실형이 선고되는 경우가 많습니다. 외국인 투자자의 경우 회계 장부 불일치, 송금 절차 위반 등 사소해 보이는 실수도 경제범죄로 기소될 수 있으므로 통역 시 충분한 경고가 필요합니다.",
            "commonMistakes": [
                {
                    "mistake": "vi phạm hành chính를 '경제범죄'로 통역",
                    "correction": "'행정위반' (경제범죄는 tội kinh tế)",
                    "explanation": "행정위반은 벌금형이지만 경제범죄는 형사처벌입니다"
                },
                {
                    "mistake": "tham ô를 '배임'으로 번역",
                    "correction": "'횡령' (배임은 다른 개념)",
                    "explanation": "tham ô는 공금이나 타인 재산을 가로채는 횡령입니다"
                },
                {
                    "mistake": "경제범죄 처벌 수위를 한국 기준으로 설명",
                    "correction": "베트남의 엄격한 실형 선고 가능성 명시",
                    "explanation": "베트남은 경제범죄에 대한 처벌이 매우 무겁습니다"
                }
            ],
            "examples": [
                {
                    "ko": "횡령죄로 경제범죄 혐의를 받고 있습니다.",
                    "vi": "Đang bị cáo buộc tội kinh tế về hành vi tham ô.",
                    "situation": "formal"
                },
                {
                    "ko": "경제범죄는 최대 20년 징역형까지 가능합니다.",
                    "vi": "Tội kinh tế có thể bị phạt tù lên đến 20 năm.",
                    "situation": "formal"
                },
                {
                    "ko": "회계 장부 조작만으로도 경제범죄가 될 수 있어요.",
                    "vi": "Chỉ việc làm giả sổ sách kế toán cũng có thể cấu thành tội kinh tế.",
                    "situation": "onsite"
                }
            ],
            "relatedTerms": ["tham ô (횡령)", "hối lộ (뇌물)", "lừa đảo (사기)", "trốn thuế (탈세)"]
        }
    ]

    # 5. 중복 제거 필터링
    filtered_terms = [term for term in new_terms if term['slug'] not in existing_slugs]

    # 6. 데이터 확장
    data.extend(filtered_terms)

    # 7. 파일 저장
    with open(file_path, 'w', encoding='utf-8') as f:
        json.dump(data, f, ensure_ascii=False, indent=2)

    print(f"✅ 추가 완료: {len(filtered_terms)}개 용어")
    print(f"📊 총 용어 수: {len(data)}개")

    if len(filtered_terms) < len(new_terms):
        skipped = len(new_terms) - len(filtered_terms)
        print(f"⚠️  중복으로 건너뛴 용어: {skipped}개")

if __name__ == "__main__":
    main()
