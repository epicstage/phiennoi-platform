#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
건설 IT/관리시스템 용어 추가 스크립트
테마: PMIS, CALS, 전자조달, 원가관리시스템, 안전관리시스템, 하자관리시스템, 전자입찰, 전자계약, 현장CCTV, 출입관리시스템
10개 용어 - Tier S 품질 기준
"""

import json
import os.path

# 추가할 용어 데이터 (10개)
data = [
    {
        "slug": "he-thong-quan-ly-du-an",
        "korean": "프로젝트 관리 정보 시스템",
        "vietnamese": "Hệ thống quản lý dự án (PMIS)",
        "hanja": "工事管理情報體系",
        "hanjaReading": "工(장인 공) + 事(일 사) + 管(대롱 관) + 理(다스릴 리) + 情(뜻 정) + 報(알릴 보) + 體(몸 체) + 系(맬 계)",
        "pronunciation": "프로젝트 관리 정보 시스템 [PMIS: 피엠아이에스]",
        "meaningKo": "건설 프로젝트의 공정, 예산, 품질, 안전 등 전 과정을 통합 관리하는 정보시스템입니다. PMIS(Project Management Information System)는 프로젝트의 계획부터 준공까지 모든 데이터를 실시간으로 관리하며, 의사결정을 지원합니다. 통역 시 '시스템'과 '프로그램'을 혼동하지 않도록 주의해야 하며, PMIS는 단순 소프트웨어가 아닌 통합 관리 체계임을 강조해야 합니다. 한국에서는 대형 건설사마다 자체 PMIS를 운영하며, 베트남에서는 '프로젝트 관리 시스템' 도입이 확대되고 있습니다.",
        "meaningVi": "Hệ thống thông tin quản lý dự án xây dựng, tích hợp quản lý tiến độ, ngân sách, chất lượng, an toàn từ lập kế hoạch đến nghiệm thu. PMIS hỗ trợ ra quyết định theo thời gian thực và là hệ thống quản lý tổng thể, không chỉ là phần mềm đơn lẻ.",
        "context": "IT시스템, 프로젝트 관리, 건설정보화",
        "culturalNote": "한국 대형 건설사는 자체 PMIS를 필수로 운영하며 공공공사는 시스템 도입이 의무화되어 있습니다. 베트남에서는 PMIS 도입이 시작 단계이며 대부분 외국계 또는 대형 프로젝트에서만 사용됩니다. 한국은 클라우드 기반 모바일 PMIS가 보편화되어 있으나, 베트남은 아직 데스크톱 기반이 많습니다. 통역 시 'hệ thống'(시스템)과 'phần mềm'(소프트웨어)를 명확히 구분해야 합니다.",
        "commonMistakes": [
            {
                "mistake": "PMIS를 '프로그램'으로 번역",
                "correction": "Hệ thống quản lý dự án (시스템으로 표현)",
                "explanation": "PMIS는 단순 프로그램이 아닌 통합 관리 시스템이므로 'chương trình'보다 'hệ thống'이 적절합니다."
            },
            {
                "mistake": "공정관리시스템과 혼동",
                "correction": "PMIS는 공정+예산+품질+안전 통합",
                "explanation": "공정관리는 PMIS의 일부 기능일 뿐이며, PMIS는 프로젝트 전반을 관리하는 상위 개념입니다."
            },
            {
                "mistake": "'hệ thống thông tin'을 생략",
                "correction": "반드시 'hệ thống thông tin quản lý dự án'으로 완전 표현",
                "explanation": "정보시스템임을 명시해야 단순 관리 방법론과 구분됩니다."
            }
        ],
        "examples": [
            {
                "ko": "당사는 자체 PMIS를 통해 전국 50개 현장을 실시간으로 모니터링합니다.",
                "vi": "Công ty chúng tôi giám sát thời gian thực 50 công trường trên toàn quốc thông qua hệ thống PMIS tự phát triển.",
                "situation": "formal"
            },
            {
                "ko": "PMIS에 일일 공정 데이터를 입력해 주세요.",
                "vi": "Vui lòng nhập dữ liệu tiến độ hàng ngày vào hệ thống PMIS.",
                "situation": "onsite"
            },
            {
                "ko": "모바일 PMIS 앱으로 현장에서 바로 보고서 작성이 가능합니다.",
                "vi": "Có thể lập báo cáo trực tiếp tại công trường bằng ứng dụng PMIS di động.",
                "situation": "formal"
            }
        ],
        "relatedTerms": ["공정관리시스템", "통합관리시스템", "건설정보화", "클라우드 시스템"]
    },
    {
        "slug": "he-thong-cals",
        "korean": "건설사업관리시스템",
        "vietnamese": "Hệ thống CALS",
        "hanja": "建設事業管理體系",
        "hanjaReading": "建(세울 건) + 設(베풀 설) + 事(일 사) + 業(업 업) + 管(대롱 관) + 理(다스릴 리) + 體(몸 체) + 系(맬 계)",
        "pronunciation": "건설 사업 관리 시스템 [CALS: 칼스]",
        "meaningKo": "CALS(Commerce At Light Speed)는 건설 생애주기 전반의 정보를 전자적으로 생성, 교환, 관리, 재활용하는 통합 정보 시스템입니다. 설계도면, 시방서, 준공도서 등을 전자문서로 관리하며 발주자-시공사-감리 간 정보 공유를 실시간으로 지원합니다. 통역 시 'CALS'를 그대로 사용하되 '전자문서 관리 시스템'으로 부연 설명해야 하며, 단순 문서 보관이 아닌 '정보 교환 및 재활용' 체계임을 강조해야 합니다. 한국 공공공사는 CALS 적용이 의무화되어 있습니다.",
        "meaningVi": "Hệ thống trao đổi và quản lý thông tin điện tử trong toàn bộ vòng đời xây dựng, bao gồm bản vẽ, tiêu chuẩn kỹ thuật, hồ sơ hoàn công. Hỗ trợ chia sẻ thông tin thời gian thực giữa chủ đầu tư, nhà thầu, giám sát.",
        "context": "전자문서, 공공공사, 정보화시스템",
        "culturalNote": "한국에서는 2000년대 초반부터 공공공사에 CALS 적용이 법적으로 의무화되어 있으며, 모든 도면과 문서를 전자파일로 제출해야 합니다. 베트남에서는 CALS 개념이 생소하며 대부분 종이 도면과 수기 문서를 병행합니다. 한국은 CALS-EC(전자조달 연계)까지 발전했으나, 베트남은 기본적인 전자문서 관리 단계입니다. 통역 시 'tài liệu điện tử'(전자문서)를 강조해야 합니다.",
        "commonMistakes": [
            {
                "mistake": "CALS를 '문서 보관 시스템'으로만 설명",
                "correction": "정보 생성, 교환, 관리, 재활용의 통합 체계로 설명",
                "explanation": "CALS는 단순 보관이 아닌 정보의 전 생애주기 관리 시스템입니다."
            },
            {
                "mistake": "'hệ thống tài liệu'로만 번역",
                "correction": "Hệ thống trao đổi thông tin điện tử (전자정보 교환 시스템)",
                "explanation": "'정보 교환'이 핵심이므로 'trao đổi thông tin'을 명시해야 합니다."
            },
            {
                "mistake": "설계 단계만 적용되는 것으로 오해",
                "correction": "계획-설계-시공-유지관리 전 단계 적용",
                "explanation": "CALS는 건설 생애주기 전체를 포괄하는 시스템입니다."
            }
        ],
        "examples": [
            {
                "ko": "이 공사는 국가 발주이므로 CALS 시스템에 모든 도면을 등록해야 합니다.",
                "vi": "Đây là công trình nhà nước nên phải đăng ký toàn bộ bản vẽ lên hệ thống CALS.",
                "situation": "formal"
            },
            {
                "ko": "CALS 제출 기한이 내일까지니까 서류 확인 부탁드립니다.",
                "vi": "Hạn nộp CALS là đến ngày mai, vui lòng kiểm tra hồ sơ.",
                "situation": "onsite"
            },
            {
                "ko": "CALS를 통해 실시간으로 공정률을 확인할 수 있습니다.",
                "vi": "Có thể xác nhận tỷ lệ tiến độ theo thời gian thực qua hệ thống CALS.",
                "situation": "formal"
            }
        ],
        "relatedTerms": ["전자문서", "공공공사", "전자조달", "BIM"]
    },
    {
        "slug": "he-thong-dau-thau-dien-tu",
        "korean": "전자입찰시스템",
        "vietnamese": "Hệ thống đấu thầu điện tử",
        "hanja": "電子入札體系",
        "hanjaReading": "電(번개 전) + 子(아들 자) + 入(들 입) + 札(편지 찰) + 體(몸 체) + 系(맬 계)",
        "pronunciation": "전자 입찰 시스템",
        "meaningKo": "건설공사 입찰을 인터넷을 통해 전자적으로 진행하는 시스템입니다. 입찰공고, 입찰서 제출, 개찰, 낙찰자 선정까지 모든 과정이 온라인으로 이루어집니다. 통역 시 '입찰'과 '낙찰'을 명확히 구분해야 하며, 한국의 나라장터(G2B), 베트남의 muasamcong.mpi.gov.vn 등 국가별 시스템 명칭을 정확히 알아야 합니다. 전자입찰은 투명성 확보와 부정 방지가 핵심 목적이며, 공인인증서 또는 디지털 서명이 필수입니다. 한국은 1억 원 이상 공사는 전자입찰이 의무화되어 있습니다.",
        "meaningVi": "Hệ thống thực hiện đấu thầu xây dựng qua internet, từ thông báo mời thầu, nộp hồ sơ, mở thầu đến công bố trúng thầu hoàn toàn trực tuyến. Yêu cầu chữ ký số và nhằm đảm bảo minh bạch.",
        "context": "입찰, 전자조달, 공공공사",
        "culturalNote": "한국은 나라장터(G2B)를 통해 모든 공공입찰이 전자화되어 있으며, 1억 원 이상 공사는 전자입찰이 의무입니다. 베트nam은 muasamcong.mpi.gov.vn 시스템이 있으나 아직 수기 입찰도 병행됩니다. 한국은 공인인증서, 베트남은 디지털 서명(chữ ký số)을 사용합니다. 한국은 최저가 낙찰제가 일반적이나, 베트남은 종합평가 낙찰제가 많습니다. 통역 시 'đấu thầu'(입찰)와 'trúng thầu'(낙찰)를 정확히 구분해야 합니다.",
        "commonMistakes": [
            {
                "mistake": "'đấu giá'(경매)로 잘못 번역",
                "correction": "đấu thầu (입찰)",
                "explanation": "경매(đấu giá)와 입찰(đấu thầu)은 완전히 다른 개념입니다."
            },
            {
                "mistake": "입찰과 낙찰을 같은 단어로 표현",
                "correction": "입찰=đấu thầu, 낙찰=trúng thầu",
                "explanation": "입찰은 참여 행위, 낙찰은 선정 결과로 구분해야 합니다."
            },
            {
                "mistake": "'hệ thống mua sắm'으로만 표현",
                "correction": "Hệ thống đấu thầu điện tử (전자입찰시스템)",
                "explanation": "'구매'가 아닌 '입찰' 개념을 명확히 해야 합니다."
            }
        ],
        "examples": [
            {
                "ko": "이번 공사는 전자입찰로 진행되며 나라장터에 등록해야 합니다.",
                "vi": "Công trình này thực hiện đấu thầu điện tử và phải đăng ký trên hệ thống G2B.",
                "situation": "formal"
            },
            {
                "ko": "전자입찰 마감일이 다음 주 금요일 오후 5시입니다.",
                "vi": "Hạn chót nộp hồ sơ đấu thầu điện tử là 5 giờ chiều thứ Sáu tuần sau.",
                "situation": "formal"
            },
            {
                "ko": "공인인증서가 없으면 전자입찰에 참여할 수 없습니다.",
                "vi": "Không có chứng thư số thì không thể tham gia đấu thầu điện tử.",
                "situation": "onsite"
            }
        ],
        "relatedTerms": ["나라장터", "공인인증서", "최저가낙찰제", "전자조달"]
    },
    {
        "slug": "hop-dong-dien-tu",
        "korean": "전자계약",
        "vietnamese": "Hợp đồng điện tử",
        "hanja": "電子契約",
        "hanjaReading": "電(번개 전) + 子(아들 자) + 契(맺을 계) + 約(맺을 약)",
        "pronunciation": "전자 계약",
        "meaningKo": "종이 문서가 아닌 전자문서 형태로 체결하는 계약을 말하며, 전자서명 또는 공인인증서로 법적 효력을 인정받습니다. 건설 현장에서는 하도급 계약, 자재 구매 계약 등에 활용되며, 계약서 작성부터 서명, 보관까지 모두 전자적으로 처리됩니다. 통역 시 '전자서명'(chữ ký điện tử)과 '디지털 서명'(chữ ký số)의 차이를 이해해야 하며, 한국에서는 공인인증서 기반, 베트남에서는 디지털 서명 기반임을 알아야 합니다. 전자계약은 종이 계약과 동등한 법적 효력을 가지며, 위변조 방지와 신속한 계약 체결이 장점입니다.",
        "meaningVi": "Hợp đồng được lập và ký kết dưới dạng tài liệu điện tử, có hiệu lực pháp lý thông qua chữ ký số. Áp dụng trong hợp đồng thầu phụ, mua vật tư xây dựng, từ soạn thảo đến lưu trữ hoàn toàn điện tử.",
        "context": "계약, 전자서명, 법률",
        "culturalNote": "한국은 전자문서법에 따라 전자계약이 법적으로 완전히 인정되며, 공인인증서 또는 민간인증서로 서명합니다. 베트남도 전자거래법(Luật Giao dịch điện tử)에 따라 전자계약이 유효하나 중요 계약은 아직 종이 계약을 선호합니다. 한국은 전자계약 플랫폼(모두싸인, 카카오 전자계약 등)이 활성화되었으나, 베트남은 아직 초기 단계입니다. 통역 시 'hợp đồng giấy'(종이 계약)와 명확히 대비해야 합니다.",
        "commonMistakes": [
            {
                "mistake": "'hợp đồng online'으로만 표현",
                "correction": "Hợp đồng điện tử (전자계약)",
                "explanation": "'online'은 구어적이며 법률 용어로는 'điện tử'를 사용해야 합니다."
            },
            {
                "mistake": "전자서명과 디지털 서명을 혼동",
                "correction": "한국=공인인증서, 베트남=chữ ký số",
                "explanation": "국가별 전자서명 체계를 정확히 알고 통역해야 합니다."
            },
            {
                "mistake": "법적 효력이 없다고 오해",
                "correction": "전자계약은 종이 계약과 동등한 법적 효력",
                "explanation": "전자문서법과 전자거래법으로 법적 효력이 보장됩니다."
            }
        ],
        "examples": [
            {
                "ko": "이번 하도급 계약은 전자계약으로 진행하며, 공인인증서로 서명해 주시기 바랍니다.",
                "vi": "Hợp đồng thầu phụ lần này thực hiện bằng hợp đồng điện tử, vui lòng ký bằng chứng thư số.",
                "situation": "formal"
            },
            {
                "ko": "전자계약은 종이 계약과 동일한 법적 효력을 가집니다.",
                "vi": "Hợp đồng điện tử có hiệu lực pháp lý tương đương hợp đồng giấy.",
                "situation": "formal"
            },
            {
                "ko": "전자계약 플랫폼에서 계약서를 다운로드할 수 있습니다.",
                "vi": "Có thể tải hợp đồng từ nền tảng hợp đồng điện tử.",
                "situation": "onsite"
            }
        ],
        "relatedTerms": ["전자서명", "공인인증서", "전자문서", "디지털 서명"]
    },
    {
        "slug": "he-thong-quan-ly-chi-phi",
        "korean": "원가관리시스템",
        "vietnamese": "Hệ thống quản lý chi phí",
        "hanja": "原價管理體系",
        "hanjaReading": "原(근원 원) + 價(값 가) + 管(대롱 관) + 理(다스릴 리) + 體(몸 체) + 系(맬 계)",
        "pronunciation": "원가 관리 시스템",
        "meaningKo": "건설공사의 예상 원가와 실제 원가를 산정, 비교, 분석하여 관리하는 정보시스템입니다. 자재비, 노무비, 경비 등 모든 비용을 실시간으로 집계하고, 예산 대비 실행 원가를 추적하여 수익성을 관리합니다. 통역 시 '원가'(chi phí gốc)와 '공사비'(chi phí xây dựng)를 구분해야 하며, 원가는 순수 투입비용, 공사비는 원가+이윤임을 설명해야 합니다. 원가관리시스템은 설계 단계 예상원가부터 시공 단계 실행원가, 준공 후 실적원가까지 전 과정을 추적하며, ERP와 연동되어 재무 관리를 지원합니다.",
        "meaningVi": "Hệ thống tính toán, so sánh và phân tích chi phí dự kiến với chi phí thực tế của công trình xây dựng. Tổng hợp vật tư, nhân công, chi phí khác theo thời gian thực, theo dõi chi phí thực hiện so với ngân sách để quản lý lợi nhuận.",
        "context": "원가, 예산, 수익성관리",
        "culturalNote": "한국 건설사는 원가관리시스템을 필수로 운영하며 공종별, 공정별 원가를 세밀하게 관리합니다. 베트남은 간단한 예산 관리 수준이며 원가 분석이 상대적으로 덜 정교합니다. 한국은 실시간 원가 집계가 가능하나 베트남은 월 단위 집계가 일반적입니다. 한국은 원가 절감 목표(VE)와 연계되지만, 베트남은 초기 예산 준수에 집중합니다. 통역 시 'chi phí gốc'(원가)와 'chi phí xây dựng'(공사비)를 혼동하지 않아야 합니다.",
        "commonMistakes": [
            {
                "mistake": "'hệ thống ngân sách'으로만 번역",
                "correction": "Hệ thống quản lý chi phí (원가관리)",
                "explanation": "예산(ngân sách)은 계획, 원가(chi phí)는 실제 투입비용으로 구분됩니다."
            },
            {
                "mistake": "원가와 공사비를 같은 것으로 설명",
                "correction": "원가=chi phí gốc, 공사비=chi phí xây dựng (원가+이윤)",
                "explanation": "공사비는 원가에 이윤과 간접비가 포함된 금액입니다."
            },
            {
                "mistake": "'quản lý giá'로 번역",
                "correction": "quản lý chi phí (비용 관리)",
                "explanation": "'giá'는 가격, 'chi phí'는 비용으로 원가는 비용 개념입니다."
            }
        ],
        "examples": [
            {
                "ko": "원가관리시스템을 통해 이번 달 자재비가 예산을 10% 초과했음을 확인했습니다.",
                "vi": "Qua hệ thống quản lý chi phí xác nhận chi phí vật tư tháng này vượt ngân sách 10%.",
                "situation": "formal"
            },
            {
                "ko": "일일 원가 보고서를 작성해서 시스템에 입력해 주세요.",
                "vi": "Vui lòng lập báo cáo chi phí hàng ngày và nhập vào hệ thống.",
                "situation": "onsite"
            },
            {
                "ko": "원가관리시스템과 ERP를 연동하여 재무 관리를 자동화했습니다.",
                "vi": "Đã tự động hóa quản lý tài chính bằng cách kết nối hệ thống quản lý chi phí với ERP.",
                "situation": "formal"
            }
        ],
        "relatedTerms": ["예산관리", "수익성분석", "실행예산", "ERP"]
    },
    {
        "slug": "he-thong-quan-ly-an-toan",
        "korean": "안전관리시스템",
        "vietnamese": "Hệ thống quản lý an toàn",
        "hanja": "安全管理體系",
        "hanjaReading": "安(편안 안) + 全(온전 전) + 管(대롱 관) + 理(다스릴 리) + 體(몸 체) + 系(맬 계)",
        "pronunciation": "안전 관리 시스템",
        "meaningKo": "건설 현장의 안전사고 예방, 안전교육, 위험요소 관리 등을 통합적으로 수행하는 정보시스템입니다. 근로자 안전교육 이수 여부, TBM(Tool Box Meeting) 기록, 안전점검 결과, 아차사고 보고 등을 전산으로 관리하며, 스마트 안전장비(IoT 헬멧, 위치추적 등)와 연동됩니다. 통역 시 '안전관리'와 '보건관리'를 구분해야 하며, 한국은 중대재해처벌법으로 안전관리 의무가 강화되었음을 설명해야 합니다. 안전관리시스템은 단순 기록이 아닌 '예방적 관리'와 '실시간 모니터링'이 핵심입니다.",
        "meaningVi": "Hệ thống tích hợp phòng ngừa tai nạn lao động, đào tạo an toàn, quản lý yếu tố nguy hiểm tại công trường. Quản lý điện tử việc hoàn thành đào tạo an toàn, ghi chép TBM, kết quả kiểm tra an toàn, báo cáo sự cố suýt xảy ra, kết nối với thiết bị an toàn thông minh.",
        "context": "안전관리, 산업안전, IoT",
        "culturalNote": "한국은 중대재해처벌법으로 안전관리시스템 구축이 사실상 의무화되었으며, 50억 원 이상 공사는 안전관리비를 별도 계상합니다. 베트남도 안전 규정이 강화되고 있으나 시스템화는 초기 단계입니다. 한국은 IoT 헬멧, 스마트 안전조끼 등 스마트 안전장비가 보편화되었으나 베트남은 기본 안전장비 착용 단계입니다. 한국은 아차사고(near-miss) 보고 문화가 정착되었으나 베트남은 아직 사고 후 조치 중심입니다. 통역 시 'an toàn lao động'(산업안전)으로 표현해야 합니다.",
        "commonMistakes": [
            {
                "mistake": "'hệ thống bảo vệ'로 번역",
                "correction": "Hệ thống quản lý an toàn (안전관리)",
                "explanation": "'bảo vệ'는 경비/보안, 'an toàn'은 안전(safety)입니다."
            },
            {
                "mistake": "안전과 보건을 혼동",
                "correction": "안전=an toàn, 보건=sức khỏe lao động",
                "explanation": "안전은 사고 방지, 보건은 건강 관리로 구분됩니다."
            },
            {
                "mistake": "기록 시스템으로만 이해",
                "correction": "예방+모니터링+교육 통합 시스템",
                "explanation": "안전관리시스템은 기록뿐 아니라 예방과 실시간 관리가 핵심입니다."
            }
        ],
        "examples": [
            {
                "ko": "안전관리시스템에 오늘 TBM 내용을 등록했습니까?",
                "vi": "Đã đăng ký nội dung TBM hôm nay vào hệ thống quản lý an toàn chưa?",
                "situation": "onsite"
            },
            {
                "ko": "IoT 헬멧 데이터가 안전관리시스템으로 실시간 전송됩니다.",
                "vi": "Dữ liệu mũ IoT được truyền thời gian thực vào hệ thống quản lý an toàn.",
                "situation": "formal"
            },
            {
                "ko": "아차사고 보고는 안전관리시스템 모바일 앱으로 즉시 작성해 주세요.",
                "vi": "Vui lòng lập báo cáo sự cố suýt xảy ra ngay qua ứng dụng di động hệ thống quản lý an toàn.",
                "situation": "onsite"
            }
        ],
        "relatedTerms": ["중대재해처벌법", "TBM", "아차사고", "스마트안전장비"]
    },
    {
        "slug": "he-thong-quan-ly-khiem-khuyet",
        "korean": "하자관리시스템",
        "vietnamese": "Hệ thống quản lý khiếm khuyết",
        "hanja": "瑕疵管理體系",
        "hanjaReading": "瑕(옥의 티 하) + 疵(흠 자) + 管(대롱 관) + 理(다스릴 리) + 體(몸 체) + 系(맬 계)",
        "pronunciation": "하자 관리 시스템",
        "meaningKo": "건설공사 완료 후 발생하는 하자(결함)를 접수, 처리, 추적 관리하는 정보시스템입니다. 입주자가 하자를 신고하면 시스템에 등록되고, 하자 유형(누수, 균열, 마감 불량 등)을 분류하여 담당자에게 배정하며, 처리 과정과 결과를 기록합니다. 통역 시 '하자'(khiếm khuyết)와 '하자보수'(sửa chữa khiếm khuyết)를 구분해야 하며, 한국의 하자담보책임기간(1~10년)과 베트남의 보증기간 차이를 이해해야 합니다. 하자관리시스템은 하자 통계 분석을 통해 설계·시공 품질 개선에도 활용됩니다.",
        "meaningVi": "Hệ thống tiếp nhận, xử lý và theo dõi khiếm khuyết (lỗi) phát sinh sau khi hoàn thành công trình. Khi cư dân báo lỗi, hệ thống ghi nhận, phân loại (thấm nước, nứt, hoàn thiện kém...), phân công người phụ trách và ghi nhận quá trình xử lý.",
        "context": "하자보수, 준공 후 관리, AS",
        "culturalNote": "한국은 공동주택 하자담보책임기간이 법으로 정해져 있으며(구조부 10년, 방수 5년 등) 입주자대표회의를 통해 체계적으로 하자를 관리합니다. 베트nam은 bảo hành(보증) 개념으로 보통 1~2년이며 하자 관리가 덜 체계적입니다. 한국은 하자관리 전용 시스템(앱)이 보편화되었으나 베트남은 전화나 문자로 하자를 신고합니다. 한국은 하자 통계를 분석해 다음 프로젝트 품질 개선에 활용하지만, 베트남은 개별 처리 위주입니다. 통역 시 'lỗi kỹ thuật'(기술적 하자)와 구분해야 합니다.",
        "commonMistakes": [
            {
                "mistake": "'hệ thống bảo hành'으로만 표현",
                "correction": "Hệ thống quản lý khiếm khuyết (하자관리)",
                "explanation": "보증(bảo hành)보다 포괄적인 하자 관리(quản lý khiếm khuyết) 개념입니다."
            },
            {
                "mistake": "하자와 불량품을 혼동",
                "correction": "하자=시공 결함, 불량품=재료 불량",
                "explanation": "하자는 시공 후 발생한 결함, 불량품은 자재 자체의 문제입니다."
            },
            {
                "mistake": "'sửa chữa'로만 번역",
                "correction": "quản lý (관리) + sửa chữa (보수)",
                "explanation": "하자관리는 단순 수리가 아닌 접수-처리-추적 전 과정입니다."
            }
        ],
        "examples": [
            {
                "ko": "하자관리시스템에서 현재 미처리 하자가 몇 건인지 확인해 주세요.",
                "vi": "Vui lòng kiểm tra có bao nhiêu khiếm khuyết chưa xử lý trong hệ thống quản lý khiếm khuyết.",
                "situation": "onsite"
            },
            {
                "ko": "이 아파트는 하자관리 앱으로 입주자가 직접 하자를 신고할 수 있습니다.",
                "vi": "Chung cư này cư dân có thể tự báo khiếm khuyết qua ứng dụng quản lý khiếm khuyết.",
                "situation": "formal"
            },
            {
                "ko": "하자 유형별 통계를 보니 누수 하자가 가장 많네요.",
                "vi": "Theo thống kê phân loại khiếm khuyết, khiếm khuyết thấm nước nhiều nhất.",
                "situation": "formal"
            }
        ],
        "relatedTerms": ["하자담보책임", "하자보수", "AS", "입주자대표회의"]
    },
    {
        "slug": "camera-giam-sat-cong-truong",
        "korean": "현장CCTV",
        "vietnamese": "Camera giám sát công trường",
        "hanja": "現場監視體系",
        "hanjaReading": "現(나타날 현) + 場(마당 장) + 監(볼 감) + 視(볼 시) + 體(몸 체) + 系(맬 계)",
        "pronunciation": "현장 씨씨티비",
        "meaningKo": "건설 현장에 설치된 CCTV(폐쇄회로 텔레비전)로 공정 진행, 안전 관리, 보안을 실시간으로 모니터링하는 시스템입니다. 최근에는 AI 기반으로 안전모 미착용, 위험 구역 진입 등을 자동 감지하며, 타임랩스 영상으로 공정 기록을 남깁니다. 통역 시 'CCTV'를 베트남어로는 'camera giám sát'로 표현하며, 한국에서는 '현장 CCTV'가 일반적이고 베트남에서는 'camera công trường'이 자연스럽습니다. 현장CCTV는 안전사고 분석, 분쟁 발생 시 증거자료, 원격 현장관리 등 다목적으로 활용됩니다.",
        "meaningVi": "Hệ thống camera giám sát (CCTV) lắp đặt tại công trường để theo dõi tiến độ, quản lý an toàn và bảo mật theo thời gian thực. Gần đây có AI tự động phát hiện không đội mũ an toàn, xâm nhập khu vực nguy hiểm, ghi hình time-lapse để lưu tiến độ.",
        "context": "안전관리, 공정관리, 보안",
        "culturalNote": "한국 건설 현장은 필수적으로 CCTV를 설치하며 중대재해처벌법 이후 AI CCTV 도입이 확대되고 있습니다. 베트남도 대형 현장은 CCTV를 설치하지만 AI 기능은 아직 드뭅니다. 한국은 CCTV 영상을 본사에서 실시간으로 모니터링하지만, 베트남은 현장 관리소에서만 확인하는 경우가 많습니다. 한국은 타임랩스 영상을 마케팅에도 활용하나 베트남은 보안 목적이 주입니다. 통역 시 'camera an ninh'(보안 카메라)와 'camera giám sát'(감시 카메라)를 혼용할 수 있습니다.",
        "commonMistakes": [
            {
                "mistake": "'camera an ninh'로만 표현",
                "correction": "camera giám sát công trường (현장 감시 카메라)",
                "explanation": "'an ninh'는 보안 목적, 'giám sát'는 감시/모니터링으로 더 포괄적입니다."
            },
            {
                "mistake": "CCTV를 베트남어로 그대로 사용",
                "correction": "camera giám sát (감시 카메라)",
                "explanation": "베트남에서는 'CCTV'보다 'camera giám sát'가 일반적입니다."
            },
            {
                "mistake": "보안 목적으로만 이해",
                "correction": "공정+안전+보안 다목적 활용",
                "explanation": "현장CCTV는 보안뿐 아니라 공정 기록, 안전 관리에도 사용됩니다."
            }
        ],
        "examples": [
            {
                "ko": "현장CCTV 영상을 확인한 결과 안전모 미착용자가 발견되었습니다.",
                "vi": "Kiểm tra hình ảnh camera giám sát công trường phát hiện người không đội mũ an toàn.",
                "situation": "formal"
            },
            {
                "ko": "AI CCTV가 위험 구역 진입을 감지하여 경보가 울렸습니다.",
                "vi": "Camera AI phát hiện xâm nhập khu vực nguy hiểm và kêu cảnh báo.",
                "situation": "onsite"
            },
            {
                "ko": "타임랩스 영상으로 지난 6개월 공정을 30초로 압축했습니다.",
                "vi": "Đã nén tiến độ 6 tháng qua thành 30 giây bằng video time-lapse.",
                "situation": "formal"
            }
        ],
        "relatedTerms": ["AI안전관리", "타임랩스", "원격모니터링", "스마트안전"]
    },
    {
        "slug": "he-thong-kiem-soat-ra-vao",
        "korean": "출입관리시스템",
        "vietnamese": "Hệ thống kiểm soát ra vào",
        "hanja": "出入管理體系",
        "hanjaReading": "出(날 출) + 入(들 입) + 管(대롱 관) + 理(다스릴 리) + 體(몸 체) + 系(맬 계)",
        "pronunciation": "출입 관리 시스템",
        "meaningKo": "건설 현장 출입구에 설치되어 근로자, 차량, 방문자의 출입을 통제하고 기록하는 시스템입니다. 출입카드, QR코드, 안면인식, 차량번호판 인식 등 다양한 방식으로 출입을 관리하며, 안전교육 이수 여부, 출입 권한, 근태 관리와 연동됩니다. 통역 시 '출입통제'(kiểm soát ra vào)와 '보안검색'(kiểm tra an ninh)을 구분해야 하며, 출입관리는 보안뿐 아니라 안전과 근태 관리가 핵심임을 설명해야 합니다. 최근에는 비대면 체온 측정, 마스크 착용 확인 등 방역 기능도 통합되고 있습니다.",
        "meaningVi": "Hệ thống lắp đặt tại cổng công trường để kiểm soát và ghi nhận ra vào của công nhân, xe cộ, khách. Quản lý bằng thẻ ra vào, mã QR, nhận diện khuôn mặt, biển số xe, kết nối với hoàn thành đào tạo an toàn, quyền ra vào, chấm công.",
        "context": "출입통제, 근태관리, 안전",
        "culturalNote": "한국 건설 현장은 출입카드와 QR코드 출입이 보편화되었으며, 안전교육 미이수자는 출입이 차단됩니다. 베트남은 수기 출입 대장을 여전히 많이 사용하며 전산화는 대형 현장 위주입니다. 한국은 출입관리와 근태관리가 통합되어 임금 정산에 활용되나, 베트남은 별도로 관리하는 경우가 많습니다. 한국은 안면인식 도입이 확대되고 있으나 베트남은 개인정보 우려로 제한적입니다. 통역 시 'kiểm soát'(통제)와 'quản lý'(관리)를 구분해야 합니다.",
        "commonMistakes": [
            {
                "mistake": "'hệ thống an ninh'으로만 표현",
                "correction": "Hệ thống kiểm soát ra vào (출입관리)",
                "explanation": "보안(an ninh)보다 출입 관리(kiểm soát ra vào)가 더 정확합니다."
            },
            {
                "mistake": "출입통제와 보안검색을 혼동",
                "correction": "출입통제=ra vào, 보안검색=kiểm tra an ninh",
                "explanation": "출입통제는 권한 확인, 보안검색은 소지품 검사입니다."
            },
            {
                "mistake": "보안 목적으로만 이해",
                "correction": "보안+안전+근태 통합 관리",
                "explanation": "출입관리시스템은 보안뿐 아니라 안전교육 확인, 근태 관리 기능도 포함합니다."
            }
        ],
        "examples": [
            {
                "ko": "출입관리시스템에서 안전교육 미이수자는 자동으로 출입이 거부됩니다.",
                "vi": "Hệ thống kiểm soát ra vào tự động từ chối người chưa hoàn thành đào tạo an toàn.",
                "situation": "formal"
            },
            {
                "ko": "QR코드를 스캔하면 출입이 기록되고 근태에 반영됩니다.",
                "vi": "Quét mã QR sẽ ghi nhận ra vào và phản ánh vào chấm công.",
                "situation": "onsite"
            },
            {
                "ko": "안면인식 출입관리시스템으로 카드 분실 문제가 해결되었습니다.",
                "vi": "Hệ thống kiểm soát ra vào nhận diện khuôn mặt đã giải quyết vấn đề mất thẻ.",
                "situation": "formal"
            }
        ],
        "relatedTerms": ["출입카드", "QR코드", "안면인식", "근태관리"]
    },
    {
        "slug": "he-thong-erp-xay-dung",
        "korean": "건설ERP",
        "vietnamese": "Hệ thống ERP xây dựng",
        "hanja": "建設統合管理體系",
        "hanjaReading": "建(세울 건) + 設(베풀 설) + 統(거느릴 통) + 合(합할 합) + 管(대롱 관) + 理(다스릴 리) + 體(몸 체) + 系(맬 계)",
        "pronunciation": "건설 이알피",
        "meaningKo": "건설업에 특화된 전사적 자원관리(Enterprise Resource Planning) 시스템으로, 회계, 인사, 구매, 재고, 원가, 공정 등 건설사의 모든 업무를 통합 관리합니다. 프로젝트별 수익성 분석, 자재 발주부터 대금 지급까지 전 과정을 추적하며, 본사와 현장 간 실시간 정보 공유를 지원합니다. 통역 시 'ERP'를 베트남어로 풀어서 'hệ thống quản lý tài nguyên doanh nghiệp'로 설명할 수 있으며, 일반 ERP와 건설ERP의 차이(프로젝트 중심, 원가 관리 등)를 강조해야 합니다. 건설ERP는 단순 회계 시스템이 아닌 전사 통합 관리 플랫폼입니다.",
        "meaningVi": "Hệ thống quản lý tài nguyên doanh nghiệp (ERP) chuyên biệt cho ngành xây dựng, tích hợp quản lý kế toán, nhân sự, mua hàng, tồn kho, chi phí, tiến độ. Phân tích lợi nhuận từng dự án, theo dõi từ đặt hàng vật tư đến thanh toán, hỗ trợ chia sẻ thông tin thời gian thực giữa trụ sở và công trường.",
        "context": "통합관리, 전산화, 경영관리",
        "culturalNote": "한국 중견 이상 건설사는 대부분 자체 또는 상용 건설ERP(예: 더존, 영림원)를 운영하며 전사 업무가 ERP 중심으로 처리됩니다. 베트남은 대형사 위주로 ERP를 도입하며 SAP, Oracle 등 글로벌 ERP를 사용하는 경우가 많습니다. 한국은 ERP와 PMIS, 원가시스템이 통합되어 있으나 베트남은 별도 운영이 일반적입니다. 한국은 모바일 ERP 활용이 보편화되었으나 베트남은 PC 기반이 주류입니다. 통역 시 'hệ thống tổng hợp'(통합 시스템)으로 부연 설명하면 좋습니다.",
        "commonMistakes": [
            {
                "mistake": "'phần mềm kế toán'으로만 번역",
                "correction": "Hệ thống ERP (통합 자원관리)",
                "explanation": "ERP는 회계뿐 아니라 인사, 구매, 재고 등 전사 업무를 통합합니다."
            },
            {
                "mistake": "일반 ERP와 건설ERP를 구분 없이 설명",
                "correction": "건설ERP는 프로젝트 중심, 원가 관리 특화",
                "explanation": "건설ERP는 프로젝트 단위 관리와 원가 추적이 핵심입니다."
            },
            {
                "mistake": "시스템과 프로그램을 혼동",
                "correction": "ERP는 통합 시스템(hệ thống), 프로그램은 모듈",
                "explanation": "ERP는 여러 모듈이 통합된 시스템입니다."
            }
        ],
        "examples": [
            {
                "ko": "당사는 건설ERP를 통해 50개 현장의 원가를 실시간으로 집계합니다.",
                "vi": "Công ty chúng tôi tổng hợp chi phí 50 công trường theo thời gian thực qua hệ thống ERP xây dựng.",
                "situation": "formal"
            },
            {
                "ko": "자재 발주는 ERP 시스템에서 승인 후 진행됩니다.",
                "vi": "Đặt hàng vật tư thực hiện sau khi phê duyệt trong hệ thống ERP.",
                "situation": "onsite"
            },
            {
                "ko": "건설ERP와 은행을 연동하여 대금 지급을 자동화했습니다.",
                "vi": "Đã tự động hóa thanh toán bằng cách kết nối hệ thống ERP xây dựng với ngân hàng.",
                "situation": "formal"
            }
        ],
        "relatedTerms": ["전사적자원관리", "통합관리", "원가관리", "프로젝트관리"]
    }
]

# 대상 파일 경로
file_path = os.path.join(
    os.path.dirname(__file__),
    "..",
    "data",
    "terms",
    "construction.json"
)

def main():
    # 기존 파일 읽기
    with open(file_path, 'r', encoding='utf-8') as f:
        existing_data = json.load(f)

    print(f"기존 용어 수: {len(existing_data)}")

    # 중복 확인 (slug 기준)
    existing_slugs = {term['slug'] for term in existing_data}
    new_terms = [term for term in data if term['slug'] not in existing_slugs]
    duplicates = [term['slug'] for term in data if term['slug'] in existing_slugs]

    if duplicates:
        print(f"⚠️  중복된 slug (추가 안 됨): {', '.join(duplicates)}")

    if not new_terms:
        print("추가할 신규 용어가 없습니다.")
        return

    # 병합
    merged_data = existing_data + new_terms

    # 저장
    with open(file_path, 'w', encoding='utf-8') as f:
        json.dump(merged_data, f, ensure_ascii=False, indent=2)

    print(f"✅ {len(new_terms)}개 용어 추가 완료")
    print(f"총 용어 수: {len(merged_data)}")
    print("\n추가된 용어:")
    for term in new_terms:
        print(f"  - {term['korean']} ({term['slug']})")

if __name__ == "__main__":
    main()
