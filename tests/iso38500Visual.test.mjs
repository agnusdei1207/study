import assert from 'node:assert/strict';
import { readFile } from 'node:fs/promises';
import test from 'node:test';

const notePath = 'src/content/docs/notes/itpe/01-it-strategy/002_iso_iec_38500.md';
const cssPath = 'src/styles/custom.css';

const shortHeading = '## 1교시 10점 답안';
const longHeading = '## 2~4교시 25점 답안';

test('ISO 38500 shows EDM as a feedback cycle and explains the framework', async () => {
  const note = await readFile(notePath, 'utf8');

  assert.match(note, /```mermaid\s+flowchart\s+(TD|TB)[\s\S]*?M[^\n]*-->(?:\|[^|]+\|)?\s*E/u, '큰 그림에 EDM 폐루프 Mermaid가 필요합니다.');
  assert.match(note, /Feedback Loop/u);

  for (const element of ['Direction', 'Capability', 'Policy', 'Delegation', 'Performance', 'Accountability']) {
    assert.match(note, new RegExp(`\\| \\*\\*${element}`, 'u'), `${element}의 역할 설명 표가 필요합니다.`);
  }
});

test('EDM cycle and dated-principles reference stay focused', async () => {
  const note = await readFile(notePath, 'utf8');
  const body = note.slice(note.indexOf(longHeading), note.indexOf('## 출제 이력과 검증 출처'));

  const modelStart = body.indexOf('## Ⅱ.');
  const modelEnd = body.indexOf('\n## Ⅲ.', modelStart);
  assert.match(body.slice(modelStart, modelEnd), /```mermaid/u, 'EDM 순환은 관계 그림으로 표현합니다.');
  const principlesStart = body.indexOf('## Ⅲ.');
  const principlesEnd = body.indexOf('\n## Ⅳ.', principlesStart);
  assert.match(body.slice(principlesStart, principlesEnd), /\| \*\*책임\*\*/u, '구판 원칙은 판본을 명시한 표로 간결하게 설명합니다.');
  assert.doesNotMatch(body.slice(principlesStart, principlesEnd), /```mermaid/u, '여섯 항목의 나열은 별도 도해로 중복하지 않습니다.');
});

test('the 10 point answer reuses a body diagram instead of a meta table', async () => {
  const note = await readFile(notePath, 'utf8');
  const excerpt = note.slice(note.indexOf(shortHeading), note.indexOf('## 2~4교시 예상문제'));

  const body = note.slice(note.indexOf(longHeading), note.indexOf('## 출제 이력과 검증 출처'));
  const mermaidBlocks = (text) => [...text.matchAll(/```mermaid\s*\n([\s\S]*?)```/gu)]
    .map(([, source]) => source.trim().replaceAll(/\s+/gu, ' '));
  const bodyDiagrams = new Set(mermaidBlocks(body));
  const excerptDiagrams = mermaidBlocks(excerpt);

  assert.ok(excerptDiagrams.length > 0, '10점 발췌에는 Mermaid 그림이 필요합니다.');
  assert.ok(
    excerptDiagrams.some((diagram) => bodyDiagrams.has(diagram)),
    '10점 발췌는 본문 Mermaid 그림을 그대로 재사용해야 합니다.'
  );
  const afterOverview = excerpt.slice(excerpt.indexOf('### Ⅱ.'));
  assert.doesNotMatch(afterOverview, /\|\s*(구분|항목)\s*\|/u, '개요 뒤의 본문 그림을 메타 요약 표로 대체하지 않습니다.');
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
