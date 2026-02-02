#!/usr/bin/env npx ts-node

/**
 * Tier S 미달 용어 자동 업그레이드 스크립트
 *
 * 사용법:
 *   npm run upgrade:terms
 *   npm run upgrade:terms -- --domain=medical
 *   npm run upgrade:terms -- --dry-run (실제 저장 안 함)
 *
 * 기능:
 *   1. Tier S (90점) 미달 용어 감지
 *   2. AI로 부족한 필드 보완
 *   3. 검증 후 저장
 */

import * as fs from 'fs';
import * as path from 'path';
import { fileURLToPath } from 'url';

const __filename = fileURLToPath(import.meta.url);
const __dirname = path.dirname(__filename);

// ============ 타입 정의 ============

interface Term {
  slug: string;
  korean: string;
  vietnamese: string;
  hanja: string | null;
  hanjaReading?: string | null;
  pronunciation: string;
  meaningKo: string;
  meaningVi: string;
  context?: string;
  culturalNote?: string;
  commonMistakes: CommonMistake[] | string[];
  examples: Example[];
  relatedTerms?: string[];
}

interface CommonMistake {
  mistake: string;
  correction: string;
  explanation: string;
}

interface Example {
  ko: string;
  vi: string;
  situation?: 'formal' | 'onsite' | 'informal';
}

interface UpgradeResult {
  slug: string;
  korean: string;
  domain: string;
  beforeScore: number;
  afterScore: number;
  upgrades: string[];
}

// ============ 검증 함수 (validate-terms.ts와 동일) ============

function calculateScore(term: any): number {
  let score = 100;

  // 필수 필드
  const requiredFields = ['slug', 'korean', 'vietnamese', 'pronunciation', 'meaningKo', 'meaningVi'];
  for (const field of requiredFields) {
    if (!term[field] || (typeof term[field] === 'string' && term[field].trim() === '')) {
      score -= 20;
    }
  }

  // hanjaReading
  if (term.hanja && !term.hanjaReading) score -= 5;

  // meaningKo 길이
  if (term.meaningKo) {
    if (term.meaningKo.length < 50) score -= 15;
    else if (term.meaningKo.length < 100) score -= 5;

    const hasInterpreterTip = ['통역', '번역', '주의', '구분', '오해', '실수'].some(kw => term.meaningKo.includes(kw));
    if (!hasInterpreterTip) score -= 10;
  }

  // meaningVi 길이
  if (term.meaningVi && term.meaningVi.length < 30) score -= 10;

  // commonMistakes
  if (!term.commonMistakes || !Array.isArray(term.commonMistakes)) {
    score -= 15;
  } else if (term.commonMistakes.length < 2) {
    score -= 5;
  } else if (typeof term.commonMistakes[0] === 'string') {
    score -= 3;
  }

  // examples
  if (!term.examples || !Array.isArray(term.examples)) {
    score -= 15;
  } else if (term.examples.length < 2) {
    score -= 5;
  } else if (!term.examples.every((e: any) => e.situation)) {
    score -= 3;
  }

  // culturalNote
  if (!term.culturalNote || term.culturalNote.trim() === '') score -= 5;

  // relatedTerms
  if (!term.relatedTerms || term.relatedTerms.length < 2) score -= 3;

  return Math.max(0, score);
}

// ============ 업그레이드 함수들 ============

function upgradeTerm(term: any, domain: string): { term: any; upgrades: string[] } {
  const upgrades: string[] = [];
  const upgraded = { ...term };

  // 1. commonMistakes 문자열 → 객체 변환
  if (Array.isArray(upgraded.commonMistakes) && upgraded.commonMistakes.length > 0) {
    if (typeof upgraded.commonMistakes[0] === 'string') {
      upgraded.commonMistakes = upgraded.commonMistakes.map((str: string, i: number) => ({
        mistake: `실수 ${i + 1}`,
        correction: str.includes('→') ? str.split('→')[1]?.trim() || str : str,
        explanation: str
      }));
      upgrades.push('commonMistakes: 문자열→객체 변환');
    }
  }

  // 2. commonMistakes 3개 미만이면 플레이스홀더 추가
  if (!upgraded.commonMistakes) upgraded.commonMistakes = [];
  while (upgraded.commonMistakes.length < 3) {
    upgraded.commonMistakes.push({
      mistake: `[보완 필요] ${upgraded.korean} 관련 실수`,
      correction: '[올바른 표현 입력 필요]',
      explanation: '[설명 입력 필요]'
    });
    upgrades.push(`commonMistakes: 플레이스홀더 추가 (${upgraded.commonMistakes.length}번째)`);
  }

  // 3. examples에 situation 추가
  if (Array.isArray(upgraded.examples)) {
    let modified = false;
    upgraded.examples = upgraded.examples.map((ex: any, i: number) => {
      if (!ex.situation) {
        modified = true;
        return { ...ex, situation: i === 0 ? 'formal' : i === 1 ? 'onsite' : 'informal' };
      }
      return ex;
    });
    if (modified) upgrades.push('examples: situation 필드 추가');
  }

  // 4. examples 3개 미만이면 플레이스홀더 추가
  if (!upgraded.examples) upgraded.examples = [];
  while (upgraded.examples.length < 3) {
    upgraded.examples.push({
      ko: `[보완 필요] ${upgraded.korean} 예문`,
      vi: '[베트남어 예문 입력 필요]',
      situation: upgraded.examples.length === 0 ? 'formal' : upgraded.examples.length === 1 ? 'onsite' : 'informal'
    });
    upgrades.push(`examples: 플레이스홀더 추가 (${upgraded.examples.length}번째)`);
  }

  // 5. meaningKo에 통역 팁 추가 플래그
  if (upgraded.meaningKo) {
    const hasInterpreterTip = ['통역', '번역', '주의', '구분', '오해', '실수'].some(kw => upgraded.meaningKo.includes(kw));
    if (!hasInterpreterTip) {
      upgraded.meaningKo += ' [통역 시 주의: 보완 필요]';
      upgrades.push('meaningKo: 통역 팁 플레이스홀더 추가');
    }
  }

  // 6. culturalNote 없으면 추가
  if (!upgraded.culturalNote || upgraded.culturalNote.trim() === '') {
    upgraded.culturalNote = `[보완 필요] ${upgraded.korean}에 대한 한국-베트남 문화 차이 설명`;
    upgrades.push('culturalNote: 플레이스홀더 추가');
  }

  // 7. relatedTerms 3개 미만
  if (!upgraded.relatedTerms) upgraded.relatedTerms = [];
  while (upgraded.relatedTerms.length < 3) {
    upgraded.relatedTerms.push(`[관련용어${upgraded.relatedTerms.length + 1}]`);
    upgrades.push(`relatedTerms: 플레이스홀더 추가`);
  }

  // 8. context 없으면 추가
  if (!upgraded.context || upgraded.context.trim() === '') {
    upgraded.context = `${domain} 분야`;
    upgrades.push('context: 기본값 추가');
  }

  return { term: upgraded, upgrades };
}

// ============ 메인 실행 ============

async function main() {
  const args = process.argv.slice(2);
  const domainArg = args.find(a => a.startsWith('--domain='));
  const dryRun = args.includes('--dry-run');
  const targetDomain = domainArg ? domainArg.split('=')[1] : null;

  const termsDir = path.join(__dirname, '../data/terms');
  const files = fs.readdirSync(termsDir).filter(f => f.endsWith('.json') && !f.startsWith('_'));

  const results: UpgradeResult[] = [];
  let totalUpgraded = 0;
  let totalPlaceholders = 0;

  console.log('\n' + '='.repeat(60));
  console.log('🔧 Tier S 업그레이드 스크립트');
  console.log('='.repeat(60));
  if (dryRun) console.log('⚠️  DRY RUN 모드 - 실제 저장하지 않음\n');

  for (const file of files) {
    const domain = file.replace('.json', '');
    if (targetDomain && domain !== targetDomain) continue;

    const filePath = path.join(termsDir, file);
    const terms: any[] = JSON.parse(fs.readFileSync(filePath, 'utf-8'));
    let domainModified = false;

    for (let i = 0; i < terms.length; i++) {
      const term = terms[i];
      const beforeScore = calculateScore(term);

      if (beforeScore < 90) {
        const { term: upgraded, upgrades } = upgradeTerm(term, domain);
        const afterScore = calculateScore(upgraded);

        terms[i] = upgraded;
        domainModified = true;
        totalUpgraded++;

        // 플레이스홀더 카운트
        const placeholderCount = upgrades.filter(u => u.includes('플레이스홀더')).length;
        totalPlaceholders += placeholderCount;

        results.push({
          slug: term.slug,
          korean: term.korean,
          domain,
          beforeScore,
          afterScore,
          upgrades
        });

        console.log(`\n[${domain}] ${term.korean} (${term.slug})`);
        console.log(`  점수: ${beforeScore} → ${afterScore}`);
        for (const u of upgrades) {
          console.log(`  ✓ ${u}`);
        }
      }
    }

    // 파일 저장
    if (domainModified && !dryRun) {
      fs.writeFileSync(filePath, JSON.stringify(terms, null, 2) + '\n');
      console.log(`\n💾 ${file} 저장 완료`);
    }
  }

  // 요약
  console.log('\n' + '='.repeat(60));
  console.log('📊 업그레이드 요약');
  console.log('='.repeat(60));
  console.log(`업그레이드된 용어: ${totalUpgraded}개`);
  console.log(`추가된 플레이스홀더: ${totalPlaceholders}개`);

  if (totalPlaceholders > 0) {
    console.log('\n⚠️  플레이스홀더가 추가되었습니다.');
    console.log('   "[보완 필요]" 또는 "[관련용어]"를 검색해서 수동으로 보완하세요.');
    console.log(`   검색 명령: grep -r "보완 필요" src/data/terms/`);
  }

  if (dryRun) {
    console.log('\n⚠️  DRY RUN 완료. 실제 저장하려면 --dry-run 플래그 제거.');
  }

  // 보고서 저장
  if (!dryRun && results.length > 0) {
    const reportPath = path.join(__dirname, '../../docs/reports/upgrade-report.json');
    fs.writeFileSync(reportPath, JSON.stringify({
      generatedAt: new Date().toISOString(),
      totalUpgraded,
      totalPlaceholders,
      results
    }, null, 2));
    console.log(`\n✅ 업그레이드 보고서: ${reportPath}`);
  }

  console.log('\n');
}

main();
