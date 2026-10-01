# Personal CLI Toolkit

A small command-line tool with three subcommands for quotes and notes.

## Install

```bash
git clone https://github.com/Ematute3/ai-engineering.git
cd ai-engineering/phase-01.5-ai-native-workflow/week-1/projects/cli-toolkit
```

No dependencies — pure Python standard library.

## Usage

```bash
python toolkit.py quote
python toolkit.py note "buy milk"
python toolkit.py notes
```

## Subcommands

| Command | What it does |
|---------|--------------|
| `quote` | Print a random motivational quote |
| `note "<text>"` | Save a note to `notes.txt` |
| `notes` | List all saved notes, numbered |
| `--help` | Show usage |

## Tests

```bash
pytest test_toolkit.py -v
```

## Project structure

```
cli-toolkit/
├── toolkit.py        # main script
├── test_toolkit.py   # pytest tests
└── README.md         # this file
```
