# Dotfiles

Personal configuration files for macOS development environment.

## Overview

This repository contains configuration for:

| Tool | Description | Documentation |
|------|-------------|---------------|
| [nvim](nvim/) | Neovim editor with LSP, Telescope, and modern plugins | [README](nvim/README.md) |
| [ghostty](ghostty/) | Terminal emulator with theme manager CLI (`term`) | [README](ghostty/README.md) |
| [zellij](zellij/) | Terminal multiplexer with Claude Code layouts | [README](zellij/README.md) |
| [zsh](zsh/) | Shell configuration with Powerlevel10k | - |
| [claude](claude/) | Claude Code CLI settings and statusline | - |
| [git](git/) | Git configuration | - |
| [lazygit](lazygit/) | Lazygit TUI configuration | - |
| [fastfetch](fastfetch/) | System info display | - |
| [btop](btop/) | Resource monitor | - |
| [thefuck](thefuck/) | Command correction | - |

## Quick Start

```bash
# Clone the repository
git clone https://github.com/Cabbagito/dotfiles ~/.config

# Run the install script
cd ~/.config
./install.sh
```

## Key Interconnections

### Ghostty + Neovim Theme Sync
The `term` CLI tool automatically syncs theme changes to running Neovim instances:
```bash
term theme set catppuccin-mocha  # Changes both Ghostty and Neovim themes
```

### Zellij + Claude Code Layouts
Custom layouts for Claude Code development workflows:
- `claude-3` - Three Claude Code instances + shell tab
- `claude-5` - Five Claude Code instances
- `ccc` - Minimal single-tab layout

Launch with:
```bash
zj                    # Default session with fastfetch
zellij -l claude-3    # Multi-Claude layout
ccc                   # Attach/create ccc session
```

### Shell Aliases
Key aliases defined in `.zshrc`:
- `vim` → `nvim`
- `lg` → `lazygit`
- `term` → Ghostty theme manager
- `zj` → Launch zellij with named session
- `ccc` → Quick Claude Code session
- `ff` → fastfetch

## Requirements

- macOS (tested on Sequoia)
- [Homebrew](https://brew.sh/)
- A [Nerd Font](https://www.nerdfonts.com/) for icons

### Core Dependencies

```bash
brew install neovim ghostty zellij fzf ripgrep zoxide lazygit
brew install --cask font-jetbrains-mono-nerd-font
```

### Shell Setup

```bash
# Oh My Zsh
sh -c "$(curl -fsSL https://raw.githubusercontent.com/ohmyzsh/ohmyzsh/master/tools/install.sh)"

# Powerlevel10k theme
git clone --depth=1 https://github.com/romkatv/powerlevel10k.git ${ZSH_CUSTOM:-$HOME/.oh-my-zsh/custom}/themes/powerlevel10k

# Plugins
git clone https://github.com/zsh-users/zsh-autosuggestions ${ZSH_CUSTOM:-~/.oh-my-zsh/custom}/plugins/zsh-autosuggestions
git clone https://github.com/zsh-users/zsh-syntax-highlighting ${ZSH_CUSTOM:-~/.oh-my-zsh/custom}/plugins/zsh-syntax-highlighting
```

## Structure

```
~/.config/
├── README.md              # This file
├── CLAUDE.md              # AI assistant context
├── .gitignore
├── install.sh             # Setup script
│
├── nvim/                  # Neovim (lazy.nvim, LSP, Telescope)
├── ghostty/               # Terminal + theme manager CLI
├── zellij/                # Multiplexer with Claude layouts
├── zsh/                   # Shell config (p10k.zsh)
├── claude/                # Claude Code settings
├── git/                   # Git config
├── lazygit/               # Lazygit config
├── fastfetch/             # System info display
├── btop/                  # Resource monitor
└── thefuck/               # Command correction
```

## License

Personal configuration - feel free to take inspiration.
