# Zsh Configuration - AI Assistant Context

Context for AI assistants modifying this shell configuration.

## Overview

This directory contains Zsh shell configuration that serves as the foundation for the terminal environment. It integrates with other dotfiles components (ghostty, zellij, nvim) through aliases and functions.

## Architecture

```
~/.zshrc (symlink)
    │
    └──► ~/.config/zsh/.zshrc (canonical)
              │
              ├── Oh My Zsh framework
              │     └── plugins (git, fzf, autosuggestions, etc.)
              │
              ├── Powerlevel10k theme
              │     └── p10k.zsh (prompt config)
              │
              ├── Tool integrations
              │     ├── brew (package manager)
              │     ├── fzf (fuzzy finder)
              │     ├── zoxide (smart cd)
              │     └── thefuck (command correction)
              │
              └── Custom aliases & functions
                    └── Integration with ghostty, zellij, claude
```

## Key Customizations

### Aliases for Dotfiles Integration
```bash
term='uv run --directory ~/.config/ghostty term'  # Ghostty theme CLI
zj="zellij -s giskard"                            # Default zellij session
claude-yolo="claude --dangerously-skip-permissions"
ghost="cd ~/Documents/ai/ghost && claude-yolo"    # AI workspace
```

### Functions
- `y()` - Yazi wrapper that changes directory on exit
- `ccc()` - Zellij session manager for Claude Code workflows
- `auto_activate_venv()` - Directory hook for Python venvs

### Prompt Configuration
Powerlevel10k with instant prompt enabled. Config in `p10k.zsh` defines:
- Segment layout (left/right prompt elements)
- Colors and icons
- Transient prompt behavior

## Integration Points

### With Ghostty
The `term` alias invokes the ghostty term CLI for theme management:
```bash
term theme set <name>  # Changes terminal + nvim themes
term                   # Shows current settings
```

### With Zellij
Session management aliases create consistent workspaces:
- `zj` - Main development session (giskard)
- `zk` - Kill all sessions (clean slate)
- `ccc()` - Claude Code dedicated session

### With Claude Code
- `claude-yolo` alias for permissionless mode
- `ghost` alias combines directory change + claude launch
- Zellij layouts spawn Claude via these aliases

## Modification Patterns

### Adding a New Alias
```bash
# In .zshrc, add to alias section:
alias myalias="command"
```

### Adding a New Function
```bash
# In .zshrc, add to functions section:
myfunction() {
    # function body
}
```

### Modifying Prompt
Edit `p10k.zsh` or run `p10k configure` for guided setup.

### Adding a Plugin
```bash
# In .zshrc, add to plugins array:
plugins=(git fzf ... new-plugin)
```

## Testing Changes

```bash
# Reload configuration
source ~/.zshrc

# Verify aliases loaded
alias | grep <name>

# Check functions available
type <function-name>

# Test prompt (should show instantly)
exec zsh
```

## Common Issues

- **Slow startup**: Check if instant prompt is enabled, avoid synchronous commands before p10k init
- **Plugin not found**: Ensure plugin is installed via brew or oh-my-zsh custom plugins directory
- **Alias conflicts**: Use `type <name>` to check what a command resolves to
