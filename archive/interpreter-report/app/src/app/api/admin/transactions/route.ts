export const runtime = 'edge';


import { NextResponse } from 'next/server';
import { auth } from '@/lib/auth';
import { getD1, CreditTransaction } from '@/lib/d1';


const ADMIN_EMAILS = ['seokheel.kang@gmail.com', 'admin@phiennoi.com'];

export async function GET(request: Request) {
  try {
    const session = await auth();

    if (!session?.user?.email || !ADMIN_EMAILS.includes(session.user.email)) {
      return NextResponse.json({ error: 'Unauthorized' }, { status: 401 });
    }

    const { searchParams } = new URL(request.url);
    const page = parseInt(searchParams.get('page') || '1');
    const limit = parseInt(searchParams.get('limit') || '50');
    const userEmail = searchParams.get('user_email') || '';
    const type = searchParams.get('type') || '';
    const offset = (page - 1) * limit;

    const db = getD1();

    // Build query dynamically
    const conditions: string[] = [];
    const params: (string | number)[] = [];

    if (userEmail) {
      conditions.push('user_email = ?');
      params.push(userEmail);
    }
    if (type) {
      conditions.push('type = ?');
      params.push(type);
    }

    const whereClause = conditions.length > 0 ? `WHERE ${conditions.join(' AND ')}` : '';

    // Get count
    const countResult = await db.prepare(
      `SELECT COUNT(*) as count FROM phiennoi_credit_transactions ${whereClause}`
    ).bind(...params).first<{ count: number }>();

    const count = countResult?.count ?? 0;

    // Get transactions
    const { results } = await db.prepare(
      `SELECT * FROM phiennoi_credit_transactions ${whereClause}
       ORDER BY created_at DESC LIMIT ? OFFSET ?`
    ).bind(...params, limit, offset).all<CreditTransaction>();

    return NextResponse.json({
      transactions: results || [],
      total: count,
      page,
      totalPages: Math.ceil(count / limit),
    });
  } catch (error) {
    console.error('Admin transactions error:', error);
    return NextResponse.json({ error: 'Internal server error' }, { status: 500 });
  }
}
