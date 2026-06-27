# Flutter Implementation Playbook

Use this reference after the Design Read and Design Bible are set. It translates art direction into concrete Flutter implementation choices without replacing official Flutter architecture, layout, preview, testing, routing, localization, or networking guidance.

## Contents

- [Design Bible to Code](#design-bible-to-code)
- [Theme and Tokens](#theme-and-tokens)
- [Screen Architecture](#screen-architecture)
- [Motion](#motion)
- [Assets and Custom Visuals](#assets-and-custom-visuals)
- [Adaptive Layout](#adaptive-layout)
- [Preview and Screenshot QA](#preview-and-screenshot-qa)
- [Implementation Checklists](#implementation-checklists)

## Design Bible to Code

Translate each Design Bible decision into a concrete file, class, or widget family.

| Design Bible choice | Flutter implementation |
|---|---|
| Platform mode | `MaterialApp`, `CupertinoApp`, adaptive wrappers, platform-specific navigation affordances |
| Product world | Feature names, asset folders, custom components, screen metaphors |
| Emotional stance | Copy tone, state design, animation timing, empty/error screens |
| Palette logic | `ColorScheme`, custom color extensions, semantic tokens |
| Typography mood | `TextTheme`, app text styles, font assets, line-height rules |
| Spacing and density | spacing constants, max widths, touch target rules |
| Shape logic | radius tokens and component themes |
| Icon style | one icon family or one custom asset style |
| Imagery and texture | asset manifest, image wrappers, crop ratios, custom painters |
| Motion language | durations, curves, transition components, reduced-motion path |
| Navigation model | `go_router`, shell routes, tab state, sheet routes, detail stacks |
| State design | loading, empty, error, permission, selected, pressed, long-text widgets |
| QA method | previews, screenshots, golden tests, widget tests, integration flows |

Do not leave a Design Bible item as prose only. If it matters visually, encode it.

## Theme and Tokens

Create theme primitives before composing rich screens.

Recommended core files for new apps:

```text
lib/ui/core/theme/app_theme.dart
lib/ui/core/theme/app_colors.dart
lib/ui/core/theme/app_spacing.dart
lib/ui/core/theme/app_radii.dart
lib/ui/core/typography/app_text_styles.dart
lib/ui/core/motion/app_motion.dart
lib/ui/core/assets/app_assets.dart
```

Use semantic names:

- `surfaceBase`, `surfaceRaised`, `surfaceMuted`, `accent`, `accentSoft`, `danger`, `success`
- `spaceXs`, `spaceSm`, `spaceMd`, `spaceLg`, `spaceXl`
- `radiusSm`, `radiusMd`, `radiusLg`, `radiusPill`
- `motionFast`, `motionMedium`, `motionSlow`

Avoid:

- raw color literals scattered through widgets
- unrelated radius values on every component
- one-off animation durations
- component names like `PrettyCard` or `FancyButton`

## Screen Architecture

Keep visual richness maintainable by separating roles.

Recommended feature layout:

```text
lib/ui/features/reflection/
  view_models/
    reflection_view_model.dart
  views/
    reflection_screen.dart
  widgets/
    reflection_prompt_card.dart
    mood_rhythm_picker.dart
    reflection_empty_state.dart
```

Rules:

- Views own layout, safe areas, navigation surfaces, and composition.
- ViewModels own UI state, commands, and state transitions.
- Widgets own reusable product-specific pieces.
- Theme/core files own shared visual language.
- Data/repository files own real data and mock/sample data boundaries.

Use product-specific widget names. A good name explains the app world:

- good: `ArtifactTimeline`, `RecoveryRangeChart`, `ReflectionPromptCard`, `FlightStatusSheet`
- weak: `InfoCard`, `CustomCard`, `HomeTile`, `StatsWidget`

## Motion

Motion must communicate hierarchy, storytelling, feedback, or state transition.

Use Flutter primitives first:

- `AnimatedSwitcher` for state replacement
- `AnimatedContainer` for simple property transitions
- `TweenAnimationBuilder` for local animated values
- `AnimationController` for coordinated screen motion
- `Hero` for meaningful shared elements
- `PageRouteBuilder` or router transitions for route-level personality

Use packages only when they already exist or clearly justify themselves:

- `flutter_animate` for expressive chained effects
- `rive` for authored vector animation systems
- `lottie` for provided motion assets

Always provide a reduced-motion path for strong motion:

- use shorter durations, opacity-only fades, or static end states
- do not make content unreachable when animation is disabled
- avoid infinite loops unless they communicate live status or gentle ambience

Avoid:

- perpetual shimmer, pulse, float, or carousel motion on static information
- route transitions that hide where the user went
- physics that feels playful in a trust-heavy app
- animation implemented with repeated `setState` on every frame when an `AnimationController` or builder would isolate updates

## Assets and Custom Visuals

Asset work is part of the art direction.

Create folders by product world, not by random screen:

```text
assets/images/common/
assets/images/reflection/
assets/images/recovery/
assets/images/artifacts/
assets/textures/
assets/icons/
```

Use stable media rules:

- define repeatable aspect ratios for image cards, headers, thumbnails, and share artifacts
- protect text over images with scrims, fades, or masks
- avoid mixing photo, 3D, line-art, and sticker styles unless the system defines why
- use `RepaintBoundary` around heavy custom paint, image stacks, and animated effects
- compress and size assets for mobile screens

Custom paint is appropriate for:

- charts with product-specific meaning
- timelines, maps, guides, range bands, or progress metaphors
- subtle texture, masks, or illustration pieces

Custom paint is not appropriate for:

- icons that should come from an asset or icon family
- decorative noise that makes text harder to read
- complex visuals that cannot be maintained or tested

## Adaptive Layout

Design for constraints, not device names.

Use:

- `LayoutBuilder` for parent constraints
- `MediaQuery.sizeOf(context)` for app window size
- `SafeArea` or explicit safe-area padding where content touches system regions
- `ConstrainedBox` for max content width on tablets and desktop
- `SliverList`, `SliverGrid`, and `CustomScrollView` for rich scroll surfaces

Check:

- small phone width
- large phone width
- tablet or wide layout if supported
- landscape if the app can rotate
- long localized text
- large text scale when accessibility matters

Avoid:

- hard-coding layout from "phone" or "tablet"
- top-level `OrientationBuilder` as the main layout switch
- scrollables inside unconstrained columns
- important content under bottom navigation or home indicators
- tiny decorative labels that fail under text scaling

## Preview and Screenshot QA

Visual QA is mandatory for visual work.

Preferred order:

1. Add widget previews when the project supports Flutter widget previews.
2. Run the app or preview and capture screenshots for target states.
3. Inspect screenshots for safe areas, text scale, spacing, contrast, and AI tells.
4. Add widget tests or golden tests when behavior or visuals are stable enough.
5. Add integration tests for important flows.

Preview scenarios to create when relevant:

- default state
- loading state
- empty state
- error state
- permission denied state
- long text state
- selected and pressed states
- light and dark modes when supported
- small phone and large phone constraints

Screenshot acceptance:

- no overflow stripes
- no clipped text
- no unreadably small copy
- no critical controls in unsafe regions
- no nested-card clutter
- no copied reference-app styling
- no generic AI tells from `SKILL.md`
- main flow is understandable from the first view

## Implementation Checklists

### New screen

- Declare the Flutter Design Read.
- Lock the Design Bible.
- Read the principle bank if the app is visual, emotional, immersive, or category-specific.
- Map the Design Bible into theme, motion, assets, navigation, and state widgets.
- Build with constraints and safe areas from the start.
- Add or update previews for key states.
- Capture or inspect screenshots.
- Run `flutter analyze` and relevant tests.
- Fix every Visual QA Gate failure before final delivery.

### Existing app screen

- Identify current architecture, theme, navigation, and state patterns.
- Preserve existing project conventions unless they directly cause visual or UX failure.
- Add art-direction structure only where it reduces repetition or clarifies the system.
- Do not migrate state management or routing just for taste work.
- Improve the screen in focused passes: hierarchy, palette, type, spacing, states, motion, assets, QA.

### Highly visual app

- Consider image concepts first.
- Define asset language and media frame rules.
- Use product-world widget names.
- Build custom visuals as reusable pieces.
- Use reduced-motion paths and `RepaintBoundary`.
- Verify with screenshots on real mobile proportions.
