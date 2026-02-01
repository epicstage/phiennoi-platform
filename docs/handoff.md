# 세션 핸드오프

> 생성: 2026-02-01
> 프로젝트: Epic Note - 베트남 통역 플랫폼 (vn.epicstage.co.kr)

## 📌 현재 상태
- 진행 중인 작업: 신규 6개 도메인 용어 생성
- 완료율: 77% (기존 작업 완료, 도메인 확장만 남음)
- 마지막 작업: 백그라운드 에이전트 4회 시도 → 세션 끊김으로 소실

## ✅ 이전 세션에서 완료한 것

### 용어 확장 (완료)
- **20개 도메인, 2,003개 용어** 달성
- 기존 12개 → 20개 도메인 확장
- 도메인당 100개 목표 달성

### 이미지 (완료)
- **621개 Ideogram 이미지** 생성
- 예산 ~$25 사용
- 일부 누락 용어는 유사 이미지 재사용

### 박람회 자동화 (완료)
- `.github/workflows/exhibition-content.yml` - 주간 자동 실행
- `scripts/generate-exhibition-content.js` - 박람회 콘텐츠 생성 스크립트
- 전략: 베트남 출장 준비하는 한국인 대상 SEO 콘텐츠

## 🎯 다음 세션에서 할 일

### 1순위: 신규 6개 도메인 생성 (필수)
**⚠️ 백그라운드 에이전트 사용 금지 - 순차 직접 생성 권장**

| 도메인 | 목표 | 설명 |
|--------|------|------|
| golf | 100개 | 베트남 골프 관광 |
| cosmetics | 100개 | K-뷰티 |
| plasticSurgery | 100개 | 의료관광 |
| fnb | 100개 | F&B/프랜차이즈 |
| semiconductor | 100개 | 삼성/인텔 베트남 |
| furniture | 100개 | HAWAEXPO 가구 박람회 |

### 2순위: 신규 도메인 이미지 (선택)
- Ideogram 잔액 확인 후 진행

### 3순위: GitHub Actions 테스트
- `exhibition-content.yml` 수동 실행 테스트

## 🔑 핵심 맥락
- **기존 완료**: 20개 도메인, 2,003개 용어, 621개 이미지
- **박람회 전략**: 도메인 확장용이 아닌 SEO 콘텐츠 전략
- **빌드**: Next.js 16.1.6, Vercel 배포
- **Ideogram 잔액**: ~$6-7 남음

## 📁 참조 파일
- `src/data/terms/*.json` - 20개 도메인 용어 파일
- `public/images/terms/` - 621개 Ideogram 이미지
- `.github/workflows/exhibition-content.yml` - 주간 박람회 자동화
- `scripts/generate-exhibition-content.js` - 박람회 콘텐츠 생성
- `scripts/generate-term-images-ideogram.mjs` - Ideogram 이미지 생성

## ⚠️ 주의사항
- **백그라운드 에이전트 4회 시도 모두 실패** - 세션 끊기면 작업 소실됨
- 신규 도메인은 **포그라운드에서 순차 직접 생성** 권장
- 용어 스키마는 기존 파일 참조

## 📋 용어 스키마 (신규 도메인 생성 시 참조)
```json
{
  "slug": "english-slug",
  "korean": "한국어",
  "vietnamese": "tiếng Việt",
  "hanja": "",
  "hanjaReading": "",
  "termType": "word|compound|abbreviation",
  "meaningKo": "150자 이상 한국어 설명",
  "meaningVi": "100자 이상 베트남어 설명",
  "pronunciation": "발음 가이드",
  "commonMistakes": ["실수1"],
  "culturalNote": "문화적 맥락",
  "context": "사용 맥락",
  "examples": [{"ko": "예문", "vi": "example", "situation": "formal"}],
  "relatedTerms": ["related-slug"],
  "difficulty": "beginner|intermediate|advanced",
  "frequency": 1-5,
  "formalLevel": "formal|neutral|informal"
}
```

## 💬 마지막 대화 요약
1. 신규 6개 도메인 생성 시도 4회 → 모두 세션 끊김으로 소실
2. 백그라운드 에이전트 대신 포그라운드 순차 생성 제안
3. 사용자가 새 세션에서 작업하기로 결정
