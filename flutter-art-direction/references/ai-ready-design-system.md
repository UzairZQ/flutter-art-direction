# AI-Ready Design System for Flutter

## Overview
Make your design tokens and components discoverable by AI coding agents.

## Why AI-Ready
AI tools generate better code when they can look up your design decisions instead of guessing.

## MCP (Model Context Protocol) Server
A small server that AI tools query for design tokens and components.

File structure:
.design-system/
  tokens/
    primitives.json
    semantic.json
    component.json
  components/
    button.md
    card.md
    input.md
    navigation.md
  patterns/
    onboarding-flow.md
    empty-states.md
    error-states.md
  registry.json
  mcp-server/
    server.py
    tools/
      get_tokens.py
      get_component.py
      get_pattern.py

## Registry Entry Format
{
  "name": "ReflectionPromptCard",
  "description": "Primary card for daily reflection prompt",
  "tokens": ["semantic.color.surfaceBase", "semantic.spacing.cardPadding"],
  "variants": ["default", "completed", "skipped"],
  "file": "lib/ui/features/reflection/widgets/reflection_prompt_card.dart"
}

## Agent Prompt Template
"Use the design system MCP server. Before generating UI, call get_tokens for spacing/color/radius, get_component for the widget spec, and get_pattern for the flow pattern."

## JSON Token Exports
Export tokens.json alongside code for AI consumption.

## Benefits
- Consistent AI-generated output
- No raw values/guessing
- Design system evolves with code
- Multi-agent collaboration possible
