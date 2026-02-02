#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
환경법/환경규제 전문용어 추가 스크립트
Theme: Environmental Law / Environmental Regulations
Tier S Quality Standard (90+ points)
"""

import json
import os

def main():
    # CRITICAL: Use relative path from script location
    file_path = os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', 'data', 'terms', 'legal.json')

    # Load existing data (data is a LIST!)
    with open(file_path, 'r', encoding='utf-8') as f:
        data = json.load(f)

    # Get existing slugs to prevent duplicates
    existing_slugs = {t['slug'] for t in data}

    # New environmental law terms (Tier S quality)
    new_terms = [
        {
            "slug": "danh-gia-tac-dong-moi-truong",
            "korean": "환경영향평가",
            "vietnamese": "đánh giá tác động môi trường",
            "hanja": "環境影響評價",
            "hanjaReading": "環(환경 환) + 境(지경 경) + 影(그림자 영) + 響(울릴 향) + 評(평할 평) + 價(값 가)",
            "pronunciation": "다인 지아 닥 동 머이 쯔엉",
            "meaningKo": "개발사업이나 정책이 환경에 미치는 영향을 사전에 조사·예측·평가하여 환경보전 방안을 마련하는 제도입니다. 통역 시 주의할 점은 한국의 '환경영향평가'와 베트남의 'đánh giá tác động môi trường'은 평가 절차와 법적 구속력이 다르다는 점입니다. 한국은 전략환경영향평가, 환경영향평가, 소규모 환경영향평가로 3단계로 구분되지만, 베트남은 프로젝트 규모와 환경 위험도에 따라 평가 수준이 결정됩니다. 또한 한국은 환경부 산하 한국환경정책·평가연구원(KEI)이 검토하지만, 베트남은 천연자원환경부(Bộ Tài nguyên và Môi trường)가 직접 승인합니다.",
            "meaningVi": "Là chế độ điều tra, dự báo và đánh giá trước các tác động đến môi trường của dự án phát triển hoặc chính sách, nhằm xây dựng phương án bảo vệ môi trường. Quy trình đánh giá môi trường ở Việt Nam do Bộ Tài nguyên và Môi trường quy định, bao gồm lập báo cáo đánh giá tác động môi trường (ĐTM) và xin phê duyệt.",
            "context": "환경법, 개발사업 허가, 건설 프로젝트 통역 시 필수 용어",
            "culturalNote": "한국은 환경영향평가를 매우 엄격하게 시행하며, 주민 의견 수렴 절차가 법제화되어 있습니다. 반면 베트남은 경제 개발 우선 정책으로 인해 환경영향평가가 상대적으로 유연하게 적용되는 경우가 많습니다. 통역사는 양국의 환경 규제 강도 차이를 이해하고, 한국 기업이 베트남에서 사업할 때 현지 환경법 준수 수준을 정확히 전달해야 합니다. 또한 베트남에서는 '관계(quan hệ)' 중심 문화로 인해 환경평가 승인 과정에서 비공식적 협의가 중요한 역할을 하기도 합니다.",
            "commonMistakes": [
                {
                    "mistake": "'EIA'를 그대로 '이아이에이'로 발음",
                    "correction": "'đánh giá tác động môi trường' 또는 'ĐTM'으로 표현",
                    "explanation": "영문 약어를 그대로 발음하면 베트남 실무자가 이해하지 못하므로 베트남어 정식 명칭이나 현지 약어를 사용해야 합니다."
                },
                {
                    "mistake": "'환경평가'를 'đánh giá môi trường'으로만 번역",
                    "correction": "'đánh giá tác động môi trường' (tác động 강조)",
                    "explanation": "'영향(impact)'의 의미인 'tác động'을 생략하면 단순 환경 조사로 오해될 수 있습니다."
                },
                {
                    "mistake": "한국식 3단계 평가 체계를 베트남에도 동일하게 적용",
                    "correction": "베트남은 프로젝트별 환경 위험도에 따라 평가 수준 결정",
                    "explanation": "한국의 전략환경영향평가, 환경영향평가, 소규모 환경영향평가 구분이 베트남에는 없으므로 혼동 주의."
                }
            ],
            "examples": [
                {
                    "ko": "이 공장 건설 프로젝트는 환경영향평가 대상 사업입니다.",
                    "vi": "Dự án xây dựng nhà máy này thuộc đối tượng phải lập báo cáo đánh giá tác động môi trường.",
                    "situation": "formal"
                },
                {
                    "ko": "환경영향평가서 초안이 완성되면 주민 공람을 실시해야 합니다.",
                    "vi": "Khi hoàn thành bản dự thảo báo cáo ĐTM, cần tổ chức lấy ý kiến cộng đồng dân cư.",
                    "situation": "formal"
                },
                {
                    "ko": "현장에서 환경평가 관련 서류 준비 다 됐나요?",
                    "vi": "Anh đã chuẩn bị đủ hồ sơ đánh giá môi trường cho dự án chưa?",
                    "situation": "onsite"
                }
            ],
            "relatedTerms": ["giay-phep-moi-truong", "tieu-chuan-khi-thai", "trach-nhiem-moi-truong"]
        },
        {
            "slug": "giay-phep-moi-truong",
            "korean": "환경허가",
            "vietnamese": "giấy phép môi trường",
            "hanja": "環境許可",
            "hanjaReading": "環(환경 환) + 境(지경 경) + 許(허락할 허) + 可(옳을 가)",
            "pronunciation": "지이 펩 머이 쯔엉",
            "meaningKo": "환경오염물질을 배출하는 사업장이 사업 개시 전에 환경 관련 법규 준수를 확약하고 관할 기관으로부터 받는 허가증을 말합니다. 통역 시 중요한 점은 한국의 '환경허가'는 배출시설 설치허가, 물환경보전법상 허가 등 여러 종류가 있으나, 베트남의 'giấy phép môi trường'은 통합 환경허가 개념에 가깝다는 점입니다. 한국 기업이 베트남에서 공장을 설립할 때 '환경허가증(giấy phép môi trường)'을 먼저 취득해야 하며, 이를 받지 않으면 사업 개시가 불가능합니다. 베트남에서는 성급(tỉnh) 천연자원환경부서(Sở Tài nguyên và Môi trường)가 발급 권한을 가집니다.",
            "meaningVi": "Là giấy phép do cơ quan quản lý nhà nước về môi trường cấp cho cơ sở sản xuất, kinh doanh có phát sinh chất thải gây ô nhiễm môi trường. Giấy phép này xác nhận rằng cơ sở đã cam kết tuân thủ các quy định về bảo vệ môi trường.",
            "context": "공장 설립, 사업 허가, 환경법 준수 통역 시 필수",
            "culturalNote": "베트남에서 환경허가 취득은 형식적 절차가 아니라 실질적 사업 개시 조건이므로, 한국 기업들이 간과하기 쉬운 부분입니다. 특히 베트남은 환경 관련 벌금이 매우 높고, 무허가 운영 적발 시 사업 중단 명령까지 내려질 수 있어 주의가 필요합니다. 한국은 환경 규제가 체계적이고 사후 관리가 철저한 반면, 베트남은 초기 허가 과정에서 더 많은 서류와 증빙을 요구하는 경향이 있습니다. 통역사는 '관계 중심' 문화에서 환경허가 담당 공무원과의 원활한 소통이 승인 기간에 영향을 줄 수 있음을 인지해야 합니다.",
            "commonMistakes": [
                {
                    "mistake": "'허가'를 'cho phép'으로만 번역",
                    "correction": "'giấy phép' (허가증 문서 강조)",
                    "explanation": "'cho phép'은 동사형으로 '허락하다'의 의미이고, 'giấy phép'은 명사형으로 실제 허가증 문서를 의미합니다."
                },
                {
                    "mistake": "'환경허가증'을 'giấy chứng nhận môi trường'으로 표현",
                    "correction": "'giấy phép môi trường' (법적 허가)",
                    "explanation": "'giấy chứng nhận'은 인증서를 의미하고, 'giấy phép'은 허가증을 의미하므로 법적 효력이 다릅니다."
                },
                {
                    "mistake": "한국의 배출시설 설치허가를 베트남 환경허가와 동일하게 취급",
                    "correction": "베트남은 통합환경허가 개념, 한국은 개별 허가",
                    "explanation": "한국은 대기, 수질, 폐기물 등 배출 분야별 개별 허가가 있지만, 베트남은 하나의 통합 환경허가로 운영됩니다."
                }
            ],
            "examples": [
                {
                    "ko": "공장 가동 전에 환경허가증을 반드시 취득해야 합니다.",
                    "vi": "Trước khi vận hành nhà máy, bắt buộc phải có giấy phép môi trường.",
                    "situation": "formal"
                },
                {
                    "ko": "환경허가 신청 서류에 폐수 처리 계획서도 포함해야 합니다.",
                    "vi": "Hồ sơ xin giấy phép môi trường cũng cần bao gồm phương án xử lý nước thải.",
                    "situation": "formal"
                },
                {
                    "ko": "환경허가증 나오는 데 보통 얼마나 걸려요?",
                    "vi": "Thông thường mất bao lâu để được cấp giấy phép môi trường?",
                    "situation": "informal"
                }
            ],
            "relatedTerms": ["danh-gia-tac-dong-moi-truong", "xu-ly-chat-thai", "tieu-chuan-khi-thai"]
        },
        {
            "slug": "tieu-chuan-khi-thai",
            "korean": "배출기준",
            "vietnamese": "tiêu chuẩn khí thải",
            "hanja": "排出基準",
            "hanjaReading": "排(물리칠 배) + 出(날 출) + 基(터 기) + 準(준할 준)",
            "pronunciation": "띠에우 쭈언 키 타이",
            "meaningKo": "사업장에서 배출되는 대기오염물질, 수질오염물질, 소음·진동 등이 환경기준을 초과하지 않도록 법으로 정한 허용 한계치를 말합니다. 통역 시 주의할 점은 'khí thải'가 '배기가스'를 의미하지만, 문맥에 따라 '배출물 전반'을 의미할 수 있다는 점입니다. 한국은 대기환경보전법, 물환경보전법 등에서 배출허용기준을 명확히 규정하지만, 베트남은 'QCVN(Quy chuẩn kỹ thuật quốc gia - 국가기술기준)'으로 통칭됩니다. 예를 들어 QCVN 19:2009는 산업 배출수 기준, QCVN 20:2009는 대기배출 기준입니다. 통역사는 양국의 기준치가 다르므로 단순 번역이 아니라 기준 수치 자체를 확인해야 합니다.",
            "meaningVi": "Là giới hạn tối đa cho phép của các chất gây ô nhiễm không khí, nước thải, tiếng ồn, độ rung do cơ sở sản xuất thải ra, được quy định bởi pháp luật để bảo vệ môi trường. Việt Nam áp dụng hệ thống QCVN (Quy chuẩn kỹ thuật quốc gia) để quản lý các tiêu chuẩn này.",
            "context": "환경 규제, 공장 운영, 환경법 준수 통역",
            "culturalNote": "한국의 배출기준은 세계적으로 매우 엄격한 수준이며, 실시간 모니터링 시스템(TMS: Tele-Monitoring System)을 통해 24시간 감시됩니다. 반면 베트남은 배출기준은 있으나 모니터링 인프라가 부족해 실질적 단속이 약한 편입니다. 그러나 최근 베트남 정부가 환경 규제를 강화하고 있어, 한국 기업들이 '베트남은 환경 규제가 느슨하다'는 과거 인식으로 접근하면 곤란합니다. 통역사는 한국 기업이 베트남 현지 기준을 준수하도록 정확한 정보를 전달해야 하며, 특히 '기준 초과 시 벌금'이 매우 높다는 점을 강조해야 합니다.",
            "commonMistakes": [
                {
                    "mistake": "'배출기준'을 'mức phát thải'로만 번역",
                    "correction": "'tiêu chuẩn khí thải' 또는 'QCVN'",
                    "explanation": "'mức phát thải'는 배출 수준이고, 'tiêu chuẩn khí thải'는 법적 기준을 의미하므로 법적 맥락에서는 후자를 사용해야 합니다."
                },
                {
                    "mistake": "'khí thải'를 '대기 배출'로만 한정",
                    "correction": "문맥에 따라 '배출물 전반' 또는 '배기가스'",
                    "explanation": "'khí thải'는 좁게는 대기 배출, 넓게는 모든 배출물을 의미할 수 있으므로 문맥 파악이 중요합니다."
                },
                {
                    "mistake": "한국 기준치를 베트남 기준치로 착각",
                    "correction": "양국의 QCVN과 한국 법령 기준치는 다름",
                    "explanation": "예를 들어 COD 배출 기준이 한국과 베트남이 다르므로, 수치를 그대로 적용하면 안 됩니다."
                }
            ],
            "examples": [
                {
                    "ko": "귀사의 배출가스가 법적 배출기준을 초과하고 있습니다.",
                    "vi": "Khí thải của công ty quý vị đã vượt quá tiêu chuẩn khí thải theo quy định pháp luật.",
                    "situation": "formal"
                },
                {
                    "ko": "베트남 QCVN 기준에 맞춰 배출 시설을 업그레이드해야 합니다.",
                    "vi": "Cần nâng cấp hệ thống xử lý khí thải để phù hợp với tiêu chuẩn QCVN của Việt Nam.",
                    "situation": "formal"
                },
                {
                    "ko": "배출 기준 넘으면 벌금 엄청 세요.",
                    "vi": "Nếu vượt tiêu chuẩn khí thải thì bị phạt rất nặng đó.",
                    "situation": "informal"
                }
            ],
            "relatedTerms": ["xu-ly-chat-thai", "o-nhiem-nguon-nuoc", "giay-phep-moi-truong"]
        },
        {
            "slug": "xu-ly-chat-thai",
            "korean": "폐기물처리",
            "vietnamese": "xử lý chất thải",
            "hanja": "廢棄物處理",
            "hanjaReading": "廢(버릴 폐) + 棄(버릴 기) + 物(물건 물) + 處(곳 처) + 理(다스릴 리)",
            "pronunciation": "쑤 리 짯 타이",
            "meaningKo": "생활, 사업 활동 등에서 발생한 쓰레기나 폐기물을 수집·운반·재활용·소각·매립 등의 방법으로 처리하는 일련의 과정을 말합니다. 통역 시 주의할 점은 한국의 '폐기물'은 생활폐기물, 사업장폐기물, 건설폐기물, 의료폐기물 등으로 세분화되어 각각 관리 체계가 다르지만, 베트남의 'chất thải'는 포괄적 개념으로 쓰인다는 점입니다. 베트남에서는 'chất thải rắn(고체 폐기물)', 'chất thải lỏng(액체 폐기물)', 'chất thải nguy hại(유해 폐기물)' 등으로 구분합니다. 한국 기업이 베트남에서 공장을 운영할 때 폐기물 처리 업체를 선정하고 계약하는 과정에서 통역사의 역할이 매우 중요합니다.",
            "meaningVi": "Là quá trình thu gom, vận chuyển, tái chế, đốt hoặc chôn lấp rác thải và chất thải phát sinh từ hoạt động sinh hoạt, sản xuất kinh doanh. Việt Nam phân loại chất thải thành chất thải rắn, chất thải lỏng, chất thải khí và chất thải nguy hại, mỗi loại có quy định xử lý riêng.",
            "context": "환경법, 공장 운영, 폐기물 관리 통역",
            "culturalNote": "한국은 폐기물 처리 시스템이 고도로 발달해 있으며, '쓰레기 종량제'와 '재활용 분리수거'가 일상화되어 있습니다. 반면 베트남은 폐기물 분리수거 문화가 아직 정착되지 않았고, 대부분 혼합 수거 후 매립하는 방식이 주를 이룹니다. 한국 기업이 베트남에서 공장을 운영할 때 '한국식 폐기물 관리'를 요구하면 현지 업체가 대응하기 어려운 경우가 많습니다. 통역사는 양국의 폐기물 처리 문화 차이를 이해하고, 현실적인 대안을 제시할 수 있도록 소통을 도와야 합니다. 특히 베트남에서는 폐기물 처리 비용이 한국보다 저렴하지만, 불법 투기 위험도 높으므로 신뢰할 수 있는 업체 선정이 중요합니다.",
            "commonMistakes": [
                {
                    "mistake": "'폐기물'을 'rác'로만 번역",
                    "correction": "'chất thải' (산업 폐기물) 또는 'rác thải' (생활 쓰레기)",
                    "explanation": "'rác'은 일반 쓰레기를 의미하고, 'chất thải'는 산업·의료 폐기물 등 법적 관리 대상을 의미합니다."
                },
                {
                    "mistake": "'처리'를 'xử lý'로만 쓰고 세부 방법 명시 안 함",
                    "correction": "'xử lý bằng cách đốt(소각)', 'chôn lấp(매립)', 'tái chế(재활용)' 등 구체화",
                    "explanation": "베트남 현지 업체는 '처리 방법'에 따라 비용과 절차가 다르므로 구체적 표현이 필요합니다."
                },
                {
                    "mistake": "한국식 분리수거 체계를 베트남에 그대로 적용",
                    "correction": "베트남은 혼합 수거 후 처리장에서 분류",
                    "explanation": "베트남은 가정·사업장에서 분리배출하는 문화가 약하므로, 한국식 요구는 현실성이 낮습니다."
                }
            ],
            "examples": [
                {
                    "ko": "공장에서 발생하는 유해 폐기물은 전문 처리 업체에 위탁해야 합니다.",
                    "vi": "Chất thải nguy hại phát sinh từ nhà máy phải giao cho đơn vị chuyên xử lý có giấy phép.",
                    "situation": "formal"
                },
                {
                    "ko": "폐기물 처리 비용은 톤당 얼마인가요?",
                    "vi": "Chi phí xử lý chất thải là bao nhiêu tiền một tấn?",
                    "situation": "onsite"
                },
                {
                    "ko": "쓰레기 분리수거 좀 해줘야 하는데, 여기는 다 섞어서 버리네.",
                    "vi": "Cần phân loại rác thải chứ, ở đây họ trộn tất cả vào một chỗ luôn.",
                    "situation": "informal"
                }
            ],
            "relatedTerms": ["giay-phep-moi-truong", "tieu-chuan-khi-thai", "trach-nhiem-moi-truong"]
        },
        {
            "slug": "o-nhiem-nguon-nuoc",
            "korean": "수질오염",
            "vietnamese": "ô nhiễm nguồn nước",
            "hanja": "水質汚染",
            "hanjaReading": "水(물 수) + 質(바탕 질) + 汚(더러울 오) + 染(물들일 염)",
            "pronunciation": "오 니엠 응우언 느억",
            "meaningKo": "하천, 호수, 지하수 등의 수질이 화학물질, 미생물, 중금속 등으로 오염되어 사람이나 생태계에 해를 끼치는 상태를 말합니다. 통역 시 주의할 점은 한국의 '수질오염'은 물환경보전법상 '수질오염물질'로 정의된 83종의 물질 기준으로 관리되지만, 베트남은 QCVN 08:2015(지표수 수질 기준), QCVN 14:2008(생활용수 수질 기준) 등으로 관리된다는 점입니다. 한국 기업이 베트남에서 공장을 운영할 때 폐수 처리 시설 없이 방류하면 엄청난 벌금과 사업 중단 위험이 있으므로, 통역사는 '수질오염 방지'의 중요성을 강조해야 합니다. 특히 베트남 메콩강 유역은 농업·어업 의존도가 높아 수질오염에 매우 민감합니다.",
            "meaningVi": "Là tình trạng chất lượng nước ở sông, hồ, nước ngầm bị ô nhiễm bởi hóa chất, vi sinh vật, kim loại nặng, gây hại cho con người và hệ sinh thái. Việt Nam quản lý ô nhiễm nước qua các quy chuẩn QCVN về chất lượng nước mặt, nước sinh hoạt và nước thải.",
            "context": "환경법, 공장 폐수 관리, 환경 책임 통역",
            "culturalNote": "한국은 4대강 유역 환경청이 수질을 철저히 관리하며, 실시간 수질 측정망(TMS)을 통해 감시합니다. 반면 베트남은 수질 모니터링 인프라가 부족해 오염 사고 발생 후에야 대응하는 경우가 많습니다. 그러나 최근 베트남에서 '포름알데히드 물고기 사건(cá nhiễm formaldehyde)' 등 수질오염 사고가 사회적 이슈가 되면서, 정부가 단속을 강화하고 있습니다. 한국 기업이 베트남에서 공장을 운영할 때 '폐수 무단 방류'로 적발되면 벌금뿐 아니라 지역 주민의 집단 민원, 언론 보도 등으로 기업 이미지에 큰 타격을 입을 수 있습니다. 통역사는 수질오염의 법적·사회적 리스크를 정확히 전달해야 합니다.",
            "commonMistakes": [
                {
                    "mistake": "'수질오염'을 'ô nhiễm nước'로만 번역",
                    "correction": "'ô nhiễm nguồn nước' (수원 오염 강조)",
                    "explanation": "'ô nhiễm nước'는 '물 오염' 일반이고, 'ô nhiễm nguồn nước'는 수원지 오염으로 더 심각한 의미입니다."
                },
                {
                    "mistake": "'폐수'를 'nước bẩn'으로 표현",
                    "correction": "'nước thải' (산업 폐수)",
                    "explanation": "'nước bẩn'은 '더러운 물'이고, 'nước thải'는 법적 관리 대상인 '폐수'입니다."
                },
                {
                    "mistake": "한국의 COD, BOD 기준을 베트남에 그대로 적용",
                    "correction": "베트남 QCVN 기준 확인 필수",
                    "explanation": "한국과 베트남의 수질 기준치가 다르므로, 수치를 그대로 적용하면 오해가 발생합니다."
                }
            ],
            "examples": [
                {
                    "ko": "공장 폐수로 인한 수질오염이 심각해 주민들이 민원을 제기했습니다.",
                    "vi": "Ô nhiễm nguồn nước do nước thải từ nhà máy rất nghiêm trọng, người dân đã khiếu nại.",
                    "situation": "formal"
                },
                {
                    "ko": "수질오염 방지를 위해 폐수 처리 시설을 설치해야 합니다.",
                    "vi": "Để phòng ngừa ô nhiễm nguồn nước, cần lắp đặt hệ thống xử lý nước thải.",
                    "situation": "formal"
                },
                {
                    "ko": "강물이 너무 더러워서 물고기가 다 죽었어요.",
                    "vi": "Nước sông bị ô nhiễm nặng nên cá chết hết rồi.",
                    "situation": "informal"
                }
            ],
            "relatedTerms": ["xu-ly-chat-thai", "tieu-chuan-khi-thai", "bao-ve-rung"]
        },
        {
            "slug": "bao-ve-rung",
            "korean": "산림보호",
            "vietnamese": "bảo vệ rừng",
            "hanja": "山林保護",
            "hanjaReading": "山(뫼 산) + 林(수풀 림) + 保(지킬 보) + 護(지킬 호)",
            "pronunciation": "바오 베 중",
            "meaningKo": "산림 자원을 산불, 병충해, 불법 벌채 등으로부터 지키고, 지속 가능한 이용을 위해 관리하는 활동을 말합니다. 통역 시 주의할 점은 한국의 '산림'은 주로 사유림과 국유림으로 구분되며 산림청이 관리하지만, 베트남의 'rừng'은 국가 소유가 대부분이고 '3종 산림(rừng đặc dụng, rừng phòng hộ, rừng sản xuất)' 체계로 관리된다는 점입니다. 베트남은 과거 전쟁으로 산림이 크게 훼손되어 '녹화 사업'을 국가 과제로 추진 중이며, 산림 보호 위반 시 처벌이 매우 엄격합니다. 한국 기업이 베트남에서 목재 가공 사업을 할 때 '합법 목재 증명(gỗ hợp pháp)'이 없으면 불법 벌채 연루 위험이 있으므로 주의해야 합니다.",
            "meaningVi": "Là hoạt động bảo vệ tài nguyên rừng khỏi cháy rừng, sâu bệnh, khai thác trái phép, và quản lý để sử dụng bền vững. Việt Nam phân loại rừng thành rừng đặc dụng (bảo tồn), rừng phòng hộ (bảo vệ đầu nguồn), và rừng sản xuất (khai thác kinh tế).",
            "context": "환경법, 목재 산업, 환경 보호 통역",
            "culturalNote": "베트남은 '산림법(Luật Lâm nghiệp)'에서 산림을 국가 자산으로 규정하며, 무단 벌채 시 형사 처벌까지 가능합니다. 특히 '귀중목(gỗ quý)'으로 지정된 나무(예: trắc, lim, sưa)는 벌채가 금지되며, 적발 시 거액의 벌금과 함께 목재 전량 몰수됩니다. 한국은 산림이 주로 사유재산이지만, 베트남은 국가 소유이므로 산림 이용 허가 절차가 복잡합니다. 통역사는 한국 기업이 베트남에서 목재를 조달할 때 '합법성 증명(FSC 인증 등)'을 반드시 확인하도록 안내해야 합니다. 또한 베트남 중부 고원지대(Tây Nguyên)는 소수민족이 전통적으로 산림에 의존하므로, 산림 사업 시 지역 공동체와의 갈등도 고려해야 합니다.",
            "commonMistakes": [
                {
                    "mistake": "'산림'을 'rừng núi'로 번역",
                    "correction": "'rừng' (산림) 또는 'tài nguyên rừng' (산림 자원)",
                    "explanation": "'rừng núi'는 '산과 숲' 전체를 의미하고, 'rừng'은 법적 관리 대상인 산림을 의미합니다."
                },
                {
                    "mistake": "'벌채'를 'chặt cây'로만 표현",
                    "correction": "'khai thác gỗ' (목재 벌채) 또는 'chặt phá rừng' (산림 훼손)",
                    "explanation": "'chặt cây'는 나무 베기 일반이고, 'khai thác gỗ'는 상업적 벌채, 'chặt phá rừng'은 불법 훼손입니다."
                },
                {
                    "mistake": "한국의 사유림 개념을 베트남에 적용",
                    "correction": "베트남은 대부분 국유림",
                    "explanation": "베트남은 산림의 약 80%가 국가 소유이므로, 사유림 거래나 이용이 한국처럼 자유롭지 않습니다."
                }
            ],
            "examples": [
                {
                    "ko": "불법 벌채를 방지하기 위해 산림보호 단속을 강화하고 있습니다.",
                    "vi": "Để ngăn chặn khai thác gỗ trái phép, đang tăng cường kiểm tra bảo vệ rừng.",
                    "situation": "formal"
                },
                {
                    "ko": "이 목재는 합법적으로 벌채된 것인지 증명서를 확인해야 합니다.",
                    "vi": "Cần kiểm tra giấy chứng nhận xem gỗ này có được khai thác hợp pháp không.",
                    "situation": "formal"
                },
                {
                    "ko": "여기 나무 함부로 베면 안 돼요, 벌금 엄청 나와요.",
                    "vi": "Ở đây chặt cây bừa bãi là không được đâu, bị phạt rất nặng.",
                    "situation": "informal"
                }
            ],
            "relatedTerms": ["phat-trien-ben-vung", "bien-doi-khi-hau", "trach-nhiem-moi-truong"]
        },
        {
            "slug": "phat-trien-ben-vung",
            "korean": "지속가능개발",
            "vietnamese": "phát triển bền vững",
            "hanja": "持續可能開發",
            "hanjaReading": "持(가질 지) + 續(이을 속) + 可(옳을 가) + 能(능할 능) + 開(열 개) + 發(필 발)",
            "pronunciation": "팟 찌엔 벤 붕",
            "meaningKo": "현세대의 필요를 충족하면서도 미래 세대의 필요를 저해하지 않는 방식으로 경제·사회·환경을 조화롭게 발전시키는 개념입니다. 통역 시 중요한 점은 한국에서는 'SDGs(지속가능발전목표)'가 정부 정책과 기업 ESG 경영에 반영되고 있지만, 베트남은 아직 '경제 성장' 우선 정책이 강하다는 점입니다. 그러나 베트남 정부도 2030년까지 '녹색 성장 전략(chiến lược tăng trưởng xanh)'을 추진 중이며, 재생에너지, 친환경 농업 등을 장려하고 있습니다. 한국 기업이 베트남에서 사업할 때 '지속가능성'을 강조하면 정부 지원을 받거나 세제 혜택을 받을 가능성이 있으므로, 통역사는 이를 적극 활용하도록 조언할 수 있습니다.",
            "meaningVi": "Là khái niệm phát triển kinh tế, xã hội và môi trường một cách hài hòa, đáp ứng nhu cầu của thế hệ hiện tại mà không ảnh hưởng đến khả năng đáp ứng nhu cầu của thế hệ tương lai. Việt Nam đang thực hiện chiến lược tăng trưởng xanh và cam kết đạt mục tiêu phát triển bền vững SDGs đến năm 2030.",
            "context": "환경법, 기업 CSR, 정부 정책 통역",
            "culturalNote": "한국은 2050 탄소중립 목표를 선언하고, 기업들도 ESG(환경·사회·지배구조) 경영을 도입하고 있습니다. 반면 베트남은 여전히 '경제 개발'이 최우선 과제이지만, 국제 사회의 압력과 기후변화 영향으로 점차 '지속가능성'을 중요시하고 있습니다. 특히 베트남은 메콩강 삼각주 지역이 해수면 상승 위협에 노출되어 있어, '기후변화 적응'이 국가적 과제입니다. 통역사는 한국 기업이 베트남에서 '친환경 기술', '재생에너지' 등을 제안할 때 '지속가능개발' 프레임을 활용하면 현지 정부와의 협상에서 유리할 수 있음을 인지해야 합니다. 또한 베트남은 '녹색 성장'을 국가 브랜드로 육성 중이므로, 관련 사업은 정부 지원을 받을 가능성이 높습니다.",
            "commonMistakes": [
                {
                    "mistake": "'지속가능'을 'có thể tiếp tục'로 직역",
                    "correction": "'bền vững' (지속가능성)",
                    "explanation": "'có thể tiếp tục'는 '계속할 수 있다'는 의미이고, 'bền vững'은 환경·경제·사회를 아우르는 '지속가능성' 개념입니다."
                },
                {
                    "mistake": "'개발'을 'phát triển'과 'khai thác' 혼용",
                    "correction": "'phát triển' (발전) vs 'khai thác' (개발/채굴)",
                    "explanation": "'phát triển'은 긍정적 발전이고, 'khai thác'은 자원 채굴로 부정적 뉘앙스가 있습니다."
                },
                {
                    "mistake": "SDGs를 '에스디지'로 발음",
                    "correction": "'Mục tiêu phát triển bền vững' 또는 'SDGs'",
                    "explanation": "영문 약어를 그대로 발음하면 이해되지 않으므로, 베트남어 정식 명칭을 함께 사용해야 합니다."
                }
            ],
            "examples": [
                {
                    "ko": "우리 회사는 지속가능개발 목표에 부합하는 친환경 사업을 추진하고 있습니다.",
                    "vi": "Công ty chúng tôi đang triển khai các dự án thân thiện với môi trường phù hợp với mục tiêu phát triển bền vững.",
                    "situation": "formal"
                },
                {
                    "ko": "베트남 정부의 녹색 성장 전략에 맞춰 재생에너지 사업을 제안합니다.",
                    "vi": "Chúng tôi đề xuất dự án năng lượng tái tạo phù hợp với chiến lược tăng trưởng xanh của Chính phủ Việt Nam.",
                    "situation": "formal"
                },
                {
                    "ko": "요즘 지속가능 경영 안 하면 투자 못 받아요.",
                    "vi": "Dạo này không làm kinh doanh bền vững thì không huy động được vốn đâu.",
                    "situation": "informal"
                }
            ],
            "relatedTerms": ["bien-doi-khi-hau", "nang-luong-tai-tao", "bao-ve-rung"]
        },
        {
            "slug": "bien-doi-khi-hau",
            "korean": "기후변화",
            "vietnamese": "biến đổi khí hậu",
            "hanja": "氣候變化",
            "hanjaReading": "氣(기운 기) + 候(때 후) + 變(변할 변) + 化(될 화)",
            "pronunciation": "비엔 도이 키 하우",
            "meaningKo": "지구 온난화로 인해 기온, 강수량, 해수면 등이 장기적으로 변화하는 현상을 말하며, 인간 활동에 의한 온실가스 배출이 주요 원인입니다. 통역 시 주의할 점은 한국은 '2050 탄소중립' 목표를 법제화했지만, 베트남은 2050년이 아닌 2060년을 목표로 설정했다는 점입니다. 베트남은 메콩강 삼각주 지역이 해수면 상승으로 침수 위험이 크고, 태풍 피해가 빈번해 '기후변화 적응'이 국가적 과제입니다. 한국 기업이 베트남에서 탄소배출권, 재생에너지, 에너지 효율 개선 사업을 제안할 때 '기후변화 대응'을 강조하면 정부 지원을 받을 가능성이 높습니다. 통역사는 양국의 탄소중립 목표 차이를 정확히 전달해야 합니다.",
            "meaningVi": "Là hiện tượng thay đổi lâu dài về nhiệt độ, lượng mưa, mực nước biển do hiện tượng ấm lên toàn cầu, nguyên nhân chính là phát thải khí nhà kính từ hoạt động của con người. Việt Nam cam kết đạt mục tiêu trung hòa carbon vào năm 2060 và đang đối mặt với nguy cơ ngập lụt do nước biển dâng ở vùng đồng bằng sông Cửu Long.",
            "context": "환경법, 기후 정책, 재생에너지 통역",
            "culturalNote": "베트남은 세계에서 기후변화 피해에 가장 취약한 국가 중 하나로, 특히 메콩강 삼각주는 해수면 1m 상승 시 약 40%가 침수될 위험이 있습니다. 이로 인해 베트남 정부는 '기후변화 적응 국가 계획(NĐ 139/2016/NĐ-CP)'을 수립하고, 국제 사회로부터 기후기금을 유치하려 노력하고 있습니다. 한국은 '녹색기후기금(GCF)' 사무국을 인천에 유치했으며, 베트남에 기후변화 대응 기술을 지원하는 ODA 사업을 다수 진행 중입니다. 통역사는 한국 기업이 베트남 정부와 협력할 때 '기후변화 대응'을 명분으로 활용하면 유리하다는 점을 인지해야 합니다. 또한 베트남은 '탄소세(thuế carbon)' 도입을 검토 중이므로, 향후 탄소 배출 규제가 강화될 가능성이 높습니다.",
            "commonMistakes": [
                {
                    "mistake": "'기후변화'를 'thay đổi khí hậu'로만 번역",
                    "correction": "'biến đổi khí hậu' (공식 용어)",
                    "explanation": "'thay đổi'는 일반적 변화이고, 'biến đổi'는 환경·과학 분야에서 쓰는 공식 용어입니다."
                },
                {
                    "mistake": "'탄소중립'을 'carbon trung hòa'로 직역",
                    "correction": "'trung hòa carbon' 또는 'Net Zero'",
                    "explanation": "베트남어는 '명사 + 형용사' 순서이므로 'trung hòa carbon'이 올바른 표현입니다."
                },
                {
                    "mistake": "한국의 2050 목표를 베트남에도 동일하게 적용",
                    "correction": "베트남은 2060년 탄소중립 목표",
                    "explanation": "한국과 베트남의 탄소중립 목표 연도가 다르므로, 정책 논의 시 혼동 주의."
                }
            ],
            "examples": [
                {
                    "ko": "기후변화로 인해 베트남 남부 지역의 해수면 상승이 심각한 문제입니다.",
                    "vi": "Do biến đổi khí hậu, vấn đề nước biển dâng ở miền Nam Việt Nam rất nghiêm trọng.",
                    "situation": "formal"
                },
                {
                    "ko": "우리 회사는 탄소 배출을 줄이기 위해 재생에너지로 전환하고 있습니다.",
                    "vi": "Công ty chúng tôi đang chuyển đổi sang năng lượng tái tạo để giảm phát thải carbon.",
                    "situation": "formal"
                },
                {
                    "ko": "요즘 날씨 너무 이상해요, 기후변화 때문인가 봐요.",
                    "vi": "Dạo này thời tiết lạ quá, chắc là do biến đổi khí hậu.",
                    "situation": "informal"
                }
            ],
            "relatedTerms": ["nang-luong-tai-tao", "phat-trien-ben-vung", "trach-nhiem-moi-truong"]
        },
        {
            "slug": "nang-luong-tai-tao",
            "korean": "재생에너지",
            "vietnamese": "năng lượng tái tạo",
            "hanja": "再生에너지",
            "hanjaReading": "再(다시 재) + 生(날 생) + energy(에너지)",
            "pronunciation": "낭 르엉 따이 따오",
            "meaningKo": "태양광, 풍력, 수력, 바이오매스 등 자연에서 지속적으로 얻을 수 있는 에너지로, 화석연료와 달리 온실가스 배출이 적어 환경 친화적입니다. 통역 시 주의할 점은 한국의 '재생에너지 3020 정책'(2030년까지 재생에너지 발전 비중 20%)과 베트남의 '전력개발계획 8(PDP 8)'의 목표가 다르다는 점입니다. 베트남은 2030년까지 재생에너지 비중을 30%로 확대하려 하며, 특히 태양광(điện mặt trời)과 풍력(điện gió)에 집중 투자하고 있습니다. 한국 기업이 베트남에 재생에너지 플랜트를 수출하거나 투자할 기회가 많으므로, 통역사는 양국의 에너지 정책을 정확히 이해해야 합니다.",
            "meaningVi": "Là năng lượng có thể tái tạo liên tục từ thiên nhiên như năng lượng mặt trời, gió, thủy điện, sinh khối, thân thiện với môi trường do ít phát thải khí nhà kính so với nhiên liệu hóa thạch. Việt Nam đang đẩy mạnh phát triển năng lượng tái tạo theo Quy hoạch điện 8 (PDP 8), mục tiêu đạt 30% vào năm 2030.",
            "context": "에너지 정책, 환경법, 발전소 건설 통역",
            "culturalNote": "베트남은 2010년대 후반부터 태양광 발전에 대한 FIT(발전차액지원제도)를 도입해 급격히 성장했으나, 송전망 부족으로 '재생에너지 발전 중단(cắt giảm điện tái tạo)' 사태가 발생하기도 했습니다. 한국은 재생에너지 발전 기술은 앞서지만, 부지 확보와 주민 수용성 문제로 어려움을 겪고 있습니다. 반면 베트남은 넓은 국토와 풍부한 일조량으로 태양광 발전 잠재력이 크지만, 송전 인프라가 부족합니다. 통역사는 한국 기업이 베트남에서 재생에너지 사업을 할 때 '송전망 연계(kết nối lưới điện)' 문제를 사전에 확인하도록 조언해야 합니다. 또한 베트남 정부가 'Direct PPA(직접 전력구매계약)'를 허용하면서, 외국 기업이 재생에너지를 직접 구매할 수 있게 되어 한국 기업의 베트남 진출 기회가 확대되고 있습니다.",
            "commonMistakes": [
                {
                    "mistake": "'재생에너지'를 'năng lượng tái sinh'으로 번역",
                    "correction": "'năng lượng tái tạo' (재생 가능)",
                    "explanation": "'tái sinh'은 '부활'의 의미이고, 'tái tạo'는 '재생 가능'의 의미로 에너지 분야 공식 용어입니다."
                },
                {
                    "mistake": "'태양광'을 'ánh sáng mặt trời'로 표현",
                    "correction": "'điện mặt trời' (태양광 발전)",
                    "explanation": "'ánh sáng mặt trời'는 '햇빛'이고, 'điện mặt trời'는 '태양광 발전'입니다."
                },
                {
                    "mistake": "FIT를 '피트'로 발음",
                    "correction": "'chính sách giá điện ưu đãi' 또는 'FIT'",
                    "explanation": "영문 약어를 발음하면 이해되지 않으므로, 베트남어 설명과 함께 사용해야 합니다."
                }
            ],
            "examples": [
                {
                    "ko": "베트남 정부는 재생에너지 개발을 적극 지원하고 있습니다.",
                    "vi": "Chính phủ Việt Nam đang hỗ trợ mạnh mẽ phát triển năng lượng tái tạo.",
                    "situation": "formal"
                },
                {
                    "ko": "우리 회사는 태양광 발전소 건설 경험이 풍부합니다.",
                    "vi": "Công ty chúng tôi có kinh nghiệm phong phú trong xây dựng nhà máy điện mặt trời.",
                    "situation": "formal"
                },
                {
                    "ko": "재생에너지 쓰면 전기료 줄일 수 있어요.",
                    "vi": "Dùng năng lượng tái tạo thì giảm được tiền điện đó.",
                    "situation": "informal"
                }
            ],
            "relatedTerms": ["bien-doi-khi-hau", "phat-trien-ben-vung", "trach-nhiem-moi-truong"]
        },
        {
            "slug": "trach-nhiem-moi-truong",
            "korean": "환경책임",
            "vietnamese": "trách nhiệm môi trường",
            "hanja": "環境責任",
            "hanjaReading": "環(환경 환) + 境(지경 경) + 責(꾸짖을 책) + 任(맡길 임)",
            "pronunciation": "짝 니엠 머이 쯔엉",
            "meaningKo": "기업이나 개인이 환경에 미치는 영향에 대해 지는 법적·도덕적 책임을 말하며, 환경 오염 발생 시 복구, 배상, 처벌 등의 의무를 포함합니다. 통역 시 중요한 점은 한국의 '환경책임'은 환경오염피해 배상책임 및 구제에 관한 법률(환경오염피해구제법)로 구체화되어 있지만, 베트Nam의 'trách nhiệm môi trường'은 환경보호법(Luật Bảo vệ môi trường 2020)에서 포괄적으로 규정된다는 점입니다. 베트남에서는 '환경 오염 발생 시 원인자 부담 원칙(nguyên tắc người gây ô nhiễm phải trả tiền)'이 엄격히 적용되며, 한국 기업이 베트남에서 환경 사고를 일으키면 막대한 배상금과 함께 사업 허가 취소까지 당할 수 있습니다.",
            "meaningVi": "Là trách nhiệm pháp lý và đạo đức của doanh nghiệp hoặc cá nhân đối với tác động môi trường, bao gồm nghĩa vụ khắc phục, bồi thường và chịu xử phạt khi gây ô nhiễm. Việt Nam áp dụng nguyên tắc 'người gây ô nhiễm phải trả tiền' theo Luật Bảo vệ môi trường 2020.",
            "context": "환경법, 기업 CSR, 환경 사고 대응 통역",
            "culturalNote": "베트남에서는 2016년 '포름알데히드 물고기 사건'으로 대만 기업 Formosa가 5억 달러 배상금을 내고도 사회적 비난을 받은 사례가 있습니다. 이 사건 이후 베트남 정부와 국민의 '환경 책임' 인식이 크게 높아졌으며, 외국 기업에 대한 환경 감시가 강화되었습니다. 한국 기업이 베트남에서 사업할 때 '환경 책임'을 경시하면 법적 처벌뿐 아니라 언론 보도, 주민 시위 등으로 기업 이미지에 큰 타격을 입을 수 있습니다. 통역사는 한국 기업에 '환경 책임 보험(bảo hiểm trách nhiệm môi trường)' 가입을 권장하고, 사고 발생 시 신속한 대응과 투명한 소통이 중요함을 강조해야 합니다. 또한 베트남은 '환경 책임'을 기업의 사회적 책임(CSR)과 연계해 평가하므로, 환경 관리를 잘하는 기업은 정부 입찰에서 가점을 받을 수 있습니다.",
            "commonMistakes": [
                {
                    "mistake": "'책임'을 'trách nhiệm'과 'nghĩa vụ' 혼용",
                    "correction": "'trách nhiệm' (책임) vs 'nghĩa vụ' (의무)",
                    "explanation": "'trách nhiệm'은 책임(liability)이고, 'nghĩa vụ'는 의무(obligation)로 법적 뉘앙스가 다릅니다."
                },
                {
                    "mistake": "'환경 배상'을 'bồi thường môi trường'으로만 표현",
                    "correction": "'bồi thường thiệt hại môi trường' (환경 피해 배상)",
                    "explanation": "'thiệt hại(피해)'를 명시해야 배상 대상이 명확해집니다."
                },
                {
                    "mistake": "한국의 환경오염피해구제법을 베트남에 그대로 적용",
                    "correction": "베트남은 환경보호법으로 통합 규정",
                    "explanation": "한국은 별도 법률이지만, 베트남은 환경보호법 내에 책임 조항이 포함되어 있습니다."
                }
            ],
            "examples": [
                {
                    "ko": "환경 오염 사고 발생 시 기업은 즉시 복구 조치를 취하고 배상해야 합니다.",
                    "vi": "Khi xảy ra sự cố ô nhiễm môi trường, doanh nghiệp phải ngay lập tức thực hiện biện pháp khắc phục và bồi thường.",
                    "situation": "formal"
                },
                {
                    "ko": "우리 회사는 환경책임 보험에 가입하여 만일의 사태에 대비하고 있습니다.",
                    "vi": "Công ty chúng tôi đã mua bảo hiểm trách nhiệm môi trường để phòng ngừa rủi ro.",
                    "situation": "formal"
                },
                {
                    "ko": "환경 문제 일으키면 여기서 사업 못 해요.",
                    "vi": "Nếu gây vấn đề môi trường thì không làm ăn được ở đây đâu.",
                    "situation": "informal"
                }
            ],
            "relatedTerms": ["danh-gia-tac-dong-moi-truong", "giay-phep-moi-truong", "xu-ly-chat-thai"]
        }
    ]

    # Filter out duplicates
    new_terms_filtered = [t for t in new_terms if t['slug'] not in existing_slugs]

    # Extend data list
    data.extend(new_terms_filtered)

    # Write back to file
    with open(file_path, 'w', encoding='utf-8') as f:
        json.dump(data, f, ensure_ascii=False, indent=2)

    print(f"✅ Successfully added {len(new_terms_filtered)} environmental law terms to legal.json")
    print(f"📊 Total terms in legal.json: {len(data)}")

    # Print added terms
    for term in new_terms_filtered:
        print(f"  - {term['slug']} ({term['korean']})")

if __name__ == "__main__":
    main()
