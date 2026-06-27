# Read Me First

This folder is the only source Claude Code should use for the prototype.

The broader Obsidian vault contains research notes, tutorial notes, models, references and archive material. Do not use the wider vault unless explicitly instructed.

Prototype goal:

Build a DetectedX-inspired case-based mammography reading prototype with an embedded AI-human disagreement handling layer.

Reference screenshots are stored in `assets/references-detectedx/`. They are for interaction-pattern reference only and must not be copied directly.

## What Claude Code should build

Build a single-page interactive prototype that shows:

1. A dark mammography reading environment.
2. A human reader making an initial judgement.
3. AI judgement being revealed after the human submission.
4. AI-human disagreement being detected.
5. A soft intervention panel appearing.
6. A warm handover card being prepared.
7. A non-blame decision receipt being generated.
8. The case being added to the Disagreement Case Library for team calibration and future arbitration reference.

## What Claude Code should not build

Do not build:

- A full DetectedX clone.
- A full education / course platform.
- Login, payment, account, or scoring system.
- A real DICOM viewer.
- Real diagnosis logic.
- A generic medical dashboard.
- A large analytics dashboard.
- A direct copy of DetectedX UI, text, branding, or visual assets.
