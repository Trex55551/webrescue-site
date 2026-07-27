// WebRescue progressive enhancement: menu, year, and sticky header state.
const toggle = document.querySelector('.nav-toggle');
const menu = document.querySelector('#site-menu');

if (toggle && menu) {
  toggle.addEventListener('click', () => {
    const open = toggle.getAttribute('aria-expanded') === 'true';
    toggle.setAttribute('aria-expanded', String(!open));
    menu.dataset.open = String(!open);
  });

  menu.addEventListener('click', (event) => {
    if (event.target.closest('a')) {
      toggle.setAttribute('aria-expanded', 'false');
      menu.dataset.open = 'false';
    }
  });
}

document.querySelectorAll('[data-year]').forEach((node) => {
  node.textContent = new Date().getFullYear();
});

const header = document.querySelector('.site-header');
const setHeader = () => header?.classList.toggle('is-scrolled', window.scrollY > 12);
setHeader();
window.addEventListener('scroll', setHeader, { passive: true });
