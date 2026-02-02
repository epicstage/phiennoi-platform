#!/usr/bin/env python3
"""이메일 데이터와 이력서 데이터 병합"""

import json
import csv
from collections import defaultdict

# 이력서 데이터 로드
with open('이력서_프로젝트.json', 'r', encoding='utf-8') as f:
    resume_data = json.load(f)

# 이메일 데이터 로드
with open('통역의뢰_정리.json', 'r', encoding='utf-8') as f:
    email_data = json.load(f)

# 통합 데이터 구조
all_projects = []

# 이력서 데이터 추가 (더 정확함)
for p in resume_data:
    all_projects.append({
        'date': p['date'],
        'event_name': p['event_name'],
        'client': p['client'],
        'location': p['location'],
        'type': p['type'],
        'source': '이력서'
    })

# 이메일에서 이력서에 없는 것만 추가
resume_events = set(p['event_name'].lower()[:30] for p in resume_data)

for e in email_data:
    name = e.get('event_name', '')
    if not name:
        continue

    # 중복 체크
    name_lower = name.lower()[:30]
    if any(name_lower in r or r in name_lower for r in resume_events):
        continue

    all_projects.append({
        'date': e.get('event_date', ''),
        'event_name': name,
        'client': e.get('organizer', ''),
        'location': e.get('location', ''),
        'type': '메일 의뢰',
        'source': '이메일'
    })

# 번호 부여
for i, p in enumerate(all_projects, 1):
    p['no'] = i

# JSON 저장
with open('통역_전체목록.json', 'w', encoding='utf-8') as f:
    json.dump(all_projects, f, ensure_ascii=False, indent=2)

# CSV 저장
fields = ['no', 'date', 'event_name', 'client', 'location', 'type', 'source']
with open('통역_전체목록.csv', 'w', encoding='utf-8-sig', newline='') as f:
    writer = csv.DictWriter(f, fieldnames=fields)
    writer.writeheader()
    writer.writerows(all_projects)

print(f"통합 완료: 총 {len(all_projects)}건")
print(f"  - 이력서: {len(resume_data)}건")
print(f"  - 이메일 추가: {len(all_projects) - len(resume_data)}건")
print()

# 연도별 통계
from collections import Counter
import re

years = []
for p in all_projects:
    match = re.search(r'20\d{2}', p['date'])
    if match:
        years.append(match.group())

year_counts = Counter(years)
print("연도별 건수:")
for y in sorted(year_counts.keys()):
    print(f"  {y}: {year_counts[y]}건")

print()

# 유형별 통계
types = Counter(p['type'] for p in all_projects)
print("유형별 건수:")
for t, c in types.most_common():
    print(f"  {t}: {c}건")

print()

# 발주처별 통계
clients = Counter(p['client'] for p in all_projects if p['client'] and p['client'] != '개인')
print("주요 발주처 TOP 20:")
for c, cnt in clients.most_common(20):
    print(f"  {c}: {cnt}건")

print()
print("=" * 60)
print("저장 파일:")
print("  - 통역_전체목록.json")
print("  - 통역_전체목록.csv")
