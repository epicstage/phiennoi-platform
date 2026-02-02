export const runtime = 'edge';


import { NextResponse } from 'next/server';
import { auth } from '@/lib/auth';
import { getD1 } from '@/lib/d1';


const ADMIN_EMAILS = ['seokheel.kang@gmail.com', 'admin@phiennoi.com'];

export async function POST(request: Request) {
  try {
    const session = await auth();

    if (!session?.user?.email || !ADMIN_EMAILS.includes(session.user.email)) {
      return NextResponse.json({ error: 'Unauthorized' }, { status: 401 });
    }

    const { userId, amount, reason } = await request.json() as { userId: string; amount: number; reason: string };

    if (!userId || typeof amount !== 'number' || !reason) {
      return NextResponse.json({ error: 'Invalid request' }, { status: 400 });
    }

    const db = getD1();

    // 현재 크레딧 조회
    const user = await db.prepare(
      'SELECT credits, email FROM phiennoi_users WHERE id = ?'
    ).bind(userId).first<{ credits: number; email: string }>();

    if (!user) {
      return NextResponse.json({ error: 'User not found' }, { status: 404 });
    }

    const newCredits = user.credits + amount;

    if (newCredits < 0) {
      return NextResponse.json({ error: 'Insufficient credits' }, { status: 400 });
    }

    // 크레딧 업데이트
    await db.prepare(
      'UPDATE phiennoi_users SET credits = ?, updated_at = datetime("now") WHERE id = ?'
    ).bind(newCredits, userId).run();

    // 거래 기록
    await db.prepare(`
      INSERT INTO phiennoi_credit_transactions (id, user_email, amount, type, description)
      VALUES (?, ?, ?, ?, ?)
    `).bind(
      crypto.randomUUID(),
      user.email,
      amount,
      amount > 0 ? 'admin_add' : 'admin_deduct',
      `[Admin] ${reason} (by ${session.user.email})`
    ).run();

    return NextResponse.json({ success: true, newCredits });
  } catch (error) {
    console.error('Admin credits error:', error);
    return NextResponse.json({ error: 'Internal server error' }, { status: 500 });
  }
}
