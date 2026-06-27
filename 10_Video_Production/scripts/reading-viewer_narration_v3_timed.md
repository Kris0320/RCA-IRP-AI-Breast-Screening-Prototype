# Reading Viewer — Timed Narration v3

**Video:** `prototype-recording-part1-v1.mp4` (66.4s raw)  
**Target output:** 50s (video sped up to 1.33×)  
**Narration length:** ~100 words · ~50s at 120 wpm  

---

## Cues timed to the 1.33× sped-up video

| Video cue (50s version) | What's on screen | Narration |
|---|---|---|
| **0:00** | Case opens, 4 views, no AI | *Case BSV-000254. The radiologist opens the screening case — four standard mammogram views. No AI output is visible.* |
| **0:05** | User marks finding (red circle, BI-RADS 2) | *The radiologist reviews the images and marks a finding independently.* |
| **0:08** | Submit modal — No further assessment selected | *They record their outcome: no further assessment needed. And submit.* |
| **0:12** | AI result revealed, orange + red markers appear | *After submission, the AI result is revealed. Recall suggested — focal asymmetry, left breast, upper outer. High confidence, 91%.* |
| **0:20** | Disagreement panel appears right side | *A disagreement is detected: AI-positive, human-negative. The Disagreement Support panel structures the case.* |
| **0:26** | Zoomed L-CC with AI orange marking | *The radiologist can zoom in to review exactly where the AI flagged concern.* |
| **0:29** | Peer pause triggered, review note dropdown | *A peer pause is requested — a colleague notified. A reason is captured and saved to the decision trace.* |
| **0:36** | View Comparison panel open | *View Comparison lays out both readings side by side: suspicion score, patient context, and a similar reference case from the library.* |
| **0:44** | Warm Handover Card generated | *Prepare Handover generates the handover card — everything arbitration needs, packaged and ready.* |
| **0:48** | Open Arbitration Queue button lit | *The case enters the Arbitration Queue.* |

---

## Full narration (continuous read · ~100 words)

> Case BSV-000254. The radiologist opens the screening case — four standard mammogram views. No AI output is visible.
>
> The radiologist reviews the images and marks a finding independently. They record their outcome: no further assessment needed. And submit.
>
> After submission, the AI result is revealed. Recall suggested — focal asymmetry, left breast, upper outer. High confidence, 91%.
>
> A disagreement is detected: AI-positive, human-negative. The Disagreement Support panel structures the case. The radiologist can zoom in to review exactly where the AI flagged concern.
>
> A peer pause is requested — a colleague notified. A reason is captured and saved to the decision trace.
>
> View Comparison lays out both readings side by side: suspicion score, patient context, and a similar reference case from the library.
>
> Prepare Handover generates the handover card — everything arbitration needs, packaged and ready.
>
> The case enters the Arbitration Queue.

---

## How to generate audio (macOS Terminal)

Run this in Terminal — it generates `narration.aiff` in your current folder:

```bash
say -v Samantha -r 158 \
"Case B.S.V. 000254. The radiologist opens the screening case — four standard mammogram views. No A.I. output is visible. \
The radiologist reviews the images and marks a finding independently. They record their outcome: no further assessment needed. And submit. \
After submission, the A.I. result is revealed. Recall suggested — focal asymmetry, left breast, upper outer. High confidence, 91 percent. \
A disagreement is detected: A.I. positive, human negative. The Disagreement Support panel structures the case. The radiologist can zoom in to review exactly where the A.I. flagged concern. \
A peer pause is requested — a colleague notified. A reason is captured and saved to the decision trace. \
View Comparison lays out both readings side by side: suspicion score, patient context, and a similar reference case from the library. \
Prepare Handover generates the handover card — everything arbitration needs, packaged and ready. \
The case enters the Arbitration Queue." \
-o narration.aiff
```

**Notes on `say` flags:**
- `-v Samantha` — best built-in English voice (natural cadence)
- `-r 158` — words per minute; adjust up/down ±10 to tune length
- `-o narration.aiff` — output file; convert to mp3 with: `ffmpeg -i narration.aiff narration.mp3`

---

## ffmpeg: speed up video to 50s

```bash
ffmpeg -i "prototype-recording- part1-v1.mp4" \
  -vf "setpts=0.75*PTS" \
  -an \
  "reading-viewer_video_50s.mp4"
```

`setpts=0.75*PTS` = 1.33× speed → 66.4s becomes ~50s. `-an` removes original audio (no audio track to keep).

---

## Merge video + narration audio

```bash
ffmpeg \
  -i "reading-viewer_video_50s.mp4" \
  -i narration.mp3 \
  -c:v copy -c:a aac \
  -shortest \
  "reading-viewer_final_50s.mp4"
```

Output: `reading-viewer_final_50s.mp4` — ready for presentation.
