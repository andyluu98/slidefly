/* SlideFly landing page: live deck projector, mini stage, OS tabs, copy buttons. */
(() => {
  const $ = (s, r = document) => r.querySelector(s);
  const $$ = (s, r = document) => [...r.querySelectorAll(s)];
  const calm = matchMedia('(prefers-reduced-motion: reduce)').matches;

  /* header border once scrolled */
  const top = $('.top');
  const onScroll = () => top.classList.toggle('scrolled', scrollY > 8);
  addEventListener('scroll', onScroll, { passive: true }); onScroll();

  /* ---------- projector: drive the iframe deck ---------- */
  const frame = $('#live');
  const screen = $('.screen');
  const nowName = $('#now-name'), nowNum = $('#now-num'), full = $('#full');
  let idx = 0, count = 10;
  const deckApi = () => { try { return frame.contentWindow.deck || null; } catch { return null; } };
  const show = () => { nowNum.textContent = `${idx + 1}/${count}`; };
  const go = (n) => {
    idx = Math.max(0, Math.min(count - 1, n));
    const d = deckApi();
    if (d) d.go(idx);
    else frame.src = frame.src.replace(/#.*$/, '') + '#' + (idx + 1); // cross-origin (file://) fallback
    screen.classList.add('touched');
    show();
  };
  frame.addEventListener('load', () => {
    const d = deckApi();
    if (d) count = d.count;
    show();
  });
  $('#prev').addEventListener('click', () => go(idx - 1));
  $('#next').addEventListener('click', () => go(idx + 1));
  const hit = $('.hit');
  hit.addEventListener('click', (e) => {
    const r = hit.getBoundingClientRect();
    go(e.clientX && e.clientX - r.left < r.width / 4 ? idx - 1 : idx + 1);
  });
  hit.addEventListener('keydown', (e) => {
    if (e.key === 'ArrowRight') { e.preventDefault(); go(idx + 1); }
    if (e.key === 'ArrowLeft') { e.preventDefault(); go(idx - 1); }
  });
  $$('.chip').forEach((chip) => chip.addEventListener('click', () => {
    $$('.chip').forEach((c) => c.setAttribute('aria-pressed', String(c === chip)));
    const url = `gallery/${chip.dataset.file}.html`;
    frame.src = `${url}#${idx + 1}`;
    full.href = url;
    nowName.textContent = chip.textContent.trim();
  }));

  /* ---------- mini stage: actors change pose ---------- */
  const mini = $('.mini'), tag = $('.pose-tag');
  const poseBtns = $$('.poses button');
  let auto = !calm, timer;
  const setPose = (btn) => {
    poseBtns.forEach((b) => b.setAttribute('aria-pressed', String(b === btn)));
    mini.dataset.pose = btn.dataset.pose;
    tag.textContent = `data-layout="${btn.dataset.pose}"`;
  };
  poseBtns.forEach((b) => b.addEventListener('click', () => { auto = false; clearInterval(timer); setPose(b); }));
  const cycle = () => {
    const i = poseBtns.findIndex((b) => b.getAttribute('aria-pressed') === 'true');
    setPose(poseBtns[(i + 1) % poseBtns.length]);
  };
  if ('IntersectionObserver' in window) {
    new IntersectionObserver(([en]) => {
      clearInterval(timer);
      if (en.isIntersecting && auto) timer = setInterval(cycle, 2600);
    }, { threshold: 0.5 }).observe(mini);
  }

  /* ---------- install: OS tabs ---------- */
  const steps = $('#steps');
  const tabs = $$('.os button');
  const pickOs = (os) => {
    steps.dataset.os = os;
    tabs.forEach((t) => t.setAttribute('aria-selected', String(t.dataset.os === os)));
  };
  tabs.forEach((t) => t.addEventListener('click', () => pickOs(t.dataset.os)));
  pickOs(/Windows/i.test(navigator.userAgent) ? 'win' : 'unix');

  /* ---------- gallery: reveal all 47 styles in place ---------- */
  const shelf = $('#shelf'), showAll = $('#show-all');
  showAll.addEventListener('click', () => {
    const open = shelf.classList.toggle('open');
    showAll.setAttribute('aria-expanded', String(open));
    showAll.textContent = open ? 'Thu gọn' : 'Hiện cả 47 style';
    if (!open) shelf.scrollIntoView({ block: 'start' });
  });

  /* ---------- copy buttons ---------- */
  $$('.code').forEach((box) => {
    const btn = document.createElement('button');
    btn.className = 'copy'; btn.type = 'button'; btn.textContent = 'Sao chép';
    btn.addEventListener('click', async () => {
      const text = $('pre', box).innerText.trim();
      try { await navigator.clipboard.writeText(text); btn.textContent = 'Đã chép'; }
      catch { btn.textContent = 'Không chép được'; }
      setTimeout(() => { btn.textContent = 'Sao chép'; }, 1600);
    });
    box.appendChild(btn);
  });
})();
