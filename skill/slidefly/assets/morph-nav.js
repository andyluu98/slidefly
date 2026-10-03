/* ===========================================================
   MORPH-SLIDES NAVIGATION (load after morph-engine.js)
   Keys: Right/Down/PageDown/Space/Enter = next,
         Left/Up/PageUp/Backspace = back, Home/End, F = fullscreen.
   Click: left quarter = back, elsewhere = next. One-finger swipe.
   Mouse wheel (throttled). Editing the #hash jumps to that slide.
   =========================================================== */
(() => {
  const deck = window.deck;
  if (!deck) return;
  const isEditable = (t) => t.closest?.('a, button, input, textarea, select, [contenteditable]');
  let wheelLock = 0;

  addEventListener('keydown', (e) => {
    // leave browser shortcuts alone (Ctrl+F, Alt+Left, ...)
    if (e.ctrlKey || e.metaKey || e.altKey || isEditable(e.target)) return;
    const k = e.key;
    if (['ArrowRight', 'ArrowDown', 'PageDown', ' ', 'Enter'].includes(k)) { e.preventDefault(); deck.next(); }
    else if (['ArrowLeft', 'ArrowUp', 'PageUp', 'Backspace'].includes(k)) { e.preventDefault(); deck.prev(); }
    else if (k === 'Home') deck.go(0);
    else if (k === 'End') deck.go(deck.count - 1);
    else if (k === 'f' || k === 'F') {
      if (document.fullscreenElement) document.exitFullscreen();
      else document.documentElement.requestFullscreen?.();
    }
  });

  addEventListener('click', (e) => {
    if (isEditable(e.target)) return;
    (e.clientX < innerWidth * 0.25 ? deck.prev : deck.next)();
  });

  let touch = null;
  addEventListener('touchstart', (e) => {
    touch = e.touches.length === 1 ? { x: e.touches[0].clientX, y: e.touches[0].clientY } : null;
  }, { passive: true });
  addEventListener('touchend', (e) => {
    if (!touch || e.touches.length) { touch = null; return; } // pinch / multi-finger: ignore
    const dx = e.changedTouches[0].clientX - touch.x;
    const dy = e.changedTouches[0].clientY - touch.y;
    touch = null;
    if (Math.max(Math.abs(dx), Math.abs(dy)) < 50) return;
    const forward = Math.abs(dx) > Math.abs(dy) ? dx < 0 : dy < 0;
    (forward ? deck.next : deck.prev)();
  });

  addEventListener('wheel', (e) => {
    const now = Date.now();
    if (e.ctrlKey || now < wheelLock || Math.abs(e.deltaY) < 20) return; // ctrl+wheel = zoom
    wheelLock = now + 900;
    (e.deltaY > 0 ? deck.next : deck.prev)();
  }, { passive: true });

  addEventListener('hashchange', () => {
    const n = parseInt(location.hash.slice(1), 10);
    if (n) deck.go(n - 1);
  });
})();
