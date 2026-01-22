"""Shared utilities for ghostty configuration management."""
import json
from pathlib import Path
from .neovim_sync import NeovimSync
from .ghostty_reload import GhosttyReload

CONFIG_FILE = Path("/Users/peki/.config/ghostty/config")
DATA_DIR = Path(__file__).parent / "data"
THEMES_JSON = DATA_DIR / "themes.json"
SHADERS_JSON = DATA_DIR / "shaders.json"
PRESETS_JSON = DATA_DIR / "presets.json"

def load_json(filepath):
    """Load JSON data from file."""
    with open(filepath, 'r') as f:
        return json.load(f)

def read_config():
    """Read ghostty config file lines."""
    with open(CONFIG_FILE, 'r') as f:
        return f.readlines()

def write_config(lines):
    """Write lines to ghostty config file."""
    with open(CONFIG_FILE, 'w') as f:
        f.writelines(lines)

def save_json(filepath, data):
    """Save data to JSON file."""
    with open(filepath, 'w') as f:
        json.dump(data, f, indent=2)

def set_theme_in_config(theme_name):
    """Set the active theme in config file."""
    lines = read_config()
    theme_line = f"theme = {theme_name}\n"
    theme_found = False
    
    # Replace existing theme line
    for i, line in enumerate(lines):
        if line.strip().startswith("theme = "):
            lines[i] = theme_line
            theme_found = True
            break
    
    # If no theme line found, append at end
    if not theme_found:
        # Add blank line if last line isn't empty
        if lines and lines[-1].strip():
            lines.append("\n")
        lines.append(theme_line)
    
    write_config(lines)