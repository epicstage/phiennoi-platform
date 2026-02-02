# 세션 핸드오프 - 용어 DB 10배 확장 프로젝트

> 생성: 2026-02-02
> 프로젝트: phiennoi-platform (한-베 통역 용어 데이터베이스)

---

## ⚠️ 현재 상태 (이것만 봐!)

**Legal 도메인 507/1,000 진행 중 ⚖️**
- Medical: 1,000/1,000 ✅ COMPLETE
- Construction: 1,000/1,000 ✅ COMPLETE
- Legal: 507/1,000 🔄 IN PROGRESS (50% 완료)
- 전체 진행률: ~4,307/20,000 (22%)
- ⏸️ 대표님 요청으로 일시 중단

---

## 🎯 프로젝트 목표

**한-베 통역 용어 데이터베이스 10배 확장**
- 기존: 20개 도메인 × 100개 = **2,000개**
- 목표: 20개 도메인 × 1,000개 = **20,000개**
- 품질: 모든 용어 **Tier S (90점 이상)** 필수
- 최종 목표: 20,000개 용어 DB → RAG 기반 통역사 훈련 챗봇 서비스

---

## ✅ 완료된 작업

| 작업 | 상태 | 비고 |
|------|------|------|
| 20개 도메인 초기 구축 (각 100개) | ✅ 완료 | 2,000개 |
| Medical 100→500개 확장 | ✅ 완료 | +400개 추가 |
| Medical 500→1,000개 확장 | ✅ 완료 | +500개 추가 (자율 작업) |
| 2,000+ 용어 프로덕션 배포 | ✅ 완료 | Vercel, 2,213 정적 페이지 |
| 홈페이지 통계/브랜딩 업데이트 | ✅ 완료 | 2,000+ 용어, 20개 분야 |
| EPIC 파비콘 SVG 적용 | ✅ 완료 | icon.svg (Next.js 컨벤션) |
| 이력서 업로드 PDF-only 간소화 | ✅ 완료 | 폼 필드 제거 |

---

## 📊 도메인별 현황

| 도메인 | 현재 | 목표 | 상태 |
|--------|------|------|------|
| **medical** | **1,000** | 1,000 | ✅ 완료 |
| **construction** | **1,000** | 1,000 | ✅ 완료 |
| **legal** | **507** | 1,000 | 🔄 진행중 (50%) |
| agriculture | 100 | 1,000 | ⏳ 대기 |
| automotive | 100 | 1,000 | ⏳ 대기 |
| beauty | 100 | 1,000 | ⏳ 대기 |
| education | 100 | 1,000 | ⏳ 대기 |
| electronics | 100 | 1,000 | ⏳ 대기 |
| environment | 100 | 1,000 | ⏳ 대기 |
| exhibition | 100 | 1,000 | ⏳ 대기 |
| finance | 100 | 1,000 | ⏳ 대기 |
| food | 100 | 1,000 | ⏳ 대기 |
| hr | 100 | 1,000 | ⏳ 대기 |
| it | 100 | 1,000 | ⏳ 대기 |
| legal | 100 | 1,000 | ⏳ 대기 |
| logistics | 100 | 1,000 | ⏳ 대기 |
| manufacturing | 100 | 1,000 | ⏳ 대기 |
| realEstate | 100 | 1,000 | ⏳ 대기 |
| startup | 99 | 1,000 | ⏳ 대기 (중복 1개 정리 필요) |
| textile | 100 | 1,000 | ⏳ 대기 |
| tourism | 100 | 1,000 | ⏳ 대기 |
| trade | 100 | 1,000 | ⏳ 대기 |

**총: 4,307 / 20,000 (22%)**

---

## 🔑 핵심 규칙 (반드시 준수!)

### 1. Tier S 품질 기준 (90+ 점)
```
✅ meaningKo: 200자 이상 + 통역사 팁 포함
✅ commonMistakes: 3개 이상 (각각 객체 형식)
   → {mistake: "...", correction: "...", explanation: "..."}
✅ examples: 3개 이상 (각각 situation 필드 필수)
   → situation: "formal" | "onsite" | "informal"
✅ culturalNote: 100자 이상 (한-베 문화 차이)
✅ meaningVi: 100자 이상 (베트남어 성조 포함)
✅ relatedTerms: 3개 이상
```

### 2. 스크립트 작성법 (검증됨)
```python
import json, os

file_path = os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', 'data', 'terms', 'DOMAIN.json')

with open(file_path, 'r', encoding='utf-8') as f:
    data = json.load(f)  # ⚠️ data가 바로 배열! data['terms'] 아님!

existing_slugs = {t['slug'] for t in data}

new_terms = [
    {
        "slug": "...",
        "korean": "...",
        "vietnamese": "...",  # 성조 필수
        "hanja": "...",       # 또는 None
        "hanjaReading": "...",
        "pronunciation": "...",
        "meaningKo": "...",   # 200자+, 통역 팁 포함
        "meaningVi": "...",   # 100자+
        "context": "...",
        "culturalNote": "...", # 100자+
        "commonMistakes": [   # 3개+
            {"mistake": "...", "correction": "...", "explanation": "..."}
        ],
        "examples": [         # 3개+
            {"ko": "...", "vi": "...", "situation": "formal|onsite|informal"}
        ],
        "relatedTerms": ["...", "...", "..."]  # 3개+
    }
]

filtered = [t for t in new_terms if t['slug'] not in existing_slugs]
data.extend(filtered)

with open(file_path, 'w', encoding='utf-8') as f:
    json.dump(data, f, ensure_ascii=False, indent=2)

print(f"Added {len(filtered)} terms. Total: {len(data)}")
```

### 3. 흔한 에러 방지
- ❌ `data['terms']` → ✅ `data` (JSON이 배열)
- ❌ `term['id']` → ✅ `term['slug']` (id 필드 없음)
- ❌ `null` → ✅ `None` (Python 코드)
- ❌ 따옴표 안 닫기 → ✅ 긴 문자열 특히 주의
- ❌ 상대 경로 `../data/` → ✅ `os.path.join(os.path.dirname(os.path.abspath(__file__)), ...)`

### 4. 작업 방식
- 스크립트 **병렬 생성** OK (Task 에이전트 동시 실행)
- 스크립트 **실행은 순차** (JSON 충돌 방지)
- **배치 크기: 10개/스크립트** (50개는 토큰 초과, 20개는 불안정)
- **500개마다 핸드오프 작성**
- 주기적 dedup 실행 (slug 기준)

---

## 📁 파일 위치

```
/src/data/terms/
├── medical.json      # 1,000개 ✅
├── construction.json  # 1,000개 ✅
├── legal.json        # 507개 🔄
├── it.json           # 100개
├── startup.json      # 99개 (중복 1개)
└── ... (17개 더)     # 각 100개

/src/scripts/
└── add-med-*.py      # 참고용 스크립트 (v4~v6)
```

---

## 💬 다음 세션 할 일

1. **Legal 507→1,000 마무리** (493개 남음, v6~v10 배치 필요)
2. Legal 완료 후 → it → finance 순서
3. startup.json 중복 1개 정리
4. 500개 단위로 핸드오프 업데이트
5. 전체 20,000개 달성 시 빌드 + 배포

### Legal 확장 진행 내역
- v1 (a-j): 민법, 형법, 헌법, 상법, 지재권, 부동산법, 세법, 국제법, 노동법, 환경법 → 100→191
- v2 (a-j): 가족법, 민사소송, 투자법, 출입국, 소비자, 경쟁법, 건설법, 금융법, 사이버법, 중재 → 191→284
- v3 (a-j): 해상보험, 부동산거래, 형사심화, 행정절차, 법조윤리, 지방자치, 교통법, 통관법, 공기업, 의료법 → 284→379
- v4 (a-j): 교육법, 미디어법, 종교/민족, 에너지법, 농업법, 채권법, 선거법, 사회복지, 군사법, 과기법 → 379→478
- v5 (a-c): 주택법, 반부패, 문화체육 → 478→507
- **다음**: v6부터 재개 (예정 테마: 노동심화, 형사특별법, 국제인권, 해양법, 의료분쟁, 건설분쟁, 금융규제, 보험심화, 소년법, 민사집행)

---

## 📝 Medical 확장 회고

- **시작**: 100개 (기존) → 500개 (세션1) → 1,000개 (세션2)
- **전략**: 10개/스크립트 × 14 병렬 에이전트 → 순차 실행
- **주요 테마**: 재활, 노인의학, 응급, 소아/산부인과, 치과/안과/이비인후과, 피부/비뇨기, 정형/신경, 내과/소화기/호흡기, 심장/혈액, 종양/내분비, 의료행정/보험, 외과/마취/중환자, 영양/생활, 감염/공중보건, 한의학, 정신건강, 의료기기, 약학, 간호
- **문제 해결**: SyntaxError(미닫힌 문자열) → 스킵+대체, KeyError('id') → slug 기반으로 수정, 중복 축적 → 주기적 dedup
