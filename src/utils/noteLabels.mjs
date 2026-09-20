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

/** Return the public cumulative study grade and reject legacy status/percent badges. */
export function getKeywordGrade(value) {
  if (!value) return undefined;
  const grade = String(value).trim().toUpperCase();
  return /^[ABC]$/u.test(grade) ? grade : undefined;
}
