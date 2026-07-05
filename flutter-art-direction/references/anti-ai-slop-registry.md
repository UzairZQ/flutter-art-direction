# Flutter Anti-Slop Registry

> **Optional deep-dive.** The compact reference (16-pattern table) is in `SKILL.md` section 5. Read this file when you need full before/after Dart code examples, `custom_lint` rule definitions, CI hook examples, or detailed prevention strategies for a specific pattern.

## Overview

This registry catalogs 16 AI-generated UI patterns that frequently appear in Flutter apps. These patterns emerge when AI models generate Flutter code without a grounded understanding of product design, brand systems, platform conventions, or real user data. Each entry includes detection heuristics, impact analysis, before/after code examples, and prevention strategies.

The registry serves as a code review checklist, an AI prompt engineering reference, and a lint rule catalog for teams that want to systematically eliminate low-quality generated UI.

---

## Detection

---

### 1. Purple-Blue Default Gradient

**Detection**
- Regex: `LinearGradient\(.*(Colors\.(purple|blue|deepPurple|indigo)|Color(0xFF[67][A-F0-9]{6}))` or `gradient.*purple.*blue`
- Heuristics: A `Container` or `ShaderMask` with a gradient that references no theme tokens; the gradient appears on CTAs, headers, or backgrounds without brand justification.
- Visual: Purple-to-blue sweep (or teal-to-blue) used as a primary brand color despite no brand assets using those hues.

**Impact**
- Erodes brand identity — the gradient signals "app template" rather than a specific product.
- Creates accessibility issues — purple+blue gradients often fail contrast checks on white text.
- Couples UI to hardcoded color literals, making theming impossible.

**Flutter Fix**

```dart
// BAD: Hardcoded generic gradient, no connection to theme
Container(
  decoration: const BoxDecoration(
    gradient: LinearGradient(
      colors: [Color(0xFF7C3AED), Color(0xFF3B82F6)],
      begin: Alignment.topLeft,
      end: Alignment.bottomRight,
    ),
  ),
  child: const Text('Get Started', style: TextStyle(color: Colors.white)),
),
```

```dart
// GOOD: Derived from a design token via ColorScheme
Container(
  decoration: BoxDecoration(
    gradient: LinearGradient(
      colors: [
        Theme.of(context).colorScheme.primary,
        Theme.of(context).colorScheme.tertiary,
      ],
      begin: Alignment.topLeft,
      end: Alignment.bottomRight,
    ),
  ),
  child: Text(
    'Get Started',
    style: TextStyle(color: Theme.of(context).colorScheme.onPrimary),
  ),
),
```

**Prevention**
- Never write a `LinearGradient` literal in widget code. Define gradients in a `ThemeExtension` or a dedicated tokens class.
- Use `ColorScheme.fromSeed` with a real brand seed color instead of raw `Color(0xFF…)` literals.
- Run `flutter analyze` with a custom lint that bans `LinearGradient` outside of theme extensions.

---

### 2. Fake Dashboard Chart Spam

**Detection**
- Regex: `(charts_flutter|fl_chart|syncfusion_flutter_charts).*Random\(` or `data\.generate\(.*Random\(\)\)`
- Heuristics: Three+ chart widgets (bar, line, pie) on a single screen; data sourced from `Random()` or hardcoded decimal lists; no `DataSource`, `Repository`, or API call in the widget tree.
- Visual: Decorative chart cards with no axis labels, legends, or data sources noted.

**Impact**
- Misleading in screenshots or demos — stakeholders may mistake mock data for real metrics.
- Wastes rendering resources — each chart widget rebuilds on every frame if data is generated inline.
- Signals incomplete product thinking; real dashboards answer specific questions (KPI trends, cohorts, funnels).

**Flutter Fix**

```dart
// BAD: Inline random data masquerading as a real chart
LineChart(
  LineChartData(
    lineBarsData: [
      LineChartBarData(
        spots: List.generate(12, (i) => FlSpot(i.toDouble(), Random().nextDouble() * 100)),
      ),
    ],
  ),
)
```

```dart
// GOOD: Semantic placeholder with loading/empty/error states
class RevenueChart extends StatelessWidget {
  const RevenueChart({required this.data, super.key});

  final List<RevenueRecord>? data;

  @override
  Widget build(BuildContext context) {
    if (data == null) return const Card(child: Skeletonizer());
    if (data!.isEmpty) return const Card(child: Text('No revenue data yet'));
    return LineChart(
      LineChartData(
        lineBarsData: [
          LineChartBarData(
            spots: data!.map((r) => FlSpot(r.day, r.amount)).toList(),
          ),
        ],
      ),
    );
  }
}
```

**Prevention**
- Require a data-fetching layer before any chart widget.
- Use a `ChartData` sealed class with `Loading`, `Empty`, `Error`, and `Loaded` variants.
- Label all mock/sample data with a visual badge in development builds.

---

### 3. Repeated Onboarding Slides

**Detection**
- Regex: `PageView\.builder.*onboarding` or `PageView.*children.*\[.*PageViewModel`
- Heuristics: Three identical `PageView` slides differing only in icon/headline/body text; a `PageController` + `AnimatedContainer` dot indicator; fourth slide has a "Get Started" button.
- Visual: Phone illustration → feature headline → "skip" link in top-right.

**Impact**
- High drop-off: generic onboarding communicates nothing about the app's actual differentiator.
- Ignores platform conventions — iOS uses `UIPageControl` at bottom, Android rarely uses page- slide onboarding at all.
- Every real onboarding should be A/B tested; templated onboarding is test- naïve.

**Flutter Fix**

```dart
// BAD: Three identical slides, only copy changes
PageView(
  children: [
    _OnboardingSlide(icon: Icons.lock, title: 'Secure', body: 'Your data is safe with us'),
    _OnboardingSlide(icon: Icons.speed, title: 'Fast', body: 'Lightning quick performance'),
    _OnboardingSlide(icon: Icons.people, title: 'Social', body: 'Connect with friends'),
  ],
)
```

```dart
// GOOD: Contextual, skip-able, platform-aware
class OnboardingFlow extends StatelessWidget {
  const OnboardingFlow({super.key});

  @override
  Widget build(BuildContext context) {
    // Only show onboarding if the user hasn't completed it yet
    return ValueListenableBuilder<bool>(
      valueListenable: onboardingCompleted,
      builder: (context, completed, _) {
        if (completed) return const HomeScreen();
        return PageView(
          children: const [
            ValuePropositionSlide(),
            FeatureHighlightSlide(),
            PermissionRequestSlide(),
          ],
        );
      },
    );
  }
}
```

**Prevention**
- Reduce onboarding to zero slides if possible (just-in-time permission requests).
- Each slide must serve a measurable purpose (permission grant, personalization choice, value prop unique to the app).
- Never generate onboarding slides from an LLM prompt without a product designer's input.

---

### 4. Pill/Badge/Chip Clutter

**Detection**
- Regex: `(Chip|InputChip|ChoiceChip|FilterChip|RawChip).*\{.*\n.*\n.*\n.*\}.*,` (four+ chips in one row)
- Heuristics: A horizontal `Wrap` or `SingleChildScrollView` with 5+ chips of varying colors; badges on every list tile; chips used as decorative elements rather than interactive filters.
- Visual: Rainbow-colored chips, text overflowing pill bounds, badges on icons that have no count.

**Impact**
- Visual noise: users cannot distinguish interactive chips from decorative badges.
- Accessibility: multiple colored chips without labels fail for color-blind users.
- Performance: `Wrap` with many children recalculates layout on every rebuild.

**Flutter Fix**

```dart
// BAD: Decorative chip wall with no semantic grouping
Wrap(
  children: ['Design', 'Dev', 'Marketing', 'Sales', 'HR', 'Legal', 'Finance']
      .map((tag) => Chip(label: Text(tag), backgroundColor: Colors.primaries[index++ % Colors.primaries.length]))
      .toList(),
)
```

```dart
// GOOD: Purposeful, accessible chips with FilterChip
Wrap(
  spacing: 8,
  children: categories
      .map((cat) => FilterChip(
            label: Text(cat.name),
            selected: cat.selected,
            onSelected: (_) => viewModel.toggleCategory(cat),
            visualDensity: VisualDensity.compact,
          ))
      .toList(),
)
```

**Prevention**
- Establish a maximum chip count per row (3–4 on mobile).
- Use `FilterChip` for filters, `Badge` for counts, never one for the other's job.
- Apply a single accent color for all chips; let selection state differentiate.

---

### 5. Generic Line Icons (no custom IconData)

**Detection**
- Regex: `Icon\(Icons\.(home|person|settings|search|notifications|favorite|share|arrow_back|more_vert)\)`
- Heuristics: Every icon in the app comes from `Icons.*`; no `IconData` custom instances; icons used for brand- specific concepts (logo, product feature, unique navigation).
- Visual: Standard Material outline icons that clash with a custom brand illustration style.

**Impact**
- Blends into every other Material app; destroys brand recognition.
- Custom features cannot be represented by generic icons (e.g., a "Swipe to Match" feature using `Icons.favorite` is ambiguous).
- Missed opportunity: custom icons compress better and can be animated.

**Flutter Fix**

```dart
// BAD: Generic Material icon for a product-specific feature
ListTile(
  leading: const Icon(Icons.favorite),
  title: const Text('Saved Matches'),
)
```

```dart
// GOOD: Custom IconData from a font-glyph or SVG sprite
class AppIcons {
  AppIcons._();
  static const _fontFamily = 'AppIcons';
  static const matches = IconData(0xe001, fontFamily: _fontFamily);
  static const swipe = IconData(0xe002, fontFamily: _fontFamily);
}

ListTile(
  leading: const Icon(AppIcons.matches),
  title: const Text('Saved Matches'),
)
```

**Prevention**
- Generate an icon font early in the project (use `flutter_iconpicker` or `icomoon`).
- Only use `Icons.*` for platform-standard actions (back, close, overflow menu).
- Ban `Icons.*` in design review for screens that represent brand-specific concepts.

---

### 6. Nested Cards (Card inside Card)

**Detection**
- Regex: `Card.*\n.*Card` or `Card.*child.*Card`
- Heuristics: Tree depth of 3+ with `Card → Column → Card → ListTile` or similar.
- Visual: Cards with `elevation` inside cards with `elevation`, creating competing shadows; rounded rectangles inside rounded rectangles.

**Impact**
- Visual hierarchy collapse — the user cannot tell which card is the container.
- Shadow conflicts produce muddy or uneven lighting.
- Material Design 3 explicitly discourages nested surfaces at the same elevation tier.

**Flutter Fix**

```dart
// BAD: Card inside Card with competing elevations
Card(
  elevation: 2,
  child: Column(
    children: [
      Card(
        elevation: 1,
        child: ListTile(title: Text('Sub-item')),
      ),
    ],
  ),
)
```

```dart
// GOOD: Single Card with semantic sections
Card(
  elevation: 2,
  child: Column(
    children: [
      Padding(
        padding: const EdgeInsets.all(16),
        child: Text('Section Title', style: Theme.of(context).textTheme.titleMedium),
      ),
      const Divider(height: 1),
      ListTile(title: Text('Sub-item')),
    ],
  ),
)
```

**Prevention**
- Rule: a `Card` must never be a descendant of another `Card`.
- Use `Divider`, `Padding`, and `SizedBox` to create visual sections within a single surface.
- If nesting is unavoidable (e.g., a feed of cards), ensure no inner card has elevation.

---

### 7. Random Glassmorphism (BackdropFilter with no depth system)

**Detection**
- Regex: `BackdropFilter.*filter.*ImageFilter\.blur` or `ClipRRect.*BackdropFilter`
- Heuristics: A frosted-glass panel that appears on an unrelated screen (e.g., a settings page); no other depth effects (shadows, elevation) are used in the app; `BackdropFilter` used inside a `Stack` with no fallback for non-GPU devices.
- Visual: Translucent blur overlay over a background image, often with a gradient border.

**Impact**
- Performance: `BackdropFilter` is one of the most expensive operations in Flutter; it causes off-screen renders and jank on mid-range devices.
- Inconsistency: a single frosted panel in an otherwise flat UI signals a copy-pasted component.
- Accessibility: reduced contrast on blurred text.

**Flutter Fix**

```dart
// BAD: Decorative glass panel with no performance consideration
Stack(
  children: [
    Image.network('https://picsum.photos/400'),
    Positioned(
      top: 100,
      child: ClipRRect(
        borderRadius: BorderRadius.circular(20),
        child: BackdropFilter(
          filter: ImageFilter.blur(sigmaX: 10, sigmaY: 10),
          child: Container(
            width: 300,
            height: 200,
            color: Colors.white.withOpacity(0.2),
          ),
        ),
      ),
    ),
  ],
)
```

```dart
// GOOD: Solid surface with theme-aware opacity; blur only if performance budget allows
Container(
  width: 300,
  height: 200,
  decoration: BoxDecoration(
    borderRadius: BorderRadius.circular(20),
    color: Theme.of(context).colorScheme.surfaceContainerHighest,
  ),
  child: /* content */,
)
```

**Prevention**
- Do not use `BackdropFilter` unless the product spec explicitly requires it and a performance budget has been allotted.
- Prefer `colorScheme.surfaceContainerHighest` with `withOpacity` for a similar visual at zero GPU cost.
- If `BackdropFilter` is necessary, guard it behind a `PlatformChecker` for low-end devices.

---

### 8. Template Names (Acme, Nova, Flow, Nexus, Smart, Pulse, Vibe)

**Detection**
- Regex: `\b(Acme|Nova|Flow|Nexus|Smart|Pulse|Vibe|Apex|Zenith|Vertex|Stratus|Lumina)\b`
- Heuristics: App name, sample data, or placeholder content using these generic startup nouns.
- Visual: "Welcome to Flow" as the onboarding title, "Nova Corp" in legal copy.

**Impact**
- Shipping with "Acme" or "Nova" in production text signals incomplete work.
- These names carry no brand meaning and may conflict with existing trademarks.
- Search-and-replace risk: developers forget to update all occurrences.

**Flutter Fix**

```dart
// BAD: Template name in sample data
const companyName = 'Nova Corp';
const appTitle = 'Pulse';
```

```dart
// GOOD: Descriptive placeholder that cannot ship
const companyName = '{COMPANY_NAME}';  // TODO: configure at build time
const appTitle = '{APP_NAME}';
```

**Prevention**
- Use `--dart-define` for app-wide strings so placeholder values crash the build if unset.
- Add a CI check: `grep -rE '(Acme|Nova|Flow|Nexus|Smart|Pulse|Vibe)' lib/` must return exit 1.
- Use `envied` or `.env` files for configuration rather than string literals.

---

### 9. AI Marketing Copy ("elevate", "unlock", "seamless", "next-gen")

**Detection**
- Regex: `\b(elevate|unlock|seamless(ly)?|next-gen(eration)?|revolutioniz(?:e|ing)|game-?changer|empower|supercharge|harness|delve|navigate|reimagine|streamline)\b`
- Heuristics: Headlines, CTAs, or body text using these words with no specific product detail.
- Visual: "Unlock your potential," "Elevate your workflow," "Seamless experience."

**Impact**
- Lowers conversion: generic copy is less persuasive than specific value propositions.
- Fails app store review guidelines if copy contains unsubstantiated claims ("revolutionary").
- Makes the app look like a template rather than a product.

**Flutter Fix**

```dart
// BAD: Marketing fluff
const cta = 'Unlock Your Potential';
const tagline = 'A seamless next-gen experience';
```

```dart
// GOOD: Specific, measurable copy
const cta = 'Start your free trial';
const tagline = 'Export Figma designs to Flutter in one click';
```

**Prevention**
- Run all copy through a linter that flags the regex above.
- Write copy first as user stories ("As a X, I want to Y so that Z").
- Have a real product marketer review AI-generated copy before it enters the codebase.

---

### 10. Fake-Precision Metrics (percentages without real data)

**Detection**
- Regex: `\d{2}\.\d+%` or `"\d+%"` in a `Text` widget that is not bound to a `ValueNotifier`, `Stream`, or state variable.
- Heuristics: Static strings containing percentages like `"87.4%"` or `"23.5%"` in a `Text` widget.
- Visual: A progress ring displaying `"73.2%"` with no input field or data source driving it.

**Impact**
- Dishonest — fake precision implies data-backed measurement.
- Static — the value never updates, contradicting any real-time expectation.
- Maintenance burden — someone must later find and replace these literals with real bindings.

**Flutter Fix**

```dart
// BAD: Fake-precision literal
Text('87.4%', style: theme.textTheme.headlineLarge)
```

```dart
// GOOD: Bound to actual data
ValueListenableBuilder<double>(
  valueListenable: viewModel.completionRate,
  builder: (context, rate, _) {
    return Text(
      '${(rate * 100).toStringAsFixed(1)}%',
      style: theme.textTheme.headlineLarge,
    );
  },
)
```

**Prevention**
- Ban percentage string literals in lint rules: any `%` in a string should be a format argument.
- Use `DecimalFormat` or `NumberFormat` for all numeric display.
- In development builds, overlay a "MOCK" badge on any hardcoded metric.

---

### 11. Generic Material Scaffold (Scaffold/AppBar/ListView with no product nav)

**Detection**
- Regex: `Scaffold\(.*appBar: AppBar\(.*title: Text\(.*\),\s*body: ListView\(`
- Heuristics: Every screen is `Scaffold → AppBar → ListView` or `Scaffold → AppBar → Center(Text(...))`.
- Visual: No `BottomNavigationBar`, `NavigationRail`, `Drawer`, `TabBar`, or `SliverAppBar`; no custom navigation beyond `Navigator.push`.

**Impact**
- Flat navigation structure confuses users — they cannot tell where they are in the app.
- Ignores platform idiom: iOS uses tab bars, Android uses nav rails/bottom nav.
- Scalability problem: as screens are added, the app lacks a navigation spine.

**Flutter Fix**

```dart
// BAD: Identical scaffold pattern on every screen
class HomeScreen extends StatelessWidget {
  @override
  Widget build(BuildContext context) => Scaffold(
    appBar: AppBar(title: const Text('Home')),
    body: ListView(children: [...]);
  );
}
```

```dart
// GOOD: Navigation shell separates layout from content
class AppShell extends StatelessWidget {
  const AppShell({super.key});

  @override
  Widget build(BuildContext context) {
    return Scaffold(
      body: Row(
        children: [
          if (MediaQuery.of(context).size.width > 600)
            const NavigationRail(
              destinations: [
                NavigationRailDestination(icon: Icon(Icons.home_outlined), label: Text('Home')),
                NavigationRailDestination(icon: Icon(Icons.explore_outlined), label: Text('Explore')),
                NavigationRailDestination(icon: Icon(Icons.person_outline), label: Text('Profile')),
              ],
            ),
          Expanded(child: _buildContent(context)),
        ],
      ),
      bottomNavigationBar: MediaQuery.of(context).size.width > 600
          ? null
          : NavigationBar(
              destinations: const [
                NavigationDestination(icon: Icon(Icons.home_outlined), label: 'Home'),
                NavigationDestination(icon: Icon(Icons.explore_outlined), label: 'Explore'),
                NavigationDestination(icon: Icon(Icons.person_outline), label: 'Profile'),
              ],
            ),
    );
  }
}
```

**Prevention**
- Define a navigation shell (adaptive `NavigationBar`/`NavigationRail`) before writing any content screen.
- Use `GoRouter` or `Beamer` with `ShellRoute` for persistent navigation.
- Review every scaffold for navigation context — users should always know "where am I?"

---

### 12. Hardcoded Spacing/Colors (EdgeInsets.all(16), Color(0xFF…))

**Detection**
- Regex: `EdgeInsets\.(all|symmetric|only)\([^)]*\)` (outside of a theme file) or `Color\(0x[Ff][0-9a-fA-F]{8}\)`
- Heuristics: `EdgeInsets.all(16)` repeats across 20+ files; `Color(0xFF…)` literals in widget build methods.
- Visual: Inconsistent padding between screens, colors that shift slightly when the theme is toggled.

**Impact**
- Maintenance nightmare: changing the global padding from 16 to 12 requires a project-wide diff.
- Theme switching fails — dark mode cannot override `Color(0xFF…)`.
- Design system drift: spacing values degrade into isolated exceptions.

**Flutter Fix**

```dart
// BAD: Hardcoded every time
Padding(
  padding: const EdgeInsets.all(16),
  child: Text('Content'),
)

Container(
  color: const Color(0xFF1A1A2E),
)
```

```dart
// GOOD: Theme-driven spacing and color
Padding(
  padding: EdgeInsets.all(Theme.of(context).visualDensity.effectiveSpacing(16)),
  child: Text('Content'),
)

Container(
  color: Theme.of(context).colorScheme.surface,
)
```

**Prevention**
- Define spacing constants in a single `Spacing` class (e.g., `Spacing.xs = 4`, `Spacing.md = 16`).
- Use `Theme.of(context).colorScheme` for all colors; never write `Color(0xFF…)` outside a `ThemeData` definition.
- Lint: flag `EdgeInsets.all(16)` in widget code (allow in a single `spacing.dart` file).

---

### 13. Inconsistent Border Radius (different values per component)

**Detection**
- Regex: `BorderRadius\.circular\((\d+)\)` where the captured number varies across components of the same type (cards: 8, 12, 16; buttons: 4, 8, 12).
- Heuristics: Cards have `BorderRadius.circular(8)` in one file, `BorderRadius.circular(16)` in another; buttons mix `8`, `12`, `4`.
- Visual: Rounding that feels arbitrary — some cards sharp, others pill-like.

**Impact**
- Visual noise: inconsistent radii make the UI feel unpolished.
- Design system gap: each radius should map to a token (small, medium, large).
- Accessibility: extreme rounding can distort focus indicators.

**Flutter Fix**

```dart
// BAD: Inconsistent per-file literals
Card(
  shape: RoundedRectangleBorder(borderRadius: BorderRadius.circular(12)),
)

// elsewhere...
Card(
  shape: RoundedRectangleBorder(borderRadius: BorderRadius.circular(8)),
)
```

```dart
// GOOD: Centralized radius tokens
class RadiusTokens {
  RadiusTokens._();
  static const sm = 4.0;
  static const md = 8.0;
  static const lg = 16.0;
}

Card(
  shape: RoundedRectangleBorder(borderRadius: BorderRadius.circular(RadiusTokens.md)),
)
```

**Prevention**
- Define 3–4 radius values in a tokens file.
- Lint: `BorderRadius.circular(N)` where `N` is not in `{4, 8, 16}` (or your token set).
- Use `Theme.of(context).cardTheme.shape` to set card radius globally.

---

### 14. Infinite Shimmer/Loops (infinite repeat animations)

**Detection**
- Regex: `\.repeat\(\)` or `\.periodic\(.*Duration\(\)` or `AnimationController.*infinite`
- Heuristics: `AnimationController` with `repeat()` for a shimmer that never stops; a `TweenAnimationBuilder` with `infinite` cycle; `Timer.periodic` for UI updates.
- Visual: Shimmer placeholders that continue animating after content loads; spinners that spin forever even after data arrives.

**Impact**
- Battery drain: GPU-bound infinite animations prevent the device from entering low-power states.
- Motion sickness: users with vestibular disorders react negatively to continuous motion.
- Distraction: animated elements fight for user attention against real content.

**Flutter Fix**

```dart
// BAD: Default shimmer that loops forever
class ShimmerWidget extends StatefulWidget {
  @override
  State<ShimmerWidget> createState() => _ShimmerWidgetState();
}

class _ShimmerWidgetState extends State<ShimmerWidget>
    with SingleTickerProviderStateMixin {
  late final AnimationController _controller;

  @override
  void initState() {
    super.initState();
    _controller = AnimationController(
      vsync: this,
      duration: const Duration(milliseconds: 1500),
    )..repeat();  // 🔴 never stops
  }

  @override
  void dispose() {
    _controller.dispose();
    super.dispose();
  }

  @override
  Widget build(BuildContext context) {
    return /* shimmer UI */;
  }
}
```

```dart
// GOOD: Shimmer that stops when content arrives, respects reduced motion
class ContentLoader extends StatefulWidget {
  const ContentLoader({required this.isLoading, required this.child, super.key});
  final bool isLoading;
  final Widget child;

  @override
  State<ContentLoader> createState() => _ContentLoaderState();
}

class _ContentLoaderState extends State<ContentLoader>
    with SingleTickerProviderStateMixin {
  late final AnimationController _controller;

  @override
  void initState() {
    super.initState();
    _controller = AnimationController(vsync: this, duration: const Duration(milliseconds: 1500));
    if (widget.isLoading) _controller.repeat();
  }

  @override
  void didUpdateWidget(ContentLoader oldWidget) {
    super.didUpdateWidget(oldWidget);
    if (widget.isLoading && !oldWidget.isLoading) {
      _controller.repeat();
    } else if (!widget.isLoading && oldWidget.isLoading) {
      _controller.stop();
    }
  }

  @override
  void dispose() {
    _controller.dispose();
    super.dispose();
  }

  @override
  Widget build(BuildContext context) {
    final motion = MediaQuery.of(context).disableAnimations;
    if (motion) return widget.child;  // respect reduced motion
    return widget.isLoading ? _shimmer() : widget.child;
  }
}
```

**Prevention**
- Never call `.repeat()` without a condition that stops it.
- Check `MediaQuery.of(context).disableAnimations` (iOS Reduce Motion, Android Remove Animations).
- Use `shimmer` package's built-in lifecycle management rather than custom controllers.

---

### 15. Hidden Route Transitions (>500ms, unclear direction)

**Detection**
- Regex: `PageRouteBuilder.*transitionsBuilder.*(Duration\(.*[6-9]\d{2}|Duration\(.*[12]\d{3})` or `transitionDuration.*Duration\(.*[6-9]\d{2}`
- Heuristics: Custom `PageRouteBuilder` with `transitionDuration` > 500ms; transitions that fade without a directional slide; mix of `CupertinoPageRoute` and custom routes.
- Visual: Routes that feel "sticky" or slow; disappearing/reappearing content without a spatial metaphor.

**Impact**
- User perception of slowness: any transition over 300ms feels sluggish on mobile.
- Disorientation: fade-only transitions (no slide) break the user's spatial map of the app.
- Platform inconsistency: Android uses 200–300ms; iOS uses 300–400ms.

**Flutter Fix**

```dart
// BAD: Slow, directionless route transition
Navigator.of(context).push(
  PageRouteBuilder(
    transitionDuration: const Duration(milliseconds: 800),
    pageBuilder: (_, __, ___) => const DetailScreen(),
    transitionsBuilder: (_, animation, __, child) =>
        FadeTransition(opacity: animation, child: child),
  ),
);
```

```dart
// GOOD: Fast, platform-appropriate transition
Navigator.of(context).push(
  CupertinoPageRoute(
    builder: (_) => const DetailScreen(),
  ),
);

// Or for Android:
Navigator.of(context).push(
  MaterialPageRoute(
    builder: (_) => const DetailScreen(),
  ),
);
```

**Prevention**
- Always use platform-native routes (`CupertinoPageRoute` / `MaterialPageRoute`) unless a spec demands custom transitions.
- If custom transitions are required, cap `transitionDuration` at 300ms.
- Provide a directional clue: slide-left for push, slide-right for pop.

---

### 16. Physics Mismatch (spring in finance, sharp in wellness)

**Detection**
- Regex: `SpringDescription\(` or `BouncingScrollPhysics` in an app where the content type doesn't match the physics.
- Heuristics: `BouncingScrollPhysics` on a finance or document-reading app; `ClampingScrollPhysics` on a playful wellness or social app; spring animation used for a chart update.
- Visual: Overscroll glow/bounce on a spreadsheet-like screen; stiff scroll on a photo gallery.

**Impact**
- Feels wrong: physics carry semantic weight — bouncing says "playful," clamping says "precise."
- Platform violation: iOS defaults to bouncing; Android defaults to clamping. Mixing them without intent confuses users.
- Accessibility: bouncy physics can be disorienting for users with motion sensitivity.

**Flutter Fix**

```dart
// BAD: Bouncing physics on a finance portfolio screen
ListView.builder(
  physics: const BouncingScrollPhysics(),
  itemCount: transactions.length,
  itemBuilder: (_, i) => TransactionTile(transaction: transactions[i]),
)
```

```dart
// GOOD: Physics matched to app personality + platform
class AppScrollPhysics {
  /// Financial/privacy apps → precise, no bounce
  static const precise = ClampingScrollPhysics();

  /// Social/wellness/creative apps → playful bounce
  static const playful = BouncingScrollPhysics();
}

ListView.builder(
  physics: AppScrollPhysics.precise,
  itemCount: transactions.length,
  itemBuilder: (_, i) => TransactionTile(transaction: transactions[i]),
)
```

**Prevention**
- Define an `AppScrollPhysics` enum or class in the design system.
- Match physics to brand personality: finance/tools → `ClampingScrollPhysics`, social/wellness → `BouncingScrollPhysics`.
- Never leave `physics` unset if the default platform physics would contradict the brand tone.

---

## Lint Rules

Add these custom lint rules to `analysis_options.yaml`:

```yaml
# analysis_options.yaml — Anti-Slop Lint Rules
custom_lint:
  rules:
    - avoid_generic_gradient:
        description: Flag hardcoded purple-blue gradients not sourced from ColorScheme.
        severity: warning
        selector: |
          MethodInvocation
            [targetName='LinearGradient']
            [argumentList//StringLiteral
              [@value=/purple|blue|deepPurple|indigo/i]]

    - avoid_inline_chart_data:
        description: Ban Random() or hardcoded lists used as chart data.
        severity: error
        selector: |
          MethodInvocation
            [targetName='Random']
            [../..//InstanceCreationExpression
              [typeName='LineChartBarData' or typeName='BarChartGroupData']]

    - avoid_nested_card:
        description: Card descendant of another Card.
        severity: error
        selector: |
          InstanceCreationExpression
            [typeName='Card']
            [.//InstanceCreationExpression[typeName='Card']]

    - avoid_template_names:
        description: Flag placeholder brand names (Acme, Nova, etc.).
        severity: error
        selector: |
          StringLiteral
            [@value=/Acme|Nova|Flow|Nexus|Smart|Pulse|Vibe|Apex/i]

    - avoid_hardcoded_spacing:
        description: Flag EdgeInsets.all(16) outside designated tokens file.
        severity: warning
        selector: |
          MethodInvocation
            [targetName='EdgeInsets']
            [argumentList//NumericLiteral]

    - avoid_infinite_repeat:
        description: Flag .repeat() on AnimationController without a stop condition.
        severity: error

    - avoid_fake_percentage:
        description: Flag string literals containing percentages not bound to state.
        severity: warning
        selector: |
          StringLiteral
            [@value=/\d+\.\d+%/]

    - prefer_theme_colors:
        description: Ban Color(0xFF…) literals outside theme definitions.
        severity: error
```

For teams using `custom_lint` or `dart_code_metrics`, adapt the selectors to your rule engine. These rules are illustrative — adjust selectors to match your Flutter version and lint tooling.

---

## Prevention Strategies

### Design Before Code

- Generate a design token spec (colors, spacing, radii, elevation, iconography) before writing any widget code.
- Create a "slop budget": at most 2 generated patterns per screen; flag screens that exceed it.
- Use design-to-code handoff tools that enforce token usage (e.g., Supernova, Specify).

### AI Prompt Engineering

- Never prompt "Create a Flutter dashboard." Instead: "Create a Flutter dashboard for a fintech app. Use ColorScheme.fromSeed with brand hex #1A365D. No charts unless data source is provided. Use ClampingScrollPhysics."
- Include anti-patterns in system prompts: "Do not use LinearGradient with purple/blue. Do not use Card inside Card. Do not generate fake percentage metrics. Use theme tokens for all spacing and color."
- Append a constraints block to every code generation prompt:
  ```
  CONSTRAINTS:
  - No hardcoded Color(0xFF…)
  - No EdgeInsets literals
  - No generic onboarding slides
  - No purple-blue gradients
  - All strings must be in arb/i18n files
  ```

### Code Review Checklist

For every AI-generated PR, verify:

- [ ] No purple-blue gradients in widget code
- [ ] No `Random()` or inline decimal lists used as chart/display data
- [ ] No `Card` descendant of another `Card`
- [ ] No `BackdropFilter` without a performance budget
- [ ] No template/buzzword names (Acme, Nova, Flow, etc.)
- [ ] No marketing fluff copy ("elevate", "unlock", "seamless", "next-gen")
- [ ] No fake-precision percentage strings
- [ ] No `EdgeInsets.all(N)` or `Color(0xFF…)` outside theme files
- [ ] Border radius values match a token set (not arbitrary)
- [ ] No infinite `.repeat()` shimmer/animations
- [ ] Route transitions ≤ 400ms with directional clue
- [ ] Scroll physics match brand personality
- [ ] Navigation shell is used (not bare Scaffold everywhere)

### Tooling

- Add a `pre-push` git hook that runs `grep -E` for the regex patterns listed under Detection above.
- Run `custom_lint` rules in CI with a slop budget threshold (fail if >5 warnings).
- Use `dart run build_runner` to generate token-aware widgets that cannot accept raw `Color` or `EdgeInsets`.

---

## Conclusion

The 16 patterns in this registry share a root cause: code generated without a design system. An AI model does not know your brand color, your spacing philosophy, your platform target, or your data model — so it invents plausible defaults.

Fixing slop is not about banning AI tools. It is about:

1. **Defining tokens first** — colors, spacing, radius, physics, navigation pattern.
2. **Tightening lint rules** — make the compiler enforce the design system.
3. **Reviewing with a checklist** — treat AI-generated code as a draft, not a final artifact.
4. **Improving prompts** — encode constraints explicitly rather than hoping the model "knows."

When a Flutter codebase passes all 16 checks, it is no longer a template. It is a product.

---

*Maintain this registry as a living document. Add new patterns as AI generation capabilities evolve. The goal is not to eliminate all generics but to raise the floor so that generated code is indistinguishable from hand-crafted code in a mature design system.*
