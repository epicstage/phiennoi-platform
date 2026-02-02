#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""형사특별법 용어 추가 스크립트 (v6-b)"""

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
            "slug": "toi-pham-tinh-duc",
            "korean": "성범죄",
            "vietnamese": "Tội phạm tình dục",
            "hanja": "性犯罪",
            "hanjaReading": "性(성별 성) + 犯(범할 범) + 罪(허물 죄)",
            "pronunciation": "또이 팜 띤 쭉",
            "meaningKo": "성적 자기결정권을 침해하는 범죄로, 강간, 강제추행, 성희롱 등을 포괄하는 개념입니다. 통역 시 피해자의 2차 피해를 방지하기 위해 용어 선택에 각별히 주의해야 하며, 한국에서는 '성폭력', '성추행', '성희롱'을 명확히 구분하지만 베트남어에서는 문맥에 따라 표현이 달라질 수 있어 주의가 필요합니다. 법정 통역 시 피해자의 진술을 정확하게 전달하되 존중하는 태도를 유지해야 합니다.",
            "meaningVi": "Tội phạm xâm phạm quyền tự quyết tình dục, bao gồm hiếp dâm, cưỡng dâm, quấy rối tình dục. Trong thông dịch cần thận trọng để tránh gây tổn thương thứ cấp cho nạn nhân.",
            "context": "형사 재판, 경찰 조사, 피해자 상담",
            "culturalNote": "한국은 2012년 친고죄 폐지 이후 피해자 동의 없이도 기소 가능하지만, 베트nam은 여전히 일부 성범죄에서 피해자 고소가 필요합니다. 한국의 '성폭력처벌법'과 '아동청소년성보호법'은 베트남보다 처벌 범위가 넓고 엄격하며, 디지털 성범죄(몰카, 딥페이크)에 대한 법적 대응도 한국이 더 발달되어 있습니다. 통역 시 양국 법체계 차이를 인지하고 설명해야 합니다.",
            "commonMistakes": [
                {
                    "mistake": "Tội ác tình dục",
                    "correction": "Tội phạm tình dục",
                    "explanation": "'Tội ác'은 너무 강한 표현이며 법률 용어로는 'Tội phạm'이 적절합니다"
                },
                {
                    "mistake": "성범죄를 'Phạm tội tình dục'으로 번역",
                    "correction": "Tội phạm tình dục",
                    "explanation": "어순이 잘못되었으며, 'Tội phạm'이 명사로 앞에 와야 합니다"
                },
                {
                    "mistake": "모든 성범죄를 'Hiếp dâm'으로 통칭",
                    "correction": "범죄 유형에 따라 구분 (Hiếp dâm-강간, Quấy rối tình dục-성희롱, Cưỡng dâm-강제추행)",
                    "explanation": "성범죄는 다양한 유형이 있어 정확한 구분이 필수적입니다"
                }
            ],
            "examples": [
                {
                    "ko": "피고인은 성폭력범죄의처벌등에관한특례법 위반으로 기소되었습니다.",
                    "vi": "Bị cáo bị truy tố vi phạm Luật đặc lệ về xử phạt tội phạm bạo lực tình dục.",
                    "situation": "formal"
                },
                {
                    "ko": "성범죄 피해자는 신변보호와 심리상담을 받을 권리가 있습니다.",
                    "vi": "Nạn nhân tội phạm tình dục có quyền được bảo vệ thân thể và tư vấn tâm lý.",
                    "situation": "formal"
                },
                {
                    "ko": "현장에서 성범죄 증거물을 확보했습니다.",
                    "vi": "Đã thu thập được vật chứng tội phạm tình dục tại hiện trường.",
                    "situation": "onsite"
                }
            ],
            "relatedTerms": ["친고죄", "피해자", "성폭력특례법", "강간", "강제추행"]
        },
        {
            "slug": "ma-tuy",
            "korean": "마약",
            "vietnamese": "Ma túy",
            "hanja": "麻藥",
            "hanjaReading": "麻(삼 마) + 藥(약 약)",
            "pronunciation": "마 뚜이",
            "meaningKo": "중추신경계에 작용하여 정신적, 육체적 의존성을 일으키는 물질로, 대마, 아편, 향정신성의약품 등을 포함합니다. 통역 시 '마약', '향정신성의약품', '대마'를 명확히 구분해야 하며, 한국의 '마약류관리에관한법률'은 베트남보다 처벌이 엄격하여 소지만으로도 처벌됩니다. 법정 통역에서는 마약 종류, 중량, 투약 방법 등을 정확히 전달해야 하며, 베트남에서는 마약범죄에 대해 사형까지 가능하므로 중대성을 인지해야 합니다.",
            "meaningVi": "Chất gây nghiện tác động lên hệ thần kinh trung ương, gây phụ thuộc về tâm lý và thể chất. Bao gồm cần sa, thuốc phiện, chất hướng thần.",
            "context": "형사 재판, 세관 검사, 경찰 수사",
            "culturalNote": "베트남은 마약범죄에 대해 매우 엄격하여 일정량 이상 밀수 시 사형까지 선고 가능하며, 한국보다 처벌 수위가 훨씬 높습니다. 한국은 '마약류관리법'으로 마약, 향정신성의약품, 대마를 통합 관리하지만 베트남은 별도 법령으로 구분합니다. 양국 모두 마약범죄를 중대범죄로 보지만, 베트남은 재활보다 처벌 중심이고 한국은 최근 치료감호제도를 강화하는 추세입니다.",
            "commonMistakes": [
                {
                    "mistake": "Thuốc phiện만으로 모든 마약 지칭",
                    "correction": "Ma túy (총칭), Thuốc phiện (아편), Cần sa (대마), Chất hướng thần (향정신성)",
                    "explanation": "마약은 종류가 다양하므로 정확한 용어 사용이 필수입니다"
                },
                {
                    "mistake": "마약을 'Thuốc độc'으로 번역",
                    "correction": "Ma túy",
                    "explanation": "'Thuốc độc'은 독약을 의미하며 법률 용어로 부적절합니다"
                },
                {
                    "mistake": "대마를 일반 마약과 동일하게 취급",
                    "correction": "Cần sa로 구분하고 법적 분류 차이 설명",
                    "explanation": "대마는 별도 법률 분류이며 처벌 수위가 다릅니다"
                }
            ],
            "examples": [
                {
                    "ko": "피고인은 마약류관리에관한법률위반(향정)으로 구속되었습니다.",
                    "vi": "Bị cáo bị giam giữ vì vi phạm Luật quản lý ma túy (chất hướng thần).",
                    "situation": "formal"
                },
                {
                    "ko": "압수된 마약의 순도를 감정 의뢰했습니다.",
                    "vi": "Đã yêu cầu giám định độ tinh khiết của ma túy bị thu giữ.",
                    "situation": "onsite"
                },
                {
                    "ko": "마약 투약 혐의로 소변검사를 실시합니다.",
                    "vi": "Thực hiện xét nghiệm nước tiểu với nghi ngờ sử dụng ma túy.",
                    "situation": "onsite"
                }
            ],
            "relatedTerms": ["향정신성의약품", "대마", "밀수", "투약", "소지"]
        },
        {
            "slug": "to-chuc-toi-pham",
            "korean": "조직폭력",
            "vietnamese": "Tổ chức tội phạm",
            "hanja": "組織暴力",
            "hanjaReading": "組(모을 조) + 織(짤 직) + 暴(사나울 폭) + 力(힘 력)",
            "pronunciation": "또 쯕 또이 팜",
            "meaningKo": "3인 이상이 조직적으로 폭력행위를 하거나 범죄를 저지르는 집단을 의미하며, 한국의 '폭력행위등처벌에관한법률'에서 가중처벌 대상입니다. 통역 시 '조직폭력배', '폭력조직', '범죄조직'을 문맥에 따라 구분해야 하며, 베트남어에서는 'Băng nhóm tội phạm'과 'Tổ chức tội phạm'의 규모 차이를 인지해야 합니다. 법정에서는 조직 구성원의 역할(두목, 행동대장 등)을 정확히 전달하는 것이 중요하며, 한국 특유의 '조폭 문화' 용어를 베트남어로 설명할 때 주의가 필요합니다.",
            "meaningVi": "Nhóm từ 3 người trở lên có tổ chức thực hiện hành vi bạo lực hoặc phạm tội. Bị xử phạt nặng theo luật xử phạt hành vi bạo lực.",
            "context": "형사 재판, 경찰 수사, 검찰 조사",
            "culturalNote": "한국은 1990년대 '범죄와의 전쟁' 이후 조직폭력에 대한 단속이 강화되었고, '폭처법'으로 일반 폭력보다 가중처벌합니다. 베트남도 조직범죄를 엄격히 처벌하지만, 한국의 '조폭' 문화(계급, 의리, 조직 구조)는 베트남과 차이가 있어 통역 시 설명이 필요합니다. 한국은 조직 가입만으로도 처벌 가능하지만, 베트남은 실제 범죄 행위가 있어야 처벌됩니다.",
            "commonMistakes": [
                {
                    "mistake": "Bạo lực tổ chức",
                    "correction": "Tổ chức tội phạm hoặc Tổ chức bạo lực",
                    "explanation": "어순이 잘못되었으며, 명사가 먼저 와야 합니다"
                },
                {
                    "mistake": "모든 폭력 사건을 조직폭력으로 번역",
                    "correction": "3인 이상 조직적 범행만 'Tổ chức tội phạm'",
                    "explanation": "조직폭력은 조직성과 계획성이 있어야 성립합니다"
                },
                {
                    "mistake": "Băng đảng만 사용",
                    "correction": "규모에 따라 Băng nhóm (소규모) / Tổ chức tội phạm (대규모) 구분",
                    "explanation": "조직 규모와 체계성에 따라 용어를 달리 사용해야 합니다"
                }
            ],
            "examples": [
                {
                    "ko": "피고인들은 조직폭력배로서 상습적으로 폭행을 가했습니다.",
                    "vi": "Các bị cáo với tư cách thành viên tổ chức tội phạm đã thực hiện hành vi bạo hành thường xuyên.",
                    "situation": "formal"
                },
                {
                    "ko": "조직의 두목과 행동대장을 검거했습니다.",
                    "vi": "Đã bắt giữ đầu sỏ và chỉ huy hành động của tổ chức.",
                    "situation": "onsite"
                },
                {
                    "ko": "폭력조직 가입 및 활동 혐의로 기소되었습니다.",
                    "vi": "Bị truy tố với cáo buộc gia nhập và hoạt động trong tổ chức bạo lực.",
                    "situation": "formal"
                }
            ],
            "relatedTerms": ["폭처법", "상습범", "공갈", "협박", "폭행"]
        },
        {
            "slug": "khung-bo",
            "korean": "테러",
            "vietnamese": "Khủng bố",
            "hanja": None,
            "hanjaReading": None,
            "pronunciation": "쿵 보",
            "meaningKo": "정치적, 종교적, 사회적 목적을 달성하기 위해 불특정 다수에게 공포심을 조성하는 범죄행위로, 한국의 '국민보호와공공안전을위한테러방지법'으로 처벌됩니다. 통역 시 '테러', '테러예비음모', '테러자금조달'을 명확히 구분해야 하며, 국제 테러 관련 용어(ISIS, 알카에다 등)는 원어 발음 그대로 사용하는 것이 안전합니다. 국가안보 사안이므로 통역 시 기밀 유지가 중요하며, 베트남어에서 'Khủng bố'는 테러뿐 아니라 '공포' 일반을 의미할 수 있어 문맥 파악이 필수입니다.",
            "meaningVi": "Hành vi phạm tội nhằm gây ra nỗi sợ hãi cho đông đảo người dân để đạt mục đích chính trị, tôn giáo, xã hội. Bị xử phạt theo Luật phòng chống khủng bố.",
            "context": "국가안보 재판, 검찰 조사, 정보기관 조사",
            "culturalNote": "한국은 2016년 테러방지법 제정으로 테러 예비·음모 단계부터 처벌 가능하며, 정보기관의 감시 권한이 강화되었습니다. 베트남도 테러를 중대범죄로 보지만, 한국처럼 별도 테러방지법은 없고 형법으로 처리합니다. 9·11 이후 양국 모두 국제 테러 대응을 강화했으나, 한국은 북한 관련 테러 위협이 독특한 상황입니다. 통역 시 양국의 안보 상황 차이를 인지해야 합니다.",
            "commonMistakes": [
                {
                    "mistake": "Sợ hãi",
                    "correction": "Khủng bố (명사)",
                    "explanation": "'Sợ hãi'는 일반적인 공포를 의미하며, 테러 범죄는 'Khủng bố'를 사용해야 합니다"
                },
                {
                    "mistake": "테러를 'Tấn công'(공격)으로만 번역",
                    "correction": "Khủng bố",
                    "explanation": "테러는 단순 공격이 아니라 공포 조성 목적이 있는 범죄입니다"
                },
                {
                    "mistake": "테러예비음모를 'Âm mưu khủng bố'만 사용",
                    "correction": "Chuẩn bị và âm mưu khủng bố",
                    "explanation": "예비(준비)와 음모를 모두 포함해야 법률적으로 정확합니다"
                }
            ],
            "examples": [
                {
                    "ko": "피고인은 테러자금 조달 혐의로 구속되었습니다.",
                    "vi": "Bị cáo bị giam giữ với cáo buộc tài trợ vốn cho khủng bố.",
                    "situation": "formal"
                },
                {
                    "ko": "테러 예비 음모 혐의로 수사 중입니다.",
                    "vi": "Đang điều tra với nghi ngờ chuẩn bị và âm mưu khủng bố.",
                    "situation": "onsite"
                },
                {
                    "ko": "국제 테러 조직과의 연계 정황이 포착되었습니다.",
                    "vi": "Đã phát hiện dấu hiệu liên kết với tổ chức khủng bố quốc tế.",
                    "situation": "formal"
                }
            ],
            "relatedTerms": ["국가보안법", "간첩", "내란", "테러방지법", "테러자금"]
        },
        {
            "slug": "bao-luc-gia-dinh",
            "korean": "가정폭력",
            "vietnamese": "Bạo lực gia đình",
            "hanja": "家庭暴力",
            "hanjaReading": "家(집 가) + 庭(뜰 정) + 暴(사나울 폭) + 力(힘 력)",
            "pronunciation": "바오 릭 자 딘",
            "meaningKo": "가족 구성원 사이의 신체적, 정신적, 경제적 폭력을 의미하며, 한국의 '가정폭력범죄의처벌등에관한특례법'으로 일반 폭행보다 엄격히 처벌됩니다. 통역 시 피해자(주로 배우자, 아동)의 심리적 상태를 고려해 존중하는 태도가 필수이며, '신체적 폭력', '정서적 학대', '경제적 학대'를 명확히 구분해야 합니다. 한국은 가정보호사건으로 처리 가능하지만 베트남은 형사처벌이 원칙이므로, 법정 통역 시 절차 차이를 설명할 수 있어야 합니다.",
            "meaningVi": "Bạo lực về thể chất, tinh thần, kinh tế giữa các thành viên trong gia đình. Bị xử phạt nghiêm khắc theo Luật đặc lệ về xử phạt tội phạm bạo lực gia đình.",
            "context": "가정보호재판, 경찰 조사, 피해자 상담",
            "culturalNote": "한국은 2007년 가정폭력특례법 개정으로 피해자 보호가 강화되었고, 긴급임시조치(가해자 격리) 제도가 있습니다. 베트남도 2007년 가정폭력방지법을 제정했지만, 한국보다 집행력이 약하고 '가족 내 일'로 치부하는 문화가 남아있습니다. 한국은 상담조건부 기소유예, 보호처분 등 회복적 사법을 도입했지만, 베트남은 형사처벌 위주입니다. 통역 시 피해자가 '가족 창피'를 우려해 진술을 꺼리는 경우가 많아 세심한 배려가 필요합니다.",
            "commonMistakes": [
                {
                    "mistake": "Bạo hành gia đình",
                    "correction": "Bạo lực gia đình",
                    "explanation": "'Bạo hành'은 일반 폭행이고, 가정폭력은 'Bạo lực gia đình'이 공식 용어입니다"
                },
                {
                    "mistake": "신체 폭력만 가정폭력으로 인식",
                    "correction": "신체, 정서, 경제적 폭력 모두 포함 (Bạo lực thể chất, tinh thần, kinh tế)",
                    "explanation": "가정폭력은 다양한 형태가 있으며 모두 처벌 대상입니다"
                },
                {
                    "mistake": "가정폭력을 'Chuyện gia đình'(집안일)으로 축소",
                    "correction": "Tội phạm bạo lực gia đình (범죄)",
                    "explanation": "가정폭력은 범죄이며, 사적 영역으로 치부해서는 안 됩니다"
                }
            ],
            "examples": [
                {
                    "ko": "가정폭력 피해자 보호명령을 신청했습니다.",
                    "vi": "Đã đăng ký lệnh bảo vệ nạn nhân bạo lực gia đình.",
                    "situation": "formal"
                },
                {
                    "ko": "가해자에게 임시조치로 접근금지를 명령했습니다.",
                    "vi": "Đã ra lệnh cấm tiếp cận với người gia hại bằng biện pháp tạm thời.",
                    "situation": "formal"
                },
                {
                    "ko": "정서적 학대도 가정폭력에 해당됩니다.",
                    "vi": "Lạm dụng về mặt tinh thần cũng thuộc bạo lực gia đình.",
                    "situation": "informal"
                }
            ],
            "relatedTerms": ["보호명령", "임시조치", "피해자", "가해자", "접근금지"]
        },
        {
            "slug": "lam-dung-tre-em",
            "korean": "아동학대",
            "vietnamese": "Lạm dụng trẻ em",
            "hanja": "兒童虐待",
            "hanjaReading": "兒(어린아이 아) + 童(아이 동) + 虐(괴롭힐 학) + 待(대접 대)",
            "pronunciation": "람 중 째 엠",
            "meaningKo": "18세 미만 아동에게 가해지는 신체적, 정서적, 성적 학대 및 방임을 의미하며, 한국의 '아동학대범죄의처벌등에관한특례법'으로 엄격히 처벌됩니다. 통역 시 아동의 진술을 보호하고 2차 피해를 방지하는 것이 최우선이며, '신체학대', '정서학대', '성학대', '방임'을 명확히 구분해야 합니다. 한국은 아동학대 신고의무자 제도(교사, 의사 등)가 있고, 아동보호전문기관이 개입하는데 베트남과 시스템이 다르므로 절차 설명이 필요합니다. 법정에서는 아동의 연령, 인지 수준을 고려한 통역이 요구됩니다.",
            "meaningVi": "Lạm dụng về thể chất, tinh thần, tình dục và bỏ bê đối với trẻ dưới 18 tuổi. Bị xử phạt nghiêm khắc theo Luật đặc lệ về xử phạt tội phạm lạm dụng trẻ em.",
            "context": "형사 재판, 아동보호기관, 경찰 조사",
            "culturalNote": "한국은 2014년 아동학대특례법 제정으로 신고의무, 응급조치, 피해아동 보호가 체계화되었고, '아동학대범죄'로 가중처벌됩니다. 베트남도 아동보호법이 있지만 실효성이 한국보다 낮고, '훈육'과 '학대'의 경계가 모호한 경우가 많습니다. 한국은 체벌 금지가 명확하지만, 베트남은 문화적으로 체벌을 훈육으로 보는 경향이 남아있어 통역 시 주의가 필요합니다. 양국 모두 아동 최우선 원칙을 표방하지만 실제 보호 수준에는 차이가 있습니다.",
            "commonMistakes": [
                {
                    "mistake": "Ngược đãi trẻ em",
                    "correction": "Lạm dụng trẻ em",
                    "explanation": "'Ngược đãi'는 구어체이고, 법률 용어는 'Lạm dụng'입니다"
                },
                {
                    "mistake": "방임(neglect)을 번역하지 않음",
                    "correction": "Bỏ bê, Bỏ mặc",
                    "explanation": "방임도 학대의 한 형태이며 반드시 번역해야 합니다"
                },
                {
                    "mistake": "훈육을 'Lạm dụng'으로 오역",
                    "correction": "Kỷ luật, Dạy dỗ (훈육) vs Lạm dụng (학대) 구분",
                    "explanation": "문화적 차이로 인해 훈육과 학대의 경계를 명확히 해야 합니다"
                }
            ],
            "examples": [
                {
                    "ko": "아동학대 신고를 받고 현장에 출동했습니다.",
                    "vi": "Đã xuất động hiện trường sau khi nhận báo cáo lạm dụng trẻ em.",
                    "situation": "onsite"
                },
                {
                    "ko": "피해 아동을 아동보호전문기관에 인계했습니다.",
                    "vi": "Đã chuyển giao trẻ em bị hại cho cơ quan chuyên trách bảo vệ trẻ em.",
                    "situation": "formal"
                },
                {
                    "ko": "정서적 학대와 방임도 아동학대에 포함됩니다.",
                    "vi": "Lạm dụng tinh thần và bỏ bê cũng được bao gồm trong lạm dụng trẻ em.",
                    "situation": "informal"
                }
            ],
            "relatedTerms": ["방임", "신고의무자", "피해아동", "보호조치", "친권상실"]
        },
        {
            "slug": "hanh-vi-theo-doi",
            "korean": "스토킹",
            "vietnamese": "Hành vi theo dõi",
            "hanja": None,
            "hanjaReading": None,
            "pronunciation": "한 비 떠오 조이",
            "meaningKo": "상대방의 의사에 반하여 지속적으로 접근·감시하여 불안감을 조성하는 행위로, 한국은 2021년 '스토킹범죄의처벌등에관한법률' 제정으로 독립된 범죄로 인정했습니다. 통역 시 '스토킹', '지속적 괴롭힘', '사이버 스토킹'을 구분해야 하며, 베트남어로 'Stalking'을 직역하기 어려워 'Hành vi theo dõi bám đuôi'로 풀어 설명해야 합니다. 피해자의 공포심과 불안감을 정확히 전달하는 것이 중요하며, 한국은 긴급응급조치(접근금지 등)가 있지만 베트남에는 유사 제도가 없어 절차 설명이 필요합니다.",
            "meaningVi": "Hành vi tiếp cận, giám sát liên tục trái ý muốn của đối phương gây lo lắng bất an. Được công nhận là tội phạm độc lập theo Luật xử phạt tội phạm theo dõi năm 2021.",
            "context": "형사 재판, 경찰 신고, 피해자 상담",
            "culturalNote": "한국은 2021년 스토킹처벌법 제정 전까지는 경범죄로만 처벌했으나, 이제는 독립 범죄로 최대 3년 징역이 가능합니다. 베트남에는 스토킹을 독립 범죄로 규정한 법이 없고, 일반 괴롭힘이나 협박죄로 처리합니다. 한국은 데이트폭력과 스토킹을 연계해 강력 대응하지만, 베트남은 아직 인식이 낮습니다. 통역 시 '스토킹'이라는 외래어를 베트남어로 설명하는 것이 어려워, 구체적 행위(따라다니기, 무단 침입, SNS 감시 등)를 나열하는 것이 효과적입니다.",
            "commonMistakes": [
                {
                    "mistake": "Theo dõi만 사용",
                    "correction": "Hành vi theo dõi bám đuôi hoặc Stalking (영어 병기)",
                    "explanation": "'Theo dõi'는 일반적인 '관찰'을 의미하므로 범죄 의미를 명확히 해야 합니다"
                },
                {
                    "mistake": "스토킹을 단순 괴롭힘으로 축소",
                    "correction": "Tội phạm theo dõi (범죄로 강조)",
                    "explanation": "스토킹은 독립된 범죄이며, 단순 괴롭힘보다 중대합니다"
                },
                {
                    "mistake": "사이버 스토킹을 일반 스토킹과 혼용",
                    "correction": "Theo dõi trên mạng, Theo dõi điện tử",
                    "explanation": "사이버 스토킹은 별도로 구분하여 설명해야 합니다"
                }
            ],
            "examples": [
                {
                    "ko": "피해자는 3개월간 지속적인 스토킹 피해를 입었습니다.",
                    "vi": "Nạn nhân đã bị hành vi theo dõi liên tục trong 3 tháng.",
                    "situation": "formal"
                },
                {
                    "ko": "가해자에게 긴급응급조치로 접근금지 100m를 명령했습니다.",
                    "vi": "Đã ra lệnh cấm tiếp cận trong bán kính 100m với người gia hại bằng biện pháp khẩn cấp.",
                    "situation": "formal"
                },
                {
                    "ko": "SNS로 사생활을 감시하는 사이버 스토킹도 처벌됩니다.",
                    "vi": "Theo dõi đời tư qua mạng xã hội (cyber stalking) cũng bị xử phạt.",
                    "situation": "informal"
                }
            ],
            "relatedTerms": ["접근금지", "긴급응급조치", "데이트폭력", "괴롭힘", "사이버범죄"]
        },
        {
            "slug": "lua-dao-qua-dien-thoai",
            "korean": "보이스피싱",
            "vietnamese": "Lừa đảo qua điện thoại",
            "hanja": None,
            "hanjaReading": None,
            "pronunciation": "르어 다오 꽈 디엔 토아이",
            "meaningKo": "전화, 문자, 메신저 등을 이용해 개인정보나 금융정보를 편취하는 사기 범죄로, 한국의 '전기통신금융사기 피해 방지 및 피해금 환급에 관한 특별법'으로 처벌됩니다. 통역 시 'Voice Phishing'을 'Lừa đảo qua điện thoại' 또는 'Lừa đảo giả danh'으로 풀어 설명해야 하며, 한국 특유의 '메신저피싱', '스미싱', '파밍' 등 세부 유형을 베트남어로 구분하는 것이 어려워 영어 병기가 필요합니다. 피해자가 고령자인 경우가 많아 쉬운 용어 사용이 중요하며, 금융 거래 과정을 정확히 통역해야 피해 회복이 가능합니다.",
            "meaningVi": "Tội phạm lừa đảo chiếm đoạt thông tin cá nhân, tài chính qua điện thoại, tin nhắn, ứng dụng nhắn tin. Bị xử phạt theo Luật đặc biệt về phòng ngừa thiệt hại do lừa đảo tài chính điện tử.",
            "context": "형사 재판, 경찰 신고, 금융사기 조사",
            "culturalNote": "한국은 보이스피싱 피해가 매년 급증하여 전담 수사팀과 피해금 환급 제도를 운영하지만, 베트남은 아직 유사 범죄가 적고 법적 대응이 미흡합니다. 한국은 '금융감독원 사칭', '검찰 사칭', '자녀 납치 사칭' 등 다양한 수법이 있고, 대포통장·대포폰 사용이 특징입니다. 베트남에서는 'Lừa đảo qua điện thoại'가 일반적 표현이지만, 한국처럼 세분화된 유형 구분은 없어 통역 시 구체적 설명이 필요합니다.",
            "commonMistakes": [
                {
                    "mistake": "Voice phishing을 음역",
                    "correction": "Lừa đảo qua điện thoại 또는 Lừa đảo giả danh",
                    "explanation": "외래어를 그대로 쓰면 이해하기 어려우므로 베트남어로 풀어야 합니다"
                },
                {
                    "mistake": "모든 전화 사기를 동일하게 번역",
                    "correction": "보이스피싱, 스미싱, 파밍 등 구분 (영어 병기)",
                    "explanation": "유형별 수법이 다르므로 구분이 필요합니다"
                },
                {
                    "mistake": "대포통장을 직역",
                    "correction": "Tài khoản ngân hàng giả, Tài khoản đứng tên người khác",
                    "explanation": "'대포통장'은 한국 특유 용어이므로 설명이 필요합니다"
                }
            ],
            "examples": [
                {
                    "ko": "금융감독원을 사칭한 보이스피싱 범죄로 기소되었습니다.",
                    "vi": "Bị truy tố vì tội lừa đảo qua điện thoại giả danh Cơ quan Giám sát Tài chính.",
                    "situation": "formal"
                },
                {
                    "ko": "피해자가 대포통장으로 3천만 원을 송금했습니다.",
                    "vi": "Nạn nhân đã chuyển 30 triệu won vào tài khoản giả.",
                    "situation": "onsite"
                },
                {
                    "ko": "문자메시지로 링크를 보내는 스미싱 수법을 사용했습니다.",
                    "vi": "Đã sử dụng thủ đoạn smishing gửi đường link qua tin nhắn.",
                    "situation": "formal"
                }
            ],
            "relatedTerms": ["스미싱", "파밍", "대포통장", "금융사기", "피해금환급"]
        },
        {
            "slug": "lai-xe-say-ruou",
            "korean": "음주운전",
            "vietnamese": "Lái xe say rượu",
            "hanja": "飮酒運轉",
            "hanjaReading": "飮(마실 음) + 酒(술 주) + 運(운전할 운) + 轉(구를 전)",
            "pronunciation": "라이 쎄 사이 르어우",
            "meaningKo": "술을 마신 상태에서 자동차 등을 운전하는 범죄로, 한국의 '도로교통법' 및 '특정범죄가중처벌법'으로 엄격히 처벌됩니다. 통역 시 혈중알코올농도(BAC) 기준(0.03%, 0.08%, 0.2%)을 정확히 전달해야 하며, '단순 음주운전', '음주운전 교통사고', '음주운전 치사상'을 구분해야 합니다. 한국은 음주운전에 대한 처벌이 매우 엄격하고 사회적 비난이 강하지만, 베트남은 상대적으로 처벌이 약해 양국 인식 차이를 고려한 통역이 필요합니다. 측정 거부도 처벌 대상임을 명확히 해야 합니다.",
            "meaningVi": "Tội phạm lái xe ô tô sau khi uống rượu. Bị xử phạt nghiêm khắc theo Luật giao thông đường bộ và Luật gia trọng xử phạt tội phạm đặc định.",
            "context": "교통사고 조사, 경찰 단속, 형사 재판",
            "culturalNote": "한국은 2018년 윤창호법(음주운전 가중처벌법) 제정으로 음주운전 사망사고 시 최소 징역 3년이며, 3회 이상 음주운전 시 가중처벌됩니다. 베트남도 음주운전을 처벌하지만 한국만큼 엄격하지 않고, 사회적 인식도 한국보다 관대한 편입니다. 한국은 혈중알코올농도 0.03%부터 처벌하지만, 베트남은 기준이 다르므로 통역 시 수치를 명확히 해야 합니다. 한국에서는 음주측정 거부도 처벌되며, 이는 베트남과 차이가 있습니다.",
            "commonMistakes": [
                {
                    "mistake": "Uống rượu lái xe",
                    "correction": "Lái xe say rượu 또는 Lái xe sau khi uống rượu",
                    "explanation": "어순과 의미상 'Lái xe say rượu'가 공식 용어입니다"
                },
                {
                    "mistake": "혈중알코올농도를 'Độ cồn'만 사용",
                    "correction": "Nồng độ cồn trong máu (BAC)",
                    "explanation": "'Độ cồn'만으로는 불명확하므로 '혈중'임을 명시해야 합니다"
                },
                {
                    "mistake": "측정 거부를 번역하지 않음",
                    "correction": "Từ chối đo nồng độ cồn",
                    "explanation": "측정 거부도 처벌 대상이므로 반드시 번역해야 합니다"
                }
            ],
            "examples": [
                {
                    "ko": "혈중알코올농도 0.15%로 음주운전으로 적발되었습니다.",
                    "vi": "Bị phát hiện lái xe say rượu với nồng độ cồn trong máu 0.15%.",
                    "situation": "onsite"
                },
                {
                    "ko": "음주운전으로 인한 교통사고치사죄로 기소되었습니다.",
                    "vi": "Bị truy tố tội gây tai nạn giao thông chết người do lái xe say rượu.",
                    "situation": "formal"
                },
                {
                    "ko": "음주측정을 3회 거부하여 면허 취소되었습니다.",
                    "vi": "Đã bị thu hồi bằng lái do từ chối đo nồng độ cồn 3 lần.",
                    "situation": "formal"
                }
            ],
            "relatedTerms": ["혈중알코올농도", "교통사고", "면허취소", "특가법", "윤창호법"]
        },
        {
            "slug": "danh-bac",
            "korean": "도박",
            "vietnamese": "Đánh bạc",
            "hanja": "賭博",
            "hanjaReading": "賭(내기 도) + 博(넓을 박)",
            "pronunciation": "다인 박",
            "meaningKo": "우연한 사행에 재물을 걸고 득실을 결정하는 행위로, 한국의 '형법' 및 '사행행위규제법'으로 처벌됩니다. 통역 시 '도박', '상습도박', '도박개장', '인터넷도박'을 명확히 구분해야 하며, 베트남어에서 'Đánh bạc'는 일반 도박, 'Cờ bạc'는 도박 게임을 의미하므로 문맥에 따라 선택해야 합니다. 한국은 강원랜드 외 카지노가 내국인 출입 금지이며, 온라인 도박이 불법이지만 해외 사이트를 통한 도박이 증가하여 처벌이 강화되는 추세입니다. 도박 빚으로 인한 2차 범죄(횡령, 사기)도 함께 다뤄지는 경우가 많습니다.",
            "meaningVi": "Hành vi đặt cược tài sản vào sự may rủi để quyết định thiệt hơn. Bị xử phạt theo Hình luật và Luật quy chế hành vi cờ bạc.",
            "context": "형사 재판, 경찰 수사, 도박 단속",
            "culturalNote": "한국은 도박을 엄격히 금지하여 성인 오락실의 슬롯머신도 불법이며, 합법 카지노(강원랜드)는 내국인 출입이 제한됩니다. 베트남도 도박을 금지하지만 일부 카지노가 허용되고, 한국보다 단속이 느슨합니다. 한국은 온라인 도박(불법 스포츠토토, 카지노 사이트)이 급증하여 해외 사이트 이용도 처벌하며, 도박 중독 치료 프로그램도 운영합니다. 양국 모두 도박을 사회악으로 보지만, 한국이 더 강력히 규제합니다.",
            "commonMistakes": [
                {
                    "mistake": "Cờ bạc와 Đánh bạc 혼용",
                    "correction": "Đánh bạc (행위), Cờ bạc (게임)",
                    "explanation": "'Đánh bạc'는 도박하는 행위, 'Cờ bạc'는 도박 게임 자체를 의미합니다"
                },
                {
                    "mistake": "도박개장을 단순 도박과 동일하게 번역",
                    "correction": "Mở sòng bạc (도박장 개설)",
                    "explanation": "도박개장은 더 중한 범죄로 구분해야 합니다"
                },
                {
                    "mistake": "상습도박을 일반 도박과 혼용",
                    "correction": "Đánh bạc thường xuyên (상습)",
                    "explanation": "상습도박은 가중처벌 대상이므로 구분이 필수입니다"
                }
            ],
            "examples": [
                {
                    "ko": "불법 인터넷 도박 사이트를 운영한 혐의로 구속되었습니다.",
                    "vi": "Bị giam giữ với cáo buộc điều hành trang web đánh bạc trực tuyến bất hợp pháp.",
                    "situation": "formal"
                },
                {
                    "ko": "상습도박 혐의로 징역 1년을 선고받았습니다.",
                    "vi": "Bị kết án 1 năm tù với tội danh đánh bạc thường xuyên.",
                    "situation": "formal"
                },
                {
                    "ko": "도박장을 개설하고 이익금을 챙긴 혐의입니다.",
                    "vi": "Cáo buộc mở sòng bạc và chiếm đoạt tiền lời.",
                    "situation": "onsite"
                }
            ],
            "relatedTerms": ["사행행위", "불법카지노", "온라인도박", "도박개장", "상습도박"]
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
