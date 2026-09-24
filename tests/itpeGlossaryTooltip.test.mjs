import assert from 'node:assert/strict';
import { readFileSync } from 'node:fs';
import { test } from 'node:test';
import { JSDOM } from 'jsdom';

const script = readFileSync(new URL('../public/itpe-glossary-tooltips.js', import.meta.url), 'utf8');

test('IT strategy glossary opens from matching bold terms by click and keyboard', () => {
  const dom = new JSDOM(`<!doctype html><article class="sl-markdown-content">
    <details><summary>핵심 용어</summary><ul><li><strong>PMO(Project Management Office)</strong> : 발주기관의 사업관리 지원 조직</li></ul></details>
    <h2>1교시 10점 답안</h2><p><strong>PMO</strong>의 역할</p>
  </article>`, { url: 'https://example.com/study/notes/itpe/01-it-strategy/008_it_audit/', runScripts: 'outside-only' });
  dom.window.eval(script);
  dom.window.document.dispatchEvent(new dom.window.Event('DOMContentLoaded'));
  const term = [...dom.window.document.querySelectorAll('article strong')].at(-1);
  const popup = dom.window.document.querySelector('.itpe-glossary-tooltip');
  assert.equal(term.tabIndex, 0);
  term.click();
  assert.equal(popup.hidden, false);
  assert.match(popup.textContent, /발주기관의 사업관리 지원 조직/);
  term.dispatchEvent(new dom.window.KeyboardEvent('keydown', { key: 'Enter', bubbles: true }));
  assert.equal(popup.hidden, true);
  dom.window.close();
});
