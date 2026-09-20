import assert from 'node:assert/strict';
import { readdir, readFile } from 'node:fs/promises';
import path from 'node:path';
import test from 'node:test';

const notesRoot = path.resolve('src/content/docs/notes/itpe');

async function markdownFiles(directory) {
  const entries = await readdir(directory, { withFileTypes: true });
  const nested = await Promise.all(entries.map(async (entry) => {
    const target = path.join(directory, entry.name);
    if (entry.isDirectory()) return markdownFiles(target);
    return entry.isFile() && entry.name.endsWith('.md') ? [target] : [];
  }));
  return nested.flat();
}

test('separates blockquotes and HTML blocks from following Markdown blocks', async () => {
  const violations = [];

  for (const file of await markdownFiles(notesRoot)) {
    const source = await readFile(file, 'utf8');
    const lines = source.split(/\r?\n/u);

    for (let index = 0; index < lines.length - 1; index += 1) {
      const current = lines[index];
      const next = lines[index + 1];
      const quoteNeedsBoundary = current.startsWith('>')
        && (/^\|/u.test(next) || /^-/u.test(next) || /^<div\b/u.test(next));
      const htmlNeedsBoundary = /<\/(?:div|details)>\s*$/u.test(current)
        && (/^\|/u.test(next) || /^-/u.test(next));

      if (quoteNeedsBoundary || htmlNeedsBoundary) {
        violations.push(`${path.relative(notesRoot, file)}:${index + 2}`);
      }
    }
  }

  assert.deepEqual(
    violations,
    [],
    `빈 줄이 없어 Markdown 블록이 깨질 수 있습니다:\n${violations.join('\n')}`
  );
});
