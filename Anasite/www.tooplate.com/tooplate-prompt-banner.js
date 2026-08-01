const banner = document.getElementById('banner');
const glow = document.getElementById('bannerGlow');
const tabs = document.querySelectorAll('.banner-tab');
const slides = document.querySelectorAll('.banner-slide');
const indicator = document.getElementById('tabIndicator');
const shapePortfolio = document.getElementById('shapePortfolio');
const shapeLanding = document.getElementById('shapeLanding');
const shapes = [shapePortfolio, shapeLanding];
const progressBar = document.getElementById('progressBar');

const links = [
  'https://www.tooplate.com/tools/ai-portfolio-page-prompt-generator',
  'https://www.tooplate.com/tools/ai-landing-page-prompt-generator'
];

let currentTab = 0;
let autoTimer = null;
let progressAnim = null;
const AUTO_DURATION = 5000;

// Position indicator on active tab
function moveIndicator(tabEl) {
  indicator.style.width = tabEl.offsetWidth + 'px';
  indicator.style.transform = `translateX(${tabEl.offsetLeft}px)`;
}

function switchTab(index, direction) {
  if (index === currentTab) return;

  // Update tabs
  tabs.forEach(t => t.classList.remove('is-active'));
  tabs[index].classList.add('is-active');
  moveIndicator(tabs[index]);
  indicator.classList.toggle('is-landing', index === 1);

  // Slide out current
  slides[currentTab].classList.remove('is-active');
  slides[currentTab].classList.add('exit-left');
  setTimeout(() => slides[currentTab].classList.remove('exit-left'), 400);

  // Slide in new
  slides[index].classList.add('is-active');

  // Update link
  banner.href = links[index];

  // Crossfade shapes
  shapes.forEach(s => s.classList.remove('is-active'));
  shapes[index].classList.add('is-active');

  // Progress bar color
  progressBar.className = 'banner-progress-bar ' + (index === 0 ? 'is-portfolio' : 'is-landing');

  currentTab = index;
}

// Tab click
tabs.forEach(tab => {
  tab.addEventListener('click', (e) => {
    e.preventDefault();
    e.stopPropagation();
    const idx = parseInt(tab.dataset.tab);
    switchTab(idx);
    resetAutoRotate();
  });
});

// Auto-rotate with progress
function startProgress() {
  let start = null;
  progressBar.style.width = '0%';

  function step(timestamp) {
    if (!start) start = timestamp;
    const elapsed = timestamp - start;
    const pct = Math.min((elapsed / AUTO_DURATION) * 100, 100);
    progressBar.style.width = pct + '%';

    if (elapsed < AUTO_DURATION) {
      progressAnim = requestAnimationFrame(step);
    } else {
      const next = (currentTab + 1) % 2;
      switchTab(next);
      startProgress();
    }
  }
  progressAnim = requestAnimationFrame(step);
}

function resetAutoRotate() {
  if (progressAnim) cancelAnimationFrame(progressAnim);
  startProgress();
}

// Init
banner.href = links[0];
moveIndicator(tabs[0]);
startProgress();

// Cursor glow
banner.addEventListener('mousemove', (e) => {
  const rect = banner.getBoundingClientRect();
  glow.style.left = (e.clientX - rect.left) + 'px';
  glow.style.top = (e.clientY - rect.top) + 'px';
});
