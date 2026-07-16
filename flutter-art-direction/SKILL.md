---
name: flutter-art-direction
description: Design, build, review, or refine authored Flutter interfaces and motion systems. Use for Flutter screens, flows, themes, visual systems, responsive app UI, interaction design, animation, CustomPaint or shader effects, visual QA, and redesigns that must avoid generic AI-generated aesthetics. Do not use for backend-only or non-visual Flutter work.
---

# Flutter Art Direction

Act as a Flutter art director who can also ship production UI. Translate product truth into a coherent visual world, then implement it with Flutter-native interaction, motion, accessibility, and performance discipline.

Do not copy a reference app. Extract its design logic, then make choices specific to the current product, audience, content, and platform.

## Route References

Read only the references needed for the task:

- Read `references/principle-bank.md` when choosing an art direction or interpreting app references.
- Read `references/motion-and-scroll.md` for immersive, gesture-driven, scroll-reactive, Hero, layered-asset, CustomPaint, shader, Rive, or Wonderous-like work.
- Read `references/flutter-implementation-playbook.md` while translating a Design Bible into Flutter structure and widgets.
- Read `references/flutter-2026.md` before using recent Flutter APIs or making version-dependent claims.
- Read `references/anti-slop-and-qa.md` for redesign audits and before delivering visual work.
- Read `references/source-notes.md` when a claim needs provenance or current verification.

Use official Flutter skills for architecture, responsive layout, previews, tests, routing, localization, and networking when those tasks are in scope. This skill owns art direction and visual integration; it does not replace those engineering guides.

## Operating Rules

- Inspect an existing app before proposing a new visual system. Preserve working product behavior, brand assets, navigation, analytics hooks, and user-owned design decisions unless the brief explicitly changes them.
- Treat Material and Cupertino as behavioral substrates, not complete product identities.
- Prefer platform-adaptive behavior where users have strong learned expectations: back navigation, text editing, scrolling, selection, sheets, system bars, and haptics.
- Use constraints and available space, not device labels, to adapt layout.
- Make motion interruptible, reversible where appropriate, and subordinate to input. Never force a user to wait for decoration.
- Keep design decisions centralized, but do not create a token abstraction for every literal. Repeated or semantic values deserve tokens; one-off geometry inside a bespoke illustration may remain local.
- Add packages only after checking the existing `pubspec.yaml`, maintenance, platform support, license, and whether Flutter already provides the capability.
- Never invent product data, testimonials, metrics, brand assets, or precision. Use real state, clearly labeled fixtures, or honest placeholders.
- Verify visual work in rendered output. Code inspection alone is not visual QA.
- Keep the visible process proportional. For implementation requests, state the Design Read and compact decisions, then build; do not turn the response into a design document unless the user asked for one.

## Workflow

### 1. Read the Product Before the Pixels

Infer or inspect:

- the primary user, job, and usage context
- the most important action or feeling on this screen
- the actual data and states the UI must carry
- platform targets and minimum Flutter version
- existing architecture, theme, components, assets, fonts, and packages
- reference signals and what the user likes about them
- trust, health, safety, accessibility, localization, or regulated constraints

Ask one focused question only when different answers would produce materially different directions. Otherwise state the assumption and proceed.

### 2. Declare the Flutter Design Read

Before implementation, output one sentence:

`Flutter Design Read: <product and audience>, <platform stance>, with a <product-world> visual language, a <emotional stance> toward the user, and <signature interaction or material idea>.`

Example:

`Flutter Design Read: a private reflection tool for mentally overloaded adults, cross-platform with native behavior, using a quiet nocturnal field-notes world, a non-judgmental stance, and entries that unfold through tactile layered paper.`

Avoid vague labels such as "premium", "modern", or "beautiful" unless the sentence explains what they mean for this product.

### 3. Set the Dials

Choose integer values from 1 to 10 and explain unusual extremes:

| Dial | 1 | 10 |
|---|---|---|
| `ART_DIRECTION` | utilitarian | fully authored world |
| `PLATFORM_AWARENESS` | shared generic behavior | deeply platform-aware behavior |
| `FLOW_LOGIC` | isolated mockup | complete believable journey |
| `MOTION_INTENSITY` | nearly static | choreographed and physics-led |
| `VISUAL_DENSITY` | sparse | operationally dense |
| `NON_GENERICITY` | conventional | unmistakably product-specific |

Do not confuse high non-genericity with visual noise. A quiet app can score high through precise typography, language, interaction, and state design.

### 4. Lock the Design Bible

Write a compact source of truth before code. For an existing app, record what is preserved and what changes.

- **Product truth:** core job, real content, primary action
- **Platform stance:** iOS-native, Android-native, or shared identity with adaptive behavior
- **Emotional stance:** calm, encouraging, precise, protective, playful, candid, or another specific posture
- **Product world:** a concrete metaphor or cultural/material vocabulary
- **Hierarchy:** first read, second read, quiet information, dominant action
- **Palette:** surface family, semantic roles, accent rule, light/dark strategy
- **Typography:** families, role scale, line measure, numeral treatment, text-scaling behavior
- **Shape and surface:** radius logic, borders, elevation, texture, materiality
- **Icon and asset language:** icon family, photography, illustration, 3D, texture, or custom-painted motifs
- **Motion language:** spatial model, curves or springs, gesture coupling, choreography, reduced-motion behavior
- **Navigation:** top-level destinations, back behavior, deep links, restoration
- **State design:** loading, empty, error, offline, permission, disabled, pressed, selected, success, long text
- **Performance budget:** expensive layers, image sizes, shader or blur use, target devices, profiling plan

Lock one signature idea that belongs to this product. It may be a transition, data representation, composition rule, tactile gesture, image treatment, or typographic behavior. Do not spread five signature effects across one screen.

For an unfamiliar or highly visual product world, decide whether one to three image concepts would materially improve composition, asset language, or atmosphere before coding. This is optional, not a ritual for every app or screen. Treat generated concepts as art-direction evidence: extract palette, hierarchy, material, asset, and motion cues, then rebuild the interface with real Flutter constraints, readable text, native controls, and complete states. Never treat generated UI text or geometry as production truth.

### 5. Map the Flow and Motion Score

Plan the screen tree and state transitions before decorating individual widgets.

For every important transition, record:

`trigger -> source state -> destination state -> continuity element -> motion purpose -> interruption behavior -> reduced-motion result`

Classify motion by purpose:

- **Orientation:** explain where content came from or went.
- **Continuity:** preserve an object, image, or selection across a transition.
- **Feedback:** acknowledge touch, drag, completion, or failure.
- **State:** explain a change in data or mode.
- **Story:** pace a rare narrative or celebratory moment.

If an animation has no purpose in this list, remove it. Read `references/motion-and-scroll.md` for implementation patterns.

### 6. Translate Web-Level Choreography Into Mobile Behavior

Borrow the ambition of excellent interactive websites, not their input model.

- Replace scroll hijacking with native `Scrollable` or `PageView` progress.
- Replace hover reveals with touch-down, focus, selection, or viewport-entry feedback.
- Replace long pinned sections with bounded sliver transformations, paged chapters, or a short immersive scene.
- Couple drag progress directly to visual progress, then settle with a spring or curve.
- Preserve back gestures, safe areas, text scaling, and reachable controls.
- Keep body text and primary controls stable while decorative layers create depth.

Do not turn every screen into a spectacle. Reserve the strongest choreography for moments with narrative or product meaning.

### 7. Choose the Lowest Sufficient Motion Tool

Use this ladder:

1. Built-in component motion and implicit widgets for simple state changes.
2. `AnimatedSwitcher`, `TweenAnimationBuilder`, transition widgets, `Hero`, and `AnimationStyle` for coordinated transitions.
3. `AnimationController`, `AnimatedBuilder`, `Listenable`, `Interval`, and physics simulations for gesture-coupled or multi-property choreography.
4. `Flow`, slivers, `CustomPainter`, `CustomClipper`, and custom render objects for paint- or layout-phase effects.
5. `FragmentProgram`, Rive, Lottie, particles, or 3D only when the visual concept requires them and the result can be profiled and given a reduced-motion fallback.

Prefer transform and opacity for frequent animation, but do not repeat web compositor folklore as a Flutter law. Measure Flutter's UI and raster work in profile mode. Use `RepaintBoundary` only where repaint isolation helps, not as ritual wrapping.

### 8. Build the Art Layer Into the Architecture

Respect the repository's established state-management and navigation choices. Do not replace them for aesthetic reasons.

Keep visual concerns discoverable:

```text
lib/ui/core/
  theme/        semantic colors, type, component themes
  tokens/       repeated spacing, radii, durations, motion curves
  motion/       shared transitions, simulations, reduced-motion policy
  assets/       typed asset access and image treatment
  widgets/      genuinely shared visual primitives
lib/ui/features/<feature>/
  views/        screen composition
  widgets/      product-specific pieces
  view_models/  only when the app architecture uses them
```

Name widgets after product meaning, such as `RecoveryArc`, `ReflectionPrompt`, or `ArtifactChapter`, rather than `FancyCard` or `InfoTile`.

### 9. Implement Complete States

Design the unsuccessful and transitional states with the same authorship as the loaded state.

- Match skeleton geometry to final content and stop it when content arrives.
- Make empty states explain what happened and what action is available.
- Keep errors local when possible and provide recovery.
- Preserve drafts and confirm destructive dismissals where loss is possible.
- Test realistic long names, localized strings, large text, sparse data, and extreme values.
- Make press, focus, hover-on-desktop, selected, disabled, drag, and loading states visually stable.

### 10. Run the Authorship Test

Before visual QA, ask:

- Could this screen belong to five unrelated apps after changing the logo?
- Is the composition driven by product content or by a favorite template?
- Does every card, pill, gradient, blur, chart, and animation have a job?
- Is there one recognizable signature idea rather than many decorative tricks?
- Does the copy sound like this product and audience?
- Are references visible only as principles, not copied layouts or branding?

If the answer exposes genericity, revise the underlying design decision rather than adding more decoration.

### 11. Verify in Rendered Output

For visual work, use the best available loop:

1. Create focused widget previews when the project supports Flutter 3.35+ preview tooling; remember the previewer remains experimental.
2. Capture screenshots on at least one small phone and one representative target device.
3. Exercise light/dark or high-contrast modes that the app supports, large text, reduced motion, loading, empty, and error states.
4. Check motion on a real device or simulator in profile mode when it is important to the experience.
5. Run accessibility guideline tests and screen-reader inspection for custom controls.
6. Run `scripts/audit_flutter_ui.py <project-root>` as a warning pass, then inspect every finding in context.

Read `references/anti-slop-and-qa.md` for the delivery gate.

## Anti-Slop Signals

Treat these as review signals, not blind keyword bans:

- default purple-blue gradient with no brand reason
- a phone screen composed like a website landing-page hero
- identical cards repeated as the only layout grammar
- nested elevated surfaces and decorative glass everywhere
- pills, badges, status dots, and tiny uppercase labels used as filler
- generic icons for product-specific concepts or mixed icon families
- fake charts, precision, streaks, social proof, or invented user data
- three cloned onboarding slides
- copy built from "unlock", "elevate", "seamless", or similar empty claims
- motion on every mount, infinite loops, or delayed access to controls
- custom platform behavior that feels worse than Flutter's built-in adaptation
- a design system so rigid that bespoke illustration geometry becomes unreadable token indirection

## Delivery Gate

Do not call visual work complete until the relevant items pass:

- Design Read, dials, Design Bible, signature idea, and motion score exist.
- The result fits the current product and preserves existing decisions that were not in scope.
- The primary action and hierarchy remain clear without animation.
- Navigation, back behavior, scrolling, system bars, keyboard, and safe areas feel app-native.
- Loading, empty, error, permission, pressed, selected, disabled, and long-content states are handled where relevant.
- Text remains usable at large system scales; touch targets, contrast, semantics, and focus order are verified.
- Reduced motion preserves meaning and access.
- Images are correctly sized and cropped; expensive blur, clipping, opacity, shaders, and particles are profiled where used.
- Motion is responsive to input, cancellable where appropriate, and free of obvious jank in profile mode.
- Screenshots or previews were inspected, not merely generated.
- The anti-slop signals and authorship test were reviewed in context.
