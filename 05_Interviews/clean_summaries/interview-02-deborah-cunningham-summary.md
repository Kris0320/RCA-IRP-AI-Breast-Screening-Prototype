# Interview - Deborah Cunningham

## Interviewee
Name: Deborah Cunningham  
Role: to confirm; transcript suggests an experienced breast screening radiologist / screening mammogram reader  
Date: to confirm

Transcript quality note: the transcript is clearer than Interview 01 but still includes automatic transcription errors, translated lines, and duplicated/truncated-looking sections. Treat short quotations as provisional.

## One-line relevance
This interview matters because it gives a clinician-facing account of how NHS breast screening arbitration works and where AI changes workload, trust, responsibility, and review.

## Core insights

1. Before AI, disagreement between two human readers is handled through arbitration, either by a third individual reader or through a consensus meeting of two or three radiologists.

2. Arbitration cases are also part of a learning loop. When a disagreed case later turns out to be cancer, readers review it to understand how one of the initial readers missed it.

3. AI has not yet been formally introduced into the British breast screening programme, according to the interview. Key barriers include uncertainty about algorithms, mammography hardware, and image post-processing.

4. Processed mammograms, not raw data, are used by both clinicians and AI. Changes in manufacturer post-processing can materially affect AI performance even when human readers are not confused by the change.

5. Different AI placement models create different risks. AI-first triage may reduce workload but raises responsibility questions if a case excluded from human review later proves cancerous.

6. Using AI as one reader may reduce routine reading workload but increase arbitration workload. The net efficiency gain is therefore not straightforward.

7. Human arbitrators may reject AI outputs even when AI is later shown to be right. This supports the need for trust calibration, confidence visibility, and careful review of high-confidence AI disagreement cases.

8. The interviewee suggests that recording should capture what each reader or AI output indicated and what the final decision was. This supports an audit trail around disagreement and final arbitration.

## Evidence for our current direction

[[Universal Disagreement Pattern Map]]  
Strongly supports the map because Deborah describes multiple AI placement options: AI triage before human review, AI as one reader, and AI outputs used to adjust arbitration. These are not a single universal workflow; they are placement patterns with different consequences.

[[Specific Anchor Model]]  
Supports the anchor model but also challenges its simplicity. Deborah says AI could be first or second reader and that the main issue is what happens in arbitration. This reinforces the choice to anchor on human-AI comparison and human-led arbitration, while leaving placement flexible.

[[Disagreement Handling Logic]]  
Strongly supports explicit trigger, guide, and record logic. The interview gives direct support for using AI confidence or likelihood to trigger another look, escalate cases, and reduce inappropriate overriding of correct AI outputs.

## Useful quotes or paraphrases

- Short quote: "The arbitration's done by the people."
- Short quote: "You can only know which one's correct by... Looking into the future."
- Paraphrase: Standard recording should include what each reader thought and what the final decision was.
- Paraphrase: If AI is highly confident and the human reader disagrees, the system could prompt the reader to look again.
- Paraphrase: Doctors may not need to see the AI's inner workings; confidence may come from reviewing its results across cases.

## Design implications

- The prototype should make disagreement actionable: detect the mismatch, show AI confidence or likelihood where available, and guide whether the case needs another look or formal arbitration.
- The design should record the human read, AI output, confidence/risk score if available, arbitration participants, final decision, and later ground-truth or learning outcome where available.
- Trust-building should be designed as calibration over time, not just explainability at one moment. Deborah's comments on a run-in period and PERFORMS suggest a training/review layer.
- AI output should be framed as evidence, likelihood, or abnormal/normal signal, not as a final clinical decision.
- The system should respect that radiologists already know human colleagues' reading tendencies; a useful AI service may help them learn the AI's tendencies in a similar way.
- A patient-facing transparency intervention seems less supported by this interview than a radiologist-facing workflow and confidence-calibration intervention.

## Open questions

- What is Deborah Cunningham's exact professional title and NHS role?
- What date was this interview conducted?
- Which arbitration model is most common in the relevant NHS breast screening setting: third-reader arbitration or consensus meeting?
- What minimum AI confidence/risk information would radiologists find useful without causing automation bias?
- How should high-confidence AI disagreement be displayed so it prompts review without pressuring the radiologist into blind agreement?
- What exact fields are currently recorded in breast screening arbitration systems?
- Could AI comparison be integrated into PERFORMS or a similar professional learning workflow?
- Who sets the AI operating threshold in a national screening programme, and how visible is that threshold to clinicians?
