# GitHub Copilot Setup

Copilot is your AI pair-programmer. It's free for students, otherwise $10/mo. Set it up properly — half-assed setup = half-assed results.

## Step 1 — Sign up

1. Go to https://github.com/features/copilot
2. Click **Sign up** or **Get Copilot Free**
3. Choose your plan:
   - **Free tier:** 50 chat messages/month, 2,000 code completions/month. Fine to start.
   - **Student:** Free Copilot Pro (unlimited) if you have a `.edu` email. Sign up at https://education.github.com with your student account.
   - **Pro:** $10/mo, unlimited.
4. Connect your GitHub account

## Step 2 — Connect VS Code

1. Open VS Code
2. Press `Cmd+Shift+X` to open Extensions
3. Search `GitHub Copilot`
4. Install both:
   - **GitHub Copilot** (the autocomplete)
   - **GitHub Copilot Chat** (the chat panel)
5. VS Code will pop up asking you to sign in — do it, use your GitHub account
6. After signing in, you should see a Copilot icon in the bottom status bar

## Step 3 — Verify it works

Open any `.py` file in your project. Start typing:

```python
# function that reverses a string
def reverse_string(s):
```

Copilot should suggest the rest in gray text. Press **Tab** to accept.

If nothing appears:
- Check the bottom-right of VS Code — does it show "Copilot" with a checkmark?
- Try `Cmd+Shift+P` → "Copilot: Sign In"
- Make sure you're in a `.py` file, not a `.md` or `.txt`

## Step 4 — Learn the 4 ways to use Copilot

### 1. Inline autocomplete (passive)
Just type. Copilot predicts the next line. **Tab** to accept, **Esc** to reject.

### 2. Copilot Chat (active conversation)
- `Cmd+I` opens the inline chat — ask Copilot to do something in the current file
- `Cmd+Shift+I` or click the chat icon in the sidebar for the full chat panel
- Use cases:
  - "Explain what this function does"
  - "Refactor this to be cleaner"
  - "Add error handling to this code"
  - "Write tests for this"

### 3. Slash commands in chat
Type `/` in Copilot Chat to see commands:
- `/explain` — explain the selected code
- `/fix` — fix bugs in the selected code
- `/tests` — generate unit tests
- `/doc` — write docstrings
- `/new` — scaffold a new file from a prompt

### 4. Inline Chat (`Cmd+I`)
Highlight code, hit `Cmd+I`, ask a question. Faster than switching to the panel.

## Step 5 — Prompt patterns that actually work

Bad prompt: "make a calculator"
Good prompt: "Write a Python function `add(a, b)` that takes two numbers and returns their sum. Include a docstring and type hints."

Bad prompt: "fix this"
Good prompt: "This function crashes when input is empty. Add a guard that returns `None` for empty input."

Bad prompt: "write tests"
Good prompt: "Write pytest tests for the `reverse_string` function above. Cover: normal string, empty string, single character, palindrome."

**The pattern:** be specific about inputs, outputs, edge cases, and constraints. AI is a genius intern — it does exactly what you say, no more.

## What's next

Once Copilot is set up and verified working, move to [`week-1/projects/cli-toolkit/README.md`](../projects/cli-toolkit/README.md).
