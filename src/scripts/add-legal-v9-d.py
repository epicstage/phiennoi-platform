#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""동물보호/환경특별법 용어 추가 (v9-d)"""
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
            "slug": "hoc-dai-dong-vat",
            "korean": "동물학대",
            "vietnamese": "Học đãi động vật",
            "hanja": "動物虐待",
            "hanjaReading": "動(움직일 동) + 物(물건 물) + 虐(학대할 학) + 待(기다릴 대)",
            "pronunciation": "동물학대",
            "meaningKo": "동물을 대상으로 정당한 사유 없이 불필요하거나 피할 수 있는 신체적 고통과 스트레스를 주는 행위를 말합니다. 통역 시 한국 동물보호법은 유기·학대·살해를 모두 처벌하며, 학대 시 3년 이하 징역 또는 3천만 원 이하 벌금, 살해 시 5년 이하 징역이며, 신고 의무와 동물보호감시원 제도가 있다는 점을 명확히 전달해야 합니다.",
            "meaningVi": "Hành vi gây đau khổ thể chất và căng thẳng không cần thiết hoặc có thể tránh được cho động vật mà không có lý do chính đáng. Luật bảo vệ động vật Hàn Quốc phạt cả bỏ rơi, học đãi, giết hại, học đãi bị phạt tù 3 năm hoặc phạt tiền đến 30 triệu won, giết hại bị phạt tù 5 năm, có nghĩa vụ báo cáo và chế độ thanh tra viên bảo vệ động vật.",
            "context": "동물학대 신고 및 처벌 절차에서 사용",
            "culturalNote": "한국은 2007년 동물보호법 제정 후 처벌이 계속 강화되고 있으며, 동물학대 영상이 SNS에서 확산되면서 사회적 관심이 높습니다. 동물보호법은 반려동물뿐 아니라 산업동물도 보호하며, 농장동물 복지 기준도 도입 중입니다. 베트남은 동물보호법이 미비하며 학대 개념이 생소합니다. 통역 시 한국의 동물 복지 수준과 처벌 강화 추세를 설명해야 합니다.",
            "commonMistakes": [
                {
                    "mistake": "đánh đập động vật",
                    "correction": "học đãi động vật (신체적 학대만이 아님)",
                    "explanation": "'때리다'는 물리적 폭력만 의미하며 방치·굶김 등 다른 학대가 누락됩니다"
                },
                {
                    "mistake": "hành hạ thú vật",
                    "correction": "học đãi động vật (법률 용어)",
                    "explanation": "'동물 괴롭힘'은 일상 표현이며 법적 용어로 부적절합니다"
                },
                {
                    "mistake": "đối xử tàn ác",
                    "correction": "học đãi động vật (동물 대상 특정)",
                    "explanation": "'잔혹하게 대하다'는 일반 표현이며 동물학대의 법적 정의가 누락됩니다"
                }
            ],
            "examples": [
                {
                    "ko": "피고인은 반려견을 2주간 먹이지 않고 방치하여 동물학대로 기소되었습니다",
                    "vi": "Bị cáo bị truy tố tội học đãi động vật vì bỏ đói chó cưng 2 tuần",
                    "situation": "formal"
                },
                {
                    "ko": "이웃집에서 개를 때리는데 신고해도 되나요?",
                    "vi": "Nhà bên cạnh đánh chó, có thể báo cáo không?",
                    "situation": "onsite"
                },
                {
                    "ko": "동물학대 목격 시 동물보호 핫라인 1577-0954로 신고하세요",
                    "vi": "Khi chứng kiến học đãi động vật hãy gọi đường dây nóng bảo vệ động vật 1577-0954",
                    "situation": "formal"
                }
            ],
            "relatedTerms": ["동물보호법", "동물유기", "동물복지", "반려동물"]
        },
        {
            "slug": "dang-ky-thu-cung",
            "korean": "반려동물등록",
            "vietnamese": "Đăng ký thú cưng",
            "hanja": "伴侶動物登錄",
            "hanjaReading": "伴(짝 반) + 侶(짝 려) + 動(움직일 동) + 物(물건 물) + 登(오를 등) + 錄(기록할 록)",
            "pronunciation": "반려동물등록",
            "meaningKo": "개를 양육하는 경우 소유자 정보와 동물 정보를 지방자치단체에 등록하는 제도입니다. 통역 시 한국은 2개월령 이상 개에 대해 등록을 의무화하며, 미등록 시 100만 원 이하 과태료, 등록 방법은 무선식별장치(마이크로칩) 또는 인식표 부착이며, 유실·유기 시 신속한 소유자 확인이 가능하다는 점을 명확히 전달해야 합니다.",
            "meaningVi": "Chế độ đăng ký thông tin chủ sở hữu và thông tin động vật lên chính quyền địa phương khi nuôi chó. Ở Hàn Quốc bắt buộc đăng ký chó từ 2 tháng tuổi trở lên, không đăng ký bị phạt đến 1 triệu won, phương thức đăng ký là gắn thiết bị nhận dạng vô tuyến (microchip) hoặc thẻ nhận dạng, khi thất lạc/bỏ rơi có thể xác nhận chủ sở hữu nhanh chóng.",
            "context": "반려동물 등록 의무 안내 및 미등록 단속 상황에서 사용",
            "culturalNote": "한국은 2014년부터 반려동물 등록을 의무화했으며, 마이크로칩 삽입이 일반화되고 있습니다. 등록률은 50% 수준으로 아직 낮아 지자체가 단속을 강화하고 있습니다. 베트남은 반려동물 등록 제도가 없어 통역 시 제도의 목적(유실 방지, 유기 책임 추적)을 설명해야 합니다.",
            "commonMistakes": [
                {
                    "mistake": "đăng ký chó",
                    "correction": "đăng ký thú cưng (반려동물)",
                    "explanation": "'개 등록'은 좁으며 반려동물의 개념을 포함해야 합니다"
                },
                {
                    "mistake": "giấy phép nuôi chó",
                    "correction": "đăng ký thú cưng (등록 vs 허가)",
                    "explanation": "'개 사육 허가'는 허가 개념이며 등록과 법적 성격이 다릅니다"
                },
                {
                    "mistake": "khai báo động vật",
                    "correction": "đăng ký thú cưng (법적 용어)",
                    "explanation": "'동물 신고'는 비공식적이며 법적 등록의 개념이 약화됩니다"
                }
            ],
            "examples": [
                {
                    "ko": "반려견 등록은 동물병원이나 동물보호센터에서 할 수 있습니다",
                    "vi": "Đăng ký thú cưng có thể làm tại bệnh viện thú y hoặc trung tâm bảo vệ động vật",
                    "situation": "formal"
                },
                {
                    "ko": "강아지 키우는데 등록 꼭 해야 하나요?",
                    "vi": "Nuôi chó con, có bắt buộc phải đăng ký không?",
                    "situation": "onsite"
                },
                {
                    "ko": "반려동물 미등록 시 100만 원 이하 과태료가 부과됩니다",
                    "vi": "Không đăng ký thú cưng bị phạt đến 1 triệu won",
                    "situation": "formal"
                }
            ],
            "relatedTerms": ["마이크로칩", "동물보호법", "유실동물", "과태료"]
        },
        {
            "slug": "thi-nghiem-dong-vat",
            "korean": "동물실험",
            "vietnamese": "Thí nghiệm động vật",
            "hanja": "動物實驗",
            "hanjaReading": "動(움직일 동) + 物(물건 물) + 實(열매 실) + 驗(시험할 험)",
            "pronunciation": "동물실험",
            "meaningKo": "교육·시험·연구 및 생물학적 제제 생산 등 과학적 목적을 위해 동물을 대상으로 실시하는 실험을 말합니다. 통역 시 한국은 실험동물법으로 규율하며, 동물실험윤리위원회 승인이 필수이고, 3R 원칙(대체·감소·개선)을 따라야 하며, 승인 없는 실험은 2년 이하 징역 또는 2천만 원 이하 벌금에 처해진다는 점을 명확히 전달해야 합니다.",
            "meaningVi": "Thí nghiệm thực hiện trên động vật cho mục đích khoa học như giáo dục, thử nghiệm, nghiên cứu và sản xuất chế phẩm sinh học. Ở Hàn Quốc được quy định bởi Luật động vật thí nghiệm, phải có phê duyệt của Ủy ban đạo đức thí nghiệm động vật, phải tuân theo nguyên tắc 3R (thay thế, giảm thiểu, cải thiện), thí nghiệm không có phê duyệt bị phạt tù 2 năm hoặc phạt tiền đến 20 triệu won.",
            "context": "연구기관 동물실험 승인 및 윤리 심사 상황에서 사용",
            "culturalNote": "한국은 2008년 실험동물법을 제정하여 동물실험을 체계적으로 관리하며, 모든 연구기관은 동물실험윤리위원회(IACUC)를 설치해야 합니다. 화장품 동물실험은 2017년부터 금지되었으며, 대체시험법 개발이 활발합니다. 베트남은 동물실험 규제가 약해 통역 시 한국의 윤리 기준을 설명해야 합니다.",
            "commonMistakes": [
                {
                    "mistake": "thử nghiệm trên động vật",
                    "correction": "thí nghiệm động vật (과학적 실험)",
                    "explanation": "'동물 대상 시험'은 일반 표현이며 과학 실험의 법적 개념이 약화됩니다"
                },
                {
                    "mistake": "dùng động vật làm thí nghiệm",
                    "correction": "thí nghiệm động vật (제도 용어)",
                    "explanation": "'동물을 실험에 사용'은 설명이며 법률 용어로 부적절합니다"
                },
                {
                    "mistake": "động vật thí nghiệm",
                    "correction": "thí nghiệm động vật (행위) vs động vật thí nghiệm (대상)",
                    "explanation": "'실험동물'은 동물 자체이며, '동물실험'은 행위로 구분됩니다"
                }
            ],
            "examples": [
                {
                    "ko": "이 연구는 동물실험윤리위원회의 승인을 받아 수행되었습니다",
                    "vi": "Nghiên cứu này được thực hiện sau khi nhận phê duyệt từ Ủy ban đạo đức thí nghiệm động vật",
                    "situation": "formal"
                },
                {
                    "ko": "동물실험 하려면 어떤 절차가 필요한가요?",
                    "vi": "Muốn thí nghiệm động vật cần thủ tục gì?",
                    "situation": "onsite"
                },
                {
                    "ko": "화장품 동물실험은 법으로 금지되어 있습니다",
                    "vi": "Thí nghiệm động vật mỹ phẩm bị cấm theo luật",
                    "situation": "formal"
                }
            ],
            "relatedTerms": ["실험동물법", "동물실험윤리위원회", "3R원칙", "대체시험법"]
        },
        {
            "slug": "dong-vat-nguy-hiem",
            "korean": "위험동물",
            "vietnamese": "Động vật nguy hiểm",
            "hanja": "危險動物",
            "hanjaReading": "危(위태할 위) + 險(험할 험) + 動(움직일 동) + 物(물건 물)",
            "pronunciation": "위험동물",
            "meaningKo": "사람의 생명·신체에 위해를 가할 우려가 있는 개나 맹수·맹금류 등을 말합니다. 통역 시 한국은 맹견 5종(도사견·아메리칸 핏불테리어·아메리칸 스태퍼드셔 테리어·스태퍼드셔 불 테리어·로트와일러)과 맹수·맹금류를 지정하며, 사육 시 허가가 필요하고 무단 사육 시 300만 원 이하 과태료, 공공장소에서 목줄·입마개 의무를 위반하면 500만 원 이하 과태료가 부과된다는 점을 명확히 전달해야 합니다.",
            "meaningVi": "Chó, thú dữ, chim săn mồi có nguy cơ gây hại cho tính mạng, thân thể con người. Ở Hàn Quốc chỉ định 5 giống chó hung dữ (Tosa, American Pit Bull Terrier, American Staffordshire Terrier, Staffordshire Bull Terrier, Rottweiler) và thú dữ, chim săn, nuôi phải có giấy phép, nuôi không phép bị phạt đến 3 triệu won, vi phạm nghĩa vụ xích dây/rọ mõm nơi công cộng bị phạt đến 5 triệu won.",
            "context": "위험동물 사육 허가 및 관리 의무 상황에서 사용",
            "culturalNote": "한국은 맹견 사고가 증가하며 2018년부터 맹견 관리를 대폭 강화했습니다. 공공장소에서 목줄 2m 이하, 입마개 착용이 의무이며, 위반 시 과태료와 함께 사고 발생 시 가중처벌됩니다. 베트남은 위험동물 규제가 약해 통역 시 한국의 엄격한 관리 기준을 설명해야 합니다.",
            "commonMistakes": [
                {
                    "mistake": "chó hung dữ",
                    "correction": "động vật nguy hiểm (개뿐만 아니라 맹수 포함)",
                    "explanation": "'사나운 개'는 개만 의미하며 맹수·맹금류가 누락됩니다"
                },
                {
                    "mistake": "động vật dữ",
                    "correction": "động vật nguy hiểm (법적 지정)",
                    "explanation": "'야생동물'은 포괄적이며 법적으로 지정된 위험동물과 다릅니다"
                },
                {
                    "mistake": "thú hoang",
                    "correction": "động vật nguy hiểm (사육 관리 대상)",
                    "explanation": "'야생동물'은 자연 상태이며 사육 관리 대상인 위험동물과 개념이 다릅니다"
                }
            ],
            "examples": [
                {
                    "ko": "위험동물을 사육하려면 지자체에 신고하고 허가를 받아야 합니다",
                    "vi": "Muốn nuôi động vật nguy hiểm phải báo cáo chính quyền địa phương và xin phép",
                    "situation": "formal"
                },
                {
                    "ko": "핏불 키우는데 입마개 꼭 해야 하나요?",
                    "vi": "Nuôi Pit Bull có bắt buộc đeo rọ mõm không?",
                    "situation": "onsite"
                },
                {
                    "ko": "맹견이 사람을 물면 소유자는 형사처벌을 받을 수 있습니다",
                    "vi": "Nếu chó hung dữ cắn người, chủ sở hữu có thể bị xử lý hình sự",
                    "situation": "formal"
                }
            ],
            "relatedTerms": ["맹견", "동물보호법", "사육허가", "과태료"]
        },
        {
            "slug": "bo-roi-dong-vat",
            "korean": "유기동물",
            "vietnamese": "Bỏ rơi động vật",
            "hanja": "遺棄動物",
            "hanjaReading": "遺(남길 유) + 棄(버릴 기) + 動(움직일 동) + 物(물건 물)",
            "pronunciation": "유기동물",
            "meaningKo": "반려동물을 버려 소유자를 알 수 없게 된 동물을 말합니다. 통역 시 한국은 동물 유기 시 3년 이하 징역 또는 3천만 원 이하 벌금에 처하며, 유기동물은 동물보호센터에서 공고 후 10일 이내 주인이 나타나지 않으면 입양·안락사되고, 반려동물 등록 시 유기 시 소유자 추적이 가능하다는 점을 명확히 전달해야 합니다.",
            "meaningVi": "Động vật thú cưng bị bỏ rơi không xác định được chủ sở hữu. Ở Hàn Quốc bỏ rơi động vật bị phạt tù 3 năm hoặc phạt tiền đến 30 triệu won, động vật bị bỏ rơi được trung tâm bảo vệ động vật công bố, nếu trong 10 ngày không có chủ sở hữu xuất hiện sẽ được cho nhận nuôi hoặc an tử, nếu đăng ký thú cưng thì khi bỏ rơi có thể truy vết chủ sở hữu.",
            "context": "유기동물 신고 및 입양 절차 상황에서 사용",
            "culturalNote": "한국은 연간 10만 마리 이상의 유기동물이 발생하며, 지자체 동물보호센터가 보호합니다. 입양률은 30% 수준이며, 안락사율을 낮추기 위해 민간 보호소와 협력합니다. 베트남은 유기동물 보호 시스템이 거의 없어 통역 시 한국의 보호센터 운영과 입양 시스템을 설명해야 합니다.",
            "commonMistakes": [
                {
                    "mistake": "chó hoang",
                    "correction": "bỏ rơi động vật (유기된 반려동물)",
                    "explanation": "'들개'는 야생화된 개이며 유기동물은 원래 반려동물이었다는 차이가 있습니다"
                },
                {
                    "mistake": "động vật lang thang",
                    "correction": "bỏ rơi động vật (소유자가 버림)",
                    "explanation": "'떠도는 동물'은 자연 발생처럼 들리며 소유자가 버렸다는 점이 누락됩니다"
                },
                {
                    "mistake": "thú cưng bị mất",
                    "correction": "bỏ rơi động vật (유기) vs thất lạc (실종)",
                    "explanation": "'잃어버린 애완동물'은 실종이며 고의적 유기와 구분됩니다"
                }
            ],
            "examples": [
                {
                    "ko": "유기동물을 발견하면 동물보호센터에 신고하세요",
                    "vi": "Khi phát hiện động vật bị bỏ rơi hãy báo cáo trung tâm bảo vệ động vật",
                    "situation": "formal"
                },
                {
                    "ko": "강아지 못 키우겠는데 어떻게 해야 하나요? 유기하면 안 되나요?",
                    "vi": "Không nuôi được chó con nữa, phải làm sao? Bỏ rơi được không?",
                    "situation": "onsite"
                },
                {
                    "ko": "반려동물 유기 시 3년 이하 징역에 처해집니다",
                    "vi": "Bỏ rơi thú cưng bị phạt tù đến 3 năm",
                    "situation": "formal"
                }
            ],
            "relatedTerms": ["동물보호센터", "입양", "안락사", "반려동물등록"]
        },
        {
            "slug": "phuc-loi-dong-vat",
            "korean": "동물복지",
            "vietnamese": "Phúc lợi động vật",
            "hanja": "動物福祉",
            "hanjaReading": "動(움직일 동) + 物(물건 물) + 福(복 복) + 祉(복 지)",
            "pronunciation": "동물복지",
            "meaningKo": "동물이 본래 습성을 유지하며 정상적으로 살 수 있도록 관리하는 것을 말합니다. 통역 시 한국은 동물복지 5대 자유(배고픔과 갈증으로부터의 자유, 불편함으로부터의 자유, 고통·질병으로부터의 자유, 정상 행동 표현의 자유, 공포·스트레스로부터의 자유)를 채택하며, 축산법에 동물복지 인증제를 도입하여 복지형 축산을 장려한다는 점을 명확히 전달해야 합니다.",
            "meaningVi": "Quản lý để động vật có thể sống bình thường giữ nguyên tập tính vốn có. Ở Hàn Quốc áp dụng 5 quyền tự do phúc lợi động vật (tự do khỏi đói khát, tự do khỏi bất tiện, tự do khỏi đau khổ/bệnh tật, tự do thể hiện hành vi bình thường, tự do khỏi sợ hãi/căng thẳng), đưa chế độ chứng nhận phúc lợi động vật vào Luật chăn nuôi để khuyến khích chăn nuôi phúc lợi.",
            "context": "동물복지 인증 및 축산 정책 논의 상황에서 사용",
            "culturalNote": "한국은 2012년부터 동물복지 축산농장 인증제를 시행하며, 산란계·돼지·육계·한육우·젖소를 대상으로 합니다. 동물복지 인증 제품은 프리미엄 가격을 받지만 시장 규모는 아직 작습니다. 베트남은 동물복지 개념이 생소하여 통역 시 5대 자유와 인증제도를 상세히 설명해야 합니다.",
            "commonMistakes": [
                {
                    "mistake": "chăm sóc động vật",
                    "correction": "phúc lợi động vật (복지 철학)",
                    "explanation": "'동물 돌봄'은 일상적 관리이며 복지 철학의 개념이 누락됩니다"
                },
                {
                    "mistake": "bảo vệ động vật",
                    "correction": "phúc lợi động vật (복지) vs bảo vệ (보호)",
                    "explanation": "'동물보호'는 학대 금지이며, '동물복지'는 적극적 삶의 질 보장으로 구분됩니다"
                },
                {
                    "mistake": "nuôi động vật tốt",
                    "correction": "phúc lợi động vật (법적·윤리적 기준)",
                    "explanation": "'잘 키우다'는 주관적이며 법적·윤리적 복지 기준의 개념이 약화됩니다"
                }
            ],
            "examples": [
                {
                    "ko": "이 농장은 동물복지 인증을 받아 닭이 넓은 공간에서 자유롭게 움직입니다",
                    "vi": "Trang trại này có chứng nhận phúc lợi động vật nên gà di chuyển tự do trong không gian rộng",
                    "situation": "formal"
                },
                {
                    "ko": "동물복지 인증 받으려면 어떤 조건이 필요한가요?",
                    "vi": "Muốn nhận chứng nhận phúc lợi động vật cần điều kiện gì?",
                    "situation": "onsite"
                },
                {
                    "ko": "동물복지 5대 자유는 국제적으로 인정받는 기준입니다",
                    "vi": "5 quyền tự do phúc lợi động vật là tiêu chuẩn được công nhận quốc tế",
                    "situation": "formal"
                }
            ],
            "relatedTerms": ["5대자유", "동물복지인증", "축산법", "복지형축산"]
        },
        {
            "slug": "sap-tuyet-chung",
            "korean": "멸종위기",
            "vietnamese": "Sắp tuyệt chủng",
            "hanja": "滅種危機",
            "hanjaReading": "滅(멸할 멸) + 種(씨 종) + 危(위태할 위) + 機(틀 기)",
            "pronunciation": "멸종위기",
            "meaningKo": "야생생물이 생존에 위협을 받아 개체 수가 현저히 감소하여 멸종될 위험에 처한 상태를 말합니다. 통역 시 한국은 야생생물법으로 멸종위기 야생생물 I급(267종)과 II급(멸종위기종)을 지정하며, 포획·채취·훼손 시 5년 이하 징역 또는 5천만 원 이하 벌금, 국제적으로 CITES 협약을 준수한다는 점을 명확히 전달해야 합니다.",
            "meaningVi": "Trạng thái sinh vật hoang dã bị đe dọa sống còn, số lượng cá thể giảm đáng kể và có nguy cơ tuyệt chủng. Ở Hàn Quốc Luật sinh vật hoang dã chỉ định sinh vật hoang dã sắp tuyệt chủng cấp I (267 loài) và cấp II, bắt giữ/thu hái/phá hoại bị phạt tù 5 năm hoặc phạt tiền đến 50 triệu won, tuân thủ Công ước CITES quốc tế.",
            "context": "멸종위기종 보호 및 밀수 단속 상황에서 사용",
            "culturalNote": "한국은 수달·사향노루·황새 등 267종을 멸종위기종으로 지정하여 보호하며, 서식지 훼손도 처벌합니다. 밀수되는 호랑이 뼈·곰 쓸개 등 야생동물 제품 단속도 강화하고 있습니다. 베트남은 생물 다양성이 높으나 밀렵·밀수가 심각해 통역 시 국제 협약 준수와 처벌 수위를 설명해야 합니다.",
            "commonMistakes": [
                {
                    "mistake": "động vật quý hiếm",
                    "correction": "sắp tuyệt chủng (멸종 위험)",
                    "explanation": "'희귀동물'은 수가 적은 것이며 멸종 위험의 긴박성이 누락됩니다"
                },
                {
                    "mistake": "sinh vật nguy cấp",
                    "correction": "sắp tuyệt chủng (법적 지정)",
                    "explanation": "'위급 생물'은 모호하며 법적으로 지정된 멸종위기종 개념이 약화됩니다"
                },
                {
                    "mistake": "loài đang biến mất",
                    "correction": "sắp tuyệt chủng (공식 용어)",
                    "explanation": "'사라지는 종'은 일상 표현이며 법률 용어로 부적절합니다"
                }
            ],
            "examples": [
                {
                    "ko": "호랑이는 멸종위기 야생생물 I급으로 보호받고 있습니다",
                    "vi": "Hổ được bảo vệ như sinh vật hoang dã sắp tuyệt chủng cấp I",
                    "situation": "formal"
                },
                {
                    "ko": "멸종위기종 포획하면 어떻게 되나요?",
                    "vi": "Nếu bắt loài sắp tuyệt chủng thì sao?",
                    "situation": "onsite"
                },
                {
                    "ko": "멸종위기종 밀수는 국제 범죄로 엄중히 처벌됩니다",
                    "vi": "Buôn lậu loài sắp tuyệt chủng là tội phạm quốc tế, bị phạt nghiêm khắc",
                    "situation": "formal"
                }
            ],
            "relatedTerms": ["야생생물법", "CITES", "서식지보호", "밀렵"]
        },
        {
            "slug": "dong-vat-hoang-da",
            "korean": "야생동물",
            "vietnamese": "Động vật hoang dã",
            "hanja": "野生動物",
            "hanjaReading": "野(들 야) + 生(날 생) + 動(움직일 동) + 物(물건 물)",
            "pronunciation": "야생동물",
            "meaningKo": "산·들·강·바다 등 자연 상태에서 서식하는 동물을 말합니다. 통역 시 한국은 야생생물법으로 야생동물의 포획·사육·거래를 규제하며, 무단 포획 시 3년 이하 징역 또는 3천만 원 이하 벌금, 유해 야생동물(멧돼지·고라니 등)은 허가 후 포획 가능하며, 조류독감 등 질병 관리도 포함된다는 점을 명확히 전달해야 합니다.",
            "meaningVi": "Động vật sống trong tự nhiên như núi, đồng, sông, biển. Ở Hàn Quốc Luật sinh vật hoang dã quy định bắt giữ, nuôi, buôn bán động vật hoang dã, bắt giữ không phép bị phạt tù 3 năm hoặc phạt tiền đến 30 triệu won, động vật hoang dã có hại (lợn rừng, nai) có thể bắt sau khi xin phép, cũng bao gồm quản lý dịch bệnh như cúm gia cầm.",
            "context": "야생동물 보호 및 유해동물 포획 허가 상황에서 사용",
            "culturalNote": "한국은 야생동물과 인간의 접촉이 증가하며 갈등이 많아지고 있습니다. 멧돼지·고라니는 농작물 피해를 주어 유해동물로 관리되며, 조수보호법에 따라 허가 후 포획합니다. 야생동물 구조·치료 시스템도 운영 중입니다. 베트남은 야생동물 밀렵이 심각해 통역 시 한국의 보호 체계를 설명해야 합니다.",
            "commonMistakes": [
                {
                    "mistake": "thú rừng",
                    "correction": "động vật hoang dã (포괄적)",
                    "explanation": "'숲 짐승'은 육상 포유류만 연상되며 조류·어류·파충류가 누락됩니다"
                },
                {
                    "mistake": "động vật tự nhiên",
                    "correction": "động vật hoang dã (야생 상태)",
                    "explanation": "'자연동물'은 모호하며 야생 상태의 의미가 명확하지 않습니다"
                },
                {
                    "mistake": "thú dữ",
                    "correction": "động vật hoang dã (야생) vs thú dữ (맹수)",
                    "explanation": "'맹수'는 사나운 동물만 의미하며 모든 야생동물을 포함하지 못합니다"
                }
            ],
            "examples": [
                {
                    "ko": "야생동물을 무단으로 포획하면 형사처벌을 받습니다",
                    "vi": "Bắt động vật hoang dã không phép sẽ bị xử lý hình sự",
                    "situation": "formal"
                },
                {
                    "ko": "다친 새를 발견했는데 어떻게 해야 하나요?",
                    "vi": "Phát hiện chim bị thương, phải làm sao?",
                    "situation": "onsite"
                },
                {
                    "ko": "멧돼지는 유해 야생동물로 지정되어 포획 허가를 받을 수 있습니다",
                    "vi": "Lợn rừng được chỉ định là động vật hoang dã có hại, có thể xin phép bắt giữ",
                    "situation": "formal"
                }
            ],
            "relatedTerms": ["야생생물법", "유해동물", "동물구조", "조수보호"]
        },
        {
            "slug": "bao-ton-he-sinh-thai",
            "korean": "생태계보전",
            "vietnamese": "Bảo tồn hệ sinh thái",
            "hanja": "生態系保全",
            "hanjaReading": "生(날 생) + 態(모습 태) + 系(맬 계) + 保(지킬 보) + 全(온전할 전)",
            "pronunciation": "생태계보전",
            "meaningKo": "생물과 그 서식환경을 체계적으로 보존·관리하여 생태계의 균형을 유지하는 것을 말합니다. 통역 시 한국은 자연환경보전법으로 생태·경관보전지역을 지정하고, 생태계 훼손 행위를 처벌하며(5년 이하 징역 또는 5천만 원 이하 벌금), 환경영향평가를 통해 개발 사업의 생태계 영향을 사전 검토한다는 점을 명확히 전달해야 합니다.",
            "meaningVi": "Bảo tồn, quản lý có hệ thống sinh vật và môi trường sống của chúng để duy trì cân bằng hệ sinh thái. Ở Hàn Quốc Luật bảo tồn môi trường tự nhiên chỉ định khu vực bảo tồn sinh thái và cảnh quan, phạt hành vi phá hoại hệ sinh thái (tù 5 năm hoặc phạt tiền đến 50 triệu won), thông qua đánh giá tác động môi trường kiểm tra trước ảnh hưởng hệ sinh thái của dự án phát triển.",
            "context": "생태계 보호 정책 및 환경영향평가 상황에서 사용",
            "culturalNote": "한국은 1990년대부터 생태계보전 정책을 강화하며, DMZ·습지·갯벌 등을 보전지역으로 지정했습니다. 4대강 사업 등 개발과 보전의 갈등이 있으며, 최근 기후변화로 생태계 보전의 중요성이 커지고 있습니다. 베트남도 생물 다양성이 높으나 개발 압력이 강해 통역 시 한국의 보전 정책을 설명해야 합니다.",
            "commonMistakes": [
                {
                    "mistake": "bảo vệ môi trường",
                    "correction": "bảo tồn hệ sinh thái (생태계 중심)",
                    "explanation": "'환경보호'는 포괄적이며 생태계의 특수성이 약화됩니다"
                },
                {
                    "mistake": "giữ gìn thiên nhiên",
                    "correction": "bảo tồn hệ sinh thái (체계적 관리)",
                    "explanation": "'자연 보존'은 일반 표현이며 생태계의 체계적 보전 개념이 누락됩니다"
                },
                {
                    "mistake": "bảo tồn sinh vật",
                    "correction": "bảo tồn hệ sinh thái (생물 + 환경)",
                    "explanation": "'생물 보존'은 생물만 의미하며 서식환경이 제외됩니다"
                }
            ],
            "examples": [
                {
                    "ko": "이 지역은 생태·경관보전지역으로 지정되어 개발이 제한됩니다",
                    "vi": "Khu vực này được chỉ định là khu bảo tồn sinh thái và cảnh quan nên hạn chế phát triển",
                    "situation": "formal"
                },
                {
                    "ko": "습지를 매립하면 생태계보전법 위반인가요?",
                    "vi": "Lấp đất ngập nước có vi phạm Luật bảo tồn hệ sinh thái không?",
                    "situation": "onsite"
                },
                {
                    "ko": "대규모 개발 사업은 환경영향평가에서 생태계 영향을 검토합니다",
                    "vi": "Dự án phát triển quy mô lớn phải kiểm tra ảnh hưởng hệ sinh thái trong đánh giá tác động môi trường",
                    "situation": "formal"
                }
            ],
            "relatedTerms": ["자연환경보전법", "환경영향평가", "보전지역", "생물다양성"]
        },
        {
            "slug": "cong-vien-tu-nhien",
            "korean": "자연공원",
            "vietnamese": "Công viên tự nhiên",
            "hanja": "自然公園",
            "hanjaReading": "自(스스로 자) + 然(그러할 연) + 公(공평할 공) + 園(동산 원)",
            "pronunciation": "자연공원",
            "meaningKo": "자연 생태계와 자연경관 및 문화경관을 보전하고 지속 가능한 이용을 도모하기 위해 지정·관리하는 공원을 말합니다. 통역 시 한국은 자연공원법으로 국립공원·도립공원·군립공원을 구분하며, 공원 내 행위 제한(건축·벌목·채취 등)이 있고, 위반 시 5년 이하 징역 또는 5천만 원 이하 벌금에 처해진다는 점을 명확히 전달해야 합니다.",
            "meaningVi": "Công viên được chỉ định và quản lý để bảo tồn hệ sinh thái tự nhiên, cảnh quan tự nhiên và văn hóa, thúc đẩy sử dụng bền vững. Ở Hàn Quốc Luật công viên tự nhiên phân chia công viên quốc gia, tỉnh, quận, có hạn chế hành vi trong công viên (xây dựng, chặt cây, thu hái), vi phạm bị phạt tù 5 năm hoặc phạt tiền đến 50 triệu won.",
            "context": "자연공원 관리 및 행위 제한 안내 상황에서 사용",
            "culturalNote": "한국은 22개 국립공원(지리산·설악산·한라산 등)을 지정하여 환경부가 관리하며, 탐방객 수는 연간 4천만 명이 넘습니다. 과잉 이용으로 훼손이 우려되어 탐방 예약제·케이블카 철거 등 보전 정책을 강화하고 있습니다. 베트남도 국립공원이 있으나 관리가 약해 통역 시 한국의 엄격한 규제를 설명해야 합니다.",
            "commonMistakes": [
                {
                    "mistake": "công viên quốc gia",
                    "correction": "công viên tự nhiên (포괄) - quốc gia là một loại",
                    "explanation": "'국립공원'은 자연공원의 한 종류이며 전체를 대표하지 못합니다"
                },
                {
                    "mistake": "khu du lịch",
                    "correction": "công viên tự nhiên (보전 목적)",
                    "explanation": "'관광지'는 이용 중심이며 자연공원의 보전 목적이 누락됩니다"
                },
                {
                    "mistake": "vườn quốc gia",
                    "correction": "công viên tự nhiên (법적 용어)",
                    "explanation": "'국가 정원'은 비공식적이며 법률 용어로 부적절합니다"
                }
            ],
            "examples": [
                {
                    "ko": "지리산 국립공원에서는 야생화 채취가 금지되어 있습니다",
                    "vi": "Trong công viên quốc gia Jirisan cấm thu hái hoa dại",
                    "situation": "formal"
                },
                {
                    "ko": "국립공원에서 텐트 치면 안 되나요?",
                    "vi": "Trong công viên quốc gia không được dựng lều à?",
                    "situation": "onsite"
                },
                {
                    "ko": "자연공원 내 무단 건축 시 형사처벌을 받습니다",
                    "vi": "Xây dựng không phép trong công viên tự nhiên sẽ bị xử lý hình sự",
                    "situation": "formal"
                }
            ],
            "relatedTerms": ["국립공원", "자연공원법", "생태계보전", "환경부"]
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
    print(f"✅ Added {len(filtered)} terms (동물보호/환경특별법). Total: {len(data)}")

if __name__ == '__main__':
    main()
