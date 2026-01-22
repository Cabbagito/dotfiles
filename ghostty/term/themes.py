"""Theme management for ghostty configuration."""
import random
from .utils import load_json, save_json, THEMES_JSON, set_theme_in_config

class ThemeManager:
    def __init__(self):
        self.reload()
    
    def reload(self):
        """Reload themes from JSON file."""
        data = load_json(THEMES_JSON)
        self.favorites = data.get("favorites", [])
        self.all_themes = data.get("all", [])
    
    def get_current(self):
        """Get current active theme name from config file."""
        from .utils import read_config
        lines = read_config()
        for line in lines:
            line = line.strip()
            if line.startswith("theme = ") and not line.startswith("#"):
                return line.split("=", 1)[1].strip()
        return None
    
    def set_active(self, theme_name):
        """Set a theme as active."""
        if theme_name not in self.all_themes:
            raise ValueError(f"Theme '{theme_name}' not found")
        
        set_theme_in_config(theme_name)
    
    def random_favorite(self):
        """Switch to a random favorite theme."""
        current = self.get_current()
        available = [t for t in self.favorites if t != current]
        
        if not available:
            return None
        
        new_theme = random.choice(available)
        self.set_active(new_theme)
        return new_theme
    
    def random_all(self):
        """Switch to a random theme from all themes."""
        current = self.get_current()
        available = [t for t in self.all_themes if t != current]
        
        if not available:
            return None
        
        new_theme = random.choice(available)
        self.set_active(new_theme)
        return new_theme
    
    def show_info(self):
        """Return formatted info about current theme and favorites."""
        current = self.get_current()
        
        info = [f"Current: {current or 'None'}"]
        info.append(f"\nFavorites ({len(self.favorites)}):")  
        
        # Show favorites in columns
        for i in range(0, len(self.favorites), 2):
            if i + 1 < len(self.favorites):
                info.append(f"  {self.favorites[i]:<30} {self.favorites[i+1]}")
            else:
                info.append(f"  {self.favorites[i]}")
        
        return "\n".join(info)
    
    def show_all(self):
        """Return formatted list of all themes."""
        current = self.get_current()
        
        info = [f"Current: {current or 'None'}"]
        info.append(f"\nAll themes ({len(self.all_themes)}):")  
        
        # Show themes in columns
        for i in range(0, len(self.all_themes), 2):
            if i + 1 < len(self.all_themes):
                info.append(f"  {self.all_themes[i]:<30} {self.all_themes[i+1]}")
            else:
                info.append(f"  {self.all_themes[i]}")
        
        return "\n".join(info)
    
    def add_to_favorites(self):
        """Add current theme to favorites."""
        current = self.get_current()
        if not current:
            raise ValueError("No theme currently set")
        
        if current in self.favorites:
            raise ValueError(f"Theme '{current}' is already in favorites")
        
        if current not in self.all_themes:
            raise ValueError(f"Theme '{current}' not found in theme list")
        
        # Add to favorites and save
        self.favorites.append(current)
        self.favorites.sort()  # Keep alphabetical order
        self._save_themes()
        return current
    
    def remove_from_favorites(self):
        """Remove current theme from favorites."""
        current = self.get_current()
        if not current:
            raise ValueError("No theme currently set")
        
        if current not in self.favorites:
            raise ValueError(f"Theme '{current}' is not in favorites")
        
        # Remove from favorites and save
        self.favorites.remove(current)
        self._save_themes()
        return current
    
    def _save_themes(self):
        """Save themes data back to JSON file."""
        data = {
            "favorites": self.favorites,
            "all": self.all_themes
        }
        save_json(THEMES_JSON, data)