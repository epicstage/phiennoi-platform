export const runtime = 'edge';


import { NextResponse } from 'next/server';
import { auth } from '@/lib/auth';
import { getUserByEmail } from '@/lib/d1';


export async function GET() {
  try {
    const session = await auth();

    if (!session?.user?.email) {
      return NextResponse.json({ error: '로그인이 필요합니다.' }, { status: 401 });
    }

    const user = await getUserByEmail(session.user.email);

    if (!user) {
      return NextResponse.json({ error: '사용자를 찾을 수 없습니다.' }, { status: 404 });
    }

    return NextResponse.json({
      id: user.id,
      email: user.email,
      name: user.name,
      image: user.image,
      phone: user.phone,
      university: user.university,
      major: user.major,
      koreanCertificate: user.korean_certificate,
      experience: user.experience,
      region: user.region,
      credits: user.credits,
      profileCompleted: !!user.profile_completed,
      referralCode: user.referral_code,
      referredBy: user.referred_by,
      createdAt: user.created_at,
    });
  } catch (error) {
    console.error('User fetch error:', error);
    return NextResponse.json({ error: '서버 오류가 발생했습니다.' }, { status: 500 });
  }
}
