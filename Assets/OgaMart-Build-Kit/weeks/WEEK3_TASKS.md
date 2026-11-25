# Week 3: Characters, Ripple system and testing

**Paste this into Claude Code to start week 3:**

> Read `CLAUDE.md`, `CLAUDE_CODE_PROMPT.md` (sections 6 to 9) and `weeks/WEEK3_TASKS.md`. Weeks 1 and 2 are done (see `PROGRESS.md`). Do the week 3 tasks in order. Stop at the end of each day, show me what you did and how to test it, and wait for my OK.

**Goal (design doc 14.2.4, week 3):** a playable Android prototype with supermarket management, neighborhood building, character interaction and simple ripple consequences.

## Day 1: Mama Biggie and character interaction
- [ ] Mama Biggie walks into the shop as a shopper. She has her own Sprite with all her animations: walk with hip sway, hands on hips, adjust glasses, wave handbag, hip-shake dance and laugh.
- [ ] When she has a dialogue ready (`availableDialogues()`), show a "!" above her. Tapping her opens the `Dialogue` scene.
- [ ] Build the `Dialogue` scene from `layout/OgaMart-3-Mama-Biggie-Conversation.json`:
  - dim store background
  - her big image (`Speaker` Sprite)
  - name plate and FRIENDLY tag
  - speech bubble with the pointer
  - 3 choice buttons with tags
  - Close Conversation and SKIP
- [ ] Choices call `ogaGame.choose()`. Show her reply and her signature animation (for example the dance when you offer a discount), then go back to the shop.
- **Check:** each of the 3 egg-price choices changes happiness, relationship and price as `ogaData.dialogues.mama_eggs` says.

## Day 2: Optional storyline and Customer Happiness
- [ ] Mama Biggie's story has 3 chapters, all optional: the price of eggs → bargain bundle → gossip of the week. Build the `CharacterProfile` scene (screen 11) with the chapters, the relationship bar and the Talk / Request / Discount actions.
- [ ] Customer Happiness (0–100), shown on the top bar and on the `Ripple` scene (screen 9):
  - it rises with good service and full shelves
  - it drops with empty shelves, high prices and long queues
  - it moves slowly, as `ogaGame` does already
- [ ] Ripple toasts: "Mama Biggie loved your egg discount · Happiness +3" slides in.
- **Check:** emptying all the shelves makes happiness fall within about a minute, with "found no milk" toasts. Restocking brings it back.

## Day 3: Two events and five levels
- [ ] **Event 1, Morning rush:** the red banner with a countdown (screen 23 style), more customers, and bread and milk selling 2× faster.
- [ ] **Event 2, VIP visit:** Uncle Money's order card with **Accept order** / **Decline**, using `fulfillVip()` and `declineVip()`.
- [ ] Levels 1 to 5 are fully playable, with the unlocks from the data:
  - level 2: shelves and decor
  - level 3: drinks and snacks
  - level 4: coffee shop
  - level 5: staff (shows "Daniel wants a job")
- [ ] Add the first-10-minutes hints (design doc 3.10), using the `TipCard` with Maya, `HighlightRing` and `TutorialArrow`. Each shows once and can be skipped.
- **Check:** a new player reaches level 4 in about 5 minutes and is guided without being forced.

## Day 4: Missions, saving and Welcome Back
- [ ] Build the `Missions` scene (screen 6):
  - the 5 daily optional missions from `ogaGame.missions()`
  - Accept / Ignore / Claim
  - progress bars
  - the nav badge count
- [ ] Local saving:
  - auto-save every 30 seconds
  - save when the app is paused or closed
  - save on every scene change
  - load at start
- [ ] Welcome Back pop-up (screen 4): offline earnings per business, capped at 4 hours, with **Collect** and an optional **Watch ad · Get 2×**. The ad button uses the `showRewardedAd` stub, which is never required.
- **Check:** close the preview, wait 3 minutes, reopen. The progress is the same, and Welcome Back shows sensible numbers.

## Day 5: Sound and Android
- [ ] Sound and music, using the provided `audio/` folder (`audio/README.md` says when to play each file):
  - copy it into `game/assets/audio/` and register the files as audio resources
  - load `scripts/game/ogamart_audio.js` in `Boot`, after the bridge
  - play `ui_tap` on every button press
  - the shop, neighborhood, menu and rush music loops switch with the scene and with rush events
  - the music and sound volumes come from the Settings sliders
- [ ] Android export settings: package name, icon, portrait lock and keeping the screen awake while playing. Write `ANDROID_BUILD.md` with step-by-step instructions to build the APK from GDevelop.
- [ ] Test on Android: give me a checklist to run on my phone, then fix whatever I report.

## Day 6–7: Bugs and the evaluation build
- [ ] Fix every critical bug.
- [ ] Performance: reuse customer objects instead of creating new ones each time, keep at most 12 actors, and add no per-frame object searches in hot loops.
- [ ] Go through the prototype completion checklist (design doc 14.2.6) and mark each item done, or not done with the reason:
  - players can operate a supermarket
  - customers buy correctly
  - inventory and coin maths work
  - upgrades work
  - neighborhood businesses can be built
  - Mama Biggie appears and interacts
  - Customer Happiness responds to events
  - five levels are playable
  - progress persists after closing
  - the game runs on Android
  - no blocking bugs remain
  - testers understand it without long instructions
- [ ] Run all the tests. Update `PROGRESS.md`, tag the release `v0.1-prototype`, and commit: "Week 3: prototype evaluation build".

**Week 3 deliverable:** an Android prototype APK that meets every item in the design doc 14.2.6 checklist.

## After week 3
Continue with `CLAUDE_CODE_PROMPT.md` milestones M2 (all 42 screens), M3 (levels 1–25 and all content) and M4 (polish and Android release). The design doc suggests 1–3 weeks of stabilization first (section 14.2.5).
