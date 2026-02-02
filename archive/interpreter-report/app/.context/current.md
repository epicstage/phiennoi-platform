# Phiennoi 프로젝트 현황 및 계획안
마지막 업데이트: 2026-01-04

---

## 1. 프로젝트 개요

**Phiennoi** - 베트남 통역사를 위한 보고서 자동화 서비스

### 기술 스택
- **프론트엔드**: Next.js 15.5.2, Tailwind CSS v4, lucide-react
- **백엔드**: Cloudflare Pages (Edge Runtime)
- **데이터베이스**: Cloudflare D1
- **스토리지**: Cloudflare R2 (phiennoi-uploads)
- **AI**: Google Gemini 2.0 Flash
- **인증**: Auth.js v5 (NextAuth)

### 배포
- **Production**: https://phiennoi.pages.dev
- **GitHub**: https://github.com/epicstage/phiennoi

---

## 2. 완료된 작업

### 2.1 인프라 마이그레이션 (Supabase → Cloudflare)
- [x] D1 데이터베이스 설정 (phiennoi-db)
- [x] R2 버킷 설정 (phiennoi-uploads, Asia Pacific)
- [x] 모든 API 라우트 Edge Runtime 적용
- [x] wrangler.toml 구성

### 2.2 인증 시스템
- [x] Auth.js v5 설정 (Edge Runtime 호환)
- [x] Google OAuth 연동
  - Client ID/Secret: Cloudflare Secrets에 저장
  - Redirect URI: https://phiennoi.pages.dev/api/auth/callback/google
- [x] 테스트 로그인 제거 (프로덕션 모드)

### 2.3 크레딧 시스템
```
신규 가입: +5 크레딧
프로필 완성: +20 크레딧
추천 코드 사용: +10 크레딧 (양방향)
2단계 추천: +10 크레딧
보고서 생성: -1 크레딧
```

### 2.4 크레딧 충전 기능 (플레이스홀더)
- [x] API: `/api/watch-ad` (GET: 남은 횟수, POST: 지급)
- [x] 대시보드 UI: 모달 + 15초 카운트다운
- [x] 일일 3회 제한, 회당 5크레딧
- [ ] **추후 검토**: SNS 공유, 친구 초대 등으로 대체 가능

---

## 3. 진행 예정 작업

### 3.1 통역사 평가 시스템 (다음 작업)

**목적**: 고객(기업)이 통역사의 서비스 품질을 평가

**설계 방향 (확정 필요)**:
| 항목 | 옵션 |
|------|------|
| 평가 주체 | 고객(기업) → 통역사 |
| 평가 시점 | 보고서 완료 후 / 프로젝트 종료 후 |
| 평가 항목 | 별점(1~5), 텍스트 리뷰 |
| 세부 카테고리 | 정확성, 전문성, 시간준수, 소통능력 등 |
| 결과 활용 | 통역사 프로필에 평점 표시, 랭킹 |

**필요한 DB 테이블**:
```sql
CREATE TABLE phiennoi_reviews (
  id TEXT PRIMARY KEY,
  reviewer_email TEXT NOT NULL,      -- 평가자 (고객)
  interpreter_email TEXT NOT NULL,   -- 피평가자 (통역사)
  report_id TEXT,                    -- 연결된 보고서 (optional)
  rating INTEGER NOT NULL,           -- 1~5
  accuracy INTEGER,                  -- 정확성 1~5
  professionalism INTEGER,           -- 전문성 1~5
  punctuality INTEGER,               -- 시간준수 1~5
  communication INTEGER,             -- 소통능력 1~5
  comment TEXT,                      -- 텍스트 리뷰
  created_at TEXT DEFAULT (datetime('now')),
  FOREIGN KEY (reviewer_email) REFERENCES phiennoi_users(email),
  FOREIGN KEY (interpreter_email) REFERENCES phiennoi_users(email)
);
```

**UI 구성**:
- 보고서 완료 후 평가 요청 배너
- 평가 모달 (별점 + 카테고리별 점수 + 코멘트)
- 통역사 프로필에 평균 평점 표시

---

### 3.2 통역 프로젝트 보기/지원 메뉴

**목적**: 통역사가 새로운 통역 프로젝트를 찾고 지원할 수 있는 마켓플레이스

**기능 설계 (확정 필요)**:
1. **프로젝트 목록 페이지** (`/projects`)
   - 진행 중인 통역 프로젝트 리스트
   - 필터: 지역, 분야, 날짜, 언어쌍

2. **프로젝트 상세 페이지** (`/projects/[id]`)
   - 프로젝트 정보 (일시, 장소, 분야, 요구사항)
   - 지원 버튼

3. **지원 관리** (`/my-applications`)
   - 내가 지원한 프로젝트 목록
   - 상태: 지원완료 / 검토중 / 선정 / 미선정

**필요한 DB 테이블**:
```sql
CREATE TABLE phiennoi_projects (
  id TEXT PRIMARY KEY,
  client_email TEXT NOT NULL,        -- 의뢰자
  title TEXT NOT NULL,
  description TEXT,
  location TEXT,
  date TEXT,
  duration TEXT,
  field TEXT,                        -- 분야 (의료, 법률, 비즈니스 등)
  language_pair TEXT,                -- ko-vi, vi-ko
  budget TEXT,
  status TEXT DEFAULT 'open',        -- open, closed, completed
  created_at TEXT DEFAULT (datetime('now'))
);

CREATE TABLE phiennoi_applications (
  id TEXT PRIMARY KEY,
  project_id TEXT NOT NULL,
  interpreter_email TEXT NOT NULL,
  message TEXT,
  status TEXT DEFAULT 'pending',     -- pending, accepted, rejected
  created_at TEXT DEFAULT (datetime('now')),
  FOREIGN KEY (project_id) REFERENCES phiennoi_projects(id)
);
```

---

### 3.3 Zalo 로그인 구현

**현재 상태**: 로그인 페이지에 "준비중" 표시

**구현 계획**:
1. Zalo Developers에서 앱 생성
2. OAuth 2.0 설정 (Redirect URI)
3. Auth.js에 Zalo Provider 추가
4. 베트남 사용자 대상 주요 로그인 수단

---

## 4. 환경변수 관리

### Cloudflare Pages Secrets (설정됨)
```
AUTH_SECRET         - Auth.js 시크릿
GEMINI_API_KEY      - Google Gemini API
GOOGLE_CLIENT_ID    - Google OAuth
GOOGLE_CLIENT_SECRET - Google OAuth
NEXTAUTH_URL        - https://phiennoi.pages.dev
```

### Admin/.env.local (로컬 백업)
```
PHIENNOI_GOOGLE_CLIENT_ID=86937709360-...
PHIENNOI_GOOGLE_CLIENT_SECRET=GOCSPX-...
```

---

## 5. 파일 구조

```
phiennoi/
├── migrations/
│   └── 0001_init.sql          # D1 스키마
├── src/
│   ├── app/
│   │   ├── api/
│   │   │   ├── auth/[...nextauth]/  # 인증
│   │   │   ├── watch-ad/            # 크레딧 충전
│   │   │   ├── admin/               # 관리자 API
│   │   │   └── ...
│   │   ├── dashboard/         # 대시보드
│   │   ├── login/             # 로그인
│   │   ├── profile/           # 프로필
│   │   ├── report/            # 보고서
│   │   └── ...
│   ├── lib/
│   │   ├── auth.ts            # Auth.js 설정
│   │   └── d1.ts              # D1 헬퍼 함수
│   └── middleware.ts          # 인증 미들웨어
├── wrangler.toml              # Cloudflare 설정
└── .context/                  # 프로젝트 맥락
```

---

## 6. 다음 액션 아이템

1. **통역사 평가 시스템 상세 설계 확정**
   - 평가 항목/카테고리 결정
   - UI 플로우 확정

2. **프로젝트 마켓플레이스 상세 설계**
   - 프로젝트 등록 주체 (관리자? 기업 직접?)
   - 지원 프로세스 확정

3. **Zalo OAuth 설정**
   - Zalo Developers 계정 및 앱 생성

---

## 7. 참고 링크

- Cloudflare Dashboard: https://dash.cloudflare.com
- GitHub Repo: https://github.com/epicstage/phiennoi
- Production: https://phiennoi.pages.dev
