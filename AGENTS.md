# AGENTS.md — how to work on this project

You are helping a **student** build **Gestural**, a webcam gesture synth. Read this first.

## Before changing anything
1. Read `README.md`, `PROJECT.md`, `TASKS.md`, and everything in `docs/`.
2. Run `git status` and `git diff` to see the current state.
3. `START_PROJECT.md` holds the original class rules. Follow them. It's the professor's file: it stays **local only** (git-ignored) and must not be committed.

## How to work
- Keep it **simple**. The app is browser-first: one `index.html` (HTML + CSS + JS together) plus a small `server.py`.
- Don't add frameworks, build tools, or libraries unless they solve a real problem. Discuss the change with the student first.
- Explain unfamiliar technical ideas in plain language.
- Preserve working code. Make small, understandable changes.
- Ask before large rewrites, destructive operations, or major architecture changes.
- Never silently remove working features.
- Keep useful logging (`console.log/warn/error` in the browser, and `print`-style logs in `server.py`). Don't log on every frame.

## Keep the project memory up to date
- `TASKS.md`: keep Now / Next / Done / Questions current.
- `docs/decisions.md`: record important design decisions.
- `docs/development-log.md`: record meaningful changes, with the date.
- `docs/architecture.md`: update it when how the pieces fit together changes.
- `README.md`: update it when how to run the project, or what it does, changes.

## Git
- Make small commits with clear messages (e.g. "Add texture mixer mode").
- The remote is `origin` → https://github.com/uandhafb/VB-Gestural-Synth (branch `main`).
- **Never** push to GitHub or any remote without the student's permission.
- Don't change global Git settings.

## Secrets
- The Freesound API key lives only in `.env` (git-ignored). `.env.example` shows the variable name.
- Never put real keys in code, docs, or logs. The browser must never see the key; `server.py` adds it.
- Never delete important files or data without the student's permission.
