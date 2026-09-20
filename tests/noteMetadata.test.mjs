import assert from 'node:assert/strict';
import test from 'node:test';

import { formatNoteDate, formatNoteModel } from '../src/utils/noteMetadata.mjs';

test('labels the actual writing model explicitly', () => {
  assert.equal(formatNoteModel('GPT-5.6 Sol'), '작성 모델 · GPT-5.6 Sol');
  assert.equal(formatNoteModel('  '), undefined);
});

test('formats an RFC 3339 timestamp as a visible Korea writing time', () => {
  assert.equal(
    formatNoteDate('2026-09-20T18:55:00+09:00'),
    '작성 · 2026.09.20 18:55 KST'
  );
  assert.equal(formatNoteDate('not-a-date'), undefined);
});
