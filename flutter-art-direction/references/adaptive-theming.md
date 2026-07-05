# Adaptive Theming for Flutter

## Overview
Modern theming beyond light/dark: Dynamic Color, platform adaptation, semantic roles.

## Dynamic Color (Material You)

Use ColorScheme.fromSeed() for dynamic palette generation:
- Android 12+: wallpaper-aware dynamic color
- Other platforms: brand seed fallback
- DynamicSchemeVariant options: tonalSpot, fidelity, vibrant, expressive, etc.

## Platform-Adaptive Components

Table:
| Component | Android (M3) | iOS (Cupertino) | Cross-Platform |
| Button | FilledButton, tonal | CupertinoButton.filled | AdaptiveButton |
| Navigation | NavigationBar | CupertinoTabBar | AdaptiveNavigationBar |
| Dialog | AlertDialog | CupertinoAlertDialog | AdaptiveDialog |
| Switch | Switch.adaptive | CupertinoSwitch | Switch.adaptive |

## Semantic Color Roles (not literal colors)
- surfaceBase, surfaceContainerLow, surfaceContainerHigh
- primary, secondary, tertiary (via ColorScheme)
- error, warning, success (via ColorScheme)
- outline, outlineVariant

## Light/Dark + High Contrast
- darkTheme: dark color scheme
- highContrast: ThemeData with highContrast: true
- Platform brightness detection through MediaQuery

## Implementation
- ThemeData.from(colorScheme: scheme) 
- useMaterial3: true as default
- Component themes: NavigationBarThemeData, CardTheme, etc.
- Theme extensions for custom tokens
