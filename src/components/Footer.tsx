import Link from "next/link";

const companyInfo = {
  name: "주식회사 에픽스테이지",
  nameEn: "Epic Stage Corp.",
  ceo: "대표 강석일",
  email: "pd@epicstage.co.kr",
  phone: "010-2957-3747",
  address: "경기도 김포시 김포한강4로420번길 30, 비321호 (한강비즈나인)",
  businessNumber: "393-86-03150",
};

const footerLinks = {
  서비스: [
    { name: "용어사전", href: "/terms" },
    { name: "통역 가이드", href: "/guides" },
    { name: "통역사 등록", href: "/upload" },
  ],
  분야별: [
    { name: "전시회 통역", href: "/guides/exhibition" },
    { name: "제조업 통역", href: "/guides/manufacturing" },
    { name: "뷰티 통역", href: "/guides/beauty" },
  ],
};

export default function Footer() {
  return (
    <footer className="border-t border-border-default bg-[#050505]">
      <div className="max-w-6xl mx-auto px-6 py-12">
        {/* 상단: 링크 섹션 */}
        <div className="grid grid-cols-2 md:grid-cols-4 gap-8 mb-10">
          {/* 브랜드 */}
          <div className="col-span-2 md:col-span-2">
            <Link href="/" className="flex items-center gap-2">
              <span className="text-xl font-bold text-foreground">Epic Note</span>
              <span className="text-xs text-red-primary font-medium">한-베 전문 통역</span>
            </Link>
            <p className="mt-3 text-sm text-foreground-muted max-w-xs">
              베트남 전문 통역 서비스. 20개 분야, 4,700+ 전문 용어, 검증된 통역사 네트워크.
            </p>
          </div>

          {/* 링크 그룹 */}
          {Object.entries(footerLinks).map(([category, links]) => (
            <div key={category}>
              <h3 className="text-xs font-semibold text-foreground-secondary uppercase tracking-wider mb-4">
                {category}
              </h3>
              <ul className="space-y-2">
                {links.map((link) => (
                  <li key={link.name}>
                    <Link
                      href={link.href}
                      className="text-sm text-foreground-muted hover:text-foreground transition-colors"
                    >
                      {link.name}
                    </Link>
                  </li>
                ))}
              </ul>
            </div>
          ))}
        </div>

        {/* 구분선 + CTA */}
        <div className="border-t border-border-default pt-8 mb-8">
          <div className="flex flex-col md:flex-row justify-between items-start md:items-center gap-4">
            <div>
              <p className="text-foreground-secondary font-medium">통역 준비가 필요하신가요?</p>
              <p className="text-sm text-foreground-muted">전문 분야별 용어집과 통역 가이드를 확인하세요.</p>
            </div>
            <div className="flex gap-4">
              <Link
                href="/terms"
                className="px-4 py-2 text-sm border border-red-primary text-red-primary rounded-lg hover:bg-red-primary hover:text-white transition"
              >
                용어사전
              </Link>
              <Link
                href="/guides"
                className="px-4 py-2 text-sm bg-red-primary text-white rounded-lg hover:bg-red-hover transition"
              >
                가이드 보기
              </Link>
            </div>
          </div>
        </div>

        {/* 회사 정보 */}
        <div className="border-t border-border-default pt-6">
          <div className="flex flex-col md:flex-row justify-between gap-4">
            <div className="text-xs text-foreground-muted space-y-1">
              <p>
                <span className="font-medium">{companyInfo.name}</span> ({companyInfo.nameEn}) | {companyInfo.ceo}
              </p>
              <p>사업자등록번호: {companyInfo.businessNumber}</p>
              <p>{companyInfo.address}</p>
              <p>
                이메일:{" "}
                <a
                  href={`mailto:${companyInfo.email}`}
                  className="hover:text-foreground transition"
                >
                  {companyInfo.email}
                </a>
                {" | "}
                전화:{" "}
                <a
                  href={`tel:${companyInfo.phone.replace(/-/g, "")}`}
                  className="hover:text-foreground transition"
                >
                  {companyInfo.phone}
                </a>
              </p>
            </div>
            <div className="flex items-center gap-4 text-xs text-foreground-muted">
              <a
                href="https://www.epicstage.co.kr"
                target="_blank"
                rel="noopener noreferrer"
                className="hover:text-foreground transition"
              >
                epicstage.co.kr
              </a>
              <a
                href="https://hub.epicstage.co.kr"
                target="_blank"
                rel="noopener noreferrer"
                className="hover:text-foreground transition"
              >
                EpicStage Hub
              </a>
            </div>
          </div>
          <p className="mt-6 text-xs text-foreground-muted text-center">
            © {new Date().getFullYear()} Epic Note by EpicStage. All rights reserved.
          </p>
        </div>
      </div>
    </footer>
  );
}
