export function formatNoteModel(model) {
  const value = typeof model === 'string' ? model.trim() : '';
  return value ? `작성 모델 · ${value}` : undefined;
}

export function formatNoteDate(date) {
  if (typeof date !== 'string' || Number.isNaN(Date.parse(date))) return undefined;

  const parts = new Intl.DateTimeFormat('en-CA', {
    timeZone: 'Asia/Seoul',
    year: 'numeric',
    month: '2-digit',
    day: '2-digit',
    hour: '2-digit',
    minute: '2-digit',
    hourCycle: 'h23',
  }).formatToParts(new Date(date));
  const part = (type) => parts.find((item) => item.type === type)?.value;

  return `작성 · ${part('year')}.${part('month')}.${part('day')} ${part('hour')}:${part('minute')} KST`;
}
