"""Randomization management for Ghostty configuration."""
import random
from .themes import ThemeManager
from .transparency import TransparencyManager
from .blur import BlurManager


class RandomizationManager:
    """Manages randomization of themes, blur, and transparency settings."""
    
    def __init__(self, config_path: str):
        self.config_path = config_path
        self.theme_manager = ThemeManager()
        self.transparency_manager = TransparencyManager(config_path)
        self.blur_manager = BlurManager(config_path)
    
    def random_settings(self):
        """Apply random theme, blur, and transparency settings."""
        results = []
        
        # Random theme from favorites
        new_theme = self.theme_manager.random_favorite()
        if new_theme:
            results.append(f"→ theme: {new_theme}")
        
        # Random transparency
        transparency_presets = list(self.transparency_manager.PRESETS.keys())
        transparency_choice = random.choice(transparency_presets)
        if self.transparency_manager.set_transparency(transparency_choice):
            results.append(f"→ transparency: {transparency_choice}")
        
        # Random blur
        blur_presets = list(self.blur_manager.PRESETS.keys())
        blur_choice = random.choice(blur_presets)
        if self.blur_manager.set_blur(blur_choice):
            results.append(f"→ blur: {blur_choice}")
        
        return "\n".join(results)
    
    def random_all_settings(self):
        """Apply random theme from all themes, blur, and transparency settings."""
        results = []
        
        # Random theme from all themes
        new_theme = self.theme_manager.random_all()
        if new_theme:
            results.append(f"→ theme: {new_theme}")
        
        # Random transparency
        transparency_presets = list(self.transparency_manager.PRESETS.keys())
        transparency_choice = random.choice(transparency_presets)
        if self.transparency_manager.set_transparency(transparency_choice):
            results.append(f"→ transparency: {transparency_choice}")
        
        # Random blur
        blur_presets = list(self.blur_manager.PRESETS.keys())
        blur_choice = random.choice(blur_presets)
        if self.blur_manager.set_blur(blur_choice):
            results.append(f"→ blur: {blur_choice}")
        
        return "\n".join(results)