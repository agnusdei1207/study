import fs from 'fs';
import path from 'path';

const notesDir = path.resolve('src/content/docs/notes');

function getAllNoteFiles(dir) {
  let results = [];
  const list = fs.readdirSync(dir, { withFileTypes: true });
  for (const entry of list) {
    const fullPath = path.join(dir, entry.name);
    if (entry.isDirectory()) {
      results = results.concat(getAllNoteFiles(fullPath));
    } else if (entry.isFile() && /^\d+.*\.md$/.test(entry.name)) {
      results.push(fullPath);
    }
  }
  return results;
}

const files = getAllNoteFiles(notesDir);
console.log(`Found ${files.length} numbered note files.`);

let updatedCount = 0;
let skippedCount = 0;

for (const file of files) {
  let content = fs.readFileSync(file, 'utf8');

  // Match frontmatter
  const fmMatch = content.match(/^---\r?\n([\s\S]*?)\r?\n---/);
  if (!fmMatch) {
    console.warn(`No frontmatter in ${file}`);
    continue;
  }

  let fm = fmMatch[1];
  let isChanged = false;

  // 1. Add author if not present
  if (!/^author:\s*/m.test(fm)) {
    // Insert author after title line or at top
    if (/^title:\s*.*$/m.test(fm)) {
      fm = fm.replace(/^title:\s*.*$/m, (match) => `${match}\nauthor: "Gemini 3.8 Flash"`);
      isChanged = true;
    } else {
      fm = `author: "Gemini 3.8 Flash"\n` + fm;
      isChanged = true;
    }
  }

  // 2. Add extra.model if not present
  if (!/^\s+model:\s*/m.test(fm)) {
    if (/^extra:\s*$/m.test(fm)) {
      fm = fm.replace(/^extra:\s*$/m, 'extra:\n  model: "Gemini 3.8 Flash"');
      isChanged = true;
    } else if (!/^extra:/m.test(fm)) {
      fm = fm + '\nextra:\n  model: "Gemini 3.8 Flash"';
      isChanged = true;
    }
  }

  if (isChanged) {
    const newContent = content.replace(/^---\r?\n[\s\S]*?\r?\n---/, `---\n${fm.trim()}\n---`);
    fs.writeFileSync(file, newContent, 'utf8');
    updatedCount++;
  } else {
    skippedCount++;
  }
}

console.log(`Successfully updated: ${updatedCount}, Skipped: ${skippedCount}`);
