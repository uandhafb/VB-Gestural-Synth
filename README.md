# Gestural 🖐️🙂🎛️ (VB-Gestural-Synth)

Play a synth with your **hands and face** using your webcam, and shape real sounds from **[Freesound](https://freesound.org)**.

## What it does
- Tracks both hands and your face in the browser (with MediaPipe).
- Has **3 hand modes** (switch with keys `1` `2` `3`, the buttons, or by holding ✌️ for 1 second):
  1. **Theremin**: right hand height = pitch (on a musical scale), left hand height = volume, right pinch = vibrato.
  2. **Sculptor**: right hand moves through a recording like a scrubber, pinch = grain size (smooth ↔ glitchy), right hand height = pitch, left hand height = volume.
  3. **Texture Mixer**: each hand holds a sound (A and B). Height = volume and brightness, hands apart = wide stereo, hands together = melt into a cloud, fist = freeze.
- **Face effects, always on:** open mouth = brighter filter, raise eyebrows = more reverb, tilt head = pitch bend, turn head = left/right pan, smile = switch major/minor (Theremin).
- **Freesound search:** type a word (e.g. "rain"), then load a result into slot A or B.

## How to run it
1. Open a terminal in this folder.
2. (First time only) Create the Python virtual environment:
   ```bash
   python3 -m venv .venv
   ```
3. Activate it (macOS/Linux):
   ```bash
   source .venv/bin/activate
   ```
4. Start the server:
   ```bash
   python3 server.py
   ```
5. Open **http://localhost:8000** in Chrome. Click **Start**, then allow the camera.
6. Stop the server with `Ctrl + C`.

The app works without a Freesound key; it uses a built-in sound. To turn on Freesound search, see below.

## Setting up Freesound search (free)
1. Make an account at https://freesound.org.
2. Go to https://freesound.org/apiv2/apply and create an API key. Any name and description will do, e.g. "Gestural class project".
3. Copy `.env.example` to a new file called `.env`, and paste your key there:
   ```
   FREESOUND_API_KEY=abc123yourkey
   ```
4. Restart `server.py`.

`.env` is ignored by Git, so your key is never committed.

## Important files
| File | What it is |
|---|---|
| `index.html` | The whole app: page, style, tracking, and sound engine |
| `server.py` | Small local server: serves the page and talks to Freesound, keeping your key secret |
| `.env.example` | Template for your secret key file |
| `docs/` | How it's built, decisions, development history |
| `TASKS.md` | What's being worked on |

## Troubleshooting
- Open the browser console (`Cmd + Option + J` in Chrome) to see log messages.
- The terminal running `server.py` shows server logs (searches, errors).
- No camera? Make sure you opened `http://localhost:8000`, not the file directly.

## Source code
GitHub: https://github.com/uandhafb/VB-Gestural-Synth
The local project folder is the main copy. GitHub is a backup and a way to share it.

## License and credits
- **Code:** [MIT License](LICENSE) © 2026 uandhafb. You may use, copy and change it, but keep the copyright notice.
- **Hand/face tracking:** [MediaPipe](https://github.com/google-ai-edge/mediapipe) by Google (Apache 2.0). It's loaded from a CDN and not included in this repo.
- **Sounds:** no Freesound audio is stored in this repo. Sounds are streamed from [Freesound](https://freesound.org), and **each sound has its own license** (CC0, CC BY, CC BY-NC…). The app shows the name, author and license of every loaded sound. If you record or publish a performance, credit the authors of CC BY sounds, and don't use CC BY-NC sounds commercially.
- Built for a class, following `START_PROJECT.md`.
