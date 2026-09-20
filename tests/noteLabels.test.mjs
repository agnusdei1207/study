import assert from 'node:assert/strict';
import test from 'node:test';

import { getKeywordGrade, getNoteLabel } from '../src/utils/noteLabels.mjs';

test('derives a three-digit note number from the route and preserves the full keyword', () => {
  assert.deepEqual(
    getNoteLabel(
      'ISMP(Information System Master Plan)',
      '/study/notes/itpe/01-it-strategy/001_ismp/'
    ),
    {
      number: '001',
      keyword: 'ISMP(Information System Master Plan)',
    }
  );
});

test('uses an explicit numbered label without duplicating the number', () => {
  assert.deepEqual(
    getNoteLabel('023. 국가 AI 전략', '/study/notes/itpe/01-it-strategy/023_korea_ai_action_plan/'),
    { number: '023', keyword: '국가 AI 전략' }
  );
});

test('does not number subject index routes', () => {
  assert.equal(
    getNoteLabel('01 정보 전략 및 관리', '/study/notes/itpe/01-it-strategy/'),
    undefined
  );
});

test('accepts only A, B, or C as a public keyword grade', () => {
  assert.equal(getKeywordGrade('A'), 'A');
  assert.equal(getKeywordGrade(' b '), 'B');
  assert.equal(getKeywordGrade('C'), 'C');
  assert.equal(getKeywordGrade('기출 · 100%'), undefined);
  assert.equal(getKeywordGrade('100%'), undefined);
});
