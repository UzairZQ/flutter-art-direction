# Motion With Intent for Flutter

> **Optional deep-dive.** The compact reference (5-category table, spring physics, choreography rules) is in `SKILL.md` section 6. Read this file when you need detail on route transition choreography, staggered animation patterns, or platform-specific spring differences.

## Overview
Every animation must serve a purpose. Map to one of 5 categories.

## Five Motion Categories

### 1. Navigational
Purpose: Show spatial relationships (push/pop, tab switch, sheet, shared element)
Max Duration: 300ms
Spring: SpringDescription(mass: 1, stiffness: 210, damping: 20)
Flutter: Hero, PageRouteBuilder, AnimatedSwitcher with shared-axis

### 2. Feedback
Purpose: Confirm action received (press, toggle, swipe, haptic)
Max Duration: 150ms
Spring: SpringDescription(damping: 15)
Flutter: HapticFeedback, InkWell splash, AnimatedContainer for button states
Reduce-motion: Duration.zero

### 3. State Transition
Purpose: Explain data/state change (loading → success, empty → populated)
Max Duration: 250ms
Spring: SpringDescription(stiffness: 180)
Flutter: AnimatedSwitcher, TweenAnimationBuilder, AnimatedCrossFade
Reduced-motion: Fade only

### 4. Emotional/Storytelling
Purpose: Reveal narrative (onboarding, celebration, empty state delight)
Max Duration: 400-600ms
Spring: Custom choreography (staggered, sequenced)
Flutter: StaggeredAnimation, flutter_animate chains, Lottie/Rive
Reduced-motion: Static end state only

### 5. Brand/Signature
Purpose: Memorable moment (splash, logo transition, signature micro-interaction)
Max Duration: <2000ms (one-time)
Spring: Brand-specific
Flutter: CustomPainter animation, Rive animation
Reduced-motion: Skip entirely

## Choreography Rules
- Max 2 concurrent motions per screen
- Stagger children: delay = index × 50ms
- Parent completes before children
- Exit in parallel (fast)
- Reduced-motion: always provide path

## Spring Physics
| Feeling | Stiffness | Damping | 
| Crisp/Snappy | 300 | 25 |
| Standard | 210 | 20 |
| Soft/Bouncy | 150 | 12 |
| Loose/Expressive | 100 | 8 |

## Implementation Pattern
```dart
final disableAnimations = MediaQuery.of(context).disableAnimations;
final duration = disableAnimations ? Duration.zero : AppMotion.mediumSpring.duration;
```

## Anti-Slop
- No infinite shimmer/loops
- No decorative animation
- No motion that makes content unreachable with reduced motion
- No route transitions that hide destination
