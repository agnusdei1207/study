import assert from 'node:assert/strict';
import { readFile } from 'node:fs/promises';
import test from 'node:test';

const notePath = 'src/content/docs/notes/itpe/01-it-strategy/002_iso_iec_38500.md';
const cssPath = 'src/styles/custom.css';

const excerptHeading = '## 1교시 10점 답안 발췌';

test('ISO 38500 shows EDM as a feedback cycle and explains the framework', async () => {
  const note = await readFile(notePath, 'utf8');

  assert.match(note, /```mermaid\s+flowchart\s+(TD|TB)[\s\S]*?M[^\n]*-->(?:\|[^|]+\|)?\s*E/u, '큰 그림에 EDM 폐루프 Mermaid가 필요합니다.');
  assert.match(note, /Feedback Loop/u);

  for (const element of ['Direction', 'Capability', 'Policy', 'Delegation', 'Performance', 'Accountability']) {
    assert.match(note, new RegExp(`\\| \\*\\*${element}`, 'u'), `${element}의 역할 설명 표가 필요합니다.`);
  }
});

test('each answer section carries its own relationship diagram', async () => {
  const note = await readFile(notePath, 'utf8');
  const body = note.slice(note.indexOf('## Ⅰ.'), note.indexOf(excerptHeading));

  for (const section of ['## Ⅱ.', '## Ⅲ.']) {
    const start = body.indexOf(section);
    const rest = body.slice(start + section.length);
    const end = rest.indexOf('\n## ');
    const block = end === -1 ? rest : rest.slice(0, end);
    assert.match(block, /```mermaid/u, `${section} 절에는 Mermaid 관계 그림이 필요합니다.`);
  }
});

test('the 10 point excerpt reuses a body diagram instead of a meta table', async () => {
  const note = await readFile(notePath, 'utf8');
  const excerpt = note.slice(note.indexOf(excerptHeading));

  const body = note.slice(note.indexOf('## Ⅰ.'), note.indexOf(excerptHeading));
  const mermaidBlocks = (text) => [...text.matchAll(/```mermaid\s*\n([\s\S]*?)```/gu)]
    .map(([, source]) => source.trim().replaceAll(/\s+/gu, ' '));
  const bodyDiagrams = new Set(mermaidBlocks(body));
  const excerptDiagrams = mermaidBlocks(excerpt);

  assert.ok(excerptDiagrams.length > 0, '10점 발췌에는 Mermaid 그림이 필요합니다.');
  assert.ok(
    excerptDiagrams.some((diagram) => bodyDiagrams.has(diagram)),
    '10점 발췌는 본문 Mermaid 그림을 그대로 재사용해야 합니다.'
  );
  assert.doesNotMatch(excerpt, /\|\s*(구분|항목)\s*\|/u, '본문 그림을 메타 요약 표로 대체하지 않습니다.');
});

test('legacy ITPE visualization CSS is removed after the Mermaid transition', async () => {
  const css = await readFile(cssPath, 'utf8');

  for (const legacyClass of ['itpe-flow-', 'itpe-pipeline', 'itpe-trace-band', 'itpe-svg-', 'itpe-edm-']) {
    assert.doesNotMatch(css, new RegExp(`\\.${legacyClass}`, 'u'), `${legacyClass} 시각화 CSS는 제거해야 합니다.`);
  }
});

test('desktop Markdown tables use the full content width', async () => {
  const css = await readFile(cssPath, 'utf8');
  assert.match(
    css,
    /\.sl-markdown-content table\s*\{[^}]*display:\s*table;[^}]*width:\s*100%;/su
  );
});
