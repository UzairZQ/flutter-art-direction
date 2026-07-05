# Material 3 Expressive for Flutter

## Overview
Google's latest M3 expressive system: spring motion, dynamic shapes, adaptive layouts.

## Key Components

### Navigation
- NavigationBar with NavigationDestination (replaces BottomNavigationBar)
- NavigationRail for tablets/desktop
- NavigationDrawer (replaces Drawer)

### Buttons
- FilledButton (primary action, no shadow)
- FilledButton.tonal (medium emphasis, M3 tonal surface)
- ElevatedButton (with surfaceTint for elevation)
- TextButton, OutlinedButton
- SegmentedButton (replaces ToggleButtons)

### Inputs
- SearchBar (M3 search)
- SearchView (expanded search with suggestions)
- MenuAnchor (replaces PopupMenuButton)
- SegmentedButton for filters

### Surfaces
- Card (with surfaceTint for elevation instead of shadow)
- CarouselView (scrollable content strips)
- NavigationDrawer

## Shape System
- Small/Medium/Large component shapes
- Radius tokens: none, extraSmall, small, medium, large, extraLarge, full
- Morphing shapes through AnimatedContainer

## Spring Motion
- Default M3 spring: SpringDescription(mass: 1, stiffness: 210, damping: 20)
- Emphasis spring: stiffer for feedback, looser for storytelling
- Reduced-motion: respect MediaQuery.disableAnimations

## Migration Checklist
- useMaterial3: true
- Replace BottomNavigationBar → NavigationBar
- Replace Drawer → NavigationDrawer
- Replace ToggleButtons → SegmentedButton
- Replace ElevatedButton → FilledButton where appropriate
- Enable surfaceTint for cards and elevated surfaces
