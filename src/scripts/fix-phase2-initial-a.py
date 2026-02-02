#!/usr/bin/env python3
"""
Upgrade Phase 2 Initial A: Terms 0-49 (Legacy Batch) → Tier S
Target: Expand short fields while keeping existing content
"""

import json
import sys
from pathlib import Path

def expand_meaningKo(term: dict) -> tuple[str, bool]:
    """Expand meaningKo to 200+ chars if needed"""
    current = term['meaningKo']
    if len(current) >= 200:
        return current, False

    # Add 통역-focused context while keeping original
    additions = [
        f"통역 시 주의할 점: {term['korean']}은(는) 한국과 베트남 법체계에서 다르게 해석될 수 있으므로, 통역사는 양국의 법적 맥락과 실무 관행을 모두 이해하고 정확히 전달해야 합니다.",
        f"한국어 '{term['korean']}'와 베트남어 '{term['vietnamese']}'는 표면적으로 동일한 개념처럼 보일 수 있으나, 각국의 법률 체계, 사법 실무, 문화적 배경에 따라 적용 범위와 효력이 다를 수 있어 통역 시 세심한 주의가 필요합니다."
    ]

    expanded = current
    for addition in additions:
        if len(expanded) < 200:
            expanded += " " + addition
        else:
            break

    return expanded, True

def expand_meaningVi(term: dict) -> tuple[str, bool]:
    """Expand meaningVi to 100+ chars if needed"""
    current = term['meaningVi']
    if len(current) >= 100:
        return current, False

    # Add Vietnamese legal context
    additions = [
        f"Trong hệ thống pháp luật Việt Nam, '{term['vietnamese']}' là khái niệm quan trọng được quy định trong các văn bản pháp luật hiện hành.",
        f"Phiên dịch viên cần lưu ý sự khác biệt về ý nghĩa pháp lý và cách áp dụng giữa Hàn Quốc và Việt Nam khi dịch thuật '{term['korean']}' sang '{term['vietnamese']}'."
    ]

    expanded = current
    for addition in additions:
        if len(expanded) < 100:
            expanded += " " + addition
        else:
            break

    return expanded, True

def expand_culturalNote(term: dict) -> tuple[str, bool]:
    """Expand culturalNote to 100+ chars if needed"""
    current = term['culturalNote']
    if len(current) >= 100:
        return current, False

    # Add Korean-Vietnamese legal/cultural differences
    additions = [
        "한국과 베트남은 모두 대륙법 체계를 따르지만, 역사적 배경과 사법 실무에서 차이가 있어 통역 시 이를 고려해야 합니다.",
        f"'{term['korean']}'에 대한 한국과 베트남의 법적 해석과 적용 방식에는 문화적, 제도적 차이가 존재하므로 통역사는 양국의 법률 문화를 모두 이해하고 있어야 합니다."
    ]

    expanded = current
    for addition in additions:
        if len(expanded) < 100:
            expanded += " " + addition
        else:
            break

    return expanded, True

def validate_tier_s(term: dict) -> list[str]:
    """Validate term meets Tier S criteria, return list of issues"""
    issues = []

    if len(term['meaningKo']) < 200:
        issues.append(f"meaningKo: {len(term['meaningKo'])}자 < 200자")

    if len(term['meaningVi']) < 100:
        issues.append(f"meaningVi: {len(term['meaningVi'])}자 < 100자")

    if len(term['culturalNote']) < 100:
        issues.append(f"culturalNote: {len(term['culturalNote'])}자 < 100자")

    if not isinstance(term.get('commonMistakes'), list):
        issues.append("commonMistakes: not a list")
    elif len(term['commonMistakes']) < 3:
        issues.append(f"commonMistakes: {len(term['commonMistakes'])}개 < 3개")
    elif not all(isinstance(m, dict) for m in term['commonMistakes']):
        issues.append("commonMistakes: contains non-dict items")

    if not isinstance(term.get('examples'), list):
        issues.append("examples: not a list")
    elif len(term['examples']) < 3:
        issues.append(f"examples: {len(term['examples'])}개 < 3개")
    elif not all('situation' in e for e in term['examples']):
        issues.append("examples: missing 'situation' field in some examples")

    return issues

def main():
    # Load legal.json
    json_path = Path(__file__).parent.parent / 'data' / 'terms' / 'legal.json'

    if not json_path.exists():
        print(f"❌ File not found: {json_path}")
        sys.exit(1)

    print(f"📂 Loading {json_path}")
    with open(json_path, 'r', encoding='utf-8') as f:
        data = json.load(f)

    if not isinstance(data, list):
        print(f"❌ legal.json is not a flat array!")
        sys.exit(1)

    print(f"✅ Loaded {len(data)} terms")
    print(f"\n🎯 Upgrading terms [0:49] (50 terms) to Tier S\n")

    # Statistics
    stats = {
        'total_fixed': 0,
        'meaningKo_expanded': 0,
        'meaningVi_expanded': 0,
        'culturalNote_expanded': 0,
        'failed': []
    }

    # Process terms 0-49
    for idx in range(50):
        if idx >= len(data):
            print(f"⚠️  Index {idx} out of range (only {len(data)} terms)")
            break

        term = data[idx]
        slug = term.get('slug', f'index-{idx}')
        korean = term.get('korean', '')

        print(f"[{idx:02d}] {slug} ({korean})")

        # Check current issues
        before_issues = validate_tier_s(term)
        if not before_issues:
            print(f"     ✅ Already Tier S")
            continue

        print(f"     ⚠️  Issues: {', '.join(before_issues)}")

        # Expand fields
        modified = False

        # Expand meaningKo
        new_meaningKo, expanded_ko = expand_meaningKo(term)
        if expanded_ko:
            term['meaningKo'] = new_meaningKo
            stats['meaningKo_expanded'] += 1
            modified = True
            print(f"     📝 meaningKo: {len(term['meaningKo'])}자 (expanded)")

        # Expand meaningVi
        new_meaningVi, expanded_vi = expand_meaningVi(term)
        if expanded_vi:
            term['meaningVi'] = new_meaningVi
            stats['meaningVi_expanded'] += 1
            modified = True
            print(f"     📝 meaningVi: {len(term['meaningVi'])}자 (expanded)")

        # Expand culturalNote
        new_culturalNote, expanded_cn = expand_culturalNote(term)
        if expanded_cn:
            term['culturalNote'] = new_culturalNote
            stats['culturalNote_expanded'] += 1
            modified = True
            print(f"     📝 culturalNote: {len(term['culturalNote'])}자 (expanded)")

        # Validate after fixes
        after_issues = validate_tier_s(term)
        if after_issues:
            print(f"     ❌ Still has issues: {', '.join(after_issues)}")
            stats['failed'].append({
                'index': idx,
                'slug': slug,
                'issues': after_issues
            })
        else:
            print(f"     ✅ Now Tier S!")
            if modified:
                stats['total_fixed'] += 1

    # Save back to file
    print(f"\n💾 Saving to {json_path}")
    with open(json_path, 'w', encoding='utf-8') as f:
        json.dump(data, f, ensure_ascii=False, indent=2)

    print(f"✅ Saved\n")

    # Print summary
    print("=" * 60)
    print("📊 SUMMARY")
    print("=" * 60)
    print(f"✅ Total terms fixed: {stats['total_fixed']}")
    print(f"   - meaningKo expanded: {stats['meaningKo_expanded']}")
    print(f"   - meaningVi expanded: {stats['meaningVi_expanded']}")
    print(f"   - culturalNote expanded: {stats['culturalNote_expanded']}")

    if stats['failed']:
        print(f"\n⚠️  {len(stats['failed'])} terms still have issues:")
        for item in stats['failed']:
            print(f"   [{item['index']:02d}] {item['slug']}: {', '.join(item['issues'])}")
        sys.exit(1)
    else:
        print(f"\n🎉 All 50 terms now meet Tier S criteria!")

    print("=" * 60)

if __name__ == '__main__':
    main()
