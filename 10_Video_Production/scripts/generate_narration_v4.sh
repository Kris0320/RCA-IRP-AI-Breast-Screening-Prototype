#!/bin/bash
# Run from: 10_Video_Production/
# Output: exports/narration_v4.mp3
#
# FIRST: download "Samantha (Enhanced)" in
# System Settings → Accessibility → Spoken Content → System Voice → Customise
# Then re-run this script.

mkdir -p exports

VOICE="Siri (Voice 3)"

# Check if Enhanced voice is available; fall back to standard
if say -v "$VOICE" "" 2>/dev/null; then
  echo "Using: $VOICE"
else
  VOICE="Samantha"
  echo "Enhanced voice not found — using standard Samantha. Download it for better quality."
fi

# Timing targets (50s sped-up video):
#   0:00  opener
#   0:02  mark action
#   0:06  submit reading
#   0:09  no further assessment / submit modal
#   0:11  AI revealed
#   0:13  panel slides in / disagreement detected
#   0:16  AI-POSITIVE HUMAN-NEGATIVE
#   0:20  exploring panel / marks
#   0:28  peer pause triggered
#   0:32  review note / reason dropdown
#   0:35  view comparison opens
#   0:40  prepare handover
#   0:46  arbitration queue

say -v "$VOICE" -r 155 \
"A routine screening case. \
[[slnc 1000]] \
The radiologist marks a finding — BI-RADS 2. \
[[slnc 1400]] \
The reading is submitted. No further assessment. \
[[slnc 600]] \
After submission, the AI result appears — recall suggested. Focal asymmetry. High confidence. \
[[slnc 300]] \
A disagreement is detected. AI-positive, human-negative. \
[[slnc 400]] \
The service layer surfaces both results — the gap is made visible. \
[[slnc 7500]] \
A peer pause is requested — a colleague notified. \
[[slnc 300]] \
A reason is captured and saved to the decision trace. \
[[slnc 500]] \
View Comparison: both readings, suspicion score, a reference case. \
[[slnc 1200]] \
Prepare Handover packages the case — everything arbitration needs, ready to go. \
[[slnc 800]] \
The case enters the Arbitration Queue." \
-o exports/narration_v4.aiff

ffmpeg -i exports/narration_v4.aiff exports/narration_v4.mp3 -y -loglevel error

echo ""
echo "✓ exports/narration_v4.mp3 done"
echo "Next: bash scripts/make_final_video_v4.sh"
