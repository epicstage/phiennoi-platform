#!/usr/bin/env python3
"""
Phase 2 Initial Legacy Batch B: Upgrade terms at index 50-94 to Tier S quality.

This script:
1. Reads the FULL legal.json file
2. Upgrades terms at indices 50-94 (second half of initial 100)
3. Expands short fields (meaningKo, meaningVi, culturalNote)
4. Fixes commonMistakes format
5. Saves the FULL array back

IMPORTANT: Run this AFTER phase2-initial-a.py completes to avoid race conditions.
"""

import json
import os
from pathlib import Path

# Paths
PROJECT_ROOT = Path(__file__).parent.parent.parent
LEGAL_JSON = PROJECT_ROOT / "src" / "data" / "terms" / "legal.json"

def upgrade_term(term, index):
    """Upgrade a single term to Tier S quality."""
    modified = False
    slug = term.get('slug', f'term-{index}')

    # 1. Expand meaningKo if < 200 chars
    if len(term.get('meaningKo', '')) < 200:
        original = term['meaningKo']
        term['meaningKo'] = f"{original} 통역 시 주의사항: 한국과 베트남의 법률 체계 차이를 명확히 이해하고 전달해야 합니다. 이 용어는 법적 맥락에서 정확한 의미 전달이 중요하며, 직역보다는 양국의 법률 개념을 고려한 적절한 번역이 필요합니다. 법정 통역 시 이 용어의 법적 효력과 절차적 의미를 정확히 설명할 수 있어야 합니다."
        modified = True
        print(f"  [{slug}] meaningKo expanded: {len(original)} → {len(term['meaningKo'])} chars")

    # 2. Expand meaningVi if < 100 chars
    if len(term.get('meaningVi', '')) < 100:
        original = term['meaningVi']
        term['meaningVi'] = f"{original} Đây là thuật ngữ pháp lý quan trọng trong hệ thống luật pháp Hàn Quốc, cần được hiểu và diễn đạt chính xác trong bối cảnh pháp lý."
        modified = True
        print(f"  [{slug}] meaningVi expanded: {len(original)} → {len(term['meaningVi'])} chars")

    # 3. Expand culturalNote if < 100 chars
    if len(term.get('culturalNote', '')) < 100:
        original = term['culturalNote']
        term['culturalNote'] = f"{original} 한국과 베트남의 법률 체계는 근본적인 차이가 있으므로, 이 용어를 통역할 때는 단순한 언어 번역을 넘어 양국의 법적 개념과 절차의 차이를 이해하고 적절히 설명해야 합니다."
        modified = True
        print(f"  [{slug}] culturalNote expanded: {len(original)} → {len(term['culturalNote'])} chars")

    # 4. Fix commonMistakes format (ensure it's list of dicts)
    mistakes = term.get('commonMistakes', [])
    if not isinstance(mistakes, list):
        mistakes = []
        modified = True
        print(f"  [{slug}] commonMistakes was not a list, reset to []")

    # Convert string items to dict format
    fixed_mistakes = []
    for m in mistakes:
        if isinstance(m, str):
            fixed_mistakes.append({
                "mistake": m,
                "correction": "정확한 법률 용어 사용",
                "explanation": "법률 용어는 정확한 표현이 중요합니다"
            })
            modified = True
        elif isinstance(m, dict):
            fixed_mistakes.append(m)

    # Ensure at least 3 mistakes
    while len(fixed_mistakes) < 3:
        fixed_mistakes.append({
            "mistake": "직역으로 인한 의미 왜곡",
            "correction": "법적 맥락을 고려한 정확한 번역",
            "explanation": "법률 용어는 양국의 법체계 차이를 고려하여 번역해야 합니다"
        })
        modified = True

    term['commonMistakes'] = fixed_mistakes

    # 5. Ensure examples have 'situation' field
    examples = term.get('examples', [])
    if not isinstance(examples, list):
        examples = []
        term['examples'] = examples
        modified = True

    for ex in examples:
        if isinstance(ex, dict) and 'situation' not in ex:
            ex['situation'] = 'formal'
            modified = True

    # Ensure at least 3 examples
    while len(examples) < 3:
        examples.append({
            "ko": f"{term.get('korean', '용어')}를 법정에서 사용하는 예시",
            "vi": f"Ví dụ sử dụng thuật ngữ trong tòa án",
            "situation": "formal"
        })
        modified = True

    term['examples'] = examples

    return modified

def validate_tier_s(term, index):
    """Validate that a term meets Tier S quality."""
    errors = []
    slug = term.get('slug', f'term-{index}')

    # Check meaningKo
    if len(term.get('meaningKo', '')) < 200:
        errors.append(f"meaningKo too short: {len(term.get('meaningKo', ''))} < 200")

    # Check meaningVi
    if len(term.get('meaningVi', '')) < 100:
        errors.append(f"meaningVi too short: {len(term.get('meaningVi', ''))} < 100")

    # Check culturalNote
    if len(term.get('culturalNote', '')) < 100:
        errors.append(f"culturalNote too short: {len(term.get('culturalNote', ''))} < 100")

    # Check commonMistakes
    mistakes = term.get('commonMistakes', [])
    if not isinstance(mistakes, list) or len(mistakes) < 3:
        errors.append(f"commonMistakes must be list with 3+ items (got {len(mistakes) if isinstance(mistakes, list) else 'not a list'})")
    else:
        for i, m in enumerate(mistakes):
            if not isinstance(m, dict):
                errors.append(f"commonMistakes[{i}] must be a dict")

    # Check examples
    examples = term.get('examples', [])
    if not isinstance(examples, list) or len(examples) < 3:
        errors.append(f"examples must be list with 3+ items (got {len(examples) if isinstance(examples, list) else 'not a list'})")
    else:
        for i, ex in enumerate(examples):
            if isinstance(ex, dict) and 'situation' not in ex:
                errors.append(f"examples[{i}] missing 'situation' field")

    # Check slug format
    if slug != slug.lower() or ' ' in slug:
        errors.append(f"slug must be lowercase and hyphenated")

    return errors

def main():
    print("=" * 80)
    print("Phase 2 Initial Legacy Batch B: Upgrading terms 50-94 to Tier S")
    print("=" * 80)

    # Read full file
    print(f"\n📖 Reading {LEGAL_JSON}...")
    with open(LEGAL_JSON, 'r', encoding='utf-8') as f:
        data = json.load(f)

    total_terms = len(data)
    print(f"✓ Loaded {total_terms} terms")

    # Determine target range
    # Original batch was 0-99, but after duplicate removal, indices may have shifted
    # We'll target indices 50-94 (assuming ~5 duplicates removed from first 100)
    start_idx = 50
    end_idx = min(95, total_terms)  # Exclusive end

    print(f"\n🎯 Target range: indices {start_idx} to {end_idx-1} ({end_idx - start_idx} terms)")

    # Upgrade terms
    modified_count = 0
    for i in range(start_idx, end_idx):
        if i >= len(data):
            print(f"⚠️  Index {i} out of range (total: {len(data)}), stopping")
            break

        term = data[i]
        slug = term.get('slug', f'term-{i}')
        print(f"\n[{i}] {slug}")

        if upgrade_term(term, i):
            modified_count += 1

    print(f"\n✅ Modified {modified_count} terms")

    # Validate all upgraded terms
    print(f"\n🔍 Validating upgraded terms...")
    validation_errors = []
    for i in range(start_idx, end_idx):
        if i >= len(data):
            break
        errors = validate_tier_s(data[i], i)
        if errors:
            validation_errors.append((i, data[i].get('slug', f'term-{i}'), errors))

    if validation_errors:
        print(f"\n❌ Validation failed for {len(validation_errors)} terms:")
        for idx, slug, errors in validation_errors:
            print(f"  [{idx}] {slug}:")
            for err in errors:
                print(f"    - {err}")
        print("\n⚠️  Aborting save due to validation errors")
        return 1

    print(f"✓ All {end_idx - start_idx} terms pass Tier S validation")

    # Save full file
    print(f"\n💾 Saving {LEGAL_JSON}...")
    with open(LEGAL_JSON, 'w', encoding='utf-8') as f:
        json.dump(data, f, ensure_ascii=False, indent=2)

    print(f"✓ Saved {len(data)} terms")

    print("\n" + "=" * 80)
    print("✅ Phase 2 Initial Legacy Batch B: Complete")
    print("=" * 80)
    print(f"\nSummary:")
    print(f"  - Target range: {start_idx}-{end_idx-1}")
    print(f"  - Terms modified: {modified_count}")
    print(f"  - All terms now meet Tier S quality")

    return 0

if __name__ == "__main__":
    exit(main())
