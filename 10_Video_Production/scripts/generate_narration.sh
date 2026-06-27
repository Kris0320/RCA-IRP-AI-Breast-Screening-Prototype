#!/bin/bash
# Run this from: 10_Video_Production/
# Output: exports/narration.aiff + exports/narration.mp3

mkdir -p exports

say -v Samantha -r 158 \
"Case B.S.V. 000254. The radiologist opens the screening case — four standard mammogram views. No A.I. output is visible. \
The radiologist reviews the images and marks a finding independently. They record their outcome: no further assessment needed. And submit. \
After submission, the A.I. result is revealed. Recall suggested — focal asymmetry, left breast, upper outer. High confidence, 91 percent. \
A disagreement is detected: A.I. positive, human negative. The Disagreement Support panel structures the case. The radiologist can zoom in to review exactly where the A.I. flagged concern. \
A peer pause is requested — a colleague notified. A reason is captured and saved to the decision trace. \
View Comparison lays out both readings side by side: suspicion score, patient context, and a similar reference case from the library. \
Prepare Handover generates the handover card — everything arbitration needs, packaged and ready. \
The case enters the Arbitration Queue." \
-o exports/narration.aiff

ffmpeg -i exports/narration.aiff exports/narration.mp3 -y

echo "✓ exports/narration.mp3 generated"
echo ""
echo "Next: run make_final_video.sh to combine with sped-up video"
