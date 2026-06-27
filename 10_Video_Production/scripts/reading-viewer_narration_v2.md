# Reading Viewer — Narration Script v2

**Video goal:** Reading Viewer walkthrough — independent human reading, AI result revealed after submission, AI-human disagreement detected, structured handover prepared for arbitration.

**Flow source:** Based on actual prototype interaction (v2, 2026-06-25)  
**Target length:** 90–120 seconds  
**Status:** Script ready for recording

---

## What this video shows

1. Radiologist opens a case and marks findings independently — no AI visible
2. Radiologist submits their reading
3. AI runs in the background and detects a disagreement
4. Comparison view reveals both readings: red = human markings, orange = AI markings
5. Right-panel service layer: three cards — Human Reading, AI Result, Disagreement Detection
6. Disagreement card actions: Peer Pause, Record Doubt, View Detailed Comparison, Prepare Handover
7. Handover card generated — case enters Arbitration Queue

---

## Narration — Shot by Shot

---

### Shot 1 — Independent reading begins

> A radiologist opens a screening case. The mammogram is displayed across standard views.
> No AI output is visible. The radiologist reviews and marks findings independently — just as they would in a standard workflow.

**Design note:** The AI layer is deliberately hidden during initial reading to protect independent clinical judgement. The radiologist's assessment is formed without AI influence.

---

### Shot 2 — Mark, annotate, and submit

> The radiologist marks areas of concern, records their findings, confirms the finding type, and submits.
> This is a familiar action — the submission step hasn't changed.

**Design note:** The interaction stays close to existing workflow. No new cognitive burden is added at this stage.

---

### Shot 3 — AI detects a disagreement in the background

> After submission, the AI runs its analysis. It detects a disagreement between the human reading and its own result.
> The system now surfaces a structured comparison — without interrupting the submission flow.

**Design note:** The AI doesn't intervene before the human decides. It waits. Disagreement is only surfaced after the reading is locked in — making the AI a checking layer, not a directing one.

---

### Shot 4 — Comparison view: red and orange

> The comparison view loads. Red markers show where the radiologist identified findings. Orange markers show where the AI identified findings.
> Alongside the comparison, the system displays basic anomaly information and an enlarged image of the area in question.

**Design note:** Showing both readings simultaneously — without one overwriting the other — makes the nature of the disagreement visible at a glance. The radiologist can immediately see what the AI saw, and where it differs.

---

### Shot 5 — Right panel: three cards

> On the right, a service layer panel appears. Three cards structure the disagreement:
> the Human Reading result, the AI Result, and a Disagreement Detection card.
> This panel is where the service design intervenes — adding structure to a moment that is currently unstructured in most screening workflows.

**Design note:** The three-card layout separates evidence from interpretation. Each card has a defined role: record what was seen, record what the AI saw, and frame the disagreement for action.

---

### Shot 6 — Disagreement card: Peer Pause

> The Disagreement card offers several response options.
> Peer Pause sends a message to a colleague — flagging this case for a quick discussion before it moves forward.
> A note can be added at the point of disagreement, capturing the radiologist's thinking in the moment.

**Design note:** Disagreement cases often involve ambiguity that benefits from a second opinion before formal arbitration. Peer Pause lowers the friction of raising a question informally — without requiring a full arbitration process to start.

---

### Shot 7 — Record Doubt

> The radiologist can also record a specific doubt or question — attaching it directly to the case.
> This doubt travels with the case into arbitration, giving the arbitration team context on what was uncertain and why.

**Design note:** Disagreements are rarely binary. Recording doubt at the point of reading preserves the radiologist's reasoning for later review — reducing information loss between reading and arbitration.

---

### Shot 8 — View Detailed Comparison

> Selecting View Detailed Comparison opens a deeper evidence panel.
> This shows granular comparison data and surfaces similar historical cases from the disagreement library.
> The radiologist can click into any reference case for full detail, or navigate directly to the case library.

**Design note:** Similar past cases are a resource that currently lives outside the reading workflow. Surfacing them at the point of disagreement helps calibrate judgement without requiring a separate lookup.

---

### Shot 9 — Prepare Handover

> When ready, the radiologist selects Prepare Handover.
> The system generates a structured handover card — capturing the human reading, the AI result, the disagreement classification, and any notes or doubts recorded.

**Design note:** Arbitration currently relies on verbal handover or informal notes. The handover card standardises what gets passed on — making disagreement context consistent and traceable across the team.

---

### Shot 10 — Arbitration Queue

> The case enters the Arbitration Queue.
> A team member can now open the queue, select this case, and begin the consensus review — with full disagreement context already in place.

**Design note:** The Reading Viewer doesn't resolve the disagreement. It structures it. Resolution happens in arbitration, where the right evidence and the right people come together.

---

## Full narration (continuous read)

> A radiologist opens a screening case. The mammogram is displayed across standard views. No AI output is visible. The radiologist reviews and marks findings independently — just as they would in a standard workflow.
>
> They mark areas of concern, record their findings, confirm the finding type, and submit. A familiar action. Nothing has changed in the submission step.
>
> After submission, the AI runs its analysis. It detects a disagreement. The system surfaces a structured comparison — without having interrupted the reading.
>
> The comparison view loads. Red markers show the radiologist's findings. Orange markers show the AI's findings. Basic anomaly information and an enlarged image appear alongside.
>
> On the right, a service layer panel structures the disagreement into three cards: the Human Reading result, the AI Result, and a Disagreement Detection card.
>
> The Disagreement card offers several options. Peer Pause sends a message to a colleague — flagging this case for a quick discussion before it moves forward. A note can be added to capture the radiologist's thinking in the moment.
>
> The radiologist can also record a specific doubt — a question that travels with the case into arbitration.
>
> Selecting View Detailed Comparison opens a deeper evidence panel, surfacing similar historical cases. Reference cases can be opened in full, or the radiologist can navigate to the case library.
>
> When ready, they select Prepare Handover. The system generates a structured handover card — capturing the human reading, the AI result, the disagreement classification, and any recorded notes.
>
> The case enters the Arbitration Queue. A team member selects it to begin consensus review — with full disagreement context already in place.
>
> The Reading Viewer doesn't resolve the disagreement. It structures it. Resolution happens in arbitration, where the right evidence and the right people come together.

---

## Shot list

| # | On screen | Action | Approx. duration |
|---|---|---|---|
| 1 | Mammogram viewer, no AI overlay | Case opens, four views visible | 5s |
| 2 | Reading workspace | Radiologist marks, records finding type | 6s |
| 3 | Submit confirmation | Radiologist submits | 3s |
| 4 | Comparison view loads | Red + orange markers appear, anomaly info shown | 6s |
| 5 | Right panel: three cards | Human Reading, AI Result, Disagreement Detection cards visible | 5s |
| 6 | Disagreement card: Peer Pause | Peer Pause triggered, note added | 5s |
| 7 | Disagreement card: Record Doubt | Doubt recorded and attached to case | 4s |
| 8 | Detailed Comparison panel | Similar cases surfaced, reference case opened | 7s |
| 9 | Prepare Handover | Handover card generated | 5s |
| 10 | Arbitration Queue | Case appears in queue, team selects for review | 4s |

**Total: ~50s on-screen action + narration pacing ≈ 90–120s**

---

## Terminology guide

**Use:**
- independent human reading
- initial reading outcome
- AI result revealed after submission
- AI-human disagreement detected
- red markers (human) / orange markers (AI)
- Peer Pause
- Record Doubt
- View Detailed Comparison
- Prepare Handover
- structured handover card
- arbitration / consensus review
- service layer
- disagreement classification

**Avoid:**
- "the doctor sees the AI mark first"
- "the doctor overrides the AI"
- "AI recommends recall" (AI suggests; arbitration decides)
- "AI decides recall"
- "recording tool"
- "the AI was right / wrong"
