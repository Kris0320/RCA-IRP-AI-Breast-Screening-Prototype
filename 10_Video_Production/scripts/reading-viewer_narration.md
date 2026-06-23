# Reading Viewer — Narration Script

**Video goal:** Reading Viewer walkthrough: independent human reading, AI result revealed after submission, AI-human disagreement detected, structured handover prepared for arbitration.

**Status:** Raw recording completed (2026-06-23)  
**Target length:** 60–90 seconds  
**Raw recording:** `raw_recordings/reading-viewer_full-flow_2026-06-23.mov`

> This is Video 1 in the series. It covers the Reading Viewer only.
> It is not a full product tour. Later videos will cover Arbitration, Decision Trace, Disagreement Case Library, and Team Calibration.

---

## What this video is and is not

**This video shows:**
- The radiologist performing an independent initial reading with no AI visible
- The human reading submitted and initial outcome recorded
- The AI result revealed after submission
- AI-human disagreement detected by the system
- A structured handover prepared and ready for arbitration

**This video does not show:**
- The radiologist seeing AI marks before making their own judgement
- The radiologist overriding the AI inside the Reading Viewer
- AI directly deciding or recommending recall
- Peer pause, ambient discussion capture, or learning library features (save for later videos)

---

## Storyline (9 steps)

1. A radiologist opens a screening case.
2. The mammogram is visible. The AI layer is not yet visible.
3. The radiologist completes an independent initial reading.
4. The initial reading outcome is recorded — no recall-level finding.
5. The reading is submitted.
6. The AI result is revealed after submission.
7. The AI suggests recall with high confidence (focal asymmetry, 91%).
8. The system detects an AI-positive / human-negative disagreement.
9. The case is structured into a handover and ready to enter arbitration / consensus review.

---

## Narration draft

> [Shot 1 — Case opens, AI not visible]  
> A radiologist opens a screening case. The mammogram is shown across four standard views. No AI output is visible yet.

> [Shot 2 — Independent reading]  
> The radiologist reviews the images independently and records an initial reading: no recall-level finding.

> [Shot 3 — Submit]  
> The initial reading is submitted.

> [Shot 4 — AI revealed]  
> The AI result is now revealed. The AI suggests recall — focal asymmetry, left breast, 91% confidence.

> [Shot 5 — Disagreement detected]  
> The system detects a disagreement: AI-positive, human-negative. The disagreement is classified and a structured handover is prepared.

> [Shot 6 — Handover ready]  
> The case enters the arbitration queue, carrying the disagreement context, AI evidence, and the human reading record. The pathway is ready for consensus review.

---

## Shot list

| # | What is on screen | Action shown | Approx. duration |
|---|---|---|---|
| 1 | Mammogram viewer, no AI overlay | Case opens, four views visible | 4s |
| 2 | Reading workspace | Radiologist records no recall-level finding | 5s |
| 3 | Submit button / initial outcome | Submit action | 3s |
| 4 | AI result revealed in panel | AI finding appears: recall, 91% confidence | 5s |
| 5 | Disagreement detection state | System classifies disagreement, handover structured | 5s |
| 6 | Handover / arbitration queue entry | Case ready for consensus review | 4s |

---

## Terminology guide

**Use:**
- independent human reading
- initial reading outcome
- reading submitted
- AI result revealed after submission
- AI-human disagreement detected
- AI-positive / human-negative
- structured handover
- arbitration / consensus review
- disagreement pathway
- service layer

**Avoid:**
- "the doctor sees the AI mark first"
- "the doctor overrides the AI"
- "AI recommends recall" (AI suggests; human arbitration decides)
- "AI decides recall"
- "AI mark rejected / accepted by reader"

---

## Recording checklist

- [ ] Clear `localStorage` before recording: DevTools → Application → Clear site data
- [ ] Browser at 100% zoom, full screen or browser chrome hidden
- [ ] Mouse movements deliberate — pause ~0.5s before each click
- [ ] Confirm AI overlay is **not** visible at the start of the recording
- [ ] Confirm AI result panel appears only after submitting the reading
- [ ] Record at 1920×1080 or 2560×1440 to match presentation resolution

---

## Notes

This is the first video in the series. Keep it focused on the Reading Viewer flow only. The goal is to make the **Detect** moment legible — from independent reading to structured handover — without introducing every feature of the prototype.

Peer pause, ambient discussion capture, and learning library will be covered in subsequent videos.
