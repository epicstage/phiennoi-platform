#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
건설 용어 추가 스크립트 - 건설안전법규 테마 (10개)
Tier S 기준 (90점 이상) 준수
"""

import json
import os

# 추가할 용어 데이터
data = [
    {
        "slug": "luat-an-toan-ve-sinh-lao-dong",
        "korean": "산업안전보건법",
        "vietnamese": "Luật An toàn vệ sinh lao động",
        "hanja": "産業安全保健法",
        "hanjaReading": "産(낳을 산) + 業(업 업) + 安(편안할 안) + 全(온전할 전) + 保(지킬 보) + 健(건강할 건) + 法(법 법)",
        "pronunciation": "루엇 안 토안 베 신 라오 동",
        "meaningKo": "산업재해를 예방하고 쾌적한 작업환경을 조성하여 근로자의 안전과 보건을 유지·증진함을 목적으로 하는 법률입니다. 베트남어 통역 시 '안전보건'을 '안전위생'으로 직역하면 의미가 축소되므로 주의가 필요합니다. 한국의 중대재해처벌법까지 포함하는 개념인지 맥락을 확인해야 하며, 베트남 현장에서는 Luật An toàn vệ sinh lao động이 비교적 포괄적으로 쓰이지만 구체적 조항은 Nghị định(시행령)을 함께 언급해야 합니다. 법 개정 이력을 확인하고 최신 조항을 기준으로 통역해야 오해가 없습니다.",
        "meaningVi": "Luật quy định về phòng ngừa tai nạn lao động, bảo vệ sức khỏe và tạo môi trường làm việc an toàn cho người lao động trong các ngành công nghiệp. Luật này bao gồm các quy định về đánh giá rủi ro, đào tạo an toàn, trang bị bảo hộ, và trách nhiệm của người sử dụng lao động.",
        "context": "법률 조항 인용, 안전교육 자료, 계약서, 감사 대응 시 사용",
        "culturalNote": "한국은 중대재해처벌법으로 사업주 형사처벌까지 가능하지만, 베트남은 행정처분 중심입니다. 한국에서 '안전보건'은 안전(Safety)과 보건(Health)을 분리하지만 베트남어는 하나의 개념(An toàn vệ sinh lao động)으로 묶어 표현합니다. 한국 현장에서는 법 위반 시 즉시 작업중지 명령이 가능하지만 베트남은 절차가 상대적으로 복잡합니다.",
        "commonMistakes": [
            {
                "mistake": "안전위생법",
                "correction": "산업안전보건법",
                "explanation": "베트nam어를 직역하면 '안전위생'이지만 한국 법명은 '안전보건'입니다"
            },
            {
                "mistake": "Luật An toàn lao động만 언급",
                "correction": "Luật An toàn vệ sinh lao động",
                "explanation": "vệ sinh(위생/보건)을 누락하면 법의 범위가 축소됩니다"
            },
            {
                "mistake": "중대재해처벌법과 혼동",
                "correction": "산업안전보건법과 중대재해처벌법은 별개 법률임을 구분",
                "explanation": "중대재해처벌법은 2021년 제정된 별도 법률입니다"
            }
        ],
        "examples": [
            {
                "ko": "산업안전보건법 제38조에 따라 위험성평가를 실시해야 합니다.",
                "vi": "Theo Điều 38 Luật An toàn vệ sinh lao động, phải thực hiện đánh giá rủi ro.",
                "situation": "formal"
            },
            {
                "ko": "이 현장은 산안법 위반으로 과태료 처분을 받았어요.",
                "vi": "Công trường này bị phạt vi phạm hành chính do vi phạm Luật An toàn vệ sinh lao động.",
                "situation": "onsite"
            },
            {
                "ko": "산업안전보건법상 안전관리자 선임이 의무입니다.",
                "vi": "Theo Luật An toàn vệ sinh lao động, việc bổ nhiệm người quản lý an toàn là bắt buộc.",
                "situation": "formal"
            }
        ],
        "relatedTerms": ["중대재해", "안전관리자", "위험성평가", "작업중지권"]
    },
    {
        "slug": "nguoi-quan-ly-an-toan",
        "korean": "안전관리자",
        "vietnamese": "Người quản lý an toàn",
        "hanja": "安全管理者",
        "hanjaReading": "安(편안할 안) + 全(온전할 전) + 管(대롱 관) + 理(다스릴 리) + 者(놈 자)",
        "pronunciation": "응으어이 꾸안 리 안 토안",
        "meaningKo": "산업안전보건법에 따라 일정 규모 이상의 사업장에서 안전에 관한 기술적인 사항을 관리하는 사람입니다. 통역 시 '안전담당자'와 혼동하지 않도록 주의해야 합니다. 안전관리자는 법정 자격(산업안전기사 등)이 필요한 법정직책이며, 건설업의 경우 공사금액에 따라 배치 인원이 달라집니다. 베트남에서는 Chuyên viên an toàn(안전전문가)로도 표현하나, 공식 문서에서는 Người quản lý an toàn을 사용합니다.",
        "meaningVi": "Người có trách nhiệm quản lý các vấn đề kỹ thuật về an toàn lao động tại nơi làm việc theo quy định của pháp luật. Phải có chứng chỉ chuyên môn về an toàn lao động và được bổ nhiệm chính thức.",
        "context": "조직도 작성, 안전교육, 인사발령, 법정 의무 이행 보고 시 사용",
        "culturalNote": "한국은 안전관리자와 보건관리자를 분리 선임하지만, 베트남은 통합 운영하는 경우가 많습니다. 한국 건설현장에서는 안전관리자가 작업중지권을 가지지만, 베트남은 현장소장 권한인 경우가 대부분입니다. 자격증 체계도 다르므로 양국 자격을 상호인정하지 않습니다.",
        "commonMistakes": [
            {
                "mistake": "안전담당자",
                "correction": "안전관리자",
                "explanation": "안전관리자는 법정직책이며 자격 요건이 있지만, 안전담당자는 일반 업무 분장입니다"
            },
            {
                "mistake": "Nhân viên an toàn(안전직원)",
                "correction": "Người quản lý an toàn(안전관리자)",
                "explanation": "직급과 권한의 차이를 구분해야 합니다"
            },
            {
                "mistake": "보건관리자와 혼동",
                "correction": "안전관리자는 Safety, 보건관리자는 Health 담당",
                "explanation": "업무 영역이 다릅니다"
            }
        ],
        "examples": [
            {
                "ko": "이번 달까지 안전관리자를 선임해야 합니다.",
                "vi": "Phải bổ nhiệm người quản lý an toàn trước hết tháng này.",
                "situation": "formal"
            },
            {
                "ko": "안전관리자가 작업중지를 명령했어요.",
                "vi": "Người quản lý an toàn đã ra lệnh dừng công việc.",
                "situation": "onsite"
            },
            {
                "ko": "산업안전기사 자격증 소지자를 안전관리자로 선임합니다.",
                "vi": "Bổ nhiệm người có chứng chỉ kỹ sư an toàn công nghiệp làm người quản lý an toàn.",
                "situation": "formal"
            }
        ],
        "relatedTerms": ["보건관리자", "안전보건총괄책임자", "산업안전보건법", "작업중지권"]
    },
    {
        "slug": "nguoi-quan-ly-suc-khoe",
        "korean": "보건관리자",
        "vietnamese": "Người quản lý sức khỏe",
        "hanja": "保健管理者",
        "hanjaReading": "保(지킬 보) + 健(건강할 건) + 管(대롱 관) + 理(다스릴 리) + 者(놈 자)",
        "pronunciation": "응으어이 꾸안 리 썩 쾨",
        "meaningKo": "산업안전보건법에 따라 근로자의 건강관리, 작업환경 측정, 직업병 예방 등 보건에 관한 기술적 사항을 관리하는 사람입니다. 통역 시 '건강관리자'로 오역하지 않도록 주의해야 하며, 간호사·산업위생관리기사 등 법정 자격이 필요합니다. 베트남어로는 sức khỏe(건강)보다 vệ sinh lao động(노동위생)을 더 많이 사용하므로 맥락에 따라 Người quản lý vệ sinh lao động으로도 표현할 수 있습니다.",
        "meaningVi": "Người chịu trách nhiệm quản lý sức khỏe người lao động, đo lường môi trường làm việc, phòng ngừa bệnh nghề nghiệp. Phải có trình độ chuyên môn về y tế hoặc vệ sinh lao động.",
        "context": "건강검진 계획, 작업환경 측정, 직업병 관리, 인사발령 시 사용",
        "culturalNote": "한국은 안전(Safety)과 보건(Health)을 명확히 분리하여 각각 관리자를 두지만, 베트남은 안전과 보건을 통합 관리하는 경우가 많습니다. 한국 보건관리자는 의료 배경이 우선이지만 베트남은 공학 배경도 가능합니다. 건강검진 주기와 항목도 양국이 다르므로 혼동 주의가 필요합니다.",
        "commonMistakes": [
            {
                "mistake": "건강관리자",
                "correction": "보건관리자",
                "explanation": "법정 명칭은 '보건관리자'입니다"
            },
            {
                "mistake": "Người quản lý y tế(의료관리자)",
                "correction": "Người quản lý sức khỏe 또는 Người quản lý vệ sinh lao động",
                "explanation": "산업보건 맥락에서는 y tế보다 sức khỏe/vệ sinh lao động이 적합합니다"
            },
            {
                "mistake": "안전관리자와 혼동",
                "correction": "안전관리자는 재해 예방, 보건관리자는 건강 관리",
                "explanation": "업무 영역이 다릅니다"
            }
        ],
        "examples": [
            {
                "ko": "보건관리자가 작업환경 측정 계획을 수립했습니다.",
                "vi": "Người quản lý sức khỏe đã lập kế hoạch đo lường môi trường làm việc.",
                "situation": "formal"
            },
            {
                "ko": "보건관리자 자격증 있는 분 채용 중이에요.",
                "vi": "Đang tuyển người có chứng chỉ quản lý sức khỏe lao động.",
                "situation": "informal"
            },
            {
                "ko": "간호사 면허가 있으면 보건관리자로 선임 가능합니다.",
                "vi": "Nếu có giấy phép hành nghề điều dưỡng thì có thể bổ nhiệm làm người quản lý sức khỏe.",
                "situation": "formal"
            }
        ],
        "relatedTerms": ["안전관리자", "작업환경측정", "직업병", "건강검진"]
    },
    {
        "slug": "nguoi-chiu-trach-nhiem-tong-quan-an-toan-suc-khoe",
        "korean": "안전보건총괄책임자",
        "vietnamese": "Người chịu trách nhiệm tổng quát an toàn sức khỏe",
        "hanja": "安全保健總括責任者",
        "hanjaReading": "安(편안할 안) + 全(온전할 전) + 保(지킬 보) + 健(건강할 건) + 總(다 총) + 括(묶을 괄) + 責(꾸짖을 책) + 任(맡길 임) + 者(놈 자)",
        "pronunciation": "응으어이 찌으 짝 녀임 똥 꾸앗 안 토안 썩 쾨",
        "meaningKo": "건설업 등에서 해당 사업장의 안전 및 보건에 관한 업무를 총괄·관리하는 사람으로, 주로 현장소장이나 공사 책임자가 담당합니다. 통역 시 '안전보건관리책임자'와 혼동하지 않도록 주의해야 합니다. 총괄책임자는 건설현장 전체를 책임지며, 안전관리자·보건관리자를 지휘하는 위치입니다. 베트남어로는 tổng quát(총괄)을 강조하여 최고 책임자임을 명확히 해야 합니다.",
        "meaningVi": "Người có trách nhiệm quản lý tổng thể các vấn đề về an toàn và sức khỏe tại công trường xây dựng hoặc nơi làm việc, thường là giám đốc công trường hoặc người đứng đầu. Có quyền chỉ đạo người quản lý an toàn và người quản lý sức khỏe.",
        "context": "건설현장 조직도, 안전관리 체계 수립, 법적 책임 소재 명시 시 사용",
        "culturalNote": "한국 건설현장에서는 안전보건총괄책임자가 최종 책임을 지며 작업중지권도 가집니다. 베트남은 Giám đốc công trường(현장소장)이 총괄하지만 안전 전담 조직이 약한 편입니다. 중대재해 발생 시 한국은 총괄책임자가 형사처벌 대상이 되지만, 베트남은 행정처분 위주입니다.",
        "commonMistakes": [
            {
                "mistake": "안전보건관리책임자",
                "correction": "안전보건총괄책임자",
                "explanation": "'총괄'이 빠지면 다른 직책입니다(관리책임자는 제조업 등에서 사용)"
            },
            {
                "mistake": "Giám đốc an toàn(안전이사)",
                "correction": "Người chịu trách nhiệm tổng quát an toàn sức khỏe",
                "explanation": "총괄책임자는 현장 최고 책임자로서의 역할을 명시해야 합니다"
            },
            {
                "mistake": "안전관리자와 동일 인물로 간주",
                "correction": "총괄책임자는 안전관리자를 지휘하는 상위 직책",
                "explanation": "조직 위계를 구분해야 합니다"
            }
        ],
        "examples": [
            {
                "ko": "안전보건총괄책임자는 현장소장이 겸임합니다.",
                "vi": "Người chịu trách nhiệm tổng quát an toàn sức khỏe do giám đốc công trường겸 겸임.",
                "situation": "formal"
            },
            {
                "ko": "총괄책임자 서명이 필요한 서류예요.",
                "vi": "Đây là tài liệu cần chữ ký của người chịu trách nhiệm tổng quát.",
                "situation": "onsite"
            },
            {
                "ko": "안전보건총괄책임자의 직무는 산업안전보건법 시행령에 명시되어 있습니다.",
                "vi": "Nhiệm vụ của người chịu trách nhiệm tổng quát an toàn sức khỏe được quy định trong Nghị định thi hành Luật An toàn vệ sinh lao động.",
                "situation": "formal"
            }
        ],
        "relatedTerms": ["안전관리자", "보건관리자", "현장소장", "작업중지권"]
    },
    {
        "slug": "danh-gia-rui-ro",
        "korean": "위험성평가",
        "vietnamese": "Đánh giá rủi ro",
        "hanja": "危險性評價",
        "hanjaReading": "危(위태로울 위) + 險(험할 험) + 性(성품 성) + 評(평할 평) + 價(값 가)",
        "pronunciation": "다잉 지아 주이 조",
        "meaningKo": "사업장에 존재하는 유해·위험요인을 찾아내어 부상 또는 질병으로 이어질 가능성과 중대성을 추정·결정하고 감소대책을 수립하여 실행하는 일련의 과정입니다. 통역 시 '위험평가'로 축약하지 말고 '위험성평가'로 정확히 표현해야 하며, 베트남어 rủi ro는 risk를 의미하므로 '위험'과 '위험성'을 구분해야 합니다. 한국에서는 사업주의 법정 의무이며, 평가 결과를 문서화하여 보관해야 합니다.",
        "meaningVi": "Quá trình xác định các yếu tố nguy hiểm tại nơi làm việc, đánh giá khả năng xảy ra tai nạn hoặc bệnh nghề nghiệp, mức độ nghiêm trọng, và thiết lập biện pháp giảm thiểu rủi ro. Là nghĩa vụ pháp lý của người sử dụng lao động.",
        "context": "안전관리 계획 수립, 안전교육, 작업 전 준비, 감독기관 보고 시 사용",
        "culturalNote": "한국은 위험성평가를 정기적으로 실시하고 기록을 3년간 보관해야 하지만, 베트남은 절차가 덜 엄격합니다. 한국에서는 근로자 참여가 법적 요건이지만 베트남은 관리자 중심입니다. 평가 방법론(JSA, HAZOP 등)도 양국이 선호하는 기법이 다를 수 있습니다.",
        "commonMistakes": [
            {
                "mistake": "위험평가",
                "correction": "위험성평가",
                "explanation": "법률 용어는 '위험성평가'입니다"
            },
            {
                "mistake": "Đánh giá nguy hiểm(위험 평가)",
                "correction": "Đánh giá rủi ro(위험성 평가)",
                "explanation": "nguy hiểm은 danger, rủi ro는 risk로 개념이 다릅니다"
            },
            {
                "mistake": "위험성평가 = 안전점검",
                "correction": "위험성평가는 사전 예방, 안전점검은 사후 확인",
                "explanation": "목적과 시점이 다릅니다"
            }
        ],
        "examples": [
            {
                "ko": "착공 전에 위험성평가를 완료해야 합니다.",
                "vi": "Phải hoàn thành đánh giá rủi ro trước khi khởi công.",
                "situation": "formal"
            },
            {
                "ko": "이번 작업 위험성평가 결과 확인해 주세요.",
                "vi": "Vui lòng kiểm tra kết quả đánh giá rủi ro cho công việc này.",
                "situation": "onsite"
            },
            {
                "ko": "위험성평가에 근로자 의견을 반영해야 합니다.",
                "vi": "Phải phản ánh ý kiến người lao động trong đánh giá rủi ro.",
                "situation": "formal"
            }
        ],
        "relatedTerms": ["안전점검", "유해위험요인", "안전관리", "산업재해"]
    },
    {
        "slug": "quyen-dung-cong-viec",
        "korean": "작업중지권",
        "vietnamese": "Quyền dừng công việc",
        "hanja": "作業中止權",
        "hanjaReading": "作(지을 작) + 業(업 업) + 中(가운데 중) + 止(그칠 지) + 權(권세 권)",
        "pronunciation": "꾸엔 중 꽁 비엑",
        "meaningKo": "근로자가 산업재해가 발생할 급박한 위험이 있다고 판단될 때 작업을 중지하고 대피할 수 있는 권리입니다. 통역 시 '작업정지권'으로 오역하지 않도록 주의해야 하며, 이는 근로자의 권리이자 사업주가 불이익을 줄 수 없는 법적 보호 대상입니다. 베트남어로는 quyền(권리)을 강조하여 일방적 명령이 아님을 명확히 해야 하며, 안전관리자뿐 아니라 일반 근로자도 행사할 수 있습니다.",
        "meaningVi": "Quyền của người lao động được dừng công việc và sơ tán khi nhận thấy có nguy cơ xảy ra tai nạn lao động nghiêm trọng. Người sử dụng lao động không được xử phạt hoặc gây bất lợi cho người lao động khi họ thực hiện quyền này.",
        "context": "위험 상황 발생 시, 안전교육, 근로계약서, 안전수칙 설명 시 사용",
        "culturalNote": "한국은 2019년 산업안전보건법 개정으로 근로자의 작업중지권이 명확히 보장되었지만, 베트남은 법적 명시가 약하고 관리자 권한입니다. 한국에서는 작업중지 후 불이익 조치가 금지되지만, 베트남 현장에서는 무단이탈로 간주될 위험이 있습니다. 문화적으로도 한국은 개인 권리 존중, 베트남은 집단 질서 우선 경향이 있습니다.",
        "commonMistakes": [
            {
                "mistake": "작업정지권",
                "correction": "작업중지권",
                "explanation": "'정지'가 아닌 '중지'가 법률 용어입니다"
            },
            {
                "mistake": "Lệnh dừng công việc(작업중지 명령)",
                "correction": "Quyền dừng công việc(작업중지권)",
                "explanation": "lệnh(명령)이 아닌 quyền(권리)으로 표현해야 합니다"
            },
            {
                "mistake": "관리자만 행사 가능",
                "correction": "모든 근로자가 행사 가능",
                "explanation": "근로자 개인의 권리입니다"
            }
        ],
        "examples": [
            {
                "ko": "낙하 위험이 있어 작업중지권을 행사했습니다.",
                "vi": "Đã thực hiện quyền dừng công việc do có nguy cơ rơi rớt.",
                "situation": "formal"
            },
            {
                "ko": "위험하다 싶으면 바로 작업 멈추고 대피하세요.",
                "vi": "Nếu thấy nguy hiểm, hãy dừng công việc ngay và sơ tán.",
                "situation": "onsite"
            },
            {
                "ko": "작업중지권 행사를 이유로 불이익을 주면 법 위반입니다.",
                "vi": "Vi phạm pháp luật nếu gây bất lợi cho người lao động vì họ thực hiện quyền dừng công việc.",
                "situation": "formal"
            }
        ],
        "relatedTerms": ["산업재해", "위험성평가", "안전관리자", "긴급대피"]
    },
    {
        "slug": "tai-nan-nghiem-trong",
        "korean": "중대재해",
        "vietnamese": "Tai nạn nghiêm trọng",
        "hanja": "重大災害",
        "hanjaReading": "重(무거울 중) + 大(큰 대) + 災(재앙 재) + 害(해할 해)",
        "pronunciation": "따이 난 응이엠 쫑",
        "meaningKo": "사망자가 1명 이상 발생하거나, 3개월 이상 치료가 필요한 부상자가 2명 이상 발생하거나, 동시에 10명 이상의 부상자가 발생한 재해를 의미합니다. 통역 시 '중대사고'로 오역하지 않도록 주의해야 하며, 한국에서는 중대재해처벌법으로 사업주 처벌까지 가능합니다. 베트남어로는 tai nạn lao động nghiêm trọng(중대 산업재해)로 풀어서 표현할 수 있으며, 발생 시 즉시 신고 의무가 있습니다.",
        "meaningVi": "Tai nạn lao động gây tử vong hoặc thương tích nghiêm trọng (từ 2 người bị thương cần điều trị trên 3 tháng, hoặc từ 10 người bị thương cùng lúc). Theo pháp luật Hàn Quốc, chủ doanh nghiệp có thể bị truy cứu trách nhiệm hình sự.",
        "context": "재해 보고, 사고 조사, 법적 대응, 보험 처리, 안전교육 시 사용",
        "culturalNote": "한국은 2022년부터 중대재해처벌법으로 사업주·경영책임자 처벌이 가능하지만, 베트남은 행정처분과 민사배상이 주요 수단입니다. 한국은 중대재해 발생 시 즉시 관할 관청 신고 의무가 있으나, 베트남은 보고 절차가 상대적으로 느슨합니다. 재해 은폐 시 처벌 수위도 양국이 다릅니다.",
        "commonMistakes": [
            {
                "mistake": "중대사고",
                "correction": "중대재해",
                "explanation": "'사고'가 아닌 '재해'가 법률 용어입니다"
            },
            {
                "mistake": "Tai nạn lớn(큰 사고)",
                "correction": "Tai nạn nghiêm trọng(중대재해)",
                "explanation": "nghiêm trọng이 법적 기준에 맞는 표현입니다"
            },
            {
                "mistake": "산업재해와 동일 개념",
                "correction": "중대재해는 산업재해 중 특히 심각한 경우",
                "explanation": "중대재해는 산업재해의 하위 개념입니다"
            }
        ],
        "examples": [
            {
                "ko": "중대재해 발생으로 공사가 중단되었습니다.",
                "vi": "Công trình đã bị đình chỉ do xảy ra tai nạn nghiêm trọng.",
                "situation": "formal"
            },
            {
                "ko": "중대재해 은폐 시 가중처벌 받아요.",
                "vi": "Sẽ bị gia tăng hình phạt nếu che giấu tai nạn nghiêm trọng.",
                "situation": "onsite"
            },
            {
                "ko": "이 사고는 중대재해에 해당하므로 즉시 신고해야 합니다.",
                "vi": "Vụ tai nạn này thuộc loại tai nạn nghiêm trọng nên phải báo cáo ngay lập tức.",
                "situation": "formal"
            }
        ],
        "relatedTerms": ["산업재해", "재해율", "중대재해처벌법", "작업중지권"]
    },
    {
        "slug": "tai-nan-lao-dong",
        "korean": "산업재해",
        "vietnamese": "Tai nạn lao động",
        "hanja": "産業災害",
        "hanjaReading": "産(낳을 산) + 業(업 업) + 災(재앙 재) + 害(해할 해)",
        "pronunciation": "따이 난 라오 동",
        "meaningKo": "근로자가 업무에 관계되는 건설물·설비·원재료·가스·증기·분진 등에 의하거나 작업 또는 그 밖의 업무로 인하여 사망 또는 부상하거나 질병에 걸리는 것을 말합니다. 통역 시 '산재'로 축약하거나 '노동재해'로 오역하지 않도록 주의해야 하며, 업무상 재해 인정 기준이 양국이 다르므로 맥락 확인이 필요합니다. 베트남어로는 tai nạn lao động(노동사고)이지만 bệnh nghề nghiệp(직업병)도 포함하는 포괄 개념입니다.",
        "meaningVi": "Tình trạng người lao động bị tử vong, bị thương hoặc mắc bệnh do các yếu tố liên quan đến công việc như thiết bị, nguyên liệu, khí gas, bụi, hoặc do quá trình thực hiện công việc. Bao gồm cả bệnh nghề nghiệp.",
        "context": "재해 통계, 산재보험 청구, 안전교육, 보고서 작성 시 사용",
        "culturalNote": "한국은 산재보험이 의무가입이며 업무상 재해 인정 범위가 넓지만(출퇴근 재해 포함), 베트남은 인정 기준이 상대적으로 좁습니다. 한국은 산재 은폐 시 가중처벌이 있으나, 베트남은 보험 처리 중심입니다. 직업병 인정 질환 목록도 양국이 다르므로 주의가 필요합니다.",
        "commonMistakes": [
            {
                "mistake": "노동재해",
                "correction": "산업재해",
                "explanation": "한국 법률 용어는 '산업재해'입니다"
            },
            {
                "mistake": "Tai nạn công nghiệp(공업사고)",
                "correction": "Tai nạn lao động(산업재해)",
                "explanation": "lao động(노동)이 법적으로 정확한 표현입니다"
            },
            {
                "mistake": "사고만 산재",
                "correction": "사고 + 질병(직업병) 모두 포함",
                "explanation": "산업재해는 부상과 질병을 모두 포함합니다"
            }
        ],
        "examples": [
            {
                "ko": "지난해 이 현장에서 산업재해가 3건 발생했습니다.",
                "vi": "Năm ngoái tại công trường này đã xảy ra 3 vụ tai nạn lao động.",
                "situation": "formal"
            },
            {
                "ko": "산재 신청하면 치료비 나와요.",
                "vi": "Nếu nộp đơn yêu cầu bảo hiểm tai nạn lao động sẽ được chi trả chi phí điều trị.",
                "situation": "informal"
            },
            {
                "ko": "산업재해 예방을 위해 안전교육을 정기적으로 실시합니다.",
                "vi": "Thực hiện đào tạo an toàn định kỳ để phòng ngừa tai nạn lao động.",
                "situation": "formal"
            }
        ],
        "relatedTerms": ["중대재해", "재해율", "직업병", "산재보험"]
    },
    {
        "slug": "ty-le-tai-nan",
        "korean": "재해율",
        "vietnamese": "Tỷ lệ tai nạn",
        "hanja": "災害率",
        "hanjaReading": "災(재앙 재) + 害(해할 해) + 率(비율 률)",
        "pronunciation": "띠 레 따이 난",
        "meaningKo": "일정 기간 동안 발생한 재해자 수를 근로자 수로 나눈 비율로, 산업재해 발생 정도를 나타내는 지표입니다. 통역 시 '사고율'로 오역하지 않도록 주의해야 하며, 도수율(건수 기준)과 강도율(손실일수 기준)로 구분됩니다. 베트남어로는 tỷ lệ(비율)을 명확히 하여 백분율 개념임을 표현해야 하며, 연간 재해율은 건설업 평가 지표로도 활용됩니다.",
        "meaningVi": "Chỉ số thể hiện mức độ xảy ra tai nạn lao động, được tính bằng số người bị tai nạn chia cho tổng số lao động trong một khoảng thời gian nhất định. Bao gồm tỷ lệ tần suất (số vụ) và tỷ lệ nghiêm trọng (số ngày nghỉ).",
        "context": "안전 통계 보고, 현장 평가, 입찰 서류, KPI 관리 시 사용",
        "culturalNote": "한국은 재해율을 건설업 평가 시 중요한 지표로 활용하며, 재해율이 높으면 입찰 제한을 받을 수 있습니다. 베트남은 재해율 통계가 상대적으로 덜 엄격하며, 보고 누락이 많아 실제보다 낮게 나타날 수 있습니다. 계산 방식(도수율, 강도율)도 양국이 다를 수 있으므로 확인이 필요합니다.",
        "commonMistakes": [
            {
                "mistake": "사고율",
                "correction": "재해율",
                "explanation": "'재해'가 법률 용어입니다"
            },
            {
                "mistake": "Tỷ lệ sự cố(사고율)",
                "correction": "Tỷ lệ tai nạn(재해율)",
                "explanation": "sự cố는 incident, tai nạn은 accident로 다릅니다"
            },
            {
                "mistake": "재해 건수와 동일 개념",
                "correction": "재해율은 비율(%), 재해 건수는 절대값",
                "explanation": "단위가 다릅니다"
            }
        ],
        "examples": [
            {
                "ko": "올해 목표 재해율은 0.3% 이하입니다.",
                "vi": "Mục tiêu tỷ lệ tai nạn năm nay là dưới 0,3%.",
                "situation": "formal"
            },
            {
                "ko": "재해율이 높으면 입찰 참여가 제한돼요.",
                "vi": "Nếu tỷ lệ tai nạn cao sẽ bị hạn chế tham gia đấu thầu.",
                "situation": "onsite"
            },
            {
                "ko": "재해율 감소를 위해 안전관리 강화가 필요합니다.",
                "vi": "Cần tăng cường quản lý an toàn để giảm tỷ lệ tai nạn.",
                "situation": "formal"
            }
        ],
        "relatedTerms": ["산업재해", "도수율", "강도율", "안전점검"]
    },
    {
        "slug": "kiem-tra-an-toan",
        "korean": "안전점검",
        "vietnamese": "Kiểm tra an toàn",
        "hanja": "安全點檢",
        "hanjaReading": "安(편안할 안) + 全(온전할 전) + 點(점 점) + 檢(검사할 검)",
        "pronunciation": "끼엠 짜 안 토안",
        "meaningKo": "작업 현장의 안전 상태를 확인하고 위험 요소를 점검하는 활동으로, 정기점검·수시점검·특별점검으로 구분됩니다. 통역 시 '안전검사'로 오역하지 않도록 주의해야 하며, 점검은 일상적 확인, 검사는 공식적 인증 절차를 의미합니다. 베트남어로는 kiểm tra(점검)와 thanh tra(감사)를 구분하며, 안전점검은 자체 점검이므로 kiểm tra가 적합합니다.",
        "meaningVi": "Hoạt động kiểm tra tình trạng an toàn tại nơi làm việc, phát hiện các yếu tố nguy hiểm. Bao gồm kiểm tra định kỳ, kiểm tra đột xuất, và kiểm tra đặc biệt. Khác với thanh tra (audit) do cơ quan chức năng thực hiện.",
        "context": "일일 안전점검, 정기 점검 계획, 점검표 작성, 시정조치 보고 시 사용",
        "culturalNote": "한국은 일일 안전점검(TBM)을 의무화하는 현장이 많지만, 베트남은 형식적인 경우가 많습니다. 한국은 점검 결과를 기록하고 보관해야 하지만, 베트남은 문서화가 덜 철저합니다. 안전점검과 안전감사(audit)를 구분하는 것도 중요하며, 베트남어로는 kiểm tra vs thanh tra로 명확히 구분됩니다.",
        "commonMistakes": [
            {
                "mistake": "안전검사",
                "correction": "안전점검",
                "explanation": "점검(check)과 검사(inspection/certification)는 다릅니다"
            },
            {
                "mistake": "Thanh tra an toàn(안전감사)",
                "correction": "Kiểm tra an toàn(안전점검)",
                "explanation": "thanh tra는 공식 감사, kiểm tra는 일상 점검입니다"
            },
            {
                "mistake": "위험성평가와 동일",
                "correction": "위험성평가는 사전 분석, 안전점검은 사후 확인",
                "explanation": "목적과 시점이 다릅니다"
            }
        ],
        "examples": [
            {
                "ko": "매일 아침 작업 전 안전점검을 실시합니다.",
                "vi": "Thực hiện kiểm tra an toàn trước khi làm việc mỗi sáng.",
                "situation": "formal"
            },
            {
                "ko": "안전점검 체크리스트 확인해 주세요.",
                "vi": "Vui lòng kiểm tra danh sách kiểm tra an toàn.",
                "situation": "onsite"
            },
            {
                "ko": "특별안전점검 결과 시정조치가 필요한 사항이 5건입니다.",
                "vi": "Kết quả kiểm tra an toàn đặc biệt cho thấy có 5 hạng mục cần khắc phục.",
                "situation": "formal"
            }
        ],
        "relatedTerms": ["위험성평가", "안전관리자", "시정조치", "TBM"]
    }
]

# 파일 경로
file_path = os.path.join(
    os.path.dirname(__file__),
    "..",
    "data",
    "terms",
    "construction.json"
)

# 기존 데이터 읽기
with open(file_path, "r", encoding="utf-8") as f:
    existing_data = json.load(f)

# 새 데이터 추가
existing_data.extend(data)

# 저장
with open(file_path, "w", encoding="utf-8") as f:
    json.dump(existing_data, f, ensure_ascii=False, indent=2)

print(f"✅ {len(data)}개 용어 추가 완료: {file_path}")
print(f"📊 총 용어 수: {len(existing_data)}개")
