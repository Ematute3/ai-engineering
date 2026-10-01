# Glossary — Terms I'm Building Real Understanding Of

I'll add a term here the first time I actually understand it (not just hear it). If I can't explain it simply, I haven't earned it.

---

## Phase 01 — Python

**Variable** — a name attached to a value. The value can change; the name is just a label.

**String** — text. Anything in quotes.

**Integer / Float** — whole numbers / numbers with decimals.

**List** — ordered, changeable collection. `[1, 2, 3]`.

**Dictionary** — key-value pairs. `{"name": "Evan", "age": 30}`.

**Loop** — repeating code until a condition is met.

**Function** — a reusable block of code that takes inputs and returns an output.

**Class** — a blueprint for making objects that bundle data (attributes) and behavior (methods) together.

**Module** — a `.py` file you can `import` from.

**Package** — a folder of modules with an `__init__.py`.

---

## Phase 02 — Tooling

**Virtual environment (venv)** — an isolated Python install for one project. So project A's packages don't break project B.

**requirements.txt** — a list of packages and versions a project needs.

**API** — a way for programs to talk to each other over HTTP. You send a request, get a response.

**HTTP** — the protocol of the web. GET, POST, etc.

**JSON** — a text format that looks like Python dicts/lists. The lingua franca of APIs.

**REST** — a style of API design where URLs are nouns and HTTP methods are verbs.

---

## Phase 03 — Data & ML

**NumPy** — Python library for fast array math. The foundation of basically everything.

**Pandas** — Python library for tabular data (think: Excel, but programmatic).

**Model** — a function that takes input and predicts output, learned from data instead of written by hand.

**Training** — adjusting the model's parameters so it does well on data.

**Train / validation / test split** — three cuts of your data: train to learn, validation to tune, test to honestly evaluate.

**Overfitting** — the model memorized the training data instead of learning the pattern. Bad on new data.

**Transformer** — the architecture behind modern LLMs. Attention-based. Reads all tokens at once instead of one by one.

**Attention** — a way for the model to decide which other words in a sentence matter most for understanding the current word.

---

## Phase 04 — LLMs

**LLM (Large Language Model)** — a transformer trained on a huge amount of text to predict the next token.

**Token** — the chunk of text a model reads. Roughly 4 characters in English. Models have a context window measured in tokens.

**Context window** — how much text the model can see at once. Bigger = more memory, more cost.

**Prompt** — the input you give the model. Can include system instructions, examples, and the actual question.

**System prompt** — hidden instructions that set the model's behavior. Sets the "personality."

**Temperature** — a setting from 0 to 2. Low = focused and deterministic. High = creative and random.

**Embedding** — a list of numbers that represents the meaning of text. Similar text → similar numbers.

**Vector database** — a database optimized for "find me the things most similar to this." Stores embeddings.

**RAG (Retrieval-Augmented Generation)** — look up relevant info first, then give it to the model as context. Reduces hallucination.

---

## Phase 05 — LangChain

**Chain** — a sequence of calls stitched together (prompt → model → output parser).

**LCEL (LangChain Expression Language)** — the pipe-style syntax for building chains. `prompt | model | parser`.

**Retriever** — a component that fetches relevant documents given a query.

**Memory** — how a chain keeps track of conversation history.

**Tool** — a function an agent can call (search web, run code, query DB).

---

## Phase 06 — Agents

**Agent** — an LLM loop that decides which tool to call, calls it, reads the result, decides again, until done.

**ReAct** — "Reason + Act." The agent thinks out loud, picks a tool, observes, repeats.

**Multi-agent** — multiple agents with different roles, handing off to each other.

**Observability / tracing** — recording every step an agent took so you can debug it later.

---

## Open questions I'll resolve as I learn

- What's the actual difference between LangChain and just calling the API directly?
- When does an agent help vs. just being a more expensive way to call a function?
- What does "fine-tuning" actually change vs. prompting?
