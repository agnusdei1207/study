/**
 * Build a sidebar label from either an explicit `001. Title` label or the
 * numeric prefix in a note route such as `001_title`.
 */
export function getNoteLabel(label, href) {
  const explicit = label.match(/^(\d{3})\.\s*(.+)$/u);
  if (explicit) {
    return { number: explicit[1], keyword: explicit[2].trim() };
  }

  const path = href.split(/[?#]/, 1)[0].replace(/\/+$/, '');
  const slug = path.slice(path.lastIndexOf('/') + 1);
  const fromSlug = slug.match(/^(\d{3})[_-]/u);

  if (!fromSlug) return undefined;

  return { number: fromSlug[1], keyword: label.trim() };
}

/** Return the study role; accept legacy letter metadata during migration. */
export function getKeywordGrade(value) {
  if (!value) return undefined;
  const label = String(value).trim();
  const roles = { A: '기초', B: '서브', C: '응용' };
  return roles[label.toUpperCase()] ?? (['기초', '서브', '응용'].includes(label) ? label : undefined);
}
