#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""난민/이민법 용어 추가 (v9-f)"""
import json
import os

def load_existing_terms():
    file_path = os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', 'data', 'terms', 'legal.json')
    with open(file_path, 'r', encoding='utf-8') as f:
        data = json.load(f)
    return data, file_path

def create_legal_terms():
    terms = [
        {
            "slug": "cong-nhan-nguoi-ti-nan",
            "korean": "난민인정",
            "vietnamese": "Công nhận người tị nạn",
            "hanja": "難民認定",
            "hanjaReading": "難(어려울 난) + 民(백성 민) + 認(알 인) + 定(정할 정)",
            "pronunciation": "난민인정",
            "meaningKo": "인종·종교·국적·정치적 의견 등으로 박해받을 우려가 있어 본국을 떠나 대한민국에 보호를 요청한 외국인을 난민으로 인정하는 법적 절차입니다. 통역 시 한국 난민법은 난민 신청 후 법무부가 심사하여 인정·불인정·보충적 보호를 결정하며, 난민 인정률은 약 4%로 낮고, 인정 시 체류자격·취업·사회보장 혜택을 받는다는 점을 명확히 전달해야 합니다.",
            "meaningVi": "Thủ tục pháp lý công nhận người nước ngoài rời bỏ quê hương và yêu cầu bảo vệ tại Hàn Quốc vì có nguy cơ bị ngược đãi do chủng tộc, tôn giáo, quốc tịch, quan điểm chính trị. Luật tị nạn Hàn Quốc quy định sau khi xin tị nạn, Bộ Pháp lý thẩm tra và quyết định công nhận, không công nhận, bảo vệ bổ sung, tỷ lệ công nhận khoảng 4% rất thấp, khi được công nhận sẽ nhận tư cách lưu trú, việc làm, phúc lợi xã hội.",
            "context": "난민 심사 및 지위 결정 절차에서 사용",
            "culturalNote": "한국은 2013년 아시아 최초로 난민법을 제정했으나 인정률이 매우 낮아 비판을 받습니다. 제주도 예멘 난민(2018)으로 사회적 논란이 컸으며, 심사 기간이 길어 신청자가 장기간 불안정한 상태로 머뭅니다. 베트남은 난민 발생국이었으나 현재는 난민 수용에 소극적입니다. 통역 시 한국의 낮은 인정률과 엄격한 심사를 설명해야 합니다.",
            "commonMistakes": [
                {
                    "mistake": "chấp nhận tị nạn",
                    "correction": "công nhận người tị nạn (법적 지위 부여)",
                    "explanation": "'난민 수용'은 입국 허용이며, '난민 인정'은 법적 지위 부여로 구분됩니다"
                },
                {
                    "mistake": "cấp tị nạn",
                    "correction": "công nhận người tị nạn (인정 절차)",
                    "explanation": "'난민 부여'는 모호하며 법적 인정 절차의 개념이 누락됩니다"
                },
                {
                    "mistake": "cho phép tị nạn",
                    "correction": "công nhận người tị nạn (공식 용어)",
                    "explanation": "'난민 허가'는 비공식적이며 법률 용어로 부적절합니다"
                }
            ],
            "examples": [
                {
                    "ko": "신청인은 종교적 박해를 이유로 난민 인정을 받았습니다",
                    "vi": "Người xin được công nhận người tị nạn vì lý do ngược đãi tôn giáo",
                    "situation": "formal"
                },
                {
                    "ko": "난민 신청하면 얼마나 걸려요?",
                    "vi": "Xin tị nạn mất bao lâu?",
                    "situation": "onsite"
                },
                {
                    "ko": "난민 인정률은 약 4%로 매우 낮습니다",
                    "vi": "Tỷ lệ công nhận người tị nạn khoảng 4% rất thấp",
                    "situation": "formal"
                }
            ],
            "relatedTerms": ["난민법", "난민심사", "보충적보호", "난민협약"]
        },
        {
            "slug": "tham-tra-ti-nan",
            "korean": "난민심사",
            "vietnamese": "Thẩm tra tị nạn",
            "hanja": "難民審査",
            "hanjaReading": "難(어려울 난) + 民(백성 민) + 審(살필 심) + 査(조사할 사)",
            "pronunciation": "난민심사",
            "meaningKo": "난민 신청자가 실제로 박해의 위험이 있는지를 법무부가 조사하여 난민 인정 여부를 결정하는 절차입니다. 통역 시 신청서 제출 후 면접 심사를 거쳐 평균 1~2년 소요되며, 불인정 시 이의신청과 행정소송이 가능하고, 심사 중에는 취업 제한이 있으며 생계비 지원은 제한적이라는 점을 명확히 전달해야 합니다.",
            "meaningVi": "Thủ tục Bộ Pháp lý điều tra xem người xin tị nạn có thực sự có nguy cơ bị ngược đãi hay không để quyết định có công nhận tị nạn. Sau khi nộp đơn phải qua phỏng vấn thẩm tra, trung bình mất 1-2 năm, nếu không công nhận có thể khiếu nại và kiện hành chính, trong khi thẩm tra có hạn chế việc làm và hỗ trợ sinh hoạt phí hạn chế.",
            "context": "난민 신청 및 심사 과정 안내 상황에서 사용",
            "culturalNote": "한국 난민심사는 법무부 출입국·외국인정책본부가 담당하며, 면접에서 박해 경험과 두려움을 입증해야 합니다. 통역이 제공되지만 질이 낮아 문제가 많고, 변호사 조력이 부족하여 신청자가 불리합니다. 베트남 출신 난민 신청은 극히 드뭅니다. 통역 시 심사의 까다로운 입증 기준을 설명해야 합니다.",
            "commonMistakes": [
                {
                    "mistake": "xét tị nạn",
                    "correction": "thẩm tra tị nạn (법적 절차)",
                    "explanation": "'난민 검토'는 비공식적이며 법적 심사 절차의 개념이 약화됩니다"
                },
                {
                    "mistake": "kiểm tra người tị nạn",
                    "correction": "thẩm tra tị nạn (심사)",
                    "explanation": "'난민 검사'는 물리적 검사처럼 들리며 법적 심사와 다릅니다"
                },
                {
                    "mistake": "đánh giá tị nạn",
                    "correction": "thẩm tra tị nạn (공식 용어)",
                    "explanation": "'난민 평가'는 일상 표현이며 법률 용어로 부적절합니다"
                }
            ],
            "examples": [
                {
                    "ko": "난민심사에는 평균 1~2년이 소요됩니다",
                    "vi": "Thẩm tra tị nạn trung bình mất 1-2 năm",
                    "situation": "formal"
                },
                {
                    "ko": "면접 때 무엇을 준비해야 하나요?",
                    "vi": "Phỏng vấn phải chuẩn bị gì?",
                    "situation": "onsite"
                },
                {
                    "ko": "난민심사 중에는 취업이 제한됩니다",
                    "vi": "Trong khi thẩm tra tị nạn có hạn chế việc làm",
                    "situation": "formal"
                }
            ],
            "relatedTerms": ["난민인정", "이의신청", "행정소송", "면접조사"]
        },
        {
            "slug": "bao-ve-bo-sung",
            "korean": "보충적보호",
            "vietnamese": "Bảo vệ bổ sung",
            "hanja": "補充的保護",
            "hanjaReading": "補(기울 보) + 充(채울 충) + 的(과녁 적) + 保(지킬 보) + 護(도울 호)",
            "pronunciation": "보충적보호",
            "meaningKo": "난민 요건은 충족하지 못하지만 본국 송환 시 고문·비인도적 처우·생명 위협 등의 위험이 있는 외국인에게 체류를 허가하는 제도입니다. 통역 시 난민 인정보다 요건이 완화되어 인정률이 높고(약 10%), 1년 체류허가를 받으며 갱신 가능하지만 난민만큼 광범위한 사회보장은 받지 못한다는 점을 명확히 전달해야 합니다.",
            "meaningVi": "Chế độ cho phép lưu trú người nước ngoài không đáp ứng điều kiện tị nạn nhưng nếu trả về quê có nguy cơ tra tấn, đối xử phi nhân đạo, đe dọa tính mạng. So với công nhận tị nạn điều kiện nới lỏng hơn nên tỷ lệ công nhận cao hơn (khoảng 10%), nhận giấy phép lưu trú 1 năm có thể gia hạn nhưng không được phúc lợi xã hội rộng rãi như người tị nạn.",
            "context": "보충적 보호 지위 신청 및 결정 상황에서 사용",
            "culturalNote": "한국은 2013년 난민법 제정 시 보충적 보호 제도를 도입했으며, 시리아 내전 피난민 등이 주로 이 지위를 받습니다. 난민보다 요건이 완화되어 인정률이 높지만, 사회적 인지도는 낮습니다. 베트남 출신은 극히 드뭅니다. 통역 시 난민과의 차이(요건·권리)를 명확히 설명해야 합니다.",
            "commonMistakes": [
                {
                    "mistake": "bảo vệ thêm",
                    "correction": "bảo vệ bổ sung (법적 용어)",
                    "explanation": "'추가 보호'는 일상 표현이며 법률 용어로 부적절합니다"
                },
                {
                    "mistake": "bảo vệ nhân đạo",
                    "correction": "bảo vệ bổ sung (법적 지위) vs nhân đạo (일반 개념)",
                    "explanation": "'인도적 보호'는 일반 개념이며 법적 지위로서의 보충적 보호와 다릅니다"
                },
                {
                    "mistake": "tị nạn cấp 2",
                    "correction": "bảo vệ bổ sung (난민과 별개)",
                    "explanation": "'2급 난민'처럼 들리며 난민과는 별개의 제도임을 명확히 해야 합니다"
                }
            ],
            "examples": [
                {
                    "ko": "신청인은 난민 불인정되었지만 보충적 보호 지위를 받았습니다",
                    "vi": "Người xin không được công nhận tị nạn nhưng nhận được tư cách bảo vệ bổ sung",
                    "situation": "formal"
                },
                {
                    "ko": "난민과 보충적 보호는 뭐가 다른가요?",
                    "vi": "Tị nạn và bảo vệ bổ sung khác nhau thế nào?",
                    "situation": "onsite"
                },
                {
                    "ko": "보충적 보호는 1년 체류허가를 받으며 갱신할 수 있습니다",
                    "vi": "Bảo vệ bổ sung nhận giấy phép lưu trú 1 năm và có thể gia hạn",
                    "situation": "formal"
                }
            ],
            "relatedTerms": ["난민인정", "인도적체류", "고문방지협약", "체류허가"]
        },
        {
            "slug": "luu-tru-nhan-dao",
            "korean": "인도적체류",
            "vietnamese": "Lưu trú nhân đạo",
            "hanja": "人道的滯留",
            "hanjaReading": "人(사람 인) + 道(길 도) + 的(과녁 적) + 滯(머무를 체) + 留(머무를 류)",
            "pronunciation": "인도적체류",
            "meaningKo": "난민 불인정되었지만 인도적 고려(나이·질병·체류기간 등)로 일시적 체류를 허가하는 제도입니다. 통역 시 법적 지위가 아닌 재량적 조치이며, 1년 허가 후 연장 가능하지만 불안정하고, 취업은 별도 허가가 필요하며, 사회보장 혜택은 거의 없다는 점을 명확히 전달해야 합니다. 난민이나 보충적 보호보다 권리가 제한적입니다.",
            "meaningVi": "Chế độ cho phép lưu trú tạm thời vì lý do nhân đạo (tuổi tác, bệnh tật, thời gian lưu trú) dù không được công nhận tị nạn. Không phải là tư cách pháp lý mà là biện pháp tùy ý, được phép 1 năm có thể gia hạn nhưng không ổn định, việc làm cần giấy phép riêng, hầu như không có phúc lợi xã hội. Quyền lợi hạn chế hơn tị nạn hoặc bảo vệ bổ sung.",
            "context": "인도적 체류 허가 신청 및 갱신 상황에서 사용",
            "culturalNote": "한국은 난민 불인정자 중 상당수에게 인도적 체류를 부여하며, 이는 강제송환을 피하기 위한 임시 조치입니다. 지위가 불안정하여 장기간 한국에 머물러도 정착이 어렵고, 가족 결합권도 제한됩니다. 베트남 출신은 극히 드뭅니다. 통역 시 법적 지위가 아닌 임시 조치임을 강조해야 합니다.",
            "commonMistakes": [
                {
                    "mistake": "tị nạn nhân đạo",
                    "correction": "lưu trú nhân đạo (난민 아님)",
                    "explanation": "'인도적 난민'은 난민으로 오해되며 법적 지위가 아님을 명확히 해야 합니다"
                },
                {
                    "mistake": "ở lại vì lý do nhân đạo",
                    "correction": "lưu trú nhân đạo (법적 용어)",
                    "explanation": "'인도적 이유로 체류'는 일상 표현이며 법률 용어로 부적절합니다"
                },
                {
                    "mistake": "bảo vệ tạm thời",
                    "correction": "lưu trú nhân đạo (공식 명칭)",
                    "explanation": "'임시 보호'는 의미는 맞으나 공식 명칭은 '인도적 체류'입니다"
                }
            ],
            "examples": [
                {
                    "ko": "신청인은 난민 불인정되었으나 인도적 체류 허가를 받았습니다",
                    "vi": "Người xin không được công nhận tị nạn nhưng nhận được cho phép lưu trú nhân đạo",
                    "situation": "formal"
                },
                {
                    "ko": "인도적 체류로 일할 수 있나요?",
                    "vi": "Lưu trú nhân đạo có thể làm việc không?",
                    "situation": "onsite"
                },
                {
                    "ko": "인도적 체류는 법적 지위가 아닌 재량적 조치입니다",
                    "vi": "Lưu trú nhân đạo không phải tư cách pháp lý mà là biện pháp tùy ý",
                    "situation": "formal"
                }
            ],
            "relatedTerms": ["난민불인정", "체류허가", "재량조치", "임시보호"]
        },
        {
            "slug": "khong-cong-nhan-ti-nan",
            "korean": "난민불인정",
            "vietnamese": "Không công nhận tị nạn",
            "hanja": "難民不認定",
            "hanjaReading": "難(어려울 난) + 民(백성 민) + 不(아닐 불) + 認(알 인) + 定(정할 정)",
            "pronunciation": "난민불인정",
            "meaningKo": "난민 요건을 충족하지 못하여 법무부가 난민 지위를 부여하지 않는 결정을 말합니다. 통역 시 불인정 사유는 박해 입증 부족·경제적 이주·허위 진술 등이며, 불인정 시 30일 이내 이의신청 가능, 그 후 행정소송 가능, 불인정되면 출국 명령 대상이 되지만 인도적 체류가 부여될 수 있다는 점을 명확히 전달해야 합니다.",
            "meaningVi": "Quyết định Bộ Pháp lý không cấp tư cách tị nạn vì không đáp ứng điều kiện tị nạn. Lý do không công nhận là thiếu chứng cứ ngược đãi, di cư kinh tế, khai báo gian dối, khi không công nhận có thể khiếu nại trong 30 ngày, sau đó có thể kiện hành chính, nếu không công nhận sẽ là đối tượng lệnh xuất cảnh nhưng có thể được cho lưu trú nhân đạo.",
            "context": "난민 불인정 결정 통지 및 불복 절차 안내 상황에서 사용",
            "culturalNote": "한국 난민 불인정률은 96%로 매우 높으며, 주요 사유는 박해 입증 부족입니다. 통역 품질이 낮아 면접에서 제대로 진술하지 못하는 경우가 많고, 변호사 조력이 부족합니다. 불인정 후 이의신청·행정소송을 거쳐 수년이 걸리며, 최종 불인정 시 강제퇴거 대상이 됩니다. 통역 시 불복 절차를 상세히 설명해야 합니다.",
            "commonMistakes": [
                {
                    "mistake": "từ chối tị nạn",
                    "correction": "không công nhận tị nạn (법적 결정)",
                    "explanation": "'난민 거부'는 비공식적이며 법적 결정의 개념이 약화됩니다"
                },
                {
                    "mistake": "bị loại tị nạn",
                    "correction": "không công nhận tị nạn (공식 용어)",
                    "explanation": "'난민 탈락'은 일상 표현이며 법률 용어로 부적절합니다"
                },
                {
                    "mistake": "không được tị nạn",
                    "correction": "không công nhận tị nạn (결정 명칭)",
                    "explanation": "'난민 못 받음'은 구어체이며 공식 결정 명칭이 아닙니다"
                }
            ],
            "examples": [
                {
                    "ko": "신청인은 박해 입증이 부족하여 난민 불인정 결정을 받았습니다",
                    "vi": "Người xin nhận quyết định không công nhận tị nạn vì thiếu chứng cứ ngược đãi",
                    "situation": "formal"
                },
                {
                    "ko": "난민 불인정되면 어떻게 하나요?",
                    "vi": "Nếu không công nhận tị nạn thì làm sao?",
                    "situation": "onsite"
                },
                {
                    "ko": "난민 불인정 시 30일 이내에 이의신청할 수 있습니다",
                    "vi": "Khi không công nhận tị nạn có thể khiếu nại trong 30 ngày",
                    "situation": "formal"
                }
            ],
            "relatedTerms": ["이의신청", "행정소송", "출국명령", "인도적체류"]
        },
        {
            "slug": "tai-dinh-cu-ti-nan",
            "korean": "재정착난민",
            "vietnamese": "Tái định cư tị nạn",
            "hanja": "再定着難民",
            "hanjaReading": "再(다시 재) + 定(정할 정) + 着(붙을 착) + 難(어려울 난) + 民(백성 민)",
            "pronunciation": "재정착난민",
            "meaningKo": "제3국에서 난민으로 인정받았으나 그곳에서도 정착이 어려워 한국으로 재정착하는 난민을 말합니다. 통역 시 한국은 UNHCR 추천을 받아 연간 30명 정도를 수용하며, 미얀마 카렌족 등이 주로 해당하고, 입국 전 사전 심사를 거쳐 정착 지원(주거·생계비·한국어 교육)을 받으며, 일반 난민보다 안정적이라는 점을 명확히 전달해야 합니다.",
            "meaningVi": "Người tị nạn được công nhận ở nước thứ ba nhưng khó định cư ở đó nên tái định cư tại Hàn Quốc. Hàn Quốc nhận khoảng 30 người/năm được UNHCR giới thiệu, chủ yếu là người Karen Myanmar, trải qua thẩm tra trước khi nhập cảnh và nhận hỗ trợ định cư (nhà ở, sinh hoạt phí, giáo dục tiếng Hàn), ổn định hơn tị nạn thông thường.",
            "context": "재정착 난민 수용 및 정착 지원 상황에서 사용",
            "culturalNote": "한국은 2015년부터 재정착 난민을 수용하기 시작했으며, 미얀마 카렌족이 대부분입니다. 일반 난민과 달리 사전에 심사하여 수용하므로 정착 지원이 체계적이며, 인천에 정착 지원 시설이 있습니다. 베트남은 과거 보트피플로 재정착을 경험했으나 현재는 수용하지 않습니다. 통역 시 일반 난민과의 차이를 설명해야 합니다.",
            "commonMistakes": [
                {
                    "mistake": "di cư lại",
                    "correction": "tái định cư tị nạn (난민 재정착)",
                    "explanation": "'재이주'는 일반 이주이며 난민의 특수성이 누락됩니다"
                },
                {
                    "mistake": "người tị nạn thứ ba",
                    "correction": "tái định cư tị nạn (제3국 경유)",
                    "explanation": "'제3 난민'은 모호하며 제3국을 거쳐 정착하는 개념이 불명확합니다"
                },
                {
                    "mistake": "nhập cư tị nạn",
                    "correction": "tái định cư tị nạn (재정착 강조)",
                    "explanation": "'난민 이민'은 일반 이민처럼 들리며 재정착의 특수성이 약화됩니다"
                }
            ],
            "examples": [
                {
                    "ko": "한국은 UNHCR 추천으로 연간 30명의 재정착 난민을 수용합니다",
                    "vi": "Hàn Quốc nhận 30 người tái định cư tị nạn mỗi năm theo giới thiệu UNHCR",
                    "situation": "formal"
                },
                {
                    "ko": "재정착 난민은 어떻게 신청하나요?",
                    "vi": "Tái định cư tị nạn xin thế nào?",
                    "situation": "onsite"
                },
                {
                    "ko": "재정착 난민은 입국 전에 심사를 받아 정착 지원이 체계적입니다",
                    "vi": "Tái định cư tị nạn được thẩm tra trước khi nhập cảnh nên hỗ trợ định cư có hệ thống",
                    "situation": "formal"
                }
            ],
            "relatedTerms": ["UNHCR", "정착지원", "카렌족", "제3국정착"]
        },
        {
            "slug": "lenh-xuat-canh",
            "korean": "출국명령",
            "vietnamese": "Lệnh xuất cảnh",
            "hanja": "出國命令",
            "hanjaReading": "出(날 출) + 國(나라 국) + 命(목숨 명) + 令(하여금 령)",
            "pronunciation": "출국명령",
            "meaningKo": "체류 자격이 없거나 불법체류 중인 외국인에게 일정 기간 내 자진 출국을 명령하는 행정처분입니다. 통역 시 출국 기한은 통상 30일이며, 불이행 시 강제퇴거로 전환되고, 자진 출국 시 입국 금지 기간이 짧거나 면제되지만 강제퇴거 시 5년~영구 금지되며, 난민 불인정자도 출국명령 대상이 된다는 점을 명확히 전달해야 합니다.",
            "meaningVi": "Xử phạt hành chính ra lệnh cho người nước ngoài không có tư cách lưu trú hoặc lưu trú bất hợp pháp tự nguyện xuất cảnh trong thời hạn. Thời hạn xuất cảnh thường là 30 ngày, nếu không tuân thủ sẽ chuyển thành trục xuất cưỡng chế, nếu tự nguyện xuất cảnh thời gian cấm nhập cảnh ngắn hoặc miễn nhưng nếu bị trục xuất cưỡng chế sẽ cấm 5 năm đến vĩnh viễn, người không được công nhận tị nạn cũng là đối tượng lệnh xuất cảnh.",
            "context": "출국명령 통지 및 자진 출국 안내 상황에서 사용",
            "culturalNote": "한국은 불법체류자에게 강제퇴거보다 출국명령을 우선 적용하여 자진 출국을 유도합니다. 자진 출국 시 재입국이 상대적으로 용이하나, 불이행 시 강제퇴거로 전환되어 입국 금지 기간이 길어집니다. 베트남 불법체류자가 많아 통역 시 자진 출국의 이점을 강조해야 합니다.",
            "commonMistakes": [
                {
                    "mistake": "lệnh rời khỏi",
                    "correction": "lệnh xuất cảnh (법적 명령)",
                    "explanation": "'떠나라는 명령'은 비공식적이며 법적 행정처분의 개념이 약화됩니다"
                },
                {
                    "mistake": "yêu cầu về nước",
                    "correction": "lệnh xuất cảnh (강제성)",
                    "explanation": "'귀국 요청'은 임의적처럼 들리며 법적 강제성이 누락됩니다"
                },
                {
                    "mistake": "trục xuất",
                    "correction": "lệnh xuất cảnh (자진) vs trục xuất (강제)",
                    "explanation": "'강제퇴거'는 강제 조치이며 자진 출국 명령과 구분됩니다"
                }
            ],
            "examples": [
                {
                    "ko": "불법체류자는 출국명령을 받으면 30일 이내에 자진 출국해야 합니다",
                    "vi": "Người lưu trú bất hợp pháp nhận lệnh xuất cảnh phải tự nguyện xuất cảnh trong 30 ngày",
                    "situation": "formal"
                },
                {
                    "ko": "출국명령 안 따르면 어떻게 되나요?",
                    "vi": "Nếu không theo lệnh xuất cảnh thì sao?",
                    "situation": "onsite"
                },
                {
                    "ko": "출국명령을 이행하면 입국 금지 기간이 면제되거나 단축됩니다",
                    "vi": "Nếu tuân thủ lệnh xuất cảnh thời gian cấm nhập cảnh sẽ được miễn hoặc rút ngắn",
                    "situation": "formal"
                }
            ],
            "relatedTerms": ["강제퇴거", "불법체류", "자진출국", "입국금지"]
        },
        {
            "slug": "co-so-bao-ve",
            "korean": "보호시설",
            "vietnamese": "Cơ sở bảo vệ",
            "hanja": "保護施設",
            "hanjaReading": "保(지킬 보) + 護(도울 호) + 施(베풀 시) + 設(베풀 설)",
            "pronunciation": "보호시설",
            "meaningKo": "출국명령이나 강제퇴거 대상자 중 도주 우려가 있거나 신원 확인이 필요한 외국인을 일시 수용하는 시설입니다. 통역 시 화성·여수·청주에 있으며, 수용 기간은 원칙적으로 3개월이나 연장 가능하고, 인권 침해 논란이 있으며, 변호사 접견·외부 연락이 제한적이고, 난민 신청자도 수용될 수 있다는 점을 명확히 전달해야 합니다.",
            "meaningVi": "Cơ sở tạm giam người nước ngoài là đối tượng lệnh xuất cảnh hoặc trục xuất cưỡng chế có nguy cơ trốn hoặc cần xác minh danh tính. Có ở Hwaseong, Yeosu, Cheongju, thời gian giam giữ về nguyên tắc 3 tháng nhưng có thể gia hạn, có tranh cãi vi phạm nhân quyền, hạn chế gặp luật sư và liên lạc bên ngoài, người xin tị nạn cũng có thể bị giam.",
            "context": "보호시설 수용 통지 및 인권 침해 대응 상황에서 사용",
            "culturalNote": "한국 출입국 보호시설은 사실상 구금 시설이며, 장기 수용과 인권 침해로 국제사회의 비판을 받습니다. 난민 신청자가 수용되는 경우도 많아 논란이 큽니다. 2019년 화재 사건으로 사망자가 발생하며 개선 요구가 높아졌습니다. 베트남 출신도 많이 수용됩니다. 통역 시 변호사 조력권과 외부 연락권을 강조해야 합니다.",
            "commonMistakes": [
                {
                    "mistake": "trại giam",
                    "correction": "cơ sở bảo vệ (공식 명칭)",
                    "explanation": "'수용소'는 부정적 뉘앙스이며 공식 명칭은 '보호시설'입니다"
                },
                {
                    "mistake": "nhà tạm giữ",
                    "correction": "cơ sở bảo vệ (외국인 전용)",
                    "explanation": "'유치장'은 일반 범죄자용이며 출입국 보호시설과 다릅니다"
                },
                {
                    "mistake": "trung tâm bảo vệ",
                    "correction": "cơ sở bảo vệ (법적 용어)",
                    "explanation": "'보호센터'는 비공식적이며 법률 용어로 '보호시설'이 정확합니다"
                }
            ],
            "examples": [
                {
                    "ko": "강제퇴거 대상자는 출국 전까지 보호시설에 수용될 수 있습니다",
                    "vi": "Đối tượng trục xuất cưỡng chế có thể bị giam tại cơ sở bảo vệ cho đến khi xuất cảnh",
                    "situation": "formal"
                },
                {
                    "ko": "보호시설에서 변호사 만날 수 있나요?",
                    "vi": "Trong cơ sở bảo vệ có thể gặp luật sư không?",
                    "situation": "onsite"
                },
                {
                    "ko": "보호시설 수용은 3개월이 원칙이나 연장될 수 있습니다",
                    "vi": "Giam giữ tại cơ sở bảo vệ về nguyên tắc là 3 tháng nhưng có thể gia hạn",
                    "situation": "formal"
                }
            ],
            "relatedTerms": ["강제퇴거", "출국명령", "장기수용", "인권침해"]
        },
        {
            "slug": "cong-uoc-ti-nan",
            "korean": "난민협약",
            "vietnamese": "Công ước tị nạn",
            "hanja": "難民協約",
            "hanjaReading": "難(어려울 난) + 民(백성 민) + 協(화할 협) + 約(약속할 약)",
            "pronunciation": "난민협약",
            "meaningKo": "난민의 지위와 권리를 보장하는 1951년 국제협약으로, 정식 명칭은 '난민의 지위에 관한 협약'입니다. 통역 시 한국은 1992년 가입했으며, 난민을 정의하고 강제송환 금지 원칙을 규정하며, 가입국은 난민에게 취업·교육·사회보장 등 권리를 보장해야 하고, 1967년 의정서로 지리적·시간적 제한이 철폐되었다는 점을 명확히 전달해야 합니다.",
            "meaningVi": "Công ước quốc tế năm 1951 đảm bảo tư cách và quyền lợi người tị nạn, tên chính thức là 'Công ước về tư cách người tị nạn'. Hàn Quốc gia nhập năm 1992, định nghĩa người tị nạn và quy định nguyên tắc cấm trả về cưỡng bức, nước gia nhập phải đảm bảo quyền lợi như việc làm, giáo dục, bảo hiểm xã hội cho người tị nạn, Nghị định thư 1967 bỏ giới hạn địa lý và thời gian.",
            "context": "난민 권리 보장 및 국제법 적용 상황에서 사용",
            "culturalNote": "한국은 난민협약 가입국이지만 인정률이 매우 낮아 협약 이행에 비판을 받습니다. 강제송환 금지 원칙(non-refoulement)은 지켜지지만, 난민에게 보장되어야 할 권리(사회보장 등)는 제한적입니다. 베트남은 난민협약 미가입국이며 난민 수용에 소극적입니다. 통역 시 협약의 핵심 원칙을 설명해야 합니다.",
            "commonMistakes": [
                {
                    "mistake": "hiệp định tị nạn",
                    "correction": "công ước tị nạn (국제조약)",
                    "explanation": "'협정'은 양국 간이며, '공약'은 다자간 조약으로 구분됩니다"
                },
                {
                    "mistake": "luật tị nạn quốc tế",
                    "correction": "công ước tị nạn (조약 명칭)",
                    "explanation": "'국제 난민법'은 일반 명칭이며 1951년 협약의 구체적 명칭이 아닙니다"
                },
                {
                    "mistake": "điều ước về người tị nạn",
                    "correction": "công ước tị nạn (약칭)",
                    "explanation": "'난민에 관한 조약'은 풀네임이며 약칭은 '난민협약'입니다"
                }
            ],
            "examples": [
                {
                    "ko": "난민협약은 강제송환 금지 원칙을 규정하고 있습니다",
                    "vi": "Công ước tị nạn quy định nguyên tắc cấm trả về cưỡng bức",
                    "situation": "formal"
                },
                {
                    "ko": "한국이 난민협약 가입국이면 난민을 받아야 하나요?",
                    "vi": "Nếu Hàn Quốc là nước gia nhập Công ước tị nạn thì phải nhận tị nạn à?",
                    "situation": "onsite"
                },
                {
                    "ko": "난민협약은 1951년 채택되어 1967년 의정서로 보완되었습니다",
                    "vi": "Công ước tị nạn được thông qua năm 1951 và bổ sung bằng Nghị định thư năm 1967",
                    "situation": "formal"
                }
            ],
            "relatedTerms": ["강제송환금지", "1967년의정서", "난민의권리", "UNHCR"]
        },
        {
            "slug": "ti-nan-chinh-tri",
            "korean": "망명",
            "vietnamese": "Tị nạn chính trị",
            "hanja": "亡命",
            "hanjaReading": "亡(망할 망) + 命(목숨 명)",
            "pronunciation": "망명",
            "meaningKo": "정치적 박해를 피해 외국으로 도피하여 보호를 요청하는 것을 말합니다. 통역 시 한국은 별도의 망명 제도가 없고 난민 신청 절차로 처리하며, 정치적 망명은 난민 인정 사유 중 하나이고, 북한 이탈 주민은 망명이 아닌 대한민국 국민으로 보호받으며, 외교적 망명(대사관 보호)은 국제법상 인정되지 않는다는 점을 명확히 전달해야 합니다.",
            "meaningVi": "Trốn sang nước ngoài và yêu cầu bảo vệ để tránh ngược đãi chính trị. Hàn Quốc không có chế độ tị nạn chính trị riêng mà xử lý theo thủ tục xin tị nạn, tị nạn chính trị là một trong các lý do công nhận tị nạn, người Triều Tiên đào tẩu không phải tị nạn chính trị mà được bảo vệ như công dân Hàn Quốc, tị nạn ngoại giao (bảo vệ đại sứ quán) không được công nhận theo luật quốc tế.",
            "context": "정치적 망명 신청 및 외교적 보호 요청 상황에서 사용",
            "culturalNote": "한국은 냉전 시대 소련·중국 망명자를 수용했으나 현재는 망명 제도가 없고 난민법으로 처리합니다. 정치적 박해는 난민 인정의 주요 사유이지만 입증이 까다롭습니다. 북한 이탈 주민은 망명자가 아닌 대한민국 국민으로 보호받습니다. 베트남은 과거 보트피플로 망명을 경험했습니다. 통역 시 망명과 난민의 차이를 설명해야 합니다.",
            "commonMistakes": [
                {
                    "mistake": "xin tị nạn chính trị",
                    "correction": "tị nạn chính trị (망명) = xin tị nạn vì chính trị",
                    "explanation": "'정치 난민 신청'은 절차이며 망명은 행위로 구분됩니다"
                },
                {
                    "mistake": "trốn sang nước ngoài",
                    "correction": "tị nạn chính trị (법적 개념)",
                    "explanation": "'해외 도피'는 일상 표현이며 법적 망명의 개념이 약화됩니다"
                },
                {
                    "mistake": "đào tẩu",
                    "correction": "tị nạn chính trị (보호 요청)",
                    "explanation": "'탈출'은 행위이며 외국의 보호를 요청하는 망명의 의미가 누락됩니다"
                }
            ],
            "examples": [
                {
                    "ko": "정치적 박해를 피해 한국에 망명을 요청했습니다",
                    "vi": "Đã yêu cầu tị nạn chính trị tại Hàn Quốc để tránh ngược đãi chính trị",
                    "situation": "formal"
                },
                {
                    "ko": "대사관에 들어가면 망명할 수 있나요?",
                    "vi": "Nếu vào đại sứ quán có thể tị nạn chính trị không?",
                    "situation": "onsite"
                },
                {
                    "ko": "한국은 별도의 망명 제도가 없고 난민법으로 처리합니다",
                    "vi": "Hàn Quốc không có chế độ tị nạn chính trị riêng mà xử lý theo Luật tị nạn",
                    "situation": "formal"
                }
            ],
            "relatedTerms": ["정치적박해", "난민인정", "외교적보호", "북한이탈주민"]
        }
    ]
    return terms

def main():
    data, file_path = load_existing_terms()
    existing_slugs = {t['slug'] for t in data}
    new_terms = create_legal_terms()
    filtered = [t for t in new_terms if t['slug'] not in existing_slugs]
    data.extend(filtered)
    with open(file_path, 'w', encoding='utf-8') as f:
        json.dump(data, f, ensure_ascii=False, indent=2)
    print(f"✅ Added {len(filtered)} terms (난민/이민법). Total: {len(data)}")

if __name__ == '__main__':
    main()
