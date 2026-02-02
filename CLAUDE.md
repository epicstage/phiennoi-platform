# Phiennoi Platform - 한베 통역 전문용어 플랫폼

> 전역 에피 시스템 규칙: `~/.claude/CLAUDE.md`
> 이 파일: 프로젝트 고유 규칙 (품질 기준 등)

---

## 프로젝트 정보

- **이름**: Phiennoi Platform (vn.epicstage.co.kr)
- **목적**: 한국어-베트남어 통역사를 위한 전문용어 학습 플랫폼
- **핵심 자산**: 20개 도메인 × 100개 용어 = 2,000개 전문용어 DB

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
├── construction.json   # 건설 (100개)
├── education.json      # 교육 (100개)
├── electronics.json    # 전자 (100개)
├── environment.json    # 환경 (100개)
├── exhibition.json     # 전시 (100개)
├── finance.json        # 금융 (100개)
├── food.json           # 식품 (100개)
├── hr.json             # 인사 (100개)
├── it.json             # IT (100개)
├── legal.json          # 법률 (100개)
├── logistics.json      # 물류 (100개)
├── manufacturing.json  # 제조 (100개)
├── medical.json        # 의료 (100개)
├── realEstate.json     # 부동산 (100개)
├── textile.json        # 섬유 (100개)
├── tourism.json        # 관광 (100개)
└── trade.json          # 무역 (100개)
```

---

## 참고 문서

- 품질 프레임워크 상세: `docs/specs/2025-02-01-content-quality-framework.md`
- 품질 보고서: `docs/reports/quality-report.json`
