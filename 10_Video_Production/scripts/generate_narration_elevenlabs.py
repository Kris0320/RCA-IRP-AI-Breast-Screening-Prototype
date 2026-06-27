#!/usr/bin/env python3
# Narration — ElevenLabs / Alice voice, per-sentence placement
# Run from: 10_Video_Production/
# Output:   exports/narration_elevenlabs.mp3
#
# Segments are cached: re-run only re-mixes unless you delete exports/segments_el/

import urllib.request
import json
import os
import subprocess

API_KEY  = os.environ.get("ELEVENLABS_API_KEY", "")
VOICE_ID = "Xb7hH8MSUJpSbSDYk0k2"  # Alice — Clear, Engaging Educator
MODEL    = "eleven_turbo_v2_5"

os.makedirs("exports/segments_el", exist_ok=True)

# ── Text segments ──────────────────────────────────────────────────────────────
SEGMENTS = [
    ("s01", "A routine screening case."),
    ("s02", "The radiologist marks a finding. BI-RADS 2."),
    ("s03", "The reading is submitted."),
    ("s04", "No further assessment."),
    ("s05", "After submission, the AI result appears."),
    ("s06", "Recall suggested. Focal asymmetry. High confidence."),
    ("s07", "A disagreement is detected."),
    ("s08", "AI-positive, human-negative."),
    ("s09", "A peer pause is requested. A colleague notified."),
    ("s10", "A reason is captured and saved to the decision trace."),
    ("s11", "View Comparison: both readings, suspicion score, a reference case."),
    ("s12", "Prepare Handover packages the case. Everything arbitration needs, ready to go."),
    ("s13", "The case enters the Arbitration Queue."),
]

# ── Cue timestamps (milliseconds into the 50s video) ──────────────────────────
DELAYS = {
    "s01":     0,   # ends ~1900ms
    "s02":  2000,   # ends ~5990ms
    "s03":  6000,   # ends ~7720ms
    "s04":  8500,   # ends ~10080ms
    "s05": 11000,   # ends ~14020ms
    "s06": 14200,   # ends ~18380ms  (was 13500 → overlapped s05)
    "s07": 18500,   # ends ~20640ms  (was 16000 → overlapped s06)
    "s08": 20800,   # ends ~23260ms  (was 18000 → overlapped s07)
    "s09": 28000,   # ends ~31580ms
    "s10": 32000,   # ends ~35810ms
    "s11": 36000,   # ends ~40830ms  (was 35000 → overlapped s10)
    "s12": 41000,   # ends ~46150ms  (was 40000 → overlapped s11)
    "s13": 46200,   # ends ~48710ms
}

# ── TTS call ───────────────────────────────────────────────────────────────────
def tts(text, out_path):
    url = f"https://api.elevenlabs.io/v1/text-to-speech/{VOICE_ID}"
    payload = json.dumps({
        "text": text,
        "model_id": MODEL,
        "voice_settings": {"stability": 0.5, "similarity_boost": 0.75},
    }).encode("utf-8")
    req = urllib.request.Request(url, data=payload, headers={
        "xi-api-key": API_KEY,
        "Content-Type": "application/json",
        "Accept": "audio/mpeg",
    })
    with urllib.request.urlopen(req) as resp:
        data = resp.read()
    with open(out_path, "wb") as f:
        f.write(data)

# ── Generate segments (cached) ─────────────────────────────────────────────────
print("Generating segments via ElevenLabs (Alice)...")
for name, text in SEGMENTS:
    mp3 = f"exports/segments_el/{name}.mp3"
    wav = f"exports/segments_el/{name}.wav"
    if os.path.exists(mp3):
        print(f"  {name}: cached")
    else:
        print(f"  {name}: {text[:50]}")
        tts(text, mp3)
    subprocess.run(["ffmpeg", "-i", mp3, wav, "-y", "-loglevel", "error"], check=True)

# ── Mix at exact timestamps ────────────────────────────────────────────────────
print("Mixing at exact timestamps...")

inputs, filter_parts, labels = [], [], []
for i, (name, _) in enumerate(SEGMENTS):
    inputs += ["-i", f"exports/segments_el/{name}.wav"]
    d = DELAYS[name]
    filter_parts.append(f"[{i}]adelay={d}|{d}[a{i}]")
    labels.append(f"[a{i}]")

n = len(SEGMENTS)
filter_complex = ";\n    ".join(filter_parts) + ";\n    " + "".join(labels) + f"amix=inputs={n}:normalize=0"

subprocess.run(
    ["ffmpeg"] + inputs + [
        "-filter_complex", filter_complex,
        "-t", "50",
        "exports/narration_elevenlabs.mp3",
        "-y", "-loglevel", "error",
    ],
    check=True,
)

print("\n✓ exports/narration_elevenlabs.mp3 done")
print("Next: bash scripts/make_final_video_elevenlabs.sh")
