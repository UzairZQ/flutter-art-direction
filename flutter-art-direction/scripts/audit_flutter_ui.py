#!/usr/bin/env python3
"""Advisory static audit for common Flutter UI design and motion risks."""

from __future__ import annotations

import argparse
import json
import re
import sys
from dataclasses import asdict, dataclass
from pathlib import Path
from typing import Iterable


SEVERITY_ORDER = {"info": 0, "low": 1, "medium": 2, "high": 3}
GENERATED_SUFFIXES = (
    ".g.dart",
    ".freezed.dart",
    ".gr.dart",
    ".mocks.dart",
    ".config.dart",
)


@dataclass(frozen=True)
class Finding:
    rule: str
    severity: str
    path: str
    line: int
    message: str
    excerpt: str


@dataclass(frozen=True)
class PatternRule:
    rule: str
    severity: str
    pattern: re.Pattern[str]
    message: str


PATTERN_RULES = (
    PatternRule(
        "invented-percentage",
        "high",
        re.compile(r"""Text\s*\(\s*(?:const\s+)?[rR]?['"][^'"]*\d+(?:\.\d+)?\s*%"""),
        "Static percentage in visible text may be invented or disconnected from state.",
    ),
    PatternRule(
        "empty-marketing-copy",
        "medium",
        re.compile(
            r"""[rR]?['"][^'"]*\b(?:unlock|elevate|seamless|next[- ]gen|revolutionize|supercharge)\b""",
            re.IGNORECASE,
        ),
        "Generic marketing language deserves a product-specific copy review.",
    ),
    PatternRule(
        "placeholder-brand",
        "medium",
        re.compile(
            r"""[rR]?['"][^'"]*\b(?:Acme|Nova|Nexus|SmartFlow|Cloudly|Lumina)\b""",
            re.IGNORECASE,
        ),
        "Template-like brand name found in a visible string or fixture.",
    ),
    PatternRule(
        "expensive-save-layer-clip",
        "high",
        re.compile(r"Clip\.antiAliasWithSaveLayer"),
        "This clip requests an offscreen layer; verify the effect and profile raster cost.",
    ),
    PatternRule(
        "generic-product-widget-name",
        "low",
        re.compile(r"class\s+(?:HomeCard|InfoBox|FeatureTile|FancyCard)\b"),
        "Generic widget name may hide product meaning and encourage template composition.",
    ),
)


def line_number(text: str, offset: int) -> int:
    return text.count("\n", 0, offset) + 1


def excerpt_for(text: str, offset: int, limit: int = 120) -> str:
    start = text.rfind("\n", 0, offset) + 1
    end = text.find("\n", offset)
    if end == -1:
        end = len(text)
    excerpt = " ".join(text[start:end].strip().split())
    return excerpt[:limit]


def add_finding(
    findings: list[Finding],
    *,
    rule: str,
    severity: str,
    path: Path,
    root: Path,
    text: str,
    offset: int,
    message: str,
) -> None:
    findings.append(
        Finding(
            rule=rule,
            severity=severity,
            path=str(path.relative_to(root)),
            line=line_number(text, offset),
            message=message,
            excerpt=excerpt_for(text, offset),
        )
    )


def dart_files(project: Path) -> Iterable[Path]:
    roots = [candidate for candidate in (project / "lib", project / "test") if candidate.exists()]
    if not roots:
        roots = [project]
    for root in roots:
        for path in root.rglob("*.dart"):
            if path.name.endswith(GENERATED_SUFFIXES):
                continue
            if any(part in {".dart_tool", "build"} for part in path.parts):
                continue
            yield path


def scan_file(path: Path, root: Path) -> list[Finding]:
    text = path.read_text(encoding="utf-8", errors="replace")
    findings: list[Finding] = []

    for rule in PATTERN_RULES:
        for match in rule.pattern.finditer(text):
            add_finding(
                findings,
                rule=rule.rule,
                severity=rule.severity,
                path=path,
                root=root,
                text=text,
                offset=match.start(),
                message=rule.message,
            )

    normalized_path = path.as_posix().lower()
    theme_file = any(
        part in normalized_path
        for part in (
            "/theme/",
            "/themes/",
            "/styles/",
            "/tokens/",
            "theme.dart",
            "colors.dart",
        )
    )

    raw_colors = list(re.finditer(r"\bColor\s*\(\s*0x[0-9a-fA-F]{8}\s*\)", text))
    if len(raw_colors) >= 4 and not theme_file:
        add_finding(
            findings,
            rule="repeated-raw-colors",
            severity="medium",
            path=path,
            root=root,
            text=text,
            offset=raw_colors[0].start(),
            message=f"{len(raw_colors)} raw colors in one non-theme file; review semantic theme roles.",
        )

    raw_spacing = list(
        re.finditer(
            r"EdgeInsets\.(?:all|symmetric|only)\s*\([^\n;]*\b\d+(?:\.\d+)?",
            text,
        )
    )
    if len(raw_spacing) >= 7 and not theme_file:
        add_finding(
            findings,
            rule="repeated-raw-spacing",
            severity="low",
            path=path,
            root=root,
            text=text,
            offset=raw_spacing[0].start(),
            message=f"{len(raw_spacing)} literal spacing declarations; check for a repeated spacing role.",
        )

    controller_match = re.search(
        r"(?:\bAnimationController\s*\(|"
        r"\b(?:late\s+)?(?:final\s+)?AnimationController\s+\w+)",
        text,
    )
    if controller_match and not re.search(r"\.dispose\s*\(\s*\)", text):
        add_finding(
            findings,
            rule="animation-controller-disposal",
            severity="high",
            path=path,
            root=root,
            text=text,
            offset=controller_match.start(),
            message="AnimationController found without an obvious dispose call in the same file.",
        )

    repeat_match = re.search(r"\.repeat\s*\(", text)
    if repeat_match and not re.search(
        r"disableAnimations|reduceMotion|reducedMotion|TickerMode|VisibilityDetector|maybeAnimate",
        text,
        re.IGNORECASE,
    ):
        add_finding(
            findings,
            rule="unbounded-repeating-motion",
            severity="high",
            path=path,
            root=root,
            text=text,
            offset=repeat_match.start(),
            message="Repeating animation has no obvious reduced-motion or visibility policy in this file.",
        )

    random_match = re.search(r"\b(?:Random\s*\(|rnd\s*\()", text)
    if random_match:
        chart_context = re.search(
            r"\b(?:fl_chart|Chart|Series|dashboard|metric)\b",
            text,
            re.IGNORECASE,
        )
        procedural_context = re.search(
            r"\b(?:Particle|CustomPainter|Canvas|shader|texture)\b",
            text,
            re.IGNORECASE,
        )
        if chart_context:
            random_rule = "random-ui-data"
            random_severity = "high"
            random_message = (
                "Randomness appears near chart or metric code; verify that visible data is not fabricated."
            )
        elif procedural_context:
            random_rule = "procedural-randomness-review"
            random_severity = "info"
            random_message = (
                "Procedural visual randomness found; verify deterministic tests, bounded lifetime, and performance."
            )
        else:
            random_rule = "random-visible-output"
            random_severity = "medium"
            random_message = (
                "Randomness can make visible output unstable; confirm that it is intentional and not fake product data."
            )
        add_finding(
            findings,
            rule=random_rule,
            severity=random_severity,
            path=path,
            root=root,
            text=text,
            offset=random_match.start(),
            message=random_message,
        )

    animated_tokens = len(
        re.findall(
            r"\b(?:AnimationController|AnimatedBuilder|TweenAnimationBuilder|"
            r"AnimatedSwitcher|Hero|FragmentProgram|ParticleField)\b",
            text,
        )
    )
    if animated_tokens >= 4 and not re.search(
        r"disableAnimations|reduceMotion|reducedMotion", text, re.IGNORECASE
    ):
        first = re.search(
            r"\b(?:AnimationController|AnimatedBuilder|TweenAnimationBuilder|"
            r"AnimatedSwitcher|Hero|FragmentProgram|ParticleField)\b",
            text,
        )
        assert first is not None
        add_finding(
            findings,
            rule="motion-policy-review",
            severity="medium",
            path=path,
            root=root,
            text=text,
            offset=first.start(),
            message="Motion-heavy file has no obvious reduced-motion policy; verify it is supplied by an ancestor.",
        )

    backdrop_match = re.search(r"\bBackdropFilter\s*\(", text)
    if backdrop_match and not re.search(r"\bClip(?:Rect|RRect|Path)\s*\(", text):
        add_finding(
            findings,
            rule="unbounded-backdrop-filter",
            severity="medium",
            path=path,
            root=root,
            text=text,
            offset=backdrop_match.start(),
            message="BackdropFilter has no obvious local clip; verify that the filtered area is bounded.",
        )

    for match in re.finditer(r"\b(?:ShaderMask|ImageFilter\.|ColorFilter\.)", text):
        add_finding(
            findings,
            rule="rendering-cost-review",
            severity="info",
            path=path,
            root=root,
            text=text,
            offset=match.start(),
            message="Advanced rendering primitive found; inspect saveLayer, backend support, and raster cost.",
        )

    single_scroll = re.search(r"\bSingleChildScrollView\s*\(", text)
    nested_scroll = re.search(r"\b(?:ListView|GridView|CustomScrollView)\s*(?:\.|\()", text)
    if single_scroll and nested_scroll:
        add_finding(
            findings,
            rule="nested-scroll-review",
            severity="medium",
            path=path,
            root=root,
            text=text,
            offset=single_scroll.start(),
            message="SingleChildScrollView and another scrollable share a file; inspect constraints and gesture behavior.",
        )

    intrinsic_match = re.search(r"\bIntrinsic(?:Height|Width)\s*\(", text)
    lazy_collection = re.search(r"\b(?:ListView|GridView|SliverList|SliverGrid)\b", text)
    if intrinsic_match and lazy_collection:
        add_finding(
            findings,
            rule="intrinsic-scroll-layout",
            severity="medium",
            path=path,
            root=root,
            text=text,
            offset=intrinsic_match.start(),
            message="Intrinsic layout near a collection can add extra layout passes; profile or simplify.",
        )

    card_count = len(re.findall(r"\bCard\s*\(", text))
    if card_count >= 6:
        first_card = re.search(r"\bCard\s*\(", text)
        assert first_card is not None
        add_finding(
            findings,
            rule="card-density-review",
            severity="low",
            path=path,
            root=root,
            text=text,
            offset=first_card.start(),
            message=f"{card_count} Card widgets in one file; verify that containment reflects real hierarchy.",
        )

    return findings


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(
        description="Advisory audit for Flutter UI, motion, and anti-slop risks."
    )
    parser.add_argument("project", type=Path, help="Flutter project root or source directory")
    parser.add_argument("--json", action="store_true", help="Emit machine-readable JSON")
    parser.add_argument(
        "--fail-on",
        choices=("low", "medium", "high"),
        help="Exit with status 1 when a finding meets this severity.",
    )
    return parser.parse_args()


def main() -> int:
    args = parse_args()
    project = args.project.expanduser().resolve()
    if not project.exists():
        print(f"error: path does not exist: {project}", file=sys.stderr)
        return 2

    files = sorted(dart_files(project))
    findings = [finding for path in files for finding in scan_file(path, project)]
    findings.sort(
        key=lambda item: (
            -SEVERITY_ORDER[item.severity],
            item.path,
            item.line,
            item.rule,
        )
    )

    counts = {severity: 0 for severity in SEVERITY_ORDER}
    for finding in findings:
        counts[finding.severity] += 1

    if args.json:
        print(
            json.dumps(
                {
                    "project": str(project),
                    "files_scanned": len(files),
                    "counts": counts,
                    "findings": [asdict(finding) for finding in findings],
                },
                indent=2,
            )
        )
    else:
        print(f"Flutter UI audit: {project}")
        print(f"Scanned {len(files)} Dart files.")
        if not findings:
            print("No advisory patterns found.")
        for finding in findings:
            print(
                f"{finding.severity.upper():6} "
                f"{finding.path}:{finding.line} "
                f"[{finding.rule}] {finding.message}"
            )
            if finding.excerpt:
                print(f"       {finding.excerpt}")
        print(
            "Summary: "
            + ", ".join(f"{severity}={counts[severity]}" for severity in ("high", "medium", "low", "info"))
        )
        print("Findings are review prompts, not automatic proof of a defect.")

    if args.fail_on:
        threshold = SEVERITY_ORDER[args.fail_on]
        if any(SEVERITY_ORDER[item.severity] >= threshold for item in findings):
            return 1
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
