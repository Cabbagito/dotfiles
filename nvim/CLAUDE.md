# Neovim Configuration - AI Assistant Context

This file provides guidance to AI assistants working with this Neovim configuration.

## Overview

A modern Neovim configuration using lazy.nvim for plugin management. The setup emphasizes fast startup, transparent backgrounds for terminal integration, and automatic theme syncing with Ghostty terminal.

## Architecture

```
init.lua
    └── lua/config/init.lua (bootstrap)
            ├── options.lua    → Editor settings
            ├── keymaps.lua    → Global keybindings
            ├── autocmds.lua   → Autocommands
            └── lazy.lua       → Plugin manager setup
                    └── lua/plugins/*.lua (plugin specs)
```

### Plugin Organization

| File | Purpose |
|------|---------|
| `colorscheme.lua` | Theme plugins + Ghostty sync logic |
| `coding.lua` | LSP, completion, formatting |
| `navigation.lua` | Telescope, Harpoon, Oil |
| `treesitter.lua` | Syntax highlighting |
| `ui.lua` | Lualine, Alpha dashboard |
| `terminal.lua` | Custom floating terminal |
| `editor.lua` | Editor enhancements |
| `misc.lua` | Other utilities |

## Key Design Decisions

### Ghostty Theme Sync
The most complex integration. Located in `colorscheme.lua`:
1. `ghostty-theme-sync.nvim` plugin reads `~/.config/ghostty/config`
2. `theme_handlers` table maps Ghostty theme names to Neovim colorschemes
3. Fallback chain: handler → direct match → lowercase → base name → catppuccin
4. `:SyncColorscheme` command triggers manual sync
5. Transparency enforced on every colorscheme change via autocmd

### Transparent Backgrounds
`enforce_transparency()` function clears backgrounds for:
- Normal, NormalFloat, NormalNC, SignColumn
- Floating windows (Pmenu*)
- Diagnostic virtual text
- Status lines

### LSP Setup (Mason v2)
- `mason.nvim` + `mason-lspconfig.nvim` for server management
- Servers auto-installed: `lua_ls`, `rust_analyzer`, `pyright`
- Keymaps attached on `LspAttach` event
- Note: LSP keymaps use `<space>` directly, not `<leader>`

### Completion
nvim-cmp with sources:
1. `nvim_lsp` - LSP completions (primary)
2. `luasnip` - Snippets
3. `render-markdown` - Markdown completions
4. `buffer` - Buffer words (fallback)

## Key Customizations

### Options (`lua/config/options.lua`)
```lua
vim.g.mapleader = " "           -- Space as leader
vim.opt.tabstop = 4             -- 4-space tabs
vim.opt.scrolloff = 8           -- Keep 8 lines visible
vim.wo.relativenumber = true    -- Relative line numbers
vim.opt.clipboard = "unnamedplus"  -- System clipboard
```

### Notification Suppression
Only errors are shown; info/warn notifications are suppressed:
```lua
vim.notify = function(msg, log_level, opts)
  if log_level == vim.log.levels.ERROR then
    vim.api.nvim_echo({{msg, "ErrorMsg"}}, true, {})
  end
end
```

### Formatters (none-ls)
- Lua: `stylua`
- Python: `black`, `isort`
- General: `prettier`

## Integration Points

### With Ghostty Terminal
- Colorscheme auto-syncs when `term theme set <name>` runs
- Transparent backgrounds let terminal colors show through
- `<leader>tt` triggers random theme from terminal

### With Shell
- `vim` alias points to `nvim` in `.zshrc`
- `<leader>nv` opens Telescope in nvim config dir
- `<leader>df` opens Telescope in dotfiles dir

## Modification Patterns

### Adding a New Theme
1. Add plugin spec to `lua/plugins/colorscheme.lua`
2. Add handler to `theme_handlers` table if name differs
3. Add lualine mapping to `lualine_themes` table
4. Add dashboard color to `dashboard_colors` table

### Adding a New LSP Server
1. Add to `ensure_installed` in `mason-lspconfig` setup
2. Add `lspconfig.<server>.setup({capabilities = capabilities})` call
3. Optionally add language-specific settings

### Adding Keymaps
- Global: `lua/config/keymaps.lua`
- Plugin-specific: in the plugin's config function
- LSP-specific: in the `LspAttach` callback

### Adding Plugins
Create or edit file in `lua/plugins/`:
```lua
return {
  {
    "author/plugin-name",
    event = "VeryLazy",  -- or other lazy-loading trigger
    config = function()
      require("plugin").setup({})
    end,
  },
}
```

## Testing Changes

```bash
# Check for errors
nvim --headless -c "checkhealth" -c "qa"

# Verify plugins load
nvim --headless -c "Lazy" -c "qa"

# Test colorscheme sync
nvim -c "SyncColorscheme"
```

## Common Issues

### Theme not syncing
1. Check Ghostty config has `theme = <name>` line
2. Verify handler exists in `theme_handlers`
3. Run `:SyncColorscheme` manually

### LSP not starting
1. Run `:Mason` to check server installation
2. Run `:LspInfo` to see active servers
3. Check `:checkhealth lsp`

### Transparency not working
- Ensure terminal supports transparency
- Check `enforce_transparency()` is called after colorscheme change
