# Spatial Mobile Design for Flutter

## Overview
Depth communicates hierarchy, not decoration. 4-layer system for mobile.

## Depth Layer System
| Layer | Elevation | Shadow | Use Case |
|-------|-----------|--------|----------|
| Base | 0 | None | Background, full-bleed images |
| Surface | 1-3 | Subtle | Cards, sheets, bottom bars |
| Raised | 6-8 | Medium | Modals, FAB, dropdowns |
| Overlay | 12-16+ | Strong | Dialogs, toasts, bottom sheets |

## Glass as Hierarchy (Not Decoration)
Only on raised/overlay layers. Use BackdropFilter sparingly. Ensure readability.

## Parallax & Depth Effects
- Hero parallax on scroll: max 20px offset via Transform.translate
- Gyroscope tilt: subtle 3D on 2D (opt-in, reduced-motion off)
- CustomPainter for depth-aware charts/timelines

## Flutter Implementation
- Elevation via Material widget or shadow BoxDecoration
- SurfaceTint for M3 elevation
- RepaintBoundary around heavy visuals
- Reduced-motion: no parallax, no 3D transforms

## Anti-Slop
- No random z-index variations
- No glass/blur without depth system
- No depth that obscures readability
- No 3D transforms on reduced motion
