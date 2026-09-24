(() => {
  if (!location.pathname.includes('/notes/itpe/01-it-strategy/')) return;

  function aliases(label) {
    const parts = label.match(/^([^()]+)(?:\(([^)]+)\))?/);
    return [label, parts?.[1], parts?.[2]]
      .filter(Boolean)
      .map((value) => value.trim().toLocaleLowerCase());
  }

  function init() {
    const content = document.querySelector('.sl-markdown-content');
    if (!content) return;
    const glossary = [...content.querySelectorAll('details')]
      .find((details) => details.querySelector('summary')?.textContent?.trim() === '핵심 용어');
    if (!glossary) return;

    const definitions = new Map();
    for (const item of glossary.querySelectorAll('li')) {
      const term = item.querySelector('strong');
      if (!term) continue;
      const description = item.textContent.replace(term.textContent, '').replace(/^\s*[:：-]\s*/, '').trim();
      if (!description) continue;
      for (const alias of aliases(term.textContent)) definitions.set(alias, { label: term.textContent.trim(), description });
    }

    const popup = document.createElement('div');
    popup.className = 'itpe-glossary-tooltip';
    popup.id = 'itpe-glossary-tooltip';
    popup.setAttribute('role', 'tooltip');
    popup.hidden = true;
    document.body.append(popup);
    let current = null;
    let pinned = false;

    function close() {
      if (current) current.removeAttribute('aria-describedby');
      popup.hidden = true;
      current = null;
      pinned = false;
    }

    function open(target, definition, lock = false) {
      if (current && current !== target) current.removeAttribute('aria-describedby');
      current = target;
      pinned = lock;
      popup.replaceChildren();
      const title = document.createElement('strong');
      title.textContent = definition.label;
      const body = document.createElement('span');
      body.textContent = definition.description;
      popup.append(title, body);
      popup.hidden = false;
      target.setAttribute('aria-describedby', popup.id);
      const rect = target.getBoundingClientRect();
      const width = popup.offsetWidth;
      const left = Math.max(8, Math.min(rect.left, innerWidth - width - 8));
      const below = rect.bottom + 8;
      popup.style.left = `${left}px`;
      popup.style.top = `${below + popup.offsetHeight > innerHeight ? Math.max(8, rect.top - popup.offsetHeight - 8) : below}px`;
    }

    for (const target of content.querySelectorAll('strong, .itpe-keyword')) {
      if (target.matches('.itpe-keyword') && target.querySelector('strong')) continue;
      if (glossary.contains(target) || target.closest('.itpe-glossary-trigger')) continue;
      const key = target.textContent.trim().toLocaleLowerCase();
      const definition = definitions.get(key);
      if (!definition) continue;
      target.classList.add('itpe-glossary-trigger');
      target.tabIndex = 0;
      target.setAttribute('role', 'button');
      target.setAttribute('aria-label', `${target.textContent.trim()} 설명`);
      target.addEventListener('pointerenter', () => open(target, definition));
      target.addEventListener('pointerleave', () => { if (!pinned && current === target) close(); });
      target.addEventListener('focus', () => open(target, definition));
      target.addEventListener('blur', () => { if (!pinned && current === target) close(); });
      target.addEventListener('click', (event) => {
        event.stopPropagation();
        if (current === target && pinned) close();
        else open(target, definition, true);
      });
      target.addEventListener('keydown', (event) => {
        if (event.key === 'Enter' || event.key === ' ') {
          event.preventDefault();
          target.click();
        }
      });
    }
    document.addEventListener('click', (event) => { if (current && !current.contains(event.target) && !popup.contains(event.target)) close(); });
    document.addEventListener('keydown', (event) => { if (event.key === 'Escape') close(); });
    window.addEventListener('scroll', () => { if (current && !pinned) close(); }, { passive: true });
  }

  if (document.readyState === 'loading') document.addEventListener('DOMContentLoaded', init, { once: true });
  else init();
})();
