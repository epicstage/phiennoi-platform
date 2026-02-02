#!/usr/bin/env npx ts-node

/**
 * 한베 전문용어 품질 검증 스크립트
 *
 * 사용법:
 *   npx ts-node src/scripts/validate-terms.ts
 *   npx ts-node src/scripts/validate-terms.ts --domain=medical
 *   npx ts-node src/scripts/validate-terms.ts --report
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

interface ValidationIssue {
  field: string;
  type: 'missing' | 'invalid' | 'warning';
  message: string;
  penalty: number;
}

interface ValidationResult {
  slug: string;
  korean: string;
  domain: string;
  tier: 'S' | 'A' | 'B' | 'C' | 'F';
  score: number;
  issues: ValidationIssue[];
}

interface DomainReport {
  domain: string;
  total: number;
  tierDistribution: Record<string, number>;
  averageScore: number;
  topIssues: { issue: string; count: number }[];
}

// ============ 검증 함수 ============

function validateTerm(term: any, domain: string): ValidationResult {
  const issues: ValidationIssue[] = [];
  let score = 100;

  // 1. 필수 필드 검증
  const requiredFields = ['slug', 'korean', 'vietnamese', 'pronunciation', 'meaningKo', 'meaningVi'];
  for (const field of requiredFields) {
    if (!term[field] || (typeof term[field] === 'string' && term[field].trim() === '')) {
      issues.push({
        field,
        type: 'missing',
        message: `필수 필드 '${field}' 누락`,
        penalty: 20
      });
      score -= 20;
    }
  }

  // 2. 한자 검증 (null 허용)
  if (term.hanja !== null && term.hanja !== undefined && term.hanja !== '') {
    if (term.hanjaReading === undefined || term.hanjaReading === null) {
      issues.push({
        field: 'hanjaReading',
        type: 'warning',
        message: '한자가 있지만 hanjaReading 누락',
        penalty: 5
      });
      score -= 5;
    }
  }

  // 3. meaningKo 길이 및 품질 검증
  if (term.meaningKo) {
    const len = term.meaningKo.length;
    if (len < 50) {
      issues.push({
        field: 'meaningKo',
        type: 'invalid',
        message: `meaningKo 너무 짧음 (${len}자, 최소 100자 권장)`,
        penalty: 15
      });
      score -= 15;
    } else if (len < 100) {
      issues.push({
        field: 'meaningKo',
        type: 'warning',
        message: `meaningKo 다소 짧음 (${len}자, 100자 이상 권장)`,
        penalty: 5
      });
      score -= 5;
    }

    // 통역 관련 키워드 체크
    const interpreterKeywords = ['통역', '번역', '주의', '구분', '오해', '실수'];
    const hasInterpreterTip = interpreterKeywords.some(kw => term.meaningKo.includes(kw));
    if (!hasInterpreterTip) {
      issues.push({
        field: 'meaningKo',
        type: 'warning',
        message: '통역 팁이 포함되지 않음',
        penalty: 10
      });
      score -= 10;
    }
  }

  // 4. meaningVi 길이 검증
  if (term.meaningVi) {
    const len = term.meaningVi.length;
    if (len < 30) {
      issues.push({
        field: 'meaningVi',
        type: 'invalid',
        message: `meaningVi 너무 짧음 (${len}자, 최소 50자 권장)`,
        penalty: 10
      });
      score -= 10;
    }
  }

  // 5. commonMistakes 검증
  if (!term.commonMistakes || !Array.isArray(term.commonMistakes)) {
    issues.push({
      field: 'commonMistakes',
      type: 'missing',
      message: 'commonMistakes 누락',
      penalty: 15
    });
    score -= 15;
  } else if (term.commonMistakes.length < 2) {
    issues.push({
      field: 'commonMistakes',
      type: 'warning',
      message: `commonMistakes ${term.commonMistakes.length}개 (최소 2개 권장)`,
      penalty: 5
    });
    score -= 5;
  } else {
    // 객체 형식인지 확인
    const isObjectFormat = term.commonMistakes.every((m: any) =>
      typeof m === 'object' && m.mistake && m.correction
    );
    if (!isObjectFormat && term.commonMistakes.length > 0 && typeof term.commonMistakes[0] === 'string') {
      issues.push({
        field: 'commonMistakes',
        type: 'warning',
        message: '레거시 문자열 형식 (객체 형식 권장)',
        penalty: 3
      });
      score -= 3;
    }
  }

  // 6. examples 검증
  if (!term.examples || !Array.isArray(term.examples)) {
    issues.push({
      field: 'examples',
      type: 'missing',
      message: 'examples 누락',
      penalty: 15
    });
    score -= 15;
  } else if (term.examples.length < 2) {
    issues.push({
      field: 'examples',
      type: 'warning',
      message: `examples ${term.examples.length}개 (최소 2개 권장)`,
      penalty: 5
    });
    score -= 5;
  } else {
    // situation 필드 확인
    const hasSituation = term.examples.every((e: any) => e.situation);
    if (!hasSituation) {
      issues.push({
        field: 'examples',
        type: 'warning',
        message: 'examples에 situation 필드 없음',
        penalty: 3
      });
      score -= 3;
    }
  }

  // 7. culturalNote 검증
  if (!term.culturalNote || term.culturalNote.trim() === '') {
    issues.push({
      field: 'culturalNote',
      type: 'warning',
      message: 'culturalNote 누락',
      penalty: 5
    });
    score -= 5;
  }

  // 8. relatedTerms 검증
  if (!term.relatedTerms || !Array.isArray(term.relatedTerms) || term.relatedTerms.length < 2) {
    issues.push({
      field: 'relatedTerms',
      type: 'warning',
      message: 'relatedTerms 부족 (최소 2개 권장)',
      penalty: 3
    });
    score -= 3;
  }

  // 9. 베트남어 성조 검증
  if (term.vietnamese) {
    const vietnameseChars = term.vietnamese.replace(/[a-zA-Z\s\(\)\/]/g, '');
    const hasTones = /[àáảãạăằắẳẵặâầấẩẫậèéẻẽẹêềếểễệìíỉĩịòóỏõọôồốổỗộơờớởỡợùúủũụưừứửữựỳýỷỹỵđ]/i.test(term.vietnamese);
    if (!hasTones && vietnameseChars.length > 0) {
      issues.push({
        field: 'vietnamese',
        type: 'warning',
        message: '베트남어 성조가 없을 수 있음',
        penalty: 5
      });
      score -= 5;
    }
  }

  // 점수 최소값 보정
  score = Math.max(0, score);

  // 등급 결정
  let tier: 'S' | 'A' | 'B' | 'C' | 'F';
  if (score >= 90) tier = 'S';
  else if (score >= 75) tier = 'A';
  else if (score >= 60) tier = 'B';
  else if (score >= 40) tier = 'C';
  else tier = 'F';

  return {
    slug: term.slug || 'unknown',
    korean: term.korean || 'unknown',
    domain,
    tier,
    score,
    issues
  };
}

// ============ 메인 실행 ============

function main() {
  const args = process.argv.slice(2);
  const domainArg = args.find(a => a.startsWith('--domain='));
  const reportArg = args.includes('--report');
  const targetDomain = domainArg ? domainArg.split('=')[1] : null;

  const termsDir = path.join(__dirname, '../data/terms');
  const files = fs.readdirSync(termsDir).filter(f => f.endsWith('.json') && !f.startsWith('_'));

  const allResults: ValidationResult[] = [];
  const domainReports: DomainReport[] = [];

  for (const file of files) {
    const domain = file.replace('.json', '');

    if (targetDomain && domain !== targetDomain) continue;

    const filePath = path.join(termsDir, file);
    const terms: any[] = JSON.parse(fs.readFileSync(filePath, 'utf-8'));

    const results = terms.map(term => validateTerm(term, domain));
    allResults.push(...results);

    // 도메인 보고서 생성
    const tierDist: Record<string, number> = { S: 0, A: 0, B: 0, C: 0, F: 0 };
    const issueCount: Record<string, number> = {};
    let totalScore = 0;

    for (const r of results) {
      tierDist[r.tier]++;
      totalScore += r.score;
      for (const issue of r.issues) {
        const key = `${issue.field}: ${issue.message}`;
        issueCount[key] = (issueCount[key] || 0) + 1;
      }
    }

    const topIssues = Object.entries(issueCount)
      .sort((a, b) => b[1] - a[1])
      .slice(0, 5)
      .map(([issue, count]) => ({ issue, count }));

    domainReports.push({
      domain,
      total: results.length,
      tierDistribution: tierDist,
      averageScore: Math.round(totalScore / results.length),
      topIssues
    });
  }

  // ============ 결과 출력 ============

  console.log('\n' + '='.repeat(60));
  console.log('📊 한베 전문용어 품질 검증 보고서');
  console.log('='.repeat(60) + '\n');

  // 전체 요약
  const totalTerms = allResults.length;
  const avgScore = Math.round(allResults.reduce((sum, r) => sum + r.score, 0) / totalTerms);
  const tierCounts = { S: 0, A: 0, B: 0, C: 0, F: 0 };
  allResults.forEach(r => tierCounts[r.tier]++);

  console.log('📈 전체 요약');
  console.log('-'.repeat(40));
  console.log(`총 용어 수: ${totalTerms}`);
  console.log(`평균 점수: ${avgScore}점`);
  console.log(`\n등급 분포:`);
  console.log(`  🏆 Tier S (90+): ${tierCounts.S}개 (${(tierCounts.S/totalTerms*100).toFixed(1)}%)`);
  console.log(`  ✅ Tier A (75+): ${tierCounts.A}개 (${(tierCounts.A/totalTerms*100).toFixed(1)}%)`);
  console.log(`  📝 Tier B (60+): ${tierCounts.B}개 (${(tierCounts.B/totalTerms*100).toFixed(1)}%)`);
  console.log(`  ⚠️ Tier C (40+): ${tierCounts.C}개 (${(tierCounts.C/totalTerms*100).toFixed(1)}%)`);
  console.log(`  ❌ Tier F (<40): ${tierCounts.F}개 (${(tierCounts.F/totalTerms*100).toFixed(1)}%)`);

  // 도메인별 보고서
  if (reportArg || targetDomain) {
    console.log('\n' + '='.repeat(60));
    console.log('📁 도메인별 상세 보고서');
    console.log('='.repeat(60));

    for (const report of domainReports) {
      console.log(`\n### ${report.domain.toUpperCase()} (${report.total}개)`);
      console.log(`평균 점수: ${report.averageScore}점`);
      console.log(`등급: S=${report.tierDistribution.S} A=${report.tierDistribution.A} B=${report.tierDistribution.B} C=${report.tierDistribution.C} F=${report.tierDistribution.F}`);

      if (report.topIssues.length > 0) {
        console.log(`주요 이슈:`);
        for (const issue of report.topIssues) {
          console.log(`  - ${issue.issue} (${issue.count}건)`);
        }
      }
    }
  }

  // 문제 용어 목록 (Tier C/F)
  const problemTerms = allResults.filter(r => r.tier === 'C' || r.tier === 'F');
  if (problemTerms.length > 0) {
    console.log('\n' + '='.repeat(60));
    console.log(`⚠️ 개선 필요 용어 (${problemTerms.length}개)`);
    console.log('='.repeat(60));

    for (const term of problemTerms.slice(0, 20)) {
      console.log(`\n[${term.tier}] ${term.korean} (${term.domain}) - ${term.score}점`);
      for (const issue of term.issues.slice(0, 3)) {
        console.log(`  - ${issue.field}: ${issue.message}`);
      }
    }

    if (problemTerms.length > 20) {
      console.log(`\n... 외 ${problemTerms.length - 20}개`);
    }
  }

  // JSON 보고서 저장
  if (reportArg) {
    const reportPath = path.join(__dirname, '../../docs/reports/quality-report.json');
    const reportData = {
      generatedAt: new Date().toISOString(),
      summary: {
        totalTerms,
        averageScore: avgScore,
        tierDistribution: tierCounts
      },
      domains: domainReports,
      problemTerms: problemTerms.map(t => ({
        slug: t.slug,
        korean: t.korean,
        domain: t.domain,
        score: t.score,
        issues: t.issues
      }))
    };

    fs.writeFileSync(reportPath, JSON.stringify(reportData, null, 2));
    console.log(`\n✅ 상세 보고서 저장: ${reportPath}`);
  }

  console.log('\n');
}

main();
