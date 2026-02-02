#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
legal.json 중복 검사 스크립트
- 정확히 중복된 slug
- 유사한 slug (숫자 접미사 차이)
- 정확히 중복된 korean 용어
- 유사한 korean 용어
"""

import json
import re
from collections import Counter, defaultdict
from pathlib import Path


def load_legal_terms():
    """legal.json 로드"""
    json_path = Path(__file__).parent.parent / "data" / "terms" / "legal.json"
    with open(json_path, "r", encoding="utf-8") as f:
        return json.load(f)


def find_exact_duplicate_slugs(terms):
    """정확히 중복된 slug 찾기"""
    slug_counts = Counter(term["slug"] for term in terms)
    duplicates = {slug: count for slug, count in slug_counts.items() if count > 1}
    return duplicates


def find_exact_duplicate_korean(terms):
    """정확히 중복된 korean 필드 찾기"""
    korean_counts = Counter(term["korean"] for term in terms)
    duplicates = {korean: count for korean, count in korean_counts.items() if count > 1}
    return duplicates


def normalize_slug(slug):
    """slug에서 숫자 접미사 제거"""
    # 끝에 있는 -숫자 또는 _숫자 패턴 제거
    return re.sub(r'[-_]\d+$', '', slug)


def find_near_duplicate_slugs(terms):
    """유사한 slug 찾기 (base가 같은 것들)"""
    base_to_slugs = defaultdict(list)

    for term in terms:
        slug = term["slug"]
        base = normalize_slug(slug)
        base_to_slugs[base].append(slug)

    # base가 같은데 실제 slug는 다른 것들 (변형이 있는 경우)
    near_duplicates = {
        base: slugs for base, slugs in base_to_slugs.items()
        if len(slugs) > 1 and len(set(slugs)) > 1
    }

    return near_duplicates


def calculate_korean_similarity(term1, term2):
    """두 한국어 용어의 유사도 계산 (간단한 문자 겹침 체크)"""
    set1 = set(term1)
    set2 = set(term2)

    if not set1 or not set2:
        return 0.0

    intersection = len(set1 & set2)
    union = len(set1 | set2)

    return intersection / union if union > 0 else 0.0


def find_near_duplicate_korean(terms, threshold=0.7):
    """유사한 korean 용어 찾기"""
    similar_pairs = []
    korean_terms = [(term["korean"], term["slug"]) for term in terms]

    for i, (korean1, slug1) in enumerate(korean_terms):
        for korean2, slug2 in korean_terms[i+1:]:
            if korean1 != korean2:  # 정확히 같은 건 이미 체크했으므로 제외
                similarity = calculate_korean_similarity(korean1, korean2)
                if similarity >= threshold:
                    similar_pairs.append({
                        "korean1": korean1,
                        "slug1": slug1,
                        "korean2": korean2,
                        "slug2": slug2,
                        "similarity": round(similarity, 2)
                    })

    return similar_pairs


def main():
    print("=" * 80)
    print("legal.json 중복 검사 시작")
    print("=" * 80)
    print()

    # 데이터 로드
    data = load_legal_terms()
    # legal.json은 배열 형태일 수 있음
    terms = data if isinstance(data, list) else data.get("terms", [])

    print(f"📊 총 용어 수: {len(terms)}")
    print()

    # 1. 정확히 중복된 slug
    print("🔍 1. 정확히 중복된 slug")
    print("-" * 80)
    exact_slug_dups = find_exact_duplicate_slugs(terms)

    if exact_slug_dups:
        print(f"⚠️  발견된 중복 slug: {len(exact_slug_dups)}개")
        for slug, count in sorted(exact_slug_dups.items()):
            print(f"   • {slug}: {count}회 출현")
            # 해당 slug의 korean 용어들 출력
            matching_terms = [t["korean"] for t in terms if t["slug"] == slug]
            for korean in matching_terms:
                print(f"     - {korean}")
    else:
        print("✅ 중복된 slug 없음")
    print()

    # 2. 유사한 slug (base가 같은 것들)
    print("🔍 2. 유사한 slug (숫자 접미사 차이)")
    print("-" * 80)
    near_slug_dups = find_near_duplicate_slugs(terms)

    if near_slug_dups:
        print(f"⚠️  발견된 유사 slug 그룹: {len(near_slug_dups)}개")
        for base, slugs in sorted(near_slug_dups.items()):
            print(f"   • Base: {base}")
            for slug in sorted(set(slugs)):
                matching_terms = [t["korean"] for t in terms if t["slug"] == slug]
                print(f"     - {slug}: {matching_terms[0]}")
    else:
        print("✅ 유사한 slug 없음")
    print()

    # 3. 정확히 중복된 korean 용어
    print("🔍 3. 정확히 중복된 korean 용어")
    print("-" * 80)
    exact_korean_dups = find_exact_duplicate_korean(terms)

    if exact_korean_dups:
        print(f"⚠️  발견된 중복 korean 용어: {len(exact_korean_dups)}개")
        for korean, count in sorted(exact_korean_dups.items()):
            print(f"   • {korean}: {count}회 출현")
            # 해당 korean의 slug들 출력
            matching_slugs = [t["slug"] for t in terms if t["korean"] == korean]
            for slug in matching_slugs:
                print(f"     - {slug}")
    else:
        print("✅ 중복된 korean 용어 없음")
    print()

    # 4. 유사한 korean 용어
    print("🔍 4. 유사한 korean 용어 (유사도 70% 이상)")
    print("-" * 80)
    similar_korean = find_near_duplicate_korean(terms, threshold=0.7)

    if similar_korean:
        print(f"⚠️  발견된 유사 korean 용어 쌍: {len(similar_korean)}개")
        for pair in sorted(similar_korean, key=lambda x: x["similarity"], reverse=True):
            print(f"   • 유사도: {pair['similarity']}")
            print(f"     - {pair['korean1']} ({pair['slug1']})")
            print(f"     - {pair['korean2']} ({pair['slug2']})")
    else:
        print("✅ 유사한 korean 용어 없음 (유사도 70% 이상)")
    print()

    # 요약
    print("=" * 80)
    print("📋 요약")
    print("=" * 80)
    print(f"총 용어 수: {len(terms)}")
    print(f"정확히 중복된 slug: {len(exact_slug_dups)}개")
    print(f"유사한 slug 그룹: {len(near_slug_dups)}개")
    print(f"정확히 중복된 korean: {len(exact_korean_dups)}개")
    print(f"유사한 korean 쌍: {len(similar_korean)}개")
    print()

    # 문제 있으면 종료 코드 1
    if exact_slug_dups or exact_korean_dups:
        print("❌ 정확한 중복이 발견되었습니다. 수정이 필요합니다.")
        return 1
    elif near_slug_dups or similar_korean:
        print("⚠️  유사한 항목이 발견되었습니다. 검토가 필요할 수 있습니다.")
        return 0
    else:
        print("✅ 모든 검사 통과!")
        return 0


if __name__ == "__main__":
    exit(main())
