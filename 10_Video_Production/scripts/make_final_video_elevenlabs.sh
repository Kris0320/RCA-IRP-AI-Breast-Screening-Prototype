#!/bin/bash
# Run from: 10_Video_Production/
# Output:   exports/reading-viewer_final_elevenlabs.mp4

set -e
mkdir -p exports

echo "Step 1: Speeding up video to 50s (1.33×)..."
ffmpeg -i raw_recordings/prototype-recording-\ part1-v1.mp4 \
  -filter:v "setpts=0.75*PTS" \
  -an \
  exports/reading-viewer_video_50s_noaudio.mp4 \
  -y -loglevel error

echo "Step 2: Merging with ElevenLabs narration..."
ffmpeg \
  -i exports/reading-viewer_video_50s_noaudio.mp4 \
  -i exports/narration_elevenlabs.mp3 \
  -c:v copy -c:a aac -shortest \
  exports/reading-viewer_final_elevenlabs.mp4 \
  -y -loglevel error

echo "✓ exports/reading-viewer_final_elevenlabs.mp4"
