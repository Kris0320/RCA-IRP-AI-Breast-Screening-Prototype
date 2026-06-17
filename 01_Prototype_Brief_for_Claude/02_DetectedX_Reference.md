# DetectedX Reference

## What DetectedX is useful for

- Case-based mammography reading
- Diagnosis practice
- Reader calibration
- Feedback after case decisions
- Peer comparison and benchmarking

## What DetectedX does not cover

- AI-human disagreement handling
- Arbitration workflow
- Responsibility handover
- Decision traceability between human and AI judgement
- Learning loop from disagreement cases

## How we use it

Use DetectedX as a reference environment, not as something to copy. The prototype should borrow the general idea of a case-based mammography reading interface, then add a service design layer for AI-human disagreement, handover, arbitration and learning.

## Reference screenshots and how to use them

The screenshots in `assets/references-detectedx/` are used only to understand interaction patterns and visual context from a case-based mammography reading and learning platform. They should not be copied directly. Do not copy DetectedX branding, exact UI, proprietary text, layout, or visual assets. Translate the observed patterns into an original prototype focused on AI-human disagreement handling.

- `detectedx-01-case-selection-01.png` and `detectedx-01-case-selection-02.png`
  Show the case-based learning / test selection structure. Useful only for understanding the learning platform context. Do not build a full course platform.

- `detectedx-02-viewer-main-01.png` and `detectedx-02-viewer-main-02.png`
  Show the dark mammography viewer structure: left series thumbnails, central multi-view mammogram layout, top toolbar, and image-first reading environment. These are the most important visual references for the prototype.

- `detectedx-03-toolbar.png`
  Shows typical viewer tools such as pan, zoom, magnify, window, mark, freehand, reset, grid, and sync. Use this to create a simplified simulated toolbar, not a real DICOM viewer.

- `detectedx-04-decision-submit-01.png` and `detectedx-04-decision-submit-02.png`
  Show structured human judgement input, including lesion type, BI-RADS style rating, and recall decision. Use this as a reference for the human judgement panel.

- `detectedx-05-decision-delete.png`
  Shows mark editing and deletion. This is optional and should not be prioritised in the first prototype.

- `detectedx-05-results-01.png`
  Shows performance feedback after reading, including sensitivity, specificity, lesion sensitivity, ROC, and JAFROC. Use this only as inspiration for the later learning loop, not as the main interface.

- `detectedx-06-results-peer-comparison-01.png` and `detectedx-06-results-peer-comparison-02.png`
  Show peer comparison and calibration logic. Use this as a precedent for the Care Loop / team calibration concept.

- `detectedx-07-case-answers-01.png` and `detectedx-07-case-answers-02.png`
  Show expert answers, marked lesions, and feedback after submission. Use this as inspiration for how a disputed case can later become a reviewable learning case.
