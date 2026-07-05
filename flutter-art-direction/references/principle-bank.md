# Flutter Art Direction Principle Bank

Use this file when a Flutter app needs a stronger visual or emotional point of view. These principles are reference-inspired, not app-copying. Apply the principle that matches the brief; do not imitate the named app's surface style.

## Core Principles

### Visceral-Behavioral-Reflective Alignment

Great apps create emotional coherence across all three Norman levels. Every screen should have an intentional visceral reaction (first impression), reliable behavioral response (usability), and reflective meaning (long-term connection).

Flutter implication:

- Map every visual element to one of three emotional registers: visceral (aesthetic), behavioral (function), reflective (meaning)
- Ensure empty/error/loading states match the emotional stance
- Use design tokens to carry emotional meaning (e.g., color_scheme.surfaceBase for calm, accent_primary for attention)

Anti-slop failure:

- Apps that feel emotionally inconsistent (beautiful but unusable, usable but forgettable)
- Emotional design treated as decoration rather than functional layer

### Design Token as System Layer

Design tokens are the single source of truth for visual decisions. They're not just colors and spacing, but semantic rules that can be checked, validated, and shared across platforms.

Flutter implication:

- Create a token system that automatically generates themes (light/dark, platform, reduced motion)
- Use tokens for all visual properties: `AppTokens.colors.surfaceBase`, `AppTokens.spacing.cardPadding`, `AppTokens.typography.body`
- Provide code generation to keep tokens in sync with UI changes

Anti-slop failure:

- Mix of hardcoded values and semantic tokens
- Visual inconsistency between screens

### Spatial Depth as Hierarchy

Depth in mobile interfaces should communicate information priority, not decoration. Use elevation, shadow, and layering to establish visual hierarchy and cognitive flow.

Flutter implication:

- Implement a limited set of elevation levels (0-5) using shadows or layered surfaces
- Use depth to indicate importance: cards float above content, modals above everything
- Consistent depth language across all screens

Anti-slop failure:

- Arbitrary z-index and shadow variations
- Depth used for decoration without hierarchy purpose

### Material as Implementation Substrate

Material Design and Cupertino are reliable foundations, not design identities. Use them to solve specific platform problems, but let the app's product world define its visual language.

Flutter implication:

- Platform-specific implementations: `MaterialApp` with custom themes, `CupertinoApp` with semantic overrides
- Compose, don't copy: Material patterns adapted to the app's world
- Platform affordances should be believable but never the entire UI

Anti-slop failure:

- Generic Material or Cupertino apps without product identity
- Platform-specific but not app-native

### Adaptive Theming Beyond Light/Dark

Theming is more than color inversion. Modern apps need dynamic color, platform adaptation, and context-aware variations.

Flutter implication:

- Dynamic Color (Material You) adapts to wallpaper/content
- Platform-specific tuning: more texture on Android, flatter on iOS
- Responsive theming for different window sizes, orientations, and reduced motion

Anti-slop failure:

- One-size-fits-all theme (dark mode only inversion)
- Static theming that ignores device context

### Gesture-First Interaction Design

Mobile interactions should prioritize finger gestures, device sensors, and context-aware flows over button-centric interfaces.

Flutter implication:

- Swipe-back navigation, drag-to-reorder, long-press actions
- Haptic feedback that signals intent
- Platform-contextual gestures (iOS immune swipe, Android back gesture)
- Discoverable affordances for gesture vocabulary

Anti-slop failure:

- Button-centric flows that ignore mobile interaction patterns
- Hidden or poorly labeled gestures

### Spatial Depth as Hierarchy Failure

Depth is abused: random z-index values, inconsistent shadow systems, elevation that doesn't communicate hierarchy.

### Adaptive Theming Failure

Themes are reactive, not anticipatory: dark/light only, platform curves applied without product context.

### Gesture-First Failure

Gestures are documented but not used: generic buttons where swipe-back, drag, and long-press would be more native.

### Accessibility as Design Constraint

Accessibility is not a checklist but a design discipline that shapes layout, typography, motion, and interaction from the start.

Flutter implication:

- Semantic widgets: `Semantics(label: 'button')`, `ExcludeSemantics()`, `MergeSemantics()`
- Touch target sizes: 44×44pts (iOS), 48×48dp (Android) minimum
- Color contrast validation: WCAG AA (4.5:1), with higher contrast for large text
- Reduced motion: `MediaQuery.disableAnimations` respected everywhere

Anti-slop failure:

- Accessibility layered on top of design
- Assumed rather than designed for accessibility

### Product world before components

Great mobile apps feel like they come from a world, not a widget catalog. Before designing screens, define the world: museum archive, soft diary, humane coach, flight control room, creative toybox, premium camera, neighborhood marketplace, or focused workbench.

Flutter implication:

- Build theme, type, motion, assets, and component names from the world.
- Prefer product-specific widgets over generic `Card` wrappers.
- Let imagery, custom paint, texture, maps, timelines, or charts serve the world.

Anti-slop failure:

- Generic Material scaffold with nice colors but no product identity.
- Same cards, buttons, and icons reused across unrelated app categories.

### Emotional stance toward the user

Every app has a posture. It can be calming, encouraging, precise, playful, protective, cinematic, direct, or quietly competent. Decide the stance and make copy, color, states, motion, and data hierarchy support it.

Flutter implication:

- Empty and error states must speak in the same emotional register as the main screen.
- Health, journaling, and productivity apps should avoid shame-driven or fake-motivational language unless the product intentionally wants it.
- Interaction timing matters: soft transitions can reassure; crisp transitions can convey control.

Anti-slop failure:

- One-size-fits-all "You're all set!" tone.
- Fitness screens that punish the user with aggressive red warnings and streak pressure.

### Material is substrate, not identity

Material and Cupertino provide reliable components, patterns, accessibility, and platform expectations. They should not be the entire art direction unless the brief explicitly asks for plain platform-native UI.

Flutter implication:

- Use `ThemeData`, `ColorScheme`, component themes, and custom wrappers.
- Compose platform patterns into the product world.
- Keep platform affordances believable while making surfaces, typography, and motion ownable.

Anti-slop failure:

- Default `AppBar`, `FloatingActionButton`, `Card`, and `ListTile` with only accent-color changes.

### Controlled richness beats forced minimalism

Clean does not mean empty. Rich imagery, texture, custom paint, motion, and illustration are allowed when they improve meaning and remain readable.

Flutter implication:

- Use layered `Stack`s, `CustomPainter`, masks, gradients, image frames, particles, or parallax only when they communicate hierarchy, story, or feedback.
- Use `RepaintBoundary`, reduced-motion alternatives, and profiling awareness for heavy visuals.
- Keep text legible and touch targets practical.

Anti-slop failure:

- Blank white screens with one nice font.
- Decorative blobs, glass cards, or particles with no reason.

### Flow logic is part of taste

A screen set should read as a believable journey. Screen order, navigation, data carry-forward, and state transitions should make sense.

Flutter implication:

- Pick a navigation model early: tab-first, stack/detail, sheet-led, carousel-led, map-led, timeline-led, or creation-flow.
- Use `go_router` or the existing router to encode the real flow.
- Test journeys, not only static screens.

Anti-slop failure:

- Random "home, stats, profile" screens that look consistent but do not form a product.

### Humane data design

Numbers should help the user understand and act. They should not exist just to make a screen look sophisticated.

Flutter implication:

- Use charts sparingly and explain what matters.
- Prefer clear trend ranges, status summaries, and action guidance over fake precision.
- Label mock values as mock or sample when real data does not exist.

Anti-slop failure:

- Random finance or health dashboards with meaningless charts, percentages, and progress rings.

### Asset language matters

Visual assets are not decoration after code. They are part of the product system.

Flutter implication:

- Plan image ratios, crop behavior, texture intensity, icon treatment, and illustration rules.
- Use generated or provided assets when they materially improve the app.
- Keep assets consistent across screens.

Anti-slop failure:

- One beautiful hero image, then generic placeholder thumbnails everywhere else.
- Mixed icon styles and random decorative stickers.

### Screenshot QA is a design requirement

Visual quality cannot be claimed from code alone.

Flutter implication:

- Use widget previews, simulator/device screenshots, golden tests, or screenshot inspection for visual work.
- Check small phone, large phone, long text, empty/error/loading states, and reduced motion where relevant.
- Fix visible clipping, overflow, weak contrast, cramped spacing, and inconsistent surfaces.

Anti-slop failure:

- Passing `flutter analyze` while the UI still looks broken.

## Reference-Inspired Lessons

### Wonderous

Lesson: An app can create an immersive authored world through custom illustration layers, typography, texture, route transitions, timelines, artifacts, maps, and content-specific UI.

Reusable rule:

- For culture, education, travel, editorial, or exploration apps, define a world-building layer before screen widgets.
- Give each major surface a role in the world: map, artifact, timeline, field note, gallery, ritual, collection, or discovery.

Avoid copying:

- Do not make every immersive app a Wonderous-style ancient-world museum. Copy the commitment to world-building, not the subject matter.

### Reflectly

Lesson: A simple journaling app can feel emotionally specific through pacing, soft guidance, personal prompts, and warmth.

Reusable rule:

- For journaling, mental health, reflection, and onboarding flows, prioritize emotional safety, breathing room, gentle prompts, and state design that does not judge the user.

Avoid copying:

- Do not assume all emotional apps need pastel gradients. The stance matters more than the palette.

## Apple Design Awards 2025 Reference Lessons

### CapWords (Delight & Fun)

Lesson: A language-learning app can transform everyday objects into interactive stickers through camera + animation + sound. Each flashcard transition is meaningful.

Reusable rule:

- For apps that need to recognize real-world objects: use camera, haptics, and sound for layered animation
- Make learning feel like discovery: snap, animate, reveal, narrate
- Avoid copying CapWords's educational content — copy its transformation approach

### Speechify (Inclusivity)

Lesson: A text-to-speech app can be approachable UI while serving diverse accessibility needs: Dyslexia, ADHD, low vision, auditory learning.

Reusable rule:

- Design for the widest user base: voice commands, dynamic type, VoiceOver, hundreds of languages
- Make comprehension clear across cognitive styles: layout hierarchy, focus order, announce state changes
- Avoid copying Speechify's voice capabilities — copy its accessibility-first approach

### Denims (Interaction)

Lesson: Playlist art can be the driving UI metaphor through mesh gradients, smooth scroll, haptics, depth effects, intelligent cropping.

Reusable rule:

- Use texture and depth to anchor brand identity in the UI
- Make interactions tactile: haptics confirm, scroll flows naturally
- Avoid copying Denim's gradient aesthetic — copy its texture-as-interaction approach

### Play (Innovation)

Lesson: A sophisticated prototyping tool can feel approachable with clean, powerful UI, real-time sync, and integration bridges.

Reusable rule:

- Build interfaces that scale: clean navigation, powerful features, seamless export
- Make collaboration visible: real-time sync, shared views, quick feedback loops
- Avoid copying Play's prototyping domain — copy its collaboration UX patterns

### Taobao (Spatial 3D)

Lesson: Shopping for physical items can benefit from 3D models that match real counterparts, spatial comparison, and immersive placement.

Reusable rule:

- Use 3D models for products with form-critical visual properties (shape, fit, texture)
- Enable spatial comparison and placement in the context of the user
- Avoid copying Taobao's e-commerce domain — copy its spatial interaction patterns

### Moises (AI Simplicity)

Lesson: Pro audio editing can feel approachable when AI is visible, controllable, and explainable, not magical.

Reusable rule:

- Show users what the AI did, not just the result: visualizations, process indicators, reversible controls
- Make AI transparent: explain choices, provide controls, enable overrides
- Avoid copying Moises's audio editing — copy its AI transparency patterns

### iA Writer (Distraction-Free Focus)

Lesson: Writing can be separated from interruption through custom keyboard, selective highlighting, iCloud sync, and intuitive gestures.

Reusable rule:

- Remove distractions: fullscreen, keyboard customization, full-text editing
- Make navigation smooth: swipe-right library, swipe-left preview, haptic feedback
- Avoid copying iA Writer's functionality — copy its focus-first patterns

### Feather (3D Drawing)

Lesson: Transforming 2D designs into 3D masterpieces can be approachable with touch/Pencil-native gestures, progressive disclosure, and accessible depth controls.

Reusable rule:

- Use native gestures for native tools: touch for basic, Apple Pencil for precision, layer controls for complexity
- Make complex features discoverable through progressive disclosure
- Avoid copying Feather's drawing domain — copy its touch-first approach

### Watch Duty: Wildfire Maps (Social Impact)

Lesson: Volunteer-run emergency alerts can be critical, reliable, and accessible when built for speed, clarity, and community trust.

Reusable rule:

- Prioritize critical information: maps, alerts, sources, real-time updates
- Make it easy for volunteers and users: simple controls, clear feedback loops, minimal friction
- Avoid copying Watch Duty's domain — copy its crisis communication patterns

### Neva (Social Impact Game)

Lesson: Storytelling within a decaying world can feel meaningful through unique art, intuitive controls, and emotional narrative.

Reusable rule:

- Use art style to convey world-building and narrative tone
- Keep controls simple and intuitive: drag to move, tap to interact, inventory for items
- Avoid copying Neva's story — copy its art-driven game design

### Infinity Nikki (Visuals & Graphics)

Lesson: Dress-up games can stand out through premium visuals, high art standards, and fluid interaction.

Reusable rule:

- Focus on visual excellence: high-resolution textures, smooth transitions, brand-consistent art direction
- Make inventory and selection intuitive: drag-and-drop, layering, strong visual feedback
- Avoid copying Infinity Nikki's gameplay — copy its visual excellence approach

### Gentler Streak

Lesson: Health metrics can be humane, encouraging, and recovery-aware instead of punitive.

Reusable rule:

- For health and fitness apps, design data as coaching. Show readiness, range, recovery, and context before streak pressure.

Avoid copying:

- Do not add a mascot just because a reference has one. Use illustration only when it supports the emotional stance.

### Flighty

Lesson: A stressful utility can feel calm by making complex information glanceable, timely, and obvious.

Reusable rule:

- For travel, logistics, delivery, finance, or operations apps, reduce cognitive load with status hierarchy, timelines, alerts, and one-hand actions.

Avoid copying:

- Do not decorate complexity. Prioritize the next useful fact.

### Halide

Lesson: Dense pro tools can feel premium when controls have clear modes, tactile feedback, and a disciplined active-state language.

Reusable rule:

- For camera, creative, developer, or expert tools, allow density but enforce mode clarity, consistent active states, and ergonomic control placement.

Avoid copying:

- Do not mimic camera dials unless the product actually has expert controls.

### Not Boring Habits

Lesson: A familiar category can become memorable through a strong metaphor, playful interaction, haptics, and reward moments.

Reusable rule:

- For habits, learning, finance, chores, or utilities, choose one metaphor and let interaction carry personality.

Avoid copying:

- Do not gamify everything. Use reward only when it reinforces the user's goal.

### Any Distance

Lesson: Apps can produce beautiful artifacts users want to share, not only screens they operate.

Reusable rule:

- For fitness, social, travel, creative, or journaling apps, consider the user's output artifact: route card, reflection card, progress snapshot, receipt, poster, or share image.

Avoid copying:

- Do not add share cards without a reason users would be proud to share them.

### Rooms

Lesson: A coherent world can be quirky, playful, and tactile while still being understandable.

Reusable rule:

- For social, creative, game-like, or community apps, make the visual rules clear: pixel, clay, paper, sticker, object, terminal, map, or toybox.

Avoid copying:

- Do not use retro pixels as a default personality shortcut.

### Lyft

Lesson: Strong brand color and platform patterns can coexist when accessibility and interaction structure are solved.

Reusable rule:

- For service, transport, marketplace, and booking apps, use familiar mobile patterns such as bottom sheets and map/status layers, then brand them through color, motion, and copy.

Avoid copying:

- Do not let loud color destroy contrast or state clarity.

### Airbnb

Lesson: Complex flows can become calmer when decomposed into focused mobile steps.

Reusable rule:

- For booking, checkout, onboarding, onboarding surveys, and configuration flows, avoid one giant form. Break the journey into clear, reversible, low-cognitive-load steps.

Avoid copying:

- Do not split flows just to look modern. Split only when each step becomes easier.

### Superlist

Lesson: Productivity can be warm and branded while remaining practical.

Reusable rule:

- For productivity tools, prioritize task hierarchy, collaboration state, keyboard/touch efficiency, and a memorable but restrained brand rhythm.

Avoid copying:

- Do not turn practical work surfaces into decorative posters.

### Rive

Lesson: For creative tools, motion and interaction are product material, not garnish.

Reusable rule:

- For animation, design, creative, and media apps, design the canvas/control relationship first. Keep previews live, controls tactile, and animation testable.

Avoid copying:

- Do not add motion that cannot be edited, understood, or disabled.

## Category Defaults

### Culture / education / travel

- Product world: archive, journey, museum, field note, map, timeline, collection.
- Use: imagery, layered motion, artifacts, contextual navigation.
- Avoid: generic lesson cards and empty quizzes.

### Journaling / emotional wellness

- Product world: private room, soft guide, diary, companion, ritual.
- Use: gentle prompts, calm transitions, nonjudgmental copy, soft empty states.
- Avoid: fake positivity, cluttered mood chips, pressure streaks.

### Health / fitness

- Product world: humane coach, recovery guide, progress companion.
- Use: readable metrics, trend ranges, encouragement, rest states.
- Avoid: shame language, aggressive red states, fake chart spam.

### Productivity / tools

- Product world: workbench, command center, notebook, calm cockpit.
- Use: density with hierarchy, keyboard/touch efficiency, clear states.
- Avoid: decorative dashboards and meaningless status dots.

### Finance

- Product world: trusted ledger, calm advisor, secure wallet.
- Use: clear balances, transaction clarity, risk/status language.
- Avoid: random gradient cards, fake stock charts, "next-gen finance" copy.

### Commerce

- Product world: shop floor, catalog, fitting room, collector shelf.
- Use: stable product imagery, clear browse/detail/cart flow, tactile product cards.
- Avoid: generic product grids without brand or material presence.

### Social / community

- Product world: room, club, circle, feed, shared canvas.
- Use: identity, creation flow, media rhythm, clear privacy states.
- Avoid: cloned feeds, meaningless avatars, random reaction pills.
