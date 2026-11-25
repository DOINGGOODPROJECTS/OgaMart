// headless balance test: a simple bot plays OgaMart and prints when each level is reached
// run: node tests/simulate.js [hours] [seed]
require('../scripts/game/ogamart_data.js'); require('../scripts/game/ogamart_game.js');
const G = gdjs.ogaGame, D = gdjs.ogaData;
const hours = +(process.argv[2] || 6), seed0 = +(process.argv[3] || 1);
let seed = seed0; G.setRandom(() => { seed = (seed * 16807) % 2147483647; return (seed - 1) / 2147483646; });
G.newGame();
const log = []; const t0 = { v: 0 }; let now = 0;
G.on('levelup', e => log.push(`${fmt(now)}  level ${e.level}  ${e.title}  coins=${G.state().coins}  happy=${Math.round(G.state().ind.happiness)}`));
G.on('build', e => log.push(`${fmt(now)}    built ${e.def.name}`));
G.on('staff', e => e.hired && log.push(`${fmt(now)}    hired ${e.hired} as ${e.role}`));
G.on('event_start', e => ev++);
const flow = {}; G.on('coins', e => { flow[e.why] = (flow[e.why] || 0) + e.delta; });
let ev = 0;
function fmt(s) { const h = Math.floor(s / 3600), m = Math.floor(s % 3600 / 60); return `${h}h${String(m).padStart(2, '0')}m`; }
const dt = 0.25; let think = 0;
while (now < hours * 3600) {
  G.tick(dt); now += dt; think += dt;
  if (think < 3) continue; think = 0;
  const S = G.state();
  // restock low shelves (a player taps when it gets low)
  S.shelves.forEach((s, i) => { if (s.product && s.stock < G.shelfCap(s) * 0.35) G.restock(i); });
  // next business to save for (players usually jump at a new business)
  const nextB = G.buildingList().filter(b => b.unlocked && !b.built).sort((a, b) => a.cost - b.cost)[0];
  if (nextB && S.coins > nextB.cost + 100) G.build(nextB.id);
  const buffer = 300 + S.level * 40 + (nextB ? nextB.cost * 0.6 : 0);
  // put newly unlocked products on new shelves
  const unshelved = S.unlocked.products.filter(p => D.products[p].storage === 'shelf' && !S.shelves.some(s => s.product === p));
  if (unshelved.length && S.shelves.length < G.maxShelves() && S.unlocked.upgrades.includes('add_shelf') && S.coins > G.addShelfCost() + buffer) G.addShelf(unshelved[0]);
  S.shelves.forEach((s, i) => { if (S.coins > D.shelf.upgradeCost[s.level] + buffer) G.upgradeShelf(i); });
  for (const u of G.upgradeList().filter(u => u.unlocked && !u.owned && isFinite(u.cost)).sort((a, b) => a.cost - b.cost)) if (S.coins > u.cost + buffer && u.id !== 'add_shelf') G.buyUpgrade(u.id);
  for (const b of S.buildings) { if (b.level < 2 && S.coins > D.buildings[b.type].upgradeCost[b.level] + buffer * 2) G.upgradeBuilding(b.id); }
  if (Math.floor(now) % 60 < 3) G.collectAll();
  for (const c of G.candidates()) { if (S.staff.length < 2 + Math.floor(S.level / 5) && S.coins > 600 + buffer) G.hire(c.id); }
  for (const st of S.staff) if (S.coins > G.trainCost(st.id) + buffer * 2) G.train(st.id);
  for (const m of G.missions()) { if (m.state === 'new') G.acceptMission(m.uid); if (m.state === 'done') G.claimMission(m.uid); }
  for (const d of G.availableDialogues()) G.choose(d, 0);
  if (S.event && S.event.order) { if (!G.fulfillVip()) G.declineVip(); }
}
console.log(log.join('\n'));
const d = G.dashboard();
console.log(flow);
console.log(`\nafter ${hours}h: level ${d.level} coins ${d.coins} sold ${d.sold} served ${d.served} missed ${d.missed} happy ${d.happiness} trust ${d.trust} growth ${d.growth} businesses ${d.businesses} staff ${d.staff} events ${ev}`);
