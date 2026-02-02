#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""AI/기술규제 용어 추가 (v9-h)"""
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
            "slug": "quy-che-tri-tue-nhan-tao",
            "korean": "인공지능규제",
            "vietnamese": "Quy chế trí tuệ nhân tạo",
            "hanja": "人工知能規制",
            "hanjaReading": "人(사람 인) + 工(장인 공) + 知(알 지) + 能(능할 능) + 規(법 규) + 制(억제할 제)",
            "pronunciation": "인공지능규제",
            "meaningKo": "인공지능 기술의 개발·활용을 규율하여 윤리·안전·책임을 확보하는 법적 체계입니다. 통역 시 한국은 AI 기본법 제정을 추진 중이며, EU AI Act를 참고하고, 고위험 AI는 사전 평가 의무화, AI 생성물 표시 의무, 알고리즘 차별 금지, AI 사고 시 제조자 책임이 규정될 예정이라는 점을 명확히 전달해야 합니다.",
            "meaningVi": "Hệ thống pháp lý quy định phát triển và ứng dụng công nghệ trí tuệ nhân tạo để đảm bảo đạo đức, an toàn, trách nhiệm. Hàn Quốc đang thúc đẩy Luật cơ bản AI, tham khảo EU AI Act, AI rủi ro cao bắt buộc đánh giá trước, nghĩa vụ ghi nhãn sản phẩm AI, cấm phân biệt thuật toán, tai nạn AI sẽ quy định trách nhiệm nhà sản xuất.",
            "context": "AI 서비스 개발 및 윤리 심사 상황에서 사용",
            "culturalNote": "한국은 AI 강국을 목표로 규제보다 진흥 중심이었으나, ChatGPT 등장 이후 규제 필요성이 대두되었습니다. 개인정보보호법·저작권법 등 기존 법으로 부분 규율하지만, 포괄적 AI 법안이 논의 중입니다. 베트남은 AI 규제가 없어 통역 시 한국의 규제 방향을 설명해야 합니다.",
            "commonMistakes": [
                {
                    "mistake": "luật AI",
                    "correction": "quy chế trí tuệ nhân tạo (규제 체계)",
                    "explanation": "'AI법'은 단일 법률처럼 들리며 규제 체계의 포괄성이 약화됩니다"
                },
                {
                    "mistake": "kiểm soát AI",
                    "correction": "quy chế trí tuệ nhân tạo (법적 규율)",
                    "explanation": "'AI 통제'는 일상 표현이며 법적 규제의 개념이 누락됩니다"
                },
                {
                    "mistake": "quản lý trí tuệ nhân tạo",
                    "correction": "quy chế trí tuệ nhân tạo (규제)",
                    "explanation": "'AI 관리'는 행정 관리이며 법적 규제와 구분됩니다"
                }
            ],
            "examples": [
                {
                    "ko": "고위험 인공지능은 사전 안전성 평가를 받아야 합니다",
                    "vi": "AI rủi ro cao phải được đánh giá an toàn trước",
                    "situation": "formal"
                },
                {
                    "ko": "AI가 만든 콘텐츠는 표시해야 하나요?",
                    "vi": "Nội dung do AI tạo phải ghi nhãn không?",
                    "situation": "onsite"
                },
                {
                    "ko": "인공지능 규제는 혁신과 안전의 균형을 추구합니다",
                    "vi": "Quy chế trí tuệ nhân tạo theo đuổi cân bằng giữa đổi mới và an toàn",
                    "situation": "formal"
                }
            ],
            "relatedTerms": ["AI기본법", "고위험AI", "알고리즘윤리", "EU AI Act"]
        },
        {
            "slug": "xe-tu-lai",
            "korean": "자율주행",
            "vietnamese": "Xe tự lái",
            "hanja": "自律走行",
            "hanjaReading": "自(스스로 자) + 律(법률 률) + 走(달릴 주) + 行(다닐 행)",
            "pronunciation": "자율주행",
            "meaningKo": "운전자 개입 없이 차량이 스스로 주행하는 기술로, 레벨 0~5로 구분됩니다. 통역 시 한국은 자율주행법을 제정하여 시험운행을 허가하며, 레벨 3 이상은 제조사 책임, 사고 시 보험 적용 방식이 다르고, 완전자율주행(레벨 5)은 아직 불법이며, 데이터 수집·개인정보 보호도 규제한다는 점을 명확히 전달해야 합니다.",
            "meaningVi": "Công nghệ xe tự chạy không cần can thiệp người lái, chia thành cấp 0-5. Hàn Quốc ban hành Luật xe tự lái cho phép vận hành thử nghiệm, từ cấp 3 trở lên là trách nhiệm nhà sản xuất, tai nạn áp dụng bảo hiểm khác nhau, xe tự lái hoàn toàn (cấp 5) còn bất hợp pháp, cũng quy định thu thập dữ liệu và bảo vệ thông tin cá nhân.",
            "context": "자율주행차 시험운행 및 사고 책임 판단 상황에서 사용",
            "culturalNote": "한국은 자율주행 선도국을 목표로 세종·판교 등에서 시범 운행 중이며, 현대차·카카오모빌리티가 기술을 개발하고 있습니다. 레벨 3 자율주행이 부분 허가되었으나 사고 책임 논란이 많습니다. 베트남은 자율주행이 초기 단계여서 통역 시 한국의 선진 기술과 규제를 설명해야 합니다.",
            "commonMistakes": [
                {
                    "mistake": "xe không người lái",
                    "correction": "xe tự lái (자율주행)",
                    "explanation": "'무인 차량'은 완전자율만 연상되며 부분자율이 누락됩니다"
                },
                {
                    "mistake": "lái xe tự động",
                    "correction": "xe tự lái (차량 중심)",
                    "explanation": "'자동 운전'은 행위 중심이며 차량 기술로서의 자율주행과 다릅니다"
                },
                {
                    "mistake": "ô tô AI",
                    "correction": "xe tự lái (공식 용어)",
                    "explanation": "'AI 자동차'는 비공식적이며 법률 용어로 부적절합니다"
                }
            ],
            "examples": [
                {
                    "ko": "레벨 3 자율주행차는 제한적 조건에서 운전자 개입 없이 주행할 수 있습니다",
                    "vi": "Xe tự lái cấp 3 có thể chạy không cần can thiệp người lái trong điều kiện hạn chế",
                    "situation": "formal"
                },
                {
                    "ko": "자율주행 중 사고 나면 누구 책임인가요?",
                    "vi": "Nếu xe tự lái tai nạn, ai chịu trách nhiệm?",
                    "situation": "onsite"
                },
                {
                    "ko": "완전 자율주행은 아직 공공도로에서 불법입니다",
                    "vi": "Xe tự lái hoàn toàn vẫn còn bất hợp pháp trên đường công cộng",
                    "situation": "formal"
                }
            ],
            "relatedTerms": ["레벨3", "제조사책임", "자율주행법", "시험운행"]
        },
        {
            "slug": "dao-duc-robot",
            "korean": "로봇윤리",
            "vietnamese": "Đạo đức robot",
            "hanja": None,
            "hanjaReading": None,
            "pronunciation": "로봇윤리",
            "meaningKo": "로봇과 AI의 설계·사용에서 지켜야 할 윤리적 원칙으로, 인간 존중·안전·투명성을 포함합니다. 통역 시 한국은 로봇윤리헌장을 제정하여 로봇의 인간 해침 금지, 인간의 로봇 통제권 보장, 로봇의 책임 소재 명확화를 규정하며, 의료·군사 로봇은 엄격한 윤리 기준을 적용하고, 로봇 권리는 인정하지 않는다는 점을 명확히 전달해야 합니다.",
            "meaningVi": "Nguyên tắc đạo đức cần tuân thủ trong thiết kế và sử dụng robot và AI, bao gồm tôn trọng con người, an toàn, minh bạch. Hàn Quốc ban hành Hiến chương đạo đức robot quy định cấm robot gây hại con người, đảm bảo quyền kiểm soát robot của con người, làm rõ trách nhiệm robot, robot y tế và quân sự áp dụng tiêu chuẩn đạo đức nghiêm ngặt, không công nhận quyền robot.",
            "context": "로봇 개발 및 AI 윤리 심사 상황에서 사용",
            "culturalNote": "한국은 2007년 세계 최초로 로봇윤리헌장을 제정했으며, 과학기술정보통신부가 관리합니다. 로봇이 인간을 대체하는 윤리적 문제, 의료 로봇의 오진 책임, 자율 살상 무기 금지 등이 논의됩니다. 베트남은 로봇 산업이 초기 단계여서 통역 시 한국의 선도적 윤리 기준을 설명해야 합니다.",
            "commonMistakes": [
                {
                    "mistake": "luật robot",
                    "correction": "đạo đức robot (윤리) vs luật (법률)",
                    "explanation": "'로봇법'은 법률이며, '로봇윤리'는 윤리 원칙으로 구분됩니다"
                },
                {
                    "mistake": "quy tắc AI",
                    "correction": "đạo đức robot (포괄적)",
                    "explanation": "'AI 규칙'은 좁으며 로봇과 AI 전체의 윤리를 포함해야 합니다"
                },
                {
                    "mistake": "nguyên tắc sử dụng robot",
                    "correction": "đạo đức robot (설계 + 사용)",
                    "explanation": "'로봇 사용 원칙'은 사용만 의미하며 설계 윤리가 누락됩니다"
                }
            ],
            "examples": [
                {
                    "ko": "로봇윤리헌장은 로봇이 인간을 해치지 말아야 한다고 규정합니다",
                    "vi": "Hiến chương đạo đức robot quy định robot không được gây hại con người",
                    "situation": "formal"
                },
                {
                    "ko": "AI 판사가 판결하면 공정한가요?",
                    "vi": "Nếu thẩm phán AI phán quyết có công bằng không?",
                    "situation": "onsite"
                },
                {
                    "ko": "의료 로봇은 오진 시 제조사가 책임을 집니다",
                    "vi": "Robot y tế chẩn đoán sai thì nhà sản xuất chịu trách nhiệm",
                    "situation": "formal"
                }
            ],
            "relatedTerms": ["AI윤리", "로봇헌장", "제조사책임", "자율살상무기"]
        },
        {
            "slug": "phan-biet-thuat-toan",
            "korean": "알고리즘차별",
            "vietnamese": "Phân biệt thuật toán",
            "hanja": None,
            "hanjaReading": None,
            "pronunciation": "알고리즘차별",
            "meaningKo": "AI 알고리즘이 인종·성별·나이 등을 이유로 불공정하게 차별하는 것을 말합니다. 통역 시 한국은 개인정보보호법으로 자동화된 결정의 거부권을 보장하며, 채용·대출·보험에서 알고리즘 차별 금지가 논의 중이고, AI 편향 감사 제도 도입 예정이며, 차별 피해 시 손해배상 청구가 가능하다는 점을 명확히 전달해야 합니다.",
            "meaningVi": "AI thuật toán phân biệt bất công vì chủng tộc, giới tính, tuổi tác. Hàn Quốc Luật bảo vệ thông tin cá nhân đảm bảo quyền từ chối quyết định tự động, đang thảo luận cấm phân biệt thuật toán trong tuyển dụng, cho vay, bảo hiểm, dự kiến đưa chế độ kiểm toán thiên lệch AI, bị thiệt hại phân biệt có thể yêu cầu bồi thường.",
            "context": "AI 공정성 심사 및 차별 피해 구제 상황에서 사용",
            "culturalNote": "한국은 AI 채용에서 여성·장애인 차별 논란이 있었고, 대출·보험에서 알고리즘 차별이 문제되며, 국가인권위원회가 AI 차별 권고안을 발표했습니다. 미국·EU는 알고리즘 차별 규제가 강화되고 있어 한국도 따라갈 전망입니다. 베트남은 AI 차별 개념이 생소해 통역 시 구체적 사례를 설명해야 합니다.",
            "commonMistakes": [
                {
                    "mistake": "AI không công bằng",
                    "correction": "phân biệt thuật toán (법적 차별)",
                    "explanation": "'AI 불공정'은 일반 표현이며 법적 차별의 개념이 약화됩니다"
                },
                {
                    "mistake": "thiên vị AI",
                    "correction": "phân biệt thuật toán (알고리즘 특화)",
                    "explanation": "'AI 편향'은 기술 용어이며 법적 차별과 구분됩니다"
                },
                {
                    "mistake": "kỳ thị bằng máy tính",
                    "correction": "phân biệt thuật toán (공식 용어)",
                    "explanation": "'컴퓨터로 차별'은 비공식적이며 법률 용어로 부적절합니다"
                }
            ],
            "examples": [
                {
                    "ko": "이 기업은 AI 채용에서 여성 지원자를 차별하여 문제가 되었습니다",
                    "vi": "Công ty này gặp vấn đề vì phân biệt ứng viên nữ trong tuyển dụng AI",
                    "situation": "formal"
                },
                {
                    "ko": "AI가 대출 거절했는데 이유를 알 수 있나요?",
                    "vi": "AI từ chối cho vay, có thể biết lý do không?",
                    "situation": "onsite"
                },
                {
                    "ko": "알고리즘 차별은 개인정보보호법 위반으로 손해배상을 청구할 수 있습니다",
                    "vi": "Phân biệt thuật toán vi phạm Luật bảo vệ thông tin cá nhân có thể yêu cầu bồi thường",
                    "situation": "formal"
                }
            ],
            "relatedTerms": ["AI편향", "자동화결정", "개인정보보호법", "공정성감사"]
        },
        {
            "slug": "deepfake",
            "korean": "딥페이크",
            "vietnamese": "Deepfake",
            "hanja": None,
            "hanjaReading": None,
            "pronunciation": "딥페이크",
            "meaningKo": "AI로 사람의 얼굴·목소리를 합성하여 가짜 영상·음성을 만드는 기술과 그 결과물을 말합니다. 통역 시 한국은 성범죄 목적 딥페이크는 5년 이하 징역으로 처벌하며, 허위정보 유포는 명예훼손죄 적용, 정치인 딥페이크는 선거법 위반, 딥페이크 탐지 기술 개발을 지원하며, 피해 영상 삭제 지원도 제공한다는 점을 명확히 전달해야 합니다.",
            "meaningVi": "Công nghệ và sản phẩm tạo video, âm thanh giả bằng cách dùng AI tổng hợp khuôn mặt, giọng nói người. Hàn Quốc deepfake vì mục đích tội phạm tình dục bị phạt tù 5 năm, phát tán thông tin sai là tội xúc phạm danh dự, deepfake chính trị vi phạm Luật bầu cử, hỗ trợ phát triển công nghệ phát hiện deepfake, cũng cung cấp hỗ trợ xóa video bị hại.",
            "context": "딥페이크 피해 신고 및 처벌 절차에서 사용",
            "culturalNote": "한국은 딥페이크 성범죄가 급증하며 2020년 처벌 규정을 신설했습니다. 연예인·정치인 딥페이크가 많아 사회 문제이며, 텔레그램 N번방 사건으로 규제가 강화되었습니다. 피해자는 영상 삭제 지원을 받을 수 있습니다. 베트남도 딥페이크가 증가하나 규제가 약해 통역 시 한국의 엄격한 처벌을 설명해야 합니다.",
            "commonMistakes": [
                {
                    "mistake": "video giả",
                    "correction": "deepfake (기술 용어)",
                    "explanation": "'가짜 영상'은 일반 조작이며 AI 합성의 특수성이 누락됩니다"
                },
                {
                    "mistake": "ghép mặt AI",
                    "correction": "deepfake (포괄적)",
                    "explanation": "'AI 얼굴 합성'은 기술 설명이며 딥페이크라는 고유 용어가 정확합니다"
                },
                {
                    "mistake": "làm giả bằng AI",
                    "correction": "deepfake (국제 표준 용어)",
                    "explanation": "'AI로 위조'는 번역이지만 딥페이크는 고유명사로 원어 사용이 원칙입니다"
                }
            ],
            "examples": [
                {
                    "ko": "성범죄 목적 딥페이크 제작·유포 시 5년 이하 징역에 처해집니다",
                    "vi": "Chế tạo/phát tán deepfake mục đích tội phạm tình dục bị phạt tù đến 5 năm",
                    "situation": "formal"
                },
                {
                    "ko": "제 얼굴로 딥페이크 만들어졌는데 어떻게 하나요?",
                    "vi": "Làm deepfake bằng mặt tôi, phải làm sao?",
                    "situation": "onsite"
                },
                {
                    "ko": "딥페이크 탐지 기술 개발이 처벌만큼 중요합니다",
                    "vi": "Phát triển công nghệ phát hiện deepfake quan trọng như xử phạt",
                    "situation": "formal"
                }
            ],
            "relatedTerms": ["AI합성", "성범죄", "명예훼손", "영상삭제"]
        },
        {
            "slug": "AI-sinh",
            "korean": "생성AI",
            "vietnamese": "AI sinh",
            "hanja": "生成AI",
            "hanjaReading": "生(날 생) + 成(이룰 성) + AI",
            "pronunciation": "생성에이아이",
            "meaningKo": "텍스트·이미지·영상·음악 등을 자동으로 생성하는 AI를 말합니다. 통역 시 한국은 생성AI의 저작권 귀속이 불명확하여 논란이 있으며, AI 학습 데이터의 저작권 침해 여부, 생성물의 진위 표시 의무, 허위정보 생성 시 책임, 개인정보 유출 위험 등이 규제 과제이고, AI 저작물 등록 제도 도입을 검토 중이라는 점을 명확히 전달해야 합니다.",
            "meaningVi": "AI tự động tạo văn bản, hình ảnh, video, âm nhạc. Ở Hàn Quốc quy định quyền tác giả của AI sinh không rõ ràng nên có tranh cãi, vi phạm bản quyền dữ liệu học AI, nghĩa vụ ghi nhãn sản phẩm AI, trách nhiệm khi tạo thông tin sai, nguy cơ rò rỉ thông tin cá nhân là vấn đề quy định, đang xem xét đưa chế độ đăng ký tác phẩm AI.",
            "context": "생성AI 서비스 개발 및 저작권 분쟁 상황에서 사용",
            "culturalNote": "한국은 ChatGPT·Midjourney 등 생성AI가 확산되며 규제 필요성이 대두되었습니다. 저작권법은 AI를 저작자로 인정하지 않아 생성물의 저작권이 불명확하며, AI 학습 데이터의 저작권 침해 논란도 큽니다. 정부는 AI 진흥과 규제의 균형을 모색 중입니다. 베트남은 생성AI 규제가 없어 통역 시 한국의 논의 현황을 설명해야 합니다.",
            "commonMistakes": [
                {
                    "mistake": "AI tạo",
                    "correction": "AI sinh (공식 용어)",
                    "explanation": "'AI 만들기'는 일상 표현이며 법률 용어로 '생성AI'가 정확합니다"
                },
                {
                    "mistake": "trí tuệ nhân tạo sáng tạo",
                    "correction": "AI sinh (간결)",
                    "explanation": "'창의 인공지능'은 장황하며 '생성AI'가 간결하고 표준적입니다"
                },
                {
                    "mistake": "ChatGPT",
                    "correction": "AI sinh (포괄) - ChatGPT는 예시",
                    "explanation": "ChatGPT는 생성AI의 한 예시이며 전체를 대표하지 못합니다"
                }
            ],
            "examples": [
                {
                    "ko": "생성AI가 만든 작품의 저작권은 아직 법적으로 불명확합니다",
                    "vi": "Quyền tác giả tác phẩm do AI sinh tạo vẫn chưa rõ ràng về mặt pháp lý",
                    "situation": "formal"
                },
                {
                    "ko": "AI로 그린 그림을 팔아도 되나요?",
                    "vi": "Bán tranh vẽ bằng AI được không?",
                    "situation": "onsite"
                },
                {
                    "ko": "생성AI 학습에 사용된 데이터의 저작권 침해 여부가 쟁점입니다",
                    "vi": "Vi phạm bản quyền dữ liệu dùng cho học AI sinh là điểm tranh luận",
                    "situation": "formal"
                }
            ],
            "relatedTerms": ["ChatGPT", "AI저작권", "학습데이터", "허위정보"]
        },
        {
            "slug": "chu-quyen-du-lieu",
            "korean": "데이터주권",
            "vietnamese": "Chủ quyền dữ liệu",
            "hanja": None,
            "hanjaReading": None,
            "pronunciation": "데이터주권",
            "meaningKo": "국가가 자국민의 데이터에 대한 통제권과 관할권을 행사하는 것을 말합니다. 통역 시 한국은 개인정보의 해외 이전을 규제하며, 중요 데이터는 국내 저장 의무화를 검토 중이고, 외국 기업도 한국법 적용, 클라우드법으로 공공기관 데이터 국내 저장 의무화, EU GDPR과 유사한 규제 강화 중이라는 점을 명확히 전달해야 합니다.",
            "meaningVi": "Quốc gia thực thi quyền kiểm soát và quyền tài phán đối với dữ liệu công dân. Hàn Quốc quy định chuyển thông tin cá nhân ra nước ngoài, đang xem xét bắt buộc lưu trữ dữ liệu quan trọng trong nước, công ty nước ngoài cũng áp dụng luật Hàn Quốc, Luật đám mây bắt buộc cơ quan công quyền lưu trữ dữ liệu trong nước, đang tăng cường quy định tương tự EU GDPR.",
            "context": "데이터 국외 이전 및 클라우드 규제 상황에서 사용",
            "culturalNote": "한국은 개인정보보호법으로 데이터 해외 이전을 규제하며, 최근 데이터 주권 논의가 활발합니다. 중국은 강력한 데이터 주권 정책으로 외국 기업을 규제하며, EU도 GDPR로 역외 적용을 강화하고 있습니다. 한국도 클라우드법 제정으로 공공 데이터 국내 저장을 의무화했습니다. 베트남은 사이버보안법으로 데이터 국내 저장을 요구해 통역 시 양국 규제를 비교 설명해야 합니다.",
            "commonMistakes": [
                {
                    "mistake": "quyền dữ liệu",
                    "correction": "chủ quyền dữ liệu (국가 주권)",
                    "explanation": "'데이터 권리'는 개인 권리처럼 들리며 국가 주권의 의미가 누락됩니다"
                },
                {
                    "mistake": "bảo vệ dữ liệu",
                    "correction": "chủ quyền dữ liệu (주권 개념)",
                    "explanation": "'데이터 보호'는 보안이며 주권의 정치적 개념이 약화됩니다"
                },
                {
                    "mistake": "kiểm soát thông tin",
                    "correction": "chủ quyền dữ liệu (국가 차원)",
                    "explanation": "'정보 통제'는 일반 관리이며 국가 주권의 법적 성격이 누락됩니다"
                }
            ],
            "examples": [
                {
                    "ko": "개인정보를 해외로 이전하려면 별도 동의를 받아야 합니다",
                    "vi": "Chuyển thông tin cá nhân ra nước ngoài phải có đồng ý riêng",
                    "situation": "formal"
                },
                {
                    "ko": "외국 클라우드에 데이터 저장해도 되나요?",
                    "vi": "Lưu dữ liệu trên đám mây nước ngoài được không?",
                    "situation": "onsite"
                },
                {
                    "ko": "데이터 주권은 국가안보와 개인정보 보호를 위해 중요합니다",
                    "vi": "Chủ quyền dữ liệu quan trọng để bảo vệ an ninh quốc gia và thông tin cá nhân",
                    "situation": "formal"
                }
            ],
            "relatedTerms": ["클라우드법", "데이터이전", "GDPR", "국내저장"]
        },
        {
            "slug": "nen-tang-so",
            "korean": "디지털플랫폼",
            "vietnamese": "Nền tảng số",
            "hanja": None,
            "hanjaReading": None,
            "pronunciation": "디지털플랫폼",
            "meaningKo": "온라인으로 상품·서비스·정보를 중개하는 플랫폼 사업을 말합니다. 통역 시 한국은 플랫폼 규제법(온라인플랫폼법) 제정을 추진하며, 지배적 플랫폼은 공정거래법 적용, 앱마켓 수수료 규제, 검색 순위 조작 금지, 이용자 정보 보호 강화, 플랫폼 노동자 보호도 논의 중이라는 점을 명확히 전달해야 합니다.",
            "meaningVi": "Kinh doanh nền tảng trung gian hàng hóa, dịch vụ, thông tin trực tuyến. Hàn Quốc đang thúc đẩy Luật quy định nền tảng (Luật nền tảng trực tuyến), nền tảng chi phối áp dụng Luật cạnh tranh công bằng, quy định phí chợ ứng dụng, cấm thao túng thứ hạng tìm kiếm, tăng cường bảo vệ thông tin người dùng, cũng đang thảo luận bảo vệ lao động nền tảng.",
            "context": "플랫폼 사업자 규제 및 이용자 보호 상황에서 사용",
            "culturalNote": "한국은 네이버·카카오·쿠팡 등 대형 플랫폼이 시장을 지배하며, 공정위가 갑질·끼워팔기를 규제하고 있습니다. 배달·택시 플랫폼 노동자 보호도 쟁점이며, 구글·애플 앱마켓 수수료 30% 논란으로 규제가 강화되었습니다. 베트남도 플랫폼 경제가 성장 중이나 규제가 약해 통역 시 한국의 규제 강화 추세를 설명해야 합니다.",
            "commonMistakes": [
                {
                    "mistake": "nền tảng internet",
                    "correction": "nền tảng số (디지털 포괄)",
                    "explanation": "'인터넷 플랫폼'은 좁으며 앱·모바일도 포함하는 '디지털플랫폼'이 정확합니다"
                },
                {
                    "mistake": "công ty công nghệ",
                    "correction": "nền tảng số (중개 사업)",
                    "explanation": "'기술회사'는 포괄적이며 중개 플랫폼의 특수성이 약화됩니다"
                },
                {
                    "mistake": "trang web",
                    "correction": "nền tảng số (사업 모델)",
                    "explanation": "'웹사이트'는 기술이며 플랫폼 비즈니스 모델의 의미가 누락됩니다"
                }
            ],
            "examples": [
                {
                    "ko": "지배적 플랫폼은 공정거래법상 특별한 규제를 받습니다",
                    "vi": "Nền tảng chi phối chịu quy định đặc biệt theo Luật cạnh tranh công bằng",
                    "situation": "formal"
                },
                {
                    "ko": "앱마켓 수수료가 너무 높은데 규제 안 되나요?",
                    "vi": "Phí chợ ứng dụng quá cao, không quy định à?",
                    "situation": "onsite"
                },
                {
                    "ko": "플랫폼 노동자의 권리 보호가 새로운 과제입니다",
                    "vi": "Bảo vệ quyền lợi lao động nền tảng là vấn đề mới",
                    "situation": "formal"
                }
            ],
            "relatedTerms": ["온라인플랫폼법", "지배적사업자", "플랫폼노동", "공정거래법"]
        },
        {
            "slug": "du-lieu-lon",
            "korean": "빅데이터",
            "vietnamese": "Dữ liệu lớn",
            "hanja": None,
            "hanjaReading": None,
            "pronunciation": "빅데이터",
            "meaningKo": "대량의 정형·비정형 데이터를 수집·저장·분석하여 가치를 창출하는 것을 말합니다. 통역 시 한국은 개인정보 비식별 처리 시 활용 가능하며, 가명정보는 동의 없이 연구·통계 목적 사용 가능, 빅데이터 오남용 시 처벌, 공공 빅데이터 개방 정책 추진, 의료·금융 빅데이터 활용 규제 완화 중이라는 점을 명확히 전달해야 합니다.",
            "meaningVi": "Thu thập, lưu trữ, phân tích dữ liệu lớn có cấu trúc và phi cấu trúc để tạo giá trị. Hàn Quốc khi xử lý phi nhận dạng thông tin cá nhân có thể khai thác, thông tin giả danh có thể dùng vì mục đích nghiên cứu/thống kê không cần đồng ý, lạm dụng dữ liệu lớn sẽ bị phạt, thúc đẩy chính sách mở dữ liệu lớn công, đang nới lỏng quy định khai thác dữ liệu lớn y tế, tài chính.",
            "context": "빅데이터 활용 및 개인정보 보호 상황에서 사용",
            "culturalNote": "한국은 빅데이터 산업 육성을 위해 2020년 개인정보보호법을 개정하여 가명정보 개념을 도입했습니다. 의료·금융·통신 빅데이터를 결합하여 활용하는 사업이 증가하고 있으며, 정부는 공공 빅데이터를 개방하고 있습니다. 베트남은 빅데이터 규제가 없어 통역 시 한국의 가명정보 제도를 설명해야 합니다.",
            "commonMistakes": [
                {
                    "mistake": "dữ liệu khổng lồ",
                    "correction": "dữ liệu lớn (빅데이터)",
                    "explanation": "'거대 데이터'는 직역이며 '빅데이터'라는 고유 용어가 더 정확합니다"
                },
                {
                    "mistake": "big data",
                    "correction": "dữ liệu lớn (베트남어 용어)",
                    "explanation": "영어를 그대로 쓰지 말고 베트남어로 번역해야 합니다"
                },
                {
                    "mistake": "thông tin lớn",
                    "correction": "dữ liệu lớn (데이터)",
                    "explanation": "'큰 정보'는 모호하며 '데이터'와 '정보'를 구분해야 합니다"
                }
            ],
            "examples": [
                {
                    "ko": "가명정보는 개인 동의 없이 빅데이터로 활용할 수 있습니다",
                    "vi": "Thông tin giả danh có thể khai thác làm dữ liệu lớn không cần đồng ý cá nhân",
                    "situation": "formal"
                },
                {
                    "ko": "제 정보가 빅데이터로 쓰이나요?",
                    "vi": "Thông tin của tôi có dùng làm dữ liệu lớn không?",
                    "situation": "onsite"
                },
                {
                    "ko": "빅데이터 활용은 개인정보 보호와 균형을 이루어야 합니다",
                    "vi": "Khai thác dữ liệu lớn phải cân bằng với bảo vệ thông tin cá nhân",
                    "situation": "formal"
                }
            ],
            "relatedTerms": ["가명정보", "비식별화", "데이터결합", "개인정보보호"]
        },
        {
            "slug": "luat-blockchain",
            "korean": "블록체인법",
            "vietnamese": "Luật blockchain",
            "hanja": None,
            "hanjaReading": None,
            "pronunciation": "블록체인법",
            "meaningKo": "블록체인 기술과 암호화폐를 규율하는 법률을 말합니다. 통역 시 한국은 가상자산법으로 거래소를 규제하며, ICO(코인공개)는 사실상 금지, 가상자산 과세 추진 중, 블록체인 기술 진흥은 지원하지만 암호화폐 투기는 규제, NFT·DeFi 등 신규 서비스는 규제 공백이라는 점을 명확히 전달해야 합니다.",
            "meaningVi": "Luật quy định công nghệ blockchain và tiền mã hóa. Hàn Quốc Luật tài sản ảo quy định sàn giao dịch, ICO (công khai coin) trên thực tế bị cấm, đang thúc đẩy đánh thuế tài sản ảo, hỗ trợ xúc tiến công nghệ blockchain nhưng quy định đầu cơ tiền mã hóa, dịch vụ mới như NFT, DeFi là khoảng trống quy định.",
            "context": "가상자산 거래 및 블록체인 사업 규제 상황에서 사용",
            "culturalNote": "한국은 암호화폐 투기 열풍 이후 규제를 강화했으며, 2021년 가상자산법(특금법)으로 거래소에 실명 계좌를 의무화했습니다. 비트코인·이더리움 등은 합법이지만 ICO는 금지되어 해외에서 발행 후 상장하는 우회 방식이 사용됩니다. 베트남은 암호화폐를 금지하여 통역 시 양국의 큰 차이를 설명해야 합니다.",
            "commonMistakes": [
                {
                    "mistake": "luật tiền ảo",
                    "correction": "luật blockchain (기술 + 자산)",
                    "explanation": "'가상화폐법'은 화폐만 의미하며 블록체인 기술이 누락됩니다"
                },
                {
                    "mistake": "quy định Bitcoin",
                    "correction": "luật blockchain (포괄)",
                    "explanation": "'비트코인 규정'은 특정 코인만 지칭하며 전체 블록체인 규율을 포함하지 못합니다"
                },
                {
                    "mistake": "luật công nghệ phân tán",
                    "correction": "luật blockchain (표준 용어)",
                    "explanation": "'분산기술법'은 기술 명칭이며 '블록체인법'이 표준 용어입니다"
                }
            ],
            "examples": [
                {
                    "ko": "가상자산 거래소는 금융당국에 신고하고 실명 계좌를 발급받아야 합니다",
                    "vi": "Sàn giao dịch tài sản ảo phải khai báo cơ quan tài chính và cấp tài khoản thực danh",
                    "situation": "formal"
                },
                {
                    "ko": "ICO 하려면 어떻게 하나요?",
                    "vi": "Muốn ICO thì làm sao?",
                    "situation": "onsite"
                },
                {
                    "ko": "블록체인 기술은 진흥하되 암호화폐 투기는 규제합니다",
                    "vi": "Xúc tiến công nghệ blockchain nhưng quy định đầu cơ tiền mã hóa",
                    "situation": "formal"
                }
            ],
            "relatedTerms": ["가상자산법", "ICO", "NFT", "암호화폐"]
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
    print(f"✅ Added {len(filtered)} terms (AI/기술규제). Total: {len(data)}")

if __name__ == '__main__':
    main()
