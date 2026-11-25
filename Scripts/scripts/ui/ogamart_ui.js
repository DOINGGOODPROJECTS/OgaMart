// OgaMart UI helpers for GDevelop 5 (paste into a JavaScript code event)
// how to use:
//  1. at the beginning of the scene: run this whole file once, then call gdjs.ogaUI.init(runtimeScene)
//  2. every frame: gdjs.ogaUI.update(runtimeScene)
//  3. call the helpers below from JavaScript events (see GDEVELOP_SETUP.md)

gdjs.ogaUI = (function () {
  const UI = {};
  let tweens = [], loops = [], timers = {}, bars = {}, buttons = {}, sliders = {}, clicked = {}, scene = null;

  // ---- small helpers
  const first = (rs, name) => { const a = rs.getObjects(name); return a && a.length ? a[0] : null; };
  const all = (rs, names) => [].concat(...[].concat(names).map(n => rs.getObjects(n) || []));
  const setTxt = (o, s) => { if (!o) return; if (o.setText) o.setText(String(s)); else if (o.setString) o.setString(String(s)); };
  const fmt = n => Math.round(n).toString().replace(/\B(?=(\d{3})+(?!\d))/g, ',');
  const clamp = (v, a, b) => Math.max(a, Math.min(b, v));
  UI.fmt = fmt;
  const EASE = {
    linear: t => t,
    out: t => 1 - Math.pow(1 - t, 3),
    inOut: t => t < 0.5 ? 4 * t * t * t : 1 - Math.pow(-2 * t + 2, 3) / 2,
    back: t => { const c = 1.70158, c3 = c + 1; return 1 + c3 * Math.pow(t - 1, 3) + c * Math.pow(t - 1, 2); },
  };

  // tween any numeric property through a setter
  function tween(get, set, to, dur, ease, done) {
    const from = get();
    tweens.push({ from, to, t: 0, dur: Math.max(0.0001, dur), set, ease: EASE[ease || 'out'], done });
  }
  UI.tween = tween;
  UI.tweenX = (o, x, d, e, done) => tween(() => o.getX(), v => o.setX(v), x, d, e, done);
  UI.tweenY = (o, y, d, e, done) => tween(() => o.getY(), v => o.setY(v), y, d, e, done);
  UI.tweenW = (o, w, d, e, done) => tween(() => o.getWidth(), v => o.setWidth(v), w, d, e, done);
  UI.tweenOpacity = (o, a, d, e, done) => tween(() => o.getOpacity(), v => o.setOpacity(v), a, d, e, done);
  UI.tweenScale = (o, s, d, e, done) => tween(() => (o.getScale ? o.getScale() : 1), v => o.setScale && o.setScale(v), s, d, e, done);

  UI.init = function (rs) { scene = rs; tweens = []; loops = []; timers = {}; bars = {}; buttons = {}; sliders = {}; clicked = {}; };

  // ---- 1. progress bars (XP, mission, happiness, stock, delivery...)
  // track and fill are Panel Sprites placed on top of each other, fill starts at the track's left edge
  UI.bindBar = function (rs, id, trackName, fillName, value) {
    const tr = first(rs, trackName), fi = first(rs, fillName);
    if (!tr || !fi) return;
    bars[id] = { tr, fi, full: tr.getWidth(), min: fi.getHeight(), value: value || 0 };
    UI.setBar(id, bars[id].value, 0);
  };
  UI.setBar = function (id, value, seconds) {
    const b = bars[id]; if (!b) return;
    b.value = clamp(value, 0, 1);
    const w = b.value <= 0 ? 0 : Math.max(b.min, b.full * b.value);   // never thinner than its round ends
    if (w === 0) { tween(() => b.fi.getWidth(), v => b.fi.setWidth(v), b.min, seconds === undefined ? 0.5 : seconds, 'out', () => b.fi.hide(true)); return; }
    b.fi.hide(false);
    tween(() => b.fi.getWidth(), v => b.fi.setWidth(v), w, seconds === undefined ? 0.5 : seconds, 'out');
  };
  UI.getBar = id => (bars[id] ? bars[id].value : 0);
  // XP that can level up: fills to the end, resets, then fills again
  UI.addXP = function (rs, id, current, gained, needed, onLevelUp) {
    let total = current + gained;
    if (total >= needed) {
      UI.setBar(id, 1, 0.4);
      setTimeout(() => { bars[id] && bars[id].fi.setWidth(bars[id].min); if (onLevelUp) onLevelUp(total - needed); }, 450);
      return total - needed;
    }
    UI.setBar(id, total / needed, 0.6); return total;
  };

  // ---- 2. numbers that count up/down (coins, happiness, scores)
  UI.countTo = function (rs, textName, from, to, seconds, prefix, suffix) {
    const o = first(rs, textName); if (!o) return;
    tween(() => from, v => setTxt(o, (prefix || '') + fmt(v) + (suffix || '')), to, seconds || 0.6, 'out');
    from = to;
  };
  UI.setText = (rs, name, s) => setTxt(first(rs, name), s);

  // ---- 3. buttons: press feel + click detection
  // works with Sprite, Panel Sprite or Text. optional: pass the label/icon objects so they move with the button
  UI.makeButton = function (rs, name, extras, pressedAnim) {
    for (const o of rs.getObjects(name) || []) {
      buttons[name + '#' + o.id] = { o, name, extras: (extras || []).map(n => first(rs, n)).filter(Boolean), down: false, y0: o.getY(), anim: pressedAnim };
    }
  };
  UI.clicked = name => !!clicked[name];          // true for one frame after a tap
  // while a pop-up or sheet is open, only its own buttons react (the screen behind is blocked)
  let modal = null;
  UI.setModal = names => { modal = names ? [].concat(names) : null; };
  function cursorIn(rs, o) {
    const im = rs.getGame().getInputManager();
    const p = rs.getLayer(o.getLayer()).convertCoords(im.getCursorX(), im.getCursorY());
    const bb = o.getAABB();
    return p[0] >= bb.min[0] && p[0] <= bb.max[0] && p[1] >= bb.min[1] && p[1] <= bb.max[1];
  }
  UI.cursorIn = cursorIn;
  function updateButtons(rs) {
    const im = rs.getGame().getInputManager();
    const down = im.isMouseButtonPressed(0);
    const released = im.isMouseButtonReleased ? im.isMouseButtonReleased(0) : false;   // catches very quick taps
    clicked = {};
    for (const k in buttons) {
      const b = buttons[k]; if (!b.o.isVisible || !b.o.isVisible()) continue;
      if (modal && modal.indexOf(b.name) < 0) continue;
      const inside = cursorIn(rs, b.o);
      if (down && inside && !b.down) { b.down = true; press(b, true); }
      if (!down && b.down) { b.down = false; press(b, false); if (inside) { clicked[b.name] = true; rs.getVariables().get('UIClicked').setString(b.name); } }
      else if (!down && released && inside && !clicked[b.name]) { clicked[b.name] = true; rs.getVariables().get('UIClicked').setString(b.name); }
      if (down && b.down && !inside) { b.down = false; press(b, false); }
    }
  }
  function press(b, isDown) {
    const dy = isDown ? 6 : 0;   // 2pt at 3x
    for (const o of [b.o].concat(b.extras)) { if (o._oy === undefined) o._oy = o.getY(); o.setY(o._oy + dy); }
    if (b.anim && b.o.setAnimationName) b.o.setAnimationName(isDown ? b.anim : 'Normal');
  }

  // ---- 4. bottom navigation (5 tabs)
  // NavActive: gold Panel Sprite. NavIcon: Sprite with animations "active"/"inactive", instance variable Index 0-4.
  // NavLabel: Text with instance variable Index.
  UI.setNav = function (rs, index, seconds) {
    const hi = first(rs, 'NavActive');
    const icons = rs.getObjects('NavIcon') || [], labels = rs.getObjects('NavLabel') || [];
    for (const ic of icons) {
      const i = ic.getVariables().get('Index').getAsNumber(); const on = i === index;
      if (ic.setAnimationName) ic.setAnimationName(on ? 'active' : 'inactive');
      if (on && hi) UI.tweenX(hi, ic.getX() + ic.getWidth() / 2 - hi.getWidth() / 2, seconds === undefined ? 0.25 : seconds, 'out');
    }
    for (const lb of labels) {
      const on = lb.getVariables().get('Index').getAsNumber() === index;
      if (lb.setColor) lb.setColor(on ? '43;33;24' : '241;228;200');
    }
  };

  // ---- 5. chips / tabs / segmented control: slide the highlight under the chosen option
  UI.setSegment = function (rs, highlightName, optionName, index, labelName, onColor, offColor) {
    const hi = first(rs, highlightName); if (!hi) return;
    if (labelName) for (const lb of rs.getObjects(labelName) || []) if (lb.setColor) lb.setColor(lb.getVariables().get('Index').getAsNumber() === index ? (onColor || '255;255;255') : (offColor || '43;33;24'));
    for (const op of rs.getObjects(optionName) || []) {
      if (op.getVariables().get('Index').getAsNumber() !== index) continue;
      UI.tweenX(hi, op.getX() + op.getWidth() / 2 - hi.getWidth() / 2, 0.22, 'out');
      if (hi.setWidth && op.getWidth() > 0) UI.tweenW(hi, op.getWidth(), 0.22, 'out');
    }
  };

  // ---- 6. toggles / checkboxes (Sprite with animations "on"/"off")
  UI.setToggle = function (rs, name, on) {
    const o = first(rs, name); if (!o) return;
    if (o.setAnimationName) o.setAnimationName(on ? 'on' : 'off');
    o.getVariables().get('On').setBoolean ? o.getVariables().get('On').setBoolean(on) : o.getVariables().get('On').setNumber(on ? 1 : 0);
  };
  UI.flipToggle = function (rs, name) {
    const o = first(rs, name); if (!o) return false;
    const v = o.getVariables().get('On'); const on = !(v.getAsBoolean ? v.getAsBoolean() : v.getAsNumber() > 0);
    UI.setToggle(rs, name, on); return on;
  };

  // ---- 7. sliders (music, sound, price). value saved in scene variable varName
  UI.makeSlider = function (rs, id, trackName, fillName, knobName, min, max, value, varName, step) {
    const tr = first(rs, trackName), fi = first(rs, fillName), kn = first(rs, knobName); if (!tr || !kn) return;
    sliders[id] = { tr, fi, kn, min, max, value, varName, step: step || 0, drag: false };
    placeSlider(sliders[id]);
  };
  function placeSlider(s) {
    const t = (s.value - s.min) / (s.max - s.min);
    const x = s.tr.getX() + s.tr.getWidth() * t;
    s.kn.setX(x - s.kn.getWidth() / 2);
    if (s.fi) s.fi.setWidth(Math.max(s.fi.getHeight(), s.tr.getWidth() * t));
  }
  function updateSliders(rs) {
    const im = rs.getGame().getInputManager(); const down = im.isMouseButtonPressed(0);
    for (const id in sliders) {
      const s = sliders[id]; if (!s.kn.isVisible()) continue;
      if (down && !s.drag && (cursorIn(rs, s.kn) || cursorIn(rs, s.tr))) s.drag = true;
      if (!down) s.drag = false;
      if (s.drag) {
        const p = rs.getLayer(s.tr.getLayer()).convertCoords(im.getCursorX(), im.getCursorY());
        let t = clamp((p[0] - s.tr.getX()) / s.tr.getWidth(), 0, 1);
        let v = s.min + t * (s.max - s.min); if (s.step) v = Math.round(v / s.step) * s.step;
        s.value = v; placeSlider(s);
        if (s.varName) rs.getVariables().get(s.varName).setNumber(v);
      }
    }
  }
  UI.getSlider = id => (sliders[id] ? sliders[id].value : 0);

  // ---- 8. toasts, pop-ups and sheets
  // slide a group of objects down from above the screen, wait, slide back up
  UI.toast = function (rs, names, seconds, text, textName) {
    const objs = all(rs, names); if (!objs.length) return;
    if (text !== undefined) setTxt(first(rs, textName || 'ToastText'), text);
    const dy = 300;
    for (const o of objs) {
      if (o._ty === undefined) o._ty = o.getY();
      o.hide(false); o.setY(o._ty - dy); if (o.setOpacity) o.setOpacity(0);
      UI.tweenY(o, o._ty, 0.35, 'back'); if (o.setOpacity) UI.tweenOpacity(o, 255, 0.25);
    }
    setTimeout(() => { for (const o of objs) { UI.tweenY(o, o._ty - dy, 0.3, 'inOut', () => o.hide(true)); if (o.setOpacity) UI.tweenOpacity(o, 0, 0.3); } }, (seconds || 2.5) * 1000);
  };
  // pop-up card: grow from 85% with a small bounce. dim is the dark overlay object
  UI.popIn = function (rs, names, dimName) {
    UI.setModal(names);
    if (dimName) for (const d of rs.getObjects(dimName) || []) { d.hide(false); d.setOpacity(0); UI.tweenOpacity(d, 255, 0.25); }
    for (const o of all(rs, names)) {
      o.hide(false);
      if (o._ty === undefined) o._ty = o.getY();
      o.setY(o._ty + 60); if (o.setOpacity) o.setOpacity(0);
      UI.tweenY(o, o._ty, 0.35, 'back'); if (o.setOpacity) UI.tweenOpacity(o, 255, 0.2);
    }
  };
  UI.popOut = function (rs, names, dimName) {
    UI.setModal(null);
    if (dimName) for (const d of rs.getObjects(dimName) || []) UI.tweenOpacity(d, 0, 0.2, 'out', () => d.hide(true));
    for (const o of all(rs, names)) { UI.tweenY(o, (o._ty || o.getY()) + 60, 0.2, 'inOut', () => o.hide(true)); if (o.setOpacity) UI.tweenOpacity(o, 0, 0.2); }
  };
  // bottom sheet: slides up from below the screen
  UI.openSheet = function (rs, names, dimName) {
    UI.setModal(names);
    const h = rs.getGame().getGameResolutionHeight ? rs.getGame().getGameResolutionHeight() : 2532;
    if (dimName) for (const d of rs.getObjects(dimName) || []) { d.hide(false); d.setOpacity(0); UI.tweenOpacity(d, 255, 0.25); }
    for (const o of all(rs, names)) { if (o._ty === undefined) o._ty = o.getY(); o.hide(false); o.setY(o._ty + h * 0.6); UI.tweenY(o, o._ty, 0.4, 'out'); }
  };
  UI.closeSheet = function (rs, names, dimName) {
    UI.setModal(null);
    const h = rs.getGame().getGameResolutionHeight ? rs.getGame().getGameResolutionHeight() : 2532;
    if (dimName) for (const d of rs.getObjects(dimName) || []) UI.tweenOpacity(d, 0, 0.25, 'out', () => d.hide(true));
    for (const o of all(rs, names)) UI.tweenY(o, o._ty + h * 0.6, 0.3, 'inOut', () => o.hide(true));
  };

  // ---- 9. effects
  // "+15" reward: floats up and fades. names = pop background, coin icon, text
  UI.floatUp = function (rs, names, distance, seconds) {
    for (const o of all(rs, names)) {
      if (o._fy === undefined) o._fy = o.getY();
      o.hide(false); o.setY(o._fy); if (o.setOpacity) o.setOpacity(255);
      UI.tweenY(o, o._fy - (distance || 120), seconds || 1.0, 'out');
      if (o.setOpacity) setTimeout(() => UI.tweenOpacity(o, 0, 0.4, 'out', () => o.hide(true)), (seconds || 1.0) * 600);
    }
  };
  // coins fly from (x, y) to the coin pill, then the coin number counts up
  UI.coinFly = function (rs, coinObjName, x, y, targetName, count, onArrive) {
    const target = first(rs, targetName); if (!target) return;
    const tx = target.getX() + target.getWidth() / 2, ty = target.getY() + target.getHeight() / 2;
    for (let i = 0; i < (count || 6); i++) {
      const c = rs.createObject(coinObjName); if (!c) continue;
      c.setX(x + (Math.random() - 0.5) * 90); c.setY(y + (Math.random() - 0.5) * 60);
      const delay = i * 70;
      setTimeout(() => {
        UI.tweenX(c, tx - c.getWidth() / 2, 0.6, 'inOut');
        UI.tweenY(c, ty - c.getHeight() / 2, 0.6, 'inOut', () => { c.deleteFromScene(rs); if (i === (count || 6) - 1 && onArrive) onArrive(); });
      }, delay);
    }
  };
  // looped motion: pulse (alert dot, tutorial ring), bob (tutorial arrow), spin (level-up rays)
  UI.pulse = (rs, name, amount, period) => { for (const o of rs.getObjects(name) || []) loops.push({ o, kind: 'pulse', a: amount || 0.12, p: period || 1, t: 0, s0: o.getScale ? o.getScale() : 1 }); };
  UI.bob = (rs, name, amount, period) => { for (const o of rs.getObjects(name) || []) loops.push({ o, kind: 'bob', a: amount || 18, p: period || 0.8, t: 0, y0: o.getY() }); };
  UI.spin = (rs, name, degPerSec) => { for (const o of rs.getObjects(name) || []) loops.push({ o, kind: 'spin', a: degPerSec || 12, t: 0 }); };
  UI.stopLoops = (name) => { loops = loops.filter(l => l.o.getName() !== name); };
  // confetti: Sprite with 6 animations named c1..c6 (the confetti_1-6 pieces)
  UI.confetti = function (rs, name, count, x, w) {
    const W = w || 1170;
    for (let i = 0; i < (count || 40); i++) {
      const c = rs.createObject(name); if (!c) continue;
      if (c.setAnimationName) c.setAnimationName('c' + (1 + (i % 6)));
      c.setX((x || 0) + Math.random() * W); c.setY(-40 - Math.random() * 400); if (c.setAngle) c.setAngle(Math.random() * 360);
      const fall = 1.6 + Math.random() * 1.2;
      UI.tweenY(c, 2600, fall, 'linear', () => c.deleteFromScene(rs));
      loops.push({ o: c, kind: 'spin', a: 200 + Math.random() * 300, t: 0 });
    }
  };

  // ---- 10. timers (rush hour, deliveries): text "2:14" and optional ring Sprite with 9 frames
  UI.startTimer = function (rs, id, seconds, textName, ringName, onEnd) {
    timers[id] = { left: seconds, total: seconds, text: first(rs, textName), ring: ringName ? first(rs, ringName) : null, onEnd };
  };
  UI.timeLeft = id => (timers[id] ? timers[id].left : 0);
  function updateTimers(dt) {
    for (const id in timers) {
      const t = timers[id]; t.left = Math.max(0, t.left - dt);
      const m = Math.floor(t.left / 60), s = Math.floor(t.left % 60);
      setTxt(t.text, m + ':' + (s < 10 ? '0' : '') + s);
      if (t.ring && t.ring.setAnimationFrame) t.ring.setAnimationFrame(Math.round(8 * (1 - t.left / t.total)));
      if (t.left <= 0) { delete timers[id]; if (t.onEnd) t.onEnd(); }
    }
  }

  // ---- 11. relationship / skill segments (5 Sprites "segment_on"/"segment_off" as animations on/off, variable Index)
  UI.setSegments = function (rs, name, filled) {
    for (const o of rs.getObjects(name) || []) if (o.setAnimationName) o.setAnimationName(o.getVariables().get('Index').getAsNumber() < filled ? 'on' : 'off');
  };

  // ---- frame update: call every frame
  UI.update = function (rs) {
    const dt = rs.getTimeManager().getElapsedTime() / 1000;
    for (let i = tweens.length - 1; i >= 0; i--) {
      const tw = tweens[i]; tw.t += dt; const k = clamp(tw.t / tw.dur, 0, 1);
      try { tw.set(tw.from + (tw.to - tw.from) * tw.ease(k)); } catch (e) { tweens.splice(i, 1); continue; }
      if (k >= 1) { tweens.splice(i, 1); if (tw.done) try { tw.done(); } catch (e) {} }
    }
    for (let i = loops.length - 1; i >= 0; i--) {
      const l = loops[i]; l.t += dt;
      try {
        if (l.kind === 'pulse' && l.o.setScale) l.o.setScale(l.s0 * (1 + l.a * Math.sin(l.t / l.p * Math.PI * 2)));
        if (l.kind === 'bob') l.o.setY(l.y0 + l.a * Math.sin(l.t / l.p * Math.PI * 2));
        if (l.kind === 'spin' && l.o.setAngle) l.o.setAngle(l.o.getAngle() + l.a * dt);
      } catch (e) { loops.splice(i, 1); }
    }
    updateButtons(rs); updateSliders(rs); updateTimers(dt);
  };
  return UI;
})();
