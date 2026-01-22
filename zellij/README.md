# Zellij Configuration

Terminal multiplexer configuration with custom layouts for Claude Code development.

## Layouts

### claude-3
Multi-tab layout with three Claude Code instances:
- Tab 1: Shell with fastfetch on startup
- Tabs 2-4: Claude Code instances in `~/Documents` with `--dangerously-skip-permissions`

```bash
zellij -l claude-3
```

### claude-5
Extended layout with five Claude Code instances for parallel agentic work.

```bash
zellij -l claude-5
```

### ccc
Minimal single-tab layout for quick Claude sessions. Use with the `ccc` shell function which attaches to existing session or creates new:

```bash
ccc  # Defined in .zshrc - attaches or creates 'ccc' session
```

### default
Standard layout without pre-configured tabs.

## Plugins

### zjstatus
Custom status bar plugin providing:
- Mode indicator (normal/locked/tab/scroll)
- Tab names with active highlighting
- Date/time display

Location: `plugins/zjstatus.wasm`

### zjframes
Frame management plugin.

Location: `plugins/zjframes.wasm`

## Keybindings

Keybindings use `clear-defaults=true` - only explicit bindings work.

### Mode Switching
| Key | Action |
|-----|--------|
| `Ctrl+g` | Toggle locked mode |
| `Ctrl+t` | Tab mode |
| `Ctrl+s` | Scroll mode |
| `Ctrl+m` | Quit zellij |

### Tab Mode (`Ctrl+t`)
| Key | Action |
|-----|--------|
| `h/l` or arrows | Navigate tabs |
| `H/L` | Move tab left/right |
| `1-9` | Go to tab N |
| `t` | Go to tab 1 |
| `n` | New tab |
| `x` | Close tab |
| `r` | Rename tab |
| `d` | Detach |
| `[/]` | Break pane left/right |

### Scroll Mode (`Ctrl+s`)
| Key | Action |
|-----|--------|
| `j/k` | Scroll down/up |
| `d/u` | Half page down/up |
| `Ctrl+f/b` | Full page down/up |
| `Ctrl+c` | Exit to bottom |

### Move Mode
| Key | Action |
|-----|--------|
| `h/j/k/l` | Move pane in direction |
| `n` | Move pane forward |
| `p` | Move pane backward |

## Quick Session Management

Shell aliases/functions from `.zshrc`:

```bash
# Kill and recreate main session
zj      # Kills 'giskard' session and starts fresh

# Kill all sessions
zk      # zellij kill-all-sessions -y && delete-all-sessions -y

# Claude quick session
ccc     # Attaches to 'ccc' or creates with ccc layout
```

## Ideas & Future Enhancements

From `zellij_ideas.md`:

- **Default ghostty command spawns zellij**: Make zellij the default terminal experience
- **Multiple Claude instances**: `zj -c 3` to launch with N claude instances
- **Random theme on launch**: Integrate with `term random` for variety
- **Quick Claude popup**: Tab-mode shortcut to spawn Claude in specific directory

## Configuration Notes

- **Default mode**: normal (not locked)
- **Pane frames**: Disabled in layouts for cleaner look
- **Status bar**: 1 row at top using zjstatus
- **Kitty keyboard protocol**: Supported

## File Structure

```
zellij/
├── config.kdl          # Main configuration
├── layouts/
│   ├── claude-3.kdl    # 3 Claude instances
│   ├── claude-5.kdl    # 5 Claude instances
│   ├── ccc.kdl         # Minimal Claude layout
│   └── default.kdl     # Standard layout
└── plugins/
    ├── zjstatus.wasm   # Status bar
    └── zjframes.wasm   # Frame management
```
