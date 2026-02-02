#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
건설문서양식 (Construction Documents/Forms) 용어 추가 스크립트
Tier S 품질 기준 준수
"""

import json
import os

def main():
    # 1. 파일 경로 설정 (CRITICAL RULE #1)
    file_path = os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', 'data', 'terms', 'construction.json')

    # 2. 기존 데이터 로드 (CRITICAL RULE #2)
    with open(file_path, 'r', encoding='utf-8') as f:
        data = json.load(f)  # data is a LIST, not dict!

    # 3. 기존 slug 추출 (CRITICAL RULE #4)
    existing_slugs = {t['slug'] for t in data}

    # 4. 새 용어 정의 (건설문서양식 테마)
    new_terms = [
        {
            "slug": "nhat-ky-cong-trinh",
            "korean": "공사일지",
            "vietnamese": "nhật ký công trình",
            "hanja": "工事日誌",
            "hanjaReading": "工(장인 공) 事(일 사) 日(날 일) 誌(기록할 지)",
            "pronunciation": "응앗 끼 꽁 찡",
            "meaningKo": "건설 현장에서 매일 작성하는 공사 진행 상황 기록. 통역 시 '일지(nhật ký)'는 베트남에서도 매우 공식적인 문서로 인식되므로, 작성 의무와 법적 효력을 강조해야 함. '공사(công trình)'는 '건설 프로젝트' 전체를 의미하므로 단순 '공사(công việc)'와 혼동 주의. 현장 감독이 매일 작성해야 하는 법정 문서임을 명확히 전달.",
            "meaningVi": "Bản ghi chép hàng ngày về tình hình tiến độ thi công, sự kiện, thời tiết, nhân lực và vật tư tại công trường xây dựng. Là tài liệu pháp lý quan trọng, phải được lưu trữ cẩn thận và có thể dùng làm bằng chứng khi có tranh chấp.",
            "context": "매일 작성 의무, 법적 증거 효력",
            "culturalNote": "한국: 공사일지는 법적으로 5년 보관 의무. 베트남: 'sổ nhật ký công trình'이라고도 하며, 감리 검토 후 서명 필수. 양국 모두 공사 분쟁 시 중요한 법적 증거로 활용되므로 작성 누락 시 처벌 대상.",
            "commonMistakes": [
                {
                    "mistake": "công việc hàng ngày (일상 업무)",
                    "correction": "nhật ký công trình (공사일지)",
                    "explanation": "'công việc'는 일반 업무, 'công trình'은 건설 프로젝트 전체를 의미"
                },
                {
                    "mistake": "báo cáo ngày (일일 보고서)",
                    "correction": "nhật ký công trình (공사일지)",
                    "explanation": "'báo cáo'는 보고서, 'nhật ký'는 일지라는 공식 문서 형식"
                },
                {
                    "mistake": "sổ ghi chép (메모장)",
                    "correction": "nhật ký công trình (공사일지)",
                    "explanation": "법적 문서이므로 공식 명칭 사용 필수"
                }
            ],
            "examples": [
                {
                    "ko": "오늘 공사일지 작성하셨나요?",
                    "vi": "Hôm nay anh đã viết nhật ký công trình chưa?",
                    "situation": "onsite"
                },
                {
                    "ko": "공사일지에는 날씨, 인원, 작업 내용을 반드시 기재해야 합니다.",
                    "vi": "Trong nhật ký công trình phải ghi đầy đủ thời tiết, nhân lực và nội dung thi công.",
                    "situation": "formal"
                },
                {
                    "ko": "감리가 공사일지 서명 안 해줘서 작업 못 시작했어.",
                    "vi": "Giám sát chưa ký nhật ký công trình nên không thể bắt đầu làm được.",
                    "situation": "informal"
                }
            ],
            "relatedTerms": ["bao-cao-tien-do", "bien-ban-hop", "phieu-kiem-tra"]
        },
        {
            "slug": "ke-hoach-thi-cong",
            "korean": "시공계획서",
            "vietnamese": "kế hoạch thi công",
            "hanja": "施工計劃書",
            "hanjaReading": "施(베풀 시) 工(장인 공) 計(셀 계) 劃(그을 획) 書(글 서)",
            "pronunciation": "께 호억 티 꽁",
            "meaningKo": "공사 시작 전 작성하는 상세 시공 방법 및 일정 계획서. 통역 시 '계획서(kế hoạch)'는 단순 플랜이 아니라 공식 승인받아야 하는 문서임을 강조. 베트남에서는 '방안(phương án)'이라는 표현도 혼용되지만, 공식 문서명은 'kế hoạch thi công'. 안전, 품질, 환경 관리 계획 모두 포함되어야 함.",
            "meaningVi": "Tài liệu chi tiết về phương pháp, trình tự, tiến độ, nhân lực, thiết bị và biện pháp an toàn cho từng hạng mục công việc. Phải được phê duyệt bởi chủ đầu tư và giám sát trước khi thi công.",
            "context": "공사 착수 전 제출 및 승인 필수",
            "culturalNote": "한국: 시공계획서는 착공 신고 시 필수 첨부 서류. 베트남: 'Kế hoạch tổng thể' (총괄 계획)와 'Kế hoạch chi tiết' (상세 계획)으로 구분. 양국 모두 변경 시 재승인 필요하며, 무단 변경 시 공사 중지 사유가 됨.",
            "commonMistakes": [
                {
                    "mistake": "phương án thi công (시공방안)",
                    "correction": "kế hoạch thi công (시공계획서)",
                    "explanation": "'phương án'은 방법론, 'kế hoạch'는 일정 포함한 종합 계획"
                },
                {
                    "mistake": "bản vẽ thi công (시공도면)",
                    "correction": "kế hoạch thi công (시공계획서)",
                    "explanation": "도면이 아니라 문서 형태의 계획서"
                },
                {
                    "mistake": "lịch trình thi công (시공 일정)",
                    "correction": "kế hoạch thi công (시공계획서)",
                    "explanation": "일정만이 아닌 방법, 안전, 품질 계획 모두 포함"
                }
            ],
            "examples": [
                {
                    "ko": "시공계획서 검토 완료하면 연락 주세요.",
                    "vi": "Xem xét xong kế hoạch thi công thì liên hệ cho tôi nhé.",
                    "situation": "formal"
                },
                {
                    "ko": "이 시공계획서로는 승인 못 받아. 안전 대책 보완해.",
                    "vi": "Kế hoạch thi công này không được phê duyệt đâu. Bổ sung biện pháp an toàn đi.",
                    "situation": "onsite"
                },
                {
                    "ko": "설계 변경으로 시공계획서 다시 작성해야 합니다.",
                    "vi": "Do thay đổi thiết kế, phải làm lại kế hoạch thi công.",
                    "situation": "formal"
                }
            ],
            "relatedTerms": ["nhat-ky-cong-trinh", "bao-cao-tien-do", "ban-ve-shop"]
        },
        {
            "slug": "bao-cao-tien-do",
            "korean": "공정보고서",
            "vietnamese": "báo cáo tiến độ",
            "hanja": "工程報告書",
            "hanjaReading": "工(장인 공) 程(법 정) 報(알릴 보) 告(고할 고) 書(글 서)",
            "pronunciation": "바오 까오 띠엔 도",
            "meaningKo": "주기적으로 작성하는 공사 진행률 보고서. 통역 시 '공정(tiến độ)'은 단순 진행이 아닌 계획 대비 실제 진행률을 의미함을 명확히 해야 함. 베트남에서는 주간, 월간 보고서를 구분하여 'báo cáo tuần' (주간), 'báo cáo tháng' (월간)으로 표현. 지연 사유와 만회 대책을 반드시 포함해야 함.",
            "meaningVi": "Báo cáo định kỳ về tỷ lệ hoàn thành công việc so với kế hoạch, bao gồm các hạng mục đã làm, đang làm, tồn đọng, nguyên nhân chậm tiến độ và biện pháp khắc phục. Thường có báo cáo tuần, báo cáo tháng.",
            "context": "주간/월간 정기 보고, 지연 시 대책 필수",
            "culturalNote": "한국: 공정률은 기성 대비 퍼센트로 표시. 베트남: 공정 지연 시 벌금 조항이 계약서에 명시되는 경우 많음. 한국은 준공 전체 일정 관리 중시, 베트남은 마일스톤별 관리 선호.",
            "commonMistakes": [
                {
                    "mistake": "báo cáo công việc (업무 보고서)",
                    "correction": "báo cáo tiến độ (공정보고서)",
                    "explanation": "'công việc'는 일반 업무, 'tiến độ'는 진행률에 초점"
                },
                {
                    "mistake": "báo cáo tình hình (상황 보고서)",
                    "correction": "báo cáo tiến độ (공정보고서)",
                    "explanation": "공사 진행률 보고서는 전문 용어 사용 필수"
                },
                {
                    "mistake": "báo cáo kết quả (결과 보고서)",
                    "correction": "báo cáo tiến độ (공정보고서)",
                    "explanation": "'kết quả'는 완료 후 결과, 'tiến độ'는 진행 중 현황"
                }
            ],
            "examples": [
                {
                    "ko": "이번 주 공정보고서 금요일까지 제출해 주세요.",
                    "vi": "Báo cáo tiến độ tuần này nộp trước thứ Sáu nhé.",
                    "situation": "formal"
                },
                {
                    "ko": "공정 5% 지연됐는데 만회 대책이 뭐야?",
                    "vi": "Tiến độ chậm 5% rồi, biện pháp khắc phục là gì?",
                    "situation": "onsite"
                },
                {
                    "ko": "월간 공정보고서에 사진 자료도 첨부하세요.",
                    "vi": "Báo cáo tiến độ tháng cũng đính kèm hình ảnh nữa.",
                    "situation": "formal"
                }
            ],
            "relatedTerms": ["nhat-ky-cong-trinh", "ke-hoach-thi-cong", "so-theo-doi"]
        },
        {
            "slug": "phieu-yeu-cau",
            "korean": "의뢰서",
            "vietnamese": "phiếu yêu cầu",
            "hanja": "依賴書",
            "hanjaReading": "依(의지할 의) 賴(의뢰할 뢰) 書(글 서)",
            "pronunciation": "피에우 예우 까우",
            "meaningKo": "특정 업무나 자재를 요청하는 공식 문서. 통역 시 '의뢰(yêu cầu)'는 단순 요청이 아닌 공식 신청 절차임을 명확히 해야 함. 베트남에서는 'đơn yêu cầu' (요청서)와 혼용되지만 현장에서는 'phiếu' (전표) 형식 선호. 승인 라인과 결재 날짜 기록 필수.",
            "meaningVi": "Giấy tờ chính thức để yêu cầu vật tư, thiết bị, nhân lực hoặc hỗ trợ kỹ thuật. Phải có chữ ký người yêu cầu và người phê duyệt, kèm thời gian cần thiết. Thường dùng trong quản lý nội bộ công trường.",
            "context": "자재, 장비, 인력 요청 시 작성",
            "culturalNote": "한국: 의뢰서는 주로 내부 결재용. 베트남: 'phiếu' 문화가 발달해 있어 모든 요청을 서면화. 한국은 구두 요청 후 확인서 작성도 가능하지만, 베트남은 사전 서면 요청 원칙.",
            "commonMistakes": [
                {
                    "mistake": "đơn xin (신청서)",
                    "correction": "phiếu yêu cầu (의뢰서)",
                    "explanation": "'đơn xin'은 개인이 조직에 신청, 'phiếu yêu cầu'는 업무상 요청"
                },
                {
                    "mistake": "giấy đề nghị (건의서)",
                    "correction": "phiếu yêu cầu (의뢰서)",
                    "explanation": "'đề nghị'는 제안/건의, 'yêu cầu'는 필요에 의한 요청"
                },
                {
                    "mistake": "phiếu đặt hàng (주문서)",
                    "correction": "phiếu yêu cầu (의뢰서)",
                    "explanation": "'đặt hàng'는 외부 구매, 'yêu cầu'는 내부 요청"
                }
            ],
            "examples": [
                {
                    "ko": "크레인 사용 의뢰서 내일까지 제출하세요.",
                    "vi": "Nộp phiếu yêu cầu sử dụng cẩu trước ngày mai.",
                    "situation": "formal"
                },
                {
                    "ko": "의뢰서 없으면 자재 못 내줘.",
                    "vi": "Không có phiếu yêu cầu thì không xuất vật tư được.",
                    "situation": "onsite"
                },
                {
                    "ko": "추가 인력 의뢰서에 소장님 결재 받으셨어요?",
                    "vi": "Phiếu yêu cầu thêm nhân lực đã có chữ ký giám đốc chưa?",
                    "situation": "formal"
                }
            ],
            "relatedTerms": ["giay-de-nghi", "so-theo-doi", "phieu-kiem-tra"]
        },
        {
            "slug": "bien-ban-hop",
            "korean": "회의록",
            "vietnamese": "biên bản họp",
            "hanja": "會議錄",
            "hanjaReading": "會(모일 회) 議(의논할 의) 錄(기록할 록)",
            "pronunciation": "비엔 반 홉",
            "meaningKo": "회의 내용과 결정 사항을 기록한 공식 문서. 통역 시 '회의록(biên bản họp)'은 단순 메모가 아닌 법적 효력 있는 공식 기록임을 강조. 베트남에서 'biên bản'은 '의사록, 합의서' 의미가 강하므로 참석자 전원 서명 필수. 결정 사항 미이행 시 책임 소재 확인 자료로 활용.",
            "meaningVi": "Bản ghi chép chính thức về nội dung thảo luận, quyết định và phân công nhiệm vụ trong cuộc họp. Phải có chữ ký của tất cả người tham dự, có giá trị pháp lý để làm bằng chứng cho các cam kết và thỏa thuận.",
            "context": "회의 후 작성, 참석자 전원 서명 필수",
            "culturalNote": "한국: 회의록은 주로 결정 사항 위주 기록. 베트남: 'biên bản'은 합의서 성격이 강해 토론 내용까지 상세 기록. 양국 모두 중요 회의는 녹음/녹화 병행하지만, 베트남은 서면 서명 문화가 더 강함.",
            "commonMistakes": [
                {
                    "mistake": "bản ghi chép (메모)",
                    "correction": "biên bản họp (회의록)",
                    "explanation": "'ghi chép'은 개인 메모, 'biên bản'은 공식 의사록"
                },
                {
                    "mistake": "tóm tắt cuộc họp (회의 요약)",
                    "correction": "biên bản họp (회의록)",
                    "explanation": "요약이 아닌 공식 기록 문서"
                },
                {
                    "mistake": "kết luận họp (회의 결론)",
                    "correction": "biên bản họp (회의록)",
                    "explanation": "결론만이 아닌 전체 과정 기록"
                }
            ],
            "examples": [
                {
                    "ko": "회의록 검토하시고 서명해 주세요.",
                    "vi": "Xem biên bản họp và ký tên giúp tôi.",
                    "situation": "formal"
                },
                {
                    "ko": "지난주 회의록 보니까 네가 담당이던데?",
                    "vi": "Xem biên bản họp tuần trước thì anh phụ trách mà?",
                    "situation": "informal"
                },
                {
                    "ko": "회의록에 없는 내용은 합의된 것 아닙니다.",
                    "vi": "Nội dung không có trong biên bản họp thì không phải là thỏa thuận.",
                    "situation": "formal"
                }
            ],
            "relatedTerms": ["nhat-ky-cong-trinh", "bao-cao-tien-do", "giay-de-nghi"]
        },
        {
            "slug": "ban-ve-shop",
            "korean": "시공상세도",
            "vietnamese": "bản vẽ shop",
            "hanja": "施工詳細圖",
            "hanjaReading": "施(베풀 시) 工(장인 공) 詳(자세할 상) 細(가늘 세) 圖(그림 도)",
            "pronunciation": "반 베 솝",
            "meaningKo": "실제 제작 및 시공을 위한 상세 도면 (Shop Drawing). 통역 시 베트남에서는 영어 'shop'을 그대로 사용하여 'bản vẽ shop'이라고 함. 설계도(bản vẽ thiết kế)보다 더 구체적인 제작 치수, 자재 규격, 시공 방법이 표시됨. 시공 전 감리 승인 필수.",
            "meaningVi": "Bản vẽ chi tiết để chế tạo và lắp đặt, thể hiện kích thước thực tế, vật liệu cụ thể, phương pháp thi công. Chi tiết hơn bản vẽ thiết kế, phải được nhà thầu lập và giám sát phê duyệt trước khi sản xuất hoặc thi công.",
            "context": "제작/시공 전 작성 및 승인 필수",
            "culturalNote": "한국: 시공상세도는 샵드로잉을 한글화한 표현. 베트남: 'bản vẽ shop' 또는 'bản vẽ thi công chi tiết'로 표현. 양국 모두 설계 의도와 불일치 시 재작성 필요하며, 무단 변경 시 하자 책임 소재 분쟁 발생 가능.",
            "commonMistakes": [
                {
                    "mistake": "bản vẽ thiết kế (설계도)",
                    "correction": "bản vẽ shop (시공상세도)",
                    "explanation": "'thiết kế'는 기본설계, 'shop'은 제작용 상세도"
                },
                {
                    "mistake": "bản vẽ thi công (시공도)",
                    "correction": "bản vẽ shop (시공상세도)",
                    "explanation": "시공도는 포괄적 개념, shop drawing은 제작 상세도"
                },
                {
                    "mistake": "bản vẽ kỹ thuật (기술 도면)",
                    "correction": "bản vẽ shop (시공상세도)",
                    "explanation": "현장에서는 'shop' 용어 사용이 표준"
                }
            ],
            "examples": [
                {
                    "ko": "철골 시공상세도 검토 완료했습니까?",
                    "vi": "Đã xem xét xong bản vẽ shop kết cấu thép chưa?",
                    "situation": "formal"
                },
                {
                    "ko": "샵드로잉 승인 안 나면 제작 못 해.",
                    "vi": "Bản vẽ shop chưa được duyệt thì không sản xuất được.",
                    "situation": "onsite"
                },
                {
                    "ko": "설계도랑 시공상세도가 달라서 확인 좀 해주세요.",
                    "vi": "Bản vẽ thiết kế và bản vẽ shop khác nhau, kiểm tra giúp tôi.",
                    "situation": "formal"
                }
            ],
            "relatedTerms": ["ke-hoach-thi-cong", "phieu-kiem-tra", "bien-ban-hop"]
        },
        {
            "slug": "phieu-kiem-tra",
            "korean": "검사표",
            "vietnamese": "phiếu kiểm tra",
            "hanja": "檢査表",
            "hanjaReading": "檢(검사할 검) 査(조사할 사) 表(표 표)",
            "pronunciation": "피에우 끼엠 짜",
            "meaningKo": "품질, 안전, 시공 상태를 점검하기 위한 체크리스트 양식. 통역 시 '검사표(phiếu kiểm tra)'는 단순 확인이 아닌 합격/불합격 판정을 위한 공식 양식임을 명확히 해야 함. 베트남에서는 항목별 체크박스 형식으로 작성하며, 불합격 시 재검사 일정까지 기재. 검사자 서명 필수.",
            "meaningVi": "Mẫu phiếu để kiểm tra chất lượng, an toàn và tiến độ thi công theo từng hạng mục. Có danh sách các tiêu chí cần kiểm tra, ô đánh dấu đạt/không đạt, ghi chú và chữ ký người kiểm tra. Dùng để đảm bảo thi công đúng quy chuẩn.",
            "context": "공정별 검사 시 작성, 합격 판정 기록",
            "culturalNote": "한국: 검사표는 자체 점검과 감리 점검 구분. 베트남: 'kiểm tra' (일반 점검)과 'nghiệm thu' (준공 검사) 구분 명확. 양국 모두 불합격 시 시정 후 재검사 필수이며, 검사표 없이 다음 공정 진행 불가.",
            "commonMistakes": [
                {
                    "mistake": "danh sách kiểm tra (점검 목록)",
                    "correction": "phiếu kiểm tra (검사표)",
                    "explanation": "목록이 아닌 공식 서식 양식"
                },
                {
                    "mistake": "bảng đánh giá (평가표)",
                    "correction": "phiếu kiểm tra (검사표)",
                    "explanation": "'đánh giá'는 평가, 'kiểm tra'는 검사"
                },
                {
                    "mistake": "giấy xác nhận (확인서)",
                    "correction": "phiếu kiểm tra (검사표)",
                    "explanation": "확인서는 결과, 검사표는 과정 문서"
                }
            ],
            "examples": [
                {
                    "ko": "콘크리트 타설 전 검사표 작성해 주세요.",
                    "vi": "Trước khi đổ bê tông, điền phiếu kiểm tra giúp tôi.",
                    "situation": "formal"
                },
                {
                    "ko": "검사표에 불합격 항목 있으면 바로 얘기해.",
                    "vi": "Có mục nào không đạt trong phiếu kiểm tra thì nói ngay.",
                    "situation": "onsite"
                },
                {
                    "ko": "안전 검사표 감독님 확인 받았어요?",
                    "vi": "Phiếu kiểm tra an toàn đã có xác nhận của giám sát chưa?",
                    "situation": "formal"
                }
            ],
            "relatedTerms": ["phieu-yeu-cau", "nhat-ky-cong-trinh", "so-theo-doi"]
        },
        {
            "slug": "so-theo-doi",
            "korean": "추적대장",
            "vietnamese": "sổ theo dõi",
            "hanja": "追跡臺帳",
            "hanjaReading": "追(쫓을 추) 跡(자취 적) 臺(대 대) 帳(장부 장)",
            "pronunciation": "쏘 테오 조이",
            "meaningKo": "특정 항목의 이력을 지속적으로 기록하는 관리 대장. 통역 시 '추적(theo dõi)'은 단순 모니터링이 아닌 시작부터 종료까지 전 과정 기록 관리를 의미함. 베트남에서는 'sổ' (장부) 개념이 강해 자재, 장비, 안전사고 등 항목별로 별도 대장 작성. 감사/감리 점검 시 필수 제출 자료.",
            "meaningVi": "Sổ sách ghi chép liên tục về một hạng mục cụ thể như vật tư, thiết bị, sự cố, từ lúc bắt đầu đến kết thúc. Dùng để quản lý và truy xuất nguồn gốc khi cần. Phải cập nhật đầy đủ, chính xác và lưu giữ theo quy định.",
            "context": "자재, 장비, 안전 등 항목별 이력 관리",
            "culturalNote": "한국: 추적대장은 주로 중요 자재 위주 관리. 베트남: 'sổ' 문화 발달로 거의 모든 항목을 대장 관리. 한국은 전산화 추세지만, 베트남은 수기 장부와 전산 병행. 분실 시 과태료 부과 가능.",
            "commonMistakes": [
                {
                    "mistake": "danh sách theo dõi (추적 목록)",
                    "correction": "sổ theo dõi (추적대장)",
                    "explanation": "목록이 아닌 이력 기록 장부"
                },
                {
                    "mistake": "bảng quản lý (관리표)",
                    "correction": "sổ theo dõi (추적대장)",
                    "explanation": "'bảng'은 표, 'sổ'는 장부 형식"
                },
                {
                    "mistake": "lịch sử ghi chép (기록 이력)",
                    "correction": "sổ theo dõi (추적대장)",
                    "explanation": "공식 용어는 'sổ theo dõi'"
                }
            ],
            "examples": [
                {
                    "ko": "철근 입고 시 추적대장에 기록하세요.",
                    "vi": "Khi nhập thép thì ghi vào sổ theo dõi.",
                    "situation": "formal"
                },
                {
                    "ko": "장비 추적대장 어디 갔어? 감리가 보자는데.",
                    "vi": "Sổ theo dõi thiết bị đâu rồi? Giám sát muốn xem.",
                    "situation": "onsite"
                },
                {
                    "ko": "안전사고 추적대장은 5년간 보관해야 합니다.",
                    "vi": "Sổ theo dõi tai nạn lao động phải lưu giữ 5 năm.",
                    "situation": "formal"
                }
            ],
            "relatedTerms": ["nhat-ky-cong-trinh", "phieu-yeu-cau", "bao-cao-tien-do"]
        },
        {
            "slug": "giay-de-nghi",
            "korean": "요청서",
            "vietnamese": "giấy đề nghị",
            "hanja": "要請書",
            "hanjaReading": "要(구할 요) 請(청할 청) 書(글 서)",
            "pronunciation": "재이 데 응이",
            "meaningKo": "특정 사항에 대한 공식 건의 또는 제안 문서. 통역 시 '건의(đề nghị)'는 단순 요청(yêu cầu)보다 상위 개념으로, 의사결정권자에게 제안하는 공식 문서임을 강조. 베트남에서는 변경, 추가, 개선 등 제안 시 주로 사용. 검토 결과 회신 필수.",
            "meaningVi": "Văn bản chính thức để đề xuất, kiến nghị về thay đổi thiết kế, bổ sung hạng mục, điều chỉnh tiến độ hoặc các vấn đề khác cần phê duyệt từ cấp trên. Phải nêu rõ lý do, phương án và lợi ích mong đợi.",
            "context": "설계 변경, 공정 조정 등 제안 시 작성",
            "culturalNote": "한국: 요청서와 건의서를 혼용. 베트남: 'đề nghị' (제안)와 'yêu cầu' (요구) 명확히 구분. 한국은 구두 협의 후 서면화도 가능하지만, 베트남은 사전 서면 제출 원칙. 미회신 시 독촉 공문 발송 가능.",
            "commonMistakes": [
                {
                    "mistake": "phiếu yêu cầu (의뢰서)",
                    "correction": "giấy đề nghị (요청서)",
                    "explanation": "'yêu cầu'는 필요 요청, 'đề nghị'는 개선 제안"
                },
                {
                    "mistake": "đơn xin (신청서)",
                    "correction": "giấy đề nghị (요청서)",
                    "explanation": "'xin'은 허가 신청, 'đề nghị'는 건의/제안"
                },
                {
                    "mistake": "văn bản kiến nghị (건의 공문)",
                    "correction": "giấy đề nghị (요청서)",
                    "explanation": "공식 공문보다 간소한 건의서"
                }
            ],
            "examples": [
                {
                    "ko": "설계 변경 요청서 작성해서 제출하세요.",
                    "vi": "Viết giấy đề nghị thay đổi thiết kế và nộp lên.",
                    "situation": "formal"
                },
                {
                    "ko": "요청서 냈는데 답변이 없네. 다시 물어봐.",
                    "vi": "Đã nộp giấy đề nghị mà không thấy trả lời. Hỏi lại đi.",
                    "situation": "onsite"
                },
                {
                    "ko": "공정 연장 요청서에 사유를 상세히 기재해 주세요.",
                    "vi": "Trong giấy đề nghị gia hạn tiến độ, ghi rõ lý do chi tiết.",
                    "situation": "formal"
                }
            ],
            "relatedTerms": ["phieu-yeu-cau", "bien-ban-hop", "bao-cao-tien-do"]
        },
        {
            "slug": "bao-cao-su-co",
            "korean": "사고보고서",
            "vietnamese": "báo cáo sự cố",
            "hanja": "事故報告書",
            "hanjaReading": "事(일 사) 故(연고 고) 報(알릴 보) 告(고할 고) 書(글 서)",
            "pronunciation": "바오 까오 쓰 꼬",
            "meaningKo": "안전사고, 품질 결함 등 비정상 사건 발생 시 작성하는 보고서. 통역 시 '사고(sự cố)'는 안전사고(tai nạn)와 구분하여 '돌발 상황, 이슈'를 포괄하는 개념임을 명확히 해야 함. 베트남에서는 즉시 보고(báo cáo khẩn) 후 상세 보고서 제출이 원칙. 원인, 조치, 재발 방지 대책 필수 포함.",
            "meaningVi": "Báo cáo chi tiết về sự cố xảy ra tại công trường như tai nạn lao động, sự cố kỹ thuật, hỏa hoạn. Phải ghi rõ thời gian, địa điểm, nguyên nhân, thiệt hại, biện pháp xử lý và phòng ngừa. Báo cáo ngay sau khi xảy ra sự cố.",
            "context": "사고 발생 즉시 작성 및 보고",
            "culturalNote": "한국: 중대재해 시 고용노동부 즉시 보고 의무. 베트남: 사망 사고 시 경찰, 노동청 동시 신고 필수. 양국 모두 사고 은폐 시 처벌 강화 추세. 한국은 원청 책임 강화, 베트남은 현장 책임자 형사 처벌 가능.",
            "commonMistakes": [
                {
                    "mistake": "báo cáo tai nạn (재해 보고서)",
                    "correction": "báo cáo sự cố (사고보고서)",
                    "explanation": "'tai nạn'은 인명 피해, 'sự cố'는 모든 비정상 상황 포함"
                },
                {
                    "mistake": "báo cáo tình huống (상황 보고서)",
                    "correction": "báo cáo sự cố (사고보고서)",
                    "explanation": "일반 상황이 아닌 사고 전용 보고서"
                },
                {
                    "mistake": "biên bản sự việc (사건 조서)",
                    "correction": "báo cáo sự cố (사고보고서)",
                    "explanation": "'biên bản'은 조사 기록, 'báo cáo'는 보고서"
                }
            ],
            "examples": [
                {
                    "ko": "추락 사고 발생했으니 즉시 사고보고서 작성하세요.",
                    "vi": "Xảy ra tai nạn rơi từ trên cao, lập báo cáo sự cố ngay.",
                    "situation": "formal"
                },
                {
                    "ko": "사고보고서 2시간 내로 본사에 보고해야 해.",
                    "vi": "Báo cáo sự cố phải gửi về công ty trong vòng 2 giờ.",
                    "situation": "onsite"
                },
                {
                    "ko": "재발 방지 대책 없는 사고보고서는 반려됩니다.",
                    "vi": "Báo cáo sự cố không có biện pháp phòng ngừa sẽ bị trả lại.",
                    "situation": "formal"
                }
            ],
            "relatedTerms": ["nhat-ky-cong-trinh", "so-theo-doi", "phieu-kiem-tra"]
        }
    ]

    # 5. 중복 제거 (CRITICAL RULE #5)
    filtered_terms = [term for term in new_terms if term['slug'] not in existing_slugs]

    if not filtered_terms:
        print("⚠️  모든 용어가 이미 존재합니다. 추가할 용어 없음.")
        return

    # 6. 데이터 추가 (CRITICAL RULE #3: None, not null)
    data.extend(filtered_terms)

    # 7. 파일 저장
    with open(file_path, 'w', encoding='utf-8') as f:
        json.dump(data, f, ensure_ascii=False, indent=2)

    print(f"✅ {len(filtered_terms)}개 건설문서양식 용어 추가 완료!")
    print(f"📊 총 용어 수: {len(data)}개")
    for term in filtered_terms:
        print(f"   - {term['slug']}: {term['korean']} ({term['vietnamese']})")

if __name__ == "__main__":
    main()
