export const runtime = 'edge';


import { NextResponse } from 'next/server';
import { auth } from '@/lib/auth';
import { getD1 } from '@/lib/d1';


const ADMIN_EMAILS = ['seokheel.kang@gmail.com', 'admin@phiennoi.com'];

interface ReportRow {
  id: string;
  title: string | null;
  user_email: string;
  status: string;
  language: string;
  created_at: string;
}

export async function GET(request: Request) {
  try {
    const session = await auth();

    if (!session?.user?.email || !ADMIN_EMAILS.includes(session.user.email)) {
      return NextResponse.json({ error: 'Unauthorized' }, { status: 401 });
    }

    const { searchParams } = new URL(request.url);
    const page = parseInt(searchParams.get('page') || '1');
    const limit = parseInt(searchParams.get('limit') || '20');
    const search = searchParams.get('search') || '';
    const offset = (page - 1) * limit;

    const db = getD1();

    // Get count
    let countQuery = 'SELECT COUNT(*) as count FROM phiennoi_reports';
    if (search) {
      countQuery += ` WHERE title LIKE ? OR user_email LIKE ?`;
    }

    const countResult = search
      ? await db.prepare(countQuery).bind(`%${search}%`, `%${search}%`).first<{ count: number }>()
      : await db.prepare(countQuery).first<{ count: number }>();

    const count = countResult?.count ?? 0;

    // Get reports
    let dataQuery = `SELECT id, title, user_email, status, language, created_at
                     FROM phiennoi_reports`;
    if (search) {
      dataQuery += ` WHERE title LIKE ? OR user_email LIKE ?`;
    }
    dataQuery += ` ORDER BY created_at DESC LIMIT ? OFFSET ?`;

    const { results } = search
      ? await db.prepare(dataQuery).bind(`%${search}%`, `%${search}%`, limit, offset).all<ReportRow>()
      : await db.prepare(dataQuery).bind(limit, offset).all<ReportRow>();

    return NextResponse.json({
      reports: results || [],
      total: count,
      page,
      totalPages: Math.ceil(count / limit),
    });
  } catch (error) {
    console.error('Admin reports error:', error);
    return NextResponse.json({ error: 'Internal server error' }, { status: 500 });
  }
}

export async function DELETE(request: Request) {
  try {
    const session = await auth();

    if (!session?.user?.email || !ADMIN_EMAILS.includes(session.user.email)) {
      return NextResponse.json({ error: 'Unauthorized' }, { status: 401 });
    }

    const { reportId } = await request.json() as { reportId: string };

    if (!reportId) {
      return NextResponse.json({ error: 'Report ID required' }, { status: 400 });
    }

    const db = getD1();
    await db.prepare('DELETE FROM phiennoi_reports WHERE id = ?').bind(reportId).run();

    return NextResponse.json({ success: true });
  } catch (error) {
    console.error('Admin delete report error:', error);
    return NextResponse.json({ error: 'Internal server error' }, { status: 500 });
  }
}
