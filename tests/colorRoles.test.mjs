import assert from 'node:assert/strict';
import { readFile } from 'node:fs/promises';
import test from 'node:test';

test('bold note text and keyword spans use the primary color in every theme', async () => {
  const css = await readFile('src/styles/custom.css', 'utf8');
  const pageTitle = await readFile('src/components/PageTitle.astro', 'utf8');
  const sidebar = await readFile('src/components/SidebarSublist.astro', 'utf8');

  assert.match(css, /\.sl-markdown-content strong\s*\{[^}]*color:\s*var\(--color-primary\)/u);
  assert.match(css, /\.sl-markdown-content \.itpe-keyword strong\s*\{[^}]*color:\s*var\(--color-primary\)/u);
  assert.match(css, /\.sl-markdown-content \.itpe-topic-path > strong\s*\{[^}]*color:\s*var\(--color-primary\)/u);
  assert.match(pageTitle, /\.note-number strong\s*\{[^}]*color:\s*var\(--color-primary\)/u);
  assert.match(sidebar, /\.note-keyword\s*\{[^}]*color:\s*var\(--color-primary\)/u);
  assert.doesNotMatch(css, /:has\(\.itpe-topic-path\)/u);
});

test('component colors go through semantic roles instead of palette values', async () => {
  const css = await readFile('src/styles/custom.css', 'utf8');
  const pageTitle = await readFile('src/components/PageTitle.astro', 'utf8');
  const [, componentCss] = css.split('/* ---------- 4. Semantic roles');

  assert.ok(componentCss, 'semantic role boundary exists');
  assert.doesNotMatch(componentCss, /var\(--palette-/u);
  assert.doesNotMatch(pageTitle, /var\(--palette-/u);
  for (const role of ['primary', 'background', 'surface', 'text', 'text-muted', 'border', 'code-background']) {
    assert.match(css, new RegExp(`--color-${role}: var\\(--palette-`, 'u'));
  }
});
