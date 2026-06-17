
# Presentation Structure

## Page 1 — Project Focus: AI-Human Disagreement in Breast Screening
Purpose: introduce the project focus and why AI-human disagreement matters.

## Page 2 — Universal Disagreement Pattern Map
Purpose: compare disagreement locations across models.

## Page 3 — From Universal Map to Specific Anchor
Purpose: explain why we choose AI as second reader + human-led arbitration.

## Page 4 — Specific Anchor Workflow / Human–AI Disagreement System Map
Purpose: show the concrete anchor workflow and system map.

## Page 5 — Disagreement Handling Logic
Purpose: Detect → Classify → Escalate → Resolve → Record → Learn.

## Page 6 — Prototype Direction / Intervention Concept
Purpose: show service package: protocol, review card, audit trail, learning loop.

## Supporting Model / Appendix — Accountability / Transparency / Consistency Matrix
Purpose: use as supporting material if it directly strengthens the prototype rationale or design requirements. Keep it outside the main six-page narrative unless the prototype needs an explicit value-to-requirement bridge.

---

# Current Narrative Flow

Working narrative: the project moves from a broad concern about AI-human disagreement in breast screening, through a comparative pattern map of AI placement, into a specific anchor workflow where the design intervention can be prototyped.

Tutorial 5 update: the anchor workflow now needs to be grounded in organisational reality. The presentation should make clear that the prototype is a service package for people, process and learning, not only a dashboard interface.

## Page 1 — Project Focus: AI-Human Disagreement in Breast Screening

### Slide purpose
Introduce the IRP focus and explain why AI-human disagreement is the critical moment for service design.

### Key message
AI-assisted breast screening is not only a detection problem. Once AI enters the reading workflow, the service must decide how disagreement is reviewed, escalated, recorded and learned from.

### Evidence sources from the vault
- [[Interview - Hutan Ashrafian]]
- [[Interview - Deborah Cunningham]]
- [[AI in Breast Cancer Screening Workflow: Pilot Implementation and Disagreement Scenarios]]
- [[FigJam Interview Synthesis]]
- [[FigJam Causes Effects Opportunities]]
- [[HMW and Design Direction]]

### Speaker notes draft
This project focuses on the moment when AI output and human judgement do not align. The research suggests that this moment is where questions of trust, accountability, workload and learning become visible. Rather than asking whether AI is simply accurate enough, the project asks what the screening system does when AI and human readers disagree.

### What visual is needed
A concise opening visual showing a mammogram reading context with two parallel sources: human judgement and AI output. It should introduce disagreement as the design focus, not show a full workflow yet.

## Page 2 — Universal Disagreement Pattern Map

### Slide purpose
Compare how different AI placement models shift where disagreement appears in breast screening workflows.

### Key message
There is no single universal NHS workflow. There is a shared screening backbone, and different AI placements create different disagreement patterns.

### Evidence sources from the vault
- [[Universal Disagreement Pattern Map]]
- [[Decision Log]]
- [[EDITH: Early Detection Using Information Technology in Health]]
- [[AI in Breast Cancer Screening Workflow: Pilot Implementation and Disagreement Scenarios]]
- [[FigJam Workflow Comparison 1]]
- [[FigJam Workflow Comparison 2]]

### Current SVG visual draft
![[page-2-universal-disagreement-pattern-map.svg]]

### Speaker notes draft
This map should be framed as a comparison tool, not a proposed universal NHS process. The four pattern numbers are placement labels, not a risk ranking. Each pattern changes where disagreement appears: before human reading, at comparison, after human reading as a safety net, or at triage boundaries. The purpose is to show that placement changes the kind of handling mechanism needed.

### What visual is needed
Use the current Page 2 draft as the base. It should show a shared screening backbone plus span bars for AI placement variations. The visual should avoid implying a single standard workflow or a low-to-high risk scale.

## Page 3 — From Universal Map to Specific Anchor

### Slide purpose
Explain why the project moves from a comparative pattern map to one concrete design anchor.

### Key message
The chosen anchor is "AI as second reader + human-led arbitration" because it makes comparison, mismatch, escalation and accountability visible.

### Evidence sources from the vault
- [[Specific Anchor Model]]
- [[Decision Log]]
- [[Interview - Hutan Ashrafian]]
- [[Interview - Deborah Cunningham]]
- [[Marinovich simulated arbitration evidence note]]
- [[FigJam Workflow Comparison 1]]

### Current SVG visual draft
![[page-3-from-universal-map-to-specific-anchor.svg]]

### Speaker notes draft
The universal map helps compare possible placements, but the design work needs a specific workflow point. The evidence points toward AI as a second reader or evidence layer because it creates an explicit comparison between human judgement and AI output. When they disagree, the system can trigger arbitration or senior review, then record the final decision and feed the case into learning.

### What visual is needed
Use the current Page 3 draft as the base. It should show the move from four placement patterns into the selected anchor. Human judgement and AI output should be shown as parallel sources feeding into comparison.

## Page 4 — Specific Anchor Workflow / Human–AI Disagreement System Map

### Slide purpose
Show the concrete workflow and system relationships for the selected anchor model.

### Key message
The intervention point is the Human–AI comparison: when human judgement and AI output diverge, the system should support disagreement handling / arbitration, a human-led final recall decision, and an audit & learning loop.

### Evidence sources from the vault
- [[Specific Anchor Model]]
- [[Disagreement Handling Logic]]
- [[Decision Log]]
- [[Interview - Hutan Ashrafian]]
- [[Interview - Deborah Cunningham]]
- [[FigJam Relationship Quadrant]]
- [[FigJam Causes Effects Opportunities]]
- [[Marinovich simulated arbitration evidence note]]
- [[Tutorial 5 - 2026-06-04]]

### Current SVG visual draft
![[page-4-specific-anchor-workflow-system-map.svg]]

### Speaker notes draft
This page makes the anchor operational. The human reader produces a judgement, while AI produces an output such as a risk score, flag or evidence layer. These should be treated as parallel sources, not as a linear chain where AI becomes the final decision-maker. The comparison stage identifies agreement, uncertainty or mismatch. If disagreement matters, the workflow moves into disagreement handling or arbitration, ending in a human-led final recall decision. Tutorial 5 adds that this system map must also show organisational grounding: actors, authority levels, arbitration roles, existing protocols and the learning loop that supports future judgement.

### What visual is needed
Build a new system map using consistent terminology:
- Mammogram acquired
- Case routed into review workflow
- Human judgement
- Human judgement recorded
- AI output
- AI output generated
- Human–AI comparison
- Disagreement detected
- Arbitration / senior review
- Final recall decision
- Audit & learning loop

The visual should show:
- Mammogram acquired, then case routed into review workflow.
- Human judgement and AI output as parallel inputs.
- Human judgement recorded and AI output generated before comparison.
- Human–AI comparison as the central decision point.
- Disagreement detected when the two sources diverge.
- Arbitration / senior review as a structured pathway, not an informal exception.
- Final recall decision as human-led.
- Audit & learning loop feeding back into training, calibration, monitoring or review.
- Optional support fields: confidence / risk score, override reason, arbitration rationale, timestamp, actor, later outcome.
- Clarify whether the visual shows current pilot state, future service state, or a before / after comparison.
- Include the relevant human hierarchy where useful: reader, senior / consultant reviewer, arbitration group or service lead.

## Page 5 — Disagreement Handling Logic

### Slide purpose
Turn the anchor workflow into a clear service logic for handling disagreement.

### Key message
The service mechanism is: Detect -> Classify -> Escalate -> Resolve -> Record -> Learn.

### Evidence sources from the vault
- [[Disagreement Handling Logic]]
- [[Decision Log]]
- [[Interview - Deborah Cunningham]]
- [[Interview - Hutan Ashrafian]]
- [[FigJam Causes Effects Opportunities]]
- [[FigJam Relationship Quadrant]]
- [[Marinovich simulated arbitration evidence note]]
- [[Tutorial 5 - 2026-06-04]]

### Speaker notes draft
The project is not proposing that AI should arbitrate or make the final decision. Instead, it proposes a structured way to manage disagreement. Detect the mismatch, classify the type and risk, escalate when needed, resolve through human-led arbitration or senior review, record what happened, and use difficult cases for later learning. Tutorial 5 strengthens the people/process side: resolving disagreement may require guided discussion, protocol, review practice, training, audit or workshop formats, not only software prompts.

### What visual is needed
A simple logic diagram or service blueprint strip showing the six steps. It should include what is captured at each step, especially AI output, human judgement, confidence / risk information, override reason, final decision and learning outcome.

## Page 6 — Prototype Direction / Intervention Concept

### Slide purpose
Show how the research becomes a service design intervention.

### Key message
The prototype should help clinicians review, decide, record and learn from AI-human disagreement, without treating AI as the final decision-maker.

### Evidence sources from the vault
- [[HMW and Design Direction]]
- [[Decision Log]]
- [[Disagreement Handling Logic]]
- [[FigJam Causes Effects Opportunities]]
- [[FigJam Relationship Quadrant]]
- [[Interview - Deborah Cunningham]]
- [[Interview - Hutan Ashrafian]]
- [[Tutorial 5 - 2026-06-04]]

### Speaker notes draft
The prototype direction is a clinician-facing disagreement support mechanism. It could include a comparison view, high-confidence second-look trigger, arbitration guidance, decision trace, override reason capture, and an audit / learning loop. After Tutorial 5, this should be framed as a service package rather than only a dashboard: a digital touchpoint plus protocol, guided review, learning workshop / case audit and validation questions for radiologists. The goal is not to make AI more dominant, but to make disagreement visible, accountable and useful for learning.

### What visual is needed
A prototype concept overview showing the service package:
- Comparison card or review panel.
- Disagreement trigger.
- Escalation / arbitration guide.
- Record or audit trail.
- Learning loop / case review.
- People/process layer: arbitration protocol, role hierarchy, review workshop, training or audit ritual.

# Next Visual to Build

## Page 4 — Specific Anchor Workflow / Human–AI Disagreement System Map

Build this next because it bridges the current Page 3 anchor selection and Page 5 handling logic.

Tutorial 5 revision: Page 4 should not only show the technical workflow. It should also show how the workflow sits inside an organisational setting, with actors, authority, existing review structures and learning touchpoints.

### Visual brief
Create a clear system map for the selected anchor model: **AI as second reader + human-led arbitration**.

Use consistent terminology:
- Mammogram acquired
- Case routed into review workflow
- Human judgement
- Human judgement recorded
- AI output
- AI output generated
- Human–AI comparison
- Disagreement detected
- Arbitration / senior review
- Final recall decision
- Audit & learning loop

### Required structure
Mammogram acquired  
-> Case routed into review workflow  
-> Human judgement recorded  
-> AI output generated  
-> Human–AI comparison  
-> Disagreement detected  
-> Arbitration / senior review  
-> Final recall decision  
-> Audit & learning loop

### Design notes
- Do not call AI a final decision-maker.
- Show AI as output, evidence, score or flag.
- Show arbitration as human-led.
- Show the audit trail as part of the workflow, not an afterthought.
- Include learning feedback to calibration, training, monitoring or case review.
- Highlight the disagreement moment and its impact clearly, then show how the future service resolves it.
