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

## Design Tokens in Code

Reference: `references/design-token-architecture.md`

Implement a three-tier token system before any widget code.

### File Structure
```text
lib/ui/core/tokens/
  primitives/           # Raw values: color-primitives.dart, spacing-primitives.dart
  semantic/             # Context-aware: colors.dart, spacing.dart, typography.dart
  component/            # Component-scoped: button-tokens.dart, card-tokens.dart
```

### Code Gen Pipeline
1. Source: `tokens/source/figma-tokens.json`
2. Transform: `scripts/generate_tokens.dart` → Dart files
3. Output: `lib/ui/core/tokens/`

### Usage Rules
- **NEVER** hardcode raw values in widget code
- **ALWAYS** use semantic tokens: `AppTokens.semantic.color.surfaceBase`
- **Use** component tokens for component-specific overrides

### Platform-Adaptive Tokens
```dart
static BorderRadius get radiusCard =>
  Platform.isAndroid ? BorderRadius.circular(16) // M3
                     : BorderRadius.circular(12); // iOS
```

## Adaptive Theming in Practice

Reference: `references/adaptive-theming.md`

### Dynamic Color
```dart
final colorScheme = ColorScheme.fromSeed(
  seedColor: brandSeed,
  dynamicSchemeVariant: DynamicSchemeVariant.fidelity,
);
final fallbackScheme = ColorScheme.fromSeed(seedColor: brandSeed);
```

### Platform-Adaptive Components
| Component | Android (M3) | iOS (Cupertino) | Neutral |
| Button | FilledButton | CupertinoButton | Stadium |
| Nav Bar | NavigationBar | CupertinoTabBar | Adaptive |
| Dialog | AlertDialog | CupertinoAlertDialog | Custom |
| Switch | Switch.adaptive | CupertinoSwitch | Switch.adaptive |

### Semantic Color Roles
Use `Theme.of(context).colorScheme.surfaceContainerHigh` instead of `Colors.grey[100]`.

## Motion System

Reference: `references/motion-with-intent.md`

Every animation must map to one of 5 intent categories: Navigational, Feedback, State Transition, Emotional/Storytelling, Brand.

### Spring Physics Defaults
| Feeling | Stiffness | Damping | Use Case |
| Crisp | 300 | 25 | Feedback, button press |
| Standard | 210 | 20 | Navigational, default |
| Soft | 150 | 12 | State transitions, sheets |
| Loose | 100 | 8 | Celebrations, storytelling |

### Reduced Motion Pattern
```dart
final disableAnimations = MediaQuery.of(context).disableAnimations;
final duration = disableAnimations ? Duration.zero : AppMotion.mediumSpring.duration;
```

### Choreography Rules
- Max 2 concurrent motions per screen
- Stagger children: `delay = index * 50ms`
- Parent completes before children for enters
- Exits in parallel (fast)

## Spatial/Depth Implementation

Reference: `references/spatial-mobile-design.md`

Use 4 depth layers: Base (0), Surface (1-3), Raised (6-8), Overlay (12-16).

### Glass as Hierarchy
```dart
ClipRRect(
  borderRadius: AppRadii.card,
  child: BackdropFilter(
    filter: ImageFilter.blur(sigmaX: 20, sigmaY: 20),
    child: Container(
      color: Colors.white.withOpacity(0.7),
      child: content,
    ),
  ),
)
```

### Parallax on Scroll
- Hero parallax: max 20px offset via `Transform.translate`
- Gyroscope tilt: subtle 3D on 2D (opt-in, reduced-motion off)

## Gesture System Implementation

Reference: `references/gesture-first-navigation.md`

### Core Gestures
| Gesture | Affordance | Fallback |
| Edge swipe back | System gesture + optional < | Back button |
| Drag down | Sheet drag handle | Close button |
| Long press | Haptic + scale | Context menu |
| Swipe horizontal | Reveal actions | Trailing button |

### Back Gesture (go_router compatible)
```dart
PopScope(
  canPop: false,
  onPopInvoked: (didPop) => if (!didPop) context.pop(),
  child: Scaffold(...),
)
```

### Sheet Dismiss
```dart
DraggableScrollableSheet(
  initialChildSize: 0.5,
  minChildSize: 0.25,
  maxChildSize: 0.9,
  builder: (context, scrollController) => SheetContent(
    dragHandle: true,
    onDragEnd: (details) =>
      if (details.velocity.pixelsPerSecond.dy > 500) context.pop(),
  ),
)
```

## Emotional Design Integration

Reference: `references/emotional-design-framework.md`

### Norman's 3 Levels → Widget Mapping
| Level | Design Concern | Flutter Pattern |
| Visceral | Immediate reaction | Theme, hero imagery, first-frame motion |
| Behavioral | Flow & usability | Navigation, state design, micro-interactions |
| Reflective | Meaning & memory | Empty states, milestones, share artifacts |

### Emotional Stance Validation
Every screen must have intentional choices at all 3 levels. Empty/error states are reflective-level surfaces.

## Accessibility Implementation

Reference: `references/accessibility-gates.md`

### CI-Enforced Gates
1. Reduced motion: `MediaQuery.disableAnimations` respected
2. Text scaling: tested at 200%
3. Semantics: labels on all interactive elements
4. Contrast: 4.5:1 (AA) minimum
5. Touch targets: 48×48dp minimum

### Implementation Pattern
```dart
Semantics(
  label: 'Close dialog',
  hint: 'Double tap to dismiss',
  child: IconButton(
    icon: Icon(Icons.close),
    onPressed: () => Navigator.pop(context),
  ),
)
```

## Golden/Screenshot Testing

Reference: `references/preview-and-screenshot-qa.md`

### Device Matrix
- Small phone (320px width)
- Large phone (414px width)
- Tablet (768px+) if supported
- Landscape if app rotates

### Scenarios
- Default, loading, empty, error, permission denied
- Long text, text scaling at 200%
- Reduced motion enabled
- Light and dark modes

### CI Integration
```yaml
# .github/workflows/visual-qa.yml
- name: Golden Tests
  run: flutter test --update-goldens
- name: Screenshot Inspection
  run: flutter test test/screenshots/
```

## Platform Alignment Checklist

Reference: `references/apple-design-awards-2025.md`, `references/material-3-expressive.md`

### iOS (HIG)
- [ ] Safe areas, Dynamic Type, SF Symbols
- [ ] Navigation: UINavigationController stack or go_router equivalent
- [ ] Haptics: UIImpactFeedbackGenerator equivalent
- [ ] Back swipe: edge swipe gesture
- [ ] Sheets: drag-to-dismiss, detents

### Android (M3 Expressive)
- [ ] Material 3 components (NavigationBar, FilledButton, SegmentedButton)
- [ ] Dynamic Color: ColorScheme.fromSeed
- [ ] Predictive back: PopScope
- [ ] Edge-to-edge: SystemUiOverlayStyle
- [ ] Spring motion: SpringDescription

### Cross-Platform Neutral
- [ ] Adaptive components for key surfaces
- [ ] Platform-consistent navigation pattern
- [ ] One design system that works on both
