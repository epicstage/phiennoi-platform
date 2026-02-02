-- Phiennoi D1 Database Schema
-- Migration: 0001_init

-- Users table
CREATE TABLE IF NOT EXISTS phiennoi_users (
    id TEXT PRIMARY KEY DEFAULT (lower(hex(randomblob(16)))),
    email TEXT UNIQUE,
    name TEXT,
    image TEXT,
    phone TEXT,
    university TEXT,
    major TEXT,
    korean_certificate TEXT,
    experience TEXT,
    region TEXT,
    credits INTEGER DEFAULT 5,
    profile_completed INTEGER DEFAULT 0,
    referral_code TEXT UNIQUE,
    referred_by TEXT,
    zalo_id TEXT UNIQUE,
    zalo_verified INTEGER DEFAULT 0,
    created_at TEXT DEFAULT (datetime('now')),
    updated_at TEXT DEFAULT (datetime('now'))
);

-- Index for faster lookups
CREATE INDEX IF NOT EXISTS idx_users_email ON phiennoi_users(email);
CREATE INDEX IF NOT EXISTS idx_users_zalo_id ON phiennoi_users(zalo_id);
CREATE INDEX IF NOT EXISTS idx_users_referral_code ON phiennoi_users(referral_code);

-- Reports table
CREATE TABLE IF NOT EXISTS phiennoi_reports (
    id TEXT PRIMARY KEY DEFAULT (lower(hex(randomblob(16)))),
    user_email TEXT NOT NULL,
    title TEXT,
    transcript TEXT,
    content TEXT, -- JSON stored as text
    template_type TEXT,
    language TEXT DEFAULT 'ko',
    signature TEXT,
    status TEXT DEFAULT 'draft',
    created_at TEXT DEFAULT (datetime('now')),
    updated_at TEXT DEFAULT (datetime('now')),
    FOREIGN KEY (user_email) REFERENCES phiennoi_users(email)
);

CREATE INDEX IF NOT EXISTS idx_reports_user ON phiennoi_reports(user_email);
CREATE INDEX IF NOT EXISTS idx_reports_status ON phiennoi_reports(status);

-- Credit transactions table
CREATE TABLE IF NOT EXISTS phiennoi_credit_transactions (
    id TEXT PRIMARY KEY DEFAULT (lower(hex(randomblob(16)))),
    user_email TEXT NOT NULL,
    amount INTEGER NOT NULL,
    type TEXT NOT NULL, -- 'use', 'earn', 'purchase', 'referral', 'profile_bonus', 'signup_bonus'
    description TEXT,
    created_at TEXT DEFAULT (datetime('now')),
    FOREIGN KEY (user_email) REFERENCES phiennoi_users(email)
);

CREATE INDEX IF NOT EXISTS idx_transactions_user ON phiennoi_credit_transactions(user_email);
CREATE INDEX IF NOT EXISTS idx_transactions_type ON phiennoi_credit_transactions(type);
