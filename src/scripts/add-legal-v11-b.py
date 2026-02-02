#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""선거법/정당법 용어 추가 (v11-B)"""
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
            "slug": "ung-cu-vien",
            "korean": "후보자",
            "vietnamese": "Ứng cử viên",
            "hanja": "候補者",
            "hanjaReading": "候(뒤 후) + 補(기울 보) + 者(놈 자)",
            "pronunciation": "후보자",
            "meaningKo": "선거에 출마하여 당선을 목표로 하는 사람을 의미합니다. 통역 시 주의할 점은 베트남에서는 공산당이 추천한 후보자와 자천 후보자를 명확히 구분한다는 점입니다. 한국의 다당제 선거와 달리 베트남은 국회의원 선거에서도 공산당의 승인이 필요하므로, '후보 등록' 절차나 '경선' 개념이 다릅니다. 선거 관련 통역에서는 양국의 정치 제도 차이를 설명해야 오해를 방지할 수 있습니다.",
            "meaningVi": "Người tham gia tranh cử trong một cuộc bầu cử với mục tiêu được bầu vào vị trí dân cử. Ở Việt Nam, ứng cử viên có thể do Đảng Cộng sản đề cử hoặc tự ứng cử, nhưng đều phải được Ủy ban bầu cử phê duyệt.",
            "context": "선거 실무, 선거 보도, 정치 토론",
            "culturalNote": "한국은 정당 공천을 받거나 무소속으로 자유롭게 출마할 수 있는 다당제 국가입니다. 베트남은 공산당이 후보자 선정 과정에 깊이 관여하며, 국회의원 후보자는 조국전선(Mặt trận Tổ quốc)의 심사를 거쳐야 합니다. 따라서 '후보자 난립', '경선', '공천 갈등' 같은 한국 정치 용어를 베트남 통역사가 직역하면 현실과 맞지 않을 수 있습니다.",
            "commonMistakes": [
                {
                    "mistake": "Ứng viên를 후보자로 번역",
                    "correction": "Ứng cử viên이 정확한 표현",
                    "explanation": "Ứng viên은 일반 지원자(입사 지원 등)를 뜻하고, 선거 출마자는 Ứng cử viên입니다"
                },
                {
                    "mistake": "후보 등록을 Đăng ký ứng viên로 번역",
                    "correction": "Đăng ký ứng cử가 정확",
                    "explanation": "선거 출마 등록은 ứng cử라는 동사를 써야 합니다"
                },
                {
                    "mistake": "예비후보를 Ứng cử viên dự bị로 직역",
                    "correction": "Ứng cử viên tiềm năng 또는 설명 추가",
                    "explanation": "한국 선거법의 예비후보 제도는 베트남에 없으므로 개념 설명이 필요합니다"
                }
            ],
            "examples": [
                {
                    "ko": "이번 총선에는 300명이 넘는 후보자가 등록했습니다.",
                    "vi": "Kỳ bầu cử quốc hội này có hơn 300 ứng cử viên đăng ký.",
                    "situation": "formal"
                },
                {
                    "ko": "후보자 토론회가 다음 주에 열립니다.",
                    "vi": "Buổi tranh luận giữa các ứng cử viên sẽ diễn ra vào tuần tới.",
                    "situation": "formal"
                },
                {
                    "ko": "그는 무소속 후보로 출마했습니다.",
                    "vi": "Anh ấy ra tranh cử với tư cách ứng cử viên độc lập.",
                    "situation": "informal"
                }
            ],
            "relatedTerms": ["선거", "공천", "입후보", "당선", "득표"]
        },
        {
            "slug": "phieu-bau",
            "korean": "투표",
            "vietnamese": "Phiếu bầu",
            "hanja": "投票",
            "hanjaReading": "投(던질 투) + 票(표 표)",
            "pronunciation": "투표",
            "meaningKo": "선거에서 유권자가 자신의 의사를 표시하는 행위를 말합니다. 통역 시 주의할 점은 '투표하다'(Bỏ phiếu)와 '투표용지'(Phiếu bầu)를 구분해야 한다는 것입니다. 한국은 전자투표 도입 논의가 있지만 베트남은 여전히 종이 투표용지를 사용하며, 사전투표 제도도 제한적입니다. 부재자 투표나 선상 투표 같은 제도는 양국이 다르므로, 선거 관련 통역에서는 제도적 배경을 함께 설명해야 합니다.",
            "meaningVi": "Hành động thể hiện ý chí của cử tri trong cuộc bầu cử, hoặc tờ giấy dùng để bỏ phiếu. Việt Nam vẫn sử dụng phiếu bầu giấy và có quy định nghiêm ngặt về bảo mật phiếu bầu.",
            "context": "선거 당일, 투표소 운영, 개표",
            "culturalNote": "한국은 사전투표가 보편화되어 있고, 일부 지역에서는 전자 개표 시스템을 사용합니다. 베트남은 투표일 당일에만 투표가 가능하며, 군인이나 해외 거주자를 위한 부재자 투표는 특별 절차를 거쳐야 합니다. 또한 베트남은 투표율이 90%를 넘는 경우가 많아, 한국의 낮은 투표율을 설명할 때 문화적 차이를 언급해야 합니다.",
            "commonMistakes": [
                {
                    "mistake": "투표하다를 Phiếu bầu로 번역",
                    "correction": "Bỏ phiếu가 동사 표현",
                    "explanation": "Phiếu bầu는 명사(투표용지)이고, 투표 행위는 Bỏ phiếu입니다"
                },
                {
                    "mistake": "사전투표를 Bỏ phiếu trước로 직역",
                    "correction": "Bỏ phiếu sớm 또는 제도 설명 추가",
                    "explanation": "베트남에는 한국식 사전투표 제도가 없으므로 개념 설명 필요"
                },
                {
                    "mistake": "전자투표를 Phiếu điện tử로 번역",
                    "correction": "Bỏ phiếu điện tử가 더 자연스러움",
                    "explanation": "투표 행위를 나타낼 때는 동사구 형태가 적절합니다"
                }
            ],
            "examples": [
                {
                    "ko": "투표는 오전 6시부터 오후 6시까지입니다.",
                    "vi": "Thời gian bỏ phiếu từ 6 giờ sáng đến 6 giờ chiều.",
                    "situation": "formal"
                },
                {
                    "ko": "투표용지를 잘못 작성하면 무효표가 됩니다.",
                    "vi": "Nếu ghi sai vào phiếu bầu sẽ trở thành phiếu không hợp lệ.",
                    "situation": "onsite"
                },
                {
                    "ko": "이번 선거 투표율이 60%를 넘었습니다.",
                    "vi": "Tỷ lệ đi bỏ phiếu trong cuộc bầu cử này đã vượt 60%.",
                    "situation": "formal"
                }
            ],
            "relatedTerms": ["투표소", "투표함", "개표", "선거", "무효표"]
        },
        {
            "slug": "dang-phai",
            "korean": "정당",
            "vietnamese": "Đảng phái",
            "hanja": "政黨",
            "hanjaReading": "政(정사 정) + 黨(무리 당)",
            "pronunciation": "정당",
            "meaningKo": "공동의 정치적 이념과 목표를 가진 사람들이 결성한 조직을 의미합니다. 통역 시 가장 주의해야 할 점은 한국은 다당제 민주주의 국가이지만, 베트남은 공산당 일당 체제라는 근본적 차이입니다. 한국의 '야당', '여당', '제3당' 같은 용어는 베트남 정치 구조에서는 의미가 없습니다. 정치 관련 통역에서는 양국의 정치 제도를 이해하고, 직역보다는 맥락에 맞는 설명을 추가해야 합니다.",
            "meaningVi": "Tổ chức chính trị được hình thành bởi những người có chung lý tưởng và mục tiêu chính trị. Ở Việt Nam, Đảng Cộng sản Việt Nam là đảng duy nhất lãnh đạo Nhà nước theo Hiến pháp.",
            "context": "정치 제도 설명, 국제 비교, 역사 교육",
            "culturalNote": "한국은 보수·진보 정당이 경쟁하는 다당제 국가로, 정권 교체가 선거를 통해 이루어집니다. 베트남은 공산당이 헌법상 유일한 집권당이며, '정당 간 경쟁'이라는 개념 자체가 존재하지 않습니다. 따라서 한국 정치 뉴스를 베트남어로 통역할 때는 '야당'(đảng đối lập)이라는 용어가 베트남에서는 존재하지 않는 개념임을 인식해야 합니다.",
            "commonMistakes": [
                {
                    "mistake": "정당을 Đảng로만 번역",
                    "correction": "Đảng phái 또는 Chính đảng이 더 정확",
                    "explanation": "Đảng만 쓰면 베트남에서는 공산당을 지칭하는 것으로 오해될 수 있습니다"
                },
                {
                    "mistake": "여당·야당을 직역해서 설명 없이 사용",
                    "correction": "Đảng cầm quyền / Đảng đối lập + 한국 정치 제도 설명 추가",
                    "explanation": "베트남은 일당제이므로 이 개념이 낯설어 맥락 설명이 필수입니다"
                },
                {
                    "mistake": "정당 공천을 Đảng phái đề cử로만 번역",
                    "correction": "Đề cử của đảng (한국 맥락) 또는 추가 설명",
                    "explanation": "베트남의 후보 추천 방식과 다르므로 제도 차이를 명확히 해야 합니다"
                }
            ],
            "examples": [
                {
                    "ko": "한국에는 여러 정당이 있어 유권자가 선택할 수 있습니다.",
                    "vi": "Ở Hàn Quốc có nhiều chính đảng để cử tri lựa chọn.",
                    "situation": "formal"
                },
                {
                    "ko": "그는 어느 정당 소속입니까?",
                    "vi": "Anh ấy thuộc đảng phái nào?",
                    "situation": "informal"
                },
                {
                    "ko": "새로운 정당이 창당 준비를 하고 있습니다.",
                    "vi": "Một chính đảng mới đang chuẩn bị thành lập.",
                    "situation": "formal"
                }
            ],
            "relatedTerms": ["여당", "야당", "공천", "당원", "정치"]
        },
        {
            "slug": "chien-dich-tranh-cu",
            "korean": "선거운동",
            "vietnamese": "Chiến dịch tranh cử",
            "hanja": "選擧運動",
            "hanjaReading": "選(가릴 선) + 擧(들 거) + 運(옮길 운) + 動(움직일 동)",
            "pronunciation": "선거운동",
            "meaningKo": "후보자나 정당이 유권자의 지지를 얻기 위해 펼치는 모든 활동을 말합니다. 통역 시 주의할 점은 한국은 선거운동 기간이 법으로 정해져 있고(공식 선거운동 기간), SNS·인터넷 선거운동도 엄격히 규제된다는 점입니다. 베트남은 선거운동 방식이 제한적이며, 대부분 공식 집회나 인쇄물 배포로 진행됩니다. '네거티브 캠페인', '표밭 관리', '지역구 순회' 같은 한국 선거 용어는 베트남 맥락에 맞게 재해석해야 합니다.",
            "meaningVi": "Các hoạt động mà ứng cử viên hoặc đảng phái thực hiện để giành được sự ủng hộ của cử tri. Ở Việt Nam, chiến dịch tranh cử được quản lý chặt chẽ và chủ yếu thông qua các buổi tiếp xúc cử tri và tài liệu tuyên truyền chính thức.",
            "context": "선거 캠페인, 정치 홍보, 선거법 해설",
            "culturalNote": "한국은 선거운동 기간 동안 대형 집회, TV 토론, 거리 유세, SNS 홍보 등 다양한 방식이 허용됩니다. 베트남은 선거운동이 조국전선 주최 행사나 공식 홍보물 위주로 진행되며, 개인적인 대규모 유세는 드뭅니다. 또한 한국의 '선거 벽보', '선거 공보', '후보자 홍보물' 같은 개념이 베트남에서는 형태가 다르므로 설명이 필요합니다.",
            "commonMistakes": [
                {
                    "mistake": "선거운동을 Vận động bầu cử로 번역",
                    "correction": "Chiến dịch tranh cử가 더 자연스러움",
                    "explanation": "Vận động bầu cử는 직역이고, Chiến dịch tranh cử가 실제로 많이 쓰이는 표현입니다"
                },
                {
                    "mistake": "유세를 Diễn thuyết로만 번역",
                    "correction": "Vận động tranh cử trên đường phố 등 구체적 설명",
                    "explanation": "한국의 거리 유세 문화는 베트남에 없으므로 추가 설명 필요"
                },
                {
                    "mistake": "선거 벽보를 Áp phích bầu cử로 직역",
                    "correction": "Poster ứng cử viên 또는 Tài liệu tuyên truyền",
                    "explanation": "베트남 선거에서는 벽보 형태가 다르므로 실제 사용 방식 설명 필요"
                }
            ],
            "examples": [
                {
                    "ko": "공식 선거운동 기간은 2주입니다.",
                    "vi": "Thời gian chiến dịch tranh cử chính thức là 2 tuần.",
                    "situation": "formal"
                },
                {
                    "ko": "후보자들이 시장에서 선거운동을 하고 있습니다.",
                    "vi": "Các ứng cử viên đang vận động tranh cử tại chợ.",
                    "situation": "onsite"
                },
                {
                    "ko": "불법 선거운동으로 고발당했습니다.",
                    "vi": "Bị tố cáo về hành vi vận động tranh cử bất hợp pháp.",
                    "situation": "formal"
                }
            ],
            "relatedTerms": ["공보", "벽보", "유세", "선거법", "후보자"]
        },
        {
            "slug": "quyen-bau-cu",
            "korean": "선거권",
            "vietnamese": "Quyền bầu cử",
            "hanja": "選擧權",
            "hanjaReading": "選(가릴 선) + 擧(들 거) + 權(권세 권)",
            "pronunciation": "선거권",
            "meaningKo": "국민이 선거에서 투표할 수 있는 권리를 의미합니다. 통역 시 주의할 점은 선거권 연령이 한국은 만 18세, 베트남도 만 18세이지만, 피선거권 연령은 직위에 따라 다르다는 점입니다. 한국은 지역구 국회의원 피선거권이 만 25세, 대통령은 만 40세인 반면, 베트남은 국회의원이 만 21세부터 가능합니다. 법정 통역에서 선거권 관련 사건을 다룰 때는 양국의 법적 기준 차이를 명확히 전달해야 합니다.",
            "meaningVi": "Quyền của công dân được tham gia bỏ phiếu trong cuộc bầu cử. Ở Việt Nam, công dân từ đủ 18 tuổi trở lên có quyền bầu cử, và từ 21 tuổi có thể ứng cử đại biểu Quốc hội.",
            "context": "헌법 교육, 시민권 논의, 선거법 해설",
            "culturalNote": "한국과 베트남 모두 보통선거 원칙을 따르지만, 피선거권 연령 기준이 다릅니다. 한국은 대통령 피선거권이 만 40세로 높은 편이고, 베트남은 국회의원 피선거권이 만 21세로 상대적으로 낮습니다. 또한 한국은 재외국민 투표권이 보장되지만, 베트남은 해외 거주자의 투표가 제한적입니다. 선거권 관련 통역 시 이러한 차이를 설명해야 오해를 줄일 수 있습니다.",
            "commonMistakes": [
                {
                    "mistake": "선거권을 Quyền bầu로만 번역",
                    "correction": "Quyền bầu cử가 완전한 표현",
                    "explanation": "Quyền bầu는 불완전한 표현이고, 법률 용어로는 Quyền bầu cử를 써야 합니다"
                },
                {
                    "mistake": "피선거권을 직역 없이 생략",
                    "correction": "Quyền ứng cử 또는 Quyền được bầu cử",
                    "explanation": "선거권과 피선거권은 다른 개념이므로 구분해서 번역해야 합니다"
                },
                {
                    "mistake": "재외국민 투표권을 직역만 사용",
                    "correction": "Quyền bầu cử của công dân ở nước ngoài + 제도 설명",
                    "explanation": "베트남은 해외 투표 제도가 제한적이므로 한국 제도 설명 필요"
                }
            ],
            "examples": [
                {
                    "ko": "만 18세가 되면 선거권을 갖습니다.",
                    "vi": "Khi đủ 18 tuổi sẽ có quyền bầu cử.",
                    "situation": "formal"
                },
                {
                    "ko": "선거권은 헌법이 보장하는 기본권입니다.",
                    "vi": "Quyền bầu cử là quyền cơ bản được Hiến pháp bảo đảm.",
                    "situation": "formal"
                },
                {
                    "ko": "그는 선거권이 박탈되었습니다.",
                    "vi": "Anh ta bị tước quyền bầu cử.",
                    "situation": "formal"
                }
            ],
            "relatedTerms": ["피선거권", "투표", "공민권", "헌법", "유권자"]
        },
        {
            "slug": "kiem-phieu",
            "korean": "개표",
            "vietnamese": "Kiểm phiếu",
            "hanja": "開票",
            "hanjaReading": "開(열 개) + 票(표 표)",
            "pronunciation": "개표",
            "meaningKo": "투표가 끝난 후 투표함을 열어 득표 결과를 집계하는 과정을 말합니다. 통역 시 주의할 점은 한국은 전자 개표기를 일부 사용하지만 베트남은 수작업 개표가 대부분이라는 점입니다. 또한 한국은 개표 과정이 공개되고 참관인 제도가 엄격히 운영되는 반면, 베트남도 개표 참관은 있지만 절차가 다릅니다. 선거 통역 시 '개표소', '개표 참관', '개표 방송' 같은 용어는 양국의 실제 운영 방식 차이를 고려해 설명해야 합니다.",
            "meaningVi": "Quá trình mở hòm phiếu và tính phiếu bầu sau khi bỏ phiếu kết thúc. Ở Việt Nam, kiểm phiếu chủ yếu được thực hiện thủ công với sự giám sát của Ủy ban bầu cử và đại diện các tổ chức.",
            "context": "선거 당일, 선거 보도, 개표 작업",
            "culturalNote": "한국은 선거 당일 밤에 개표 결과가 대부분 나오며, TV에서 실시간 개표 방송을 합니다. 베트남도 선거일에 개표하지만, 결과 발표는 더 신중하게 진행되며 언론 보도 방식도 다릅니다. 한국은 출구조사 결과를 먼저 발표해 사실상 당락을 예측하지만, 베트남은 출구조사 문화가 없습니다. 개표 관련 통역 시 이러한 절차 차이를 명확히 전달해야 합니다.",
            "commonMistakes": [
                {
                    "mistake": "개표를 Mở phiếu로 번역",
                    "correction": "Kiểm phiếu 또는 Đếm phiếu가 정확",
                    "explanation": "Mở phiếu는 '열다'는 뜻이고, 집계 과정은 Kiểm phiếu입니다"
                },
                {
                    "mistake": "개표소를 Phòng mở phiếu로 직역",
                    "correction": "Điểm kiểm phiếu 또는 Trung tâm kiểm phiếu",
                    "explanation": "공식 용어는 Điểm kiểm phiếu이며 장소를 나타낼 때 쓰입니다"
                },
                {
                    "mistake": "전자개표를 직역 없이 생략",
                    "correction": "Kiểm phiếu điện tử + 한국 시스템 설명",
                    "explanation": "베트남은 전자개표가 거의 없으므로 개념 설명 필요"
                }
            ],
            "examples": [
                {
                    "ko": "개표는 투표 마감 즉시 시작됩니다.",
                    "vi": "Kiểm phiếu bắt đầu ngay sau khi đóng cửa bỏ phiếu.",
                    "situation": "formal"
                },
                {
                    "ko": "개표 결과가 자정쯤 나올 예정입니다.",
                    "vi": "Kết quả kiểm phiếu dự kiến công bố vào khoảng nửa đêm.",
                    "situation": "formal"
                },
                {
                    "ko": "개표 과정에서 의문 투표가 발견되었습니다.",
                    "vi": "Trong quá trình kiểm phiếu phát hiện phiếu bầu đáng ngờ.",
                    "situation": "onsite"
                }
            ],
            "relatedTerms": ["투표", "개표소", "득표", "참관인", "선거관리위원회"]
        },
        {
            "slug": "dan-nguyen",
            "korean": "당원",
            "vietnamese": "Đảng viên",
            "hanja": "黨員",
            "hanjaReading": "黨(무리 당) + 員(인원 원)",
            "pronunciation": "당원",
            "meaningKo": "정당에 가입하여 활동하는 구성원을 의미합니다. 통역 시 주의할 점은 한국의 당원은 정당 가입비와 당비를 내고 자유롭게 입당·탈당할 수 있지만, 베트남의 당원(공산당원)은 엄격한 심사를 거쳐 선발되며 특권과 의무를 동시에 지닌다는 점입니다. 한국에서 '당원'은 단순 정치 참여자를 뜻하지만, 베트남에서 '당원'은 사회적 지위와 책임을 상징합니다. 정치 관련 통역에서는 이 차이를 명확히 설명해야 오해를 방지할 수 있습니다.",
            "meaningVi": "Thành viên của một đảng chính trị. Ở Việt Nam, đảng viên Đảng Cộng sản được tuyển chọn qua quá trình thẩm định nghiêm ngặt và có nghĩa vụ, trách nhiệm cao trong xã hội.",
            "context": "정당 활동, 정치 조직, 당내 경선",
            "culturalNote": "한국의 당원은 정당 지지자로서 자유롭게 가입·탈퇴하며, 당비 납부 외에 특별한 의무는 없습니다. 베트남의 공산당원은 입당 과정이 까다롭고, 당원 자격은 공직 진출이나 사회적 신뢰의 상징이 됩니다. 한국의 '당원 모집 캠페인'이나 '당원 권리 강화' 같은 용어는 베트남 맥락에서는 의미가 다르므로, 통역 시 제도 차이를 설명해야 합니다.",
            "commonMistakes": [
                {
                    "mistake": "당원을 Đảng viên으로만 번역하고 맥락 설명 생략",
                    "correction": "한국 정당의 당원임을 명시 (Đảng viên của đảng chính trị Hàn Quốc)",
                    "explanation": "베트남에서 Đảng viên은 공산당원을 의미하므로 혼동 방지 필요"
                },
                {
                    "mistake": "당원 권리를 Quyền đảng viên으로 직역",
                    "correction": "Quyền của thành viên đảng + 한국 정당 맥락 설명",
                    "explanation": "베트남 공산당원의 권리·의무 체계와 다르므로 추가 설명 필요"
                },
                {
                    "mistake": "입당을 Nhập đảng로만 번역",
                    "correction": "Gia nhập đảng 또는 Trở thành đảng viên",
                    "explanation": "Nhập đảng는 공산당 입당을 연상시키므로 일반 정당은 다른 표현 선호"
                }
            ],
            "examples": [
                {
                    "ko": "그는 20년 경력의 당원입니다.",
                    "vi": "Anh ấy là đảng viên với 20 năm kinh nghiệm.",
                    "situation": "formal"
                },
                {
                    "ko": "당원 모집 행사가 열렸습니다.",
                    "vi": "Sự kiện tuyển thành viên đảng đã được tổ chức.",
                    "situation": "informal"
                },
                {
                    "ko": "당원 자격으로 경선에 투표할 수 있습니다.",
                    "vi": "Với tư cách đảng viên có thể bỏ phiếu trong bầu cử sơ bộ.",
                    "situation": "formal"
                }
            ],
            "relatedTerms": ["정당", "입당", "탈당", "당비", "당직"]
        },
        {
            "slug": "cuoc-bau-cu-so-bo",
            "korean": "경선",
            "vietnamese": "Cuộc bầu cử sơ bộ",
            "hanja": "競選",
            "hanjaReading": "競(다툴 경) + 選(가릴 선)",
            "pronunciation": "경선",
            "meaningKo": "정당 내에서 공직 후보를 선출하기 위해 당원들이 투표하는 과정을 의미합니다. 통역 시 주의할 점은 한국의 경선 제도가 베트남에는 존재하지 않는다는 점입니다. 한국은 국민참여경선, 당원 경선 등 다양한 방식이 있지만, 베트남은 공산당이 후보자를 선정하므로 당내 경쟁 투표 개념이 없습니다. 정치 통역 시 '경선'이라는 용어를 설명 없이 쓰면 베트남 청중은 이해하기 어려우므로, 한국 정당의 후보 선출 방식임을 반드시 명시해야 합니다.",
            "meaningVi": "Quá trình bỏ phiếu của đảng viên để lựa chọn ứng cử viên chính thức của đảng tranh cử chức vụ công. Đây là thủ tục phổ biến ở các nước đa đảng như Hàn Quốc, nhưng không tồn tại trong hệ thống chính trị Việt Nam.",
            "context": "정당 내부 절차, 대선 준비, 총선 공천",
            "culturalNote": "한국의 경선은 정당 민주주의의 상징으로, 당원이나 일반 국민이 후보를 직접 선택합니다. 베트남은 공산당 중앙위원회나 조국전선이 후보를 심사·선정하므로, 경쟁 투표 방식의 '경선'이 존재하지 않습니다. 한국 정치 뉴스를 통역할 때 '경선 레이스', '경선 승리', '경선 패배' 같은 표현은 베트남 청중에게 생소하므로, 제도 설명을 덧붙여야 합니다.",
            "commonMistakes": [
                {
                    "mistake": "경선을 Cuộc bầu cử로만 번역",
                    "correction": "Cuộc bầu cử sơ bộ (nội bộ đảng) 또는 Bầu chọn ứng cử viên",
                    "explanation": "일반 선거와 구분하기 위해 '당내 예비 선거'임을 명확히 해야 합니다"
                },
                {
                    "mistake": "국민참여경선을 직역 없이 생략",
                    "correction": "Bầu chọn ứng cử viên có sự tham gia của công dân + 제도 설명",
                    "explanation": "베트남에 없는 제도이므로 개념 설명 필수"
                },
                {
                    "mistake": "경선 후보를 Ứng cử viên로만 번역",
                    "correction": "Ứng cử viên trong cuộc bầu cử sơ bộ",
                    "explanation": "본선 후보와 구분해야 혼동을 막을 수 있습니다"
                }
            ],
            "examples": [
                {
                    "ko": "이번 경선에서 세 명의 후보가 경쟁합니다.",
                    "vi": "Trong cuộc bầu cử sơ bộ này có ba ứng cử viên cạnh tranh.",
                    "situation": "formal"
                },
                {
                    "ko": "경선 결과가 내일 발표됩니다.",
                    "vi": "Kết quả bầu chọn ứng cử viên sẽ công bố vào ngày mai.",
                    "situation": "formal"
                },
                {
                    "ko": "그는 경선에서 패배했지만 본선을 지원하겠다고 했습니다.",
                    "vi": "Anh ấy thua trong cuộc bầu cử sơ bộ nhưng nói sẽ ủng hộ cuộc bầu cử chính.",
                    "situation": "informal"
                }
            ],
            "relatedTerms": ["공천", "후보자", "당원", "본선", "투표"]
        },
        {
            "slug": "de-cu",
            "korean": "공천",
            "vietnamese": "Đề cử",
            "hanja": "公薦",
            "hanjaReading": "公(공평할 공) + 薦(천거할 천)",
            "pronunciation": "공천",
            "meaningKo": "정당이 공직 선거에 출마할 후보자를 공식적으로 지명하는 행위를 의미합니다. 통역 시 주의할 점은 한국의 공천은 정당 내부 경쟁과 협상을 거쳐 이루어지며, 공천권을 둘러싼 갈등이 정치 뉴스의 주요 이슈라는 점입니다. 베트남은 공산당이나 조국전선이 후보를 추천하지만, 한국식 '공천 경쟁'이나 '공천 헌금' 같은 개념은 없습니다. 정치 통역 시 한국의 공천 제도를 설명할 때는 당내 권력 구조와 연결지어 맥락을 제공해야 합니다.",
            "meaningVi": "Hành vi đảng chính trị chính thức chỉ định ứng cử viên cho cuộc bầu cử công chức. Ở Hàn Quốc, việc đề cử (công천) là quá trình quan trọng với nhiều cạnh tranh nội bộ đảng.",
            "context": "정당 내부 절차, 선거 준비, 정치 뉴스",
            "culturalNote": "한국의 공천은 정치권력의 핵심 요소로, 공천을 받지 못하면 사실상 당선 가능성이 낮습니다. 공천 과정에서 당비, 경선, 전략공천, 컷오프 등 복잡한 절차가 있습니다. 베트남은 공산당 중앙위원회나 조국전선이 후보를 추천하지만, 한국처럼 공천을 둘러싼 당내 갈등은 거의 없습니다. 통역 시 '공천 파동', '공천 헌금', '전략공천' 같은 용어는 한국 정치 구조를 이해해야 번역 가능합니다.",
            "commonMistakes": [
                {
                    "mistake": "공천을 Đề cử로만 번역하고 맥락 생략",
                    "correction": "Đề cử của đảng (công천) + 한국 제도 설명",
                    "explanation": "베트남의 후보 추천 방식과 다르므로 제도 차이 명시 필요"
                },
                {
                    "mistake": "전략공천을 Đề cử chiến lược로 직역",
                    "correction": "Đề cử theo chiến lược chính trị + 의미 설명",
                    "explanation": "베트남에 없는 개념이므로 당이 특정 이유로 선택한 후보임을 설명"
                },
                {
                    "mistake": "공천권을 Quyền đề cử로만 번역",
                    "correction": "Quyền đề cử ứng cử viên của đảng + 권력 구조 설명",
                    "explanation": "한국 정당에서 공천권이 갖는 정치적 의미를 전달해야 합니다"
                }
            ],
            "examples": [
                {
                    "ko": "그는 당의 공천을 받아 출마합니다.",
                    "vi": "Anh ấy được đảng đề cử và ra tranh cử.",
                    "situation": "formal"
                },
                {
                    "ko": "공천 심사가 다음 주에 열립니다.",
                    "vi": "Cuộc xét duyệt đề cử sẽ diễn ra vào tuần tới.",
                    "situation": "formal"
                },
                {
                    "ko": "공천을 못 받아서 무소속으로 나갈 예정입니다.",
                    "vi": "Vì không được đề cử nên sẽ tranh cử độc lập.",
                    "situation": "informal"
                }
            ],
            "relatedTerms": ["경선", "후보자", "정당", "전략공천", "무소속"]
        },
        {
            "slug": "cuoc-tham-do-y-kien",
            "korean": "여론조사",
            "vietnamese": "Cuộc thăm dò ý kiến",
            "hanja": "輿論調査",
            "hanjaReading": "輿(수레 여) + 論(논할 론) + 調(고를 조) + 査(살필 사)",
            "pronunciation": "여론조사",
            "meaningKo": "선거 전후로 유권자의 의견이나 투표 성향을 조사하는 활동을 말합니다. 통역 시 주의할 점은 한국은 여론조사가 선거의 핵심 지표로 활용되며, 방송사와 언론이 경쟁적으로 실시하지만, 베트남은 선거 관련 여론조사가 제한적이라는 점입니다. 한국의 '지지율 조사', '출구조사', '여론조사 금지 기간' 같은 용어는 베트남 맥락에서 생소할 수 있으므로, 통역 시 제도 차이를 설명해야 합니다. 또한 한국은 여론조사 결과가 선거 판세에 큰 영향을 미치지만, 베트남은 그 역할이 다릅니다.",
            "meaningVi": "Hoạt động khảo sát ý kiến hoặc xu hướng bỏ phiếu của cử tri trước và sau cuộc bầu cử. Ở Việt Nam, các cuộc thăm dò ý kiến liên quan đến bầu cử ít phổ biến hơn so với Hàn Quốc.",
            "context": "선거 보도, 정치 분석, 여론 파악",
            "culturalNote": "한국은 선거 시즌마다 주요 언론사가 지지율 조사를 발표하고, 출구조사로 당락을 사실상 예측합니다. 베트남은 선거 관련 여론조사가 공산당이나 국가 기관에서 제한적으로 실시되며, 민간 여론조사 기관의 활동은 드뭅니다. 한국의 '여론조사 금지 기간'(선거일 6일 전)이나 '오차범위' 같은 개념은 베트남 선거 제도에는 해당하지 않으므로, 통역 시 한국 특유의 제도임을 명시해야 합니다.",
            "commonMistakes": [
                {
                    "mistake": "여론조사를 Khảo sát로만 번역",
                    "correction": "Cuộc thăm dò ý kiến (dư luận) 또는 Khảo sát dư luận",
                    "explanation": "Khảo sát는 일반 조사이고, 여론조사는 정치적 의견 조사임을 명시해야 합니다"
                },
                {
                    "mistake": "출구조사를 Khảo sát đầu ra로 직역",
                    "correction": "Thăm dò ý kiến sau khi bỏ phiếu + 개념 설명",
                    "explanation": "베트남에 출구조사 문화가 없으므로 방식 설명 필요"
                },
                {
                    "mistake": "지지율을 Tỷ lệ hỗ trợ로 번역",
                    "correction": "Tỷ lệ ủng hộ가 정확한 표현",
                    "explanation": "Hỗ trợ는 물리적 지원이고, 정치적 지지는 Ủng hộ입니다"
                }
            ],
            "examples": [
                {
                    "ko": "최근 여론조사에서 지지율이 40%로 나타났습니다.",
                    "vi": "Cuộc thăm dò ý kiến gần đây cho thấy tỷ lệ ủng hộ là 40%.",
                    "situation": "formal"
                },
                {
                    "ko": "선거일 6일 전부터 여론조사 발표가 금지됩니다.",
                    "vi": "Từ 6 ngày trước ngày bầu cử, việc công bố kết quả thăm dò ý kiến bị cấm.",
                    "situation": "formal"
                },
                {
                    "ko": "출구조사 결과가 실제 개표와 거의 일치했습니다.",
                    "vi": "Kết quả thăm dò sau bỏ phiếu gần như trùng khớp với kết quả kiểm phiếu thực tế.",
                    "situation": "informal"
                }
            ],
            "relatedTerms": ["지지율", "출구조사", "선거", "여론", "투표"]
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
    print(f"✅ Added {len(filtered)} terms (선거법/정당법). Total: {len(data)}")

if __name__ == '__main__':
    main()
