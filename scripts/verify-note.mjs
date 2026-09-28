import { readFile } from 'node:fs/promises';
import path from 'node:path';

const file = process.argv[2];
if (!file) {
  console.error("Usage: node scripts/verify-note.mjs <filepath>");
  process.exit(1);
}

const markdown = await readFile(file, 'utf8');
const errors = [];

// 1. Frontmatter
const fmMatch = markdown.match(/^---\r?\n([\s\S]*?)\r?\n---/);
if (!fmMatch) {
  errors.push("Frontmatter missing");
} else {
  const fm = fmMatch[1];
  if (!/model:\s*"Gemini 3.8 Flash"/i.test(fm)) errors.push("model should be 'Gemini 3.8 Flash'");
  if (!/author:\s*"Antigravity"/i.test(fm)) errors.push("author should be 'Antigravity'");
  if (!/date:\s*"\d{4}-\d{2}-\d{2}T\d{2}:\d{2}:\d{2}\+09:00"/.test(fm)) errors.push("date should be RFC 3339 KST format");
}

// 2. 30초 인출
const recallMatch = markdown.match(/## 30초 인출\s*([\s\S]*?)(?=<details>|---)/);
if (!recallMatch) {
  errors.push("30초 인출 missing");
} else {
  const lines = recallMatch[1].trim().split(/\r?\n/).map(l => l.trim()).filter(l => l.startsWith('-'));
  if (lines.length !== 3) {
    errors.push(`30초 인출 should have 3 lines, got ${lines.length}`);
  } else {
    if (!/^- (?:\*\*)?본질(?:\*\*)?:/.test(lines[0])) errors.push("30초 인출 1st line must be 본질");
    if (!/^- (?:\*\*)?메커니즘(?:\*\*)?:/.test(lines[1])) errors.push("30초 인출 2nd line must be 메커니즘");
    if (!/^- (?:\*\*)?통찰(?:\*\*)?:/.test(lines[2])) errors.push("30초 인출 3rd line must be 통찰");
    if (/한계\s*:|→|방안\s*:/.test(lines[2])) errors.push("30초 통찰 should be a single sentence without '한계: / 방안: / →'");
  }
}

// 3. 1교시 check
if (/## 1교시/m.test(markdown)) errors.push("1교시 section must not exist");

// 4. 25점 답안
const answerStart = markdown.indexOf("## 2~4교시 25점 답안");
if (answerStart === -1) {
  errors.push("## 2~4교시 25점 답안 missing");
} else {
  const answer = markdown.slice(answerStart);
  const headings = [...answer.matchAll(/^## ([Ⅰ-Ⅻ]+)\.([^\n]*)$/gmu)];
  const numbers = headings.map(h => h[1]);
  if (JSON.stringify(numbers) !== JSON.stringify(['Ⅰ', 'Ⅱ', 'Ⅲ', 'Ⅳ', 'Ⅴ', 'Ⅵ'])) {
    errors.push(`Sections must be Ⅰ~Ⅵ, found: ${numbers.join(', ')}`);
  }

  const sections = headings.map((h, i) => ({
    number: h[1],
    title: h[2].trim(),
    body: answer.slice(h.index + h[0].length, i + 1 < headings.length ? headings[i + 1].index : answer.indexOf("## 출제 이력"))
  }));

  const byNum = Object.fromEntries(sections.map(s => [s.number, s]));

  // Ⅰ. 개요
  if (byNum['Ⅰ']) {
    if (!/개요/.test(byNum['Ⅰ'].title)) errors.push("Ⅰ title must contain 개요");
    if (!/\|\s*구분\s*\|\s*핵심\s*\|/.test(byNum['Ⅰ'].body)) errors.push("Ⅰ must have 구분 | 핵심 table");
    if (!/\|\s*정의\s*\|/.test(byNum['Ⅰ'].body)) errors.push("Ⅰ must have 정의 row");
    if (!/\|\s*목적\s*\|/.test(byNum['Ⅰ'].body)) errors.push("Ⅰ must have 목적 row");
    if (/```text/.test(byNum['Ⅰ'].body)) errors.push("Ⅰ must not have text diagram");
  }

  // Ⅱ. 특징
  if (byNum['Ⅱ'] && !/특징|특성/.test(byNum['Ⅱ'].title)) {
    errors.push("Ⅱ title must contain 특징 or 특성");
  }

  // Ⅲ. 체계
  if (byNum['Ⅲ'] && !/```text/.test(byNum['Ⅲ'].body)) {
    errors.push("Ⅲ must have text diagram");
  }

  // Ⅳ. 종류/비교
  if (byNum['Ⅳ'] && !(/```text/.test(byNum['Ⅳ'].body) || /\|[^\n]+\|\r?\n\|/.test(byNum['Ⅳ'].body))) {
    errors.push("Ⅳ must have table or text diagram");
  }

  // Ⅴ. 한계와 방안
  if (byNum['Ⅴ']) {
    if (!/한계.*방안/.test(byNum['Ⅴ'].title)) errors.push("Ⅴ title must be 한계와 방안");
    if (!/\|\s*한계\s*\|\s*방안\s*\|/.test(byNum['Ⅴ'].body)) errors.push("Ⅴ must have 한계 | 방안 table");
    const rows = byNum['Ⅴ'].body.split(/\r?\n/).filter(l => l.startsWith('|')).slice(2);
    if (rows.length < 2) errors.push("Ⅴ table must have at least 2 rows");
    for (const row of rows) {
      if (row.replace(/\\\|/g, '').split('|').length !== 4) {
        errors.push(`Ⅴ table row must have exactly 2 columns: ${row}`);
      }
    }
  }

  // Ⅵ. 제언
  if (byNum['Ⅵ']) {
    if (!/제언/.test(byNum['Ⅵ'].title)) errors.push("Ⅵ title must be 제언");
    const diagrams = (byNum['Ⅵ'].body.match(/```text\s*$/gm) || []).length;
    if (diagrams < 1 || diagrams > 3) errors.push(`Ⅵ must have 1~3 text diagrams, found ${diagrams}`);
    if (!/\|[^\n]+\|\r?\n\|/.test(byNum['Ⅵ'].body)) errors.push("Ⅵ must have comparison table");
  }
}

// 5. Bold closing space check
const withoutCode = markdown.replace(/```[\s\S]*?```/g, '');
const boldLines = withoutCode.split(/\r?\n/);
boldLines.forEach((line, idx) => {
  const parts = line.split('**');
  for (let i = 1; i + 1 < parts.length; i += 2) {
    if (/^\s|\s$/.test(parts[i])) errors.push(`Line ${idx+1}: bold inner whitespace: "${parts[i]}"`);
    if (!/^(?:$|[\s|.,():;?><!~-])/.test(parts[i+1])) {
      // Allow punctuation like ) or , if standard, but itStrategyVisual test requires space or specific:
      // Note: itStrategyVisual says: !/^(?:$|[\s|])/u.test(parts[index + 1])
      if (!/^(?:$|[\s|])/.test(parts[i+1])) {
        errors.push(`Line ${idx+1}: closing ** not followed by space or pipe: "**${parts[i]}**${parts[i+1].slice(0, 5)}"`);
      }
    }
  }
});

// 6. Noun phrase nominal ending check
const authPart1 = markdown.slice(markdown.indexOf('## 30초 인출'), markdown.indexOf('## 2~4교시 예상문제'));
const authPart2 = markdown.slice(markdown.indexOf('## 2~4교시 25점 답안'), markdown.indexOf('## 출제 이력'));
for (const part of [authPart1, authPart2]) {
  for (const line of part.split(/\r?\n/)) {
    if (/^\s*(?:>|- \[|https?:\/\/|```|\|)/.test(line)) continue;
    const trimmed = line.trim();
    if (!trimmed) continue;
    if (/다\.?(?=\s*\||\s*$)/.test(trimmed)) errors.push(`Ending in 다: "${trimmed}"`);
    if (/(?:해야|하도록|되어야|수행|확인|설명|판단|적용|관리|기록|검토|정의|분석|제공|지원|처리|반영|설정|결정|활용|개선|보완|보장|확보|유지|운영|평가|파악|도출|구분)\s*(?:함|됨)(?:\.|\s*\|)?\s*$/.test(trimmed)) {
      errors.push(`Mechanical 함/됨 ending: "${trimmed}"`);
    }
  }
}

// 7. No URLs in 출제 이력
const historyPart = markdown.slice(markdown.indexOf('## 출제 이력'));
if (/https?:\/\//.test(historyPart)) {
  errors.push("출제 이력 must not contain URLs");
}

if (errors.length > 0) {
  console.log(`❌ ${path.basename(file)}: ${errors.length} errors`);
  errors.forEach(e => console.log(`   - ${e}`));
  process.exit(1);
} else {
  console.log(`✅ ${path.basename(file)}: PASSED`);
}
