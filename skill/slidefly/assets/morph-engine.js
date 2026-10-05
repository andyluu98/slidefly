/* ===========================================================
   MORPH-SLIDES ENGINE (no dependencies)
   - Scales the 1920x1080 stage to the window (letterbox)
   - Builds actors from the style's --actors list
   - Sets data-layout / data-pose / data-parity on .deck-stage
     -> style CSS moves actors, CSS transitions do the "morph"
   - FLIP for elements sharing data-morph-id across two slides
   Input (keys, click, swipe, wheel, #hash) lives in morph-nav.js.
   =========================================================== */
(() => {
  const stage = document.querySelector('.deck-stage');
  const slides = stage ? [...stage.querySelectorAll(':scope > .slide')] : [];
  if (!slides.length) return;
  const REVEAL = '.reveal, .reveal-left, .reveal-right, .reveal-scale, .reveal-blur';
  let cur = -1;
  let scale = 1;

  /* ---------- fit stage to window ---------- */
  function fit() {
    scale = Math.min(innerWidth / 1920, innerHeight / 1080);
    const x = (innerWidth - 1920 * scale) / 2;
    const y = (innerHeight - 1080 * scale) / 2;
    stage.style.transform = `translate(${x}px, ${y}px) scale(${scale})`;
  }

  /* Actors: if the deck has no .actors markup, build them from the style's
     --actors list (DOM order = z-order), so switching style = swapping one CSS link. */
  if (!stage.querySelector('.actors')) {
    const names = getComputedStyle(stage).getPropertyValue('--actors').replace(/["']/g, '').trim().split(/\s+/).filter(Boolean);
    const layer = Object.assign(document.createElement('div'), { className: 'actors back' });
    layer.setAttribute('aria-hidden', 'true');
    names.forEach((name) => {
      const el = Object.assign(document.createElement('div'), { className: 'actor' });
      el.dataset.actor = name;
      layer.append(el);
    });
    stage.prepend(layer);
  }

  /* item count -> type size step. Agenda/timeline/stats tiles are bigger, so they allow more items. */
  function densityOf(slide) {
    const cols = [...slide.querySelectorAll('.col')];
    const n = cols.length
      ? Math.max(...cols.map((c) => c.querySelectorAll('li, p').length))
      : slide.querySelectorAll('.bullets > li, .agenda-list > li, .stats > .stat, .timeline > .step').length;
    const [lg, md] = slide.querySelector('.agenda-list, .timeline, .stats') ? [4, 6] : [3, 5];
    return n <= lg ? 'lg' : n <= md ? 'md' : 'sm';
  }

  /* ---------- one-time prep per slide ---------- */
  const seen = {};
  slides.forEach((slide, k) => {
    // stagger order for reveal items (author may override with style="--i:n")
    slide.querySelectorAll(REVEAL).forEach((el, i) => {
      if (!el.style.getPropertyValue('--i')) el.style.setProperty('--i', i);
    });
    if (!slide.dataset.density) slide.dataset.density = densityOf(slide);
    // parity of the slide itself: content tweaks must not follow the *current* slide
    slide.dataset.parity = k % 2 ? 'even' : 'odd';
    // variant 1..3: Nth time this layout appears (styles may give repeats a different pose)
    const lay = slide.dataset.layout || 'content';
    seen[lay] = (seen[lay] || 0) + 1;
    if (!slide.dataset.variant) slide.dataset.variant = String(((seen[lay] - 1) % 3) + 1);
    slide.querySelectorAll('.agenda-list').forEach((list) => {
      const items = [...list.children];
      const rows = Math.ceil(items.length / 2);
      list.style.setProperty('--rows', rows);
      items.forEach((li, i) => li.classList.toggle('is-right', i >= rows));
    });
  });

  /* ---------- UI chrome ---------- */
  const progress = Object.assign(document.createElement('div'), { className: 'deck-progress' });
  const counter = Object.assign(document.createElement('div'), { className: 'deck-counter' });
  counter.setAttribute('aria-live', 'polite');
  document.body.append(progress, counter);

  function morphMs() {
    const v = getComputedStyle(stage).getPropertyValue('--morph-dur').trim();
    const ms = v.endsWith('ms') ? parseFloat(v) : parseFloat(v) * 1000;
    return Number.isFinite(ms) ? ms : 1200;
  }

  /* rect in stage coordinates (only differences are used) */
  function rectOf(el) {
    const r = el.getBoundingClientRect();
    return { x: r.left / scale, y: r.top / scale, w: r.width / scale, h: r.height / scale };
  }

  /* ---------- FLIP: First, Last, Invert, Play ---------- */
  function flip(a, b, ra, fontA) {
    a._flipDone?.();             // finish any flight still running on either element
    b._flipDone?.();
    b.classList.remove('flip-src');
    b.style.transition = 'none';
    b.style.transformOrigin = '0 0';
    b.style.transform = 'none';
    const rb = rectOf(b);
    if (!rb.w || !rb.h) { b.style.transition = ''; b.style.transform = ''; b.style.transformOrigin = ''; return; }
    const isText = b.textContent.trim() && !b.querySelector('img, svg, video');
    const fontB = parseFloat(getComputedStyle(b).fontSize);
    // text: uniform scale by font-size ratio (avoids squashed letters)
    const sx = isText ? fontA / fontB : ra.w / rb.w;
    const sy = isText ? fontA / fontB : ra.h / rb.h;
    b.style.transform = `translate(${ra.x - rb.x}px, ${ra.y - rb.y}px) scale(${sx}, ${sy})`;
    a.classList.add('flip-src');
    void b.offsetWidth; // commit the inverted position
    b.style.transition = '';
    b.classList.add('flip-run');
    b.style.transform = 'none';

    let timer = 0;
    const onEnd = (e) => { if (e.target === b && e.propertyName === 'transform') done(); };
    const done = () => {
      clearTimeout(timer);
      b.removeEventListener('transitionend', onEnd);
      b.classList.remove('flip-run');
      b.style.transform = '';
      b.style.transformOrigin = '';
      a.classList.remove('flip-src');
      a._flipDone = b._flipDone = null;
    };
    a._flipDone = b._flipDone = done;
    b.addEventListener('transitionend', onEnd);
    timer = setTimeout(done, morphMs() + 150);
  }

  /* ---------- go to slide n ---------- */
  function go(n) {
    n = Math.max(0, Math.min(slides.length - 1, Number(n) || 0));
    if (n === cur) return;
    const from = slides[cur];
    const to = slides[n];

    // FIRST: measure shared elements on the outgoing slide
    const pairs = [];
    if (from) {
      from.querySelectorAll('[data-morph-id]').forEach((a) => {
        const b = to.querySelector(`[data-morph-id="${CSS.escape(a.dataset.morphId)}"]`);
        if (b) pairs.push([a, b, rectOf(a), parseFloat(getComputedStyle(a).fontSize)]);
      });
    }

    // switch: actors re-pose via CSS, content cross-fades.
    // A slide with its own data-pose gets parity "none" so the pose is never fought by parity rules.
    stage.dataset.dir = n > cur ? 'fwd' : 'back';
    stage.dataset.layout = to.dataset.layout || 'content';
    stage.dataset.pose = to.dataset.pose || '';
    stage.dataset.parity = to.dataset.pose ? 'none' : to.dataset.parity;
    stage.dataset.variant = to.dataset.variant;
    stage.dataset.brand = to.dataset.brand || ''; // morph-brand.css: hero | corner | hide
    stage.dataset.slide = String(n + 1);
    from?.classList.remove('active');
    to.classList.add('active');
    cur = n;

    pairs.forEach(([a, b, ra, fa]) => flip(a, b, ra, fa));

    progress.style.width = `${((n + 1) / slides.length) * 100}%`;
    progress.style.background = getComputedStyle(stage).getPropertyValue('--accent'); // bar lives outside the stage
    counter.textContent = `${n + 1} / ${slides.length}`;
    history.replaceState(null, '', `#${n + 1}`);
  }

  addEventListener('resize', fit);

  /* ---------- start: actors fly in from off-stage defaults ---------- */
  fit();
  const start = Math.max(0, (parseInt(location.hash.slice(1), 10) || 1) - 1);
  requestAnimationFrame(() => requestAnimationFrame(() => go(start)));

  window.deck = {
    go,
    next: () => go(cur + 1),
    prev: () => go(cur - 1),
    get index() { return cur; },
    get count() { return slides.length; },
  };
})();
