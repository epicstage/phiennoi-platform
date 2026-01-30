#!/usr/bin/env node

/**
 * Ideogram API를 사용해 남은 용어 이미지를 생성하는 스크립트
 * Recraft 크레딧 소진 후 이어서 사용
 *
 * 사용법: node scripts/generate-term-images-ideogram.mjs
 */

import fs from "node:fs";
import path from "node:path";
import { fileURLToPath } from "node:url";
import sharp from "sharp";

const __filename = fileURLToPath(import.meta.url);
const __dirname = path.dirname(__filename);
const ROOT = path.resolve(__dirname, "..");

// ── .env.local 파싱 ──
function loadEnv() {
  const envPath = path.join(ROOT, ".env.local");
  if (!fs.existsSync(envPath)) {
    console.error("❌ .env.local 파일이 없습니다:", envPath);
    process.exit(1);
  }
  const content = fs.readFileSync(envPath, "utf-8");
  for (const line of content.split("\n")) {
    const trimmed = line.trim();
    if (!trimmed || trimmed.startsWith("#")) continue;
    const eqIdx = trimmed.indexOf("=");
    if (eqIdx === -1) continue;
    const key = trimmed.slice(0, eqIdx).trim();
    let value = trimmed.slice(eqIdx + 1).trim();
    if (
      (value.startsWith('"') && value.endsWith('"')) ||
      (value.startsWith("'") && value.endsWith("'"))
    ) {
      value = value.slice(1, -1);
    }
    if (!process.env[key]) {
      process.env[key] = value;
    }
  }
}

loadEnv();

const API_KEY = process.env.IDEOGRAM_API_KEY;
if (!API_KEY) {
  console.error("❌ IDEOGRAM_API_KEY 환경변수가 설정되지 않았습니다.");
  process.exit(1);
}

// ── 도메인별 씬 설정 ──
const DOMAIN_SCENES = {
  agriculture: "farm field, agricultural machinery, crops",
  beauty: "beauty salon, cosmetics, skincare products",
  construction: "construction site, building, heavy machinery",
  exhibition: "exhibition hall, trade show booth, business event",
  finance: "modern office, financial charts, banking",
  food: "food factory, restaurant kitchen, food products",
  it: "tech office, computer screens, software development",
  legal: "law office, courtroom, legal documents",
  logistics: "warehouse, shipping containers, cargo",
  manufacturing: "factory floor, assembly line, industrial equipment",
  medical: "hospital, medical equipment, clinic",
  realEstate: "modern building, apartment complex, office space",
};

const TERMS_DIR = path.join(ROOT, "src", "data", "terms");
const IMAGES_DIR = path.join(ROOT, "public", "images", "terms");

// ── Ideogram API 호출 ──
async function generateImage(prompt) {
  const res = await fetch("https://api.ideogram.ai/v1/ideogram-v3/generate", {
    method: "POST",
    headers: {
      "Content-Type": "application/json",
      "Api-Key": API_KEY,
    },
    body: JSON.stringify({
      prompt,
      rendering_speed: "TURBO",
      aspect_ratio: "3x2",
      style_type: "REALISTIC",
    }),
  });

  if (!res.ok) {
    const text = await res.text();
    throw new Error(`Ideogram API ${res.status}: ${text}`);
  }

  const json = await res.json();
  return json.data[0].url;
}

// ── 이미지 다운로드 + webp 변환 ──
async function downloadAndConvert(imageUrl, outputPath) {
  const res = await fetch(imageUrl);
  if (!res.ok) {
    throw new Error(`이미지 다운로드 실패: ${res.status}`);
  }

  const buffer = Buffer.from(await res.arrayBuffer());

  await sharp(buffer)
    .resize({ width: 800, withoutEnlargement: true })
    .webp({ quality: 80 })
    .toFile(outputPath);
}

// ── 프롬프트 생성 ──
function buildPrompt(term, domain) {
  const scene = DOMAIN_SCENES[domain] || "professional business environment";
  const context = term.context || term.korean;

  return `Professional photo of ${context} scene, ${scene}, Korean-Vietnamese business meeting context, modern and clean setting, warm lighting, corporate style, high quality stock photo`;
}

function sleep(ms) {
  return new Promise((resolve) => setTimeout(resolve, ms));
}

// ── 메인 ──
async function main() {
  console.log("=".repeat(60));
  console.log("  Ideogram 이미지 생성 스크립트 (남은 용어)");
  console.log("  모델: ideogram-v3 TURBO | 스타일: REALISTIC");
  console.log("  비율: 3:2 → 800px webp (품질 80)");
  console.log("=".repeat(60));
  console.log();

  const files = fs.readdirSync(TERMS_DIR).filter((f) => f.endsWith(".json"));
  console.log(`📁 도메인 ${files.length}개 발견\n`);

  let totalSuccess = 0;
  let totalFail = 0;
  let totalSkip = 0;

  for (const file of files) {
    const domain = path.basename(file, ".json");
    const filePath = path.join(TERMS_DIR, file);
    const terms = JSON.parse(fs.readFileSync(filePath, "utf-8"));

    const domainDir = path.join(IMAGES_DIR, domain);
    fs.mkdirSync(domainDir, { recursive: true });

    // 이미 모두 완료된 도메인은 스킵
    const missing = terms.filter(
      (t) => !fs.existsSync(path.join(domainDir, `${t.slug}.webp`))
    );
    if (missing.length === 0) {
      console.log(`── ${domain} (${terms.length}개) ── 전부 완료, 스킵`);
      totalSkip += terms.length;
      continue;
    }

    console.log(
      `\n── ${domain} (남은 ${missing.length}/${terms.length}개) ──`
    );

    for (let i = 0; i < terms.length; i++) {
      const term = terms[i];
      const slug = term.slug;
      const outputPath = path.join(domainDir, `${slug}.webp`);
      const label = `[${domain}] ${slug} (${i + 1}/${terms.length})`;

      if (fs.existsSync(outputPath)) {
        totalSkip++;
        continue;
      }

      try {
        const prompt = buildPrompt(term, domain);
        const imageUrl = await generateImage(prompt);
        await downloadAndConvert(imageUrl, outputPath);

        console.log(`  ✅ ${label}`);
        totalSuccess++;
      } catch (err) {
        console.error(`  ❌ ${label} — ${err.message}`);
        totalFail++;

        // 크레딧 소진 감지 시 조기 종료
        if (
          err.message.includes("402") ||
          err.message.includes("credit") ||
          err.message.includes("insufficient")
        ) {
          console.log("\n💰 크레딧 소진 — 스크립트 종료");
          break;
        }
      }

      // rate limit 방지: 1.5초 대기
      await sleep(1500);
    }
  }

  console.log("\n" + "=".repeat(60));
  console.log("  결과 요약");
  console.log("=".repeat(60));
  console.log(`  ✅ 성공: ${totalSuccess}`);
  console.log(`  ⏭️  스킵: ${totalSkip}`);
  console.log(`  ❌ 실패: ${totalFail}`);
  console.log(`  📊 전체: ${totalSuccess + totalSkip + totalFail}`);
  console.log("=".repeat(60));
}

main().catch((err) => {
  console.error("스크립트 에러:", err);
  process.exit(1);
});
