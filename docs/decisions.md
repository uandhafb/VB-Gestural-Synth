# Decisions

## 2026-09-24: Browser-first with MediaPipe for tracking
- **Decision:** Track the hands and face in the browser with Google's MediaPipe Tasks Vision (`HandLandmarker` + `FaceLandmarker`), loaded from cdn.jsdelivr.net. Make the sound with the Web Audio API.
- **Why:** It's free, fast, runs locally in the browser, and needs no install. It follows the class's browser-first rule.
- **Alternatives:** Python + OpenCV + a native synth. That's more setup and harder to share.
- **Revisit if:** tracking is too slow on the student's computer, or offline use is required (then download the model files into `assets/`).

## 2026-09-24: Small Python server (`server.py`, standard library only)
- **Decision:** A tiny server in the repo serves the page and acts as a middleman for Freesound.
- **Why:** (1) The browser only allows webcam access on `http://localhost` (or https), not on `file://`. (2) The Freesound API key must stay secret. If it were in `index.html`, anyone could read it. (3) Fetching audio through our own server avoids CORS errors (CORS is the browser's rule that blocks loading from other websites).
- **Alternatives:** Put the key in the browser (insecure), or build a Node.js server (would add another tool).
- **Revisit if:** the project is deployed publicly (then the proxy must be hosted somewhere).

## 2026-09-24: Three hand modes plus always-on face effects
- **Decision:** Don't map every idea at once. The hands switch between Theremin, Sculptor and Texture Mixer. The face always controls the effects.
- **Why:** The student wanted every feature. Modes keep each one playable and understandable.
- **Revisit if:** the student wants a "performance" mode that combines them.

## 2026-09-24: Granular engine written by hand
- **Decision:** Write the granular synthesis ourselves: many tiny overlapping snippets ("grains") of the sound, each with a fade in and out.
- **Why:** It's about 60 lines of Web Audio, needs no library, and is a good learning example.

## 2026-09-24: Publish on GitHub under the MIT License
- **Decision:** Connect the local repo to https://github.com/uandhafb/VB-Gestural-Synth (remote `origin`, branch `main`), and keep the MIT License that the GitHub repo was created with.
- **Why:** MIT is simple and permissive, which suits a class project. It's compatible with MediaPipe (Apache 2.0, loaded from a CDN). Freesound audio is not in the repo, and each sound keeps its own license, which the app shows.
- **Alternatives:** GPL (forces derived work to stay open; more restrictive) or no license (legally "all rights reserved").
- **Revisit if:** the project starts bundling audio files or third-party code in the repo. Then check those licenses.
