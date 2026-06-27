---
name: flutter-art-direction
description: Agent-agnostic Flutter art-direction skill for designing and implementing authored, app-native, anti-slop mobile app screens and flows. Use for new Flutter apps or screens where visual quality, emotional intent, product-world specificity, motion, assets, adaptive layout, and screenshot/preview QA matter. Complements official Flutter architecture, responsive layout, routing, localization, networking, widget preview, widget test, and integration test guidance instead of replacing it.
---

# Flutter Art Direction

## Overview

Use this skill to make Flutter UI feel authored rather than AI-generated. The goal is not to copy reference apps; extract reusable principles from excellent mobile products, then create a product-specific Flutter design system, screen flow, and implementation plan that fits the user's brief.

This skill is mobile-first by default. Material and Cupertino are implementation substrates, not the whole identity.

## Workflow

### 1. Read the brief

Before writing code, infer:

- app category and primary user
- platform mode: `iOS-native premium`, `Android-native premium`, or `cross-platform premium neutral`
- product world: the visual universe the app belongs to
- emotional stance: how the app should make the user feel
- reference signals: apps, screenshots, brands, or user taste words
- quiet constraints: accessibility, trust, health, safety, kids, public-sector, or regulated domains

Output one line before implementation:

`Flutter Design Read: <app category> for <audience>, <platform mode>, with a <product world> visual language and a <emotional stance> toward the user.`

Ask one clarifying question only when the design read can split into meaningfully different directions.

### 2. Lock the Design Bible

Before building screens, lock these choices and keep them consistent:

- platform mode and navigation model
- product world and emotional stance
- palette logic, including background family and accent use
- typography mood and type scale rhythm
- spacing, density, and touch-target rhythm
- shape/corner-radius logic
- icon style and illustration/custom-paint language
- imagery, texture, and asset strategy
- motion language and reduced-motion fallback
- state design: loading, empty, error, permission, selected, pressed, long-text
- QA method: widget preview, screenshot, simulator/device, or visual test

For deeper inspiration, read `references/principle-bank.md` when the brief is visual, emotional, immersive, health/wellness, productivity, finance, education, culture, commerce, social, or travel.

### 3. Set the dials

Use these values as design constraints, not decorative labels:

- `ART_DIRECTION`: 1 = plain utility, 10 = highly authored world
- `PLATFORM_AWARENESS`: 1 = generic mobile, 10 = strongly app-native
- `FLOW_LOGIC`: 1 = isolated screens, 10 = believable user journey
- `MOTION_INTENSITY`: 1 = static, 10 = cinematic/physics-led
- `VISUAL_DENSITY`: 1 = airy, 10 = dense/operational
- `NON_GENERICITY`: 1 = familiar template, 10 = distinct product identity

Default for creative consumer apps: `8 / 9 / 8 / 6 / 4 / 9`.
Default for trust-heavy apps: `5 / 10 / 9 / 3 / 5 / 7`.
Default for practical tools: `6 / 9 / 9 / 4 / 6 / 8`.

If motion cannot be implemented and verified in scope, lower `MOTION_INTENSITY` and ship a polished static interaction rather than broken animation.

### 4. Use Flutter architecture without losing the art

Complement official Flutter guidance instead of duplicating it:

- For structure, use layered architecture: data, domain when useful, UI, feature folders, ViewModels/Listenable state where needed.
- Add an art layer under UI: theme/tokens, typography, motion, assets, reusable components, and screen worlds.
- Use `LayoutBuilder`, `MediaQuery.sizeOf(context)`, constraints, and max widths. Never infer layout from phone/tablet labels alone.
- Use `go_router` or the existing router for real navigation. The navigation model must match the Design Bible.
- Use localization-safe copy and layouts. Do not design only for short English labels.
- Use strongly typed models and repositories when data/API work exists.

Suggested structure for new apps:

```text
lib/
  data/
  domain/
  ui/
    core/
      theme/
      typography/
      motion/
      assets/
      widgets/
    features/
      feature_name/
        view_models/
        views/
        widgets/
```

### 5. Use image concepts selectively

Image concepts are optional, not mandatory. Use them when the app is highly visual, immersive, brand-led, editorial, consumer, cultural, wellness, education, travel, commerce, social, or otherwise likely to benefit from visual source-of-truth before coding.

When using image concepts:

- generate fresh, readable screen concepts rather than tiny multi-screen collages
- keep the Design Bible consistent across all screens
- analyze the image for palette, type, spacing, navigation, assets, and motion implication
- translate into Flutter widgets, theme tokens, assets, and screen states
- verify the Flutter result with screenshots or previews

Skip image concepts for small utilitarian changes, bug fixes, or existing UI systems where the visual language is already fixed.

## Flutter Anti-Slop Rules

### App-native screens

- Respect safe areas, status regions, bottom navigation/home-indicator regions, and gesture zones.
- Do not build website heroes inside phone screens.
- Use tab bars, navigation stacks, sheets, segmented controls, carousels, timelines, maps, or custom interactions when the product flow calls for them.
- Keep first screens calm, readable, and focused.

### Product-world specificity

- Name widgets and interactions after the product experience, not generic layout nouns.
- Prefer `ReflectionPromptCard`, `RecoveryRangeChart`, `ArtifactTimeline`, or `TripStatusSheet` over `HomeCard`, `InfoBox`, or `FeatureTile`.
- Make assets, illustrations, icons, and motion belong to one world.
- Use custom paint, layered images, texture, particles, masks, or motion when they communicate the product world and can be maintained.

### Controlled richness

Cleanliness is the goal, not forced minimalism. A screen may be rich, image-led, animated, textured, or layered if it remains readable, touch-friendly, and structurally clear.

Use richness for:

- storytelling and onboarding
- culture, education, travel, lifestyle, social, wellness, commerce, or creative tools
- emotional stance and memorable product identity
- data explanation, not data decoration

Avoid richness when it becomes:

- nested-card clutter
- random glass effects
- decorative pills and labels
- fake chart dashboards
- unreadable small text
- motion without purpose

### Common AI tells to remove

- default purple-blue gradients unless the brand explicitly justifies them
- fake dashboard chart spam
- repeated onboarding slides with only icon/headline changes
- too many pills, badges, chips, or tiny labels
- generic line-icon language with no product specificity
- nested cards inside cards
- random glassmorphism
- generic fintech/wellness/productivity templates
- placeholder names like Acme, Nova, Flow, Nexus, or Smart
- copy such as "elevate", "unlock", "seamless", "next-gen", "transform your life"
- fake-precise metrics without real data or mock labeling

## Visual QA Gate

Before delivery, verify every relevant item. If one fails, fix before final output.

- Design Read declared.
- Design Bible locked and visible in implementation choices.
- Dials chosen and reflected in the UI.
- Screen feels app-native, not web-in-phone.
- Product world is specific and not copied from a reference app.
- Emotional stance is reflected in copy, state design, color, motion, and hierarchy.
- Material/Cupertino components are themed or composed into the product identity.
- Safe areas, status region, bottom region, and gestures are respected.
- Text is comfortably readable on small phones.
- Touch targets are practical, generally 44-48 logical pixels or larger for primary controls.
- Layout adapts with constraints, not device-name guesses.
- No overflow stripes, clipped text, unbounded scrollables, or unstable layout.
- Loading, empty, error, permission, selected, pressed, and long-text states are present where relevant.
- Motion is motivated by hierarchy, storytelling, feedback, or state transition.
- Reduced-motion fallback exists for strong motion.
- Palette, type, icon, radius, spacing, and surface logic remain consistent.
- Screens in a flow vary in composition without drifting into another design system.
- Any visual assets are purposeful, correctly framed, and consistent.
- Widget previews, screenshots, simulator/device checks, or visual tests were used for visual work.

## Example Responses

### Cultural learning app

`Flutter Design Read: immersive culture app for curious learners, cross-platform premium neutral, with a museum-field-notes product world and a calm sense of discovery.`

Use layered imagery, textured backgrounds, artifact-specific navigation, timeline/detail flow, and motion that reveals content like exploration.

### Journaling app

`Flutter Design Read: private journaling app for emotionally overloaded users, iOS-native premium, with a soft guided-reflection world and a reassuring emotional stance.`

Use calm onboarding, readable prompts, soft transitions, careful empty states, and visual warmth without fake positivity.

### Fitness or health app

`Flutter Design Read: health tracking app for everyday users, cross-platform premium neutral, with a humane coaching world and a non-punitive stance toward data.`

Use approachable metrics, recovery-aware states, clear charts, encouraging microcopy, and no shame-driven streak pressure.
