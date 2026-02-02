'use client';

import { useState, useRef, useEffect, useCallback } from 'react';
import Link from 'next/link';
import Image from 'next/image';
import html2canvas from 'html2canvas';
import { jsPDF } from 'jspdf';
import {
  ArrowLeft,
  Mic,
  Square,
  Upload,
  FileText,
  ChevronRight,
  Loader2,
  Play,
  Pause,
  X,
  AlertCircle,
  Download,
  Image as ImageIcon,
  CreditCard,
  Check,
  LayoutTemplate,
} from 'lucide-react';
import { REPORT_TEMPLATES, getTemplateById, type ReportTemplate } from '@/lib/templates';
import { TemplateRenderer, getEmptyTemplateData } from '@/components/templates';

type Step = 'template' | 'form' | 'audio' | 'generate' | 'preview' | 'sign';

interface FieldPosition {
  label: string;
  x: number;
  y: number;
  width: number;
  height: number;
  type: 'text' | 'date' | 'signature' | 'checkbox' | 'multiline';
  value?: string;
}

interface FormAnalysis {
  fields: FieldPosition[];
  hasSignature: boolean;
  signaturePosition?: FieldPosition;
  pageWidth: number;
  pageHeight: number;
}

interface BusinessCard {
  companyName?: string;
  personName?: string;
  position?: string;
  phone?: string;
  email?: string;
  address?: string;
}

export default function NewReportPage() {
  // Step management
  const [currentStep, setCurrentStep] = useState<Step>('template');

  // Template state
  const [selectedTemplate, setSelectedTemplate] = useState<ReportTemplate | null>(null);
  const [useCustomForm, setUseCustomForm] = useState(false);
  const [templateCategory, setTemplateCategory] = useState<'all' | 'tech' | 'beauty' | 'trade' | 'general'>('all');
  const [templateFormData, setTemplateFormData] = useState<Record<string, string>>({});

  // Form/Business card state
  const [formImage, setFormImage] = useState<File | null>(null);
  const [formImageUrl, setFormImageUrl] = useState<string | null>(null);
  const [businessCardImage, setBusinessCardImage] = useState<File | null>(null);
  const [businessCardUrl, setBusinessCardUrl] = useState<string | null>(null);
  const [isAnalyzing, setIsAnalyzing] = useState(false);
  const [formAnalysis, setFormAnalysis] = useState<FormAnalysis | null>(null);
  const [businessCard, setBusinessCard] = useState<BusinessCard | null>(null);
  const [analyzeError, setAnalyzeError] = useState<string | null>(null);

  // Audio state
  const [isRecording, setIsRecording] = useState(false);
  const [recordingTime, setRecordingTime] = useState(0);
  const [audioFile, setAudioFile] = useState<File | null>(null);
  const [audioUrl, setAudioUrl] = useState<string | null>(null);
  const [isPlaying, setIsPlaying] = useState(false);
  const [permissionDenied, setPermissionDenied] = useState(false);
  const [audioProgress, setAudioProgress] = useState(0);
  const [audioDuration, setAudioDuration] = useState(0);
  const [isTranscribing, setIsTranscribing] = useState(false);
  const [transcript, setTranscript] = useState<string | null>(null);
  const [transcribeError, setTranscribeError] = useState<string | null>(null);
  const [selectedLanguage, setSelectedLanguage] = useState<'ko-KR' | 'vi-VN'>('ko-KR');

  // Generate state
  const [isGenerating, setIsGenerating] = useState(false);
  const [filledFields, setFilledFields] = useState<FieldPosition[]>([]);
  const [generateError, setGenerateError] = useState<string | null>(null);

  // Signature state
  const [signature, setSignature] = useState<string | null>(null);
  const [isDrawing, setIsDrawing] = useState(false);
  const [isDownloading, setIsDownloading] = useState(false);

  // Refs
  const formInputRef = useRef<HTMLInputElement>(null);
  const cardInputRef = useRef<HTMLInputElement>(null);
  const audioInputRef = useRef<HTMLInputElement>(null);
  const audioRef = useRef<HTMLAudioElement>(null);
  const mediaRecorderRef = useRef<MediaRecorder | null>(null);
  const audioChunksRef = useRef<Blob[]>([]);
  const timerRef = useRef<NodeJS.Timeout | null>(null);
  const signatureCanvasRef = useRef<HTMLCanvasElement>(null);

  const formatTime = (seconds: number) => {
    const mins = Math.floor(seconds / 60);
    const secs = Math.floor(seconds % 60);
    return `${mins.toString().padStart(2, '0')}:${secs.toString().padStart(2, '0')}`;
  };

  // Cleanup
  useEffect(() => {
    return () => {
      if (timerRef.current) clearInterval(timerRef.current);
      if (mediaRecorderRef.current?.state === 'recording') mediaRecorderRef.current.stop();
      if (formImageUrl) URL.revokeObjectURL(formImageUrl);
      if (businessCardUrl) URL.revokeObjectURL(businessCardUrl);
      if (audioUrl) URL.revokeObjectURL(audioUrl);
    };
  }, [formImageUrl, businessCardUrl, audioUrl]);

  // Form image handlers
  const handleFormImageUpload = (e: React.ChangeEvent<HTMLInputElement>) => {
    const file = e.target.files?.[0];
    if (file) {
      if (formImageUrl) URL.revokeObjectURL(formImageUrl);
      setFormImage(file);
      setFormImageUrl(URL.createObjectURL(file));
      setFormAnalysis(null);
    }
  };

  const handleBusinessCardUpload = (e: React.ChangeEvent<HTMLInputElement>) => {
    const file = e.target.files?.[0];
    if (file) {
      if (businessCardUrl) URL.revokeObjectURL(businessCardUrl);
      setBusinessCardImage(file);
      setBusinessCardUrl(URL.createObjectURL(file));
      setBusinessCard(null);
    }
  };

  const handleAnalyzeForm = async () => {
    if (!formImage) return;

    setIsAnalyzing(true);
    setAnalyzeError(null);

    try {
      const formData = new FormData();
      formData.append('formImage', formImage);
      formData.append('type', businessCardImage ? 'both' : 'form');
      if (businessCardImage) {
        formData.append('businessCardImage', businessCardImage);
      }

      const response = await fetch('/api/analyze-form', {
        method: 'POST',
        body: formData,
      });

      interface FormResult {
        error?: string;
        form?: FormAnalysis;
        fields?: FieldPosition[];
        businessCard?: BusinessCard;
      }
      const result = await response.json() as FormResult;

      if (!response.ok) {
        throw new Error(result.error || '양식 분석에 실패했습니다.');
      }

      if (result.form) {
        setFormAnalysis(result.form);
      } else if (result.fields) {
        setFormAnalysis({
          fields: result.fields,
          hasSignature: false,
          pageWidth: 595,
          pageHeight: 842,
        });
      }

      if (result.businessCard) {
        setBusinessCard(result.businessCard);
      }

      setCurrentStep('audio');
    } catch (error) {
      setAnalyzeError(error instanceof Error ? error.message : '양식 분석 중 오류가 발생했습니다.');
    } finally {
      setIsAnalyzing(false);
    }
  };

  // Audio handlers
  const handleStartRecording = async () => {
    try {
      setPermissionDenied(false);
      const stream = await navigator.mediaDevices.getUserMedia({ audio: true });

      const mimeType = MediaRecorder.isTypeSupported('audio/webm;codecs=opus')
        ? 'audio/webm;codecs=opus'
        : MediaRecorder.isTypeSupported('audio/webm')
        ? 'audio/webm'
        : 'audio/mp4';

      const mediaRecorder = new MediaRecorder(stream, { mimeType });
      mediaRecorderRef.current = mediaRecorder;
      audioChunksRef.current = [];

      mediaRecorder.ondataavailable = (event) => {
        if (event.data.size > 0) audioChunksRef.current.push(event.data);
      };

      mediaRecorder.onstop = () => {
        const audioBlob = new Blob(audioChunksRef.current, { type: mimeType });
        const url = URL.createObjectURL(audioBlob);
        const file = new File([audioBlob], `recording-${Date.now()}.webm`, { type: mimeType });
        setAudioFile(file);
        setAudioUrl(url);
        stream.getTracks().forEach(track => track.stop());
      };

      mediaRecorder.start(1000);
      setIsRecording(true);
      setRecordingTime(0);

      timerRef.current = setInterval(() => {
        setRecordingTime(prev => prev + 1);
      }, 1000);
    } catch (error) {
      console.error('Recording error:', error);
      if (error instanceof DOMException && error.name === 'NotAllowedError') {
        setPermissionDenied(true);
      }
    }
  };

  const handleStopRecording = useCallback(() => {
    if (mediaRecorderRef.current?.state === 'recording') {
      mediaRecorderRef.current.stop();
    }
    if (timerRef.current) {
      clearInterval(timerRef.current);
      timerRef.current = null;
    }
    setIsRecording(false);
  }, []);

  const handleAudioUpload = (e: React.ChangeEvent<HTMLInputElement>) => {
    const file = e.target.files?.[0];
    if (file) {
      setAudioFile(file);
      setAudioUrl(URL.createObjectURL(file));
    }
  };

  const handleRemoveAudio = () => {
    if (audioUrl) URL.revokeObjectURL(audioUrl);
    setAudioFile(null);
    setAudioUrl(null);
    setRecordingTime(0);
    setAudioProgress(0);
    setAudioDuration(0);
    setIsPlaying(false);
  };

  const handlePlayPause = () => {
    if (audioRef.current) {
      if (isPlaying) {
        audioRef.current.pause();
      } else {
        audioRef.current.play();
      }
      setIsPlaying(!isPlaying);
    }
  };

  const handleTranscribeAndGenerate = async () => {
    if (!audioFile || !formAnalysis) return;

    setIsTranscribing(true);
    setTranscribeError(null);

    try {
      // Step 1: Transcribe
      const formData = new FormData();
      formData.append('audio', audioFile);
      formData.append('language', selectedLanguage);

      const transcribeRes = await fetch('/api/transcribe', {
        method: 'POST',
        body: formData,
      });

      const transcribeResult = await transcribeRes.json() as { error?: string; transcript?: string };

      if (!transcribeRes.ok) {
        throw new Error(transcribeResult.error || '전사에 실패했습니다.');
      }

      setTranscript(transcribeResult.transcript || null);
      setCurrentStep('generate');
      setIsTranscribing(false);

      // Step 2: Generate field content using AI
      setIsGenerating(true);
      setGenerateError(null);

      const generateRes = await fetch('/api/generate-report', {
        method: 'POST',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify({
          transcript: transcribeResult.transcript,
          templateType: 'custom',
          customFields: formAnalysis.fields.map(f => f.label),
          language: selectedLanguage === 'ko-KR' ? 'ko' : 'vi',
          businessCard: businessCard,
        }),
      });

      const generateResult = await generateRes.json() as { error?: string; report?: Record<string, unknown> };

      if (!generateRes.ok) {
        throw new Error(generateResult.error || '보고서 생성에 실패했습니다.');
      }

      // Map AI output to form fields
      const report = generateResult.report || {};
      const filled = formAnalysis.fields.map(field => {
        let value = '';

        // Try to match field label with report keys
        const labelLower = field.label.toLowerCase();
        for (const [key, val] of Object.entries(report)) {
          const keyLower = key.toLowerCase();
          if (labelLower.includes(keyLower) || keyLower.includes(labelLower)) {
            value = typeof val === 'string' ? val : JSON.stringify(val);
            break;
          }
        }

        // Special mappings for business card
        if (businessCard) {
          if (labelLower.includes('회사') || labelLower.includes('company')) {
            value = businessCard.companyName || value;
          }
          if (labelLower.includes('담당') || labelLower.includes('이름') || labelLower.includes('name')) {
            value = businessCard.personName || value;
          }
          if (labelLower.includes('연락') || labelLower.includes('전화') || labelLower.includes('phone')) {
            value = businessCard.phone || value;
          }
          if (labelLower.includes('이메일') || labelLower.includes('email')) {
            value = businessCard.email || value;
          }
        }

        return { ...field, value };
      });

      setFilledFields(filled);
      setCurrentStep('preview');
    } catch (error) {
      if (isTranscribing) {
        setTranscribeError(error instanceof Error ? error.message : '오류가 발생했습니다.');
      } else {
        setGenerateError(error instanceof Error ? error.message : '오류가 발생했습니다.');
      }
    } finally {
      setIsTranscribing(false);
      setIsGenerating(false);
    }
  };

  // Signature handlers
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
    if (currentStep === 'sign' && signatureCanvasRef.current) {
      const canvas = signatureCanvasRef.current;
      const ctx = canvas.getContext('2d');
      if (ctx) {
        ctx.fillStyle = '#1a1a1a';
        ctx.fillRect(0, 0, canvas.width, canvas.height);
      }
    }
  }, [currentStep]);

  // PDF download for custom form
  const handleDownloadPDF = async () => {
    if (!formImage || filledFields.length === 0) return;

    setIsDownloading(true);

    try {
      const formData = new FormData();
      formData.append('formImage', formImage);
      formData.append('fields', JSON.stringify(filledFields));
      formData.append('pageWidth', String(formAnalysis?.pageWidth || 595));
      formData.append('pageHeight', String(formAnalysis?.pageHeight || 842));

      if (signature && formAnalysis?.hasSignature) {
        formData.append('signatureImage', signature);
      }

      const response = await fetch('/api/generate-pdf', {
        method: 'POST',
        body: formData,
      });

      if (!response.ok) {
        const errorData = await response.json() as { error?: string };
        throw new Error(errorData.error || 'PDF 생성에 실패했습니다.');
      }

      const blob = await response.blob();
      const url = URL.createObjectURL(blob);
      const a = document.createElement('a');
      a.href = url;
      a.download = `report-${Date.now()}.pdf`;
      document.body.appendChild(a);
      a.click();
      document.body.removeChild(a);
      URL.revokeObjectURL(url);
    } catch (error) {
      console.error('PDF download error:', error);
      alert(error instanceof Error ? error.message : 'PDF 다운로드 중 오류가 발생했습니다.');
    } finally {
      setIsDownloading(false);
    }
  };

  // Ref for the template print container
  const templatePrintRef = useRef<HTMLDivElement>(null);

  // PDF download for template-based reports (client-side)
  const handleDownloadTemplatePDF = async () => {
    if (!selectedTemplate || !templatePrintRef.current) return;

    setIsDownloading(true);

    try {
      // Get the print container element
      const element = templatePrintRef.current;

      // Use html2canvas to capture the element as an image
      const canvas = await html2canvas(element, {
        scale: 2, // Higher resolution
        useCORS: true,
        logging: false,
        backgroundColor: '#ffffff',
        width: element.scrollWidth,
        height: element.scrollHeight,
      });

      // Get image dimensions
      const imgWidth = 210; // A4 width in mm
      const imgHeight = (canvas.height * imgWidth) / canvas.width;

      // Create PDF
      const pdf = new jsPDF({
        orientation: imgHeight > imgWidth ? 'portrait' : 'landscape',
        unit: 'mm',
        format: 'a4',
      });

      // Calculate pages needed
      const pageHeight = 297; // A4 height in mm
      let heightLeft = imgHeight;
      let position = 0;

      // Add image to first page
      const imgData = canvas.toDataURL('image/png');
      pdf.addImage(imgData, 'PNG', 0, position, imgWidth, imgHeight);
      heightLeft -= pageHeight;

      // Add additional pages if needed
      while (heightLeft > 0) {
        position = heightLeft - imgHeight;
        pdf.addPage();
        pdf.addImage(imgData, 'PNG', 0, position, imgWidth, imgHeight);
        heightLeft -= pageHeight;
      }

      // Add signature if present
      if (signature) {
        // Get last page
        const pageCount = pdf.getNumberOfPages();
        pdf.setPage(pageCount);

        // Add signature at bottom right
        const signatureImg = new window.Image();
        signatureImg.src = signature;
        await new Promise((resolve) => {
          signatureImg.onload = resolve;
        });

        // Add signature (positioned at bottom-right area)
        pdf.addImage(signature, 'PNG', imgWidth - 60, pageHeight - 40, 50, 25);
      }

      // Download the PDF
      pdf.save(`${selectedTemplate.id}-${Date.now()}.pdf`);
    } catch (error) {
      console.error('PDF download error:', error);
      alert(error instanceof Error ? error.message : 'PDF 다운로드 중 오류가 발생했습니다.');
    } finally {
      setIsDownloading(false);
    }
  };

  return (
    <div className="min-h-screen bg-[#0f0f0f]">
      {/* Header */}
      <header className="bg-[#1a1a1a] border-b border-[#2a2a2a] px-6 py-4">
        <div className="max-w-4xl mx-auto flex items-center gap-4">
          <Link href="/dashboard" className="text-gray-400 hover:text-gray-200">
            <ArrowLeft className="w-6 h-6" />
          </Link>
          <div>
            <h1 className="text-lg font-semibold text-gray-100">새 보고서</h1>
            <p className="text-[10px] text-gray-600">Phiennoi by Epicstage Corp.</p>
          </div>
        </div>
      </header>

      {/* Progress Steps */}
      <div className="bg-[#1a1a1a] border-b border-[#2a2a2a]">
        <div className="max-w-4xl mx-auto px-6 py-4">
          <div className="flex items-center justify-between">
            <StepIndicator step={1} label="템플릿" active={currentStep === 'template'} completed={!!selectedTemplate || useCustomForm} />
            <StepConnector active={!!selectedTemplate || useCustomForm} />
            <StepIndicator step={2} label="양식" active={currentStep === 'form'} completed={!!formAnalysis || Object.keys(templateFormData).length > 0} />
            <StepConnector active={!!formAnalysis || Object.keys(templateFormData).length > 0} />
            <StepIndicator step={3} label="녹음" active={currentStep === 'audio'} completed={!!transcript} />
            <StepConnector active={!!transcript} />
            <StepIndicator step={4} label="생성" active={currentStep === 'generate'} completed={filledFields.length > 0} />
            <StepConnector active={filledFields.length > 0} />
            <StepIndicator step={5} label="완료" active={currentStep === 'preview' || currentStep === 'sign'} completed={!!signature} />
          </div>
        </div>
      </div>

      <main className="max-w-4xl mx-auto px-6 py-6">
        {/* Step 1: Template Selection */}
        {currentStep === 'template' && (
          <div className="space-y-6">
            <div className="bg-[#1a1a1a] border border-[#2a2a2a] rounded-2xl p-6">
              <h2 className="text-lg font-semibold text-gray-100 mb-4 flex items-center gap-2">
                <LayoutTemplate className="w-5 h-5 text-indigo-400" />
                보고서 템플릿 선택
              </h2>
              <p className="text-sm text-gray-500 mb-6">
                미리 정의된 템플릿을 선택하거나, 직접 양식을 업로드하세요.
              </p>

              {/* Category Tabs */}
              <div className="flex gap-2 mb-6 overflow-x-auto pb-2">
                {[
                  { id: 'all', label: '전체', labelVi: 'Tất cả' },
                  { id: 'tech', label: '기술/IT', labelVi: 'Công nghệ' },
                  { id: 'beauty', label: '뷰티', labelVi: 'Làm đẹp' },
                  { id: 'general', label: '일반', labelVi: 'Chung' },
                ].map((cat) => (
                  <button
                    key={cat.id}
                    onClick={() => setTemplateCategory(cat.id as typeof templateCategory)}
                    className={`px-4 py-2 rounded-lg text-sm font-medium whitespace-nowrap transition ${
                      templateCategory === cat.id
                        ? 'bg-indigo-600 text-white'
                        : 'bg-[#242424] text-gray-400 hover:bg-[#2a2a2a]'
                    }`}
                  >
                    {cat.label}
                  </button>
                ))}
              </div>

              {/* Template Grid */}
              <div className="grid grid-cols-1 sm:grid-cols-2 gap-4">
                {REPORT_TEMPLATES.filter(
                  (t) => templateCategory === 'all' || t.category === templateCategory
                ).map((template) => (
                  <button
                    key={template.id}
                    onClick={() => {
                      setSelectedTemplate(template);
                      setUseCustomForm(false);
                      setTemplateFormData({});
                    }}
                    className={`relative p-4 rounded-xl border-2 text-left transition ${
                      selectedTemplate?.id === template.id
                        ? 'border-indigo-500 bg-indigo-900/20'
                        : 'border-[#2a2a2a] hover:border-[#3a3a3a] bg-[#1a1a1a]'
                    }`}
                  >
                    {/* Template Preview */}
                    <div className="relative w-full h-40 mb-3 rounded-lg overflow-hidden bg-white">
                      <div className="transform scale-[0.2] origin-top-left w-[500%] h-[500%]">
                        <TemplateRenderer
                          templateId={template.id}
                          formData={getEmptyTemplateData(template.id)}
                          mode="preview"
                        />
                      </div>
                    </div>
                    <h3 className="font-medium text-gray-100 mb-1">{template.name}</h3>
                    <p className="text-xs text-gray-500 mb-2">{template.nameVi}</p>
                    <p className="text-sm text-gray-400 line-clamp-2">{template.description}</p>
                    <div className="mt-2 flex items-center gap-2">
                      <span className="text-xs px-2 py-1 rounded bg-[#242424] text-gray-500">
                        {template.fields.length}개 필드
                      </span>
                      <span className={`text-xs px-2 py-1 rounded ${
                        template.category === 'tech' ? 'bg-blue-900/50 text-blue-400' :
                        template.category === 'beauty' ? 'bg-pink-900/50 text-pink-400' :
                        'bg-gray-800 text-gray-400'
                      }`}>
                        {template.category === 'tech' ? '기술' :
                         template.category === 'beauty' ? '뷰티' : '일반'}
                      </span>
                    </div>
                    {selectedTemplate?.id === template.id && (
                      <div className="absolute top-2 right-2 w-6 h-6 bg-indigo-500 rounded-full flex items-center justify-center">
                        <Check className="w-4 h-4 text-white" />
                      </div>
                    )}
                  </button>
                ))}
              </div>
            </div>

            {/* Custom Form Option */}
            <div className="relative">
              <div className="absolute inset-0 flex items-center">
                <div className="w-full border-t border-[#2a2a2a]" />
              </div>
              <div className="relative flex justify-center">
                <span className="px-4 bg-[#0f0f0f] text-sm text-gray-500">또는</span>
              </div>
            </div>

            <button
              onClick={() => {
                setSelectedTemplate(null);
                setUseCustomForm(true);
                setCurrentStep('form');
              }}
              className="w-full bg-[#1a1a1a] border-2 border-dashed border-[#3a3a3a] rounded-xl p-6 text-center hover:border-indigo-500 hover:bg-indigo-900/10 transition"
            >
              <Upload className="w-8 h-8 text-gray-500 mx-auto mb-2" />
              <p className="text-gray-400 font-medium">직접 양식 업로드</p>
              <p className="text-sm text-gray-600 mt-1">기존 양식 이미지를 촬영하거나 업로드</p>
            </button>

            {/* Next Button */}
            <button
              onClick={() => setCurrentStep('form')}
              disabled={!selectedTemplate}
              className="w-full bg-indigo-600 text-white py-3 rounded-xl font-medium hover:bg-indigo-500 transition disabled:opacity-50 disabled:cursor-not-allowed flex items-center justify-center gap-2"
            >
              {selectedTemplate ? (
                <>
                  템플릿으로 시작하기
                  <ChevronRight className="w-5 h-5" />
                </>
              ) : (
                '템플릿을 선택해주세요'
              )}
            </button>
          </div>
        )}

        {/* Step 2: Form Upload or Template Fields */}
        {currentStep === 'form' && (
          <div className="space-y-6">
            {/* Template Form Mode */}
            {selectedTemplate && !useCustomForm ? (
              <>
                {/* Template Header */}
                <div className="bg-[#1a1a1a] border border-[#2a2a2a] rounded-2xl p-6">
                  <div className="flex items-start gap-4 mb-6">
                    <div className="relative w-24 h-32 rounded-lg overflow-hidden bg-white flex-shrink-0">
                      <div className="transform scale-[0.12] origin-top-left w-[833%] h-[833%]">
                        <TemplateRenderer
                          templateId={selectedTemplate.id}
                          formData={Object.keys(templateFormData).length > 0 ? templateFormData : getEmptyTemplateData(selectedTemplate.id)}
                          mode="preview"
                        />
                      </div>
                    </div>
                    <div>
                      <h2 className="text-lg font-semibold text-gray-100">{selectedTemplate.name}</h2>
                      <p className="text-sm text-gray-500">{selectedTemplate.nameVi}</p>
                      <p className="text-sm text-gray-400 mt-1">{selectedTemplate.description}</p>
                    </div>
                  </div>

                  {/* Group fields by section */}
                  {(() => {
                    const sections: Record<string, typeof selectedTemplate.fields> = {};
                    selectedTemplate.fields.forEach((field) => {
                      const section = field.section || 'default';
                      if (!sections[section]) sections[section] = [];
                      sections[section].push(field);
                    });

                    const sectionLabels: Record<string, { ko: string; vi: string }> = {
                      basic: { ko: '기본 정보', vi: 'Thông tin cơ bản' },
                      buyer: { ko: '바이어 정보', vi: 'Thông tin người mua' },
                      buyer1: { ko: '바이어 정보', vi: 'Thông tin người mua' },
                      consult: { ko: '상담 유형', vi: 'Loại tư vấn' },
                      result: { ko: '상담 결과', vi: 'Kết quả tư vấn' },
                      rating: { ko: '상담 평가', vi: 'Đánh giá' },
                      export: { ko: '수출/계약', vi: 'Xuất khẩu/Hợp đồng' },
                      content: { ko: '상담 내용', vi: 'Nội dung' },
                      participants: { ko: '참석자', vi: 'Người tham dự' },
                      default: { ko: '기타', vi: 'Khác' },
                    };

                    return Object.entries(sections).map(([sectionKey, fields]) => (
                      <div key={sectionKey} className="mb-6 last:mb-0">
                        <h3 className="text-sm font-medium text-indigo-400 mb-3 border-b border-[#2a2a2a] pb-2">
                          {sectionLabels[sectionKey]?.ko || sectionKey}
                          <span className="text-gray-600 ml-2">
                            {sectionLabels[sectionKey]?.vi || ''}
                          </span>
                        </h3>
                        <div className="grid grid-cols-1 sm:grid-cols-2 gap-4">
                          {fields.map((field) => (
                            <div key={field.id} className={field.type === 'textarea' ? 'sm:col-span-2' : ''}>
                              <label className="block text-sm text-gray-300 mb-1">
                                {field.label}
                                {field.labelVi && <span className="text-gray-600 ml-2">({field.labelVi})</span>}
                                {field.required && <span className="text-red-400 ml-1">*</span>}
                              </label>
                              {field.type === 'textarea' ? (
                                <textarea
                                  value={templateFormData[field.id] || ''}
                                  onChange={(e) => setTemplateFormData(prev => ({
                                    ...prev,
                                    [field.id]: e.target.value
                                  }))}
                                  placeholder={field.placeholder}
                                  rows={3}
                                  className="w-full border border-[#3a3a3a] bg-[#242424] rounded-lg p-3 text-sm text-gray-200 placeholder-gray-600 focus:ring-2 focus:ring-indigo-500 focus:border-transparent"
                                />
                              ) : field.type === 'select' ? (
                                <select
                                  value={templateFormData[field.id] || ''}
                                  onChange={(e) => setTemplateFormData(prev => ({
                                    ...prev,
                                    [field.id]: e.target.value
                                  }))}
                                  className="w-full border border-[#3a3a3a] bg-[#242424] rounded-lg p-3 text-sm text-gray-200 focus:ring-2 focus:ring-indigo-500 focus:border-transparent"
                                >
                                  <option value="">선택해주세요</option>
                                  {field.options?.map((opt) => (
                                    <option key={opt} value={opt}>{opt}</option>
                                  ))}
                                </select>
                              ) : field.type === 'rating' ? (
                                <div className="flex gap-1">
                                  {[1, 2, 3, 4, 5].map((star) => (
                                    <button
                                      key={star}
                                      type="button"
                                      onClick={() => setTemplateFormData(prev => ({
                                        ...prev,
                                        [field.id]: String(star)
                                      }))}
                                      className={`w-10 h-10 rounded-lg flex items-center justify-center text-lg transition ${
                                        Number(templateFormData[field.id]) >= star
                                          ? 'bg-yellow-500 text-white'
                                          : 'bg-[#242424] text-gray-600 hover:bg-[#2a2a2a]'
                                      }`}
                                    >
                                      ★
                                    </button>
                                  ))}
                                </div>
                              ) : (
                                <input
                                  type={field.type === 'date' ? 'date' : field.type === 'time' ? 'time' : field.type === 'number' ? 'number' : 'text'}
                                  value={templateFormData[field.id] || ''}
                                  onChange={(e) => setTemplateFormData(prev => ({
                                    ...prev,
                                    [field.id]: e.target.value
                                  }))}
                                  placeholder={field.placeholder}
                                  className="w-full border border-[#3a3a3a] bg-[#242424] rounded-lg p-3 text-sm text-gray-200 placeholder-gray-600 focus:ring-2 focus:ring-indigo-500 focus:border-transparent"
                                />
                              )}
                            </div>
                          ))}
                        </div>
                      </div>
                    ));
                  })()}
                </div>

                <div className="flex gap-3">
                  <button
                    onClick={() => {
                      setCurrentStep('template');
                      setSelectedTemplate(null);
                      setTemplateFormData({});
                    }}
                    className="flex-1 bg-[#242424] text-gray-300 py-3 rounded-xl font-medium hover:bg-[#2a2a2a] transition flex items-center justify-center gap-2"
                  >
                    <ArrowLeft className="w-4 h-4" />
                    템플릿 변경
                  </button>
                  <button
                    onClick={() => setCurrentStep('audio')}
                    className="flex-1 bg-indigo-600 text-white py-3 rounded-xl font-medium hover:bg-indigo-500 transition flex items-center justify-center gap-2"
                  >
                    녹음하기
                    <ChevronRight className="w-5 h-5" />
                  </button>
                </div>
              </>
            ) : (
              /* Custom Form Upload Mode */
              <>
                {/* Form Image Upload */}
                <div className="bg-[#1a1a1a] border border-[#2a2a2a] rounded-2xl p-6">
                  <h2 className="text-lg font-semibold text-gray-100 mb-4 flex items-center gap-2">
                    <ImageIcon className="w-5 h-5 text-indigo-400" />
                    양식 이미지 업로드
                  </h2>
                  <p className="text-sm text-gray-500 mb-4">
                    작성할 양식을 촬영하거나 업로드해주세요.
                  </p>

                  <input
                    type="file"
                    ref={formInputRef}
                    onChange={handleFormImageUpload}
                    accept="image/*"
                    capture="environment"
                    className="hidden"
                  />

                  {formImageUrl ? (
                    <div className="relative">
                      <img
                        src={formImageUrl}
                        alt="양식 미리보기"
                        className="w-full rounded-xl border border-[#2a2a2a]"
                      />
                      <button
                        onClick={() => {
                          if (formImageUrl) URL.revokeObjectURL(formImageUrl);
                          setFormImage(null);
                          setFormImageUrl(null);
                          setFormAnalysis(null);
                        }}
                        className="absolute top-2 right-2 bg-[#1a1a1a] rounded-full p-1 shadow-lg hover:bg-[#2a2a2a]"
                      >
                        <X className="w-5 h-5 text-gray-400" />
                      </button>
                    </div>
                  ) : (
                    <button
                      onClick={() => formInputRef.current?.click()}
                      className="w-full border-2 border-dashed border-[#3a3a3a] rounded-xl p-8 text-center hover:border-indigo-500 hover:bg-indigo-900/20 transition"
                    >
                      <Upload className="w-10 h-10 text-gray-500 mx-auto mb-3" />
                      <p className="text-gray-400">양식 이미지 선택</p>
                      <p className="text-sm text-gray-600 mt-1">PNG, JPG, HEIC 지원</p>
                    </button>
                  )}
                </div>

                {/* Business Card Upload (Optional) */}
                <div className="bg-[#1a1a1a] border border-[#2a2a2a] rounded-2xl p-6">
                  <h2 className="text-lg font-semibold text-gray-100 mb-4 flex items-center gap-2">
                    <CreditCard className="w-5 h-5 text-green-400" />
                    명함 이미지 (선택)
                  </h2>
                  <p className="text-sm text-gray-500 mb-4">
                    담당자 명함이 있다면 업로드해주세요. 자동으로 정보를 추출합니다.
                  </p>

                  <input
                    type="file"
                    ref={cardInputRef}
                    onChange={handleBusinessCardUpload}
                    accept="image/*"
                    capture="environment"
                    className="hidden"
                  />

                  {businessCardUrl ? (
                    <div className="relative">
                      <img
                        src={businessCardUrl}
                        alt="명함 미리보기"
                        className="w-full max-w-md rounded-xl border border-[#2a2a2a]"
                      />
                      <button
                        onClick={() => {
                          if (businessCardUrl) URL.revokeObjectURL(businessCardUrl);
                          setBusinessCardImage(null);
                          setBusinessCardUrl(null);
                          setBusinessCard(null);
                        }}
                        className="absolute top-2 right-2 bg-[#1a1a1a] rounded-full p-1 shadow-lg hover:bg-[#2a2a2a]"
                      >
                        <X className="w-5 h-5 text-gray-400" />
                      </button>
                    </div>
                  ) : (
                    <button
                      onClick={() => cardInputRef.current?.click()}
                      className="w-full border-2 border-dashed border-[#3a3a3a] rounded-xl p-6 text-center hover:border-green-500 hover:bg-green-900/20 transition"
                    >
                      <CreditCard className="w-8 h-8 text-gray-500 mx-auto mb-2" />
                      <p className="text-gray-400">명함 이미지 선택</p>
                    </button>
                  )}
                </div>

                {analyzeError && (
                  <div className="bg-red-900/30 border border-red-800/50 rounded-xl p-4 flex items-start gap-3">
                    <AlertCircle className="w-5 h-5 text-red-400 flex-shrink-0 mt-0.5" />
                    <div>
                      <p className="font-medium text-red-300">분석 실패</p>
                      <p className="text-sm text-red-400 mt-1">{analyzeError}</p>
                    </div>
                  </div>
                )}

                <div className="flex gap-3">
                  <button
                    onClick={() => {
                      setCurrentStep('template');
                      setUseCustomForm(false);
                    }}
                    className="flex-1 bg-[#242424] text-gray-300 py-3 rounded-xl font-medium hover:bg-[#2a2a2a] transition flex items-center justify-center gap-2"
                  >
                    <ArrowLeft className="w-4 h-4" />
                    템플릿 선택
                  </button>
                  <button
                    onClick={handleAnalyzeForm}
                    disabled={!formImage || isAnalyzing}
                    className="flex-1 bg-indigo-600 text-white py-3 rounded-xl font-medium hover:bg-indigo-500 transition disabled:opacity-50 disabled:cursor-not-allowed flex items-center justify-center gap-2"
                  >
                    {isAnalyzing ? (
                      <>
                        <Loader2 className="w-5 h-5 animate-spin" />
                        양식 분석 중...
                      </>
                    ) : (
                      <>
                        양식 분석하기
                        <ChevronRight className="w-5 h-5" />
                      </>
                    )}
                  </button>
                </div>
              </>
            )}
          </div>
        )}

        {/* Step 2: Audio Recording */}
        {currentStep === 'audio' && (
          <div className="space-y-6">
            {formAnalysis && (
              <div className="bg-green-900/30 border border-green-800/50 rounded-xl p-4">
                <div className="flex items-center gap-2 text-green-400 font-medium mb-2">
                  <Check className="w-5 h-5" />
                  양식 분석 완료
                </div>
                <p className="text-sm text-green-500">
                  {formAnalysis.fields.length}개 필드 감지됨
                  {formAnalysis.hasSignature && ' (서명란 포함)'}
                </p>
                {businessCard && (
                  <p className="text-sm text-green-500 mt-1">
                    명함: {businessCard.companyName} / {businessCard.personName}
                  </p>
                )}
              </div>
            )}

            {!audioUrl ? (
              <>
                {permissionDenied && (
                  <div className="bg-red-900/30 border border-red-800/50 rounded-xl p-4 flex items-start gap-3">
                    <AlertCircle className="w-5 h-5 text-red-400 flex-shrink-0 mt-0.5" />
                    <div>
                      <p className="font-medium text-red-300">마이크 권한이 필요합니다</p>
                      <p className="text-sm text-red-400 mt-1">
                        브라우저 설정에서 마이크 권한을 허용해주세요.
                      </p>
                    </div>
                  </div>
                )}

                <div className="bg-[#1a1a1a] border border-[#2a2a2a] rounded-2xl p-8">
                  <h2 className="text-lg font-semibold text-gray-100 text-center mb-6">음성 녹음</h2>

                  {isRecording ? (
                    <div className="text-center">
                      <div className="relative w-32 h-32 mx-auto mb-6">
                        <div className="absolute inset-0 bg-red-500/30 rounded-full animate-ping opacity-75" />
                        <div className="relative w-full h-full bg-red-500 rounded-full flex items-center justify-center">
                          <Mic className="w-12 h-12 text-white" />
                        </div>
                      </div>
                      <p className="text-3xl font-mono font-bold text-gray-100 mb-6">
                        {formatTime(recordingTime)}
                      </p>
                      <button
                        onClick={handleStopRecording}
                        className="inline-flex items-center gap-2 bg-gray-100 text-gray-900 px-6 py-3 rounded-xl font-medium hover:bg-gray-200 transition"
                      >
                        <Square className="w-5 h-5" fill="currentColor" />
                        녹음 중지
                      </button>
                    </div>
                  ) : (
                    <div className="text-center">
                      <button
                        onClick={handleStartRecording}
                        className="w-32 h-32 mx-auto mb-6 bg-red-500 rounded-full flex items-center justify-center hover:bg-red-600 transition shadow-lg"
                      >
                        <Mic className="w-12 h-12 text-white" />
                      </button>
                      <p className="text-gray-400">탭하여 녹음 시작</p>
                    </div>
                  )}
                </div>

                <div className="relative">
                  <div className="absolute inset-0 flex items-center">
                    <div className="w-full border-t border-[#2a2a2a]" />
                  </div>
                  <div className="relative flex justify-center">
                    <span className="px-4 bg-[#0f0f0f] text-sm text-gray-500">또는</span>
                  </div>
                </div>

                <div className="bg-[#1a1a1a] border border-[#2a2a2a] rounded-2xl p-6">
                  <input
                    type="file"
                    ref={audioInputRef}
                    onChange={handleAudioUpload}
                    accept="audio/*"
                    className="hidden"
                  />
                  <button
                    onClick={() => audioInputRef.current?.click()}
                    className="w-full border-2 border-dashed border-[#3a3a3a] rounded-xl p-6 text-center hover:border-indigo-500 hover:bg-indigo-900/20 transition"
                  >
                    <Upload className="w-8 h-8 text-gray-500 mx-auto mb-2" />
                    <p className="text-gray-400">음성 파일 업로드</p>
                  </button>
                </div>
              </>
            ) : (
              <div className="bg-[#1a1a1a] border border-[#2a2a2a] rounded-2xl p-6">
                <div className="flex items-center justify-between mb-4">
                  <h2 className="text-lg font-semibold text-gray-100">녹음 완료</h2>
                  <button onClick={handleRemoveAudio} className="text-gray-500 hover:text-red-400">
                    <X className="w-5 h-5" />
                  </button>
                </div>

                <div className="bg-[#242424] rounded-xl p-4 flex items-center gap-4">
                  <button
                    onClick={handlePlayPause}
                    className="w-12 h-12 bg-indigo-600 rounded-full flex items-center justify-center text-white hover:bg-indigo-500 transition flex-shrink-0"
                  >
                    {isPlaying ? <Pause className="w-5 h-5" /> : <Play className="w-5 h-5 ml-1" />}
                  </button>
                  <div className="flex-1">
                    <div className="h-2 bg-[#3a3a3a] rounded-full overflow-hidden">
                      <div
                        className="h-full bg-indigo-500 transition-all duration-100"
                        style={{ width: audioDuration > 0 ? `${(audioProgress / audioDuration) * 100}%` : '0%' }}
                      />
                    </div>
                    <div className="flex justify-between text-sm text-gray-500 mt-1">
                      <span>{formatTime(audioProgress)}</span>
                      <span>{formatTime(audioDuration || recordingTime)}</span>
                    </div>
                  </div>
                </div>

                {audioUrl && (
                  <audio
                    ref={audioRef}
                    src={audioUrl}
                    onEnded={() => setIsPlaying(false)}
                    onTimeUpdate={() => audioRef.current && setAudioProgress(audioRef.current.currentTime)}
                    onLoadedMetadata={() => audioRef.current && setAudioDuration(audioRef.current.duration)}
                  />
                )}

                {/* Language Selection */}
                <div className="mt-6">
                  <label className="block text-sm font-medium text-gray-300 mb-2">음성 언어</label>
                  <div className="flex gap-3">
                    <button
                      onClick={() => setSelectedLanguage('ko-KR')}
                      className={`flex-1 py-3 px-4 rounded-xl font-medium transition ${
                        selectedLanguage === 'ko-KR'
                          ? 'bg-indigo-600 text-white'
                          : 'bg-[#242424] text-gray-400 hover:bg-[#2a2a2a]'
                      }`}
                    >
                      한국어
                    </button>
                    <button
                      onClick={() => setSelectedLanguage('vi-VN')}
                      className={`flex-1 py-3 px-4 rounded-xl font-medium transition ${
                        selectedLanguage === 'vi-VN'
                          ? 'bg-indigo-600 text-white'
                          : 'bg-[#242424] text-gray-400 hover:bg-[#2a2a2a]'
                      }`}
                    >
                      Tiếng Việt
                    </button>
                  </div>
                </div>

                {(transcribeError || generateError) && (
                  <div className="mt-4 bg-red-900/30 border border-red-800/50 rounded-xl p-4">
                    <p className="text-red-400">{transcribeError || generateError}</p>
                  </div>
                )}

                <button
                  onClick={handleTranscribeAndGenerate}
                  disabled={isTranscribing || isGenerating}
                  className="w-full mt-6 bg-indigo-600 text-white py-3 rounded-xl font-medium hover:bg-indigo-500 transition disabled:opacity-50 flex items-center justify-center gap-2"
                >
                  {isTranscribing ? (
                    <>
                      <Loader2 className="w-5 h-5 animate-spin" />
                      음성 전사 중...
                    </>
                  ) : isGenerating ? (
                    <>
                      <Loader2 className="w-5 h-5 animate-spin" />
                      보고서 생성 중...
                    </>
                  ) : (
                    <>
                      보고서 생성하기
                      <ChevronRight className="w-5 h-5" />
                    </>
                  )}
                </button>
              </div>
            )}

            <button
              onClick={() => setCurrentStep('form')}
              className="flex items-center gap-2 text-gray-500 hover:text-gray-300 transition"
            >
              <ArrowLeft className="w-4 h-4" />
              이전 단계로
            </button>
          </div>
        )}

        {/* Step 3: Generating */}
        {currentStep === 'generate' && (
          <div className="bg-[#1a1a1a] border border-[#2a2a2a] rounded-2xl p-12 text-center">
            <Loader2 className="w-16 h-16 text-indigo-400 animate-spin mx-auto mb-6" />
            <h2 className="text-xl font-semibold text-gray-100 mb-2">보고서 생성 중...</h2>
            <p className="text-gray-500">AI가 내용을 분석하고 양식에 채우고 있습니다.</p>
          </div>
        )}

        {/* Step 4: Preview */}
        {currentStep === 'preview' && (
          <div className="space-y-6">
            <div className="bg-[#1a1a1a] border border-[#2a2a2a] rounded-2xl p-6">
              <h2 className="text-lg font-semibold text-gray-100 mb-4">미리보기</h2>

              {/* Template Preview Mode */}
              {selectedTemplate && !useCustomForm ? (
                <>
                  <div className="border border-[#2a2a2a] rounded-xl overflow-hidden bg-white">
                    <div id="template-preview-content">
                      <TemplateRenderer
                        templateId={selectedTemplate.id}
                        formData={templateFormData}
                        mode="preview"
                      />
                    </div>
                  </div>

                  {/* Quick edit for key fields */}
                  <div className="mt-6 space-y-4">
                    <h3 className="font-medium text-gray-300">빠른 수정</h3>
                    <div className="grid grid-cols-1 sm:grid-cols-2 gap-4">
                      {selectedTemplate.fields.slice(0, 6).map((field) => (
                        <div key={field.id}>
                          <label className="block text-sm text-gray-500 mb-1">{field.label}</label>
                          <input
                            type={field.type === 'date' ? 'date' : 'text'}
                            value={templateFormData[field.id] || ''}
                            onChange={(e) => setTemplateFormData(prev => ({
                              ...prev,
                              [field.id]: e.target.value
                            }))}
                            className="w-full border border-[#3a3a3a] bg-[#242424] rounded-lg p-2 text-sm text-gray-200 focus:ring-2 focus:ring-indigo-500 focus:border-transparent"
                          />
                        </div>
                      ))}
                    </div>
                  </div>
                </>
              ) : (
                /* Custom Form Preview Mode */
                <>
                  <div className="relative border border-[#2a2a2a] rounded-xl overflow-hidden">
                    {formImageUrl && (
                      <img src={formImageUrl} alt="양식" className="w-full" />
                    )}
                    {/* Overlay filled fields preview */}
                    <div className="absolute inset-0 pointer-events-none">
                      {filledFields.map((field, idx) => (
                        field.value && (
                          <div
                            key={idx}
                            className="absolute bg-indigo-900/60 border border-indigo-500 text-xs text-indigo-200 p-1 overflow-hidden"
                            style={{
                              left: `${(field.x / (formAnalysis?.pageWidth || 595)) * 100}%`,
                              top: `${(field.y / (formAnalysis?.pageHeight || 842)) * 100}%`,
                              width: `${(field.width / (formAnalysis?.pageWidth || 595)) * 100}%`,
                              height: `${(field.height / (formAnalysis?.pageHeight || 842)) * 100}%`,
                            }}
                          >
                            {field.value}
                          </div>
                        )
                      ))}
                    </div>
                  </div>

                  {/* Editable fields */}
                  <div className="mt-6 space-y-4">
                    <h3 className="font-medium text-gray-300">필드 수정</h3>
                    {filledFields.map((field, idx) => (
                      <div key={idx}>
                        <label className="block text-sm text-gray-500 mb-1">{field.label}</label>
                        {field.type === 'multiline' ? (
                          <textarea
                            value={field.value || ''}
                            onChange={(e) => {
                              const updated = [...filledFields];
                              updated[idx] = { ...field, value: e.target.value };
                              setFilledFields(updated);
                            }}
                            rows={3}
                            className="w-full border border-[#3a3a3a] bg-[#242424] rounded-lg p-2 text-sm text-gray-200 focus:ring-2 focus:ring-indigo-500 focus:border-transparent"
                          />
                        ) : (
                          <input
                            type={field.type === 'date' ? 'date' : 'text'}
                            value={field.value || ''}
                            onChange={(e) => {
                              const updated = [...filledFields];
                              updated[idx] = { ...field, value: e.target.value };
                              setFilledFields(updated);
                            }}
                            className="w-full border border-[#3a3a3a] bg-[#242424] rounded-lg p-2 text-sm text-gray-200 focus:ring-2 focus:ring-indigo-500 focus:border-transparent"
                          />
                        )}
                      </div>
                    ))}
                  </div>
                </>
              )}
            </div>

            <div className="flex gap-3">
              <button
                onClick={() => setCurrentStep(selectedTemplate && !useCustomForm ? 'form' : 'audio')}
                className="flex-1 bg-[#242424] text-gray-300 py-3 rounded-xl font-medium hover:bg-[#2a2a2a] transition"
              >
                이전
              </button>
              <button
                onClick={() => setCurrentStep('sign')}
                className="flex-1 bg-indigo-600 text-white py-3 rounded-xl font-medium hover:bg-indigo-500 transition flex items-center justify-center gap-2"
              >
                PDF 생성
                <ChevronRight className="w-5 h-5" />
              </button>
            </div>
          </div>
        )}

        {/* Step 5: Signature & Download */}
        {currentStep === 'sign' && (
          <div className="space-y-6">
            {/* Template PDF Download Mode */}
            {selectedTemplate && !useCustomForm ? (
              <>
                {/* Hidden container for PDF capture at full scale */}
                <div
                  ref={templatePrintRef}
                  className="fixed left-[-9999px] top-0 bg-white"
                  style={{ width: '210mm', minHeight: '297mm' }}
                >
                  <TemplateRenderer
                    templateId={selectedTemplate.id}
                    formData={templateFormData}
                    mode="print"
                  />
                </div>

                <div className="bg-[#1a1a1a] border border-[#2a2a2a] rounded-2xl p-6">
                  <h2 className="text-lg font-semibold text-gray-100 mb-4">PDF 다운로드</h2>
                  <p className="text-sm text-gray-500 mb-4">
                    작성한 보고서를 PDF로 다운로드합니다.
                  </p>

                  {/* Final Preview (scaled for display) */}
                  <div className="border border-[#2a2a2a] rounded-xl overflow-hidden bg-white mb-6">
                    <div className="transform scale-[0.5] origin-top-left w-[200%] h-auto" style={{ minHeight: '400px' }}>
                      <TemplateRenderer
                        templateId={selectedTemplate.id}
                        formData={templateFormData}
                        mode="print"
                      />
                    </div>
                  </div>

                  {/* Signature (optional for templates) */}
                  <div className="border-t border-[#2a2a2a] pt-4">
                    <h3 className="text-sm font-medium text-gray-300 mb-3">서명 (선택사항)</h3>
                    <div className="border-2 border-[#3a3a3a] rounded-xl overflow-hidden">
                      <canvas
                        ref={signatureCanvasRef}
                        width={350}
                        height={100}
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
                      className="mt-2 text-sm text-gray-500 hover:text-gray-300 transition"
                    >
                      서명 지우기
                    </button>
                  </div>
                </div>

                <div className="flex gap-3">
                  <button
                    onClick={() => setCurrentStep('preview')}
                    className="flex-1 bg-[#242424] text-gray-300 py-3 rounded-xl font-medium hover:bg-[#2a2a2a] transition"
                  >
                    이전
                  </button>
                  <button
                    onClick={handleDownloadTemplatePDF}
                    disabled={isDownloading}
                    className="flex-1 bg-indigo-600 text-white py-3 rounded-xl font-medium hover:bg-indigo-500 transition disabled:opacity-50 flex items-center justify-center gap-2"
                  >
                    {isDownloading ? (
                      <>
                        <Loader2 className="w-5 h-5 animate-spin" />
                        PDF 생성 중...
                      </>
                    ) : (
                      <>
                        <Download className="w-5 h-5" />
                        PDF 다운로드
                      </>
                    )}
                  </button>
                </div>
              </>
            ) : (
              /* Custom Form PDF Mode */
              <>
                {formAnalysis?.hasSignature && (
                  <div className="bg-[#1a1a1a] border border-[#2a2a2a] rounded-2xl p-6">
                    <h2 className="text-lg font-semibold text-gray-100 mb-4">서명</h2>
                    <p className="text-sm text-gray-500 mb-4">아래 영역에 서명해주세요.</p>

                    <div className="border-2 border-[#3a3a3a] rounded-xl overflow-hidden">
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
                      className="mt-3 text-sm text-gray-500 hover:text-gray-300 transition"
                    >
                      서명 지우기
                    </button>
                  </div>
                )}

                <div className="flex gap-3">
                  <button
                    onClick={() => setCurrentStep('preview')}
                    className="flex-1 bg-[#242424] text-gray-300 py-3 rounded-xl font-medium hover:bg-[#2a2a2a] transition"
                  >
                    이전
                  </button>
                  <button
                    onClick={handleDownloadPDF}
                    disabled={isDownloading || (formAnalysis?.hasSignature && !signature)}
                    className="flex-1 bg-indigo-600 text-white py-3 rounded-xl font-medium hover:bg-indigo-500 transition disabled:opacity-50 flex items-center justify-center gap-2"
                  >
                    {isDownloading ? (
                      <>
                        <Loader2 className="w-5 h-5 animate-spin" />
                        PDF 생성 중...
                      </>
                    ) : (
                      <>
                        <Download className="w-5 h-5" />
                        PDF 다운로드
                      </>
                    )}
                  </button>
                </div>
              </>
            )}
          </div>
        )}
      </main>
    </div>
  );
}

function StepIndicator({ step, label, active, completed }: { step: number; label: string; active: boolean; completed: boolean }) {
  return (
    <div className="flex flex-col items-center">
      <div
        className={`w-8 h-8 rounded-full flex items-center justify-center text-sm font-medium transition ${
          completed ? 'bg-green-500 text-white' : active ? 'bg-indigo-600 text-white' : 'bg-[#2a2a2a] text-gray-500'
        }`}
      >
        {completed ? '✓' : step}
      </div>
      <span className={`text-xs mt-1 ${active ? 'text-indigo-400 font-medium' : 'text-gray-500'}`}>
        {label}
      </span>
    </div>
  );
}

function StepConnector({ active }: { active: boolean }) {
  return <div className={`flex-1 h-0.5 mx-1 ${active ? 'bg-green-500' : 'bg-[#2a2a2a]'}`} />;
}
