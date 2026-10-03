import assert from 'node:assert/strict';
import { readdir, readFile } from 'node:fs/promises';
import path from 'node:path';
import test from 'node:test';

const root = 'src/content/docs/notes/itpe';

async function allNotes() {
  const files = [];
  for (const subject of await readdir(root, { withFileTypes: true })) {
    if (!subject.isDirectory()) continue;
    const dir = path.join(root, subject.name);
    for (const name of await readdir(dir)) {
      if (/^\d{3}_.+\.md$/u.test(name)) files.push(path.join(dir, name));
    }
  }
  return files.sort();
}

function proseLines(markdown) {
  return markdown
    .replace(/```[\s\S]*?```/gu, '')
    .replace(/`[^`\n]*`/gu, '')
    .split(/\r?\n/u);
}

test('bold spans close so CommonMark renders them', async () => {
  for (const file of await allNotes()) {
    const violations = proseLines(await readFile(file, 'utf8')).filter((line) => {
      // '**'로 나눈 홀수 조각이 강조 안쪽, 그다음 조각이 닫는 '**' 뒤의 글자
      const parts = line.split('**');
      for (let index = 1; index + 1 < parts.length; index += 2) {
        if (/^\s|\s$/u.test(parts[index])) return true;
        // 문장부호로 끝난 강조 바로 뒤에 글자가 붙으면 닫는 '**'가 인식되지 않는다.
        if (/[\p{P}\p{S}]$/u.test(parts[index]) && /^[\p{L}\p{N}]/u.test(parts[index + 1])) return true;
      }
      return false;
    });
    assert.deepEqual(violations, [], `${file}: 강조 안쪽 공백이나 부호 뒤에 바로 붙은 글자가 있습니다.`);
  }
});

test('bold spans do not leave a space before a following particle', async () => {
  for (const file of await allNotes()) {
    const violations = proseLines(await readFile(file, 'utf8')).filter((line) =>
      /\*\* (?:을|를|은|는|의|에서|으로|와|과|도|만|에)(?:[ .,]|$)/u.test(line),
    );
    assert.deepEqual(violations, [], `${file}: 닫는 ** 와 조사 사이에 공백이 있습니다.`);
  }
});

test('bullet labels are not bolded as keywords', async () => {
  const label = /^\s*-\s+\*\*(?:개념|배경|배경 및 필요성|필요성|특징|목적|주요 목적|핵심 목적|효과|한계점|해결 방안|제언)\*\*\s*:/u;
  for (const file of await allNotes()) {
    const violations = proseLines(await readFile(file, 'utf8')).filter((line) => label.test(line));
    assert.deepEqual(violations, [], `${file}: 불릿 라벨은 굵게 하지 않습니다.`);
  }
});
