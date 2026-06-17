# Touchpoint 3 — Decision Receipt & Calibration Case Card

## Source visual

![[page-touchpoint-3-decision-receipt-learning-memory.svg]]

## Slide purpose

Show what happens after arbitration, before and after follow-up outcome is known.

Touchpoint 3 explains two linked artefacts with different timings: the Non-blame Decision Receipt is generated immediately after arbitration, while the Calibration Case Card is generated later only after follow-up outcome is reviewed.

## Key message

Every arbitration case should generate a structured, non-blame Decision Receipt. It records the arbitration decision rationale and evidence used at that moment, but it does not yet know the final clinical outcome. A case becomes a Calibration Case Card only after follow-up outcome is updated and an outcome-linked Learning Value Check selects it for learning.

## Visual structure

Left: **Non-blame Decision Receipt**  
Records the final recall decision, human judgement, AI evidence layer, arbitration rationale and evidence used.

Within the receipt: **Follow-up & Learning Status**  
Shows that outcome status is pending, learning review will happen after outcome update, and the next step is to mark the case for outcome-linked review.

Middle: **Outcome-linked review selects learning cases**  
Shows that follow-up outcome comes before calibration material is created.

Right: **Calibration Case Card**  
Turns an outcome-linked selected receipt into a reusable calibration object. It keeps only the learning value: source receipt, follow-up outcome, why the case was selected, disagreement pattern, learning focus, discussion prompt, suggested use and output.

## Speaker notes draft

Touchpoint 2 ends with a human-led arbitration review. Touchpoint 3 asks what the service does with that decision afterwards.

The Non-blame Decision Receipt is generated immediately after arbitration as service evidence for audit and later review. It captures the final recall decision and arbitration rationale without framing the case as an individual reader problem. It records the human judgement, AI evidence layer, evidence used and a short record purpose statement.

At this point, the follow-up outcome is still pending. The receipt can be marked for outcome-linked review, but it should not automatically become a learning case. Recall result, ultrasound, biopsy or pathology may later update the case outcome.

The Calibration Case Card is generated from the receipt only after the follow-up outcome is reviewed through a Learning Value Check. It does not repeat the full evidence list or audit fields; instead it extracts the learning focus of the case. The same case can support a monthly Disagreement Review Workshop, trainee calibration, a case-of-the-week prompt, audit or pattern review.

## Service logic

- **Receipt = immediate record:** every arbitration case preserves the final recall decision, evidence used and arbitration rationale.
- **Follow-up outcome = later clinical update:** recall result, ultrasound, biopsy or pathology may update what happened after the arbitration decision.
- **Outcome-linked Learning Value Check = selection mechanism:** the case is reviewed after outcome update to decide whether it is useful enough to become a calibration case.
- **Calibration Case Card = selected learning object:** generated from a receipt after outcome-linked Learning Value Check, then used in the Disagreement Case Library, review workshops or calibration sessions.

## Design principles

- Keep the focus on learning and non-punitive review.
- Keep AI as an evidence layer, not the recall decision-maker.
- Show that arbitration produces a receipt, while calibration material is created only after outcome-linked review.
- Make the artefacts feel like service evidence, not a full interface replacement.
- Use calm, accountable and non-punitive wording.

## Related notes

- [[Prototype Direction]]
- [[Disagreement Review Workshop]]
- [[Disagreement Handling Logic]]
- [[Specific Anchor Model]]
- [[Decision Log]]
- [[Presentation Structure]]

## What to refine next

- Validate whether the receipt captures enough information for audit without adding too much workload.
- Test which learning tags radiologists would actually use.
- Prototype how a Calibration Case Card appears inside a review workshop or Quiet Review Station.
