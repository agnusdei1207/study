import assert from 'node:assert/strict';
import { readdir, readFile } from 'node:fs/promises';
import path from 'node:path';
import test from 'node:test';

const root = path.resolve('src/content/docs/notes/itpe');

async function markdownNotes(directory) {
  const entries = await readdir(directory, { withFileTypes: true });
  const nested = await Promise.all(
    entries.map(async (entry) => {
      const target = path.join(directory, entry.name);
      if (entry.isDirectory()) return markdownNotes(target);
      return entry.isFile() && entry.name.endsWith('.md') && entry.name !== 'index.md'
        ? [target]
        : [];
    })
  );
  return nested.flat();
}

test('every ITPE topic exposes its writing model and RFC 3339 writing time', async () => {
  const failures = [];

  for (const file of await markdownNotes(root)) {
    const source = await readFile(file, 'utf8');
    const frontmatter = source.match(/^---\r?\n([\s\S]*?)\r?\n---/u)?.[1] ?? '';
    const author = frontmatter.match(/^author:\s*["']?([^"'\r\n]+)["']?\s*$/mu)?.[1]?.trim();
    const date = frontmatter.match(/^date:\s*["']?([^"'\r\n]+)["']?\s*$/mu)?.[1]?.trim();
    const model = frontmatter.match(/(?:^|\n|[{,]\s*)\s*model:\s*["']([^"']+)["']/mu)?.[1]?.trim();

    if (!author || !date || Number.isNaN(Date.parse(date)) || !/(?:Z|[+-]\d{2}:\d{2})$/u.test(date) || !model) {
      failures.push(path.relative(root, file));
    }
  }

  assert.deepEqual(failures, [], `Missing writing metadata:\n${failures.join('\n')}`);
});
