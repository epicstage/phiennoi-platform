// 용어 데이터 로드 및 관리 유틸리티

import { domains } from "@/data/pseo-dimensions";
import type { Term, TermWithDomain } from "@/types/term";

// 도메인별 용어 데이터 동적 로드
const termDataCache: Record<string, Term[]> = {};

export async function getTermsByDomain(domainSlug: string): Promise<Term[]> {
  if (termDataCache[domainSlug]) {
    return termDataCache[domainSlug];
  }

  try {
    const data = await import(`@/data/terms/${domainSlug}.json`);
    termDataCache[domainSlug] = data.default as Term[];
    return termDataCache[domainSlug];
  } catch {
    return [];
  }
}

export function getTermsByDomainSync(domainSlug: string): Term[] {
  // 빌드 타임에 사용할 동기 버전
  // eslint-disable-next-line @typescript-eslint/no-require-imports
  const data = require(`@/data/terms/${domainSlug}.json`);
  return data as Term[];
}

export async function getTermBySlug(
  domainSlug: string,
  termSlug: string
): Promise<TermWithDomain | null> {
  const terms = await getTermsByDomain(domainSlug);
  const term = terms.find((t) => t.slug === termSlug);

  if (!term) return null;

  const domain = domains.find((d) => d.slug === domainSlug);
  if (!domain) return null;

  return {
    ...term,
    domain: domainSlug,
    domainName: domain.name,
    domainNameVi: domain.nameVi,
  };
}

export async function getAllTermSlugs(): Promise<
  { domain: string; term: string }[]
> {
  const allSlugs: { domain: string; term: string }[] = [];

  for (const domain of domains) {
    try {
      const terms = await getTermsByDomain(domain.slug);
      for (const term of terms) {
        allSlugs.push({
          domain: domain.slug,
          term: term.slug,
        });
      }
    } catch {
      // 해당 도메인의 데이터가 없으면 스킵
      continue;
    }
  }

  return allSlugs;
}

// 전체 용어 수 계산 (빌드 타임)
export function getTotalTermCount(): number {
  return domains.reduce((sum, domain) => {
    try {
      const terms = getTermsByDomainSync(domain.slug);
      return sum + terms.length;
    } catch {
      return sum;
    }
  }, 0);
}

// 전체 용어 수를 포맷팅 (예: 4,794 → "4,700+")
export function getFormattedTermCount(): string {
  const total = getTotalTermCount();
  const rounded = Math.floor(total / 100) * 100;
  return `${rounded.toLocaleString()}+`;
}

export function getRelatedTerms(
  allTerms: Term[],
  relatedSlugs: string[]
): Term[] {
  return allTerms.filter((t) => relatedSlugs.includes(t.slug));
}
