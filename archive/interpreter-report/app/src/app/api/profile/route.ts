export const runtime = 'edge';


import { NextRequest, NextResponse } from 'next/server';
import { auth } from '@/lib/auth';
import { completeProfile } from '@/lib/d1';


export async function POST(request: NextRequest) {
  try {
    const session = await auth();

    if (!session?.user?.email) {
      return NextResponse.json({ error: '로그인이 필요합니다.' }, { status: 401 });
    }

    const body = await request.json() as {
      phone: string;
      university: string;
      major: string;
      koreanCertificate: string;
      experience: string;
      region: string;
    };
    const { phone, university, major, koreanCertificate, experience, region } = body;

    // Validate required fields
    if (!phone || !university || !major || !koreanCertificate || !experience || !region) {
      return NextResponse.json({ error: '모든 필드를 입력해주세요.' }, { status: 400 });
    }

    const success = await completeProfile(session.user.email, {
      phone,
      university,
      major,
      korean_certificate: koreanCertificate,
      experience,
      region,
    });

    if (!success) {
      return NextResponse.json({ error: '프로필 업데이트에 실패했습니다.' }, { status: 500 });
    }

    return NextResponse.json({ success: true, message: '프로필이 완성되었습니다! +20 크레딧 지급!' });
  } catch (error) {
    console.error('Profile update error:', error);
    return NextResponse.json({ error: '서버 오류가 발생했습니다.' }, { status: 500 });
  }
}
