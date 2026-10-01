# DAY 0 — Setup

Do these in order. Don't skip ahead. If something fails, stop and figure out why before continuing.

## Step 1 — Create a GitHub account (you, in a browser)

1. Go to https://github.com/signup
2. Use the email you actually check
3. Pick a username you won't be embarrassed by in 2 years — this will be on your resume
4. Verify your email

Once done, tell me your GitHub username so I can help you with the repo URL.

## Step 2 — Install Homebrew (if you don't have it)

Open Terminal (Cmd+Space → "Terminal"), paste:

```bash
/bin/bash -c "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/HEAD/install.sh)"
```

Follow the prompts. This is the package manager for macOS — every dev tool you'll install for the next decade starts here.

## Step 3 — Install pyenv and Python 3.11

System Python is 3.9 — too old for modern AI libraries. Install pyenv (a Python version manager) so you don't wreck your system:

```bash
brew install pyenv
```

Add pyenv to your shell. For zsh (default on modern macOS), add to `~/.zshrc`:

```bash
echo 'export PYENV_ROOT="$HOME/.pyenv"' >> ~/.zshrc
echo 'export PATH="$PYENV_ROOT/bin:$PATH"' >> ~/.zshrc
echo 'eval "$(pyenv init -)"' >> ~/.zshrc
```

Restart Terminal. Then:

```bash
pyenv install 3.11.9
pyenv global 3.11.9
python --version   # should show 3.11.9
```

If `python` still shows the old version, close and reopen Terminal.

## Step 4 — Set up git with your identity

```bash
git config --global user.name "Your Full Name"
git config --global user.email "your-github-email@example.com"
git config --global init.defaultBranch main
git config --global pull.rebase true
```

## Step 5 — Generate an SSH key for GitHub

```bash
ssh-keygen -t ed25519 -C "your-github-email@example.com"
# press Enter to accept default location
# enter a passphrase (you'll type this once per session)
```

Then add it to GitHub:

```bash
cat ~/.ssh/id_ed25519.pub
```

Copy that output. In GitHub:
1. Click your profile picture → Settings → SSH and GPG keys → New SSH key
2. Title: "MacBook"
3. Paste the key
4. Save

Verify it worked:

```bash
ssh -T git@github.com
# should say: Hi <username>! You've successfully authenticated
```

## Step 6 — Create the repo on GitHub

1. Go to https://github.com/new
2. Repository name: `ai-engineering`
3. Description: "My zero-to-AI-engineer learning path"
4. Public
5. **Do NOT** check "Add README" or "Add .gitignore" — we already have those
6. Click "Create repository"

GitHub will show you a URL like: `git@github.com:YOUR_USERNAME/ai-engineering.git`

## Step 7 — Connect this local repo and push

I'll do this with you once you've created the GitHub repo. I'll run:

```bash
cd /Users/evanmatute/Documents/Minimax/ai-engineering
git remote add origin git@github.com:YOUR_USERNAME/ai-engineering.git
git add -A
git commit -m "Initial scaffold: roadmap, week structure, setup docs"
git push -u origin main
```

## Verification

After all of this, run this and paste me the output if anything looks weird:

```bash
python --version
git --version
git config user.name
git config user.email
ssh -T git@github.com
```

---

## Common gotchas

- **"Permission denied (publickey)"** — your SSH key isn't loaded. Try `ssh-add ~/.ssh/id_ed25519` then re-test.
- **"xcrun: error"** when running git — install Xcode CLI tools: `xcode-select --install`
- **pyenv shims not found** — restart Terminal after editing `.zshrc`
- **GitHub says username already taken** — pick a different one, or check if you have an old account
