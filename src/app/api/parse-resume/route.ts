import { NextRequest, NextResponse } from 'next/server';
import { GoogleGenAI } from '@google/genai';

let genAIClient: GoogleGenAI | null = null;

function getGenAIClient(): GoogleGenAI {
  if (!genAIClient) {
    if (!process.env.GEMINI_API_KEY) {
      throw new Error('GEMINI_API_KEY is not configured');
    }
    genAIClient = new GoogleGenAI({ apiKey: process.env.GEMINI_API_KEY });
  }
  return genAIClient;
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

    const genAI = getGenAIClient();

    const prompt = `이 이력서에서 다음 정보를 추출해주세요. 정보가 없으면 빈 문자열/배열로 응답하세요.

베트남인 통역사 이력서이므로 다음 정보를 추출하세요:

JSON 형식으로만 응답하세요 (다른 텍스트 없이):
{
  "name": "이름 (베트남 이름)",
  "phoneVietnam": "베트남 전화번호 (84 또는 0으로 시작하는 번호)",
  "phoneKorea": "한국 전화번호 (82 또는 010으로 시작하는 번호)",
  "email": "이메일",
  "universityVietnam": "베트남에서 졸업한 대학교명 (있으면)",
  "universityKorea": "한국에서 졸업한 대학교명 (있으면)",
  "major": "전공",
  "koreanLevel": "TOPIK 급수 (예: 6급) 또는 한국어 능력 수준",
  "location": "활동 지역 (호치민/하노이/다낭 등)",
  "domains": ["이력서 내용에 기반하여 가장 관련 있는 전문 분야를 선택. 가능한 값: agriculture, beauty, manufacturing, legal, medical, it, construction, exhibition, finance, logistics, food, hr, tourism, trade, textile, electronics, environment, education, automotive, realEstate"],
  "companyExperience": [
    {"period": "기간", "company": "회사명", "position": "직책/역할", "description": "업무 설명"}
  ],
  "eventExperience": [
    {"period": "기간", "eventName": "행사/전시회/B2B 이름", "client": "클라이언트", "type": "exhibition/b2b/seminar/project/legal/other", "location": "장소"}
  ],
  "summary": "경력 요약 (2-3문장, 한국어로)"
}

중요:
- 전화번호는 베트남 번호와 한국 번호를 분리해서 추출
- 대학교도 베트남 대학과 한국 대학을 분리
- 경력은 '회사 근무 이력(companyExperience)'과 '행사/통역 이력(eventExperience)'으로 분리
- domains는 이력서 내용을 분석하여 가장 관련 있는 분야 2-5개 선택
- 전시회, B2B, 세미나 등 행사 통역 이력은 eventExperience로 분류`;

    let extractedText = '';

    if (resumeFile.type === 'application/pdf') {
      const response = await genAI.models.generateContent({
        model: 'gemini-2.0-flash',
        contents: [
          {
            role: 'user',
            parts: [
              { text: prompt },
              {
                inlineData: {
                  mimeType: 'application/pdf',
                  data: base64,
                },
              },
            ],
          },
        ],
      });
      extractedText = response.text || '';
    } else {
      const response = await genAI.models.generateContent({
        model: 'gemini-2.0-flash',
        contents: [
          {
            role: 'user',
            parts: [
              { text: `${prompt}\n\n이력서 파일명: ${resumeFile.name}\n(Word 파일이므로 파일명에서 유추 가능한 정보만 추출하세요.)` },
            ],
          },
        ],
      });
      extractedText = response.text || '';
    }

    // Parse the JSON response
    interface ParsedResume {
      name: string;
      phoneVietnam: string;
      phoneKorea: string;
      email: string;
      universityVietnam: string;
      universityKorea: string;
      major: string;
      koreanLevel: string;
      location: string;
      domains: string[];
      companyExperience: Array<{
        period: string;
        company: string;
        position: string;
        description: string;
      }>;
      eventExperience: Array<{
        period: string;
        eventName: string;
        client: string;
        type: string;
        location: string;
      }>;
      summary: string;
    }

    let parsed: ParsedResume = {
      name: '',
      phoneVietnam: '',
      phoneKorea: '',
      email: '',
      universityVietnam: '',
      universityKorea: '',
      major: '',
      koreanLevel: '',
      location: '',
      domains: [],
      companyExperience: [],
      eventExperience: [],
      summary: '',
    };

    try {
      const jsonMatch = extractedText.match(/\{[\s\S]*\}/);
      if (jsonMatch) {
        const jsonData = JSON.parse(jsonMatch[0]);
        parsed = {
          name: jsonData.name || '',
          phoneVietnam: jsonData.phoneVietnam || '',
          phoneKorea: jsonData.phoneKorea || '',
          email: jsonData.email || '',
          universityVietnam: jsonData.universityVietnam || '',
          universityKorea: jsonData.universityKorea || '',
          major: jsonData.major || '',
          koreanLevel: jsonData.koreanLevel || '',
          location: jsonData.location || '',
          domains: Array.isArray(jsonData.domains) ? jsonData.domains : [],
          companyExperience: Array.isArray(jsonData.companyExperience) ? jsonData.companyExperience : [],
          eventExperience: Array.isArray(jsonData.eventExperience) ? jsonData.eventExperience : [],
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
