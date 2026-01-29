import type { MetadataRoute } from "next";
import { domains, interpretTypes } from "@/data/pseo-dimensions";
import fs from "fs";
import path from "path";
import type { Term } from "@/types/term";

const BASE_URL = "https://phiennoi-platform.vercel.app";

// 빌드 타임에 JSON 파일에서 용어 데이터 로드
function getTermsForDomain(domainSlug: string): Term[] {
  try {
    const filePath = path.join(
      process.cwd(),
      "src/data/terms",
      `${domainSlug}.json`
    );
    const fileContents = fs.readFileSync(filePath, "utf8");
    return JSON.parse(fileContents) as Term[];
  } catch {
    return [];
  }
}

export default function sitemap(): MetadataRoute.Sitemap {
  const currentDate = new Date();
  const entries: MetadataRoute.Sitemap = [];

  // 1. 정적 페이지 (Static pages)
  entries.push(
    {
      url: BASE_URL,
      lastModified: currentDate,
      changeFrequency: "weekly",
      priority: 1.0,
    },
    {
      url: `${BASE_URL}/terms`,
      lastModified: currentDate,
      changeFrequency: "weekly",
      priority: 0.8,
    },
    {
      url: `${BASE_URL}/guides`,
      lastModified: currentDate,
      changeFrequency: "weekly",
      priority: 0.8,
    },
    {
      url: `${BASE_URL}/upload`,
      lastModified: currentDate,
      changeFrequency: "monthly",
      priority: 0.7,
    }
  );

  // 2. 도메인별 용어 목록 페이지 (/terms/[domain])
  for (const domain of domains) {
    entries.push({
      url: `${BASE_URL}/terms/${domain.slug}`,
      lastModified: currentDate,
      changeFrequency: "weekly",
      priority: 0.8,
    });

    // 3. 개별 용어 페이지 (/terms/[domain]/[term])
    const terms = getTermsForDomain(domain.slug);
    for (const term of terms) {
      entries.push({
        url: `${BASE_URL}/terms/${domain.slug}/${term.slug}`,
        lastModified: currentDate,
        changeFrequency: "monthly",
        priority: 0.6,
      });
    }
  }

  // 4. 도메인별 가이드 목록 페이지 (/guides/[domain])
  for (const domain of domains) {
    entries.push({
      url: `${BASE_URL}/guides/${domain.slug}`,
      lastModified: currentDate,
      changeFrequency: "weekly",
      priority: 0.8,
    });

    // 5. 개별 가이드 페이지 (/guides/[domain]/[type])
    for (const type of interpretTypes) {
      entries.push({
        url: `${BASE_URL}/guides/${domain.slug}/${type.slug}`,
        lastModified: currentDate,
        changeFrequency: "monthly",
        priority: 0.6,
      });
    }
  }

  return entries;
}
