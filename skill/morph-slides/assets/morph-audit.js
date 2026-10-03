/* ===========================================================
   MORPH-SLIDES AUDIT: measures how well each slide fills space.
   Run in the browser console (or via a test tool): deck.audit()
   - Collects "ink" (text line boxes + media) per slide.
   - maxGapY / maxGapX = biggest empty band inside the safe area.
   - overflow = ink outside the slide or past the safe margins.
   Display slides (cover, section, quote, closing) are only
   checked for overflow: their emptiness is intentional.
   =========================================================== */
(() => {
  const stage = document.querySelector('.deck-stage');
  if (!stage || !window.deck) return;
  const SAFE = { x0: 80, x1: 1840, y0: 60, y1: 1020 };
  const LIMIT = { gapY: 0.28, gapX: 0.3 };
  // big-number slides are meant to breathe around the figures
  const LIMIT_Y_BY_LAYOUT = { stats: 0.34 };
  const DISPLAY = ['cover', 'section', 'quote', 'closing'];

  /* text line boxes + images/svg, in stage coordinates */
  function inkRects(slide) {
    const s = stage.getBoundingClientRect();
    const k = s.width / 1920;
    const out = [];
    const push = (r) => {
      if (r.width < 1 || r.height < 1) return;
      out.push({ x0: (r.left - s.left) / k, x1: (r.right - s.left) / k, y0: (r.top - s.top) / k, y1: (r.bottom - s.top) / k });
    };
    const walker = document.createTreeWalker(slide, NodeFilter.SHOW_TEXT);
    while (walker.nextNode()) {
      const node = walker.currentNode;
      if (!node.textContent.trim()) continue;
      const range = document.createRange();
      range.selectNodeContents(node);
      [...range.getClientRects()].forEach(push);
    }
    slide.querySelectorAll('img, svg, video, canvas').forEach((el) => push(el.getBoundingClientRect()));
    return out;
  }

  /* biggest uncovered interval of [lo, hi] given covered spans */
  function maxGap(spans, lo, hi) {
    const sorted = spans.map(([a, b]) => [Math.max(a, lo), Math.min(b, hi)]).filter(([a, b]) => b > a).sort((p, q) => p[0] - q[0]);
    let gap = 0;
    let cursor = lo;
    for (const [a, b] of sorted) {
      gap = Math.max(gap, a - cursor);
      cursor = Math.max(cursor, b);
    }
    return Math.max(gap, hi - cursor);
  }

  function auditSlide(slide, i) {
    const layout = slide.dataset.layout || 'content';
    const ink = inkRects(slide);
    const issues = [];
    const out = ink.filter((r) => r.x0 < SAFE.x0 - 40 || r.x1 > SAFE.x1 + 40 || r.y0 < SAFE.y0 - 30 || r.y1 > SAFE.y1 + 30);
    if (out.length) issues.push(`tràn khung (${out.length} dòng)`);
    // text overflow = a text line box past its container (decorative pseudo-elements are ignored)
    slide.querySelectorAll('.col, .takeaway, .highlight').forEach((box) => {
      const b = box.getBoundingClientRect();
      const range = document.createRange();
      range.selectNodeContents(box);
      const past = [...range.getClientRects()].some((r) => r.height && (r.bottom > b.bottom + 2 || r.right > b.right + 2));
      if (past) issues.push(`chữ tràn hộp .${box.className.split(' ')[0]}`);
    });
    const gapY = maxGap(ink.map((r) => [r.y0, r.y1]), SAFE.y0, SAFE.y1) / (SAFE.y1 - SAFE.y0);
    const gapX = maxGap(ink.map((r) => [r.x0, r.x1]), SAFE.x0, SAFE.x1) / (SAFE.x1 - SAFE.x0);
    const display = DISPLAY.includes(layout);
    if (!display && gapY > (LIMIT_Y_BY_LAYOUT[layout] || LIMIT.gapY)) issues.push(`trống dọc ${Math.round(gapY * 100)}%`);
    if (!display && gapX > LIMIT.gapX) issues.push(`trống ngang ${Math.round(gapX * 100)}%`);
    return {
      slide: i + 1, layout, density: slide.dataset.density || '',
      gapY: `${Math.round(gapY * 100)}%`, gapX: `${Math.round(gapX * 100)}%`,
      status: issues.length ? 'SỬA' : 'OK', issues: issues.join('; '),
    };
  }

  window.deck.audit = () => {
    stage.classList.add('auditing');
    const slides = [...stage.querySelectorAll(':scope > .slide')];
    const report = slides.map(auditSlide);
    stage.classList.remove('auditing');
    console.table(report);
    return report;
  };
})();
