import Link from "next/link";

export default function Header() {
  return (
    <header className="sticky top-0 z-50 border-b border-border-default bg-background/95 backdrop-blur">
      <div className="max-w-7xl mx-auto px-6 h-16 flex items-center justify-between">
        <Link href="/" className="flex items-center gap-3">
          <div className="w-8 h-8 bg-red-primary rounded" />
          <span className="text-lg font-bold tracking-wide text-foreground">한베통역</span>
        </Link>
        <nav className="hidden md:flex items-center gap-8">
          <Link href="/terms" className="text-sm text-foreground-secondary hover:text-foreground transition">
            용어사전
          </Link>
          <Link href="/guides" className="text-sm text-foreground-secondary hover:text-foreground transition">
            통역 가이드
          </Link>
          <Link
            href="/upload"
            className="px-5 py-2 bg-red-primary text-white text-sm font-semibold rounded hover:bg-red-hover transition"
          >
            이력서 등록
          </Link>
        </nav>
      </div>
    </header>
  );
}
