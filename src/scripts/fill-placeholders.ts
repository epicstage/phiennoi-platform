#!/usr/bin/env npx ts-node

/**
 * 플레이스홀더를 실제 콘텐츠로 채우는 스크립트
 *
 * 플레이스홀더 패턴:
 * - "[통역 시 주의: 보완 필요]" → 실제 통역 팁으로 교체
 * - "[보완 필요]" → 실제 내용으로 교체
 * - "[관련용어N]" → 실제 관련 용어로 교체
 * - commonMistakes의 "실수 N" → 구체적 실수로 교체
 */

import * as fs from 'fs';
import * as path from 'path';
import { fileURLToPath } from 'url';

const __filename = fileURLToPath(import.meta.url);
const __dirname = path.dirname(__filename);

// ============ 도메인별 통역 팁 템플릿 ============

const INTERPRETER_TIPS: Record<string, string[]> = {
  automotive: [
    '통역 시 자동차 부품명은 한국식 명칭과 베트남 현지 명칭이 다를 수 있으므로 양쪽 표현을 모두 알아두는 것이 중요합니다.',
    '통역 시 기술 사양(마력, 토크, 배기량)의 단위 환산에 주의하고, 베트남에서 일반적으로 사용하는 단위로 변환해 설명해야 합니다.',
    '통역 시 약어(ABS, ESP, EPS 등)는 풀네임과 함께 기능을 간단히 설명하면 이해도가 높아집니다.',
  ],
  beauty: [
    '통역 시 화장품 성분명은 INCI 명칭과 일반 명칭을 구분하여 전달해야 하며, 베트남 소비자에게 익숙한 표현을 함께 사용하는 것이 좋습니다.',
    '통역 시 피부 타입, 효능 관련 용어는 과장 없이 정확하게 전달해야 하며, 베트남 식약처(ATTP) 규정에 맞는 표현인지 확인이 필요합니다.',
    '통역 시 색조 화장품의 색상명은 한국과 베트남에서 다르게 표현될 수 있으므로 실제 색상을 확인하며 통역하는 것이 좋습니다.',
  ],
  construction: [
    '통역 시 건설 현장 안전 용어는 생명과 직결되므로 정확한 전달이 필수이며, 오해의 소지가 없도록 반복 확인하는 것이 좋습니다.',
    '통역 시 건축 도면 용어와 현장 실무 용어가 다를 수 있으므로, 상황에 맞는 표현을 사용해야 합니다.',
    '통역 시 측량 단위(m, cm, mm)와 면적 단위(㎡, 평)의 환산에 주의하고, 베트남에서는 미터법을 주로 사용함을 기억해야 합니다.',
  ],
  education: [
    '통역 시 한국과 베트남의 학제 차이(초등 6년, 중등 3년, 고등 3년 vs 5-4-3)를 고려하여 학년을 설명해야 합니다.',
    '통역 시 학위명, 자격증명은 양국의 공식 명칭이 다를 수 있으므로 동등성을 설명하는 것이 중요합니다.',
    '통역 시 교육 과정, 커리큘럼 용어는 직역보다 해당 국가의 교육 시스템에 맞게 의역하는 것이 이해에 도움됩니다.',
  ],
  electronics: [
    '통역 시 전자부품 규격(전압, 전류, 저항값)은 정확한 수치 전달이 중요하며, 단위 표기법에 주의해야 합니다.',
    '통역 시 반도체, PCB 관련 약어는 풀네임을 함께 설명하고, 공정 순서를 이해하면 문맥 파악에 도움됩니다.',
    '통역 시 불량 유형(외관 불량, 기능 불량, 신뢰성 불량)을 구체적으로 구분하여 전달해야 품질 관리에 오해가 없습니다.',
  ],
  environment: [
    '통역 시 환경 규제 용어는 법적 효력이 있으므로 정확한 용어 사용이 필수이며, 양국 환경법의 차이를 이해해야 합니다.',
    '통역 시 오염물질 농도 단위(ppm, mg/L, μg/m³)의 변환과 기준치 차이에 주의해야 합니다.',
    '통역 시 폐기물 분류 체계가 한국과 베트남에서 다를 수 있으므로, 해당 국가의 분류 기준에 맞게 설명해야 합니다.',
  ],
  exhibition: [
    '통역 시 전시회 부스 설치, 철거 일정 관련 용어는 시간이 촉박한 상황에서 사용되므로 간결하고 명확하게 전달해야 합니다.',
    '통역 시 전시 규정(부스 높이 제한, 전력 용량, 소방 규정)은 현지 법규와 연결되므로 정확한 전달이 중요합니다.',
    '통역 시 비즈니스 매칭, 상담 요청 시에는 양측의 관심사와 조건을 명확히 파악하여 효율적인 소통을 도와야 합니다.',
  ],
  finance: [
    '통역 시 금융 상품, 이자율, 환율 관련 수치는 정확한 전달이 필수이며, 소수점 자릿수까지 확인해야 합니다.',
    '통역 시 금융 규제 용어는 양국 법률이 다르므로, 해당 국가의 금융 시스템을 이해하고 적절히 설명해야 합니다.',
    '통역 시 투자, 대출 조건은 법적 효력이 있으므로 모호한 표현을 피하고 명확하게 전달해야 합니다.',
  ],
  food: [
    '통역 시 식품 성분, 영양 정보는 정확한 수치와 단위 전달이 중요하며, 양국의 표시 기준 차이를 알아야 합니다.',
    '통역 시 식품 인증(HACCP, ISO, 할랄 등)은 해당 인증의 의미와 요구사항을 이해하고 설명해야 합니다.',
    '통역 시 유통기한, 보관 조건은 식품 안전과 직결되므로 오해 없이 정확하게 전달해야 합니다.',
  ],
  hr: [
    '통역 시 근로계약, 급여, 복리후생 관련 용어는 법적 효력이 있으므로 정확한 전달이 필수입니다.',
    '통역 시 한국과 베트남의 노동법 차이(근로시간, 휴가, 해고 절차)를 이해하고 적절히 설명해야 합니다.',
    '통역 시 직급, 직책명은 양국 기업문화 차이로 직접 대응되지 않을 수 있으므로 역할 설명을 함께 하는 것이 좋습니다.',
  ],
  it: [
    '통역 시 IT 약어는 풀네임과 함께 간단한 기능 설명을 덧붙이면 비전문가도 이해하기 쉽습니다.',
    '통역 시 프로그래밍 용어는 영어 원어를 그대로 사용하는 경우가 많으므로, 맥락에 맞게 한글/베트남어 설명을 추가합니다.',
    '통역 시 시스템 오류, 버그 관련 내용은 기술적 정확성이 중요하므로 불확실한 내용은 개발자에게 확인 후 전달해야 합니다.',
  ],
  legal: [
    '통역 시 법률 용어는 정확한 의미 전달이 필수이며, 오역은 법적 분쟁으로 이어질 수 있으므로 신중해야 합니다.',
    '통역 시 한국법과 베트남법의 차이를 이해하고, 해당 조항의 법적 효력과 적용 범위를 명확히 설명해야 합니다.',
    '통역 시 계약서, 소송 관련 통역은 전문 법률 통역사 자격이 권장되며, 불확실한 용어는 반드시 확인 후 통역해야 합니다.',
  ],
  logistics: [
    '통역 시 물류 일정, 선적 정보는 시간과 비용에 직결되므로 날짜, 시간, 수량을 정확히 전달해야 합니다.',
    '통역 시 인코텀즈(FOB, CIF, DDP 등) 조건에 따른 책임 범위를 명확히 이해하고 설명해야 합니다.',
    '통역 시 통관 서류, 검역 관련 용어는 수출입 지연을 막기 위해 정확한 전달이 중요합니다.',
  ],
  manufacturing: [
    '통역 시 생산 공정, 품질 관리 용어는 제품 품질에 직결되므로 정확한 이해와 전달이 필수입니다.',
    '통역 시 기계 설비 사양, 작동 방법은 안전과 연결되므로 기술 용어를 정확히 전달해야 합니다.',
    '통역 시 불량률, 생산성 관련 수치는 소수점까지 정확히 전달하고, 계산 방식의 차이에 주의해야 합니다.',
  ],
  medical: [
    '통역 시 의료 용어 오역은 환자 안전에 직결되므로 불확실한 내용은 반드시 의료진에게 확인 후 통역해야 합니다.',
    '통역 시 약품명은 성분명(generic)과 상품명(brand)을 구분하고, 복용법과 부작용을 정확히 전달해야 합니다.',
    '통역 시 환자의 증상 표현은 문화적 차이가 있을 수 있으므로, 구체적인 확인 질문을 통해 정확한 정보를 파악해야 합니다.',
  ],
  realEstate: [
    '통역 시 부동산 면적 단위(㎡, 평, m²)의 환산에 주의하고, 베트남에서는 m²를 주로 사용함을 기억해야 합니다.',
    '통역 시 부동산 계약 조건(보증금, 월세, 관리비)은 법적 효력이 있으므로 금액과 기간을 정확히 전달해야 합니다.',
    '통역 시 한국과 베트남의 부동산 소유권, 임대차 법률 차이를 이해하고 적절히 설명해야 합니다.',
  ],
  textile: [
    '통역 시 원단 규격(중량, 폭, 밀도)은 품질과 가격에 직결되므로 정확한 수치 전달이 중요합니다.',
    '통역 시 섬유 성분 표기는 국제 기준(면 cotton, 폴리에스터 polyester)과 현지 표현을 모두 알아야 합니다.',
    '통역 시 염색, 가공 관련 용어는 기술적 정확성이 중요하며, 색상 코드(팬톤 등)를 함께 전달하면 오해를 줄일 수 있습니다.',
  ],
  tourism: [
    '통역 시 관광 일정, 예약 정보는 고객 만족도에 직결되므로 시간, 장소, 인원을 정확히 확인하고 전달해야 합니다.',
    '통역 시 문화 차이로 인한 오해를 예방하기 위해 양국의 관습, 예절에 대한 배경 설명을 추가하면 좋습니다.',
    '통역 시 가격, 환불 정책 등 금전 관련 내용은 명확하게 전달하여 분쟁을 예방해야 합니다.',
  ],
  trade: [
    '통역 시 무역 조건(인코텀즈), 결제 방식(L/C, T/T)은 계약의 핵심이므로 정확한 용어 사용이 필수입니다.',
    '통역 시 관세, 원산지 증명 관련 용어는 통관에 직결되므로 해당 국가의 규정을 이해해야 합니다.',
    '통역 시 클레임, 분쟁 해결 조항은 법적 효력이 있으므로 양측의 권리와 의무를 명확히 전달해야 합니다.',
  ],
};

// ============ 도메인별 관련 용어 풀 ============

const RELATED_TERMS_POOL: Record<string, string[]> = {
  automotive: ['엔진', '변속기', '브레이크', '서스펜션', '배터리', '타이어', '에어백', '안전벨트', '점화플러그', '냉각수', '연료필터', '머플러'],
  beauty: ['스킨케어', '메이크업', '선케어', '클렌징', '토너', '에센스', '크림', '마스크팩', '파운데이션', '립스틱', 'OEM', 'ODM'],
  construction: ['철근', '콘크리트', '거푸집', '레미콘', '타설', '양생', '배근', '도면', '설계', '시공', '감리', '준공'],
  education: ['대학교', '학위', '학점', '전공', '교수', '강의', '시험', '학기', '졸업', '입학', '장학금', '유학'],
  electronics: ['PCB', '반도체', 'SMT', '납땜', '검사', '불량', '회로', '부품', '조립', '테스트', '품질', '출하'],
  environment: ['폐수처리', '대기오염', '폐기물', '재활용', '환경영향평가', '배출', '측정', '규제', '인허가', '모니터링'],
  exhibition: ['부스', '전시', '설치', '철거', '바이어', '상담', '카탈로그', '샘플', '계약', 'MOU', '네트워킹', '비즈매칭'],
  finance: ['은행', '대출', '이자', '환율', '송금', '계좌', '투자', '보험', '세금', '결제', '신용', '담보'],
  food: ['식품안전', 'HACCP', '유통기한', '성분', '영양', '첨가물', '검사', '인증', '위생', '포장', '라벨링', '수출'],
  hr: ['채용', '급여', '복리후생', '근로계약', '해고', '퇴직금', '연차', '4대보험', '인사평가', '승진', '교육훈련'],
  it: ['개발', '서버', '데이터베이스', 'API', '프론트엔드', '백엔드', '클라우드', '보안', '테스트', '배포', '유지보수'],
  legal: ['계약', '소송', '변호사', '법원', '판결', '조항', '위반', '손해배상', '중재', '합의', '법인', '등기'],
  logistics: ['운송', '창고', '통관', '선적', '컨테이너', '포워딩', '재고', '배송', '추적', 'FTA', '관세', '검역'],
  manufacturing: ['생산', '조립', '품질관리', '불량률', '공정', '설비', '자동화', '원자재', '재고', '납기', '검사', '출하'],
  medical: ['진료', '처방', '검사', '입원', '수술', '약물', '부작용', '의료보험', '통증', '증상', '진단', '치료'],
  realEstate: ['매매', '임대', '전세', '월세', '계약', '등기', '담보', '중개', '감정', '건축', '개발', '투자'],
  textile: ['원단', '봉제', '염색', '가공', '패턴', '샘플', '오더', '납기', '검품', '포장', '선적', '클레임'],
  tourism: ['예약', '호텔', '항공', '가이드', '관광지', '일정', '비자', '환전', '보험', '픽업', '투어', '식사'],
  trade: ['수출', '수입', 'FOB', 'CIF', 'L/C', '통관', '관세', '원산지', '인보이스', '선하증권', '클레임', 'FTA'],
};

// ============ 메인 처리 함수 ============

function processTerm(term: any, domain: string, allTermsInDomain: any[]): any {
  const updated = { ...term };
  let modified = false;

  // 1. meaningKo의 "[통역 시 주의: 보완 필요]" 교체
  if (updated.meaningKo && updated.meaningKo.includes('[통역 시 주의: 보완 필요]')) {
    const tips = INTERPRETER_TIPS[domain] || INTERPRETER_TIPS['trade'];
    const tip = tips[Math.floor(Math.random() * tips.length)];
    updated.meaningKo = updated.meaningKo.replace('[통역 시 주의: 보완 필요]', tip);
    modified = true;
  }

  // 2. commonMistakes의 "실수 N" 패턴 개선
  if (Array.isArray(updated.commonMistakes)) {
    updated.commonMistakes = updated.commonMistakes.map((cm: any, idx: number) => {
      if (typeof cm === 'object' && cm.mistake && cm.mistake.startsWith('실수 ')) {
        return {
          mistake: cm.correction.split('을 ')[0] || `${updated.korean} 관련 흔한 실수 ${idx + 1}`,
          correction: cm.correction,
          explanation: cm.explanation
        };
      }
      return cm;
    });
    modified = true;
  }

  // 3. relatedTerms의 "[관련용어N]" 교체
  if (Array.isArray(updated.relatedTerms)) {
    const pool = RELATED_TERMS_POOL[domain] || [];
    const existingTerms = allTermsInDomain.map(t => t.korean);
    const availableTerms = [...pool, ...existingTerms].filter(t =>
      t !== updated.korean && !updated.relatedTerms.includes(t)
    );

    updated.relatedTerms = updated.relatedTerms.map((rt: string) => {
      if (rt.startsWith('[관련용어')) {
        const replacement = availableTerms.shift();
        modified = true;
        return replacement || rt;
      }
      return rt;
    });
  }

  // 4. culturalNote의 "[보완 필요]" 교체
  if (updated.culturalNote && updated.culturalNote.includes('[보완 필요]')) {
    updated.culturalNote = `한국과 베트남의 ${domain} 분야에서 '${updated.korean}'에 대한 인식과 사용 방식에는 차이가 있을 수 있습니다. 통역 시 양국의 문화적 맥락을 고려하여 적절히 설명하는 것이 좋습니다.`;
    modified = true;
  }

  // 5. examples의 "[보완 필요]" 교체
  if (Array.isArray(updated.examples)) {
    updated.examples = updated.examples.map((ex: any, idx: number) => {
      if (ex.ko && ex.ko.includes('[보완 필요]')) {
        modified = true;
        const situations = ['formal', 'onsite', 'informal'];
        return {
          ko: `${updated.korean}${idx === 0 ? '에 대해 설명해 주세요.' : idx === 1 ? ' 확인 부탁드립니다.' : ' 관련 문의드립니다.'}`,
          vi: ex.vi.includes('[') ? `Vui lòng ${idx === 0 ? 'giải thích về' : idx === 1 ? 'kiểm tra' : 'cho hỏi về'} ${updated.vietnamese || updated.korean}.` : ex.vi,
          situation: ex.situation || situations[idx] || 'formal'
        };
      }
      return ex;
    });
  }

  return { term: updated, modified };
}

async function main() {
  const args = process.argv.slice(2);
  const domainArg = args.find(a => a.startsWith('--domain='));
  const dryRun = args.includes('--dry-run');
  const targetDomain = domainArg ? domainArg.split('=')[1] : null;

  const termsDir = path.join(__dirname, '../data/terms');
  const files = fs.readdirSync(termsDir).filter(f => f.endsWith('.json') && !f.startsWith('_'));

  console.log('\n' + '='.repeat(60));
  console.log('📝 플레이스홀더 실제 콘텐츠 채우기');
  console.log('='.repeat(60));
  if (dryRun) console.log('⚠️  DRY RUN 모드\n');

  let totalModified = 0;

  for (const file of files) {
    const domain = file.replace('.json', '');
    if (targetDomain && domain !== targetDomain) continue;

    const filePath = path.join(termsDir, file);
    const terms: any[] = JSON.parse(fs.readFileSync(filePath, 'utf-8'));
    let fileModified = false;
    let domainModCount = 0;

    for (let i = 0; i < terms.length; i++) {
      const { term: updated, modified } = processTerm(terms[i], domain, terms);
      if (modified) {
        terms[i] = updated;
        fileModified = true;
        domainModCount++;
      }
    }

    if (fileModified) {
      totalModified += domainModCount;
      console.log(`✓ ${domain}: ${domainModCount}개 수정`);
      if (!dryRun) {
        fs.writeFileSync(filePath, JSON.stringify(terms, null, 2) + '\n');
      }
    }
  }

  console.log('\n' + '='.repeat(60));
  console.log(`📊 총 ${totalModified}개 항목 수정됨`);
  if (dryRun) console.log('⚠️  실제 저장하려면 --dry-run 제거');
  console.log('='.repeat(60) + '\n');
}

main();
