export const runtime = 'edge';


import { NextRequest, NextResponse } from 'next/server';
import { auth } from '@/lib/auth';
import { getD1 } from '@/lib/d1';


interface ReportRow {
  id: string;
  title: string | null;
  status: string;
  template_type: string | null;
  language: string;
  created_at: string;
}

export async function GET(request: NextRequest) {
  try {
    const session = await auth();

    if (!session?.user?.email) {
      return NextResponse.json({ error: '로그인이 필요합니다.' }, { status: 401 });
    }

    const { searchParams } = new URL(request.url);
    const limit = parseInt(searchParams.get('limit') || '20');
    const page = parseInt(searchParams.get('page') || '1');
    const offset = (page - 1) * limit;

    const db = getD1();

    // Get total count
    const countResult = await db.prepare(
      'SELECT COUNT(*) as count FROM phiennoi_reports WHERE user_email = ?'
    ).bind(session.user.email).first<{ count: number }>();

    const count = countResult?.count ?? 0;

    // Get paginated reports
    const { results } = await db.prepare(
      `SELECT id, title, status, template_type, language, created_at
       FROM phiennoi_reports
       WHERE user_email = ?
       ORDER BY created_at DESC
       LIMIT ? OFFSET ?`
    ).bind(session.user.email, limit, offset).all<ReportRow>();

    return NextResponse.json({
      reports: results ?? [],
      total: count,
      page,
      totalPages: Math.ceil(count / limit),
    });
  } catch (error) {
    console.error('Reports fetch error:', error);
    return NextResponse.json({ error: '서버 오류가 발생했습니다.' }, { status: 500 });
  }
}
