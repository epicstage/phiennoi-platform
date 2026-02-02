#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
행정절차/행정소송 (Administrative Procedure/Litigation) 용어 추가 스크립트
Tier S 품질 기준 준수
"""

import json
import os

# 파일 경로 설정
file_path = os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', 'data', 'terms', 'legal.json')

# 추가할 용어 데이터
new_terms = [
    {
        "slug": "thu-tuc-hanh-chinh",
        "korean": "행정절차",
        "vietnamese": "Thủ tục hành chính",
        "hanja": "行政節次",
        "hanjaReading": "行(다닐 행) 政(다스릴 정) 節(마디 절) 次(버금 차)",
        "pronunciation": "투뚝 한잉 찐",
        "meaningKo": "행정기관이 행정목적을 달성하기 위해 거치는 일련의 절차와 과정을 의미합니다. 통역 시 주의할 점은 베트남의 행정절차법(Luật Thủ tục hành chính)과 한국의 행정절차법이 구조적으로 다르다는 것입니다. 베트남은 원스톱(một cửa) 시스템을 강조하는 반면, 한국은 처분의 적법성과 절차적 권리 보장을 더 중시합니다. '절차'를 단순히 quy trình으로 번역하면 민간 업무 절차와 혼동될 수 있으므로 반드시 thủ tục hành chính으로 명확히 구분해야 합니다.",
        "meaningVi": "Quy trình và các bước mà cơ quan hành chính thực hiện để đạt được mục đích hành chính. Theo Luật Thủ tục hành chính Việt Nam, đây là trình tự các bước, thao tác mà cơ quan, tổ chức, cá nhân phải thực hiện trong quá trình giải quyết công việc với cơ quan nhà nước. Bao gồm các khâu như tiếp nhận hồ sơ, thẩm định, ra quyết định và trả kết quả.",
        "context": "행정법, 민원 처리, 인허가",
        "culturalNote": "한국은 행정절차법에서 처분의 사전통지, 의견청취, 이유제시 등 절차적 권리를 강조하며 위반 시 처분이 위법해질 수 있습니다. 베트남은 2015년 행정절차법 개정 이후 간소화와 신속성을 우선시하며 '묵시적 승인' 제도(chế độ chấp thuận mặc định)를 도입했습니다. 한국의 '행정심판'은 베트남의 'khiếu nại hành chính'와 유사하지만 독립적 위원회 운영 방식이 다릅니다.",
        "commonMistakes": [
            {
                "mistake": "quy trình hành chính",
                "correction": "thủ tục hành chính",
                "explanation": "quy trình은 일반적인 프로세스를 의미하고, thủ tục은 법적으로 정해진 절차를 의미하므로 행정법 맥락에서는 thủ tục이 정확합니다."
            },
            {
                "mistake": "절차를 'bước'로만 번역",
                "correction": "thủ tục (법적 절차 전체) vs. bước (개별 단계)",
                "explanation": "행정절차는 여러 bước로 구성되지만 전체를 지칭할 때는 thủ tục hành chính이라고 해야 법적 의미가 명확합니다."
            },
            {
                "mistake": "민원과 행정절차를 동일시",
                "correction": "민원(đơn thư) ≠ 행정절차(thủ tục hành chính)",
                "explanation": "민원은 국민이 제기하는 요청/불만이고, 행정절차는 그것을 처리하는 법적 프로세스입니다."
            }
        ],
        "examples": [
            {
                "ko": "건축허가 행정절차는 30일 이내에 완료되어야 합니다.",
                "vi": "Thủ tục hành chính cấp phép xây dựng phải hoàn thành trong vòng 30 ngày.",
                "situation": "formal"
            },
            {
                "ko": "행정절차법에 따라 처분 전에 의견청취를 해야 합니다.",
                "vi": "Theo Luật Thủ tục hành chính, phải lấy ý kiến trước khi ra quyết định hành chính.",
                "situation": "formal"
            },
            {
                "ko": "원스톱 서비스로 여러 행정절차를 한 곳에서 처리할 수 있습니다.",
                "vi": "Với dịch vụ một cửa, có thể giải quyết nhiều thủ tục hành chính tại một nơi.",
                "situation": "informal"
            }
        ],
        "relatedTerms": ["quyet-dinh-hanh-chinh", "giay-phep", "co-che-mot-cua", "kien-nghi"]
    },
    {
        "slug": "quyet-dinh-hanh-chinh",
        "korean": "행정처분",
        "vietnamese": "Quyết định hành chính",
        "hanja": "行政處分",
        "hanjaReading": "行(다닐 행) 政(다스릴 정) 處(처리할 처) 分(나눌 분)",
        "pronunciation": "꾸엣 딘 한잉 찐",
        "meaningKo": "행정청이 공권력을 행사하여 국민의 권리·의무에 직접적인 법적 효과를 발생시키는 행위를 말합니다. 통역 시 핵심은 베트남어 quyết định이 '결정'이라는 일반적 의미와 '행정처분'이라는 법적 의미를 모두 가지므로 맥락을 명확히 해야 한다는 점입니다. 한국 행정법에서는 '처분'이 취소소송의 대상이 되는 핵심 개념이지만, 베트남에서는 quyết định hành chính이 khiếu nại(이의신청)나 khởi kiện(소송)의 대상이 됩니다. 또한 한국은 '수익적 처분'과 '침익적 처분'을 구분하지만 베트남에서는 이런 분류가 덜 명확합니다.",
        "meaningVi": "Quyết định của cơ quan hành chính có thẩm quyền ban hành để điều chỉnh hành vi của cá nhân, tổ chức trong các lĩnh vực quản lý nhà nước. Quyết định hành chính có hiệu lực pháp lý bắt buộc và có thể là quyết định cấp phép, quyết định xử phạt, quyết định thu hồi, hoặc các quyết định hành chính khác ảnh hưởng đến quyền lợi của người dân và tổ chức.",
        "context": "행정법, 행정소송, 행정심판",
        "culturalNote": "한국에서는 '처분'의 취소·무효 소송이 행정소송의 중심이며, 처분이 있은 날로부터 90일 이내에 제기해야 합니다. 베트남에서는 quyết định hành chính에 불복하려면 먼저 khiếu nại(이의신청)를 거쳐야 하고, 그 결과에 불복할 때 비로소 tòa án hành chính(행정법원)에 khởi kiện(제소)할 수 있습니다. 한국은 처분청이 아닌 법원이 직접 취소할 수 있지만, 베트남은 법원이 quyết định의 위법성을 확인하면 처분청에게 철회를 명령하는 방식입니다.",
        "commonMistakes": [
            {
                "mistake": "quyết định을 '결정'으로만 번역",
                "correction": "행정처분(quyết định hành chính) vs. 일반 결정(quyết định)",
                "explanation": "법적 맥락에서는 반드시 hành chính을 붙여 행정행위임을 명확히 해야 합니다."
            },
            {
                "mistake": "처분과 명령(lệnh)을 혼동",
                "correction": "처분(quyết định hành chính)은 개별적·구체적, 명령(lệnh)은 일반적·추상적 규범",
                "explanation": "처분은 특정인에게 특정 효과를 발생시키지만, 명령은 불특정 다수에게 적용되는 규칙입니다."
            },
            {
                "mistake": "'침익적 처분'을 quyết định bất lợi로 직역",
                "correction": "quyết định hành chính bất lợi cho công dân (국민에게 불리한 행정처분)",
                "explanation": "베트남어로 '침익적'이라는 법률 용어가 없으므로 풀어서 설명해야 합니다."
            }
        ],
        "examples": [
            {
                "ko": "영업정지 행정처분에 불복하여 행정심판을 청구했습니다.",
                "vi": "Đã nộp đơn khiếu nại hành chính để phản đối quyết định đình chỉ hoạt động kinh doanh.",
                "situation": "formal"
            },
            {
                "ko": "위법한 행정처분은 취소소송을 통해 다툴 수 있습니다.",
                "vi": "Có thể khởi kiện hành chính để hủy bỏ quyết định hành chính trái pháp luật.",
                "situation": "formal"
            },
            {
                "ko": "인허가 취소 처분은 사전에 의견청취 절차를 거쳐야 합니다.",
                "vi": "Quyết định thu hồi giấy phép phải trải qua thủ tục lấy ý kiến trước.",
                "situation": "formal"
            }
        ],
        "relatedTerms": ["to-tung-hanh-chinh", "thu-tuc-hanh-chinh", "kien-nghi", "thanh-tra"]
    },
    {
        "slug": "to-tung-hanh-chinh",
        "korean": "행정소송",
        "vietnamese": "Tố tụng hành chính",
        "hanja": "行政訴訟",
        "hanjaReading": "行(다닐 행) 政(다스릴 정) 訴(호소할 소) 訟(송사할 송)",
        "pronunciation": "또 뚱 한잉 찐",
        "meaningKo": "행정청의 위법한 처분이나 부작위에 대하여 법원에 그 취소나 무효확인 또는 의무이행을 구하는 소송을 말합니다. 통역 시 가장 주의해야 할 점은 한국과 베트남의 행정소송 제도가 구조적으로 다르다는 것입니다. 한국은 취소소송·무효확인소송·부작위위법확인소송 등 유형이 다양하고 행정심판 전치주의를 일부 사건에만 적용하지만, 베트남은 원칙적으로 khiếu nại(이의신청) 절차를 먼저 거쳐야 tố tụng hành chính(행정소송)을 제기할 수 있습니다. 또한 한국은 독립된 행정법원이 없고 일반 법원에서 다루지만, 베트남은 2011년부터 tòa án hành chính(행정법원)이 별도로 설치되어 있습니다.",
        "meaningVi": "Hoạt động của Tòa án nhân dân và những người tham gia tố tụng hành chính trong việc giải quyết các vụ án hành chính nhằm bảo vệ quyền, lợi ích hợp pháp của công dân, cơ quan, tổ chức và bảo đảm việc thi hành pháp luật trong hoạt động quản lý hành chính nhà nước. Theo Luật Tố tụng hành chính 2015, công dân có thể khởi kiện quyết định hành chính, hành vi hành chính trái pháp luật sau khi đã thực hiện thủ tục khiếu nại.",
        "context": "행정법, 사법제도, 권리구제",
        "culturalNote": "한국은 처분이 있은 날로부터 90일 이내에 행정소송을 제기해야 하며(단, 정당한 사유가 있으면 1년까지 연장 가능), 집행정지 신청이 비교적 쉽게 인용됩니다. 베트남은 khiếu nại 결과를 받은 날로부터 90일 이내에 소를 제기해야 하며, 집행정지(đình chỉ thi hành)는 매우 제한적으로 인정됩니다. 한국 행정소송은 변호사 강제주의가 아니지만 베트남은 변호사 없이도 본인 소송이 더 일반적입니다. 또한 한국은 패소자 부담 원칙이지만 베트남은 소송비용(án phí) 부담 방식이 다릅니다.",
        "commonMistakes": [
            {
                "mistake": "행정소송을 kiện hành chính으로 번역",
                "correction": "tố tụng hành chính (제도/절차) vs. khởi kiện hành chính (소송 제기 행위)",
                "explanation": "tố tụng은 전체 소송 제도와 절차를 의미하고, khởi kiện은 소를 제기하는 행위입니다."
            },
            {
                "mistake": "행정심판(khiếu nại hành chính)과 행정소송을 혼동",
                "correction": "khiếu nại hành chính은 행정 내부 구제, tố tụng hành chính은 법원의 사법심사",
                "explanation": "베트남에서는 원칙적으로 khiếu nại를 먼저 거쳐야 tố tụng을 할 수 있습니다."
            },
            {
                "mistake": "'집행정지'를 tạm dừng로만 번역",
                "correction": "đình chỉ thi hành quyết định hành chính (행정처분 집행정지)",
                "explanation": "법적으로 정확한 용어는 đình chỉ thi hành이며, 단순 tạm dừng는 일시 중단의 일반적 의미입니다."
            }
        ],
        "examples": [
            {
                "ko": "건축허가 거부처분에 대해 행정소송을 제기했습니다.",
                "vi": "Đã khởi kiện hành chính đối với quyết định từ chối cấp phép xây dựng.",
                "situation": "formal"
            },
            {
                "ko": "행정소송법에 따라 집행정지 신청을 할 수 있습니다.",
                "vi": "Theo Luật Tố tụng hành chính, có thể nộp đơn yêu cầu đình chỉ thi hành quyết định hành chính.",
                "situation": "formal"
            },
            {
                "ko": "행정소송은 행정심판을 거치지 않고도 바로 제기할 수 있습니다.",
                "vi": "Tại Hàn Quốc, có thể khởi kiện hành chính mà không cần qua thủ tục khiếu nại trước.",
                "situation": "informal"
            }
        ],
        "relatedTerms": ["quyet-dinh-hanh-chinh", "kien-nghi", "thu-tuc-hanh-chinh", "thanh-tra"]
    },
    {
        "slug": "giay-phep",
        "korean": "허가",
        "vietnamese": "Giấy phép",
        "hanja": "許可",
        "hanjaReading": "許(허락할 허) 可(옳을 가)",
        "pronunciation": "저이 펩",
        "meaningKo": "법령에 의해 일반적으로 금지된 행위를 특정인에게 해제하여 적법하게 할 수 있도록 하는 행정행위를 말합니다. 통역 시 주의할 점은 '허가(giấy phép)'와 '인가(phê duyệt)', '등록(đăng ký)', '신고(báo cáo)'를 명확히 구분해야 한다는 것입니다. 한국 행정법에서 허가는 금지의 해제이고, 인가는 법률행위의 보충이며, 신고는 일정 사실을 행정청에 알리는 것입니다. 베트남에서도 giấy phép(허가증), giấy chứng nhận(증명서), đăng ký(등록)이 구분되지만, 실무에서는 giấy phép이 넓은 의미로 쓰이기도 합니다. 또한 한국의 '건축허가'는 베트남에서 giấy phép xây dựng이지만, 절차와 요건이 상당히 다릅니다.",
        "meaningVi": "Văn bản do cơ quan nhà nước có thẩm quyền cấp cho cá nhân, tổ chức để được phép thực hiện một hoạt động nhất định theo quy định của pháp luật. Giấy phép là điều kiện bắt buộc để hoạt động hợp pháp trong nhiều lĩnh vực như xây dựng, kinh doanh, y tế, giáo dục. Việc cấp giấy phép phải tuân thủ thủ tục hành chính và điều kiện do pháp luật quy định.",
        "context": "행정법, 인허가, 사업 규제",
        "culturalNote": "한국은 건축허가·영업허가 등 허가제도가 엄격하며, 허가 없이 행위하면 형사처벌 대상이 됩니다. 베트남도 giấy phép이 없으면 불법이지만, 실무에서는 사후에 보완하는 경우도 있습니다. 한국은 허가 신청 후 일정 기간 내 회신이 없으면 '묵시적 거부'로 보지만, 베트남은 2015년 행정절차법 개정 이후 일부 허가에서 '묵시적 승인(chấp thuận mặc định)' 제도를 도입했습니다. 또한 한국은 '허가취소'가 행정처분이지만, 베트남은 thu hồi giấy phép(허가 회수)이라고 합니다.",
        "commonMistakes": [
            {
                "mistake": "허가(giấy phép)와 인가(phê duyệt)를 혼동",
                "correction": "허가는 금지 해제, 인가는 법률행위 보충",
                "explanation": "건축허가는 giấy phép xây dựng이지만, 정관변경 인가는 phê duyệt sửa đổi điều lệ입니다."
            },
            {
                "mistake": "'허가증'과 '허가'를 동일시",
                "correction": "허가(hành vi cấp phép) vs. 허가증(giấy phép - 물리적 문서)",
                "explanation": "허가는 행정행위이고 허가증은 그 증빙 서류입니다."
            },
            {
                "mistake": "신고(báo cáo)를 허가로 잘못 번역",
                "correction": "신고(đăng ký báo cáo)는 허가(giấy phép)보다 간소한 절차",
                "explanation": "신고는 알리는 것이고 허가는 승인받는 것으로 법적 성격이 다릅니다."
            }
        ],
        "examples": [
            {
                "ko": "건축허가를 받지 않고 공사를 시작하면 불법입니다.",
                "vi": "Nếu bắt đầu thi công mà chưa có giấy phép xây dựng là vi phạm pháp luật.",
                "situation": "formal"
            },
            {
                "ko": "영업허가 신청 후 30일 이내에 결과를 통보받아야 합니다.",
                "vi": "Sau khi nộp hồ sơ xin giấy phép kinh doanh, phải nhận kết quả trong vòng 30 ngày.",
                "situation": "formal"
            },
            {
                "ko": "허가 조건을 위반하면 허가가 취소될 수 있습니다.",
                "vi": "Nếu vi phạm điều kiện cấp phép, giấy phép có thể bị thu hồi.",
                "situation": "informal"
            }
        ],
        "relatedTerms": ["thu-tuc-hanh-chinh", "dang-ky", "chung-nhan", "quyet-dinh-hanh-chinh"]
    },
    {
        "slug": "dang-ky",
        "korean": "등록",
        "vietnamese": "Đăng ký",
        "hanja": "登錄",
        "hanjaReading": "登(오를 등) 錄(기록할 록)",
        "pronunciation": "당 끼",
        "meaningKo": "일정한 사항을 행정청의 공적 장부에 기재하는 행위로, 권리의 발생·변경·소멸이나 일정한 사실을 공시하기 위한 행정행위입니다. 통역 시 핵심은 한국에서 '등록'은 경우에 따라 권리의 성립요건(예: 법인설립등기)이거나 대항요건(예: 부동산등기)일 수 있으며, 베트남의 đăng ký도 마찬가지지만 제도적 세부사항이 다르다는 점입니다. 한국의 '등기(đăng ký)'와 '등록(đăng ký)'은 법적으로 구분되지만 베트남어로는 둘 다 đăng ký이므로, 맥락을 통해 đăng ký doanh nghiệp(사업자등록), đăng ký bất động sản(부동산등기) 등으로 명확히 해야 합니다. 또한 '신고(báo cáo)'와도 구분이 필요합니다.",
        "meaningVi": "Việc ghi chép, lưu giữ thông tin về một sự kiện, tài sản, hoặc quyền lợi vào sổ sách chính thức của cơ quan nhà nước có thẩm quyền. Đăng ký có thể là điều kiện để quyền được thừa nhận (như đăng ký doanh nghiệp), hoặc để công khai thông tin (như đăng ký quyền sử dụng đất). Các loại đăng ký phổ biến bao gồm đăng ký kinh doanh, đăng ký kết hôn, đăng ký bất động sản, đăng ký xe cơ giới.",
        "context": "행정법, 부동산, 회사법",
        "culturalNote": "한국에서 법인은 등기를 해야 법인격이 생기고(설립등기), 부동산은 등기를 해야 제3자에게 대항할 수 있습니다(대항요건). 베트남에서도 doanh nghiệp(기업)는 đăng ký를 해야 법적 실체가 되지만, 절차가 한국보다 간소합니다. 부동산의 경우 한국은 '등기부등본(bản sao đăng ký bất động sản)'이 권리관계의 핵심 증빙이지만, 베트남은 'sổ đỏ(빨간 책)'로 불리는 giấy chứng nhận quyền sử dụng đất(토지사용권 증명서)가 더 중요합니다. 한국의 '상호등록'은 베트남의 'đăng ký tên thương mại'에 해당하지만 보호 범위가 다릅니다.",
        "commonMistakes": [
            {
                "mistake": "등록(đăng ký)과 신고(báo cáo)를 혼동",
                "correction": "등록은 공적 장부 기재, 신고는 사실 통지",
                "explanation": "사업자등록은 đăng ký kinh doanh이지만, 폐업신고는 báo cáo ngừng kinh doanh입니다."
            },
            {
                "mistake": "'등기'와 '등록'을 베트남어로 구분 없이 번역",
                "correction": "맥락으로 구분 - 부동산등기(đăng ký bất động sản), 사업자등록(đăng ký kinh doanh)",
                "explanation": "한국어에서는 법적 의미가 다르지만 베트남어로는 같은 đăng ký를 쓰므로 분야를 명시해야 합니다."
            },
            {
                "mistake": "등록증을 giấy phép(허가증)으로 잘못 번역",
                "correction": "giấy chứng nhận đăng ký (등록증명서)",
                "explanation": "등록증은 등록 사실을 증명하는 것이지 허가증과는 법적 성격이 다릅니다."
            }
        ],
        "examples": [
            {
                "ko": "법인설립등기를 완료해야 법인으로 인정받습니다.",
                "vi": "Phải hoàn thành đăng ký thành lập doanh nghiệp để được công nhận là pháp nhân.",
                "situation": "formal"
            },
            {
                "ko": "부동산 등기는 소유권 변동을 공시하는 제도입니다.",
                "vi": "Đăng ký bất động sản là chế độ công khai sự thay đổi quyền sở hữu.",
                "situation": "formal"
            },
            {
                "ko": "상호등록을 하면 동일한 상호 사용을 막을 수 있습니다.",
                "vi": "Nếu đăng ký tên thương mại, có thể ngăn người khác sử dụng tên giống nhau.",
                "situation": "informal"
            }
        ],
        "relatedTerms": ["giay-phep", "chung-nhan", "thu-tuc-hanh-chinh", "quyet-dinh-hanh-chinh"]
    },
    {
        "slug": "chung-nhan",
        "korean": "인증",
        "vietnamese": "Chứng nhận",
        "hanja": "認證",
        "hanjaReading": "認(알 인) 證(증거 증)",
        "pronunciation": "층 년",
        "meaningKo": "일정한 사실이나 법률관계의 존재를 공적으로 증명하는 행정행위를 말합니다. 통역 시 주의할 점은 한국어 '인증'이 맥락에 따라 베트남어로 chứng nhận(공적 증명), xác nhận(확인), công chứng(공증) 등으로 다르게 번역된다는 것입니다. 예를 들어 '전자서명 인증'은 chứng thực chữ ký điện tử이고, 'ISO 인증'은 chứng nhận ISO이며, '공증'은 công chứng입니다. 한국의 '자격증'은 giấy chứng nhận(인증서)이지만, '면허증'은 giấy phép(허가증)입니다. 또한 한국의 '건축물 사용승인'은 베트남의 'nghiệm thu công trình(공사 검수)'에 가깝지만 제도가 다릅니다.",
        "meaningVi": "Hành vi của cơ quan có thẩm quyền xác định và cấp văn bản chính thức về việc một sản phẩm, dịch vụ, hoặc tổ chức đáp ứng các tiêu chuẩn, quy định cụ thể. Chứng nhận có thể liên quan đến chất lượng sản phẩm (như chứng nhận ISO, chứng nhận an toàn thực phẩm), năng lực cá nhân (như chứng nhận hành nghề), hoặc tình trạng pháp lý (như chứng nhận quyền sử dụng đất).",
        "context": "행정법, 품질관리, 자격증",
        "culturalNote": "한국에서는 각종 자격증 제도가 발달해 있고 국가기술자격(chứng chỉ kỹ năng quốc gia)과 민간자격(chứng chỉ tư nhân)이 구분됩니다. 베트남도 chứng chỉ hành nghề(직업 자격증) 제도가 있지만, 한국만큼 세분화되지 않았습니다. 한국의 '사용승인(giấy chứng nhận đủ điều kiện sử dụng công trình)'은 건축물 준공 후 사용 가능 여부를 확인하는 것이지만, 베트남은 nghiệm thu(검수) 절차가 더 중요합니다. ISO 인증 등 국제 표준은 양국이 유사하게 인정하지만, 인증 기관의 신뢰도는 다를 수 있습니다.",
        "commonMistakes": [
            {
                "mistake": "인증(chứng nhận)과 공증(công chứng)을 혼동",
                "correction": "인증은 행정청의 공적 증명, 공증은 공증인의 법률행위 증명",
                "explanation": "졸업증명서는 chứng nhận tốt nghiệp이지만, 계약서 공증은 công chứng hợp đồng입니다."
            },
            {
                "mistake": "'확인(xác nhận)'과 '인증(chứng nhận)'을 구분 없이 번역",
                "correction": "확인은 사실 체크, 인증은 공식 증명서 발급",
                "explanation": "서명확인은 xác nhận chữ ký이지만, 자격인증은 chứng nhận trình độ입니다."
            },
            {
                "mistake": "자격증과 면허증을 모두 giấy chứng nhận으로 번역",
                "correction": "자격증(giấy chứng nhận/chứng chỉ), 면허증(giấy phép/bằng lái xe)",
                "explanation": "자격증은 능력을 증명하지만 면허증은 특정 행위의 허가입니다."
            }
        ],
        "examples": [
            {
                "ko": "ISO 9001 인증을 받으면 품질관리 시스템을 인정받은 것입니다.",
                "vi": "Nếu được chứng nhận ISO 9001, tức là hệ thống quản lý chất lượng được công nhận.",
                "situation": "formal"
            },
            {
                "ko": "건축물 사용승인을 받아야 입주가 가능합니다.",
                "vi": "Phải có giấy chứng nhận đủ điều kiện sử dụng công trình mới được vào ở.",
                "situation": "formal"
            },
            {
                "ko": "자격증이 있어야 해당 업무를 수행할 수 있습니다.",
                "vi": "Phải có chứng chỉ hành nghề mới được thực hiện công việc đó.",
                "situation": "informal"
            }
        ],
        "relatedTerms": ["giay-phep", "dang-ky", "thu-tuc-hanh-chinh", "thanh-tra"]
    },
    {
        "slug": "thanh-tra",
        "korean": "감사/감찰",
        "vietnamese": "Thanh tra",
        "hanja": "監査/監察",
        "hanjaReading": "監(볼 감) 査(조사할 사) / 監(볼 감) 察(살필 찰)",
        "pronunciation": "타인 짜",
        "meaningKo": "행정기관이나 공공기관의 업무 집행과 소속 공무원의 직무 수행이 법령과 규정에 적합한지를 조사하고 확인하는 활동을 말합니다. 통역 시 가장 주의해야 할 점은 한국어 '감사'와 '감찰'의 미묘한 차이를 이해하고, 베트남어 thanh tra가 두 가지를 모두 포괄한다는 것입니다. 한국에서 '감사'는 주로 업무와 회계를 점검하는 것이고, '감찰'은 공무원의 비위나 부정을 조사하는 것에 가깝습니다. 베트남의 thanh tra는 thanh tra hành chính(행정감사), thanh tra chuyên ngành(전문분야 감사) 등으로 세분되며, kiểm tra(검사)와도 구분됩니다. 또한 한국의 '감사원(Kiểm toán Nhà nước)'과 베트남의 'Thanh tra Chính phủ(정부감찰)'는 역할과 권한이 다릅니다.",
        "meaningVi": "Hoạt động của cơ quan nhà nước có thẩm quyền kiểm tra, đánh giá việc chấp hành pháp luật, thực hiện chính sách, nhiệm vụ, quyền hạn của cơ quan, tổ chức, cá nhân thuộc phạm vi quản lý. Thanh tra có thể là thanh tra hành chính (kiểm tra tuân thủ quy định hành chính) hoặc thanh tra chuyên ngành (kiểm tra theo lĩnh vực cụ thể như y tế, xây dựng, thuế). Kết quả thanh tra có thể dẫn đến kiến nghị xử lý vi phạm hoặc cải thiện công tác quản lý.",
        "context": "행정법, 공무원법, 부패 방지",
        "culturalNote": "한국은 대통령 직속 '감사원'이 중앙행정기관과 지방자치단체를 감사하고, 각 부처에도 자체 감사기구가 있습니다. 베트남은 'Thanh tra Chính phủ(정부감찰)'가 행정부 전체를 감독하며, 각 부처와 지방에도 thanh tra 조직이 있습니다. 한국의 감사원은 회계검사(kiểm toán)와 직무감찰(thanh tra kỷ luật)을 모두 하지만, 베트남은 Kiểm toán Nhà nước(국가감사원)가 회계를, Thanh tra가 행정을 담당하는 식으로 분리되어 있습니다. 한국은 감사 결과를 공개하는 것이 원칙이지만, 베트남은 공개 범위가 제한적일 수 있습니다.",
        "commonMistakes": [
            {
                "mistake": "감사(thanh tra)와 회계감사(kiểm toán)를 혼동",
                "correction": "감사(thanh tra)는 행정 전반, 회계감사(kiểm toán)는 재정",
                "explanation": "감사원의 회계검사는 kiểm toán이고, 직무감사는 thanh tra입니다."
            },
            {
                "mistake": "감사(thanh tra)와 검사(kiểm tra)를 구분 없이 사용",
                "correction": "thanh tra는 공식 조사, kiểm tra는 일상적 점검",
                "explanation": "정부감사는 thanh tra이지만, 일상적 업무 점검은 kiểm tra입니다."
            },
            {
                "mistake": "'감사 결과'를 kết quả kiểm tra로 번역",
                "correction": "kết luận thanh tra (감사 결론) 또는 kết quả thanh tra",
                "explanation": "공식 감사 결과는 kết luận thanh tra라는 법적 용어를 씁니다."
            }
        ],
        "examples": [
            {
                "ko": "감사원이 공공기관 예산 집행을 감사했습니다.",
                "vi": "Kiểm toán Nhà nước đã thanh tra việc thực hiện ngân sách của các cơ quan công.",
                "situation": "formal"
            },
            {
                "ko": "건설 현장에 대한 전문감사가 실시되었습니다.",
                "vi": "Đã thực hiện thanh tra chuyên ngành đối với công trường xây dựng.",
                "situation": "formal"
            },
            {
                "ko": "감사 결과 여러 위반 사항이 적발되었습니다.",
                "vi": "Kết luận thanh tra phát hiện nhiều hành vi vi phạm.",
                "situation": "informal"
            }
        ],
        "relatedTerms": ["quyet-dinh-hanh-chinh", "kien-nghi", "thu-tuc-hanh-chinh", "to-tung-hanh-chinh"]
    },
    {
        "slug": "kien-nghi",
        "korean": "건의/진정",
        "vietnamese": "Kiến nghị",
        "hanja": "建議/陳情",
        "hanjaReading": "建(세울 건) 議(의논할 의) / 陳(베풀 진) 情(뜻 정)",
        "pronunciation": "끼엔 응이",
        "meaningKo": "국민이 행정기관에 대하여 일정한 사항을 요청하거나 의견을 제시하는 행위를 말합니다. 한국 행정절차법상 '건의'는 행정제도나 운영에 관한 개선 의견이고, '진정'은 특정 행정작용에 대한 시정 요구에 가깝습니다. 통역 시 핵심은 베트남어 kiến nghị가 이 두 가지를 포괄하며, đơn thư(민원), khiếu nại(이의신청)와는 구분된다는 것입니다. 베트남에서 kiến nghị는 정책이나 법령 개선을 제안하는 것이고, khiếu nại는 자신의 권리가 침해되었을 때 행정기관에 구제를 요청하는 것입니다. 한국의 '민원'은 포괄적 개념이지만 베트남의 đơn thư는 더 넓은 의미로 쓰입니다. 또한 한국의 '국민신문고'와 베트남의 '접수 및 민원 처리 시스템'은 운영 방식이 다릅니다.",
        "meaningVi": "Hành vi của công dân, cơ quan, tổ chức đề xuất với cơ quan nhà nước có thẩm quyền về việc sửa đổi, bổ sung, ban hành chính sách, pháp luật hoặc biện pháp quản lý nhằm nâng cao hiệu quả hoạt động và bảo vệ quyền lợi hợp pháp. Kiến nghị khác với khiếu nại (yêu cầu giải quyết quyền lợi bị vi phạm) và tố cáo (báo cáo hành vi vi phạm pháp luật). Kiến nghị thường mang tính xây dựng và hướng tới cải thiện chung.",
        "context": "행정절차, 민원, 정책 참여",
        "culturalNote": "한국에서는 '국민신문고'를 통해 온라인으로 민원과 건의를 제출할 수 있고, 답변 기한(14일)이 법으로 정해져 있습니다. 베트남도 온라인 민원 시스템이 있지만, 실무적으로는 trực tiếp(직접 방문)이나 thư tay(서면)가 여전히 많이 쓰입니다. 한국은 '민원'과 '고충민원'을 구분하고 국민권익위원회가 총괄하지만, 베트남은 tiếp công dân(민원 접수) 부서가 각 기관마다 있습니다. 또한 한국의 '행정심판'은 준사법 절차지만, 베트남의 khiếu nại는 행정 내부 구제에 가깝습니다.",
        "commonMistakes": [
            {
                "mistake": "건의(kiến nghị)와 민원(đơn thư)을 동일시",
                "correction": "건의는 제도 개선 제안, 민원은 개인적 요청 포함",
                "explanation": "정책 개선 제안은 kiến nghị이지만, 개인 문제 해결 요청은 đơn thư입니다."
            },
            {
                "mistake": "건의(kiến nghị)와 이의신청(khiếu nại)을 혼동",
                "correction": "건의는 제안, 이의신청은 권리 구제 요청",
                "explanation": "khiếu nại는 자신의 권리가 침해되었을 때 쓰지만, kiến nghị는 일반적 개선 제안입니다."
            },
            {
                "mistake": "'진정'을 khiếu nại로 번역",
                "correction": "진정(kiến nghị / đơn khiếu nại) - 맥락에 따라 다름",
                "explanation": "타인의 부당행위를 신고하는 진정은 tố cáo에 가깝고, 시정 요구는 kiến nghị입니다."
            }
        ],
        "examples": [
            {
                "ko": "행정절차 간소화에 관한 건의를 제출했습니다.",
                "vi": "Đã nộp kiến nghị về việc đơn giản hóa thủ tục hành chính.",
                "situation": "formal"
            },
            {
                "ko": "국민신문고를 통해 정책 개선을 건의할 수 있습니다.",
                "vi": "Có thể kiến nghị cải thiện chính sách qua hệ thống tiếp nhận ý kiến người dân.",
                "situation": "formal"
            },
            {
                "ko": "건의 사항에 대해 14일 이내에 답변이 와야 합니다.",
                "vi": "Phải trả lời kiến nghị trong vòng 14 ngày.",
                "situation": "informal"
            }
        ],
        "relatedTerms": ["thu-tuc-hanh-chinh", "quyet-dinh-hanh-chinh", "to-tung-hanh-chinh", "thanh-tra"]
    },
    {
        "slug": "co-che-mot-cua",
        "korean": "원스톱서비스",
        "vietnamese": "Cơ chế một cửa",
        "hanja": None,
        "hanjaReading": None,
        "pronunciation": "꺼 께 못 꾸어",
        "meaningKo": "민원인이 여러 부서를 방문하지 않고 한 곳(một cửa)에서 행정절차를 모두 처리할 수 있도록 하는 제도를 말합니다. 통역 시 주의할 점은 베트남에서 'cơ chế một cửa'가 행정개혁의 핵심 개념이며, 2015년 행정절차법 개정의 주요 내용이라는 것입니다. 한국의 '민원24'나 '정부24'와 유사하게, 베트남은 '국가 공공서비스 포털(Cổng Dịch vụ công Quốc gia)'을 통해 온라인 원스톱 서비스를 제공합니다. 그러나 실무적으로는 베트Nam이 오프라인 một cửa 창구를 더 강조하고, 한국은 온라인 통합 서비스를 우선합니다. 또한 한국의 '민원실'과 베트Nam의 'bộ phận một cửa(원스톱 부서)'는 운영 방식이 다릅니다.",
        "meaningVi": "Là hình thức tổ chức tiếp nhận hồ sơ và trả kết quả giải quyết thủ tục hành chính tại một đầu mối thống nhất của cơ quan hành chính nhà nước. Theo quy định của Chính phủ Việt Nam, cơ chế một cửa giúp người dân và doanh nghiệp chỉ cần đến một nơi duy nhất để nộp hồ sơ và nhận kết quả mà không phải chạy từ phòng ban này sang phòng ban khác. Hiện nay có thể thực hiện trực tuyến qua Cổng Dịch vụ công Quốc gia.",
        "context": "행정개혁, 민원 서비스, 전자정부",
        "culturalNote": "베트남은 2003년부터 cơ chế một cửa를 시범 운영하기 시작했고, 2015년 행정절차법에서 법제화했습니다. 각급 인민위원회(Ủy ban nhân dân)에 bộ phận một cửa를 설치하도록 의무화했으며, 특히 기업 등록과 건설 허가 등에서 효과를 보고 있습니다. 한국은 1999년 '민원24(현 정부24)'를 출범시켜 온라인 중심으로 발전했지만, 베트남은 오프라인과 온라인을 병행하며 점진적으로 디지털화하고 있습니다. 베트남의 một cửa는 '접수와 결과 교부만' 담당하고 내부 처리는 각 부서가 하는 방식이지만, 한국은 통합처리를 더 강조합니다.",
        "commonMistakes": [
            {
                "mistake": "'원스톱'을 one-stop으로 직역",
                "correction": "cơ chế một cửa (베트남 공식 용어)",
                "explanation": "베트남에서는 một cửa가 법률 용어로 정착되어 있어 이를 사용해야 합니다."
            },
            {
                "mistake": "'민원실'을 phòng tiếp dân으로만 번역",
                "correction": "bộ phận một cửa (원스톱 부서) vs. phòng tiếp dân (민원접수실)",
                "explanation": "bộ phận một cửa는 통합 처리 부서이고, phòng tiếp dân은 일반 민원 접수실입니다."
            },
            {
                "mistake": "'통합창구'와 'một cửa'를 동일시",
                "correction": "một cửa는 베트남 특유의 행정개혁 모델",
                "explanation": "단순 창구 통합이 아니라 절차 간소화를 포함한 포괄적 개혁입니다."
            }
        ],
        "examples": [
            {
                "ko": "기업 등록은 원스톱서비스로 3일 안에 완료됩니다.",
                "vi": "Đăng ký doanh nghiệp được xử lý qua cơ chế một cửa trong vòng 3 ngày.",
                "situation": "formal"
            },
            {
                "ko": "원스톱 창구에서 모든 서류를 제출하고 결과를 받을 수 있습니다.",
                "vi": "Tại bộ phận một cửa, có thể nộp tất cả hồ sơ và nhận kết quả.",
                "situation": "formal"
            },
            {
                "ko": "온라인 원스톱서비스로 집에서도 신청할 수 있습니다.",
                "vi": "Với dịch vụ công trực tuyến một cửa, có thể đăng ký ngay tại nhà.",
                "situation": "informal"
            }
        ],
        "relatedTerms": ["thu-tuc-hanh-chinh", "cai-cach-hanh-chinh", "giay-phep", "dang-ky"]
    },
    {
        "slug": "cai-cach-hanh-chinh",
        "korean": "행정개혁",
        "vietnamese": "Cải cách hành chính",
        "hanja": "行政改革",
        "hanjaReading": "行(다닐 행) 政(다스릴 정) 改(고칠 개) 革(가죽 혁)",
        "pronunciation": "까이 까익 한잉 찐",
        "meaningKo": "행정의 능률성·투명성·책임성을 높이고 국민 편의를 증진하기 위해 행정체계·제도·절차를 개선하는 일련의 활동을 말합니다. 통역 시 중요한 점은 한국과 베트남 모두 행정개혁이 국정 최우선 과제 중 하나이지만, 개혁의 초점이 다르다는 것입니다. 한국은 1990년대 이후 전자정부 구축과 규제 완화에 집중했고, 베트남은 2000년대 이후 '행정절차 간소화(đơn giản hóa thủ tục hành chính)'와 '원스톱 서비스(cơ chế một cửa)'를 강조해 왔습니다. 또한 한국은 민간위탁·책임운영기관 등 다양한 모델을 실험했지만, 베트남은 중앙집권적 구조 속에서 점진적 개혁을 추진합니다. 통역 시 '개혁(cải cách)'과 '혁신(đổi mới)'의 뉘앙스 차이도 고려해야 합니다.",
        "meaningVi": "Quá trình thay đổi tổ chức, quy trình, phương thức hoạt động của bộ máy hành chính nhà nước nhằm nâng cao hiệu lực, hiệu quả, tính minh bạch và trách nhiệm giải trình, đáp ứng yêu cầu phát triển kinh tế - xã hội và hội nhập quốc tế. Cải cách hành chính ở Việt Nam được triển khai toàn diện trên các lĩnh vực: cải cách thể chế, cải cách tổ chức bộ máy, xây dựng và nâng cao chất lượng đội ngũ cán bộ, công chức, cải cách tài chính công, và hiện đại hóa nền hành chính.",
        "context": "행정학, 공공정책, 정부 현대화",
        "culturalNote": "베트남 공산당은 1986년 '도이머이(Đổi mới - 쇄신)' 정책 이후 행정개혁을 지속적으로 추진해 왔으며, 2001년 결의안 13-NQ/TW로 본격화했습니다. 한국은 1998년 외환위기 이후 '작고 효율적인 정부'를 목표로 조직 감축과 민영화를 추진했지만, 베트남은 당-국가 체제 유지 속에서 서비스 개선과 부패 척결에 더 집중합니다. 한국의 '정부혁신'은 민간 경영 기법 도입(New Public Management)에 영향을 받았지만, 베트남은 사회주의 지향 시장경제 체제에 맞는 독자적 모델을 추구합니다. 또한 한국은 전자정부(e-Government) 세계 1위를 차지한 반면, 베트남은 아직 디지털 전환 초기 단계입니다.",
        "commonMistakes": [
            {
                "mistake": "'개혁(cải cách)'과 '혁신(đổi mới)'을 구분 없이 사용",
                "correction": "cải cách은 제도 개선, đổi mới는 근본적 쇄신",
                "explanation": "베트남에서 Đổi mới는 1986년 이후 전체 체제 변화를 의미하고, cải cách은 개별 분야 개선입니다."
            },
            {
                "mistake": "'규제개혁'을 cải cách quy định으로 직역",
                "correction": "cải cách thể chế (제도 개혁) 또는 cắt giảm thủ tục hành chính (행정절차 축소)",
                "explanation": "베트남에서는 thủ tục hành chính 간소화가 규제개혁의 핵심입니다."
            },
            {
                "mistake": "'전자정부'를 chính phủ điện tử로만 번역",
                "correction": "chính phủ điện tử (전자정부) vs. chuyển đổi số (디지털 전환)",
                "explanation": "최근 베트남은 chuyển đổi số를 더 많이 쓰며, 이는 더 포괄적인 개념입니다."
            }
        ],
        "examples": [
            {
                "ko": "행정개혁의 핵심은 절차 간소화와 투명성 제고입니다.",
                "vi": "Trọng tâm của cải cách hành chính là đơn giản hóa thủ tục và tăng cường tính minh bạch.",
                "situation": "formal"
            },
            {
                "ko": "정부는 행정개혁 평가 결과를 매년 공개합니다.",
                "vi": "Chính phủ công bố kết quả đánh giá cải cách hành chính hàng năm.",
                "situation": "formal"
            },
            {
                "ko": "디지털 전환은 행정개혁의 중요한 수단입니다.",
                "vi": "Chuyển đổi số là công cụ quan trọng của cải cách hành chính.",
                "situation": "informal"
            }
        ],
        "relatedTerms": ["thu-tuc-hanh-chinh", "co-che-mot-cua", "thanh-tra", "quyet-dinh-hanh-chinh"]
    }
]

def main():
    # legal.json 파일 읽기
    with open(file_path, 'r', encoding='utf-8') as f:
        data = json.load(f)

    # 기존 slug 목록 추출
    existing_slugs = {term['slug'] for term in data}

    # 중복 제거
    unique_new_terms = [term for term in new_terms if term['slug'] not in existing_slugs]

    print(f"총 {len(new_terms)}개 용어 중 {len(unique_new_terms)}개가 고유한 용어입니다.")

    if len(unique_new_terms) == 0:
        print("추가할 새 용어가 없습니다. (모두 중복)")
        return

    # 새 용어 추가
    data.extend(unique_new_terms)

    # 파일에 다시 쓰기
    with open(file_path, 'w', encoding='utf-8') as f:
        json.dump(data, f, ensure_ascii=False, indent=2)

    print(f"\n✅ {len(unique_new_terms)}개의 행정절차/행정소송 용어가 추가되었습니다.")
    print("\n추가된 용어:")
    for term in unique_new_terms:
        print(f"  - {term['slug']} ({term['korean']} / {term['vietnamese']})")

    print(f"\n총 용어 수: {len(data)}개")

if __name__ == "__main__":
    main()
