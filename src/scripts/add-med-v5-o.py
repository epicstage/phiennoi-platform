#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
응급의학 전문용어 추가 스크립트
10개의 Tier S 품질 응급의학 용어를 medical.json에 추가
"""

import json
import os

# 파일 경로 설정
file_path = os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', 'data', 'terms', 'medical.json')

# 추가할 응급의학 용어 데이터
new_terms = [
    {
        "slug": "phong-cap-cuu",
        "korean": "응급실",
        "vietnamese": "Phòng cấp cứu",
        "hanja": "應急室",
        "hanjaReading": "應(응할 응) 急(급할 급) 室(집 실)",
        "pronunciation": "퐁 껍 꾸",
        "meaningKo": "생명이 위급한 환자나 즉각적인 치료가 필요한 환자를 24시간 진료하는 병원 내 특수 부서입니다. 통역 시 주의할 점은 한국의 응급실은 등급제(1~3등급)로 나뉘며, 베트남은 '응급과(Khoa cấp cứu)'와 '응급실(Phòng cấp cứu)'을 구분하여 사용하므로 병원 규모에 따라 정확히 번역해야 합니다. 또한 한국의 '응급의료센터'는 'Trung tâm y tế cấp cứu'로 번역하며, 단순 응급실과는 규모와 기능이 다르므로 혼동하지 않도록 주의해야 합니다.",
        "meaningVi": "Phòng cấp cứu là khu vực chuyên biệt trong bệnh viện hoạt động 24/7 để tiếp nhận và điều trị những bệnh nhân trong tình trạng nguy kịch hoặc cần can thiệp y tế khẩn cấp. Ở Việt Nam, phòng cấp cứu thường là bộ phận của khoa cấp cứu.",
        "context": "응급의료, 병원 시설, 의료 행정",
        "culturalNote": "한국은 응급의료체계가 3단계(권역응급의료센터, 지역응급의료센터, 지역응급의료기관)로 세분화되어 있으며, 응급실 과밀화가 심각한 사회 문제입니다. 베트남은 응급실 시스템이 아직 발전 단계에 있으며, 대도시 종합병원 위주로 운영됩니다. 통역 시 '응급실 뺑뺑이(응급실을 여러 곳 전전하는 현상)'같은 한국 특유의 표현은 'hiện tượng bệnh viện từ chối tiếp nhận bệnh nhân cấp cứu'로 설명적으로 번역해야 이해가 쉽습니다.",
        "commonMistakes": [
            {
                "mistake": "응급실을 항상 'Khoa cấp cứu'로 번역",
                "correction": "병원 규모에 따라 'Phòng cấp cứu' (응급실) 또는 'Trung tâm cấp cứu' (응급센터) 구분",
                "explanation": "'Khoa'는 '과(科)'를 의미하므로 부서 전체를 지칭할 때 사용하고, 'Phòng'은 '실(室)'로 물리적 공간을 의미합니다."
            },
            {
                "mistake": "응급의료센터와 응급실을 같은 용어로 번역",
                "correction": "응급실 = Phòng cấp cứu, 응급의료센터 = Trung tâm y tế cấp cứu",
                "explanation": "응급의료센터는 권역 단위의 큰 규모 시설이므로 'Trung tâm'(센터)를 사용해야 정확합니다."
            },
            {
                "mistake": "'ER'을 그대로 'ER'로 표기",
                "correction": "베트남어로 완전히 번역하거나 설명 추가",
                "explanation": "베트남에서는 'ER'이라는 영어 약자가 일반적이지 않으므로, 정식 베트남어 명칭을 사용해야 합니다."
            }
        ],
        "examples": [
            {
                "ko": "환자를 응급실로 즉시 이송하세요.",
                "vi": "Vui lòng đưa bệnh nhân đến phòng cấp cứu ngay lập tức.",
                "situation": "formal"
            },
            {
                "ko": "응급실 대기 시간이 2시간입니다.",
                "vi": "Thời gian chờ ở phòng cấp cứu là 2 giờ.",
                "situation": "onsite"
            },
            {
                "ko": "응급실에서 응급처치를 받았어요.",
                "vi": "Tôi đã được sơ cứu ở phòng cấp cứu.",
                "situation": "informal"
            }
        ],
        "relatedTerms": ["중환자실", "외래진료", "119구급대", "응급의료", "트리아지"]
    },
    {
        "slug": "hoi-suc-tim-phoi",
        "korean": "심폐소생술",
        "vietnamese": "Hồi sức tim phổi",
        "hanja": "心肺蘇生術",
        "hanjaReading": "心(마음 심) 肺(허파 폐) 蘇(소생할 소) 生(날 생) 術(재주 술)",
        "pronunciation": "허이 썩 팀 퍼이",
        "meaningKo": "심장과 호흡이 멈춘 환자에게 인공호흡과 가슴압박을 통해 혈액순환과 산소공급을 유지하는 응급처치법입니다. 영어 약자 CPR(Cardiopulmonary Resuscitation)로도 불립니다. 통역 시 주의할 점은 한국에서는 '가슴압박 소생술'이라는 용어도 함께 사용되며, 이는 인공호흡 없이 가슴압박만 하는 'Hồi sức chỉ bằng ép tim'을 의미합니다. 베트남에서는 전통적으로 'Hồi sức tim phổi'를 사용하지만, 최근에는 'CPR'이라는 약어도 의료진 사이에서 통용되므로 청중에 따라 선택적으로 사용해야 합니다.",
        "meaningVi": "Hồi sức tim phổi (CPR) là kỹ thuật cấp cứu kết hợp ép tim và thông khí nhân tạo nhằm duy trì tuần hoàn máu và cung cấp oxy cho bệnh nhân ngừng tim hoặc ngừng thở. Đây là kỹ năng sơ cứu thiết yếu có thể cứu sống người bệnh.",
        "context": "응급의료, 구조 및 구급, 의료 교육",
        "culturalNote": "한국에서는 심폐소생술 교육이 학교, 직장, 군대 등에서 의무적으로 실시되며, 일반인의 CPR 인지도가 매우 높습니다. 자동심장충격기(AED) 사용법도 함께 교육됩니다. 반면 베트남에서는 CPR 교육이 주로 의료 종사자에게만 집중되어 있고, 일반인 교육은 아직 초기 단계입니다. 통역 시 'Hands-only CPR(가슴압박 소생술)'과 'Full CPR(전통적 CPR)'의 차이를 명확히 설명해야 하며, 베트남 청중에게는 추가 설명이 필요할 수 있습니다.",
        "commonMistakes": [
            {
                "mistake": "CPR을 'Massage tim' (심장 마사지)로 번역",
                "correction": "정확한 의학 용어인 'Hồi sức tim phổi' 사용",
                "explanation": "'Massage tim'은 구어적 표현이며 의학적으로 부정확합니다. 전문 의료 통역에서는 정식 용어를 사용해야 합니다."
            },
            {
                "mistake": "가슴압박 소생술과 심폐소생술을 구분하지 않음",
                "correction": "가슴압박 소생술 = Hồi sức chỉ bằng ép tim, 심폐소생술 = Hồi sức tim phổi (ép tim + thông khí)",
                "explanation": "두 용어는 인공호흡 포함 여부가 다르므로 정확히 구분해야 합니다."
            },
            {
                "mistake": "'CPR'을 베트남어로 번역하지 않고 그대로 사용",
                "correction": "일반인 대상 시 'Hồi sức tim phổi (CPR)'로 병기",
                "explanation": "베트남 일반인은 'CPR'이라는 약어에 익숙하지 않을 수 있으므로 풀어서 설명해야 합니다."
            }
        ],
        "examples": [
            {
                "ko": "즉시 심폐소생술을 시작하겠습니다.",
                "vi": "Chúng tôi sẽ bắt đầu hồi sức tim phổi ngay lập tức.",
                "situation": "formal"
            },
            {
                "ko": "가슴 중앙을 강하게 30회 압박하세요.",
                "vi": "Hãy ép mạnh vào giữa ngực 30 lần.",
                "situation": "onsite"
            },
            {
                "ko": "심폐소생술 교육 받은 적 있어요?",
                "vi": "Bạn đã từng được đào tạo về hồi sức tim phổi chưa?",
                "situation": "informal"
            }
        ],
        "relatedTerms": ["자동제세동기", "기도확보", "응급처치", "가슴압박", "인공호흡"]
    },
    {
        "slug": "may-khu-rung-tim-tu-dong",
        "korean": "자동제세동기",
        "vietnamese": "Máy khử rung tim tự động",
        "hanja": "自動除細動機",
        "hanjaReading": "自(스스로 자) 動(움직일 동) 除(덜 제) 細(가늘 세) 動(움직일 동) 機(틀 기)",
        "pronunciation": "마이 쿠 중 팀 뜨 동",
        "meaningKo": "심장이 불규칙하게 떨리는 심실세동 상태를 감지하여 자동으로 전기충격을 가해 정상 리듬으로 되돌리는 의료기기입니다. 영어 약자 AED(Automated External Defibrillator)로 널리 알려져 있습니다. 통역 시 주의할 점은 한국에서는 공공장소에 AED 설치가 법적으로 의무화되어 있으며, '자동심장충격기'라는 용어도 함께 사용됩니다. 베트남에서는 'Máy sốc điện tim tự động' 또는 'AED'로 불리는데, 아직 공공장소 보급률이 낮아 일반인 인지도가 한국보다 낮습니다. 의료기관 외 장소에서의 사용법을 설명할 때는 더욱 상세한 통역이 필요합니다.",
        "meaningVi": "Máy khử rung tim tự động (AED) là thiết bị y tế có thể phát hiện rung thất và tự động phát ra xung điện để khôi phục nhịp tim bình thường. Thiết bị này được thiết kế để cả người không chuyên y tế cũng có thể sử dụng trong trường hợp khẩn cấp.",
        "context": "응급의료, 심장질환, 의료기기, 공공안전",
        "culturalNote": "한국은 2008년부터 다중이용시설에 AED 설치를 의무화했으며, 지하철역, 공항, 대형 쇼핑몰 등에서 쉽게 찾을 수 있습니다. 사용법은 음성 안내로 제공되어 일반인도 사용 가능합니다. 베트남에서는 AED가 주로 대형 병원에만 비치되어 있고, 공공장소 설치는 하노이, 호치민 등 대도시 일부 지역에 국한됩니다. 통역 시 'AED 위치 안내판'을 'Biển chỉ dẫn vị trí máy AED'로 번역하고, 한국의 보급 현황을 설명할 때는 베트남과의 차이를 감안하여 추가 설명이 필요합니다.",
        "commonMistakes": [
            {
                "mistake": "제세동기를 'Máy sốc điện' (전기충격기)로만 번역",
                "correction": "'Máy khử rung tim tự động' 또는 'Máy sốc điện tim tự động'으로 정확히 표현",
                "explanation": "단순 'Máy sốc điện'은 다른 전기충격 의료기기와 혼동될 수 있으므로 '심장(tim)' 명시가 필요합니다."
            },
            {
                "mistake": "자동제세동기와 수동제세동기를 구분하지 않음",
                "correction": "자동 = tự động, 수동 = thủ công을 명확히 구분",
                "explanation": "AED는 자동으로 심전도를 분석하지만, 수동 제세동기는 의료진이 직접 판단해야 하므로 구분이 중요합니다."
            },
            {
                "mistake": "'AED'를 베트nam어로 번역하지 않고 약자만 사용",
                "correction": "일반인 대상 시 'Máy khử rung tim tự động (AED)'로 병기",
                "explanation": "베트남 일반인은 'AED'라는 약어에 익숙하지 않을 수 있습니다."
            }
        ],
        "examples": [
            {
                "ko": "자동제세동기를 즉시 가져와 주세요.",
                "vi": "Vui lòng mang máy khử rung tim tự động đến ngay.",
                "situation": "formal"
            },
            {
                "ko": "AED 패드를 가슴에 부착하세요.",
                "vi": "Dán miếng dán AED lên ngực bệnh nhân.",
                "situation": "onsite"
            },
            {
                "ko": "지하철역에 제세동기가 있어요.",
                "vi": "Ở ga tàu điện ngầm có máy AED.",
                "situation": "informal"
            }
        ],
        "relatedTerms": ["심폐소생술", "심실세동", "응급처치", "전기충격", "심장마비"]
    },
    {
        "slug": "dam-bao-duong-tho",
        "korean": "기도확보",
        "vietnamese": "Đảm bảo đường thở",
        "hanja": "氣道確保",
        "hanjaReading": "氣(기운 기) 道(길 도) 確(확실할 확) 保(지킬 보)",
        "pronunciation": "담 바오 즈엉 터",
        "meaningKo": "의식이 없거나 호흡곤란 상태의 환자에게 공기가 폐로 들어갈 수 있도록 기도(공기가 지나가는 통로)를 열어주는 응급처치입니다. 머리 뒤로젖히기-턱 들어올리기(Head tilt-Chin lift) 또는 하악거상법(Jaw thrust)을 사용합니다. 통역 시 주의할 점은 '기도'를 '氣道(airway)'와 '祈禱(prayer)'로 혼동하지 않는 것이며, 베트남어로는 'đường thở' 또는 'đường dẫn khí'로 번역됩니다. 또한 '기도확보'는 단순히 입을 벌리는 것이 아니라 해부학적으로 기도를 개방하는 의학적 처치이므로, 'mở đường thở' 또는 'đảm bảo đường thở thông thoáng'으로 정확히 표현해야 합니다.",
        "meaningVi": "Đảm bảo đường thở là thủ thuật cấp cứu nhằm mở đường dẫn khí từ miệng/mũi đến phổi cho bệnh nhân bất tỉnh hoặc khó thở. Các kỹ thuật phổ biến bao gồm ngửa đầu-nâng cằm (head tilt-chin lift) hoặc đẩy hàm dưới (jaw thrust).",
        "context": "응급의료, 마취과, 중환자 치료",
        "culturalNote": "한국 응급의료 교육에서는 기도확보가 심폐소생술의 첫 번째 단계(CAB 중 A - Airway)로 강조되며, 일반인 교육에서도 기본적인 머리 뒤로젖히기-턱 들어올리기 방법을 가르칩니다. 베트남에서는 기도확보 개념이 주로 의료진 교육에 포함되며, 일반인 대상 응급처치 교육에서는 덜 강조됩니다. 통역 시 '기도삽관(intubation, đặt nội khí quản)'과 '기도확보'를 혼동하지 않도록 주의해야 하며, 전자는 의료진이 튜브를 삽입하는 고급 처치, 후자는 일반인도 할 수 있는 기본 처치임을 구분해야 합니다.",
        "commonMistakes": [
            {
                "mistake": "기도확보를 'Mở miệng' (입 벌리기)로 번역",
                "correction": "'Đảm bảo đường thở' 또는 'Mở đường thở'로 정확히 표현",
                "explanation": "단순히 입을 벌리는 것이 아니라 해부학적으로 기도를 개방하는 의학적 처치입니다."
            },
            {
                "mistake": "기도삽관과 기도확보를 같은 용어로 번역",
                "correction": "기도확보 = Đảm bảo đường thở (수기), 기도삽관 = Đặt nội khí quản (기구 사용)",
                "explanation": "기도확보는 손으로 하는 기본 처치, 기도삽관은 튜브를 삽입하는 고급 처치로 전혀 다릅니다."
            },
            {
                "mistake": "'Airway'를 '공기길'로 직역",
                "correction": "'Đường thở' (호흡 통로) 사용",
                "explanation": "의학 용어는 확립된 베트남어 표현을 사용해야 하며, 직역은 비전문적으로 들립니다."
            }
        ],
        "examples": [
            {
                "ko": "먼저 환자의 기도를 확보하세요.",
                "vi": "Trước tiên hãy đảm bảo đường thở cho bệnh nhân.",
                "situation": "formal"
            },
            {
                "ko": "머리를 뒤로 젖히고 턱을 들어 올리세요.",
                "vi": "Ngửa đầu ra sau và nâng cằm lên.",
                "situation": "onsite"
            },
            {
                "ko": "기도가 막혀서 숨을 못 쉬고 있어요.",
                "vi": "Đường thở bị tắc nên không thở được.",
                "situation": "informal"
            }
        ],
        "relatedTerms": ["심폐소생술", "기도삽관", "하임리히법", "후두마스크", "응급기도관리"]
    },
    {
        "slug": "so-cuu-gay-xuong",
        "korean": "골절응급처치",
        "vietnamese": "Sơ cứu gãy xương",
        "hanja": "骨折應急處置",
        "hanjaReading": "骨(뼈 골) 折(꺾을 절) 應(응할 응) 急(급할 급) 處(곳 처) 置(둘 치)",
        "pronunciation": "서 꾸 가이 쑤엉",
        "meaningKo": "뼈가 부러진 환자에게 현장에서 실시하는 초기 응급처치로, 부목 고정, 환부 안정화, 통증 관리, 2차 손상 방지를 목적으로 합니다. 통역 시 주의할 점은 '골절'과 '탈구(dislocation, trật khớp)'를 명확히 구분해야 하며, 한국에서는 개방성 골절(피부가 찢어진 골절)과 폐쇄성 골절을 구분하여 처치 방법이 다르므로 'gãy xương hở' (개방성)와 'gãy xương kín' (폐쇄성)으로 정확히 번역해야 합니다. 또한 '부목'은 'nẹp cứng'으로 번역하며, 즉석 부목(신문지, 우산 등)은 'nẹp tạm thời'로 표현합니다.",
        "meaningVi": "Sơ cứu gãy xương là các biện pháp xử lý ban đầu tại hiện trường cho bệnh nhân bị gãy xương, bao gồm cố định bằng nẹp, giữ yên vùng bị thương, giảm đau và phòng ngừa tổn thương thứ phát. Cần phân biệt gãy xương kín và gãy xương hở để xử lý phù hợp.",
        "context": "응급의료, 정형외과, 재난 구조",
        "culturalNote": "한국에서는 응급처치 교육에서 골절 응급처치가 필수 항목으로 포함되며, 특히 등산, 스키 등 야외 활동이 많아 현장 응급처치 능력이 강조됩니다. 베트남에서도 교통사고가 많아 골절 응급처치가 중요하지만, 일반인 교육보다는 의료진 위주의 교육이 이루어집니다. 통역 시 '부목 대용(신문지, 잡지, 우산 등)'을 설명할 때 'vật liệu thay thế nẹp (báo, tạp chí, dù)'로 구체적으로 표현하면 이해가 쉽습니다. 또한 한국의 '119 응급처치 앱'과 같은 디지털 도구는 베트남에 익숙하지 않으므로 설명이 필요합니다.",
        "commonMistakes": [
            {
                "mistake": "골절을 'Xương bị thương' (뼈 부상)로 모호하게 번역",
                "correction": "'Gãy xương' (골절)로 정확히 표현",
                "explanation": "'Xương bị thương'은 타박상, 염좌 등도 포함하는 광범위한 표현이므로 골절을 특정하지 못합니다."
            },
            {
                "mistake": "탈구와 골절을 구분하지 않고 번역",
                "correction": "골절 = Gãy xương, 탈구 = Trật khớp을 명확히 구분",
                "explanation": "탈구는 관절이 빠진 것이고, 골절은 뼈가 부러진 것으로 처치 방법이 전혀 다릅니다."
            },
            {
                "mistake": "부목을 'Thanh gỗ' (나무 막대)로만 번역",
                "correction": "'Nẹp cứng' (부목) 사용, 재질은 'nẹp gỗ/nhựa/kim loại'로 구체화",
                "explanation": "부목은 다양한 재질이 가능하며, 의료용 부목은 단순 나무 막대가 아닙니다."
            }
        ],
        "examples": [
            {
                "ko": "다리 골절이 의심되니 움직이지 마세요.",
                "vi": "Nghi ngờ gãy xương chân, vui lòng không di chuyển.",
                "situation": "formal"
            },
            {
                "ko": "부목으로 팔을 고정하고 병원으로 이송하세요.",
                "vi": "Cố định cánh tay bằng nẹp và vận chuyển đến bệnh viện.",
                "situation": "onsite"
            },
            {
                "ko": "골절된 부위를 움직이면 안 돼요.",
                "vi": "Không được cử động vùng gãy xương.",
                "situation": "informal"
            }
        ],
        "relatedTerms": ["부목고정", "탈구", "염좌", "개방성골절", "정형외과"]
    },
    {
        "slug": "so-cuu-bong",
        "korean": "화상응급처치",
        "vietnamese": "Sơ cứu bỏng",
        "hanja": "火傷應急處置",
        "hanjaReading": "火(불 화) 傷(다칠 상) 應(응할 응) 急(급할 급) 處(곳 처) 置(둘 치)",
        "pronunciation": "서 꾸 봉",
        "meaningKo": "열, 화학물질, 전기, 방사선 등에 의해 피부 조직이 손상된 환자에게 현장에서 실시하는 초기 응급처치입니다. 기본 원칙은 '흐르는 차가운 물로 최소 10분 이상 식히기'이며, 통역 시 주의할 점은 화상 정도를 1도(표피), 2도(진피), 3도(전층)로 구분하여 'bỏng độ 1, 2, 3'로 번역해야 한다는 것입니다. 특히 한국에서 흔히 쓰는 민간요법(된장, 감자, 소주 등)은 의학적으로 위험하므로, 베트남에서도 유사한 민간요법을 사용하지 않도록 '절대 금기 사항'을 강조하여 통역해야 합니다. '물집'은 'vết phồng rộp'로 번역합니다.",
        "meaningVi": "Sơ cứu bỏng là xử lý ban đầu cho vết thương do nhiệt, hóa chất, điện hoặc bức xạ gây ra. Nguyên tắc vàng là làm mát vết bỏng bằng nước lạnh chảy trong ít nhất 10 phút. Phân loại: bỏng độ 1 (nông), độ 2 (trung bình), độ 3 (sâu). Tuyệt đối không sử dụng các phương pháp dân gian như bôi kem đánh răng, nước tương, hay dầu ăn.",
        "context": "응급의료, 화재 안전, 산업 안전",
        "culturalNote": "한국에서는 화상 응급처치에 대한 잘못된 민간요법(된장, 감자즙, 소주 등)이 여전히 널리 퍼져 있어, 응급의료 교육에서 이러한 방법의 위험성을 강조합니다. 베트남에서도 'bôi kem đánh răng' (치약 바르기), 'bôi nước tương' (간장 바르기) 같은 민간요법이 있어 주의가 필요합니다. 통역 시 두 문화권 모두에서 이러한 방법이 감염과 2차 손상을 유발할 수 있음을 명확히 전달해야 합니다. 또한 한국의 '화상 전문 센터(Trung tâm chuyên khoa bỏng)'는 베트남에서 드물기 때문에, 중증 화상 환자의 이송 체계를 설명할 때 추가 설명이 필요합니다.",
        "commonMistakes": [
            {
                "mistake": "화상 정도를 단순히 'nhẹ/nặng' (가벼움/심함)으로만 표현",
                "correction": "'Bỏng độ 1/2/3' 또는 'bỏng nông/trung bình/sâu'로 정확히 분류",
                "explanation": "의학적 분류를 사용해야 치료 방침을 정확히 전달할 수 있습니다."
            },
            {
                "mistake": "물집을 터뜨려야 한다고 잘못 통역",
                "correction": "'Không được làm vỡ vết phồng rộp' (물집을 터뜨리지 말 것)",
                "explanation": "물집은 자연 보호막 역할을 하므로 인위적으로 터뜨리면 감염 위험이 높아집니다."
            },
            {
                "mistake": "얼음을 직접 대라고 통역",
                "correction": "'Dùng nước lạnh chảy' (흐르는 차가운 물), 얼음 직접 접촉은 금지",
                "explanation": "얼음 직접 접촉은 동상을 유발할 수 있으므로 위험합니다."
            }
        ],
        "examples": [
            {
                "ko": "화상 부위를 흐르는 차가운 물에 10분 이상 담그세요.",
                "vi": "Ngâm vùng bị bỏng trong nước lạnh chảy ít nhất 10 phút.",
                "situation": "formal"
            },
            {
                "ko": "2도 화상이니 병원 치료가 필요합니다.",
                "vi": "Đây là bỏng độ 2, cần điều trị tại bệnh viện.",
                "situation": "onsite"
            },
            {
                "ko": "물집이 생겼는데 터뜨려도 돼요?",
                "vi": "Có vết phồng rộp, có được làm vỡ không?",
                "situation": "informal"
            }
        ],
        "relatedTerms": ["화상센터", "피부이식", "1도화상", "2도화상", "3도화상"]
    },
    {
        "slug": "cam-mau",
        "korean": "출혈지혈",
        "vietnamese": "Cầm máu",
        "hanja": "出血止血",
        "hanjaReading": "出(날 출) 血(피 혈) 止(그칠 지) 血(피 혈)",
        "pronunciation": "껌 마우",
        "meaningKo": "상처 부위에서 피가 흐르는 것을 멈추게 하는 응급처치입니다. 직접압박법(거즈나 천으로 상처 부위를 강하게 누름), 간접압박법(동맥 압박점 누름), 지혈대 사용 등의 방법이 있습니다. 통역 시 주의할 점은 '출혈'과 '지혈'을 명확히 구분하는 것입니다. '출혈(xuất huyết)'은 피가 나오는 상태, '지혈(cầm máu)'은 피를 멈추는 행위입니다. 또한 동맥출혈(máu động mạch, 선홍색, 박동성)과 정맥출혈(máu tĩnh mạch, 암적색, 지속적 흐름)을 구분하여 통역해야 하며, 지혈대(dây cầm máu/tourniquet) 사용은 최후의 수단임을 강조해야 합니다.",
        "meaningVi": "Cầm máu là xử lý khẩn cấp nhằm làm ngừng chảy máu từ vết thương. Các phương pháp bao gồm: ép trực tiếp (dùng gạc hoặc vải ép mạnh vào vết thương), ép gián tiếp (ép điểm động mạch), và sử dụng dây cầm máu (chỉ dùng khi các biện pháp khác thất bại). Cần phân biệt máu động mạch (màu đỏ tươi, phun theo nhịp) và máu tĩnh mạch (màu đỏ sẫm, chảy đều).",
        "context": "응급의료, 외상 치료, 전투 의학",
        "culturalNote": "한국에서는 일반인 응급처치 교육에서 직접압박법이 기본으로 교육되며, 지혈대 사용은 군대나 전문 구조대원 교육에서 주로 다루어집니다. 베트남 전쟁의 역사적 배경으로 인해 베트남에서는 지혈대(dây cầm máu) 개념이 비교적 잘 알려져 있지만, 현대적 응급처치 프로토콜은 한국과 유사하게 직접압박을 우선시합니다. 통역 시 '코피(chảy máu cam)'와 같은 일상적 출혈과 외상성 출혈을 구분하고, 내출혈(xuất huyết nội, internal bleeding)은 외부에서 보이지 않아 더 위험할 수 있음을 설명해야 합니다.",
        "commonMistakes": [
            {
                "mistake": "지혈대를 'Dây buộc' (끈)으로 단순하게 번역",
                "correction": "'Dây cầm máu' 또는 'tourniquet' 사용",
                "explanation": "'Dây buộc'은 일반 끈을 의미하며, 의료용 지혈대의 특수성을 나타내지 못합니다."
            },
            {
                "mistake": "동맥출혈과 정맥출혈을 구분하지 않고 통역",
                "correction": "동맥출혈 = máu động mạch (선홍색, 박동), 정맥출혈 = máu tĩnh mạch (암적색, 지속)",
                "explanation": "출혈 유형에 따라 응급처치 긴급도와 방법이 다르므로 정확한 구분이 필수입니다."
            },
            {
                "mistake": "상처를 계속 확인하기 위해 압박을 풀라고 통역",
                "correction": "'Giữ nguyên áp lực' (압박을 유지), 거즈를 제거하지 말 것",
                "explanation": "압박을 풀면 응고가 방해되어 출혈이 다시 시작될 수 있습니다."
            }
        ],
        "examples": [
            {
                "ko": "깨끗한 거즈로 상처를 5분 이상 강하게 눌러 지혈하세요.",
                "vi": "Dùng gạc sạch ép mạnh vào vết thương trong ít nhất 5 phút để cầm máu.",
                "situation": "formal"
            },
            {
                "ko": "동맥 출혈이라 빨리 지혈해야 합니다.",
                "vi": "Đây là xuất huyết động mạch, cần cầm máu khẩn cấp.",
                "situation": "onsite"
            },
            {
                "ko": "계속 피가 나는데 어떻게 해요?",
                "vi": "Máu vẫn chảy, phải làm sao?",
                "situation": "informal"
            }
        ],
        "relatedTerms": ["직접압박법", "지혈대", "동맥출혈", "정맥출혈", "외상"]
    },
    {
        "slug": "danh-gia-muc-do-y-thuc",
        "korean": "의식수준평가",
        "vietnamese": "Đánh giá mức độ ý thức",
        "hanja": "意識水準評價",
        "hanjaReading": "意(뜻 의) 識(알 식) 水(물 수) 準(준할 준) 評(평할 평) 價(값 가)",
        "pronunciation": "다잉 자 믹 도 이 턱",
        "meaningKo": "응급 상황에서 환자의 의식 상태를 신속하게 판단하는 평가 방법입니다. 대표적으로 AVPU 척도(Alert 각성, Verbal 언어 반응, Pain 통증 반응, Unresponsive 무반응) 또는 글래스고 혼수 척도(GCS, Glasgow Coma Scale, 3~15점)를 사용합니다. 통역 시 주의할 점은 '의식'을 'ý thức' (consciousness)로 정확히 번역하고, '혼수(hôn mê, coma)'와 구분해야 한다는 것입니다. 또한 GCS는 'thang điểm Glasgow' 또는 'GCS'로 번역하며, 눈 뜨기(mở mắt), 언어 반응(phản ứng ngôn ngữ), 운동 반응(phản ứng vận động)의 3가지 영역으로 평가함을 설명해야 합니다.",
        "meaningVi": "Đánh giá mức độ ý thức là phương pháp xác định nhanh tình trạng tỉnh táo của bệnh nhân trong cấp cứu. Thang đo AVPU (Tỉnh táo - Alert, Phản ứng lời nói - Verbal, Phản ứng đau - Pain, Không phản ứng - Unresponsive) và Thang điểm hôn mê Glasgow (GCS, 3-15 điểm) là hai công cụ phổ biến nhất. GCS đánh giá 3 yếu tố: mở mắt, phản ứng ngôn ngữ và phản ứng vận động.",
        "context": "응급의료, 신경과, 중환자실",
        "culturalNote": "한국 응급의료 시스템에서는 119 구급대원과 응급실 간호사가 기본적으로 AVPU를 사용하며, 의사는 더 정밀한 GCS를 활용합니다. GCS 8점 이하는 중증 의식 저하로 기도삽관이 필요한 기준이 됩니다. 베트남에서도 GCS가 표준 평가 도구이지만, 일부 지역 병원에서는 간단한 '깨어있음/졸림/혼수' 3단계로만 평가하기도 합니다. 통역 시 '의식이 명료하다(tỉnh táo)', '기면(lờ đờ, drowsy)', '혼미(hôn mê nông)', '혼수(hôn mê sâu)' 등의 의식 수준 용어를 정확히 구분해야 합니다.",
        "commonMistakes": [
            {
                "mistake": "AVPU를 베트남어로 번역하지 않고 영어 약자만 사용",
                "correction": "A-Tỉnh táo, V-Phản ứng lời nói, P-Phản ứng đau, U-Không phản ứng로 풀어서 설명",
                "explanation": "약자만 사용하면 비의료인이 이해하기 어렵습니다."
            },
            {
                "mistake": "의식 저하를 단순히 'Ngất' (실신)로 번역",
                "correction": "의식 저하 = giảm ý thức, 실신 = ngất xỉu (일시적 의식 소실)",
                "explanation": "실신은 짧은 순간의 의식 소실이고, 의식 저하는 지속적인 상태로 구분해야 합니다."
            },
            {
                "mistake": "GCS 점수를 정확히 전달하지 않음",
                "correction": "GCS는 3~15점 범위이며, 8점 이하는 중증임을 명시",
                "explanation": "GCS 점수는 환자 중증도를 판단하는 핵심 지표이므로 정확한 숫자 전달이 필수입니다."
            }
        ],
        "examples": [
            {
                "ko": "환자의 의식수준은 GCS 12점입니다.",
                "vi": "Mức độ ý thức của bệnh nhân là GCS 12 điểm.",
                "situation": "formal"
            },
            {
                "ko": "통증 자극에만 반응하고 있습니다.",
                "vi": "Chỉ có phản ứng với kích thích đau.",
                "situation": "onsite"
            },
            {
                "ko": "환자가 의식이 명료한가요?",
                "vi": "Bệnh nhân có tỉnh táo không?",
                "situation": "informal"
            }
        ],
        "relatedTerms": ["글래스고혼수척도", "AVPU척도", "혼수", "의식장애", "뇌손상"]
    },
    {
        "slug": "van-chuyen-cap-cuu",
        "korean": "응급이송",
        "vietnamese": "Vận chuyển cấp cứu",
        "hanja": "應急移送",
        "hanjaReading": "應(응할 응) 急(급할 급) 移(옮길 이) 送(보낼 송)",
        "pronunciation": "번 추옌 껍 꾸",
        "meaningKo": "응급 환자를 의료기관으로 안전하고 신속하게 이동시키는 과정입니다. 구급차(xe cấp cứu), 닥터헬기(trực thăng y tế), 해상구조선 등 다양한 수단을 사용하며, 이송 중에도 지속적인 응급처치와 모니터링이 이루어집니다. 통역 시 주의할 점은 '이송'과 '후송'의 차이입니다. '이송(vận chuyển)'은 일반적인 환자 이동, '후송(hậu송)'은 전방에서 후방으로 또는 하급 의료기관에서 상급 기관으로 옮기는 의미가 강합니다. 또한 한국의 119 구급대는 'Đội cấp cứu 119'로 번역하며, 민간 구급차는 'xe cấp cứu tư nhân'으로 구분합니다.",
        "meaningVi": "Vận chuyển cấp cứu là quá trình di chuyển bệnh nhân nguy kịch đến cơ sở y tế một cách an toàn và nhanh chóng. Các phương tiện bao gồm xe cấp cứu, trực thăng y tế, tàu cứu hộ. Trong quá trình vận chuyển, bệnh nhân được theo dõi sát và xử lý cấp cứu liên tục. Cần phân biệt vận chuyển (di chuyển chung) và chuyển tuyến (từ bệnh viện tuyến dưới lên tuyến trên).",
        "context": "응급의료, 구급 시스템, 재난 대응",
        "culturalNote": "한국의 응급이송 체계는 119 소방 구급대가 주축이며, 무료로 제공됩니다. 닥터헬기(doctor helicopter) 시스템도 전국 권역별로 운영되어 외딴 지역이나 교통체증 시 활용됩니다. 베트남에서는 115가 응급전화번호이며, 구급차 서비스는 일부 유료인 경우가 많습니다. 민간 구급차도 많이 이용되며, 교통 혼잡으로 인해 이송 시간이 길어지는 경우가 빈번합니다. 통역 시 '이송 거부(từ chối tiếp nhận)'는 병원이 만원이거나 해당 진료과가 없어 환자를 받지 못하는 상황을 의미하며, 한국에서 사회 문제가 되고 있음을 설명할 수 있습니다.",
        "commonMistakes": [
            {
                "mistake": "119를 'Số điện thoại 119'로만 번역",
                "correction": "'Đội cấp cứu 119' 또는 'Cứu hỏa cấp cứu 119'로 기관 포함하여 번역",
                "explanation": "119는 단순 전화번호가 아니라 소방 구급 시스템을 의미합니다."
            },
            {
                "mistake": "닥터헬기를 'trực thăng' (헬리콥터)로만 번역",
                "correction": "'Trực thăng y tế' 또는 'trực thăng cấp cứu có bác sĩ'로 의료 기능 명시",
                "explanation": "일반 헬기가 아닌 의료 장비와 의료진이 탑승한 특수 헬기입니다."
            },
            {
                "mistake": "이송과 후송을 같은 용어로 번역",
                "correction": "이송 = vận chuyển (일반), 후송 = hậu송 hoặc chuyển tuyến (상급 기관으로)",
                "explanation": "후송은 방향성과 의료기관 등급이 포함된 개념입니다."
            }
        ],
        "examples": [
            {
                "ko": "환자를 닥터헬기로 권역응급의료센터에 이송하겠습니다.",
                "vi": "Chúng tôi sẽ vận chuyển bệnh nhân bằng trực thăng y tế đến trung tâm cấp cứu khu vực.",
                "situation": "formal"
            },
            {
                "ko": "이송 중 심폐소생술을 계속 시행하세요.",
                "vi": "Tiếp tục hồi sức tim phổi trong quá trình vận chuyển.",
                "situation": "onsite"
            },
            {
                "ko": "119 불러서 병원으로 이송했어요.",
                "vi": "Gọi xe cấp cứu 119 và đưa đến bệnh viện rồi.",
                "situation": "informal"
            }
        ],
        "relatedTerms": ["구급차", "닥터헬기", "119구급대", "전원", "응급의료센터"]
    },
    {
        "slug": "phan-loai-muc-do-nang",
        "korean": "중증도분류",
        "vietnamese": "Phân loại mức độ nặng",
        "hanja": "重症度分類",
        "hanjaReading": "重(무거울 중) 症(증세 증) 度(법도 도) 分(나눌 분) 類(무리 류)",
        "pronunciation": "판 로아이 믹 도 낭",
        "meaningKo": "응급실에 동시에 여러 환자가 도착했을 때, 각 환자의 중증도를 신속히 평가하여 치료 우선순위를 정하는 시스템입니다. 영어로 'Triage(트리아지)'라고 하며, 보통 1~5등급(또는 색상: 빨강-최우선, 노랑-긴급, 초록-비긴급, 검정-사망/소생불가)으로 분류합니다. 통역 시 주의할 점은 '트리아지'를 베트남어로 'Phân loại bệnh nhân cấp cứu' 또는 'Triage'로 표현하며, 한국의 KTAS(Korean Triage and Acuity Scale, 한국형 응급환자 분류도구) 시스템을 설명할 때는 'Hệ thống phân loại cấp cứu Hàn Quốc KTAS'로 번역합니다. 1단계가 가장 심각하고 5단계가 가장 경미함을 명확히 해야 합니다.",
        "meaningVi": "Phân loại mức độ nặng (Triage) là hệ thống đánh giá nhanh mức độ nghiêm trọng của từng bệnh nhân khi nhiều người đến cấp cứu cùng lúc, nhằm xác định thứ tự ưu tiên điều trị. Thường chia thành 5 cấp độ (hoặc màu sắc: đỏ-ưu tiên cao nhất, vàng-khẩn cấp, xanh-không khẩn cấp, đen-tử vong/không hồi sinh). Hàn Quốc sử dụng hệ thống KTAS với cấp độ 1 (nguy kịch nhất) đến cấp độ 5 (nhẹ nhất).",
        "context": "응급의료, 재난 의료, 전시 의학",
        "culturalNote": "한국은 2016년부터 KTAS를 전국 응급실에 의무적으로 도입하여 표준화된 중증도 분류를 시행하고 있으며, 응급실 간호사가 트리아지 전담 간호사로 배치됩니다. 색상 태그(빨강, 노랑, 초록, 검정) 시스템은 주로 재난 현장에서 사용됩니다. 베트남에서도 대형 병원에서 트리아지 개념을 도입하고 있지만, 표준화된 시스템은 아직 전국적으로 확립되지 않았습니다. 통역 시 '경증 환자가 중증 환자보다 먼저 치료받는 것이 아니다'라는 트리아지의 기본 원칙을 강조하고, '응급실 대기 시간'이 중증도에 따라 달라짐을 설명해야 합니다.",
        "commonMistakes": [
            {
                "mistake": "Triage를 '환자 분류'로만 단순 번역",
                "correction": "'Phân loại mức độ nặng' 또는 'Phân loại ưu tiên cấp cứu'로 목적을 포함하여 번역",
                "explanation": "단순 분류가 아니라 응급도와 우선순위를 정하는 의학적 과정입니다."
            },
            {
                "mistake": "숫자가 클수록 심각하다고 잘못 설명",
                "correction": "1단계가 가장 위중, 5단계가 가장 경미함을 명확히",
                "explanation": "KTAS는 숫자가 작을수록 심각한 시스템이므로 혼동하지 않도록 주의해야 합니다."
            },
            {
                "mistake": "색상 태그 시스템을 모든 응급실에서 사용한다고 설명",
                "correction": "색상 태그는 주로 재난 현장용, 병원은 KTAS 1~5단계 사용",
                "explanation": "병원과 재난 현장의 트리아지 시스템은 다를 수 있습니다."
            }
        ],
        "examples": [
            {
                "ko": "트리아지 결과 1단계로 분류되어 즉시 치료를 시작합니다.",
                "vi": "Kết quả phân loại là cấp độ 1, bắt đầu điều trị ngay lập tức.",
                "situation": "formal"
            },
            {
                "ko": "이 환자는 노란색 태그, 긴급 환자입니다.",
                "vi": "Bệnh nhân này được gắn thẻ vàng, là ca khẩn cấp.",
                "situation": "onsite"
            },
            {
                "ko": "트리아지에서 3단계라서 좀 기다려야 해요.",
                "vi": "Phân loại cấp độ 3 nên phải đợi một chút.",
                "situation": "informal"
            }
        ],
        "relatedTerms": ["KTAS", "응급실", "재난의료", "색상태그", "응급도"]
    }
]

def main():
    print("=" * 60)
    print("응급의학 전문용어 추가 스크립트 실행")
    print("=" * 60)

    # 파일 존재 확인
    if not os.path.exists(file_path):
        print(f"❌ 오류: {file_path} 파일을 찾을 수 없습니다.")
        return

    # 기존 데이터 로드
    with open(file_path, 'r', encoding='utf-8') as f:
        data = json.load(f)

    print(f"\n📊 기존 의료 용어 개수: {len(data)}개")

    # 기존 slug 목록 추출 (중복 방지)
    existing_slugs = {term['slug'] for term in data}
    print(f"📋 기존 slug 목록 확인 완료")

    # 중복되지 않은 새 용어만 필터링
    terms_to_add = [term for term in new_terms if term['slug'] not in existing_slugs]
    duplicates = [term['slug'] for term in new_terms if term['slug'] in existing_slugs]

    if duplicates:
        print(f"\n⚠️  중복된 slug 발견 (추가하지 않음): {', '.join(duplicates)}")

    if not terms_to_add:
        print("\n✅ 추가할 새 용어가 없습니다. (모두 중복)")
        return

    # 새 용어 추가
    data.extend(terms_to_add)
    print(f"\n✅ {len(terms_to_add)}개의 새 응급의학 용어 추가")

    # 파일 저장 (들여쓰기 2칸, 유니코드 그대로, 마지막 줄바꿈 포함)
    with open(file_path, 'w', encoding='utf-8') as f:
        json.dump(data, f, ensure_ascii=False, indent=2)
        f.write('\n')  # 마지막 줄바꿈

    print(f"💾 파일 저장 완료: {file_path}")
    print(f"📊 최종 의료 용어 개수: {len(data)}개")

    # 추가된 용어 목록 출력
    print("\n📝 추가된 용어:")
    for i, term in enumerate(terms_to_add, 1):
        print(f"  {i}. {term['korean']} ({term['vietnamese']}) - slug: {term['slug']}")

    print("\n" + "=" * 60)
    print("✨ 완료! 이제 'npm run validate:terms'로 품질을 검증하세요.")
    print("=" * 60)

if __name__ == '__main__':
    main()
