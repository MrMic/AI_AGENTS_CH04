# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Project

Chapter 4 exercises from the Manning *AI Agents Apps* book. Scaffold for building a LangChain-based agent with web scraping (`requests` + `beautifulsoup4`) and web search (`duckduckgo-search` / `ddgs`).

Currently `main.py` is a placeholder — implementation lands here as the chapter progresses.

## Toolchain

- Python **3.13** (pinned via `.python-version`)
- Package manager: **uv** (do not use `pip` directly)
- Dependencies tracked in `requirements.txt`; `pyproject.toml` `[project.dependencies]` is empty — the requirements file is the source of truth for now

## Commands

```bash
uv sync                          # create .venv + install from pyproject
uv pip install -r requirements.txt  # install pinned chapter deps
uv run python main.py            # run entrypoint
uv add <pkg>                     # add a new dep (updates pyproject + lock)
uv pip index versions <pkg>      # check latest PyPI version
```

## Conventions

- LangChain stack is pinned to **1.x** (`langchain==1.3.x`, `langchain-openai==1.3.x`) — API differs from 0.x tutorials; check Context7 docs before assuming an import path.
- Use canonical `beautifulsoup4`, not the `bs4` shim.
- `duckduckgo-search` is being superseded by `ddgs`; both present during transition.
