#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""노동법 심화 용어 추가 스크립트 (v6-a)"""

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
            "slug": "thuong-luong-tap-the",
            "korean": "단체교섭",
            "vietnamese": "Thương lượng tập thể",
            "hanja": "團體交涉",
            "hanjaReading": "團(모일 단) + 體(몸 체) + 交(사귈 교) + 涉(건널 섭)",
            "pronunciation": "트엉 르엉 떱 테",
            "meaningKo": "근로자단체(노동조합)와 사용자 또는 사용자단체가 임금, 근로시간, 복지 등 근로조건에 관한 사항을 협의하여 단체협약을 체결하는 절차. 통역 시 주의할 점은 베트남에서는 기업별 노조가 대부분이며 산업별·직종별 교섭이 드물다는 점을 설명해야 한다. 한국의 복수노조 교섭창구 단일화 제도는 베트남에 없으므로 이 개념을 설명할 때는 배경 설명이 필요하다. 교섭 결렬 시 조정·중재 절차도 양국이 다르므로 통역 시 구분이 중요하다.",
            "meaningVi": "Quá trình đàm phán giữa tổ chức đại diện người lao động (công đoàn) và người sử dụng lao động hoặc tổ chức đại diện người sử dụng lao động về các điều kiện lao động như tiền lương, thời giờ làm việc, phúc lợi nhằm ký kết thỏa ước lao động tập thể. Tại Việt Nam, công đoàn cơ sở doanh nghiệp chiếm đa số, ít có thương lượng theo ngành nghề như Hàn Quốc.",
            "context": "노동법, 단체협약, 노사관계, 노동조합 활동에서 사용. 교섭 결렬 시 조정·중재 절차로 이어진다.",
            "culturalNote": "한국은 산업별·지역별 교섭도 활발하지만 베트남은 기업별 노조 중심이며 정부의 노사관계 개입이 상대적으로 강하다. 한국의 교섭창구 단일화 제도는 베트남에 존재하지 않는다. 베트남 노동법(2019)에서는 단체교섭권을 명시하지만 실무에서는 협상력이 한국보다 약한 편이다. 통역 시 양국 교섭 관행의 차이를 설명하면 이해도가 높아진다.",
            "commonMistakes": [
                {
                    "mistake": "Thương lượng cá nhân",
                    "correction": "Thương lượng tập thể",
                    "explanation": "단체교섭은 개인이 아닌 집단(노조) 차원의 협상이므로 '집단'을 뜻하는 'tập thể'를 반드시 사용해야 한다."
                },
                {
                    "mistake": "협상을 '협의(Hội ý)'로만 번역",
                    "correction": "Thương lượng (정식 교섭) vs Hội ý (일반 협의)",
                    "explanation": "법적 구속력 있는 단체교섭은 'Thương lượng'으로 표현해야 하며, 단순 의견 교환은 'Hội ý'로 구분한다."
                },
                {
                    "mistake": "교섭창구 단일화를 그대로 직역",
                    "correction": "한국 고유 제도임을 설명 후 의역",
                    "explanation": "베트남에 없는 제도이므로 '복수 노조 존재 시 하나의 교섭 대표를 정하는 한국 제도'로 풀어서 설명해야 한다."
                }
            ],
            "examples": [
                {
                    "ko": "노동조합은 내년도 임금 인상을 위해 사측과 단체교섭을 진행하고 있습니다.",
                    "vi": "Công đoàn đang tiến hành thương lượng tập thể với phía sử dụng lao động để tăng lương năm sau.",
                    "situation": "formal"
                },
                {
                    "ko": "단체교섭이 결렬되어 노동위원회의 조정 절차에 들어갔습니다.",
                    "vi": "Thương lượng tập thể đã thất bại nên đã chuyển sang thủ tục hòa giải của Ủy ban quan hệ lao động.",
                    "situation": "formal"
                },
                {
                    "ko": "현장에서 단체교섭 요구가 나왔는데 어떻게 대응해야 할까요?",
                    "vi": "Có yêu cầu thương lượng tập thể từ hiện trường thì nên phản hồi như thế nào?",
                    "situation": "onsite"
                }
            ],
            "relatedTerms": ["단체협약", "노동조합", "조정", "중재", "쟁의행위"]
        },
        {
            "slug": "dinh-cong",
            "korean": "파업",
            "vietnamese": "Đình công",
            "hanja": "罷業",
            "hanjaReading": "罷(그칠 파) + 業(일 업)",
            "pronunciation": "딘 꽁",
            "meaningKo": "근로자들이 근로조건 개선이나 요구사항 관철을 위해 집단적으로 노무 제공을 거부하는 쟁의행위. 통역 시 주의할 점은 한국은 합법 파업 요건이 까다로운 반면(쟁의조정 전치주의, 조합원 찬성 등), 베트남도 노동법상 파업 전 조정 절차를 거쳐야 하지만 실무상 비공식 파업이 빈번하다는 점이다. 한국의 '필수공익사업' 개념과 베트남의 파업 제한 업종도 차이가 있으므로 통역 시 구체적 설명이 필요하다. 불법 파업 시 법적 책임도 양국이 다르다.",
            "meaningVi": "Hành vi ngừng việc tập thể của người lao động nhằm yêu cầu cải thiện điều kiện làm việc hoặc đòi quyền lợi chính đáng. Theo Bộ luật Lao động Việt Nam 2019, đình công phải qua thủ tục hòa giải trước, tuy nhiên trên thực tế có nhiều cuộc đình công tự phát chưa qua thủ tục pháp lý.",
            "context": "노동쟁의, 노사분규, 근로조건 협상 결렬 시 발생. 합법 파업과 불법 파업 구분이 중요하다.",
            "culturalNote": "한국은 파업 전 조정 절차, 조합원 찬성투표 등 엄격한 요건이 있으며 필수공익사업은 직권중재 대상이다. 베트남도 법적으로는 사전 조정 의무가 있으나 실제로는 급여 미지급, 근로조건 악화 시 자발적 파업이 많다. 한국은 파업 시 임금 지급 의무가 없지만 베트남은 사용자 귀책 파업이면 임금 지급 의무가 있을 수 있다. 통역 시 양국의 파업 문화와 법적 요건 차이를 명확히 해야 오해를 줄인다.",
            "commonMistakes": [
                {
                    "mistake": "Ngừng việc (일반 업무 중단)",
                    "correction": "Đình công (집단 파업)",
                    "explanation": "'Ngừng việc'은 개인적 업무 중단이고, 'Đình công'은 집단적 쟁의행위로서의 파업을 의미한다."
                },
                {
                    "mistake": "합법 파업을 'Đình công hợp pháp'으로만 표현",
                    "correction": "Đình công hợp pháp (법 요건 충족) vs Đình công tự phát (자발적 파업)",
                    "explanation": "베트남 현장에서는 절차를 거치지 않은 자발적 파업이 많으므로 'tự phát' 개념을 추가 설명해야 한다."
                },
                {
                    "mistake": "필수공익사업을 직역",
                    "correction": "한국 법 개념 설명 후 베트남 대응 개념 제시",
                    "explanation": "한국의 필수공익사업(병원, 철도 등)과 베트남의 파업 금지 업종이 일치하지 않으므로 구체적 설명이 필요하다."
                }
            ],
            "examples": [
                {
                    "ko": "근로자들은 임금 인상 요구가 받아들여지지 않자 합법 파업에 돌입했습니다.",
                    "vi": "Người lao động đã tiến hành đình công hợp pháp sau khi yêu cầu tăng lương không được chấp nhận.",
                    "situation": "formal"
                },
                {
                    "ko": "이 공장에서 파업이 발생했는데 절차를 제대로 밟지 않은 불법 파업입니다.",
                    "vi": "Nhà máy này đã xảy ra đình công tự phát, chưa qua thủ tục pháp lý nên là đình công bất hợp pháp.",
                    "situation": "onsite"
                },
                {
                    "ko": "필수공익사업이라 파업권이 제한되는 업종입니다.",
                    "vi": "Đây là ngành dịch vụ thiết yếu nên quyền đình công bị hạn chế theo pháp luật Hàn Quốc.",
                    "situation": "formal"
                }
            ],
            "relatedTerms": ["쟁의행위", "단체교섭", "노동쟁의", "조정", "직장폐쇄"]
        },
        {
            "slug": "dong-cua-noi-lam-viec",
            "korean": "직장폐쇄",
            "vietnamese": "Đóng cửa nơi làm việc",
            "hanja": "職場閉鎖",
            "hanjaReading": "職(직분 직) + 場(마당 장) + 閉(닫을 폐) + 鎖(자물쇠 쇄)",
            "pronunciation": "동 꾸아 느이 람 비엑",
            "meaningKo": "사용자가 쟁의행위에 대응하여 사업장의 전부 또는 일부를 폐쇄하고 근로자의 근로 제공을 거부하는 행위. 통역 시 주의할 점은 한국에서는 방어적 직장폐쇄와 공격적 직장폐쇄를 구분하며 방어적 폐쇄만 합법으로 인정한다는 점이다. 베트남에서는 직장폐쇄 개념이 법적으로 명확하지 않아 실무상 거의 사용되지 않는다. 한국의 직장폐쇄는 파업에 대한 대응 수단이지만 베트남에서는 사업 중단으로 해석될 수 있어 통역 시 맥락 설명이 필수다.",
            "meaningVi": "Hành vi người sử dụng lao động đóng cửa toàn bộ hoặc một phần cơ sở sản xuất kinh doanh và từ chối tiếp nhận lao động của người lao động để đối phóng với đình công hoặc tranh chấp lao động. Khái niệm này không phổ biến trong pháp luật lao động Việt Nam, chủ yếu tồn tại trong luật Hàn Quốc như một biện pháp phòng thủ hợp pháp của người sử dụng lao động.",
            "context": "노동쟁의, 노사분규 대응 수단으로 사용자 측이 실행. 한국 노동법에서 인정되나 요건이 엄격하다.",
            "culturalNote": "한국 판례상 방어적 직장폐쇄(파업으로 사업 운영이 불가능할 때)만 합법이며, 공격적 폐쇄(근로자 압박 목적)는 불법이다. 베트남 노동법에는 직장폐쇄 개념이 명시되어 있지 않고, 사업장 폐쇄는 주로 경영상 이유나 구조조정 맥락에서만 다뤄진다. 베트남 통역 현장에서 이 용어를 설명할 때는 한국 법제의 독특한 개념임을 강조하고, '파업에 대응한 임시 폐쇄'로 풀어 설명하는 것이 효과적이다.",
            "commonMistakes": [
                {
                    "mistake": "Đóng cửa doanh nghiệp (기업 폐업)",
                    "correction": "Đóng cửa nơi làm việc (임시 작업장 폐쇄)",
                    "explanation": "영구 폐업이 아닌 쟁의 대응 수단으로서의 임시 폐쇄이므로 '작업장(nơi làm việc)'을 사용해야 한다."
                },
                {
                    "mistake": "방어적·공격적 직장폐쇄를 구분하지 않고 번역",
                    "correction": "Đóng cửa phòng thủ vs Đóng cửa tấn công",
                    "explanation": "한국 법상 합법성 여부가 달라지는 중요한 구분이므로 반드시 설명을 덧붙여야 한다."
                },
                {
                    "mistake": "베트남에서 직장폐쇄가 일반적인 것처럼 설명",
                    "correction": "한국 법 고유 개념임을 명시",
                    "explanation": "베트남 노동법에는 이 개념이 없으므로 한국 법제를 설명하는 맥락에서만 사용해야 한다."
                }
            ],
            "examples": [
                {
                    "ko": "회사는 불법 파업에 대응하여 방어적 직장폐쇄를 단행했습니다.",
                    "vi": "Công ty đã thực hiện đóng cửa nơi làm việc mang tính phòng thủ để đối phó với đình công bất hợp pháp.",
                    "situation": "formal"
                },
                {
                    "ko": "직장폐쇄는 파업에 대한 사용자의 정당한 대응 수단이지만 요건이 까다롭습니다.",
                    "vi": "Đóng cửa nơi làm việc là biện pháp đối phó chính đáng của người sử dụng lao động với đình công, nhưng điều kiện thực hiện rất nghiêm ngặt theo luật Hàn Quốc.",
                    "situation": "formal"
                },
                {
                    "ko": "이건 공격적 직장폐쇄로 봐야 해서 불법일 가능성이 높습니다.",
                    "vi": "Trường hợp này có thể bị xem là đóng cửa tấn công nên khả năng cao là bất hợp pháp.",
                    "situation": "onsite"
                }
            ],
            "relatedTerms": ["파업", "쟁의행위", "노동쟁의", "조정", "단체교섭"]
        },
        {
            "slug": "thanh-tra-lao-dong",
            "korean": "근로감독",
            "vietnamese": "Thanh tra lao động",
            "hanja": "勤勞監督",
            "hanjaReading": "勤(부지런할 근) + 勞(일할 로) + 監(볼 감) + 督(살필 독)",
            "pronunciation": "타인 짜 라오 동",
            "meaningKo": "노동관계법령 준수 여부를 확인하고 위반 사항을 시정하기 위해 국가기관(고용노동부)이 실시하는 행정 감독 활동. 통역 시 주의할 점은 한국의 근로감독관은 사법경찰권을 가지며 강제 조사와 처벌이 가능하지만, 베트남의 노동감독관(Thanh tra viên lao động)은 행정 시정 중심이며 처벌권은 제한적이라는 점이다. 정기 감독과 수시 감독, 신고 접수 후 감독 등 절차가 양국이 유사하나 실무 운영 방식에 차이가 있다. 임금 체불, 부당해고, 안전보건 위반 등이 주요 감독 대상이다.",
            "meaningVi": "Hoạt động giám sát hành chính của cơ quan nhà nước (Thanh tra Sở Lao động - Thương binh và Xã hội) nhằm kiểm tra việc tuân thủ pháp luật lao động và yêu cầu khắc phục các vi phạm. Thanh tra viên lao động có quyền thanh tra định kỳ, đột xuất và xử lý vi phạm theo quy định pháp luật Việt Nam, tuy nhiên quyền xử phạt có giới hạn so với Hàn Quốc.",
            "context": "노동법 집행, 사업장 점검, 임금 체불·부당해고·안전보건 위반 조사에서 사용된다.",
            "culturalNote": "한국의 근로감독관은 형사사법권(수사·압수수색·체포)을 가지며 중대재해처벌법 적용 대상 사업장은 처벌이 엄격하다. 베트남의 노동감독관은 주로 행정 시정 명령을 내리고, 형사 처벌은 별도 사법 절차를 거친다. 한국은 정기 감독 외에 근로자 신고에 따른 특별 감독이 활발하나, 베트남은 정기 점검 중심이며 신고 기반 감독은 상대적으로 덜 활성화되어 있다. 통역 시 양국의 감독 권한과 절차 차이를 명확히 해야 혼란을 줄일 수 있다.",
            "commonMistakes": [
                {
                    "mistake": "Kiểm tra lao động (일반 점검)",
                    "correction": "Thanh tra lao động (공식 감독)",
                    "explanation": "'Kiểm tra'는 일반 점검, 'Thanh tra'는 법적 권한을 가진 공식 감독 활동이므로 구분해야 한다."
                },
                {
                    "mistake": "한국 근로감독관의 사법권을 설명하지 않음",
                    "correction": "사법경찰권 보유 명시 (Có quyền tư pháp hình sự)",
                    "explanation": "베트남 감독관과 달리 한국 근로감독관은 체포·수색 권한이 있으므로 이를 명확히 해야 한다."
                },
                {
                    "mistake": "정기 감독과 수시 감독을 혼동",
                    "correction": "Thanh tra định kỳ (정기) vs Thanh tra đột xuất (수시)",
                    "explanation": "감독 유형에 따라 대응 방식이 다르므로 구분이 필요하다."
                }
            ],
            "examples": [
                {
                    "ko": "고용노동부의 근로감독 결과 임금 체불이 적발되어 시정 명령을 받았습니다.",
                    "vi": "Sau thanh tra lao động của Bộ Lao động, đã phát hiện vi phạm nợ lương và nhận lệnh khắc phục.",
                    "situation": "formal"
                },
                {
                    "ko": "근로감독관이 사업장에 방문할 예정이니 서류를 준비해 주세요.",
                    "vi": "Thanh tra viên lao động sẽ đến kiểm tra cơ sở, vui lòng chuẩn bị hồ sơ.",
                    "situation": "onsite"
                },
                {
                    "ko": "익명 신고에 따라 특별 근로감독이 실시될 수 있습니다.",
                    "vi": "Có thể tiến hành thanh tra lao động đặc biệt dựa trên báo cáo ẩn danh.",
                    "situation": "formal"
                }
            ],
            "relatedTerms": ["근로기준법", "임금체불", "부당해고", "산업안전보건법", "고용노동부"]
        },
        {
            "slug": "luong-toi-thieu",
            "korean": "최저임금",
            "vietnamese": "Lương tối thiểu",
            "hanja": "最低賃金",
            "hanjaReading": "最(가장 최) + 低(낮을 저) + 賃(삯 임) + 金(쇠 금)",
            "pronunciation": "르엉 또이 티에우",
            "meaningKo": "근로자의 생활 안정과 노동력의 질적 향상을 위해 국가가 임금의 최저 수준을 정하고 사용자에게 그 이상의 임금을 지급하도록 강제하는 제도. 통역 시 주의할 점은 한국은 전국 단일 최저임금제이나 베트남은 4개 지역별로 다르다는 점이다(Region I~IV, 지역에 따라 월 최저임금이 다름). 한국은 시간급 기준이지만 베트남은 월급 기준이며, 한국은 매년 최저임금위원회 심의로 결정되지만 베트남은 정부 주도로 결정된다. 수습 기간, 청소년 임금 등 세부 규정도 양국이 다르므로 통역 시 구체적 비교 설명이 필요하다.",
            "meaningVi": "Mức lương thấp nhất mà người sử dụng lao động phải trả cho người lao động theo quy định của nhà nước, nhằm đảm bảo đời sống tối thiểu cho người lao động và gia đình. Tại Việt Nam, lương tối thiểu vùng chia thành 4 vùng (Vùng I, II, III, IV) với mức khác nhau, trong khi Hàn Quốc áp dụng mức lương tối thiểu thống nhất toàn quốc tính theo giờ.",
            "context": "근로계약, 임금 협상, 노동법 준수 점검 시 사용. 위반 시 처벌 대상이다.",
            "culturalNote": "한국은 2024년 기준 시간당 9,860원(전국 동일)이며 매년 8월 최저임금위원회가 심의·의결한다. 베트남은 2024년 기준 지역별로 월 480만~630만 VND(약 26만~35만 원) 수준이며 정부가 직접 결정한다. 한국은 수습 기간(3개월 이내) 중 최저임금의 90% 지급이 가능하나 베트남은 수습 기간에도 최저임금의 85~100%를 보장해야 한다. 통역 시 지역별 차이와 단위(시간급 vs 월급) 차이를 명확히 해야 혼선을 막을 수 있다.",
            "commonMistakes": [
                {
                    "mistake": "베트남도 전국 단일 최저임금으로 번역",
                    "correction": "Lương tối thiểu vùng (지역별 최저임금) 4단계",
                    "explanation": "베트남은 지역별로 다르므로 'vùng (지역)'을 반드시 명시해야 한다."
                },
                {
                    "mistake": "시간당 최저임금을 그대로 월급으로 환산하지 않음",
                    "correction": "한국은 시간급, 베트남은 월급 기준임을 설명",
                    "explanation": "단위가 다르므로 비교 시 환산 기준(주 40시간 등)을 명확히 해야 한다."
                },
                {
                    "mistake": "수습 기간 최저임금 예외를 동일하게 설명",
                    "correction": "한국 90% vs 베트남 85~100%로 구분",
                    "explanation": "수습 기간 최저임금 적용 비율이 양국이 다르므로 정확한 수치를 제시해야 한다."
                }
            ],
            "examples": [
                {
                    "ko": "내년도 최저임금이 인상되어 시간당 10,030원으로 결정되었습니다.",
                    "vi": "Lương tối thiểu năm sau đã được tăng lên 10,030 won mỗi giờ (theo quyết định của Ủy ban Lương tối thiểu Hàn Quốc).",
                    "situation": "formal"
                },
                {
                    "ko": "베트남 1지역(하노이, 호치민)의 최저임금은 월 480만 동입니다.",
                    "vi": "Lương tối thiểu vùng I (Hà Nội, TP.HCM) là 4,800,000 VND mỗi tháng.",
                    "situation": "formal"
                },
                {
                    "ko": "수습 기간이라도 최저임금의 90% 이상은 지급해야 합니다.",
                    "vi": "Ngay cả trong thời gian thử việc, phải trả ít nhất 90% lương tối thiểu theo luật Hàn Quốc.",
                    "situation": "onsite"
                }
            ],
            "relatedTerms": ["임금", "근로계약", "수습기간", "근로기준법", "최저임금위원회"]
        },
        {
            "slug": "tien-thoi-viec",
            "korean": "퇴직금",
            "vietnamese": "Tiền thôi việc",
            "hanja": "退職金",
            "hanjaReading": "退(물러날 퇴) + 職(직분 직) + 金(쇠 금)",
            "pronunciation": "띠엔 토이 비엑",
            "meaningKo": "근로자가 퇴직 시 받는 일시금 또는 연금 형태의 급여로, 재직 기간 동안의 공로에 대한 보상. 통역 시 주의할 점은 한국은 계속 근로 1년 이상 시 30일분 평균임금을 의무 지급(근로자퇴직급여 보장법)하지만, 베트남은 근속 1년당 0.5개월 치 평균 급여를 지급한다는 점이다(무기계약 근로자 대상). 한국은 퇴직연금(DC·DB) 제도가 활성화되어 있으나 베트남은 사회보험(BHXH) 중심이며 별도 퇴직금 제도는 제한적이다. 중간 정산 제도도 한국은 예외적으로 허용하지만 베트남은 거의 없다.",
            "meaningVi": "Khoản tiền mà người sử dụng lao động phải trả cho người lao động khi chấm dứt hợp đồng lao động không xác định thời hạn hoặc hợp đồng xác định thời hạn từ 12 tháng trở lên, tính theo mức 0.5 tháng lương bình quân cho mỗi năm làm việc (áp dụng cho người lao động làm việc đủ 12 tháng trở lên). Ở Hàn Quốc, chế độ lương hưu nghỉ việc (퇴직연금) bắt buộc cho doanh nghiệp từ 5 người trở lên và trả ít nhất 1 tháng lương bình quân cho mỗi năm làm việc.",
            "context": "퇴직, 근로계약 종료, 노동법 준수 확인 시 사용. 미지급 시 임금 체불에 해당한다.",
            "culturalNote": "한국은 퇴직급여제도가 법정 의무(5인 이상 사업장)이며 퇴직 전에 임의로 중간 정산이 가능한 경우가 있다(주택 구입 등). 베트남은 무기계약 근로자에게만 퇴직금을 지급하고, 정기계약(계약 기간 명시) 근로자는 대상이 아니다. 한국의 퇴직연금(DC형: 확정기여, DB형: 확정급여)은 베트남에 없는 개념이므로 통역 시 '기업이 적립하는 연금 제도'로 풀어 설명해야 한다. 베트남은 사회보험 탈퇴 시 일시금 수령이 가능하지만 한국의 퇴직금과는 성격이 다르다.",
            "commonMistakes": [
                {
                    "mistake": "Tiền lương hưu (연금)",
                    "correction": "Tiền thôi việc (퇴직 일시금)",
                    "explanation": "'Lương hưu'는 정기 연금, 'Thôi việc'은 퇴직 시 받는 일시금이므로 구분해야 한다."
                },
                {
                    "mistake": "한국 1개월분과 베트남 0.5개월분을 동일하게 표현",
                    "correction": "한국 1개월/년, 베트남 0.5개월/년 명시",
                    "explanation": "지급 기준이 다르므로 정확한 비율을 통역해야 오해가 없다."
                },
                {
                    "mistake": "베트남의 사회보험을 퇴직금으로 번역",
                    "correction": "BHXH (사회보험) vs Tiền thôi việc (퇴직금) 구분",
                    "explanation": "사회보험 일시금과 기업이 지급하는 퇴직금은 별개이므로 혼동하지 말아야 한다."
                }
            ],
            "examples": [
                {
                    "ko": "5년 근속 후 퇴사하면 퇴직금으로 5개월 치 평균임금을 받습니다.",
                    "vi": "Sau 5 năm làm việc, khi nghỉ việc sẽ nhận tiền thôi việc tương đương 5 tháng lương bình quân (theo luật Hàn Quốc: 1 tháng/năm).",
                    "situation": "formal"
                },
                {
                    "ko": "베트남에서는 무기계약 근로자만 퇴직금을 받을 수 있습니다.",
                    "vi": "Ở Việt Nam, chỉ người lao động có hợp đồng không xác định thời hạn mới được nhận tiền thôi việc (0.5 tháng/năm).",
                    "situation": "formal"
                },
                {
                    "ko": "퇴직금을 중간 정산 받으려면 주택 구입 같은 사유가 필요합니다.",
                    "vi": "Để nhận thanh toán tiền thôi việc trước khi nghỉ, cần có lý do như mua nhà (theo quy định Hàn Quốc, không áp dụng ở Việt Nam).",
                    "situation": "onsite"
                }
            ],
            "relatedTerms": ["퇴직연금", "평균임금", "근로계약", "사회보험", "임금체불"]
        },
        {
            "slug": "an-toan-lao-dong",
            "korean": "산업안전",
            "vietnamese": "An toàn lao động",
            "hanja": "産業安全",
            "hanjaReading": "産(낳을 산) + 業(일 업) + 安(편안할 안) + 全(온전할 전)",
            "pronunciation": "안 토안 라오 동",
            "meaningKo": "산업 현장에서 근로자의 안전과 건강을 보호하기 위한 제반 조치와 관리 체계. 통역 시 주의할 점은 한국은 중대재해처벌법(2022) 시행으로 경영책임자가 직접 처벌받을 수 있지만, 베트남은 기업 책임 중심이며 개인 형사 책임은 제한적이라는 점이다. 한국은 50인 이상 사업장은 안전관리자·보건관리자 선임이 의무이나 베트남은 10인 이상 사업장부터 안전 담당자 배치 의무가 있다. PSM(공정안전관리), KOSHA(안전보건공단) 등 한국 고유 제도는 설명이 필요하다.",
            "meaningVi": "Hệ thống biện pháp và quản lý nhằm bảo vệ an toàn và sức khỏe cho người lao động tại nơi làm việc. Luật An toàn vệ sinh lao động Việt Nam (2015) quy định trách nhiệm của người sử dụng lao động trong việc đảm bảo điều kiện làm việc an toàn, tuy nhiên chưa có chế độ truy cứu trách nhiệm hình sự cá nhân đối với người đứng đầu doanh nghiệp như Hàn Quốc (Đạo luật xử phạt tai nạn nghiêm trọng 2022).",
            "context": "건설 현장, 제조업, 화학 공장 등 위험 작업장에서 필수. 안전교육, 보호구 착용, 정기 점검 등이 포함된다.",
            "culturalNote": "한국은 중대재해(사망 1명 또는 부상 2명 이상) 발생 시 경영책임자가 1년 이상 징역형을 받을 수 있어 경영진의 안전 책임이 매우 무겁다. 베트남은 산업재해 발생 시 기업이 벌금과 행정 처분을 받으나 경영자 개인의 형사 책임은 극히 제한적이다. 한국은 산업안전보건공단(KOSHA)이 민간 기업 안전 컨설팅과 교육을 담당하나 베트남은 노동안전국(Cục An toàn lao động) 중심의 공공 관리다. 통역 시 양국의 책임 주체와 처벌 수위 차이를 명확히 해야 한다.",
            "commonMistakes": [
                {
                    "mistake": "An toàn lao động vs Vệ sinh lao động 혼용",
                    "correction": "An toàn lao động (안전) vs Vệ sinh lao động (보건)",
                    "explanation": "안전(사고 예방)과 보건(건강 관리)은 다른 개념이므로 맥락에 맞게 구분해야 한다."
                },
                {
                    "mistake": "중대재해처벌법을 일반 산업안전법으로 번역",
                    "correction": "Đạo luật xử phạt tai nạn nghiêm trọng (중대재해처벌법) 명시",
                    "explanation": "2022년 신설된 한국 고유 법률이므로 정식 명칭과 함께 설명이 필요하다."
                },
                {
                    "mistake": "안전관리자를 일반 관리자로 번역",
                    "correction": "Người quản lý an toàn (법정 안전관리자) vs Quản lý (일반 관리자)",
                    "explanation": "법정 자격(산업안전기사 등)을 가진 전문 인력이므로 구분해야 한다."
                }
            ],
            "examples": [
                {
                    "ko": "이 공장은 중대재해처벌법 적용 대상이므로 안전 관리를 철저히 해야 합니다.",
                    "vi": "Nhà máy này thuộc đối tượng áp dụng Đạo luật xử phạt tai nạn nghiêm trọng, nên phải quản lý an toàn rất chặt chẽ (trách nhiệm hình sự của người đứng đầu).",
                    "situation": "formal"
                },
                {
                    "ko": "근로자는 작업 시작 전 반드시 안전교육을 이수해야 합니다.",
                    "vi": "Người lao động phải hoàn thành khóa đào tạo an toàn lao động trước khi bắt đầu làm việc.",
                    "situation": "onsite"
                },
                {
                    "ko": "안전모와 안전화 착용은 필수이며, 미착용 시 현장 출입이 금지됩니다.",
                    "vi": "Bắt buộc đeo mũ bảo hộ và đi giày bảo hộ, nếu không sẽ bị cấm vào khu vực làm việc.",
                    "situation": "onsite"
                }
            ],
            "relatedTerms": ["중대재해처벌법", "산업안전보건법", "안전관리자", "보호구", "산업재해"]
        },
        {
            "slug": "quay-roi-noi-lam-viec",
            "korean": "직장 내 괴롭힘",
            "vietnamese": "Quấy rối nơi làm việc",
            "hanja": None,
            "hanjaReading": None,
            "pronunciation": "꾸에이 조이 느이 람 비엑",
            "meaningKo": "직장에서의 지위 또는 관계 등의 우위를 이용하여 업무상 적정 범위를 넘어 다른 근로자에게 신체적·정신적 고통을 주거나 근무환경을 악화시키는 행위(근로기준법 제76조의2). 통역 시 주의할 점은 한국은 2019년부터 명문화되어 피해자 보호 의무와 사용자 조사 의무가 강화되었지만, 베트남 노동법에는 직장 내 괴롭힘 개념이 명시되지 않았고 '성희롱(Quấy rối tình dục)' 규정만 존재한다는 점이다. 한국의 '태움 문화', '군기 잡기' 같은 관행이 법적 처벌 대상임을 설명할 때 베트남 청중에게는 맥락 설명이 필요하다.",
            "meaningVi": "Hành vi sử dụng ưu thế về địa vị hoặc mối quan hệ trong công việc để vượt quá phạm vi hợp lý của công việc, gây đau khổ về thể chất, tinh thần cho người lao động khác hoặc làm xấu đi môi trường làm việc (theo Điều 76-2 Luật Tiêu chuẩn Lao động Hàn Quốc, có hiệu lực từ 2019). Khái niệm này chưa được quy định rõ ràng trong pháp luật lao động Việt Nam, chỉ có quy định về quấy rối tình dục.",
            "context": "직장 내 인권 보호, 괴롭힘 신고 처리, 인사 관리, 노동법 준수 교육에서 사용된다.",
            "culturalNote": "한국은 2019년 근로기준법 개정으로 직장 내 괴롭힘 금지가 명문화되었고, 피해자가 신고하면 사용자는 조사 의무와 피해자 보호 의무를 진다. 가해자는 징계 대상이며, 사용자가 조사를 하지 않거나 피해자에게 불이익을 주면 처벌받는다. 베트남은 성희롱 규정은 있으나 일반적 직장 내 괴롭힘(언어 폭력, 따돌림 등)을 규율하는 법령이 없어 실무상 대응이 어렵다. 한국의 '태움'(신입을 압박하여 가르치는 문화), '군기 잡기' 같은 위계적 문화가 법적으로 금지되었음을 통역할 때는 문화적 배경을 함께 설명해야 이해도가 높아진다.",
            "commonMistakes": [
                {
                    "mistake": "Bắt nạt (왕따, 일반 괴롭힘)",
                    "correction": "Quấy rối nơi làm việc (직장 내 괴롭힘)",
                    "explanation": "'Bắt nạt'는 학교 폭력 맥락이 강하고, 직장 내 괴롭힘은 'Quấy rối nơi làm việc'으로 명확히 해야 한다."
                },
                {
                    "mistake": "성희롱과 직장 내 괴롭힘을 혼용",
                    "correction": "Quấy rối tình dục (성희롱) vs Quấy rối nơi làm việc (일반 괴롭힘)",
                    "explanation": "성희롱은 특정 유형이고, 직장 내 괴롭힘은 더 넓은 개념이므로 구분해야 한다."
                },
                {
                    "mistake": "베트남에도 동일한 법이 있는 것처럼 설명",
                    "correction": "한국 2019년 신설 법률이며 베트남은 미비",
                    "explanation": "베트남 노동법에는 명시되지 않은 개념이므로 한국 법제 설명임을 명확히 해야 한다."
                }
            ],
            "examples": [
                {
                    "ko": "상사가 지속적으로 업무와 무관한 심부름을 시키고 인격 모독 발언을 한다면 직장 내 괴롭힘에 해당합니다.",
                    "vi": "Nếu cấp trên liên tục yêu cầu làm việc riêng không liên quan đến công việc và có phát ngôn xúc phạm nhân phẩm, đó là hành vi quấy rối nơi làm việc (theo luật Hàn Quốc).",
                    "situation": "formal"
                },
                {
                    "ko": "직장 내 괴롭힘 신고를 받으면 회사는 즉시 조사하고 피해자를 보호해야 합니다.",
                    "vi": "Khi nhận được tố cáo quấy rối nơi làm việc, công ty phải điều tra ngay và bảo vệ nạn nhân (nghĩa vụ của người sử dụng lao động theo luật Hàn Quốc).",
                    "situation": "formal"
                },
                {
                    "ko": "이 행위는 태움 문화로, 한국에서는 직장 내 괴롭힘으로 처벌받을 수 있습니다.",
                    "vi": "Hành vi này thuộc văn hóa 'đốt cháy' (taeeum - áp lực quá mức lên nhân viên mới), ở Hàn Quốc có thể bị xử phạt là quấy rối nơi làm việc.",
                    "situation": "onsite"
                }
            ],
            "relatedTerms": ["성희롱", "근로기준법", "인사위원회", "징계", "피해자 보호"]
        },
        {
            "slug": "lao-dong-khong-chinh-thuc",
            "korean": "비정규직",
            "vietnamese": "Lao động không chính thức",
            "hanja": "非正規職",
            "hanjaReading": "非(아닐 비) + 正(바를 정) + 規(법 규) + 職(직분 직)",
            "pronunciation": "라오 동 콩 칭 툭",
            "meaningKo": "정규직(무기계약 전일제)이 아닌 근로 형태를 총칭하는 개념으로, 기간제, 단시간, 파견, 용역, 특수고용 등을 포함한다. 통역 시 주의할 점은 한국은 '기간제법'과 '파견법'으로 비정규직을 세분화하여 규율하지만, 베트남은 '정기계약(Hợp đồng xác định thời hạn)'과 '무기계약(Hợp đồng không xác định thời hạn)'으로만 구분하며 파견·용역 개념이 약하다는 점이다. 한국은 2년 초과 사용 시 정규직 전환 의무가 있으나 베트남은 명확한 전환 의무가 없다. 차별 시정 제도도 한국이 더 강화되어 있다.",
            "meaningVi": "Các hình thức lao động không phải là lao động chính thức (hợp đồng không xác định thời hạn, toàn thời gian), bao gồm lao động thời vụ, bán thời gian, lao động qua công ty cung ứng, v.v. Tại Hàn Quốc, có Luật Lao động thời hạn (기간제법) và Luật Lao động cử đi (파견법) quy định chi tiết, trong khi Việt Nam chủ yếu phân biệt hợp đồng xác định thời hạn và không xác định thời hạn, chưa có khái niệm cử đi - cung ứng lao động rõ ràng.",
            "context": "인사 관리, 근로계약 체결, 노동법 준수, 차별 시정 신청 시 사용된다.",
            "culturalNote": "한국은 비정규직 비율이 약 36%(2023년 기준)이며 정규직과의 임금·복지 격차가 사회 문제다. 기간제 근로자는 2년을 초과하면 무기계약으로 간주되며(기간제법), 파견 근로는 32개 업무로 제한되고 2년 초과 시 직접 고용 의무가 있다. 베트남은 정기계약이 일반적이며(공장 근로자 대부분), 계약 갱신 횟수 제한은 있으나 정규직 전환 의무는 명시되지 않았다. 한국의 '동일가치 노동 동일임금' 원칙은 베트남에서 아직 법제화되지 않아 통역 시 한국 법의 선진성을 설명할 필요가 있다.",
            "commonMistakes": [
                {
                    "mistake": "Lao động tạm thời (임시 근로)",
                    "correction": "Lao động không chính thức (비정규직 포괄 개념)",
                    "explanation": "'Tạm thời'는 계절 근로만 의미하고, 비정규직은 다양한 형태를 포함하므로 'không chính thức'이 적절하다."
                },
                {
                    "mistake": "파견과 용역을 구분하지 않고 번역",
                    "correction": "Cử đi (파견) vs Cung ứng lao động (용역)",
                    "explanation": "파견은 파견업체가 지휘권 없이 근로자만 제공, 용역은 업체가 지휘권 보유. 법적 책임이 달라 구분 필수."
                },
                {
                    "mistake": "2년 전환 의무를 베트남에도 적용되는 것처럼 설명",
                    "correction": "한국 기간제법 고유 규정임을 명시",
                    "explanation": "베트남에는 2년 초과 시 자동 전환 규정이 없으므로 한국 법제임을 명확히 해야 한다."
                }
            ],
            "examples": [
                {
                    "ko": "이 회사는 비정규직 근로자가 전체의 40%를 차지하고 있습니다.",
                    "vi": "Công ty này có 40% tổng số lao động là lao động không chính thức (hợp đồng xác định thời hạn, bán thời gian, v.v.).",
                    "situation": "formal"
                },
                {
                    "ko": "기간제 근로자를 2년 넘게 쓰면 정규직으로 전환해야 합니다.",
                    "vi": "Nếu sử dụng lao động thời hạn quá 2 năm, phải chuyển đổi thành lao động chính thức theo luật Hàn Quốc (Luật Lao động thời hạn).",
                    "situation": "formal"
                },
                {
                    "ko": "비정규직이라는 이유로 차별하면 노동위원회에 시정 신청을 할 수 있습니다.",
                    "vi": "Nếu bị phân biệt đối xử vì là lao động không chính thức, có thể yêu cầu khắc phục tại Ủy ban Quan hệ lao động (theo luật Hàn Quốc).",
                    "situation": "onsite"
                }
            ],
            "relatedTerms": ["정규직", "기간제", "파견", "용역", "동일가치노동 동일임금"]
        },
        {
            "slug": "uy-ban-quan-he-lao-dong",
            "korean": "노동위원회",
            "vietnamese": "Ủy ban quan hệ lao động",
            "hanja": "勞動委員會",
            "hanjaReading": "勞(일할 로) + 動(움직일 동) + 委(맡길 위) + 員(인원 원) + 會(모일 회)",
            "pronunciation": "우이 반 꾸안 헤 라오 동",
            "meaningKo": "노동관계에 관한 사항을 심판하고 조정하는 행정 기관으로, 부당해고·부당노동행위 구제 신청, 차별 시정 신청, 노동쟁의 조정 등을 담당한다. 통역 시 주의할 점은 한국의 노동위원회는 준사법 기관(행정심판)으로 결정이 법적 구속력을 가지며 불복 시 행정소송으로 이어지지만, 베트남의 '노동조정위원회(Hội đồng hòa giải lao động)'는 조정 중심이며 구속력이 약하다는 점이다. 한국은 중앙·지방노동위원회 2심 구조이나 베트남은 단일 조정 절차다.",
            "meaningVi": "Cơ quan hành chính giải quyết các tranh chấp và điều chỉnh quan hệ lao động, bao gồm xử lý đơn khiếu nại sa thải trái pháp luật, hành vi lao động không công bằng, yêu cầu khắc phục phân biệt đối xử, và hòa giải tranh chấp lao động. Ở Hàn Quốc, Ủy ban Quan hệ lao động có tính chất cơ quan bán tư pháp, quyết định có hiệu lực pháp luật bắt buộc, trong khi Hội đồng hòa giải lao động Việt Nam chủ yếu thực hiện hòa giải, không có quyền cưỡng chế.",
            "context": "부당해고 구제, 부당노동행위 신고, 노동쟁의 조정, 차별 시정 신청 시 언급된다.",
            "culturalNote": "한국 노동위원회는 고용노동부 산하지만 독립적 의사결정 권한을 가지며, 노사 대표와 공익 위원으로 구성된다. 지방노동위원회(1심) → 중앙노동위원회(재심) → 행정소송(법원) 순으로 불복이 가능하다. 부당해고 구제 신청은 해고일로부터 3개월 이내에 해야 하며, 인정되면 원직 복직과 임금 지급 명령이 내려진다. 베트남은 '노동조정위원회'가 기업 내부 또는 지역별로 구성되며, 조정이 실패하면 법원 소송으로 가야 한다. 한국의 노동위원회는 준사법 기능이 강하므로 '행정 법원'에 가까운 개념으로 설명하는 것이 효과적이다.",
            "commonMistakes": [
                {
                    "mistake": "Tòa án lao động (노동법원)",
                    "correction": "Ủy ban quan hệ lao động (노동위원회, 행정기관)",
                    "explanation": "노동위원회는 법원이 아닌 행정심판 기관이므로 'Tòa án'이 아닌 'Ủy ban'을 사용해야 한다."
                },
                {
                    "mistake": "베트남 조정위원회와 동일한 것처럼 번역",
                    "correction": "한국 노동위원회는 구속력 있는 결정 가능, 베트남은 조정만",
                    "explanation": "한국은 결정이 준사법적 효력을 가지지만 베트남은 조정(화해) 중심이므로 차이를 명확히 해야 한다."
                },
                {
                    "mistake": "부당해고 구제 신청 기한을 명시하지 않음",
                    "correction": "해고일로부터 3개월 이내 신청 (한국)",
                    "explanation": "법정 기한이 있으므로 통역 시 반드시 기한을 함께 안내해야 한다."
                }
            ],
            "examples": [
                {
                    "ko": "부당해고를 당했다면 3개월 이내에 노동위원회에 구제 신청을 하세요.",
                    "vi": "Nếu bị sa thải trái pháp luật, hãy nộp đơn khiếu nại đến Ủy ban Quan hệ lao động trong vòng 3 tháng kể từ ngày bị sa thải.",
                    "situation": "formal"
                },
                {
                    "ko": "노동위원회에서 부당해고로 인정되어 원직 복직 명령이 내려졌습니다.",
                    "vi": "Ủy ban Quan hệ lao động đã xác nhận sa thải trái luật và ra lệnh phục hồi công việc ban đầu.",
                    "situation": "formal"
                },
                {
                    "ko": "노동쟁의 조정이 노동위원회에서 진행 중입니다.",
                    "vi": "Tranh chấp lao động đang được hòa giải tại Ủy ban Quan hệ lao động (Hàn Quốc).",
                    "situation": "onsite"
                }
            ],
            "relatedTerms": ["부당해고", "부당노동행위", "조정", "행정소송", "구제신청"]
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
