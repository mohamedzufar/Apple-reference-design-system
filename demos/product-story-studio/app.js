(() => {
  const menuButton = document.querySelector('.menu-toggle');
  const mobileNav = document.querySelector('#mobile-nav');
  if (menuButton && mobileNav) {
    menuButton.addEventListener('click', () => {
      const open = menuButton.getAttribute('aria-expanded') === 'true';
      menuButton.setAttribute('aria-expanded', String(!open));
      mobileNav.hidden = open;
    });
    mobileNav.querySelectorAll('a').forEach(link => link.addEventListener('click', () => {
      mobileNav.hidden = true; menuButton.setAttribute('aria-expanded', 'false');
    }));
    document.addEventListener('keydown', e => {
      if (e.key === 'Escape' && !mobileNav.hidden) {
        mobileNav.hidden = true; menuButton.setAttribute('aria-expanded', 'false'); menuButton.focus();
      }
    });
  }

  const details = {
    display: { label: 'Display', title: 'A more immersive canvas.', copy: 'Color, contrast and clarity come together in a space that keeps your attention on the work.' },
    performance: { label: 'Performance', title: 'Ready for demanding work.', copy: 'Responsive performance helps ideas move from rough draft to finished work without getting in your way.' },
    connectivity: { label: 'Connectivity', title: 'Your workflow, connected.', copy: 'Move between tools and tasks with fewer interruptions and more room to focus.' },
    craft: { label: 'Craft', title: 'Every detail has a reason.', copy: 'Careful proportions, tactile surfaces and restrained details make the experience feel considered.' }
  };
  const detail = document.querySelector('.feature-detail');
  const buttons = [...document.querySelectorAll('[data-feature]')];
  buttons.forEach(button => button.addEventListener('click', () => {
    const key = button.dataset.feature; const item = details[key]; if (!item || !detail) return;
    buttons.forEach(b => { const active = b === button; b.classList.toggle('active', active); b.setAttribute('aria-pressed', String(active)); });
    detail.dataset.mode = key;
    document.querySelector('#detail-eyebrow').textContent = item.label;
    document.querySelector('#detail-title').textContent = item.title;
    document.querySelector('#detail-copy').textContent = item.copy;
  }));

  const rail = document.querySelector('#highlight-rail');
  const arrows = [...document.querySelectorAll('[data-rail-dir]')];
  const updateArrows = () => {
    if (!rail) return;
    const max = Math.max(0, rail.scrollWidth - rail.clientWidth);
    arrows.forEach(button => { button.disabled = Number(button.dataset.railDir) < 0 ? rail.scrollLeft <= 2 : rail.scrollLeft >= max - 2; });
  };
  arrows.forEach(button => button.addEventListener('click', () => {
    if (!rail) return;
    const card = rail.querySelector('.rail-card');
    const step = card ? card.getBoundingClientRect().width + 16 : rail.clientWidth * .8;
    rail.scrollBy({ left: step * Number(button.dataset.railDir), behavior: matchMedia('(prefers-reduced-motion: reduce)').matches ? 'auto' : 'smooth' });
  }));
  rail?.addEventListener('scroll', () => requestAnimationFrame(updateArrows), { passive: true });
  if (rail && 'ResizeObserver' in window) new ResizeObserver(updateArrows).observe(rail);
  window.addEventListener('load', updateArrows, { once: true });

  const sections = [...document.querySelectorAll('main section[id]')];
  const navLinks = [...document.querySelectorAll('.product-links a[href^="#"]')];
  if ('IntersectionObserver' in window && sections.length && navLinks.length) {
    const visibleSections = new Map();
    const syncCurrentSection = () => {
      const candidates = [...visibleSections.keys()];
      if (!candidates.length) return;
      // Pick the visible section nearest the upper reading line; this avoids
      // multiple aria-current links when adjacent sections overlap.
      const readingLine = window.innerHeight * 0.3;
      candidates.sort((a, b) => Math.abs(a.getBoundingClientRect().top - readingLine) - Math.abs(b.getBoundingClientRect().top - readingLine));
      const currentId = candidates[0].id;
      navLinks.forEach(link => {
        if (link.getAttribute('href') === `#${currentId}`) link.setAttribute('aria-current', 'location');
        else link.removeAttribute('aria-current');
      });
    };
    const observer = new IntersectionObserver(entries => {
      entries.forEach(entry => {
        if (entry.isIntersecting) visibleSections.set(entry.target, true);
        else visibleSections.delete(entry.target);
      });
      syncCurrentSection();
    }, { rootMargin: '-20% 0px -60% 0px', threshold: 0 });
    sections.forEach(section => observer.observe(section));
  }

  const year = document.querySelector('#year');
  if (year) year.textContent = new Date().getFullYear();
})();
