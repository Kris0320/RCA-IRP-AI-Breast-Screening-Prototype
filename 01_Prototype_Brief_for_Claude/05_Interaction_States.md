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
- Receipt frames the case as traceability and learning, not blame.
- User can add the case to Care Loop.

## State 7: Added to Care Loop

- Care Loop message appears.
- Case is marked for outcome-linked review.
- Prototype ends with learning loop visible.

