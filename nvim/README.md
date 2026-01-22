# My Neovim Configuration

A highly customized Neovim configuration focused on modern development workflows with Lua-based configuration.

## Features

- **Package Management**: Lazy.nvim for fast plugin loading
- **LSP Integration**: Full LSP support with Mason v2 for language server management
- **Fuzzy Finding**: Telescope for file/text searching and navigation (with ui-select for better prompts)
- **File Management**: Oil.nvim for efficient file operations
- **Syntax Highlighting**: Treesitter for advanced syntax highlighting
- **Code Completion**: nvim-cmp with multiple sources
- **Terminal Integration**: Custom floating terminal with `<C-t><C-t>`
- **Multiple Themes**: Catppuccin (primary), Tokyonight, Everforest, Edge, Sonokai
- **Status Line**: Lualine with custom configuration
- **Code Formatting**: none-ls for formatting and linting
- **Navigation**: Harpoon for quick file switching

## Installation

### Quick Setup (Recommended)

Clone directly to your Neovim config directory:

```bash
# Backup existing config (optional)
mv ~/.config/nvim ~/.config/nvim.backup

# Clone this config
git clone https://github.com/Cabbagito/i_use_neovim_btw ~/.config/nvim

# Start Neovim (plugins will auto-install)
nvim
```

### Manual Setup

```bash
# Clone to any directory
git clone https://github.com/Cabbagito/i_use_neovim_btw

# Copy to Neovim config directory
cp -r i_use_neovim_btw/* ~/.config/nvim/

# Start Neovim
nvim
```

## Key Features & Keybindings

### Leader Key
- `<space>` - Leader key for most commands
- Note: LSP commands use `<space>` directly (not `<leader>`)

### File Navigation
- `<leader>ff` - Find files
- `<leader>fw` - Find word (live grep)
- `<leader>fb` - Find buffers
- `<leader>fr` - Find recent files
- `<leader>nv` - Find Neovim config files
- `<leader>df` - Find dotfiles
- `-` - Open Oil.nvim file manager

### Code Navigation
- `<leader>cs` - Find colorscheme
- `<leader>ft` - Find TODOs
- `gd` - Go to definition
- `gr` - Go to references
- `K` - Hover documentation

### Harpoon (Quick Navigation)
- `<leader>a` - Add file to Harpoon
- `<C-e>` - Open Harpoon menu
- `<C-1>` to `<C-4>` - Jump to Harpoon marks 1-4

### Terminal
- `<C-t><C-t>` - Toggle floating terminal
- `<Esc>` - Exit terminal mode

### LSP & Formatting
- `<space>fm` - Format current file
- `<space>rn` - Rename symbol
- `<space>ca` - Code actions
- `<space>D` - Type definition
- `<space>wa` - Add workspace folder
- `<space>wr` - Remove workspace folder
- `<space>wl` - List workspace folders

### Other
- `<leader>hs` - Open homescreen
- `<leader>tw` - Toggle twilight (focus mode)
- `<leader>fd` - Toggle diagnostics (Trouble)

## Configuration Structure

```
├── init.lua                # Minimal entry point
├── lazy-lock.json          # Plugin lockfile
├── CLAUDE.md              # Notes for AI assistants
├── .gitignore             # Git ignore rules
└── lua/
    ├── config/            # Core configuration
    │   ├── init.lua       # Bootstrap loader
    │   ├── lazy.lua       # Lazy.nvim setup
    │   ├── options.lua    # Neovim options
    │   ├── keymaps.lua    # Global keymaps
    │   └── autocmds.lua   # Autocommands
    └── plugins/           # Plugin specifications
        ├── colorscheme.lua # Theme plugins
        ├── ui.lua         # UI plugins (lualine, alpha)
        ├── editor.lua     # Editor enhancements
        ├── navigation.lua # Telescope, Harpoon, Oil
        ├── treesitter.lua # Syntax highlighting
        ├── coding.lua     # LSP, completion, formatting
        ├── terminal.lua   # Custom terminal
        └── misc.lua       # Other plugins
```

## Customization

This configuration is designed to be easily customizable:

1. **Themes**: Change theme in `lua/plugins/colorscheme.lua`
2. **Keymaps**: Modify keybindings in `lua/config/keymaps.lua`
3. **Plugins**: Add/remove plugins in appropriate files under `lua/plugins/`
4. **LSP**: Configure language servers in `lua/plugins/coding.lua`
5. **Options**: Adjust editor settings in `lua/config/options.lua`

## Requirements

- Neovim 0.11.2+ (for Mason v2 compatibility)
- Git
- A Nerd Font (for icons)
- ripgrep (for Telescope live grep)
- Node.js (for some LSP servers)
- make/gcc (for telescope-fzf-native)

## Language Support

Pre-configured LSP servers:
- **Lua** - lua_ls (with Neovim-specific settings)
- **Python** - pyright
- **Rust** - rust_analyzer (with rust-tools.nvim)

Additional servers can be installed via `:Mason`


