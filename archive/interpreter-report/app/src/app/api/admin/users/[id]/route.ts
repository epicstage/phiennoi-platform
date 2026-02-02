export const runtime = 'edge';


import { NextResponse } from 'next/server';
import { auth } from '@/lib/auth';
import { getD1, User, Report, CreditTransaction } from '@/lib/d1';


const ADMIN_EMAILS = ['seokheel.kang@gmail.com', 'admin@phiennoi.com'];

export async function GET(
  request: Request,
  { params }: { params: Promise<{ id: string }> }
) {
  try {
    const session = await auth();

    if (!session?.user?.email || !ADMIN_EMAILS.includes(session.user.email)) {
      return NextResponse.json({ error: 'Unauthorized' }, { status: 401 });
    }

    const { id } = await params;
    const db = getD1();

    // 사용자 정보
    const user = await db.prepare(
      'SELECT * FROM phiennoi_users WHERE id = ?'
    ).bind(id).first<User>();

    if (!user) {
      return NextResponse.json({ error: 'User not found' }, { status: 404 });
    }

    // 사용자의 보고서
    const { results: reports } = await db.prepare(
      `SELECT id, title, status, created_at
       FROM phiennoi_reports
       WHERE user_email = ?
       ORDER BY created_at DESC
       LIMIT 10`
    ).bind(user.email).all<Report>();

    // 사용자의 크레딧 거래 내역
    const { results: transactions } = await db.prepare(
      `SELECT * FROM phiennoi_credit_transactions
       WHERE user_email = ?
       ORDER BY created_at DESC
       LIMIT 20`
    ).bind(user.email).all<CreditTransaction>();

    return NextResponse.json({
      user,
      reports: reports || [],
      transactions: transactions || [],
    });
  } catch (error) {
    console.error('Admin user detail error:', error);
    return NextResponse.json({ error: 'Internal server error' }, { status: 500 });
  }
}

export async function PATCH(
  request: Request,
  { params }: { params: Promise<{ id: string }> }
) {
  try {
    const session = await auth();

    if (!session?.user?.email || !ADMIN_EMAILS.includes(session.user.email)) {
      return NextResponse.json({ error: 'Unauthorized' }, { status: 401 });
    }

    const { id } = await params;
    const updates = await request.json() as Record<string, string | number>;
    const db = getD1();

    // 허용된 필드만 업데이트
    const allowedFields = ['name', 'credits', 'profile_completed'];
    const setClauses: string[] = [];
    const values: (string | number)[] = [];

    for (const field of allowedFields) {
      if (updates[field] !== undefined) {
        setClauses.push(`${field} = ?`);
        values.push(updates[field]);
      }
    }

    if (setClauses.length === 0) {
      return NextResponse.json({ error: 'No valid fields to update' }, { status: 400 });
    }

    setClauses.push('updated_at = datetime("now")');
    values.push(id);

    await db.prepare(
      `UPDATE phiennoi_users SET ${setClauses.join(', ')} WHERE id = ?`
    ).bind(...values).run();

    return NextResponse.json({ success: true });
  } catch (error) {
    console.error('Admin user update error:', error);
    return NextResponse.json({ error: 'Internal server error' }, { status: 500 });
  }
}

export async function DELETE(
  request: Request,
  { params }: { params: Promise<{ id: string }> }
) {
  try {
    const session = await auth();

    if (!session?.user?.email || !ADMIN_EMAILS.includes(session.user.email)) {
      return NextResponse.json({ error: 'Unauthorized' }, { status: 401 });
    }

    const { id } = await params;
    const db = getD1();

    // 사용자 삭제
    await db.prepare('DELETE FROM phiennoi_users WHERE id = ?').bind(id).run();

    return NextResponse.json({ success: true });
  } catch (error) {
    console.error('Admin user delete error:', error);
    return NextResponse.json({ error: 'Internal server error' }, { status: 500 });
  }
}
