# Forward-Test Rubric

Score each dimension from 0 to 2.

- **0:** missing or contradicted
- **1:** present but generic, incomplete, or weakly connected to the brief
- **2:** specific, coherent, and actionable

## Required Dimensions

1. **Product reading:** identifies audience, job, context, real data, and constraints.
2. **Flutter Design Read:** names platform stance, product world, emotional stance, and signature idea.
3. **Dials:** chooses all six values and uses them consistently.
4. **Design Bible:** covers hierarchy, palette, typography, shape, assets, motion, navigation, states, and performance.
5. **Authorship:** produces a product-specific mechanism that survives a logo swap test.
6. **Reference translation:** extracts principles without copying layout, branding, subject matter, or assets.
7. **App-native flow:** preserves mobile navigation, back, scrolling, safe areas, keyboard, and reachability.
8. **Motion score:** defines trigger, continuity, purpose, control, interruption, reduced motion, and cost.
9. **Flutter tool choice:** uses the lowest sufficient built-in or package capability and checks project compatibility.
10. **Complete states:** includes realistic loading, empty, error, permission, long-content, and interaction states where relevant.
11. **Accessibility:** addresses semantics, target size, contrast, text scaling, gesture alternatives, and reduced motion.
12. **Performance:** identifies likely rebuild, repaint, image, filter, shader, or particle cost and proposes profile-mode verification.
13. **Anti-slop reasoning:** catches repeated defaults without blindly banning valid brand choices.
14. **Rendered QA:** plans previews, screenshots, device checks, and motion inspection appropriate to risk.
15. **Repository respect:** preserves existing architecture and unrelated behavior in redesign prompts.

## Pass Conditions

- No dimension scores 0.
- Product reading, authorship, app-native flow, accessibility, and rendered QA must score 2.
- Total score is at least 25 out of 30.
- Any fabricated product data, copied reference design, inaccessible gesture-only action, or unverified claim of visual completion is an automatic fail.
