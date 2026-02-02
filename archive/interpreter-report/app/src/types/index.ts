// User types
export interface User {
  id: string;
  email: string;
  name: string;
  image?: string;
  phone?: string;
  university?: string;
  major?: string;
  koreanCertificate?: string; // TOPIK level etc
  experience?: string;
  region?: string; // Ho Chi Minh, Hanoi, etc
  credits: number;
  profileCompleted: boolean;
  createdAt: Date;
  updatedAt: Date;
}

// Report types
export interface ReportField {
  name: string;
  value: string;
  type: 'text' | 'number' | 'date' | 'textarea' | 'rating';
}

export interface Report {
  id: string;
  userId: string;
  title: string;
  fields: ReportField[];
  signature?: string;
  transcription?: string;
  audioUrl?: string;
  createdAt: Date;
  updatedAt: Date;
}

// Form template extracted from image
export interface FormTemplate {
  title: string;
  fields: {
    name: string;
    type: 'text' | 'number' | 'date' | 'textarea' | 'rating';
    required: boolean;
  }[];
}

// Transcription result
export interface TranscriptionResult {
  text: string;
  language: 'ko' | 'vi' | 'mixed';
  duration: number;
  confidence: number;
}

// Credit transaction
export interface CreditTransaction {
  id: string;
  userId: string;
  amount: number;
  type: 'use' | 'earn' | 'purchase' | 'referral' | 'profile_bonus';
  description: string;
  createdAt: Date;
}
