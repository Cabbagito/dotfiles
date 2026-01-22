"""Ghostty configuration reload functionality."""
import subprocess
import time
import platform


class GhosttyReload:
    """Handles reloading Ghostty configuration."""
    
    @staticmethod
    def reload_config():
        """Reload Ghostty configuration by sending CMD+SHIFT+comma keystroke."""
        # Only works on macOS
        if platform.system() != 'Darwin':
            return
        
        try:
            # AppleScript to activate Ghostty and send reload keystroke
            applescript = '''
            tell application "Ghostty"
                activate
            end tell
            
            delay 0.1
            
            tell application "System Events"
                keystroke "," using {command down, shift down}
            end tell
            '''
            
            # Execute the AppleScript
            subprocess.run(
                ['osascript', '-e', applescript],
                capture_output=True,
                text=True
            )
            
        except Exception:
            # Silently ignore errors (Ghostty not running, permissions, etc.)
            pass