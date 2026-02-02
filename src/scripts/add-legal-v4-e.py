#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
농업법/어업법 전문용어 추가 스크립트
Theme: Agriculture/Fisheries Law
Target: legal.json
"""

import json
import os

def main():
    # 파일 경로 설정
    file_path = os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', 'data', 'terms', 'legal.json')

    # 기존 데이터 로드
    with open(file_path, 'r', encoding='utf-8') as f:
        data = json.load(f)  # LIST 형식

    # 기존 slug 목록 (중복 방지)
    existing_slugs = {item['slug'] for item in data}

    # 새 용어 데이터 (10개)
    new_terms = [
        {
            "slug": "luat-thuy-san",
            "korean": "수산법",
            "vietnamese": "Luật Thủy sản",
            "hanja": "水産法",
            "hanjaReading": "水(물 수) + 産(날 산) + 法(법 법)",
            "pronunciation": "루엇 투이 산",
            "meaningKo": "베트남의 수산자원 관리, 수산업 활동, 양식업, 어업 허가 등을 규율하는 법률입니다. 한국의 수산업법과 유사하나 베트남은 양식업 비중이 높아 양식 관련 규정이 상세합니다. 통역 시 한국은 '어업'과 '양식업'을 구분하지만 베트남어 'nuôi trồng thủy sản'은 양식 전반을 포괄하므로 문맥에 따라 정확히 구분해야 합니다. 또한 베트남은 메콩델타 지역의 민물 양식이 발달해 담수/해수 양식 용어를 혼동하지 않도록 주의가 필요합니다.",
            "meaningVi": "Luật điều chỉnh hoạt động khai thác, nuôi trồng, bảo vệ và phát triển nguồn lợi thủy sản. Bao gồm cấp phép đánh bắt, quản lý tàu cá, bảo vệ môi trường biển, phát triển nuôi trồng thủy sản. Việt Nam có quy định đặc thù về nuôi trồng thủy sản nước ngọt và nước mặn.",
            "context": "legal|formal",
            "culturalNote": "베트남은 세계 3대 수산물 수출국으로 새우·바사(tra) 양식이 주요 산업입니다. 한국은 연근해 어업 중심인 반면 베트남은 메콩델타 양식업이 핵심이라 법 체계도 양식 중심으로 설계되어 있습니다. 통역 시 한국 의뢰인이 '어업법'을 언급하면 베트남에선 어획보다 양식 규정이 더 중요할 수 있음을 인지해야 합니다.",
            "commonMistakes": [
                {
                    "mistake": "수산법을 'Luật đánh cá'로 번역",
                    "correction": "Luật Thủy sản",
                    "explanation": "'đánh cá'는 낚시/어획만 의미하고 양식·가공·유통을 포괄하지 못함"
                },
                {
                    "mistake": "'양식업'을 'nuôi cá'로만 표현",
                    "correction": "nuôi trồng thủy sản",
                    "explanation": "'nuôi cá'는 물고기만, 'nuôi trồng thủy sản'은 새우·조개·해조류 등 전체 포괄"
                },
                {
                    "mistake": "한국 수산업법 조항을 그대로 대입",
                    "correction": "베트남 수산법 체계 확인 필수",
                    "explanation": "베트남은 양식업법(2017)으로 개정돼 구조가 다름"
                }
            ],
            "examples": [
                {
                    "ko": "수산법 제12조에 따라 양식업 허가를 신청합니다.",
                    "vi": "Xin cấp giấy phép nuôi trồng thủy sản theo Điều 12 Luật Thủy sản.",
                    "situation": "formal"
                },
                {
                    "ko": "이번 개정 수산법은 불법 어업 단속을 강화합니다.",
                    "vi": "Luật Thủy sản sửa đổi lần này tăng cường kiểm soát đánh bắt bất hợp pháp.",
                    "situation": "formal"
                },
                {
                    "ko": "수산법상 보호 수역에서는 어업이 금지됩니다.",
                    "vi": "Theo Luật Thủy sản, nghiêm cấm đánh bắt tại vùng bảo vệ.",
                    "situation": "onsite"
                }
            ],
            "relatedTerms": ["giấy phép đánh bắt", "bảo vệ nguồn lợi thủy sản", "nuôi trồng thủy sản", "kiểm dịch thủy sản"]
        },
        {
            "slug": "giay-phep-danh-bat",
            "korean": "어업허가",
            "vietnamese": "Giấy phép đánh bắt",
            "hanja": "漁業許可",
            "hanjaReading": "漁(고기잡을 어) + 業(업 업) + 許(허락할 허) + 可(옳을 가)",
            "pronunciation": "지이 펩 다잉 밧",
            "meaningKo": "수산 자원을 어획하기 위해 정부가 발급하는 허가증으로, 어선 규모, 어획 방법, 조업 구역, 어종 등이 명시됩니다. 베트남은 'giấy phép khai thác thủy sản'으로도 불리며 연안/근해/원양을 엄격히 구분합니다. 통역 시 한국은 허가·신고·면허 체계가 복잡하지만 베트남은 'giấy phép' 하나로 통합되므로 한국 측 설명 시 세부 구분을 단순화해야 합니다. 또한 베트남은 외국인 어업 허가 절차가 까다로워 한국 어선의 베트남 조업 시 각별한 주의가 필요합니다.",
            "meaningVi": "Giấy phép do cơ quan có thẩm quyền cấp cho tổ chức, cá nhân để khai thác nguồn lợi thủy sản. Quy định rõ loại hình khai thác, vùng biển, công suất tàu, thời hạn. Phân chia theo vùng ven bờ, vùng lộng, vùng xa bờ.",
            "context": "legal|administrative",
            "culturalNote": "베트남 어업허가는 지방 수산국(Sở Nông nghiệp)에서 발급하며, 중국 어선의 불법 조업 문제로 단속이 강화되고 있습니다. 한국은 연근해 허가가 세분화되어 있으나 베트남은 통합 관리되므로, 한국 어업인이 베트남 진출 시 허가 범위를 정확히 확인해야 합니다. 특히 메콩델타 내수면 어업은 별도 규정 적용됩니다.",
            "commonMistakes": [
                {
                    "mistake": "'어업허가'를 'cho phép đánh cá'로 표현",
                    "correction": "giấy phép đánh bắt / giấy phép khai thác thủy sản",
                    "explanation": "'cho phép'은 동사, 'giấy phép'은 명사(허가증)"
                },
                {
                    "mistake": "한국의 '신고 어업'을 'đăng ký'로만 번역",
                    "correction": "문맥에 따라 giấy phép 필요 여부 확인",
                    "explanation": "베트남은 소규모도 giấy phép 필요한 경우 많음"
                },
                {
                    "mistake": "'조업 구역'을 'khu vực làm việc'로 표현",
                    "correction": "vùng khai thác / vùng đánh bắt",
                    "explanation": "'làm việc'은 일반 업무, 어업은 'khai thác/đánh bắt' 사용"
                }
            ],
            "examples": [
                {
                    "ko": "연안 어업허가를 갱신하려면 어떤 서류가 필요합니까?",
                    "vi": "Cần giấy tờ gì để gia hạn giấy phép đánh bắt ven bờ?",
                    "situation": "formal"
                },
                {
                    "ko": "허가 없이 조업하면 벌금 5천만 동입니다.",
                    "vi": "Đánh bắt không giấy phép bị phạt 50 triệu đồng.",
                    "situation": "onsite"
                },
                {
                    "ko": "이 해역은 어업허가 대상 구역입니다.",
                    "vi": "Vùng biển này yêu cầu giấy phép khai thác thủy sản.",
                    "situation": "formal"
                }
            ],
            "relatedTerms": ["luật thủy sản", "đăng ký tàu cá", "vùng cấm đánh bắt", "kiểm tra hải sản"]
        },
        {
            "slug": "bao-ve-nguon-loi-thuy-san",
            "korean": "수산자원보호",
            "vietnamese": "Bảo vệ nguồn lợi thủy sản",
            "hanja": "水産資源保護",
            "hanjaReading": "水(물 수) + 産(날 산) + 資(재물 자) + 源(근원 원) + 保(지킬 보) + 護(도울 호)",
            "pronunciation": "바오 베 응우언 러이 투이 산",
            "meaningKo": "수산 생물의 종 다양성과 개체 수를 유지하기 위한 법적·행정적 조치로, 금어기, 금지 어구, 최소 어획 크기, 보호 구역 지정 등을 포함합니다. 베트남은 'bảo tồn đa dạng sinh học biển'(해양 생물 다양성 보전)과 연계돼 관리됩니다. 통역 시 한국은 '자원관리'와 '환경보호'를 구분하지만 베트남은 'bảo vệ nguồn lợi'로 통합하므로, 한국 측 설명 시 환경법과의 중복을 정리해야 합니다. 또한 베트남은 맹그로브 숲 보호가 수산자원 보호의 핵심이라 육상 생태계와 연계된 설명이 필요합니다.",
            "meaningVi": "Các biện pháp bảo vệ, khôi phục và phát triển bền vững nguồn lợi thủy sản. Bao gồm quy định thời vụ cấm đánh bắt, kích cỡ tối thiểu, bảo vệ khu vực sinh sản, hạn chế ngư cụ khai thác. Gắn liền với bảo vệ rừng ngập mặn, san hô.",
            "context": "legal|environmental",
            "culturalNote": "베트남은 남중국해 분쟁으로 수산자원 보호가 주권 문제와 연결됩니다. 한국은 TAC(총허용어획량) 중심이지만 베트남은 보호구역 확대 중심이라 접근법이 다릅니다. 메콩델타는 담수 어류 자원 고갈이 심각해 정부가 '4년 금어' 등 강력한 조치를 시행 중입니다. 통역 시 환경 NGO와 어민 간 갈등 맥락도 이해해야 합니다.",
            "commonMistakes": [
                {
                    "mistake": "'자원보호'를 'bảo vệ tài nguyên'으로만 번역",
                    "correction": "bảo vệ nguồn lợi thủy sản",
                    "explanation": "'nguồn lợi'는 생물 자원 특화 용어, 'tài nguyên'은 광물 등 포괄"
                },
                {
                    "mistake": "'금어기'를 'thời gian cấm'으로 표현",
                    "correction": "thời vụ cấm đánh bặt",
                    "explanation": "어업 전문 용어 'thời vụ' 사용 필수"
                },
                {
                    "mistake": "환경보호법과 수산법을 혼동",
                    "correction": "수산자원은 Luật Thủy sản, 일반 환경은 Luật Bảo vệ môi trường",
                    "explanation": "법 체계 구분 명확히 해야 함"
                }
            ],
            "examples": [
                {
                    "ko": "산란기 수산자원보호를 위해 6월은 금어기입니다.",
                    "vi": "Tháng 6 là thời vụ cấm đánh bắt để bảo vệ nguồn lợi thủy sản mùa sinh sản.",
                    "situation": "formal"
                },
                {
                    "ko": "이 해역은 수산자원보호구역으로 지정되었습니다.",
                    "vi": "Vùng biển này được chỉ định là khu bảo vệ nguồn lợi thủy sản.",
                    "situation": "onsite"
                },
                {
                    "ko": "치어 포획 금지는 자원보호의 핵심입니다.",
                    "vi": "Cấm bắt cá con là trọng tâm của bảo vệ nguồn lợi.",
                    "situation": "formal"
                }
            ],
            "relatedTerms": ["thời vụ cấm đánh bắt", "khu bảo tồn biển", "kích cỡ tối thiểu", "rừng ngập mặn"]
        },
        {
            "slug": "luat-chan-nuoi",
            "korean": "축산법",
            "vietnamese": "Luật Chăn nuôi",
            "hanja": "畜産法",
            "hanjaReading": "畜(기를 축) + 産(날 산) + 法(법 법)",
            "pronunciation": "루엇 찬 누오이",
            "meaningKo": "가축의 사육, 방역, 도축, 유통 등을 규율하는 법률로, 베트남은 2018년 전면 개정되어 대규모 축산 단지 환경 기준이 강화되었습니다. 한국의 축산법과 유사하나 베트남은 소규모 가정 축산이 많아 '농가 사육'과 '기업 축산' 규정이 이원화되어 있습니다. 통역 시 한국은 '가축분뇨법'이 별도이지만 베트남은 축산법에 통합되어 있어 환경 규제 설명 시 혼동 주의가 필요합니다. 또한 베트nam은 돼지고기 소비가 압도적이라 '돼지 축산' 규정이 특히 상세합니다.",
            "meaningVi": "Luật quy định về quản lý chăn nuôi gia súc, gia cầm, bao gồm nuôi nhốt, giết mổ, kiểm dịch, xử lý chất thải chăn nuôi. Áp dụng cho cả nông hộ và doanh nghiệp chăn nuôi quy mô lớn. Quy định nghiêm ngặt về vệ sinh thú y và môi trường.",
            "context": "legal|agricultural",
            "culturalNote": "베트남은 아프리카돼지열병(ASF)으로 2019년 돼지 400만 마리가 살처분되면서 축산법 방역 규정이 대폭 강화되었습니다. 한국은 HACCP 중심이지만 베트남은 지방 수의국의 정기 검사가 핵심입니다. 농촌 지역은 여전히 가정 내 소규모 사육이 많아 법 적용이 느슨하므로, 기업 투자 시 현지 관행과 법 규정의 괴리를 인지해야 합니다.",
            "commonMistakes": [
                {
                    "mistake": "'축산법'을 'Luật nuôi súc vật'로 번역",
                    "correction": "Luật Chăn nuôi",
                    "explanation": "공식 법률명은 'Luật Chăn nuôi' 고정"
                },
                {
                    "mistake": "'가축분뇨'를 'phân động vật'로만 표현",
                    "correction": "chất thải chăn nuôi",
                    "explanation": "'chất thải chăn nuôi'가 법률 용어"
                },
                {
                    "mistake": "한국 축산법 체계를 그대로 설명",
                    "correction": "베트남은 도축·방역·환경이 통합된 구조",
                    "explanation": "법 체계 차이로 혼란 발생 가능"
                }
            ],
            "examples": [
                {
                    "ko": "축산법에 따라 대규모 농장은 환경영향평가를 받아야 합니다.",
                    "vi": "Theo Luật Chăn nuôi, trang trại quy mô lớn phải đánh giá tác động môi trường.",
                    "situation": "formal"
                },
                {
                    "ko": "축산법 위반으로 농장이 폐쇄 명령을 받았습니다.",
                    "vi": "Trang trại bị lệnh đóng cửa do vi phạm Luật Chăn nuôi.",
                    "situation": "onsite"
                },
                {
                    "ko": "돼지 사육은 축산법상 허가 대상입니다.",
                    "vi": "Chăn nuôi lợn thuộc diện phải xin phép theo Luật Chăn nuôi.",
                    "situation": "formal"
                }
            ],
            "relatedTerms": ["kiểm dịch động vật", "chất thải chăn nuôi", "vệ sinh thú y", "giết mổ gia súc"]
        },
        {
            "slug": "kiem-dich-dong-vat",
            "korean": "동물검역",
            "vietnamese": "Kiểm dịch động vật",
            "hanja": "動物檢疫",
            "hanjaReading": "動(움직일 동) + 物(만물 물) + 檢(조사할 검) + 疫(전염병 역)",
            "pronunciation": "끼엠 짓 동 밧",
            "meaningKo": "가축 및 동물성 제품의 국내 이동이나 수출입 시 전염병 확산 방지를 위해 실시하는 검사 및 격리 조치입니다. 베트남은 구제역, 조류독감, 아프리카돼지열병 등이 자주 발생해 검역이 매우 엄격합니다. 통역 시 한국은 농림축산검역본부가 일원화되어 있지만 베트남은 국경 검역(Chi cục Kiểm dịch)과 국내 검역(Chi cục Thú y)이 분리되어 있어 업무 범위를 명확히 구분해야 합니다. 또한 베트남은 중국 국경을 통한 밀수입 동물이 많아 '밀수 검역 회피' 문제가 심각합니다.",
            "meaningVi": "Hoạt động kiểm tra, giám sát động vật, sản phẩm động vật xuất nhập khẩu hoặc vận chuyển nội địa để phòng chống dịch bệnh. Bao gồm kiểm tra lâm sàng, xét nghiệm, cách ly kiểm dịch. Do Chi cục Kiểm dịch động vật thực hiện.",
            "context": "legal|trade",
            "culturalNote": "베트남은 중국·라오스·캄보디아 국경에서 불법 가축 유입이 많아 검역 시스템이 취약합니다. 한국 축산 기업이 베트남 진출 시 공식 검역 절차를 밟아도 현지 농장에서 검역되지 않은 가축과 접촉 가능성이 있어 주의가 필요합니다. 특히 돼지 수입은 ASF 이후 거의 중단 상태이고, 소·닭은 태국·호주산이 주류입니다.",
            "commonMistakes": [
                {
                    "mistake": "'검역'을 'kiểm tra'로만 번역",
                    "correction": "kiểm dịch",
                    "explanation": "'kiểm tra'는 일반 검사, 'kiểm dịch'는 방역 검사"
                },
                {
                    "mistake": "'검역소'를 'trạm kiểm dịch'로 표현",
                    "correction": "Chi cục Kiểm dịch động vật",
                    "explanation": "공식 기관명 사용 필수"
                },
                {
                    "mistake": "식물검역과 동물검역 용어 혼용",
                    "correction": "động vật(동물), thực vật(식물) 명확히 구분",
                    "explanation": "검역 대상에 따라 용어·절차·기관 다름"
                }
            ],
            "examples": [
                {
                    "ko": "수입 소는 30일 검역 격리가 필수입니다.",
                    "vi": "Bò nhập khẩu phải cách ly kiểm dịch 30 ngày.",
                    "situation": "formal"
                },
                {
                    "ko": "검역증명서 없이는 통관이 불가능합니다.",
                    "vi": "Không có giấy chứng nhận kiểm dịch thì không thể thông quan.",
                    "situation": "onsite"
                },
                {
                    "ko": "동물검역법에 따라 모든 가축은 검사를 받습니다.",
                    "vi": "Theo pháp luật kiểm dịch động vật, mọi gia súc đều phải kiểm tra.",
                    "situation": "formal"
                }
            ],
            "relatedTerms": ["kiểm dịch thực vật", "chứng nhận kiểm dịch", "cách ly kiểm dịch", "dịch bệnh gia súc"]
        },
        {
            "slug": "kiem-dich-thuc-vat",
            "korean": "식물검역",
            "vietnamese": "Kiểm dịch thực vật",
            "hanja": "植物檢疫",
            "hanjaReading": "植(심을 식) + 物(만물 물) + 檢(조사할 검) + 疫(전염병 역)",
            "pronunciation": "끼엠 짓 턱 밧",
            "meaningKo": "식물, 종자, 과일 등의 수출입 또는 국내 이동 시 병해충 확산 방지를 위해 실시하는 검사 및 소독 조치입니다. 베트남은 과일 수출국으로 'kiểm dịch thực vật xuất khẩu'(수출 식물검역)이 특히 중요하며, 한국·일본·미국 등으로의 과일 수출 시 잔류농약 검사가 엄격합니다. 통역 시 한국은 '식물방역법'이지만 베트남은 '식물보호법'(Luật Bảo vệ và Kiểm dịch thực vật)으로 검역과 병해충 방제가 통합되어 있습니다. 또한 베트남은 목재 포장재(pallet) 검역도 포함되므로 화물 운송 시 별도 확인이 필요합니다.",
            "meaningVi": "Hoạt động kiểm tra, giám sát thực vật, sản phẩm thực vật xuất nhập khẩu để ngăn chặn sâu bệnh xâm nhập. Bao gồm kiểm tra dịch hại, xử lý tiêu độc, cấp giấy chứng nhận kiểm dịch. Thuộc Chi cục Bảo vệ thực vật.",
            "context": "legal|trade",
            "culturalNote": "베트남은 망고·용과·리치 등 열대과일 수출이 주력이라 식물검역이 경제적으로 중요합니다. 한국으로의 과일 수출은 '훈증 처리'(xử lý hóa chất)가 필수이며, 미국은 '조사 처리'(xử lý phóng xạ)를 요구합니다. 통역 시 검역 방법의 차이를 정확히 전달해야 무역 분쟁을 예방할 수 있습니다. 또한 베트남은 중국산 농산물 밀수입이 많아 원산지 증명과 검역의 연계가 중요합니다.",
            "commonMistakes": [
                {
                    "mistake": "'식물검역'을 'kiểm tra cây cối'로 번역",
                    "correction": "kiểm dịch thực vật",
                    "explanation": "'cây cối'는 나무만, 'thực vật'은 식물 전반"
                },
                {
                    "mistake": "'병해충'을 'côn trùng'으로만 표현",
                    "correction": "sâu bệnh hại",
                    "explanation": "'sâu bệnh'은 병해충 전문 용어"
                },
                {
                    "mistake": "'훈증 소독'을 'khử trùng'으로만 번역",
                    "correction": "xử lý hóa chất / hun trùng",
                    "explanation": "'hun trùng'이 검역 전문 용어"
                }
            ],
            "examples": [
                {
                    "ko": "망고 수출은 식물검역 증명서가 필수입니다.",
                    "vi": "Xuất khẩu xoài phải có giấy chứng nhận kiểm dịch thực vật.",
                    "situation": "formal"
                },
                {
                    "ko": "목재 포장재도 식물검역 대상입니다.",
                    "vi": "Bao bì gỗ cũng thuộc đối tượng kiểm dịch thực vật.",
                    "situation": "onsite"
                },
                {
                    "ko": "병해충 발견 시 화물은 폐기됩니다.",
                    "vi": "Nếu phát hiện sâu bệnh, hàng hóa sẽ bị tiêu hủy.",
                    "situation": "formal"
                }
            ],
            "relatedTerms": ["kiểm dịch động vật", "sâu bệnh hại", "giấy chứng nhận kiểm dịch", "xử lý hóa chất"]
        },
        {
            "slug": "nong-nghiep-huu-co",
            "korean": "유기농업",
            "vietnamese": "Nông nghiệp hữu cơ",
            "hanja": "有機農業",
            "hanjaReading": "有(있을 유) + 機(틀 기) + 農(농사 농) + 業(업 업)",
            "pronunciation": "농 응이엡 흐우 꺼",
            "meaningKo": "화학비료와 농약을 사용하지 않고 유기물과 자연 순환을 활용하는 농업 방식으로, 베트남은 'nông nghiệp sạch'(청정농업)와 구분됩니다. 유기농은 국제 인증(USDA, EU) 기준을 충족해야 하지만 청정농업은 베트남 국내 기준입니다. 통역 시 한국 의뢰인이 '친환경 농산물'을 언급하면 베트남에서는 유기·무농약·저농약의 3단계 구분이 없고 'hữu cơ'(유기) 아니면 'thông thường'(일반)으로만 나뉘므로 혼동 방지가 필요합니다. 또한 베트남은 유기농 인증 비용이 높아 소농이 접근하기 어려워 '자칭 유기농' 판매가 많습니다.",
            "meaningVi": "Phương thức sản xuất nông nghiệp không sử dụng phân bón hóa học, thuốc trừ sâu tổng hợp, chỉ dùng phân hữu cơ và biện pháp sinh học. Cần chứng nhận quốc tế hoặc trong nước. Khác với 'nông nghiệp sạch' là tiêu chuẩn nội địa.",
            "context": "legal|agricultural",
            "culturalNote": "베트남은 유기농 시장이 성장 중이나 인증 시스템이 취약해 '가짜 유기농' 문제가 심각합니다. 한국은 친환경인증제가 정착되어 있지만 베트남은 국제 인증(IFOAM, USDA Organic)을 받아야 수출이 가능합니다. 달랏(Đà Lạt) 지역이 유기농 채소 중심지이며, 메콩델타는 유기농 쌀 생산이 늘고 있습니다. 통역 시 '유기농'과 '무농약'의 차이를 명확히 해야 소비자 신뢰를 확보할 수 있습니다.",
            "commonMistakes": [
                {
                    "mistake": "'유기농'을 'nông nghiệp sạch'로 번역",
                    "correction": "nông nghiệp hữu cơ",
                    "explanation": "'sạch'는 청정농업(저농약), 'hữu cơ'는 유기농(무농약)"
                },
                {
                    "mistake": "'친환경'을 'thân thiện môi trường'으로 직역",
                    "correction": "문맥에 따라 hữu cơ / sạch / VietGAP",
                    "explanation": "베트남은 인증 체계가 달라 정확한 용어 선택 필요"
                },
                {
                    "mistake": "한국 친환경 3단계를 그대로 설명",
                    "correction": "베트남은 hữu cơ(유기) / VietGAP(안전) / thông thường(일반)",
                    "explanation": "인증 체계 차이로 혼란 방지"
                }
            ],
            "examples": [
                {
                    "ko": "유기농 인증을 받으려면 3년간 무농약 재배가 필수입니다.",
                    "vi": "Để được chứng nhận hữu cơ, phải trồng không thuốc hóa học trong 3 năm.",
                    "situation": "formal"
                },
                {
                    "ko": "이 쌀은 유기농 인증을 받았습니다.",
                    "vi": "Gạo này đã được chứng nhận nông nghiệp hữu cơ.",
                    "situation": "onsite"
                },
                {
                    "ko": "유기농 시장은 매년 20% 성장하고 있습니다.",
                    "vi": "Thị trường nông nghiệp hữu cơ tăng trưởng 20% mỗi năm.",
                    "situation": "formal"
                }
            ],
            "relatedTerms": ["chứng nhận hữu cơ", "nông nghiệp sạch", "VietGAP", "phân hữu cơ"]
        },
        {
            "slug": "bao-ho-giong-cay-trong",
            "korean": "식물신품종보호",
            "vietnamese": "Bảo hộ giống cây trồng",
            "hanja": "植物新品種保護",
            "hanjaReading": "植(심을 식) + 物(만물 물) + 新(새 신) + 品(물건 품) + 種(씨 종) + 保(지킬 보) + 護(도울 호)",
            "pronunciation": "바오 호 종 까이 쫑",
            "meaningKo": "육종가가 개발한 신품종 식물에 대해 일정 기간 독점적 권리를 부여하는 제도로, UPOV 협약(국제식물신품종보호동맹)에 기반합니다. 베트남은 2006년 UPOV에 가입했으며 'Luật Sở hữu trí tuệ'(지식재산법) 내에서 보호됩니다. 통역 시 한국은 '품종보호법'이 별도이지만 베트남은 지식재산법에 통합되어 있어 특허·상표와 함께 설명됩니다. 또한 베트남은 쌀·커피 품종 보호가 중요하며, 농민이 보호 품종을 무단 재배하는 경우가 많아 단속이 강화되고 있습니다.",
            "meaningVi": "Chế độ bảo hộ quyền đối với giống cây trồng mới do tổ chức, cá nhân tạo ra. Quy định trong Luật Sở hữu trí tuệ, theo Công ước UPOV. Người tạo giống có quyền độc quyền sản xuất, bán giống trong thời hạn nhất định.",
            "context": "legal|agricultural",
            "culturalNote": "베트남은 쌀 품종(IR50404, OM18)과 커피(Robusta clones) 품종 보호가 핵심입니다. 한국 종자 기업이 베트남 진출 시 품종 도용 위험이 크므로 사전 등록이 필수입니다. 베트남 농민은 '자가 채종' 관행이 강해 보호 품종의 종자를 불법 유통하는 경우가 많아 법적 분쟁 소지가 있습니다. 특히 고추·토마토 하이브리드 종자는 중국산 모방품이 많습니다.",
            "commonMistakes": [
                {
                    "mistake": "'품종보호'를 'bảo vệ giống'으로 번역",
                    "correction": "bảo hộ giống cây trồng",
                    "explanation": "'bảo hộ'는 법적 보호, 'bảo vệ'는 일반 보호"
                },
                {
                    "mistake": "'신품종'을 'giống mới'로만 표현",
                    "correction": "giống cây trồng mới được bảo hộ",
                    "explanation": "법률 용어는 'bảo hộ' 포함 필수"
                },
                {
                    "mistake": "특허와 품종보호를 혼동",
                    "correction": "특허(sáng chế)는 기술, 품종보호(bảo hộ giống)는 식물",
                    "explanation": "지식재산 유형 구분 필요"
                }
            ],
            "examples": [
                {
                    "ko": "이 쌀 품종은 20년간 보호됩니다.",
                    "vi": "Giống lúa này được bảo hộ trong 20 năm.",
                    "situation": "formal"
                },
                {
                    "ko": "품종보호 등록 없이 판매하면 불법입니다.",
                    "vi": "Bán giống chưa đăng ký bảo hộ là vi phạm pháp luật.",
                    "situation": "onsite"
                },
                {
                    "ko": "신품종 개발자는 로열티를 받을 권리가 있습니다.",
                    "vi": "Người tạo giống mới có quyền nhận tiền bản quyền.",
                    "situation": "formal"
                }
            ],
            "relatedTerms": ["sở hữu trí tuệ", "giống cây trồng", "đăng ký bảo hộ", "quyền tác giả"]
        },
        {
            "slug": "hop-tac-xa-nong-nghiep",
            "korean": "농업협동조합",
            "vietnamese": "Hợp tác xã nông nghiệp",
            "hanja": "農業協同組合",
            "hanjaReading": "農(농사 농) + 業(업 업) + 協(협력할 협) + 同(한가지 동) + 組(짤 조) + 合(합할 합)",
            "pronunciation": "헙 탁 싸 농 응이엡",
            "meaningKo": "농민들이 자발적으로 결성하여 공동 생산·구매·판매·신용 활동을 수행하는 조직으로, 베트남은 'HTX'로 약칭합니다. 사회주의 체제 잔재로 과거 강제 집단농장의 이미지가 있어 한국의 농협과 달리 신뢰도가 낮습니다. 통역 시 한국 농협은 정부 지원 금융기관이지만 베트남 HTX는 순수 민간 조직이라 역할과 권한이 다릅니다. 또한 베트남은 2012년 협동조합법 개정으로 '신형 협동조합' 육성 중이며, 커피·후추·쌀 수출 HTX가 성장하고 있습니다.",
            "meaningVi": "Tổ chức kinh tế tập thể do nông dân tự nguyện thành lập, hoạt động theo Luật Hợp tác xã. Mục đích hỗ trợ thành viên trong sản xuất, tiêu thụ, mua sắm vật tư, tín dụng. HTX mới theo mô hình thị trường, khác HTX cũ thời bao cấp.",
            "context": "legal|economic",
            "culturalNote": "베트남은 1980~90년대 집단농장 실패로 협동조합에 대한 불신이 깊습니다. 현재는 '신형 HTX' 육성 정책으로 자율성이 강화되었으나 여전히 형식적인 곳이 많습니다. 한국 농협과 달리 금융 기능이 약하고, 주로 비료 공동 구매나 농산물 공동 판매에 집중합니다. 메콩델타의 쌀 HTX, 중부 고원의 커피 HTX가 대표적이며, 유기농 인증도 HTX 단위로 받는 경우가 많습니다.",
            "commonMistakes": [
                {
                    "mistake": "'농협'을 'Nông hiệp'로 음역",
                    "correction": "Hợp tác xã nông nghiệp (HTX)",
                    "explanation": "베트남 공식 용어 사용 필수"
                },
                {
                    "mistake": "한국 농협의 금융 기능을 그대로 설명",
                    "correction": "베트남 HTX는 금융 기능 약함",
                    "explanation": "조직 구조와 기능이 완전히 다름"
                },
                {
                    "mistake": "'조합원'을 'thành viên hợp tác'으로 표현",
                    "correction": "xã viên / thành viên HTX",
                    "explanation": "'xã viên'이 정확한 용어"
                }
            ],
            "examples": [
                {
                    "ko": "우리 마을은 농업협동조합을 설립했습니다.",
                    "vi": "Làng chúng tôi đã thành lập hợp tác xã nông nghiệp.",
                    "situation": "formal"
                },
                {
                    "ko": "협동조합을 통해 비료를 싸게 삽니다.",
                    "vi": "Qua HTX, chúng tôi mua phân bón giá rẻ.",
                    "situation": "informal"
                },
                {
                    "ko": "이 커피 협동조합은 유기농 인증을 받았습니다.",
                    "vi": "HTX cà phê này đã được chứng nhận hữu cơ.",
                    "situation": "formal"
                }
            ],
            "relatedTerms": ["xã viên", "hợp tác xã", "liên hiệp hợp tác xã", "quỹ hỗ trợ nông dân"]
        },
        {
            "slug": "chinh-sach-nong-nghiep",
            "korean": "농업정책",
            "vietnamese": "Chính sách nông nghiệp",
            "hanja": "農業政策",
            "hanjaReading": "農(농사 농) + 業(업 업) + 政(정사 정) + 策(꾀 책)",
            "pronunciation": "찐 삭 농 응이엡",
            "meaningKo": "정부가 농업 생산성 향상, 농가 소득 증대, 농촌 개발, 식량 안보 등을 목적으로 수립·시행하는 정책입니다. 베트남은 '3농 정책'(nông nghiệp-nông dân-nông thôn: 농업-농민-농촌)이 핵심이며, 쌀 수출 정책과 토지 사용권 정책이 가장 민감합니다. 통역 시 한국은 쌀 수매제·직불제가 중심이지만 베트남은 토지 사용권 50년 연장, 쌀 수출 쿼터제, 고부가 작물 전환 지원이 핵심이라 정책 방향이 다릅니다. 또한 베트남은 중국 의존도를 낮추기 위해 비료·농약 국산화 정책을 추진 중입니다.",
            "meaningVi": "Hệ thống chính sách của Nhà nước nhằm phát triển nông nghiệp, tăng thu nhập nông dân, xây dựng nông thôn mới. Bao gồm chính sách đất đai, tín dụng, khuyến nông, xuất khẩu nông sản, chuyển đổi cây trồng.",
            "context": "legal|political",
            "culturalNote": "베트남 농업정책은 공산당 5개년 계획에 따라 결정되며, 최근 '고부가 농업'(nông nghiệp công nghệ cao)과 '스마트 농업'(nông nghiệp thông minh) 육성이 핵심입니다. 한국과 달리 토지 국유제라 '토지 사용권' 정책이 가장 중요하며, 외국인 토지 취득 제한으로 한국 기업은 장기 임대 방식으로 진출해야 합니다. 쌀 가격 정책은 메콩델타 농민 생계와 직결되어 정치적으로 민감합니다.",
            "commonMistakes": [
                {
                    "mistake": "'농업정책'을 'chính sách về nông nghiệp'로 번역",
                    "correction": "chính sách nông nghiệp",
                    "explanation": "관용 표현으로 'về' 불필요"
                },
                {
                    "mistake": "한국 쌀 수매제를 그대로 설명",
                    "correction": "베트남은 시장 가격 중심, 정부 개입 제한적",
                    "explanation": "정책 메커니즘이 완전히 다름"
                },
                {
                    "mistake": "'농지'를 'đất nông nghiệp'으로만 표현",
                    "correction": "문맥에 따라 đất nông nghiệp / quyền sử dụng đất",
                    "explanation": "토지 소유권 vs 사용권 구분 필수"
                }
            ],
            "examples": [
                {
                    "ko": "새 농업정책은 유기농 전환을 지원합니다.",
                    "vi": "Chính sách nông nghiệp mới hỗ trợ chuyển đổi sang hữu cơ.",
                    "situation": "formal"
                },
                {
                    "ko": "정부는 농업정책으로 쌀 수출을 장려합니다.",
                    "vi": "Chính phủ khuyến khích xuất khẩu gạo qua chính sách nông nghiệp.",
                    "situation": "formal"
                },
                {
                    "ko": "이번 농업정책은 스마트팜 확대가 목표입니다.",
                    "vi": "Chính sách nông nghiệp lần này nhắm mở rộng nông trại thông minh.",
                    "situation": "formal"
                }
            ],
            "relatedTerms": ["chính sách đất đai", "nông nghiệp công nghệ cao", "nông thôn mới", "xuất khẩu nông sản"]
        }
    ]

    # 중복 제거 후 추가
    added_count = 0
    skipped_slugs = []

    for term in new_terms:
        if term['slug'] not in existing_slugs:
            data.append(term)
            existing_slugs.add(term['slug'])
            added_count += 1
            print(f"✅ Added: {term['slug']} ({term['korean']})")
        else:
            skipped_slugs.append(term['slug'])
            print(f"⚠️  Skipped (duplicate): {term['slug']}")

    # 파일 저장
    with open(file_path, 'w', encoding='utf-8') as f:
        json.dump(data, f, ensure_ascii=False, indent=2)

    # 결과 출력
    print(f"\n{'='*60}")
    print(f"✅ 완료: {added_count}개 용어 추가")
    if skipped_slugs:
        print(f"⚠️  중복 스킵: {len(skipped_slugs)}개 - {', '.join(skipped_slugs)}")
    print(f"📊 총 용어 수: {len(data)}개")
    print(f"💾 저장 위치: {file_path}")
    print(f"{'='*60}")

if __name__ == "__main__":
    main()
