# AGENTS

## Project Overview

This is an experimental repository for exploring AI-assisted development workflows with Ona. The project does not yet have a defined language or framework — agents should ask before assuming a tech stack.

Development environment: Dev container using `mcr.microsoft.com/devcontainers/universal:4.0.1-noble`.

## Repository Layout

```
.devcontainer/          # Dev container configuration
.ona/                   # Ona review and skill files
README.md               # Project description
AGENTS.md               # This file — conventions for AI agents
AGENTS-IMPROVEMENT-SPEC.md  # Improvement plan for agent configuration
```

## Development Setup

1. Open the repository in an Ona environment (or any devcontainer-compatible tool).
2. The universal image includes Node.js, Python, Go, Java, and common CLI tools.
3. No additional setup steps are required until the project has source code.

## Conventions

### Code Style

- Match the style of surrounding code. When no surrounding code exists, follow the language's community standard (e.g., `gofmt` for Go, Prettier defaults for JS/TS, PEP 8 for Python).
- Use meaningful variable and function names. Avoid abbreviations unless they are universally understood (e.g., `ctx`, `err`, `req`, `res`).

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

No test framework is configured yet. When one is added:
- Run the full test suite before committing.
- New code should include tests.
- Document the test command in this section.

## Common Tasks

### Adding a new dependency

1. Verify `.gitignore` covers the dependency directory (e.g., `node_modules/`, `venv/`).
2. Install the dependency using the project's package manager.
3. Commit the manifest file (e.g., `package.json`) but not the lock file unless the project explicitly tracks it.

### Starting a new feature

1. Create a branch: `git checkout -b feature/<name>`.
2. Make changes in small, focused commits.
3. Open a PR against `main`.

## Do Not

- Do not install dependencies without first checking that `.gitignore` exists and is appropriate.
- Do not commit `node_modules/`, `venv/`, `__pycache__/`, or other dependency/build directories.
- Do not modify `.devcontainer/devcontainer.json` without explicit approval.
- Do not create arbitrary markdown files — update existing docs or code comments instead.
- Do not assume a tech stack. If the project has no source code, ask before scaffolding.
