import assert from 'node:assert/strict';
import { readFile } from 'node:fs/promises';
import test from 'node:test';

const notePath = 'src/content/docs/notes/itpe/01-it-strategy/002_iso_iec_38500.md';
const cssPath = 'src/styles/custom.css';

test('ISO 38500 shows EDM as a feedback cycle and explains the framework', async () => {
  const note = await readFile(notePath, 'utf8');
  const cycles = note.match(/class="itpe-edm-cycle"/gu) ?? [];

  assert.ok(cycles.length >= 2, '본문과 1교시 발췌에 EDM 순환 그림이 각각 필요합니다.');
  assert.match(note, /Feedback Loop/u);
  assert.doesNotMatch(note, /^\s*- 프레임워크: Direction/u);

  for (const element of ['Direction', 'Capability', 'Policy', 'Delegation', 'Performance', 'Accountability']) {
    assert.match(note, new RegExp(`\\| \\*\\*${element}`, 'u'), `${element}의 역할 설명 표가 필요합니다.`);
  }
});

test('desktop Markdown tables use the full content width', async () => {
  const css = await readFile(cssPath, 'utf8');
  assert.match(
    css,
    /\.sl-markdown-content table\s*\{[^}]*display:\s*table;[^}]*width:\s*100%;/su
  );
});
