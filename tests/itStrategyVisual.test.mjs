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

test('All IT strategy notes follow 7-frame structure (개요→특징→구조→비교→장단점→제언→결론)', async () => {
  for (const file of await rewrittenNotes()) {
    const note = await readFile(file, 'utf8');
    const sections = romanSections(note);
    assert.ok(sections.length >= 7, `${file}: 7개 프레임(Ⅰ~Ⅶ) 섹션이 필요합니다. 현재 ${sections.length}개`);
    assert.equal(sections[0].number, 'Ⅰ', `${file}: 첫 번째 섹션 번호는 Ⅰ이어야 합니다.`);
    assert.match(sections[0].title, /개요/u, `${file}: 첫 번째 섹션은 '개요'를 포함해야 합니다.`);
    // Check 7-frame order: Ⅰ개요 Ⅱ특징 Ⅲ구조 Ⅳ비교 Ⅴ장점/한계 Ⅵ제언 Ⅶ결론
    const titles = sections.map(s => s.title);
    assert.match(titles[1], /특징/u, `${file}: Ⅱ번 섹션은 '특징'을 포함해야 합니다. (실제: ${titles[1]})`);
    assert.match(titles[2], /구조|흐름/u, `${file}: Ⅲ번 섹션은 '구조' 또는 '흐름'을 포함해야 합니다.`);
    assert.match(titles[3], /비교/u, `${file}: Ⅳ번 섹션은 '비교'를 포함해야 합니다.`);
    assert.match(titles[4], /장점|한계/u, `${file}: Ⅴ번 섹션은 '장점' 또는 '한계'를 포함해야 합니다.`);
    assert.match(titles[5], /제언/u, `${file}: Ⅵ번 섹션은 '제언'을 포함해야 합니다.`);
    assert.match(titles[6], /결론/u, `${file}: Ⅶ번 섹션은 '결론'을 포함해야 합니다.`);
  }
});
