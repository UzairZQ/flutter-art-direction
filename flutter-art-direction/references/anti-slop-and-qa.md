# Flutter Anti-Slop and Visual QA

Use this reference to audit an existing Flutter interface and before delivering visual work. Anti-slop is contextual: identify repeated defaults and weak reasoning, then repair the design system. Do not turn this list into a style police checklist that bans valid product choices.

## Contents

- Audit order
- Common signals and repairs
- Interaction and state QA
- Accessibility verification
- Motion and performance QA
- Preview and screenshot matrix
- Delivery report

## Audit Order

Review in this order:

1. **Product truth:** Does the screen show the real job, data, and action?
2. **Flow:** Can users reach, complete, reverse, and recover from the task?
3. **Hierarchy:** Is the first read obvious without relying on animation?
4. **Platform behavior:** Do scrolling, back, text input, system bars, and controls feel native?
5. **Authorship:** Is there a coherent product world and one ownable idea?
6. **States:** Are unsuccessful and edge states designed?
7. **Accessibility:** Can people perceive and operate the custom UI?
8. **Performance:** Does the rendered design stay smooth on target hardware?
9. **Polish:** Are alignment, crop, type, color, shape, and motion coherent?

Do not begin by changing colors or adding shadows when the flow or information hierarchy is wrong.

## Common Signals and Repairs

| Signal | Likely cause | Better repair |
|---|---|---|
| Purple-blue gradient with generic dark cards | default aesthetic chosen before product research | derive palette from product world, content, and brand assets |
| Every fact is inside a rounded card | containment used instead of hierarchy | group with alignment, type, spacing, and dividers; keep cards for real boundaries |
| Nested cards and glass layers | depth has no semantic model | define surface levels and remove effects that do not indicate focus or elevation |
| Many pills, chips, badges, and status dots | labels used as decoration | keep interactive filters and real statuses; rewrite the rest as hierarchy or copy |
| Three cloned onboarding pages | template substituted for onboarding strategy | teach in context, request permission just in time, or make each step behaviorally distinct |
| Generic line icons for domain concepts | component library became the product identity | use one coherent family for system actions and create specific assets for ownable concepts |
| Dashboard of unrelated metrics | desire to make the screen look substantial | identify the next decision and show only data that supports it |
| Static percentages or suspicious precision | invented data used as visual filler | bind to real state, label fixtures, show uncertainty, or omit the metric |
| Hero image, headline, paragraph, CTA on every phone screen | website composition copied into app UI | start from navigation, task, content, and thumb-reachable actions |
| Tiny uppercase eyebrow on every section | repeated template rhythm | remove labels that do not add information and vary hierarchy by content |
| Same fade-up on every child | motion added after layout without a model | create a motion score and animate only meaningful groups or continuity objects |
| Infinite shimmer, float, pulse, or particles | movement treated as polish | bind loops to a live state, pause when hidden, and stop when the state ends |
| Custom physics everywhere | authored feel confused with unfamiliar behavior | preserve platform scrolling and back; customize bounded product interactions |
| Huge token layer around every literal | design-system purity replacing clarity | tokenize repeated semantic decisions and keep bespoke geometry readable |
| "Unlock", "elevate", "seamless", "smart" copy | value proposition was never made concrete | name the action, content, result, timing, or limitation |

No single item proves poor quality. Repetition without product reasoning is the stronger signal.

## Composition QA

- The most important action is visible and reachable.
- The screen remains understandable with images delayed and motion disabled.
- Content groups use at least two hierarchy tools before adding a container.
- Repeated components have a real repeated content role.
- Shapes communicate component family or state.
- Surfaces do not compete through equal elevation.
- Long text has a readable measure on wider devices.
- Empty space reflects hierarchy rather than accidental missing content.
- Edge-to-edge media does not place text or controls under system UI.
- A small phone does not become a squeezed desktop composition.
- Text is comfortably readable without shrinking to preserve an overfilled layout.

## Concept-Image QA

For generated screen concepts:

- Generate each requested screen at readable scale rather than as a tiny collage.
- Keep device frame, scale, bezel, background, and outer margins consistent across the set.
- Keep palette, type hierarchy, icon weight, radii, texture, navigation, and button hierarchy in one product system.
- Let composition, density, imagery, and CTA placement vary enough that screens do not look cloned.
- Inspect status bars, safe areas, navigation, keyboards, sheets, and home-indicator regions for believable mobile behavior.
- Treat malformed text, impossible controls, generated device chrome, and accidental geometry as concept errors, not implementation instructions.
- Regenerate weak screens directly; do not crop details out of a larger board to hide quality problems.

## Copy and Data QA

Read every visible string:

- remove generic marketing language
- replace invented precision and fake social proof
- keep action labels concrete
- explain errors with a recovery path
- avoid shame, false urgency, and manipulative streak language
- distinguish pending, stale, estimated, and final data
- test real long names, values, and localized strings
- ensure placeholder and sample data are visibly honest

For charts:

- identify the decision the chart supports
- label units and time range
- provide non-color distinctions
- expose a semantic summary
- handle sparse, missing, and extreme data
- avoid decorative chart varieties in one screen

## Interaction and State QA

### Controls

- Use semantic Flutter controls where they fit.
- Give custom controls an equivalent semantic role, label, value, and action.
- Keep pressed feedback quick and visually stable.
- Avoid moving a control outside its hit area during press.
- Make disabled state visibly distinct and actually non-interactive.
- Keep destructive actions separated and recoverable where possible.

### Gestures

- Keep one primary gesture per region.
- Avoid conflicts with iOS back swipe, Android predictive back, sheet dismiss, and system gesture regions.
- Provide a visible button or menu alternative for custom gestures.
- Preserve content and input when a gesture is cancelled.
- Test slow drag, fast fling, reversal, repeated input, and multi-touch edge cases.

### States

Verify the states relevant to the feature:

- loading and slow loading
- empty and first use
- partial, stale, and offline
- error and retry
- permission rationale, denial, and permanent denial
- pressed, selected, focused, hovered, disabled
- save in progress, success, conflict, and undo
- long text, keyboard open, and validation error

## Accessibility Verification

### Automated Flutter guideline test

```dart
testWidgets('meets accessibility guidelines', (tester) async {
  final handle = tester.ensureSemantics();
  addTearDown(handle.dispose);

  await tester.pumpWidget(const TestApp());
  await tester.pumpAndSettle();

  await expectLater(tester, meetsGuideline(androidTapTargetGuideline));
  await expectLater(tester, meetsGuideline(iOSTapTargetGuideline));
  await expectLater(tester, meetsGuideline(labeledTapTargetGuideline));
  await expectLater(tester, meetsGuideline(textContrastGuideline));
});
```

Run both target-size checks only when the app intentionally supports both platform conventions; otherwise use the relevant platform gate.

### Manual checks

- TalkBack on Android
- VoiceOver and Xcode Accessibility Inspector on iOS
- Android Accessibility Scanner
- large system text and display scaling
- bold text and high contrast where supported
- grayscale or color-vision checks for functional color
- keyboard and focus traversal on tablets, desktop, and accessibility input
- reduced motion

Do not add `Semantics` around every widget. Flutter's built-in controls already expose semantics. Add or merge semantics for custom controls, compound content, custom painting, images, and state that the framework cannot infer.

### Touch and text

- Target approximately 48x48 logical pixels on Android and 44x44 points on iOS for interactive controls.
- Keep tap targets separated enough to avoid accidental activation.
- Let text wrap before truncating meaningful content.
- Use ellipsis only when the full value is available elsewhere.
- Test at the largest supported text settings, not only a fixed 2.0 multiplier.

## Motion and Performance QA

### Motion

- Every important animation has a named purpose.
- Navigation never waits on decoration.
- Repeated input interrupts or updates the current motion cleanly.
- Push, pop, reverse, and cancellation paths work.
- Reduced motion removes camera-like movement, parallax, particles, and nonessential scale or rotation.
- No essential information exists only in an animated intermediate frame.
- Haptics reinforce a causal event and are not fired for every routine tap.

### Rendering

Profile important screens in profile mode:

- inspect UI and raster frame charts
- enable slow animations to inspect choreography
- look for `saveLayer`, large opacity groups, clipping, shadows, blur, and filters
- check raster cache and image decode behavior
- inspect repaints before adding `RepaintBoundary`
- avoid intrinsic layout in large scrolling regions
- use lazy builders for long collections
- pause or remove offscreen loops

An effect is allowed when it earns its cost and meets the target device budget.

## Preview and Screenshot Matrix

Use the smallest matrix that covers the feature risk.

| Dimension | Minimum visual check |
|---|---|
| Width | small phone plus representative target |
| Orientation | portrait; landscape when supported or likely |
| Theme | every shipped brightness or contrast mode |
| Text | default plus large system setting |
| State | loaded plus relevant loading, empty, error, permission |
| Motion | normal plus reduced motion |
| Content | realistic, long, sparse, and extreme values |
| Platform | Android and iOS when behavior differs |
| Concept presentation | raw screen or one consistent, evenly padded device frame |

Inspect screenshots at full size and thumbnail size. Thumbnail inspection reveals hierarchy; full size reveals type, alignment, crop, and state polish.

For motion, capture video or inspect live. A start and end screenshot cannot prove timing, interruption, continuity, or jank.

## Static Audit Script

Run:

```bash
python3 <skill-folder>/scripts/audit_flutter_ui.py <flutter-project>
```

The script flags code patterns that deserve review, including:

- invented percentages and generic marketing copy
- random data in UI code
- repeated literal color and spacing usage
- explicit type below 12 logical pixels, repeated large radii, and gradient-heavy files
- animations without an obvious reduced-motion policy
- controllers without local disposal
- expensive rendering primitives
- nested scroll warning combinations

Findings are advisory. Inspect context before changing code. The script cannot determine whether a gradient belongs to the brand, a `BackdropFilter` is performant, or a local literal is appropriate.

## Delivery Report

At handoff, state:

- the Design Read and signature idea
- which screens and states changed
- which rendered sizes and modes were inspected
- which tests and audits ran
- whether motion was profiled on device
- any unverified platform, asset, accessibility, or performance risk
- for image concepts, the generation mode, prompt set or reusable direction, inspected screen count, and saved paths

Do not claim a screen is production-ready when it was never rendered.
