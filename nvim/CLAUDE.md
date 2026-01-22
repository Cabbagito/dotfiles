# Neovim Configuration Notes for AI Assistants

## Structure
- **Modern modular** configuration using lazy.nvim
- Plugins organized by category in `lua/plugins/`
- Core config in `lua/config/`

## Key Features
- Leader key: `<space>`
- Formatting: `<space>fm` (LSP commands use `<space>` directly, not `<leader>`)
- Terminal: `<space>T<space>T` (custom floating terminal)
- File navigation: Oil.nvim with `-` key
- NO nvim-tree (removed intentionally)
- NO autoclose (disabled)
- NO virtual edit commands

## Important Notes
- Using Mason v2 with Neovim 0.11.2
- Notifications are suppressed except errors
- Catppuccin theme with transparent background
- Custom terminal implementation as a plugin
- Telescope loads immediately for ui-select functionality

## Testing Commands
When making changes, test with:
```bash
nvim --headless -c "checkhealth" -c "qa"
```


