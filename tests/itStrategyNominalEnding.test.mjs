import assert from 'node:assert/strict';
import { readdir, readFile } from 'node:fs/promises';
import path from 'node:path';
import test from 'node:test';

const notesDir = 'src/content/docs/notes/itpe/01-it-strategy';

function section(markdown, start, end) {
  const from = markdown.indexOf(start);
  if (from < 0) return '';
  const to = markdown.indexOf(end, from + start.length);
  return markdown.slice(from + start.length, to < 0 ? undefined : to);
}

test('IT strategy authored explanations end as noun phrases', async () => {
  const names = (await readdir(notesDir)).filter((name) => /^\d{3}_.+\.md$/u.test(name));
  assert.equal(names.length, 81);
  const violations = [];
  for (const name of names) {
    const markdown = await readFile(path.join(notesDir, name), 'utf8');
    const authored = [
      section(markdown, '## 30초 인출', '## 1교시 예상문제'),
      section(markdown, '## 1교시 10점 답안', '## 2~4교시 예상문제'),
      section(markdown, '## 2~4교시 25점 답안', '## 출제 이력과 검증 출처'),
    ];
    for (const part of authored) {
      const lines = part.split(/\r?\n/u);
      for (const line of lines) {
        if (/^\s*(?:- \[|https?:\/\/)/u.test(line)) continue;
        if (/다\.(?=\s|\||$)/u.test(line)) violations.push(`${name}: ${line.trim()}`);
        if (/(?:해야|하도록|되어야|수행|확인|설명|판단|적용|관리|기록|검토|정의|분석|제공|지원|처리|반영|설정|결정|활용|개선|보완|보장|확보|유지|운영|평가|파악|도출|구분)\s*(?:함|됨)(?:\.|\s*\|)?\s*$/u.test(line)) violations.push(`${name}: ${line.trim()}`);
      }
    }
  }
  const firstByFile = new Map();
  for (const violation of violations) {
    const name = violation.split(':', 1)[0];
    const previous = firstByFile.get(name);
    firstByFile.set(name, previous ? { count: previous.count + 1, sample: previous.sample } : { count: 1, sample: violation });
  }
  const summary = [...firstByFile].map(([name, { count, sample }]) => `${name} (${count}건): ${sample.slice(name.length + 2)}`);
  assert.equal(violations.length, 0, `${violations.length}개 평서형·기계적 종결:\n${summary.join('\n')}`);
});
