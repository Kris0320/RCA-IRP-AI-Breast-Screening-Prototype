# Simulated Arbitration of Discordance Between Radiologists and AI

## Source file
![[marinovich-et-al-2024-simulated-arbitration-of-discordance-between-radiologists-and-artificial-intelligence.pdf]]

## Source type
Paper

## Relevance to our project
This source is directly relevant because it focuses on what happens when radiologist and AI interpretations are discordant in breast screening. It supports the IRP argument that disagreement is not a small edge case: it is a workflow, arbitration, and monitoring problem that determines whether AI improves detection or creates new harms.

## Key points for AI-assisted breast screening
- The paper studies AI as a potential replacement for one radiologist in mammography double-reading.
- It uses a large retrospective cohort from BreastScreen WA with 108,970 consecutive screening examinations.
- The authors argue that retrospective studies may underestimate cancer detection and recall when they do not realistically resolve radiologist/AI discordance.
- AI may help identify interval cancers, but benefits depend on how discordant cases are arbitrated.

## Key points for AI placement / workflow
- The workflow being studied pairs a first reader with AI as the replacement for another reader.
- The key workflow issue is not only whether AI performs well, but how discordance between Reader 1 and AI is escalated or resolved.
- The paper distinguishes real-world arbitration outcomes from simulated arbitration where no real arbitration occurred.
- It shows that evaluation methods need to model the arbitration step, not only the initial AI-human comparison.

## Key points for disagreement / arbitration / accountability
- Of 21,960 Reader 1 / AI discordant screens, 20,120 had no real-world arbitration outcome.
- The paper argues that using historical second-reader findings to resolve AI-human discordance can be biased because AI findings were unavailable to that reader.
- Cancer detection gains depend on a majority of interval cancers being detected in radiologist/AI discordant screens.
- Recall is likely to increase if AI is deployed as a reader in double-reading, so recall must be closely monitored.
- The paper strongly supports the need for explicit arbitration logic, disagreement capture, and later monitoring.

## Possible evidence to cite later
- AI-human discordance requires a designed arbitration process; it cannot be treated as a simple retrospective comparison.
- Retrospective evidence may underestimate both CDR and recall if discordance is handled poorly.
- Any cancer detection improvement may come with higher recall, making workload and false-positive monitoring central to service design.
- Useful evidence for why the prototype should include trigger, guide, and record functions.

## Limitations / caution
This source is not NHS-specific; it is based on BreastScreen WA in Australia. It uses simulation rather than a live clinical arbitration intervention, so it is best used to support the logic of arbitration design and monitoring rather than to claim real-world NHS performance.

## Linked notes
- [[Universal Disagreement Pattern Map]]
- [[Specific Anchor Model]]
- [[Disagreement Handling Logic]]
- [[HMW and Design Direction]]
