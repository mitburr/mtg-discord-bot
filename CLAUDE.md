# CLAUDE.md
This file provides guidance to Claude Code when working with code in this repository.

## Project Overview
Discord bot that detects MTG card names wrapped in `[[double brackets]]` and replies in a thread with Scryfall links. Python + discord.py.

## IRON-CLAD RULES (NEVER VIOLATE)
1. **TDD OR NOTHING** - Follow Kent Beck's TDD:
   - List test scenarios (happy path, edge cases, errors)
   - Write failing test FIRST
   - Confirm test fails for expected reason
   - Write simplest code to pass
   - All tests pass
   - Refactor while green
2. **NEVER** commit hardcoded values, credentials, or tokens
3. **ALWAYS** use semantic commits: `type(scope): message`
   - Types: `feat`, `fix`, `docs`, `test`, `refactor`, `chore`
4. **ALL** AI documentation goes in `/docs/ai/` (except this file)

## Commands
```bash
# Setup
python -m venv venv && source venv/bin/activate
pip install -r requirements.txt

# Run
task start

# Testing
task test
task test -- tests/test_scryfall.py  # single file

# Linting
task lint
```

## Style Guide
- **Linting**: Black (line length 100) + Ruff
- **Naming**: snake_case (variables, functions), PascalCase (classes)
- **Comments**: Explain "why" not "what". Be concise.
- **Error Handling**: Never silently swallow exceptions — log and re-raise or reply with a user-facing error

## Tech Stack
| Layer | Tech |
|-------|------|
| Language | Python 3.11+ |
| Discord | discord.py 2.x |
| HTTP | aiohttp |
| Card Data | Scryfall REST API (no auth required) |
| Testing | pytest + pytest-asyncio |

## AI Guidelines
- **Be Opinionated**: Express strong opinions clearly instead of being sycophantic.
- **Be Concise**: Keep responses token-efficient.
- **Always Plan Before Execution**: Write plans explicitly to the user or in `/docs/ai/`.
