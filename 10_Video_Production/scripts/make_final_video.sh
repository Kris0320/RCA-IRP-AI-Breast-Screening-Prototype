#!/bin/bash
# Run this from: 10_Video_Production/
# Requires: exports/narration.mp3 (run generate_narration.sh first)

INPUT="raw_recordings/prototype-recording- part1-v1.mp4"
OUTPUT="exports/reading-viewer_final_50s.mp4"

# Step 1: Speed up video to 50s (1.33×), drop audio
ffmpeg -i "$INPUT" \
  -vf "setpts=0.75*PTS" \
  -an \
  exports/reading-viewer_video_50s_noaudio.mp4 -y

# Step 2: Merge sped-up video + narration audio
ffmpeg \
  -i exports/reading-viewer_video_50s_noaudio.mp4 \
  -i exports/narration.mp3 \
  -c:v copy -c:a aac \
  -shortest \
  "$OUTPUT" -y

echo "✓ $OUTPUT ready"
