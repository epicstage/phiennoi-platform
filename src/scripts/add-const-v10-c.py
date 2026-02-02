#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
플랜트건설 전문용어 10개 추가 스크립트
Theme: Plant Construction/Industrial
Tier S Quality (90+ points)
"""

import json
import os

# CRITICAL: Use correct file path
file_path = os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', 'data', 'terms', 'construction.json')

# Load existing data (data is a LIST!)
with open(file_path, 'r', encoding='utf-8') as f:
    data = json.load(f)

# Get existing slugs to prevent duplicates
existing_slugs = {t['slug'] for t in data}

# New terms - Plant Construction theme
new_terms = [
    {
        "slug": "nha-may",
        "korean": "공장",
        "vietnamese": "nhà máy",
        "hanja": "工場",
        "hanjaReading": "工(장인 공) + 場(마당 장)",
        "pronunciation": "냐 마이",
        "meaningKo": "산업 생산을 위한 대규모 시설물. 통역 시 '플랜트(plant)'와 구분 필요 - 베트남어로 'nhà máy'는 일반 공장, 'nhà máy công nghiệp'은 대형 산업플랜트를 의미. 현장에서는 공정별로 세부 명칭 사용하므로 정유공장(nhà máy lọc dầu), 화학공장(nhà máy hóa chất) 등 구체적 표현이 필요. 베트nam에서는 외국인 투자 공장을 'xí nghiệp'로 부르기도 하니 맥락 파악이 중요.",
        "meaningVi": "Cơ sở sản xuất công nghiệp quy mô lớn với các thiết bị, máy móc chuyên dụng. Bao gồm nhà máy chế biến, nhà máy sản xuất, và các công trình công nghiệp phụ trợ. Khác với xưởng sản xuất nhỏ lẻ.",
        "context": "산업시설, 플랜트 건설, 제조업",
        "culturalNote": "한국에서는 '공장'과 '플랜트'를 규모와 복잡도로 구분하지만, 베트남에서는 'nhà máy'로 통칭하고 형용사로 구분(nhà máy lớn/nhỏ). 베트남 북부는 구소련식 용어 'xí nghiệp'을 쓰기도 함. 건설 현장에서 한국 발주처는 '플랜트'를 선호하나 베트남 근로자는 'nhà máy'로 이해하므로 통역 시 맥락 설명 필요.",
        "commonMistakes": [
            {
                "mistake": "모든 공장을 'nhà máy công nghiệp'으로 번역",
                "correction": "일반 공장은 'nhà máy', 대형 플랜트만 'nhà máy công nghiệp'",
                "explanation": "과도한 수식은 베트남 현장 근로자에게 혼란을 줌"
            },
            {
                "mistake": "'xí nghiệp'을 구식 표현으로 무시",
                "correction": "북부 지역에서는 여전히 사용되는 정식 용어로 인정",
                "explanation": "지역별 언어 차이를 존중해야 원활한 의사소통 가능"
            },
            {
                "mistake": "'plant'를 'cây'(나무)로 오역",
                "correction": "'nhà máy công nghiệp' 또는 'khu liên hợp công nghiệp'",
                "explanation": "영어 차용어를 직역하면 의미가 완전히 달라짐"
            }
        ],
        "examples": [
            {
                "ko": "이 공장은 일일 생산능력 500톤 규모입니다",
                "vi": "Nhà máy này có công suất sản xuất 500 tấn/ngày",
                "situation": "formal"
            },
            {
                "ko": "공장 건설은 내년 3월 완공 예정입니다",
                "vi": "Dự án xây dựng nhà máy dự kiến hoàn thành vào tháng 3 năm sau",
                "situation": "formal"
            },
            {
                "ko": "공장 가동 전에 안전교육 필수입니다",
                "vi": "Bắt buộc phải có đào tạo an toàn trước khi vận hành nhà máy",
                "situation": "onsite"
            }
        ],
        "relatedTerms": ["duong-ong-cong-nghiep", "he-thong-dieu-khien", "lo-hoi", "설비", "공정"]
    },
    {
        "slug": "duong-ong-cong-nghiep",
        "korean": "산업배관",
        "vietnamese": "đường ống công nghiệp",
        "hanja": "産業配管",
        "hanjaReading": "産(날 산) + 業(업 업) + 配(나눌 배) + 管(대롱 관)",
        "pronunciation": "두엉 옹 꽁 응이엡",
        "meaningKo": "플랜트 내에서 유체(액체, 기체, 증기)를 이송하는 배관 시스템. 통역 시 주의할 점은 재질과 규격을 정확히 구분해야 함 - 'ống thép'(강관), 'ống inox'(스테인리스관), 'ống nhựa'(플라스틱관) 등. 압력 등급도 중요하므로 'đường ống áp lực cao/thấp' 구분 필수. 베트남 현장에서는 배관 사이즈를 인치 단위로 많이 쓰지만, 공식 도면은 밀리미터 표기가 일반적이므로 혼동 주의.",
        "meaningVi": "Hệ thống ống dẫn chất lỏng, khí, hơi trong nhà máy công nghiệp. Bao gồm ống chính, ống nhánh, phụ kiện kết nối, van và thiết bị đo lường. Phân loại theo vật liệu, đường kính và áp suất vận hành.",
        "context": "플랜트 건설, 배관 공사, 설비",
        "culturalNote": "한국 건설현장은 KS 규격 기준이지만 베트남은 TCVN(베트남 표준) 또는 국제 규격(ASME, DIN) 혼용. 배관 색상 코드도 다름 - 한국은 증기관=주황색이지만 베트남은 빨간색 사용 지역도 있음. 용접사 자격도 양국이 달라서 통역 시 '한국산업인력공단 자격증'을 베트남에서 인정받는 절차 설명이 자주 필요함.",
        "commonMistakes": [
            {
                "mistake": "'배관'을 단순히 'ống'으로만 번역",
                "correction": "'đường ống công nghiệp' 또는 'hệ thống đường ống'",
                "explanation": "'ống'만 쓰면 일반 파이프로 오해, 산업용 배관 시스템 의미 불명확"
            },
            {
                "mistake": "인치와 밀리미터 단위 혼용 시 구분 없이 통역",
                "correction": "반드시 단위 명시 - 'inch' 또는 'mm'",
                "explanation": "배관 규격 오류는 대형 사고로 이어질 수 있음"
            },
            {
                "mistake": "'파이프라인'을 'đường ống dẫn dầu'로 한정",
                "correction": "산업배관은 'đường ống công nghiệp', 송유관만 'đường ống dẫn dầu'",
                "explanation": "배관 용도에 따라 명칭이 다름"
            }
        ],
        "examples": [
            {
                "ko": "산업배관 용접은 자격증 소지자만 가능합니다",
                "vi": "Chỉ người có chứng chỉ mới được hàn đường ống công nghiệp",
                "situation": "onsite"
            },
            {
                "ko": "배관 압력시험 결과 이상 없습니다",
                "vi": "Kết quả thử áp lực đường ống không có bất thường",
                "situation": "formal"
            },
            {
                "ko": "6인치 배관으로 교체 작업 진행 중입니다",
                "vi": "Đang tiến hành thay thế bằng đường ống 6 inch",
                "situation": "onsite"
            }
        ],
        "relatedTerms": ["van-cong-nghiep", "be-chua", "lo-hoi", "용접", "압력시험"]
    },
    {
        "slug": "be-chua",
        "korean": "저장탱크",
        "vietnamese": "bể chứa",
        "hanja": "貯藏tank",
        "hanjaReading": "貯(쌓을 저) + 藏(감출 장)",
        "pronunciation": "베 쭈어",
        "meaningKo": "액체나 기체 원료를 보관하는 대형 용기. 통역 시 'tank'와 'vessel'을 구분해야 - 'bể chứa'는 저장탱크, 'bình chứa'는 소형 용기. 위험물 저장탱크는 'bể chứa hóa chất nguy hiểm'으로 명확히 표현 필요. 탱크 형태도 구분 - 원통형(hình trụ), 구형(hình cầu), 부유식 지붕(mái nổi) 등. 베트남 안전 규정상 위험물 탱크는 방유제(khu vực chứa tràn) 필수이므로 건설 시 이 부분 통역 중요.",
        "meaningVi": "Thiết bị chứa nguyên liệu lỏng hoặc khí trong nhà máy. Phân loại theo hình dạng: bể trụ đứng, bể nằm ngang, bể cầu. Theo vật liệu: bể thép, bể inox, bể composite. Cần có hệ thống thông gió, đo mức và thiết bị an toàn.",
        "context": "플랜트 설비, 위험물 저장, 석유화학",
        "culturalNote": "한국은 소방법에 따라 탱크 용량별로 안전거리 규정이 엄격하지만, 베트남은 TCVN 5507 기준으로 다소 차이 있음. 탱크 점검 주기도 달라서 한국 기업이 베트남 플랜트 운영 시 현지 법규 확인 필수. 베트남에서는 태풍 대비 탱크 고정(neo đậu bể) 기준이 중요하며, 중부 지역은 특히 강화된 기준 적용.",
        "commonMistakes": [
            {
                "mistake": "'탱크'를 모두 'bể'로 번역",
                "correction": "저장탱크는 'bể chứa', 압력용기는 'bình áp lực'",
                "explanation": "용기 종류에 따라 안전 기준이 다름"
            },
            {
                "mistake": "'저장'을 'lưu trữ'로 번역",
                "correction": "산업용은 'chứa', 문서 보관은 'lưu trữ'",
                "explanation": "'lưu trữ'는 주로 정보/문서 저장에 사용"
            },
            {
                "mistake": "탱크 용량 단위를 kL(킬로리터)로만 표현",
                "correction": "베트남은 'm³(mét khối)' 단위가 일반적",
                "explanation": "단위 환산 오류 방지 위해 현지 단위 사용"
            }
        ],
        "examples": [
            {
                "ko": "저장탱크 용량은 5,000킬로리터입니다",
                "vi": "Dung tích bể chứa là 5.000 mét khối",
                "situation": "formal"
            },
            {
                "ko": "탱크 내부 청소 전 가스 농도 측정 필수",
                "vi": "Bắt buộc đo nồng độ khí trước khi vệ sinh bên trong bể",
                "situation": "onsite"
            },
            {
                "ko": "부유식 지붕 탱크로 증발 손실 최소화",
                "vi": "Giảm thiểu tổn thất bốc hơi bằng bể có mái nổi",
                "situation": "formal"
            }
        ],
        "relatedTerms": ["duong-ong-cong-nghiep", "van-cong-nghiep", "dong-ho-do", "압력용기", "방유제"]
    },
    {
        "slug": "lo-hoi",
        "korean": "보일러",
        "vietnamese": "lò hơi",
        "hanja": None,
        "hanjaReading": None,
        "pronunciation": "로 허이",
        "meaningKo": "연료를 연소시켜 증기나 온수를 생산하는 장치. 통역 시 'boiler'를 그대로 쓰지 말고 'lò hơi'로 표현해야 베트남 근로자가 이해함. 보일러 종류도 구분 필요 - 수관식(lò hơi ống nước), 연관식(lò hơi ống khói), 관류식(lò hơi tuần hoàn). 압력 단위는 한국이 kg/cm²를 쓰지만 베트남은 bar 또는 MPa 선호. 안전 교육 시 보일러 폭발 사고(nổ lò hơi) 사례를 반드시 설명하므로 관련 용어 숙지 필요.",
        "meaningVi": "Thiết bị đốt nhiên liệu để tạo hơi nước hoặc nước nóng phục vụ sản xuất. Bao gồm buồng đốt, hệ thống ống dẫn, bơm cấp nước và thiết bị kiểm soát. Phân loại theo nhiên liệu: lò hơi dầu, lò hơi khí, lò hơi than, lò hơi sinh khối.",
        "context": "플랜트 설비, 에너지, 산업용 증기",
        "culturalNote": "한국은 에너지관리법상 보일러 운전은 자격증 필수이지만, 베트남은 소형 보일러(2톤/h 이하)는 무자격 운전 가능한 경우도 있음. 보일러 검사 주기도 달라서 한국 업체가 베트남 공장 운영 시 현지 규정 확인 필요. 베트남은 최근 환경 규제로 석탄 보일러(lò hơi than) 신설 제한되고 가스/바이오매스로 전환 추세.",
        "commonMistakes": [
            {
                "mistake": "'보일러'를 영어 그대로 'boiler'로 발음",
                "correction": "'lò hơi'로 번역해야 베트남 근로자 이해",
                "explanation": "현장에서 영어 용어는 의사소통 장애 유발"
            },
            {
                "mistake": "압력 단위 'kg/cm²'를 환산 없이 사용",
                "correction": "'bar' 또는 'MPa'로 환산 표기",
                "explanation": "베트남은 국제 단위계 사용"
            },
            {
                "mistake": "'증기'를 'khí'(기체)로 번역",
                "correction": "'hơi nước'(수증기)로 정확히 표현",
                "explanation": "'khí'는 일반 기체, 보일러는 수증기 생산"
            }
        ],
        "examples": [
            {
                "ko": "보일러 압력이 10kg/cm²를 초과하면 안전밸브 작동",
                "vi": "Khi áp suất lò hơi vượt 10 bar, van an toàn sẽ hoạt động",
                "situation": "onsite"
            },
            {
                "ko": "보일러 수질 관리 철저히 해야 스케일 방지됩니다",
                "vi": "Phải quản lý chất lượng nước lò hơi nghiêm ngặt để ngăn cặn bám",
                "situation": "formal"
            },
            {
                "ko": "가스 보일러로 교체하면 환경오염 줄어듭니다",
                "vi": "Thay bằng lò hơi khí sẽ giảm ô nhiễm môi trường",
                "situation": "formal"
            }
        ],
        "relatedTerms": ["be-chua", "bang-dieu-khien", "van-cong-nghiep", "증기", "압력"]
    },
    {
        "slug": "thap-lam-mat",
        "korean": "냉각탑",
        "vietnamese": "tháp làm mát",
        "hanja": "冷却塔",
        "hanjaReading": "冷(찰 냉) + 却(물리칠 각) + 塔(탑 탑)",
        "pronunciation": "탑 람 맛",
        "meaningKo": "공정에서 발생한 열을 대기로 방출하여 냉각수 온도를 낮추는 설비. 통역 시 냉각탑 종류 구분 필요 - 개방형(tháp mở), 밀폐형(tháp kín), 강제통풍(thông gió cưỡng bức), 자연통풍(thông gió tự nhiên). 베트남 남부 고온다습 기후에서는 냉각 효율이 북부보다 낮으므로 설계 시 이 점 반영. 레지오넬라균 방지 위해 냉각수 소독(khử trùng nước làm mát) 필수이며, 베트남 보건부 규정 준수 설명 자주 필요.",
        "meaningVi": "Thiết bị làm mát nước tuần hoàn bằng cách trao đổi nhiệt với không khí. Nước nóng từ quy trình sản xuất được phun xuống, tiếp xúc với không khí để giảm nhiệt độ. Phân loại: tháp gió tự nhiên, tháp gió cưỡng bức, tháp dòng ngược, tháp dòng chéo.",
        "context": "플랜트 설비, 냉각 시스템, 공조",
        "culturalNote": "한국은 냉각탑 소음 규제가 엄격하지만, 베트남은 산업단지 내 소음 기준이 상대적으로 느슨함. 단 주거지역 인접 시 민원 가능성 있어 사전 설명 필요. 베트남은 우기 시 냉각탑 물 보충(bổ sung nước) 용이하나 건기엔 수자원 확보가 중요 이슈. 냉각탑 청소 주기도 한국(월 1회)보다 베트남(분기 1회)이 긴 편.",
        "commonMistakes": [
            {
                "mistake": "'냉각탑'을 'tháp lạnh'로 번역",
                "correction": "'tháp làm mát'이 정확한 기술 용어",
                "explanation": "'tháp lạnh'는 비표준 표현"
            },
            {
                "mistake": "'쿨링타워'를 영어 발음 그대로 사용",
                "correction": "'tháp làm mát' 또는 'tháp giải nhiệt'",
                "explanation": "현장 근로자는 베트남어 용어만 이해"
            },
            {
                "mistake": "냉각수와 냉동수를 구분 없이 'nước làm mát'로 통칭",
                "correction": "냉각수는 'nước làm mát', 냉동수는 'nước lạnh'",
                "explanation": "용도와 온도 범위가 다름"
            }
        ],
        "examples": [
            {
                "ko": "냉각탑 충진재 교체 작업 예정입니다",
                "vi": "Dự kiến thay vật liệu đệm tháp làm mát",
                "situation": "onsite"
            },
            {
                "ko": "냉각수 온도가 설계치보다 5도 높습니다",
                "vi": "Nhiệt độ nước làm mát cao hơn thiết kế 5 độ",
                "situation": "formal"
            },
            {
                "ko": "냉각탑 팬 모터 과열로 정지했습니다",
                "vi": "Động cơ quạt tháp làm mát dừng do quá nhiệt",
                "situation": "onsite"
            }
        ],
        "relatedTerms": ["duong-ong-cong-nghiep", "may-nen-khi", "dong-ho-do", "냉각수", "순환펌프"]
    },
    {
        "slug": "he-thong-dieu-khien",
        "korean": "제어시스템",
        "vietnamese": "hệ thống điều khiển",
        "hanja": "制御system",
        "hanjaReading": "制(만들 제) + 御(어거할 어)",
        "pronunciation": "헤 통 지에우 키엔",
        "meaningKo": "플랜트의 온도, 압력, 유량 등을 자동으로 조절하는 시스템. 통역 시 DCS(Distributed Control System)는 'hệ thống điều khiển phân tán', PLC(Programmable Logic Controller)는 'bộ điều khiển logic lập trình'으로 구분. SCADA는 'hệ thống giám sát và thu thập dữ liệu'로 번역. 제어 모드도 구분 - 자동(tự động), 수동(thủ công), cascade(điều khiển tầng). 알람(cảnh báo)과 인터록(liên động bảo vệ)은 안전에 직결되므로 정확한 통역 필수.",
        "meaningVi": "Hệ thống tự động điều chỉnh các thông số vận hành như nhiệt độ, áp suất, lưu lượng trong nhà máy. Bao gồm cảm biến, bộ điều khiển, cơ cấu chấp hành và giao diện giám sát. Đảm bảo quy trình vận hành ổn định, an toàn và tiết kiệm năng lượng.",
        "context": "플랜트 자동화, 공정제어, 계측",
        "culturalNote": "한국은 제어시스템을 주로 Yokogawa, Honeywell 등 외국 제품 사용하지만 베트남은 중국산 저가 제품도 많이 쓰임. 매뉴얼이 중국어인 경우 통역 시 어려움. 제어실(phòng điều khiển) 출입 통제도 한국이 더 엄격하며, 베트남은 상대적으로 자유로운 편. 제어시스템 고장 시 한국은 즉시 수리/교체하지만 베트남은 수동 운전으로 버티는 경우 많아 안전 이슈 설명 중요.",
        "commonMistakes": [
            {
                "mistake": "'제어'와 '조절'을 구분 없이 'điều chỉnh'로 번역",
                "correction": "자동 제어는 'điều khiển tự động', 수동 조절은 'điều chỉnh'",
                "explanation": "제어는 시스템이, 조절은 사람이 하는 행위"
            },
            {
                "mistake": "PLC를 'máy điều khiển'로 단순화",
                "correction": "'bộ điều khiển logic lập trình' 또는 'PLC'",
                "explanation": "기술 용어는 정확성이 중요"
            },
            {
                "mistake": "알람과 인터록을 모두 'cảnh báo'로 번역",
                "correction": "알람은 'cảnh báo', 인터록은 'liên động bảo vệ'",
                "explanation": "기능이 다름 - 알람은 경고, 인터록은 자동 차단"
            }
        ],
        "examples": [
            {
                "ko": "제어시스템 점검 중이므로 수동 모드로 운전합니다",
                "vi": "Đang kiểm tra hệ thống điều khiển nên vận hành ở chế độ thủ công",
                "situation": "onsite"
            },
            {
                "ko": "압력이 설정치를 벗어나면 자동으로 차단됩니다",
                "vi": "Khi áp suất vượt giá trị đặt, hệ thống sẽ tự động ngắt",
                "situation": "formal"
            },
            {
                "ko": "DCS 화면에서 모든 공정을 모니터링 가능합니다",
                "vi": "Có thể giám sát toàn bộ quy trình trên màn hình DCS",
                "situation": "formal"
            }
        ],
        "relatedTerms": ["bang-dieu-khien", "dong-ho-do", "van-cong-nghiep", "센서", "PLC"]
    },
    {
        "slug": "van-cong-nghiep",
        "korean": "산업용밸브",
        "vietnamese": "van công nghiệp",
        "hanja": "産業用valve",
        "hanjaReading": "産(날 산) + 業(업 업) + 用(쓸 용)",
        "pronunciation": "반 꽁 응이엡",
        "meaningKo": "배관에서 유체의 흐름을 제어하는 장치. 통역 시 밸브 종류 정확히 구분 - 게이트밸브(van cổng), 글로브밸브(van địa cầu), 체크밸브(van một chiều), 볼밸브(van bi), 나비밸브(van bướm). 밸브 작동 방식도 구분 - 수동(van tay), 전동(van điện), 공압(van khí nén), 유압(van thủy lực). 안전밸브(van an toàn)는 과압 방지용으로 중요하며, 설정 압력(áp suất cài đặt) 수치 통역 시 오류 금물.",
        "meaningVi": "Thiết bị điều khiển dòng chảy chất lỏng, khí trong đường ống. Phân loại theo chức năng: van đóng/mở, van điều chỉnh lưu lượng, van giảm áp, van một chiều, van an toàn. Theo cấu tạo: van cổng, van bi, van bướm, van màng. Vật liệu chế tạo: gang, thép, inox, đồng, nhựa.",
        "context": "배관 시스템, 플랜트 설비, 유체 제어",
        "culturalNote": "한국은 밸브 규격을 KS로 통일하지만 베트남은 JIS, DIN, ANSI 혼용으로 혼란 가능. 밸브 핸들 회전 방향도 나라마다 다를 수 있어 현장 교육 시 주의 환기 필요. 베트남은 중국산 저가 밸브 사용이 많아 품질 이슈 발생 시 한국 기준 설명 필요. 밸브 색상 표시도 한국과 베트남이 달라서 통역 시 혼동 방지 위해 'van màu đỏ'처럼 색상 명시.",
        "commonMistakes": [
            {
                "mistake": "모든 밸브를 'van'으로만 번역",
                "correction": "밸브 종류에 따라 'van cổng', 'van bi', 'van bướm' 등 구체적 표현",
                "explanation": "밸브 종류마다 용도와 특성이 다름"
            },
            {
                "mistake": "'체크밸브'를 'van kiểm tra'로 번역",
                "correction": "'van một chiều'(일방향 밸브)",
                "explanation": "'kiểm tra'는 점검, 'một chiều'는 역류 방지 의미"
            },
            {
                "mistake": "밸브 사이즈를 센티미터로 환산",
                "correction": "인치 단위 그대로 사용 또는 'DN(đường kính danh nghĩa)' 표기",
                "explanation": "밸브 업계는 인치 또는 DN 단위가 국제 표준"
            }
        ],
        "examples": [
            {
                "ko": "이 볼밸브는 1/4회전으로 개폐 가능합니다",
                "vi": "Van bi này có thể đóng/mở bằng 1/4 vòng quay",
                "situation": "onsite"
            },
            {
                "ko": "안전밸브 설정 압력은 15bar입니다",
                "vi": "Áp suất cài đặt van an toàn là 15 bar",
                "situation": "formal"
            },
            {
                "ko": "체크밸브 역할은 역류 방지입니다",
                "vi": "Chức năng van một chiều là ngăn dòng chảy ngược",
                "situation": "formal"
            }
        ],
        "relatedTerms": ["duong-ong-cong-nghiep", "he-thong-dieu-khien", "be-chua", "압력", "유량"]
    },
    {
        "slug": "may-nen-khi",
        "korean": "공기압축기",
        "vietnamese": "máy nén khí",
        "hanja": "空氣壓縮機",
        "hanjaReading": "空(빌 공) + 氣(기운 기) + 壓(누를 압) + 縮(줄일 축) + 機(기계 기)",
        "pronunciation": "마이 넨 키",
        "meaningKo": "공기를 압축하여 고압 공기를 공급하는 설비. 통역 시 압축기 종류 구분 - 왕복동식(máy nén piston), 스크류식(máy nén trục vít), 터보식(máy nén ly tâm). 공기 압력은 한국이 kg/cm²를 쓰지만 베트남은 bar 단위 선호. 압축공기 품질 등급(cấp độ chất lượng khí nén)도 ISO 8573 기준으로 설명. 드라이어(máy sấy khí) 및 필터(lọc khí) 포함 여부 확인 필요.",
        "meaningVi": "Thiết bị nén không khí để tạo khí nén áp suất cao phục vụ sản xuất. Khí nén được dùng cho thiết bị khí nén, dụng cụ cầm tay, hệ thống điều khiển. Bao gồm đầu nén, động cơ, bình chứa khí, hệ thống làm mát và lọc khí. Phân loại: máy nén piston, máy nén trục vít, máy nén ly tâm.",
        "context": "공압 시스템, 플랜트 설비, 유틸리티",
        "culturalNote": "한국은 압축공기 품질 관리가 엄격하지만 베트남은 필터 교체 주기가 느슨한 편. 압축기 소음도 이슈인데 한국은 방음실(phòng cách âm) 필수지만 베트남은 야외 설치도 많음. 압축공기 누설(rò rỉ khí nén) 점검도 한국이 더 철저하며, 에너지 절감 관점 설명 시 베트남 현장의 관심도 높아짐.",
        "commonMistakes": [
            {
                "mistake": "'컴프레셔'를 영어 발음 그대로 사용",
                "correction": "'máy nén khí' 또는 'máy nén'",
                "explanation": "현장 근로자는 베트남어만 이해"
            },
            {
                "mistake": "압력 단위 'kg/cm²'를 환산 없이 사용",
                "correction": "'bar' 또는 'MPa'로 환산",
                "explanation": "베트남은 국제 단위계 사용"
            },
            {
                "mistake": "'공압'을 'áp suất không khí'로 번역",
                "correction": "'khí nén' 또는 'hệ thống khí nén'",
                "explanation": "'áp suất không khí'는 기압, 공압은 'khí nén'"
            }
        ],
        "examples": [
            {
                "ko": "공기압축기 오일 교환 주기는 2,000시간입니다",
                "vi": "Chu kỳ thay dầu máy nén khí là 2.000 giờ",
                "situation": "onsite"
            },
            {
                "ko": "압축공기 압력이 7bar로 떨어졌습니다",
                "vi": "Áp suất khí nén đã giảm xuống 7 bar",
                "situation": "onsite"
            },
            {
                "ko": "스크류 압축기가 왕복동식보다 효율 좋습니다",
                "vi": "Máy nén trục vít hiệu quả hơn máy nén piston",
                "situation": "formal"
            }
        ],
        "relatedTerms": ["he-thong-dieu-khien", "thap-lam-mat", "van-cong-nghiep", "공압", "드라이어"]
    },
    {
        "slug": "bang-dieu-khien",
        "korean": "제어반",
        "vietnamese": "bảng điều khiển",
        "hanja": "制御盤",
        "hanjaReading": "制(만들 제) + 御(어거할 어) + 盤(소반 반)",
        "pronunciation": "방 지에우 키엔",
        "meaningKo": "전기 및 제어 장치를 수납하고 기기를 조작하는 판넬. 통역 시 MCC(Motor Control Center)는 'tủ điều khiển động cơ', PLC 패널은 'tủ PLC', 배전반은 'tủ phân phối điện'으로 구분. 제어반 등급도 구분 - 옥내형(loại trong nhà), 옥외형(loại ngoài trời), 방폭형(loại chống nổ). 안전 거리 및 접지(nối đất) 규정 설명 시 베트남 전기 규정(TCVN) 기준 확인 필요.",
        "meaningVi": "Tủ chứa các thiết bị điện và điều khiển, có nút bấm, công tắc, đèn báo để vận hành thiết bị. Bao gồm aptomat, contactor, rơle, PLC, biến tần. Phân loại: tủ điều khiển động cơ, tủ phân phối điện, tủ điều khiển tự động. Vật liệu: tủ thép, tủ inox, tủ nhựa.",
        "context": "전기 설비, 플랜트 제어, 자동화",
        "culturalNote": "한국은 제어반 내부 배선을 매우 정리정돈하지만 베트남은 상대적으로 느슨한 편. 제어반 접지 기준도 다르며, 베트남은 접지봉 설치가 부실한 경우 많아 안전 교육 시 강조 필요. 제어반 방진/방습(chống bụi/ẩm) 등급도 한국이 더 엄격하며, 베트남 고온다습 환경에서는 IP54 이상 권장 설명 필요.",
        "commonMistakes": [
            {
                "mistake": "'제어반'을 'bảng điều khiển'로만 번역",
                "correction": "폐쇄형은 'tủ điều khiển', 개방형만 'bảng điều khiển'",
                "explanation": "한국은 대부분 폐쇄형 사용"
            },
            {
                "mistake": "'배전반'과 '제어반'을 구분 없이 'tủ điện'으로 통칭",
                "correction": "배전반은 'tủ phân phối điện', 제어반은 'tủ điều khiển'",
                "explanation": "용도가 다름 - 배전은 전력 분배, 제어는 기기 조작"
            },
            {
                "mistake": "IP 등급을 'cấp IP'로만 표현",
                "correction": "'Chỉ số phòng thủ IP'(방진방수 등급)",
                "explanation": "IP가 무엇의 약자인지 설명 필요"
            }
        ],
        "examples": [
            {
                "ko": "제어반 문 열 때는 전원 차단 후 열어야 합니다",
                "vi": "Khi mở cửa tủ điều khiển phải ngắt điện trước",
                "situation": "onsite"
            },
            {
                "ko": "제어반 내부 온도가 50도를 초과했습니다",
                "vi": "Nhiệt độ bên trong tủ điều khiển vượt 50 độ C",
                "situation": "onsite"
            },
            {
                "ko": "방폭형 제어반은 위험 구역에 설치합니다",
                "vi": "Tủ điều khiển chống nổ được lắp đặt ở khu vực nguy hiểm",
                "situation": "formal"
            }
        ],
        "relatedTerms": ["he-thong-dieu-khien", "dong-ho-do", "van-cong-nghiep", "PLC", "배전반"]
    },
    {
        "slug": "dong-ho-do",
        "korean": "계측기",
        "vietnamese": "đồng hồ đo",
        "hanja": "計測器",
        "hanjaReading": "計(셀 계) + 測(잴 측) + 器(그릇 기)",
        "pronunciation": "동 호 도",
        "meaningKo": "온도, 압력, 유량, 레벨 등을 측정하는 기기. 통역 시 계측기 종류 정확히 구분 - 압력계(đồng hồ đo áp suất), 온도계(nhiệt kế), 유량계(đồng hồ đo lưu lượng), 레벨계(đồng hồ đo mức). 아날로그(đồng hồ kim)와 디지털(đồng hồ số)도 구분. 정밀도 표현 시 '±1%'는 'sai số ±1%'로 번역. 계측기 교정(hiệu chuẩn) 주기도 중요하며, 베트남은 국가 교정 기관(Viet Instrumentation) 기준 설명 필요.",
        "meaningVi": "Thiết bị đo lường các thông số vận hành như nhiệt độ, áp suất, lưu lượng, mức chất lỏng. Bao gồm cảm biến, bộ chuyển đổi tín hiệu, màn hình hiển thị. Phân loại: đồng hồ cơ, đồng hồ điện tử, cảm biến thông minh. Dùng để giám sát, điều khiển quy trình sản xuất.",
        "context": "플랜트 계측, 공정 모니터링, 자동화",
        "culturalNote": "한국은 계측기 교정을 KOLAS 인증기관에서 필수로 받지만, 베트남은 교정 주기가 느슨하거나 자가 교정도 허용되는 경우 있음. 계측기 단위도 한국은 SI 단위 위주이나 베트남은 미국식 단위(psi, °F) 혼용 장비도 많아 확인 필요. 계측기 고장 시 한국은 즉시 교체하지만 베트남은 수리해서 쓰는 경향 강함.",
        "commonMistakes": [
            {
                "mistake": "'계측기'를 'máy đo'로 단순화",
                "correction": "패널형은 'đồng hồ đo', 휴대형은 'máy đo'",
                "explanation": "형태에 따라 명칭이 다름"
            },
            {
                "mistake": "모든 온도계를 'nhiệt kế'로 번역",
                "correction": "산업용은 'đồng hồ đo nhiệt độ', 일상용은 'nhiệt kế'",
                "explanation": "용도에 따라 구분"
            },
            {
                "mistake": "센서와 계측기를 구분 없이 'cảm biến'으로 통칭",
                "correction": "센서는 'cảm biến', 계측기는 'đồng hồ đo' 또는 'thiết bị đo'",
                "explanation": "센서는 감지부, 계측기는 전체 시스템"
            }
        ],
        "examples": [
            {
                "ko": "압력계 지침이 레드존에 들어가면 즉시 정지",
                "vi": "Khi kim đồng hồ áp suất vào vùng đỏ, phải dừng ngay",
                "situation": "onsite"
            },
            {
                "ko": "계측기 교정 유효기간이 만료되었습니다",
                "vi": "Đã hết hạn hiệu chuẩn đồng hồ đo",
                "situation": "formal"
            },
            {
                "ko": "디지털 유량계가 아날로그보다 정확합니다",
                "vi": "Đồng hồ đo lưu lượng số chính xác hơn đồng hồ kim",
                "situation": "formal"
            }
        ],
        "relatedTerms": ["he-thong-dieu-khien", "bang-dieu-khien", "van-cong-nghiep", "센서", "교정"]
    }
]

# Filter out duplicates
new_terms = [t for t in new_terms if t['slug'] not in existing_slugs]

if not new_terms:
    print("❌ All terms already exist. No new terms to add.")
else:
    # Extend data (data is a LIST)
    data.extend(new_terms)

    # Write back to file
    with open(file_path, 'w', encoding='utf-8') as f:
        json.dump(data, f, ensure_ascii=False, indent=2)

    print(f"✅ Added {len(new_terms)} plant construction terms to construction.json")
    print(f"📊 Total terms now: {len(data)}")
    print("\n📋 Added terms:")
    for term in new_terms:
        print(f"  - {term['slug']}: {term['korean']} / {term['vietnamese']}")
