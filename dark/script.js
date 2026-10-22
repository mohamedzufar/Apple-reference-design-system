(() => {
  const items = [...document.querySelectorAll('.reveal')];
  const reduceMotion = window.matchMedia('(prefers-reduced-motion: reduce)').matches;
  const canObserve = 'IntersectionObserver' in window;
  if (reduceMotion || !canObserve) {
    items.forEach((item) => item.classList.add('is-visible'));
    return;
  }
  const observer = new IntersectionObserver((entries, currentObserver) => {
    for (const entry of entries) {
      if (!entry.isIntersecting) continue;
      entry.target.classList.add('is-visible');
      currentObserver.unobserve(entry.target);
    }
  }, { threshold: 0.06, rootMargin: '0px 0px -40px 0px' });
  items.forEach((item) => observer.observe(item));
  // If the user changes their OS preference while the page is open, reveal all content.
  const motionQuery = window.matchMedia('(prefers-reduced-motion: reduce)');
  motionQuery.addEventListener?.('change', (event) => {
    if (!event.matches) return;
    items.forEach((item) => item.classList.add('is-visible'));
    observer.disconnect();
  });
})();

(() => {
  document.querySelectorAll('[data-demo-action]').forEach((button) => {
    button.addEventListener('click', () => {
      const output = document.querySelector('#demo-feedback');
      if (output) output.textContent = 'Interaction works — wire this control to your product action.';
    });
  });
})();

(() => {
  const trigger = document.querySelector('[data-menu-trigger]');
  const menu = document.querySelector('[data-mobile-menu]');
  if (!trigger || !menu) return;
  const links = [...menu.querySelectorAll('a')];
  const isOpen = () => trigger.getAttribute('aria-expanded') === 'true';
  const setOpen = (open, {returnFocus = false} = {}) => {
    trigger.setAttribute('aria-expanded', String(open));
    trigger.setAttribute('aria-label', open ? 'Close menu' : 'Open menu');
    menu.dataset.open = String(open);
    menu.setAttribute('aria-hidden', String(!open));
    if (open) {
      menu.removeAttribute('inert');
      requestAnimationFrame(() => links[0]?.focus());
    } else {
      menu.setAttribute('inert', '');
      if (returnFocus) trigger.focus();
    }
  };
  setOpen(false);
  trigger.addEventListener('click', () => setOpen(!isOpen(), {returnFocus: isOpen()}));
  links.forEach(link => link.addEventListener('click', () => setOpen(false)));
  document.addEventListener('keydown', event => {
    if (event.key === 'Escape' && isOpen()) {
      setOpen(false, {returnFocus:true});
    }
  });
  document.addEventListener('click', event => {
    if (isOpen() && !menu.contains(event.target) && !trigger.contains(event.target)) setOpen(false);
  });
  window.addEventListener('resize', () => {
    if (window.matchMedia('(min-width: 901px)').matches && isOpen()) setOpen(false);
  });
})();

// Keep horizontal rails responsive without doing layout work on every scroll event.
(() => {
  document.querySelectorAll('.card-rail').forEach((rail) => {
    let frame = 0;
    const update = () => {
      if (frame) return;
      frame = requestAnimationFrame(() => {
        frame = 0;
        const max = Math.max(0, rail.scrollWidth - rail.clientWidth);
        rail.toggleAttribute('data-scroll-start', rail.scrollLeft <= 2);
        rail.toggleAttribute('data-scroll-end', rail.scrollLeft >= max - 2);
      });
    };
    rail.addEventListener('scroll', update, { passive: true });
    window.addEventListener('resize', update, { passive: true });
    if ('ResizeObserver' in window) new ResizeObserver(update).observe(rail);
    update();
  });
})();

// Keep the demo copyright year current.
document.querySelectorAll('#year').forEach(node => { node.textContent = String(new Date().getFullYear()); });
