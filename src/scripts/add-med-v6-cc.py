#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
의료 용어 추가 스크립트 v6 - 간호/환자관리
Tier S 품질 기준 준수 (90점 이상)
"""

import json
import os

# 파일 경로 설정
file_path = os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', 'data', 'terms', 'medical.json')

# 추가할 용어 데이터
new_terms = [
    {
        "slug": "y-ta-dieu-duong",
        "korean": "간호사",
        "vietnamese": "Y tá / Điều dưỡng",
        "hanja": "看護士",
        "hanjaReading": "看(볼 간) + 護(지킬 호) + 士(선비 사)",
        "pronunciation": "이 타 / 지에우 즈엉",
        "meaningKo": "환자의 건강 회복과 유지를 위해 의료 행위를 보조하고 직접 간호를 제공하는 의료 전문가. 통역 시 주의: 베트남에서는 'Y tá'가 일반적이지만 'Điều dưỡng'이 공식 명칭이며, 한국의 간호사 자격 체계(간호조무사/간호사/전문간호사)와 베트남의 체계(Hộ lý/Y tá/Điều dưỡng viên)가 다르므로 자격 수준을 명확히 구분해야 함. 베트남 의료기관에서는 Y tá가 한국보다 더 폭넓은 의료 행위를 수행할 수 있어 업무 범위 설명 시 주의 필요.",
        "meaningVi": "Chuyên gia y tế chuyên nghiệp hỗ trợ các hành vi y tế và cung cấp dịch vụ chăm sóc trực tiếp cho bệnh nhân để phục hồi và duy trì sức khỏe. Y tá/Điều dưỡng đảm nhận vai trò quan trọng trong việc theo dõi tình trạng bệnh nhân, thực hiện các thủ thuật y tế cơ bản, và phối hợp với bác sĩ.",
        "context": "의료기관, 간호사실, 환자 돌봄 현장, 자격증 관련 대화",
        "culturalNote": "한국의 간호사는 4년제 대학 졸업 후 국가시험을 통과해야 하며, 간호조무사와 명확히 구분됨. 베트남에서는 Hộ lý(간호조무사급), Y tá(일반 간호사급), Điều dưỡng viên(전문 간호사급)으로 세분화되며, 교육 기간과 업무 범위가 다름. 베트님에서는 가족이 병원에서 환자를 직접 돌보는 문화가 강해 간호사의 역할이 한국과 다소 차이가 있음. 통역 시 자격 수준을 정확히 전달해야 함.",
        "commonMistakes": [
            {
                "mistake": "간호사를 'Y sĩ'로 번역",
                "correction": "'Y tá' 또는 'Điều dưỡng' 사용",
                "explanation": "Y sĩ는 '의사'를 의미하므로 완전히 다른 직종임"
            },
            {
                "mistake": "간호조무사와 간호사를 동일하게 'Y tá'로 번역",
                "correction": "간호조무사는 'Hộ lý', 간호사는 'Y tá' 또는 'Điều dưỡng'",
                "explanation": "자격과 업무 범위가 다르므로 명확히 구분 필요"
            },
            {
                "mistake": "'Điều dưỡng'을 간병인으로 오해",
                "correction": "간병인은 'Người chăm sóc bệnh nhân', 간호사는 'Điều dưỡng'",
                "explanation": "간호사는 의료 전문 자격증 소지자이며 간병인과 다름"
            }
        ],
        "examples": [
            {
                "ko": "담당 간호사가 2시간마다 활력징후를 체크합니다.",
                "vi": "Y tá phụ trách sẽ kiểm tra dấu hiệu sinh tồn mỗi 2 giờ.",
                "situation": "formal"
            },
            {
                "ko": "수술 후 간호사 호출 버튼을 누르시면 즉시 도와드립니다.",
                "vi": "Sau phẫu thuật, nhấn nút gọi y tá thì sẽ được hỗ trợ ngay lập tức.",
                "situation": "onsite"
            },
            {
                "ko": "전문간호사가 상처 치료를 담당합니다.",
                "vi": "Điều dưỡng chuyên khoa sẽ phụ trách điều trị vết thương.",
                "situation": "formal"
            }
        ],
        "relatedTerms": ["의사", "간호조무사", "환자", "병동", "활력징후"]
    },
    {
        "slug": "vong-deo-an-toan-benh-nhan",
        "korean": "환자안전밴드",
        "vietnamese": "Vòng đeo an toàn bệnh nhân",
        "hanja": "患者安全band",
        "hanjaReading": "患(근심 환) + 者(놈 자) + 安(편안 안) + 全(온전 전)",
        "pronunciation": "봉 제오 안 토안 벵 년",
        "meaningKo": "환자의 신원 확인과 안전을 위해 손목이나 발목에 착용하는 식별 밴드. 환자의 이름, 등록번호, 생년월일, 알레르기 정보 등이 기재됨. 통역 시 주의: 한국 의료기관에서는 환자안전을 위해 필수적으로 착용하지만, 베트남의 일부 병원에서는 아직 보편화되지 않았을 수 있어 그 목적과 중요성을 설명해야 함. 특히 수술, 투약, 수혈 전 환자 확인 절차에서 핵심 역할을 하므로 '반드시 착용해야 한다'는 점을 강조 필요.",
        "meaningVi": "Vòng đeo nhận dạng đeo tay hoặc chân để xác minh danh tính và đảm bảo an toàn cho bệnh nhân. Thông tin ghi trên vòng bao gồm tên, số đăng ký, ngày sinh, thông tin dị ứng. Đây là biện pháp quan trọng để phòng ngừa sai sót y tế.",
        "context": "입원 수속, 수술 전 준비, 환자 식별 절차",
        "culturalNote": "한국 의료기관에서는 2004년부터 환자안전법에 따라 모든 입원 환자에게 환자안전밴드 착용이 의무화되어 있으며, 색상으로 알레르기(빨강), 낙상위험(노랑), DNR(보라) 등을 구분함. 베트남에서는 대형 병원에서는 점차 도입되고 있으나 중소 병원에서는 아직 보편화되지 않았음. 환자나 보호자가 '감시받는 느낌'으로 거부감을 보일 수 있으므로 안전 목적임을 충분히 설명해야 함.",
        "commonMistakes": [
            {
                "mistake": "환자안전밴드를 'Vòng tay bệnh nhân'으로만 번역",
                "correction": "'Vòng đeo an toàn bệnh nhân' 또는 'Vòng nhận dạng bệnh nhân'",
                "explanation": "단순 팔찌가 아니라 안전 확인 목적의 의료 도구임을 명시해야 함"
            },
            {
                "mistake": "착용 거부 시 강제 설명 없이 진행",
                "correction": "환자안전을 위한 필수 절차임을 설명하고 동의 구함",
                "explanation": "문화적 차이로 거부감이 있을 수 있으므로 목적 설명 필요"
            },
            {
                "mistake": "색상 코드 설명 없이 밴드만 채움",
                "correction": "색상별 의미(알레르기, 낙상위험 등)를 함께 설명",
                "explanation": "색상이 중요한 안전 정보를 담고 있음"
            }
        ],
        "examples": [
            {
                "ko": "입원 시 환자안전밴드를 착용하셔야 합니다. 이름과 생년월일을 확인해주세요.",
                "vi": "Khi nhập viện, bạn phải đeo vòng an toàn bệnh nhân. Vui lòng xác nhận tên và ngày sinh.",
                "situation": "formal"
            },
            {
                "ko": "빨간색 밴드는 알레르기가 있다는 표시입니다. 절대 떼지 마세요.",
                "vi": "Vòng màu đỏ biểu thị có dị ứng. Tuyệt đối không được tháo ra.",
                "situation": "onsite"
            },
            {
                "ko": "수술 전 환자안전밴드로 본인 확인 절차를 진행하겠습니다.",
                "vi": "Trước phẫu thuật, chúng tôi sẽ tiến hành xác minh danh tính qua vòng đeo an toàn bệnh nhân.",
                "situation": "formal"
            }
        ],
        "relatedTerms": ["환자식별", "환자안전", "알레르기", "낙상위험", "바코드"]
    },
    {
        "slug": "phong-chong-nga",
        "korean": "낙상방지",
        "vietnamese": "Phòng chống ngã",
        "hanja": "落傷防止",
        "hanjaReading": "落(떨어질 락) + 傷(다칠 상) + 防(막을 방) + 止(그칠 지)",
        "pronunciation": "퐁 쫑 응아",
        "meaningKo": "환자가 넘어져 다치는 사고를 예방하기 위한 모든 조치와 활동. 침상 난간 설치, 미끄럼방지 양말 착용, 보행 보조, 화장실 안전바 설치 등이 포함됨. 통역 시 주의: 한국 병원에서는 낙상이 주요 환자안전 지표로 관리되며, 낙상위험 환자에게는 노란색 안전밴드를 착용시키고 집중 관리함. 베트남어로는 'Phòng té ngã' 또는 'Phòng chống ngã' 모두 사용 가능하나, 의료 현장에서는 'Phòng chống ngã'가 더 공식적. 고령 환자나 어지럼증 환자에게 특히 중요하므로 보호자 교육 시 강조 필요.",
        "meaningVi": "Tất cả các biện pháp và hoạt động nhằm phòng ngừa tai nạn té ngã gây thương tích cho bệnh nhân. Bao gồm lắp đặt lan can giường, đeo tất chống trượt, hỗ trợ di chuyển, lắp thanh vịn trong nhà vệ sinh. Đây là chỉ số an toàn bệnh nhân quan trọng trong bệnh viện.",
        "context": "노인 환자 관리, 수술 후 보행, 어지럼증 환자, 안전 교육",
        "culturalNote": "한국 의료기관에서는 낙상예방이 환자안전의 핵심 지표로, 낙상 발생 시 사고보고서 작성이 의무화되어 있음. 낙상위험 환자는 노란색 안전밴드를 착용하고, 병실 입구에 낙상주의 표지를 부착함. 베트남 의료기관에서는 낙상예방 시스템이 한국만큼 체계화되지 않은 경우가 많으며, 가족이 24시간 병실에 상주하며 환자를 직접 돌보는 문화 때문에 낙상예방 책임이 가족에게 더 많이 부여되는 경향이 있음.",
        "commonMistakes": [
            {
                "mistake": "낙상방지를 'Không té'로 번역",
                "correction": "'Phòng chống ngã' 또는 'Phòng ngừa té ngã'",
                "explanation": "'Không té'는 명령문이며, 의료 용어로는 'Phòng chống'이 적절"
            },
            {
                "mistake": "낙상 위험 환자를 'Bệnh nhân nguy hiểm'으로 번역",
                "correction": "'Bệnh nhân có nguy cơ té ngã cao'",
                "explanation": "'Nguy hiểm'은 '위험한 환자'로 오해될 수 있음"
            },
            {
                "mistake": "보호자에게만 책임을 전가하는 설명",
                "correction": "병원의 낙상방지 시스템과 보호자 협조 사항을 균형있게 설명",
                "explanation": "한국 병원에서는 병원의 시스템적 책임이 더 크다는 점 명시"
            }
        ],
        "examples": [
            {
                "ko": "어지럼증이 있으시므로 낙상방지를 위해 혼자 화장실에 가지 마시고 간호사를 호출하세요.",
                "vi": "Vì bạn bị chóng mặt, để phòng chống ngã, đừng tự đi vệ sinh mà hãy gọi y tá.",
                "situation": "onsite"
            },
            {
                "ko": "낙상방지 양말을 착용하시고 침상 난간을 올려두겠습니다.",
                "vi": "Vui lòng đeo tất chống trượt và tôi sẽ kéo lan can giường lên.",
                "situation": "onsite"
            },
            {
                "ko": "노란색 안전밴드는 낙상위험이 높다는 표시이므로 보행 시 반드시 보호자나 간호사가 동행해야 합니다.",
                "vi": "Vòng đeo màu vàng biểu thị nguy cơ té ngã cao, nên khi đi lại nhất định phải có người thân hoặc y tá đi cùng.",
                "situation": "formal"
            }
        ],
        "relatedTerms": ["환자안전", "침상난간", "보행보조기", "안전손잡이", "낙상위험평가"]
    },
    {
        "slug": "dau-hieu-sinh-ton",
        "korean": "활력징후",
        "vietnamese": "Dấu hiệu sinh tồn",
        "hanja": "活力徵候",
        "hanjaReading": "活(살 활) + 力(힘 력) + 徵(징조 징) + 候(기후 후)",
        "pronunciation": "저우 히에우 신 턴",
        "meaningKo": "환자의 생명 유지와 직결되는 기본적인 신체 지표로, 혈압, 맥박, 호흡, 체온을 포함하며 최근에는 산소포화도도 추가됨. 의료진이 환자 상태를 판단하는 가장 기본적인 지표. 통역 시 주의: 'Vital Signs'를 직역하여 'Dấu hiệu sống' 또는 'Sinh hiệu'로 쓰기도 하나, 의료 현장에서는 'Dấu hiệu sinh tồn'이 표준 용어임. 각 수치의 정상 범위가 연령과 상태에 따라 다르므로, 수치 전달 시 정상/비정상 여부를 함께 설명하는 것이 중요. 한국에서는 V/S로 약칭하나 베트남 환자에게는 전체 용어 사용 권장.",
        "meaningVi": "Các chỉ số cơ thể cơ bản liên quan trực tiếp đến duy trì sự sống của bệnh nhân, bao gồm huyết áp, mạch, nhịp thở, thân nhiệt, và gần đây còn bổ sung độ bão hòa oxy. Đây là chỉ số cơ bản nhất để nhân viên y tế đánh giá tình trạng bệnh nhân.",
        "context": "회진, 간호 기록, 응급실, 수술 전후 모니터링",
        "culturalNote": "한국 의료기관에서는 활력징후를 정기적으로 측정하고 차트에 기록하는 것이 표준 간호 절차이며, 중환자는 자동 모니터로 실시간 감시함. 베트남 의료기관에서는 병원 등급에 따라 활력징후 측정 빈도와 정확도에 차이가 있을 수 있음. 한국에서는 '바이탈'이라는 영어식 표현도 흔히 쓰이나, 베트남어 통역 시에는 정확한 의료 용어를 사용하는 것이 신뢰도를 높임.",
        "commonMistakes": [
            {
                "mistake": "활력징후를 'Dấu hiệu sống'으로만 번역",
                "correction": "'Dấu hiệu sinh tồn' 사용",
                "explanation": "'Dấu hiệu sinh tồn'이 의료 현장의 표준 용어"
            },
            {
                "mistake": "V/S를 그대로 'V/S'로 읽어줌",
                "correction": "'Dấu hiệu sinh tồn' 또는 각 항목을 구체적으로 설명",
                "explanation": "약어는 환자가 이해하지 못할 수 있음"
            },
            {
                "mistake": "수치만 전달하고 정상/비정상 설명 없음",
                "correction": "수치와 함께 '정상 범위입니다' 또는 '높습니다' 등의 평가 포함",
                "explanation": "환자는 수치만으로는 상태를 이해하기 어려움"
            }
        ],
        "examples": [
            {
                "ko": "지금부터 활력징후를 측정하겠습니다. 혈압, 맥박, 체온, 호흡을 체크합니다.",
                "vi": "Bây giờ tôi sẽ đo dấu hiệu sinh tồn. Kiểm tra huyết áp, mạch, thân nhiệt, nhịp thở.",
                "situation": "onsite"
            },
            {
                "ko": "활력징후가 안정적입니다. 혈압 120/80, 맥박 72, 체온 36.5도입니다.",
                "vi": "Dấu hiệu sinh tồn ổn định. Huyết áp 120/80, mạch 72, nhiệt độ 36.5 độ.",
                "situation": "formal"
            },
            {
                "ko": "2시간마다 활력징후 체크가 필요하므로 깨워드릴 수 있습니다.",
                "vi": "Cần kiểm tra dấu hiệu sinh tồn mỗi 2 giờ nên có thể đánh thức bạn.",
                "situation": "onsite"
            }
        ],
        "relatedTerms": ["혈압", "맥박", "체온", "호흡", "산소포화도"]
    },
    {
        "slug": "tiem-tinh-mach",
        "korean": "정맥주사",
        "vietnamese": "Tiêm tĩnh mạch",
        "hanja": "靜脈注射",
        "hanjaReading": "靜(고요할 정) + 脈(맥 맥) + 注(부을 주) + 射(쏠 사)",
        "pronunciation": "띠엠 띤 맥",
        "meaningKo": "약물이나 수액을 정맥혈관에 직접 주입하는 의료 행위. 근육주사나 피하주사에 비해 약효가 빠르고 확실하며, 대량의 수액 투여가 가능함. 통역 시 주의: 한국에서는 '링거', 'IV'라는 구어적 표현도 많이 쓰이나, 베트남어로는 'Tiêm tĩnh mạch' 또는 'Truyền tĩnh mạch'이 정확함. 'Tiêm'은 주사를 찌르는 행위, 'Truyền'은 수액을 지속적으로 주입하는 것을 의미하므로 상황에 따라 구분 필요. 부작용으로 혈관통증, 부종, 정맥염 등이 있을 수 있음을 사전 설명하면 환자 불안 감소.",
        "meaningVi": "Hành vi y tế truyền thuốc hoặc dung dịch trực tiếp vào tĩnh mạch. So với tiêm bắp hay tiêm dưới da, tiêm tĩnh mạch có hiệu quả nhanh và chắc chắn hơn, có thể truyền lượng lớn dịch truyền.",
        "context": "응급실, 수술실, 입원 병동, 수액 치료",
        "culturalNote": "한국 의료기관에서는 정맥주사(IV) 투여가 매우 일반적이며, 외래에서도 '링거 맞기'를 흔히 시행함. 베트남에서도 정맥주사는 보편적이나 'Truyền dịch'(수액 투여)라는 표현을 더 자주 사용함. 한국에서는 간호사가 정맥주사를 시행하지만 베트남에서는 Y tá 외에 Hộ lý도 시행할 수 있어 자격 확인이 중요할 수 있음. 일부 베트남 환자는 '링거를 너무 자주 맞으면 안 좋다'는 민간 믿음이 있어 설명 필요.",
        "commonMistakes": [
            {
                "mistake": "정맥주사를 'Tiêm kim'으로 번역",
                "correction": "'Tiêm tĩnh mạch' 또는 'Truyền tĩnh mạch'",
                "explanation": "'Tiêm kim'은 단순히 '주사 바늘'이며 투여 방법을 나타내지 않음"
            },
            {
                "mistake": "링거를 'Ringer'로 그대로 사용",
                "correction": "'Dịch truyền' 또는 'Truyền tĩnh mạch'",
                "explanation": "Ringer는 링거액의 종류이며, 일반적으로는 'Dịch truyền' 사용"
            },
            {
                "mistake": "'Tiêm'과 'Truyền' 구분 없이 사용",
                "correction": "일회 주사는 'Tiêm', 지속 투여는 'Truyền'",
                "explanation": "투여 방식에 따라 용어가 다름"
            }
        ],
        "examples": [
            {
                "ko": "지금부터 정맥주사로 항생제를 투여하겠습니다. 손등에 바늘을 찌를 겁니다.",
                "vi": "Bây giờ sẽ tiêm kháng sinh qua tĩnh mạch. Tôi sẽ đâm kim vào mu bàn tay.",
                "situation": "onsite"
            },
            {
                "ko": "탈수 증상이 있어서 정맥주사로 수액을 보충해야 합니다.",
                "vi": "Vì có triệu chứng mất nước nên cần bổ sung dịch qua truyền tĩnh mạch.",
                "situation": "formal"
            },
            {
                "ko": "정맥주사 부위가 붓거나 아프면 즉시 알려주세요.",
                "vi": "Nếu vị trí tiêm tĩnh mạch sưng hoặc đau, hãy báo ngay lập tức.",
                "situation": "onsite"
            }
        ],
        "relatedTerms": ["수액", "링거", "정맥", "주사바늘", "혈관확보"]
    },
    {
        "slug": "dat-ong-thong",
        "korean": "카테터삽입",
        "vietnamese": "Đặt ống thông",
        "hanja": "catheter揷入",
        "hanjaReading": "揷(꽂을 삽) + 入(들 입)",
        "pronunciation": "닷 옹 통",
        "meaningKo": "진단이나 치료 목적으로 신체의 관이나 공간에 가늘고 긴 관(카테터)을 삽입하는 의료 행위. 소변 배출을 위한 도뇨관(요도 카테터), 혈관 내 약물 투여를 위한 중심정맥관, 심장 검사를 위한 심장 카테터 등 다양한 종류가 있음. 통역 시 주의: 'Catheter'를 그대로 '까떼떼르'로 읽지 말고 'Ống thông'으로 번역. 삽입 부위와 목적에 따라 'Ống thông tiểu'(도뇨관), 'Ống thông tĩnh mạch trung tâm'(중심정맥관) 등으로 구체화 필요. 특히 도뇨관 삽입은 환자에게 수치심을 줄 수 있으므로 사전 설명과 동의가 중요.",
        "meaningVi": "Hành vi y tế đưa ống mềm, dài (catheter/ống thông) vào các ống hoặc khoảng trong cơ thể nhằm mục đích chẩn đoán hoặc điều trị. Có nhiều loại như ống thông tiểu để dẫn nước tiểu, ống thông tĩnh mạch trung tâm để truyền thuốc, ống thông tim để kiểm tra tim.",
        "context": "수술 전 준비, 중환자 치료, 배뇨 장애 환자, 심혈관 검사",
        "culturalNote": "한국 의료기관에서는 카테터 삽입이 표준 치료 프로토콜에 포함되어 있으며, 수술 전 도뇨관 삽입이 일반적임. 베트남에서도 유사하나, 환자와 보호자가 카테터 삽입에 대해 거부감이나 수치심을 느낄 수 있어 사전 충분한 설명과 동의 절차가 중요함. 특히 여성 환자의 경우 문화적으로 더 민감할 수 있으므로, 여성 간호사가 시행하거나 보호자 동석 여부를 확인하는 것이 좋음.",
        "commonMistakes": [
            {
                "mistake": "카테터를 'Catheter'로 그대로 읽어줌",
                "correction": "'Ống thông' 사용",
                "explanation": "영어 발음은 환자가 이해하기 어려움"
            },
            {
                "mistake": "도뇨관을 '소변줄'로만 번역",
                "correction": "'Ống thông tiểu' 또는 'Ống thông bàng quang'",
                "explanation": "의료 용어로 정확히 전달하는 것이 전문성을 높임"
            },
            {
                "mistake": "삽입 전 동의 절차 없이 진행 통역",
                "correction": "환자에게 목적과 필요성을 설명하고 동의 구하는 과정 포함",
                "explanation": "문화적으로 민감한 부분이므로 충분한 설명 필요"
            }
        ],
        "examples": [
            {
                "ko": "수술 중 소변 배출을 위해 도뇨관을 삽입하겠습니다. 마취 후 시행하므로 통증은 없습니다.",
                "vi": "Sẽ đặt ống thông tiểu để dẫn nước tiểu trong khi phẫu thuật. Thực hiện sau gây mê nên không đau.",
                "situation": "formal"
            },
            {
                "ko": "중심정맥 카테터를 목 부위에 삽입하여 장기간 약물 투여를 할 예정입니다.",
                "vi": "Sẽ đặt ống thông tĩnh mạch trung tâm ở vùng cổ để truyền thuốc dài hạn.",
                "situation": "formal"
            },
            {
                "ko": "카테터 삽입 부위는 감염 위험이 있으므로 청결하게 관리해야 합니다.",
                "vi": "Vị trí đặt ống thông có nguy cơ nhiễm trùng nên phải giữ sạch sẽ.",
                "situation": "onsite"
            }
        ],
        "relatedTerms": ["도뇨관", "중심정맥관", "카테터", "방광", "감염관리"]
    },
    {
        "slug": "sat-trung-vet-thuong",
        "korean": "상처소독",
        "vietnamese": "Sát trùng vết thương",
        "hanja": "傷處消毒",
        "hanjaReading": "傷(다칠 상) + 處(곳 처) + 消(사라질 소) + 毒(독 독)",
        "pronunciation": "샛 쭝 벳 투엉",
        "meaningKo": "상처 부위의 세균이나 미생물을 제거하여 감염을 예방하고 치유를 촉진하기 위한 처치. 생리식염수로 세척 후 소독제(포비돈, 알코올 등)를 바르고 필요 시 드레싱함. 통역 시 주의: 'Sát trùng'은 소독, 'Rửa vết thương'은 세척을 의미하므로 구분 필요. 한국 의료기관에서는 소독-세척-소독-드레싱의 순서로 진행하며, 베트남에서도 유사하나 소독제의 종류가 다를 수 있음. 환자에게 '약간 따끔거릴 수 있다'는 사전 안내로 긴장 완화. 당뇨 환자나 면역저하 환자는 감염 위험이 높으므로 더 철저한 소독 필요성 설명.",
        "meaningVi": "Xử lý loại bỏ vi khuẩn và vi sinh vật ở vùng vết thương để phòng ngừa nhiễm trùng và thúc đẩy quá trình lành vết thương. Rửa sạch bằng nước muối sinh lý, sau đó bôi thuốc sát trùng (povidone, cồn) và băng bó nếu cần.",
        "context": "응급실, 외과, 상처 드레싱, 수술 후 관리",
        "culturalNote": "한국 의료기관에서는 상처 소독 시 일회용 소독 키트를 사용하며, 무균술을 엄격히 준수함. 베트남에서도 대형 병원은 유사하나 중소 병원에서는 소독 방법과 재료에 차이가 있을 수 있음. 한국에서는 '빨간약(포비돈)'이 흔히 쓰이나 베트남에서는 다른 소독제를 선호할 수 있어, 소독제 종류 설명 시 주의 필요. 일부 환자는 민간요법(꿀, 알로에 등)을 선호하는 경우가 있으므로 의료적 소독의 중요성 강조.",
        "commonMistakes": [
            {
                "mistake": "소독과 세척을 구분하지 않고 'Rửa'로만 번역",
                "correction": "세척은 'Rửa', 소독은 'Sát trùng'으로 구분",
                "explanation": "세척과 소독은 다른 단계의 처치임"
            },
            {
                "mistake": "'Khử trùng'과 'Sát trùng'을 혼용",
                "correction": "의료 현장에서는 'Sát trùng' 사용",
                "explanation": "'Khử trùng'은 일반적 살균, 'Sát trùng'은 의료적 소독"
            },
            {
                "mistake": "소독제 이름을 한국어 그대로 전달",
                "correction": "성분명이나 베트남어 명칭 사용 (예: Povidone-iodine)",
                "explanation": "브랜드명은 나라마다 다를 수 있음"
            }
        ],
        "examples": [
            {
                "ko": "지금부터 상처를 소독하겠습니다. 약간 따끔거릴 수 있습니다.",
                "vi": "Bây giờ tôi sẽ sát trùng vết thương. Có thể hơi đau nhói.",
                "situation": "onsite"
            },
            {
                "ko": "하루 2회 상처 소독이 필요하므로 아침 저녁으로 오세요.",
                "vi": "Cần sát trùng vết thương 2 lần mỗi ngày nên hãy đến vào buổi sáng và tối.",
                "situation": "formal"
            },
            {
                "ko": "집에서 소독할 때는 반드시 손을 씻고 일회용 거즈를 사용하세요.",
                "vi": "Khi sát trùng ở nhà, nhất định phải rửa tay và dùng gạc dùng một lần.",
                "situation": "onsite"
            }
        ],
        "relatedTerms": ["소독제", "드레싱", "거즈", "반창고", "감염예방"]
    },
    {
        "slug": "khau-vet-thuong",
        "korean": "봉합술",
        "vietnamese": "Khâu vết thương",
        "hanja": "縫合術",
        "hanjaReading": "縫(꿰맬 봉) + 合(합할 합) + 術(재주 술)",
        "pronunciation": "커우 벳 투엉",
        "meaningKo": "피부나 조직이 찢어지거나 절개된 상처의 가장자리를 실이나 스테이플러로 붙여 치유를 촉진하는 외과적 처치. 봉합 방법은 일반 봉합, 피하 봉합, 연속 봉합 등이 있으며, 봉합사의 종류에 따라 녹는 실(흡수성)과 안 녹는 실(비흡수성)로 구분됨. 통역 시 주의: 베트남어로 'Khâu'는 일반적인 '바느질'도 의미하므로 'Khâu vết thương' 또는 'Khâu phẫu thuật'로 명확히 해야 함. 봉합 후 실밥 제거(Tháo chỉ) 시기를 반드시 안내하고, 흉터 관리에 대한 환자의 관심이 높으므로 흉터 최소화 방법도 함께 설명하면 좋음.",
        "meaningVi": "Thủ thuật ngoại khoa khâu nối các mép vết thương da hoặc mô bị rách hoặc rạch bằng chỉ hoặc dụng cụ khâu để thúc đẩy quá trình lành. Có nhiều phương pháp khâu và loại chỉ khác nhau như chỉ tiêu (hấp thụ) và chỉ không tiêu (không hấp thụ).",
        "context": "응급실, 외과, 수술실, 외상 치료",
        "culturalNote": "한국 의료기관에서는 봉합 전 국소마취를 충분히 시행하며, 미용 봉합(성형 봉합)에 대한 관심이 높아 얼굴 부위는 성형외과 의뢰도 흔함. 베트남에서도 봉합술은 일반적이나, 마취 정도나 봉합 방법이 병원에 따라 차이가 있을 수 있음. 한국 환자들은 '실밥 제거'에 대한 이해도가 높으나, 베트남 환자 중 일부는 녹는 실의 개념을 모를 수 있어 설명 필요. 흉터에 대한 문화적 인식도 다를 수 있어, 흉터 관리 방법 안내가 중요함.",
        "commonMistakes": [
            {
                "mistake": "봉합을 'May vết thương'으로 번역",
                "correction": "'Khâu vết thương' 사용",
                "explanation": "'May'는 옷을 '재봉'하는 것이며, 의료에서는 'Khâu' 사용"
            },
            {
                "mistake": "녹는 실을 'Chỉ tan'으로 번역",
                "correction": "'Chỉ tiêu' 또는 'Chỉ tự hấp thụ'",
                "explanation": "'Chỉ tiêu'가 의료 용어로 정확함"
            },
            {
                "mistake": "실밥 제거 시기를 말하지 않음",
                "correction": "봉합 시 반드시 '~일 후 실밥 제거' 안내 포함",
                "explanation": "환자가 재방문 시기를 알아야 함"
            }
        ],
        "examples": [
            {
                "ko": "상처가 깊어서 봉합이 필요합니다. 국소마취 후 5바늘 정도 꿰맬 예정입니다.",
                "vi": "Vết thương sâu nên cần khâu. Sau gây tê cục bộ, dự kiến khâu khoảng 5 mũi.",
                "situation": "formal"
            },
            {
                "ko": "녹는 실로 봉합했으므로 실밥 제거는 필요 없습니다. 2주 후 자연히 녹습니다.",
                "vi": "Đã khâu bằng chỉ tiêu nên không cần tháo chỉ. Sau 2 tuần sẽ tự tan.",
                "situation": "onsite"
            },
            {
                "ko": "7일 후 실밥을 제거하러 오셔야 합니다. 그 전까지 물에 닿지 않게 주의하세요.",
                "vi": "Sau 7 ngày phải đến tháo chỉ. Đến lúc đó cẩn thận không để vết thương dính nước.",
                "situation": "onsite"
            }
        ],
        "relatedTerms": ["봉합사", "실밥제거", "피부봉합", "스테이플러", "국소마취"]
    },
    {
        "slug": "ong-dan-luu",
        "korean": "배액관",
        "vietnamese": "Ống dẫn lưu",
        "hanja": "排液管",
        "hanjaReading": "排(배열 배) + 液(진 액) + 管(대롱 관)",
        "pronunciation": "옹 젠 르우",
        "meaningKo": "수술 부위나 감염 부위에서 고름, 피, 삼출액 등의 체액을 체외로 배출하기 위해 삽입하는 관. 복강, 흉강, 뇌척수강 등 다양한 부위에 사용되며, 감염 예방과 회복 촉진이 목적. 통역 시 주의: 'Drain'을 그대로 '드레인'으로 읽지 말고 'Ống dẫn lưu'로 번역. 배액량과 색깔이 중요한 관찰 지표이므로 환자/보호자에게 '혈액같이 빨간 색이거나 양이 갑자기 많아지면 즉시 알리라'고 교육 필요. 배액관이 빠지면 안 되므로 움직임 주의사항 설명 중요. 제거 시기는 배액량이 줄어들 때이며, 제거 시 약간의 통증이 있을 수 있음을 사전 안내.",
        "meaningVi": "Ống được đặt vào vùng phẫu thuật hoặc vùng nhiễm trùng để dẫn mủ, máu, dịch tiết ra ngoài cơ thể. Sử dụng ở nhiều vị trí như ổ bụng, lồng ngực, não tuỷ, nhằm phòng ngừa nhiễm trùng và thúc đẩy hồi phục.",
        "context": "수술 후 관리, 농양 배농, 흉강 천자 후",
        "culturalNote": "한국 의료기관에서는 수술 후 배액관 관리가 표준 간호 프로토콜이며, 배액량과 성상을 정기적으로 기록함. 배액관은 보통 수술 후 2-7일 내 제거되며, 환자가 움직일 때 불편함과 통증이 있을 수 있어 진통제 처방이 흔함. 베트남에서도 유사하나, 환자와 보호자가 배액관의 목적을 이해하지 못하거나 빨리 제거를 요구하는 경우가 있어 충분한 설명 필요. 배액관이 있는 동안 샤워나 목욕이 제한되므로 위생 관리 방법도 안내해야 함.",
        "commonMistakes": [
            {
                "mistake": "배액관을 'Drain'으로 그대로 읽어줌",
                "correction": "'Ống dẫn lưu' 사용",
                "explanation": "영어 발음은 환자가 이해하기 어려움"
            },
            {
                "mistake": "배액관을 '호스'로 번역",
                "correction": "'Ống dẫn lưu' 또는 'Ống dẫn lưu dịch'",
                "explanation": "의료 용어로 정확히 표현해야 함"
            },
            {
                "mistake": "배액관 색깔/양 관찰 안내 없음",
                "correction": "배액 색깔과 양의 변화를 관찰하고 이상 시 알려달라고 교육",
                "explanation": "환자/보호자의 관찰이 중요한 안전 지표임"
            }
        ],
        "examples": [
            {
                "ko": "수술 부위에 배액관을 넣었습니다. 체액이 빠져나오는지 확인하기 위한 것이니 걱정하지 마세요.",
                "vi": "Đã đặt ống dẫn lưu ở vùng phẫu thuật. Đây là để kiểm tra dịch tiết ra ngoài nên đừng lo lắng.",
                "situation": "onsite"
            },
            {
                "ko": "배액관에서 나오는 액체의 색깔과 양을 확인하고, 갑자기 많아지거나 빨개지면 알려주세요.",
                "vi": "Hãy kiểm tra màu sắc và lượng dịch từ ống dẫn lưu, nếu đột ngột nhiều lên hoặc đỏ thì báo cho tôi.",
                "situation": "onsite"
            },
            {
                "ko": "배액량이 줄어들면 2-3일 후 배액관을 제거할 수 있습니다.",
                "vi": "Khi lượng dẫn lưu giảm, sau 2-3 ngày có thể tháo ống dẫn lưu.",
                "situation": "formal"
            }
        ],
        "relatedTerms": ["배액", "드레싱", "수술후관리", "감염예방", "체액"]
    },
    {
        "slug": "bo-bot",
        "korean": "석고붕대",
        "vietnamese": "Bó bột",
        "hanja": "石膏繃帶",
        "hanjaReading": "石(돌 석) + 膏(기름 고) + 繃(감을 붕) + 帶(띠 대)",
        "pronunciation": "보 봇",
        "meaningKo": "골절이나 인대 손상 시 해당 부위를 고정하여 치유를 돕기 위해 석고 재질로 단단하게 감싸는 붕대. 최근에는 가벼운 합성 석고(fiberglass cast)도 많이 사용됨. 통역 시 주의: 베트남어로는 'Bó bột'이 가장 일반적이며, 'Thạch cao'는 석고 재료 자체를 의미함. 석고 착용 시 가려움, 부종, 통증 등의 불편함이 있을 수 있으며, 물에 닿으면 안 되고, 손가락/발가락 색깔과 감각을 확인하도록 교육해야 함. 석고 제거 시기(보통 4-8주)와 제거 후 재활 필요성도 사전 안내.",
        "meaningVi": "Băng thạch cao cứng bao quanh vùng bị gãy xương hoặc tổn thương dây chằng để cố định và hỗ trợ quá trình lành. Gần đây cũng sử dụng nhiều thạch cao tổng hợp (fiberglass cast) nhẹ hơn.",
        "context": "정형외과, 응급실, 골절 치료, 염좌 고정",
        "culturalNote": "한국 의료기관에서는 석고 착용 시 주의사항 안내가 체계적이며, 석고 착용 중 손가락/발가락의 색깔, 온도, 감각을 확인하도록 교육함. 베트남에서도 유사하나 석고 관리 교육의 수준이 병원마다 다를 수 있음. 한국에서는 '기브스'라는 일본어 외래어도 흔히 쓰이나, 베트남어 통역 시에는 'Bó bột' 사용. 석고 착용 중 목욕이 어려워 위생 관리 방법(비닐 씌우기 등)을 안내하면 좋음. 석고 제거 후 피부가 하얗고 각질이 많아 놀랄 수 있음을 미리 알려주면 불안 감소.",
        "commonMistakes": [
            {
                "mistake": "석고를 'Thạch cao'로만 번역",
                "correction": "'Bó bột' 또는 'Băng thạch cao'",
                "explanation": "'Thạch cao'는 재료이며, 'Bó bột'이 의료 용어로 적절"
            },
            {
                "mistake": "기브스를 'Gibs'로 그대로 읽어줌",
                "correction": "'Bó bột' 사용",
                "explanation": "일본어 외래어는 베트남어 통역 시 사용하지 않음"
            },
            {
                "mistake": "석고 관리 주의사항 설명 없음",
                "correction": "물에 닿지 않게, 손가락/발가락 색깔 확인 등 구체적 안내",
                "explanation": "석고 착용 중 합병증 예방을 위한 교육 필수"
            }
        ],
        "examples": [
            {
                "ko": "골절 부위를 고정하기 위해 석고붕대를 하겠습니다. 24시간 후 단단해집니다.",
                "vi": "Sẽ bó bột để cố định vùng gãy xương. Sau 24 giờ sẽ cứng lại.",
                "situation": "onsite"
            },
            {
                "ko": "석고가 물에 닿으면 안 되고, 가려워도 긁지 마세요. 손가락 색깔이 변하거나 저리면 즉시 오세요.",
                "vi": "Bó bột không được dính nước, và dù ngứa cũng đừng gãi. Nếu ngón tay đổi màu hoặc tê thì đến ngay.",
                "situation": "onsite"
            },
            {
                "ko": "6주 후 석고를 제거하고 재활 치료를 시작합니다.",
                "vi": "Sau 6 tuần sẽ tháo bó bột và bắt đầu điều trị phục hồi chức năng.",
                "situation": "formal"
            }
        ],
        "relatedTerms": ["골절", "고정", "정형외과", "부목", "재활치료"]
    }
]

def main():
    # 기존 데이터 로드
    try:
        with open(file_path, 'r', encoding='utf-8') as f:
            data = json.load(f)
        print(f"✅ 기존 파일 로드 성공: {len(data)}개 용어")
    except FileNotFoundError:
        print(f"❌ 파일을 찾을 수 없습니다: {file_path}")
        return
    except json.JSONDecodeError:
        print(f"❌ JSON 파싱 오류: {file_path}")
        return

    # 기존 slug 목록 추출
    existing_slugs = {term['slug'] for term in data}
    print(f"📋 기존 slug 개수: {len(existing_slugs)}")

    # 중복 필터링
    new_unique_terms = [term for term in new_terms if term['slug'] not in existing_slugs]
    duplicates = [term['slug'] for term in new_terms if term['slug'] in existing_slugs]

    if duplicates:
        print(f"⚠️  중복 발견 ({len(duplicates)}개): {', '.join(duplicates)}")

    if not new_unique_terms:
        print("❌ 추가할 고유 용어가 없습니다.")
        return

    # 데이터에 추가
    data.extend(new_unique_terms)
    print(f"✅ {len(new_unique_terms)}개 용어 추가됨")

    # 파일 저장
    try:
        with open(file_path, 'w', encoding='utf-8') as f:
            json.dump(data, f, ensure_ascii=False, indent=2)
        print(f"✅ 파일 저장 성공: {file_path}")
        print(f"📊 최종 용어 개수: {len(data)}개")
    except Exception as e:
        print(f"❌ 파일 저장 실패: {e}")

if __name__ == "__main__":
    main()
