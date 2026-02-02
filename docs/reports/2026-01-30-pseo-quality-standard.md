# pSEO 품질 기준 & 실행 계획

> 2026-01-30 | Epic Note (vn.epicstage.co.kr)

---

## 1. 좋은 pSEO란 무엇인가

### 업계 정의
pSEO는 템플릿 + 데이터로 수천 개 페이지를 체계적으로 생성하는 전략. 핵심은 **규모와 품질의 균형**.

### Google의 기준 (Helpful Content Update)
- "검색 순위 조작 목적의 자동 생성 콘텐츠는 스팸"
- **Site-Wide Signal**: 도움 안 되는 콘텐츠가 많으면 **사이트 전체** 순위 하락
- pSEO 자체는 금지 아님. **진정한 사용자 가치 제공**이 핵심

### 성공 사례에서 배운 공식

| 사례 | 규모 | 비결 |
|------|------|------|
| **Zapier** | 56,000페이지 / 월 580만 세션 | "{app1} + {app2}" NxN 조합, 독점 통합 데이터 |
| **Canva** | 190,000+ 페이지 / 월 1억+ | 실제 사용 가능한 템플릿이 콘텐츠 자체 |
| **Wise** | 8,500,000 페이지 | 실시간 환율 데이터 = 독점 자산 |
| **Nomadlist** | 24,000 페이지 | 도시별 생활비, 인터넷 등 실측 데이터 |

**공통점**: 모두 **독점 데이터 자산** + **실질적 사용자 가치** 보유

### 실패 패턴
- 도시 이름만 바꾼 50,000페이지 → 3개월 내 98% 인덱스 제거
- 300단어 미만 Thin Content → 패널티
- 한번에 수만 페이지 배포 → 스팸 탐지

---

## 2. Epic Note 품질 기준 (정립)

리서치 결과를 바탕으로 Epic Note에 맞는 기준을 정합니다.

### 용어 페이지 기준

| 항목 | 업계 기준 | **Epic Note 기준** | 현재 |
|------|----------|-------------------|------|
| 고유 콘텐츠 최소 단어 | 500단어 | **600자 (한국어)** | ⚠️ 400~600자 |
| 페이지 간 차별화 | 30%+ | **90%+** | ✅ 100% (각 용어 고유) |
| meaningKo 길이 | - | **150자 이상** | ❌ 40~60자 |
| meaningVi 길이 | - | **100자 이상** | ⚠️ 40~60자 |
| 예문 개수 | - | **3개 이상** | ❌ 1개 |
| pronunciation | - | **필수** | ❌ 0% |
| commonMistakes | - | **2개 이상** | ❌ 0% |
| culturalNote | - | **50자 이상** | ❌ 0% |
| 관련 용어 | 5~10개 링크 | **5개 이상** | ⚠️ 3~4개 |
| 내부 링크 총 수 | 5~10개 | **10개 이상** | ✅ 12~15개 |
| 구조화 데이터 | 필수 | **4개 스키마** | ✅ 완벽 |
| Canonical URL | 필수 | **필수** | ❌ 누락 |

### 가이드 페이지 기준

| 항목 | 업계 기준 | **Epic Note 기준** | 현재 |
|------|----------|-------------------|------|
| 고유 콘텐츠 | 500단어+ | **2,000자 이상** | ✅ 3,000~5,000자 (JSON 있는 72개) |
| 폴백 콘텐츠 | noindex | **JSON 필수 or noindex** | ❌ 8개 폴백 템플릿 |
| 시나리오 대화 | - | **3개 이상** | ✅ (JSON 있으면) |
| 준비 체크리스트 | - | **필수** | ✅ |
| 내부 링크 | 5~10개 | **20개 이상** | ✅ 24개 |

### 기술 SEO 기준

| 항목 | 기준 | 현재 |
|------|------|------|
| Canonical URL | 모든 페이지 | ❌ 누락 |
| OG Image | 도메인별 | ❌ 누락 |
| Twitter Card | summary_large_image | ❌ 누락 |
| LCP | < 2.5초 | ✅ (Next.js SSG) |
| CLS | < 0.1 | ✅ |
| 모바일 반응형 | 필수 | ✅ |

---

## 3. 현재 상태 vs 기준 (GAP 분석)

### 수치 요약

| 항목 | 현재 | 기준 | GAP |
|------|------|------|-----|
| 총 용어 수 | 357개 | - | - |
| meaningKo 평균 | 40~60자 | 150자 | **-90자** |
| pronunciation 채움률 | 0% | 100% | **-100%** |
| commonMistakes 채움률 | 0% | 100% | **-100%** |
| culturalNote 채움률 | 0% | 100% | **-100%** |
| examples 평균 | 1개 | 3개 | **-2개** |
| relatedTerms 평균 | 3~4개 | 5개 | **-1~2개** |
| 가이드 JSON 보유 | 72/80 | 80/80 | **-8개** |
| Canonical URL | 없음 | 전체 | **미구현** |
| OG Image | 없음 | 10개+ | **미구현** |

### 위험도 평가

| 위험 | 수준 | 영향 | 시급도 |
|------|------|------|--------|
| Thin Content (용어 400~600자) | 🟡 중간 | 구글 색인 품질 저하 | P1 |
| 가이드 폴백 8개 | 🔴 높음 | Site-Wide Signal 악영향 | **P0** |
| Canonical 누락 | 🔴 높음 | 중복 색인 (vercel + 커스텀) | **P0** |
| 콘텐츠 깊이 부족 (pronunciation 등) | 🟡 중간 | 경쟁력 저하 | P1 |
| OG Image 누락 | 🟢 낮음 | SNS 공유 효과 감소 | P2 |

---

## 4. 실행 계획

### Phase 1: 긴급 수정 (P0) — 당일

**1-1. Canonical URL 추가**
- 모든 페이지 메타데이터에 `alternates.canonical` 추가
- 파일: layout.tsx, 용어 page.tsx, 가이드 page.tsx

**1-2. 폴백 가이드 noindex 처리**
- JSON 없는 8개 가이드 → `robots: { index: false, follow: true }`
- 내부 링크는 유지 (follow: true)
- 또는: 누락 8개 JSON 즉시 생성

### Phase 2: 콘텐츠 깊이 강화 (P1) — 1주

**2-1. 용어 데이터 보강 (357개)**
- meaningKo: 40~60자 → **150자+** (설명 확장)
- meaningVi: 동일 수준 확장
- pronunciation: 전체 추가 (베트남어 발음 가이드)
- commonMistakes: 2개+ 추가
- culturalNote: 50자+ 추가
- examples: 1개 → **3개+** (상황별: formal/informal/onsite)

**2-2. relatedTerms 보강**
- 현재 3~4개 → 5개+
- 도메인 내 자동 추천 로직 (키워드 매칭)

### Phase 3: 기술 SEO (P1) — 3일

**3-1. OG Image 자동 생성**
- Next.js `opengraph-image.tsx` 활용
- 도메인별 컬러 + 용어/가이드 제목 자동 생성
- 1200×630 사이즈

**3-2. Twitter Card 추가**
- `summary_large_image` 설정

### Phase 4: 콘텐츠 확장 (P2) — 2주

**4-1. 누락 가이드 8개 JSON 생성**
- 80개 완성 목표

**4-2. 도메인 간 교차 링크**
- "다른 분야 비슷한 용어" 섹션 추가
- 예: 농업 "비료" → 화학 원료 관련 용어

**4-3. 용어 페이지 목차 추가**
- 긴 페이지에서 섹션 빠른 이동

### Phase 5: 모니터링 (지속)

| 주기 | 작업 |
|------|------|
| 매주 | Search Console 인덱싱 상태 확인 |
| 매월 | 트래픽 분석, 저성과 페이지 정리 |
| 분기 | 콘텐츠 업데이트, 새 용어 추가 |

---

## 5. 예상 효과

### 개선 전 vs 후

| 지표 | 현재 (개선 전) | 목표 (개선 후) |
|------|--------------|---------------|
| 용어 페이지 평균 콘텐츠 | 400~600자 | **1,200~1,500자** |
| 가이드 폴백 페이지 | 8개 (Thin) | **0개** |
| Canonical URL | 없음 | **전체 적용** |
| 구글 인덱싱률 | 추정 60~70% | **목표 95%+** |
| pSEO 품질 점수 | 8.1/10 | **9.2/10** |

### 2026년 트래픽 전망

| 시점 | 예상 월간 유기 트래픽 |
|------|---------------------|
| 현재 (신규 사이트) | 0 (색인 시작) |
| 3개월 후 | 500~1,000 |
| 6개월 후 (P1 완료) | 3,000~5,000 |
| 12개월 후 (P2 완료) | 10,000~20,000 |

---

## Sources

- [Backlinko - Programmatic SEO](https://backlinko.com/programmatic-seo)
- [Google Search Central - Creating Helpful Content](https://developers.google.com/search/docs/fundamentals/creating-helpful-content)
- [Seomatic - Common pSEO Mistakes](https://seomatic.ai/blog/programmatic-seo-mistakes)
- [Get Passionfruit - Traffic Cliff Guide](https://www.getpassionfruit.com/blog/programmatic-seo-traffic-cliff-guide)
- [AirOps - Hidden Dangers of pSEO](https://www.airops.com/blog/hidden-dangers-of-programmatic-seo)
- [Practical Programmatic - Zapier/Canva/Wise Case Studies](https://practicalprogrammatic.com/examples)
