# Fastfetch Configuration

Custom system information display with a personalized layout and Japanese aesthetic.

## Display Sections

### Header
- Custom ASCII/text logo with padding
- Japanese text: **強くなりたい** ("I want to become stronger")

### System Information
- OS version and kernel
- Uptime
- Shell and terminal info

### Development Environment
- Package counts
- Editor configuration
- Terminal multiplexer

### Hardware Details
- CPU and GPU specs
- Memory usage
- Display information
- Battery status

## Custom Elements

### Styling
- **Key color**: Cyan
- **Output color**: White
- **Module prefixes**: Emoji icons for visual scanning

### Hardcoded Values
| Field | Value | Reason |
|-------|-------|--------|
| Terminal | `ghostty` | Detection unreliable in some contexts |
| Model | `MacBook Pro (14-inch, 2024)` | Cleaner display format |

## Shell Alias

```bash
ff  # → fastfetch
```

## Customization

Edit `config.jsonc` to modify:
- `logo` section for ASCII art/text changes
- `modules` array to add/remove/reorder sections
- Individual module `key` values for different emoji prefixes
- `keyColor` and `outputColor` for theme changes
