import { Metadata } from "next";
import Link from "next/link";
import { notFound } from "next/navigation";
import { domains, interpretTypes } from "@/data/pseo-dimensions";
import Header from "@/components/Header";
import Footer from "@/components/Footer";

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

  const title = `${domain.name} ${interpretType.name} 가이드 | 한-베 통역`;
  const description = `${domain.name} 분야 ${interpretType.name} 완벽 가이드. ${domain.keywords.join(", ")} 관련 통역 준비사항, 핵심 표현, 주의점을 알아보세요.`;

  return {
    title,
    description,
    keywords: [
      `${domain.name} ${interpretType.name}`,
      `${domain.name} 베트남어 통역`,
      `${interpretType.nameVi}`,
      ...domain.keywords.map((k) => `${k} 통역`),
    ],
    openGraph: {
      title,
      description,
      type: "article",
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

  // 관련 통역 유형 (같은 도메인)
  const relatedTypes = interpretTypes.filter((t) => t.slug !== interpretType.slug).slice(0, 4);

  // 관련 도메인 (같은 통역 유형)
  const relatedDomains = domains.filter((d) => d.slug !== domain.slug).slice(0, 5);

  return (
    <div className="min-h-screen bg-background">
      <Header />

      <article className="max-w-4xl mx-auto px-4 py-8">
        {/* Breadcrumb */}
        <nav className="text-sm text-foreground-muted mb-6">
          <Link href="/" className="hover:text-red-primary">
            홈
          </Link>
          <span className="mx-2">/</span>
          <Link href="/guides" className="hover:text-red-primary">
            가이드
          </Link>
          <span className="mx-2">/</span>
          <Link href={`/guides/${domain.slug}`} className="hover:text-red-primary">
            {domain.name}
          </Link>
          <span className="mx-2">/</span>
          <span className="text-foreground">{interpretType.name}</span>
        </nav>

        {/* 헤더 */}
        <header className="mb-8">
          <div className="flex flex-wrap items-center gap-2 mb-3">
            <span className="px-3 py-1 bg-background-surface text-red-primary text-sm rounded-full">
              {domain.name}
            </span>
            <span className="px-3 py-1 bg-background-surface text-green-success text-sm rounded-full">
              {interpretType.name}
            </span>
          </div>

          <h1 className="text-3xl md:text-4xl font-bold text-foreground mb-4">
            {domain.name} {interpretType.name} 가이드
          </h1>

          <p className="text-lg text-foreground-secondary">
            {domain.name} 분야 {interpretType.description}을 위한 완벽 가이드.
            {domain.keywords.slice(0, 3).join(", ")} 관련 통역을 준비하세요.
          </p>
        </header>

        {/* 목차 */}
        <nav className="bg-background-secondary rounded-lg p-6 mb-8">
          <h2 className="text-lg font-semibold text-foreground mb-4">목차</h2>
          <ul className="space-y-2">
            <li>
              <a href="#overview" className="text-red-primary hover:underline">
                1. {domain.name} {interpretType.name} 개요
              </a>
            </li>
            <li>
              <a href="#preparation" className="text-red-primary hover:underline">
                2. 사전 준비사항
              </a>
            </li>
            <li>
              <a href="#expressions" className="text-red-primary hover:underline">
                3. 핵심 표현
              </a>
            </li>
            <li>
              <a href="#tips" className="text-red-primary hover:underline">
                4. 통역 팁
              </a>
            </li>
            <li>
              <a href="#cautions" className="text-red-primary hover:underline">
                5. 주의사항
              </a>
            </li>
          </ul>
        </nav>

        {/* 개요 */}
        <section id="overview" className="mb-12">
          <h2 className="text-2xl font-bold text-foreground mb-4 pb-2 border-b border-border-default">
            1. {domain.name} {interpretType.name} 개요
          </h2>
          <p className="text-foreground-secondary mb-4 leading-relaxed">
            {domain.name} 분야의 {interpretType.name}은 {interpretType.description}의 형태로 진행됩니다.
            특히 {domain.keywords[0]}과 {domain.keywords[1]} 관련 내용이 자주 다뤄지며,
            해당 분야의 전문 용어 숙지가 필수입니다.
          </p>
          <div className="bg-background-surface border border-border-default rounded-lg p-4">
            <h3 className="font-semibold text-foreground mb-2">이 가이드의 대상</h3>
            <p className="text-foreground-secondary">
              {domain.name} 분야 {interpretType.name}를 준비하는 통역사,
              {domain.name} 기업의 베트남 진출 담당자,
              한-베 비즈니스 커뮤니케이션이 필요한 분
            </p>
          </div>
        </section>

        {/* 사전 준비사항 */}
        <section id="preparation" className="mb-12">
          <h2 className="text-2xl font-bold text-foreground mb-4 pb-2 border-b border-border-default">
            2. 사전 준비사항
          </h2>
          <div className="space-y-4">
            <div className="border-l-4 border-red-primary pl-4">
              <h3 className="font-semibold text-foreground mb-1">용어 사전 준비</h3>
              <p className="text-foreground-secondary">
                {domain.name} 분야 전문 용어 목록을 미리 준비하세요.
                특히 {domain.keywords.join(", ")} 관련 용어가 중요합니다.
              </p>
              <Link
                href={`/terms/${domain.slug}`}
                className="text-red-primary hover:underline text-sm mt-2 inline-block"
              >
                → {domain.name} 용어사전 보기
              </Link>
            </div>
            <div className="border-l-4 border-green-success pl-4">
              <h3 className="font-semibold text-foreground mb-1">자료 사전 검토</h3>
              <p className="text-foreground-secondary">
                행사/미팅 관련 자료를 미리 받아 검토하세요.
                회사 소개서, 제품 카탈로그, 발표 자료 등을 확인합니다.
              </p>
            </div>
            <div className="border-l-4 border-foreground-muted pl-4">
              <h3 className="font-semibold text-foreground mb-1">목적 파악</h3>
              <p className="text-foreground-secondary">
                통역 의뢰인의 목적과 기대를 미리 파악하세요.
                계약 체결, 기술 협의, 일반 상담 등 목적에 따라 준비가 달라집니다.
              </p>
            </div>
          </div>
        </section>

        {/* 핵심 표현 */}
        <section id="expressions" className="mb-12">
          <h2 className="text-2xl font-bold text-foreground mb-4 pb-2 border-b border-border-default">
            3. 핵심 표현
          </h2>
          <div className="space-y-4">
            <div className="bg-background-secondary rounded-lg p-4">
              <h3 className="font-semibold text-foreground mb-3">인사 및 소개</h3>
              <div className="space-y-2">
                <div className="flex gap-4">
                  <span className="text-foreground-secondary">한:</span>
                  <span className="text-foreground">안녕하세요, {domain.name} 분야 통역을 맡은 OOO입니다.</span>
                </div>
                <div className="flex gap-4">
                  <span className="text-red-primary">베:</span>
                  <span className="text-foreground">Xin chào, tôi là OOO, phiên dịch viên chuyên ngành {domain.nameVi}.</span>
                </div>
              </div>
            </div>

            <div className="bg-background-secondary rounded-lg p-4">
              <h3 className="font-semibold text-foreground mb-3">확인 요청</h3>
              <div className="space-y-2">
                <div className="flex gap-4">
                  <span className="text-foreground-secondary">한:</span>
                  <span className="text-foreground">제가 이해한 것이 맞는지 확인해 주시겠습니까?</span>
                </div>
                <div className="flex gap-4">
                  <span className="text-red-primary">베:</span>
                  <span className="text-foreground">Xin vui lòng xác nhận xem tôi hiểu có đúng không?</span>
                </div>
              </div>
            </div>

            <div className="bg-background-secondary rounded-lg p-4">
              <h3 className="font-semibold text-foreground mb-3">재설명 요청</h3>
              <div className="space-y-2">
                <div className="flex gap-4">
                  <span className="text-foreground-secondary">한:</span>
                  <span className="text-foreground">죄송합니다, 다시 한 번 설명해 주시겠습니까?</span>
                </div>
                <div className="flex gap-4">
                  <span className="text-red-primary">베:</span>
                  <span className="text-foreground">Xin lỗi, anh/chị có thể giải thích lại một lần nữa được không?</span>
                </div>
              </div>
            </div>
          </div>
        </section>

        {/* 통역 팁 */}
        <section id="tips" className="mb-12">
          <h2 className="text-2xl font-bold text-foreground mb-4 pb-2 border-b border-border-default">
            4. 통역 팁
          </h2>
          <div className="bg-background-surface border border-border-default rounded-lg p-6">
            <ul className="space-y-3 text-foreground-secondary">
              <li className="flex items-start gap-2">
                <span className="text-green-success">&#10003;</span>
                <span>{domain.name} 분야 특수 용어는 미리 상호 확인하세요</span>
              </li>
              <li className="flex items-start gap-2">
                <span className="text-green-success">&#10003;</span>
                <span>숫자, 단위, 날짜는 반드시 재확인하세요</span>
              </li>
              <li className="flex items-start gap-2">
                <span className="text-green-success">&#10003;</span>
                <span>메모를 적극 활용하여 핵심 내용을 기록하세요</span>
              </li>
              <li className="flex items-start gap-2">
                <span className="text-green-success">&#10003;</span>
                <span>문화적 차이로 인한 오해 소지가 있으면 보충 설명하세요</span>
              </li>
              <li className="flex items-start gap-2">
                <span className="text-green-success">&#10003;</span>
                <span>모르는 용어가 나오면 솔직하게 확인 요청하세요</span>
              </li>
            </ul>
          </div>
        </section>

        {/* 주의사항 */}
        <section id="cautions" className="mb-12">
          <h2 className="text-2xl font-bold text-foreground mb-4 pb-2 border-b border-border-default">
            5. 주의사항
          </h2>
          <div className="bg-background-surface border border-red-primary/30 rounded-lg p-6">
            <ul className="space-y-3 text-foreground-secondary">
              <li className="flex items-start gap-2">
                <span className="text-red-primary">&#10007;</span>
                <span>임의로 내용을 추가하거나 생략하지 마세요</span>
              </li>
              <li className="flex items-start gap-2">
                <span className="text-red-primary">&#10007;</span>
                <span>개인적인 의견을 통역에 섞지 마세요</span>
              </li>
              <li className="flex items-start gap-2">
                <span className="text-red-primary">&#10007;</span>
                <span>비밀 정보를 제3자에게 누설하지 마세요</span>
              </li>
              <li className="flex items-start gap-2">
                <span className="text-red-primary">&#10007;</span>
                <span>확실하지 않은 내용을 추측으로 통역하지 마세요</span>
              </li>
              <li className="flex items-start gap-2">
                <span className="text-red-primary">&#10007;</span>
                <span>감정적인 표현을 과장하거나 축소하지 마세요</span>
              </li>
            </ul>
          </div>
        </section>

        {/* CTA: 통역사 등록 */}
        <section className="bg-gradient-to-r from-red-primary to-red-dark text-white rounded-lg p-8 mb-8">
          <h2 className="text-2xl font-bold mb-3">
            {domain.name} {interpretType.name} 경험이 있으신가요?
          </h2>
          <p className="text-foreground-secondary mb-6">
            이력서를 등록하고 {domain.name} 분야 {interpretType.name} 의뢰를 받아보세요.
            경험 많은 통역사를 찾는 기업들이 기다리고 있습니다!
          </p>
          <Link
            href="/upload"
            className="inline-block bg-white text-red-primary px-6 py-3 rounded-lg font-semibold hover:bg-foreground-secondary transition"
          >
            이력서 등록하기
          </Link>
        </section>

        {/* 관련 콘텐츠 */}
        <div className="border-t border-border-default pt-8">
          <h3 className="text-lg font-semibold text-foreground mb-4">관련 가이드</h3>

          <div className="mb-6">
            <h4 className="text-sm font-medium text-foreground-muted mb-2">
              {domain.name} 분야 다른 통역 유형
            </h4>
            <div className="flex flex-wrap gap-2">
              {relatedTypes.map((t) => (
                <Link
                  key={t.slug}
                  href={`/guides/${domain.slug}/${t.slug}`}
                  className="px-3 py-1 bg-background-surface hover:bg-background-card rounded-full text-sm text-foreground-secondary transition"
                >
                  {domain.name} {t.name}
                </Link>
              ))}
            </div>
          </div>

          <div>
            <h4 className="text-sm font-medium text-foreground-muted mb-2">
              다른 분야 {interpretType.name}
            </h4>
            <div className="flex flex-wrap gap-2">
              {relatedDomains.map((d) => (
                <Link
                  key={d.slug}
                  href={`/guides/${d.slug}/${interpretType.slug}`}
                  className="px-3 py-1 bg-background-surface hover:bg-background-card rounded-full text-sm text-foreground-secondary transition"
                >
                  {d.name} {interpretType.name}
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
