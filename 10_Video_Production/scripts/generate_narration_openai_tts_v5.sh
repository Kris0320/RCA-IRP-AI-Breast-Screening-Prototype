#!/bin/bash
# Narration v5 using OpenAI Text-to-Speech
# Run from: 10_Video_Production/
# Output: exports/narration_openai_tts_v5.mp3
#
# Requirements:
#   export OPENAI_API_KEY="sk-..."
#   ffmpeg
#
# Optional overrides:
#   MODEL="gpt-4o-mini-tts" VOICE="marin" bash scripts/generate_narration_openai_tts_v5.sh
#
# Notes:
# - This script keeps the same exact cue timing as generate_narration_v5.sh.
# - OpenAI policy requires clear disclosure that the TTS voice is AI-generated
#   when presented to end users.

set -euo pipefail

if [[ -z "${OPENAI_API_KEY:-}" ]]; then
  echo "Missing OPENAI_API_KEY."
  echo ""
  echo "Set it first, then rerun:"
  echo "  export OPENAI_API_KEY=\"sk-...\""
  echo "  bash scripts/generate_narration_openai_tts_v5.sh"
  exit 1
fi

MODEL="${MODEL:-gpt-4o-mini-tts}"
VOICE="${VOICE:-marin}"
OUT="exports"
SEG="$OUT/openai_tts_segments"

mkdir -p "$SEG"

INSTRUCTIONS="Speak as a calm, professional documentary narrator for a design prototype demo. Natural, warm, precise, and not dramatic. Keep a measured pace, with clear clinical terms and slight pauses between ideas."

texts=(
  "A routine screening case."
  "The radiologist marks a finding, BI-RADS 2."
  "The reading is submitted."
  "No further assessment."
  "After submission, the AI result appears."
  "Recall suggested. Focal asymmetry. High confidence."
  "A disagreement is detected."
  "AI-positive, human-negative."
  "A peer pause is requested. A colleague is notified."
  "A reason is captured and saved to the decision trace."
  "View Comparison shows both readings, suspicion score, and a reference case."
  "Prepare Handover packages the case. Everything arbitration needs, ready to go."
  "The case enters the Arbitration Queue."
)

delays=(
  0
  2000
  6000
  8500
  11000
  13500
  16000
  18000
  28000
  32000
  35000
  40000
  46000
)

echo "Generating OpenAI TTS segments..."
echo "Model: $MODEL"
echo "Voice: $VOICE"
echo ""

for idx in "${!texts[@]}"; do
  num=$(printf "%02d" "$((idx + 1))")
  text="${texts[$idx]}"
  wav="$SEG/s${num}.wav"

  if [[ -f "$wav" ]]; then
    echo "s${num}.wav exists, skipping"
    continue
  fi

  echo "Generating s${num}.wav: $text"

  json_payload=$(python3 -c '
import json, os, sys
model, voice, instructions, text = sys.argv[1:5]
print(json.dumps({
    "model": model,
    "voice": voice,
    "input": text,
    "instructions": instructions,
    "response_format": "wav"
}))
' "$MODEL" "$VOICE" "$INSTRUCTIONS" "$text")

  curl -sS https://api.openai.com/v1/audio/speech \
    -H "Authorization: Bearer $OPENAI_API_KEY" \
    -H "Content-Type: application/json" \
    -d "$json_payload" \
    --output "$wav"

  if ! file "$wav" | grep -qi "WAVE audio"; then
    echo "OpenAI TTS did not return valid WAV for segment s${num}."
    echo "Response saved at: $wav"
    exit 1
  fi
done

echo ""
echo "Placing segments at exact timestamps..."

inputs=()
filters=()
mix_inputs=""

for idx in "${!texts[@]}"; do
  num=$(printf "%02d" "$((idx + 1))")
  delay="${delays[$idx]}"
  inputs+=(-i "$SEG/s${num}.wav")
  filters+=("[$idx:a]adelay=${delay}|${delay}[a$idx]")
  mix_inputs="${mix_inputs}[a$idx]"
done

filter_complex="$(IFS=';'; echo "${filters[*]}");${mix_inputs}amix=inputs=${#texts[@]}:normalize=0"

ffmpeg \
  "${inputs[@]}" \
  -filter_complex "$filter_complex" \
  -t 50 \
  "$OUT/narration_openai_tts_v5.mp3" \
  -y -loglevel error

echo ""
echo "Done: $OUT/narration_openai_tts_v5.mp3"
echo ""
echo "Next:"
echo "  ffmpeg -i exports/reading-viewer_video_50s_noaudio.mp4 -i exports/narration_openai_tts_v5.mp3 -c:v copy -c:a aac -shortest exports/reading-viewer_final_50s_openai_tts.mp4 -y"
