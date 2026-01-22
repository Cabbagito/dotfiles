"""Transparency management for Ghostty configuration."""

from typing import Optional, Dict
from term.utils import read_config, write_config


class TransparencyManager:
    """Manages transparency (background-opacity) settings."""
    
    PRESETS: Dict[str, float] = {
        'none': 1.0,
        'low': 0.95,
        'medium': 0.85,
        'high': 0.75,
        'full': 0.65
    }
    
    def __init__(self, config_path: str):
        self.config_path = config_path
    
    def get_current(self) -> Optional[float]:
        """Get current transparency value from config."""
        lines = read_config()
        
        for line in lines:
            line = line.strip()
            if line.startswith('background-opacity'):
                if '=' in line:
                    value_str = line.split('=', 1)[1].strip()
                    try:
                        return float(value_str)
                    except ValueError:
                        return None
        
        return None
    
    def get_preset_name(self, value: float) -> Optional[str]:
        """Get preset name for a given value."""
        for name, preset_value in self.PRESETS.items():
            if abs(preset_value - value) < 0.001:  # Float comparison tolerance
                return name
        return None
    
    def set_transparency(self, preset: str) -> bool:
        """Set transparency to a preset value."""
        if preset not in self.PRESETS:
            return False
        
        new_value = self.PRESETS[preset]
        lines = read_config()
        
        # Find and replace existing background-opacity line
        found = False
        for i, line in enumerate(lines):
            if line.strip().startswith('background-opacity'):
                lines[i] = f'background-opacity={new_value}\n'
                found = True
                break
        
        # If not found, append at the end
        if not found:
            lines.append(f'background-opacity={new_value}\n')
        
        write_config(lines)
        return True
    
    def display_current(self) -> None:
        """Display current transparency setting."""
        current = self.get_current()
        
        if current is None:
            print("Current transparency: none")
            return
        
        preset = self.get_preset_name(current)
        if preset:
            print(f"Current transparency: {preset}")
        else:
            print(f"Current transparency: {current} (custom)")