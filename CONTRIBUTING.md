# Contributing

Contributions that make Flutter interfaces more authored, usable, accessible, or technically sound are welcome.

## Before Opening a Change

- Keep the main `SKILL.md` concise and agent-agnostic.
- Put detailed or version-specific material in a directly linked reference.
- Prefer official Flutter, Android, Material, and Apple sources for platform claims.
- Mark open-source implementation lessons as observed patterns, not universal rules.
- Treat app references as inspiration. Do not contribute copied layouts, assets, branding, or proprietary motion.
- Write heuristics as contextual guidance. Avoid universal bans unless the framework or accessibility requirement is genuinely universal.
- Do not add a package preference without checking maintenance, license, platform support, and built-in alternatives.

## Validation

Run:

```bash
python3 ~/.codex/skills/.system/skill-creator/scripts/quick_validate.py \
  flutter-art-direction
python3 flutter-art-direction/scripts/audit_flutter_ui.py /path/to/a/flutter/project
```

Forward-test meaningful workflow changes with `evals/prompts.md` and score them with `evals/rubric.md`.

## Pull Requests

Describe:

- the problem the change solves
- source or implementation evidence
- which files changed and why
- validation and forward-test results
- any version-dependent claim that needs future review
