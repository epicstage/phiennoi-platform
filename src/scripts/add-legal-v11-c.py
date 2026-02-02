import json
import os

# 파일 경로 설정
file_path = os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', 'data', 'terms', 'legal.json')

# 기존 데이터 로드
with open(file_path, 'r', encoding='utf-8') as f:
    data = json.load(f)

# 기존 slug 목록
existing_slugs = {t['slug'] for t in data}

# 신규 용어 10개 (가족법 심화 - 양육권/입양/후견)
new_terms = [
    {
        "slug": "quyen-nuoi-con",
        "korean": "양육권",
        "vietnamese": "Quyền nuôi con",
        "hanja": "養育權",
        "hanjaReading": "양(기를 양) + 육(기를 육) + 권(권리 권)",
        "pronunciation": "꾸엔 누어이 콘",
        "meaningKo": "이혼 시 미성년 자녀를 양육할 권리와 의무를 말합니다. 통역 시 '친권'과 혼동하지 않도록 주의해야 하며, 한국에서는 양육권과 친권을 분리할 수 있지만 베트남은 대부분 함께 인정됩니다. 양육권 결정 시 '자녀의 복리'가 최우선이며, 면접교섭권, 양육비 지급 등이 함께 결정됩니다. 베트남에서는 'quyền nuôi con'(양육권) 외에 'quyền thăm nom'(면접교섭권), 'tiền nuôi con'(양육비) 등의 용어를 정확히 구분해야 하며, 한국과 베트남의 양육권 판단 기준이 다르므로 국제결혼 이혼 사건에서 특히 주의가 필요합니다.",
        "meaningVi": "Quyền và nghĩa vụ chăm sóc, nuôi dưỡng con chưa thành niên sau khi ly hôn. Tòa án quyết định dựa trên lợi ích tốt nhất của trẻ, xét tuổi tác, điều kiện kinh tế, khả năng chăm sóc của cha mẹ. Bên có quyền nuôi con sẽ trực tiếp chăm sóc, bên kia có nghĩa vụ trả tiền nuôi con và quyền thăm nom.",
        "context": "이혼 소송, 친권 분쟁, 면접교섭권 신청, 양육비 청구 등 가족법 사건에서 핵심 쟁점이 되며, 자녀의 나이와 의견을 중요하게 고려합니다.",
        "culturalNote": "한국은 이혼 시 양육권과 친권을 분리할 수 있어 한쪽이 양육권, 다른 쪽이 친권을 가질 수 있지만, 베트남은 대부분 양육권자가 친권도 함께 갖습니다. 한국에서는 '자녀의 복리'를 최우선으로 하여 양육권을 결정하지만, 베트남은 여전히 어머니 우선 원칙이 강하며 특히 어린 자녀(7세 미만)는 거의 어머니에게 양육권이 주어집니다. 한국은 면접교섭권이 법적으로 명확히 보장되지만, 베트남은 실무상 양육권자가 거부하면 강제하기 어렵습니다. 국제결혼 이혼 시 헤이그협약(아동 탈취) 문제도 발생할 수 있으므로 통역 시 각별한 주의가 필요합니다.",
        "commonMistakes": [
            {
                "mistake": "양육권과 친권을 같은 것으로 통역",
                "correction": "양육권: quyền nuôi con, 친권: quyền làm cha mẹ",
                "explanation": "양육권은 실제 양육, 친권은 법적 대리권으로 구분됩니다."
            },
            {
                "mistake": "'면접교섭권'을 '방문권'으로 단순화",
                "correction": "quyền thăm nom con (자녀 방문 및 교류권)",
                "explanation": "단순 방문이 아니라 교류할 권리를 포함합니다."
            },
            {
                "mistake": "양육비를 '생활비'로 통역",
                "correction": "tiền nuôi con (양육비), tiền sinh hoạt (생활비)",
                "explanation": "자녀 양육 비용과 일반 생활비를 구분해야 합니다."
            }
        ],
        "examples": [
            {
                "ko": "이혼 소송에서 양육권은 어머니에게, 친권은 공동으로 인정합니다.",
                "vi": "Trong vụ ly hôn, quyền nuôi con thuộc về mẹ, quyền làm cha mẹ thuộc về cả hai.",
                "situation": "formal"
            },
            {
                "ko": "양육권을 갖지 못한 아버지는 매주 토요일 면접교섭권을 행사할 수 있습니다.",
                "vi": "Người cha không có quyền nuôi con được quyền thăm nom con vào thứ bảy hàng tuần.",
                "situation": "formal"
            },
            {
                "ko": "양육비는 매월 100만원씩 자녀 명의 계좌로 입금해야 합니다.",
                "vi": "Tiền nuôi con là 100 vạn won mỗi tháng phải chuyển vào tài khoản của con.",
                "situation": "informal"
            }
        ],
        "relatedTerms": ["ly-hon", "quyen-lam-cha-me", "친권", "면접교섭권", "양육비"]
    },
    {
        "slug": "quyen-lam-cha-me",
        "korean": "친권",
        "vietnamese": "Quyền làm cha mẹ",
        "hanja": "親權",
        "hanjaReading": "친(친할 친) + 권(권리 권)",
        "pronunciation": "꾸엔 람 짜 메",
        "meaningKo": "부모가 미성년 자녀에 대해 갖는 법적 권리와 의무의 총칭으로, 신분 행위(학교 등록, 여권 발급 등)의 대리권을 포함합니다. 통역 시 '양육권'과 구분해야 하며, 친권은 법적 대리권, 양육권은 실제 양육 권한을 의미합니다. 한국에서는 이혼 시 친권과 양육권을 분리할 수 있지만, 베트남은 대부분 함께 인정됩니다. 친권 행사 사항으로는 '거소지정권', '징계권', '재산관리권', '법률행위 동의권' 등이 있으며, 베트남어로는 각각 'quyền chỉ định nơi ở', 'quyền kỷ luật', 'quyền quản lý tài sản', 'quyền đồng ý hành vi pháp lý'로 통역합니다.",
        "meaningVi": "Quyền và nghĩa vụ của cha mẹ đối với con chưa thành niên, bao gồm quyền đại diện pháp lý, quản lý tài sản, giáo dục, chăm sóc sức khỏe. Cha mẹ cùng thực hiện quyền làm cha mẹ, trừ trường hợp ly hôn hoặc tòa án tước quyền. Quyền làm cha mẹ kết thúc khi con thành niên (đủ 18 tuổi).",
        "context": "이혼 소송, 친권 상실 선고, 후견인 지정, 해외 이주 동의 등 미성년 자녀와 관련된 모든 법적 절차에서 필요하며, 국제결혼 가정에서 특히 중요합니다.",
        "culturalNote": "한국은 이혼 시 친권과 양육권을 분리하여 한쪽이 양육권, 양쪽이 공동 친권을 가질 수 있지만, 베트남은 실무상 양육권자가 친권도 독점하는 경우가 많습니다. 한국에서는 친권 남용 시 법원이 친권 상실 선고를 할 수 있지만, 베트남은 친권 제한 제도는 있으나 완전 상실은 드뭅니다. 베트남에서는 자녀가 해외 여행 시 양쪽 부모의 동의가 필요하며, 이혼 후에도 친권자의 동의서가 필요합니다. 한국의 '친권자 지정 청구'는 베트남어로 'yêu cầu chỉ định người thực hiện quyền làm cha mẹ'로 통역하며, 절차와 기준이 양국이 다르므로 주의가 필요합니다.",
        "commonMistakes": [
            {
                "mistake": "친권을 '부모 권리'로 단순 번역",
                "correction": "quyền làm cha mẹ (친권 전문 용어)",
                "explanation": "법률 용어는 정확한 베트남어 표현을 사용해야 합니다."
            },
            {
                "mistake": "친권과 양육권을 구분 없이 통역",
                "correction": "친권: quyền làm cha mẹ (법적 대리), 양육권: quyền nuôi con (실제 양육)",
                "explanation": "법적 대리권과 실제 양육 권한을 명확히 구분해야 합니다."
            },
            {
                "mistake": "'친권 상실'을 '부모 자격 박탈'로 오역",
                "correction": "tước quyền làm cha mẹ (친권 상실 법적 용어)",
                "explanation": "법원의 공식 결정 용어를 정확히 사용해야 합니다."
            }
        ],
        "examples": [
            {
                "ko": "이혼 후 친권은 어머니가, 양육권은 아버지가 갖기로 합의했습니다.",
                "vi": "Sau ly hôn, quyền làm cha mẹ thuộc về mẹ, quyền nuôi con thuộc về cha theo thỏa thuận.",
                "situation": "formal"
            },
            {
                "ko": "아동 학대로 인해 법원이 친권 상실을 선고했습니다.",
                "vi": "Do bạo hành trẻ em, tòa án đã tuyên tước quyền làm cha mẹ.",
                "situation": "formal"
            },
            {
                "ko": "미성년 자녀의 여권 발급에는 친권자 양쪽의 동의가 필요합니다.",
                "vi": "Việc cấp hộ chiếu cho con chưa thành niên cần sự đồng ý của cả hai người thực hiện quyền làm cha mẹ.",
                "situation": "formal"
            }
        ],
        "relatedTerms": ["quyen-nuoi-con", "ly-hon", "양육권", "친권상실", "법정대리인"]
    },
    {
        "slug": "nuoi-con-nuoi",
        "korean": "입양",
        "vietnamese": "Nhận con nuôi",
        "hanja": "入養",
        "hanjaReading": "입(들 입) + 양(기를 양)",
        "pronunciation": "년 콘 누어이",
        "meaningKo": "혈연관계가 없는 사람 사이에 법률상 친자관계를 맺는 제도로, 국내입양과 국외입양으로 구분됩니다. 통역 시 '양자', '양녀', '양부모', '친생부모' 등의 용어를 정확히 구분해야 하며, 베트남어로는 'con nuôi'(양자녀), 'cha mẹ nuôi'(양부모), 'cha mẹ đẻ'(친생부모)로 번역합니다. 한국은 '친양자 입양'과 '일반 입양'을 구분하지만, 베트남은 'nhận con nuôi có xóa cha mẹ đẻ'(친생부모 기록 삭제형)와 'nhận con nuôi không xóa cha mẹ đẻ'(기록 유지형)로 구분됩니다. 국제입양 시 헤이그협약, 비자 문제, 국적 취득 등 복잡한 법률 문제가 있으므로 통역 시 세심한 주의가 필요합니다.",
        "meaningVi": "Chế độ pháp lý thiết lập quan hệ cha con giữa người nhận con nuôi và người được nhận làm con nuôi. Có hai loại: nhận con nuôi có xóa cha mẹ đẻ (hoàn toàn như con ruột) và không xóa (vẫn ghi cha mẹ đẻ). Việt Nam ưu tiên nhận con nuôi trong nước, nhận con nuôi nước ngoài phải qua Bộ Tư pháp. Người nhận phải đủ điều kiện về tuổi, sức khỏe, kinh tế.",
        "context": "입양 허가 심판, 국제입양 절차, 입양아동 보호, 친생부모 찾기 등 가족법 분야에서 민감한 사안이며, 아동 복리가 최우선으로 고려됩니다.",
        "culturalNote": "한국은 과거 해외 입양이 많았으나 현재는 국내 입양을 장려하며, 입양 절차가 엄격하고 사후관리도 철저합니다. 베트남은 전통적으로 가족 내 입양(조카, 친척)이 많으며, 법적 입양보다 사실상의 양육 관계가 많습니다. 한국의 '친양자 입양'은 친생부모 기록을 완전히 삭제하지만, 베트남은 삭제 여부를 선택할 수 있습니다. 국제입양 시 한국은 헤이그협약 가입국이지만 베트남도 가입국이므로 양국 법률을 모두 준수해야 합니다. 베트남 고아원 아동의 한국 입양은 베트남 법무부(Bộ Tư pháp) 허가가 필수이며, 절차가 까다롭고 시간이 오래 걸립니다.",
        "commonMistakes": [
            {
                "mistake": "입양을 '아이 받기'로 직역",
                "correction": "nhận con nuôi (입양 법적 용어)",
                "explanation": "법률 용어는 정확한 표현을 사용해야 합니다."
            },
            {
                "mistake": "'친양자'와 '양자'를 구분 없이 통역",
                "correction": "친양자: con nuôi có xóa cha mẹ đẻ, 일반 양자: con nuôi không xóa",
                "explanation": "친생부모 기록 삭제 여부에 따라 구분해야 합니다."
            },
            {
                "mistake": "'친생부모'를 '진짜 부모'로 통역",
                "correction": "cha mẹ đẻ 또는 cha mẹ ruột (친생부모)",
                "explanation": "'cha mẹ đẻ'는 법적으로 인정되는 친생부모 용어입니다."
            }
        ],
        "examples": [
            {
                "ko": "친양자 입양 시 친생부모의 성과 본이 삭제되고 양부모의 성과 본으로 변경됩니다.",
                "vi": "Khi nhận con nuôi có xóa cha mẹ đẻ, họ và tên của cha mẹ đẻ bị xóa và đổi thành họ tên của cha mẹ nuôi.",
                "situation": "formal"
            },
            {
                "ko": "국제입양은 아동의 이익이 최우선이며, 국내 입양을 먼저 고려해야 합니다.",
                "vi": "Nhận con nuôi quốc tế phải ưu tiên lợi ích của trẻ và xem xét nhận con nuôi trong nước trước.",
                "situation": "formal"
            },
            {
                "ko": "입양 가정은 6개월마다 사후관리 방문을 받아야 합니다.",
                "vi": "Gia đình nhận con nuôi phải được thăm khám giám sát 6 tháng một lần.",
                "situation": "informal"
            }
        ],
        "relatedTerms": ["quyen-lam-cha-me", "친양자", "양부모", "친생부모", "국제입양"]
    },
    {
        "slug": "nguoi-giam-ho",
        "korean": "후견인",
        "vietnamese": "Người giám hộ",
        "hanja": "後見人",
        "hanjaReading": "후(뒤 후) + 견(볼 견) + 인(사람 인)",
        "pronunciation": "응으어이 잠 호",
        "meaningKo": "미성년자나 피성년후견인 등 스스로 법률행위를 할 수 없는 사람을 법적으로 대리하고 보호하는 사람입니다. 통역 시 '법정대리인', '보호자'와 구분해야 하며, 후견인은 법원이 선임하는 공식적인 법적 대리인입니다. 한국에서는 '미성년후견인', '성년후견인', '한정후견인', '특정후견인' 등으로 세분화되지만, 베트남은 'người giám hộ'(후견인) 하나로 통칭되는 경우가 많습니다. 후견인의 권한으로는 '신상 보호', '재산 관리', '법률행위 대리' 등이 있으며, 남용 시 법원이 후견인을 변경할 수 있습니다.",
        "meaningVi": "Người được tòa án chỉ định để đại diện pháp lý và bảo vệ quyền lợi của người chưa thành niên không có cha mẹ hoặc người lớn không có năng lực hành vi. Người giám hộ có quyền quản lý tài sản, đại diện pháp lý, chăm sóc người được giám hộ. Tòa án giám sát hoạt động giám hộ và có thể thay đổi người giám hộ nếu không đảm bảo lợi ích của người được giám hộ.",
        "context": "부모가 사망하거나 친권이 상실된 미성년자, 치매·정신질환 등으로 판단 능력이 없는 성인에 대해 법원이 후견인을 선임하며, 상속, 재산 관리, 의료 결정 등에서 중요합니다.",
        "culturalNote": "한국은 2013년 성년후견제도가 도입되어 '후견', '한정후견', '특정후견'으로 세분화되었지만, 베트남은 아직 단일한 '후견'(giám hộ) 제도만 있습니다. 한국에서는 후견인의 권한 남용을 방지하기 위해 법원의 감독이 엄격하지만, 베트남은 실무상 감독이 느슨한 편입니다. 한국은 후견인 후보자를 친족 외에 전문가(변호사, 사회복지사)도 선임할 수 있지만, 베트남은 대부분 가족 구성원이 후견인이 됩니다. 베트남에서는 후견인을 'người bảo trợ'(보호자)라고도 부르지만, 법적 정확성을 위해서는 'người giám hộ'를 사용해야 합니다.",
        "commonMistakes": [
            {
                "mistake": "후견인을 '보호자'로 단순 번역",
                "correction": "người giám hộ (법정 후견인), người bảo hộ (일반 보호자)",
                "explanation": "법원이 선임한 후견인과 일반 보호자를 구분해야 합니다."
            },
            {
                "mistake": "'성년후견인'과 '미성년후견인'을 구분 없이 통역",
                "correction": "미성년: giám hộ trẻ vị thành niên, 성년: giám hộ người lớn",
                "explanation": "피후견인의 연령대를 명확히 구분해야 합니다."
            },
            {
                "mistake": "'법정대리인'과 '후견인'을 혼동",
                "correction": "법정대리인: người đại diện theo pháp luật, 후견인: người giám hộ",
                "explanation": "법정대리인은 부모 포함, 후견인은 별도 선임입니다."
            }
        ],
        "examples": [
            {
                "ko": "부모가 사망한 미성년자에 대해 법원이 삼촌을 후견인으로 선임했습니다.",
                "vi": "Tòa án chỉ định chú là người giám hộ cho trẻ vị thành niên mất cha mẹ.",
                "situation": "formal"
            },
            {
                "ko": "치매 환자의 재산을 보호하기 위해 성년후견인 선임이 필요합니다.",
                "vi": "Cần chỉ định người giám hộ cho người mắc chứng mất trí để bảo vệ tài sản.",
                "situation": "formal"
            },
            {
                "ko": "후견인은 피후견인의 이익을 위해 성실히 임무를 수행해야 합니다.",
                "vi": "Người giám hộ phải thực hiện nhiệm vụ trung thực vì lợi ích của người được giám hộ.",
                "situation": "informal"
            }
        ],
        "relatedTerms": ["quyen-lam-cha-me", "성년후견", "법정대리인", "피후견인", "후견감독인"]
    },
    {
        "slug": "xin-thay-doi-ho-ten",
        "korean": "성명변경",
        "vietnamese": "Xin thay đổi họ tên",
        "hanja": "姓名變更",
        "hanjaReading": "성(성씨 성) + 명(이름 명) + 변(변할 변) + 경(고칠 경)",
        "pronunciation": "신 타이도이 호 텐",
        "meaningKo": "법원에 성(姓) 또는 이름(名)의 변경을 신청하여 허가받는 절차입니다. 통역 시 '개명'은 이름만 바꾸는 것이고, '성명변경'은 성과 이름 모두 바꿀 수 있음을 구분해야 합니다. 한국에서는 '성본 변경'(성과 본관 변경)은 매우 어렵고, 이름 변경은 '사회생활 불편', '개명 사주' 등의 사유로 가능하지만, 베트남은 비교적 자유롭게 이름을 바꿀 수 있습니다. 입양, 이혼, 국제결혼 등에서 성명변경이 자주 발생하므로 절차와 요건을 정확히 통역해야 합니다.",
        "meaningVi": "Thủ tục xin phép tòa án thay đổi họ hoặc tên. Ở Việt Nam, việc đổi tên tương đối dễ dàng nếu có lý do chính đáng (tên xấu, trùng tên, phong thủy). Đổi họ khó hơn, thường chỉ khi nhận con nuôi, ly hôn hoặc lý do đặc biệt. Cần nộp hồ sơ lên tòa án, sau khi được chấp thuận phải đăng ký dân cư và thay đổi các giấy tờ khác.",
        "context": "개명 신청, 입양 후 성 변경, 이혼 후 성 복구, 국제결혼 후 성 변경 등 신분 변경 절차에서 필요하며, 법원 허가가 필수입니다.",
        "culturalNote": "한국은 성(姓) 변경이 극히 어려우며 '입양', '성전환' 등 특별한 사유만 인정되지만, 베트남은 결혼·이혼 시 자유롭게 성을 선택할 수 있습니다. 한국에서는 이름 변경도 '사회생활 불편'을 입증해야 하고 횟수 제한(1~2회)이 있지만, 베트남은 상대적으로 자유롭습니다. 베트남 여성은 결혼 시 성을 바꾸지 않는 것이 일반적이지만, 한국 남성과 결혼한 경우 한국 성을 추가로 사용하기도 합니다(법적으로는 베트남 성 유지). 한국에서 베트남 이름을 한글로 표기할 때 발음 차이 문제가 있으며, 통역 시 정확한 발음 표기를 확인해야 합니다.",
        "commonMistakes": [
            {
                "mistake": "'개명'과 '성명변경'을 같은 것으로 통역",
                "correction": "개명: đổi tên (이름만), 성명변경: đổi họ tên (성+이름)",
                "explanation": "성 변경 포함 여부를 명확히 구분해야 합니다."
            },
            {
                "mistake": "'성본 변경'을 단순 '성 변경'으로 통역",
                "correction": "đổi họ và quán (성과 본관 변경)",
                "explanation": "한국의 성본 제도는 베트남에 없으므로 설명이 필요합니다."
            },
            {
                "mistake": "이름 변경 사유를 제대로 전달 안 함",
                "correction": "gây bất tiện trong sinh hoạt xã hội (사회생활 불편)",
                "explanation": "법원 허가 사유를 정확히 통역해야 합니다."
            }
        ],
        "examples": [
            {
                "ko": "사주에서 이름이 좋지 않다고 하여 개명을 신청했습니다.",
                "vi": "Xin đổi tên vì thầy bói nói tên không tốt cho vận mệnh.",
                "situation": "informal"
            },
            {
                "ko": "입양으로 인해 성본을 양부모의 성본으로 변경합니다.",
                "vi": "Do nhận con nuôi, đổi họ sang họ của cha mẹ nuôi.",
                "situation": "formal"
            },
            {
                "ko": "이혼 후 결혼 전 성으로 복구하는 것을 희망합니다.",
                "vi": "Sau ly hôn, mong muốn khôi phục lại họ trước khi kết hôn.",
                "situation": "formal"
            }
        ],
        "relatedTerms": ["nuoi-con-nuoi", "ly-hon", "개명", "성본", "호적정리"]
    },
    {
        "slug": "phan-chia-tai-san-ly-hon",
        "korean": "재산분할",
        "vietnamese": "Phân chia tài sản ly hôn",
        "hanja": "財產分割",
        "hanjaReading": "재(재물 재) + 산(재산 산) + 분(나눌 분) + 할(나눌 할)",
        "pronunciation": "판찌아 타이산 리혼",
        "meaningKo": "이혼 시 부부가 혼인 중 형성한 재산을 분할하는 제도로, 한국은 '기여도'를 고려하지만 대체로 5:5 분할이 원칙입니다. 통역 시 '공동재산', '특유재산', '기여도' 등의 개념을 정확히 구분해야 하며, 베트남어로는 'tài sản chung'(공동재산), 'tài sản riêng'(특유재산), 'mức độ đóng góp'(기여도)로 번역합니다. 베트남도 공동재산 제도가 있으나 한국과 범위와 분할 비율이 다르므로 국제결혼 이혼 시 특히 주의가 필요합니다. 부동산, 예금, 주식, 사업체 등 재산 유형별로 평가와 분할 방법이 다르므로 통역 시 세심한 주의가 필요합니다.",
        "meaningVi": "Chế độ chia tài sản chung của vợ chồng khi ly hôn. Ở Việt Nam, tài sản chung trong thời kỳ hôn nhân được chia đôi trừ khi có thỏa thuận khác. Tài sản riêng (được tặng cho, thừa kế, có trước khi kết hôn) không chia. Tòa án xét xét mức độ đóng góp của mỗi bên để chia công bằng, đặc biệt khi có con nhỏ.",
        "context": "이혼 소송, 재산분할 청구, 위자료 청구 등에서 핵심 쟁점이며, 혼인 기간, 기여도, 자녀 양육 등을 종합 고려하여 분할 비율을 결정합니다.",
        "culturalNote": "한국은 법적으로 재산분할 비율이 정해져 있지 않고 '기여도'를 따지지만 실무상 대부분 5:5 분할이며, 전업주부도 가사노동을 인정받아 동등 분할을 받습니다. 베트남도 원칙적으로 5:5 분할이나, 여성의 가사노동 기여도를 덜 인정하는 경향이 있으며 특히 농촌 지역에서는 남성이 더 많은 재산을 가져가는 경우가 많습니다. 한국은 혼인 중 취득한 모든 재산이 분할 대상이지만, 베트남은 '결혼 전 재산', '증여·상속 재산'은 분할 대상이 아닙니다. 국제결혼 이혼 시 양국에 재산이 분산되어 있으면 관할 법원과 준거법 문제가 복잡하므로 전문가 자문이 필수입니다.",
        "commonMistakes": [
            {
                "mistake": "재산분할과 위자료를 혼동",
                "correction": "재산분할: phân chia tài sản, 위자료: bồi thường tinh thần",
                "explanation": "재산 분할은 경제적 정산, 위자료는 정신적 손해 배상입니다."
            },
            {
                "mistake": "'공동재산'을 '같이 산 재산'으로 직역",
                "correction": "tài sản chung của vợ chồng (부부 공동재산)",
                "explanation": "법적 용어로 혼인 중 형성한 재산을 의미합니다."
            },
            {
                "mistake": "'기여도'를 설명 없이 통역",
                "correction": "mức độ đóng góp vào việc tạo lập tài sản (재산 형성 기여도)",
                "explanation": "기여도 개념을 구체적으로 설명해야 합니다."
            }
        ],
        "examples": [
            {
                "ko": "이혼 시 혼인 중 취득한 아파트는 재산분할 대상이지만, 결혼 전 소유한 주택은 제외됩니다.",
                "vi": "Khi ly hôn, căn hộ mua trong thời kỳ hôn nhân là đối tượng phân chia, nhưng nhà có trước khi kết hôn không được chia.",
                "situation": "formal"
            },
            {
                "ko": "아내가 전업주부로 가사노동에 기여했으므로 재산분할 비율은 5:5입니다.",
                "vi": "Vợ làm nội trợ toàn thời gian đóng góp công việc gia đình nên tỷ lệ chia tài sản là 5:5.",
                "situation": "formal"
            },
            {
                "ko": "재산분할 외에 정신적 손해에 대한 위자료를 별도로 청구합니다.",
                "vi": "Ngoài phân chia tài sản, còn yêu cầu bồi thường tinh thần riêng.",
                "situation": "informal"
            }
        ],
        "relatedTerms": ["ly-hon", "공동재산", "특유재산", "위자료", "기여도"]
    },
    {
        "slug": "tien-cap-duong-cho-vo-chong",
        "korean": "부양료",
        "vietnamese": "Tiền cấp dưỡng cho vợ/chồng",
        "hanja": "扶養料",
        "hanjaReading": "부(도울 부) + 양(기를 양) + 료(요금 료)",
        "pronunciation": "띠엔 깝즈엉 쪼 보/쫑",
        "meaningKo": "혼인 관계에 있거나 이혼 후 생활이 어려운 배우자에게 지급하는 생활비로, '양육비'와는 구분됩니다. 통역 시 '부양료'는 배우자에게, '양육비'는 자녀에게 지급하는 것임을 명확히 해야 하며, 베트남어로는 'tiền cấp dưỡng cho vợ/chồng'(부양료), 'tiền nuôi con'(양육비)으로 구분합니다. 한국에서는 이혼 시 '재산분할'과 별도로 '부양료'를 청구할 수 있으며, 배우자의 소득·재산·건강 상태를 고려하여 결정합니다. 베트남도 유사한 제도가 있으나 실무상 거의 인정되지 않는 편입니다.",
        "meaningVi": "Tiền hỗ trợ sinh hoạt cho vợ hoặc chồng trong thời kỳ hôn nhân hoặc sau ly hôn nếu một bên gặp khó khăn về kinh tế. Khác với tiền nuôi con, tiền cấp dưỡng là cho vợ/chồng. Tòa án xét xét thu nhập, tài sản, sức khỏe, tuổi tác của cả hai bên để quyết định mức và thời gian trả. Ở Việt Nam, chế độ này ít được áp dụng trong thực tế.",
        "context": "이혼 소송, 혼인비용 분담, 별거 중 생활비 청구 등에서 필요하며, 특히 경제력 차이가 큰 부부의 이혼 시 중요한 쟁점이 됩니다.",
        "culturalNote": "한국은 '부양료' 제도가 있으나 실무상 거의 인정되지 않고 대신 '재산분할'로 해결하는 경향이 있습니다. 부양료가 인정되는 경우는 배우자가 질병·고령 등으로 경제 활동이 불가능하거나, 재산분할만으로는 생계가 어려운 경우입니다. 베트남도 법적으로는 부양료 제도가 있으나 한국보다 더 인정률이 낮으며, 여성이 남편에게 부양료를 청구하기 어려운 사회 분위기가 있습니다. 한국에서는 '양육비'와 '부양료'를 명확히 구분하지만, 베트남에서는 실무상 혼용되는 경우가 많아 통역 시 주의가 필요합니다.",
        "commonMistakes": [
            {
                "mistake": "부양료와 양육비를 혼동",
                "correction": "부양료: tiền cấp dưỡng cho vợ/chồng, 양육비: tiền nuôi con",
                "explanation": "배우자와 자녀에 대한 지원을 명확히 구분해야 합니다."
            },
            {
                "mistake": "부양료를 '생활비'로 단순 번역",
                "correction": "tiền cấp dưỡng (법적 부양료), tiền sinh hoạt (일반 생활비)",
                "explanation": "법적 의무로서의 부양료와 일반 생활비를 구분해야 합니다."
            },
            {
                "mistake": "부양료와 재산분할을 같은 것으로 통역",
                "correction": "재산분할: phân chia tài sản (일시금), 부양료: tiền cấp dưỡng (정기금)",
                "explanation": "재산 정산과 생활비 지원을 구분해야 합니다."
            }
        ],
        "examples": [
            {
                "ko": "이혼 후 전업주부였던 아내가 취업할 때까지 3년간 월 100만원의 부양료를 지급합니다.",
                "vi": "Sau ly hôn, trả tiền cấp dưỡng 100 vạn won/tháng trong 3 năm cho vợ từng làm nội trợ cho đến khi tìm được việc.",
                "situation": "formal"
            },
            {
                "ko": "남편의 소득이 높고 아내가 질병으로 경제활동이 불가능하여 부양료를 청구합니다.",
                "vi": "Chồng có thu nhập cao và vợ không thể làm việc do bệnh tật nên yêu cầu tiền cấp dưỡng.",
                "situation": "formal"
            },
            {
                "ko": "부양료는 양육비와 별도로 청구할 수 있습니다.",
                "vi": "Tiền cấp dưỡng có thể yêu cầu riêng với tiền nuôi con.",
                "situation": "informal"
            }
        ],
        "relatedTerms": ["ly-hon", "phan-chia-tai-san-ly-hon", "양육비", "재산분할", "위자료"]
    },
    {
        "slug": "quyen-tham-nom-con",
        "korean": "면접교섭권",
        "vietnamese": "Quyền thăm nom con",
        "hanja": "面接交涉權",
        "hanjaReading": "면(얼굴 면) + 접(접할 접) + 교(사귈 교) + 섭(섭할 섭) + 권(권리 권)",
        "pronunciation": "꾸엔 탐 놈 콘",
        "meaningKo": "이혼 후 양육권을 갖지 못한 부모가 자녀를 만나고 교류할 수 있는 권리로, 자녀의 복리를 위해 보장됩니다. 통역 시 '방문권', '면회권' 등으로 불리기도 하지만 단순 방문이 아니라 자녀와의 정기적 교류를 포함하므로 'quyền thăm nom con'(자녀 방문 및 돌봄 권리)으로 번역합니다. 면접교섭의 방법(시간, 장소, 빈도 등)은 부모 합의 또는 법원 결정으로 정하며, 상대방이 거부 시 강제집행도 가능합니다. 베트남에서는 법적으로는 보장되나 실무상 양육권자가 거부하면 강제하기 어려운 경우가 많습니다.",
        "meaningVi": "Quyền của cha hoặc mẹ không có quyền nuôi con được gặp gỡ, liên lạc, chăm sóc con sau ly hôn. Quyền này được đảm bảo vì lợi ích của trẻ. Thời gian, địa điểm thăm nom do hai bên thỏa thuận hoặc tòa án quyết định. Bên có quyền nuôi con không được cản trở bên kia thực hiện quyền thăm nom trừ trường hợp ảnh hưởng xấu đến trẻ.",
        "context": "이혼 소송, 면접교섭 조정, 면접교섭 방해 금지 청구 등에서 중요하며, 자녀의 나이와 의사를 존중하여 구체적 방법을 정합니다.",
        "culturalNote": "한국은 면접교섭권이 법적으로 명확히 보장되며, 양육권자가 정당한 이유 없이 거부하면 과태료나 양육권 변경 사유가 될 수 있지만, 베트남은 법적으로는 있으나 실무상 강제력이 약해 양육권자가 거부하면 실현이 어렵습니다. 한국에서는 '숙박 면접교섭'(주말 1박, 방학 기간 등)도 인정되지만, 베트남은 대부분 단순 방문(몇 시간) 수준입니다. 국제결혼 이혼 시 한쪽 부모가 자녀를 데리고 본국으로 돌아가면 면접교섭이 사실상 불가능해지는 경우가 많으며, 헤이그협약(국제 아동 탈취)이 적용될 수 있으므로 통역 시 주의가 필요합니다. 베트남에서는 '방문'을 'thăm'으로 표현하는데, 법적 권리임을 강조하려면 'quyền thăm nom'을 사용해야 합니다.",
        "commonMistakes": [
            {
                "mistake": "면접교섭권을 '방문권'으로 단순화",
                "correction": "quyền thăm nom con (방문 및 돌봄 권리)",
                "explanation": "단순 방문이 아니라 교류·돌봄 권리를 포함합니다."
            },
            {
                "mistake": "'면접교섭 거부'를 단순 '만나주지 않음'으로 통역",
                "correction": "cản trở quyền thăm nom con (면접교섭 방해, 법적 문제)",
                "explanation": "법적 권리 침해임을 명확히 해야 합니다."
            },
            {
                "mistake": "면접교섭 방법을 구체적으로 통역 안 함",
                "correction": "매주 토요일 오후 2~5시, 공원에서 (cụ thể: thứ 7 hàng tuần 14h-17h, tại công viên)",
                "explanation": "시간·장소·빈도를 구체적으로 통역해야 합니다."
            }
        ],
        "examples": [
            {
                "ko": "이혼 후 아버지는 매주 토요일 오후 2시부터 5시까지 자녀와 면접교섭할 수 있습니다.",
                "vi": "Sau ly hôn, người cha được quyền thăm nom con từ 14h đến 17h thứ bảy hàng tuần.",
                "situation": "formal"
            },
            {
                "ko": "어머니가 정당한 이유 없이 면접교섭을 거부하면 양육권 변경 사유가 됩니다.",
                "vi": "Nếu người mẹ cản trở quyền thăm nom con không có lý do chính đáng thì có thể thay đổi quyền nuôi con.",
                "situation": "formal"
            },
            {
                "ko": "방학 기간에는 1주일간 숙박 면접교섭을 허가합니다.",
                "vi": "Trong kỳ nghỉ, cho phép thăm nom con có nghỉ lại 1 tuần.",
                "situation": "informal"
            }
        ],
        "relatedTerms": ["quyen-nuoi-con", "ly-hon", "양육권", "면접교섭", "헤이그협약"]
    },
    {
        "slug": "tien-bo-thuong-tinh-than",
        "korean": "위자료",
        "vietnamese": "Tiền bồi thường tinh thần",
        "hanja": "慰藉料",
        "hanjaReading": "위(위로할 위) + 자(도울 자) + 료(요금 료)",
        "pronunciation": "띠엔 보이투엉 띤탄",
        "meaningKo": "이혼 또는 혼인 파탄의 책임이 있는 배우자가 상대방에게 정신적 고통에 대해 배상하는 금액입니다. 통역 시 '재산분할', '부양료'와 명확히 구분해야 하며, 위자료는 귀책사유(외도, 폭행, 유기 등)가 있을 때만 인정됩니다. 베트남어로는 'tiền bồi thường tinh thần' 또는 'tiền đền bù thiệt hại tinh thần'으로 번역하며, 한국과 베트남 모두 위자료 제도가 있으나 인정 기준과 금액이 다릅니다. 위자료 산정 시 혼인 기간, 귀책 정도, 경제력, 자녀 유무 등을 종합 고려합니다.",
        "meaningVi": "Tiền bồi thường tổn thất tinh thần mà bên có lỗi trong việc ly hôn phải trả cho bên kia. Chỉ được công nhận khi có lỗi rõ ràng như ngoại tình, bạo hành, bỏ rơi gia đình. Khác với phân chia tài sản (quyền lợi kinh tế) và tiền cấp dưỡng (hỗ trợ sinh hoạt), tiền bồi thường tinh thần là bồi hoàn thiệt hại về mặt tinh thần. Mức bồi thường tùy thuộc thời gian hôn nhân, mức độ lỗi, điều kiện kinh tế.",
        "context": "이혼 소송에서 상대방의 외도, 폭행, 유기 등 귀책사유를 입증하여 청구하며, 재산분할과 별개로 인정됩니다.",
        "culturalNote": "한국은 위자료 제도가 확립되어 있으며 외도의 경우 통상 3천만~5천만원 수준이지만, 베트남은 위자료 금액이 훨씬 낮고(수천~수만 달러) 입증 기준도 엄격합니다. 한국에서는 '유책배우자'는 위자료를 청구할 수 없지만 재산분할은 청구할 수 있으나, 베트남은 유책배우자의 재산분할 비율도 줄어들 수 있습니다. 한국에서는 '제3자(외도 상대방)'에게도 위자료를 청구할 수 있지만, 베트남은 일반적으로 배우자에게만 청구합니다. 국제결혼 이혼 시 준거법(한국법 vs 베트남법)에 따라 위자료 인정 여부와 금액이 크게 달라지므로 통역 시 주의가 필요합니다.",
        "commonMistakes": [
            {
                "mistake": "위자료를 '위로금'으로 직역",
                "correction": "tiền bồi thường tinh thần (정신적 손해 배상)",
                "explanation": "법적 배상 책임이지 단순 위로가 아닙니다."
            },
            {
                "mistake": "위자료와 재산분할을 혼동",
                "correction": "위자료: bồi thường tinh thần, 재산분할: phân chia tài sản",
                "explanation": "정신적 손해 배상과 재산 정산을 구분해야 합니다."
            },
            {
                "mistake": "'귀책사유'를 설명 없이 통역",
                "correction": "lỗi dẫn đến ly hôn (이혼 원인 책임)",
                "explanation": "귀책사유가 무엇인지 구체적으로 설명해야 합니다."
            }
        ],
        "examples": [
            {
                "ko": "남편의 외도로 인한 정신적 고통에 대해 위자료 5천만원을 청구합니다.",
                "vi": "Yêu cầu bồi thường tinh thần 50 triệu won do tổn thất tinh thần từ việc chồng ngoại tình.",
                "situation": "formal"
            },
            {
                "ko": "위자료는 재산분할과 별도로 청구할 수 있으며, 혼인 파탄의 책임이 있는 쪽이 지급합니다.",
                "vi": "Tiền bồi thường tinh thần có thể yêu cầu riêng với phân chia tài sản, bên có lỗi gây ra ly hôn phải trả.",
                "situation": "formal"
            },
            {
                "ko": "외도 상대방에게도 위자료를 청구할 수 있습니다.",
                "vi": "Có thể yêu cầu bồi thường tinh thần từ người thứ ba (tình nhân).",
                "situation": "informal"
            }
        ],
        "relatedTerms": ["ly-hon", "phan-chia-tai-san-ly-hon", "재산분할", "귀책사유", "외도"]
    },
    {
        "slug": "thoa-thuan-ly-hon",
        "korean": "협의이혼",
        "vietnamese": "Ly hôn thỏa thuận",
        "hanja": "協議離婚",
        "hanjaReading": "협(화합할 협) + 의(의논할 의) + 이(떠날 이) + 혼(혼인할 혼)",
        "pronunciation": "리혼 토아투언",
        "meaningKo": "부부가 합의하여 법원의 이혼 확인을 받아 이혼하는 절차로, '재판이혼'과 구분됩니다. 통역 시 한국의 협의이혼은 법원의 '이혼숙려기간'(1~3개월)을 거쳐야 하며, 베트남의 'ly hôn thỏa thuận'도 법원 확인이 필요함을 전달해야 합니다. 협의이혼 시 '재산분할', '양육권', '양육비', '면접교섭권' 등을 미리 합의하여 이혼 합의서에 명시하는 것이 중요하며, 합의가 안 되면 재판이혼으로 전환됩니다. 베트남어로는 '이혼 합의서'를 'thỏa thuận ly hôn' 또는 'bản thỏa thuận ly hôn'이라고 합니다.",
        "meaningVi": "Ly hôn theo thỏa thuận của vợ chồng sau khi được tòa án xác nhận. Cả hai bên thống nhất về việc ly hôn và các vấn đề liên quan như phân chia tài sản, quyền nuôi con, tiền nuôi con, quyền thăm nom. Khác với ly hôn theo bản án (tòa quyết định), ly hôn thỏa thuận nhanh hơn và ít tốn kém hơn. Ở Hàn Quốc, phải có thời gian cân nhắc (1-3 tháng) trước khi tòa chấp thuận.",
        "context": "이혼 의사가 있는 부부가 분쟁 없이 원만히 이혼하려 할 때 선택하며, 재판이혼보다 시간과 비용이 절약됩니다.",
        "culturalNote": "한국은 협의이혼 시 법원에서 '이혼숙려기간'(미성년 자녀 있으면 3개월, 없으면 1개월)을 의무적으로 두지만, 베트남은 협의이혼 시 즉시 가능합니다(단, 법원 확인 필요). 한국에서는 협의이혼 시 '양육비 산정표'를 기준으로 양육비를 정하지만, 베트남은 당사자 합의로 자유롭게 정합니다. 한국은 협의이혼 후 공증이 필수가 아니지만, 재산분할 등은 공증을 권장하며, 베트남은 협의이혼도 법원에서 확인을 받아야 법적 효력이 있습니다. 국제결혼 이혼 시 한국에서 협의이혼하면 베트남에서도 신고해야 양국 모두에서 효력이 있으므로 통역 시 이를 안내해야 합니다.",
        "commonMistakes": [
            {
                "mistake": "협의이혼을 '합의서만 작성하면 끝'으로 오해",
                "correction": "법원의 이혼 확인 필수 (phải có xác nhận của tòa án)",
                "explanation": "한국과 베트남 모두 법원 절차가 필요합니다."
            },
            {
                "mistake": "'재판이혼'과 '협의이혼'의 차이를 설명 안 함",
                "correction": "협의: ly hôn thỏa thuận (합의), 재판: ly hôn theo bản án (판결)",
                "explanation": "합의 여부에 따른 절차 차이를 명확히 해야 합니다."
            },
            {
                "mistake": "이혼숙려기간을 '대기 기간'으로 단순 번역",
                "correction": "thời gian cân nhắc trước ly hôn (이혼 전 숙고 기간)",
                "explanation": "제도의 취지를 설명해야 합니다."
            }
        ],
        "examples": [
            {
                "ko": "협의이혼은 재판이혼보다 빠르고 비용이 적게 들지만, 법원의 이혼 확인은 받아야 합니다.",
                "vi": "Ly hôn thỏa thuận nhanh hơn và ít tốn kém hơn ly hôn theo bản án, nhưng vẫn phải được tòa án xác nhận.",
                "situation": "formal"
            },
            {
                "ko": "미성년 자녀가 있어서 3개월의 이혼숙려기간을 거쳐야 합니다.",
                "vi": "Do có con chưa thành niên nên phải trải qua thời gian cân nhắc 3 tháng trước khi ly hôn.",
                "situation": "formal"
            },
            {
                "ko": "협의이혼 시 재산분할과 양육권을 미리 합의하는 것이 좋습니다.",
                "vi": "Khi ly hôn thỏa thuận nên thống nhất trước về phân chia tài sản và quyền nuôi con.",
                "situation": "informal"
            }
        ],
        "relatedTerms": ["ly-hon", "재판이혼", "이혼숙려기간", "이혼합의서", "양육권"]
    }
]

# 기존 slug와 중복 제거
filtered_terms = [t for t in new_terms if t['slug'] not in existing_slugs]

# 데이터 추가
data.extend(filtered_terms)

# 저장
with open(file_path, 'w', encoding='utf-8') as f:
    json.dump(data, f, ensure_ascii=False, indent=2)

print(f"Added {len(filtered_terms)} terms. Total: {len(data)}")
