import assert from 'node:assert/strict';
import { readFileSync } from 'node:fs';
import { test } from 'node:test';
import { JSDOM } from 'jsdom';

const script = readFileSync(new URL('../public/itpe-glossary-tooltips.js', import.meta.url), 'utf8');

test('IT strategy glossary opens from matching bold terms by click and keyboard', () => {
  const dom = new JSDOM(`<!doctype html><article class="sl-markdown-content">
    <details><summary>핵심 용어</summary><ul><li><strong>PMO(Project Management Office)</strong> : 발주기관의 사업관리 지원 조직</li><li><strong>Risk Register(위험 등록부)</strong> : 식별한 위험을 추적하는 문서</li></ul></details>
    <h2>1교시 10점 답안</h2><p><strong>PMO</strong>의 역할과 <strong>위험등록부(Risk Register)</strong></p>
  </article>`, { url: 'https://example.com/study/notes/itpe/01-it-strategy/008_it_audit/', runScripts: 'outside-only' });
  dom.window.eval(script);
  dom.window.document.dispatchEvent(new dom.window.Event('DOMContentLoaded'));
  const term = [...dom.window.document.querySelectorAll('article strong')].at(-2);
  const popup = dom.window.document.querySelector('.itpe-glossary-tooltip');
  assert.equal(term.tabIndex, 0);
  term.dispatchEvent(new dom.window.Event('pointerenter'));
  assert.equal(popup.hidden, false);
  term.dispatchEvent(new dom.window.Event('pointerleave'));
  assert.equal(popup.hidden, true);
  term.click();
  assert.equal(popup.hidden, false);
  assert.match(popup.textContent, /발주기관의 사업관리 지원 조직/);
  term.dispatchEvent(new dom.window.KeyboardEvent('keydown', { key: 'Enter', bubbles: true }));
  assert.equal(popup.hidden, true);
  const reversed = [...dom.window.document.querySelectorAll('article strong')].at(-1);
  reversed.click();
  assert.match(popup.textContent, /식별한 위험을 추적하는 문서/);
  const glossaryTerm = dom.window.document.querySelector('details strong');
  glossaryTerm.click();
  assert.match(popup.textContent, /발주기관의 사업관리 지원 조직/);
  dom.window.close();
});
