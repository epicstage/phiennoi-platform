export const runtime = 'edge';

import { NextRequest, NextResponse } from 'next/server';
import { auth } from '@/lib/auth';
import { rewardAdWatch, getAdWatchCountToday, CREDIT_AMOUNTS } from '@/lib/d1';

// GET: 오늘 남은 광고 시청 횟수 조회
export async function GET() {
  try {
    const session = await auth();
    if (!session?.user?.email) {
      return NextResponse.json({ error: '로그인이 필요합니다.' }, { status: 401 });
    }

    const watchedToday = await getAdWatchCountToday(session.user.email);
    const remaining = Math.max(0, CREDIT_AMOUNTS.AD_DAILY_LIMIT - watchedToday);

    return NextResponse.json({
      watchedToday,
      remaining,
      dailyLimit: CREDIT_AMOUNTS.AD_DAILY_LIMIT,
      rewardPerWatch: CREDIT_AMOUNTS.AD_WATCH_REWARD,
    });
  } catch (error) {
    console.error('Watch ad GET error:', error);
    return NextResponse.json({ error: '서버 오류' }, { status: 500 });
  }
}

// POST: 광고 시청 완료 후 크레딧 지급
export async function POST(request: NextRequest) {
  try {
    const session = await auth();
    if (!session?.user?.email) {
      return NextResponse.json({ error: '로그인이 필요합니다.' }, { status: 401 });
    }

    // 광고 시청 검증 (추후 실제 광고 SDK 연동 시 검증 로직 추가)
    // MVP: adToken 검증 생략 (프론트에서 15초 대기 후 호출)
    // 추후: 실제 광고 SDK의 완료 토큰 검증

    const result = await rewardAdWatch(session.user.email);

    if (!result.success) {
      return NextResponse.json({ error: result.message }, { status: 400 });
    }

    return NextResponse.json({
      success: true,
      message: result.message,
      credits: result.credits,
    });
  } catch (error) {
    console.error('Watch ad POST error:', error);
    return NextResponse.json({ error: '서버 오류' }, { status: 500 });
  }
}
