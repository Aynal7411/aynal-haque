document.addEventListener('DOMContentLoaded', () => {
  const root = document.documentElement;
  const toggle = document.querySelector('[data-theme-toggle]');
  const savedTheme = localStorage.getItem('portfolio-theme');
  const systemPrefersDark = window.matchMedia('(prefers-color-scheme: dark)').matches;

  const applyTheme = (theme) => {
    const resolved = theme === 'system' ? (systemPrefersDark ? 'dark' : 'light') : theme;
    root.setAttribute('data-theme', resolved);
    if (toggle) {
      toggle.setAttribute('aria-label', `Switch to ${resolved === 'dark' ? 'light' : 'dark'} theme`);
      toggle.innerHTML = resolved === 'dark' ? '<i class="bi bi-sun"></i>' : '<i class="bi bi-moon"></i>';
    }
  };

  const currentTheme = savedTheme || 'system';
  applyTheme(currentTheme);

  toggle?.addEventListener('click', () => {
    const current = root.getAttribute('data-theme') || 'dark';
    const nextTheme = current === 'dark' ? 'light' : 'dark';
    localStorage.setItem('portfolio-theme', nextTheme);
    applyTheme(nextTheme);
  });

  const observer = new IntersectionObserver((entries) => {
    entries.forEach((entry) => {
      if (entry.isIntersecting) {
        entry.target.classList.add('is-visible');
        observer.unobserve(entry.target);
      }
    });
  }, { threshold: 0.12 });

  document.querySelectorAll('.reveal').forEach((item) => observer.observe(item));

  const buttons = document.querySelectorAll('[data-filter]');
  const cards = document.querySelectorAll('[data-project-category]');

  buttons.forEach((button) => {
    button.addEventListener('click', () => {
      buttons.forEach((item) => item.classList.remove('is-active'));
      button.classList.add('is-active');
      const filter = button.getAttribute('data-filter');
      cards.forEach((card) => {
        const matches = filter === 'all' || card.getAttribute('data-project-category') === filter;
        card.classList.toggle('is-hidden', !matches);
      });
    });
  });

  const modalBackdrop = document.getElementById('project-modal');
  const modalTitle = document.getElementById('modal-title');
  const modalBody = document.getElementById('modal-body');
  const modalClose = document.getElementById('modal-close');
  const openers = document.querySelectorAll('[data-project-modal]');

  const closeModal = () => modalBackdrop?.classList.remove('is-open');
  const openModal = (content) => {
    if (!modalBackdrop || !modalTitle || !modalBody) return;
    modalTitle.innerHTML = content.title;
    modalBody.innerHTML = content.body;
    modalBackdrop.classList.add('is-open');
    modalBackdrop.querySelector('.modal-card')?.focus();
  };

  openers.forEach((button) => {
    button.addEventListener('click', () => {
      const content = JSON.parse(button.getAttribute('data-project-modal') || '{}');
      openModal(content);
    });
  });

  modalClose?.addEventListener('click', closeModal);
  modalBackdrop?.addEventListener('click', (event) => {
    if (event.target === modalBackdrop) closeModal();
  });
  document.addEventListener('keydown', (event) => {
    if (event.key === 'Escape') closeModal();
  });
});
