# PROJECT.md — Gestural

## Main idea
A synth you play with your **body**. The webcam tracks your **hands and face**, and those movements shape sounds: a theremin-style synth, and real recordings found on **Freesound**.

## Audience
The student (the creator) and anyone who wants to try it: classmates, or an audience at a performance or demo.

## How it plays
The hands have **3 modes**. The **face** always controls the effects.

| Mode | Hands |
|---|---|
| 1. Theremin | Right hand height sets pitch (snapped to a scale). Left hand height sets volume. Right pinch adds vibrato. |
| 2. Sculptor | Right hand X moves through a sound. Right hand Y sets pitch. Pinch sets grain size. Left hand Y sets volume. |
| 3. Texture Mixer | Each hand holds a sound (A/B). Height sets volume and brightness. Hands apart = wide stereo. Hands together = the sounds melt into one reverby cloud. A fist freezes the sound. |

**Face, in every mode:** mouth open → filter brightness, eyebrows up → reverb, head tilt → pitch bend, head turn → left/right pan, smile → major/minor scale.

**Switching modes:** keys 1/2/3, on-screen buttons, or hold ✌️ for 1 second.

## Constraints
- Runs in the browser (Chrome is recommended) at `http://localhost:8000`.
- The Freesound API key must stay secret. `server.py` holds it, never the browser.
- The app must still work without a key, using a built-in fallback sound.
- Sounds from Freesound must show their name, author and license (attribution).

## First useful version
You can open the page, allow the camera, see your hands and face tracked, and play all 3 modes with face effects. You can also search Freesound and load sounds into slots A/B.
