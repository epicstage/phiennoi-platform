import Link from "next/link";

export default function Footer() {
  return (
    <footer className="border-t border-border-default bg-[#050505] py-8 px-6 text-center">
      <p className="text-foreground-secondary mb-4">통역 준비가 필요하신가요?</p>
      <div className="flex justify-center gap-6">
        <Link href="/terms" className="text-red-primary hover:underline font-medium">
          용어사전 보기
        </Link>
        <Link href="/guides" className="text-red-primary hover:underline font-medium">
          가이드 보기
        </Link>
      </div>
      <p className="text-foreground-muted text-xs mt-6">
        © 2026 Epic Note. All rights reserved.
      </p>
    </footer>
  );
}
