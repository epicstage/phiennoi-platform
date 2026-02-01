import { NextRequest, NextResponse } from 'next/server';
import { GoogleGenerativeAI } from '@google/generative-ai';

let geminiClient: GoogleGenerativeAI | null = null;

function getGeminiClient(): GoogleGenerativeAI {
  if (!geminiClient) {
    if (!process.env.GEMINI_API_KEY) {
      throw new Error('GEMINI_API_KEY is not configured');
    }
    geminiClient = new GoogleGenerativeAI(process.env.GEMINI_API_KEY);
  }
  return geminiClient;
}

export async function POST(request: NextRequest) {
  try {
    const formData = await request.formData();
    const resumeFile = formData.get('resume') as File | null;

    if (!resumeFile) {
      return NextResponse.json({ error: '이력서 파일이 필요합니다.' }, { status: 400 });
    }

    // Check file type
    const allowedTypes = ['application/pdf', 'application/msword', 'application/vnd.openxmlformats-officedocument.wordprocessingml.document'];
    if (!allowedTypes.includes(resumeFile.type)) {
      return NextResponse.json({ error: 'PDF 또는 Word 파일만 지원합니다.' }, { status: 400 });
    }

    // Check file size (max 10MB)
    if (resumeFile.size > 10 * 1024 * 1024) {
      return NextResponse.json({ error: '파일 크기는 10MB 이하여야 합니다.' }, { status: 400 });
    }

    // Convert file to base64
    const bytes = await resumeFile.arrayBuffer();
    const base64 = Buffer.from(bytes).toString('base64');

    const genAI = getGeminiClient();
    const model = genAI.getGenerativeModel({ model: 'gemini-1.5-flash' });

    const prompt = `이 이력서에서 다음 정보를 추출해주세요. 정보가 없으면 빈 문자열/배열로 응답하세요.

통역사 이력서이므로 다음 정보를 추출하세요:

JSON 형식으로만 응답하세요 (다른 텍스트 없이):
{
  "name": "이름",
  "phone": "전화번호",
  "email": "이메일",
  "university": "대학교명",
  "major": "전공",
  "koreanLevel": "TOPIK 급수 (예: 6급)",
  "location": "활동 지역 (호치민/하노이/다낭 등)",
  "domains": ["전문 분야 배열 - agriculture, beauty, manufacturing, legal, medical, it, construction, exhibition, finance, logistics, food, hr, tourism, trade, textile, electronics, environment, education, automotive, realEstate 중에서"],
  "careers": [
    {"period": "기간", "description": "내용", "organization": "기관/회사", "type": "fulltime/project/exhibition/b2b/other"}
  ],
  "summary": "경력 요약 (2-3문장)"
}`;

    let extractedText = '';

    if (resumeFile.type === 'application/pdf') {
      const result = await model.generateContent([
        prompt,
        {
          inlineData: {
            mimeType: 'application/pdf',
            data: base64,
          },
        },
      ]);
      extractedText = result.response.text();
    } else {
      const result = await model.generateContent([
        `${prompt}\n\n이력서 파일명: ${resumeFile.name}\n(Word 파일이므로 파일명에서 유추 가능한 정보만 추출하세요.)`,
      ]);
      extractedText = result.response.text();
    }

    // Parse the JSON response
    interface ParsedResume {
      name: string;
      phone: string;
      email: string;
      university: string;
      major: string;
      koreanLevel: string;
      location: string;
      domains: string[];
      careers: Array<{
        period: string;
        description: string;
        organization: string;
        type: string;
      }>;
      summary: string;
    }

    let parsed: ParsedResume = {
      name: '',
      phone: '',
      email: '',
      university: '',
      major: '',
      koreanLevel: '',
      location: '',
      domains: [],
      careers: [],
      summary: '',
    };

    try {
      const jsonMatch = extractedText.match(/\{[\s\S]*\}/);
      if (jsonMatch) {
        const jsonData = JSON.parse(jsonMatch[0]);
        parsed = {
          name: jsonData.name || '',
          phone: jsonData.phone || '',
          email: jsonData.email || '',
          university: jsonData.university || '',
          major: jsonData.major || '',
          koreanLevel: jsonData.koreanLevel || '',
          location: jsonData.location || '',
          domains: Array.isArray(jsonData.domains) ? jsonData.domains : [],
          careers: Array.isArray(jsonData.careers) ? jsonData.careers : [],
          summary: jsonData.summary || '',
        };
      }
    } catch (parseError) {
      console.error('JSON parse error:', parseError);
    }

    return NextResponse.json({
      success: true,
      parsed,
    });

  } catch (error) {
    console.error('Resume parsing error:', error);
    const errorMessage = error instanceof Error ? error.message : 'Unknown error';
    return NextResponse.json(
      { error: `이력서 분석 중 오류가 발생했습니다: ${errorMessage}` },
      { status: 500 }
    );
  }
}
