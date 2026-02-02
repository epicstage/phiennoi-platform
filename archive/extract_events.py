#!/usr/bin/env python3
"""통역 의뢰 메일에서 행사 정보 추출"""

import json
import re
from collections import defaultdict

def extract_event_info(email):
    """메일에서 행사 정보 추출 (규칙 기반)"""

    subject = email.get('subject', '')
    body = email.get('body', '')
    from_addr = email.get('from', '')
    date = email.get('date', '')
    full_text = subject + '\n' + body

    event = {
        'email_id': email.get('id'),
        'email_date': date,
        'email_from': from_addr,
        'email_subject': subject,

        # 추출할 필드
        'event_name': '',           # 행사명
        'organizer': '',            # 주최자/의뢰처
        'event_date': '',           # 행사 일시
        'event_location': '',       # 장소
        'event_type': '',           # 행사 유형 (박람회, 세미나, 회의 등)
        'description': '',          # 내용/업무
        'client_company': '',       # 의뢰 기업
    }

    # 행사명 추출 패턴
    event_patterns = [
        r'(?:행사명|Event|Sự kiện)[:\s]*([^\n]+)',
        r'([\w\s-]+ (?:EXPO|Expo|expo|박람회|전시회|세미나|Seminar|포럼|Forum|컨퍼런스|Conference)[\s\d]*)',
        r'(?:참가|참석|진행).*?([\w\s]+ (?:EXPO|박람회|전시회|세미나|포럼)[\s\d]*)',
        r'\[([^\]]*(?:EXPO|박람회|전시회|세미나|포럼)[^\]]*)\]',
    ]

    for pattern in event_patterns:
        match = re.search(pattern, full_text, re.IGNORECASE)
        if match:
            event['event_name'] = match.group(1).strip()[:100]
            break

    # 제목에서 행사명 추출 (대괄호 안)
    if not event['event_name']:
        bracket_match = re.search(r'\[([^\]]+)\]', subject)
        if bracket_match:
            event['event_name'] = bracket_match.group(1).strip()[:100]

    # 날짜/일시 추출
    date_patterns = [
        r'(?:일시|날짜|Date|Ngày|Thời gian)[:\s]*([^\n]+)',
        r'(\d{4}[-./]\d{1,2}[-./]\d{1,2}(?:\s*[-~]\s*\d{1,2})?)',
        r'(\d{1,2}/\d{1,2}/\d{4})',
        r'(\d{1,2}[-./]\d{1,2}[-./]\d{4})',
    ]

    for pattern in date_patterns:
        match = re.search(pattern, full_text)
        if match:
            event['event_date'] = match.group(1).strip()[:50]
            break

    # 장소 추출
    location_patterns = [
        r'(?:장소|Location|Địa điểm|Venue)[:\s]*([^\n]+)',
        r'(?:at|tại|에서)\s+([^\n,]+(?:센터|Center|Hotel|호텔|Convention|컨벤션|Hall|홀))',
        r'(SECC|Saigon Exhibition|GEM Center|White Palace|호치민|하노이|다낭)',
    ]

    for pattern in location_patterns:
        match = re.search(pattern, full_text, re.IGNORECASE)
        if match:
            event['event_location'] = match.group(1).strip()[:100]
            break

    # 주최자/의뢰처 추출
    organizer_patterns = [
        r'(?:주최|주관|Organizer|Ban tổ chức|BTC)[:\s]*([^\n]+)',
        r'(?:기업|Company|Công ty)[:\s]*([^\n]+)',
    ]

    for pattern in organizer_patterns:
        match = re.search(pattern, full_text, re.IGNORECASE)
        if match:
            event['organizer'] = match.group(1).strip()[:100]
            break

    # 발신자 이메일에서 회사 추출
    if not event['organizer']:
        if 'sinasean' in from_addr.lower():
            event['organizer'] = 'SINASEAN VIETNAM'
        elif 'megaus' in from_addr.lower():
            event['organizer'] = 'MEGA-US EXPO'
        elif 'koretoviet' in from_addr.lower():
            event['organizer'] = 'KORETO VIET'

    # 행사 유형 분류
    type_keywords = {
        '박람회': ['expo', 'exhibition', 'triển lãm', '박람회', '전시회'],
        '세미나': ['seminar', 'hội thảo', '세미나', '워크샵', 'workshop'],
        '회의': ['meeting', 'conference', 'hội nghị', '회의', '미팅'],
        '포럼': ['forum', 'diễn đàn', '포럼'],
        '비즈니스 매칭': ['matching', 'B2B', '매칭', '상담회'],
    }

    text_lower = full_text.lower()
    for event_type, keywords in type_keywords.items():
        if any(kw in text_lower for kw in keywords):
            event['event_type'] = event_type
            break

    # 내용/업무 설명 (본문 첫 200자)
    clean_body = re.sub(r'\s+', ' ', body).strip()
    event['description'] = clean_body[:300] if clean_body else ''

    return event


def is_event_email(email):
    """실제 행사 정보가 담긴 메일인지 확인"""
    subject = email.get('subject', '').lower()
    body = email.get('body', '').lower()
    full_text = subject + ' ' + body

    # 단순 회신/확인 메일 제외
    reply_patterns = ['đã nhận', '감사합니다', 'thank you', '확인했습니다', 'received']
    if len(body) < 100 and any(p in full_text for p in reply_patterns):
        return False

    # 행사 정보가 포함된 메일
    event_indicators = [
        'expo', 'exhibition', '박람회', '전시회', 'triển lãm',
        '일시', '장소', 'địa điểm', 'thời gian', 'venue',
        '통역', 'phiên dịch', 'thông dịch',
        '행사', 'sự kiện', 'event',
    ]

    return any(ind in full_text for ind in event_indicators)


def deduplicate_events(events):
    """같은 행사에 대한 여러 메일을 하나로 통합"""

    # 행사명으로 그룹화
    event_groups = defaultdict(list)

    for e in events:
        # 행사명이 있으면 그걸로 그룹화
        key = e['event_name'].lower()[:30] if e['event_name'] else f"unknown_{e['email_id']}"
        event_groups[key].append(e)

    # 각 그룹에서 가장 정보가 많은 메일 선택
    unique_events = []
    for key, group in event_groups.items():
        # 정보가 가장 많은 것 선택
        best = max(group, key=lambda x: sum(1 for v in x.values() if v))

        # 다른 메일에서 빠진 정보 보충
        for e in group:
            for field in ['event_date', 'event_location', 'organizer', 'event_type']:
                if not best[field] and e[field]:
                    best[field] = e[field]

        unique_events.append(best)

    return unique_events


def main():
    # 메일 데이터 로드
    with open('gmail_data.json', 'r', encoding='utf-8') as f:
        emails = json.load(f)

    print(f"총 {len(emails)}개 메일")

    # 통역 관련 키워드 필터
    keywords = ['통역', '번역', '행사', '세미나', '회의', 'phiên dịch', 'biên dịch',
                'thông dịch', 'hội nghị', 'sự kiện', 'expo', 'exhibition', '박람회',
                '전시회', 'triển lãm']

    filtered = []
    for e in emails:
        text = (e['subject'] + ' ' + e['body']).lower()
        if any(k in text for k in keywords):
            filtered.append(e)

    print(f"통역 관련 메일: {len(filtered)}개")

    # 실제 행사 정보가 있는 메일만 필터링
    event_emails = [e for e in filtered if is_event_email(e)]
    print(f"행사 정보 포함 메일: {len(event_emails)}개")

    # 행사 정보 추출
    events = []
    for email in event_emails:
        event = extract_event_info(email)
        if event['event_name'] or event['event_date']:  # 최소한 행사명이나 날짜가 있어야
            events.append(event)

    print(f"추출된 행사 정보: {len(events)}개")

    # 중복 제거
    unique_events = deduplicate_events(events)
    print(f"중복 제거 후: {len(unique_events)}개")

    # 날짜순 정렬
    unique_events.sort(key=lambda x: x.get('email_date', ''), reverse=True)

    # JSON 저장
    with open('interpretation_events.json', 'w', encoding='utf-8') as f:
        json.dump(unique_events, f, ensure_ascii=False, indent=2)

    # CSV 저장
    import csv
    csv_fields = ['event_name', 'organizer', 'event_date', 'event_location',
                  'event_type', 'client_company', 'email_date', 'email_from', 'description']

    with open('interpretation_events.csv', 'w', encoding='utf-8-sig', newline='') as f:
        writer = csv.DictWriter(f, fieldnames=csv_fields, extrasaction='ignore')
        writer.writeheader()
        writer.writerows(unique_events)

    print("\n저장 완료:")
    print("  - interpretation_events.json")
    print("  - interpretation_events.csv")

    # 요약 출력
    print("\n" + "=" * 60)
    print("추출된 행사 목록")
    print("=" * 60)

    for i, e in enumerate(unique_events[:20], 1):
        print(f"\n{i}. {e['event_name'] or '(행사명 미상)'}")
        print(f"   유형: {e['event_type'] or '-'}")
        print(f"   주최: {e['organizer'] or '-'}")
        print(f"   일시: {e['event_date'] or '-'}")
        print(f"   장소: {e['event_location'] or '-'}")


if __name__ == "__main__":
    main()
