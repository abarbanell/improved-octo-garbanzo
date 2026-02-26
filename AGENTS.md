# AGENTS

## Project Overview

Prototype web application built with Flask (Python). Used for exploring AI-assisted development workflows with Ona.

Development environment: Dev container using `mcr.microsoft.com/devcontainers/universal:4.0.1-noble`.

## Repository Layout

```
app.py                  # Flask application entry point
templates/              # Jinja2 HTML templates
static/                 # CSS, JS, and other static assets
requirements.txt        # Python dependencies
.env.example            # Template for required environment variables
.gitignore              # Git ignore rules
.devcontainer/          # Dev container configuration
.ona/                   # Ona review and skill files
AGENTS.md               # This file — conventions for AI agents
```

## Development Setup

1. Open the repository in an Ona environment (or any devcontainer-compatible tool).
2. Create a virtualenv and install dependencies:
   ```
   python3 -m venv venv
   . venv/bin/activate
   pip install -r requirements.txt
   ```
3. Copy `.env.example` to `.env` and fill in values (see README for details):
   ```
   cp .env.example .env
   ```
4. Run the app:
   ```
   python app.py
   ```
   The server starts on port 5000. Set `FLASK_DEBUG=1` in `.env` to enable debug mode.

## Architecture

Server-rendered Flask app with Google OAuth via Authlib.

Routes:
- `/` — Login page (shows logout confirmation when arriving from `/logout`)
- `/login` — Redirects to Google OAuth consent screen
- `/callback` — OAuth callback, stores user info in session
- `/profile` — Displays user profile data (requires login)
- `/logout` — Clears session, redirects to `/`

User data is stored in the Flask session (cookie-based). No database.

## Conventions

### Code Style

- Follow PEP 8 for Python code.
- Use meaningful variable and function names. Avoid abbreviations unless universally understood (e.g., `ctx`, `err`, `req`, `res`).
- Templates use Jinja2. Keep logic in Python; templates should only handle presentation.

### Commit Messages

- Use imperative mood: "Add feature" not "Added feature".
- First line: concise summary under 72 characters.
- Body (if needed): explain *why*, not *what*.
- Include `Co-authored-by: Ona <no-reply@ona.com>` when changes are agent-assisted.

### Branch Naming

- `feature/<short-description>` for new features
- `fix/<short-description>` for bug fixes
- `chore/<short-description>` for maintenance tasks

### File Organization

- Keep related files together. Prefer flat structures until complexity demands nesting.
- Configuration files belong in the project root.
- Do not create documentation files unless explicitly asked — prefer code comments and README updates.

## Testing

No test framework is configured yet. When one is added (likely `pytest`):
- Run the full test suite before committing.
- New code should include tests.
- Document the test command in this section.

## Common Tasks

### Adding a new dependency

1. Activate the virtualenv: `. venv/bin/activate`
2. Install: `pip install <package>`
3. Update requirements: `pip freeze > requirements.txt`
4. Commit `requirements.txt`.

### Starting a new feature

1. Create a branch: `git checkout -b feature/<name>`.
2. Make changes in small, focused commits.
3. Open a PR against `main`.

## Do Not

- Do not install dependencies without first checking that `.gitignore` exists and is appropriate.
- Do not commit `node_modules/`, `venv/`, `__pycache__/`, or other dependency/build directories.
- Do not modify `.devcontainer/devcontainer.json` without explicit approval.
- Do not create arbitrary markdown files — update existing docs or code comments instead.
- Do not add JavaScript frameworks (React, Vue, etc.) unless explicitly asked. This is a server-rendered Flask app.
