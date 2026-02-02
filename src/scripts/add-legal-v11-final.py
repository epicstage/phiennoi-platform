#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Legal 1,000개 달성을 위한 최종 3개 용어 추가"""
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
            "slug": "quyen-im-lang",
            "korean": "묵비권",
            "vietnamese": "Quyền im lặng",
            "hanja": "默秘權",
            "hanjaReading": "默(잠잠할 묵) 秘(숨길 비) 權(권리 권)",
            "pronunciation": "묵비권",
            "meaningKo": "형사 피의자 또는 피고인이 수사기관이나 법정에서 자신에게 불리한 진술을 거부할 수 있는 권리입니다. 통역 시 한국의 '묵비권 행사'와 베트남의 'quyền im lặng'은 법적 보장 수준이 다르므로 주의해야 합니다. 한국은 헌법 제12조에 의해 보장되며, 체포 시 반드시 고지되어야 합니다. 베트남에서는 2015년 형사소송법 개정으로 도입되었으나 실무 적용이 제한적인 경우가 있어, 통역 시 양국의 실질적 보장 차이를 설명해야 합니다.",
            "meaningVi": "Quyền của bị can hoặc bị cáo được từ chối khai báo những điều bất lợi cho mình trước cơ quan điều tra hoặc tòa án. Tại Việt Nam, quyền này được quy định trong Bộ luật Tố tụng hình sự 2015, tuy nhiên việc áp dụng trong thực tế vẫn còn hạn chế so với Hàn Quốc.",
            "context": "수사 단계, 법정 심리, 피의자 권리 고지 시",
            "culturalNote": "한국은 미란다 원칙에 따라 체포 즉시 묵비권을 고지하는 것이 엄격히 준수되지만, 베트남에서는 2015년 법 개정 이후에도 실무에서 묵비권 고지가 형식적인 경우가 많습니다. 특히 베트남 수사기관은 '협조적 태도'를 중시하는 경향이 있어 묵비권 행사가 불이익으로 이어질 수 있다는 인식이 존재합니다. 통역 시 이러한 문화적 차이를 이해하고 피의자의 권리를 정확히 전달해야 합니다.",
            "commonMistakes": [
                {
                    "mistake": "quyền từ chối khai báo와 혼동",
                    "correction": "quyền im lặng이 더 포괄적인 개념",
                    "explanation": "từ chối khai báo는 진술 거부의 의미이고, im lặng은 침묵할 권리 전체를 포함하는 더 넓은 개념"
                },
                {
                    "mistake": "묵비권을 '침묵 권리'로 직역",
                    "correction": "법률용어로 quyền im lặng 사용",
                    "explanation": "일상적 표현인 quyền giữ im lặng보다 법률용어인 quyền im lặng이 정확"
                },
                {
                    "mistake": "묵비권 행사를 유죄의 증거로 해석",
                    "correction": "묵비권 행사는 유죄 추정의 근거가 될 수 없음",
                    "explanation": "양국 모두 법적으로 묵비권 행사를 불이익 사유로 삼을 수 없으나, 실무에서는 인식 차이가 있음"
                }
            ],
            "examples": [
                {
                    "ko": "피의자는 수사기관에서 묵비권을 행사할 수 있으며, 이를 이유로 불이익을 받지 않습니다",
                    "vi": "Bị can có quyền im lặng trước cơ quan điều tra và không bị bất lợi vì lý do này",
                    "situation": "formal"
                },
                {
                    "ko": "변호인이 도착할 때까지 묵비권을 행사하시겠습니까?",
                    "vi": "Anh/chị có muốn sử dụng quyền im lặng cho đến khi luật sư đến không?",
                    "situation": "onsite"
                },
                {
                    "ko": "묵비권을 고지받았음에도 피의자가 자발적으로 진술한 경우 증거능력이 인정됩니다",
                    "vi": "Trong trường hợp bị can tự nguyện khai báo mặc dù đã được thông báo về quyền im lặng, lời khai đó có giá trị chứng cứ",
                    "situation": "formal"
                }
            ],
            "relatedTerms": ["진술거부권", "미란다원칙", "변호인접견권", "자백배제법칙"]
        },
        {
            "slug": "thi-hieu-khoi-kien",
            "korean": "소멸시효",
            "vietnamese": "Thời hiệu khởi kiện",
            "hanja": "消滅時效",
            "hanjaReading": "消(사라질 소) 滅(멸할 멸) 時(때 시) 效(효험 효)",
            "pronunciation": "소멸시효",
            "meaningKo": "일정 기간 동안 권리를 행사하지 않으면 그 권리가 소멸하는 제도입니다. 통역 시 한국과 베트남의 소멸시효 기간이 상당히 다르므로 주의가 필요합니다. 한국 민법상 일반 채권의 소멸시효는 10년이지만, 베트남 민법은 일반적으로 3년입니다. 또한 시효의 중단(tạm ngừng)과 정지(tạm đình chỉ) 사유도 양국이 다르므로, 계약서 번역이나 법률 상담 통역 시 구체적 기간을 반드시 확인해야 합니다. 시효 완성 후 효과도 한국은 항변권 발생, 베트남은 권리 자체 소멸로 차이가 있습니다.",
            "meaningVi": "Chế độ pháp lý theo đó quyền sẽ bị tiêu diệt nếu không được thực hiện trong một khoảng thời gian nhất định. Theo Bộ luật Dân sự Việt Nam, thời hiệu khởi kiện chung là 3 năm, trong khi Hàn Quốc quy định 10 năm cho các khoản nợ thông thường. Sự khác biệt này rất quan trọng trong các giao dịch thương mại quốc tế.",
            "context": "민사 소송, 계약 분쟁, 채권 회수, 법률 상담 통역 시",
            "culturalNote": "한국의 소멸시효 10년과 베트남의 3년은 실무에서 큰 차이를 만듭니다. 한국 기업이 베트남에서 채권을 회수할 때 한국 기준으로 시간 여유가 있다고 판단하면 베트남 시효가 이미 완성된 경우가 빈번합니다. 또한 한국은 시효 완성 후에도 채무자가 항변해야 효력이 발생하지만, 베트남은 법원이 직권으로 시효 완성을 확인하여 소를 각하할 수 있습니다. 통역 시 이 차이를 명확히 전달해야 합니다.",
            "commonMistakes": [
                {
                    "mistake": "thời hạn과 thời hiệu 혼동",
                    "correction": "thời hạn은 기한, thời hiệu는 시효",
                    "explanation": "thời hạn은 계약 기간이나 납부 기한 등 일반적 기한이고, thời hiệu는 권리 소멸과 관련된 법적 시효"
                },
                {
                    "mistake": "한국 시효 기간을 베트남에 적용",
                    "correction": "베트남 민법의 3년 시효를 확인",
                    "explanation": "국제 계약에서 준거법에 따라 시효 기간이 크게 달라지므로 반드시 해당국 법률 확인 필요"
                },
                {
                    "mistake": "소멸시효와 제척기간을 같은 개념으로 통역",
                    "correction": "소멸시효는 thời hiệu, 제척기간은 thời hạn pháp luật",
                    "explanation": "제척기간은 중단/정지가 없고 기간 경과로 권리 자체가 소멸하며, 소멸시효는 중단/정지가 가능"
                }
            ],
            "examples": [
                {
                    "ko": "해당 채권은 소멸시효가 완성되어 더 이상 법적으로 청구할 수 없습니다",
                    "vi": "Khoản nợ này đã hết thời hiệu khởi kiện nên không thể yêu cầu pháp lý được nữa",
                    "situation": "formal"
                },
                {
                    "ko": "시효 중단을 위해 내용증명을 보내야 합니다",
                    "vi": "Cần gửi thông báo có chứng nhận để tạm ngừng thời hiệu",
                    "situation": "onsite"
                },
                {
                    "ko": "베트남법에 따르면 이 사건의 소멸시효는 3년이므로 이미 기간이 지났습니다",
                    "vi": "Theo pháp luật Việt Nam, thời hiệu khởi kiện vụ này là 3 năm nên đã quá hạn",
                    "situation": "formal"
                }
            ],
            "relatedTerms": ["제척기간", "시효중단", "시효정지", "채권소멸"]
        },
        {
            "slug": "bien-phap-khan-cap-tam-thoi",
            "korean": "가처분",
            "vietnamese": "Biện pháp khẩn cấp tạm thời",
            "hanja": "假處分",
            "hanjaReading": "假(가짜 가) 處(처리할 처) 分(나눌 분)",
            "pronunciation": "가처분",
            "meaningKo": "소송의 본안 판결이 확정되기 전에 현재 상태를 보전하거나 임시적 법적 지위를 설정하기 위한 법원의 잠정적 처분입니다. 통역 시 한국의 '가처분'은 민사보전법에 의한 것이고, 베트남의 'biện pháp khẩn cấp tạm thời'는 민사소송법 제111조에 규정된 것으로, 적용 범위와 요건이 다르므로 주의해야 합니다. 한국은 피보전권리와 보전의 필요성만 소명하면 되지만, 베트남은 담보금 제공이 필수적인 경우가 많아 실무적 차이가 큽니다. 국제 계약 분쟁에서 양국 보전처분 절차를 비교 설명해야 하는 경우가 많습니다.",
            "meaningVi": "Quyết định tạm thời của tòa án nhằm bảo toàn tình trạng hiện tại hoặc thiết lập địa vị pháp lý tạm thời trước khi có bản án chính thức. Theo Điều 111 Bộ luật Tố tụng dân sự Việt Nam, có 16 biện pháp khẩn cấp tạm thời khác nhau, bao gồm phong tỏa tài sản, cấm chuyển dịch quyền và các biện pháp bảo toàn khác.",
            "context": "민사 소송, 지식재산권 분쟁, 부동산 분쟁, 상사 중재",
            "culturalNote": "한국은 가처분 신청이 상대적으로 신속하게 처리되며 담보금 없이도 가능한 경우가 있지만, 베트남에서는 biện pháp khẩn cấp tạm thời 신청 시 거의 항상 담보금(khoản bảo đảm) 납부가 요구됩니다. 또한 한국은 가처분 결정에 대한 이의신청 절차가 체계적이지만, 베트남은 결정 취소 절차가 복잡하고 시간이 오래 걸릴 수 있습니다. 통역 시 이러한 절차적 차이를 명확히 설명해야 당사자의 기대를 적절히 관리할 수 있습니다.",
            "commonMistakes": [
                {
                    "mistake": "가처분과 가압류를 혼동",
                    "correction": "가처분은 biện pháp khẩn cấp tạm thời, 가압류는 phong tỏa tài sản",
                    "explanation": "가압류는 금전채권 보전을 위한 재산 동결이고, 가처분은 비금전적 청구권 보전을 위한 포괄적 처분"
                },
                {
                    "mistake": "lệnh cấm tạm thời로 축소 번역",
                    "correction": "biện pháp khẩn cấp tạm thời가 정확한 법률용어",
                    "explanation": "lệnh cấm은 금지명령만을 의미하지만, 가처분은 금지 외에도 다양한 형태의 잠정적 처분을 포함"
                },
                {
                    "mistake": "본안 소송 없이 가처분만으로 최종 해결 가능하다고 설명",
                    "correction": "가처분은 임시 조치이며 본안 소송이 별도로 필요",
                    "explanation": "양국 모두 가처분은 잠정적 성격이나, 한국은 일정 기간 내 본안 소송 제기 의무가 있음"
                }
            ],
            "examples": [
                {
                    "ko": "상대방의 재산 처분을 막기 위해 부동산 처분금지 가처분을 신청하겠습니다",
                    "vi": "Chúng tôi sẽ nộp đơn yêu cầu biện pháp khẩn cấp tạm thời cấm chuyển dịch bất động sản để ngăn đối phương xử lý tài sản",
                    "situation": "formal"
                },
                {
                    "ko": "가처분 결정이 내려지면 상대방은 해당 건물을 매도할 수 없습니다",
                    "vi": "Khi có quyết định áp dụng biện pháp khẩn cấp tạm thời, đối phương không được bán tòa nhà đó",
                    "situation": "onsite"
                },
                {
                    "ko": "법원이 가처분 신청을 인용하기 위해서는 보전의 필요성을 소명해야 합니다",
                    "vi": "Để tòa án chấp nhận đơn yêu cầu biện pháp khẩn cấp tạm thời, cần chứng minh sự cần thiết của việc bảo toàn",
                    "situation": "formal"
                }
            ],
            "relatedTerms": ["가압류", "보전처분", "본안소송", "담보금"]
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
    print(f"✅ Added {len(filtered)} terms (최종). Total: {len(data)}")

if __name__ == '__main__':
    main()
