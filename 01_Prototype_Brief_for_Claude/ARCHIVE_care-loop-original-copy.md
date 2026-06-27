# ARCHIVE — Original Care Loop Copy

> Archived: 2026-06-23
> Reason: "Care Loop" framing replaced by "Disagreement Case Library" across the prototype
> and documentation. The original copy below is preserved for reference only.
> Do not use this content in the live prototype or presentation.

---

## From 03_Prototype_User_Flow.md — Step 13 (original)

```
13. Case is added to the Care Loop:
   - `This case has been added to the next team calibration review.`
   - `Pattern to review: High-confidence AI-positive cases initially dismissed by human readers.`
```

---

## From 04_UI_Content_and_Copy.md — Care Loop message (original)

```
## Care Loop message

Title: `Added to Care Loop`

Body:

`This case has been added to the next team calibration review.`

Pattern:

`High-confidence AI-positive cases initially dismissed by human readers.`
```

---

## From 05_Interaction_States.md — State 6 and State 7 (original)

```
## State 6: Decision receipt generated

- Decision receipt records the disagreement, escalation route and rationale.
- Receipt frames the case as traceability and learning, not blame.
- User can add the case to Care Loop.

## State 7: Added to Care Loop

- Care Loop message appears.
- Case is marked for outcome-linked review.
- Prototype ends with learning loop visible.
```

---

## From 00_READ_ME_FIRST.md — Step 8 (original)

```
8. The case being added to a Care Loop / team calibration review.
```

---

## Why this was changed

The "Care Loop" label risked implying that the purpose is feeding data back to the AI model.
The current project direction is that the learning loop is primarily for **human and team calibration**:
radiologists recognising recurring disagreement patterns, improving judgement, and building a reference
library for future arbitration. AI model improvement is a distant secondary possibility, not the
current prototype goal.

See: `10_Video_Production/README.md`, section "3 · Learning / Disagreement Library"
