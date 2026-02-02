#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""사이버범죄 용어 추가 (v9-b)"""
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
            "slug": "hacking",
            "korean": "해킹",
            "vietnamese": "Hacking",
            "hanja": None,
            "hanjaReading": None,
            "pronunciation": "해킹",
            "meaningKo": "정보통신망에 부정하게 접근하거나 정보를 훼손·멸실·변경·위조하는 행위를 말합니다. 통역 시 한국 정보통신망법은 해킹 자체뿐 아니라 해킹 도구 제작·배포, 접근권한 무단 대여도 처벌하며, 국가기관 해킹 시 가중처벌된다는 점을 명확히 전달해야 합니다. 형량은 1년~10년 징역으로 매우 무겁습니다.",
            "meaningVi": "Hành vi truy cập trái phép vào mạng thông tin hoặc phá hủy, xóa, thay đổi, giả mạo thông tin. Luật mạng thông tin Hàn Quốc phạt cả việc tạo/phân phối công cụ hack và cho thuê quyền truy cập, với hình phạt nặng 1-10 năm tù.",
            "context": "사이버범죄 수사 및 법정 진술 상황에서 사용",
            "culturalNote": "한국은 2001년 해킹 사건 이후 사이버 보안법을 대폭 강화했으며, 사이버안전국이 전담 수사합니다. 주요 기업과 정부기관은 침입탐지 시스템을 의무화하고 있습니다. 베트남도 2018년 사이버보안법을 제정했으나 집행 인프라가 약합니다. 통역 시 한국의 높은 처벌 수위와 신속한 디지털 포렌식 역량을 설명해야 합니다.",
            "commonMistakes": [
                {
                    "mistake": "xâm nhập máy tính",
                    "correction": "hacking (mạng thông tin)",
                    "explanation": "'컴퓨터 침입'은 네트워크 해킹을 포함하지 못하여 범위가 좁습니다"
                },
                {
                    "mistake": "đột nhập hệ thống",
                    "correction": "hacking (행위 + 결과)",
                    "explanation": "'시스템 침입'은 물리적 침입과 혼동될 수 있습니다"
                },
                {
                    "mistake": "tin tặc",
                    "correction": "hacker (người) vs hacking (hành vi)",
                    "explanation": "'해커'는 사람, '해킹'은 행위로 구분해야 합니다"
                }
            ],
            "examples": [
                {
                    "ko": "피고인은 정보통신망에 무단으로 침입하여 고객 정보 10만 건을 탈취했습니다",
                    "vi": "Bị cáo đã hacking trái phép vào mạng thông tin và đánh cắp 100,000 thông tin khách hàng",
                    "situation": "formal"
                },
                {
                    "ko": "제 계정이 해킹당했어요. 신고하고 싶어요",
                    "vi": "Tài khoản của tôi bị hack. Tôi muốn báo cáo",
                    "situation": "onsite"
                },
                {
                    "ko": "해킹 프로그램 제작·배포 시 10년 이하 징역에 처해집니다",
                    "vi": "Chế tạo/phân phối chương trình hack bị phạt tù đến 10 năm",
                    "situation": "formal"
                }
            ],
            "relatedTerms": ["랜섬웨어", "디지털증거", "정보통신망법", "사이버수사"]
        },
        {
            "slug": "ransomware",
            "korean": "랜섬웨어",
            "vietnamese": "Ransomware",
            "hanja": None,
            "hanjaReading": None,
            "pronunciation": "랜섬웨어",
            "meaningKo": "컴퓨터 시스템을 감염시켜 파일을 암호화한 뒤 복구 대가로 금전을 요구하는 악성 프로그램입니다. 통역 시 한국은 랜섬웨어 배포를 정보통신망법 위반(10년 이하 징역)과 공갈죄(10년 이하 징역)로 이중 처벌하며, 가상화폐 추적을 통해 검거율을 높이고 있다는 점을 명확히 전달해야 합니다. 피해 신고 시 복구 지원과 수사가 병행됩니다.",
            "meaningVi": "Chương trình độc hại lây nhiễm hệ thống máy tính, mã hóa file và đòi tiền để khôi phục. Ở Hàn Quốc bị xử lý kép theo Luật mạng thông tin (10 năm tù) và tội đe dọa tống tiền (10 năm tù), với truy vết tiền ảo để nâng cao tỷ lệ bắt giữ.",
            "context": "랜섬웨어 피해 신고 및 수사 협조 상황에서 사용",
            "culturalNote": "한국은 2017년 워너크라이 대란 이후 국가 차원의 랜섬웨어 대응 시스템을 구축했으며, 한국인터넷진흥원(KISA)이 무료 복구 도구와 상담을 제공합니다. 베트남은 랜섬웨어 피해가 증가하고 있으나 대응 인프라가 부족합니다. 통역 시 한국의 신속한 기술 지원과 가상화폐 추적 역량을 설명해야 합니다.",
            "commonMistakes": [
                {
                    "mistake": "virus mã hóa",
                    "correction": "ransomware",
                    "explanation": "'암호화 바이러스'는 기술적으로 정확하나 범죄 유형으로서의 특성이 누락됩니다"
                },
                {
                    "mistake": "phần mềm tống tiền",
                    "correction": "ransomware (국제 표준 용어)",
                    "explanation": "'공갈 소프트웨어'는 번역이지만 통역에서는 원어를 사용하는 것이 명확합니다"
                },
                {
                    "mistake": "virus khóa máy",
                    "correction": "ransomware (파일 암호화 + 금전 요구)",
                    "explanation": "'컴퓨터 잠금 바이러스'는 랜섬웨어의 핵심인 금전 요구가 빠집니다"
                }
            ],
            "examples": [
                {
                    "ko": "회사 서버가 랜섬웨어에 감염되어 모든 파일이 암호화되었습니다",
                    "vi": "Server công ty bị lây nhiễm ransomware và tất cả file đã bị mã hóa",
                    "situation": "formal"
                },
                {
                    "ko": "랜섬웨어 걸렸는데 돈 내야 하나요?",
                    "vi": "Bị ransomware rồi, có phải trả tiền không?",
                    "situation": "onsite"
                },
                {
                    "ko": "랜섬웨어 제작·배포자는 정보통신망법 위반으로 10년 이하 징역에 처해집니다",
                    "vi": "Người chế tạo/phán tán ransomware bị phạt tù đến 10 năm theo Luật mạng thông tin",
                    "situation": "formal"
                }
            ],
            "relatedTerms": ["해킹", "악성코드", "가상화폐", "디지털포렌식"]
        },
        {
            "slug": "phishing",
            "korean": "피싱",
            "vietnamese": "Phishing",
            "hanja": None,
            "hanjaReading": None,
            "pronunciation": "피싱",
            "meaningKo": "금융기관 등을 사칭하여 개인정보나 금융정보를 빼내는 사기 수법입니다. 통역 시 한국은 스미싱(문자), 보이스피싱(전화), 메신저피싱(카톡) 등 유형이 다양하며, 전기통신금융사기로 3년~50년 무기징역까지 처벌이 가능하다는 점을 명확히 전달해야 합니다. 중국 조직이 베트남에서 한국인을 대상으로 보이스피싱 하는 사례가 많습니다.",
            "meaningVi": "Thủ đoạn lừa đảo mạo danh tổ chức tài chính để đánh cắp thông tin cá nhân hoặc tài chính. Ở Hàn Quốc có nhiều loại như smishing (tin nhắn), voice phishing (điện thoại), messenger phishing (KakaoTalk), bị phạt 3 năm đến chung thân theo tội lừa đảo tài chính viễn thông.",
            "context": "피싱 피해 신고 및 금융사기 수사 상황에서 사용",
            "culturalNote": "한국은 보이스피싱 피해가 연간 수천억 원에 달하며, 금융감독원과 경찰이 합동으로 대응합니다. 피해 신고 시 계좌 지급정지와 피해금 환급이 가능하나 시간이 중요합니다. 베트남은 피싱 개념이 아직 생소하며, 베트남 현지 조직범죄단이 한국인 대상 보이스피싱 콜센터를 운영하는 사례가 많아 통역 시 주의가 필요합니다.",
            "commonMistakes": [
                {
                    "mistake": "lừa đảo qua điện thoại",
                    "correction": "voice phishing (전화) vs phishing (포괄)",
                    "explanation": "'전화 사기'는 보이스피싱만 지칭하여 이메일·문자 피싱을 누락합니다"
                },
                {
                    "mistake": "giả mạo ngân hàng",
                    "correction": "phishing (수법) - giả mạo là một phần",
                    "explanation": "'은행 사칭'은 피싱의 한 요소이지 전체를 대표하지 못합니다"
                },
                {
                    "mistake": "đánh cắp thông tin",
                    "correction": "phishing (사기 수법) vs hacking (기술적 침입)",
                    "explanation": "'정보 절취'는 해킹과 혼동되며 사기 수법의 본질이 누락됩니다"
                }
            ],
            "examples": [
                {
                    "ko": "금융감독원을 사칭한 피싱 메일로 개인정보 1만 건이 유출되었습니다",
                    "vi": "1 vạn thông tin cá nhân bị rò rỉ qua email phishing mạo danh Cơ quan giám sát tài chính",
                    "situation": "formal"
                },
                {
                    "ko": "경찰이라며 돈 보내래요. 피싱인가요?",
                    "vi": "Họ tự xưng là cảnh sát và bảo chuyển tiền. Có phải phishing không?",
                    "situation": "onsite"
                },
                {
                    "ko": "피싱 범죄는 전기통신금융사기법으로 처벌됩니다",
                    "vi": "Tội phishing bị xử phạt theo Luật lừa đảo tài chính viễn thông",
                    "situation": "formal"
                }
            ],
            "relatedTerms": ["보이스피싱", "스미싱", "전기통신금융사기", "계좌지급정지"]
        },
        {
            "slug": "bang-chung-so",
            "korean": "디지털증거",
            "vietnamese": "Bằng chứng số",
            "hanja": None,
            "hanjaReading": None,
            "pronunciation": "디지털증거",
            "meaningKo": "컴퓨터나 전자기기에 저장된 디지털 정보로서 범죄 입증에 사용되는 증거를 말합니다. 통역 시 한국은 디지털증거의 수집·보관·분석에 엄격한 절차(압수수색영장 필수, 해시값 검증, 연속성 입증)를 요구하며, 절차 위반 시 증거능력이 부정된다는 점을 명확히 전달해야 합니다. 포렌식 전문가가 법정에서 증거의 무결성을 증언합니다.",
            "meaningVi": "Chứng cứ là thông tin số được lưu trữ trên máy tính hoặc thiết bị điện tử dùng để chứng minh tội phạm. Ở Hàn Quốc yêu cầu quy trình nghiêm ngặt (lệnh khám xét bắt buộc, xác minh hash, chứng minh tính liên tục), vi phạm thủ tục sẽ bị từ chối hiệu lực chứng cứ.",
            "context": "사이버범죄 재판 및 디지털 포렌식 분석 상황에서 사용",
            "culturalNote": "한국은 2011년 형사소송법 개정으로 디지털증거의 증거능력 요건을 명문화했으며, 경찰·검찰에 디지털포렌식센터가 설치되어 있습니다. 증거 수집 시 원본 보존과 복사본 분석이 원칙이며, 블록체인 기반 증거 보전 시스템도 도입 중입니다. 베트남은 디지털증거 개념은 있으나 절차법이 미비하여 통역 시 한국의 엄격한 절차를 강조해야 합니다.",
            "commonMistakes": [
                {
                    "mistake": "chứng cứ điện tử",
                    "correction": "bằng chứng số (디지털증거)",
                    "explanation": "'전자증거'는 포괄적이나 법률 용어로는 '디지털증거'가 정확합니다"
                },
                {
                    "mistake": "dữ liệu máy tính",
                    "correction": "bằng chứng số (증거로서의 법적 성격)",
                    "explanation": "'컴퓨터 데이터'는 일반 정보이며 증거로서의 법적 요건이 누락됩니다"
                },
                {
                    "mistake": "tài liệu số",
                    "correction": "bằng chứng số (디지털 형태의 증거)",
                    "explanation": "'디지털 문서'는 텍스트 파일만 연상되며 로그, 메타데이터 등이 제외됩니다"
                }
            ],
            "examples": [
                {
                    "ko": "피고인의 컴퓨터에서 압수한 디지털증거를 분석한 결과 범행이 입증되었습니다",
                    "vi": "Phân tích bằng chứng số thu giữ từ máy tính bị cáo đã chứng minh hành vi phạm tội",
                    "situation": "formal"
                },
                {
                    "ko": "제 휴대폰이 압수되었는데 디지털증거로 쓰이나요?",
                    "vi": "Điện thoại của tôi bị thu giữ, có dùng làm bằng chứng số không?",
                    "situation": "onsite"
                },
                {
                    "ko": "디지털증거는 해시값으로 무결성을 검증합니다",
                    "vi": "Bằng chứng số được xác minh tính toàn vẹn bằng giá trị hash",
                    "situation": "formal"
                }
            ],
            "relatedTerms": ["디지털포렌식", "압수수색", "해시값", "증거능력"]
        },
        {
            "slug": "dieu-tra-an-ninh-mang",
            "korean": "사이버수사",
            "vietnamese": "Điều tra an ninh mạng",
            "hanja": None,
            "hanjaReading": None,
            "pronunciation": "사이버수사",
            "meaningKo": "정보통신망을 이용한 범죄를 수사하는 활동으로, 해킹·랜섬웨어·피싱·명예훼손 등을 포함합니다. 통역 시 한국은 경찰청 사이버안전국과 사이버수사대가 전담하며, IP 추적·디지털 포렌식·가상화폐 추적 등 전문 기술을 활용한다는 점을 명확히 전달해야 합니다. 국제공조 수사가 빈번하며 베트남 경찰과도 협력합니다.",
            "meaningVi": "Hoạt động điều tra tội phạm sử dụng mạng thông tin, bao gồm hacking, ransomware, phishing, xúc phạm danh dự. Ở Hàn Quốc do Cục An ninh mạng và Đội điều tra an ninh mạng phụ trách, sử dụng công nghệ chuyên môn như truy vết IP, điều tra số, truy vết tiền ảo.",
            "context": "사이버범죄 피해 신고 및 수사 협조 요청 상황에서 사용",
            "culturalNote": "한국은 1990년대 후반부터 사이버범죄가 급증하며 전문 수사 조직을 구축했습니다. 경찰청 사이버안전국은 24시간 신고센터를 운영하며, 암호화폐 추적과 다크웹 모니터링 능력이 뛰어납니다. 베트남도 사이버범죄가 증가하고 있으나 수사 인프라가 부족합니다. 통역 시 국제공조 수사 절차와 증거 제출 방법을 설명해야 합니다.",
            "commonMistakes": [
                {
                    "mistake": "điều tra internet",
                    "correction": "điều tra an ninh mạng (사이버범죄 전문)",
                    "explanation": "'인터넷 수사'는 포괄적이며 사이버범죄의 전문성이 약화됩니다"
                },
                {
                    "mistake": "điều tra tội phạm mạng",
                    "correction": "điều tra an ninh mạng (조직·절차 포함)",
                    "explanation": "'네트워크 범죄 수사'는 행위 중심이며 전문 조직의 개념이 누락됩니다"
                },
                {
                    "mistake": "cảnh sát mạng",
                    "correction": "điều tra an ninh mạng (수사 활동) vs cảnh sát an ninh mạng (조직)",
                    "explanation": "'사이버 경찰'은 조직이며, '사이버수사'는 활동으로 구분해야 합니다"
                }
            ],
            "examples": [
                {
                    "ko": "사이버수사대는 IP 추적을 통해 해커를 검거했습니다",
                    "vi": "Đội điều tra an ninh mạng đã bắt giữ hacker thông qua truy vết IP",
                    "situation": "formal"
                },
                {
                    "ko": "사이버 범죄 신고는 어디 하나요?",
                    "vi": "Báo cáo tội phạm mạng ở đâu?",
                    "situation": "onsite"
                },
                {
                    "ko": "사이버수사는 국제공조가 필수적입니다",
                    "vi": "Điều tra an ninh mạng cần thiết phải có hợp tác quốc tế",
                    "situation": "formal"
                }
            ],
            "relatedTerms": ["디지털포렌식", "IP추적", "국제공조", "사이버안전국"]
        },
        {
            "slug": "luat-mang-thong-tin",
            "korean": "정보통신망법",
            "vietnamese": "Luật mạng thông tin",
            "hanja": "情報通信網法",
            "hanjaReading": "情(뜻 정) + 報(알릴 보) + 通(통할 통) + 信(믿을 신) + 網(그물 망) + 法(법 법)",
            "pronunciation": "정보통신망뻡",
            "meaningKo": "정보통신망의 이용 촉진 및 정보 보호를 위한 법률로, 해킹·악성프로그램·개인정보 유출·스팸·명예훼손 등을 규제합니다. 통역 시 정보통신서비스 제공자의 개인정보 보호 의무, 불법정보 유통 금지, 사이버 명예훼손 처벌 등이 포함되며, 위반 시 형사처벌과 과징금이 부과된다는 점을 명확히 전달해야 합니다.",
            "meaningVi": "Luật xúc tiến sử dụng mạng thông tin và bảo vệ thông tin, quy định về hacking, chương trình độc hại, rò rỉ thông tin cá nhân, spam, xúc phạm danh dự. Vi phạm sẽ bị xử lý hình sự và phạt tiền hành chính.",
            "context": "정보통신 관련 법률 자문 및 규제 위반 사건에서 사용",
            "culturalNote": "한국은 2001년 정보통신망법을 제정하여 개인정보 보호와 사이버 범죄를 동시에 규율합니다. 최근 개인정보보호법과 통합 논의가 진행 중이며, 주요 인터넷 기업은 본인확인제와 개인정보 암호화를 의무화하고 있습니다. 베트남은 2018년 사이버보안법을 제정했으나 정보통신망법처럼 포괄적이지 않습니다. 통역 시 한국의 높은 규제 수준을 설명해야 합니다.",
            "commonMistakes": [
                {
                    "mistake": "luật internet",
                    "correction": "luật mạng thông tin (정보통신망법)",
                    "explanation": "'인터넷법'은 비공식적이며 법률의 정확한 명칭이 아닙니다"
                },
                {
                    "mistake": "luật an ninh mạng",
                    "correction": "luật mạng thông tin (보호+규제) vs luật an ninh mạng (보안)",
                    "explanation": "'사이버보안법'은 보안에 초점을 두며 개인정보 보호 등이 누락됩니다"
                },
                {
                    "mistake": "luật bảo vệ thông tin",
                    "correction": "luật mạng thông tin (정보통신망 전체)",
                    "explanation": "'정보보호법'은 보호만 다루며 망 이용 촉진 등 다른 목적이 빠집니다"
                }
            ],
            "examples": [
                {
                    "ko": "정보통신망법 위반으로 해커에게 징역 5년이 선고되었습니다",
                    "vi": "Hacker bị tuyên án 5 năm tù vì vi phạm Luật mạng thông tin",
                    "situation": "formal"
                },
                {
                    "ko": "개인정보 유출되면 정보통신망법으로 처벌되나요?",
                    "vi": "Nếu rò rỉ thông tin cá nhân có bị phạt theo Luật mạng thông tin không?",
                    "situation": "onsite"
                },
                {
                    "ko": "정보통신서비스 제공자는 개인정보를 암호화해야 합니다",
                    "vi": "Nhà cung cấp dịch vụ mạng thông tin phải mã hóa thông tin cá nhân",
                    "situation": "formal"
                }
            ],
            "relatedTerms": ["개인정보보호법", "해킹", "개인정보유출", "과징금"]
        },
        {
            "slug": "lua-dao-internet",
            "korean": "인터넷사기",
            "vietnamese": "Lừa đảo internet",
            "hanja": None,
            "hanjaReading": None,
            "pronunciation": "인터넷사기",
            "meaningKo": "인터넷을 이용한 사기 범죄로, 전자상거래 사기·중고거래 사기·구인구직 사기 등을 포함합니다. 통역 시 한국은 인터넷 거래가 일상화되면서 사기 피해도 급증했으며, 경찰청 사이버수사대가 전담 수사하고, 피해금 환급을 위한 전자금융사기 피해구제 제도가 있다는 점을 명확히 전달해야 합니다. 형량은 10년 이하 징역입니다.",
            "meaningVi": "Tội lừa đảo sử dụng internet, bao gồm lừa đảo thương mại điện tử, giao dịch đồ cũ, tuyển dụng. Ở Hàn Quốc do Đội điều tra an ninh mạng phụ trách, có chế độ cứu trợ nạn nhân lừa đảo tài chính điện tử để hoàn trả tiền, hình phạt đến 10 năm tù.",
            "context": "인터넷 사기 피해 신고 및 수사 협조 상황에서 사용",
            "culturalNote": "한국은 중고거래 플랫폼(당근마켓 등)과 전자상거래가 발달하면서 인터넷사기가 증가했습니다. 경찰은 '사이버캅' 앱으로 실시간 신고를 받으며, 피해 신고 시 계좌 추적과 지급정지가 신속히 이루어집니다. 베트남도 인터넷 사기가 증가하고 있으나 피해 구제 시스템이 약합니다. 통역 시 한국의 신속한 계좌 추적과 피해금 환급 제도를 설명해야 합니다.",
            "commonMistakes": [
                {
                    "mistake": "lừa đảo online",
                    "correction": "lừa đảo internet (공식 용어)",
                    "explanation": "'온라인 사기'는 영어식 표현으로 한국어 법률 용어와 대응하지 않습니다"
                },
                {
                    "mistake": "lừa đảo mạng",
                    "correction": "lừa đảo internet (인터넷 사기) vs lừa đảo viễn thông (전기통신 사기)",
                    "explanation": "'망 사기'는 모호하며 전기통신 사기와 혼동됩니다"
                },
                {
                    "mistake": "mua bán lừa đảo",
                    "correction": "lừa đảo internet (phạm vi rộng hơn)",
                    "explanation": "'매매 사기'는 거래 사기만 지칭하여 구인·구직 사기 등이 누락됩니다"
                }
            ],
            "examples": [
                {
                    "ko": "중고거래 사이트에서 물건값을 받고 물건을 보내지 않은 인터넷사기 혐의로 기소되었습니다",
                    "vi": "Bị truy tố tội lừa đảo internet vì nhận tiền trên trang giao dịch đồ cũ nhưng không gửi hàng",
                    "situation": "formal"
                },
                {
                    "ko": "인터넷으로 물건 샀는데 안 와요. 신고할 수 있나요?",
                    "vi": "Mua hàng qua internet mà không nhận được. Có thể báo cáo không?",
                    "situation": "onsite"
                },
                {
                    "ko": "인터넷사기 피해는 사이버수사대에 신고하세요",
                    "vi": "Nạn nhân lừa đảo internet hãy báo cáo cho Đội điều tra an ninh mạng",
                    "situation": "formal"
                }
            ],
            "relatedTerms": ["전자상거래", "중고거래", "계좌추적", "피해금환급"]
        },
        {
            "slug": "xuc-pham-danh-du",
            "korean": "명예훼손",
            "vietnamese": "Xúc phạm danh dự",
            "hanja": "名譽毁損",
            "hanjaReading": "名(이름 명) + 譽(명예 예) + 毁(무너뜨릴 훼) + 損(덜 손)",
            "pronunciation": "명예훼손",
            "meaningKo": "공연히 사실 또는 허위사실을 적시하여 타인의 명예를 훼손하는 범죄입니다. 통역 시 한국은 사실적시 명예훼손도 처벌하며(진실이어도 처벌 가능), 사이버 명예훼손은 정보통신망법으로 가중처벌된다는 점을 명확히 전달해야 합니다. 형량은 2년~7년 징역이며, 피해자 고소가 있어야 처벌됩니다(친고죄).",
            "meaningVi": "Tội công khai nêu sự thật hoặc sự thật giả để xúc phạm danh dự người khác. Ở Hàn Quốc ngay cả nêu sự thật cũng bị phạt (dù là sự thật vẫn có thể bị phạt), xúc phạm danh dự trên mạng bị phạt nặng hơn theo Luật mạng thông tin. Hình phạt 2-7 năm tù, phải có đơn tố cáo của nạn nhân (tội cáo tố).",
            "context": "사이버 명예훼손 고소 및 재판 상황에서 사용",
            "culturalNote": "한국은 명예훼손을 형사처벌하는 드문 나라로, 표현의 자유와 명예 보호 사이에서 논란이 많습니다. 사실 적시 명예훼손은 진실이어도 공익성이 없으면 처벌되며, 인터넷 댓글·SNS 게시물도 포함됩니다. 베트남은 형법에 명예훼손죄가 있으나 사실 적시는 처벌하지 않습니다. 통역 시 한국의 엄격한 명예 보호 기준을 설명해야 합니다.",
            "commonMistakes": [
                {
                    "mistake": "phỉ báng",
                    "correction": "xúc phạm danh dự (사실 적시) vs phỉ báng (허위사실)",
                    "explanation": "'비방'은 허위사실만 의미하며 사실적시 명예훼손을 포함하지 못합니다"
                },
                {
                    "mistake": "làm mất danh dự",
                    "correction": "xúc phạm danh dự (범죄 행위)",
                    "explanation": "'명예를 잃게 하다'는 일상 표현이며 범죄로서의 법적 성격이 누락됩니다"
                },
                {
                    "mistake": "nói xấu",
                    "correction": "xúc phạm danh dự (공연성 + 사실 적시)",
                    "explanation": "'욕하다'는 단순 모욕이며 사실 적시와 공연성 요건이 빠집니다"
                }
            ],
            "examples": [
                {
                    "ko": "피고인은 인터넷 게시판에 피해자의 사생활을 공개하여 명예를 훼손했습니다",
                    "vi": "Bị cáo đã xúc phạm danh dự bằng cách công khai đời tư của nạn nhân trên diễn đàn internet",
                    "situation": "formal"
                },
                {
                    "ko": "SNS에 제 얘기를 막 올렸어요. 명예훼손으로 고소할 수 있나요?",
                    "vi": "Họ lung tung đăng chuyện của tôi lên SNS. Có thể kiện xúc phạm danh dự không?",
                    "situation": "onsite"
                },
                {
                    "ko": "사실이어도 공익성이 없으면 명예훼손이 성립합니다",
                    "vi": "Dù là sự thật nhưng nếu không có tính công ích vẫn cấu thành xúc phạm danh dự",
                    "situation": "formal"
                }
            ],
            "relatedTerms": ["모욕죄", "정보통신망법", "친고죄", "공연성"]
        },
        {
            "slug": "theo-doi-quay-roi-mang",
            "korean": "사이버스토킹",
            "vietnamese": "Theo dõi quấy rối mạng",
            "hanja": None,
            "hanjaReading": None,
            "pronunciation": "사이버스토킹",
            "meaningKo": "정보통신망을 통해 지속적·반복적으로 타인에게 공포심이나 불안감을 유발하는 행위입니다. 통역 시 한국은 정보통신망법으로 2년 이하 징역 또는 2천만 원 이하 벌금에 처하며, SNS 메시지·댓글·위치추적 등 다양한 형태를 포함하고, 스토킹처벌법과 중복 적용될 수 있다는 점을 명확히 전달해야 합니다.",
            "meaningVi": "Hành vi liên tục, lặp đi lặp lại gây sợ hãi hoặc lo lắng cho người khác qua mạng thông tin. Ở Hàn Quốc bị phạt tù 2 năm hoặc phạt tiền đến 20 triệu won theo Luật mạng thông tin, bao gồm tin nhắn SNS, bình luận, truy vết vị trí, có thể áp dụng chồng lên Luật phạt theo dõi quấy rối.",
            "context": "사이버스토킹 피해 신고 및 법적 대응 상황에서 사용",
            "culturalNote": "한국은 2021년 스토킹처벌법 제정 후 사이버스토킹에 대한 처벌이 강화되었습니다. SNS 메시지 수백 통, 악성 댓글 도배, GPS 추적 등이 포함되며, 피해자는 경찰에 신고하여 접근금지·잠정조치를 받을 수 있습니다. 베트남은 사이버스토킹 개념이 생소하며 관련 법률이 미비합니다. 통역 시 한국의 적극적 피해자 보호 조치를 설명해야 합니다.",
            "commonMistakes": [
                {
                    "mistake": "theo dõi online",
                    "correction": "theo dõi quấy rối mạng (지속성·반복성)",
                    "explanation": "'온라인 추적'은 단순 행위이며 공포·불안 유발의 범죄 요소가 누락됩니다"
                },
                {
                    "mistake": "quấy rối internet",
                    "correction": "theo dõi quấy rối mạng (스토킹의 특성)",
                    "explanation": "'인터넷 괴롭힘'은 일회성도 포함하며 스토킹의 지속적 추적 특성이 약화됩니다"
                },
                {
                    "mistake": "bám đuôi trên mạng",
                    "correction": "theo dõi quấy rối mạng (법적 용어)",
                    "explanation": "'온라인 미행'은 일상 표현으로 법률 용어로 부적절합니다"
                }
            ],
            "examples": [
                {
                    "ko": "피고인은 6개월간 피해자에게 하루 수십 통의 SNS 메시지를 보내 사이버스토킹을 했습니다",
                    "vi": "Bị cáo đã theo dõi quấy rối mạng bằng cách gửi hàng chục tin nhắn SNS mỗi ngày cho nạn nhân trong 6 tháng",
                    "situation": "formal"
                },
                {
                    "ko": "전 남자친구가 계속 메시지 보내요. 사이버스토킹인가요?",
                    "vi": "Bạn trai cũ cứ gửi tin nhắn liên tục. Có phải theo dõi quấy rối mạng không?",
                    "situation": "onsite"
                },
                {
                    "ko": "사이버스토킹 피해자는 경찰에 신고하여 잠정조치를 받을 수 있습니다",
                    "vi": "Nạn nhân theo dõi quấy rối mạng có thể báo cáo cảnh sát để được biện pháp tạm thời",
                    "situation": "formal"
                }
            ],
            "relatedTerms": ["스토킹처벌법", "접근금지", "잠정조치", "정보통신망법"]
        },
        {
            "slug": "quay-phim-bat-hop-phap",
            "korean": "불법촬영",
            "vietnamese": "Quay phim bất hợp pháp",
            "hanja": "不法撮影",
            "hanjaReading": "不(아닐 불) + 法(법 법) + 撮(찍을 촬) + 影(그림자 영)",
            "pronunciation": "불법촬영",
            "meaningKo": "타인의 신체를 그 의사에 반하여 촬영하거나 유포하는 범죄로, 몰래카메라·디지털 성범죄를 포함합니다. 통역 시 한국은 성폭력처벌법으로 촬영(7년 이하 징역), 유포(7년 이하 징역), 유포 협박(1년~3년 징역)을 각각 처벌하며, n번방 사건 이후 처벌이 대폭 강화되었다는 점을 명확히 전달해야 합니다. 피해 영상 삭제 지원도 제공됩니다.",
            "meaningVi": "Tội quay phim hoặc phát tán hình ảnh cơ thể người khác trái với ý muốn của họ, bao gồm camera giấu kín và tội phạm tình dục số. Ở Hàn Quốc Luật phạt bạo lực tình dục phạt riêng quay (7 năm tù), phát tán (7 năm tù), đe dọa phát tán (1-3 năm tù), hình phạt được tăng mạnh sau vụ n번방.",
            "context": "불법촬영 피해 신고 및 디지털 성범죄 수사 상황에서 사용",
            "culturalNote": "한국은 2010년대 몰카 범죄가 급증하며 2020년 성폭력처벌법을 대폭 개정했습니다. 불법촬영물 삭제 지원센터가 운영되며, AI로 유포 영상을 추적·삭제합니다. 화장실·숙박시설 몰카 단속도 강화되었습니다. 베트남은 불법촬영 개념이 생소하며 처벌 규정이 약합니다. 통역 시 한국의 엄격한 처벌과 피해자 지원 시스템을 설명해야 합니다.",
            "commonMistakes": [
                {
                    "mistake": "quay lén",
                    "correction": "quay phim bất hợp pháp (법적 용어)",
                    "explanation": "'몰래 촬영'은 일상 표현이며 법적 처벌 대상으로서의 성격이 약화됩니다"
                },
                {
                    "mistake": "camera giấu kín",
                    "correction": "quay phim bất hợp pháp (행위 + 도구)",
                    "explanation": "'숨은 카메라'는 도구이며 범죄 행위 자체를 지칭하지 못합니다"
                },
                {
                    "mistake": "chụp ảnh trái phép",
                    "correction": "quay phim bất hợp pháp (영상 중심)",
                    "explanation": "'불법 사진'은 사진만 의미하며 영상 촬영이 누락됩니다"
                }
            ],
            "examples": [
                {
                    "ko": "피고인은 공중화장실에 초소형 카메라를 설치하여 불법촬영한 혐의로 기소되었습니다",
                    "vi": "Bị cáo bị truy tố tội quay phim bất hợp pháp vì lắp camera siêu nhỏ trong nhà vệ sinh công cộng",
                    "situation": "formal"
                },
                {
                    "ko": "탈의실에서 몰카 당했어요. 신고하고 싶어요",
                    "vi": "Tôi bị quay lén trong phòng thay đồ. Muốn báo cáo",
                    "situation": "onsite"
                },
                {
                    "ko": "불법촬영물 유포 시 7년 이하 징역에 처해집니다",
                    "vi": "Phát tán phim bất hợp pháp bị phạt tù đến 7 năm",
                    "situation": "formal"
                }
            ],
            "relatedTerms": ["디지털성범죄", "성폭력처벌법", "몰카", "영상삭제지원"]
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
    print(f"✅ Added {len(filtered)} terms (사이버범죄). Total: {len(data)}")

if __name__ == '__main__':
    main()
