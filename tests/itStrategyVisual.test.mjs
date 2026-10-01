import assert from 'node:assert/strict';
import { readdir, readFile } from 'node:fs/promises';
import path from 'node:path';
import test from 'node:test';

const notesDir = 'src/content/docs/notes/itpe/01-it-strategy';
const ONLY_IDS = process.env.ITPE_IDS?.split(",").map((value) => value.trim()).filter(Boolean);
const inScope = (name) => !ONLY_IDS || ONLY_IDS.includes(name.slice(0, 3));

async function targetNotes() {
  const names = await readdir(notesDir);
  return names.filter((name) => /^\d{3}_.+\.md$/u.test(name)).sort().map((name) => path.join(notesDir, name));
}

async function rewrittenNotes() {
  return (await targetNotes()).filter((file) => inScope(path.basename(file)));
}

function romanSections(markdown) {
  const headings = [...markdown.matchAll(/^## ([Ⅰ-Ⅻ]+)\.([^\n]*)$/gmu)];
  return headings.map((heading, index) => ({
    number: heading[1],
    title: heading[2].trim(),
    body: markdown.slice(heading.index + heading[0].length, index + 1 < headings.length ? headings[index + 1].index : markdown.length),
  }));
}

function withoutCode(markdown) {
  return markdown.replace(/```[\s\S]*?```/gu, '');
}

test('All IT strategy notes use readable text diagrams or tables', async () => {
  const files = await targetNotes();
  assert.equal(files.length, 79, '현재 카탈로그의 IT 전략 과목에는 79개 노트가 있어야 합니다.');
  for (const file of files) {
    const note = await readFile(file, 'utf8');
    assert.match(note, /\|---|```text/u, `${file}: 표 또는 텍스트 도해가 필요합니다.`);
    assert.doesNotMatch(note, /```mermaid/u, `${file}: Mermaid 도해를 제거해야 합니다.`);
    assert.doesNotMatch(note, /<svg\b/iu, `${file}: 인라인 SVG를 제거해야 합니다.`);
    assert.doesNotMatch(note, /class="itpe-(?:flow|pipeline|trace|svg|edm|diagram)/iu, `${file}: 레거시 시각화 HTML 클래스를 제거해야 합니다.`);
  }
});

test('All IT strategy notes start with 개요 and end with 제언', async () => {
  for (const file of await rewrittenNotes()) {
    const note = await readFile(file, 'utf8');
    const sections = romanSections(note);
    assert.ok(sections.length >= 2, `${file}: 로마자 섹션이 최소 2개 이상 필요합니다.`);
    assert.equal(sections[0].number, 'Ⅰ', `${file}: 첫 번째 섹션 번호는 Ⅰ이어야 합니다.`);
    assert.match(sections[0].title, /개요/u, `${file}: 첫 번째 섹션은 '개요'로 시작해야 합니다.`);
    const lastSection = sections[sections.length - 1];
    assert.match(lastSection.title, /제언/u, `${file}: 마지막 섹션은 '제언'으로 끝나야 합니다.`);
  }
});

test('rewritten notes separate closing bold markers from following text', async () => {
  for (const file of await rewrittenNotes()) {
    const note = withoutCode(await readFile(file, 'utf8'));
    const violations = note.split(/\r?\n/u).filter((line) => {
      // '**'로 나눈 홀수 조각이 강조 안쪽, 그다음 조각이 닫는 '**' 뒤의 글자
      const parts = line.split('**');
      for (let index = 1; index + 1 < parts.length; index += 2) {
        if (/^\s|\s$/u.test(parts[index])) return true;
        if (!/^(?:$|[\s|])/u.test(parts[index + 1])) return true;
      }
      return false;
    });
    assert.deepEqual(violations, [], `${file}: 닫는 ** 뒤에는 공백이 필요합니다.`);
  }
});
