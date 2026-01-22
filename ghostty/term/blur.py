"""Blur management for Ghostty configuration."""

from typing import Optional, Dict
from term.utils import read_config, write_config


class BlurManager:
    """Manages blur (background-blur-radius) settings."""
    
    PRESETS: Dict[str, int] = {
        'off': 0,
        'low': 21,
        'medium': 42,
        'high': 69
    }
    
    def __init__(self, config_path: str):
        self.config_path = config_path
    
    def get_current(self) -> Optional[int]:
        """Get current blur value from config."""
        lines = read_config()
        
        for line in lines:
            line = line.strip()
            if line.startswith('background-blur-radius'):
                if '=' in line:
                    value_str = line.split('=', 1)[1].strip()
                    try:
                        return int(value_str)
                    except ValueError:
                        return None
        
        return None
    
    def get_preset_name(self, value: int) -> Optional[str]:
        """Get preset name for a given value."""
        for name, preset_value in self.PRESETS.items():
            if preset_value == value:
                return name
        return None
    
    def set_blur(self, preset: str) -> bool:
        """Set blur to a preset value."""
        if preset not in self.PRESETS:
            return False
        
        new_value = self.PRESETS[preset]
        lines = read_config()
        
        # Find and replace existing background-blur-radius line
        found = False
        for i, line in enumerate(lines):
            if line.strip().startswith('background-blur-radius'):
                lines[i] = f'background-blur-radius = {new_value}\n'
                found = True
                break
        
        # If not found, append at the end
        if not found:
            lines.append(f'background-blur-radius = {new_value}\n')
        
        write_config(lines)
        return True
    
    def display_current(self) -> None:
        """Display current blur setting."""
        current = self.get_current()
        
        if current is None:
            print("Current blur: off")
            return
        
        preset = self.get_preset_name(current)
        if preset:
            print(f"Current blur: {preset}")
        else:
            print(f"Current blur: {current} (custom)")