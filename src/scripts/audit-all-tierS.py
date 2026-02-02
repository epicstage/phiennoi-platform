#!/usr/bin/env python3
"""
All Domains Tier S Audit Script
Validates every term across all domains against Tier S quality criteria.
Reusable version of audit-legal-tierS.py for the entire platform.
"""

import json
import re
import sys
from pathlib import Path
from collections import defaultdict
from typing import List, Dict, Any, Set


# Legal is already verified - include for completeness but flag it
VERIFIED_DOMAINS = {'legal'}

ALL_DOMAINS = [
    'agriculture', 'automotive', 'beauty', 'construction', 'education',
    'electronics', 'environment', 'exhibition', 'finance', 'food',
    'hr', 'it', 'legal', 'logistics', 'manufacturing', 'medical',
    'realEstate', 'startup', 'textile', 'tourism', 'trade'
]


def is_valid_slug(slug: str) -> bool:
    if not slug:
        return False
    return bool(re.match(r'^[a-z0-9]+(-[a-z0-9]+)*$', slug))


def normalize_text(text: str) -> Set[str]:
    return set(re.findall(r'\w+', text.lower()))


def calculate_similarity(text1: str, text2: str) -> float:
    words1 = normalize_text(text1)
    words2 = normalize_text(text2)
    if not words1 or not words2:
        return 0.0
    intersection = words1 & words2
    union = words1 | words2
    return len(intersection) / len(union) if union else 0.0


def audit_term(term: Dict[str, Any], index: int) -> Dict[str, Any]:
    issues = []
    details = {}

    # meaningKo >= 200
    meaning_ko = term.get('meaningKo', '') or ''
    meaning_ko_len = len(meaning_ko)
    details['meaningKo_len'] = meaning_ko_len
    if meaning_ko_len < 200:
        issues.append('meaningKo_short')

    # meaningKo must contain interpreter tips
    tip_keywords = ['통역', '번역', '주의', '구분', '오해', '실수']
    has_tip = any(keyword in meaning_ko for keyword in tip_keywords)
    details['meaningKo_has_tip'] = has_tip
    if not has_tip:
        issues.append('meaningKo_no_tip')

    # meaningVi >= 100
    meaning_vi = term.get('meaningVi', '') or ''
    meaning_vi_len = len(meaning_vi)
    details['meaningVi_len'] = meaning_vi_len
    if meaning_vi_len < 100:
        issues.append('meaningVi_short')

    # culturalNote >= 100
    cultural_note = term.get('culturalNote', '') or ''
    cultural_note_len = len(cultural_note)
    details['culturalNote_len'] = cultural_note_len
    if cultural_note_len < 100:
        issues.append('culturalNote_short')

    # commonMistakes: list of 3+ dicts
    common_mistakes = term.get('commonMistakes', [])
    details['commonMistakes_type'] = type(common_mistakes).__name__
    details['commonMistakes_count'] = len(common_mistakes) if isinstance(common_mistakes, list) else 0

    if not isinstance(common_mistakes, list):
        issues.append('commonMistakes_format')
    elif len(common_mistakes) < 3:
        issues.append('commonMistakes_count')
    else:
        for i, mistake in enumerate(common_mistakes):
            if not isinstance(mistake, dict):
                issues.append('commonMistakes_format')
                break
            if not all(k in mistake for k in ['mistake', 'correction', 'explanation']):
                issues.append('commonMistakes_format')
                break

    # examples: list of 3+ dicts with situation
    examples = term.get('examples', [])
    details['examples_count'] = len(examples) if isinstance(examples, list) else 0

    if not isinstance(examples, list):
        issues.append('examples_format')
    elif len(examples) < 3:
        issues.append('examples_count')
    else:
        for i, example in enumerate(examples):
            if not isinstance(example, dict):
                issues.append('examples_format')
                break
            if 'situation' not in example:
                issues.append('examples_no_situation')
                break

    # relatedTerms: 3+
    related_terms = term.get('relatedTerms', [])
    details['relatedTerms_count'] = len(related_terms) if isinstance(related_terms, list) else 0
    if not isinstance(related_terms, list) or len(related_terms) < 3:
        issues.append('relatedTerms_count')

    # slug format
    slug = term.get('slug', '')
    if not is_valid_slug(slug):
        issues.append('slug_format')
        details['slug_value'] = slug

    # required fields
    for field in ['korean', 'vietnamese', 'pronunciation', 'context']:
        if not term.get(field):
            issues.append(f'{field}_missing')

    return {
        'index': index,
        'slug': term.get('slug', ''),
        'korean': term.get('korean', ''),
        'issues': issues,
        'details': details
    }


def find_duplicates(terms: List[Dict[str, Any]]) -> List[Dict[str, Any]]:
    korean_map = defaultdict(list)
    for i, term in enumerate(terms):
        korean = term.get('korean', '')
        if korean:
            ctx = term.get('context', '') or ''
            if isinstance(ctx, list):
                ctx = ' '.join(str(c) for c in ctx)
            korean_map[korean].append({
                'index': i,
                'slug': term.get('slug', ''),
                'context': ctx[:50]
            })

    duplicate_groups = []
    for korean, entries in korean_map.items():
        if len(entries) > 1:
            contexts = [e['context'] for e in entries]
            is_similar = False
            for i in range(len(contexts)):
                for j in range(i + 1, len(contexts)):
                    if calculate_similarity(contexts[i], contexts[j]) > 0.5:
                        is_similar = True
                        break
                if is_similar:
                    break
            duplicate_groups.append({
                'korean': korean,
                'entries': entries,
                'verdict': "true_duplicate" if is_similar else "legitimate_homonym"
            })
    return duplicate_groups


def audit_domain(domain: str, terms_dir: Path) -> Dict[str, Any]:
    json_path = terms_dir / f'{domain}.json'
    if not json_path.exists():
        return {'domain': domain, 'error': 'file_not_found', 'total': 0}

    with open(json_path, 'r', encoding='utf-8') as f:
        terms = json.load(f)

    total = len(terms)
    failures = []
    by_issue = defaultdict(int)

    for i, term in enumerate(terms):
        result = audit_term(term, i)
        if result['issues']:
            failures.append(result)
            for issue in result['issues']:
                by_issue[issue] += 1

    duplicates = find_duplicates(terms)
    true_dupes = sum(1 for g in duplicates if g['verdict'] == 'true_duplicate')

    fail_count = len(failures)
    pass_count = total - fail_count
    tier_s_pct = (pass_count / total * 100) if total > 0 else 0

    return {
        'domain': domain,
        'total': total,
        'pass': pass_count,
        'fail': fail_count,
        'tier_s_pct': round(tier_s_pct, 1),
        'by_issue': dict(by_issue),
        'true_duplicates': true_dupes,
        'failures': failures,
        'duplicate_groups': duplicates
    }


def main():
    script_dir = Path(__file__).parent
    project_root = script_dir.parent.parent
    terms_dir = project_root / 'src' / 'data' / 'terms'

    # Allow filtering by domain via CLI
    target_domains = ALL_DOMAINS
    if len(sys.argv) > 1:
        arg = sys.argv[1].replace('--domain=', '')
        target_domains = [d.strip() for d in arg.split(',')]

    print("=" * 70)
    print("TIER S AUDIT - ALL DOMAINS")
    print("=" * 70)

    all_results = []
    grand_total = 0
    grand_pass = 0
    grand_fail = 0

    for domain in target_domains:
        result = audit_domain(domain, terms_dir)
        all_results.append(result)

        if 'error' in result:
            print(f"  {domain:20} ERROR: {result['error']}")
            continue

        grand_total += result['total']
        grand_pass += result['pass']
        grand_fail += result['fail']

        status = "✅" if result['tier_s_pct'] == 100.0 else "❌"
        verified = " (previously verified)" if domain in VERIFIED_DOMAINS else ""
        print(f"  {status} {domain:20} {result['pass']:4}/{result['total']:4} Tier S ({result['tier_s_pct']:5.1f}%) fail={result['fail']}{verified}")

    # Summary
    grand_pct = (grand_pass / grand_total * 100) if grand_total > 0 else 0
    print("\n" + "=" * 70)
    print("GRAND TOTAL")
    print("=" * 70)
    print(f"  Total terms:    {grand_total}")
    print(f"  Tier S pass:    {grand_pass} ({grand_pct:.1f}%)")
    print(f"  Tier S fail:    {grand_fail}")

    # Issue breakdown across all domains
    print("\n" + "-" * 70)
    print("ISSUE BREAKDOWN (all domains)")
    print("-" * 70)
    global_issues = defaultdict(int)
    for r in all_results:
        for issue, count in r.get('by_issue', {}).items():
            global_issues[issue] += count

    for issue, count in sorted(global_issues.items(), key=lambda x: -x[1]):
        print(f"  {issue:40} {count:5}")

    # Per-domain failure details (top 5 per domain)
    print("\n" + "-" * 70)
    print("DOMAINS WITH FAILURES (top issues per domain)")
    print("-" * 70)
    for r in all_results:
        if r.get('fail', 0) > 0:
            print(f"\n  [{r['domain']}] {r['fail']} failures:")
            for issue, count in sorted(r.get('by_issue', {}).items(), key=lambda x: -x[1])[:5]:
                print(f"    {issue:38} {count:4}")

    # Save full results
    output_path = script_dir / 'audit-all-results.json'
    # Strip detailed failures for summary, keep them in full report
    save_data = {
        'summary': {
            'grand_total': grand_total,
            'grand_pass': grand_pass,
            'grand_fail': grand_fail,
            'grand_pct': round(grand_pct, 1),
            'domains': {
                r['domain']: {
                    'total': r['total'],
                    'pass': r.get('pass', 0),
                    'fail': r.get('fail', 0),
                    'tier_s_pct': r.get('tier_s_pct', 0),
                    'by_issue': r.get('by_issue', {}),
                    'true_duplicates': r.get('true_duplicates', 0)
                } for r in all_results if 'error' not in r
            }
        },
        'details': {
            r['domain']: {
                'failures': r.get('failures', []),
                'duplicate_groups': r.get('duplicate_groups', [])
            } for r in all_results if r.get('fail', 0) > 0
        }
    }

    with open(output_path, 'w', encoding='utf-8') as f:
        json.dump(save_data, f, ensure_ascii=False, indent=2)

    print(f"\nFull results saved to: {output_path}")

    # Exit code: 0 if all pass, 1 if any failures
    sys.exit(0 if grand_fail == 0 else 1)


if __name__ == '__main__':
    main()
