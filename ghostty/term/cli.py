#!/usr/bin/env python3
"""Command-line interface for term - terminal configuration management."""
import argparse
from .themes import ThemeManager
from .config import ConfigReader
from .shaders import ShaderManager
from .transparency import TransparencyManager
from .blur import BlurManager
from .randomization import RandomizationManager
from .presets import PresetManager
from .sync import sync_all

def main():
    parser = argparse.ArgumentParser(
        prog="term",
        description="Term - Terminal configuration manager for Ghostty",
        epilog="Run without arguments to see all current settings"
    )
    
    # Create subparsers
    subparsers = parser.add_subparsers(dest="command", help="Commands")
    
    # Theme command
    theme_parser = subparsers.add_parser(
        "theme", 
        help="Manage terminal color themes",
        description="Control Ghostty color themes - view favorites, list all, or switch themes"
    )
    theme_parser.add_argument(
        "action", 
        nargs="?",
        choices=["list", "set", "random", "random-all", "add", "remove"],
        help="Action: list (all themes), set (specific theme), random (favorite), random-all (any theme), add (to favorites), remove (from favorites)"
    )
    theme_parser.add_argument(
        "theme_name",
        nargs="?",
        help="Theme name for 'set' action (e.g., 'cyberpunk', 'nord')"
    )
    
    # Shader command
    shader_parser = subparsers.add_parser(
        "shader", 
        help="Manage visual effect shaders",
        description="Control Ghostty shaders - toggle visual effects on/off. Multiple shaders can be active simultaneously."
    )
    shader_parser.add_argument(
        "action",
        nargs="?",
        choices=["toggle"],
        help="Action to perform: toggle (turn shader on/off). Default: show all shaders with status"
    )
    shader_parser.add_argument(
        "shader_name",
        nargs="?",
        help="Shader ID or partial name to toggle (e.g., 'crt', 'bloom', 'matrix')"
    )
    
    # Transparency command
    transparency_parser = subparsers.add_parser(
        "transparency",
        help="Set window transparency level",
        description="Control Ghostty window transparency with preset values"
    )
    transparency_parser.add_argument(
        "preset",
        nargs="?",
        choices=["none", "low", "medium", "high", "full"],
        help="Transparency preset: none (opaque), low, medium, high, full (most transparent)"
    )
    
    # Blur command
    blur_parser = subparsers.add_parser(
        "blur",
        help="Set background blur intensity",
        description="Control Ghostty background blur effect with preset values"
    )
    blur_parser.add_argument(
        "preset",
        nargs="?",
        choices=["off", "low", "medium", "high"],
        help="Blur preset: off (no blur), low, medium, high (maximum blur)"
    )
    
    # Random command
    random_parser = subparsers.add_parser(
        "random",
        help="Apply random theme, blur, and transparency settings",
        description="Randomly select a favorite theme, blur preset, and transparency preset"
    )
    
    # Random-all command
    random_all_parser = subparsers.add_parser(
        "random-all",
        help="Apply random theme from all themes, blur, and transparency settings",
        description="Randomly select any theme (not just favorites), blur preset, and transparency preset"
    )
    
    # Preset command
    preset_parser = subparsers.add_parser(
        "preset",
        help="Manage configuration presets",
        description="Save and apply preset combinations of theme, blur, and transparency settings"
    )
    preset_parser.add_argument(
        "action",
        nargs="?",
        help="Preset name/number to apply, or action: add, list, remove, set"
    )
    preset_parser.add_argument(
        "preset_name",
        nargs="?",
        help="Preset name for add/remove/set actions"
    )
    
    args = parser.parse_args()
    
    # No command - show all settings
    if not args.command:
        config = ConfigReader()
        print(config.get_display_info())
    
    # Theme command
    elif args.command == "theme":
        tm = ThemeManager()
        
        if not args.action:  # Just 'gc theme' - show favorites
            print(tm.show_info())
        elif args.action == "list":
            print(tm.show_all())
        elif args.action == "set":
            if not args.theme_name:
                print("Error: theme name required for 'set' action")
            else:
                try:
                    tm.set_active(args.theme_name)
                    print(f"→ {args.theme_name}")
                except ValueError as e:
                    print(f"Error: {e}")
        elif args.action == "random":
            new_theme = tm.random_favorite()
            if new_theme:
                print(f"→ {new_theme}")
            else:
                print("No favorite themes available")
        elif args.action == "random-all":
            new_theme = tm.random_all()
            if new_theme:
                print(f"→ {new_theme}")
            else:
                print("No themes available")
        elif args.action == "add":
            try:
                theme = tm.add_to_favorites()
                print(f"Added '{theme}' to favorites")
            except ValueError as e:
                print(f"Error: {e}")
        elif args.action == "remove":
            try:
                theme = tm.remove_from_favorites()
                print(f"Removed '{theme}' from favorites")
            except ValueError as e:
                print(f"Error: {e}")
    
    # Shader command
    elif args.command == "shader":
        sm = ShaderManager()
        
        if not args.action:  # Just 'gc shader' - show list
            print(sm.show_info())
        elif args.action == "toggle":
            if not args.shader_name:
                print("Error: shader name required for 'toggle' action")
            else:
                try:
                    shader_name, is_on = sm.toggle(args.shader_name)
                    status = "ON" if is_on else "OFF"
                    print(f"Toggled: {shader_name} - {status}")
                except ValueError as e:
                    print(f"Error: {e}")
    
    # Transparency command
    elif args.command == "transparency":
        tm = TransparencyManager("/Users/peki/.config/ghostty/config")
        
        if not args.preset:  # Just 'gc transparency' - show current
            tm.display_current()
        else:
            if tm.set_transparency(args.preset):
                print(f"→ transparency: {args.preset}")
            else:
                print(f"Error: Invalid preset '{args.preset}'")
    
    # Blur command
    elif args.command == "blur":
        bm = BlurManager("/Users/peki/.config/ghostty/config")
        
        if not args.preset:  # Just 'gc blur' - show current
            bm.display_current()
        else:
            if bm.set_blur(args.preset):
                print(f"→ blur: {args.preset}")
            else:
                print(f"Error: Invalid preset '{args.preset}'")
    
    # Random command
    elif args.command == "random":
        rm = RandomizationManager("/Users/peki/.config/ghostty/config")
        result = rm.random_settings()
        print(result)
    
    # Random-all command
    elif args.command == "random-all":
        rm = RandomizationManager("/Users/peki/.config/ghostty/config")
        result = rm.random_all_settings()
        print(result)
    
    # Preset command
    elif args.command == "preset":
        pm = PresetManager("/Users/peki/.config/ghostty/config")
        
        if not args.action:  # Just 'gc preset' - show list
            print(pm.list_presets())
        elif args.action == "list":
            print(pm.list_presets())
        elif args.action == "add":
            if not args.preset_name:
                print("Error: preset name required for 'add' action")
            else:
                success, message = pm.add_preset(args.preset_name)
                print(message)
        elif args.action == "remove":
            if not args.preset_name:
                print("Error: preset name required for 'remove' action")
            else:
                success, message = pm.remove_preset(args.preset_name)
                print(message)
        elif args.action == "set":
            if not args.preset_name:
                print("Error: preset name required for 'set' action")
            else:
                success, result = pm.apply_preset(args.preset_name)
                if success:
                    print(result)
                else:
                    print(f"Error: {result}")
        else:
            # args.action is the preset name/number to apply
            success, result = pm.apply_preset(args.action)
            if success:
                print(result)
            else:
                print(f"Error: {result}")
    
    # Always sync at the end (even for read-only commands)
    sync_all()

if __name__ == "__main__":
    main()