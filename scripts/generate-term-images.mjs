#!/usr/bin/env node

/**
 * Recraft API를 사용해 12개 도메인의 모든 용어 이미지를 생성하는 스크립트
 *
 * 사용법: node scripts/generate-term-images.mjs
 * 환경변수: RECRAFT_API_KEY (.env.local에서 로드)
 */

import fs from "node:fs";
import path from "node:path";
import { fileURLToPath } from "node:url";
import sharp from "sharp";

// __dirname 대체 (ESM)
const __filename = fileURLToPath(import.meta.url);
const __dirname = path.dirname(__filename);
const ROOT = path.resolve(__dirname, "..");

// ── .env.local 수동 파싱 (dotenv 의존성 없이) ──────────────────────────────
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
    // 따옴표 제거
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

const API_KEY = process.env.RECRAFT_API_KEY;
if (!API_KEY) {
  console.error("❌ RECRAFT_API_KEY 환경변수가 설정되지 않았습니다.");
  process.exit(1);
}

// ── 도메인별 씬 설정 ────────────────────────────────────────────────────────
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

// ── 경로 상수 ────────────────────────────────────────────────────────────────
const TERMS_DIR = path.join(ROOT, "src", "data", "terms");
const IMAGES_DIR = path.join(ROOT, "public", "images", "terms");

// ── Recraft API 호출 ─────────────────────────────────────────────────────────
async function generateImage(prompt) {
  const res = await fetch(
    "https://external.api.recraft.ai/v1/images/generations",
    {
      method: "POST",
      headers: {
        "Content-Type": "application/json",
        Authorization: `Bearer ${API_KEY}`,
      },
      body: JSON.stringify({
        prompt,
        style: "realistic_image",
        model: "recraftv3",
        size: "1365x1024",
        response_format: "url",
      }),
    }
  );

  if (!res.ok) {
    const text = await res.text();
    throw new Error(`Recraft API ${res.status}: ${text}`);
  }

  const json = await res.json();
  return json.data[0].url;
}

// ── 이미지 다운로드 + webp 변환 ──────────────────────────────────────────────
async function downloadAndConvert(imageUrl, outputPath) {
  const res = await fetch(imageUrl);
  if (!res.ok) {
    throw new Error(`이미지 다운로드 실패: ${res.status}`);
  }

  const buffer = Buffer.from(await res.arrayBuffer());

  // sharp로 webp 변환 + 리사이즈
  await sharp(buffer)
    .resize({ width: 800, withoutEnlargement: true })
    .webp({ quality: 80 })
    .toFile(outputPath);
}

// ── 프롬프트 생성 ────────────────────────────────────────────────────────────
function buildPrompt(term, domain) {
  const scene = DOMAIN_SCENES[domain] || "professional business environment";
  const context = term.context || term.korean;

  return `Professional photo of ${context} scene, ${scene}, Korean-Vietnamese business meeting context, modern and clean setting, warm lighting, corporate style, high quality stock photo`;
}

// ── 대기 유틸리티 ────────────────────────────────────────────────────────────
function sleep(ms) {
  return new Promise((resolve) => setTimeout(resolve, ms));
}

// ── 메인 ─────────────────────────────────────────────────────────────────────
async function main() {
  console.log("=".repeat(60));
  console.log("  Recraft 이미지 생성 스크립트");
  console.log("  모델: recraftv3 | 스타일: realistic_image");
  console.log("  사이즈: 1365x1024 → 800px webp (품질 80)");
  console.log("=".repeat(60));
  console.log();

  // JSON 파일 목록
  const files = fs.readdirSync(TERMS_DIR).filter((f) => f.endsWith(".json"));
  if (files.length === 0) {
    console.error("❌ 용어 JSON 파일을 찾을 수 없습니다:", TERMS_DIR);
    process.exit(1);
  }

  console.log(`📁 도메인 ${files.length}개 발견\n`);

  let totalSuccess = 0;
  let totalFail = 0;
  let totalSkip = 0;

  for (const file of files) {
    const domain = path.basename(file, ".json");
    const filePath = path.join(TERMS_DIR, file);
    const terms = JSON.parse(fs.readFileSync(filePath, "utf-8"));

    // 도메인 이미지 디렉토리 생성
    const domainDir = path.join(IMAGES_DIR, domain);
    fs.mkdirSync(domainDir, { recursive: true });

    console.log(`\n── ${domain} (${terms.length}개 용어) ──`);

    for (let i = 0; i < terms.length; i++) {
      const term = terms[i];
      const slug = term.slug;
      const outputPath = path.join(domainDir, `${slug}.webp`);
      const label = `[${domain}] ${slug} (${i + 1}/${terms.length})`;

      // 이미 존재하면 스킵
      if (fs.existsSync(outputPath)) {
        console.log(`  ⏭️  ${label} — 이미 존재, 스킵`);
        totalSkip++;
        continue;
      }

      try {
        const prompt = buildPrompt(term, domain);

        // API 호출
        const imageUrl = await generateImage(prompt);

        // 다운로드 + 변환
        await downloadAndConvert(imageUrl, outputPath);

        console.log(`  ✅ ${label}`);
        totalSuccess++;
      } catch (err) {
        console.error(`  ❌ ${label} — ${err.message}`);
        totalFail++;
      }

      // rate limit 방지: 1초 대기
      await sleep(1000);
    }
  }

  // ── 결과 요약 ──────────────────────────────────────────────────────────────
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
