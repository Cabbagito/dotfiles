#!/bin/bash

# Dotfiles Installation Script
# Creates symlinks from home directory to config files

set -e

DOTFILES_DIR="${HOME}/.config"
BACKUP_DIR="${HOME}/.dotfiles-backup-$(date +%Y%m%d-%H%M%S)"

# Colors for output
RED='\033[0;31m'
GREEN='\033[0;32m'
YELLOW='\033[1;33m'
NC='\033[0m' # No Color

info() { echo -e "${GREEN}[INFO]${NC} $1"; }
warn() { echo -e "${YELLOW}[WARN]${NC} $1"; }
error() { echo -e "${RED}[ERROR]${NC} $1"; }

# =============================================================================
# BACKUP FUNCTION
# =============================================================================
backup_if_exists() {
    local file=$1
    if [[ -e "$file" && ! -L "$file" ]]; then
        mkdir -p "$BACKUP_DIR"
        mv "$file" "$BACKUP_DIR/"
        warn "Backed up existing $file to $BACKUP_DIR/"
    elif [[ -L "$file" ]]; then
        rm "$file"
    fi
}

# =============================================================================
# SYMLINK FUNCTION
# =============================================================================
create_symlink() {
    local source=$1
    local target=$2

    backup_if_exists "$target"
    ln -s "$source" "$target"
    info "Linked $target -> $source"
}

# =============================================================================
# MAIN INSTALLATION
# =============================================================================
echo ""
echo "========================================"
echo "  Dotfiles Installation"
echo "========================================"
echo ""

# Check if running from correct directory
if [[ ! -f "${DOTFILES_DIR}/README.md" ]]; then
    error "Please clone the dotfiles to ~/.config first"
    exit 1
fi

# Create symlinks for home directory files
info "Creating symlinks..."

# .zshrc
create_symlink "${DOTFILES_DIR}/zsh/.zshrc" "${HOME}/.zshrc"

# Claude Code settings (create .claude dir if needed)
mkdir -p "${HOME}/.claude"
create_symlink "${DOTFILES_DIR}/claude/settings.json" "${HOME}/.claude/settings.json"
create_symlink "${DOTFILES_DIR}/claude/statusline-command.sh" "${HOME}/.claude/statusline-command.sh"

# =============================================================================
# HOMEBREW DEPENDENCIES
# =============================================================================
echo ""
info "Checking Homebrew dependencies..."

BREW_PACKAGES=(
    neovim
    ghostty
    zellij
    fzf
    ripgrep
    zoxide
    lazygit
    thefuck
    fastfetch
    btop
    jq
    uv
)

BREW_CASKS=(
    font-jetbrains-mono-nerd-font
)

install_brew_packages() {
    for pkg in "${BREW_PACKAGES[@]}"; do
        if ! brew list "$pkg" &>/dev/null; then
            info "Installing $pkg..."
            brew install "$pkg"
        else
            info "$pkg already installed"
        fi
    done
}

install_brew_casks() {
    for cask in "${BREW_CASKS[@]}"; do
        if ! brew list --cask "$cask" &>/dev/null; then
            info "Installing $cask..."
            brew install --cask "$cask"
        else
            info "$cask already installed"
        fi
    done
}

if command -v brew &>/dev/null; then
    read -p "Install Homebrew packages? [y/N] " -n 1 -r
    echo
    if [[ $REPLY =~ ^[Yy]$ ]]; then
        install_brew_packages
        install_brew_casks
    fi
else
    warn "Homebrew not found. Install from https://brew.sh/"
fi

# =============================================================================
# OH MY ZSH
# =============================================================================
echo ""
info "Checking Oh My Zsh..."

if [[ ! -d "${HOME}/.oh-my-zsh" ]]; then
    read -p "Install Oh My Zsh? [y/N] " -n 1 -r
    echo
    if [[ $REPLY =~ ^[Yy]$ ]]; then
        sh -c "$(curl -fsSL https://raw.githubusercontent.com/ohmyzsh/ohmyzsh/master/tools/install.sh)" "" --unattended
    fi
else
    info "Oh My Zsh already installed"
fi

# Powerlevel10k
P10K_DIR="${ZSH_CUSTOM:-${HOME}/.oh-my-zsh/custom}/themes/powerlevel10k"
if [[ ! -d "$P10K_DIR" ]]; then
    info "Installing Powerlevel10k..."
    git clone --depth=1 https://github.com/romkatv/powerlevel10k.git "$P10K_DIR"
fi

# Zsh plugins
ZSH_CUSTOM="${ZSH_CUSTOM:-${HOME}/.oh-my-zsh/custom}"
PLUGINS=(
    "zsh-users/zsh-autosuggestions"
    "zsh-users/zsh-syntax-highlighting"
)

for plugin in "${PLUGINS[@]}"; do
    plugin_name=$(basename "$plugin")
    plugin_dir="${ZSH_CUSTOM}/plugins/${plugin_name}"
    if [[ ! -d "$plugin_dir" ]]; then
        info "Installing $plugin_name..."
        git clone "https://github.com/${plugin}.git" "$plugin_dir"
    fi
done

# =============================================================================
# GHOSTTY TERM CLI
# =============================================================================
echo ""
info "Setting up Ghostty term CLI..."

if command -v uv &>/dev/null; then
    cd "${DOTFILES_DIR}/ghostty"
    if [[ ! -d ".venv" ]]; then
        uv venv
        uv pip install -e .
        info "Ghostty term CLI installed"
    else
        info "Ghostty term CLI already set up"
    fi
    cd - >/dev/null
else
    warn "uv not found. Install with: brew install uv"
fi

# =============================================================================
# COMPLETION
# =============================================================================
echo ""
echo "========================================"
echo "  Installation Complete!"
echo "========================================"
echo ""
info "Next steps:"
echo "  1. Restart your terminal or run: source ~/.zshrc"
echo "  2. Open Neovim to install plugins: nvim"
echo "  3. Test the term command: term"
echo "  4. Try a zellij layout: zellij -l claude-3"
echo ""

if [[ -d "$BACKUP_DIR" ]]; then
    warn "Backups saved to: $BACKUP_DIR"
fi
