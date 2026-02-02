#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
사이버법/개인정보보호 용어 추가 스크립트
Theme: Cyber Law/Data Protection
Target: 10 unique terms (Tier S quality)
"""

import json
import os

def main():
    # 1. 파일 경로 설정 (상대 경로)
    file_path = os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', 'data', 'terms', 'legal.json')

    print(f"📂 파일 경로: {file_path}")

    # 2. 기존 데이터 로드
    with open(file_path, 'r', encoding='utf-8') as f:
        data = json.load(f)  # data는 LIST

    print(f"📊 기존 용어 수: {len(data)}개")

    # 3. 기존 slug 목록 추출 (중복 방지)
    existing_slugs = {t['slug'] for t in data}

    # 4. 새 용어 정의
    new_terms = [
        {
            "slug": "du-lieu-ca-nhan",
            "korean": "개인정보",
            "vietnamese": "dữ liệu cá nhân",
            "hanja": "個人情報",
            "hanjaReading": "個(낱 개) + 人(사람 인) + 情(뜻 정) + 報(알릴 보)",
            "pronunciation": "쭈리에우까년",
            "meaningKo": "특정 개인을 식별할 수 있는 모든 정보를 의미하며, 이름, 주민등록번호, 여권번호, 주소, 전화번호, 이메일, 생년월일 등이 포함됩니다. 한국의 개인정보보호법과 베트남의 개인정보보호법령(Nghị định 13/2023/NĐ-CP)은 처리 방식과 동의 요건이 다르므로, 통역 시 '동의(đồng ý)'와 '명시적 동의(đồng ý rõ ràng)'를 구분해야 합니다. 특히 민감정보(dữ liệu nhạy cảm)의 경우 양국 모두 엄격한 보호를 요구하니 주의가 필요합니다.",
            "meaningVi": "Là tất cả thông tin có thể nhận dạng một cá nhân cụ thể, bao gồm họ tên, số CMND/CCCD, số hộ chiếu, địa chỉ, số điện thoại, email, ngày sinh. Pháp luật Hàn Quốc và Việt Nam đều quy định nghiêm ngặt về thu thập, xử lý và bảo vệ dữ liệu cá nhân.",
            "context": "법률 자문, 개인정보 처리 계약, 규정 준수 교육 시 사용",
            "culturalNote": "한국은 개인정보보호위원회가 독립 기관으로 강력한 규제 권한을 가지며, 베트남은 공안부(Bộ Công an)가 주도합니다. 한국은 과징금이 매우 높고(최대 매출액 3%), 베트남은 형사처벌(최대 3억 동)과 행정 제재를 병행합니다. 통역 시 '개인정보보호위원회'를 'Ủy ban Bảo vệ Dữ liệu Cá nhân'이 아닌 'Ủy ban Bảo vệ Thông tin Cá nhân'으로 번역해야 공식 명칭에 맞습니다.",
            "commonMistakes": [
                {
                    "mistake": "thông tin cá nhân",
                    "correction": "dữ liệu cá nhân",
                    "explanation": "베트남 법령(Nghị định 13/2023)에서 공식 용어는 'dữ liệu cá nhân'이며, 'thông tin cá nhân'은 구어체입니다."
                },
                {
                    "mistake": "개인정보를 'information cá nhân'으로 번역",
                    "correction": "dữ liệu cá nhân",
                    "explanation": "영어 혼용은 법률 문서에서 부적합하며, 베트남어 고유 표현을 사용해야 합니다."
                },
                {
                    "mistake": "민감정보를 'thông tin quan trọng'으로 번역",
                    "correction": "dữ liệu nhạy cảm 또는 dữ liệu cá nhân đặc biệt",
                    "explanation": "'quan trọng'은 '중요한'이라는 의미로, 법적 개념인 '민감정보'와 다릅니다."
                }
            ],
            "examples": [
                {
                    "ko": "당사는 고객의 개인정보를 법령에 따라 안전하게 보호합니다.",
                    "vi": "Công ty chúng tôi bảo vệ an toàn dữ liệu cá nhân của khách hàng theo quy định pháp luật.",
                    "situation": "formal"
                },
                {
                    "ko": "개인정보 수집 시 반드시 동의를 받아야 합니다.",
                    "vi": "Khi thu thập dữ liệu cá nhân, bắt buộc phải có sự đồng ý.",
                    "situation": "formal"
                },
                {
                    "ko": "개인정보 유출 사고가 발생하면 즉시 신고해야 합니다.",
                    "vi": "Khi xảy ra sự cố rò rỉ dữ liệu cá nhân, phải báo cáo ngay lập tức.",
                    "situation": "onsite"
                }
            ],
            "relatedTerms": ["bao-ve-du-lieu", "lo-thong-tin", "dong-y-xu-ly-du-lieu"]
        },
        {
            "slug": "bao-ve-du-lieu",
            "korean": "개인정보보호",
            "vietnamese": "bảo vệ dữ liệu",
            "hanja": "個人情報保護",
            "hanjaReading": "個(낱 개) + 人(사람 인) + 情(뜻 정) + 報(알릴 보) + 保(지킬 보) + 護(도울 호)",
            "pronunciation": "바오베쭈리에우",
            "meaningKo": "개인정보의 수집, 이용, 제공, 파기 전 과정에서 정보주체의 권리를 보장하고 정보를 안전하게 관리하는 법적·기술적 조치를 총칭합니다. 한국은 개인정보보호법(PIPA), 베트남은 Nghị định 13/2023/NĐ-CP를 기준으로 하며, 통역 시 '보호(bảo vệ)'와 '보안(bảo mật)'을 혼동하지 않도록 주의해야 합니다. 'bảo vệ'는 권리 보장 중심, 'bảo mật'은 기술적 안전성 중심입니다.",
            "meaningVi": "Là các biện pháp pháp lý và kỹ thuật nhằm đảm bảo quyền của chủ thể dữ liệu và quản lý an toàn thông tin trong toàn bộ quá trình thu thập, sử dụng, cung cấp và hủy dữ liệu cá nhân. Việt Nam áp dụng Nghị định 13/2023/NĐ-CP làm khung pháp lý chính.",
            "context": "개인정보보호 감사, 규정 준수 점검, 교육 자료 번역 시 사용",
            "culturalNote": "한국은 개인정보보호 인증(PIPL)과 개인정보보호 관리체계(PIMS) 인증이 발달했으나, 베트남은 아직 인증 체계가 초기 단계입니다. 한국 기업이 베트남 진출 시 현지 법령 준수(compliance)뿐 아니라, 한국 본사의 높은 보호 수준을 유지해야 하는 이중 부담이 있습니다. 통역 시 '준수'를 'tuân thủ'로, '이행'을 'thực hiện'으로 구분해야 합니다.",
            "commonMistakes": [
                {
                    "mistake": "bảo mật dữ liệu",
                    "correction": "bảo vệ dữ liệu",
                    "explanation": "'bảo mật'은 기술적 보안(security)을 의미하고, 'bảo vệ'는 법적 보호(protection)를 의미합니다."
                },
                {
                    "mistake": "개인정보보호를 'an toàn thông tin'으로 번역",
                    "correction": "bảo vệ dữ liệu cá nhân",
                    "explanation": "'an toàn thông tin'은 정보보안(information security) 일반을 뜻하며, 개인정보보호의 법적 개념과 다릅니다."
                },
                {
                    "mistake": "보호조치를 'biện pháp phòng ngừa'로 번역",
                    "correction": "biện pháp bảo vệ",
                    "explanation": "'phòng ngừa'는 예방(prevention)이고, 'bảo vệ'는 보호(protection)입니다."
                }
            ],
            "examples": [
                {
                    "ko": "당사는 개인정보보호 관리체계 인증을 취득했습니다.",
                    "vi": "Công ty chúng tôi đã đạt chứng nhận hệ thống quản lý bảo vệ dữ liệu cá nhân.",
                    "situation": "formal"
                },
                {
                    "ko": "개인정보보호 교육을 분기별로 실시합니다.",
                    "vi": "Chúng tôi thực hiện đào tạo bảo vệ dữ liệu cá nhân theo quý.",
                    "situation": "formal"
                },
                {
                    "ko": "개인정보보호 책임자를 지정해야 합니다.",
                    "vi": "Phải chỉ định người chịu trách nhiệm bảo vệ dữ liệu cá nhân.",
                    "situation": "onsite"
                }
            ],
            "relatedTerms": ["du-lieu-ca-nhan", "an-ninh-mang", "luu-tru-du-lieu"]
        },
        {
            "slug": "an-ninh-mang",
            "korean": "사이버보안",
            "vietnamese": "an ninh mạng",
            "hanja": None,
            "hanjaReading": None,
            "pronunciation": "안닌망",
            "meaningKo": "사이버 공격, 해킹, 랜섬웨어, 데이터 유출 등으로부터 네트워크와 시스템을 보호하는 기술적·조직적 대책을 의미합니다. 베트남은 사이버보안법(Luật An ninh mạng 2018)을 통해 강력한 규제를 시행하며, 특히 외국 기업에게 베트남 내 서버 설치와 데이터 현지화(localization)를 요구할 수 있습니다. 통역 시 'an ninh mạng'(국가 안보 차원)과 'bảo mật mạng'(기술적 보안)을 구분해야 하며, 법률 맥락에서는 'an ninh mạng'이 공식 용어입니다.",
            "meaningVi": "Là các biện pháp kỹ thuật và tổ chức nhằm bảo vệ mạng và hệ thống khỏi các cuộc tấn công mạng, tin tặc, mã độc tống tiền, rò rỉ dữ liệu. Luật An ninh mạng 2018 của Việt Nam quy định nghiêm ngặt, yêu cầu doanh nghiệp nước ngoài có thể phải đặt máy chủ tại Việt Nam.",
            "context": "사이버보안 감사, IT 인프라 구축, 법률 자문 시 사용",
            "culturalNote": "베트남의 사이버보안법은 중국 모델을 일부 참고했으며, 정부의 정보 접근 권한이 한국보다 강력합니다. 한국 기업이 베트남에 진출할 때 '국가 안보'를 이유로 데이터 제공을 요구받을 수 있으므로, 법률 검토가 필수입니다. 통역 시 '국가안보'를 'an ninh quốc gia'로, '정보보안'을 'bảo mật thông tin'으로 명확히 구분해야 오해가 없습니다.",
            "commonMistakes": [
                {
                    "mistake": "bảo mật mạng",
                    "correction": "an ninh mạng",
                    "explanation": "법률 문서에서는 'an ninh mạng'이 공식 용어이며, 'bảo mật mạng'은 기술적 보안을 뜻합니다."
                },
                {
                    "mistake": "사이버보안을 'internet security'로 번역",
                    "correction": "an ninh mạng",
                    "explanation": "베트남어 고유 용어를 사용해야 하며, 영어 혼용은 부적절합니다."
                },
                {
                    "mistake": "해킹을 'hack'으로 음차",
                    "correction": "tấn công mạng 또는 xâm nhập trái phép",
                    "explanation": "법률 용어로는 'xâm nhập trái phép'(불법 침입)가 적합합니다."
                }
            ],
            "examples": [
                {
                    "ko": "사이버보안 사고 발생 시 72시간 이내 신고해야 합니다.",
                    "vi": "Khi xảy ra sự cố an ninh mạng, phải báo cáo trong vòng 72 giờ.",
                    "situation": "formal"
                },
                {
                    "ko": "당사는 사이버보안 대책을 강화하고 있습니다.",
                    "vi": "Công ty chúng tôi đang tăng cường các biện pháp an ninh mạng.",
                    "situation": "formal"
                },
                {
                    "ko": "사이버보안 전문가를 채용 중입니다.",
                    "vi": "Chúng tôi đang tuyển chuyên gia an ninh mạng.",
                    "situation": "onsite"
                }
            ],
            "relatedTerms": ["bao-ve-du-lieu", "toi-pham-cong-nghe-cao", "luu-tru-du-lieu"]
        },
        {
            "slug": "toi-pham-cong-nghe-cao",
            "korean": "사이버범죄",
            "vietnamese": "tội phạm công nghệ cao",
            "hanja": None,
            "hanjaReading": None,
            "pronunciation": "또이팜꽁응에까오",
            "meaningKo": "컴퓨터, 네트워크, 인터넷을 이용한 범죄 행위로, 해킹, 개인정보 절취, 금융사기, 명예훼손, 저작권 침해, 랜섬웨어 유포 등이 포함됩니다. 한국은 정보통신망법과 형법으로, 베트남은 형법(Bộ luật Hình sự) 제9장으로 처벌하며, 양국 모두 국제 공조를 강화하고 있습니다. 통역 시 'tội phạm mạng'(사이버범죄 일반)과 'tội phạm công nghệ cao'(고도 기술범죄)를 구분해야 하며, 법률 맥락에서는 후자가 정확합니다.",
            "meaningVi": "Là hành vi phạm tội sử dụng máy tính, mạng, internet, bao gồm tấn công mạng, đánh cắp thông tin cá nhân, lừa đảo tài chính, xâm phạm danh dự, vi phạm bản quyền, phát tán mã độc tống tiền. Bộ luật Hình sự Việt Nam quy định tại Chương IX với các hình phạt nghiêm khắc.",
            "context": "형사 고소, 법률 자문, 사이버 범죄 신고 시 사용",
            "culturalNote": "한국은 사이버범죄 전담 수사기관(사이버안전국)이 체계적으로 운영되지만, 베트남은 공안부 산하 A05국이 담당하며 신고 절차가 복잡합니다. 한국인이 베트남에서 피해를 입으면 한국 대사관을 통한 영사 조력이 중요하며, 통역사는 '영사 조력'을 'hỗ trợ lãnh sự'로 정확히 전달해야 합니다. 또한 베트남에서는 사이버 명예훼손도 형사처벌 대상이므로 주의가 필요합니다.",
            "commonMistakes": [
                {
                    "mistake": "tội phạm mạng",
                    "correction": "tội phạm công nghệ cao",
                    "explanation": "'tội phạm mạng'은 넓은 의미이고, 'tội phạm công nghệ cao'가 법률상 정확한 용어입니다."
                },
                {
                    "mistake": "해킹을 'hacking'으로 음차",
                    "correction": "tấn công mạng 또는 xâm nhập hệ thống",
                    "explanation": "법률 문서에서는 베트남어 고유 표현을 사용해야 합니다."
                },
                {
                    "mistake": "피싱을 'phishing'으로 음차",
                    "correction": "lừa đảo trực tuyến 또는 giả mạo website",
                    "explanation": "법정 통역에서는 베트남어 설명이 필요합니다."
                }
            ],
            "examples": [
                {
                    "ko": "사이버범죄 피해를 입으면 즉시 경찰에 신고하세요.",
                    "vi": "Nếu bị thiệt hại do tội phạm công nghệ cao, hãy báo cáo ngay cho công an.",
                    "situation": "informal"
                },
                {
                    "ko": "사이버범죄 예방을 위한 교육을 실시합니다.",
                    "vi": "Chúng tôi thực hiện đào tạo phòng ngừa tội phạm công nghệ cao.",
                    "situation": "formal"
                },
                {
                    "ko": "랜섬웨어 공격은 중대한 사이버범죄입니다.",
                    "vi": "Tấn công bằng mã độc tống tiền là tội phạm công nghệ cao nghiêm trọng.",
                    "situation": "formal"
                }
            ],
            "relatedTerms": ["an-ninh-mang", "lo-thong-tin", "du-lieu-ca-nhan"]
        },
        {
            "slug": "thuong-mai-dien-tu",
            "korean": "전자상거래",
            "vietnamese": "thương mại điện tử",
            "hanja": "電子商去來",
            "hanjaReading": "電(번개 전) + 子(아들 자) + 商(장사 상) + 去(갈 거) + 來(올 래)",
            "pronunciation": "트엉마이디엔뜨",
            "meaningKo": "인터넷, 모바일 앱 등 전자적 수단을 통해 상품이나 서비스를 거래하는 모든 상업 활동을 의미하며, 온라인 쇼핑몰, 오픈마켓, 소셜커머스 등이 포함됩니다. 한국은 전자상거래법, 베트남은 전자상거래법(Luật Thương mại điện tử 2005)과 소비자보호법을 적용하며, 통역 시 'thương mại điện tử'(법률 용어)와 'mua sắm trực tuyến'(일상 용어)을 맥락에 따라 구분해야 합니다.",
            "meaningVi": "Là tất cả hoạt động thương mại mua bán hàng hóa hoặc dịch vụ thông qua phương tiện điện tử như internet, ứng dụng di động, bao gồm cửa hàng trực tuyến, sàn thương mại điện tử, mạng xã hội. Việt Nam áp dụng Luật Thương mại điện tử 2005 và Luật Bảo vệ quyền lợi người tiêu dùng.",
            "context": "전자상거래 계약, 소비자 분쟁, 사업자 등록 상담 시 사용",
            "culturalNote": "한국은 통신판매업 신고와 전자상거래 소비자보호 체계가 발달했으나, 베트남은 아직 온라인 분쟁 해결 제도가 미비합니다. 한국 쇼핑몰이 베트남 진출 시 현지 결제 수단(MoMo, ZaloPay) 통합과 베트남어 고객 서비스가 필수이며, 통역사는 '청약철회'를 'quyền hủy đơn hàng'로, '환불'을 'hoàn tiền'으로 정확히 전달해야 소비자 분쟁을 예방할 수 있습니다.",
            "commonMistakes": [
                {
                    "mistake": "mua bán online",
                    "correction": "thương mại điện tử",
                    "explanation": "법률 문서에서는 'thương mại điện tử'가 공식 용어이며, 'online'은 구어체입니다."
                },
                {
                    "mistake": "전자상거래를 'e-commerce'로 번역",
                    "correction": "thương mại điện tử",
                    "explanation": "베트남어 고유 용어를 사용해야 합니다."
                },
                {
                    "mistake": "쇼핑몰을 'shopping mall'로 음차",
                    "correction": "cửa hàng trực tuyến 또는 sàn thương mại điện tử",
                    "explanation": "법률 용어로는 'sàn thương mại điện tử'(플랫폼)가 적합합니다."
                }
            ],
            "examples": [
                {
                    "ko": "전자상거래 사업자는 통신판매업 신고를 해야 합니다.",
                    "vi": "Doanh nghiệp thương mại điện tử phải đăng ký kinh doanh bán hàng từ xa.",
                    "situation": "formal"
                },
                {
                    "ko": "전자상거래 분쟁 발생 시 소비자보호원에 신청하세요.",
                    "vi": "Khi phát sinh tranh chấp thương mại điện tử, hãy nộp đơn lên Cơ quan Bảo vệ Người tiêu dùng.",
                    "situation": "formal"
                },
                {
                    "ko": "전자상거래 플랫폼 이용 약관을 확인하세요.",
                    "vi": "Hãy kiểm tra điều khoản sử dụng sàn thương mại điện tử.",
                    "situation": "informal"
                }
            ],
            "relatedTerms": ["chu-ky-dien-tu", "dong-y-xu-ly-du-lieu", "du-lieu-ca-nhan"]
        },
        {
            "slug": "chu-ky-dien-tu",
            "korean": "전자서명",
            "vietnamese": "chữ ký điện tử",
            "hanja": "電子署名",
            "hanjaReading": "電(번개 전) + 子(아들 자) + 署(관청 서) + 名(이름 명)",
            "pronunciation": "쯔끼디엔뜨",
            "meaningKo": "전자문서에 서명자의 신원과 문서의 위변조 방지를 위해 전자적 형태로 첨부되는 서명으로, 한국은 전자서명법, 베트남은 전자거래법(Luật Giao dịch điện tử 2005)에서 법적 효력을 인정합니다. 공인전자서명(chữ ký số công cộng)과 사설전자서명(chữ ký số riêng)을 구분해야 하며, 통역 시 'chữ ký điện tử'(전자서명 일반)와 'chữ ký số'(디지털 서명, PKI 기반)을 맥락에 따라 구분해야 정확합니다.",
            "meaningVi": "Là chữ ký dạng điện tử được đính kèm vào văn bản điện tử để xác thực danh tính người ký và ngăn chặn giả mạo, sửa đổi tài liệu. Luật Giao dịch điện tử Việt Nam công nhận hiệu lực pháp lý. Cần phân biệt chữ ký số công cộng và chữ ký số riêng.",
            "context": "계약서 작성, 법률 자문, 전자문서 관리 시 사용",
            "culturalNote": "한국은 공동인증서(구 공인인증서)와 민간인증서가 병존하며, 베트남은 공안부 산하 국가인증기관(VNCA)이 발급하는 공인전자서명이 법적으로 강력합니다. 한국 기업이 베트남 파트너와 계약 시 베트남 공인전자서명을 요구받을 수 있으므로, 통역사는 '공인전자서명'을 'chữ ký số công cộng'으로 정확히 전달해야 하며, '인증서'는 'chứng thư số'로 번역해야 합니다.",
            "commonMistakes": [
                {
                    "mistake": "chữ ký số",
                    "correction": "chữ ký điện tử (맥락에 따라)",
                    "explanation": "'chữ ký số'는 PKI 기반 디지털 서명이고, 'chữ ký điện tử'는 넓은 의미의 전자서명입니다."
                },
                {
                    "mistake": "서명을 'signature'로 음차",
                    "correction": "chữ ký điện tử",
                    "explanation": "베트남어 고유 용어를 사용해야 합니다."
                },
                {
                    "mistake": "인증서를 'certificate'로 음차",
                    "correction": "chứng thư số",
                    "explanation": "법률 용어로는 'chứng thư số'가 공식 표현입니다."
                }
            ],
            "examples": [
                {
                    "ko": "계약서에 전자서명을 해주세요.",
                    "vi": "Vui lòng ký điện tử vào hợp đồng.",
                    "situation": "formal"
                },
                {
                    "ko": "전자서명 인증서가 만료되었습니다.",
                    "vi": "Chứng thư số đã hết hạn.",
                    "situation": "formal"
                },
                {
                    "ko": "공인전자서명으로 신청서를 제출하세요.",
                    "vi": "Hãy nộp đơn bằng chữ ký số công cộng.",
                    "situation": "formal"
                }
            ],
            "relatedTerms": ["thuong-mai-dien-tu", "dong-y-xu-ly-du-lieu", "luu-tru-du-lieu"]
        },
        {
            "slug": "quyen-rieng-tu",
            "korean": "사생활권",
            "vietnamese": "quyền riêng tư",
            "hanja": "私生活權",
            "hanjaReading": "私(사사로울 사) + 生(날 생) + 活(살 활) + 權(권세 권)",
            "pronunciation": "꾸엔리엥뜨",
            "meaningKo": "개인의 사생활이 타인에게 공개되거나 침해받지 않을 권리로, 헌법상 기본권이며 민법, 개인정보보호법, 정보통신망법 등으로 보호됩니다. 베트남 헌법 제21조와 민법 제38조도 명시하며, 통역 시 'quyền riêng tư'(사생활권 일반)와 'quyền bảo vệ đời sống riêng tư'(사생활 보호권, 법률적)를 구분해야 정확합니다. 특히 직장 내 감시, CCTV 설치, SNS 게시물 등에서 사생활 침해 분쟁이 빈발하므로 주의가 필요합니다.",
            "meaningVi": "Là quyền cá nhân không bị người khác công khai hoặc xâm phạm đời sống riêng tư, là quyền cơ bản theo Hiến pháp, được bảo vệ bởi Luật Dân sự, Luật Bảo vệ dữ liệu cá nhân. Điều 21 Hiến pháp Việt Nam và Điều 38 Bộ luật Dân sự quy định rõ.",
            "context": "인권 침해, 명예훼손, 개인정보 침해 소송 시 사용",
            "culturalNote": "한국은 판례로 사생활권의 범위가 확대되어 왔으나, 베트남은 아직 판례 축적이 부족하고 법원의 해석이 보수적입니다. 특히 SNS 게시물을 증거로 제출할 때, 한국은 공개된 게시물도 맥락에 따라 사생활 침해로 인정될 수 있지만, 베트남은 공개된 정보는 사생활로 보지 않는 경향이 강합니다. 통역 시 '사생활 침해'를 'xâm phạm quyền riêng tư'로, '명예훼손'을 'xâm phạm danh dự'로 명확히 구분해야 합니다.",
            "commonMistakes": [
                {
                    "mistake": "đời sống riêng",
                    "correction": "quyền riêng tư",
                    "explanation": "'đời sống riêng'은 사생활 자체이고, 'quyền riêng tư'는 권리입니다."
                },
                {
                    "mistake": "사생활권을 'privacy right'로 번역",
                    "correction": "quyền riêng tư",
                    "explanation": "베트남어 고유 용어를 사용해야 합니다."
                },
                {
                    "mistake": "침해를 'vi phạm'으로 번역",
                    "correction": "xâm phạm",
                    "explanation": "'vi phạm'은 위반(violation)이고, 'xâm phạm'은 침해(infringement)입니다."
                }
            ],
            "examples": [
                {
                    "ko": "사생활권 침해로 민사 소송을 제기했습니다.",
                    "vi": "Đã khởi kiện dân sự do xâm phạm quyền riêng tư.",
                    "situation": "formal"
                },
                {
                    "ko": "직장 내 CCTV 설치는 사생활권을 고려해야 합니다.",
                    "vi": "Lắp đặt camera trong công ty phải xem xét quyền riêng tư của nhân viên.",
                    "situation": "formal"
                },
                {
                    "ko": "사생활 침해 여부는 구체적 사안에 따라 판단됩니다.",
                    "vi": "Việc có xâm phạm quyền riêng tư hay không được xét đoán theo từng trường hợp cụ thể.",
                    "situation": "formal"
                }
            ],
            "relatedTerms": ["du-lieu-ca-nhan", "bao-ve-du-lieu", "lo-thong-tin"]
        },
        {
            "slug": "lo-thong-tin",
            "korean": "개인정보유출",
            "vietnamese": "lộ thông tin",
            "hanja": "個人情報流出",
            "hanjaReading": "個(낱 개) + 人(사람 인) + 情(뜻 정) + 報(알릴 보) + 流(흐를 류) + 出(날 출)",
            "pronunciation": "로통띤",
            "meaningKo": "개인정보가 정당한 권한 없이 외부로 유출되거나 노출되는 사고로, 해킹, 내부자 유출, 관리 소홀 등이 원인입니다. 한국은 개인정보보호법 제34조(유출 통지), 베트남은 Nghị định 13/2023 제26조(사고 처리)에서 신고 의무를 규정하며, 통역 시 'lộ thông tin'(정보 유출 일반)과 'rò rỉ dữ liệu cá nhân'(개인정보 유출, 법률적)을 구분해야 정확합니다. 특히 유출 시점, 규모, 피해자 수, 조치 내용을 신속히 통보해야 과징금을 감경받을 수 있습니다.",
            "meaningVi": "Là sự cố dữ liệu cá nhân bị rò rỉ hoặc lộ ra ngoài mà không có thẩm quyền hợp pháp, do tin tặc, người nội bộ tiết lộ, hoặc quản lý lỏng lẻo. Luật Bảo vệ dữ liệu cá nhân Việt Nam quy định nghĩa vụ báo cáo sự cố trong Điều 26 Nghị định 13/2023.",
            "context": "개인정보 유출 신고, 손해배상 소송, 사고 대응 매뉴얼 작성 시 사용",
            "culturalNote": "한국은 개인정보 유출 시 정보주체에게 즉시 통지하고 개인정보보호위원회에 신고해야 하며, 피해자가 많으면 집단소송으로 이어질 수 있습니다. 베트남은 공안부에 신고하고 피해자에게 통지해야 하나, 집단소송 제도가 없어 개별 민사소송으로 진행됩니다. 통역 시 '유출'을 'lộ' 또는 'rò rỉ'로, '통지'를 'thông báo'로, '신고'를 'báo cáo'로 구분해야 혼란이 없습니다.",
            "commonMistakes": [
                {
                    "mistake": "rò rỉ thông tin",
                    "correction": "rò rỉ dữ liệu cá nhân (법률적) 또는 lộ thông tin (일반)",
                    "explanation": "법률 문서에서는 'dữ liệu cá nhân'을 명시해야 정확합니다."
                },
                {
                    "mistake": "유출을 'leak'으로 음차",
                    "correction": "lộ 또는 rò rỉ",
                    "explanation": "베트남어 고유 동사를 사용해야 합니다."
                },
                {
                    "mistake": "통지를 'thông tin'으로 번역",
                    "correction": "thông báo",
                    "explanation": "'thông tin'은 정보이고, 'thông báo'는 통지입니다."
                }
            ],
            "examples": [
                {
                    "ko": "개인정보 유출 사고가 발생하여 고객에게 통지했습니다.",
                    "vi": "Đã xảy ra sự cố rò rỉ dữ liệu cá nhân và đã thông báo cho khách hàng.",
                    "situation": "formal"
                },
                {
                    "ko": "개인정보 유출로 인한 손해배상을 청구합니다.",
                    "vi": "Yêu cầu bồi thường thiệt hại do rò rỉ dữ liệu cá nhân.",
                    "situation": "formal"
                },
                {
                    "ko": "개인정보 유출 사고 대응 매뉴얼을 작성하세요.",
                    "vi": "Hãy soạn hướng dẫn ứng phó sự cố rò rỉ dữ liệu cá nhân.",
                    "situation": "onsite"
                }
            ],
            "relatedTerms": ["du-lieu-ca-nhan", "an-ninh-mang", "toi-pham-cong-nghe-cao"]
        },
        {
            "slug": "luu-tru-du-lieu",
            "korean": "데이터저장",
            "vietnamese": "lưu trữ dữ liệu",
            "hanja": None,
            "hanjaReading": None,
            "pronunciation": "르어쭈쭈리에우",
            "meaningKo": "개인정보나 업무 데이터를 서버, 클라우드, 하드디스크 등에 보관하는 행위로, 저장 위치, 기간, 보안 조치가 법적으로 중요합니다. 한국은 국내 저장 의무가 없으나, 베트남은 사이버보안법에 따라 중요 데이터는 국내 서버 저장을 요구할 수 있습니다. 통역 시 'lưu trữ'(저장, storage)와 'bảo quản'(보관, preservation)을 구분하며, 법률 맥락에서는 'lưu trữ dữ liệu'가 공식 용어입니다. 클라우드 서비스 이용 시 데이터 현지화(localization) 요건을 반드시 확인해야 합니다.",
            "meaningVi": "Là hành vi lưu giữ dữ liệu cá nhân hoặc dữ liệu công việc trên máy chủ, đám mây, ổ cứng. Vị trí lưu trữ, thời gian, biện pháp bảo mật có ý nghĩa pháp lý quan trọng. Luật An ninh mạng Việt Nam có thể yêu cầu lưu trữ dữ liệu quan trọng tại máy chủ trong nước.",
            "context": "클라우드 계약, 데이터 관리 정책, 법률 자문 시 사용",
            "culturalNote": "베트남은 외국 클라우드 서비스(AWS, Google Cloud) 사용 시 정부가 데이터 접근을 요구할 수 있는 권한을 법으로 보장하므로, 한국 기업은 민감 데이터를 베트남에 저장할 때 신중해야 합니다. 한국은 클라우드 보안 인증(CSAP)이 발달했으나, 베트남은 아직 인증 체계가 미비합니다. 통역 시 '저장'을 'lưu trữ'로, '백업'을 'sao lưu'로, '보관'을 'bảo quản'으로 구분해야 정확합니다.",
            "commonMistakes": [
                {
                    "mistake": "bảo quản dữ liệu",
                    "correction": "lưu trữ dữ liệu",
                    "explanation": "'bảo quản'은 물리적 보관이고, 'lưu trữ'는 데이터 저장입니다."
                },
                {
                    "mistake": "저장을 'save'로 음차",
                    "correction": "lưu trữ",
                    "explanation": "베트남어 고유 동사를 사용해야 합니다."
                },
                {
                    "mistake": "클라우드를 'cloud'로 음차",
                    "correction": "đám mây 또는 điện toán đám mây",
                    "explanation": "법률 용어로는 'điện toán đám mây'(클라우드 컴퓨팅)가 적합합니다."
                }
            ],
            "examples": [
                {
                    "ko": "고객 데이터는 암호화하여 안전하게 저장합니다.",
                    "vi": "Dữ liệu khách hàng được mã hóa và lưu trữ an toàn.",
                    "situation": "formal"
                },
                {
                    "ko": "데이터 저장 위치를 명시해주세요.",
                    "vi": "Vui lòng nêu rõ vị trí lưu trữ dữ liệu.",
                    "situation": "formal"
                },
                {
                    "ko": "클라우드에 데이터를 백업합니다.",
                    "vi": "Sao lưu dữ liệu lên đám mây.",
                    "situation": "onsite"
                }
            ],
            "relatedTerms": ["bao-ve-du-lieu", "an-ninh-mang", "chu-ky-dien-tu"]
        },
        {
            "slug": "dong-y-xu-ly-du-lieu",
            "korean": "정보처리동의",
            "vietnamese": "đồng ý xử lý dữ liệu",
            "hanja": "情報處理同意",
            "hanjaReading": "情(뜻 정) + 報(알릴 보) + 處(곳 처) + 理(다스릴 리) + 同(한가지 동) + 意(뜻 의)",
            "pronunciation": "동이쓰리쭈리에우",
            "meaningKo": "개인정보를 수집, 이용, 제공, 처리하기 위해 정보주체로부터 받는 동의로, 한국은 명시적 동의(사전 고지 후 동의), 베트남은 Nghị định 13/2023에서 명확한 동의(đồng ý rõ ràng)를 요구합니다. 민감정보는 별도 동의가 필수이며, 통역 시 'đồng ý'(일반 동의)와 'đồng ý rõ ràng'(명시적 동의)를 구분해야 정확합니다. 특히 마케팅 목적 사용은 선택적 동의(đồng ý tùy chọn)로 분리해야 법 위반을 피할 수 있습니다.",
            "meaningVi": "Là sự đồng ý của chủ thể dữ liệu để thu thập, sử dụng, cung cấp, xử lý dữ liệu cá nhân. Nghị định 13/2023/NĐ-CP của Việt Nam yêu cầu đồng ý rõ ràng. Dữ liệu nhạy cảm cần đồng ý riêng biệt. Mục đích marketing phải là đồng ý tùy chọn.",
            "context": "개인정보 처리 방침, 이용약관, 회원가입 동의서 작성 시 사용",
            "culturalNote": "한국은 포괄적 동의를 금지하고 각 목적별로 동의를 받아야 하며, 거부 시 불이익을 주면 과징금이 부과됩니다. 베트남도 유사하나, 실무에서는 아직 포괄 동의가 흔합니다. 한국 기업이 베트남 진출 시 한국 기준으로 동의서를 작성하면 법적 리스크를 줄일 수 있습니다. 통역 시 '동의'를 'đồng ý'로, '철회'를 'rút lại'로, '거부'를 'từ chối'로 구분해야 정확합니다.",
            "commonMistakes": [
                {
                    "mistake": "chấp thuận xử lý dữ liệu",
                    "correction": "đồng ý xử lý dữ liệu",
                    "explanation": "법률 용어로는 'đồng ý'가 공식 표현입니다."
                },
                {
                    "mistake": "동의를 'agreement'로 번역",
                    "correction": "đồng ý",
                    "explanation": "'agreement'는 계약(hợp đồng)이고, 동의는 'đồng ý'입니다."
                },
                {
                    "mistake": "철회를 'hủy'로 번역",
                    "correction": "rút lại",
                    "explanation": "'hủy'는 취소(cancel)이고, 'rút lại'는 철회(withdraw)입니다."
                }
            ],
            "examples": [
                {
                    "ko": "개인정보 처리 동의를 받아야 회원가입이 가능합니다.",
                    "vi": "Phải có đồng ý xử lý dữ liệu cá nhân mới có thể đăng ký thành viên.",
                    "situation": "formal"
                },
                {
                    "ko": "동의 철회는 언제든지 가능합니다.",
                    "vi": "Có thể rút lại đồng ý bất cứ lúc nào.",
                    "situation": "formal"
                },
                {
                    "ko": "마케팅 목적 사용은 선택적 동의입니다.",
                    "vi": "Sử dụng cho mục đích marketing là đồng ý tùy chọn.",
                    "situation": "formal"
                }
            ],
            "relatedTerms": ["du-lieu-ca-nhan", "bao-ve-du-lieu", "thuong-mai-dien-tu"]
        }
    ]

    # 5. 중복 제거
    new_terms_filtered = [t for t in new_terms if t['slug'] not in existing_slugs]

    print(f"✅ 신규 용어: {len(new_terms_filtered)}개 (중복 {len(new_terms) - len(new_terms_filtered)}개 제외)")

    if not new_terms_filtered:
        print("⚠️ 추가할 용어가 없습니다 (모두 중복)")
        return

    # 6. 데이터 병합
    data.extend(new_terms_filtered)

    # 7. 파일 저장
    with open(file_path, 'w', encoding='utf-8') as f:
        json.dump(data, f, ensure_ascii=False, indent=2)

    print(f"💾 저장 완료: {file_path}")
    print(f"📊 총 용어 수: {len(data)}개")
    print("\n🎯 추가된 용어:")
    for term in new_terms_filtered:
        print(f"   - {term['slug']} ({term['korean']} / {term['vietnamese']})")

if __name__ == "__main__":
    main()
