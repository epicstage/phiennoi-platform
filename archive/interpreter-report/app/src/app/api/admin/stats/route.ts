export const runtime = 'edge';


import { NextResponse } from 'next/server';
import { auth } from '@/lib/auth';
import { getD1 } from '@/lib/d1';


const ADMIN_EMAILS = ['seokheel.kang@gmail.com', 'admin@phiennoi.com'];

export async function GET() {
  try {
    const session = await auth();

    if (!session?.user?.email || !ADMIN_EMAILS.includes(session.user.email)) {
      return NextResponse.json({ error: 'Unauthorized' }, { status: 401 });
    }

    const db = getD1();

    // 총 회원 수
    const usersCount = await db.prepare(
      'SELECT COUNT(*) as count FROM phiennoi_users'
    ).first<{ count: number }>();

    // 총 보고서 수
    const reportsCount = await db.prepare(
      'SELECT COUNT(*) as count FROM phiennoi_reports'
    ).first<{ count: number }>();

    // 사용된 크레딧 합계
    const creditsUsed = await db.prepare(
      'SELECT SUM(ABS(amount)) as total FROM phiennoi_credit_transactions WHERE amount < 0'
    ).first<{ total: number }>();

    // 오늘 가입자 수
    const todaySignupsCount = await db.prepare(
      `SELECT COUNT(*) as count FROM phiennoi_users
       WHERE created_at >= date('now', 'start of day')`
    ).first<{ count: number }>();

    return NextResponse.json({
      totalUsers: usersCount?.count || 0,
      totalReports: reportsCount?.count || 0,
      totalCreditsUsed: creditsUsed?.total || 0,
      todaySignups: todaySignupsCount?.count || 0,
    });
  } catch (error) {
    console.error('Admin stats error:', error);
    return NextResponse.json({ error: 'Internal server error' }, { status: 500 });
  }
}
