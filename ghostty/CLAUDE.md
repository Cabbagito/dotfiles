# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Project Overview

Term is a terminal configuration manager for Ghostty that provides a clean CLI interface for managing themes and settings. The tool offers easy theme switching between 394 themes, with 41 hand-picked favorites for quick access.

## Architecture

### Data Flow
1. **Current settings**: Read directly from `/Users/peki/.config/ghostty/config` file
2. **Theme lists**: Stored in `term/data/themes.json` with "favorites" and "all" lists
3. **Shader catalog**: Stored in `term/data/shaders.json` as a read-only reference
4. **Active shaders**: Read from config file (any `custom-shader = X` lines)

### Key Design Decisions
- The ghostty config file is the single source of truth for ALL active settings
- themes.json contains two lists: favorites (41 curated themes) and all (394 total themes)
- shaders.json is a read-only catalog - no user preferences stored
- Config modifications append to end of file (shaders) or replace in-place (themes)
- No dependency on comment markers or specific config order

## Running the Tool

```bash
# Create virtual environment (first time only)
cd /Users/peki/.config/ghostty
uv venv
uv pip install -e .

# Run with UV
uv run term

# Or add to .zshrc for global alias
alias term='cd /Users/peki/.config/ghostty && uv run term'
```

## Command Structure

```bash
term                    # Show all settings
term theme             # Show favorites and current theme
term theme list        # List all 394 themes
term theme set <name>  # Set specific theme
term theme random       # Random theme from favorites
term theme random-all  # Random theme from all themes

term shader            # List all shaders with on/off status
term shader toggle <name>  # Toggle shader on/off

term transparency      # Show current transparency
term transparency <preset>  # Set transparency: none, low, medium, high, full

term blur              # Show current blur
term blur <preset>     # Set blur: off, low, medium, high

term random            # Apply random theme, blur, and transparency
term preset            # List saved presets
term preset <name>     # Apply preset by name or number
term preset add <name> # Save current settings as preset
```

## Core Components

- `cli.py`: Command-line interface using argparse
- `themes.py`: ThemeManager class - handles theme operations
- `shaders.py`: ShaderManager class - handles shader operations
- `transparency.py`: TransparencyManager class - handles transparency presets
- `blur.py`: BlurManager class - handles blur presets
- `config.py`: ConfigReader class - reads and displays settings
- `presets.py`: PresetManager class - handles saving/loading preset configurations
- `randomization.py`: RandomizationManager class - handles random settings
- `neovim_sync.py`: NeovimSync class - syncs colorscheme changes to Neovim instances
- `ghostty_reload.py`: GhosttyReload class - triggers Ghostty config reload
- `utils.py`: File I/O utilities for config and JSON
- `data/themes.json`: Contains favorites list (41 themes) and all themes list (394 themes)
- `data/shaders.json`: Catalog of available shaders with metadata
- `data/presets.json`: User-saved preset configurations

## Theme Management Logic

When switching themes:
1. Find existing `theme = X` line and replace with `theme = Y`
2. If no theme line exists, append to end of config
3. themes.json is read-only - no modifications needed
4. Ghostty configuration is automatically reloaded (macOS only)
5. All running Neovim instances receive :SyncColorscheme command

## Shader Management Logic

Shaders work differently from themes:
1. Multiple shaders can be active simultaneously
2. Toggle ON: Appends `custom-shader = X` line to end of config
3. Toggle OFF: Removes the shader line entirely from config
4. shaders.json is a read-only catalog with metadata
5. No commented shader lines kept in config - only active ones

## Future Extensions

The modular structure supports adding:
- `term font [family|size]` - Font configuration
- Additional shader actions (add favorites, etc.)

## Current Features

### Theme Management
- Browse and switch between 394 total themes
- Quick access to 41 favorite themes
- Random theme selection (from favorites or all)
- Clean display of themes in two-column format

### Shader Support
- Toggle multiple shaders on/off simultaneously
- Shaders stored in `shaders/` with hackr-sh and zoitrok collections
- Each shader can be independently enabled/disabled

### Transparency & Blur
- Transparency presets: none (1.0), low (0.95), medium (0.85), high (0.75), full (0.65)
- Blur presets: off (0), low (21), medium (42), high (69)
- All displays show descriptor values (e.g., "low", "medium") instead of numeric values
- Custom values show as numeric with "(custom)" indicator

### Preset System
- Save current theme, transparency, and blur settings as named presets
- Apply presets by name or number
- List and manage saved presets

### Randomization
- Apply random theme from favorites, random blur, and random transparency
- Great for discovering new combinations

## Auto-sync Implementation

### Neovim Integration
- Uses `pynvim` to communicate with running Neovim instances
- Finds Neovim sockets in various locations (/tmp, /var/folders, etc.)
- Sends `:SyncColorscheme` command after theme changes
- Gracefully handles missing instances or connection errors

### Ghostty Reload
- Uses AppleScript on macOS to send CMD+SHIFT+comma keystroke
- Activates Ghostty first, then sends reload command
- Works only on macOS (silently skips on other platforms)

## Development Notes

- Always test theme switching updates config file correctly
- themes.json is now a static list of favorites and all themes (read-only)
- Config file no longer requires comment markers - works with any organization
- Config modifications are minimal - only change what's necessary
- The system is resilient to config file reorganization
- Theme curation is complete - no add/remove functionality needed
- Neovim sync requires `pynvim` package (optional dependency)
- Ghostty reload only works on macOS with accessibility permissions
- Display values use descriptors (e.g., "low", "medium") instead of raw numeric values for better UX