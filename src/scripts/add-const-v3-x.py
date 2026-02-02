#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Construction Terms Addition Script v3-x: Roof/Rooftop (지붕/옥상)
Tier S Quality Standard (90+ points)
10 terms: 슬래브, 파라펫, 옥상녹화, 기와, 금속지붕, 채광창, 물끊기, 물홈통, 드레인, 옥탑
"""

import json
import os

# 추가할 용어 데이터 (Tier S 기준)
data = [
    {
        "slug": "san-thuong",
        "korean": "옥상",
        "vietnamese": "Sàn thượng",
        "hanja": "屋上",
        "hanjaReading": "屋(집 옥) + 上(위 상)",
        "pronunciation": "억썽",
        "meaningKo": "건물의 맨 위층 지붕 위 평평한 공간. 통역 시 '옥상 방수', '옥상 녹화', '옥상 설비'처럼 복합어로 자주 쓰이므로 문맥 파악 필수. 베트남에서는 sàn thượng을 빨래 건조, 물탱크 설치 등 실용 공간으로 많이 활용하나, 한국은 최근 옥상정원이나 휴게공간으로 조성하는 경우가 많아 용도 차이 설명 필요. '옥상층'과 '옥탑'을 혼동하지 않도록 주의.",
        "meaningVi": "Không gian phẳng trên mái nhà ở tầng cao nhất của tòa nhà. Thường được sử dụng để phơi quần áo, đặt bồn nước hoặc thiết bị. Ở Hàn Quốc gần đây có xu hướng thiết kế thành vườn sân thượng hoặc không gian nghỉ ngơi.",
        "context": "건축 설계, 방수 시공, 옥상 설비",
        "culturalNote": "베트남의 옥상은 주로 실용적 공간(빨래 건조, 물탱크)으로 활용되지만, 한국은 옥상정원, 루프탑 카페 등 여가·상업 공간으로 변화 중. 건축법상 옥상 난간 높이, 방수 기준도 양국이 다르므로 설계 도면 통역 시 규정 차이 확인 필요. '옥상 방수층', '옥상 녹화 시스템' 등 전문 용어는 사전 숙지.",
        "commonMistakes": [
            {
                "mistake": "mái nhà (지붕)로 번역",
                "correction": "sàn thượng",
                "explanation": "mái nhà는 경사진 지붕, sàn thượng은 평평한 옥상. 구조가 다름"
            },
            {
                "mistake": "옥탑과 옥상 혼동",
                "correction": "옥탑(tầng gác mái)은 옥상 위 추가 구조물",
                "explanation": "옥상은 평평한 면, 옥탑은 그 위 작은 건물"
            },
            {
                "mistake": "'屋上'을 '집 위'로 직역",
                "correction": "건축 용어로서 옥상은 고유명사",
                "explanation": "한자 뜻보다 건축 개념으로 이해해야 함"
            }
        ],
        "examples": [
            {
                "ko": "옥상 방수 공사가 완료되었습니다.",
                "vi": "Công trình chống thấm sàn thượng đã hoàn thành.",
                "situation": "formal"
            },
            {
                "ko": "옥상에 물탱크 설치해야 돼요.",
                "vi": "Cần lắp đặt bồn nước trên sàn thượng.",
                "situation": "onsite"
            },
            {
                "ko": "이 건물 옥상은 녹화 공간으로 쓸 거예요.",
                "vi": "Sàn thượng của tòa nhà này sẽ được dùng làm vườn xanh.",
                "situation": "informal"
            }
        ],
        "relatedTerms": ["파라펫", "옥탑", "방수층", "드레인"]
    },
    {
        "slug": "tuong-chan-gio",
        "korean": "파라펫",
        "vietnamese": "Tường chắn gió",
        "hanja": None,
        "hanjaReading": None,
        "pronunciation": "뚜엉 쨘 지오",
        "meaningKo": "옥상이나 발코니 가장자리에 설치하는 낮은 난간벽. 통역 시 '난간'(lan can)과 구분 필수 - 난간은 주로 금속 구조물, 파라펫은 벽체 구조. 건축법상 추락 방지 높이 기준(한국 1.2m 이상)이 있으므로 설계 도면 검토 시 규정 확인 필요. 베트nam에서는 tường chắn gió(바람막이 벽) 또는 tường ngực(가슴 높이 벽)으로 표현하며, 방수·미관 기능도 겸함.",
        "meaningVi": "Bức tường thấp được xây dựng ở mép sàn thượng hoặc ban công để ngăn gió và phòng ngừa té ngã. Khác với lan can kim loại, đây là kết cấu tường xây. Ở Hàn Quốc quy định chiều cao tối thiểu 1.2m theo luật xây dựng.",
        "context": "옥상 설계, 안전 규정, 방수 시공",
        "culturalNote": "한국 건축에서 파라펫은 안전·방수·미관을 동시에 담당하는 중요 요소. 베트남 건축에서는 tường chắn gió로 주로 바람·비 차단 목적이 강조됨. 양국 모두 높이 규정이 엄격하나 기준이 다르므로 설계 변경 시 반드시 현지 법규 확인. '파라펫 캡핑', '파라펫 방수' 등 복합어는 사전 학습 필요.",
        "commonMistakes": [
            {
                "mistake": "lan can (난간)으로 번역",
                "correction": "tường chắn gió 또는 tường ngực",
                "explanation": "난간은 금속 구조, 파라펫은 벽체"
            },
            {
                "mistake": "parapet을 음차로 그대로 사용",
                "correction": "베트남어 고유 표현 사용",
                "explanation": "현장 근로자는 외래어보다 베트남어 선호"
            },
            {
                "mistake": "높이 기준 혼동",
                "correction": "한국 1.2m, 베트남은 현지 법규 확인",
                "explanation": "양국 건축법 기준이 다름"
            }
        ],
        "examples": [
            {
                "ko": "파라펫 높이를 1.2미터로 시공하세요.",
                "vi": "Xây tường chắn gió cao 1.2 mét.",
                "situation": "onsite"
            },
            {
                "ko": "파라펫 방수 처리가 미흡합니다.",
                "vi": "Xử lý chống thấm tường chắn gió chưa đạt yêu cầu.",
                "situation": "formal"
            },
            {
                "ko": "파라펫에 캡핑 작업 해야 돼요.",
                "vi": "Cần làm lớp phủ trên tường chắn gió.",
                "situation": "informal"
            }
        ],
        "relatedTerms": ["옥상", "난간", "방수층", "캡핑"]
    },
    {
        "slug": "vuon-tren-mai",
        "korean": "옥상녹화",
        "vietnamese": "Vườn trên mái",
        "hanja": "屋上綠化",
        "hanjaReading": "屋(집 옥) + 上(위 상) + 綠(푸를 록) + 化(될 화)",
        "pronunciation": "부온 쩬 마이",
        "meaningKo": "건물 옥상에 식물을 심어 녹지 공간을 조성하는 공법. 통역 시 '녹화'는 '녹색화(xanh hóa)'를 의미하며 '녹음·녹화(quay phim)'와 혼동 주의. 한국은 도시 열섬 완화, 에너지 절감 목적으로 공공건물에 의무화 추세. 베트남에서는 vườn trên mái 외에 mái xanh(그린 루프)라고도 하며, 방수·배수·하중 계산이 핵심 기술 요소. 설계 시 '경량형'과 '중량형' 구분 필요.",
        "meaningVi": "Công nghệ trồng cây xanh trên mái nhà hoặc sàn thượng của tòa nhà. Ở Hàn Quốc được khuyến khích để giảm hiệu ứng đảo nhiệt đô thị và tiết kiệm năng lượng. Yêu cầu kỹ thuật chính là chống thấm, thoát nước và tính toán tải trọng.",
        "context": "친환경 건축, 도시 계획, 에너지 절감",
        "culturalNote": "한국은 서울시 등 대도시에서 옥상녹화 의무 비율을 법제화하고 보조금 지원. 베트남은 아직 초기 단계로 호치민 일부 고급 건물에서 시도 중. 통역 시 '저관리 경량형(세덤)'과 '정원형 중량형' 구분, 관수 시스템, 방근층(chống rễ cây xuyên thấm) 등 전문 용어 숙지 필요. 양국 모두 하중 안전 검토는 필수.",
        "commonMistakes": [
            {
                "mistake": "quay phim (영상 녹화)로 오역",
                "correction": "vườn trên mái 또는 mái xanh",
                "explanation": "綠化는 '녹색화'이지 '녹음·녹화'가 아님"
            },
            {
                "mistake": "단순 화분 배치를 옥상녹화로 표현",
                "correction": "체계적인 방수·배수·식재 시스템 필요",
                "explanation": "옥상녹화는 공학적 설계가 필요한 시스템"
            },
            {
                "mistake": "하중 계산 생략",
                "correction": "토양·식물·물 무게 반드시 구조 검토",
                "explanation": "안전사고 위험"
            }
        ],
        "examples": [
            {
                "ko": "이 건물은 옥상녹화 의무 대상입니다.",
                "vi": "Tòa nhà này thuộc đối tượng bắt buộc làm vườn trên mái.",
                "situation": "formal"
            },
            {
                "ko": "세덤으로 경량 옥상녹화 하면 돼요.",
                "vi": "Dùng cây sedum làm vườn mái nhẹ là được.",
                "situation": "informal"
            },
            {
                "ko": "방근층 시공 후 배수판 깔아주세요.",
                "vi": "Sau khi thi công lớp chống rễ, hãy lát tấm thoát nước.",
                "situation": "onsite"
            }
        ],
        "relatedTerms": ["옥상", "방수층", "배수판", "세덤"]
    },
    {
        "slug": "ngoi",
        "korean": "기와",
        "vietnamese": "Ngói",
        "hanja": "瓦",
        "hanjaReading": "瓦(기와 와)",
        "pronunciation": "응오이",
        "meaningKo": "점토나 시멘트 등으로 만든 지붕 덮개 재료. 통역 시 한국 전통 '한식 기와(ngói Hàn Quốc truyền thống)'와 '시멘트 기와(ngói xi măng)', '금속 기와풍(tôn giả ngói)' 구분 필수. 베트남은 ngói âm dương(음양기와), ngói lợp(이엉 기와) 등 종류가 다양하며, 한국은 암·수 기와 결합 방식이 전통. 현대 건축에서는 경량 금속 기와나 아스팔트 슁글로 대체 추세.",
        "meaningVi": "Vật liệu lợp mái làm từ đất sét hoặc xi măng. Ở Việt Nam có nhiều loại như ngói âm dương, ngói lợp, ngói xi măng. Ở Hàn Quốc truyền thống dùng ngói đất nung với hệ thống âm dương kết hợp, hiện nay nhiều nơi chuyển sang tôn hoặc shingle nhựa đường.",
        "context": "전통 건축, 지붕 공사, 문화재 보수",
        "culturalNote": "한국 전통 한옥의 기와는 문화재적 가치가 높아 보수 시 장인 기술 필요. 베트남도 cổ trấn Hội An 등지에서 전통 기와 보존 중. 현대 건축에서는 한국이 금속 기와나 슁글을 선호하고, 베트남은 여전히 시멘트 기와 사용 많음. 통역 시 '기와 잇기', '기와 교체', '처마 기와' 등 시공 용어 숙지 필요.",
        "commonMistakes": [
            {
                "mistake": "모든 지붕재를 ngói로 통칭",
                "correction": "금속은 tôn, 슁글은 shingle",
                "explanation": "재료에 따라 명칭이 다름"
            },
            {
                "mistake": "한식 기와와 베트남 기와 형태 동일시",
                "correction": "암수 결합 방식, 크기, 무게가 다름",
                "explanation": "전통 방식이 다르므로 설명 필요"
            },
            {
                "mistake": "'瓦'를 '깨지다'로 오해",
                "correction": "기와(와) 한자는 지붕재 의미",
                "explanation": "한자 본뜻과 용도 구분"
            }
        ],
        "examples": [
            {
                "ko": "한옥 기와 보수 작업 견적을 내주세요.",
                "vi": "Vui lòng lập báo giá sửa chữa ngói nhà truyền thống Hàn Quốc.",
                "situation": "formal"
            },
            {
                "ko": "기와 몇 장 깨졌어요. 교체해야 돼요.",
                "vi": "Mấy viên ngói bị vỡ rồi. Cần thay mới.",
                "situation": "onsite"
            },
            {
                "ko": "이 건물은 시멘트 기와로 시공합니다.",
                "vi": "Tòa nhà này sẽ lợp bằng ngói xi măng.",
                "situation": "informal"
            }
        ],
        "relatedTerms": ["지붕", "처마", "슁글", "금속지붕"]
    },
    {
        "slug": "mai-ton",
        "korean": "금속지붕",
        "vietnamese": "Mái tôn",
        "hanja": "金屬지붕",
        "hanjaReading": "金(쇠 금) + 屬(무리 속)",
        "pronunciation": "마이 똔",
        "meaningKo": "강판이나 알루미늄 등 금속 재료로 만든 지붕. 통역 시 '함석지붕(mái tôn)', '징크 도금 강판(tôn mạ kẽm)', '컬러강판(tôn màu)', '스탠딩심(tôn đứng)' 등 세부 구분 필요. 한국은 공장·창고에 주로 쓰이고 주택은 아스팔트 슁글 선호. 베트남은 주택에도 mái tôn 사용 많으나 소음·단열 문제로 tôn cách nhiệt(단열 함석) 보급 중. 시공 시 열팽창 고려 필수.",
        "meaningVi": "Mái nhà làm bằng vật liệu kim loại như tôn thép, tôn nhôm. Ở Việt Nam phổ biến cho cả nhà ở và nhà xưởng, nhưng có vấn đề về tiếng ồn và cách nhiệt. Ở Hàn Quốc chủ yếu dùng cho nhà kho, nhà máy, nhà ở ít dùng hơn.",
        "context": "공장 건축, 창고 시공, 저비용 주택",
        "culturalNote": "베트남 농촌에서는 mái tôn이 저렴하고 시공 빠른 장점으로 널리 쓰임. 한국은 주택용으로는 미관상 기피하고 공업 시설에 한정. 최근 양국 모두 단열재 합판(tôn sandwich) 기술 발달로 성능 개선 중. 통역 시 '골조', '체결 볼트', '방청 처리' 등 시공 용어 중요.",
        "commonMistakes": [
            {
                "mistake": "mái sắt (철판 지붕)로 표현",
                "correction": "mái tôn이 일반적",
                "explanation": "베트남에서 tôn이 통용어"
            },
            {
                "mistake": "소음·단열 문제 간과",
                "correction": "tôn cách nhiệt 또는 lớp cách âm 필요",
                "explanation": "주거용은 반드시 단열·방음 고려"
            },
            {
                "mistake": "열팽창 여유 미확보",
                "correction": "체결 시 이동 여유 필수",
                "explanation": "금속은 온도 변화에 민감"
            }
        ],
        "examples": [
            {
                "ko": "공장 지붕을 금속 샌드위치 패널로 시공하세요.",
                "vi": "Lợp mái nhà xưởng bằng tấm tôn sandwich.",
                "situation": "onsite"
            },
            {
                "ko": "금속지붕 누수 부위 확인해주세요.",
                "vi": "Vui lòng kiểm tra vị trí rò rỉ trên mái tôn.",
                "situation": "formal"
            },
            {
                "ko": "함석 지붕 소음 때문에 단열재 추가해야 돼요.",
                "vi": "Phải thêm vật liệu cách nhiệt vì mái tôn ồn quá.",
                "situation": "informal"
            }
        ],
        "relatedTerms": ["샌드위치 패널", "함석", "컬러강판", "방청"]
    },
    {
        "slug": "cua-so-mai",
        "korean": "채광창",
        "vietnamese": "Cửa sổ mái",
        "hanja": "採光窗",
        "hanjaReading": "採(캘 채) + 光(빛 광) + 窗(창 창)",
        "pronunciation": "꾸어 쏘 마이",
        "meaningKo": "지붕이나 천장에 설치해 자연광을 실내로 들이는 창. 통역 시 '천창(skylight)', '루프창', '탑라이트' 등 다양한 표현이 있으나 베트남어는 cửa sổ mái로 통일. 한국은 주택 다락방이나 공장·미술관에 설치하며, 채광·환기·미관 목적. 시공 시 방수(chống thấm), 열손실 방지(chống thất thoát nhiệt), 결로 방지(chống ngưng tụ) 중요. 개폐형과 고정형 구분 필요.",
        "meaningVi": "Cửa sổ được lắp trên mái hoặc trần nhà để đưa ánh sáng tự nhiên vào trong. Ở Hàn Quốc thường dùng cho gác mái nhà ở hoặc nhà máy, bảo tàng. Khi thi công cần chú ý chống thấm, chống thất thoát nhiệt và chống ngưng tụ. Có loại mở được và loại cố định.",
        "context": "주택 설계, 공장 채광, 친환경 건축",
        "culturalNote": "한국은 에너지 절약형 주택에서 채광창 의무 설치 권장. 베트남은 열대 기후로 과도한 직사광선 유입 우려 있어 차양(che nắng) 병행 필수. 양국 모두 방수·결로가 핵심 이슈. 통역 시 'Low-E 유리(kính Low-E)', '이중 유리(kính 2 lớp)', '전동 개폐(mở điện)' 등 옵션 설명 능력 필요.",
        "commonMistakes": [
            {
                "mistake": "cửa sổ thường (일반 창문)으로 번역",
                "correction": "cửa sổ mái (지붕창) 명시",
                "explanation": "위치가 다르므로 구분 필요"
            },
            {
                "mistake": "방수 처리 생략",
                "correction": "플래싱(miếng chặn nước) 필수 시공",
                "explanation": "누수 주요 원인"
            },
            {
                "mistake": "베트남 기후 고려 안 함",
                "correction": "차양, 열차단 필름 추가 검토",
                "explanation": "직사광선으로 과열 가능"
            }
        ],
        "examples": [
            {
                "ko": "다락방에 채광창 2개 설치해주세요.",
                "vi": "Vui lòng lắp 2 cửa sổ mái cho gác xép.",
                "situation": "formal"
            },
            {
                "ko": "채광창 주변 누수 보수 작업 필요해요.",
                "vi": "Cần sửa chữa chỗ rò rỉ xung quanh cửa sổ mái.",
                "situation": "onsite"
            },
            {
                "ko": "자동 개폐 채광창으로 바꿔요.",
                "vi": "Đổi sang cửa sổ mái mở tự động nhé.",
                "situation": "informal"
            }
        ],
        "relatedTerms": ["천창", "지붕", "방수", "결로"]
    },
    {
        "slug": "rach-nuoc",
        "korean": "물끊기",
        "vietnamese": "Rạch nước",
        "hanja": None,
        "hanjaReading": None,
        "pronunciation": "잌 느억",
        "meaningKo": "외벽이나 창틀 하단에 빗물이 역류하지 않도록 홈을 파는 시공법. 통역 시 '물끊기홈(rạch nước)', '드립(drip)', '워터컷(water cut)' 등으로 불리며, 베트남어는 rạch nước 또는 홈 thoát nước가 일반적. 창틀·처마·파라펫 하단에 필수 시공하며, 깊이 5~10mm 권장. 누수·곰팡이 방지 핵심 디테일로, 시공 누락 시 외벽 오염 및 누수 원인. 도면에 명시 안 되는 경우 많아 현장 확인 필요.",
        "meaningVi": "Rãnh nhỏ được tạo ở mặt dưới của khung cửa sổ hoặc mái hiên để nước mưa không chảy ngược vào trong. Còn gọi là drip hoặc water cut. Độ sâu khuyến nghị 5-10mm. Là chi tiết quan trọng để phòng ngừa thấm nước và nấm mốc.",
        "context": "방수 시공, 창호 설치, 외벽 마감",
        "culturalNote": "한국 건축에서는 최근 필수 디테일로 자리잡았으나, 과거 시공 건물에는 누락된 경우 많아 리모델링 시 보완 필요. 베트남은 우기 강수량이 많아 물끊기 시공 더욱 중요하나, 현장에서 인식 부족한 경우 있음. 통역 시 '물이 타고 올라가지 않도록(không cho nước chảy ngược)' 기능 설명 중요.",
        "commonMistakes": [
            {
                "mistake": "홈 thoát nước (배수구)로 혼동",
                "correction": "rạch nước는 역류 방지 홈",
                "explanation": "배수와 역류 방지는 다른 개념"
            },
            {
                "mistake": "깊이 부족 (1~2mm)",
                "correction": "최소 5mm 이상 확보",
                "explanation": "너무 얕으면 효과 없음"
            },
            {
                "mistake": "도면 미표기로 시공 누락",
                "correction": "현장 감리 시 반드시 확인",
                "explanation": "누수 사후 보수 비용이 큼"
            }
        ],
        "examples": [
            {
                "ko": "창틀 하단에 물끊기 홈 가공해주세요.",
                "vi": "Hãy tạo rạch nước ở mặt dưới khung cửa sổ.",
                "situation": "onsite"
            },
            {
                "ko": "물끊기 시공이 누락되어 외벽 오염이 발생했습니다.",
                "vi": "Do thiếu rạch nước nên tường ngoài bị bẩn.",
                "situation": "formal"
            },
            {
                "ko": "처마 밑에 물끊기 해야 돼요.",
                "vi": "Phải làm rạch nước dưới mái hiên.",
                "situation": "informal"
            }
        ],
        "relatedTerms": ["방수", "처마", "창틀", "드립"]
    },
    {
        "slug": "may-thoat-nuoc",
        "korean": "물홈통",
        "vietnamese": "Máng thoát nước",
        "hanja": None,
        "hanjaRading": None,
        "pronunciation": "망 토앝 느억",
        "meaningKo": "지붕 처마 끝에 설치해 빗물을 모아 배수하는 홈통. 통역 시 '낙수받이', '처마홈통', '거터(gutter)' 등으로도 불리며, 베트남어는 máng thoát nước 또는 máng xối. 재질은 PVC, 아연도금강판, 스테인리스 등 다양. 한국은 주로 사각 단면, 베트남은 반원형 많음. 설치 시 적정 기울기(1~2%) 확보해야 물고임 방지. 낙엽 막이(lưới chắn lá) 병행 권장.",
        "meaningVi": "Máng được lắp ở mép mái nhà để thu và thoát nước mưa. Còn gọi là máng xối hoặc gutter. Vật liệu phổ biến là PVC, tôn mạ kẽm, inox. Ở Việt Nam thường dùng dạng bán nguyệt, ở Hàn Quốc dùng dạng vuông nhiều hơn. Cần đảm bảo độ dốc 1-2% để tránh đọng nước.",
        "context": "지붕 공사, 배수 시스템, 외벽 보호",
        "culturalNote": "한국은 겨울철 결빙으로 물홈통 파손 우려 있어 열선(dây sưởi) 설치하기도 함. 베트남은 우기 집중 호우 대비로 단면적 크게 설계 필요. 양국 모두 낙엽·쓰레기로 막힘 주의. 통역 시 '낙수관(ống thoát nước)', '집수구(miệng thu nước)' 등 부속 용어 함께 숙지.",
        "commonMistakes": [
            {
                "mistake": "ống thoát nước (배수관)와 혼동",
                "correction": "máng thoát nước는 처마 수평 홈통",
                "explanation": "위치와 형태가 다름"
            },
            {
                "mistake": "기울기 없이 수평 설치",
                "correction": "1~2% 기울기 필수",
                "explanation": "물고임으로 모기·오염 발생"
            },
            {
                "mistake": "한국 겨울 결빙 미고려",
                "correction": "열선 또는 단열 조치 필요",
                "explanation": "결빙 시 파손 위험"
            }
        ],
        "examples": [
            {
                "ko": "물홈통 기울기를 1.5%로 맞춰주세요.",
                "vi": "Hãy lắp máng thoát nước với độ dốc 1.5%.",
                "situation": "onsite"
            },
            {
                "ko": "물홈통이 낙엽으로 막혔습니다.",
                "vi": "Máng thoát nước bị lá cây tắc rồi.",
                "situation": "informal"
            },
            {
                "ko": "스테인리스 물홈통으로 교체 견적 부탁드립니다.",
                "vi": "Vui lòng báo giá thay máng thoát nước bằng inox.",
                "situation": "formal"
            }
        ],
        "relatedTerms": ["낙수관", "처마", "배수구", "거터"]
    },
    {
        "slug": "cong-thoat-nuoc",
        "korean": "드레인",
        "vietnamese": "Cống thoát nước",
        "hanja": None,
        "hanjaReading": None,
        "pronunciation": "꽁 토앝 느억",
        "meaningKo": "옥상이나 바닥에서 물을 배수하는 배수구. 통역 시 'drain'을 그대로 쓰기도 하나 베트남어는 cống thoát nước 또는 hố ga가 일반적. 옥상 드레인은 cống sàn thượng, 바닥 드레인은 ga thu nước sàn. 한국은 루프 드레인(roof drain) 막힘 방지용 스트레이너(lưới lọc) 필수 설치. 베트남은 대형 낙엽·쓰레기 유입 많아 청소 주기 짧게 관리 필요. 동절기 결빙 주의.",
        "meaningVi": "Cống thoát nước trên sàn thượng hoặc sàn nhà. Còn gọi là hố ga. Ở Hàn Quốc bắt buộc lắp lưới lọc (strainer) để tránh tắc nghẽn. Ở Việt Nam do lá cây, rác nhiều nên cần vệ sinh thường xuyên. Mùa đông ở Hàn Quốc cần chú ý đóng băng.",
        "context": "옥상 방수, 배수 설계, 하수 시스템",
        "culturalNote": "한국은 옥상 드레인 막힘 시 역류로 방수층 손상 우려 커서 정기 점검 강조. 베트남은 우기 집중 호우로 배수 용량 부족 문제 많아 드레인 개수·크기 설계 시 여유 확보 필요. 양국 모두 '트랩(bẫy mùi)' 설치로 악취 차단. 통역 시 '오버플로우(tràn)', '역류 방지(chống trào ngược)' 개념 중요.",
        "commonMistakes": [
            {
                "mistake": "hố ga (맨홀)와 혼동",
                "correction": "옥상은 cống sàn thượng, 도로는 hố ga",
                "explanation": "위치와 용도에 따라 구분"
            },
            {
                "mistake": "스트레이너 미설치",
                "correction": "lưới lọc 필수",
                "explanation": "낙엽·쓰레기로 막힘 방지"
            },
            {
                "mistake": "배수 용량 과소 설계",
                "correction": "집중 호우 대비 여유 확보",
                "explanation": "베트남 우기 강수량 고려"
            }
        ],
        "examples": [
            {
                "ko": "옥상 드레인 청소 좀 해주세요.",
                "vi": "Hãy vệ sinh cống thoát nước sàn thượng.",
                "situation": "onsite"
            },
            {
                "ko": "드레인이 막혀서 물이 고입니다.",
                "vi": "Cống bị tắc nên nước đọng lại.",
                "situation": "informal"
            },
            {
                "ko": "루프 드레인 스트레이너를 스테인리스로 교체하세요.",
                "vi": "Thay lưới lọc cống mái bằng inox.",
                "situation": "formal"
            }
        ],
        "relatedTerms": ["옥상", "배수관", "트랩", "스트레이너"]
    },
    {
        "slug": "tang-gac-mai",
        "korean": "옥탑",
        "vietnamese": "Tầng gác mái",
        "hanja": "屋塔",
        "hanjaReading": "屋(집 옥) + 塔(탑 탑)",
        "pronunciation": "땅 각 마이",
        "meaningKo": "옥상 위에 추가로 지어진 작은 구조물. 통역 시 '옥상(sàn thượng)'과 구분 필수 - 옥상은 평평한 면, 옥탑은 그 위 작은 건물. 한국 옥탑방(phòng gác mái)은 저렴한 주거 공간으로 인식되며, 엘리베이터 기계실·물탱크실 등 설비 공간으로도 활용. 베트남에서는 tầng gác mái 또는 penthouse(고급형)로 구분. 건폐율·용적률 계산 시 옥탑 면적 제외 조건 있음.",
        "meaningVi": "Kết cấu nhỏ được xây thêm trên sàn thượng. Ở Hàn Quốc, phòng gác mái (옥탑방) thường là nơi ở giá rẻ, hoặc dùng làm phòng máy thang máy, bồn nước. Ở Việt Nam gọi là tầng gác mái hoặc penthouse (loại cao cấp). Diện tích gác mái có thể được loại trừ khỏi tính toán tỷ lệ xây dựng trong một số trường hợp.",
        "context": "건축 설계, 주거 공간, 설비 배치",
        "culturalNote": "한국 옥탑방은 1960~90년대 도시 저소득층 주거 공간으로 문화적 상징성 있음. 최근은 리모델링해 루프탑 하우스로 활용하기도. 베트남 penthouse는 고급 주거 이미지 강함. 통역 시 '옥탑 증축', '옥탑 철거', '옥탑 방수' 등 시공 관련 용어 숙지. 건축법상 높이·면적 제한 양국 상이.",
        "commonMistakes": [
            {
                "mistake": "옥상과 옥탑 혼용",
                "correction": "옥상(sàn thượng)은 평면, 옥탑(tầng gác mái)은 구조물",
                "explanation": "구조와 용도가 다름"
            },
            {
                "mistake": "penthouse와 동일시",
                "correction": "한국 옥탑방≠고급 penthouse",
                "explanation": "문화적 의미 차이 설명 필요"
            },
            {
                "mistake": "건폐율 계산 시 옥탑 포함",
                "correction": "조건 충족 시 제외 가능",
                "explanation": "양국 건축법 확인 필요"
            }
        ],
        "examples": [
            {
                "ko": "엘리베이터 기계실을 옥탑에 설치합니다.",
                "vi": "Lắp phòng máy thang máy ở tầng gác mái.",
                "situation": "formal"
            },
            {
                "ko": "옥탑방 방수 공사 필요해요.",
                "vi": "Cần làm chống thấm cho phòng gác mái.",
                "situation": "onsite"
            },
            {
                "ko": "이 건물 옥탑 면적은 건폐율에 안 들어가요.",
                "vi": "Diện tích gác mái của tòa này không tính vào tỷ lệ xây dựng.",
                "situation": "informal"
            }
        ],
        "relatedTerms": ["옥상", "엘리베이터", "기계실", "방수"]
    }
]

# 파일 경로 설정
project_root = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
json_file_path = os.path.join(project_root, "data", "terms", "construction.json")

# 기존 JSON 파일 읽기
with open(json_file_path, "r", encoding="utf-8") as f:
    existing_data = json.load(f)

# 새 용어 추가
existing_data.extend(data)

# JSON 파일 저장 (UTF-8, indent=2, ensure_ascii=False)
with open(json_file_path, "w", encoding="utf-8") as f:
    json.dump(existing_data, f, ensure_ascii=False, indent=2)

print(f"✅ {len(data)}개 지붕/옥상 용어 추가 완료")
print(f"📁 파일: {json_file_path}")
print(f"📊 총 용어 수: {len(existing_data)}개")
print("\n추가된 용어:")
for term in data:
    print(f"  - {term['korean']} ({term['vietnamese']})")
