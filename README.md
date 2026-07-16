# Flutter Art Direction

An agent-agnostic skill for designing and implementing Flutter apps that feel authored, app-native, emotionally intentional, and visually distinct.

The skill is reference-inspired, not app-copying. It combines product-specific art direction with Flutter-native motion, adaptive behavior, accessibility, rendering discipline, and screenshot-based QA.

## What It Changes

Most Flutter skills answer how to structure, route, test, or fetch data. This skill focuses on a different problem:

- infer a visual and emotional direction from the real product
- create a compact Design Bible and one ownable signature idea
- translate ambitious web-style choreography into touch-first mobile behavior
- apply layered scenes, direct gesture progress, Hero continuity, slivers, custom painting, shaders, Rive, or particles only when they serve the product
- catch repeated AI defaults without banning legitimate styles
- verify the result in previews, screenshots, accessibility checks, and profile-mode motion

Wonderous is a major implementation reference, alongside Flutter 3.44 documentation, Material and Android guidance, Apple HIG, TasteSkill, UI UX Pro Max, and strong consumer app patterns.

## Package

```text
flutter-art-direction/
  SKILL.md
  agents/
    openai.yaml
  references/
    anti-slop-and-qa.md
    flutter-2026.md
    flutter-implementation-playbook.md
    motion-and-scroll.md
    principle-bank.md
    source-notes.md
  scripts/
    audit_flutter_ui.py
evals/
  prompts.md
  rubric.md
  results-2026-07-16.md
```

`SKILL.md` stays portable across Codex, Claude, and other skill-compatible agents. `agents/openai.yaml` is optional Codex metadata.

## Install

### Codex

```bash
python3 ~/.codex/skills/.system/skill-installer/scripts/install-skill-from-github.py \
  --repo UzairZQ/flutter-art-direction \
  --path flutter-art-direction
```

Restart Codex after installation.

### Claude Code

Clone the repository and place the `flutter-art-direction` folder in either:

- `~/.claude/skills/flutter-art-direction` for a personal install
- `.claude/skills/flutter-art-direction` for a project install

Other skill-compatible agents can use the same folder and `SKILL.md`.

## Use

Invoke the skill explicitly:

```text
$flutter-art-direction Build a reflective journaling flow with a calm,
non-judgmental stance and one tactile signature interaction.
```

The agent should begin with a Flutter Design Read, dials, a Design Bible, a signature idea, and a motion score before implementation.

## Static Audit

The included audit is advisory. It finds code patterns worth reviewing but does not pretend to judge design automatically.

```bash
python3 flutter-art-direction/scripts/audit_flutter_ui.py /path/to/flutter-project
python3 flutter-art-direction/scripts/audit_flutter_ui.py /path/to/flutter-project --json
```

## Validate

```bash
python3 ~/.codex/skills/.system/skill-creator/scripts/quick_validate.py \
  flutter-art-direction
```

Use the prompts and rubric in `evals/` for forward tests after meaningful changes.

## Principles

- Product truth before aesthetic.
- One signature idea before many effects.
- Native behavior before custom spectacle.
- Direct manipulation before canned motion.
- Material and Cupertino as substrates, not identity.
- References as mechanisms, not templates.
- Accessibility and reduced motion as design inputs.
- Profile expensive visuals on target hardware.
- Rendered QA before claims of completion.

## License

MIT. See `LICENSE`.
