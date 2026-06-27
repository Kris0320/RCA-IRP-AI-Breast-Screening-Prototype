#!/bin/bash
# Run from: 10_Video_Production/
# Requires: exports/narration_v5.mp3

INPUT="raw_recordings/prototype-recording- part1-v1.mp4"
OUTPUT="exports/reading-viewer_final_50s_v5.mp4"

echo "Step 1: Speeding up video to 50s (1.33×)..."
ffmpeg -i "$INPUT" \
  -vf "setpts=0.75*PTS" \
  -an \
  exports/_video_50s_noaudio.mp4 -y -loglevel error

echo "Step 2: Merging with narration..."
ffmpeg \
  -i exports/_video_50s_noaudio.mp4 \
  -i exports/narration_v5.mp3 \
  -c:v copy -c:a aac \
  -shortest \
  "$OUTPUT" -y -loglevel error

echo "✓ $OUTPUT"
