export const runtime = 'edge';


import { NextRequest, NextResponse } from 'next/server';
import { auth } from '@/lib/auth';

const GEMINI_API_KEY = process.env.GEMINI_API_KEY;

interface FieldPosition {
  label: string;
  x: number;
  y: number;
  width: number;
  height: number;
  type: 'text' | 'date' | 'signature' | 'checkbox' | 'multiline';
}

interface FormAnalysisResult {
  fields: FieldPosition[];
  hasSignature: boolean;
  signaturePosition?: FieldPosition;
  pageWidth: number;
  pageHeight: number;
}

interface BusinessCardResult {
  companyName?: string;
  personName?: string;
  position?: string;
  phone?: string;
  email?: string;
  address?: string;
}

export async function POST(request: NextRequest) {
  try {
    const session = await auth();

    if (!session?.user?.email) {
      return NextResponse.json({ error: '로그인이 필요합니다.' }, { status: 401 });
    }

    if (!GEMINI_API_KEY) {
      return NextResponse.json({ error: 'Gemini API가 설정되지 않았습니다.' }, { status: 500 });
    }

    const formData = await request.formData();
    const formImage = formData.get('formImage') as File | null;
    const businessCardImage = formData.get('businessCardImage') as File | null;
    const analysisType = formData.get('type') as string || 'form';

    if (analysisType === 'form' && !formImage) {
      return NextResponse.json({ error: '양식 이미지가 필요합니다.' }, { status: 400 });
    }

    if (analysisType === 'businessCard' && !businessCardImage) {
      return NextResponse.json({ error: '명함 이미지가 필요합니다.' }, { status: 400 });
    }

    if (analysisType === 'form' && formImage) {
      const result = await analyzeForm(formImage);
      return NextResponse.json(result);
    }

    if (analysisType === 'businessCard' && businessCardImage) {
      const result = await analyzeBusinessCard(businessCardImage);
      return NextResponse.json(result);
    }

    if (analysisType === 'both') {
      const results: { form?: FormAnalysisResult; businessCard?: BusinessCardResult } = {};

      if (formImage) {
        results.form = await analyzeForm(formImage);
      }
      if (businessCardImage) {
        results.businessCard = await analyzeBusinessCard(businessCardImage);
      }

      return NextResponse.json(results);
    }

    return NextResponse.json({ error: '잘못된 요청입니다.' }, { status: 400 });
  } catch (error) {
    console.error('Analyze form error:', error);
    return NextResponse.json({ error: '서버 오류가 발생했습니다.' }, { status: 500 });
  }
}

async function analyzeForm(formImage: File): Promise<FormAnalysisResult> {
  const imageBase64 = await fileToBase64(formImage);
  const mimeType = formImage.type || 'image/jpeg';

  const prompt = `이 양식 이미지를 분석해주세요. 다음 정보를 JSON 형식으로 반환해주세요:

1. 모든 입력 필드(빈칸)의 위치와 크기를 찾아주세요.
2. 각 필드 옆에 있는 라벨(소제목)을 확인해주세요.
3. 서명란이 있는지 확인하고, 있다면 위치를 알려주세요.
4. 이미지의 전체 크기(가로 x 세로)를 추정해주세요 (A4 기준 595 x 842 포인트).

모든 좌표는 이미지 왼쪽 위를 기준(0,0)으로 하고, 단위는 포인트(pt, A4 기준)로 표시해주세요.

JSON 형식:
{
  "fields": [
    {
      "label": "필드 라벨/소제목",
      "x": 왼쪽 위 X 좌표,
      "y": 왼쪽 위 Y 좌표,
      "width": 필드 너비,
      "height": 필드 높이,
      "type": "text" | "date" | "signature" | "checkbox" | "multiline"
    }
  ],
  "hasSignature": true/false,
  "signaturePosition": { 서명란 정보 (있는 경우) },
  "pageWidth": 페이지 너비,
  "pageHeight": 페이지 높이
}

중요:
- 빈칸이 아닌 곳(이미 텍스트가 채워진 곳)은 제외하세요.
- 필드 타입을 정확히 구분해주세요 (날짜, 서명, 체크박스, 여러 줄 텍스트 등).
- 좌표는 최대한 정확하게 추정해주세요.`;

  const response = await callGeminiVision(imageBase64, mimeType, prompt);

  try {
    const jsonMatch = response.match(/\{[\s\S]*\}/);
    if (jsonMatch) {
      return JSON.parse(jsonMatch[0]);
    }
  } catch (e) {
    console.error('Failed to parse form analysis:', e);
  }

  return {
    fields: [],
    hasSignature: false,
    pageWidth: 595,
    pageHeight: 842,
  };
}

async function analyzeBusinessCard(cardImage: File): Promise<BusinessCardResult> {
  const imageBase64 = await fileToBase64(cardImage);
  const mimeType = cardImage.type || 'image/jpeg';

  const prompt = `이 명함 이미지에서 다음 정보를 추출해주세요:

1. 회사명
2. 담당자 이름
3. 직책/직위
4. 전화번호
5. 이메일
6. 주소

JSON 형식으로 반환해주세요:
{
  "companyName": "회사명",
  "personName": "담당자 이름",
  "position": "직책",
  "phone": "전화번호",
  "email": "이메일",
  "address": "주소"
}

읽을 수 없거나 없는 정보는 null로 표시해주세요.
한국어와 베트남어, 영어 명함 모두 처리 가능합니다.`;

  const response = await callGeminiVision(imageBase64, mimeType, prompt);

  try {
    const jsonMatch = response.match(/\{[\s\S]*\}/);
    if (jsonMatch) {
      return JSON.parse(jsonMatch[0]);
    }
  } catch (e) {
    console.error('Failed to parse business card:', e);
  }

  return {};
}

async function callGeminiVision(imageBase64: string, mimeType: string, prompt: string): Promise<string> {
  const response = await fetch(
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
                inline_data: {
                  mime_type: mimeType,
                  data: imageBase64,
                },
              },
              {
                text: prompt,
              },
            ],
          },
        ],
        generationConfig: {
          temperature: 0.2,
          topK: 40,
          topP: 0.95,
          maxOutputTokens: 4096,
        },
      }),
    }
  );

  const result = await response.json() as {
    error?: { message: string };
    candidates?: Array<{ content?: { parts?: Array<{ text?: string }> } }>;
  };

  if (result.error) {
    throw new Error(result.error.message);
  }

  return result.candidates?.[0]?.content?.parts?.[0]?.text || '';
}

async function fileToBase64(file: File): Promise<string> {
  const buffer = await file.arrayBuffer();
  const bytes = new Uint8Array(buffer);
  let binary = '';
  for (let i = 0; i < bytes.byteLength; i++) {
    binary += String.fromCharCode(bytes[i]);
  }
  return btoa(binary);
}
