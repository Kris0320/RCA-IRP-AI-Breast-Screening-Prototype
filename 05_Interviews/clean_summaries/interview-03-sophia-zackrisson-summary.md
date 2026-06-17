# Interview 03 — Sophia Zackrisson Summary

## 1. Interview Context

- Interviewee: Sophia Zackrisson.
- Role: Senior Consultant Radiologist / Professor of Radiology.
- Context: expert interview and prototype testing session for the RCA IRP AI Breast Screening project.
- Transcript note: the transcript is an automatic bilingual transcript with some mistranscribed phrases. Treat exact wording as provisional and use paraphrased evidence unless checked against audio.

This interview matters because Sophia gave a breast screening expert perspective on AI-assisted screening workflows, consensus review, prior image comparison, workload, and the prototype logic. The session tested whether our disagreement support layer made sense inside real screening practice, especially around soft cues, comparison review, handover, consensus / arbitration support, non-blame recording and outcome-linked learning.

## 2. What We Tested

- Prototype service logic: whether the Detect → Resolve → Learn pathway makes sense in AI-assisted breast screening.
- Soft comparison cue: whether a non-alarm cue is appropriate when human judgement and AI evidence layer differ.
- Comparison review: whether key evidence can be brought together without overloading the reader.
- Warm handover / review summary: whether context can travel into senior or consensus review.
- Consensus / arbitration support layer: whether support should sit inside difficult-case review rather than replace existing systems.
- Low-burden reasoning capture: whether suggested reason tags or confirmation-based recording are preferable to manual classification.
- Non-blame Decision Receipt: whether the decision rationale and evidence used should be recorded after arbitration.
- Outcome-linked learning and case library: whether selected cases can later become calibration cases after follow-up outcome is known.

## 3. Key Insights

1. AI-assisted breast screening workflows differ across systems. Sophia described multiple implementation patterns rather than one fixed pathway.

2. AI may act as a second reader, triage / risk stratification tool, or consensus support. In some workflows, AI replaces or supports a reader; in others, it routes low-risk and high-risk cases differently.

3. The project should not be tied to one fixed AI-as-second-reader workflow. The support layer should be able to sit across different AI placements where difficult AI-human cases appear.

4. Consensus / arbitration review remains important. Even when AI is introduced, difficult or discrepant cases may still move into a consensus list where radiologists compare images and make the final recall decision.

5. AI can function like a formal evidence-producing reader, not just a minor signal. AI scores, marks and thresholds can affect whether cases are escalated, discussed or dismissed.

6. Prior images and previous screening history are crucial in AI-human disagreement. A high AI score may be interpreted differently if the suspicious area is stable across previous mammograms or has already been investigated.

7. Radiologists work under high-throughput conditions, so every extra click matters. Additional prompts, manual cards or repeated classifications may undermine the efficiency benefit of AI.

8. Reasoning capture should be lightweight, automated where possible, and confirmation-based. The system could suggest a short rationale or reason tag that the reviewer confirms or edits, rather than asking radiologists to fill in long forms.

9. Learning loops should connect to existing audit, teaching, interval cancer review or case review practices. Learning is valuable, but it should not become a constant extra task inside every reading moment.

10. Extra wall displays, tea-room devices or daily-space interventions should be downgraded. Sophia advised that useful support should be integrated into existing reading stations and high-resolution clinical screens.

## 4. Prototype Feedback

### Soft cue / comparison review

Sophia’s feedback supports a soft cue rather than a strong warning. The cue should not interrupt every case or create extra work. It should appear only when comparison is useful and should help the reader inspect AI score, AI mark, human judgement, prior images and screening history.

### Consensus review support layer

The project should shift from a narrow “arbitration screen” to a consensus / difficult-case review support layer. In Swedish screening contexts, consensus review can involve radiologists reviewing all images and deciding whether recall is needed. The support layer should preserve context for this moment.

### Reasoning capture

Reasoning capture should be minimal. The prototype should move away from asking readers to manually classify many factors. It should favour auto-captured information, suggested tags and confirm / edit interactions.

### Decision receipt

The Non-blame Decision Receipt remains useful as a record of the decision rationale and evidence used at the arbitration / consensus moment. However, it should not immediately become a learning case because the follow-up outcome may not yet be known.

### Case library / learning loop

The case library should contain selected calibration cases, not every decision receipt. Cases should enter after follow-up outcomes are available and after an outcome-linked Learning Value Check confirms learning value.

### Arbitration test toolkit

The idea of a toolkit is useful for making service logic visible in testing, but future clinical use must be much lighter. If used, the toolkit should show what information might be needed in a consensus review rather than imply a new burden-heavy workflow.

## 5. Design Implications

- Reframe the project as a lightweight support layer for difficult AI-human cases across AI-assisted breast screening workflows.
- Avoid making the prototype dependent on one fixed AI-as-second-reader model.
- Rename or soften “arbitration” where appropriate as consensus review / difficult-case review.
- Keep the support inside existing workstations rather than designing a separate device, wall display or tea-room intervention.
- Make prior-image status and previous screening history more visible in the comparison logic.
- Reduce visible manual steps in the prototype: fewer cards, fewer prompts, fewer mandatory classifications.
- Use suggested reason tags such as “stable in prior images”, “AI high score but no visible change”, or “subtle lesion after prior comparison”.
- Keep the Decision Receipt as an immediate record, then wait for follow-up outcome before selecting calibration cases.
- Position the Disagreement Case Library as a scheduled review / teaching / audit resource, not a live reading burden.

## 6. Important Quotes / Evidence

- Paraphrase: AI can be introduced as a second reader, but it can also be used as a triage or risk stratification layer.
- Paraphrase: Discrepancies between a reader and AI, or between two human readers, commonly move into a consensus list where radiologists review images and make the final recall decision.
- Paraphrase: Prior images and previous investigations are central to deciding whether a high AI score is meaningful.
- Paraphrase: If the system adds too many prompts or manual steps, radiologists may dismiss them just to continue the work.
- Paraphrase: Support should be integrated into existing reading stations and high-resolution screens, not placed on extra devices or wall displays.
- Short transcript phrase: “keep it simple”.
- Short transcript phrase: “no extra steps for the radiologist”.
- Short transcript phrase: “integrate it into the reading stations”.

## 7. Links

- [[interview-03-sophia-zackrisson-transcript]]
- [[interview-03-sophia-zackrisson-evidence]]
- [[Expert Testing Design Implications]]
- [[Refined Prototype Storyline after Expert Testing]]
- [[Reflection Notes]]
