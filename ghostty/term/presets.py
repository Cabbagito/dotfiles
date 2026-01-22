"""Preset management for Ghostty configuration."""
from .utils import load_json, save_json, PRESETS_JSON
from .themes import ThemeManager
from .transparency import TransparencyManager
from .blur import BlurManager
from .shaders import ShaderManager


class PresetManager:
    """Manages configuration presets for themes, blur, and transparency."""
    
    def __init__(self, config_path: str):
        self.config_path = config_path
        self.theme_manager = ThemeManager()
        self.transparency_manager = TransparencyManager(config_path)
        self.blur_manager = BlurManager(config_path)
        self.shader_manager = ShaderManager()
        self.reload()
    
    def reload(self):
        """Reload presets from JSON file."""
        try:
            data = load_json(PRESETS_JSON)
            self.presets = data.get("presets", {})
        except FileNotFoundError:
            self.presets = {}
    
    def save(self):
        """Save presets to JSON file."""
        save_json(PRESETS_JSON, {"presets": self.presets})
    
    def add_preset(self, name: str):
        """Add current settings as a new preset."""
        # Get current values
        theme = self.theme_manager.get_current()
        transparency = self.transparency_manager.get_current()
        blur = self.blur_manager.get_current()
        
        if not theme:
            return False, "No theme found in current configuration"
        
        # Convert transparency value to preset name
        transparency_preset = None
        if transparency is not None:
            transparency_preset = self.transparency_manager.get_preset_name(transparency)
            if not transparency_preset:
                transparency_preset = str(transparency)  # Use custom value
        
        # Convert blur value to preset name
        blur_preset = None
        if blur is not None:
            blur_preset = self.blur_manager.get_preset_name(blur)
            if not blur_preset:
                blur_preset = str(blur)  # Use custom value
        
        # Save preset
        self.presets[name] = {
            "theme": theme,
            "transparency": transparency_preset,
            "blur": blur_preset
        }
        
        self.save()
        return True, f"Saved preset '{name}'"
    
    def apply_preset(self, name: str):
        """Apply a saved preset."""
        if name not in self.presets:
            # Try to match by number if numeric
            if name.isdigit():
                preset_list = list(self.presets.keys())
                index = int(name) - 1
                if 0 <= index < len(preset_list):
                    name = preset_list[index]
                else:
                    return False, f"Preset {name} not found"
            else:
                return False, f"Preset '{name}' not found"
        
        preset = self.presets[name]
        results = []
        
        # Apply theme
        if "theme" in preset:
            try:
                self.theme_manager.set_active(preset["theme"])
                results.append(f"→ theme: {preset['theme']}")
            except ValueError as e:
                results.append(f"Error setting theme: {e}")
        
        # Apply transparency
        if "transparency" in preset and preset["transparency"]:
            # Check if it's a preset name or custom value
            if preset["transparency"] in self.transparency_manager.PRESETS:
                if self.transparency_manager.set_transparency(preset["transparency"]):
                    results.append(f"→ transparency: {preset['transparency']}")
            else:
                # Handle custom value
                try:
                    value = float(preset["transparency"])
                    from .utils import read_config, write_config
                    lines = read_config()
                    found = False
                    for i, line in enumerate(lines):
                        if line.strip().startswith('background-opacity'):
                            lines[i] = f'background-opacity={value}\n'
                            found = True
                            break
                    if not found:
                        lines.append(f'background-opacity={value}\n')
                    write_config(lines)
                    results.append(f"→ transparency: {value} (custom)")
                except ValueError:
                    results.append(f"Error: Invalid transparency value")
        
        # Apply blur
        if "blur" in preset and preset["blur"]:
            # Check if it's a preset name or custom value
            if preset["blur"] in self.blur_manager.PRESETS:
                if self.blur_manager.set_blur(preset["blur"]):
                    results.append(f"→ blur: {preset['blur']}")
            else:
                # Handle custom value
                try:
                    value = int(preset["blur"])
                    from .utils import read_config, write_config
                    lines = read_config()
                    found = False
                    for i, line in enumerate(lines):
                        if line.strip().startswith('background-blur-radius'):
                            lines[i] = f'background-blur-radius = {value}\n'
                            found = True
                            break
                    if not found:
                        lines.append(f'background-blur-radius = {value}\n')
                    write_config(lines)
                    results.append(f"→ blur: {value} (custom)")
                except ValueError:
                    results.append(f"Error: Invalid blur value")
        
        return True, "\n".join(results)
    
    def list_presets(self):
        """List all saved presets."""
        if not self.presets:
            return "No presets saved"
        
        lines = ["Presets:"]
        for i, (name, preset) in enumerate(self.presets.items(), 1):
            theme = preset.get("theme", "none")
            transparency = preset.get("transparency", "none")
            blur = preset.get("blur", "none")
            lines.append(f"{i}. {name}: theme={theme}, transparency={transparency}, blur={blur}")
        
        return "\n".join(lines)
    
    def remove_preset(self, name: str):
        """Remove a preset."""
        if name not in self.presets:
            # Try to match by number if numeric
            if name.isdigit():
                preset_list = list(self.presets.keys())
                index = int(name) - 1
                if 0 <= index < len(preset_list):
                    name = preset_list[index]
                else:
                    return False, f"Preset {name} not found"
            else:
                return False, f"Preset '{name}' not found"
        
        del self.presets[name]
        self.save()
        return True, f"Removed preset '{name}'"