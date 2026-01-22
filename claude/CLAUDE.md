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
