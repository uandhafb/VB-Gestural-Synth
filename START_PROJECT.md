# START_PROJECT.md
## A beginner-friendly project setup prompt for coding agents

This file is the starting point for this project.

If you are an AI coding agent, follow these instructions before doing substantial coding.

If you are a student, you do **not** need to understand every technical detail yet. The agent should explain important steps in plain language as they happen.

---

# 1. Begin with the student's idea

Before building anything, ask the student what they want to make.

Help them describe the idea in simple language:

- What is the project?
- What should it do?
- Who is it for?
- What would count as a good first working version?

Do not force the student to make every technical decision in advance.

Once the idea is reasonably clear, record it in `README.md` and `PROJECT.md`.

---

# 2. Keep the project folder tidy

The local project folder is the **source of truth**.

That means:

- All important code must exist inside this project folder.
- Documentation must live inside this project folder.
- If a local server (in Python, Node.js, PHP, or any other language) is required to run, test, or develop the project, build it inside the project repository folder as an explicit part of the repository (e.g., `server.py`). Do not create or rely on servers external to the repo, and do not use untracked ad-hoc server commands; everything required to run the project must be contained within the repo folder and documented in `README.md`.
- If the project is deployed to the web, the hosted version is a copy of the project, not the only copy.
- Do not create files in random locations on the student's computer.
- Organize files into sensible folders when folders are genuinely useful.
- Do not create a complicated folder structure before the project needs one.

Prefer the simplest structure that makes the project easy to understand.

---

# 3. Create the basic project files

At the beginning of the project, create:

```text
AGENTS.md
README.md
PROJECT.md
TASKS.md
docs/
    architecture.md
    development-log.md
    decisions.md
```

Create additional files or folders only when the project needs them.

If the project is deployed, also create:

```text
docs/deployment.md
```

---

# 4. What each file is for

## `AGENTS.md`

This is the standing instruction file for future coding agents.

It should tell agents how to work on this project, including:

- keep the code and folders organized;
- prefer simple solutions;
- explain unfamiliar technical ideas in plain language;
- read the existing project documentation before making changes;
- inspect the current Git status and Git diff before changing existing work;
- preserve working code unless there is a clear reason to change it;
- ask before large rewrites, destructive operations, or major architectural changes;
- never silently remove important working functionality;
- keep documentation up to date as the project develops;
- keep `TASKS.md` current;
- record important decisions in `docs/decisions.md`;
- record meaningful development history in `docs/development-log.md`;
- make small, understandable changes;
- use clear Git commit messages;
- never push code to a remote service without the student's permission;
- never delete important files or data without the student's permission;
- never expose passwords, API keys, tokens, or other secrets.

`AGENTS.md` should be written so that another agent can enter the project later and quickly understand how to behave.

---

## `README.md`

This is the friendly front door to the project.

Keep it understandable to someone who did not write the code.

It should eventually explain:

- what the project is;
- what it currently does;
- how to run it;
- the important files and folders;
- any setup steps;
- where it is deployed, if applicable.

Update it when those facts change.

---

## `PROJECT.md`

This explains the project itself.

Keep a short description of:

- the main idea;
- the current goal;
- the intended user or audience;
- the important features;
- any important constraints;
- what the first useful version should accomplish.

Do not turn this into a huge specification unless the project truly needs one.

---

## `TASKS.md`

This is the student's quick project dashboard.

Use these headings:

```markdown
# Now

# Next

# Done

# Questions
```

Keep it short and current.

A student should be able to open `TASKS.md` and immediately understand:

- what is being worked on now;
- what is likely to happen next;
- what has already been completed;
- what still needs a decision.

Move items as the project develops.

---

## `docs/architecture.md`

Explain how the project is put together.

Use plain language first.

Include technical detail only where it helps.

For example:

- what the main parts are;
- how they connect;
- where data comes from;
- which file starts the program;
- which external services are used.

Keep this accurate as the project changes.

---

## `docs/development-log.md`

Keep a concise history of meaningful development.

Each entry should include:

- date;
- what changed;
- why it changed;
- anything the next agent should know.

Do not record every tiny edit. Record changes that help preserve project memory between coding sessions.

---

## `docs/decisions.md`

Record important design decisions.

For each meaningful decision, briefly note:

- the decision;
- why it was made;
- any important alternative that was considered;
- anything that may cause the decision to be revisited later.

This file exists so future agents do not unknowingly repeat old debates or undo intentional choices.

---

## `docs/deployment.md`

Create this when the project is first deployed.

Record:

- where the project is deployed;
- the live URL;
- how deployment works;
- how to update the live version;
- any account or service involved.

Never place passwords, private API keys, or access tokens in this file.

---

# 5. Set up Git locally

Initialize Git in the project folder:

```bash
git init
```

Before running commands, briefly explain what they do when the student is likely to be unfamiliar with them.

For example:

> `git init` turns this folder into a Git project so we can keep a history of changes.

Git should be used as a safety net and a learning tool, not as mysterious background machinery.

---

# 6. Check the Git author before the first commit

Git commits contain an author name and email address.

Before the first commit, check whether Git already has them configured.

Useful commands include:

```bash
git config user.name
git config user.email
```

If they are missing, explain the situation in plain language.

Offer to configure them **for this project only**:

```bash
git config user.name "Student Name"
git config user.email "student@example.com"
```

Do not change global Git settings unless the student specifically asks.

Explain that:

- the Git name and email identify the author of a commit;
- this is separate from signing in to GitHub;
- the email does not itself give Git permission to push anywhere;
- if the student later uses GitHub, using an email associated with their GitHub account can help GitHub connect commits to their account;
- students may also choose a privacy-preserving email if appropriate.

---

# 7. Make Git history useful

Before changing existing code, inspect the project state.

Useful commands include:

```bash
git status
git diff
```

Explain them simply when needed:

- `git status` shows which files have changed.
- `git diff` shows the actual differences inside changed files.

Make small, meaningful commits.

A commit should represent an understandable step.

Use clear messages such as:

```text
Create first working webpage
Add score display
Fix mobile layout
Document deployment process
```

Avoid vague messages such as:

```text
stuff
changes
update
fix
```

Before a major change, make sure the current working state is safely committed when appropriate.

Do not commit broken experiments over a known working version without a clear reason.

---

# 8. GitHub is optional and separate from Git

Local Git comes first.

Do not assume the student wants GitHub.

If the student later wants to use GitHub, explain that GitHub requires an additional setup step.

In plain language:

- Git keeps project history locally.
- GitHub can store a remote copy of the Git repository online.
- Git author information is not the same thing as GitHub authentication.
- Pushing to GitHub requires signing in or otherwise authenticating.
- A GitHub repository must be connected as a remote before pushing.

Explain each step as it happens.

Never create, connect, or push to a remote repository without the student's permission.

---

# 9. Create a `.gitignore`

Create a `.gitignore` appropriate for the project.

At minimum, protect files that should normally remain local, including things such as:

```text
.env
.venv/
venv/
node_modules/
tmp/
.DS_Store
```

Add other generated, temporary, cache, build, or secret files when appropriate.

Do not blindly ignore files that the project actually needs.

---

# 10. Protect secrets

If the project needs API keys, passwords, tokens, or other private values:

- keep real secrets in `.env`;
- make sure `.env` is ignored by Git;
- never place real secrets directly in committed source code;
- never place real secrets in documentation;
- create `.env.example` with placeholder names so another person knows what variables are required.

Example:

```env
OPENAI_API_KEY=your_key_here
DATABASE_URL=your_database_url_here
```

The example file may be committed.

The real `.env` file should remain local.

---

# 11. Python projects: always use a virtual environment

If the project uses Python, create a project-local virtual environment.

Prefer:

```text
.venv/
```

Create it with something like:

```bash
python -m venv .venv
```

Activate it using the appropriate command for the student's operating system.

Install project libraries inside that environment, not globally on the student's computer.

The first time this happens, explain briefly:

> A virtual environment gives this project its own private set of Python libraries. It helps one project avoid interfering with another.

Add `.venv/` to `.gitignore`.

Keep the project's dependency list up to date, using an appropriate standard file such as:

```text
requirements.txt
```

or another dependency file if the project has a clear reason to use one.

Do not ask a beginner to manually solve an environment problem that the agent can safely diagnose and fix. Explain what happened after fixing it.

---


# 12. Use the browser as the default coding environment

For this class, the **browser is the default place to build and run projects** unless the project has a clear reason to use something else.

Prefer:

- HTML;
- JavaScript;
- CSS;
- browser APIs;
- the Web Audio API for browser-based sound and music projects.

For a simple project, begin with the browser before introducing another language, runtime, framework, or application.

This keeps projects easier to open, understand, share, and troubleshoot.

Use another environment when the project genuinely needs capabilities that the browser does not provide well.

Examples include:

- access to local files that is blocked or awkward because of browser security or CORS restrictions;
- server-side processing;
- a backend that must protect secret credentials;
- a hosting environment that specifically requires PHP;
- database or server functionality that cannot reasonably live in the browser;
- operating-system or hardware access that requires a native application;
- advanced audio work that is better suited to specialized environments and tools such as SuperCollider, Max, Pure Data, Faust, HISE, JUCE, or iPlug2, or to native plug-in development using formats and SDKs such as VST3, Audio Unit, CLAP, or LV2;
- performance or technical requirements that clearly exceed what the browser can reasonably provide.

Before moving away from the browser-first approach:

1. explain the limitation in plain language;
2. explain what the proposed new environment solves;
3. discuss the change with the student;
4. add the new technology only after the student understands why it is being introduced;
5. document the decision in `docs/decisions.md`;
6. update `docs/architecture.md` so future agents understand how the pieces fit together.

Do not introduce Python, Node.js, PHP, a native audio environment, a framework, or another technology merely because it is familiar to the agent.

Use the simplest environment that can do the work well.

### When a local server is needed to serve browser files
Even when a project is browser-first, browsers often require an `http://localhost` origin to grant permissions for security-sensitive APIs (such as webcam video, microphone input, or audio context) or to prevent CORS errors with local assets. When a local server is needed:
- write the server script directly inside the project repository (e.g. `server.py`);
- keep it simple, favoring standard-library solutions (such as Python's built-in `http.server`);
- ensure the server script is committed to Git as an explicit part of the repository;
- document how to start the server in `README.md`;
- never run external servers outside the project or rely on undocumented ad-hoc terminal one-liners.

For audio plug-in work, distinguish between **development tools/frameworks** and **plug-in formats**:

- JUCE, iPlug2, HISE, and Faust are tools or frameworks that can help build audio software.
- VST3, Audio Unit, CLAP, and LV2 are plug-in formats or standards in which that software may be delivered.

Do not treat “VST” as a programming language. If the student wants to make a plug-in, first discuss which development environment and which plug-in format actually fit the project.

---

# 15. Beginner HTML + CSS + JavaScript projects

For simple class projects using HTML, CSS, and JavaScript, default to **one file**:

```text
index.html
```

Put CSS inside:

```html
<style>
    /* CSS here */
</style>
```

Put JavaScript inside:

```html
<script>
    // JavaScript here
</script>
```

Keep the HTML, CSS, and JavaScript together in `index.html` unless there is a clear technical reason to separate them.

If separate files become genuinely useful, explain why before restructuring the project.

Images, sound files, fonts, data, and similar resources may go in a simple folder such as:

```text
assets/
```

Avoid creating complex web-development structures for small beginner projects.

---

# 16. Build useful logging into the program

Every project should include enough logging to make problems easier to understand and troubleshoot.

Logging means that while the program runs, it leaves useful messages about what it is doing.

For a browser project, use the browser console appropriately, for example:

```javascript
console.log("Audio engine started");
console.warn("No microphone permission yet");
console.error("Could not load sound file", error);
```

For projects with a server, backend, or another runtime, use the normal logging system for that environment so important information is visible in the terminal, console, server logs, or application logs.

Useful things to log include:

- application startup and shutdown;
- important initialization steps;
- major user actions when they affect program state;
- successful or failed loading of important files or resources;
- connections to servers or external services;
- meaningful state changes;
- warnings;
- errors and enough context to understand where they happened.

When an error is caught, preserve useful diagnostic information instead of silently hiding the error.

Logging should help answer questions such as:

- Did this part of the program run?
- What happened immediately before the problem?
- Did the file, device, network request, or audio system load successfully?
- What value or state caused the failure?
- Where in the program did the error occur?

Keep logs readable.

Do not flood the console with messages on every animation frame, audio sample, mouse movement, or other extremely frequent event unless temporarily debugging that specific problem.

Never print passwords, API keys, authentication tokens, private personal information, or other secrets into logs.

When troubleshooting, inspect the available logs early rather than guessing blindly.

If temporary debugging logs are added, remove unnecessary noise once the problem is understood while keeping the useful operational logging that will help future troubleshooting.

Document any unusual logging system or log-file location in `README.md` or `docs/architecture.md`.

---


# 15. Deployment comes after the local project

A project may be deployed to a service such as `here.now`, GitHub Pages, Netlify, Vercel, or another host.

The local project folder remains the source of truth.

The preferred sequence is:

```text
edit locally
→ test
→ review changes
→ commit a useful checkpoint
→ deploy
```

Do not build something only inside a deployment service if that would leave the student without an organized local copy.

If an agent creates HTML for direct deployment, it must also save the same working code inside the project folder.

Record deployment information in `docs/deployment.md`.

---

# 16. Start every coding session by understanding the project

At the beginning of each coding session, read or inspect the relevant project context before changing code.

At minimum, check:

```text
AGENTS.md
TASKS.md
README.md
PROJECT.md
docs/
```

Also inspect:

```bash
git status
git diff
```

when Git is available.

Do not assume that the previous agent's memory is available.

The project files are the shared memory between people and agents.

Use them.

---

# 17. End every coding session cleanly

Before ending a substantial session:

1. Check that the project still runs or behaves as expected.
2. Review the files that changed.
3. Update `TASKS.md`.
4. Update documentation that has become inaccurate.
5. Add a short entry to `docs/development-log.md` when the session made a meaningful change.
6. Record important new decisions in `docs/decisions.md`.
7. Make a clear Git commit when appropriate.
8. Tell the student what happened.

Give the student a short summary in plain language:

```text
What we did:
...

How to run or view it:
...

What to notice:
...

What comes next:
...
```

---

# 18. Teach while building

The student is learning through the project.

When using an unfamiliar command or concept:

- explain it briefly before or immediately after using it;
- use ordinary language;
- connect the explanation to what the student is currently doing;
- avoid overwhelming them with theory they do not yet need.

For example:

> A commit is a named checkpoint in the project's history. If something goes wrong later, Git helps us see what changed.

Prefer useful explanations over jargon.

If you use a technical term, explain it the first time.

---

# 19. Keep the student in control

The agent may handle routine technical work independently, but the student remains the author of the project.

Ask before actions that have significant consequences, including:

- deleting important files or data;
- replacing a working approach with a major rewrite;
- changing the project's architecture substantially;
- publishing private information;
- pushing to GitHub or another remote repository;
- deploying publicly when the student has not already approved deployment;
- changing account-level or global computer settings.

For ordinary safe coding work, proceed efficiently and explain what matters.

---

# 20. Prefer clarity over sophistication

For this class:

**simple and understandable is usually better than clever and complicated.**

Avoid adding frameworks, libraries, build systems, databases, cloud services, or architectural layers merely because they are common in professional software development.

Add complexity when the project actually benefits from it.

When adding a new dependency or tool, be prepared to answer:

> What problem does this solve for this project?

---

# 21. Leave the project better organized than you found it

Whenever you work on the project:

- preserve useful history;
- keep filenames understandable;
- remove accidental clutter when safe;
- keep documentation truthful;
- keep the task list current;
- keep secrets protected;
- keep the code runnable;
- make the next coding session easier than this one.

The goal is not only to make the software work.

The goal is to leave behind a project that the student can understand, continue, and learn from.