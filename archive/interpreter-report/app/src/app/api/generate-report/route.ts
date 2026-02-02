export const runtime = 'edge';


import { NextRequest, NextResponse } from 'next/server';
import { auth } from '@/lib/auth';
import { getD1 } from '@/lib/d1';


interface GenerateReportRequest {
  transcript: string;
  templateType: 'standard' | 'meeting' | 'business' | 'custom';
  customFields?: string[];
  language: 'ko' | 'vi' | 'both';
}

interface GeminiResponse {
  candidates?: Array<{
    content: {
      parts: Array<{
        text: string;
      }>;
    };
  }>;
  error?: {
    message: string;
  };
}

export async function POST(request: NextRequest) {
  try {
    const session = await auth();

    if (!session?.user?.email) {
      return NextResponse.json({ error: '로그인이 필요합니다.' }, { status: 401 });
    }

    const GEMINI_API_KEY = process.env.GEMINI_API_KEY;
    if (!GEMINI_API_KEY) {
      return NextResponse.json({ error: 'Gemini API가 설정되지 않았습니다.' }, { status: 500 });
    }

    const body: GenerateReportRequest = await request.json();
    const { transcript, templateType, customFields, language } = body;

    if (!transcript) {
      return NextResponse.json({ error: '전사 내용이 필요합니다.' }, { status: 400 });
    }

    // Build prompt based on template type
    const prompt = buildPrompt(transcript, templateType, customFields, language);

    // Call Gemini API
    const geminiResponse = await fetch(
      `https://generativelanguage.googleapis.com/v1beta/models/gemini-1.5-flash:generateContent?key=${GEMINI_API_KEY}`,
      {
        method: 'POST',
        headers: {
          'Content-Type': 'application/json',
        },
        body: JSON.stringify({
          contents: [
            {
              parts: [
                {
                  text: prompt,
                },
              ],
            },
          ],
          generationConfig: {
            temperature: 0.7,
            topK: 40,
            topP: 0.95,
            maxOutputTokens: 8192,
          },
        }),
      }
    );

    const geminiResult: GeminiResponse = await geminiResponse.json();

    if (geminiResult.error) {
      console.error('Gemini API error:', geminiResult.error);
      return NextResponse.json(
        { error: `보고서 생성 실패: ${geminiResult.error.message}` },
        { status: 500 }
      );
    }

    const reportContent = geminiResult.candidates?.[0]?.content?.parts?.[0]?.text;

    if (!reportContent) {
      return NextResponse.json(
        { error: '보고서를 생성하지 못했습니다.' },
        { status: 500 }
      );
    }

    // Parse the structured report from Gemini response
    const parsedReport = parseReportContent(reportContent);

    // Save report to database
    const db = getD1();
    const reportId = crypto.randomUUID();

    try {
      await db.prepare(`
        INSERT INTO phiennoi_reports (id, user_email, transcript, content, template_type, language, status)
        VALUES (?, ?, ?, ?, ?, ?, 'draft')
      `).bind(
        reportId,
        session.user.email,
        transcript,
        JSON.stringify(parsedReport),
        templateType,
        language
      ).run();

      return NextResponse.json({
        report: parsedReport,
        reportId,
        saved: true,
      });
    } catch (dbError) {
      console.error('Database error:', dbError);
      // Still return the report even if DB save fails
      return NextResponse.json({
        report: parsedReport,
        saved: false,
      });
    }
  } catch (error) {
    console.error('Generate report error:', error);
    return NextResponse.json({ error: '서버 오류가 발생했습니다.' }, { status: 500 });
  }
}

function buildPrompt(
  transcript: string,
  templateType: string,
  customFields: string[] | undefined,
  language: string
): string {
  const languageInstruction =
    language === 'ko'
      ? '한국어로 작성해주세요.'
      : language === 'vi'
      ? 'Viết bằng tiếng Việt.'
      : '한국어와 베트남어를 병기해주세요.';

  const basePrompt = `다음 회의/통역 녹취록을 바탕으로 전문적인 보고서를 작성해주세요.

## 녹취록:
${transcript}

## 작성 지침:
- ${languageInstruction}
- 내용을 논리적으로 정리하고 구조화해주세요.
- 핵심 내용, 결정 사항, 후속 조치 등을 명확히 구분해주세요.
- JSON 형식으로 응답해주세요.

`;

  let templateInstruction = '';

  switch (templateType) {
    case 'meeting':
      templateInstruction = `## 보고서 형식: 회의록
다음 JSON 형식으로 작성해주세요:
{
  "title": "회의 제목",
  "date": "YYYY-MM-DD",
  "attendees": ["참석자1", "참석자2"],
  "agenda": ["안건1", "안건2"],
  "discussion": [
    {"topic": "논의 주제", "content": "논의 내용", "decision": "결정 사항"}
  ],
  "actionItems": [
    {"task": "할 일", "responsible": "담당자", "deadline": "기한"}
  ],
  "nextMeeting": "다음 회의 일정",
  "summary": "전체 요약"
}`;
      break;

    case 'business':
      templateInstruction = `## 보고서 형식: 비즈니스 미팅
다음 JSON 형식으로 작성해주세요:
{
  "title": "미팅 제목",
  "date": "YYYY-MM-DD",
  "parties": [{"name": "회사/담당자명", "role": "역할"}],
  "purpose": "미팅 목적",
  "keyPoints": ["핵심 내용1", "핵심 내용2"],
  "agreements": ["합의 사항1", "합의 사항2"],
  "concerns": ["우려 사항/질문"],
  "nextSteps": [{"action": "다음 단계", "owner": "담당"}],
  "summary": "전체 요약"
}`;
      break;

    case 'custom':
      if (customFields && customFields.length > 0) {
        templateInstruction = `## 보고서 형식: 사용자 정의
다음 항목을 포함한 JSON 형식으로 작성해주세요:
{
  "title": "보고서 제목",
  "date": "YYYY-MM-DD",
  ${customFields.map(field => `"${field}": "내용"`).join(',\n  ')},
  "summary": "전체 요약"
}`;
      }
      break;

    default: // standard
      templateInstruction = `## 보고서 형식: 표준 통역 보고서
다음 JSON 형식으로 작성해주세요:
{
  "title": "보고서 제목",
  "date": "YYYY-MM-DD",
  "location": "장소",
  "participants": ["참석자"],
  "purpose": "목적",
  "content": "주요 내용 (상세하게)",
  "keyPoints": ["핵심 포인트1", "핵심 포인트2"],
  "conclusion": "결론 및 후속 조치",
  "interpreterNotes": "통역사 메모 (필요시)",
  "summary": "전체 요약"
}`;
  }

  return basePrompt + templateInstruction;
}

function parseReportContent(content: string): Record<string, unknown> {
  try {
    // Try to extract JSON from the response
    const jsonMatch = content.match(/\{[\s\S]*\}/);
    if (jsonMatch) {
      return JSON.parse(jsonMatch[0]);
    }
    // If no JSON found, return as plain text
    return { content, format: 'text' };
  } catch {
    // If JSON parsing fails, return as plain text
    return { content, format: 'text' };
  }
}
