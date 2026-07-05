# Emotional Design Framework for Flutter

> **Optional deep-dive.** The compact reference is in `SKILL.md` section 3. Read this file when you need detailed stance mapping, before/after code examples, or implementation checklist for a specific emotional stance.

## Overview

Don Norman's three levels of emotional design applied to mobile interfaces.

## The Three Levels

### Visceral (Immediate Aesthetic)
- First 500ms: color, shape, texture, motion, imagery
- Flutter: ThemeData, hero imagery, initial motion choreography
- Tokens, typography, spacing, radius all contribute to visceral
- Code pattern: Theme.of(context), AppColors, Hero transitions

### Behavioral (Usability & Flow)
- How it works: navigation, feedback, state transitions, gesture ergonomics
- Flutter: NavigationBar, HapticFeedback, AnimatedSwitcher, loading/empty/error states
- Focus: task completion speed, error recovery, undo, confirmation
- Code pattern: AnimatedContainer, GestureDetector, Dismissible

### Reflective (Meaning & Memory)
- After using: identity, storytelling, shareability, trust
- Flutter: EmptyState, Onboarding flow, MilestoneCelebration, ShareCard
- Focus: brand memory, personalization, progress narrative
- Code pattern: AnimatedDefaultTextStyle, custom painting

## Emotional Stance → Token Mapping Table

| Stance | Visceral | Behavioral | Reflective |
|--------|----------|------------|------------|
| Calming | Soft palette, organic shapes, slow motion | Gentle transitions, no harsh errors | "Take your time" copy, breathing room |
| Encouraging | Warm accent, progress glow | Micro-celebrations, streak-aware | "You're building a habit" reflection |
| Precise | High contrast, geometric, crisp motion | Instant feedback, keyboard shortcuts | "You're in control" transparency |
| Playful | Bright palette, bounce, surprise | Drag-to-discover, haptic rewards | "You discovered X" share moments |
| Protective | Muted, safe colors, clear boundaries | Explicit confirmations, undo everywhere | "Your data stays yours" trust signals |

## Implementation Checklist

Per screen, verify all 3 levels:
- Visceral: Color, shape, motion evoke intended feeling
- Behavioral: Navigation, feedback, states work intuitively
- Reflective: Copy, empty/error states, milestones resonate

## Anti-Slop: Emotional Design Failures

- Visceral-only: Pretty but unusable
- Behavioral-only: Works fine, feels cold
- Reflective-only: Story without substance
- All three disconnected: Emotionally incoherent
