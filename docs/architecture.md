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
2. **Tracking:** loads MediaPipe `HandLandmarker` (2 hands) and `FaceLandmarker` (with blendshapes and a head matrix) from cdn.jsdelivr.net. The model files come from storage.googleapis.com. Each video frame gives:
   - hands: 21 points each, plus which hand is Left or Right;
   - face: blendshape scores (`jawOpen`, `browInnerUp`, `mouthSmileLeft/Right`) and a 4×4 matrix, which gives head roll (tilt) and yaw (turn).
3. **Controls:** turns raw points into 0..1 values (hand height, pinch, fist, ✌️) and smooths them so the sound doesn't jump.
4. **Audio engine (Web Audio API):**
   ```
   theremin osc ─┐
   grain voice A ─┼─► filter (mouth) ─► panner (head turn) ─► dry ───────────► master ─► out
   grain voice B ─┘                                        └► reverb (brows) ─┘
   ```
   - **Theremin:** two slightly detuned oscillators.
   - **Grain voice:** a granular player. About every 30 ms it plays a tiny snippet ("grain") of the sound buffer, with a fade in and out. Position, grain size, pitch, and a "freeze" flag are controlled by the hands.
   - **Reverb:** a ConvolverNode with a generated noise-decay impulse (no files needed).
5. **Modes:** `theremin`, `sculptor` and `mixer` decide which controls go to which sound parameters.
6. **Freesound UI:** a search box → `GET /api/search?q=...` → results list → load into slot A/B via `GET /api/audio?url=...` → `decodeAudioData`. Attribution is shown.
7. **Drawing:** the video is mirrored with points drawn over it, plus meters.

The first sound is a **built-in fallback** generated in JS (a chord-like pad), so the app works with no key.

### `server.py` (Python standard library)
- Serves the files in this folder on `http://localhost:8000`.
- `/api/search?q=word`: reads `FREESOUND_API_KEY` from `.env`, calls `https://freesound.org/apiv2/search/text/`, and returns simplified JSON (id, name, username, license, duration, preview URL).
- `/api/audio?url=...`: downloads a preview mp3 **only** from `freesound.org` domains and passes it to the browser (this avoids CORS).
- Logs requests and errors to the terminal. Never logs the key.

## External services
- **cdn.jsdelivr.net / storage.googleapis.com:** the MediaPipe library and models (needs internet).
- **freesound.org:** the sound search API (needs a free API key).
