# Touchpoint 2 — Arbitration Support Layer

## Source visual

![[page-touchpoint-2-arbitration-handover-review.svg]]

## Slide purpose

Show how a detected AI-human disagreement moves from a soft cue into a structured support layer for human-led senior review.

This slide should make clear that we are adding to the clinical environment, not replacing it. Existing review workspace tools already support image viewing, prior comparison and reporting. The prototype adds a disagreement support layer when AI-human disagreement occurs.

## Key message

The Warm Handover Summary brings the case into arbitration with context. The Arbitration Support Layer creates a pause point inside the existing review workspace, supports human-led senior review and records the arbitration rationale.

## Visual structure

Left: **Warm Handover Summary**  
Small transition artefact before senior review.

Middle: **Context travels with the case**  
The connector shows that escalation should carry structured context, not just a case ID.

Right: **Arbitration Support Layer**  
Disagreement support layer embedded in the existing review workspace, with a Warm Handover Summary, Arbitration Pause Point, rationale capture and learning handoff.

## Speaker notes draft

Touchpoint 1 detects the disagreement gently. Touchpoint 2 shows what happens next.

The Warm Handover Summary supports the reader transferring a difficult case to senior review without losing context. It records why the case is escalated, the disagreement type, what has already been checked, and what support is needed from the arbitrator.

The Arbitration Support Layer is not a replacement for PACS, RIS or the mammogram reading system. It sits on top of the existing review workspace as a pause mechanism. The senior reviewer still uses the familiar image viewer and reporting context, while the support layer makes the disagreement context, arbitration rationale and learning handoff visible.

The learning handoff makes the service loop visible. If the case is useful for calibration, it can be sent to learning memory with a learning tag such as subtle lesion, prior comparison or detection gap.

## Design principles

- Keep AI as an evidence layer, not the recall decision-maker.
- Show senior review as human-led and embedded in the existing review workspace.
- Make rationale capture visible.
- Connect arbitration to learning memory.
- Use non-blame, structured handover language.

## Related notes

- [[Prototype Direction]]
- [[Disagreement Review Workshop]]
- [[Disagreement Handling Logic]]
- [[Specific Anchor Model]]
- [[Decision Log]]
- [[Presentation Structure]]

## What to refine next

- Test whether radiologists would actually complete the handover card before escalation.
- Validate which evidence items are essential for arbitration.
- Prototype a realistic filled example of the arbitration rationale and final recall decision.
