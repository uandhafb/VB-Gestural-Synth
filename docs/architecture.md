# Architecture

## The big picture
```
Webcam ──► MediaPipe (in browser) ──► hand + face numbers ──► "controls" ──► Web Audio synth ──► speakers
                                                                                ▲
Freesound.org ◄── server.py (adds secret key) ◄── search box in index.html ─────┘ (loads sounds)
```

## Parts
### `index.html` (everything the browser runs)
Sections, in order inside the `<script type="module">`:
1. **Logging helper:** `log()` prints tagged messages to the console.
2. **Tracking:** loads MediaPipe `HandLandmarker` (2 hands) and `FaceLandmarker` (with blendshapes) from cdn.jsdelivr.net. The model files come from storage.googleapis.com. Each video frame gives:
   - hands: 21 points each, plus which hand is Left or Right;
   - face: 478 points plus blendshape scores (`jawOpen`, `browInnerUp`, `mouthSmileLeft/Right`). Head **tilt** is the angle between the outer eye corners (points 33 and 263). Head **turn** is where the nose tip (1) sits between the cheeks (234 and 454).
   - Left/right hand is decided by **screen position** (mirrored), not by the model's label, which is easy to get backwards.
3. **Controls:** turns raw points into 0..1 values (hand height, pinch, fist, ✌️) and smooths them so the sound doesn't jump.
4. **Audio engine (Web Audio API):**
   ```
   theremin osc ─┐
   grain voice A ─┼─► filter (mouth) ─► panner (head turn) ─► dry ───────────► master ─► out
   grain voice B ─┘                                        └► reverb (brows) ─┘
   ```
   - **Theremin:** two slightly detuned oscillators, plus a vibrato LFO controlled by right-hand pinch.
   - **Grain voice:** a granular player. A scheduler runs every 25 ms and queues tiny snippets ("grains") of the sound 100 ms ahead. Each grain has a smooth fade in and out, and about 4 grains overlap at a time. Position, grain size, pitch, and a "freeze" flag are controlled by the hands.
   - **Reverb:** a ConvolverNode with a generated noise-decay impulse (no files needed).
5. **Modes:** `theremin`, `sculptor` and `mixer` decide which controls go to which sound parameters.
6. **Freesound UI:** a search box → `GET /api/search?q=...` → results list → load into slot A/B via `GET /api/audio?url=...` → `decodeAudioData`. Attribution is shown.
7. **Drawing:** the video is mirrored with points drawn over it, plus meters.

The first sound is a **built-in fallback** generated in JS (slot A: a chord pad, slot B: random bells), so the app works with no key.

### `server.py` (Python standard library)
- Serves the files in this folder on `http://localhost:8000`.
- `/api/search?q=word`: reads `FREESOUND_API_KEY` from `.env`, calls `https://freesound.org/apiv2/search/text/`, and returns simplified JSON (id, name, username, license, duration, preview URL).
- `/api/audio?url=...`: downloads a preview mp3 **only** from `freesound.org` domains and passes it to the browser (this avoids CORS).
- Logs requests and errors to the terminal. Never logs the key.

## External services
- **cdn.jsdelivr.net / storage.googleapis.com:** the MediaPipe library and models (needs internet).
- **freesound.org:** the sound search API (needs a free API key).
