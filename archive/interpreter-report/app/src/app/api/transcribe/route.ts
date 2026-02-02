export const runtime = 'edge';


import { NextRequest, NextResponse } from 'next/server';
import { auth } from '@/lib/auth';
import { getD1, deductCredit } from '@/lib/d1';


const GOOGLE_SPEECH_API_KEY = process.env.GOOGLE_SPEECH_API_KEY;

interface SpeechRecognitionResult {
  alternatives: Array<{
    transcript: string;
    confidence: number;
  }>;
}

interface SpeechRecognitionResponse {
  results?: SpeechRecognitionResult[];
  error?: {
    code: number;
    message: string;
  };
}

export async function POST(request: NextRequest) {
  try {
    const session = await auth();

    if (!session?.user?.email) {
      return NextResponse.json({ error: '로그인이 필요합니다.' }, { status: 401 });
    }

    // Check credits
    const db = getD1();
    const user = await db.prepare(
      'SELECT credits FROM phiennoi_users WHERE email = ?'
    ).bind(session.user.email).first<{ credits: number }>();
    const credits = user?.credits ?? 0;
    if (credits < 1) {
      return NextResponse.json(
        { error: '크레딧이 부족합니다. 프로필을 완성하거나 친구를 초대해주세요.' },
        { status: 402 }
      );
    }

    if (!GOOGLE_SPEECH_API_KEY) {
      return NextResponse.json({ error: 'Speech API가 설정되지 않았습니다.' }, { status: 500 });
    }

    const formData = await request.formData();
    const audioFile = formData.get('audio') as File | null;
    const languageCode = (formData.get('language') as string) || 'ko-KR';

    if (!audioFile) {
      return NextResponse.json({ error: '음성 파일이 필요합니다.' }, { status: 400 });
    }

    // Convert audio file to base64
    const arrayBuffer = await audioFile.arrayBuffer();
    const base64Audio = Buffer.from(arrayBuffer).toString('base64');

    // Determine encoding based on file type
    let encoding = 'WEBM_OPUS';
    const mimeType = audioFile.type.toLowerCase();
    if (mimeType.includes('mp3') || mimeType.includes('mpeg')) {
      encoding = 'MP3';
    } else if (mimeType.includes('wav')) {
      encoding = 'LINEAR16';
    } else if (mimeType.includes('flac')) {
      encoding = 'FLAC';
    } else if (mimeType.includes('ogg')) {
      encoding = 'OGG_OPUS';
    }

    // Call Google Speech-to-Text API
    const speechResponse = await fetch(
      `https://speech.googleapis.com/v1/speech:recognize?key=${GOOGLE_SPEECH_API_KEY}`,
      {
        method: 'POST',
        headers: {
          'Content-Type': 'application/json',
        },
        body: JSON.stringify({
          config: {
            encoding,
            sampleRateHertz: 48000,
            languageCode,
            alternativeLanguageCodes: languageCode === 'ko-KR' ? ['vi-VN'] : ['ko-KR'],
            enableAutomaticPunctuation: true,
            model: 'latest_long',
            useEnhanced: true,
          },
          audio: {
            content: base64Audio,
          },
        }),
      }
    );

    const speechResult: SpeechRecognitionResponse = await speechResponse.json();

    if (speechResult.error) {
      console.error('Speech API error:', speechResult.error);
      return NextResponse.json(
        { error: `전사 실패: ${speechResult.error.message}` },
        { status: 500 }
      );
    }

    // Extract transcript
    const transcript = speechResult.results
      ?.map(result => result.alternatives[0]?.transcript || '')
      .join('\n') || '';

    if (!transcript) {
      return NextResponse.json(
        { error: '음성을 인식하지 못했습니다. 다시 시도해주세요.' },
        { status: 400 }
      );
    }

    // Deduct credit after successful transcription
    const creditUsed = await deductCredit(session.user.email, '음성 전사');
    if (!creditUsed) {
      console.error('Failed to deduct credit');
    }

    return NextResponse.json({
      transcript,
      creditsRemaining: credits - 1,
    });
  } catch (error) {
    console.error('Transcribe error:', error);
    return NextResponse.json({ error: '서버 오류가 발생했습니다.' }, { status: 500 });
  }
}
