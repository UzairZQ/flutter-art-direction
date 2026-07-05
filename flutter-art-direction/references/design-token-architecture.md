# Design Token Architecture for Flutter

> **Optional deep-dive.** The compact reference (3-tier structure, banned patterns, platform adaptation) is in `SKILL.md` section 4. Read this file when you need the full code generation pipeline, `ThemeExtension` patterns, or platform-specific token overrides.

## Overview
Design tokens are the single source of truth for visual properties. Three tiers: Primitives → Semantic → Component.

## Three-Tier Structure

### Tier 1: Primitives (Raw Values)
Context-independent raw values.

File structure:
lib/ui/core/tokens/primitives/
  color-primitives.dart
  spacing-primitives.dart
  typography-primitives.dart
  motion-primitives.dart
  radius-primitives.dart
  shadow-primitives.dart

Examples:
- spacing-0 (0px), spacing-1 (4px), spacing-2 (8px)... spacing-24 (96px)
- colors: neutral-0 through neutral-1000, brand-50 through brand-900
- typography: font sizes, weights, line-heights
- motion: duration-fast (150ms), duration-medium (250ms), duration-slow (400ms)
- radius: radius-4, radius-8, radius-12, radius-16, radius-pill (9999)

### Tier 2: Semantic (Context-Aware)
Theme-adaptive roles referencing primitives.

File structure:
lib/ui/core/tokens/semantic/
  colors.dart
  spacing.dart
  typography.dart
  motion.dart

Examples:
- surfaceBase, surfaceRaised, surfaceMuted
- accentPrimary, accentSoft, danger, success
- textHeadline, textBody, textCaption
- spaceCardPadding, spaceSectionGap, spacePageMargin
- motionFast, motionMedium, motionSlow

### Tier 3: Component (Component-Specific)
Component-scoped overrides.

File structure:
lib/ui/core/tokens/component/
  button-tokens.dart
  card-tokens.dart
  input-tokens.dart
  navigation-tokens.dart

## Code Generation Pipeline

Source: tokens/source/figma-tokens.json
Transform: scripts/generate_tokens.dart
Output: lib/ui/core/tokens/ (committed)

## Usage Rules
- NEVER hardcode raw values in widget code
- ALWAYS use semantic tokens in component code
- Use component tokens for component-specific overrides

## Platform Adaptation
- radius adapts: M3 (16dp) vs iOS (12dp)
- navigation adapts: NavigationBar vs CupertinoTabBar

## Anti-Slop
- No hardcoded EdgeInsets.all(x)
- No Color(0xFF...) in widgets
- No BorderRadius.circular(different values)
