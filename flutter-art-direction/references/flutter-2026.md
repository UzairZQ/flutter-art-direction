# Flutter 2026 Design Capability Guide

Last research pass: 2026-07-16.

Flutter documentation currently reflects Flutter 3.44.0. Treat this file as a capability map, not permission to use every API. Inspect the project's SDK constraint and installed Flutter version before implementation, and verify current API documentation when exact signatures matter.

## Contents

- Version discipline
- Current platform baseline
- Flutter 3.44 design-relevant changes
- Rendering and effects
- Widget Previewer
- Material and platform behavior
- Package discipline

## Version Discipline

Before proposing a recent API:

1. Read the project's `environment.flutter` and Dart SDK constraints.
2. Run `flutter --version` when execution is available.
3. Search the repository for existing compatibility wrappers.
4. Check the API against the installed SDK, not only the latest website.
5. Offer a compatible fallback when raising the minimum Flutter version is not in scope.

Do not write "latest Flutter" into durable guidance. Name the verified version and date.

## Current Platform Baseline

### Rendering

Impeller is the default rendering engine for iOS and Android in current Flutter documentation. This improves rendering predictability but does not make every blur, shader, particle field, clip, or opacity group free.

Continue to:

- profile UI and raster work
- inspect `saveLayer` events
- constrain backdrop and image-filter areas
- avoid unnecessary intrinsic layout in scrolling regions
- size and cache images intentionally
- test on representative hardware

### Material 3

Material 3 has been enabled by default since Flutter 3.16. Use current components as accessible, platform-aware building blocks:

- `NavigationBar`, `NavigationRail`, and `NavigationDrawer`
- `FilledButton`, tonal buttons, and `SegmentedButton`
- `SearchBar`, `SearchAnchor`, and `MenuAnchor`
- `CarouselView`
- semantic `ColorScheme` roles and component themes

Material 3 Expressive encourages more intentional color, type, shape, hierarchy, and motion. It does not require maximal color, constant shape morphing, or a Google-branded appearance. Start from user need and critical journeys.

### Android edge-to-edge

Flutter apps targeting Android 15 moved to edge-to-edge by default beginning with the Flutter 3.27 transition. Design backgrounds and scrolling media to extend under system bars while keeping text, controls, and gesture targets clear of system insets and cutouts.

Do not stack multiple system-bar protections. Test gesture navigation and three-button navigation when Android is a target.

### iOS 26

Flutter 3.38 added full support for iOS 26, Xcode 26, and macOS 26, including migration work for Apple's UIScene lifecycle. Platform support does not mean a Flutter app should imitate every current Apple visual effect.

Use Cupertino behavior and system conventions where they improve familiarity. Treat Liquid Glass or similar material treatments as product decisions with contrast, fallback, and performance requirements.

### Platform adaptation

Flutter automatically adapts several behaviors, including:

- route transitions
- back gestures
- scroll physics, overscroll, momentum, and scrollbars
- text editing and selection behavior
- some icons and haptics

Do not override these reflexively. Flutter's guidance distinguishes OS-environment behavior, which should usually adapt, from app information architecture, which requires a deliberate design decision.

## Flutter 3.44 Design-Relevant Changes

The 3.44 release notes include additions and refinements relevant to art-directed UI:

- Hero gained more customizable animation-curve support.
- `SizeTransition` gained alignment control.
- `RoundedSuperellipseInputBorder` expanded expressive input shape options.
- `MenuAnchor` gained animation and positioning improvements.
- `CarouselView` and `CarouselController` gained richer item-change and infinite-carousel capabilities.
- Modal bottom sheets can use `AnimationStyle` curve and reverse-curve configuration.
- Predictive-back transitions gained fallback color and display-corner-radius support.
- `NavigationRail` gained additional main-axis alignment control.
- Widget Preview detection, custom annotations, filtering, and IDE integration continued to improve.
- Flutter web added reduced-motion or disable-animation support.

These are version-dependent. Confirm exact constructors and properties in the installed SDK before coding.

## Rendering and Effects

### Built-in animation system

Flutter's typed animation system remains the default foundation:

- implicit animation widgets for isolated property changes
- transition widgets and `AnimatedBuilder` for controlled rebuild scope
- `AnimationController`, `Tween`, `Curve`, and `Interval` for choreography
- physics simulations and `fling` for physical settling
- `Hero` for shared-object continuity
- `Flow` for paint-phase child positioning
- slivers for scroll-aware layout

Use the lowest level that expresses the intended behavior cleanly.

### Fragment shaders

Custom `.frag` shaders can be declared in `pubspec.yaml` and loaded through `FragmentProgram.fromAsset`. Canvas-based shader painting works across supported Skia and Impeller backends.

`ImageFilter.shader` is Impeller-only. Always:

- bound the affected area
- provide fallback behavior
- avoid using a shader as the only information channel
- test every target backend
- profile on device

### Custom graphics

Choose:

- `CustomPainter` when painting changes but layout and hit testing remain widget-driven
- `FlowDelegate` when child position should change during paint
- `CustomClipper` for authored clipping with a measured cost
- a custom render object only when layout, paint, or hit testing cannot be expressed clearly with existing widgets

## Widget Previewer

The Flutter Widget Previewer requires Flutter 3.35 or newer. IDE integration requires Flutter 3.38 or newer. As of the current documentation, the feature remains experimental and its APIs may change.

Use previews for:

- component states
- phone-size constraints
- light and dark themes
- custom text scale
- localization
- wrappers that inject theme or state

Do not use a Chrome preview as the only proof of native route behavior, platform text editing, haptics, system bars, or runtime performance.

## Current Visual QA Stack

Use the layers that match risk:

1. Widget previews for rapid visual iteration.
2. Widget tests for behavior and accessibility guidelines.
3. Golden or screenshot tests for stable visual contracts.
4. Simulator or device screenshots for platform composition.
5. Profile-mode device inspection for important motion and rendering.
6. TalkBack, VoiceOver, Android Accessibility Scanner, and Xcode Accessibility Inspector for custom UI.

Flutter's accessibility Guideline API includes Android and iOS tap-target checks, labeled-target checks, and text-contrast checks.

## Package Discipline

Do not maintain a universal category-to-package table. Package quality and project fit change.

Before adding a visual or motion package:

- confirm Flutter does not already provide the capability
- inspect publication recency, repository activity, unresolved issues, platform support, license, and migration cost
- verify it supports the project's minimum SDK and rendering targets
- estimate binary, startup, memory, and asset-pipeline cost
- prototype the hardest state before committing
- preserve a static or built-in fallback for critical flows

Reasonable roles:

- `flutter_animate`: concise, declarative effect composition
- Rive: interactive vector state machines and designer handoff
- Lottie: bounded playback of existing motion assets
- chart packages: real data visualization with semantic alternatives
- custom carousel packages: only when `PageView` or `CarouselView` cannot express the interaction

Never switch the app's state-management, routing, or component system solely because an art-direction table prefers another package.
