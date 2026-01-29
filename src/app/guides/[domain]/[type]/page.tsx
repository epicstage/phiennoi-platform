import { Metadata } from "next";
import Link from "next/link";
import { notFound } from "next/navigation";
import { domains, interpretTypes } from "@/data/pseo-dimensions";
import type { GuideContent } from "@/types/term";
import Header from "@/components/Header";
import Footer from "@/components/Footer";
import GuideSchema from "@/components/schema/GuideSchema";

// 가이드 콘텐츠 JSON 로드 (없으면 null)
function loadGuideContent(
  domainSlug: string,
  typeSlug: string
): GuideContent | null {
  try {
    // eslint-disable-next-line @typescript-eslint/no-require-imports
    return require(`@/data/guides/${domainSlug}-${typeSlug}.json`) as GuideContent;
  } catch {
    return null;
  }
}

// 관련 용어 로드
function loadDomainTerms(domainSlug: string): { slug: string; korean: string; vietnamese: string; pronunciation?: string }[] {
  try {
    // eslint-disable-next-line @typescript-eslint/no-require-imports
    return require(`@/data/terms/${domainSlug}.json`);
  } catch {
    return [];
  }
}

// 모든 도메인 × 통역유형 조합에 대해 정적 페이지 생성
export function generateStaticParams() {
  const params: { domain: string; type: string }[] = [];

  for (const domain of domains) {
    for (const interpretType of interpretTypes) {
      params.push({
        domain: domain.slug,
        type: interpretType.slug,
      });
    }
  }

  return params;
}

// 동적 메타데이터
export async function generateMetadata({
  params,
}: {
  params: Promise<{ domain: string; type: string }>;
}): Promise<Metadata> {
  const { domain: domainSlug, type: typeSlug } = await params;

  const domain = domains.find((d) => d.slug === domainSlug);
  const interpretType = interpretTypes.find((t) => t.slug === typeSlug);

  if (!domain || !interpretType) {
    return { title: "페이지를 찾을 수 없습니다" };
  }

  const guide = loadGuideContent(domainSlug, typeSlug);

  const title = `${domain.name} ${interpretType.name} 가이드 | 한-베 통역`;
  const description = guide
    ? guide.overview.slice(0, 155)
    : `${domain.name} 분야 ${interpretType.name} 완벽 가이드. ${domain.keywords.join(", ")} 관련 통역 준비사항, 핵심 표현, 주의점을 알아보세요.`;

  return {
    title,
    description,
    keywords: [
      `${domain.name} ${interpretType.name}`,
      `${domain.name} 베트남어 통역`,
      `${domain.nameVi} ${interpretType.nameVi}`,
      `${interpretType.nameVi}`,
      ...domain.keywords.map((k) => `${k} 통역`),
    ],
    openGraph: {
      title,
      description,
      type: "article",
      locale: "ko_KR",
      alternateLocale: "vi_VN",
    },
  };
}

export default async function GuideDetailPage({
  params,
}: {
  params: Promise<{ domain: string; type: string }>;
}) {
  const { domain: domainSlug, type: typeSlug } = await params;

  const domain = domains.find((d) => d.slug === domainSlug);
  const interpretType = interpretTypes.find((t) => t.slug === typeSlug);

  if (!domain || !interpretType) {
    notFound();
  }

  const guide = loadGuideContent(domainSlug, typeSlug);
  const domainTerms = loadDomainTerms(domainSlug);

  // 관련 통역 유형 (같은 도메인)
  const relatedTypes = interpretTypes.filter(
    (t) => t.slug !== interpretType.slug
  );

  // 관련 도메인 (같은 통역 유형)
  const relatedDomains = domains.filter((d) => d.slug !== domain.slug);

  // 가이드에 연결된 용어 찾기
  const linkedTerms = guide?.relatedTermSlugs
    ? domainTerms.filter((t) => guide.relatedTermSlugs.includes(t.slug))
    : domainTerms.slice(0, 8);

  return (
    <div className="min-h-screen bg-background">
      <GuideSchema
        domainName={domain.name}
        domainNameVi={domain.nameVi}
        domainSlug={domain.slug}
        typeName={interpretType.name}
        typeNameVi={interpretType.nameVi}
        typeSlug={interpretType.slug}
        typeDescription={interpretType.description}
        domainKeywords={domain.keywords}
      />

      <Header />

      <article className="max-w-4xl mx-auto px-4 sm:px-6 py-8 sm:py-10">
        {/* Breadcrumb */}
        <nav className="text-sm text-foreground-muted mb-6">
          <Link href="/" className="hover:text-foreground transition">
            홈
          </Link>
          <span className="mx-2 text-border-default">/</span>
          <Link href="/guides" className="hover:text-foreground transition">
            가이드
          </Link>
          <span className="mx-2 text-border-default">/</span>
          <Link
            href={`/guides/${domain.slug}`}
            className="hover:text-foreground transition"
          >
            {domain.name}
          </Link>
          <span className="mx-2 text-border-default">/</span>
          <span className="text-foreground">{interpretType.name}</span>
        </nav>

        {/* 헤더 */}
        <header className="mb-10">
          <div className="flex flex-wrap items-center gap-2 mb-4">
            <span className="px-3 py-1 bg-red-primary/10 text-red-primary text-sm rounded-full border border-red-primary/20">
              {domain.name}
            </span>
            <span className="px-3 py-1 bg-background-surface text-foreground-secondary text-sm rounded-full border border-border-default">
              {domain.nameVi}
            </span>
            <span className="px-3 py-1 bg-green-success/10 text-green-success text-sm rounded-full border border-green-success/20">
              {interpretType.name}
            </span>
          </div>

          <h1 className="text-3xl md:text-4xl font-bold text-foreground mb-4">
            {domain.name} {interpretType.name} 가이드
          </h1>
          <p className="text-base text-foreground-muted mb-2">
            Hướng dẫn {interpretType.nameVi} ngành {domain.nameVi}
          </p>

          {guide ? (
            <p className="text-lg text-foreground-secondary leading-relaxed">
              {guide.overview}
            </p>
          ) : (
            <p className="text-lg text-foreground-secondary leading-relaxed">
              {domain.name} 분야의 {interpretType.name}은{" "}
              {interpretType.description}의 형태로 진행됩니다. 특히{" "}
              {domain.keywords[0]}과 {domain.keywords[1]} 관련 내용이 자주
              다뤄지며, 해당 분야의 전문 용어 숙지가 필수입니다.
            </p>
          )}
        </header>

        {/* 목차 */}
        <nav className="bg-background-secondary rounded-lg p-6 mb-10">
          <h2 className="text-lg font-semibold text-foreground mb-4">
            📑 목차
          </h2>
          <ul className="space-y-2">
            {guide?.characteristics && (
              <li>
                <a
                  href="#characteristics"
                  className="text-red-primary hover:underline"
                >
                  1. 이 통역의 특징
                </a>
              </li>
            )}
            <li>
              <a
                href="#preparation"
                className="text-red-primary hover:underline"
              >
                {guide?.characteristics ? "2" : "1"}. 사전 준비사항
              </a>
            </li>
            <li>
              <a
                href="#expressions"
                className="text-red-primary hover:underline"
              >
                {guide?.characteristics ? "3" : "2"}. 핵심 표현
              </a>
            </li>
            {guide?.scenarios && guide.scenarios.length > 0 && (
              <li>
                <a
                  href="#scenarios"
                  className="text-red-primary hover:underline"
                >
                  4. 실전 시나리오
                </a>
              </li>
            )}
            {guide?.checklists && guide.checklists.length > 0 && (
              <li>
                <a
                  href="#checklists"
                  className="text-red-primary hover:underline"
                >
                  5. 체크리스트
                </a>
              </li>
            )}
            <li>
              <a
                href="#cultural"
                className="text-red-primary hover:underline"
              >
                {guide ? "6" : "3"}. 문화적 주의사항
              </a>
            </li>
            <li>
              <a
                href="#mistakes"
                className="text-red-primary hover:underline"
              >
                {guide ? "7" : "4"}. 흔한 실수
              </a>
            </li>
            <li>
              <a href="#terms" className="text-red-primary hover:underline">
                {guide ? "8" : "5"}. 관련 용어
              </a>
            </li>
          </ul>
        </nav>

        {/* 이 통역의 특징 (가이드 JSON 있을 때만) */}
        {guide?.characteristics && guide.characteristics.length > 0 && (
          <section id="characteristics" className="mb-12">
            <h2 className="text-2xl font-bold text-foreground mb-6 pb-2 border-b border-border-default">
              1. 이 통역의 특징
            </h2>
            <div className="space-y-3">
              {guide.characteristics.map((char, i) => (
                <div
                  key={i}
                  className="flex items-start gap-3 bg-background-card border border-border-default rounded-lg p-4"
                >
                  <span className="text-red-primary font-bold shrink-0 mt-0.5">
                    {i + 1}
                  </span>
                  <p className="text-foreground-secondary leading-relaxed">
                    {char}
                  </p>
                </div>
              ))}
            </div>
          </section>
        )}

        {/* 사전 준비사항 */}
        <section id="preparation" className="mb-12">
          <h2 className="text-2xl font-bold text-foreground mb-6 pb-2 border-b border-border-default">
            {guide?.characteristics ? "2" : "1"}. 사전 준비사항
          </h2>

          {guide?.preparation && guide.preparation.length > 0 ? (
            <div className="space-y-6">
              {guide.preparation.map((prep, i) => (
                <div
                  key={i}
                  className="border-l-4 border-red-primary bg-background-card rounded-r-lg p-5"
                >
                  <h3 className="font-semibold text-foreground text-lg mb-2">
                    {prep.title}
                  </h3>
                  <p className="text-foreground-secondary leading-relaxed mb-4">
                    {prep.description}
                  </p>
                  {prep.tips && prep.tips.length > 0 && (
                    <ul className="space-y-2">
                      {prep.tips.map((tip, j) => (
                        <li
                          key={j}
                          className="flex items-start gap-2 text-foreground-secondary"
                        >
                          <span className="text-green-success shrink-0">
                            •
                          </span>
                          <span>{tip}</span>
                        </li>
                      ))}
                    </ul>
                  )}
                </div>
              ))}
            </div>
          ) : (
            <div className="space-y-4">
              <div className="border-l-4 border-red-primary pl-4">
                <h3 className="font-semibold text-foreground mb-1">
                  용어 사전 준비
                </h3>
                <p className="text-foreground-secondary">
                  {domain.name} 분야 전문 용어 목록을 미리 준비하세요. 특히{" "}
                  {domain.keywords.join(", ")} 관련 용어가 중요합니다.
                </p>
                <Link
                  href={`/terms/${domain.slug}`}
                  className="text-red-primary hover:underline text-sm mt-2 inline-block"
                >
                  → {domain.name} 용어사전 보기
                </Link>
              </div>
              <div className="border-l-4 border-green-success pl-4">
                <h3 className="font-semibold text-foreground mb-1">
                  자료 사전 검토
                </h3>
                <p className="text-foreground-secondary">
                  행사/미팅 관련 자료를 미리 받아 검토하세요. 회사 소개서, 제품
                  카탈로그, 발표 자료 등을 확인합니다.
                </p>
              </div>
              <div className="border-l-4 border-foreground-muted pl-4">
                <h3 className="font-semibold text-foreground mb-1">
                  목적 파악
                </h3>
                <p className="text-foreground-secondary">
                  통역 의뢰인의 목적과 기대를 미리 파악하세요. 계약 체결, 기술
                  협의, 일반 상담 등 목적에 따라 준비가 달라집니다.
                </p>
              </div>
            </div>
          )}
        </section>

        {/* 핵심 표현 */}
        <section id="expressions" className="mb-12">
          <h2 className="text-2xl font-bold text-foreground mb-6 pb-2 border-b border-border-default">
            {guide?.characteristics ? "3" : "2"}. 핵심 표현
          </h2>

          {guide?.keyExpressions && guide.keyExpressions.length > 0 ? (
            <div className="space-y-4">
              {guide.keyExpressions.map((expr, i) => (
                <div
                  key={i}
                  className="border border-border-default rounded-lg overflow-hidden"
                >
                  <div className="bg-background-surface px-4 py-2 border-b border-border-default flex items-center justify-between">
                    <span className="text-xs font-semibold text-foreground-muted tracking-wider uppercase">
                      {expr.situation}
                    </span>
                    {expr.note && (
                      <span className="text-xs text-foreground-muted">
                        💡 {expr.note}
                      </span>
                    )}
                  </div>
                  <div className="bg-background-card p-4 border-b border-border-default">
                    <span className="text-xs font-semibold text-foreground-muted mb-1 block tracking-wider">
                      한국어
                    </span>
                    <p className="text-foreground">{expr.ko}</p>
                  </div>
                  <div className="bg-background-surface p-4">
                    <span className="text-xs font-semibold text-red-primary mb-1 block tracking-wider">
                      Tiếng Việt
                    </span>
                    <p className="text-foreground">{expr.vi}</p>
                  </div>
                </div>
              ))}
            </div>
          ) : (
            <div className="space-y-4">
              <div className="bg-background-secondary rounded-lg p-4">
                <h3 className="font-semibold text-foreground mb-3">
                  인사 및 소개
                </h3>
                <div className="space-y-2">
                  <div className="flex gap-4">
                    <span className="text-foreground-secondary shrink-0">
                      한:
                    </span>
                    <span className="text-foreground">
                      안녕하세요, {domain.name} 분야 통역을 맡은
                      OOO입니다.
                    </span>
                  </div>
                  <div className="flex gap-4">
                    <span className="text-red-primary shrink-0">베:</span>
                    <span className="text-foreground">
                      Xin chào, tôi là OOO, phiên dịch viên chuyên ngành{" "}
                      {domain.nameVi}.
                    </span>
                  </div>
                </div>
              </div>
              <div className="bg-background-secondary rounded-lg p-4">
                <h3 className="font-semibold text-foreground mb-3">
                  확인 요청
                </h3>
                <div className="space-y-2">
                  <div className="flex gap-4">
                    <span className="text-foreground-secondary shrink-0">
                      한:
                    </span>
                    <span className="text-foreground">
                      제가 이해한 것이 맞는지 확인해 주시겠습니까?
                    </span>
                  </div>
                  <div className="flex gap-4">
                    <span className="text-red-primary shrink-0">베:</span>
                    <span className="text-foreground">
                      Xin vui lòng xác nhận xem tôi hiểu có đúng không?
                    </span>
                  </div>
                </div>
              </div>
              <div className="bg-background-secondary rounded-lg p-4">
                <h3 className="font-semibold text-foreground mb-3">
                  재설명 요청
                </h3>
                <div className="space-y-2">
                  <div className="flex gap-4">
                    <span className="text-foreground-secondary shrink-0">
                      한:
                    </span>
                    <span className="text-foreground">
                      죄송합니다, 다시 한 번 설명해 주시겠습니까?
                    </span>
                  </div>
                  <div className="flex gap-4">
                    <span className="text-red-primary shrink-0">베:</span>
                    <span className="text-foreground">
                      Xin lỗi, anh/chị có thể giải thích lại một lần nữa
                      được không?
                    </span>
                  </div>
                </div>
              </div>
            </div>
          )}
        </section>

        {/* 실전 시나리오 (가이드 JSON 있을 때만) */}
        {guide?.scenarios && guide.scenarios.length > 0 && (
          <section id="scenarios" className="mb-12">
            <h2 className="text-2xl font-bold text-foreground mb-6 pb-2 border-b border-border-default">
              4. 실전 시나리오
            </h2>
            <div className="space-y-8">
              {guide.scenarios.map((scenario, i) => (
                <div
                  key={i}
                  className="border border-border-default rounded-lg overflow-hidden"
                >
                  <div className="bg-red-primary/10 p-5 border-b border-border-default">
                    <h3 className="text-lg font-semibold text-foreground mb-1">
                      시나리오 {i + 1}: {scenario.title}
                    </h3>
                    <p className="text-sm text-red-primary">
                      {scenario.titleVi}
                    </p>
                    <p className="text-foreground-secondary mt-2">
                      {scenario.description}
                    </p>
                  </div>
                  <div className="divide-y divide-border-default">
                    {scenario.dialogues.map((dialogue, j) => (
                      <div key={j} className="p-4">
                        <div className="flex items-center gap-2 mb-2">
                          <span
                            className={`px-2 py-0.5 rounded text-xs font-semibold ${
                              dialogue.speaker === "바이어" ||
                              dialogue.speaker.includes("베트남")
                                ? "bg-red-primary/10 text-red-primary"
                                : "bg-background-surface text-foreground-secondary"
                            }`}
                          >
                            {dialogue.speaker}
                          </span>
                        </div>
                        <p className="text-foreground mb-1">{dialogue.ko}</p>
                        <p className="text-red-primary text-sm">
                          {dialogue.vi}
                        </p>
                      </div>
                    ))}
                  </div>
                </div>
              ))}
            </div>
          </section>
        )}

        {/* 체크리스트 (가이드 JSON 있을 때만) */}
        {guide?.checklists && guide.checklists.length > 0 && (
          <section id="checklists" className="mb-12">
            <h2 className="text-2xl font-bold text-foreground mb-6 pb-2 border-b border-border-default">
              5. 체크리스트
            </h2>
            <div className="grid md:grid-cols-2 gap-4">
              {guide.checklists.map((checklist, i) => (
                <div
                  key={i}
                  className="bg-background-card border border-border-default rounded-lg p-5"
                >
                  <h3 className="font-semibold text-foreground mb-3">
                    ✅ {checklist.category}
                  </h3>
                  <ul className="space-y-2">
                    {checklist.items.map((item, j) => (
                      <li
                        key={j}
                        className="flex items-start gap-2 text-foreground-secondary text-sm"
                      >
                        <span className="text-foreground-muted shrink-0">
                          ☐
                        </span>
                        <span>{item}</span>
                      </li>
                    ))}
                  </ul>
                </div>
              ))}
            </div>
          </section>
        )}

        {/* 문화적 주의사항 */}
        <section id="cultural" className="mb-12">
          <h2 className="text-2xl font-bold text-foreground mb-6 pb-2 border-b border-border-default">
            {guide ? "6" : "3"}. 문화적 주의사항
          </h2>

          {guide?.culturalNotes && guide.culturalNotes.length > 0 ? (
            <div className="space-y-3">
              {guide.culturalNotes.map((note, i) => (
                <div
                  key={i}
                  className="border-l-4 border-red-primary bg-background-card rounded-r-lg p-4"
                >
                  <p className="text-foreground-secondary leading-relaxed">
                    {note}
                  </p>
                </div>
              ))}
            </div>
          ) : (
            <div className="bg-background-surface border border-border-default rounded-lg p-6">
              <ul className="space-y-3 text-foreground-secondary">
                <li className="flex items-start gap-2">
                  <span className="text-green-success">✓</span>
                  <span>
                    {domain.name} 분야 특수 용어는 미리 상호 확인하세요
                  </span>
                </li>
                <li className="flex items-start gap-2">
                  <span className="text-green-success">✓</span>
                  <span>숫자, 단위, 날짜는 반드시 재확인하세요</span>
                </li>
                <li className="flex items-start gap-2">
                  <span className="text-green-success">✓</span>
                  <span>
                    메모를 적극 활용하여 핵심 내용을 기록하세요
                  </span>
                </li>
                <li className="flex items-start gap-2">
                  <span className="text-green-success">✓</span>
                  <span>
                    문화적 차이로 인한 오해 소지가 있으면 보충 설명하세요
                  </span>
                </li>
              </ul>
            </div>
          )}
        </section>

        {/* 흔한 실수 */}
        <section id="mistakes" className="mb-12">
          <h2 className="text-2xl font-bold text-foreground mb-6 pb-2 border-b border-border-default">
            {guide ? "7" : "4"}. 흔한 실수
          </h2>

          {guide?.commonMistakes && guide.commonMistakes.length > 0 ? (
            <div className="bg-background-card border border-red-primary/20 rounded-lg p-5">
              <ul className="space-y-3">
                {guide.commonMistakes.map((mistake, i) => (
                  <li
                    key={i}
                    className="flex items-start gap-3 text-foreground-secondary"
                  >
                    <span className="text-red-primary shrink-0 mt-0.5">
                      ✗
                    </span>
                    <span className="leading-relaxed">{mistake}</span>
                  </li>
                ))}
              </ul>
            </div>
          ) : (
            <div className="bg-background-surface border border-red-primary/30 rounded-lg p-6">
              <ul className="space-y-3 text-foreground-secondary">
                <li className="flex items-start gap-2">
                  <span className="text-red-primary">✗</span>
                  <span>임의로 내용을 추가하거나 생략하지 마세요</span>
                </li>
                <li className="flex items-start gap-2">
                  <span className="text-red-primary">✗</span>
                  <span>개인적인 의견을 통역에 섞지 마세요</span>
                </li>
                <li className="flex items-start gap-2">
                  <span className="text-red-primary">✗</span>
                  <span>비밀 정보를 제3자에게 누설하지 마세요</span>
                </li>
                <li className="flex items-start gap-2">
                  <span className="text-red-primary">✗</span>
                  <span>확실하지 않은 내용을 추측으로 통역하지 마세요</span>
                </li>
                <li className="flex items-start gap-2">
                  <span className="text-red-primary">✗</span>
                  <span>감정적인 표현을 과장하거나 축소하지 마세요</span>
                </li>
              </ul>
            </div>
          )}
        </section>

        {/* 관련 용어 (P3 내부 링크) */}
        <section id="terms" className="mb-12">
          <h2 className="text-2xl font-bold text-foreground mb-6 pb-2 border-b border-border-default">
            {guide ? "8" : "5"}. {domain.name} 관련 용어
          </h2>
          {linkedTerms.length > 0 ? (
            <div className="grid sm:grid-cols-2 lg:grid-cols-3 gap-3">
              {linkedTerms.map((t) => (
                <Link
                  key={t.slug}
                  href={`/terms/${domainSlug}/${t.slug}`}
                  className="p-4 border border-border-default rounded-lg hover:border-red-primary/50 bg-background-card transition"
                >
                  <p className="font-medium text-foreground">{t.korean}</p>
                  <p className="text-sm text-red-primary">{t.vietnamese}</p>
                  {t.pronunciation && (
                    <p className="text-xs text-foreground-muted mt-1">
                      [{t.pronunciation}]
                    </p>
                  )}
                </Link>
              ))}
            </div>
          ) : (
            <p className="text-foreground-secondary">
              <Link
                href={`/terms/${domainSlug}`}
                className="text-red-primary hover:underline"
              >
                {domain.name} 용어사전 보기 →
              </Link>
            </p>
          )}
          <div className="mt-4">
            <Link
              href={`/terms/${domainSlug}`}
              className="text-red-primary hover:underline text-sm"
            >
              {domain.name} 전체 용어사전 보기 →
            </Link>
          </div>
        </section>

        {/* CTA: 통역사 등록 */}
        <section className="bg-background-card border border-red-primary/30 rounded-lg p-8 mb-10">
          <h2 className="text-2xl font-bold text-foreground mb-3">
            {domain.name} {interpretType.name} 경험이 있으신가요?
          </h2>
          <p className="text-foreground-secondary mb-6">
            이력서를 등록하고 {domain.name} 분야 {interpretType.name}{" "}
            의뢰를 받아보세요. 경험 많은 통역사를 찾는 기업들이 기다리고
            있습니다!
          </p>
          <Link
            href="/upload"
            className="inline-flex items-center gap-2 bg-red-primary text-white px-6 py-3 rounded font-semibold hover:bg-red-hover transition"
          >
            이력서 등록하기
          </Link>
        </section>

        {/* 관련 가이드 (내부 링크) */}
        <div className="border-t border-border-default pt-8 space-y-6">
          <div>
            <h3 className="text-lg font-semibold text-foreground mb-4">
              {domain.name} 분야 다른 통역 유형
            </h3>
            <div className="grid sm:grid-cols-2 lg:grid-cols-4 gap-2">
              {relatedTypes.map((t) => (
                <Link
                  key={t.slug}
                  href={`/guides/${domain.slug}/${t.slug}`}
                  className="p-3 bg-background-card border border-border-default hover:border-red-primary/40 rounded-lg text-sm transition"
                >
                  <p className="font-medium text-foreground">
                    {domain.name} {t.name}
                  </p>
                  <p className="text-xs text-red-primary">{t.nameVi}</p>
                </Link>
              ))}
            </div>
          </div>

          <div>
            <h3 className="text-lg font-semibold text-foreground mb-4">
              다른 분야 {interpretType.name}
            </h3>
            <div className="grid sm:grid-cols-2 lg:grid-cols-3 gap-2">
              {relatedDomains.map((d) => (
                <Link
                  key={d.slug}
                  href={`/guides/${d.slug}/${interpretType.slug}`}
                  className="p-3 bg-background-card border border-border-default hover:border-red-primary/40 rounded-lg text-sm transition"
                >
                  <p className="font-medium text-foreground">
                    {d.name} {interpretType.name}
                  </p>
                  <p className="text-xs text-foreground-muted">
                    {d.nameVi}
                  </p>
                </Link>
              ))}
            </div>
          </div>
        </div>
      </article>

      <Footer />
    </div>
  );
}
