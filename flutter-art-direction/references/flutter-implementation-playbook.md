# Flutter Art Direction Implementation Playbook

Use this reference while turning a Design Bible into code. Adapt it to the repository. Do not replace established architecture, state management, routing, or component conventions without a product or engineering reason.

## Contents

- Existing-app audit
- Design Bible to code
- Theme and tokens
- App-native composition
- Adaptive layout and platform behavior
- Asset systems
- State design
- Motion integration
- Visual verification

## Existing-App Audit

Before editing an existing app, inspect:

- `pubspec.yaml` and SDK constraints
- app entry point and theme construction
- current navigation shell and route transitions
- state-management pattern
- shared component and token locations
- assets, fonts, icon sources, and generation tools
- representative screens and their state models
- tests, previews, goldens, screenshots, and device scripts
- current git status

Record:

- **Preserve:** recognizable brand or behavior that already works
- **Repair:** inconsistent, inaccessible, generic, or brittle patterns
- **Introduce:** the smallest new visual primitives needed by the brief

Do not interpret a visual refresh as permission to rewrite app architecture.

## Design Bible to Code

| Design Bible decision | Flutter location |
|---|---|
| Platform stance | app shell, route builders, adaptive controls, `ScrollBehavior` |
| Palette roles | `ColorScheme`, semantic `ThemeExtension`, component themes |
| Typography | `TextTheme`, bundled fonts, numeral features, text-scale tests |
| Shape and surface | component themes, `ShapeBorder`, border/elevation tokens |
| Spacing and density | a small repeated spacing scale and layout constraints |
| Icon language | one platform or brand family, semantic labels, size tokens |
| Asset language | typed paths, crop/focal rules, placeholders, decode strategy |
| Motion language | motion policy, shared curves/springs, route and state transitions |
| Navigation | existing router, shell, restoration, deep-link behavior |
| Complete states | feature state model and state-specific compositions |
| Signature idea | a product-specific widget, transition, painter, or asset system |

## Theme and Tokens

### Tokenize meaning, not every number

Centralize values when they are:

- repeated across files
- semantic across themes
- part of a component contract
- likely to change as a family
- necessary for consistent motion or spacing

Keep local:

- illustration coordinates
- asset-specific crop values
- math constants inside a painter
- one-off geometry that would become less readable through indirection

### Suggested theme layers

```text
ui/core/theme/
  app_theme.dart
  app_color_roles.dart
  app_text_theme.dart
  app_component_themes.dart
ui/core/tokens/
  app_spacing.dart
  app_radii.dart
  app_motion.dart
```

Use `ThemeExtension` for semantic values not represented by `ColorScheme` or `ThemeData`.

```dart
@immutable
class AppSurfaces extends ThemeExtension<AppSurfaces> {
  const AppSurfaces({
    required this.success,
    required this.warning,
    required this.editorialPaper,
  });

  final Color success;
  final Color warning;
  final Color editorialPaper;

  @override
  AppSurfaces copyWith({
    Color? success,
    Color? warning,
    Color? editorialPaper,
  }) {
    return AppSurfaces(
      success: success ?? this.success,
      warning: warning ?? this.warning,
      editorialPaper: editorialPaper ?? this.editorialPaper,
    );
  }

  @override
  AppSurfaces lerp(covariant AppSurfaces? other, double t) {
    if (other == null) return this;
    return AppSurfaces(
      success: Color.lerp(success, other.success, t)!,
      warning: Color.lerp(warning, other.warning, t)!,
      editorialPaper:
          Color.lerp(editorialPaper, other.editorialPaper, t)!,
    );
  }
}
```

### Shape grammar

Define a reason for each shape family:

- buttons and direct controls
- content containers
- modal or elevated layers
- selected or transforming states
- bespoke product objects

Avoid one universal radius for every component and avoid arbitrary per-widget radii. A small semantic scale is usually enough.

### Typography

- Bundle or load fonts according to project policy and license.
- Define role styles in `TextTheme`; do not hard-code a new type scale in every screen.
- Keep body line length constrained on tablets and desktop windows.
- Use tabular figures for values that update or align in columns.
- Test bold text, large system text, localization, and mixed-script fallback.
- Avoid `FittedBox` as a general cure for overflowing text.

## App-Native Composition

### Start with the shell

Decide:

- top-level destinations
- navigation bar, rail, drawer, tabs, or platform-specific alternative
- safe-area and system-bar behavior
- back and deep-link behavior
- how state and scroll position survive navigation

Then compose feature screens inside that model. Do not put a marketing-site hero and CTA stack inside every phone screen.

### Use content-shaped layouts

Choose based on information:

- `CustomScrollView` and slivers for heterogeneous scroll and collapsing structure
- `ListView.builder` or sliver builders for long collections
- `PageView` or `CarouselView` for discrete chapters or browseable media
- `Stack` for bounded, authored overlap
- `LayoutBuilder` for available-space decisions
- `ConstrainedBox` and centered content for readable large-screen widths
- `Wrap`, grids, or multi-pane composition when width allows

Avoid nested unconstrained scrollables, `shrinkWrap` as a default fix, and layout decisions based only on portrait versus landscape.

### Keep controls reachable

- Place frequent actions in thumb-reachable regions where platform conventions allow.
- Keep drag and system-back gesture regions from fighting.
- Reserve bottom inset for persistent bars and the keyboard.
- Use visible alternatives for custom gestures.
- Keep fixed controls out of display cutouts and system-gesture regions.

## Adaptive Layout and Platform Behavior

Adapt three different things deliberately:

1. **Available space:** layout, pane count, gutters, content width, image crop.
2. **Input capability:** touch, mouse, keyboard, trackpad, stylus.
3. **Platform convention:** route transition, back gesture, text editing, scrolling, haptics, icon idiom.

Use `LayoutBuilder` and `MediaQuery.sizeOf` for layout. Use platform checks only for actual platform policy or convention, not as a proxy for screen size.

Flutter already adapts many behaviors. Preserve that behavior unless the product explicitly needs a shared interaction model and the replacement is tested on every target.

### Edge-to-edge

- Let backgrounds and scrolling media extend under system bars when appropriate.
- Inset text, controls, and drag targets.
- Use `SafeArea` or selected `MediaQuery.paddingOf` values intentionally.
- Avoid applying `SafeArea` around an entire immersive scene if it creates visible dead bands; protect interactive content instead.
- Test Android gesture and three-button navigation plus iOS home-indicator regions.

## Asset Systems

### Build an asset brief

For each required asset, specify:

- content and purpose
- visual style
- aspect ratio and minimum resolution
- focal point and crop behavior
- background and transparency
- light/dark variants
- semantic description
- loading and failure state
- license and provenance

### Layered art

For an immersive scene:

```text
scene/
  background/
  middle/
  foreground/
  overlays/
  texture/
```

Each layer should have a depth role, responsive anchor, and motion range. Do not create parallax from one flattened image unless a simple crop shift is sufficient.

### Image performance

- Decode close to rendered size where practical.
- Preserve aspect ratio and focal point.
- Pre-cache only assets needed soon.
- Keep placeholders structurally stable.
- Avoid giant transparent images for small decorative layers.
- Check memory when several full-screen pages stay alive.
- Verify network errors and slow loading.

### Custom visuals

Use:

- `CustomPaint` for diagrams, paths, procedural motifs, and finite effects
- fragment shaders for bounded GPU effects
- Rive for interactive vector state machines
- Lottie for authored playback assets
- platform views only when the capability requires them

Always preserve semantics and non-animated meaning outside the visual layer.

## State Design

Create compositions for:

- initial/loading
- loaded
- empty
- error and retry
- offline or stale data
- permission before request, denied, and permanently denied
- pressed, focused, hovered, selected, disabled
- destructive confirmation and undo
- long text and localization
- large values, missing values, and partial data

Do not simply center a spinner for every load. The state should preserve the expected hierarchy and layout stability.

### Honest fixtures

When real data is unavailable:

- label fixtures as sample or preview data
- keep values plausible but do not imply product performance
- do not fabricate testimonials, customers, health outcomes, or financial results
- ensure fixture states include failure and edge cases

## Motion Integration

Read `motion-and-scroll.md` for deep patterns.

At implementation time:

- add a central reduced-motion policy
- keep motion parameters near the component or shared motion role they control
- use stable keys for state and Hero continuity
- isolate animated rebuild and repaint scope
- pre-cache imminent signature assets
- dispose controllers and listeners
- preserve actions during transitions
- test reversal, repeated taps, back gestures, and route interruption

Do not add `flutter_animate`, Rive, Lottie, a carousel, or a particle package before proving a built-in widget cannot express the desired result cleanly.

## Visual Verification

### Preview matrix

Create previews or test harness states for:

- small phone
- representative large phone
- tablet or resizable wide window when supported
- light and dark themes
- text scale around 1.0 and a large system scale
- loaded, loading, empty, error
- reduced motion
- long localized content

The Widget Previewer is experimental; keep previews easy to update.

### Screenshot and device pass

Inspect:

- hierarchy at a glance
- content below fixed bars
- safe areas and edge-to-edge backgrounds
- crop and focal point
- text wrap and truncation
- selected, pressed, disabled, and focus visuals
- keyboard appearance and field visibility
- scroll start, mid-state, and end-state
- route push, pop, and system back
- motion in profile mode

### Test support

Use official Flutter testing guidance for:

- widget behavior
- accessibility guidelines
- integration flows
- goldens or screenshots

Keep golden coverage focused on stable visual contracts. Do not lock every animated intermediate frame unless it protects a real regression.

## Implementation Checklist

- [ ] Existing architecture and visual system inspected.
- [ ] Preserve, repair, and introduce decisions recorded.
- [ ] Design Bible maps to discoverable code locations.
- [ ] Tokens cover semantic repetition without hiding bespoke geometry.
- [ ] Shell, back behavior, and system insets are intentional.
- [ ] Layout responds to available space.
- [ ] Assets have crop, fallback, provenance, and memory strategy.
- [ ] Complete states are implemented.
- [ ] Motion policy and interruption behavior exist.
- [ ] Custom visuals preserve semantics.
- [ ] Preview and screenshot matrix was inspected.
- [ ] Accessibility and performance checks match the feature's risk.
