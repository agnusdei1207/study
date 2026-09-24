(() => {
  if (!location.pathname.includes('/notes/itpe/01-it-strategy/')) return;

  function normalize(value) {
    return value.toLocaleLowerCase().replace(/[^\p{L}\p{N}]/gu, '');
  }

  function aliases(label) {
    const parts = label.match(/^([^()]+)(?:\(([^)]+)\))?/);
    return [label, parts?.[1], ...(parts?.[2]?.split(/[,/]/) ?? [])]
      .filter(Boolean)
      .map(normalize);
  }

  function writtenAliases(label) {
    const parts = label.match(/^([^()]+)(?:\(([^)]+)\))?/);
    return [parts?.[1], ...(parts?.[2]?.split(/[,/]/) ?? [])]
      .filter(Boolean).map((part) => part.trim()).filter((part) => part.length >= 2);
  }

  function init() {
    const content = document.querySelector('.sl-markdown-content');
    if (!content) return;
    const glossary = [...content.querySelectorAll('details')]
      .find((details) => details.querySelector('summary')?.textContent?.trim() === '핵심 용어');
    if (!glossary) return;

    const definitions = new Map();
    const glossaryTerms = new Map();
    const writtenTerms = [];
    for (const item of glossary.querySelectorAll('li')) {
      const term = item.querySelector('strong');
      if (!term) continue;
      const description = item.textContent.replace(term.textContent, '').replace(/^\s*[:：-]\s*/, '').trim();
      if (!description) continue;
      const definition = { label: term.textContent.trim(), description };
      glossaryTerms.set(term, definition);
      for (const alias of aliases(term.textContent)) definitions.set(alias, definition);
      for (const alias of writtenAliases(term.textContent)) writtenTerms.push({ alias, definition });
    }

    writtenTerms.sort((a, b) => b.alias.length - a.alias.length);

    // A glossary entry is an explanation target even when its first answer mention
    // was left as plain text in the source Markdown.
    for (const answerTitle of [...content.querySelectorAll('h2')].filter((heading) => /(?:1교시 10점 답안|2~4교시 25점 답안)/.test(heading.textContent))) {
      const seen = new Set();
      for (let block = answerTitle.nextElementSibling; block && !(block.matches('h2') && /^(?:2~4교시 예상문제|출제 이력|연결 토픽)/.test(block.textContent.trim())); block = block.nextElementSibling) {
        for (const element of block.matches('p, td, li') ? [block] : block.querySelectorAll('p, td, li')) {
          const walker = document.createTreeWalker(element, NodeFilter.SHOW_TEXT);
          const nodes = [];
          while (walker.nextNode()) nodes.push(walker.currentNode);
          for (const node of nodes) {
            if (node.parentElement.closest('a, code, pre, strong, .itpe-keyword, .itpe-glossary-trigger')) {
              if (node.parentElement.closest('strong')) {
                const match = definitions.get(normalize(node.parentElement.closest('strong').textContent));
                if (match) seen.add(match);
              }
              continue;
            }
            let remaining = node.textContent;
            const fragment = document.createDocumentFragment();
            let changed = false;
            while (remaining) {
              let found = null;
              for (const candidate of writtenTerms) {
                if (seen.has(candidate.definition)) continue;
                const index = remaining.toLocaleLowerCase().indexOf(candidate.alias.toLocaleLowerCase());
                if (index < 0) continue;
                const before = remaining[index - 1] ?? '';
                const after = remaining[index + candidate.alias.length] ?? '';
                if (/^[A-Za-z0-9]$/.test(candidate.alias[0]) && /[A-Za-z0-9]/.test(before)) continue;
                if (/[A-Za-z0-9]$/.test(candidate.alias) && /[A-Za-z0-9]/.test(after)) continue;
                if (!found || index < found.index || (index === found.index && candidate.alias.length > found.candidate.alias.length)) found = { index, candidate };
              }
              if (!found) break;
              fragment.append(document.createTextNode(remaining.slice(0, found.index)));
              const span = document.createElement('span');
              span.className = 'itpe-keyword';
              span.textContent = remaining.slice(found.index, found.index + found.candidate.alias.length);
              fragment.append(span);
              seen.add(found.candidate.definition);
              remaining = remaining.slice(found.index + found.candidate.alias.length);
              changed = true;
            }
            if (changed) {
              fragment.append(document.createTextNode(remaining));
              node.replaceWith(fragment);
            }
          }
        }
      }
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
      if (target.closest('.itpe-glossary-trigger')) continue;
      const definition = glossaryTerms.get(target) ?? aliases(target.textContent)
        .map((alias) => definitions.get(alias)).find(Boolean);
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
