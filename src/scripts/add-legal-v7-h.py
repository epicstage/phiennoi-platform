#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""통신비밀/정보보호법 용어 추가 스크립트 (v7-h)"""

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
            "slug": "gam-cheong",
            "korean": "감청",
            "vietnamese": "Nghe lén hợp pháp",
            "hanja": "監聽",
            "hanjaReading": "監(볼 감) + 聽(들을 청)",
            "pronunciation": "감청",
            "meaningKo": "통신비밀보호법상 법원의 허가를 받아 타인의 대화나 통신 내용을 청취하거나 녹음하는 수사 기법. 통역 시 주의할 점은 베트남어 'nghe lén'은 일반적인 도청을 의미하므로, 법적 절차를 거친 합법적 감청임을 강조하기 위해 'hợp pháp'을 반드시 추가해야 함. 불법 도청과 구분하여 통역해야 하며, 영장주의 원칙이 적용됨을 설명할 필요가 있음.",
            "meaningVi": "Theo Luật Bảo vệ Bí mật Thông tin Liên lạc, là kỹ thuật điều tra được tòa án cho phép để nghe hoặc ghi âm nội dung đàm thoại hay thông tin liên lạc của người khác. Khác với nghe lén bất hợp pháp, đây là hoạt động được pháp luật cho phép theo lệnh của tòa án.",
            "context": "형사 수사, 국가안보, 통신비밀보호법 절차",
            "culturalNote": "한국은 통신비밀보호법에 따라 엄격한 영장주의를 적용하여 감청을 제한하고 있으나, 베트남은 국가안보 목적의 감청에 대해 상대적으로 넓은 재량권을 인정하는 경향이 있음. 통역 시 양국의 법적 기준 차이를 명확히 설명해야 함. 또한 한국에서는 감청 남용에 대한 시민사회의 감시가 강한 반면, 베트남에서는 국가 안보 우선 원칙이 더 강조됨.",
            "commonMistakes": [
                {
                    "mistake": "감청을 단순히 'nghe lén'으로만 번역",
                    "correction": "'nghe lén hợp pháp' 또는 'do thám hợp pháp theo lệnh tòa'로 번역",
                    "explanation": "'nghe lén'은 불법 도청의 뉘앙스가 강하므로, 법적 절차를 거친 합법적 감청임을 명확히 해야 함"
                },
                {
                    "mistake": "영장 없는 긴급 감청을 일반 감청과 동일하게 통역",
                    "correction": "'nghe lén khẩn cấp không cần lệnh' (긴급 감청) vs 'nghe lén theo lệnh tòa' (일반 감청) 구분",
                    "explanation": "한국 통신비밀보호법은 예외적으로 긴급 감청을 허용하므로 구분 필요"
                },
                {
                    "mistake": "감청 대상을 단순히 '피의자'로만 설명",
                    "correction": "'người bị nghi ngờ và người liên quan'으로 설명",
                    "explanation": "감청은 피의자뿐 아니라 관련자의 통신도 대상이 될 수 있음"
                }
            ],
            "examples": [
                {
                    "ko": "검찰은 범죄조직 두목의 통화 내용을 확보하기 위해 법원에 감청 영장을 청구했습니다.",
                    "vi": "Viện kiểm sát đã yêu cầu tòa án cấp lệnh nghe lén hợp pháp để thu thập nội dung cuộc gọi của trùm tổ chức tội phạm.",
                    "situation": "formal"
                },
                {
                    "ko": "감청 기간은 최초 2개월이며, 법원의 허가로 연장할 수 있습니다.",
                    "vi": "Thời gian nghe lén ban đầu là 2 tháng và có thể gia hạn với sự cho phép của tòa án.",
                    "situation": "formal"
                },
                {
                    "ko": "불법 감청으로 수집한 증거는 법정에서 증거능력이 인정되지 않습니다.",
                    "vi": "Bằng chứng thu thập qua nghe lén bất hợp pháp không được công nhận giá trị chứng cứ tại tòa.",
                    "situation": "formal"
                }
            ],
            "relatedTerms": ["영장", "통신비밀보호법", "증거능력", "불법 도청"]
        },
        {
            "slug": "thong-sin-ja-ryo-je-gong",
            "korean": "통신자료제공",
            "vietnamese": "Cung cấp dữ liệu thông tin liên lạc",
            "hanja": "通信資料提供",
            "hanjaReading": "通(통할 통) + 信(믿을 신) + 資(재물 자) + 料(헤아릴 료) + 提(들 제) + 供(이바지할 공)",
            "pronunciation": "통신자료제공",
            "meaningKo": "수사기관이 통신사업자에게 요청하여 가입자의 통신 사실 확인 자료를 제공받는 절차. 통역 시 핵심은 이것이 통신 '내용'이 아니라 '메타데이터'(누가, 언제, 어디서 통신했는지)만 제공하는 것임을 명확히 구분해야 함. 감청보다 낮은 수준의 영장주의가 적용되어 검사나 경찰서장의 승인만으로 가능하다는 점을 설명해야 하며, 베트남 통역사들은 이를 감청과 혼동하지 않도록 주의해야 함.",
            "meaningVi": "Quy trình mà cơ quan điều tra yêu cầu nhà cung cấp dịch vụ viễn thông cung cấp dữ liệu xác nhận sự thật thông tin liên lạc của thuê bao. Điều quan trọng là đây chỉ là 'siêu dữ liệu' (ai, khi nào, ở đâu đã liên lạc) chứ không phải nội dung thông tin liên lạc, khác với nghe lén hợp pháp.",
            "context": "형사 수사, 통신비밀보호법, 개인정보 보호",
            "culturalNote": "한국에서는 2016년 헌법재판소가 통신자료제공의 영장주의 위반 여지를 지적한 이후 논란이 계속되고 있으며, 수사기관의 남용 사례가 사회적 이슈가 됨. 베트남에서는 통신 메타데이터에 대한 법적 보호 수준이 한국보다 낮아, 통역 시 한국의 엄격한 개인정보 보호 문화를 설명할 필요가 있음. 한국 의뢰인은 통신자료제공의 법적 한계에 매우 민감함.",
            "commonMistakes": [
                {
                    "mistake": "통신자료제공을 감청과 동일한 것으로 설명",
                    "correction": "'cung cấp siêu dữ liệu' (메타데이터 제공) vs 'nghe lén nội dung' (내용 감청) 명확히 구분",
                    "explanation": "통신자료제공은 통신 내용이 아니라 발신·수신 번호, 시간, 기지국 위치 등만 제공"
                },
                {
                    "mistake": "'통신사실확인자료'를 단순히 'dữ liệu viễn thông'으로 번역",
                    "correction": "'dữ liệu xác nhận sự thật thông tin liên lạc'로 정확히 번역",
                    "explanation": "법적 용어이므로 정확한 번역 필요"
                },
                {
                    "mistake": "영장 없이 가능한 점을 설명하지 않음",
                    "correction": "'không cần lệnh tòa, chỉ cần phê duyệt của kiểm sát hoặc trưởng công an'으로 명시",
                    "explanation": "감청과 달리 법원 영장이 아닌 내부 승인만으로 가능함을 강조"
                }
            ],
            "examples": [
                {
                    "ko": "경찰은 피의자의 최근 3개월간 통신사실확인자료를 통신사로부터 제공받았습니다.",
                    "vi": "Công an đã nhận được dữ liệu xác nhận sự thật thông tin liên lạc 3 tháng gần đây của nghi phạm từ công ty viễn thông.",
                    "situation": "formal"
                },
                {
                    "ko": "통신자료제공은 통신 내용이 아니라 발신·수신 번호와 시간만 확인하는 것입니다.",
                    "vi": "Cung cấp dữ liệu thông tin liên lạc chỉ xác nhận số gọi đi, gọi đến và thời gian, không phải nội dung cuộc gọi.",
                    "situation": "formal"
                },
                {
                    "ko": "검사의 승인만으로 통신자료를 제공받을 수 있어 영장주의 위반 논란이 있습니다.",
                    "vi": "Việc có thể nhận dữ liệu thông tin liên lạc chỉ với phê duyệt của kiểm sát viên gây tranh cãi về vi phạm nguyên tắc lệnh tòa.",
                    "situation": "formal"
                }
            ],
            "relatedTerms": ["감청", "통신사실확인자료", "영장주의", "개인정보보호"]
        },
        {
            "slug": "wi-chi-chu-jeok",
            "korean": "위치추적",
            "vietnamese": "Theo dõi vị trí",
            "hanja": "位置追跡",
            "hanjaReading": "位(자리 위) + 置(놓을 치) + 追(쫓을 추) + 跡(자취 적)",
            "pronunciation": "위치추적",
            "meaningKo": "전자장치를 이용하여 사람이나 물건의 소재를 실시간으로 파악하는 수사 기법. 통역 시 주의할 점은 위치추적 방식이 다양하다는 것(GPS 추적기, 휴대폰 기지국 추적, 전자발찌 등)을 구분해서 설명해야 함. 한국에서는 통신비밀보호법과 위치정보법이 적용되며, 영장주의가 원칙이지만 긴급 상황에서는 예외가 인정됨. 베트남 통역사는 '추적'이 범죄 수사뿐 아니라 보호관찰 등에도 사용됨을 이해해야 함.",
            "meaningVi": "Kỹ thuật điều tra xác định vị trí của người hoặc đồ vật theo thời gian thực bằng thiết bị điện tử. Áp dụng Luật Bảo vệ Bí mật Thông tin Liên lạc và Luật Thông tin Vị trí ở Hàn Quốc, nguyên tắc là cần lệnh tòa nhưng có ngoại lệ trong trường hợp khẩn cấp.",
            "context": "형사 수사, 보호관찰, 실종자 수색, 위치정보법",
            "culturalNote": "한국에서는 2012년 이후 위치추적 전자장치(전자발찌)가 성범죄자 등에 대한 보호관찰 수단으로 확대되었으며, 사회적 수용도가 높은 편임. 베트남에서는 전자발찌 제도가 상대적으로 제한적이고, GPS 추적 기술을 활용한 수사가 한국만큼 보편화되지 않았음. 통역 시 한국의 선진화된 위치추적 기술과 법적 프레임워크를 설명할 필요가 있음.",
            "commonMistakes": [
                {
                    "mistake": "모든 위치추적을 'GPS'로만 설명",
                    "correction": "'GPS', 'định vị qua trạm BTS' (기지국), 'vòng đeo chân điện tử' (전자발찌) 등 구분",
                    "explanation": "위치추적 방식은 다양하므로 상황에 맞게 정확히 표현"
                },
                {
                    "mistake": "위치추적을 단순히 'theo dõi'로만 번역",
                    "correction": "'theo dõi vị trí bằng thiết bị điện tử'로 구체화",
                    "explanation": "'theo dõi'는 일반적인 추적이므로, 전자장치를 이용한 위치추적임을 명시"
                },
                {
                    "mistake": "범죄 수사용 위치추적과 전자발찌를 구분하지 않음",
                    "correction": "'theo dõi điều tra' (수사용) vs 'giám sát bằng vòng đeo chân' (보호관찰용) 구분",
                    "explanation": "목적과 법적 근거가 다르므로 명확히 구분 필요"
                }
            ],
            "examples": [
                {
                    "ko": "범인의 차량에 GPS 추적 장치를 부착하여 도주 경로를 파악했습니다.",
                    "vi": "Đã xác định được lộ trình trốn chạy bằng cách gắn thiết bị theo dõi GPS vào xe của thủ phạm.",
                    "situation": "formal"
                },
                {
                    "ko": "아동 성범죄자에게 전자발찌를 부착하여 24시간 위치를 추적합니다.",
                    "vi": "Gắn vòng đeo chân điện tử cho kẻ phạm tội tình dục trẻ em để theo dõi vị trí 24 giờ.",
                    "situation": "formal"
                },
                {
                    "ko": "긴급 상황에서는 영장 없이도 휴대폰 기지국을 통해 위치를 추적할 수 있습니다.",
                    "vi": "Trong tình huống khẩn cấp, có thể theo dõi vị trí qua trạm BTS điện thoại di động mà không cần lệnh tòa.",
                    "situation": "formal"
                }
            ],
            "relatedTerms": ["전자발찌", "GPS", "기지국", "위치정보법"]
        },
        {
            "slug": "di-ji-teol-po-ren-sik",
            "korean": "디지털포렌식",
            "vietnamese": "Pháp y số",
            "hanja": None,
            "hanjaReading": None,
            "pronunciation": "디지털포렌식",
            "meaningKo": "디지털 기기나 저장매체에서 범죄의 증거를 과학적으로 수집·분석·보존하는 수사 기법. 통역 시 핵심은 이것이 단순한 데이터 복구가 아니라 법정에서 증거능력을 인정받을 수 있도록 '증거 보전의 연속성(Chain of Custody)'을 유지하며 진행되는 전문 절차임을 강조해야 함. 삭제된 파일 복구, 암호 해독, 로그 분석 등 다양한 기법이 사용되며, 한국에서는 사이버 범죄뿐 아니라 일반 형사 사건에서도 필수적인 수사 방법으로 자리잡았음.",
            "meaningVi": "Kỹ thuật điều tra thu thập, phân tích và bảo quản bằng chứng tội phạm từ thiết bị số hoặc phương tiện lưu trữ một cách khoa học. Không chỉ là khôi phục dữ liệu đơn giản mà là quy trình chuyên môn duy trì 'chuỗi bảo quản bằng chứng' để được công nhận giá trị chứng cứ tại tòa án.",
            "context": "사이버 범죄 수사, 증거 수집, 형사소송법",
            "culturalNote": "한국은 디지털포렌식 기술과 전문 인력이 고도로 발달했으며, 대검찰청 디지털수사과와 경찰청 사이버안전국이 전문 장비를 보유하고 있음. 베트남은 사이버 범죄 수사 역량을 빠르게 강화하고 있으나 아직 한국 수준의 포렌식 인프라는 부족한 상황. 통역 시 한국의 선진 포렌식 기술과 법적 절차의 엄격성을 설명하고, 베트남 의뢰인에게 한국 수사기관의 높은 증거 수집 능력을 이해시켜야 함.",
            "commonMistakes": [
                {
                    "mistake": "디지털포렌식을 단순히 'khôi phục dữ liệu'(데이터 복구)로 번역",
                    "correction": "'pháp y số' 또는 'điều tra khoa học kỹ thuật số'로 번역",
                    "explanation": "포렌식은 법정 증거 확보를 위한 과학적 절차이므로 단순 복구와 구분"
                },
                {
                    "mistake": "증거 보전의 연속성 개념을 설명하지 않음",
                    "correction": "'chuỗi bảo quản bằng chứng' (Chain of Custody) 개념 반드시 설명",
                    "explanation": "포렌식의 법적 증거능력은 이 개념에서 나오므로 필수 설명 요소"
                },
                {
                    "mistake": "하드웨어 포렌식과 네트워크 포렌식을 구분하지 않음",
                    "correction": "'pháp y phần cứng' (하드웨어) vs 'pháp y mạng' (네트워크) 명확히 구분",
                    "explanation": "포렌식 대상과 방법론이 다르므로 구분 필요"
                }
            ],
            "examples": [
                {
                    "ko": "검찰은 피의자의 노트북을 압수하여 디지털포렌식 분석을 실시했습니다.",
                    "vi": "Viện kiểm sát đã tịch thu máy tính xách tay của nghi phạm và tiến hành phân tích pháp y số.",
                    "situation": "formal"
                },
                {
                    "ko": "삭제된 이메일을 복구하여 횡령 증거를 확보했습니다.",
                    "vi": "Đã khôi phục email đã xóa để xác bảo bằng chứng tham ô.",
                    "situation": "formal"
                },
                {
                    "ko": "디지털포렌식 절차를 위반하면 증거능력이 부정될 수 있습니다.",
                    "vi": "Nếu vi phạm quy trình pháp y số, giá trị chứng cứ có thể bị phủ nhận.",
                    "situation": "formal"
                }
            ],
            "relatedTerms": ["증거능력", "압수수색", "사이버범죄", "데이터복구"]
        },
        {
            "slug": "jeon-ja-gam-si",
            "korean": "전자감시",
            "vietnamese": "Giám sát điện tử",
            "hanja": "電子監視",
            "hanjaReading": "電(번개 전) + 子(아들 자) + 監(볼 감) + 視(볼 시)",
            "pronunciation": "전자감시",
            "meaningKo": "전자장치를 이용하여 특정인의 행동이나 위치를 지속적으로 감시하는 제도. 통역 시 주의할 점은 '감시'와 '추적'의 차이를 명확히 해야 함. 전자감시는 보호관찰, 가택구금, 출입국 제한 등 다양한 목적으로 활용되며, 한국에서는 전자발찌(위치추적 전자장치)가 대표적임. 이것이 형벌이 아니라 '보안처분'이라는 점, 재범 방지와 사회 복귀를 동시에 목표로 한다는 점을 설명해야 하며, 베트남에는 유사 제도가 제한적이므로 개념 설명이 중요함.",
            "meaningVi": "Chế độ giám sát liên tục hành vi hoặc vị trí của một người cụ thể bằng thiết bị điện tử. Ở Hàn Quốc, vòng đeo chân điện tử (thiết bị theo dõi vị trí điện tử) là điển hình, được sử dụng cho quản chế, giam giữ tại gia, hạn chế xuất nhập cảnh. Đây không phải hình phạt mà là 'biện pháp bảo an' nhằm ngăn tái phạm và tái hòa nhập xã hội.",
            "context": "보호관찰, 보안처분, 성범죄자 관리, 가택구금",
            "culturalNote": "한국은 2008년 전자발찌 제도를 도입한 이후 성범죄자, 살인범 등 강력범죄자에 대한 전자감시를 확대해왔으며, 사회적 수용도가 높은 편. 베트남에서는 전자감시 제도가 아직 초기 단계이고, 교정 시스템이 시설 수용 중심이라 전자감시 개념이 낯설 수 있음. 통역 시 한국의 선진 보안처분 제도와 인권 보호 장치(법원 결정 필수, 기간 제한 등)를 함께 설명해야 함.",
            "commonMistakes": [
                {
                    "mistake": "전자감시를 형벌로 설명",
                    "correction": "'biện pháp bảo an' (보안처분)이지 'hình phạt' (형벌)이 아님을 명시",
                    "explanation": "전자감시는 형벌이 아닌 재범 방지를 위한 별도 처분"
                },
                {
                    "mistake": "전자발찌와 전자감시를 동일시",
                    "correction": "전자발찌는 전자감시의 '수단' 중 하나임을 설명",
                    "explanation": "전자감시는 개념, 전자발찌는 구체적 장치"
                },
                {
                    "mistake": "'감시'를 부정적으로만 표현",
                    "correction": "'theo dõi để ngăn tái phạm và hỗ trợ tái hòa nhập' (재범 방지와 재활 지원)으로 균형있게 설명",
                    "explanation": "전자감시는 처벌이 아니라 사회 복귀 지원 목적도 있음"
                }
            ],
            "examples": [
                {
                    "ko": "성폭력 범죄자에게 10년간 전자감시 처분을 선고했습니다.",
                    "vi": "Đã tuyên án giám sát điện tử 10 năm đối với tội phạm bạo lực tình dục.",
                    "situation": "formal"
                },
                {
                    "ko": "전자감시 대상자는 보호관찰관의 지시를 따라야 합니다.",
                    "vi": "Người chịu giám sát điện tử phải tuân theo chỉ thị của quản chế viên.",
                    "situation": "formal"
                },
                {
                    "ko": "가택구금 기간 동안 전자발찌를 착용하고 외출이 제한됩니다.",
                    "vi": "Trong thời gian giam giữ tại gia, phải đeo vòng đeo chân điện tử và bị hạn chế ra ngoài.",
                    "situation": "formal"
                }
            ],
            "relatedTerms": ["전자발찌", "보호관찰", "보안처분", "가택구금"]
        },
        {
            "slug": "am-ho-hwa",
            "korean": "암호화",
            "vietnamese": "Mã hóa",
            "hanja": "暗號化",
            "hanjaReading": "暗(어두울 암) + 號(부를 호) + 化(될 화)",
            "pronunciation": "암호화",
            "meaningKo": "정보를 제3자가 알아볼 수 없도록 특정 알고리즘을 이용해 변환하는 기술. 통역 시 핵심은 암호화가 정보보호의 핵심 수단이지만, 수사기관 입장에서는 증거 확보의 장애물이 될 수 있다는 양면성을 이해시켜야 함. 한국에서는 개인정보보호법상 개인정보의 암호화가 의무이며, 통신비밀보호법도 암호화 통신을 보호하지만, 범죄 수사 시 암호 해독이 필요한 딜레마가 있음. 대칭키와 비대칭키, 종단간 암호화(E2EE) 등 기술적 개념도 설명할 수 있어야 함.",
            "meaningVi": "Công nghệ chuyển đổi thông tin bằng thuật toán cụ thể để bên thứ ba không thể hiểu được. Là phương tiện cốt lõi bảo vệ thông tin, nhưng từ góc độ cơ quan điều tra có thể là rào cản thu thập bằng chứng. Ở Hàn Quốc, mã hóa thông tin cá nhân là bắt buộc theo Luật Bảo vệ Thông tin Cá nhân.",
            "context": "정보보호, 개인정보보호법, 사이버보안, 통신비밀보호",
            "culturalNote": "한국은 2010년대 이후 대규모 개인정보 유출 사건들을 겪으며 암호화 의무를 강화했고, 금융권과 공공기관의 암호화 수준이 매우 높음. 베트남도 사이버보안법으로 암호화를 장려하지만, 중소기업의 적용 수준은 한국보다 낮은 편. 통역 시 한국의 엄격한 암호화 규제와 위반 시 제재(과태료, 형사처벌)를 설명해야 하며, 암호화가 범죄 은폐 수단이 아니라 정당한 권리임을 강조해야 함.",
            "commonMistakes": [
                {
                    "mistake": "암호화를 단순히 '비밀번호'로 이해",
                    "correction": "'mã hóa dữ liệu bằng thuật toán' (알고리즘 기반 데이터 암호화)로 설명",
                    "explanation": "비밀번호는 인증 수단, 암호화는 데이터 변환 기술로 개념이 다름"
                },
                {
                    "mistake": "종단간 암호화를 일반 암호화와 구분하지 않음",
                    "correction": "'mã hóa đầu cuối' (E2EE)는 중간 서버도 내용을 볼 수 없는 강화된 암호화임을 명시",
                    "explanation": "E2EE는 보안 수준이 다르므로 구분 필요"
                },
                {
                    "mistake": "암호 해독을 불법으로만 설명",
                    "correction": "법원 명령에 따른 합법적 암호 해독과 불법 해킹 구분",
                    "explanation": "수사 목적의 합법적 암호 해독은 법적으로 허용됨"
                }
            ],
            "examples": [
                {
                    "ko": "개인정보를 저장할 때는 반드시 암호화해야 합니다.",
                    "vi": "Khi lưu trữ thông tin cá nhân, bắt buộc phải mã hóa.",
                    "situation": "formal"
                },
                {
                    "ko": "검찰은 압수한 USB의 암호를 해독하여 비자금 증거를 확보했습니다.",
                    "vi": "Viện kiểm sát đã giải mã USB bị tịch thu và xác bảo bằng chứng quỹ đen.",
                    "situation": "formal"
                },
                {
                    "ko": "메신저의 종단간 암호화로 수사기관도 대화 내용을 볼 수 없습니다.",
                    "vi": "Do mã hóa đầu cuối của ứng dụng nhắn tin, cơ quan điều tra cũng không thể xem nội dung hội thoại.",
                    "situation": "formal"
                }
            ],
            "relatedTerms": ["개인정보보호", "사이버보안", "해킹", "디지털포렌식"]
        },
        {
            "slug": "sa-i-beo-bo-an",
            "korean": "사이버보안",
            "vietnamese": "An ninh mạng",
            "hanja": None,
            "hanjaReading": None,
            "pronunciation": "사이버보안",
            "meaningKo": "사이버 공간에서 발생하는 위협으로부터 정보시스템과 데이터를 보호하는 모든 활동과 기술. 통역 시 핵심은 이것이 단순한 '해킹 방지'가 아니라 국가 안보, 기업 경영, 개인 프라이버시를 모두 포괄하는 종합적 개념임을 이해시켜야 함. 한국은 정보통신망법, 개인정보보호법, 정보보호산업법 등 다층적 법체계로 사이버보안을 규율하며, 국가정보원과 과학기술정보통신부가 주요 역할을 담당. 베트남 통역사는 한국의 사이버보안 수준과 의무 준수 문화가 매우 엄격함을 이해해야 함.",
            "meaningVi": "Mọi hoạt động và công nghệ bảo vệ hệ thống thông tin và dữ liệu khỏi các mối đe dọa xảy ra trong không gian mạng. Không chỉ là 'phòng chống hack' đơn giản mà là khái niệm tổng hợp bao gồm an ninh quốc gia, quản trị doanh nghiệp và quyền riêng tư cá nhân. Hàn Quốc điều chỉnh an ninh mạng bằng hệ thống pháp luật đa tầng.",
            "context": "정보통신망법, 개인정보보호법, 국가안보, 기업보안",
            "culturalNote": "한국은 2013년 3·20 사이버테러, 2014년 한국수력원자력 해킹 등 대규모 사이버 공격을 겪으며 사이버보안을 국가 핵심 의제로 설정했고, K-사이버 방위체계를 구축함. 베트남도 2019년 사이버안보법을 시행하며 보안을 강화하고 있으나, 민간 기업의 보안 수준은 한국보다 낮음. 통역 시 한국 기업의 높은 보안 요구사항과 컴플라이언스 문화를 설명하고, 베트남 인력의 보안 교육 필요성을 강조해야 함.",
            "commonMistakes": [
                {
                    "mistake": "사이버보안을 단순히 '안티바이러스'로 이해",
                    "correction": "방화벽, 침입탐지, 암호화, 접근통제 등 종합적 개념으로 설명",
                    "explanation": "사이버보안은 다층적 방어 체계"
                },
                {
                    "mistake": "'an ninh mạng'과 'bảo mật thông tin' 혼용",
                    "correction": "'an ninh mạng'(사이버보안)은 'bảo mật thông tin'(정보보안)보다 넓은 개념",
                    "explanation": "사이버보안이 정보보안을 포함하는 상위 개념"
                },
                {
                    "mistake": "법적 의무 사항을 기술적 권고로 축소",
                    "correction": "한국은 정보통신망법상 보안 조치가 '의무'이며 위반 시 처벌됨을 명시",
                    "explanation": "한국의 엄격한 법적 요구사항 강조 필요"
                }
            ],
            "examples": [
                {
                    "ko": "모든 기업은 정보통신망법에 따라 사이버보안 조치를 취해야 합니다.",
                    "vi": "Mọi doanh nghiệp phải thực hiện biện pháp an ninh mạng theo Luật Mạng Thông tin Truyền thông.",
                    "situation": "formal"
                },
                {
                    "ko": "랜섬웨어 공격으로 회사 전산망이 마비되어 큰 피해를 입었습니다.",
                    "vi": "Hệ thống mạng công ty bị tê liệt do tấn công ransomware, gây thiệt hại lớn.",
                    "situation": "formal"
                },
                {
                    "ko": "국가정보원은 국가 차원의 사이버보안 위협에 대응합니다.",
                    "vi": "Cơ quan Tình báo Quốc gia ứng phó với các mối đe dọa an ninh mạng cấp quốc gia.",
                    "situation": "formal"
                }
            ],
            "relatedTerms": ["해킹", "랜섬웨어", "정보통신망법", "개인정보보호"]
        },
        {
            "slug": "jeong-bo-gong-gae",
            "korean": "정보공개",
            "vietnamese": "Công khai thông tin",
            "hanja": "情報公開",
            "hanjaReading": "情(뜻 정) + 報(알릴 보) + 公(공평할 공) + 開(열 개)",
            "pronunciation": "정보공개",
            "meaningKo": "공공기관이 보유·관리하는 정보를 국민의 청구에 따라 공개하는 제도로, 공공기관의정보공개에관한법률이 적용됨. 통역 시 핵심은 이것이 '알 권리'라는 헌법적 권리에 기반한 제도이며, 원칙적으로 모든 정보가 공개 대상이지만 국가안보, 개인 프라이버시 등 예외 사유가 있다는 점을 설명해야 함. 정보공개 청구는 누구나 할 수 있고, 거부 시 행정심판이나 행정소송으로 다툴 수 있음. 베트남에도 유사 제도가 있으나 실효성 면에서 한국이 더 발달했음을 이해시켜야 함.",
            "meaningVi": "Chế độ công khai thông tin mà cơ quan công theo yêu cầu của quốc dân đang nắm giữ và quản lý, áp dụng Luật Công khai Thông tin của Cơ quan Công. Dựa trên quyền 'được biết thông tin' - quyền hiến định, nguyên tắc là công khai mọi thông tin nhưng có ngoại lệ như an ninh quốc gia, quyền riêng tư cá nhân.",
            "context": "공공기관정보공개법, 행정법, 알 권리, 투명성",
            "culturalNote": "한국은 1996년 정보공개법 제정 이후 정보공개 제도가 정착되었고, 시민단체와 언론의 활발한 활용으로 정부 투명성이 크게 향상됨. 온라인 정보공개 시스템이 잘 구축되어 있어 접근성이 높음. 베트남도 2016년 정보접근법을 시행했으나, 공개 범위와 실제 이행 수준은 한국보다 제한적. 통역 시 한국의 적극적 정보공개 문화와 국민의 높은 참여도를 설명하고, 정보공개 청구가 권리임을 강조해야 함.",
            "commonMistakes": [
                {
                    "mistake": "정보공개를 '정보 유출'과 혼동",
                    "correction": "'công khai hợp pháp theo yêu cầu' (합법적 청구에 따른 공개) vs 'rò rỉ thông tin' (정보 유출) 구분",
                    "explanation": "정보공개는 법적 절차, 정보 유출은 불법 행위"
                },
                {
                    "mistake": "공개 예외 사유를 단순히 '비밀'로만 표현",
                    "correction": "'thông tin liên quan an ninh quốc gia' (국가안보), 'quyền riêng tư' (프라이버시) 등 구체적 예외 사유 명시",
                    "explanation": "예외는 법으로 정한 구체적 사유에 한정됨"
                },
                {
                    "mistake": "정보공개 청구를 복잡한 절차로 설명",
                    "correction": "'ai cũng có thể yêu cầu, thủ tục đơn giản' (누구나 청구 가능, 간단한 절차)로 설명",
                    "explanation": "한국의 정보공개는 접근성이 높음"
                }
            ],
            "examples": [
                {
                    "ko": "시민은 정보공개법에 따라 정부의 예산 집행 내역을 청구할 수 있습니다.",
                    "vi": "Công dân có thể yêu cầu nội dung chi ngân sách của chính phủ theo Luật Công khai Thông tin.",
                    "situation": "formal"
                },
                {
                    "ko": "국가안보에 관한 정보는 공개가 거부될 수 있습니다.",
                    "vi": "Thông tin liên quan an ninh quốc gia có thể bị từ chối công khai.",
                    "situation": "formal"
                },
                {
                    "ko": "정보공개 거부 처분에 불복하여 행정소송을 제기했습니다.",
                    "vi": "Đã nộp đơn kiện hành chính vì không phục quyết định từ chối công khai thông tin.",
                    "situation": "formal"
                }
            ],
            "relatedTerms": ["알권리", "행정심판", "행정소송", "공공기관"]
        },
        {
            "slug": "bi-mil-bun-ryu",
            "korean": "비밀분류",
            "vietnamese": "Phân loại mật",
            "hanja": "秘密分類",
            "hanjaReading": "秘(숨길 비) + 密(빽빽할 밀) + 分(나눌 분) + 類(무리 류)",
            "pronunciation": "비밀분류",
            "meaningKo": "국가의 안전보장과 이익을 위해 특정 정보를 보호 등급에 따라 분류하고 접근을 제한하는 제도로, 보안업무규정이 적용됨. 통역 시 핵심은 한국의 비밀 등급 체계(Ⅰ급 비밀, Ⅱ급 비밀, Ⅲ급 비밀)를 정확히 이해하고, 각 등급에 따른 유출 시 처벌 수위가 다름을 설명해야 함. Ⅰ급은 '전쟁 도발이나 국가 안전보장에 치명적 위해', Ⅱ급은 '국가안보에 막대한 지장', Ⅲ급은 '국가안보에 손해' 기준. 군사기밀, 외교기밀뿐 아니라 산업기밀도 포함될 수 있으며, 비밀취급인가를 받은 사람만 접근 가능함.",
            "meaningVi": "Chế độ phân loại thông tin cụ thể theo cấp độ bảo vệ và hạn chế tiếp cận vì an ninh quốc gia và lợi ích quốc gia, áp dụng Quy định Công tác Bảo mật. Hàn Quốc có hệ thống cấp độ mật (Cấp I, Cấp II, Cấp III), mức độ xử phạt khi tiết lộ khác nhau theo từng cấp. Chỉ người có giấy phép xử lý thông tin mật mới được tiếp cận.",
            "context": "보안업무규정, 군사기밀, 국가안보, 형법",
            "culturalNote": "한국은 분단 상황으로 인해 비밀 보호가 매우 엄격하며, 군 복무 중 보안교육이 철저함. 공무원, 방산업체 직원 등은 비밀취급인가를 받아야 하고, 신원조사 절차가 까다로움. 베트남도 국가기밀 보호법이 있으나, 한국처럼 세분화된 등급 체계와 엄격한 관리는 상대적으로 덜함. 통역 시 한국의 높은 보안 의식과 위반 시 중형(최고 사형까지 가능)을 설명해야 하며, 외국인도 한국 기밀 유출 시 처벌 대상임을 강조해야 함.",
            "commonMistakes": [
                {
                    "mistake": "모든 비밀을 'tuyệt mật'(극비)로 번역",
                    "correction": "'mật cấp I' (Ⅰ급), 'mật cấp II' (Ⅱ급), 'mật cấp III' (Ⅲ급) 구분",
                    "explanation": "각 등급에 따라 보호 수준과 처벌이 다름"
                },
                {
                    "mistake": "비밀 해제(declassification)를 설명하지 않음",
                    "correction": "'giải mật'는 일정 기간 후 또는 사유 소멸 시 가능함을 명시",
                    "explanation": "비밀은 영구적이지 않고 해제 절차가 있음"
                },
                {
                    "mistake": "민간 기업의 산업기밀을 비밀분류에서 제외",
                    "correction": "방산업체 등 국가안보 관련 민간기밀도 비밀분류 대상임을 설명",
                    "explanation": "비밀분류는 공공기관뿐 아니라 민간도 포함"
                }
            ],
            "examples": [
                {
                    "ko": "이 문서는 Ⅱ급 비밀로 분류되어 비밀취급인가를 받은 사람만 볼 수 있습니다.",
                    "vi": "Tài liệu này được phân loại mật cấp II, chỉ người có giấy phép xử lý thông tin mật mới được xem.",
                    "situation": "formal"
                },
                {
                    "ko": "군사기밀을 유출하면 최고 사형까지 처벌받을 수 있습니다.",
                    "vi": "Nếu tiết lộ bí mật quân sự, có thể bị xử tử hình cao nhất.",
                    "situation": "formal"
                },
                {
                    "ko": "이 정보는 30년 후 자동으로 비밀이 해제됩니다.",
                    "vi": "Thông tin này sẽ tự động được giải mật sau 30 năm.",
                    "situation": "formal"
                }
            ],
            "relatedTerms": ["국가기밀", "보안업무규정", "군사기밀", "형법"]
        },
        {
            "slug": "tong-sin-bi-mil-bo-ho-beop",
            "korean": "통신비밀보호법",
            "vietnamese": "Luật Bảo vệ Bí mật Thông tin Liên lạc",
            "hanja": "通信秘密保護法",
            "hanjaReading": "通(통할 통) + 信(믿을 신) + 秘(숨길 비) + 密(빽빽할 밀) + 保(지킬 보) + 護(지킬 호) + 法(법 법)",
            "pronunciation": "통신비밀보호법",
            "meaningKo": "헌법상 통신의 비밀을 보장하고 통신의 자유를 보호하기 위한 법률로, 감청, 우편물 검열 등 통신 제한의 요건과 절차를 규정함. 통역 시 핵심은 이 법이 '국가 권력의 통신 침해로부터 국민을 보호'하는 기본권 보장법이라는 점을 강조해야 함. 동시에 범죄 수사와 국가안보를 위해 예외적으로 통신 제한을 허용하되, 엄격한 영장주의를 적용한다는 양면성을 설명해야 함. 1993년 제정 이후 여러 차례 개정되었고, 특히 2001년 9·11 테러 이후와 2016년 헌재 결정 이후 주요 변화가 있었음을 이해해야 함.",
            "meaningVi": "Luật nhằm bảo đảm bí mật thông tin liên lạc theo Hiến pháp và bảo vệ tự do thông tin liên lạc, quy định yêu cầu và thủ tục hạn chế thông tin liên lạc như nghe lén, kiểm duyệt thư từ. Điều cốt lõi là đây là luật bảo đảm quyền cơ bản 'bảo vệ công dân khỏi sự xâm phạm thông tin liên lạc của quyền lực nhà nước', đồng thời cho phép ngoại lệ hạn chế thông tin liên lạc vì điều tra tội phạm và an ninh quốc gia với nguyên tắc lệnh tòa nghiêm ngặt.",
            "context": "헌법, 통신의 자유, 영장주의, 형사소송법",
            "culturalNote": "한국에서 통신비밀보호법은 권위주의 정권 시절의 불법 도청 역사에 대한 반성으로 제정된 법으로, 민주주의와 인권의 상징적 의미가 있음. 그러나 국가안보와 범죄 수사의 필요성으로 인해 개정 논란이 계속되고 있음. 베트남에도 유사한 법이 있으나 국가안보 우선 원칙이 더 강하고, 통신 제한의 절차적 엄격성은 한국보다 낮음. 통역 시 한국의 높은 인권 의식과 영장주의 전통을 강조하고, 불법 감청에 대한 사회적 민감도가 매우 높음을 설명해야 함.",
            "commonMistakes": [
                {
                    "mistake": "통신비밀보호법을 단순히 '감청법'으로 축소",
                    "correction": "감청뿐 아니라 우편검열, 통신자료제공, 위치추적 등 모든 통신 제한을 포괄하는 법임을 설명",
                    "explanation": "통신비밀보호법은 통신 제한의 포괄적 법률"
                },
                {
                    "mistake": "이 법이 '수사 편의'를 위한 법으로 설명",
                    "correction": "기본적으로 '국민의 통신 자유 보호'가 목적이고, 수사는 예외적 허용임을 명시",
                    "explanation": "법의 입법 취지와 목적을 정확히 전달"
                },
                {
                    "mistake": "영장주의 예외를 강조하지 않음",
                    "correction": "국가안보 위협 시 긴급 감청 등 예외가 있음을 설명",
                    "explanation": "원칙과 예외를 모두 이해해야 정확한 통역 가능"
                }
            ],
            "examples": [
                {
                    "ko": "통신비밀보호법 위반으로 불법 감청한 증거는 재판에서 사용할 수 없습니다.",
                    "vi": "Bằng chứng nghe lén bất hợp pháp vi phạm Luật Bảo vệ Bí mật Thông tin Liên lạc không thể sử dụng trong phiên tòa.",
                    "situation": "formal"
                },
                {
                    "ko": "검찰은 통신비밀보호법에 따라 법원에 감청 영장을 청구했습니다.",
                    "vi": "Viện kiểm sát đã yêu cầu tòa án cấp lệnh nghe lén theo Luật Bảo vệ Bí mật Thông tin Liên lạc.",
                    "situation": "formal"
                },
                {
                    "ko": "이 법은 통신의 자유라는 헌법적 권리를 보호하기 위해 만들어졌습니다.",
                    "vi": "Luật này được tạo ra để bảo vệ quyền hiến định là tự do thông tin liên lạc.",
                    "situation": "formal"
                }
            ],
            "relatedTerms": ["감청", "영장주의", "통신자료제공", "헌법"]
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
