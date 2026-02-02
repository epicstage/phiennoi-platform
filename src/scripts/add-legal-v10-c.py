#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""상법/회사법 심화 용어 추가 (v10-C)"""
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
            "slug": "sap-nhap-cong-ty",
            "korean": "합병",
            "vietnamese": "Sáp nhập công ty",
            "hanja": "合倂",
            "hanjaReading": "合(합할 합) 倂(아우를 병)",
            "pronunciation": "합병",
            "meaningKo": "두 개 이상의 회사가 법률상 하나의 회사로 통합되는 것을 말합니다. 통역 시 흡수합병(존속회사가 소멸회사를 흡수)과 신설합병(모든 회사가 소멸하고 새 회사 설립)을 구분하고, 합병 절차(이사회 결의, 주주총회 승인, 채권자 보호 절차, 합병등기)를 명확히 전달해야 합니다. 베트남 기업법에서도 'sáp nhập(합병)'과 'hợp nhất(통합)'을 구분하며, 한국의 흡수합병과 신설합병에 대응합니다. 통역 시 합병 시 주주와 채권자의 권리 보호, 반대주주의 주식매수청구권, 합병 대가의 적정성 등을 설명하고, 합병 무효 사유를 전달해야 합니다.",
            "meaningVi": "Việc hai hay nhiều công ty hợp nhất thành một công ty duy nhất về mặt pháp lý. Có sáp nhập (công ty tồn tại hấp thụ công ty giải thể) và hợp nhất (tất cả giải thể, thành lập công ty mới). Quy trình gồm: nghị quyết hội đồng quản trị, phê duyệt đại hội đồng cổ đông, bảo vệ chủ nợ, đăng ký sáp nhập. Cổ đông phản đối có quyền yêu cầu mua lại cổ phiếu.",
            "context": "M&A, 기업 구조조정, 그룹 계열사 통합 시",
            "culturalNote": "한국은 합병이 기업 성장 전략으로 활발히 사용되지만, 베트남은 합병 사례가 적고 절차가 복잡하여 실무상 어려움이 많습니다. 베트남에서는 합병 시 노동자 보호가 엄격하여 기존 근로계약을 승계해야 하며, 한국보다 노조의 영향력이 크므로 통역 시 노동자 협의 절차를 강조해야 합니다. 베트남은 합병 후 채무 승계 문제로 분쟁이 많으며, 통역사는 합병 전 실사(due diligence)의 중요성을 설명하고 숨겨진 부채를 확인하도록 조언해야 합니다. 한국 기업이 베트남 현지 법인을 합병할 때는 외국인 투자 비율 제한을 확인하고, 합병 후에도 투자 한도를 준수하는지 통역사가 체크해야 합니다.",
            "commonMistakes": [
                {
                    "mistake": "합병과 인수를 구분하지 않음",
                    "correction": "합병은 법인격 소멸, 인수는 법인격 유지",
                    "explanation": "합병은 회사가 사라지고 하나로 통합, 인수는 별도 회사로 존속"
                },
                {
                    "mistake": "합병은 이사회 결의만으로 가능하다고 설명",
                    "correction": "주주총회 특별결의 필수, 2/3 이상 찬성",
                    "explanation": "합병은 중대한 사항으로 주주총회 승인 필수"
                },
                {
                    "mistake": "합병 후 채무는 승계 안 된다고 설명",
                    "correction": "합병 회사는 모든 권리의무 포괄 승계",
                    "explanation": "합병은 포괄승계로 채무도 당연 승계"
                }
            ],
            "examples": [
                {
                    "ko": "A사와 B사의 합병비율은 1:0.8로 하며, A사가 존속회사가 됩니다",
                    "vi": "Tỷ lệ sáp nhập giữa công ty A và B là 1:0.8, công ty A là công ty tồn tại",
                    "situation": "formal"
                },
                {
                    "ko": "합병하면 두 회사가 하나로 합쳐져서 한 회사만 남아요",
                    "vi": "Khi sáp nhập, hai công ty hợp thành một, chỉ còn lại một công ty",
                    "situation": "informal"
                },
                {
                    "ko": "현장 법인 합병 시 직원들 근로계약 승계 여부 명확히 공지하세요",
                    "vi": "Khi sáp nhập pháp nhân tại hiện trường, hãy thông báo rõ về việc kế thừa hợp đồng lao động của nhân viên",
                    "situation": "onsite"
                }
            ],
            "relatedTerms": ["인수", "분할", "주식매수청구권", "채권자보호"]
        },
        {
            "slug": "tach-cong-ty",
            "korean": "분할",
            "vietnamese": "Tách công ty",
            "hanja": "分割",
            "hanjaReading": "分(나눌 분) 割(나눌 할)",
            "pronunciation": "분할",
            "meaningKo": "하나의 회사를 두 개 이상의 회사로 나누는 것입니다. 통역 시 단순분할(일부 사업 분리, 원회사 존속)과 분할합병(분할 후 다른 회사에 합병)을 구분하고, 분할 절차와 주주·채권자 보호 방법을 명확히 전달해야 합니다. 베트남 기업법에서도 'tách(분할)'을 인정하며, 기업 구조조정이나 사업부문 분리 시 사용됩니다. 통역 시 분할 시 재산 분배 방법, 채무 분담 기준, 분할 후 각 회사의 책임 범위를 명확히 설명하고, 분할 무효 사유를 전달해야 합니다. 베트남에서는 분할 시 세무 문제가 복잡하므로 사전 세무 자문을 권장해야 합니다.",
            "meaningVi": "Việc chia một công ty thành hai hay nhiều công ty. Có tách đơn thuần (tách một phần, công ty gốc tồn tại) và tách để sáp nhập (sau khi tách, sáp nhập vào công ty khác). Quy trình bao gồm bảo vệ cổ đông và chủ nợ. Cần phân chia rõ tài sản, phân bổ nợ, và xác định trách nhiệm của từng công ty sau tách. Vấn đề thuế phức tạp nên cần tư vấn trước.",
            "context": "기업 구조조정, 사업 분리, 상속 계획 시",
            "culturalNote": "한국은 분할을 통해 사업부문별 독립 경영을 추구하지만, 베트남은 분할 문화가 미발달하여 실무 사례가 적습니다. 베트남에서는 분할보다 별도 법인 설립을 선호하는 경향이 있으며, 통역 시 분할의 장단점(조세 혜택, 책임 분리)을 설명하여 적절한 방법을 선택하도록 조언해야 합니다. 베트남은 분할 시 채무 분담에 대한 법적 기준이 불명확하여 분쟁이 발생할 수 있으므로, 통역사는 분할 계획서에 채무 분담 기준을 명확히 기재하도록 권장해야 합니다. 한국 기업이 베트남 현지 법인을 분할할 때는 외국인 투자 승인 절차를 다시 거쳐야 할 수 있으므로 통역사가 사전에 확인해야 합니다.",
            "commonMistakes": [
                {
                    "mistake": "분할은 자산만 나누는 것이라고 설명",
                    "correction": "자산·부채·인력 모두 분할 대상",
                    "explanation": "분할은 사업 전체의 분리로 포괄적 승계"
                },
                {
                    "mistake": "분할 후 채무는 원회사만 부담한다고 설명",
                    "correction": "분할 계획서에 따라 채무도 분할 승계",
                    "explanation": "채무 분담은 분할 계획서에 명시된 대로 진행"
                },
                {
                    "mistake": "분할은 이사회만 결정하면 된다고 설명",
                    "correction": "주주총회 특별결의 필요",
                    "explanation": "분할도 중대 사항으로 주주총회 승인 필수"
                }
            ],
            "examples": [
                {
                    "ko": "A사의 IT사업부를 단순분할하여 신설 B사로 독립시킵니다",
                    "vi": "Tách bộ phận IT của công ty A để thành lập công ty B mới độc lập",
                    "situation": "formal"
                },
                {
                    "ko": "회사를 둘로 쪼개서 각각 따로 운영하는 게 분할이에요",
                    "vi": "Chia công ty làm hai để vận hành riêng biệt, đó là tách",
                    "situation": "informal"
                },
                {
                    "ko": "현장 법인 분할 시 직원들 어느 회사로 갈지 미리 공지하세요",
                    "vi": "Khi tách pháp nhân tại hiện trường, hãy thông báo trước nhân viên sẽ thuộc công ty nào",
                    "situation": "onsite"
                }
            ],
            "relatedTerms": ["합병", "물적분할", "인적분할", "분할합병"]
        },
        {
            "slug": "quyen-yeu-cau-mua-co-phieu",
            "korean": "주식매수청구권",
            "vietnamese": "Quyền yêu cầu mua cổ phiếu",
            "hanja": "株式買受請求權",
            "hanjaReading": "株(그루 주) 式(법 식) 買(살 매) 受(받을 수) 請(청할 청) 求(구할 구) 權(권세 권)",
            "pronunciation": "주식매수청구권",
            "meaningKo": "회사의 중요한 결정에 반대하는 주주가 자신의 주식을 회사에 매도하고 퇴출할 수 있는 권리입니다. 통역 시 주식매수청구권은 합병, 분할, 영업 양도 등 중대한 사항 결정 시 반대 주주를 보호하는 제도이며, 회사는 공정한 가격으로 주식을 매수해야 한다는 점을 명확히 해야 합니다. 베트남 기업법에서도 'quyền yêu cầu công ty mua lại cổ phần(회사의 주식 환매 청구권)'으로 규정하며, 주주 보호 장치로 작동합니다. 통역 시 매수가격 산정 방법, 청구 기간, 회사의 재무 상태에 따른 제약 등을 설명하고, 청구권 행사 절차를 명확히 전달해야 합니다.",
            "meaningVi": "Quyền của cổ đông phản đối các quyết định quan trọng của công ty, yêu cầu công ty mua lại cổ phiếu của mình với giá công bằng để rút lui. Đây là chế độ bảo vệ cổ đông thiểu số khi có sáp nhập, tách, chuyển nhượng doanh nghiệp. Luật doanh nghiệp Việt Nam cũng quy định quyền này. Cần chú ý cách tính giá mua, thời hạn yêu cầu, và hạn chế theo tình hình tài chính công ty.",
            "context": "합병 반대, 분할 반대, 주요 자산 매각 시",
            "culturalNote": "한국은 주식매수청구권이 법률로 명확히 보장되지만, 베트남은 실무상 행사가 어렵고 회사가 매수를 거부하는 경우가 많습니다. 베트남에서는 주식 매수가격 산정 시 분쟁이 빈번하며, 통역사는 독립적인 가치평가 전문가를 선임하여 공정한 가격을 산정하도록 조언해야 합니다. 베트남 중소기업은 재무 상태가 열악하여 주식매수청구권 행사 시 실제로 대금을 지급하지 못하는 경우가 있으므로, 통역 시 이 위험을 설명하고 대안(제3자 매각 등)을 제시해야 합니다. 한국 투자자가 베트남 합작법인에서 주식매수청구권을 행사할 때는 외국인 투자 관련 규제를 확인하고, 외환 송금 절차를 사전에 파악하도록 통역사가 조력해야 합니다.",
            "commonMistakes": [
                {
                    "mistake": "모든 주주가 언제든 매수청구 가능하다고 설명",
                    "correction": "합병 등 중대 사항 결정 시에만 청구 가능",
                    "explanation": "주식매수청구권은 특정 사유에 한정됨"
                },
                {
                    "mistake": "회사가 임의로 가격을 정한다고 설명",
                    "correction": "공정가격 산정, 협의 안 되면 법원 결정",
                    "explanation": "매수가격은 객관적 기준으로 산정해야 함"
                },
                {
                    "mistake": "찬성한 주주도 매수청구 가능하다고 설명",
                    "correction": "반대 의사 표시한 주주만 청구 가능",
                    "explanation": "찬성 주주는 매수청구권 없음"
                }
            ],
            "examples": [
                {
                    "ko": "본 합병안에 반대하며 주식매수청구권을 행사합니다. 공정가격으로 매수해 주시기 바랍니다",
                    "vi": "Tôi phản đối phương án sáp nhập này và thực hiện quyền yêu cầu mua lại cổ phiếu. Đề nghị mua lại với giá công bằng",
                    "situation": "formal"
                },
                {
                    "ko": "합병 싫으면 주식 돌려주고 나갈 수 있어요. 그게 매수청구권이에요",
                    "vi": "Nếu không thích sáp nhập, có thể trả lại cổ phiếu và ra đi. Đó là quyền yêu cầu mua lại",
                    "situation": "informal"
                },
                {
                    "ko": "주주총회에서 반대표 던지고 매수청구 기간 내에 서면 제출하세요",
                    "vi": "Bỏ phiếu phản đối tại đại hội cổ đông và nộp văn bản trong thời hạn yêu cầu mua lại",
                    "situation": "onsite"
                }
            ],
            "relatedTerms": ["합병", "분할", "공정가격", "소수주주보호"]
        },
        {
            "slug": "hoi-dong-quan-tri",
            "korean": "이사회",
            "vietnamese": "Hội đồng quản trị",
            "hanja": "理事會",
            "hanjaReading": "理(다스릴 리) 事(일 사) 會(모일 회)",
            "pronunciation": "이사회",
            "meaningKo": "회사의 업무집행을 결정하는 필수 기관으로, 이사들로 구성됩니다. 통역 시 이사회는 주요 경영 사항을 결의하고 대표이사를 선임하며, 이사는 회사에 대해 선관주의 의무와 충실의무를 부담한다는 점을 명확히 해야 합니다. 베트남 기업법에서도 'hội đồng quản trị(이사회)'는 필수 기관이며, 최소 3인 이상의 이사로 구성됩니다. 통역 시 이사회 소집 절차, 결의 요건(과반수 출석, 과반수 찬성), 이사의 책임과 의무, 이사회 의사록 작성 의무 등을 명확히 전달하고, 이사의 위법행위 시 손해배상 책임을 설명해야 합니다.",
            "meaningVi": "Cơ quan bắt buộc của công ty, quyết định việc điều hành công ty, gồm các giám đốc (thành viên hội đồng quản trị). Hội đồng quản trị ra nghị quyết về các vấn đề kinh doanh quan trọng, bầu tổng giám đốc. Giám đốc có nghĩa vụ cẩn trọng và trung thành với công ty. Luật doanh nghiệp Việt Nam quy định tối thiểu 3 thành viên. Cần tuân thủ quy trình triệu tập, yêu cầu biểu quyết (quá bán số), và lập biên bản họp.",
            "context": "회사 설립, 경영 의사결정, 지배구조 논의 시",
            "culturalNote": "한국은 이사회가 실질적 경영 결정 기관으로 작동하지만, 베트남 중소기업은 이사회가 형식적인 경우가 많고 실제로는 총사장(Tổng Giám Đốc)이 독단적으로 결정하는 경향이 있습니다. 통역 시 한국 기업에게는 베트남 합작사의 이사회 운영이 느슨할 수 있음을 설명하고, 정관과 이사회 규정을 명확히 작성하여 의사결정 절차를 제도화하도록 조언해야 합니다. 베트남에서는 이사가 겸직하는 경우가 많아 이해충돌 문제가 발생할 수 있으므로, 통역 시 이사의 충실의무와 이익충돌 회피 의무를 강조해야 합니다. 한국 기업이 베트남 법인에 이사를 파견할 때는 이사의 법적 책임(형사·민사)을 명확히 설명하고, 이사배상책임보험(D&O 보험) 가입을 권장하는 것이 좋습니다.",
            "commonMistakes": [
                {
                    "mistake": "이사회와 주주총회를 구분하지 않음",
                    "correction": "이사회는 경영 결정, 주주총회는 기본 사항 결정",
                    "explanation": "이사회는 업무집행 기관, 주주총회는 최고 의사결정 기관"
                },
                {
                    "mistake": "이사는 경영진이라 책임 없다고 설명",
                    "correction": "이사는 선관주의·충실의무 위반 시 손해배상 책임",
                    "explanation": "이사는 회사와 주주에 대해 법적 책임 부담"
                },
                {
                    "mistake": "이사회 없이 회사 운영 가능하다고 설명",
                    "correction": "주식회사는 이사회 필수, 없으면 위법",
                    "explanation": "이사회는 주식회사의 법정 필수 기관"
                }
            ],
            "examples": [
                {
                    "ko": "이사회 결의로 신규 공장 건설을 승인하고 예산 50억원을 배정합니다",
                    "vi": "Hội đồng quản trị thông qua nghị quyết phê duyệt xây dựng nhà máy mới và phân bổ ngân sách 5 tỷ won",
                    "situation": "formal"
                },
                {
                    "ko": "이사회에서 결정해야 해요. 사장 혼자 못 정해요",
                    "vi": "Phải quyết định tại hội đồng quản trị. Giám đốc không thể quyết một mình",
                    "situation": "informal"
                },
                {
                    "ko": "현장 투자 건은 이사회 승인 받아야 하니 의사록 준비하세요",
                    "vi": "Dự án đầu tư tại hiện trường cần phê duyệt hội đồng quản trị, hãy chuẩn bị biên bản",
                    "situation": "onsite"
                }
            ],
            "relatedTerms": ["주주총회", "대표이사", "사외이사", "선관주의의무"]
        },
        {
            "slug": "ban-kiem-soat",
            "korean": "감사위원회",
            "vietnamese": "Ban kiểm soát",
            "hanja": "監査委員會",
            "hanjaReading": "監(볼 감) 査(조사할 사) 委(맡길 위) 員(인원 원) 會(모일 회)",
            "pronunciation": "감사위원회",
            "meaningKo": "이사회 내에 설치하여 회사의 회계와 업무를 감사하는 위원회입니다. 통역 시 감사위원회는 이사의 직무집행을 감독하고, 위법·부당한 행위를 견제하는 기능을 하며, 일정 규모 이상 회사는 의무적으로 설치해야 한다는 점을 명확히 해야 합니다. 베트남 기업법에서는 'ban kiểm soát(감사위원회)' 또는 'kiểm soát viên(감사)'으로 규정하며, 주주총회에서 선임됩니다. 통역 시 감사위원의 자격 요건(사외이사 과반, 회계·재무 전문가 1인 이상), 권한(장부 열람, 이사회 출석), 의무(감사보고서 작성)를 명확히 전달하고, 감사의 독립성 보장 방법을 설명해야 합니다.",
            "meaningVi": "Ủy ban được thành lập trong hội đồng quản trị để kiểm soát kế toán và nghiệp vụ của công ty. Giám sát việc thi hành nhiệm vụ của giám đốc, kiềm chế hành vi vi phạm. Công ty đạt quy mô nhất định bắt buộc phải có. Luật Việt Nam quy định ban kiểm soát hoặc kiểm soát viên do đại hội đồng cổ đông bầu. Cần có chuyên gia kế toán/tài chính, có quyền xem sổ sách, tham dự hội đồng quản trị, lập báo cáo kiểm soát.",
            "context": "지배구조 개선, 회계감사, 내부통제 논의 시",
            "culturalNote": "한국은 상장사를 중심으로 감사위원회가 활성화되어 있으나, 베트남은 감사위원회가 형식적으로 운영되는 경우가 많고 실질적 견제 기능이 약합니다. 베트남에서는 감사가 대주주나 경영진의 친인척인 경우가 많아 독립성이 보장되지 않으므로, 통역 시 한국 투자자에게 감사의 독립성 확보를 위한 정관 조항 마련을 조언해야 합니다. 베트남 중소기업은 감사 선임을 생략하거나 형식적으로 임명하는 경우가 있어, 통역 시 법적 의무를 명확히 전달하고 감사 미선임 시 제재(과태료, 등록 취소)를 설명해야 합니다. 한국 기업이 베트남 합작사에서 감사위원을 파견할 때는 베트남어 능력과 현지 회계기준 이해가 필요하므로 통역사가 지원해야 합니다.",
            "commonMistakes": [
                {
                    "mistake": "감사와 감사위원회를 구분하지 않음",
                    "correction": "감사는 1-2인 개인, 감사위원회는 3인 이상 위원회",
                    "explanation": "감사위원회는 이사회 내 위원회, 감사는 별도 기관"
                },
                {
                    "mistake": "감사위원회는 자문 기능만 한다고 설명",
                    "correction": "감사위원회는 감독·견제 기능, 법적 권한 보유",
                    "explanation": "감사위원회는 이사 직무 감독 및 위법행위 시정 권한"
                },
                {
                    "mistake": "감사위원은 사내이사만 가능하다고 설명",
                    "correction": "감사위원 과반은 사외이사여야 함",
                    "explanation": "독립성 보장 위해 사외이사 과반 필수"
                }
            ],
            "examples": [
                {
                    "ko": "감사위원회는 분기별 재무제표를 검토하고 이사회에 보고합니다",
                    "vi": "Ban kiểm soát xem xét báo cáo tài chính hàng quý và báo cáo cho hội đồng quản trị",
                    "situation": "formal"
                },
                {
                    "ko": "감사위원회가 회계 장부 보자고 하면 거부 못 해요",
                    "vi": "Nếu ban kiểm soát muốn xem sổ sách kế toán thì không thể từ chối",
                    "situation": "informal"
                },
                {
                    "ko": "현장 법인에 감사위원회 설치 의무 있으니 사외이사 후보 찾으세요",
                    "vi": "Pháp nhân tại hiện trường bắt buộc có ban kiểm soát, hãy tìm ứng viên giám đốc độc lập",
                    "situation": "onsite"
                }
            ],
            "relatedTerms": ["이사회", "사외이사", "내부감사", "회계감사"]
        },
        {
            "slug": "dai-hoi-dong-co-dong",
            "korean": "주주총회",
            "vietnamese": "Đại hội đồng cổ đông",
            "hanja": "株主總會",
            "hanjaReading": "株(그루 주) 主(주인 주) 總(모을 총) 會(모일 회)",
            "pronunciation": "주주총회",
            "meaningKo": "주주 전원으로 구성되는 회사의 최고 의사결정 기관입니다. 통역 시 주주총회는 정기총회(연 1회, 결산 승인)와 임시총회(필요시 소집)로 나뉘며, 정관 변경, 이사 선임, 합병·분할 등 회사의 기본 사항을 결의한다는 점을 명확히 해야 합니다. 베트남 기업법에서도 'đại hội đồng cổ đông(주주총회)'는 최고 기관이며, 소집 절차와 결의 요건이 엄격히 규정되어 있습니다. 통역 시 소집 통지 기간(최소 15일 전), 의결정족수(보통결의 과반, 특별결의 2/3), 의결권 행사 방법(대리·서면·전자투표), 총회 의사록 작성 의무를 명확히 전달해야 합니다.",
            "meaningVi": "Cơ quan quyết định tối cao của công ty, gồm toàn bộ cổ đông. Có đại hội thường niên (mỗi năm 1 lần, phê duyệt quyết toán) và đại hội bất thường (khi cần thiết). Quyết định các vấn đề cơ bản như sửa điều lệ, bầu giám đốc, sáp nhập/tách. Luật Việt Nam quy định nghiêm ngặt về quy trình triệu tập (ít nhất trước 15 ngày), tỷ lệ biểu quyết (thường quá bán, đặc biệt 2/3), phương thức bỏ phiếu (ủy quyền, văn bản, điện tử), và lập biên bản.",
            "context": "회사 의사결정, 정관 변경, 이사 선임 시",
            "culturalNote": "한국은 주주총회가 형식화되어 안건이 대부분 원안대로 통과되지만, 베트남은 주주 간 갈등이 총회에서 분출되는 경우가 많아 통역사가 긴장감 있게 대응해야 합니다. 베트남에서는 주주총회 소집 통지를 제대로 하지 않아 총회 결의가 무효가 되는 사례가 빈번하므로, 통역 시 소집 절차 준수의 중요성을 강조하고 통지 증빙을 남기도록 조언해야 합니다. 베트남은 대리 출석이 제한적이고 본인 참석을 원칙으로 하므로, 한국 투자자가 출석하지 못할 때는 위임장 작성 요건을 명확히 확인하도록 통역사가 조력해야 합니다. 베트남에서는 주주총회 의사록이 법적 분쟁에서 결정적 증거가 되므로, 통역 시 의사록 작성의 정확성과 서명 날인의 중요성을 설명해야 합니다.",
            "commonMistakes": [
                {
                    "mistake": "주주총회는 대주주만 참석한다고 설명",
                    "correction": "모든 주주가 의결권 비율대로 참석 및 투표 가능",
                    "explanation": "주주총회는 주주 전원의 권리, 소수주주도 참석 가능"
                },
                {
                    "mistake": "주주총회 결의는 과반수면 된다고 설명",
                    "correction": "안건에 따라 보통결의·특별결의 구분",
                    "explanation": "정관 변경, 합병 등은 특별결의(2/3 이상) 필요"
                },
                {
                    "mistake": "주주총회 없이 이사회로 모든 결정 가능하다고 설명",
                    "correction": "회사 기본 사항은 반드시 주주총회 결의",
                    "explanation": "이사회는 업무집행, 주주총회는 기본 사항 결정"
                }
            ],
            "examples": [
                {
                    "ko": "정기 주주총회에서 2023년 결산을 승인하고 이익배당을 결의합니다",
                    "vi": "Đại hội đồng cổ đông thường niên phê duyệt quyết toán năm 2023 và nghị quyết phân phối lợi nhuận",
                    "situation": "formal"
                },
                {
                    "ko": "주주총회에서 손들어 표결해야 해요. 주주 전원이 주인이니까요",
                    "vi": "Phải giơ tay biểu quyết tại đại hội cổ đông. Vì tất cả cổ đông đều là chủ",
                    "situation": "informal"
                },
                {
                    "ko": "현장 법인 주주총회 소집 시 15일 전 통지 필수, 안 하면 무효됩니다",
                    "vi": "Khi triệu tập đại hội cổ đông pháp nhân tại hiện trường, bắt buộc thông báo trước 15 ngày, không thì vô hiệu",
                    "situation": "onsite"
                }
            ],
            "relatedTerms": ["이사회", "의결권", "정관", "특별결의"]
        },
        {
            "slug": "co-phieu-quy",
            "korean": "자기주식",
            "vietnamese": "Cổ phiếu quỹ",
            "hanja": "自己株式",
            "hanjaReading": "自(스스로 자) 己(몸 기) 株(그루 주) 式(법 식)",
            "pronunciation": "자기주식",
            "meaningKo": "회사가 자신의 주식을 취득하여 보유하는 것입니다. 통역 시 자기주식은 원칙적으로 금지되나 예외적으로 허용되며(주식매수청구권 행사, 주가 안정 등), 의결권이 없고 배당도 받을 수 없다는 점을 명확히 해야 합니다. 베트남 기업법에서도 'cổ phiếu quỹ(자기주식)'를 인정하지만 취득 목적과 한도가 엄격히 제한됩니다. 통역 시 자기주식 취득 사유, 취득 한도(발행주식 총수의 일정 비율), 처분 방법(소각 또는 재매각), 재무제표 표시 방법을 명확히 전달하고, 불법 자기주식 취득 시 제재를 설명해야 합니다.",
            "meaningVi": "Công ty mua lại cổ phiếu của chính mình. Nguyên tắc cấm nhưng có ngoại lệ (thực hiện quyền mua lại cổ phiếu, ổn định giá cổ phiếu). Cổ phiếu quỹ không có quyền biểu quyết, không nhận cổ tức. Luật doanh nghiệp Việt Nam cho phép nhưng hạn chế mục đích và tỷ lệ mua. Cần chú ý lý do mua, hạn mức (tỷ lệ % tổng cổ phiếu phát hành), cách xử lý (hủy hoặc bán lại), cách trình bày trên báo cáo tài chính.",
            "context": "주가 관리, 구조조정, 스톡옵션 부여 시",
            "culturalNote": "한국은 자기주식을 주가 방어 수단으로 활용하지만, 베트남은 자기주식 취득이 엄격히 제한되어 실무상 거의 사용되지 않습니다. 베트남에서는 자기주식 취득이 불법 배당이나 자본 감소로 오해받을 수 있어, 통역 시 합법적 취득 사유를 명확히 설명하고 주주총회 승인을 받도록 조언해야 합니다. 베트남은 자기주식 보유 기간 제한(1년 내 처분)이 있어 한국보다 엄격하므로, 통역 시 이 차이를 설명하고 장기 보유 시 제재를 경고해야 합니다. 한국 기업이 베트남 자회사의 자기주식 취득을 검토할 때는 현지 회계기준과 세무 처리를 사전에 확인하도록 통역사가 조력해야 합니다.",
            "commonMistakes": [
                {
                    "mistake": "회사가 자유롭게 자기주식을 살 수 있다고 설명",
                    "correction": "법정 사유에 한해 제한적 취득 가능",
                    "explanation": "자기주식 취득은 원칙 금지, 예외적 허용"
                },
                {
                    "mistake": "자기주식도 의결권이 있다고 설명",
                    "correction": "자기주식은 의결권·배당권 모두 없음",
                    "explanation": "자기주식은 주주권이 정지된 상태"
                },
                {
                    "mistake": "자기주식을 영구 보유 가능하다고 설명",
                    "correction": "베트남은 1년 내 처분 의무, 위반 시 제재",
                    "explanation": "자기주식 장기 보유는 제한됨"
                }
            ],
            "examples": [
                {
                    "ko": "주가 하락 방어를 위해 자기주식 100만주를 취득합니다",
                    "vi": "Để phòng vệ giá cổ phiếu giảm, công ty sẽ mua lại 1 triệu cổ phiếu quỹ",
                    "situation": "formal"
                },
                {
                    "ko": "회사가 자기 주식 사면 의결권 없어서 주주총회 표 수가 줄어요",
                    "vi": "Khi công ty mua cổ phiếu quỹ, không có quyền biểu quyết nên số phiếu tại đại hội giảm",
                    "situation": "informal"
                },
                {
                    "ko": "현장 법인 자기주식 취득 시 1년 내 처분 의무 있으니 계획 세우세요",
                    "vi": "Khi pháp nhân tại hiện trường mua cổ phiếu quỹ, có nghĩa vụ xử lý trong 1 năm nên hãy lập kế hoạch",
                    "situation": "onsite"
                }
            ],
            "relatedTerms": ["자본감소", "주식소각", "주가안정", "스톡옵션"]
        },
        {
            "slug": "trai-phieu-chuyen-doi",
            "korean": "전환사채",
            "vietnamese": "Trái phiếu chuyển đổi",
            "hanja": "轉換社債",
            "hanjaReading": "轉(구를 전) 換(바꿀 환) 社(모일 사) 債(빚 채)",
            "pronunciation": "전환사채",
            "meaningKo": "일정 기간 후 주식으로 전환할 수 있는 권리가 부여된 회사채입니다. 통역 시 전환사채는 채권과 주식의 성격을 동시에 가지며, 보유자는 전환권을 행사하여 주주가 될 수 있다는 점을 명확히 해야 합니다. 베트남 증권법에서도 'trái phiếu chuyển đổi(전환사채)'를 인정하며, 스타트업 투자 수단으로 활용됩니다. 통역 시 전환가격, 전환비율, 전환 청구 기간, 조기상환 조건 등을 명확히 전달하고, 전환권 행사 시 기존 주주의 지분 희석 효과를 설명해야 합니다. 베트남에서는 전환사채 발행 시 증권위원회 승인이 필요하므로 절차를 안내해야 합니다.",
            "meaningVi": "Trái phiếu công ty được trao quyền chuyển đổi thành cổ phiếu sau một thời gian nhất định. Có tính chất vừa là trái phiếu vừa là cổ phiếu, người nắm giữ có thể thực hiện quyền chuyển đổi để trở thành cổ đông. Luật chứng khoán Việt Nam cũng công nhận, được sử dụng làm công cụ đầu tư startup. Cần chú ý giá chuyển đổi, tỷ lệ chuyển đổi, thời hạn yêu cầu chuyển đổi, điều kiện mua lại sớm, và hiệu ứng pha loãng cổ phần cổ đông cũ. Phát hành cần phê duyệt của Ủy ban Chứng khoán.",
            "context": "기업 자금 조달, 투자 유치, M&A 시",
            "culturalNote": "한국은 전환사채가 스타트업과 중소기업의 주요 자금 조달 수단이지만, 베트남은 전환사채 시장이 미발달하여 실무 사례가 적습니다. 베트남에서는 전환사채보다 직접 지분 투자를 선호하는 경향이 있으며, 통역 시 전환사채의 장점(투자자는 위험 회피, 발행사는 이자 부담 경감)을 설명하여 활용을 촉진해야 합니다. 베트남은 전환사채 전환 시 기존 주주의 우선 인수권 문제로 분쟁이 발생할 수 있으므로, 통역 시 정관에 전환 절차를 명확히 규정하도록 조언해야 합니다. 한국 투자자가 베트남 기업에 전환사채를 인수할 때는 전환가격 산정 기준과 외환 리스크를 고려하도록 통역사가 설명해야 합니다.",
            "commonMistakes": [
                {
                    "mistake": "전환사채와 신주인수권부사채를 구분하지 않음",
                    "correction": "전환사채는 채권을 주식으로 전환, 신주인수권부사채는 채권 유지+신주 인수",
                    "explanation": "전환사채는 채권 소멸, 신주인수권부사채는 채권 존속"
                },
                {
                    "mistake": "전환은 언제든 가능하다고 설명",
                    "correction": "전환 청구 기간이 정해져 있음",
                    "explanation": "전환권 행사는 계약서에 명시된 기간 내에만 가능"
                },
                {
                    "mistake": "전환 시 추가 대금 없다고 설명",
                    "correction": "전환가격과 전환비율에 따라 결정",
                    "explanation": "전환가격이 액면보다 높으면 추가 납입 필요할 수 있음"
                }
            ],
            "examples": [
                {
                    "ko": "전환가격 1만원, 전환비율 1:1로 전환사채 10억원을 발행합니다",
                    "vi": "Phát hành 1 tỷ won trái phiếu chuyển đổi với giá chuyển đổi 10,000 won, tỷ lệ 1:1",
                    "situation": "formal"
                },
                {
                    "ko": "전환사채는 나중에 주식으로 바꿀 수 있는 채권이에요",
                    "vi": "Trái phiếu chuyển đổi là trái phiếu có thể đổi thành cổ phiếu sau này",
                    "situation": "informal"
                },
                {
                    "ko": "현장 법인 전환사채 발행 시 증권위 승인 필요하니 서류 준비하세요",
                    "vi": "Khi pháp nhân tại hiện trường phát hành trái phiếu chuyển đổi, cần phê duyệt Ủy ban Chứng khoán nên chuẩn bị hồ sơ",
                    "situation": "onsite"
                }
            ],
            "relatedTerms": ["신주인수권부사채", "주식", "회사채", "전환가격"]
        },
        {
            "slug": "tang-von-co-phi",
            "korean": "유상증자",
            "vietnamese": "Tăng vốn có phí",
            "hanja": "有償增資",
            "hanjaReading": "有(있을 유) 償(갚을 상) 增(더할 증) 資(재물 자)",
            "pronunciation": "유상증자",
            "meaningKo": "주주가 대가를 지급하고 신주를 인수하여 회사의 자본금을 증가시키는 것입니다. 통역 시 유상증자는 회사의 자금 조달 수단이며, 기존 주주는 지분율 유지를 위해 신주인수권을 행사할 수 있다는 점을 명확히 해야 합니다. 베트남 기업법에서도 'tăng vốn có phí(유상증자)'를 인정하며, 주주총회 결의로 진행됩니다. 통역 시 증자 가격, 배정 비율, 실권주 처리 방법, 증자 후 지분 변동을 명확히 전달하고, 소수주주의 권리 보호(우선 인수권)를 설명해야 합니다. 베트남에서는 유상증자 시 기존 주주에게 우선 배정해야 하므로 절차를 준수하도록 조언해야 합니다.",
            "meaningVi": "Cổ đông trả tiền để mua cổ phiếu mới phát hành, tăng vốn điều lệ của công ty. Là phương thức huy động vốn, cổ đông cũ có quyền ưu tiên mua để duy trì tỷ lệ sở hữu. Luật doanh nghiệp Việt Nam cho phép, quyết định tại đại hội cổ đông. Cần chú ý giá tăng vốn, tỷ lệ phân bổ, xử lý cổ phiếu bỏ quyền, biến động cổ phần sau tăng vốn, và bảo vệ quyền cổ đông thiểu số (quyền ưu tiên). Phải ưu tiên phân bổ cho cổ đông cũ.",
            "context": "자금 조달, 투자 유치, 자본 확충 시",
            "culturalNote": "한국은 유상증자가 빈번하게 이루어지지만, 베트남은 유상증자 절차가 복잡하고 시간이 오래 걸려 기업들이 선호하지 않습니다. 베트남에서는 유상증자보다 차입을 통한 자금 조달을 선호하는 경향이 있으며, 통역 시 유상증자의 장점(재무구조 개선, 이자 부담 없음)을 설명하여 활용을 촉진해야 합니다. 베트남은 유상증자 시 기존 주주의 우선 인수권이 엄격히 보장되므로, 제3자 배정 증자를 하려면 기존 주주의 인수권 포기 절차를 거쳐야 한다는 점을 통역 시 명확히 전달해야 합니다. 한국 투자자가 베트남 합작사의 유상증자에 참여할 때는 증자 가격의 적정성을 평가하고, 증자 후 지배구조 변화를 확인하도록 통역사가 조력해야 합니다.",
            "commonMistakes": [
                {
                    "mistake": "유상증자와 무상증자를 구분하지 않음",
                    "correction": "유상증자는 대가 지급, 무상증자는 무료 배정",
                    "explanation": "유상증자는 주주가 돈 내고 주식 받음, 무상은 무료"
                },
                {
                    "mistake": "유상증자는 이사회만 결정하면 된다고 설명",
                    "correction": "주주총회 특별결의 필요",
                    "explanation": "자본금 증가는 정관 변경 사항으로 주주총회 승인 필수"
                },
                {
                    "mistake": "실권주는 소멸된다고 설명",
                    "correction": "실권주는 제3자 배정 또는 이사회 처리",
                    "explanation": "인수하지 않은 주식은 회사가 재배정 가능"
                }
            ],
            "examples": [
                {
                    "ko": "1주당 5천원에 유상증자를 실시하며, 기존 주주는 지분율대로 우선 인수할 수 있습니다",
                    "vi": "Thực hiện tăng vốn có phí 5,000 won mỗi cổ phiếu, cổ đông cũ có quyền ưu tiên mua theo tỷ lệ sở hữu",
                    "situation": "formal"
                },
                {
                    "ko": "유상증자는 돈 내고 주식 사는 거예요. 공짜로 주는 무상증자와 달라요",
                    "vi": "Tăng vốn có phí là trả tiền mua cổ phiếu. Khác với tăng vốn vô phí là cho không",
                    "situation": "informal"
                },
                {
                    "ko": "현장 법인 유상증자 시 기존 주주 우선권 공지 필수예요",
                    "vi": "Khi pháp nhân tại hiện trường tăng vốn có phí, bắt buộc phải thông báo quyền ưu tiên cho cổ đông cũ",
                    "situation": "onsite"
                }
            ],
            "relatedTerms": ["무상증자", "신주인수권", "실권주", "자본금"]
        },
        {
            "slug": "tiep-quan-thuong-mai",
            "korean": "상법인수",
            "vietnamese": "Tiếp quản thương mại",
            "hanja": "商法引受",
            "hanjaReading": "商(장사 상) 法(법 법) 引(끌 인) 受(받을 수)",
            "pronunciation": "상법인수",
            "meaningKo": "상법상 인수인이 발행회사로부터 신주나 사채를 인수하여 일반 투자자에게 판매하는 것을 말합니다. 통역 시 인수는 총액인수(전액 인수 책임), 잔액인수(미매각분만 인수), 주선(판매만 중개)로 구분되며, 증권회사가 발행 위험을 분담한다는 점을 명확히 해야 합니다. 베트남 증권법에서도 'bảo lãnh phát hành(발행 보증)'으로 규정하며, 증권회사의 역할이 규정되어 있습니다. 통역 시 인수 수수료, 인수 조건, 인수인의 책임 범위를 명확히 전달하고, 발행 실패 시 처리 방법을 설명해야 합니다.",
            "meaningVi": "Công ty chứng khoán (người bảo lãnh) nhận cổ phiếu hoặc trái phiếu mới từ công ty phát hành và bán cho nhà đầu tư. Có bảo lãnh toàn bộ (chịu trách nhiệm toàn bộ), bảo lãnh phần còn lại (chỉ nhận phần chưa bán được), và môi giới (chỉ trung gian bán). Công ty chứng khoán chia sẻ rủi ro phát hành. Luật chứng khoán Việt Nam quy định vai trò này. Cần chú ý phí bảo lãnh, điều kiện, phạm vi trách nhiệm, và cách xử lý khi phát hành thất bại.",
            "context": "IPO, 공모, 회사채 발행 시",
            "culturalNote": "한국은 증권 인수 시장이 발달하여 대형 증권사가 주관하지만, 베트남은 인수 시장이 미성숙하여 소규모 발행이 많고 인수 수수료가 높습니다. 베트남에서는 인수인의 책임 범위가 불명확하여 발행 실패 시 분쟁이 발생할 수 있으므로, 통역 시 인수 계약서에 책임 범위를 명확히 기재하도록 조언해야 합니다. 베트남은 공모 절차가 복잡하고 증권위원회 승인이 까다로워 시간이 오래 걸리므로, 통역 시 충분한 준비 기간을 두도록 권장해야 합니다. 한국 기업이 베트남에서 IPO를 추진할 때는 현지 증권회사와 인수 계약을 체결해야 하므로, 통역사가 계약 조건 협상을 지원해야 합니다.",
            "commonMistakes": [
                {
                    "mistake": "인수와 매수를 구분하지 않음",
                    "correction": "인수는 신주 발행, 매수는 기존주 거래",
                    "explanation": "인수는 발행시장, 매수는 유통시장 거래"
                },
                {
                    "mistake": "인수인은 위험 부담 없다고 설명",
                    "correction": "총액인수는 미매각 위험 전부 부담",
                    "explanation": "인수 방식에 따라 위험 부담 정도가 다름"
                },
                {
                    "mistake": "인수는 증권회사만 가능하다고 설명",
                    "correction": "베트남도 한국처럼 증권회사만 가능",
                    "explanation": "인수업은 인가받은 증권회사만 영위 가능"
                }
            ],
            "examples": [
                {
                    "ko": "본 공모는 A증권이 총액인수 방식으로 주관합니다",
                    "vi": "Đợt chào bán công khai này do công ty chứng khoán A bảo lãnh toàn bộ",
                    "situation": "formal"
                },
                {
                    "ko": "증권사가 주식 못 팔면 자기가 사야 하는 게 인수예요",
                    "vi": "Nếu công ty chứng khoán không bán được cổ phiếu thì phải tự mua, đó là bảo lãnh",
                    "situation": "informal"
                },
                {
                    "ko": "현장 법인 IPO 시 증권사 인수 수수료 협상 잘 하세요",
                    "vi": "Khi pháp nhân tại hiện trường IPO, hãy thương lượng tốt phí bảo lãnh với công ty chứng khoán",
                    "situation": "onsite"
                }
            ],
            "relatedTerms": ["IPO", "공모", "증권회사", "발행시장"]
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
    print(f"Added {len(filtered)} terms. Total: {len(data)}")

if __name__ == '__main__':
    main()
