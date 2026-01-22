# Claude Code CLI Configuration

Configuration files for [Claude Code](https://docs.anthropic.com/en/docs/claude-code), Anthropic's official CLI for Claude.

## Features

- **Custom Status Line**: Dynamic status bar showing user, host, directory, git branch, and model
- **Always Thinking**: Extended thinking mode enabled by default for deeper reasoning
- **Auto Updates**: Automatic updates from the latest release channel

## Files

| File | Location | Purpose |
|------|----------|---------|
| `settings.json` | `~/.config/claude/` | Main configuration file |
| `statusline-command.sh` | `~/.claude/` | Custom status line generator script |

## Configuration Overview

### settings.json

```json
{
  "permissions": { "defaultMode": "default" },
  "statusLine": { "type": "command", "command": "bash ~/.claude/statusline-command.sh" },
  "alwaysThinkingEnabled": true,
  "autoUpdatesChannel": "latest"
}
```

### Status Line

The custom status line displays:
- Current user and hostname
- Working directory (abbreviated)
- Git branch (when in a repository)
- Active model name

## Customization

To modify the status line output, edit `~/.claude/statusline-command.sh`. The script receives JSON data via stdin containing context about the current session.

To change Claude Code behavior, edit `settings.json`. See the [schema](https://json.schemastore.org/claude-code-settings.json) for available options.

## Related

- [Claude Code Documentation](https://docs.anthropic.com/en/docs/claude-code)
- Parent dotfiles: `~/.config/`
