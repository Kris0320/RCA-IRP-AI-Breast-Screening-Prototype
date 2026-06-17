# Refined Prototype Storyline after Expert Testing

A radiologist is reading mammograms in the existing screening workflow. The work is fast, repetitive and highly focused, so the prototype does not redesign the whole radiology system.

In this case, the AI risk score is high and the AI marks a suspicious area. But the radiologist is not fully convinced. She compares the current image with prior images and feels the area may have been stable for years. So the issue is not simply “AI is right” or “human is wrong”. It is a difficult case where AI risk signal, reader judgement and patient history need to be compared carefully.

Instead of showing a strong alarm, the system gives a soft comparison cue. It reminds the reader that the AI risk signal and the human judgement need review. A lightweight comparison layer appears inside the existing workstation and brings together the key information: AI score, AI suspicious mark, reader judgement, prior image status, image quality and suggested reason tags.

If the case needs further review, the system creates a short handover summary automatically. The next reviewer receives the case with context: why the case is difficult, what the AI marked, what the first reader considered, and what needs attention.

During consensus review, senior reviewers still make the final decision. The support layer does not decide for them. It helps them compare the AI signal, suspicious region, prior images and human reasoning. If needed, the system can suggest a simple rationale, such as “stable in prior images” or “AI high score but no visible change”. The reviewer only confirms or edits it instead of filling in a long form.

After the decision, the system creates a non-blame decision receipt. It records the final pathway decision, evidence used and reasoning at that moment.

Later, when follow-up outcomes are available, selected cases with learning value can become calibration cases and enter a disagreement case library. The library supports existing audit meetings, teaching sessions and team calibration.

## Links

- [[Expert Testing Design Implications]]
- [[interview-03-sophia-zackrisson-summary]]
- [[Prototype Direction]]
