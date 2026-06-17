# Prototype Sketch Synthesis - Disagreement Support Layer

## Source

Hand sketch photographs shared on 2026-06-13.

These sketches appear to explore how the project prototype could sit across the existing mammogram review workflow, comparison review, consensus / arbitration, automatic rationale recording, case library and learning outputs.

## One-line synthesis

The sketches support a lightweight disagreement support layer: a soft cue appears inside the existing review workspace, helps the reader compare AI evidence and human judgement, prepares consensus / arbitration handover, records reasoning, and later turns selected outcome-linked cases into learning material.

## Key ideas extracted from the sketches

- A soft cue or soft tag appears after a mismatch between reader judgement and AI evidence.
- The cue should allow optional review rather than forcing immediate interruption.
- The reader may ask for peer support or discussion before formal escalation.
- The comparison moment should bring together human judgement, AI evidence, prior images and suspicious regions.
- Arbitration / consensus review should preserve the context that travelled with the case.
- A short reason / rationale field is important, but should not become a heavy form.
- Some reasoning could be auto-suggested or pre-filled, then confirmed or edited by the human reviewer.
- Final recall decision should remain human-led.
- The case may later become part of a case library only if it has learning value.
- Learning outputs may include tricky cases, interval cases, disagreement cases, posters, teaching material or review-session prompts.

## Interpreted prototype flow

1. Existing mammogram review workspace

The radiologist reads the mammogram in the existing review environment. The prototype should not redesign PACS / RIS / mammogram viewing from scratch.

2. Human judgement and AI evidence layer

Human judgement and AI evidence are available for comparison. The sketches show the need to compare the AI result with reader judgement, not to treat AI as the final decision-maker.

3. Soft cue / soft tag

When a mismatch appears, a soft cue signals that the second interpretation differs. The cue should be low-pressure and allow the reader to open comparison review when useful.

Possible wording:

- Non-blame review cue
- Second interpretation differs
- Comparison review available
- Open comparison review

4. Comparison review

The comparison review brings together:

- Human judgement
- AI evidence layer
- AI risk signal / suspicious region
- Prior image comparison
- Reader annotation
- Disagreement type
- Reader reflection note

5. Peer support / discussion option

The sketches include an “ask for peer support / discuss” idea. This is useful as a softer step before full arbitration, especially for uncertainty, hierarchy pressure or difficult judgement moments.

Prototype implication: this could become an optional Peer Pause / Consensus Check action, not a separate break-time activity.

6. Warm handover into consensus / arbitration

If the case needs review, the system prepares a lightweight handover summary. Context should travel with the case:

- Case ID
- Why this case is difficult
- Human judgement
- AI evidence layer
- Evidence checked
- Prior image relevance
- Support needed from consensus / arbitration reviewer

7. Consensus / arbitration review

The reviewer uses the existing review workspace with a support layer. The support layer should show:

- Current mammogram with AI / human marks
- Prior image comparison
- Human judgement
- AI evidence layer
- Disagreement type
- Arbitration / consensus rationale
- Final recall decision
- Learning handoff status

8. Automatic rationale / record support

The sketches suggest that reasoning evidence may be automatically captured or lightly structured. This should reduce typing burden:

- Pre-filled evidence checked
- Suggested reason tags
- Short rationale prompt
- Human confirm / edit
- Automatic decision receipt generation

9. Final recall decision

The final recall decision remains human-led. The design should avoid implying that AI makes the final decision.

10. Outcome-linked learning

After follow-up outcome is available, selected cases can move into learning:

- Tricky case
- Interval case
- Disagreement case
- AI-human mismatch case
- Teaching / poster / case-of-the-week material
- Disagreement Case Library

## Prototype components reinforced by the sketches

## Touchpoint 1 - Disagreement Detection Cue

The sketches reinforce the idea of a soft cue rather than an alarm.

Design requirement:

- Detect first, inspect second.
- Keep the mammogram viewer primary.
- Do not show all details immediately.
- Let the reader open comparison review when ready.

## Touchpoint 1b - Expanded Comparison Review

The sketches show a comparison layer that should help the reader inspect the difference.

Useful sections:

- Human judgement
- AI evidence layer
- Difference identified
- Disagreement classification
- Prior image relevance
- Reader note before handover
- Prepare senior review / consensus handover

## Touchpoint 2 - Arbitration Support Layer

The sketches suggest a support layer embedded in the existing review workspace, not a new dashboard.

Designed elements:

- Warm Handover Summary
- Peer Pause / Consensus Check
- Rationale capture
- Final recall decision support
- Learning handoff

## Touchpoint 3 - Non-blame Decision Receipt

The sketches reinforce automatic record creation after consensus / arbitration.

The receipt should capture:

- Final recall decision
- Human judgement
- AI evidence layer
- Arbitration / consensus rationale
- Evidence used
- Record purpose
- Follow-up and learning status

## Learning layer - Calibration Case Card and Library

The sketches show several possible learning outputs: tricky cases, interval cases, disagreement cases, posters and case review material.

Updated logic:

- Not every receipt becomes a learning case.
- Follow-up outcome is needed before learning value can be assessed.
- Selected cases become Calibration Case Cards.
- Calibration cases enter the Disagreement Case Library.
- The library supports existing review meetings, calibration, audit and AI governance.

## Candidate interface / artefact labels

- Soft tag
- Non-blame review cue
- Comparison review
- Peer Pause
- Ask for peer support
- Warm Handover Summary
- Consensus review
- Arbitration support layer
- Rationale capture
- Automatic decision receipt
- Outcome-linked review
- Calibration Case Card
- Disagreement Case Library
- Tricky case
- Interval case
- Disagreement case

## Design risks to avoid

- Do not make the prototype look like a full new radiology workspace.
- Do not create extra learning activity during radiologists’ break time.
- Do not make peer support feel like surveillance or weakness.
- Do not make the cue feel like an alarm.
- Do not imply AI is the final decision-maker.
- Do not turn rationale capture into a long form.
- Do not send every arbitration receipt into the library automatically.

## Open design questions

1. Should “Peer Pause” happen before formal arbitration, or should it be folded into existing consensus review?
2. What is the minimum rationale field that is useful without adding workload?
3. Which fields can be auto-filled from the existing system?
4. Who confirms or edits the suggested rationale?
5. How should prior image comparison be highlighted without increasing automation bias?
6. Which cases become “tricky cases” versus interval cancer learning cases versus AI governance cases?
7. What existing meeting should use the selected Calibration Case Cards?
8. How should the design show learning outputs such as posters or teaching cases without implying extra break-time labour?

## Next prototype implications

- Rename or frame “peer support” as a lightweight optional consensus check.
- Add “auto-captured evidence checked” into Touchpoint 2 or Touchpoint 3.
- Keep the handover summary short and mostly system-generated.
- In visual slides, show PACS / existing review workspace as a background container only.
- Make the learning output explicitly outcome-linked and selected, not automatic.
- Consider a small “used in review” status for Calibration Case Cards.

## Related notes

- [[Prototype Direction]]
- [[Refined Prototype Storyline after Expert Testing]]
- [[Clinical Learning Formats for Disagreement Review]]
- [[Disagreement Review Workshop]]
- [[Specific Anchor Model]]
- [[Disagreement Handling Logic]]
- [[Decision Log]]

