-- 한베통역 플랫폼 - Supabase 마이그레이션
-- interpreters 테이블: 통역사 이력서 등록 정보

CREATE TABLE IF NOT EXISTS interpreters (
  id UUID DEFAULT gen_random_uuid() PRIMARY KEY,
  name TEXT NOT NULL,
  email TEXT NOT NULL,
  phone TEXT NOT NULL,
  location TEXT,
  domains TEXT[] DEFAULT '{}',
  resume_url TEXT,
  status TEXT DEFAULT 'pending' CHECK (status IN ('pending', 'approved', 'rejected')),
  created_at TIMESTAMPTZ DEFAULT NOW(),
  updated_at TIMESTAMPTZ DEFAULT NOW()
);

-- 인덱스
CREATE INDEX idx_interpreters_email ON interpreters(email);
CREATE INDEX idx_interpreters_status ON interpreters(status);
CREATE INDEX idx_interpreters_created ON interpreters(created_at DESC);

-- RLS 활성화
ALTER TABLE interpreters ENABLE ROW LEVEL SECURITY;

-- 정책: 서비스 역할만 접근 (API route에서 service role key 사용)
CREATE POLICY "Service role full access" ON interpreters
  FOR ALL
  USING (auth.role() = 'service_role');

-- Storage bucket for resumes
INSERT INTO storage.buckets (id, name, public)
VALUES ('uploads', 'uploads', true)
ON CONFLICT (id) DO NOTHING;

-- Storage policy: 누구나 업로드 가능 (API route 경유)
CREATE POLICY "Allow public uploads" ON storage.objects
  FOR INSERT
  WITH CHECK (bucket_id = 'uploads');

CREATE POLICY "Allow public read" ON storage.objects
  FOR SELECT
  USING (bucket_id = 'uploads');
