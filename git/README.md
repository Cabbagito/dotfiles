# Git Configuration

Multi-identity git configuration using conditional includes to automatically switch between personal and work profiles.

## How It Works

Git's `includeIf` directive applies configuration conditionally based on repository location:

- **Personal repos**: Uses default identity (`Cabbagito`)
- **Work repos**: Any repo under `~/Documents/holycode/` uses work identity (`Petar`)

The matching happens at git command runtime - no manual switching required.

## Conditional Include

```gitconfig
[includeIf "gitdir:~/Documents/holycode/"]
    path = ~/.config/git/config-work
```

When you run git commands in any repository within `~/Documents/holycode/`, git automatically loads `config-work` and overrides the default user settings.

## Files

| File | Purpose |
|------|---------|
| `config` | Main config with personal identity + conditional include |
| `config-work` | Work identity override (name and email) |

## Adding More Contexts

To add another identity context (e.g., freelance):

1. Create `config-freelance` with `[user]` section
2. Add to main `config`:
   ```gitconfig
   [includeIf "gitdir:~/Documents/freelance/"]
       path = ~/.config/git/config-freelance
   ```
