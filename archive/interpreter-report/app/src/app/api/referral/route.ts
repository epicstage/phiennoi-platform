export const runtime = 'edge';


import { NextRequest, NextResponse } from 'next/server';
import { auth } from '@/lib/auth';
import { applyReferralCode } from '@/lib/d1';


export async function POST(request: NextRequest) {
  try {
    const session = await auth();

    if (!session?.user?.email) {
      return NextResponse.json({ error: '로그인이 필요합니다.' }, { status: 401 });
    }

    const body = await request.json() as { code?: string; referralCode?: string };
    const code = body.code || body.referralCode;

    if (!code) {
      return NextResponse.json({ error: '추천 코드를 입력해주세요.' }, { status: 400 });
    }

    const result = await applyReferralCode(session.user.email, code);

    if (!result.success) {
      return NextResponse.json({ error: result.message }, { status: 400 });
    }

    return NextResponse.json({ success: true, message: result.message });
  } catch (error) {
    console.error('Referral error:', error);
    return NextResponse.json({ error: '서버 오류가 발생했습니다.' }, { status: 500 });
  }
}
