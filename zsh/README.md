# Zsh Configuration

Personal Zsh shell configuration with Oh My Zsh, Powerlevel10k theme, and productivity-focused customizations.

## Features

### Framework & Theme
- **Oh My Zsh** - Plugin framework and configuration management
- **Powerlevel10k** - Fast, feature-rich prompt with instant prompt support
- Custom p10k configuration in `p10k.zsh`

### Plugins
| Plugin | Purpose |
|--------|---------|
| git | Git aliases and completions |
| fzf | Fuzzy finder integration |
| zsh-autosuggestions | Fish-like command suggestions |
| zsh-syntax-highlighting | Command syntax coloring |
| zsh-autocomplete | Real-time completions |

### Tools Integration
- **Homebrew** - Package manager paths
- **fzf** - Fuzzy finding key bindings
- **zoxide** - Smart directory jumping (`z` command)
- **thefuck** - Command correction

## Aliases

| Alias | Command | Description |
|-------|---------|-------------|
| `c` | `clear` | Clear terminal |
| `ll` | `ls -l` | Long listing |
| `vim` | `nvim` | Use Neovim |
| `lg` | `lazygit` | Git TUI |
| `pwdc` | `pwd \| pbcopy` | Copy current path |
| `claude-yolo` | `claude --dangerously-skip-permissions` | Claude without confirmations |
| `me` / `this` | `whoami@hostname` | Show current user/host |
| `gdu` | `gdu-go` | Disk usage analyzer |
| `ff` | `fastfetch` | System info |
| `zk` | Kill all zellij sessions | Clean slate for zellij |
| `zj` | Create/attach giskard session | Default zellij session |
| `term` | Ghostty term CLI | Terminal theme management |
| `ghost` | cd + claude-yolo | AI project workspace |

## Functions

| Function | Description |
|----------|-------------|
| `y` | Launch Yazi file manager, change to selected directory on exit |
| `ccc` | Attach to or create 'ccc' zellij session for Claude Code |

## Auto-Features

### Virtual Environment Activation
The `auto_activate_venv()` hook automatically activates Python virtual environments when entering directories containing a `.venv` folder. Deactivates when leaving.

## Files

| File | Purpose |
|------|---------|
| `.zshrc` | Main configuration (symlinked to `~/.zshrc`) |
| `p10k.zsh` | Powerlevel10k prompt configuration |
