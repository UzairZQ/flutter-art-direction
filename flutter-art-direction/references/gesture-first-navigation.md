# Gesture-First Navigation for Flutter

## Overview
Mobile interactions should prioritize finger gestures over button-centric flows.

## Core Gesture Table
| Gesture | Action | Affordance | Fallback |
|---------|--------|------------|----------|
| Edge swipe left | Back | System gesture + optional < | Back button |
| Drag down | Dismiss sheet | Drag handle + scrim | Close button |
| Long press | Peek/preview | Haptic + scale | Context menu |
| Swipe horizontal | Delete/archive | Reveal actions | Trailing button |
| Pull down | Refresh | Spinner hint | Menu action |
| Pinch | Zoom | Two-finger hint | Double-tap zoom |

## Implementation Patterns
- PopScope for back gesture (works with go_router)
- Dismissible for swipe-to-delete
- DraggableScrollableSheet for sheets
- GestureDetector with onLongPressStart for peek

## Discoverability
- First-time use: brief contextual tutorial
- Visual affordances: drag handle, chevron, hint text
- Reduced motion: disable gesture animations
- Accessibility: provide button alternatives for all gestures

## Platform Conventions
- iOS: edge swipe back, swipe-to-go-back
- Android 14+: predictive back animation
- Cross: PopScope for both platforms
