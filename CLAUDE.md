# Phiennoi Platform - 한베 통역 전문용어 플랫폼

> 전역 에피 시스템 규칙: `~/.claude/CLAUDE.md`
> 이 파일: 프로젝트 고유 규칙 (품질 기준 등)

---

## 프로젝트 정보

- **이름**: Phiennoi Platform (vn.epicstage.co.kr)
- **목적**: 한국어-베트남어 통역사를 위한 전문용어 학습 플랫폼
- **핵심 자산**: 20개 도메인 × 1,000개 용어 = 20,000개 전문용어 DB (목표)
- **현황**: Medical 1,000 / Construction 1,000 / Legal 1,000 / 나머지 17개 도메인 100개씩

---

## ⚠️ 콘텐츠 품질 규칙 (필수)

> **이 규칙은 절대 타협 불가. 모든 용어 데이터는 Tier S 기준을 충족해야 함.**

### 최소 품질 기준: Tier S (90점 이상)

모든 신규/수정 용어는 아래 기준을 **반드시** 충족:

| 필드 | 기준 | 필수 |
|------|------|------|
| `slug` | 베트남어 기반, 소문자, 하이픈 | ✅ |
| `korean` | 1~50자 | ✅ |
| `vietnamese` | 성조 포함 필수 | ✅ |
| `hanja` | 한자 또는 null (외래어) | ✅ |
| `hanjaReading` | "X(훈 음) + Y(훈 음)" 형식 | ✅ (한자 있을 때) |
| `pronunciation` | 한글 발음 표기 | ✅ |
| `meaningKo` | **200자 이상**, 통역 팁 필수 포함 | ✅ |
| `meaningVi` | **100자 이상** | ✅ |
| `context` | 사용 맥락 | ✅ |
| `culturalNote` | **100자 이상**, 한베 문화 차이 | ✅ |
| `commonMistakes` | **3개 이상**, 객체 형식 | ✅ |
| `examples` | **3개 이상**, situation 포함 | ✅ |
| `relatedTerms` | **3개 이상** | ✅ |

### commonMistakes 필수 형식

```json
{
  "commonMistakes": [
    {
      "mistake": "잘못된 표현",
      "correction": "올바른 표현",
      "explanation": "왜 잘못인지 설명"
    }
  ]
}
```

### examples 필수 형식

```json
{
  "examples": [
    {
      "ko": "한국어 예문",
      "vi": "베트남어 예문",
      "situation": "formal|onsite|informal"
    }
  ]
}
```

### meaningKo 필수 포함 키워드 (최소 1개)

- "통역", "번역", "주의", "구분", "오해", "실수"
- 실제 통역 현장에서의 팁을 반드시 포함할 것

---

## 품질 검증 명령어

```bash
# 전체 검증
npm run validate:terms

# 도메인별 검증
npm run validate:terms -- --domain=medical

# 보고서 생성
npm run validate:terms -- --report

# Tier S 미달 업그레이드 (AI 자동)
npm run upgrade:terms
```

---

## 용어 추가/수정 워크플로우

```
1. 용어 데이터 작성 (Tier S 기준 준수)
2. npm run validate:terms 실행
3. 90점 이상 확인 → 커밋
4. 90점 미만 → 수정 후 재검증
```

**절대 금지:**
- ❌ Tier S 미달 용어 커밋
- ❌ commonMistakes 문자열 형식 사용
- ❌ meaningKo에 통역 팁 없이 저장
- ❌ 검증 없이 용어 데이터 수정

---

## ⛔ 대량 확장 시 품질 관리 원칙 (필수)

> **배경**: Legal 507→1,000 확장 시 초기 레거시 데이터(100개)와 마감 압박 배치(v9)에서
> 전체 문제의 77%가 발생. 이 원칙은 같은 실수 방지를 위한 것.

### 원칙 1: 확장 전 레거시 검증 (Validate Before Scale)

```
⛔ 금지: 기존 데이터 검증 없이 새 용어 추가 시작
✅ 필수: 도메인 확장 시작 전 기존 데이터 Tier S 검증 → 미달분 먼저 수정
```

- 100개→1,000개 확장 요청 시, **기존 100개부터 Tier S 통과 확인**
- 미달 항목이 있으면 확장 전 업그레이드 우선 실행
- 이유: 초기 데이터는 품질 기준 수립 전에 만들어진 경우가 많음

### 원칙 2: 배치별 즉시 검증 게이트 (Batch Quality Gate)

```
⛔ 금지: 다음 배치 생성 전 현재 배치 검증 건너뛰기
✅ 필수: 매 배치(10개) 실행 후 즉시 검증 스크립트 실행
```

- 스크립트 실행 → **즉시 검증** → 통과 시에만 다음 배치 진행
- 검증 항목 (자동화 필수):
  - meaningKo ≥ 200자
  - meaningVi ≥ 100자
  - culturalNote ≥ 100자
  - commonMistakes: 배열 + 객체 3개+
  - examples: 배열 3개+ + situation 필드
  - slug: 소문자, ASCII, 하이픈만
- **1개라도 미달 → 해당 배치 수정 후 재실행** (다음 배치 진행 금지)

### 원칙 3: 속도보다 품질 (Quality Over Speed)

```
⛔ 금지: "일단 수량 채우고 나중에 품질 올리자"
✅ 필수: 매 용어가 Tier S 통과해야 카운트에 포함
```

- 1,000개 목표라도 Tier S 미달 용어는 "미완성"으로 취급
- 병렬 에이전트 10개 동시 생성은 OK, 단 각각 검증 통과 필수
- 마감 압박 시에도 품질 기준 하향 조정 절대 금지

### 원칙 4: 동음이의어 관리 (Homonym Management)

```
✅ 허용: 같은 korean 값의 다른 법률 개념 (slug/context가 다를 때)
⛔ 금지: 같은 korean + 같은 맥락의 진짜 중복
```

- "조정"(mediation) vs "조정"(adjustment) → ✅ 허용 (다른 slug, 다른 context)
- "가처분"이 2번 → ⛔ 같은 개념이면 삭제
- 동음이의어 허용 시 **slug에 구분 접미사** 권장: `dieu-chinh-hoa-giai` vs `dieu-chinh-dieu-hoa`
- 스크립트에서 korean 중복 감지 시 **context 비교 후 판단**

### 원칙 5: 스크립트 생성 시 필수 포함 사항

```
모든 용어 추가 Python 스크립트는 아래를 반드시 포함:
```

```python
# ⛔ 금지 패턴 (자동 sed 수정 대상이 되면 안 됨)
# - null 사용 → None 사용
# - data['terms'] → data (JSON은 flat array)
# - {"terms": data} 저장 → data 직접 저장

# ✅ 필수 검증 (main 함수 끝에 포함)
for t in filtered:
    assert len(t['meaningKo']) >= 200, f"{t['slug']}: meaningKo {len(t['meaningKo'])}자 < 200자"
    assert len(t['meaningVi']) >= 100, f"{t['slug']}: meaningVi {len(t['meaningVi'])}자 < 100자"
    assert len(t['culturalNote']) >= 100, f"{t['slug']}: culturalNote {len(t['culturalNote'])}자 < 100자"
    assert isinstance(t['commonMistakes'], list) and len(t['commonMistakes']) >= 3
    assert all(isinstance(m, dict) for m in t['commonMistakes'])
    assert isinstance(t['examples'], list) and len(t['examples']) >= 3
    assert all('situation' in e for e in t['examples'])
    assert t['slug'] == t['slug'].lower() and ' ' not in t['slug']
```

### 원칙 6: 커밋 전 전체 도메인 검증

```
⛔ 금지: 부분 검증만으로 커밋
✅ 필수: 커밋 전 전체 JSON에 대해 검증 실행
```

```bash
# 커밋 전 필수 실행
python3 src/scripts/validate-domain.py --domain=legal --strict
# --strict: Tier S 미달 1개라도 있으면 exit 1
```

---

## 도메인별 특수 규칙

### 의료 (medical)
- 질병명: 한/베/영 병기
- 약품명: 성분명 + 상품명 구분
- culturalNote: 한베 의료 시스템 차이 필수

### 법률 (legal)
- 관련 법령 명시
- 양국 법체계 차이 설명
- commonMistakes: 법적 오해 표현 필수

### 건설 (construction)
- 안전 경고 포함
- 단위 환산 정보
- 현장 구어체 병기

### IT (it)
- 약어 풀네임 병기 (예: API - Application Programming Interface)
- 원어 표기 포함

---

## 파일 구조

```
src/data/terms/
├── agriculture.json    # 농업 (100개)
├── automotive.json     # 자동차 (100개)
├── beauty.json         # 뷰티 (100개)
├── construction.json   # 건설 (1,000개)
├── education.json      # 교육 (100개)
├── electronics.json    # 전자 (100개)
├── environment.json    # 환경 (100개)
├── exhibition.json     # 전시 (100개)
├── finance.json        # 금융 (100개)
├── food.json           # 식품 (100개)
├── hr.json             # 인사 (100개)
├── it.json             # IT (100개)
├── legal.json          # 법률 (1,000개)
├── logistics.json      # 물류 (100개)
├── manufacturing.json  # 제조 (100개)
├── medical.json        # 의료 (1,000개)
├── realEstate.json     # 부동산 (100개)
├── textile.json        # 섬유 (100개)
├── tourism.json        # 관광 (100개)
└── trade.json          # 무역 (100개)
```

---

## 참고 문서

- 품질 프레임워크 상세: `docs/specs/2025-02-01-content-quality-framework.md`
- 품질 보고서: `docs/reports/quality-report.json`
