
# Universal Disagreement Pattern Map

## Why not call it a universal workflow?

We should avoid calling it a universal workflow because it may sound like we are proposing a single standard NHS process.

Instead, this should be framed as a **Universal Disagreement Pattern Map**.

It is not a workflow that every hospital follows. It is a cross-model pattern map used to compare how AI placement changes where disagreement appears in AI-assisted breast screening.

## What it is

A cross-model pattern map that compares how AI placement shifts disagreement across AI-assisted breast screening workflows.

It helps us answer:

1. Where does disagreement happen?
2. What kind of disagreement does each AI placement create?
3. What kind of handling, escalation, recording or learning mechanism is needed?

## Shared screening backbone

Mammogram acquired  
→ Case enters reading workflow  
→ Human / AI interpretation  
→ Comparison or risk judgement  
→ Disagreement / uncertainty handling  
→ Final decision  
→ Audit / learning

## Key variable

The key variable is **AI placement in relation to human readers**.

Different placements do not just change the workflow sequence. They change where disagreement appears, who sees it, and what kind of responsibility or escalation is required.

## Four AI placement patterns

### 1. AI before reading

AI output is visible before human judgement.

**Where disagreement appears:**  
Before or during human interpretation.

**Risk:**  
Automation bias, over-trust, under-trust, or influence on independent judgement.

**Possible handling need:**  
Independent reading protection, delayed AI reveal, trust calibration, reader training.

---

### 2. AI as second reader

AI replaces or supports one reading position.

**Where disagreement appears:**  
At comparison / arbitration.

**Risk:**  
AI-human mismatch, unclear override rationale, uncertainty about when to escalate.

**Possible handling need:**  
Disagreement classification, arbitration protocol, override reason, audit trail.

---

### 3. AI as safety net

AI checks after human reading.

**Where disagreement appears:**  
After human judgement, when AI flags a possible missed case.

**Risk:**  
Late escalation, missed-case anxiety, uncertainty about whether to reopen or override a human decision.

**Possible handling need:**  
Second-look trigger, risk threshold, senior review, case review log.

---

### 4. AI as triage

AI sorts cases into low-risk and high-risk routes.

**Where disagreement appears:**  
At allocation boundaries.

**Risk:**  
Routing disagreement, workload redistribution, uncertainty about whether low-risk cases are safely excluded from full human reading.

**Possible handling need:**  
Triage threshold governance, exception handling, sample audit, monitoring loop.

## Design question

Where does disagreement happen?  
How should it be resolved, recorded and learned from?

## Design implication

The universal pattern map is useful for analysis, but it should not be the final design model.

For intervention, we still need a **specific anchor model** with concrete actors, workflow steps and escalation points.

Current preferred anchor:

**AI as second reader + human-led arbitration**

This model makes the AI-human disagreement moment explicit and gives the project a concrete point for prototyping.

## Links

- [[Specific Anchor Model]]
- [[Disagreement Handling Logic]]
- [[Tutorial 4 - 2026-05-28]]