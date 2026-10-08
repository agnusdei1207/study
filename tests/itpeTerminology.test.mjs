import assert from 'node:assert/strict';
import fs from 'node:fs';
import path from 'node:path';
import test from 'node:test';
import { auditNotes, namesForFile, root, terminologyIssues, titleIssues } from '../scripts/audit-itpe-terminology.mjs';

test('audits every ITPE subject and note for known terminology regressions', () => {
  const results = auditNotes();
  assert.equal(new Set(results.map(({ file }) => path.dirname(file))).size, 8);
  assert.ok(results.length >= 939, 'The audit must cover the complete corpus');
  assert.deepEqual(results.flatMap(({ file, issues }) => issues.map(issue => `${file}: ${issue}`)), []);
});

test('keeps title meanings contextual and product identifiers unexpanded', () => {
  assert.equal(namesForFile('092_technology_acceptance_model.md').TAM, 'Technology Acceptance Model');
  assert.equal(namesForFile('089_tam_sam_som.md').TAM, 'Total Addressable Market');
  assert.equal(namesForFile('118_som.md').SOM, 'Self-Organizing Map');
  assert.equal(namesForFile('111_mac.md').MAC, 'Message Authentication Code');
  assert.deepEqual(titleIssues('rack_scale.md', 'GB200 NVL72'), []);
  assert.deepEqual(titleIssues('011_csma_ca.md', 'CSMA/CA(Carrier Sense Multiple Access with Collision Avoidance)'), []);
  assert.ok(titleIssues('001_ismp.md', 'ISMP').length > 0);
});

test('rejects invented expansions without rejecting real meanings in other fields', () => {
  assert.ok(terminologyIssues('08-law-policy/fee.md', 'FP, Floating Point').length > 0);
  assert.deepEqual(terminologyIssues('04-computer-system/arithmetic.md', 'FP, Floating Point'), []);
  assert.ok(terminologyIssues('ai.md', 'LIME(Lightweight Interoperability of Model Explanations)').length > 0);
  assert.ok(terminologyIssues('ci.md', '**CDelivery**').length > 0);
});

test('distinguishes signature validation from customer lifetime value', () => {
  const signature = fs.readFileSync(path.join(root, '06-security/079_digital_signature.md'), 'utf8');
  const crm = fs.readFileSync(path.join(root, '01-it-strategy/031_crm.md'), 'utf8');
  assert.match(signature, /LTV, Long-Term Validation/);
  assert.match(crm, /CLV\(Customer Lifetime Value\)/);
  assert.match(crm, /LTV\(Lifetime Value\)/);
});
