# Flutter Art Direction

An agent-agnostic skill for designing and implementing Flutter apps that feel authored, app-native, emotionally intentional, visually distinct, and free of obvious AI-generated slop.

The skill is reference-inspired, not app-copying. It distills reusable design principles from strong mobile apps and applies them to new Flutter app screens and flows based on the user's actual brief.

## Contents

- `flutter-art-direction/SKILL.md` - portable workflow for Codex, Claude, and other skill-compatible AI coding agents.
- `flutter-art-direction/references/principle-bank.md` - distilled app-design principles inspired by Wonderous, Reflectly, Gentler Streak, and broader mobile app research.
- `flutter-art-direction/references/flutter-implementation-playbook.md` - concrete Flutter patterns for translating the Design Bible into theme tokens, widgets, motion, assets, adaptive layouts, previews, screenshots, and visual QA.
- `flutter-art-direction/agents/openai.yaml` - optional Codex UI metadata.

## Core Ideas

- Start with a Flutter Design Read before implementation.
- Lock a Design Bible: platform mode, product world, emotional stance, palette, typography, spacing, assets, motion, navigation, and state design.
- Treat Material and Cupertino as implementation substrates, not the whole identity.
- Use official Flutter architecture, responsive layout, preview, routing, localization, and testing guidance where relevant.
- Require preview or screenshot-based QA for visual work.
