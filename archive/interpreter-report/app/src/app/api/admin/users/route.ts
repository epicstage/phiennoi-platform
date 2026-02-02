export const runtime = 'edge';


import { NextResponse } from 'next/server';
import { auth } from '@/lib/auth';
import { getD1 } from '@/lib/d1';


const ADMIN_EMAILS = ['seokheel.kang@gmail.com', 'admin@phiennoi.com'];

interface UserRow {
  id: string;
  email: string | null;
  name: string | null;
  credits: number;
  profile_completed: number;
  created_at: string;
}

export async function GET() {
  try {
    const session = await auth();

    if (!session?.user?.email || !ADMIN_EMAILS.includes(session.user.email)) {
      return NextResponse.json({ error: 'Unauthorized' }, { status: 401 });
    }

    const db = getD1();

    const { results } = await db.prepare(
      `SELECT id, email, name, credits, profile_completed, created_at
       FROM phiennoi_users
       ORDER BY created_at DESC
       LIMIT 100`
    ).all<UserRow>();

    return NextResponse.json({ users: results || [] });
  } catch (error) {
    console.error('Admin users error:', error);
    return NextResponse.json({ error: 'Internal server error' }, { status: 500 });
  }
}
