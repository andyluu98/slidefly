/* MORPH-SLIDES GSAP LAYER (optional): real shape morphing with MorphSVG.
   Needs gsap.min.js + MorphSVGPlugin.min.js (GSAP 3.15.0, GreenSock "Standard
   no charge" license) loaded before this file; inline-assets.py embeds them.
   Without GSAP this file does nothing and every shape simply shows its final form.

   <path data-morph-shape="k" d="..."/>            a path (or circle/rect) morphs
   <i class="ico" data-icon="file-text" data-morph-shape="hero"></i>   a Tabler icon morphs
   When a slide shows key "k", its shape grows out of the last shape shown
   with the same key (on the previous slide or any slide before). Pair it with
   data-morph-id on a wrapper to also fly position and size (engine FLIP).
   Automated browsers (check-deck.py) skip the motion and see final shapes. */
(() => {
  const stage = document.querySelector('.deck-stage');
  const { gsap, MorphSVGPlugin } = window;
  if (!stage || !window.deck || !gsap || !MorphSVGPlugin) return;
  gsap.registerPlugin(MorphSVGPlugin);
  const slides = [...stage.querySelectorAll(':scope > .slide')];
  const reduce = matchMedia('(prefers-reduced-motion: reduce)').matches;
  const last = new Map(); // key -> path data last shown

  /* one path per morphing element: icons with several strokes are merged */
  function pathOf(el) {
    if (el.tagName.toLowerCase() === 'path') return el;
    if (/^(circle|rect|ellipse|polygon|polyline|line)$/i.test(el.tagName)) return MorphSVGPlugin.convertToPath(el)[0];
    const svg = el.tagName.toLowerCase() === 'svg' ? el : el.querySelector('svg');
    if (!svg) return null; // icon not loaded yet
    const ready = svg.querySelector('path[data-merged]');
    if (ready) return ready;
    MorphSVGPlugin.convertToPath(svg.querySelectorAll('circle, rect, ellipse, polygon, polyline, line'));
    const parts = [...svg.querySelectorAll('path')].filter((p) => p.getAttribute('stroke') !== 'none');
    if (!parts.length) return null;
    const merged = parts[0];
    merged.setAttribute('d', parts.map((p) => p.getAttribute('d')).join(' '));
    merged.dataset.merged = '';
    parts.slice(1).forEach((p) => p.remove());
    return merged;
  }

  function play() {
    const slide = slides[window.deck.index];
    if (!slide) return;
    slide.querySelectorAll('[data-morph-shape]').forEach((el) => {
      const key = el.dataset.morphShape;
      const p = pathOf(el);
      if (!p) return;
      p.dataset.d0 ||= p.getAttribute('d');
      const to = p.dataset.d0;
      const from = last.get(key);
      last.set(key, to);
      gsap.killTweensOf(p);
      if (!from || from === to || navigator.webdriver) { p.setAttribute('d', to); return; }
      gsap.fromTo(p, { morphSVG: from }, { morphSVG: to, duration: reduce ? 0.4 : 1.15, ease: 'expo.out' });
    });
  }

  new MutationObserver(play).observe(stage, { attributes: true, attributeFilter: ['data-slide'] });
  addEventListener('load', play);
  addEventListener('morph-icons-ready', play); // icons fetched while editing
})();
