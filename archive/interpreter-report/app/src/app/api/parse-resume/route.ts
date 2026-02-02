export const runtime = 'edge';


import { NextRequest, NextResponse } from 'next/server';
import { auth } from '@/lib/auth';
import { GoogleGenerativeAI } from '@google/generative-ai';

// Gemini client initialized lazily to avoid build-time errors
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
    const session = await auth();

    if (!session?.user?.email) {
      return NextResponse.json({ error: '로그인이 필요합니다.' }, { status: 401 });
    }

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
    const model = genAI.getGenerativeModel({ model: 'gemini-2.0-flash-exp' });

    const prompt = `이 이력서에서 다음 정보를 추출해주세요. 정보가 없으면 빈 배열/문자열로 응답하세요.

통역사 이력서이므로 경력을 5가지 카테고리로 분류해주세요:
1. fullTimeCareer: 정규직 경력 (회사에서 근무한 경력)
2. projectCareer: 프로젝트/워크샵/세미나 통역 (KOICA, 세미나, 연수 등)
3. exhibitionCareer: 전시회/현장 통역 (K-Beauty, VietFood, SECC전시회 등)
4. b2bCareer: B2B 매칭/수출상담회 (KOTRA, aT 주관 상담회 등)
5. otherCareer: 기타 (법원통역, 수사통역, 구치소, 교육 등)

JSON 형식으로만 응답하세요 (다른 텍스트 없이):
{
  "phone": "전화번호 (베트남 형식 +84...)",
  "university": "대학교명",
  "major": "전공",
  "koreanCertificate": "TOPIK 급수 (예: TOPIK 6급)",
  "fullTimeCareer": [
    {"period": "2021.01~2021.10", "description": "대표비서/통번역", "organization": "EQ LOGIS CO., LTD.", "location": ""}
  ],
  "projectCareer": [
    {"period": "2025.08.19", "description": "KSP HCMC 교육센터 설립 통역", "organization": "우송대학교", "location": "도시철도관리위원회 (HCMC)"}
  ],
  "exhibitionCareer": [
    {"period": "2025.10.30~11.1", "description": "K-Beauty (BeautifulSmile)", "organization": "SECC전시회", "location": "HCMC, D7"}
  ],
  "b2bCareer": [
    {"period": "2024.10.17~18", "description": "K-Food 수출상담회", "organization": "aT", "location": "New World Hotel"}
  ],
  "otherCareer": [
    {"period": "2024.07.12", "description": "노동분쟁 합의 통역", "organization": "Thu Duc법원", "location": ""}
  ]
}`;

    let extractedText = '';

    if (resumeFile.type === 'application/pdf') {
      // Use Gemini Vision for PDF
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
      // For Word files, just use the filename as hint
      // In production, you'd use mammoth.js to extract text first
      const result = await model.generateContent([
        `${prompt}

이력서 파일명: ${resumeFile.name}
(Word 파일이므로 파일명에서 유추 가능한 정보만 추출하세요. 확실하지 않으면 빈 문자열로 응답하세요.)`,
      ]);

      extractedText = result.response.text();
    }

    // Parse the JSON response
    interface CareerItem {
      period: string;
      description: string;
      organization: string;
      location?: string;
    }

    let parsed: {
      phone: string;
      university: string;
      major: string;
      koreanCertificate: string;
      fullTimeCareer: CareerItem[];
      projectCareer: CareerItem[];
      exhibitionCareer: CareerItem[];
      b2bCareer: CareerItem[];
      otherCareer: CareerItem[];
    } = {
      phone: '',
      university: '',
      major: '',
      koreanCertificate: '',
      fullTimeCareer: [],
      projectCareer: [],
      exhibitionCareer: [],
      b2bCareer: [],
      otherCareer: [],
    };

    try {
      // Extract JSON from the response (may have markdown code blocks)
      const jsonMatch = extractedText.match(/\{[\s\S]*\}/);
      if (jsonMatch) {
        const jsonData = JSON.parse(jsonMatch[0]);

        // 경력 항목에 ID 추가하는 헬퍼
        const addIds = (items: CareerItem[] | undefined): CareerItem[] => {
          if (!Array.isArray(items)) return [];
          return items.map(item => ({
            ...item,
            id: crypto.randomUUID(),
          }));
        };

        parsed = {
          phone: jsonData.phone || '',
          university: jsonData.university || '',
          major: jsonData.major || '',
          koreanCertificate: jsonData.koreanCertificate || '',
          fullTimeCareer: addIds(jsonData.fullTimeCareer),
          projectCareer: addIds(jsonData.projectCareer),
          exhibitionCareer: addIds(jsonData.exhibitionCareer),
          b2bCareer: addIds(jsonData.b2bCareer),
          otherCareer: addIds(jsonData.otherCareer),
        };
      }
    } catch (parseError) {
      console.error('JSON parse error:', parseError);
      // Return empty parsed data if parsing fails
    }

    return NextResponse.json({
      success: true,
      parsed,
      resumeUrl: '',
    });

  } catch (error) {
    console.error('Resume parsing error:', error);
    return NextResponse.json(
      { error: '이력서 분석 중 오류가 발생했습니다.' },
      { status: 500 }
    );
  }
}
