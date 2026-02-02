#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
건축물 유형 테마 용어 추가 스크립트
테마: 아파트, 주상복합, 오피스텔, 다세대주택, 상가, 공장, 물류센터, 데이터센터, 병원, 학교
"""

import json
import os

# 추가할 용어 데이터 (Tier S 기준)
data = [
    {
        "slug": "chung-cu",
        "korean": "아파트",
        "vietnamese": "Chung cư",
        "hanja": None,
        "hanjaReading": None,
        "pronunciation": "충 꾸",
        "meaningKo": "공동주택의 한 형태로, 5층 이상의 주거용 건축물을 의미합니다. 한국에서는 단지형 아파트가 주거 문화의 대표이며, 각 세대가 독립된 주거 공간을 가집니다. 통역 시 베트남의 'chung cư'는 한국의 아파트와 유사하나, 한국은 단지 중심의 커뮤니티 시설(놀이터, 헬스장, 상가)이 발달한 반면 베트남은 개별 동 중심 구조가 많습니다. 베트남 현장에서는 '공동주택(nhà ở chung)'이라는 표현도 쓰이나 'chung cư'가 일반적이며, 고급 아파트는 'căn hộ cao cấp'으로 구분합니다. 통역 시 층수, 세대수, 단지 규모를 명확히 해야 오해를 방지할 수 있습니다.",
        "meaningVi": "Loại hình nhà ở chung từ 5 tầng trở lên, mỗi hộ có không gian sinh hoạt riêng biệt. Ở Hàn Quốc, chung cư theo khu đô thị với đầy đủ tiện ích cộng đồng như sân chơi, phòng gym, khu thương mại.",
        "context": "공동주택, 주거 건축, 부동산, 아파트 단지, 주택 건설",
        "culturalNote": "한국은 아파트가 전체 주거의 60% 이상을 차지하며, '단지형 아파트(khu chung cư)'가 주류입니다. 베트남은 도시 중심으로 chung cư가 증가하고 있으나, 아직 단독주택 선호도가 높습니다. 통역 시 한국의 '아파트 단지(khu chung cư)' 개념과 커뮤니티 시설(tiện ích cộng đồng)을 강조하면 차별성을 전달할 수 있습니다. 또한 한국은 '평형(diện tích theo bình phương mét)'이라는 고유 단위를 사용하므로, 베트남의 'm²' 단위로 변환 설명이 필요합니다.",
        "commonMistakes": [
            {
                "mistake": "nhà chung",
                "correction": "chung cư / nhà ở chung",
                "explanation": "'공동 집'은 모호한 표현, 아파트는 'chung cư'로 명확히 해야"
            },
            {
                "mistake": "아파트 빌딩",
                "correction": "아파트 / 아파트 동",
                "explanation": "'빌딩'은 업무용 뉘앙스, 주거용은 '아파트' 또는 '동'으로 표현"
            },
            {
                "mistake": "tòa nhà",
                "correction": "chung cư / căn hộ",
                "explanation": "'건물'은 일반적 표현, 주거용은 'chung cư'로 구체화 필요"
            }
        ],
        "examples": [
            {
                "ko": "이번 프로젝트는 2,000세대 규모의 아파트 단지입니다.",
                "vi": "Dự án lần này là khu chung cư quy mô 2.000 căn hộ.",
                "situation": "formal"
            },
            {
                "ko": "아파트 지하에 주차장 3층 규모로 설계했어요.",
                "vi": "Thiết kế bãi đỗ xe 3 tầng hầm ở chung cư.",
                "situation": "onsite"
            },
            {
                "ko": "이 아파트는 30평형이에요.",
                "vi": "Căn hộ này khoảng 99m².",
                "situation": "informal"
            }
        ],
        "relatedTerms": ["공동주택", "주상복합", "세대", "단지", "평형"]
    },
    {
        "slug": "toa-nha-van-phong-ket-hop-can-ho",
        "korean": "주상복합",
        "vietnamese": "Tòa nhà văn phòng kết hợp căn hộ",
        "hanja": "住商複合",
        "hanjaReading": "住(살 주) + 商(장사 상) + 複(겹 복) + 合(합할 합)",
        "pronunciation": "토아 냐 반 퐁 껫 합 껀 호",
        "meaningKo": "주거(住)와 상업(商)이 복합(複合)된 건축물로, 하부는 상가·오피스, 상부는 주거 공간으로 구성됩니다. 도심 입지, 높은 층수, 프리미엄 이미지가 특징이며, 한국에서는 부동산 고급 상품으로 인식됩니다. 통역 시 베트nam에서는 'hỗn hợp thương mại-nhà ở' 또는 'mixed-use'라는 영어 표현도 통용되나, 전문 회의에서는 'tòa nhà kết hợp căn hộ và thương mại'로 구체화하세요. 한국의 주상복합은 대부분 30층 이상 초고층이며, 베트남은 아직 중고층이 주류입니다.",
        "meaningVi": "Công trình kết hợp chức năng sinh hoạt (căn hộ) và thương mại (văn phòng, cửa hàng), tầng dưới là khu thương mại, tầng trên là khu dân cư. Thường nằm tại trung tâm thành phố và có tầng cao.",
        "context": "도심 개발, 초고층 건축, 복합 용도, 프리미엄 주거",
        "culturalNote": "한국은 주상복합이 도심 랜드마크로 자리 잡았으며, 고급 주거 브랜드가 집중되어 있습니다. 베트남은 하노이, 호치민 중심으로 증가 추세이나 아직 '아파트 + 상가' 수준이 많습니다. 통역 시 한국의 '스카이라운지(sky lounge)', '인피니티풀(infinity pool)' 같은 프리미엄 시설을 설명하면 베트남 고급 시장 고객에게 어필할 수 있습니다. 베트남은 'mixed-use'라는 영어 표현이 통용되나, 'tòa nhà phức hợp'이라는 표현도 쓰입니다.",
        "commonMistakes": [
            {
                "mistake": "주거 상업 건물",
                "correction": "주상복합 / 주상복합 건물",
                "explanation": "설명이 아닌 고유 용어로 표현 필요"
            },
            {
                "mistake": "nhà ở và thương mại",
                "correction": "tòa nhà phức hợp / kết hợp căn hộ và thương mại",
                "explanation": "단순 나열이 아닌 복합 용도 건축물임을 명시 필요"
            },
            {
                "mistake": "복합 빌딩",
                "correction": "주상복합 / 주거상업복합",
                "explanation": "'빌딩'은 일반적, 주상복합은 특정 유형 지칭"
            }
        ],
        "examples": [
            {
                "ko": "이 주상복합은 지하 5층부터 지상 50층 규모입니다.",
                "vi": "Tòa nhà phức hợp này quy mô từ tầng hầm 5 đến tầng 50.",
                "situation": "formal"
            },
            {
                "ko": "1층부터 10층까지는 상가와 오피스, 위층은 주거예요.",
                "vi": "Từ tầng 1 đến 10 là thương mại và văn phòng, trên là khu căn hộ.",
                "situation": "onsite"
            },
            {
                "ko": "주상복합은 교통 좋은 곳에 지어요.",
                "vi": "Tòa phức hợp được xây ở nơi giao thông thuận lợi.",
                "situation": "informal"
            }
        ],
        "relatedTerms": ["초고층", "복합 용도", "도심 입지", "프리미엄", "아파트"]
    },
    {
        "slug": "can-ho-officetel",
        "korean": "오피스텔",
        "vietnamese": "Căn hộ officetel",
        "hanja": None,
        "hanjaReading": None,
        "pronunciation": "껀 호 오피텔",
        "meaningKo": "Office(사무실) + Hotel(숙박)의 합성어로, 업무와 주거가 가능한 소형 건축물입니다. 한국에서는 1인 가구, 신혼부부, 사무실 겸용 주거로 인기가 높으며, 전용면적 60㎡ 이하가 대부분입니다. 통역 시 베트남에는 정확히 대응하는 건축 유형이 없어 'căn hộ văn phòng(사무실 아파트)' 또는 'officetel'을 음차하여 사용합니다. 베트남 현장에서는 'căn hộ dịch vụ(서비스 아파트)'와 혼동되기 쉬우므로, '주거 가능한 사무 공간'임을 명확히 설명하세요.",
        "meaningVi": "Loại hình kết hợp văn phòng và nơi ở, diện tích nhỏ (thường dưới 60m²), phù hợp cho người độc thân, cặp đôi mới cưới hoặc văn phòng kiêm nơi ở. Không có khái niệm tương tự chính xác ở Việt Nam.",
        "context": "소형 주거, 1인 가구, 사무실 겸용, 도심 입지",
        "culturalNote": "한국은 오피스텔이 법적으로 '업무시설'로 분류되어 주택 수에 포함되지 않으므로, 세금 및 대출 규제에서 차이가 있습니다. 베트남은 유사 개념이 없어 '서비스 아파트(căn hộ dịch vụ)'로 오해되기 쉬우나, 서비스 아파트는 호텔식 서비스가 제공되는 반면 오피스텔은 독립 주거입니다. 통역 시 '주거 가능한 사무 공간(không gian văn phòng có thể ở)'으로 설명하고, 한국의 법적 분류(phân loại pháp lý)를 언급하면 이해도를 높일 수 있습니다.",
        "commonMistakes": [
            {
                "mistake": "사무실 아파트",
                "correction": "오피스텔",
                "explanation": "직역이 아닌 고유 명사로 표현 필요"
            },
            {
                "mistake": "căn hộ dịch vụ",
                "correction": "officetel / căn hộ văn phòng",
                "explanation": "서비스 아파트는 호텔식, 오피스텔은 독립 주거"
            },
            {
                "mistake": "원룸",
                "correction": "오피스텔 / 소형 오피스텔",
                "explanation": "원룸은 주거만, 오피스텔은 업무 겸용"
            }
        ],
        "examples": [
            {
                "ko": "이 오피스텔은 전용면적 30㎡로 1인 가구에 적합합니다.",
                "vi": "Officetel này diện tích sử dụng 30m² phù hợp cho hộ gia đình 1 người.",
                "situation": "formal"
            },
            {
                "ko": "오피스텔은 주거용으로도 사무실로도 쓸 수 있어요.",
                "vi": "Officetel có thể dùng làm nơi ở hoặc văn phòng.",
                "situation": "onsite"
            },
            {
                "ko": "역 근처 오피스텔이 투자로 인기예요.",
                "vi": "Officetel gần ga tàu điện ngầm phổ biến cho đầu tư.",
                "situation": "informal"
            }
        ],
        "relatedTerms": ["원룸", "1인 가구", "소형 주거", "업무시설", "도심"]
    },
    {
        "slug": "nha-nhieu-ho-dan-cu",
        "korean": "다세대주택",
        "vietnamese": "Nhà nhiều hộ dân cư",
        "hanja": "多世帶住宅",
        "hanjaReading": "多(많을 다) + 世(인간 세) + 帶(띠 대) + 住(살 주) + 宅(집 택)",
        "pronunciation": "냐 니에우 호 전 꾸",
        "meaningKo": "연면적 660㎡ 이하, 4층 이하의 소규모 공동주택으로, 여러 세대가 독립된 주거 공간을 가지는 건축물입니다. 한국에서는 다가구주택과 구분되며, 각 세대가 개별 등기가 가능합니다. 통역 시 베트남의 'nhà tập thể(집단 주택)'와 유사하나, 한국의 다세대는 소유권 독립이 핵심입니다. 베트남 현장에서는 'nhà chung nhỏ' 또는 'nhà ở chia lô(필지 분할 주택)'로 설명하면 이해가 쉽습니다. 통역 시 세대수, 층수, 면적 기준을 명확히 해야 다가구주택과의 혼동을 방지할 수 있습니다.",
        "meaningVi": "Nhà ở chung quy mô nhỏ, diện tích dưới 660m², tối đa 4 tầng, nhiều hộ có quyền sở hữu riêng biệt. Tương tự 'nhà tập thể' ở Việt Nam nhưng mỗi hộ có giấy chứng nhận riêng.",
        "context": "소규모 공동주택, 주거 건축, 부동산, 저층 주택",
        "culturalNote": "한국은 다세대주택이 법적으로 '공동주택'으로 분류되어 개별 등기가 가능하며, 재건축·재개발 대상이 됩니다. 베트남은 유사 개념이 명확하지 않으나, 'nhà tập thể cũ(구 집단 주택)'가 가장 가깝습니다. 통역 시 한국의 '개별 등기(đăng ký riêng)' 제도를 설명하고, 베트남의 'sổ hồng(red book, 부동산 증서)' 개념과 연결하면 이해도를 높일 수 있습니다. 한국은 다세대와 다가구의 법적 구분이 엄격하므로, 베트남 측에 명확히 전달해야 혼란을 방지할 수 있습니다.",
        "commonMistakes": [
            {
                "mistake": "다가구주택",
                "correction": "다세대주택 (또는 차이 설명)",
                "explanation": "다가구는 단일 소유, 다세대는 개별 소유"
            },
            {
                "mistake": "nhà chung",
                "correction": "nhà nhiều hộ dân cư / nhà ở chung nhỏ",
                "explanation": "'공동 집'은 모호, 다세대 특성 명시 필요"
            },
            {
                "mistake": "빌라",
                "correction": "다세대주택 (빌라는 통칭)",
                "explanation": "빌라는 비공식 표현, 다세대가 법적 용어"
            }
        ],
        "examples": [
            {
                "ko": "이 다세대주택은 4층에 8세대가 거주합니다.",
                "vi": "Nhà nhiều hộ này 4 tầng có 8 hộ sinh sống.",
                "situation": "formal"
            },
            {
                "ko": "다세대는 각 세대마다 등기가 따로 나와요.",
                "vi": "Nhà nhiều hộ mỗi căn có giấy chứng nhận riêng.",
                "situation": "onsite"
            },
            {
                "ko": "역세권 다세대주택 재개발 계획이에요.",
                "vi": "Kế hoạch tái phát triển nhà nhiều hộ gần ga tàu.",
                "situation": "informal"
            }
        ],
        "relatedTerms": ["다가구주택", "공동주택", "재개발", "등기", "저층"]
    },
    {
        "slug": "khu-thuong-mai",
        "korean": "상가",
        "vietnamese": "Khu thương mại",
        "hanja": "商街",
        "hanjaReading": "商(장사 상) + 街(거리 가)",
        "pronunciation": "쿠 트엉 마이",
        "meaningKo": "상업용 건축물로, 소매점, 음식점, 서비스업 등이 입주하는 공간입니다. 한국에서는 단독 상가, 근린상가, 복합쇼핑몰 등으로 구분되며, 1층 상가는 유동인구가 많아 프리미엄이 붙습니다. 통역 시 베트남의 'cửa hàng(가게)'는 개별 점포, 'khu thương mại'는 상가 건물 전체를 의미하므로 구분하세요. 베트남 현장에서는 'nhà phố thương mại(상업용 타운하우스)' 또는 'trung tâm thương mại nhỏ(소형 쇼핑센터)'로 설명하면 이해가 쉽습니다. 통역 시 '근린상가(khu thương mại lân cận)'와 '대형 쇼핑몰(trung tâm thương mại lớn)'을 구분해야 혼동을 방지할 수 있습니다.",
        "meaningVi": "Công trình thương mại cho thuê hoặc bán các cửa hàng bán lẻ, nhà hàng, dịch vụ. Phân loại thành cửa hàng độc lập, khu thương mại lân cận, trung tâm mua sắm. Tầng 1 có vị trí đắc địa do lưu lượng người qua lại cao.",
        "context": "상업 건축, 소매업, 부동산 임대, 유동인구",
        "culturalNote": "한국은 상가가 부동산 투자 대상으로 인기가 높으며, '역세권 1층 상가'는 프리미엄이 매우 높습니다. 베트남은 'nhà phố thương mại(상업용 타운하우스)' 형태가 많고, 대형 쇼핑몰은 'trung tâm thương mại'로 구분됩니다. 통역 시 한국의 '근린상가(khu thương mại gần khu dân cư)' 개념을 설명하면 베트남의 소규모 상업 지역과 연결할 수 있습니다. 베트남은 'shophouse'라는 영어 표현도 통용되나, 'khu thương mại' 또는 'nhà phố thương mại'가 더 정확합니다.",
        "commonMistakes": [
            {
                "mistake": "가게",
                "correction": "상가 / 상가 건물",
                "explanation": "가게는 개별 점포, 상가는 건물 전체"
            },
            {
                "mistake": "cửa hàng",
                "correction": "khu thương mại / nhà phố thương mại",
                "explanation": "'가게'는 개별, 상가는 건축물 지칭 필요"
            },
            {
                "mistake": "쇼핑몰",
                "correction": "상가 / 근린상가 (쇼핑몰과 구분)",
                "explanation": "쇼핑몰은 대형 복합시설, 상가는 소규모"
            }
        ],
        "examples": [
            {
                "ko": "이 상가 건물은 지하 1층부터 지상 5층 규모입니다.",
                "vi": "Tòa nhà thương mại này quy mô từ tầng hầm 1 đến tầng 5.",
                "situation": "formal"
            },
            {
                "ko": "1층 상가는 임대료가 제일 비싸요.",
                "vi": "Cửa hàng tầng 1 tiền thuê đắt nhất.",
                "situation": "onsite"
            },
            {
                "ko": "아파트 단지 내 근린상가예요.",
                "vi": "Khu thương mái lân cận trong khu chung cư.",
                "situation": "informal"
            }
        ],
        "relatedTerms": ["근린상가", "쇼핑몰", "유동인구", "임대", "상업시설"]
    },
    {
        "slug": "nha-may",
        "korean": "공장",
        "vietnamese": "Nhà máy",
        "hanja": "工場",
        "hanjaReading": "工(장인 공) + 場(마당 장)",
        "pronunciation": "냐 마이",
        "meaningKo": "제조업을 위한 산업 건축물로, 생산 설비, 창고, 사무동 등으로 구성됩니다. 한국에서는 일반 공장, 아파트형 공장, 지식산업센터 등으로 구분되며, 산업단지 내 입지가 일반적입니다. 통역 시 베트남의 'nhà máy'는 한국의 공장과 동일하나, 한국은 '스마트 공장(smart factory)' 개념이 빠르게 확산 중이므로 자동화 수준을 설명하면 좋습니다. 베트남 현장에서는 'xưởng(작업장)'과 'nhà máy(공장)'를 규모로 구분하므로, 통역 시 면적과 생산 규모를 명확히 하세요.",
        "meaningVi": "Công trình sản xuất công nghiệp gồm khu vực sản xuất, kho và văn phòng. Phân loại thành nhà máy thông thường, nhà máy kiểu căn hộ, trung tâm công nghiệp tri thức. Thường nằm trong khu công nghiệp.",
        "context": "제조업, 산업 건축, 생산 시설, 산업단지",
        "culturalNote": "한국은 스마트 공장 정책으로 자동화·디지털화가 빠르게 진행 중이며, 정부 보조금도 지원됩니다. 베트남은 외국인 투자 중심의 대규모 공장이 많고, 한국 기업도 다수 진출해 있습니다. 통역 시 한국의 '지식산업센터(trung tâm công nghiệp tri thức)' 개념을 설명하면 베트남의 'tòa nhà văn phòng kiêm xưởng'과 연결할 수 있습니다. 베트남은 'nhà máy'와 'xưởng'을 규모와 정식 허가 여부로 구분하므로, 통역 시 명확히 해야 합니다.",
        "commonMistakes": [
            {
                "mistake": "작업장",
                "correction": "공장 / 제조 시설",
                "explanation": "작업장은 소규모, 공장은 산업 시설"
            },
            {
                "mistake": "xưởng",
                "correction": "nhà máy / cơ sở sản xuất",
                "explanation": "'xưởng'은 소규모, 공장은 'nhà máy'로 표현"
            },
            {
                "mistake": "팩토리",
                "correction": "공장 / 제조 공장",
                "explanation": "외래어보다 한국어 표준 용어 사용"
            }
        ],
        "examples": [
            {
                "ko": "이 공장은 연면적 5,000㎡에 자동화 생산 라인을 갖췄습니다.",
                "vi": "Nhà máy này diện tích 5.000m² với dây chuyền sản xuất tự động hóa.",
                "situation": "formal"
            },
            {
                "ko": "공장 건물은 내진 설계로 지어야 해요.",
                "vi": "Nhà máy phải xây dựng theo thiết kế chống động đất.",
                "situation": "onsite"
            },
            {
                "ko": "산업단지 내 공장 부지 분양받았어요.",
                "vi": "Đã mua đất xây nhà máy trong khu công nghiệp.",
                "situation": "informal"
            }
        ],
        "relatedTerms": ["산업단지", "제조업", "스마트 공장", "자동화", "생산시설"]
    },
    {
        "slug": "trung-tam-logistics",
        "korean": "물류센터",
        "vietnamese": "Trung tâm logistics",
        "hanja": "物流",
        "hanjaReading": "物(물건 물) + 流(흐를 류)",
        "pronunciation": "쯩 땀 로지스틱",
        "meaningKo": "물류(보관, 분류, 배송)를 전문으로 하는 대형 산업 건축물로, 창고, 하역장, 분류 시스템, 사무동으로 구성됩니다. 한국에서는 이커머스 성장으로 물류센터 수요가 급증하고 있으며, 자동화 물류센터가 확산 중입니다. 통역 시 베트남의 'kho hàng(창고)'와 구분하여, 물류센터는 '분류·배송 기능(chức năng phân loại và giao hàng)'을 갖춘 첨단 시설임을 강조하세요. 베트남 현장에서는 'trung tâm logistics' 또는 'kho phân phối(배송 창고)'로 표현하며, 자동화 수준을 명시하면 이해도가 높아집니다.",
        "meaningVi": "Công trình chuyên về logistics (lưu kho, phân loại, giao hàng) quy mô lớn, gồm kho, khu bốc dỡ, hệ thống phân loại, văn phòng. Do thương mại điện tử phát triển, nhu cầu trung tâm logistics tự động hóa tăng nhanh ở Hàn Quốc.",
        "context": "물류, 이커머스, 배송, 자동화 창고, 산업 건축",
        "culturalNote": "한국은 쿠팡, 마켓컬리 등 이커머스 성장으로 대형 물류센터가 급증했으며, 자동화·로봇 도입이 활발합니다. 베트남은 외국 투자 중심으로 물류센터가 건설되고 있으나, 아직 수작업 중심이 많습니다. 통역 시 한국의 '풀필먼트 센터(trung tâm fulfillment)' 또는 '자동 분류 시스템(hệ thống phân loại tự động)'을 설명하면 베트남 측의 첨단 물류 이해를 도울 수 있습니다. 베트남은 'kho hàng(창고)'라는 표현도 쓰이나, 물류센터는 기능이 더 복합적이므로 'trung tâm logistics'로 구분하세요.",
        "commonMistakes": [
            {
                "mistake": "창고",
                "correction": "물류센터 / 물류 거점",
                "explanation": "창고는 보관만, 물류센터는 분류·배송 기능 포함"
            },
            {
                "mistake": "kho hàng",
                "correction": "trung tâm logistics / kho phân phối",
                "explanation": "'창고'는 보관, 물류센터는 물류 기능 전체"
            },
            {
                "mistake": "배송 창고",
                "correction": "물류센터 / 풀필먼트 센터",
                "explanation": "구어체가 아닌 전문 용어 사용 필요"
            }
        ],
        "examples": [
            {
                "ko": "이 물류센터는 연면적 50,000㎡로 하루 10만 건 처리합니다.",
                "vi": "Trung tâm logistics này diện tích 50.000m² xử lý 100 nghìn đơn hàng/ngày.",
                "situation": "formal"
            },
            {
                "ko": "자동 분류 시스템으로 배송 속도가 2배 빨라졌어요.",
                "vi": "Hệ thống phân loại tự động giúp tăng tốc độ giao hàng gấp đôi.",
                "situation": "onsite"
            },
            {
                "ko": "경기도에 신규 물류센터 건설 중이에요.",
                "vi": "Đang xây dựng trung tâm logistics mới ở Gyeonggi-do.",
                "situation": "informal"
            }
        ],
        "relatedTerms": ["이커머스", "창고", "자동화", "배송", "풀필먼트"]
    },
    {
        "slug": "trung-tam-du-lieu",
        "korean": "데이터센터",
        "vietnamese": "Trung tâm dữ liệu",
        "hanja": None,
        "hanjaReading": None,
        "pronunciation": "쯩 땀 즈 리에우",
        "meaningKo": "IT 서버와 네트워크 장비를 집중 관리하는 특수 목적 건축물로, 냉각 시스템, 무정전 전원(UPS), 보안 시설이 핵심입니다. 한국에서는 클라우드 서비스 확대로 대형 데이터센터 건설이 증가하고 있으며, 전력 소비와 냉각이 설계의 최우선 과제입니다. 통역 시 베트남에서는 'trung tâm dữ liệu' 또는 'data center'라는 영어 표현이 통용되며, 'IDC(Internet Data Center)'라는 약어도 쓰입니다. 베트남 현장에서는 'phòng server(서버실)'와 구분하여, 데이터센터는 '대규모 전문 시설(cơ sở chuyên dụng quy mô lớn)'임을 강조하세요.",
        "meaningVi": "Công trình chuyên dụng quản lý tập trung máy chủ và thiết bị mạng, hệ thống làm mát, nguồn điện liên tục (UPS), an ninh là yếu tố cốt lõi. Do dịch vụ đám mây mở rộng, nhu cầu xây dựng data center lớn tăng nhanh ở Hàn Quốc.",
        "context": "IT 인프라, 클라우드, 서버, 전력, 냉각",
        "culturalNote": "한국은 네이버, 카카오 등 대형 IT 기업이 대규모 데이터센터를 운영하며, 그린 데이터센터(친환경)가 트렌드입니다. 베트남은 외국 클라우드 기업(AWS, Google) 중심으로 데이터센터가 건설되고 있으며, 전력 공급이 주요 이슈입니다. 통역 시 한국의 'Tier 등급(phân loại Tier)' 제도를 설명하면 베트남 측이 데이터센터 안정성을 이해하는 데 도움이 됩니다. 베트남은 'trung tâm dữ liệu' 또는 'data center'로 표현하며, 'IDC'라는 약어도 통용됩니다.",
        "commonMistakes": [
            {
                "mistake": "서버실",
                "correction": "데이터센터 / IDC",
                "explanation": "서버실은 소규모, 데이터센터는 대규모 전문 시설"
            },
            {
                "mistake": "phòng máy chủ",
                "correction": "trung tâm dữ liệu / data center",
                "explanation": "'서버실'은 소규모, 데이터센터는 전문 시설"
            },
            {
                "mistake": "전산실",
                "correction": "데이터센터 / 클라우드 센터",
                "explanation": "전산실은 구시대 용어, 데이터센터가 현대 표현"
            }
        ],
        "examples": [
            {
                "ko": "이 데이터센터는 Tier 3 등급으로 99.98% 가용성을 보장합니다.",
                "vi": "Data center này đạt chuẩn Tier 3 đảm bảo khả dụng 99,98%.",
                "situation": "formal"
            },
            {
                "ko": "냉각 시스템이 전체 전력의 40%를 소비해요.",
                "vi": "Hệ thống làm mát tiêu thụ 40% tổng điện năng.",
                "situation": "onsite"
            },
            {
                "ko": "신규 데이터센터는 그린 에너지로 운영합니다.",
                "vi": "Data center mới vận hành bằng năng lượng xanh.",
                "situation": "informal"
            }
        ],
        "relatedTerms": ["서버", "클라우드", "IDC", "냉각", "전력"]
    },
    {
        "slug": "benh-vien",
        "korean": "병원",
        "vietnamese": "Bệnh viện",
        "hanja": "病院",
        "hanjaReading": "病(병 병) + 院(집 원)",
        "pronunciation": "벵 비엔",
        "meaningKo": "의료 서비스를 제공하는 건축물로, 진료실, 병실, 수술실, 검사실, 약국 등으로 구성됩니다. 한국에서는 의원, 병원, 종합병원, 상급종합병원으로 구분되며, 병원 건축은 감염 관리, 동선 설계, 의료 설비가 핵심입니다. 통역 시 베트남의 'bệnh viện'는 한국의 병원과 동일하나, 한국은 '종합병원(bệnh viện đa khoa)'과 '전문병원(bệnh viện chuyên khoa)'의 구분이 명확합니다. 베트남 현장에서는 의료 설비(thiết bị y tế) 수준과 병상 수(số giường bệnh)를 명시하면 규모를 이해하기 쉽습니다.",
        "meaningVi": "Công trình cung cấp dịch vụ y tế gồm phòng khám, phòng bệnh, phòng mổ, phòng xét nghiệm, nhà thuốc. Ở Hàn Quốc phân loại thành phòng khám, bệnh viện, bệnh viện đa khoa, bệnh viện hạng đặc biệt. Thiết kế bệnh viện tập trung vào kiểm soát nhiễm khuẩn, động tuyến, thiết bị y tế.",
        "context": "의료 건축, 병원 설계, 감염 관리, 의료 시설",
        "culturalNote": "한국은 병원 건축 시 음압 병실(negative pressure room), 감염 동선 분리가 법적으로 의무화되어 있으며, 환자 중심 설계가 강조됩니다. 베트남은 국립병원(bệnh viện công)과 민간병원(bệnh viện tư)의 시설 격차가 크며, 한국식 병원 설계가 참고 사례로 주목받고 있습니다. 통역 시 한국의 '감염 관리(kiểm soát nhiễm khuẩn)' 및 '환자 동선(động tuyến bệnh nhân)' 개념을 설명하면 베트남 의료계의 관심을 유도할 수 있습니다. 베트남은 'bệnh viện'이 일반적이나, 'phòng khám(의원)'과 'bệnh viện(병원)'을 규모로 구분합니다.",
        "commonMistakes": [
            {
                "mistake": "의료 시설",
                "correction": "병원 / 의료 건축물",
                "explanation": "시설은 넓은 개념, 병원은 구체적 건축물"
            },
            {
                "mistake": "cơ sở y tế",
                "correction": "bệnh viện / bệnh viện đa khoa",
                "explanation": "'의료 시설'은 일반적, 병원은 'bệnh viện'으로 명확히"
            },
            {
                "mistake": "병원 건물",
                "correction": "병원 / 병원 시설",
                "explanation": "'건물'은 물리적, '병원'이 기능 포함한 표현"
            }
        ],
        "examples": [
            {
                "ko": "이 병원은 500병상 규모의 종합병원으로 설계됩니다.",
                "vi": "Bệnh viện này được thiết kế quy mô 500 giường bệnh đa khoa.",
                "situation": "formal"
            },
            {
                "ko": "음압 병실을 감염병 대응을 위해 10개 설치해요.",
                "vi": "Lắp 10 phòng áp suất âm để ứng phó bệnh truyền nhiễm.",
                "situation": "onsite"
            },
            {
                "ko": "환자 동선과 의료진 동선을 분리 설계했어요.",
                "vi": "Thiết kế tách động tuyến bệnh nhân và nhân viên y tế.",
                "situation": "informal"
            }
        ],
        "relatedTerms": ["의료 시설", "종합병원", "감염 관리", "병상", "수술실"]
    },
    {
        "slug": "truong-hoc",
        "korean": "학교",
        "vietnamese": "Trường học",
        "hanja": "學校",
        "hanjaReading": "學(배울 학) + 校(학교 교)",
        "pronunciation": "쯩 혹",
        "meaningKo": "교육을 목적으로 하는 건축물로, 교실, 강당, 운동장, 급식실, 도서관 등으로 구성됩니다. 한국에서는 초등학교, 중학교, 고등학교, 대학교로 구분되며, 학교 건축은 안전, 채광, 환기, 교육 환경이 설계 핵심입니다. 통역 시 베트남의 'trường học'은 한국의 학교와 동일하나, 한국은 '그린스마트 미래학교' 정책으로 친환경·첨단 학교가 확산 중입니다. 베트남 현장에서는 교실 수(số phòng học), 학생 수용 인원(sức chứa học sinh)을 명시하면 규모를 이해하기 쉽습니다.",
        "meaningVi": "Công trình phục vụ giáo dục gồm phòng học, hội trường, sân vận động, nhà ăn, thư viện. Ở Hàn Quốc phân loại thành tiểu học, trung học cơ sở, trung học phổ thông, đại học. Thiết kế trường học tập trung vào an toàn, ánh sáng, thông gió, môi trường giáo dục.",
        "context": "교육 시설, 학교 건축, 안전 설계, 교육 환경",
        "culturalNote": "한국은 학교 건축 시 내진 설계, 석면 제거, 그린 리모델링이 정부 정책으로 추진되고 있으며, 학생 안전이 최우선입니다. 베트남은 도시와 농촌 간 학교 시설 격차가 크며, 한국의 선진 학교 설계가 벤치마킹 대상입니다. 통역 시 한국의 '무장애 설계(thiết kế không rào cản)' 및 '친환경 자재(vật liệu thân thiện môi trường)' 개념을 설명하면 베트남 교육계의 관심을 유도할 수 있습니다. 베트남은 'trường học'이 일반적이나, 'trường tiểu học(초등학교)', 'trường cấp 2(중학교)', 'trường cấp 3(고등학교)'으로 세분화됩니다.",
        "commonMistakes": [
            {
                "mistake": "교육 시설",
                "correction": "학교 / 학교 건물",
                "explanation": "시설은 넓은 개념, 학교는 구체적 건축물"
            },
            {
                "mistake": "cơ sở giáo dục",
                "correction": "trường học / trường",
                "explanation": "'교육 시설'은 일반적, 학교는 'trường học'으로 명확히"
            },
            {
                "mistake": "교사 건물",
                "correction": "학교 / 교사(校舍)",
                "explanation": "'교사'는 학교 건물의 한자어 표현, 일반적으로 '학교' 사용"
            }
        ],
        "examples": [
            {
                "ko": "이 학교는 30개 교실에 900명 수용 규모입니다.",
                "vi": "Trường này có 30 phòng học, sức chứa 900 học sinh.",
                "situation": "formal"
            },
            {
                "ko": "내진 설계로 지진에 안전한 학교예요.",
                "vi": "Trường học an toàn khi động đất nhờ thiết kế chống chấn.",
                "situation": "onsite"
            },
            {
                "ko": "신축 학교는 태양광 패널을 설치했어요.",
                "vi": "Trường mới lắp tấm pin mặt trời.",
                "situation": "informal"
            }
        ],
        "relatedTerms": ["교육 시설", "교실", "내진 설계", "그린스쿨", "안전"]
    }
]

# 파일 경로 (절대 경로)
file_path = os.path.join(
    os.path.expanduser("~"),
    "Documents",
    "claude_code",
    "projects",
    "vn.epicstage.co.kr",
    "src",
    "data",
    "terms",
    "construction.json"
)

def main():
    """메인 실행 함수"""
    # 기존 파일 읽기
    with open(file_path, "r", encoding="utf-8") as f:
        existing_data = json.load(f)

    print(f"기존 용어 수: {len(existing_data)}")

    # 새 용어 추가
    existing_data.extend(data)

    print(f"추가 후 용어 수: {len(existing_data)}")

    # 파일 저장 (들여쓰기 2칸, 유니코드 이스케이프 없이)
    with open(file_path, "w", encoding="utf-8") as f:
        json.dump(existing_data, f, ensure_ascii=False, indent=2)

    print(f"✅ {len(data)}개 용어 추가 완료: {file_path}")
    print("\n추가된 용어:")
    for term in data:
        print(f"  - {term['korean']} ({term['vietnamese']})")

if __name__ == "__main__":
    main()
