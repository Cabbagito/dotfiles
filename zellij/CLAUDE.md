# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with this zellij configuration.

## Configuration Philosophy

This configuration uses `keybinds clear-defaults=true`, meaning ALL keybinds are explicit. Zellij ships with many default bindings, but this config discards them entirely and defines only the bindings actually used. This creates a minimal, intentional keybind surface.

## Mode System

Zellij uses a modal keybinding system. This config has selectively enabled/disabled modes:

### Active Modes
| Mode | Enter Key | Purpose |
|------|-----------|---------|
| normal | (default) | Pass-through to terminal |
| locked | `Ctrl+g` | Block all zellij keybinds |
| tab | `Ctrl+t` | Tab navigation and management |
| scroll | `Ctrl+s` | Scrollback buffer navigation |
| move | (no binding) | Move panes between positions |
| renametab | `r` in tab mode | Rename current tab |
| renamepane | (no binding) | Rename current pane |

### Disabled Modes (commented out)
- **pane**: Pane management (split, focus, close) - use tab mode instead
- **resize**: Pane resizing - not needed with current workflow
- **search**: Scrollback search - rarely used
- **session**: Session management plugin - use shell aliases instead
- **tmux**: Tmux-style bindings - not needed

## Keybind Architecture

The config uses two keybind sharing patterns:

### `shared_except`
Bindings active in all modes EXCEPT the listed ones:
```kdl
shared_except "locked" {
    bind "Ctrl g" { SwitchToMode "locked"; }  // Works everywhere except locked
}
```

### `shared_among`
Bindings active ONLY in the listed modes:
```kdl
shared_among "scroll" {
    bind "j" { ScrollDown; }  // Only works in scroll mode
}
```

### Key Mode Entry Points
- `Ctrl+g` - Toggle locked mode (blocks all zellij keybinds)
- `Ctrl+t` - Enter tab mode (tab management)
- `Ctrl+s` - Enter scroll mode (scrollback navigation)
- `Ctrl+m` - Quit zellij entirely
- `Esc` or `Enter` - Return to normal mode (from most modes)

## Layout System

Layouts define pre-configured tab and pane arrangements.

### Layout Files
| Layout | Purpose | Tabs |
|--------|---------|------|
| `claude-3.kdl` | 3 Claude instances | zsh + 3 claude tabs |
| `claude-5.kdl` | 5 Claude instances | zsh + 5 claude tabs |
| `ccc.kdl` | Minimal Claude session | single tab |
| `default.kdl` | Standard layout | basic setup |

### Layout Structure Pattern
```kdl
layout {
    default_tab_template {
        pane size=1 borderless=true {
            plugin location="file:~/.config/zellij/plugins/zjstatus.wasm" {
                // Status bar configuration
            }
        }
        children  // Placeholder for tab content
    }
    tab name="tab-name" {
        pane { /* pane config */ }
    }
}
```

### Claude Tab Pattern
Claude instances use this pattern to start Claude Code in a directory:
```kdl
tab name="claude-1" borderless=true {
    pane {
        command "zsh"
        args "-c" "cd Documents && claude --dangerously-skip-permissions; zsh"
    }
}
```
Note: `--dangerously-skip-permissions` bypasses file permission prompts for automated workflows.

## zjstatus Plugin Configuration

The status bar is customized per-layout using zjstatus options:

```kdl
plugin location="file:~/.config/zellij/plugins/zjstatus.wasm" {
    format_left   "{mode} {tabs}"
    format_right  "{datetime}"

    mode_normal  "#[fg=blue]NORMAL"
    mode_locked  "#[fg=red]LOCKED"
    mode_tab     "#[fg=magenta]TAB"
    mode_scroll  "#[fg=cyan]SCROLL"

    tab_normal   "#[fg=#6C7086]{name}"
    tab_active   "#[fg=cyan,bold]{name}"
    tab_separator "#[fg=cyan] | "

    datetime_format "%H:%M:%S"
    datetime_timezone "Europe/Vienna"
}
```

## Shell Integration

From `.zshrc`, these aliases/functions manage zellij sessions:

```bash
# zj - Kill 'giskard' session and start fresh with claude-3 layout
alias zj='zellij kill-session giskard 2>/dev/null; zellij -s giskard -l claude-3'

# zk - Kill all sessions
alias zk='zellij kill-all-sessions -y && zellij delete-all-sessions -y'

# ccc - Attach to 'ccc' session or create new with ccc layout
function ccc() {
    zellij attach ccc 2>/dev/null || zellij -s ccc -l ccc
}
```

## Modification Patterns

### Adding a New Keybind
1. Identify the mode(s) where the binding should work
2. Add the binding to that mode's block:
```kdl
tab {
    bind "KEY" { Action; SwitchToMode "normal"; }
}
```
3. Consider if `SwitchToMode "normal"` should follow the action

### Creating a New Layout
1. Create `layouts/name.kdl`
2. Include `default_tab_template` with zjstatus plugin block
3. Define tabs with pane configurations
4. Optionally add shell alias in `.zshrc`

### Enabling a Disabled Mode
1. Uncomment the mode block in `config.kdl`
2. Uncomment the `shared_except` entry that enters the mode
3. Review bindings for conflicts with active modes

### Adding Mode-Specific Scroll Bindings
Use `shared_among` for mode-specific bindings:
```kdl
shared_among "scroll" {
    bind "KEY" { Action; }
}
```

## Testing Changes

```bash
# Test a layout
zellij -l layout-name

# Test config changes (new session required)
zellij kill-session test; zellij -s test

# Verify keybinds work
# 1. Start zellij
# 2. Try Ctrl+t (tab mode), Ctrl+s (scroll mode), Ctrl+g (locked)
# 3. Test mode-specific bindings

# Check for syntax errors
zellij setup --check
```

## Key Files

- `config.kdl` - Main configuration with keybinds and settings
- `layouts/*.kdl` - Layout definitions
- `plugins/zjstatus.wasm` - Status bar plugin
- `plugins/zjframes.wasm` - Frame management plugin
