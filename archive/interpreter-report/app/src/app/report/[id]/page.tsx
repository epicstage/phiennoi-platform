'use client';

import { useEffect, useState, useRef, use } from 'react';
import Link from 'next/link';
import { useSession } from 'next-auth/react';
import { useRouter } from 'next/navigation';
import { jsPDF } from 'jspdf';
import {
  ArrowLeft,
  Download,
  Trash2,
  Loader2,
  FileText,
  Clock,
  AlertCircle,
  Share2,
  MessageCircle,
  X,
  FolderDown,
  Send
} from 'lucide-react';

interface ReportData {
  id: string;
  title: string;
  content: Record<string, unknown>;
  transcript: string;
  template_type: string;
  language: string;
  status: string;
  created_at: string;
  signature?: string;
}

export default function ReportDetailPage({ params }: { params: Promise<{ id: string }> }) {
  const resolvedParams = use(params);
  const { data: session, status } = useSession();
  const router = useRouter();
  const [report, setReport] = useState<ReportData | null>(null);
  const [isLoading, setIsLoading] = useState(true);
  const [isDeleting, setIsDeleting] = useState(false);
  const [isDownloading, setIsDownloading] = useState(false);
  const [error, setError] = useState<string | null>(null);
  const [showSignature, setShowSignature] = useState(false);
  const [showShareModal, setShowShareModal] = useState(false);
  const [signature, setSignature] = useState<string | null>(null);
  const [isDrawing, setIsDrawing] = useState(false);
  const [pdfBlob, setPdfBlob] = useState<Blob | null>(null);
  const [isSharing, setIsSharing] = useState(false);
  const signatureCanvasRef = useRef<HTMLCanvasElement>(null);

  useEffect(() => {
    if (status === 'unauthenticated') {
      router.push('/login');
    }
  }, [status, router]);

  useEffect(() => {
    const fetchReport = async () => {
      if (!session?.user?.email) return;

      try {
        const res = await fetch(`/api/reports/${resolvedParams.id}`);
        const data = await res.json() as { error?: string; report?: ReportData };

        if (!res.ok) {
          throw new Error(data.error || '보고서를 불러올 수 없습니다.');
        }

        setReport(data.report || null);
      } catch (err) {
        setError(err instanceof Error ? err.message : '오류가 발생했습니다.');
      } finally {
        setIsLoading(false);
      }
    };

    if (status === 'authenticated') {
      fetchReport();
    }
  }, [session, status, resolvedParams.id]);

  const handleDelete = async () => {
    if (!confirm('정말 이 보고서를 삭제하시겠습니까?')) return;

    setIsDeleting(true);
    try {
      const res = await fetch(`/api/reports/${resolvedParams.id}`, { method: 'DELETE' });
      if (res.ok) {
        router.push('/reports');
      } else {
        const data = await res.json() as { error?: string };
        alert(data.error || '삭제에 실패했습니다.');
      }
    } catch {
      alert('삭제 중 오류가 발생했습니다.');
    } finally {
      setIsDeleting(false);
    }
  };

  // Signature functions
  const startDrawing = (e: React.MouseEvent<HTMLCanvasElement> | React.TouchEvent<HTMLCanvasElement>) => {
    const canvas = signatureCanvasRef.current;
    if (!canvas) return;

    setIsDrawing(true);
    const ctx = canvas.getContext('2d');
    if (!ctx) return;

    const rect = canvas.getBoundingClientRect();
    let x: number, y: number;

    if ('touches' in e) {
      x = e.touches[0].clientX - rect.left;
      y = e.touches[0].clientY - rect.top;
    } else {
      x = e.clientX - rect.left;
      y = e.clientY - rect.top;
    }

    ctx.beginPath();
    ctx.moveTo(x, y);
  };

  const draw = (e: React.MouseEvent<HTMLCanvasElement> | React.TouchEvent<HTMLCanvasElement>) => {
    if (!isDrawing) return;
    const canvas = signatureCanvasRef.current;
    if (!canvas) return;

    const ctx = canvas.getContext('2d');
    if (!ctx) return;

    const rect = canvas.getBoundingClientRect();
    let x: number, y: number;

    if ('touches' in e) {
      e.preventDefault();
      x = e.touches[0].clientX - rect.left;
      y = e.touches[0].clientY - rect.top;
    } else {
      x = e.clientX - rect.left;
      y = e.clientY - rect.top;
    }

    ctx.lineWidth = 2;
    ctx.lineCap = 'round';
    ctx.strokeStyle = '#6366f1';
    ctx.lineTo(x, y);
    ctx.stroke();
  };

  const stopDrawing = () => {
    setIsDrawing(false);
    const canvas = signatureCanvasRef.current;
    if (canvas) {
      setSignature(canvas.toDataURL('image/png'));
    }
  };

  const clearSignature = () => {
    const canvas = signatureCanvasRef.current;
    if (canvas) {
      const ctx = canvas.getContext('2d');
      if (ctx) {
        ctx.fillStyle = '#1a1a1a';
        ctx.fillRect(0, 0, canvas.width, canvas.height);
      }
    }
    setSignature(null);
  };

  useEffect(() => {
    if (showSignature && signatureCanvasRef.current) {
      const canvas = signatureCanvasRef.current;
      const ctx = canvas.getContext('2d');
      if (ctx) {
        ctx.fillStyle = '#1a1a1a';
        ctx.fillRect(0, 0, canvas.width, canvas.height);
      }
    }
  }, [showSignature]);

  const handleDownloadPDF = async () => {
    if (!report) return;

    setIsDownloading(true);

    try {
      const doc = new jsPDF({
        orientation: 'portrait',
        unit: 'mm',
        format: 'a4',
      });

      const pageWidth = doc.internal.pageSize.getWidth();
      const pageHeight = doc.internal.pageSize.getHeight();
      const margin = 20;
      const contentWidth = pageWidth - margin * 2;
      let yPos = margin;

      const checkNewPage = (neededSpace: number) => {
        if (yPos + neededSpace > pageHeight - margin) {
          doc.addPage();
          yPos = margin;
        }
      };

      const fieldLabels: Record<string, string> = {
        title: '제목 / Title',
        date: '날짜 / Date',
        location: '장소 / Location',
        participants: '참석자 / Participants',
        attendees: '참석자 / Attendees',
        parties: '참가자 / Parties',
        purpose: '목적 / Purpose',
        content: '내용 / Content',
        keyPoints: '핵심 포인트 / Key Points',
        discussion: '논의 내용 / Discussion',
        agreements: '합의 사항 / Agreements',
        actionItems: '후속 조치 / Action Items',
        nextSteps: '다음 단계 / Next Steps',
        nextMeeting: '다음 회의 / Next Meeting',
        conclusion: '결론 / Conclusion',
        concerns: '우려 사항 / Concerns',
        interpreterNotes: '통역사 메모 / Interpreter Notes',
        summary: '요약 / Summary',
        agenda: '안건 / Agenda',
      };

      // Header
      doc.setFontSize(18);
      doc.setTextColor(30, 58, 95);
      const title = String(report.content.title || report.title || '통역 보고서');
      doc.text(title, pageWidth / 2, yPos, { align: 'center' });
      yPos += 10;

      // Date
      doc.setFontSize(10);
      doc.setTextColor(128, 128, 128);
      const date = String(report.content.date || new Date(report.created_at).toLocaleDateString('ko-KR'));
      doc.text(date, pageWidth / 2, yPos, { align: 'center' });
      yPos += 10;

      doc.setDrawColor(200, 200, 200);
      doc.line(margin, yPos, pageWidth - margin, yPos);
      yPos += 10;

      doc.setTextColor(0, 0, 0);

      const renderValue = (value: unknown): string => {
        if (value === null || value === undefined) return '';
        if (Array.isArray(value)) {
          return value.map((item) => {
            if (typeof item === 'object') {
              return Object.entries(item as Record<string, unknown>)
                .map(([k, v]) => `${k}: ${v}`)
                .join(', ');
            }
            return `• ${String(item)}`;
          }).join('\n');
        }
        if (typeof value === 'object') {
          return Object.entries(value as Record<string, unknown>)
            .map(([k, v]) => `${k}: ${v}`)
            .join('\n');
        }
        return String(value);
      };

      for (const [key, value] of Object.entries(report.content)) {
        if (key === 'format' || key === 'title' || key === 'date') continue;
        if (value === null || value === undefined) continue;

        const label = fieldLabels[key] || key;
        const content = renderValue(value);
        if (!content) continue;

        checkNewPage(20);

        doc.setFontSize(11);
        doc.setFont('helvetica', 'bold');
        doc.setTextColor(30, 58, 95);
        doc.text(label, margin, yPos);
        yPos += 6;

        doc.setFontSize(10);
        doc.setFont('helvetica', 'normal');
        doc.setTextColor(60, 60, 60);

        const lines = doc.splitTextToSize(content, contentWidth);
        for (const line of lines) {
          checkNewPage(6);
          doc.text(line, margin, yPos);
          yPos += 5;
        }
        yPos += 5;
      }

      // Signature if available
      if (signature) {
        checkNewPage(50);
        yPos += 10;

        doc.setDrawColor(200, 200, 200);
        doc.line(margin, yPos, pageWidth - margin, yPos);
        yPos += 10;

        doc.setFontSize(11);
        doc.setFont('helvetica', 'bold');
        doc.setTextColor(30, 58, 95);
        doc.text('서명 / Signature', margin, yPos);
        yPos += 8;

        const signatureImg = new Image();
        signatureImg.src = signature;
        await new Promise<void>((resolve) => {
          signatureImg.onload = () => {
            const sigWidth = 60;
            const sigHeight = 25;
            doc.addImage(signature, 'PNG', margin, yPos, sigWidth, sigHeight);
            resolve();
          };
          signatureImg.onerror = () => resolve();
        });
        yPos += 30;

        doc.setFontSize(9);
        doc.setFont('helvetica', 'normal');
        doc.setTextColor(128, 128, 128);
        doc.text(`서명일: ${new Date().toLocaleDateString('ko-KR')}`, margin, yPos);
      }

      // Footer
      doc.setFontSize(8);
      doc.setTextColor(180, 180, 180);
      doc.text('Generated by Phiennoi - AI Interpreter Report', pageWidth / 2, pageHeight - 10, { align: 'center' });

      const fileName = `report-${report.id.substring(0, 8)}.pdf`;
      doc.save(fileName);

    } catch (error) {
      console.error('PDF generation error:', error);
      alert('PDF 생성 중 오류가 발생했습니다.');
    } finally {
      setIsDownloading(false);
      setShowSignature(false);
    }
  };

  // PDF Blob 생성 (공유용)
  const generatePDFBlob = async (): Promise<Blob | null> => {
    if (!report) return null;

    try {
      const doc = new jsPDF({
        orientation: 'portrait',
        unit: 'mm',
        format: 'a4',
      });

      const pageWidth = doc.internal.pageSize.getWidth();
      const pageHeight = doc.internal.pageSize.getHeight();
      const margin = 20;
      const contentWidth = pageWidth - margin * 2;
      let yPos = margin;

      const checkNewPage = (neededSpace: number) => {
        if (yPos + neededSpace > pageHeight - margin) {
          doc.addPage();
          yPos = margin;
        }
      };

      const fieldLabels: Record<string, string> = {
        title: '제목 / Title',
        date: '날짜 / Date',
        location: '장소 / Location',
        participants: '참석자 / Participants',
        attendees: '참석자 / Attendees',
        parties: '참가자 / Parties',
        purpose: '목적 / Purpose',
        content: '내용 / Content',
        keyPoints: '핵심 포인트 / Key Points',
        discussion: '논의 내용 / Discussion',
        agreements: '합의 사항 / Agreements',
        actionItems: '후속 조치 / Action Items',
        nextSteps: '다음 단계 / Next Steps',
        nextMeeting: '다음 회의 / Next Meeting',
        conclusion: '결론 / Conclusion',
        concerns: '우려 사항 / Concerns',
        interpreterNotes: '통역사 메모 / Interpreter Notes',
        summary: '요약 / Summary',
        agenda: '안건 / Agenda',
      };

      // Header
      doc.setFontSize(18);
      doc.setTextColor(30, 58, 95);
      const title = String(report.content.title || report.title || '통역 보고서');
      doc.text(title, pageWidth / 2, yPos, { align: 'center' });
      yPos += 10;

      // Date
      doc.setFontSize(10);
      doc.setTextColor(128, 128, 128);
      const date = String(report.content.date || new Date(report.created_at).toLocaleDateString('ko-KR'));
      doc.text(date, pageWidth / 2, yPos, { align: 'center' });
      yPos += 10;

      doc.setDrawColor(200, 200, 200);
      doc.line(margin, yPos, pageWidth - margin, yPos);
      yPos += 10;

      doc.setTextColor(0, 0, 0);

      const renderValueStr = (value: unknown): string => {
        if (value === null || value === undefined) return '';
        if (Array.isArray(value)) {
          return value.map((item) => {
            if (typeof item === 'object') {
              return Object.entries(item as Record<string, unknown>)
                .map(([k, v]) => `${k}: ${v}`)
                .join(', ');
            }
            return `• ${String(item)}`;
          }).join('\n');
        }
        if (typeof value === 'object') {
          return Object.entries(value as Record<string, unknown>)
            .map(([k, v]) => `${k}: ${v}`)
            .join('\n');
        }
        return String(value);
      };

      for (const [key, value] of Object.entries(report.content)) {
        if (key === 'format' || key === 'title' || key === 'date') continue;
        if (value === null || value === undefined) continue;

        const label = fieldLabels[key] || key;
        const content = renderValueStr(value);
        if (!content) continue;

        checkNewPage(20);

        doc.setFontSize(11);
        doc.setFont('helvetica', 'bold');
        doc.setTextColor(30, 58, 95);
        doc.text(label, margin, yPos);
        yPos += 6;

        doc.setFontSize(10);
        doc.setFont('helvetica', 'normal');
        doc.setTextColor(60, 60, 60);

        const lines = doc.splitTextToSize(content, contentWidth);
        for (const line of lines) {
          checkNewPage(6);
          doc.text(line, margin, yPos);
          yPos += 5;
        }
        yPos += 5;
      }

      // Signature if available
      if (signature) {
        checkNewPage(50);
        yPos += 10;

        doc.setDrawColor(200, 200, 200);
        doc.line(margin, yPos, pageWidth - margin, yPos);
        yPos += 10;

        doc.setFontSize(11);
        doc.setFont('helvetica', 'bold');
        doc.setTextColor(30, 58, 95);
        doc.text('서명 / Signature', margin, yPos);
        yPos += 8;

        const signatureImg = new Image();
        signatureImg.src = signature;
        await new Promise<void>((resolve) => {
          signatureImg.onload = () => {
            const sigWidth = 60;
            const sigHeight = 25;
            doc.addImage(signature, 'PNG', margin, yPos, sigWidth, sigHeight);
            resolve();
          };
          signatureImg.onerror = () => resolve();
        });
        yPos += 30;

        doc.setFontSize(9);
        doc.setFont('helvetica', 'normal');
        doc.setTextColor(128, 128, 128);
        doc.text(`서명일: ${new Date().toLocaleDateString('ko-KR')}`, margin, yPos);
      }

      // Footer
      doc.setFontSize(8);
      doc.setTextColor(180, 180, 180);
      doc.text('Generated by Phiennoi - Epicstage Corp.', pageWidth / 2, pageHeight - 10, { align: 'center' });

      return doc.output('blob');
    } catch (error) {
      console.error('PDF generation error:', error);
      return null;
    }
  };

  // 공유 모달 열기 (PDF 먼저 생성)
  const handleOpenShareModal = async () => {
    setIsSharing(true);
    const blob = await generatePDFBlob();
    if (blob) {
      setPdfBlob(blob);
      setShowShareModal(true);
    } else {
      alert('PDF 생성에 실패했습니다.');
    }
    setIsSharing(false);
  };

  // 네이티브 공유 (Web Share API)
  const handleNativeShare = async () => {
    if (!pdfBlob || !report) return;

    const fileName = `report-${report.id.substring(0, 8)}.pdf`;
    const file = new File([pdfBlob], fileName, { type: 'application/pdf' });

    if (navigator.share && navigator.canShare && navigator.canShare({ files: [file] })) {
      try {
        await navigator.share({
          files: [file],
          title: String(report.content.title || '통역 보고서'),
          text: 'Phiennoi로 생성된 통역 보고서입니다.',
        });
        setShowShareModal(false);
      } catch (err) {
        if ((err as Error).name !== 'AbortError') {
          console.error('Share failed:', err);
        }
      }
    } else {
      alert('이 브라우저에서는 파일 공유가 지원되지 않습니다.');
    }
  };

  // Zalo로 공유 (딥링크 - 텍스트만 가능)
  const handleZaloShare = () => {
    const title = String(report?.content.title || '통역 보고서');
    const text = `[Phiennoi 보고서]\n${title}\n\nPhiennoi로 생성된 통역 보고서입니다.`;
    const zaloUrl = `https://zalo.me/share?url=${encodeURIComponent(window.location.href)}&text=${encodeURIComponent(text)}`;
    window.open(zaloUrl, '_blank');
  };

  // WhatsApp으로 공유
  const handleWhatsAppShare = () => {
    const title = String(report?.content.title || '통역 보고서');
    const text = `[Phiennoi 보고서]\n${title}\n\nPhiennoi로 생성된 통역 보고서입니다.\n${window.location.href}`;
    const whatsappUrl = `https://wa.me/?text=${encodeURIComponent(text)}`;
    window.open(whatsappUrl, '_blank');
  };

  // 카카오톡으로 공유 (카카오 SDK 미사용시 URL 공유)
  const handleKakaoShare = () => {
    const title = String(report?.content.title || '통역 보고서');
    const text = `[Phiennoi 보고서] ${title}`;
    const kakaoUrl = `https://story.kakao.com/share?url=${encodeURIComponent(window.location.href)}&text=${encodeURIComponent(text)}`;
    window.open(kakaoUrl, '_blank');
  };

  // PDF 파일 저장
  const handleSavePDF = () => {
    if (!pdfBlob || !report) return;

    const fileName = `report-${report.id.substring(0, 8)}.pdf`;
    const url = URL.createObjectURL(pdfBlob);
    const a = document.createElement('a');
    a.href = url;
    a.download = fileName;
    document.body.appendChild(a);
    a.click();
    document.body.removeChild(a);
    URL.revokeObjectURL(url);
    setShowShareModal(false);
  };

  const formatDate = (dateString: string) => {
    const date = new Date(dateString);
    return date.toLocaleDateString('ko-KR', {
      year: 'numeric',
      month: 'long',
      day: 'numeric',
      hour: '2-digit',
      minute: '2-digit',
    });
  };

  const renderValue = (value: unknown): React.ReactNode => {
    if (value === null || value === undefined) return null;

    if (Array.isArray(value)) {
      if (value.length === 0) return null;

      if (typeof value[0] === 'object') {
        return (
          <div className="space-y-2">
            {value.map((item, idx) => (
              <div key={idx} className="bg-[#1a1a1a] rounded-lg p-3 text-sm">
                {Object.entries(item as Record<string, unknown>).map(([k, v]) => (
                  <div key={k} className="flex gap-2">
                    <span className="text-gray-500 capitalize">{k}:</span>
                    <span className="text-gray-200">{String(v)}</span>
                  </div>
                ))}
              </div>
            ))}
          </div>
        );
      }

      return (
        <ul className="list-disc list-inside space-y-1">
          {value.map((item, idx) => (
            <li key={idx} className="text-sm text-gray-300">{String(item)}</li>
          ))}
        </ul>
      );
    }

    if (typeof value === 'object') {
      return (
        <div className="bg-[#1a1a1a] rounded-lg p-3 space-y-2">
          {Object.entries(value as Record<string, unknown>).map(([k, v]) => (
            <div key={k}>
              <span className="text-gray-500 text-xs capitalize">{k}:</span>
              <div className="text-sm text-gray-200">{String(v)}</div>
            </div>
          ))}
        </div>
      );
    }

    return <p className="text-sm text-gray-300">{String(value)}</p>;
  };

  const fieldLabels: Record<string, string> = {
    title: '제목',
    date: '날짜',
    location: '장소',
    participants: '참석자',
    attendees: '참석자',
    parties: '참가자',
    purpose: '목적',
    content: '내용',
    keyPoints: '핵심 포인트',
    discussion: '논의 내용',
    agreements: '합의 사항',
    actionItems: '후속 조치',
    nextSteps: '다음 단계',
    nextMeeting: '다음 회의',
    conclusion: '결론',
    concerns: '우려 사항',
    interpreterNotes: '통역사 메모',
    summary: '요약',
    agenda: '안건',
  };

  if (status === 'loading' || isLoading) {
    return (
      <div className="min-h-screen bg-[#0f0f0f] flex items-center justify-center">
        <Loader2 className="w-8 h-8 animate-spin text-indigo-400" />
      </div>
    );
  }

  if (error) {
    return (
      <div className="min-h-screen bg-[#0f0f0f] flex items-center justify-center p-6">
        <div className="bg-[#1a1a1a] border border-[#2a2a2a] rounded-2xl p-8 max-w-md w-full text-center">
          <div className="w-16 h-16 bg-red-900/50 rounded-full flex items-center justify-center mx-auto mb-4">
            <AlertCircle className="w-8 h-8 text-red-400" />
          </div>
          <h1 className="text-xl font-bold text-gray-100 mb-2">오류</h1>
          <p className="text-gray-400 mb-6">{error}</p>
          <Link
            href="/reports"
            className="inline-block bg-indigo-600 text-white px-6 py-3 rounded-xl font-medium hover:bg-indigo-500 transition"
          >
            보고서 목록으로
          </Link>
        </div>
      </div>
    );
  }

  if (!report) return null;

  return (
    <div className="min-h-screen bg-[#0f0f0f]">
      {/* Header */}
      <header className="bg-[#1a1a1a] border-b border-[#2a2a2a] px-6 py-4">
        <div className="max-w-4xl mx-auto flex items-center justify-between">
          <div className="flex items-center gap-4">
            <Link href="/reports" className="text-gray-400 hover:text-gray-200">
              <ArrowLeft className="w-6 h-6" />
            </Link>
            <div>
              <h1 className="text-lg font-semibold text-gray-100">보고서 상세</h1>
              <p className="text-[10px] text-gray-600">Phiennoi by Epicstage Corp.</p>
            </div>
          </div>
          <div className="flex items-center gap-2">
            <button
              onClick={handleOpenShareModal}
              disabled={isSharing}
              className="flex items-center gap-2 bg-green-600 text-white px-4 py-2 rounded-lg font-medium hover:bg-green-500 transition disabled:opacity-50"
            >
              {isSharing ? (
                <Loader2 className="w-4 h-4 animate-spin" />
              ) : (
                <Share2 className="w-4 h-4" />
              )}
              공유
            </button>
            <button
              onClick={() => setShowSignature(true)}
              className="flex items-center gap-2 bg-indigo-600 text-white px-4 py-2 rounded-lg font-medium hover:bg-indigo-500 transition"
            >
              <Download className="w-4 h-4" />
              PDF
            </button>
            <button
              onClick={handleDelete}
              disabled={isDeleting}
              className="flex items-center gap-2 text-red-400 hover:text-red-300 px-3 py-2"
            >
              {isDeleting ? (
                <Loader2 className="w-4 h-4 animate-spin" />
              ) : (
                <Trash2 className="w-4 h-4" />
              )}
            </button>
          </div>
        </div>
      </header>

      <main className="max-w-4xl mx-auto px-6 py-6 space-y-6">
        {/* Report Header */}
        <div className="bg-[#1a1a1a] border border-[#2a2a2a] rounded-xl p-6">
          <div className="flex items-start gap-4">
            <div className="w-12 h-12 rounded-lg bg-indigo-900/50 flex items-center justify-center">
              <FileText className="w-6 h-6 text-indigo-400" />
            </div>
            <div className="flex-1">
              <h2 className="text-xl font-bold text-gray-100">
                {String(report.content.title || report.title || '제목 없음')}
              </h2>
              <div className="flex items-center gap-4 text-sm text-gray-500 mt-1">
                <span className="flex items-center gap-1">
                  <Clock className="w-4 h-4" />
                  {formatDate(report.created_at)}
                </span>
                <span className={`px-2 py-0.5 rounded-full ${
                  report.status === 'completed'
                    ? 'bg-green-900/50 text-green-400'
                    : 'bg-yellow-900/50 text-yellow-400'
                }`}>
                  {report.status === 'completed' ? '완료' : '임시저장'}
                </span>
              </div>
            </div>
          </div>
        </div>

        {/* Report Content */}
        <div className="bg-[#1a1a1a] border border-[#2a2a2a] rounded-xl p-6">
          <h3 className="font-semibold text-gray-100 mb-4">보고서 내용</h3>
          <div className="space-y-6 bg-[#0f0f0f] rounded-xl p-4">
            {Object.entries(report.content).map(([key, value]) => {
              if (key === 'format') return null;
              const label = fieldLabels[key] || key;
              const renderedValue = renderValue(value);
              if (!renderedValue) return null;

              return (
                <div key={key}>
                  <h4 className="text-xs font-semibold text-gray-500 uppercase tracking-wide mb-2">
                    {label}
                  </h4>
                  {renderedValue}
                </div>
              );
            })}
          </div>
        </div>

        {/* Transcript */}
        {report.transcript && (
          <div className="bg-[#1a1a1a] border border-[#2a2a2a] rounded-xl p-6">
            <h3 className="font-semibold text-gray-100 mb-4">원본 전사</h3>
            <div className="bg-[#0f0f0f] rounded-xl p-4 max-h-60 overflow-y-auto">
              <p className="text-sm text-gray-400 whitespace-pre-wrap">
                {report.transcript}
              </p>
            </div>
          </div>
        )}

        {/* Footer */}
        <footer className="text-center py-4 mt-6">
          <p className="text-xs text-gray-600">© 2025 Epicstage Corp.</p>
        </footer>
      </main>

      {/* Signature Modal */}
      {showSignature && (
        <div className="fixed inset-0 bg-black/70 flex items-center justify-center p-6 z-50">
          <div className="bg-[#1a1a1a] border border-[#2a2a2a] rounded-2xl p-6 w-full max-w-md">
            <h3 className="text-lg font-semibold text-gray-100 mb-4">서명 후 다운로드</h3>
            <p className="text-sm text-gray-500 mb-4">
              아래 영역에 서명해주세요.
            </p>

            <div className="border-2 border-[#3a3a3a] rounded-xl overflow-hidden mb-4">
              <canvas
                ref={signatureCanvasRef}
                width={350}
                height={150}
                className="w-full touch-none bg-[#1a1a1a]"
                onMouseDown={startDrawing}
                onMouseMove={draw}
                onMouseUp={stopDrawing}
                onMouseLeave={stopDrawing}
                onTouchStart={startDrawing}
                onTouchMove={draw}
                onTouchEnd={stopDrawing}
              />
            </div>

            <button
              onClick={clearSignature}
              className="text-sm text-gray-500 hover:text-gray-300 mb-4"
            >
              서명 지우기
            </button>

            <div className="flex gap-3">
              <button
                onClick={() => setShowSignature(false)}
                className="flex-1 bg-[#242424] text-gray-300 py-3 rounded-xl font-medium hover:bg-[#2a2a2a] transition"
              >
                취소
              </button>
              <button
                onClick={handleDownloadPDF}
                disabled={!signature || isDownloading}
                className="flex-1 bg-indigo-600 text-white py-3 rounded-xl font-medium hover:bg-indigo-500 transition disabled:opacity-50 disabled:cursor-not-allowed flex items-center justify-center gap-2"
              >
                {isDownloading ? (
                  <>
                    <Loader2 className="w-5 h-5 animate-spin" />
                    생성 중...
                  </>
                ) : (
                  <>
                    <Download className="w-5 h-5" />
                    다운로드
                  </>
                )}
              </button>
            </div>
          </div>
        </div>
      )}

      {/* Share Modal */}
      {showShareModal && (
        <div className="fixed inset-0 bg-black/70 flex items-end sm:items-center justify-center p-0 sm:p-6 z-50">
          <div className="bg-[#1a1a1a] border border-[#2a2a2a] rounded-t-2xl sm:rounded-2xl p-6 w-full sm:max-w-md">
            <div className="flex justify-between items-center mb-6">
              <h3 className="text-lg font-semibold text-gray-100">PDF 공유하기</h3>
              <button
                onClick={() => setShowShareModal(false)}
                className="text-gray-500 hover:text-gray-300"
              >
                <X className="w-5 h-5" />
              </button>
            </div>

            <div className="space-y-3">
              {/* Native Share - 모바일에서 우선 표시 */}
              <button
                onClick={handleNativeShare}
                className="w-full flex items-center gap-4 bg-[#242424] hover:bg-[#2a2a2a] rounded-xl p-4 transition"
              >
                <div className="w-12 h-12 rounded-full bg-blue-600 flex items-center justify-center">
                  <Send className="w-6 h-6 text-white" />
                </div>
                <div className="text-left">
                  <p className="font-medium text-gray-100">앱으로 공유</p>
                  <p className="text-sm text-gray-500">설치된 앱으로 PDF 파일 공유</p>
                </div>
              </button>

              {/* Zalo */}
              <button
                onClick={handleZaloShare}
                className="w-full flex items-center gap-4 bg-[#242424] hover:bg-[#2a2a2a] rounded-xl p-4 transition"
              >
                <div className="w-12 h-12 rounded-full bg-blue-500 flex items-center justify-center">
                  <span className="text-white font-bold text-lg">Z</span>
                </div>
                <div className="text-left">
                  <p className="font-medium text-gray-100">Zalo</p>
                  <p className="text-sm text-gray-500">Zalo로 링크 공유</p>
                </div>
              </button>

              {/* WhatsApp */}
              <button
                onClick={handleWhatsAppShare}
                className="w-full flex items-center gap-4 bg-[#242424] hover:bg-[#2a2a2a] rounded-xl p-4 transition"
              >
                <div className="w-12 h-12 rounded-full bg-green-500 flex items-center justify-center">
                  <MessageCircle className="w-6 h-6 text-white" />
                </div>
                <div className="text-left">
                  <p className="font-medium text-gray-100">WhatsApp</p>
                  <p className="text-sm text-gray-500">WhatsApp으로 링크 공유</p>
                </div>
              </button>

              {/* KakaoTalk */}
              <button
                onClick={handleKakaoShare}
                className="w-full flex items-center gap-4 bg-[#242424] hover:bg-[#2a2a2a] rounded-xl p-4 transition"
              >
                <div className="w-12 h-12 rounded-full bg-yellow-400 flex items-center justify-center">
                  <MessageCircle className="w-6 h-6 text-yellow-900" />
                </div>
                <div className="text-left">
                  <p className="font-medium text-gray-100">카카오톡</p>
                  <p className="text-sm text-gray-500">카카오스토리로 링크 공유</p>
                </div>
              </button>

              {/* Save to device */}
              <button
                onClick={handleSavePDF}
                className="w-full flex items-center gap-4 bg-[#242424] hover:bg-[#2a2a2a] rounded-xl p-4 transition"
              >
                <div className="w-12 h-12 rounded-full bg-gray-600 flex items-center justify-center">
                  <FolderDown className="w-6 h-6 text-white" />
                </div>
                <div className="text-left">
                  <p className="font-medium text-gray-100">파일로 저장</p>
                  <p className="text-sm text-gray-500">기기에 PDF 파일 다운로드</p>
                </div>
              </button>
            </div>

            <p className="text-xs text-gray-600 text-center mt-4">
              * Zalo, WhatsApp, 카카오톡은 링크만 공유됩니다
            </p>
          </div>
        </div>
      )}
    </div>
  );
}
