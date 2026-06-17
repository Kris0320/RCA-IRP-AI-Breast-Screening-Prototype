# Touchpoint 1 — Expanded Comparison Review

## Source visual

![[page-touchpoint-1-expanded-comparison-review.svg]]

## Slide purpose

Show what appears after the radiologist opens the collapsed soft disagreement cue.

This is the inspected state of Touchpoint 1. It stays inside the existing mammogram review workspace and adds a calm comparison review panel rather than replacing the reading system.

## Key message

The expanded state helps the reader inspect the difference, classify the disagreement and prepare a senior review handover if needed. It does not tell the reader that one judgement is automatically correct.

## Visual structure

- Background: existing mammogram review workspace with current and prior image areas.
- Overlay: expanded **Comparison review** panel.
- Comparison summary: human judgement and AI evidence layer shown side by side.
- Classification: disagreement type and primary concern.
- Reader reflection note: a short prompt for what the senior reviewer should know.
- Suggested next step: **Prepare senior review handover**.
- Footer relationship: the primary action prepares the Warm Handover Summary used in Touchpoint 2.

## Speaker notes draft

The collapsed cue only says that the second interpretation differs. This expanded panel appears after the radiologist chooses to inspect it.

The design keeps the tone calm. It shows human judgement and the AI evidence layer as two sources to compare, then names the disagreement type. The reader can add a short reflection note before sending the case forward.

The primary action is not a final clinical decision. It prepares the senior review handover, creating the Warm Handover Summary used in Touchpoint 2. This keeps the service logic continuous: detect, inspect, classify, then hand over with context.

## Design principles

- Keep the existing mammogram review workspace in place.
- Reveal detail only after the reader opens the soft cue.
- Classify the disagreement rather than making it feel punitive.
- Keep AI as an evidence layer.
- Make the next step toward senior review clear.

## Related notes

- [[Prototype Direction]]
- [[Specific Anchor Model]]
- [[Disagreement Handling Logic]]
- [[Disagreement Review Workshop]]
- [[Decision Log]]
- [[Presentation Structure]]

## What to refine next

- Validate whether readers need more or less detail before preparing senior review handover.
- Test the wording of the reader reflection prompt.
- Decide whether the expanded panel should sit as a right drawer, modal overlay or side-by-side comparison panel in the prototype walkthrough.
