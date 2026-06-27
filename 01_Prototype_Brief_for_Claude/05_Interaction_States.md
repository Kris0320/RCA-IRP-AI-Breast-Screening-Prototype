# Interaction States

## State 1: Initial reading

- Mammography case is open.
- Mammogram image area is dominant.
- Human judgement panel is visible.
- AI output is hidden.
- User can submit an independent decision.

## State 2: Human judgement submitted

- Human decision is locked as `No recall`.
- System confirms that independent judgement has been recorded.
- AI reveal becomes available.

## State 3: AI revealed

- AI judgement panel appears.
- AI output shows `Recall suggested`.
- AI confidence shows `High confidence`.

## State 4: Disagreement detected

- System compares human judgement and AI output.
- Disagreement panel appears.
- Language is neutral and non-blaming.
- User can prepare a warm handover.

## State 5: Warm handover prepared

- Warm handover card appears.
- Human judgement and AI output are shown together.
- Escalation reason and reviewer notes can be prepared.
- User can generate a decision receipt.

## State 6: Decision receipt generated

- Decision receipt records the disagreement, escalation route and rationale.
- Receipt frames the case as a decision trace, not blame.
- User can add the case to the Disagreement Case Library.

## State 7: Added to Disagreement Library

<!-- previously: "Added to Care Loop" — archived in ARCHIVE_care-loop-original-copy.md -->

- Disagreement Library confirmation appears.
- Case is saved for team calibration and future arbitration reference.
- Follow-up outcome pending confirmation before full library entry.
- Prototype ends with Disagreement Library state visible.

