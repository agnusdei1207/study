import assert from 'node:assert/strict';
import { readdir, readFile } from 'node:fs/promises';
import path from 'node:path';
import test from 'node:test';

const notesDir = 'src/content/docs/notes/itpe/01-it-strategy';

async function targetNotes() {
  const names = await readdir(notesDir);
  return names.filter((name) => /^\d{3}_.+\.md$/u.test(name)).sort().map((name) => path.join(notesDir, name));
}

function sectionAfter(markdown, headingPattern) {
  const match = markdown.match(headingPattern);
  if (!match || match.index === undefined) return null;
  const rest = markdown.slice(match.index + match[0].length);
  const nextHeading = rest.search(/^##\s+/mu);
  return nextHeading === -1 ? rest : rest.slice(0, nextHeading);
}

function mermaidBlocks(markdown) {
  return [...markdown.matchAll(/```mermaid\s*\r?\n([\s\S]*?)```/gu)].map((match) => match[1].replace(/\r\n/gu, '\n').trim());
}

test('All IT strategy notes use Mermaid instead of legacy visual markup', async () => {
  const files = await targetNotes();
  assert.equal(files.length, 81, '현재 카탈로그의 IT 전략 과목에는 81개 노트가 있어야 합니다.');
  for (const file of files) {
    const note = await readFile(file, 'utf8');
    assert.match(note, /```mermaid/u, `${file}: Mermaid 시각화가 필요합니다.`);
    assert.doesNotMatch(note, /<svg\b/iu, `${file}: 인라인 SVG를 제거해야 합니다.`);
    assert.doesNotMatch(note, /class="itpe-(?:flow|pipeline|trace|svg|edm|diagram)/iu, `${file}: 레거시 시각화 HTML 클래스를 제거해야 합니다.`);
    assert.doesNotMatch(note, /[┌┐└┘├┤┬┴┼─│]/u, `${file}: ASCII 박스 다이어그램을 제거해야 합니다.`);
  }
});

test('30초 인출은 본질·메커니즘을 중심으로 하고 추가 단서는 선택한다', async () => {
  for (const file of await targetNotes()) {
    const note = await readFile(file, 'utf8');
    const recall = sectionAfter(note, /^## 30초 인출\s*$/mu);
    assert.notEqual(recall, null, `${file}: 30초 인출 절이 필요합니다.`);
    assert.doesNotMatch(recall, /```mermaid/u, `${file}: 30초 인출에는 Mermaid를 넣지 않습니다.`);
    const summary = recall.split(/<details\b/iu, 1)[0];
    const lines = summary.split(/\r?\n/u).map((line) => line.trim()).filter(Boolean);
    assert.ok(lines.length >= 2, `${file}: 30초 인출에는 본질과 메커니즘이 필요합니다.`);
    assert.match(lines[0], /^- (?:\*\*)?본질(?:\*\*)?:/u, `${file}: 첫 줄은 본질이어야 합니다.`);
    assert.match(lines[1], /^- (?:\*\*)?메커니즘(?:\*\*)?:/u, `${file}: 둘째 줄은 메커니즘이어야 합니다.`);
  }
});

test('10점 답안의 Mermaid는 본문에서 검증한 그림을 그대로 재사용한다', async () => {
  for (const file of await targetNotes()) {
    const note = await readFile(file, 'utf8');
    const short = sectionAfter(note, /^## 1교시 10점 답안\s*$/mu) ?? '';
    const longStart = note.indexOf('## 2~4교시 25점 답안');
    const longEnd = note.indexOf('## 출제 이력과 검증 출처', longStart);
    assert.ok(longStart >= 0 && longEnd > longStart, `${file}: 25점 답안 절이 필요합니다.`);
    const bodyDiagrams = new Set(mermaidBlocks(note.slice(longStart, longEnd)));
    for (const diagram of mermaidBlocks(short)) {
      assert.ok(bodyDiagrams.has(diagram), `${file}: 10점 답안 Mermaid는 25점 답안 그림을 그대로 재사용해야 합니다.`);
    }
  }
});

test('IT strategy notes place each question above its answer, with 10 points first', async () => {
  for (const file of await targetNotes()) {
    const note = await readFile(file, 'utf8');
    assert.match(note, /---\s+## 1교시 예상문제 \(10점\)\s+>[^\n]+\s+---\s+## 1교시 10점 답안/u, file);
    assert.match(note, /---\s+## 2~4교시 예상문제 \(25점\)\s+(?:>[^\n]+\s*)+---\s+## 2~4교시 25점 답안/u, file);
    assert.ok(note.indexOf('## 1교시 10점 답안') < note.indexOf('## 2~4교시 25점 답안'), file);
  }
});
