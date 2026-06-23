# 10 · Video Production

Promo and demo videos for the AI Breast Screening prototype presentation.

---

## Project summary

This prototype explores how AI-human disagreement in breast screening can be detected, handed over, resolved, and learned from. The service does not replace clinical judgement. It adds a structured service layer around existing reading and arbitration workflows, making disagreement context, AI evidence, discussion traces and outcome rationale more transparent, traceable and consistent. The learning loop is designed primarily for radiologist and team calibration through a disagreement case library.

---

## Prototype modules

The prototype has three connected parts, following the logic: **Detect → Resolve → Learn**.

### 1 · Reading Viewer

The radiologist performs an **independent initial reading** of the mammogram. The AI layer is not visible during reading. After the human reading is submitted and the initial outcome is recorded, the AI result is revealed. If the AI and human readings disagree, the system detects the disagreement, classifies it, and structures a handover ready for arbitration / consensus review.

Key design goals:
- Protect independent human judgement before AI is revealed
- Make AI-human disagreement visible without blame
- Prepare a structured handover with disagreement context

Do not describe this module as: "the doctor sees AI marks, then decides whether to agree or override."

### 2 · Arbitration / Consensus Review

This module is not primarily a recording or transcript tool. Its purpose is to support arbitration so that AI-human disagreement can be handled in a more **transparent, traceable, consistent and lower-friction** way.

Arbitration remains a clinical decision-making process. The service layer helps structure disagreement context, AI evidence, discussion traces, and outcome rationale so the pathway is easier to understand and review.

Key design goals:
- Bring the right evidence and comparison views into the arbitration workspace
- Capture discussion and rationale without adding excessive workload
- Record the arbitration outcome in a traceable, consistent format
- Make the case ready for handover to the learning library

Recall / no further assessment / further review are normal clinical arbitration outcomes. They are not new decisions created by AI presence. AI adds disagreement context and traceability support, but it does not make or force the outcome.

Do not describe this module as: "recording tool", "AI decides recall", or "transcript system".

### 3 · Learning / Disagreement Library *(not yet built)*

The library collects completed disagreement cases so radiologists and teams can learn from patterns.

The learning loop is **not primarily about training the AI model**. It is about helping human teams recognise recurring disagreement patterns and improve how they interpret, discuss and resolve AI-human disagreement.

Key design goals:
- Support radiologist calibration and team discussion
- Make disagreement patterns available for future arbitration reference
- Enable shared learning from AI-positive / human-negative cases, missed findings, trust gaps, and other disagreement types
- Possibly support PERFORMS-style learning logic, adapted to AI-human disagreement

AI model improvement or vendor feedback may be mentioned only as a secondary future possibility, not as the current prototype goal.

---

## Video plan

| Module | Video goal | Status | Raw recording | Export |
|---|---|---|---|---|
| Reading Viewer | Independent human reading → AI result revealed → disagreement detected → structured handover prepared for arbitration | 🟡 Recorded | reading-viewer_full-flow_2026-06-23.mov | — |
| Arbitration | Service layer supports transparent, traceable arbitration: disagreement context, discussion trace, outcome rationale | 🟡 Recorded | — | — |
| Disagreement Case Library | Completed cases enter the library for team calibration and future arbitration reference | 🔴 Not started | — | — |

### Video 1 — Reading Viewer (recorded)

**Description:** Reading Viewer walkthrough: independent human reading, AI result revealed after submission, AI-human disagreement detected, structured handover prepared for arbitration.

This video shows one focused flow. It is not a full product tour.

### Later videos can cover

- Arbitration support: how the service layer structures disagreement context, AI evidence and outcome rationale
- Discussion / participation trace: ambient capture and rationale recording during arbitration
- Decision trace: how the outcome and rationale are saved in a traceable format
- Disagreement Case Library: how completed cases become calibration references
- Team calibration / learning loop: how teams use disagreement patterns for shared learning

---

## Folder structure

```
10_Video_Production/
├── README.md               ← This file
├── raw_recordings/         ← QuickTime screen recordings (.mov), unedited
├── exports/                ← Final cut videos ready for presentation (.mp4)
├── scripts/                ← Narration scripts, shot lists, storyboards (.md)
└── assets/
    ├── music/              ← Background music files
    └── overlays/           ← Graphics, annotations, motion assets
```

## Naming convention

`[module]_[description]_[date].[ext]`

Examples:
- `raw_recordings/reading-viewer_full-flow_2026-06-23.mov`
- `exports/reading-viewer_final_2026-06-23.mp4`
- `scripts/reading-viewer_narration.md`

## Demo reset before recording

Before recording any video, reset the prototype to its initial state so BS-V000254 appears as awaiting review in the Arbitration Queue.

Open any of these URLs in the browser:

```
arbitration.html?reset=1
reading.html?reset=1
arbitration-case.html?reset=1
```

This clears the saved arbitration outcome from localStorage and removes the `?reset=1` parameter from the URL automatically. The page does not reload. Navigate to the starting page for your recording after running the reset.

What is cleared: `arb_BS-V000254` (the confirmed arbitration outcome for case BS-V000254).
What is not cleared: theme setting, any other prototype state.

After reset, the Arbitration Queue shows BS-V000254 as awaiting review with the Review → button active.

---

## Git note

Raw recordings and exports are excluded from git (see `.gitignore`).
Scripts and this README are tracked.
