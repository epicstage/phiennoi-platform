#!/usr/bin/env python3
"""
Content Quality Analysis Script
Detects low-quality content patterns in legal.json
"""

import json
import re
from collections import Counter, defaultdict
from typing import Dict, List, Set, Tuple

def load_terms(filepath: str) -> List[Dict]:
    """Load terms from JSON file"""
    with open(filepath, 'r', encoding='utf-8') as f:
        return json.load(f)

def check_vietnamese_diacritics(text: str) -> bool:
    """Check if text contains Vietnamese diacritics"""
    vietnamese_chars = set('àáảãạăằắẳẵặâầấẩẫậèéẻẽẹêềếểễệìíỉĩịòóỏõọôồốổỗộơờớởỡợùúủũụưừứửữựỳýỷỹỵđ')
    vietnamese_chars.update('ÀÁẢÃẠĂẰẮẲẴẶÂẦẤẨẪẬÈÉẺẼẸÊỀẾỂỄỆÌÍỈĨỊÒÓỎÕỌÔỒỐỔỖỘƠỜỚỞỠỢÙÚỦŨỤƯỪỨỬỮỰỲÝỶỸỴĐ')
    return any(char in vietnamese_chars for char in text)

def extract_sentences(text: str) -> List[str]:
    """Extract sentences from text"""
    if not text:
        return []
    # Split by Korean sentence endings
    sentences = re.split(r'[.!?]\s+', text)
    return [s.strip() for s in sentences if len(s.strip()) > 10]

def calculate_text_overlap(text1: str, text2: str) -> float:
    """Calculate overlap percentage between two texts"""
    if not text1 or not text2:
        return 0.0

    sentences1 = set(extract_sentences(text1))
    sentences2 = set(extract_sentences(text2))

    if not sentences1 or not sentences2:
        return 0.0

    intersection = sentences1.intersection(sentences2)
    union = sentences1.union(sentences2)

    return len(intersection) / len(union) * 100 if union else 0.0

def find_repeated_phrases(texts: List[str], min_length: int = 20) -> Counter:
    """Find phrases that appear in multiple texts"""
    phrase_counter = Counter()

    for text in texts:
        if not text:
            continue
        # Find phrases between 20-100 chars
        words = text.split()
        for i in range(len(words)):
            for j in range(i + 3, min(len(words) + 1, i + 20)):
                phrase = ' '.join(words[i:j])
                if min_length <= len(phrase) <= 100:
                    phrase_counter[phrase] += 1

    # Return only phrases that appear more than once
    return Counter({k: v for k, v in phrase_counter.items() if v > 1})

def extract_topic_keywords(slug: str, korean: str) -> Set[str]:
    """Extract topic keywords from slug and korean term"""
    keywords = set()

    # Common legal topics in Korean
    legal_topics = [
        '계약', '소송', '법원', '판결', '합의', '증거', '변호',
        '민사', '형사', '행정', '헌법', '상법', '노동',
        '권리', '의무', '소유권', '채권', '담보', '보증',
        '손해배상', '위법', '위헌', '조정', '중재', '재판',
        '고소', '고발', '기소', '피고', '원고', '증인',
        '법인', '회사', '주주', '이사', '감사', '청산',
        '파산', '회생', '압류', '가압류', '가처분',
        '등기', '등록', '신고', '허가', '인가', '승인'
    ]

    for topic in legal_topics:
        if topic in korean or topic in slug:
            keywords.add(topic)

    return keywords

def check_slug_format(slug: str) -> List[str]:
    """Check if slug follows proper format"""
    issues = []

    if not slug:
        issues.append("Empty slug")
        return issues

    if slug != slug.lower():
        issues.append("Contains uppercase")

    if ' ' in slug:
        issues.append("Contains spaces")

    if not re.match(r'^[a-z0-9-]+$', slug):
        issues.append("Contains invalid characters")

    return issues

def analyze_terms(terms: List[Dict]) -> Dict:
    """Comprehensive term quality analysis"""

    results = {
        'total_terms': len(terms),
        'repetitive_content': [],
        'generic_phrases': [],
        'missing_diacritics': [],
        'empty_fields': [],
        'slug_issues': [],
        'topic_distribution': defaultdict(int)
    }

    # Generic filler phrases to detect
    generic_phrases = [
        "하는 것이 중요합니다",
        "에 주의해야 합니다",
        "양국의 차이를 이해하는 것이 필요합니다",
        "반드시 확인해야 합니다",
        "정확한 이해가 필요합니다",
        "주의가 필요합니다",
        "유의해야 합니다",
        "이해하는 것이 중요합니다"
    ]

    # 1. Check for repetitive meaningKo
    print("Analyzing repetitive content...")
    meaning_ko_texts = [(i, term.get('meaningKo', '')) for i, term in enumerate(terms)]

    for i, text1 in meaning_ko_texts:
        for j, text2 in meaning_ko_texts[i+1:]:
            overlap = calculate_text_overlap(text1, text2)
            if overlap >= 50:
                results['repetitive_content'].append({
                    'term1_index': i,
                    'term1_slug': terms[i].get('slug', 'unknown'),
                    'term2_index': j,
                    'term2_slug': terms[j].get('slug', 'unknown'),
                    'overlap_percent': round(overlap, 2)
                })

    # 2. Find most repeated phrases
    print("Finding repeated phrases...")
    all_meaning_ko = [term.get('meaningKo', '') for term in terms]
    all_cultural_notes = [term.get('culturalNote', '') for term in terms]

    repeated_phrases = find_repeated_phrases(all_meaning_ko + all_cultural_notes, min_length=20)

    for phrase, count in repeated_phrases.most_common(20):
        if any(generic in phrase for generic in generic_phrases):
            results['generic_phrases'].append({
                'phrase': phrase,
                'count': count
            })

    # 3-6. Per-term checks
    print("Checking individual terms...")
    topic_keywords_all = defaultdict(int)

    for i, term in enumerate(terms):
        slug = term.get('slug', '')
        korean = term.get('korean', '')
        vietnamese = term.get('vietnamese', '')

        # 3. Vietnamese diacritics
        if vietnamese and not check_vietnamese_diacritics(vietnamese):
            results['missing_diacritics'].append({
                'index': i,
                'slug': slug,
                'vietnamese': vietnamese
            })

        # 4. Empty or null fields
        required_fields = ['slug', 'korean', 'vietnamese', 'meaningKo', 'meaningVi',
                          'context', 'culturalNote', 'commonMistakes', 'examples', 'relatedTerms']

        for field in required_fields:
            value = term.get(field)
            if value is None or value == "" or (isinstance(value, list) and len(value) == 0):
                results['empty_fields'].append({
                    'index': i,
                    'slug': slug,
                    'field': field
                })

        # 5. Slug format issues
        slug_problems = check_slug_format(slug)
        if slug_problems:
            results['slug_issues'].append({
                'index': i,
                'slug': slug,
                'issues': slug_problems
            })

        # 6. Topic distribution
        topics = extract_topic_keywords(slug, korean)
        if topics:
            for topic in topics:
                topic_keywords_all[topic] += 1
        else:
            topic_keywords_all['기타/분류불가'] += 1

    results['topic_distribution'] = dict(sorted(topic_keywords_all.items(),
                                                 key=lambda x: x[1], reverse=True))

    return results

def print_report(results: Dict):
    """Print formatted analysis report"""

    print("\n" + "="*80)
    print("CONTENT QUALITY ANALYSIS REPORT - legal.json")
    print("="*80)

    print(f"\nTotal Terms: {results['total_terms']}")

    # 1. Repetitive Content
    print("\n" + "-"*80)
    print("1. REPETITIVE CONTENT (50%+ overlap)")
    print("-"*80)
    if results['repetitive_content']:
        print(f"Found {len(results['repetitive_content'])} pairs with high overlap:\n")
        for pair in results['repetitive_content'][:10]:  # Show top 10
            print(f"  • {pair['term1_slug']} <-> {pair['term2_slug']}")
            print(f"    Overlap: {pair['overlap_percent']}%")
    else:
        print("✅ No highly repetitive content detected")

    # 2. Generic Phrases
    print("\n" + "-"*80)
    print("2. GENERIC/TEMPLATE PHRASES (20+ chars, repeated 2+ times)")
    print("-"*80)
    if results['generic_phrases']:
        print(f"Found {len(results['generic_phrases'])} repeated generic phrases:\n")
        for item in results['generic_phrases'][:15]:
            print(f"  • [{item['count']}x] {item['phrase'][:70]}...")
    else:
        print("✅ No generic phrases detected")

    # 3. Missing Diacritics
    print("\n" + "-"*80)
    print("3. MISSING VIETNAMESE DIACRITICS")
    print("-"*80)
    if results['missing_diacritics']:
        print(f"⚠️  Found {len(results['missing_diacritics'])} terms without diacritics:\n")
        for item in results['missing_diacritics'][:20]:
            print(f"  • {item['slug']}: {item['vietnamese']}")
    else:
        print("✅ All Vietnamese terms have proper diacritics")

    # 4. Empty Fields
    print("\n" + "-"*80)
    print("4. EMPTY OR NULL FIELDS")
    print("-"*80)
    if results['empty_fields']:
        field_counts = Counter([item['field'] for item in results['empty_fields']])
        print(f"⚠️  Found {len(results['empty_fields'])} empty field instances:\n")
        for field, count in field_counts.most_common():
            print(f"  • {field}: {count} terms")
    else:
        print("✅ No empty fields detected")

    # 5. Slug Issues
    print("\n" + "-"*80)
    print("5. SLUG FORMAT ISSUES")
    print("-"*80)
    if results['slug_issues']:
        print(f"⚠️  Found {len(results['slug_issues'])} slugs with issues:\n")
        for item in results['slug_issues'][:20]:
            print(f"  • {item['slug']}: {', '.join(item['issues'])}")
    else:
        print("✅ All slugs properly formatted")

    # 6. Topic Distribution
    print("\n" + "-"*80)
    print("6. TOPIC DISTRIBUTION (Top 20 categories)")
    print("-"*80)
    total_categorized = sum(v for k, v in results['topic_distribution'].items()
                           if k != '기타/분류불가')
    print(f"Categorized: {total_categorized} / {results['total_terms']} terms\n")

    for topic, count in list(results['topic_distribution'].items())[:20]:
        percentage = (count / results['total_terms']) * 100
        bar = "█" * int(percentage / 2)
        print(f"  {topic:15s} │ {bar:25s} {count:4d} ({percentage:5.1f}%)")

    print("\n" + "="*80)
    print("END OF REPORT")
    print("="*80)

def main():
    filepath = '/Users/mac/Documents/claude_code/projects/vn.epicstage.co.kr/src/data/terms/legal.json'

    print("Loading terms...")
    terms = load_terms(filepath)

    print(f"Loaded {len(terms)} terms")
    print("Starting analysis...\n")

    results = analyze_terms(terms)
    print_report(results)

    # Save detailed results to JSON
    output_path = '/Users/mac/Documents/claude_code/projects/vn.epicstage.co.kr/src/scripts/quality-check-results.json'
    with open(output_path, 'w', encoding='utf-8') as f:
        json.dump(results, f, ensure_ascii=False, indent=2)

    print(f"\n💾 Detailed results saved to: {output_path}")

if __name__ == '__main__':
    main()
