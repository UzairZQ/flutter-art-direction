# Research Sources and Provenance

Last research pass: 2026-07-16.

Use this file to distinguish framework facts from design interpretation. Verify live documentation again when a task depends on an exact current API, release, package version, award result, or platform policy.

## Primary Technical Sources

### Flutter

- Current release and documentation baseline: https://docs.flutter.dev/release
- Flutter 3.44 release notes: https://docs.flutter.dev/release/release-notes/release-notes-3.44.0
- What's new in Flutter documentation: https://docs.flutter.dev/release/whats-new
- Animation overview: https://docs.flutter.dev/ui/animations/overview
- Animation and motion widget catalog: https://docs.flutter.dev/ui/widgets/animation
- Staggered animations: https://docs.flutter.dev/ui/animations/staggered-animations
- Hero animations: https://docs.flutter.dev/ui/animations/hero-animations
- Parallax with `FlowDelegate`: https://docs.flutter.dev/cookbook/effects/parallax-scrolling
- Fragment shaders: https://docs.flutter.dev/ui/design/graphics/fragment-shaders
- Performance best practices: https://docs.flutter.dev/perf/best-practices
- UI performance profiling: https://docs.flutter.dev/perf/ui-performance
- DevTools performance view: https://docs.flutter.dev/tools/devtools/performance
- Material Design for Flutter: https://docs.flutter.dev/ui/design/material
- Automatic platform adaptations: https://docs.flutter.dev/ui/adaptive-responsive/platform-adaptations
- Accessibility testing: https://docs.flutter.dev/ui/accessibility/accessibility-testing
- Accessibility UI design and styling: https://docs.flutter.dev/ui/accessibility/ui-design-and-styling
- Widget Previewer: https://docs.flutter.dev/tools/widget-previewer
- Android edge-to-edge Flutter migration: https://docs.flutter.dev/release/breaking-changes/default-systemuimode-edge-to-edge

### Android and Material

- Android mobile design guidance: https://developer.android.com/design/ui/mobile
- Android edge-to-edge design: https://developer.android.com/design/ui/mobile/guides/layout-and-content/edge-to-edge
- Android system bars: https://developer.android.com/design/ui/mobile/guides/foundations/system-bars
- Material components overview: https://developer.android.com/design/ui/mobile/guides/components/material-overview
- Material 3 theme, shape, and motion handoff: https://developer.android.com/codelabs/m3-design-theming
- Material 3 Expressive research lessons: https://developer.android.com/design/ui/wear/guides/get-started/benefits

Material 3 Expressive pages for Wear provide useful principles about emotion, type, shape, and motion, but Wear-specific component geometry must not be treated as phone guidance.

### Apple

- Human Interface Guidelines: https://developer.apple.com/design/human-interface-guidelines/
- Motion: https://developer.apple.com/design/human-interface-guidelines/motion
- Accessibility: https://developer.apple.com/design/human-interface-guidelines/accessibility
- Haptics: https://developer.apple.com/design/human-interface-guidelines/playing-haptics

Apple guidance informs iOS behavior and accessibility. Do not present Apple-only materials or symbols as portable Flutter web or Android APIs.

## Reference Implementations

### Wonderous

- Source repository: https://github.com/gskinnerTeam/flutter-wonderous-app
- gskinner Flutter showcase: https://flutter.gskinner.com/

The motion guide was derived from the current repository's real patterns, especially:

- `lib/ui/screens/home/wonders_home_screen.dart`
- `lib/ui/screens/home/_vertical_swipe_controller.dart`
- `lib/ui/wonder_illustrations/common/wonder_illustration_builder.dart`
- `lib/ui/wonder_illustrations/common/illustration_piece.dart`
- `lib/ui/screens/editorial/editorial_screen.dart`
- `lib/ui/screens/editorial/widgets/_scrolling_content.dart`
- `lib/ui/screens/timeline/widgets/_scrolling_viewport.dart`
- `lib/ui/screens/collectible_found/collectible_found_screen.dart`
- `lib/logic/common/animate_utils.dart`

Wonderous is MIT-licensed, but this skill extracts patterns rather than redistributing its assets or cloning its screens.

## Skill Research

### TasteSkill

- Repository: https://github.com/Leonxlnx/taste-skill
- Website: https://www.tasteskill.dev/

Useful transferable ideas:

- infer the brief before choosing an aesthetic
- state a Design Read
- use dials as reasoning constraints
- identify recurring AI defaults
- require rendered preflight checks
- keep motion motivated
- treat references and assets as first-class inputs

Web-only prescriptions, GSAP code, landing-page rules, hover behavior, and desktop typography defaults were not copied into the Flutter skill.

### UI UX Pro Max

- Repository: https://github.com/nextlevelbuilder/ui-ux-pro-max-skill

Useful transferable ideas:

- route detailed knowledge through progressive disclosure
- inspect the stack before recommending implementation
- prioritize accessibility, touch, performance, responsive layout, and navigation
- persist a design-system source of truth
- use searchable or deterministic tooling for repeatable audits
- include a pre-delivery checklist

Its Flutter table contains broad heuristics rather than an authoritative Flutter architecture standard. This skill does not copy package preferences, blanket `RepaintBoundary` advice, web animation presets, or style-database aesthetics.

## Design References

Wonderous, Reflectly, Gentler Streak, Flighty, Halide, Not Boring, Any Distance, Rive, and other apps are used as principle prompts. Their current features, awards, ownership, and exact visual systems may change.

When a user asks to emulate a current app:

1. verify the current product or supplied screenshots
2. identify the mechanism they value
3. avoid copying branding, assets, layout, and proprietary interaction
4. translate the principle into the new product's content and platform behavior

## Claims Policy

Use these labels while maintaining the skill:

- **Official:** directly supported by current Flutter, Android, Material, or Apple documentation.
- **Observed:** present in an inspected open-source implementation.
- **Heuristic:** a design recommendation requiring context and judgment.
- **Version-dependent:** confirm against the project's installed SDK or package.
- **Inspiration:** useful for art direction but not a technical requirement.

Do not turn a heuristic into a universal ban or an inspiration into a factual platform rule.
