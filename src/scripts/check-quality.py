#!/usr/bin/env python3
"""
Tier S Quality Validation Script for Legal Domain Terms
Checks all 1,000 terms against strict quality criteria
"""

import json
import sys
from pathlib import Path
from collections import defaultdict

# Quality thresholds
THRESHOLDS = {
    'meaningKo_min': 200,
    'meaningVi_min': 100,
    'culturalNote_min': 100,
    'commonMistakes_min': 3,
    'examples_min': 3,
    'relatedTerms_min': 3,
}

REQUIRED_FIELDS = [
    'slug', 'korean', 'vietnamese', 'pronunciation',
    'meaningKo', 'meaningVi', 'context', 'culturalNote',
    'commonMistakes', 'examples', 'relatedTerms'
]

INTERPRETER_KEYWORDS = ['통역', '번역', '주의', '구분', '오해', '실수']


def validate_term(term, index):
    """Validate a single term and return list of violations"""
    violations = []
    slug = term.get('slug', f'[MISSING_SLUG_#{index}]')

    # 1. Check meaningKo length
    meaning_ko = term.get('meaningKo', '')
    if len(meaning_ko) < THRESHOLDS['meaningKo_min']:
        violations.append({
            'type': 'meaningKo_too_short',
            'slug': slug,
            'actual': len(meaning_ko),
            'required': THRESHOLDS['meaningKo_min']
        })

    # 2. Check meaningVi length
    meaning_vi = term.get('meaningVi', '')
    if len(meaning_vi) < THRESHOLDS['meaningVi_min']:
        violations.append({
            'type': 'meaningVi_too_short',
            'slug': slug,
            'actual': len(meaning_vi),
            'required': THRESHOLDS['meaningVi_min']
        })

    # 3. Check culturalNote length
    cultural_note = term.get('culturalNote', '')
    if len(cultural_note) < THRESHOLDS['culturalNote_min']:
        violations.append({
            'type': 'culturalNote_too_short',
            'slug': slug,
            'actual': len(cultural_note),
            'required': THRESHOLDS['culturalNote_min']
        })

    # 4. Check commonMistakes count
    common_mistakes = term.get('commonMistakes', [])
    if not isinstance(common_mistakes, list):
        common_mistakes = []
    if len(common_mistakes) < THRESHOLDS['commonMistakes_min']:
        violations.append({
            'type': 'commonMistakes_too_few',
            'slug': slug,
            'actual': len(common_mistakes),
            'required': THRESHOLDS['commonMistakes_min']
        })

    # 5. Check commonMistakes format (must be objects, not strings)
    for i, mistake in enumerate(common_mistakes):
        if isinstance(mistake, str):
            violations.append({
                'type': 'commonMistakes_string_format',
                'slug': slug,
                'index': i,
                'value': mistake[:50]  # First 50 chars
            })
        elif isinstance(mistake, dict):
            # Check required fields
            if not all(k in mistake for k in ['mistake', 'correction', 'explanation']):
                violations.append({
                    'type': 'commonMistakes_missing_fields',
                    'slug': slug,
                    'index': i,
                    'fields': list(mistake.keys())
                })

    # 6. Check examples count
    examples = term.get('examples', [])
    if not isinstance(examples, list):
        examples = []
    if len(examples) < THRESHOLDS['examples_min']:
        violations.append({
            'type': 'examples_too_few',
            'slug': slug,
            'actual': len(examples),
            'required': THRESHOLDS['examples_min']
        })

    # 7. Check examples situation field
    for i, example in enumerate(examples):
        if isinstance(example, dict) and 'situation' not in example:
            violations.append({
                'type': 'examples_missing_situation',
                'slug': slug,
                'index': i
            })

    # 8. Check relatedTerms count
    related_terms = term.get('relatedTerms', [])
    if not isinstance(related_terms, list):
        related_terms = []
    if len(related_terms) < THRESHOLDS['relatedTerms_min']:
        violations.append({
            'type': 'relatedTerms_too_few',
            'slug': slug,
            'actual': len(related_terms),
            'required': THRESHOLDS['relatedTerms_min']
        })

    # 9. Check missing required fields
    missing_fields = [field for field in REQUIRED_FIELDS if field not in term]
    if missing_fields:
        violations.append({
            'type': 'missing_required_fields',
            'slug': slug,
            'fields': missing_fields
        })

    # 10. Check meaningKo for interpreter keywords
    has_keyword = any(keyword in meaning_ko for keyword in INTERPRETER_KEYWORDS)
    if not has_keyword:
        violations.append({
            'type': 'meaningKo_missing_interpreter_keyword',
            'slug': slug,
            'keywords': INTERPRETER_KEYWORDS
        })

    return violations


def main():
    # Load legal.json
    legal_json_path = Path(__file__).parent.parent / 'data' / 'terms' / 'legal.json'

    if not legal_json_path.exists():
        print(f"❌ Error: {legal_json_path} not found")
        sys.exit(1)

    with open(legal_json_path, 'r', encoding='utf-8') as f:
        data = json.load(f)

    terms = data if isinstance(data, list) else []
    total_terms = len(terms)

    print(f"{'='*80}")
    print(f"TIER S QUALITY VALIDATION REPORT - Legal Domain")
    print(f"{'='*80}")
    print(f"Total terms: {total_terms}")
    print()

    # Collect all violations
    all_violations = []
    for i, term in enumerate(terms):
        violations = validate_term(term, i)
        all_violations.extend(violations)

    # Group by type
    violations_by_type = defaultdict(list)
    for v in all_violations:
        violations_by_type[v['type']].append(v)

    # Sort by count (most violations first)
    sorted_types = sorted(violations_by_type.items(), key=lambda x: len(x[1]), reverse=True)

    # Print summary
    print("📊 SUMMARY")
    print("-" * 80)
    for vtype, violations in sorted_types:
        print(f"{len(violations):4d} violations: {vtype}")
    print()
    print(f"Total violations: {len(all_violations)}")
    print(f"Terms with violations: {len(set(v['slug'] for v in all_violations))}")
    print(f"Terms passing: {total_terms - len(set(v['slug'] for v in all_violations))}")
    print()

    # Print detailed lists for each violation type
    print("📋 DETAILED VIOLATIONS (sorted by severity)")
    print("=" * 80)

    for vtype, violations in sorted_types:
        print()
        print(f"🔴 {vtype.upper()} ({len(violations)} violations)")
        print("-" * 80)

        if vtype in ['meaningKo_too_short', 'meaningVi_too_short', 'culturalNote_too_short']:
            for v in violations[:20]:  # Show first 20
                print(f"  • {v['slug']}: {v['actual']} chars (required: {v['required']})")
            if len(violations) > 20:
                print(f"  ... and {len(violations) - 20} more")

        elif vtype in ['commonMistakes_too_few', 'examples_too_few', 'relatedTerms_too_few']:
            for v in violations[:20]:
                print(f"  • {v['slug']}: {v['actual']} items (required: {v['required']})")
            if len(violations) > 20:
                print(f"  ... and {len(violations) - 20} more")

        elif vtype == 'commonMistakes_string_format':
            for v in violations[:20]:
                print(f"  • {v['slug']} [index {v['index']}]: \"{v['value']}...\"")
            if len(violations) > 20:
                print(f"  ... and {len(violations) - 20} more")

        elif vtype == 'commonMistakes_missing_fields':
            for v in violations[:20]:
                print(f"  • {v['slug']} [index {v['index']}]: has fields {v['fields']}")
            if len(violations) > 20:
                print(f"  ... and {len(violations) - 20} more")

        elif vtype == 'examples_missing_situation':
            for v in violations[:20]:
                print(f"  • {v['slug']} [index {v['index']}]")
            if len(violations) > 20:
                print(f"  ... and {len(violations) - 20} more")

        elif vtype == 'missing_required_fields':
            for v in violations[:20]:
                print(f"  • {v['slug']}: missing {v['fields']}")
            if len(violations) > 20:
                print(f"  ... and {len(violations) - 20} more")

        elif vtype == 'meaningKo_missing_interpreter_keyword':
            for v in violations[:20]:
                print(f"  • {v['slug']}")
            if len(violations) > 20:
                print(f"  ... and {len(violations) - 20} more")

    print()
    print("=" * 80)

    # Exit with error code if violations found
    if all_violations:
        print(f"❌ VALIDATION FAILED: {len(all_violations)} violations found")
        sys.exit(1)
    else:
        print("✅ VALIDATION PASSED: All terms meet Tier S quality standards")
        sys.exit(0)


if __name__ == '__main__':
    main()
