#!/usr/bin/env python3
"""통역 의뢰 메일에서 행사 정보 추출 - 개선 버전"""

import json
import re
import csv
from collections import defaultdict
from datetime import datetime

def clean_text(text):
    """텍스트 정리"""
    if not text:
        return ""
    # HTML 엔티티 정리
    text = text.replace('&nbsp;', ' ')
    text = text.replace('&amp;', '&')
    text = re.sub(r'\s+', ' ', text)
    return text.strip()

def extract_between(text, start_markers, end_markers):
    """특정 마커 사이의 텍스트 추출"""
    for start in start_markers:
        for end in end_markers:
            pattern = f'{re.escape(start)}[:\\s]*([^\\n]+(?:\\n(?!{re.escape(end)})[^\\n]*)*)'
            match = re.search(pattern, text, re.IGNORECASE | re.MULTILINE)
            if match:
                return clean_text(match.group(1))
    return ""

def extract_sinasean_event(email):
    """SINASEAN 형식 메일에서 추출"""
    body = email['body']
    subject = email['subject']

    event = {}

    # 행사명 (Tên sự kiện 다음)
    event_match = re.search(r'Tên sự kiện[:\s]*\n*([^\n]+)', body)
    if event_match:
        event['event_name'] = clean_text(event_match.group(1))

    # 제목에서 행사명
    if not event.get('event_name'):
        subj_match = re.search(r'SINASEAN.*?-\s*([^-]+(?:EXPO|KOPIA|Exhibition|박람회|포럼)[^-]*)', subject, re.IGNORECASE)
        if subj_match:
            event['event_name'] = clean_text(subj_match.group(1))

    # 형식 (Hình thức)
    format_match = re.search(r'Hình thức[:\s]*\n*([^\n]+)', body)
    if format_match:
        event['work_type'] = clean_text(format_match.group(1))

    # 날짜 (Thời gian, Ngày)
    date_patterns = [
        r'Ngày\s+(\d{1,2}[/&]\d{1,2}/\d{4})',
        r'(\d{1,2}[/]\d{1,2}[/]\d{4})',
        r'ngày\s+(\d{1,2}/\d{1,2}/\d{4})',
        r'(\d{4}-\d{2}-\d{2})',
    ]
    for pattern in date_patterns:
        match = re.search(pattern, body)
        if match:
            event['event_date'] = match.group(1)
            break

    # 장소
    location_match = re.search(r'Địa điểm[^:]*:[:\s]*\n*([^\n]+)', body)
    if location_match:
        event['location'] = clean_text(location_match.group(1))

    # 시간
    time_match = re.search(r'(\d{1,2}h\d{0,2}|\d{1,2}:\d{2})', body)
    if time_match:
        event['time'] = time_match.group(1)

    return event

def extract_megaus_event(email):
    """MEGA-US 형식 메일에서 추출"""
    body = email['body']
    subject = email['subject']

    event = {
        'event_name': 'MEGA-US EXPO 2025',
        'organizer': 'MEGA-US EXPO 사무국'
    }

    # 장소 추출
    if 'White Palace' in body:
        event['location'] = 'White Palace Hoàng Văn Thụ'

    return event

def extract_kotra_event(email):
    """KOTRA 형식 메일에서 추출"""
    body = email['body']

    event = {
        'organizer': 'KOTRA 호치민'
    }

    # 날짜
    date_match = re.search(r'(\d{4}년\s*\d{1,2}월\s*\d{1,2}일)', body)
    if date_match:
        event['event_date'] = date_match.group(1)

    # 장소
    if 'LOTTE HOTEL' in body:
        event['location'] = 'LOTTE HOTEL SAIGON'

    return event

def extract_generic_event(email):
    """일반 메일에서 추출"""
    body = email['body']
    subject = email['subject']
    full_text = subject + '\n' + body

    event = {}

    # 행사명 (대괄호 안)
    bracket_match = re.search(r'\[([^\]]+(?:EXPO|박람회|전시회|세미나|포럼|Forum)[^\]]*)\]', subject, re.IGNORECASE)
    if bracket_match:
        event['event_name'] = clean_text(bracket_match.group(1))

    # 날짜 패턴
    date_patterns = [
        r'(\d{4}[-./]\d{1,2}[-./]\d{1,2})',
        r'(\d{1,2}[-./]\d{1,2}[-./]\d{4})',
        r'(\d{4}년\s*\d{1,2}월\s*\d{1,2}일)',
    ]
    for pattern in date_patterns:
        match = re.search(pattern, full_text)
        if match:
            event['event_date'] = match.group(1)
            break

    # 장소 키워드
    locations = ['SECC', 'White Palace', 'LOTTE HOTEL', 'GEM Center', 'THE MYST',
                 '호치민', '하노이', 'Saigon', 'Ho Chi Minh']
    for loc in locations:
        if loc.lower() in full_text.lower():
            event['location'] = loc
            break

    return event

def categorize_and_extract(email):
    """메일 유형 분류 후 추출"""
    from_addr = email['from'].lower()
    subject = email['subject']
    body = email['body']

    result = {
        'email_id': email['id'],
        'email_date': email['date'],
        'email_from': email['from'],
        'email_subject': subject,
        'event_name': '',
        'organizer': '',
        'event_date': '',
        'location': '',
        'work_type': '',
        'time': '',
        'notes': ''
    }

    # SINASEAN 메일
    if 'sinasean' in from_addr or 'SINASEAN' in body:
        extracted = extract_sinasean_event(email)
        result.update(extracted)
        result['organizer'] = result.get('organizer') or 'SINASEAN VIETNAM'

    # MEGA-US 메일
    elif 'megaus' in from_addr or 'Mega-us' in body or 'MEGA-US' in body:
        extracted = extract_megaus_event(email)
        result.update(extracted)

    # KOTRA 메일
    elif 'kotra' in from_addr.lower() or 'KOTRA' in body:
        extracted = extract_kotra_event(email)
        result.update(extracted)

    # 기타
    else:
        extracted = extract_generic_event(email)
        result.update(extracted)

    # 제목에서 행사명 보완
    if not result['event_name']:
        # 제목 전체를 행사명으로 사용 (Re: 제거)
        clean_subj = re.sub(r'^(Re:|Fwd:|FW:)\s*', '', subject, flags=re.IGNORECASE)
        if any(kw in clean_subj.lower() for kw in ['expo', '박람회', '전시회', 'exhibition', 'seminar', '세미나', 'forum', '포럼', 'kopia', 'matching']):
            result['event_name'] = clean_subj[:100]

    return result

def is_actual_event_info(email):
    """실제 행사 의뢰/정보 메일인지 확인"""
    body = email['body'].lower()
    subject = email['subject'].lower()

    # 단순 회신 제외
    if len(body) < 150:
        simple_replies = ['đã nhận', '감사', 'thank', 'ok', 'received', 'confirmed', 'cảm ơn']
        if any(r in body for r in simple_replies):
            return False

    # 행사 정보 지표
    event_indicators = [
        'tên sự kiện',      # 행사명
        'địa điểm',         # 장소
        'thời gian',        # 시간
        'hình thức',        # 형식
        'expo',
        'exhibition',
        '박람회',
        '전시회',
        'kopia',
        'matching',
        '통역사',
        'phiên dịch',
        'thông dịch viên',
    ]

    return any(ind in body or ind in subject for ind in event_indicators)

def deduplicate_events(events):
    """같은 행사 중복 제거 - 가장 정보가 많은 것 유지"""
    # 행사명 + 날짜로 그룹화
    groups = defaultdict(list)

    for e in events:
        key = (e['event_name'][:30].lower() if e['event_name'] else '') + '_' + (e['event_date'] or '')
        if key == '_':
            key = f"unknown_{e['email_id']}"
        groups[key].append(e)

    unique = []
    for key, group in groups.items():
        # 정보 완성도 점수로 정렬
        def completeness(e):
            return sum(1 for v in [e['event_name'], e['organizer'], e['event_date'], e['location'], e['work_type']] if v)

        group.sort(key=completeness, reverse=True)
        best = group[0]

        # 다른 메일에서 빠진 정보 보충
        for e in group[1:]:
            for field in ['event_name', 'organizer', 'event_date', 'location', 'work_type', 'time']:
                if not best[field] and e[field]:
                    best[field] = e[field]

        unique.append(best)

    return unique

def main():
    with open('gmail_data.json', 'r', encoding='utf-8') as f:
        emails = json.load(f)

    print(f"총 메일: {len(emails)}개")

    # 통역/행사 관련 필터
    keywords = ['통역', 'phiên dịch', 'thông dịch', 'interpreter',
                'expo', 'exhibition', '박람회', '전시회', 'triển lãm',
                'kopia', 'kotra', 'sinasean', 'megaus', 'matching',
                '세미나', 'seminar', '포럼', 'forum']

    filtered = []
    for e in emails:
        text = (e['subject'] + ' ' + e['body']).lower()
        if any(k in text for k in keywords):
            filtered.append(e)

    print(f"관련 메일: {len(filtered)}개")

    # 실제 행사 정보 메일만
    event_emails = [e for e in filtered if is_actual_event_info(e)]
    print(f"행사 정보 메일: {len(event_emails)}개")

    # 정보 추출
    events = []
    for email in event_emails:
        event = categorize_and_extract(email)
        # 최소한 행사명이나 organizer가 있어야
        if event['event_name'] or event['organizer']:
            events.append(event)

    print(f"추출 성공: {len(events)}개")

    # 중복 제거
    unique_events = deduplicate_events(events)
    print(f"중복 제거 후: {len(unique_events)}개")

    # 날짜순 정렬 (최신 먼저)
    unique_events.sort(key=lambda x: x['email_date'], reverse=True)

    # JSON 저장
    with open('interpretation_requests.json', 'w', encoding='utf-8') as f:
        json.dump(unique_events, f, ensure_ascii=False, indent=2)

    # CSV 저장
    csv_fields = ['event_name', 'organizer', 'event_date', 'time', 'location',
                  'work_type', 'email_date', 'email_from', 'notes']

    with open('interpretation_requests.csv', 'w', encoding='utf-8-sig', newline='') as f:
        writer = csv.DictWriter(f, fieldnames=csv_fields, extrasaction='ignore')
        writer.writeheader()
        writer.writerows(unique_events)

    print("\n저장 완료:")
    print("  - interpretation_requests.json")
    print("  - interpretation_requests.csv")

    # 요약 출력
    print("\n" + "=" * 70)
    print("통역 의뢰 목록 (최근 20개)")
    print("=" * 70)

    for i, e in enumerate(unique_events[:20], 1):
        print(f"\n{i}. {e['event_name'] or '(미상)'}")
        print(f"   의뢰처: {e['organizer'] or '-'}")
        print(f"   일시: {e['event_date'] or '-'} {e['time'] or ''}")
        print(f"   장소: {e['location'] or '-'}")
        print(f"   업무: {e['work_type'] or '-'}")

    # 통계
    print("\n" + "=" * 70)
    print("통계")
    print("=" * 70)

    organizers = defaultdict(int)
    for e in unique_events:
        org = e['organizer'] or '기타'
        organizers[org] += 1

    print("\n의뢰처별 건수:")
    for org, count in sorted(organizers.items(), key=lambda x: -x[1])[:10]:
        print(f"  {org}: {count}건")

if __name__ == "__main__":
    main()
