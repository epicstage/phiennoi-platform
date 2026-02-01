#!/usr/bin/env node

/**
 * 베트남 박람회 데이터 기반 콘텐츠 자동 생성 스크립트
 *
 * 실행: node scripts/generate-exhibition-content.js
 * GitHub Actions: .github/workflows/exhibition-content.yml
 *
 * 기능:
 * 1. SECC, ICE Hanoi, MyFair 등에서 박람회 일정 수집
 * 2. 관련 도메인 용어 큐레이션
 * 3. SEO 랜딩 페이지 생성 (해당 시)
 */

import fs from 'node:fs';
import path from 'node:path';
import { fileURLToPath } from 'node:url';

const __filename = fileURLToPath(import.meta.url);
const __dirname = path.dirname(__filename);
const ROOT = path.resolve(__dirname, '..');

// ── 환경변수 로드 ───────────────────────────────────────────────────────────
function loadEnv() {
  const envPath = path.join(ROOT, '.env.local');
  if (fs.existsSync(envPath)) {
    const content = fs.readFileSync(envPath, 'utf-8');
    for (const line of content.split('\n')) {
      const trimmed = line.trim();
      if (!trimmed || trimmed.startsWith('#')) continue;
      const eqIdx = trimmed.indexOf('=');
      if (eqIdx === -1) continue;
      const key = trimmed.slice(0, eqIdx).trim();
      let value = trimmed.slice(eqIdx + 1).trim();
      if ((value.startsWith('"') && value.endsWith('"')) ||
          (value.startsWith("'") && value.endsWith("'"))) {
        value = value.slice(1, -1);
      }
      if (!process.env[key]) {
        process.env[key] = value;
      }
    }
  }
}

loadEnv();

// ── 상수 ────────────────────────────────────────────────────────────────────
const ANTHROPIC_API_KEY = process.env.ANTHROPIC_API_KEY;
const TERMS_DIR = path.join(ROOT, 'src', 'data', 'terms');
const EXHIBITIONS_DIR = path.join(ROOT, 'src', 'data', 'exhibitions');
const CONTENT_DIR = path.join(ROOT, 'src', 'content', 'exhibitions');

// 도메인 매핑 (박람회 키워드 → 용어 도메인)
const DOMAIN_KEYWORDS = {
  agriculture: ['농업', '농산물', 'agri', 'farm', 'agriculture', 'food processing'],
  automotive: ['자동차', '오토', 'auto', 'automotive', 'vehicle', 'motor'],
  beauty: ['뷰티', '화장품', 'beauty', 'cosmetic', 'skincare'],
  construction: ['건설', '건축', 'construction', 'building', 'architecture'],
  electronics: ['전자', '반도체', 'electronic', 'semiconductor', 'tech'],
  exhibition: ['박람회', '전시', 'expo', 'exhibition', 'trade show'],
  finance: ['금융', '투자', 'finance', 'banking', 'investment'],
  fnb: ['식음료', '프랜차이즈', 'f&b', 'food', 'beverage', 'restaurant', 'franchise'],
  food: ['식품', '가공식품', 'food', 'processing'],
  furniture: ['가구', '인테리어', 'furniture', 'interior', 'home'],
  golf: ['골프', 'golf'],
  hr: ['인사', '채용', 'hr', 'recruitment', 'employment'],
  it: ['IT', '소프트웨어', 'software', 'digital', 'tech'],
  legal: ['법률', '법무', 'legal', 'law'],
  logistics: ['물류', '운송', 'logistics', 'shipping', 'transport'],
  manufacturing: ['제조', '공장', 'manufacturing', 'factory', 'industrial'],
  medical: ['의료', '헬스케어', 'medical', 'healthcare', 'hospital', 'pharma'],
  plasticSurgery: ['성형', '미용의료', 'plastic surgery', 'aesthetic'],
  realEstate: ['부동산', '건물', 'real estate', 'property'],
  semiconductor: ['반도체', '칩', 'semiconductor', 'chip'],
  textile: ['섬유', '의류', 'textile', 'garment', 'fashion', 'apparel'],
  tourism: ['관광', '여행', 'tourism', 'travel', 'hospitality'],
  trade: ['무역', '수출입', 'trade', 'import', 'export'],
  cosmetics: ['화장품', 'cosmetic', 'beauty', 'skincare'],
  environment: ['환경', '에너지', 'environment', 'energy', 'green'],
  education: ['교육', '학습', 'education', 'training', 'learning'],
};

// ── 박람회 소스 정보 ────────────────────────────────────────────────────────
const EXHIBITION_SOURCES = [
  {
    name: 'SECC',
    url: 'https://www.secc.com.vn',
    location: 'Ho Chi Minh City',
  },
  {
    name: 'ICE Hanoi',
    url: 'https://www.icehanoi.com.vn',
    location: 'Hanoi',
  },
  {
    name: 'MyFair',
    url: 'https://myfair.co',
    region: 'vietnam',
  },
];

// ── 유틸리티 함수 ───────────────────────────────────────────────────────────
function sleep(ms) {
  return new Promise(resolve => setTimeout(resolve, ms));
}

function getWeekRange() {
  const now = new Date();
  const startOfWeek = new Date(now);
  startOfWeek.setDate(now.getDate() - now.getDay() + 1); // 월요일

  const endOfWeek = new Date(startOfWeek);
  endOfWeek.setDate(startOfWeek.getDate() + 13); // 2주 후까지

  return {
    start: startOfWeek.toISOString().split('T')[0],
    end: endOfWeek.toISOString().split('T')[0],
  };
}

// ── Claude API 호출 ─────────────────────────────────────────────────────────
async function callClaude(systemPrompt, userPrompt) {
  if (!ANTHROPIC_API_KEY) {
    console.warn('⚠️ ANTHROPIC_API_KEY 없음 - 모의 데이터 사용');
    return null;
  }

  const response = await fetch('https://api.anthropic.com/v1/messages', {
    method: 'POST',
    headers: {
      'Content-Type': 'application/json',
      'x-api-key': ANTHROPIC_API_KEY,
      'anthropic-version': '2023-06-01',
    },
    body: JSON.stringify({
      model: 'claude-3-5-haiku-20241022',
      max_tokens: 4096,
      system: systemPrompt,
      messages: [{ role: 'user', content: userPrompt }],
    }),
  });

  if (!response.ok) {
    const text = await response.text();
    throw new Error(`Claude API ${response.status}: ${text}`);
  }

  const data = await response.json();
  return data.content[0].text;
}

// ── 박람회 데이터 수집 (웹 스크래핑 대신 Claude로 조사) ─────────────────────
async function fetchExhibitionData() {
  const { start, end } = getWeekRange();

  console.log(`📅 박람회 조사 기간: ${start} ~ ${end}`);

  const systemPrompt = `You are a Vietnamese trade show researcher.
Provide ONLY real, verifiable exhibitions happening in Vietnam.
Output JSON array format. No markdown.
Focus on exhibitions relevant to Korean businesses.`;

  const userPrompt = `List upcoming trade shows and exhibitions in Vietnam from ${start} to ${end}.
Include SECC Ho Chi Minh, ICE Hanoi, and other major venues.

Return JSON array with this structure:
[
  {
    "name": "Exhibition Name",
    "nameKo": "한국어 이름",
    "venue": "Venue name",
    "city": "Ho Chi Minh City" or "Hanoi",
    "startDate": "YYYY-MM-DD",
    "endDate": "YYYY-MM-DD",
    "industry": "main industry category",
    "description": "Brief description in Korean",
    "website": "official website if known",
    "relevantDomains": ["domain1", "domain2"]
  }
]

Only include real exhibitions you're confident about.
If no exhibitions found for this period, return empty array [].`;

  try {
    const result = await callClaude(systemPrompt, userPrompt);

    if (!result) {
      // 모의 데이터 (API 키 없을 때)
      return getMockExhibitions(start, end);
    }

    // JSON 파싱 시도
    const jsonMatch = result.match(/\[[\s\S]*\]/);
    if (jsonMatch) {
      return JSON.parse(jsonMatch[0]);
    }

    return [];
  } catch (err) {
    console.error('❌ 박람회 데이터 수집 실패:', err.message);
    return getMockExhibitions(start, end);
  }
}

// 모의 데이터 (테스트/폴백용)
function getMockExhibitions(start, end) {
  return [
    {
      name: 'Vietnam Expo',
      nameKo: '베트남 국제 무역 박람회',
      venue: 'SECC',
      city: 'Ho Chi Minh City',
      startDate: start,
      endDate: end,
      industry: 'Trade',
      description: '베트남 최대 규모의 국제 무역 박람회. 다양한 산업 분야의 기업들이 참가.',
      website: 'https://vietnamexpo.com.vn',
      relevantDomains: ['trade', 'manufacturing', 'logistics'],
    },
  ];
}

// ── 관련 도메인 매칭 ────────────────────────────────────────────────────────
function matchDomains(exhibition) {
  const matched = new Set();
  const searchText = [
    exhibition.name,
    exhibition.nameKo,
    exhibition.industry,
    exhibition.description,
  ].join(' ').toLowerCase();

  for (const [domain, keywords] of Object.entries(DOMAIN_KEYWORDS)) {
    for (const keyword of keywords) {
      if (searchText.includes(keyword.toLowerCase())) {
        matched.add(domain);
        break;
      }
    }
  }

  // 박람회에서 직접 지정한 도메인도 추가
  if (exhibition.relevantDomains) {
    exhibition.relevantDomains.forEach(d => matched.add(d));
  }

  return Array.from(matched);
}

// ── 용어 큐레이션 ───────────────────────────────────────────────────────────
function curateTermsForExhibition(exhibition, domains) {
  const curatedTerms = {};

  for (const domain of domains) {
    const termsFile = path.join(TERMS_DIR, `${domain}.json`);
    if (!fs.existsSync(termsFile)) continue;

    const terms = JSON.parse(fs.readFileSync(termsFile, 'utf-8'));

    // 도메인별 상위 10개 용어 선택 (frequency 기준)
    const topTerms = terms
      .sort((a, b) => (b.frequency || 3) - (a.frequency || 3))
      .slice(0, 10)
      .map(t => ({
        slug: t.slug,
        korean: t.korean,
        vietnamese: t.vietnamese,
        meaningKo: t.meaningKo?.slice(0, 100),
      }));

    if (topTerms.length > 0) {
      curatedTerms[domain] = topTerms;
    }
  }

  return curatedTerms;
}

// ── 콘텐츠 생성 (Markdown) ──────────────────────────────────────────────────
async function generateExhibitionContent(exhibition, curatedTerms) {
  const domains = Object.keys(curatedTerms);

  if (!ANTHROPIC_API_KEY) {
    // 간단한 템플릿 기반 콘텐츠
    return generateTemplateContent(exhibition, curatedTerms);
  }

  const systemPrompt = `You are a Korean content writer for a Vietnamese business interpreter platform.
Write helpful, practical content for Korean businesspeople preparing for exhibitions in Vietnam.
Output in Korean. Be concise but informative.`;

  const userPrompt = `Write a brief guide (300-500 characters) for Koreans attending this exhibition:

박람회: ${exhibition.nameKo || exhibition.name}
장소: ${exhibition.venue}, ${exhibition.city}
기간: ${exhibition.startDate} ~ ${exhibition.endDate}
산업: ${exhibition.industry}

관련 도메인 용어:
${domains.map(d => `- ${d}: ${curatedTerms[d]?.slice(0, 3).map(t => t.korean).join(', ')}`).join('\n')}

Include:
1. 박람회 소개 (1-2문장)
2. 한국 기업 참가 포인트
3. 필수 통역 용어 팁

Output plain text, no markdown headers.`;

  try {
    const content = await callClaude(systemPrompt, userPrompt);
    return content || generateTemplateContent(exhibition, curatedTerms);
  } catch (err) {
    console.error('❌ 콘텐츠 생성 실패:', err.message);
    return generateTemplateContent(exhibition, curatedTerms);
  }
}

function generateTemplateContent(exhibition, curatedTerms) {
  const domains = Object.keys(curatedTerms);

  return `${exhibition.nameKo || exhibition.name}이(가) ${exhibition.city}의 ${exhibition.venue}에서 ${exhibition.startDate}부터 ${exhibition.endDate}까지 개최됩니다.

${exhibition.description || '베트남 현지 바이어와의 비즈니스 미팅을 준비하세요.'}

관련 분야: ${domains.join(', ')}

📚 필수 통역 용어:
${domains.slice(0, 3).map(d => {
  const terms = curatedTerms[d]?.slice(0, 3) || [];
  return `[${d}] ${terms.map(t => `${t.korean}(${t.vietnamese})`).join(', ')}`;
}).join('\n')}`;
}

// ── 파일 저장 ───────────────────────────────────────────────────────────────
function saveExhibitionData(exhibitions) {
  fs.mkdirSync(EXHIBITIONS_DIR, { recursive: true });

  const { start } = getWeekRange();
  const filename = `exhibitions-${start}.json`;
  const filepath = path.join(EXHIBITIONS_DIR, filename);

  fs.writeFileSync(filepath, JSON.stringify(exhibitions, null, 2), 'utf-8');
  console.log(`✅ 박람회 데이터 저장: ${filepath}`);

  return filepath;
}

function saveContent(exhibition, content) {
  fs.mkdirSync(CONTENT_DIR, { recursive: true });

  const slug = exhibition.name
    .toLowerCase()
    .replace(/[^a-z0-9]+/g, '-')
    .replace(/(^-|-$)/g, '');

  const filename = `${exhibition.startDate}-${slug}.md`;
  const filepath = path.join(CONTENT_DIR, filename);

  const markdown = `---
title: "${exhibition.nameKo || exhibition.name}"
venue: "${exhibition.venue}"
city: "${exhibition.city}"
startDate: "${exhibition.startDate}"
endDate: "${exhibition.endDate}"
industry: "${exhibition.industry}"
website: "${exhibition.website || ''}"
generatedAt: "${new Date().toISOString()}"
---

${content}
`;

  fs.writeFileSync(filepath, markdown, 'utf-8');
  console.log(`✅ 콘텐츠 저장: ${filepath}`);

  return filepath;
}

// ── 메인 ────────────────────────────────────────────────────────────────────
async function main() {
  console.log('═'.repeat(60));
  console.log('  베트남 박람회 콘텐츠 자동 생성');
  console.log('  Epic Note - vn.epicstage.co.kr');
  console.log('═'.repeat(60));
  console.log();

  // 1. 박람회 데이터 수집
  console.log('📡 박람회 데이터 수집 중...');
  const exhibitions = await fetchExhibitionData();

  if (exhibitions.length === 0) {
    console.log('ℹ️ 이번 주 예정된 박람회가 없습니다.');
    process.exit(0);
  }

  console.log(`📋 ${exhibitions.length}개 박람회 발견\n`);

  // 2. 각 박람회별 처리
  const results = [];

  for (const exhibition of exhibitions) {
    console.log(`\n── ${exhibition.nameKo || exhibition.name} ──`);
    console.log(`   📍 ${exhibition.venue}, ${exhibition.city}`);
    console.log(`   📅 ${exhibition.startDate} ~ ${exhibition.endDate}`);

    // 도메인 매칭
    const domains = matchDomains(exhibition);
    console.log(`   🏷️ 관련 도메인: ${domains.join(', ') || '없음'}`);

    if (domains.length === 0) {
      console.log('   ⏭️ 관련 도메인 없음, 스킵');
      continue;
    }

    // 용어 큐레이션
    const curatedTerms = curateTermsForExhibition(exhibition, domains);
    const termCount = Object.values(curatedTerms).flat().length;
    console.log(`   📚 큐레이션된 용어: ${termCount}개`);

    // 콘텐츠 생성
    console.log('   ✍️ 콘텐츠 생성 중...');
    const content = await generateExhibitionContent(exhibition, curatedTerms);

    // 저장
    const contentPath = saveContent(exhibition, content);

    results.push({
      exhibition: exhibition.nameKo || exhibition.name,
      domains,
      termCount,
      contentPath,
    });

    // rate limit 방지
    await sleep(1000);
  }

  // 3. 박람회 데이터 저장
  saveExhibitionData(exhibitions);

  // 4. 결과 요약
  console.log('\n' + '═'.repeat(60));
  console.log('  결과 요약');
  console.log('═'.repeat(60));
  console.log(`  📋 처리된 박람회: ${results.length}/${exhibitions.length}`);
  console.log(`  📄 생성된 콘텐츠: ${results.length}개`);

  if (results.length > 0) {
    console.log('\n  생성된 파일:');
    results.forEach(r => {
      console.log(`    - ${r.exhibition} (${r.termCount} 용어)`);
    });
  }

  console.log('═'.repeat(60));
}

main().catch(err => {
  console.error('스크립트 에러:', err);
  process.exit(1);
});
