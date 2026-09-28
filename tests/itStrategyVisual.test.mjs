import assert from 'node:assert/strict';
import { readdir, readFile } from 'node:fs/promises';
import path from 'node:path';
import test from 'node:test';

const notesDir = 'src/content/docs/notes/itpe/01-it-strategy';
// 작업 중 특정 노트만 검사: ITPE_IDS=001,002 node --test ...
const ONLY_IDS = process.env.ITPE_IDS?.split(",").map((value) => value.trim()).filter(Boolean);
const inScope = (name) => !ONLY_IDS || ONLY_IDS.includes(name.slice(0, 3));

async function targetNotes() {
  const names = await readdir(notesDir);
  return names.filter((name) => /^\d{3}_.+\.md$/u.test(name)).sort().map((name) => path.join(notesDir, name));
}

async function rewrittenNotes() {
  return (await targetNotes()).filter((file) => inScope(path.basename(file)));
}

function sectionAfter(markdown, headingPattern) {
  const match = markdown.match(headingPattern);
  if (!match || match.index === undefined) return null;
  const rest = markdown.slice(match.index + match[0].length);
  const nextHeading = rest.search(/^##\s+/mu);
  return nextHeading === -1 ? rest : rest.slice(0, nextHeading);
}

function answerBody(markdown) {
  const start = markdown.indexOf('## 2~4교시 25점 답안');
  const end = markdown.indexOf('## 출제 이력과 검증 출처', start);
  return start >= 0 && end > start ? markdown.slice(start, end) : '';
}

function romanSections(answer) {
  const headings = [...answer.matchAll(/^## ([Ⅰ-Ⅻ]+)\.([^\n]*)$/gmu)];
  return headings.map((heading, index) => ({
    number: heading[1],
    title: heading[2].trim(),
    body: answer.slice(heading.index + heading[0].length, index + 1 < headings.length ? headings[index + 1].index : answer.length),
  }));
}

function termAliases(label) {
  const parts = label.match(/^([^()]+)(?:\(([^)]+)\))?/u);
  return [label, parts?.[1], parts?.[2]].filter(Boolean)
    .map((value) => value.toLocaleLowerCase().replace(/[^\p{L}\p{N}]/gu, ''));
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

test('30초 인출은 본질·메커니즘을 중심으로 하고 추가 단서는 선택한다', async () => {
  for (const file of await targetNotes()) {
    const note = await readFile(file, 'utf8');
    const recall = sectionAfter(note, /^## 30초 인출\s*$/mu);
    assert.notEqual(recall, null, `${file}: 30초 인출 절이 필요합니다.`);
    assert.doesNotMatch(recall, /```(?:mermaid|text)/u, `${file}: 30초 인출에는 도해를 넣지 않습니다.`);
    const summary = recall.split(/<details\b/iu, 1)[0];
    const lines = summary.split(/\r?\n/u).map((line) => line.trim()).filter(Boolean);
    assert.ok(lines.length >= 2, `${file}: 30초 인출에는 본질과 메커니즘이 필요합니다.`);
    assert.match(lines[0], /^- (?:\*\*)?본질(?:\*\*)?:/u, `${file}: 첫 줄은 본질이어야 합니다.`);
    assert.match(lines[1], /^- (?:\*\*)?메커니즘(?:\*\*)?:/u, `${file}: 둘째 줄은 메커니즘이어야 합니다.`);
  }
});

test('recall keeps three lines with a one-sentence insight', async () => {
  for (const file of await rewrittenNotes()) {
    const note = await readFile(file, 'utf8');
    const summary = (sectionAfter(note, /^## 30초 인출\s*$/mu) ?? '').split(/<details\b/iu, 1)[0];
    const lines = summary.split(/\r?\n/u).map((line) => line.trim()).filter(Boolean);
    assert.equal(lines.length, 3, `${file}: 30초 인출은 본질·메커니즘·통찰 3줄이어야 합니다.`);
    assert.match(lines[2], /^- 통찰: \S/u, `${file}: 셋째 줄은 통찰이어야 합니다.`);
    assert.doesNotMatch(lines[2], /한계\s*:|→|방안\s*:/u, `${file}: 통찰은 라벨·화살표 없이 한계와 해결 방향을 잇는 한 문장이어야 합니다.`);
  }
});

test('rewritten notes keep one 25-point question and answer without a 10-point answer', async () => {
  for (const file of await rewrittenNotes()) {
    const note = await readFile(file, 'utf8');
    assert.doesNotMatch(note, /^## 1교시/mu, `${file}: 1교시 문항·답안은 두지 않습니다.`);
    assert.match(note, /---\s+## 2~4교시 예상문제 \(25점\)\s+(?:>[^\n]+\s*)+---\s+## 2~4교시 25점 답안/u, `${file}: 문제와 답안 사이에 구분선이 필요합니다.`);
  }
});

test('rewritten answers follow the six-section order and required visuals', async () => {
  for (const file of await rewrittenNotes()) {
    const note = await readFile(file, 'utf8');
    const sections = romanSections(answerBody(note));
    assert.deepEqual(sections.map(({ number }) => number), ['Ⅰ', 'Ⅱ', 'Ⅲ', 'Ⅳ', 'Ⅴ', 'Ⅵ'], `${file}: Ⅰ~Ⅵ 순서가 필요합니다.`);
    const [overview, features, core, extension, limits, proposal] = sections;

    assert.match(overview.title, /개요/u, `${file}: Ⅰ은 개요여야 합니다.`);
    assert.match(overview.body, /^\| 구분 \| 핵심 \|\r?\n\|[^\n]+\|\r?\n\| 정의 \|[^\n]+\|\r?\n\| 목적 \|[^\n]+\|/mu, `${file}: Ⅰ에는 정의·목적 두 행 표가 필요합니다.`);
    assert.doesNotMatch(overview.body, /```text/u, `${file}: Ⅰ에는 도해를 두지 않습니다.`);
    assert.match(features.title, /특징|특성/u, `${file}: Ⅱ 제목에 특징이 드러나야 합니다.`);
    assert.match(core.body, /```text/u, `${file}: Ⅲ에는 체계·프로세스 텍스트 도해가 필요합니다.`);
    assert.match(extension.body, /\|---|```text/u, `${file}: Ⅳ에는 표나 도해가 필요합니다.`);

    assert.match(limits.title, /한계.*방안/u, `${file}: Ⅴ 제목은 한계와 방안이어야 합니다.`);
    const tableHeaders = [...limits.body.matchAll(/^\|[^\n]+\|\r?\n\|\s*:?-{3,}/gmu)];
    assert.equal(tableHeaders.length, 1, `${file}: Ⅴ에는 표가 하나만 있어야 합니다.`);
    assert.match(limits.body, /^\| 한계 \| 방안 \|\r?\n\|---\|---\|/mu, `${file}: Ⅴ 표는 한계 | 방안 두 열이어야 합니다.`);
    const rows = limits.body.split(/\r?\n/u).filter((line) => line.startsWith('|')).slice(2);
    assert.ok(rows.length >= 2, `${file}: Ⅴ 표에는 대응 행이 두 개 이상 필요합니다.`);
    for (const row of rows) assert.equal(row.replace(/\\\|/gu, '').split('|').length, 4, `${file}: Ⅴ 표의 행은 두 열이어야 합니다: ${row}`);

    assert.match(proposal.title, /제언/u, `${file}: Ⅵ은 제언이어야 합니다.`);
    const proposalDiagrams = [...proposal.body.matchAll(/^```text\s*$/gmu)].length;
    assert.ok(proposalDiagrams >= 1 && proposalDiagrams <= 3, `${file}: Ⅵ에는 실행 도해 1~3개가 필요합니다 (현재 ${proposalDiagrams}개).`);
  }
});

test('each overview term has a matching glossary explanation', async () => {
  for (const file of await rewrittenNotes()) {
    const note = await readFile(file, 'utf8');
    const glossary = note.match(/<summary>핵심 용어<\/summary>([\s\S]*?)<\/details>/u)?.[1] ?? '';
    const labels = [...glossary.matchAll(/^- \*\*([^*]+)\*\*/gmu)].flatMap((match) => termAliases(match[1]));
    const term = answerBody(note).match(/^\| 정의 \| \*\*([^*]+)\*\*/mu)?.[1];
    assert.ok(term, `${file}: 정의의 주제명을 강조해야 합니다.`);
    assert.ok(termAliases(term).some((alias) => labels.includes(alias)), `${file}: ${term} 설명이 핵심 용어에 필요합니다.`);
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
