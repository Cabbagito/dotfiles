# =============================================================================
# POWERLEVEL10K INSTANT PROMPT
# =============================================================================
if [[ -r "${XDG_CACHE_HOME:-$HOME/.cache}/p10k-instant-prompt-${(%):-%n}.zsh" ]]; then
  source "${XDG_CACHE_HOME:-$HOME/.cache}/p10k-instant-prompt-${(%):-%n}.zsh"
fi

# =============================================================================
# CORE SETUP
# =============================================================================
eval "$(/opt/homebrew/bin/brew shellenv)"

export ZSH="$HOME/.oh-my-zsh"
ZSH_THEME="powerlevel10k/powerlevel10k"
plugins=(git fzf zsh-autosuggestions zsh-syntax-highlighting)
source $ZSH/oh-my-zsh.sh

# =============================================================================
# ENVIRONMENT
# =============================================================================
export EDITOR=nvim
export DISABLE_UPDATE_PROMPT=true
export OMZ_DISABLE_UPDATE_WARNING=true
export PATH="$HOME/.local/bin:$PATH"
export PATH="/Users/peki/.antigravity/antigravity/bin:$PATH"

# Bun
export BUN_INSTALL="$HOME/.bun"
export PATH="$BUN_INSTALL/bin:$PATH"
[ -s "/Users/peki/.bun/_bun" ] && source "/Users/peki/.bun/_bun"

# NVM
export NVM_DIR="$HOME/.nvm"
[ -s "$NVM_DIR/nvm.sh" ] && \. "$NVM_DIR/nvm.sh"
[ -s "$NVM_DIR/bash_completion" ] && \. "$NVM_DIR/bash_completion"

# opencode
export PATH=/Users/peki/.opencode/bin:$PATH

# =============================================================================
# TOOLS INIT
# =============================================================================
eval "$(fzf --zsh)"
eval "$(zoxide init zsh)"
eval "$(thefuck --alias)"
source $(brew --prefix)/share/zsh-autocomplete/zsh-autocomplete.plugin.zsh 2>/dev/null || true

# Unbind fzf defaults
bindkey -r '^T'
bindkey -r '^[c'

# =============================================================================
# ALIASES
# =============================================================================
alias c="clear"
alias ll="ls -l"
alias vim="nvim"
alias lg="lazygit"
alias pwdc="pwd | pbcopy"
alias claude-yolo="claude --dangerously-skip-permissions"
alias me='echo "$(whoami)@$(hostname -s)"'
alias this='echo "$(whoami)@$(hostname -s)"'
alias gdu='gdu-go'
alias ff="fastfetch"
alias zk="zellij kill-all-sessions -y; zellij delete-all-sessions -y"
alias zj="zellij kill-session giskard 2>/dev/null; zellij delete-session giskard 2>/dev/null; zellij -s giskard"
alias term='uv run --directory /Users/peki/.config/ghostty term'
alias ghost="cd /Users/peki/Documents/ai/ghost && claude-yolo"
# alias cc="zellij -l cc"
# =============================================================================
# FUNCTIONS
# =============================================================================
# Yazi with directory change on exit
function y() {
  local tmp="$(mktemp -t "yazi-cwd.XXXXXX")"
  yazi "$@" --cwd-file="$tmp"
  if cwd="$(cat -- "$tmp")" && [ -n "$cwd" ] && [ "$cwd" != "$PWD" ]; then
    builtin cd -- "$cwd"
  fi
  rm -f -- "$tmp"
}

function ccc() {
    if zellij list-sessions 2>/dev/null | grep -q "ccc"; then
        zellij attach ccc
    else
        zellij -n ccc -s ccc
    fi
}
# =============================================================================
# DIRECTORY CHANGE HOOKS
# =============================================================================
autoload -Uz add-zsh-hook

auto_activate_venv() {
  if [[ -d .venv && -z "$VIRTUAL_ENV" ]]; then
    source .venv/bin/activate
  fi
}

add-zsh-hook chpwd auto_activate_venv

# =============================================================================
# POWERLEVEL10K CONFIG
# =============================================================================
[[ -f ~/.config/zsh/p10k.zsh ]] && source ~/.config/zsh/p10k.zsh
