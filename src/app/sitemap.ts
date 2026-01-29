import type { MetadataRoute } from "next";
import { domains, interpretTypes } from "@/data/pseo-dimensions";
import type { Term } from "@/types/term";

const BASE_URL = "https://phiennoi-platform.vercel.app";

export default function sitemap(): MetadataRoute.Sitemap {
  const entries: MetadataRoute.Sitemap = [];

  // Static pages
  entries.push(
    { url: BASE_URL, lastModified: new Date(), changeFrequency: "weekly", priority: 1.0 },
    { url: `${BASE_URL}/upload`, lastModified: new Date(), changeFrequency: "monthly", priority: 0.9 },
    { url: `${BASE_URL}/terms`, lastModified: new Date(), changeFrequency: "weekly", priority: 0.8 },
    { url: `${BASE_URL}/guides`, lastModified: new Date(), changeFrequency: "weekly", priority: 0.8 },
  );

  // Domain term list pages
  for (const domain of domains) {
    entries.push({
      url: `${BASE_URL}/terms/${domain.slug}`,
      lastModified: new Date(),
      changeFrequency: "weekly",
      priority: 0.7,
    });

    // Term detail pages
    try {
      // eslint-disable-next-line @typescript-eslint/no-require-imports
      const terms = require(`@/data/terms/${domain.slug}.json`) as Term[];
      for (const term of terms) {
        entries.push({
          url: `${BASE_URL}/terms/${domain.slug}/${term.slug}`,
          lastModified: new Date(),
          changeFrequency: "monthly",
          priority: 0.6,
        });
      }
    } catch {
      // skip domains without term data
    }
  }

  // Guide pages
  for (const domain of domains) {
    entries.push({
      url: `${BASE_URL}/guides/${domain.slug}`,
      lastModified: new Date(),
      changeFrequency: "weekly",
      priority: 0.7,
    });

    for (const type of interpretTypes) {
      entries.push({
        url: `${BASE_URL}/guides/${domain.slug}/${type.slug}`,
        lastModified: new Date(),
        changeFrequency: "monthly",
        priority: 0.6,
      });
    }
  }

  return entries;
}
