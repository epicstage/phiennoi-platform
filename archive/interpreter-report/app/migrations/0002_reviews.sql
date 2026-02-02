-- Phiennoi D1 Database Schema
-- Migration: 0002_reviews
-- 통역사 평가 시스템 테이블

-- Reviews table (고객이 통역사를 평가)
CREATE TABLE IF NOT EXISTS phiennoi_reviews (
    id TEXT PRIMARY KEY DEFAULT (lower(hex(randomblob(16)))),
    reviewer_email TEXT NOT NULL,           -- 평가자 (고객/기업)
    interpreter_email TEXT NOT NULL,        -- 피평가자 (통역사)
    report_id TEXT,                         -- 연결된 보고서 (optional)
    rating INTEGER NOT NULL CHECK (rating >= 1 AND rating <= 5),  -- 종합 평점 1~5
    accuracy INTEGER CHECK (accuracy >= 1 AND accuracy <= 5),      -- 정확성
    professionalism INTEGER CHECK (professionalism >= 1 AND professionalism <= 5),  -- 전문성
    punctuality INTEGER CHECK (punctuality >= 1 AND punctuality <= 5),  -- 시간준수
    communication INTEGER CHECK (communication >= 1 AND communication <= 5),  -- 소통능력
    comment TEXT,                           -- 텍스트 리뷰
    is_public INTEGER DEFAULT 1,            -- 공개 여부
    created_at TEXT DEFAULT (datetime('now')),
    updated_at TEXT DEFAULT (datetime('now')),
    FOREIGN KEY (reviewer_email) REFERENCES phiennoi_users(email),
    FOREIGN KEY (interpreter_email) REFERENCES phiennoi_users(email),
    FOREIGN KEY (report_id) REFERENCES phiennoi_reports(id)
);

-- 인덱스
CREATE INDEX IF NOT EXISTS idx_reviews_interpreter ON phiennoi_reviews(interpreter_email);
CREATE INDEX IF NOT EXISTS idx_reviews_reviewer ON phiennoi_reviews(reviewer_email);
CREATE INDEX IF NOT EXISTS idx_reviews_report ON phiennoi_reviews(report_id);
CREATE INDEX IF NOT EXISTS idx_reviews_rating ON phiennoi_reviews(rating);
