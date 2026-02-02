#!/usr/bin/env npx ts-node

/**
 * 모든 남은 플레이스홀더를 실제 콘텐츠로 교체
 */

import * as fs from 'fs';
import * as path from 'path';
import { fileURLToPath } from 'url';

const __filename = fileURLToPath(import.meta.url);
const __dirname = path.dirname(__filename);

// 도메인별 구체적 실수 예시
const DOMAIN_MISTAKES: Record<string, { mistake: string; correction: string; explanation: string }[]> = {
  food: [
    { mistake: '식품 용어를 직역', correction: '현지 소비자가 이해하는 표현으로 의역', explanation: '식품명은 문화적 맥락이 중요하므로 현지 표현을 사용해야 합니다.' },
    { mistake: '단위 환산 오류', correction: 'g, kg, ml, L 등 단위를 정확히 환산', explanation: '식품 표시에서 단위 오류는 규정 위반이 될 수 있습니다.' },
    { mistake: '유통기한 표현 혼동', correction: '제조일자(ngày sản xuất)와 유통기한(hạn sử dụng) 구분', explanation: '한국은 유통기한, 베트남은 제조일자+유효기간 표시가 일반적입니다.' },
  ],
  beauty: [
    { mistake: '성분명 직역', correction: 'INCI 명칭과 일반명을 함께 사용', explanation: '화장품 성분은 국제 표준명(INCI)과 현지 일반명이 다를 수 있습니다.' },
    { mistake: '효능 과장', correction: '각국 광고법에 맞는 표현 사용', explanation: '화장품 효능 표현은 양국의 광고 규제가 다르므로 주의가 필요합니다.' },
    { mistake: '피부 타입 표현 차이', correction: '건성(da khô), 지성(da dầu), 복합성(da hỗn hợp) 정확히 구분', explanation: '피부 타입 분류 기준이 다를 수 있으므로 구체적 설명이 필요합니다.' },
  ],
  it: [
    { mistake: 'IT 약어를 풀지 않음', correction: '약어와 풀네임을 함께 설명', explanation: '비전문가도 이해할 수 있도록 약어의 의미를 설명해야 합니다.' },
    { mistake: '기술 용어 직역', correction: '맥락에 맞는 현지 기술 용어 사용', explanation: 'IT 용어는 영어 원어를 그대로 쓰거나 현지화된 표현이 있을 수 있습니다.' },
    { mistake: '버전/호환성 정보 누락', correction: '소프트웨어 버전과 호환성 정보 함께 전달', explanation: '기술 통역 시 버전 정보는 중요한 맥락이므로 정확히 전달해야 합니다.' },
  ],
  legal: [
    { mistake: '법률 용어 직역', correction: '해당 국가 법체계에 맞는 용어 사용', explanation: '법률 용어는 직역 시 법적 의미가 달라질 수 있어 전문 용어를 사용해야 합니다.' },
    { mistake: '조항 번호 혼동', correction: '양국 법률의 조항 체계 차이 설명', explanation: '한국법과 베트남법의 구조가 달라 조항 대응이 1:1이 아닐 수 있습니다.' },
    { mistake: '법적 책임 범위 오해', correction: '권리와 의무를 명확히 구분하여 전달', explanation: '계약서 통역 시 책임 소재를 불명확하게 전달하면 분쟁 원인이 됩니다.' },
  ],
  manufacturing: [
    { mistake: '공정 용어 직역', correction: '현장에서 실제 사용하는 용어로 통역', explanation: '제조 현장 용어는 교과서적 표현과 다를 수 있습니다.' },
    { mistake: '불량률 계산 방식 차이', correction: 'PPM, % 등 불량률 표현 방식 확인 후 통역', explanation: '불량률 계산 기준이 다를 수 있으므로 정의를 확인해야 합니다.' },
    { mistake: '안전 지시 불명확', correction: '안전 관련 지시는 반복 확인 후 정확히 전달', explanation: '안전 지시 오역은 인명사고로 이어질 수 있어 신중해야 합니다.' },
  ],
  exhibition: [
    { mistake: '부스 규격 단위 혼동', correction: 'm, ft 등 단위를 명확히 환산', explanation: '전시 부스 규격은 국가별로 다른 단위를 사용할 수 있습니다.' },
    { mistake: '설치/철거 일정 오해', correction: '날짜와 시간대를 현지 기준으로 확인', explanation: '시차와 현지 공휴일을 고려하여 일정을 전달해야 합니다.' },
    { mistake: '비즈니스 매칭 조건 불명확', correction: '양측의 요구사항을 구체적으로 확인 후 매칭', explanation: '막연한 매칭보다 구체적 조건을 확인해야 효과적입니다.' },
  ],
  textile: [
    { mistake: '원단 규격 단위 혼동', correction: 'g/m², 야드, 인치 등 단위 정확히 환산', explanation: '섬유 업계는 다양한 단위를 사용하므로 환산에 주의해야 합니다.' },
    { mistake: '색상 코드 누락', correction: '팬톤, CMYK 등 정확한 색상 코드 전달', explanation: '색상명만으로는 정확한 색을 전달하기 어려워 코드가 필요합니다.' },
    { mistake: '납기일 계산 오류', correction: '영업일/역일 구분, 현지 공휴일 고려', explanation: '납기 계산 시 양국의 공휴일과 영업일 기준을 확인해야 합니다.' },
  ],
  realEstate: [
    { mistake: '면적 단위 혼동', correction: '㎡, 평, m² 환산 명확히 (1평 ≈ 3.3㎡)', explanation: '한국은 평, 베트남은 m²를 주로 사용하므로 환산이 필요합니다.' },
    { mistake: '계약 조건 모호', correction: '보증금, 월세, 관리비 항목별로 명확히 구분', explanation: '부동산 계약 조건은 법적 효력이 있으므로 정확해야 합니다.' },
    { mistake: '소유권 개념 차이', correction: '한국 소유권과 베트남 토지사용권 차이 설명', explanation: '베트남은 토지 사유화가 없어 사용권 개념으로 설명해야 합니다.' },
  ],
};

// 기본 실수 (도메인 특화가 없을 때)
const DEFAULT_MISTAKES = [
  { mistake: '전문 용어 직역', correction: '해당 분야에서 통용되는 표현 사용', explanation: '전문 용어는 직역보다 업계 표준 표현을 사용해야 이해도가 높습니다.' },
  { mistake: '단위 환산 오류', correction: '양국에서 사용하는 단위로 정확히 환산', explanation: '단위 오류는 비용, 수량 등에서 큰 차이를 만들 수 있습니다.' },
  { mistake: '문화적 맥락 무시', correction: '양국의 문화적 차이를 고려한 설명 추가', explanation: '같은 용어도 문화에 따라 다르게 이해될 수 있어 맥락 설명이 필요합니다.' },
];

function fixPlaceholders(term: any, domain: string): any {
  const updated = { ...term };

  // commonMistakes 플레이스홀더 수정
  if (Array.isArray(updated.commonMistakes)) {
    const domainMistakes = DOMAIN_MISTAKES[domain] || DEFAULT_MISTAKES;
    let mistakeIndex = 0;

    updated.commonMistakes = updated.commonMistakes.map((cm: any) => {
      if (typeof cm === 'object') {
        if (cm.mistake?.includes('보완 필요') || cm.correction?.includes('입력 필요')) {
          const replacement = domainMistakes[mistakeIndex % domainMistakes.length];
          mistakeIndex++;
          return {
            mistake: replacement.mistake,
            correction: replacement.correction,
            explanation: replacement.explanation
          };
        }
      }
      return cm;
    });
  }

  return updated;
}

async function main() {
  const termsDir = path.join(__dirname, '../data/terms');
  const files = fs.readdirSync(termsDir).filter(f => f.endsWith('.json') && !f.startsWith('_'));

  console.log('\n=== 플레이스홀더 최종 수정 ===\n');

  let totalFixed = 0;

  for (const file of files) {
    const domain = file.replace('.json', '');
    const filePath = path.join(termsDir, file);
    const terms: any[] = JSON.parse(fs.readFileSync(filePath, 'utf-8'));
    let fileModified = false;
    let fixCount = 0;

    for (let i = 0; i < terms.length; i++) {
      const original = JSON.stringify(terms[i]);
      const fixed = fixPlaceholders(terms[i], domain);
      if (JSON.stringify(fixed) !== original) {
        terms[i] = fixed;
        fileModified = true;
        fixCount++;
      }
    }

    if (fileModified) {
      fs.writeFileSync(filePath, JSON.stringify(terms, null, 2) + '\n');
      console.log(`✓ ${domain}: ${fixCount}개 수정`);
      totalFixed += fixCount;
    }
  }

  console.log(`\n총 ${totalFixed}개 항목 수정 완료\n`);
}

main();
