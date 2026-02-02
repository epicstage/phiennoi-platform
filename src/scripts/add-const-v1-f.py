#!/usr/bin/env python3
import json, os

file_path = os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', 'data', 'terms', 'construction.json')

with open(file_path, 'r', encoding='utf-8') as f:
    data = json.load(f)

existing_slugs = {t['slug'] for t in data}

new_terms = [
    {
        "slug": "dam-h",
        "korean": "H빔",
        "vietnamese": "Dầm H",
        "hanja": None,
        "hanjaReading": None,
        "pronunciation": "쯤 하익",
        "meaningKo": "H자 형태의 단면을 가진 구조용 강재로, 철골 건축의 기둥과 보로 가장 많이 사용되는 자재입니다. 플랜지(날개 부분)와 웹(중앙 수직 부분)으로 구성되며, 휨강도가 높아 장스팬 구조물에 적합합니다. 통역 시 H빔의 규격(예: H-400×200×8×13)을 정확히 전달해야 하며, 플랜지 두께와 웹 두께를 구분하여 설명해야 합니다. 현장에서는 '에이치빔', '형강'으로 불리며, 용접 접합 시 용접 순서와 변형 관리가 중요합니다.",
        "meaningVi": "Thép kết cấu có tiết diện hình chữ H, là vật liệu phổ biến nhất cho cột và dầm trong xây dựng khung thép. Gồm cánh (flange) và vách (web), có độ bền uốn cao phù hợp cho kết cấu nhịp lớn. Khi thông dịch cần truyền đạt chính xác quy cách (ví dụ: H-400×200×8×13), phân biệt độ dày cánh và độ dày vách.",
        "context": "철골공사, 구조공사, 강구조",
        "culturalNote": "한국 건설현장에서는 H빔 규격을 밀리미터로 표기하며 4개 숫자로 표시(높이×너비×웹두께×플랜지두께)하지만, 베트남은 일부 현장에서 인치 단위를 혼용하는 경우가 있어 단위 확인이 필수입니다. 한국은 용접 품질관리가 엄격하여 비파괴검사를 필수로 하지만 베트남은 현장 여건에 따라 검사가 생략되는 경우도 있습니다.",
        "commonMistakes": [
            {"mistake": "Dầm I (I빔)", "correction": "Dầm H (H빔)", "explanation": "H빔과 I빔은 플랜지 두께가 다른 별개의 강재입니다"},
            {"mistake": "규격 숫자 순서 혼동", "correction": "높이×너비×웹두께×플랜지두께 순서 정확히 전달", "explanation": "규격 오류는 강도 계산 오류로 이어집니다"},
            {"mistake": "현장 속어 '형강'을 그대로 번역", "correction": "Dầm H 또는 Thép hình H로 정확히 전달", "explanation": "전문용어를 사용해야 도면과 일치합니다"}
        ],
        "examples": [
            {"ko": "H-400×200×8×13 빔을 현장에 반입하세요", "vi": "Hãy đưa dầm H-400×200×8×13 vào công trường", "situation": "formal"},
            {"ko": "이 H빔 용접 품질 확인 좀 해봐", "vi": "Kiểm tra chất lượng hàn dầm H này xem", "situation": "onsite"},
            {"ko": "형강 설치 전에 수직 확인 필수야", "vi": "Trước khi lắp dầm H phải kiểm tra độ thẳng đứng nhé", "situation": "informal"}
        ],
        "relatedTerms": ["철골", "용접", "플랜지"]
    },
    {
        "slug": "bu-long-neo",
        "korean": "앵커볼트",
        "vietnamese": "Bu lông neo",
        "hanja": None,
        "hanjaReading": None,
        "pronunciation": "부 롱 네오",
        "meaningKo": "철골 기둥을 콘크리트 기초에 고정하기 위해 미리 매립하는 볼트로, 철골 구조물의 안정성을 결정하는 핵심 부재입니다. 기초 콘크리트 타설 전 거푸집에 정확한 위치와 수직도를 맞춰 설치하며, 설치 오차가 ±5mm 이내여야 철골 기둥 설치가 가능합니다. 통역 시 앵커볼트의 매립 깊이, 노출 길이, 나사산 보호, 수직도 허용오차를 정확히 전달해야 하며, 위치 오류 발생 시 보수 방법(에폭시 그라우팅, 케미컬 앵커 등)을 설명할 수 있어야 합니다.",
        "meaningVi": "Bu lông được chôn sẵn trong móng bê tông để cố định cột thép, là cấu kiện quyết định độ ổn định của kết cấu thép. Phải lắp đặt với vị trí chính xác và độ thẳng đứng trước khi đổ bê tông móng, sai số lắp đặt phải nằm trong ±5mm để có thể lắp được cột thép. Khi thông dịch cần truyền đạt chính xác độ sâu chôn, chiều dài lộ ra, bảo vệ ren và sai số độ thẳng đứng cho phép.",
        "context": "기초공사, 철골조립, 정밀시공",
        "culturalNote": "한국 현장에서는 앵커볼트 설치를 철골업체가 직접 관리하며 전문 지그(jig)를 사용해 정밀도를 확보하지만, 베트남 현장에서는 토목팀이 설치하고 정밀도가 낮아 철골 설치 시 보정이 필요한 경우가 많습니다. 한국은 설치 후 검측을 필수로 하고 기록을 남기지만 베트남은 육안 확인에 그치는 경우가 있어 품질 관리에 주의가 필요합니다.",
        "commonMistakes": [
            {"mistake": "Neo móng (기초 앵커)", "correction": "Bu lông neo (앵커볼트)", "explanation": "볼트라는 것을 명시해야 합니다"},
            {"mistake": "설치 오차 기준을 전달하지 않음", "correction": "±5mm 이내 오차 기준 명확히 전달", "explanation": "허용오차 초과 시 철골 설치 불가능합니다"},
            {"mistake": "나사산 손상 주의사항 누락", "correction": "콘크리트 타설 전 나사산 보호 필수 안내", "explanation": "나사산 손상 시 볼트 교체가 매우 어렵습니다"}
        ],
        "examples": [
            {"ko": "앵커볼트 위치 오차가 10mm라 철골 못 올려요", "vi": "Sai lệch vị trí bu lông neo 10mm nên không lắp được cột thép", "situation": "onsite"},
            {"ko": "앵커볼트 수직도 검측 완료했습니다", "vi": "Đã hoàn tất kiểm tra độ thẳng đứng của bu lông neo", "situation": "formal"},
            {"ko": "볼트 나사산 망가졌으니 케미컬 앵커로 보강해", "vi": "Ren bu lông hỏng rồi nên phải gia cố bằng neo hóa chất", "situation": "informal"}
        ],
        "relatedTerms": ["기초", "철골", "정밀시공"]
    },
    {
        "slug": "han",
        "korean": "용접",
        "vietnamese": "Hàn",
        "hanja": "熔接",
        "hanjaReading": "熔(녹을 용) + 接(이을 접)",
        "pronunciation": "한",
        "meaningKo": "금속 부재를 열로 녹여 접합하는 공법으로, 철골 구조의 주요 연결 방법입니다. 아크용접, 가스용접, CO2용접 등 종류가 다양하며, 용접사 자격증(기능사, 산업기사, 기사)을 보유한 전문 인력이 시공합니다. 통역 시 용접 종류, 용접 자세(아래보기, 수평, 수직, 위보기), 예열 온도, 패스 수, 비파괴검사(RT, UT, MT) 요구사항을 정확히 전달해야 합니다. 용접 품질은 구조물 안전에 직결되므로 용접 결함(기공, 언더컷, 오버랩 등) 용어를 정확히 알아야 합니다.",
        "meaningVi": "Phương pháp nối các cấu kiện kim loại bằng cách nung chảy bằng nhiệt, là phương pháp liên kết chính trong kết cấu thép. Có nhiều loại như hàn hồ quang, hàn khí, hàn CO2, do nhân lực chuyên môn có chứng chỉ thợ hàn thi công. Khi thông dịch cần truyền đạt chính xác loại hàn, tư thế hàn (phẳng, ngang, đứng, trần), nhiệt độ nung sơ, số mối hàn, yêu cầu kiểm tra không phá hủy (RT, UT, MT).",
        "context": "철골공사, 배관공사, 품질관리",
        "culturalNote": "한국은 용접사 자격 등급이 엄격하고 중요 부위는 특급 용접사만 작업 가능하며, 용접 후 100% 비파괴검사를 실시하지만, 베트남은 자격 관리가 덜 엄격하고 샘플 검사로 대체하는 경우가 많습니다. 한국 현장에서는 날씨(바람, 습도)에 따라 용접 작업을 중단하지만 베트남은 작업 진행을 우선시하는 경향이 있어 품질 문제가 발생할 수 있습니다.",
        "commonMistakes": [
            {"mistake": "Nối (일반 접합)", "correction": "Hàn (용접)", "explanation": "용접은 열을 사용하는 특수 접합법입니다"},
            {"mistake": "용접 자세를 설명 없이 넘어감", "correction": "아래보기/수평/수직/위보기 자세 구분하여 전달", "explanation": "용접 난이도와 품질이 자세에 따라 달라집니다"},
            {"mistake": "비파괴검사 약자만 전달", "correction": "RT(방사선투과검사), UT(초음파탐상검사) 등 풀네임과 목적 설명", "explanation": "검사 방법에 따라 준비사항이 다릅니다"}
        ],
        "examples": [
            {"ko": "이 부위는 완전용입용접으로 시공하세요", "vi": "Phần này hãy thi công bằng hàn thấm hoàn toàn", "situation": "formal"},
            {"ko": "용접부 비파괴검사 결과 기공 발견됨", "vi": "Kết quả kiểm tra không phá hủy phát hiện lỗ khí tại mối hàn", "situation": "onsite"},
            {"ko": "바람 많이 부니까 용접 중단하고 내일 해", "vi": "Gió mạnh quá nên dừng hàn lại, mai hãy làm", "situation": "informal"}
        ],
        "relatedTerms": ["철골", "비파괴검사", "용접사"]
    },
    {
        "slug": "vit-cao-cuong-do",
        "korean": "고장력볼트",
        "vietnamese": "Vít cao cường độ",
        "hanja": "高張力",
        "hanjaReading": "高(높을 고) + 張(베풀 장) + 力(힘 력)",
        "pronunciation": "빗 까오 꾸엉 도",
        "meaningKo": "일반 볼트보다 강도가 높은 특수 볼트로, 철골 구조의 주요 접합 부재입니다. F8T, F10T 등 강도 등급이 있으며, 토크렌치로 규정 토크값까지 조임하여 마찰력으로 하중을 전달합니다. 통역 시 고장력볼트의 1차 조임, 본 조임, 마킹 확인, 너트 회전법 등 시공 순서를 정확히 전달해야 하며, 토크값(예: 200N·m)과 볼트 조임 순서(중앙에서 외곽으로)를 명확히 설명해야 합니다. 재사용 불가 원칙과 조임 후 마킹 검사를 반드시 안내해야 합니다.",
        "meaningVi": "Bu lông đặc biệt có cường độ cao hơn bu lông thường, là cấu kiện nối chính trong kết cấu thép. Có các cấp độ bền như F8T, F10T, được siết bằng cờ lê lực đến giá trị mô-men quy định để truyền tải trọng bằng lực ma sát. Khi thông dịch cần truyền đạt chính xác trình tự thi công: siết sơ bộ, siết chính, kiểm tra đánh dấu, phương pháp xoay đai ốc, giá trị mô-men (ví dụ: 200N·m) và thứ tự siết (từ giữa ra ngoài).",
        "context": "철골조립, 볼트접합, 정밀시공",
        "culturalNote": "한국 현장에서는 고장력볼트 조임을 전문팀이 토크렌치로 수행하고 조임 기록을 남기며, 조임 후 페인트 마킹으로 육안 검사를 하지만, 베트남 현장에서는 일반 임팩렌치로 조이고 토크 확인을 생략하는 경우가 있어 접합부 품질 문제가 발생할 수 있습니다. 한국은 볼트 재사용을 절대 금지하지만 베트남은 현장 여건상 재사용하는 경우가 있어 주의가 필요합니다.",
        "commonMistakes": [
            {"mistake": "Bu lông thường (일반 볼트)", "correction": "Vít cao cường độ 또는 Bu lông cường độ cao", "explanation": "고장력볼트는 특수 강재로 만든 고강도 볼트입니다"},
            {"mistake": "토크값 전달 누락", "correction": "규정 토크값(N·m)과 조임 순서 명확히 전달", "explanation": "토크 부족 시 접합부 파괴 위험이 있습니다"},
            {"mistake": "재사용 금지 원칙 미전달", "correction": "고장력볼트는 한 번만 사용 가능함을 강조", "explanation": "재사용 시 소성변형으로 강도 저하됩니다"}
        ],
        "examples": [
            {"ko": "F10T 고장력볼트로 200N·m까지 조이세요", "vi": "Hãy siết vít cao cường độ F10T đến 200N·m", "situation": "formal"},
            {"ko": "볼트 조인 후 마킹 확인 안 된 거 다시 조여", "vi": "Những vít siết rồi mà chưa có đánh dấu thì siết lại nhé", "situation": "onsite"},
            {"ko": "이 볼트 한번 썼던 건데 다시 쓰면 안 돼", "vi": "Vít này đã dùng rồi, không được dùng lại đâu", "situation": "informal"}
        ],
        "relatedTerms": ["볼트조임", "토크렌치", "철골"]
    },
    {
        "slug": "phu-chong-chay",
        "korean": "내화피복",
        "vietnamese": "Phủ chống cháy",
        "hanja": "耐火被覆",
        "hanjaReading": "耐(견딜 내) + 火(불 화) + 被(입을 피) + 覆(덮을 복)",
        "pronunciation": "푸 쫑 짜이",
        "meaningKo": "화재 시 철골의 급속한 온도 상승을 방지하여 구조물 붕괴를 막는 보호층으로, 건축물의 내화 성능을 확보하는 핵심 공정입니다. 뿜칠 내화피복(습식), 내화보드(건식), 내화페인트 등 종류가 있으며, 건물 용도에 따라 1시간, 2시간, 3시간 내화 등급이 요구됩니다. 통역 시 내화피복 두께, 시공 방법, 양생 기간, 품질 시험(접착력 시험, 밀도 시험) 요구사항을 정확히 전달해야 하며, 철골 표면 전처리(녹 제거, 프라이머 도장)가 선행되어야 함을 안내해야 합니다.",
        "meaningVi": "Lớp bảo vệ ngăn chặn sự gia tăng nhiệt độ nhanh của kết cấu thép khi hỏa hoạn để tránh sụp đổ công trình, là công đoạn then chốt đảm bảo khả năng chống cháy của công trình. Có các loại như phun chống cháy (ướt), tấm chống cháy (khô), sơn chống cháy, tùy theo mục đích sử dụng tòa nhà yêu cầu cấp chống cháy 1 giờ, 2 giờ, 3 giờ. Khi thông dịch cần truyền đạt chính xác độ dày lớp phủ, phương pháp thi công, thời gian dưỡng hộ, yêu cầu thử nghiệm chất lượng (thử lực bám dính, thử mật độ).",
        "context": "내화공사, 소방안전, 철골마감",
        "culturalNote": "한국은 건축법령에서 내화 등급을 엄격히 규정하고 시공 후 공인기관 성능 시험을 의무화하지만, 베트남은 규정이 상대적으로 느슨하고 시험 없이 육안 검사로 대체하는 경우가 많습니다. 한국 현장에서는 내화피복 시공 전 철골 표면 청결도 기준(Sa 2.5급)을 요구하지만 베트남은 간단한 청소로 넘어가는 경우가 있어 접착 불량이 발생할 수 있습니다.",
        "commonMistakes": [
            {"mistake": "Sơn chống cháy (내화페인트)", "correction": "Phủ chống cháy (내화피복 일반)", "explanation": "내화피복은 페인트 외에 뿜칠, 보드 등 다양한 방법을 포괄합니다"},
            {"mistake": "내화 등급 시간 전달 누락", "correction": "1시간/2시간/3시간 내화 등급 명확히 전달", "explanation": "등급에 따라 피복 두께가 달라집니다"},
            {"mistake": "철골 전처리 필요성 미안내", "correction": "녹 제거, 프라이머 도장 후 내화피복 시공 필수", "explanation": "전처리 없으면 접착력 저하로 탈락합니다"}
        ],
        "examples": [
            {"ko": "이 건물은 2시간 내화 등급이 필요합니다", "vi": "Tòa nhà này cần cấp chống cháy 2 giờ", "situation": "formal"},
            {"ko": "내화피복 시공 전에 철골 녹 다 제거해야 돼", "vi": "Trước khi thi công phủ chống cháy phải loại hết rỉ trên thép nhé", "situation": "onsite"},
            {"ko": "내화뿜칠 두께 50mm로 균일하게 시공하세요", "vi": "Hãy thi công phun chống cháy đồng đều với độ dày 50mm", "situation": "formal"}
        ],
        "relatedTerms": ["철골", "소방", "내화등급"]
    },
    {
        "slug": "tam-san-thep",
        "korean": "데크플레이트",
        "vietnamese": "Tấm sàn thép",
        "hanja": None,
        "hanjaReading": None,
        "pronunciation": "땀 산 텝",
        "meaningKo": "파형 단면의 얇은 강판으로, 철골 구조물의 바닥 슬래브 거푸집 겸 보강재로 사용되는 자재입니다. 콘크리트 타설 시 거푸집 역할을 하고 경화 후에는 슬래브 하부 인장철근 역할을 하여 거푸집 해체가 불필요한 영구 거푸집입니다. 통역 시 데크플레이트의 두께(0.8mm, 1.0mm, 1.2mm), 높이(50mm, 75mm, 100mm), 지지 간격, 콘크리트 두께를 정확히 전달해야 하며, 스터드볼트 용접, 와이어메시 배근, 콘크리트 타설 순서를 설명할 수 있어야 합니다.",
        "meaningVi": "Tấm thép mỏng có tiết diện gợn sóng, được dùng làm ván khuôn kiêm cốt thép gia cường cho sàn bê tông trong kết cấu thép. Khi đổ bê tông đóng vai trò ván khuôn, sau khi đông cứng đóng vai trò thép chịu kéo phía dưới sàn, là ván khuôn vĩnh viễn không cần tháo dỡ. Khi thông dịch cần truyền đạt chính xác độ dày (0.8mm, 1.0mm, 1.2mm), chiều cao (50mm, 75mm, 100mm), khoảng cách chống đỡ, độ dày bê tông, và giải thích trình tự hàn đinh chống cắt, đặt lưới thép, đổ bê tông.",
        "context": "철골공사, 슬래브공사, 바닥공사",
        "culturalNote": "한국 철골 건축에서는 데크플레이트가 표준 공법으로 자리잡아 시공 속도가 빠르고 품질이 균일하지만, 베트남에서는 전통적인 합판 거푸집을 선호하는 경향이 있어 데크플레이트 시공 경험이 부족한 인력이 많습니다. 한국은 데크플레이트 하부 지지 간격과 콘크리트 타설 속도를 엄격히 관리하지만 베트남은 관리가 느슨하여 처짐이나 변형이 발생할 수 있습니다.",
        "commonMistakes": [
            {"mistake": "Ván khuôn thép (강재 거푸집)", "correction": "Tấm sàn thép 또는 Deck plate", "explanation": "데크플레이트는 영구적으로 남는 구조 부재입니다"},
            {"mistake": "규격 전달 시 두께만 언급", "correction": "두께, 높이, 지지 간격 모두 전달", "explanation": "규격이 불완전하면 구조 계산 오류 발생합니다"},
            {"mistake": "콘크리트 두께 계산 오류", "correction": "데크 상단부터의 콘크리트 두께를 명확히 설명", "explanation": "총 슬래브 두께와 데크 위 콘크리트 두께를 구분해야 합니다"}
        ],
        "examples": [
            {"ko": "데크플레이트 1.0t, 높이 75mm로 시공하세요", "vi": "Hãy thi công tấm sàn thép dày 1.0mm, cao 75mm", "situation": "formal"},
            {"ko": "데크 위에 콘크리트 100mm 타설 예정입니다", "vi": "Dự định đổ bê tông dày 100mm trên tấm sàn thép", "situation": "formal"},
            {"ko": "데크 처짐 생겼으니 중간에 서포트 더 대", "vi": "Tấm sàn bị võng rồi nên thêm giá đỡ ở giữa", "situation": "onsite"}
        ],
        "relatedTerms": ["슬래브", "철골", "거푸집"]
    },
    {
        "slug": "gia-dan-hinh-tam-giac",
        "korean": "트러스",
        "vietnamese": "Giàn dàn hình tam giác",
        "hanja": None,
        "hanjaReading": None,
        "pronunciation": "잔 잔 힌 땀 짝",
        "meaningKo": "삼각형 골조를 기본 단위로 조합한 구조체로, 장스팬 지붕이나 다리 등에 사용되는 경량 구조입니다. 상현재(상부), 하현재(하부), 사재(대각선 부재)로 구성되며, 축력만 받는 부재들의 조합으로 휨모멘트 없이 하중을 전달하여 효율적입니다. 통역 시 트러스의 형식(프랫 트러스, 워렌 트러스, 하우 트러스 등), 부재명(상현재, 하현재, 사재), 접합부 방식(핀 접합, 용접 접합)을 정확히 전달해야 하며, 조립 순서와 가설 지지대 계획을 설명할 수 있어야 합니다.",
        "meaningVi": "Kết cấu được tổ hợp từ khung tam giác làm đơn vị cơ bản, là kết cấu nhẹ được sử dụng cho mái nhịp lớn hoặc cầu. Gồm dây thượng (trên), dây hạ (dưới), thanh xiên (đường chéo), các thanh chỉ chịu lực dọc trục kết hợp để truyền tải trọng mà không có mômen uốn nên rất hiệu quả. Khi thông dịch cần truyền đạt chính xác dạng giàn (Pratt, Warren, Howe...), tên các thanh (dây thượng, dây hạ, thanh xiên), phương pháp liên kết (chốt, hàn) và giải thích trình tự lắp ráp cùng kế hoạch giá đỡ tạm.",
        "context": "지붕공사, 장스팬구조, 철골조립",
        "culturalNote": "한국에서는 대형 체육관이나 공장 지붕에 트러스를 많이 사용하고 공장에서 제작하여 현장 조립하는 방식이 일반적이며, 크레인으로 일괄 양중하지만, 베트남에서는 현장 제작 비중이 높고 소규모로 나누어 조립하는 경우가 많아 정밀도와 안전 관리에 차이가 있습니다. 한국은 트러스 처짐 검토를 정밀하게 하지만 베트남은 간단한 경험식으로 계산하는 경우가 있습니다.",
        "commonMistakes": [
            {"mistake": "Khung tam giác (삼각형 프레임)", "correction": "Giàn dàn hình tam giác 또는 Truss", "explanation": "트러스는 여러 삼각형이 조합된 특수 구조입니다"},
            {"mistake": "부재명 혼동 (상현재/하현재)", "correction": "Dây thượng(상현재), Dây hạ(하현재), Thanh xiên(사재) 구분", "explanation": "부재 역할이 다르므로 정확히 구분해야 합니다"},
            {"mistake": "조립 순서 설명 없이 시공", "correction": "중앙부터 또는 단부부터 조립 순서 명확히 안내", "explanation": "순서 오류 시 변형이나 붕괴 위험이 있습니다"}
        ],
        "examples": [
            {"ko": "프랫 트러스 형식으로 30m 스팬 지붕을 계획합니다", "vi": "Kế hoạch mái nhịp 30m bằng giàn dàn dạng Pratt", "situation": "formal"},
            {"ko": "트러스 상현재 용접 품질 확인 필요해", "vi": "Cần kiểm tra chất lượng hàn dây thượng của giàn dàn", "situation": "onsite"},
            {"ko": "트러스 조립할 때 중간에 임시 서포트 꼭 대야 해", "vi": "Khi lắp giàn dàn nhất định phải chống đỡ tạm ở giữa nhé", "situation": "informal"}
        ],
        "relatedTerms": ["철골", "장스팬", "지붕"]
    },
    {
        "slug": "thanh-chong-doc",
        "korean": "브레이싱",
        "vietnamese": "Thanh chống dọc",
        "hanja": None,
        "hanjaReading": None,
        "pronunciation": "탄 쫑 족",
        "meaningKo": "철골 구조물의 횡력(풍하중, 지진하중)에 저항하기 위해 설치하는 대각선 보강재로, 건물의 수평 안정성을 확보하는 핵심 부재입니다. X형, K형, V형 등 형태가 다양하며, 가새 또는 버팀대라고도 불립니다. 통역 시 브레이싱의 형식, 설치 위치, 접합 방법, 긴장력 도입 여부를 정확히 전달해야 하며, 수직 부재(기둥)와 수평 부재(보) 사이의 각도와 연결 상세를 설명할 수 있어야 합니다. 시공 중 가설 브레이싱과 영구 브레이싱을 구분하는 것도 중요합니다.",
        "meaningVi": "Thanh gia cường chéo được lắp đặt để chống lại lực ngang (gió, động đất) của kết cấu thép, là cấu kiện then chốt đảm bảo độ ổn định ngang cho công trình. Có nhiều dạng như hình X, K, V, còn gọi là thanh giằng hoặc thanh chống. Khi thông dịch cần truyền đạt chính xác dạng, vị trí lắp đặt, phương pháp liên kết, có căng lực ban đầu hay không, và giải thích góc giữa thanh đứng (cột) và thanh ngang (dầm) cùng chi tiết kết nối. Phân biệt giữa thanh chống tạm trong thi công và thanh chống vĩnh viễn cũng quan trọng.",
        "context": "철골조립, 구조보강, 내진설계",
        "culturalNote": "한국 건축에서는 내진설계 의무화로 브레이싱 설치가 필수이며 구조 계산서에 명시된 위치와 규격을 엄격히 준수하지만, 베트남은 지진 빈도가 낮아 브레이싱 설치가 생략되거나 간소화되는 경우가 많습니다. 한국은 브레이싱 설치 후 긴장력 확인을 하지만 베트남은 볼트 조임만 확인하고 긴장력 측정을 생략하는 경향이 있습니다.",
        "commonMistakes": [
            {"mistake": "Thanh xiên (사재)", "correction": "Thanh chống dọc (브레이싱)", "explanation": "트러스의 사재와 횡력 저항용 브레이싱은 역할이 다릅니다"},
            {"mistake": "형식 구분 없이 '브레이싱'만 언급", "correction": "X형/K형/V형 등 형식 명확히 전달", "explanation": "형식에 따라 효과와 시공 방법이 다릅니다"},
            {"mistake": "가설과 영구 구분 안 함", "correction": "시공 중 임시 브레이싱과 영구 브레이싱 구분", "explanation": "임시는 해체되고 영구는 남아야 합니다"}
        ],
        "examples": [
            {"ko": "5층부터 10층까지 X형 브레이싱을 설치하세요", "vi": "Hãy lắp thanh chống dọc dạng X từ tầng 5 đến tầng 10", "situation": "formal"},
            {"ko": "브레이싱 볼트 조임 후 긴장력 확인 필요", "vi": "Sau khi siết bu lông thanh chống cần kiểm tra lực căng", "situation": "onsite"},
            {"ko": "철골 세우는 동안 임시 브레이싱 계속 유지해야 돼", "vi": "Trong khi dựng thép phải giữ thanh chống tạm liên tục nhé", "situation": "informal"}
        ],
        "relatedTerms": ["철골", "내진", "횡력"]
    },
    {
        "slug": "tam-gusset",
        "korean": "가셋플레이트",
        "vietnamese": "Tấm gusset",
        "hanja": None,
        "hanjaReading": None,
        "pronunciation": "땀 거쎗",
        "meaningKo": "철골 부재들이 만나는 접합부에서 응력을 분산시키고 접합 강도를 높이기 위해 덧대는 보강판입니다. 브레이싱과 기둥·보의 접합부, 트러스 접합부 등에 사용되며, 용접이나 볼트로 고정됩니다. 통역 시 가셋플레이트의 두께, 크기, 형상, 볼트 구멍 위치, 용접 길이를 정확히 전달해야 하며, 응력 집중 방지를 위한 모서리 라운드 처리나 보강 리브 설치 여부를 설명할 수 있어야 합니다. 접합부 상세도를 참조하여 정확한 위치 선정이 중요합니다.",
        "meaningVi": "Tấm gia cường được ghép thêm tại nút nối của các thanh thép để phân tán ứng suất và tăng cường độ liên kết. Được sử dụng tại nút nối giữa thanh chống với cột-dầm, nút giàn dàn..., được cố định bằng hàn hoặc bu lông. Khi thông dịch cần truyền đạt chính xác độ dày, kích thước, hình dạng, vị trí lỗ bu lông, chiều dài hàn, và giải thích việc bo tròn góc hoặc lắp gân gia cường để tránh tập trung ứng suất. Quan trọng là chọn vị trí chính xác dựa trên bản vẽ chi tiết nút nối.",
        "context": "철골접합, 구조보강, 상세설계",
        "culturalNote": "한국 철골 공사에서는 가셋플레이트 두께와 용접 길이를 구조 계산서에 따라 엄격히 시공하고, 용접 후 비파괴검사를 실시하지만, 베트남에서는 경험적으로 두께를 결정하고 검사 없이 육안 확인으로 넘어가는 경우가 있습니다. 한국은 모서리 라운드 처리를 표준화하지만 베트님은 직각 처리로 응력 집중이 발생할 수 있습니다.",
        "commonMistakes": [
            {"mistake": "Tấm thép (일반 강판)", "correction": "Tấm gusset (가셋플레이트)", "explanation": "가셋은 접합부 보강 전용 부재입니다"},
            {"mistake": "두께만 전달하고 크기 누락", "correction": "두께, 가로×세로 크기, 볼트 구멍 위치 모두 전달", "explanation": "크기가 부족하면 응력 분산 효과가 없습니다"},
            {"mistake": "모서리 처리 지시 생략", "correction": "모서리 R처리(bo tròn) 또는 리브 보강 여부 안내", "explanation": "직각 모서리는 응력 집중으로 균열 위험이 있습니다"}
        ],
        "examples": [
            {"ko": "브레이싱 접합부에 두께 12mm 가셋플레이트를 용접하세요", "vi": "Hãy hàn tấm gusset dày 12mm tại nút nối thanh chống", "situation": "formal"},
            {"ko": "가셋 모서리는 반드시 R20으로 라운드 처리해", "vi": "Góc tấm gusset nhất định phải bo tròn R20 nhé", "situation": "onsite"},
            {"ko": "이 가셋 크기로는 응력 못 받아, 더 크게 해야 돼", "vi": "Kích thước tấm gusset này không đủ chịu ứng suất, phải làm to hơn", "situation": "informal"}
        ],
        "relatedTerms": ["브레이싱", "철골접합", "용접"]
    },
    {
        "slug": "vit-bulông",
        "korean": "볼트조임",
        "vietnamese": "Vít bu lông",
        "hanja": None,
        "hanjaReading": None,
        "pronunciation": "빗 불롱",
        "meaningKo": "철골 부재를 볼트와 너트로 체결하는 작업으로, 용접과 함께 철골 구조의 양대 접합 방법입니다. 일반볼트와 고장력볼트로 구분되며, 토크렌치나 임팩렌치를 사용하여 규정 토크값으로 조임합니다. 통역 시 볼트 규격(M16, M20, M22 등), 볼트 등급(4.6, 8.8, 10.9 등), 조임 토크값, 조임 순서(대각선 방향, 중앙에서 외곽으로), 와셔 사용 여부를 정확히 전달해야 하며, 볼트 체결 후 육안 검사(돌출 나사산 2~3산 확인)를 안내해야 합니다.",
        "meaningVi": "Công tác liên kết các thanh thép bằng bu lông và đai ốc, cùng với hàn là hai phương pháp liên kết chính trong kết cấu thép. Chia thành bu lông thường và bu lông cao cường độ, sử dụng cờ lê lực hoặc súng bu lông để siết đến giá trị mô-men quy định. Khi thông dịch cần truyền đạt chính xác quy cách bu lông (M16, M20, M22...), cấp bu lông (4.6, 8.8, 10.9...), giá trị mô-men siết, thứ tự siết (theo đường chéo, từ giữa ra ngoài), có dùng vòng đệm hay không, và hướng dẫn kiểm tra bằng mắt sau khi siết (kiểm tra 2~3 ren lộ ra).",
        "context": "철골조립, 볼트접합, 품질관리",
        "culturalNote": "한국 현장에서는 토크렌치로 정확한 토크값을 확인하며 조임 기록을 남기고, 조임 후 페인트 마킹으로 2차 확인을 하지만, 베트남 현장에서는 임팩렌치로 경험적으로 조이고 기록을 남기지 않는 경우가 많아 품질 편차가 큽니다. 한국은 볼트 조임 순서를 엄격히 지키지만 베트남은 편의에 따라 조이는 경우가 있어 접합부 변형이 발생할 수 있습니다.",
        "commonMistakes": [
            {"mistake": "Siết ốc (너트 조임)", "correction": "Vít bu lông (볼트 조임)", "explanation": "볼트와 너트는 세트이므로 'bu lông'으로 통칭합니다"},
            {"mistake": "토크값 확인 없이 조임", "correction": "규정 토크값까지 토크렌치로 확인하며 조임", "explanation": "토크 부족 시 접합부 이완, 과다 시 파단됩니다"},
            {"mistake": "조임 순서 무시", "correction": "대각선 방향, 중앙→외곽 순서 준수", "explanation": "순서 오류 시 접합면 변형이 발생합니다"}
        ],
        "examples": [
            {"ko": "M20 볼트를 150N·m로 조이세요", "vi": "Hãy siết bu lông M20 đến 150N·m", "situation": "formal"},
            {"ko": "볼트 조일 때 중앙부터 시작해서 바깥쪽으로 나가", "vi": "Khi siết bu lông bắt đầu từ giữa ra ngoài nhé", "situation": "onsite"},
            {"ko": "너트 돌출 나사산 2개 이상 나와야 합격이야", "vi": "Ren lộ ra từ đai ốc phải từ 2 ren trở lên mới đạt", "situation": "informal"}
        ],
        "relatedTerms": ["고장력볼트", "토크렌치", "철골"]
    }
]

filtered = [t for t in new_terms if t['slug'] not in existing_slugs]
data.extend(filtered)

with open(file_path, 'w', encoding='utf-8') as f:
    json.dump(data, f, ensure_ascii=False, indent=2)

print(f"Added {len(filtered)} terms. Total: {len(data)}")
