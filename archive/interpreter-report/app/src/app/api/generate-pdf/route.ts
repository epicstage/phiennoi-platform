export const runtime = 'edge';


import { NextRequest, NextResponse } from 'next/server';
import { auth } from '@/lib/auth';
import { PDFDocument, rgb, StandardFonts } from 'pdf-lib';

interface FieldData {
  label: string;
  value: string;
  x: number;
  y: number;
  width: number;
  height: number;
  type: 'text' | 'date' | 'signature' | 'checkbox' | 'multiline';
}

export async function POST(request: NextRequest) {
  try {
    const session = await auth();

    if (!session?.user?.email) {
      return NextResponse.json({ error: '로그인이 필요합니다.' }, { status: 401 });
    }

    const formData = await request.formData();
    const formImage = formData.get('formImage') as File | null;
    const fieldsJson = formData.get('fields') as string | null;
    const signatureImage = formData.get('signatureImage') as string | null;
    const pageWidth = parseFloat(formData.get('pageWidth') as string) || 595;
    const pageHeight = parseFloat(formData.get('pageHeight') as string) || 842;

    if (!formImage) {
      return NextResponse.json({ error: '양식 이미지가 필요합니다.' }, { status: 400 });
    }

    if (!fieldsJson) {
      return NextResponse.json({ error: '필드 데이터가 필요합니다.' }, { status: 400 });
    }

    const fields: FieldData[] = JSON.parse(fieldsJson);

    // Create PDF document
    const pdfDoc = await PDFDocument.create();
    const page = pdfDoc.addPage([pageWidth, pageHeight]);

    // Embed the form image as background
    const imageBuffer = await formImage.arrayBuffer();
    const imageBytes = new Uint8Array(imageBuffer);

    let embeddedImage;
    const mimeType = formImage.type.toLowerCase();

    if (mimeType.includes('png')) {
      embeddedImage = await pdfDoc.embedPng(imageBytes);
    } else if (mimeType.includes('jpeg') || mimeType.includes('jpg')) {
      embeddedImage = await pdfDoc.embedJpg(imageBytes);
    } else {
      // Try to embed as JPEG by default
      try {
        embeddedImage = await pdfDoc.embedJpg(imageBytes);
      } catch {
        try {
          embeddedImage = await pdfDoc.embedPng(imageBytes);
        } catch {
          return NextResponse.json({ error: '지원하지 않는 이미지 형식입니다. PNG 또는 JPEG를 사용해주세요.' }, { status: 400 });
        }
      }
    }

    // Scale image to fit page while maintaining aspect ratio
    const imgDims = embeddedImage.scale(1);
    const scaleX = pageWidth / imgDims.width;
    const scaleY = pageHeight / imgDims.height;
    const scale = Math.min(scaleX, scaleY);

    const scaledWidth = imgDims.width * scale;
    const scaledHeight = imgDims.height * scale;
    const xOffset = (pageWidth - scaledWidth) / 2;
    const yOffset = (pageHeight - scaledHeight) / 2;

    // Draw background image
    page.drawImage(embeddedImage, {
      x: xOffset,
      y: yOffset,
      width: scaledWidth,
      height: scaledHeight,
    });

    // Embed font for text
    const font = await pdfDoc.embedFont(StandardFonts.Helvetica);
    const boldFont = await pdfDoc.embedFont(StandardFonts.HelveticaBold);

    // Draw text fields
    for (const field of fields) {
      if (!field.value) continue;

      // Convert coordinates (PDF uses bottom-left origin, our data uses top-left)
      const pdfX = xOffset + field.x * scale;
      const pdfY = yOffset + (scaledHeight - (field.y + field.height) * scale);

      if (field.type === 'signature' && signatureImage) {
        // Handle signature
        try {
          // signatureImage is base64 data URL
          const base64Data = signatureImage.replace(/^data:image\/\w+;base64,/, '');
          const signatureBytes = Uint8Array.from(atob(base64Data), c => c.charCodeAt(0));

          const sigImage = await pdfDoc.embedPng(signatureBytes);
          const sigDims = sigImage.scale(1);

          // Scale signature to fit the field
          const sigScaleX = (field.width * scale) / sigDims.width;
          const sigScaleY = (field.height * scale) / sigDims.height;
          const sigScale = Math.min(sigScaleX, sigScaleY, 1);

          page.drawImage(sigImage, {
            x: pdfX,
            y: pdfY,
            width: sigDims.width * sigScale,
            height: sigDims.height * sigScale,
          });
        } catch (e) {
          console.error('Failed to embed signature:', e);
        }
      } else if (field.type === 'checkbox') {
        // Draw checkmark if value is truthy
        if (field.value === 'true' || field.value === '1' || field.value === 'yes') {
          page.drawText('✓', {
            x: pdfX + 2,
            y: pdfY + 2,
            size: Math.min(field.height * scale - 4, 14),
            font: font,
            color: rgb(0, 0, 0),
          });
        }
      } else if (field.type === 'multiline') {
        // Handle multiline text
        const fontSize = Math.min(10, field.height * scale / 3);
        const lines = wrapText(field.value, field.width * scale - 4, fontSize, font);
        let currentY = pdfY + field.height * scale - fontSize - 2;

        for (const line of lines) {
          if (currentY < pdfY) break;
          page.drawText(line, {
            x: pdfX + 2,
            y: currentY,
            size: fontSize,
            font: font,
            color: rgb(0, 0, 0),
          });
          currentY -= fontSize + 2;
        }
      } else {
        // Regular text
        const fontSize = Math.min(12, field.height * scale - 4);
        const textWidth = font.widthOfTextAtSize(field.value, fontSize);

        // Center text horizontally if it fits
        let textX = pdfX + 2;
        if (textWidth < field.width * scale - 4) {
          textX = pdfX + (field.width * scale - textWidth) / 2;
        }

        page.drawText(field.value, {
          x: textX,
          y: pdfY + (field.height * scale - fontSize) / 2,
          size: fontSize,
          font: font,
          color: rgb(0, 0, 0),
        });
      }
    }

    // Generate PDF bytes
    const pdfBytes = await pdfDoc.save();

    // Return PDF as response
    return new NextResponse(Buffer.from(pdfBytes), {
      headers: {
        'Content-Type': 'application/pdf',
        'Content-Disposition': `attachment; filename="report-${Date.now()}.pdf"`,
      },
    });
  } catch (error) {
    console.error('Generate PDF error:', error);
    return NextResponse.json({ error: '서버 오류가 발생했습니다.' }, { status: 500 });
  }
}

function wrapText(text: string, maxWidth: number, fontSize: number, font: { widthOfTextAtSize: (text: string, size: number) => number }): string[] {
  const words = text.split(' ');
  const lines: string[] = [];
  let currentLine = '';

  for (const word of words) {
    const testLine = currentLine ? `${currentLine} ${word}` : word;
    const testWidth = font.widthOfTextAtSize(testLine, fontSize);

    if (testWidth > maxWidth && currentLine) {
      lines.push(currentLine);
      currentLine = word;
    } else {
      currentLine = testLine;
    }
  }

  if (currentLine) {
    lines.push(currentLine);
  }

  return lines;
}
