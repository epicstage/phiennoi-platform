export const runtime = 'edge';


import { NextRequest, NextResponse } from 'next/server';
import { auth } from '@/lib/auth';
import { getD1, Report } from '@/lib/d1';


export async function GET(
  request: NextRequest,
  { params }: { params: Promise<{ id: string }> }
) {
  try {
    const session = await auth();

    if (!session?.user?.email) {
      return NextResponse.json({ error: '로그인이 필요합니다.' }, { status: 401 });
    }

    const { id } = await params;
    const db = getD1();

    const report = await db.prepare(
      'SELECT * FROM phiennoi_reports WHERE id = ? AND user_email = ?'
    ).bind(id, session.user.email).first<Report>();

    if (!report) {
      return NextResponse.json({ error: '보고서를 찾을 수 없습니다.' }, { status: 404 });
    }

    // Parse content JSON if it's a string
    const parsedReport = {
      ...report,
      content: report.content ? JSON.parse(report.content) : null,
    };

    return NextResponse.json({ report: parsedReport });
  } catch (error) {
    console.error('Report fetch error:', error);
    return NextResponse.json({ error: '서버 오류가 발생했습니다.' }, { status: 500 });
  }
}

export async function DELETE(
  request: NextRequest,
  { params }: { params: Promise<{ id: string }> }
) {
  try {
    const session = await auth();

    if (!session?.user?.email) {
      return NextResponse.json({ error: '로그인이 필요합니다.' }, { status: 401 });
    }

    const { id } = await params;
    const db = getD1();

    await db.prepare(
      'DELETE FROM phiennoi_reports WHERE id = ? AND user_email = ?'
    ).bind(id, session.user.email).run();

    return NextResponse.json({ success: true });
  } catch (error) {
    console.error('Report delete error:', error);
    return NextResponse.json({ error: '서버 오류가 발생했습니다.' }, { status: 500 });
  }
}
