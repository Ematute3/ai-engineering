# ROADMAP — Zero to AI Engineer

**Pace:** 1–2 hours/day, 5 days/week. **Total:** ~24 weeks (5–6 months).
**Commit cadence:** at least one commit per day you work. Git history = proof.
**Math note:** I'm staying at algebra level. I'll learn concepts visually and through code, not proofs. If I hit a wall where I can't fake it (e.g., fine-tuning), I'll add 3Blue1Brown then.

---

## Phase 01 — Python Basics (Weeks 1–4)

**Goal:** I can read and write small Python scripts without Googling every line.

| Week | Topic | Concrete deliverable |
|------|-------|---------------------|
| 1 | Variables, types, strings, print/input | 10 tiny scripts in `phase-01/week-01/` |
| 2 | Conditionals, loops, lists, dicts | A number-guessing game + a word-frequency counter |
| 3 | Functions, file I/O, exceptions | A script that reads a CSV and prints stats |
| 4 | OOP basics, modules, packages | A small `library/` package with 2 classes |

**Checkpoint to pass before Phase 02:** I can write a script from scratch that reads a file, transforms data, and writes output — without copy-pasting.

## Phase 02 — Python Tooling (Weeks 5–8)

**Goal:** I can manage real projects: dependencies, virtual envs, version control, testing.

| Week | Topic | Concrete deliverable |
|------|-------|---------------------|
| 5 | Git basics + GitHub workflow | This repo pushed to GitHub, first PR merged to my own `dev` branch |
| 6 | Virtual envs, pip, requirements.txt | Clean venv workflow, can install/uninstall without breaking my system |
| 7 | HTTP, REST, `requests`, JSON | Script that calls 3 real public APIs (weather, github, jokes) |
| 8 | Testing with pytest, logging, debugging | Same API script, now with tests and structured logging |

**Checkpoint:** I can clone a repo, set it up, make a branch, push, and open a PR — fluently.

## Phase 03 — Data & ML Foundations (Weeks 9–12)

**Goal:** I know what a model actually is, at a working-intuition level.

| Week | Topic | Concrete deliverable |
|------|-------|---------------------|
| 9 | NumPy basics | Array ops, broadcasting, a small linear algebra demo |
| 10 | Pandas basics | Load a CSV, clean it, group/aggregate, plot |
| 11 | What is ML? Supervised vs unsupervised, train/val/test | Train a tiny classifier on the Iris dataset |
| 12 | Neural nets intuition, transformers intuition | Read "The Illustrated Transformer", write notes in `notes/` |

**Checkpoint:** I can explain — in writing — what a transformer does, in my own words, to a non-technical friend.

## Phase 04 — LLM APIs (Weeks 13–16)

**Goal:** I can call LLMs from Python and build real things with them.

| Week | Topic | Concrete deliverable |
|------|-------|---------------------|
| 13 | First API call, prompts, tokens, temperature | Chat CLI in Python that talks to an LLM |
| 14 | System prompts, structured output (JSON mode), function calling | A "tool-using" prompt that returns validated JSON |
| 15 | Embeddings, vector search, ChromaDB | A semantic search over my own notes folder |
| 16 | RAG: chunking, retrieval, generation, evaluation | A RAG system that answers questions about a PDF I pick |

**Checkpoint:** I have a working RAG app. I can explain every line.

## Phase 05 — LangChain (Weeks 17–19)

**Goal:** I understand why LangChain exists, use it where it helps, skip it where it doesn't.

| Week | Topic | Concrete deliverable |
|------|-------|---------------------|
| 17 | Chains, prompt templates, output parsers, LCEL | Rebuild my RAG app using LangChain |
| 18 | Memory, conversation history, retrieval augmented chat | A chatbot that remembers context across turns |
| 19 | LangChain agents (intro), tool registration | An agent that can use 2–3 tools |

**Checkpoint:** I can read a LangChain error message and fix it without rage-quitting.

## Phase 06 — Agents (Weeks 20–23)

**Goal:** I can build and reason about agentic systems.

| Week | Topic | Concrete deliverable |
|------|-------|---------------------|
| 20 | ReAct loop, planning, reflection | Build a ReAct agent from scratch (no framework) |
| 21 | Tool design, error handling, observability | Wrap my agent with LangSmith tracing |
| 22 | Multi-agent systems, routing | A 2-agent system (researcher + writer) |
| 23 | Frameworks: LangGraph, CrewAI, AutoGen — pick one | A small project in my chosen framework |

**Checkpoint:** I can name 3 things each framework is bad at. (This means I actually compared them.)

## Phase 07 — Capstone (Weeks 24+)

**Goal:** A real project on a real GitHub repo that someone can look at and learn from me.

Pick ONE:
- Personal research assistant (RAG over your notes/PDFs, with agents that can take actions)
- Codebase Q&A bot (ingests a repo, answers questions about it)
- Daily-briefing agent (scrapes RSS/news, summarizes, emails you)
- Workflow automation agent (reads inbox, drafts replies, files things)

Requirements:
- Public GitHub repo with a real README
- Tests
- Deployment (even just a Dockerfile)
- A short blog post explaining what I built and why

---

## What I'm NOT doing

- Reinforcement learning from scratch (out of scope for AI engineer)
- Training models from scratch (out of scope)
- Math proofs (algebra-level is the ceiling unless I change my mind)
- Tutorial hell — I code, I don't watch 40 hours of videos

## How I'll know this worked

In 6 months, if someone asks me "how does an agent work", I don't answer with a definition from a YouTube video. I open my laptop and show them mine.
