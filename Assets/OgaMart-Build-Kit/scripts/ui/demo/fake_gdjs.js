// tiny stand-in for the GDevelop runtime so ogamart_ui.js can run in a browser preview
window.gdjs = {};
(function () {
  const stage = document.getElementById('stage'); let nextId = 1;
  class Var { constructor() { this.v = 0; } getAsNumber() { return +this.v || 0; } setNumber(n) { this.v = n; } setString(s) { this.v = s; } getAsString() { return String(this.v); } getAsBoolean() { return !!this.v; } setBoolean(b) { this.v = !!b; } }
  class Vars { constructor(init) { this.m = {}; for (const k in (init || {})) { this.get(k).setNumber(init[k]); } } get(n) { return this.m[n] || (this.m[n] = new Var()); } }
  class Obj {
    constructor(name, o) {
      this.name = name; this.id = nextId++; this.o = o; this.x = o.x || 0; this.y = o.y || 0; this.angle = 0; this.scale = 1; this.opacity = 255; this.visible = !o.hidden; this.vars = new Vars(o.vars);
      const el = this.el = document.createElement(o.text !== undefined ? 'div' : 'div'); el.className = 'o'; el.style.zIndex = o.z || 1; stage.appendChild(el);
      if (o.text !== undefined) { el.textContent = o.text; Object.assign(el.style, { font: o.font, color: o.color, whiteSpace: 'nowrap', lineHeight: '1' }); this.w = 0; this.h = 0; }
      else if (o.margin !== undefined) { this.w = o.w; this.h = o.h; const m = o.margin; el.style.borderStyle = 'solid'; el.style.borderWidth = `${o.mt ?? m}px ${m}px ${o.mb ?? m}px ${m}px`; el.style.borderImage = `url(${o.img}) ${o.mt ?? m} ${m} ${o.mb ?? m} ${m} fill stretch`; el.style.boxSizing = 'border-box'; }
      else if (o.tiled) { this.w = o.w; this.h = o.h; el.style.background = `url(${o.img})`; el.style.backgroundSize = 'auto 100%'; }
      else { this.anims = o.anims || { Normal: [o.img] }; this.anim = Object.keys(this.anims)[0]; this.frame = 0; this.img = document.createElement('img'); this.img.src = this.anims[this.anim][0]; el.appendChild(this.img); this.w = o.w; this.h = o.h; this.img.style.width = '100%'; this.img.style.height = '100%'; }
      if (o.onTextLoad !== false && o.text !== undefined) requestAnimationFrame(() => { this.w = el.offsetWidth; this.h = el.offsetHeight; });
      this.draw();
    }
    draw() { const s = this.el.style; s.left = this.x + 'px'; s.top = this.y + 'px'; if (this.o.text === undefined) { s.width = this.w + 'px'; s.height = this.h + 'px'; } s.opacity = this.opacity / 255; s.display = this.visible ? 'block' : 'none'; s.transform = `rotate(${this.angle}deg) scale(${this.scale})`; }
    getName() { return this.name; } getX() { return this.x; } setX(v) { this.x = v; this.draw(); } getY() { return this.y; } setY(v) { this.y = v; this.draw(); }
    getWidth() { return this.o.text !== undefined ? this.el.offsetWidth : this.w; } getHeight() { return this.o.text !== undefined ? this.el.offsetHeight : this.h; }
    setWidth(v) { this.w = Math.max(0, v); this.draw(); } setHeight(v) { this.h = v; this.draw(); }
    getOpacity() { return this.opacity; } setOpacity(v) { this.opacity = v; this.draw(); } hide(b) { this.visible = !b; this.draw(); } isVisible() { return this.visible; }
    getScale() { return this.scale; } setScale(v) { this.scale = v; this.draw(); } getAngle() { return this.angle; } setAngle(v) { this.angle = v; this.draw(); }
    setAnimationName(n) { if (this.anims && this.anims[n]) { this.anim = n; this.img.src = this.anims[n][0]; } }
    setAnimationFrame(i) { if (this.anims) { const f = this.anims[this.anim]; this.img.src = f[Math.min(i, f.length - 1)]; } }
    setText(t) { this.el.textContent = t; } setColor(c) { const [r, g, b] = c.split(';'); this.el.style.color = `rgb(${r},${g},${b})`; }
    getVariables() { return this.vars; } getLayer() { return ''; }
    getAABB() { return { min: [this.x, this.y], max: [this.x + this.getWidth(), this.y + this.getHeight()] }; }
    deleteFromScene() { this.el.remove(); const l = scene.objs[this.name]; l.splice(l.indexOf(this), 1); }
  }
  const input = { down: false, x: 0, y: 0, released: false };
  const toStage = e => { const r = stage.getBoundingClientRect(); const p = e.touches ? e.touches[0] : e; return [(p.clientX - r.left) * 1170 / r.width, (p.clientY - r.top) * 2532 / r.height]; };
  stage.addEventListener('pointerdown', e => { input.down = true; [input.x, input.y] = toStage(e); });
  window.addEventListener('pointermove', e => { [input.x, input.y] = toStage(e); });
  window.addEventListener('pointerup', () => { input.down = false; input.released = true; });
  let last = performance.now(), elapsed = 16;
  const scene = window.scene = {
    objs: {}, templates: {}, vars: new Vars(),
    add(name, o) { const ob = new Obj(name, o); (this.objs[name] = this.objs[name] || []).push(ob); return ob; },
    template(name, o) { this.templates[name] = o; this.objs[name] = this.objs[name] || []; },
    getObjects(n) { return this.objs[n] || []; }, createObject(n) { return this.add(n, Object.assign({}, this.templates[n])); },
    getTimeManager() { return { getElapsedTime: () => elapsed }; }, getVariables() { return this.vars; },
    getLayer() { return { convertCoords: (x, y) => [x, y] }; },
    getGame() { return { getInputManager: () => ({ isMouseButtonPressed: () => input.down, isMouseButtonReleased: () => input.released, getCursorX: () => input.x, getCursorY: () => input.y }), getGameResolutionHeight: () => 2532 }; },
  };
  window.runFrames = fn => { const step = now => { elapsed = Math.min(50, now - last); last = now; fn(scene); input.released = false; requestAnimationFrame(step); }; requestAnimationFrame(step); };
})();
