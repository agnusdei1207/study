import assert from 'node:assert/strict';
import { readFile } from 'node:fs/promises';
import test from 'node:test';

const notePath = 'src/content/docs/notes/itpe/01-it-strategy/002_iso_iec_38500.md';
const cssPath = 'src/styles/custom.css';

function answerSection(note, number, next) {
  const body = note.slice(note.indexOf('## 2~4교시 25점 답안'), note.indexOf('## 출제 이력과 검증 출처'));
  const start = body.indexOf(`## ${number}.`);
  const end = next ? body.indexOf(`\n## ${next}.`, start) : body.length;
  return body.slice(start, end);
}

test('ISO 38500 shows the EDM cycle as a directed text diagram in the framework section', async () => {
  const note = await readFile(notePath, 'utf8');
  const core = answerSection(note, 'Ⅲ', 'Ⅳ');
  assert.match(core, /```text[\s\S]*?평가[\s\S]*?(?:지시|방향 제시)[\s\S]*?(?:감독|모니터링)[\s\S]*?```/u, 'Ⅲ에 EDM 순환을 방향이 있는 텍스트 도해로 보여야 합니다.');
  assert.match(core, /↓|→/u, 'EDM 순환은 방향이 있는 관계입니다.');
});

test('ISO 38500 separates edition principles and framework elements in tables', async () => {
  const note = await readFile(notePath, 'utf8');
  const extension = answerSection(note, 'Ⅳ', 'Ⅴ');
  for (const element of ['Direction', 'Capability', 'Policy', 'Delegation', 'Performance', 'Accountability']) {
    assert.ok(extension.includes(`| **${element}**`) || extension.includes(`| ${element}`), `${element}의 역할 설명 표가 필요합니다.`);
  }
  assert.match(extension, /2015/u, '구판 원칙은 판본을 명시해야 합니다.');
});

test('legacy ITPE visualization CSS stays removed', async () => {
  const css = await readFile(cssPath, 'utf8');
  for (const legacyClass of ['itpe-flow-', 'itpe-pipeline', 'itpe-trace-band', 'itpe-svg-', 'itpe-edm-']) {
    assert.doesNotMatch(css, new RegExp(`\.${legacyClass}`, 'u'), `${legacyClass} 시각화 CSS는 제거해야 합니다.`);
  }
});

test('desktop Markdown tables use the full content width', async () => {
  const css = await readFile(cssPath, 'utf8');
  assert.match(css, /\.sl-markdown-content table\s*\{[^}]*display:\s*table;[^}]*width:\s*100%;/su);
});
