#!/usr/bin/env python3
"""최종 통역 의뢰 데이터 생성"""

import json
import csv
import re

with open('interpretation_requests.json', 'r', encoding='utf-8') as f:
    events = json.load(f)

# 수동 정제
clean_events = []
seen = set()

for e in events:
    name = e['event_name']

    # 쓰레기 데이터 제외
    if not name or name.startswith('>') or len(name) < 5:
        continue

    # 중복 체크 (이름 정규화)
    normalized = re.sub(r'[^a-zA-Z0-9가-힣]', '', name.lower())[:30]
    if normalized in seen:
        continue
    seen.add(normalized)

    # 데이터 정제
    clean_name = name.replace('//', '').strip()
    clean_name = re.sub(r'^(Re:|Fwd:|FW:)\s*', '', clean_name).strip()

    # 날짜 정제 (전화번호 등 오류 제거)
    date = e['event_date']
    if date and ('39.25' in date or '90.' in date):
        date = ''

    # 장소 정제
    location = e['location'] or ''
    if location.startswith('http') or 'drive.google' in location:
        location = ''
    # 날짜가 장소에 들어간 경우
    if re.match(r'^\d+[/&]\d+', location):
        location = ''

    clean_events.append({
        'no': len(clean_events) + 1,
        'event_name': clean_name,
        'organizer': e['organizer'] or '',
        'event_date': date,
        'location': location[:100] if location else '',
        'work_type': e['work_type'][:80] if e['work_type'] and not e['work_type'].startswith('>') else '',
        'email_date': e['email_date'][:10] if e['email_date'] else ''
    })

# 정렬: 이메일 날짜 기준 최신순
clean_events.sort(key=lambda x: x['email_date'], reverse=True)
for i, e in enumerate(clean_events, 1):
    e['no'] = i

# JSON 저장
with open('통역의뢰_정리.json', 'w', encoding='utf-8') as f:
    json.dump(clean_events, f, ensure_ascii=False, indent=2)

# CSV 저장
fields = ['no', 'event_name', 'organizer', 'event_date', 'location', 'work_type', 'email_date']
with open('통역의뢰_정리.csv', 'w', encoding='utf-8-sig', newline='') as f:
    writer = csv.DictWriter(f, fieldnames=fields)
    writer.writeheader()
    writer.writerows(clean_events)

print(f"총 {len(clean_events)}건 저장 완료")
print()
print("=" * 80)
print(f"{'No':>3} | {'행사명':<45} | {'일시':<12} | {'의뢰처'}")
print("=" * 80)

for e in clean_events:
    name = e['event_name'][:43] + '..' if len(e['event_name']) > 45 else e['event_name']
    print(f"{e['no']:>3} | {name:<45} | {e['event_date']:<12} | {e['organizer']}")
