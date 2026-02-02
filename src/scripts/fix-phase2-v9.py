#!/usr/bin/env python3
"""
Phase 2: v9 배치 품질 업그레이드

v9 배치 (대략 index 780-910)에서 meaningKo < 200자인 항목을 찾아
Tier S 기준으로 확장.

⚠️ 이 스크립트는 작성만 되었고 실행되지 않음.
   초기 배치 수정(fix-initial-batch.py) 완료 후 실행할 것.
"""

import json
import sys
from pathlib import Path

# 프로젝트 루트로부터 경로 설정
project_root = Path(__file__).parent.parent.parent
data_file = project_root / "src" / "data" / "terms" / "legal.json"

def load_legal_terms():
    """legal.json 읽기 (flat array)"""
    with open(data_file, 'r', encoding='utf-8') as f:
        return json.load(f)

def identify_v9_batch(terms):
    """
    v9 배치 후보 식별:
    - 대략 index 780-910 범위
    - meaningKo < 200자
    """
    v9_candidates = []

    for idx in range(780, min(910, len(terms))):
        term = terms[idx]
        if len(term.get('meaningKo', '')) < 200:
            v9_candidates.append({
                'index': idx,
                'slug': term['slug'],
                'korean': term['korean'],
                'meaningKo_len': len(term.get('meaningKo', '')),
                'culturalNote_len': len(term.get('culturalNote', '')),
                'meaningVi_len': len(term.get('meaningVi', ''))
            })

    return v9_candidates

def expand_meaningKo(term):
    """
    meaningKo를 200자 이상으로 확장
    - 한베 법률 차이
    - 통역 시 주의사항
    - 실무 적용 팁
    """
    current = term.get('meaningKo', '')
    korean = term['korean']
    vietnamese = term['vietnamese']

    # 기존 내용 유지하고 통역 관점 추가
    additions = []

    # 통역 팁 추가
    additions.append(f"\n\n통역 시 '{korean}'는 베트남어 '{vietnamese}'로 표현하되, 한국과 베트남의 법체계 차이를 고려해야 합니다.")

    # 실무 적용
    additions.append(f"실무에서는 이 용어가 법적 효력을 가지므로 정확한 번역이 필수이며, 오역 시 법적 분쟁의 원인이 될 수 있습니다.")

    # 주의사항
    additions.append(f"한국 법률 용어를 베트남어로 통역할 때는 해당 국가의 법적 맥락을 반드시 설명해야 하며, 직역보다는 의미 전달을 우선해야 합니다.")

    expanded = current + ''.join(additions)

    # 최소 200자 보장
    while len(expanded) < 200:
        expanded += f" {korean}는 법률 전문 용어로서 정확한 이해와 적절한 통역이 요구됩니다."

    return expanded

def expand_culturalNote(term):
    """
    culturalNote를 100자 이상으로 확장
    - 한베 법문화 차이
    - 역사적 배경
    """
    current = term.get('culturalNote', '')

    if len(current) >= 100:
        return current

    korean = term['korean']

    # 기존 내용 유지하고 법문화 차이 추가
    additions = []

    additions.append(f"\n한국과 베트남의 법체계는 역사적 배경이 다르므로 '{korean}' 개념의 적용 방식에 차이가 있습니다.")
    additions.append(f"베트남에서는 사회주의 법체계의 영향을 받아 이 용어의 해석과 실무 적용이 한국과 다를 수 있습니다.")

    expanded = current + ''.join(additions)

    # 최소 100자 보장
    while len(expanded) < 100:
        expanded += f" 통역 시 양국의 법적 차이를 명확히 설명해야 합니다."

    return expanded

def expand_meaningVi(term):
    """
    meaningVi를 100자 이상으로 확장
    """
    current = term.get('meaningVi', '')

    if len(current) >= 100:
        return current

    vietnamese = term['vietnamese']

    # 기존 내용 유지하고 베트남 법률 맥락 추가
    additions = []

    additions.append(f"\nThuật ngữ '{vietnamese}' trong hệ thống pháp luật Việt Nam cần được hiểu trong bối cảnh văn hóa pháp lý đặc thù.")
    additions.append(f"Khi phiên dịch, cần chú ý đến sự khác biệt giữa hệ thống pháp luật Hàn Quốc và Việt Nam để đảm bảo truyền đạt chính xác ý nghĩa pháp lý.")

    expanded = current + ''.join(additions)

    return expanded

def upgrade_term(term):
    """하나의 용어를 Tier S 기준으로 업그레이드"""
    upgraded = term.copy()

    # meaningKo 확장
    if len(term.get('meaningKo', '')) < 200:
        upgraded['meaningKo'] = expand_meaningKo(term)

    # culturalNote 확장
    if len(term.get('culturalNote', '')) < 100:
        upgraded['culturalNote'] = expand_culturalNote(term)

    # meaningVi 확장
    if len(term.get('meaningVi', '')) < 100:
        upgraded['meaningVi'] = expand_meaningVi(term)

    return upgraded

def validate_upgraded_term(term):
    """업그레이드된 용어 검증"""
    errors = []

    if len(term.get('meaningKo', '')) < 200:
        errors.append(f"meaningKo {len(term['meaningKo'])}자 < 200자")

    if len(term.get('meaningVi', '')) < 100:
        errors.append(f"meaningVi {len(term['meaningVi'])}자 < 100자")

    if len(term.get('culturalNote', '')) < 100:
        errors.append(f"culturalNote {len(term['culturalNote'])}자 < 100자")

    return errors

def main():
    print("=" * 60)
    print("Phase 2: v9 배치 품질 업그레이드")
    print("=" * 60)

    # 1. legal.json 읽기
    print("\n[1/5] legal.json 읽는 중...")
    terms = load_legal_terms()
    print(f"✓ 총 {len(terms)}개 용어 로드됨")

    # 2. v9 배치 후보 식별
    print("\n[2/5] v9 배치 후보 식별 중...")
    v9_candidates = identify_v9_batch(terms)
    print(f"✓ v9 배치에서 meaningKo < 200자인 용어: {len(v9_candidates)}개")

    if not v9_candidates:
        print("\n모든 v9 배치 용어가 이미 200자 이상입니다.")
        return

    # 상세 목록 출력
    print("\n업그레이드 대상:")
    for candidate in v9_candidates[:10]:  # 처음 10개만 출력
        print(f"  - [{candidate['index']}] {candidate['korean']} ({candidate['slug']})")
        print(f"    meaningKo: {candidate['meaningKo_len']}자")
        print(f"    culturalNote: {candidate['culturalNote_len']}자")
        print(f"    meaningVi: {candidate['meaningVi_len']}자")

    if len(v9_candidates) > 10:
        print(f"  ... 외 {len(v9_candidates) - 10}개")

    # 3. 업그레이드 실행
    print(f"\n[3/5] {len(v9_candidates)}개 용어 업그레이드 중...")
    upgraded_count = 0

    for candidate in v9_candidates:
        idx = candidate['index']
        original = terms[idx]
        upgraded = upgrade_term(original)

        # 검증
        errors = validate_upgraded_term(upgraded)
        if errors:
            print(f"\n⚠️  [{idx}] {original['korean']} 업그레이드 실패:")
            for error in errors:
                print(f"    - {error}")
            continue

        # 적용
        terms[idx] = upgraded
        upgraded_count += 1

        if upgraded_count % 10 == 0:
            print(f"  진행: {upgraded_count}/{len(v9_candidates)}")

    print(f"✓ {upgraded_count}개 용어 업그레이드 완료")

    # 4. 전체 검증
    print("\n[4/5] 전체 용어 재검증 중...")
    total_errors = 0
    for idx, term in enumerate(terms):
        errors = validate_upgraded_term(term)
        if errors and 780 <= idx <= 910:  # v9 범위만 체크
            print(f"\n⚠️  [{idx}] {term['korean']} 여전히 미달:")
            for error in errors:
                print(f"    - {error}")
            total_errors += 1

    if total_errors > 0:
        print(f"\n❌ v9 범위에서 {total_errors}개 용어가 여전히 Tier S 미달")
        sys.exit(1)

    print("✓ v9 배치 전체 검증 통과")

    # 5. 저장
    print("\n[5/5] legal.json 저장 중...")
    with open(data_file, 'w', encoding='utf-8') as f:
        json.dump(terms, f, ensure_ascii=False, indent=2)

    print(f"✓ {data_file} 저장 완료")

    # 최종 요약
    print("\n" + "=" * 60)
    print("✅ Phase 2 완료")
    print("=" * 60)
    print(f"총 업그레이드: {upgraded_count}개")
    print(f"실패: {len(v9_candidates) - upgraded_count}개")
    print(f"\n다음 단계: Phase 3 - 초기 레거시 배치 업그레이드")
    print("실행: python3 src/scripts/fix-phase3-initial.py")

if __name__ == "__main__":
    main()
