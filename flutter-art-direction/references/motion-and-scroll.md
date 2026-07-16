# Motion and Scroll for Authored Flutter Apps

Read this reference for motion-led screens, gesture coupling, immersive storytelling, custom graphics, or Wonderous-like depth. Use the patterns selectively.

## Contents

- Motion principles
- Motion score
- Wonderous-derived patterns
- Web-to-mobile translation
- Flutter implementation patterns
- Advanced rendering
- Performance and accessibility
- Motion QA

## Motion Principles

### Motion explains a model

Use motion to communicate one of five things:

1. **Orientation:** where a view or object came from.
2. **Continuity:** which object persists across a transition.
3. **Feedback:** that input was received.
4. **State:** what changed and which value caused it.
5. **Story:** how a rare narrative moment should unfold.

Do not animate because a dial is high. A still screen with one excellent transition is more authored than a screen where every child fades upward.

### Input leads, visuals follow

During direct manipulation:

- map drag distance to progress continuously
- keep the touched object visually attached to the finger
- let the user reverse direction
- decide completion from distance and velocity
- settle only after release
- keep the destination available even if motion is disabled

Avoid starting a canned animation on drag start while ignoring the rest of the gesture.

### Preserve spatial truth

If a sheet enters from the bottom, dismiss it toward the bottom. If an image is selected, preserve its identity and apparent position into detail. If a list item moves, animate from its previous location rather than fading the whole list.

### Make routine motion brief

Frequent interactions should not demand attention. Use stronger choreography for:

- first-use teaching that cannot be just-in-time
- a chapter or mode change
- a rare achievement
- a signature object transition
- an immersive product-specific scene

Keep navigation and controls usable while motion runs. Allow repeated interactions to interrupt or supersede the current animation.

### Design reduced motion, do not merely shorten it

Reduced motion may require:

- replacing parallax with a stable crop
- replacing a Hero flight with an immediate route and short fade
- showing the final state of a stagger at once
- removing scale, rotation, camera movement, particles, and oscillation
- retaining a color, icon, text, or haptic confirmation

A duration of one millisecond can avoid code-path problems, but it is not a complete design policy by itself.

## Write a Motion Score

For each important transition, write:

| Field | Question |
|---|---|
| Trigger | Tap, drag, scroll, data update, route, or system event? |
| Source | What is visually true before it starts? |
| Destination | What must be visually true after it ends? |
| Continuity | Which object, axis, or focal point remains stable? |
| Purpose | Orientation, continuity, feedback, state, or story? |
| Control | Time-driven, gesture-driven, scroll-driven, or physics-driven? |
| Interruption | What happens if the user acts again halfway through? |
| Reduced motion | What static or low-motion result preserves meaning? |
| Cost | Which subtree rebuilds or repaints? Which assets or filters are involved? |

Do not specify one global duration or spring for the entire app. Define a small motion vocabulary:

- quick feedback
- standard state change
- spatial navigation
- expressive one-off
- continuous gesture response

Calibrate curves and springs in rendered output. Numeric stiffness and damping values are implementation parameters, not emotional truth.

## Wonderous-Derived Patterns

These patterns come from the open-source Wonderous implementation. Reuse the engineering logic, not its visual identity.

### 1. Layer a scene by depth role

Wonderous composes background, middle-ground, foreground, gradients, and floating controls in a `Stack`. Each illustration piece has:

- fractional height and alignment
- authored pixel or fractional offsets
- an entrance offset and scale
- a depth-specific zoom amount
- optional Hero continuity

This makes an art-directed scene responsive without flattening every coordinate into generic tokens.

Apply it when:

- the screen represents a place, object, collection, or narrative world
- assets can be separated cleanly into depth layers
- motion has a focal object

Avoid it when:

- the screen is a dense tool
- layers obscure controls or text
- assets cannot tolerate varied aspect ratios

### 2. Drive several effects from one gesture value

The Wonderous home gesture maps upward drag progress to:

- foreground zoom
- middle-ground zoom
- gradient density
- route intent
- release animation

A single normalized value creates coherence. The visual system feels physical because every dependent effect agrees about progress.

Use a `ValueNotifier<double>`, `AnimationController`, or another existing state primitive to expose normalized progress. Rebuild only the dependent layers.

### 3. Freeze the transition handoff

Before routing, Wonderous captures the current swipe amount so the foreground does not jump while the next route takes over. This is a general handoff rule:

- snapshot gesture-driven state at commit
- keep source visuals stable during route construction
- let Hero or route motion continue from that stable state
- clear the snapshot after the destination owns the frame

### 4. Use one timeline for a layered entrance

Wonderous illustration pieces receive one parent animation and derive their own offset, scale, and opacity. Flutter's official stagger pattern uses the same concept: one controller, multiple tweens with `Interval` values.

Use one timeline when elements belong to one perceptual event. Use separate controllers when interactions can occur independently.

### 5. Skip invisible rendering work

The Wonderous illustration builder omits a fully hidden scene instead of keeping every layer alive at zero opacity. It also isolates selected expensive visuals with `RepaintBoundary`.

Generalize carefully:

- do not build offscreen art worlds without a reason
- keep adjacent pages only when continuity or preloading justifies the memory
- isolate repaints only after checking repaint behavior
- predecode important images before a signature transition

### 6. Build editorial scroll with slivers

Wonderous uses `CustomScrollView`, `SliverAppBar`, sliver content, and scroll-driven transforms to move from an immersive illustration into readable editorial content.

The key is choreography around native scrolling:

- an opening gap reveals the scene
- title content translates and fades as the user scrolls
- the app bar collapses and pins
- long-form content becomes stable and readable
- decorative imagery reacts while body copy remains grounded

This achieves website-level storytelling without replacing mobile scrolling.

### 7. Preserve selected objects with Hero

Wonderous uses stable, product-derived Hero tags for artifacts and illustration pieces. Apply `Hero` when the same object genuinely exists in both routes. Do not Hero unrelated containers simply to add movement.

### 8. Keep celebration finite

The collectible celebration creates a bounded particle burst, reduces emission over time, fades the field, removes old particles, and isolates painting. The lesson is proportionality:

- celebrate a rare event, not every tap
- end the effect
- keep controls available
- use a static success state under reduced motion
- profile particle count on target hardware

## Translate Web Choreography to Mobile

| Web pattern | Mobile translation | Avoid |
|---|---|---|
| Pinned scrollytelling section | Short `SliverAppBar` or bounded chapter with native scroll | Locking the user into a long fake scroll |
| Scroll-scrubbed parallax | Small paint-phase background shift via `Flow` or a bounded transform | Moving body text or controls at different rates |
| Horizontal scroll hijack | `PageView`, `CarouselView`, or explicit chapter tabs | Converting vertical gestures unexpectedly |
| Hover reveal | Press, focus, selection, drag, or viewport-entry state | Hiding essential information until hover |
| Sticky card stack | Paged deck, sliver overlap, or direct drag stack | Dozens of layered cards with costly shadows |
| Full-page transition overlay | Shared object, platform route, or short state transition | Blocking navigation until a decorative wipe finishes |
| Cursor magnetism | Touch-down compression, drag attraction, or haptic snap | Controls that move away from the finger |
| Kinetic typography | Short title reveal or variable-font state cue | Character animation on long or localized text |
| Infinite marquee | User-controlled horizontal collection | Perpetual motion competing with reading |
| WebGL ambient scene | Bounded CustomPaint, fragment shader, Rive, or 3D scene | Full-screen GPU work behind routine screens |

On mobile, direct manipulation and continuity usually feel more advanced than a longer animation.

## Flutter Implementation Patterns

### Centralize motion policy

```dart
@immutable
final class AppMotionPolicy {
  const AppMotionPolicy({
    required this.reduceMotion,
    required this.highContrast,
  });

  factory AppMotionPolicy.of(BuildContext context) {
    final media = MediaQuery.of(context);
    return AppMotionPolicy(
      reduceMotion: media.disableAnimations,
      highContrast: media.highContrast,
    );
  }

  final bool reduceMotion;
  final bool highContrast;

  Duration choose(Duration normal) =>
      reduceMotion ? Duration.zero : normal;
}
```

For complex scenes, pass the policy into the scene instead of reading `MediaQuery` in every leaf.

### Couple a drag to normalized progress

```dart
class RevealController {
  RevealController({required TickerProvider vsync})
      : settle = AnimationController(vsync: vsync)
          ..addListener(() => progress.value = settle.value);

  final progress = ValueNotifier<double>(0);
  final AnimationController settle;

  void update(double primaryDelta, double travel) {
    settle.stop();
    progress.value = (progress.value + primaryDelta / travel).clamp(0, 1);
  }

  Future<void> release({required bool commit}) async {
    final target = commit ? 1.0 : 0.0;
    await settle.animateTo(target, curve: Curves.easeOutCubic);
  }

  void dispose() {
    progress.dispose();
    settle.dispose();
  }
}
```

Choose the sign, travel distance, velocity rule, and route commit behavior for the actual gesture. Under reduced motion, commit the state directly.

### Derive several visual properties from one progress value

```dart
AnimatedBuilder(
  animation: reveal.progress,
  child: const ProductArtwork(),
  builder: (context, child) {
    final t = Curves.easeOut.transform(reveal.progress.value);
    return Transform.scale(
      scale: 1 + 0.08 * t,
      alignment: Alignment.bottomCenter,
      child: DecoratedBox(
        decoration: BoxDecoration(
          color: Colors.black.withValues(alpha: 0.18 * t),
        ),
        child: child,
      ),
    );
  },
)
```

Hoist stable children through the `child` argument. Keep semantic controls outside decorative transforms when possible.

### Use intervals for a single perceptual event

```dart
final image = CurvedAnimation(
  parent: controller,
  curve: const Interval(0.0, 0.65, curve: Curves.easeOutCubic),
);
final title = CurvedAnimation(
  parent: controller,
  curve: const Interval(0.28, 0.82, curve: Curves.easeOut),
);
final action = CurvedAnimation(
  parent: controller,
  curve: const Interval(0.55, 1.0, curve: Curves.easeOut),
);
```

Do not stagger long lists item by item. Animate the visible group or the first few meaningful elements, then show the rest.

### Use native scroll as the clock

```dart
AnimatedBuilder(
  animation: scrollController,
  child: const ChapterArtwork(),
  builder: (context, child) {
    if (!scrollController.hasClients) return child!;
    final t = (scrollController.offset / 280).clamp(0.0, 1.0);
    return Transform.translate(
      offset: Offset(0, 28 * t),
      child: Opacity(opacity: 1 - t, child: child),
    );
  },
)
```

For list-item parallax that depends on paint-time position, prefer Flutter's documented `FlowDelegate` pattern. Avoid calling `setState` for an entire screen on every scroll tick.

### Preserve object continuity

```dart
Hero(
  tag: ObjectKey(item.id),
  createRectTween: (begin, end) =>
      MaterialRectCenterArcTween(begin: begin, end: end),
  child: ItemArtwork(item: item),
)
```

Use matching tags and compatible child trees. Test push, pop, interrupted gestures, text scaling, and image loading. Check the current SDK before using newly added Hero curve APIs.

### Paint only what changes

For `CustomPainter`:

- pass a `Listenable` to `repaint` when paint can update without rebuilding widgets
- return a meaningful `shouldRepaint`
- keep semantic information in widgets or `semanticsBuilder`
- cache paths, pictures, and decoded assets when profiling proves value
- avoid allocating large objects inside `paint`

## Advanced Rendering

### Fragment shaders

Use `FragmentProgram` when the concept requires a GPU-authored effect that widgets and `CustomPaint` cannot express cleanly. Declare shaders in `pubspec.yaml`, load them as assets, and update uniforms without rebuilding unrelated UI.

Keep in mind:

- Canvas shaders work on supported Skia and Impeller backends.
- `ImageFilter.shader` is Impeller-only.
- Clip a backdrop filter to the smallest required area.
- Provide a non-shader fallback where backend support or accessibility requires it.
- Profile startup, shader loading, memory, and raster time.

### Rive and Lottie

Prefer Rive for interactive state machines and designer-authored vector behavior. Prefer Lottie for bounded playback of an existing After Effects animation. Do not add either package for a fade, slide, or simple morph Flutter already handles.

### CustomPaint and particles

Use custom painting for product-specific diagrams, procedural texture, paths, and finite effects. Keep interactive hit targets and semantics in the widget layer. Bound particle lifetime and emission; pause or remove effects when obscured.

## Performance and Accessibility

- Profile in profile mode on a representative lower-end target, not only a simulator in debug mode.
- Inspect both UI and raster timelines. High-refresh devices reduce the time available per frame.
- Treat `saveLayer`, large opacity groups, clipping, blur, `ShaderMask`, shadows, and filters as costs to inspect, not forbidden features.
- Use lazy builders for long collections and avoid intrinsic layout passes in scrolling regions.
- Decode images close to display size when practical and pre-cache only assets needed for an imminent transition.
- Keep animated subtrees small. Hoist stable children from builders.
- Use `RepaintBoundary` after checking repaint behavior; too many boundaries consume memory and can hurt compositing.
- Test with `MediaQuery.disableAnimations`, large text, high contrast, TalkBack, and VoiceOver.
- Never rely on movement, color, sound, or haptics alone to convey meaning.
- Keep gesture alternatives visible for users who cannot perform the custom gesture.

## Motion QA

For each important animation:

- [ ] Purpose is named.
- [ ] Source and destination states are visually coherent.
- [ ] Input remains available or cancellation behavior is defined.
- [ ] Back and reverse paths work.
- [ ] Reduced motion preserves meaning and access.
- [ ] Large text and localization do not collide with moving layers.
- [ ] Hero tags are stable and unique in each route subtree.
- [ ] Scroll remains native and does not trap the user.
- [ ] Decorative layers do not move controls or body text unpredictably.
- [ ] Controllers, listeners, and subscriptions are disposed.
- [ ] Infinite animations stop when hidden or no longer meaningful.
- [ ] Performance is checked in profile mode on a target device.
- [ ] Screenshots capture start and end states; video or live inspection checks the path between them.
