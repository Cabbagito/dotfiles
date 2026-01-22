# Dotfiles - AI Assistant Context

High-level context for AI assistants working with this configuration.

## Architecture Overview

This is a unified dotfiles repository containing configuration for a macOS development environment. The configs are interconnected - changes in one may affect others.

## Config Relationships

```
┌─────────────┐     theme sync     ┌─────────────┐
│   ghostty   │ ─────────────────► │    nvim     │
│  (terminal) │    via pynvim      │   (editor)  │
└─────────────┘                    └─────────────┘
       │
       │ runs inside
       ▼
┌─────────────┐     launches       ┌─────────────┐
│   zellij    │ ─────────────────► │   claude    │
│ (multiplex) │   via layouts      │   (CLI)     │
└─────────────┘                    └─────────────┘
       │
       │ sources
       ▼
┌─────────────┐
│    zsh      │
│   (shell)   │
└─────────────┘
```

## Key Integration Points

### 1. Ghostty → Neovim Theme Sync
- Location: `ghostty/term/neovim_sync.py`
- When `term theme set <name>` runs, it:
  1. Updates `ghostty/config` theme line
  2. Finds running Neovim instances via sockets
  3. Sends `:SyncColorscheme` command to each
- Neovim must have corresponding theme installed

### 2. Zellij → Claude Code Layouts
- Location: `zellij/layouts/`
- Layouts spawn Claude Code in specific directories
- Uses `--dangerously-skip-permissions` flag
- zjstatus plugin provides custom status bar

### 3. Shell Integration
- `.zshrc` defines aliases that tie everything together
- `term` alias points to ghostty's Python CLI
- `zj` and `ccc` functions manage zellij sessions
- Powerlevel10k config lives in `zsh/p10k.zsh`

## Common Modification Patterns

### Adding a New Theme
1. Theme must exist in both ghostty's theme list AND nvim's colorscheme plugins
2. Add to ghostty favorites: `ghostty/term/data/themes.json`
3. Ensure nvim has the colorscheme: `nvim/lua/plugins/colorscheme.lua`

### Adding a Zellij Layout
1. Create layout in `zellij/layouts/<name>.kdl`
2. Include zjstatus plugin block for status bar
3. Optionally add shell alias/function in `.zshrc`

### Modifying Keybindings
- Zellij: `zellij/config.kdl` (keybinds section)
- Neovim: `nvim/lua/config/keymaps.lua`
- Both use similar vim-style navigation (hjkl)

### Adding Shell Aliases
1. Edit `zsh/.zshrc` (canonical location)
2. Source change: `source ~/.zshrc`

## Directory-Specific Notes

### nvim/
- Uses lazy.nvim for plugin management
- Mason v2 for LSP server management
- Run `:checkhealth` after changes

### ghostty/
- `term` CLI is a Python project using uv
- Theme data in `term/data/themes.json`
- Shader files in `shaders/`

### zellij/
- Plugins (zjstatus, zjframes) in `plugins/`
- `clear-defaults=true` - all keybinds are explicit
- Main modes: normal, tab, scroll, locked

### claude/
- `settings.json` - Claude Code configuration
- `statusline-command.sh` - Custom status line script

## Testing Changes

```bash
# Neovim
nvim --headless -c "checkhealth" -c "qa"

# Ghostty themes
term theme set <name> && term  # Check current settings

# Zellij layouts
zellij -l <layout-name>

# Shell
source ~/.zshrc && alias  # Verify aliases
```

## Conventions

- **Leader key**: Space (both nvim and zellij modes)
- **Navigation**: hjkl everywhere possible
- **Mode indicators**: Color-coded in status bars
- **Tab naming**: Emoji prefixes in zellij (󰨈 for claude tabs)

## Git Commit Style

- Concise commit messages (single line preferred)
- No extended descriptions unless truly necessary
- No Co-Author footers
