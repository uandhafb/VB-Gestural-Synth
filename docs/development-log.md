# Development log

## 2026-09-24: Project setup
- **What:** Initialized Git and created the docs (`AGENTS.md`, `README.md`, `PROJECT.md`, `TASKS.md`, `docs/`), `.gitignore`, `.env.example`, and `requirements.txt`.
- **Why:** These follow the class rules in `START_PROJECT.md`, so the project has a memory from the start.
- **Next agent:** The concept is 3 hand modes plus face effects. See `PROJECT.md` and `docs/decisions.md`.

## 2026-09-24: First full version
- **What:** Added `server.py` (Python stdlib: static files, `/api/search`, `/api/audio`) and `index.html` (MediaPipe hand + face tracking, 3 modes, face effects, granular engine, Freesound UI).
- **Why:** This is the first playable version of the whole concept.
- **Tested:** Python/JS syntax checks. The server serves the page; search without a key returns a friendly `no_key` message; non-Freesound audio URLs are blocked; `/.env` is not served; HTTPS to freesound.org works (SSL is OK).
- **Not yet tested:** the live camera + sound feel (needs the student at the webcam), and real Freesound search (needs an API key).
- **Next agent:** gesture thresholds live in `analyzeHand()` / `analyzeFace()`; sound mappings live in `updateAudio()`.

## 2026-09-24: Connected to GitHub
- **What:** Added the remote `origin` → github.com/uandhafb/VB-Gestural-Synth. Merged GitHub's initial commit (LICENSE, README) and kept the local README. Added license/credits to the README and editor/log files to `.gitignore`.
- **Why:** The student wants the project backed up and shared on GitHub.
- **Next agent:** Push only when the student asks. `.env` (the Freesound key) is git-ignored. Keep it that way.
