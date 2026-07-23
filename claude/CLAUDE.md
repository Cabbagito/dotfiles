# Claude Code Configuration - AI Assistant Context

Configuration context for AI assistants working with Claude Code CLI settings.

## Overview

This directory contains Claude Code CLI configuration. The setup includes a custom status line script that provides contextual information during sessions.

## Architecture

### Status Line Data Flow

```
┌─────────────────┐      JSON stdin       ┌─────────────────────┐
│   Claude Code   │ ───────────────────► │ statusline-command  │
│      CLI        │                       │       .sh           │
└─────────────────┘                       └─────────────────────┘
                                                   │
                                                   │ parse & format
                                                   ▼
                                          ┌─────────────────────┐
                                          │   ANSI-colored      │
                                          │   status output     │
                                          └─────────────────────┘
```

### JSON Input Structure

The status line script receives JSON via stdin:
- `current_dir` - Current working directory
- `project_dir` - Project root directory
- `model` - Active model information

## Key Settings

| Setting | Value | Effect |
|---------|-------|--------|
| `permissions.defaultMode` | `"default"` | Standard permission prompts |
| `statusLine.type` | `"command"` | External command generates status |
| `alwaysThinkingEnabled` | `true` | Extended thinking on all requests |
| `autoUpdatesChannel` | `"latest"` | Automatic updates from latest |

## Status Line Components

The output format: `user@host * directory * git_branch * model_name`

Components:
1. **User/Host** - Current user and machine identifier
2. **Directory** - Abbreviated working directory path
3. **Git Branch** - Current branch when in a git repository
4. **Model** - Active Claude model name

## Color Scheme

| Component | Color | ANSI Code |
|-----------|-------|-----------|
| Username | Magenta | `\e[35m` |
| @ symbol | White | `\e[37m` |
| Hostname | Cyan | `\e[36m` |
| Directory | Blue | `\e[34m` |
| Git Branch | Yellow | `\e[33m` |
| Model Name | Green | `\e[32m` |
| Separators | Dim | `\e[2m` |

## Modification Patterns

### Customizing Status Line Output

Edit `~/.claude/statusline-command.sh`:
1. Modify the parsing logic for different JSON fields
2. Change color codes for different appearance
3. Add/remove components from the output string
4. Adjust separators or formatting

### Changing Claude Code Behavior

Edit `settings.json`:
1. Toggle `alwaysThinkingEnabled` for thinking mode
2. Change `autoUpdatesChannel` to `"stable"` for less frequent updates
3. Modify `permissions.defaultMode` for different permission handling

## Testing Changes

```bash
# Test status line script directly
echo '{"current_dir":"/test","project_dir":"/test","model":"opus"}' | bash ~/.claude/statusline-command.sh

# Validate settings.json syntax
python3 -c "import json; json.load(open('settings.json'))"

# Restart Claude Code to apply settings changes
```

## File Locations

- Config directory: `~/.config/claude/`
- Status script: `~/.claude/statusline-command.sh`
- Note: These are separate directories (`~/.config/claude` vs `~/.claude`)

## IMPORTANT: Settings Live in TWO Files

Claude Code config is split across two locations. When debugging "why is my setting not taking effect", **always check both**:

1. **`~/.config/claude/settings.json`** (symlinked from `~/.claude/settings.json`) — the
   dotfile-managed settings. Edited by hand / via this repo.
2. **`~/.claude.json`** — written by the `/config` UI and by Claude Code itself. Holds
   OAuth session, MCP servers, per-project state, `numStartups`, `theme`,
   `hasCompletedOnboarding`, and a number of UI toggles including
   `leftArrowOpensAgents`, `autoScrollEnabled`, `editorMode`.

### Precedence gotcha

For UI-ish toggles that exist in both files, **`~/.claude.json` wins at runtime** (it's
what `/config` reads/writes). If `settings.json` says `true` and `~/.claude.json` says
`false`, the user sees `false` and `/config` shows `false`. This has bitten us before
(see `leftArrowOpensAgents`).

### Debugging checklist when a setting "doesn't stick"

```bash
# Compare both files for the setting in question
jq '.leftArrowOpensAgents' ~/.claude.json
jq '.leftArrowOpensAgents' ~/.config/claude/settings.json

# If they disagree, align them (usually patch ~/.claude.json):
cp ~/.claude.json ~/.claude.json.bak-$(date +%Y%m%d-%H%M%S)
jq '.leftArrowOpensAgents = true' ~/.claude.json > ~/.claude.json.tmp \
  && mv ~/.claude.json.tmp ~/.claude.json
```

Known UI toggles that may live in `~/.claude.json` rather than (or in addition to)
`settings.json`: `leftArrowOpensAgents`, `autoScrollEnabled`, `editorMode`,
`showTurnDuration`, `teammateMode`, `terminalProgressBarEnabled`, `theme`.

### Key UI toggles, explained

| Setting | What it does |
|---------|--------------|
| `leftArrowOpensAgents` | Pressing `←` from the prompt opens the agents view |
| `autoScrollEnabled` | Auto-scroll viewport to follow streaming output (off = stays put while you read) |
| `editorMode` | `"emacs"` (readline bindings) vs `"normal"` (vim modal editing) |
| `agentViewOpenOnStartup` | Whether the agents view is visible when Claude Code launches |
| `defaultMode` (under `permissions`) | Default permission mode (`"auto"`, `"default"`, etc.) |
