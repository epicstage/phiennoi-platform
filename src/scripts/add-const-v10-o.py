#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import json
import os

# CRITICAL: Correct file path using relative path from script location
file_path = os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', 'data', 'terms', 'construction.json')

# Load existing data (LIST, not dict!)
with open(file_path, 'r', encoding='utf-8') as f:
    data = json.load(f)

# Get existing slugs to prevent duplicates
existing_slugs = {t['slug'] for t in data}

# New terms - Construction Logistics/Material Management theme
new_terms = [
    {
        "slug": "kho-bai",
        "korean": "야적장",
        "vietnamese": "kho bãi",
        "hanja": "野積場",
        "hanjaReading": "野(들 야) + 積(쌓을 적) + 場(마당 장)",
        "pronunciation": "꺼 바이",
        "meaningKo": "건설 자재를 야외에 쌓아두는 임시 보관 장소입니다. 통역 시 주의할 점은 베트남 현장에서는 'kho bãi'와 'kho mở'(개방형 창고)를 혼용하는 경우가 많으나, kho bãi는 지붕이 없는 완전 야외 공간을 의미하고 kho mở는 지붕은 있으되 벽이 없는 반개방형을 뜻하므로 구분해야 합니다. 특히 철근, 파이프 등 우천에 영향을 덜 받는 자재는 kho bãi에, 시멘트나 석고보드 등은 kho mở에 보관하는 것이 일반적이므로 자재 특성에 따라 정확히 번역해야 합니다.",
        "meaningVi": "Khu vực lưu trữ vật liệu xây dựng ngoài trời, không có mái che. Thường dùng để chứa các vật liệu như sắt thép, ống nước, gạch block có khả năng chống chịu thời tiết. Cần phân biệt với 'kho mở' (kho có mái nhưng không tường) để bảo quản đúng loại vật liệu theo đặc tính.",
        "context": "자재 관리, 현장 배치, 보관 계획",
        "culturalNote": "한국 건설 현장에서는 야적장을 체계적으로 구획하여 자재별로 정리하는 경향이 강하지만, 베트남 중소형 현장에서는 공간 부족으로 인해 야적장 관리가 덜 체계적인 경우가 많습니다. 또한 베트남은 우기와 건기가 뚜렷하여 우기 전 kho bãi의 자재를 kho có mái(지붕 있는 창고)로 이동시키는 계절적 관리가 필요하며, 이를 간과하면 자재 손실이 클 수 있습니다. 통역사는 이러한 기후적 차이를 인지하고 자재 보관 방식에 대한 추가 설명을 제공해야 합니다.",
        "commonMistakes": [
            {
                "mistake": "kho bãi를 '창고'로 번역",
                "correction": "'야적장' 또는 '야외 보관소'로 번역",
                "explanation": "kho(창고)와 bãi(마당, 터)의 합성어로 지붕 없는 야외 공간을 의미하므로 실내 창고와 혼동하지 말아야 함"
            },
            {
                "mistake": "kho bãi와 kho mở를 동일하게 번역",
                "correction": "kho bãi는 '야적장', kho mở는 '개방형 창고'로 구분",
                "explanation": "전자는 완전 야외, 후자는 지붕은 있으나 벽이 없는 구조로 보관 가능한 자재 종류가 다름"
            },
            {
                "mistake": "'bãi tập kết'과 혼용",
                "correction": "kho bãi는 '보관용', bãi tập kết은 '임시 집하용'",
                "explanation": "kho bãi는 중장기 보관, bãi tập kết은 하역 후 즉시 분류·이동하는 임시 공간으로 목적이 다름"
            },
            {
                "mistake": "우기 대비 조치를 언급하지 않음",
                "correction": "베트남 현장에서는 'chuẩn bị mùa mưa'(우기 준비) 맥락 추가",
                "explanation": "열대 기후 특성상 우기 전 자재 이동 계획이 필수이므로 통역 시 이를 강조해야 함"
            }
        ],
        "examples": [
            {
                "ko": "철근은 야적장에 보관하고, 시멘트는 창고에 넣어두세요.",
                "vi": "Thép cốt thép để ở kho bãi, còn xi măng phải cất vào kho có mái.",
                "situation": "onsite"
            },
            {
                "ko": "우기가 오기 전에 야적장 자재를 점검하고 필요시 이동 조치 바랍니다.",
                "vi": "Trước mùa mưa, kiểm tra vật liệu ở kho bãi và di chuyển vào kho có mái nếu cần.",
                "situation": "formal"
            },
            {
                "ko": "야적장 면적이 부족해서 자재 반입 일정을 조정해야 할 것 같아요.",
                "vi": "Diện tích kho bãi không đủ nên có lẽ phải điều chỉnh lịch nhập vật liệu.",
                "situation": "informal"
            }
        ],
        "relatedTerms": ["kho-mo", "bai-tap-ket", "quan-ly-ton-kho", "van-chuyen-noi-bo"]
    },
    {
        "slug": "nhap-kho",
        "korean": "입고",
        "vietnamese": "nhập kho",
        "hanja": "入庫",
        "hanjaReading": "入(들 입) + 庫(곳간 고)",
        "pronunciation": "녑 커",
        "meaningKo": "자재나 장비를 창고 또는 야적장에 받아들이는 작업입니다. 통역 시 베트남에서는 'nhập kho'와 'nhận hàng'(물품 수령)을 구분해야 하는데, nhập kho는 시스템에 정식 등록하고 재고로 반영하는 행위를 의미하며, nhận hàng은 단순히 물리적으로 받는 것을 뜻합니다. 특히 ERP 시스템을 사용하는 한국 기업 현장에서는 '입고 처리'가 시스템 입력까지 포함하므로, 베트남 현장 담당자에게 'nhập vào hệ thống'(시스템 입력)까지 해야 한다고 명확히 전달해야 합니다.",
        "meaningVi": "Thao tác tiếp nhận vật liệu hoặc thiết bị vào kho và ghi nhận vào hệ thống quản lý tồn kho. Khác với 'nhận hàng' chỉ là việc tiếp nhận vật lý, 'nhập kho' yêu cầu cập nhật chính thức vào sổ sách hoặc phần mềm quản lý để theo dõi số lượng, chất lượng và vị trí lưu trữ.",
        "context": "물류 관리, 자재 수불, ERP 운영",
        "culturalNote": "한국 현장에서는 입고 시 바코드 스캔이나 RFID 태그 등 자동화 시스템을 많이 사용하지만, 베트남 중소형 현장에서는 여전히 수기 장부나 엑셀로 관리하는 경우가 많습니다. 따라서 한국 본사가 요구하는 'nhập kho tự động'(자동 입고)과 베트남 현장의 'nhập kho thủ công'(수동 입고) 간 격차가 발생할 수 있으며, 통역사는 이를 인지하고 시스템 교육이나 업그레이드 필요성을 중재할 수 있어야 합니다. 또한 베트남에서는 검수(kiểm nhận) 없이 입고하는 관행이 있어 품질 문제 발생 시 책임 소재가 불분명해지므로, 한국식 '검수 후 입고' 원칙을 강조해야 합니다.",
        "commonMistakes": [
            {
                "mistake": "nhập kho와 nhận hàng을 동일하게 번역",
                "correction": "nhập kho는 '입고(시스템 등록)', nhận hàng은 '수령(물리적 접수)'",
                "explanation": "전자는 재고 관리 시스템 반영을 포함하고, 후자는 단순 물품 인수를 의미함"
            },
            {
                "mistake": "'입고증'을 'giấy nhận hàng'으로 번역",
                "correction": "'phiếu nhập kho' 또는 'biên bản nhập kho'",
                "explanation": "공식 입고 문서는 phiếu nhập kho이며, 이는 법적 증빙 효력이 있음"
            },
            {
                "mistake": "검수 절차를 생략하고 입고만 언급",
                "correction": "'kiểm nhận rồi mới nhập kho'(검수 후 입고)로 명시",
                "explanation": "베트남 현장에서 검수 없이 입고하는 관행이 있어 한국식 절차를 명확히 전달해야 함"
            },
            {
                "mistake": "입고 시점을 'khi nhận hàng'(수령 시)로 표현",
                "correction": "'khi hoàn tất kiểm tra và ghi nhận vào hệ thống'(검사 완료 및 시스템 등록 시)",
                "explanation": "입고는 물리적 수령이 아니라 공식 등록 시점을 기준으로 해야 정확함"
            }
        ],
        "examples": [
            {
                "ko": "오늘 오후 3시에 철근 입고 예정이니 검수 담당자 대기 바랍니다.",
                "vi": "Dự kiến nhập kho thép lúc 3 giờ chiều nay, nhờ người phụ trách kiểm nhận sẵn sàng.",
                "situation": "formal"
            },
            {
                "ko": "입고 시 수량과 규격을 꼼꼼히 확인한 후 시스템에 입력해 주세요.",
                "vi": "Khi nhập kho, kiểm tra kỹ số lượng và quy cách rồi mới nhập vào hệ thống.",
                "situation": "onsite"
            },
            {
                "ko": "입고증에 서명하고 한 부는 회계팀에 전달하세요.",
                "vi": "Ký vào phiếu nhập kho và chuyển một bản cho bộ phận kế toán.",
                "situation": "formal"
            }
        ],
        "relatedTerms": ["xuat-kho", "kiem-ke", "boc-xep", "quan-ly-ton-kho"]
    },
    {
        "slug": "xuat-kho",
        "korean": "출고",
        "vietnamese": "xuất kho",
        "hanja": "出庫",
        "hanjaReading": "出(날 출) + 庫(곳간 고)",
        "pronunciation": "쑤엇 커",
        "meaningKo": "창고나 야적장에서 자재나 장비를 꺼내어 현장에 투입하거나 외부로 반출하는 작업입니다. 통역 시 주의할 점은 베트남에서 'xuất kho'는 공식적인 출고 절차(문서 작성, 시스템 반영)를 의미하고, 'lấy hàng'는 단순히 물건을 가져가는 행위를 뜻하므로 구분해야 합니다. 특히 한국 현장에서는 출고 시 출고 요청서(yêu cầu xuất kho)를 승인받고 출고증(phiếu xuất kho)을 발행하는 절차가 필수인데, 베트남 소규모 현장에서는 이를 생략하는 경우가 많아 재고 불일치 문제가 발생할 수 있으므로 절차 준수를 강조해야 합니다.",
        "meaningVi": "Thao tác lấy vật liệu hoặc thiết bị ra khỏi kho để sử dụng tại công trường hoặc chuyển giao cho bên ngoài, đồng thời ghi giảm trong hệ thống quản lý tồn kho. Cần có phiếu xuất kho chính thức và được phê duyệt để đảm bảo minh bạch và tránh thất thoát.",
        "context": "자재 불출, 재고 관리, 현장 투입",
        "culturalNote": "한국 건설 현장에서는 출고 시 '누가, 언제, 무엇을, 얼마나, 어디에 사용할 것인지'를 명확히 기록하는 문화가 강하지만, 베트nam 현장에서는 급하면 구두 요청으로 출고하고 사후에 기록하는 경우가 많습니다. 이로 인해 재고 수불부와 실제 재고가 불일치하는 문제가 빈번하므로, 통역사는 한국식 사전 승인 시스템의 중요성을 설명하고 베트남 담당자가 이를 습관화할 수 있도록 도와야 합니다. 또한 베트남에서는 'xuất kho tạm'(임시 출고) 개념이 있어 나중에 반납할 수 있는데, 한국에서는 이를 '대여'로 구분하므로 혼동하지 않도록 주의해야 합니다.",
        "commonMistakes": [
            {
                "mistake": "xuất kho와 lấy hàng을 동일하게 번역",
                "correction": "xuất kho는 '출고(공식 절차)', lấy hàng은 '물품 인출(비공식)'",
                "explanation": "전자는 문서와 시스템 반영을 포함하고, 후자는 단순 물리적 행위만을 의미함"
            },
            {
                "mistake": "'출고 요청'을 'yêu cầu lấy hàng'로 번역",
                "correction": "'yêu cầu xuất kho' 또는 'đơn xin xuất kho'",
                "explanation": "공식 출고 요청서는 phiếu yêu cầu xuất kho로 표현해야 정확함"
            },
            {
                "mistake": "출고증 없이 출고 가능하다고 안내",
                "correction": "'phải có phiếu xuất kho được duyệt'(승인된 출고증 필수)로 명시",
                "explanation": "베트남 현장에서 구두 요청으로 출고하는 관행이 있으나 한국 시스템에서는 문서 필수"
            },
            {
                "mistake": "xuất kho tạm을 '임시 출고'로만 번역",
                "correction": "'대여' 또는 '일시 불출(반납 예정)'로 구체화",
                "explanation": "한국에서는 반납 전제 출고를 '대여'로 구분하므로 오해 방지 필요"
            }
        ],
        "examples": [
            {
                "ko": "2층 타설 작업을 위해 시멘트 50포대 출고 요청합니다.",
                "vi": "Yêu cầu xuất kho 50 bao xi măng để đổ bê tông tầng 2.",
                "situation": "formal"
            },
            {
                "ko": "출고 시 반드시 출고증을 작성하고 창고 담당자 서명을 받으세요.",
                "vi": "Khi xuất kho, nhất định phải lập phiếu xuất kho và lấy chữ ký người quản lý kho.",
                "situation": "onsite"
            },
            {
                "ko": "이 장비는 내일 반납 예정이니 임시 출고로 처리해 주세요.",
                "vi": "Thiết bị này sẽ trả lại ngày mai nên xử lý là xuất kho tạm thời.",
                "situation": "informal"
            }
        ],
        "relatedTerms": ["nhap-kho", "kiem-ke", "quan-ly-ton-kho", "van-chuyen-noi-bo"]
    },
    {
        "slug": "kiem-ke",
        "korean": "재고조사",
        "vietnamese": "kiểm kê",
        "hanja": "檢檢",
        "hanjaReading": "檢(검사할 검) + 檢(검사할 검)",
        "pronunciation": "끼엠 께",
        "meaningKo": "창고나 현장에 보관된 자재와 장비의 실제 수량을 확인하고 장부상 재고와 대조하는 작업입니다. 통역 시 주의할 점은 베트남에서 'kiểm kê'는 단순 수량 확인을 넘어 품질 상태까지 점검하는 개념을 포함하며, 특히 'kiểm kê định kỳ'(정기 재고조사)와 'kiểm kê đột xuất'(수시 재고조사)을 구분해야 합니다. 한국 현장에서는 월말이나 분기말에 정기 재고조사를 하는 것이 일반적이지만, 베트남에서는 고가 자재나 분실 위험이 높은 품목에 대해 수시 조사를 더 자주 실시하는 경향이 있으므로 이를 고려해 일정을 조율해야 합니다.",
        "meaningVi": "Công tác kiểm tra, đếm số lượng thực tế vật tư, thiết bị hiện có tại kho hoặc công trường và đối chiếu với sổ sách quản lý. Bao gồm cả việc đánh giá tình trạng chất lượng, phát hiện hư hỏng hoặc thất thoát để điều chỉnh số liệu cho chính xác.",
        "context": "재고 관리, 회계 감사, 자산 관리",
        "culturalNote": "한국 건설 현장에서는 재고조사를 회계팀 주도로 체계적으로 진행하며 결과를 ERP에 즉시 반영하지만, 베트남 중소형 현장에서는 현장소장이나 자재 담당자가 간이 조사를 하고 엑셀로 관리하는 경우가 많아 정확도가 떨어질 수 있습니다. 또한 베트남에서는 재고조사 시 'hàng tồn kho chết'(사장 재고, 장기 미사용 자재)를 별도 분류하여 처분 계획을 수립하는 것이 관례인데, 한국에서는 이를 간과하는 경우가 있으므로 통역사는 이러한 현지 관행을 본사에 전달하여 재고 효율화를 도울 수 있습니다.",
        "commonMistakes": [
            {
                "mistake": "kiểm kê를 단순 '재고 확인'으로 번역",
                "correction": "'재고조사' 또는 '실사'로 번역하여 공식적 절차임을 명시",
                "explanation": "kiểm kê는 공식 문서 작성과 시스템 반영을 포함하는 감사 수준의 작업임"
            },
            {
                "mistake": "kiểm kê định kỳ와 kiểm kê đột xuất을 구분 없이 '재고조사'로만 번역",
                "correction": "전자는 '정기 재고조사', 후자는 '수시 재고조사' 또는 '긴급 실사'",
                "explanation": "목적과 절차가 다르므로 구분하여 번역해야 현장에서 혼선 방지"
            },
            {
                "mistake": "'hàng tồn kho chết'을 그냥 '재고'로 번역",
                "correction": "'사장 재고' 또는 '장기 미사용 재고'로 구체화",
                "explanation": "처분 대상이 되는 특수 재고이므로 별도 표현 필요"
            },
            {
                "mistake": "재고조사 결과를 '대충 맞다'는 식으로 모호하게 전달",
                "correction": "'chênh lệch X%'(오차율 X%) 또는 'khớp 100%'(100% 일치)로 수치화",
                "explanation": "재고조사는 회계 감사 근거이므로 정확한 수치 전달이 필수"
            }
        ],
        "examples": [
            {
                "ko": "월말 재고조사 일정이 25일인데, 자재 담당자들에게 미리 공지해 주세요.",
                "vi": "Lịch kiểm kê cuối tháng là ngày 25, nhờ thông báo trước cho các người phụ trách vật tư.",
                "situation": "formal"
            },
            {
                "ko": "이번 재고조사에서 시멘트 20포대 부족한 것으로 확인됐어요.",
                "vi": "Lần kiểm kê này phát hiện thiếu 20 bao xi măng.",
                "situation": "onsite"
            },
            {
                "ko": "사장 재고는 별도 목록으로 작성해서 처분 방안을 검토하겠습니다.",
                "vi": "Hàng tồn kho chết sẽ lập danh sách riêng để xem xét phương án xử lý.",
                "situation": "formal"
            }
        ],
        "relatedTerms": ["nhap-kho", "xuat-kho", "quan-ly-ton-kho", "kho-bai"]
    },
    {
        "slug": "van-chuyen-noi-bo",
        "korean": "현장내운반",
        "vietnamese": "vận chuyển nội bộ",
        "hanja": "現場內運搬",
        "hanjaReading": "現(나타날 현) + 場(마당 장) + 內(안 내) + 運(옮길 운) + 搬(옮길 반)",
        "pronunciation": "번 추엔 노이 보",
        "meaningKo": "건설 현장 내에서 자재나 장비를 한 장소에서 다른 장소로 이동시키는 작업입니다. 통역 시 주의할 점은 베트남에서 'vận chuyển'은 일반적으로 장거리 운송을 의미하고, 현장 내 단거리 이동은 'di chuyển'이라고도 표현하는데, 한국에서는 이를 명확히 '현장내운반'으로 구분하므로 'vận chuyển nội bộ' 또는 'vận chuyển trong công trường'으로 번역해야 합니다. 특히 타워크레인이나 지게차를 이용한 수직·수평 운반을 구분해야 하며, 베트남 현장에서는 인력 운반(vận chuyển thủ công)의 비중이 높아 안전사고 위험이 크므로 기계화 운반 방식을 적극 제안해야 합니다.",
        "meaningVi": "Công việc di chuyển vật liệu hoặc thiết bị từ vị trí này sang vị trí khác trong phạm vi công trường xây dựng. Bao gồm vận chuyển theo chiều ngang (bằng xe nâng, xe công trình) và theo chiều dọc (bằng cẩu tháp, thang máy vật liệu). Cần phân biệt với 'vận chuyển từ bên ngoài' để quản lý chi phí và trách nhiệm rõ ràng.",
        "context": "공정 관리, 자재 투입, 장비 운용",
        "culturalNote": "한국 대형 현장에서는 타워크레인과 컨베이어 시스템으로 현장내운반을 자동화하는 것이 일반적이지만, 베트남 중소형 현장에서는 인력과 소형 지게차에 의존하는 경우가 많아 효율성과 안전성이 떨어집니다. 또한 베트남에서는 'cửu vạn'(지게차 기사) 비용이 저렴하여 인력 운반을 선호하는 경향이 있으나, 한국 안전 기준에서는 2인 이상 협동 운반 시 중량 제한(50kg)과 안전 교육이 필수이므로 이를 강조해야 합니다. 통역사는 기계화 운반의 장기적 비용 절감 효과를 설명하여 베트남 현장의 운반 방식 개선을 유도할 수 있어야 합니다.",
        "commonMistakes": [
            {
                "mistake": "'현장내운반'을 단순 'vận chuyển'로 번역",
                "correction": "'vận chuyển nội bộ' 또는 'vận chuyển trong công trường'",
                "explanation": "vận chuyển만 쓰면 외부 운송으로 오해할 수 있으므로 '내부(nội bộ)' 명시 필요"
            },
            {
                "mistake": "수직 운반과 수평 운반을 구분하지 않음",
                "correction": "'vận chuyển theo chiều ngang'(수평), 'vận chuyển theo chiều dọc'(수직)로 구분",
                "explanation": "사용 장비와 안전 조치가 다르므로 명확히 구분해야 함"
            },
            {
                "mistake": "'인력 운반'을 'vận chuyển bằng người'로 직역",
                "correction": "'vận chuyển thủ công' 또는 'bốc vác bằng sức người'",
                "explanation": "베트남 현장 용어에 맞춰 자연스럽게 표현해야 함"
            },
            {
                "mistake": "운반 거리를 명시하지 않음",
                "correction": "'거리 X미터'를 'khoảng cách X mét'로 구체화",
                "explanation": "운반비 산정과 장비 선택에 거리가 중요하므로 명시 필요"
            }
        ],
        "examples": [
            {
                "ko": "1층에서 3층까지 블록 운반은 타워크레인을 이용하고, 같은 층 내 이동은 지게차를 쓰세요.",
                "vi": "Vận chuyển gạch block từ tầng 1 lên tầng 3 dùng cẩu tháp, di chuyển trong cùng tầng dùng xe nâng.",
                "situation": "onsite"
            },
            {
                "ko": "현장내운반 중 안전사고가 많이 발생하니 작업자 안전 교육을 강화해 주세요.",
                "vi": "Tai nạn lao động trong quá trình vận chuyển nội bộ xảy ra nhiều, nhờ tăng cường đào tạo an toàn cho công nhân.",
                "situation": "formal"
            },
            {
                "ko": "50kg 넘는 자재는 혼자 들지 말고 꼭 두 명이 함께 운반하세요.",
                "vi": "Vật liệu trên 50kg đừng bốc một mình, nhất định phải hai người cùng vận chuyển.",
                "situation": "onsite"
            }
        ],
        "relatedTerms": ["boc-xep", "kho-bai", "xuat-kho", "pallet-go"]
    },
    {
        "slug": "boc-xep",
        "korean": "하역",
        "vietnamese": "bốc xếp",
        "hanja": "荷役",
        "hanjaReading": "荷(짐 하) + 役(부릴 역)",
        "pronunciation": "복 쎕",
        "meaningKo": "화물차나 컨테이너에서 자재를 내리거나(하차) 싣는(상차) 작업입니다. 통역 시 주의할 점은 베트남에서 'bốc xếp'은 '내리고 싣는' 양방향 작업을 모두 포함하는 반면, 한국에서는 '하역'(내리기), '적재'(싣기)로 구분하는 경우가 많으므로 상황에 따라 'bốc hàng'(하차), 'xếp hàng'(상차)로 나누어 번역해야 할 수 있습니다. 특히 베트남 현장에서는 인력 하역('bốc xếp thủ công')이 여전히 주류이나, 한국 안전 기준에서는 지게차나 크레인 사용을 권장하므로 'bốc xếp cơ giới hóa'(기계화 하역)를 제안해야 합니다.",
        "meaningVi": "Công việc dỡ hàng xuống từ xe tải, container hoặc xếp hàng lên phương tiện vận chuyển. Bao gồm cả thao tác thủ công (bốc vác bằng người) và cơ giới hóa (dùng xe nâng, cẩu). Đây là khâu quan trọng trong chuỗi logistics vật liệu xây dựng, cần đảm bảo an toàn và tránh hư hỏng vật tư.",
        "context": "물류 작업, 자재 반입, 현장 입하",
        "culturalNote": "한국 건설 현장에서는 하역 시 안전모, 안전화, 안전벨트 착용이 의무이며, 1톤 이상 중량물은 반드시 기계 하역을 해야 하지만, 베트남 중소형 현장에서는 이러한 규정이 느슨하게 적용되어 안전사고 위험이 높습니다. 또한 베트남에서는 'bốc vác'(인력 하역) 노동자의 임금이 저렴하여 지게차보다 인력을 선호하는 경향이 있으나, 장기적으로는 산재 보상 비용과 작업 지연으로 손해가 크므로 통역사는 기계화 하역의 경제성을 설명해야 합니다. 특히 우기에는 진흙 때문에 인력 하역이 어려우므로 계절별 하역 계획을 수립하도록 조언할 필요가 있습니다.",
        "commonMistakes": [
            {
                "mistake": "bốc xếp을 '운반'으로 번역",
                "correction": "'하역' 또는 '상하차'로 번역",
                "explanation": "운반(vận chuyển)은 이동 과정이고, 하역(bốc xếp)은 싣고 내리는 작업이므로 구분해야 함"
            },
            {
                "mistake": "bốc hàng과 xếp hàng을 구분 없이 '하역'으로 통칭",
                "correction": "bốc hàng은 '하차', xếp hàng은 '상차' 또는 '적재'",
                "explanation": "작업 방향이 반대이므로 필요 시 구분하여 번역해야 정확함"
            },
            {
                "mistake": "'인력 하역'을 권장하는 듯이 번역",
                "correction": "'인력 하역은 위험하니 기계 사용 권장'으로 안전 강조",
                "explanation": "한국 안전 기준에서는 기계화를 우선하므로 이를 명확히 전달해야 함"
            },
            {
                "mistake": "하역 시간을 명시하지 않음",
                "correction": "'하역 시작 X시, 완료 예정 Y시'로 구체화",
                "explanation": "하역은 다른 공정에 영향을 주므로 정확한 시간 전달이 중요함"
            }
        ],
        "examples": [
            {
                "ko": "오늘 오후 2시에 시멘트 하역 예정이니 지게차 준비해 주세요.",
                "vi": "Dự kiến bốc xếp xi măng lúc 2 giờ chiều nay, nhờ chuẩn bị sẵn xe nâng.",
                "situation": "onsite"
            },
            {
                "ko": "하역 시 자재 손상이 자주 발생하니 조심해서 작업하세요.",
                "vi": "Trong quá trình bốc xếp, vật liệu hay bị hư hỏng nên làm việc cẩn thận.",
                "situation": "informal"
            },
            {
                "ko": "중량물 하역은 반드시 크레인을 사용하고 인력 작업은 금지합니다.",
                "vi": "Bốc xếp hàng nặng bắt buộc phải dùng cẩu, cấm dùng sức người.",
                "situation": "formal"
            }
        ],
        "relatedTerms": ["van-chuyen-noi-bo", "nhap-kho", "kho-bai", "pallet-go"]
    },
    {
        "slug": "pallet-go",
        "korean": "목재파레트",
        "vietnamese": "pallet gỗ",
        "hanja": "木材pallet",
        "hanjaReading": "木(나무 목) + 材(재목 재) + pallet(외래어)",
        "pronunciation": "팔레 고",
        "meaningKo": "자재를 적재하고 운반하기 위해 사용하는 나무로 만든 깔판입니다. 통역 시 주의할 점은 베트남에서 'pallet gỗ'는 일회용과 다회용을 구분하지 않고 통칭하는 경우가 많은데, 한국 현장에서는 '일회용 파레트(pallet dùng một lần)'와 '회수용 파레트(pallet tái sử dụng)'를 명확히 구분하여 관리하므로 이를 구체적으로 전달해야 합니다. 특히 베트남에서는 파레트 규격이 다양하여 표준 파레트(1100x1100mm)와 비표준 파레트가 혼재하는데, 한국 물류 시스템은 표준 규격 준수가 중요하므로 '규격 확인'을 강조해야 합니다.",
        "meaningVi": "Khay gỗ dùng để xếp chồng và vận chuyển vật liệu xây dựng, giúp thuận tiện cho xe nâng hoặc xe cẩu di chuyển. Có hai loại chính: pallet sử dụng một lần (thường nhẹ, rẻ) và pallet tái sử dụng (chắc chắn, đắt hơn). Cần tuân thủ quy cách chuẩn để tương thích với thiết bị logistics.",
        "context": "자재 포장, 하역 작업, 창고 적재",
        "culturalNote": "한국 건설 현장에서는 파레트를 재사용하고 반납하는 시스템이 정착되어 있어 파레트 분실 시 벌금을 물리는 경우가 많지만, 베트남 중소형 현장에서는 파레트를 소모품으로 간주하여 사용 후 폐기하거나 다른 용도로 전용하는 관행이 있습니다. 이로 인해 한국 본사가 요구하는 파레트 회수율(tỷ lệ thu hồi pallet)을 맞추지 못하는 경우가 발생하므로, 통역사는 파레트 관리 시스템의 중요성을 설명하고 반납 절차를 명확히 전달해야 합니다. 또한 베트남에서는 열처리(xử lý nhiệt) 파레트가 아닌 일반 파레트를 수출입에 사용하여 검역 문제가 생기는 경우가 있으므로 국제 기준(ISPM 15) 준수를 주지시켜야 합니다.",
        "commonMistakes": [
            {
                "mistake": "'파레트'를 'khay gỗ' 또는 'giá đỡ'로만 번역",
                "correction": "'pallet gỗ'로 외래어 그대로 사용",
                "explanation": "베트남 현장에서 'pallet'이 표준 용어로 정착되어 있어 의역보다 외래어가 더 명확함"
            },
            {
                "mistake": "일회용과 재사용 파레트를 구분하지 않음",
                "correction": "'pallet dùng một lần'과 'pallet tái sử dụng'로 명시",
                "explanation": "관리 방식과 비용이 다르므로 구분 필수"
            },
            {
                "mistake": "파레트 규격을 언급하지 않음",
                "correction": "'pallet chuẩn 1100x1100mm' 등 규격 명시",
                "explanation": "비표준 파레트는 물류 효율성을 떨어뜨리므로 규격 확인이 중요함"
            },
            {
                "mistake": "열처리 파레트(ISPM 15) 기준을 설명하지 않음",
                "correction": "'pallet xử lý nhiệt theo ISPM 15'로 국제 기준 강조",
                "explanation": "수출입 시 검역 문제 방지를 위해 필수 정보"
            }
        ],
        "examples": [
            {
                "ko": "시멘트는 파레트에 20포대씩 쌓아서 보관하고, 파레트는 사용 후 반납하세요.",
                "vi": "Xi măng xếp 20 bao trên mỗi pallet để bảo quản, sau khi dùng phải trả lại pallet.",
                "situation": "onsite"
            },
            {
                "ko": "이번 주 파레트 회수율이 70%밖에 안 되는데, 분실된 파레트를 찾아주세요.",
                "vi": "Tuần này tỷ lệ thu hồi pallet chỉ đạt 70%, nhờ tìm lại các pallet bị thất lạc.",
                "situation": "formal"
            },
            {
                "ko": "수출용 자재는 반드시 열처리 파레트에 적재해야 검역 통과가 가능합니다.",
                "vi": "Vật liệu xuất khẩu bắt buộc phải xếp trên pallet xử lý nhiệt mới qua được kiểm dịch.",
                "situation": "formal"
            }
        ],
        "relatedTerms": ["boc-xep", "van-chuyen-noi-bo", "kho-bai", "nhap-kho"]
    },
    {
        "slug": "container-van-phong",
        "korean": "컨테이너사무실",
        "vietnamese": "container văn phòng",
        "hanja": "container事務室",
        "hanjaReading": "container(외래어) + 事(일 사) + 務(힘쓸 무) + 室(집 실)",
        "pronunciation": "껀테이너 번 퐁",
        "meaningKo": "건설 현장에 임시로 설치하는 컨테이너 형태의 사무 공간입니다. 통역 시 주의할 점은 베트남에서 'container văn phòng'은 단순 사무실뿐 아니라 회의실, 휴게실, 숙소 등 다양한 용도를 포함하는 개념인데, 한국에서는 용도별로 '사무용 컨테이너', '숙소용 컨테이너', '회의실 컨테이너'로 세분화하여 부르므로 혼동하지 않도록 주의해야 합니다. 특히 베트남 현장에서는 중고 컨테이너(container cũ)를 많이 사용하는 반면, 한국에서는 신품 또는 리모델링한 컨테이너를 선호하므로 품질 기준을 명확히 전달해야 합니다.",
        "meaningVi": "Không gian làm việc tạm thời hình dạng container, được lắp đặt tại công trường xây dựng. Thường có điều hòa, điện, bàn ghế và có thể di chuyển khi cần. Ngoài làm văn phòng, còn dùng làm phòng họp, phòng nghỉ hoặc nhà ở cho công nhân. Phân loại theo mục đích sử dụng và mức độ trang bị.",
        "context": "현장 시설, 가설 건축물, 사무 환경",
        "culturalNote": "한국 대형 현장에서는 컨테이너사무실을 다층으로 적층하여 본사 수준의 사무 환경을 구축하는 경우가 많지만, 베트남 중소형 현장에서는 단층 컨테이너 1~2개로 간소하게 운영하는 경향이 있습니다. 또한 베트남 열대 기후에서는 컨테이너 내부 온도가 40도 이상 올라가므로 에어컨(điều hòa) 설치가 필수인데, 한국 현장 관리자는 이를 간과하여 작업 환경 불만이 발생할 수 있습니다. 통역사는 현지 기후 특성을 고려한 냉방 시설과 단열재(vật liệu cách nhiệt) 추가 설치를 제안해야 합니다. 또한 베트남에서는 컨테이너 임대(thuê container) 시장이 발달해 있어 구매보다 임대가 경제적일 수 있으므로 비용 비교 정보를 제공하는 것이 좋습니다.",
        "commonMistakes": [
            {
                "mistake": "'컨테이너사무실'을 'phòng làm việc container'로 번역",
                "correction": "'container văn phòng'으로 합성어 형태 유지",
                "explanation": "베트남 현장에서 'container văn phòng'이 고유명사처럼 굳어진 표현임"
            },
            {
                "mistake": "용도별 구분 없이 모두 'container văn phòng'으로 통칭",
                "correction": "'container làm văn phòng'(사무), 'container nhà ở'(숙소), 'container họp'(회의) 등으로 구분",
                "explanation": "용도에 따라 내부 시설과 안전 기준이 다르므로 명확히 구분 필요"
            },
            {
                "mistake": "중고 컨테이너 사용을 기본으로 안내",
                "correction": "'container mới' 또는 'container tân trang'(리모델링) 옵션 제시",
                "explanation": "한국 본사 기준에서는 일정 품질 이상의 컨테이너를 요구할 수 있음"
            },
            {
                "mistake": "냉방 시설 필요성을 언급하지 않음",
                "correction": "'cần lắp điều hòa do khí hậu nóng'(더운 기후로 에어컨 필수) 명시",
                "explanation": "베트남 열대 기후에서 냉방 없이는 사무 환경으로 부적합함"
            }
        ],
        "examples": [
            {
                "ko": "내일 컨테이너사무실 2동이 반입되니 설치 위치를 미리 정리해 주세요.",
                "vi": "Ngày mai sẽ nhập 2 container văn phòng vào, nhờ chuẩn bị sẵn vị trí lắp đặt.",
                "situation": "onsite"
            },
            {
                "ko": "이 컨테이너는 사무실로 쓰고, 옆 컨테이너는 회의실로 개조하겠습니다.",
                "vi": "Container này dùng làm văn phòng, container bên cạnh sẽ cải tạo thành phòng họp.",
                "situation": "formal"
            },
            {
                "ko": "더워서 컨테이너 안에서 일하기 힘들다는 불만이 많은데, 에어컨 추가 설치 검토 부탁합니다.",
                "vi": "Nhiều người phản ánh nóng khó làm việc trong container, nhờ xem xét lắp thêm điều hòa.",
                "situation": "informal"
            }
        ],
        "relatedTerms": ["kho-bai", "bai-tap-ket", "van-chuyen-noi-bo", "construction"]
    },
    {
        "slug": "bai-tap-ket",
        "korean": "집하장",
        "vietnamese": "bãi tập kết",
        "hanja": "集荷場",
        "hanjaReading": "集(모을 집) + 荷(짐 하) + 場(마당 장)",
        "pronunciation": "바이 땁 껫",
        "meaningKo": "여러 곳에서 들어온 자재나 장비를 임시로 모아두었다가 분류하여 각 작업 구역으로 배송하는 중간 집결 공간입니다. 통역 시 주의할 점은 베트남에서 'bãi tập kết'은 단순 보관 공간인 'kho bãi'(야적장)와는 달리 물류 허브 기능을 하는 동적 공간을 의미하므로, '입고→분류→출고'의 흐름이 빠르게 일어나는 곳임을 강조해야 합니다. 특히 대형 현장에서는 집하장에서 자재를 동별·층별로 사전 분류(phân loại trước)하여 현장 투입 효율을 높이는데, 베트남 현장에서는 이를 간과하고 무작위로 쌓아두는 경우가 많아 재작업(làm lại)이 발생하므로 사전 분류 프로세스를 명확히 전달해야 합니다.",
        "meaningVi": "Khu vực tập trung vật liệu từ nhiều nguồn khác nhau, sau đó phân loại và chuyển tiếp đến các khu vực thi công. Khác với kho bãi dùng để bảo quản lâu dài, bãi tập kết là điểm trung chuyển logistics với chu kỳ luân chuyển nhanh. Cần tổ chức khoa học để tránh tắc nghẽn và sai sót trong phân phối vật tư.",
        "context": "물류 계획, 자재 배송, 현장 동선",
        "culturalNote": "한국 대형 현장에서는 집하장을 현장 입구 근처에 별도로 확보하여 자재 입고→검수→분류→배송의 체계적 프로세스를 운영하지만, 베트남 중소형 현장에서는 공간 부족으로 인해 집하장과 야적장을 혼용하거나 도로변에 임시로 자재를 쌓아두는 경우가 많아 교통 혼잡과 도난 위험이 높습니다. 또한 베트남에서는 'bãi tập kết'을 지방자치단체에 신고해야 하는 경우가 있으므로(특히 도심 현장), 통역사는 이러한 행정 절차를 안내하여 단속(kiểm tra, xử phạt)을 피하도록 도와야 합니다. 특히 우기에는 집하장이 진흙탕이 되어 자재 오염과 작업 지연이 발생하므로 배수 시설(hệ thống thoát nước)과 포장(lát nền) 필요성을 강조해야 합니다.",
        "commonMistakes": [
            {
                "mistake": "bãi tập kết을 단순 '야적장'으로 번역",
                "correction": "'집하장' 또는 '물류 집결지'로 번역하여 중계 기능 강조",
                "explanation": "야적장(kho bãi)은 보관 위주, 집하장(bãi tập kết)은 분류·배송 위주로 목적이 다름"
            },
            {
                "mistake": "'입고 후 즉시 배송'이라는 원칙을 설명하지 않음",
                "correction": "'nhập - phân loại - xuất nhanh'(입고-분류-신속출고) 프로세스 명시",
                "explanation": "집하장에 자재가 장기간 쌓이면 본래 목적을 상실하므로 빠른 회전율 강조 필요"
            },
            {
                "mistake": "사전 분류(phân loại trước) 필요성을 언급하지 않음",
                "correction": "'분류 후 배송'을 '동별·층별로 미리 분류하여 투입'으로 구체화",
                "explanation": "분류 없이 배송하면 현장에서 재작업이 발생하여 비효율적임"
            },
            {
                "mistake": "행정 신고 의무를 안내하지 않음",
                "correction": "도심 현장은 'cần báo cáo chính quyền địa phương'(지방정부 신고 필요) 추가",
                "explanation": "베트남 일부 지역에서 집하장 무단 운영 시 단속 대상이 됨"
            }
        ],
        "examples": [
            {
                "ko": "집하장에서 자재를 동별로 분류한 후 각 작업 구역으로 배송하세요.",
                "vi": "Tại bãi tập kết, phân loại vật liệu theo từng tòa rồi mới chuyển đến khu vực thi công.",
                "situation": "onsite"
            },
            {
                "ko": "집하장이 혼잡해서 자재 찾기가 어렵다는 불만이 많은데, 구역 표시를 명확히 해 주세요.",
                "vi": "Nhiều người phàn nàn bãi tập kết lộn xộn, khó tìm vật liệu, nhờ đánh dấu khu vực rõ ràng.",
                "situation": "informal"
            },
            {
                "ko": "도심 현장이라 집하장 운영 전에 구청 신고를 먼저 해야 합니다.",
                "vi": "Vì là công trường nội thành nên trước khi vận hành bãi tập kết phải báo cáo quận trước.",
                "situation": "formal"
            }
        ],
        "relatedTerms": ["kho-bai", "nhap-kho", "xuat-kho", "van-chuyen-noi-bo"]
    },
    {
        "slug": "quan-ly-ton-kho",
        "korean": "재고관리",
        "vietnamese": "quản lý tồn kho",
        "hanja": "在庫管理",
        "hanjaReading": "在(있을 재) + 庫(곳간 고) + 管(대롱 관) + 理(다스릴 리)",
        "pronunciation": "꽌 리 똔 커",
        "meaningKo": "건설 현장의 자재와 장비 재고를 체계적으로 파악하고 적정 수준을 유지하며 입출고를 기록·관리하는 업무입니다. 통역 시 주의할 점은 베트남에서 'quản lý tồn kho'는 단순 수량 관리를 넘어 'hàng tồn kho chết'(사장 재고), 'hàng sắp hết hạn'(유효기간 임박 자재) 등 품질 관리까지 포함하는 개념인데, 한국 현장에서는 이를 별도의 '품질 관리' 업무로 분리하는 경우가 많으므로 업무 범위를 명확히 해야 합니다. 특히 ERP 시스템을 사용하는 한국 현장에서는 실시간 재고 데이터(dữ liệu tồn kho thời gian thực)를 중시하는데, 베트남 중소형 현장에서는 일일 또는 주간 단위로 수기 업데이트하는 경우가 많아 데이터 신뢰도 격차가 발생할 수 있습니다.",
        "meaningVi": "Công tác theo dõi, kiểm soát số lượng và chất lượng vật tư, thiết bị hiện có tại kho hoặc công trường, đảm bảo cung ứng đủ cho thi công mà không dư thừa gây lãng phí. Bao gồm ghi chép nhập-xuất, kiểm kê định kỳ, cảnh báo hàng sắp hết, phát hiện hàng tồn kho chết, và đối chiếu với kế hoạch sử dụng.",
        "context": "물류 운영, 원가 관리, 공정 계획",
        "culturalNote": "한국 건설 현장에서는 JIT(적시 생산) 방식으로 재고를 최소화하여 보관 비용과 자금 회전율을 개선하는 것이 일반적이지만, 베트남 현장에서는 공급 불안정(배송 지연, 품질 불량 등)을 우려하여 '안전 재고(tồn kho an toàn)'를 과다하게 확보하는 경향이 있습니다. 이로 인해 현장 공간 부족과 자재 노후화 문제가 발생하므로, 통역사는 적정 재고 수준 산정 방법(công thức tính tồn kho hợp lý)을 설명하고 과잉 재고의 폐해를 인식시켜야 합니다. 또한 베트남에서는 시멘트, 페인트 등 유효기간이 있는 자재의 선입선출(FIFO - First In First Out) 원칙이 잘 지켜지지 않아 자재 손실이 크므로, 이를 강조하고 날짜별 재고 관리(quản lý theo ngày sản xuất) 시스템 도입을 제안해야 합니다.",
        "commonMistakes": [
            {
                "mistake": "'재고관리'를 단순 'quản lý hàng tồn'으로 번역",
                "correction": "'quản lý tồn kho'로 전문 용어 사용",
                "explanation": "'tồn kho'가 재고를 의미하는 정확한 물류 용어임"
            },
            {
                "mistake": "안전 재고 개념을 설명하지 않음",
                "correction": "'tồn kho an toàn'(안전 재고)과 'tồn kho tối đa'(최대 재고) 개념 명시",
                "explanation": "적정 재고 범위를 설정해야 과잉·부족 방지 가능"
            },
            {
                "mistake": "FIFO 원칙을 'xuất trước nhập sau'로 오역",
                "correction": "'xuất trước hàng nhập trước' 또는 'FIFO - First In First Out'",
                "explanation": "선입선출은 먼저 들어온 것을 먼저 내보내는 것이므로 정확히 번역해야 함"
            },
            {
                "mistake": "실시간 재고 업데이트 필요성을 강조하지 않음",
                "correction": "'cập nhật tồn kho theo thời gian thực'(실시간 업데이트) 요구 명시",
                "explanation": "한국 ERP 시스템은 실시간 데이터를 전제로 하므로 이를 명확히 전달해야 함"
            }
        ],
        "examples": [
            {
                "ko": "재고관리 시스템에 매일 입출고 내역을 입력해서 실시간 재고를 파악하세요.",
                "vi": "Hàng ngày nhập dữ liệu xuất-nhập vào hệ thống quản lý tồn kho để nắm tồn kho thời gian thực.",
                "situation": "formal"
            },
            {
                "ko": "시멘트는 유효기간이 있으니 선입선출 원칙을 꼭 지켜주세요.",
                "vi": "Xi măng có hạn sử dụng nên nhất định phải tuân thủ nguyên tắc FIFO (xuất trước hàng nhập trước).",
                "situation": "onsite"
            },
            {
                "ko": "안전 재고를 너무 많이 쌓아두면 창고 공간도 부족하고 자재도 상할 수 있어요.",
                "vi": "Nếu tồn kho an toàn quá nhiều thì vừa thiếu chỗ kho vừa có thể làm hỏng vật liệu.",
                "situation": "informal"
            }
        ],
        "relatedTerms": ["nhap-kho", "xuat-kho", "kiem-ke", "kho-bai"]
    }
]

# Filter out duplicates
new_terms_filtered = [t for t in new_terms if t['slug'] not in existing_slugs]

# Extend data with new terms
data.extend(new_terms_filtered)

# Write back to file
with open(file_path, 'w', encoding='utf-8') as f:
    json.dump(data, f, ensure_ascii=False, indent=2)

print(f"✅ Added {len(new_terms_filtered)} new terms to construction.json")
print(f"📊 Total terms now: {len(data)}")
print(f"🏗️ Theme: Construction Logistics/Material Management")
print("\nAdded terms:")
for t in new_terms_filtered:
    print(f"  - {t['slug']}: {t['korean']} ({t['vietnamese']})")
