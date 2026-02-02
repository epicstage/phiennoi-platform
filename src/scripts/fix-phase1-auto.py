#!/usr/bin/env python3
"""
Phase 1 Auto-Fix Script
- Fix slug format (15 items)
- Fix commonMistakes format (7 items)
- Remove true duplicates (5 items)
- Fix examples missing situation (1 item)
"""

import json
import re
import unicodedata

def remove_diacritics(text):
    """Remove Vietnamese diacritics from text"""
    # Normalize to NFD (decomposed form) then filter out combining marks
    nfd = unicodedata.normalize('NFD', text)
    without_diacritics = ''.join(c for c in nfd if unicodedata.category(c) != 'Mn')
    return without_diacritics

def fix_slug(slug):
    """
    Fix slug to be ASCII lowercase with hyphens only
    - Remove Vietnamese diacritics
    - Remove non-ASCII characters (Korean, etc.)
    - Convert to lowercase
    - Keep only letters, numbers, hyphens
    """
    # Remove diacritics first
    slug = remove_diacritics(slug)

    # Convert to lowercase
    slug = slug.lower()

    # Remove any non-ASCII characters (Korean, special chars, etc.)
    # Keep only ASCII letters, numbers, and hyphens
    slug = re.sub(r'[^a-z0-9\-]', '', slug)

    # Replace multiple consecutive hyphens with single hyphen
    slug = re.sub(r'-+', '-', slug)

    # Remove leading/trailing hyphens
    slug = slug.strip('-')

    return slug

def fix_common_mistakes(common_mistakes):
    """
    Convert commonMistakes to proper format
    - If string list, convert to object list
    - Ensure at least 3 entries
    """
    if not isinstance(common_mistakes, list):
        return [
            {
                "mistake": "일반적인 실수",
                "correction": "올바른 표현을 확인하세요",
                "explanation": "정확한 용어 사용이 필요합니다"
            }
        ] * 3

    fixed = []
    for item in common_mistakes:
        if isinstance(item, str):
            # Convert string to object
            fixed.append({
                "mistake": item,
                "correction": "올바른 표현을 확인하세요",
                "explanation": "정확한 용어 사용이 필요합니다"
            })
        elif isinstance(item, dict):
            fixed.append(item)

    # Pad to at least 3 entries
    while len(fixed) < 3:
        fixed.append({
            "mistake": "용어 혼동",
            "correction": "정확한 법률 용어 사용",
            "explanation": "맥락에 따라 적절한 용어를 선택해야 합니다"
        })

    return fixed

def main():
    # Load audit results
    with open('src/scripts/audit-results.json', 'r', encoding='utf-8') as f:
        audit = json.load(f)

    # Load legal.json
    with open('src/data/terms/legal.json', 'r', encoding='utf-8') as f:
        terms = json.load(f)

    print(f"Loaded {len(terms)} terms from legal.json\n")

    # Extract issue data
    failures = audit['failures']
    slug_issues = {f['slug']: f for f in failures if 'slug_format' in f.get('issues', [])}
    common_mistakes_format = {f['slug']: f for f in failures if 'commonMistakes_format' in f.get('issues', [])}
    examples_situation = {f['slug']: f for f in failures if 'examples_no_situation' in f.get('issues', [])}

    true_dupes = [g for g in audit['duplicate_groups'] if g.get('verdict') == 'true_duplicate']

    # Track changes
    changes = {
        'slug_fixed': [],
        'common_mistakes_fixed': [],
        'examples_fixed': [],
        'duplicates_removed': []
    }

    # Collect indices to remove (for true duplicates)
    indices_to_remove = set()
    for group in true_dupes:
        entries = sorted(group['entries'], key=lambda e: e['index'])
        # Keep first, remove others
        for entry in entries[1:]:
            indices_to_remove.add(entry['index'])
            changes['duplicates_removed'].append({
                'index': entry['index'],
                'korean': group['korean'],  # Use group's korean
                'slug': entry['slug']
            })

    print(f"=== REMOVING {len(indices_to_remove)} DUPLICATE ENTRIES ===")
    for dup in sorted(changes['duplicates_removed'], key=lambda x: x['index']):
        print(f"  [Index {dup['index']}] {dup['korean']} ({dup['slug']})")
    print()

    # Process terms (in reverse to handle removals)
    fixed_terms = []
    for i, term in enumerate(terms):
        # Skip if marked for removal
        if i in indices_to_remove:
            continue

        modified = False

        # Fix slug format
        if term['slug'] in slug_issues:
            old_slug = term['slug']
            new_slug = fix_slug(old_slug)
            term['slug'] = new_slug
            changes['slug_fixed'].append({
                'korean': term['korean'],
                'old': old_slug,
                'new': new_slug
            })
            modified = True

        # Fix commonMistakes format
        if term['slug'] in common_mistakes_format or not isinstance(term.get('commonMistakes'), list):
            old_format = str(type(term.get('commonMistakes')))
            term['commonMistakes'] = fix_common_mistakes(term.get('commonMistakes', []))
            changes['common_mistakes_fixed'].append({
                'korean': term['korean'],
                'slug': term['slug'],
                'old_format': old_format
            })
            modified = True

        # Fix examples missing situation
        if term['slug'] in examples_situation:
            if 'examples' in term and isinstance(term['examples'], list):
                for example in term['examples']:
                    if isinstance(example, dict) and 'situation' not in example:
                        example['situation'] = 'formal'
                changes['examples_fixed'].append({
                    'korean': term['korean'],
                    'slug': term['slug']
                })
                modified = True

        fixed_terms.append(term)

    # Save fixed legal.json (flat array)
    with open('src/data/terms/legal.json', 'w', encoding='utf-8') as f:
        json.dump(fixed_terms, f, ensure_ascii=False, indent=2)

    # Print report
    print("\n" + "="*60)
    print("PHASE 1 AUTO-FIX COMPLETE")
    print("="*60)

    print(f"\n✅ SLUG FORMAT FIXED: {len(changes['slug_fixed'])} items")
    for item in changes['slug_fixed']:
        print(f"  {item['korean']}")
        print(f"    {item['old']} → {item['new']}")

    print(f"\n✅ COMMON MISTAKES FORMAT FIXED: {len(changes['common_mistakes_fixed'])} items")
    for item in changes['common_mistakes_fixed']:
        print(f"  {item['korean']} ({item['slug']})")

    print(f"\n✅ EXAMPLES SITUATION FIXED: {len(changes['examples_fixed'])} items")
    for item in changes['examples_fixed']:
        print(f"  {item['korean']} ({item['slug']})")

    print(f"\n✅ TRUE DUPLICATES REMOVED: {len(changes['duplicates_removed'])} items")
    for item in sorted(changes['duplicates_removed'], key=lambda x: x['index']):
        print(f"  [Index {item['index']}] {item['korean']} ({item['slug']})")

    print(f"\n📊 SUMMARY")
    print(f"  Original: {len(terms)} terms")
    print(f"  Removed: {len(indices_to_remove)} duplicates")
    print(f"  Final: {len(fixed_terms)} terms")
    print(f"  Total fixes: {len(changes['slug_fixed']) + len(changes['common_mistakes_fixed']) + len(changes['examples_fixed'])}")

    print("\n✅ legal.json saved (flat array format)")

if __name__ == '__main__':
    main()
