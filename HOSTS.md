# Hosts

Machines this dotfiles repo is deployed to. See [CLAUDE.md](CLAUDE.md) for the high-level architecture.

## Identifying the current host

```sh
this          # alias → whoami@hostname -s
me            # same
hostname -s   # raw
uname -s      # Darwin | Linux
ff            # fastfetch — OS, model, kernel
```

## giskard

| | |
|---|---|
| Role | Primary dev laptop |
| OS | macOS Tahoe 26.3.1 (Darwin 25.3.0, arm64) |
| Model | MacBook Pro 14-inch, 2024 (Apple Silicon) |
| Shell | zsh + oh-my-zsh + powerlevel10k |
| Package manager | Homebrew at `/opt/homebrew` |
| Home | `/Users/peki` |
| WM | native macOS |
| Notable tools | bun (`$HOME/.bun`), opencode (`$HOME/.opencode`), antigravity (`$HOME/.antigravity`), nvm (`$HOME/.nvm`), uv |

## parker

| | |
|---|---|
| Role | Desktop |
| OS | Omarchy (Arch Linux base) |
| Package manager | pacman (+ AUR) |
| Home | `/home/peki` |
| Brew | absent, or `/home/linuxbrew/.linuxbrew` if installed |
| WM | Hyprland (Omarchy default) |

*Fill in model, kernel, and tool list from parker directly — run `ff` there and paste.*

## Shared vs host-specific inventory

Fully portable today (land on any host via `git pull`):

- `nvim/`, `zellij/`, `git/`, `lazygit/`, `btop/`, `fastfetch/`, `claude/`, `zed/`
- `ghostty/` mostly — theme manager CLI is pure Python/uv

Known host-specific surface still present in shared files:

| Location | What | Notes |
|---|---|---|
| `ghostty/config` | `macos-titlebar-style`, `macos-non-native-fullscreen` | Ignored on Linux but shows as unknown keys |
| `zsh/.zshrc` `pwdc` | `pbcopy` | macOS only. On Wayland use `wl-copy`, on X11 `xclip -selection clipboard` |
| `zsh/.zshrc` `ghost` | `cd /Users/peki/Documents/projects/ghost` | Absolute, user-specific; path may not exist on parker |

Already made portable (Phase 1):

- `$HOME` substituted for `/Users/peki` throughout `.zshrc` (bun, opencode, antigravity, term CLI)
- `zj` session name now derived from `hostname -s`, not hardcoded `giskard`
- `brew shellenv` guarded — tries `/opt/homebrew`, falls back to `/home/linuxbrew/.linuxbrew`, silently skips if neither exists

## Sync workflow

1. On each machine: `git pull` — safe for portable configs.
2. If you edit a file that has per-host bits, prefer adding a runtime check (e.g. `[[ "$OSTYPE" == darwin* ]]`) over forking the file.
3. Secrets/runtime dirs (`gh/`, `hcloud/`, `cagent/`, etc.) are in `.gitignore` — they stay local per machine.
4. Host-specific extras that must differ per machine → Phase 2 (fragment files under `zsh/hosts/<name>.zsh`). Not needed yet.

## Phase 2 candidates (not done yet)

- Split `.zshrc` into shared + `hosts/giskard.zsh` / `hosts/parker.zsh` + `os/darwin.zsh` / `os/linux.zsh`
- Platform-conditional `ghostty/config` (via `config-file = ./config.<os>` include)
- Cross-platform clipboard wrapper (replace bare `pbcopy` alias)
- `install.sh` Linux branch + per-host symlink selection
- Add parker-only configs to repo (hypr, waybar, etc.) once parker is inventoried
