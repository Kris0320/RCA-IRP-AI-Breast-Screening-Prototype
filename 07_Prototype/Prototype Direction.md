# Prototype Direction

## Why the prototype changed after Tutorial 5

After [[Tutorial 5 - 2026-06-04]], the prototype should no longer be framed as only a dashboard or interface. The tutor pushed the project beyond screen-based signalling toward a fuller service package that addresses people, process, organisational grounding and learning.

The key shift is that AI-human disagreement is not just a data display problem. It is also a human judgement, authority, arbitration, accountability and learning problem. A dashboard may help surface disagreement, but the service also needs to support how people classify, discuss, escalate, resolve, record and learn from disagreement.

Working prototype frame:

**Disagreement Care Service Package**

Core service logic:

**Detect -> Resolve -> Learn**

Detailed mechanism:

- **Detect** = flag + classify disagreement
- **Resolve** = escalate + arbitrate + record rationale
- **Learn** = audit + review difficult cases + feed learning back into practice

## What problem the prototype addresses

Current AI-assisted breast screening may surface AI-human disagreement, but lacks a structured way to classify, resolve, record and learn from it.

The problem is not only that human judgement and AI output may differ. The deeper issue is that the service may not clearly show what kind of disagreement it is, who should review it, what evidence is needed, why AI or human judgement was overridden, and how the case becomes useful for future learning.

## As-is journey

- Case enters review workflow.
- Human judgement recorded.
- AI output generated.
- Human-AI mismatch appears.
- Arbitration happens.
- Final recall decision is made.
- But disagreement rationale and learning record may be weak.

As-is risk:

- AI value may be lost if correct AI signals are overridden without trace.
- Human accountability pressure remains even when AI contributes to uncertainty.
- Arbitration workload may increase without better decision support.
- Difficult cases may not become structured learning material.

## Future service package

The future service package changes the journey by adding structured support around the disagreement moment.

- A disagreement flag makes the mismatch visible and classifies the type of disagreement.
- An arbitration review workspace gives the senior reviewer / arbitration group the right evidence, comparison view and rationale capture.
- A learning memory card turns difficult disagreement cases into reviewable patterns for audit, training and future practice.

The service is not designed to let AI make final decisions. It treats AI as an evidence layer and supports human-led arbitration, final recall decision making and learning.

## Touchpoint 1 — Disagreement Flag / Detection Card

**Purpose**  
Detect and classify the disagreement between human judgement and AI output.

**User**  
Human reader, senior reviewer, arbitration coordinator or breast screening team member.

**Moment**  
After human judgement and AI output are both available, before escalation or arbitration.

**Key information**  
- Human judgement
- AI output / risk score / confidence
- Agreement or mismatch
- Disagreement type
- Suggested escalation level
- Whether the case needs second look, arbitration or routine path

**Design question**  
How can the system flag disagreement clearly without creating automation bias, alarm fatigue or unnecessary workload?

## Touchpoint 2 — Arbitration Review Workspace

**Purpose**  
Support human-led arbitration by bringing together evidence, comparison, disagreement classification and rationale capture.

**User**  
Senior / consultant radiologist, arbitration group, or reviewer responsible for final recall recommendation.

**Moment**  
When disagreement is significant enough to require arbitration, senior review or a structured second look.

**Key information**  
- Mammogram and relevant prior images
- Human judgement and notes
- AI output, risk score, confidence or suspicious area
- Disagreement category
- Escalation reason
- Arbitration rationale
- Override reason if human judgement or AI output is not followed
- Final recall decision

**Design question**  
What evidence does an arbitrator need in order to resolve disagreement confidently, explain the rationale and avoid treating AI as the final decision-maker?

## Touchpoint 3 — Learning Memory Card / Pattern Review

**Purpose**  
Turn difficult or repeated disagreement cases into learning material for audit, calibration and future practice.

**User**  
Radiologists, senior reviewers, service leads, training leads, audit teams or AI governance groups.

**Moment**  
After final recall decision, especially when later outcomes, audit results or repeated disagreement patterns become available.

**Key information**  
- Case summary
- Human judgement
- AI output / risk score
- Disagreement type
- Arbitration rationale
- Final recall decision
- Later outcome if available
- Learning flag / pattern category
- Suggested review or training theme

**Design question**  
How can disagreement records become useful learning material rather than passive archive data?

## Priority disagreement scenarios to prototype

- Human low-risk / AI high-risk
- Human high-risk / AI low-risk
- AI high-confidence flag / human disagreement

## What to validate with radiologists

1. What categories of AI-human disagreement are meaningful in real screening practice?
2. When should a disagreement be ignored, flagged, second-looked, or escalated to arbitration?
3. What evidence would you need to see before trusting an AI high-risk flag?
4. What evidence would you need before overriding AI output?
5. How should override reasons be recorded without adding excessive workload?
6. Would AI confidence / risk score help arbitration, or could it create bias?
7. Who should see the disagreement flag: first reader, second reader, senior reviewer, arbitration group or service lead?
8. What would make a disagreement review feel like useful clinical support rather than surveillance or blame?
9. How should difficult disagreement cases feed into learning: audit meeting, workshop, training set, PERFORMS-style review or informal case library?
10. What accountability concerns would this service need to address before it could fit into a real breast screening workflow?

## Related notes

- [[Tutorial 5 - 2026-06-04]]
- [[Prototype Sketch Synthesis - Disagreement Support Layer]]
- [[Specific Anchor Model]]
- [[Disagreement Handling Logic]]
- [[Decision Log]]
- [[Presentation Structure]]
