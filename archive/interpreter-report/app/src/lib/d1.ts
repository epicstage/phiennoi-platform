// D1 Database helper functions for Cloudflare Pages
// Replaces Supabase client

import { getRequestContext } from '@cloudflare/next-on-pages';

export const CREDIT_AMOUNTS = {
  SIGNUP_BONUS: 5,
  PROFILE_COMPLETE_BONUS: 20,
  REFERRAL_BONUS: 10,
  REFERRAL_CHAIN_BONUS: 10,
  REPORT_COST: 1,
  AD_WATCH_REWARD: 5,
  AD_DAILY_LIMIT: 3,
} as const;

// Get D1 database from request context
export function getD1(): D1Database {
  const ctx = getRequestContext();
  return (ctx.env as { DB: D1Database }).DB;
}

// Type definitions
export interface User {
  id: string;
  email: string | null;
  name: string | null;
  image: string | null;
  phone: string | null;
  university: string | null;
  major: string | null;
  korean_certificate: string | null;
  experience: string | null;
  region: string | null;
  credits: number;
  profile_completed: number;
  referral_code: string | null;
  referred_by: string | null;
  zalo_id: string | null;
  zalo_verified: number;
  created_at: string;
  updated_at: string;
}

export interface Report {
  id: string;
  user_email: string;
  title: string | null;
  transcript: string | null;
  content: string | null;
  template_type: string | null;
  language: string;
  signature: string | null;
  status: string;
  created_at: string;
  updated_at: string;
}

export interface CreditTransaction {
  id: string;
  user_email: string;
  amount: number;
  type: string;
  description: string | null;
  created_at: string;
}

// User functions
export async function getUserByEmail(email: string): Promise<User | null> {
  const db = getD1();
  const result = await db.prepare(
    'SELECT * FROM phiennoi_users WHERE email = ?'
  ).bind(email).first<User>();
  return result;
}

export async function getUserByZaloId(zaloId: string): Promise<User | null> {
  const db = getD1();
  const result = await db.prepare(
    'SELECT * FROM phiennoi_users WHERE zalo_id = ?'
  ).bind(zaloId).first<User>();
  return result;
}

export async function getUserCredits(email: string): Promise<number> {
  const user = await getUserByEmail(email);
  return user?.credits ?? 0;
}

export async function getOrCreateUser(
  email: string,
  name?: string,
  image?: string
): Promise<User | null> {
  const db = getD1();

  // Check existing
  const existing = await getUserByEmail(email);
  if (existing) return existing;

  // Generate referral code
  const referralCode = email.split('@')[0].toUpperCase().slice(0, 6) +
    Math.random().toString(36).slice(2, 5).toUpperCase();

  // Create new user
  const id = crypto.randomUUID();
  await db.prepare(`
    INSERT INTO phiennoi_users (id, email, name, image, credits, referral_code)
    VALUES (?, ?, ?, ?, ?, ?)
  `).bind(id, email, name ?? null, image ?? null, CREDIT_AMOUNTS.SIGNUP_BONUS, referralCode).run();

  // Record signup bonus
  await db.prepare(`
    INSERT INTO phiennoi_credit_transactions (id, user_email, amount, type, description)
    VALUES (?, ?, ?, 'signup_bonus', '회원가입 보너스')
  `).bind(crypto.randomUUID(), email, CREDIT_AMOUNTS.SIGNUP_BONUS).run();

  return getUserByEmail(email);
}

export async function getOrCreateZaloUser(
  zaloId: string,
  name?: string,
  image?: string
): Promise<User | null> {
  const db = getD1();

  // Check existing
  const existing = await getUserByZaloId(zaloId);
  if (existing) return existing;

  // Generate referral code
  const referralCode = 'ZL' + zaloId.slice(-4).toUpperCase() +
    Math.random().toString(36).slice(2, 5).toUpperCase();

  // Create new user
  const id = crypto.randomUUID();
  await db.prepare(`
    INSERT INTO phiennoi_users (id, zalo_id, name, image, credits, referral_code, zalo_verified)
    VALUES (?, ?, ?, ?, ?, ?, 1)
  `).bind(id, zaloId, name ?? null, image ?? null, CREDIT_AMOUNTS.SIGNUP_BONUS, referralCode).run();

  // Record signup bonus
  await db.prepare(`
    INSERT INTO phiennoi_credit_transactions (id, user_email, amount, type, description)
    VALUES (?, ?, ?, 'signup_bonus', '회원가입 보너스 (Zalo)')
  `).bind(crypto.randomUUID(), `zalo:${zaloId}`, CREDIT_AMOUNTS.SIGNUP_BONUS).run();

  return getUserByZaloId(zaloId);
}

export async function deductCredit(email: string, description: string): Promise<boolean> {
  const db = getD1();

  const user = await getUserByEmail(email);
  if (!user || user.credits < CREDIT_AMOUNTS.REPORT_COST) {
    return false;
  }

  // Deduct credit
  await db.prepare(
    'UPDATE phiennoi_users SET credits = credits - ?, updated_at = datetime("now") WHERE email = ?'
  ).bind(CREDIT_AMOUNTS.REPORT_COST, email).run();

  // Record transaction
  await db.prepare(`
    INSERT INTO phiennoi_credit_transactions (id, user_email, amount, type, description)
    VALUES (?, ?, ?, 'use', ?)
  `).bind(crypto.randomUUID(), email, -CREDIT_AMOUNTS.REPORT_COST, description).run();

  return true;
}

export async function addCredits(
  email: string,
  amount: number,
  type: 'earn' | 'purchase' | 'referral' | 'profile_bonus' | 'signup_bonus',
  description: string
): Promise<boolean> {
  const db = getD1();

  const user = await getUserByEmail(email);
  if (!user) return false;

  await db.prepare(
    'UPDATE phiennoi_users SET credits = credits + ?, updated_at = datetime("now") WHERE email = ?'
  ).bind(amount, email).run();

  await db.prepare(`
    INSERT INTO phiennoi_credit_transactions (id, user_email, amount, type, description)
    VALUES (?, ?, ?, ?, ?)
  `).bind(crypto.randomUUID(), email, amount, type, description).run();

  return true;
}

export async function completeProfile(
  email: string,
  profileData: {
    phone: string;
    university: string;
    major: string;
    korean_certificate: string;
    experience: string;
    region: string;
  }
): Promise<boolean> {
  const db = getD1();

  const user = await getUserByEmail(email);
  if (!user) return false;
  if (user.profile_completed) return true;

  await db.prepare(`
    UPDATE phiennoi_users SET
      phone = ?, university = ?, major = ?,
      korean_certificate = ?, experience = ?, region = ?,
      profile_completed = 1,
      credits = credits + ?,
      updated_at = datetime('now')
    WHERE email = ?
  `).bind(
    profileData.phone,
    profileData.university,
    profileData.major,
    profileData.korean_certificate,
    profileData.experience,
    profileData.region,
    CREDIT_AMOUNTS.PROFILE_COMPLETE_BONUS,
    email
  ).run();

  await db.prepare(`
    INSERT INTO phiennoi_credit_transactions (id, user_email, amount, type, description)
    VALUES (?, ?, ?, 'profile_bonus', '프로필 완성 보너스')
  `).bind(crypto.randomUUID(), email, CREDIT_AMOUNTS.PROFILE_COMPLETE_BONUS).run();

  return true;
}

export async function applyReferralCode(
  email: string,
  referralCode: string
): Promise<{ success: boolean; message: string }> {
  const db = getD1();

  // Find referrer
  const referrer = await db.prepare(
    'SELECT email, referred_by FROM phiennoi_users WHERE referral_code = ?'
  ).bind(referralCode.toUpperCase()).first<{ email: string; referred_by: string | null }>();

  if (!referrer) {
    return { success: false, message: '유효하지 않은 추천 코드입니다.' };
  }

  const user = await getUserByEmail(email);
  if (!user) {
    return { success: false, message: '사용자를 찾을 수 없습니다.' };
  }

  if (user.referred_by) {
    return { success: false, message: '이미 추천 코드를 사용하셨습니다.' };
  }

  if (referrer.email === email) {
    return { success: false, message: '자신의 추천 코드는 사용할 수 없습니다.' };
  }

  // Update user
  await db.prepare(
    'UPDATE phiennoi_users SET referred_by = ?, updated_at = datetime("now") WHERE email = ?'
  ).bind(referrer.email, email).run();

  // Add credits to both
  await addCredits(email, CREDIT_AMOUNTS.REFERRAL_BONUS, 'referral', '추천 코드 사용 보너스');
  await addCredits(referrer.email, CREDIT_AMOUNTS.REFERRAL_BONUS, 'referral', '친구 추천 보너스');

  // 2-tier referral
  if (referrer.referred_by) {
    await addCredits(
      referrer.referred_by,
      CREDIT_AMOUNTS.REFERRAL_CHAIN_BONUS,
      'referral',
      '2단계 추천 보너스'
    );
  }

  return { success: true, message: `${CREDIT_AMOUNTS.REFERRAL_BONUS} 크레딧이 지급되었습니다!` };
}

// Report functions
export async function createReport(
  userEmail: string,
  data: {
    title?: string;
    transcript?: string;
    content?: object;
    template_type?: string;
    language?: string;
  }
): Promise<Report | null> {
  const db = getD1();
  const id = crypto.randomUUID();

  await db.prepare(`
    INSERT INTO phiennoi_reports (id, user_email, title, transcript, content, template_type, language)
    VALUES (?, ?, ?, ?, ?, ?, ?)
  `).bind(
    id,
    userEmail,
    data.title ?? null,
    data.transcript ?? null,
    data.content ? JSON.stringify(data.content) : null,
    data.template_type ?? null,
    data.language ?? 'ko'
  ).run();

  return getReportById(id);
}

export async function getReportById(id: string): Promise<Report | null> {
  const db = getD1();
  return db.prepare('SELECT * FROM phiennoi_reports WHERE id = ?')
    .bind(id).first<Report>();
}

export async function getUserReports(email: string): Promise<Report[]> {
  const db = getD1();
  const { results } = await db.prepare(
    'SELECT * FROM phiennoi_reports WHERE user_email = ? ORDER BY created_at DESC'
  ).bind(email).all<Report>();
  return results ?? [];
}

export async function updateReport(
  id: string,
  data: Partial<{
    title: string;
    transcript: string;
    content: object;
    signature: string;
    status: string;
  }>
): Promise<boolean> {
  const db = getD1();

  const updates: string[] = [];
  const values: (string | null)[] = [];

  if (data.title !== undefined) {
    updates.push('title = ?');
    values.push(data.title);
  }
  if (data.transcript !== undefined) {
    updates.push('transcript = ?');
    values.push(data.transcript);
  }
  if (data.content !== undefined) {
    updates.push('content = ?');
    values.push(JSON.stringify(data.content));
  }
  if (data.signature !== undefined) {
    updates.push('signature = ?');
    values.push(data.signature);
  }
  if (data.status !== undefined) {
    updates.push('status = ?');
    values.push(data.status);
  }

  if (updates.length === 0) return false;

  updates.push('updated_at = datetime("now")');
  values.push(id);

  await db.prepare(
    `UPDATE phiennoi_reports SET ${updates.join(', ')} WHERE id = ?`
  ).bind(...values).run();

  return true;
}

// Ad watch functions
export async function getAdWatchCountToday(email: string): Promise<number> {
  const db = getD1();
  const today = new Date().toISOString().split('T')[0];

  const result = await db.prepare(`
    SELECT COUNT(*) as count FROM phiennoi_credit_transactions
    WHERE user_email = ? AND type = 'ad_watch' AND date(created_at) = ?
  `).bind(email, today).first<{ count: number }>();

  return result?.count || 0;
}

export async function rewardAdWatch(email: string): Promise<{ success: boolean; message: string; credits?: number }> {
  const db = getD1();

  // Check daily limit
  const watchCount = await getAdWatchCountToday(email);
  if (watchCount >= CREDIT_AMOUNTS.AD_DAILY_LIMIT) {
    return {
      success: false,
      message: `오늘 광고 시청 한도(${CREDIT_AMOUNTS.AD_DAILY_LIMIT}회)에 도달했습니다. 내일 다시 시도해주세요.`
    };
  }

  // Add credits
  await db.prepare(
    'UPDATE phiennoi_users SET credits = credits + ?, updated_at = datetime("now") WHERE email = ?'
  ).bind(CREDIT_AMOUNTS.AD_WATCH_REWARD, email).run();

  // Record transaction
  await db.prepare(`
    INSERT INTO phiennoi_credit_transactions (id, user_email, amount, type, description)
    VALUES (?, ?, ?, 'ad_watch', '광고 시청 보상')
  `).bind(crypto.randomUUID(), email, CREDIT_AMOUNTS.AD_WATCH_REWARD).run();

  const user = await getUserByEmail(email);

  return {
    success: true,
    message: `${CREDIT_AMOUNTS.AD_WATCH_REWARD} 크레딧이 지급되었습니다!`,
    credits: user?.credits || 0
  };
}
