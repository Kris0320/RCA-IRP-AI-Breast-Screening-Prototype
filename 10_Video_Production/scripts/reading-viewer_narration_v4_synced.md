# Reading Viewer — Narration v4 (action-synced)

**Video:** prototype-recording-part1-v1.mp4 (66.4s raw → 50s at 1.33×)  
**Method:** Each line fires when that action appears on screen  
**Word count:** ~80 words · leaves breathing room between cues

---

## Cue map (times = 1.33× sped-up video)

| Time in 50s video | On screen | Say this |
|---|---|---|
| **0:00** | 4 mammogram views load, no AI | *The radiologist opens the case. Four standard views — no AI output visible.* |
| **0:04** | BI-RADS popup, Benign·2 selected | *They mark a finding and classify it.* |
| **0:06** | Mark saved (red circle on image) | *(brief pause — let the mark land)* |
| **0:08** | Cursor moves toward Submit reading | *The reading is submitted.* |
| **0:11** | Modal: No further assessment → Submit | *Outcome recorded: no further assessment.* |
| **0:13** | AI markers (orange) appear on mammogram | *The AI result is revealed after submission —* |
| **0:15** | Disagreement panel slides in right | *— focal asymmetry, high confidence. A disagreement is detected.* |
| **0:18** | Panel: AI-POSITIVE / HUMAN-NEGATIVE tags | *AI-positive. Human-negative. The service layer structures what happened.* |
| **0:22** | User hovering over AI finding label on image | *The AI flagged a different location to the reader.* |
| **0:26** | Cursor scanning the right panel | *Human reading and AI result sit side by side — the gap is made visible.* |
| **0:30** | Peer pause triggered | *A peer pause is requested — a colleague is notified.* |
| **0:33** | Review note dropdown (reason list) | *A reason is captured and saved to the decision trace.* |
| **0:36** | View Comparison panel opens | *View Comparison shows the full picture: both readings, suspicion score, a reference case.* |
| **0:42** | Prepare Handover → Handover Card | *Prepare Handover packages the case. Everything arbitration needs — ready to go.* |
| **0:47** | Open Arbitration Queue button | *The case enters the Arbitration Queue.* |

---

## Continuous narration (read straight through — ~80 words)

> The radiologist opens the case. Four standard views — no AI output visible.
>
> They mark a finding and classify it.
>
> The reading is submitted. Outcome recorded: no further assessment.
>
> The AI result is revealed after submission — focal asymmetry, high confidence. A disagreement is detected.
>
> AI-positive. Human-negative. The service layer structures what happened. The AI flagged a different location to the reader. Human reading and AI result sit side by side — the gap is made visible.
>
> A peer pause is requested — a colleague is notified. A reason is captured and saved to the decision trace.
>
> View Comparison shows the full picture: both readings, suspicion score, a reference case.
>
> Prepare Handover packages the case. Everything arbitration needs — ready to go.
>
> The case enters the Arbitration Queue.

---

## Voice quality

Standard `say -v Samantha` sounds robotic. Use the **Enhanced** version instead:

1. Open **System Settings → Accessibility → Spoken Content → System Voice → Customise**
2. Find **Samantha** → click the download arrow next to **Samantha (Enhanced)**
3. Wait for download, then use `-v "Samantha (Enhanced)"` in the command below

Alternative enhanced voices worth trying: `Ava (Enhanced)`, `Allison (Enhanced)`, `Susan (Enhanced)`

---

## Generate audio (run in Terminal from 10_Video_Production/)

```bash
bash scripts/generate_narration_v4.sh
```
