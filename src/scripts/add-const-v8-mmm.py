#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
건설 용어 추가 스크립트 v8: 공사서류/보고서 테마
테마: 시공상세도, 준공도서, 유지관리매뉴얼, 자재승인서, 품질시험보고서 등
"""

import json
import os.path

# 추가할 용어 데이터 (Tier S 기준)
data = [
    {
        "slug": "ban-ve-thi-cong-chi-tiet",
        "korean": "시공상세도",
        "vietnamese": "Bản vẽ thi công chi tiết",
        "hanja": "施工詳細圖",
        "hanjaReading": "베풀 시(施) + 工장 공(工) + 자세할 상(詳) + 가늘 세(細) + 그림 도(圖)",
        "pronunciation": "시공상세도",
        "meaningKo": "건축물의 실제 시공을 위해 작성된 상세한 설계도면으로, 치수, 재료, 시공 방법 등이 구체적으로 표기된 도면입니다. 통역 시 '도면'과 '시방서'를 혼동하지 않도록 주의하고, 베트남 현장에서는 도면 수정(revision) 이력 관리가 매우 중요하므로 버전 번호를 명확히 전달해야 합니다. 한국은 KCS 기준, 베트남은 TCVN 기준으로 작성되므로 기준 차이를 설명할 수 있어야 합니다.",
        "meaningVi": "Bản vẽ thiết kế chi tiết được lập để thi công thực tế công trình, ghi rõ kích thước, vật liệu, phương pháp thi công. Cần phân biệt với 'thuyết minh kỹ thuật' (시방서). Quan trọng: phải theo dõi lịch sử sửa đổi (revision) và số phiên bản.",
        "context": "formal",
        "culturalNote": "한국에서는 시공도를 설계사무소와 시공사가 협의하여 작성하는 경우가 많으나, 베트남에서는 시공사가 독자적으로 작성 후 감리단의 승인을 받는 절차가 일반적입니다. 도면 보관 및 revision 관리 체계가 한국보다 엄격하며, 모든 수정 사항은 문서로 기록되어야 합니다. 베트남 현장에서는 도면을 '원본(bản gốc)'과 '사본(bản copy)'으로 구분하여 관리합니다.",
        "commonMistakes": [
            {
                "mistake": "bản vẽ thiết kế",
                "correction": "bản vẽ thi công chi tiết",
                "explanation": "'설계도'와 '시공도'는 다릅니다. 설계도는 개념적, 시공도는 실행용 상세도입니다."
            },
            {
                "mistake": "shop drawing",
                "correction": "bản vẽ thi công chi tiết (hoặc shop drawing khi dùng thuật ngữ quốc tế)",
                "explanation": "베트남 현장에서도 'shop drawing'을 쓰지만, 공식 문서에는 베트남어 표현 사용이 권장됩니다."
            },
            {
                "mistake": "bản vẽ",
                "correction": "bản vẽ thi công chi tiết",
                "explanation": "단순히 '도면'이라고만 하면 어떤 종류인지 불명확합니다. 반드시 '시공상세도'임을 명시하세요."
            }
        ],
        "examples": [
            {
                "ko": "내일까지 철근 배근 시공상세도를 제출해 주세요.",
                "vi": "Vui lòng nộp bản vẽ thi công chi tiết bố trí cốt thép trước ngày mai.",
                "situation": "formal"
            },
            {
                "ko": "시공상세도 Rev.3으로 변경되었으니 현장 적용 바랍니다.",
                "vi": "Bản vẽ thi công chi tiết đã thay đổi sang Rev.3, vui lòng áp dụng tại công trường.",
                "situation": "onsite"
            },
            {
                "ko": "설계도와 시공도가 다른데 어느 걸 따라야 하나요?",
                "vi": "Bản vẽ thiết kế và bản vẽ thi công khác nhau, nên theo bản nào?",
                "situation": "informal"
            }
        ],
        "relatedTerms": ["설계도서", "시방서", "준공도서", "도면승인"]
    },
    {
        "slug": "ho-so-hoan-cong",
        "korean": "준공도서",
        "vietnamese": "Hồ sơ hoàn công",
        "hanja": "竣工圖書",
        "hanjaReading": "마칠 준(竣) + 工장 공(工) + 그림 도(圖) + 글 서(書)",
        "pronunciation": "준공도서",
        "meaningKo": "건축 공사가 완료된 후 실제 시공된 내용을 반영하여 작성하는 최종 도면 및 관련 서류 일체를 말합니다. 준공검사, 건축물대장 등록, 유지관리에 필수적인 자료입니다. 통역 시 '준공도면'과 '준공도서'를 구분해야 하며, 도서는 도면뿐 아니라 시방서, 계산서, 시험성적서 등을 모두 포함합니다. 베트남에서는 준공도서 미제출 시 최종 대금 지급이 보류되므로 납품 일정 협의가 중요합니다.",
        "meaningVi": "Toàn bộ bản vẽ và tài liệu liên quan được lập sau khi hoàn thành thi công, phản ánh nội dung thực tế đã thi công. Bao gồm: bản vẽ hoàn công, thuyết minh kỹ thuật, biên bản thí nghiệm, v.v. Là tài liệu bắt buộc để nghiệm thu và quản lý vận hành công trình.",
        "context": "formal",
        "culturalNote": "한국에서는 준공도서를 디지털(CAD, PDF) + 인쇄본으로 제출하지만, 베트남에서는 인쇄본 원본(bản gốc)에 더 큰 법적 효력을 부여합니다. 베트남은 준공도서 작성 기준이 매우 상세하며(TCVN 2682), 누락 시 벌금이나 준공 불허가 나올 수 있습니다. 한국은 준공 후 보완 제출이 가능하지만, 베트남은 준공검사 전 완료가 원칙입니다.",
        "commonMistakes": [
            {
                "mistake": "bản vẽ hoàn công",
                "correction": "hồ sơ hoàn công",
                "explanation": "'준공도면'은 도면만, '준공도서'는 모든 문서를 포함합니다. 도서(hồ sơ)가 더 포괄적입니다."
            },
            {
                "mistake": "竣工 도면",
                "correction": "준공도서 (竣工圖書)",
                "explanation": "한자어를 섞어 쓰면 베트남 기술자가 이해 못 합니다. 베트남어로 명확히 번역하세요."
            },
            {
                "mistake": "hoàn thành hồ sơ",
                "correction": "hồ sơ hoàn công",
                "explanation": "'hồ sơ hoàn công'은 고정된 법률 용어입니다. 어순을 바꾸면 안 됩니다."
            }
        ],
        "examples": [
            {
                "ko": "준공도서는 3부를 제본하여 납품해 주시기 바랍니다.",
                "vi": "Vui lòng đóng quyển và nộp 3 bộ hồ sơ hoàn công.",
                "situation": "formal"
            },
            {
                "ko": "준공도서 검토 완료되면 최종 대금 지급하겠습니다.",
                "vi": "Sau khi kiểm tra xong hồ sơ hoàn công, chúng tôi sẽ thanh toán khoản tiền cuối cùng.",
                "situation": "formal"
            },
            {
                "ko": "준공도서에 실제 시공 내용이 반영 안 된 부분이 있네요.",
                "vi": "Trong hồ sơ hoàn công có phần chưa phản ánh nội dung thi công thực tế.",
                "situation": "onsite"
            }
        ],
        "relatedTerms": ["준공검사", "시공상세도", "유지관리매뉴얼", "준공도면"]
    },
    {
        "slug": "huong-dan-van-hanh-bao-duong",
        "korean": "유지관리매뉴얼",
        "vietnamese": "Hướng dẫn vận hành bảo dưỡng",
        "hanja": "維持管理manual",
        "hanjaReading": "매울 유(維) + 가질 지(持) + 대롱 관(管) + 다스릴 리(理) + 영어 manual",
        "pronunciation": "유지관리매뉴얼",
        "meaningKo": "건축물이나 설비의 사용, 점검, 보수 방법을 체계적으로 정리한 지침서로, 건물주나 관리자가 장기간 건물을 유지하기 위해 필요한 모든 정보를 담고 있습니다. 통역 시 'manual'을 그대로 쓸지 '지침서'로 번역할지 상황에 따라 판단해야 하며, 베트남에서는 법적으로 준공도서에 포함되어야 하는 필수 서류이므로 누락 시 준공 불가 사실을 강조해야 합니다. 한국은 선택 제출이지만 베트남은 의무입니다.",
        "meaningVi": "Sách hướng dẫn hệ thống về cách sử dụng, kiểm tra, bảo trì công trình hoặc thiết bị, chứa đựng mọi thông tin cần thiết để chủ đầu tư hoặc người quản lý duy trì công trình lâu dài. Là tài liệu bắt buộc phải có trong hồ sơ hoàn công theo quy định của Việt Nam.",
        "context": "formal",
        "culturalNote": "한국에서는 유지관리매뉴얼을 간략하게 작성하는 경우가 많으나, 베트남에서는 TCVN 기준에 따라 매우 상세하게(설비별, 부위별) 작성해야 합니다. 베트남은 영문과 베트남어 병기를 선호하며, 사진과 도해가 풍부해야 합니다. 한국은 건축물 규모에 따라 작성 의무가 다르지만, 베트남은 모든 공공 건축물에 의무입니다.",
        "commonMistakes": [
            {
                "mistake": "manual vận hành",
                "correction": "hướng dẫn vận hành bảo dưỡng",
                "explanation": "'manual'을 그대로 쓰기보다 베트남어 '지침서(hướng dẫn)'를 쓰는 것이 공식 문서에 적합합니다."
            },
            {
                "mistake": "hướng dẫn sử dụng",
                "correction": "hướng dẫn vận hành bảo dưỡng",
                "explanation": "'사용 설명서'는 일반 제품용입니다. 건축물은 '운영·보수 지침서'가 정확합니다."
            },
            {
                "mistake": "sổ tay bảo trì",
                "correction": "hướng dẫn vận hành bảo dưỡng",
                "explanation": "'핸드북'보다 '지침서'가 공식적이고 포괄적입니다."
            }
        ],
        "examples": [
            {
                "ko": "유지관리매뉴얼은 한국어와 베트남어 2개 국어로 작성 부탁드립니다.",
                "vi": "Vui lòng lập hướng dẫn vận hành bảo dưỡng bằng 2 ngôn ngữ: tiếng Hàn và tiếng Việt.",
                "situation": "formal"
            },
            {
                "ko": "매뉴얼에 비상 상황 대응 절차도 포함시켜 주세요.",
                "vi": "Vui lòng bổ sung quy trình ứng phó tình huống khẩn cấp vào hướng dẫn.",
                "situation": "onsite"
            },
            {
                "ko": "이 설비 매뉴얼 어디 있어요? 고장 났는데 못 찾겠어요.",
                "vi": "Hướng dẫn thiết bị này ở đâu vậy? Bị hỏng rồi mà không tìm thấy.",
                "situation": "informal"
            }
        ],
        "relatedTerms": ["준공도서", "설비명세서", "점검일지", "보증서"]
    },
    {
        "slug": "giay-chung-nhan-vat-lieu",
        "korean": "자재승인서",
        "vietnamese": "Giấy chứng nhận vật liệu",
        "hanja": "資材承認書",
        "hanjaReading": "재물 자(資) + 재목 재(材) + 받을 승(承) + 허락할 인(認) + 글 서(書)",
        "pronunciation": "자재승인서",
        "meaningKo": "공사에 사용할 자재가 설계도서 및 시방서의 기준에 적합함을 확인하고 감리자나 발주처가 승인한 문서입니다. 제조사 인증서, 시험성적서, 견본 등을 첨부하여 제출합니다. 통역 시 '승인(approval)'과 '검토(review)'를 구분해야 하며, 베트남에서는 자재승인 없이 시공 시 무조건 재시공 조치되므로 승인 절차의 중요성을 강조해야 합니다. 한국보다 승인 기간이 길어 일정 관리에 주의가 필요합니다.",
        "meaningVi": "Tài liệu xác nhận vật liệu sử dụng trong thi công phù hợp với tiêu chuẩn trong hồ sơ thiết kế và thuyết minh kỹ thuật, được giám sát hoặc chủ đầu tư phê duyệt. Cần kèm theo: giấy chứng nhận nhà sản xuất, kết quả thử nghiệm, mẫu vật. Tuyệt đối không thi công trước khi có phê duyệt.",
        "context": "formal",
        "culturalNote": "한국에서는 자재승인을 구두나 이메일로 간소화하는 경우도 있으나, 베트남에서는 반드시 공식 문서(도장 날인)로 받아야 법적 효력이 있습니다. 베트남은 자재 원산지 증명과 품질인증서를 매우 엄격하게 요구하며, 중국산 자재는 별도 승인 절차가 필요한 경우가 많습니다. 승인 소요 기간이 한국(3~5일)보다 길어(7~14일) 일정에 반영해야 합니다.",
        "commonMistakes": [
            {
                "mistake": "giấy phê duyệt nguyên vật liệu",
                "correction": "giấy chứng nhận vật liệu (hoặc giấy phê duyệt vật liệu)",
                "explanation": "'nguyên vật liệu'는 공업 원료, 'vật liệu'는 건축 자재입니다. 건설에는 'vật liệu'를 씁니다."
            },
            {
                "mistake": "자재 검토서",
                "correction": "자재승인서",
                "explanation": "'검토'는 review, '승인'은 approval입니다. 승인(phê duyệt/chứng nhận)이 공식 용어입니다."
            },
            {
                "mistake": "material approval",
                "correction": "giấy chứng nhận vật liệu",
                "explanation": "영어를 그대로 쓰기보다 공식 베트남어 용어를 사용하세요."
            }
        ],
        "examples": [
            {
                "ko": "이 철근은 자재승인서를 받았나요?",
                "vi": "Cốt thép này đã có giấy chứng nhận vật liệu chưa?",
                "situation": "onsite"
            },
            {
                "ko": "자재승인서에 시험성적서와 견본을 첨부해서 제출하세요.",
                "vi": "Vui lòng nộp giấy chứng nhận vật liệu kèm theo kết quả thử nghiệm và mẫu vật.",
                "situation": "formal"
            },
            {
                "ko": "승인 안 받은 자재 쓰면 나중에 다 뜯어내야 돼요.",
                "vi": "Nếu dùng vật liệu chưa được phê duyệt, sau này phải phá bỏ hết.",
                "situation": "informal"
            }
        ],
        "relatedTerms": ["시험성적서", "품질인증서", "제조사증명서", "견본"]
    },
    {
        "slug": "bao-cao-thu-nghiem-chat-luong",
        "korean": "품질시험보고서",
        "vietnamese": "Báo cáo thử nghiệm chất lượng",
        "hanja": "品質試驗報告書",
        "hanjaReading": "물건 품(品) + 바탕 질(質) + 시험 시(試) + 시험할 험(驗) + 알릴 보(報) + 알릴 고(告) + 글 서(書)",
        "pronunciation": "품질시험보고서",
        "meaningKo": "콘크리트 강도, 철근 인장 강도, 용접부 비파괴검사 등 시공된 자재나 구조물의 품질을 시험한 결과를 정리한 공식 보고서입니다. 공인 시험기관이 발행하며 준공도서에 필수로 포함됩니다. 통역 시 '시험'과 '검사'를 구분해야 하며(시험=정량적 측정, 검사=육안 확인), 베트남에서는 시험 결과가 기준 미달 시 무조건 재시공되므로 시험 일정과 샘플링 방법을 사전에 명확히 협의해야 합니다. 한국보다 재시험 비용 분쟁이 잦습니다.",
        "meaningVi": "Báo cáo chính thức tổng hợp kết quả thử nghiệm chất lượng vật liệu hoặc kết cấu đã thi công (ví dụ: cường độ bê tông, cường độ kéo cốt thép, kiểm tra không phá hủy mối hàn, v.v.). Do cơ quan thử nghiệm được công nhận phát hành, là tài liệu bắt buộc trong hồ sơ hoàn công. Nếu kết quả không đạt tiêu chuẩn, bắt buộc phải thi công lại.",
        "context": "formal",
        "culturalNote": "한국은 자체 시험실 결과도 인정되는 경우가 많으나, 베트남에서는 정부 공인 시험기관(Vinacontrol, QUATEST 등)의 결과만 유효합니다. 베트남은 시험 빈도가 한국보다 높고(예: 콘크리트 시험 - 한국 150㎥당 1회, 베트남 100㎥당 1회), 시험 비용도 발주자와 시공자가 분담하는 비율이 프로젝트마다 다릅니다. 시험 불합격 시 재시험 비용 부담 주체에 대한 명확한 계약 조항이 필요합니다.",
        "commonMistakes": [
            {
                "mistake": "kết quả kiểm tra chất lượng",
                "correction": "báo cáo thử nghiệm chất lượng",
                "explanation": "'kiểm tra'는 일반 검사, 'thử nghiệm'은 공식 시험입니다. 시험 보고서는 'báo cáo thử nghiệm'입니다."
            },
            {
                "mistake": "giấy chứng nhận chất lượng",
                "correction": "báo cáo thử nghiệm chất lượng",
                "explanation": "'인증서'는 제품 인증, '시험보고서'는 실제 시험 결과 문서입니다. 다른 문서입니다."
            },
            {
                "mistake": "phúc tra chất lượng",
                "correction": "thử nghiệm chất lượng",
                "explanation": "'phúc tra'는 '재검사', 'thử nghiệm'은 '시험'입니다. 용도가 다릅니다."
            }
        ],
        "examples": [
            {
                "ko": "콘크리트 품질시험보고서는 타설 후 28일 뒤에 나옵니다.",
                "vi": "Báo cáo thử nghiệm chất lượng bê tông sẽ có sau 28 ngày kể từ khi đổ bê tông.",
                "situation": "formal"
            },
            {
                "ko": "이번 시험 결과가 기준 미달이라 해당 구간 재시공해야 합니다.",
                "vi": "Kết quả thử nghiệm lần này không đạt tiêu chuẩn nên phải thi công lại đoạn đó.",
                "situation": "onsite"
            },
            {
                "ko": "시험 성적서 언제 나와요? 준공도서에 넣어야 하는데.",
                "vi": "Báo cáo thử nghiệm khi nào ra được? Cần cho vào hồ sơ hoàn công.",
                "situation": "informal"
            }
        ],
        "relatedTerms": ["비파괴검사", "콘크리트강도시험", "자재승인서", "준공도서"]
    },
    {
        "slug": "bao-cao-kiem-tra-an-toan",
        "korean": "안전점검보고서",
        "vietnamese": "Báo cáo kiểm tra an toàn",
        "hanja": "安全點檢報告書",
        "hanjaReading": "편안 안(安) + 온전할 전(全) + 점 점(點) + 조사할 검(檢) + 알릴 보(報) + 알릴 고(告) + 글 서(書)",
        "pronunciation": "안전점검보고서",
        "meaningKo": "건설 현장의 안전 상태를 주기적으로 점검하고 그 결과를 기록한 보고서로, 위험 요소 발견 시 개선 조치 사항을 포함합니다. 한국은 월 1회 이상, 베트남은 주 1회 이상 작성이 의무입니다. 통역 시 '점검'과 '검사'를 구분하고(점검=정기 확인, 검사=공식 검증), 베트남에서는 외국인 근로자 안전교육 이수 증명도 함께 관리되므로 교육 기록과 점검 보고서를 연계하여 설명해야 합니다. 베트남은 안전 위반 시 현장 폐쇄 조치가 즉각 가능합니다.",
        "meaningVi": "Báo cáo ghi nhận kết quả kiểm tra định kỳ tình trạng an toàn tại công trường xây dựng, bao gồm các biện pháp khắc phục khi phát hiện yếu tố nguy hiểm. Việt Nam quy định phải lập ít nhất 1 lần/tuần. Cần quản lý cùng với hồ sơ đào tạo an toàn lao động (đặc biệt lao động nước ngoài). Vi phạm an toàn có thể dẫn đến đình chỉ công trường ngay lập tức.",
        "context": "formal",
        "culturalNote": "한국은 안전점검보고서 작성이 안전관리자의 주요 업무이나, 베트남에서는 현장소장이 직접 서명해야 법적 책임이 인정됩니다. 베트남은 외국인 근로자(특히 한국인 기술자)의 안전교육 이수 증명을 엄격히 요구하며, 미이수 시 개인과 회사 모두 벌금이 부과됩니다. 한국은 사후 시정 명령이 일반적이나, 베트남은 즉시 공사 중단 명령이 가능하여 일정 차질이 큽니다.",
        "commonMistakes": [
            {
                "mistake": "báo cáo kiểm định an toàn",
                "correction": "báo cáo kiểm tra an toàn",
                "explanation": "'kiểm định'은 공식 인증 검사, 'kiểm tra'는 일반 점검입니다. 안전점검은 'kiểm tra'입니다."
            },
            {
                "mistake": "안전 검사 보고서",
                "correction": "안전점검보고서",
                "explanation": "'점검'은 정기적 확인, '검사'는 공식 검증입니다. 안전 업무는 '점검'이 표준 용어입니다."
            },
            {
                "mistake": "sổ kiểm tra",
                "correction": "báo cáo kiểm tra an toàn",
                "explanation": "'노트'가 아니라 '보고서(báo cáo)' 형태로 작성해야 법적 효력이 있습니다."
            }
        ],
        "examples": [
            {
                "ko": "이번 주 안전점검보고서는 금요일까지 제출해 주세요.",
                "vi": "Vui lòng nộp báo cáo kiểm tra an toàn tuần này trước thứ Sáu.",
                "situation": "formal"
            },
            {
                "ko": "점검 결과 안전난간이 누락된 구간이 발견되었습니다.",
                "vi": "Kết quả kiểm tra phát hiện có đoạn thiếu lan can an toàn.",
                "situation": "onsite"
            },
            {
                "ko": "안전모 안 쓴 사람 있으면 점검 보고서에 꼭 기록하세요.",
                "vi": "Nếu có người không đội mũ bảo hộ, nhớ ghi vào báo cáo kiểm tra.",
                "situation": "informal"
            }
        ],
        "relatedTerms": ["안전교육일지", "위험성평가서", "안전관리계획서", "사고보고서"]
    },
    {
        "slug": "so-anh-thi-cong",
        "korean": "공사사진대지",
        "vietnamese": "Sổ ảnh thi công",
        "hanja": "工事寫眞臺紙",
        "hanjaReading": "工장 공(工) + 일 사(事) + 베낄 사(寫) + 참 진(眞) + 대 대(臺) + 종이 지(紙)",
        "pronunciation": "공사사진대지",
        "meaningKo": "공사 진행 과정을 사진으로 기록하고 날짜, 위치, 공종 등을 표기하여 정리한 문서로, 준공도서의 필수 구성 요소입니다. 숨겨지는 구조물(매립 배관, 철근 배근 등)은 시공 중 사진 촬영이 의무입니다. 통역 시 '사진대지'를 직역하면 이해가 안 되므로 '공사 사진 기록부(sổ ảnh thi công)'로 설명해야 하며, 베트남에서는 사진에 반드시 날짜 스탬프와 좌표(GPS)를 포함해야 하는 경우가 많아 촬영 방법을 명확히 안내해야 합니다.",
        "meaningVi": "Tài liệu ghi nhận quá trình thi công bằng ảnh, ghi rõ ngày tháng, vị trí, hạng mục công việc, là thành phần bắt buộc trong hồ sơ hoàn công. Các kết cấu bị che khuất (đường ống chôn ngầm, bố trí cốt thép, v.v.) bắt buộc phải chụp ảnh trong khi thi công. Ảnh cần có đóng dấu ngày giờ và tọa độ GPS (tùy quy định dự án).",
        "context": "formal",
        "culturalNote": "한국에서는 공사사진을 PPT나 PDF로 간단히 정리하는 경우가 많으나, 베트남에서는 인쇄하여 제본한 '사진첩(앨범)' 형태를 선호하며, 표지에 프로젝트명, 공종, 작성자를 명기해야 합니다. 베트남은 사진 원본 파일(RAW, JPEG 원본)도 함께 제출하도록 요구하는 경우가 있어 파일 관리가 중요합니다. 한국은 주요 공정만 촬영하지만, 베트남은 전 공정을 빠짐없이 촬영해야 분쟁 시 유리합니다.",
        "commonMistakes": [
            {
                "mistake": "album ảnh công trình",
                "correction": "sổ ảnh thi công",
                "explanation": "'앨범'은 일상용, '공사 사진 기록부(sổ)'가 공식 문서 용어입니다."
            },
            {
                "mistake": "사진 기록부",
                "correction": "공사사진대지",
                "explanation": "한국 건설 표준 용어는 '공사사진대지'입니다. '기록부'는 일반적 표현입니다."
            },
            {
                "mistake": "ảnh hiện trường",
                "correction": "sổ ảnh thi công",
                "explanation": "'현장 사진'은 일반 사진, '공사 사진 기록부'는 공식 문서입니다."
            }
        ],
        "examples": [
            {
                "ko": "매립되는 배관은 공사사진대지에 꼭 남겨주세요.",
                "vi": "Đường ống chôn ngầm nhớ chụp ảnh để vào sổ ảnh thi công.",
                "situation": "onsite"
            },
            {
                "ko": "공사사진대지는 공종별로 구분해서 제본해 주시기 바랍니다.",
                "vi": "Vui lòng đóng quyển sổ ảnh thi công theo từng hạng mục công việc.",
                "situation": "formal"
            },
            {
                "ko": "이 부분 사진 안 찍었으면 나중에 증명 못 해요.",
                "vi": "Nếu không chụp ảnh phần này, sau này không chứng minh được.",
                "situation": "informal"
            }
        ],
        "relatedTerms": ["준공도서", "시공상세도", "검사조서", "촬영대장"]
    },
    {
        "slug": "bien-ban-nghiem-thu",
        "korean": "검사조서",
        "vietnamese": "Biên bản nghiệm thu",
        "hanja": "檢査調書",
        "hanjaReading": "조사할 검(檢) + 조사할 사(査) + 고를 조(調) + 글 서(書)",
        "pronunciation": "검사조서",
        "meaningKo": "시공된 공사 내용이 설계도서 및 계약 내용에 적합한지 검사한 결과를 기록한 공식 문서로, 발주자, 감리자, 시공자가 함께 서명합니다. 준공검사뿐 아니라 중간검사(은폐 구조물 등)에도 작성됩니다. 통역 시 '검사조서'를 직역하면 어색하므로 '검수 확인서(biên bản nghiệm thu)'로 설명하고, 베트남에서는 서명과 도장이 모두 필요하며 서명자의 직함과 이름을 정확히 기재해야 법적 효력이 발생한다는 점을 강조해야 합니다.",
        "meaningVi": "Tài liệu chính thức ghi nhận kết quả kiểm tra xem nội dung thi công có phù hợp với hồ sơ thiết kế và hợp đồng hay không, được chủ đầu tư, giám sát và nhà thầu cùng ký. Lập cho cả nghiệm thu hoàn thành và nghiệm thu giai đoạn (kết cấu bị che khuất, v.v.). Cần có cả chữ ký và dấu đỏ, ghi rõ chức danh và tên người ký để có hiệu lực pháp lý.",
        "context": "formal",
        "culturalNote": "한국에서는 검사조서를 간략히 작성하는 경우가 많으나, 베트남에서는 매우 상세하게(불합격 사유, 개선 조치, 재검사 일정 등) 작성해야 하며, 불합격 항목이 있으면 '조건부 합격' 처리가 불가능하고 반드시 재검사를 거쳐야 합니다. 베트남은 검사조서 원본(bản gốc)을 발주자가 보관하고 사본을 시공자에게 교부하는데, 원본 없이는 법적 효력이 없으므로 사본 수령 시 '사본(bản sao)' 표기를 확인해야 합니다.",
        "commonMistakes": [
            {
                "mistake": "biên bản kiểm tra",
                "correction": "biên bản nghiệm thu",
                "explanation": "'kiểm tra'는 일반 점검, 'nghiệm thu'는 공식 검수입니다. 검사조서는 'nghiệm thu'입니다."
            },
            {
                "mistake": "검수서",
                "correction": "검사조서",
                "explanation": "'검수서'는 물품 인수증, '검사조서'는 공사 검사 기록입니다. 건설에는 '검사조서'를 씁니다."
            },
            {
                "mistake": "giấy xác nhận nghiệm thu",
                "correction": "biên bản nghiệm thu",
                "explanation": "'확인서'는 간단한 증명서, '의사록(biên bản)'은 공식 회의록/검수 기록입니다."
            }
        ],
        "examples": [
            {
                "ko": "오늘 철근 배근 검사조서 작성하겠습니다. 참석 부탁드립니다.",
                "vi": "Hôm nay sẽ lập biên bản nghiệm thu bố trí cốt thép. Vui lòng tham dự.",
                "situation": "formal"
            },
            {
                "ko": "검사 결과 불합격 항목이 있어서 재시공 후 재검사하겠습니다.",
                "vi": "Kết quả nghiệm thu có hạng mục không đạt nên sẽ thi công lại và nghiệm thu lại.",
                "situation": "onsite"
            },
            {
                "ko": "검사조서에 도장 안 찍으면 인정 안 된대요.",
                "vi": "Nghe nói biên bản nghiệm thu không đóng dấu thì không được công nhận.",
                "situation": "informal"
            }
        ],
        "relatedTerms": ["준공검사", "중간검사", "품질시험보고서", "준공도서"]
    },
    {
        "slug": "ke-hoach-thi-cong",
        "korean": "시공계획서",
        "vietnamese": "Kế hoạch thi công",
        "hanja": "施工計劃書",
        "hanjaReading": "베풀 시(施) + 工장 공(工) + 셀 계(計) + 꾀할 획(劃) + 글 서(書)",
        "pronunciation": "시공계획서",
        "meaningKo": "공사를 어떻게 진행할 것인지(공법, 장비, 인력, 일정, 안전 대책 등)를 구체적으로 기술한 계획 문서로, 착공 전 발주자와 감리자의 승인을 받아야 합니다. 통역 시 '계획서'와 '제안서'를 구분하고(계획서=실행 계획, 제안서=입찰용 제안), 베트남에서는 시공계획서 미승인 상태로 공사 시작 시 즉시 공사 중단 명령이 내려지므로 승인 일정을 반드시 확보해야 합니다. 한국보다 승인 과정이 까다롭고 수정 요구가 많습니다.",
        "meaningVi": "Tài liệu mô tả chi tiết cách thức tiến hành thi công (phương pháp, thiết bị, nhân lực, tiến độ, biện pháp an toàn, v.v.), phải được chủ đầu tư và giám sát phê duyệt trước khi khởi công. Nếu thi công khi chưa có phê duyệt kế hoạch, sẽ bị đình chỉ công trình ngay lập tức. Quy trình phê duyệt ở Việt Nam khắt khe hơn Hàn Quốc và thường yêu cầu sửa đổi nhiều lần.",
        "context": "formal",
        "culturalNote": "한국에서는 시공계획서를 입찰 시 제출하고 실제 시공 시 간략히 수정하는 경우가 많으나, 베트남에서는 착공 전 새로 작성하여 승인받는 것이 원칙입니다. 베트남은 시공계획서에 '환경 영향 최소화 방안', '지역 주민 피해 방지 대책'을 반드시 포함해야 하며, 야간/휴일 공사 계획은 별도 승인이 필요합니다. 한국은 A4 10~20페이지 분량이 일반적이나, 베트남은 50~100페이지 이상의 상세한 계획서를 요구합니다.",
        "commonMistakes": [
            {
                "mistake": "phương án thi công",
                "correction": "kế hoạch thi công",
                "explanation": "'phương án'은 '방안/방법', 'kế hoạch'은 '계획'입니다. 공식 문서는 'kế hoạch'입니다."
            },
            {
                "mistake": "đề xuất thi công",
                "correction": "kế hoạch thi công",
                "explanation": "'제안서(đề xuất)'와 '계획서(kế hoạch)'는 다릅니다. 착공 후는 '계획서'입니다."
            },
            {
                "mistake": "계획안",
                "correction": "시공계획서",
                "explanation": "'계획안'은 일반 계획, '시공계획서'는 공식 문서입니다. 건설에는 '시공계획서'를 씁니다."
            }
        ],
        "examples": [
            {
                "ko": "착공 전까지 시공계획서 승인을 받아야 합니다.",
                "vi": "Phải được phê duyệt kế hoạch thi công trước khi khởi công.",
                "situation": "formal"
            },
            {
                "ko": "시공계획서에 안전 대책이 미흡하다고 수정 요청이 왔습니다.",
                "vi": "Có yêu cầu sửa đổi kế hoạch thi công vì biện pháp an toàn chưa đầy đủ.",
                "situation": "onsite"
            },
            {
                "ko": "이 공법은 시공계획서에 없는데 괜찮을까요?",
                "vi": "Phương pháp này không có trong kế hoạch thi công, có sao không nhỉ?",
                "situation": "informal"
            }
        ],
        "relatedTerms": ["공정표", "안전관리계획서", "품질관리계획서", "가설계획서"]
    },
    {
        "slug": "de-xuat-ky-thuat",
        "korean": "기술제안서",
        "vietnamese": "Đề xuất kỹ thuật",
        "hanja": "技術提案書",
        "hanjaReading": "재주 기(技) + 재주 술(術) + 끌어낼 제(提) + 책상 안(案) + 글 서(書)",
        "pronunciation": "기술제안서",
        "meaningKo": "공사 입찰 시 시공 방법, 공사 기간, 품질 관리 방안 등을 제안하는 문서로, 발주자가 입찰자의 기술력을 평가하는 주요 자료입니다. 가격 제안서와 함께 제출되며, 기술 평가 점수가 낙찰에 큰 영향을 미칩니다. 통역 시 '제안서'와 '계획서'를 구분하고(제안서=입찰용, 계획서=실행용), 베트남에서는 기술제안서의 형식과 분량이 매우 엄격하게 규정되어 있어 입찰 공고문(HSMT)을 정확히 따라야 탈락을 피할 수 있음을 강조해야 합니다.",
        "meaningVi": "Tài liệu đề xuất phương pháp thi công, thời gian thi công, phương án quản lý chất lượng, v.v. khi dự thầu, là tài liệu chính để chủ đầu tư đánh giá năng lực kỹ thuật của nhà thầu. Nộp cùng với đề xuất giá, điểm đánh giá kỹ thuật ảnh hưởng lớn đến kết quả trúng thầu. Hình thức và khối lượng đề xuất kỹ thuật ở Việt Nam được quy định rất chặt chẽ, phải tuân thủ chính xác hồ sơ mời thầu (HSMT) để tránh bị loại.",
        "context": "formal",
        "culturalNote": "한국에서는 기술제안서를 자유롭게 작성하는 편이나, 베트남에서는 입찰 공고문(HSMT - Hồ Sơ Mời Thầu)에 명시된 목차, 페이지 제한, 글꼴, 여백까지 지켜야 하며, 형식 위반 시 개봉도 안 하고 탈락시킵니다. 베트남은 기술 점수 비중이 한국(보통 30~40%)보다 높아(50~70%) 기술제안서 품질이 낙찰의 핵심입니다. 베트남어와 영어 병기가 요구되는 경우가 많고, 공증 또는 영사 확인이 필요한 서류도 있습니다.",
        "commonMistakes": [
            {
                "mistake": "제안서",
                "correction": "기술제안서",
                "explanation": "단순히 '제안서'라고 하면 가격 제안서와 혼동됩니다. '기술제안서'로 명확히 구분하세요."
            },
            {
                "mistake": "đề nghị kỹ thuật",
                "correction": "đề xuất kỹ thuật",
                "explanation": "'đề nghị'는 '요청', 'đề xuất'은 '제안'입니다. 입찰 문서는 'đề xuất'입니다."
            },
            {
                "mistake": "hồ sơ kỹ thuật",
                "correction": "đề xuất kỹ thuật",
                "explanation": "'서류(hồ sơ)'는 일반 문서, '제안서(đề xuất)'는 제안 문서입니다. 입찰에는 'đề xuất'입니다."
            }
        ],
        "examples": [
            {
                "ko": "기술제안서는 입찰 공고문의 목차를 정확히 따라 작성하세요.",
                "vi": "Đề xuất kỹ thuật phải tuân thủ chính xác mục lục trong hồ sơ mời thầu.",
                "situation": "formal"
            },
            {
                "ko": "우리 기술제안서 점수가 높아서 1순위로 선정되었습니다.",
                "vi": "Điểm đề xuất kỹ thuật của chúng ta cao nên được xếp hạng 1.",
                "situation": "onsite"
            },
            {
                "ko": "제안서 분량 초과하면 탈락된대요. 페이지 수 확인하세요.",
                "vi": "Nghe nói vượt quá khối lượng đề xuất thì bị loại. Kiểm tra số trang đi.",
                "situation": "informal"
            }
        ],
        "relatedTerms": ["입찰공고", "시공계획서", "실시설계", "낙찰자선정"]
    }
]

# 타겟 파일 경로
target_file = os.path.join(
    "/Users/mac/Documents/claude_code/projects/vn.epicstage.co.kr/src/data/terms",
    "construction.json"
)

print(f"Target file: {target_file}")
print(f"Terms to add: {len(data)}")
print("Ready to execute. DO NOT RUN - just write the file.")
