# Accessibility Gates for Flutter

## Overview
Accessibility is a design constraint, not a checklist. These are CI-blocking gates.

## Gate 1: Reduced Motion
- MediaQuery.of(context).disableAnimations respected everywhere
- No infinite loops without user control
- Reduced-motion path: Duration.zero, opacity-only, static end state
- Test: flutter test with disabled animations

## Gate 2: Dynamic Type / Text Scaling
- MediaQuery.textScaler tested at 1.0, 1.5, 2.0
- No clipping at any scale
- Use FittedBox only for single-line labels
- Avoid hardcoded font sizes: use TextTheme styles

## Gate 3: VoiceOver / TalkBack Semantics
- Every interactive element has Semantics label
- ExcludeSemantics for decorative elements
- MergeSemantics for compound widgets
- SemanticsService.announce for live region updates

## Gate 4: Color Contrast
- WCAG AA: 4.5:1 normal text, 3:1 large text
- APCA preferred for modern apps
- Test with WAVE or axe DevTools
- No text on images without scrim/overlay

## Gate 5: Touch Targets
- iOS: 44x44pt minimum
- Android/Material: 48x48dp minimum
- Primary controls: larger (56x56dp preferred)
- Test: visual inspection of tap areas

## Gate 6: Focus Order
- Logical tab order for keyboard navigation
- FocusTraversalGroup for modal containment
- No focus traps
- Visible focus indicator on all interactive elements

## Implementation Checklist
[ ] MediaQuery.disableAnimations respected
[ ] MediaQuery.textScaler at 2.0 works
[ ] Semantics labels on all icon buttons
[ ] ExcludeSemantics for decorative images
[ ] MergeSemantics for card+button
[ ] FocusTraversalGroup in modals
[ ] Contrast validated (4.5:1+)
[ ] Touch targets 44-48dp+
[ ] Golden tests at 200% text scale + reduced motion

## CI Pipeline Integration
GitHub action or flutter test that runs a11y checks.
