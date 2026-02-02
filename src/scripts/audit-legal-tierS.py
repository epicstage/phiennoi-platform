#!/usr/bin/env python3
"""
Legal Domain Tier S Audit Script
Produces precise categorization of all Tier S failures for automated fixing.
"""

import json
import re
from pathlib import Path
from collections import defaultdict
from typing import List, Dict, Any, Set


def get_batch_name(index: int) -> str:
    """Determine batch name by index."""
    if 0 <= index <= 99:
        return "initial"
    elif 100 <= index <= 506:
        return "v1-v5"
    elif 507 <= index <= 600:
        return "v6"
    elif 601 <= index <= 693:
        return "v7"
    elif 694 <= index <= 787:
        return "v8"
    elif 788 <= index <= 907:
        return "v9"
    elif 908 <= index <= 999:
        return "v11"
    else:
        return "unknown"


def normalize_text(text: str) -> Set[str]:
    """Normalize text for comparison (lowercase words)."""
    return set(re.findall(r'\w+', text.lower()))


def calculate_similarity(text1: str, text2: str) -> float:
    """Calculate Jaccard similarity between two texts."""
    words1 = normalize_text(text1)
    words2 = normalize_text(text2)

    if not words1 or not words2:
        return 0.0

    intersection = words1 & words2
    union = words1 | words2

    return len(intersection) / len(union) if union else 0.0


def is_valid_slug(slug: str) -> bool:
    """Check if slug follows format rules."""
    if not slug:
        return False
    # Must be lowercase, only ASCII letters, numbers, hyphens
    return bool(re.match(r'^[a-z0-9]+(-[a-z0-9]+)*$', slug))


def audit_term(term: Dict[str, Any], index: int) -> Dict[str, Any]:
    """Audit a single term for Tier S compliance."""
    issues = []
    details = {}

    # Check meaningKo
    meaning_ko = term.get('meaningKo', '')
    meaning_ko_len = len(meaning_ko)
    details['meaningKo_len'] = meaning_ko_len
    if meaning_ko_len < 200:
        issues.append('meaningKo_short')

    # Check for interpreter tips in meaningKo
    tip_keywords = ['통역', '번역', '주의', '구분', '오해', '실수']
    has_tip = any(keyword in meaning_ko for keyword in tip_keywords)
    details['meaningKo_has_tip'] = has_tip
    if not has_tip:
        issues.append('meaningKo_no_tip')

    # Check meaningVi
    meaning_vi = term.get('meaningVi', '')
    meaning_vi_len = len(meaning_vi)
    details['meaningVi_len'] = meaning_vi_len
    if meaning_vi_len < 100:
        issues.append('meaningVi_short')

    # Check culturalNote
    cultural_note = term.get('culturalNote', '')
    cultural_note_len = len(cultural_note)
    details['culturalNote_len'] = cultural_note_len
    if cultural_note_len < 100:
        issues.append('culturalNote_short')

    # Check commonMistakes
    common_mistakes = term.get('commonMistakes', [])
    details['commonMistakes_type'] = type(common_mistakes).__name__
    details['commonMistakes_count'] = len(common_mistakes) if isinstance(common_mistakes, list) else 0

    if not isinstance(common_mistakes, list):
        issues.append('commonMistakes_format')
    elif len(common_mistakes) < 3:
        issues.append('commonMistakes_count')
    else:
        # Check if all items are objects with required fields
        for i, mistake in enumerate(common_mistakes):
            if not isinstance(mistake, dict):
                issues.append('commonMistakes_format')
                details[f'commonMistakes_{i}_type'] = type(mistake).__name__
                break
            if not all(k in mistake for k in ['mistake', 'correction', 'explanation']):
                issues.append('commonMistakes_format')
                details[f'commonMistakes_{i}_missing'] = [k for k in ['mistake', 'correction', 'explanation'] if k not in mistake]
                break

    # Check examples
    examples = term.get('examples', [])
    details['examples_count'] = len(examples) if isinstance(examples, list) else 0

    if not isinstance(examples, list):
        issues.append('examples_format')
    elif len(examples) < 3:
        issues.append('examples_count')
    else:
        # Check for situation field
        missing_situation = []
        for i, example in enumerate(examples):
            if not isinstance(example, dict):
                issues.append('examples_format')
                break
            if 'situation' not in example:
                missing_situation.append(i)

        if missing_situation:
            issues.append('examples_no_situation')
            details['examples_missing_situation'] = missing_situation

    # Check relatedTerms
    related_terms = term.get('relatedTerms', [])
    details['relatedTerms_count'] = len(related_terms) if isinstance(related_terms, list) else 0
    if not isinstance(related_terms, list) or len(related_terms) < 3:
        issues.append('relatedTerms_count')

    # Check slug format
    slug = term.get('slug', '')
    if not is_valid_slug(slug):
        issues.append('slug_format')
        details['slug_value'] = slug

    # Check required fields
    for field in ['korean', 'vietnamese', 'pronunciation', 'context']:
        if not term.get(field):
            issues.append(f'{field}_missing')

    return {
        'index': index,
        'slug': term.get('slug', ''),
        'korean': term.get('korean', ''),
        'issues': issues,
        'details': details,
        'batch': get_batch_name(index)
    }


def find_duplicates(terms: List[Dict[str, Any]]) -> List[Dict[str, Any]]:
    """Find and categorize duplicate korean terms."""
    korean_map = defaultdict(list)

    for i, term in enumerate(terms):
        korean = term.get('korean', '')
        if korean:
            korean_map[korean].append({
                'index': i,
                'slug': term.get('slug', ''),
                'context': term.get('context', '')[:50]  # First 50 chars
            })

    duplicate_groups = []

    for korean, entries in korean_map.items():
        if len(entries) > 1:
            # Analyze if they are true duplicates or legitimate homonyms
            contexts = [e['context'] for e in entries]

            # Compare contexts pairwise
            is_similar = False
            for i in range(len(contexts)):
                for j in range(i + 1, len(contexts)):
                    similarity = calculate_similarity(contexts[i], contexts[j])
                    if similarity > 0.5:
                        is_similar = True
                        break
                if is_similar:
                    break

            verdict = "true_duplicate" if is_similar else "legitimate_homonym"

            duplicate_groups.append({
                'korean': korean,
                'entries': entries,
                'verdict': verdict
            })

    return duplicate_groups


def main():
    # Load legal.json
    script_dir = Path(__file__).parent
    project_root = script_dir.parent.parent
    legal_path = project_root / 'src' / 'data' / 'terms' / 'legal.json'

    print(f"Loading {legal_path}...")
    with open(legal_path, 'r', encoding='utf-8') as f:
        terms = json.load(f)

    total = len(terms)
    print(f"Total terms: {total}")

    # Audit all terms
    print("Auditing all terms...")
    failures = []
    by_issue = defaultdict(int)

    for i, term in enumerate(terms):
        result = audit_term(term, i)

        if result['issues']:
            failures.append(result)
            for issue in result['issues']:
                by_issue[issue] += 1

    # Find duplicates
    print("Analyzing duplicates...")
    duplicate_groups = find_duplicates(terms)

    # Count true duplicates
    true_duplicates = sum(1 for g in duplicate_groups if g['verdict'] == 'true_duplicate')
    by_issue['duplicate_korean_same_context'] = true_duplicates

    # Calculate pass/fail
    fail_count = len(failures)
    pass_count = total - fail_count

    # Create report
    report = {
        'summary': {
            'total': total,
            'pass': pass_count,
            'fail': fail_count,
            'by_issue': dict(by_issue)
        },
        'failures': failures,
        'duplicate_groups': duplicate_groups
    }

    # Save to JSON
    output_path = script_dir / 'audit-results.json'
    print(f"\nSaving audit results to {output_path}...")
    with open(output_path, 'w', encoding='utf-8') as f:
        json.dump(report, f, ensure_ascii=False, indent=2)

    # Print summary
    print("\n" + "="*70)
    print("LEGAL DOMAIN TIER S AUDIT SUMMARY")
    print("="*70)
    print(f"Total terms:     {total}")
    print(f"Pass (Tier S):   {pass_count} ({pass_count/total*100:.1f}%)")
    print(f"Fail:            {fail_count} ({fail_count/total*100:.1f}%)")
    print("\n" + "-"*70)
    print("Issues breakdown:")
    print("-"*70)

    for issue, count in sorted(by_issue.items(), key=lambda x: -x[1]):
        print(f"  {issue:40} {count:4} ({count/total*100:.1f}%)")

    print("\n" + "-"*70)
    print("Duplicate Analysis:")
    print("-"*70)
    total_duplicates = len(duplicate_groups)
    legitimate = sum(1 for g in duplicate_groups if g['verdict'] == 'legitimate_homonym')
    print(f"  Total duplicate korean values:  {total_duplicates}")
    print(f"  Legitimate homonyms:            {legitimate}")
    print(f"  True duplicates (need fixing):  {true_duplicates}")

    print("\n" + "-"*70)
    print("Failures by batch:")
    print("-"*70)
    batch_failures = defaultdict(int)
    for failure in failures:
        batch_failures[failure['batch']] += 1

    for batch in ['initial', 'v1-v5', 'v6', 'v7', 'v8', 'v9', 'v11', 'unknown']:
        count = batch_failures.get(batch, 0)
        if count > 0:
            print(f"  {batch:15} {count:4} failures")

    print("\n" + "="*70)
    print(f"Full audit results saved to: {output_path}")
    print("="*70)


if __name__ == '__main__':
    main()
