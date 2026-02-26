# AGENTS Improvement Spec

## Current State

| Item | Status |
|---|---|
| `AGENTS.md` | Missing |
| Agent skill files (`.ona/skills/`, `.cursor/rules/`, etc.) | Missing |
| `.gitignore` | Missing |
| `CONTRIBUTING.md` / `CODEOWNERS` | Missing |
| CI/CD configuration | Missing |
| README with project context | Stub only ("test the vibe of ona") |
| `.devcontainer/devcontainer.json` | Present, uses universal image |
| `.ona/review/comments.json` | Present, empty |

## What's Good

- **Dev container configuration exists.** The `devcontainer.json` uses a standard Microsoft universal image and includes helpful comments about alternatives. This means agents can spin up a working environment immediately.
- **`.ona/` directory is initialized.** The review infrastructure is in place, even if currently empty.

## What's Missing

### 1. AGENTS.md (high priority)

No `AGENTS.md` exists. This is the primary file AI agents read to understand project conventions. Without it, agents have zero project-specific context and fall back to generic behavior.

### 2. .gitignore (high priority)

No `.gitignore` exists. Any agent that installs dependencies (e.g., `npm install`, `pip install`) will create large directories that could be accidentally committed.

### 3. Agent skill/rule files (medium priority)

No tool-specific agent configuration exists:
- No `.cursor/rules/` for Cursor AI
- No `.github/copilot-instructions.md` for GitHub Copilot
- No `.aider*` config for Aider
- No `CLAUDE.md` for Claude Code

### 4. Contributing guidelines (low priority)

No `CONTRIBUTING.md` or `CODEOWNERS`. Less urgent for a test/experimental repo, but useful once the project has a defined purpose.

### 5. CI/CD (low priority)

No GitHub Actions workflows or other CI configuration. Agents benefit from CI because they can verify their changes pass automated checks.

## What's Wrong

- **README provides no useful context.** The single line "test the vibe of ona" tells agents nothing about the project's language, framework, architecture, or conventions. Agents will guess or ask.
- **No conventions are documented anywhere.** Without any guidance, every agent session starts from scratch with no shared understanding of how the project should be structured.

## Concrete Improvements

### Action 1: Create `AGENTS.md`

Create a root-level `AGENTS.md` with these sections:

```markdown
# AGENTS

## Project Overview
Brief description of the project's purpose, primary language(s), and architecture.

## Repository Layout
Map of key directories and their purpose.

## Development Setup
How to install dependencies and run the project.

## Conventions
- Code style and formatting rules
- Naming conventions
- Commit message format
- Branch naming strategy

## Testing
How to run tests. What test framework is used. Expected coverage.

## Common Tasks
Step-by-step for frequent operations (e.g., adding a new feature, running migrations).

## Do Not
Explicit list of things agents should avoid (e.g., "Do not modify X", "Do not use library Y").
```

**Note:** Since this repo has no source code yet, the initial `AGENTS.md` should be a skeleton that establishes the structure. Fill in sections as the project takes shape. Avoid placeholder text like "TBD" — either include real content or omit the section until it's relevant.

### Action 2: Create `.gitignore`

Create a `.gitignore` appropriate for the likely project type. Since the repo purpose is unclear, start with a general-purpose template covering Node.js, Python, Go, and IDE artifacts:

```
node_modules/
dist/
build/
__pycache__/
*.pyc
venv/
.env
.env.local
*.log
.DS_Store
.idea/
*.swp
*.swo
```

### Action 3: Expand README.md

Update `README.md` to include at minimum:
- What the project is
- How to set up the development environment (reference the devcontainer)
- How to run the project

This gives agents (and humans) enough context to be productive.

### Action 4: Add `.ona/skills/` directory (optional)

If the project develops recurring workflows (e.g., "add a new API endpoint", "run database migrations"), create skill files in `.ona/skills/` to codify them. Not needed until the project has actual code.

## Priority Order

1. **Create `.gitignore`** — prevents accidental commits of dependency directories. Zero risk, immediate value.
2. **Create `AGENTS.md`** — establishes project conventions for all agents. Fill in as the project develops.
3. **Expand `README.md`** — provides human and agent context.
4. **Add agent skill files** — defer until the project has defined workflows.
5. **Add CI/CD** — defer until there's code to test.
