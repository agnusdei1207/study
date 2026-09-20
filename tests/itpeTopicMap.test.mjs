import assert from 'node:assert/strict';
import { readFile } from 'node:fs/promises';
import test from 'node:test';

const ismpPath = new URL(
  '../src/content/docs/notes/itpe/01-it-strategy/001_ismp.md',
  import.meta.url
);

test('the exemplar note uses a semantic topic path instead of a generic subject map', async () => {
  const note = await readFile(ismpPath, 'utf8');

  assert.match(note, /## 지식 로드맵 내 현재 위치/u);
  assert.match(note, /class="itpe-topic-path"/u);
  assert.match(note, /정보화 기획·발주/u);
  assert.doesNotMatch(note, /▶ 01 정보 전략·관리/u);
});
