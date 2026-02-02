#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Construction(건설) 도메인 - 안전관리/환경 용어 추가 스크립트
테마: Safety & Environment (안전모, 안전벨트, 낙하물방지망, 추락방지, TBM, MSDS, 밀폐공간, 분진, 소음측정, 환경영향평가 등)
정확히 10개 신규 용어
"""

import json
import os

# 프로젝트 루트 기준 상대 경로
script_dir = os.path.dirname(os.path.abspath(__file__))
project_root = os.path.dirname(os.path.dirname(script_dir))
file_path = os.path.join(project_root, "src", "data", "terms", "construction.json")

# 추가할 용어 데이터 (정확히 10개)
new_terms = [
    {
        "slug": "mu-bao-ho",
        "korean": "안전모",
        "vietnamese": "Mũ bảo hộ",
        "hanja": "安全帽",
        "hanjaReading": "安(편안 안) + 全(온전 전) + 帽(모자 모)",
        "pronunciation": "안전모",
        "meaningKo": "건설 현장에서 낙하물이나 충격으로부터 머리를 보호하기 위해 착용하는 보호구. 통역 시 색상별 직급/직종 구분 관행(예: 흰색-감독관, 노란색-일반작업자, 파란색-전기공)을 설명해야 현장 혼선 방지 가능. 한국에서는 안전모 미착용 시 과태료 및 현장 출입 금지 조치가 엄격하므로, 베트남 근로자에게 반드시 착용 의무를 강조하고 턱끈 고정 여부까지 점검받는다는 점을 통역해야 실수를 줄일 수 있음.",
        "meaningVi": "Thiết bị bảo vệ đầu để chống lại vật rơi hoặc va chạm tại công trường xây dựng. Tại Hàn Quốc, việc không đeo mũ bảo hộ có thể bị phạt và cấm vào công trường, nên cần giải thích rõ quy định phân biệt màu sắc theo chức vụ (trắng-giám sát, vàng-công nhân, xanh-thợ điện) và yêu cầu buộc chặt dây đai cằm.",
        "context": "건설 현장 안전교육, 작업 착수 전 점검",
        "culturalNote": "한국 건설 현장은 안전모 색상으로 직급·직종을 엄격히 구분하며, 베트남보다 착용 점검이 훨씬 빈번함. 베트남 근로자는 턱끈을 느슨하게 매는 경우가 많아 한국 감독관이 재차 지적하는 경우가 잦으므로, 통역 시 '턱끈을 손가락 2개 들어갈 정도로 조이라'는 구체적 설명을 덧붙이면 현장 마찰 감소.",
        "commonMistakes": [
            {
                "mistake": "Mũ an toàn",
                "correction": "Mũ bảo hộ",
                "explanation": "'Mũ an toàn'는 일반적이나 공식 용어는 'Mũ bảo hộ lao động'이며 현장에서는 줄여서 'Mũ bảo hộ'라고 함"
            },
            {
                "mistake": "안전모를 '쓰다'만 강조",
                "correction": "착용 + 턱끈 고정 확인까지 통역",
                "explanation": "한국 현장은 안전모를 쓰기만 하면 되는 게 아니라 턱끈 미고정 시 미착용으로 간주하여 경고"
            },
            {
                "mistake": "색상 구분을 생략",
                "correction": "직급별 색상(흰색/노란색/파란색 등) 명시",
                "explanation": "베트남 근로자는 색상 규칙을 모르는 경우가 많아 타 직종 구역 출입 시 혼선 발생 가능"
            }
        ],
        "examples": [
            {
                "ko": "현장 출입 시 반드시 안전모를 착용하고 턱끈을 조여주세요.",
                "vi": "Khi vào công trường, bắt buộc phải đeo mũ bảo hộ và buộc chặt dây đai cằm.",
                "situation": "onsite"
            },
            {
                "ko": "노란색 안전모는 일반 작업자, 흰색은 감독관용입니다.",
                "vi": "Mũ bảo hộ màu vàng dành cho công nhân thường, màu trắng dành cho giám sát viên.",
                "situation": "formal"
            },
            {
                "ko": "안전모 미착용 적발 시 즉시 퇴출 조치됩니다.",
                "vi": "Nếu phát hiện không đeo mũ bảo hộ, sẽ bị đuổi ra khỏi công trường ngay lập tức.",
                "situation": "formal"
            }
        ],
        "relatedTerms": ["안전벨트", "낙하물방지망", "추락방지", "TBM"]
    },
    {
        "slug": "day-an-toan",
        "korean": "안전벨트",
        "vietnamese": "Dây an toàn",
        "hanja": "安全帶",
        "hanjaReading": "安(편안 안) + 全(온전 전) + 帶(띠 대)",
        "pronunciation": "안전벨트",
        "meaningKo": "고소작업이나 추락 위험이 있는 장소에서 작업자를 보호하기 위해 착용하는 추락방지 보호구. 통역 시 '안전대'와 '안전벨트'를 혼용하지 말고, 현장에서는 공식적으로 '안전대(추락방지대)'로 불리며 2m 이상 높이에서 작업 시 의무 착용 사항임을 명확히 전달해야 함. 한국은 고리 체결 불량으로 인한 추락사고가 빈발하므로 베트남 근로자에게 '더블 후크' 방식과 체결 확인 절차를 반복 설명하고, 안전대 훼손 여부를 작업 전 점검하도록 통역해야 사고 예방 가능.",
        "meaningVi": "Thiết bị bảo hộ chống rơi ngã khi làm việc trên cao hoặc nơi có nguy cơ té ngã. Tại Hàn Quốc, bắt buộc đeo 'dây an toàn (안전대)' khi làm việc trên độ cao từ 2m trở lên, phải kiểm tra móc kép (double hook) và tình trạng dây trước khi bắt đầu ca làm, vì tai nạn do móc lỏng rất phổ biến.",
        "context": "고소작업, 비계작업, 작업 전 안전점검",
        "culturalNote": "한국은 추락사고가 건설재해 1위여서 안전대 점검이 극도로 엄격하며, 베트남보다 훨씬 자주 감독관이 체결 상태를 확인함. 베트님 근로자는 '한 번 걸어두면 끝'이라 생각하는 경향이 있으나, 한국 현장은 이동할 때마다 더블 후크로 재체결하는 규칙을 요구하므로 통역 시 '이동 시마다 한쪽 고리는 항상 체결 유지'를 강조해야 안전사고 예방.",
        "commonMistakes": [
            {
                "mistake": "Dây đai an toàn",
                "correction": "Dây an toàn / Đai an toàn chống rơi",
                "explanation": "'Dây đai an toàn'는 자동차 안전벨트와 혼동 가능, 건설 현장에서는 'Dây an toàn' 또는 'Đai an toàn chống rơi'가 정확"
            },
            {
                "mistake": "'매다'만 통역",
                "correction": "체결 + 고리 확인 + 이동 시 더블 후크 절차까지 통역",
                "explanation": "한국은 단순 착용이 아니라 체결 상태와 이동 시 안전 절차까지 점검하므로 구체적 동작 설명 필수"
            },
            {
                "mistake": "高所作業(고소작업)을 '술 마시는 작업'으로 오해",
                "correction": "높은 곳에서 하는 작업 (Công việc trên cao)",
                "explanation": "한자 '高所'와 '高笑(술 마시며 즐거워함)'를 혼동하면 안전교육 내용 전체가 왜곡됨"
            }
        ],
        "examples": [
            {
                "ko": "2m 이상 고소작업 시 안전벨트를 반드시 착용하고 더블 후크로 체결하세요.",
                "vi": "Khi làm việc trên cao từ 2m trở lên, bắt buộc phải đeo dây an toàn và móc bằng móc kép (double hook).",
                "situation": "onsite"
            },
            {
                "ko": "안전벨트 고리가 헐겁거나 훼손된 경우 즉시 교체 요청하세요.",
                "vi": "Nếu móc dây an toàn bị lỏng hoặc hư hỏng, yêu cầu thay thế ngay lập tức.",
                "situation": "formal"
            },
            {
                "ko": "이동할 때는 한쪽 고리를 먼저 체결한 후 다른 쪽을 풀어야 합니다.",
                "vi": "Khi di chuyển, phải móc một bên trước rồi mới tháo bên còn lại.",
                "situation": "onsite"
            }
        ],
        "relatedTerms": ["안전모", "추락방지", "고소작업", "비계"]
    },
    {
        "slug": "luoi-chan-vat-roi",
        "korean": "낙하물방지망",
        "vietnamese": "Lưới chắn vật rơi",
        "hanja": "落下物防止網",
        "hanjaReading": "落(떨어질 락) + 下(아래 하) + 物(물건 물) + 防(막을 방) + 止(그칠 지) + 網(그물 망)",
        "pronunciation": "나카물방지망",
        "meaningKo": "건설 현장에서 공구나 자재가 아래로 떨어지는 것을 막기 위해 설치하는 그물망. 통역 시 '낙하물'과 '추락(사람이 떨어짐)'을 명확히 구분해야 하며, 낙하물방지망은 물건 낙하 방지용, 추락방지망은 사람 추락 방지용임을 설명해야 혼선 방지. 한국 현장은 3m 이상 고소작업 시 하부에 낙하물방지망 설치가 의무이며, 망 파손·처짐 여부를 매일 점검하므로 베트남 근로자에게 '망 위에 공구나 자재를 올려놓지 말 것'과 '파손 발견 즉시 보고'를 반복 교육해야 안전사고 예방.",
        "meaningVi": "Lưới được lắp đặt để ngăn chặn dụng cụ hoặc vật liệu rơi xuống phía dưới tại công trường xây dựng. Tại Hàn Quốc, bắt buộc phải lắp lưới chắn vật rơi khi làm việc trên độ cao từ 3m trở lên, cần kiểm tra hàng ngày tình trạng rách hoặc chùng xuống, tuyệt đối không để dụng cụ hoặc vật liệu trên lưới.",
        "context": "고소작업, 외부 비계작업, 안전점검",
        "culturalNote": "한국은 낙하물 사고로 인한 보행자·하부 작업자 피해가 잦아 낙하물방지망 설치와 점검이 매우 엄격함. 베트남 현장은 망을 설치만 하고 관리는 소홀한 경우가 있으나, 한국은 망 위에 자재를 올려두거나 파손된 채 방치 시 즉시 작업중지 명령이 내려지므로 통역 시 '낙하물방지망은 임시 보관소가 아님'을 명확히 전달해야 함.",
        "commonMistakes": [
            {
                "mistake": "Lưới an toàn (일반 안전망)",
                "correction": "Lưới chắn vật rơi (낙하물 전용)",
                "explanation": "'Lưới an toàn'는 추락방지망과 혼동 가능, 낙하물방지망은 'Lưới chắn vật rơi' 또는 'Lưới ngăn rơi vật liệu'로 구분"
            },
            {
                "mistake": "낙하물과 추락을 같은 단어로 통역",
                "correction": "낙하물(Vật rơi - 물건), 추락(Rơi ngã - 사람)",
                "explanation": "낙하물은 물건이 떨어지는 것, 추락은 사람이 떨어지는 것으로 안전장비와 대응 방법이 완전히 다름"
            },
            {
                "mistake": "'설치만 하면 됨'으로 안내",
                "correction": "설치 + 매일 점검 + 파손 즉시 보고까지 통역",
                "explanation": "한국은 망 파손·처짐 방치 시 작업중지 명령이 내려지므로 점검 의무까지 강조 필요"
            }
        ],
        "examples": [
            {
                "ko": "3층 이상 작업 시 하부에 낙하물방지망을 반드시 설치하세요.",
                "vi": "Khi làm việc từ tầng 3 trở lên, bắt buộc phải lắp lưới chắn vật rơi ở phía dưới.",
                "situation": "formal"
            },
            {
                "ko": "낙하물방지망 위에 공구나 자재를 올려놓지 마세요.",
                "vi": "Không được để dụng cụ hoặc vật liệu trên lưới chắn vật rơi.",
                "situation": "onsite"
            },
            {
                "ko": "망이 찢어지거나 처진 부분을 발견하면 즉시 보고하세요.",
                "vi": "Nếu phát hiện lưới bị rách hoặc chùng xuống, báo cáo ngay lập tức.",
                "situation": "onsite"
            }
        ],
        "relatedTerms": ["추락방지", "안전망", "비계", "고소작업"]
    },
    {
        "slug": "chong-roi-nga",
        "korean": "추락방지",
        "vietnamese": "Chống rơi ngã",
        "hanja": "墜落防止",
        "hanjaReading": "墜(떨어질 추) + 落(떨어질 락) + 防(막을 방) + 止(그칠 지)",
        "pronunciation": "추락방지",
        "meaningKo": "고소작업 중 작업자가 떨어지는 사고를 예방하기 위한 모든 안전 조치 및 장비 통칭. 통역 시 '추락방지'와 '낙하물방지'를 혼동하지 않도록 주의해야 하며, 추락방지는 사람이 떨어지지 않도록 하는 조치(안전대, 난간, 안전망 등)임을 명확히 해야 함. 한국 건설 현장에서는 추락사고가 사망재해 1위여서 2m 이상 높이에서 작업 시 난간 설치 또는 안전대 착용이 의무이며, 위반 시 즉각 작업중지 및 과태료 부과. 베트남 근로자는 '2m는 낮다'고 느낄 수 있으나 한국 기준은 절대적이므로 통역 시 '2m 이상 = 무조건 추락방지 조치'를 반복 강조해야 사고 예방.",
        "meaningVi": "Tất cả các biện pháp và thiết bị an toàn nhằm ngăn chặn tai nạn rơi ngã của người lao động khi làm việc trên cao. Tại Hàn Quốc, tai nạn rơi ngã là nguyên nhân tử vong hàng đầu nên bắt buộc phải có lan can hoặc đeo dây an toàn khi làm việc trên độ cao từ 2m, vi phạm sẽ bị dừng công việc và phạt tiền ngay lập tức.",
        "context": "고소작업, 비계작업, 안전교육",
        "culturalNote": "한국은 추락사고 사망률이 높아 2m 이상 작업에 극도로 엄격한 반면, 베트남 현장은 상대적으로 느슨한 경우가 많아 베트남 근로자가 '2m 정도는 괜찮다'고 생각할 위험이 있음. 통역 시 '2m는 사람 키 1.5배 정도로 매우 위험'하며 한국 법상 절대 기준임을 강조하고, 추락 시 사망 또는 중상 가능성이 높다는 점을 구체적 사례와 함께 설명해야 경각심 형성.",
        "commonMistakes": [
            {
                "mistake": "Ngăn chặn vật rơi (낙하물방지로 오역)",
                "correction": "Chống rơi ngã (사람 추락방지)",
                "explanation": "'Vật rơi'는 물건 낙하, 'Rơi ngã'는 사람 추락으로 안전장비와 대응이 완전히 다름"
            },
            {
                "mistake": "'2m 이상'을 '높은 곳'으로 애매하게 통역",
                "correction": "2m 이상 (Từ 2m trở lên) 명시",
                "explanation": "한국 법은 2m를 절대 기준으로 하므로 구체적 수치 통역 필수"
            },
            {
                "mistake": "추락방지를 '조심하면 됨'으로 안내",
                "correction": "난간 또는 안전대 착용 의무 명시",
                "explanation": "추락방지는 개인 주의가 아니라 법적 의무 조치이므로 구체적 장비·시설 설치 기준 통역 필요"
            }
        ],
        "examples": [
            {
                "ko": "2m 이상 높이에서 작업 시 추락방지 조치 없이 작업할 수 없습니다.",
                "vi": "Khi làm việc trên độ cao từ 2m trở lên, không được phép làm việc mà không có biện pháp chống rơi ngã.",
                "situation": "formal"
            },
            {
                "ko": "추락방지를 위해 난간을 설치하거나 안전대를 착용하세요.",
                "vi": "Để chống rơi ngã, phải lắp lan can hoặc đeo dây an toàn.",
                "situation": "onsite"
            },
            {
                "ko": "추락사고는 건설 현장 사망사고 1위이므로 절대 주의하세요.",
                "vi": "Tai nạn rơi ngã là nguyên nhân tử vong hàng đầu tại công trường xây dựng, tuyệt đối phải cẩn thận.",
                "situation": "formal"
            }
        ],
        "relatedTerms": ["안전벨트", "안전모", "낙하물방지망", "고소작업"]
    },
    {
        "slug": "tbm-hop-cong-cu",
        "korean": "TBM",
        "vietnamese": "TBM (Họp công cụ)",
        "hanja": None,
        "hanjaReading": None,
        "pronunciation": "티비엠",
        "meaningKo": "Tool Box Meeting의 약자로, 작업 시작 전 현장에서 10~15분간 진행하는 안전 미팅. 통역 시 '공구함 회의'로 직역하지 말고 '작업 전 안전 미팅' 또는 '조회'로 설명해야 이해가 빠르며, 한국 현장에서는 매일 아침 또는 위험 작업 전 의무적으로 실시함을 명확히 해야 함. TBM에서는 당일 작업 내용, 위험 요소, 안전 수칙, 날씨·장비 점검 사항을 공유하고 작업자 전원이 서명하므로, 베트남 근로자에게 '형식적 참석이 아니라 실제 위험 파악과 질문 시간'임을 통역해야 참여도 향상. TBM 불참 시 작업 배제 가능하므로 지각 금지 및 참석 의무를 강조해야 함.",
        "meaningVi": "Viết tắt của Tool Box Meeting, là cuộc họp an toàn ngắn 10~15 phút trước khi bắt đầu ca làm tại công trường. Tại Hàn Quốc, TBM là bắt buộc hàng ngày hoặc trước công việc nguy hiểm, nội dung bao gồm công việc trong ngày, yếu tố rủi ro, quy tắc an toàn, kiểm tra thời tiết và thiết bị, toàn bộ công nhân phải ký tên. Nếu vắng mặt TBM có thể bị loại khỏi ca làm.",
        "context": "작업 시작 전, 안전교육, 일일 조회",
        "culturalNote": "한국 건설 현장은 TBM을 법적 의무로 간주하여 기록을 남기고 감독기관 점검 시 확인하지만, 베트남 현장은 상대적으로 덜 엄격한 경우가 많음. 베트남 근로자는 TBM을 '형식적 회의'로 여기거나 졸거나 딴짓하는 경우가 있으나, 한국 감독관은 이를 매우 부정적으로 보므로 통역 시 'TBM 중 휴대폰 사용 금지, 졸지 말 것, 질문 있으면 반드시 하라'는 구체적 행동 지침을 전달해야 현장 평가 개선.",
        "commonMistakes": [
            {
                "mistake": "Họp hộp công cụ (공구함 회의로 직역)",
                "correction": "TBM / Họp an toàn trước ca (작업 전 안전 미팅)",
                "explanation": "'Tool Box'를 직역하면 의미 전달 실패, 베트남에서는 'Họp an toàn' 또는 'TBM'으로 통일"
            },
            {
                "mistake": "TBM을 선택 사항으로 안내",
                "correction": "매일 의무 참석, 불참 시 작업 배제 가능 명시",
                "explanation": "한국 현장은 TBM 불참 시 당일 작업 금지 조치 가능하므로 의무 사항 강조 필수"
            },
            {
                "mistake": "'들으면 됨'으로 안내",
                "correction": "서명 필수, 질문 권장, 휴대폰 사용 금지까지 통역",
                "explanation": "TBM은 단순 청취가 아니라 참여 확인(서명)과 쌍방향 소통이 목적"
            }
        ],
        "examples": [
            {
                "ko": "아침 8시 TBM에 반드시 참석하여 당일 작업 내용과 안전 수칙을 확인하세요.",
                "vi": "Bắt buộc phải tham gia TBM lúc 8h sáng để xác nhận nội dung công việc trong ngày và quy tắc an toàn.",
                "situation": "formal"
            },
            {
                "ko": "TBM 중에는 휴대폰을 사용하지 말고 집중해서 들으세요.",
                "vi": "Trong TBM, không được dùng điện thoại và phải tập trung lắng nghe.",
                "situation": "onsite"
            },
            {
                "ko": "위험 요소가 이해되지 않으면 TBM에서 꼭 질문하세요.",
                "vi": "Nếu không hiểu yếu tố rủi ro, nhất định phải hỏi trong TBM.",
                "situation": "informal"
            }
        ],
        "relatedTerms": ["안전교육", "작업지시서", "위험성평가", "안전점검"]
    },
    {
        "slug": "msds",
        "korean": "MSDS",
        "vietnamese": "MSDS (Phiếu dữ liệu an toàn)",
        "hanja": None,
        "hanjaReading": None,
        "pronunciation": "엠에스디에스",
        "meaningKo": "Material Safety Data Sheet의 약자로, 화학물질의 유해성·위험성, 응급조치, 취급·보관 방법 등을 기재한 안전보건자료. 통역 시 '물질안전보건자료'로 풀어 설명하거나 'MSDS'를 그대로 사용하되 베트남 근로자에게 '화학약품 사용 전 반드시 확인해야 하는 안전 설명서'라고 안내해야 이해가 빠름. 한국 현장은 MSDS를 작업장 내 비치 의무가 있으며, 화학물질 사용 전 MSDS 교육을 받지 않으면 작업 금지. 베트남 근로자는 MSDS를 형식적 문서로 여기는 경우가 많으나, 한국은 화학물질 누출·화재 시 MSDS 기준으로 대응하므로 '비상 시 행동 요령'까지 숙지하도록 통역해야 사고 예방.",
        "meaningVi": "Viết tắt của Material Safety Data Sheet, là tài liệu ghi rõ tính độc hại, nguy hiểm, biện pháp sơ cứu, cách xử lý và bảo quản hóa chất. Tại Hàn Quốc, bắt buộc phải có MSDS tại nơi làm việc và công nhân phải được đào tạo MSDS trước khi sử dụng hóa chất, không được làm việc nếu chưa được đào tạo. Khi có sự cố rò rỉ hoặc hỏa hoạn hóa chất, phải xử lý theo hướng dẫn MSDS.",
        "context": "화학물질 취급, 도장작업, 방수작업, 안전교육",
        "culturalNote": "한국은 화학물질 관리가 매우 엄격하여 MSDS 미비치 시 과태료 부과 및 작업중지 명령이 내려지지만, 베트남 현장은 MSDS를 형식적으로만 비치하는 경우가 많아 실제 활용도가 낮음. 베트남 근로자는 한글 MSDS를 읽지 못하는 경우가 많으므로 통역 시 '주요 위험 내용(인화성, 독성, 응급조치)은 그림 기호로도 표시되어 있으니 반드시 확인'하고, 베트남어 번역본 요청 가능 여부를 안내하면 안전도 향상.",
        "commonMistakes": [
            {
                "mistake": "Giấy an toàn vật liệu (직역)",
                "correction": "MSDS / Phiếu dữ liệu an toàn hóa chất",
                "explanation": "'Material Safety Data Sheet'를 직역하면 어색, 베트남에서도 'MSDS' 약자를 그대로 쓰거나 'Phiếu an toàn hóa chất'으로 통일"
            },
            {
                "mistake": "MSDS를 '참고 자료' 정도로 안내",
                "correction": "법적 의무 비치, 교육 필수, 미준수 시 작업 금지 명시",
                "explanation": "한국은 MSDS 미비치·미교육 시 과태료 및 작업중지 명령이므로 강제성 강조 필요"
            },
            {
                "mistake": "한글 MSDS만 제공하고 설명 생략",
                "correction": "베트남 근로자는 한글 미숙이므로 그림 기호 설명 또는 베트남어 번역본 요청 안내",
                "explanation": "베트남 근로자 다수는 한글 읽기 어려워 MSDS 내용 이해 못하면 사고 위험 증가"
            }
        ],
        "examples": [
            {
                "ko": "도료 사용 전 MSDS를 확인하여 환기 방법과 보호구 착용 기준을 숙지하세요.",
                "vi": "Trước khi sử dụng sơn, kiểm tra MSDS để nắm rõ cách thông gió và tiêu chuẩn đeo bảo hộ.",
                "situation": "formal"
            },
            {
                "ko": "화학물질 누출 시 MSDS에 명시된 응급조치 절차를 따르세요.",
                "vi": "Khi hóa chất bị rò rỉ, tuân theo quy trình sơ cứu ghi trong MSDS.",
                "situation": "onsite"
            },
            {
                "ko": "MSDS는 작업장 내 쉽게 볼 수 있는 곳에 비치해야 합니다.",
                "vi": "MSDS phải được bố trí tại nơi dễ thấy trong khu vực làm việc.",
                "situation": "formal"
            }
        ],
        "relatedTerms": ["화학물질", "유해물질", "안전보건자료", "개인보호구"]
    },
    {
        "slug": "khong-gian-kin",
        "korean": "밀폐공간",
        "vietnamese": "Không gian kín",
        "hanja": "密閉空間",
        "hanjaReading": "密(빽빽할 밀) + 閉(닫을 폐) + 空(빌 공) + 間(사이 간)",
        "pronunciation": "밀폐공간",
        "meaningKo": "환기가 불충분하여 산소 결핍, 유해가스 축적 등의 위험이 있는 장소(탱크, 맨홀, 터널, 피트 등). 통역 시 '밀폐공간'을 단순히 '닫힌 공간'으로 번역하지 말고, 산소 농도 18% 미만 또는 유해가스 노출 위험이 있는 공간임을 명확히 해야 하며, 한국 법상 밀폐공간 작업 시 관리감독자 배치, 산소·유해가스 측정, 환기, 감시인 배치가 의무임을 전달해야 함. 베트남 근로자는 밀폐공간 위험성을 과소평가하는 경우가 많으므로 '산소 부족으로 수 분 내 의식 잃고 사망 가능'하다는 구체적 위험을 설명하고, 작업 전 측정 결과 확인 및 작업 중 감시인과 소통 의무를 강조해야 사고 예방.",
        "meaningVi": "Nơi có thông gió không đủ, nguy cơ thiếu oxy hoặc tích tụ khí độc (bể chứa, cống rãnh, hầm, hố). Tại Hàn Quốc, bắt buộc phải có giám sát viên quản lý, đo nồng độ oxy và khí độc, thông gió, bố trí người giám sát khi làm việc trong không gian kín. Thiếu oxy có thể gây mất ý thức và tử vong trong vài phút, nên phải kiểm tra kết quả đo trước khi làm và giữ liên lạc với người giám sát trong suốt ca làm.",
        "context": "지하작업, 탱크 내부 작업, 맨홀 작업, 안전교육",
        "culturalNote": "한국은 밀폐공간 질식사고가 빈발하여 관련 규정이 극도로 엄격하지만, 베트남 현장은 상대적으로 느슨한 경우가 많아 베트남 근로자가 '좁은 곳이지만 괜찮다'고 판단할 위험이 있음. 통역 시 '밀폐공간은 눈에 보이지 않는 산소 부족·유해가스가 치명적'이며, 작업 전 산소·가스 측정 결과가 안전 범위 내일 때만 작업 가능하고, 작업 중에도 감시인이 상시 확인한다는 절차를 구체적으로 설명해야 경각심 형성.",
        "commonMistakes": [
            {
                "mistake": "Không gian đóng kín (단순히 닫힌 공간)",
                "correction": "Không gian kín / Không gian nguy hiểm thiếu oxy",
                "explanation": "'Đóng kín'은 물리적 밀폐만 표현, 밀폐공간은 산소 결핍·유해가스 위험을 포함하므로 'Không gian kín' 또는 'Không gian nguy hiểm'으로 통역"
            },
            {
                "mistake": "'좁은 곳'으로만 설명",
                "correction": "산소 부족·유해가스 위험 명시",
                "explanation": "밀폐공간의 핵심은 좁음이 아니라 환기 불량으로 인한 질식·중독 위험"
            },
            {
                "mistake": "측정 절차를 생략하고 바로 작업 지시",
                "correction": "산소·가스 측정 → 안전 확인 → 작업 허가 순서 통역",
                "explanation": "한국은 측정 결과 안전 범위 확인 없이 밀폐공간 작업 금지, 절차 누락 시 작업중지 명령"
            }
        ],
        "examples": [
            {
                "ko": "밀폐공간 작업 전 산소 농도와 유해가스 농도를 반드시 측정하세요.",
                "vi": "Trước khi làm việc trong không gian kín, bắt buộc phải đo nồng độ oxy và khí độc.",
                "situation": "formal"
            },
            {
                "ko": "밀폐공간 내부에 들어갈 때는 감시인과 무전기로 계속 연락하세요.",
                "vi": "Khi vào bên trong không gian kín, phải liên tục liên lạc với người giám sát qua bộ đàm.",
                "situation": "onsite"
            },
            {
                "ko": "산소 농도가 18% 미만이면 절대 작업하지 마세요.",
                "vi": "Nếu nồng độ oxy dưới 18%, tuyệt đối không được làm việc.",
                "situation": "formal"
            }
        ],
        "relatedTerms": ["산소결핍", "유해가스", "환기", "안전교육"]
    },
    {
        "slug": "bui",
        "korean": "분진",
        "vietnamese": "Bụi",
        "hanja": "粉塵",
        "hanjaReading": "粉(가루 분) + 塵(티끌 진)",
        "pronunciation": "분진",
        "meaningKo": "공기 중에 부유하는 미세한 고체 입자로, 건설 현장에서는 절단·연마·해체 작업 시 다량 발생하며 호흡기 질환 및 진폐증을 유발할 수 있음. 통역 시 '분진'과 '먼지'를 구분하여, 분진은 호흡기로 흡입 시 건강 피해를 일으키는 산업보건 용어임을 명확히 해야 하며, 한국 현장은 분진 발생 작업 시 방진 마스크(KF94 이상) 착용 의무와 작업장 살수·환기를 요구함을 전달해야 함. 베트남 근로자는 일반 마스크로 분진 작업을 하는 경우가 많으나, 한국 감독관은 방진 마스크 미착용 시 즉시 작업중지 명령을 내리므로 '일반 마스크는 분진 차단 효과 없음'을 강조하고, 장기 노출 시 폐 질환 위험을 구체적으로 설명해야 보호구 착용 독려 가능.",
        "meaningVi": "Hạt rắn mịn lơ lửng trong không khí, phát sinh nhiều khi cắt, mài, phá dỡ tại công trường, có thể gây bệnh đường hô hấp và bệnh phổi bụi. Tại Hàn Quốc, bắt buộc phải đeo khẩu trang chống bụi (KF94 trở lên) khi làm việc phát sinh bụi và phải tưới nước, thông gió. Khẩu trang thường không có tác dụng chống bụi, tiếp xúc lâu dài có thể gây bệnh phổi nghiêm trọng.",
        "context": "절단작업, 연마작업, 해체작업, 안전교육",
        "culturalNote": "한국은 분진 노출로 인한 진폐증·폐암 문제가 심각하여 방진 마스크 착용과 작업장 환기를 엄격히 요구하지만, 베트남 현장은 일반 마스크 착용이나 마스크 미착용 상태로 작업하는 경우가 많음. 베트남 근로자는 '마스크 착용이 불편하다'고 느끼거나 '단기 작업이라 괜찮다'고 생각할 수 있으나, 한국은 분진 작업 중 방진 마스크 미착용 시 즉시 작업중지 및 과태료 부과하므로 통역 시 '단 1시간 작업이라도 방진 마스크 필수'를 강조해야 함.",
        "commonMistakes": [
            {
                "mistake": "Bụi bặm (일반 먼지)",
                "correction": "Bụi (산업 분진)",
                "explanation": "'Bụi bặm'은 일상적 먼지, 건설 현장 분진은 'Bụi' 또는 'Bụi công nghiệp'로 구분하여 건강 위해성 강조"
            },
            {
                "mistake": "일반 마스크 착용으로 안내",
                "correction": "방진 마스크(KF94 이상) 착용 의무 명시",
                "explanation": "일반 마스크는 분진 차단 효과 거의 없으며 한국 현장은 방진 마스크 미착용 시 작업 금지"
            },
            {
                "mistake": "'짧은 작업이라 괜찮다'고 안내",
                "correction": "작업 시간 무관하게 분진 발생 작업은 무조건 방진 마스크 착용",
                "explanation": "한국 법은 분진 발생 작업 시 작업 시간과 무관하게 보호구 착용 의무"
            }
        ],
        "examples": [
            {
                "ko": "콘크리트 절단 시 분진이 많이 발생하므로 KF94 이상 방진 마스크를 착용하세요.",
                "vi": "Khi cắt bê tông phát sinh nhiều bụi, phải đeo khẩu trang chống bụi KF94 trở lên.",
                "situation": "onsite"
            },
            {
                "ko": "분진 작업 구역에는 살수 장치를 가동하여 분진 발생을 억제하세요.",
                "vi": "Tại khu vực làm việc có bụi, phải vận hành thiết bị tưới nước để giảm phát sinh bụi.",
                "situation": "formal"
            },
            {
                "ko": "일반 마스크는 분진 차단 효과가 없으니 반드시 방진 마스크를 쓰세요.",
                "vi": "Khẩu trang thường không có tác dụng chống bụi, nhất định phải đeo khẩu trang chống bụi.",
                "situation": "onsite"
            }
        ],
        "relatedTerms": ["방진마스크", "호흡기보호구", "환기", "살수"]
    },
    {
        "slug": "do-tieng-on",
        "korean": "소음측정",
        "vietnamese": "Đo tiếng ồn",
        "hanja": "騷音測定",
        "hanjaReading": "騷(시끄러울 소) + 音(소리 음) + 測(잴 측) + 定(정할 정)",
        "pronunciation": "소음측정",
        "meaningKo": "작업장 소음 수준을 측정하여 근로자 청력 보호 및 소음성 난청 예방을 위한 조치를 결정하는 절차. 통역 시 '소음측정'을 단순 소리 크기 확인이 아니라 법적 의무 조치이며, 한국 현장은 85dB(데시벨) 이상 소음 발생 작업장에서 6개월마다 소음측정을 실시하고 귀마개·귀덮개 착용을 의무화함을 전달해야 함. 베트남 근로자는 소음에 익숙해져 '시끄러워도 괜찮다'고 느끼는 경우가 많으나, 한국은 소음성 난청을 직업병으로 인정하여 보상하므로 '장기 노출 시 청력 손실 영구적'이라는 점을 강조하고, 귀마개 착용 거부 시 작업 배제 가능함을 통역해야 보호구 착용 독려.",
        "meaningVi": "Quy trình đo mức độ tiếng ồn tại nơi làm việc để bảo vệ thính lực người lao động và ngăn ngừa điếc nghề nghiệp. Tại Hàn Quốc, bắt buộc phải đo tiếng ồn 6 tháng/lần tại nơi làm việc có tiếng ồn từ 85dB trở lên và bắt buộc đeo nút tai hoặc bịt tai. Tiếp xúc lâu dài với tiếng ồn cao có thể gây mất thính lực vĩnh viễn, được công nhận là bệnh nghề nghiệp tại Hàn Quốc.",
        "context": "건설기계 작업, 항타작업, 절단작업, 안전교육",
        "culturalNote": "한국은 소음성 난청을 직업병으로 인정하고 보상하며 소음측정과 청력검사를 정기적으로 실시하지만, 베트남 현장은 소음 관리가 상대적으로 느슨한 경우가 많음. 베트남 근로자는 '시끄러운 곳에서 일해도 익숙하다'거나 '귀마개가 불편하다'고 느낄 수 있으나, 한국 감독관은 소음 작업장에서 귀마개 미착용 시 즉시 작업중지 명령을 내리므로 통역 시 '소음 85dB 이상 = 귀마개 필수'를 명확히 하고, 소음성 난청은 치료 불가능한 영구 장애임을 강조해야 함.",
        "commonMistakes": [
            {
                "mistake": "Đo âm thanh (일반 소리 측정)",
                "correction": "Đo tiếng ồn / Đo độ ồn",
                "explanation": "'Âm thanh'는 일반 소리, 산업 소음은 'Tiếng ồn'으로 구분하여 건강 위해성 강조"
            },
            {
                "mistake": "'시끄럽다'는 표현만 통역",
                "correction": "85dB 이상, 귀마개 착용 의무, 청력 손실 위험 명시",
                "explanation": "소음측정은 주관적 느낌이 아니라 구체적 기준(85dB)과 법적 의무(보호구 착용) 전달 필요"
            },
            {
                "mistake": "'익숙해지면 괜찮다'고 안내",
                "correction": "익숙함과 무관하게 청력 손상 진행, 영구적 장애 강조",
                "explanation": "소음 적응은 청력 보호와 무관하며, 장기 노출 시 치료 불가능한 난청 발생"
            }
        ],
        "examples": [
            {
                "ko": "이번 주 금요일에 소음측정을 실시하니 해당 구역 작업자는 협조해 주세요.",
                "vi": "Thứ Sáu tuần này sẽ tiến hành đo tiếng ồn, công nhân khu vực đó vui lòng hợp tác.",
                "situation": "formal"
            },
            {
                "ko": "소음 수준이 85dB을 초과하여 귀마개 착용이 의무입니다.",
                "vi": "Mức độ tiếng ồn vượt quá 85dB nên bắt buộc phải đeo nút tai.",
                "situation": "onsite"
            },
            {
                "ko": "소음성 난청은 치료가 불가능하므로 반드시 귀마개를 착용하세요.",
                "vi": "Điếc do tiếng ồn không thể chữa được, nhất định phải đeo nút tai.",
                "situation": "formal"
            }
        ],
        "relatedTerms": ["귀마개", "청력검사", "소음", "직업병"]
    },
    {
        "slug": "danh-gia-tac-dong-moi-truong",
        "korean": "환경영향평가",
        "vietnamese": "Đánh giá tác động môi trường",
        "hanja": "環境影響評價",
        "hanjaReading": "環(고리 환) + 境(지경 경) + 影(그림자 영) + 響(울릴 향) + 評(평할 평) + 價(값 가)",
        "pronunciation": "환경영향평가",
        "meaningKo": "개발사업이 환경에 미치는 영향을 사전에 조사·예측·평가하여 환경 보전 방안을 마련하는 제도. 통역 시 '환경영향평가'를 약어 '환평'으로 부르는 경우가 많으므로 베트남 근로자에게 '환평 = 환경영향평가'임을 설명하고, 한국은 일정 규모 이상 건설사업 시 환경영향평가를 법적으로 의무화하며 평가 결과에 따라 공사 방법·시기를 변경하거나 사업 자체가 중단될 수 있음을 전달해야 함. 베트남도 환경영향평가 제도가 있으나 한국보다 강제성이 약한 경우가 많아, 베트남 근로자는 '형식적 절차'로 여길 위험이 있으므로 통역 시 '환경영향평가 미이행 시 공사 중단 및 과태료'를 강조하고, 소음·분진·폐기물 관리 의무를 구체적으로 설명해야 현장 협조 유도.",
        "meaningVi": "Chế độ điều tra, dự đoán, đánh giá trước tác động của dự án phát triển đối với môi trường và lập phương án bảo vệ môi trường. Tại Hàn Quốc, đánh giá tác động môi trường (gọi tắt là '환평') là bắt buộc đối với dự án xây dựng quy mô nhất định, kết quả đánh giá có thể thay đổi phương pháp, thời gian thi công hoặc dừng dự án. Nếu không thực hiện đánh giá tác động môi trường, công trình có thể bị dừng và phạt tiền.",
        "context": "대형 건설사업, 환경 관련 인허가, 공사 착수 전 협의",
        "culturalNote": "한국은 환경 보호 의식이 높아 환경영향평가를 매우 엄격히 적용하며, 주민 의견 수렴 및 환경단체 감시도 활발하여 평가 결과에 따라 공사가 지연되거나 중단되는 경우가 많음. 베트남은 환경영향평가 제도가 있으나 한국만큼 강제성이 높지 않아 베트남 근로자는 '환경평가 = 형식적 서류'로 여기는 경향이 있음. 통역 시 '한국은 환경평가 미이행 시 공사 불가'를 명확히 하고, 소음·분진·폐기물 관리 의무와 주민 민원 대응의 중요성을 설명하면 현장 협조도 향상.",
        "commonMistakes": [
            {
                "mistake": "Đánh giá môi trường (환경평가로 축약)",
                "correction": "Đánh giá tác động môi trường (정식 명칭)",
                "explanation": "'Đánh giá môi trường'는 일반적이나 공식 용어는 'Đánh giá tác động môi trường'이며 법적 절차 강조 필요"
            },
            {
                "mistake": "'형식적 절차'로 안내",
                "correction": "법적 의무, 미이행 시 공사 중단 명시",
                "explanation": "한국은 환경영향평가 미이행 시 인허가 취소 및 과태료 부과하므로 강제성 강조 필수"
            },
            {
                "mistake": "'환평' 약어를 설명 없이 사용",
                "correction": "'환평 = 환경영향평가' 풀어서 설명",
                "explanation": "베트남 근로자는 한국 약어에 익숙하지 않아 오해 발생 가능"
            }
        ],
        "examples": [
            {
                "ko": "이 현장은 환경영향평가 결과에 따라 야간 공사가 제한됩니다.",
                "vi": "Công trường này bị hạn chế thi công ban đêm theo kết quả đánh giá tác động môi trường.",
                "situation": "formal"
            },
            {
                "ko": "환경영향평가 협의 중이므로 공사 착수 일정이 연기될 수 있습니다.",
                "vi": "Đang trong quá trình thỏa thuận đánh giá tác động môi trường nên lịch khởi công có thể bị hoãn.",
                "situation": "formal"
            },
            {
                "ko": "소음·분진 관리 기준을 초과하면 주민 민원으로 공사가 중단될 수 있어요.",
                "vi": "Nếu vượt tiêu chuẩn quản lý tiếng ồn, bụi có thể bị dân dân khiếu nại và dừng công trình.",
                "situation": "informal"
            }
        ],
        "relatedTerms": ["환경관리", "소음규제", "분진관리", "폐기물처리"]
    }
]

def main():
    # JSON 파일 읽기
    with open(file_path, 'r', encoding='utf-8') as f:
        data = json.load(f)

    print(f"현재 용어 수: {len(data)}개")

    # 신규 용어 추가
    data.extend(new_terms)

    print(f"추가 후 용어 수: {len(data)}개")
    print(f"추가된 용어: {len(new_terms)}개")

    # JSON 파일 저장 (한글 유지, 들여쓰기 2칸)
    with open(file_path, 'w', encoding='utf-8') as f:
        json.dump(data, f, ensure_ascii=False, indent=2)

    print(f"\n✅ {file_path} 업데이트 완료")
    print("\n추가된 용어 목록:")
    for i, term in enumerate(new_terms, 1):
        print(f"{i}. {term['korean']} ({term['vietnamese']})")

if __name__ == "__main__":
    main()
