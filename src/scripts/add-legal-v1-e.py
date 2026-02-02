#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
지적재산권/특허 전문용어 추가 스크립트
Theme: Intellectual Property/Patents (10 terms)
Quality: Tier S (90+ points)
"""

import json
import os

def main():
    # 1. 파일 경로 설정
    file_path = os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', 'data', 'terms', 'legal.json')

    # 2. 기존 데이터 로드
    with open(file_path, 'r', encoding='utf-8') as f:
        data = json.load(f)  # data is a LIST

    # 3. 기존 slug 추출
    existing_slugs = {t['slug'] for t in data}

    # 4. 새 용어 정의
    new_terms = [
        {
            "slug": "so-huu-tri-tue",
            "korean": "지적재산권",
            "vietnamese": "sở hữu trí tuệ",
            "hanja": "知的財産權",
            "hanjaReading": "知(알 지) + 的(과녁 적) + 財(재물 재) + 産(날 산) + 權(권세 권)",
            "pronunciation": "쏘 흐우 찌 뜨에",
            "meaningKo": "인간의 지적 창작물에 대한 법적 권리. 베트남에서는 'sở hữu trí tuệ'로 표현하며, 한국의 '지재권'보다 포괄적인 의미로 사용됩니다. 통역 시 특허, 상표, 저작권 등 구체적 권리를 명시해야 오해를 방지할 수 있습니다. 베트남 지재권법(Luật Sở hữu trí tuệ 2005, 2019년 개정)과 한국 지재권법의 보호 범위 차이를 이해하고 통역해야 합니다. 특히 베트남은 전통 지식(kiến thức truyền thống)도 지재권으로 보호하는 점이 한국과 다릅니다.",
            "meaningVi": "Quyền pháp lý đối với các sáng tạo trí tuệ của con người. Bao gồm bằng sáng chế, nhãn hiệu, quyền tác giả. Luật Sở hữu trí tuệ Việt Nam (2005, sửa đổi 2019) bảo vệ cả kiến thức truyền thống và di sản văn hóa phi vật thể, điểm khác biệt so với luật Hàn Quốc.",
            "context": "계약서, 기술이전 협상, 분쟁 조정",
            "culturalNote": "한국은 지재권을 산업 경쟁력의 핵심으로 보는 반면, 베트남은 전통 지식과 문화유산 보호에 더 중점을 둡니다. 베트남 통역사는 'sở hữu trí tuệ truyền thống'(전통 지식 재산권) 개념을 이해해야 하며, 한국 기업이 베트남 전통 문양이나 지식을 무단 사용하지 않도록 주의를 환기시켜야 합니다. 베트남에서는 공동체 지재권(quyền sở hữu trí tuệ cộng đồng) 개념도 인정됩니다.",
            "commonMistakes": [
                {
                    "mistake": "지재권을 'quyền tài sản trí tuệ'로 번역",
                    "correction": "sở hữu trí tuệ",
                    "explanation": "'quyền tài sản trí tuệ'는 문법적으로 어색하며, 공식 용어는 'sở hữu trí tuệ'입니다."
                },
                {
                    "mistake": "IP를 그대로 'IP'로 사용",
                    "correction": "sở hữu trí tuệ (SHTT) 또는 풀어서 설명",
                    "explanation": "베트남 법률 문서에서는 약어보다 정식 명칭 사용이 원칙입니다."
                },
                {
                    "mistake": "전통 지식 보호를 생략하고 통역",
                    "correction": "베트남법은 kiến thức truyền thống도 보호 대상임을 명시",
                    "explanation": "한국과 달리 베트남은 전통 지식 보호 조항이 강력하므로 계약 시 반드시 언급해야 합니다."
                }
            ],
            "examples": [
                {
                    "ko": "이 기술의 지적재산권은 당사가 보유합니다.",
                    "vi": "Quyền sở hữu trí tuệ đối với công nghệ này thuộc về công ty chúng tôi.",
                    "situation": "formal"
                },
                {
                    "ko": "지재권 침해 여부를 검토해 주세요.",
                    "vi": "Vui lòng xem xét xem có xâm phạm quyền sở hữu trí tuệ hay không.",
                    "situation": "formal"
                },
                {
                    "ko": "베트남 지재권법에 따라 전통 문양도 보호받나요?",
                    "vi": "Theo Luật Sở hữu trí tuệ Việt Nam, hoa văn truyền thống có được bảo vệ không?",
                    "situation": "informal"
                }
            ],
            "relatedTerms": ["bang-sang-che", "nhan-hieu", "quyen-tac-gia", "xam-pham-quyen"]
        },
        {
            "slug": "bang-sang-che",
            "korean": "특허",
            "vietnamese": "bằng sáng chế",
            "hanja": "特許",
            "hanjaReading": "特(특별할 특) + 許(허락할 허)",
            "pronunciation": "방 상 쩨",
            "meaningKo": "발명에 대한 독점적 권리를 부여하는 제도. 베트남에서는 'bằng sáng chế'(발명 증서)로 표현하며, 한국의 '특허'보다 증서/인증서의 의미가 강합니다. 통역 시 'bằng độc quyền sáng chế'(독점권 증서)로 풀어 설명하면 한국인이 이해하기 쉽습니다. 베트남 특허법은 의약품 특허에 강제실시권(cấp phép bắt buộc) 조항이 있어 한국과 다르므로, 제약 분야 통역 시 주의가 필요합니다. 베트남 특허 출원은 국가 지식재산청(Cục Sở hữu trí tuệ)에서 처리합니다.",
            "meaningVi": "Chứng nhận quyền độc quyền đối với phát minh. Do Cục Sở hữu trí tuệ cấp, bảo hộ 20 năm kể từ ngày nộp đơn. Luật Sở hữu trí tuệ Việt Nam quy định chế độ cấp phép bắt buộc đối với thuốc chữa bệnh trong trường hợp khẩn cấp quốc gia.",
            "context": "기술이전, R&D 계약, 투자 협상",
            "culturalNote": "한국은 특허를 '권리'로 인식하는 반면, 베트남은 '증서(bằng)'로 표현해 문서/인증의 개념이 강합니다. 베트nam 특허 심사는 한국(평균 18개월)보다 느린 편(평균 36개월)이므로, 계약 시 심사 기간을 고려해야 합니다. 베트남에서는 특허 출원 전 기술 공개가 신규성을 상실시키므로, NDA(Hợp đồng bảo mật) 체결이 필수입니다.",
            "commonMistakes": [
                {
                    "mistake": "특허를 'giấy phép'로 번역",
                    "correction": "bằng sáng chế",
                    "explanation": "'giấy phép'는 일반 허가증이고, 특허는 'bằng sáng chế'가 법률 용어입니다."
                },
                {
                    "mistake": "특허권을 'quyền bằng sáng chế'로 표현",
                    "correction": "quyền sáng chế 또는 quyền độc quyền sáng chế",
                    "explanation": "'bằng'은 증서이므로 권리 표현 시 생략하거나 '독점권'을 추가합니다."
                },
                {
                    "mistake": "강제실시권 조항을 통역 시 생략",
                    "correction": "베트남은 의약품에 cấp phép bắt buộc 가능함을 명시",
                    "explanation": "제약사 계약 시 강제실시권 조항이 계약에 영향을 주므로 반드시 통역해야 합니다."
                }
            ],
            "examples": [
                {
                    "ko": "이 기술은 한국과 베트남에서 특허 등록되었습니다.",
                    "vi": "Công nghệ này đã được cấp bằng sáng chế tại Hàn Quốc và Việt Nam.",
                    "situation": "formal"
                },
                {
                    "ko": "특허 심사에 얼마나 걸리나요?",
                    "vi": "Thẩm định bằng sáng chế mất bao lâu?",
                    "situation": "informal"
                },
                {
                    "ko": "의약품 특허에 강제실시권이 적용될 수 있습니다.",
                    "vi": "Đối với bằng sáng chế thuốc có thể áp dụng chế độ cấp phép bắt buộc.",
                    "situation": "formal"
                }
            ],
            "relatedTerms": ["so-huu-tri-tue", "don-dang-ky-bang-sang-che", "quyen-doc-quyen", "cap-phep-bat-buoc"]
        },
        {
            "slug": "nhan-hieu",
            "korean": "상표",
            "vietnamese": "nhãn hiệu",
            "hanja": "商標",
            "hanjaReading": "商(장사 상) + 標(표 표)",
            "pronunciation": "년 히에우",
            "meaningKo": "상품이나 서비스를 식별하는 표지. 베트남에서는 'nhãn hiệu'로 표현하며, 한자어 '標號'에서 유래했습니다. 통역 시 'thương hiệu'(브랜드)와 구분해야 하며, 'nhãn hiệu'는 법적 등록 상표, 'thương hiệu'는 일반 브랜드 개념입니다. 베트남 상표법은 색채상표, 입체상표, 소리상표도 보호하지만, 냄새상표는 아직 인정하지 않습니다. 상표 등록은 국가 지식재산청에 출원하며, 10년마다 갱신이 필요합니다. 한국과 달리 베트남은 상표 선사용주의가 아닌 선출원주의(đăng ký trước)를 엄격히 적용합니다.",
            "meaningVi": "Dấu hiệu để phân biệt hàng hóa, dịch vụ của cá nhân, tổ chức. Bao gồm chữ, hình ảnh, màu sắc, âm thanh, hình ba chiều. Đăng ký tại Cục Sở hữu trí tuệ, hiệu lực 10 năm và có thể gia hạn. Việt Nam áp dụng nguyên tắc đăng ký trước, không công nhận quyền theo thói quen sử dụng.",
            "context": "브랜드 계약, 프랜차이즈, 라이선스",
            "culturalNote": "한국은 상표를 마케팅 자산으로 중시하는 반면, 베트남은 법적 보호 수단으로 우선 인식합니다. 베트남에서는 미등록 상표(nhãn hiệu chưa đăng ký)는 법적 보호를 거의 받지 못하므로, 한국 기업이 베트남 진출 시 반드시 사전 등록을 권장해야 합니다. 베트남에서는 유명 상표 모방(nhái nhãn hiệu nổi tiếng)이 많아 분쟁이 잦으므로, 계약서에 상표권 침해 책임 조항을 명확히 해야 합니다.",
            "commonMistakes": [
                {
                    "mistake": "상표를 'thương hiệu'로 번역",
                    "correction": "nhãn hiệu (법률), thương hiệu (마케팅)",
                    "explanation": "법률 문서에서는 'nhãn hiệu', 일반 문서에서는 'thương hiệu'를 사용합니다."
                },
                {
                    "mistake": "미등록 상표도 보호받는다고 통역",
                    "correction": "베트남은 선출원주의로 등록 상표만 보호됨을 명시",
                    "explanation": "한국과 달리 베트남은 관습적 사용만으로는 상표권을 주장할 수 없습니다."
                },
                {
                    "mistake": "냄새상표 등록 가능하다고 설명",
                    "correction": "베트남은 아직 냄새상표 미인정",
                    "explanation": "한국은 2016년부터 냄새상표를 인정하지만 베트남은 아직 불가능합니다."
                }
            ],
            "examples": [
                {
                    "ko": "상표 등록을 먼저 하고 베트남 시장에 진출하세요.",
                    "vi": "Hãy đăng ký nhãn hiệu trước khi thâm nhập thị trường Việt Nam.",
                    "situation": "formal"
                },
                {
                    "ko": "이 상표는 한국에서 유명하지만 베트남에서는 미등록 상태입니다.",
                    "vi": "Nhãn hiệu này nổi tiếng ở Hàn Quốc nhưng chưa đăng ký tại Việt Nam.",
                    "situation": "informal"
                },
                {
                    "ko": "상표권 침해 시 손해배상 청구가 가능합니다.",
                    "vi": "Trường hợp xâm phạm quyền nhãn hiệu có thể yêu cầu bồi thường thiệt hại.",
                    "situation": "formal"
                }
            ],
            "relatedTerms": ["so-huu-tri-tue", "thuong-hieu", "dang-ky-nhan-hieu", "xam-pham-nhan-hieu"]
        },
        {
            "slug": "quyen-tac-gia",
            "korean": "저작권",
            "vietnamese": "quyền tác giả",
            "hanja": "著作權",
            "hanjaReading": "著(지을 저) + 作(지을 작) + 權(권세 권)",
            "pronunciation": "꾸엔 딱 쟈",
            "meaningKo": "문학, 예술, 학술 작품에 대한 창작자의 권리. 베트남에서는 'quyền tác giả'(작가의 권리)로 표현하며, 한국의 '저작권'보다 창작자 중심 개념이 강합니다. 통역 시 'quyền sở hữu tác phẩm'(작품 소유권)과 혼동하지 않도록 주의해야 합니다. 베트남 저작권법은 저작인격권(quyền nhân thân)과 재산권(quyền tài sản)을 구분하며, 저작인격권은 양도 불가능합니다. 저작권 보호 기간은 저작자 사망 후 50년(한국 70년)으로 한국보다 짧습니다. 등록 없이도 창작 시점부터 자동 보호됩니다.",
            "meaningVi": "Quyền của người sáng tạo đối với tác phẩm văn học, nghệ thuật, khoa học. Bao gồm quyền nhân thân (không chuyển nhượng) và quyền tài sản (có thể chuyển nhượng). Bảo hộ 50 năm sau khi tác giả mất, tự động có hiệu lực từ khi sáng tạo mà không cần đăng ký.",
            "context": "출판 계약, 소프트웨어 라이선스, 콘텐츠 제작",
            "culturalNote": "한국은 저작권을 경제적 자산으로 보는 경향이 강한 반면, 베트남은 창작자의 인격권 보호를 더 중시합니다. 베트남에서는 저작인격권(성명표시권, 동일성유지권)을 양도하거나 포기할 수 없으므로, 한국 기업이 전면 매수 계약을 체결할 때 이를 명확히 설명해야 합니다. 베트남에서는 저작권 침해 시 형사처벌(최대 7년)이 가능하여 한국보다 처벌이 강한 편입니다.",
            "commonMistakes": [
                {
                    "mistake": "저작권을 'quyền sở hữu tác phẩm'로 번역",
                    "correction": "quyền tác giả",
                    "explanation": "'quyền sở hữu'는 일반 소유권이고, 저작권은 'quyền tác giả'가 법률 용어입니다."
                },
                {
                    "mistake": "저작인격권을 양도 가능하다고 통역",
                    "correction": "베트남법은 quyền nhân thân 양도 불가",
                    "explanation": "한국은 일부 양도 가능하지만 베트남은 절대 불가능하므로 계약서 작성 시 주의해야 합니다."
                },
                {
                    "mistake": "보호 기간을 70년으로 통역",
                    "correction": "베트남은 사망 후 50년",
                    "explanation": "한국(70년)과 다르므로 국제 계약 시 명확히 해야 합니다."
                }
            ],
            "examples": [
                {
                    "ko": "이 소프트웨어의 저작권은 개발사에 귀속됩니다.",
                    "vi": "Quyền tác giả đối với phần mềm này thuộc về công ty phát triển.",
                    "situation": "formal"
                },
                {
                    "ko": "저작인격권은 양도할 수 없습니다.",
                    "vi": "Quyền nhân thân của tác giả không thể chuyển nhượng.",
                    "situation": "formal"
                },
                {
                    "ko": "저작권 침해로 형사고소가 가능한가요?",
                    "vi": "Có thể khởi kiện hình sự vì xâm phạm quyền tác giả không?",
                    "situation": "informal"
                }
            ],
            "relatedTerms": ["so-huu-tri-tue", "quyen-nhan-than", "quyen-tai-san", "xam-pham-tac-gia"]
        },
        {
            "slug": "kieu-dang-cong-nghiep",
            "korean": "디자인권",
            "vietnamese": "kiểu dáng công nghiệp",
            "hanja": None,
            "hanjaReading": None,
            "pronunciation": "끼에우 장 꽁 응이엡",
            "meaningKo": "제품의 외관 디자인에 대한 권리. 베트남에서는 'kiểu dáng công nghiệp'(공업 형태)로 표현하며, 한국의 '디자인권'보다 산업 응용성이 강조됩니다. 통역 시 'thiết kế công nghiệp'(공업 디자인)과 혼용할 수 있으나, 법률 문서에서는 'kiểu dáng công nghiệp'이 정확한 용어입니다. 베트남 디자인권 보호는 등록 후 5년이며, 최대 2회 갱신(총 15년)이 가능합니다. 한국(최대 20년)보다 짧으므로 계약 시 주의가 필요합니다. 신규성, 창조성, 산업 응용성이 등록 요건이며, 공개 후 6개월 이내 출원 시 신규성 상실 예외가 인정됩니다.",
            "meaningVi": "Quyền đối với hình dáng bên ngoài của sản phẩm công nghiệp. Bảo hộ 5 năm kể từ ngày cấp văn bằng, có thể gia hạn 2 lần (tối đa 15 năm). Yêu cầu tính mới, tính sáng tạo và khả năng áp dụng công nghiệp. Công khai trước 6 tháng vẫn được bảo hộ nếu do chính người nộp đơn thực hiện.",
            "context": "제품 개발, 디자인 계약, 모방 분쟁",
            "culturalNote": "한국은 디자인을 창작물로 인식하는 반면, 베트남은 산업 응용 수단으로 우선 인식합니다. 베트남에서는 부분 디자인(kiểu dáng bộ phận) 등록이 한국보다 까다로워, 전체 제품 디자인으로 출원하는 것이 유리합니다. 베트남 시장에서는 디자인 모방품이 많아 분쟁이 잦으므로, 한국 기업이 진출 시 신속하게 디자인권 등록을 권장해야 합니다. 베트남에서는 미등록 디자인은 법적 보호가 거의 없습니다.",
            "commonMistakes": [
                {
                    "mistake": "디자인권을 'quyền thiết kế'로 번역",
                    "correction": "kiểu dáng công nghiệp 또는 quyền kiểu dáng công nghiệp",
                    "explanation": "'quyền thiết kế'는 일반 디자인이고, 법률 용어는 'kiểu dáng công nghiệp'입니다."
                },
                {
                    "mistake": "보호 기간을 20년으로 통역",
                    "correction": "베트남은 최대 15년 (5년 + 갱신 2회)",
                    "explanation": "한국(20년)과 다르므로 계약 시 명확히 해야 합니다."
                },
                {
                    "mistake": "부분 디자인 등록이 쉽다고 설명",
                    "correction": "베트남은 부분 디자인 등록이 까다로움",
                    "explanation": "한국보다 전체 제품 디자인 출원이 유리하므로 출원 전략을 조정해야 합니다."
                }
            ],
            "examples": [
                {
                    "ko": "이 제품의 디자인권은 베트남에 등록되어 있습니다.",
                    "vi": "Kiểu dáng công nghiệp của sản phẩm này đã được đăng ký tại Việt Nam.",
                    "situation": "formal"
                },
                {
                    "ko": "디자인권 보호 기간을 갱신할 수 있나요?",
                    "vi": "Có thể gia hạn thời hạn bảo hộ kiểu dáng công nghiệp không?",
                    "situation": "informal"
                },
                {
                    "ko": "부분 디자인으로 출원하면 거절될 수 있습니다.",
                    "vi": "Nếu nộp đơn kiểu dáng bộ phận có thể bị từ chối.",
                    "situation": "formal"
                }
            ],
            "relatedTerms": ["so-huu-tri-tue", "thiet-ke-cong-nghiep", "dang-ky-kieu-dang", "bao-ho-kieu-dang"]
        },
        {
            "slug": "bi-mat-kinh-doanh",
            "korean": "영업비밀",
            "vietnamese": "bí mật kinh doanh",
            "hanja": "營業秘密",
            "hanjaReading": "營(경영할 영) + 業(업 업) + 秘(숨길 비) + 密(빽빽할 밀)",
            "pronunciation": "비 멋 낀 조안",
            "meaningKo": "경쟁 우위를 제공하는 비공개 정보. 베트남에서는 'bí mật kinh doanh'로 표현하며, 한국의 '영업비밀'과 거의 동일한 법적 개념입니다. 통역 시 'thông tin mật'(기밀 정보)과 구분해야 하며, 영업비밀은 경제적 가치가 있는 비밀에 한정됩니다. 베트남 영업비밀 보호는 부정경쟁방지법(Luật Cạnh tranh)과 지식재산법에 규정되어 있으며, 비밀 유지 노력(nỗ lực giữ bí mật)이 보호 요건입니다. 한국과 달리 베트남은 영업비밀 침해 시 형사처벌(최대 12년)이 강력하여, 이직 시 NDA 위반이 심각한 범죄가 될 수 있습니다.",
            "meaningVi": "Thông tin không được công khai, có giá trị kinh tế và được chủ sở hữu nỗ lực giữ bí mật. Bảo vệ theo Luật Cạnh tranh và Luật Sở hữu trí tuệ. Vi phạm có thể bị xử phạt hình sự tối đa 12 năm tù. Bao gồm công thức, quy trình, danh sách khách hàng, chiến lược kinh doanh.",
            "context": "NDA, 이직 분쟁, 기술이전",
            "culturalNote": "한국은 영업비밀을 민사 분쟁으로 주로 다루는 반면, 베트남은 형사처벌을 적극 활용합니다. 베트남에서는 직원 이직 시 영업비밀 유출 우려가 크므로, 한국 기업이 베트남 직원 채용 시 이전 회사와의 NDA 위반 여부를 반드시 확인해야 합니다. 베트남에서는 영업비밀 침해 입증이 한국보다 어려우므로, 계약서에 구체적 비밀 항목과 보호 조치를 명시하는 것이 중요합니다.",
            "commonMistakes": [
                {
                    "mistake": "영업비밀을 'thông tin bí mật'로 번역",
                    "correction": "bí mật kinh doanh",
                    "explanation": "'thông tin bí mật'는 일반 기밀이고, 경제적 가치가 있는 것은 'bí mật kinh doanh'입니다."
                },
                {
                    "mistake": "형사처벌이 약하다고 통역",
                    "correction": "베트남은 최대 12년 징역으로 매우 강력",
                    "explanation": "한국보다 형사처벌이 강하므로 NDA 위반의 심각성을 강조해야 합니다."
                },
                {
                    "mistake": "비밀 유지 노력 없이도 보호된다고 설명",
                    "correction": "nỗ lực giữ bí mật 입증 필수",
                    "explanation": "베트남법은 비밀 유지 조치를 취했음을 입증해야 보호받으므로 계약서에 명시해야 합니다."
                }
            ],
            "examples": [
                {
                    "ko": "이직 시 영업비밀을 유출하면 형사처벌을 받을 수 있습니다.",
                    "vi": "Khi chuyển việc, nếu tiết lộ bí mật kinh doanh có thể bị xử lý hình sự.",
                    "situation": "formal"
                },
                {
                    "ko": "고객 리스트는 영업비밀로 보호됩니다.",
                    "vi": "Danh sách khách hàng được bảo vệ như bí mật kinh doanh.",
                    "situation": "formal"
                },
                {
                    "ko": "영업비밀 보호를 위해 어떤 조치를 취하셨나요?",
                    "vi": "Anh đã có biện pháp gì để bảo vệ bí mật kinh doanh?",
                    "situation": "informal"
                }
            ],
            "relatedKeys": ["so-huu-tri-tue", "hop-dong-bao-mat", "tiet-lo-bi-mat", "nda"]
        },
        {
            "slug": "xam-pham-quyen",
            "korean": "권리침해",
            "vietnamese": "xâm phạm quyền",
            "hanja": "權利侵害",
            "hanjaReading": "權(권세 권) + 利(이로울 리) + 侵(침노할 침) + 害(해칠 해)",
            "pronunciation": "섬 팜 꾸엔",
            "meaningKo": "타인의 법적 권리를 부당하게 침해하는 행위. 베트남에서는 'xâm phạm quyền'으로 표현하며, 지식재산권뿐 아니라 모든 법적 권리 침해에 사용됩니다. 통역 시 'vi phạm quyền'(권리 위반)과 혼용할 수 있으나, 'xâm phạm'이 더 강한 불법성을 내포합니다. 베트남 법원은 고의적 침해(cố ý xâm phạm)와 과실 침해를 구분하며, 고의적 침해는 3배 손해배상(tối đa gấp 3 lần)이 가능합니다. 한국과 달리 베트남은 지재권 침해 시 형사고소가 일반적이며, 통역사는 민사와 형사 절차를 모두 이해해야 합니다.",
            "meaningVi": "Hành vi trái pháp luật vi phạm quyền hợp pháp của người khác. Bao gồm xâm phạm quyền sở hữu trí tuệ, quyền dân sự, quyền lao động. Xâm phạm cố ý có thể bị bồi thường gấp 3 lần thiệt hại thực tế và xử phạt hình sự. Chủ thể bị xâm phạm có quyền yêu cầu dừng ngay hành vi, tiêu hủy sản phẩm vi phạm và bồi thường.",
            "context": "분쟁 조정, 소송, 손해배상",
            "culturalNote": "한국은 권리침해를 주로 민사 손해배상으로 해결하는 반면, 베트남은 형사고소와 민사소송을 병행하는 경우가 많습니다. 베트남에서는 침해 제품 압류(tịch thu sản phẩm vi phạm)와 즉시 중지 명령(lệnh dừng ngay)이 신속하게 내려지므로, 한국 기업이 베트남에서 침해 분쟁 시 신속한 법적 조치가 필요함을 안내해야 합니다. 베트남 법원은 침해 증거 확보를 엄격히 요구하므로, 공증된 증거 자료 준비가 중요합니다.",
            "commonMistakes": [
                {
                    "mistake": "권리침해를 'vi phạm quyền'로만 번역",
                    "correction": "xâm phạm quyền (불법성 강조)",
                    "explanation": "'vi phạm'은 일반 위반이고, 'xâm phạm'이 침해의 법적 용어입니다."
                },
                {
                    "mistake": "손해배상만 가능하다고 통역",
                    "correction": "베트남은 형사고소와 3배 배상 가능",
                    "explanation": "한국보다 구제 수단이 강력하므로 분쟁 전략 수립 시 반드시 설명해야 합니다."
                },
                {
                    "mistake": "증거 확보를 소홀히 하도록 안내",
                    "correction": "베트남은 공증된 증거 필수",
                    "explanation": "베트남 법원은 증거 요건이 엄격하므로 침해 발견 즉시 공증 절차를 밟아야 합니다."
                }
            ],
            "examples": [
                {
                    "ko": "당사 특허권을 침해한 제품에 대해 법적 조치를 취하겠습니다.",
                    "vi": "Chúng tôi sẽ có biện pháp pháp lý đối với sản phẩm xâm phạm quyền bằng sáng chế của công ty.",
                    "situation": "formal"
                },
                {
                    "ko": "권리침해로 3배 배상을 청구할 수 있나요?",
                    "vi": "Có thể yêu cầu bồi thường gấp 3 lần vì xâm phạm quyền không?",
                    "situation": "informal"
                },
                {
                    "ko": "침해 증거를 공증받아 두세요.",
                    "vi": "Hãy công chứng bằng chứng xâm phạm.",
                    "situation": "formal"
                }
            ],
            "relatedTerms": ["so-huu-tri-tue", "boi-thuong-thiet-hai", "vi-pham-ban-quyen", "kien-tung"]
        },
        {
            "slug": "chuyen-nhuong-quyen",
            "korean": "권리이전",
            "vietnamese": "chuyển nhượng quyền",
            "hanja": "權利移轉",
            "hanjaReading": "權(권세 권) + 利(이로울 리) + 移(옮길 이) + 轉(구를 전)",
            "pronunciation": "쭈엔 뉴엉 꾸엔",
            "meaningKo": "권리를 타인에게 넘기는 법률 행위. 베트남에서는 'chuyển nhượng quyền'으로 표현하며, '讓渡'의 개념이 강합니다. 통역 시 'chuyển giao quyền'(권리 인계)과 혼용할 수 있으나, 법률 문서에서는 'chuyển nhượng'이 정확한 용어입니다. 베트남에서는 권리 양도 시 반드시 서면 계약(hợp đồng bằng văn bản)이 필요하며, 특허·상표 양도는 국가 지식재산청에 등록해야 효력이 발생합니다. 한국과 달리 베트남은 저작인격권은 양도가 절대 불가능하므로, 저작권 양도 계약 시 재산권만 양도됨을 명확히 해야 합니다.",
            "meaningVi": "Hành vi chuyển quyền từ chủ thể này sang chủ thể khác. Phải lập hợp đồng bằng văn bản, công chứng hoặc chứng thực. Chuyển nhượng bằng sáng chế, nhãn hiệu phải đăng ký tại Cục Sở hữu trí tuệ mới có hiệu lực. Quyền nhân thân của tác giả không thể chuyển nhượng. Chuyển nhượng có thể toàn bộ hoặc một phần quyền, có thời hạn hoặc vô thời hạn.",
            "context": "M&A, 기술이전, 라이선스",
            "culturalNote": "한국은 권리 양도를 유연하게 인정하는 반면, 베트남은 형식 요건(공증, 등록)을 엄격히 요구합니다. 베트남에서는 등록하지 않은 권리 양도는 제3자에게 대항할 수 없으므로, 한국 기업이 베트남 기업으로부터 권리를 매수할 때 반드시 등록 여부를 확인하도록 안내해야 합니다. 베트남에서는 국가 소유 지재권(nhà nước sở hữu)은 양도가 제한되므로, 국영 기업과의 거래 시 주의가 필요합니다.",
            "commonMistakes": [
                {
                    "mistake": "권리이전을 'chuyển giao quyền'로 번역",
                    "correction": "chuyển nhượng quyền",
                    "explanation": "'chuyển giao'는 일반 인계이고, 법률 용어는 'chuyển nhượng'입니다."
                },
                {
                    "mistake": "구두 합의로 양도 가능하다고 설명",
                    "correction": "베트남은 서면 + 공증 + 등록 필수",
                    "explanation": "한국보다 형식 요건이 엄격하므로 계약 절차를 명확히 해야 합니다."
                },
                {
                    "mistake": "저작인격권도 양도 가능하다고 통역",
                    "correction": "베트남은 quyền nhân thân 양도 절대 불가",
                    "explanation": "저작권 계약 시 재산권만 양도됨을 명시해야 분쟁을 예방할 수 있습니다."
                }
            ],
            "examples": [
                {
                    "ko": "특허권을 전부 양도하는 계약입니다.",
                    "vi": "Đây là hợp đồng chuyển nhượng toàn bộ quyền bằng sáng chế.",
                    "situation": "formal"
                },
                {
                    "ko": "권리 이전 등록을 완료해야 효력이 발생합니다.",
                    "vi": "Phải hoàn tất đăng ký chuyển nhượng quyền mới có hiệu lực.",
                    "situation": "formal"
                },
                {
                    "ko": "저작인격권은 양도할 수 없습니다.",
                    "vi": "Quyền nhân thân của tác giả không thể chuyển nhượng.",
                    "situation": "formal"
                }
            ],
            "relatedTerms": ["so-huu-tri-tue", "hop-dong-chuyen-nhuong", "dang-ky-chuyen-nhuong", "quyen-su-dung"]
        },
        {
            "slug": "giay-chung-nhan-nhan-hieu",
            "korean": "상표등록증",
            "vietnamese": "giấy chứng nhận nhãn hiệu",
            "hanja": "商標登錄證",
            "hanjaReading": "商(장사 상) + 標(표 표) + 登(오를 등) + 錄(기록할 록) + 證(증거 증)",
            "pronunciation": "쟈이 쯩 년 년 히에우",
            "meaningKo": "상표 등록을 증명하는 공식 문서. 베트남에서는 'giấy chứng nhận nhãn hiệu'로 표현하며, 국가 지식재산청(Cục Sở hữu trí tuệ)이 발급합니다. 통역 시 'văn bằng bảo hộ nhãn hiệu'(상표 보호 증서)와 혼용할 수 있으나, 실무에서는 'giấy chứng nhận'이 더 일반적입니다. 등록증에는 상표 이미지, 등록 번호, 보호 범위(상품·서비스 분류), 유효 기간이 명시됩니다. 베트남 상표등록증은 10년 유효이며, 갱신 시 새 증서를 발급받습니다. 한국과 달리 베트남은 등록증 원본 제시가 필요한 경우가 많으므로, 분실 시 재발급 절차를 숙지해야 합니다.",
            "meaningVi": "Văn bản chứng nhận đăng ký nhãn hiệu do Cục Sở hữu trí tuệ cấp. Ghi rõ hình ảnh nhãn hiệu, số đăng ký, phạm vi bảo hộ (danh mục hàng hóa, dịch vụ), thời hạn hiệu lực 10 năm. Khi gia hạn sẽ được cấp giấy chứng nhận mới. Mất giấy chứng nhận có thể xin cấp lại tại Cục Sở hữu trí tuệ.",
            "context": "상표 등록, 프랜차이즈, 분쟁 입증",
            "culturalNote": "한국은 상표등록증을 주로 전자 문서로 관리하는 반면, 베트남은 여전히 종이 증서를 중시합니다. 베트남에서는 법원 분쟁이나 세관 신고 시 등록증 원본 제시를 요구하는 경우가 많으므로, 한국 기업이 베트남에서 상표 소송을 준비할 때 등록증 원본을 미리 확보하도록 안내해야 합니다. 베트남에서는 등록증 위조가 가끔 발생하므로, 중고 거래 시 국가 지식재산청 온라인 DB에서 진위를 확인하는 것이 중요합니다.",
            "commonMistakes": [
                {
                    "mistake": "상표등록증을 'giấy phép nhãn hiệu'로 번역",
                    "correction": "giấy chứng nhận nhãn hiệu",
                    "explanation": "'giấy phép'는 허가증이고, 등록증은 'giấy chứng nhận'입니다."
                },
                {
                    "mistake": "전자 문서만으로 충분하다고 안내",
                    "correction": "베트남은 원본 제시 요구 가능",
                    "explanation": "법원·세관에서 원본을 요구할 수 있으므로 원본 보관을 권장해야 합니다."
                },
                {
                    "mistake": "위조 여부 확인 없이 거래 진행",
                    "correction": "Cục SHTT 온라인 DB에서 진위 확인 필수",
                    "explanation": "베트남에서는 위조 등록증이 유통되므로 거래 전 확인이 필요합니다."
                }
            ],
            "examples": [
                {
                    "ko": "상표등록증 원본을 법원에 제출해야 합니다.",
                    "vi": "Phải nộp bản chính giấy chứng nhận nhãn hiệu cho tòa án.",
                    "situation": "formal"
                },
                {
                    "ko": "등록증을 분실했는데 재발급 받을 수 있나요?",
                    "vi": "Tôi bị mất giấy chứng nhận, có thể xin cấp lại không?",
                    "situation": "informal"
                },
                {
                    "ko": "이 등록증이 진짜인지 확인해 주세요.",
                    "vi": "Vui lòng xác minh giấy chứng nhận này có thật không.",
                    "situation": "formal"
                }
            ],
            "relatedTerms": ["nhan-hieu", "dang-ky-nhan-hieu", "cuc-so-huu-tri-tue", "gia-han-nhan-hieu"]
        },
        {
            "slug": "li-xang",
            "korean": "라이선스",
            "vietnamese": "li-xăng",
            "hanja": None,
            "hanjaReading": None,
            "pronunciation": "리 상",
            "meaningKo": "지식재산권 사용 허가. 베트남에서는 영어 'license'를 음차한 'li-xăng'을 사용하며, 공식 문서에서는 'giấy phép sử dụng'(사용 허가증)로도 표현합니다. 통역 시 'cấp phép'(허가)과 혼동하지 않도록 주의해야 하며, 'li-xăng'은 지재권 분야 특화 용어입니다. 베트남 라이선스 계약은 독점(độc quyền), 비독점(không độc quyền), 단독(duy nhất) 세 가지 유형이 있으며, 계약서에 명시하지 않으면 비독점으로 간주됩니다. 라이선스 계약은 국가 지식재산청에 등록해야 제3자에게 대항할 수 있으며, 기술 라이선스는 과학기술부(Bộ Khoa học và Công nghệ)에도 신고가 필요합니다.",
            "meaningVi": "Giấy phép sử dụng quyền sở hữu trí tuệ. Có 3 loại: độc quyền (exclusive), không độc quyền (non-exclusive), duy nhất (sole). Hợp đồng li-xăng phải đăng ký tại Cục Sở hữu trí tuệ mới có hiệu lực đối với bên thứ ba. Li-xăng công nghệ phải báo cáo Bộ Khoa học và Công nghệ. Thời hạn li-xăng không vượt quá thời hạn bảo hộ quyền.",
            "context": "기술이전, 프랜차이즈, 소프트웨어",
            "culturalNote": "한국은 라이선스를 유연하게 운용하는 반면, 베트남은 등록과 신고를 엄격히 요구합니다. 베트남에서는 기술 라이선스 계약 시 로열티 송금에 외환 관리 규정이 적용되므로, 한국 기업이 베트남에 라이선스를 제공할 때 송금 절차를 사전에 확인하도록 안내해야 합니다. 베트남에서는 라이선스 계약 미등록 시 제3자에게 권리를 주장할 수 없으므로, 계약 체결 즉시 등록 절차를 밟는 것이 중요합니다.",
            "commonMistakes": [
                {
                    "mistake": "라이선스를 'giấy phép'로만 번역",
                    "correction": "li-xăng 또는 giấy phép sử dụng (지재권)",
                    "explanation": "'giấy phép'는 일반 허가이고, 지재권 라이선스는 'li-xăng'이 관례입니다."
                },
                {
                    "mistake": "계약만 하면 된다고 안내",
                    "correction": "Cục SHTT 등록 + Bộ KH&CN 신고 필수",
                    "explanation": "베트남은 등록·신고 없이는 법적 효력이 제한되므로 절차를 명확히 해야 합니다."
                },
                {
                    "mistake": "독점 여부를 명시하지 않음",
                    "correction": "베트남은 미명시 시 비독점으로 간주",
                    "explanation": "한국과 달리 베트남은 명시하지 않으면 không độc quyền으로 해석되므로 계약서에 반드시 기재해야 합니다."
                }
            ],
            "examples": [
                {
                    "ko": "이 기술에 대한 독점 라이선스를 제공합니다.",
                    "vi": "Chúng tôi cấp li-xăng độc quyền đối với công nghệ này.",
                    "situation": "formal"
                },
                {
                    "ko": "라이선스 계약을 등록해야 하나요?",
                    "vi": "Có phải đăng ký hợp đồng li-xăng không?",
                    "situation": "informal"
                },
                {
                    "ko": "로열티 송금 절차를 확인해 주세요.",
                    "vi": "Vui lòng xác nhận thủ tục chuyển tiền nhuận bút.",
                    "situation": "formal"
                }
            ],
            "relatedTerms": ["so-huu-tri-tue", "hop-dong-chuyen-nhuong", "giay-phep-su-dung", "quyen-doc-quyen"]
        }
    ]

    # 5. 중복 필터링
    unique_terms = [t for t in new_terms if t['slug'] not in existing_slugs]

    # 6. 데이터 추가
    data.extend(unique_terms)

    # 7. 저장
    with open(file_path, 'w', encoding='utf-8') as f:
        json.dump(data, f, ensure_ascii=False, indent=2)

    print(f"✅ {len(unique_terms)}개 용어 추가 완료 (중복 {len(new_terms) - len(unique_terms)}개 제외)")
    print(f"📊 전체 용어 수: {len(data)}개")

    for term in unique_terms:
        print(f"  - {term['slug']}: {term['korean']} ({term['vietnamese']})")

if __name__ == "__main__":
    main()
