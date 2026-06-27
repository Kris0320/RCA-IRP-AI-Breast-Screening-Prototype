# UI Content and Copy

## Human judgement panel

Title: `Human judgement`

Options:

- `Recall`
- `No recall`

Button: `Submit initial judgement`

Note: `AI result will be revealed after your independent judgement.`

## AI judgement panel

Title: `AI reader result`

AI judgement: `Recall`

Confidence: `High`

Finding type: `Focal asymmetry`

Location: `Left breast, upper outer area`

## Disagreement detected panel

Title: `AI-Human Disagreement Detected`

Body: `The human judgement and AI reader result are not aligned. Pause before finalising the case.`

Disagreement type: `High-confidence AI positive vs human negative`

Actions:

- `Take a second look`
- `Request peer pause`
- `Prepare warm handover`
- `Record override reason`

## Warm handover card

Title: `Warm Handover Card`

Fields:

- `Case ID`
- `Initial human judgement`
- `AI judgement`
- `AI confidence`
- `Finding type`
- `Location`
- `Reason for escalation`
- `Suggested arbitration question`

Suggested arbitration question:

`Should this high-confidence AI-positive case be recalled for further assessment?`

## Non-blame decision receipt

Title: `Non-blame Decision Receipt`

Body: `This receipt records the decision pathway without assigning individual blame.`

Fields:

- `Initial human judgement: No recall`
- `AI judgement: Recall, high confidence`
- `Disagreement type: High-confidence AI positive vs human negative`
- `Action taken: Warm handover prepared`
- `Arbitration outcome: Recall to assessment`
- `Learning tag: AI-positive / human-negative disagreement`

## Disagreement Case Library message

<!-- previously: "Care Loop message" — archived in ARCHIVE_care-loop-original-copy.md -->

Title: `Added to Disagreement Library`

Body:

`Available for team calibration and future arbitration reference.`

Pattern:

`Pattern observed: AI-positive / human-negative · detection gap`

Learning note:

`The learning loop is not primarily about training the AI model. It helps radiologists and teams recognise recurring disagreement patterns, calibrate judgement, and improve how they interpret, discuss and resolve AI-human disagreement.`
