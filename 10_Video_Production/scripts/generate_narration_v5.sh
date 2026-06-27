#!/bin/bash
# Narration v5 — precise per-sentence placement using ffmpeg adelay
# Each sentence is placed at an EXACT millisecond, no guessing with [[slnc]]
#
# Run from: 10_Video_Production/
# Output:   exports/narration_v5.mp3
#
# Cue targets (50s sped-up video):
#   0:00  opener
#   0:02  mark action
#   0:06  submit reading
#   0:09  no further assessment selected + submit
#   0:11  AI revealed (orange markers appear)
#   0:14  disagreement panel slides in
#   0:17  AI-POSITIVE / HUMAN-NEGATIVE tags visible
#   0:28  peer pause triggered
#   0:32  review note / reason dropdown
#   0:35  view comparison panel opens
#   0:40  prepare handover clicked
#   0:46  arbitration queue button

set -e
mkdir -p exports/segments

VOICE="Samantha (Enhanced)"
if ! say -v "$VOICE" "" 2>/dev/null; then
  VOICE="Samantha"
  echo "Note: using standard Samantha. For better quality, download Samantha (Enhanced) in:"
  echo "System Settings → Accessibility → Spoken Content → System Voice → Customise"
fi

echo "Generating sentence segments..."

say -v "$VOICE" -r 155 "A routine screening case."                                         -o exports/segments/s01.aiff
say -v "$VOICE" -r 155 "The radiologist marks a finding — BI-RADS 2."                     -o exports/segments/s02.aiff
say -v "$VOICE" -r 155 "The reading is submitted."                                         -o exports/segments/s03.aiff
say -v "$VOICE" -r 155 "No further assessment."                                            -o exports/segments/s04.aiff
say -v "$VOICE" -r 155 "After submission — the AI result appears."                        -o exports/segments/s05.aiff
say -v "$VOICE" -r 155 "Recall suggested. Focal asymmetry. High confidence."              -o exports/segments/s06.aiff
say -v "$VOICE" -r 155 "A disagreement is detected."                                      -o exports/segments/s07.aiff
say -v "$VOICE" -r 155 "AI-positive, human-negative."                                     -o exports/segments/s08.aiff
say -v "$VOICE" -r 155 "A peer pause is requested — a colleague notified."                -o exports/segments/s09.aiff
say -v "$VOICE" -r 155 "A reason is captured and saved to the decision trace."            -o exports/segments/s10.aiff
say -v "$VOICE" -r 155 "View Comparison: both readings, suspicion score, a reference case." -o exports/segments/s11.aiff
say -v "$VOICE" -r 155 "Prepare Handover packages the case — everything arbitration needs, ready to go." -o exports/segments/s12.aiff
say -v "$VOICE" -r 155 "The case enters the Arbitration Queue."                           -o exports/segments/s13.aiff

echo "Converting segments to wav..."
for i in exports/segments/s*.aiff; do
  ffmpeg -i "$i" "${i%.aiff}.wav" -y -loglevel error
done

echo "Placing segments at exact timestamps..."
# Delays in milliseconds — adjust these values to fine-tune sync
S01=0       # 0:00  "A routine screening case."
S02=2000    # 0:02  "marks a finding — BI-RADS 2"
S03=6000    # 0:06  "reading is submitted"
S04=8500    # 0:08  "no further assessment"  (selected in modal)
S05=11000   # 0:11  "AI result appears"      (orange markers appear)
S06=13500   # 0:13  "Recall suggested..."    (panel slides in)
S07=16000   # 0:16  "disagreement detected"
S08=18000   # 0:18  "AI-positive, human-negative"
S09=28000   # 0:28  "peer pause"
S10=32000   # 0:32  "reason captured"
S11=35000   # 0:35  "view comparison"
S12=40000   # 0:40  "prepare handover"
S13=46000   # 0:46  "arbitration queue"

ffmpeg \
  -i exports/segments/s01.wav \
  -i exports/segments/s02.wav \
  -i exports/segments/s03.wav \
  -i exports/segments/s04.wav \
  -i exports/segments/s05.wav \
  -i exports/segments/s06.wav \
  -i exports/segments/s07.wav \
  -i exports/segments/s08.wav \
  -i exports/segments/s09.wav \
  -i exports/segments/s10.wav \
  -i exports/segments/s11.wav \
  -i exports/segments/s12.wav \
  -i exports/segments/s13.wav \
  -filter_complex "
    [0]adelay=${S01}|${S01}[a0];
    [1]adelay=${S02}|${S02}[a1];
    [2]adelay=${S03}|${S03}[a2];
    [3]adelay=${S04}|${S04}[a3];
    [4]adelay=${S05}|${S05}[a4];
    [5]adelay=${S06}|${S06}[a5];
    [6]adelay=${S07}|${S07}[a6];
    [7]adelay=${S08}|${S08}[a7];
    [8]adelay=${S09}|${S09}[a8];
    [9]adelay=${S10}|${S10}[a9];
    [10]adelay=${S11}|${S11}[a10];
    [11]adelay=${S12}|${S12}[a11];
    [12]adelay=${S13}|${S13}[a12];
    [a0][a1][a2][a3][a4][a5][a6][a7][a8][a9][a10][a11][a12]amix=inputs=13:normalize=0
  " \
  -t 50 \
  exports/narration_v5.mp3 -y -loglevel error

echo ""
echo "✓ exports/narration_v5.mp3 done"
echo ""
echo "To adjust timing: edit the S01–S13 delay values (in milliseconds) in this script."
echo "Then re-run — only the mix step re-runs, segments are already generated."
echo ""
echo "Next: bash scripts/make_final_video_v5.sh"
