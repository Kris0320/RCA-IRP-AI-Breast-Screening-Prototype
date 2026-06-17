# Decision Log

Purpose: track project decisions that affect the IRP presentation, prototype direction, and model language.

## 1. Use "Universal Disagreement Pattern Map", Not "Universal Workflow"

**Decision**  
Use "Universal Disagreement Pattern Map", not "Universal Workflow".

**Reason**  
Avoid implying one universal NHS workflow. The map is a comparative pattern map for showing how disagreement shifts across AI placement models.

**Impact on presentation / prototype**  
Presentation Page 2 should show a shared backbone plus AI placement variations, not a proposed universal NHS process.

**Related notes**  
- [[Universal Disagreement Pattern Map]]
- [[Specific Anchor Model]]

## 2. Use Pattern Numbers 1-4 as Placement Labels, Not Risk Ranking

**Decision**  
Use pattern numbers 1-4 as placement labels, not risk ranking.

**Reason**  
The four AI placement patterns create different risk types, not a linear risk severity scale.

**Impact on presentation / prototype**  
Numbers should help connect span bars and cards, but should not imply low-to-high risk.

**Related notes**  
- [[Universal Disagreement Pattern Map]]

## 3. Use Span Bars to Show Workflow Segments, Not Point Annotations

**Decision**  
Use span bars to show workflow segments, not point annotations.

**Reason**  
Each AI placement modifies a segment of the shared screening backbone, not a single node.

**Impact on presentation / prototype**  
Page 2 should use span bars from one workflow node to another, so the viewer understands each pattern as a workflow variation.

**Related notes**  
- [[Universal Disagreement Pattern Map]]

## 4. Anchor Intervention in "AI as Second Reader + Human-Led Arbitration"

**Decision**  
Anchor intervention in "AI as second reader + human-led arbitration".

**Reason**  
This model makes AI-human disagreement, comparison, escalation and accountability visible.

**Impact on presentation / prototype**  
The following design work should focus on comparison, mismatch detection, arbitration / senior review, audit trail and learning loop.

**Related notes**  
- [[Specific Anchor Model]]
- [[Disagreement Handling Logic]]

## 5. Show Human Judgement and AI Output as Parallel Sources

**Decision**  
Show human judgement and AI output as parallel sources.

**Reason**  
A linear sequence may wrongly imply one judgement influences the other. The anchor model should show two judgement sources feeding into comparison.

**Impact on presentation / prototype**  
Presentation Page 3 and future workflow diagrams should show human judgement and AI output as parallel inputs into comparison / mismatch.

**Related notes**  
- [[Specific Anchor Model]]
- [[Universal Disagreement Pattern Map]]

## 6. Avoid Calling AI a Final Decision-Maker

**Decision**  
Avoid calling AI a final decision-maker.

**Reason**  
AI is treated as an evidence / output layer. The human-led workflow remains responsible for arbitration and final recall decision.

**Impact on presentation / prototype**  
Use "AI output", "AI risk score", "AI evidence", or "AI-supported flag" instead of "AI decision".

**Related notes**  
- [[Specific Anchor Model]]
- [[Disagreement Handling Logic]]

## 7. Prototype as a Service Package, Not Just a Dashboard

**Decision**  
Frame the prototype as a disagreement support service package, not only as a dashboard or interface.

**Reason**  
Tutorial 5 clarified that AI-human disagreement is a people, process and organisational problem as much as a technology problem. A dashboard can signal disagreement, but it does not by itself resolve trust, authority, arbitration dynamics, learning, or role-based decision making.

**Impact on presentation / prototype**  
Page 4 should show organisational grounding around the anchor workflow, including actors, hierarchy, arbitration roles and learning touchpoints. Page 6 should present a service package: digital comparison surface, arbitration protocol, decision record, case audit, learning workshop / training loop and radiologist validation questions.

**Related notes**  
- [[Tutorial 5 - 2026-06-04]]
- [[Specific Anchor Model]]
- [[Disagreement Handling Logic]]
- [[Presentation Structure]]
