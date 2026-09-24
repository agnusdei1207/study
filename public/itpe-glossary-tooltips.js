(() => {
  if (!location.pathname.includes('/notes/itpe/')) return;

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

    function annotate(element, skippedAncestors) {
      const walker = document.createTreeWalker(element, NodeFilter.SHOW_TEXT);
      const nodes = [];
      while (walker.nextNode()) nodes.push(walker.currentNode);
      for (const node of nodes) {
        if (node.parentElement.closest(skippedAncestors)) continue;
        let remaining = node.textContent;
        const fragment = document.createDocumentFragment();
        let changed = false;
        while (remaining) {
          let found = null;
          for (const candidate of writtenTerms) {
            let searchFrom = 0;
            while (searchFrom < remaining.length) {
              const index = remaining.toLocaleLowerCase().indexOf(candidate.alias.toLocaleLowerCase(), searchFrom);
              if (index < 0) break;
              const before = remaining[index - 1] ?? '';
              const after = remaining[index + candidate.alias.length] ?? '';
              const embeddedBefore = /^[A-Za-z0-9]$/.test(candidate.alias[0]) && /[A-Za-z0-9]/.test(before);
              const embeddedAfter = /[A-Za-z0-9]$/.test(candidate.alias) && /[A-Za-z0-9]/.test(after);
              if (!embeddedBefore && !embeddedAfter) {
                if (!found || index < found.index || (index === found.index && candidate.alias.length > found.candidate.alias.length)) found = { index, candidate };
                break;
              }
              searchFrom = index + 1;
            }
          }
          if (!found) break;
          fragment.append(document.createTextNode(remaining.slice(0, found.index)));
          const span = document.createElement('span');
          span.className = 'itpe-keyword';
          span.textContent = remaining.slice(found.index, found.index + found.candidate.alias.length);
          fragment.append(span);
          remaining = remaining.slice(found.index + found.candidate.alias.length);
          changed = true;
        }
        if (changed) {
          fragment.append(document.createTextNode(remaining));
          node.replaceWith(fragment);
        }
      }
    }

    // Mark every written occurrence from the recall block through the answers.
    const start = [...content.querySelectorAll('h2')].find((heading) => /(?:30초 인출|1교시 10점 답안)/.test(heading.textContent));
    for (let block = start?.nextElementSibling; block && !(block.matches('h2') && /^(?:출제 이력|연결 토픽)/.test(block.textContent.trim())); block = block.nextElementSibling) {
      if (block.matches('details')) continue;
      for (const element of block.matches('p, td, th, li') ? [block] : block.querySelectorAll('p, td, th, li')) {
        annotate(element, 'a, code, pre, strong, details, .itpe-keyword, .itpe-glossary-trigger');
      }
    }

    // A bold phrase can contain multiple glossary terms, such as RTO·RPO.
    for (const term of content.querySelectorAll('strong')) {
      if (term.closest('details') || aliases(term.textContent).some((alias) => definitions.has(alias))) continue;
      annotate(term, 'a, code, pre, details, .itpe-keyword, .itpe-glossary-trigger');
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
      if (target.matches('strong') && target.querySelector('.itpe-keyword')) continue;
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
