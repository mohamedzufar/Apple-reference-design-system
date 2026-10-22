/* Optional reveal helper. It does not hijack scrolling or add custom scroll physics. */
(() => {
  const targets = document.querySelectorAll('.motion-reveal');
  if (!targets.length) return;

  const reduced = window.matchMedia('(prefers-reduced-motion: reduce)').matches;
  if (reduced || !('IntersectionObserver' in window)) {
    targets.forEach((el) => {
      el.dataset.motionVisible = 'true';
      el.removeAttribute('data-motion-pending');
    });
    return;
  }

  const observer = new IntersectionObserver((entries) => {
    entries.forEach((entry) => {
      if (!entry.isIntersecting) return;
      entry.target.dataset.motionVisible = 'true';
      entry.target.removeAttribute('data-motion-pending');
      observer.unobserve(entry.target);
    });
  }, { rootMargin: '0px 0px -8% 0px', threshold: 0.08 });

  targets.forEach((el) => {
    el.dataset.motionPending = 'true';
    observer.observe(el);
  });
})();
