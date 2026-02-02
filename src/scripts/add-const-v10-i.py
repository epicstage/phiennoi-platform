#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
건설민원/환경관리 용어 추가 스크립트 (Construction Complaints/Environmental Management)
Tier S 품질 기준 준수
"""

import json
import os

def main():
    # 1. 파일 경로 설정
    file_path = os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', 'data', 'terms', 'construction.json')

    # 2. 기존 데이터 로드
    with open(file_path, 'r', encoding='utf-8') as f:
        data = json.load(f)  # data is a LIST

    # 3. 기존 slug 추출
    existing_slugs = {t['slug'] for t in data}

    # 4. 새 용어 정의
    new_terms = [
        {
            "slug": "khieu-nai",
            "korean": "민원",
            "vietnamese": "khiếu nại",
            "hanja": "民願",
            "hanjaReading": "民(백성 민) + 願(원할 원)",
            "pronunciation": "끼에우 나이",
            "meaningKo": "시민이나 주민이 행정기관이나 사업자에게 불만이나 요구사항을 제기하는 행위. 건설 현장에서는 소음, 분진, 진동 등으로 인한 주민 불편 사항이 주요 민원 대상이 됩니다. 통역 시 주의할 점은 베트남어 'khiếu nại'는 '불만 제기'라는 부정적 뉘앙스가 강하므로, 맥락에 따라 'ý kiến'(의견) 또는 'phản ánh'(반영 요청)으로 순화해서 표현하는 것이 원만한 대화에 도움이 됩니다. 민원 접수 시 'tiếp nhận khiếu nại'라고 표현합니다.",
            "meaningVi": "Hành động công dân hoặc cư dân đưa ra khiếu nại, bất mãn hoặc yêu cầu đối với cơ quan hành chính hoặc chủ đầu tư. Tại công trường xây dựng, tiếng ồn, bụi, rung động là những nguyên nhân chính gây khiếu nại từ người dân xung quanh.",
            "context": "건설 현장 주변 주민과의 소통, 행정 처리",
            "culturalNote": "한국에서는 민원이 매우 체계적으로 관리되며 '국민신문고' 등 온라인 플랫폼을 통해 접수됩니다. 베트남에서는 'khiếu nại'가 법적 절차로 이어질 수 있어 더 무거운 의미를 가지므로, 일상적 불만은 'phản ánh' 또는 'ý kiến đóng góp'로 표현하는 것이 일반적입니다. 한국 현장에서는 민원 예방을 위해 사전 설명회를 자주 여는 반면, 베트남에서는 사후 처리가 더 일반적입니다.",
            "commonMistakes": [
                {
                    "mistake": "khiếu kiện",
                    "correction": "khiếu nại",
                    "explanation": "'khiếu kiện'은 법적 소송을 의미하므로 민원보다 훨씬 무거운 표현입니다."
                },
                {
                    "mistake": "complain",
                    "correction": "khiếu nại / phản ánh",
                    "explanation": "영어 'complain'을 그대로 쓰지 말고 상황에 맞는 베트남어를 사용해야 합니다."
                },
                {
                    "mistake": "dân nguyện",
                    "correction": "khiếu nại",
                    "explanation": "'dân nguyện'은 오래된 한자어 차용으로 현대 베트남어에서는 거의 쓰이지 않습니다."
                }
            ],
            "examples": [
                {
                    "ko": "소음 관련 민원이 접수되어 즉시 방음벽을 설치했습니다.",
                    "vi": "Đã tiếp nhận khiếu nại về tiếng ồn và lập tức lắp đặt tường cách âm.",
                    "situation": "formal"
                },
                {
                    "ko": "민원 발생 시 24시간 내 답변 드리겠습니다.",
                    "vi": "Khi có khiếu nại, chúng tôi sẽ phản hồi trong vòng 24 giờ.",
                    "situation": "onsite"
                },
                {
                    "ko": "주민 의견을 수렴하여 작업 시간을 조정했습니다.",
                    "vi": "Đã điều chỉnh giờ làm việc sau khi lắng nghe ý kiến của cư dân.",
                    "situation": "formal"
                }
            ],
            "relatedTerms": ["tieng-on", "bui", "rung-dong", "giao-tiep-dan-su"]
        },
        {
            "slug": "tieng-on",
            "korean": "소음",
            "vietnamese": "tiếng ồn",
            "hanja": "騷音",
            "hanjaReading": "騷(시끄러울 소) + 音(소리 음)",
            "pronunciation": "띠엥 언",
            "meaningKo": "건설 현장에서 발생하는 과도한 소리로 주변 환경이나 주민에게 불쾌감을 주는 음향. 통역 시 주의할 점은 'tiếng ồn'이 일반적 소음이고, 'tiếng động lớn'은 큰 소리, 'ô nhiễm tiếng ồn'은 소음 공해를 의미합니다. 소음 측정 시 'đo tiếng ồn', 소음 저감 시 'giảm tiếng ồn' 또는 'kiểm soát tiếng ồn'이라고 표현합니다. 공사 시간대별 소음 허용 기준이 한국과 베트남이 다르므로 반드시 현지 기준을 확인해야 합니다.",
            "meaningVi": "Âm thanh quá mức phát sinh từ công trường xây dựng gây khó chịu cho môi trường xung quanh và người dân. Tiếng ồn từ máy móc, xe tải, búa đóng cọc là những nguồn chính gây ảnh hưởng đến khu vực lân cận.",
            "context": "환경 관리, 소음 측정 및 규제",
            "culturalNote": "한국은 '소음진동관리법'으로 주간 70dB, 야간 55dB 등 엄격한 기준을 적용하며 위반 시 과태료가 부과됩니다. 베트남도 'QCVN 26:2010/BTNMT' 기준이 있지만 집행이 덜 엄격한 편입니다. 한국 현장에서는 소음측정기를 상시 운영하고 실시간 데이터를 공개하는 경우가 많습니다. 베트남 통역사는 소음 단위 'decibel (dB)'를 'đề xi ben' 또는 'dB'로 표현합니다.",
            "commonMistakes": [
                {
                    "mistake": "âm thanh ồn",
                    "correction": "tiếng ồn",
                    "explanation": "'âm thanh ồn'은 어색한 표현이며 'tiếng ồn'이 표준입니다."
                },
                {
                    "mistake": "nhiễu âm",
                    "correction": "tiếng ồn / ô nhiễm tiếng ồn",
                    "explanation": "'nhiễu âm'은 음향 기술 용어로 소음과는 다른 의미입니다."
                },
                {
                    "mistake": "noise",
                    "correction": "tiếng ồn",
                    "explanation": "영어 단어를 그대로 쓰지 말고 베트남어를 사용해야 합니다."
                }
            ],
            "examples": [
                {
                    "ko": "야간 공사로 인한 소음을 최소화하기 위해 저소음 장비를 사용합니다.",
                    "vi": "Sử dụng thiết bị ít tiếng ồn để giảm thiểu tiếng ồn từ thi công ban đêm.",
                    "situation": "formal"
                },
                {
                    "ko": "소음 측정 결과 기준치를 초과하여 작업을 중단했습니다.",
                    "vi": "Kết quả đo tiếng ồn vượt ngưỡng cho phép nên đã tạm dừng thi công.",
                    "situation": "onsite"
                },
                {
                    "ko": "오전 8시 이전에는 소음이 큰 작업을 하지 않습니다.",
                    "vi": "Không thực hiện các công việc gây tiếng ồn lớn trước 8 giờ sáng.",
                    "situation": "informal"
                }
            ],
            "relatedTerms": ["khieu-nai", "rung-dong", "phong-am", "do-luong-moi-truong"]
        },
        {
            "slug": "bui",
            "korean": "분진",
            "vietnamese": "bụi",
            "hanja": "粉塵",
            "hanjaReading": "粉(가루 분) + 塵(티끌 진)",
            "pronunciation": "부이",
            "meaningKo": "건설 현장에서 발생하는 미세한 고체 입자로 공기 중에 떠다니는 먼지. 통역 시 주의할 점은 베트남어에서 'bụi'는 일반 먼지, 'bụi mịn'은 미세먼지(PM10, PM2.5), 'bụi xây dựng'은 건설 분진을 구분해서 사용합니다. 분진 억제는 'kiểm soát bụi' 또는 'chống bụi', 방진 조치는 'biện pháp chống bụi'라고 표현합니다. 건강 영향 설명 시 'ảnh hưởng đến sức khỏe' 또는 'gây hại cho phổi'(폐에 해로움) 등으로 구체화합니다.",
            "meaningVi": "Hạt rắn nhỏ phát sinh từ công trường xây dựng bay lơ lửng trong không khí. Bụi từ phá dỡ, cắt, khoan, vận chuyển vật liệu có thể gây hại cho sức khỏe công nhân và người dân xung quanh.",
            "context": "환경 안전, 작업자 보호, 주민 건강",
            "culturalNote": "한국은 '미세먼지 저감 및 관리에 관한 특별법'으로 건설 현장 분진 관리를 엄격히 규제하며, 실시간 측정기 설치와 살수 시설 운영이 의무화되어 있습니다. 베트남도 환경법이 있지만 집행이 상대적으로 느슨합니다. 한국 현장에서는 'PM10', 'PM2.5' 용어를 많이 쓰는데, 베트nam에서는 'bụi mịn' 또는 'PM'으로 줄여 말합니다. 보호장비로 'khẩu trang chống bụi'(방진마스크)를 반드시 착용해야 합니다.",
            "commonMistakes": [
                {
                    "mistake": "bồ hóng",
                    "correction": "bụi",
                    "explanation": "'bồ hóng'은 그을음을 의미하며 분진과는 다릅니다."
                },
                {
                    "mistake": "bụi bặm",
                    "correction": "bụi",
                    "explanation": "'bụi bặm'은 '지저분함'을 의미하는 구어체로 기술 용어가 아닙니다."
                },
                {
                    "mistake": "phấn trần",
                    "correction": "bụi / phân trần",
                    "explanation": "'phấn'은 가루(powder)이고 한자어 그대로 읽으면 부자연스럽습니다."
                }
            ],
            "examples": [
                {
                    "ko": "분진 발생을 줄이기 위해 정기적으로 살수 작업을 실시합니다.",
                    "vi": "Thực hiện tưới nước định kỳ để giảm phát sinh bụi.",
                    "situation": "onsite"
                },
                {
                    "ko": "미세먼지 농도가 높아 야외 작업을 일시 중단합니다.",
                    "vi": "Tạm dừng công việc ngoài trời do nồng độ bụi mịn cao.",
                    "situation": "formal"
                },
                {
                    "ko": "모든 작업자는 방진마스크를 필수로 착용하세요.",
                    "vi": "Tất cả công nhân phải đeo khẩu trang chống bụi.",
                    "situation": "onsite"
                }
            ],
            "relatedTerms": ["tuoi-nuoc-chong-bui", "hang-rao-chan-bui", "khau-trang", "pm10"]
        },
        {
            "slug": "rung-dong",
            "korean": "진동",
            "vietnamese": "rung động",
            "hanja": "振動",
            "hanjaReading": "振(떨칠 진) + 動(움직일 동)",
            "pronunciation": "중 동",
            "meaningKo": "건설 현장에서 기계나 장비의 작동으로 발생하는 물리적 떨림 현상. 통역 시 주의할 점은 'rung động'은 일반적인 진동, 'rung lắc'은 흔들림(주로 지진), 'dao động'은 진동/변동을 포괄하는 용어입니다. 진동 측정은 'đo rung động', 진동 저감은 'giảm rung động' 또는 'kiểm soát rung động'이라고 표현합니다. 진동 단위는 'cm/s'(초속 센티미터)나 'dB(V)'(진동 데시벨)을 사용하며, 베트남어로는 'xen-ti-met trên giây' 또는 'đề xi ben rung động'으로 설명합니다.",
            "meaningVi": "Hiện tượng rung lắc vật lý phát sinh từ máy móc hoặc thiết bị tại công trường xây dựng. Rung động từ đóng cọc, đào đất, phá dỡ có thể ảnh hưởng đến công trình lân cận và gây khó chịu cho cư dân.",
            "context": "환경 안전, 구조물 안전, 민원 관리",
            "culturalNote": "한국은 '소음진동관리법'으로 진동 허용 기준(주간 70dB(V), 야간 65dB(V) 등)을 엄격히 규제하고, 특히 도심지 항타 작업 시 주변 건물 안전 진단을 병행합니다. 베트남도 'TCVN 7027:2008' 기준이 있지만 측정 장비와 감독이 부족한 편입니다. 한국 현장에서는 실시간 진동 모니터링을 통해 데이터를 기록하고, 허용치 초과 시 자동으로 경보가 울립니다. 통역사는 '균열(nứt)'과 '침하(lún)' 같은 진동 피해 용어도 숙지해야 합니다.",
            "commonMistakes": [
                {
                    "mistake": "chấn động",
                    "correction": "rung động",
                    "explanation": "'chấn động'은 충격이나 감정적 동요를 의미하며 물리적 진동과는 다릅니다."
                },
                {
                    "mistake": "rung lắc",
                    "correction": "rung động",
                    "explanation": "'rung lắc'은 주로 지진과 같은 큰 흔들림을 의미하며, 기계 진동은 'rung động'이 적합합니다."
                },
                {
                    "mistake": "dao động",
                    "correction": "rung động",
                    "explanation": "'dao động'은 넓은 의미의 변동/진동이며, 건설 진동은 'rung động'이 더 정확합니다."
                }
            ],
            "examples": [
                {
                    "ko": "항타 작업으로 인한 진동을 모니터링하여 안전을 확보합니다.",
                    "vi": "Giám sát rung động từ đóng cọc để đảm bảo an toàn.",
                    "situation": "formal"
                },
                {
                    "ko": "진동 측정 결과 허용 기준을 초과하지 않았습니다.",
                    "vi": "Kết quả đo rung động không vượt ngưỡng cho phép.",
                    "situation": "onsite"
                },
                {
                    "ko": "진동 저감을 위해 저진동 공법을 적용합니다.",
                    "vi": "Áp dụng công pháp ít rung động để giảm thiểu rung động.",
                    "situation": "formal"
                }
            ],
            "relatedTerms": ["dong-coc", "pha-do", "do-luong-moi-truong", "kiem-dinh-an-toan"]
        },
        {
            "slug": "xu-ly-nuoc-thai",
            "korean": "폐수처리",
            "vietnamese": "xử lý nước thải",
            "hanja": "廢水處理",
            "hanjaReading": "廢(버릴 폐) + 水(물 수) + 處(처리할 처) + 理(다스릴 리)",
            "pronunciation": "쑤 리 느억 타이",
            "meaningKo": "건설 현장에서 발생하는 오염된 물을 정화하여 배출하거나 재사용하는 과정. 통역 시 주의할 점은 'xử lý nước thải'는 폐수처리 전체 과정, 'làm sạch nước thải'는 정화, 'tái sử dụng nước thải'는 재활용을 의미합니다. 처리 단계는 'xử lý sơ bộ'(1차 처리), 'xử lý thứ cấp'(2차 처리), 'xử lý nâng cao'(3차 처리)로 구분됩니다. 배출 기준은 'tiêu chuẩn xả thải', 폐수 검사는 'kiểm tra nước thải'라고 표현합니다.",
            "meaningVi": "Quá trình xử lý nước bị ô nhiễm từ công trường xây dựng để có thể xả ra môi trường hoặc tái sử dụng. Nước thải xây dựng chứa xi măng, bùn đất, dầu mỡ cần được xử lý đạt tiêu chuẩn trước khi thải ra nguồn nước.",
            "context": "환경 관리, 수질 보호, 법규 준수",
            "culturalNote": "한국은 '물환경보전법'으로 건설 현장 폐수 배출을 엄격히 규제하며, 생물화학적 산소요구량(BOD), 화학적 산소요구량(COD), 부유물질(SS) 등의 기준을 준수해야 합니다. 베트남은 'QCVN 40:2011/BTNMT' 기준이 있으며, 칼럼 A(엄격)와 칼럼 B(일반)로 구분합니다. 한국 현장에서는 폐수처리 시설을 필수로 설치하고 정기적으로 수질 검사를 받지만, 베트남에서는 소규모 현장에서는 간이 침전조만 운영하는 경우도 많습니다.",
            "commonMistakes": [
                {
                    "mistake": "xử lý nước bẩn",
                    "correction": "xử lý nước thải",
                    "explanation": "'nước bẩn'은 '더러운 물'이라는 구어체이고, 'nước thải'가 기술 용어입니다."
                },
                {
                    "mistake": "lọc nước",
                    "correction": "xử lý nước thải",
                    "explanation": "'lọc nước'는 정수(깨끗한 물 만들기)이고, 폐수처리는 'xử lý nước thải'입니다."
                },
                {
                    "mistake": "thải nước",
                    "correction": "xử lý nước thải",
                    "explanation": "'thải nước'는 물 배출이고, 처리 과정은 'xử lý'를 반드시 포함해야 합니다."
                }
            ],
            "examples": [
                {
                    "ko": "모든 폐수는 처리 후 수질 기준을 충족해야 배출할 수 있습니다.",
                    "vi": "Tất cả nước thải phải được xử lý đạt tiêu chuẩn chất lượng nước trước khi xả.",
                    "situation": "formal"
                },
                {
                    "ko": "폐수처리 시설이 정상 작동하는지 매일 점검합니다.",
                    "vi": "Kiểm tra hàng ngày để đảm bảo hệ thống xử lý nước thải hoạt động bình thường.",
                    "situation": "onsite"
                },
                {
                    "ko": "처리된 폐수는 살수용으로 재활용합니다.",
                    "vi": "Nước thải đã xử lý được tái sử dụng cho mục đích tưới nước.",
                    "situation": "informal"
                }
            ],
            "relatedTerms": ["nuoc-thai", "chat-luong-nuoc", "o-nhiem-moi-truong", "tieu-chuan-xa-thai"]
        },
        {
            "slug": "quan-trac-moi-truong",
            "korean": "환경모니터링",
            "vietnamese": "quan trắc môi trường",
            "hanja": "環境監測",
            "hanjaReading": "環(고리 환) + 境(지경 경) + 監(볼 감) + 測(잴 측)",
            "pronunciation": "꽌 짝 모이 쯔엉",
            "meaningKo": "건설 현장에서 대기, 수질, 소음, 진동 등 환경 요소를 지속적으로 측정하고 기록하는 활동. 통역 시 주의할 점은 'quan trắc'은 관측/모니터링, 'giám sát'은 감독/감시를 의미하므로 혼동하지 않아야 합니다. 실시간 모니터링은 'quan trắc thời gian thực', 자동 측정은 'đo tự động', 수동 측정은 'đo thủ công'이라고 표현합니다. 모니터링 결과는 'kết quả quan trắc', 보고서는 'báo cáo quan trắc môi trường'입니다.",
            "meaningVi": "Hoạt động đo lường và ghi nhận liên tục các yếu tố môi trường như không khí, nước, tiếng ồn, rung động tại công trường xây dựng. Quan trắc giúp phát hiện sớm các vấn đề môi trường và đảm bảo tuân thủ quy định pháp luật.",
            "context": "환경 관리, 법규 준수, 데이터 기록",
            "culturalNote": "한국은 '환경영향평가법'에 따라 일정 규모 이상의 건설 현장은 환경모니터링을 의무화하고, 대기질(PM10, PM2.5), 소음, 진동, 수질(BOD, COD, SS) 등을 실시간 측정하여 지자체에 보고합니다. 베트남도 'Luật Bảo vệ môi trường 2020'에 따라 EIA 대상 프로젝트는 모니터링이 필요하지만, 측정 장비와 전문 인력 부족으로 월 1회 또는 분기별 측정이 일반적입니다. 한국 통역사는 'IoT 센서', 'telemetry' 같은 최신 기술 용어도 익혀야 합니다.",
            "commonMistakes": [
                {
                    "mistake": "giám sát môi trường",
                    "correction": "quan trắc môi trường",
                    "explanation": "'giám sát'은 감독이고, 측정 활동은 'quan trắc'이 더 정확합니다."
                },
                {
                    "mistake": "theo dõi môi trường",
                    "correction": "quan trắc môi trường",
                    "explanation": "'theo dõi'는 일반적 추적이고, 기술 용어로는 'quan trắc'을 씁니다."
                },
                {
                    "mistake": "kiểm tra môi trường",
                    "correction": "quan trắc môi trường",
                    "explanation": "'kiểm tra'는 검사/점검이고, 지속적 모니터링은 'quan trắc'입니다."
                }
            ],
            "examples": [
                {
                    "ko": "환경모니터링 결과를 매월 관할 관청에 제출합니다.",
                    "vi": "Nộp kết quả quan trắc môi trường hàng tháng cho cơ quan quản lý.",
                    "situation": "formal"
                },
                {
                    "ko": "실시간 모니터링 시스템으로 대기질을 24시간 추적합니다.",
                    "vi": "Theo dõi chất lượng không khí 24/7 bằng hệ thống quan trắc thời gian thực.",
                    "situation": "onsite"
                },
                {
                    "ko": "분기별 환경모니터링 보고서를 작성하고 있습니다.",
                    "vi": "Đang lập báo cáo quan trắc môi trường theo quý.",
                    "situation": "formal"
                }
            ],
            "relatedTerms": ["do-luong-moi-truong", "cam-bien-iot", "bao-cao-moi-truong", "qcvn"]
        },
        {
            "slug": "giam-thieu-tac-dong",
            "korean": "영향저감",
            "vietnamese": "giảm thiểu tác động",
            "hanja": "影響低減",
            "hanjaReading": "影(그림자 영) + 響(울릴 향) + 低(낮을 저) + 減(덜 감)",
            "pronunciation": "잠 티에우 땁 동",
            "meaningKo": "건설 활동으로 인한 환경적, 사회적 부정적 영향을 줄이기 위한 조치와 활동. 통역 시 주의할 점은 'giảm thiểu'는 저감/최소화, 'tác động'은 영향을 의미하며, 긍정적 영향은 'tác động tích cực', 부정적 영향은 'tác động tiêu cực' 또는 'tác động bất lợi'로 구분합니다. 저감 대책은 'biện pháp giảm thiểu', 저감 효과는 'hiệu quả giảm thiểu'라고 표현합니다. 환경영향평가(EIA) 맥락에서 자주 사용되므로 'đánh giá tác động môi trường'과 함께 익혀야 합니다.",
            "meaningVi": "Các biện pháp và hoạt động nhằm giảm thiểu tác động tiêu cực về môi trường và xã hội từ hoạt động xây dựng. Bao gồm kiểm soát tiếng ồn, bụi, nước thải, bảo vệ cây xanh và đảm bảo an toàn giao thông xung quanh công trường.",
            "context": "환경 관리, EIA, 사회적 책임",
            "culturalNote": "한국은 환경영향평가(EIA) 제도가 체계적으로 운영되며, 평가서에 명시된 저감 대책을 이행하지 않으면 공사 중지나 과태료가 부과됩니다. 저감 대책에는 방음벽, 살수 시설, 폐수처리, 교통관리 등이 포함됩니다. 베트남도 'ĐTM(Đánh giá tác động môi trường)' 제도가 있지만, 저감 대책 이행 감독이 상대적으로 약합니다. 한국 현장에서는 저감 대책 이행 여부를 사진과 보고서로 정기적으로 증빙하며, '사후환경영향조사'로 효과를 검증합니다.",
            "commonMistakes": [
                {
                    "mistake": "giảm ảnh hưởng",
                    "correction": "giảm thiểu tác động",
                    "explanation": "'giảm ảnh hưởng'도 맞지만 'giảm thiểu tác động'이 공식 용어입니다."
                },
                {
                    "mistake": "hạ thấp tác động",
                    "correction": "giảm thiểu tác động",
                    "explanation": "'hạ thấp'은 낮추다이고, 저감은 'giảm thiểu'가 표준 용어입니다."
                },
                {
                    "mistake": "giảm impact",
                    "correction": "giảm thiểu tác động",
                    "explanation": "영어 혼용을 피하고 베트남어 'tác động'을 사용해야 합니다."
                }
            ],
            "examples": [
                {
                    "ko": "소음 영향 저감을 위해 방음벽을 3m 높이로 설치했습니다.",
                    "vi": "Lắp đặt tường cách âm cao 3m để giảm thiểu tác động tiếng ồn.",
                    "situation": "formal"
                },
                {
                    "ko": "교통 영향 저감 대책으로 공사 차량 진출입 시간을 제한합니다.",
                    "vi": "Hạn chế giờ ra vào của xe công trường như biện pháp giảm thiểu tác động giao thông.",
                    "situation": "onsite"
                },
                {
                    "ko": "환경 영향 저감 이행 상황을 분기별로 보고합니다.",
                    "vi": "Báo cáo tình hình thực hiện giảm thiểu tác động môi trường theo quý.",
                    "situation": "formal"
                }
            ],
            "relatedTerms": ["danh-gia-tac-dong-moi-truong", "bien-phap-bao-ve", "giam-sat-moi-truong"]
        },
        {
            "slug": "tuoi-nuoc-chong-bui",
            "korean": "살수",
            "vietnamese": "tưới nước chống bụi",
            "hanja": "撒水",
            "hanjaReading": "撒(뿌릴 살) + 水(물 수)",
            "pronunciation": "뛰어이 느억 총 부이",
            "meaningKo": "건설 현장에서 분진 발생을 억제하기 위해 물을 뿌리는 작업. 통역 시 주의할 점은 'tưới nước'는 물 뿌리기, 'chống bụi'는 방진을 의미하며, 함께 쓰여 '분진 억제 살수'를 나타냅니다. 살수 차량은 'xe tưới nước', 살수 설비는 'hệ thống tưới nước' 또는 'vòi phun nước'(스프링클러)라고 표현합니다. 살수 빈도는 'tần suất tưới nước', 살수량은 'lượng nước tưới'로 표현하며, 건조한 날씨나 바람 부는 날에는 횟수를 늘려야 합니다.",
            "meaningVi": "Công việc phun nước tại công trường xây dựng để kiểm soát phát sinh bụi. Tưới nước thường xuyên giúp giảm lượng bụi bay trong không khí, bảo vệ sức khỏe công nhân và người dân xung quanh.",
            "context": "환경 관리, 분진 저감, 일상 운영",
            "culturalNote": "한국 건설 현장에서는 '미세먼지 계절적 관리 강화 기간'(12월~3월)에 살수 횟수를 늘려야 하며, 대형 현장에서는 자동 살수 시스템을 설치합니다. 일반적으로 하루 3~5회 살수를 하며, 비산먼지 발생 작업 전후로 필수 실시합니다. 베트남에서는 법적 의무는 있지만 물 부족이나 비용 문제로 살수가 불규칙한 경우가 많습니다. 한국 통역사는 '비산먼지(bụi bay)' 용어도 함께 알아두어야 합니다.",
            "commonMistakes": [
                {
                    "mistake": "tưới nước",
                    "correction": "tưới nước chống bụi",
                    "explanation": "'tưới nước'만 쓰면 일반적인 물 뿌리기로 오해될 수 있으므로 목적을 명시합니다."
                },
                {
                    "mistake": "phun nước",
                    "correction": "tưới nước chống bụi",
                    "explanation": "'phun nước'는 물 분사이고, 방진 목적은 'tưới nước chống bụi'가 더 정확합니다."
                },
                {
                    "mistake": "rải nước",
                    "correction": "tưới nước",
                    "explanation": "'rải'는 흩뿌리다이고, 물은 'tưới'를 씁니다."
                }
            ],
            "examples": [
                {
                    "ko": "분진 발생이 심한 구역에는 하루 5회 이상 살수합니다.",
                    "vi": "Tưới nước ít nhất 5 lần mỗi ngày tại khu vực phát sinh bụi nhiều.",
                    "situation": "onsite"
                },
                {
                    "ko": "살수 차량을 배치하여 진입로와 작업장을 정기적으로 살수하세요.",
                    "vi": "Bố trí xe tưới nước để tưới định kỳ đường vào và khu vực thi công.",
                    "situation": "onsite"
                },
                {
                    "ko": "바람이 강한 날에는 살수 횟수를 늘려야 합니다.",
                    "vi": "Cần tăng tần suất tưới nước vào những ngày gió mạnh.",
                    "situation": "informal"
                }
            ],
            "relatedTerms": ["bui", "kiem-soat-bui", "phun-suong", "bi-san-bui"]
        },
        {
            "slug": "hang-rao-chan-bui",
            "korean": "방진막",
            "vietnamese": "hàng rào chắn bụi",
            "hanja": "防塵幕",
            "hanjaReading": "防(막을 방) + 塵(티끌 진) + 幕(휘장 막)",
            "pronunciation": "항 자오 잔 부이",
            "meaningKo": "건설 현장에서 분진이 외부로 확산되는 것을 막기 위해 설치하는 차단막. 통역 시 주의할 점은 'hàng rào'는 울타리/펜스, 'chắn'은 막다, 'bụi'는 먼지를 의미하며, 방음벽 'tường cách âm'과 구분해야 합니다. 방진망은 'lưới chắn bụi', 방진 시트는 'tấm phủ chống bụi' 또는 'bạt che bụi'로 표현합니다. 높이는 'chiều cao', 재질은 'chất liệu'(예: 강판, 메쉬 등)라고 설명합니다.",
            "meaningVi": "Tấm chắn hoặc hàng rào được lắp đặt xung quanh công trường xây dựng để ngăn bụi lan ra bên ngoài. Thường làm từ tôn, lưới hoặc bạt, có tác dụng giảm thiểu ảnh hưởng bụi đến khu vực xung quanh.",
            "context": "환경 관리, 현장 안전, 민원 예방",
            "culturalNote": "한국 건설 현장에서는 '건설기술진흥법 시행규칙'에 따라 공사용 가설울타리를 2m 이상 높이로 설치해야 하며, 분진 발생이 많은 현장에서는 밀폐형 방진막을 추가 설치합니다. 일부 대형 현장에서는 컬러강판이나 그린넷(녹색 방진망)을 사용합니다. 베트남에서도 도심지 현장에서는 방진막 설치가 의무지만, 교외 지역에서는 간단한 울타리만 설치하는 경우가 많습니다. 해체 공사 시에는 건물 전체를 방진막으로 감싸는 '전면 포장(bao phủ toàn bộ)'도 시행됩니다.",
            "commonMistakes": [
                {
                    "mistake": "tường chắn bụi",
                    "correction": "hàng rào chắn bụi",
                    "explanation": "'tường'은 벽이고, 임시 울타리는 'hàng rào'가 더 적합합니다."
                },
                {
                    "mistake": "màn chắn bụi",
                    "correction": "hàng rào chắn bụi / lưới chắn bụi",
                    "explanation": "'màn'은 커튼이고, 건설용은 'hàng rào' 또는 'lưới'가 정확합니다."
                },
                {
                    "mistake": "rào cản bụi",
                    "correction": "hàng rào chắn bụi",
                    "explanation": "'rào cản'은 장애물이고, 방진막은 'hàng rào chắn bụi'입니다."
                }
            ],
            "examples": [
                {
                    "ko": "현장 경계에 높이 3m의 방진막을 설치하여 분진 확산을 차단합니다.",
                    "vi": "Lắp đặt hàng rào chắn bụi cao 3m ở ranh giới công trường để ngăn bụi lan ra.",
                    "situation": "formal"
                },
                {
                    "ko": "해체 공사 중에는 건물 전체를 방진막으로 감싸야 합니다.",
                    "vi": "Trong quá trình phá dỡ phải bao phủ toàn bộ tòa nhà bằng lưới chắn bụi.",
                    "situation": "onsite"
                },
                {
                    "ko": "태풍 대비해서 방진막 고정 상태를 점검하세요.",
                    "vi": "Kiểm tra tình trạng cố định hàng rào chắn bụi để chuẩn bị cho bão.",
                    "situation": "informal"
                }
            ],
            "relatedTerms": ["bui", "hang-rao-cong-truong", "luoi-xanh", "tam-phu"]
        },
        {
            "slug": "gio-lam-viec-han-che",
            "korean": "작업시간제한",
            "vietnamese": "giờ làm việc hạn chế",
            "hanja": "作業時間制限",
            "hanjaReading": "作(지을 작) + 業(업 업) + 時(때 시) + 間(사이 간) + 制(절제할 제) + 限(한할 한)",
            "pronunciation": "저 람 비엑 한 쩨",
            "meaningKo": "소음, 진동 등 주변 환경에 영향을 주는 작업의 시간을 제한하는 규제. 통역 시 주의할 점은 'giờ làm việc'은 작업 시간, 'hạn chế'는 제한을 의미하며, 'giờ làm việc cho phép'(허용 작업 시간), 'giờ cấm thi công'(공사 금지 시간)과 구분해야 합니다. 야간 작업은 'làm việc ban đêm', 주말 작업은 'làm việc cuối tuần', 공휴일은 'ngày lễ'라고 표현합니다. 작업 시간 연장 시 'gia hạn giờ làm việc' 또는 'xin phép làm việc ngoài giờ'라고 합니다.",
            "meaningVi": "Quy định hạn chế thời gian làm việc đối với các công việc gây ảnh hưởng đến môi trường xung quanh như tiếng ồn, rung động. Thông thường cấm thi công vào ban đêm, sáng sớm và ngày lễ để bảo đảm yên tĩnh cho khu dân cư.",
            "context": "민원 예방, 법규 준수, 공정 관리",
            "culturalNote": "한국은 '소음진동관리법'과 지자체 조례로 주거 지역 인근 공사 시간을 제한하며, 일반적으로 평일 오전 8시~오후 6시만 소음 발생 작업이 가능하고 야간(오후 10시~오전 6시)과 주말/공휴일 작업은 사전 허가가 필요합니다. 베트남도 'Nghị định 40/2019/NĐ-CP'로 야간 작업(22시~06시)을 규제하지만, 집행이 덜 엄격하여 공기 단축을 위해 야간 작업이 빈번합니다. 한국 통역사는 '소음 작업 시간 연장 허가(giấy phép gia hạn giờ thi công)' 절차도 숙지해야 합니다.",
            "commonMistakes": [
                {
                    "mistake": "thời gian làm việc giới hạn",
                    "correction": "giờ làm việc hạn chế",
                    "explanation": "'giới hạn'과 'hạn chế'는 유사하지만 'hạn chế'가 더 자연스럽습니다."
                },
                {
                    "mistake": "giờ làm việc bị cấm",
                    "correction": "giờ làm việc hạn chế / giờ cấm thi công",
                    "explanation": "완전 금지는 'giờ cấm'이고, 제한은 'hạn chế'입니다."
                },
                {
                    "mistake": "giờ cấm làm việc",
                    "correction": "giờ làm việc hạn chế",
                    "explanation": "제한과 금지는 다르므로 정확한 용어를 사용해야 합니다."
                }
            ],
            "examples": [
                {
                    "ko": "주거 지역 인근에서는 평일 오전 8시부터 오후 6시까지만 작업 가능합니다.",
                    "vi": "Gần khu dân cư chỉ được làm việc từ 8 giờ sáng đến 6 giờ chiều các ngày trong tuần.",
                    "situation": "formal"
                },
                {
                    "ko": "야간 작업이 필요하면 관할 관청에 사전 허가를 받아야 합니다.",
                    "vi": "Nếu cần làm việc ban đêm phải xin phép trước từ cơ quan quản lý.",
                    "situation": "onsite"
                },
                {
                    "ko": "주말과 공휴일에는 소음 발생 작업을 하지 마세요.",
                    "vi": "Không thực hiện công việc gây tiếng ồn vào cuối tuần và ngày lễ.",
                    "situation": "informal"
                }
            ],
            "relatedTerms": ["khieu-nai", "tieng-on", "phep-thi-cong", "lam-viec-ban-dem"]
        }
    ]

    # 5. 중복 제거 (existing_slugs에 없는 것만)
    new_terms_filtered = [t for t in new_terms if t['slug'] not in existing_slugs]

    # 6. 데이터 추가
    data.extend(new_terms_filtered)

    # 7. 파일 저장
    with open(file_path, 'w', encoding='utf-8') as f:
        json.dump(data, f, ensure_ascii=False, indent=2)

    print(f"✅ 성공: {len(new_terms_filtered)}개 용어 추가 완료")
    print(f"📋 추가된 용어: {[t['slug'] for t in new_terms_filtered]}")
    print(f"🔄 중복 제외: {len(new_terms) - len(new_terms_filtered)}개")
    print(f"📊 총 용어 수: {len(data)}개")

if __name__ == '__main__':
    main()
