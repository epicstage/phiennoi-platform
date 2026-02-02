#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""항공/우주법 용어 추가 (v9-e)"""
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
            "slug": "an-toan-hang-khong",
            "korean": "항공안전",
            "vietnamese": "An toàn hàng không",
            "hanja": "航空安全",
            "hanjaReading": "航(다닐 항) + 空(빌 공) + 安(편안할 안) + 全(온전할 전)",
            "pronunciation": "항공안전",
            "meaningKo": "항공기의 운항과 관련하여 사람과 재산의 안전을 확보하기 위한 제반 조치와 기준을 말합니다. 통역 시 한국 항공안전법은 항공기 감항성·정비·운항 기준을 규정하며, 위반 시 운항정지·면허취소·형사처벌(10년 이하 징역)이 가능하고, 국제민간항공기구(ICAO) 기준을 준수한다는 점을 명확히 전달해야 합니다.",
            "meaningVi": "Các biện pháp và tiêu chuẩn để đảm bảo an toàn con người và tài sản liên quan đến vận hành tàu bay. Luật an toàn hàng không Hàn Quốc quy định tiêu chuẩn khả năng bay, bảo dưỡng, vận hành tàu bay, vi phạm có thể bị đình chỉ vận hành, thu hồi giấy phép, xử lý hình sự (tù 10 năm), tuân thủ tiêu chuẩn Tổ chức Hàng không Dân dụng Quốc tế (ICAO).",
            "context": "항공 사고 조사 및 안전 규제 상황에서 사용",
            "culturalNote": "한국은 항공안전 관리를 국토교통부 항공정책실이 담당하며, 항공기 사고율이 매우 낮은 국가입니다. 아시아나항공 사고(2013) 이후 조종사 피로도 관리·영어 능력 강화 등 안전 규제가 대폭 강화되었습니다. 베트남도 항공 산업이 성장 중이나 안전 기준이 낮아 통역 시 한국의 엄격한 안전 체계를 설명해야 합니다.",
            "commonMistakes": [
                {
                    "mistake": "an ninh hàng không",
                    "correction": "an toàn hàng không (안전) vs an ninh (보안)",
                    "explanation": "'항공보안'은 테러 방지이며, '항공안전'은 사고 예방으로 구분됩니다"
                },
                {
                    "mistake": "bay an toàn",
                    "correction": "an toàn hàng không (체계적 기준)",
                    "explanation": "'안전하게 비행'은 일상 표현이며 법적 안전 체계의 개념이 누락됩니다"
                },
                {
                    "mistake": "đảm bảo máy bay",
                    "correction": "an toàn hàng không (포괄적)",
                    "explanation": "'항공기 보장'은 모호하며 안전의 구체적 의미가 약화됩니다"
                }
            ],
            "examples": [
                {
                    "ko": "이 항공사는 항공안전법 위반으로 6개월 운항정지 처분을 받았습니다",
                    "vi": "Hãng hàng không này bị đình chỉ vận hành 6 tháng vì vi phạm Luật an toàn hàng không",
                    "situation": "formal"
                },
                {
                    "ko": "조종사 과로는 항공안전에 큰 위협입니다",
                    "vi": "Mệt mỏi của phi công là mối đe dọa lớn cho an toàn hàng không",
                    "situation": "onsite"
                },
                {
                    "ko": "한국은 ICAO 항공안전 감사에서 최고 등급을 받았습니다",
                    "vi": "Hàn Quốc đạt hạng cao nhất trong kiểm tra an toàn hàng không của ICAO",
                    "situation": "formal"
                }
            ],
            "relatedTerms": ["감항성", "항공사고", "ICAO", "운항정지"]
        },
        {
            "slug": "tai-nan-hang-khong",
            "korean": "항공사고",
            "vietnamese": "Tai nạn hàng không",
            "hanja": "航空事故",
            "hanjaReading": "航(다닐 항) + 空(빌 공) + 事(일 사) + 故(연고 고)",
            "pronunciation": "항공사고",
            "meaningKo": "항공기의 운항 중 발생한 사망·중상 또는 항공기 파손 사고를 말합니다. 통역 시 한국 항공·철도사고조사위원회가 독립적으로 조사하며, 사고 원인 규명과 재발 방지가 목적이고, 조사 결과는 형사처벌과 별개이며, 항공사는 몬트리올협약에 따라 손해배상 책임을 진다는 점을 명확히 전달해야 합니다.",
            "meaningVi": "Tai nạn tử vong, thương nặng hoặc hư hỏng tàu bay xảy ra trong quá trình vận hành tàu bay. Ở Hàn Quốc Ủy ban điều tra tai nạn hàng không và đường sắt điều tra độc lập, mục đích làm rõ nguyên nhân và phòng ngừa tái diễn, kết quả điều tra riêng với xử lý hình sự, hãng hàng không chịu trách nhiệm bồi thường thiệt hại theo Công ước Montreal.",
            "context": "항공사고 조사 및 손해배상 청구 상황에서 사용",
            "culturalNote": "한국은 항공사고 발생 시 국토교통부와 조사위원회가 즉시 출동하여 블랙박스 분석과 현장 조사를 실시합니다. 조사는 최소 6개월~수년 소요되며, 보고서는 공개됩니다. 아시아나 214편 사고(2013)처럼 국제 공조 조사도 빈번합니다. 베트남은 항공사고 조사 역량이 약해 통역 시 한국의 과학적 조사 시스템을 설명해야 합니다.",
            "commonMistakes": [
                {
                    "mistake": "máy bay rơi",
                    "correction": "tai nạn hàng không (추락만이 아님)",
                    "explanation": "'항공기 추락'은 추락 사고만 의미하며 충돌·화재 등이 누락됩니다"
                },
                {
                    "mistake": "sự cố bay",
                    "correction": "tai nạn hàng không (사고) vs sự cố (준사고)",
                    "explanation": "'비행 사건'은 경미한 문제이며 사망·중상을 수반하는 사고와 다릅니다"
                },
                {
                    "mistake": "va chạm máy bay",
                    "correction": "tai nạn hàng không (포괄적)",
                    "explanation": "'항공기 충돌'은 충돌 사고만 지칭하여 범위가 좁습니다"
                }
            ],
            "examples": [
                {
                    "ko": "항공사고 조사에는 평균 2년이 소요됩니다",
                    "vi": "Điều tra tai nạn hàng không trung bình mất 2 năm",
                    "situation": "formal"
                },
                {
                    "ko": "항공사고로 다쳤는데 보상받을 수 있나요?",
                    "vi": "Bị thương do tai nạn hàng không, có được bồi thường không?",
                    "situation": "onsite"
                },
                {
                    "ko": "항공사고 조사는 형사처벌이 아닌 재발 방지가 목적입니다",
                    "vi": "Điều tra tai nạn hàng không nhằm phòng ngừa tái diễn chứ không phải xử phạt hình sự",
                    "situation": "formal"
                }
            ],
            "relatedTerms": ["사고조사위원회", "블랙박스", "몬트리올협약", "손해배상"]
        },
        {
            "slug": "an-ninh-hang-khong",
            "korean": "항공보안",
            "vietnamese": "An ninh hàng không",
            "hanja": "航空保安",
            "hanjaReading": "航(다닐 항) + 空(빌 공) + 保(지킬 보) + 安(편안할 안)",
            "pronunciation": "항공보안",
            "meaningKo": "항공기·공항시설·승객에 대한 불법행위(테러·납치·폭발물 등)를 예방하고 대응하는 체계를 말합니다. 통역 시 한국 항공보안법은 보안검색·접근통제·경비를 의무화하며, 보안검색 거부 시 탑승 불가, 보안 위협 행위 시 10년 이하 징역, 국제적으로 시카고협약과 도쿄·헤이그·몬트리올 협약을 준수한다는 점을 명확히 전달해야 합니다.",
            "meaningVi": "Hệ thống phòng ngừa và ứng phó hành vi bất hợp pháp (khủng bố, bắt cóc, chất nổ) đối với tàu bay, cơ sở sân bay, hành khách. Luật an ninh hàng không Hàn Quốc bắt buộc kiểm tra an ninh, kiểm soát ra vào, canh gác, từ chối kiểm tra an ninh không được lên máy bay, hành vi đe dọa an ninh bị phạt tù 10 năm, tuân thủ Công ước Chicago và Tokyo, Hague, Montreal quốc tế.",
            "context": "공항 보안검색 및 항공보안 위반 사건에서 사용",
            "culturalNote": "한국은 9·11 테러 이후 항공보안을 대폭 강화했으며, 인천공항은 세계 최고 수준의 보안 시스템을 갖추고 있습니다. 액체물 제한·신발 검사·생체인식 등을 도입하며, 기내 난동 승객에 대한 처벌도 강화되었습니다. 베트남은 보안 검색이 느슨해 통역 시 한국의 엄격한 보안 기준을 설명해야 합니다.",
            "commonMistakes": [
                {
                    "mistake": "an toàn hàng không",
                    "correction": "an ninh hàng không (보안) vs an toàn (안전)",
                    "explanation": "'항공안전'은 사고 예방이며, '항공보안'은 테러 방지로 구분됩니다"
                },
                {
                    "mistake": "kiểm tra sân bay",
                    "correction": "an ninh hàng không (체계 전반)",
                    "explanation": "'공항 검사'는 일부 절차이며 보안 체계 전반을 포함하지 못합니다"
                },
                {
                    "mistake": "bảo vệ máy bay",
                    "correction": "an ninh hàng không (법적 체계)",
                    "explanation": "'항공기 보호'는 일상 표현이며 법적 보안 체계의 개념이 누락됩니다"
                }
            ],
            "examples": [
                {
                    "ko": "보안검색을 거부하면 탑승이 거부됩니다",
                    "vi": "Từ chối kiểm tra an ninh sẽ bị từ chối lên máy bay",
                    "situation": "formal"
                },
                {
                    "ko": "액체는 100mL 이하만 기내 반입 가능합니다",
                    "vi": "Chỉ được mang chất lỏng dưới 100mL lên máy bay",
                    "situation": "onsite"
                },
                {
                    "ko": "기내 난동 시 항공보안법 위반으로 10년 이하 징역에 처해집니다",
                    "vi": "Gây rối trên máy bay vi phạm Luật an ninh hàng không, bị phạt tù đến 10 năm",
                    "situation": "formal"
                }
            ],
            "relatedTerms": ["보안검색", "테러", "기내난동", "국제협약"]
        },
        {
            "slug": "giay-phep-lai-may-bay",
            "korean": "조종사면허",
            "vietnamese": "Giấy phép lái máy bay",
            "hanja": "操縱士免許",
            "hanjaReading": "操(잡을 조) + 縱(세로 종) + 士(선비 사) + 免(면할 면) + 許(허락할 허)",
            "pronunciation": "조종사면허",
            "meaningKo": "항공기를 조종할 수 있는 자격을 인정하는 면허로, 자가용·사업용·운송용으로 구분됩니다. 통역 시 한국은 항공안전법에 따라 학과·실기 시험을 거쳐 국토교통부가 발급하며, 1~5년마다 정기 신체검사와 비행 경력 유지가 필요하고, 무면허 조종 시 10년 이하 징역에 처해진다는 점을 명확히 전달해야 합니다.",
            "meaningVi": "Giấy phép công nhận tư cách lái tàu bay, chia thành cá nhân, thương mại, vận tải. Ở Hàn Quốc theo Luật an toàn hàng không phải qua thi lý thuyết và thực hành do Bộ Giao thông Đất đai cấp, cần khám sức khỏe định kỳ 1-5 năm và duy trì kinh nghiệm bay, lái không phép bị phạt tù đến 10 năm.",
            "context": "조종사 면허 취득 및 갱신 절차에서 사용",
            "culturalNote": "한국은 조종사 양성을 대학(한국항공대 등)과 비행학교에서 담당하며, 군 출신 조종사도 많습니다. 면허는 비행기·헬리콥터·글라이더 등 기종별로 구분되며, 영어 능력도 필수입니다. 베트남은 조종사 부족으로 해외에서 양성하며 통역 시 한국의 체계적 교육 시스템을 설명해야 합니다.",
            "commonMistakes": [
                {
                    "mistake": "bằng lái phi công",
                    "correction": "giấy phép lái máy bay (법적 용어)",
                    "explanation": "'조종사 운전면허'는 비공식적이며 법률 용어로 부적절합니다"
                },
                {
                    "mistake": "chứng chỉ bay",
                    "correction": "giấy phép lái máy bay (면허)",
                    "explanation": "'비행 증명서'는 자격증처럼 들리며 면허의 법적 성격이 약화됩니다"
                },
                {
                    "mistake": "giấy phép phi công",
                    "correction": "giấy phép lái máy bay",
                    "explanation": "'조종사 면허'는 의미는 맞으나 공식 용어는 '항공기 조종 면허'입니다"
                }
            ],
            "examples": [
                {
                    "ko": "운송용 조종사 면허를 취득하려면 최소 1,500시간 비행 경력이 필요합니다",
                    "vi": "Để có giấy phép lái máy bay vận tải cần tối thiểu 1.500 giờ kinh nghiệm bay",
                    "situation": "formal"
                },
                {
                    "ko": "조종사 면허 시험은 어떻게 준비하나요?",
                    "vi": "Thi giấy phép lái máy bay chuẩn bị thế nào?",
                    "situation": "onsite"
                },
                {
                    "ko": "조종사는 매년 신체검사를 받아야 면허가 유지됩니다",
                    "vi": "Phi công phải khám sức khỏe hàng năm để giữ giấy phép",
                    "situation": "formal"
                }
            ],
            "relatedTerms": ["항공안전법", "비행경력", "신체검사", "자가용조종사"]
        },
        {
            "slug": "may-bay-khong-nguoi-lai",
            "korean": "무인항공기",
            "vietnamese": "Máy bay không người lái",
            "hanja": "無人航空機",
            "hanjaReading": "無(없을 무) + 人(사람 인) + 航(다닐 항) + 空(빌 공) + 機(틀 기)",
            "pronunciation": "무인항공기",
            "meaningKo": "사람이 탑승하지 않고 원격 조종 또는 자동으로 비행하는 항공기(드론)를 말합니다. 통역 시 한국 항공안전법은 250g 이상 드론을 신고 대상으로 하며, 2kg 이상은 자격증 필요, 관제권·비행금지구역 비행 금지, 야간·목시외 비행 승인 필요, 위반 시 1년 이하 징역 또는 1천만 원 이하 벌금에 처해진다는 점을 명확히 전달해야 합니다.",
            "meaningVi": "Tàu bay (drone) không có người lái, bay bằng điều khiển từ xa hoặc tự động. Luật an toàn hàng không Hàn Quốc quy định drone từ 250g phải đăng ký, từ 2kg cần chứng chỉ, cấm bay vùng kiểm soát/cấm bay, bay đêm/ngoài tầm nhìn cần phê duyệt, vi phạm bị phạt tù 1 năm hoặc phạt tiền đến 10 triệu won.",
            "context": "드론 등록·운용 규제 및 단속 상황에서 사용",
            "culturalNote": "한국은 드론 산업 육성과 안전 규제를 병행하며, 배송·촬영·방역 등 다양한 분야에서 활용됩니다. 청와대·원전 등 중요시설 상공은 비행금지구역이며, 위반 시 드론을 격추할 수 있습니다. 베트남도 드론 사용이 증가하나 규제가 약해 통역 시 한국의 체계적 관리를 설명해야 합니다.",
            "commonMistakes": [
                {
                    "mistake": "drone",
                    "correction": "máy bay không người lái (또는 drone)",
                    "explanation": "드론도 통용되지만 공식 용어는 '무인항공기'이며 통역 시 둘 다 사용 가능합니다"
                },
                {
                    "mistake": "máy bay điều khiển",
                    "correction": "máy bay không người lái (무인 강조)",
                    "explanation": "'조종 항공기'는 사람이 타는 원격조종도 포함되어 무인의 의미가 약화됩니다"
                },
                {
                    "mistake": "thiết bị bay",
                    "correction": "máy bay không người lái (항공기)",
                    "explanation": "'비행 장치'는 일반 기기이며 항공기로서의 법적 성격이 누락됩니다"
                }
            ],
            "examples": [
                {
                    "ko": "2kg 이상 드론을 조종하려면 자격증을 취득해야 합니다",
                    "vi": "Để lái drone từ 2kg trở lên phải có chứng chỉ",
                    "situation": "formal"
                },
                {
                    "ko": "공항 근처에서 드론 날리면 안 되나요?",
                    "vi": "Gần sân bay không được bay drone à?",
                    "situation": "onsite"
                },
                {
                    "ko": "무인항공기 무단 비행 시 격추 조치될 수 있습니다",
                    "vi": "Bay máy bay không người lái không phép có thể bị bắn hạ",
                    "situation": "formal"
                }
            ],
            "relatedTerms": ["드론", "비행금지구역", "드론자격증", "항공안전법"]
        },
        {
            "slug": "van-chuyen-hang-khong",
            "korean": "항공운송",
            "vietnamese": "Vận chuyển hàng không",
            "hanja": "航空運送",
            "hanjaReading": "航(다닐 항) + 空(빌 공) + 運(옮길 운) + 送(보낼 송)",
            "pronunciation": "항공운송",
            "meaningKo": "항공기를 이용하여 여객이나 화물을 운송하는 사업을 말합니다. 통역 시 한국 항공사업법은 항공운송사업 면허를 국토교통부가 심사·허가하며, 면허 없이 영업 시 5년 이하 징역, 운임은 신고제, 초과예약·지연 시 보상 의무가 있으며, 국제 운송은 바르샤바·몬트리올 협약을 준수한다는 점을 명확히 전달해야 합니다.",
            "meaningVi": "Kinh doanh vận chuyển hành khách hoặc hàng hóa bằng tàu bay. Luật kinh doanh hàng không Hàn Quốc quy định giấy phép kinh doanh vận chuyển hàng không do Bộ Giao thông Đất đai thẩm tra và cấp, kinh doanh không phép bị phạt tù 5 năm, giá vé chế độ khai báo, đặt chỗ quá mức/chậm trễ có nghĩa vụ bồi thường, vận chuyển quốc tế tuân thủ Công ước Warsaw và Montreal.",
            "context": "항공사 운영 및 승객 권리 보호 상황에서 사용",
            "culturalNote": "한국은 대한항공·아시아나항공 등 대형 항공사와 저비용항공사(LCC)가 경쟁하며, 항공 자유화로 국제선이 확대되었습니다. 소비자 보호를 위해 초과예약 보상·지연 배상·수하물 분실 책임이 강화되었습니다. 베트남도 항공 산업이 성장 중이나 소비자 보호가 약해 통역 시 한국의 보상 제도를 설명해야 합니다.",
            "commonMistakes": [
                {
                    "mistake": "hàng không",
                    "correction": "vận chuyển hàng không (운송 사업)",
                    "explanation": "'항공'은 포괄적이며 운송 사업의 의미가 누락됩니다"
                },
                {
                    "mistake": "chở khách máy bay",
                    "correction": "vận chuyển hàng không (여객 + 화물)",
                    "explanation": "'항공기 승객 운송'은 여객만 의미하며 화물 운송이 제외됩니다"
                },
                {
                    "mistake": "dịch vụ bay",
                    "correction": "vận chuyển hàng không (법적 사업)",
                    "explanation": "'비행 서비스'는 일상 표현이며 법적 운송 사업의 개념이 약화됩니다"
                }
            ],
            "examples": [
                {
                    "ko": "항공운송사업 면허는 재무 건전성과 안전성을 심사받습니다",
                    "vi": "Giấy phép kinh doanh vận chuyển hàng không được thẩm tra về tính lành mạnh tài chính và an toàn",
                    "situation": "formal"
                },
                {
                    "ko": "비행기 연착되면 보상받을 수 있나요?",
                    "vi": "Máy bay chậm có được bồi thường không?",
                    "situation": "onsite"
                },
                {
                    "ko": "국제 항공운송은 몬트리올협약에 따라 배상 한도가 정해져 있습니다",
                    "vi": "Vận chuyển hàng không quốc tế có hạn mức bồi thường theo Công ước Montreal",
                    "situation": "formal"
                }
            ],
            "relatedTerms": ["항공사업법", "몬트리올협약", "초과예약", "운송약관"]
        },
        {
            "slug": "cong-uoc-montreal",
            "korean": "몬트리올협약",
            "vietnamese": "Công ước Montreal",
            "hanja": None,
            "hanjaReading": None,
            "pronunciation": "몬트리올협약",
            "meaningKo": "국제항공운송에서 여객·수하물·화물의 손해배상 책임을 통일한 국제협약입니다. 통역 시 1999년 채택되어 바르샤바협약을 대체했으며, 사망·상해는 무한 책임, 지연은 4,150 SDR(약 7백만 원), 수하물 분실은 1,131 SDR(약 2백만 원) 한도로 배상하며, 한국은 2007년 가입했다는 점을 명확히 전달해야 합니다.",
            "meaningVi": "Công ước quốc tế thống nhất trách nhiệm bồi thường thiệt hại hành khách, hành lý, hàng hóa trong vận chuyển hàng không quốc tế. Được thông qua năm 1999 thay thế Công ước Warsaw, tử vong/thương tích trách nhiệm vô hạn, chậm trễ bồi thường đến 4.150 SDR (khoảng 7 triệu won), mất hành lý đến 1.131 SDR (khoảng 2 triệu won), Hàn Quốc gia nhập năm 2007.",
            "context": "국제항공 분쟁 및 손해배상 청구 상황에서 사용",
            "culturalNote": "한국은 몬트리올협약 가입으로 국제 항공 분쟁 시 예측 가능한 배상 기준을 확보했습니다. SDR(특별인출권)은 IMF 통화 단위로 환율에 따라 변동하며, 승객은 약관에서 배상 한도를 확인할 수 있습니다. 베트남도 가입국이나 인지도가 낮아 통역 시 협약의 배상 한도를 설명해야 합니다.",
            "commonMistakes": [
                {
                    "mistake": "hiệp định Montreal",
                    "correction": "công ước Montreal (국제협약)",
                    "explanation": "'협정'은 양국 간이며, '공약'은 다자간 조약으로 구분됩니다"
                },
                {
                    "mistake": "luật hàng không Montreal",
                    "correction": "công ước Montreal (국제협약, 법률 아님)",
                    "explanation": "'몬트리올 항공법'은 국내법처럼 들리며 국제협약의 성격이 누락됩니다"
                },
                {
                    "mistake": "quy định Montreal",
                    "correction": "công ước Montreal (조약)",
                    "explanation": "'몬트리올 규정'은 행정규칙처럼 들리며 조약의 법적 지위가 약화됩니다"
                }
            ],
            "examples": [
                {
                    "ko": "국제선 수하물 분실 시 몬트리올협약에 따라 최대 약 200만 원까지 배상받을 수 있습니다",
                    "vi": "Khi mất hành lý chuyến bay quốc tế có thể được bồi thường tối đa khoảng 2 triệu won theo Công ước Montreal",
                    "situation": "formal"
                },
                {
                    "ko": "항공사가 손해배상을 거부하는데 몬트리올협약으로 청구할 수 있나요?",
                    "vi": "Hãng hàng không từ chối bồi thường, có thể yêu cầu theo Công ước Montreal không?",
                    "situation": "onsite"
                },
                {
                    "ko": "몬트리올협약은 127개국이 가입한 국제협약입니다",
                    "vi": "Công ước Montreal là công ước quốc tế có 127 nước tham gia",
                    "situation": "formal"
                }
            ],
            "relatedTerms": ["바르샤바협약", "SDR", "손해배상", "국제항공운송"]
        },
        {
            "slug": "toi-pham-hang-khong",
            "korean": "항공범죄",
            "vietnamese": "Tội phạm hàng không",
            "hanja": "航空犯罪",
            "hanjaReading": "航(다닐 항) + 空(빌 공) + 犯(범할 범) + 罪(허물 죄)",
            "pronunciation": "항공범죄",
            "meaningKo": "운항 중인 항공기 내에서 또는 항공기·공항에 대해 저지른 범죄로, 납치·폭발물·난동 등을 포함합니다. 통역 시 한국 항공보안법과 항공안전법으로 처벌하며, 항공기 납치는 무기~10년 징역, 폭발물은 무기~7년 징역, 기내 난동은 10년 이하 징역이며, 국제범죄로 도쿄·헤이그·몬트리올 협약을 적용한다는 점을 명확히 전달해야 합니다.",
            "meaningVi": "Tội phạm thực hiện trên tàu bay đang vận hành hoặc đối với tàu bay/sân bay, bao gồm bắt cóc, chất nổ, gây rối. Luật an ninh hàng không và Luật an toàn hàng không Hàn Quốc xử phạt, bắt cóc tàu bay chung thân đến 10 năm tù, chất nổ chung thân đến 7 năm tù, gây rối trên máy bay 10 năm tù, là tội phạm quốc tế áp dụng Công ước Tokyo, Hague, Montreal.",
            "context": "항공범죄 수사 및 국제공조 요청 상황에서 사용",
            "culturalNote": "한국은 항공범죄를 중대범죄로 엄격히 처벌하며, 국제공조를 통해 범인을 검거합니다. 기내 난동(폭행·성추행·흡연 등)이 증가하며 처벌이 강화되었고, 술에 취한 승객도 엄중 처벌됩니다. 베트남도 항공범죄 규정이 있으나 처벌이 약해 통역 시 한국의 높은 처벌 수위를 설명해야 합니다.",
            "commonMistakes": [
                {
                    "mistake": "tội phạm trên máy bay",
                    "correction": "tội phạm hàng không (항공기 + 공항)",
                    "explanation": "'항공기 내 범죄'는 기내만 의미하며 공항 범죄가 누락됩니다"
                },
                {
                    "mistake": "bắt cóc máy bay",
                    "correction": "tội phạm hàng không (납치는 일부)",
                    "explanation": "'항공기 납치'는 항공범죄의 한 유형이며 전체를 대표하지 못합니다"
                },
                {
                    "mistake": "vi phạm hàng không",
                    "correction": "tội phạm hàng không (범죄) vs vi phạm (위반)",
                    "explanation": "'항공 위반'은 경미한 규정 위반이며 범죄의 심각성이 약화됩니다"
                }
            ],
            "examples": [
                {
                    "ko": "기내에서 승무원을 폭행한 승객은 항공범죄로 10년 이하 징역에 처해집니다",
                    "vi": "Hành khách hành hung tiếp viên trên máy bay bị phạt tù đến 10 năm vì tội phạm hàng không",
                    "situation": "formal"
                },
                {
                    "ko": "비행 중에 흡연하면 어떻게 되나요?",
                    "vi": "Hút thuốc trong lúc bay thì sao?",
                    "situation": "onsite"
                },
                {
                    "ko": "항공범죄는 국제협약에 따라 범인을 어느 나라에서든 처벌할 수 있습니다",
                    "vi": "Tội phạm hàng không theo công ước quốc tế có thể xử phạt tội phạm ở bất kỳ nước nào",
                    "situation": "formal"
                }
            ],
            "relatedTerms": ["항공기납치", "기내난동", "도쿄협약", "국제공조"]
        },
        {
            "slug": "co-so-san-bay",
            "korean": "공항시설",
            "vietnamese": "Cơ sở sân bay",
            "hanja": "空港施設",
            "hanjaReading": "空(빌 공) + 港(항구 항) + 施(베풀 시) + 設(베풀 설)",
            "pronunciation": "공항시설",
            "meaningKo": "항공기의 이착륙과 여객·화물 처리를 위한 활주로·여객터미널·화물터미널·관제탑 등의 시설을 말합니다. 통역 시 한국 공항시설법은 국가·지자체·민간이 설치·운영하며, 인천공항은 공사가 관리하고, 시설 훼손 시 5년 이하 징역 또는 5천만 원 이하 벌금, 무단 침입 시 3년 이하 징역에 처해진다는 점을 명확히 전달해야 합니다.",
            "meaningVi": "Các cơ sở như đường băng, nhà ga hành khách, nhà ga hàng hóa, tháp kiểm soát để phục vụ cất hạ cánh tàu bay và xử lý hành khách, hàng hóa. Luật cơ sở sân bay Hàn Quốc quy định quốc gia, chính quyền địa phương, tư nhân lắp đặt và vận hành, sân bay Incheon do công ty quản lý, phá hoại cơ sở bị phạt tù 5 năm hoặc phạt tiền đến 50 triệu won, xâm nhập không phép bị phạt tù 3 năm.",
            "context": "공항 시설 관리 및 보안 구역 침입 사건에서 사용",
            "culturalNote": "한국은 인천국제공항을 허브공항으로 육성하며 세계 최고 수준의 시설을 갖추었습니다. 김포·김해·제주 등 지방공항도 현대화하고 있으며, 민자 투자도 활발합니다. 공항 보안구역 무단 침입은 엄격히 처벌됩니다. 베트남은 공항 인프라가 부족해 통역 시 한국의 선진 시설을 설명해야 합니다.",
            "commonMistakes": [
                {
                    "mistake": "sân bay",
                    "correction": "cơ sở sân bay (시설 중심)",
                    "explanation": "'공항'은 장소이며 '공항시설'은 구체적 시설물을 의미합니다"
                },
                {
                    "mistake": "thiết bị sân bay",
                    "correction": "cơ sở sân bay (건축물 + 장비)",
                    "explanation": "'공항 장비'는 기계만 연상되며 건축물이 누락됩니다"
                },
                {
                    "mistake": "nhà ga",
                    "correction": "cơ sở sân bay (터미널은 일부)",
                    "explanation": "'터미널'은 공항시설의 일부이며 전체를 포함하지 못합니다"
                }
            ],
            "examples": [
                {
                    "ko": "인천공항 제2여객터미널은 2018년 개장한 최신 공항시설입니다",
                    "vi": "Nhà ga hành khách số 2 sân bay Incheon là cơ sở sân bay mới nhất khai trương năm 2018",
                    "situation": "formal"
                },
                {
                    "ko": "활주로는 일반인 출입 금지 구역인가요?",
                    "vi": "Đường băng có phải khu vực cấm người thường vào không?",
                    "situation": "onsite"
                },
                {
                    "ko": "공항시설 보안구역에 무단 침입하면 형사처벌을 받습니다",
                    "vi": "Xâm nhập không phép vào khu an ninh cơ sở sân bay sẽ bị xử lý hình sự",
                    "situation": "formal"
                }
            ],
            "relatedTerms": ["활주로", "여객터미널", "관제탑", "인천공항"]
        },
        {
            "slug": "duong-bay-hang-khong",
            "korean": "항공노선",
            "vietnamese": "Đường bay hàng không",
            "hanja": "航空路線",
            "hanjaReading": "航(다닐 항) + 空(빌 공) + 路(길 로) + 線(줄 선)",
            "pronunciation": "항공노선",
            "meaningKo": "항공기가 정기적으로 운항하는 출발지와 목적지를 연결하는 노선을 말합니다. 통역 시 한국 항공사업법은 국제선은 항공자유화로 항공사가 자율 개설하지만 외교·안보 고려 필요하고, 국내선은 독점 방지를 위해 복수 항공사 운항을 유도하며, 적자 노선은 공공성 유지를 위해 보조금을 지원한다는 점을 명확히 전달해야 합니다.",
            "meaningVi": "Đường bay kết nối điểm xuất phát và điểm đến mà tàu bay vận hành thường xuyên. Luật kinh doanh hàng không Hàn Quốc quy định chuyến quốc tế do tự do hóa hàng không nên hãng hàng không tự mở nhưng cần xem xét ngoại giao và an ninh, chuyến nội địa khuyến khích nhiều hãng vận hành để chống độc quyền, đường bay thua lỗ được trợ cấp để duy trì tính công cộng.",
            "context": "항공노선 개설 및 운항 정책 논의 상황에서 사용",
            "culturalNote": "한국은 항공자유화로 국제선이 크게 확대되었으며, 저비용항공사(LCC)가 다양한 노선을 개설하고 있습니다. 제주·김포 등 주요 노선은 경쟁이 치열하며, 울릉도·백령도 등 도서 노선은 공익성으로 보조금을 지원합니다. 베트남도 항공 노선이 증가하나 인프라 부족으로 혼잡합니다. 통역 시 한국의 노선 다양성을 설명해야 합니다.",
            "commonMistakes": [
                {
                    "mistake": "chuyến bay",
                    "correction": "đường bay hàng không (노선) vs chuyến bay (편명)",
                    "explanation": "'비행편'은 개별 운항이며 '노선'은 정기 운항 경로로 구분됩니다"
                },
                {
                    "mistake": "tuyến đường bay",
                    "correction": "đường bay hàng không",
                    "explanation": "'비행 노선'은 의미는 맞으나 '항공노선'이 더 간결하고 공식적입니다"
                },
                {
                    "mistake": "lộ trình bay",
                    "correction": "đường bay hàng không (정기 노선)",
                    "explanation": "'비행 경로'는 개별 비행의 루트이며 정기 노선의 개념이 약화됩니다"
                }
            ],
            "examples": [
                {
                    "ko": "인천-하노이 노선은 하루 10편 이상 운항합니다",
                    "vi": "Đường bay Incheon-Hà Nội vận hành hơn 10 chuyến mỗi ngày",
                    "situation": "formal"
                },
                {
                    "ko": "새로운 국제선 노선을 개설하려면 양국 정부 협의가 필요한가요?",
                    "vi": "Muốn mở đường bay quốc tế mới có cần thỏa thuận chính phủ hai nước không?",
                    "situation": "onsite"
                },
                {
                    "ko": "울릉도 항공노선은 공익성 유지를 위해 국가가 보조금을 지원합니다",
                    "vi": "Đường bay Ulleungdo được nhà nước trợ cấp để duy trì tính công ích",
                    "situation": "formal"
                }
            ],
            "relatedTerms": ["항공자유화", "국제선", "국내선", "저비용항공사"]
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
    print(f"✅ Added {len(filtered)} terms (항공/우주법). Total: {len(data)}")

if __name__ == '__main__':
    main()
