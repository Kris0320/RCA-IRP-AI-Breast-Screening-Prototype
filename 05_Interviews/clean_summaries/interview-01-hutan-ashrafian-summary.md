# Interview - Hutan Ashrafian

## Interviewee
Name: Hutan Ashrafian  
Role: to confirm; transcript suggests involvement in Google/healthcare AI research and breast screening AI implementation work  
Date: to confirm

Transcript quality note: the RTF appears to contain a poor automatic transcription plus reconstructed English and Chinese translation. Treat detailed wording as uncertain unless checked against the original audio.

## One-line relevance
This interview matters because it frames AI-assisted breast screening as an implementation, arbitration, and accountability problem rather than only a model-accuracy problem.

## Core insights

1. High-quality, real-world screening data is central to AI deployment. The interview links early Google/healthcare AI work to the need for large, high-quality mammography datasets, including UK and US data.

2. The UK breast screening context is valuable because of population scale, routine mammography, and broadly comparable imaging standards across several international settings.

3. Moving from published research into clinical practice requires prospective or real-world evidence. Hospitals, government bodies, and regulators are described as needing stronger clinical evidence before adoption.

4. The tested workflow placed AI as a second reader: first reader human, second reader AI, followed by standard arbitration when the two disagreed.

5. AI-human disagreement did not trigger a single consistent response. Some clinicians arbitrated any yes/no conflict, while others only escalated clearer or higher-risk positive cases.

6. The interview suggests AI may slightly improve accuracy and reduce routine reading workload, but that all cancer-suspicious cases still need human oversight.

7. Human arbitration can overrule AI even when AI is later shown to be correct. This is important for trust calibration: under-trust and dismissal of AI may be as risky as over-reliance.

8. Accountability remains legally and institutionally human-led. The transcript says that even when AI contributes to an error, blame or responsibility currently falls on human clinicians, arbitration panels, or hospitals rather than on AI itself.

## Evidence for our current direction

[[Universal Disagreement Pattern Map]]  
Supports the map because the interview describes AI placement as a variable in the workflow. AI as second reader changes where disagreement appears and how cases enter arbitration.

[[Specific Anchor Model]]  
Strongly supports anchoring the project in "AI as second reader + human-led arbitration". This model makes the disagreement moment concrete: a human reader and AI output feed into a comparison, then unresolved mismatch moves to arbitration.

[[Disagreement Handling Logic]]  
Supports the need for explicit escalation logic. The transcript describes inconsistent human responses to AI-human discrepancy, which suggests the workflow needs clearer rules for when a mismatch is ignored, reviewed, escalated, or audited.

## Useful quotes or paraphrases

- Paraphrase: The study placed AI in the role of the second reader, while the first reader remained human and normal arbitration followed.
- Paraphrase: Clinicians handled human-AI discrepancies differently; some escalated any conflict, while others escalated only obvious high-risk positives.
- Paraphrase: AI was sometimes overruled by humans even when AI was correct.
- Short quote from reconstructed transcript: "everyone still puts all the blame at the human."

## Design implications

- The service intervention should focus on the disagreement moment rather than the whole screening pathway.
- The prototype should show human judgement and AI output as parallel inputs into comparison, not as a linear chain where one simply replaces the other.
- Mismatch handling should include explicit trigger thresholds, escalation criteria, and a record of why arbitration did or did not happen.
- The audit trail should preserve the human read, AI output, arbitration outcome, and eventual learning evidence where available.
- The design should avoid presenting AI as the final decision-maker; the interview points to human and institutional accountability as the current reality.

## Open questions

- What was Hutan Ashrafian's exact role in the study or implementation work?
- What date was this interview conducted?
- What were the exact study sites and study design details?
- What specific disagreement categories were observed in the AI-as-second-reader trial?
- What level of AI confidence or risk score, if any, was available to arbitrators?
- How often did human arbitrators reject correct AI outputs, and how was correctness later established?
