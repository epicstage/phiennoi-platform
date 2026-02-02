#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
미디어법/언론법 용어 추가 스크립트
Theme: Media Law/Press Law
"""

import json
import os

# 파일 경로 설정
file_path = os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', 'data', 'terms', 'legal.json')

# 새로운 용어 데이터 (10개)
new_terms = [
    {
        "slug": "bao-chi",
        "korean": "언론",
        "vietnamese": "Báo chí",
        "hanja": "言論",
        "hanjaReading": "言(말씀 언) + 論(논할 론)",
        "pronunciation": "바오찌",
        "meaningKo": "신문, 방송, 잡지 등 대중에게 정보를 전달하는 매체 활동을 총칭하는 용어입니다. 통역 시 '언론'과 '보도'를 구분해야 하며, '언론'은 제도적 의미(báo chí), '보도'는 행위적 의미(tin tức/đưa tin)로 번역합니다. 베트남에서는 국가 통제가 강한 반면, 한국은 상대적으로 자유로운 언론 환경이므로 양국의 언론 자유도 차이를 이해하고 통역해야 합니다. 법정 통역 시 '언론중재위원회', '언론사' 등의 맥락을 정확히 파악하는 것이 중요합니다.",
        "meaningVi": "Hoạt động truyền tải thông tin đến công chúng thông qua các phương tiện như báo chí, phát thanh, truyền hình, tạp chí. Trong bối cảnh pháp luật, báo chí là hoạt động được quy định và quản lý bởi Luật Báo chí, bao gồm cả quyền và nghĩa vụ của cơ quan báo chí và người làm báo.",
        "context": "법률 문서, 언론중재 절차, 언론사 등록 및 허가 관련 행정 업무",
        "culturalNote": "한국의 언론은 헌법상 자유가 보장되며 독립적 운영이 원칙이지만, 베트남의 언론은 공산당과 국가의 지도 하에 운영되어 사회주의 이념에 부합해야 합니다. 따라서 '언론 자유'라는 개념 자체가 양국에서 다른 의미로 받아들여질 수 있으므로, 통역 시 맥락을 명확히 전달해야 합니다. 한국에서는 언론중재위원회를 통한 민간 분쟁 해결이 활성화되어 있으나, 베트남에서는 국가 기관이 언론 통제의 주체가 됩니다.",
        "commonMistakes": [
            {
                "mistake": "Báo chí를 모든 '뉴스' 맥락에 사용",
                "correction": "제도는 báo chí, 개별 기사는 tin tức/bài báo",
                "explanation": "Báo chí는 언론 '기관'이나 '제도'를 의미하므로, 개별 뉴스 기사에는 부적절"
            },
            {
                "mistake": "'자유 언론'을 tự do báo chí로 직역",
                "correction": "Tự do ngôn luận 또는 tự do báo chí (맥락에 따라)",
                "explanation": "한국식 '언론 자유'는 베트남에서 정치적으로 민감한 표현이므로 신중히 사용"
            },
            {
                "mistake": "'언론사'를 công ty báo chí로 번역",
                "correction": "Cơ quan báo chí 또는 tòa soạn",
                "explanation": "베트남에서는 언론사를 영리 기업이 아닌 '기관'으로 보는 경향"
            }
        ],
        "examples": [
            {
                "ko": "피고인은 언론에 허위 사실을 유포하여 원고의 명예를 훼손하였습니다.",
                "vi": "Bị cáo đã phát tán thông tin sai sự thật trên báo chí, làm tổn hại danh dự nguyên đơn.",
                "situation": "formal"
            },
            {
                "ko": "이 사건은 언론의 과도한 보도로 인해 사회적 파장이 컸습니다.",
                "vi": "Vụ việc này đã gây phản ứng xã hội lớn do sự đưa tin quá mức của báo chí.",
                "situation": "formal"
            },
            {
                "ko": "언론사 등록 신청서를 제출해 주시기 바랍니다.",
                "vi": "Vui lòng nộp đơn đăng ký cơ quan báo chí.",
                "situation": "formal"
            }
        ],
        "relatedTerms": ["언론자유", "보도", "명예훼손", "언론중재"]
    },
    {
        "slug": "quyen-tu-do-bao-chi",
        "korean": "언론자유",
        "vietnamese": "Quyền tự do báo chí",
        "hanja": "言論自由",
        "hanjaReading": "言(말씀 언) + 論(논할 론) + 自(스스로 자) + 由(말미암을 유)",
        "pronunciation": "꿘뚜도바오찌",
        "meaningKo": "국가나 타인의 간섭 없이 자유롭게 의견을 표현하고 정보를 전달할 수 있는 헌법상 기본권입니다. 통역 시 주의할 점은 '언론의 자유'와 '표현의 자유'를 구분하는 것인데, 언론의 자유는 매체를 통한 표현(quyền tự do báo chí), 표현의 자유는 개인의 일반적 의사 표현(quyền tự do ngôn luận)을 의미합니다. 한국에서는 헌법 제21조로 보장되지만 베트남에서는 사회주의 체제 내에서 제한적으로 인정되므로, 양국의 법적 개념 차이를 명확히 전달해야 합니다. 법정에서는 명예훼손이나 모욕죄와의 충돌 사례가 많으므로 균형 있는 통역이 필요합니다.",
        "meaningVi": "Quyền cơ bản được hiến pháp bảo đảm, cho phép cá nhân và cơ quan báo chí tự do bày tỏ ý kiến, truyền đạt thông tin mà không bị nhà nước hoặc bên thứ ba can thiệp. Tuy nhiên, quyền này không phải là tuyệt đối và phải tuân thủ pháp luật về danh dự, an ninh quốc gia, và trật tự công cộng.",
        "context": "헌법 소송, 언론 관련 민·형사 사건, 언론중재 절차",
        "culturalNote": "한국은 군사독재 시절 언론 탄압을 겪은 후 언론 자유를 매우 중시하며, 언론중재위원회를 통한 자율적 분쟁 해결 제도가 발달했습니다. 반면 베트남은 공산당이 언론을 '당과 국가의 도구'로 규정하므로, 언론 자유의 범위가 사회주의 이념과 국가 이익에 부합하는 선에서 제한됩니다. 통역 시 '자유'라는 단어가 양국에서 다른 정치적 함의를 갖는다는 점을 인지하고, 법적 맥락을 정확히 전달해야 합니다.",
        "commonMistakes": [
            {
                "mistake": "'언론 자유'를 tự do báo chí만으로 번역",
                "correction": "Quyền tự do báo chí (권리임을 명시)",
                "explanation": "법적 맥락에서는 '권리'임을 명확히 해야 함"
            },
            {
                "mistake": "한국의 언론 자유 개념을 그대로 설명",
                "correction": "베트남 청자에게는 '법적 제한 범위' 함께 설명",
                "explanation": "베트남에서는 무제한적 자유로 오해될 수 있음"
            },
            {
                "mistake": "'표현의 자유'와 혼용",
                "correction": "언론=báo chí, 표현=ngôn luận으로 구분",
                "explanation": "법적으로 다른 보호 범위를 가진 별개의 권리"
            }
        ],
        "examples": [
            {
                "ko": "헌법은 언론의 자유를 보장하지만, 타인의 명예를 훼손해서는 안 됩니다.",
                "vi": "Hiến pháp bảo đảm quyền tự do báo chí, nhưng không được xâm phạm danh dự người khác.",
                "situation": "formal"
            },
            {
                "ko": "이번 판결은 언론 자유와 사생활 보호의 균형점을 제시했습니다.",
                "vi": "Phán quyết này đã đưa ra điểm cân bằng giữa quyền tự do báo chí và bảo vệ đời tư.",
                "situation": "formal"
            },
            {
                "ko": "언론 자유의 한계는 공익과의 비교형량으로 판단됩니다.",
                "vi": "Giới hạn của quyền tự do báo chí được xác định thông qua cân nhắc lợi ích công cộng.",
                "situation": "formal"
            }
        ],
        "relatedTerms": ["표현의자유", "언론", "검열", "명예훼손"]
    },
    {
        "slug": "vu-khong",
        "korean": "명예훼손",
        "vietnamese": "Vụ khống",
        "hanja": "名譽毁損",
        "hanjaReading": "名(이름 명) + 譽(기릴 예) + 毁(헐 훼) + 損(덜 손)",
        "pronunciation": "붕콩",
        "meaningKo": "타인의 사회적 평가를 저하시킬 만한 구체적 사실이나 허위 사실을 공연히 적시하여 명예를 해치는 행위입니다. 통역 시 핵심은 '사실 적시'인지 '의견 표명'인지를 구분하는 것으로, 사실 적시만 명예훼손이 됩니다. 또한 '공연성'(công khai) 요건이 중요하므로 1:1 대화는 해당하지 않습니다. 한국은 진실한 사실도 명예훼손이 될 수 있으나(단, 공익 목적 시 위법성 조각), 베트남은 허위 사실만 처벌하는 경향이 있어 양국의 법리 차이를 명확히 전달해야 합니다. '모욕'(xúc phạm danh dự)과 구분하여 통역하는 것이 필수입니다.",
        "meaningVi": "Hành vi công khai đưa ra thông tin cụ thể (thật hoặc giả) làm giảm uy tín, danh dự của người khác trong xã hội. Theo pháp luật Hàn Quốc, cả sự thật lẫn thông tin sai đều có thể cấu thành tội nếu không vì mục đích công ích. Ở Việt Nam, chủ yếu xử lý trường hợp thông tin sai sự thật (vu khống).",
        "context": "민·형사 소송, 언론 중재, 인터넷 명예훼손 사건",
        "culturalNote": "한국에서는 SNS와 온라인 커뮤니티 발달로 인터넷 명예훼손 사건이 급증하여, '사이버 명예훼손'이 별도 법리로 발전했습니다. 베트남에서는 전통적으로 개인 간 분쟁은 조정으로 해결하려는 경향이 강하나, 최근 소셜미디어 확산으로 명예훼손 사건이 증가하고 있습니다. 특히 베트남에서는 '당과 국가 지도자에 대한 명예훼손'을 일반 명예훼손보다 엄중히 처벌하는 점이 한국과 다르므로, 통역 시 정치적 맥락을 고려해야 합니다.",
        "commonMistakes": [
            {
                "mistake": "'명예훼손'을 mất danh dự로 번역",
                "correction": "Vụ khống (법률 용어) 또는 tội phỉ báng",
                "explanation": "Mất danh dự는 '명예를 잃다'는 일반 표현, 법적 용어 아님"
            },
            {
                "mistake": "모욕죄와 구분 없이 같은 용어 사용",
                "correction": "명예훼손=vụ khống, 모욕=xúc phạm danh dự",
                "explanation": "법적으로 구성요건이 다른 별개의 범죄"
            },
            {
                "mistake": "'진실 적시 명예훼손' 개념 설명 누락",
                "correction": "베트남 청자에게 '사실이어도 처벌 가능' 설명 추가",
                "explanation": "베트남법에는 없는 개념이므로 오해 방지 필요"
            }
        ],
        "examples": [
            {
                "ko": "피고는 인터넷 게시판에 원고가 사기를 쳤다는 허위 사실을 게재하여 명예를 훼손했습니다.",
                "vi": "Bị cáo đã đăng thông tin sai sự thật lên diễn đàn internet rằng nguyên đơn lừa đảo, làm tổn hại danh dự.",
                "situation": "formal"
            },
            {
                "ko": "진실한 사실이라도 공익 목적이 없으면 명예훼손이 성립할 수 있습니다.",
                "vi": "Ngay cả khi là sự thật, nếu không vì mục đích công ích vẫn có thể cấu thành tội vụ khống.",
                "situation": "formal"
            },
            {
                "ko": "이 발언은 구체적 사실 적시가 아닌 의견 표명이므로 명예훼손에 해당하지 않습니다.",
                "vi": "Phát ngôn này là bày tỏ ý kiến, không phải nêu sự việc cụ thể nên không cấu thành vụ khống.",
                "situation": "formal"
            }
        ],
        "relatedTerms": ["모욕", "언론", "반론권", "사이버명예훼손"]
    },
    {
        "slug": "xuc-pham-danh-du",
        "korean": "모욕",
        "vietnamese": "Xúc phạm danh dự",
        "hanja": "侮辱",
        "hanjaReading": "侮(업신여길 모) + 辱(욕될 욕)",
        "pronunciation": "쑥팜잉주",
        "meaningKo": "사실을 적시하지 않고 추상적 판단이나 경멸적 표현으로 타인의 사회적 평가를 저하시키는 행위입니다. 통역 시 핵심 차이는 명예훼손은 '구체적 사실' 적시, 모욕은 '추상적 표현'이라는 점입니다. 예를 들어 '사기꾼'이라는 표현은 구체적 사기 행위 언급 없이 사용되면 모욕입니다. 베트남어로는 xúc phạm danh dự(명예 침해) 또는 lăng mạ(욕설)로 번역되나, 법적 맥락에서는 전자가 적절합니다. 한국은 형법상 모욕죄가 있으나 베트남은 행정처벌 수준이므로, 양국의 처벌 수위 차이를 통역 시 유의해야 합니다.",
        "meaningVi": "Hành vi dùng lời lẽ hoặc cử chỉ xúc phạm, hạ thấp danh dự, nhân phẩm của người khác mà không cần nêu sự việc cụ thể. Khác với vụ khống (phỉ báng), xúc phạm danh dự là dùng ngôn từ trừu tượng, mang tính khinh thường (ví dụ: 'đồ ngu', 'vô đạo đức') mà không đưa ra bằng chứng sự việc cụ thể.",
        "context": "형사 소송, 사이버 모욕 사건, 직장 내 괴롭힘 분쟁",
        "culturalNote": "한국은 2022년 '사이버 모욕죄' 처벌 강화 법안이 통과되어 온라인 악플(ác bình/bình luận tiêu cực)에 대한 처벌이 엄격해졌습니다. 베트남에서는 모욕 행위를 주로 '질서 위반'으로 보아 행정 벌금 수준에서 처리하며, 한국처럼 형사처벌하는 경우는 드뭅니다. 또한 유교 문화권인 양국 모두 체면과 명예를 중시하나, 한국은 법적 구제 수단이 더 발달한 반면 베트남은 공동체 내 조정을 선호하는 경향이 있습니다.",
        "commonMistakes": [
            {
                "mistake": "'모욕'을 lăng mạ로만 번역",
                "correction": "법정에서는 xúc phạm danh dự 사용",
                "explanation": "Lăng mạ는 일상 '욕설', 법률 용어는 xúc phạm danh dự"
            },
            {
                "mistake": "명예훼손과 구분 없이 같은 번역 사용",
                "correction": "모욕=추상적 표현, 명예훼손=구체적 사실",
                "explanation": "법적 구성요건이 다르므로 반드시 구분 필요"
            },
            {
                "mistake": "'사이버 모욕'을 직역",
                "correction": "Xúc phạm danh dự trên mạng 또는 bạo lực mạng",
                "explanation": "베트남에서는 '사이버 불링(bạo lực mạng)' 개념이 더 보편적"
            }
        ],
        "examples": [
            {
                "ko": "피고인이 공개 석상에서 피해자를 '쓰레기 같은 인간'이라고 한 행위는 모욕에 해당합니다.",
                "vi": "Hành vi bị cáo gọi bị hại là 'con người như rác' trước công chúng cấu thành tội xúc phạm danh dự.",
                "situation": "formal"
            },
            {
                "ko": "SNS에 악의적 댓글을 게재한 행위로 모욕죄가 성립됩니다.",
                "vi": "Đăng bình luận ác ý lên mạng xã hội cấu thành tội xúc phạm danh dự trên mạng.",
                "situation": "formal"
            },
            {
                "ko": "모욕과 명예훼손의 차이는 구체적 사실 적시 여부입니다.",
                "vi": "Sự khác biệt giữa xúc phạm danh dự và vụ khống là có hay không nêu sự việc cụ thể.",
                "situation": "formal"
            }
        ],
        "relatedTerms": ["명예훼손", "악플", "사이버불링", "언론"]
    },
    {
        "slug": "quyen-phan-hoi",
        "korean": "반론권",
        "vietnamese": "Quyền phản hồi",
        "hanja": "反論權",
        "hanjaReading": "反(돌이킬 반) + 論(논할 론) + 權(권세 권)",
        "pronunciation": "꿘판호이",
        "meaningKo": "언론 보도로 인해 피해를 입은 당사자가 같은 지면이나 방송 시간에 자신의 주장을 반박할 수 있는 권리입니다. 통역 시 주의할 점은 '정정보도청구권'(quyền yêu cầu đính chính)과 구분하는 것인데, 정정보도는 '사실 오류 수정', 반론권은 '의견 제시'라는 차이가 있습니다. 한국은 언론중재법으로 보장하며 14일 이내 청구해야 하고, 언론사는 3일 이내 게재 의무가 있습니다. 베트남에서는 이러한 제도가 덜 발달했으므로, 한국의 반론권 절차를 설명할 때 베트남 청자에게 생소한 개념임을 인지하고 부연 설명이 필요합니다.",
        "meaningVi": "Quyền của người bị tổn hại do tin bài báo chí được trả lời, phản bác lại trên cùng mặt báo hoặc thời lượng phát sóng. Khác với quyền yêu cầu đính chính (chỉ sửa sai sự thật), quyền phản hồi cho phép đưa ra ý kiến, lập trường của mình để bảo vệ danh dự.",
        "context": "언론 중재 절차, 민사 소송 전 화해 단계, 언론사와의 분쟁",
        "culturalNote": "한국은 1980년대 언론중재위원회 설립 이후 반론권 제도가 정착되어, 언론 보도 피해자가 법원 소송 전에 중재를 통해 신속히 구제받을 수 있습니다. 특히 인터넷 언론의 발달로 온라인 매체에 대한 반론권 행사가 증가하고 있습니다. 베트남은 국가가 언론을 통제하므로 개인의 반론권 행사보다는 언론사 자체의 '자기 정정' 또는 상급 기관의 시정 명령이 일반적입니다. 따라서 한국의 반론권을 설명할 때는 '개인이 언론에 맞서는 권리'라는 개념 자체가 베트남 청자에게 새로울 수 있음을 고려해야 합니다.",
        "commonMistakes": [
            {
                "mistake": "'반론권'을 quyền đính chính으로 번역",
                "correction": "Quyền phản hồi (반론) vs. quyền đính chính (정정)",
                "explanation": "반론은 '의견 제시', 정정은 '사실 수정'으로 법적 효과가 다름"
            },
            {
                "mistake": "베트남에도 같은 제도가 있다고 가정",
                "correction": "한국 고유 제도임을 설명 후 베트남식 구제 방법 비교",
                "explanation": "베트남은 언론중재위원회 같은 독립 기구가 없음"
            },
            {
                "mistake": "반론권 행사 절차를 생략하고 번역",
                "correction": "'14일 청구 기한, 3일 게재 의무' 등 구체적 절차 전달",
                "explanation": "법적 효력을 위해 절차 요건이 중요함"
            }
        ],
        "examples": [
            {
                "ko": "피해자는 보도일로부터 14일 이내에 반론권을 행사할 수 있습니다.",
                "vi": "Bị hại có thể thực hiện quyền phản hồi trong vòng 14 ngày kể từ ngày đăng bài.",
                "situation": "formal"
            },
            {
                "ko": "언론사가 반론 보도를 거부하면 언론중재위원회에 조정을 신청할 수 있습니다.",
                "vi": "Nếu cơ quan báo chí từ chối đăng bài phản hồi, có thể yêu cầu Ủy ban Trọng tài Báo chí hòa giải.",
                "situation": "formal"
            },
            {
                "ko": "반론권은 사실 관계가 아닌 의견에 대해서도 행사할 수 있습니다.",
                "vi": "Quyền phản hồi có thể thực hiện ngay cả với ý kiến, không chỉ sự việc sai sự thật.",
                "situation": "formal"
            }
        ],
        "relatedTerms": ["정정보도청구권", "언론중재", "언론", "명예훼손"]
    },
    {
        "slug": "bao-ve-nguon-tin",
        "korean": "취재원보호",
        "vietnamese": "Bảo vệ nguồn tin",
        "hanja": "取材源保護",
        "hanjaReading": "取(취할 취) + 材(재목 재) + 源(근원 원) + 保(지킬 보) + 護(도울 호)",
        "pronunciation": "바오베응언틴",
        "meaningKo": "언론인이 취재 과정에서 얻은 정보 제공자의 신원을 공개하지 않을 권리로, 언론의 자유를 보장하기 위한 핵심 제도입니다. 통역 시 중요한 점은 '취재원'(nguồn tin)과 '정보원'(người cung cấp thông tin)을 구분하는 것으로, 법적 맥락에서는 전자가 적절합니다. 한국은 형사소송법과 언론중재법으로 취재원 보호를 명시하나, 법원은 공익과의 비교형량으로 공개 명령을 내릴 수 있습니다. 베트남은 국가 통제형 언론 구조상 취재원 보호 개념이 약하므로, 한국의 제도를 설명할 때 '언론인의 독립성 보장 장치'임을 강조해야 합니다.",
        "meaningVi": "Quyền của nhà báo không tiết lộ danh tính người cung cấp thông tin trong quá trình thu thập tin bài. Đây là chế độ quan trọng để bảo đảm tự do báo chí, giúp nguồn tin an tâm cung cấp thông tin mà không lo bị trả thù hoặc truy cứu. Tuy nhiên, tòa án có thể yêu cầu tiết lộ nếu xét thấy lợi ích công cộng lớn hơn.",
        "context": "형사 재판에서 증인 신문, 언론 관련 소송, 언론 윤리 심의",
        "culturalNote": "한국은 1990년대 이후 탐사 보도 저널리즘이 발달하면서 취재원 보호가 언론의 생명선으로 자리잡았으나, 동시에 허위 사실 유포 시 취재원 보호를 악용하는 사례도 증가했습니다. 베트남은 언론이 당과 국가의 정책 홍보 수단으로 기능하므로, '비공개 취재원을 통한 폭로 기사'보다는 공식 발표를 전달하는 보도가 주류입니다. 따라서 한국식 탐사 보도와 취재원 보호 개념을 베트남 청자에게 설명할 때는 언론의 역할 차이를 먼저 이해시켜야 합니다.",
        "commonMistakes": [
            {
                "mistake": "'취재원'을 người cung cấp thông tin으로만 번역",
                "correction": "Nguồn tin (법률 용어) 사용",
                "explanation": "Người cung cấp thông tin은 일반 '정보 제공자', nguồn tin이 언론 전문 용어"
            },
            {
                "mistake": "취재원 보호가 절대적이라고 설명",
                "correction": "'법원의 공개 명령 가능성' 함께 전달",
                "explanation": "공익과의 형량으로 예외 인정되므로 오해 방지 필요"
            },
            {
                "mistake": "베트남에도 같은 제도가 있다고 가정",
                "correction": "한국의 독립 언론 환경에서만 의미 있는 제도임을 설명",
                "explanation": "베트남의 언론 구조상 생소한 개념일 수 있음"
            }
        ],
        "examples": [
            {
                "ko": "기자는 법정에서 취재원 보호를 이유로 증언을 거부할 수 있습니다.",
                "vi": "Phóng viên có thể từ chối làm chứng tại tòa vì lý do bảo vệ nguồn tin.",
                "situation": "formal"
            },
            {
                "ko": "취재원의 신원이 공개되면 향후 언론 활동에 심각한 위축 효과가 발생합니다.",
                "vi": "Nếu tiết lộ danh tính nguồn tin, sẽ gây hiệu ứng co cụm nghiêm trọng cho hoạt động báo chí trong tương lai.",
                "situation": "formal"
            },
            {
                "ko": "법원은 국가 안보를 이유로 취재원 공개를 명령했습니다.",
                "vi": "Tòa án đã ra lệnh tiết lộ nguồn tin vì lý do an ninh quốc gia.",
                "situation": "formal"
            }
        ],
        "relatedTerms": ["언론자유", "증언거부권", "언론", "탐사보도"]
    },
    {
        "slug": "kiem-duyet",
        "korean": "검열",
        "vietnamese": "Kiểm duyệt",
        "hanja": "檢閱",
        "hanjaReading": "檢(조사할 검) + 閱(볼 열)",
        "pronunciation": "끼엠주옛",
        "meaningKo": "국가나 권력 기관이 출판물이나 방송 내용을 사전에 심사하여 특정 내용의 표현을 금지하거나 삭제하는 행위입니다. 통역 시 핵심은 '사전 검열'(kiểm duyệt trước)과 '사후 규제'(quy định sau)를 구분하는 것으로, 헌법상 금지되는 것은 사전 검열입니다. 한국은 헌법 제21조 제2항으로 검열을 금지하지만, 영화 등급 분류나 청소년 유해물 차단은 검열이 아닌 '사후 규제'로 봅니다. 베트남은 사회주의 국가로 당과 국가 이익에 반하는 내용에 대한 사전 검열이 합법적이므로, 양국의 검열 개념이 정반대임을 통역 시 명확히 구분해야 합니다.",
        "meaningVi": "Hành vi nhà nước hoặc cơ quan có thẩm quyền xem xét trước nội dung xuất bản phẩm, phát sóng để cấm hoặc xóa bỏ những phần không phù hợp. Tại Việt Nam, kiểm duyệt được thực hiện hợp pháp đối với nội dung chống phá Đảng, Nhà nước, trái thuần phong mỹ tục. Tại Hàn Quốc, kiểm duyệt trước bị cấm theo Hiến pháp, chỉ có quy định sau khi xuất bản.",
        "context": "헌법 소송, 출판·방송 규제 사건, 표현의 자유 관련 논쟁",
        "culturalNote": "한국은 군사독재 시절 '사전 검열'로 언론·출판의 자유가 심각하게 침해받은 역사가 있어, 현재 헌법으로 검열을 엄격히 금지합니다. 다만 영화는 '사전 등급 분류'를 하는데, 이는 검열이 아니라는 헌법재판소 판례가 있습니다. 베트남은 공산당이 언론·출판을 통제하는 것이 합법이므로, '검열'이라는 단어 자체가 부정적 의미가 아닙니다. 통역 시 한국 화자가 '검열 금지'를 언급하면 베트남 청자에게는 이해하기 어려운 개념일 수 있으므로, '사전 심사 없는 자유 출판 제도'로 부연 설명이 필요합니다.",
        "commonMistakes": [
            {
                "mistake": "한국의 영화 등급 분류를 '검열'로 번역",
                "correction": "Phân loại phim (등급 분류), kiểm duyệt은 별개",
                "explanation": "헌법상 검열 금지되므로 등급 분류는 검열이 아님"
            },
            {
                "mistake": "베트남에서 검열이 불법이라고 설명",
                "correction": "베트남은 합법적 검열 제도 존재함을 인정",
                "explanation": "양국 법체계 차이를 왜곡하지 않아야 함"
            },
            {
                "mistake": "'사전 검열'과 '사후 규제' 구분 없이 번역",
                "correction": "Kiểm duyệt trước (사전) vs. quy định sau (사후) 명확히",
                "explanation": "헌법적 허용 여부가 다르므로 구분 필수"
            }
        ],
        "examples": [
            {
                "ko": "헌법은 언론·출판에 대한 검열을 금지하고 있습니다.",
                "vi": "Hiến pháp cấm kiểm duyệt đối với báo chí và xuất bản.",
                "situation": "formal"
            },
            {
                "ko": "이 조치는 사후 규제이지 사전 검열이 아니므로 합헌입니다.",
                "vi": "Biện pháp này là quy định sau xuất bản, không phải kiểm duyệt trước, nên hợp hiến.",
                "situation": "formal"
            },
            {
                "ko": "영화 등급 분류는 검열이 아닌 정보 제공 목적의 행정 조치입니다.",
                "vi": "Phân loại phim không phải kiểm duyệt mà là biện pháp hành chính cung cấp thông tin.",
                "situation": "formal"
            }
        ],
        "relatedTerms": ["언론자유", "표현의자유", "출판", "사전검열금지"]
    },
    {
        "slug": "giay-phep-bao-chi",
        "korean": "언론허가",
        "vietnamese": "Giấy phép báo chí",
        "hanja": "言論許可",
        "hanjaReading": "言(말씀 언) + 論(논할 론) + 許(허락할 허) + 可(옳을 가)",
        "pronunciation": "저이펩바오찌",
        "meaningKo": "신문, 잡지, 방송 등 언론사를 설립하거나 운영하기 위해 정부로부터 받아야 하는 허가입니다. 통역 시 주의할 점은 한국은 '등록제'(đăng ký), 베트남은 '허가제'(cấp phép)라는 근본적 차이입니다. 한국은 언론의 자유 보장을 위해 신고만으로 언론사를 설립할 수 있으나(등록제), 베트남은 정부의 사전 허가가 필요합니다. 따라서 '언론 허가'라는 표현 자체가 한국에서는 위헌 소지가 있으나 베트남에서는 합법적 제도이므로, 통역 시 양국의 언론 규제 철학 차이를 명확히 전달해야 합니다. 또한 '정기간행물 등록'과 '방송 허가'를 구분하여 번역해야 합니다.",
        "meaningVi": "Giấy phép do cơ quan nhà nước có thẩm quyền cấp để thành lập và hoạt động cơ quan báo chí (báo, tạp chí, đài phát thanh, truyền hình). Ở Việt Nam, mọi hoạt động báo chí đều cần xin phép trước, trong khi Hàn Quốc chỉ cần đăng ký (không cần xin phép) theo nguyên tắc tự do báo chí.",
        "context": "언론사 설립 행정 절차, 언론 규제 소송, 방송 허가 심의",
        "culturalNote": "한국은 1987년 민주화 이후 언론 자유 확대 정책으로 '허가제'에서 '등록제'로 전환하여, 정부가 언론사 설립을 사전에 차단할 수 없게 했습니다. 현재는 온라인 언론도 간단한 등록만으로 운영 가능합니다. 반면 베트남은 언론을 '당과 국가의 도구'로 보므로, 모든 언론사는 공산당 산하 기관이거나 정부 허가를 받은 조직만 가능합니다. 개인이나 사기업의 언론 설립은 원칙적으로 불가능합니다. 이러한 차이로 인해 '언론 허가'라는 용어를 통역할 때, 베트남 청자에게는 당연한 제도지만 한국 화자에게는 '언론 탄압'으로 들릴 수 있음을 유의해야 합니다.",
        "commonMistakes": [
            {
                "mistake": "한국의 '등록제'를 giấy phép으로 번역",
                "correction": "Đăng ký (등록) vs. Giấy phép (허가) 구분",
                "explanation": "등록은 신고만 하면 되지만, 허가는 승인이 필요하므로 법적 성격이 다름"
            },
            {
                "mistake": "'언론 허가'가 양국 모두 같은 제도라고 가정",
                "correction": "한국은 등록제, 베트남은 허가제임을 명시",
                "explanation": "언론 자유의 범위가 근본적으로 다름"
            },
            {
                "mistake": "신문과 방송을 같은 절차로 설명",
                "correction": "한국은 신문=등록, 방송=허가로 다름",
                "explanation": "매체별로 규제 수준이 다르므로 구분 필요"
            }
        ],
        "examples": [
            {
                "ko": "한국은 언론사 설립 시 허가가 아닌 등록제를 채택하고 있습니다.",
                "vi": "Hàn Quốc áp dụng chế độ đăng ký, không phải xin phép khi thành lập cơ quan báo chí.",
                "situation": "formal"
            },
            {
                "ko": "방송사업은 방송통신위원회의 허가를 받아야 합니다.",
                "vi": "Hoạt động phát thanh truyền hình phải được Ủy ban Truyền thông cấp phép.",
                "situation": "formal"
            },
            {
                "ko": "온라인 언론도 간단한 등록 절차만 거치면 운영할 수 있습니다.",
                "vi": "Báo chí trực tuyến chỉ cần qua thủ tục đăng ký đơn giản là có thể hoạt động.",
                "situation": "formal"
            }
        ],
        "relatedTerms": ["언론", "언론자유", "방송법", "정기간행물등록"]
    },
    {
        "slug": "quang-cao-phap-luat",
        "korean": "광고법",
        "vietnamese": "Pháp luật quảng cáo",
        "hanja": "廣告法",
        "hanjaReading": "廣(넓을 광) + 告(고할 고) + 法(법 법)",
        "pronunciation": "꽝까오팝루엇",
        "meaningKo": "상품이나 서비스의 광고 활동을 규제하여 소비자를 보호하고 공정 경쟁을 보장하기 위한 법률입니다. 통역 시 핵심은 '표시·광고의 공정화에 관한 법률'(한국), 'Luật Quảng cáo'(베트남)로 정확히 번역하는 것입니다. 특히 '허위·과장 광고'(quảng cáo gian dối, cường điệu), '비교 광고'(quảng cáo so sánh), '간접 광고'(quảng cáo gián tiếp/PPL)는 양국에서 규제 기준이 다르므로 주의가 필요합니다. 한국은 공정거래위원회, 베트남은 문화체육관광부가 광고를 규제하며, 특히 베트남은 정치·이념적으로 민감한 광고에 대한 사전 심의가 엄격합니다.",
        "meaningVi": "Pháp luật quy định hoạt động quảng cáo sản phẩm, dịch vụ nhằm bảo vệ người tiêu dùng và đảm bảo cạnh tranh công bằng. Việt Nam có Luật Quảng cáo (2012, sửa đổi 2022) quy định nội dung cấm, thời lượng, hình thức quảng cáo trên các phương tiện truyền thông. Hàn Quốc có Luật Công bằng hóa Biểu thị và Quảng cáo.",
        "context": "소비자 보호 소송, 공정거래위원회 심의, 광고주-광고사 분쟁",
        "culturalNote": "한국은 2000년대 이후 인터넷 광고와 인플루언서 마케팅이 급증하면서, '뒷광고(광고임을 숨긴 홍보)'에 대한 규제가 강화되었습니다. 특히 유튜브, 인스타그램 등에서 '#광고' 표시를 의무화했습니다. 베트남은 전통적으로 국영 방송 위주였으나, 최근 소셜미디어 광고가 증가하면서 규제가 뒤따라가지 못하는 상황입니다. 또한 베트남은 정치적 내용, 사회주의 가치관에 반하는 광고를 엄격히 금지하므로, 한국 기업이 베트남 진출 시 광고 심의에서 예상치 못한 제재를 받는 경우가 많습니다.",
        "commonMistakes": [
            {
                "mistake": "'광고법'을 luật quảng cáo로만 번역",
                "correction": "한국은 '표시광고법(Luật Công bằng hóa Biểu thị và Quảng cáo)' 정식 명칭 사용",
                "explanation": "법률 정식 명칭이 다르므로 정확한 번역 필요"
            },
            {
                "mistake": "PPL을 직역(Product Placement)",
                "correction": "Quảng cáo gián tiếp 또는 sản phẩm xuất hiện trong phim",
                "explanation": "베트남에서는 PPL이라는 약어가 덜 보편적"
            },
            {
                "mistake": "'뒷광고'를 번역 없이 사용",
                "correction": "Quảng cáo ngầm 또는 quảng cáo không ghi nhãn",
                "explanation": "한국 특유의 신조어이므로 설명 필요"
            }
        ],
        "examples": [
            {
                "ko": "허위·과장 광고로 공정거래위원회의 시정 명령을 받았습니다.",
                "vi": "Đã nhận lệnh chấn chỉnh từ Ủy ban Công bằng Thương mại do quảng cáo gian dối, cường điệu.",
                "situation": "formal"
            },
            {
                "ko": "인플루언서는 광고성 게시물에 반드시 '#광고' 표시를 해야 합니다.",
                "vi": "Người có ảnh hưởng phải ghi rõ '#광고' (quảng cáo) trong bài đăng có tính chất quảng cáo.",
                "situation": "formal"
            },
            {
                "ko": "비교 광고는 객관적 사실에 근거해야 하며 경쟁사를 비방해서는 안 됩니다.",
                "vi": "Quảng cáo so sánh phải dựa trên sự thật khách quan, không được phỉ báng đối thủ cạnh tranh.",
                "situation": "formal"
            }
        ],
        "relatedTerms": ["소비자보호법", "공정거래법", "허위광고", "언론"]
    },
    {
        "slug": "phat-thanh-truyen-hinh",
        "korean": "방송법",
        "vietnamese": "Luật Phát thanh truyền hình",
        "hanja": "放送法",
        "hanjaReading": "放(놓을 방) + 送(보낼 송) + 法(법 법)",
        "pronunciation": "팟타인쭈옌틴",
        "meaningKo": "방송의 자유와 공적 책임을 규정하고, 방송 사업의 질서 있는 발전을 도모하기 위한 법률입니다. 통역 시 핵심은 '지상파 방송'(phát thanh truyền hình mặt đất), '유료 방송'(truyền hình trả tiền), '인터넷 방송'(phát thanh trực tuyến)을 구분하는 것입니다. 한국은 방송통신위원회가 독립 규제 기관으로 기능하나, 베트남은 문화체육관광부와 정보통신부가 이중 규제하며 공산당의 선전선동부가 최종 감독합니다. 특히 '공영 방송'(đài phát thanh công cộng) 개념이 한국(KBS, MBC)과 베트남(VTV, VOV)에서 완전히 다른 의미이므로, 통역 시 '독립성' 여부를 명확히 구분해야 합니다.",
        "meaningVi": "Luật quy định về tự do và trách nhiệm công cộng của hoạt động phát thanh truyền hình, thúc đẩy sự phát triển có trật tự của ngành. Việt Nam có Luật Phát thanh truyền hình (2016), quy định mọi hoạt động phát thanh truyền hình phải phù hợp với đường lối Đảng và pháp luật Nhà nước. Hàn Quốc có Luật Phát thanh (방송법) với nguyên tắc độc lập biên tập.",
        "context": "방송 허가·재허가 절차, 방송 심의 위원회, 방송사-제작사 분쟁",
        "culturalNote": "한국은 1987년 민주화 이후 방송의 독립성과 공정성을 강조하며, 방송통신심의위원회가 사후 규제만 할 수 있습니다. 사전 검열은 헌법상 금지되어 있으며, 방송사의 편성 자율권이 보장됩니다. 반면 베트남은 모든 방송사가 국영 또는 당 산하 조직이며, 방송 내용은 당의 노선과 국가 이익에 부합해야 합니다. 예능, 드라마도 사전 심의를 받으며, 정치적으로 민감한 내용은 엄격히 통제됩니다. 따라서 한국의 '방송 자유'를 베트남식으로 통역하면 오해가 발생할 수 있으므로, '편성 자율권 보장' 수준으로 부연 설명이 필요합니다.",
        "commonMistakes": [
            {
                "mistake": "'방송법'을 luật phát thanh로만 번역",
                "correction": "Luật Phát thanh truyền hình (방송+TV 포함)",
                "explanation": "Phát thanh은 라디오만 의미할 수 있으므로 truyền hình 병기 필요"
            },
            {
                "mistake": "공영방송을 đài nhà nước로 번역",
                "correction": "Đài phát thanh công cộng (공적 방송) + '독립성' 설명",
                "explanation": "Đài nhà nước는 국영방송, 한국의 공영방송은 독립 운영"
            },
            {
                "mistake": "인터넷 방송을 phát thanh trực tuyến으로만 번역",
                "correction": "개인 방송=phát trực tiếp cá nhân, OTT=dịch vụ video theo yêu cầu",
                "explanation": "방송 유형에 따라 번역 달라져야 함"
            }
        ],
        "examples": [
            {
                "ko": "방송법은 방송의 공적 책임과 편성의 자유를 함께 보장합니다.",
                "vi": "Luật Phát thanh truyền hình vừa bảo đảm trách nhiệm công cộng, vừa bảo vệ quyền tự do biên tập.",
                "situation": "formal"
            },
            {
                "ko": "종합편성채널 사업자는 방송통신위원회의 재허가를 받아야 합니다.",
                "vi": "Doanh nghiệp kênh tổng hợp phải được Ủy ban Truyền thông cấp phép lại.",
                "situation": "formal"
            },
            {
                "ko": "유튜브 개인 방송도 일정 조건에서 방송법 적용 대상이 됩니다.",
                "vi": "Kênh cá nhân YouTube cũng có thể thuộc phạm vi điều chỉnh của Luật Phát thanh truyền hình theo điều kiện nhất định.",
                "situation": "formal"
            }
        ],
        "relatedTerms": ["언론", "언론자유", "공영방송", "OTT"]
    }
]

def main():
    """메인 실행 함수"""
    print("📋 미디어법/언론법 용어 추가 시작...")

    # JSON 파일 읽기
    try:
        with open(file_path, 'r', encoding='utf-8') as f:
            data = json.load(f)
    except FileNotFoundError:
        print(f"❌ 파일을 찾을 수 없습니다: {file_path}")
        return
    except json.JSONDecodeError as e:
        print(f"❌ JSON 파싱 오류: {e}")
        return

    # data가 리스트인지 확인
    if not isinstance(data, list):
        print(f"❌ 데이터 형식 오류: 리스트가 아닙니다 (type: {type(data)})")
        return

    print(f"✅ 기존 용어 수: {len(data)}개")

    # 중복 체크 (slug 기준)
    existing_slugs = {term.get('slug') for term in data if isinstance(term, dict)}
    print(f"🔍 기존 slug 수: {len(existing_slugs)}개")

    added_count = 0
    skipped_count = 0

    for term in new_terms:
        slug = term.get('slug')
        if slug in existing_slugs:
            print(f"⏭️  중복 건너뜀: {slug} ({term.get('korean')})")
            skipped_count += 1
            continue

        data.append(term)
        existing_slugs.add(slug)
        added_count += 1
        print(f"➕ 추가됨: {slug} ({term.get('korean')} - {term.get('vietnamese')})")

    # JSON 파일 쓰기 (UTF-8, 들여쓰기 2칸, 한글 유지)
    try:
        with open(file_path, 'w', encoding='utf-8') as f:
            json.dump(data, f, ensure_ascii=False, indent=2)
        print(f"\n✅ 저장 완료!")
        print(f"📊 최종 용어 수: {len(data)}개")
        print(f"➕ 추가된 용어: {added_count}개")
        print(f"⏭️  중복 건너뜀: {skipped_count}개")
    except Exception as e:
        print(f"❌ 파일 저장 실패: {e}")

if __name__ == "__main__":
    main()
