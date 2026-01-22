# Term - Terminal Configuration Manager for Ghostty

A clean CLI tool for managing Ghostty terminal themes, shaders, and visual settings.

## Features

- **Theme Management**: Browse and switch between 394 themes (41 favorites)
- **Shader Support**: Toggle visual effect shaders on/off
- **Transparency & Blur**: Quick presets for window transparency and blur effects
- **Randomization**: Random theme, blur, and transparency combinations
- **Preset System**: Save and load custom configuration combinations
- **Auto-sync**: Automatically syncs theme changes to running Neovim instances
- **Live Reload**: Ghostty configuration reloads automatically on theme changes

## Installation

```bash
cd /Users/peki/.config/ghostty
uv venv
uv pip install -e .
```

### Dependencies

- `pynvim` - For Neovim integration (optional, auto-detects if available)

## Usage

Run with UV:
```bash
uv run term
```

### Commands

- `term` - Show all current settings
- `term theme` - Show favorite themes
- `term theme list` - List all themes
- `term theme set <name>` - Set specific theme
- `term shader` - List shaders with status
- `term shader toggle <name>` - Toggle shader on/off
- `term transparency <preset>` - Set transparency level
- `term blur <preset>` - Set blur intensity
- `term random` - Apply random settings
- `term preset` - Manage configuration presets

## Examples

```bash
# Set a theme
uv run term theme set cyberpunk

# Toggle a shader
uv run term shader toggle crt-classic

# Apply random settings
uv run term random

# Save current config as preset
uv run term preset add dark

# Load a preset
uv run term preset dark
```