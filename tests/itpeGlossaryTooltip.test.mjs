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

test('plain first mentions of selected glossary terms receive the same tooltip in both answers', () => {
  const dom = new JSDOM(`<!doctype html><article class="sl-markdown-content">
    <details><summary>핵심 용어</summary><ul><li><strong>기술수용모델(TAM, Technology Acceptance Model)</strong> : 유용성과 용이성으로 기술 수용을 설명하는 모델</li></ul></details>
    <h2>1교시 10점 답안</h2><h3>Ⅰ. 개요</h3><p>TAM은 사용 의도를 설명한다.</p>
    <h2>2~4교시 예상문제</h2><h2>2~4교시 25점 답안</h2><h2>Ⅰ. 개요</h2><p>기술수용모델은 수용 요인을 다룬다.</p>
    <h2>출제 이력과 검증 출처</h2>
  </article>`, { url: 'https://example.com/study/notes/itpe/01-it-strategy/092_technology_acceptance_model/', runScripts: 'outside-only' });
  dom.window.eval(script);
  dom.window.document.dispatchEvent(new dom.window.Event('DOMContentLoaded'));
  const triggers = [...dom.window.document.querySelectorAll('p .itpe-glossary-trigger')];
  assert.equal(triggers.length, 2);
  assert.deepEqual(triggers.map((trigger) => trigger.textContent), ['TAM', '기술수용모델']);
  const popup = dom.window.document.querySelector('.itpe-glossary-tooltip');
  for (const trigger of triggers) {
    trigger.click();
    assert.match(popup.textContent, /유용성과 용이성/);
  }
  dom.window.close();
});

test('every answer mention of a glossary term receives a tooltip', () => {
  const dom = new JSDOM(`<!doctype html><article class="sl-markdown-content">
    <details><summary>핵심 용어</summary><ul><li><strong>PMO(Project Management Office)</strong> : 프로젝트 관리 조직</li></ul></details>
    <h2>1교시 10점 답안</h2><p><strong>PMO</strong>가 기준을 정한다. PMO가 결과를 확인한다.</p>
    <h2>2~4교시 예상문제</h2><h2>2~4교시 25점 답안</h2><p>PMO의 권한과 PMO의 책임을 구분한다.</p>
    <h2>출제 이력과 검증 출처</h2>
  </article>`, { url: 'https://example.com/study/notes/itpe/01-it-strategy/004_pmo/', runScripts: 'outside-only' });
  dom.window.eval(script);
  dom.window.document.dispatchEvent(new dom.window.Event('DOMContentLoaded'));
  const triggers = [...dom.window.document.querySelectorAll('article p .itpe-glossary-trigger')];
  assert.deepEqual(triggers.map((trigger) => trigger.textContent), ['PMO', 'PMO', 'PMO', 'PMO']);
  const popup = dom.window.document.querySelector('.itpe-glossary-tooltip');
  for (const trigger of triggers) {
    trigger.click();
    assert.match(popup.textContent, /프로젝트 관리 조직/);
  }
  dom.window.close();
});

test('combined bold terms and terms outside answers link to their own definitions', () => {
  const dom = new JSDOM(`<!doctype html><article class="sl-markdown-content">
    <h2>30초 인출</h2><p>RTO·RPO 목표를 확인한다.</p>
    <details><summary>핵심 용어</summary><ul>
      <li><strong>RTO(Recovery Time Objective)</strong> : 복구 목표시간</li>
      <li><strong>RPO(Recovery Point Objective)</strong> : 복구 목표시점</li>
    </ul></details>
    <h2>1교시 10점 답안</h2><p><strong>RTO·RPO</strong>를 비교한다.</p>
    <table><thead><tr><th>RTO</th><th>RPO</th></tr></thead></table>
    <h2>출제 이력과 검증 출처</h2>
  </article>`, { url: 'https://example.com/study/notes/itpe/01-it-strategy/006_sla/', runScripts: 'outside-only' });
  dom.window.eval(script);
  dom.window.document.dispatchEvent(new dom.window.Event('DOMContentLoaded'));
  const body = dom.window.document.querySelector('article');
  const triggers = [...body.querySelectorAll('p .itpe-glossary-trigger, th .itpe-glossary-trigger')];
  assert.deepEqual(triggers.map((trigger) => trigger.textContent), ['RTO', 'RPO', 'RTO', 'RPO', 'RTO', 'RPO']);
  const popup = dom.window.document.querySelector('.itpe-glossary-tooltip');
  triggers[2].click();
  assert.match(popup.textContent, /복구 목표시간/);
  triggers[3].click();
  assert.match(popup.textContent, /복구 목표시점/);
  dom.window.close();
});

test('a later standalone acronym still matches after an embedded occurrence', () => {
  const dom = new JSDOM(`<!doctype html><article class="sl-markdown-content">
    <details><summary>핵심 용어</summary><ul><li><strong>AI(Artificial Intelligence)</strong> : 인공지능</li></ul></details>
    <h2>1교시 10점 답안</h2><p>OpenAI 기반 AI 서비스</p>
    <h2>출제 이력과 검증 출처</h2>
  </article>`, { url: 'https://example.com/study/notes/itpe/01-it-strategy/050_ai_governance_platform/', runScripts: 'outside-only' });
  dom.window.eval(script);
  dom.window.document.dispatchEvent(new dom.window.Event('DOMContentLoaded'));
  const triggers = [...dom.window.document.querySelectorAll('p .itpe-glossary-trigger')];
  assert.deepEqual(triggers.map((trigger) => trigger.textContent), ['AI']);
  dom.window.close();
});
