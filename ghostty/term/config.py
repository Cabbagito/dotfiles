"""Configuration reader for ghostty settings."""
from .utils import read_config
from .transparency import TransparencyManager
from .blur import BlurManager

class ConfigReader:
    """Reads and displays ghostty configuration settings."""
    
    def __init__(self):
        self.settings = self._parse_config()
        self.transparency_manager = TransparencyManager("/Users/peki/.config/ghostty/config")
        self.blur_manager = BlurManager("/Users/peki/.config/ghostty/config")
    
    def _parse_config(self):
        """Parse config file and extract key settings."""
        lines = read_config()
        settings = {}
        
        for line in lines:
            line = line.strip()
            # Skip comments and empty lines
            if not line or line.startswith('#'):
                continue
            
            # Parse key = value pairs
            if '=' in line:
                key, value = line.split('=', 1)
                key = key.strip()
                value = value.strip()
                settings[key] = value
        
        return settings
    
    def get_display_info(self):
        """Get formatted display of current settings."""
        info = ["Current Ghostty Settings:"]
        info.append("")
        
        # Theme
        theme = self.settings.get('theme', 'None')
        info.append(f"Theme: {theme}")
        
        # Font
        font_family = self.settings.get('font-family', 'Default')
        font_size = self.settings.get('font-size', 'Default')
        info.append(f"Font: {font_family} @ {font_size}pt")
        
        # Window
        title = self.settings.get('title', 'Default')
        info.append(f"Window Title: {title}")
        
        # Transparency and Blur with descriptors
        transparency_value = self.transparency_manager.get_current()
        blur_value = self.blur_manager.get_current()
        
        # Get descriptors or fall back to numeric values
        if transparency_value is not None:
            transparency_desc = self.transparency_manager.get_preset_name(transparency_value)
            transparency_display = transparency_desc if transparency_desc else str(transparency_value)
        else:
            transparency_display = "none"
        
        if blur_value is not None:
            blur_desc = self.blur_manager.get_preset_name(blur_value)
            blur_display = blur_desc if blur_desc else str(blur_value)
        else:
            blur_display = "off"
        
        info.append(f"Transparency: {transparency_display}, Blur: {blur_display}")
        
        # Other notable settings
        if 'custom-shader' in self.settings:
            shader = self.settings['custom-shader'].split('/')[-1]
            info.append(f"Shader: {shader}")
        
        return "\n".join(info)