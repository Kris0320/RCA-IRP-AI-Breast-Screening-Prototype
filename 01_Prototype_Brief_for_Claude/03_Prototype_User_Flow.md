# Prototype User Flow

## Demo flow

1. User opens Case `BSV000254` in a dark mammography viewer.
2. Viewer shows four mammogram views: `L-CC`, `R-CC`, `L-MLO`, `R-MLO`.
3. User reviews the case independently.
4. User selects initial human judgement: `No recall`.
5. User clicks `Submit initial judgement`.
6. AI result is revealed:
   - AI judgement: `Recall`
   - AI confidence: `High`
   - Finding type: `Focal asymmetry`
   - Location: `Left breast, upper outer area`
7. System detects disagreement:
   - Human: `No recall`
   - AI: `Recall`
   - Disagreement type: `High-confidence AI positive vs human negative`
8. A soft panel appears:
   - Title: `AI-Human Disagreement Detected`
   - Tone: calm, non-blaming, supportive
9. User chooses `Prepare warm handover`.
10. Warm Handover Card appears.
11. User clicks `Generate decision receipt`.
12. Non-blame Decision Receipt appears.
13. Case is added to the Disagreement Case Library:
   - `This case has been added to the Disagreement Case Library.`
   - `Available for team calibration and future arbitration reference.`
   - `Pattern observed: AI-positive / human-negative · detection gap`

<!-- previously: "Care Loop" — archived in ARCHIVE_care-loop-original-copy.md -->

## Flow intent

The demo should show that the initial human judgement is independent, then the AI output introduces a disagreement that requires structured handling rather than blame or simple override.
