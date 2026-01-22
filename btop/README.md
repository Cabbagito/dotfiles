# btop Configuration

Resource monitor with vim-style navigation and transparent Dracula theme.

## Key Customizations

- **Theme**: Dracula with transparent background (`theme_background = False`)
- **Update interval**: 500ms for responsive monitoring
- **Graph style**: Braille characters for detailed visualizations
- **Default sort**: Processes sorted by memory usage
- **Visible boxes**: CPU, memory, network, and processes
- **Extras enabled**: Uptime display, CPU wattage, temperature monitoring
- **UI**: Rounded corners enabled

## Vim Keybindings

Vim keys are enabled (`vim_keys = True`). Navigation uses hjkl, but note these conflicts require Shift:

| Key | Default Action | Vim Conflict |
|-----|----------------|--------------|
| `H` | Help | h = left |
| `K` | Kill process | k = up |

Use Shift+H for help and Shift+K to kill processes.

## Navigation Quick Reference

- `hjkl` - Navigate
- `Enter` - Select/expand
- `f` - Filter processes
- `s` - Sort options
- `q` - Quit

## Files

| File | Purpose |
|------|---------|
| `btop.conf` | Main configuration |
| `themes/` | Custom theme files |
| `dracula.theme` | Active color theme |
