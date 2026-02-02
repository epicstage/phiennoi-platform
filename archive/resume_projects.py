#!/usr/bin/env python3
"""향뉴 이력서에서 프로젝트 정보 추출"""

import json
import csv

# 이력서에서 수동 추출한 데이터
resume_projects = [
    # 프로젝트 / 워크샵 / 세미나
    {"date": "2025.10.01~03", "event_name": "베트남 메콩델타 지역 지속 가능한 환경 조성을 위한 재생에너지 전환 및 폐기물 관리 역량강화사업", "client": "KOICA – 초록우산어린이재단-액션에이드", "location": "", "type": "프로젝트"},
    {"date": "2025.08.19", "event_name": "2024/25 KSP HCMC 교육센터 설립 (우송대학교) 통역", "client": "도시철도관리위원회 (HCMC)", "location": "", "type": "세미나"},
    {"date": "2025.08.12~13", "event_name": "철도산업 국산화 세미나 (한국철도연구원 KRRI) 통역", "client": "도시철도관리위원회 (HCMC)", "location": "", "type": "세미나"},
    {"date": "2025.07.16", "event_name": "KSP 법체계 세미나 (우송대학교) 통역", "client": "도시철도관리위원회 (HCMC)", "location": "", "type": "세미나"},
    {"date": "2025.06.23~25", "event_name": "세종학당 통번역과정 교원 연수 워크샵 (사회자)", "client": "세종학당", "location": "Hilton Hotel (D1, HCMC)", "type": "워크샵"},
    {"date": "2025.01.08", "event_name": "우미희망재단&초등학교 교류활동 (사회자)", "client": "우미희망재단", "location": "Binh My 2 (HCMC, Cu Chi)", "type": "행사"},
    {"date": "2024.12.13", "event_name": "지분인수협약식 (사회자)", "client": "K-water", "location": "Lotte Hotel (D1)", "type": "행사"},
    {"date": "2024.11.28~29", "event_name": "전북대학원 유학설명회 (사회자.발표자)", "client": "전북대학원", "location": "Ramana SG Hotel (D3)", "type": "세미나"},
    {"date": "2024.10.17", "event_name": "K-Food Fair 수출세미나 (사회자.통역사)", "client": "aT (농수산식품유통공사)", "location": "New World Hotel (D1)", "type": "세미나"},
    {"date": "2023.11~2024.04", "event_name": "투득시의 폐수처리공장건설 프로젝트: 통역, 비서, 행정 총무", "client": "태영건설사", "location": "HCMC RO사무실", "type": "프로젝트"},
    {"date": "2022.12.15", "event_name": "교통운반대학교에서 교통 특강 통역", "client": "DOHWA ENGINEERING", "location": "", "type": "세미나"},
    {"date": "2022.12.09", "event_name": "HCMC 버스 노선개편 BRT2-CS9: 최종 워크샵 지원 및 통역", "client": "DOHWA ENGINEERING", "location": "", "type": "워크샵"},
    {"date": "2021.11 (1년)", "event_name": "HCMC 버스 노선개편 BRT2-CS9 비서, 통역", "client": "DOHWA ENGINEERING", "location": "", "type": "프로젝트"},
    {"date": "2016.01 (1년7개월)", "event_name": "MRT프로젝트-2호선 비서, 통역", "client": "DOHWA ENGINEERING", "location": "", "type": "프로젝트"},

    # 전시회 / 현장 통역
    {"date": "2025.10.30~11.1", "event_name": "K-Beauty (BeautifulSmile)", "client": "BeautifulSmile", "location": "SECC전시회 (HCMC, D7)", "type": "전시회"},
    {"date": "2025.10.22~24", "event_name": "VietWater (Dyne Pump)", "client": "다인펌프 (Dyne Pump)", "location": "SECC전시회 (HCMC, D7)", "type": "전시회"},
    {"date": "2025.08.29~30", "event_name": "Beauty Summit (Jbeauty: drlola, fascy)", "client": "Jbeauty (drlola, fascy)", "location": "SECC전시회 (HCMC, D7)", "type": "전시회"},
    {"date": "2025.08.20~22", "event_name": "Innoex 울산 (Gana E&T: VOCs회수장비)", "client": "Gana E&T", "location": "Thiskyhall Sala (HCMC, D2)", "type": "전시회"},
    {"date": "2025.08.14~16", "event_name": "MegaUs (이드엠: 차량공기청정기)", "client": "이드엠", "location": "WhitePalace (HCMC)", "type": "전시회"},
    {"date": "2025.08.07~09", "event_name": "VietFood (서울장수: 막걸리)", "client": "서울장수", "location": "SECC전시회 (HCMC, D7)", "type": "전시회"},
    {"date": "2025.07.24~26", "event_name": "Viet Beauty Show (JDBio)", "client": "JDBio", "location": "SECC전시회 (HCMC, D7)", "type": "전시회"},
    {"date": "2025.06.12~14", "event_name": "ICT Comm (Piolink: 보안솔루션)", "client": "Piolink", "location": "SECC전시회 (HCMC, D7)", "type": "전시회"},
    {"date": "2025.06.05~08", "event_name": "Vipremium (고려은단: 비타민씨)", "client": "고려은단", "location": "SECC전시회 (HCMC, D7)", "type": "전시회"},
    {"date": "2025.03.12~14", "event_name": "Agritechnica (한국농어촌공사: 남해화학)", "client": "한국농어촌공사, 남해화학", "location": "SECC전시회 (HCMC, D7)", "type": "전시회"},
    {"date": "2025.02.24~26", "event_name": "울산재생산업개발센터 (재생산단 타당성 조사)", "client": "울산재생산업개발센터", "location": "Becamex Bau Bang IP", "type": "현장통역"},
    {"date": "2024.12.20~21", "event_name": "국제무술축제 통역", "client": "충주시 & 시민위원회", "location": "시민위원회 (HCMC, D1)", "type": "행사"},
    {"date": "2024.11.07~09", "event_name": "K-Beauty Expo Vietnam (NKHeadSpa)", "client": "NKHeadSpa", "location": "SECC전시회 (HCMC, D7)", "type": "전시회"},
    {"date": "2024.10.30~31", "event_name": "Suwon Univ_Early Startup Package (TF: 쇽업소버)", "client": "수원대학교 (쇽업소버)", "location": "Buyer Visit (HCMC)", "type": "B2B"},
    {"date": "2024.10.23", "event_name": "Marine Industry Research Institute: (대게김)", "client": "해양산업연구원 (대게김)", "location": "Buyer Visit (HCMC)", "type": "B2B"},
    {"date": "2024.09.25~27", "event_name": "AUTOMATION WORLD (HatioLab)", "client": "HatioLab", "location": "WTC Expo Binh Duong", "type": "전시회"},
    {"date": "2024.09.05", "event_name": "KOPIA (동남아 플랜트 수출상담회)", "client": "KOPIA", "location": "Buyer Visit (HCMC)", "type": "B2B"},
    {"date": "2024.08.22~23", "event_name": "STARTUP LEAP PACKAGE (ULSAN)", "client": "울산시", "location": "ThiskyHall Sala (HCMC, D2)", "type": "B2B"},
    {"date": "2024.08.13~14", "event_name": "SECUTECH VN (대진정공: 소방차 생산)", "client": "대진정공", "location": "Buyer Visit (Binh Duong)", "type": "전시회"},
    {"date": "2024.08.01~02", "event_name": "MEDIPHARM EXPO (AITrics: 환자상태악화예측AI)", "client": "AITrics", "location": "SECC전시회 (HCMC, D7)", "type": "전시회"},
    {"date": "2024.06.29~07.03", "event_name": "법륜스님의 호치민시 답사 통역 (방문, 법담…)", "client": "정토회", "location": "HCMC, DongNai사찰들", "type": "행사"},
    {"date": "2024.06.13~15", "event_name": "KMED (Gieum Medi International: Hifu, Needle RF기 등..)", "client": "Gieum Medi International", "location": "SECC전시회 (HCMC, D7)", "type": "전시회"},
    {"date": "2024.06.06~08", "event_name": "ICT-COMM (LightVision – AI 주차장)", "client": "LightVision", "location": "SECC전시회 (HCMC, D7)", "type": "전시회"},
    {"date": "2024.05.30~06.02", "event_name": "VIPREMIUM (나눔푸드 - 나누미홍삼)", "client": "나눔푸드", "location": "SECC전시회 (HCMC, D7)", "type": "전시회"},

    # B2B MATCHING
    {"date": "2025.11.17~19", "event_name": "Koica 환경사업 촉진 (Ecohopia: 유기비료)", "client": "KOICA, Ecohopia", "location": "Ninh Thuan 폐시물처리장", "type": "B2B"},
    {"date": "2025.08.26~27", "event_name": "업체방문 (SkinHealth Cosmetic: OEM, ODM)", "client": "SkinHealth Cosmetic", "location": "HCMC", "type": "B2B"},
    {"date": "2025.07.03~04", "event_name": "업체방문 (Ecohopia: 유기비료)", "client": "Ecohopia", "location": "HCMC", "type": "B2B"},
    {"date": "2025.05.13", "event_name": "아세안 종합품목 무역사절단 (Ecohopia: 유기비료)", "client": "KOTRA, Ecohopia", "location": "Lotte Hotel (D1)", "type": "B2B"},
    {"date": "2025.04.14", "event_name": "비료수입 관련 (남해화학 x Tuong Nguyen)", "client": "남해화학", "location": "Zoom B2B 미팅", "type": "B2B"},
    {"date": "2025.02.19~20", "event_name": "한국화장품 교역 (IBITA x Vinexad)", "client": "IBITA", "location": "Rex Hotel (D1)", "type": "B2B"},
    {"date": "2024.11.14", "event_name": "인천 Tourism Night", "client": "인천시", "location": "Rex Hotel (D1)", "type": "B2B"},
    {"date": "2024.10.17~18", "event_name": "K-Food 수출상담회 (농협홍삼: 한삼인)", "client": "aT, 농협홍삼", "location": "New World Hotel (D1)", "type": "B2B"},
    {"date": "2024.08.27", "event_name": "K-Agro 수출상담회 (아미노랩: 식물영양제)", "client": "aT, 아미노랩", "location": "Lotte Hotel (D1)", "type": "B2B"},
    {"date": "2024.07.24~25", "event_name": "Chungbuk Biz Agency (Bio-interchange Co.,LTD)", "client": "충북비즈에이전시, Bio-interchange", "location": "Nikko Hotel (D1)", "type": "B2B"},
    {"date": "2024.07.16", "event_name": "ECO-FRIENDLY, ENERGY (Hankuk Carbon Co., Ltd)", "client": "한국카본", "location": "New World Hotel (D1)", "type": "B2B"},
    {"date": "2024.06.14", "event_name": "EPECK-ELECTRIC POWER INDUSTRY EXPO Korea", "client": "EPECK", "location": "Zoom B2B 미팅", "type": "B2B"},
    {"date": "2020.11.26", "event_name": "여행 촉진 Zoom 통역 (냐짱 Global Open Tour)", "client": "냐짱 Global Open Tour", "location": "Lotte Hotel (D1)", "type": "B2B"},
    {"date": "2019.06.26", "event_name": "한국수산물 수출 상담회", "client": "수산물수출협회", "location": "New World Hotel (D1)", "type": "B2B"},
    {"date": "2019.05.15", "event_name": "Korea-Asean Digital Content Business RoadShow", "client": "한국콘텐츠진흥원", "location": "Nikko Hotel (D1)", "type": "B2B"},

    # 기타
    {"date": "2025.11.28~29", "event_name": "친선축구경기 개최 (FCTA-HCTAA)", "client": "부산-호치민시 세무사회", "location": "", "type": "행사"},
    {"date": "2025.06.30", "event_name": "구치소면회 (마약)", "client": "개인", "location": "T30 구치소 Cu Chi", "type": "법률통역"},
    {"date": "2025.05~09", "event_name": "구치소면회 (성매매)", "client": "개인", "location": "T30 구치소 Cu Chi", "type": "법률통역"},
    {"date": "2025.02~07", "event_name": "수사 통역 (구치소, 원심) (절도)", "client": "개인", "location": "Thu Duc 경찰청 / T30", "type": "법률통역"},
    {"date": "2024.08.21", "event_name": "무역투자진흥센터, CityGame와 총영사관과의 회의", "client": "한국총영사관", "location": "Lotte Hotel (D1)", "type": "회의"},
    {"date": "2024.08.05", "event_name": "Madison Group와 하나투어 여행사와의 여행촉진미팅", "client": "하나투어", "location": "Madison Group (D1)", "type": "회의"},
    {"date": "2024.07.26", "event_name": "무역투자진흥센터, CityGame와 총영사관과의 회의", "client": "한국총영사관", "location": "호치민 한국총영사관", "type": "회의"},
    {"date": "2024.07.12", "event_name": "일방적으로 계약해지에 대한 노동분쟁 합의 통역", "client": "개인", "location": "Thu Duc법원", "type": "법률통역"},
    {"date": "2024.07.08", "event_name": "BariaVungTau관광청과 총영사관과의 여행촉진미팅", "client": "한국총영사관", "location": "호치민 한국총영사관", "type": "회의"},

    # 한국 파트타임
    {"date": "2017.10.19", "event_name": "수산물 해외바이어 초청 상담회", "client": "수산물수출협회", "location": "충남 보령", "type": "B2B"},
    {"date": "2017.09.25", "event_name": "국제한장바이오산업 엑스포", "client": "", "location": "제천", "type": "전시회"},
    {"date": "2017.09.21", "event_name": "GTI EXPO-국제무역투자 박람회", "client": "GTI", "location": "강원도-동해웰빙레포츠타운", "type": "전시회"},
]

# 번호 추가
for i, p in enumerate(resume_projects, 1):
    p['no'] = i

# JSON 저장
with open('이력서_프로젝트.json', 'w', encoding='utf-8') as f:
    json.dump(resume_projects, f, ensure_ascii=False, indent=2)

# CSV 저장
fields = ['no', 'date', 'event_name', 'client', 'location', 'type']
with open('이력서_프로젝트.csv', 'w', encoding='utf-8-sig', newline='') as f:
    writer = csv.DictWriter(f, fieldnames=fields)
    writer.writeheader()
    writer.writerows(resume_projects)

print(f"이력서에서 {len(resume_projects)}건 추출 완료")
print()

# 통계
from collections import Counter
types = Counter(p['type'] for p in resume_projects)
print("유형별 건수:")
for t, c in types.most_common():
    print(f"  {t}: {c}건")

print()
clients = Counter(p['client'] for p in resume_projects if p['client'])
print("주요 발주처:")
for c, cnt in clients.most_common(15):
    print(f"  {c}: {cnt}건")
